#!/usr/bin/env python3
"""Схемы кейса IRS (провизорные слайды `c6-01`…`c6-05`).

Устройство — по образцу `make_figures_c5.py` того же круга: самодостаточная
рисовалка на PIL, палитра Ocean теми же HEX, что `deck_kit.py`, шрифты DejaVu.
Копия помощников, а не импорт: `fig_toolkit` несёт разбор `--lang` и словарь,
которого у этого занятия ещё нет, и тащить его сюда на две схемы дороже, чем
держать обе самодостаточными (то же решение и та же причина, что у c5).

Имена файлов — по кейсу (`irs-c6-…`), БЕЗ номера слайда: номера `c6-NN`
провизорные, сквозной счёт сведёт `renumber_slides.py`, и номер внутри имени
схемы пережил бы сведение молча.

## irs-c6-tsena-pisma — чего стоит письмо о проверке заявителю EITC

Замена таблице «белый / чёрный — та же декларация — разная вероятность»,
которая по форме повторяла таблицу кейса Optum на экран раньше (болезнь №7,
`tools/seminar-production/README.md` §4.1 — одинаковые машины подряд). Здесь
другая фигура и другое содержание: человек и цена (§4.2 П2), которых у этого
кейса на экране не было вовсе.

Брусок — год, на который бюджет семьи распределён заранее с учётом уже
заявленного возврата. Золотой штырь — письмо о проверке, падающее в середину
этого года. Две плашки под бруском — то, во что письмо обходится: дни на сбор
документов и часть возврата под риском. Подпись внизу — та же задержка по
бюджету с более высоким и устойчивым доходом.

Все пять утверждений схемы — дословно из `rework/section-2-routing-part4b.md`
§B.1; ни одно число здесь не вводится, числа живут в блоке-цитате слайда.

## irs-c6-lestnitsa-deshevizny — спуск, на котором ни один шаг не ошибается

Главная схема кейса и носитель его поворота. Форма сознательно НЕ повторяет
ни таблицу разбора Optum, ни горизонтальный конвейер механики цепочки: это
лестница ВНИЗ из четырёх ступеней, где каждая стрелка подписана «верно», а
внизу справа стоит исход. Поворот читается с картинки до слов: золотом залита
ВЕРХНЯЯ ступень — постановка цели, — потому что единственное сломанное место
находится там, а весь спуск под ней безупречен.

Почему золото именно на верхней ступени: в кейсе Optum ломается измерение
(удобный признак встал на место нужной величины), здесь — выбор самой
величины. Это ДРУГАЯ поломка, и она ловится другой проверкой: сравнение
признака с прямым измерением на этой лестнице проходит чисто. Золотой пиксель
получает ровно та ступень, которая и есть содержание слайда (§7, порог ≥300
золотых пикселей на слайд закрывается содержанием).

Кегль: самый мелкий текст обеих схем — 26 px на холсте 2400 px, который
встаёт в 12,23″ ширины слайда (196 px/″), то есть 9,5 pt — выше порога
7,5 pt (§7).

    python3 make_figures_c6.py          # пишет figures/irs-c6-*.png
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "figures"

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

DEEP = (0x21, 0x29, 0x5C)
MID = (0x06, 0x5A, 0x82)
LIGHT = (0x1C, 0x72, 0x93)
TEAL = (0x02, 0x80, 0x90)
GOLD = (0xF0, 0xAB, 0x00)
GOLD_INK = (0x8A, 0x62, 0x00)
SURF = (0xF4, 0xF7, 0xFA)
INK = (0x14, 0x1B, 0x2E)
MUTE = (0x5B, 0x6B, 0x7F)
WHITE = (255, 255, 255)

MIN_PX = 26          # 9,5 pt на холсте 2400 px в 12,23″ — порог §7 (7,5 pt)
_USED = []


def font(size, bold=False):
    if size < MIN_PX:
        raise SystemExit(f"кегль {size} px ниже порога {MIN_PX} px (7,5 pt)")
    _USED.append(size)
    return ImageFont.truetype(FB if bold else F, size)


def text(d, xy, s, f, color, anchor="la"):
    d.text(xy, s, font=f, fill=color, anchor=anchor)


def wrap(d, s, f, width):
    out, line = [], ""
    for w in s.split():
        probe = f"{line} {w}".strip()
        if d.textlength(probe, font=f) <= width or not line:
            line = probe
        else:
            out.append(line)
            line = w
    if line:
        out.append(line)
    return out


def paragraph(d, x, y, s, f, color, width, step):
    lines = wrap(d, s, f, width)
    for i, line in enumerate(lines):
        text(d, (x, y + i * step), line, f, color)
    return y + len(lines) * step


def plate(d, x, y, w, h, s, f, *, fill=SURF, border=LIGHT, color=DEEP,
          pad=22, step=None, bold_border=4):
    d.rounded_rectangle([x, y, x + w, y + h], radius=12, fill=fill,
                        outline=border, width=bold_border)
    step = step or f.size + 8
    lines = wrap(d, s, f, w - 2 * pad)
    y0 = y + (h - len(lines) * step + (step - f.size)) / 2
    for i, line in enumerate(lines):
        text(d, (x + w / 2, y0 + i * step), line, f, color, anchor="ma")


def arrow(d, x1, y1, x2, y2, color=TEAL, width=6, head=18):
    import math
    d.line([(x1, y1), (x2, y2)], fill=color, width=width)
    a = math.atan2(y2 - y1, x2 - x1)
    d.polygon([(x2, y2),
               (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45)),
               (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))],
              fill=color)


# ── Схема 1 ────────────────────────────────────────────────────────────────

def tsena_pisma(path):
    """Год, распределённый заранее, и письмо о проверке посередине него."""
    W, H = 2400, 560
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    f_cap = font(28)
    f_note = font(26)
    f_body = font(30)
    f_plate = font(28)
    f_pin = font(34, bold=True)

    text(d, (120, 26), "что письмо о проверке означает заявителю EITC", f_cap, MUTE)

    pin_x = 1180
    plate(d, pin_x - 270, 88, 540, 78, "письмо о проверке", f_pin,
          fill=GOLD, border=GOLD_INK, color=WHITE)
    d.line([(pin_x, 166), (pin_x, 246)], fill=GOLD_INK, width=9)

    bar_x0, bar_x1, bar_y, bar_h = 120, 2280, 246, 62
    d.rounded_rectangle([bar_x0, bar_y, bar_x1, bar_y + bar_h], radius=10,
                        fill=SURF, outline=LIGHT, width=4)
    for i in range(1, 12):
        tx = bar_x0 + (bar_x1 - bar_x0) * i / 12
        d.line([(tx, bar_y + 12), (tx, bar_y + bar_h - 12)], fill=LIGHT, width=2)
    text(d, (bar_x1 - 16, bar_y + bar_h + 12), "конец года", f_note, MUTE,
         anchor="ra")

    # Левый край бруска — момент, когда возврат заявлен и уже разошёлся по
    # плану года. Без этой привязки подпись внизу слева читалась бы как
    # отдельная реплика, а не как отметка на самом бруске.
    d.line([(bar_x0 + 26, bar_y + bar_h), (bar_x0 + 26, 368)], fill=LIGHT, width=5)
    paragraph(d, 120, 380,
              "возврат уже заявлен и распределён по бюджету на весь год",
              f_body, DEEP, 700, 40)

    # Цена письма висит на том же золотом штыре: две плашки, к каждой —
    # ветка от штыря, иначе они читаются как самостоятельные блоки.
    d.line([(pin_x, 308), (pin_x, 348)], fill=GOLD_INK, width=7)
    d.line([(pin_x, 348), (1970, 348)], fill=GOLD_INK, width=7)
    for cx in (1290, 1970):
        d.line([(cx, 348), (cx, 380)], fill=GOLD_INK, width=7)
    plate(d, 980, 380, 620, 104, "дни на сбор документов", f_plate)
    plate(d, 1660, 380, 620, 104,
          "часть возврата под риском: семья им уже распорядилась", f_plate)

    paragraph(d, 120, 508,
              "по бюджету с более высоким и устойчивым доходом та же задержка "
              "проходит легче", f_note, MUTE, 2160, 36)

    img.save(path)
    print(f"{path.name}: {W}×{H}, самый мелкий кегль {min(_USED)} px "
          f"({min(_USED) / 196.2 * 72:.1f} pt на слайде)")


# ── Схема 2 ────────────────────────────────────────────────────────────────

STUPENI = (
    "часов у инспекторов мало, и цель отбора — больше нарушений на час",
    "декларации с EITC закрываются быстрее: короче документы, меньше статей",
    "отбор смещается к тем, кого дешевле проверить",
    "среди заявителей EITC чернокожих больше, чем в среднем по декларациям",
)


def lestnitsa_deshevizny(path):
    """Спуск из четырёх ступеней; сломана верхняя, остальные безупречны."""
    W, H = 2400, 620
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    f_step = font(28)
    f_mark = font(26, bold=True)
    f_note = font(26)
    f_num = font(84, bold=True)
    f_sub = font(30)

    x, bw, bh, dy = 60, 1240, 92, 140
    ys = tuple(24 + i * dy for i in range(4))

    for i, y in enumerate(ys):
        top = i == 0
        plate(d, x, y, bw, bh, STUPENI[i], f_step,
              fill=GOLD if top else SURF,
              border=GOLD_INK if top else LIGHT,
              color=WHITE if top else DEEP,
              pad=20, step=36, bold_border=5 if top else 4)
        if i < 3:
            arrow(d, x + 180, y + bh + 6, x + 180, y + dy - 8)
            text(d, (x + 212, y + bh + 10), "верно", f_mark, TEAL)

    # Единственное сломанное место — верхняя ступень. Метка стоит СБОКУ от
    # неё и привязана чертой, чтобы спуск читался целиком, а поломка имела
    # адрес.
    d.line([(x + bw, ys[0] + bh / 2), (x + bw + 26, ys[0] + bh / 2)],
           fill=GOLD_INK, width=6)
    text(d, (x + bw + 38, ys[0] + bh / 2), "сломано здесь", f_mark, GOLD_INK,
         anchor="lm")

    rx, rw = 1400, 940
    text(d, (rx, 252), "2,9–4,7×", f_num, GOLD_INK)
    y = paragraph(d, rx, 372,
                  "чаще аудировали чернокожих налогоплательщиков при схожих "
                  "декларациях", f_sub, DEEP, rw, 40)
    paragraph(d, rx, y + 16, "Stanford и IRS, 2023", f_note, MUTE, rw, 36)

    paragraph(d, 60, 560,
              "раса ни на одной ступени не упоминается: такого поля декларация "
              "не содержит", f_note, MUTE, 2280, 36)

    img.save(path)
    print(f"{path.name}: {W}×{H}, самый мелкий кегль {min(_USED)} px "
          f"({min(_USED) / 196.2 * 72:.1f} pt на слайде)")


def main():
    OUT.mkdir(exist_ok=True)
    tsena_pisma(OUT / "irs-c6-tsena-pisma.png")
    _USED.clear()
    lestnitsa_deshevizny(OUT / "irs-c6-lestnitsa-deshevizny.png")


if __name__ == "__main__":
    main()
