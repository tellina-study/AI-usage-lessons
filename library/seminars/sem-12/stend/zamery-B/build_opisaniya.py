#!/usr/bin/env python3
"""Собирает именованный выход кейса B для кейса D — `opisaniya.json`:
на каждый id корпуса (40) — свободный рассказ, YOLO-теги, поля по схеме,
имя модели и дословный промт каждого метода (план кейса B §5 / план кейса
D §3,§7).

Печатает СЧЁТ, а не просто «готово» (требование оркестратора 2026-11-24,
после случая прошлого круга — «файл выглядел целым, были не все векторы»):
сколько записей всего, сколько непустых по каждому методу ОТДЕЛЬНО, и
журнал отказов с кодами. Если непустых меньше числа в корпусе — выход
НЕ считается готовым для передачи, скрипт говорит об этом явно в stdout
(решение — за человеком, не тихий автосброс).

Запуск:  python3 build_opisaniya.py
"""
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAZMETKA = HERE / "razmetka.json"
YOLO = HERE / "raw_yolo_results.json"
VISION = HERE / "raw" / "vision_results.json"
OUT = HERE / "opisaniya.json"


def main():
    razmetka = json.loads(RAZMETKA.read_text(encoding="utf-8"))
    ids = [e["id"] for e in razmetka["entries"] if e["in_corpus"]]
    groups = {e["id"]: e["group"] for e in razmetka["entries"] if e["in_corpus"]}
    n = len(ids)
    print(f"корпус (razmetka.json, in_corpus=true): {n} id")

    yolo_doc = json.loads(YOLO.read_text(encoding="utf-8")) if YOLO.exists() else None
    if not VISION.exists():
        raise SystemExit(
            f"НЕТ {VISION} — vision-методы (рассказ/поля) ещё не получены. "
            f"Собирать opisaniya.json рано (см. журнал: прогон передан "
            f"сессии s12-plan-abc-tri-keysa, ждём коммит)."
        )
    vision_doc = json.loads(VISION.read_text(encoding="utf-8"))

    by_id_variant = {}
    for r in vision_doc["results"]:
        by_id_variant[(r["id"], r["variant"])] = r

    entries = []
    fail_codes = Counter()
    nonempty = {"caption": 0, "fields": 0, "yolo": 0}

    for i in ids:
        cap = by_id_variant.get((i, "caption"))
        fld = by_id_variant.get((i, "fields"))
        yt = (yolo_doc["results"].get(i) if yolo_doc else None) or {}

        cap_text = (cap or {}).get("content")
        fld_parsed = (fld or {}).get("parsed")
        fld_raw = (fld or {}).get("content")
        yolo_tags = yt.get("tags", [])

        if cap_text:
            nonempty["caption"] += 1
        else:
            code = (cap or {}).get("raw_error") or (cap or {}).get("error") or "MISSING"
            fail_codes[f"caption:{code}"] += 1

        if fld_parsed:
            nonempty["fields"] += 1
        else:
            code = (fld or {}).get("raw_error") or (fld or {}).get("error") or (
                "PARSE_FAIL" if fld_raw else "MISSING")
            fail_codes[f"fields:{code}"] += 1

        if yolo_tags or (yt and "tags" in yt):
            nonempty["yolo"] += 1
        else:
            fail_codes["yolo:MISSING"] += 1

        entries.append({
            "id": i,
            "group": groups[i],
            "caption": cap_text,
            "fields": fld_parsed,
            "fields_raw": None if fld_parsed else fld_raw,
            "yolo_tags": yolo_tags,
        })

    doc = {
        "date": "2026-11-24",
        "corpus_size": n,
        "methods": {
            "caption": {
                "model": vision_doc["model"],
                "system_prompt": vision_doc["sys_caption"],
                "user_prompt": vision_doc["user_caption"],
            },
            "fields": {
                "model": vision_doc["model"],
                "system_prompt": vision_doc["sys_fields"],
                "user_prompt": vision_doc["user_fields"],
            },
            "yolo": {
                "model": yolo_doc["model"] if yolo_doc else None,
                "conf_threshold": yolo_doc["conf_threshold"] if yolo_doc else None,
                "vocab": yolo_doc["vocab"] if yolo_doc else None,
                "prompt": None,
                "note": "детерминированный детектор общего назначения, не LLM — промта нет",
            },
        },
        "entries": entries,
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"\nвсего записей: {len(entries)}")
    for k, v in nonempty.items():
        flag = "OK" if v == n else "НЕХВАТКА"
        print(f"  {k}: непустых {v}/{n}  [{flag}]")
    if fail_codes:
        print("журнал отказов:")
        for code, cnt in fail_codes.most_common():
            print(f"  {code}: {cnt}")
    ready = all(v == n for v in nonempty.values())
    print(f"\n{'ГОТОВ к передаче D' if ready else 'НЕ ГОТОВ — есть нехватка, см. выше'}: {OUT}")


if __name__ == "__main__":
    main()
