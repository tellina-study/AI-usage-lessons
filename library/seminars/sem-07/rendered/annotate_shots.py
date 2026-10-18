#!/usr/bin/env python3
"""Пояснения поверх снимков холста: обзорный экран на каждый кейс.

Правка владельца (2026-10-13): «в слайдах ещё не хватает скрина процесса с
пояснениями на каждый кейс, сразу ныряем внутрь, а взгляда сверху нет».

Делает ровно одно: берёт снимок холста с живого стенда и ставит на него
нумерованные метки у нужных узлов плюс подписи снизу. Снимок не
перерисовывается и не подделывается — метки кладутся поверх настоящего кадра.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

HERE = Path(__file__).parent / "figures"
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
GOLD, TEAL, INK, W = (0xF0, 0xAB, 0x00), (0x02, 0x80, 0x90), (0x14, 0x1B, 0x2E), (255, 255, 255)
SURF, RED = (0xF4, 0xF7, 0xFA), (0xB3, 0x26, 0x1E)


def annotate(src, dst, marks, caption, color=TEAL):
    """`marks` — (номер, x, y) в координатах ИСХОДНОГО снимка."""
    im = Image.open(HERE / src).convert("RGB")
    w, h = im.size
    band = 150
    out = Image.new("RGB", (w, h + band), W)
    out.paste(im, (0, 0))
    d = ImageDraw.Draw(out)
    r = 34
    for num, x, y in marks:
        d.ellipse([x - r, y - r, x + r, y + r], fill=color, outline=W, width=5)
        f = ImageFont.truetype(FB, 40)
        tw = d.textlength(str(num), font=f)
        d.text((x - tw / 2, y - 26), str(num), font=f, fill=W)
    d.rectangle([0, h, w, h + band], fill=SURF)
    f = ImageFont.truetype(F, 34)
    y = h + 26
    for line in caption:
        d.text((40, y), line, font=f, fill=INK)
        y += 46
    out.save(HERE / dst)
    print(f"{dst}: {out.size[0]}×{out.size[1]}")


# Координаты: метка ставится НАД коробкой узла, не на подпись. Прежде кружки
# легли поверх имён («Reque*orm», «Voca*ary check») — находка собственного
# просмотра кадра.
annotate("n8n-holst-stage1.png", "obzor-k1.png",
         [(1, 140, 48), (2, 620, 48), (3, 565, 600), (4, 1110, 48),
          (5, 1580, 48), (6, 2065, 48)],
         ["1 форма — вход процесса   ·   2 извлечение — достаёт значения из текста   ·   3 модель — второй узел шага",
          "4 сверка со списком   ·   5 запись строки   ·   6 экран результата — печатает всю дорогу"])

annotate("n8n-holst-stage1.png", "obzor-k2.png",
         [(2, 620, 48), (4, 1110, 48)],
         ["Меняются ДВА узла из шести: 2 — в схеме извлечения появляется поле «ещё в заявке»,",
          "4 — сверка проверяет его тем же списком. Форма, модель, запись и экран не трогаются."],
         color=GOLD)

# холст стадии 3 после обрезки: 2300×980
annotate("n8n-holst-vetka-otkaza.png", "obzor-k3.png",
         [(1, 565, 160), (2, 955, 405), (3, 1140, 575)],
         ["1 на узле извлечения — повтор: 3 попытки с паузой   ·   2 второй выход, подписан Error",
          "3 ветка отказа: та же таблица со status = not_parsed и свой экран результата"],
         color=RED)

annotate("n8n-verh-published.png", "obzor-k4.png",
         [(1, 1640, 110)],
         ["1 значок Published — в бою работает ОПУБЛИКОВАННАЯ версия, а не та, что открыта в редакторе.",
          "Правка на холсте сохраняется в черновик сама; в бой она уходит отдельным действием."],
         color=GOLD)
