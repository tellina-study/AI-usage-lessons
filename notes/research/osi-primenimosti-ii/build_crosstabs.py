#!/usr/bin/env python3
"""Compute the 5 cross-tabs required for 12-svodnyj-reestr-kombinirovannyj.md,
each split by dataset in {original, verified, combined}. Reads only
reestr-reshenij-combined.csv (already built by build_combined.py). Prints
markdown tables to stdout — the analysis .md is assembled by hand from this
output so every number in the prose is copy-pasted from a script run, not
hand-computed.

Formula B (course convention): success_rate = success / (success + failure),
partial and undetermined excluded from the denominator.
"""
import csv
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
COMBINED = os.path.join(HERE, "reestr-reshenij-combined.csv")

with open(COMBINED, newline="", encoding="utf-8") as f:
    ALL_ROWS = list(csv.DictReader(f))

assert len(ALL_ROWS) == 669

OUTCOMES = ["success", "partial", "failure", "undetermined"]


def subset(dataset):
    if dataset == "combined":
        return ALL_ROWS
    return [r for r in ALL_ROWS if r["dataset"] == dataset]


def success_rate(counts):
    s = counts.get("success", 0)
    fa = counts.get("failure", 0)
    denom = s + fa
    if denom == 0:
        return None
    return s / denom


def crosstab(rows, key_col):
    """key -> {outcome: count}"""
    table = defaultdict(lambda: defaultdict(int))
    for r in rows:
        table[r[key_col]][r["outcome"]] += 1
    return table


def print_crosstab(title, key_col, key_order, exclude_lecture15=False):
    print(f"\n## {title}  (key={key_col}, exclude_lec15={exclude_lecture15})\n")
    datasets = ["original", "verified", "combined"]
    data = {}
    excluded_counts = {}
    for ds in datasets:
        rows = subset(ds)
        if exclude_lecture15:
            before = len(rows)
            rows = [r for r in rows if r["lecture_num"] != "15"]
            excluded_counts[ds] = before - len(rows)
        data[ds] = crosstab(rows, key_col)

    if exclude_lecture15:
        print(f"excluded lecture_num==15 rows: original={excluded_counts['original']}, "
              f"verified={excluded_counts['verified']}, combined={excluded_counts['original']+excluded_counts['verified']}")

    header = ["key"]
    for ds in datasets:
        for oc in OUTCOMES:
            header.append(f"{ds[:3]}_{oc}")
        header.append(f"{ds[:3]}_success_rate")
    print(",".join(header))

    keys = key_order if key_order else sorted(set().union(*[set(data[ds].keys()) for ds in datasets]))
    for k in keys:
        row = [k]
        for ds in datasets:
            counts = data[ds].get(k, {})
            for oc in OUTCOMES:
                row.append(str(counts.get(oc, 0)))
            sr = success_rate(counts)
            row.append(f"{sr:.3f}" if sr is not None else "n/a")
        print(",".join(row))
    return data, excluded_counts


# 1. industry x outcome
industries = sorted(set(r["industry"] for r in ALL_ROWS))
print_crosstab("industry x outcome", "industry", industries)

# 2. axis3_class x outcome
axis3_vals = ["rule-based", "classical-ml", "deep-learning", "foundation-model",
              "agentic-llm", "sensor-fusion", "hybrid", "unclear"]
print_crosstab("axis3_class x outcome", "axis3_class", axis3_vals)

# 3. axis4_gate x outcome, excluding lecture_num==15
axis4_gate_vals = ["yes", "no", "not-applicable", "unclear"]
print_crosstab("axis4_gate x outcome (lecture 15 EXCLUDED)", "axis4_gate", axis4_gate_vals,
               exclude_lecture15=True)

# 4. axis1_level x outcome
axis1_vals = ["low", "moderate", "high", "extreme", "unclear"]
print_crosstab("axis1_level x outcome", "axis1_level", axis1_vals)

# 5. year coverage 2018-2026, verified only
print("\n## year coverage 2018-2026 (verified dataset only)\n")
ver_rows = subset("verified")
year_counts = defaultdict(int)
for r in ver_rows:
    year_counts[r["year"]] += 1
for y in [str(y) for y in range(2018, 2027)]:
    print(f"{y},{year_counts.get(y, 0)}")
other_years = {y: c for y, c in year_counts.items() if y not in [str(y) for y in range(2018, 2027)]}
if other_years:
    print("OTHER/BLANK YEAR VALUES OUTSIDE 2018-2026:", other_years)
print("total verified rows counted:", sum(year_counts.values()), "(expect 248)")
