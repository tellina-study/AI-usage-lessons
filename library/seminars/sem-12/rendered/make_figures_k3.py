#!/usr/bin/env python3
"""Программные схемы и фотокомпозиты для Кейса 3 Семинара 12 («Чем ищем —
три задачи, которые зал считает одной»).

Инфраструктура и палитра — общий тулкит `tools/seminar-build/fig_toolkit.py`
(canon `tools/seminar-production/README.md` §7: «своё у занятия —
rendered/make_figures_*.py», тулкит один на все занятия). Эта рисовалка
обслуживает только слайды Кейса 3 (`slides/n50-n64`) — слайды других кейсов
этого же занятия (n01-n49, n65+) пишут параллельные сессии своими
рисовалками, этот файл их не трогает.

Четыре фигуры:

    case3-shema-postanovka.png       n51 — схема С1: сплошное — поток
                                       Кейса 2 (скан → вектор → косинус),
                                       пунктирная золотая стрелка — вопрос
                                       этого кейса («какой метод поиска?»).
    case3-hash-device.png            n55 — устройство перцептивного хэша:
                                       средний хэш (aHash) и pHash, сходящиеся в
                                       расстояние Хэмминга.
    case3-image-pairs.png            n56 — четыре НАСТОЯЩИЕ фотографии:
                                       оригинал / мягкий дубль / жёсткий
                                       дубль одного документа (receipt_07) +
                                       другой документ (receipt_00) без
                                       трансформации. Трансформации —
                                       буквальная копия soft_dup/hard_dup из
                                       sem-10/stend/measure/
                                       case4_full_retrieval_30.py.
    case3-odin-dokument-na-zapros.png n60 — две настоящие фотографии чеков-
                                       источников, уже лежащие в
                                       stend/zamery-k3/raw/ (замер этой же
                                       сессии), с подписями числа запросов.

Запуск (из своей папки):

    cd library/seminars/sem-12/rendered
    python3 make_figures_k3.py
"""
import io
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent               # .../sem-12/rendered
SEMINARS = HERE.parent.parent                          # .../library/seminars
CORD = SEMINARS / "sem-10" / "stend" / "corpus" / "cord_sample"
ATTR = HERE.parent / "stend" / "zamery-k3" / "raw"      # .../sem-12/stend/zamery-k3/raw


# ── n51 — схема постановки Кейса 3 (правило С1, канон
# `tools/seminar-production/forma-keysa-s-zamerom.md` §2) ───────────────────
# Сплошное — поток, уже построенный Кейсом 2 этого же занятия: скан →
# вектор (эмбеддинг) → косинус-сравнение. Пунктирная золотая стрелка и
# золотой контур — узел, который строит именно Кейс 3: какой метод поиска
# вообще отвечает на какой из трёх вопросов Ольги. Имён конкретных моделей
# внутри узлов нет умышленно — это слой архитектуры, не экран вызова (тот —
# в плашках n53/n58, текстом, не схемой).
SCENE_W_PX = 1700


def case3_shema_postanovka():
    im = Image.new("RGB", (SCENE_W_PX, 560), W)
    d = ImageDraw.Draw(im)
    head(d, "Где в поиске по архиву встаёт выбор метода", sz=30)
    d.text((40, 64),
            "скан, вектор и косинус-сравнение уже работают (Кейс 2) — вопрос в том, "
            "какой метод поиска вообще вызывается на конкретный запрос",
            font=f(21), fill=LIGHT)

    y1, h1 = 150, 150
    nodes = [
        ("Скан документа", "архив Ольги"),
        ("Вектор (эмбеддинг)", "готово — Кейс 2"),
        ("Косинус-сравнение", "готово — Кейс 2"),
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
    center_x = xs[2] + node_w / 2
    goal_x = min(center_x - goal_w / 2, SCENE_W_PX - 40 - goal_w)
    box(d, goal_x, y2, goal_w, h2,
        ["Строим сегодня:", "какой метод отвечает на какой вопрос Ольги"],
        W, tc=DEEP, sz=19, outline=GOLD, where="сцена-цель")
    arrow(d, center_x, y2, center_x, y1 + h1,
          col=GOLD, wd=4, dash=True)

    save(im, "case3-shema-postanovka.png")


# ── n55 — устройство перцептивного хэша ─────────────────────────────────────
# Две параллельные ветки (средний хэш (aHash) / pHash), каждая — цепочка шагов,
# сходящаяся в общий узел расстояния Хэмминга. Числа и порядок шагов — по
# первоисточникам (Krawetz 2011, Zauner 2010), см. backup n55.
HASH_W, HASH_H = 1700, 760


def case3_hash_device():
    im = Image.new("RGB", (HASH_W, HASH_H), W)
    d = ImageDraw.Draw(im)
    head(d, "Устройство перцептивного хэша: две ветки, одно сравнение", sz=28)

    top_w, top_h = 320, 100
    top_x = HASH_W / 2 - top_w / 2
    top_y = 70
    box(d, top_x, top_y, top_w, top_h, ["Картинка"], SURF, tc=DEEP, sz=24,
        outline=TEAL, where="картинка")

    col_w = 680
    gap = 60
    x_left = HASH_W / 2 - gap / 2 - col_w
    x_right = HASH_W / 2 + gap / 2

    steps_avg = [
        "8×8 точек, градации серого",
        "Среднее значение яркости 64 точек",
        "Бит 1/0 по порогу среднего",
    ]
    steps_phash = [
        "32×32 → DCT (пространственные частоты)",
        "Верхний левый угол 8×8 (низкие частоты)",
        "Бит 1/0 по порогу среднего (та же процедура)",
    ]

    def column(x, title, steps):
        y = 230
        h = 80
        gapy = 36
        clabel(d, x + col_w / 2, 200, title, 22, DEEP, b=True,
               where=f"заголовок колонки «{title}»", limit=col_w - 20)
        cy_prev = None
        for i, s in enumerate(steps):
            box(d, x, y, col_w, h, [s], SURF, tc=DEEP, sz=17,
                outline=LIGHT, where=f"{title} · шаг {i + 1}", pad=24)
            cy = y + h / 2
            if cy_prev is not None:
                arrow(d, x + col_w / 2, y - gapy, x + col_w / 2, y, col=LIGHT, wd=3)
            cy_prev = cy
            y += h + gapy
        return y - gapy  # y нижнего края последнего бокса

    bottom_avg = column(x_left, "средний хэш (aHash)", steps_avg)
    bottom_phash = column(x_right, "pHash", steps_phash)

    # Стрелки заканчиваются НАД заголовком колонки (y=193), не на верхней
    # кромке первого бокса (y=230): линия до бокса проходила сквозь текст
    # заголовка — с подписью «средний хэш (aHash)» перечёркивала «(aHash)».
    arrow(d, top_x + top_w * 0.25, top_y + top_h, x_left + col_w / 2, 193,
          col=TEAL, wd=3)
    arrow(d, top_x + top_w * 0.75, top_y + top_h, x_right + col_w / 2, 193,
          col=TEAL, wd=3)

    merge_w, merge_h = 560, 110
    merge_x = HASH_W / 2 - merge_w / 2
    merge_y = bottom_avg + 30
    box(d, merge_x, merge_y, merge_w, merge_h,
        ["64 бита = хэш", "сравнение — расстояние Хэмминга"],
        W, tc=DEEP, sz=21, outline=GOLD, where="узел слияния")
    arrow(d, x_left + col_w / 2, bottom_avg, merge_x + merge_w * 0.3, merge_y,
          col=GOLD, wd=3)
    arrow(d, x_right + col_w / 2, bottom_phash, merge_x + merge_w * 0.7, merge_y,
          col=GOLD, wd=3)

    save(im, "case3-hash-device.png")


# ── n56 — четыре настоящие фотографии: оригинал / мягкий дубль / жёсткий
# дубль receipt_07 + другой документ receipt_00 без трансформации.
# Трансформации — буквальная копия soft_dup/hard_dup из
# sem-10/stend/measure/case4_full_retrieval_30.py (строки ~59-76), не
# пересчитаны заново и не приближены на глаз. ──────────────────────────────
PAIR_W, PAIR_H = 300, 450
CAP_H = 56


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


def _captioned_panel(img, caption):
    panel = Image.new("RGB", (PAIR_W, CAP_H + PAIR_H), W)
    d = ImageDraw.Draw(panel)
    d.rectangle([0, 0, PAIR_W, CAP_H], fill=MID)
    clabel(d, PAIR_W / 2, 16, caption, 15, W, b=True,
           where=f"подпись панели «{caption}»", limit=PAIR_W - 16)
    panel.paste(img.resize((PAIR_W, PAIR_H)), (0, CAP_H))
    return panel


def case3_image_pairs():
    base = Image.open(CORD / "receipt_07.jpg").convert("RGB")
    other = Image.open(CORD / "receipt_00.jpg").convert("RGB")

    original = base.resize((PAIR_W, PAIR_H))
    soft = _soft_dup(base)
    hard = _hard_dup(base)
    other_r = other.resize((PAIR_W, PAIR_H))

    panels = [
        _captioned_panel(original, "оригинал"),
        _captioned_panel(soft, "мягкий дубль — пересжатие"),
        _captioned_panel(hard, "жёсткий дубль — поворот"),
        _captioned_panel(other_r, "другой документ"),
    ]

    gap = 28
    title_h = 66
    w = sum(p.width for p in panels) + gap * (len(panels) - 1) + 80
    h = title_h + max(p.height for p in panels) + 40
    im = Image.new("RGB", (w, h), W)
    d = ImageDraw.Draw(im)
    head(d, "Один и тот же документ: оригинал, два дубля, чужой документ", sz=24)
    x = 40
    for p in panels:
        im.paste(p, (x, title_h))
        x += p.width + gap
    save(im, "case3-image-pairs.png")


# ── n60 — две настоящие фотографии чеков-источников замера «плитки против
# целого кадра» (zamery-k3), подписанные числом запросов, для которых метод
# «весь кадр» их предсказал источником. Своё явление называется описательно
# действием («один и тот же документ на любой запрос»), не термином
# рабочего файла замера (канон §8.1 — слово из README замера на видимый
# слой не выходит). ─────────────────────────────────────────────────────────
ATTR_PAIR_W, ATTR_PAIR_H = 420, 560
ATTR_CAP_H = 90


def case3_odin_dokument_na_zapros():
    r07 = Image.open(ATTR / "attractor_receipt_07.jpg").convert("RGB")
    r11 = Image.open(ATTR / "attractor_receipt_11.jpg").convert("RGB")

    def panel(img, line1, line2):
        p = Image.new("RGB", (ATTR_PAIR_W, ATTR_CAP_H + ATTR_PAIR_H), W)
        d = ImageDraw.Draw(p)
        d.rectangle([0, 0, ATTR_PAIR_W, ATTR_CAP_H], fill=MID)
        clabel(d, ATTR_PAIR_W / 2, 14, line1, 18, W, b=True,
               where=f"подпись «{line1}»", limit=ATTR_PAIR_W - 20)
        clabel(d, ATTR_PAIR_W / 2, 44, line2, 16, GOLD,
               where=f"подпись «{line2}»", limit=ATTR_PAIR_W - 20)
        p.paste(img.resize((ATTR_PAIR_W, ATTR_PAIR_H)), (0, ATTR_CAP_H))
        return p

    left = panel(r07, "чек слева", "источник для 34 из 60 запросов")
    right = panel(r11, "чек справа", "источник для 20 из 60 запросов")

    gap = 40
    title_h = 70
    w = left.width + right.width + gap + 80
    h = title_h + max(left.height, right.height) + 30
    im = Image.new("RGB", (w, h), W)
    d = ImageDraw.Draw(im)
    head(d, "Один и тот же документ — ответ почти на любой запрос", sz=26)
    im.paste(left, (40, title_h))
    im.paste(right, (40 + left.width + gap, title_h))
    save(im, "case3-odin-dokument-na-zapros.png")


if __name__ == "__main__":
    case3_shema_postanovka()
    case3_hash_device()
    case3_image_pairs()
    case3_odin_dokument_na_zapros()
    report()
