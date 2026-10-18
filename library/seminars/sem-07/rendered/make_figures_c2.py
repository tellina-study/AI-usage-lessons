#!/usr/bin/env python3
"""Схемы кейса Zillow Offers (ступень 1, кейс B) — две штуки, рисуются PIL.

Имена файлов — по финальной сквозной нумерации слайдов (переименованы при
технической сборке; были `zillow-c2-02-dve-tsepochki.png`/`zillow-c2-04-
spektr.png` на промежуточном круге сведения):

    zillow-n11-dve-tsepochki.png       n11    одна цифра в двух цепочках;
                                              место гейта во второй — пустой слот
    zillow-n13-spektr.png              n13    спектр цены и обратимости линией,
                                              две точки на нём: письмо и дом

Обе схемы объявлены самими слайдами (поле `visual.figure` во фронтматтере),
таблица `FIGS` в сборщике не тронута — слайд главнее, так в `audit_figs` и
записано.

Почему PIL, а не mermaid/QuickChart: обе схемы — композиции с пустым слотом и с
клином переменной толщины, в языке последовательностей их не выразить, зато
кегль, цвет и координаты здесь замеряются (пол кегля деки — 7,5 pt, на холсте
1600 px при рабочей ширине 12,23″ это 13,6 px; обе схемы печатают свой пол при
запуске). Тот же способ, которым сделаны схемы Семинаров 5 и 6.

РАСХОЖДЕНИЕ, КОТОРОЕ НАДО СВЕСТИ ПРИ СБОРКЕ. В этой папке два способа рисовать
схемы, заведённые параллельными сессиями одной волны: `make_figures_c1.py` и
`make_figures_mostik.py` идут от `fig_toolkit.py` (копия тулкита Семинара 6
вместе с машинерией EN-трека), `make_figures_c5.py` и этот файл — со своими
примитивами. Прогон `--lang en` сейчас не работает ни у тех, ни у других:
словаря `fig_strings_en.py` у Семинара 7 нет. Выбор одного способа — работа
сведения, не этой сессии; сказано здесь, чтобы оно не обнаружилось случайно.

    python3 make_figures_c2.py

Нумерация `c2-NN` временная: окончательные номера слайдов даёт оркестратор при
сведении. При переименовании правятся три места — имена PNG, поля
`visual.figure` в двух слайдах и строки с именами в этом докстринге.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

DEEP = (0x21, 0x29, 0x5C)
MID = (0x06, 0x5A, 0x82)
LIGHT = (0x1C, 0x72, 0x93)
TEAL = (0x02, 0x80, 0x90)
GOLD_DARK = (0x8A, 0x62, 0x00)
SURF = (0xF4, 0xF7, 0xFA)
WARM = (0xFF, 0xF7, 0xE2)
PALE = (0xE6, 0xEE, 0xF4)
INK = (0x14, 0x1B, 0x2E)
MUTE = (0x5B, 0x6B, 0x7F)
WHITE = (255, 255, 255)

MW = 1600                     # холст = рабочая ширина слайда 12,23″
PT_PER_PX = 12.23 * 72 / MW   # 0,55 pt на пиксель
FLOOR_PT = 7.5                # пол кегля деки

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

_FONTS = []
_DREW = []
_WARN = []


def f(size, bold=False):
    _FONTS.append(size)
    return ImageFont.truetype(FB if bold else F, size)


def text(d, x, y, s, size=20, col=INK, bold=False):
    d.text((x, y), s, font=f(size, bold), fill=col)


def cent(d, x0, w, y, s, size=20, col=INK, bold=False):
    fo = f(size, bold)
    d.text((x0 + (w - d.textlength(s, font=fo)) / 2, y), s, font=fo, fill=col)


def right(d, x1, y, s, size=20, col=INK, bold=False):
    fo = f(size, bold)
    d.text((x1 - d.textlength(s, font=fo), y), s, font=fo, fill=col)


def wrap(d, s, size, max_w, bold=False):
    fo = f(size, bold)
    out, line = [], ""
    for word in s.split():
        probe = (line + " " + word).strip()
        if d.textlength(probe, font=fo) <= max_w or not line:
            line = probe
        else:
            out.append(line)
            line = word
    if line:
        out.append(line)
    return out


def block(d, x, y, w, h, s, size=19, col=INK, bold=False, lh=1.34):
    """Абзац по центру коробки — и по горизонтали, и по вертикали.

    Вертикаль здесь не украшение: коробки одного ряда одной высоты, а строк
    текста в них разное число, и текст, посаженный от верхней грани, даёт
    ряд, который визуально валится вверх."""
    lines = wrap(d, s, size, w, bold)
    step = int(size * lh)
    y0 = y + (h - len(lines) * step) / 2
    for i, line in enumerate(lines):
        cent(d, x, w, y0 + i * step, line, size, col, bold)


def box(d, x, y, w, h, *, fill=SURF, stroke=LIGHT, sw=3, r=14):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=stroke, width=sw)


def dashed(d, x, y, w, h, *, fill=WARM, stroke=GOLD_DARK, sw=3, dash=16, gap=11):
    """Пустой слот: прямые углы и пунктир — чтобы коробка читалась как МЕСТО,
    на котором ничего не стоит, а не как ещё один заполненный шаг."""
    d.rectangle([x, y, x + w, y + h], fill=fill)
    for x0 in range(int(x), int(x + w), dash + gap):
        x1 = min(x0 + dash, x + w)
        d.rectangle([x0, y, x1, y + sw - 1], fill=stroke)
        d.rectangle([x0, y + h - sw + 1, x1, y + h], fill=stroke)
    for y0 in range(int(y), int(y + h), dash + gap):
        y1 = min(y0 + dash, y + h)
        d.rectangle([x, y0, x + sw - 1, y1], fill=stroke)
        d.rectangle([x + w - sw + 1, y0, x + w, y1], fill=stroke)


def arrow(d, x0, x1, y, *, col=LIGHT, sw=4, head=14):
    d.line([x0, y, x1 - head, y], fill=col, width=sw)
    d.polygon([(x1, y), (x1 - head, y - head * 0.62), (x1 - head, y + head * 0.62)], fill=col)


def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def save(im, name):
    im.save(OUT / name)
    lo = min(_FONTS) if _FONTS else 0
    _DREW.append((name, im.size, lo))
    if lo * PT_PER_PX < FLOOR_PT:
        _WARN.append(f"{name}: кегль {lo} px = {lo * PT_PER_PX:.1f} pt — ниже пола {FLOOR_PT} pt")
    _FONTS.clear()


# ═══════════════════════════════════════════════════════════════════════════
# c2-02 — одна и та же цифра в двух цепочках; во второй гейта нет
#
# Средний столбец — ось сравнения: в нём стоит то, что находится МЕЖДУ цифрой
# и действием. На сайте там человек, внутри Zillow Offers — пустой слот. Без
# первой строки пустота во второй не читается: пустое место видно только
# рядом с заполненным.
# ═══════════════════════════════════════════════════════════════════════════
H = 486
im = Image.new("RGB", (MW, H), WHITE)
d = ImageDraw.Draw(im)

C1, W1 = 252, 250
C2, W2 = 596, 420
C3, W3 = 1096, 486

# Светлая полоса за средним столбцом: он здесь ось сравнения, и пустота во
# второй строке читается как ПУСТОЕ МЕСТО в размеченном столбце, а не как
# пропуск в рисунке. Двумя кусками, по одному на строку: сплошная полоса во
# всю высоту проходила под подписями строк, и те читались наполовину
# подсвеченными без всякой на то причины.
BAND = (0xF2, 0xF6, 0xFA)
d.rounded_rectangle([C2 - 26, 2, C2 + W2 + 26, 178], radius=16, fill=BAND)
d.rounded_rectangle([C2 - 26, 244, C2 + W2 + 26, 386], radius=16, fill=BAND)

cent(d, C1, W1, 10, "Цифра", 20, MID, True)
cent(d, C2, W2, 10, "Что стоит между цифрой и действием", 20, MID, True)
cent(d, C3, W3, 10, "Действие", 20, MID, True)

# ── строка 1: сайт ────────────────────────────────────────────────────────
Y1, BH = 54, 116
text(d, 14, Y1 + 32, "На сайте Zillow", 21, DEEP, True)
text(d, 14, Y1 + 62, "годами", 19, MUTE)

box(d, C1, Y1, W1, BH)
cent(d, C1, W1, Y1 + 44, "Zestimate", 25, MID, True)

box(d, C2, Y1, W2, BH, stroke=TEAL)
block(d, C2 + 20, Y1, W2 - 40, BH, "Человек. Смотрит, сравнивает с другими домами, торгуется", 19)

box(d, C3, Y1, W3, BH)
block(d, C3 + 20, Y1, W3 - 40, BH, "Покупает или ждёт. Риск и деньги его собственные", 19)

arrow(d, C1 + W1 + 8, C2 - 8, Y1 + BH / 2)
arrow(d, C2 + W2 + 8, C3 - 8, Y1 + BH / 2)

text(d, C1, Y1 + BH + 14, "Проверкой здесь был сам человек, и ничего не ломалось.", 20, TEAL)

d.line([14, 232, MW - 14, 232], fill=PALE, width=3)

# ── строка 2: Zillow Offers ───────────────────────────────────────────────
Y2 = 262
text(d, 14, Y2 + 32, "В Zillow Offers", 21, DEEP, True)
text(d, 14, Y2 + 62, "2018–2021", 19, MUTE)

box(d, C1, Y2, W1, BH)
cent(d, C1, W1, Y2 + 44, "Zestimate", 25, MID, True)

dashed(d, C2, Y2, W2, BH)
cent(d, C2, W2, Y2 + 44, "ничего", 25, GOLD_DARK, True)

box(d, C3, Y2, W3, BH, fill=DEEP, stroke=DEEP)
block(d, C3 + 20, Y2, W3 - 40, BH,
      "Zillow покупает этот дом по этой цене. Капитал потрачен", 19, WHITE, True)

arrow(d, C1 + W1 + 8, C2 - 8, Y2 + BH / 2)
arrow(d, C2 + W2 + 8, C3 - 8, Y2 + BH / 2, col=GOLD_DARK)

text(d, C1, Y2 + BH + 14, "Цифра дошла до обязательства без остановки.", 20, GOLD_DARK)

cent(d, 0, MW, H - 42, "Модель в обеих строках одна и та же.", 22, DEEP, True)
# Имя файла — ПО ССЫЛКЕ СЛАЙДА (`slides/n11-*.md` `visual.figure`), не по
# провизорному номеру круга сведения: было `zillow-c2-02-dve-tsepochki.png`,
# пока слайд этой схемы не получил финальный сквозной номер n11. Переименован
# при технической сборке финальной нумерации — иначе повторный запуск этого
# генератора писал бы файл, которого ни один слайд не читает, а тот, что
# дека реально использует, оставался бы несвязанным со своим источником.
save(im, "zillow-n11-dve-tsepochki.png")


# ═══════════════════════════════════════════════════════════════════════════
# c2-04 — спектр цены и обратимости линией, две точки на нём
#
# Линия, а не таблица: таблица уравнивает соседние ячейки по площади, и
# «недовольный клиент» получает столько же места, сколько списание в сотни
# миллионов. Клин растёт к правому краю, подписи под точками намеренно разной
# природы — слово слева и сумма справа.
# ═══════════════════════════════════════════════════════════════════════════
H = 318
im = Image.new("RGB", (MW, H), WHITE)
d = ImageDraw.Draw(im)

text(d, 14, 8, "Что цепочка сделает сразу после текущего шага", 20, MID, True)

AX, BX, AY = 120, 1470, 128
text(d, AX, 48, "отменяется одним действием", 19, MUTE)
right(d, 1510, 48, "одним действием не отменить", 19, MUTE)

# Клин, а не линия равной толщины: толщина и цвет растут слева направо — ось
# непрерывна, и промежуточных делений на ней нет намеренно (в коде их тоже
# нет, они есть только в цене). Переход через DEEP, а не напрямую из бирюзы
# в золото: прямое смешение этих двух даёт болотно-зелёную середину.
for px in range(AX, BX):
    t = (px - AX) / (BX - AX)
    half = 2 + 7 * t
    col = mix(LIGHT, DEEP, t / 0.6) if t < 0.6 else mix(DEEP, GOLD_DARK, (t - 0.6) / 0.4)
    d.line([px, AY - half, px, AY + half], fill=col)
d.polygon([(1512, AY), (BX, AY - 17), (BX, AY + 17)], fill=GOLD_DARK)

PA, PB = 332, 1282
for px, col in ((PA, TEAL), (PB, GOLD_DARK)):
    d.line([px, AY + 18, px, AY + 40], fill=mix(col, WHITE, 0.62), width=3)
d.ellipse([PA - 13, AY - 13, PA + 13, AY + 13], fill=TEAL, outline=WHITE, width=3)
d.ellipse([PB - 19, AY - 19, PB + 19, AY + 19], fill=GOLD_DARK, outline=WHITE, width=3)

cent(d, PA - 200, 400, AY + 44, "Черновик письма", 23, DEEP, True)
cent(d, PA - 200, 400, AY + 78, "потерянное время", 19, MUTE)

cent(d, PB - 220, 440, AY + 44, "Покупка дома", 23, DEEP, True)
cent(d, PB - 220, 440, AY + 76, "$407,9 млн", 29, GOLD_DARK, True)

cent(d, 0, MW, H - 40,
     "Чем правее следующий шаг, тем дороже проверка, сэкономленная перед ним.", 21, DEEP, True)
# Имя файла — ПО ССЫЛКЕ СЛАЙДА (`slides/n13-*.md` `visual.figure`), то же
# переименование и та же причина, что у схемы выше (было
# `zillow-c2-04-spektr.png`).
save(im, "zillow-n13-spektr.png")


# ═══════════════════════════════════════════════════════════════════════════
print("схемы кейса Zillow:")
for name, size, lo in _DREW:
    w_in = 12.23
    h_in = w_in * size[1] / size[0]
    print(f"  {name}  {size[0]}×{size[1]} px = {w_in:.2f}″×{h_in:.2f}″  "
          f"пол кегля {lo} px = {lo * PT_PER_PX:.1f} pt")
for w in _WARN:
    print("  ВНИМАНИЕ:", w)
if not _WARN:
    print("  кегль: обе схемы выше пола 7,5 pt")
