#!/usr/bin/env python3
"""Build reestr-reshenij-combined.csv from the original (421) and verified (248)
registries. Additive-only script; does not modify either source CSV.

Usage: python3 build_combined.py
Run from repo root or any cwd — paths are relative to this file's directory.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ORIGINAL = os.path.join(HERE, "reestr-reshenij.csv")
VERIFIED = os.path.join(HERE, "reestr-reshenij-verified.csv")
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

    out_rows = []
    for r in orig_rows:
        row = {"dataset": "original"}
        for c in COMMON_COLS:
            row[c] = r[c]
        row["year"] = ""
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

    print(f"OK: wrote {COMBINED}")
    print(f"  total rows (reread) = {len(reread)}")
    print(f"  dataset=original    = {n_orig}")
    print(f"  dataset=verified     = {n_ver}")


if __name__ == "__main__":
    main()
