#!/usr/bin/env python3
"""Генерация точечных + поверхностных + распределительных диаграмм из сырых строк
reestr-reshenij.csv для issue #349.

Раунд 1 (chart1-3): 2 х 2D jittered scatter + 1 х 3D scatter — точки читаются напрямую
из CSV построчно (csv.DictReader), без промежуточной агрегации в процентах. Заменил
прежние 4 агрегированных bar/line графика по прямому указанию владельца курса:
"графики не особо. давай точечные диаграммы и какую-нить трехмерную".

Раунд 2 (chart_surface_*, chart_dist_*): владелец попросил (а) настоящую 3D-поверхность
вместо scatter-облака по агрегированной метрике "чистый счёт" (+1 успех, -1 провал,
частичный/неопределённый — нейтральны) + отдельно количество кейсов, и (б) распределения
успех/провал по осям тремя способами — точками, столбцами по количеству, поверхностью по
двум осям: "давай сделаем метрику по успешности/неуспешности агрегированной (+ за успех,
- за неуспех и просто количество проектов)... + давай покрутим распределения успешных и
неуспешных проектов по разным осям - точками, график количества по каждой оси, поверхность
по двум осям".
"""
import csv
import random
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TwoSlopeNorm
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


# ---------------------------------------------------------------------------
# Общие хелперы для раунда 2 (метрика net_score, сетки, распределения)
# ---------------------------------------------------------------------------
AXIS_HUMAN_NAMES = {
    "axis1_level": "Неопределённость",
    "axis2_bucket": "Время обратной связи",
    "axis3_class": "Класс метода",
    "axis4_blast_radius": "Цена ошибки",
}

AXIS_ORDERS = {
    "axis1_level": ["low", "moderate", "high", "extreme"],
    "axis2_bucket": ["seconds-minutes", "hours-days", "weeks-months", "season-years"],
    "axis3_class": AXIS3_ORDER,
    "axis4_blast_radius": ["low", "medium", "high", "catastrophic"],
}

AXIS_TICK_LABELS = {
    "axis1_level": AXIS1_LABELS[1:],
    "axis2_bucket": AXIS2_LABELS[1:],
    "axis3_class": AXIS3_ORDER,
    "axis4_blast_radius": AXIS4_LABELS[1:],
}


def net_score_grid(rows, row_key, row_order, col_key, col_order):
    """Возвращает (net_grid, n_grid) — numpy-массивы shape (len(row_order), len(col_order)).

    net_score = count(success) - count(failure) по ячейке (partial/undetermined — нейтральны).
    n = полное количество строк в ячейке (включая partial/undetermined).
    """
    net = defaultdict(int)
    n = defaultdict(int)
    for r in rows:
        rv, cv = r[row_key], r[col_key]
        if rv not in row_order or cv not in col_order:
            continue
        key = (rv, cv)
        n[key] += 1
        if r["outcome"] == "success":
            net[key] += 1
        elif r["outcome"] == "failure":
            net[key] -= 1

    net_grid = np.array(
        [[net[(rv, cv)] for cv in col_order] for rv in row_order], dtype=float
    )
    n_grid = np.array(
        [[n[(rv, cv)] for cv in col_order] for rv in row_order], dtype=float
    )
    return net_grid, n_grid


def _surface_pair(rows, row_key, col_key, title_net, title_n, out_name):
    row_order = AXIS_ORDERS[row_key]
    col_order = AXIS_ORDERS[col_key]
    net_grid, n_grid = net_score_grid(rows, row_key, row_order, col_key, col_order)

    X_idx = np.arange(1, len(row_order) + 1)
    Y_idx = np.arange(1, len(col_order) + 1)
    X, Y = np.meshgrid(X_idx, Y_idx, indexing="ij")

    fig = plt.figure(figsize=(13, 5.5))

    # --- левая панель: net_score, диверг. colormap, центр на нуле ---
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    vmax = max(abs(net_grid.min()), abs(net_grid.max()), 1)
    norm1 = TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)
    surf1 = ax1.plot_surface(
        X, Y, net_grid, facecolors=plt.cm.RdYlGn(norm1(net_grid)),
        rstride=1, cstride=1, edgecolor="#444444", linewidth=0.4, antialiased=True,
    )
    ax1.set_xticks(X_idx)
    ax1.set_xticklabels(AXIS_TICK_LABELS[row_key], fontsize=7, rotation=20, ha="right")
    ax1.set_yticks(Y_idx)
    ax1.set_yticklabels(AXIS_TICK_LABELS[col_key], fontsize=7)
    ax1.set_zlabel("net_score (успех − провал)", fontsize=8)
    mappable1 = plt.cm.ScalarMappable(norm=norm1, cmap="RdYlGn")
    mappable1.set_array(net_grid)
    fig.colorbar(mappable1, ax=ax1, shrink=0.6, pad=0.12, label="net_score")

    # --- правая панель: n (количество кейсов), sequential colormap ---
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    norm2 = plt.Normalize(vmin=0, vmax=max(n_grid.max(), 1))
    surf2 = ax2.plot_surface(
        X, Y, n_grid, facecolors=plt.cm.viridis(norm2(n_grid)),
        rstride=1, cstride=1, edgecolor="#444444", linewidth=0.4, antialiased=True,
    )
    ax2.set_xticks(X_idx)
    ax2.set_xticklabels(AXIS_TICK_LABELS[row_key], fontsize=7, rotation=20, ha="right")
    ax2.set_yticks(Y_idx)
    ax2.set_yticklabels(AXIS_TICK_LABELS[col_key], fontsize=7)
    ax2.set_zlabel("n (количество кейсов)", fontsize=8)
    mappable2 = plt.cm.ScalarMappable(norm=norm2, cmap="viridis")
    mappable2.set_array(n_grid)
    fig.colorbar(mappable2, ax=ax2, shrink=0.6, pad=0.12, label="n")

    # Заголовки — через fig.text (фиксированные fig-координаты), а не ax.set_title:
    # 3D-оси центрируются не по центру своей сетки, и длинный заголовок через
    # set_title обрезается левым краем холста (измерено на этом самом графике).
    fig.text(0.27, 0.95, title_net, ha="center", fontsize=11)
    fig.text(0.76, 0.95, title_n, ha="center", fontsize=11)

    fig.subplots_adjust(left=0.05, right=0.97, top=0.85, bottom=0.05, wspace=0.35)
    fig.savefig(HERE / out_name, dpi=150)
    plt.close(fig)
    print(out_name, "net_grid=\n", net_grid, "\nn_grid=\n", n_grid)


# ---------------------------------------------------------------------------
# Chart 4: поверхность net_score/n — axis1 (неопределённость) x axis2 (обратная связь)
# ---------------------------------------------------------------------------
def chart_surface_axisA_axisB(rows):
    _surface_pair(
        rows,
        row_key="axis1_level",
        col_key="axis2_bucket",
        title_net="Чистый счёт (успех−провал) — неопределённость × обратная связь",
        title_n="Количество кейсов — та же сетка",
        out_name="chart-surface-axisA-axisB.png",
    )


# ---------------------------------------------------------------------------
# Chart 5: поверхность net_score/n — axis1 (неопределённость) x axis3 (класс метода)
# ---------------------------------------------------------------------------
def chart_surface_axisA_axisC(rows):
    _surface_pair(
        rows,
        row_key="axis1_level",
        col_key="axis3_class",
        title_net="Чистый счёт — неопределённость × класс метода",
        title_n="Количество кейсов — та же сетка",
        out_name="chart-surface-axisA-axisC.png",
    )


# ---------------------------------------------------------------------------
# Chart 6: 2x2 — количество кейсов по исходу, по каждой оси (столбцы)
# ---------------------------------------------------------------------------
def chart_dist_counts_per_axis(rows):
    axis_keys = ["axis1_level", "axis2_bucket", "axis3_class", "axis4_blast_radius"]
    outcomes = ["success", "partial", "failure", "undetermined"]

    fig, axes = plt.subplots(2, 2, figsize=(11, 9))
    for ax, axis_key in zip(axes.flat, axis_keys):
        order = AXIS_ORDERS[axis_key]
        labels = AXIS_TICK_LABELS[axis_key]
        counts = {o: [0] * len(order) for o in outcomes}
        for r in rows:
            v = r[axis_key]
            if v not in order:
                continue
            idx = order.index(v)
            counts[r["outcome"]][idx] += 1

        x = np.arange(len(order))
        width = 0.2
        for i, o in enumerate(outcomes):
            ax.bar(
                x + (i - 1.5) * width, counts[o], width,
                color=OUTCOME_COLORS[o], label=OUTCOME_LABELS[o],
            )
        ax.set_xticks(x)
        rot = 30 if axis_key == "axis3_class" else 0
        ha = "right" if axis_key == "axis3_class" else "center"
        ax.set_xticklabels(labels, rotation=rot, ha=ha, fontsize=8)
        ax.set_title(AXIS_HUMAN_NAMES[axis_key], fontsize=10)
        ax.set_ylabel("количество кейсов", fontsize=8)
        ax.grid(True, axis="y", linestyle=":", alpha=0.35)

    axes.flat[0].legend(fontsize=8, loc="upper right")
    fig.suptitle("Распределение исходов по каждой оси — количество проектов", fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(HERE / "chart-dist-counts-per-axis.png", dpi=150)
    plt.close(fig)
    print("chart_dist_counts_per_axis saved")


# ---------------------------------------------------------------------------
# Chart 7: 2x2 — jittered strip scatter по исходу, по каждой оси (точки)
# ---------------------------------------------------------------------------
def chart_dist_points_per_axis(rows):
    axis_keys = ["axis1_level", "axis2_bucket", "axis3_class", "axis4_blast_radius"]

    fig, axes = plt.subplots(2, 2, figsize=(11, 9))
    for ax, axis_key in zip(axes.flat, axis_keys):
        order = AXIS_ORDERS[axis_key]
        labels = AXIS_TICK_LABELS[axis_key]

        for outcome in OUTCOME_ORDER:
            xs, ys = [], []
            for r in rows:
                v = r[axis_key]
                if v not in order or r["outcome"] != outcome:
                    continue
                idx = order.index(v)
                xs.append(jitter(idx, 0.15))
                ys.append(random.uniform(-0.4, 0.4))
            ax.scatter(
                xs, ys, s=22, c=OUTCOME_COLORS[outcome], alpha=0.5,
                edgecolors="none", label=OUTCOME_LABELS[outcome],
            )

        ax.set_xticks(range(len(order)))
        rot = 30 if axis_key == "axis3_class" else 0
        ha = "right" if axis_key == "axis3_class" else "center"
        ax.set_xticklabels(labels, rotation=rot, ha=ha, fontsize=8)
        ax.set_xlim(-0.5, len(order) - 0.5)
        ax.set_ylim(-0.6, 0.6)
        ax.set_yticks([])
        ax.set_ylabel("(для разброса)", fontsize=7)
        ax.set_title(AXIS_HUMAN_NAMES[axis_key], fontsize=10)
        ax.grid(True, axis="x", linestyle=":", alpha=0.25)

    axes.flat[0].legend(fontsize=8, loc="upper right")
    fig.suptitle("Распределение исходов по каждой оси — отдельные кейсы", fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(HERE / "chart-dist-points-per-axis.png", dpi=150)
    plt.close(fig)
    print("chart_dist_points_per_axis saved")


if __name__ == "__main__":
    rows = load_rows()
    chart1(rows)
    chart2(rows)
    chart3(rows)
    chart_surface_axisA_axisB(rows)
    chart_surface_axisA_axisC(rows)
    chart_dist_counts_per_axis(rows)
    chart_dist_points_per_axis(rows)
