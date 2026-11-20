#!/usr/bin/env python3
"""Шаг 1 извлечения годов для original-реестра (#349, файл 16): для каждой из 421
строк reestr-reshenij.csv найти её строку-таблицу в razmetka/lec-NN.md и выдать
ВСЕ regex-кандидаты лет (19xx/20xx) с контекстом ±70 символов — на ручное ревью.
Сам ничего не решает: решения (год/диапазон/false-positive) принимает ревью,
зафиксированное отдельным файлом year_decisions.py.

Граница методологии: текст ровно одной строки таблицы lec-NN.md (все ячейки);
chapter.md, os4-файлы и внешние знания не используются.
"""
import csv
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
RAZMETKA = os.path.join(HERE, "razmetka")
CSV_PATH = os.path.join(HERE, "reestr-reshenij.csv")

YEAR_RE = re.compile(r"(?<![0-9])(19[5-9][0-9]|20[0-2][0-9])(?![0-9])")

SUBTABLE_PREFIXES = ("section1", "hiring", "editorial", "release", "rights",
                     "discrete", "process", "telecom", "aiops", "cybersecurity")


def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = s.replace("*", "").replace("`", "").replace("\\|", "|")
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"^\d+[.)]\s*", "", s)  # нумерация в начале
    return s


def table_rows(path):
    """Все строки-таблицы файла: список (lineno, [cells])."""
    rows = []
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            ls = line.strip()
            if not ls.startswith("|"):
                continue
            if re.match(r"^\|[\s:\-|]+\|$", ls):  # разделитель
                continue
            cells = [c.strip() for c in ls.strip("|").split("|")]
            rows.append((i, cells))
    return rows


with open(CSV_PATH, newline="", encoding="utf-8") as f:
    reestr = list(csv.DictReader(f))
assert len(reestr) == 421

rows_by_file = {}
unmatched = []
multi = []
out = []

for r in reestr:
    sf = r["source_file"]
    if sf not in rows_by_file:
        rows_by_file[sf] = table_rows(os.path.join(RAZMETKA, sf))
    loc = r["source_locator"]
    name = loc
    for p in SUBTABLE_PREFIXES:
        if loc.startswith(p + ": "):
            name = loc[len(p) + 2:]
            break
    target = norm(name)

    def find(pred):
        return [(ln, cells) for ln, cells in rows_by_file[sf] if cells and pred(cells)]

    # имя кейса — в 1-й ячейке; в лекциях 04/05 1-я ячейка — номер, имя во 2-й
    matches = find(lambda c: norm(c[0]) == target)
    if not matches:
        matches = find(lambda c: len(c) > 1 and norm(c[1]) == target)
    if not matches:
        matches = find(lambda c: norm(c[0]).startswith(target)
                       or (len(c) > 1 and norm(c[1]).startswith(target)))
    if not matches:
        # усечённые имена (например, L09-029): общий префикс ≥40 симв.
        t40 = target[:40]
        matches = find(lambda c: norm(c[0]).startswith(t40)
                       or (len(c) > 1 and norm(c[1]).startswith(t40)))
    if not matches:
        unmatched.append((r["id"], sf, loc))
        continue
    if len(matches) > 1:
        multi.append((r["id"], sf, loc, [m[0] for m in matches]))
    ln, cells = matches[0]
    row_text = " | ".join(cells)
    cands = []
    for m in YEAR_RE.finditer(row_text):
        a, b = m.span()
        ctx = row_text[max(0, a - 70):min(len(row_text), b + 70)]
        cands.append((m.group(1), ctx.replace("\n", " ")))
    out.append((r["id"], r["outcome"], sf, ln, len(cands), cands))

print(f"MATCHED: {len(out)}/421; UNMATCHED: {len(unmatched)}; MULTI-MATCH: {len(multi)}")
for u in unmatched:
    print("  UNMATCHED:", u)
for m in multi:
    print("  MULTI:", m)

with_c = [o for o in out if o[4] > 0]
print(f"STROK S KANDIDATAMI: {len(with_c)}; bez: {len(out) - len(with_c)}")
total_c = sum(o[4] for o in out)
print(f"VSEGO KANDIDATOV: {total_c}")

with open(os.path.join(HERE, "year_candidates_review.txt"), "w", encoding="utf-8") as f:
    for cid, outcome, sf, ln, n, cands in out:
        if n == 0:
            continue
        f.write(f"### {cid} [{outcome}] {sf}:{ln}\n")
        for y, ctx in cands:
            f.write(f"  {y} :: …{ctx}…\n")
print("written: year_candidates_review.txt")
