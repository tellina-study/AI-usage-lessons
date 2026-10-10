#!/usr/bin/env python3
"""Схема раздела «Мостик» Семинара 6 — обложка n01.

Рисуется программно (PIL), не описывается словами. Продолжает приём обложки
Семинара 5 (`sem-05/rendered/make_figures_ramka.py` § n01) — тот же
hero-формат (нижняя треть во всю ширину, ≥40% площади слайда). Файл сессии
рамки (n01–n05, n61–n64); `make_figures_mcp.py` / `make_figures_subagent.py`
этой сессией не трогаются.

Круг правок владельца (issue 225, §А1+§А2): прежняя схема («сообщение»
против «факта», с пунктирной стрелкой и незалитой галочкой, плюс ряд оси из
ПЯТИ сегментов, включая «процесс») снята целиком вместе с аркой, которую она
держала. Новая схема рисует новую несущую мысль занятия (см. `n01.md`,
поле `visual.primary`): слева пунктирная карточка «контекст агента» —
«репозиторий» и «разговор с вами», подпись «дальше агент не видит ничего» —
от неё две стрелки к двум белым карточкам справа: «данные снаружи — MCP» и
«своя роль, урезанные права — субагент». Под этой парой — ряд из ЧЕТЫРЁХ
сегментов, не пяти: хук и скилл серые («закрыты в прошлый раз»), MCP и
субагент gold («решаем сегодня»).

  ramka-n01-hero-sem06.png   n01   контекст агента → (две стрелки) →
                                   MCP / субагент; ниже — ось из четырёх
                                   сегментов, без «процесса»

Холст 2400×620 px при вставке во всю ширину канвы (13,333″) даёт высоту
620/2400×13,333 = 3,44″ = 45,9% площади слайда 13,333×7,5 — hero-порог ≥40%
выполнен с тем же запасом, что у Семинара 5 (там 45%).
"""
from fig_toolkit import *

W_PX, H_PX = 2400, 620
# Полотно прижато к низу слайда: по высоте оно занимает доли
# (7.5 - 3.44)/7.5 .. 1.0 — те же координаты подложки, что у Семинара 5.
im = cover_backdrop(W_PX, H_PX, (7.5 - 3.44) / 7.5, 1.0)
d = ImageDraw.Draw(im)

# Приглушённые величины ОТ ПОДЛОЖКИ (см. sem-05 ramka n01 — то же предупреждение:
# фон здесь градиент DEEP→MID→LIGHT, не ровный тёмный, и обычный MUTE/GHOST на
# нём сольётся с фоном справа).
COVER_DIM = (0xC4, 0xD6, 0xE6)
COVER_LINE = (0x9D, 0xBA, 0xD0)

d.line([50, 596, 2350, 596], fill=COVER_LINE, width=4)

# ── Левая пунктирная карточка «контекст агента» ────────────────────────────
CX, CY, CW, CH = 70, 40, 640, 250
bgsample = im.getpixel((CX + CW // 2, CY + CH // 2))
dashbox(d, CX, CY, CW, CH, COVER_LINE, dash=16, gap=10, width=3, bg=bgsample)
clabel(d, CX + CW / 2, CY + 26, "контекст агента", 32, W, b=True,
       where="n01 контекст", limit=CW - 50)
d.line([CX + 40, CY + 78, CX + CW - 40, CY + 78], fill=COVER_LINE, width=2)
clabel(d, CX + CW / 2, CY + 102, "репозиторий", 25, COVER_DIM, b=True,
       where="n01 контекст", limit=CW - 56)
clabel(d, CX + CW / 2, CY + 142, "разговор с вами", 25, COVER_DIM, b=True,
       where="n01 контекст", limit=CW - 56)
for k, ln in enumerate(("дальше агент", "не видит ничего")):
    clabel(d, CX + CW / 2, CY + 190 + k * 26, ln, 19, COVER_DIM,
           where="n01 контекст", limit=CW - 56)

# ── Две стрелки к двум карточкам справа ─────────────────────────────────────
AX1 = CX + CW + 20
AX2 = AX1 + 130
RX = AX2
RW = 820
RH = (CH - 30) / 2
arrow(d, AX1, CY + RH / 2, AX2, CY + RH / 2, col=COVER_LINE, wd=6, head=18)
arrow(d, AX1, CY + RH + 30 + RH / 2, AX2, CY + RH + 30 + RH / 2, col=COVER_LINE, wd=6, head=18)

# ── Правая верхняя карточка «данные снаружи — MCP» ─────────────────────────
d.rounded_rectangle([RX, CY, RX + RW, CY + RH], radius=14, fill=W)
clabel(d, RX + RW / 2, CY + RH / 2 - 34, "данные снаружи", 28, INK, b=True,
       where="n01 MCP-карточка", limit=RW - 48)
clabel(d, RX + RW / 2, CY + RH / 2 + 6, "— MCP", 28, MID, b=True,
       where="n01 MCP-карточка", limit=RW - 48)

# ── Правая нижняя карточка «своя роль, урезанные права — субагент» ─────────
RY2 = CY + RH + 30
d.rounded_rectangle([RX, RY2, RX + RW, RY2 + RH], radius=14, fill=W)
clabel(d, RX + RW / 2, RY2 + RH / 2 - 34, "своя роль, урезанные права", 26, INK, b=True,
       where="n01 субагент-карточка", limit=RW - 48)
clabel(d, RX + RW / 2, RY2 + RH / 2 + 8, "— субагент", 28, MID, b=True,
       where="n01 субагент-карточка", limit=RW - 48)

# ── Ряд оси из ЧЕТЫРЁХ сегментов (issue 225, §А1: пятого — «процесс» — нет) ─
SEGY, SEGH = 330, 220
GAP = 26
SEGW = (2330 - 70 - 3 * GAP) / 4
names = ["хук", "скилл", "MCP", "субагент"]
x = 70
for i, name in enumerate(names):
    if i < 2:
        d.rounded_rectangle([x, SEGY, x + SEGW, SEGY + SEGH], radius=14, fill=GREY_FILL)
        clabel(d, x + SEGW / 2, SEGY + 46, name, 34, GREY_TX, b=True, where="n01 ось")
        for k, ln in enumerate(("закрыты", "в прошлый раз")):
            clabel(d, x + SEGW / 2, SEGY + 128 + k * 30, ln, 19, GREY_TX,
                   where="n01 ось", limit=SEGW - 24)
    else:
        d.rounded_rectangle([x, SEGY, x + SEGW, SEGY + SEGH], radius=14, fill=GOLD)
        clabel(d, x + SEGW / 2, SEGY + 46, name, 34, DEEP, b=True, where="n01 ось")
        for k, ln in enumerate(("решаем", "сегодня")):
            clabel(d, x + SEGW / 2, SEGY + 128 + k * 30, ln, 19, GOLDINK,
                   where="n01 ось", limit=SEGW - 24)
    x += SEGW + GAP

save(im, "ramka-n01-hero-sem06.png")
report()
