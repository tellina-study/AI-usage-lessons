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

Раунд 3 (chart_lines_*, chart_groups_*, chart_wow_*): владелец попросил "а где графики
отдельно по количеству успехов/провалов? барчарты переделай на графики и сделай в таких же
(по каждой оси) график успеха и провала классики, МЛ, большого ИИ, ну и пофантазируй ещё
графиков пока нет вау". Три части: (а) chart_dist_counts_per_axis (сгруппированные столбцы)
заменён на chart_lines_outcome_per_axis (линии — читается тренд роста/падения); (б) три
новых chart_groups_axis{1,2,4}_* — по 6 линий (3 группы метода × успех/провал) на каждую из
трёх осей (ось 3 пропущена — она и определяет группы); (в) два "wow"-графика:
chart-wow-slope-successrate (bump/slope-chart, успех-доля по 4 уровням неопределённости) и
chart-wow-radar (radar/spider на 5 нормированных метриках) + один опциональный третий —
chart-wow-gate-dumbbell (dumbbell, эффект гейта по группам — проверяет, держится ли самый
сильный предиктор исследования (гейт/обратимость, файл 07 §1) одинаково во всех трёх классах
методов).

Определение групп метода для раунда 3 (ровно так, как попросил владелец — классика / МЛ /
большой ИИ; deep-learning/sensor-fusion/hybrid сознательно не входят в это сравнение):
  Классика    = axis3_class == "rule-based"
  МЛ          = axis3_class == "classical-ml"
  Большой ИИ  = axis3_class in ("foundation-model", "agentic-llm")

Раунд 4 (chart_lines_outcome_share_per_axis, chart_groups_*_share): владелец попросил долевые
версии двух семейств графиков раунда 3 — "распределение исходов и другие графики с разбивкой
по типам по количеству сделай еще не по количеству, а по доле от тотала в этом срезе". Смысл:
уровень оси с большим n (axis1_level=moderate, n=152) визуально "выигрывает" у axis1_level=
extreme (n=10) просто по объёму, а не по составу исходов — доля убирает этот эффект объёма и
показывает именно состав. Знаменатель для осей 1/2/4 — ПОЛНОЕ число кейсов на уровне оси
(включая unclear-кейсы по ДРУГИМ осям, все 4 исхода), не только успех+провал и не только три
именованные группы метода. Исходные count-графики НЕ удалены и НЕ изменены — обе версии стоят
рядом в 00-rezyume.md.

Раунд 5 (chart_donut_*, заменяет chart1/chart2 — bubble/scatter "карты" 2D): владелец попросил
"карты двумерные тоже из точечных диаграмм переделай в бублики, где размер бублика - агрегированная
метрика успешности по точкам средняя по кейсам которые туда попали". Старые chart1/chart2 рисовали
точку на кейс (джиттер, цвет=исход) — хорошо показывали объём, но не агрегированный исход ячейки.
Новые chart_donut_axisA_axisB / chart_donut_class_vs_uncertainty рисуют одно кольцо на ЯЧЕЙКУ сетки:
радиус кольца = |net_score/n| (та же метрика "чистый счёт", что и в _surface_pair выше — успех=+1,
провал=-1, частичный/неопределённый нейтральны, но входят в n), цвет кольца — RdYlGn по ЗНАКУ
net_score/n (не только модулю), а в полом центре кольца — текст "n=XX", чтобы объём остался читаем
даже когда размер/цвет теперь кодируют не объём, а успешность. Числа для обеих сеток (net_score/n
по ячейке) сверены дважды двумя независимыми агентами в этой исследовательской линии и взяты как
авторитетные (см. также `net_score_grid` выше — та же формула, тот же знаменатель).
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

# --- Раунд 3: группы метода (владелец назвал ровно эти три) ---------------
GROUP_ORDER = ["classic", "ml", "bigai"]
GROUP_LABELS = {"classic": "Классика", "ml": "МЛ", "bigai": "Большой ИИ"}
GROUP_COLORS = {
    "classic": "#5B6472",  # серо-сланцевый
    "ml": "#1C7293",       # тил/синий (вторичный цвет палитры курса)
    "bigai": "#8C1C27",    # тёмно-бордовый
}


def group_of(row):
    """classic = rule-based; ml = classical-ml; bigai = foundation-model | agentic-llm.

    deep-learning / sensor-fusion / hybrid / unclear -> None (не входят в это
    3-стороннее сравнение — владелец назвал ровно эти три группы).
    """
    c = row["axis3_class"]
    if c == "rule-based":
        return "classic"
    if c == "classical-ml":
        return "ml"
    if c in ("foundation-model", "agentic-llm"):
        return "bigai"
    return None


def load_rows():
    with open(CSV_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def jitter(value, spread):
    return value + random.uniform(-spread, spread)


def _burn_random_draws(n):
    """Сжигает n вызовов random.uniform(), не используя результат.

    Раунд 5 удалил chart1/chart2 (scatter), которые раньше потребляли
    2*327 + 2*356 = 1366 вызовов jitter() -> random.uniform() из ОБЩЕГО
    глобального потока `random`, засеянного один раз (random.seed(349)) на
    весь модуль. chart3 (3D) и chart_dist_points_per_axis тоже используют
    jitter() и раньше стартовали из состояния потока ПОСЛЕ этих 1366
    вызовов — без этого burn их джиттер сдвинулся бы на другие случайные
    смещения и PNG изменились бы пиксель-в-пиксель, хотя владелец явно
    попросил оставить "остальные 15 PNG нетронутыми" (chart-3d-three-axes.png
    входит в их число буквально по тексту задачи). random.uniform(a, b)
    в CPython делает ровно один вызов self.random() независимо от a/b —
    поэтому для восстановления состояния потока важно только КОЛИЧЕСТВО
    вызовов, не их аргументы.
    """
    for _ in range(n):
        random.uniform(0, 1)


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
# Раунд 5: общий донат-рисовальщик для 2D-карт (заменяет chart1/chart2 scatter).
# Один кольцевой маркер на ЯЧЕЙКУ сетки (x_level, y_level):
#   - радиус кольца кодирует |avg_score| (avg_score = net_score/n по ячейке,
#     та же формула, что в net_score_grid/_surface_pair выше), с минимальным
#     видимым радиусом даже у near-zero ячеек;
#   - цвет кольца — RdYlGn по ЗНАКУ avg_score (не по модулю);
#   - в полом центре кольца — "n=XX" (счётчик кейсов, иначе объём ячейки
#     исчезает из графика вместе с переходом от scatter к агрегату).
# Ячейка с n=0 — без маркера вовсе (не кольцо нулевого размера).
# ---------------------------------------------------------------------------
from matplotlib.patches import Wedge

RADIUS_MIN = 0.17
RADIUS_MAX = 0.46


def _score_to_radius(abs_score):
    return RADIUS_MIN + (RADIUS_MAX - RADIUS_MIN) * abs_score


def _draw_donut_grid(
    rows, x_key, x_order, x_labels, y_key, y_order, y_labels,
    xlabel, ylabel, title, out_name, x_rotation=0,
):
    # net_score_grid(row_key=y, col_key=x) -> grid shape (len(y_order), len(x_order));
    # читаем как net_grid[yi][xi].
    net_grid, n_grid = net_score_grid(rows, y_key, y_order, x_key, x_order)
    n_total = int(n_grid.sum())

    fig, ax = plt.subplots(figsize=(10.5, 9.4))
    norm = TwoSlopeNorm(vmin=-1, vcenter=0, vmax=1)
    cmap = plt.cm.RdYlGn

    for yi in range(len(y_order)):
        for xi in range(len(x_order)):
            n_cell = n_grid[yi, xi]
            if n_cell <= 0:
                continue
            avg_score = net_grid[yi, xi] / n_cell
            r = _score_to_radius(abs(avg_score))
            width = max(0.4 * r, 0.065)
            color = cmap(norm(avg_score))
            wedge = Wedge(
                (xi + 1, yi + 1), r, 0, 360, width=width,
                facecolor=color, edgecolor="#333333", linewidth=0.6, zorder=3,
            )
            ax.add_patch(wedge)
            ax.text(
                xi + 1, yi + 1, f"n={int(n_cell)}",
                ha="center", va="center", fontsize=7.3, color="#222222", zorder=4,
            )

    ax.set_xticks(range(1, len(x_order) + 1))
    ax.set_xticklabels(x_labels, rotation=x_rotation, ha="right" if x_rotation else "center")
    ax.set_xlabel(xlabel)
    ax.set_yticks(range(1, len(y_order) + 1))
    ax.set_yticklabels(y_labels)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0.4, len(x_order) + 0.6)
    ax.set_ylim(0.4, len(y_order) + 0.6)
    ax.set_aspect("equal")
    ax.grid(True, linestyle=":", alpha=0.3, zorder=0)
    ax.set_title(title, fontsize=12)

    mappable = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    mappable.set_array(net_grid)
    cbar = fig.colorbar(mappable, ax=ax, shrink=0.75, pad=0.03)
    cbar.set_label("средний балл по кейсам ячейки (−1 провал … +1 успех)", fontsize=8)

    # Главная сетка данных отведена в верхние ~70% холста (bottom=0.30 ниже);
    # нижняя полоса целиком свободна от данных (ось X + подпись оси там же,
    # выше этой полосы) — туда ставим размерную легенду и подпись-сноску,
    # без риска наложиться на кольца/colorbar/подпись оси X.
    fig.subplots_adjust(left=0.14, right=0.98, top=0.93, bottom=0.30)

    # Размерная легенда — 3 эталонных кольца (|avg_score| = 0.2 / 0.6 / 1.0),
    # отдельная мини-ось в правом нижнем углу, вне области данных.
    leg_ax = fig.add_axes([0.66, 0.02, 0.30, 0.14])
    leg_ax.set_xlim(0, 3)
    leg_ax.set_ylim(-0.6, 0.8)
    leg_ax.axis("off")
    leg_ax.set_title("размер кольца = |балл|", fontsize=7.5, pad=2)
    for i, val in enumerate([0.2, 0.6, 1.0]):
        r = _score_to_radius(val)
        w = max(0.4 * r, 0.065)
        leg_ax.add_patch(
            Wedge((i * 1 + 0.5, 0.2), r, 0, 360, width=w,
                  facecolor="#AAAAAA", edgecolor="#333333", linewidth=0.5)
        )
        leg_ax.text(i * 1 + 0.5, -0.5, f"{val:.1f}", ha="center", fontsize=7.5)

    fig.text(
        0.5, 0.19,
        f"n={n_total} из 421 ('unclear' хотя бы на одной из двух осей исключены). Балл = "
        "(успех − провал)/n по ячейке; частичный/неопределённый — нейтральны, но входят в n.",
        ha="center", fontsize=7.5, color="#555555",
    )
    fig.savefig(HERE / out_name, dpi=150)
    plt.close(fig)
    print(out_name, "n_total =", n_total)


# ---------------------------------------------------------------------------
# Chart 1 (раунд 5, донат): ось1 (неопределённость, x) x ось2 (обратная связь, y)
# ---------------------------------------------------------------------------
def chart_donut_axisA_axisB(rows):
    _draw_donut_grid(
        rows,
        x_key="axis1_level", x_order=AXIS_ORDERS["axis1_level"], x_labels=AXIS1_LABELS[1:],
        y_key="axis2_bucket", y_order=AXIS_ORDERS["axis2_bucket"], y_labels=AXIS2_LABELS[1:],
        xlabel="Неопределённость задачи", ylabel="Время обратной связи",
        title="Средний балл по кейсам (+1 успех / −1 провал) — размер и цвет кольца",
        out_name="chart-donut-axisA-axisB.png",
    )


# ---------------------------------------------------------------------------
# Chart 2 (раунд 5, донат): класс метода (ось3, x) x неопределённость (ось1, y)
# ---------------------------------------------------------------------------
def chart_donut_class_vs_uncertainty(rows):
    _draw_donut_grid(
        rows,
        x_key="axis3_class", x_order=AXIS3_ORDER, x_labels=AXIS3_ORDER,
        y_key="axis1_level", y_order=AXIS_ORDERS["axis1_level"], y_labels=AXIS1_LABELS[1:],
        xlabel="Класс метода", ylabel="Неопределённость задачи",
        title="Класс метода × неопределённость — средний балл по кейсам, размер и цвет кольца",
        out_name="chart-donut-class-vs-uncertainty.png",
        x_rotation=35,
    )


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
# Chart 6 (раунд 3, заменяет старый bar-график): 2x2 — количество кейсов по
# исходу, по каждой оси, ЛИНИЯМИ (а не столбцами) — тренд виден напрямую.
# ---------------------------------------------------------------------------
def chart_lines_outcome_per_axis(rows):
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
        for o in outcomes:
            ax.plot(
                x, counts[o], marker="o", markersize=5, linewidth=1.9,
                color=OUTCOME_COLORS[o], label=OUTCOME_LABELS[o],
            )
        ax.set_xticks(x)
        rot = 30 if axis_key == "axis3_class" else 0
        ha = "right" if axis_key == "axis3_class" else "center"
        ax.set_xticklabels(labels, rotation=rot, ha=ha, fontsize=8)
        ax.set_title(AXIS_HUMAN_NAMES[axis_key], fontsize=10)
        ax.set_ylabel("количество кейсов", fontsize=8)
        ax.grid(True, linestyle=":", alpha=0.35)

    axes.flat[0].legend(fontsize=8, loc="upper right")
    fig.suptitle("Распределение исходов по каждой оси — количество проектов (линии)", fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(HERE / "chart-lines-outcome-per-axis.png", dpi=150)
    plt.close(fig)
    print("chart_lines_outcome_per_axis saved")


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


def _succ_rate(sub):
    """success/(success+failure)*100, или None если знаменатель 0. Partial/undetermined
    игнорируются по запросу владельца — "формула простая", без спора о весах."""
    s = sum(1 for r in sub if r["outcome"] == "success")
    f = sum(1 for r in sub if r["outcome"] == "failure")
    return (s / (s + f) * 100) if (s + f) > 0 else None


# ---------------------------------------------------------------------------
# Chart 8-10 (раунд 3): 3 группы метода (классика/МЛ/большой ИИ) × успех/провал
# по каждой из осей 1/2/4 (ось 3 пропущена — она же определяет группы).
# ---------------------------------------------------------------------------
def chart_groups_per_axis(rows, axis_key, out_name, title, xlabel):
    order = AXIS_ORDERS[axis_key]
    labels = AXIS_TICK_LABELS[axis_key]
    x = np.arange(len(order))

    fig, ax = plt.subplots(figsize=(10, 6.5))
    for g in GROUP_ORDER:
        for outcome, ls, ru in (("success", "-", "успех"), ("failure", "--", "провал")):
            ys = []
            for lvl in order:
                cell = [r for r in rows if group_of(r) == g and r[axis_key] == lvl]
                # честный разрыв: группы вообще нет на этом уровне (n=0) -> None
                # (а не "0 успехов при наличии кейсов" — это настоящий 0, рисуется).
                ys.append(
                    sum(1 for r in cell if r["outcome"] == outcome) if cell else None
                )
            xs_plot = [xi for xi, yi in zip(x, ys) if yi is not None]
            ys_plot = [yi for yi in ys if yi is not None]
            ax.plot(
                xs_plot, ys_plot, marker="o", markersize=6, linewidth=2.2,
                linestyle=ls, color=GROUP_COLORS[g],
                label=f"{GROUP_LABELS[g]} — {ru}",
            )

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("количество кейсов")
    ax.set_title(title, fontsize=12)
    ax.grid(True, linestyle=":", alpha=0.3)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.legend(fontsize=8.5, loc="best")
    fig.text(
        0.5, 0.01,
        "сплошная — успех, пунктир — провал; цвет — группа метода; разрыв линии = у группы"
        " вообще нет кейсов на этом уровне (не 0 успехов/провалов)",
        ha="center", fontsize=7.5, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(HERE / out_name, dpi=150)
    plt.close(fig)
    print(out_name, "saved")


def chart_groups_axis1_uncertainty(rows):
    chart_groups_per_axis(
        rows, "axis1_level", "chart-groups-axis1-uncertainty.png",
        "Классика vs МЛ vs большой ИИ: успех и провал по неопределённости",
        "Неопределённость задачи",
    )


def chart_groups_axis2_feedback(rows):
    chart_groups_per_axis(
        rows, "axis2_bucket", "chart-groups-axis2-feedback.png",
        "Классика vs МЛ vs большой ИИ: успех и провал по времени обратной связи",
        "Время обратной связи",
    )


def chart_groups_axis4_blastradius(rows):
    chart_groups_per_axis(
        rows, "axis4_blast_radius", "chart-groups-axis4-blastradius.png",
        "Классика vs МЛ vs большой ИИ: успех и провал по цене ошибки",
        "Цена ошибки (blast radius)",
    )


# ---------------------------------------------------------------------------
# Chart 11 ("wow" 3a): bump/slope-chart — доля успеха по неопределённости,
# один скос-график на все три группы, подписи прямо у концов линий.
# ---------------------------------------------------------------------------
def chart_wow_slope_successrate(rows):
    order = AXIS_ORDERS["axis1_level"]
    labels = AXIS1_LABELS[1:]
    x = np.arange(len(order))

    fig, ax = plt.subplots(figsize=(9, 7))

    # у классики и МЛ конец линии (high, x=2) совпадает в точности на 0% —
    # смещаем подписи вручную, чтобы не легли друг на друга.
    end_label_offset = {"classic": (10, -16), "ml": (10, 14), "bigai": (10, 0)}
    start_label_offset = {"classic": (-10, 10), "ml": (-10, -4), "bigai": (-10, -14)}

    for g in GROUP_ORDER:
        rows_g = [r for r in rows if group_of(r) == g]
        ys = []
        for lvl in order:
            cell = [r for r in rows_g if r["axis1_level"] == lvl]
            ys.append(_succ_rate(cell) if cell else None)
        xs_plot = [xi for xi, yi in zip(x, ys) if yi is not None]
        ys_plot = [yi for yi in ys if yi is not None]

        ax.plot(
            xs_plot, ys_plot, marker="o", markersize=8, linewidth=2.6,
            color=GROUP_COLORS[g], zorder=3,
        )
        ax.annotate(
            f"{GROUP_LABELS[g]} — {ys_plot[0]:.0f}%",
            (xs_plot[0], ys_plot[0]), textcoords="offset points",
            xytext=start_label_offset[g], ha="right", fontsize=9.5,
            color=GROUP_COLORS[g], fontweight="bold",
        )
        ax.annotate(
            f"{ys_plot[-1]:.0f}%",
            (xs_plot[-1], ys_plot[-1]), textcoords="offset points",
            xytext=end_label_offset[g], ha="left", fontsize=9.5,
            color=GROUP_COLORS[g], fontweight="bold",
        )

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_xlim(-0.35, len(order) - 0.4)
    ax.set_ylim(-5, 100)
    ax.set_ylabel("доля успеха среди (успех+провал), %")
    ax.set_title(
        "Доля успеха по неопределённости: классика vs МЛ vs большой ИИ", fontsize=12
    )
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.grid(True, axis="y", linestyle=":", alpha=0.25)
    fig.text(
        0.5, 0.01,
        "доля = успех / (успех+провал), частичный/неопределённый не учтены; точка"
        " пропущена там, где у группы вообще нет кейсов на этом уровне (не 0%)",
        ha="center", fontsize=7.5, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(HERE / "chart-wow-slope-successrate.png", dpi=150)
    plt.close(fig)
    print("chart_wow_slope_successrate saved")


# ---------------------------------------------------------------------------
# Chart 12 ("wow" 3b): radar/spider — 3 группы × 5 нормированных метрик 0-100.
# ---------------------------------------------------------------------------
def chart_wow_radar(rows):
    axis1_order = AXIS_ORDERS["axis1_level"]
    radar_vals = {}
    debug_rows = []

    for g in GROUP_ORDER:
        rows_g = [r for r in rows if group_of(r) == g]

        low_sub = [r for r in rows_g if r["axis1_level"] == "low"]
        mod_sub = [r for r in rows_g if r["axis1_level"] == "moderate"]
        m1 = _succ_rate(low_sub) or 0.0
        m2 = _succ_rate(mod_sub) or 0.0

        ceiling = None
        for lvl in axis1_order:
            if any(r["axis1_level"] == lvl for r in rows_g):
                ceiling = lvl
        low_rate = _succ_rate(low_sub)
        if not low_rate:
            m3 = 0.0  # низкая база 0/None -> метрика 0, без деления на ноль
        else:
            ceiling_sub = [r for r in rows_g if r["axis1_level"] == ceiling]
            ceiling_rate = _succ_rate(ceiling_sub) or 0.0
            decline = (low_rate - ceiling_rate) / low_rate
            m3 = max(0.0, 100.0 - 100.0 * decline)

        highext_n = sum(1 for r in rows_g if r["axis1_level"] in ("high", "extreme"))
        total_n = sum(1 for r in rows_g if r["axis1_level"] in axis1_order)
        m4 = (highext_n / total_n * 100) if total_n > 0 else 0.0

        gate_yes = sum(1 for r in rows_g if r["axis4_gate"] == "yes")
        gate_no = sum(1 for r in rows_g if r["axis4_gate"] == "no")
        m5 = (gate_yes / (gate_yes + gate_no) * 100) if (gate_yes + gate_no) > 0 else 0.0

        radar_vals[g] = [m1, m2, m3, m4, m5]
        debug_rows.append((g, ceiling, m1, m2, m3, m4, m5))

    for row in debug_rows:
        print("chart_wow_radar", row)

    metric_labels = [
        "Успех\n(низкая неопр.)",
        "Успех\n(умеренная неопр.)",
        "Устойчивость\nк росту неопр.",
        "Доля попыток\nпри выс. неопр.",
        "Доля кейсов\nс гейтом",
    ]
    n = len(metric_labels)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8.5, 8.5), subplot_kw=dict(polar=True))
    for g in GROUP_ORDER:
        data = radar_vals[g] + radar_vals[g][:1]
        ax.plot(
            angles, data, linewidth=2.3, marker="o", markersize=5,
            color=GROUP_COLORS[g], label=GROUP_LABELS[g],
        )
        ax.fill(angles, data, color=GROUP_COLORS[g], alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metric_labels, fontsize=9)
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(["20", "40", "60", "80", "100"], fontsize=7, color="#777777")
    ax.set_title(
        "Классика vs МЛ vs большой ИИ — 5 метрик применимости (0-100)",
        fontsize=12, pad=24,
    )
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.12), fontsize=9.5)
    fig.tight_layout()
    fig.savefig(HERE / "chart-wow-radar.png", dpi=150)
    plt.close(fig)
    print("chart_wow_radar saved")


# ---------------------------------------------------------------------------
# Chart 13 ("wow" 3c, опциональный): dumbbell — эффект гейта (самый сильный
# предиктор исхода во всём исследовании, файл 07 §1) по трём группам метода.
# Проверяет: держится ли этот эффект одинаково у классики/МЛ/большого ИИ,
# или он — артефакт того, что именно большой ИИ чаще работает без гейта.
# ---------------------------------------------------------------------------
def chart_wow_gate_dumbbell(rows):
    fig, ax = plt.subplots(figsize=(9, 5.2))
    y_positions = np.arange(len(GROUP_ORDER))

    for yi, g in zip(y_positions, GROUP_ORDER):
        rows_g = [r for r in rows if group_of(r) == g]
        r_no = _succ_rate([r for r in rows_g if r["axis4_gate"] == "no"])
        r_yes = _succ_rate([r for r in rows_g if r["axis4_gate"] == "yes"])
        ax.plot([r_no, r_yes], [yi, yi], color=GROUP_COLORS[g], linewidth=2.6, zorder=2)
        ax.scatter([r_no], [yi], color=GROUP_COLORS[g], s=150, marker="o",
                   alpha=0.55, zorder=3, edgecolors="none")
        ax.scatter([r_yes], [yi], color=GROUP_COLORS[g], s=150, marker="D", zorder=3)
        ax.annotate(f"{r_no:.0f}%", (r_no, yi), textcoords="offset points",
                    xytext=(0, -16), ha="center", fontsize=9.5)
        ax.annotate(f"{r_yes:.0f}%", (r_yes, yi), textcoords="offset points",
                    xytext=(0, 10), ha="center", fontsize=9.5)

    ax.set_yticks(y_positions)
    ax.set_yticklabels([GROUP_LABELS[g] for g in GROUP_ORDER], fontsize=11)
    ax.set_ylim(-0.6, len(GROUP_ORDER) - 0.4)
    ax.set_xlim(-5, 105)
    ax.set_xlabel("доля успеха среди (успех+провал), %")
    ax.set_title(
        "Эффект гейта держится во всех трёх группах метода: ○ без гейта → ◆ с гейтом",
        fontsize=11,
    )
    ax.grid(True, axis="x", linestyle=":", alpha=0.3)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    legend_elems = [
        plt.Line2D([0], [0], marker="o", color="none", markerfacecolor="#888888",
                   markersize=10, label="без гейта"),
        plt.Line2D([0], [0], marker="D", color="none", markerfacecolor="#888888",
                   markersize=9, label="с гейтом"),
    ]
    ax.legend(handles=legend_elems, loc="lower right", fontsize=9)
    fig.tight_layout()
    fig.savefig(HERE / "chart-wow-gate-dumbbell.png", dpi=150)
    plt.close(fig)
    print("chart_wow_gate_dumbbell saved")


# ---------------------------------------------------------------------------
# Раунд 4: долевые (share-of-total) знаменатели по уровню оси — зафиксированы
# владельцем/оркестратором напрямую по CSV в этой сессии (issue #349), здесь
# НЕ пересчитываются, чтобы не держать два разных способа их получить.
# Для axis1/axis2/axis4 — полное n на уровне оси (все 4 исхода, независимо от
# того, unclear ли у строки какая-то ДРУГАЯ ось). Для axis3_class — собственное
# n класса (у оси 3 нет отдельного понятия "итог по всей оси" помимо суммы
# классов — каждый класс сам себе срез).
# ---------------------------------------------------------------------------
AXIS_LEVEL_TOTALS = {
    "axis1_level": {"low": 125, "moderate": 152, "high": 85, "extreme": 10},
    "axis2_bucket": {
        "seconds-minutes": 114, "hours-days": 73,
        "weeks-months": 53, "season-years": 105,
    },
    "axis4_blast_radius": {"low": 113, "medium": 85, "high": 83, "catastrophic": 59},
    "axis3_class": {
        "foundation-model": 101, "deep-learning": 69, "hybrid": 57,
        "classical-ml": 51, "rule-based": 36, "sensor-fusion": 34,
        "agentic-llm": 31,
    },
}


# ---------------------------------------------------------------------------
# Chart 14 (раунд 4, долевая пара к chart_lines_outcome_per_axis): та же 2x2
# раскладка, те же 4 линии-исхода на панель, но Y = доля от ВСЕГО n на этом
# уровне оси (%), а не количество кейсов. По запросу владельца ("по доле от
# тотала в этом срезе"), чтобы уровень с большим n не "выигрывал" визуально
# просто объёмом.
# ---------------------------------------------------------------------------
def chart_lines_outcome_share_per_axis(rows):
    axis_keys = ["axis1_level", "axis2_bucket", "axis3_class", "axis4_blast_radius"]
    outcomes = ["success", "partial", "failure", "undetermined"]

    fig, axes = plt.subplots(2, 2, figsize=(11, 9))
    for ax, axis_key in zip(axes.flat, axis_keys):
        order = AXIS_ORDERS[axis_key]
        labels = AXIS_TICK_LABELS[axis_key]
        denom = AXIS_LEVEL_TOTALS[axis_key]
        counts = {o: [0] * len(order) for o in outcomes}
        for r in rows:
            v = r[axis_key]
            if v not in order:
                continue
            idx = order.index(v)
            counts[r["outcome"]][idx] += 1

        x = np.arange(len(order))
        for o in outcomes:
            shares = [
                counts[o][i] / denom[lvl] * 100 for i, lvl in enumerate(order)
            ]
            ax.plot(
                x, shares, marker="o", markersize=5, linewidth=1.9,
                color=OUTCOME_COLORS[o], label=OUTCOME_LABELS[o],
            )
        ax.set_xticks(x)
        rot = 30 if axis_key == "axis3_class" else 0
        ha = "right" if axis_key == "axis3_class" else "center"
        ax.set_xticklabels(labels, rotation=rot, ha=ha, fontsize=8)
        ax.set_title(AXIS_HUMAN_NAMES[axis_key], fontsize=10)
        ax.set_ylabel("доля от кейсов на этом уровне, %", fontsize=8)
        ax.set_ylim(0, 100)
        ax.grid(True, linestyle=":", alpha=0.35)

    axes.flat[0].legend(fontsize=8, loc="upper right")
    fig.suptitle(
        "Распределение исходов по каждой оси — доля от общего n на уровне (не количество)",
        fontsize=13,
    )
    fig.text(
        0.5, 0.005,
        "знаменатель — всё n на уровне (все 4 исхода), не только успех+провал; для класса"
        " метода — собственное n класса. Версия по количеству: chart-lines-outcome-per-axis.png",
        ha="center", fontsize=7.5, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.02, 1, 0.96))
    fig.savefig(HERE / "chart-lines-outcome-share-per-axis.png", dpi=150)
    plt.close(fig)
    print("chart_lines_outcome_share_per_axis saved")


# ---------------------------------------------------------------------------
# Chart 15-17 (раунд 4, долевая пара к chart_groups_per_axis): те же 6 линий
# (3 группы × успех/провал), но Y = доля от ВСЕХ кейсов на этом уровне оси
# (across всех 7 классов, все 4 исхода) — не 100%-суммирующийся набор, а
# "какую долю целого среза занимает именно эта группа+исход". Честный разрыв
# сохранён: у группы вообще нет кейсов на уровне -> точка пропущена, а не 0%.
#
# Раунд 6 (фикс владельца, 2026-11-18): "графики по долям слишком сжаты и
# одноцветные не читаются". Причина — все 6 линий лежат в диапазоне ~0-15%
# (кроме "Большой ИИ — провал" до ~50%) на фиксированной шкале 0-100%, плюс
# Классика/МЛ были слишком похожи (серый/тил) в этой тесной зоне. Фикс:
# (а) y-автомасштаб под фактический максимум именно этого графика вместо
# жёстких 0-100; (б) отдельная, более контрастная палитра групп ТОЛЬКО для
# этих 3 долевых графиков (GROUP_COLORS основной/count-версии не трогается);
# (в) своя форма маркера на группу (круг/квадрат/треугольник) — различимость
# не только по цвету; (г) чуть толще линии и крупнее маркеры.
# ---------------------------------------------------------------------------
GROUP_COLORS_SHARE = {
    "classic": "#0D47A1",  # сильный синий
    "ml": "#EF6C00",       # сильный оранжевый
    "bigai": "#7B1FA2",    # сильный фиолетовый/маджента
}
GROUP_MARKERS_SHARE = {
    "classic": "o",   # круг
    "ml": "s",        # квадрат
    "bigai": "^",     # треугольник
}


def chart_groups_per_axis_share(rows, axis_key, out_name, title, xlabel):
    order = AXIS_ORDERS[axis_key]
    labels = AXIS_TICK_LABELS[axis_key]
    denom = AXIS_LEVEL_TOTALS[axis_key]
    x = np.arange(len(order))

    fig, ax = plt.subplots(figsize=(10, 6.5))
    all_values = []
    for g in GROUP_ORDER:
        for outcome, ls, ru in (("success", "-", "успех"), ("failure", "--", "провал")):
            ys = []
            for lvl in order:
                cell = [r for r in rows if group_of(r) == g and r[axis_key] == lvl]
                if not cell:
                    # честный разрыв: у группы вообще нет кейсов на этом уровне
                    ys.append(None)
                else:
                    cnt = sum(1 for r in cell if r["outcome"] == outcome)
                    ys.append(cnt / denom[lvl] * 100)
            xs_plot = [xi for xi, yi in zip(x, ys) if yi is not None]
            ys_plot = [yi for yi in ys if yi is not None]
            all_values.extend(ys_plot)
            ax.plot(
                xs_plot, ys_plot, marker=GROUP_MARKERS_SHARE[g], markersize=7.5,
                linewidth=2.4, linestyle=ls, color=GROUP_COLORS_SHARE[g],
                label=f"{GROUP_LABELS[g]} — {ru}",
            )

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("доля от всех кейсов на этом уровне, %")
    y_max = max(all_values) if all_values else 1.0
    ax.set_ylim(0, y_max * 1.15)
    ax.set_title(title, fontsize=12)
    ax.grid(True, linestyle=":", alpha=0.3)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.legend(fontsize=8.5, loc="best")
    fig.text(
        0.5, 0.035,
        "сплошная — успех, пунктир — провал; знаменатель — ВСЕ кейсы на этом уровне оси"
        " (все 7 классов, все 4 исхода), не только 3 группы/успех+провал",
        ha="center", fontsize=7, color="#555555",
    )
    fig.text(
        0.5, 0.01,
        "6 линий НЕ обязаны суммироваться в 100%; разрыв линии = у группы вообще нет"
        " кейсов на этом уровне (не 0%)",
        ha="center", fontsize=7, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.09, 1, 1))
    fig.savefig(HERE / out_name, dpi=150)
    plt.close(fig)
    print(out_name, "saved")


def chart_groups_axis1_uncertainty_share(rows):
    chart_groups_per_axis_share(
        rows, "axis1_level", "chart-groups-axis1-uncertainty-share.png",
        "Классика vs МЛ vs большой ИИ: доля от кейсов на уровне неопределённости",
        "Неопределённость задачи",
    )


def chart_groups_axis2_feedback_share(rows):
    chart_groups_per_axis_share(
        rows, "axis2_bucket", "chart-groups-axis2-feedback-share.png",
        "Классика vs МЛ vs большой ИИ: доля от кейсов на уровне времени обратной связи",
        "Время обратной связи",
    )


def chart_groups_axis4_blastradius_share(rows):
    chart_groups_per_axis_share(
        rows, "axis4_blast_radius", "chart-groups-axis4-blastradius-share.png",
        "Классика vs МЛ vs большой ИИ: доля от кейсов на уровне цены ошибки",
        "Цена ошибки (blast radius)",
    )


if __name__ == "__main__":
    rows = load_rows()
    chart_donut_axisA_axisB(rows)
    chart_donut_class_vs_uncertainty(rows)
    _burn_random_draws(1366)  # см. docstring _burn_random_draws — сохраняет chart3/dist нетронутыми
    chart3(rows)
    chart_surface_axisA_axisB(rows)
    chart_surface_axisA_axisC(rows)
    chart_lines_outcome_per_axis(rows)
    chart_dist_points_per_axis(rows)
    chart_groups_axis1_uncertainty(rows)
    chart_groups_axis2_feedback(rows)
    chart_groups_axis4_blastradius(rows)
    chart_wow_slope_successrate(rows)
    chart_wow_radar(rows)
    chart_wow_gate_dumbbell(rows)
    chart_lines_outcome_share_per_axis(rows)
    chart_groups_axis1_uncertainty_share(rows)
    chart_groups_axis2_feedback_share(rows)
    chart_groups_axis4_blastradius_share(rows)
