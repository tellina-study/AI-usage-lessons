#!/usr/bin/env python3
"""Build reestr-reshenij-combined.csv from the original (421) and verified (248)
registries. Additive-only script; does not modify either source CSV.

Расширение (#349, файл 16): если рядом лежит reestr-reshenij-original-years.csv
(явные годы, извлечённые из razmetka/lec-NN.md ревью build_original_years.py /
year_decisions.py), его непустые года подставляются в колонку `year` строк
dataset=original. Строки без извлечённого года остаются с пустым `year`, как
раньше (обратная совместимость); verified не затрагивается. Если файла годов
нет — поведение прежнее (все original с пустым year).

Usage: python3 build_combined.py
Run from repo root or any cwd — paths are relative to this file's directory.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ORIGINAL = os.path.join(HERE, "reestr-reshenij.csv")
VERIFIED = os.path.join(HERE, "reestr-reshenij-verified.csv")
ORIGINAL_YEARS = os.path.join(HERE, "reestr-reshenij-original-years.csv")
COMBINED = os.path.join(HERE, "reestr-reshenij-combined.csv")

COMMON_COLS = [
    "id", "lecture_num", "industry", "case_name",
    "axis1_level", "axis1_mechanism", "axis2_bucket", "axis2_mechanism",
    "axis3_class", "axis4_gate", "axis4_blast_radius", "external_driver",
    "outcome", "confidence", "source_file", "source_locator",
]
OUT_COLS = ["dataset"] + COMMON_COLS + ["year", "source_url"]


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    orig_rows = load(ORIGINAL)
    ver_rows = load(VERIFIED)

    assert len(orig_rows) == 421, f"original row count = {len(orig_rows)}, expected 421"
    assert len(ver_rows) == 248, f"verified row count = {len(ver_rows)}, expected 248"

    # id prefix sanity check
    assert all(r["id"].startswith("L") for r in orig_rows), "non-L id in original"
    assert all(r["id"].startswith("V") for r in ver_rows), "non-V id in verified"

    orig_years = {}
    if os.path.exists(ORIGINAL_YEARS):
        yrows = load(ORIGINAL_YEARS)
        assert len(yrows) == 421, f"original-years row count = {len(yrows)}"
        orig_years = {r["id"]: r["year"] for r in yrows if r["year"]}
        print(f"original-years найден: непустой year у {len(orig_years)} из 421 строк")
    else:
        print("original-years не найден — все original с пустым year (прежнее поведение)")

    out_rows = []
    for r in orig_rows:
        row = {"dataset": "original"}
        for c in COMMON_COLS:
            row[c] = r[c]
        row["year"] = orig_years.get(r["id"], "")
        row["source_url"] = ""
        out_rows.append(row)

    for r in ver_rows:
        row = {"dataset": "verified"}
        for c in COMMON_COLS:
            row[c] = r[c]
        row["year"] = r["year"]
        row["source_url"] = r["source_url"]
        out_rows.append(row)

    assert len(out_rows) == 421 + 248 == 669, f"pre-write total = {len(out_rows)}"

    with open(COMBINED, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS)
        w.writeheader()
        for row in out_rows:
            w.writerow(row)

    # Re-read what was actually written and recount — do not trust the write.
    with open(COMBINED, newline="", encoding="utf-8") as f:
        reread = list(csv.DictReader(f))

    assert len(reread) == 669, f"post-write reread total = {len(reread)}"
    n_orig = sum(1 for r in reread if r["dataset"] == "original")
    n_ver = sum(1 for r in reread if r["dataset"] == "verified")
    assert n_orig == 421, f"reread original count = {n_orig}"
    assert n_ver == 248, f"reread verified count = {n_ver}"

    n_orig_year = sum(1 for r in reread if r["dataset"] == "original" and r["year"])
    assert n_orig_year == len(orig_years), (
        f"reread original-with-year = {n_orig_year}, ожидалось {len(orig_years)}")

    print(f"OK: wrote {COMBINED}")
    print(f"  total rows (reread) = {len(reread)}")
    print(f"  dataset=original    = {n_orig} (с непустым year: {n_orig_year})")
    print(f"  dataset=verified     = {n_ver}")


if __name__ == "__main__":
    main()
