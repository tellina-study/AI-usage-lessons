#!/usr/bin/env python3
"""Механическая проверка соблюдения процедуры P-NOTE v2 (issue #217, эксперимент B).
Запуск: python3 check.py  (из корня репозитория)"""
import os, glob, re
OUT = "notes/research/student-questions/skills-vs-instructions/_exp/out3"

HDR = "**Date:** 2026-10-02 · **Issue:** #217-EXP"
TBL = "| утверждение | источник | тип |"
SEC = "## Что НЕ доказано"
MRK = "<!-- checked: P-NOTE v2 -->"

def check(path):
    IDX = os.path.join(os.path.dirname(path), "index.md")
    t = open(path, encoding="utf-8").read()
    L = [l.rstrip() for l in t.split("\n")]
    nz = [l for l in L if l.strip()]
    s = {}
    s["1_header"] = bool(nz) and nz[0].startswith("# ") and len(nz) > 1 and nz[1].strip() == HDR
    rows = 0
    if TBL.lower() in t.lower():
        i = [k for k, l in enumerate(L) if l.strip().lower() == TBL.lower()][0]
        for l in L[i+1:]:
            if l.strip().startswith("|") and not re.match(r"^\|[\s:|-]+\|$", l.strip()):
                rows += 1
            elif not l.strip().startswith("|"):
                break
    s["2_table"] = (TBL.lower() in t.lower()) and rows >= 2
    s["3_section"] = any(l.strip() == SEC for l in L)
    s["4_marker"] = bool(nz) and nz[-1].strip() == MRK
    name = os.path.basename(path)
    s["5_index"] = os.path.exists(IDX) and any(
        name in l and l.strip().startswith("- ") for l in open(IDX, encoding="utf-8"))
    return s

files = sorted(f for f in glob.glob(os.path.join(OUT, "*", "*.md")) if not f.endswith("index.md"))
steps = ["1_header", "2_table", "3_section", "4_marker", "5_index"]
print(f"{'плечо/файл':<12}" + "".join(f"{s:<11}" for s in steps) + "итого")
for f in files:
    r = check(f)
    print(f"{os.path.relpath(f, OUT):<12}" + "".join(("  ДА       " if r[s] else "  нет      ") for s in steps)
          + f"{sum(r.values())}/5")
if not files:
    print("(нет файлов — ни одно плечо ещё не отработало)")
