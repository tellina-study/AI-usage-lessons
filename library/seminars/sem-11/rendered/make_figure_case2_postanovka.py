#!/usr/bin/env python3
"""Семинар 11, Кейс 2 — схема постановки (правило С1, `forma-keysa-s-zamerom.md` §2):
сплошными — блоки, уже работающие с рецепта Семинара 10 (документ режется по
предложениям, кусок кладётся в хранилище, поиск находит кусок, модель отвечает по
куску), пунктирной золотой рамкой — узел, который ЭТОТ кейс вставляет между поиском и
ответом: разведение единицы поиска и единицы ответа. Тот же минимальный Pillow-приём,
что `make_figure_case1_postanovka.py` этого же занятия (не стилизация живого UI —
обычная принципиальная схема, как того требует С1).

Палитра курса (CLAUDE.md, LOCKED): Ocean `#21295C`/`#065A82`/`#1C7293`, Teal `#028090`,
Gold `#F0AB00` (акцент — пунктирный новый блок).

Запуск: `python3 make_figure_case2_postanovka.py` (из `rendered/`).
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

W, H = 2150, 460
BG = (244, 247, 250)
INK = (33, 41, 92)       # #21295C
STROKE = (28, 114, 147)  # #1C7293
GOLD = (240, 171, 0)     # #F0AB00
WHITE = (255, 255, 255)

try:
    FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    FONT_B = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
except Exception:
    FONT = ImageFont.load_default()
    FONT_B = FONT


def rounded_box(draw, box, text, dashed=False, fill=WHITE, stroke=STROKE, text_color=INK, font=FONT):
    x0, y0, x1, y1 = box
    if not dashed:
        draw.rounded_rectangle(box, radius=14, fill=fill, outline=stroke, width=4)
    else:
        draw.rounded_rectangle(box, radius=14, fill=fill)
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
            draw.line([perim_pts[i], perim_pts[i + 1]], fill=GOLD, width=5)
    lines = text.split("\n")
    lh = font.size + 6
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


def main():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)

    boxes = [
        ((20, 150, 380, 280), "Документ режется\nпо предложениям (С10)", False),
        ((440, 150, 800, 280), "Кусок в хранилище,\nпоиск по вопросу", False),
        ((860, 150, 1340, 280), "Единица поиска ≠ единица ответа:\nмельче ищем, крупнее отвечаем", True),
        ((1400, 150, 1760, 280), "Ответ модели\nпо найденному контексту", False),
        ((1820, 150, 2130, 280), "Ответ\nобратившемуся", False),
    ]
    centers = []
    for box, text, dashed in boxes:
        rounded_box(d, box, text, dashed=dashed, font=FONT)
        x0, y0, x1, y1 = box
        centers.append(((x0, (y0 + y1) / 2), (x1, (y0 + y1) / 2)))

    for i in range(len(centers) - 1):
        arrow(d, centers[i][1], centers[i + 1][0])

    d.text((20, 40), "Куда вмешивается Кейс 2: узел между поиском и ответом, не сама резка",
           fill=INK, font=FONT_B)
    d.text((20, 320), "сплошные линии — уже работает с Семинара 10", fill=STROKE, font=FONT)
    d.text((20, 365), "пунктирная золотая рамка — узел, который собирает этот кейс", fill=GOLD, font=FONT)

    im.save(OUT / "case2-s11-shema-postanovka.png")
    print("saved", OUT / "case2-s11-shema-postanovka.png", im.size)


if __name__ == "__main__":
    main()
