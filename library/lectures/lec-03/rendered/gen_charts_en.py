"""EN chart generator for Лекция 3 (issue #172 Ф3).

Regenerates the 3 charts with baked-in Cyrillic into English, matching the
original Ocean-palette visual style. Outputs to assets/charts-en/.
c29-nanda.png has NO embedded text → copied verbatim by the caller (not here).

Run: python3 gen_charts_en.py   (from rendered/)
"""
import shutil
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "assets" / "charts"
OUT = ROOT / "assets" / "charts-en"
OUT.mkdir(parents=True, exist_ok=True)

# Ocean palette (mirror build_v3.py)
DEEP = "#21295C"
MID = "#065A82"
LIGHT = "#1C7293"
TEAL = "#028090"
GOLD = "#F0AB00"
CREAM = "#FCEFCB"      # filled area under c08 (soft gold tint)
STEEL_TINT = "#E7EEF3"  # filled area under c23 (soft steel tint)

FB = FontProperties(family="DejaVu Sans")


def style_axes(ax):
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color(LIGHT)
    ax.spines["bottom"].set_color(LIGHT)
    ax.tick_params(colors=LIGHT)


# ============================================================
# c08 — retrieval accuracy decays as context grows
# ============================================================
def chart_c08():
    x = [8, 32, 64, 128, 256, 512]
    y = [97, 93, 86, 76, 63, 48]
    xi = list(range(len(x)))
    fig, ax = plt.subplots(figsize=(14.8, 9.0), dpi=200)
    ax.plot(xi, y, color=MID, lw=5, zorder=3)
    ax.scatter(xi, y, s=260, color=MID, zorder=4, edgecolors="white", linewidths=2)
    ax.fill_between(xi, y, 40, color=CREAM, zorder=1)
    ax.set_xlim(-0.15, len(x) - 0.85)
    ax.set_ylim(40, 100)
    ax.set_xticks(xi)
    ax.set_xticklabels([f"{v}k" for v in x], fontsize=26, fontweight="bold",
                       color=MID, fontproperties=FB)
    ax.set_yticks([40, 50, 60, 70, 80, 90, 100])
    ax.tick_params(axis="y", labelsize=22)
    for lbl in ax.get_yticklabels():
        lbl.set_color(MID)
        lbl.set_fontproperties(FB)
    ax.text(0.5, 1.105, "Retrieval accuracy ↓ as the context grows",
            transform=ax.transAxes, ha="center", fontsize=34, fontweight="bold",
            color=DEEP, fontproperties=FB)
    ax.text(0.5, 1.04,
            "SCHEMATIC — illustration of the effect, not measured data · "
            "effect: Chroma Research, 2025",
            transform=ax.transAxes, ha="center", fontsize=17, style="italic",
            color=GOLD, fontproperties=FB)
    ax.set_ylabel("retrieval accuracy", fontsize=20, style="italic", color=LIGHT,
                  fontproperties=FB)
    ax.set_xlabel("tokens in context   →", fontsize=22, style="italic",
                  color=TEAL, labelpad=14, fontproperties=FB)
    style_axes(ax)
    ax.grid(axis="y", color="#E3E8ED", lw=1)
    ax.set_axisbelow(True)
    fig.subplots_adjust(top=0.86, bottom=0.14)
    fig.savefig(OUT / "c08-context-rot.png", dpi=200, facecolor="white")
    plt.close(fig)


# ============================================================
# c16 — narrow aggressive fine-tuning: target up, general abilities down
# ============================================================
def chart_c16():
    x = list(range(6))
    target = [55, 72, 84, 91, 95, 97]
    general = [90, 86, 79, 68, 55, 42]
    fig, ax = plt.subplots(figsize=(14.8, 9.2), dpi=200)
    ax.plot(x, target, color=TEAL, lw=5, zorder=3,
            label="Target metric (rises)")
    ax.scatter(x, target, s=260, color=TEAL, zorder=4, edgecolors="white",
               linewidths=2)
    ax.plot(x, general, color=GOLD, lw=5, ls=(0, (6, 4)), zorder=3,
            label="General abilities (drop unnoticed)")
    ax.scatter(x, general, s=260, color=GOLD, zorder=4, edgecolors="white",
               linewidths=2)
    ax.set_xlim(-0.2, 5.2)
    ax.set_ylim(30, 100)
    ax.set_xticks(x)
    ax.set_xticklabels([str(v) for v in x], fontsize=26, color=MID,
                       fontproperties=FB)
    ax.set_yticks([30, 40, 50, 60, 70, 80, 90, 100])
    ax.tick_params(axis="y", labelsize=22)
    for lbl in ax.get_yticklabels():
        lbl.set_color(MID)
        lbl.set_fontproperties(FB)
    ax.text(0.5, 1.11, "Narrow aggressive fine-tuning: target ↑, "
            "general abilities ↓",
            transform=ax.transAxes, ha="center", fontsize=31, fontweight="bold",
            color=DEEP, fontproperties=FB)
    ax.text(0.5, 1.045,
            "SCHEMATIC — illustration of the effect, not measured data · "
            "effect: Luo et al., arXiv:2308.08747, 2023",
            transform=ax.transAxes, ha="center", fontsize=16, style="italic",
            color=GOLD, fontproperties=FB)
    ax.set_xlabel("narrow fine-tuning epochs   →", fontsize=22,
                  style="italic", color=TEAL, labelpad=14, fontproperties=FB)
    style_axes(ax)
    ax.grid(axis="y", color="#EEF1F4", lw=1)
    ax.set_axisbelow(True)
    leg = ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.11), ncol=2,
                    fontsize=20, frameon=False, prop=FB)
    for txt in leg.get_texts():
        txt.set_color(DEEP)
    fig.subplots_adjust(top=0.86, bottom=0.14)
    fig.savefig(OUT / "c16-forgetting.png", dpi=200, facecolor="white",
                bbox_inches="tight")
    plt.close(fig)


# ============================================================
# c23 — reliabilities multiply along the chain
# ============================================================
def chart_c23():
    x = [1, 5, 10, 15, 20]
    y = [99, 95, 90, 86, 82]
    fig, ax = plt.subplots(figsize=(12.4, 7.2), dpi=200)
    ax.plot(x, y, color=MID, lw=4.5, zorder=3)
    ax.fill_between(x, y, 75, color=STEEL_TINT, zorder=1)
    # base markers
    ax.scatter(x, y, s=210, color=MID, zorder=4)
    # gold-highlight markers at x=5 and x=20
    for gx, gy in [(5, 95), (20, 82)]:
        ax.scatter([gx], [gy], s=230, color=GOLD, zorder=5,
                   edgecolors=MID, linewidths=2)
    ax.set_xlim(0.4, 20.6)
    ax.set_ylim(75, 100)
    ax.set_xticks(x)
    ax.set_xticklabels([str(v) for v in x], fontsize=24, color=MID,
                       fontproperties=FB)
    ax.set_yticks([75, 80, 85, 90, 95, 100])
    ax.set_yticklabels([f"{v}%" for v in [75, 80, 85, 90, 95, 100]],
                       fontsize=22, color=MID, fontproperties=FB)
    ax.text(0.5, 1.055, "5×99% ≈ 95%, 10 ≈ 90%, 20 ≈ 82% — "
            "reliabilities multiply",
            transform=ax.transAxes, ha="center", fontsize=27, fontweight="bold",
            color=DEEP, fontproperties=FB)
    ax.set_xlabel("number of steps in the chain", fontsize=22, style="italic",
                  color=TEAL, labelpad=14, fontproperties=FB)
    style_axes(ax)
    ax.grid(axis="y", color="#E3E8ED", lw=1)
    ax.set_axisbelow(True)
    fig.subplots_adjust(top=0.86, bottom=0.14)
    fig.savefig(OUT / "c23-compounding.png", dpi=200, facecolor="white")
    plt.close(fig)


def copy_c29():
    shutil.copy(SRC / "c29-nanda.png", OUT / "c29-nanda.png")


if __name__ == "__main__":
    chart_c08()
    chart_c16()
    chart_c23()
    copy_c29()
    print("EN charts written to", OUT)
