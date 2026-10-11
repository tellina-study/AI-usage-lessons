#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборщик деки Лекции 7 (каркас). Issue #229.

Источник истины видимого текста — файлы `slides/*.md`. В сборщике литералов
видимого текста НЕТ ни одного: всё, что попадает на экран, пришло из файла
кадра. Служебные поля фронтматтера (`assertion`, `timing_min`, `in_bucket`,
`method_steps`, `form`, `media_needed`, `media_note`, `status`) на экран не
выводятся ни одной строкой — их место здесь, в отчёте сборки, и в `deck.yaml`.

Что сборщик умеет и почему именно это:

  * палитра Ocean Gradient, золото не реже раза на кадр (проверяется);
  * мотив «океанская скруглённая коробка» на содержательных кадрах, на
    обложке его нет — мотив принадлежит содержанию;
  * ПОЛОСА ПЛАШЕК `blocks` — числа отдельными блочками «было · стало · к
    чему привело», а не внутри абзаца;
  * СХЕМА-КОНВЕЙЕР `scheme` — порядок работы, не длиннее четырёх шагов в
    ряду (больше — предупреждение, это прямой запрет владельца);
  * ДВА СТОЛБЦА `columns` — ТОЛЬКО под противопоставление «что получается /
    что не получается»; перечни кейсов идут буллитами в теле;
  * настоящие гиперссылки (`run.hyperlink.address`) в подвале и в заметках;
    URL в теле слайда — блокирующее предупреждение `[ссылка]`.

БЛОКИРУЮЩИЕ предупреждения — те, по которым видно физический предел кадра:

  [высота]  текст не укладывается в свою рамку и наедет сам на себя
  [ширина]  слово шире рамки — LibreOffice рвёт его посреди корня
  [кегль]   блок набран на дне лестницы кеглей
  [ссылка]  URL в видимом теле слайда (место ссылки — подвал)

Каждое из четырёх прогнано на нарочно сломанном входе: `--selftest`. Прогон,
показавший ноль, ничего не значит, пока не доказано, что проверка умеет
находить, — поэтому самопроверка не опция, а часть сдачи.

Запуск:
  python3 build_lec07.py                 — только PPTX (по умолчанию)
  python3 build_lec07.py --selftest      — прогон проверок на сломанном входе
  python3 build_lec07.py --render        — ещё PDF и PNG, частями, с таймаутом
  python3 build_lec07.py --only s01,s11  — собрать только эти кадры

Рендер убран из обычного прогона не для удобства: `soffice --convert-to pdf`
на деках этого курса дважды вешал машину на часы
(`notes/mcp-limitations.md` [#223-6], [#229-2]). Предупреждения считаются при
сборке PPTX и от рендера не зависят.
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

import yaml
from PIL import ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

HERE = Path(__file__).resolve().parent
SLIDES_DIR = HERE / "slides"
LEC_ROOT = HERE.parent.parent                      # library/lectures/lec-07
OUT = HERE / "lec-07-karkas.pptx"
PDF = HERE / "lec-07-karkas.pdf"
SNAPS = HERE / "snapshots"
LO_ENV = Path("/home/harness/.local/lo-portable-env.sh")

# ════════════════════════════════════════════════════════════════════
# палитра и шрифт
# ════════════════════════════════════════════════════════════════════
DEEP = RGBColor(0x21, 0x29, 0x5C)      # основной текст, заголовки
MID = RGBColor(0x06, 0x5A, 0x82)       # подзаголовки, акценты
LIGHT = RGBColor(0x1C, 0x72, 0x93)     # обводки, подвал, второстепенное
TEAL = RGBColor(0x02, 0x80, 0x90)      # вторая серия, разнообразие
SURFACE = RGBColor(0xF4, 0xF7, 0xFA)   # поверхность мотива
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GOLD = RGBColor(0xF0, 0xAB, 0x00)      # акцент, не реже раза на кадр
OUTLINE = RGBColor(0xD9, 0xE2, 0xEC)

FONT = "Arial"                          # в PPTX рендерится Liberation Sans
SLIDE_W, SLIDE_H = 13.333, 7.5

_TTF_DIR = Path("/home/harness/.local/libreoffice-portable/share/fonts/truetype")
_TTF = {False: _TTF_DIR / "LiberationSans-Regular.ttf",
        True: _TTF_DIR / "LiberationSans-Bold.ttf"}
_FCACHE = {}
LH = 1.19          # натуральная высота строки Liberation Sans, в кеглях
SAFE = 1.04        # запас по высоте на расхождение разметки с измерением
W_SAFE = 0.97      # запас по ширине: на пограничной строке метрика и
                   # LibreOffice расходятся ровно на строку

WARNINGS = []
BLOCKING = ("[высота]", "[ширина]", "[кегль]", "[ссылка]")
LINKS = Counter()
PRIM = Counter()
GOLD_SEEN = set()
PLACEHOLDERS = Counter()

# ════════════════════════════════════════════════════════════════════
# измерение текста настоящими метриками шрифта
# ════════════════════════════════════════════════════════════════════


def _font(bold):
    if bold not in _FCACHE:
        _FCACHE[bold] = ImageFont.truetype(str(_TTF[bold]), 200)
    return _FCACHE[bold]


def text_w(text, size, bold=False):
    """Ширина строки в пунктах."""
    return _font(bold).getlength(text) / 200.0 * size


def longest_word_w(text, size, bold=False):
    """Ширина самого длинного неразрывного куска: перенос идёт по пробелам,
    и слово шире места LibreOffice рвёт посреди корня."""
    words = re.split(r"\s+", text.strip())
    return max((text_w(w, size, bold) for w in words if w), default=0.0)


def n_lines(text, size, w_in, bold=False):
    maxw = w_in * 72.0
    words = text.split()
    if not words:
        return 1
    lines, cur = 1, words[0]
    for wd in words[1:]:
        if text_w(cur + " " + wd, size, bold) <= maxw:
            cur += " " + wd
        else:
            lines, cur = lines + 1, wd
    return lines


def est_h(text, size, w_in, ls=1.18, bold=False):
    """Высота текстового блока в дюймах."""
    if w_in <= 0:
        return 0.0
    rows = sum(n_lines(p, size, w_in, bold) for p in text.split("\n"))
    return rows * size * ls * LH / 72.0 * SAFE


def check_width(text, size, w_in, tag, bold=False):
    """[ширина] — слово шире рамки. Проверка отдельная от высоты: высокий
    блок ужимается кеглем, а слово, которое не влезает по ширине, кеглем
    почти не лечится и рвётся на экране посреди корня."""
    lw = longest_word_w(text, size, bold) / 72.0
    if lw > w_in * W_SAFE:
        WARNINGS.append(
            f"[ширина] {tag}: слово шире рамки — {lw:.2f}\" против "
            f"{w_in:.2f}\" при кегле {size:.1f}  «{text[:40]}…»")
        return False
    return True


def fit_size(text, w, h, *, hi=17.0, lo=11.5, floor=8.5, ls=1.18,
             bold=False, tag=""):
    """Крупнейший кегль, при котором текст укладывается в рамку w × h.

    Два разных исхода и два разных предупреждения. Не влезло даже на полу —
    `[высота]`: текст физически наедет сам на себя. Влезло, но ниже рабочего
    предела — `[кегль]`: блок набран на дне лестницы, и это предел плотности
    кадра, а не раскладки."""
    f = round(hi * 2) / 2
    while f >= floor:
        if est_h(text, f, w, ls, bold) <= h:
            if f < lo:
                WARNINGS.append(
                    f"[кегль] {tag}: тело ужалось до {f:.1f} пт "
                    f"(рабочий предел {lo:.1f}) — предел плотности кадра")
            return f
        f -= 0.5
    WARNINGS.append(
        f"[высота] {tag}: не укладывается даже при {floor:.1f} пт — "
        f"{est_h(text, floor, w, ls, bold):.2f}\" против {h:.2f}\"")
    return floor


# ════════════════════════════════════════════════════════════════════
# примитивы
# ════════════════════════════════════════════════════════════════════


def _no_shadow(shp):
    spPr = shp.fill._xPr
    for tag in ("effectLst", "effectRef"):
        for el in spPr.findall(
                f"{{http://schemas.openxmlformats.org/drawingml/2006/main}}{tag}"):
            spPr.remove(el)
    try:
        shp.shadow.inherit = False
    except Exception:
        pass


def rect(s, x, y, w, h, fill, *, stroke=None, stroke_pt=1.0):
    shp = s.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                             Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(stroke_pt)
    _no_shadow(shp)
    PRIM["плашка"] += 1
    return shp


def ocean_box(s, x, y, w, h, *, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5):
    """Мотив деки: океанская скруглённая коробка. Радиус 12 пт."""
    shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                             Inches(x), Inches(y), Inches(w), Inches(h))
    try:
        shp.adjustments[0] = max(0.03, min(0.25,
                                 (12.0 / 72.0) / max(min(w, h) / 2.0, 0.4)))
    except Exception:
        pass
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.color.rgb = stroke
    shp.line.width = Pt(stroke_pt)
    _no_shadow(shp)
    PRIM["мотив"] += 1
    return shp


def arrow(s, x, y, w, h, color=LIGHT):
    shp = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,
                             Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    _no_shadow(shp)
    PRIM["стрелка"] += 1
    return shp


def text_box(s, x, y, w, h, text, *, size=16, bold=False, italic=False,
             color=DEEP, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             ls=1.18, tag=""):
    e = est_h(text, size, w, ls, bold)
    if e > h + 0.02:
        WARNINGS.append(
            f"[высота] {tag}: рамка {w:.2f}×{h:.2f}\" кегль {size:.1f} — "
            f"оценка {e:.2f}\" > {h:.2f}\"  «{text[:40]}…»")
    check_width(text, size, w, tag, bold)
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = Inches(0.0)
    tf.margin_top = tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for i, line in enumerate(text.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = ls
        r = p.add_run()
        r.text = line
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
    return tb


def runs_paras(runs):
    """Прогоны → абзацы (текст, кегль, полужирность) ровно так, как их потом
    сложит `text_runs`. Отдельная функция нужна затем, чтобы высоту считала
    и подбирала кегль одна и та же арифметика: мера по «плоскому» тексту без
    полужирных кусков давала блок ниже надписи, и надпись вылезала за рамку."""
    paras, cur, sz, bd = [], "", 0.0, False
    for c in runs:
        if c.get("newpara") and (cur or sz):
            paras.append((cur, sz or 16, bd))
            cur, sz, bd = "", 0.0, False
        cur += c["text"]
        sz = max(sz, c.get("size", 16))
        bd = bd or bool(c.get("bold"))
    paras.append((cur, sz or 16, bd))
    return paras


def runs_h(runs, w, ls=1.18):
    return sum(est_h(t, z, w, ls, b) for t, z, b in runs_paras(runs))


def fit_runs(runs, w, h, *, hi=1.0, lo=0.72, floor=0.58, ls=1.26, tag=""):
    """Крупнейший МАСШТАБ кеглей прогона, при котором он укладывается в
    рамку. Масштаб, а не кегль: внутри прогона кегли разные — заголовок
    блока, тело, подпись, — и сбивать их в один нельзя, иначе иерархия
    кадра исчезает."""
    k = hi
    base = [r.get("size", 15.0) for r in runs]
    while k >= floor - 1e-9:
        for r, b0 in zip(runs, base):
            r["size"] = max(8.5, round(b0 * k, 1))
        if runs_h(runs, w, ls) <= h:
            if k < lo:
                WARNINGS.append(
                    f"[кегль] {tag}: прогон ужат до {k:.2f} от рабочего "
                    f"кегля — предел плотности кадра")
            return k
        k -= 0.02
    for r, b0 in zip(runs, base):
        r["size"] = max(8.5, round(b0 * floor, 1))
    WARNINGS.append(
        f"[высота] {tag}: не укладывается даже при масштабе {floor:.2f} — "
        f"{runs_h(runs, w, ls):.2f}\" против {h:.2f}\"")
    return floor


def text_runs(s, x, y, w, h, runs, *, ls=1.18, align=PP_ALIGN.LEFT,
              anchor=MSO_ANCHOR.TOP, tag=""):
    """runs — список словарей: text, size, bold, italic, color, url,
    newpara. Высота считается по абзацам, собранным из этих же словарей."""
    paras = runs_paras(runs)
    e = sum(est_h(t, z, w, ls, b) for t, z, b in paras)
    if e > h + 0.02:
        WARNINGS.append(
            f"[высота] {tag}: прогон {w:.2f}×{h:.2f}\" — оценка {e:.2f}\" > "
            f"{h:.2f}\"  «{paras[0][0][:40]}…»")
    for t, z, bd2 in paras:
        check_width(t, z, w, tag, bd2)
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = Inches(0.0)
    tf.margin_top = tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = ls
    for cfg in runs:
        if cfg.get("newpara"):
            p = tf.add_paragraph()
            p.alignment = cfg.get("align", align)
            p.line_spacing = ls
            if cfg.get("space_before"):
                p.space_before = Pt(cfg["space_before"])
        r = p.add_run()
        r.text = cfg["text"]
        r.font.name = FONT
        r.font.size = Pt(cfg.get("size", 16))
        r.font.bold = cfg.get("bold", False)
        r.font.italic = cfg.get("italic", False)
        r.font.color.rgb = cfg.get("color", DEEP)
        if cfg.get("url"):
            r.hyperlink.address = cfg["url"]
            r.font.underline = True
            LINKS["подвал"] += 1
    return tb


# ════════════════════════════════════════════════════════════════════
# ссылки: настоящие, а не текст адреса
# ════════════════════════════════════════════════════════════════════
_URL = re.compile(r"(?:https?://|www\.)[^\s<>\"«»'()\[\]]+", re.I)
_MDLINK = re.compile(r"\[([^\]\n]+)\]\((https?://[^)\s]+)\)")
_TAIL = ".,;:!?…»\"'"


def _abs_url(u):
    u = u.rstrip(_TAIL)
    return u if u.lower().startswith(("http://", "https://")) else "https://" + u


def short_url(u, lim=46):
    t = re.sub(r"^https?://", "", u).rstrip("/")
    t = re.sub(r"^www\.", "", t)
    return t if len(t) <= lim else t[:lim - 1] + "…"


def _bare(text):
    out, pos = [], 0
    for m in _URL.finditer(text):
        raw = m.group(0).rstrip(_TAIL)
        if m.start() > pos:
            out.append((text[pos:m.start()], None))
        out.append((raw, _abs_url(raw)))
        pos = m.start() + len(raw)
    if pos < len(text):
        out.append((text[pos:], None))
    return out


def link_parts(text):
    """Строка → [(видимое, адрес или None), …]. Это разбор ЗАМЕТОК: адрес
    остаётся виден, потому что заметки читают как текст."""
    out, pos = [], 0
    for m in _MDLINK.finditer(text):
        if m.start() > pos:
            out += _bare(text[pos:m.start()])
        out.append((m.group(1), _abs_url(m.group(2))))
        pos = m.end()
    if pos < len(text):
        out += _bare(text[pos:])
    return [p for p in out if p[0]]


def _seg_parts(seg):
    """Одна работа из поля `source` → прогоны подвала. Голый адрес из
    видимой строки УБИРАЕТСЯ: ссылкой становится название работы перед
    ним. Названия нет — якорем идёт сокращённый адрес."""
    if _MDLINK.search(seg):
        return link_parts(seg)
    urls = [_abs_url(m.group(0)) for m in _URL.finditer(seg)]
    if not urls:
        return [(seg, None)]
    vis = re.sub(r"\s{2,}", " ", _URL.sub("", seg))
    vis = re.sub(r"\s*[—–-]\s*$", "", vis).strip(" ,;:·—–")
    if not vis:
        return [(short_url(urls[0]), urls[0])]
    out = [(vis, urls[0])]
    for u in urls[1:]:
        out += [(" · ", None), (short_url(u, 30), u)]
    return out


def source_parts(src):
    out = []
    for i, seg in enumerate(str(src).split(" · ")):
        if i:
            out.append((" · ", None))
        out += _seg_parts(seg)
    return [p for p in out if p[0]]


def notes_with_links(slide, text):
    """Заметки лектора с ЖИВЫМИ ссылками. `.text = …` кладёт заметки одной
    строкой, а у строки нет прогонов, на которые можно поставить ссылку."""
    tf = slide.notes_slide.notes_text_frame
    tf.text = ""
    n = 0
    for i, ln in enumerate((text or "").split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        for seg, url in (link_parts(ln) or [(ln, None)]):
            r = p.add_run()
            r.text = seg
            if url:
                r.hyperlink.address = url
                r.font.underline = True
                r.font.color.rgb = MID
                n += 1
    LINKS["заметки"] += n
    return n


# ════════════════════════════════════════════════════════════════════
# разбор файла кадра
# ════════════════════════════════════════════════════════════════════
_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITAL = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)")
_PH = re.compile(r"\{\{([^}]*)\}\}")


class Slide:
    __slots__ = ("sid", "path", "meta", "body", "notes")


def inline_runs(line, size, color=DEEP):
    """**полужирный** и *курсив* внутри строки — прогонами, не разметкой."""
    out, pos = [], 0
    toks = sorted([(m.start(), m.end(), "b", m.group(1)) for m in _BOLD.finditer(line)] +
                  [(m.start(), m.end(), "i", m.group(1)) for m in _ITAL.finditer(line)])
    keep, last = [], -1
    for t in toks:                       # вложенные совпадения не берём
        if t[0] >= last:
            keep.append(t)
            last = t[1]
    for st, en, kind, inner in keep:
        if st > pos:
            out.append({"text": line[pos:st], "size": size, "color": color})
        out.append({"text": inner, "size": size, "color": color,
                    "bold": kind == "b", "italic": kind == "i"})
        pos = en
    if pos < len(line):
        out.append({"text": line[pos:], "size": size, "color": color})
    return out or [{"text": line, "size": size, "color": color}]


def read_slide(path):
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.S)
    if not m:
        WARNINGS.append(f"[файл] {path.name}: нет фронтматтера")
        return None
    sl = Slide()
    sl.path = path
    try:
        sl.meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        WARNINGS.append(f"[файл] {path.name}: фронтматтер не читается — {e}")
        return None
    sl.sid = str(sl.meta.get("id") or path.stem.split("-")[0])
    rest = m.group(2)
    vis = re.search(r"##\s*Видимый текст слайда\s*\n(.*?)(?=\n##\s|\Z)", rest, re.S)
    nts = re.search(r"##\s*Заметки лектора\s*\n(.*?)(?=\n##\s|\Z)", rest, re.S)
    sl.body = (vis.group(1) if vis else "").strip()
    sl.notes = (nts.group(1) if nts else "").strip()
    if not sl.notes:
        WARNINGS.append(f"[заметки] {sl.sid}: раздела «Заметки лектора» нет")
    PLACEHOLDERS[sl.sid] = len(_PH.findall(sl.body))
    # [ссылка] — URL в видимом теле. Место ссылки — подвал.
    for u in _URL.finditer(sl.body):
        WARNINGS.append(
            f"[ссылка] {sl.sid}: адрес «{short_url(u.group(0), 34)}» стоит в "
            "теле слайда — место ссылки в подвале, поле `source`")
    return sl


def body_lines(sl):
    """Тело → список (вид, текст). Вид: head · bullet · cap · para."""
    out = []
    for blk in re.split(r"\n\s*\n", sl.body):
        blk = blk.strip()
        if not blk:
            continue
        if blk.startswith("#"):
            out.append(("head", blk.lstrip("# ").strip()))
        elif all(l.strip().startswith(("- ", "* ", "• ")) or not l.strip()
                 for l in blk.split("\n")) and blk.lstrip().startswith(("- ", "* ", "• ")):
            for l in blk.split("\n"):
                if l.strip():
                    out.append(("bullet", "• " + l.strip()[2:].strip()))
        elif _ITAL.fullmatch(blk) and "\n" not in blk:
            out.append(("cap", _ITAL.fullmatch(blk).group(1)))
        else:
            out.append(("para", blk.replace("\n", " ")))
    return out


# ════════════════════════════════════════════════════════════════════
# раскладка
# ════════════════════════════════════════════════════════════════════
MX = 0.55                              # поле слева и справа
FULL_W = SLIDE_W - 2 * MX              # 12,23"
TITLE_Y = 0.40
BODY_TOP = 1.46
FOOT_Y = 6.94
BODY_BOT = FOOT_Y - 0.12
MEDIA_W = 4.30
COL_GAP = 0.34
GAP = 0.20

PLATE_MAX = 4                          # плашек в ряд; больше — второй ряд
PLATE_GAP, PLATE_PAD = 0.18, 0.15
SCHEME_MAX_STEPS = 4                   # владелец: длинных конвейеров не надо
SCHEME_MAX_ROWS = 3

CONTENT_TYPES = {"case", "norm", "comparison", "summary", "map", "question"}


def new_deck():
    p = Presentation()
    p.slide_width = Inches(SLIDE_W)
    p.slide_height = Inches(SLIDE_H)
    return p


def blank(p):
    return p.slides.add_slide(p.slide_layouts[6])


def gold_tick(s, x, y, sid):
    rect(s, x, y, 1.05, 0.055, GOLD)
    GOLD_SEEN.add(sid)


def heading(s, sl, color=DEEP, size=27.0):
    t = str(sl.meta.get("title") or "").strip()
    if not t:
        WARNINGS.append(f"[заголовок] {sl.sid}: поле `title` пусто")
        return BODY_TOP
    sz = fit_size(t, FULL_W, 0.92, hi=size, lo=19.0, floor=15.0, bold=True,
                  ls=1.08, tag=f"{sl.sid}/заголовок")
    text_box(s, MX, TITLE_Y, FULL_W, 0.92, t, size=sz, bold=True, color=color,
             ls=1.08, tag=f"{sl.sid}/заголовок")
    gold_tick(s, MX, TITLE_Y + 0.98, sl.sid)
    return BODY_TOP


# ── полоса плашек ───────────────────────────────────────────────────


def plates_of(sl):
    raw = sl.meta.get("blocks")
    if raw in (None, "", [], {}):
        return []
    if not isinstance(raw, list):
        WARNINGS.append(f"[плашки] {sl.sid}: поле `blocks` — "
                        f"{type(raw).__name__}, а должно быть списком")
        return []
    out = []
    for i, it in enumerate(raw, 1):
        if not isinstance(it, dict):
            WARNINGS.append(f"[плашки] {sl.sid}: плашка {i} не пара label/value")
            continue
        p = {"label": str(it.get("label") or "").strip(),
             "value": "" if it.get("value") is None else str(it["value"]).strip(),
             "note": str(it.get("note") or "").strip(),
             "key": bool(it.get("key"))}
        if not (p["label"] or p["value"]):
            WARNINGS.append(f"[плашки] {sl.sid}: плашка {i} пуста")
            continue
        out.append(p)
    if len(out) > PLATE_MAX:
        WARNINGS.append(
            f"[плашки] {sl.sid}: плашек {len(out)} — в ряд встаёт не больше "
            f"{PLATE_MAX}, остальные уходят во второй ряд и забирают у тела "
            "ещё одну высоту полосы")
    return out


def _gold_idx(plates):
    keyed = {i for i, p in enumerate(plates) if p["key"]}
    if keyed:
        return keyed
    nums = [i for i, p in enumerate(plates) if re.search(r"\d", p["value"])]
    return {nums[-1]} if nums else ({len(plates) - 1} if plates else set())


BL_LAB_PT, BL_NOTE_PT = 10.0, 10.5
BL_VAL_HI, BL_VAL_LO, BL_VAL_FLOOR = 23.0, 13.0, 10.0


def _plate_metrics(p, iw):
    """Кегль значения и ВЫСОТЫ трёх строк плашки — ровно те, которыми плашка
    потом рисуется.

    Мерится то же, что рисуется, и это не формальность: подпись рисуется
    ПРОПИСНЫМИ и полужирной, значение — полужирным. Мера по строчным и
    светлым давала плашку ниже надписи, и надпись наезжала на оговорку снизу.

    Строк у значения столько, сколько ему НУЖНО, а не сколько положено: число
    укладывается в две, а словесная плашка цены ошибки — в три, и зажатая по
    пределу она наезжает на соседку. Предел нужен решению «какой кегль», а не
    высоте рамки."""
    iw = max(0.3, iw)
    lab = p["label"].upper()
    hl = (est_h(lab, BL_LAB_PT, iw, 1.10, True) + 0.05) if lab else 0.0
    rows_max = 2 if re.search(r"\d", p["value"]) else 3
    vs = BL_VAL_HI
    while vs > BL_VAL_FLOOR:
        fits_w = longest_word_w(p["value"], vs, True) / 72.0 <= iw * W_SAFE
        if fits_w and n_lines(p["value"], vs, iw * W_SAFE, True) <= rows_max:
            break
        vs -= 0.5
    hv = est_h(p["value"], vs, iw, 1.08, True) + 0.04
    hn = est_h(p["note"], BL_NOTE_PT, iw, 1.12) if p["note"] else 0.0
    return vs, hl, hv, hn, PLATE_PAD * 2 + hl + hv + hn


def _plate_rows(plates, w):
    rows = [plates[i:i + PLATE_MAX] for i in range(0, len(plates), PLATE_MAX)]
    out = []
    for row in rows:
        pw = (w - PLATE_GAP * (len(row) - 1)) / len(row)
        iw = pw - 2 * PLATE_PAD
        met = [_plate_metrics(p, iw) for p in row]
        out.append((row, pw, iw, met, max(m[4] for m in met)))
    return out


def plates_h(plates, w):
    rows = _plate_rows(plates, w)
    return (sum(r[4] for r in rows) + PLATE_GAP * (len(rows) - 1)
            if rows else 0.0), rows


def draw_plates(s, sl, plates, x, y, w):
    total, rows = plates_h(plates, w)
    gold = _gold_idx(plates)
    k, yy = 0, y
    for row, pw, iw, met, rh in rows:
        xx = x
        for p, (vs, hl, hv, hn, _) in zip(row, met):
            is_gold = k in gold
            ocean_box(s, xx, yy, pw, rh,
                      fill=WHITE if is_gold else SURFACE,
                      stroke=GOLD if is_gold else LIGHT,
                      stroke_pt=2.0 if is_gold else 1.2)
            if is_gold:
                GOLD_SEEN.add(sl.sid)
            cy = yy + PLATE_PAD
            if hl:
                text_box(s, xx + PLATE_PAD, cy, iw, hl, p["label"].upper(),
                         size=BL_LAB_PT, bold=True, color=LIGHT, ls=1.10,
                         tag=f"{sl.sid}/плашка-подпись")
                cy += hl
            text_box(s, xx + PLATE_PAD, cy, iw, hv, p["value"], size=vs,
                     bold=True, color=GOLD if is_gold else DEEP, ls=1.08,
                     tag=f"{sl.sid}/плашка-значение")
            cy += hv
            if hn:
                text_box(s, xx + PLATE_PAD, cy, iw, hn, p["note"],
                         size=BL_NOTE_PT, italic=True, color=LIGHT, ls=1.12,
                         tag=f"{sl.sid}/плашка-оговорка")
            xx += pw + PLATE_GAP
            k += 1
        yy += rh + PLATE_GAP
    return total


# ── схема-конвейер ──────────────────────────────────────────────────


def scheme_of(sl):
    raw = sl.meta.get("scheme")
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict) or not isinstance(raw.get("rows"), list):
        WARNINGS.append(f"[схема] {sl.sid}: поле `scheme` должно быть "
                        "словарём с ключом `rows`")
        return None
    rows = []
    for i, r in enumerate(raw["rows"], 1):
        if not isinstance(r, dict) or not isinstance(r.get("steps"), list):
            WARNINGS.append(f"[схема] {sl.sid}: ряд {i} без списка `steps`")
            continue
        steps = [str(x).strip() for x in r["steps"] if str(x).strip()]
        if len(steps) > SCHEME_MAX_STEPS:
            WARNINGS.append(
                f"[схема] {sl.sid}: в ряду {i} шагов {len(steps)} — в ряд "
                f"встаёт не больше {SCHEME_MAX_STEPS}; длинный конвейер "
                "запрещён, ряд надо разбить")
            steps = steps[:SCHEME_MAX_STEPS]
        rows.append({"label": str(r.get("label") or "").strip(), "steps": steps})
    if len(rows) > SCHEME_MAX_ROWS:
        WARNINGS.append(f"[схема] {sl.sid}: рядов {len(rows)} — больше "
                        f"{SCHEME_MAX_ROWS} схема перестаёт читаться")
    return {"caption": str(raw.get("caption") or "").strip(),
            "arrows": raw.get("arrows", True) is not False,
            "rows": rows} if rows else None


SCH_LAB_W, SCH_ARR = 1.55, 0.30


def scheme_h(sch, w):
    h = 0.0
    for r in sch["rows"]:
        n = len(r["steps"])
        gap = SCH_ARR if sch["arrows"] else 0.16
        bw = (w - (SCH_LAB_W if r["label"] else 0.0) - gap * (n - 1)) / n
        iw = max(0.3, bw - 0.18)
        rh = max(est_h(st, 11.5, iw, 1.12) for st in r["steps"]) + 0.26
        h += max(0.50, rh) + 0.16
    if sch["caption"]:
        h += est_h(sch["caption"], 10.5, w, 1.12) + 0.04
    return h


def draw_scheme(s, sl, sch, x, y, w):
    yy = y
    for r in sch["rows"]:
        n = len(r["steps"])
        lab = SCH_LAB_W if r["label"] else 0.0
        gap = SCH_ARR if sch["arrows"] else 0.16
        bw = (w - lab - gap * (n - 1)) / n
        iw = max(0.3, bw - 0.18)
        rh = max(0.50, max(est_h(st, 11.5, iw, 1.12) for st in r["steps"]) + 0.26)
        if r["label"]:
            text_box(s, x, yy + 0.06, SCH_LAB_W - 0.14, rh, r["label"],
                     size=11.5, bold=True, color=LIGHT, ls=1.12,
                     tag=f"{sl.sid}/схема-подпись")
        xx = x + lab
        for j, st in enumerate(r["steps"]):
            ocean_box(s, xx, yy, bw, rh, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
            text_box(s, xx + 0.09, yy + 0.09, iw, rh - 0.18, st, size=11.5,
                     color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                     ls=1.12, tag=f"{sl.sid}/схема-шаг")
            if j < n - 1 and sch["arrows"]:
                arrow(s, xx + bw + 0.05, yy + rh / 2 - 0.075, SCH_ARR - 0.10,
                      0.15, TEAL)
            xx += bw + gap
        yy += rh + 0.16
    if sch["caption"]:
        hc = est_h(sch["caption"], 10.5, w, 1.12)
        text_box(s, x, yy, w, hc, sch["caption"], size=10.5, italic=True,
                 color=LIGHT, ls=1.12, tag=f"{sl.sid}/схема-подпись-низ")
    return scheme_h(sch, w)


# ── два столбца: только противопоставление ──────────────────────────


def columns_of(sl):
    raw = sl.meta.get("columns")
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict) or "left" not in raw or "right" not in raw:
        WARNINGS.append(f"[столбцы] {sl.sid}: поле `columns` должно иметь "
                        "`left` и `right`")
        return None
    cols = []
    for side in ("left", "right"):
        c = raw[side]
        if not isinstance(c, dict):
            WARNINGS.append(f"[столбцы] {sl.sid}: `{side}` не словарь")
            return None
        cols.append({"head": str(c.get("head") or "").strip(),
                     "items": [str(i).strip() for i in (c.get("items") or [])
                               if str(i).strip()]})
    if sl.meta.get("type") != "comparison":
        WARNINGS.append(
            f"[столбцы] {sl.sid}: два столбца объявлены на кадре типа "
            f"«{sl.meta.get('type')}» — они идут ТОЛЬКО под противопоставление "
            "«что получается / что не получается», тип кадра `comparison`")
    return cols


def draw_columns(s, sl, cols, x, y, w, h):
    cw = (w - COL_GAP) / 2
    for i, c in enumerate(cols):
        xx = x + i * (cw + COL_GAP)
        ocean_box(s, xx, y, cw, h, fill=SURFACE if i == 0 else WHITE,
                  stroke=LIGHT if i == 0 else TEAL)
        iw = cw - 0.36
        yy = y + 0.17
        if c["head"]:
            hh = est_h(c["head"], 14.0, iw, 1.12)
            text_box(s, xx + 0.18, yy, iw, hh, c["head"], size=14.0, bold=True,
                     color=MID if i == 0 else TEAL, ls=1.12,
                     tag=f"{sl.sid}/столбец-шапка")
            yy += hh + 0.12
        body = "\n".join("• " + it for it in c["items"])
        if body:
            avail = y + h - 0.17 - yy
            sz = fit_size(body, iw, avail, hi=14.5, lo=11.0, floor=9.0,
                          ls=1.26, tag=f"{sl.sid}/столбец-{i + 1}")
            text_box(s, xx + 0.18, yy, iw, avail, body, size=sz, color=DEEP,
                     ls=1.26, tag=f"{sl.sid}/столбец-{i + 1}")


# ── кадр и подвал ───────────────────────────────────────────────────


def media_path(sl):
    m = str(sl.meta.get("media") or "").strip()
    if not m:
        return None
    p = (LEC_ROOT / m) if not os.path.isabs(m) else Path(m)
    if not p.exists():
        WARNINGS.append(f"[кадр] {sl.sid}: файла нет — {m}")
        return None
    return p


def draw_media(s, sl, p, x, y, w, h):
    ocean_box(s, x, y, w, h)
    try:
        from PIL import Image
        with Image.open(p) as im:
            ar = im.width / max(1, im.height)
    except Exception as e:
        WARNINGS.append(f"[кадр] {sl.sid}: {p.name} — {e}")
        return
    iw, ih = w - 0.3, h - 0.3
    if iw / ih > ar:
        iw = ih * ar
    else:
        ih = iw / ar
    s.shapes.add_picture(str(p), Inches(x + (w - iw) / 2),
                         Inches(y + (h - ih) / 2), Inches(iw), Inches(ih))
    PRIM["кадр"] += 1


def footer(s, sl):
    src = str(sl.meta.get("source") or "").strip()
    if not src or src == "—":
        return
    runs = []
    for i, (vis, url) in enumerate(source_parts(src)):
        runs.append({"text": vis, "size": 11.0, "italic": True,
                     "color": MID if url else LIGHT, "url": url})
    if not runs:
        return
    flat = "".join(r["text"] for r in runs)
    if est_h(flat, 11.0, FULL_W, 1.12) > 0.46:
        WARNINGS.append(f"[подвал] {sl.sid}: источник не влезает в две "
                        f"строки подвала — {len(flat)} знаков")
    text_runs(s, MX, FOOT_Y, FULL_W, 0.50, runs, ls=1.12,
              tag=f"{sl.sid}/подвал")


# ── типы кадров ─────────────────────────────────────────────────────


def check_prims(sl, kind):
    """Примитив объявлен на кадре, который его не рисует. Молчать нельзя:
    сессия раздела написала бы полосу плашек и не узнала, что её нет."""
    for f, name in (("blocks", "плашки"), ("scheme", "схема"),
                    ("columns", "столбцы")):
        if sl.meta.get(f):
            WARNINGS.append(
                f"[{name}] {sl.sid}: поле `{f}` объявлено на кадре типа "
                f"«{kind}» — оно рисуется только на содержательных кадрах")


def cover(p, sl):
    s = blank(p)
    rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE)
    check_prims(sl, "cover")
    img = media_path(sl)
    tw = 7.10 if img else FULL_W
    if img:
        draw_media(s, sl, img, MX + tw + 0.40, 0.60,
                   SLIDE_W - MX * 2 - tw - 0.40, SLIDE_H - 1.60)
    lines = body_lines(sl)
    runs = []
    for i, (kind, t) in enumerate(lines):
        sz = {"head": 34.0, "cap": 12.5}.get(kind, 17.0)
        for r in inline_runs(t, sz, DEEP if kind != "cap" else LIGHT):
            r.setdefault("italic", kind == "cap")
            r["newpara"] = r["newpara"] if "newpara" in r else False
            runs.append(r)
        if runs:
            runs[-1]["_end"] = True
        if i < len(lines) - 1:
            runs.append({"text": "", "size": sz, "newpara": True,
                         "space_before": 12})
    if runs:
        text_runs(s, MX, 1.70, tw, 4.20, runs, ls=1.22,
                  anchor=MSO_ANCHOR.TOP, tag=f"{sl.sid}/обложка")
    rect(s, MX, 1.28, 1.60, 0.07, GOLD)
    GOLD_SEEN.add(sl.sid)
    footer(s, sl)
    return s


def divider(p, sl):
    s = blank(p)
    rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE)
    rect(s, 0, 0, 0.17, SLIDE_H, MID)
    check_prims(sl, "divider")
    img = media_path(sl)
    tw = 7.30 if img else FULL_W
    if img:
        draw_media(s, sl, img, MX + tw + 0.40, 1.00,
                   SLIDE_W - MX * 2 - tw - 0.40, SLIDE_H - 2.40)
    lines = body_lines(sl)
    y = 1.05
    for kind, t in lines:
        if kind == "head":
            sz = fit_size(t, tw, 1.05, hi=30.0, lo=20.0, floor=16.0, bold=True,
                          ls=1.10, tag=f"{sl.sid}/дивайдер-имя")
            h = est_h(t, sz, tw, 1.10, True)
            text_box(s, MX + 0.22, y, tw, h, t, size=sz, bold=True, color=DEEP,
                     ls=1.10, tag=f"{sl.sid}/дивайдер-имя")
            y += h + 0.10
            rect(s, MX + 0.22, y, 1.30, 0.065, GOLD)
            GOLD_SEEN.add(sl.sid)
            y += 0.30
        elif kind == "cap":
            h = est_h(t, 12.0, tw, 1.14)
            text_box(s, MX + 0.22, y, tw, h, t, size=12.0, italic=True,
                     color=LIGHT, ls=1.14, tag=f"{sl.sid}/дивайдер-подпись")
            y += h + 0.14
        else:
            runs = inline_runs(t, 15.5, DEEP)
            h = est_h(t, 15.5, tw - 0.22, 1.24)
            text_runs(s, MX + 0.22, y, tw - 0.22, h + 0.04, runs, ls=1.24,
                      tag=f"{sl.sid}/дивайдер-тело")
            y += h + 0.18
        if y > FOOT_Y - 0.2:
            WARNINGS.append(f"[высота] {sl.sid}/дивайдер: текст дошёл до "
                            f"подвала — {y:.2f}\" при пределе {FOOT_Y:.2f}\"")
            break
    footer(s, sl)
    return s


def content(p, sl):
    s = blank(p)
    rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE)
    y = heading(s, sl)
    img = media_path(sl)
    body_w = FULL_W - (MEDIA_W + COL_GAP if img else 0.0)
    if img:
        draw_media(s, sl, img, MX + body_w + COL_GAP, y, MEDIA_W,
                   min(3.40, BODY_BOT - y))

    plates = plates_of(sl) if sl.meta.get("type") in CONTENT_TYPES else []
    if plates and sl.meta.get("type") not in CONTENT_TYPES:
        plates = []
    if plates:
        y += draw_plates(s, sl, plates, MX, y, body_w) + GAP

    sch = scheme_of(sl)
    if sch:
        y += draw_scheme(s, sl, sch, MX, y, body_w) + GAP

    cols = columns_of(sl)
    avail = BODY_BOT - y
    if cols:
        # Столбцы берут не фиксированную высоту, а ОСТАТОК за вычетом того,
        # что нужно телу: иначе кадр с противопоставлением И телом выдавал
        # телу 0,75" и ломался предупреждением там, где места хватало.
        need = 0.0
        for kind, t in body_lines(sl):
            need += est_h(t, {"head": 15.0, "cap": 11.0}.get(kind, 13.0),
                          body_w - 0.08, 1.26, kind == "head") + 0.08
        ch = max(1.55, min(avail - (need + GAP if need else 0.0), 3.40))
        draw_columns(s, sl, cols, MX, y, body_w, ch)
        y += ch + GAP
        avail = BODY_BOT - y

    lines = body_lines(sl)
    if lines and avail > 0.35:
        runs, flat = [], []
        first = True
        for kind, t in lines:
            sz = {"head": 20.0, "cap": 12.0, "bullet": 15.0}.get(kind, 15.0)
            col = LIGHT if kind == "cap" else DEEP
            if not first:
                runs.append({"text": "", "size": sz, "newpara": True,
                             "space_before": 7})
            first = False
            for r in inline_runs(t, sz, col):
                if kind == "cap":
                    r["italic"] = True
                if kind == "head":
                    r["bold"] = True
                runs.append(r)
            flat.append(t)
        fit_runs(runs, body_w - 0.08, avail, ls=1.26, tag=f"{sl.sid}/тело")
        ocean_box(s, MX - 0.14, y - 0.10, body_w + 0.28,
                  min(avail + 0.18, BODY_BOT - y + 0.10))
        text_runs(s, MX + 0.04, y, body_w - 0.08, avail, runs, ls=1.26,
                  tag=f"{sl.sid}/тело")
    elif lines:
        WARNINGS.append(f"[высота] {sl.sid}/тело: места под тело не осталось "
                        f"({avail:.2f}\") — примитивы съели кадр")
    footer(s, sl)
    return s


BUILDERS = {"cover": cover, "divider": divider}


def build_one(p, sl):
    kind = str(sl.meta.get("type") or "case").strip()
    s = BUILDERS.get(kind, content)(p, sl)
    notes_with_links(s, sl.notes)
    if sl.sid not in GOLD_SEEN:
        WARNINGS.append(f"[золото] {sl.sid}: золотого акцента на кадре нет")
    return s


# ════════════════════════════════════════════════════════════════════
# сборка
# ════════════════════════════════════════════════════════════════════


def order_key(name):
    m = re.match(r"^s(\d+)([a-z]*)", name)
    return (int(m.group(1)), m.group(2)) if m else (9999, name)


def all_slides(only=None):
    files = sorted((f for f in SLIDES_DIR.glob("s*.md")),
                   key=lambda f: order_key(f.name))
    if only:
        want = {x.strip() for x in only.split(",") if x.strip()}
        files = [f for f in files if f.name.split("-")[0] in want]
    return files


def build(only=None, out=OUT, slides_dir=None):
    global SLIDES_DIR
    if slides_dir:
        SLIDES_DIR = slides_dir
    p = new_deck()
    n = 0
    for f in all_slides(only):
        sl = read_slide(f)
        if sl is None:
            continue
        build_one(p, sl)
        n += 1
    p.save(str(out))
    return n


def report(n):
    print(f"\nсобрано кадров: {n}  →  {OUT.name}")
    print(f"примитивы: " + " · ".join(f"{k} {v}" for k, v in sorted(PRIM.items())))
    print(f"ссылки: " + (" · ".join(f"{k} {v}" for k, v in sorted(LINKS.items()))
                         or "ни одной"))
    tot_ph = sum(PLACEHOLDERS.values())
    with_ph = sum(1 for v in PLACEHOLDERS.values() if v)
    print(f"заглушки чисел: {tot_ph} на {with_ph} кадрах из {n}")
    blk = [w for w in WARNINGS if w.startswith(BLOCKING)]
    oth = [w for w in WARNINGS if not w.startswith(BLOCKING)]
    if blk:
        print(f"\nБЛОКИРУЮЩИЕ предупреждения ({len(blk)}):")
        for w in blk:
            print("  " + w)
    if oth:
        print(f"\nпрочие предупреждения ({len(oth)}):")
        for w in oth:
            print("  " + w)
    if not WARNINGS:
        print("\nпредупреждений нет")
    return len(blk)


def verify_links(path=OUT):
    """`r:id` в XML сохранённого файла. Самоотчёт не принимается: ссылка
    считается поставленной только тогда, когда отношение лежит в пакете."""
    import zipfile
    from lxml import etree
    A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
    body, notes, targets = 0, 0, 0
    with zipfile.ZipFile(path) as z:
        for nm in z.namelist():
            if not (nm.startswith("ppt/slides/slide") or
                    nm.startswith("ppt/notesSlides/notesSlide")) or \
                    not nm.endswith(".xml"):
                continue
            root = etree.fromstring(z.read(nm))
            k = sum(1 for e in root.iter(f"{A}hlinkClick") if e.get(f"{R}id"))
            if nm.startswith("ppt/slides/"):
                body += k
            else:
                notes += k
        for nm in z.namelist():
            if ".rels" in nm and ("slides/_rels" in nm or "notesSlides/_rels" in nm):
                root = etree.fromstring(z.read(nm))
                targets += sum(1 for e in root.iter()
                               if e.get("Type", "").endswith("/hyperlink"))
    print(f"\nгиперссылки в XML: подвал {body} · заметки {notes} · "
          f"отношений в пакете {targets}")
    return body + notes, targets


# ════════════════════════════════════════════════════════════════════
# САМОПРОВЕРКА: каждое блокирующее предупреждение на сломанном входе
# ════════════════════════════════════════════════════════════════════
_CLEAN = """---
id: s01
local_id: ч-01
section: "проба"
type: case
title: "Короткий заголовок пробы"
source: "Работа, автор — https://example.org/a"
blocks:
  - {label: "Было", value: "100"}
  - {label: "Стало", value: "40", key: true}
scheme:
  caption: "подпись"
  rows:
    - {label: "Ряд", steps: ["шаг один", "шаг два", "шаг три"]}
timing_min: 0.8
---

## Видимый текст слайда

Короткий абзац тела, который заведомо укладывается в рамку и ничего не ломает.

## Заметки лектора

Заметка пробы со ссылкой [работа](https://example.org/a) внутри строки.
"""

_BROKEN = {
    "[высота]": ("s90", """---
id: s90
type: case
title: "Проба на высоту"
source: "—"
---

## Видимый текст слайда

""" + ("Очень длинный абзац, который заведомо не укладывается в тело кадра ни "
       "при каком кегле, потому что его объём превышает физическую площадь "
       "рамки в несколько раз. " * 90) + """

## Заметки лектора

проба
"""),
    "[ширина]": ("s91", """---
id: s91
type: case
title: "Проба на ширину"
source: "—"
blocks:
  - {label: "Подпись", value: "НЕРАЗРЫВНОЕСЛОВОКОТОРОЕШИРЕЛЮБОЙПЛАШКИИРВЁТСЯПОСРЕДИКОРНЯ"}
  - {label: "Вторая", value: "11"}
  - {label: "Третья", value: "12"}
  - {label: "Четвёртая", value: "13"}
---

## Видимый текст слайда

Короткое тело.

## Заметки лектора

проба
"""),
    "[кегль]": ("s92", """---
id: s92
type: case
title: "Проба на кегль"
source: "—"
blocks:
  - {label: "Было", value: "100"}
  - {label: "Стало", value: "40"}
scheme:
  rows:
    - {label: "Ряд", steps: ["шаг один", "шаг два", "шаг три", "шаг четыре"]}
    - {label: "Второй", steps: ["шаг один", "шаг два", "шаг три"]}
    - {label: "Третий", steps: ["шаг один", "шаг два"]}
---

## Видимый текст слайда

""" + ("Абзац тела такого объёма, что он влезает лишь ниже рабочего предела "
       "кегля, и это ровно тот случай, который обязан называться "
       "предупреждением сборки, а не молча ужиматься. " * 11) + """

## Заметки лектора

проба
"""),
    "[ссылка]": ("s93", """---
id: s93
type: case
title: "Проба на ссылку в теле"
source: "—"
---

## Видимый текст слайда

Адрес стоит прямо в теле слайда: https://example.org/v-tele — так нельзя.

## Заметки лектора

проба
"""),
    "[схема]": ("s94", """---
id: s94
type: case
title: "Проба на длинный конвейер"
source: "—"
scheme:
  rows:
    - {label: "Ряд", steps: ["раз", "два", "три", "четыре", "пять", "шесть"]}
---

## Видимый текст слайда

Короткое тело.

## Заметки лектора

проба
"""),
    "[плашки]": ("s95", """---
id: s95
type: case
title: "Проба на шестую плашку"
source: "—"
blocks:
  - {label: "Один", value: "1"}
  - {label: "Два", value: "2"}
  - {label: "Три", value: "3"}
  - {label: "Четыре", value: "4"}
  - {label: "Пять", value: "5"}
  - {label: "Шесть", value: "6"}
---

## Видимый текст слайда

Короткое тело.

## Заметки лектора

проба
"""),
    "[столбцы]": ("s96", """---
id: s96
type: summary
title: "Проба на два столбца не под противопоставление"
source: "—"
columns:
  left:  {head: "Перечень один", items: ["кейс", "кейс"]}
  right: {head: "Перечень два", items: ["кейс", "кейс"]}
---

## Видимый текст слайда

Короткое тело.

## Заметки лектора

проба
"""),
}


def selftest():
    """Прогон каждой проверки на нарочно сломанном входе.

    Проверка, показавшая ноль, ничего не значит, пока не доказано, что она
    умеет находить. Поэтому здесь два прогона на каждое предупреждение:
    чистый кадр (обязан молчать) и сломанный (обязан сработать)."""
    global WARNINGS
    tmp = Path(tempfile.mkdtemp(prefix="lec07-selftest-"))
    ok, bad = [], []

    seq = [0]

    def run(files, name="probe"):
        global WARNINGS
        WARNINGS = []
        seq[0] += 1
        d = tmp / f"d{seq[0]}"
        d.mkdir()
        for nm, txt in files:
            (d / nm).write_text(txt, encoding="utf-8")
        build(out=tmp / f"{name}.pptx", slides_dir=d)
        return list(WARNINGS)

    base = run([("s01-clean.md", _CLEAN)], name="clean")
    print("── САМОПРОВЕРКА ─────────────────────────────────────────────")
    print(f"чистый кадр: предупреждений {len(base)}"
          + (" — " + "; ".join(base) if base else " (молчит, как и должен)"))
    if base:
        bad.append("чистый кадр выдал предупреждение — проверка шумит")

    for tag, (sid, txt) in _BROKEN.items():
        w = run([(f"{sid}-broken.md", txt)])
        hit = [x for x in w if x.startswith(tag)]
        mark = "ЛОВИТ" if hit else "НЕ ЛОВИТ"
        print(f"{tag:<11} на сломанном входе: {mark}"
              + (f"  →  {hit[0][:96]}" if hit else ""))
        (ok if hit else bad).append(tag)

    # Гиперссылки проверяются на ЧИСТОМ кадре: у него один адрес в подвале и
    # один в заметках. Самоотчёт не принимается — считаются `r:id` в XML.
    n, targets = verify_links(tmp / "clean.pptx")
    if n < 2 or targets < 2:
        bad.append("[ссылка-живая] в XML чистого кадра не нашлось двух "
                   f"отношений гиперссылки (подвал+заметки): {n}/{targets}")
    else:
        ok.append("[ссылка-живая]")
        print("[ссылка-живая] на чистом кадре: ЛОВИТ  →  подвал и заметки "
              "дали настоящие `r:id` в пакете")
    print("─────────────────────────────────────────────────────────────")
    print(f"проверок ловит: {len(ok)} из {len(_BROKEN) + 1}")
    if bad:
        print("НЕ ДОКАЗАНО: " + ", ".join(bad))
        return 1
    print("все проверки доказаны на сломанном входе")
    return 0


# ════════════════════════════════════════════════════════════════════
# рендер (по требованию, с таймаутом)
# ════════════════════════════════════════════════════════════════════


def render():
    SNAPS.mkdir(exist_ok=True)
    env = f". {LO_ENV} && " if LO_ENV.exists() else ""
    cmds = [
        f'{env}cd "{HERE}" && soffice --headless --convert-to pdf '
        f'--outdir "{HERE}" "{OUT.name}"',
        f'cd "{HERE}" && pdftoppm -r 110 -png "{PDF.name}" "{SNAPS}/k"',
    ]
    for c in cmds:
        try:
            r = subprocess.run(["bash", "-lc", c], timeout=115,
                               capture_output=True, text=True)
            if r.returncode:
                print(f"рендер: код {r.returncode}\n{r.stderr[-600:]}")
                return 1
        except subprocess.TimeoutExpired:
            print("рендер: таймаут 115 с — снято, см. notes/mcp-limitations.md "
                  "[#223-6]")
            return 1
    print(f"рендер готов: {PDF.name}, снимки в {SNAPS.name}/")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--render", action="store_true")
    ap.add_argument("--only")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    n = build(only=a.only)
    blk = report(n)
    verify_links()
    if a.render:
        render()
    return 0


if __name__ == "__main__":
    sys.exit(main())
