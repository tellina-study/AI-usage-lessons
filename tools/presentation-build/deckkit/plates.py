# -*- coding: utf-8 -*-
"""ПОЛОСА ПЛАШЕК `blocks:` — числа отдельными блочками, а не внутри абзаца.

Владелец, разбор 2026-10-08: «чтобы прям отдельными блочками были цифры:
было, стало, к чему привело — потому что сейчас надо из текста всё это
выискивать, это ужасно».

Контракт фронтматтера:

    blocks:
      - {label: "Было",     value: "5 500 ч", note: "ручная вычитка"}
      - {label: "Стало",    value: "10 500 ч", key: true}
      - {label: "Привело к", value: "лишний круг согласования"}

`note` необязателен. `key: true` помечает плашку с ключевым числом; не
помечено ничего — золото уходит ПОСЛЕДНЕЙ плашке, в значении которой есть
цифра. Полоса занимает СВОЮ высоту: тело кадра начинается под ней, и его
место на эту высоту меньше, поэтому перегруженный плашками кадр ужимает
тело и выдаёт предупреждение сам собой.

ЗДЕСЬ ДВА СБОРЩИКА РАСХОДЯТСЯ СИЛЬНЕЕ ВСЕГО, и расхождение не стилевое.
Обе полосы написаны по одному наказу владельца, независимо, и разошлись в
десятке мест: верхний кегль значения (23 против 28), цвет подписи (LIGHT
против TEAL), курсив у оговорки (есть против нет), поле плашки (0,15 против
0,16), обводка (1,2 против 1,4), предел строк значения (2 либо 3 по наличию
цифры против всегда 2 с предупреждением).

Сведено так: ЧИСЛА и ВИД — в `PlateStyle`, с тремя готовыми наборами
(`DEFAULT`, `LEC07`, `LEC06`), а арифметика высоты одна. Это возможно
потому, что формулы высоты у них оказались ТОЖДЕСТВЕННЫ:
`est_h(t, z, w, ls, b)` и `n_lines(t, z, w, b) * z * ls * LH / 72 * SAFE` —
одно и то же число, просто записанное двумя способами.

`DEFAULT` для новой деки — это НЕ один из двух: это геометрия lec-07
(у неё кегль значения подбирается с настоящим полом, а самое длинное слово
ищется по ШИРИНЕ, а не по числу знаков) плюс три предупреждения lec-06
(подпись в три строки, значение в три строки, оговорка длиннее трёх строк),
которых у lec-07 нет вовсе. Каждое из трёх куплено видимым наездом на
кадре `s38a` Лекции 6.
"""
import re
from dataclasses import dataclass, field, replace

from . import floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, SLATE, SURFACE, TEAL, WHITE


@dataclass(frozen=True)
class PlateStyle:
    gap: float = 0.18
    pad: float = 0.15
    max_per_row: int = 4            # плашек в ряд; больше — второй ряд
    stroke_pt: float = 1.2
    gold_stroke_pt: float = 2.0
    label_pt: float = 12.0          # пол видимого слоя, см. `floor.py`
    label_ls: float = 1.10
    label_extra: float = 0.05
    label_extra_in_box: bool = True   # отбивка под подписью входит в РАМКУ
    label_color: object = LIGHT
    label_wsafe: bool = False       # мерить подпись по суженной ширине
    value_hi: float = 23.0
    value_lo: float = 13.0
    value_floor: float = 12.0       # пол видимого слоя, см. `floor.py`
    value_ls: float = 1.08
    value_extra: float = 0.04
    value_rows_digit: int = 2       # предел строк, когда в значении есть цифра
    value_rows_word: int = 3        # … и когда это слово, а не число
    value_longest_by_width: bool = True
    value_h_wsafe: bool = False
    note_pt: float = 12.0           # пол видимого слоя, см. `floor.py`
    note_ls: float = 1.12
    note_extra: float = 0.0
    note_rows: int = 3
    note_italic: bool = True
    note_color: object = LIGHT
    note_wsafe: bool = False
    warn_overflow: bool = True      # три предупреждения lec-06
    # ЦВЕТ КЛЮЧЕВОГО ЗНАЧЕНИЯ — решение владельца О3 (`decisions-owner.md`,
    # «на весь курс»), исполненное ПЕРЕКЛЮЧАТЕЛЕМ, а не сменой темы.
    #
    # Замер приёмки по пикселям собранной страницы: золото `F0AB00` на
    # белом даёт 1,99 : 1, на поверхности `F4F7FA` — 1,85, при пороге 3,0
    # для КРУПНОГО текста. Им набрано не украшение, а значение ключевой
    # плашки — то самое число, по которому назван кадр, — и соседние
    # плашки рядом идут тёмно-синим и читаются. То есть самое важное число
    # кадра выходило самым бледным на нём, а сборка при этом молчала:
    # кегль 15,0, предупреждений ноль.
    #
    # Умолчание ОСТАВЛЕНО золотым нарочно: Лекция 6 сдана и прочитана залу,
    # и её «СОВПАЛО, 2202 фигуры, 0 расхождений» обязано пережить эту
    # правку. Дека, которой решение адресовано, объявляет цвет сама —
    # `1C7293` (5,42 : 1) либо `028090` (4,67). Золото при этом НЕ уходит с
    # кадра: оно остаётся обводкой плашки, чертой под заголовком и меткой,
    # то есть палитра курса не меняется ни на один цвет.
    #
    # Перевёрнутая плашка (заливка `21295C`, число золотом, 6,85 : 1)
    # сильнее по иерархии и владельцем ОТВЕРГНУТА: менять вид пятнадцати
    # дек по одной находке в разгар переделки нельзя.
    value_key_color: object = GOLD
    gold_fallback_last: bool = True
    total_from_rows: bool = True    # сумма рядов, а не «докуда дошёл курсор»


# Геометрия lec-07 + предупреждения lec-06 — набор для НОВОЙ деки.
DEFAULT = PlateStyle()

# Ровно то, чем собрана доставленная дека Лекции 7.
LEC07 = replace(DEFAULT, warn_overflow=False)

# Ровно то, чем собрана доставленная дека Лекции 6.
# Числа Лекции 6 ПРИШПИЛЕНЫ все до одного, в том числе те, что совпадали с
# умолчаниями класса. Пока они брались из умолчаний, этот набор означал не
# «ровно то, чем собрана доставленная дека», а «то, что осталось от
# умолчаний сегодня»: поднятие пола видимого слоя в `DEFAULT` сдвинуло бы
# доставленную деку, которую читали залу. Пришпиленное число — обещание,
# унаследованное — совпадение.
LEC06 = PlateStyle(
    gap=0.18, pad=0.16, stroke_pt=1.4,
    label_pt=10.0,
    label_ls=1.08, label_extra=0.05, label_extra_in_box=False,
    label_color=TEAL, label_wsafe=True,
    value_hi=28.0, value_lo=13.0, value_floor=13.0, value_ls=1.06,
    value_extra=0.0, value_rows_digit=2, value_rows_word=2,
    value_longest_by_width=False, value_h_wsafe=True,
    value_key_color=GOLD,
    note_pt=10.5, note_ls=1.14, note_extra=0.07, note_rows=3,
    note_italic=False, note_color=SLATE, note_wsafe=True,
    warn_overflow=True, gold_fallback_last=False, total_from_rows=False)


def plates_of(sl, st=DEFAULT):
    """Поле `blocks` → перечень плашек. Чужая форма поля не роняет сборку:
    она называется предупреждением `[плашки]` и кадр собирается без полосы.

    Эта половина у двух сборщиков совпадала почти посимвольно — одно и то же
    решение, принятое дважды."""
    raw = sl.meta.get("blocks")
    if raw in (None, "", [], {}):
        return []
    if not isinstance(raw, list):
        report.warn(f"[плашки] {sl.sid}: поле `blocks` — "
                    f"{type(raw).__name__}, а должно быть списком")
        return []
    out = []
    for i, it in enumerate(raw, 1):
        if not isinstance(it, dict):
            report.warn(f"[плашки] {sl.sid}: плашка {i} не пара label/value")
            continue
        val = it.get("value")
        p = {"label": str(it.get("label") or "").strip(),
             "value": "" if val is None else str(val).strip(),
             "note": str(it.get("note") or "").strip(),
             "key": bool(it.get("key"))}
        if not (p["label"] or p["value"]):
            report.warn(f"[плашки] {sl.sid}: плашка {i} пуста")
            continue
        out.append(p)
    if len(out) > st.max_per_row:
        report.warn(
            f"[плашки] {sl.sid}: плашек {len(out)} — в ряд встаёт не больше "
            f"{st.max_per_row}, остальные уходят во второй ряд и забирают у "
            "тела ещё одну высоту полосы")
    return out


def gold_idx(plates, st=DEFAULT):
    """Какие плашки несут ключевое число. Явное `key: true` — приоритет.

    РАСХОЖДЕНИЕ: без цифр нигде lec-07 отдаёт золото ПОСЛЕДНЕЙ плашке,
    lec-06 — никому. Прав lec-07: золото обязано быть на кадре не реже раза
    (правило палитры курса), и полоса словесных плашек без него оставляет
    кадр без акцента вовсе."""
    keyed = {i for i, p in enumerate(plates) if p["key"]}
    if keyed:
        return keyed
    nums = [i for i, p in enumerate(plates) if re.search(r"\d", p["value"])]
    if nums:
        return {nums[-1]}
    if st.gold_fallback_last and plates:
        return {len(plates) - 1}
    return set()


def _rows_max(value, st):
    """Строк, в которые значение ОБЯЗАНО уложиться при подборе кегля.

    РАСХОЖДЕНИЕ: lec-07 даёт словесному значению три строки, числу — две;
    lec-06 всем две и предупреждает, когда вышло больше. Прав lec-07 по
    геометрии (словесная плашка цены ошибки в две строки не укладывается, а
    зажатая по пределу наезжает на соседку) и lec-06 по отчёту (значение в
    три строки — признак того, что в плашку положили фразу вместо числа).
    `DEFAULT` берёт и то и другое."""
    return (st.value_rows_digit if re.search(r"\d", value)
            else st.value_rows_word)


def _val_fit(value, iw, st):
    """Кегль значения и ЧИСЛО СТРОК, которое оно на деле займёт.

    Строки возвращаются НАСТОЯЩИЕ, а не обрезанные по пределу: значение,
    которому и на нижнем кегле нужно три строки, обязано получить высоту под
    три. Зажатое по пределу оно наезжало на оговорку снизу — настоящий
    `s38a` Лекции 6, «432 729 против 44 840» поверх своей же подписи.

    РАСХОЖДЕНИЕ: самое длинное слово lec-06 ищет по ЧИСЛУ ЗНАКОВ, lec-07 —
    по ШИРИНЕ. Прав lec-07: «ЖЖЖЖ» шире «iiiiiii» при меньшем числе знаков,
    и в кириллице этот промах даёт как раз тот разрыв посреди корня, от
    которого проверка и защищает."""
    # Подбор кегля меряется по СУЖЕННОЙ ширине (запас `W_SAFE`), а надпись
    # рисуется по полной: запас нужен решению «сколько строк», а не самой
    # надписи. Здесь два сборщика совпали — оба брали суженную.
    iwm = max(0.3, iw * metrics.W_SAFE)
    rows_max = _rows_max(value, st)
    f = st.value_hi
    while f > st.value_floor:
        if st.value_longest_by_width:
            fits_w = (metrics.longest_word_w(value, f, True) / 72.0
                      <= iwm)
        else:
            longest = max(value.split(), key=len, default="")
            fits_w = metrics.text_w(longest, f, True) <= iwm * 72.0
        if fits_w and metrics.n_lines(value, f, iwm, True) <= rows_max:
            break
        f -= 0.5
    hw = iwm if st.value_h_wsafe else max(0.3, iw)
    return f, metrics.n_lines(value, f, hw, True)


def plate_h(p, pw, st=DEFAULT):
    """Высота ОДНОЙ плашки по её собственному содержимому.

    Мерится то же, что рисуется, и это не формальность: подпись рисуется
    ПРОПИСНЫМИ и полужирной, значение — полужирным. Мера по строчным и
    светлым давала плашку ниже надписи, и надпись наезжала на оговорку."""
    iw = max(0.3, pw - 2 * st.pad)
    h = 2 * st.pad
    if p["label"]:
        lw = iw * metrics.W_SAFE if st.label_wsafe else iw
        h += metrics.est_h(p["label"].upper(), st.label_pt, lw,
                           st.label_ls, True) + st.label_extra
    if p["value"]:
        f, rows = _val_fit(p["value"], iw, st)
        h += (rows * f * st.value_ls * metrics.LH / 72.0 * metrics.SAFE
              + st.value_extra)
    if p["note"]:
        nw = iw * metrics.W_SAFE if st.note_wsafe else iw
        h += st.note_extra + metrics.est_h(
            p["note"], st.note_pt, nw, st.note_ls, False, st.note_italic)
    return h


def _plate_rows(plates, w, st):
    rows = [plates[i:i + st.max_per_row]
            for i in range(0, len(plates), st.max_per_row)]
    out = []
    for row in rows:
        pw = (w - st.gap * (len(row) - 1)) / len(row)
        out.append((row, pw, max(plate_h(p, pw, st) for p in row)))
    return out


def plates_h(plates, w, st=DEFAULT):
    """Высота всей полосы — она же то, что полоса отнимает у тела кадра."""
    rows = _plate_rows(plates, w, st)
    if not rows:
        return 0.0
    return sum(r[2] for r in rows) + st.gap * (len(rows) - 1)


def draw_plates(s, sid, plates, x, y, w, st=DEFAULT, tag=None):
    """Горизонтальная полоса плашек. Возвращает занятую высоту."""
    tag = tag or sid
    gold = gold_idx(plates, st)
    k, yy = 0, y
    for row, pw, rh in _plate_rows(plates, w, st):
        xx = x
        for p in row:
            _draw_plate(s, sid, p, xx, yy, pw, rh, k in gold, st,
                        f"{tag}/плашка{k + 1}")
            xx += pw + st.gap
            k += 1
        yy += rh + st.gap
    report.PRIM["полоса плашек"] += 1
    if st.total_from_rows:
        return plates_h(plates, w, st)
    return yy - y - st.gap


def _draw_plate(s, sid, p, x, y, w, h, is_gold, st, tag):
    prims.ocean_box(s, x, y, w, h,
                    fill=WHITE if is_gold else SURFACE,
                    stroke=GOLD if is_gold else LIGHT,
                    stroke_pt=st.gold_stroke_pt if is_gold else st.stroke_pt)
    if is_gold:
        report.GOLD_SEEN.add(sid)
    iw = max(0.3, w - 2 * st.pad)
    cy = y + st.pad
    if p["label"]:
        lw = iw * metrics.W_SAFE if st.label_wsafe else iw
        lab = p["label"].upper()
        rows = metrics.n_lines(lab, st.label_pt, lw, True)
        if st.warn_overflow and rows > 2:
            report.warn(
                f"[плашки] {tag}: подпись «{p['label']}» заняла {rows} "
                "строки — она задумана капителью в строку-две, длинное "
                "место ей в `note`")
        # РАСХОЖДЕНИЕ, видимое в геометрии: lec-07 кладёт отбивку (0,05")
        # ВНУТРЬ рамки подписи, lec-06 — только в сдвиг курсора, а рамку
        # даёт ровно по строкам. Сумма высот одна и та же, поэтому полоса
        # целиком у обоих одинаковой высоты, но рамка самой подписи
        # отличается на 0,05" — и это видно в XML доставленных дек.
        floor.pt(st.label_pt, tag, "подпись плашки")
        hl = metrics.est_h(lab, st.label_pt, lw, st.label_ls, True)
        box = hl + st.label_extra if st.label_extra_in_box else hl
        prims.text_box(s, x + st.pad, cy, iw, box, lab, size=st.label_pt,
                       bold=True, color=st.label_color, ls=st.label_ls,
                       tag=f"{tag}/подпись")
        cy += hl + st.label_extra
    if p["value"]:
        f, rows = _val_fit(p["value"], iw, st)
        if st.warn_overflow and rows > _rows_max(p["value"], st):
            report.warn(
                f"[плашки] {tag}: значению «{p['value']}» и на {f:.1f} пт "
                f"нужно {rows} строки — плашка держит крупное ЧИСЛО, а не "
                "фразу: длинное в `note` или на отдельную плашку")
        floor.pt(f, tag, "значение плашки")
        hv = (rows * f * st.value_ls * metrics.LH / 72.0 * metrics.SAFE
              + st.value_extra)
        prims.text_box(s, x + st.pad, cy, iw, hv, p["value"], size=f,
                       bold=True,
                       color=st.value_key_color if is_gold else DEEP,
                       ls=st.value_ls, tag=f"{tag}/значение")
        cy += hv
    if p["note"]:
        nw = iw * metrics.W_SAFE if st.note_wsafe else iw
        rows = metrics.n_lines(p["note"], st.note_pt, nw, False,
                               st.note_italic)
        if st.warn_overflow and rows > st.note_rows:
            report.warn(
                f"[плашки] {tag}: оговорка заняла {rows} строки "
                f"(> {st.note_rows}) — полоса плашек выросла на эту высоту "
                "за счёт тела слайда")
        floor.pt(st.note_pt, tag, "оговорка плашки")
        hn = metrics.est_h(p["note"], st.note_pt, nw, st.note_ls, False,
                           st.note_italic)
        prims.text_box(s, x + st.pad, cy + st.note_extra, iw, hn, p["note"],
                       size=st.note_pt, italic=st.note_italic,
                       color=st.note_color, ls=st.note_ls,
                       tag=f"{tag}/оговорка")
