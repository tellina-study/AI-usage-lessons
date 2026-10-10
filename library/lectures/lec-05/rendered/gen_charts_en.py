"""Lecture 5 (EN) — matplotlib charts (Ocean palette, no default styling).

EN twin of gen_charts.py: same datasets/layouts, English axis/bar labels.
Output: assets/charts-en/<name>.png (transparent bg).

Palette: DEEP #21295C, MID #065A82, LIGHT #1C7293, TEAL #028090,
GOLD #F0AB00, SURFACE #F4F7FA.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

REND = Path(__file__).resolve().parent
OUT = REND / "assets/charts-en"
OUT.mkdir(parents=True, exist_ok=True)

DEEP = "#21295C"; MID = "#065A82"; LIGHT = "#1C7293"; TEAL = "#028090"
GOLD = "#F0AB00"; SURFACE = "#F4F7FA"; GREY = "#D9E2EC"; SLATE = "#5B6678"

# Cyrillic-safe font (kept for consistency, not needed for EN glyphs)
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


# ── s18: WCAG 29% donut (of 21,880 evaluations) ──
def c_wcag():
    fig, ax = plt.subplots(figsize=(4.4, 4.4))
    vals = [29.0, 71.0]
    ax.pie(vals, colors=[GOLD, GREY], startangle=90, counterclock=False,
           wedgeprops=dict(width=0.42, edgecolor="white", linewidth=2))
    ax.text(0, 0.08, "29%", ha="center", va="center", fontsize=44,
            fontweight="bold", color=DEEP)
    ax.text(0, -0.30, "WCAG compliance", ha="center", va="center",
            fontsize=12, color=SLATE)
    ax.set_aspect("equal")
    save(fig, "c-wcag-29.png")


# ── s23: +200% code vs 16% reviewed (contrast bars) ──
def c_review_bottleneck():
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    bars = ax.bar(["code volume\nper engineer", "PRs with substantive\nhuman review"],
                  [200, 16], color=[GOLD, LIGHT], width=0.56, zorder=3)
    ax.bar_label(bars, labels=["+200%", "16%"], fontsize=17, fontweight="bold",
                 color=DEEP, padding=4)
    ax.set_ylim(0, 230)
    ax.set_ylabel("% year over year / share of PRs", fontsize=11)
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
            marker="o", markersize=4, label="pass@k (at least 1 of k)")
    ax.plot(ks, [v * 100 for v in pow_k], color=GOLD, linewidth=3,
            marker="s", markersize=4, label="pass^k (all k succeed)")
    ax.set_xlabel("k (number of runs)", fontsize=11)
    ax.set_ylabel("probability, %", fontsize=11)
    ax.set_ylim(0, 105)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color=GREY, linewidth=0.7)
    ax.legend(fontsize=10, frameon=False, loc="center right")
    ax.tick_params(labelsize=10)
    save(fig, "c-passk.png")


# ── s40: Zillow — bought against sold in the third quarter of 2021 ──
# EN twin of gen_charts.py::c_zillow after the #212 fix (student-roast
# 2026-09-30): there were TWO charts side by side here, captioned "do NOT
# compare bar lengths directly" — $304-408M on one scale and ~$80K on the
# other. The student compared them by eye before finishing the warning, and
# that is to be expected: two charts side by side READ as a comparison
# whatever is written under them. A warning you have to write is a symptom
# of a bad chart, not a cure for one. Now there is ONE chart, and both
# quantities on it are in the SAME unit (homes), so comparing them is not
# only allowed but required: that gap — 9,680 bought against 3,032 sold in a
# single quarter — IS the mechanism of the failure. The money figures stay
# in the slide's text block.
def c_zillow():
    fig, ax = plt.subplots(figsize=(7.4, 2.9))
    bars = ax.barh(["Bought", "Sold"], [9680, 3032],
                   color=[GOLD, LIGHT], height=0.52, zorder=3)
    ax.bar_label(bars, labels=["9,680 homes", "3,032 homes"], fontsize=13,
                 fontweight="bold", color=DEEP, padding=8)
    ax.invert_yaxis()
    ax.set_xlim(0, 13200)
    ax.set_xticks([0, 3000, 6000, 9000])
    ax.set_xticklabels(["0", "3,000", "6,000", "9,000"])
    ax.set_xlabel("homes in the third quarter of 2021 · a gap of 6,648 homes "
                  "in one quarter — that is what had to be written down",
                  fontsize=10, color=SLATE, labelpad=8)
    ax.set_title("Zillow Offers: homes bought and homes sold",
                 fontsize=12, fontweight="bold", color=DEEP, pad=12,
                 loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="x", color=GREY, linewidth=0.7, zorder=0)
    ax.tick_params(labelsize=11)
    save(fig, "c-zillow.png")


# ── s47: MIT funnel 60→20→5 (of surveyed) ──
def c_mit_funnel():
    fig, ax = plt.subplots(figsize=(5.8, 3.4))
    stages = ["explored", "reached a pilot", "succeeded"]
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
    ax.text(36, -0.55, "% of all companies surveyed (MIT)", ha="center",
            fontsize=10, color=SLATE)
    save(fig, "c-mit-funnel.png")


# ── s47: Gartner 782 success of 3400+ pilots ──
def c_gartner():
    fig, ax = plt.subplots(figsize=(4.2, 4.2))
    vals = [782, 3400 - 782]
    ax.pie(vals, colors=[GOLD, GREY], startangle=90, counterclock=False,
           wedgeprops=dict(width=0.42, edgecolor="white", linewidth=2))
    ax.text(0, 0.10, "~23%", ha="center", va="center", fontsize=34,
            fontweight="bold", color=DEEP)
    ax.text(0, -0.28, "782 of 3,400+\npilots — success", ha="center",
            va="center", fontsize=11, color=SLATE)
    ax.set_aspect("equal")
    save(fig, "c-gartner.png")


# ── s48: Just Walk Out 700/1000 vs target 50/1000 ──
def c_jwo():
    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    bars = ax.bar(["actual:\nmanual review", "target"],
                  [700, 50], color=[GOLD, LIGHT], width=0.52, zorder=3)
    ax.bar_label(bars, labels=["700 / 1000", "50 / 1000"], fontsize=15,
                 fontweight="bold", color=DEEP, padding=4)
    ax.set_ylim(0, 800)
    ax.set_ylabel("transactions per 1,000", fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color=GREY, linewidth=0.7, zorder=0)
    ax.tick_params(labelsize=10.5)
    save(fig, "c-jwo.png")


# ── s42: Klarna automation 700 → 853 FTE-eq ──
def c_klarna():
    fig, ax = plt.subplots(figsize=(5.0, 3.0))
    bars = ax.bar(["before the\npolicy reversal", "after the\npolicy reversal"],
                  [700, 853], color=[LIGHT, GOLD], width=0.5, zorder=3)
    ax.bar_label(bars, labels=["~700", "853"], fontsize=15, fontweight="bold",
                 color=DEEP, padding=4)
    ax.set_ylim(0, 950)
    ax.set_ylabel("automation FTE-equivalent", fontsize=10.5)
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
