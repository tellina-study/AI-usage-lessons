#!/usr/bin/env python3
"""Генерация 3 точечных диаграмм (2 х 2D jittered scatter + 1 х 3D) из сырых строк
reestr-reshenij.csv для issue #349. Заменяет прежние 4 агрегированных bar/line графика
по прямому указанию владельца курса: "графики не особо. давай точечные диаграммы и
какую-нить трехмерную".

Все точки читаются напрямую из CSV построчно (csv.DictReader), без промежуточной
агрегации в процентах — именно это отличает точечную диаграмму кейсов от прежних
agg-графиков.
"""
import csv
import random
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (регистрирует projection='3d')

random.seed(349)

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE.parent / "reestr-reshenij.csv"

OUTCOME_COLORS = {
    "success": "#2E7D32",
    "partial": "#F0AB00",
    "failure": "#B23A48",
    "undetermined": "#B0B0B0",
}
OUTCOME_ORDER = ["undetermined", "failure", "partial", "success"]  # undetermined/zorder внизу
OUTCOME_LABELS = {
    "success": "успех",
    "partial": "частичный",
    "failure": "провал",
    "undetermined": "не определён",
}

AXIS1_ORDINAL = {"low": 1, "moderate": 2, "high": 3, "extreme": 4}
AXIS1_LABELS = ["", "низкая", "умеренная", "высокая", "экстремальная"]

AXIS2_ORDINAL = {
    "seconds-minutes": 1,
    "hours-days": 2,
    "weeks-months": 3,
    "season-years": 4,
}
AXIS2_LABELS = ["", "секунды-минуты", "часы-дни", "недели-месяцы", "сезон-годы"]

AXIS4_ORDINAL = {"low": 1, "medium": 2, "high": 3, "catastrophic": 4}
AXIS4_LABELS = ["", "низкий", "средний", "высокий", "катастрофический"]

AXIS3_ORDER = [
    "rule-based",
    "classical-ml",
    "sensor-fusion",
    "hybrid",
    "deep-learning",
    "agentic-llm",
    "foundation-model",
]
AXIS3_ORDINAL = {name: i + 1 for i, name in enumerate(AXIS3_ORDER)}


def load_rows():
    with open(CSV_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def jitter(value, spread):
    return value + random.uniform(-spread, spread)


def legend_handles():
    return [
        plt.Line2D(
            [0], [0], marker="o", linestyle="none",
            markerfacecolor=OUTCOME_COLORS[o], markeredgecolor="none",
            markersize=8, alpha=0.9, label=OUTCOME_LABELS[o],
        )
        for o in ["success", "partial", "failure", "undetermined"]
    ]


# ---------------------------------------------------------------------------
# Chart 1: ось1 (неопределённость) x ось2 (обратная связь), цвет = исход
# ---------------------------------------------------------------------------
def chart1(rows):
    filtered = [
        r for r in rows
        if r["axis1_level"] != "unclear" and r["axis2_bucket"] != "unclear"
    ]
    n = len(filtered)

    fig, ax = plt.subplots(figsize=(9, 7))
    for outcome in OUTCOME_ORDER:
        xs, ys = [], []
        for r in filtered:
            if r["outcome"] != outcome:
                continue
            xs.append(jitter(AXIS1_ORDINAL[r["axis1_level"]], 0.18))
            ys.append(jitter(AXIS2_ORDINAL[r["axis2_bucket"]], 0.18))
        alpha = 0.35 if outcome == "undetermined" else 0.55
        zorder = 2 if outcome == "undetermined" else 3
        ax.scatter(
            xs, ys, s=40, c=OUTCOME_COLORS[outcome], alpha=alpha,
            edgecolors="none", zorder=zorder,
        )

    ax.set_xticks([1, 2, 3, 4])
    ax.set_xticklabels(AXIS1_LABELS[1:])
    ax.set_xlabel("Неопределённость задачи")
    ax.set_yticks([1, 2, 3, 4])
    ax.set_yticklabels(AXIS2_LABELS[1:])
    ax.set_ylabel("Время обратной связи")
    ax.set_xlim(0.5, 4.5)
    ax.set_ylim(0.5, 4.5)
    ax.set_title(f"Карта {n} кейсов по двум осям — цвет: исход")
    ax.grid(True, linestyle=":", alpha=0.35, zorder=0)
    ax.legend(handles=legend_handles(), loc="upper left", frameon=True, fontsize=9)
    fig.text(
        0.5, 0.01,
        f"n={n} из 421 (94 исключены — 'unclear' хотя бы на одной из осей)",
        ha="center", fontsize=8, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(HERE / "chart-scatter-axisA-axisB.png", dpi=150)
    plt.close(fig)
    print("chart1 n =", n)


# ---------------------------------------------------------------------------
# Chart 2: класс метода (ось3) x неопределённость (ось1), цвет = исход
# ---------------------------------------------------------------------------
def chart2(rows):
    filtered = [
        r for r in rows
        if r["axis1_level"] != "unclear" and r["axis3_class"] != "unclear"
    ]
    n = len(filtered)

    fig, ax = plt.subplots(figsize=(9, 7))
    for outcome in OUTCOME_ORDER:
        xs, ys = [], []
        for r in filtered:
            if r["outcome"] != outcome:
                continue
            xs.append(jitter(AXIS3_ORDINAL[r["axis3_class"]], 0.22))
            ys.append(jitter(AXIS1_ORDINAL[r["axis1_level"]], 0.18))
        alpha = 0.35 if outcome == "undetermined" else 0.55
        zorder = 2 if outcome == "undetermined" else 3
        ax.scatter(
            xs, ys, s=40, c=OUTCOME_COLORS[outcome], alpha=alpha,
            edgecolors="none", zorder=zorder,
        )

    ax.set_xticks(range(1, 8))
    ax.set_xticklabels(AXIS3_ORDER, rotation=35, ha="right")
    ax.set_xlabel("Класс метода")
    ax.set_yticks([1, 2, 3, 4])
    ax.set_yticklabels(AXIS1_LABELS[1:])
    ax.set_ylabel("Неопределённость задачи")
    ax.set_xlim(0.4, 7.6)
    ax.set_ylim(0.5, 4.5)
    ax.set_title("Класс метода × неопределённость — где исчезает классика, где гуще красный")
    ax.grid(True, linestyle=":", alpha=0.35, zorder=0)
    ax.legend(handles=legend_handles(), loc="upper left", frameon=True, fontsize=9)
    fig.text(
        0.5, 0.01,
        f"n={n} из 421 (65 исключены — 'unclear' хотя бы на одной из осей)",
        ha="center", fontsize=8, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(HERE / "chart-scatter-class-vs-uncertainty.png", dpi=150)
    plt.close(fig)
    print("chart2 n =", n)


# ---------------------------------------------------------------------------
# Chart 3: 3D — неопределённость x обратная связь x цена ошибки, цвет = исход
# ---------------------------------------------------------------------------
def chart3(rows):
    filtered = [
        r for r in rows
        if r["axis1_level"] != "unclear"
        and r["axis2_bucket"] != "unclear"
        and r["axis4_blast_radius"] != "unclear"
    ]
    n = len(filtered)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    for outcome in OUTCOME_ORDER:
        xs, ys, zs = [], [], []
        for r in filtered:
            if r["outcome"] != outcome:
                continue
            xs.append(jitter(AXIS1_ORDINAL[r["axis1_level"]], 0.15))
            ys.append(jitter(AXIS2_ORDINAL[r["axis2_bucket"]], 0.15))
            zs.append(jitter(AXIS4_ORDINAL[r["axis4_blast_radius"]], 0.15))
        alpha = 0.35 if outcome == "undetermined" else 0.6
        ax.scatter(
            xs, ys, zs, s=38, c=OUTCOME_COLORS[outcome], alpha=alpha,
            edgecolors="none", depthshade=True,
        )

    ax.set_xlabel("Неопределённость", labelpad=12)
    ax.set_xticks([1, 2, 3, 4])
    ax.set_xticklabels(AXIS1_LABELS[1:], fontsize=8)

    ax.set_ylabel("Обратная связь", labelpad=18)
    ax.set_yticks([1, 2, 3, 4])
    ax.set_yticklabels(AXIS2_LABELS[1:], fontsize=8)

    ax.set_zlabel("Цена ошибки (blast radius)", labelpad=10)
    ax.set_zticks([1, 2, 3, 4])
    ax.set_zticklabels(AXIS4_LABELS[1:], fontsize=8)

    ax.set_xlim(0.5, 4.5)
    ax.set_ylim(0.5, 4.5)
    ax.set_zlim(0.5, 4.5)

    ax.view_init(elev=20, azim=-60)
    ax.xaxis.pane.set_alpha(0.08)
    ax.yaxis.pane.set_alpha(0.08)
    ax.zaxis.pane.set_alpha(0.08)
    ax.grid(True, linestyle=":", alpha=0.4)

    ax.set_title("Три оси одновременно: неопределённость × обратная связь × цена ошибки", pad=20)
    ax.legend(handles=legend_handles(), loc="upper left", frameon=True, fontsize=9)
    fig.text(
        0.5, 0.02,
        f"n={n} из 421 (123 исключены — 'unclear' хотя бы на одной из трёх осей)",
        ha="center", fontsize=8, color="#555555",
    )
    fig.tight_layout()
    fig.savefig(HERE / "chart-3d-three-axes.png", dpi=150)
    plt.close(fig)
    print("chart3 n =", n)


if __name__ == "__main__":
    rows = load_rows()
    chart1(rows)
    chart2(rows)
    chart3(rows)
