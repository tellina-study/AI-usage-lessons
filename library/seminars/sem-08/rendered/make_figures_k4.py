#!/usr/bin/env python3
"""Кейс «Карточка в Telegram» Семинара 8 (issue #274) — 4 схемы.

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
    k4-shema-generatsii.png    НОВАЯ (голосовая правка 2026-10-20, issue #274,
                                слайд n48a): генерация картинки — текст
                                уведомления → специализированная генерирующая
                                модель → готовая карточка (текст встроен в
                                пиксели) → отправка в Telegram, плюс стоимость
                                генерации одной картинки и примечание про
                                перекодировку перед отправкой в Telegram.
                                Системно-нейтральный стиль (не n8n-узлы — этот
                                шаг на стенде не собран, см. disclaimer на
                                схеме), по образцу `make_figures_zillow.py`.
    k4-shema-szhatie.png       НОВАЯ (та же правка, слайд n48b): механическая
                                проверка → ветка (не прошла → отклонить /
                                прошла → модель проверки содержимого), и ниже
                                — до/после размера картинки при умеренном
                                сжатии перед отправкой в модель-проверяющую.

Формулировки и числа — дословно `SETKA-KEYSOV-S8-part2.md` «Кейс 4 —
Карточка в Telegram» и `BRIEF-PROIZVODSTVO.md` §3, КРОМЕ двух новых схем:
их числа — из брифа голосовой правки `qa/BRIEF-GOLOSOVAYA-PRAVKA-2026-10-20.md`
(генерация — публичная цена gpt-image-1.5, OpenAI, с источником на самой
схеме; сжатие — готовый исследовательский ответ оттуда же, строки 180-196,
цифры не менялись). Слой 2 (`k4-n8n-tsepochka.png`) и ветка «модель проверки
содержимого» на `k4-shema-szhatie.png` — не снимок живого UI n8n и не
реализованный узел, недостижимо/не собрано в этой среде, см.
`notes/mcp-limitations.md` [#233-8].

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
    clabel(d, RX + COLW / 2, CY0 + 318, "нужна модель с распознаванием", 17, GOLDINK, True,
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


# ── общий мелкий примитив: прямоугольник + заголовок + подпись ─────────────
def two_lines(d, cx, cy, top, bottom, *, tsz=20, bsz=15, tcol=DEEP, bcol=MUTE,
              tb=True, limit=None, where="?", third=None, tsz3=15, tcol3=None):
    """Коробка с 2-3 строками по центру: заголовок, подпись, опциональная
    третья строка (число) другим цветом. По образцу `make_figures_zillow.py`
    `two_lines`, расширено третьей строкой для чисел (размер/токены)."""
    lines = [(top, tsz, tcol, True), (bottom, bsz, bcol, False)]
    if third:
        lines.append((third, tsz3, tcol3 or bcol, True))
    fos = [f(sz, b) for _, sz, _, b in lines]
    if limit:
        for (txt, sz, _, b), fo in zip(lines, fos):
            fit(d, txt, fo, limit, f"{where} · {txt[:20]}")
    gaps = [sz + 7 for _, sz, _, _ in lines]
    th = sum(gaps) + 3 * (len(lines) - 1)
    y = cy - th / 2
    for (txt, sz, col, _), fo, gap in zip(lines, fos, gaps):
        d.text((cx - d.textlength(txt, font=fo) / 2, y), txt, font=fo, fill=col)
        y += gap + 3


# ── НОВАЯ слой: генерация картинки (n48a, голосовая правка 2026-10-20) ─────
def generatsiya():
    CW2, CH = 1600, 560
    im = Image.new("RGB", (CW2, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Генерация карточки: текст встроен в изображение, не подписан отдельно",
         sz=23, x=40, y=16)

    y, h = 130, 160
    xs = [40, 430, 820, 1210]
    bw = 350
    lim = bw - 40

    frame(d, xs[0], y, bw, h, fill=SURF, stroke=LIGHT)
    two_lines(d, xs[0] + bw / 2, y + h / 2, "Текст уведомления",
              "+ требование: текст поверх картинки", limit=lim, where="узел 1")

    frame(d, xs[1], y, bw, h, fill=WARM, stroke=GOLD, sw=4)
    two_lines(d, xs[1] + bw / 2, y + h / 2, "Генерирующая модель",
              "специально: текст → изображение", bsz=14,
              tcol=GOLDINK, bcol=GOLDINK, limit=lim, where="узел 2 · генерация")

    frame(d, xs[2], y, bw, h, fill=SURF, stroke=TEAL)
    two_lines(d, xs[2] + bw / 2, y + h / 2, "Готовая карточка",
              "текст уже встроен в пиксели", limit=lim, where="узел 3")

    frame(d, xs[3], y, bw, h, fill=W, stroke=DEEP, sw=4)
    two_lines(d, xs[3] + bw / 2, y + h / 2, "Отправка в Telegram",
              "как фото", limit=lim, where="узел 4")

    for i in range(3):
        arrow(d, xs[i] + bw, y + h / 2, xs[i + 1], y + h / 2, col=MID, wd=4)

    cy2 = y + h + 40
    callout(d, 40, cy2, 760, 160,
            "Стоимость генерации одной картинки — ориентир",
            ["gpt-image-1.5 (OpenAI), 1024×1024: низкое качество $0,009 ·"
             " среднее $0,034 · высокое $0,133 за картинку",
             "Допущение: карточка не требует наивысшей точности — беру"
             " среднее качество, ≈$0,034 за картинку",
             "Источник: прайсинг OpenAI на модели генерации изображений,"
             " сверено октябрь 2026"],
            tone="ok", where="стоимость генерации")

    callout(d, 820, cy2, 740, 160,
            "Примечание: генерируемый файл — не готов к отправке сразу",
            ["Картинки из генерирующих моделей приходят большого"
             " стандартного размера и слабо сжаты",
             "Нужна перекодировка в более лёгкий формат перед отправкой"
             " в Telegram — тот же лимит sendPhoto 10 МБ, что уже измерен"
             " на слое 2"],
            tone="warn", where="примечание перекодировка")

    clabel(d, CW2 / 2, cy2 + 190,
           "Архитектурная оценка, не узел на стенде: генерация картинки сегодня в цепочке не собрана.",
           17, MUTE, where="дисклеймер", limit=CW2 - 100)
    return im


save(generatsiya(), "k4-shema-generatsii.png")


# ── НОВАЯ слой: механика → модель + сжатие перед проверкой (n48b) ──────────
def szhatie():
    CW2, CH = 1600, 680
    im = Image.new("RGB", (CW2, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Механическая проверка → модель содержимого, и вопрос сжатия",
         sz=23, x=40, y=16)

    y, h = 110, 140
    frame(d, 40, y, 300, h, fill=SURF, stroke=LIGHT)
    two_lines(d, 40 + 150, y + h / 2, "Файл получен", "бинарные данные",
              limit=260, where="узел файл")

    frame(d, 390, y, 340, h, fill=PALE, stroke=MID, sw=4)
    two_lines(d, 390 + 170, y + h / 2, "Механическая проверка",
              "размер · формат · разрешение", limit=300, where="узел мех. проверка")

    frame(d, 850, y, 420, h, fill=WARM, stroke=GOLD, sw=4)
    two_lines(d, 850 + 210, y + h / 2, "Проверка содержимого",
              "модель-проверяющая — смысловое требование", bsz=14,
              tcol=GOLDINK, bcol=GOLDINK, limit=380, where="узел модель-проверка")
    clabel(d, 850 + 210, y + h + 24, "не собрано на стенде — оценка архитектуры",
           15, MUTE, where="тег модель-проверка", limit=420)

    arrow(d, 340, y + h / 2, 390, y + h / 2, col=MID, wd=4)
    arrow(d, 730, y + h / 2, 850, y + h / 2, col=MID, wd=4)
    clabel(d, 790, y - 14, "прошла", 18, MID, True, where="метка прошла")

    ry = y + h + 80
    frame(d, 390, ry, 340, 90, fill=W, stroke=RED, sw=3)
    clabel(d, 390 + 170, ry + 26, "Не прошла", 20, RED, True,
           where="узел отказ", limit=300)
    clabel(d, 390 + 170, ry + 54, "отклонить — дальше не идёт", 16, MUTE,
           where="узел отказ-низ", limit=300)
    arrow(d, 390 + 170, y + h, 390 + 170, ry, col=RED, wd=4, dash=True)
    clabel(d, 390 + 170 + 110, y + h + 34, "не прошла", 17, RED, True,
           where="метка не прошла")

    y2 = ry + 90 + 70
    clabel(d, CW2 / 2, y2 - 12, "Сжатие перед отправкой в модель-проверяющую",
           21, DEEP, True, where="заголовок секции 2", limit=CW2 - 120)

    y3, h3 = y2 + 40, 160
    frame(d, 120, y3, 460, h3, fill=SURF, stroke=LIGHT)
    two_lines(d, 120 + 230, y3 + h3 / 2, "До сжатия", "4032×3024, без сжатия",
              third="≈1500 токенов", tcol3=MUTE, limit=400, where="до сжатия")

    frame(d, 1020, y3, 460, h3, fill=SURF, stroke=TEAL, sw=4)
    two_lines(d, 1020 + 230, y3 + h3 / 2, "После сжатия", "720×540, JPEG Q85",
              third="≈300 токенов — впятеро дешевле", tcol3=MID, limit=400,
              where="после сжатия")

    arrow(d, 580, y3 + h3 / 2, 1020, y3 + h3 / 2, col=MID, wd=4)
    clabel(d, 800, y3 + h3 / 2 - 50, "умеренное сжатие:", 16, MUTE, True,
           where="метка сжатия 1", limit=420)
    clabel(d, 800, y3 + h3 / 2 - 28, "JPEG Q75–85, ширина ≤1024 px", 16, MUTE,
           where="метка сжатия 2", limit=420)

    clabel(d, CW2 / 2, y3 + h3 + 40,
           "Иллюстративный пример сопоставимого случая (общедоступные источники),"
           " не измерение на этом стенде.",
           16, MUTE, where="дисклеймер сжатие", limit=CW2 - 100)
    return im


save(szhatie(), "k4-shema-szhatie.png")

report()
