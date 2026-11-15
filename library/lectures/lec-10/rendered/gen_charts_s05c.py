"""
Лекция 10 — s05c «Ретроспектива отрасли по годам» (issue #340, owner follow-up).

Два настоящих многолетних графика на РЕАЛЬНЫХ точках из chapter.md /
chapter-part2.md (без изобретённых промежуточных лет):

  c39-vf-investment-collapse.png — venture-инвестиции в indoor farming,
    индекс год-к-году 2024→2025 (−91%, AgFunder Year-in-Review 2025).
    chapter.md:243, :442, :465.

  c40-consolidation-deals.png — суммы сделок консолидации по годам
    (Blue River $305M 2017 → Bear Flag $250M 2021 → MSD/Antelliq $3,85 млрд
    2024), лог-шкала Y (единственная ось, рост на порядок — не performance,
    а цена консолидации). chapter-part2.md:156-157, :270.

Matplotlib, Ocean palette (locked), DejaVu Sans (кириллица), transparent bg,
один hue на серию, без dual-axis, direct value labels вместо легенды
(одна серия на график).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib import font_manager

REND = Path(__file__).resolve().parent
OUT = REND / "assets" / "charts"
OUT.mkdir(parents=True, exist_ok=True)

DEEP = "#21295C"; MID = "#065A82"; LIGHT = "#1C7293"; TEAL = "#028090"
GOLD = "#F0AB00"; SURFACE = "#F4F7FA"; GREY = "#D9E2EC"; SLATE = "#5B6678"

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
    fig.savefig(OUT / name, dpi=200, transparent=True, bbox_inches="tight")
    plt.close(fig)
    print(f"OK {name}")


# ── c39: venture-инвестиции в indoor farming — индекс 2024→2025 (−91% YoY) ──
# Источник: AgFunder Year-in-Review 2025, цитируется chapter.md:243,442,465.
# Только ДВЕ реальные точки (YoY-сравнение) — бар «до/после», без выдуманных
# промежуточных лет.
def c_vf_collapse():
    fig, ax = plt.subplots(figsize=(6.0, 4.6))
    years = ["2024\n(база)", "2025\n(после обвала)"]
    vals = [100, 9]
    colors = [LIGHT, GOLD]
    bars = ax.bar(years, vals, color=colors, width=0.52, zorder=3)
    ax.bar_label(bars, labels=["индекс 100", "индекс 9  (−91%)"],
                 fontsize=13.5, fontweight="bold", color=DEEP, padding=6)
    ax.set_ylim(0, 128)
    ax.set_ylabel("индекс венчурных инвестиций\nв ИИ для поля и вертикальных ферм (2024 = 100)",
                  fontsize=10.5)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color=GREY, linewidth=0.7, zorder=0)
    ax.tick_params(labelsize=11.5)
    ax.set_title("Инвестиции в ИИ для поля и вертикальных ферм — год к году",
                 fontsize=13.5, fontweight="bold", color=DEEP, pad=12, loc="left")
    save(fig, "c39-vf-investment-collapse.png")


# ── c40: сделки консолидации по годам, лог-шкала Y (единственная ось) ──
# Blue River $305M (2017) → Bear Flag $250M (2021) → MSD/Antelliq $3,85 млрд
# (2024). Источник: chapter-part2.md:156-157 (Deere/Blue River, Deere/Bear
# Flag) + :270 (MSD/Antelliq). Лог-шкала — рост на порядок в цене сделки,
# не performance-кривая; явно подписано в title.
def c_consolidation():
    fig, ax = plt.subplots(figsize=(6.0, 4.6))
    labels = ["2017\nDeere / Blue River", "2021\nDeere / Bear Flag",
              "2024\nMSD / Antelliq"]
    vals = [305, 250, 3850]
    colors = [LIGHT, LIGHT, GOLD]
    bars = ax.bar(labels, vals, color=colors, width=0.56, zorder=3,
                  bottom=0.01)
    ax.set_yscale("log")
    ax.set_ylim(100, 6000)
    ax.bar_label(bars, labels=["$305M", "$250M", "$3 850M"],
                 fontsize=13, fontweight="bold", color=DEEP, padding=6)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(
        lambda v, pos: f"{int(v):,}".replace(",", " ")))
    ax.set_ylabel("$ млн за сделку (лог-шкала)", fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", which="major", color=GREY, linewidth=0.7, zorder=0)
    ax.tick_params(labelsize=10.5)
    ax.set_title("Размер сделок консолидации — цена, не производительность",
                 fontsize=13.5, fontweight="bold", color=DEEP, pad=12, loc="left")
    save(fig, "c40-consolidation-deals.png")


if __name__ == "__main__":
    c_vf_collapse()
    c_consolidation()
