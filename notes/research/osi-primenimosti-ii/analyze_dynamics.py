#!/usr/bin/env python3
"""Пересчёт гипотез линии #349 на двух реестрах (421 original + 248 verified) +
динамика по годам (только verified — единственный датасет с колонкой year) +
новые гипотезы. Читает ТОЛЬКО reestr-reshenij-combined.csv (построен
build_combined.py). Печатает markdown-таблицы в stdout — файлы 13-15 собираются
из этого вывода, ни одно число в прозе не досчитано вручную.

Формула успешности везде, где не сказано иное, — формула B этой линии
(10-industriya-i-rejting-faktorov.md §0): success / (success + failure),
partial/undetermined исключены и из числителя, и из знаменателя.

Графики — в assets/, тот же стиль, что make_charts.py (dpi=150, та же палитра
исходов), имена с префиксом chart-dyn-* / chart-cmp-*.
"""
import csv
import os
from collections import Counter, defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
COMBINED = os.path.join(HERE, "reestr-reshenij-combined.csv")

with open(COMBINED, newline="", encoding="utf-8") as f:
    ALL = list(csv.DictReader(f))
# объём корпуса растёт между волнами — фиксируем только структуру
assert len(ALL) > 0

ORIG = [r for r in ALL if r["dataset"] == "original"]
VER = [r for r in ALL if r["dataset"] == "verified"]
assert len(ORIG) == 421  # original заморожен; verified растёт волнами

OUTCOME_COLORS = {
    "success": "#2E7D32",
    "partial": "#F0AB00",
    "failure": "#B23A48",
    "undetermined": "#B0B0B0",
}

YEARS_WINDOW = list(range(2018, 2027))  # с волны 3 годы 2018-2021 наполнены (23-41 строк/год)
BIG_AI = ("foundation-model", "agentic-llm")
CLASSIC = ("rule-based", "classical-ml")


def B(rows):
    """Формула B: success/(success+failure); None если знаменатель 0."""
    c = Counter(r["outcome"] for r in rows)
    d = c["success"] + c["failure"]
    return (c["success"] / d if d else None), c["success"], c["failure"], len(rows)


def fmt_b(rows):
    b, s, f, n = B(rows)
    if b is None:
        return f"— (0 исходов S+F из n={n})"
    flag = " ⚠️" if (s + f) < 10 else ""
    return f"{100*b:.1f}% ({s}/{s+f}, n={n}){flag}"


def pct(x, d):
    return f"{100*x/d:.1f}%" if d else "—"


def section(title):
    print(f"\n{'='*80}\n{title}\n{'='*80}")


def table(headers, rows):
    print("| " + " | ".join(headers) + " |")
    print("|" + "---|" * len(headers))
    for row in rows:
        print("| " + " | ".join(str(c) for c in row) + " |")


def no_l15(rows):
    return [r for r in rows if r["lecture_num"] != "15"]


# ---------------------------------------------------------------------------
section("A1. Атрибуция провалов к статусу гейта (реплика файла 10 §1, чистые счётчики)")
for label, rows, excl in [
    ("original, весь корпус (как в файле 10 §1)", ORIG, False),
    ("original, без Лекции 15", no_l15(ORIG), True),
    ("verified, весь корпус", VER, False),
    ("verified, без Лекции 15", no_l15(VER), True),
    ("combined, без Лекции 15", no_l15(ALL), True),
]:
    fails = [r for r in rows if r["outcome"] == "failure"]
    succ = [r for r in rows if r["outcome"] == "success"]
    gf = Counter(r["axis4_gate"] for r in fails)
    gs = Counter(r["axis4_gate"] for r in succ)
    nf, ns = len(fails), len(succ)
    print(f"\n### {label}")
    table(
        ["Исход", "гейта нет", "неприменим", "гейт есть", "unclear", "всего"],
        [
            ["провал", gf["no"], gf["not-applicable"], f"**{gf['yes']}**", gf["unclear"], nf],
            ["успех", gs["no"], gs["not-applicable"], gs["yes"], gs["unclear"], ns],
        ],
    )
    at_gate = gf["yes"]
    without = gf["no"] + gf["not-applicable"]
    print(f"Провалов при действующем гейте: {at_gate}/{nf} = {pct(at_gate, nf)}; "
          f"без гейта/неприменим: {without}/{nf} = {pct(without, nf)}. "
          f"Успехов с gate=no: {gs['no']}/{ns} = {pct(gs['no'], ns)}.")

# ---------------------------------------------------------------------------
section("A2. axis2_bucket × outcome (ось обратной связи — её не было в файле 12)")
A2_ORDER = ["seconds-minutes", "hours-days", "weeks-months", "season-years", "unclear"]
rows_out = []
for lvl in A2_ORDER:
    cells = []
    for ds in (ORIG, VER, ALL):
        sub = [r for r in ds if r["axis2_bucket"] == lvl]
        cells.append(fmt_b(sub))
    rows_out.append([lvl] + cells)
table(["axis2_bucket", "original B", "verified B", "combined B"], rows_out)

# ---------------------------------------------------------------------------
section("A3. Blast radius внутри Гейт=Нет (реплика файла 07 §3; формула B, не C!)")
A4_ORDER = ["low", "medium", "high", "catastrophic"]
for label, ds in [("original", ORIG), ("verified", VER), ("combined", ALL)]:
    print(f"\n### {label} (только axis4_gate=no)")
    sub_ng = [r for r in ds if r["axis4_gate"] == "no"]
    rows_out = []
    for lvl in A4_ORDER:
        sub = [r for r in sub_ng if r["axis4_blast_radius"] == lvl]
        c = Counter(r["outcome"] for r in sub)
        rows_out.append([lvl, len(sub), c["success"], c["partial"], c["failure"],
                         c["undetermined"], fmt_b(sub)])
    table(["blast radius", "n", "S", "P", "F", "U", "B"], rows_out)

# ---------------------------------------------------------------------------
section("A4. Рейтинг измерений по разбросу B (реплика tornado файла 10 §3) — original vs verified")
DIMS = [
    ("гейт (без L15)", "axis4_gate", ["yes", "no"], True),
    ("отрасль", "industry", None, False),
    ("цена ошибки", "axis4_blast_radius", A4_ORDER, False),
    ("неопределённость", "axis1_level", ["low", "moderate", "high", "extreme"], False),
    ("класс метода", "axis3_class", ["rule-based", "classical-ml", "deep-learning",
                                     "foundation-model", "agentic-llm", "sensor-fusion",
                                     "hybrid"], False),
    ("время обратной связи", "axis2_bucket", A2_ORDER[:4], False),
]
tornado_data = {}
for label, ds0 in [("original", ORIG), ("verified", VER)]:
    print(f"\n### {label}")
    rows_out = []
    tornado_data[label] = []
    for dim_name, col, levels, excl15 in DIMS:
        ds = no_l15(ds0) if excl15 else ds0
        if levels is None:
            levels = sorted({r[col] for r in ds})
        vals = []
        for lvl in levels:
            if lvl in ("unclear", "not-applicable"):
                continue
            sub = [r for r in ds if r[col] == lvl]
            b, s, f, n = B(sub)
            if b is not None:
                vals.append((b, lvl, s, f))
        if not vals:
            continue
        lo, hi = min(vals), max(vals)
        spread = 100 * (hi[0] - lo[0])
        tornado_data[label].append((dim_name, spread))
        rows_out.append([dim_name,
                         f"{lo[1]} {100*lo[0]:.1f}% ({lo[2]}/{lo[2]+lo[3]})",
                         f"{hi[1]} {100*hi[0]:.1f}% ({hi[2]}/{hi[2]+hi[3]})",
                         f"**{spread:.1f}**"])
    rows_out.sort(key=lambda r: -float(r[3].strip("*")))
    table(["Измерение", "минимум B", "максимум B", "разброс, п.п."], rows_out)

# ---------------------------------------------------------------------------
section("A5. Доля классики по уровню неопределённости (реплика файла 09 §1)")
for label, ds in [("original", ORIG), ("verified", VER)]:
    print(f"\n### {label}")
    rows_out = []
    for lvl in ["low", "moderate", "high", "extreme"]:
        sub = [r for r in ds if r["axis1_level"] == lvl]
        cl = [r for r in sub if r["axis3_class"] in CLASSIC]
        rows_out.append([lvl, len(cl), len(sub), pct(len(cl), len(sub))])
    table(["уровень", "классика (rb+cml)", "всего", "доля"], rows_out)

# ---------------------------------------------------------------------------
section("A6. Воронка «мёртвой зоны» (реплика файла 11 §3)")
for label, ds in [("original (реплика 421→232→138→78)", ORIG), ("verified", VER),
                  ("combined", ALL)]:
    print(f"\n### {label}")
    s1 = ds
    s2 = [r for r in s1 if r["axis4_gate"] in ("no", "not-applicable")]
    s3 = [r for r in s2 if r["axis1_mechanism"] in ("U1", "U2", "U3", "U4")
          or r["axis2_mechanism"] in ("F-A", "F-B", "F-C")]
    s4 = [r for r in s3 if r["axis4_blast_radius"] in ("high", "catastrophic")]
    rows_out = []
    for name, sub in [("весь корпус", s1), ("нет гейта/неприменим", s2),
                      ("+ назван механизм U/F", s3), ("+ высокая/катастроф. цена", s4)]:
        c = Counter(r["outcome"] for r in sub)
        rows_out.append([name, len(sub), c["success"], c["failure"], fmt_b(sub)])
    table(["ступень", "n", "успехов", "провалов", "B"], rows_out)
    surv = [f'{r["id"]} {r["case_name"]}' for r in s4 if r["outcome"] == "success"]
    print("Выжившие на последней ступени: " + ("; ".join(surv) if surv else "НЕТ (0)"))

# ---------------------------------------------------------------------------
section("A7. Названный механизм U/F vs его отсутствие (реплика файла 10 §4)")
for label, ds in [("original", ORIG), ("verified", VER)]:
    print(f"\n### {label}")
    named = [r for r in ds if r["axis1_mechanism"] in ("U1", "U2", "U3", "U4")
             or r["axis2_mechanism"] in ("F-A", "F-B", "F-C")]
    none_ = [r for r in ds if r["axis1_mechanism"] == "none"
             and r["axis2_mechanism"] == "none"]
    mech_rows = []
    for m in ["U1", "U2", "U3", "U4"]:
        sub = [r for r in ds if r["axis1_mechanism"] == m]
        mech_rows.append([m, fmt_b(sub)])
    for m in ["F-A", "F-B", "F-C"]:
        sub = [r for r in ds if r["axis2_mechanism"] == m]
        mech_rows.append([m, fmt_b(sub)])
    mech_rows.append(["любой названный (U или F)", fmt_b(named)])
    mech_rows.append(["оба механизма none", fmt_b(none_)])
    table(["механизм", "B"], mech_rows)

# ===========================================================================
section("B1. Динамика: формула B по годам (только verified; окно 2018-2026)")
pre = [r for r in VER if r["year"] and int(r["year"]) < 2018]
noyear = [r for r in VER if not r["year"]]
print(f"до 2018: n={len(pre)} строк — вне окна; без года: {len(noyear)} "
      f"({[r['id'] for r in noyear]})")
rows_out = []
year_B = {}
for y in YEARS_WINDOW:
    sub = [r for r in VER if r["year"] == str(y)]
    b, s, f, n = B(sub)
    year_B[y] = (b, s, f, n)
    c = Counter(r["outcome"] for r in sub)
    rows_out.append([y, n, c["success"], c["partial"], c["failure"], c["undetermined"],
                     fmt_b(sub)])
table(["год", "n", "S", "P", "F", "U", "B"], rows_out)

# ---------------------------------------------------------------------------
section("B2. Динамика: распределение axis1_level по годам + B на high по годам")
rows_out = []
for y in YEARS_WINDOW:
    sub = [r for r in VER if r["year"] == str(y)]
    c = Counter(r["axis1_level"] for r in sub)
    n = len(sub)
    he = c["high"] + c["extreme"]
    rows_out.append([y, n, c["low"], c["moderate"], c["high"], c["extreme"], c["unclear"],
                     f"{pct(he, n)} ({he}/{n})"])
table(["год", "n", "low", "moderate", "high", "extreme", "unclear", "доля high+extreme"],
      rows_out)
print("\nB на уровне high по годам (экстрим отдельно не считаем — суммарно 7 строк за все годы):")
rows_out = []
for y in YEARS_WINDOW:
    sub = [r for r in VER if r["year"] == str(y) and r["axis1_level"] == "high"]
    rows_out.append([y, fmt_b(sub)])
table(["год", "B (axis1=high)"], rows_out)
ex_rows = [r for r in VER if r["axis1_level"] == "extreme"]
print(f"extreme за все годы: n={len(ex_rows)}, исходы: "
      f"{dict(Counter(r['outcome'] for r in ex_rows))}, годы: "
      f"{sorted(r['year'] for r in ex_rows)}")

# ---------------------------------------------------------------------------
section("B3. Динамика: состав axis3_class по годам + тянет ли big-AI ставку")
CLS_ORDER = ["rule-based", "classical-ml", "sensor-fusion", "hybrid", "deep-learning",
             "foundation-model", "agentic-llm", "unclear"]
rows_out = []
for y in YEARS_WINDOW:
    sub = [r for r in VER if r["year"] == str(y)]
    c = Counter(r["axis3_class"] for r in sub)
    n = len(sub)
    big = c["foundation-model"] + c["agentic-llm"]
    rows_out.append([y, n] + [c[k] for k in CLS_ORDER] + [f"{pct(big, n)}"])
table(["год", "n"] + CLS_ORDER + ["доля big-AI"], rows_out)
print("\nB по годам: big-AI (fm+agentic) vs все остальные классы (без unclear):")
rows_out = []
simpson = {}
for y in YEARS_WINDOW:
    sub = [r for r in VER if r["year"] == str(y)]
    big = [r for r in sub if r["axis3_class"] in BIG_AI]
    rest = [r for r in sub if r["axis3_class"] not in BIG_AI
            and r["axis3_class"] != "unclear"]
    simpson[y] = (B(big), B(rest))
    rows_out.append([y, fmt_b(big), fmt_b(rest)])
table(["год", "B big-AI", "B остальные"], rows_out)

# ---------------------------------------------------------------------------
section("B4. Динамика: доля gate=yes по годам + гейт-статус провалов по годам (без L15)")
VNO15 = no_l15(VER)
print(f"verified без Лекции 15: n={len(VNO15)}")
rows_out = []
for y in YEARS_WINDOW:
    sub = [r for r in VNO15 if r["year"] == str(y)]
    c = Counter(r["axis4_gate"] for r in sub)
    n = len(sub)
    rows_out.append([y, n, c["yes"], c["no"], c["not-applicable"], c["unclear"],
                     pct(c["yes"], n)])
table(["год", "n", "yes", "no", "n/a", "unclear", "доля yes"], rows_out)
print("\nСреди ПРОВАЛОВ (без L15): статус гейта по годам:")
rows_out = []
for y in YEARS_WINDOW:
    fails = [r for r in VNO15 if r["year"] == str(y) and r["outcome"] == "failure"]
    c = Counter(r["axis4_gate"] for r in fails)
    n = len(fails)
    noish = c["no"] + c["not-applicable"]
    rows_out.append([y, n, c["yes"], c["no"], c["not-applicable"], c["unclear"],
                     f"{pct(noish, n)} ({noish}/{n})"])
table(["год", "провалов", "yes", "no", "n/a", "unclear", "доля без гейта (no+n/a)"],
      rows_out)

# ---------------------------------------------------------------------------
section("C1. Big-AI провальность по годам: fm и agentic отдельно")
for cls in BIG_AI:
    print(f"\n### {cls}")
    rows_out = []
    for y in YEARS_WINDOW:
        sub = [r for r in VER if r["year"] == str(y) and r["axis3_class"] == cls]
        c = Counter(r["outcome"] for r in sub)
        rows_out.append([y, len(sub), c["success"], c["failure"], fmt_b(sub)])
    table(["год", "n", "S", "F", "B"], rows_out)

# ---------------------------------------------------------------------------
section("C2. Стабильность связки «провал ↔ нет гейта» по годам уже в B4; здесь — агрегат по эпохам")
for label, yrs in [("2022-2023", ("2022", "2023")), ("2024-2026", ("2024", "2025", "2026"))]:
    fails = [r for r in VNO15 if r["year"] in yrs and r["outcome"] == "failure"]
    c = Counter(r["axis4_gate"] for r in fails)
    n = len(fails)
    noish = c["no"] + c["not-applicable"]
    print(f"{label}: провалов {n}, из них без гейта (no+n/a) {noish} = {pct(noish, n)}, "
          f"при гейте {c['yes']} = {pct(c['yes'], n)}")

# ---------------------------------------------------------------------------
section("C3. Отрасль: величина расхождения original vs verified + состав-объяснение")
ind_rows = []
IND = sorted({r["industry"] for r in ALL} - {"unclear"})  # 13 строк V00-* вне 12-отраслевого словаря
for ind in IND:
    o = [r for r in ORIG if r["industry"] == ind]
    v = [r for r in VER if r["industry"] == ind]
    bo, so, fo, no_ = B(o)
    bv, sv, fv, nv = B(v)
    delta = (100 * (bv - bo)) if (bo is not None and bv is not None) else None
    # состав: доля big-AI, доля gate=yes, доля провалов в корпусе
    big_o = pct(sum(1 for r in o if r["axis3_class"] in BIG_AI), len(o))
    big_v = pct(sum(1 for r in v if r["axis3_class"] in BIG_AI), len(v))
    gate_o = pct(sum(1 for r in o if r["axis4_gate"] == "yes"), len(o))
    gate_v = pct(sum(1 for r in v if r["axis4_gate"] == "yes"), len(v))
    ind_rows.append([ind, f"{100*bo:.1f}% ({so}/{so+fo})", f"{100*bv:.1f}% ({sv}/{sv+fv})",
                     f"{delta:+.1f}", big_o, big_v, gate_o, gate_v])
ind_rows.sort(key=lambda r: -abs(float(r[3])))
table(["industry", "orig B", "verif B", "Δ п.п.", "big-AI% o", "big-AI% v",
       "gate=yes% o", "gate=yes% v"], ind_rows)

# Спирмен по рангам индустрий (12 точек) и по классам (7 точек)
def spearman(pairs):
    n = len(pairs)
    rx = {v: i for i, v in enumerate(sorted(p[0] for p in pairs))}
    ry = {v: i for i, v in enumerate(sorted(p[1] for p in pairs))}
    d2 = sum((rx[a] - ry[b]) ** 2 for a, b in pairs)
    return 1 - 6 * d2 / (n * (n * n - 1))

pairs_ind = []
for ind in IND:
    bo = B([r for r in ORIG if r["industry"] == ind])[0]
    bv = B([r for r in VER if r["industry"] == ind])[0]
    if bo is not None and bv is not None:
        pairs_ind.append((bo, bv))
print(f"\nSpearman ранговая корреляция B(original) vs B(verified) по 12 индустриям: "
      f"{spearman(pairs_ind):+.2f}")
pairs_cls = []
for cls in CLS_ORDER[:7]:
    bo = B([r for r in ORIG if r["axis3_class"] == cls])[0]
    bv = B([r for r in VER if r["axis3_class"] == cls])[0]
    if bo is not None and bv is not None:
        pairs_cls.append((bo, bv))
print(f"Spearman по 7 классам метода: {spearman(pairs_cls):+.2f}")
pairs_a1 = []
for lvl in ["low", "moderate", "high", "extreme"]:
    bo = B([r for r in ORIG if r["axis1_level"] == lvl])[0]
    bv = B([r for r in VER if r["axis1_level"] == lvl])[0]
    if bo is not None and bv is not None:
        pairs_a1.append((bo, bv))
print(f"(извлечь нельзя для extreme: B=0 в обоих — пар {len(pairs_a1)} из 4)")

# frontier-space разбор: verified-провалы поимённо
print("\nfrontier-space, verified, провалы поимённо (в original провалов 0):")
for r in VER:
    if r["industry"] == "frontier-space" and r["outcome"] == "failure":
        print(f"  {r['id']} | {r['year']} | {r['axis3_class']} | gate={r['axis4_gate']} | "
              f"{r['case_name']}")
print("\nsdlc, original: провалы по классам: ",
      dict(Counter(r["axis3_class"] for r in ORIG
                   if r["industry"] == "sdlc" and r["outcome"] == "failure")))
print("sdlc, verified: провалы по классам: ",
      dict(Counter(r["axis3_class"] for r in VER
                   if r["industry"] == "sdlc" and r["outcome"] == "failure")))
print("cad-cam, original: исходы по классам (S/F): ")
for cls in CLS_ORDER:
    sub = [r for r in ORIG if r["industry"] == "cad-cam" and r["axis3_class"] == cls]
    if sub:
        c = Counter(r["outcome"] for r in sub)
        print(f"  {cls}: S={c['success']} P={c['partial']} F={c['failure']} U={c['undetermined']}")
print("cad-cam, verified: исходы по классам: ")
for cls in CLS_ORDER:
    sub = [r for r in VER if r["industry"] == "cad-cam" and r["axis3_class"] == cls]
    if sub:
        c = Counter(r["outcome"] for r in sub)
        print(f"  {cls}: S={c['success']} P={c['partial']} F={c['failure']} U={c['undetermined']}")

# ---------------------------------------------------------------------------
section("C4. Simpson-проверка: объясняет ли сдвиг состава классов годовой тренд B")
# B по годам при фиксированном составе: усредняем B внутри классов весами 2022 года
print("Внутриклассовые B по годам (big-AI vs не-big-AI) уже в B3; здесь противоположный разрез:")
for grp_label, grp in [("big-AI", BIG_AI),
                       ("не-big-AI (без unclear)", None)]:
    sub_all = [r for r in VER if (r["axis3_class"] in grp if grp
               else r["axis3_class"] not in BIG_AI and r["axis3_class"] != "unclear")]
    print(f"  {grp_label} суммарно за 2022-2026: {fmt_b([r for r in sub_all if r['year'] in [str(y) for y in YEARS_WINDOW]])}")

# ===========================================================================
# ГРАФИКИ
# ===========================================================================
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.alpha"] = 0.25

# -- chart-dyn-success-by-year ------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6.5))
series = [
    ("все кейсы verified", None, "#21295C", "o", (-16, 8)),
    ("большой ИИ (fm+agentic)", lambda r: r["axis3_class"] in BIG_AI, "#B23A48", "s",
     (0, -16)),
    ("остальные классы", lambda r: r["axis3_class"] not in BIG_AI
        and r["axis3_class"] != "unclear", "#2E7D32", "^", (16, 8)),
]
for label, pred, color, marker, off in series:
    xs, ys, ns = [], [], []
    for y in YEARS_WINDOW:
        sub = [r for r in VER if r["year"] == str(y) and (pred is None or pred(r))]
        b, s, f, n = B(sub)
        if b is not None:
            xs.append(y)
            ys.append(100 * b)
            ns.append(s + f)
    ax.plot(xs, ys, color=color, marker=marker, linewidth=2, markersize=7, label=label)
    for x, yv, n in zip(xs, ys, ns):
        ax.annotate(f"n={n}", (x, yv), textcoords="offset points", xytext=off,
                    ha="center", fontsize=8, color=color)
ax.axvspan(2025.5, 2026.5, color="#B0B0B0", alpha=0.15)
ax.text(2026, ax.get_ylim()[0] + 3, "2026\nнеполный", ha="center", fontsize=8,
        color="#555555")
ax.set_xticks(YEARS_WINDOW)
ax.set_ylabel("Доля успеха, формула B = S/(S+F), %")
ax.set_title(f"Verified-реестр ({len(VER)}): доля успеха по годам, 2018–2026\n"
             "n у точки = знаменатель формулы B (S+F)")
ax.legend(loc="lower left", fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(ASSETS, "chart-dyn-success-by-year.png"), dpi=150)
plt.close(fig)

# -- chart-dyn-class-composition-by-year -------------------------------------
CLS_COLORS = {
    "rule-based": "#8D99AE",
    "classical-ml": "#1C7293",
    "sensor-fusion": "#65A7C5",
    "hybrid": "#028090",
    "deep-learning": "#F0AB00",
    "foundation-model": "#B23A48",
    "agentic-llm": "#6A0F49",
    "unclear": "#D9D9D9",
}
fig, ax = plt.subplots(figsize=(10, 6.5))
bottoms = np.zeros(len(YEARS_WINDOW))
year_n = {y: len([r for r in VER if r["year"] == str(y)]) for y in YEARS_WINDOW}
for cls in CLS_ORDER:
    vals = []
    for y in YEARS_WINDOW:
        c = sum(1 for r in VER if r["year"] == str(y) and r["axis3_class"] == cls)
        vals.append(100 * c / year_n[y])
    ax.bar(YEARS_WINDOW, vals, bottom=bottoms, color=CLS_COLORS[cls], label=cls,
           width=0.62, edgecolor="white", linewidth=0.5)
    bottoms += np.array(vals)
for i, y in enumerate(YEARS_WINDOW):
    ax.text(y, 101.5, f"n={year_n[y]}", ha="center", fontsize=8, color="#444444")
ax.set_ylim(0, 106)
ax.set_xticks(YEARS_WINDOW)
ax.set_ylabel("Доля кейсов года, %")
ax.set_title("Verified-реестр: состав классов метода по годам (100% = все кейсы года)")
ax.legend(loc="center left", bbox_to_anchor=(1.0, 0.5), fontsize=8)
fig.tight_layout()
fig.savefig(os.path.join(ASSETS, "chart-dyn-class-composition-by-year.png"), dpi=150)
plt.close(fig)

# -- chart-dyn-axis1-by-year --------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.6))
ax = axes[0]
he_share, lo_share = [], []
for y in YEARS_WINDOW:
    sub = [r for r in VER if r["year"] == str(y)]
    c = Counter(r["axis1_level"] for r in sub)
    he_share.append(100 * (c["high"] + c["extreme"]) / len(sub))
    lo_share.append(100 * (c["low"] + c["moderate"]) / len(sub))
ax.plot(YEARS_WINDOW, he_share, color="#B23A48", marker="o", linewidth=2,
        label="high+extreme")
ax.plot(YEARS_WINDOW, lo_share, color="#2E7D32", marker="o", linewidth=2,
        label="low+moderate")
ax.set_xticks(YEARS_WINDOW)
ax.set_ylabel("Доля кейсов года, %")
ax.set_title("Доля уровней неопределённости по годам")
ax.legend(fontsize=9)
ax = axes[1]
xs, ys, ns = [], [], []
for y in YEARS_WINDOW:
    sub = [r for r in VER if r["year"] == str(y) and r["axis1_level"] == "high"]
    b, s, f, n = B(sub)
    if b is not None:
        xs.append(y); ys.append(100 * b); ns.append(s + f)
ax.plot(xs, ys, color="#21295C", marker="o", linewidth=2)
for x, yv, n in zip(xs, ys, ns):
    flag = " ⚠" if n < 10 else ""
    ax.annotate(f"n={n}{flag}", (x, yv), textcoords="offset points", xytext=(0, 9),
                ha="center", fontsize=8)
ax.set_xticks(YEARS_WINDOW)
ax.set_ylabel("B на axis1=high, %")
ax.set_title("Доля успеха на ВЫСОКОЙ неопределённости по годам\n(⚠ = знаменатель <10)")
fig.suptitle("Verified-реестр: сдвигается ли граница неопределённости со временем", y=1.0)
fig.tight_layout()
fig.savefig(os.path.join(ASSETS, "chart-dyn-axis1-by-year.png"), dpi=150)
plt.close(fig)

# -- chart-dyn-gate-by-year ---------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.6))
ax = axes[0]
ys_ = []
for y in YEARS_WINDOW:
    sub = [r for r in VNO15 if r["year"] == str(y)]
    c = Counter(r["axis4_gate"] for r in sub)
    ys_.append(100 * c["yes"] / len(sub))
ax.plot(YEARS_WINDOW, ys_, color="#21295C", marker="o", linewidth=2)
for x, yv, y in zip(YEARS_WINDOW, ys_, YEARS_WINDOW):
    n = len([r for r in VNO15 if r["year"] == str(y)])
    ax.annotate(f"n={n}", (x, yv), textcoords="offset points", xytext=(0, 9),
                ha="center", fontsize=8)
ax.set_xticks(YEARS_WINDOW)
ax.set_ylabel("Доля gate=yes среди всех кейсов года, %")
ax.set_title("Распространённость гейта по годам (без Лекции 15)")
ax = axes[1]
GATE_COLORS = {"no": "#B23A48", "not-applicable": "#F0AB00", "yes": "#2E7D32",
               "unclear": "#B0B0B0"}
bottoms = np.zeros(len(YEARS_WINDOW))
for g in ["no", "not-applicable", "yes", "unclear"]:
    vals = []
    for y in YEARS_WINDOW:
        fails = [r for r in VNO15 if r["year"] == str(y) and r["outcome"] == "failure"]
        c = Counter(r["axis4_gate"] for r in fails)
        vals.append(100 * c[g] / len(fails) if fails else 0)
    ax.bar(YEARS_WINDOW, vals, bottom=bottoms, color=GATE_COLORS[g],
           label=f"gate={g}", width=0.62, edgecolor="white", linewidth=0.5)
    bottoms += np.array(vals)
for y in YEARS_WINDOW:
    nf = len([r for r in VNO15 if r["year"] == str(y) and r["outcome"] == "failure"])
    ax.text(y, 101.5, f"F={nf}", ha="center", fontsize=8, color="#444444")
ax.set_ylim(0, 106)
ax.set_xticks(YEARS_WINDOW)
ax.set_ylabel("Доля провалов года, %")
ax.set_title("Статус гейта у ПРОВАЛОВ по годам (без Лекции 15)")
ax.legend(fontsize=8, loc="center left", bbox_to_anchor=(1.0, 0.5))
fig.suptitle("Verified-реестр: гейт во времени — распространённость и связка с провалом", y=1.0)
fig.tight_layout()
fig.savefig(os.path.join(ASSETS, "chart-dyn-gate-by-year.png"), dpi=150)
plt.close(fig)

# -- chart-cmp-industry-dumbbell ---------------------------------------------
fig, ax = plt.subplots(figsize=(10.5, 7))
rows_d = []
for ind in IND:
    bo, so, fo, _ = B([r for r in ORIG if r["industry"] == ind])
    bv, sv, fv, _ = B([r for r in VER if r["industry"] == ind])
    rows_d.append((ind, 100 * bo, 100 * bv, so + fo, sv + fv))
rows_d.sort(key=lambda t: abs(t[2] - t[1]))
ypos = np.arange(len(rows_d))
for i, (ind, bo, bv, no_, nv) in enumerate(rows_d):
    ax.plot([bo, bv], [i, i], color="#B0B0B0", linewidth=2, zorder=1)
    ax.scatter([bo], [i], s=70, color="#21295C", zorder=2,
               label="original (лекции)" if i == 0 else None)
    ax.scatter([bv], [i], s=70, color="#F0AB00", edgecolor="#8a6200", zorder=2,
               label="verified (внешние)" if i == 0 else None)
    ax.annotate(f"{bo:.0f}% ({no_})", (bo, i), textcoords="offset points",
                xytext=(0, -14), ha="center", fontsize=7, color="#21295C")
    ax.annotate(f"{bv:.0f}% ({nv})", (bv, i), textcoords="offset points",
                xytext=(0, 8), ha="center", fontsize=7, color="#8a6200")
ax.set_yticks(ypos, [r[0] for r in rows_d])
ax.set_xlabel("Доля успеха, формула B, % (в скобках — знаменатель S+F)")
ax.set_title("Отрасль — ось наименьшего согласия: B по 12 индустриям,\n"
             "original (421, материал лекций) против verified (248, внешние источники);\n"
             "сортировка по |Δ|, самое большое расхождение сверху")
ax.legend(loc="lower right", fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(ASSETS, "chart-cmp-industry-dumbbell.png"), dpi=150)
plt.close(fig)

# -- chart-cmp-tornado-two-datasets ------------------------------------------
fig, ax = plt.subplots(figsize=(10.5, 6))
dims = [d for d, _ in tornado_data["original"]]
o_spread = dict(tornado_data["original"])
v_spread = dict(tornado_data["verified"])
order = sorted(dims, key=lambda d: o_spread[d])
ypos = np.arange(len(order))
ax.barh(ypos + 0.19, [o_spread[d] for d in order], height=0.36, color="#21295C",
        label="original (421)")
ax.barh(ypos - 0.19, [v_spread[d] for d in order], height=0.36, color="#F0AB00",
        label="verified (248)")
for i, d in enumerate(order):
    ax.text(o_spread[d] + 0.8, i + 0.19, f"{o_spread[d]:.1f}", va="center", fontsize=8,
            color="#21295C")
    ax.text(v_spread[d] + 0.8, i - 0.19, f"{v_spread[d]:.1f}", va="center", fontsize=8,
            color="#8a6200")
ax.set_yticks(ypos, order)
ax.set_xlabel("Разброс доли успеха B между уровнями измерения, п.п.")
ax.set_title("Рейтинг измерений по разбросу B: original против verified\n"
             "(гейт — без Лекции 15; у original — реплика tornado файла 10 §3 формулой B)")
ax.legend(fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(ASSETS, "chart-cmp-tornado-two-datasets.png"), dpi=150)
plt.close(fig)

print("\nCHARTS WRITTEN:")
for f in ["chart-dyn-success-by-year.png", "chart-dyn-class-composition-by-year.png",
          "chart-dyn-axis1-by-year.png", "chart-dyn-gate-by-year.png",
          "chart-cmp-industry-dumbbell.png", "chart-cmp-tornado-two-datasets.png"]:
    p = os.path.join(ASSETS, f)
    print(f"  {f}: {'OK' if os.path.exists(p) else 'MISSING'} "
          f"({os.path.getsize(p)} bytes)" if os.path.exists(p) else f"  {f}: MISSING")
