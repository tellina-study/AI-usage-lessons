#!/usr/bin/env python3
"""Схемы рамки новой деки Семинара 5 — открытие n01-n05 и закрытие n59-n62.

Слайд переноса на свой репозиторий и его схема трёх корзин сняты решением
владельца (qa/zamechaniya-vladeltsa-round3.md п. 33, «CTA убрать»): занятие
кончается на том, что стало проверяемым.

Рисуются программно (PIL), а не описываются словами. Файл принадлежит сессии
рамки; make_figures.py / make_figures_khuki.py / make_figures_skill.py /
make_figures_mcp.py / make_figures_otkrytie.py этой сессией не трогаются.

Масштаб подписей — тот же, что в make_figures_khuki.py: полотно 2400 px
вставляется во всю ширину канвы 13,333″, поэтому 38 px читается как 14 pt,
30 px — как 11 pt. Ниже 30 px не опускаться: на проекторе не читается.

  ramka-n01-hero.png            n01  просьба → пять сегментов, два залиты
  ramka-n05-karta.png           n05  две ступени по три развилки, без ролей и файлов
  ramka-n62-chto-razlozheno.png n62  две строки с артефактом, три пустые

Высота полотна = высота схемы на слайде: ширина всегда 12,23″ (а на обложке
13,333″), поэтому 2400 × H px встаёт как 12,23 × 12,23·H/2400 дюймов. Отсюда
и выбраны высоты — иначе композиция уезжает за рабочее поле слайда.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FMB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

DEEP = (0x21, 0x29, 0x5C); MID = (0x06, 0x5A, 0x82); LIGHT = (0x1C, 0x72, 0x93)
GOLD = (0xF0, 0xAB, 0x00); TEAL = (0x02, 0x80, 0x90); SURF = (0xF4, 0xF7, 0xFA)
INK = (0x14, 0x1B, 0x2E); MUTE = (0x5B, 0x6B, 0x7F); RED = (0xB3, 0x26, 0x1E)
W = (255, 255, 255); WARM = (0xFF, 0xF7, 0xE2); PALE = (0xE6, 0xEE, 0xF4)
GHOST = (0x4A, 0x57, 0x74); DIMTX = (0x8B, 0x9A, 0xAD); GOLDTX = (0xC8, 0x8E, 0x08)
DARKCARD = (0x18, 0x20, 0x3A); GOLDINK = (0x5A, 0x44, 0x08)

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)
WARN = []


def f(sz, b=False, m=False):
    return ImageFont.truetype((FMB if b else FM) if m else (FB if b else F), sz)


def fit(d, txt, fo, limit, where):
    if d.textlength(txt, font=fo) > limit:
        WARN.append(f"{where}: шире отведённого — {txt[:56]!r}")


def wrap(d, txt, fo, limit):
    """Перенос по словам: длинная строка на схеме не обрезается и не
    выезжает — она становится двумя. Ширину меряем тем же шрифтом, которым
    будем рисовать."""
    out, cur = [], ""
    for wd in txt.split():
        probe = (cur + " " + wd).strip()
        if cur and d.textlength(probe, font=fo) > limit:
            out.append(cur); cur = wd
        else:
            cur = probe
    if cur:
        out.append(cur)
    return out


def lines_at(d, x, y, lines, fo, col, lh):
    for i, ln in enumerate(lines):
        d.text((x, y + i * lh), ln, font=fo, fill=col)


def clabel(d, cx, y, txt, sz, col=INK, b=False, m=False, where="?", limit=None):
    """Подпись по центру. limit — ширина, в которую она обязана уложиться;
    без него подпись не измеряется вовсе, и так hero молча потерял рамку."""
    fo = f(sz, b, m)
    if limit:
        fit(d, txt, fo, limit, where)
    d.text((cx - d.textlength(txt, font=fo) / 2, y), txt, font=fo, fill=col)


def box(d, x, y, w, h, lines, fc, tc=W, sz=32, b=True, m=False, r=12, pad=18,
        outline=None, where="?"):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fc,
                        outline=outline, width=3 if outline else 0)
    fo = f(sz, b, m)
    if isinstance(lines, str):
        lines = [lines]
    lh = sz + 8
    cy = y + (h - (len(lines) * lh - 8)) // 2
    for i, ln in enumerate(lines):
        fit(d, ln, fo, w - 2 * pad, where)
        d.text((x + (w - d.textlength(ln, font=fo)) / 2, cy + i * lh), ln,
               font=fo, fill=tc)


def dashbox(d, x, y, w, h, col, dash=18, gap=12, width=3, r=10):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, outline=col, width=width)
    # пунктир рисуется поверх сплошной рамки фоном — дешевле и ровнее, чем
    # считать дуги скруглений
    for sx in range(int(x) + r, int(x + w) - r, dash + gap):
        d.rectangle([sx + dash, y - 1, sx + dash + gap, y + width], fill=W)
        d.rectangle([sx + dash, y + h - width - 1, sx + dash + gap, y + h + 1], fill=W)
    for sy in range(int(y) + r, int(y + h) - r, dash + gap):
        d.rectangle([x - 1, sy + dash, x + width, sy + dash + gap], fill=W)
        d.rectangle([x + w - width - 1, sy + dash, x + w + 1, sy + dash + gap], fill=W)


def arrow(d, x1, y1, x2, y2, col=MID, wd=5, head=16):
    import math
    d.line([x1, y1, x2, y2], fill=col, width=wd)
    a = math.atan2(y2 - y1, x2 - x1)
    d.polygon([(x2, y2),
               (x2 - head * math.cos(a - 0.42), y2 - head * math.sin(a - 0.42)),
               (x2 - head * math.cos(a + 0.42), y2 - head * math.sin(a + 0.42))],
              fill=col)


def lock(d, cx, cy, s, col):
    d.rounded_rectangle([cx - s, cy, cx + s, cy + s * 1.35], radius=s // 3, fill=col)
    d.arc([cx - s * 0.62, cy - s * 0.95, cx + s * 0.62, cy + s * 0.35], 180, 360,
          fill=col, width=max(4, s // 4))


def head(d, txt, sz=34, col=DEEP):
    d.text((40, 18), txt, font=f(sz, True), fill=col)


def save(im, name):
    im.save(OUT / name)
    print("  ", name, im.size)


# ── n01 · обложка: просьба и то, что ставится рядом с ней ────────────────────
# 2400 × 612 px при вставке во всю ширину канвы (13,333″) = 3,40″ высоты,
# то есть 45% площади слайда 13,333 × 7,5 — hero-порог ≥40% выполнен с запасом.
im = Image.new("RGB", (2400, 612), DEEP); d = ImageDraw.Draw(im)
d.line([50, 556, 2350, 556], fill=LIGHT, width=5)

d.rounded_rectangle([70, 352, 380, 552], radius=12, fill=W)
clabel(d, 225, 374, "просьба", 34, INK, b=True, where="n01 просьба", limit=274)
for i, s in enumerate(("записана", "прочитана")):
    clabel(d, 225, 424 + i * 30, s, 21, MUTE, where="n01 просьба", limit=274)
for i, s in enumerate(("механизма", "исполнения нет")):
    clabel(d, 225, 492 + i * 28, s, 21, RED, b=True, where="n01 просьба", limit=274)
arrow(d, 410, 452, 560, 452, col=LIGHT, head=20, wd=6)

x = 588
for name, role in (("хук", "исполняемый барьер"),
                   ("скилл", "загрузка по требованию")):
    d.rounded_rectangle([x, 236, x + 330, 556], radius=14, fill=GOLD)
    lock(d, x + 165, 300, 32, DEEP)
    clabel(d, x + 165, 396, name, 34, DEEP, b=True)
    ly = 454
    for ln in wrap(d, role, f(20), 292):
        clabel(d, x + 165, ly, ln, 20, GOLDINK); ly += 28
    x += 366
for name, gloss in (("MCP", "Model Context Protocol"),
                    ("субагент", ""), ("процесс", "")):
    d.rounded_rectangle([x, 336, x + 330, 556], radius=12, outline=GHOST, width=3)
    clabel(d, x + 165, 412, name, 28, DIMTX, b=True)
    if gloss:
        clabel(d, x + 165, 458, gloss, 18, GHOST, where="n01 расшифровка")
    x += 366

d.line([588, 184, 1500, 184], fill=GOLD, width=4)
clabel(d, 1044, 128, "сегодня — две из пяти", 26, GOLD, b=True)
d.line([1560, 184, 2340, 184], fill=GHOST, width=4)
clabel(d, 1950, 128, "следующее занятие — три", 26, DIMTX)
save(im, "ramka-n01-hero.png")


# ── n05 · карта: две ступени по три развилки, ни одного ответа ────────────────
# 2400 × 740 px при ширине 12,23″ = 3,77″ — укладывается под надзаголовок,
# ведущую строку и замыкающую строку слайда-карты.
#
# Строка «решаем» ОБЯЗАНА быть одной строкой: два ряда съедают низ карточки, и
# текст выезжает за её рамку — это не ловится ни одной проверкой сборки (внутрь
# схемы вёрстка не смотрит), поэтому проверка стоит здесь, в генераторе.
STEPS = [
    ("хук", [
        ("В файле нет ни слова про ветки", "чем заменить строку в инструкции"),
        ("Хук работал. Потом молча перестал", "в какой момент и насколько жёстко"),
        ("Хук не ломается — он замедляет", "что делать, когда он мешает"),
    ]),
    ("скилл", [
        ("Вынести процедуру легко. Что станет лучше?", "выигрыш или просто переезд"),
        ("Тела скилла в контексте нет", "что должно быть в описании"),
        ("Тринадцать скиллов, двенадцать не могут сработать", "что делать с теми, что не работают"),
    ]),
]
CARD_H, PAIN_MAX = 236, 3
im = Image.new("RGB", (2400, 740), W); d = ImageDraw.Draw(im)
y = 26
for name, forks in STEPS:
    d.rounded_rectangle([50, y, 370, y + CARD_H], radius=14, fill=MID)
    ly = y + (CARD_H - 44) // 2
    clabel(d, 210, ly, name, 44, W, b=True, where="n05 ступень")

    fx = 400
    for pain, solve in forks:
        d.rounded_rectangle([fx, y, fx + 636, y + CARD_H], radius=12, fill=SURF,
                            outline=LIGHT, width=3)
        fo = f(30, True)
        pl = wrap(d, pain, fo, 588)
        if len(pl) > PAIN_MAX:
            WARN.append(f"n05 боль: больше {PAIN_MAX} строк — {pain!r}")
        lines_at(d, fx + 24, y + 18, pl[:PAIN_MAX], fo, INK, 36)
        d.line([fx + 24, y + 140, fx + 612, y + 140], fill=(0xC6, 0xD5, 0xE2), width=2)
        d.text((fx + 24, y + 152), "решаем", font=f(22, True), fill=GOLDTX)
        fo = f(28)
        sl_ = wrap(d, solve, fo, 588)
        if len(sl_) > 1:
            WARN.append(f"n05 «решаем» не в одну строку — {solve!r}")
        lines_at(d, fx + 24, y + 188, sl_[:1], fo, MUTE, 32)
        fx += 656
    y += CARD_H + 26

dashbox(d, 50, y + 6, 1160, 84, GHOST)
clabel(d, 630, y + 32, "следующее занятие:  MCP · субагент · процесс", 30, DIMTX,
       b=True, where="n05 следующее")
d.rounded_rectangle([1250, y + 6, 1750, y + 90], radius=12, fill=PALE)
clabel(d, 1500, y + 32, "на входе:  .claude/ нет", 26, INK, where="n05 вход")
arrow(d, 1770, y + 48, 1850, y + 48, col=MID, wd=5, head=18)
d.rounded_rectangle([1870, y + 6, 2350, y + 90], radius=12, fill=WARM,
                    outline=GOLD, width=3)
clabel(d, 2110, y + 32, "на выходе:  .claude/", 26, INK, b=True, where="n05 выход")
save(im, "ramka-n05-karta.png")


# ── n62 · что разложено по артефакту, а что не разложено ничем ────────────────
# 2400 × 600 px при ширине 12,23″ = 3,06″.
im = Image.new("RGB", (2400, 600), W); d = ImageDraw.Draw(im)
head(d, "Под какими строками лежит файл, который можно открыть")
DONE = [
    ("хук", "барьер стоит и сам печатает свои дыры",
     ["settings.json + самотест", "ветка seminar-5-hook, 9803643"]),
    ("скилл", "судьбу решает описание, а не содержимое",
     ["описание-триггер", "во фронтматтере"]),
]
EMPTY = ["MCP", "субагент", "процесс"]
y = 92
for name, what, chip in DONE:
    box(d, 50, y, 300, 88, name, MID, sz=32, where="n62 имя")
    d.rounded_rectangle([370, y, 1490, y + 88], radius=12, fill=SURF,
                        outline=LIGHT, width=3)
    fo = f(30, True)
    fit(d, what, fo, 1072, "n62 плашка")
    d.text((394, y + 26), what, font=fo, fill=INK)
    d.rounded_rectangle([1510, y, 2350, y + 88], radius=12, fill=WARM,
                        outline=GOLD, width=3)
    fo = f(25, True); fo2 = f(22, m=True)
    fit(d, chip[0], fo, 800, "n62 чип")
    fit(d, chip[1], fo2, 800, "n62 чип")
    d.text((1534, y + 12), chip[0], font=fo, fill=GOLDINK)
    d.text((1534, y + 48), chip[1], font=fo2, fill=MUTE)
    y += 102
for name in EMPTY:
    box(d, 50, y, 300, 88, name, PALE, tc=DIMTX, sz=32, where="n62 имя")
    dashbox(d, 370, y, 1080, 88, GHOST)
    dashbox(d, 1550, y, 800, 88, GHOST)
    y += 102
save(im, "ramka-n62-chto-razlozheno.png")




print("схемы рамки:")
if WARN:
    print("\nПРЕДУПРЕЖДЕНИЯ (текст шире отведённого места):")
    for w in dict.fromkeys(WARN):
        print("  ", w)
else:
    print("\nпредупреждений нет: весь текст укладывается в отведённые блоки")
