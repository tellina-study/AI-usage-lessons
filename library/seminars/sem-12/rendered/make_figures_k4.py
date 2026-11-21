#!/usr/bin/env python3
"""Программные схемы и фотокомпозиты для Кейса 4 Семинара 12 («Порог похожести — число
против вердикта»).

Инфраструктура и палитра — общий тулкит `tools/seminar-build/fig_toolkit.py` (canon
`tools/seminar-production/README.md` §7). Эта рисовалка обслуживает только слайды Кейса 4
(`slides/n65-n79`) — слайды других кейсов этого же занятия пишут параллельные сессии своими
рисовалками, этот файл их не трогает.

Пять фигур:

    case4-shema-postanovka.png   n65 — схема С1: сплошное — поток Кейса 2 (скан → вектор →
                                   косинус), пунктирная золотая стрелка — узел этого кейса
                                   («число → вердикт»).
    case4-image-pairs.png        n66/n75 — ТРИ НАСТОЯЩИЕ фотографии: оригинал receipt_02,
                                   его hard-dup (поворот 12°+обрезка 4%, та же деформация,
                                   что видела модель) и оригинал receipt_04 — документ,
                                   с которым модель спутала дубль. Подписи — числа похожести
                                   из zamery-k4/raw/band_analysis_true_labels.json.
    case4-band-easy.png          n70 — числовая полоса, лёгкий случай: SAME и DIFF кластеры,
                                   зазор чистый.
    case4-band-hard.png          n71 — числовая полоса, трудный случай: SAME/DIFF точки,
                                   полоса неопределённости между двумя порогами подсвечена.
                                   Ключевая фигура кейса.
    case4-model-compare.png      n74 — сравнение ширины полосы на двух моделях (nemotron
                                   11,7% / SigLIP 75%) одной шкалой.

Запуск (из своей папки):

    cd library/seminars/sem-12/rendered
    python3 make_figures_k4.py
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent                  # .../sem-12/rendered
SEMINARS = HERE.parent.parent                             # .../library/seminars
CORD = SEMINARS / "sem-10" / "stend" / "corpus" / "cord_sample"
ZAM = HERE.parent / "stend" / "zamery-k4" / "raw"          # .../sem-12/stend/zamery-k4/raw

SEM10_MEASURE = SEMINARS / "sem-10" / "stend" / "measure"
sys.path.insert(0, str(SEM10_MEASURE))
_cwd0 = os.getcwd()
os.chdir(SEM10_MEASURE)
from case4_full_retrieval_30 import hard_dup  # noqa: E402
os.chdir(_cwd0)

TRUE_LABELS = json.load(open(ZAM / "band_analysis_true_labels.json", encoding="utf-8"))
SIGLIP = json.load(open(ZAM / "siglip_band_analysis.json", encoding="utf-8"))

W_PX = 1700


# ── n65 — схема постановки Кейса 4 ──────────────────────────────────────────
def case4_shema_postanovka():
    im = Image.new("RGB", (W_PX, 560), W)
    d = ImageDraw.Draw(im)
    head(d, "Где в поиске встаёт выбор: число или вердикт", sz=30)
    d.text((40, 64),
            "вектор и косинус-сравнение уже работают (Кейс 2) — вопрос в том, что делать "
            "с результатом сравнения, когда он не 0 и не 1",
            font=f(21), fill=LIGHT)

    y1, h1 = 150, 150
    nodes = [("Скан документа", "архив Ольги"), ("Вектор (эмбеддинг)", "готово — Кейс 2"),
             ("Косинус-сравнение", "число от -1 до 1, готово — Кейс 2")]
    gap = 50
    n = len(nodes)
    node_w = (W_PX - 80 - gap * (n - 1)) // n
    xs = [40 + i * (node_w + gap) for i in range(n)]
    cy1 = y1 + h1 / 2
    for i, (title, sub) in enumerate(nodes):
        box(d, xs[i], y1, node_w, h1, [title, sub], SURF, tc=DEEP, sz=21,
            outline=LIGHT, where=f"сцена-узел {i + 1}")
        if i:
            arrow(d, xs[i - 1] + node_w, cy1, xs[i], cy1, col=LIGHT, wd=4)

    y2, h2 = 370, 150
    goal_w = node_w + 70
    center_x = xs[2] + node_w / 2
    goal_x = min(center_x - goal_w / 2, W_PX - 40 - goal_w)
    box(d, goal_x, y2, goal_w, h2, ["Строим сегодня:", "число → решение «тот же / другой»"],
        W, tc=DEEP, sz=19, outline=GOLD, where="сцена-цель")
    arrow(d, center_x, y2, center_x, y1 + h1, col=GOLD, wd=4, dash=True)
    save(im, "case4-shema-postanovka.png")


# ── n66/n75 — три настоящие фотографии: оригинал, его hard-dup, и чужой документ,
# с которым модель его спутала ──────────────────────────────────────────────
def case4_image_pairs():
    orig = Image.open(CORD / "receipt_02.jpg").convert("RGB")
    dup_raw = hard_dup(str(CORD / "receipt_02.jpg"), w=300, h=450)
    import base64, io
    dup = Image.open(io.BytesIO(base64.b64decode(dup_raw.split(",", 1)[1]))).convert("RGB")
    other = Image.open(CORD / "receipt_04.jpg").convert("RGB")

    cell_w, cell_h = 480, 680
    gap = 60
    total_w = cell_w * 3 + gap * 2 + 80
    total_h = cell_h + 230
    im = Image.new("RGB", (total_w, total_h), W)
    d = ImageDraw.Draw(im)
    head(d, "Настоящий дубль, который модель спутала не со своим оригиналом", sz=27)
    d.text((40, 62),
            "поворот 12° + обрезка 4% краёв — ровно то изображение, что видела модель",
            font=f(19), fill=LIGHT)

    panels = [
        (orig, "Оригинал: чек с жасминовым чаем", "лежит в архиве"),
        (dup, "Его повёрнутый и обрезанный дубль", "похожесть на свой оригинал: не измерена,\nизвестно: меньше 0,75"),
        (other, "Совсем другой чек — кофе и курица", "похожесть на дубль слева: 0,75\n(модель назвала его «ближайшим»)"),
    ]
    y0 = 130
    for i, (pil, title, sub) in enumerate(panels):
        x0 = 40 + i * (cell_w + gap)
        thumb = pil.copy()
        thumb.thumbnail((cell_w - 20, cell_h - 20))
        tx = x0 + (cell_w - thumb.width) // 2
        ty = y0 + (cell_h - thumb.height) // 2
        d.rectangle([x0, y0, x0 + cell_w, y0 + cell_h], outline=LIGHT, width=3)
        im.paste(thumb, (tx, ty))
        d.text((x0, y0 + cell_h + 14), title, font=f(21, True), fill=DEEP)
        for j, ln in enumerate(sub.split("\n")):
            d.text((x0, y0 + cell_h + 48 + j * 26), ln, font=f(17), fill=MUTE)
        if i == 1:
            mx1, my = x0 - gap // 2, y0 + cell_h // 2
            arrow(d, mx1 - 8, my, mx1 + gap - 8, my, col=GOLD, wd=4, dash=True)

    save(im, "case4-image-pairs.png")


# ── n70 — числовая полоса, лёгкий случай ───────────────────────────────────
def _number_line(d, x0, x1, y, lo, hi, col=MUTE):
    d.line([x0, y, x1, y], fill=col, width=3)
    for v in [round(lo + (hi - lo) * k / 5, 2) for k in range(6)]:
        px = x0 + (x1 - x0) * (v - lo) / (hi - lo)
        d.line([px, y - 8, px, y + 8], fill=col, width=2)
        d.text((px - 18, y + 14), f"{v:.2f}", font=f(16), fill=MUTE)


def _dots(d, x0, x1, y, lo, hi, values, col, r=9, jitter=14):
    n = len(values)
    for i, v in enumerate(sorted(values)):
        px = x0 + (x1 - x0) * (v - lo) / (hi - lo)
        py = y - (jitter if i % 2 else -jitter) * 0.0  # оставлено для читаемого ряда
        d.ellipse([px - r, y - r, px + r, y + r], fill=col, outline=DEEP, width=2)


def case4_band_easy():
    d_true = TRUE_LABELS["easy_case"]
    same_vals = [r["cosine"] for r in TRUE_LABELS["raw_pairs"]["same_soft"]]
    diff_vals = [r["cosine"] for r in TRUE_LABELS["raw_pairs"]["diff_nearest_other"]]
    im = Image.new("RGB", (W_PX, 460), W)
    d = ImageDraw.Draw(im)
    head(d, "Лёгкий случай — пересжатие: зазор чистый", sz=28)
    d.text((40, 64), "nvidia/nemotron-3.5-embed-1b:free, 30 пар «тот же» + 30 пар «другой»",
           font=f(19), fill=LIGHT)

    x0, x1, y = 80, W_PX - 80, 260
    lo, hi = 0.45, 1.0
    _number_line(d, x0, x1, y, lo, hi)
    _dots(d, x0, x1, y - 40, lo, hi, diff_vals, LIGHT)
    _dots(d, x0, x1, y + 40, lo, hi, same_vals, GOLD)

    gx0 = x0 + (x1 - x0) * (d_true["t_high"] - lo) / (hi - lo)
    gx1 = x0 + (x1 - x0) * (d_true["t_low"] - lo) / (hi - lo)
    d.rectangle([gx0, y - 70, gx1, y + 70], outline=TEAL, width=3)
    d.text(((gx0 + gx1) / 2 - 90, y - 140), "любой порог здесь\nразделяет без ошибок",
           font=f(16), fill=TEAL)
    d.text((x0, y - 60), "другой документ", font=f(17, True), fill=LIGHT)
    d.text((x0, y + 60), "тот же документ", font=f(17, True), fill=GOLDTX)
    save(im, "case4-band-easy.png")


# ── n71 — числовая полоса, трудный случай (ключевая фигура) ────────────────
def case4_band_hard():
    d_true = TRUE_LABELS["hard_case"]
    same_vals = [r["cosine"] for r in TRUE_LABELS["raw_pairs"]["same_hard_known"]]
    diff_vals = ([r["cosine"] for r in TRUE_LABELS["raw_pairs"]["diff_nearest_other"]]
                 + [r["cosine"] for r in TRUE_LABELS["raw_pairs"]["diff_misfire"]])
    im = Image.new("RGB", (W_PX, 460), W)
    d = ImageDraw.Draw(im)
    head(d, "Трудный случай — поворот и обрезка: 7 из 60 известных пар в полосе", sz=27)
    d.text((40, 64), "nvidia/nemotron-3.5-embed-1b:free, полоса [0,7049; 0,7547]",
           font=f(19), fill=LIGHT)

    x0, x1, y = 80, W_PX - 80, 270
    lo, hi = 0.45, 1.0
    _number_line(d, x0, x1, y, lo, hi)
    _dots(d, x0, x1, y - 40, lo, hi, diff_vals, LIGHT)
    _dots(d, x0, x1, y + 40, lo, hi, same_vals, GOLD)

    bx0 = x0 + (x1 - x0) * (d_true["t_low"] - lo) / (hi - lo)
    bx1 = x0 + (x1 - x0) * (d_true["t_high"] - lo) / (hi - lo)
    d.rectangle([bx0, y - 90, bx1, y + 90], fill=None, outline=RED, width=4)
    d.text(((bx0 + bx1) / 2 - 90, y - 150), "полоса неопределённости\n7 пар, 11,7%",
           font=f(17, True), fill=RED)
    d.text((x0, y - 60), "другой документ", font=f(17, True), fill=LIGHT)
    d.text((x0, y + 60), "тот же документ", font=f(17, True), fill=GOLDTX)
    d.text((x0, y + 150), "ещё одна настоящая пара осталась не измеренной — известно "
                            "лишь, что она ниже 0,75", font=f(16), fill=MUTE)
    save(im, "case4-band-hard.png")


# ── n74 — сравнение ширины полосы на двух моделях ──────────────────────────
def case4_model_compare():
    im = Image.new("RGB", (W_PX, 520), W)
    d = ImageDraw.Draw(im)
    head(d, "Ширина полосы — своя у каждой модели", sz=28)
    d.text((40, 64), "та же пара дублей, та же деформация, трудный случай",
           font=f(19), fill=LIGHT)

    rows = [("nvidia/nemotron-3.5-embed-1b:free", 0.117, "7 из 60 пар"),
            ("google/siglip-base-patch16-224, локально", 0.75, "45 из 60 пар")]
    bx0, bw = 40, W_PX - 80
    y = 170
    for name, share, label in rows:
        d.text((bx0, y - 34), name, font=f(21, True), fill=DEEP)
        d.rectangle([bx0, y, bx0 + bw, y + 60], outline=LIGHT, width=3, fill=SURF)
        fill_w = bw * share
        col = RED if share > 0.4 else TEAL
        d.rectangle([bx0, y, bx0 + fill_w, y + 60], fill=col)
        tx = bx0 + fill_w + 20 if share < 0.6 else bx0 + 20
        tc = DEEP if share < 0.6 else W
        d.text((tx, y + 15), f"{label} ({share*100:.0f}%)", font=f(22, True), fill=tc)
        y += 150
    d.text((bx0, y + 10), "75% — не «порог труднее подобрать», а «модель не инструмент для сканов»",
           font=f(19), fill=MUTE)
    save(im, "case4-model-compare.png")


if __name__ == "__main__":
    case4_shema_postanovka()
    case4_image_pairs()
    case4_band_easy()
    case4_band_hard()
    case4_model_compare()
    report()
