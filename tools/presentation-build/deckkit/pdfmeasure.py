# -*- coding: utf-8 -*-
"""МЕРА ПО СОБРАННОМУ PDF — а не по числам, которые назвал сам сборщик.

ЗАЧЕМ ЭТОТ МОДУЛЬ ЕСТЬ. Трижды в этой работе сборка рапортовала одно, а зал
увидел другое, и каждый раз причина была одна: мерили собственный вход, а не
вывод. Самый дорогой случай — пол кегля. Отчёт сборки сказал «14 кадров ниже
12 пт», потому что `metrics.check_proj` смотрит МАСШТАБ ПРОГОНА ТЕЛА и
больше ни на что. По PDF той же деки ниже 12 пт набрано 24% всех видимых
знаков на 87 кадрах из 122: подписи плашек (10 пт капителью), оговорки под
числом (10,5 пт курсивом), подписи схем. Сборщик о них не говорил не потому,
что ошибался в арифметике, — он их не считал вовсе, и узнать это по его
собственному отчёту было нельзя ни при каком чтении.

ЧЕМ МЕРИТ. Потоком содержимого самого PDF: `Tf` даёт кегль, которым
LibreOffice НА САМОМ ДЕЛЕ набрал прогон, `cm` перед `Do` — рамку, в которую
он НА САМОМ ДЕЛЕ положил картинку. Между сборщиком и этими числами лежит
весь рендер, поэтому несовпадение меры с рендером здесь видно, а не
предполагается.

ЧЕГО ЗДЕСЬ НЕТ. Разбора шрифтовых таблиц и настоящего текста: коды глифов в
этих файлах — двухбайтовые CID подмножества, и обратное отображение в буквы
требует `ToUnicode`, которого модулю не нужно. Он считает ЧИСЛО ЗНАКОВ и их
КЕГЛЬ — ровно то, чем мерится «что зал читает мелким». Где нужен сам текст,
берётся `pdftotext`, и это сказано на месте.

Кегль округляется до 0,05 пт: LibreOffice пишет 27,014 вместо 27 — холст
959,98 пт вместо 960, и вся страница идёт с этим множителем. Округление
снимает его, не пряча настоящих различий (ступень лестницы 0,5 пт в десять
раз крупнее).
"""
import re
import zlib
from collections import Counter
from pathlib import Path

_OBJ = re.compile(rb"(\d+) 0 obj(.*?)endobj", re.S)
_STREAM = re.compile(rb"stream\r?\n(.*?)\r?\nendstream", re.S)
_PAGE = re.compile(rb"/Type\s*/Page(?![a-zA-Z])")
_NUM = r"[-+]?[0-9.]+"


def _objects(raw):
    return {int(m.group(1)): m.group(2) for m in _OBJ.finditer(raw)}


def _content(objs, body):
    """Поток содержимого страницы, распакованный. `/Contents` бывает и
    массивом ссылок — тогда потоки склеиваются в порядке массива."""
    m = re.search(rb"/Contents\s*(\d+) 0 R", body)
    ids = [int(m.group(1))] if m else []
    if not ids:
        m = re.search(rb"/Contents\s*\[(.*?)\]", body, re.S)
        if m:
            ids = [int(x) for x in re.findall(rb"(\d+) 0 R", m.group(1))]
    out = []
    for i in ids:
        sm = _STREAM.search(objs.get(i, b""))
        if not sm:
            continue
        data = sm.group(1)
        try:
            data = zlib.decompress(data)
        except zlib.error:
            pass
        out.append(data.decode("latin1"))
    return "\n".join(out)


def pages(pdf):
    """Страницы PDF: `(номер с 1, поток содержимого, рамка страницы)`.

    Порядок берётся по номеру объекта, а не по дереву `/Pages`: у файлов
    этого курса дерево плоское и объекты страниц идут по порядку кадров —
    проверено на обеих деках. Дерево разбирать не нужно, и честнее сказать
    это, чем сделать вид, что разобрали."""
    raw = Path(pdf).read_bytes()
    objs = _objects(raw)
    out = []
    for n in sorted(objs):
        b = objs[n]
        # Пробел между `/Type` и `/Page` НЕОБЯЗАТЕЛЕН: `python-pptx`+
        # LibreOffice пишут его, MuPDF (которым склеены прежние выпуски
        # этой деки) — нет. Поиск по строке с пробелом давал на таком файле
        # НОЛЬ страниц и ноль знаков, то есть «всё хорошо» на файле, который
        # просто не прочитан. Ровно тот класс молчания, ради которого этот
        # модуль и заведён.
        if not _PAGE.search(b) or b"/Pages" in b:
            continue
        mb = re.search(rb"/MediaBox\s*\[(.*?)\]", b)
        box = tuple(float(x) for x in mb.group(1).split()) if mb else \
            (0.0, 0.0, 960.0, 540.0)
        out.append((len(out) + 1, _content(objs, b), box))
    return out


# ── текст ───────────────────────────────────────────────────────────


def _glyphs(arg):
    """Сколько знаков в операнде `TJ`/`Tj`. Шестнадцатеричная строка — по
    два байта на знак (CID подмножества), обычная — по знаку, со снятыми
    экранами."""
    n = 0
    for m in re.finditer(r"<([0-9A-Fa-f\s]*)>|\(((?:\\.|[^)\\])*)\)", arg):
        if m.group(0) == "BT":
            x = y = 0.0
        elif m.group(1) is not None:
            n += len(re.sub(r"\s", "", m.group(1))) // 4
        else:
            n += len(re.sub(r"\\(.)", r"\1", m.group(2)))
    return n


def text_runs(stream, *, grid=0.05):
    """Прогоны текста страницы: `(кегль, знаков, x, y)`.

    Кегль — произведение `Tf` на вертикальный масштаб матрицы текста: оба
    множителя настоящие, и ни один из них нельзя опустить (`Tm` со
    масштабом встречается у повёрнутых надписей).

    `Td` СКЛАДЫВАЕТСЯ внутри одного текстового объекта и ОБНУЛЯЕТСЯ на `BT`:
    смещение задано относительно матрицы строки, а та на `BT` единичная.
    Без обнуления подвал из двадцати прогонов со ссылками уводил точку на
    пятнадцать тысяч пунктов вправо — и всякая мера «где на кадре стоит эта
    строка» становилась мусором, молча (кегль при этом оставался верным,
    поэтому замер мелкого текста ошибку пережил, а замер заголовка — нет)."""
    out = []
    size, scale, x, y = 0.0, 1.0, 0.0, 0.0
    for m in re.finditer(
            r"\bBT\b"
            rf"|/[A-Za-z0-9+.]+\s+({_NUM})\s+Tf"
            rf"|({_NUM})\s+({_NUM})\s+(?:Td|TD)"
            rf"|({_NUM})\s+({_NUM})\s+({_NUM})\s+({_NUM})\s+"
            rf"({_NUM})\s+({_NUM})\s+Tm"
            r"|(\[[^]]*\]\s*TJ|\((?:\\.|[^)\\])*\)\s*Tj|<[0-9A-Fa-f\s]*>\s*Tj)",
            stream):
        if m.group(0) == "BT":
            x = y = 0.0
        elif m.group(1) is not None:
            size = float(m.group(1))
        elif m.group(2) is not None:
            x, y = x + float(m.group(2)), y + float(m.group(3))
        elif m.group(4) is not None:
            scale = abs(float(m.group(7))) or 1.0
            x, y = float(m.group(8)), float(m.group(9))
        elif m.group(10) is not None:
            n = _glyphs(m.group(10))
            if n:
                out.append((round(size * scale / grid) * grid, n, x, y))
    return out


def size_hist(pdf, *, grid=0.05):
    """Знаков на кегль по всей деке, и по кадрам — какие кегли на каком.

    Возвращает `(счётчик кеглей, {номер кадра: {кегль: знаков}})`."""
    total, by_page = Counter(), {}
    for n, stream, _box in pages(pdf):
        per = Counter()
        for size, cnt, _x, _y in text_runs(stream):
            per[size] += cnt
        total.update(per)
        by_page[n] = per
    return total, by_page


def below(hist, limit):
    """Знаков ниже порога и доля от всех."""
    lo = sum(c for s, c in hist.items() if s < limit - 1e-9)
    tot = sum(hist.values())
    return lo, tot, (lo / tot if tot else 0.0)


# ── картинки и фигуры ───────────────────────────────────────────────


def images(stream):
    """Картинки страницы: `(имя, (x0, y0, x1, y1))` в пунктах PDF.

    Рамка берётся из матрицы `cm`, действующей на `Do`: единичный квадрат
    картинки отображается ею, то есть `e, f` — левый нижний угол, `a, d` —
    ширина и высота. Поворот/наклон (`b`, `c` не ноль) здесь не
    встречается, и если встретится, рамка будет посчитана неверно — поэтому
    такой случай называется вслух, а не проглатывается."""
    out, stack, cur = [], [], None
    for m in re.finditer(
            rf"\bq\b|\bQ\b|({_NUM})\s+({_NUM})\s+({_NUM})\s+({_NUM})\s+"
            rf"({_NUM})\s+({_NUM})\s+cm|/([A-Za-z0-9+._]+)\s+Do",
            stream):
        t = m.group(0)
        if t == "q":
            stack.append(cur)
        elif t == "Q":
            cur = stack.pop() if stack else None
        elif m.group(7):
            if cur:
                a, b, c, d, e, f = cur
                out.append((m.group(7), (min(e, e + a), min(f, f + d),
                                         max(e, e + a), max(f, f + d)),
                            abs(b) > 1e-6 or abs(c) > 1e-6))
        else:
            cur = tuple(float(m.group(i)) for i in range(1, 7))
    return out


_PATH_OP = re.compile(
    rf"({_NUM})\s+({_NUM})\s+m\b"
    rf"|({_NUM})\s+({_NUM})\s+l\b"
    rf"|(?:{_NUM}\s+){{4}}({_NUM})\s+({_NUM})\s+c\b"
    rf"|({_NUM})\s+({_NUM})\s+({_NUM})\s+({_NUM})\s+re\b"
    rf"|({_NUM})\s+({_NUM})\s+({_NUM})\s+(RG|rg)\b"
    r"|\b(f\*|f|S|B\*|B)\b")


def paths(stream):
    """Залитые и обведённые фигуры страницы: `(рамка, цвет заливки, цвет
    обводки, операция)`. Цвет — тройка 0…1 либо None.

    Кривые Безье учитываются ТОЛЬКО опорными точками (последняя пара `c`):
    рамка округлённой коробки от этого занижается на радиус скругления в
    углах, то есть на доли пункта. Для вопроса «накрывает ли картинка
    грань коробки» этого довольно, и занижение здесь работает в сторону
    осторожности — названо, чтобы его не приняли за точную рамку."""
    out = []
    xs, ys = [], []
    fill = stroke = None
    for m in _PATH_OP.finditer(stream):
        g = m.groups()
        if g[0]:
            xs.append(float(g[0])); ys.append(float(g[1]))
        elif g[2]:
            xs.append(float(g[2])); ys.append(float(g[3]))
        elif g[4]:
            xs.append(float(g[4])); ys.append(float(g[5]))
        elif g[6]:
            x, y, w, h = (float(v) for v in g[6:10])
            xs += [x, x + w]; ys += [y, y + h]
        elif g[13]:
            col = tuple(float(v) for v in g[10:13])
            if g[13] == "rg":
                fill = col
            else:
                stroke = col
        elif g[14]:
            if xs and ys:
                out.append(((min(xs), min(ys), max(xs), max(ys)),
                            fill if "f" in g[14] or "B" in g[14] else None,
                            stroke if g[14][0] in "SB" else None, g[14]))
            xs, ys = [], []
    return out


def overlap(a, b):
    """Площадь пересечения двух рамок в пунктах, и сами перехлёсты по осям."""
    dx = min(a[2], b[2]) - max(a[0], b[0])
    dy = min(a[3], b[3]) - max(a[1], b[1])
    return (max(0.0, dx) * max(0.0, dy), dx, dy)


def rgb(col):
    """Цвет PDF (0…1) → `#rrggbb`, чтобы сверять с палитрой темы."""
    if col is None:
        return None
    return "#" + "".join(f"{int(round(c * 255)):02x}" for c in col)
