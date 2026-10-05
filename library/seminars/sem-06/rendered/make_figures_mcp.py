#!/usr/bin/env python3
"""Схемы раздела «MCP» Семинара 6 — замена таблиц на n12, n13, n14, n29.

Рисуются программно (PIL). Четыре из шести разобранных слайдов — таблица
держит работу схемы (n08, n21 — ИСКЛЮЧЕНИЯ, обоснование ниже и в
VIZUAL-OTCHET.md). Холст 1600 px = 12,23″ рабочей ширины слайда, как в
`make_figures_subagent.py`.

  mcp-n12-oblasti.png          n12   слоёная схема трёх областей видимости
  mcp-n13-prioritet.png        n13   вертикальная лестница приоритета (к коду)
  mcp-n14-dolya-okna.png       n14   пропорция окна + сравнение цены действия
  mcp-n29-tsepochka.png        n29   короткая цепочка доверия по имени

n08 (`base_and_edge`) и n21 (`mechanics_table`, уже две читаемые таблицы —
см. поправку оркестратора) НЕ тронуты: обоснование — в VIZUAL-OTCHET.md.
"""
from fig_toolkit import *

MW = 1600
CODEBG = (0x16, 0x1C, 0x30)


def mtext(d, x, y, t, sz=23, col=INK, b=False, m=False):
    fo = f(sz, b, m)
    d.text((x, y), t, font=fo, fill=col)
    return d.textlength(t, font=fo)


def mcent(d, y, t, sz=23, col=INK, b=False, w=MW, x0=0):
    fo = f(sz, b)
    d.text((x0 + (w - d.textlength(t, font=fo)) // 2, y), t, font=fo, fill=col)


def mpanel(d, x, y, w, h, title=None, *, fill=SURF, stroke=LIGHT, tsz=20, tcol=DEEP, r=12, sw=3):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=stroke, width=sw)
    if title:
        d.text((x + 16, y + 10), title, font=f(tsz, True), fill=tcol)


def msave(im, name):
    im.save(OUT / name)
    print("  ", name, im.size)


# ═══════════════════════════════════════════════════════════════════════════
# n12 — слоёная схема трёх областей видимости
# ═══════════════════════════════════════════════════════════════════════════
H12 = 700
im = Image.new("RGB", (MW, H12), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "Ключ — в переменную окружения. Файл конфигурации — в одну из трёх областей", 24, DEEP, b=True)

mpanel(d, 20, 54, MW - 40, 64, None, fill=SURF, stroke=TEAL)
mtext(d, 42, 68, "Ход 3 — где хранить ключ?", 20, TEAL, b=True)
mtext(d, 420, 68, "переменная окружения, не значение в файле", 20, INK)

mtext(d, 20, 128, "Ход 4 — куда положить сам файл?", 21, MID, b=True)

LAYERS = [
    ("local", "только у меня на этой машине", "непроверенный эксперимент", MUTE, SURF, False),
    ("project", "в репозиторий, для всех", "проверенный сервер — конфигурация становится кодом,\nизменение видно в ревью", TEAL, (0xE0, 0xF1, 0xF2), False),
    ("user", "глобально во всех моих проектах", "личные инструменты, не специфичные для проекта", MUTE, SURF, False),
]
LY, LH, LGAP = 166, 118, 16
LX, LW_ = 20, MW - 40
y = LY
for i, (name, where, when, col, fillc, _unused) in enumerate(LAYERS):
    is_default = (name == "local")
    stroke_c = GOLD if is_default else col
    mpanel(d, LX, y, LW_, LH, None, fill=fillc, stroke=stroke_c, sw=4 if is_default else 3)
    d.rounded_rectangle([LX + 18, y + 16, LX + 210, y + LH - 16], radius=10,
                        fill=GOLD if is_default else col)
    nm_col = DEEP if is_default else W
    nw = d.textlength(name, font=f(24, True, m=True))
    d.text((LX + 18 + (192 - nw) / 2, y + LH / 2 - 15), name, font=f(24, True, m=True), fill=nm_col)
    mtext(d, LX + 234, y + 16, where, 20, DEEP, b=True)
    for k, ln in enumerate(when.split("\n")):
        mtext(d, LX + 234, y + 48 + k * 24, ln, 17, MUTE)
    if is_default:
        bw = d.textlength("дефолт команды подключения", font=f(15, True))
        d.rounded_rectangle([LX + LW_ - bw - 48, y + 14, LX + LW_ - 14, y + 42], radius=8, fill=GOLD)
        d.text((LX + LW_ - bw - 34, y + 19), "дефолт команды подключения", font=f(15, True), fill=DEEP)
    y += LH + LGAP

mpanel(d, 20, y + 6, MW - 40, 84, None, fill=(0xFD, 0xF3, 0xD6), stroke=GOLD)
for k, ln in enumerate(["Дефолт команды подключения кладёт сервер в local, не в project. Если про это не",
                        "знать — получится разговор «я подключил, всё работает» — «а у меня нет», и оба правы."]):
    mtext(d, 44, y + 20 + k * 26, ln, 19, GOLDINK, b=True)
im = im.crop((0, 0, MW, y + 100))
msave(im, "mcp-n12-oblasti.png")


# ═══════════════════════════════════════════════════════════════════════════
# n13 — лестница приоритета (компаньон к коду .mcp.json)
#
# Порядок правок круга после прожарок (issue 225, P1-1): старая лестница
# несла два взаимоисключающих утверждения на одном экране — ступень 1
# (политика организации) подписана «выше всех», ступень 6, самая НИЖНЯЯ
# (local) подписана «ПОБЕЖДАЕТ при конфликте». Источник
# (sem-05/research/mechanics-5-mcp.md §1.3, дословно из документации
# «Scope hierarchy and precedence»): порядок от высшего к низшему —
# local → project → user → сервер из плагина → коннектор; ОТДЕЛЬНО, поверх
# всех пяти, стоит политика организации, которая побеждает даже local. Было
# нарисовано задом наперёд среди пяти обычных уровней: local стояла внизу
# лестницы вместо второй сверху. Починка — переставить local на ступень 2,
# сразу под золотой org-policy, остальные четыре — по тому же порядку
# источника (project → user → плагин → коннектор). Теперь читается без
# противоречия: 1 бьёт всех, 2 бьёт всех остальных пятерых.
# ═══════════════════════════════════════════════════════════════════════════
H13 = 560
im = Image.new("RGB", (MW, H13), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "При совпадении имени сервера — приоритет областей, сверху вниз", 24, DEEP, b=True)

RUNGS = [
    ("1", "политика организации", "если есть — выше всех, даже local", GOLD, DEEP),
    ("2", "local — личная", "~/.claude.json · выше project/user/плагина/коннектора", TEAL, W),
    ("3", "project — общая, в репозитории", ".mcp.json в корне репозитория", MID, W),
    ("4", "user — общая личная", "~/.claude.json", MID, W),
    ("5", "сервер из плагина", "", LIGHT, W),
    ("6", "коннектор", "", LIGHT, W),
]
RX, RW_ = 20, MW - 40
RH, RGAP = 62, 10
y = 58
for num, name, note, col, tc in RUNGS:
    mpanel(d, RX, y, RW_, RH, None, fill=col, stroke=col, sw=0)
    d.ellipse([RX + 16, y + 11, RX + 16 + 40, y + 11 + 40], fill=W if col != GOLD else DEEP)
    nw = d.textlength(num, font=f(22, True))
    d.text((RX + 36 - nw / 2, y + 20), num, font=f(22, True), fill=col if col != GOLD else GOLD)
    mtext(d, RX + 76, y + RH / 2 - 14, name, 21, tc, b=True)
    if note:
        nlen = d.textlength(name, font=f(21, True))
        mtext(d, RX + 76 + nlen + 24, y + RH / 2 - 11, note, 16, tc)
    y += RH + RGAP

# Красный запрещён палитрой (P1-2) — предупреждение о «вся запись целиком,
# поля не смешиваются» переходит на тёмно-синий текст, вес держит жирное
# начертание, не цвет.
mcent(d, y + 10, "Совпало имя в двух областях — побеждает ВСЯ запись приоритетной области целиком;", 19, DEEP, b=True)
mcent(d, y + 36, "поля не смешиваются.", 19, DEEP, b=True)
im = im.crop((0, 0, MW, y + 70))
msave(im, "mcp-n13-prioritet.png")


# ═══════════════════════════════════════════════════════════════════════════
# n14 — доля окна как пропорция + цена действия как сравнение
# ═══════════════════════════════════════════════════════════════════════════
H14 = 480
im = Image.new("RGB", (MW, H14), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "Подключение стоит токенов — но это цена ХУДШЕГО случая, не дефолт", 23, DEEP, b=True)

# ── левая половина: пропорция окна ──────────────────────────────────────────
mtext(d, 20, 56, "5 серверов без отложенной загрузки", 20, MID, b=True)
BX, BY, BW_, BH_ = 20, 96, 720, 64
d.rounded_rectangle([BX, BY, BX + BW_, BY + BH_], radius=10, outline=LIGHT, width=3)
FILLW = int(BW_ * 0.21)
d.rounded_rectangle([BX, BY, BX + FILLW, BY + BH_], radius=10, fill=GOLD)
d.rectangle([BX + FILLW - 10, BY, BX + FILLW, BY + BH_], fill=GOLD)
mtext(d, BX + 14, BY + 18, "21%", 24, DEEP, b=True)
mtext(d, BX + FILLW + 16, BY + 20, "≈55 000 токенов", 20, INK, b=True)
mtext(d, BX, BY + BH_ + 14, "0", 17, MUTE)
rw = d.textlength("окно 200 000", font=f(17))
mtext(d, BX + BW_ - rw, BY + BH_ + 14, "окно 200 000", 17, MUTE)
mpanel(d, BX, BY + BH_ + 48, BW_, 60, None, fill=SURF, stroke=SOFT_GREY)
for k, ln in enumerate(wrap(d, "контекст без подключённых серверов — 0; это худший случай, не дефолт", f(16), BW_ - 32)):
    mtext(d, BX + 16, BY + BH_ + 58 + k * 22, ln, 16, MUTE)

# ── правая половина: сравнение цены одного действия ────────────────────────
RX2 = 800
mtext(d, RX2, 56, "одно и то же действие", 20, MID, b=True)
maxw = 700
v1, v2 = 1365, 44026
scale = maxw / v2
y1, y2 = 100, 180
bh = 48
mtext(d, RX2, y1 - 26, "обычная команда", 17, MUTE)
d.rounded_rectangle([RX2, y1, RX2 + max(v1 * scale, 30), y1 + bh], radius=8, fill=TEAL)
mtext(d, RX2 + max(v1 * scale, 30) + 14, y1 + 12, "1 365", 20, DEEP, b=True)
mtext(d, RX2, y2 - 26, "через инструмент сервера", 17, MUTE)
# Красный запрещён палитрой (P1-2) — «дороже» показывает самый тёмный тон
# палитры (DEEP), не спектральный красный; контраст с бирюзовой «дешёвой»
# полосой держится достаточно сильным и без него.
d.rounded_rectangle([RX2, y2, RX2 + v2 * scale, y2 + bh], radius=8, fill=DEEP)
mtext(d, RX2 + v2 * scale + 14, y2 + 12, "44 026", 20, DEEP, b=True)

box(d, RX2, 270, 440, 100, ["32× разница", "при одинаковом результате"], GOLD, tc=DEEP, sz=24)
im = im.crop((0, 0, MW, 390))
msave(im, "mcp-n14-dolya-okna.png")


# ═══════════════════════════════════════════════════════════════════════════
# n29 — короткая цепочка доверия по имени
# ═══════════════════════════════════════════════════════════════════════════
H29 = 420
im = Image.new("RGB", (MW, H29), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "Доверие держится на имени — не на тексте описания", 24, DEEP, b=True)

CX_ = [20, 420, 820, 1220]
CW_ = 360
CH_ = 110
CY_ = 70
steps = [
    ("имя одобрено\nодин раз", MID, W),
    ("текст описания\nможет смениться", TEAL, W),
    ("доверие\nостаётся", GOLD, DEEP),
]
for i, (txt, col, tc) in enumerate(steps):
    box(d, CX_[i], CY_, CW_, CH_, txt, col, tc=tc, sz=22)
    if i < 2:
        arrow(d, CX_[i] + CW_ + 6, CY_ + CH_ // 2, CX_[i + 1] - 6, CY_ + CH_ // 2, col=MID, wd=5)

mcent(d, CY_ + CH_ + 30, "— так устроена архитектура протокола в целом, не недосмотр одного продукта", 20, MUTE)

# исключение
EY = CY_ + CH_ + 80
mpanel(d, 20, EY, MW - 40, 140, None, fill=(0xFD, 0xF3, 0xD6), stroke=GOLD, sw=3)
mtext(d, 44, EY + 16, "исключение:", 19, GOLDINK, b=True)
mtext(d, 44, EY + 44, '_meta["anthropic/requiresUserInteraction"]: true', 18, DEEP, m=True, b=True)
for k, ln in enumerate(["обязательное подтверждение на КАЖДОМ вызове, без «больше не спрашивать» —",
                        "расширение клиента через пространство имён _meta, не пункт спецификации. Соблюдает Claude Code;",
                        "другой клиент может её не читать и пропустить повторное подтверждение"]):
    mtext(d, 44, EY + 74 + k * 22, ln, 16, INK)
im = im.crop((0, 0, MW, EY + 156))
msave(im, "mcp-n29-tsepochka.png")

report()
