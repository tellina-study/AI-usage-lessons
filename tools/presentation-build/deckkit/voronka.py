# -*- coding: utf-8 -*-
"""ВОРОНКА `voronka:` — отношение входа к выходу и место, где стоит затор.

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ: во сколько раз вход больше выхода, и на каком
ярусе теряется разница. Два утверждения, и второе важнее первого: отношение
можно сказать словами («на одну годную уходит тридцать»), а вот ГДЕ именно
уходит — словами говорится абзацем, а рисуется одним ярусом.

ОТКУДА ОНА ВЗЯТА. `PERENOS-PRIYOMOV.md` §2.4: в образцах (`image/s06`,
`media/s08`) воронка от широкого верха к узкому низу, рядом ярусы подписей
«Генерация (низкая цена, огромный объём)» → «Отбор (узкое горлышко)» →
«Результат и брак», вход подписан «70 000 сгенерированных клипов», выход —
«1 готовый ролик».

ПОЧЕМУ УЗКОЕ МЕСТО — СТОРОЖ, А НЕ ПОЖЕЛАНИЕ. Воронка без названного затора
рисует ровно то, что и так знают: сверху много, снизу мало. Вся работа формы
в том, чтобы сказать, КАКОЙ ярус съедает объём, — и если этого нет, форма
красива и пуста. Поэтому `check_voronka` отказывает, когда ни один ярус не
назван узким местом, и это тот же род сторожа, что `base` у `figure:`.

ЧЕМ НАША ВОРОНКА ОТЛИЧАЕТСЯ ОТ ОБРАЗЦА, И ПОЧЕМУ ИМЕННО ТАК. В образце это
гладкая трапеция. У нас — СТУПЕНЧАТАЯ: ярус за ярусом, каждый уже
предыдущего. Причина не в красоте, а в примитивах: рисовать позволено только
тем, что есть в `prims.py` (прямоугольник, скруглённый прямоугольник, чип,
надпись), трапеции и произвольной фигуры там нет, а заводить их ради одной
формы значило бы тронуть общий модуль, которым в этот же час пользуются
соседние нити. Ступень при этом не хуже: у гладкой трапеции ярус — это
полоса, границу которой назначает подпись, у ступенчатой — настоящая
фигура, к которой подпись привязана ростом.

ЧЕГО ЭТА ФОРМА НЕ ДЕЛАЕТ. Не рисует пустых рамок: у каждого яруса есть имя
внутри ступени и разбор справа — четыре молчащих концентрических коробки это
не схема, а орнамент. Не красит текст золотом: золото здесь — ЗАЛИВКА плашек
входа и выхода с тёмным текстом поверх (6,85 : 1), потому что золотой текст
на белом даёт 1,99 при пороге 3,0 (`contrast.py`, правило перевода §1).

Контракт фронтматтера:

    voronka:
      vhod:  {value: "70 000", text: "сгенерированных клипов за 30 дней"}
      vyhod: {value: "1", text: "готовый ролик"}
      caption: "…"                      # необязательна
      yarusy:
        - head: "Генерация"
          text: "цена попытки — доли цента; 30–100 генераций на одну итоговую"
        - head: "Отбор — узкое место"
          text: "около получаса человеческого просмотра на иллюстрацию"
"""
import re
from dataclasses import dataclass

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import floor, metrics, prims, report
from .theme import (DEEP, GOLD, GOLD_TINT, LIGHT, MID, SURFACE)

NEEDS_ROWS = False

TOP_KEYS = {"vhod", "vyhod", "yarusy", "caption"}
END_KEYS = {"value", "text"}
TIER_KEYS = {"head", "text"}

# Чем называют затор. Перечень закрытый: сторож ловит отсутствие НАЗВАННОГО
# узкого места, а не отсутствие конкретного слова, поэтому синонимы, которые
# в деке реально пишут, перечислены здесь все.
BOTTLENECK = re.compile(r"узк\w*\s+мест|узкое\s+горл|горлышк|затор|бутылочн"
                        r"|предел пропуск", re.I)
DIGIT = re.compile(r"\d")


@dataclass(frozen=True)
class VoronkaStyle:
    funnel_w: float = 5.00      # колонка самой воронки
    col_gap: float = 0.40       # воронка — ярусы подписей
    narrow: float = 0.30        # во сколько раз сужается последняя ступень
    band_min_h: float = 0.74
    band_gap: float = 0.09
    head_pt: float = 15.0
    head_ls: float = 1.08
    text_pt: float = 13.5
    text_ls: float = 1.16
    end_h: float = 0.74         # высота плашки входа и выхода
    end_w: float = 2.05         # ширина плашки
    end_pt_hi: float = 30.0
    end_pt_lo: float = 17.0
    end_txt_pt: float = 14.0
    end_gap: float = 0.20
    pad: float = 0.12           # поле внутри ступени
    cap_pt: float = 12.0        # пол видимого слоя, см. `floor.py`
    cap_ls: float = 1.14
    cap_gap: float = 0.10
    max_tiers: int = 3          # четвёртый ярус — отказ
    min_tiers: int = 2
    stroke_pt: float = 1.5
    key_stroke_pt: float = 2.5  # обводка яруса-затора


DEFAULT = VoronkaStyle()


def _end_of(sid, name, raw):
    if raw is None:
        report.warn(
            f"[воронка] {sid}: не задан «{name}» — воронка утверждает "
            "ОТНОШЕНИЕ входа к выходу, и без одного из концов утверждать "
            "ей нечего")
        return None
    if not isinstance(raw, dict):
        raw = {"value": raw}
    unknown = set(raw) - END_KEYS
    if unknown:
        report.warn(f"[воронка] {sid}: у «{name}» ключи "
                    f"{', '.join(sorted(unknown))} ядро не читает")
    val = str(raw.get("value") or "").strip()
    if not val:
        report.warn(f"[воронка] {sid}: у «{name}» нет `value` — плашке "
                    "конца воронки нечего показать")
        return None
    return {"value": val, "text": str(raw.get("text") or "").strip()}


def voronka_of(sl, st=DEFAULT):
    """Поле `voronka` кадра → разобранная форма или None."""
    return parse(sl.sid, sl.meta.get("voronka"), None, st)


def parse(sid, raw, rows=None, st=DEFAULT):
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[воронка] {sid}: поле `voronka` — "
                    f"{type(raw).__name__}, а должно быть vhod/vyhod/yarusy")
        return None
    unknown = set(raw) - TOP_KEYS
    if unknown:
        report.warn(f"[воронка] {sid}: ключи {', '.join(sorted(unknown))} "
                    "ядро не читает — молчащий ключ хуже отсутствующего")
    yy = raw.get("yarusy")
    if not isinstance(yy, list) or not yy:
        report.warn(f"[воронка] {sid}: у формы `voronka` нет `yarusy` — "
                    "ступени и есть воронка")
        return None
    tiers = []
    for i, t in enumerate(yy, 1):
        if not isinstance(t, dict):
            t = {"head": str(t)}
        unknown = set(t) - TIER_KEYS
        if unknown:
            report.warn(f"[воронка] {sid}: ярус {i} — ключи "
                        f"{', '.join(sorted(unknown))} ядро не читает")
        head = str(t.get("head") or "").strip()
        if not head:
            report.warn(
                f"[воронка] {sid}: у яруса {i} нет `head` — ступень без "
                "имени это пустая рамка, а пустая рамка ничего не "
                "утверждает")
        tiers.append({"head": head, "text": str(t.get("text") or "").strip()})
    vh = _end_of(sid, "vhod", raw.get("vhod"))
    vy = _end_of(sid, "vyhod", raw.get("vyhod"))
    if vh is None or vy is None:
        return None
    return {"kind": "voronka", "vhod": vh, "vyhod": vy, "yarusy": tiers,
            "caption": str(raw.get("caption") or "").strip()}


# ── геометрия ───────────────────────────────────────────────────────


def key_tier(d):
    """Номер яруса-затора (0-based) или None. Ищется и в имени, и в
    разборе: «Отбор — узкое место» и «Отбор · здесь горлышко» одинаково
    называют затор."""
    for i, t in enumerate(d["yarusy"]):
        if BOTTLENECK.search(t["head"]) or BOTTLENECK.search(t["text"]):
            return i
    return None


def band_w(i, n, st=DEFAULT):
    """Ширина ступени: от полной сверху до `narrow` доли внизу."""
    if n < 2:
        return st.funnel_w
    k = i / (n - 1)
    return st.funnel_w * (1.0 - (1.0 - st.narrow) * k)


def text_w_of(w, st=DEFAULT):
    return max(1.2, w - st.funnel_w - st.col_gap)


def band_h(d, i, w, st=DEFAULT):
    """Высота яруса: по тому, что в ступени и что в подписи справа, — одна
    высота на оба, иначе «выровнены по своим уровням» держится на удаче."""
    t = d["yarusy"][i]
    inner = max(0.6, band_w(i, len(d["yarusy"]), st) - 2 * st.pad)
    h_head = metrics.est_h(t["head"], st.head_pt, inner, st.head_ls, True) \
        if t["head"] else 0.0
    tw = text_w_of(w, st)
    h_right = metrics.est_h(t["head"], st.head_pt, tw, st.head_ls, True) \
        if t["head"] else 0.0
    if t["text"]:
        h_right += 0.06 + metrics.est_h(t["text"], st.text_pt, tw,
                                        st.text_ls)
    return max(st.band_min_h, h_head + 2 * st.pad, h_right)


def end_h(d, key, w, st=DEFAULT):
    """Высота полосы входа или выхода: плашка и подпись рядом с ней."""
    e = d[key]
    tw = max(1.0, w - st.end_w - st.end_gap)
    h = metrics.est_h(e["text"], st.end_txt_pt, tw, 1.14) if e["text"] else 0.0
    return max(st.end_h, h)


def voronka_h(d, w, st=DEFAULT):
    """Высота формы — она же то, что форма отнимает у тела кадра."""
    n = len(d["yarusy"])
    h = end_h(d, "vhod", w, st) + st.end_gap
    h += sum(band_h(d, i, w, st) for i in range(n)) + st.band_gap * (n - 1)
    h += st.end_gap + end_h(d, "vyhod", w, st)
    if d["caption"]:
        h += st.cap_gap + metrics.est_h(d["caption"], st.cap_pt, w,
                                        st.cap_ls, False, True)
    return h


# ── сторож ──────────────────────────────────────────────────────────


def check_voronka(sid, d, w, st=DEFAULT):
    """`[воронка]`: узкое место не названо · ярусов меньше двух · четвёртый
    ярус · в конце воронки нет числа · ступень уже своего имени.

    «Нет входа/выхода» и «ярус без имени» сюда не попали нарочно: их уже
    назвал разбор, и повторять значило бы считать один дефект дважды."""
    if key_tier(d) is None:
        report.warn(
            f"[воронка] {sid}: ни один ярус не назван УЗКИМ МЕСТОМ — а в нём "
            "весь смысл формы: «сверху много, снизу мало» зал знает и без "
            "рисунка, работа воронки в том, чтобы сказать, какой ярус "
            "съедает разницу. Назовите затор в `head` яруса")
    n = len(d["yarusy"])
    if n < st.min_tiers:
        report.warn(
            f"[воронка] {sid}: ярус один — сужения не видно, а именно оно "
            "здесь и утверждается. Один ярус это плашка, а не воронка")
    if n > st.max_tiers:
        report.warn(
            f"[воронка] {sid}: ярусов {n} (> {st.max_tiers}) — ступени "
            "мельчают, нижняя становится полоской, и отношение входа к "
            "выходу перестаёт читаться. Соседние ярусы сворачивают в один")
    for key, name in (("vhod", "вход"), ("vyhod", "выход")):
        if not DIGIT.search(d[key]["value"]):
            report.warn(
                f"[воронка] {sid}: у «{name}» значение «{d[key]['value']}» "
                "без единой цифры — воронка утверждает ОТНОШЕНИЕ, а "
                "отношение словами («много» к «мало») не читается")
    for i, t in enumerate(d["yarusy"]):
        inner = band_w(i, n, st) - 2 * st.pad
        need = metrics.longest_word_w(t["head"], st.head_pt, True) / 72.0
        if t["head"] and need > inner:
            report.warn(
                f"[воронка] {sid}: имя яруса «{t['head']}» просит "
                f"{need:.2f}\" одним словом, а ступень {i + 1} шириной "
                f"{inner:.2f}\" — слово разорвётся посреди корня. Нижние "
                "ступени узкие по построению, имя для них берут короче")


# ── рисование ───────────────────────────────────────────────────────


def _end_row(s, sid, d, key, x, y, w, st, tag, name):
    """Плашка конца воронки: число золотой заливкой, тёмным текстом, и
    подпись рядом. Возвращает высоту полосы."""
    e = d[key]
    h = end_h(d, key, w, st)
    px = x + (st.funnel_w - st.end_w) / 2
    sz = metrics.fit_size(e["value"], st.end_w - 0.20, st.end_h - 0.10,
                          hi=st.end_pt_hi, lo=st.end_pt_lo,
                          floor=st.end_pt_lo, bold=True, ls=1.02,
                          tag=f"{tag}/{name}")
    prims.rect(s, px, y + (h - st.end_h) / 2, st.end_w, st.end_h, GOLD,
               radius=True, count="плашка")
    report.GOLD_SEEN.add(sid)
    floor.pt(sz, tag, f"число {name}а воронки")
    prims.text_box(s, px + 0.10, y + (h - st.end_h) / 2, st.end_w - 0.20,
                   st.end_h, e["value"], size=sz, bold=True, color=DEEP,
                   align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, ls=1.02,
                   tag=f"{tag}/{name}", quiet=True)
    if e["text"]:
        tx = x + st.funnel_w + st.col_gap
        tw = max(1.0, w - st.funnel_w - st.col_gap)
        floor.pt(st.end_txt_pt, tag, f"подпись {name}а воронки")
        prims.text_box(s, tx, y, tw, h, e["text"], size=st.end_txt_pt,
                       color=DEEP, anchor=MSO_ANCHOR.MIDDLE, ls=1.14,
                       tag=f"{tag}/{name}-подпись")
    return h


def draw_voronka(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Вход · ступени с подписями справа · выход. Возвращает высоту."""
    tag = tag or sid
    top = y
    n = len(d["yarusy"])
    key = key_tier(d)
    y += _end_row(s, sid, d, "vhod", x, y, w, st, tag, "вход") + st.end_gap
    tw = text_w_of(w, st)
    tx = x + st.funnel_w + st.col_gap
    for i, t in enumerate(d["yarusy"]):
        bh = band_h(d, i, w, st)
        bw = band_w(i, n, st)
        bx = x + (st.funnel_w - bw) / 2
        hot = (i == key)
        prims.rect(s, bx, y, bw, bh, GOLD_TINT if hot else SURFACE,
                   stroke=MID, stroke_pt=st.key_stroke_pt if hot
                   else st.stroke_pt, count="ступень")
        if hot:
            report.GOLD_SEEN.add(sid)
        if t["head"]:
            floor.pt(st.head_pt, tag, "имя яруса воронки")
            hh = metrics.est_h(t["head"], st.head_pt, bw - 2 * st.pad,
                               st.head_ls, True)
            prims.text_box(s, bx + st.pad, y + (bh - hh) / 2,
                           bw - 2 * st.pad, hh, t["head"], size=st.head_pt,
                           bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                           anchor=MSO_ANCHOR.MIDDLE, ls=st.head_ls,
                           tag=f"{tag}/ярус{i + 1}")
        # Подпись справа выровнена по СВОЕМУ ярусу — та же верхняя граница
        # и та же высота, что у ступени. Это и есть «по уровням»: подпись,
        # поставленная по своему тексту, уезжает от ступени на второй.
        runs = []
        if t["head"]:
            runs.append({"text": t["head"], "size": st.head_pt, "bold": True,
                         "color": DEEP})
        if t["text"]:
            runs.append({"text": t["text"], "size": st.text_pt,
                         "color": DEEP, "newpara": bool(runs),
                         "space_before": 4, "ls": st.text_ls})
        if runs:
            floor.pt(st.text_pt, tag, "разбор яруса воронки")
            prims.text_runs(s, tx, y, tw, bh, runs, ls=st.text_ls,
                            anchor=MSO_ANCHOR.MIDDLE,
                            tag=f"{tag}/ярус{i + 1}-разбор")
        y += bh + (st.band_gap if i < n - 1 else 0.0)
    y += st.end_gap
    y += _end_row(s, sid, d, "vyhod", x, y, w, st, tag, "выход")
    if d["caption"]:
        floor.pt(st.cap_pt, tag, "подпись формы")
        ch = metrics.est_h(d["caption"], st.cap_pt, w, st.cap_ls, False, True)
        prims.text_box(s, x, y + st.cap_gap, w, ch, d["caption"],
                       size=st.cap_pt, italic=True, color=LIGHT,
                       ls=st.cap_ls, tag=f"{tag}/подпись")
        y += st.cap_gap + ch
    report.PRIM["воронка"] += 1
    return y - top


# ── общий договор формы ─────────────────────────────────────────────


def height(d, w):
    return voronka_h(d, w)


def check(sid, d, w):
    return check_voronka(sid, d, w)


def draw(s, sid, d, x, y, w, tag=None):
    return draw_voronka(s, sid, d, x, y, w, tag=tag)
