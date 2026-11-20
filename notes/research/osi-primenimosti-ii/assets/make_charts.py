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

Раунд 7 (chart_headline_*, chart_industry_*, chart_tornado_*, chart_mechanism_detail; файл
10-industriya-i-rejting-faktorov.md, issue #349): владелец — "как-то все еще не интересно 1 сделай
оси более детальными 2 подумай какие еще графики и выводы можно показать, пока не видно прям бомбы".
Четыре новых графика, все числа пересчитаны этой сессией НАПРЯМУЮ из reestr-reshenij.csv (не
переданы вербатим, в отличие от файлов 08-09) по формуле (B) = success/(success+failure) ровно,
partial/undetermined исключены из числителя И знаменателя — единственная формула успеха, используемая
в этом раунде (см. 10-industriya-i-rejting-faktorov.md §0 про расхождение с 75,4%/18,2% файла 07,
который использует другую, partial-взвешенную формулу (C) — это разница формул, не противоречие
данных, n по статусу гейта совпадает между файлами буквально 143/112/120/46):
  - chart-headline-gate-failure-attribution — две бублик-диаграммы (137 провалов / 108 успехов) по
    статусу гейта, с crIMMсон callout "96,4% провалов без гейта" / "только 4 (2,9%) несмотря на гейт".
  - chart-industry-success-rate — горизонтальный бар-чарт, 12 отраслей по ставке успеха, тонкие
    ячейки (n<20) помечены штриховкой и звёздочкой.
  - chart-tornado-axis-ranking — tornado-чарт, разброс (max−min) по 6 измерениям (гейт/отрасль/
    blast radius/неопределённость/класс метода/время обратной связи), время обратной связи —
    исходная гипотеза курса — внизу как самое слабое.
  - chart-mechanism-detail — 2 панели, ставка успеха по механизму оси1 (U1-U4) и оси2 (F-A/F-B/F-C),
    базовая линия "none" серым штрихом, U4 (n=1) помечен как не показательный.
"""
import csv
import random
from collections import Counter, defaultdict
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


# ---------------------------------------------------------------------------
# Раунд 7 (issue #349, файл 10-industriya-i-rejting-faktorov.md): владелец
# попросил детальнее оси + "бомбу". Все числа здесь считаются НАПРЯМУЮ из rows
# внутри каждой функции (не хардкод) по формуле (B) = success/(success+failure),
# тем же способом, что _succ_rate выше (не путать с формулой (C) файла 07).
# ---------------------------------------------------------------------------
def _rate_and_n(sub):
    """(ставка_в_%_или_None, success+failure, success, failure) — формула (B), чистая."""
    s = sum(1 for r in sub if r["outcome"] == "success")
    f = sum(1 for r in sub if r["outcome"] == "failure")
    denom = s + f
    rate = (s / denom * 100) if denom > 0 else None
    return rate, denom, s, f


INDUSTRY_LABELS_RU = {
    "frontier-space": "Космос / фронтир",
    "digital-twins": "Цифровые двойники",
    "scientific-research": "Научные исследования",
    "manufacturing": "Производство",
    "trust-recognition": "Доверие / распознавание",
    "agriculture": "Сельское хозяйство",
    "logistics": "Логистика",
    "cad-cam": "CAD/CAM",
    "product-lifecycle": "Жизненный цикл продукта",
    "telecom-cybersecurity": "Телеком / кибербезопасность",
    "sdlc": "Разработка ПО (SDLC)",
    "medical-decision": "Медицинские решения",
}

THIN_N = 20  # n(успех+провал) < этого порога -> ячейка помечается как тонкая


# ---------------------------------------------------------------------------
# Chart 18 ("бомба" 1/4): гейт x исход, два бублика рядом — 137 провалов и
# 108 успехов, каждый разбит по статусу гейта. Самый чистый, immune-to-formula
# результат всего раунда (Finding 1) — чистые счётчики, без ставок и делений.
# ---------------------------------------------------------------------------
GATE_STATUS_ORDER = ["no", "not-applicable", "yes", "unclear"]
GATE_STATUS_LABELS = {
    "no": "гейта нет",
    "not-applicable": "гейт неприменим",
    "yes": "гейт есть",
    "unclear": "не указано",
}
GATE_STATUS_COLORS = {
    "no": "#B23A48",
    "not-applicable": "#D98C44",
    "yes": "#2E7D32",
    "unclear": "#B0B0B0",
}


def chart_headline_gate_failure_attribution(rows):
    failures = [r for r in rows if r["outcome"] == "failure"]
    successes = [r for r in rows if r["outcome"] == "success"]
    print(
        "chart_headline_gate_failure_attribution: n_failures =", len(failures),
        "n_successes =", len(successes),
    )

    def counts_by_gate(sub):
        c = Counter(r["axis4_gate"] for r in sub)
        return [c.get(g, 0) for g in GATE_STATUS_ORDER]

    fail_counts = counts_by_gate(failures)
    succ_counts = counts_by_gate(successes)
    no_gate_n = fail_counts[GATE_STATUS_ORDER.index("no")] + fail_counts[GATE_STATUS_ORDER.index("not-applicable")]
    despite_gate_n = fail_counts[GATE_STATUS_ORDER.index("yes")]

    fig, axes = plt.subplots(1, 2, figsize=(15.5, 9))

    for ax, counts, n_total, title in (
        (axes[0], fail_counts, len(failures), f"{len(failures)} провалов — по статусу гейта"),
        (axes[1], succ_counts, len(successes), f"{len(successes)} успехов — по статусу гейта"),
    ):
        colors = [GATE_STATUS_COLORS[g] for g in GATE_STATUS_ORDER]
        wedges, _texts, _autotexts = ax.pie(
            counts, colors=colors, startangle=90, counterclock=False,
            wedgeprops=dict(width=0.42, edgecolor="white", linewidth=1.8),
            autopct=lambda pct: f"{pct:.1f}%" if pct >= 4 else "",
            pctdistance=0.78,
            textprops=dict(fontsize=10.5, fontweight="bold", color="#222222"),
        )
        small_idx = 0
        for w, g, cnt in zip(wedges, GATE_STATUS_ORDER, counts):
            if cnt == 0:
                continue
            ang = np.radians((w.theta2 + w.theta1) / 2)
            x, y = np.cos(ang), np.sin(ang)
            frac = cnt / n_total
            if frac < 0.05:
                # маленький клин (<5%) — отодвигаем дальше и разводим по перпендикуляру,
                # иначе соседние маленькие клинья (здесь: "гейт есть" n=4 и "не указано"
                # n=1 на диаграмме провалов) ложатся подписями друг на друга.
                perp_x, perp_y = -y, x
                sign = 1 if small_idx % 2 == 0 else -1
                small_idx += 1
                tx, ty = x * 1.75 + perp_x * 0.3 * sign, y * 1.75 + perp_y * 0.3 * sign
            else:
                tx, ty = x * 1.3, y * 1.3
            ax.annotate(
                f"{GATE_STATUS_LABELS[g]}\nn={cnt}",
                xy=(x * 0.79, y * 0.79), xytext=(tx, ty),
                ha="center", fontsize=9.5, color=GATE_STATUS_COLORS[g], fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=GATE_STATUS_COLORS[g], lw=1.0),
            )
        ax.set_title(title, fontsize=14, fontweight="bold", pad=22)
        ax.text(0, 0, f"n={n_total}", ha="center", va="center", fontsize=16,
                 fontweight="bold", color="#333333")

    fig.suptitle(
        "Где случились провалы и успехи — по статусу действующего гейта",
        fontsize=17, fontweight="bold", y=0.985,
    )
    fig.text(
        0.5, 0.065,
        f"96,4% провалов ({no_gate_n} из {len(failures)}) — без действующего гейта\n"
        f"Только {despite_gate_n} ({despite_gate_n/len(failures)*100:.1f}%) — несмотря на активный гейт",
        ha="center", fontsize=15, fontweight="bold", color="#8C1C27",
        bbox=dict(boxstyle="round,pad=0.6", facecolor="#FCE8E8", edgecolor="#8C1C27", linewidth=1.8),
    )
    fig.text(
        0.5, 0.012,
        "Формула — чистые счётчики (Finding 1), без деления и без выбора ставки успешности;"
        " immune к проблеме несогласованности формул (см. файл 10 §0).",
        ha="center", fontsize=7.8, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.14, 1, 0.94))
    fig.savefig(HERE / "chart-headline-gate-failure-attribution.png", dpi=150)
    plt.close(fig)
    print("chart_headline_gate_failure_attribution saved")


# ---------------------------------------------------------------------------
# Chart 19 ("бомба" 2/4): отрасль как ось — 12 отраслей по ставке успеха
# (формула B), сортировка по убыванию, тонкие ячейки (n<20) — штрихом+звёздочкой.
# ---------------------------------------------------------------------------
def chart_industry_success_rate(rows):
    industries = sorted(set(r["industry"] for r in rows))
    data = []
    for ind in industries:
        sub = [r for r in rows if r["industry"] == ind]
        rate, denom, s, f = _rate_and_n(sub)
        if rate is None:
            continue
        data.append((ind, round(rate, 1), denom))
    data.sort(key=lambda t: -t[1])  # по убыванию ставки
    order = list(reversed(data))  # по возрастанию -> позиция 0 (низ) .. n-1 (верх)

    y = np.arange(len(order))
    cmap = plt.cm.RdYlGn
    norm = plt.Normalize(vmin=0, vmax=100)

    fig, ax = plt.subplots(figsize=(11.5, 8.3))
    bars = ax.barh(
        y, [d[1] for d in order], color=[cmap(norm(d[1])) for d in order],
        edgecolor="#333333", linewidth=0.8, height=0.62, zorder=3,
    )
    for bar, (ind, rate, denom) in zip(bars, order):
        thin = denom < THIN_N
        if thin:
            bar.set_hatch("//")
            bar.set_edgecolor("#555555")
        ax.text(
            rate + 1.8, bar.get_y() + bar.get_height() / 2,
            f"n={denom}" + (" *" if thin else ""),
            va="center", fontsize=8.8, color="#333333",
        )

    ax.set_yticks(y)
    ax.set_yticklabels([
        INDUSTRY_LABELS_RU.get(ind, ind) + (" *" if denom < THIN_N else "")
        for ind, rate, denom in order
    ], fontsize=9.8)
    ax.set_xlim(0, 118)
    ax.set_xlabel("доля успеха среди (успех+провал), % — формула (B)")
    ax.set_title(
        "Доля успеха по отрасли: разброс шире, чем у любой из 4 осей курса", fontsize=13.5,
    )
    ax.grid(True, axis="x", linestyle=":", alpha=0.3)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    lo_ind, lo_rate, lo_n = order[0]
    hi_ind, hi_rate, hi_n = order[-1]
    # Обе подписи ставятся в пустое пространство справа/снизу от коротких баров
    # того же ряда (не поверх соседних баров), ha="left" от точки привязки.
    ax.annotate(
        f"крайнее значение диапазона,\nn={hi_n} — тонкая ячейка",
        xy=(hi_rate, len(order) - 1), xytext=(103, len(order) - 2.7),
        ha="left", fontsize=8.3, color="#8C1C27", fontweight="bold",
        arrowprops=dict(arrowstyle="->", color="#8C1C27"),
    )
    ax.annotate(
        f"самая тонкая ячейка раунда,\nn={lo_n}",
        xy=(lo_rate, 0), xytext=(48, 0.4),
        ha="left", fontsize=8.3, color="#8C1C27", fontweight="bold",
        arrowprops=dict(arrowstyle="->", color="#8C1C27"),
    )

    fig.text(
        0.5, 0.012,
        f"* n(успех+провал) < {THIN_N} — тонкая ячейка: несколько иначе размеченных кейсов могли бы"
        " заметно сдвинуть эту ставку. Формула — чистая success/(success+failure) (B), см. файл 10 §0.",
        ha="center", fontsize=7.6, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.045, 1, 1))
    fig.savefig(HERE / "chart-industry-success-rate.png", dpi=150)
    plt.close(fig)
    print("chart_industry_success_rate saved")
    for ind, rate, denom in data:
        print(f"  {ind}: {rate}% n={denom}")


# ---------------------------------------------------------------------------
# Chart 20 ("бомба" 3/4): tornado — разброс (max-min) ставки успеха (формула B)
# по 6 измерениям; время обратной связи (исходная гипотеза курса) подсвечено
# отдельным цветом и поставлено внизу как самое слабое из проверенных.
# ---------------------------------------------------------------------------
def _industry_extremes(rows):
    industries = sorted(set(r["industry"] for r in rows))
    rates = []
    for ind in industries:
        sub = [r for r in rows if r["industry"] == ind]
        rate, denom, s, f = _rate_and_n(sub)
        if rate is not None:
            rates.append((ind, round(rate, 1), denom))
    rates.sort(key=lambda t: t[1])
    return rates[0], rates[-1]


def chart_tornado_axis_ranking(rows):
    dims = []

    def rate_n(sub):
        rate, denom, s, f = _rate_and_n(sub)
        return round(rate, 1), denom

    rate_yes, n_yes = rate_n([r for r in rows if r["axis4_gate"] == "yes"])
    rate_no, n_no = rate_n([r for r in rows if r["axis4_gate"] == "no"])
    dims.append(dict(
        name="Гейт/обратимость", rng=round(rate_yes - rate_no, 1),
        lo_label=f"нет гейта\n{rate_no}% (n={n_no})",
        hi_label=f"гейт есть\n{rate_yes}% (n={n_yes})",
        highlight=False,
    ))

    (ind_lo, rate_lo, n_lo), (ind_hi, rate_hi, n_hi) = _industry_extremes(rows)
    dims.append(dict(
        name="Отрасль", rng=round(rate_hi - rate_lo, 1),
        lo_label=f"{INDUSTRY_LABELS_RU.get(ind_lo, ind_lo)}\n{rate_lo}% (n={n_lo})",
        hi_label=f"{INDUSTRY_LABELS_RU.get(ind_hi, ind_hi)}\n{rate_hi}% (n={n_hi})",
        highlight=False,
    ))

    rate_low, n_low = rate_n([r for r in rows if r["axis4_blast_radius"] == "low"])
    rate_high, n_high = rate_n([r for r in rows if r["axis4_blast_radius"] == "high"])
    dims.append(dict(
        name="Цена ошибки\n(blast radius)", rng=round(rate_low - rate_high, 1),
        lo_label=f"высокая\n{rate_high}% (n={n_high})",
        hi_label=f"низкая\n{rate_low}% (n={n_low})",
        highlight=False,
    ))

    rate_a1low, n_a1low = rate_n([r for r in rows if r["axis1_level"] == "low"])
    rate_a1ext, n_a1ext = rate_n([r for r in rows if r["axis1_level"] == "extreme"])
    dims.append(dict(
        name="Неопределённость", rng=round(rate_a1low - rate_a1ext, 1),
        lo_label=f"экстремальная\n{rate_a1ext}% (n={n_a1ext})",
        hi_label=f"низкая\n{rate_a1low}% (n={n_a1low})",
        highlight=False,
    ))

    rate_ml, n_ml = rate_n([r for r in rows if group_of(r) == "ml"])
    rate_bigai, n_bigai = rate_n([r for r in rows if group_of(r) == "bigai"])
    dims.append(dict(
        name="Класс метода\n(3 группы)", rng=round(rate_ml - rate_bigai, 1),
        lo_label=f"большой ИИ\n{rate_bigai}% (n={n_bigai})",
        hi_label=f"МЛ\n{rate_ml}% (n={n_ml})",
        highlight=False,
    ))

    rate_fast, n_fast = rate_n([r for r in rows if r["axis2_bucket"] == "seconds-minutes"])
    rate_slow, n_slow = rate_n([r for r in rows if r["axis2_bucket"] == "season-years"])
    dims.append(dict(
        name="Время обратной связи\n(исходная гипотеза курса)",
        rng=round(rate_fast - rate_slow, 1),
        lo_label=f"сезон-годы\n{rate_slow}% (n={n_slow})",
        hi_label=f"секунды-минуты\n{rate_fast}% (n={n_fast})",
        highlight=True,
    ))

    for d in dims:
        print("chart_tornado_axis_ranking:", d["name"].replace("\n", " "), "rng=", d["rng"])

    dims.sort(key=lambda d: d["rng"])  # самый маленький внизу (y=0) -> самый большой наверху

    y = np.arange(len(dims))
    fig, ax = plt.subplots(figsize=(12, 7.8))
    for yi, d in zip(y, dims):
        color = "#C1272D" if d["highlight"] else "#1C7293"
        ax.barh(yi, d["rng"], color=color, edgecolor="#333333", linewidth=0.8,
                height=0.56, zorder=3)
        ax.text(-2, yi, d["lo_label"], ha="right", va="center", fontsize=8.0, color="#444444")
        ax.text(d["rng"] + 2, yi, d["hi_label"], ha="left", va="center", fontsize=8.0,
                color="#444444", fontweight="bold" if d["highlight"] else "normal")
        ax.text(d["rng"] / 2, yi, f"{d['rng']:.1f} п.п.", ha="center", va="center",
                fontsize=9.8, color="white", fontweight="bold", zorder=4)

    ax.set_yticks(y)
    ax.set_yticklabels([d["name"] for d in dims], fontsize=9.8)
    ax.set_xlim(-42, 128)
    ax.set_xlabel("разброс доли успеха (max − min), п.п. — формула (B)")
    ax.set_title(
        "Какое измерение больше всего разделяет успех и провал — разброс по 6 измерениям",
        fontsize=12.8,
    )
    ax.grid(True, axis="x", linestyle=":", alpha=0.25)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)

    fig.text(
        0.5, 0.06,
        "↓ Время обратной связи — исходная гипотеза этой исследовательской линии — внизу специально:\n"
        "из всех 6 проверенных измерений у неё самый маленький разброс ставки успеха.",
        ha="center", fontsize=8.5, color="#C1272D", fontweight="bold",
    )
    fig.text(
        0.5, 0.012,
        "Разброс = round(ставка_max,1) − round(ставка_min,1); «отрасль» и «класс метода» считаются"
        " по тем же n, что в файле 10 §2/§3.",
        ha="center", fontsize=7.3, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.13, 1, 1))
    fig.savefig(HERE / "chart-tornado-axis-ranking.png", dpi=150)
    plt.close(fig)
    print("chart_tornado_axis_ranking saved")


# ---------------------------------------------------------------------------
# Chart 21 ("бомба" 4/4): детализация механизмов — ставка успеха (формула B)
# по axis1_mechanism (U1-U4 vs none) и axis2_mechanism (F-A/F-B/F-C vs none),
# "none" — серая базовая линия, U4 (n=1) помечен как не показательный.
# ---------------------------------------------------------------------------
MECH1_ORDER = ["none", "U1", "U2", "U3", "U4"]
MECH1_LABELS = {
    "none": "нет именованного\nмеханизма",
    "U1": "U1 — алеаторный\nпотолок",
    "U2": "U2 — нестационар-\nность",
    "U3": "U3 — инженерное\nузкое место",
    "U4": "U4 — доверие/\nаверсия",
}
MECH2_ORDER = ["none", "F-A", "F-B", "F-C"]
MECH2_LABELS = {
    "none": "нет именованного\nмеханизма",
    "F-A": "F-A — чистая\nзадержка",
    "F-B": "F-B — разрежен-\nность/конфаундинг",
    "F-C": "F-C — жёсткое\nреальное время",
}


def chart_mechanism_detail(rows):
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 6.8))
    norm = plt.Normalize(vmin=0, vmax=100)

    for ax, key, order, labels, title in (
        (axes[0], "axis1_mechanism", MECH1_ORDER, MECH1_LABELS,
         "Механизм неопределённости (ось 1)"),
        (axes[1], "axis2_mechanism", MECH2_ORDER, MECH2_LABELS,
         "Механизм обратной связи (ось 2)"),
    ):
        rates, denoms = [], []
        for lvl in order:
            sub = [r for r in rows if r[key] == lvl]
            rate, denom, s, f = _rate_and_n(sub)
            rates.append(round(rate, 1) if rate is not None else 0.0)
            denoms.append(denom)
            print(f"chart_mechanism_detail: {key}={lvl} rate={rate} n={denom}")

        x = np.arange(len(order))
        colors, hatches = [], []
        for lvl, rate in zip(order, rates):
            if lvl == "none":
                colors.append("#B0B0B0")
                hatches.append("//")
            else:
                colors.append(plt.cm.RdYlGn(norm(rate)))
                hatches.append(None)

        bars = ax.bar(x, rates, color=colors, edgecolor="#333333", linewidth=0.8)
        for bar, hatch in zip(bars, hatches):
            if hatch:
                bar.set_hatch(hatch)

        for xi, rate, denom, lvl in zip(x, rates, denoms, order):
            label = f"{rate:.1f}%\nn={denom}"
            if lvl == "U4":
                label += "\n(n=1, не\nпоказательно)"
            ax.text(xi, rate + 2.5, label, ha="center", fontsize=7.6, color="#333333")

        ax.set_xticks(x)
        ax.set_xticklabels([labels[lvl] for lvl in order], fontsize=8.2)
        ax.set_ylim(0, 80)
        ax.set_ylabel("доля успеха среди (успех+провал), % — формула (B)", fontsize=8.5)
        ax.set_title(title, fontsize=11.8)
        ax.grid(True, axis="y", linestyle=":", alpha=0.3)
        for spine in ("top", "right"):
            ax.spines[spine].set_visible(False)

    fig.suptitle(
        "Детализация осей: именованный механизм снижает успех резче, чем просто уровень оси",
        fontsize=13,
    )
    fig.text(
        0.5, 0.012,
        "серый/штрих — базовая линия «механизм не назван»; U4 помечен отдельно: при n=1 это один"
        " кейс, не оценка доли.",
        ha="center", fontsize=7.6, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.04, 1, 0.92))
    fig.savefig(HERE / "chart-mechanism-detail.png", dpi=150)
    plt.close(fig)
    print("chart_mechanism_detail saved")


# ===========================================================================
# Раунд 8 (issue #349, файл 11-pyat-razryvayushchih-illyustraciy.md): владелец —
# «все равно что-то не цепляет». Пять новых иллюстраций, каждая несёт >=2 (до 4)
# самостоятельных находки в одном кадре. Углы выбраны ЭТОЙ сессией самостоятельно
# по свободному проходу по reestr-reshenij.csv (владелец явно запретил кормить
# исполнителя готовыми темами). Все числа считаются из rows внутри функций,
# ключевые заголовочные значения дополнительно закреплены assert'ами — при любом
# будущем изменении реестра скрипт упадёт, а не молча нарисует устаревшую цифру.
# Формула успеха там, где она есть, — только (B) = success/(success+failure)
# (конвенция раундов 3-7, файл 10 §0); графики 2 и 4 — чистые счётчики/карточки
# без формулы вообще; график 5 дополнительно показывает РЯДОМ уже документированную
# формулу (C) файла 07 — это сравнение двух существующих формул линии, НЕ введение
# четвёртой (файл 10 §0 называет ровно три: A, B, C).
# Randomness: ни одна из пяти функций не трогает глобальный поток random —
# джиттера нет, существующие графики не сдвигаются.
# ===========================================================================

WOW2_GREEN = "#2E7D32"
WOW2_RED = "#B23A48"
WOW2_ACCENT = "#1C7293"


def _has_named_mechanism(r):
    """Назван ли у строки хоть один структурный механизм (U1-U4 или F-A/F-B/F-C)."""
    return r["axis1_mechanism"] in ("U1", "U2", "U3", "U4") or r[
        "axis2_mechanism"
    ] in ("F-A", "F-B", "F-C")


def _row_by_id(rows, rid):
    for r in rows:
        if r["id"] == rid:
            return r
    raise KeyError(rid)


# ---------------------------------------------------------------------------
# WOW2-1: «Два мира» — при действующем гейте ВСЕ оси курса перестают работать.
# Внутри gate=yes (n=143) ставка успеха (B) почти не зависит ни от
# неопределённости, ни от времени обратной связи, ни от цены ошибки (разброс
# 7-16 п.п., всё в коридоре 84-100%); внутри gate=no (n=112) те же оси дают
# разброс до 80 п.п. Вся предсказательная сила осей курса живёт в мире без гейта.
# ---------------------------------------------------------------------------
def chart_wow2_dva_mira(rows):
    dims = [
        ("axis1_level", ["low", "moderate", "high", "extreme"],
         ["низк.", "умер.", "выс.", "экстр."], "Неопределённость"),
        ("axis2_bucket", ["seconds-minutes", "hours-days", "weeks-months", "season-years"],
         ["сек-мин", "час-дни", "нед-мес", "сез-годы"], "Время обратной связи"),
        ("axis4_blast_radius", ["low", "medium", "high", "catastrophic"],
         ["низк.", "средн.", "выс.", "катастр."], "Цена ошибки"),
    ]

    def panel_data(gate_value):
        out = []
        for key, levels, lvl_labels, title in dims:
            pts = []
            for lv, lab in zip(levels, lvl_labels):
                sub = [r for r in rows if r["axis4_gate"] == gate_value and r[key] == lv]
                rate, denom, s, f = _rate_and_n(sub)
                pts.append((lab, rate, denom, s, f))
            out.append((title, key, pts))
        return out

    yes_data = panel_data("yes")
    no_data = panel_data("no")
    rate_yes, n_yes, s_yes, f_yes = _rate_and_n([r for r in rows if r["axis4_gate"] == "yes"])
    rate_no, n_no, s_no, f_no = _rate_and_n([r for r in rows if r["axis4_gate"] == "no"])
    # Заголовочные числа закреплены (см. docstring раунда 8):
    assert (s_yes, f_yes) == (74, 4) and round(rate_yes, 1) == 94.9
    assert (s_no, f_no) == (10, 79) and round(rate_no, 1) == 11.2

    fig, axes = plt.subplots(1, 2, figsize=(16.5, 8.6), sharey=True)
    panel_specs = [
        (axes[0], yes_data, rate_yes,
         f"МИР С ДЕЙСТВУЮЩИМ ГЕЙТОМ — {s_yes + f_yes} кейсов с исходом",
         "#F2F8F2", WOW2_GREEN),
        (axes[1], no_data, rate_no,
         f"МИР БЕЗ ГЕЙТА — {s_no + f_no} кейсов с исходом",
         "#FBF2F3", WOW2_RED),
    ]
    offsets = [-0.27, -0.09, 0.09, 0.27]
    for ax, data, overall, title, facecolor, edge in panel_specs:
        ax.set_facecolor(facecolor)
        ax.axhline(overall, color=edge, lw=1.4, ls="--", zorder=1)
        overall_txt = "общий успех " + f"{overall:.1f}%".replace(".", ",")
        if overall > 50:
            ax.annotate(overall_txt, xy=(0.62, overall - 0.8), xytext=(0.5, 54),
                        fontsize=10, fontweight="bold", color=edge, ha="left",
                        arrowprops=dict(arrowstyle="->", color=edge, lw=1.2))
        else:
            ax.text(0.5, overall + 2.3, overall_txt,
                    color=edge, fontsize=10, fontweight="bold", ha="left")
        for gi, (gtitle, key, pts) in enumerate(data):
            xc = gi + 1
            accent = WOW2_ACCENT if key == "axis2_bucket" else "#444444"
            rates = [p[1] for p in pts if p[1] is not None]
            if rates:
                ax.vlines(xc, min(rates), max(rates), color=accent, lw=2.4,
                          alpha=0.55, zorder=2)
            for off, (lab, rate, denom, s, f) in zip(offsets, pts):
                if rate is None:
                    continue
                thin = denom < 10
                ax.plot(xc + off, rate, "o", ms=9,
                        mfc="white" if thin else accent, mec=accent, mew=1.8, zorder=3)
                ax.annotate(f"{rate:.0f}", (xc + off, rate),
                            textcoords="offset points", xytext=(0, 8),
                            ha="center", fontsize=8.2, color=accent)
                ax.annotate(lab, (xc + off, rate),
                            textcoords="offset points", xytext=(0, -14),
                            ha="center", fontsize=7.0, color="#666666")
            spread = (max(rates) - min(rates)) if rates else 0.0
            ax.text(xc, -13.5,
                    f"{gtitle}\nразброс " + f"{spread:.1f}".replace(".", ",") + " п.п.",
                    ha="center", fontsize=9.3, color=accent,
                    fontweight="bold" if key == "axis2_bucket" else "normal")
        ax.set_xlim(0.45, 3.55)
        ax.set_ylim(-19, 108)
        ax.set_xticks([])
        ax.set_title(title, fontsize=12.5, fontweight="bold", color=edge, pad=10)
        ax.grid(axis="y", alpha=0.25)
        ax.set_yticks([0, 20, 40, 60, 80, 100])
    axes[0].set_ylabel("ставка успеха, % (формула B)", fontsize=10)

    # Каллауты про катастрофическую цену ошибки в обоих мирах
    cat_yes = _rate_and_n([r for r in rows if r["axis4_gate"] == "yes"
                           and r["axis4_blast_radius"] == "catastrophic"])
    cat_no = _rate_and_n([r for r in rows if r["axis4_gate"] == "no"
                          and r["axis4_blast_radius"] == "catastrophic"])
    assert (cat_yes[2], cat_yes[3]) == (8, 0) and (cat_no[2], cat_no[3]) == (1, 28)
    axes[0].annotate(
        f"катастрофическая цена ошибки,\nно гейт есть: {cat_yes[2]}/{cat_yes[1]} = 100%",
        xy=(3.27, 100), xytext=(2.25, 72), fontsize=9.5, color=WOW2_GREEN,
        fontweight="bold", ha="center",
        arrowprops=dict(arrowstyle="->", color=WOW2_GREEN, lw=1.3),
    )
    axes[1].annotate(
        f"та же катастрофическая цена,\nгейта нет: {cat_no[2]}/{cat_no[1]} = "
        + f"{cat_no[0]:.1f}%".replace(".", ","),
        xy=(3.27, cat_no[0]), xytext=(2.4, 55), fontsize=9.5, color=WOW2_RED,
        fontweight="bold", ha="center",
        arrowprops=dict(arrowstyle="->", color=WOW2_RED, lw=1.3),
    )
    axes[1].annotate(
        "исходная гипотеза курса (ось 2):\nвесь её сигнал — только в этом мире",
        xy=(2, 26.7), xytext=(1.25, 88), fontsize=9.0, color=WOW2_ACCENT, ha="center",
        arrowprops=dict(arrowstyle="->", color=WOW2_ACCENT, lw=1.2),
    )
    axes[0].annotate(
        "ось 2 при гейте: разброс 7,1 п.п.\n(93,9-100% — предсказывать нечего)",
        xy=(2, 93.9), xytext=(1.3, 62), fontsize=9.0, color=WOW2_ACCENT, ha="center",
        arrowprops=dict(arrowstyle="->", color=WOW2_ACCENT, lw=1.2),
    )

    fig.suptitle(
        "Два мира одного корпуса: при действующем гейте оси курса перестают предсказывать",
        fontsize=15, fontweight="bold",
    )
    fig.text(
        0.5, 0.012,
        "Формула (B) = успех/(успех+провал); полый маркер — тонкая ячейка (успех+провал < 10), её"
        " цифру не читать буквально. Гейт=есть × экстремальная неопределённость: 0 кейсов с"
        " исходом — точки нет честно. n по статусу гейта: есть=143, нет=112 строк корпуса.",
        ha="center", fontsize=7.6, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.035, 1, 0.94))
    fig.savefig(HERE / "chart-wow2-dva-mira.png", dpi=150)
    plt.close(fig)
    print("chart_wow2_dva_mira saved")


# ---------------------------------------------------------------------------
# WOW2-2: «Тот же инструмент — герой и виновник». Шесть вендоров, у каждого в
# корпусе есть и документированный успех, и документированный провал. Бренд не
# разделяет исходы; статус гейта — разделяет (во всех 12 карточках исход
# совпадает со статусом гейта либо гейт не указан). Чистые карточки, без формулы.
# ---------------------------------------------------------------------------
def chart_wow2_geroy_i_vinovnik(rows):
    # (бренд, id успеха, короткая подпись успеха, id провала, короткая подпись провала, доп.строка)
    pairs = [
        ("Claude / Anthropic",
         "L09-009", "На Марсе: планирование маршрута ровера",
         "L14-048", "На ноутбуке: удаление БД за 9 секунд\n(Cursor + Claude Opus 4.6 + PocketOS)",
         "+ ещё 2 провала Claude Code без гейта (L04-006, L14-034)"),
        ("AWS Kiro",
         "L04-002", "Target identification (life sciences)",
         "L04-023", "Инцидент простоя (декабрь 2025)",
         "+ второй провал без гейта: FT-репорт (L14-043)"),
        ("Amazon",
         "L13-003", "Склад: робот Proteus (AMR)",
         "L05-032", "Магазин: Just Walk Out — свёрнут",
         None),
        ("Google",
         "L04-017", "Big Sleep: предотвращённый SQLite zero-day",
         "L04-004", "Gemini CLI: удаление файлов пользователя",
         None),
        ("IBM Watson",
         "L04-028", "ContextQA: покрытие тестами 20%→80%",
         "L05-004", "Watson for Oncology (MSK) — свёрнут",
         "+ Watson Health закрыт (L11-021, гейт неприменим)"),
        ("John Deere",
         "L10-001", "See & Spray: селективный гербицид",
         "L10-049", "FTC v. Deere (право на ремонт)",
         None),
    ]
    gate_badge = {
        "yes": ("ГЕЙТ ЕСТЬ", WOW2_GREEN),
        "no": ("ГЕЙТА НЕТ", WOW2_RED),
        "not-applicable": ("ГЕЙТ НЕПРИМЕНИМ", "#D98C44"),
        "unclear": ("ГЕЙТ НЕ УКАЗАН", "#888888"),
    }

    fig, ax = plt.subplots(figsize=(15, 10.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, len(pairs) * 1.5 + 1.9)
    ax.axis("off")

    n_rows = len(pairs)
    gate_yes_succ = 0
    gate_absent_fail = 0
    for i, (brand, sid, s_label, fid, f_label, extra) in enumerate(pairs):
        y = (n_rows - 1 - i) * 1.5 + 1.6
        srow, frow = _row_by_id(rows, sid), _row_by_id(rows, fid)
        assert srow["outcome"] == "success", sid
        assert frow["outcome"] == "failure", fid
        if srow["axis4_gate"] == "yes":
            gate_yes_succ += 1
        if frow["axis4_gate"] in ("no", "not-applicable"):
            gate_absent_fail += 1
        ax.text(5.0, y + 0.52, brand, ha="center", fontsize=12.5, fontweight="bold",
                color="#21295C")
        for x0, row, label, rid, color, bg in [
            (0.25, srow, s_label, sid, WOW2_GREEN, "#F2F8F2"),
            (5.35, frow, f_label, fid, WOW2_RED, "#FBF2F3"),
        ]:
            ax.add_patch(plt.Rectangle((x0, y - 0.62), 4.4, 1.08, facecolor=bg,
                                       edgecolor=color, lw=1.6,
                                       zorder=2, joinstyle="round"))
            ax.text(x0 + 0.18, y + 0.18, label, fontsize=9.6, va="top",
                    color="#222222", zorder=3)
            btext, bcolor = gate_badge[row["axis4_gate"]]
            ax.text(x0 + 0.18, y - 0.49, btext, fontsize=8.3, fontweight="bold",
                    color="white", zorder=4,
                    bbox=dict(boxstyle="round,pad=0.25", facecolor=bcolor,
                              edgecolor="none"))
            ax.text(x0 + 4.22, y - 0.49, rid, fontsize=7.0, color="#999999",
                    ha="right", zorder=4)
        if extra:
            ax.text(9.73, y + 0.52, extra, fontsize=7.4, color="#8A5050", ha="right")

    ax.text(2.45, n_rows * 1.5 + 1.62, "УСПЕХ", ha="center", fontsize=13,
            fontweight="bold", color=WOW2_GREEN)
    ax.text(7.55, n_rows * 1.5 + 1.62, "ПРОВАЛ", ha="center", fontsize=13,
            fontweight="bold", color=WOW2_RED)

    assert gate_yes_succ == 5 and gate_absent_fail == 6
    ax.text(
        5.0, 0.42,
        f"Счёт по 12 карточкам: {gate_yes_succ} из 6 успехов — при действующем гейте"
        f" (шестой — гейт не указан); {gate_absent_fail} из 6 провалов — без действующего гейта.\n"
        "Ни одной карточки, где исход разошёлся со статусом гейта. Бренд не делит кейсы"
        " на успех и провал — делит гейт.",
        ha="center", fontsize=10.5, fontweight="bold", color="#21295C",
        bbox=dict(boxstyle="round,pad=0.55", facecolor="#EFF3F8", edgecolor="#21295C"),
    )
    ax.set_title(
        "Тот же инструмент — герой и виновник: вопрос не «какой ИИ», а «что стоит между ним и бедой»",
        fontsize=14.5, fontweight="bold", pad=14,
    )
    fig.text(
        0.5, 0.008,
        "Карточки — реальные строки реестра (id в углу), исход и статус гейта читаются из"
        " reestr-reshenij.csv на каждом запуске.\nПары подобраны по вендору: вендоры, у которых в"
        " корпусе есть и успех, и провал одновременно; это иллюстрация распределения, не"
        " причинная выборка.",
        ha="center", fontsize=7.4, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(HERE / "chart-wow2-geroy-i-vinovnik.png", dpi=150)
    plt.close(fig)
    print("chart_wow2_geroy_i_vinovnik saved")


# ---------------------------------------------------------------------------
# WOW2-3: «Мёртвая зона» — воронка из трёх вопросов, на дне которой в корпусе
# нет ни одного успеха: нет гейта -> назван структурный механизм -> высокая/
# катастрофическая цена ошибки = 78 кейсов, 0 успехов, 68 провалов. Выжившие
# предыдущей ступени (4 из 138) поимённо — все при дешёвой/средней цене ошибки.
# ---------------------------------------------------------------------------
def chart_wow2_mertvaya_zona(rows):
    stage0 = rows
    stage1 = [r for r in stage0 if r["axis4_gate"] in ("no", "not-applicable")]
    stage2 = [r for r in stage1 if _has_named_mechanism(r)]
    stage3 = [r for r in stage2 if r["axis4_blast_radius"] in ("high", "catastrophic")]
    stages = [
        ("Весь корпус", stage0),
        ("нет действующего гейта\n(«нет» или «структурно неприменим»)", stage1),
        ("+ назван структурный механизм\n(любой из U1-U4 / F-A / F-B / F-C)", stage2),
        ("+ высокая или катастрофическая\nцена ошибки", stage3),
    ]
    stats = [(_rate_and_n(sub), len(sub)) for _, sub in stages]
    ((r0, d0, s0, f0), n0), ((r1, d1, s1, f1), n1), ((r2, d2, s2, f2), n2), (
        (r3, d3, s3, f3), n3) = stats
    assert (n0, n1, n2, n3) == (421, 232, 138, 78)
    assert (s0, f0) == (108, 137) and (s1, f1) == (20, 132)
    assert (s2, f2) == (4, 96) and (s3, f3) == (0, 68)

    survivors = [r for r in stage2 if r["outcome"] == "success"]
    assert len(survivors) == 4
    surv_labels = {
        "L10-018": "Carbon Robotics LaserWeeder\n(лазерная прополка)",
        "L13-025": "Starship Technologies\n(роботы-курьеры)",
        "L15-021": "NotebookLM (Google)",
        "L15-022": "Elicit (обзор литературы)",
    }
    br_ru = {"low": "цена ошибки: низкая", "medium": "цена ошибки: средняя"}

    fig, ax = plt.subplots(figsize=(15.5, 9.6))
    ax.set_xlim(0, 12.2)
    ax.set_ylim(-0.4, 9.6)
    ax.axis("off")

    cx = 3.3
    max_w = 5.4
    ys = [9.0, 6.8, 4.6, 2.4]
    heights = 1.5
    colors = ["#9FB4C7", "#D98C44", "#C96A5A", WOW2_RED]
    widths = [max_w * n / 421 for n in (n0, n1, n2, n3)]
    for i, ((label, _sub), ((rate, denom, s, f), n), w, col, y) in enumerate(
            zip(stages, stats, widths, colors, ys)):
        ax.add_patch(plt.Rectangle((cx - w / 2, y - heights), w, heights,
                                   facecolor=col, edgecolor="white", lw=2, zorder=2))
        if i < 3:
            w2 = widths[i + 1]
            ax.fill([cx - w / 2, cx + w / 2, cx + w2 / 2, cx - w2 / 2],
                    [y - heights, y - heights, ys[i + 1], ys[i + 1]],
                    color=col, alpha=0.25, zorder=1)
        ax.text(cx, y - heights / 2, f"n = {n}", ha="center", va="center",
                fontsize=13, fontweight="bold", color="white", zorder=3)
        ax.text(cx - max_w / 2 - 0.15, y - heights / 2, label, ha="right",
                va="center", fontsize=9.8, color="#333333")
        rate_txt = ("успех " + f"{rate:.1f}%".replace(".", ",")
                    + f"  ({s} из {denom} с исходом)")
        if i == 3:
            rate_txt = f"успехов: 0 из {denom} с исходом\n({f} провалов, {n - denom} частичных/неопр.)"
        ax.text(cx + max_w / 2 + 0.15, y - heights / 2, rate_txt, ha="left",
                va="center", fontsize=10.5,
                fontweight="bold" if i == 3 else "normal",
                color=WOW2_RED if i == 3 else "#333333")

    ax.annotate(
        "44,1% → 13,2% → 4,0% → 0%:\nкаждый из трёх вопросов\nрежет ставку успеха в 3-4 раза",
        xy=(cx + 0.4, 1.6), xytext=(1.25, 0.25), fontsize=10.5, fontweight="bold",
        color="#21295C", ha="center",
        arrowprops=dict(arrowstyle="->", color="#21295C", lw=1.3),
    )

    # Выжившие ступени 3 (4 из 138) — поимённо, с их ценой ошибки
    bx = 9.55
    ax.text(bx + 1.2, 6.85, "4 выживших ступени «механизм назван»\n— все при дешёвой ошибке:",
            fontsize=9.8, fontweight="bold", color=WOW2_GREEN, ha="center")
    for j, r in enumerate(sorted(survivors, key=lambda x: x["id"])):
        yy = 6.05 - j * 1.12
        ax.add_patch(plt.Rectangle((bx, yy - 0.86), 2.4, 0.96, facecolor="#F2F8F2",
                                   edgecolor=WOW2_GREEN, lw=1.2, zorder=2))
        ax.text(bx + 0.1, yy - 0.06, surv_labels[r["id"]], fontsize=8.0,
                va="top", color="#222222", zorder=3)
        ax.text(bx + 0.1, yy - 0.74, br_ru[r["axis4_blast_radius"]], fontsize=7.4,
                color=WOW2_GREEN, fontweight="bold", zorder=3)
        ax.text(bx + 2.32, yy - 0.74, r["id"], fontsize=6.6, color="#999999",
                ha="right", zorder=3)
    ax.annotate("", xy=(bx - 0.08, 4.4), xytext=(cx + widths[2] / 2 + 0.1, 3.8),
                arrowprops=dict(arrowstyle="->", color=WOW2_GREEN, lw=1.2, ls="--"))

    ax.set_title(
        "Мёртвая зона корпуса: три вопроса — и из 78 кейсов не выжил ни один",
        fontsize=15, fontweight="bold", pad=12,
    )
    fig.text(
        0.5, 0.012,
        "Ставки — формула (B) = успех/(успех+провал); n ступени — все строки, включая частичные/"
        "неопределённые. Ступень 2 объединяет «гейта нет» (112) и «гейт структурно неприменим»"
        " (120)\n— у 78 кейсов дна это не непоставленный чекпойнт, а часто решение, к которому"
        " чекпойнт не прикрутить. Распределение, не причинность: корпус смещён правилом >=30%"
        " провального контента (файл 10 §6).",
        ha="center", fontsize=7.4, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(HERE / "chart-wow2-mertvaya-zona.png", dpi=150)
    plt.close(fig)
    print("chart_wow2_mertvaya_zona saved")


# ---------------------------------------------------------------------------
# WOW2-4: «Закон старше ИИ» — хроника катастрофических провалов без гейта,
# 1981-2026. Самая смертельная клетка реестра (нет гейта × катастрофическая
# цена) не ИИ-клетка: в ней Hyatt Regency (1981), Mars Climate Orbiter (1999),
# Knight Capital (2012), Facebook BGP (2021) — реестр сознательно держит их как
# структурные контрпримеры (README реестра, ограничение 5). ИИ не создал закон —
# он ускорил и участил его нарушение (сгущение точек в 2024-2026).
# ---------------------------------------------------------------------------
def chart_wow2_zakon_starshe_ii(rows):
    import re as _re

    cell = [r for r in rows if r["outcome"] == "failure"
            and r["axis4_blast_radius"] == "catastrophic"
            and r["axis4_gate"] in ("no", "not-applicable")]
    assert len(cell) == 37
    # Дубли одного инцидента между лекциями (Replit и PocketOS/Cursor размечены
    # и в L04, и в L14) — на шкалу идёт одна точка, дубль честно назван в сноске.
    dup_ids = {"L14-047", "L14-048"}
    non_ai_ids = {"L06-023", "L06-021", "L14-045", "L14-046"}  # README реестра, огранич. 5
    short = {
        "L04-004": "Gemini CLI: удаление файлов",
        "L04-022": "Replit: прод-БД в code-freeze",
        "L04-024": "Cursor+Claude: БД за 9 секунд",
        "L06-021": "Mars Climate Orbiter",
        "L06-023": "Hyatt Regency: обрушение переходов",
        "L11-004": "Boeing 737 MAX 9: door plug",
        "L11-020": "GE Predix: закрыт",
        "L11-021": "IBM Watson Health: закрыт",
        "L11-022": "Foxconn Wisconsin",
        "L13-013": "Starsky Robotics: закрыта",
        "L13-014": "Argo AI: закрыта",
        "L13-015": "Embark Trucks: закрыта",
        "L13-017": "TuSimple: делистинг",
        "L13-030": "Uber Tempe: гибель пешехода",
        "L14-001": "CrowdStrike: глобальный сбой",
        "L14-002": "AT&T: обвал сети США",
        "L14-003": "Rogers: обвал сети Канады",
        "L14-041": "Cloudflare: сбой",
        "L14-042": "AWS DynamoDB: DNS-сбой",
        "L14-045": "Knight Capital",
        "L14-046": "Facebook BGP: глобальный сбой",
        "L14-069": "Arup: deepfake-CFO, $25,6M",
    }
    dated, undated = [], []
    for r in cell:
        if r["id"] in dup_ids:
            continue
        years = _re.findall(r"(?:19[5-9]\d|20[0-2]\d)", r["case_name"])
        if years:
            dated.append((int(years[-1]), r))  # конец диапазона = год исхода
        else:
            undated.append(r)
    assert len(dated) == 22 and len(dated) + len(undated) + len(dup_ids) == 37
    dated.sort(key=lambda t: (t[0], t[1]["id"]))
    recent = sum(1 for y, _ in dated if y >= 2024)

    # Разорванная ось времени: слева сжатые 1978-2017, справа растянутые 2017.5-2028 —
    # иначе 19 современных точек нечитаемы; разрыв показан явно (косые штрихи + свои тики).
    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(16.5, 9.2), sharey=True,
        gridspec_kw={"width_ratios": [1, 2.1], "wspace": 0.015},
    )
    panels = [(ax1, 1978.0, 2017.5), (ax2, 2017.5, 2028.2)]

    def draw_point(ax, y, r, lane):
        is_ai = r["id"] not in non_ai_ids
        color = WOW2_RED if is_ai else "#5B6472"
        marker = "o" if is_ai else "s"
        ax.plot([y, y], [0, lane - 0.13], color=color, lw=0.7, alpha=0.35, zorder=1)
        ax.plot(y, lane, marker, ms=8.5, color=color, zorder=3)
        ha = "center"
        dx = 0
        if y >= 2025.7:
            ha, dx = "right", 5
        elif y <= 1982:
            ha, dx = "left", -5
        ax.annotate(short[r["id"]], (y, lane), textcoords="offset points",
                    xytext=(dx, 8), ha=ha, fontsize=7.9, color=color,
                    fontweight="bold" if not is_ai else "normal")

    # Полосы (lane) подбираются жадно: в полосу нельзя ставить подпись ближе
    # min_gap лет к предыдущей в той же полосе; расстояния — в годах ЭТОЙ панели.
    for ax, x0, x1 , in [(p[0], p[1], p[2]) for p in panels]:
        pts = [(y, r) for y, r in dated if x0 <= y < x1]
        lanes = [0.7 + 0.52 * k for k in range(12)] if ax is ax2 else [1.4, 2.9, 4.4]
        min_gap = 2.4 if ax is ax2 else 10.0
        last_in_lane = {}
        for y, r in pts:
            best = max(lanes, key=lambda ln: min(
                (abs(y - prev) for prev in last_in_lane.get(ln, [])), default=1e9))
            gap = min((abs(y - prev) for prev in last_in_lane.get(best, [])), default=1e9)
            if gap < min_gap:
                # все полосы заняты рядом — берём наименее конфликтную (уже выбрана)
                pass
            last_in_lane.setdefault(best, []).append(y)
            draw_point(ax, y, r, best)
        ax.axhline(0, color="#333333", lw=1.2)
        ax.set_xlim(x0, x1)
        ax.set_ylim(-1.9, 7.6)
        ax.set_yticks([])
        ax.grid(axis="x", alpha=0.18)
    ax1.set_xticks([1981, 1990, 1999, 2012])
    ax2.set_xticks([2018, 2020, 2022, 2024, 2026])
    for ax in (ax1, ax2):
        ax.tick_params(axis="x", labelsize=10)
    # Явный разрыв оси
    ax1.spines["right"].set_visible(False)
    ax2.spines["left"].set_visible(False)
    for ax, x in [(ax1, 1), (ax2, 0)]:
        ax.plot([x, x], [-0.013, 0.013], transform=ax.transAxes, color="#333333",
                lw=1.2, clip_on=False)
        ax.plot([x - 0.006, x + 0.006], [-0.02, 0.02], transform=ax.transAxes,
                color="#333333", lw=1.2, clip_on=False)

    # Сгущение: счёт точек по эпохам под осью (границы эпох — целые годы, не
    # координаты плашек, чтобы счёт не зависел от отрисовки)
    era_counts = []
    for ax, bx0, bx1, yr0, yr1, lab in [
            (ax1, 1978.6, 2016.9, 1981, 2017, "1981-2017"),
            (ax2, 2017.8, 2023.4, 2018, 2023, "2018-2023"),
            (ax2, 2023.6, 2027.6, 2024, 2026, "2024-2026")]:
        cnt = sum(1 for y, _ in dated if yr0 <= y <= yr1)
        era_counts.append(cnt)
        ax.add_patch(plt.Rectangle((bx0, -1.62), bx1 - bx0, 1.12,
                                   facecolor="#F4E9EA", edgecolor=WOW2_RED, lw=1.0))
        ax.text((bx0 + bx1) / 2, -1.06, f"{lab}:\n{cnt} катастроф", ha="center",
                va="center", fontsize=9.3, fontweight="bold", color=WOW2_RED)
    assert sum(era_counts) == len(dated) and era_counts[2] == recent == 11

    ax1.plot([], [], "o", color=WOW2_RED, label="с ИИ-компонентом")
    ax1.plot([], [], "s", color="#5B6472", label="без ИИ / до ИИ (контрпримеры реестра)")
    ax1.legend(loc="upper right", fontsize=9.3, framealpha=0.9)

    ax1.text(
        1994.0, 6.4,
        "одна и та же клетка реестра:\nобрушение переходов 1981 года\nи удаление БД за 9 секунд"
        " в 2026-м.\nЗакон не про ИИ — про отсутствие гейта;\nИИ ускорил и участил нарушение"
        f"\n({recent} из {len(dated)} датированных — в 2024-2026)",
        fontsize=10.3, fontweight="bold", color="#21295C", ha="center", va="top",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#EFF3F8", edgecolor="#21295C"),
    )

    fig.suptitle(
        "Закон старше ИИ: 45 лет катастроф в одной клетке «гейта нет × цена катастрофическая»",
        fontsize=15, fontweight="bold",
    )
    fig.text(
        0.5, 0.012,
        f"Клетка: провал × катастрофический blast radius × гейта нет/неприменим — 37 строк"
        f" реестра; на шкале {len(dated)} с годом в названии кейса (для диапазонов — год исхода),"
        f" 2 дубля одного инцидента между лекциями сняты (L14-047≡L04-022, L14-048≡L04-024);\n"
        f"{len(undated)} без даты в названии — не на шкале (Tesla 54 fatalities NHTSA, Babylon,"
        " Zillow Offers, Character.AI, Getty и др.). Не-ИИ кейсы — сознательные структурные"
        " контрпримеры реестра (README, ограничение 5), не шум. Ось времени разорвана на 2017/2018.",
        ha="center", fontsize=7.3, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.035, 1, 0.945))
    fig.savefig(HERE / "chart-wow2-zakon-starshe-ii.png", dpi=150)
    plt.close(fig)
    print("chart_wow2_zakon_starshe_ii saved")


# ---------------------------------------------------------------------------
# WOW2-5: «Серая зона» — 41,8% корпуса (176 из 421: 86 частичных + 90
# неопределённых) не входит ни в один «процент успеха» этой линии (формула B
# выбрасывает их из числителя И знаменателя). Серость распределена неравномерно:
# 12% (SDLC) — 58% (медицина), т.е. рейтинг отраслей по формуле B — отчасти
# рейтинг того, кого вообще удаётся измерить. Обе полюсные отрасли заголовка
# файла 10 («космос 100%» и «медицина 18,2%») — наполовину серые.
# ---------------------------------------------------------------------------
def chart_wow2_seraya_zona(rows):
    total = len(rows)
    oc_all = Counter(r["outcome"] for r in rows)
    gray_total = oc_all["partial"] + oc_all["undetermined"]
    assert total == 421 and gray_total == 176 and oc_all["partial"] == 86

    industries = sorted(set(r["industry"] for r in rows))
    data = []
    for ind in industries:
        sub = [r for r in rows if r["industry"] == ind]
        oc = Counter(r["outcome"] for r in sub)
        gray = oc["partial"] + oc["undetermined"]
        data.append((ind, oc, len(sub), gray / len(sub)))
    data.sort(key=lambda t: t[3])  # серые сверху при отрисовке снизу вверх

    seg_order = ["partial", "undetermined", "failure", "success"]
    seg_colors = {"partial": "#F0AB00", "undetermined": "#B0B0B0",
                  "failure": "#D8A3AA", "success": "#A8CBA9"}

    fig, ax = plt.subplots(figsize=(15.5, 9.4))
    ypos = list(range(len(data)))
    for yi, (ind, oc, n, gshare) in zip(ypos, data):
        left = 0.0
        for seg in seg_order:
            w = 100.0 * oc[seg] / n
            ax.barh(yi, w, left=left, color=seg_colors[seg], edgecolor="white",
                    height=0.72, lw=0.8)
            if w > 5.5:
                ax.text(left + w / 2, yi, str(oc[seg]), ha="center", va="center",
                        fontsize=8.2,
                        color="#333333" if seg != "undetermined" else "#444444")
            left += w
        ax.text(101.2, yi, f"{gshare * 100:.0f}% серого (n={n})", va="center",
                fontsize=9.0, fontweight="bold",
                color="#8A6A00" if gshare >= 0.5 else "#666666")
    # Корпус целиком — отдельной полосой сверху
    yc = len(data) + 1.0
    left = 0.0
    for seg in seg_order:
        w = 100.0 * oc_all[seg] / total
        ax.barh(yc, w, left=left, color=seg_colors[seg], edgecolor="white",
                height=0.72, lw=0.8)
        ax.text(left + w / 2, yc, f"{OUTCOME_LABELS[seg]}: {oc_all[seg]}",
                ha="center", va="center", fontsize=8.6, fontweight="bold")
        left += w
    ax.text(101.2, yc, f"41,8% серого (n={total})", va="center", fontsize=9.6,
            fontweight="bold", color="#8A6A00")
    ax.set_yticks(ypos + [yc])
    ax.set_yticklabels([INDUSTRY_LABELS_RU[d[0]] for d in data] + ["ВЕСЬ КОРПУС"],
                       fontsize=9.6)
    ax.get_yticklabels()[-1].set_fontweight("bold")
    ax.set_xlim(0, 126)
    ax.set_ylim(-5.6, yc + 0.9)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.text(50, -1.25, "доля строк отрасли, % (все 4 исхода, сумма = 100%)",
            ha="center", fontsize=9.3, color="#444444")
    ax.grid(axis="x", alpha=0.2)

    med = next(d for d in data if d[0] == "medical-decision")
    assert (med[1]["success"], med[1]["partial"], med[1]["failure"]) == (2, 10, 9)
    # Медицина по двум уже существующим формулам линии (не новая формула!):
    med_b = 100 * 2 / (2 + 9)
    med_c = 100 * (2 + 0.5 * 10) / (2 + 10 + 9)
    boxes = [
        ("Медицина — «худшая отрасль» (18,2%)?",
         "На деле не проваливается, а наполовину\nработает: частичных (10) больше, чем\n"
         "провалов (9); успехов — 2 из 26 строк.\nПо формуле (C) файла 07 та же медицина —\n"
         + f"{med_c:.1f}%".replace(".", ",") + " — вдвое выше её же "
         + f"{med_b:.1f}%".replace(".", ",") + " по (B)",
         "#8A6A00", 2.5),
        ("Космос — «лучшая отрасль» (100%)?",
         "Тоже наполовину серая: заголовок\n«100% успеха» держится на 17 строках\nиз 32"
         " (6 частичных + 9 неопределённых\nне входят в формулу вообще)",
         "#555555", 44.5),
        ("SDLC — самая «честная» цифра корпуса",
         "Измерено 88% строк отрасли (серых\nвсего 12%) — его низкие 24,1% успеха\n"
         "заработаны на почти полном корпусе,\nа не на половине",
         "#555555", 86.5),
    ]
    for title_t, body, color, x0 in boxes:
        ax.text(x0, -2.1, title_t, fontsize=9.4, fontweight="bold", color=color,
                va="top", ha="left")
        ax.text(x0, -2.85, body, fontsize=8.6, color=color, va="top", ha="left")

    ax.set_title(
        "Серая зона: 176 из 421 кейсов (41,8%) не входят ни в один «процент успеха» этой линии",
        fontsize=14.5, fontweight="bold", pad=12,
    )
    fig.text(
        0.5, 0.012,
        "Формула (B) = успех/(успех+провал) выбрасывает частичные и неопределённые исходы из"
        " числителя И знаменателя — все ставки раундов 3-7 посчитаны по 245 строкам из 421.\n"
        "Сравнение (B) и (C) для медицины — две УЖЕ документированные формулы линии (файл 10 §0),"
        " не новая четвёртая. Сортировка отраслей — по доле серого.",
        ha="center", fontsize=7.4, color="#555555",
    )
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(HERE / "chart-wow2-seraya-zona.png", dpi=150)
    plt.close(fig)
    print("chart_wow2_seraya_zona saved")


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
    chart_headline_gate_failure_attribution(rows)
    chart_industry_success_rate(rows)
    chart_tornado_axis_ranking(rows)
    chart_mechanism_detail(rows)
    chart_wow2_dva_mira(rows)
    chart_wow2_geroy_i_vinovnik(rows)
    chart_wow2_mertvaya_zona(rows)
    chart_wow2_zakon_starshe_ii(rows)
    chart_wow2_seraya_zona(rows)
