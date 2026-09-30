#!/usr/bin/env python3
"""Схемы блока «Скиллы» новой деки (n33–n58) — рисуются программно (PIL).

Свой генератор раздела: не импортирует make_figures*.py других сессий, чтобы
правка их палитры или вспомогательных функций не меняла эти четыре схемы.

Схемы намеренно НИЗКИЕ (высота 300–420 при ширине 2400): на всех четырёх
слайдах кроме схемы стоит таблица и моноширинная карточка, и высокая схема
съела бы их место. Каждая строка проверяется на ширину — что не влезло,
печатается в конце, а не обрезается молча.

Запуск: python3 make_figures_skilly.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

DEEP = (0x21, 0x29, 0x5C); MID = (0x06, 0x5A, 0x82); LIGHT = (0x1C, 0x72, 0x93)
GOLD = (0xF0, 0xAB, 0x00); TEAL = (0x02, 0x80, 0x90); SURF = (0xF4, 0xF7, 0xFA)
INK = (0x14, 0x1B, 0x2E); MUTE = (0x5B, 0x6B, 0x7F); RED = (0xB3, 0x26, 0x1E)
PALE = (0xE6, 0xEC, 0xF3); ROSE = (0xF7, 0xE6, 0xE4); W = (255, 255, 255)

OUT = Path(__file__).parent / "figures"; OUT.mkdir(exist_ok=True)
CW = 2400
WARN = []
RECTS = []


def _claim(x, y, w, h, where):
    """Регистрирует прямоугольник и ругается, если он перекрыл уже нарисованный.

    Взято у генератора блока «Хуки» — закрывает слепой угол, из-за которого
    за один день три сессии поймали наползающие блоки ТОЛЬКО глазами: проверка
    ширины текста была у всех, проверки вертикальных столкновений не было ни у
    кого. У меня этим слепым углом были ярлык, наехавший на подпись, и золотая
    плашка, наехавшая на строку над ней.

    Префикс «+» в имени — намеренная накладка, такие не считаются.
    """
    if where.startswith("+"):
        return
    x2, y2 = x + w, y + h
    for (ax, ay, bx, by, aw) in RECTS:
        ox = min(x2, bx) - max(x, ax)
        oy = min(y2, by) - max(y, ay)
        if ox > 2 and oy > 2:
            WARN.append(f"СТОЛКНОВЕНИЕ: {where!r} перекрывает {aw!r} на {ox}x{oy} px")
            break
    RECTS.append((x, y, x2, y2, where))


def _newfig(w, h):
    """Новая канва — прямоугольники предыдущей больше не в счёт."""
    RECTS.clear()
    return Image.new("RGB", (w, h), W)


def f(sz, b=False, m=False):
    return ImageFont.truetype(FM if m else (FB if b else F), sz)


def head(d, txt, sz=23):
    d.text((40, 16), txt, font=f(sz, True), fill=DEEP)


def cline(d, y, txt, sz=20, col=INK, b=False):
    fo = f(sz, b); tw = d.textlength(txt, font=fo)
    if tw > CW - 60:
        WARN.append(f"шире канвы: {txt[:56]!r}")
    d.text(((CW - tw) // 2, y), txt, font=fo, fill=col)


def plate(d, x, y, w, h, lines, fc, tc=INK, sz=21, b=False, m=False, pad=18, where=None):
    """Плашка с текстом по левому краю, вертикально по центру."""
    _claim(x, y, w, h, where or f"плашка {lines[0][:24]!r}")
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=fc)
    fo = f(sz, b, m); step = sz + 9
    cy = y + (h - (len(lines) * step - 9)) // 2
    for i, ln in enumerate(lines):
        if d.textlength(ln, font=fo) > w - 2 * pad:
            WARN.append(f"шире плашки: {ln[:56]!r}")
        d.text((x + pad, cy + i * step), ln, font=fo, fill=tc)


def cplate(d, x, y, w, h, lines, fc, tc=W, sz=21, b=True, m=False, where=None):
    """Плашка с текстом по центру."""
    _claim(x, y, w, h, where or f"плашка {lines[0][:24]!r}")
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=fc)
    fo = f(sz, b, m); step = sz + 9
    cy = y + (h - (len(lines) * step - 9)) // 2
    for i, ln in enumerate(lines):
        tw = d.textlength(ln, font=fo)
        if tw > w - 16:
            WARN.append(f"шире плашки: {ln[:56]!r}")
        d.text((x + (w - tw) // 2, cy + i * step), ln, font=fo, fill=tc)


def arrow(d, x1, y1, x2, y2, col=MID):
    """Стрелка между шагами конвейера."""
    import math
    d.line([x1, y1, x2, y2], fill=col, width=4)
    a = math.atan2(y2 - y1, x2 - x1); L = 13
    d.polygon([(x2, y2), (x2 - L * math.cos(a - 0.4), y2 - L * math.sin(a - 0.4)),
               (x2 - L * math.cos(a + 0.4), y2 - L * math.sin(a + 0.4))], fill=col)


def bar(d, x, y, w, h, frac, fc, bg=PALE):
    d.rounded_rectangle([x, y, x + w, y + h], radius=6, fill=bg)
    if frac > 0:
        d.rounded_rectangle([x, y, x + max(int(w * frac), 12), y + h], radius=6, fill=fc)


# ── Артефакт К4: двойная оплата: скилл вынесли, копию оставили ───────────────────────
im = Image.new("RGB", (CW, 360), W); d = ImageDraw.Draw(im)
head(d, "Одна процедура, два места — и платят за неё дважды с 17 мая 2026")
plate(d, 40, 70, 1090, 118,
      ["скилл  .claude/skills/pre-user-gate/SKILL.md   —  165 строк",
       "грузится, когда его выбрали по описанию"],
      SURF, sz=22, m=False)
plate(d, 1270, 70, 1090, 118,
      ["копия  CLAUDE.md, строки 252–279            —   28 строк",
       "грузится при старте КАЖДОЙ сессии, без исключений"],
      ROSE, sz=22)
cplate(d, 1140, 106, 120, 46, ["то же"], MUTE, sz=18)
# полоса времени
d.text((40, 218), "17.05.2026", font=f(19, True), fill=MUTE)
d.text((2200, 218), "сегодня", font=f(19, True), fill=MUTE)
bar(d, 40, 248, 2320, 34, 1.0, GOLD)
cline(d, 252, "четыре с половиной месяца — оба файла в контексте одновременно", 21, DEEP, True)
cline(d, 308, "Вынос сделан правильно. Не сделана зачистка — и стоит это дороже, чем не выносить вовсе.",
      21, RED, True)
im.save(OUT / "skilly-dvoynaya-oplata.png")

# ── Провал К4: цена отбора ────────────────────────────────────────────────────────
im = Image.new("RGB", (CW, 420), W); d = ImageDraw.Draw(im)
head(d, "Прирост дал отобранный скилл — и вот насколько отобранное отличается от среднего")
d.text((40, 74), "успешных прохождений: те же 87 задач, те же 18 связок модели со средой",
       font=f(21, True), fill=INK)
for i, (lbl, val, frac, col) in enumerate(
        [("без скиллов", "33,9%", 0.339, MID), ("с курированными", "50,5%", 0.505, TEAL)]):
    y = 112 + i * 62
    d.text((40, y + 4), lbl, font=f(20), fill=MUTE)
    bar(d, 330, y, 1500, 40, frac, col)
    d.text((1850, y + 4), val, font=f(22, True), fill=col)
d.text((2000, 143), "+16,6 п.п.", font=f(24, True), fill=GOLD)
d.text((40, 250), "качество по одной и той же 12-балльной рубрике", font=f(21, True), fill=INK)
for i, (lbl, val, frac, col) in enumerate(
        [("каталоги, корпус 47 150+", "6,2 / 12", 6.2 / 12, MUTE),
         ("отобранные для замера", "10,1 / 12", 10.1 / 12, LIGHT)]):
    y = 288 + i * 48
    d.text((40, y + 2), lbl, font=f(20), fill=MUTE)
    bar(d, 620, y, 1210, 30, frac, col)
    d.text((1850, y + 2), val, font=f(21, True), fill=col)
cline(d, 388, "Разница между 6,2 и 10,1 по одной рубрике и есть цена отбора.", 21, DEEP, True)
im.save(OUT / "skilly-otbor.png")




# ── Структурный слайд: скилл целиком: устройство одним экраном ────────────────────────────
# Форма согласована с блоком «Хуки» (их n12): одна схема на всю площадь,
# пять пронумерованных частей, термины — подписями К ЧАСТЯМ, а не глоссарием,
# внизу золотая плашка с правилами, которые дальше нужны не один раз.
# Уровням загрузки отдано больше площади, чем остальным частям: это блок,
# снимающий больше всего вопросов, — та же логика, что у них с событиями.
im = _newfig(2400, 845); d = ImageDraw.Draw(im)


def numbox(d, x, y, n, title, w=None):
    """Номерной кружок и заголовок части."""
    r = 17
    d.ellipse([x, y, x + 2 * r, y + 2 * r], fill=DEEP)
    fo = f(19, True); tw = d.textlength(str(n), font=fo)
    d.text((x + r - tw / 2, y + r - 13), str(n), font=fo, fill=W)
    d.text((x + 2 * r + 14, y + 2), title, font=f(23, True), fill=DEEP)


# 1 — где лежит и из чего состоит
numbox(d, 40, 24, 1, "где лежит и из чего состоит")
d.rounded_rectangle([40, 66, 1180, 430], radius=12, fill=SURF)
rows = [(".claude/skills/deploy/", "имя каталога = имя скилла", FM, DEEP, None),
        ("  SKILL.md", "единственный обязательный файл", FM, INK, None),
        ("    ---", "", FM, MUTE, "ФРОНТМАТТЕР"),
        ("    name: deploy", "", FM, INK, None),
        ("    description: Деплоит лендинг…", "", FM, INK, "ОПИСАНИЕ"),
        ("    ---", "", FM, MUTE, None),
        ("    # deploy", "", FM, INK, "ТЕЛО"),
        ("    1. Собрать: npm run build", "", FM, INK, None),
        ("  checklist.md", "читается по ссылке из тела", FM, INK, "ВЛОЖЕНИЕ"),
        ("  check.sh", "запускается, в контекст идёт вывод", FM, INK, None)]
y = 84
for txt, note, font_path, col, tag in rows:
    fo = ImageFont.truetype(font_path, 20)
    if d.textlength(txt, font=fo) > 600: WARN.append(f"шире колонки схемы: {txt[:40]!r}")
    d.text((62, y), txt, font=fo, fill=col)
    # ширина ярлыка МЕРЯЕТСЯ, а не оценивается по числу букв: оценка «11 px
    # на знак» дала наложение ярлыка ВЛОЖЕНИЕ на подпись справа от него
    nx = 700
    if tag:
        tf = f(16, True); tw = d.textlength(tag, font=tf)
        d.rounded_rectangle([700, y - 3, 700 + tw + 20, y + 26], radius=7, fill=GOLD)
        d.text((710, y + 1), tag, font=tf, fill=DEEP)
        nx = 700 + tw + 34
    if note:
        nf = f(17)
        if nx + d.textlength(note, font=nf) > 1160:
            WARN.append(f"подпись не влезает справа от ярлыка: {note[:40]!r}")
        d.text((nx, y + 1), note, font=nf, fill=MUTE)
    y += 34

# 2 — что попадает в контекст и когда (самая большая часть)
numbox(d, 1240, 24, 2, "что попадает в контекст и когда")
d.rounded_rectangle([1240, 66, 2360, 430], radius=12, fill=SURF)
lv = [("имя и описание", "всегда, с первого хода сессии", "никто — попадает само", GOLD, DEEP),
      ("тело файла", "когда скилл выбран", "модель, по описанию", (0xD8, 0xE4, 0xEE), INK),
      ("вложения", "когда тело на них сослалось", "тело файла", PALE, INK)]
for i, (name, when, who, fc, tc) in enumerate(lv):
    yy = 86 + i * 114
    d.rounded_rectangle([1262, yy, 2338, yy + 100], radius=10, fill=fc)
    d.text((1284, yy + 10), name, font=f(24, True), fill=tc)
    d.text((1284, yy + 44), f"когда: {when}", font=f(19), fill=tc)
    d.text((1284, yy + 70), f"кто решает: {who}", font=f(19), fill=tc)

# 3 — чем вызывается
numbox(d, 40, 446, 3, "чем вызывается")
d.rounded_rectangle([40, 488, 1180, 622], radius=12, fill=SURF)
cplate(d, 62, 506, 540, 50, ["модель выбирает сама — по описанию"], MID, sz=20)
cplate(d, 622, 506, 536, 50, ["человек зовёт по имени — /deploy"], LIGHT, sz=20)
d.text((62, 566), "второй способ работает даже когда описание никуда не годится —", font=f(19), fill=INK)
d.text((62, 592), "отсюда целый класс поломок, которых автор не замечает", font=f(19), fill=INK)

# 4 — перечень
numbox(d, 1240, 446, 4, "перечень — всё, что видно до выбора")
d.rounded_rectangle([1240, 488, 2360, 622], radius=12, fill=SURF)
d.text((1262, 500), "build-deck: build-deck", font=ImageFont.truetype(FM, 20), fill=MUTE)
d.text((1262, 530), "pre-user-gate: Pre-USER-GATE walkthrough — orchestrator…", font=ImageFont.truetype(FM, 20), fill=INK)
d.text((1262, 560), "…по строке на каждый установленный скилл", font=f(19), fill=MUTE)
d.rounded_rectangle([1262, 588, 2338, 616], radius=7, fill=GOLD)
d.text((1276, 591), "ПЕРЕЧЕНЬ", font=f(16, True), fill=DEEP)
d.text((1400, 592), "ни тела, ни файлов внутри до выбора не видно", font=f(19), fill=DEEP)

# 5 — путь от запроса до исполнения, во всю ширину
numbox(d, 40, 640, 5, "путь от запроса до исполнения")
steps = [("запрос", "пользователя"), ("перечень", "имён и описаний"), ("выбор", "по описанию"),
         ("чтение", "тела файла"), ("вложения", "по ссылке из тела")]
xw, gap = 420, 42
for i, st in enumerate(steps):
    x = 40 + i * (xw + gap)
    cplate(d, x, 684, xw, 84, list(st), MID if i % 2 == 0 else LIGHT, sz=20)
    if i < len(steps) - 1:
        arrow(d, x + xw + 6, 726, x + xw + gap - 6, 726, col=MUTE)

# золотая плашка: два правила, которые дальше нужны не один раз
d.rounded_rectangle([40, 780, 2360, 838], radius=12, fill=(0xFD, 0xF3, 0xD8))
d.text((66, 790), "•  до выбора модель видит ТОЛЬКО имя и описание — ни тела, ни того, что скилл умеет «на самом деле»",
       font=f(20), fill=INK)
d.text((66, 816), "•  описание пишут ТРЕТЬИМ ЛИЦОМ: «деплоит лендинг», а не «я задеплою» — оно ложится в системный "
                   "промпт рядом с чужими", font=f(20), fill=INK)
im.save(OUT / "skilly-ustroystvo.png")

# ── Сцена внешнего кейса: своё за недели или готовое сегодня ────────────────
im = _newfig(2400, 620); d = ImageDraw.Draw(im)
head(d, "Одна задача, два пути — и по трём меркам из четырёх готовое честно выигрывает")
cols = [("Написать своё", MID, [("срок", "недели"), ("качество разбора таблиц", "хуже"),
                                ("поддержка при смене формата", "ваша навсегда"),
                                ("что внутри", "знаете: сами писали")]),
        ("Взять готовое", TEAL, [("срок", "минута"), ("качество разбора таблиц", "лучше"),
                                 ("поддержка при смене формата", "чужая, пока проект жив"),
                                 ("что внутри", "НЕ ЗНАЕТЕ")])]
for i, (ttl, col, rows) in enumerate(cols):
    x = 40 + i * 1180
    cplate(d, x, 66, 1140, 52, [ttl], col, sz=24)
    for j, (k, v) in enumerate(rows):
        y = 134 + j * 78
        last = j == len(rows) - 1
        d.rounded_rectangle([x, y, x + 1140, y + 66], radius=10,
                            fill=ROSE if (last and i == 1) else SURF)
        d.text((x + 22, y + 10), k, font=f(18), fill=MUTE)
        d.text((x + 22, y + 34), v, font=f(21, True), fill=RED if (last and i == 1) else INK)
cline(d, 468, "Выбор никогда не звучит как «безопасно или опасно» — он звучит как «сегодня или через месяц».", 22, DEEP, True)
cline(d, 510, "Три мерки из четырёх за готовое. Четвёртая — единственная, ради которой стоит этот кейс.", 21, INK)
cline(d, 556, "«Недели» — оценка объёма работы, а не измерение.", 19, MUTE)
im.save(OUT / "skilly-svoy-ili-gotovyy.png")

# ── Провал внешнего кейса: два замера одного каталога ───────────────────────
im = _newfig(2400, 560); d = ImageDraw.Draw(im)
head(d, "Один открытый каталог, два сплошных обхода с разницей в одиннадцать дней")
for i, (when, bad, total, share) in enumerate([("первый обход", 341, 2857, "12%"),
                                               ("через 11 дней", 824, 10700, "8%")]):
    y = 88 + i * 150
    d.text((40, y + 10), when, font=f(21, True), fill=DEEP)
    # полосы рисуются В МАСШТАБЕ друг друга: подложка во всю ширину скрывала
    # бы главное — что каталог между обходами вырос почти вчетверо
    wtot = int(1240 * total / 10700)
    d.rounded_rectangle([330, y, 330 + wtot, y + 52], radius=6, fill=(0xD8, 0xE4, 0xEE))
    d.rounded_rectangle([330, y, 330 + max(int(1240 * bad / 10700), 10), y + 52], radius=6, fill=RED)
    d.text((330 + wtot + 14, y + 16), f"{total} всего", font=f(18), fill=MUTE)
    d.text((1830, y + 6), f"{bad} вредоносных", font=f(21, True), fill=RED)
    d.text((1830, y + 32), f"это {share} каталога", font=f(19), fill=MUTE)
plate(d, 40, 392, 2320, 62,
      ["Каталог вырос почти вчетверо, вредоносных стало вдвое больше — а доля НЕ выросла: 12% против 8%."],
      SURF, tc=DEEP, sz=22, b=True)
plate(d, 40, 468, 2320, 62,
      ["Вычитка — снимок на сегодня. Она ничего не говорит про то, что положат в каталог завтра."],
      ROSE, tc=RED, sz=22, b=True)
im.save(OUT / "skilly-chuzhoy-katalog.png")

print("схемы блока «Скиллы»:", *[p.name for p in sorted(OUT.glob("skilly-*.png"))])
if WARN:
    print("ПРЕДУПРЕЖДЕНИЯ (ширина и столкновения):", len(WARN))
    for w in dict.fromkeys(WARN):
        print("  -", w)
else:
    print("по ширине влезло, столкновений нет")
