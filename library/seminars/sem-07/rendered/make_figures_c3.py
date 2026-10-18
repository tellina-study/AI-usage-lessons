#!/usr/bin/env python3
"""Схема кейса C ступени 1 Семинара 7 (Octomind/LangChain) — «1 класс против 3»,
единственная иллюстрация, которой у этого кейса не было вовсе (`make_figures_
c1/c2/c4/c5/c6/mostik.py` уже существовали, c3 — нет, см. `backup` слайда n17).

    c3-tsena-odnogo-deystviya.png   одно и то же действие (перевод слова на
                                     другой язык) блоками и числами, а не
                                     листингом: слева прямым вызовом модели —
                                     1 класс и 1 вызов функции; справа через
                                     фреймворк — три прямоугольника столбиком
                                     (три новых понятия) и ряд из четырёх
                                     меток вызовов. КОДА НА ЭКРАНЕ НЕТ — прямое
                                     решение владельца по прежней версии
                                     слайда (см. `backup` n17): два блока
                                     питона отдавали под листинг ~60% площади,
                                     и студенческая прожарка того же круга
                                     провалила тест пяти секунд ровно из-за
                                     него.

Числа и три названия понятий — дословно из `visual.primary`/`backup`
`slides/n17-tsena-odnogo-deystviya-odin-protiv-tryoh.md` (которые сверены по
прямому чтению поста Octomind через Wayback Machine): «one class and one
function call» vs «three classes and four function calls»; три новых понятия
— «Prompt templates», «Output parsers», «Chains» (имена классов фреймворка на
экран не выносятся — на уровне пользователя приёма важен счёт сущностей, не
имена; то же решение уже приняла сама сессия слайда).

Тулкит — `fig_toolkit.py` (та же копия, что использует `make_figures_c1.py`/
`make_figures_mostik.py`), не самодостаточный модуль, каким написаны `c4`/
`c5`/`c6`: кейс C рисуется этим кругом технической сборки, а не отдельной
content-сессией, и общий тулкит избавляет от второй копии палитры/шрифтов.

Холст 1600×620 px — та же рабочая ширина 12,23″, что у `make_figures_c1.py`
(130,8 px·дюйм⁻¹), пол кегля деки 7,5 pt = 13,6 px; самый мелкий кегль схемы
проверяется при сохранении через `fig_toolkit.save`/`report()` (пол кегля
печатается, числом, не на глаз).

Запуск: `python3 make_figures_c3.py` (из `rendered/`).
"""
# Общий тулкит схем живёт в `tools/seminar-build/` — одна копия на курс
# (прежде он копировался в папку каждого занятия и копии расходились).
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))

from fig_toolkit import *

CW, CH = 1600, 620

LCX0, LCW = 70, 650          # левая колонка — прямой вызов
RCX0, RCW = 860, 670          # правая колонка — фреймворк


def frame(d, x, y, w, h, *, fill=SURF, stroke=LIGHT, sw=3, r=16):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=stroke, width=sw)


def oval(d, x1, y1, x2, y2, *, fill=MID, stroke=None, w=3):
    d.ellipse([x1, y1, x2, y2], fill=fill, outline=stroke, width=w)


def col_header(d, x0, w, txt, col=MID):
    clabel(d, x0 + w / 2, 72, txt, 23, col, True, where=f"шапка «{txt}»", limit=w - 20)


# ── холст ─────────────────────────────────────────────────────────────────
im = Image.new("RGB", (CW, CH), W)
d = ImageDraw.Draw(im)

head(d, "Одно и то же действие: перевод слова на другой язык", sz=28, col=DEEP, x=40, y=16)

col_header(d, LCX0, LCW, "прямым вызовом модели")
col_header(d, RCX0, RCW, "через фреймворк")

# ── левая колонка: один прямоугольник, один вызов ───────────────────────────
LY, LH = 112, 300
frame(d, LCX0, LY, LCW, LH, fill=W, stroke=MID, sw=4)
clabel(d, LCX0 + LCW / 2, LY + 40, "1 класс", 46, DEEP, True, where="левый блок · 1 класс",
       limit=LCW - 60)
clabel(d, LCX0 + LCW / 2, LY + 118, "1 вызов функции", 25, MID, True,
       where="левый блок · 1 вызов", limit=LCW - 60)
clabel(d, LCX0 + LCW / 2, LY + 170, "— создать клиента, передать сообщения,", 19, MUTE,
       where="левый блок · пояснение 1", limit=LCW - 60)
clabel(d, LCX0 + LCW / 2, LY + 196, "забрать текст ответа", 19, MUTE,
       where="левый блок · пояснение 2", limit=LCW - 60)
clabel(d, LCX0 + LCW / 2, LY + 246, "дальше — обычный код на обычном языке", 19, LIGHT, True,
       where="левый блок · подпись", limit=LCW - 60)

# ── правая колонка: три прямоугольника столбиком — три новых понятия ───────
RY0, RBH, RGAP = 112, 84, 14
PONYATIYA = ("шаблон промпта", "парсер вывода", "«цепочка»")
for i, name in enumerate(PONYATIYA):
    ry = RY0 + i * (RBH + RGAP)
    frame(d, RCX0, ry, RCW - 190, RBH, fill=WARM, stroke=GOLD, sw=3, r=14)
    clabel(d, RCX0 + (RCW - 190) / 2, ry + RBH / 2 - 15, name, 25, GOLDINK, True,
           where=f"правый блок · {name}", limit=RCW - 230)
    clabel(d, RCX0 + (RCW - 190) / 2, ry + RBH / 2 + 13, f"новое понятие {i + 1} из 3", 16,
           MUTE, where=f"правый блок · подпись {name}", limit=RCW - 230)

# ряд из четырёх меток вызовов — узкая колонка справа от трёх прямоугольников,
# по высоте выровнена с блоком из трёх прямоугольников (112…392)
MX = RCX0 + (RCW - 190) + 30
MW = 160
for i in range(4):
    cy = RY0 + 40 + i * 70
    oval(d, MX + MW / 2 - 24, cy - 24, MX + MW / 2 + 24, cy + 24, fill=MID)
    clabel(d, MX + MW / 2, cy - 13, str(i + 1), 22, W, True, where=f"метка вызова {i + 1}")
clabel(d, MX + MW / 2, RY0 + 40 + 3 * 70 + 36, "4 вызова", 18, MID, True,
       where="метки · итог", limit=MW)

# ── разделитель колонок ──────────────────────────────────────────────────
dx = (LCX0 + LCW + RCX0) / 2
d.line([dx, 104, dx, 430], fill=SOFT_GREY, width=3)
clabel(d, dx, 250, "против", 18, MUTE, True, where="разделитель")

# ── итоговые числа под каждой стороной ──────────────────────────────────
IY = 460
clabel(d, LCX0 + LCW / 2, IY, "1 класс · 1 вызов функции", 28, DEEP, True,
       where="итог слева", limit=LCW)
clabel(d, RCX0 + RCW / 2, IY, "3 класса · 4 вызова · 3 новых понятия", 27, GOLDINK, True,
       where="итог справа", limit=RCW)

# ── подвал: что на экране нет ────────────────────────────────────────────
clabel(d, CW / 2, 540, "Листинга кода на экране нет — только счёт сущностей.", 20, MUTE,
       where="подвал")

save(im, "c3-tsena-odnogo-deystviya.png")
report()
