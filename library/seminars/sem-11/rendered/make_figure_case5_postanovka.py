#!/usr/bin/env python3
"""Семинар 11, Кейс 5 — схема постановки (правило С1, `forma-keysa-s-zamerom.md` §2):
сплошным рядом — то, что уже работает с рецепта Семинара 10 (два разных, не
пересекающихся источника Ольгиного учебного центра — учебный план и правила
безопасности — питают один поиск, поиск отдаёт найденное прямо в ответ, без
проверки); пунктирная золотая стрелка — не новый узел в ряду и не параметр внутри
узла (как Кейс 3) и не заменяемая база (как Кейс 4), а ТОЧКА МЕЖДУ поиском и
ответом, в которую этот кейс вставляет отдельную проверку найденного (грейдер),
прежде чем отдавать его дальше (см. `primary:`/`backup:` в `slides/n75-k5-
stsena.md`). Тот же минимальный Pillow-приём, что `make_figure_case1_postanovka.
py`/`make_figure_case2_postanovka.py`/`make_figure_case3_postanovka.py`/
`make_figure_case4_postanovka.py` этого же занятия — ближе всего по форме к
Кейсу 3/4 (дашед-стрелка указывает на точку/часть содержания, не на целый
вставляемый блок, как у Кейса 1/2), но здесь дашед указывает на ПРОМЕЖУТОК между
двумя уже существующими узлами, а не на содержание внутри одного узла.

Холст — плоский широкий ряд из ТРЁХ коробок (не пяти/стопкой), тем же соотношением
сторон, что у Кейсов 1-4: первая сборка деки печатала «СХЕМА ЗАЖАТА» на более
высоком (стопочном) варианте этой же схемы — соседние текстовые блоки сцены n75
съедали высоту, доступную фигуре. Два источника сведены в ОДНУ коробку с двумя
строками текста (не в две отдельные, стопкой) — то же семантическое содержание,
плоская раскладка.

Палитра курса (CLAUDE.md, LOCKED): Ocean `#21295C`/`#065A82`/`#1C7293`, Teal
`#028090`, Gold `#F0AB00` (акцент — пунктирная стрелка на точку вставки).

Запуск: `python3 make_figure_case5_postanovka.py` (из `rendered/`).
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

W, H = 1900, 500
BG = (244, 247, 250)
INK = (33, 41, 92)       # #21295C
STROKE = (28, 114, 147)  # #1C7293
GOLD = (240, 171, 0)     # #F0AB00
WHITE = (255, 255, 255)

try:
    FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    FONT_B = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    FONT_SMALL = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 23)
except Exception:
    FONT = ImageFont.load_default()
    FONT_B = FONT
    FONT_SMALL = FONT


def rounded_box(draw, box, text, fill=WHITE, stroke=STROKE, text_color=INK, font=FONT):
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=14, fill=fill, outline=stroke, width=4)
    lines = text.split("\n")
    lh = font.size + 8
    ty = (y0 + y1) / 2 - (lh * len(lines)) / 2
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((x0 + x1) / 2 - tw / 2, ty), line, fill=text_color, font=font)
        ty += lh


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


def main():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)

    d.text((20, 16), "Куда вмешивается Кейс 5: точка между поиском и ответом, не новый узел ряда",
           fill=INK, font=FONT_B)

    box_sources = (20, 230, 620, 400)
    box_search = (650, 230, 1250, 400)
    box_answer = (1280, 230, 1880, 400)

    rounded_box(d, box_sources, "Два источника:\nучебный план + правила безопасности", font=FONT)
    rounded_box(d, box_search, "Поиск\n(гибрид, рецепт С10)", font=FONT)
    rounded_box(d, box_answer, "Ответ по найденному\n— без проверки", font=FONT)

    mid_y = (box_search[1] + box_search[3]) / 2
    arrow(d, (box_sources[2], mid_y), (box_search[0], mid_y))
    arrow(d, (box_search[2], mid_y), (box_answer[0], mid_y))

    # пунктирная золотая стрелка + подпись — указывает ВНИЗ, на ТОЧКУ МЕЖДУ
    # поиском и ответом (не на новый узел ряда и не на содержание внутри узла,
    # как у Кейса 3/4): именно туда этот кейс вставляет отдельную проверку
    # найденного (грейдер), прежде чем найденное уйдёт в ответ (см. primary: в
    # n75-k5-stsena.md).
    gap_mid_x = (box_search[2] + box_answer[0]) / 2
    label_lines = ["здесь кейс добавляет: грейдер —", "проверка найденного перед ответом"]
    ly = 66
    for line in label_lines:
        bbox = d.textbbox((0, 0), line, font=FONT_SMALL)
        lw = bbox[2] - bbox[0]
        d.text((gap_mid_x - lw / 2, ly), line, fill=GOLD, font=FONT_SMALL)
        ly += FONT_SMALL.size + 5
    dashed_arrow(d, (gap_mid_x, ly + 8), (gap_mid_x, box_search[1] - 8))

    d.text((20, 418), "сплошные линии — уже работает с Семинара 10 (два источника → один поиск → ответ по найденному)",
           fill=STROKE, font=FONT_SMALL)
    d.text((20, 452), "пунктирная золотая стрелка — точка между поиском и ответом, куда этот кейс вставляет проверку",
           fill=GOLD, font=FONT_SMALL)

    im.save(OUT / "case5-s11-postanovka.png")
    print("saved", OUT / "case5-s11-postanovka.png", im.size)


if __name__ == "__main__":
    main()
