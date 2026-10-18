#!/usr/bin/env python3
"""Две схемы кейса A ступени 2 Семинара 7 — развилка маршрута.

Заведены по разбору Опуса (круг ревью деки, issue 233): «вся ступень
называется „маршрут“, а ветвление нарисовано таблицей». Ровно та же развилка
рисуется дважды, одной сеткой и одними координатами, и разница между двумя
картинками и есть содержание кейса:

  marshrut-c4-razvilka-tseny.png          сцена   одна точка, четыре ветки,
                                                  под каждой её цена
  marshrut-c4-razvilka-chuzhoe-pismo.png  провал  та же развилка и письмо,
                                                  которое не похоже ни на одну
                                                  ветку, — и всё равно уезжает
                                                  в одну из них

Второй кадр повторяет первый по расстановке умышленно: зал уже смотрел на эту
развилку, поэтому на провале ему остаётся заметить ровно одно изменение —
вход другой, а слотов по-прежнему четыре.

Рисуется программно (PIL), как схемы Семинара 6 (`make_figures_mcp.py`).
Холст 1600 px = 12,23″ рабочей ширины слайда, то есть 130,8 px на дюйм и
1 pt = 1,82 px. Пол кегля деки — 7,5 pt = 13,6 px; самая мелкая подпись здесь
19 px = 10,5 pt, и `--proverka` печатает замеренный пол вместе с переполнением
коробок, чтобы «влезло» было замером, а не взглядом.

Имена файлов БЕЗ номера слайда: номера кейса провизорные (`c4-NN`), сведение в
сквозной счёт идёт машиной при сборке, и номер внутри имени схемы переживал бы
это сведение молча.

    python3 make_figures_c4.py
    python3 make_figures_c4.py --proverka
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

DEEP = (0x21, 0x29, 0x5C)
MID = (0x06, 0x5A, 0x82)
LIGHT = (0x1C, 0x72, 0x93)
TEAL = (0x02, 0x80, 0x90)
GOLD = (0xF0, 0xAB, 0x00)
GOLD_DARK = (0x8A, 0x62, 0x00)
GOLD_TINT = (0xFE, 0xF5, 0xE0)
SURF = (0xF4, 0xF7, 0xFA)
INK = (0x14, 0x1B, 0x2E)
MUTE = (0x5B, 0x6B, 0x7F)
PALE = (0xE5, 0xEA, 0xF0)
GREY = (0xC9, 0xD1, 0xDB)
WHITE = (255, 255, 255)

MW = 1600
PX_PT = 130.8 / 72.0        # пикселей в пункте на этом холсте
POL_PT = 7.5                # пол кегля деки

_fonts = {}
_kegli = []
_perepolnenie = []


def f(size, bold=False):
    key = (size, bold)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(FONT_B if bold else FONT, size)
    _kegli.append(size)
    return _fonts[key]


def wrap(d, text, size, width, bold=False):
    fo = f(size, bold)
    words, lines, cur = text.split(), [], ""
    for w in words:
        probe = f"{cur} {w}".strip()
        if d.textlength(probe, font=fo) <= width or not cur:
            cur = probe
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def block(d, x, y, text, size, width, *, bold=False, color=INK, lead=1.26, gde=""):
    """Абзац с переносом по словам. Возвращает занятую высоту."""
    lines = wrap(d, text, size, width, bold)
    step = int(size * lead)
    for i, ln in enumerate(lines):
        d.text((x, y + i * step), ln, font=f(size, bold), fill=color)
    h = step * (len(lines) - 1) + int(size * 1.18)
    if gde:
        _zanyato.append((gde, x, y, width, h))
    return h


_zanyato = []


def box(d, x, y, w, h, *, fill=SURF, stroke=LIGHT, sw=3, r=14, dash=False):
    if dash:
        d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill)
        step, on = 14, 8
        for cx in range(int(x), int(x + w), step):
            d.line([cx, y, min(cx + on, x + w), y], fill=stroke, width=sw)
            d.line([cx, y + h, min(cx + on, x + w), y + h], fill=stroke, width=sw)
        for cy in range(int(y), int(y + h), step):
            d.line([x, cy, x, min(cy + on, y + h)], fill=stroke, width=sw)
            d.line([x + w, cy, x + w, min(cy + on, y + h)], fill=stroke, width=sw)
        return
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=stroke, width=sw)


def vetka(d, x0, y0, x1, y1, *, color=LIGHT, sw=4, dotted=False, head=11, lane=0.45):
    """Ветка развилки: три отрезка (вправо — по вертикали — вправо), со
    стрелкой. `lane` разводит вертикальные участки по своим дорожкам: при
    общей дорожке четыре ветки накладываются друг на друга и подсвеченная
    пятая пересекает соседнюю ровно там, где зал ищет её собственный путь."""
    xm = x0 + (x1 - x0) * lane
    pts = [(x0, y0), (xm, y0), (xm, y1), (x1, y1)]
    for a, b in zip(pts, pts[1:]):
        if dotted:
            n = max(int(max(abs(b[0] - a[0]), abs(b[1] - a[1])) / 13), 1)
            for i in range(n):
                t0, t1 = i / n, (i + 0.52) / n
                d.line([a[0] + (b[0] - a[0]) * t0, a[1] + (b[1] - a[1]) * t0,
                        a[0] + (b[0] - a[0]) * t1, a[1] + (b[1] - a[1]) * t1],
                       fill=color, width=sw)
        else:
            d.line([a[0], a[1], b[0], b[1]], fill=color, width=sw)
    d.polygon([(x1, y1), (x1 - head, y1 - head * 0.62), (x1 - head, y1 + head * 0.62)],
              fill=color)


def strelka_vniz(d, x, y0, y1, *, color=LIGHT, sw=4, head=10):
    d.line([x, y0, x, y1 - head], fill=color, width=sw)
    d.polygon([(x, y1), (x - head * 0.62, y1 - head), (x + head * 0.62, y1 - head)], fill=color)


def fits(d, text, size, width, max_h, gde, *, bold=False, lead=1.26):
    lines = wrap(d, text, size, width, bold)
    h = int(size * lead) * (len(lines) - 1) + int(size * 1.18)
    if h > max_h:
        _perepolnenie.append(f"{gde}: {h} px при {int(max_h)} px — «{text[:34]}…»")
    return h


def sohranit(im, name):
    im.save(OUT / name)
    pol = min(_kegli) if _kegli else 0
    print(f"   {name}  {im.size[0]}×{im.size[1]}  пол кегля {pol} px = "
          f"{pol / PX_PT:.1f} pt")
    if pol / PX_PT < POL_PT:
        _perepolnenie.append(f"{name}: кегль {pol / PX_PT:.1f} pt ниже пола {POL_PT} pt")


# ═══════════════════════════════════════════════════════════════════════════
# Общая сетка обеих схем
# ═══════════════════════════════════════════════════════════════════════════
FORK_X, FORK_W = 320, 340           # коробка шага классификации
ROW_X, ROW_W = 740, 840             # колонка ветвей
NAME_W = 320                        # имя ветки внутри строки ветви


def shag_klassifikatsii(d, y, h, *, hvost=True):
    """Коробка «шаг классификации» — точка развилки. Одна и та же в двух схемах."""
    box(d, FORK_X, y, FORK_W, h, fill=WHITE, stroke=MID, sw=4)
    d.rounded_rectangle([FORK_X + 12, y + 12, FORK_X + 21, y + h - 12], radius=4, fill=GOLD)
    tw = FORK_W - 62
    th = block(d, FORK_X + 36, y + 18, "шаг классификации", 23, tw, bold=True, color=DEEP)
    fits(d, "на выходе — одна метка из четырёх", 19, tw, h - 34 - th,
         "подпись развилки")
    block(d, FORK_X + 36, y + 24 + th, "на выходе — одна метка из четырёх",
          19, tw, color=MUTE)
    if hvost:
        d.ellipse([FORK_X + FORK_W - 11, y + h / 2 - 11,
                   FORK_X + FORK_W + 11, y + h / 2 + 11], fill=GOLD, outline=GOLD_DARK, width=3)
    return FORK_X + FORK_W + 11, y + h / 2


# ═══════════════════════════════════════════════════════════════════════════
# Схема 1 — сцена: одна точка, четыре ветки, под каждой цена
# ═══════════════════════════════════════════════════════════════════════════
VETVI = [
    ("биллинг", "спрашивает статус оплаты у внутреннего сервиса",
     "запроса к сервису не будет вовсе", False),
    ("техподдержка", "подтягивает в черновик базу знаний по этой метке",
     "ответ придёт по чужой теме", False),
    ("жалоба", "ставит пометку «срочно» и короткий срок ответа",
     "срок сорван, и счётчика по нему никто не вёл", False),
    ("спам", "архив; человек письмо уже не увидит",
     "обращение клиента исчезает из поля зрения", True),
]

H1 = 500
im = Image.new("RGB", (MW, H1), WHITE)
d = ImageDraw.Draw(im)

d.text((ROW_X, 10), "куда уезжает письмо", font=f(21, True), fill=MID)
d.text((ROW_X + NAME_W + 30, 10), "цена неверной метки", font=f(21, True), fill=GOLD_DARK)

box(d, 20, 166, 280, 120, fill=SURF, stroke=LIGHT, sw=3)
th = block(d, 42, 182, "письмо в общий ящик", 21, 238, bold=True, color=DEEP)
fits(d, "двести писем за час", 19, 238, 120 - 32 - th, "подпись письма")
block(d, 42, 188 + th, "двести писем за час", 19, 238, color=MUTE)
d.line([300, 226, FORK_X - 4, 226], fill=LIGHT, width=4)
d.polygon([(FORK_X, 226), (FORK_X - 10, 221), (FORK_X - 10, 231)], fill=LIGHT)

fork_x, fork_y = shag_klassifikatsii(d, 166, 120)

ROW_H, ROW_GAP, ROW_Y0 = 104, 12, 40
for i, (name, delaet, tsena, dorogo) in enumerate(VETVI):
    ry = ROW_Y0 + i * (ROW_H + ROW_GAP)
    cy = ry + ROW_H / 2
    vetka(d, fork_x, fork_y, ROW_X - 6, cy, color=GOLD_DARK if dorogo else LIGHT,
          sw=5 if dorogo else 4, lane=0.26 + 0.17 * i)
    box(d, ROW_X, ry, NAME_W, ROW_H, fill=SURF, stroke=LIGHT, sw=3)
    nh = block(d, ROW_X + 20, ry + 12, name, 25, NAME_W - 40, bold=True, color=DEEP)
    fits(d, delaet, 18, NAME_W - 40, ROW_H - 20 - nh, f"что делает {name}")
    block(d, ROW_X + 20, ry + 16 + nh, delaet, 18, NAME_W - 40, color=MUTE)

    tx = ROW_X + NAME_W + 30
    tw = ROW_W - NAME_W - 30
    box(d, tx, ry, tw, ROW_H,
        fill=GOLD_TINT if dorogo else WHITE,
        stroke=GOLD if dorogo else GREY, sw=4 if dorogo else 3)
    podpis = "самая дорогая из четырёх" if dorogo else ""
    pole = ROW_H - (26 if podpis else 0)
    fits(d, tsena, 22, tw - 44, pole - 20, f"цена {name}", bold=True)
    th = len(wrap(d, tsena, 22, tw - 44, True)) * 28
    block(d, tx + 22, ry + (pole - th) / 2 + 2, tsena, 22, tw - 44, bold=True,
          color=GOLD_DARK if dorogo else INK)
    if podpis:
        fo = f(16, True)
        d.text((tx + tw - 22 - d.textlength(podpis, font=fo), ry + ROW_H - 30),
               podpis, font=fo, fill=GOLD_DARK)

sohranit(im, "marshrut-c4-razvilka-tseny.png")


# ═══════════════════════════════════════════════════════════════════════════
# Схема 2 — провал: письмо, не похожее ни на одну ветку
# ═══════════════════════════════════════════════════════════════════════════
VETVI2 = [
    ("биллинг", "", False),
    ("техподдержка", "ответ уходит не про то; узнают от клиента, когда он спросит снова", True),
    ("жалоба", "", False),
    ("спам", "", False),
]
NAME_W2 = 280                        # имена здесь однословные, хвост шире

H2 = 480
im = Image.new("RGB", (MW, H2), WHITE)
d = ImageDraw.Draw(im)

# вход — письмо пятого рода; расстановка та же, что на схеме сцены
PISMO = "предложение о партнёрстве: оптовые закупки, просят прайс и договор"
box(d, 20, 120, 290, 200, fill=GOLD_TINT, stroke=GOLD, sw=4)
th = block(d, 42, 140, "письмо пятого рода", 23, 246, bold=True, color=GOLD_DARK)
fits(d, PISMO, 19, 246, 200 - 44 - th, "письмо пятого рода")
block(d, 42, 148 + th, PISMO, 19, 246, color=INK)
d.line([310, 220, FORK_X - 4, 220], fill=GOLD_DARK, width=4)
d.polygon([(FORK_X, 220), (FORK_X - 10, 215), (FORK_X - 10, 225)], fill=GOLD_DARK)

fork_x, fork_y = shag_klassifikatsii(d, 160, 120)
d.text((FORK_X + 4, 292), "слотов четыре, и все заняты", font=f(19, True), fill=MUTE)

# то, чего в формате ответа нет
PANEL = "варианта «подходящей ветки нет» формат ответа не содержит; " \
        "сигнала «я не уверен» на выходе тоже нет"
box(d, 20, 338, 700, 108, fill=WHITE, stroke=GOLD, sw=4)
fits(d, PANEL, 21, 656, 80, "панель формата", bold=True)
block(d, 44, 356, PANEL, 21, 656, bold=True, color=GOLD_DARK)

ROW_H2, ROW_GAP2, ROW_Y02 = 80, 10, 14
for i, (name, hvost, vybran) in enumerate(VETVI2):
    ry = ROW_Y02 + i * (ROW_H2 + ROW_GAP2)
    cy = ry + ROW_H2 / 2
    vetka(d, fork_x, fork_y, ROW_X - 6, cy,
          color=GOLD_DARK if vybran else GREY, sw=6 if vybran else 3, dotted=not vybran,
          lane=0.26 + 0.17 * i)
    box(d, ROW_X, ry, NAME_W2 + (16 if vybran else 0), ROW_H2,
        fill=GOLD_TINT if vybran else PALE,
        stroke=GOLD_DARK if vybran else GREY, sw=4 if vybran else 2)
    nh = block(d, ROW_X + 20, ry + (ROW_H2 - (54 if vybran else 30)) / 2, name, 25,
               NAME_W2 - 40, bold=True, color=GOLD_DARK if vybran else MUTE)
    if vybran:
        podpis = "ближайшая по сходству"
        fo = f(17, True)
        if d.textlength(podpis, font=fo) > NAME_W2 - 24:
            _perepolnenie.append(f"подпись выбранной ветки шире коробки: «{podpis}»")
        d.text((ROW_X + 20, ry + (ROW_H2 - 54) / 2 + nh + 4), podpis, font=fo, fill=GOLD_DARK)
        tx = ROW_X + NAME_W2 + 42
        tw = ROW_W - NAME_W2 - 42
        fits(d, hvost, 22, tw - 20, ROW_H2 - 24, "хвост выбранной ветки", bold=True)
        hh = len(wrap(d, hvost, 22, tw - 20, True)) * 28
        block(d, tx, ry + (ROW_H2 - hh) / 2 + 2, hvost, 22, tw - 20, bold=True, color=INK)

# пятая строка — слота под такое письмо нет
PYATAYA = "ветки для партнёрского предложения в списке нет, и завести её " \
          "решение этого шага не может"
ry = ROW_Y02 + 4 * (ROW_H2 + ROW_GAP2)
box(d, ROW_X, ry, ROW_W, ROW_H2, fill=WHITE, stroke=GREY, sw=3, dash=True)
fits(d, PYATAYA, 21, ROW_W - 50, ROW_H2 - 24, "пятая строка")
ph = len(wrap(d, PYATAYA, 21, ROW_W - 50)) * 27
block(d, ROW_X + 24, ry + (ROW_H2 - ph) / 2 + 2, PYATAYA, 21, ROW_W - 50, color=MUTE)

sohranit(im, "marshrut-c4-razvilka-chuzhoe-pismo.png")

if _perepolnenie:
    print("\n ПЕРЕПОЛНЕНИЕ:")
    for s in _perepolnenie:
        print("   ", s)
    sys.exit(1)
print("\n  обе схемы влезли: переполнения нет, пол кегля выше 7,5 pt")
