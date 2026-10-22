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
    k4-shema-generatsii.png    НОВАЯ (голосовая правка 2026-10-20, issue #274;
                                стоит на слайде «Генерация карточки: текст
                                внутри изображения» — в деке того круга он
                                назывался n48a): генерация картинки — текст
                                уведомления → специализированная генерирующая
                                модель → готовая карточка (текст встроен в
                                пиксели) → отправка в Telegram, плюс стоимость
                                генерации одной картинки и примечание про
                                перекодировку перед отправкой в Telegram.
                                Системно-нейтральный стиль (не n8n-узлы — этот
                                шаг на стенде не собран, см. disclaimer на
                                схеме), по образцу `make_figures_zillow.py`.
    k4-shema-szhatie.png       НОВАЯ (та же правка; слайд «Порядок проверки и
                                вопрос сжатия», в том круге n48b): механическая
                                проверка → ветка (не прошла → отклонить /
                                прошла → модель проверки содержимого), и ниже
                                — до/после размера картинки при умеренном
                                сжатии перед отправкой в модель-проверяющую.
    k4-uzly-nastroyka-real.png НОВАЯ (голосовая правка 2026-10-20, issue #274,
                                слайд n50a). СНЯТА СО СЛАЙДА волной 1б
                                «конфетки» (issue #292): её кегль подписей
                                интерфейса замерялся в 3,5 pt — худшая фигура
                                деки, — и n50a переведён на перекроп
                                `k4-panel-uzly-crop-real.png`
                                (`make_figures_crops.py`). Здесь остаётся как
                                запасной показ и как история кропа; ни один
                                слайд её сегодня не берёт. НЕ нарисованная
                                схема — composite
                                из ТРЁХ НАСТОЯЩИХ кропов живого стенда, панели
                                настройки узлов `Compose notification
                                (template)` (минимальный кроп — только
                                подтверждение, что узел тот же, без
                                повторного разбора), `Fetch card image (HTTP)`
                                и `Send card (Telegram photo)` (см. функцию
                                `uzly_nastroyka()` ниже за точными пиксельными
                                координатами кропа и маскировки Chat ID).
    k4-n8n-vetvlenie-real.png  НОВАЯ (круг правки по плотности скринов
                                2026-10-20 вечером, issue #274, владелец после
                                просмотра деки: «ты сам смотрел на скрины? в
                                последнем разделе почти нет, в остальных тоже
                                мало»), НОВЫЙ letter-tail слайд n49a (между n49
                                и n50 — канон README §1): настоящий кроп того
                                же канваса, что и `k4-n8n-tsepochka-real.png`,
                                но ШИРЕ влево — показывает точку ветвления:
                                `Write row` → `Result screen` (уже знакомый
                                путь приёма заявки) и ту же стрелку, уходящую
                                вверх в `Compose notification (template)` —
                                начало трёх узлов, которые разбирает весь кейс
                                (см. функцию `vetvlenie_real()`). ПЕРВОНАЧАЛЬНО
                                задуман как `fig_after` на разборе кейса
                                (в деке того круга — n48, по образцу
                                `k2-n8n-test-stend-real.png` на n20) — снято
                                после того, как `check_tracks_pdf.py` поймал
                                настоящий дефект (фигура заходила на текст над
                                собой: на том слайде уже стоят таблица + два
                                текстовых блока, тесно), см. backup n49a.

Формулировки и числа — дословно `SETKA-KEYSOV-S8-part2.md` «Кейс 4 —
Карточка в Telegram» и `BRIEF-PROIZVODSTVO.md` §3, КРОМЕ двух новых схем:
их числа — из брифа голосовой правки `qa/BRIEF-GOLOSOVAYA-PRAVKA-2026-10-20.md`
(генерация — публичная цена gpt-image-1.5, OpenAI, с источником на самой
схеме; сжатие — готовый исследовательский ответ оттуда же, строки 180-196,
цифры не менялись). Слой 2 (`k4-n8n-tsepochka.png`) и ветка «модель проверки
содержимого» на `k4-shema-szhatie.png` — не снимок живого UI n8n и не
реализованный узел, недостижимо/не собрано в этой среде, см.
`notes/mcp-limitations.md` [#233-8].

`k4-shema-generatsii.png` СНЯТА С РУССКОГО СЛАЙДА (волна 2в «конфетки», issue
#292) и остаётся здесь только ради английского трека. Причина не в вёрстке: в
её callout вшита ПИКСЕЛЯМИ прайсовая цена «≈$0,034 за картинку» и пометка, что
шага на стенде нет, — волна 1г шаг собрала, прогнала шесть раз и измерила
($0,0387 по счёту OpenRouter; `stend/n8n-screenshots-raw/
k4-generatsiya-izmereniya-2026-10-22.md`), то есть и цифра, и пометка
перестали быть правдой. Русский n51 теперь берёт настоящий кадр холста
(`k4-gen-tsepochka-real.png`, `make_figures_k4gen.py`), а числа — плашками из
самого слайда, где их видно и можно поправить. `slides-en/n51` по-прежнему
ссылается на `k4-shema-generatsii-en.png` со старыми числами — это долг волны
6 (EN-паритет), названный здесь, а не исправленный молча: RU — источник,
EN синхронизируется отдельной волной.

Запуск: `python3 make_figures_k4.py` (из `rendered/`).
"""
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))

from fig_toolkit import *
from n8n_canvas_kit import node_n8n, arrow_n8n, callout, legend_n8n, disclaimer

RAW = _Path(__file__).resolve().parent.parent / "stend" / "n8n-screenshots-raw"

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


# ── НОВАЯ слой: генерация картинки (слайд «Генерация карточки», голосовая
# правка 2026-10-20; в деке того круга — n48a) ─────────────────────────────
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
    callout(d, 40, cy2, 760, 185,
            "Стоимость генерации одной картинки — ориентир",
            ["gpt-image-1.5 (OpenAI), 1024×1024: низкое качество $0,009 ·"
             " среднее $0,034 · высокое $0,133 за картинку — для уведомления"
             " беру среднее, ≈$0,034 за картинку",
             "Источник: прайсинг OpenAI на модели генерации изображений,"
             " сверено октябрь 2026",
             # Идентификатор слайда «(n06)» снят волной 3а «конфетки» (issue
             # #292): это ВИДИМЫЙ слой, и ссылка вида `(nNN)` на нём запрещена
             # тем же правилом, что `→ sNN` и `§X.X` (CLAUDE.md, Pre-USER-GATE
             # §5). Ни один сторож её не поймал и поймать не мог:
             # `audit_sluzhebnoe.py` читает текстовый слой pptx, а здесь текст
             # нарисован в пиксели фигуры. Кейс назван словами, как и везде на
             # экране; номер слайда остаётся в заметках и в backup слайда.
             "Иллюстративно, НЕ измерено: ≈20 карточек/день — тот же поток"
             " заявок, что в Кейсе 1 → ≈600/месяц → ≈$20,4/месяц"],
            tone="ok", where="стоимость генерации")

    callout(d, 820, cy2, 740, 185,
            "Примечание: генерируемый файл — не готов к отправке сразу",
            ["Картинки из генерирующих моделей приходят большого"
             " стандартного размера и слабо сжаты",
             "Нужна перекодировка в более лёгкий формат перед отправкой"
             " в Telegram — тот же лимит sendPhoto 10 МБ, что уже измерен"
             " на слое 2"],
            tone="warn", where="примечание перекодировка")

    clabel(d, CW2 / 2, cy2 + 205,
           "Архитектурная оценка, не узел на стенде: генерация картинки сегодня в цепочке не собрана.",
           17, MUTE, where="дисклеймер", limit=CW2 - 100)
    return im


save(generatsiya(), "k4-shema-generatsii.png")


# ── НОВАЯ слой: механика → модель + сжатие перед проверкой (слайд «Порядок
# проверки и вопрос сжатия»; в деке того круга — n48b) ─────────────────────
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


# ── НОВАЯ: настоящие панели настройки узлов (n50a, голосовая правка 2026-10-20) ─
def uzly_nastroyka():
    """Composite из ТРЁХ НАСТОЯЩИХ кропов живого стенда (не нарисованная
    схема, не холст) — по образцу `k2-n8n-panels-real.png` (n22a, тот же
    круг правки): минимальный кроп узла `Compose notification (template)`
    слева (ТОЛЬКО заголовок + Mode + Fields to Set + сама строка выражения —
    без «Include Other Input Fields» и далее, см. ниже почему), панель
    настройки узла `Fetch card image (HTTP)` в середине, панель настройки
    узла `Send card (Telegram photo)` справа, глухой кроп + склейка, без
    перерисовки.

    ПЕРЕСМОТР (круг правки по плотности скринов 2026-10-20 вечером, issue
    #274): до этого правки узел `Compose notification (template)` сюда
    сознательно НЕ включался — тот же приём подстановки значений уже
    разобран панелью узла в Кейсе 1 (n11/n14), и полный повторный разбор
    здесь означал бы повторить уже показанное, а не добавить новое. Это
    решение не отменено и по-прежнему верно для ПОЛНОГО разбора; но узкая
    претензия владельца («в последнем разделе почти нет [скринов]») указывает
    на другой, более частный пробел: ни один слайд кейса 4 до сих пор не
    подтверждает СКРИНОМ факт, что узел `Compose` в этой цепочке — тот же
    самый, а не переписанный заново (в прозе n50 это только УТВЕРЖДАЕТСЯ:
    «тот же приём подстановки значений, что мы настраивали в кейсе
    «Уведомления»»). Кроп сведён к минимуму (заголовок + выражение, без
    нижней половины панели с переключателями) ИМЕННО чтобы не повторять
    разбор — это подтверждение тождества узла, не вторая лекция про
    подстановку.

    Источник — `stend/n8n-screenshots-raw/case4-compose-notification.png`,
    `case4-fetch-image.png` и `case4-send-telegram.png` (1900×1100 каждый),
    сняты 2026-10-20 тем же каналом Playwright, что и
    `k4-n8n-tsepochka-real.png` и `k2-n8n-panels-real.png`
    (notes/mcp-limitations.md [#233-8]).

    КРОП Compose — (0,0)–(1160,430) одного скрина: заголовок узла, вкладка
    Parameters, `Mode` = Manual Mapping, `Fields to Set` → поле
    `notification_text` (тип String) и сама строка выражения целиком,
    дословно та же, что уже стояла на панели Кейса 1 (n11a/n14a):
    `Новая заявка от {{ $('Request form').item.json['Имя'] }}: тема «{{
    $('Vocabulary check').item.json.topic }}»...`. Ниже этой точки на
    настоящей панели ещё идёт «Drag input fields here / Add Field»,
    «Include Other Input Fields» и «Options» — это тот же служебный хвост,
    что уже один раз показан и назван неинтересным на панели Fetch (ниже), и
    здесь обрезан без отдельной подписи о пропуске (кроп останавливается на
    содержательной границе, а не посередине поля, поэтому ложным не
    читается).

    ОТЛИЧИЕ от кроп-бокса n22a: та панель взяла x=[0,1160] одним сплошным
    прямоугольником (0,0)–(1160,660) — у обоих её узлов (`Set` с тремя
    полями, `IF` с одним условием) все нужные поля уместились в 660 px.
    У панели `Fetch card image (HTTP)` нужные поля (Method/URL — сверху,
    Response Format/Put Output in Field — снизу) разнесены куда шире, а
    между ними лежит честно неинтересный блок из четырёх выключенных по
    умолчанию переключателей (Authentication/Send Query Parameters/Send
    Headers/Send Body) — ни один не тронут и не несёт урока. Вместо того
    чтобы тащить middle целиком (кадр вышел бы заметно выше, чем нужно) или
    молча его вырезать (стало бы неочевидно, что часть панели пропущена),
    узел `Fetch` сделан ДВУХ-ПОЛОСНЫМ кропом одного и того же скрина — верх
    (0,0)–(1160,290) и низ (0,630)–(1160,900) — сшитым вертикально через
    полосу 50 px с явной подписью, что именно пропущено и почему. Это не
    склейка РАЗНЫХ скринов (как могло бы выглядеть нечестной подменой), а
    два смежных по вертикали куска ОДНОГО И ТОГО ЖЕ скриншота с открыто
    названным пропуском между ними — честность та же, что и у «мы режем
    прямоугольник, а не перерисовываем то, что внутри него» (n22/n23), плюс
    прямое указание на сам факт пропуска.

    Панель `Send card (Telegram photo)` — один сплошной кроп (0,0)–(1160,700):
    Credential/Resource/Operation/Chat ID/Binary File/Input Binary
    Field/Reply Markup/Additional Fields → Caption — здесь каждое поле
    настроено не по умолчанию и несёт урок, пропускать нечего.

    На ВСЕХ ТРЁХ скринах панель INPUT слева — настоящая, но ПУСТАЯ: `No input
    data`/`Execute previous nodes` — в отличие от n22a (там дерево INPUT
    показывает реальные поля предыдущих узлов), на этих узлах стенда
    предыдущие шаги не прогонялись перед съёмкой скрина. Кадр оставлен как
    есть, не дорисован и не вычищен — это не теряет честности (панель
    параметров, единственное, что здесь измеряется на каждой из трёх,
    настоящая и полная в своих отведённых границах), но прямо назвать
    стоит: пустое INPUT — это свойство момента съёмки, не иллюстрация
    «реальных данных». Панель INPUT и панель OUTPUT по краям скрина Compose
    в кроп не попадают вовсе — кроп (0,0)–(1160,430) берёт только
    центральную колонку Parameters, те же границы x, что и у Fetch/Send.

    Chat ID (266536553 на экране живого тестового Telegram-аккаунта стенда,
    личный числовой id, не относится к уроку) ЗАМАСКИРОВАН прямоугольником
    поверх поля значения; поле подписано `Chat ID` на самом скрине — зал
    видит, что это такое, не видит чьё именно."""
    compose_raw = Image.open(RAW / "case4-compose-notification.png")
    fetch_raw = Image.open(RAW / "case4-fetch-image.png")
    send_raw = Image.open(RAW / "case4-send-telegram.png")

    compose_panel = compose_raw.crop((0, 0, 1160, 430)).copy()  # title + Mode + Fields to Set + expression

    fb1 = fetch_raw.crop((0, 0, 1160, 290))      # title/tabs + Method + URL
    fb2 = fetch_raw.crop((0, 630, 1160, 900))    # Response Format + Put Output in Field
    GAP_FETCH = 50
    fetch_panel = Image.new("RGB", (1160, 290 + GAP_FETCH + 270), W)
    fd = ImageDraw.Draw(fetch_panel)
    fetch_panel.paste(fb1, (0, 0))
    fetch_panel.paste(fb2, (0, 290 + GAP_FETCH))
    fd.line([(40, 290 + 8), (1120, 290 + 8)], fill=SOFT_GREY, width=2)
    fd.line([(40, 290 + GAP_FETCH - 8), (1120, 290 + GAP_FETCH - 8)], fill=SOFT_GREY, width=2)
    clabel(fd, 580, 290 + GAP_FETCH / 2 - 9,
           "⋯ Authentication / Send Query Parameters / Send Headers / Send Body — не тронуты, по умолчанию ⋯",
           15, MUTE, where="пропуск · fetch", limit=1080)

    send_panel = send_raw.crop((0, 0, 1160, 700)).copy()
    sd = ImageDraw.Draw(send_panel)
    mx0, my0, mx1, my1 = 745, 345, 1150, 393   # Chat ID — поле значения, глобальные координаты = локальным (кроп с (0,0))
    sd.rectangle([mx0, my0, mx1, my1], fill=SURF, outline=LIGHT, width=2)
    clabel(sd, (mx0 + mx1) / 2, my0 + 16, "•••••••• (скрыт, личный id стенда)",
           14, MUTE, True, where="маска · chat id", limit=mx1 - mx0 - 20)

    GAP = 24
    panel_h = max(compose_panel.height, fetch_panel.height, send_panel.height)
    CW2 = 1160 * 3 + GAP * 2
    im = Image.new("RGB", (CW2, panel_h), W)
    im.paste(compose_panel, (0, 0))
    im.paste(fetch_panel, (1160 + GAP, 0))
    im.paste(send_panel, (2 * 1160 + 2 * GAP, 0))
    d = ImageDraw.Draw(im)
    d.rectangle([1160, 0, 1160 + GAP - 1, panel_h - 1], fill=SOFT_GREY)
    d.rectangle([2 * 1160 + GAP, 0, 2 * 1160 + 2 * GAP - 1, panel_h - 1], fill=SOFT_GREY)
    d.rectangle([0, 0, 1160, compose_panel.height - 1], outline=LIGHT, width=2)
    d.rectangle([1160 + GAP, 0, 1160 + GAP + 1160, fetch_panel.height - 1], outline=LIGHT, width=2)
    d.rectangle([2 * 1160 + 2 * GAP, 0, CW2 - 1, send_panel.height - 1], outline=LIGHT, width=2)
    return im


save(uzly_nastroyka(), "k4-uzly-nastroyka-real.png")


# ── НОВАЯ: подтверждающий скрин точки ветвления (n49a, круг правки по ──────
# плотности скринов 2026-10-20 вечером) ─────────────────────────────────────
def vetvlenie_real():
    """Кроп живого n8n-стенда, без перерисовки — только вырезка
    прямоугольника из того же RAW-скрина, что и `k4-n8n-tsepochka-real.png`
    (`stend/n8n-screenshots-raw/case4-telegram-image.png`, 1900×1100,
    Playwright, живой стенд, снят 2026-10-20), но ШИРЕ влево.

    ПЕРВОНАЧАЛЬНО задуман как `fig_after` на разборе кейса (в деке того
    круга — n48), тем же приёмом,
    что `k2-n8n-test-stend-real.png` на n20 (`make_figures_k2.py`,
    `test_stend_real()`). Снято с того слайда после того, как `check_tracks_pdf.py`
    (канон §7, сверка с тем, что РЕАЛЬНО нарисовал LibreOffice, не с меркой
    `metrics`) поймал настоящий дефект: перед фигурой там уже стоят
    таблица на 4 строки и два текстовых блока, и фигура заходила на текст
    над собой на 5,7–7,0 pt при любой из опробованных пропорций кропа —
    тесно структурно, не чинится подбором соотношения сторон. Перенесено на
    СВОЙ letter-tail слайд (n49a, между n49 и n50 — канон README §1), где
    фигура — единственный содержательный блок и места достаточно.

    Кроп (820, 258, 1800, 562) исходного файла: `Write row` → `Result
    screen` (уже знакомый по Кейсу 1 главный путь приёма заявки) слева, и та
    же стрелка, уходящая вверх от развилки после `Write row` к `Compose
    notification (template)` → `Fetch card image (HTTP)` → `Send card
    (Telegram photo)` — три узла, которые весь кейс 4 разбирает дальше.
    Результат 980×304 (соотношение 3,22). Правый край кропа заодно убирает
    всплывающую кнопку «✨ AI assist» — часть интерфейса n8n, не узел
    процесса.

    Что ИСКЛЮЧЕНО этим кропом сознательно, а не случайно:
    - `Request form` / `Extract fields` / `Model` / `Vocabulary check` —
      левее x=820, тот же приём разбора заявки, что уже показан на фигуре
      Кейса 1 (`k1-n8n-versiya1-real.png`, n11) — повторять здесь означало
      бы повторить уже увиденный экран, а не добавить новое;
    - `Write row · not parsed` / `Result screen · not parsed` — на том же
      канвасе НИЖЕ y=562 (видны на необрезанном `case4-telegram-image.png`):
      запасная ветка на случай, если разбор заявки моделью не распознал
      поля. Она существует на стенде по-настоящему, но относится к шагу
      ПРИЁМА заявки, не к шагу сборки и отправки карточки — не в фокусе
      сегодня, и единственная причина не включить её в кадр ЗДЕСЬ —
      геометрия: прямоугольник, который держит и её, и три узла
      карточки одновременно, разворачивает кадр почти в портрет (соотношение
      ~1,88) и упирается в потолок схемы — проверено прямым расчётом перед
      тем, как решить обрезать, не на глаз;
    - хлебная крошка названия воркфлоу, бейдж `Published`, вкладки
      Editor/Executions/Evaluations, левая колонка иконок приложения, правая
      плавающая панель зума/поиска, кнопка «Execute workflow», нижняя
      панель `Logs` — та же причина, что и на `k4-n8n-tsepochka-real.png`:
      workflow/execution id на кадре нет нигде (канон §2–§3).
    """
    raw = Image.open(RAW / "case4-telegram-image.png").convert("RGB")
    crop = raw.crop((820, 258, 1800, 562))
    # НЕ СОХРАНЯЕТСЯ. Источник этого имени — `make_figures_crops.py:
    # vetvlenie_rekrop()` (волна 1б): прямоугольник (815, 248, 1790, 585),
    # 975×337. Тамошняя строка-документация прямо говорит «источником
    # считать этот», но ЗАПИСЬ здесь при этом осталась живой — и ловушка
    # сработала по-настоящему в волне 3а «конфетки» (issue #292): прогон
    # этого файла ради одной правки подписи на схеме генерации молча
    # вернул старый кроп (820, 258, 1800, 562), 980×304, у которого нижний
    # край режет подписи `Write row` / `Result screen` и срезает
    # `Form Ending` целиком. Поймано сверкой md5 всех фигур до и после
    # прогона; кадр возвращён чтением блоба.
    #
    # Это ровно та же ловушка и то же её закрытие, что волна 2б сделала в
    # `make_figure_k3_real_captions.py` (четыре имени, `skip()`): соседний
    # файл был тогда вне её волны, и она честно назвала его в комментарии,
    # оставив жить. Теперь закрыт и он. Прямоугольник и разбор кадра выше
    # не удалены — это история решения, а не мусор; снята только запись.
    _ = crop
    print("   ПРОПУЩЕНО k4-n8n-vetvlenie-real.png: источник — "
          "make_figures_crops.py (волна 1б, перекроп под подписи узлов)")


vetvlenie_real()


# ── EN variants of the three fully-drawn schemes (issue #172/#274, Bilingual ─
# Production Rule, first EN pass for this seminar). Self-contained English
# literals here, NOT the shared --lang/fig_strings_en.py mechanism this
# toolkit also supports (see fig_toolkit.py docstring) — that dictionary is
# a seminar-wide resource other parallel case translators may also be
# touching today, and this file only owns Case 4's own figures. Saved with
# an explicit "-en.png" name while module-level LANG stays "ru" (default),
# so `save()`/`outname()` pass the literal name through unchanged. k4-n8n-
# vetvlenie-real.png / k4-n8n-tsepochka-real.png / k4-uzly-nastroyka-real.png
# are real rig screenshots — no EN variant needed, the RU names are reused
# as-is in slides-en/ (n8n's own UI is already English in the real crops).
def trebovaniya_en():
    CH = 560
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Two classes of picture requirement — the same «model or code» axis",
         sz=23, x=40, y=16)

    COLW, GAP = 740, 60
    LX, RX = 40, 40 + COLW + GAP
    CY0, CH0 = 110, 400

    frame(d, LX, CY0, COLW, CH0, fill=PALE, stroke=MID, sw=4)
    clabel(d, LX + COLW / 2, CY0 + 28, "Mechanical", 28, DEEP, True,
           where="заголовок · mechanical", limit=COLW - 60)
    items_l = ["file size", "format", "resolution"]
    iy = CY0 + 100
    for it in items_l:
        d.ellipse([LX + 60, iy + 8, LX + 76, iy + 24], fill=MID)
        clabel(d, LX + COLW / 2 + 20, iy, it, 22, DEEP, where=f"пункт · {it}", limit=COLW - 160)
        iy += 54
    frame(d, LX + 40, CY0 + 300, COLW - 80, 70, fill=W, stroke=MID, sw=3, r=12)
    clabel(d, LX + COLW / 2, CY0 + 322, "code checks it — the file has measurable properties",
           17, MID, True, where="тег · mechanical", limit=COLW - 120)

    frame(d, RX, CY0, COLW, CH0, fill=WARM, stroke=GOLD, sw=4)
    clabel(d, RX + COLW / 2, CY0 + 28, "Semantic / content-based", 26, GOLDINK, True,
           where="заголовок · semantic", limit=COLW - 60)
    lines_r = wrap(d, "the picture actually shows what's needed"
                       " — not a broken placeholder file, not someone else's image", f(22), COLW - 160)
    iy = CY0 + 110
    for ln in lines_r:
        fit(d, ln, f(22), COLW - 160, "пункт · semantic")
        clabel(d, RX + COLW / 2, iy, ln, 22, GOLDINK, where="пункт · semantic", limit=COLW - 160)
        iy += 32
    frame(d, RX + 40, CY0 + 300, COLW - 80, 70, fill=W, stroke=GOLD, sw=3, r=12)
    clabel(d, RX + COLW / 2, CY0 + 318, "needs a vision-capable model", 17, GOLDINK, True,
           where="тег · semantic 1", limit=COLW - 120)
    clabel(d, RX + COLW / 2, CY0 + 340, "not covered today", 17, GOLDINK, True,
           where="тег · semantic 2", limit=COLW - 120)

    clabel(d, CW / 2, 530,
           "A technically sound file can still show the wrong thing.",
           19, MUTE, where="подвал", limit=CW - 120)
    return im


save(trebovaniya_en(), "k4-shema-trebovaniya-en.png")


# ── EN variant: generating the card (n51) ───────────────────────────────────
def generatsiya_en():
    CW2, CH = 1600, 600
    im = Image.new("RGB", (CW2, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Generating the card: text baked into the image, not captioned separately",
         sz=22, x=40, y=16)

    y, h = 130, 160
    xs = [40, 430, 820, 1210]
    bw = 350
    lim = bw - 40

    frame(d, xs[0], y, bw, h, fill=SURF, stroke=LIGHT)
    two_lines(d, xs[0] + bw / 2, y + h / 2, "Notification text",
              "+ requirement: text on top of the picture", limit=lim, where="узел 1 en")

    frame(d, xs[1], y, bw, h, fill=WARM, stroke=GOLD, sw=4)
    two_lines(d, xs[1] + bw / 2, y + h / 2, "Generating model",
              "specifically: text → image", bsz=14,
              tcol=GOLDINK, bcol=GOLDINK, limit=lim, where="узел 2 · generation en")

    frame(d, xs[2], y, bw, h, fill=SURF, stroke=TEAL)
    two_lines(d, xs[2] + bw / 2, y + h / 2, "Finished card",
              "text already baked into the pixels", limit=lim, where="узел 3 en")

    frame(d, xs[3], y, bw, h, fill=W, stroke=DEEP, sw=4)
    two_lines(d, xs[3] + bw / 2, y + h / 2, "Sent to Telegram",
              "as a photo", limit=lim, where="узел 4 en")

    for i in range(3):
        arrow(d, xs[i] + bw, y + h / 2, xs[i + 1], y + h / 2, col=MID, wd=4)

    cy2 = y + h + 40
    callout(d, 40, cy2, 760, 185,
            "Cost of generating one picture — a reference point",
            ["gpt-image-1.5 (OpenAI), 1024x1024: low quality $0.009 ·"
             " medium $0.034 · high $0.133 per picture — for a notification"
             " I take medium, approx $0.034 per picture",
             "Source: OpenAI pricing for image-generation models,"
             " checked October 2026",
             "Illustrative, NOT measured: approx 20 cards/day — the request"
             " flow of Case 1 (n06) -> approx 600/month -> approx $20.4/month"],
            tone="ok", where="cost of generation en")

    callout(d, 820, cy2, 740, 185,
            "Note: the generated file is not ready to send right away",
            ["Pictures from generating models come at a large standard"
             " size and lightly compressed",
             "Needs re-encoding into a lighter format before sending to"
             " Telegram — the same sendPhoto 10 MB limit already measured"
             " at layer 2"],
            tone="warn", where="перекодировка en")

    clabel(d, CW2 / 2, cy2 + 205,
           "An architectural estimate, not a node on the rig: image generation is not built into the chain today.",
           16, MUTE, where="дисклеймер en", limit=CW2 - 100)
    return im


save(generatsiya_en(), "k4-shema-generatsii-en.png")


# ── EN variant: mechanics -> content model + compression (n52) ─────────────
def szhatie_en():
    CW2, CH = 1600, 680
    im = Image.new("RGB", (CW2, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Mechanical check -> content-check model, and the compression question",
         sz=22, x=40, y=16)

    y, h = 110, 140
    frame(d, 40, y, 300, h, fill=SURF, stroke=LIGHT)
    two_lines(d, 40 + 150, y + h / 2, "File received", "binary data",
              limit=260, where="узел файл en")

    frame(d, 390, y, 340, h, fill=PALE, stroke=MID, sw=4)
    two_lines(d, 390 + 170, y + h / 2, "Mechanical check",
              "size · format · resolution", limit=300, where="узел мех. проверка en")

    frame(d, 850, y, 420, h, fill=WARM, stroke=GOLD, sw=4)
    two_lines(d, 850 + 210, y + h / 2, "Content check",
              "content-check model — semantic requirement", bsz=14,
              tcol=GOLDINK, bcol=GOLDINK, limit=380, where="узел модель-проверка en")
    clabel(d, 850 + 210, y + h + 24, "not built on the rig — an architectural estimate",
           15, MUTE, where="тег модель-проверка en", limit=420)

    arrow(d, 340, y + h / 2, 390, y + h / 2, col=MID, wd=4)
    arrow(d, 730, y + h / 2, 850, y + h / 2, col=MID, wd=4)
    clabel(d, 790, y - 14, "passed", 18, MID, True, where="метка прошла en")

    ry = y + h + 80
    frame(d, 390, ry, 340, 90, fill=W, stroke=RED, sw=3)
    clabel(d, 390 + 170, ry + 26, "Did not pass", 20, RED, True,
           where="узел отказ en", limit=300)
    clabel(d, 390 + 170, ry + 54, "reject — goes no further", 16, MUTE,
           where="узел отказ-низ en", limit=300)
    arrow(d, 390 + 170, y + h, 390 + 170, ry, col=RED, wd=4, dash=True)
    clabel(d, 390 + 170 + 110, y + h + 34, "did not pass", 17, RED, True,
           where="метка не прошла en")

    y2 = ry + 90 + 70
    clabel(d, CW2 / 2, y2 - 12, "Compression before sending to the content-check model",
           20, DEEP, True, where="заголовок секции 2 en", limit=CW2 - 120)

    y3, h3 = y2 + 40, 160
    frame(d, 120, y3, 460, h3, fill=SURF, stroke=LIGHT)
    two_lines(d, 120 + 230, y3 + h3 / 2, "Before compression", "4032x3024, uncompressed",
              third="approx 1500 tokens", tcol3=MUTE, limit=400, where="до сжатия en")

    frame(d, 1020, y3, 460, h3, fill=SURF, stroke=TEAL, sw=4)
    two_lines(d, 1020 + 230, y3 + h3 / 2, "After compression", "720x540, JPEG Q85",
              third="approx 300 tokens — five times cheaper", tcol3=MID, limit=400,
              where="после сжатия en")

    arrow(d, 580, y3 + h3 / 2, 1020, y3 + h3 / 2, col=MID, wd=4)
    clabel(d, 800, y3 + h3 / 2 - 50, "moderate compression:", 16, MUTE, True,
           where="метка сжатия 1 en", limit=420)
    clabel(d, 800, y3 + h3 / 2 - 28, "JPEG Q75-85, width <=1024 px", 16, MUTE,
           where="метка сжатия 2 en", limit=420)

    clabel(d, CW2 / 2, y3 + h3 + 40,
           "Illustrative example from a comparable case (public sources),"
           " not a measurement on this rig.",
           16, MUTE, where="дисклеймер сжатие en", limit=CW2 - 100)
    return im


save(szhatie_en(), "k4-shema-szhatie-en.png")

report()
