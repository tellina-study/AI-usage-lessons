#!/usr/bin/env python3
"""Кейс «Одобрение возврата» Семинара 8 (issue #274) — 2 новые схемы (в
дополнение к уже принятой `k3-shema-dva-protsessa-a-b.png` из
`make_figures_c3.py`, которая этим файлом НЕ трогается).

    k3-shema-versii.png    слой 1: ДВЕ горизонтальные полосы (не колонки —
                            это одна и та же цепочка во времени, не два
                            параллельных пути): общий префикс (форма →
                            извлечение суммы) → развилка на последнем узле →
                            версия 1 (модель решает по тексту правила, 9
                            ошибок из 101, все на границе 3000₽) → ВРЕМЯ →
                            версия 2 (`IF`-узел сравнивает число, 0 ошибок
                            из 101). Геометрия — по образцу
                            `make_figures_c3.py` (общий вход сверху, frame +
                            clabel), развёрнуто в две строки вместо двух
                            столбцов.
    k3-n8n-if-uzel.png     слой 2 (n8n-стиль): узел `IF` «Amount over
                            threshold?» версии 2 рядом с узлом `chainLlm`
                            «Decide refund (model)» версии 1 — для контраста
                            конфигурации.

Числа и формулировки — дословно `SETKA-KEYSOV-S8-part2.md` «Кейс 3 —
Одобрение возврата» и `BRIEF-PROIZVODSTVO.md` §3. Слой 2 — не снимок живого
UI n8n, недостижим в этой среде, см. `notes/mcp-limitations.md` [#233-8].

Запуск: `python3 make_figures_k3.py` (из `rendered/`).
"""
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))

from fig_toolkit import *
from n8n_canvas_kit import node_n8n, arrow_n8n, legend_n8n, disclaimer

CW = 1600


def frame(d, x, y, w, h, *, fill=SURF, stroke=LIGHT, sw=3, r=14):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=stroke, width=sw)


def two_lines(d, cx, cy, top, bottom, *, tsz=21, bsz=15, tcol=DEEP, bcol=MUTE, tb=True,
              limit=None, where="?"):
    ft, fb = f(tsz, tb), f(bsz)
    if limit:
        fit(d, top, ft, limit, f"{where} · верх")
        fit(d, bottom, fb, limit, f"{where} · низ")
    th = tsz + bsz + 10
    y = cy - th / 2
    d.text((cx - d.textlength(top, font=ft) / 2, y), top, font=ft, fill=tcol)
    d.text((cx - d.textlength(bottom, font=fb) / 2, y + tsz + 8), bottom, font=fb, fill=bcol)


# ── слой 1: две полосы, последовательные во времени ─────────────────────────
def shema_versii():
    CH = 700
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Одна цепочка, две версии последнего узла — не параллельно, а во времени",
         sz=24, x=40, y=16)

    # общий префикс
    PX0, PW, PY, PH = 40, 980, 70, 90
    frame(d, PX0, PY, 460, PH, fill=SURF, stroke=LIGHT)
    two_lines(d, PX0 + 230, PY + PH / 2, "Форма", "запрос на возврат",
              limit=420, where="префикс · форма")
    frame(d, PX0 + 520, PY, 460, PH, fill=SURF, stroke=LIGHT)
    two_lines(d, PX0 + 520 + 230, PY + PH / 2, "Извлечение суммы", "модель читает текст запроса",
              limit=420, where="префикс · извлечение")
    arrow(d, PX0 + 460, PY + PH / 2, PX0 + 520, PY + PH / 2, col=MID, wd=4)

    arrow(d, PX0 + 500, PY + PH, PX0 + 500, 230, col=MID, wd=4)

    # ── полоса версии 1 (выше, раньше по времени) ──────────────────────────
    R1Y = 250
    frame(d, 40, R1Y, 560, 120, fill=WARM, stroke=GOLD)
    two_lines(d, 40 + 280, R1Y + 60, "Версия 1 — модель решает по тексту правила",
              "qwen/qwen-2.5-7b-instruct, промпт с порогом 3000₽", tsz=19, bsz=14,
              tcol=GOLDINK, bcol=GOLDINK, limit=520, where="полоса 1 · заголовок")
    arrow(d, 600, R1Y + 60, 660, R1Y + 60, col=GOLD, wd=4)
    frame(d, 660, R1Y, 500, 120, fill=W, stroke=GOLD, sw=4)
    clabel(d, 660 + 250, R1Y + 36, "9 ошибок из 101", 26, GOLDINK, True,
           where="итог версия 1", limit=460)
    clabel(d, 660 + 250, R1Y + 76, "все — на сумме, ровно равной 3000₽", 16, MUTE,
           where="итог версия 1 детали", limit=460)

    # ── стрелка времени между полосами ──────────────────────────────────────
    TY = 400
    arrow(d, 300, R1Y + 120, 300, TY + 28, col=MUTE, wd=3)
    clabel(d, CW / 2, TY, "месяц в работе → эксперимент нашёл границу → версия 2", 19, MUTE,
           True, where="стрелка времени", limit=CW - 140)

    # ── полоса версии 2 (ниже, позже по времени) ────────────────────────────
    R2Y = TY + 60
    frame(d, 40, R2Y, 560, 120, fill=PALE, stroke=MID)
    two_lines(d, 40 + 280, R2Y + 60, "Версия 2 — узел IF сравнивает число",
              "условие над уже извлечённой суммой", tsz=19, bsz=14,
              limit=520, where="полоса 2 · заголовок")
    arrow(d, 600, R2Y + 60, 660, R2Y + 60, col=MID, wd=4)
    frame(d, 660, R2Y, 500, 120, fill=SURF, stroke=TEAL, sw=4)
    clabel(d, 660 + 250, R2Y + 36, "0 ошибок из 101", 26, MID, True,
           where="итог версия 2", limit=460)
    clabel(d, 660 + 250, R2Y + 76, "включая ту же сумму на границе", 16, MUTE,
           where="итог версия 2 детали", limit=460)

    clabel(d, CW / 2, R2Y + 170, "Версия 2 — прямой ответ на находку эксперимента версии 1.",
           21, DEEP, True, where="подпись-итог", limit=CW - 120)
    return im


save(shema_versii(), "k3-shema-versii.png")


# ── слой 2: n8n-стиль, IF рядом с chainLlm для контраста ───────────────────
def if_uzel():
    CH = 540
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Слой 2 — узел n8n: версия 2 (IF) рядом с версией 1 (модель)",
         sz=24, x=40, y=16)

    clabel(d, 330, 70, "версия 2", 19, MID, True, where="заголовок версия 2", limit=600)
    clabel(d, 1230, 70, "версия 1 — для контраста", 19, GOLDINK, True,
           where="заголовок версия 1", limit=600)

    CY = 260
    node_n8n(d, 40, CY - 110, 580, 220,
              "Amount over threshold?",
              "условие: сумма (число) строго больше 3000",
              kind="code", subtype="IF", body_sz=16, where="узел IF версии 2")

    node_n8n(d, 760, CY - 130, 800, 260,
              "Decide refund (model)",
              ["«Правило: не возвращай больше 3000 рублей автоматически, иначе эскалируй",
               "руководителю. Сумма запроса: {{сумма}} рублей. Ответь строго одним словом:",
               "«одобрить» или «эскалировать».»"],
              kind="model", subtype="chainLlm · qwen/qwen-2.5-7b-instruct", body_sz=15,
              where="узел модели версии 1")

    legend_n8n(d, 40, CY + 170)
    disclaimer(d, CW / 2, CY + 210)
    return im


save(if_uzel(), "k3-n8n-if-uzel.png")


# ── EN companion of слой 1 (issue #274, EN track n30b) ──────────────────────
# Параметризация через отдельную функцию, не через --lang/fig_strings_en.py:
# тот словарь общий на все четыре рисовалки кейсов занятия, и его правка из
# зоны одного переводчика (Кейс 3) рисковала бы столкнуться с параллельными
# переводчиками других кейсов, правящими тот же файл в то же время. Имя файла
# задаётся явно в save(), а не языковым патчем `_save` — он подменяет имя
# только когда LANG == "en" (а здесь LANG остаётся "ru", схема просто рисуется
# английскими строками напрямую), поэтому литеральное имя ниже доходит до
# диска как есть.
def shema_versii_en():
    CH = 700
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "One chain, two versions of the last node — not parallel, but in time",
         sz=24, x=40, y=16)

    PX0, PW, PY, PH = 40, 980, 70, 90
    frame(d, PX0, PY, 460, PH, fill=SURF, stroke=LIGHT)
    two_lines(d, PX0 + 230, PY + PH / 2, "Form", "refund request",
              limit=420, where="prefix · form")
    frame(d, PX0 + 520, PY, 460, PH, fill=SURF, stroke=LIGHT)
    two_lines(d, PX0 + 520 + 230, PY + PH / 2, "Amount extraction", "model reads the request text",
              limit=420, where="prefix · extraction")
    arrow(d, PX0 + 460, PY + PH / 2, PX0 + 520, PY + PH / 2, col=MID, wd=4)

    arrow(d, PX0 + 500, PY + PH, PX0 + 500, 230, col=MID, wd=4)

    R1Y = 250
    frame(d, 40, R1Y, 560, 120, fill=WARM, stroke=GOLD)
    two_lines(d, 40 + 280, R1Y + 60, "Version 1 — model decides from the rule text",
              "qwen/qwen-2.5-7b-instruct, prompt with a 3,000-RUB threshold", tsz=19, bsz=14,
              tcol=GOLDINK, bcol=GOLDINK, limit=520, where="band 1 · title")
    arrow(d, 600, R1Y + 60, 660, R1Y + 60, col=GOLD, wd=4)
    frame(d, 660, R1Y, 500, 120, fill=W, stroke=GOLD, sw=4)
    clabel(d, 660 + 250, R1Y + 36, "9 errors out of 101", 26, GOLDINK, True,
           where="result version 1", limit=460)
    clabel(d, 660 + 250, R1Y + 76, "all — on the amount exactly equal to 3,000 RUB", 16, MUTE,
           where="result version 1 detail", limit=460)

    TY = 400
    arrow(d, 300, R1Y + 120, 300, TY + 28, col=MUTE, wd=3)
    clabel(d, CW / 2, TY, "a month in production → the experiment found the boundary → version 2", 19, MUTE,
           True, where="time arrow", limit=CW - 140)

    R2Y = TY + 60
    frame(d, 40, R2Y, 560, 120, fill=PALE, stroke=MID)
    two_lines(d, 40 + 280, R2Y + 60, "Version 2 — IF node compares the number",
              "a condition over the already-extracted amount", tsz=19, bsz=14,
              limit=520, where="band 2 · title")
    arrow(d, 600, R2Y + 60, 660, R2Y + 60, col=MID, wd=4)
    frame(d, 660, R2Y, 500, 120, fill=SURF, stroke=TEAL, sw=4)
    clabel(d, 660 + 250, R2Y + 36, "0 errors out of 101", 26, MID, True,
           where="result version 2", limit=460)
    clabel(d, 660 + 250, R2Y + 76, "including that same amount on the boundary", 16, MUTE,
           where="result version 2 detail", limit=460)

    clabel(d, CW / 2, R2Y + 170, "Version 2 is a direct answer to what the version-1 experiment found.",
           21, DEEP, True, where="closing caption", limit=CW - 120)
    return im


save(shema_versii_en(), "k3-shema-versii-en.png")


# ── что сервис jev умеет ответить, и решающий тест (n30a) ───────────────────
#
# Волна 2б «конфетки» (issue #292, план §4.11). Слайд n30a был четырьмя
# абзацами подряд — «предложенная идея», «что показала проверка», «чем это
# отличается от калькулятора», «урок», — то есть текстовой стеной, в которой
# несущее (у сервиса нет ответа-числа, и две суммы по разные стороны порога
# получили один и тот же ответ) приходилось искать глазами. Схема показывает
# ровно эти две вещи: перечень того, что сервис УМЕЕТ, с перечёркнутой пятой
# позицией — и решающий тест.
#
# Числа и перечень типов ответа — из протокола трёх реальных вызовов
# `stend/jev-extraction-diagnostics.json`, не из описания сервиса: четыре типа
# (`noul`/`choice`/`score`/`box`), суммы 2999 и 3001 руб., один и тот же
# диапазон шкалы на обе. Единица — «руб.», как во всей деке; знак ₽ не
# используется (`notes/mcp-limitations.md` [#274-1]).
def jev_tipy_otveta():
    CH = 640
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)

    clabel(d, CW / 2, 24, "Что сервис умеет вернуть", 22, DEEP, True,
           where="заголовок ряда типов", limit=CW - 80)

    cards = [("да или нет", "с вероятностью"),
             ("выбор", "одного из перечня"),
             ("позиция", "на заданной шкале"),
             ("область", "на картинке")]
    y, h = 72, 132
    bw, gap = 272, 20
    x = 40
    for top, bottom in cards:
        frame(d, x, y, bw, h, fill=PALE, stroke=MID)
        two_lines(d, x + bw / 2, y + h / 2, top, bottom, tsz=22, bsz=16,
                  tcol=DEEP, bcol=MID, limit=bw - 36, where=f"тип ответа · {top}")
        x += bw + gap

    # Пятая позиция — не «ещё один тип», а отсутствие типа. Поэтому она
    # нарисована пунктиром и перечёркнута, а не просто подписана серым:
    # перечёркнутое читается как «этого нет» с одного взгляда.
    dashbox(d, x, y, bw, h, GREY_FILL, width=3, r=14)
    two_lines(d, x + bw / 2, y + h / 2 - 8, "открытое число", "такого ответа нет",
              tsz=22, bsz=16, tcol=GREY_TX, bcol=RED, limit=bw - 36,
              where="тип ответа · число")
    xmark(d, x + bw / 2, y + h - 22, 20, col=RED, wd=4)

    clabel(d, CW / 2, 268, "Решающий тест: две суммы по разные стороны порога 3000 руб.",
           22, DEEP, True, where="заголовок теста", limit=CW - 80)

    sy, sh_, sw_ = 330, 112, 300
    frame(d, 120, sy, sw_, sh_, fill=WARM, stroke=GOLD, sw=4)
    two_lines(d, 120 + sw_ / 2, sy + sh_ / 2, "2999 руб.", "ниже порога",
              tsz=28, bsz=16, tcol=GOLDINK, bcol=GOLDINK, limit=sw_ - 36,
              where="сумма 2999")
    frame(d, CW - 420, sy, sw_, sh_, fill=WARM, stroke=GOLD, sw=4)
    two_lines(d, CW - 420 + sw_ / 2, sy + sh_ / 2, "3001 руб.", "выше порога",
              tsz=28, bsz=16, tcol=GOLDINK, bcol=GOLDINK, limit=sw_ - 36,
              where="сумма 3001")

    frame(d, 540, sy - 4, 520, sh_ + 8, fill=SURF, stroke=LIGHT, sw=4)
    two_lines(d, 800, sy + sh_ / 2, "один и тот же диапазон",
              "и полная уверенность в обоих случаях", tsz=22, bsz=16,
              tcol=MID, bcol=MUTE, limit=480, where="ответ сервиса")
    arrow(d, 420, sy + sh_ / 2, 540, sy + sh_ / 2, col=MID, wd=5)
    arrow(d, CW - 420, sy + sh_ / 2, 1060, sy + sh_ / 2, col=MID, wd=5)

    clabel(d, CW / 2, 500, "Сервис их не различил.", 24, RED, True,
           where="вывод теста", limit=CW - 120)
    clabel(d, CW / 2, 546,
           "Различить можно было бы, только зашив границу 3000 в сам вопрос — "
           "то есть зная порог заранее,",
           18, MUTE, where="вывод теста 2", limit=CW - 120)
    clabel(d, CW / 2, 576, "ровно как в тексте правила, которое мы и пытаемся обойти.",
           18, MUTE, where="вывод теста 3", limit=CW - 120)
    return im


save(jev_tipy_otveta(), "k3-jev-tipy-otveta.png")

report()
