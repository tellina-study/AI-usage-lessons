# -*- coding: utf-8 -*-
"""ПАРАЛЛЕЛЬНЫЕ ДОРОЖКИ `scheme: kind: dorozhki` — независимые линии.

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ: независимость. Линии идут одновременно, одна не
следует из другой, и порядок между ними не назван. Ровно это и отличает её
от схемы-конвейера, которая утверждает порядок.

ЗАЧЕМ ОНА ЗАВЕДЕНА, числом. Прогон всех 20 схем деки Лекции 7 (круг #229):
`arrows` истинен по умолчанию, явно он задан на пяти кадрах, то есть
пятнадцать схем несут стрелку, которой автор не объявлял, — и содержанию
она противоречит минимум на четырёх. `s11a` «откуда берутся данные о
человеке» — это четыре ИСТОЧНИКА, а не порядок: регистр населения не
предшествует жалобе. `s71` «три механизма надзора» — механизмы действуют
одновременно. `s62` «две дорожки врача» — пути параллельны, стрелка склеила
бы их в один. `s70` «четыре участника» — лента утверждает передачу по цепи,
которой нет: разработчик не передаёт врачу, они отвечают каждый за своё.

`arrows: false` снимает стрелку, но НЕ ГОВОРИТ, что линии независимы, —
получается ряд коробок без стрелок, а это «перечень, порядок которого не
назван», не «линии, идущие одновременно». Разница видна на `s62`: две
дорожки врача без стрелок читаются как один список из шести шагов.

Контракт фронтматтера:

    scheme:
      kind: dorozhki
      caption: "подпись под схемой, необязательна"
      entry: "общий вход"      # необязателен: веер слева
      exit:  "общий выход"     # необязателен: веер справа
      steps_arrows: true       # ЯВНО: порядок ВНУТРИ дорожки, не между
      rows:
        - {label: "Было",  steps: ["набор текста", "подпись"]}
        - {label: "Стало", steps: ["разговор", "черновик", "вычитка"]}

НИЧЕГО УТВЕРЖДАЮЩЕГО ПО УМОЛЧАНИЮ. Стрелка внутри дорожки — утверждение
«сначала одно, потом другое», и она включается только ключом
`steps_arrows: true`. `arrows: true` на дорожках — противоречие форме, и
оно называется, а не исполняется: это ключ схемы-конвейера, и дорожкам он
не принадлежит.

ШИРИНА ДОРОЖКИ ОДНА НА ВСЕ ДОРОЖКИ, и это не косметика. В схеме-конвейере
ширина бокса считается по числу шагов РЯДА, поэтому ряд из двух шагов
получает боксы вдвое шире ряда из четырёх — и «было» против «стало» выходит
сравнением двух разных масштабов (настоящий `s62`: 2 · 4 · 1). Здесь шаги
стоят на общей сетке самой длинной дорожки, и короткая дорожка просто
короче.
"""
from dataclasses import dataclass

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, MID, SURFACE, TEAL, WHITE


@dataclass(frozen=True)
class TracksStyle:
    lab_w: float = 1.55
    lab_pt: float = 12.0           # пол видимого слоя, см. `floor.py`
    lab_gap: float = 0.10
    # Поле рельса РАЗНОЕ по осям, и это не придирка. По горизонтали оно
    # даёт рельсу вид линии, на которой стоят клетки, — ради него рельс и
    # нужен. По вертикали оно только растит кадр: 0,09" сверху и снизу на
    # каждой дорожке — это 0,54" на трёх, и ровно на столько `s62` не
    # поместился («места под тело не осталось, −0,30"»). Замерено на живом
    # кадре, а не выведено.
    rail_pad: float = 0.10         # поле рельса слева и справа
    rail_vpad: float = 0.03        # и сверху-снизу
    step_hi: float = 13.5
    step_lo: float = 12.0          # пол видимого слоя, см. `floor.py`
    step_rows: int = 4
    step_pad: float = 0.09
    step_ls: float = 1.10
    step_gap: float = 0.10         # просвет между шагами внутри дорожки
    arrow_w: float = 0.20
    arrow_h: float = 0.15
    box_min_h: float = 0.50
    # Запас внутри клетки и просвет между дорожками — те же числа, что у
    # схемы-конвейера этой деки (0,26 и 0,16), уменьшены на 0,06 и 0,04:
    # ОБЩАЯ СЕТКА, ради которой форма и заведена, сама по себе дороже
    # рядов (узкая клетка переносит текст на вторую строку там, где
    # широкая держала в одну), и эту цену надо было чем-то вернуть.
    # Замерено на `s62`: с прежними числами телу кадра не оставалось места.
    box_extra: float = 0.16
    track_gap: float = 0.12
    fan_w: float = 1.45            # ширина коробки общего входа/выхода
    fan_gap: float = 0.22
    tie_w: float = 0.14            # усик веера к дорожке
    tie_h: float = 0.035
    cap_pt: float = 12.0           # пол видимого слоя, см. `floor.py`
    cap_ls: float = 1.14
    cap_gap: float = 0.08
    max_tracks: int = 4
    max_steps: int = 4
    min_step_w: float = 0.95


DEFAULT = TracksStyle()


def tracks_of(sid, raw, rows, st=DEFAULT):
    """Разобранная схема → дорожки. `rows` уже разобраны общим читателем
    `scheme.scheme_of`: дорожки отличаются от конвейера не разбором, а
    смыслом, и второй читатель того же поля разошёлся бы с первым."""
    d = {"kind": "dorozhki", "rows": rows,
         "caption": str(raw.get("caption") or "").strip(),
         "entry": str(raw.get("entry") or "").strip(),
         "exit": str(raw.get("exit") or "").strip(),
         "steps_arrows": raw.get("steps_arrows", False) is True,
         "lab_w": st.lab_w if any(r["label"] for r in rows) else 0.0}
    if raw.get("arrows") is True:
        report.warn(
            f"[дорожки] {sid}: на дорожках объявлен `arrows: true` — это "
            "ключ схемы-конвейера, и он утверждает порядок МЕЖДУ линиями, "
            "которого у параллельных дорожек нет. Порядок ВНУТРИ дорожки "
            "включается ключом `steps_arrows: true`")
    return d


def _fan_w(d, st):
    w = 0.0
    if d["entry"]:
        w += st.fan_w + st.fan_gap
    if d["exit"]:
        w += st.fan_w + st.fan_gap
    return w


def _rail_x(d, x, st):
    return x + d["lab_w"] + (st.lab_gap if d["lab_w"] else 0.0) \
        + ((st.fan_w + st.fan_gap) if d["entry"] else 0.0)


def _rail_w(d, w, st):
    return w - d["lab_w"] - (st.lab_gap if d["lab_w"] else 0.0) - _fan_w(d, st)


def _cells(d):
    """Сколько клеток в сетке — по САМОЙ длинной дорожке. Общая сетка и
    есть то, что делает дорожки сравнимыми."""
    return max(len(r["steps"]) for r in d["rows"])


def _step_w(d, w, st):
    n = _cells(d)
    inner = _rail_w(d, w, st) - 2 * st.rail_pad
    gap = st.step_gap + (st.arrow_w + st.step_gap if d["steps_arrows"] else 0)
    return (inner - (n - 1) * gap) / max(n, 1)


def _iw(d, w, st):
    return max(0.3, (_step_w(d, w, st) - 2 * st.step_pad) * metrics.W_SAFE)


def _rows_of_text(text, f, iw):
    return sum(metrics.n_lines(p, f, iw, True) for p in text.split("\n"))


def _longest(text, f):
    return max(text.split(), key=lambda x: metrics.text_w(x, f, True),
               default="")


def step_size(d, w, st=DEFAULT):
    """Один кегль на все шаги всех дорожек — наибольший, при котором каждый
    шаг укладывается в свою клетку и ни одно слово не шире клетки."""
    iw = _iw(d, w, st)

    def fits(f):
        for r in d["rows"]:
            for s in r["steps"]:
                if _rows_of_text(s["text"], f, iw) > st.step_rows:
                    return False
                if metrics.text_w(_longest(s["text"], f), f, True) > iw * 72.0:
                    return False
        return True

    f = st.step_hi
    while f > st.step_lo:
        if fits(f):
            break
        f -= 0.5
    return f


def _line_h(size, ls):
    return size * ls * metrics.LH / 72.0 * metrics.SAFE


def _box_h(d, w, f, st, row=None):
    """Высота клеток ОДНОЙ дорожки (или наибольшая по всем, если дорожка
    не названа).

    Считается по дорожке, а не по всей схеме, и это не экономия ради
    экономии. Общая сетка — утверждение о ШИРИНЕ: клетки сравнимы по
    горизонтали, потому что стоят на одном шаге. К высоте оно не
    относится: дорожка из одной длинной клетки не делает соседнюю,
    однострочную, двухстрочной. Замерено на `s62`: единственная клетка в
    две строки («выборочный контроль заметок») поднимала все три дорожки
    и отнимала у тела 0,32" — ровно столько, чтобы кадр перестал
    собираться."""
    iw = _iw(d, w, st)
    rows = [r for r in (d["rows"] if row is None else [row])]
    n = max(min(st.step_rows, _rows_of_text(s["text"], f, iw))
            for r in rows for s in r["steps"])
    return max(st.box_min_h, n * _line_h(f, st.step_ls) + st.box_extra)


def _rail_h(d, w, f, st, row):
    return _box_h(d, w, f, st, row) + 2 * st.rail_vpad


def _cap_h(d, w, st):
    if not d["caption"]:
        return 0.0
    return st.cap_gap + metrics.n_lines(d["caption"], st.cap_pt, w) \
        * _line_h(st.cap_pt, st.cap_ls)


def tracks_h(d, w, st=DEFAULT):
    """Высота схемы — она же то, что схема отнимает у тела кадра."""
    f = step_size(d, w, st)
    n = len(d["rows"])
    return (sum(_rail_h(d, w, f, st, r) for r in d["rows"])
            + st.track_gap * (n - 1) + _cap_h(d, w, st))


def check_tracks(sid, d, w, st=DEFAULT):
    """`[дорожки]`: одна дорожка · больше четырёх · длинная дорожка ·
    разорванное слово · тесная клетка."""
    n = len(d["rows"])
    if n < 2:
        report.warn(
            f"[дорожки] {sid}: дорожка одна — параллельных дорожек из неё не "
            "выходит. Одна линия шагов — это схема-конвейер (`kind` убрать) "
            "или перечень (`arrows: false`)")
    if n > st.max_tracks:
        report.warn(
            f"[дорожки] {sid}: дорожек {n} (> {st.max_tracks}) — столько "
            "линий одновременно не удерживаются взглядом; это таблица, а не "
            "схема")
    for i, r in enumerate(d["rows"], 1):
        if len(r["steps"]) > st.max_steps:
            report.warn(
                f"[дорожки] {sid}: в дорожке «{r['label'] or i}» "
                f"{len(r['steps'])} шагов (> {st.max_steps}) — длинный "
                "конвейер владельцем запрещён: «не надо вот этот длинный "
                "пайплайн»")
    f = step_size(d, w, st)
    iw = _iw(d, w, st)
    for r in d["rows"]:
        for s in r["steps"]:
            long = _longest(s["text"], f)
            if long and metrics.text_w(long, f, True) > iw * 72.0:
                report.warn(
                    f"[дорожки] {sid}: слову «{long}» нужно "
                    f"{metrics.text_w(long, f, True) / 72.0:.2f}\" при "
                    f"{f:.1f} пт, а клетка вышла {iw:.2f}\" — слово будет "
                    "разорвано переносом посреди корня")
    sw = _step_w(d, w, st)
    if sw < st.min_step_w:
        report.warn(
            f"[дорожки] {sid}: клетка дорожки вышла {sw:.2f}\" "
            f"(< {st.min_step_w:.2f}\") — шагов в самой длинной дорожке или "
            "вееров по краям слишком много для этой ширины")


def _fan_box(s, sid, text, x, y, w, h, st, tag):
    prims.ocean_box(s, x, y, w, h, fill=WHITE, stroke=TEAL, stroke_pt=1.5)
    floor.pt(st.lab_pt, tag, "веер дорожек")
    prims.text_box(s, x + 0.08, y + 0.05, w - 0.16, h - 0.10, text,
                   size=st.lab_pt, bold=True, color=TEAL,
                   align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                   ls=1.10, tag=tag)


def draw_tracks(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Параллельные дорожки: рельсы друг под другом, общий вход и выход
    веером. Возвращает занятую высоту."""
    tag = tag or sid
    f = step_size(d, w, st)
    floor.pt(f, tag, "шаг дорожки")
    if d["lab_w"]:
        floor.pt(st.lab_pt, tag, "подпись дорожки")
    n = len(d["rows"])
    hs = [_rail_h(d, w, f, st, r) for r in d["rows"]]
    tops = [y + sum(hs[:i]) + st.track_gap * i for i in range(n)]
    total = sum(hs) + st.track_gap * (n - 1)
    rx, rw = _rail_x(d, x, st), _rail_w(d, w, st)
    sw = _step_w(d, w, st)
    rails = any(len(r["steps"]) > 1 for r in d["rows"])
    for i, r in enumerate(d["rows"], 1):
        cy, rail_h = tops[i - 1], hs[i - 1]
        bh = rail_h - 2 * st.rail_vpad
        if r["label"]:
            prims.text_box(s, x, cy + 0.04, d["lab_w"] - 0.12, rail_h - 0.08,
                           r["label"], size=st.lab_pt, bold=True, color=MID,
                           anchor=MSO_ANCHOR.MIDDLE, ls=1.10,
                           tag=f"{tag}/дорожка{i}")
        # Рельс говорит «это одна линия, идущая сама по себе», и нужен
        # он ровно там, где ГРУППИРУЕТ: при одной клетке на дорожку рельс
        # обводит её второй раз тем же контуром — две рамки вокруг одного
        # слова, и форма начинает выглядеть сложнее, чем есть. Решается по
        # всей схеме, а не по дорожке: рельс через раз был бы третьим
        # сообщением, которого никто не посылал.
        if rails:
            prims.ocean_box(s, rx, cy, rw, rail_h, fill=SURFACE,
                            stroke=LIGHT, stroke_pt=1.2)
        cx = rx + st.rail_pad
        for j, step in enumerate(r["steps"], 1):
            if j > 1:
                if d["steps_arrows"]:
                    prims.arrow(s, cx + st.step_gap / 2,
                                cy + rail_h / 2 - st.arrow_h / 2,
                                st.arrow_w, st.arrow_h, LIGHT)
                    cx += st.arrow_w + st.step_gap
                cx += st.step_gap
            # Клетка белая ВСЕГДА: рельс под ней уже на поверхности
            # мотива, и клетка той же заливки слилась бы с ним. Шаг модели
            # различается обводкой, как и в схеме-конвейере.
            prims.ocean_box(s, cx, cy + st.rail_vpad, sw, bh, fill=WHITE,
                            stroke=GOLD if step["ai"] else LIGHT,
                            stroke_pt=2.0 if step["ai"] else 1.3)
            if step["ai"]:
                report.GOLD_SEEN.add(sid)
            prims.text_box(s, cx + st.step_pad, cy + st.rail_vpad + 0.05,
                           sw - 2 * st.step_pad, bh - 0.10, step["text"],
                           size=f, bold=step["ai"], color=DEEP,
                           align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                           ls=st.step_ls, tag=f"{tag}/шаг{i}.{j}")
            cx += sw
    # Веер: коробка во всю высоту дорожек и усик к каждой. Усик — не
    # стрелка: он говорит «эти линии сходятся здесь», а не «потом».
    if d["entry"]:
        ex = x + d["lab_w"] + (st.lab_gap if d["lab_w"] else 0.0)
        _fan_box(s, sid, d["entry"], ex, y, st.fan_w, total, st,
                 f"{tag}/вход")
        for i in range(n):
            mid = tops[i] + hs[i] / 2
            prims.rect(s, ex + st.fan_w, mid - st.tie_h / 2,
                       st.fan_gap, st.tie_h, LIGHT, count="связка")
    if d["exit"]:
        xx = rx + rw + st.fan_gap
        _fan_box(s, sid, d["exit"], xx, y, st.fan_w, total, st,
                 f"{tag}/выход")
        for i in range(n):
            mid = tops[i] + hs[i] / 2
            prims.rect(s, rx + rw, mid - st.tie_h / 2, st.fan_gap, st.tie_h,
                       LIGHT, count="связка")
    cy = y + total
    ch = _cap_h(d, w, st)
    if ch:
        floor.pt(st.cap_pt, tag, "подпись схемы")
        prims.text_box(s, x, cy + st.cap_gap, w, ch - st.cap_gap,
                       d["caption"], size=st.cap_pt, italic=True, color=LIGHT,
                       ls=st.cap_ls, tag=f"{tag}/подпись")
        cy += ch
    report.PRIM["дорожки"] += 1
    return cy - y


# ── общий договор форм (см. развилку `kind` в `scheme.py`) ───────────
# Четыре имени, одинаковые у всех форм: разбор · высота · проверка ·
# рисование. Развилка зовёт только их, поэтому форма может завести себе
# любые собственные имена и числа, не трогая ни одну деку.
NEEDS_ROWS = True       # форме нужны разобранные `rows` общего читателя


def parse(sid, raw, rows):
    return tracks_of(sid, raw, rows)


def height(d, w):
    return tracks_h(d, w)


def check(sid, d, w):
    return check_tracks(sid, d, w)


def draw(s, sid, d, x, y, w, tag=None):
    return draw_tracks(s, sid, d, x, y, w, tag=tag)
