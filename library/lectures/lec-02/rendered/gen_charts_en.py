#!/usr/bin/env python3
"""
EN chart generator for lec-02 (issue #172 Ф3).
Recreates the 6 Cyrillic-baked QuickChart-style PNGs in matplotlib with English
labels, identical Ocean palette, proportions and pixel dimensions.

RU source charts (assets/charts/) had baked-in Cyrillic invisible to XML text-scan.
Language-neutral charts (s17-u-shape) are NOT recreated (reused as-is).

Output -> assets-en/charts/*.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, LogLocator, FixedLocator
import os

# Ocean palette (LOCKED)
DEEP   = "#21295C"
MID    = "#065A82"
LIGHT  = "#1C7293"
TEAL   = "#028090"
GOLD   = "#F0AB00"
GRIDCOL = "#dddddd"
TITLE_GRAY = "#666666"   # sampled from RU charts (102,102,102)
AXIS_GRAY  = "#595959"

FONT = "DejaVu Sans"     # only sans available; renders Latin cleanly
plt.rcParams["font.family"] = FONT
plt.rcParams["axes.edgecolor"] = "#cccccc"

OUT = os.path.join(os.path.dirname(__file__), "assets-en", "charts")
os.makedirs(OUT, exist_ok=True)

FOODS = ["apple", "pizza", "salad", "bun", "cucumber"]


def _grid(ax):
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color=GRIDCOL, linewidth=1.0)
    ax.xaxis.grid(False)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")
    ax.tick_params(colors=AXIS_GRAY, labelcolor=AXIS_GRAY, length=0)


def save(fig, name, w_px, h_px, dpi=200):
    fig.set_size_inches(w_px / dpi, h_px / dpi)
    fig.savefig(os.path.join(OUT, name), dpi=dpi,
                facecolor="white", bbox_inches=None)
    plt.close(fig)
    print("wrote", name, f"{w_px}x{h_px}")


# ---------- s08: Tokens per character (1800x1000) ----------
def s08():
    fig, ax = plt.subplots()
    labels = ["EN", "RU", "ZH", "Python"]
    vals   = [0.25, 0.50, 0.80, 0.40]
    cols   = [MID, GOLD, LIGHT, TEAL]
    ax.bar(labels, vals, color=cols, width=0.62)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([i / 10 for i in range(0, 11)])
    ax.set_ylabel("Tokens / char", fontsize=15, color=AXIS_GRAY)
    ax.set_xlabel("Language", fontsize=15, color=AXIS_GRAY)
    ax.set_title("Tokens per character", fontsize=22, fontweight="bold",
                 color=TITLE_GRAY, pad=16)
    ax.tick_params(axis="x", labelsize=15)
    ax.tick_params(axis="y", labelsize=13)
    _grid(ax)
    fig.subplots_adjust(left=0.07, right=0.97, top=0.90, bottom=0.11)
    save(fig, "s08-tokens-per-char.png", 1800, 1000)


# ---------- s14: Attention weight distribution (3600x1600) ----------
def s14():
    fig, ax = plt.subplots()
    labels = [f"t{i}" for i in range(1, 9)]
    vals   = [0.05, 0.08, 0.12, 0.35, 0.18, 0.10, 0.07, 0.05]
    cols   = [LIGHT, LIGHT, MID, GOLD, MID, MID, LIGHT, LIGHT]
    ax.bar(labels, vals, color=cols, width=0.72)
    ax.set_ylim(0, 0.40)
    ax.set_yticks([0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40])
    ax.set_ylabel("Weight", fontsize=15, color=AXIS_GRAY)
    ax.set_xlabel("Context tokens", fontsize=14, color=AXIS_GRAY)
    ax.set_title("Attention weight distribution (sum = 1)",
                 fontsize=24, fontweight="bold", color=DEEP, pad=18)
    ax.tick_params(axis="x", labelsize=16)
    ax.tick_params(axis="y", labelsize=14)
    _grid(ax)
    fig.subplots_adjust(left=0.055, right=0.985, top=0.90, bottom=0.09)
    save(fig, "s14-attention-bars.png", 3600, 1600)


# ---------- s16: Context window log-scale (1800x1000) ----------
def s16():
    fig, ax = plt.subplots()
    labels = ["GPT-3.5 (2022)", "Claude 3.5 (2024)", "Claude 4.7 (2026)"]
    vals   = [4096, 200000, 1000000]
    cols   = [LIGHT, MID, GOLD]
    ax.bar(labels, vals, color=cols, width=0.55)
    ax.set_yscale("log")
    ax.set_ylim(1000, 2000000)
    ticks = [1000, 3000, 10000, 20000, 100000, 200000, 1000000, 2000000]
    ax.yaxis.set_major_locator(FixedLocator(ticks))
    ax.yaxis.set_minor_locator(FixedLocator([]))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{int(v):,}"))
    ax.set_ylabel("Tokens (log)", fontsize=15, color=AXIS_GRAY)
    ax.set_title("Context window (log-scale)", fontsize=22, fontweight="bold",
                 color=TITLE_GRAY, pad=16)
    ax.tick_params(axis="x", labelsize=14)
    ax.tick_params(axis="y", labelsize=13)
    _grid(ax)
    fig.subplots_adjust(left=0.11, right=0.97, top=0.90, bottom=0.08)
    save(fig, "s16-context-window.png", 1800, 1000)


# ---------- s18: P(next token) distribution (1800x1000) ----------
def s18():
    fig, ax = plt.subplots()
    vals = [0.32, 0.19, 0.14, 0.11, 0.08]
    cols = [GOLD, MID, MID, MID, MID]
    ax.bar(FOODS, vals, color=cols, width=0.62)
    ax.set_ylim(0, 0.40)
    ax.set_yticks([0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40])
    ax.set_ylabel("Probability", fontsize=15, color=AXIS_GRAY)
    ax.set_title('P(next token) | context: "Today I ate…"',
                 fontsize=21, fontweight="bold", color=TITLE_GRAY, pad=16)
    ax.tick_params(axis="x", labelsize=16)
    ax.tick_params(axis="y", labelsize=13)
    _grid(ax)
    fig.subplots_adjust(left=0.07, right=0.97, top=0.90, bottom=0.09)
    save(fig, "s18-distribution.png", 1800, 1000)


# ---------- s19: temperature triptych (1000x700 each) ----------
def s19(name, title, vals, title_color, bar_cols):
    fig, ax = plt.subplots()
    ax.bar(FOODS, vals, color=bar_cols, width=0.62)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([i / 10 for i in range(0, 11)])
    ax.set_ylabel("P", fontsize=14, color=AXIS_GRAY)
    ax.set_title(title, fontsize=20, fontweight="bold", color=title_color, pad=14)
    ax.tick_params(axis="x", labelsize=13)
    ax.tick_params(axis="y", labelsize=12)
    _grid(ax)
    fig.subplots_adjust(left=0.10, right=0.96, top=0.89, bottom=0.10)
    save(fig, name, 1000, 700)


if __name__ == "__main__":
    s08()
    s14()
    s16()
    s18()
    s19("s19-T0.png", "T=0 (argmax)", [1.0, 0, 0, 0, 0],
        TITLE_GRAY, [GOLD, MID, MID, MID, MID])
    s19("s19-T1.png", "T=1.0 (standard)", [0.32, 0.19, 0.14, 0.11, 0.08],
        TITLE_GRAY, [DEEP, LIGHT, LIGHT, LIGHT, LIGHT])
    s19("s19-T2.png", "T=2.0 (chaos)", [0.24, 0.22, 0.20, 0.18, 0.16],
        TITLE_GRAY, [TEAL, LIGHT, LIGHT, LIGHT, LIGHT])
    print("DONE")
