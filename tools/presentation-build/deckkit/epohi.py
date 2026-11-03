# -*- coding: utf-8 -*-
"""КАРТОЧКИ ДВУХ ЭПОХ `epohi:` — Событие → Реакция → Итог, и разошлось на
каком шаге.

Перенос приёма §2.10 из `library/lectures/lec-08/rework-v5/
PERENOS-PRIYOMOV.md`: `image/s10` — «2006 — Сработало» и «2026 — Не
прошло», в каждой карточке лесенка с отступом (Событие → Реакция → Итог), и
внизу карточки одна строка вывода; под обеими карточками — общий вывод во
всю ширину.

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ: один и тот же манёвр с разницей в годы дал разные
исходы — и ПОКАЗЫВАЕТ, на каком шаге разошлось, лесенкой, а не абзацем.
Этим она отличается от `scheme.py` (тот утверждает порядок одной линии) и от
`columns.py` (тот противопоставляет СТОРОНЫ, а не разложенные по шагам
исходы одного и того же сценария).

ГЛАВНЫЙ СТОРОЖ ФОРМЫ — РАВНОЕ ЧИСЛО СТУПЕНЕЙ. «Число ступеней в карточках
обязано совпадать, иначе `[эпохи]`: это сравнение, и сравнивают одинаково
разложенное» (§2.10 переноса, буквально). Три ступени слева и две справа не
сравнение, а две разные формы, случайно поставленные рядом.

ЗОЛОТО ЗДЕСЬ — ЗАЛИВКА СТРОКИ-ВЫВОДА ВНУТРИ КАРТОЧКИ, А НЕ ТЕКСТ (правило
перевода §1): `#F0AB00` текстом на светлом даёт 1,99 : 1 при пороге 3,0,
заливкой с тёмным текстом поверх — 6,85 : 1. Левая карточка обведена
`#1C7293`, правая — `#028090`: те же две краски, что держит вся палитра
курса для «первое / второе», без изобретения третьей.

Контракт фронтматтера:

    epohi:
      left:
        head: "2006 — сработало"
        steps:
          - {label: "Событие", text: "цена фото падает"}
          - {label: "Реакция", text: "покупают разрушителя цены"}
          - {label: "Итог", text: "рынок разделился, игрок уцелел"}
        vyvod: "микросток был новым каналом продажи той же вещи"
      right:
        head: "2026 — не прошло"
        steps: [...]                    # то же число ступеней, что слева
        vyvod: "покупать нечего: у вещи не стало владельца"
      obshchiy_vyvod: "когда дешевеет канал — выживает тот, кто его купит; …"
"""
from dataclasses import dataclass

from pptx.enum.text import PP_ALIGN

from . import floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, MID, SURFACE, TEAL

TOP_KEYS = {"left", "right", "obshchiy_vyvod"}
CARD_KEYS = {"head", "steps", "vyvod"}
STEP_KEYS = {"label", "text"}


@dataclass(frozen=True)
class EpohiStyle:
    pad: float = 0.18
    gap: float = 0.26                  # просвет между карточками
    head_pt: float = 16.0
    head_ls: float = 1.08
    head_gap: float = 0.12
    step_pt: float = 13.5
    step_lo: float = 12.0              # пол видимого слоя
    step_ls: float = 1.14
    label_pt: float = 12.5             # пол видимого слоя
    label_gap: float = 0.03            # ярлык ступени — текст ступени
    step_gap: float = 0.10             # между ступенями лесенки
    indent: float = 0.22               # сдвиг каждой следующей ступени
    vyvod_pt: float = 13.5             # пол видимого слоя
    vyvod_ls: float = 1.14
    vyvod_pad: float = 0.12
    vyvod_gap: float = 0.14            # лесенка — плашка вывода
    obshchiy_pt: float = 15.0          # пол видимого слоя
    obshchiy_ls: float = 1.16
    obshchiy_gap: float = 0.20         # карточки — общий вывод
    obshchiy_pad: float = 0.16
    min_card_w: float = 3.00
    min_step_w: float = 0.60
    max_steps: int = 5
    min_steps: int = 2


DEFAULT = EpohiStyle()


# ── разбор поля ─────────────────────────────────────────────────────


def _step_of(sid, side_name, i, raw):
    if not isinstance(raw, dict):
        report.warn(f"[эпохи] {sid}: «{side_name}», ступень {i} — "
                    f"{type(raw).__name__}, а должна быть label/text")
        return None
    unknown = sorted(set(raw) - STEP_KEYS)
    if unknown:
        report.warn(f"[эпохи] {sid}: «{side_name}», ступень {i} — ключ(и) "
                    f"{' · '.join(unknown)} ядро не читает")
    label = str(raw.get("label") or "").strip()
    text = str(raw.get("text") or "").strip()
    if not label:
        report.warn(f"[эпохи] {sid}: «{side_name}», ступень {i} без "
                    "`label` — шаг лесенки без имени читается провалом "
                    "разметки")
    if not text:
        report.warn(f"[эпохи] {sid}: «{side_name}», ступень {i} без `text`")
    if not label and not text:
        return None
    return {"label": label, "text": text}


def _card_of(sid, name, raw):
    if not isinstance(raw, dict):
        report.warn(f"[эпохи] {sid}: «{name}» — {type(raw).__name__}, а "
                    "должно быть head/steps/vyvod")
        return None
    unknown = sorted(set(raw) - CARD_KEYS)
    if unknown:
        report.warn(f"[эпохи] {sid}: «{name}» — ключ(и) "
                    f"{' · '.join(unknown)} ядро не читает")
    head = str(raw.get("head") or "").strip()
    if not head:
        report.warn(f"[эпохи] {sid}: у карточки «{name}» нет `head`")
    ss_raw = raw.get("steps")
    if not isinstance(ss_raw, list) or not ss_raw:
        report.warn(f"[эпохи] {sid}: у карточки «{name}» нет `steps`")
        return None
    steps = []
    for i, r in enumerate(ss_raw, 1):
        s2 = _step_of(sid, name, i, r)
        if s2:
            steps.append(s2)
    if not steps:
        return None
    vyvod = str(raw.get("vyvod") or "").strip()
    if not vyvod:
        report.warn(f"[эпохи] {sid}: у карточки «{name}» нет `vyvod` — без "
                    "него в карточке не остаётся золотого акцента, а исход "
                    "манёвра читается только по лесенке, не по выводу")
    return {"head": head, "steps": steps, "vyvod": vyvod}


def epohi_of(sl, st=DEFAULT):
    """Поле `epohi` → разобранная пара карточек или None."""
    raw = sl.meta.get("epohi")
    sid = sl.sid
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[эпохи] {sid}: поле `epohi` — {type(raw).__name__}, а "
                    "должно быть left/right/obshchiy_vyvod")
        return None
    unknown = sorted(set(raw) - TOP_KEYS)
    if unknown:
        report.warn(f"[эпохи] {sid}: ключ(и) {' · '.join(unknown)} ядро не "
                    "читает")
    left = _card_of(sid, "left", raw.get("left"))
    right = _card_of(sid, "right", raw.get("right"))
    if left is None or right is None:
        return None
    if len(left["steps"]) != len(right["steps"]):
        report.warn(
            f"[эпохи] {sid}: ступеней слева {len(left['steps'])}, справа "
            f"{len(right['steps'])} — сравнивают только одинаково "
            "разложенное; разное число ступеней — это уже не сравнение "
            "манёвра, а две разные формы рядом")
    return {"left": left, "right": right,
            "obshchiy_vyvod": str(raw.get("obshchiy_vyvod") or "").strip()}


# ── мера ────────────────────────────────────────────────────────────


def card_w(w, st=DEFAULT):
    return (w - st.gap) / 2.0


def _step_w(inner_w, i, st):
    """Ширина, остающаяся ступени `i` (с нуля) после сдвига лесенки."""
    return max(0.3, inner_w - i * st.indent)


def _step_h(step, inner_w, i, st):
    sw = _step_w(inner_w, i, st)
    lh = metrics.est_h(step["label"], st.label_pt, sw, 1.08, True) \
        if step["label"] else 0.0
    th = metrics.est_h(step["text"], st.step_pt, sw, st.step_ls) \
        if step["text"] else 0.0
    gap = st.label_gap if (step["label"] and step["text"]) else 0.0
    return lh + gap + th


def _body_h(card, inner_w, st):
    n = len(card["steps"])
    hs = [_step_h(s2, inner_w, i, st) for i, s2 in enumerate(card["steps"])]
    return sum(hs) + st.step_gap * max(0, n - 1)


def _vyvod_h(card, inner_w, st):
    if not card["vyvod"]:
        return 0.0
    iw = max(0.3, inner_w - 2 * st.vyvod_pad)
    return (2 * st.vyvod_pad
            + metrics.est_h(card["vyvod"], st.vyvod_pt, iw, st.vyvod_ls, True))


def card_h(card, cw, st=DEFAULT):
    inner_w = max(0.3, cw - 2 * st.pad)
    h = 2 * st.pad
    h += metrics.est_h(card["head"], st.head_pt, inner_w, st.head_ls, True)
    h += st.head_gap
    h += _body_h(card, inner_w, st)
    if card["vyvod"]:
        h += st.vyvod_gap + _vyvod_h(card, inner_w, st)
    return h


def _obshchiy_h(d, w, st=DEFAULT):
    if not d["obshchiy_vyvod"]:
        return 0.0
    iw = max(0.3, w - 2 * st.obshchiy_pad)
    return (2 * st.obshchiy_pad
            + metrics.est_h(d["obshchiy_vyvod"], st.obshchiy_pt, iw,
                            st.obshchiy_ls, True))


def epohi_h(d, w, st=DEFAULT):
    """Высота формы — она же то, что форма отнимает у тела кадра."""
    cw = card_w(w, st)
    h = max(card_h(d["left"], cw, st), card_h(d["right"], cw, st))
    if d["obshchiy_vyvod"]:
        h += st.obshchiy_gap + _obshchiy_h(d, w, st)
    return h


# ── сторож ──────────────────────────────────────────────────────────


def _longest(text, f):
    return max(text.split(), key=lambda x: metrics.text_w(x, f, True),
               default="")


def check_epohi(sid, d, w, st=DEFAULT):
    """`[эпохи]`: карточка тесная · ступеней больше предела · ступень одна ·
    лесенка съела колонку · строка не влезает."""
    cw = card_w(w, st)
    if cw < st.min_card_w:
        report.warn(f"[эпохи] {sid}: карточка вышла {cw:.2f}\" "
                    f"(< {st.min_card_w:.2f}\") — лесенке и выводу в такой "
                    "ширине тесно")
    for name, card in (("left", d["left"]), ("right", d["right"])):
        n = len(card["steps"])
        if n > st.max_steps:
            report.warn(f"[эпохи] {sid}: у «{name}» ступеней {n} "
                        f"(> {st.max_steps}) — лесенка такой высоты не "
                        "держится в карточке")
        if n < st.min_steps:
            report.warn(f"[эпохи] {sid}: у «{name}» ступень одна — лесенки "
                        "без второй ступени не бывает, это просто карточка")
        inner = max(0.3, cw - 2 * st.pad)
        for i, s2 in enumerate(card["steps"], 1):
            sw = _step_w(inner, i - 1, st)
            if sw < st.min_step_w:
                report.warn(
                    f"[эпохи] {sid}: у «{name}» ступень {i} сдвинута на "
                    f"{(i - 1) * st.indent:.2f}\" и оставляет {sw:.2f}\" "
                    f"(< {st.min_step_w:.2f}\") под текст — лесенка зашла "
                    "дальше, чем держит карточка")
                continue
            for text, pt_, bold in ((s2["label"], st.label_pt, True),
                                    (s2["text"], st.step_pt, False)):
                if not text:
                    continue
                long = _longest(text, pt_)
                if long and metrics.text_w(long, pt_, bold) > sw * 72.0:
                    report.warn(
                        f"[эпохи] {sid}: у «{name}» ступень {i}, слову "
                        f"«{long}» не хватает ширины {sw:.2f}\" на "
                        f"{pt_:.1f} пт")


# ── рисование ───────────────────────────────────────────────────────


def _draw_lesenka(s, sid, card, x, y, inner_w, st, tag):
    """Лесенка шагов: каждая ступень сдвинута правее предыдущей. Возвращает
    занятую высоту."""
    n = len(card["steps"])
    cy = y
    for i, step in enumerate(card["steps"]):
        sw = _step_w(inner_w, i, st)
        sx = x + i * st.indent
        if step["label"]:
            floor.pt(st.label_pt, tag, "ярлык ступени эпохи")
            lh = metrics.est_h(step["label"], st.label_pt, sw, 1.08, True)
            prims.text_box(s, sx, cy, sw, lh, step["label"],
                           size=st.label_pt, bold=True, color=MID, ls=1.08,
                           tag=f"{tag}/ступень{i + 1}/ярлык")
            cy += lh + (st.label_gap if step["text"] else 0.0)
        if step["text"]:
            floor.pt(st.step_pt, tag, "текст ступени эпохи")
            th = metrics.est_h(step["text"], st.step_pt, sw, st.step_ls)
            prims.text_box(s, sx, cy, sw, th, step["text"], size=st.step_pt,
                           color=DEEP, ls=st.step_ls,
                           tag=f"{tag}/ступень{i + 1}/текст")
            cy += th
        if i < n - 1:
            cy += st.step_gap
    return cy - y


def _draw_card(s, sid, card, x, y, cw, ch, stroke, st, tag):
    prims.ocean_box(s, x, y, cw, ch, fill=SURFACE, stroke=stroke,
                    stroke_pt=1.5)
    inner_w = max(0.3, cw - 2 * st.pad)
    cx = x + st.pad
    cy = y + st.pad
    floor.pt(st.head_pt, tag, "заголовок эпохи")
    hh = metrics.est_h(card["head"], st.head_pt, inner_w, st.head_ls, True)
    prims.text_box(s, cx, cy, inner_w, hh, card["head"], size=st.head_pt,
                   bold=True, color=DEEP, ls=st.head_ls,
                   tag=f"{tag}/заголовок")
    cy += hh + st.head_gap
    cy += _draw_lesenka(s, sid, card, cx, cy, inner_w, st, tag)
    if card["vyvod"]:
        cy += st.vyvod_gap
        vh = _vyvod_h(card, inner_w, st)
        prims.rect(s, cx, cy, inner_w, vh, GOLD, radius=True, radius_adj=0.14,
                   count="вывод эпохи")
        report.GOLD_SEEN.add(sid)
        floor.pt(st.vyvod_pt, tag, "вывод эпохи")
        iw = max(0.3, inner_w - 2 * st.vyvod_pad)
        th = metrics.est_h(card["vyvod"], st.vyvod_pt, iw, st.vyvod_ls, True)
        prims.text_box(s, cx + st.vyvod_pad, cy + (vh - th) / 2, iw, th,
                       card["vyvod"], size=st.vyvod_pt, bold=True, color=DEEP,
                       ls=st.vyvod_ls, tag=f"{tag}/вывод")


def draw_epohi(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Две карточки рядом, общий вывод снизу во всю ширину. Возвращает
    занятую высоту."""
    tag = tag or sid
    top = y
    cw = card_w(w, st)
    ch = max(card_h(d["left"], cw, st), card_h(d["right"], cw, st))
    _draw_card(s, sid, d["left"], x, y, cw, ch, LIGHT, st, f"{tag}/слева")
    _draw_card(s, sid, d["right"], x + cw + st.gap, y, cw, ch, TEAL, st,
              f"{tag}/справа")
    cy = y + ch
    if d["obshchiy_vyvod"]:
        cy += st.obshchiy_gap
        oh = _obshchiy_h(d, w, st)
        prims.ocean_box(s, x, cy, w, oh, fill=SURFACE, stroke=LIGHT,
                        stroke_pt=1.5)
        floor.pt(st.obshchiy_pt, tag, "общий вывод эпох")
        iw = max(0.3, w - 2 * st.obshchiy_pad)
        th = metrics.est_h(d["obshchiy_vyvod"], st.obshchiy_pt, iw,
                           st.obshchiy_ls, True)
        prims.text_box(s, x + st.obshchiy_pad, cy + (oh - th) / 2, iw, th,
                       d["obshchiy_vyvod"], size=st.obshchiy_pt, bold=True,
                       color=DEEP, align=PP_ALIGN.CENTER, ls=st.obshchiy_ls,
                       tag=f"{tag}/общий-вывод")
        cy += oh
    report.PRIM["эпохи"] += 1
    return cy - y
