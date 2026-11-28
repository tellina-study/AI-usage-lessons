#!/usr/bin/env python3
"""Программные схемы и фотокомпозиты для Кейса 2 Семинара 12 («Как картинка
становится числами, и почему у одной картинки векторов много»).

Инфраструктура и палитра — общий тулкит `tools/seminar-build/fig_toolkit.py`
(canon `tools/seminar-production/README.md` §7: «своё у занятия —
rendered/make_figures_*.py», тулкит один на все занятия), по образцу
`make_figures_k3.py` этого же занятия (слайды n50-n64) — та же рисовалка
обслуживает только слайды Кейса 2 (`slides/n25-n49`), слайды других кейсов
(n01-n24, n50+) пишут параллельные сессии своими рисовалками, этот файл их
не трогает.

Шесть фигур:

    case2-shema-postanovka.png   n28 — схема С1: сплошное — то, что уже
                                   работает после Кейса 1 (скан → описание/
                                   поля для индекса), пунктирная золотая
                                   стрелка и контур — то, что строит этот
                                   кейс: вектор картинки и проверка запасом
                                   различения.
    case2-patch-grid.png         n29 — НАСТОЯЩИЙ скан из корпуса CORD
                                   (receipt_07) с иллюстративной сеткой
                                   14×14 = 196 патчей (размер ViT-B/16 на
                                   входе 224×224, число из arXiv:2010.11929);
                                   рядом — первые 8 чисел РЕАЛЬНОГО вектора
                                   этого же скана (voyage-multimodal-3.5,
                                   1024 чисел) и формула косинуса.
    case2-two-encoders.png       n30 — схема контрастного обучения CLIP:
                                   два энкодера → проекция → L2-нормировка →
                                   матрица косинусов в батче → loss; плашка
                                   модального зазора (0,82).
    case2-svedenie-patches.png   n31 — схема «много векторов патчей → один
                                   вектор кадра» (class-токен либо
                                   усреднение) и плашка потери детали.
    case2-image-pairs.png        n37 — НАСТОЯЩИЕ фотографии: receipt_07 из
                                   корпуса CORD в трёх видах (оригинал,
                                   мягкий дубль, жёсткий дубль). Трансформации
                                   — буквальная копия soft_dup/hard_dup из
                                   sem-10/stend/measure/case4_full_retrieval_30.py
                                   (тот же приём, что уже использован в
                                   measure_jitter_case4_strength.py этой же
                                   сессии и в case3_image_pairs() Кейса 3).
                                   Подписи — реальные числа SigLIP локально
                                   из raw/jitter_case4_strength_results.json
                                   на этом же скане.
    case2-similarity-map.png     n33 — карта похожести 435 пар корпуса:
                                   иллюстративная плотность, построенная по
                                   трём сохранённым сводным числам (mean
                                   0,521, min 0,277, max 0,849) — отдельных
                                   435 чисел в sem-10/stend/raw/
                                   case4_mm_full_retrieval.json нет, только
                                   сводка; подпись на самой схеме называет
                                   это прямо, одно не выдаётся за другое.

Запуск (из своей папки):

    cd library/seminars/sem-12/rendered
    python3 make_figures_k2.py
"""
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent                # .../sem-12/rendered
SEMINARS = HERE.parent.parent                          # .../library/seminars
CORD = SEMINARS / "sem-10" / "stend" / "corpus" / "cord_sample"
RAW = HERE.parent / "stend" / "zamery-k2" / "raw"       # .../sem-12/stend/zamery-k2/raw

SCENE_W_PX = 1700


def ru_fmt(x, prec=3):
    """Форматирует число с русской десятичной запятой вместо точки.
    Нулевое значение не получает знака: «-0,000» → «0,000»."""
    s = f"{x:.{prec}f}"
    if s.lstrip("-").strip("0") in ("", "."):
        s = s.lstrip("-")
    return s.replace(".", ",")


# ── n28 — схема постановки Кейса 2 (правило С1, канон
# `tools/seminar-production/forma-keysa-s-zamerom.md` §2). Сплошное — то,
# что уже работает по итогам Кейса 1 этого же занятия: скан → описание/поля
# для текстового индекса. Пунктирная золотая стрелка и золотой контур —
# узел, который строит именно Кейс 2: вектор самой картинки и проверка,
# можно ли ему верить. Имён конкретных моделей внутри узлов нет умышленно —
# это слой архитектуры, модели и числа — на кадрах такта 1 и такта 3. ──────
def case2_shema_postanovka():
    im = Image.new("RGB", (SCENE_W_PX, 560), W)
    d = ImageDraw.Draw(im)
    head(d, "Где в архиве встаёт проверка модели эмбеддинга", sz=30)
    d.text((40, 64),
            "скан и текстовое описание для индекса уже работают (Кейс 1) — вопрос в том, "
            "можно ли верить вектору самой картинки",
            font=f(21), fill=LIGHT)

    y1, h1 = 150, 150
    nodes = [
        ("Скан документа", "архив Ольги"),
        ("Описание и поля", "готово — Кейс 1"),
    ]
    gap = 50
    n = len(nodes)
    node_w = (SCENE_W_PX - 80 - gap * (n - 1)) // n
    xs = [40 + i * (node_w + gap) for i in range(n)]
    cy1 = y1 + h1 / 2
    for i, (title, sub) in enumerate(nodes):
        box(d, xs[i], y1, node_w, h1, [title, sub], SURF, tc=DEEP, sz=21,
            outline=LIGHT, where=f"сцена-узел {i + 1}")
        if i:
            arrow(d, xs[i - 1] + node_w, cy1, xs[i], cy1, col=LIGHT, wd=4)

    y2, h2 = 370, 150
    goal_w = node_w + 70
    center_x = xs[0] + node_w / 2
    goal_x = max(40, min(center_x - goal_w / 2, SCENE_W_PX - 40 - goal_w))
    box(d, goal_x, y2, goal_w, h2,
        ["Строим сегодня:", "вектор картинки и проверка запасом различения"],
        W, tc=DEEP, sz=19, outline=GOLD, where="сцена-цель")
    arrow(d, center_x, y2, center_x, y1 + h1, col=GOLD, wd=4, dash=True)

    save(im, "case2-shema-postanovka.png")


# ── n29 — сетка патчей на настоящем скане + первые числа настоящего вектора.
# Сетка 14×14 = 196 — иллюстративная (тот же приём, что Кейс 1 принял для
# своей сетки патчей на n13: число патчей называется без утверждения о
# точном устройстве токенизатора КОНКРЕТНОЙ модели, чей вектор показан
# справа, — это разные модели/архитектуры, и подпись это не прячет). ──────
PATCH_N = 14
PATCH_PX = 24  # 14 * 24 = 336


def case2_patch_grid():
    im_w, im_h = 1700, 640
    im = Image.new("RGB", (im_w, im_h), W)
    d = ImageDraw.Draw(im)
    head(d, "Патч за патчем: картинка становится последовательностью векторов", sz=27)

    scan = Image.open(CORD / "receipt_07.jpg").convert("RGB")
    side = PATCH_N * PATCH_PX
    w, h = scan.size
    s = min(w, h)
    left, top = (w - s) // 2, (h - s) // 2
    scan_sq = scan.crop((left, top, left + s, top + s)).resize((side, side))
    gx, gy = 60, 100
    im.paste(scan_sq, (gx, gy))

    for i in range(1, PATCH_N):
        x = gx + i * PATCH_PX
        d.line([x, gy, x, gy + side], fill=GOLD, width=1)
        y = gy + i * PATCH_PX
        d.line([gx, y, gx + side, y], fill=GOLD, width=1)
    d.rectangle([gx, gy, gx + side, gy + side], outline=DEEP, width=3)
    clabel(d, im_w / 2, gy + side + 20,
           "14×14 = 196 патчей (CORD) — сетка иллюстративная",
           16, MUTE, where="подпись сетки патчей", limit=im_w - 80)
    clabel(d, im_w / 2, gy + side + 46,
           "размер ViT-B/16 при входе 224×224 (arXiv:2010.11929), не устройство модели справа",
           14, MUTE, where="подпись-уточнение сетки", limit=im_w - 80)

    vectors = json.load(open(RAW / "originals_mongodb_voyage-multimodal-3.5.json"))["vectors"]
    vec = vectors["receipt_07"]
    nums = ", ".join(ru_fmt(x) for x in vec[:8])

    px, py = gx + side + 70, gy
    pw = im_w - px - 40
    box(d, px, py, pw, 160,
        ["вектор этого скана — mongodb/voyage-multimodal-3.5",
         nums + ", …", "длина вектора — 1024 (настройка вызова, не фиксированное свойство модели)"],
        SURF, tc=DEEP, sz=16, outline=LIGHT, where="вектор-плашка")
    box(d, px, py + 200, pw, 100,
        ["косинус(a, b) = (a · b) / (|a| · |b|)"],
        W, tc=DEEP, sz=22, outline=GOLD, where="формула косинуса")

    save(im, "case2-patch-grid.png")


# ── n30 — контрастное обучение: два энкодера, общая размерность, L2-норма,
# матрица косинусов в батче, loss. Плашка модального зазора (0,82) — отдельно
# внизу, не встроена в схему как узел: это измеренное СЛЕДСТВИЕ обучения, не
# шаг вычисления. ───────────────────────────────────────────────────────────
TWO_W, TWO_H = 1700, 760


def case2_two_encoders():
    im = Image.new("RGB", (TWO_W, TWO_H), W)
    d = ImageDraw.Draw(im)
    head(d, "Два кодировщика сводятся в одно пространство обучением", sz=26)

    top_w, top_h = 320, 90
    gap_cols = 60
    col_w = 680
    x_left = TWO_W / 2 - gap_cols / 2 - col_w
    x_right = TWO_W / 2 + gap_cols / 2

    top_left_x = x_left + col_w / 2 - top_w / 2
    top_right_x = x_right + col_w / 2 - top_w / 2
    top_y = 70
    box(d, top_left_x, top_y, top_w, top_h, ["Картинка"], SURF, tc=DEEP, sz=24,
        outline=TEAL, where="вход-картинка")
    box(d, top_right_x, top_y, top_w, top_h, ["Текст"], SURF, tc=DEEP, sz=24,
        outline=TEAL, where="вход-текст")

    steps_img = [
        "Картиночный энкодер (ViT)",
        "Проекция в общую размерность",
        "L2-нормировка (длина = 1)",
    ]
    steps_txt = [
        "Текстовый энкодер (трансформер)",
        "Проекция в общую размерность",
        "L2-нормировка (длина = 1)",
    ]

    def column(x, steps):
        y = 220
        h = 90
        gapy = 36
        cy_prev = None
        for i, s in enumerate(steps):
            box(d, x, y, col_w, h, [s], SURF, tc=DEEP, sz=18,
                outline=LIGHT, where=f"энкодер · шаг {i + 1}", pad=24)
            cy = y + h / 2
            if cy_prev is not None:
                arrow(d, x + col_w / 2, y - gapy, x + col_w / 2, y, col=LIGHT, wd=3)
            cy_prev = cy
            y += h + gapy
        return y - gapy

    bottom_left = column(x_left, steps_img)
    bottom_right = column(x_right, steps_txt)

    arrow(d, top_left_x + top_w / 2, top_y + top_h, x_left + col_w / 2, 220, col=TEAL, wd=3)
    arrow(d, top_right_x + top_w / 2, top_y + top_h, x_right + col_w / 2, 220, col=TEAL, wd=3)

    merge_w, merge_h = 720, 130
    merge_x = TWO_W / 2 - merge_w / 2
    merge_y = max(bottom_left, bottom_right) + 30
    box(d, merge_x, merge_y, merge_w, merge_h,
        ["Матрица косинусов в батче", "контрастная функция потерь — 400 млн пар, батч 32 768"],
        W, tc=DEEP, sz=19, outline=GOLD, where="узел слияния")
    arrow(d, x_left + col_w / 2, bottom_left, merge_x + merge_w * 0.3, merge_y, col=GOLD, wd=3)
    arrow(d, x_right + col_w / 2, bottom_right, merge_x + merge_w * 0.7, merge_y, col=GOLD, wd=3)

    gap_y = merge_y + merge_h + 40
    box(d, TWO_W / 2 - 520, gap_y, 1040, 110,
        ["Модальный зазор (CLIP, arXiv:2203.02053): 0,82",
         "картинка и текст лежат рядом, не в одной точке единичной гиперсферы"],
        WARM, tc=GOLDINK, sz=18, outline=GOLD, where="плашка модального зазора")

    save(im, "case2-two-encoders.png")


# ── n31 — сведение множества векторов патчей в один вектор кадра: class-
# токен либо усреднение, и плашка избирательной потери детали. ────────────
# Высота 510, не 480: нижняя плашка кончается на y=490, и на холсте 480 её
# нижняя кромка срезалась краем кадра (замечено глазами при перерендере
# 2026-11-22).
SVED_W, SVED_H = 1700, 510


def case2_svedenie_patches():
    im = Image.new("RGB", (SVED_W, SVED_H), W)
    d = ImageDraw.Draw(im)
    head(d, "Много векторов патчей — один вектор кадра", sz=28)

    y, h = 140, 150
    # Коробки расширены под подпись «служебный токен (CLS) …» — сторож `fit`
    # поймал вылезание на прежних 420/520 (замер прогоном 2026-11-22).
    w1, w2, w3 = 520, 580, 420
    gap = 50
    x1 = 40
    x2 = x1 + w1 + gap
    x3 = x2 + w2 + gap
    box(d, x1, y, w1, h, ["196 векторов патчей", "(служебный токен (CLS) + 195 остальных)"], SURF,
        tc=DEEP, sz=19, outline=LIGHT, where="узел-патчи")
    box(d, x2, y, w2, h, ["Сведение:", "служебный токен ИЛИ усреднение всех патчей"], W,
        tc=DEEP, sz=19, outline=GOLD, where="узел-сведение")
    box(d, x3, y, w3, h, ["1 вектор кадра", "(весь кадр целиком)"], SURF,
        tc=DEEP, sz=19, outline=LIGHT, where="узел-результат")
    cy = y + h / 2
    arrow(d, x1 + w1, cy, x2, cy, col=LIGHT, wd=4)
    arrow(d, x2 + w2, cy, x3, cy, col=LIGHT, wd=4)

    py = y + h + 50
    box(d, 60, py, SVED_W - 120, 150,
        ["Деталь, занимающая малую долю кадра, растворяется в сведении — архитектурный выбор, не брак",
         "предсказание: «найди похожее целиком» работает; «найди, где есть вот это» — слабее на том же векторе"],
        WARM, tc=GOLDINK, sz=19, outline=GOLD, where="плашка потери детали")

    save(im, "case2-svedenie-patches.png")


# ── n37 — receipt_07 из корпуса CORD в трёх видах: оригинал, мягкий дубль,
# жёсткий дубль. Трансформации — буквальная копия soft_dup/hard_dup из
# sem-10/stend/measure/case4_full_retrieval_30.py (строки ~59-76), тот же
# приём, которым уже воспользовался measure_jitter_case4_strength.py этой же
# сессии и case3_image_pairs() Кейса 3 — не переписаны и не приближены на
# глаз. Подписи — настоящие числа SigLIP локально
# (raw/jitter_case4_strength_results.json), тот же скан. ───────────────────
PAIR_W, PAIR_H = 360, 480
CAP_H = 100


def _soft_dup(im):
    soft = im.resize((max(1, int(im.width * 0.97)), max(1, int(im.height * 0.97))))
    soft = soft.resize((PAIR_W, PAIR_H))
    buf = io.BytesIO()
    soft.save(buf, format="JPEG", quality=60)
    buf.seek(0)
    return Image.open(buf).convert("RGB")


def _hard_dup(im):
    hard = im.rotate(12, expand=True, fillcolor=(255, 255, 255))
    ww, hh = hard.size
    hard = hard.crop((int(ww * 0.04), int(hh * 0.04), int(ww * 0.96), int(hh * 0.96)))
    hard = hard.resize((PAIR_W, PAIR_H))
    buf = io.BytesIO()
    hard.save(buf, format="JPEG", quality=80)
    buf.seek(0)
    return Image.open(buf).convert("RGB")


def _captioned_panel(img, line1, line2):
    panel = Image.new("RGB", (PAIR_W, CAP_H + PAIR_H), W)
    d = ImageDraw.Draw(panel)
    d.rectangle([0, 0, PAIR_W, CAP_H], fill=MID)
    clabel(d, PAIR_W / 2, 16, line1, 17, W, b=True,
           where=f"подпись панели «{line1}»", limit=PAIR_W - 16)
    clabel(d, PAIR_W / 2, 48, line2, 13, W,
           where=f"подпись панели «{line2}»", limit=PAIR_W - 16)
    panel.paste(img.resize((PAIR_W, PAIR_H)), (0, CAP_H))
    return panel


def case2_image_pairs():
    jitter = json.load(open(RAW / "jitter_case4_strength_results.json"))
    siglip = jitter["models"]["google/siglip-base-patch16-224"]["deformations"]
    soft_rec = next(r for r in siglip["case4_soft_dup"]["details"] if r["id"] == "receipt_07")
    hard_rec = next(r for r in siglip["case4_hard_dup"]["details"] if r["id"] == "receipt_07")

    base = Image.open(CORD / "receipt_07.jpg").convert("RGB")
    original = base.resize((PAIR_W, PAIR_H))
    soft = _soft_dup(base)
    hard = _hard_dup(base)

    panels = [
        _captioned_panel(original, "оригинал", "реальный чек, корпус CORD"),
        _captioned_panel(
            soft, "мягкий дубль",
            f"SigLIP: {ru_fmt(soft_rec['cosine_to_own_original'], 2)} к себе, сосед — сам же"),
        _captioned_panel(
            hard, "жёсткий дубль",
            f"SigLIP: {ru_fmt(hard_rec['cosine_to_own_original'], 2)} к себе, сосед — "
            f"чужой чек ({ru_fmt(hard_rec['nearest_cosine'], 2)})"),
    ]

    gap = 32
    title_h = 76
    w = sum(p.width for p in panels) + gap * (len(panels) - 1) + 80
    h = title_h + max(p.height for p in panels) + 30
    im = Image.new("RGB", (w, h), W)
    d = ImageDraw.Draw(im)
    head(d, "Один и тот же документ: оригинал и два дубля того же файла", sz=24)
    x = 40
    for p in panels:
        im.paste(p, (x, title_h))
        x += p.width + gap
    save(im, "case2-image-pairs.png")


# ── n33 — карта похожести 435 пар. Отдельных 435 чисел в сохранённом сырье
# нет (sem-10/stend/raw/case4_mm_full_retrieval.json хранит только n/mean/
# min/max) — плотность ниже ПОСТРОЕНА по этим трём числам (треугольное
# распределение, пик на mean, нули на min/max), не является гистограммой по
# настоящим 435 точкам, и подпись на самой схеме называет это прямо. ───────
MAP_W, MAP_H = 1700, 640


def case2_similarity_map():
    stats = json.load(open(SEMINARS / "sem-10" / "stend" / "raw" / "case4_mm_full_retrieval.json"))[
        "pairwise_text_cosine_stats_all_435_pairs"]
    n_pairs, mean, lo, hi = stats["n_pairs"], stats["mean"], stats["min"], stats["max"]

    im = Image.new("RGB", (MAP_W, MAP_H), W)
    d = ImageDraw.Draw(im)
    head(d, "Карта похожести: 435 пар одного корпуса, узкая полоса", sz=28)

    plot_x, plot_y, plot_w, plot_h = 90, 130, MAP_W - 180, 320
    d.rectangle([plot_x, plot_y, plot_x + plot_w, plot_y + plot_h], outline=LIGHT, width=2)

    axis_lo, axis_hi = -0.1, 1.0

    def to_x(v):
        return plot_x + (v - axis_lo) / (axis_hi - axis_lo) * plot_w

    n_bins = 28
    bin_w = plot_w / n_bins
    peak_h = plot_h - 30
    for i in range(n_bins):
        v = axis_lo + (i + 0.5) * (axis_hi - axis_lo) / n_bins
        if v <= lo or v >= hi:
            height = 0
        else:
            # треугольная плотность: пик на mean, нули на границах lo/hi —
            # ПОСТРОЕНО по трём сводным числам, не по настоящим 435 точкам
            if v <= mean:
                frac = (v - lo) / (mean - lo) if mean > lo else 0
            else:
                frac = (hi - v) / (hi - mean) if hi > mean else 0
            height = max(0, frac) * peak_h
        bx = plot_x + i * bin_w
        d.rectangle([bx + 2, plot_y + plot_h - height, bx + bin_w - 2, plot_y + plot_h],
                    fill=LIGHT)

    for v, col, lbl in [(0.0, MUTE, "0"), (lo, TEAL, f"минимум {ru_fmt(lo)}"),
                        (mean, GOLD, f"среднее {ru_fmt(mean)}"),
                        (hi, TEAL, f"максимум {ru_fmt(hi)}")]:
        x = to_x(v)
        d.line([x, plot_y - 10, x, plot_y + plot_h + 10], fill=col, width=3)
        clabel(d, x, plot_y + plot_h + 16, lbl, 15, col, b=True, where=f"метка {lbl}", limit=220)

    clabel(d, MAP_W / 2, plot_y + plot_h + 60,
           f"n = {n_pairs} пар, корпус CORD (измерено на Семинаре 10)", 17, DEEP,
           where="подпись n", limit=plot_w)
    clabel(d, MAP_W / 2, plot_y + plot_h + 88,
           "плотность — иллюстрация по трём сводным числам (среднее/минимум/максимум); 435 отдельных значений не сохранены",
           14, MUTE, where="честная оговорка о построении схемы", limit=plot_w)

    save(im, "case2-similarity-map.png")


if __name__ == "__main__":
    case2_shema_postanovka()
    case2_patch_grid()
    case2_two_encoders()
    case2_svedenie_patches()
    case2_image_pairs()
    case2_similarity_map()
    report()
