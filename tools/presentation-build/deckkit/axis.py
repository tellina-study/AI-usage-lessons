# -*- coding: utf-8 -*-
"""ОСЬ С ЗАСЕЧКАМИ `scheme: kind: shkala` — разница ВИДНА, а не прочитана.

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ: сравнение величин одной единицы. Положение засечки
несёт смысл — то, чего не несёт ни полоса плашек, ни ряд коробок: три числа
в трёх плашках стоят на равном расстоянии друг от друга независимо от того,
отличаются они на два пункта или на двадцать.

ЗАЧЕМ ОНА ЗАВЕДЕНА, адресно. У Лекции 7 два кадра, вывод которых — в самом
рисунке, и этот вывод сегодня приходится читать словами:

* `s45`: модель одна 92 · врач один 74 · врач поверх модели 76 из ста —
  пара чуть выше одинокого врача, и разница в два пункта незначима;
* `s49c`: модель одна 0,816 · хирург один 0,820 · хирург с подсказкой
  0,712 — пара заметно НИЖЕ обеих сторон.

Две одинаковые оси рядом показывают вывод раздела без единого слова: пара
то чуть выше, то ниже обеих сторон. Полосой плашек этого не показать —
плашки дают обоим кадрам один и тот же рисунок.

ДВЕ РАЗНОВИДНОСТИ, И ВТОРАЯ НЕ НАСТРОЙКА ПЕРВОЙ:

* ОБЩАЯ ШКАЛА (по умолчанию) — величины одной единицы на одной прямой,
  предел шкалы берётся с запасом от крайних значений либо задаётся `from` /
  `to`. Это `s45`, `s49c`;
* НОЛЬ ПО ЦЕНТРУ (`zero: true`) — размеры эффекта, у которых знак и есть
  содержание: `s49a`, −0,54 против +0,46, и смысл в том, что ни один
  доверительный интервал нуля НЕ ПЕРЕСЕКАЕТ. Поэтому засечка умеет нести
  интервал (`lo` / `hi`), а ноль рисуется отдельной чертой.

ЧЕГО ЭТА ФОРМА НЕ ДЕЛАЕТ — И ЭТО ЕЁ ГЛАВНОЕ СВОЙСТВО. Она НЕ сводит на одну
ось величины с РАЗНЫМИ базами. `s47`/`s48` оставлены плашками именно
поэтому: 80 033 женщины промежуточного анализа и 105 934 итогового — это
два знаменателя, и ось между ними нарисовала бы сравнение, которого нет.
Разные `base` у засечек — отказ (`[ось]`), а не рисунок: форма, которая
молча кладёт несравнимое на одну прямую, опаснее отсутствия формы.

Контракт фронтматтера:

    scheme:
      kind: shkala
      unit: "из ста"            # одна единица на всю ось — обязательна
      base: "150 случаев"       # общий знаменатель, необязателен
      caption: "…"
      zero: false
      marks:
        - {value: 0.816, label: "Модель одна"}
        - {value: 0.820, label: "Хирург один"}
        - {value: 0.712, label: "Хирург с подсказкой", key: true,
           lo: 0.65, hi: 0.78}
"""
import re
from dataclasses import dataclass

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, MID, SLATE, SURFACE, TEAL, WHITE

NEEDS_ROWS = False          # ось читает `marks`, а не `rows`


@dataclass(frozen=True)
class AxisStyle:
    line_h: float = 0.055       # толщина самой прямой
    line_pad: float = 0.55      # поле слева и справа под крайние подписи
    tick_w: float = 0.055
    tick_h: float = 0.30
    lane_h: float = 0.62        # высота дорожки подписи над/под прямой
    lane_gap: float = 0.10
    val_pt: float = 15.0
    val_ls: float = 1.08
    lab_pt: float = 12.0        # пол видимого слоя, см. `floor.py`
    lab_ls: float = 1.10
    unit_pt: float = 12.0       # пол видимого слоя, см. `floor.py`
    unit_h: float = 0.24
    ci_h: float = 0.075         # толщина полосы интервала
    cap_pt: float = 12.0        # пол видимого слоя, см. `floor.py`
    cap_ls: float = 1.14
    cap_gap: float = 0.08
    max_marks: int = 5
    min_lab_w: float = 1.05     # уже этого подпись засечки не читается
    pad_frac: float = 0.12      # запас шкалы за крайними значениями


DEFAULT = AxisStyle()
_NUM = re.compile(r"^[−\-+]?[\d  ]+(?:[.,]\d+)?$")


def _num(raw):
    """Число из значения засечки. Принимает и число, и строку — «0,712» с
    запятой и «1 000» с пробелом-разделителем: во фронтматтере деки числа
    пишутся так же, как на экране, и заставлять автора писать их дважды
    значило бы развести подпись и величину."""
    if isinstance(raw, (int, float)):
        return float(raw)
    s = str(raw or "").strip().replace("−", "-").replace(" ", "") \
                              .replace(" ", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def axis_of(sid, raw, rows=None, st=DEFAULT):
    """Поле `scheme` формы `shkala` → ось или None."""
    mm = raw.get("marks")
    if not isinstance(mm, list) or not mm:
        report.warn(f"[ось] {sid}: у формы `shkala` нет `marks` — ось это "
                    "величины с подписями, а не ряды шагов")
        return None
    marks, bases = [], set()
    for i, m in enumerate(mm, 1):
        if not isinstance(m, dict):
            report.warn(f"[ось] {sid}: засечка {i} не value/label")
            continue
        v = _num(m.get("value"))
        if v is None:
            report.warn(
                f"[ось] {sid}: у засечки «{m.get('label') or i}» значение "
                f"«{m.get('value')}» не число — на ось его положить не во "
                "что. Словесная величина живёт плашкой, не осью")
            continue
        marks.append({
            "v": v,
            "shown": str(m.get("value")).strip(),
            "label": str(m.get("label") or "").strip(),
            "key": bool(m.get("key")),
            "lo": _num(m.get("lo")), "hi": _num(m.get("hi")),
            "base": str(m.get("base") or "").strip()})
        bases.add(marks[-1]["base"])
    if not marks:
        return None
    d = {"kind": "shkala", "marks": marks,
         "unit": str(raw.get("unit") or "").strip(),
         "base": str(raw.get("base") or "").strip(),
         "caption": str(raw.get("caption") or "").strip(),
         "zero": bool(raw.get("zero")),
         "from": _num(raw.get("from")), "to": _num(raw.get("to"))}
    d["bases"] = {b for b in bases if b}
    return d


def span(d, st=DEFAULT):
    """Предел шкалы: (нижний, верхний). Берётся по крайним значениям с
    запасом, а при `zero: true` — симметрично нулю, иначе ноль уехал бы к
    краю и перестал быть точкой отсчёта."""
    vals = [m["v"] for m in d["marks"]]
    vals += [m["lo"] for m in d["marks"] if m["lo"] is not None]
    vals += [m["hi"] for m in d["marks"] if m["hi"] is not None]
    lo, hi = min(vals), max(vals)
    if d["zero"]:
        r = max(abs(lo), abs(hi)) or 1.0
        lo, hi = -r, r
    pad = (hi - lo) * st.pad_frac or (abs(hi) * st.pad_frac or 1.0)
    lo, hi = lo - pad, hi + pad
    if d["from"] is not None:
        lo = d["from"]
    if d["to"] is not None:
        hi = d["to"]
    if hi - lo <= 0:
        hi = lo + 1.0
    return lo, hi


def _x_of(v, d, x, w, st):
    lo, hi = span(d, st)
    inner = w - 2 * st.line_pad
    return x + st.line_pad + inner * (v - lo) / (hi - lo)


def _lanes(d):
    """Дорожки подписей: чётные засечки над прямой, нечётные под ней.

    Это не украшение, а то, что держит подписи от наезда друг на друга:
    0,816 и 0,820 на одной прямой стоят ближе, чем их подписи. Две дорожки
    удваивают доступную ширину подписи; где и этого мало — говорит
    `check_axis`."""
    order = sorted(range(len(d["marks"])), key=lambda i: d["marks"][i]["v"])
    return {m: (k % 2 == 0) for k, m in enumerate(order)}


def block_h(st=DEFAULT):
    """Высота САМОЙ оси: дорожка подписи · просвет · засечка · прямая ·
    засечка · просвет · дорожка подписи.

    Засечка входит в высоту ДВАЖДЫ, и это не придирка: пока её здесь не
    было, верхняя дорожка подписей начиналась выше отведённого оси блока
    ровно на высоту засечки — то есть лезла в заголовок кадра, а мера об
    этом молчала. Мерить надо то, что рисуется, и обеими сторонами."""
    return 2 * (st.lane_h + st.lane_gap + st.tick_h) + st.line_h


def line_y_of(y, st=DEFAULT):
    """Верх самой прямой при блоке, начатом в `y`. Одно место на меру и на
    рисование: две формулы одного числа расходятся на первой же правке."""
    return y + st.lane_h + st.lane_gap + st.tick_h


def axis_h(d, w, st=DEFAULT):
    """Высота оси — она же то, что ось отнимает у тела кадра."""
    h = block_h(st)
    if d["unit"] or d["base"]:
        h += st.unit_h
    if d["caption"]:
        h += st.cap_gap + metrics.n_lines(d["caption"], st.cap_pt, w) \
            * st.cap_pt * st.cap_ls * metrics.LH / 72.0 * metrics.SAFE
    return h


def check_axis(sid, d, w, st=DEFAULT):
    """`[ось]`: разные базы · единица не названа · засечек больше пяти ·
    подписи сошлись · интервал задан наполовину."""
    if len(d["bases"]) > 1:
        report.warn(
            f"[ось] {sid}: у засечек РАЗНЫЕ базы ({' · '.join(sorted(d['bases']))}) "
            "— на одну прямую их класть нельзя: это сравнение, которого нет. "
            "Величины с разными знаменателями живут плашками, каждая со "
            "своей базой")
    if not d["unit"]:
        report.warn(
            f"[ось] {sid}: у оси не названа ЕДИНИЦА (`unit`) — без неё "
            "засечки сравнимы только на вид: «92» и «0,92» встают на ось "
            "одинаково хорошо и значат разное")
    n = len(d["marks"])
    if n < 2:
        report.warn(f"[ось] {sid}: засечка одна — сравнивать не с чем. Одна "
                    "величина во весь кадр — это `figure:`")
    if n > st.max_marks:
        report.warn(
            f"[ось] {sid}: засечек {n} (> {st.max_marks}) — подписи встают "
            "друг на друга, и ось перестаёт читаться. Это график, а не "
            "засечки на прямой")
    for m in d["marks"]:
        if (m["lo"] is None) != (m["hi"] is None):
            report.warn(
                f"[ось] {sid}: у засечки «{m['label'] or m['shown']}» задан "
                "только один край интервала — полуинтервал рисует точность, "
                "которой нет")
        if m["lo"] is not None and m["hi"] is not None and m["lo"] > m["hi"]:
            report.warn(
                f"[ось] {sid}: у засечки «{m['label'] or m['shown']}» нижний "
                f"край интервала ({m['lo']}) выше верхнего ({m['hi']})")
    # Подписи сошлись: на каждой дорожке соседние засечки обязаны стоять
    # дальше, чем половина суммы их подписей. Мера идёт по НАСТОЯЩЕЙ ширине
    # текста, а не по числу знаков.
    lanes = _lanes(d)
    for up in (True, False):
        idx = sorted([i for i in range(len(d["marks"])) if lanes[i] == up],
                     key=lambda i: d["marks"][i]["v"])
        for a, b in zip(idx, idx[1:]):
            ma, mb = d["marks"][a], d["marks"][b]
            xa = _x_of(ma["v"], d, 0.0, w, st)
            xb = _x_of(mb["v"], d, 0.0, w, st)
            wa = metrics.longest_word_w(ma["label"] or ma["shown"],
                                        st.lab_pt) / 72.0
            wb = metrics.longest_word_w(mb["label"] or mb["shown"],
                                        st.lab_pt) / 72.0
            if xb - xa < (wa + wb) / 2:
                report.warn(
                    f"[ось] {sid}: засечки «{ma['label'] or ma['shown']}» и "
                    f"«{mb['label'] or mb['shown']}» стоят в "
                    f"{xb - xa:.2f}\" друг от друга, а их подписям нужно "
                    f"{(wa + wb) / 2:.2f}\" — на экране они сойдутся. "
                    "Задайте `from`/`to` поуже, сократите подписи либо "
                    "сведите две близкие величины в одну засечку")


def draw_axis(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Ось: прямая, засечки по величине, подписи двумя дорожками.
    Возвращает занятую высоту."""
    tag = tag or sid
    lanes = _lanes(d)
    top = y
    line_y = line_y_of(top, st)
    prims.rect(s, x + st.line_pad / 2, line_y,
               w - st.line_pad, st.line_h, LIGHT, count="ось")
    if d["zero"]:
        zx = _x_of(0.0, d, x, w, st)
        prims.rect(s, zx - st.tick_w / 2, line_y - st.tick_h - 0.10,
                   st.tick_w, st.tick_h * 2 + st.line_h + 0.20, SLATE,
                   count="ноль")
        floor.pt(st.unit_pt, tag, "подпись нуля оси")
        prims.text_box(s, zx - 0.35, line_y + st.tick_h + 0.12, 0.70, 0.22,
                       "ноль", size=st.unit_pt, italic=True, color=SLATE,
                       align=PP_ALIGN.CENTER, ls=1.0, tag=f"{tag}/ноль",
                       quiet=True)
    for i, m in enumerate(d["marks"]):
        mx = _x_of(m["v"], d, x, w, st)
        up = lanes[i]
        col = GOLD if m["key"] else MID
        if m["lo"] is not None and m["hi"] is not None:
            lx, hx = _x_of(m["lo"], d, x, w, st), _x_of(m["hi"], d, x, w, st)
            prims.rect(s, lx, line_y + (st.line_h - st.ci_h) / 2, hx - lx,
                       st.ci_h, TEAL, count="интервал")
        prims.rect(s, mx - st.tick_w / 2,
                   line_y - st.tick_h if up else line_y + st.line_h,
                   st.tick_w, st.tick_h, col, count="засечка")
        if m["key"]:
            report.GOLD_SEEN.add(sid)
        lane_y = (line_y - st.tick_h - st.lane_gap - st.lane_h) if up \
            else (line_y + st.line_h + st.tick_h + st.lane_gap)
        text = m["shown"] + ("\n" + m["label"] if m["label"] else "")
        lw = max(st.min_lab_w, w / max(len(d["marks"]), 1))
        floor.pt(st.lab_pt, tag, "подпись засечки")
        floor.pt(st.val_pt, tag, "величина засечки")
        prims.text_box(s, mx - lw / 2, lane_y, lw, st.lane_h, text,
                       size=st.lab_pt, bold=False, color=DEEP,
                       align=PP_ALIGN.CENTER,
                       anchor=MSO_ANCHOR.BOTTOM if up else MSO_ANCHOR.TOP,
                       ls=st.lab_ls, tag=f"{tag}/засечка{i + 1}", quiet=True)
    cy = top + block_h(st)
    if d["unit"] or d["base"]:
        floor.pt(st.unit_pt, tag, "единица оси")
        txt = " · ".join(t for t in (d["unit"], d["base"]) if t)
        prims.text_box(s, x, cy, w, st.unit_h, txt, size=st.unit_pt,
                       bold=True, color=MID, align=PP_ALIGN.CENTER,
                       ls=1.0, tag=f"{tag}/единица", quiet=True)
        cy += st.unit_h
    if d["caption"]:
        floor.pt(st.cap_pt, tag, "подпись схемы")
        ch = metrics.est_h(d["caption"], st.cap_pt, w, st.cap_ls, False, True)
        prims.text_box(s, x, cy + st.cap_gap, w, ch, d["caption"],
                       size=st.cap_pt, italic=True, color=LIGHT,
                       ls=st.cap_ls, tag=f"{tag}/подпись")
        cy += st.cap_gap + ch
    report.PRIM["ось"] += 1
    return cy - y


def parse(sid, raw, rows=None):
    return axis_of(sid, raw, rows)


def height(d, w):
    return axis_h(d, w)


def check(sid, d, w):
    return check_axis(sid, d, w)


def draw(s, sid, d, x, y, w, tag=None):
    return draw_axis(s, sid, d, x, y, w, tag=tag)
