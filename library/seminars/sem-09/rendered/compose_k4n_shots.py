#!/usr/bin/env python3
"""Два составных кадра Кейса 4 (переопределённого 2026-10-29, issue #303) из уже
снятых настоящих кусков стенда (`n8n_shots.py --figures-k4n`, живой
`n8n.lessons.tellian.io`). Это НЕ пересъёмка и не стилизация (БРИФ §5
`zamery-k4-novyy/README.md`): пиксели каждой половины — ровно те, что снял
`clip_canvas`/`clip_panel`, без единой правки внутри них. Добавлены только
подписи-заголовки СНАРУЖИ снимков — то же самое, что делает любой слайд деки,
подписывая кадр словами рядом, а не внутри.

1. `k4-holst-0-vs-prc.png` — холст конфигурации «без защиты» (6 узлов, прямая
   линия) и холст конфигурации «все три защиты» (13 узлов, две развилки) друг
   над другом. Владелец просил именно это противопоставление, читаемое с
   одного взгляда (БРИФ §А, `zamery-k4-novyy/README.md`: «холст, на котором
   узла механической проверки физически нет, — честное изображение
   конфигурации «без механики»»).
2. `k4-panel-mehanika.png` — панель узла «Механическая проверка» без нижней
   подсказки интерфейса («Type $ for a list…», мешает содержанию, срезана
   так же, как `crop_k3_panel_tight.py` срезал вкладки Mode/Language там, где
   они были лишними).

Источники — `stend/n8n-screenshots-raw/k4n-holst-0.png`,
`.../k4n-holst-prc.png`, `.../k4n-panel-mehanika-raw.png` (все три — сырые
кадры `n8n_shots.py --figures-k4n`, лежат рядом с остальными сырыми снимками
стенда, НЕ в `figures/`: это вход для склейки ниже, не самостоятельная
фигура деки).

Запуск: `python3 compose_k4n_shots.py` (из `rendered/`).
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FIGS = Path(__file__).parent / "figures"
RAW = Path(__file__).parents[1] / "stend" / "n8n-screenshots-raw"

F_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
DEEP = (0x21, 0x29, 0x5C)
LIGHT = (0x1C, 0x72, 0x93)
GOLD = (0xF0, 0xAB, 0x00)
SURF = (0xF4, 0xF7, 0xFA)
W = (255, 255, 255)

TARGET_W = 2400


def _scaled(path, target_w):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    nh = round(h * target_w / w)
    return im.resize((target_w, nh), Image.LANCZOS)


def holst_pair():
    pad = 40
    label_h = 90
    gap = 30
    im0 = _scaled(RAW / "k4n-holst-0.png", TARGET_W)
    im1 = _scaled(RAW / "k4n-holst-prc.png", TARGET_W)
    total_h = pad + label_h + im0.height + gap + label_h + im1.height + pad

    canvas = Image.new("RGB", (TARGET_W + pad * 2, total_h), W)
    d = ImageDraw.Draw(canvas)
    fo = ImageFont.truetype(F_BOLD, 54)

    y = pad
    d.rectangle([pad, y, pad + TARGET_W, y + label_h - 14], fill=SURF,
                outline=LIGHT, width=3)
    d.text((pad + 24, y + 16), "Конфигурация «0» — без единой защиты, 6 узлов",
            font=fo, fill=DEEP)
    y += label_h
    canvas.paste(im0, (pad, y))
    y += im0.height + gap

    d.rectangle([pad, y, pad + TARGET_W, y + label_h - 14], fill=W,
                outline=GOLD, width=4)
    d.text((pad + 24, y + 16),
            "Конфигурация «prc» — все три защиты вместе, 13 узлов",
            font=fo, fill=DEEP)
    y += label_h
    canvas.paste(im1, (pad, y))

    out = FIGS / "k4-holst-0-vs-prc.png"
    canvas.save(out)
    print(f"  {out.name}  {canvas.size} — два настоящих холста стенда, друг над "
          f"другом, подписи снаружи")


def mehanika_panel():
    src = RAW / "k4n-panel-mehanika-raw.png"
    im = Image.open(src)
    w, h = im.size
    # Нижняя подсказка интерфейса («Type $ for a list…») начинается в
    # последних ~150 px кадра — измерено по самому файлу, не на глаз
    # (профиль: оранжевая рамка подсказки видна с y≈1632 до низа).
    cropped = im.crop((0, 0, w, h - 150))
    out = FIGS / "k4-panel-mehanika.png"
    cropped.save(out)
    print(f"  {out.name}  {im.size} -> {cropped.size} — убрана подсказка "
          f"интерфейса снизу, код не тронут")


if __name__ == "__main__":
    holst_pair()
    mehanika_panel()
