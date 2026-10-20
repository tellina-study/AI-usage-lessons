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

report()
