#!/usr/bin/env python3
"""Сборка 100 запросов корпуса-101: 38 запросов круга 1 (`zaprosy_full.json`,
пересобирается своим скриптом из чужих источников — здесь только читается) +
62 запроса добора (`zaprosy-dobor.md`, написаны этой сессией).

Производное не правится руками (канон §8.5) — всегда пересобирается отсюда.
Запуск:  python3 build_zaprosy_101.py
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from corpus_b101 import corpus_ids, short_id_map, resolve_id  # noqa: E402

CLASS_NUM = {"К-слово": 1, "К-пересказ": 2, "К-деталь": 3}

# Запросы, у которых после расширения корпуса с 40 до 101 появился ВТОРОЙ верный
# ответ. Находятся сплошным чтением всех запросов круга 1 против всех 61 новых
# разметок (автоматический сторож на лексическом совпадении этого НЕ находит —
# см. журнал). Из головных чисел исключаются, число исключённых называется.
AMBIGUOUS = {
    "3.13": ("94043f06b44df043", "30dc8f6e837f7b47",
             "«значок на лацкане выступающего»: у 94043f06 разметка говорит «На лацкане значок», "
             "у добранного 30dc8f6e — «на лацкане круглый белый значок». Два верных ответа."),
}


def main():
    ids = corpus_ids()
    smap = short_id_map(ids)

    old = json.loads((HERE / "zaprosy_full.json").read_text(encoding="utf-8"))["queries"]
    for q in old:
        q["round"] = 1
        q["answer"] = resolve_id(q["answer"], smap)

    new = []
    for ln in (HERE / "zaprosy-dobor.md").read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\|\s*4\.\d+", ln):
            continue
        c = [x.strip() for x in ln.strip("|").split("|")]
        if len(c) != 5:
            raise SystemExit(f"строка не из пяти столбцов: {ln}")
        new.append({
            "num": c[0], "class": CLASS_NUM[c[1]], "class_name": c[1],
            "ru": c[2], "en": c[3], "answer": resolve_id(c[4], smap), "round": 3,
        })

    qs = old + new
    nums = [q["num"] for q in qs]
    if len(set(nums)) != len(nums):
        raise SystemExit("дубли номеров запросов")
    for q in qs:
        if q["num"] in AMBIGUOUS:
            q["ambiguous"] = True
            q["ambiguous_with"] = AMBIGUOUS[q["num"]][1]
            q["ambiguous_why"] = AMBIGUOUS[q["num"]][2]
    bad = [q["num"] for q in qs if q["answer"] not in ids]
    if bad:
        raise SystemExit(f"ответы вне корпуса: {bad}")

    from collections import Counter
    byc = Counter(q["class_name"] for q in qs)
    byr = Counter(q["round"] for q in qs)
    dupans = [a for a, k in Counter(q["answer"] for q in qs).items() if k > 1]

    (HERE / "zaprosy_101.json").write_text(json.dumps({
        "date": "2026-11-24", "total": len(qs),
        "corpus": "101 снимок (zamery-B/razmetka-101.json)",
        "baseline_random": round(1 / len(ids), 4),
        "sources": ["zaprosy_full.json (38, круг 1)", "zaprosy-dobor.md (62, круг 3)"],
        "ambiguous": {k: v[2] for k, v in AMBIGUOUS.items()},
        "scored": len(qs) - len(AMBIGUOUS),
        "queries": qs,
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"запросов: {len(qs)}  (круг 1: {byr[1]}, круг 3: {byr[3]})")
    for k in ("К-слово", "К-пересказ", "К-деталь"):
        print(f"  {k:12s} {byc[k]:3d}  ({byc[k]/len(qs)*100:.0f}%)")
    print(f"снимков-ответов различных: {len(set(q['answer'] for q in qs))} из {len(ids)}")
    print(f"снимки, на которые ссылаются ДВА запроса: {len(dupans)} "
          f"({', '.join(a[:8] for a in dupans) if dupans else '—'})")
    print(f"исключено из головных чисел как двусмысленные: {len(AMBIGUOUS)} "
          f"({', '.join(AMBIGUOUS)}) → считается {len(qs) - len(AMBIGUOUS)}")
    print(f"база случайного угадывания: 1/{len(ids)} = {1/len(ids):.4f} "
          f"(в круге 1 было 1/40 = {1/40:.4f})")


if __name__ == "__main__":
    main()
