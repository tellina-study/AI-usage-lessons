# -*- coding: utf-8 -*-
"""КОНВЕЙЕР СО СКОБКАМИ ФАЗ `fazy:` — длинный конвейер, сгруппированный в
фазы, с подсветкой «где вошла модель».

Перенос приёма §2.7 из `library/lectures/lec-08/rework-v5/PERENOS-PRIYOMOV.md`.
В образце (`media/s03`, `media/s10`) восемь-девять стадий лежат рядом, часть
подсвечена золотом (туда вошла модель), а ряд сгруппирован скобками в фазы —
«Поиск облика» / «Подготовка» / «Использование» — с фигурной скобкой снизу и
выводом, к чему это ведёт: «Людям остаются самые дорогие инженерные стадии».

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ: не порядок внутри фазы (его утверждает обычная
схема рядами, `scheme.py`) и не устройство (это `arhitektura.py`), а
РАСПРЕДЕЛЕНИЕ — в какую фазу модель вошла, в какую нет, и чем это
оборачивается (`itog`).

ПРЕДЕЛ «ЧЕТЫРЕ КЛЕТКИ В РЯДУ» ДЕРЖИТСЯ НА КАЖДОЙ ФАЗЕ ОТДЕЛЬНО, А НЕ НА
КОНВЕЙЕРЕ ЦЕЛИКОМ — и в этом весь смысл формы (§2.7 переноса): «девять шагов
это три группы по три, а не лента из девяти». Поэтому фазы рисуются СВОИМИ
рядами (стрелка идёт только ВНУТРИ фазы), а между фазами — скобка и зазор,
а не стрелка: иначе форма тайком собрала бы ровно ту длинную ленту, от
которой заведена. Фаза с пятью шагами называется `[фазы]`, а не ужимается
кеглем — ровно как у `arhitektura.py`.

ЗОЛОТО ЗДЕСЬ — ЗАЛИВКА КЛЕТКИ, А НЕ ТЕКСТ (правило перевода §1 того же
файла): `#F0AB00` текстом на светлом даёт 1,99 : 1 при пороге 3,0. Клетка
`model_in` — золотая заливка, текст `#21295C` поверх (6,85 : 1). Скобка фазы
и её подпись — не золото: `#1C7293` (обводка) и `#065A82` (подпись), они
называют группу, а не выделяют её.

Контракт фронтматтера:

    fazy:
      groups:
        - head: "Поиск облика"
          steps: ["Блокинг и первая форма", "Набросок текстур",
                  "Предварительное освещение"]
          model_in: [0]            # НОМЕРА шагов с нуля, где была модель
        - head: "Подготовка"
          steps: ["Ретопология", "Развёртка", "Риггинг"]
        - head: "Использование"
          steps: ["Анимация", "Физика", "Рендер"]
      itog: "людям остаются самые дорогие инженерные стадии"

Легенды форма не рисует: какая клетка золотая — видно по самой клетке, а
вторая подпись того же смысла читалась бы повтором, а не разъяснением
(README-formy, договор формы, п. 4 — «ничего не утверждать по умолчанию», и
здесь симметрично: ничего не ОБЪЯСНЯТЬ дважды).
"""
from dataclasses import dataclass

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, MID, SURFACE

FAZY_KEYS = {"groups", "itog"}
GROUP_KEYS = {"head", "steps", "model_in"}


@dataclass(frozen=True)
class FazyStyle:
    pad: float = 0.12               # поле внутри клетки
    gap: float = 0.08               # просвет клетка — стрелка (внутри фазы)
    arrow_w: float = 0.22
    arrow_h: float = 0.13
    group_gap: float = 0.32         # просвет между фазами (без стрелки)
    cell_hi: float = 14.5
    cell_lo: float = 12.0           # пол видимого слоя, см. `floor.py`
    cell_rows: int = 3
    cell_ls: float = 1.14
    cell_min_h: float = 0.80
    label_pt: float = 13.0          # пол видимого слоя
    label_gap: float = 0.07         # подпись фазы — скобка
    label_rows: int = 2
    label_ls: float = 1.10
    bracket_line_h: float = 0.024
    bracket_tick: float = 0.09      # скобка — верх клеток
    itog_pt: float = 15.0
    itog_ls: float = 1.16
    itog_gap: float = 0.20          # клетки — плашка итога (считая связку)
    itog_pad: float = 0.16
    tie_w: float = 0.022
    tie_min: float = 0.10
    max_groups: int = 4
    min_groups: int = 2
    max_steps: int = 4
    min_steps: int = 2
    min_cell_w: float = 1.00


DEFAULT = FazyStyle()


# ── разбор поля ─────────────────────────────────────────────────────


def fazy_of(sl, st=DEFAULT):
    """Поле `fazy` → разобранный конвейер или None.

    Чужая форма поля не роняет сборку: она называется `[фазы]`, и кадр
    собирается без схемы — тот же договор, что у `arhitektura_of`."""
    raw = sl.meta.get("fazy")
    sid = sl.sid
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[фазы] {sid}: поле `fazy` — {type(raw).__name__}, а "
                    "должно быть groups/itog")
        return None
    unknown = sorted(set(raw) - FAZY_KEYS)
    if unknown:
        report.warn(f"[фазы] {sid}: ключ(и) {' · '.join(unknown)} ядро не "
                    "читает, и на кадре он не скажется ничем")
    gg = raw.get("groups")
    if not isinstance(gg, list) or not gg:
        report.warn(f"[фазы] {sid}: в `fazy` нет `groups` — конвейеру "
                    "нечего показывать")
        return None
    groups = []
    for i, g in enumerate(gg, 1):
        if not isinstance(g, dict):
            report.warn(f"[фазы] {sid}: фаза {i} не head/steps/model_in")
            continue
        unknown = sorted(set(g) - GROUP_KEYS)
        if unknown:
            report.warn(f"[фазы] {sid}: фаза {i} — ключ(и) "
                        f"{' · '.join(unknown)} ядро не читает")
        head = str(g.get("head") or "").strip()
        if not head:
            report.warn(f"[фазы] {sid}: у фазы {i} нет `head` — "
                        "безымянная скобка ничего не называет")
            continue
        steps = [str(x).strip() for x in (g.get("steps") or [])
                 if str(x).strip()]
        if not steps:
            report.warn(f"[фазы] {sid}: у фазы «{head}» нет `steps`")
            continue
        mi_raw = g.get("model_in") or []
        if not isinstance(mi_raw, (list, tuple)):
            report.warn(f"[фазы] {sid}: у фазы «{head}» `model_in` — "
                        f"{type(mi_raw).__name__}, а должен быть список "
                        "номеров шагов")
            mi_raw = []
        model_in = set()
        for v in mi_raw:
            try:
                iv = int(v)
            except (TypeError, ValueError):
                report.warn(f"[фазы] {sid}: у фазы «{head}» в `model_in` "
                            f"значение «{v}» не целое число шага")
                continue
            if not 0 <= iv < len(steps):
                report.warn(
                    f"[фазы] {sid}: у фазы «{head}» `model_in` называет шаг "
                    f"{iv}, а шагов {len(steps)} (считая с нуля, крайний — "
                    f"{len(steps) - 1}) — подсветка уйдёт мимо клетки")
                continue
            model_in.add(iv)
        groups.append({"head": head, "steps": steps, "model_in": model_in})
    if not groups:
        return None
    return {"groups": groups, "itog": str(raw.get("itog") or "").strip()}


# ── мера ────────────────────────────────────────────────────────────


def _longest(text, f):
    return max(text.split(), key=lambda x: metrics.text_w(x, f, True),
               default="")


def cell_w(d, w, st=DEFAULT):
    """Ширина клетки — ОДНА на весь конвейер: клетки разных фаз остаются
    частями одного конвейера, а не разными по весу вставками."""
    ns = [len(g["steps"]) for g in d["groups"]]
    total_cells = sum(ns)
    total_gaps = sum(n - 1 for n in ns)       # стрелки ВНУТРИ фаз
    room = (w - (len(ns) - 1) * st.group_gap
            - total_gaps * (st.arrow_w + 2 * st.gap))
    return max(0.1, room / max(total_cells, 1))


def group_w(n, cw, st=DEFAULT):
    return n * cw + (n - 1) * (st.arrow_w + 2 * st.gap)


def _iw(cw, st):
    return max(0.3, (cw - 2 * st.pad) * metrics.W_SAFE)


def cell_size(d, w, st=DEFAULT):
    """Один кегль на ВСЕ клетки, по той же причине, что у `arhitektura.head_size`."""
    cw = cell_w(d, w, st)
    iw = _iw(cw, st)
    f = st.cell_hi
    while f > st.cell_lo:
        ok = True
        for g in d["groups"]:
            for t in g["steps"]:
                if metrics.n_lines(t, f, iw, True) > st.cell_rows or \
                        metrics.text_w(_longest(t, f), f, True) > iw * 72.0:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            break
        f -= 0.5
    return f


def _cell_line_h(f, st):
    return f * st.cell_ls * metrics.LH / 72.0 * metrics.SAFE


def cell_h(d, w, st=DEFAULT):
    cw = cell_w(d, w, st)
    iw = _iw(cw, st)
    f = cell_size(d, w, st)
    best = st.cell_min_h
    for g in d["groups"]:
        for t in g["steps"]:
            h = 2 * st.pad + min(st.cell_rows, metrics.n_lines(t, f, iw, True)) \
                * _cell_line_h(f, st)
            best = max(best, h)
    return best


def label_h(d, w, st=DEFAULT):
    cw = cell_w(d, w, st)
    best = 0.0
    for g in d["groups"]:
        gw = group_w(len(g["steps"]), cw, st)
        best = max(best, metrics.est_h(g["head"], st.label_pt, max(0.3, gw),
                                        st.label_ls, True))
    return best


def _itog_h(d, w, st=DEFAULT):
    if not d["itog"]:
        return 0.0
    iw = max(0.3, w - 2 * st.itog_pad)
    return (st.itog_gap + 2 * st.itog_pad
            + metrics.est_h(d["itog"], st.itog_pt, iw, st.itog_ls, True))


def fazy_h(d, w, st=DEFAULT):
    """Высота формы — она же то, что форма отнимает у тела кадра. Мера и
    рисование берут числа отсюда, из одного места: две формулы одного числа
    расходятся на первой правке."""
    h = (label_h(d, w, st) + st.label_gap + st.bracket_line_h
         + st.bracket_tick + cell_h(d, w, st))
    return h + _itog_h(d, w, st)


# ── сторож ──────────────────────────────────────────────────────────


def check_fazy(sid, d, w, st=DEFAULT):
    """`[фазы]`: фаз больше предела · фаза одна · шагов в фазе больше
    предела · шаг один · клетка тесная · слово шире клетки · строка разбора
    не влезает · подпись фазы не влезает · итог растянулся в абзац."""
    g = len(d["groups"])
    if g > st.max_groups:
        report.warn(
            f"[фазы] {sid}: фаз {g} (> {st.max_groups}) — предел «четыре "
            "клетки в ряду» держится и на числе фаз: лента фаз читается "
            "тем же длинным конвейером, от которого форма заведена")
    if g < st.min_groups:
        report.warn(
            f"[фазы] {sid}: фаза одна — группировка начинается от двух фаз; "
            "одна фаза это просто ряд, и для неё есть `scheme:`")
    for grp in d["groups"]:
        n = len(grp["steps"])
        if n > st.max_steps:
            report.warn(
                f"[фазы] {sid}: у фазы «{grp['head']}» шагов {n} "
                f"(> {st.max_steps}) — владелец, 2026-10-08: «не надо вот "
                "этот длинный пайплайн». Пятый шаг не ужимают кеглем — "
                "фазу делят на две")
        if n < st.min_steps:
            report.warn(
                f"[фазы] {sid}: у фазы «{grp['head']}» шаг один — фаза из "
                "одного шага не группировка, это клетка без скобки")
    cw = cell_w(d, w, st)
    if cw < st.min_cell_w:
        report.warn(
            f"[фазы] {sid}: клетка вышла {cw:.2f}\" (< {st.min_cell_w:.2f}\") "
            "— фаз и шагов в них больше, чем держит эта ширина")
    f = cell_size(d, w, st)
    iw = _iw(cw, st)
    for grp in d["groups"]:
        for t in grp["steps"]:
            long = _longest(t, f)
            if long and metrics.text_w(long, f, True) > iw * 72.0:
                report.warn(
                    f"[фазы] {sid}: слову «{long}» нужно "
                    f"{metrics.text_w(long, f, True) / 72.0:.2f}\" при "
                    f"{f:.1f} пт, а клетка вышла {iw:.2f}\" — слово будет "
                    "разорвано переносом посреди корня")
            elif metrics.n_lines(t, f, iw, True) > st.cell_rows:
                report.warn(
                    f"[фазы] {sid}: шаг «{t[:40]}…» не влезает и на "
                    f"{f:.1f} пт — это пол видимого слоя")
    for grp in d["groups"]:
        gw = group_w(len(grp["steps"]), cw, st)
        if metrics.n_lines(grp["head"], st.label_pt, max(0.3, gw), True) \
                > st.label_rows:
            report.warn(
                f"[фазы] {sid}: подпись фазы «{grp['head']}» не влезает в "
                f"ширину скобки {gw:.2f}\" на {st.label_pt:.1f} пт")
    if d["itog"]:
        iw2 = max(0.3, w - 2 * st.itog_pad)
        ln = metrics.n_lines(d["itog"], st.itog_pt, iw2, True)
        if ln > 2:
            report.warn(
                f"[фазы] {sid}: итог занимает {ln} строки (> 2) — это уже "
                "разбор, не вывод; место ему в заметках")


# ── рисование ───────────────────────────────────────────────────────


def _bracket(s, x, y, gw, st):
    """Скобка фазы: горизонтальная черта и два уса, повёрнутые вниз, к
    клеткам. Собственный примитив, по тому же договору, что `_line` у
    `vynoski.py`: `prims.py` фигуры-дуги не держит, а править общий файл
    этой нити нельзя — параллельно работают другие."""
    th = st.bracket_line_h
    prims.rect(s, x, y, gw, th, LIGHT, count="скобка")
    tick_w = th
    prims.rect(s, x, y, tick_w, st.bracket_tick, LIGHT, count="скобка")
    prims.rect(s, x + gw - tick_w, y, tick_w, st.bracket_tick, LIGHT,
               count="скобка")


def draw_fazy(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Фазы в ряд, каждая со своей скобкой и своим мини-конвейером клеток;
    итог снизу, со связкой к фазам без `model_in`. Возвращает занятую
    высоту."""
    tag = tag or sid
    cw = cell_w(d, w, st)
    ch = cell_h(d, w, st)
    f = cell_size(d, w, st)
    floor.pt(f, tag, "клетка конвейера фаз")
    lh = label_h(d, w, st)
    floor.pt(st.label_pt, tag, "подпись фазы")
    cell_top = y + lh + st.label_gap + st.bracket_line_h + st.bracket_tick

    cx = x
    free_centers = []    # (x центра фазы, нет ли model_in) — под связки
    for gi, grp in enumerate(d["groups"]):
        n = len(grp["steps"])
        gw = group_w(n, cw, st)
        prims.text_box(s, cx, y, gw, lh, grp["head"], size=st.label_pt,
                       bold=True, color=MID, align=PP_ALIGN.CENTER,
                       ls=st.label_ls, tag=f"{tag}/фаза{gi + 1}/подпись")
        _bracket(s, cx, y + lh + st.label_gap, gw, st)
        bx = cx
        for si, step in enumerate(grp["steps"]):
            if si:
                prims.arrow(s, bx + st.gap, cell_top + ch / 2 - st.arrow_h / 2,
                            st.arrow_w, st.arrow_h, LIGHT)
                bx += st.arrow_w + 2 * st.gap
            gold = si in grp["model_in"]
            prims.ocean_box(s, bx, cell_top, cw, ch,
                            fill=GOLD if gold else SURFACE,
                            stroke=LIGHT, stroke_pt=1.5)
            if gold:
                report.GOLD_SEEN.add(sid)
            iw = _iw(cw, st)
            th = min(st.cell_rows, metrics.n_lines(step, f, iw, True)) \
                * _cell_line_h(f, st)
            prims.text_box(s, bx + st.pad, cell_top + (ch - th) / 2, iw, th,
                           step, size=f, bold=True, color=DEEP,
                           align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                           ls=st.cell_ls, tag=f"{tag}/фаза{gi + 1}/шаг{si + 1}")
            bx += cw
        free_centers.append((cx + gw / 2, not grp["model_in"]))
        cx += gw + st.group_gap

    cy = cell_top + ch
    if d["itog"]:
        box_y = cy + st.itog_gap
        for gx, free in free_centers:
            if free:
                prims.rect(s, gx - st.tie_w / 2, cy, st.tie_w,
                           max(st.tie_min, st.itog_gap - 0.02), LIGHT,
                           count="связка")
        box_h = _itog_h(d, w, st) - st.itog_gap
        prims.ocean_box(s, x, box_y, w, box_h)
        floor.pt(st.itog_pt, tag, "итог конвейера фаз")
        iw2 = max(0.3, w - 2 * st.itog_pad)
        th2 = metrics.est_h(d["itog"], st.itog_pt, iw2, st.itog_ls, True)
        prims.text_box(s, x + st.itog_pad, box_y + (box_h - th2) / 2, iw2, th2,
                       d["itog"], size=st.itog_pt, bold=True, color=DEEP,
                       align=PP_ALIGN.CENTER, ls=st.itog_ls, tag=f"{tag}/итог")
        cy = box_y + box_h
    report.PRIM["фазы"] += 1
    return cy - y
