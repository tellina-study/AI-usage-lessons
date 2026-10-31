#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Программа замера плотности / изображения / типографики / цвета / ритма — issue #307.

Одна линейка для всех образцов: 13 чужих эталонов (notes/research/dizayn-metodika/etalony/)
и наши колоды (library/lectures/*, library/seminars/*). Единица измерения — «кадр»
(страница PDF == слайд PPTX == разворот растрового образца).

Три источника данных, три разных набора измеримого:
  - pdf   — PyMuPDF (fitz), текстовый слой + векторные заливки (get_drawings).
  - pptx  — python-pptx, фигуры/прогоны текста/заливки.
  - raster — только PIL по пикселям (нет текстового слоя): плотность «чернил», палитра.
           Типографика и ритм для такого образца — «не измеримо», не оценка на глаз.

Разряд «справочник форм» (плакаты-таксономии) меряется только по типографике и цвету —
плотность/изображение/ритм для него помечаются «неприменимо» по условию задания: это не
колода, которую показывают кадр за кадром, а инструмент выбора формы.

Запуск:
    python3 zamer.py --all                     # весь встроенный реестр образцов issue #307
    python3 zamer.py --all --skip-heavy         # то же, без самых тяжёлых PDF (быстрый прогон)
    python3 zamer.py --one <ключ-реестра>       # один образец из реестра
    python3 zamer.py --path X.pptx --type pptx --name "моя-колода" --razryad "наша колода"
        # разовый замер произвольного файла — так мерим будущие колоды той же линейкой

Результат на образец: notes/research/dizayn-metodika/zamer/sydoe-<имя>.json — все сырые
числа и промежуточные показатели, по которым в ZAMER.md даны агрегаты. Бинарные образцы и
JSON с сырыми числами не коммитятся (см. правило задания) — файл .json уже в .gitignore не
обязателен, но коммит явно запрещён инструкцией, поэтому он просто не добавляется в git add.
"""

import argparse
import json
import math
import os
import statistics as st
import sys
import time
from collections import Counter, defaultdict

import fitz  # PyMuPDF
import numpy as np
from PIL import Image
from pptx import Presentation
from pptx.util import Emu

# --------------------------------------------------------------------------------------
# Константы метода — зафиксированы здесь один раз, чтобы в документе ссылаться на код, а не
# пересказывать числа словами.
# --------------------------------------------------------------------------------------

GRID = 64            # сетка для расчёта доли площади (текст/изображение) — union, не сумма bbox
HEADER_FRAC = 0.05    # верхние 5% высоты кадра — колонтитул, исключается из "кегля основного текста"
FOOTER_FRAC = 0.08    # нижние 8% высоты кадра — колонтитул/сноска/номер страницы
MIN_SIZE_SHARE = 0.01  # кегль-ступень должна покрывать ≥1% взвешенного объёма текста, иначе шум
TITLE_ONLY_MAX_WORDS = 12       # «кроме заголовка нет ничего»: порог слов на кадре
TITLE_ONLY_MAX_AREA = 0.05      # и порог доли площади текста на кадре
DIVIDER_MAX_WORDS = 20          # «страница-разделитель»: мало текста
DIVIDER_FONT_RATIO = 1.4        # и есть кегль крупнее медианного кегля кадра минимум в 1.4 раза
IMAGE_DOMINANT_FRAC = 0.40      # «изображение занимает больше 40% площади листа»
RASTER_QUANTIZE_COLORS = 12     # на сколько цветов квантуем растровые образцы для палитры

HERE = os.path.dirname(os.path.abspath(__file__))
ETALONY = os.path.normpath(os.path.join(HERE, "..", "etalony"))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
OUT_DIR = HERE


# --------------------------------------------------------------------------------------
# Реестр образцов issue #307. "heavy" — только маркер для --skip-heavy, не влияет на метод.
# --------------------------------------------------------------------------------------

REGISTRY = {
    # --- справочники форм (типографика + цвет только) ---
    "ft-visual-vocabulary": dict(
        path=f"{ETALONY}/ft-visual-vocabulary/visual-vocabulary-en.pdf", type="pdf",
        razryad="справочник форм", heavy=False),
    "extreme-chart-chooser": dict(
        path=f"{ETALONY}/extreme-chart-chooser/chart-chooser-2020.pdf", type="pdf",
        razryad="справочник форм", heavy=False),
    "extreme-slide-chooser": dict(
        path=f"{ETALONY}/extreme-slide-chooser/slide-chooser-11x17.pdf", type="pdf",
        razryad="справочник форм", heavy=False),
    "lengler-periodic-table": dict(
        path=f"{ETALONY}/lengler-periodic-table/periodic_table.pdf", type="pdf",
        razryad="справочник форм", heavy=False),
    # --- эталон плотности ---
    "meeker-internet-trends": dict(
        path=f"{ETALONY}/meeker-internet-trends/internet-trends-2019.pdf", type="pdf",
        razryad="эталон плотности", heavy=True),
    "chen-a16z-growth-deck": dict(
        path=f"{ETALONY}/chen-a16z-growth-deck/a16z_growth_deck.pdf", type="pdf",
        razryad="эталон плотности", heavy=False),
    # --- нижняя граница ---
    "slidescarnival-westmoreland": dict(
        path=f"{ETALONY}/slidescarnival-westmoreland/westmoreland-template.pptx", type="pptx",
        razryad="нижняя граница", heavy=False),
    "wef-global-risks-2026": dict(
        path=f"{ETALONY}/wef-global-risks-2026/WEF_Global_Risks_Report_2026.pdf", type="pdf",
        razryad="нижняя граница", heavy=True),
    # --- планка подачи ---
    "porsche-annual-report-2024": dict(
        path=f"{ETALONY}/porsche-annual-report-2024/PSE2024_Annual_Report_en.pdf", type="pdf",
        razryad="планка подачи", heavy=True),
    "abbott-annual-report-2024": dict(
        path=f"{ETALONY}/abbott-annual-report-2024/abbott-ars-2024.pdf", type="pdf",
        razryad="планка подачи", heavy=True),
    "apple-environmental-report-2026": dict(
        path=f"{ETALONY}/apple-environmental-report-2026/Apple_Environmental_Progress_Report_2026.pdf",
        type="pdf", razryad="планка подачи", heavy=True),
    "feltron-annual-report-2009": dict(
        path=f"{ETALONY}/feltron-annual-report-2009", type="raster",
        razryad="планка подачи", heavy=False),
    "moscovita-studio-pitch-deck": dict(
        path=f"{ETALONY}/moscovita-studio-pitch-deck", type="raster",
        razryad="планка подачи", heavy=False),
    # --- наши колоды ---
    "nasha-lec-07": dict(
        path=f"{REPO_ROOT}/library/lectures/lec-07/rendered/lec-07.pptx", type="pptx",
        razryad="наша колода", heavy=False),
    "nasha-lec-06": dict(
        path=f"{REPO_ROOT}/library/lectures/lec-06/rendered/lec-06.pptx", type="pptx",
        razryad="наша колода", heavy=False),
    "nasha-sem-08": dict(
        path=f"{REPO_ROOT}/library/seminars/sem-08/rendered/sem-08.pptx", type="pptx",
        razryad="наша колода", heavy=False),
}


# --------------------------------------------------------------------------------------
# Общие геометрические утилиты
# --------------------------------------------------------------------------------------

def coverage_fraction(bboxes, page_w, page_h, grid=GRID):
    """Доля площади кадра, покрытая объединением bbox (без двойного счёта перекрытий)."""
    if page_w <= 0 or page_h <= 0:
        return 0.0
    mask = np.zeros((grid, grid), dtype=bool)
    for (x0, y0, x1, y1) in bboxes:
        x0, x1 = max(0, x0), min(page_w, x1)
        y0, y1 = max(0, y0), min(page_h, y1)
        if x1 <= x0 or y1 <= y0:
            continue
        gx0 = max(0, int(x0 / page_w * grid))
        gx1 = min(grid, int(math.ceil(x1 / page_w * grid)))
        gy0 = max(0, int(y0 / page_h * grid))
        gy1 = min(grid, int(math.ceil(y1 / page_h * grid)))
        mask[gy0:gy1, gx0:gx1] = True
    return float(mask.mean())


def layout_signature(text_bboxes, image_bboxes, page_w, page_h, cells=3):
    """Булев вектор occupancy по сетке cells×cells отдельно для текста и изображений —
    признак для кластеризации раскладок (видит И долю, И положение)."""
    sig = []
    for bboxes in (text_bboxes, image_bboxes):
        occ = [[False] * cells for _ in range(cells)]
        for (x0, y0, x1, y1) in bboxes:
            cx0 = min(cells - 1, max(0, int(((x0 + x1) / 2) / page_w * cells)))
            cy0 = min(cells - 1, max(0, int(((y0 + y1) / 2) / page_h * cells)))
            occ[cy0][cx0] = True
        sig.extend(1 if v else 0 for row in occ for v in row)
    return sig


def rgb_to_hex(r, g, b, quant=4):
    """Квантование до кратного `quant`, чтобы слить цвета, различающиеся на анти-алиасинг."""
    q = lambda v: int(round(v / quant) * quant)
    return "#%02x%02x%02x" % (min(255, q(r)), min(255, q(g)), min(255, q(b)))


def accent_score(rgb, min_val=0.08, white_val=0.92, white_sat=0.08):
    """«Яркость цвета-акцента» = насыщенность×значение (HSV), не площадь — иначе крупная
    тёмная фоновая плашка обгоняет настоящий яркий акцент просто своим размером. Возвращает
    None для почти-чёрного и почти-белого (не кандидат в «акцент» вовсе)."""
    r, g, b = [v / 255.0 for v in rgb]
    mx, mn = max(r, g, b), min(r, g, b)
    val = mx
    sat = 0 if mx == 0 else (mx - mn) / mx
    if val <= min_val:
        return None
    if val >= white_val and sat <= white_sat:
        return None
    return sat * val


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def weighted_median(counter):
    """Медианный кегль основного текста, взвешенный по числу символов — без разворачивания
    Counter в список (документы в сотни страниц дают миллионы символов)."""
    if not counter:
        return None
    items = sorted(counter.items())
    total = sum(w for _, w in items)
    half = total / 2.0
    cum = 0.0
    for size, w in items:
        cum += w
        if cum >= half:
            return size
    return items[-1][0]


# --------------------------------------------------------------------------------------
# Разбор одного кадра — общая структура для pdf и pptx
# --------------------------------------------------------------------------------------

class Frame:
    __slots__ = (
        "idx", "w", "h", "word_count", "text_bboxes", "image_bboxes",
        "font_sizes_weighted", "body_font_sizes_weighted", "font_names", "text_colors",
        "fill_colors_area", "n_text_blocks", "n_images",
    )

    def __init__(self, idx, w, h):
        self.idx = idx
        self.w = w
        self.h = h
        self.word_count = 0
        self.text_bboxes = []
        self.image_bboxes = []
        self.font_sizes_weighted = Counter()        # {size_rounded_0.5: char_weight} — ВСЕ span'ы
        self.body_font_sizes_weighted = Counter()   # то же, но без колонтитула/номеров страниц —
                                                     # именно этот пул идёт в min-кегль и ступени
        self.font_names = set()
        self.text_colors = set()
        self.fill_colors_area = Counter()      # {hex: area_pt2}
        self.n_text_blocks = 0
        self.n_images = 0

    # производные показатели, используемые и для агрегатов, и для кластеризации ритма
    def text_area_frac(self):
        return coverage_fraction(self.text_bboxes, self.w, self.h)

    def image_area_frac(self):
        return coverage_fraction(self.image_bboxes, self.w, self.h)

    def max_font(self):
        return max(self.font_sizes_weighted) if self.font_sizes_weighted else None

    def median_font(self):
        if not self.font_sizes_weighted:
            return None
        pool = []
        for size, weight in self.font_sizes_weighted.items():
            pool.extend([size] * max(1, int(weight)))
        return st.median(pool)

    def is_title_only(self):
        return self.word_count <= TITLE_ONLY_MAX_WORDS and self.text_area_frac() <= TITLE_ONLY_MAX_AREA

    def is_divider(self):
        if self.word_count > DIVIDER_MAX_WORDS:
            return False
        med = self.median_font()
        mx = self.max_font()
        if med is None or mx is None or med <= 0:
            return False
        return mx >= med * DIVIDER_FONT_RATIO

    def dominant_image(self):
        return self.image_area_frac() >= IMAGE_DOMINANT_FRAC

    def layout_sig(self):
        return layout_signature(self.text_bboxes, self.image_bboxes, self.w, self.h)


# --------------------------------------------------------------------------------------
# PDF — PyMuPDF
# --------------------------------------------------------------------------------------

def is_footer_zone(bbox, h):
    y0, y1 = bbox[1], bbox[3]
    return y1 <= h * HEADER_FRAC or y0 >= h * (1 - FOOTER_FRAC)


def parse_pdf(path, log=print):
    doc = fitz.open(path)
    frames = []
    t0 = time.time()
    for i, page in enumerate(doc):
        w, h = page.rect.width, page.rect.height
        fr = Frame(i, w, h)
        d = page.get_text("dict")
        for block in d.get("blocks", []):
            btype = block.get("type", 0)
            bbox = block.get("bbox", (0, 0, 0, 0))
            if btype == 1:  # растровое изображение
                fr.image_bboxes.append(bbox)
                fr.n_images += 1
                continue
            # текстовый блок
            has_text = False
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span.get("text", "")
                    stripped = text.strip()
                    if not stripped:
                        continue
                    has_text = True
                    nchars = len(stripped)
                    size = round(span.get("size", 0) * 2) / 2.0
                    fr.font_sizes_weighted[size] += nchars
                    font_name = span.get("font", "?")
                    color_int = span.get("color", 0)
                    r, g, b = (color_int >> 16) & 255, (color_int >> 8) & 255, color_int & 255
                    fr.text_colors.add(rgb_to_hex(r, g, b))
                    # основной текст: не колонтитул/сноска и не "только цифры" номера страницы
                    sbbox = span.get("bbox", bbox)
                    is_page_num = stripped.isdigit() and len(stripped) <= 3
                    if not is_footer_zone(sbbox, h) and not is_page_num:
                        fr.font_names.add(font_name)
                        fr.body_font_sizes_weighted[size] += nchars
            if has_text:
                fr.text_bboxes.append(bbox)
                fr.n_text_blocks += 1
        # счёт слов — через get_text("words"), независимо от span-разбивки выше
        words = page.get_text("words")
        fr.word_count = len(words)
        # заливки векторных фигур — через get_drawings
        try:
            drawings = page.get_drawings()
        except Exception:
            drawings = []
        for dr in drawings:
            fill = dr.get("fill")
            rect = dr.get("rect")
            if fill is None or rect is None:
                continue
            r, g, b = [int(round(c * 255)) for c in fill]
            area = max(0.0, rect.width) * max(0.0, rect.height)
            if area <= 0:
                continue
            fr.fill_colors_area[rgb_to_hex(r, g, b)] += area
        frames.append(fr)
        if (i + 1) % 50 == 0:
            log(f"    ...{i+1}/{len(doc)} страниц, {time.time()-t0:.0f}с")
    doc.close()
    return frames


# --------------------------------------------------------------------------------------
# PPTX — python-pptx
# --------------------------------------------------------------------------------------

def emu_to_pt(v):
    return float(v) / 12700.0


def walk_shapes(shapes):
    for shp in shapes:
        yield shp
        if shp.shape_type is not None and hasattr(shp, "shapes"):
            try:
                for sub in walk_shapes(shp.shapes):
                    yield sub
            except Exception:
                pass


def parse_pptx(path, log=print):
    prs = Presentation(path)
    sw, sh = emu_to_pt(prs.slide_width), emu_to_pt(prs.slide_height)
    frames = []
    for i, slide in enumerate(prs.slides):
        fr = Frame(i, sw, sh)
        for shp in walk_shapes(slide.shapes):
            try:
                left, top = emu_to_pt(shp.left), emu_to_pt(shp.top)
                width, height = emu_to_pt(shp.width), emu_to_pt(shp.height)
            except (TypeError, ValueError):
                continue
            bbox = (left, top, left + width, top + height)
            is_picture = int(shp.shape_type) == 13 if shp.shape_type is not None else False
            if is_picture:
                fr.image_bboxes.append(bbox)
                fr.n_images += 1
                continue
            # заливка фигуры (если задана прямым RGB)
            try:
                if shp.fill.type is not None and shp.fill.type == 1:  # MSO_FILL.SOLID == 1
                    rgb = shp.fill.fore_color.rgb
                    area = max(0.0, width) * max(0.0, height)
                    if area > 0:
                        fr.fill_colors_area[rgb_to_hex(rgb[0], rgb[1], rgb[2])] += area
            except Exception:
                pass
            if not getattr(shp, "has_text_frame", False):
                continue
            tf = shp.text_frame
            block_has_text = False
            for para in tf.paragraphs:
                for run in para.runs:
                    text = run.text or ""
                    stripped = text.strip()
                    if not stripped:
                        continue
                    block_has_text = True
                    nchars = len(stripped)
                    size_pt = None
                    try:
                        if run.font.size is not None:
                            size_pt = run.font.size.pt
                    except Exception:
                        size_pt = None
                    if size_pt is not None:
                        size = round(size_pt * 2) / 2.0
                        fr.font_sizes_weighted[size] += nchars
                        if not is_footer_zone(bbox, sh):
                            fr.body_font_sizes_weighted[size] += nchars
                    font_name = run.font.name or "(унаследован)"
                    if not is_footer_zone(bbox, sh):
                        fr.font_names.add(font_name)
                    try:
                        color = run.font.color
                        if color is not None and color.type is not None and color.rgb is not None:
                            rgb = color.rgb
                            fr.text_colors.add(rgb_to_hex(rgb[0], rgb[1], rgb[2]))
                    except Exception:
                        pass
            if block_has_text:
                fr.text_bboxes.append(bbox)
                fr.n_text_blocks += 1
                fr.word_count += len([w for w in tf.text.split() if w.strip()])
        frames.append(fr)
    return frames


# --------------------------------------------------------------------------------------
# Растровые образцы — только пиксели
# --------------------------------------------------------------------------------------

def parse_raster(dir_path, log=print):
    files = sorted(
        f for f in os.listdir(dir_path)
        if f.lower().endswith((".webp", ".jpg", ".jpeg", ".png"))
    )
    results = []
    for fn in files:
        img = Image.open(os.path.join(dir_path, fn)).convert("RGB")
        w, h = img.size
        arr = np.asarray(img).astype(np.float32)
        # "доля чернил" — доля пикселей заметно темнее фона; фон = медианный пиксель.
        gray = arr.mean(axis=2)
        bg = np.median(gray)
        ink_mask = np.abs(gray - bg) > 18  # эмпирический порог контраста, не точный текст
        ink_frac = float(ink_mask.mean())
        # палитра — медианное отсечение (PIL quantize), без внешней зависимости (sklearn нет)
        small = img.resize((min(w, 300), min(h, 300)))
        quant = small.quantize(colors=RASTER_QUANTIZE_COLORS, method=Image.MEDIANCUT)
        palette = quant.getpalette()
        counts = quant.getcolors()  # [(count, index), ...]
        total = sum(c for c, _ in counts)
        colors = []
        for cnt, idx in sorted(counts, key=lambda x: -x[0]):
            r, g, b = palette[idx * 3:idx * 3 + 3]
            colors.append({"hex": rgb_to_hex(r, g, b, quant=1), "share": cnt / total})
        scored = [(c, accent_score(hex_to_rgb(c["hex"]))) for c in colors]
        scored = [(c, s) for c, s in scored if s is not None]
        scored.sort(key=lambda cs: -cs[1])
        best = scored[0][0] if scored else None
        results.append({
            "file": fn, "w": w, "h": h, "ink_frac": ink_frac,
            "palette": colors, "accent_share": (best["share"] if best else 0.0),
            "accent_hex": (best["hex"] if best else None),
        })
    return results


# --------------------------------------------------------------------------------------
# Кластеризация ритма (раздел 5) — без sklearn: scipy.cluster.hierarchy
# --------------------------------------------------------------------------------------

def cluster_layouts(frames):
    from scipy.cluster.hierarchy import linkage, fcluster
    from scipy.spatial.distance import pdist

    feats = []
    for fr in frames:
        sig = fr.layout_sig()  # 18 бит occupancy (текст×9 + изображение×9)
        feats.append(sig + [
            fr.n_text_blocks / 10.0,         # масштабировано, чтобы не доминировать над битами
            fr.n_images / 5.0,
            fr.text_area_frac(),
            fr.image_area_frac(),
        ])
    X = np.array(feats, dtype=float)
    if len(X) < 2:
        return [0] * len(X), 0
    # нормировка по столбцам, чтобы бинарные и непрерывные признаки были сравнимы
    std = X.std(axis=0)
    std[std == 0] = 1.0
    Xn = (X - X.mean(axis=0)) / std
    dist = pdist(Xn, metric="euclidean")
    Z = linkage(dist, method="average")
    # порог отсечения кластеров — эвристика: 1.2 × средняя попарная дистанция нормированных
    # признаков; документирован как эвристика, не как обоснованный статистический критерий.
    t = float(np.mean(dist)) * 0.6
    labels = fcluster(Z, t=t, criterion="distance")
    return labels.tolist(), len(set(labels.tolist()))


def runs_of(labels):
    if not labels:
        return []
    runs = []
    cur = labels[0]
    length = 1
    for lb in labels[1:]:
        if lb == cur:
            length += 1
        else:
            runs.append(length)
            cur = lb
            length = 1
    runs.append(length)
    return runs


# --------------------------------------------------------------------------------------
# Сводка по образцу
# --------------------------------------------------------------------------------------

def summarize_pdf_or_pptx(name, razryad, frames, is_reference_poster):
    n = len(frames)
    out = {"name": name, "razryad": razryad, "n_frames": n, "unit": "кадр (страница/слайд)"}

    # --- 3. типографика (всегда считаем, даже для справочников форм) ---
    # Ступени и min-кегль считаются ТОЛЬКО по body_font_sizes_weighted (колонтитул/номера
    # страниц уже отфильтрованы при разборе) — иначе "мы исключаем колонтитул" было бы
    # неправдой: раньше min считался по отфильтрованному пулу, а ступени/отношения — по
    # нефильтрованному, и редкий шумовой span (напр. подстрочный индекс внутри диаграммы,
    # «O2» на apple-environmental-report-2026 стр. 102) искажал нижнюю границу кегля.
    all_sizes = Counter()
    all_names = set()
    for fr in frames:
        all_sizes.update(fr.body_font_sizes_weighted)
        all_names.update(fr.font_names)
    total_weight = sum(all_sizes.values()) or 1
    steps = sorted(s for s, w in all_sizes.items() if w / total_weight >= MIN_SIZE_SHARE)
    ratios = [round(steps[i + 1] / steps[i], 3) for i in range(len(steps) - 1)] if len(steps) > 1 else []
    # помимо "очищенного" min (после фильтра ≥1% веса) даём и абсолютный минимум — честно,
    # как выброс, с пометкой его взвешенной доли, чтобы не прятать хвост распределения.
    raw_min = min(all_sizes) if all_sizes else None
    raw_min_share = round(all_sizes.get(raw_min, 0) / total_weight, 5) if raw_min is not None else None
    median_kegl = weighted_median(all_sizes)
    out["tipografika"] = {
        "min_kegl_osnovnogo_teksta": (steps[0] if steps else None),
        "median_kegl_osnovnogo_teksta": median_kegl,
        "min_kegl_bez_filtra_shuma": raw_min,
        "dolya_simvolov_na_etom_minimalnom_kegle": raw_min_share,
        "n_stupeney_keglya": len(steps),
        "stupeni_pt": steps,
        "otnosheniya_sosednih_stupeney": ratios,
        "n_garnitur_nachertaniy": len(all_names),
        "garnitury": sorted(all_names)[:20],
        "kak_otdelili_kolontitul": f"верхние {int(HEADER_FRAC*100)}% и нижние {int(FOOTER_FRAC*100)}% "
                                     f"высоты кадра исключены из расчёта кегля/гарнитур основного "
                                     f"текста; отдельно исключены span'ы из одних цифр длиной ≤3 "
                                     f"символов (номера страниц)",
    }

    # --- 4. цвет ---
    text_colors = set()
    fill_area = Counter()
    for fr in frames:
        text_colors.update(fr.text_colors)
        for hexc, area in fr.fill_colors_area.items():
            fill_area[hexc] += area
    total_fill_area = sum(fill_area.values())
    scored_fill = [(h, a, accent_score(hex_to_rgb(h))) for h, a in fill_area.items()]
    scored_fill = [(h, a, s) for h, a, s in scored_fill if s is not None]
    scored_fill.sort(key=lambda x: -x[2])
    accent = scored_fill[0] if scored_fill else None
    out["tsvet"] = {
        "n_unikalnyh_tsvetov_teksta": len(text_colors),
        "n_unikalnyh_tsvetov_zalivok": len(fill_area),
        "samyy_yarkiy_akcent": (accent[0] if accent else None),
        "dolya_ploshchadi_pod_akcentom": (round(accent[1] / total_fill_area, 4)
                                           if accent and total_fill_area else None),
        "kak_merili": "цвет текста — span.color (PDF) / run.font.color.rgb (PPTX), квантован "
                       "кратно 4 на канал; «самый яркий акцент» выбран по насыщенность×"
                       "значение (HSV) среди различимых заливок, НЕ по площади — так крупная "
                       "тёмная фоновая плашка не обгоняет настоящий яркий акцент своим "
                       "размером; площадь акцента — сумма площадей заливок именно ЭТОГО цвета "
                       "самого насыщенного неахроматичного цвета, делённая на сумму площадей "
                       "ВСЕХ учтённых заливок (не площадь кадра — заливки часто не покрывают "
                       "кадр целиком, поэтому это доля \"внутри учтённых плашек\", а не кадра)",
    }

    if is_reference_poster:
        out["plotnost"] = "неприменимо — справочник форм, не колода для показа"
        out["izobrazhenie"] = "неприменимо — справочник форм, не колода для показа"
        out["ritm"] = "неприменимо — справочник форм, не колода для показа"
        return out

    # --- 1. плотность ---
    words = [fr.word_count for fr in frames]
    areas = [fr.text_area_frac() for fr in frames]
    title_only = sum(1 for fr in frames if fr.is_title_only())
    out["plotnost"] = {
        "slov_na_kadr_mediana": st.median(words),
        "slov_na_kadr_p90": (np.percentile(words, 90) if words else None),
        "slov_na_kadr_max": max(words) if words else None,
        "dolya_ploshchadi_pod_tekstom_mediana": round(st.median(areas), 4),
        "dolya_ploshchadi_pod_tekstom_p90": round(float(np.percentile(areas, 90)), 4),
        "dolya_ploshchadi_pod_tekstom_max": round(max(areas), 4) if areas else None,
        "dolya_kadrov_tolko_zagolovok": round(title_only / n, 4) if n else None,
        "kak_merili": f"слова — page.get_text('words')/текст прогонов; площадь текста — доля "
                       f"сетки {GRID}×{GRID}, покрытая объединением bbox текстовых блоков (не "
                       f"сумма bbox — так не дублируется перекрытие); «только заголовок» — "
                       f"слов ≤{TITLE_ONLY_MAX_WORDS} и площадь текста ≤{TITLE_ONLY_MAX_AREA}",
    }

    # --- 2. изображение ---
    img_counts = [fr.n_images for fr in frames]
    dominant = sum(1 for fr in frames if fr.dominant_image())
    zero_img = sum(1 for fr in frames if fr.n_images == 0)
    out["izobrazhenie"] = {
        "dolya_kadrov_s_krupnym_izobrazheniem": round(dominant / n, 4) if n else None,
        "dolya_kadrov_bez_izobrazheniy": round(zero_img / n, 4) if n else None,
        "srednee_chislo_izobrazheniy_na_kadr": round(st.mean(img_counts), 3) if img_counts else None,
        "kak_merili": f"изображение — растровый блок (PDF: block type==1 из get_text('dict'); "
                       f"PPTX: shape_type==PICTURE); «крупное» — доля площади кадра "
                       f"≥{IMAGE_DOMINANT_FRAC} по той же сетке {GRID}×{GRID}",
    }

    # --- 5. разнообразие и ритм ---
    labels, n_clusters = cluster_layouts(frames)
    runs = runs_of(labels)
    dividers = sum(1 for fr in frames if fr.is_divider())
    out["ritm"] = {
        "n_raznyh_raskladok": n_clusters,
        "dliny_seriy_odinakovyh_podryad_max": max(runs) if runs else None,
        "dliny_seriy_odinakovyh_podryad_mediana": st.median(runs) if runs else None,
        "dliny_seriy_odinakovyh_podryad_raspredelenie": sorted(Counter(runs).items()),
        "dolya_stranits_razdeliteley": round(dividers / n, 4) if n else None,
        "kak_merili": f"кластеризация иерархическая (scipy.cluster.hierarchy, average-linkage) "
                       f"по вектору: occupancy текста и изображений по сетке 3×3 (18 бит) + "
                       f"число текстовых блоков + число изображений + доля площади текста/"
                       f"изображения; порог отсечения — эвристика 0.6×средней попарной "
                       f"дистанции нормированных признаков, НЕ статистический критерий — "
                       f"число раскладок зависит от порога, трактовать как порядок величины; "
                       f"разделитель — слов ≤{DIVIDER_MAX_WORDS} и есть кегль ≥"
                       f"{DIVIDER_FONT_RATIO}× медианного кегля кадра",
    }
    return out


def summarize_raster(name, razryad, pages):
    n = len(pages)
    ink = [p["ink_frac"] for p in pages]
    # агрегированная палитра: взвешенная по share и по числу страниц сумма
    agg = Counter()
    for p in pages:
        for c in p["palette"]:
            agg[c["hex"]] += c["share"]
    for k in agg:
        agg[k] /= n
    top_palette = sorted(agg.items(), key=lambda x: -x[1])[:RASTER_QUANTIZE_COLORS]
    accents = [p for p in pages if p["accent_hex"]]
    return {
        "name": name, "razryad": razryad, "n_frames": n, "unit": "кадр (растровый разворот)",
        "plotnost": "не измеримо текстом — нет текстового слоя; дана доля «чернил» "
                     "(контрастных пикселей к фону) как иная величина, НЕ доля текста",
        "chernila": {
            "dolya_mediana": round(st.median(ink), 4),
            "dolya_max": round(max(ink), 4),
            "kak_merili": "доля пикселей кадра, яркость которых отличается от медианной "
                           "яркости кадра более чем на 18/255 — грубый порог контраста, "
                           "не сегментация текста",
        },
        "izobrazhenie": "не измеримо как доля кадра — весь разворот САМ является растровым "
                          "изображением по построению (растровый источник), поэтому "
                          "«доля кадров с крупным изображением» тривиально ~1.0 и бессмысленна "
                          "для сравнения с текстовыми колодами",
        "tipografika": "не измеримо — нет текстового слоя, нет данных о кегле/гарнитуре",
        "tsvet": {
            "palitra_po_pikselyam": [{"hex": h, "share": round(s, 4)} for h, s in top_palette],
            "sredняя_dolya_samogo_yarkogo_aktsenta": round(
                st.mean([p["accent_share"] for p in accents]), 4) if accents else None,
            "kak_merili": f"квантование до {RASTER_QUANTIZE_COLORS} цветов методом median-cut "
                           f"(PIL.Image.quantize), без внешней библиотеки кластеризации "
                           f"(sklearn не установлен в среде) — честная замена по условию задания",
        },
        "ritm": "не измеримо — нет позиций текстовых/изобразительных блоков для кластеризации "
                 "раскладок, только итоговый растр",
    }


# --------------------------------------------------------------------------------------
# Главная функция одного образца
# --------------------------------------------------------------------------------------

REFERENCE_POSTERS = {"ft-visual-vocabulary", "extreme-chart-chooser", "extreme-slide-chooser",
                      "lengler-periodic-table"}


def run_one(key, spec, log=print):
    log(f"[{key}] старт, тип={spec['type']}, разряд={spec['razryad']}")
    t0 = time.time()
    path = spec["path"]
    if spec["type"] == "pdf":
        frames = parse_pdf(path, log=log)
        summary = summarize_pdf_or_pptx(key, spec["razryad"], frames,
                                         is_reference_poster=(key in REFERENCE_POSTERS))
    elif spec["type"] == "pptx":
        frames = parse_pptx(path, log=log)
        summary = summarize_pdf_or_pptx(key, spec["razryad"], frames, is_reference_poster=False)
    elif spec["type"] == "raster":
        pages = parse_raster(path, log=log)
        summary = summarize_raster(key, spec["razryad"], pages)
    else:
        raise ValueError(f"неизвестный тип {spec['type']}")
    summary["path"] = path
    summary["vremya_s"] = round(time.time() - t0, 1)
    out_path = os.path.join(OUT_DIR, f"sydoe-{key}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    log(f"[{key}] готово за {summary['vremya_s']}с -> {out_path}")
    return summary


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all", action="store_true", help="прогнать весь встроенный реестр")
    ap.add_argument("--skip-heavy", action="store_true", help="пропустить образцы с heavy=True")
    ap.add_argument("--one", metavar="KEY", help="прогнать один ключ реестра")
    ap.add_argument("--path", help="разовый замер: путь к файлу/каталогу")
    ap.add_argument("--type", choices=["pdf", "pptx", "raster"], help="тип разового образца")
    ap.add_argument("--name", help="имя разового образца (для имени выходного файла)")
    ap.add_argument("--razryad", default="без разряда", help="разряд разового образца")
    args = ap.parse_args()

    if args.path:
        if not (args.type and args.name):
            ap.error("--path требует --type и --name")
        spec = dict(path=args.path, type=args.type, razryad=args.razryad, heavy=False)
        run_one(args.name, spec)
        return

    if args.one:
        run_one(args.one, REGISTRY[args.one])
        return

    if args.all:
        for key, spec in REGISTRY.items():
            if args.skip_heavy and spec.get("heavy"):
                print(f"[{key}] пропущен (--skip-heavy)")
                continue
            try:
                run_one(key, spec)
            except Exception as e:
                print(f"[{key}] ОШИБКА: {e!r}")
        return

    ap.print_help()


if __name__ == "__main__":
    main()
