"""Лекция 5 — matplotlib charts (Ocean palette, no default styling).

Each chart backs a data slide with a real dataset + baseline/denominator.
Output: assets/charts/<name>.png (transparent bg, DejaVu Cyrillic-safe).

Palette: DEEP #21295C, MID #065A82, LIGHT #1C7293, TEAL #028090,
GOLD #F0AB00, SURFACE #F4F7FA.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

REND = Path(__file__).resolve().parent
OUT = REND / "assets/charts"
OUT.mkdir(parents=True, exist_ok=True)

DEEP = "#21295C"; MID = "#065A82"; LIGHT = "#1C7293"; TEAL = "#028090"
GOLD = "#F0AB00"; SURFACE = "#F4F7FA"; GREY = "#D9E2EC"; SLATE = "#5B6678"

# Cyrillic-safe font
for fp in ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
    if Path(fp).exists():
        font_manager.fontManager.addfont(fp)
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.edgecolor"] = SLATE
plt.rcParams["text.color"] = DEEP
plt.rcParams["axes.labelcolor"] = DEEP
plt.rcParams["xtick.color"] = SLATE
plt.rcParams["ytick.color"] = SLATE


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, transparent=True, bbox_inches="tight")
    plt.close(fig)
    print(f"OK {name}")


# ── s18: WCAG 29% donut (of 21 880 evaluations) ──
def c_wcag():
    fig, ax = plt.subplots(figsize=(4.4, 4.4))
    vals = [29.0, 71.0]
    ax.pie(vals, colors=[GOLD, GREY], startangle=90, counterclock=False,
           wedgeprops=dict(width=0.42, edgecolor="white", linewidth=2))
    ax.text(0, 0.08, "29%", ha="center", va="center", fontsize=44,
            fontweight="bold", color=DEEP)
    ax.text(0, -0.30, "проверок пройдено", ha="center", va="center",
            fontsize=12, color=SLATE)
    ax.set_aspect("equal")
    save(fig, "c-wcag-29.png")


# ── s23: +200% code vs 16% reviewed (contrast bars) ──
def c_review_bottleneck():
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    bars = ax.bar(["объём кода\nна инженера", "PR с содержательным\nчеловеческим ревью"],
                  [200, 16], color=[GOLD, LIGHT], width=0.56, zorder=3)
    ax.bar_label(bars, labels=["+200%", "16%"], fontsize=17, fontweight="bold",
                 color=DEEP, padding=4)
    ax.set_ylim(0, 230)
    ax.set_ylabel("% год к году / доля PR", fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color=GREY, linewidth=0.7, zorder=0)
    ax.tick_params(labelsize=10.5)
    save(fig, "c-review-bottleneck.png")


# ── s31: pass@k vs pass^k diverging (base p=0.9) ──
def c_passk():
    ks = list(range(1, 16))
    p = 0.9
    at_k = [1 - (1 - p) ** k for k in ks]          # at least 1 success
    pow_k = [p ** k for k in ks]                     # all k succeed
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    ax.plot(ks, [v * 100 for v in at_k], color=TEAL, linewidth=3,
            marker="o", markersize=4, label="pass@k (хотя бы 1 из k)")
    ax.plot(ks, [v * 100 for v in pow_k], color=GOLD, linewidth=3,
            marker="s", markersize=4, label="pass^k (все k успешны)")
    ax.set_xlabel("k (число прогонов)", fontsize=11)
    ax.set_ylabel("вероятность, %", fontsize=11)
    ax.set_ylim(0, 105)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color=GREY, linewidth=0.7)
    ax.legend(fontsize=10, frameon=False, loc="center right")
    ax.tick_params(labelsize=10)
    save(fig, "c-passk.png")


# ── s40: Zillow — куплено против проданного за III квартал 2021 ──
# ПРАВКА #212 (student-roast 2026-09-30, правка 5): здесь стояли ДВЕ
# диаграммы рядом с подписью «длины баров НЕ сравнивать напрямую» —
# $304-408 млн на одной шкале и ≈$80 тыс. на другой. Студент сравнил их
# глазами раньше, чем дочитал предупреждение, и это закономерно: две
# диаграммы рядом ЧИТАЮТСЯ как сравнение, что бы ни было написано под ними.
# Предупреждение, которое приходится писать, — признак негодной схемы, а не
# лекарство от неё. Теперь диаграмма одна, и обе величины на ней в ОДНИХ
# единицах (дома), так что сравнивать их не только можно, но и нужно: именно
# этот разрыв — 9 680 купленных против 3 032 проданных за один квартал — и
# есть механизм провала. Денежные суммы остались в текстовом блоке слайда.
def c_zillow():
    fig, ax = plt.subplots(figsize=(7.4, 2.9))
    bars = ax.barh(["Куплено", "Продано"], [9680, 3032],
                   color=[GOLD, LIGHT], height=0.52, zorder=3)
    ax.bar_label(bars, labels=["9 680 домов", "3 032 дома"], fontsize=13,
                 fontweight="bold", color=DEEP, padding=8)
    ax.invert_yaxis()
    ax.set_xlim(0, 13200)
    ax.set_xticks([0, 3000, 6000, 9000])
    ax.set_xticklabels(["0", "3 000", "6 000", "9 000"])
    ax.set_xlabel("домов за III квартал 2021 года · разрыв в 6 648 домов "
                  "за один квартал — это и есть то, что пришлось списать",
                  fontsize=10, color=SLATE, labelpad=8)
    ax.set_title("Zillow Offers: сколько домов купили и сколько продали",
                 fontsize=12, fontweight="bold", color=DEEP, pad=12,
                 loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="x", color=GREY, linewidth=0.7, zorder=0)
    ax.tick_params(labelsize=11)
    save(fig, "c-zillow.png")


# ── s47: MIT funnel 60→20→5 (of surveyed) ──
def c_mit_funnel():
    fig, ax = plt.subplots(figsize=(5.8, 3.4))
    stages = ["исследовали", "дошли до пилота", "успех"]
    vals = [60, 20, 5]
    colors = [LIGHT, MID, GOLD]
    y = [2, 1, 0]
    for yi, v, c, s in zip(y, vals, colors, stages):
        ax.barh(yi, v, color=c, height=0.62, zorder=3)
        ax.text(v + 1.5, yi, f"{v}%", va="center", fontsize=15,
                fontweight="bold", color=DEEP)
        ax.text(-1.5, yi, s, va="center", ha="right", fontsize=11.5,
                color=DEEP)
    ax.set_xlim(0, 72)
    ax.set_ylim(-0.6, 2.6)
    ax.axis("off")
    # ПРАВКА #212 (правило Р5): «MIT» в подписи графика — нераскрытое
    # сокращение в видимом слое. Расшифровка теперь стоит в тексте слайда,
    # подпись графика говорит только про знаменатель.
    ax.text(36, -0.55, "% от всех опрошенных компаний", ha="center",
            fontsize=10, color=SLATE)
    save(fig, "c-mit-funnel.png")


# ── s47: Gartner 782 success of 3400+ pilots ──
def c_gartner():
    fig, ax = plt.subplots(figsize=(4.2, 4.2))
    vals = [782, 3400 - 782]
    ax.pie(vals, colors=[GOLD, GREY], startangle=90, counterclock=False,
           wedgeprops=dict(width=0.42, edgecolor="white", linewidth=2))
    ax.text(0, 0.10, "≈23%", ha="center", va="center", fontsize=34,
            fontweight="bold", color=DEEP)
    ax.text(0, -0.28, "782 из 3400+\nпилотов — успех", ha="center",
            va="center", fontsize=11, color=SLATE)
    ax.set_aspect("equal")
    save(fig, "c-gartner.png")


# ── s48: Just Walk Out 700/1000 vs target 50/1000 ──
def c_jwo():
    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    bars = ax.bar(["факт:\nручная проверка", "цель"],
                  [700, 50], color=[GOLD, LIGHT], width=0.52, zorder=3)
    ax.bar_label(bars, labels=["700 / 1000", "50 / 1000"], fontsize=15,
                 fontweight="bold", color=DEEP, padding=4)
    ax.set_ylim(0, 800)
    ax.set_ylabel("транзакций на 1000", fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color=GREY, linewidth=0.7, zorder=0)
    ax.tick_params(labelsize=10.5)
    save(fig, "c-jwo.png")


# ── s42: Klarna automation 700 → 853 FTE-eq ──
def c_klarna():
    fig, ax = plt.subplots(figsize=(5.0, 3.0))
    bars = ax.bar(["до отката", "после отката\nполитики"], [700, 853],
                  color=[LIGHT, GOLD], width=0.5, zorder=3)
    ax.bar_label(bars, labels=["≈700", "853"], fontsize=15, fontweight="bold",
                 color=DEEP, padding=4)
    ax.set_ylim(0, 950)
    ax.set_ylabel("чел.-эквивалент автоматизации", fontsize=10.5)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color=GREY, linewidth=0.7, zorder=0)
    ax.tick_params(labelsize=10.5)
    save(fig, "c-klarna.png")


if __name__ == "__main__":
    c_wcag()
    c_review_bottleneck()
    c_passk()
    c_zillow()
    c_mit_funnel()
    c_gartner()
    c_jwo()
    c_klarna()
