# -*- coding: utf-8 -*-
"""НУМЕРОВАННЫЕ КАРТОЧКИ ЗАКРЫТИЯ `vyvody:` — утверждение, не ярлык.

Перенос приёма §2.12 из `library/lectures/lec-08/rework-v5/
PERENOS-PRIYOMOV.md`: `media/s15` — широкие карточки, слева огромная цифра
1 / 2 / 3, справа жирное утверждение и две строки пояснения; внизу —
золотая линия и мост к следующей лекции.

ЦИФРА — ЕДИНСТВЕННОЕ МЕСТО ПАКЕТА, ГДЕ ЗОЛОТОЙ ТЕКСТ РАЗРЕШЁН, и это не
исключение из правила перевода §1 — это его прямое следствие. Правило:
«где в образце золотой текст — у нас золотая ЗАЛИВКА с тёмным текстом
поверх, либо глубокий `#21295C`». Здесь квадрат цифры залит `#21295C`
(глубоким, не золотом), и ПОВЕРХ него — золотая цифра: `#F0AB00` на
`#21295C` даёт 6,85 : 1, тот же порядок, что у золотой заливки с тёмным
текстом, просто фон и буква поменялись местами. Золотой заливки с золотым
текстом здесь нет и быть не может.

ПРЕДЕЛ 2–4 КАРТОЧКИ. Закрытие держит несколько утверждений, не ленту:
пятая карточка — `[выводы]`, а не кегль мельче. Пояснение у карточки —
не абзац: третья строка уже разбор, и место ему в заметках, не на кадре
закрытия (та же причина, что у `itog.py`).

Контракт фронтматтера:

    vyvody:
      items:
        - head: "Платят за выбор, а не за исполнение"
          text: "две строки пояснения"           # необязательно
      most: "дальше по курсу: класс угроз …"      # необязательно, мост к Лекции N+1
"""
from dataclasses import dataclass

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, MID, SURFACE

TOP_KEYS = {"items", "most"}
ITEM_KEYS = {"head", "text"}


@dataclass(frozen=True)
class VyvodyStyle:
    pad: float = 0.18
    gap: float = 0.16                # между карточками
    num_d: float = 0.56              # поперечник квадрата с цифрой
    num_pt: float = 24.0
    num_gap: float = 0.18            # квадрат — текст
    head_pt: float = 15.5            # пол видимого слоя
    head_ls: float = 1.12
    head_gap: float = 0.08
    text_pt: float = 13.0            # пол видимого слоя
    text_ls: float = 1.16
    max_lines: int = 2
    card_min_h: float = 0.80
    rule_h: float = 0.028            # золотая линия над мостом
    rule_gap: float = 0.14
    most_pt: float = 13.5            # пол видимого слоя
    most_ls: float = 1.16
    most_gap: float = 0.10
    max_items: int = 4
    min_items: int = 2
    min_w: float = 3.6


DEFAULT = VyvodyStyle()


# ── разбор поля ─────────────────────────────────────────────────────


def _item_of(sid, i, raw):
    if not isinstance(raw, dict):
        report.warn(f"[выводы] {sid}: вывод {i} — {type(raw).__name__}, а "
                    "должен быть head/text")
        return None
    unknown = sorted(set(raw) - ITEM_KEYS)
    if unknown:
        report.warn(f"[выводы] {sid}: вывод {i} — ключ(и) "
                    f"{' · '.join(unknown)} ядро не читает")
    head = str(raw.get("head") or "").strip()
    if not head:
        report.warn(f"[выводы] {sid}: у вывода {i} нет `head` — утверждение "
                    "без него не читается, остаётся одна цифра")
        return None
    return {"head": head, "text": str(raw.get("text") or "").strip()}


def vyvody_of(sl, st=DEFAULT):
    """Поле `vyvody` → разобранные карточки закрытия или None."""
    raw = sl.meta.get("vyvody")
    sid = sl.sid
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[выводы] {sid}: поле `vyvody` — {type(raw).__name__}, "
                    "а должно быть items/most")
        return None
    unknown = sorted(set(raw) - TOP_KEYS)
    if unknown:
        report.warn(f"[выводы] {sid}: ключ(и) {' · '.join(unknown)} ядро не "
                    "читает")
    rr = raw.get("items")
    if not isinstance(rr, list) or not rr:
        report.warn(f"[выводы] {sid}: в `vyvody` нет `items`")
        return None
    items = []
    for i, r in enumerate(rr, 1):
        it = _item_of(sid, i, r)
        if it:
            items.append(it)
    if not items:
        return None
    return {"items": items, "most": str(raw.get("most") or "").strip()}


# ── мера ────────────────────────────────────────────────────────────


def _longest(text, f):
    return max(text.split(), key=lambda x: metrics.text_w(x, f, True),
               default="")


def _text_w(w, st=DEFAULT):
    return max(0.3, w - 2 * st.pad - st.num_d - st.num_gap)


def item_h(item, w, st=DEFAULT):
    tw = _text_w(w, st)
    hh = metrics.est_h(item["head"], st.head_pt, tw, st.head_ls, True)
    body = hh
    if item["text"]:
        body += st.head_gap + metrics.est_h(item["text"], st.text_pt, tw,
                                            st.text_ls)
    return max(st.card_min_h, max(body, st.num_d) + 2 * st.pad)


def vyvody_h(d, w, st=DEFAULT):
    """Высота формы — она же то, что форма отнимает у тела кадра."""
    h = sum(item_h(it, w, st) for it in d["items"]) \
        + st.gap * max(0, len(d["items"]) - 1)
    if d["most"]:
        h += (st.rule_gap + st.rule_h + st.most_gap
              + metrics.est_h(d["most"], st.most_pt, w, st.most_ls, True))
    return h


# ── сторож ──────────────────────────────────────────────────────────


def check_vyvody(sid, d, w, st=DEFAULT):
    """`[выводы]`: выводов больше предела · вывод один · ширина тесная ·
    слово шире колонки · пояснение растянулось в абзац · мост растянулся
    в абзац."""
    n = len(d["items"])
    if n > st.max_items:
        report.warn(f"[выводы] {sid}: выводов {n} (> {st.max_items}) — "
                    "закрытие держит несколько утверждений, не ленту")
    if n < st.min_items:
        report.warn(f"[выводы] {sid}: вывод один — нумерованные карточки "
                    "заводят от двух выводов; один вывод это `itog:`")
    if w < st.min_w:
        report.warn(f"[выводы] {sid}: ширина {w:.2f}\" (< {st.min_w:.2f}\") "
                    "— квадрату с цифрой и утверждению рядом будет тесно")
    tw = _text_w(w, st)
    for i, it in enumerate(d["items"], 1):
        long = _longest(it["head"], st.head_pt)
        if long and metrics.text_w(long, st.head_pt, True) > tw * 72.0:
            report.warn(f"[выводы] {sid}: вывод {i}, слову «{long}» не "
                        f"хватает ширины {tw:.2f}\" на {st.head_pt:.1f} пт")
        if it["text"]:
            ln = metrics.n_lines(it["text"], st.text_pt, tw)
            if ln > st.max_lines:
                report.warn(
                    f"[выводы] {sid}: вывод {i}, пояснение занимает {ln} "
                    f"строки (> {st.max_lines}) — предел пояснения две "
                    "строки, дальше это разбор, а не вывод")
    if d["most"]:
        ln = metrics.n_lines(d["most"], st.most_pt, w, True)
        if ln > 2:
            report.warn(f"[выводы] {sid}: мост к следующей лекции занимает "
                        f"{ln} строки (> 2)")


# ── рисование ───────────────────────────────────────────────────────


def _draw_item(s, sid, item, n, x, y, w, h, st, tag):
    prims.ocean_box(s, x, y, w, h, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    sq = st.num_d
    sy = y + (h - sq) / 2
    prims.rect(s, x + st.pad, sy, sq, sq, DEEP, radius=True, radius_adj=0.12,
               count="номер вывода")
    floor.pt(st.num_pt, tag, "цифра вывода")
    # ЕДИНСТВЕННОЕ место пакета, где текст ставится золотом: фон квадрата
    # ГЛУБОКИЙ (`#21295C`), и пара золото-на-тёмном даёт 6,85 : 1 — см.
    # шапку модуля.
    prims.text_box(s, x + st.pad, sy, sq, sq, str(n), size=st.num_pt,
                   bold=True, color=GOLD, align=PP_ALIGN.CENTER,
                   anchor=MSO_ANCHOR.MIDDLE, ls=1.0, tag=f"{tag}/цифра",
                   quiet=True)
    report.GOLD_SEEN.add(sid)
    tx = x + st.pad + sq + st.num_gap
    tw = _text_w(w, st)
    floor.pt(st.head_pt, tag, "утверждение вывода")
    hh = metrics.est_h(item["head"], st.head_pt, tw, st.head_ls, True)
    th = metrics.est_h(item["text"], st.text_pt, tw, st.text_ls) \
        if item["text"] else 0.0
    block = hh + (st.head_gap + th if item["text"] else 0.0)
    cy = y + (h - block) / 2
    prims.text_box(s, tx, cy, tw, hh, item["head"], size=st.head_pt,
                   bold=True, color=DEEP, ls=st.head_ls,
                   tag=f"{tag}/утверждение")
    if item["text"]:
        floor.pt(st.text_pt, tag, "пояснение вывода")
        prims.text_box(s, tx, cy + hh + st.head_gap, tw, th, item["text"],
                       size=st.text_pt, color=LIGHT, ls=st.text_ls,
                       tag=f"{tag}/пояснение")


def draw_vyvody(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Карточки с номером и утверждением друг под другом; мост снизу под
    золотой линией. Возвращает занятую высоту."""
    tag = tag or sid
    top = y
    n = len(d["items"])
    for i, it in enumerate(d["items"], 1):
        ih = item_h(it, w, st)
        _draw_item(s, sid, it, i, x, y, w, ih, st, f"{tag}/вывод{i}")
        y += ih + (st.gap if i < n else 0.0)
    if d["most"]:
        y += st.rule_gap
        prims.rect(s, x, y, w, st.rule_h, GOLD, count="линия моста")
        report.GOLD_SEEN.add(sid)
        y += st.rule_h + st.most_gap
        floor.pt(st.most_pt, tag, "мост к следующей лекции")
        mh = metrics.est_h(d["most"], st.most_pt, w, st.most_ls, True)
        prims.text_box(s, x, y, w, mh, d["most"], size=st.most_pt, bold=True,
                       color=MID, ls=st.most_ls, tag=f"{tag}/мост")
        y += mh
    report.PRIM["выводы"] += 1
    return y - top
