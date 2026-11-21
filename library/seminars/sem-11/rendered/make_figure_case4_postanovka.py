#!/usr/bin/env python3
"""Семинар 11, Кейс 4 — схема постановки (правило С1, `forma-keysa-s-zamerom.md` §2):
сплошным рядом — то, что уже работает с рецепта Семинара 10 (вопрос студента курса ->
поиск по смыслу в базе СВОЕГО курса -> ответ); пунктирная золотая рамка и стрелка — не
новый узел (этот кейс не вставляет блок в цепочку, как Кейс 1/2) и не параметр внутри
узла (как вес 0,5/0,5 Кейса 3), а сама БАЗА, в которую идёт второй узел: версия 1 этого
кейса заменяет «базу своего курса» на «один общий индекс всех курсов центра», не трогая
сам узел поиска, его алгоритм или top-k (см. `primary:`/`backup:` в
`slides/n59-k4-stsena.md`). Тот же минимальный Pillow-приём, что
`make_figure_case1_postanovka.py`/`make_figure_case2_postanovka.py`/
`make_figure_case3_postanovka.py` этого же занятия — ближе всего по форме к Кейсу 3
(дашед-рамка+стрелка указывают НЕ на целый новый узел, а на часть содержания уже
существующего узла), не к Кейсу 1/2 (дашед-рамка целого вставляемого блока).

Палитра курса (CLAUDE.md, LOCKED): Ocean `#21295C`/`#065A82`/`#1C7293`, Teal `#028090`,
Gold `#F0AB00` (акцент — пунктирная рамка+стрелка на заменяемую базу).

Запуск: `python3 make_figure_case4_postanovka.py` (из `rendered/`).
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

W, H = 1900, 560
BG = (244, 247, 250)
INK = (33, 41, 92)       # #21295C
STROKE = (28, 114, 147)  # #1C7293
GOLD = (240, 171, 0)     # #F0AB00
WHITE = (255, 255, 255)

try:
    FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    FONT_B = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
except Exception:
    FONT = ImageFont.load_default()
    FONT_B = FONT


def rounded_box(draw, box, text, fill=WHITE, stroke=STROKE, text_color=INK, font=FONT,
                 extra_line=None, extra_color=None):
    """Сплошная коробка узла. `extra_line`, если дан, рисуется ПЕРВОЙ строкой (сверху,
    чтобы пунктирная стрелка сверху могла дойти до неё, не пересекая остальные строки)
    цветом `extra_color` (здесь — заменяемая база, на которую указывает дашед-коллаут).
    Возвращает её bbox, чтобы вызывающий код обвёл его пунктирной рамкой."""
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=14, fill=fill, outline=stroke, width=4)

    lines = text.split("\n")
    if extra_line is not None:
        lines = [extra_line] + lines
    lh = font.size + 10
    ty = (y0 + y1) / 2 - (lh * len(lines)) / 2

    extra_bbox = None
    for idx, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        lx = (x0 + x1) / 2 - tw / 2
        color = text_color
        if extra_line is not None and idx == 0:
            color = extra_color
        draw.text((lx, ty), line, fill=color, font=font)
        if extra_line is not None and idx == 0:
            extra_bbox = (lx - 12, ty - 6, lx + tw + 12, ty + font.size + 6)
        ty += lh
    return extra_bbox


def arrow(draw, p0, p1, color=STROKE, width=4):
    draw.line([p0, p1], fill=color, width=width)
    x1, y1 = p1
    draw.polygon([(x1, y1), (x1 - 16, y1 - 10), (x1 - 16, y1 + 10)], fill=color)


def dashed_line(draw, p0, p1, color=GOLD, width=5, seg=14, gap=10):
    import math
    x0, y0 = p0
    x1, y1 = p1
    length = math.hypot(x1 - x0, y1 - y0)
    if length == 0:
        return
    n = max(1, int(length / (seg + gap)))
    for i in range(n + 1):
        t0 = (i * (seg + gap)) / length
        t1 = min(1.0, (i * (seg + gap) + seg) / length)
        if t0 >= 1.0:
            break
        sx = x0 + (x1 - x0) * t0
        sy = y0 + (y1 - y0) * t0
        ex = x0 + (x1 - x0) * t1
        ey = y0 + (y1 - y0) * t1
        draw.line([(sx, sy), (ex, ey)], fill=color, width=width)


def dashed_arrow(draw, p0, p1, color=GOLD, width=5):
    dashed_line(draw, p0, p1, color=color, width=width)
    x1, y1 = p1
    draw.polygon([(x1, y1), (x1 - 14, y1 - 22), (x1 + 14, y1 - 22)], fill=color)


def dashed_rounded_rect(draw, box, color=GOLD, width=5, radius=10):
    x0, y0, x1, y1 = box
    perim_pts = []
    n = 60
    for i in range(n):
        t = i / n
        if t < 0.25:
            x = x0 + (x1 - x0) * (t / 0.25); y = y0
        elif t < 0.5:
            x = x1; y = y0 + (y1 - y0) * ((t - 0.25) / 0.25)
        elif t < 0.75:
            x = x1 - (x1 - x0) * ((t - 0.5) / 0.25); y = y1
        else:
            x = x0; y = y1 - (y1 - y0) * ((t - 0.75) / 0.25)
        perim_pts.append((x, y))
    for i in range(0, len(perim_pts) - 1, 2):
        draw.line([perim_pts[i], perim_pts[i + 1]], fill=color, width=width)


def main():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)

    box1 = (20, 220, 400, 370)
    box2 = (460, 170, 1340, 420)
    box3 = (1400, 220, 1870, 370)

    rounded_box(d, box1, "Вопрос\nстудента курса", font=FONT)

    base_bbox = rounded_box(
        d, box2,
        "поиск по смыслу\n(рецепт С10)",
        font=FONT,
        extra_line="в базе СВОЕГО курса",
        extra_color=GOLD,
    )

    rounded_box(d, box3, "Ответ", font=FONT)

    # сплошные стрелки между узлами — уже работающий ряд (Семинар 10)
    arrow(d, (box1[2], (box1[1] + box1[3]) / 2), (box2[0], (box2[1] + box2[3]) / 2))
    arrow(d, (box2[2], (box2[1] + box2[3]) / 2), (box3[0], (box3[1] + box3[3]) / 2))

    # пунктирная золотая рамка + стрелка — указывают НЕ на новый узел и не на сам узел
    # поиска, а на то, В КАКОЙ БАЗЕ он ищет: именно эту базу версия 1 заменяет (см.
    # primary: в n59-k4-stsena.md)
    if base_bbox:
        dashed_rounded_rect(d, base_bbox, radius=8)
        bx0, by0, bx1, by1 = base_bbox
        tip = ((bx0 + bx1) / 2, by0 - 6)
        dashed_arrow(d, (tip[0], 60), tip)
        label = "версия 1 заменяет эту базу: один общий индекс всех курсов центра вместо базы каждого курса отдельно"
        bbox = d.textbbox((0, 0), label, font=FONT)
        lw = bbox[2] - bbox[0]
        d.text((max(20, tip[0] - lw / 2), 18), label, fill=GOLD, font=FONT)

    d.text((20, 460), "сплошные линии — уже работает с прошлого занятия (поиск по смыслу над своей базой курса, рецепт С10)",
           fill=STROKE, font=FONT)
    d.text((20, 505), "пунктирная золотая рамка — узел, который версия 1 заменяет: общий индекс вместо базы своего курса",
           fill=GOLD, font=FONT)

    im.save(OUT / "case4-s11-postanovka.png")
    print("saved", OUT / "case4-s11-postanovka.png", im.size)


if __name__ == "__main__":
    main()
