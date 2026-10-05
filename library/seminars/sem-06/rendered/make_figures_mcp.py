#!/usr/bin/env python3
"""Схемы раздела «MCP» Семинара 6 — замена таблиц на n13, n14, n15, n31.

Рисуются программно (PIL). Четыре из шести разобранных слайдов — таблица
держит работу схемы (n08, n22 — ИСКЛЮЧЕНИЯ, обоснование ниже и в
VIZUAL-OTCHET.md). Холст 1600 px = 12,23″ рабочей ширины слайда, как в
`make_figures_subagent.py`.

  mcp-n13-oblasti.png          n13   слоёная схема трёх областей видимости
  mcp-n14-prioritet.png        n14   вертикальная лестница приоритета (к коду)
  mcp-n15-dolya-okna.png       n15   пропорция окна + сравнение цены действия
  mcp-n31-tsepochka.png        n31   короткая цепочка доверия по имени

n08 (`base_and_edge`) и n22 (`mechanics_table`, уже две читаемые таблицы —
см. поправку оркестратора) НЕ тронуты: обоснование — в VIZUAL-OTCHET.md.

Круг правок владельца (issue 225, п.4 — «по субагентам и Mcp сделай подробные
одностраничники как было в предыдущей лекции»), зона n06–n17:

  mcp-n09-mehanizm.png         n09   одностраничник «MCP целиком, одним
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
# n13 — слоёная схема трёх областей видимости
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
msave(im, "mcp-n13-oblasti.png")


# ═══════════════════════════════════════════════════════════════════════════
# n14 — лестница приоритета (компаньон к коду .mcp.json)
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
#
# Круг 2 правок владельца (issue 225, п. «одинаковые адреса непонятны»):
# ступени 2 (local) и 4 (user) обе были подписаны одной и той же строкой
# «~/.claude.json» без пояснения — читалось так, будто это один и тот же
# адрес дважды, ошибка на схеме. Это не ошибка: это один физический файл,
# но ДВЕ разные записи внутри него (sem-05/research/mechanics-5-mcp.md §1.2:
# local — «под записью конкретного проекта», user — «под верхнеключом
# mcpServers»). Починка — подписи обеих ступеней называют место внутри
# файла, не только сам файл, и внизу схемы добавлена одна явная строка об
# этом, отдельно от лестницы.
# ═══════════════════════════════════════════════════════════════════════════
H13 = 650
im = Image.new("RGB", (MW, H13), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "При совпадении имени сервера — приоритет областей, сверху вниз", 24, DEEP, b=True)

RUNGS = [
    ("1", "политика организации", "если есть — выше всех, даже local", GOLD, DEEP),
    ("2", "local — личная", "~/.claude.json, запись ЭТОГО проекта · выше остальных четырёх", TEAL, W),
    ("3", "project — общая, в репозитории", ".mcp.json в корне репозитория", MID, W),
    ("4", "user — общая личная", "~/.claude.json, ключ mcpServers — тот же файл, другое место", MID, W),
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
mpanel(d, RX, y + 64, RW_, 46, None, fill=(0xFD, 0xF3, 0xD6), stroke=GOLD, sw=3)
mcent(d, y + 78, "Ступени 2 и 4 — один и тот же физический файл, разные записи внутри него, не два одинаковых адреса.", 16, GOLDINK, b=True)
im = im.crop((0, 0, MW, y + 122))
msave(im, "mcp-n14-prioritet.png")


# ═══════════════════════════════════════════════════════════════════════════
# n15 — постоянная плата (пропорция окна) + цена вызова (сравнение по способу
# доступа) — круг 2 правок владельца (issue 225, часть А9): разведены явно,
# подписи по способу доступа, не абстрактные «команда»/«инструмент».
# ═══════════════════════════════════════════════════════════════════════════
H14 = 480
im = Image.new("RGB", (MW, H14), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "Постоянная плата и цена вызова — разные вещи, разведены ниже", 23, DEEP, b=True)

# ── левая половина: пропорция окна (постоянная плата, худший случай) ───────
mtext(d, 20, 56, "ПОСТОЯННАЯ ПЛАТА — 5 серверов без отложенной загрузки", 20, MID, b=True)
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
msave(im, "mcp-n15-dolya-okna.png")


# ═══════════════════════════════════════════════════════════════════════════
# n31 — короткая цепочка доверия по имени
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
msave(im, "mcp-n31-tsepochka.png")


# ═══════════════════════════════════════════════════════════════════════════
# n08 — одностраничник «MCP и сервер, одним экраном» (issue 225, круг 2, Б.2 + п.4)
#
# Образец — n11 Семинара 5 (khuki-n12-ustroystvo.png, 2400×844, 2,84:1):
# шесть пронумерованных блоков, у каждого своя подложка. Состав блоков —
# механика MCP, не хука. Источник фактов — sem-05/research/mechanics-5-mcp.md
# §1.1/§1.4 (транспорты, кто запускает), §1.2 (два файла области local/user —
# оба физически ~/.claude.json, разные ключи), §2.1 (tools/list и другие
# discovery-запросы, без участия модели), §2.2 (mcp__server__tool), §2.3
# (tool search, ENABLE_TOOL_SEARCH), §2.4 (вызов в выводе подписан именем
# сервера), §2.3 (MAX_MCP_OUTPUT_TOKENS — бюджет результата отдельно от
# бюджета определений).
#
# Круг 2 правок владельца (issue 225, часть Б.2 и построчный разбор n09→n08):
# слайд переставлен ДО кейса (был после сцены и вопроса, теперь сразу после
# «источников данных»); порядок блоков внутри изменён — «что такое сервер»
# теперь блок 1 (было 2, «поднять раньше» — иначе первым на экране читается
# файл конфигурации раньше того, что он вообще конфигурирует); блок «где
# объявляется» получил настоящий мини-шаблон .mcp.json вместо одних бирок
# с ключами; блок «что передаётся при вызове» явно подан как ВЫЗОВ («агент
# поднимает сервер и передаёт параметры») и его тёмная CODEBG-карточка
# заменена на светлую (правило А4 — чёрный фон с белыми буквами убрать
# ВЕЗДЕ, не только на слайдах, которые владелец назвал поимённо); блок
# «контекст и цена» переписан — был абстракцией («цена оплачена» без того,
# какая), стал конкретным: три статьи расхода прямо названы, третья (бюджет
# результата вызова) снята из блока 6 сюда же, чтобы не дублировать. Текст
# всех блоков увеличен на 1–3pt и строки раздвинуты — было мелко при проверке
# на РЕАЛЬНО собранном слайде (п.3/5 круга 1).
#
# Геометрия: холст по-прежнему 2400 px шириной. Высота увеличена с 766 до
# 800 px (ratio 2400/800 = 3,0) — выше порога 2,84:1 (`mechanics_with_figure`,
# потолок 4,3″ при ширине 12,23″), запас 0,16 — безопаснее прежнего запаса
# 0,27 при исходном расчёте 766, но всё ещё выше порога. Проверено повторным
# прогоном `build_sem06.py --block n08` после правки (см. отчёт).
# ═══════════════════════════════════════════════════════════════════════════
def bhead(x, y, n, title, w, numfill=DEEP):
    """Номер в кружке и название блока — над подложкой, тем же приёмом, что
    у n14 (лестница приоритета): кружок с цифрой, заголовок жирным рядом."""
    d.ellipse([x, y, x + 36, y + 36], fill=numfill)
    nw = d.textlength(n, font=f(20, True))
    d.text((x + 18 - nw / 2, y + 7), n, font=f(20, True), fill=W)
    for ln in wrap(d, title, f(20, True), w - 48):
        mtext(d, x + 48, y + 7, ln, 20, DEEP, b=True)
        break  # заголовок блока — одна строка по дизайну сетки


def bpanel(x, y, w, h, fill=SURF):
    mpanel(d, x, y, w, h, None, fill=fill, stroke=None, sw=0)


def code_card(x, y, w, h, lines, fill=W, stroke=LIGHT):
    """Светлая карточка кода (правило А4 — не CODEBG): белая/светлая подложка,
    тёмный моно-текст, тонкая рамка."""
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=fill, outline=stroke, width=2)
    yy = y + 12
    for ln in lines:
        d.text((x + 16, yy), ln, font=f(16, False, True), fill=DEEP)
        yy += 23


MW8 = 2400
HD8 = 46          # высота заголовка блока (кружок + название)
GAP8 = 16
COLW8 = (MW8 - 40 - 2 * GAP8) // 3
CX1, CX2, CX3 = 20, 20 + COLW8 + GAP8, 20 + 2 * (COLW8 + GAP8)

RA8 = 10          # строка А: блоки 1–2–3
HA8 = 377
RB8 = RA8 + HA8 + GAP8     # строка B: блоки 4–5–6
HB8 = 377

# Внутреннего заголовка у схемы нет — его несёт заголовок слайда, и канон
# одностраничника Семинара 5 (`khuki-n12-ustroystvo.png`) строкой-заголовком
# внутри полотна не открывается. Сведение круга владельца: два одностраничника
# занятия обязаны читаться одним жанром.
im = Image.new("RGB", (MW8, RB8 + HB8 + 20), W); d = ImageDraw.Draw(im)

# ── 1 — что такое сервер и где работает (было блоком 2 — поднято выше) ───
bhead(CX1, RA8, "1", "ЧТО ТАКОЕ СЕРВЕР", COLW8)
bpanel(CX1, RA8 + HD8, COLW8, HA8 - HD8, PALE)
yy = RA8 + HD8 + 16
for ln in wrap(d, "Отдельная программа, не часть Claude Code. Отвечает на запросы по протоколу.",
               f(18), COLW8 - 36):
    d.text((CX1 + 18, yy), ln, font=f(18), fill=INK)
    yy += 25
yy += 14
rows1 = [("stdio — локально", "процесс запускает Claude Code у вас на машине", TEAL),
         ("http — удалённо", "сервис, который хостит и обновляет кто-то другой", MID)]
for name, note, col in rows1:
    d.rounded_rectangle([CX1 + 18, yy, CX1 + 216, yy + 38], radius=9, fill=col)
    nw = d.textlength(name, font=f(16, True))
    d.text((CX1 + 18 + (198 - nw) / 2, yy + 10), name, font=f(16, True), fill=W)
    for j, ln in enumerate(wrap(d, note, f(16), COLW8 - 254)):
        d.text((CX1 + 234, yy + 3 + j * 20), ln, font=f(16), fill=MUTE)
    yy += 58
yy += 8
for ln in wrap(d, 'Команда в конфиге исполняется буквально при старте сессии: что записано, то и запустится.',
               f(16, True), COLW8 - 36):
    mtext(d, CX1 + 18, yy, ln, 16, GOLDINK, b=True)
    yy += 21

# ── 2 — где объявляется, с мини-шаблоном .mcp.json ───────────────────────
bhead(CX2, RA8, "2", "ГДЕ ОБЪЯВЛЯЕТСЯ", COLW8)
bpanel(CX2, RA8 + HD8, COLW8, HA8 - HD8, SURF)
code_card(CX2 + 18, RA8 + HD8 + 14, COLW8 - 36, 128, [
    '{ "mcpServers": {',
    '    "github": {',
    '      "command": "npx", …',
    '    } } }',
])
yy = RA8 + HD8 + 156
for k, g in [(".mcp.json", "в репозитории — область project"),
             ("~/.claude.json", "области local (дефолт) и user")]:
    d.text((CX2 + 18, yy), k, font=f(17, False, True), fill=INK)
    for j, ln in enumerate(wrap(d, g, f(15), COLW8 - 36)):
        d.text((CX2 + 18, yy + 23 + j * 19), ln, font=f(15), fill=MUTE)
    yy += 48
mtext(d, CX2 + 18, RA8 + HA8 - 28, "Какая область и почему — разбираем дальше в кейсе", 15, MUTE)

# ── 3 — что происходит при подключении ───────────────────────────────────
bhead(CX3, RA8, "3", "ЧТО ПРОИСХОДИТ ПРИ ПОДКЛЮЧЕНИИ", COLW8)
bpanel(CX3, RA8 + HD8, COLW8, HA8 - HD8, SURF)
yy = RA8 + HD8 + 16
for ln in wrap(d, "Транспорт поднялся — Claude Code САМА, без модели, спрашивает у сервера его список:",
               f(18), COLW8 - 36):
    d.text((CX3 + 18, yy), ln, font=f(18), fill=INK)
    yy += 25
yy += 10
for k in ["tools/list", "prompts/list", "resources/list"]:
    d.rounded_rectangle([CX3 + 18, yy, CX3 + COLW8 - 18, yy + 40], radius=9,
                        fill=W, outline=LIGHT, width=2)
    tw = d.textlength(k, font=f(18, False, True))
    d.text((CX3 + 18 + (COLW8 - 36 - tw) / 2, yy + 8), k, font=f(18, False, True), fill=DEEP)
    yy += 50
for ln in wrap(d, "Сервер отвечает именами и короткой инструкцией — не схемами целиком.",
               f(16), COLW8 - 36):
    mtext(d, CX3 + 18, yy + 8, ln, 16, MUTE)

# ── 4 — вызов: агент поднимает сервер и передаёт параметры ───────────────
bhead(CX1, RB8, "4", "ВЫЗОВ: ПАРАМЕТРЫ АГЕНТ СОБИРАЕТ САМ", COLW8)
bpanel(CX1, RB8 + HD8, COLW8, HB8 - HD8, PALE)
code_card(CX1 + 18, RB8 + HD8 + 14, COLW8 - 36, 96, [
    'mcp__github__create_issue',
    '{ title, body, … }',
], fill=W, stroke=TEAL)
yy = RB8 + HD8 + 124
for ln in wrap(d, "Агент сам поднимает нужный сервер и вызывает его — так же, как вызвал бы "
                  "функцию: полное имя с префиксом сервера и аргументы, которые собрала модель.",
               f(16), COLW8 - 36):
    d.text((CX1 + 18, yy), ln, font=f(16), fill=MUTE)
    yy += 21

# ── 5 — контекст и цена: три статьи расхода, конкретно ───────────────────
bhead(CX2, RB8, "5", "КОНТЕКСТ И ЦЕНА — ТРИ СТАТЬИ", COLW8)
bpanel(CX2, RB8 + HD8, COLW8, HB8 - HD8, SURF)
stages5 = [("старт сессии", "имя сервера и короткая инструкция — в контексте всегда", TEAL),
           ("модель решает", "полную схему инструмента подгружает сама, по требованию (ToolSearch)", MID),
           ("пришёл ответ", "результат вызова — отдельный бюджет: предупреждение за 10 000 токенов, обрезка за 25 000", DEEP)]
yy = RB8 + HD8 + 14
for t_, note, col in stages5:
    box(d, CX2 + 18, yy, COLW8 - 36, 42, t_, col, tc=W, sz=16)
    yy += 48
    for ln in wrap(d, note, f(14), COLW8 - 36):
        d.text((CX2 + 18, yy), ln, font=f(14), fill=MUTE)
        yy += 18
    yy += 8
mpanel(d, CX2 + 18, yy + 2, COLW8 - 36, 56, None, fill=(0xFD, 0xF3, 0xD6), stroke=GOLD, sw=3)
for i, ln in enumerate(wrap(d, "Постоянная плата идёт за то, что сервер подключён. Цена вызова — отдельно, за каждый ответ.",
                            f(14, True), COLW8 - 64)):
    mtext(d, CX2 + 32, yy + 12 + i * 19, ln, 14, GOLDINK, b=True)

# ── 6 — чем отвечает сервер ───────────────────────────────────────────────
bhead(CX3, RB8, "6", "ЧЕМ ОТВЕЧАЕТ СЕРВЕР", COLW8)
bpanel(CX3, RB8 + HD8, COLW8, HB8 - HD8, PALE)
yy = RB8 + HD8 + 16
for ln in wrap(d, "Результат приходит отдельным каналом от обнаружения возможностей — не тем же, "
                  "что при подключении.",
               f(17), COLW8 - 36):
    d.text((CX3 + 18, yy), ln, font=f(17), fill=INK)
    yy += 23
yy += 10
d.rounded_rectangle([CX3 + 18, yy, CX3 + COLW8 - 18, yy + 72], radius=9,
                    fill=W, outline=TEAL, width=2)
d.text((CX3 + 32, yy + 13), "tool call", font=f(16, False, True), fill=DEEP)
d.text((CX3 + 32, yy + 40), "mcp__github__create_issue", font=f(16, True), fill=TEAL)
yy += 88
for ln in wrap(d, "Вызов подписан именем сервера — видно, что ответ пришёл именно оттуда, "
                  "не из общих знаний модели.",
               f(16), COLW8 - 36):
    mtext(d, CX3 + 18, yy, ln, 16, MUTE)
    yy += 21

im = im.crop((0, 0, MW8, RB8 + HB8 + 20))
msave(im, "mcp-n08-mehanizm.png")

# ═══════════════════════════════════════════════════════════════════════════
# n23 — больше не рисует фигуру (круг правок владельца, issue 225, круг 2)
# ═══════════════════════════════════════════════════════════════════════════
# Слайд с временной шкалой тайм-аутов снят: владелец назвал его непонятным
# («свернуть или переформулировать»). Мысль про два разных тайм-аута свёрнута
# одной строкой без цифр в заметки n22 (правило А8 — упоминанием, не
# предметом); точные цифры (30 с / ≈28 ч, MCP_TIMEOUT/MCP_TOOL_TIMEOUT)
# остались в speaker notes n22 как «если спросят». Слайд n23 теперь текстовый
# (плохая/хорошая формулировка запроса агенту) и фигуры не требует — функция
# ниже и файл `mcp-n23-taym-auty-shkala.png` больше не актуальны и удалены из
# сборки этим кругом правок.


report()
