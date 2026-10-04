#!/usr/bin/env python3
"""Схема раздела «Мостик» Семинара 6 — обложка n01.

Рисуется программно (PIL), не описывается словами. Продолжает приём обложки
Семинара 5 (`sem-05/rendered/make_figures_ramka.py` § n01) — тот же
hero-формат (нижняя треть во всю ширину, ≥40% площади слайда), но контент
свой: n01.md Семинара 6 просит не «просьбу → хук/скилл/MCP/…», а «сообщение
против факта» + ряд оси из пяти сегментов. Файл сессии рамки (n01–n05),
`make_figures_mcp.py` / `make_figures_subagent.py` этой сессией не трогаются.

  ramka-n01-hero-sem06.png   n01   карточка «сообщение» → пунктирная стрелка
                                   со знаком вопроса → карточка «факт»;
                                   под парой — ряд оси из пяти сегментов

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

# ── Левая карточка «сообщение» ────────────────────────────────────────────
MX, MY, MW_, MH = 90, 46, 520, 230
d.rounded_rectangle([MX, MY, MX + MW_, MY + MH], radius=14, fill=W)
clabel(d, MX + MW_ / 2, MY + 20, "сообщение", 32, INK, b=True, where="n01 сообщение",
       limit=MW_ - 40)
d.line([MX + 40, MY + 74, MX + MW_ - 40, MY + 74], fill=(0xC6, 0xD5, 0xE2), width=2)
clabel(d, MX + MW_ / 2, MY + 98, "сервер: «подключено»", 25, MID, b=True,
       where="n01 сообщение", limit=MW_ - 48)
clabel(d, MX + MW_ / 2, MY + 138, "роль: «сделано»", 25, MID, b=True,
       where="n01 сообщение", limit=MW_ - 48)
clabel(d, MX + MW_ / 2, MY + 186, "— обе сообщили о себе сами", 20, MUTE,
       where="n01 сообщение", limit=MW_ - 48)

# ── Пунктирная стрелка со знаком вопроса ──────────────────────────────────
AX1, AX2, AY = MX + MW_ + 30, MX + MW_ + 310, MY + MH / 2
arrow(d, AX1, AY, AX2, AY, col=COVER_LINE, wd=6, head=20, dash=True)
clabel(d, (AX1 + AX2) / 2, AY - 56, "?", 46, GOLD, b=True, where="n01 вопрос")

# ── Правая карточка «факт» ────────────────────────────────────────────────
FX = AX2 + 30
FW_ = 520
d.rounded_rectangle([FX, MY, FX + FW_, MY + MH], radius=14, fill=W)
clabel(d, FX + FW_ / 2, MY + 20, "факт", 32, INK, b=True, where="n01 факт", limit=FW_ - 40)
check_outline(d, FX + FW_ / 2, MY + 128, 34, (0x9D, 0xB2, 0xC4))
# незалитая галочка — приглушённый, но читаемый контур: видна, но
# демонстративно «не подтверждена» (вопрос задаётся, не отвечается)
d.line([FX + 40, MY + 74, FX + FW_ - 40, MY + 74], fill=(0xC6, 0xD5, 0xE2), width=2)
clabel(d, FX + FW_ / 2, MY + 188, "проверено независимо от сообщения?", 20, MUTE,
       where="n01 факт", limit=FW_ - 48)

# ── Ряд оси из пяти сегментов ──────────────────────────────────────────────
SEGY, SEGH = 330, 220
GAP = 26
SEGW = (2330 - 70 - 4 * GAP) / 5
names = ["хук", "скилл", "MCP", "субагент", "процесс"]
x = 70
for i, name in enumerate(names):
    if i < 2:
        d.rounded_rectangle([x, SEGY, x + SEGW, SEGY + SEGH], radius=14, fill=GREY_FILL)
        clabel(d, x + SEGW / 2, SEGY + 46, name, 34, GREY_TX, b=True, where="n01 ось")
        for k, ln in enumerate(("закрыты", "в прошлый раз")):
            clabel(d, x + SEGW / 2, SEGY + 128 + k * 30, ln, 19, GREY_TX,
                   where="n01 ось", limit=SEGW - 24)
    elif i < 4:
        d.rounded_rectangle([x, SEGY, x + SEGW, SEGY + SEGH], radius=14, fill=GOLD)
        lock(d, x + SEGW / 2, SEGY + 30, 24, DEEP)
        clabel(d, x + SEGW / 2, SEGY + 96, name, 34, DEEP, b=True, where="n01 ось")
        for k, ln in enumerate(("сегодня —", "две из пяти")):
            clabel(d, x + SEGW / 2, SEGY + 150 + k * 28, ln, 19, GOLDINK,
                   where="n01 ось", limit=SEGW - 24)
    else:
        bgsample = im.getpixel((int(x + SEGW / 2), int(SEGY + SEGH / 2)))
        dashbox(d, x, SEGY, SEGW, SEGH, COVER_LINE, dash=16, gap=10, width=3, bg=bgsample)
        clabel(d, x + SEGW / 2, SEGY + 46, name, 34, COVER_DIM, b=True, where="n01 ось")
        clabel(d, x + SEGW / 2, SEGY + 128, "впереди", 19, COVER_DIM, where="n01 ось")
    x += SEGW + GAP

save(im, "ramka-n01-hero-sem06.png")
report()
