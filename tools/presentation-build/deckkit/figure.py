# -*- coding: utf-8 -*-
"""КАДР ОДНОГО ЧИСЛА `figure:` — одна величина во весь кадр, с базой.

Владелец, посмотрев деку Лекции 7 (2026-10-14): «да и остальные слайды очень
типовые». Замер сессии наряда по 101 кадру назвал это числом: словарь деки —
полоса плашек (56 кадров), схема рядами (18, все одной первоосновы), два
столбца (7), буллиты (17). Четыре формы на сто кадров, и три из них по
природе текстовые.

Эта форма — не пятая разновидность плашки, и разница не в размере шрифта.
ПОЛОСА ПЛАШЕК отвечает на вопрос «из чего состоит счёт»: было · стало · к
чему привело, три-четыре равноправных блока в ряд. КАДР ОДНОГО ЧИСЛА
отвечает на другой: «какая величина здесь главная и против чего она
читается». У деки есть места, где содержание кадра — ровно одна величина
(«0,712 против 0,816 и 0,820»), и полоса из трёх плашек там делает ровно то,
на что владелец жалуется: превращает единственное утверждение кадра в
перечень, в котором главное надо искать.

Контракт фронтматтера:

    figure:
      value: "0,712"
      unit:  "площадь под кривой у хирурга с подсказкой"
      base:  "против 0,816 у модели одной и 0,820 у хирурга одного"
      note:  "30 хирургов по группам жребием · 150 случаев · 30 дней"

`value` и `base` ОБЯЗАТЕЛЬНЫ, и `base` — не формальность: это тот самый
знаменатель из § «Baseline / Counterfactual Mandate» (`CLAUDE.md`). Число во
весь кадр без базы — самая убедительная форма неинтерпретируемого числа,
какая в этом ядре есть, и единственный сторож, который может это поймать, —
здесь. Поэтому `base` проверяется НЕ как поле («задано ли»), а как
содержание: база без второй величины и без слова сравнения называется
`[число]`.

ЧЕГО ЭТА ФОРМА НЕ ДЕЛАЕТ. Не красит число золотом. Прожарка 2026-10-14
поймала ровно это на «key»-плашке Лекции 7: золото `#F0AB00` на белом — 1,99
при пороге 3,0, и так на 60 кадрах из 109 (`contrast.py`). Самый важный
текст кадра, набранный самым нечитаемым цветом деки, — поэтому число здесь
DEEP, а золото держит ЧЕРТА под ним: у фигуры контраста нет, читать её не
нужно. `invert: true` переворачивает кадр по второму способу, который
владелец назвал в `contrast.py`: заливка DEEP, число золотом — 6,85 : 1.
Выбор между двумя способами остаётся за декой, а не за ядром.
"""
import re
from dataclasses import dataclass

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, MID, SURFACE, WHITE

# Слова сравнения, по которым видно, что база — база, а не вторая подпись.
# Перечень закрытый и короткий нарочно: он не пытается понять фразу, он
# ловит кадр, где базы нет ВОВСЕ, — тот случай, который и бывает.
BASE_WORD = re.compile(
    r"против|вместо|при\b|было|базов|сравнен|из\s|от\s|до\s|\bvs\b"
    r"|без\s|с\s+модел|знаменател|исходн|норм[аы]", re.I)

DIGIT = re.compile(r"\d")


@dataclass(frozen=True)
class FigureStyle:
    pad: float = 0.30
    val_hi: float = 96.0
    val_lo: float = 34.0         # ниже величина перестаёт быть «во весь кадр»
    val_ls: float = 1.02
    val_gap: float = 0.10
    rule_w: float = 1.60         # золотая черта под числом
    rule_h: float = 0.075
    rule_gap: float = 0.14
    unit_pt: float = 16.0
    unit_ls: float = 1.16
    unit_gap: float = 0.12
    base_pt: float = 14.0        # пол видимого слоя, см. `floor.py`
    base_ls: float = 1.18
    base_gap: float = 0.10
    note_pt: float = 12.0        # пол видимого слоя, см. `floor.py`
    note_ls: float = 1.14
    note_gap: float = 0.10
    note_italic: bool = True
    max_val_chars: int = 16      # дальше это не число, а фраза
    center: bool = True
    min_h: float = 1.70


DEFAULT = FigureStyle()


def figure_of(sl, st=DEFAULT):
    """Поле `figure` → разобранная величина или None.

    Чужая форма поля не роняет сборку: она называется `[число]`, и кадр
    собирается без фигуры — тот же договор, что у `plates_of`/`scheme_of`."""
    raw = sl.meta.get("figure")
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[число] {sl.sid}: поле `figure` — "
                    f"{type(raw).__name__}, а должно быть value/unit/base")
        return None
    val = str(raw.get("value") or "").strip()
    if not val:
        report.warn(f"[число] {sl.sid}: в `figure` нет `value` — кадру "
                    "одного числа нечего показать")
        return None
    return {"value": val,
            "unit": str(raw.get("unit") or "").strip(),
            "base": str(raw.get("base") or "").strip(),
            "note": str(raw.get("note") or "").strip(),
            "invert": bool(raw.get("invert"))}


def _iw(w, st):
    return max(0.3, w - 2 * st.pad)


def val_size(fig, w, st=DEFAULT):
    """Кегль величины: наибольший, при котором она встаёт В ОДНУ СТРОКУ.

    Одна строка здесь не вкусовое: величина, перенесённая на вторую строку,
    читается как две величины («0,712» и «против») — ровно то, от чего эта
    форма и уводит. Не влезло и на `val_lo` — об этом говорит
    `check_figure`, а кегль остаётся нижним: мера не вправе молча решить,
    что текст кадра надо сократить."""
    iw = _iw(w, st) * metrics.W_SAFE
    f = st.val_hi
    while f > st.val_lo:
        if metrics.text_w(fig["value"], f, True) / 72.0 <= iw:
            break
        f -= 1.0
    return f


def _line_h(size, ls):
    return size * ls * metrics.LH / 72.0 * metrics.SAFE


def figure_h(fig, w, st=DEFAULT):
    """Высота фигуры — она же то, что фигура отнимает у тела кадра."""
    iw = _iw(w, st)
    h = 2 * st.pad
    h += _line_h(val_size(fig, w, st), st.val_ls) + st.val_gap
    h += st.rule_gap + st.rule_h
    for key, pt, ls, gap, it in (
            ("unit", st.unit_pt, st.unit_ls, st.unit_gap, False),
            ("base", st.base_pt, st.base_ls, st.base_gap, False),
            ("note", st.note_pt, st.note_ls, st.note_gap, st.note_italic)):
        if fig[key]:
            h += gap + metrics.est_h(fig[key], pt, iw, ls, False, it)
    return max(st.min_h, h)


def check_figure(sid, fig, w, st=DEFAULT):
    """`[число]`: величина оказалась фразой, база не названа, базы нет в
    содержании. Каждое — про то, что видно на экране, а не про вкус."""
    if not DIGIT.search(fig["value"]):
        report.warn(
            f"[число] {sid}: в значении «{fig['value']}» нет ни одной "
            "цифры — кадр одного числа держит ВЕЛИЧИНУ; словесное "
            "утверждение живёт заголовком и телом")
    if len(fig["value"]) > st.max_val_chars:
        report.warn(
            f"[число] {sid}: значение «{fig['value']}» — {len(fig['value'])} "
            f"знаков (> {st.max_val_chars}): это не одно число, а фраза. "
            "Единица и сравнение идут в `unit` и `base`, иначе кадр "
            "перестаёт быть кадром одного числа")
    f = val_size(fig, w, st)
    need = metrics.text_w(fig["value"], f, True) / 72.0
    if need > _iw(w, st) * metrics.W_SAFE:
        report.warn(
            f"[число] {sid}: значению «{fig['value']}» нужно {need:.2f}\" и "
            f"на {f:.0f} пт при колонке {_iw(w, st):.2f}\" — ниже этого "
            "кегля величина перестаёт быть «во весь кадр». Сокращают "
            "значение, а не кегль")
    if not fig["base"]:
        report.warn(
            f"[число] {sid}: у величины «{fig['value']}» не названа БАЗА "
            "(`base`) — число во весь кадр без базы не интерпретируется: "
            "«–50%» от какого исходного, «0,712» против чего "
            "(CLAUDE.md § «Baseline / Counterfactual Mandate»)")
    elif not (DIGIT.search(fig["base"]) or BASE_WORD.search(fig["base"])):
        report.warn(
            f"[число] {sid}: в базе «{fig['base'][:48]}» нет ни второй "
            "величины, ни слова сравнения — это вторая подпись, а не база. "
            "База называет, ОТ ЧЕГО считается число")


def draw_figure(s, sid, fig, x, y, w, st=DEFAULT, tag=None):
    """Величина во весь кадр: число · золотая черта · единица · база ·
    оговорка. Возвращает занятую высоту."""
    tag = tag or sid
    iw = _iw(w, st)
    h = figure_h(fig, w, st)
    dark = fig["invert"]
    prims.ocean_box(s, x, y, w, h,
                    fill=DEEP if dark else SURFACE,
                    stroke=DEEP if dark else LIGHT,
                    stroke_pt=1.5)
    align = PP_ALIGN.CENTER if st.center else PP_ALIGN.LEFT
    f = val_size(fig, w, st)
    floor.pt(f, tag, "величина кадра")
    vh = _line_h(f, st.val_ls)
    prims.text_box(s, x + st.pad, y + st.pad, iw, vh, fig["value"], size=f,
                   bold=True, color=GOLD if dark else DEEP, align=align,
                   anchor=MSO_ANCHOR.TOP, ls=st.val_ls, tag=f"{tag}/величина")
    cy = y + st.pad + vh + st.val_gap + st.rule_gap
    rx = x + (w - st.rule_w) / 2 if st.center else x + st.pad
    prims.rect(s, rx, cy, st.rule_w, st.rule_h,
               WHITE if dark else GOLD, count="акцент")
    # Золото на кадре есть при любом из двух способов: светлом его несёт
    # черта, перевёрнутом — сама величина. Поэтому отметка одна.
    report.GOLD_SEEN.add(sid)
    cy += st.rule_h
    for key, pt, ls, gap, it, col in (
            ("unit", st.unit_pt, st.unit_ls, st.unit_gap, False,
             WHITE if dark else MID),
            ("base", st.base_pt, st.base_ls, st.base_gap, False,
             WHITE if dark else DEEP),
            ("note", st.note_pt, st.note_ls, st.note_gap, st.note_italic,
             LIGHT if not dark else WHITE)):
        if not fig[key]:
            continue
        floor.pt(pt, tag, {"unit": "единица величины",
                           "base": "база величины",
                           "note": "оговорка величины"}[key])
        hh = metrics.est_h(fig[key], pt, iw, ls, False, it)
        prims.text_box(s, x + st.pad, cy + gap, iw, hh, fig[key], size=pt,
                       bold=(key == "unit"), italic=it, color=col,
                       align=align, ls=ls, tag=f"{tag}/{key}")
        cy += gap + hh
    report.PRIM["одно число"] += 1
    return h
