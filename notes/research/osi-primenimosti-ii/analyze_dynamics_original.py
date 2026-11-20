#!/usr/bin/env python3
"""Динамика по годам на original-с-годом подвыборке (213 из 421, извлечение —
build_original_years.py) и сравнение с verified (файл 14). Для файла 16 (#349).
Читает только reestr-reshenij-combined.csv (пересобранный с годами original).
Формула B = success/(success+failure). Ячейки со знаменателем <10 помечаются ⚠.

График: assets/chart-dyn-orig-vs-verified-by-year.png (стиль chart-dyn-*).
"""
import csv
import os
from collections import Counter

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

with open(os.path.join(HERE, "reestr-reshenij-combined.csv"), newline="",
          encoding="utf-8") as f:
    ALL = list(csv.DictReader(f))
assert len(ALL) == 669

OY = [r for r in ALL if r["dataset"] == "original" and r["year"]]
VER = [r for r in ALL if r["dataset"] == "verified"]
print(f"original-с-годом: {len(OY)}; verified: {len(VER)}")

YEARS = [2022, 2023, 2024, 2025, 2026]
BIG_AI = ("foundation-model", "agentic-llm")


def B(rows):
    c = Counter(r["outcome"] for r in rows)
    d = c["success"] + c["failure"]
    return (c["success"] / d if d else None), c["success"], c["failure"], len(rows)


def fmt(rows):
    b, s, f, n = B(rows)
    if b is None:
        return f"— (S+F=0, n={n})"
    flag = " ⚠" if (s + f) < 10 else ""
    return f"{100*b:.1f}% ({s}/{s+f}, n={n}){flag}"


def table(h, rows):
    print("| " + " | ".join(h) + " |")
    print("|" + "---|" * len(h))
    for row in rows:
        print("| " + " | ".join(str(c) for c in row) + " |")


def yr(rows, y):
    return [r for r in rows if r["year"] == str(y)]


pre = [r for r in OY if int(r["year"]) < 2022]
print(f"\noriginal-с-годом до 2022: {len(pre)} строк "
      f"({dict(Counter(r['year'] for r in pre))}) — вне окна трендов, "
      f"исходы: {dict(Counter(r['outcome'] for r in pre))}")

print("\n=== D1. B по годам: original-с-годом vs verified vs оба (окно 2022-2026) ===")
rows_out = []
for y in YEARS:
    both = yr(OY, y) + yr(VER, y)
    rows_out.append([y, fmt(yr(OY, y)), fmt(yr(VER, y)), fmt(both)])
table(["год", "original-с-годом B", "verified B", "оба B"], rows_out)

print("\n=== D2. Состав исходов original-с-годом по годам (S/P/F/U) ===")
rows_out = []
for y in YEARS:
    sub = yr(OY, y)
    c = Counter(r["outcome"] for r in sub)
    rows_out.append([y, len(sub), c["success"], c["partial"], c["failure"],
                     c["undetermined"]])
table(["год", "n", "S", "P", "F", "U"], rows_out)

print("\n=== D3. B на axis1=high по годам (original-с-годом) ===")
rows_out = []
for y in YEARS:
    sub = [r for r in yr(OY, y) if r["axis1_level"] == "high"]
    rows_out.append([y, fmt(sub)])
table(["год", "B (axis1=high)"], rows_out)
agg22_23 = [r for r in OY if r["year"] in ("2022", "2023") and r["axis1_level"] == "high"]
agg24_25 = [r for r in OY if r["year"] in ("2024", "2025") and r["axis1_level"] == "high"]
print(f"Агрегат high: 2022-23 {fmt(agg22_23)}; 2024-25 {fmt(agg24_25)}")

print("\n=== D4. Гейт-статус провалов по годам (original-с-годом, без L15) ===")
ONL15 = [r for r in OY if r["lecture_num"] != "15"]
print(f"original-с-годом без L15: {len(ONL15)}")
rows_out = []
for y in YEARS:
    fails = [r for r in yr(ONL15, y) if r["outcome"] == "failure"]
    c = Counter(r["axis4_gate"] for r in fails)
    n = len(fails)
    noish = c["no"] + c["not-applicable"]
    rows_out.append([y, n, c["yes"], c["no"], c["not-applicable"], c["unclear"],
                     f"{100*noish/n:.1f}% ({noish}/{n})" if n else "—"])
table(["год", "провалов", "yes", "no", "n/a", "unclear", "без гейта (no+n/a)"], rows_out)

print("\n=== D5. Big-AI vs остальные по годам (original-с-годом) ===")
rows_out = []
for y in YEARS:
    sub = yr(OY, y)
    big = [r for r in sub if r["axis3_class"] in BIG_AI]
    rest = [r for r in sub if r["axis3_class"] not in BIG_AI
            and r["axis3_class"] != "unclear"]
    share = 100 * len(big) / len(sub) if sub else 0
    rows_out.append([y, len(sub), f"{share:.1f}%", fmt(big), fmt(rest)])
table(["год", "n", "доля big-AI", "B big-AI", "B остальные"], rows_out)

print("\n=== D6. Контроль смещения: датированные vs недатированные original ===")
OALL = [r for r in ALL if r["dataset"] == "original"]
ONO = [r for r in OALL if not r["year"]]
print(f"B весь original: {fmt(OALL)}; датированные: {fmt(OY)}; недатированные: {fmt(ONO)}")
print("Доля провалов: весь original "
      f"{100*sum(1 for r in OALL if r['outcome']=='failure')/len(OALL):.1f}%, "
      f"датированные {100*sum(1 for r in OY if r['outcome']=='failure')/len(OY):.1f}%, "
      f"недатированные {100*sum(1 for r in ONO if r['outcome']=='failure')/len(ONO):.1f}%")

# -------- график --------
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.alpha"] = 0.25
fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.8))
ax = axes[0]
series = [
    ("verified (248)", VER, "#F0AB00", "o", (0, 10)),
    ("original-с-годом (213)", OY, "#21295C", "s", (0, -16)),
]
for label, ds, color, marker, off in series:
    xs, ys, ns = [], [], []
    for y in YEARS:
        b, s, f, n = B(yr(ds, y))
        if b is not None:
            xs.append(y); ys.append(100 * b); ns.append(s + f)
    ax.plot(xs, ys, color=color, marker=marker, linewidth=2, markersize=7, label=label)
    for x, yv, n in zip(xs, ys, ns):
        flag = "⚠" if n < 10 else ""
        ax.annotate(f"n={n}{flag}", (x, yv), textcoords="offset points", xytext=off,
                    ha="center", fontsize=8, color=color)
ax.axvspan(2025.5, 2026.5, color="#B0B0B0", alpha=0.15)
y0, y1 = ax.get_ylim()
ax.text(2026, y0 + 0.01 * (y1 - y0), "2026 неполный", ha="center", va="bottom",
        fontsize=8, color="#555555")
ax.set_xticks(YEARS)
ax.set_ylabel("Доля успеха B = S/(S+F), %")
ax.set_title("B по годам: два независимых датированных корпуса\n"
             "(original-с-годом смещён к провалам — см. правую панель)")
ax.legend(loc="upper left", fontsize=9)

ax = axes[1]
cats = ["success", "partial", "failure", "undetermined"]
labels = {"success": "успех", "partial": "частичный", "failure": "провал",
          "undetermined": "не определён"}
colors = {"success": "#2E7D32", "partial": "#F0AB00", "failure": "#B23A48",
          "undetermined": "#B0B0B0"}
OALL_c = Counter(r["outcome"] for r in OALL)
OY_c = Counter(r["outcome"] for r in OY)
x = range(len(cats))
ax.bar([i - 0.2 for i in x], [100 * OALL_c[c] / len(OALL) for c in cats], width=0.38,
       color=[colors[c] for c in cats], alpha=0.45, label="весь original (421)")
ax.bar([i + 0.2 for i in x], [100 * OY_c[c] / len(OY) for c in cats], width=0.38,
       color=[colors[c] for c in cats], label="original-с-годом (213)")
for i, c in enumerate(cats):
    ax.text(i - 0.2, 100 * OALL_c[c] / len(OALL) + 1, f"{100*OALL_c[c]/len(OALL):.0f}%",
            ha="center", fontsize=8, color="#555555")
    ax.text(i + 0.2, 100 * OY_c[c] / len(OY) + 1, f"{100*OY_c[c]/len(OY):.0f}%",
            ha="center", fontsize=8)
ax.set_xticks(list(x), [labels[c] for c in cats])
ax.set_ylabel("Доля строк, %")
ax.set_title("Почему original-с-годом ниже по B: датируются\nчаще провалы "
             "(71,5% против 48,1% у успехов)")
ax.legend(fontsize=9)
fig.suptitle("Год из первоисточника original-реестра (213/421) против verified", y=1.0)
fig.tight_layout()
out = os.path.join(ASSETS, "chart-dyn-orig-vs-verified-by-year.png")
fig.savefig(out, dpi=150)
print(f"\nCHART: {out} {'OK' if os.path.exists(out) else 'MISSING'}")
