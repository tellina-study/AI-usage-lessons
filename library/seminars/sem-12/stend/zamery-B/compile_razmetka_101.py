"""Сборка корпуса-101: сорок снимков первого круга + 61 снимок добора.

Вход:
  razmetka.json                 — компиляция `plan-peredelki/razmetka-B.md` (40 в корпусе),
                                  автор разметки — сессия планирования A/B/C;
  razmetka-dobor.md (+part2)    — разметка добора, автор — ЭТА сессия;
  dobor-vybrannye.json          — лицензия/автор/ссылка/sha256 на каждый добранный снимок.

Выход: razmetka-101.json. У каждой записи стоит `razmetka_author` — «planner» или
«dobor»: именно по нему замер кейса B считает покрытие ДВУМЯ знаменателями раздельно
(чужая разметка против своей). Смешивать их в один процент нельзя: в первом случае
автор разметки и судья покрытия — разные сессии, во втором одна.

Запуск:  python3 compile_razmetka_101.py
"""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
HEADER_RE = re.compile(r"^### (?P<id>[0-9a-f]{16}) — (?P<rest>.+)$")
GROUP_RE = re.compile(r"^## Группа (?P<gid>G\d+) — (?P<name>.+)$")


def parse_dobor():
    meta = {r["id"]: r for r in json.loads((HERE / "dobor-vybrannye.json").read_text(encoding="utf-8"))}
    entries, cur, gid, rest, body = [], None, None, None, []

    def flush():
        nonlocal cur, body
        if cur is None:
            body = []
            return
        items, acc = [], None
        for raw in body:
            if not raw.strip():
                continue
            if re.match(r"^\d+\.\s", raw):
                if acc is not None:
                    items.append(acc.strip())
                acc = re.sub(r"^\d+\.\s", "", raw).rstrip()
            elif raw.startswith(("   ", "\t")) or not raw.startswith(("#", "**", "-")):
                if acc is not None:          # продолжение строки, НЕ новый пункт (ловушка круга 1)
                    acc = acc.rstrip() + " " + raw.strip()
        if acc is not None:
            items.append(acc.strip())
        m = meta.get(cur, {})
        deck = re.search(r"дека: (ДА|да|НЕТ)\s*(\(([^)]*)\))?", rest)
        entries.append({
            "id": cur, "group": gid, "in_corpus": rest.startswith("корпус: ДА"),
            "deck_allowed": bool(deck and deck.group(1) in ("ДА", "да")),
            "deck_reason": deck.group(3) if deck else None,
            "also_tags": ["ТРУДНЫЙ НЕГАТИВ"] if "ТРУДНЫЙ НЕГАТИВ" in rest else
                         (["ДВУСМЫСЛЕННОСТЬ КЛАССА"] if "ДВУСМЫСЛЕННОСТЬ" in rest else []),
            "excluded_reason": None, "what_is_visible": items,
            "license": m.get("license"), "author": m.get("author"), "landing": m.get("landing"),
            "s3_url": m.get("s3_url"), "sha256_downloaded": m.get("sha256_downloaded"),
            "oiv_class": m.get("oiv_class"), "subset": m.get("subset"),
            "razmetka_author": "dobor",
        })
        body = []

    for f in ("razmetka-dobor.md", "razmetka-dobor-part2.md"):
        for raw in (HERE / f).read_text(encoding="utf-8").splitlines():
            g = GROUP_RE.match(raw)
            if g:
                flush(); cur = None; gid = g.group("gid"); continue
            h = HEADER_RE.match(raw)
            if h:
                flush(); cur = h.group("id"); rest = h.group("rest"); continue
            if cur is not None:
                body.append(raw)
        flush(); cur = None
    return entries


def main():
    old = json.loads((HERE / "razmetka.json").read_text(encoding="utf-8"))
    base = []
    for e in old["entries"]:
        e = dict(e); e["razmetka_author"] = "planner"; base.append(e)
    new = parse_dobor()
    seen = {e["id"] for e in base}
    dup = [e["id"] for e in new if e["id"] in seen]
    if dup:
        raise SystemExit(f"добор пересекается с корпусом-40: {dup}")
    allе = base + new
    in_corpus = [e for e in allе if e["in_corpus"]]
    doc = {
        "date": "2026-11-24",
        "corpus_size": len(in_corpus),
        "by_razmetka_author": {
            "planner": sum(1 for e in in_corpus if e["razmetka_author"] == "planner"),
            "dobor": sum(1 for e in in_corpus if e["razmetka_author"] == "dobor"),
        },
        "sources": [
            "library/seminars/sem-12/plan-peredelki/razmetka-B.md (40, автор — планировщик A/B/C)",
            "library/seminars/sem-12/stend/zamery-B/razmetka-dobor.md (+part2) (61, автор — сессия добора)",
        ],
        "entries": allе,
    }
    (HERE / "razmetka-101.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    lines = sum(len(e["what_is_visible"]) for e in in_corpus)
    print(f"в корпусе {len(in_corpus)} "
          f"(planner {doc['by_razmetka_author']['planner']} + dobor {doc['by_razmetka_author']['dobor']})")
    print(f"строк «что видно» всего: {lines}; пустых записей: "
          f"{sum(1 for e in in_corpus if not e['what_is_visible'])}")
    from collections import Counter
    c = Counter(e["group"] for e in in_corpus)
    print("по группам:", ", ".join(f"{k}={c[k]}" for k in sorted(c, key=lambda x: int(x[1:]))))
    bad = [e["id"] for e in in_corpus if not e.get("license")]
    print("без лицензии:", len(bad))


if __name__ == "__main__":
    main()
