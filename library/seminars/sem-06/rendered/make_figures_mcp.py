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

Круг правок владельца (issue 225, п.4 — «по субагентам и Mcp сделай подробные
одностраничники как было в предыдущей лекции»), зона n06–n16:

  mcp-n08a-mehanizm.png        n08a  одностраничник «MCP целиком, одним
                                      экраном» — шесть блоков, образец n11
                                      Семинара 5 (`khuki-n12-ustroystvo.png`),
                                      состав блоков СВОЙ, не копия хука: где
                                      объявляется · что такое сервер и где
                                      работает · что передаётся при
                                      подключении · что передаётся при
                                      вызове · что попадает в контекст и чего
                                      это стоит · чем отвечает сервер и что
                                      среда делает с ответом.
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


# ═══════════════════════════════════════════════════════════════════════════
# n08a — одностраничник «MCP целиком, одним экраном» (issue 225, п.4)
#
# Образец — n11 Семинара 5 (khuki-n12-ustroystvo.png, 2400×844, 2,84:1):
# шесть пронумерованных блоков, у каждого своя подложка. Состав блоков здесь
# СВОЙ — механика MCP, не хука: где объявляется · что такое сервер и где
# работает · что передаётся при подключении · что передаётся при вызове ·
# что попадает в контекст и чего это стоит · чем отвечает сервер и что среда
# делает с ответом. Источник фактов — sem-05/research/mechanics-5-mcp.md
# §1.1/§1.4 (транспорты, кто запускает), §2.1 (tools/list и другие
# discovery-запросы, без участия модели), §2.2 (mcp__server__tool), §2.3
# (tool search, ENABLE_TOOL_SEARCH), §2.4 (вызов в выводе подписан именем
# сервера).
#
# Первая версия (2 колонки × 2 строки сверху + 2 строки во всю ширину снизу,
# холст 1600×992) была ЗАЖАТА сборкой: `K.figure()` выделяет приёму
# `mechanics_with_figure` потолок 4,3″ высоты при полной ширине 12,23″ —
# предельное соотношение сторон 2,84:1 (ровно то, что даёт холст хука,
# 2400/844). Соотношение 1600/992 = 1,61 — почти вдвое ниже порога, схема
# встала на слайд в 57% ширины и 32% площади от себя же, нечитаемо плотно.
# Починка — не перерисовка в деталях, а смена СЕТКИ: с «2+2+1+1» на чистую
# «3 колонки × 2 строки», тем же приёмом, что у хука (широкий холст, бок о
# бок, а не стопкой). Холст 2400×840 — соотношение 2,857:1, с запасом выше
# порога 2,84:1.
# ═══════════════════════════════════════════════════════════════════════════
def bhead(x, y, n, title, w, numfill=DEEP):
    """Номер в кружке и название блока — над подложкой, тем же приёмом, что
    у n13 (лестница приоритета): кружок с цифрой, заголовок жирным рядом."""
    d.ellipse([x, y, x + 34, y + 34], fill=numfill)
    nw = d.textlength(n, font=f(19, True))
    d.text((x + 17 - nw / 2, y + 7), n, font=f(19, True), fill=W)
    for ln in wrap(d, title, f(19, True), w - 46):
        mtext(d, x + 46, y + 6, ln, 19, DEEP, b=True)
        break  # заголовок блока — одна строка по дизайну сетки


def bpanel(x, y, w, h, fill=SURF):
    mpanel(d, x, y, w, h, None, fill=fill, stroke=None, sw=0)


MW8 = 2400
HD8 = 42          # высота заголовка блока (кружок + название)
GAP8 = 16
COLW8 = (MW8 - 40 - 2 * GAP8) // 3
CX1, CX2, CX3 = 20, 20 + COLW8 + GAP8, 20 + 2 * (COLW8 + GAP8)

RA8 = 54          # строка А: блоки 1–2–3
HA8 = 360
RB8 = RA8 + HA8 + GAP8     # строка B: блоки 4–5–6
HB8 = 360

im = Image.new("RGB", (MW8, RB8 + HB8 + 20), W); d = ImageDraw.Draw(im)
mtext(d, 20, 8, "MCP устроено из шести частей — одна карта на весь блок", 27, DEEP, b=True)

# ── 1 — где объявляется ──────────────────────────────────────────────────
bhead(CX1, RA8, "1", "ГДЕ ОБЪЯВЛЯЕТСЯ", COLW8)
bpanel(CX1, RA8 + HD8, COLW8, HA8 - HD8, SURF)
for i, (k, g) in enumerate([
        (".mcp.json", "в репозитории — область project"),
        ("~/.claude.json", "области local (дефолт) и user"),
        ('"command"/"args"', "чем и что запускается"),
        ('"env"', "ключ — подстановкой ${VAR}")]):
    yy = RA8 + HD8 + 16 + i * 58
    d.text((CX1 + 18, yy), k, font=f(19, False, True), fill=INK)
    for j, ln in enumerate(wrap(d, g, f(16), COLW8 - 36)):
        d.text((CX1 + 18, yy + 26 + j * 20), ln, font=f(16), fill=MUTE)
mtext(d, CX1 + 18, RA8 + HA8 - 30, "Какая область и почему — через два слайда", 15, MUTE)

# ── 2 — что такое сервер и где работает ──────────────────────────────────
bhead(CX2, RA8, "2", "ЧТО ТАКОЕ СЕРВЕР И ГДЕ РАБОТАЕТ", COLW8)
bpanel(CX2, RA8 + HD8, COLW8, HA8 - HD8, PALE)
yy = RA8 + HD8 + 14
for ln in wrap(d, "Отдельная программа, не часть Claude Code — отвечает на запросы по протоколу.",
               f(17), COLW8 - 36):
    d.text((CX2 + 18, yy), ln, font=f(17), fill=INK)
    yy += 24
yy += 14
rows2 = [("stdio — локально", "процесс запускает Claude Code у вас на машине", TEAL),
         ("http — удалённо", "сервис, который хостит и обновляет кто-то другой", MID)]
for name, note, col in rows2:
    d.rounded_rectangle([CX2 + 18, yy, CX2 + 210, yy + 36], radius=9, fill=col)
    nw = d.textlength(name, font=f(15, True))
    d.text((CX2 + 18 + (192 - nw) / 2, yy + 9), name, font=f(15, True), fill=W)
    for j, ln in enumerate(wrap(d, note, f(15), COLW8 - 248)):
        d.text((CX2 + 228, yy + 2 + j * 19), ln, font=f(15), fill=MUTE)
    yy += 56
for ln in wrap(d, 'Команда в конфиге исполняется буквально при старте сессии.',
               f(15, True), COLW8 - 36):
    mtext(d, CX2 + 18, yy + 6, ln, 15, GOLDINK, b=True)

# ── 3 — что передаётся при подключении ───────────────────────────────────
bhead(CX3, RA8, "3", "ЧТО ПЕРЕДАЁТСЯ ПРИ ПОДКЛЮЧЕНИИ", COLW8)
bpanel(CX3, RA8 + HD8, COLW8, HA8 - HD8, SURF)
yy = RA8 + HD8 + 14
for ln in wrap(d, "Транспорт поднялся — Claude Code САМА, без модели, спрашивает у сервера его список:",
               f(17), COLW8 - 36):
    d.text((CX3 + 18, yy), ln, font=f(17), fill=INK)
    yy += 24
yy += 10
for k in ["tools/list", "prompts/list", "resources/list"]:
    d.rounded_rectangle([CX3 + 18, yy, CX3 + COLW8 - 18, yy + 38], radius=9,
                        fill=W, outline=LIGHT, width=2)
    tw = d.textlength(k, font=f(17, False, True))
    d.text((CX3 + 18 + (COLW8 - 36 - tw) / 2, yy + 8), k, font=f(17, False, True), fill=DEEP)
    yy += 48
for ln in wrap(d, "Сервер отвечает именами и короткой инструкцией — не схемами целиком.",
               f(15), COLW8 - 36):
    mtext(d, CX3 + 18, yy + 8, ln, 15, MUTE)

# ── 4 — что передаётся при вызове ────────────────────────────────────────
bhead(CX1, RB8, "4", "ЧТО ПЕРЕДАЁТСЯ ПРИ ВЫЗОВЕ", COLW8)
bpanel(CX1, RB8 + HD8, COLW8, HB8 - HD8, PALE)
d.rounded_rectangle([CX1 + 18, RB8 + HD8 + 14, CX1 + COLW8 - 18, RB8 + HD8 + 96],
                    radius=10, fill=CODEBG)
d.text((CX1 + 34, RB8 + HD8 + 28), "mcp__github__", font=f(17, False, True), fill=(0xE8, 0xEE, 0xF4))
d.text((CX1 + 34, RB8 + HD8 + 50), "create_issue", font=f(17, False, True), fill=(0xE8, 0xEE, 0xF4))
d.text((CX1 + 34, RB8 + HD8 + 72), "{ title, body, … }", font=f(15, False, True), fill=(0xA9, 0xC3, 0xD6))
yy = RB8 + HD8 + 108
for ln in wrap(d, "Имя — с префиксом сервера (mcp__<сервер>__<инструмент>) и аргументы, которые собрала модель.",
               f(15), COLW8 - 36):
    d.text((CX1 + 18, yy), ln, font=f(15), fill=MUTE)
    yy += 20

# ── 5 — что попадает в контекст и чего это стоит ─────────────────────────
bhead(CX2, RB8, "5", "КОНТЕКСТ И ЦЕНА", COLW8)
bpanel(CX2, RB8 + HD8, COLW8, HB8 - HD8, SURF)
stages5 = [("старт сессии", "только имена и инструкция", TEAL),
           ("модель решает", "ToolSearch за полной схемой", MID),
           ("вызван", "цена оплачена", DEEP)]
yy = RB8 + HD8 + 14
for t_, note, col in stages5:
    box(d, CX2 + 18, yy, COLW8 - 36, 44, t_, col, tc=W, sz=16)
    yy += 48
    for ln in wrap(d, note, f(14), COLW8 - 36):
        d.text((CX2 + 18, yy), ln, font=f(14), fill=MUTE)
    yy += 22
mpanel(d, CX2 + 18, yy + 2, COLW8 - 36, 62, None, fill=(0xFD, 0xF3, 0xD6), stroke=GOLD, sw=3)
for i, ln in enumerate(wrap(d, "Худший случай без отложенной загрузки — отдельная цифра дальше.",
                            f(14, True), COLW8 - 64)):
    mtext(d, CX2 + 32, yy + 14 + i * 19, ln, 14, GOLDINK, b=True)

# ── 6 — чем отвечает сервер и что среда делает с ответом ─────────────────
bhead(CX3, RB8, "6", "ЧЕМ ОТВЕЧАЕТ СЕРВЕР", COLW8)
bpanel(CX3, RB8 + HD8, COLW8, HB8 - HD8, PALE)
yy = RB8 + HD8 + 14
for ln in wrap(d, "Результат вызова — отдельный канал от обнаружения: свой бюджет "
                  "(предупреждение на 10 000 токенов, обрезка на 25 000 по умолчанию).",
               f(16), COLW8 - 36):
    d.text((CX3 + 18, yy), ln, font=f(16), fill=INK)
    yy += 23
yy += 10
d.rounded_rectangle([CX3 + 18, yy, CX3 + COLW8 - 18, yy + 70], radius=9,
                    fill=W, outline=TEAL, width=2)
d.text((CX3 + 32, yy + 12), "tool call", font=f(15, False, True), fill=DEEP)
d.text((CX3 + 32, yy + 38), "mcp__github__create_issue", font=f(15, True), fill=TEAL)
yy += 84
for ln in wrap(d, "Вызов подписан именем сервера — видно, что ответ пришёл именно оттуда.",
               f(15), COLW8 - 36):
    mtext(d, CX3 + 18, yy, ln, 15, MUTE)
    yy += 20

im = im.crop((0, 0, MW8, RB8 + HB8 + 20))
msave(im, "mcp-n08a-mehanizm.png")

report()
