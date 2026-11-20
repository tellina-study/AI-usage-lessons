#!/usr/bin/env python3
"""Шаг 2 извлечения годов original-реестра (#349, файл 16): собирает
reestr-reshenij-original-years.csv из (а) кандидатов extract_year_candidates.py
и (б) ручных решений year_decisions.py, с перекрёстной валидацией:

1. множество решений (DECISIONS ∪ REJECTED) == множеству кейсов с кандидатами,
   ровно — ни одного неразобранного кандидата, ни одного решения без кандидата;
2. каждый принятый год обязан буквально входить в regex-кандидаты своей строки
   (решение не может «придумать» год, которого нет в тексте razmetka);
3. итоговый CSV содержит все 421 строки реестра (absent — с пустым year).

Печатает покрытие и bias-разрезы (по исходу, лекции, классу метода) — для файла 16.
"""
import csv
import os
from collections import Counter

import extract_year_candidates as ex  # выполняет матчинг при импорте
from year_decisions import DECISIONS, REJECTED

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_CSV = os.path.join(HERE, "reestr-reshenij-original-years.csv")

by_id = {o[0]: o for o in ex.out}
assert len(by_id) == 421

cand_ids = {cid for cid, _, _, _, n, _ in ex.out if n > 0}
decided = set(DECISIONS) | set(REJECTED)
assert not (set(DECISIONS) & set(REJECTED)), "кейс и принят, и отклонён"
missing = cand_ids - decided
extra = decided - cand_ids
assert not missing, f"кандидаты без решения: {sorted(missing)}"
assert not extra, f"решения без кандидатов: {sorted(extra)}"

for cid, (year, conf, quote) in DECISIONS.items():
    cand_years = {int(y) for y, _ in by_id[cid][5]}
    assert year in cand_years, f"{cid}: год {year} не входит в кандидаты {sorted(cand_years)}"
    assert conf in ("explicit", "range"), (cid, conf)

with open(os.path.join(HERE, "reestr-reshenij.csv"), newline="", encoding="utf-8") as f:
    reestr = list(csv.DictReader(f))

rows_out = []
for r in reestr:
    cid = r["id"]
    if cid in DECISIONS:
        year, conf, quote = DECISIONS[cid]
        rows_out.append([cid, str(year), conf, quote, r["source_file"], r["source_locator"]])
    else:
        rows_out.append([cid, "", "absent", "", r["source_file"], r["source_locator"]])

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "year", "year_confidence", "year_quote", "source_file",
                "source_locator"])
    w.writerows(rows_out)

# перечитываем и проверяем
with open(OUT_CSV, newline="", encoding="utf-8") as f:
    check = list(csv.DictReader(f))
assert len(check) == 421
n_year = sum(1 for r in check if r["year"])
print(f"CSV записан: {OUT_CSV}")
print(f"Всего строк: {len(check)}; с годом: {n_year} ({100*n_year/421:.1f}%); "
      f"absent: {421-n_year} (из них с отклонёнными кандидатами: {len(REJECTED)})")
print(f"confidence: {dict(Counter(r['year_confidence'] for r in check))}")

print("\nРаспределение по годам (принятые):")
yc = Counter(int(r["year"]) for r in check if r["year"])
for y in sorted(yc):
    print(f"  {y}: {yc[y]}")

# bias-разрезы: покрытие годом по исходу / лекции / классу
meta = {r["id"]: r for r in reestr}
print("\nПокрытие годом по исходу:")
for oc in ("success", "partial", "failure", "undetermined"):
    sub = [r for r in check if meta[r["id"]]["outcome"] == oc]
    k = sum(1 for r in sub if r["year"])
    print(f"  {oc}: {k}/{len(sub)} = {100*k/len(sub):.1f}%")
print("\nПокрытие годом по лекции:")
for ln in range(4, 16):
    sub = [r for r in check if meta[r["id"]]["lecture_num"] == str(ln)]
    k = sum(1 for r in sub if r["year"])
    print(f"  lec-{ln:02d}: {k}/{len(sub)} = {100*k/len(sub):.1f}%")
print("\nПокрытие годом по классу метода:")
for cls in ("rule-based", "classical-ml", "sensor-fusion", "hybrid", "deep-learning",
            "foundation-model", "agentic-llm", "unclear"):
    sub = [r for r in check if meta[r["id"]]["axis3_class"] == cls]
    k = sum(1 for r in sub if r["year"])
    print(f"  {cls}: {k}/{len(sub)} = {100*k/len(sub):.1f}%")
