"""Добор фотокорпуса B/D с 40 до ~100 снимков (issue #351, круг 3, веха 1).

Детерминированный отбор кандидатов из Open Images V7 по человеческим пометкам
(`*-annotations-human-imagelabels.csv`, Confidence=1) и выгрузка лицензионных
данных из `*-images-with-rotation.csv`. Ничего не выбирает «на глаз»: порядок —
лексикографический по id внутри класса, поэтому повторный запуск даёт тот же
список. Курация глазами идёт ПОСЛЕ загрузки, её результат — `razmetka-dobor.md`.

ЛОВУШКА, на которой эта сессия сама поймалась (в журнал): поле Confidence в
этих же файлах записано ДВУМЯ способами — `1` и `1.0`. Фильтр `== "1"` даёт
правдоподобный, но ложный ответ: по нему выходит, что у классов Lecture /
Seminar / Conference hall / Public speaking / Library подтверждённых человеком
позитивов НЕТ ВОВСЕ (на самом деле 162 / 93 / 69 / 86 / 181). Сравнивать
только числом: `float(c) == 1.0`.

Лицензия: берётся из `License` CSV набора и проверяется на каждый снимок —
в корпус попадает только CC BY 2.0 (курс публикуется открыто).

Запуск:  python3 fetch_dobor.py            # отбор + метаданные + загрузка
         python3 fetch_dobor.py --plan      # только отбор, без сети
Кэш аннотаций: /tmp/s12-corpora/oiv7  (качается fetch_korpus.py планировщика)
"""
import csv, hashlib, json, os, sys, urllib.request
import concurrent.futures as cf
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
OIV = Path("/tmp/s12-corpora/oiv7")
DEST = HERE / "corpus-cache"
OUT_META = HERE / "dobor-manifest.json"

# Группа -> (классы Open Images, сколько НОВЫХ снимков нужно в корпус).
# G1..G8 — существующие группы корпуса-40 (добор вглубь), G9..G12 — новые
# смысловые группы: они дают кейсу D ещё четыре набора «похожих, но не тех»
# и чинят мини-группу G7 из двух членов (слабость, названная в razmetka-B.md).
GROUPS = [
    ("G1",  "учебный класс / занятие",        ["Classroom"],               4),
    ("G2",  "лекция / доклад в аудитории",    ["Lecture"],                 5),
    ("G3",  "семинар с экраном",              ["Seminar"],                 3),
    ("G4",  "залы",                           ["Conference hall"],         3),
    ("G5",  "выступление с микрофоном",       ["Public speaking"],         4),
    ("G6",  "рабочая встреча / совещание",    ["Meeting"],                 3),
    ("G7",  "у доски",                        ["Whiteboard", "Blackboard"],7),
    ("G8",  "кружки и кофе",                  ["Coffee cup", "Mug"],       4),
    ("G9",  "библиотека / читальный зал",     ["Library"],                 8),
    ("G10", "лаборатория / практикум",        ["Laboratory"],              8),
    ("G11", "мастерская / воркшоп",           ["Workshop"],                8),
    ("G12", "аудитория-амфитеатр",            ["Auditorium"],              8),
]
OVERSAMPLE = 3  # кандидатов на один нужный снимок — курация глазами отбраковывает

CC_BY_20 = "https://creativecommons.org/licenses/by/2.0/"


def used_ids():
    """id, уже занятые корпусом-40 и срезами C — не предлагать повторно."""
    used = set()
    man = HERE.parent.parent / "plan-peredelki" / "korpus" / "manifest-foto-BC.json"
    for r in json.loads(man.read_text(encoding="utf-8")):
        used.add(r["id"])
    raz = json.loads((HERE / "razmetka.json").read_text(encoding="utf-8"))
    for e in raz["entries"]:
        used.add(e["id"])
    return used


def class_codes():
    return {r["DisplayName"]: r["LabelName"]
            for r in csv.DictReader(open(OIV / "oidv7-class-descriptions.csv"))}


def positives(names):
    """{DisplayName: [(id, subset), ...]} — только Confidence == 1.0."""
    codes = class_codes()
    want = {codes[n]: n for n in names if n in codes}
    missing = [n for n in names if n not in codes]
    if missing:
        raise SystemExit(f"классов нет в словаре Open Images: {missing}")
    pos = defaultdict(set)
    for f, sub in (("oidv7-val-annotations-human-imagelabels.csv", "validation"),
                   ("oidv7-test-annotations-human-imagelabels.csv", "test")):
        with open(OIV / f) as fh:
            for i, row in enumerate(csv.reader(fh)):
                if i == 0:
                    continue
                if row[2] in want and float(row[3]) == 1.0:   # НЕ row[3] == "1"
                    pos[want[row[2]]].add((row[0], sub))
    return {k: sorted(v) for k, v in pos.items()}


def meta_for(ids):
    """Лицензия/автор/ссылка из CSV набора — по снимку, не по набору целиком."""
    need = set(i for i, _ in ids)
    out = {}
    for f in ("validation-images-with-rotation.csv", "test-images-with-rotation.csv"):
        with open(OIV / f) as fh:
            for row in csv.DictReader(fh):
                if row["ImageID"] in need:
                    out[row["ImageID"]] = {
                        "license": row["License"],
                        "author": row["Author"],
                        "landing": row["OriginalLandingURL"],
                        "title": row["Title"],
                        "subset": row["Subset"],
                    }
    return out


def main():
    plan_only = "--plan" in sys.argv
    used = used_ids()
    all_names = sorted({n for _, _, ns, _ in GROUPS for n in ns})
    pos = positives(all_names)
    print("подтверждённых человеком позитивов по классу:")
    for n in all_names:
        print(f"  {n:18s} {len(pos.get(n, []))}")

    picked = []          # (gid, gname, cls, id, subset)
    for gid, gname, names, need in GROUPS:
        want = need * OVERSAMPLE
        got = []
        # круговая выборка по классам группы, чтобы G7/G8 не ушли целиком в один класс
        pools = [[c for c in pos.get(n, []) if c[0] not in used] for n in names]
        k = 0
        while len(got) < want and any(pools):
            for ni, pool in enumerate(pools):
                if not pool or len(got) >= want:
                    continue
                iid, sub = pool.pop(0)
                if iid in used:
                    continue
                used.add(iid)
                got.append((gid, gname, names[ni], iid, sub))
            k += 1
            if k > want + 10:
                break
        picked.extend(got)
        print(f"{gid:4s} {gname:30s} нужно {need}, кандидатов отобрано {len(got)}")

    meta = meta_for([(p[3], p[4]) for p in picked])
    recs, no_meta, wrong_lic = [], [], []
    for gid, gname, cls, iid, sub in picked:
        m = meta.get(iid)
        if not m:
            no_meta.append(iid)
            continue
        if m["license"] != CC_BY_20:
            wrong_lic.append((iid, m["license"]))
            continue
        recs.append({
            "id": iid, "group": gid, "group_name": gname, "oiv_class": cls,
            "subset": m["subset"], "license": m["license"], "author": m["author"],
            "landing": m["landing"], "title": m["title"],
            "s3_url": f"https://open-images-dataset.s3.amazonaws.com/{m['subset']}/{iid}.jpg",
        })
    print(f"\nкандидатов всего {len(picked)}; без метаданных {len(no_meta)}; "
          f"лицензия НЕ CC BY 2.0 {len(wrong_lic)}; годных {len(recs)}")
    for iid, lic in wrong_lic[:10]:
        print("  иная лицензия:", iid, lic)

    if plan_only:
        OUT_META.write_text(json.dumps(recs, ensure_ascii=False, indent=1), encoding="utf-8")
        print("план записан в", OUT_META.name, "— сеть не трогалась")
        return

    DEST.mkdir(exist_ok=True)

    def one(r):
        p = DEST / f"{r['id']}.jpg"
        if p.exists():
            r["sha256_downloaded"] = hashlib.sha256(p.read_bytes()).hexdigest()
            r["bytes"] = p.stat().st_size
            return (r["id"], "cached")
        try:
            req = urllib.request.Request(r["s3_url"], headers={"User-Agent": "curl/8"})
            data = urllib.request.urlopen(req, timeout=40).read()
        except Exception as e:
            r["fetch_error"] = str(e)
            return (r["id"], f"ОШИБКА {e}")
        p.write_bytes(data)
        r["sha256_downloaded"] = hashlib.sha256(data).hexdigest()
        r["bytes"] = len(data)
        return (r["id"], f"ok {len(data)}")

    with cf.ThreadPoolExecutor(8) as ex:
        res = list(ex.map(one, recs))
    ok = [r for r in res if not r[1].startswith("ОШИБКА")]
    bad = [r for r in res if r[1].startswith("ОШИБКА")]
    print(f"скачано/в кэше: {len(ok)}/{len(recs)}; отсутствует в бакете: {len(bad)}")
    for i, s in bad:
        print("  ", i, s)
    OUT_META.write_text(json.dumps(recs, ensure_ascii=False, indent=1), encoding="utf-8")
    print("манифест добора:", OUT_META.name)


if __name__ == "__main__":
    main()
