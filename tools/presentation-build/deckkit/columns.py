# -*- coding: utf-8 -*-
"""ДВА СТОЛБЦА `columns:` — ТОЛЬКО под противопоставление.

Из lec-07. Отличается от `flow.two_columns` не видом, а назначением, и
смешивать их нельзя:

* `flow.two_columns` РАЗРЕЗАЕТ одно тело на две колонки, потому что в одну
  оно не влезает. Это решение о месте.
* `columns` объявляет два столбца как СОДЕРЖАНИЕ: «что получается / что не
  получается». Это утверждение кадра, и оно заявлено во фронтматтере.

Поэтому поле `columns` на кадре типа не `comparison` даёт предупреждение:
перечень кейсов в двух столбцах — это не противопоставление, а экономия
места, и ей место в `flow.two_columns`.

Контракт фронтматтера:

    columns:
      left:  {head: "Что получается", items: ["…", "…"]}
      right: {head: "Что не получается", items: ["…", "…"]}
"""
from . import metrics, prims, report
from .theme import DEEP, LIGHT, MID, SURFACE, TEAL, WHITE

GAP = 0.34
PAD = 0.18
TOP_PAD = 0.17
HEAD_PT = 14.0
HEAD_LS = 1.12
ITEM_HI, ITEM_LO, ITEM_FLOOR = 14.5, 11.0, 9.0
ITEM_LS = 1.26
MIN_H, MAX_H = 1.55, 3.40


def columns_of(sl, *, require_type="comparison"):
    """Поле `columns` → пара столбцов или None."""
    raw = sl.meta.get("columns")
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict) or "left" not in raw or "right" not in raw:
        report.warn(f"[столбцы] {sl.sid}: поле `columns` должно иметь "
                    "`left` и `right`")
        return None
    cols = []
    for side in ("left", "right"):
        c = raw[side]
        if not isinstance(c, dict):
            report.warn(f"[столбцы] {sl.sid}: `{side}` не словарь")
            return None
        cols.append({"head": str(c.get("head") or "").strip(),
                     "items": [str(i).strip() for i in (c.get("items") or [])
                               if str(i).strip()]})
    if require_type and sl.meta.get("type") != require_type:
        report.warn(
            f"[столбцы] {sl.sid}: два столбца объявлены на кадре типа "
            f"«{sl.meta.get('type')}» — они идут ТОЛЬКО под "
            "противопоставление «что получается / что не получается», тип "
            f"кадра `{require_type}`")
    return cols


def draw_columns(s, sid, cols, x, y, w, h):
    """Два столбца в коробках мотива. Левый на поверхности, правый белый с
    бирюзовой обводкой — различие сторон держится цветом рамки, а не
    подписью «против»."""
    cw = (w - GAP) / 2
    for i, c in enumerate(cols):
        xx = x + i * (cw + GAP)
        prims.ocean_box(s, xx, y, cw, h, fill=SURFACE if i == 0 else WHITE,
                        stroke=LIGHT if i == 0 else TEAL)
        iw = cw - 2 * PAD
        yy = y + TOP_PAD
        if c["head"]:
            hh = metrics.est_h(c["head"], HEAD_PT, iw, HEAD_LS)
            prims.text_box(s, xx + PAD, yy, iw, hh, c["head"], size=HEAD_PT,
                           bold=True, color=MID if i == 0 else TEAL,
                           ls=HEAD_LS, tag=f"{sid}/столбец-шапка")
            yy += hh + 0.12
        body = "\n".join("• " + it for it in c["items"])
        if body:
            avail = y + h - TOP_PAD - yy
            sz = metrics.fit_size(body, iw, avail, hi=ITEM_HI, lo=ITEM_LO,
                                  floor=ITEM_FLOOR, ls=ITEM_LS,
                                  tag=f"{sid}/столбец-{i + 1}")
            prims.text_box(s, xx + PAD, yy, iw, avail, body, size=sz,
                           color=DEEP, ls=ITEM_LS,
                           tag=f"{sid}/столбец-{i + 1}")
    report.PRIM["столбцы"] += 1
