#!/usr/bin/env python3
"""Главная схема занятия — Кейс 3 Семинара 8 (issue #274): два параллельных
процесса на ОДНОМ и том же извлечённом значении суммы, решение о пороге X
принимает либо модель, либо код.

    k3-shema-dva-protsessa-a-b.png   одна сумма сверху (3000₽, извлечена
                                     заранее — модель здесь не участвует),
                                     дальше два столбца: слева процесс (A) —
                                     модель читает текст правила и решает
                                     сама; справа процесс (B) — `IF`-узел
                                     сравнивает число с порогом. Внизу —
                                     противоположные решения и итоговый счёт
                                     эксперимента (3 ошибки из 51 у (A), 0 у
                                     (B)). Принципиальная схема, НЕ снимок
                                     интерфейса n8n — живой UI для этого
                                     стенда недостижим (BRIEF-PROIZVODSTVO.md
                                     §3, notes/mcp-limitations.md [#233-8]).

Числа и формулировки — дословно `slides/n27-k3-reshenie-demo.md` и
`SETKA-KEYSOV-S8.md` (раздел «Кейс 3», подтверждено оркестратором прямым
чтением `runData` executions 72/74/92/73/75/93 на стенде 2026-10-18, не
пересказ).

Геометрия и тулкит — по образцу `sem-07/rendered/make_figures_c3.py` (та же
форма «два столбца с разделителем и итогом снизу», другое содержание).

Запуск: `python3 make_figures_c3.py` (из `rendered/` папки Семинара 8).
"""
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))

from fig_toolkit import *

CW, CH = 1600, 700

LCX0, LCW = 70, 700           # левая колонка — процесс (A), модель
RCX0, RCW = 830, 700           # правая колонка — процесс (B), код


def frame(d, x, y, w, h, *, fill=SURF, stroke=LIGHT, sw=3, r=16):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=stroke, width=sw)


def col_header(d, x0, w, txt, col=MID):
    clabel(d, x0 + w / 2, 118, txt, 23, col, True, where=f"шапка «{txt}»", limit=w - 20)


im = Image.new("RGB", (CW, CH), W)
d = ImageDraw.Draw(im)

head(d, "Один порог, два параллельных процесса", sz=28, col=DEEP, x=40, y=16)

# ── общий вход сверху: одна и та же извлечённая сумма ──────────────────────
TOPX0, TOPW, TOPY, TOPH = (CW - 620) / 2, 620, 54, 52
frame(d, TOPX0, TOPY, TOPW, TOPH, fill=WARM, stroke=GOLD, sw=4, r=14)
clabel(d, TOPX0 + TOPW / 2, TOPY + TOPH / 2 - 14, "извлечённая сумма — 3000₽ (порог X)",
       22, GOLDINK, True, where="общий вход", limit=TOPW - 40)

# стрелки вниз к каждому столбцу
arrow(d, TOPX0 + TOPW * 0.2, TOPY + TOPH, LCX0 + LCW / 2, 150, col=MID, wd=4)
arrow(d, TOPX0 + TOPW * 0.8, TOPY + TOPH, RCX0 + RCW / 2, 150, col=MID, wd=4)

col_header(d, LCX0, LCW, "(A) — решение принимает модель")
col_header(d, RCX0, RCW, "(B) — решение принимает код")

# ── левая колонка: модель читает текст правила ──────────────────────────
LY, LH = 160, 150
frame(d, LCX0, LY, LCW, LH, fill=W, stroke=MID, sw=4)
clabel(d, LCX0 + LCW / 2, LY + 34, "Model (decision, Qwen2.5)", 24, DEEP, True,
       where="левый блок · узел", limit=LCW - 60)
clabel(d, LCX0 + LCW / 2, LY + 76, "промт: «не возвращай больше суммы X,", 18, MUTE,
       where="левый блок · правило 1", limit=LCW - 60)
clabel(d, LCX0 + LCW / 2, LY + 102, "иначе эскалируй»", 18, MUTE,
       where="левый блок · правило 2", limit=LCW - 60)

arrow(d, LCX0 + LCW / 2, LY + LH, LCX0 + LCW / 2, LY + LH + 60, col=MID, wd=4)

LY2 = LY + LH + 70
frame(d, LCX0, LY2, LCW, 110, fill=WARM, stroke=GOLD, sw=4, r=14)
clabel(d, LCX0 + LCW / 2, LY2 + 34, "решение: «эскалировать»", 26, GOLDINK, True,
       where="левый блок · решение", limit=LCW - 60)
clabel(d, LCX0 + LCW / 2, LY2 + 74, "на сумме, равной X включительно", 18, MUTE,
       where="левый блок · пояснение", limit=LCW - 60)

# ── правая колонка: IF-узел сравнивает число ────────────────────────────
RY, RH = 160, 150
frame(d, RCX0, RY, RCW, RH, fill=W, stroke=MID, sw=4)
clabel(d, RCX0 + RCW / 2, RY + 34, "Amount over threshold? (IF)", 24, DEEP, True,
       where="правый блок · узел", limit=RCW - 60)
clabel(d, RCX0 + RCW / 2, RY + 76, "условие: сумма строго больше X", 18, MUTE,
       where="правый блок · правило 1", limit=RCW - 60)
clabel(d, RCX0 + RCW / 2, RY + 102, "— числовое, не текстовое", 18, MUTE,
       where="правый блок · правило 2", limit=RCW - 60)

arrow(d, RCX0 + RCW / 2, RY + RH, RCX0 + RCW / 2, RY + RH + 60, col=MID, wd=4)

RY2 = RY + RH + 70
frame(d, RCX0, RY2, RCW, 110, fill=SURF, stroke=TEAL, sw=4, r=14)
clabel(d, RCX0 + RCW / 2, RY2 + 34, "решение: «одобрить»", 26, MID, True,
       where="правый блок · решение", limit=RCW - 60)
clabel(d, RCX0 + RCW / 2, RY2 + 74, "на той же сумме, включая X", 18, MUTE,
       where="правый блок · пояснение", limit=RCW - 60)

# ── разделитель колонок ──────────────────────────────────────────────────
dx = (LCX0 + LCW + RCX0) / 2
d.line([dx, 150, dx, 500], fill=SOFT_GREY, width=3)
clabel(d, dx, 320, "против", 18, MUTE, True, where="разделитель")

# ── execution id под каждым столбцом ────────────────────────────────────
EY = 500
clabel(d, LCX0 + LCW / 2, EY, "execution 72 · 74 · 92", 20, MUTE, True,
       where="execution id · A", limit=LCW)
clabel(d, RCX0 + RCW / 2, EY, "execution 73 · 75 · 93", 20, MUTE, True,
       where="execution id · B", limit=RCW)

# ── итоговый счёт эксперимента ──────────────────────────────────────────
IY = 560
clabel(d, LCX0 + LCW / 2, IY, "3 ошибки из 51 — все на сумме 3000₽", 27, GOLDINK, True,
       where="итог слева", limit=LCW)
clabel(d, RCX0 + RCW / 2, IY, "0 ошибок из 51", 27, MID, True,
       where="итог справа", limit=RCW)

clabel(d, CW / 2, 640, "Принципиальная схема: имена узлов и условие — настоящие, со стенда.",
       20, MUTE, where="подвал")

save(im, "k3-shema-dva-protsessa-a-b.png")
report()
