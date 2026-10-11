#!/usr/bin/env python3
"""Схемы кейса Optum/UnitedHealth (провизорные слайды `c5-01`…`c5-04`).

Первая рисовалка схем Семинара 7: до этого круга ни один слайд деки не
объявлял `visual.figure`, папка `figures/` была пуста, а `FIGS` в
`build_sem07.py` — пустым словарём. Устройство — по образцу
`sem-06/rendered/fig_toolkit.py` (PIL, та же палитра Ocean, те же шрифты
DejaVu), но КОПИЕЙ, а не импортом: `sem-06/**` этим кругом не трогается, и
тащить оттуда тулкит на одну схему было бы дороже, чем держать её
самодостаточной.

## c5-02 — «один и тот же балл, разная тяжесть» (два столбика)

Замена таблице из двух строк («белый пациент / чёрный пациент — балл —
реальная тяжесть»), которую опус-ревью назвало строками таблицы без
человека. Суть кейса на одной картинке: ДВА столбика разной высоты и
ОДИНАКОВАЯ подпись под каждым.

Три решения по этой схеме, каждое — ответ на вопрос «откуда число»:

* **Высота столбиков — 26,3%.** Это замер самого исследования: среди
  пациентов, отнесённых к самому высокому разряду риска, у чёрных пациентов
  на 26,3% больше хронических заболеваний при сопоставимом балле
  (Obermeyer et al., Science, 2019; формулировка сверена по разбору
  Scientific American от 24.10.2019, прямое чтение страницы). Поэтому
  левый столбик — база (100), правый — 126,3, и отношение высот на схеме
  равно отношению чисел, а не «заметно выше» на глаз.
* **Разряд риска назван на схеме.** 26,3% измерены в верхнем разряде риска —
  том, по которому и отбирают в программу, — а не на середине списка.
  Подпись об этом стоит внутри картинки: без неё число читалось бы как
  свойство любой пары пациентов с одинаковым баллом.
* **Золотым залит только прирост.** Верхний сегмент правого столбика (те
  самые 26,3%) — `GOLD`, остальная высота — `MID`, как у левого. Акцент
  получает ровно та величина, которая и есть содержание слайда; счётчик
  золотых пикселей (§7, порог ≥300 на слайд) при этом закрывается самим
  содержанием, без декоративной полоски.

Кегль: самый мелкий текст схемы — 26 px на холсте 2400 px, который встаёт в
12,23″ ширины слайда (196 px/″), то есть 9,5 pt — выше порога 7,5 pt (§7).
Пропорция холста 2400×560 выбрана так, чтобы схема вставала в 2,85″ по
высоте и оставляла место двум блокам-цитатам слайда: при более высоком
холсте `K.figure` ужала бы её по ширине и кегль уехал бы вниз вместе с ней.

Имя файла схемы — БЕЗ номера слайда: номера кейса (`c5-NN`) провизорные,
сквозной счёт сведёт машина при сборке, и номер внутри имени схемы пережил бы
это сведение молча (то же решение, что в `make_figures_c4.py`).

    python3 make_figures_c5.py          # пишет figures/optum-c5-*.png
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
GOLD = (0xF0, 0xAB, 0x00)
GOLD_INK = (0x8A, 0x62, 0x00)
SURF = (0xF4, 0xF7, 0xFA)
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
    for i, line in enumerate(wrap(d, s, f, width)):
        text(d, (x, y + i * step), line, f, color)
    return y + len(wrap(d, s, f, width)) * step


def dashed(d, x0, x1, y, color, dash=18, gap=12, w=5):
    x = x0
    while x < x1:
        d.line([(x, y), (min(x + dash, x1), y)], fill=color, width=w)
        x += dash + gap


def odin_ball_dva_stolbika(path):
    """Два столбика разной высоты под одной и той же подписью.

    Подписи групп стоят ВНУТРИ столбиков, а не над ними: над правым столбиком
    места нет вовсе (его вершина — потолок рабочего поля схемы), и первый
    прогон этого круга дал ровно то, что и должен был, — «чёрный пациент»
    поверх верхней подписи. Подпись внутри заливки решает это без второго
    яруса по высоте, которого на холсте 560 px просто нет.

    Множественное число («белые пациенты») — не стиль, а точность: 26,3%
    измерены по ГРУППАМ пациентов с сопоставимым баллом, и пара конкретных
    людей таким числом не описывается. Один конкретный человек на этом слайде
    есть, но он живёт в тексте слайда, а не в подписи к столбику."""
    W, H = 2400, 560
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    f_small = font(26)
    f_name = font(36, bold=True)
    f_plate = font(30)
    f_big = font(80, bold=True)
    f_mid = font(34, bold=True)

    base_y = 420                      # общая нижняя граница столбиков
    top_y = 96                        # вершина правого столбика
    full = base_y - top_y             # 324 px = 126,3 единицы
    unit = full / 1.263               # 100 единиц — левый столбик
    bw, gap = 380, 130
    x1 = 250
    x2 = x1 + bw + gap

    paragraph(d, x1 - 40, 18,
              "высота столбика — среднее число активных хронических заболеваний "
              "по прямому измерению", f_small, MUTE, 1000, 34)

    # Числовая шкала слева от столбиков — правка круга 5 по замечанию студента:
    # без оси пропорцию высот приходится принимать на веру, а 26,3% читается
    # как подпись к картинке, не как измеримое отношение. База 100 (вершина
    # левого столбика) и метка 126,3 (вершина правого) делают отношение высот
    # проверяемым глазом прямо на схеме, независимо от текста справа.
    AXIS_X = x1 - 90
    d.line([(AXIS_X, base_y), (AXIS_X, top_y - 6)], fill=MUTE, width=4)
    for val, label in ((0, "0"), (50, "50"), (100, "100"), (126.3, "126,3")):
        y = base_y - unit * (val / 100)
        d.line([(AXIS_X - 12, y), (AXIS_X + 10, y)], fill=MUTE, width=4)
        text(d, (AXIS_X - 20, y), label, f_small, MUTE, anchor="rm")

    d.rectangle([x1, base_y - unit, x1 + bw, base_y], fill=MID)
    d.rectangle([x2, base_y - unit, x2 + bw, base_y], fill=MID)
    d.rectangle([x2, top_y, x2 + bw, base_y - unit], fill=GOLD)
    d.line([(x2, base_y - unit), (x2 + bw, base_y - unit)], fill=WHITE, width=3)
    d.line([(x1 - 40, base_y), (x2 + bw + 40, base_y)], fill=DEEP, width=6)

    text(d, (x1 + bw / 2, base_y - 28), "белые пациенты", f_name, WHITE, anchor="md")
    text(d, (x2 + bw / 2, base_y - 28), "чёрные пациенты", f_name, WHITE, anchor="md")

    # пунктир от вершины левого столбика — докуда дотянулся бы правый, будь
    # тяжесть одинаковой
    dashed(d, x1 + bw, x2 + bw + 86, base_y - unit, MUTE)

    # мерная стрелка прироста
    xa = x2 + bw + 50
    d.line([(xa, base_y - unit - 4), (xa, top_y + 4)], fill=GOLD_INK, width=7)
    for yy, dy in ((top_y, 1), (base_y - unit, -1)):
        d.polygon([(xa, yy), (xa - 14, yy + 20 * dy), (xa + 14, yy + 20 * dy)],
                  fill=GOLD_INK)

    # одинаковая подпись под КАЖДЫМ столбиком — то, ради чего схема
    for x in (x1, x2):
        d.rounded_rectangle([x, base_y + 18, x + bw, base_y + 112], radius=12,
                            fill=SURF, outline=LIGHT, width=4)
        text(d, (x + bw / 2, base_y + 48), "один и тот же", f_plate, DEEP, anchor="mm")
        text(d, (x + bw / 2, base_y + 84), "балл риска", f_plate, DEEP, anchor="mm")

    rx = x2 + bw + 150
    rw = W - rx - 60
    text(d, (rx, top_y - 16), "+26,3%", f_big, GOLD_INK)
    paragraph(d, rx, top_y + 110,
              "активных хронических заболеваний при сопоставимом балле риска",
              f_mid, DEEP, rw, 46)
    y = paragraph(d, rx, base_y - 40,
                  "Замер среди пациентов самого высокого разряда риска — того, "
                  "по которому и отбирают в программу усиленного наблюдения.",
                  f_small, MUTE, rw, 38)
    text(d, (rx, y + 10), "Obermeyer et al., Science, 2019.", f_small, MUTE)

    img.save(path)
    print(f"{path.name}: {W}×{H}, самый мелкий кегль {min(_USED)} px "
          f"({min(_USED) / 196.2 * 72:.1f} pt на слайде)")


def main():
    OUT.mkdir(exist_ok=True)
    odin_ball_dva_stolbika(OUT / "optum-c5-odin-ball-dva-stolbika.png")


if __name__ == "__main__":
    main()
