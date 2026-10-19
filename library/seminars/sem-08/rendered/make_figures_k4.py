#!/usr/bin/env python3
"""Кейс «Карточка в Telegram» Семинара 8 (issue #274) — 2 схемы.

    k4-shema-trebovaniya.png   слой 1: две колонки требований — «Механическое»
                                (размер файла, формат, разрешение — проверяет
                                код) и «Смысловое / по содержанию» (картинка
                                показывает то, что нужно — нужна модель с
                                vision, не покрыто сегодня). Разметка — по
                                образцу двух колонок с заголовками и разными
                                цветами (`sem-07/rendered/make_figures_c1.py`).
    k4-n8n-tsepochka.png       слой 2 (n8n-стиль): `Set` «Compose notification
                                (template)» → `HTTP Request` «Fetch card
                                image» → `Telegram sendPhoto` «Send card» +
                                врезка с реальной ошибкой Telegram Bot API на
                                границе размера файла.

Формулировки и числа — дословно `SETKA-KEYSOV-S8-part2.md` «Кейс 4 —
Карточка в Telegram» и `BRIEF-PROIZVODSTVO.md` §3. Слой 2 — не снимок
живого UI n8n, недостижим в этой среде, см. `notes/mcp-limitations.md`
[#233-8].

Запуск: `python3 make_figures_k4.py` (из `rendered/`).
"""
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))

from fig_toolkit import *
from n8n_canvas_kit import node_n8n, arrow_n8n, callout, legend_n8n, disclaimer

CW = 1600


def frame(d, x, y, w, h, *, fill=SURF, stroke=LIGHT, sw=3, r=16):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=stroke, width=sw)


# ── слой 1: две колонки требований ──────────────────────────────────────────
def trebovaniya():
    CH = 560
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Два класса требований к картинке — одна и та же ось «модель или код»",
         sz=23, x=40, y=16)

    COLW, GAP = 740, 60
    LX, RX = 40, 40 + COLW + GAP
    CY0, CH0 = 110, 400

    # левая колонка — механическое
    frame(d, LX, CY0, COLW, CH0, fill=PALE, stroke=MID, sw=4)
    clabel(d, LX + COLW / 2, CY0 + 28, "Механическое", 28, DEEP, True,
           where="заголовок · механическое", limit=COLW - 60)
    items_l = ["размер файла", "формат", "разрешение"]
    iy = CY0 + 100
    for it in items_l:
        d.ellipse([LX + 60, iy + 8, LX + 76, iy + 24], fill=MID)
        clabel(d, LX + COLW / 2 + 20, iy, it, 22, DEEP, where=f"пункт · {it}", limit=COLW - 160)
        iy += 54
    frame(d, LX + 40, CY0 + 300, COLW - 80, 70, fill=W, stroke=MID, sw=3, r=12)
    clabel(d, LX + COLW / 2, CY0 + 322, "код проверяет — у файла есть измеримые свойства",
           17, MID, True, where="тег · механическое", limit=COLW - 120)

    # правая колонка — смысловое
    frame(d, RX, CY0, COLW, CH0, fill=WARM, stroke=GOLD, sw=4)
    clabel(d, RX + COLW / 2, CY0 + 28, "Смысловое / по содержанию", 26, GOLDINK, True,
           where="заголовок · смысловое", limit=COLW - 60)
    lines_r = wrap(d, "картинка на самом деле показывает то, что нужно"
                       " — не битый файл-заглушка, не чужое изображение", f(22), COLW - 160)
    iy = CY0 + 110
    for ln in lines_r:
        fit(d, ln, f(22), COLW - 160, "пункт · смысловое")
        clabel(d, RX + COLW / 2, iy, ln, 22, GOLDINK, where="пункт · смысловое", limit=COLW - 160)
        iy += 32
    frame(d, RX + 40, CY0 + 300, COLW - 80, 70, fill=W, stroke=GOLD, sw=3, r=12)
    clabel(d, RX + COLW / 2, CY0 + 318, "нужна модель с vision —", 17, GOLDINK, True,
           where="тег · смысловое 1", limit=COLW - 120)
    clabel(d, RX + COLW / 2, CY0 + 340, "не покрыто сегодня", 17, GOLDINK, True,
           where="тег · смысловое 2", limit=COLW - 120)

    clabel(d, CW / 2, 530,
           "Технически исправный файл всё равно может показывать не то, что нужно.",
           19, MUTE, where="подвал", limit=CW - 120)
    return im


save(trebovaniya(), "k4-shema-trebovaniya.png")


# ── слой 2: n8n-стиль, цепочка Set → HTTP Request → Telegram ───────────────
def tsepochka():
    CH = 540
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Слой 2 — узел n8n: от шаблона текста до отправки фото", sz=24, x=40, y=16)

    CY = 200
    node_n8n(d, 40, CY - 95, 440, 190,
              "Compose notification (template)",
              "notification_text — то же выражение шаблона, что в «Уведомлениях»",
              kind="code", subtype="Set", body_sz=14, where="узел шаблона")

    node_n8n(d, 580, CY - 95, 440, 190,
              "Fetch card image",
              "забирает файл по URL · формат ответа — файл (бинарные данные)",
              kind="external", subtype="HTTP Request", body_sz=14, where="узел загрузки")

    node_n8n(d, 1120, CY - 95, 440, 190,
              "Send card",
              "бинарные данные + caption из текста уведомления",
              kind="external", subtype="Telegram · sendPhoto", body_sz=14, where="узел отправки")

    arrow_n8n(d, 480, 580, CY)
    arrow_n8n(d, 1020, 1120, CY)

    callout(d, 220, CY + 155, 1160, 150,
            "Реальная ошибка Telegram Bot API на границе размера",
            ['"Bad Request: file of size 12812355 bytes is too big for a photo;'
             ' the maximum size is 10485760 bytes"',
             "файл 12 812 355 байт — между лимитом n8n 16 МБ и лимитом sendPhoto 10 МБ"
             " (10 485 760 байт)"],
            tone="bad", where="ошибка telegram")

    legend_n8n(d, 40, CY + 350)
    disclaimer(d, CW / 2, CY + 390)
    return im


save(tsepochka(), "k4-n8n-tsepochka.png")

report()
