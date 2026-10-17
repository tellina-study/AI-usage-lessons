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
from . import floor, metrics, prims, report
from .theme import DEEP, LIGHT, MID, SURFACE, TEAL, WHITE

GAP = 0.34
PAD = 0.18
TOP_PAD = 0.17
HEAD_PT = 14.0
HEAD_LS = 1.12
# Пол видимого слоя (`floor.py`). Подбор берёт НАИБОЛЬШИЙ кегль, который
# влезает, — то есть ниже 12 пт он опускается только там, где 12 не влезает
# вовсе, и тогда об этом говорит `[пол]` (ниже по тексту). Пол поставлен
# МЯГКИМ нарочно: жёсткий оставил бы перечень торчать из своей коробки —
# замерено на `s55a`, 1,30" текста в коробке 1,11". Между «мелко, и об этом
# сказано» и «вылезло за грань молча» выбрано первое; прежде здесь не было
# ни того, ни другого — столбец уходил под пол без единого слова.
ITEM_HI, ITEM_LO, ITEM_FLOOR = 14.5, 9.0, 9.0
ITEM_LS = 1.26
MIN_H, MAX_H = 1.55, 3.40


def _strok(tekst, kegl, iw):
    """Сколько строк займёт пункт перечня. Высота делится на межстрочный
    шаг того же кегля — та же мера, которой считает раскладка."""
    shag = kegl * ITEM_LS / 72.0
    return max(1, round(metrics.est_h("• " + tekst, kegl, iw, ITEM_LS) / shag))


def proverit_pary(sid, cols, shiriny, kegli):
    """[пары] — строка слева не стоит напротив своей строки справа.

    ЗАЧЕМ ЭТО ЗДЕСЬ. Два столбца рисуются как два НЕЗАВИСИМЫХ перечня, и
    для сборки это два валидных списка: ни одна проверка пакета не знает,
    что пункт слева и пункт справа — ОДНА пара. Поэтому пункт слева в одну
    строку против пункта справа в две сдвигает всё, что ниже, и к шестой
    паре проявление стоит напротив чужого последствия. Молча.

    Найдено не прогоном, а просмотром снимка — сессией кадров о влиянии ИИ
    на человека (#244), и найдено ДВАЖДЫ В ОБЕ СТОРОНЫ: при равных столбцах
    разъезжался правый, при доле 0,40 — левый. Обходилось подгонкой длин,
    то есть держалось на дисциплине автора, а не на мере. Теперь на мере.

    Проверка включается только там, где пара ЕСТЬ по содержанию («как
    проявляется / последствия»): у противопоставления «получается / не
    получается» пункты не парные, и равнять их число нечем и незачем.
    """
    levye, pravye = cols[0]["items"], cols[1]["items"]
    if len(levye) != len(pravye):
        report.warn(
            f"[пары] {sid}: слева {len(levye)} строк, справа "
            f"{len(pravye)} — столбцы объявлены парами, и при разном числе "
            f"пунктов пара читается напротив чужой строки")
        return
    rashod = []
    for i, (l, r) in enumerate(zip(levye, pravye), 1):
        sl_ = _strok(l, kegli[0], shiriny[0] - 2 * PAD)
        sr_ = _strok(r, kegli[1], shiriny[1] - 2 * PAD)
        if sl_ != sr_:
            rashod.append(f"пара {i}: {sl_} против {sr_}")
    if rashod:
        report.warn(
            f"[пары] {sid}: строки пар не совпадают по высоте — "
            + " · ".join(rashod[:4])
            + ("…" if len(rashod) > 4 else "")
            + "; всё, что ниже первой такой пары, читается со сдвигом")


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


def draw_columns(s, sid, cols, x, y, w, h, dolya_levogo=0.5, pary=False):
    """Два столбца в коробках мотива. Левый на поверхности, правый белый с
    бирюзовой обводкой — различие сторон держится цветом рамки, а не
    подписью «против».

    `dolya_levogo` — доля ширины, отданная левому столбцу; по умолчанию
    поровну. Неравное деление нужно там, где стороны неравны по весу:
    пара «как проявляется / последствия» даёт отношение медиан около
    1 : 2 (замер сессии кадров о влиянии ИИ на человека, #244), и при
    делении пополам правый столбец переносит вдвое чаще левого и съедает
    высоту обоих — кегль подбирается на двоих."""
    dolya_levogo = min(0.75, max(0.25, float(dolya_levogo)))
    shiriny = [(w - GAP) * dolya_levogo, (w - GAP) * (1.0 - dolya_levogo)]
    kegli = [ITEM_HI, ITEM_HI]
    xx = x
    for i, c in enumerate(cols):
        cw = shiriny[i]
        prims.ocean_box(s, xx, y, cw, h, fill=SURFACE if i == 0 else WHITE,
                        stroke=LIGHT if i == 0 else TEAL)
        iw = cw - 2 * PAD
        yy = y + TOP_PAD
        if c["head"]:
            hh = metrics.est_h(c["head"], HEAD_PT, iw, HEAD_LS)
            floor.pt(HEAD_PT, f"{sid}/столбец-{i + 1}", "шапка столбца")
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
            floor.pt(sz, f"{sid}/столбец-{i + 1}", "перечень столбца")
            kegli[i] = sz
            prims.text_box(s, xx + PAD, yy, iw, avail, body, size=sz,
                           color=DEEP, ls=ITEM_LS,
                           tag=f"{sid}/столбец-{i + 1}")
        xx += cw + GAP
    if pary and len(cols) == 2:
        proverit_pary(sid, cols, shiriny, kegli)
    report.PRIM["столбцы"] += 1
