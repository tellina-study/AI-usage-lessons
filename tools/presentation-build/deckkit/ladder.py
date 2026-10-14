# -*- coding: utf-8 -*-
"""ЛЕСТНИЦА `scheme: kind: lestnitsa` — ступени, а не шаги.

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ: нарастание или убывание. Ступени упорядочены по
ВЕЛИЧИНЕ («выше / ниже»), а не по времени («раньше / позже»), и последняя
ступень читается как дно либо как верх, а не как четвёртый пункт перечня.

ЗАЧЕМ ОНА ЗАВЕДЕНА. Несущая ось Лекции 7 — ступени участия человека: смотрит
первым · смотрит вторым · смотрит только спорное · подписывает не глядя.
Это убывание, и в нём весь смысл кадра: четвёртая ступень — то самое место,
где подпись есть, а решения за ней нет. Рядом коробок со стрелками она
выходит четвёртым шагом конвейера, то есть тем, к чему приходят, — ровно
обратным по смыслу. Ось возвращается ещё на нескольких кадрах пометкой
«Ступень», то есть форма нужна деке не один раз.

Контракт фронтматтера — тот же `rows`, что у остальных форм:

    scheme:
      kind: lestnitsa
      direction: вниз          # «вниз» (по умолчанию) либо «вверх»
      axis: "участие человека" # подпись оси, необязательна
      caption: "…"
      rows:
        - label: "Ступени"
          steps:
            - "Смотрит первым\\nвидит случай"
            - "Смотрит вторым\\nвидит случай и готовый вывод"
            - "Смотрит только спорное\\nвидит выборку, которую отобрал не он"
            - "Подписывает не глядя\\nвидит только текст"

ПОЧЕМУ СТУПЕНИ ИДУТ ОДНИМ РЯДОМ, А НЕ РЯДАМИ. Лестница — ОДНА шкала; два
ряда ступеней были бы двумя шкалами, и «ниже» между ними не определено.
Второй ряд поэтому называется `[лестница]`, а не рисуется молча.

ДНО ОТЛИЧАЕТСЯ ОТ ОСТАЛЬНЫХ СТУПЕНЕЙ ВИДОМ, а не только положением: у
крайней ступени (нижней при убывании, верхней при нарастании) обводка
золотая и заливка белая. Это не украшение: без него лестница из четырёх
одинаковых коробок, сдвинутых по диагонали, читается как «четыре штуки под
углом», и крайняя ступень — та, ради которой кадр существует, — ничем не
выделена.
"""
from dataclasses import dataclass

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, MID, SURFACE, WHITE

NEEDS_ROWS = True
DOWN = ("вниз", "down", "убывание")
UP = ("вверх", "up", "нарастание")


@dataclass(frozen=True)
class LadderStyle:
    step_hi: float = 13.5
    step_lo: float = 12.0          # пол видимого слоя, см. `floor.py`
    step_rows: int = 4
    step_pad: float = 0.10
    step_ls: float = 1.12
    gap: float = 0.12              # просвет между ступенями по ширине
    rise: float = 0.30             # на сколько ступень смещена по высоте
    box_min_h: float = 0.72
    box_extra: float = 0.24
    axis_pt: float = 12.0          # пол видимого слоя, см. `floor.py`
    axis_h: float = 0.26
    axis_gap: float = 0.10
    cap_pt: float = 12.0           # пол видимого слоя, см. `floor.py`
    cap_ls: float = 1.14
    cap_gap: float = 0.08
    max_steps: int = 5             # шестая ступень не читается
    min_step_w: float = 1.05
    max_h: float = 4.20            # выше лестница съедает кадр целиком


DEFAULT = LadderStyle()


def ladder_of(sid, raw, rows, st=DEFAULT):
    d = {"kind": "lestnitsa", "rows": rows,
         "steps": rows[0]["steps"] if rows else [],
         "caption": str(raw.get("caption") or "").strip(),
         # Подпись оси берётся ТОЛЬКО из `axis`. Подставлять сюда подпись
         # ряда нельзя: она называет, что это за перечень («Ступени»), а
         # ось обязана назвать, ЧТО убывает («участие человека»), — и
         # подстановка выдавала бы первое за второе.
         "axis": str(raw.get("axis") or "").strip(),
         "down": str(raw.get("direction") or "вниз").strip().lower() not in UP}
    if len(rows) > 1:
        report.warn(
            f"[лестница] {sid}: рядов {len(rows)} — лестница это ОДНА шкала, "
            "и «ниже» между двумя шкалами не определено. Второй ряд либо "
            "лишний, либо это две разные лестницы на двух кадрах")
    return d


def _step_w(d, w, st):
    n = len(d["steps"])
    return (w - (n - 1) * st.gap) / max(n, 1)


def _iw(d, w, st):
    return max(0.3, (_step_w(d, w, st) - 2 * st.step_pad) * metrics.W_SAFE)


def _rows_of_text(text, f, iw):
    return sum(metrics.n_lines(p, f, iw, True) for p in text.split("\n"))


def _longest(text, f):
    return max(text.split(), key=lambda x: metrics.text_w(x, f, True),
               default="")


def step_size(d, w, st=DEFAULT):
    iw = _iw(d, w, st)

    def fits(f):
        for s in d["steps"]:
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


def _box_h(d, w, f, st):
    iw = _iw(d, w, st)
    rows = max((min(st.step_rows, _rows_of_text(s["text"], f, iw))
                for s in d["steps"]), default=1)
    return max(st.box_min_h, rows * _line_h(f, st.step_ls) + st.box_extra)


def _cap_h(d, w, st):
    if not d["caption"]:
        return 0.0
    return st.cap_gap + metrics.n_lines(d["caption"], st.cap_pt, w) \
        * _line_h(st.cap_pt, st.cap_ls)


def ladder_h(d, w, st=DEFAULT):
    """Высота лестницы: коробка ступени плюс весь подъём плюс ось и подпись.

    Подъём входит в высоту ЦЕЛИКОМ, а не наполовину: лестница из пяти
    ступеней при подъёме 0,30" выше своей коробки на 1,20", и мера, которая
    этого не считает, отдала бы телу место, которого нет."""
    bh = _box_h(d, w, step_size(d, w, st), st)
    rise = st.rise * max(len(d["steps"]) - 1, 0)
    axis = (st.axis_gap + st.axis_h) if d["axis"] else 0.0
    return bh + rise + axis + _cap_h(d, w, st)


def check_ladder(sid, d, w, st=DEFAULT):
    """`[лестница]`: ступеней больше пяти · одна ступень · тесная ступень ·
    разорванное слово · лестница съела кадр."""
    n = len(d["steps"])
    if n > st.max_steps:
        report.warn(
            f"[лестница] {sid}: ступеней {n} (> {st.max_steps}) — лестница "
            "читается как лестница, пока ступени различимы; дальше это "
            "перечень под углом")
    if n < 2:
        report.warn(
            f"[лестница] {sid}: ступень одна — нарастания или убывания из "
            "неё не выходит")
    f = step_size(d, w, st)
    iw = _iw(d, w, st)
    for s in d["steps"]:
        long = _longest(s["text"], f)
        if long and metrics.text_w(long, f, True) > iw * 72.0:
            report.warn(
                f"[лестница] {sid}: слову «{long}» нужно "
                f"{metrics.text_w(long, f, True) / 72.0:.2f}\" при {f:.1f} "
                f"пт, а ступень вышла {iw:.2f}\" — слово будет разорвано "
                "переносом посреди корня")
    sw = _step_w(d, w, st)
    if sw < st.min_step_w:
        report.warn(
            f"[лестница] {sid}: ступень вышла {sw:.2f}\" "
            f"(< {st.min_step_w:.2f}\") — ступеней больше, чем держит эта "
            "ширина")
    h = ladder_h(d, w, st)
    if h > st.max_h:
        report.warn(
            f"[лестница] {sid}: лестница заняла {h:.2f}\" "
            f"(> {st.max_h:.2f}\") — подъём {st.rise:.2f}\" на ступень "
            "складывается, и телу кадра места не остаётся. Убавьте ступени "
            "либо текст в них")


def draw_ladder(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Лестница: ступени со смещением по высоте, крайняя — золотом.
    Возвращает занятую высоту."""
    tag = tag or sid
    f = step_size(d, w, st)
    floor.pt(f, tag, "ступень лестницы")
    bh = _box_h(d, w, f, st)
    n = len(d["steps"])
    sw = _step_w(d, w, st)
    rise = st.rise * max(n - 1, 0)
    top = y + ((st.axis_gap + st.axis_h) if d["axis"] else 0.0)
    if d["axis"]:
        floor.pt(st.axis_pt, tag, "подпись оси лестницы")
        arrow = "вниз" if d["down"] else "вверх"
        prims.text_box(s, x, y, w, st.axis_h,
                       f"{d['axis']} — {arrow} по ступеням", size=st.axis_pt,
                       italic=True, color=MID, ls=1.10, tag=f"{tag}/ось")
    for i, step in enumerate(d["steps"]):
        cx = x + i * (sw + st.gap)
        # Смещение: при убывании каждая следующая ступень НИЖЕ, при
        # нарастании — выше. Считается от верха блока, чтобы высота,
        # обещанная `ladder_h`, совпадала с занятой при обоих направлениях.
        cy = top + (i * st.rise if d["down"] else rise - i * st.rise)
        last = (i == n - 1) if d["down"] else (i == 0)
        prims.ocean_box(s, cx, cy, sw, bh,
                        fill=WHITE if last else SURFACE,
                        stroke=GOLD if last else LIGHT,
                        stroke_pt=2.0 if last else 1.3)
        if last:
            report.GOLD_SEEN.add(sid)
        # ПЕРВАЯ строка ступени — её имя, остальные — что на ней видно.
        # Набраны они по-разному нарочно: четыре ступени по две строки
        # одним начертанием читаются восемью равноправными строками, и
        # лестница снова превращается в перечень.
        head, _, rest = step["text"].partition("\n")
        runs = [{"text": head, "size": f, "bold": True, "color": DEEP}]
        if rest:
            runs.append({"text": rest, "size": f, "color": DEEP,
                         "newpara": True})
        prims.text_runs(s, cx + st.step_pad, cy + 0.05, sw - 2 * st.step_pad,
                        bh - 0.10, runs, align=PP_ALIGN.CENTER,
                        anchor=MSO_ANCHOR.MIDDLE, ls=st.step_ls,
                        tag=f"{tag}/ступень{i + 1}")
    cy = top + rise + bh
    ch = _cap_h(d, w, st)
    if ch:
        floor.pt(st.cap_pt, tag, "подпись схемы")
        prims.text_box(s, x, cy + st.cap_gap, w, ch - st.cap_gap,
                       d["caption"], size=st.cap_pt, italic=True, color=LIGHT,
                       ls=st.cap_ls, tag=f"{tag}/подпись")
        cy += ch
    report.PRIM["лестница"] += 1
    return cy - y


def parse(sid, raw, rows):
    return ladder_of(sid, raw, rows)


def height(d, w):
    return ladder_h(d, w)


def check(sid, d, w):
    return check_ladder(sid, d, w)


def draw(s, sid, d, x, y, w, tag=None):
    return draw_ladder(s, sid, d, x, y, w, tag=tag)
