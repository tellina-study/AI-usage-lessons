# -*- coding: utf-8 -*-
"""ДВЕ ВСТРЕЧНЫЕ СТРЕЛКИ `strelki:` — та же архитектура, развёрнутая в другую
сторону.

Перенос приёма §2.9 из `library/lectures/lec-08/rework-v5/
PERENOS-PRIYOMOV.md`: `media/s11` — широкая стрелка вправо «Генерация: текст
→ шум → изображение» и под ней встречная стрелка влево «Распознавание:
изображение → блоки внимания → оценка». Один рисунок без абзаца утверждает
«та же архитектура внимания, развёрнутая в другую сторону» — то, что иначе
нужно было бы объяснять словом «наоборот».

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ: направление, а не состав и не порядок — для
порядка есть `scheme.py`, для распределения — `fazy.py`. Форма держит РОВНО
ДВЕ стрелки, одну вправо и одну влево: третьей стрелки у встречного движения
не бывает, а одна стрелка — это уже обычная схема.

ЗОЛОТО ЗДЕСЬ — ЗАЛИВКА СТРЕЛКИ ВПРАВО, А НЕ ТЕКСТ (правило перевода §1 того
же файла): `#F0AB00` текстом на светлом даёт 1,99 : 1 при пороге 3,0, а
заливкой с тёмным текстом поверх — 6,85 : 1. Стрелка влево читается второй,
менее нагруженной: заливка `#F4F7FA`, обводка `#1C7293`.

Контракт фронтматтера:

    strelki:
      vpravo: {head: "Генерация", text: "текст → шум → изображение"}
      vlevo:  {head: "Распознавание",
               text: "изображение → блоки внимания → оценка"}
      itog: "та же архитектура внимания, развёрнутая в другую сторону"   # необязательно
"""
from dataclasses import dataclass

from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

from . import floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, SURFACE

TOP_KEYS = {"vpravo", "vlevo", "itog"}
SIDE_KEYS = {"head", "text"}


@dataclass(frozen=True)
class StrelkiStyle:
    pad: float = 0.24                # поле внутри стрелки, со стороны хвоста
    tip: float = 0.60                # резерв под остриё стрелки
    shaft: float = 0.82              # доля высоты, занятая стволом (adj1)
    arrow_h: float = 1.05
    gap: float = 0.24                # просвет между двумя стрелками
    head_pt: float = 16.0
    head_ls: float = 1.08
    text_pt: float = 14.5
    text_lo: float = 12.0            # пол видимого слоя
    text_ls: float = 1.16
    itog_pt: float = 13.0
    itog_lo: float = 12.0            # пол видимого слоя
    itog_ls: float = 1.14
    itog_gap: float = 0.20
    max_lines: int = 2
    min_w: float = 3.2


DEFAULT = StrelkiStyle()


# ── разбор поля ─────────────────────────────────────────────────────


def _side_of(sid, name, raw):
    if raw is None:
        report.warn(f"[стрелки] {sid}: в `strelki` не названа «{name}» — "
                    "форма держит ровно две стрелки, и без одной из них "
                    "это уже не встречное движение")
        return None
    if not isinstance(raw, dict):
        report.warn(f"[стрелки] {sid}: «{name}» — {type(raw).__name__}, а "
                    "должно быть head/text")
        return None
    unknown = sorted(set(raw) - SIDE_KEYS)
    if unknown:
        report.warn(f"[стрелки] {sid}: «{name}» — ключ(и) "
                    f"{' · '.join(unknown)} ядро не читает")
    head = str(raw.get("head") or "").strip()
    text = str(raw.get("text") or "").strip()
    if not head:
        report.warn(f"[стрелки] {sid}: у стрелки «{name}» нет `head` — "
                    "направление без названия ничего не утверждает")
    if not text:
        report.warn(f"[стрелки] {sid}: у стрелки «{name}» нет `text` — "
                    "пустая стрелка это просто геометрия")
    if not head and not text:
        return None
    return {"head": head, "text": text}


def strelki_of(sl, st=DEFAULT):
    """Поле `strelki` → разобранная пара стрелок или None."""
    raw = sl.meta.get("strelki")
    sid = sl.sid
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[стрелки] {sid}: поле `strelki` — "
                    f"{type(raw).__name__}, а должно быть vpravo/vlevo/itog")
        return None
    unknown = sorted(set(raw) - TOP_KEYS)
    if unknown:
        report.warn(f"[стрелки] {sid}: ключ(и) {' · '.join(unknown)} ядро "
                    "не читает, и на кадре он не скажется ничем")
    vp = _side_of(sid, "vpravo", raw.get("vpravo"))
    vl = _side_of(sid, "vlevo", raw.get("vlevo"))
    if vp is None or vl is None:
        return None
    return {"vpravo": vp, "vlevo": vl,
            "itog": str(raw.get("itog") or "").strip()}


# ── мера ────────────────────────────────────────────────────────────


def _longest(text, f):
    return max(text.split(), key=lambda x: metrics.text_w(x, f, True),
               default="")


def text_w(w, st=DEFAULT):
    """Ширина под текст внутри стрелки — одна и та же для обеих: остриё
    забирает своё место ровно с одной стороны, но мера ширины держится
    симметрично, чтобы хвостовая и головная сторона мерились одинаково."""
    return max(0.3, w - st.tip - 2 * st.pad)


def _runs(side, st):
    out = []
    if side["head"]:
        out.append({"text": side["head"], "size": st.head_pt, "bold": True,
                    "color": DEEP})
    if side["text"]:
        if side["head"]:
            out.append({"text": "", "size": st.text_pt, "newpara": True,
                        "space_before": 3.0})
        out.append({"text": side["text"], "size": st.text_pt, "color": DEEP})
    return out


def strelki_h(d, w, st=DEFAULT):
    """Высота формы — она же то, что форма отнимает у тела кадра."""
    h = 2 * st.arrow_h + st.gap
    if d["itog"]:
        iw = max(0.3, w)
        h += st.itog_gap + metrics.est_h(d["itog"], st.itog_pt, iw,
                                         st.itog_ls, True)
    return h


# ── сторож ──────────────────────────────────────────────────────────


def check_strelki(sid, d, w, st=DEFAULT):
    """`[стрелки]`: ширина тесная · слово шире хода · текст растянулся в
    абзац · итог растянулся в абзац."""
    if w < st.min_w:
        report.warn(f"[стрелки] {sid}: ширина {w:.2f}\" (< {st.min_w:.2f}\") "
                    "— тексту внутри стрелки будет тесно")
    tw = text_w(w, st)
    for name, side in (("vpravo", d["vpravo"]), ("vlevo", d["vlevo"])):
        if side["head"]:
            long = _longest(side["head"], st.head_pt)
            if long and metrics.text_w(long, st.head_pt, True) > tw * 72.0:
                report.warn(
                    f"[стрелки] {sid}: слову «{long}» в «{name}» не хватает "
                    f"ширины {tw:.2f}\" — перенос порвёт его посреди корня")
        if side["text"]:
            ln = metrics.n_lines(side["text"], st.text_pt, tw)
            if ln > st.max_lines:
                report.warn(
                    f"[стрелки] {sid}: текст стрелки «{name}» занимает "
                    f"{ln} строки (> {st.max_lines}) при {tw:.2f}\" — "
                    "стрелка не держит абзац, это одна-две строки хода")
    if d["itog"]:
        ln = metrics.n_lines(d["itog"], st.itog_pt, w, True)
        if ln > 2:
            report.warn(f"[стрелки] {sid}: итог занимает {ln} строки "
                        "(> 2) — это уже разбор, не вывод")


# ── рисование ───────────────────────────────────────────────────────


def _arrow(s, shape, x, y, w, h, fill, *, stroke=None, stroke_pt=1.5,
           adj1, adj2):
    shp = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w),
                             Inches(h))
    try:
        shp.adjustments[0] = adj1
        shp.adjustments[1] = adj2
    except Exception:
        pass
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(stroke_pt)
    prims.no_shadow(shp)
    report.PRIM["стрелка"] += 1
    return shp


def draw_strelki(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Стрелка вправо (золото) над стрелкой влево (светлая, с обводкой).
    Возвращает занятую высоту."""
    tag = tag or sid
    top = y
    adj2 = max(0.08, min(0.40, st.tip / w))
    tw = text_w(w, st)

    _arrow(s, MSO_SHAPE.RIGHT_ARROW, x, y, w, st.arrow_h, GOLD,
           adj1=st.shaft, adj2=adj2)
    report.GOLD_SEEN.add(sid)
    runs_r = _runs(d["vpravo"], st)
    th_r = metrics.runs_h(runs_r, tw, st.text_ls)
    floor.pt(st.text_pt, tag, "текст стрелки вправо")
    prims.text_runs(s, x + st.pad, y + (st.arrow_h - th_r) / 2, tw, th_r,
                    runs_r, ls=st.text_ls, align=PP_ALIGN.LEFT,
                    anchor=MSO_ANCHOR.MIDDLE, tag=f"{tag}/вправо", quiet=True)
    y += st.arrow_h + st.gap

    _arrow(s, MSO_SHAPE.LEFT_ARROW, x, y, w, st.arrow_h, SURFACE,
           stroke=LIGHT, adj1=st.shaft, adj2=adj2)
    runs_l = _runs(d["vlevo"], st)
    th_l = metrics.runs_h(runs_l, tw, st.text_ls)
    floor.pt(st.text_pt, tag, "текст стрелки влево")
    prims.text_runs(s, x + st.tip + st.pad, y + (st.arrow_h - th_l) / 2, tw,
                    th_l, runs_l, ls=st.text_ls, align=PP_ALIGN.LEFT,
                    anchor=MSO_ANCHOR.MIDDLE, tag=f"{tag}/влево", quiet=True)
    y += st.arrow_h

    if d["itog"]:
        y += st.itog_gap
        floor.pt(st.itog_pt, tag, "итог встречных стрелок")
        ih = metrics.est_h(d["itog"], st.itog_pt, w, st.itog_ls, True)
        prims.text_box(s, x, y, w, ih, d["itog"], size=st.itog_pt, bold=True,
                       color=DEEP, align=PP_ALIGN.CENTER, ls=st.itog_ls,
                       tag=f"{tag}/итог")
        y += ih
    report.PRIM["встречные стрелки"] += 1
    return y - top
