#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Семинар 12, Кейс D (issue #351) — сборка единого файла запросов.

Источники (не правятся этим скриптом, только читаются — чужая зона):
- `zamery-B/zaprosy-klass1-finalizirovano.md` (коммит 9aa911a1ef, ветка
  hc/s12-keys-b-fotografii-406f51fe) — класс 1, финализированный по реальной
  лексике рассказов кейса B (таблица §1 — RU, таблица §3 — EN + ответ).
- `plan-peredelki/zaprosy-B.md` (issue-351-seminars-12-13-kartinki @ 1dc6d8044f)
  — классы 2 и 3, финальны с самого начала (не зависят от описаний).

Производное — не правится руками (канон §8.5): `zaprosy_full.json` всегда
пересобирается этим скриптом из двух источников выше.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ZB = HERE.parent / "zamery-B"
PLAN = HERE.parent.parent / "plan-peredelki"

sys.path.insert(0, str(HERE))
from corpus_b import corpus_ids, short_id_map, resolve_id  # noqa: E402

OUT = HERE / "zaprosy_full.json"


def table_rows(text, num_prefix, n_cols):
    """Строки markdown-таблицы, где первая ячейка начинается с num_prefix
    (например '1.'), независимо от того, в какой именно таблице файла они
    стоят — устойчиво к любому числу таблиц до/после."""
    out = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) != n_cols:
            continue
        if not re.match(rf"{re.escape(num_prefix)}\d+\b", cells[0]):
            continue
        out.append(cells)
    return out


def build_class1():
    ru_text = (ZB / "zaprosy-klass1-finalizirovano.md").read_text(encoding="utf-8")
    ru_rows = table_rows(ru_text, "1.", 4)  # №|Было|Стало|Почему
    ru_map = {}
    for r in ru_rows:
        m = re.match(r"1\.(\d+)", r[0])
        num = int(m.group(1))
        ru_map[num] = r[2]  # "Стало (по факту рассказа)"

    en_rows = table_rows(ru_text, "1.", 3)  # №|EN|Ответ (§3)
    out = []
    for r in en_rows:
        m = re.match(r"1\.(\d+)", r[0])
        num = int(m.group(1))
        if num not in ru_map:
            continue
        out.append({
            "num": f"1.{num}",
            "class": 1,
            "class_name": "К-слово",
            "ru": ru_map[num],
            "en": r[1],
            "answer": r[2],
        })
    out.sort(key=lambda x: int(x["num"].split(".")[1]))
    return out


def build_class23():
    text = (PLAN / "zaprosy-B.md").read_text(encoding="utf-8")

    def rows_for(num_prefix, cls, cls_name):
        rows = table_rows(text, num_prefix, 5)
        out = []
        for r in rows:
            out.append({
                "num": r[0],
                "class": cls,
                "class_name": cls_name,
                "ru": r[1],
                "en": r[2],
                "answer": r[3],
                "hard_negatives": [x.strip() for x in r[4].split(",")],
            })
        return out

    c2 = rows_for("2.", 2, "К-пересказ")
    c3 = rows_for("3.", 3, "К-деталь")
    return c2, c3


def main():
    c1 = build_class1()
    c2, c3 = build_class23()
    all_q = c1 + c2 + c3
    print(f"класс 1: {len(c1)}  класс 2: {len(c2)}  класс 3: {len(c3)}  итого: {len(all_q)}")
    assert len(c1) == 12 and len(c2) == 12 and len(c3) == 14, "число запросов не совпало с планом (38)"

    # таблицы называют ответы короткими 8-символьными префиксами id Open
    # Images; корпус хранит полные id — разрешаем раз и для всех веток.
    smap = short_id_map(corpus_ids())
    for q in all_q:
        q["answer"] = resolve_id(q["answer"], smap)
        if "hard_negatives" in q:
            q["hard_negatives"] = [resolve_id(h, smap) for h in q["hard_negatives"]]

    doc = {
        "date": "2026-11-24",
        "sources": {
            "класс 1 (RU/ответ)": "zamery-B/zaprosy-klass1-finalizirovano.md @ 9aa911a1ef (hc/s12-keys-b-fotografii-406f51fe)",
            "класс 1 (EN)": "zamery-B/zaprosy-klass1-finalizirovano.md §3 @ 9aa911a1ef (та же ветка)",
            "классы 2-3": "plan-peredelki/zaprosy-B.md @ 1dc6d8044f (issue-351-seminars-12-13-kartinki)",
        },
        "total": len(all_q),
        "queries": all_q,
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"сохранено: {OUT}")


if __name__ == "__main__":
    main()
