#!/usr/bin/env python3
"""
Data-driven renderer for case-centric seminar decks (sem-03, sem-04),
visual language matched to Семинар 2: flat Ocean rounded boxes, schema
pipelines with arrows, positive/negative example cards, chips, gold
callouts. No timing / no methodology / no "pivot"/"new input" meta-labels
in visible body.

One spec per seminar -> deck.yaml + slides/*.md + rendered/<name>.pptx.
Run: python3 tools/seminar-render/build_cases_deck.py
"""
from pathlib import Path
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

# === Ocean Gradient v3 palette (LOCKED) ===
DEEP  = RGBColor(0x21, 0x29, 0x5C)
MID   = RGBColor(0x06, 0x5A, 0x82)
LIGHT = RGBColor(0x1C, 0x72, 0x93)
TEAL  = RGBColor(0x02, 0x80, 0x90)
SURF  = RGBColor(0xF4, 0xF7, 0xFA)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GOLD  = RGBColor(0xF0, 0xAB, 0x00)
SLATE = RGBColor(0x33, 0x3B, 0x49)
GTINT = RGBColor(0xFE, 0xF5, 0xE0)
NEG_T = RGBColor(0xFB, 0xEA, 0xEA)
NEG_L = RGBColor(0xB0, 0x4A, 0x4A)
POS_T = RGBColor(0xE9, 0xF5, 0xF2)
GREY  = RGBColor(0xE5, 0xEA, 0xF0)
CODEBG = RGBColor(0x1B, 0x22, 0x3B)
CODEFG = RGBColor(0xE3, 0xE9, 0xF2)
FONT  = "PT Sans"
MONO  = "Courier New"

def _noshadow(shp):
    el = shp._element.spPr
    from lxml import etree
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    lst = etree.SubElement(el, ns + "effectLst")

def box(slide, x, y, w, h, fill=SURF, stroke=LIGHT, spt=1.4, radius=True, adj=0.08):
    shp = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
        Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke; shp.line.width = Pt(spt)
    if radius:
        try: shp.adjustments[0] = adj
        except Exception: pass
    try: _noshadow(shp)
    except Exception: pass
    return shp

def txt(slide, x, y, w, h, runs, size=17, color=SLATE, bold=False,
        align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, ls=1.12, mono=False, bullet=False):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    if isinstance(runs, str): runs = [runs]
    first = True
    for item in runs:
        s, sz, col, bd = item if isinstance(item, tuple) else (item, size, color, bold)
        p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
        p.alignment = align; p.line_spacing = ls; p.space_after = Pt(4)
        r = p.add_run(); r.text = (("— " + s) if bullet else s)
        r.font.size = Pt(sz); r.font.color.rgb = col; r.font.bold = bd
        r.font.name = MONO if mono else FONT
    return tb

def _txt_tight(slide, x, y, w, h, runs, size=17, color=SLATE, bold=False,
               align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, ls=1.12, mono=False,
               bullet=False, space_after=4):
    """txt() variant with configurable paragraph space_after (Pt) — used where
    vertical space is tight and the default 4pt gap causes overflow."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    if isinstance(runs, str): runs = [runs]
    first = True
    for item in runs:
        st, sz, col, bd = item if isinstance(item, tuple) else (item, size, color, bold)
        p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
        p.alignment = align; p.line_spacing = ls; p.space_after = Pt(space_after)
        r = p.add_run(); r.text = (("— " + st) if bullet else st)
        r.font.size = Pt(sz); r.font.color.rgb = col; r.font.bold = bd
        r.font.name = MONO if mono else FONT
    return tb

def chip(slide, x, y, label, fill=MID, color=WHITE, size=12.5):
    w = 0.28 + 0.115 * len(label)
    shp = box(slide, x, y, w, 0.42, fill=fill, stroke=None, adj=0.5)
    tf = shp.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE; tf.word_wrap = False
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = label
    r.font.size = Pt(size); r.font.bold = True; r.font.color.rgb = color; r.font.name = FONT
    return w

def titlebar(slide, kicker, title):
    box(slide, 0, 0, 13.333, 1.2, fill=DEEP, stroke=None, radius=False)
    txt(slide, 0.6, 0.14, 12.1, 0.4, kicker, size=13, color=GOLD, bold=True)
    txt(slide, 0.6, 0.48, 12.1, 0.66, title, size=22, color=WHITE, bold=True, ls=1.05)

def _est_text_h(w, s, size, ls=1.2, bold=True, bullet=False, space_after=4):
    """Conservative estimate of wrapped text height (inches) for a box of width
    w (inches). Uses a chars-per-line heuristic — deliberately pessimistic (fewer
    chars/line, taller line) so the pptx never under-provisions vs real metrics.
    A list is treated as separate paragraphs (each starts its own line, + gaps)."""
    cpi = 13.3 / (size / 13.0)          # chars per inch at this size (bold, conservative)
    chars_line = max(1.0, w * cpi)
    line_in = (size / 72.0) * ls        # line height in inches
    if isinstance(s, (list, tuple)):
        paras = [str(p) for p in s]
    else:
        paras = [str(s)]
    total_lines = 0
    for p in paras:
        pl = len(p) + (2 if bullet else 0)   # "— " prefix
        total_lines += max(1, -(-pl // int(chars_line)))
    h = total_lines * line_in
    if len(paras) > 1:
        h += (space_after / 72.0) * (len(paras) - 1)
    return h

def callout(slide, x, y, w, h, s, size=15, fill=GTINT, stroke=GOLD, color=DEEP,
            floor=11.0, max_h=None):
    """Auto-fit callout: if the (heuristically estimated) text height exceeds the
    inner box height, step the font down to `floor`, then grow the box downward
    (bounded by max_h) so nothing clips. Returns the actual box height (inches)
    so callers can shift the elements that follow. Geometry mirrored 1:1 in
    render_png.py callout()."""
    pad_x, pad_y = 0.25, 0.1
    tw = w - 2 * pad_x
    sz = size
    cur_h = h
    while True:
        need = _est_text_h(tw, s, sz)
        if need <= (cur_h - 2 * pad_y) + 0.01:
            break
        if sz > floor + 0.01:
            sz = max(floor, sz - 1.0)
            continue
        grow_to = need + 2 * pad_y
        if max_h is not None:
            grow_to = min(grow_to, max_h)
        if grow_to <= cur_h + 0.01:
            break
        cur_h = grow_to
    box(slide, x, y, w, cur_h, fill=fill, stroke=stroke, spt=1.2)
    txt(slide, x + pad_x, y + pad_y, tw, cur_h - 2 * pad_y, s, size=sz, color=color,
        bold=True, anchor=MSO_ANCHOR.MIDDLE, ls=1.2)
    return cur_h

def codeblock(slide, x, y, w, h, lines):
    box(slide, x, y, w, h, fill=CODEBG, stroke=None, adj=0.04)
    tb = slide.shapes.add_textbox(Inches(x + 0.2), Inches(y + 0.12), Inches(w - 0.4), Inches(h - 0.24))
    tf = tb.text_frame; tf.word_wrap = True; first = True
    for ln in lines:
        p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
        p.line_spacing = 1.05
        r = p.add_run(); r.text = ln
        r.font.size = Pt(12.5); r.font.color.rgb = CODEFG; r.font.name = MONO

def excard(slide, x, y, w, h, kind, title, body):
    tint, line, mark, mcol = (NEG_T, NEG_L, "✕", NEG_L) if kind == "neg" else (POS_T, TEAL, "✓", TEAL)
    box(slide, x, y, w, h, fill=tint, stroke=line, spt=1.4, adj=0.06)
    m = box(slide, x + 0.2, y + 0.2, 0.42, 0.42, fill=mcol, stroke=None, adj=0.5)
    tf = m.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = mark; r.font.size = Pt(16); r.font.bold = True
    r.font.color.rgb = WHITE; r.font.name = FONT
    txt(slide, x + 0.78, y + 0.18, w - 1.0, 0.45, title, size=14.5, color=DEEP,
        bold=True, anchor=MSO_ANCHOR.MIDDLE)
    body_w = w - 0.48; body_h = h - 0.85
    # авто-уменьшение шрифта тела: длинный text не должен уходить за низ карточки.
    # ёмкость ≈ (симв/строку) × (строк): ~13 симв/дюйм при 13.5pt, строка ~0.24″
    cap = max(1.0, (body_w * 13.0) * (body_h / 0.24))
    b_sz = 13.5
    if len(str(body)) > cap:
        b_sz = 12.5
    if len(str(body)) > cap * 1.3:
        b_sz = 11.5
    txt(slide, x + 0.24, y + 0.72, body_w, body_h, body, size=b_sz, color=SLATE, ls=1.12)

def pipeline(slide, x, y, w, nodes, accent=MID, node_h=None, label_size=None):
    """Horizontal scheme: rounded boxes + right-arrows. nodes: list of str.
    node_h / label_size авто-подбираются под число нод и длину подписей, если
    не заданы явно: при n≥5 нода выше и шрифт мельче, длинные подписи ужимаются
    ещё сильнее, чтобы текст не вылезал за ноду шириной ~2.09″."""
    n = len(nodes); gap = 0.42
    nw = (w - gap * (n - 1)) / n
    if node_h is None:
        node_h = 1.0 if n <= 4 else 1.28
    if label_size is None:
        base = 13 if n <= 4 else 11
        # ~симв/строку в ноде при base pt; длинная подпись → ещё мельче
        cap = max(1.0, (nw - 0.16) * (13.0 / base) * 3.4)
        longest = max(len(str(lb)) for lb in nodes)
        if longest > cap * 2:      # >2 строк ожидается
            label_size = base - 1.5
        else:
            label_size = base
    cx = x
    for i, label in enumerate(nodes):
        fill = SURF; stroke = accent
        box(slide, cx, y, nw, node_h, fill=fill, stroke=stroke, spt=1.4)
        txt(slide, cx + 0.07, y + 0.08, nw - 0.14, node_h - 0.16, label, size=label_size,
            color=DEEP, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, ls=1.04)
        if i < n - 1:
            ar = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,
                Inches(cx + nw + 0.04), Inches(y + node_h / 2 - 0.09),
                Inches(gap - 0.08), Inches(0.18))
            ar.fill.solid(); ar.fill.fore_color.rgb = TEAL; ar.line.fill.background()
            try: _noshadow(ar)
            except Exception: pass
        cx += nw + gap

def notes(slide, t):
    slide.notes_slide.notes_text_frame.text = t or ""

# ===== slide kinds =====
def k_cover(s, sp):
    box(s, 0, 0, 13.333, 7.5, fill=DEEP, stroke=None, radius=False)
    box(s, 0, 3.0, 13.333, 0.06, fill=GOLD, stroke=None, radius=False)
    txt(s, 1.0, 1.5, 11.3, 0.6, sp["kicker"], size=19, color=GOLD, bold=True)
    txt(s, 1.0, 2.15, 11.3, 1.6, sp["title"], size=38, color=WHITE, bold=True, ls=1.05)
    txt(s, 1.0, 4.3, 11.3, 1.5, sp["sub"], size=19, color=SURF, ls=1.2)

def k_map(s, sp):
    titlebar(s, "Карта занятия", sp["title"])
    y = 1.55
    for name, desc in sp["blocks"]:
        box(s, 0.6, y, 12.13, 1.15, fill=SURF, stroke=LIGHT)
        box(s, 0.6, y, 0.12, 1.15, fill=TEAL, stroke=None, radius=False)
        txt(s, 0.95, y + 0.13, 11.6, 0.45, name, size=18, color=DEEP, bold=True)
        txt(s, 0.95, y + 0.6, 11.6, 0.5, desc, size=14, color=SLATE)
        y += 1.32
    txt(s, 0.6, y + 0.02, 12.1, 0.5,
        "Каждый кейс: контекст → решение и схема → усложнение из практики → разбор с примером",
        size=13.5, color=MID, bold=True)

def k_divider(s, sp):
    box(s, 0, 0, 13.333, 7.5, fill=MID, stroke=None, radius=False)
    txt(s, -0.1, -0.5, 6, 3.4, sp["number"], size=250, color=RGBColor(0x2E,0x6A,0x8F),
        bold=True, anchor=MSO_ANCHOR.BOTTOM)
    box(s, 0.62, 1.72, 0.2, 0.2, fill=GOLD, stroke=None, adj=0.5)
    txt(s, 0.6, 2.9, 12, 0.5, sp["block"], size=17, color=GTINT, bold=True)
    txt(s, 0.6, 3.4, 12, 1.4, sp["title"], size=36, color=WHITE, bold=True, ls=1.05)
    chip(s, 0.64, 4.9, sp["tag"], fill=DEEP)

def _fit_font(est_fn, w, text, sizes, box_h, ls, bold=True):
    """Return the largest size from `sizes` whose estimated height ≤ box_h; if
    none fit, the smallest. est_fn(w, text, size, ls, bold) → height (inches)."""
    for sz in sizes:
        if est_fn(w, text, sz, ls=ls, bold=bold) <= box_h + 0.01:
            return sz
    return sizes[-1]

def k_context(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    # lead auto-fits (font step) up to a 0.85″ band; cards shift down by its height
    lead_sz = _fit_font(_est_text_h, 12.1, sp["lead"], [16, 15, 14, 13], 0.82, 1.2, bold=False)
    lead_h = min(0.9, max(0.7, _est_text_h(12.1, sp["lead"], lead_sz, ls=1.2, bold=False)))
    txt(s, 0.6, 1.35, 12.1, lead_h, sp["lead"], size=lead_sz, color=SLATE, ls=1.2)
    items = sp["inputs"]; cols = 3
    cw = (12.13 - 0.3 * (cols - 1)) / cols
    x0, y0, ch = 0.6, max(2.25, 1.35 + lead_h + 0.08), 1.5
    # длинный label может занять 2 строки — оценим по самому длинному в наборе,
    # чтобы value во ВСЕХ карточках стартовало на одной высоте (ровная сетка)
    lab_chars = (cw - 0.36) * 11        # ~симв/строку у label при 12.5pt bold
    max_lab = max(len(str(lab)) for lab, _ in items)
    lab_two_lines = max_lab > lab_chars
    lab_sz = 12.5 if max_lab <= lab_chars * 1.6 else 11.5
    lab_h = 0.62 if lab_two_lines else 0.36
    val_top = 0.14 + lab_h + 0.04
    for i, (lab, tx) in enumerate(items):
        r, c = divmod(i, cols)
        x = x0 + c * (cw + 0.3); y = y0 + r * (ch + 0.22)
        box(s, x, y, cw, ch, fill=SURF, stroke=LIGHT)
        txt(s, x + 0.18, y + 0.12, cw - 0.36, lab_h, lab, size=lab_sz, color=TEAL, bold=True, ls=1.05)
        txt(s, x + 0.18, y + val_top, cw - 0.36, ch - val_top - 0.1, tx,
            size=13, color=SLATE, ls=1.1)
    qy = y0 + ((len(items) + cols - 1) // cols) * (ch + 0.22) + 0.08
    if qy > 6.2: qy = 6.2
    callout(s, 0.6, qy, 12.13, 0.72, sp["question"], size=17, fill=DEEP, stroke=None,
            color=WHITE, floor=13.0, max_h=7.32 - qy)
    notes(s, sp.get("notes", ""))

def k_scheme(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    lead = sp.get("lead", "")
    lead_sz = _fit_font(_est_text_h, 12.1, lead, [15, 14, 13], 0.62, 1.15, bold=False) if lead else 15
    txt(s, 0.6, 1.35, 12.1, 0.75, lead, size=lead_sz, color=SLATE, ls=1.15)
    pipeline(s, 0.6, 2.25, 12.13, sp["nodes"], accent=sp.get("accent", MID))
    if sp.get("bullets"):
        txt(s, 0.9, 3.75, 11.6, 2.0, [(b, 15, SLATE, False) for b in sp["bullets"]],
            bullet=True, ls=1.15)
    if sp.get("caption"):
        # caption auto-fits (font step, then grow) — bottom clamped to 7.32
        callout(s, 0.6, 6.35, 12.13, 0.7, sp["caption"], size=14, floor=11.0,
                max_h=7.32 - 6.35)
    notes(s, sp.get("notes", ""))

_CONCEPT_LOW = 7.32   # note must not cross this bottom line

def _concept_note_fit(note):
    """Pick font size + height (inches) for the bottom note so it fits above
    _CONCEPT_LOW. Returns (size, note_top, note_h). pptx-side (heuristic)."""
    if not note:
        return (13.5, _CONCEPT_LOW, 0.0)
    for sz in (13.5, 12.5, 11.5, 11.0):
        h = _est_text_h(12.1, note, sz, ls=1.15, bold=True)
        if h <= 1.05 or sz == 11.0:
            note_top = _CONCEPT_LOW - h
            return (sz, note_top, h)
    return (11.0, _CONCEPT_LOW - 1.05, 1.05)

def k_concept(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    # definition-callout auto-fits: grows down (bounded) leaving a gap before the
    # "Как работает" label; the label + steps follow its ACTUAL height
    def_h = callout(s, 0.6, 1.35, 12.13, 0.95, sp["definition"], size=15,
                    fill=GTINT, stroke=GOLD, color=DEEP, max_h=1.30)
    lab_y = 1.35 + def_h + 0.12
    txt(s, 0.6, lab_y, 5.0, 0.4, "Как работает", size=14, color=MID, bold=True)
    steps_y = lab_y + 0.40
    # bottom note auto-fits; note_top bounds where steps / mini-scheme may end
    note = sp.get("note")
    note_sz, note_top, note_h = _concept_note_fit(note)
    # авто-уменьшение шрифта steps при большом объёме, чтобы не наезжать на note
    steps = sp["steps"]
    total_chars = sum(len(str(x)) for x in steps)
    if len(steps) >= 5 or total_chars > 320:
        step_sz, step_ls = 13.0, 1.12
    elif len(steps) >= 4 or total_chars > 240:
        step_sz, step_ls = 13.8, 1.15
    else:
        step_sz, step_ls = 14.5, 1.18
    step_bottom = (note_top - 0.12) if note else _CONCEPT_LOW
    step_area_h = max(1.2, step_bottom - steps_y)
    txt(s, 0.6, steps_y, 6.0, step_area_h, [(x, step_sz, SLATE, False) for x in steps],
        bullet=True, ls=step_ls)
    if sp.get("scheme"):
        cont_y = steps_y - 0.20
        cont_h = max(2.4, step_bottom - cont_y)
        box(s, 6.9, cont_y, 5.83, cont_h, fill=SURF, stroke=LIGHT)
        # vertical mini-pipeline: шаг и высота ноды подгоняются под контейнер,
        # чтобы последняя нода не протыкала низ (запас 0.16″ сверху/снизу)
        m = len(sp["scheme"]); pad = 0.16
        avail = cont_h - 2 * pad
        step_v = avail / m
        node_h = min(0.62, step_v - 0.14)
        yy = cont_y + pad
        for node in sp["scheme"]:
            box(s, 7.15, yy, 5.33, node_h, fill=WHITE, stroke=MID, spt=1.2)
            txt(s, 7.25, yy + 0.03, 5.13, node_h - 0.06, node, size=13, color=DEEP,
                bold=True, anchor=MSO_ANCHOR.MIDDLE)
            yy += step_v
    if note:
        txt(s, 0.6, note_top, 12.1, note_h + 0.05, note, size=note_sz, color=MID,
            bold=True, ls=1.15)
    notes(s, sp.get("notes", ""))

def k_complication(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    box(s, 0.6, 1.45, 12.13, 2.4, fill=SURF, stroke=LIGHT)
    box(s, 0.6, 1.45, 0.12, 2.4, fill=GOLD, stroke=None, radius=False)
    txt(s, 1.0, 1.7, 11.4, 2.0, sp["body"], size=17, color=SLATE, ls=1.25)
    # effect auto-fits (font step, then grow); ask follows its actual height
    eff_h = callout(s, 0.6, 4.15, 12.13, 1.0, sp["effect"], size=16, floor=12.0,
                    max_h=1.55)
    if sp.get("ask"):
        ask_y = max(5.4, 4.15 + eff_h + 0.12)
        txt(s, 0.6, ask_y, 12.1, 7.28 - ask_y, sp["ask"], size=15, color=MID, bold=True, ls=1.2)
    notes(s, sp.get("notes", ""))

def k_resolution(s, sp):
    titlebar(s, sp["kicker"], "Разбор · как реализовать")
    # solution auto-fits (font step, then grow); label + howto shift by its height
    sol_h = callout(s, 0.6, 1.33, 12.13, 0.9, sp["solution"], size=15, fill=DEEP,
                    stroke=None, color=WHITE, floor=11.0, max_h=1.35)
    lab_y = 1.33 + sol_h + 0.13
    txt(s, 0.6, lab_y, 11.6, 0.34, "Как реализовать", size=14, color=MID, bold=True)
    steps = sp.get("howto", sp.get("lesson", []))
    ex = sp["example"]
    ex_y = 4.98
    steps_y = lab_y + 0.36
    steps_area = max(1.0, ex_y - 0.1 - steps_y)
    # step font auto-adapts so bullets fit above the example card
    st_sz = 14
    for cand in (14, 13, 12):
        if _est_text_h(11.7, list(steps), cand, ls=1.14, bold=False, bullet=True) <= steps_area + 0.01:
            st_sz = cand; break
    else:
        st_sz = 12
    txt(s, 0.9, steps_y, 11.7, steps_area, [(x, st_sz, SLATE, False) for x in steps],
        bullet=True, ls=1.14)
    excard(s, 0.6, ex_y, 12.13, 1.72, ex["kind"], ex["title"], ex["text"])
    notes(s, sp.get("notes", ""))

def k_variants(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    lead_sz = _fit_font(_est_text_h, 12.1, sp["lead"], [15, 14, 13], 0.58, 1.15, bold=False)
    txt(s, 0.6, 1.35, 12.1, 0.7, sp["lead"], size=lead_sz, color=SLATE, ls=1.15)
    cols = sp["cols"]; n = len(cols)
    cw = (12.13 - 0.3 * (n - 1)) / n; x0, y0, ch = 0.6, 2.05, 3.7
    # per-column: длинный sample получает больше высоты и меньший шрифт,
    # use-буллеты сдвигаются ниже под фактическую высоту sample-бокса
    sample_top = y0 + 0.72
    max_chars = max(len(c["sample"]) for c in cols)
    chars_per_col = (cw - 0.36) * 13  # ~симв/строку при 12.5pt
    for i, c in enumerate(cols):
        x = x0 + i * (cw + 0.3)
        box(s, x, y0, cw, ch, fill=SURF, stroke=LIGHT)
        box(s, x, y0, cw, 0.6, fill=MID, stroke=None, radius=True, adj=0.08)
        txt(s, x + 0.1, y0 + 0.06, cw - 0.2, 0.48, c["head"], size=14.5, color=WHITE,
            bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # оценка числа строк sample по самому длинному тексту среди колонок
        est_lines = max(2, int(max_chars / chars_per_col) + 1)
        s_sz = 12.5 if est_lines <= 4 else (11.5 if est_lines <= 5 else 11.0)
        s_h = min(2.2, 0.30 * est_lines + 0.30)  # растёт с длиной, но с потолком
        txt(s, x + 0.18, sample_top, cw - 0.36, s_h, c["sample"], size=s_sz,
            color=SLATE, ls=1.1)
        use_top = sample_top + s_h + 0.12
        use_area = (y0 + ch) - use_top - 0.12
        # use-буллеты авто-фитятся в остаток колонки, чтобы не вылезать за низ
        use_sz = 12.5 if est_lines <= 4 else 11.5
        for cand in (use_sz, 11.0, 10.5, 10.0):
            if _est_text_h(cw - 0.36, list(c["use"]), cand, ls=1.1, bold=False,
                           bullet=True) <= use_area + 0.01:
                use_sz = cand; break
        else:
            use_sz = 10.0
        txt(s, x + 0.18, use_top, cw - 0.36, use_area,
            [(u, use_sz, SLATE, False) for u in c["use"]], bullet=True, ls=1.1)
    # note callout auto-fits — bottom clamped to 7.32
    callout(s, 0.6, 6.0, 12.13, 0.95, sp["note"], size=15, floor=11.0, max_h=7.32 - 6.0)
    notes(s, sp.get("notes", ""))

def k_structured(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    txt(s, 0.6, 1.3, 6.0, 0.4, "Задаём схему ответа", size=14, color=MID, bold=True)
    codeblock(s, 0.6, 1.7, 6.0, 3.0, sp["schema_code"])
    txt(s, 6.85, 1.3, 5.9, 0.4, "Что получаем", size=14, color=MID, bold=True)
    box(s, 6.85, 1.7, 5.88, 1.55, fill=POS_T, stroke=TEAL)
    txt(s, 7.05, 1.85, 5.5, 1.3, sp["sample"], size=13, color=SLATE, ls=1.15, mono=True)
    excard(s, 6.85, 3.4, 5.88, 1.3, "neg", "Где упираемся", sp["limitation"])
    callout(s, 0.6, 4.95, 12.13, 1.2, sp["takeaway"], size=15, floor=11.0, max_h=7.32 - 4.95)
    notes(s, sp.get("notes", ""))

def _bars(slide, x, y, w, h, heights, labels, cut=None, cut_kind=None, accent=MID):
    """Mini bar chart of next-token probabilities inside a panel.
    heights: list of floats 0..1 (relative). cut: index — bars at index<cut kept
    (highlighted), rest greyed. cut_kind: text tag drawn under the panel."""
    n = len(heights); gap = 0.09
    bw = (w - gap * (n - 1)) / n
    base = y + h - 0.34
    maxh = h - 0.52
    cx = x
    for i, hv in enumerate(heights):
        bh = max(0.06, hv * maxh)
        kept = (cut is None) or (i < cut)
        fill = accent if kept else GREY
        box(slide, cx, base - bh, bw, bh, fill=fill, stroke=None, radius=False)
        txt(slide, cx - 0.05, base + 0.02, bw + 0.1, 0.28, labels[i], size=9.5,
            color=SLATE if kept else RGBColor(0xA0,0xA8,0xB4), bold=kept,
            align=PP_ALIGN.CENTER)
        cx += bw + gap
    if cut_kind:
        txt(slide, x, y - 0.02, w, 0.3, cut_kind, size=11, color=accent, bold=True,
            align=PP_ALIGN.CENTER)

_PAL = {"deep": DEEP, "mid": MID, "light": LIGHT, "teal": TEAL, "gold": GOLD}

def k_distribution(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    txt(s, 0.6, 1.32, 12.1, 0.6, sp["lead"], size=15, color=SLATE, ls=1.15)
    panels = sp["panels"]; n = len(panels)
    pw = (12.13 - 0.3 * (n - 1)) / n; x0, y0, ph = 0.6, 2.15, 3.55
    for i, pn in enumerate(panels):
        x = x0 + i * (pw + 0.3)
        accent = _PAL.get(pn.get("accent", "teal"), TEAL)
        head_fill = _PAL.get(pn.get("head_fill", "mid"), MID)
        box(s, x, y0, pw, ph, fill=SURF, stroke=LIGHT)
        box(s, x, y0, pw, 0.55, fill=head_fill, stroke=None, radius=True, adj=0.08)
        txt(s, x + 0.08, y0 + 0.04, pw - 0.16, 0.46, pn["head"], size=13.5, color=WHITE,
            bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        _bars(s, x + 0.22, y0 + 0.75, pw - 0.44, 2.05, pn["heights"], pn["labels"],
              cut=pn.get("cut"), cut_kind=pn.get("cut_kind"), accent=accent)
        txt(s, x + 0.18, y0 + 2.92, pw - 0.36, 0.55, pn["note"], size=11.5, color=SLATE,
            ls=1.1, align=PP_ALIGN.CENTER)
    callout(s, 0.6, 5.95, 12.13, 0.95, sp["takeaway"], size=15, floor=11.0, max_h=7.32 - 5.95)
    notes(s, sp.get("notes", ""))

def k_breakdown(s, sp):
    """Разбор по стандарту: два подзаголовка — Ключевые компоненты / Ключевые
    комментарии по теме (Логика реализации убрана — дублировала слайд scheme).
    sp: components (list[(name, role)] or list[str]), comments (list[str]).
    Шрифт компонентов авто-уменьшается при >4 элементах, интервалы ужимаются
    при >5, низ последнего элемента гарантированно ≤ 6.9″."""
    titlebar(s, sp["kicker"], sp.get("title", "Разбор · компоненты и комментарии"))
    # Две колонки на всю рабочую высоту: слева компоненты, справа комментарии
    colw = 5.96
    bx_y, bx_h = 1.4, 5.5   # низ боксов = 6.9″
    txt(s, 0.6, 1.02, colw, 0.34, "Ключевые компоненты", size=14, color=MID, bold=True)
    txt(s, 6.77, 1.02, colw, 0.34, "Ключевые комментарии по теме", size=14, color=MID, bold=True)
    box(s, 0.6, bx_y, colw, bx_h, fill=SURF, stroke=LIGHT)
    box(s, 6.77, bx_y, colw, bx_h, fill=GTINT, stroke=GOLD)
    comps = sp["components"]
    n = len(comps)
    # авто-адаптация шрифта/интервала под число компонентов
    if n <= 4:
        name_sz, role_sz, ls, sa = 12.5, 12.0, 1.14, 4
    elif n == 5:
        name_sz, role_sz, ls, sa = 12.0, 11.0, 1.08, 2
    else:  # >=6
        name_sz, role_sz, ls, sa = 11.5, 10.5, 1.02, 1
    lines = []
    for c in comps:
        if isinstance(c, tuple):
            name, role = c
            lines.append((name, name_sz, DEEP, True))
            lines.append((role, role_sz, SLATE, False))
        else:
            lines.append((c, name_sz, SLATE, False))
    _txt_tight(s, 0.8, bx_y + 0.14, colw - 0.4, bx_h - 0.28, lines, ls=ls, space_after=sa)
    # комментарии — обычно 3 пункта, чуть уменьшаем при 4+
    csz = 12.5 if len(sp["comments"]) <= 3 else 11.5
    _txt_tight(s, 6.97, bx_y + 0.14, colw - 0.4, bx_h - 0.28,
               [(x, csz, DEEP, False) for x in sp["comments"]], ls=1.16,
               space_after=4, bullet=True)
    notes(s, sp.get("notes", ""))

def k_finale(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    txt(s, 0.9, 1.55, 11.6, 3.4, [(p, 16, SLATE, False) for p in sp["points"]],
        bullet=True, ls=1.22)
    callout(s, 0.6, 5.35, 12.13, 1.1, sp["takeaway"], size=16, floor=11.0, max_h=7.32 - 5.35)
    notes(s, sp.get("notes", ""))

def k_closing(s, sp):
    box(s, 0, 0, 13.333, 7.5, fill=DEEP, stroke=None, radius=False)
    txt(s, 0.7, 0.85, 12, 0.9, "Что унести", size=30, color=GOLD, bold=True)
    txt(s, 0.9, 2.0, 11.6, 3.2, [(t, 18, SURF, False) for t in sp["takeaways"]],
        bullet=True, ls=1.2)
    txt(s, 0.9, 5.7, 11.6, 0.9, sp["bridge"], size=16, color=GOLD, bold=True, ls=1.15)

KIND = {"cover": k_cover, "map": k_map, "divider": k_divider, "context": k_context,
        "scheme": k_scheme, "concept": k_concept, "complication": k_complication,
        "resolution": k_resolution, "variants": k_variants, "structured": k_structured,
        "distribution": k_distribution, "breakdown": k_breakdown,
        "finale": k_finale, "closing": k_closing}

def build(sem):
    root = Path("library/seminars") / sem["dir"]
    sld = root / "slides"
    if sld.exists():
        for f in sld.glob("*.md"): f.unlink()
    sld.mkdir(parents=True, exist_ok=True)
    prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]
    deck = ["deck:", f"  seminar_number: {sem['number']}", f"  title: \"{sem['title']}\"",
            "  format: \"разбор_кейсов\"", f"  central_question: \"{sem['central']}\"",
            f"  learning_outcomes: {sem['lo']}", "  language: ru",
            "  visual_style: \"matched to sem-02 (Ocean rounded boxes, schema pipelines, example cards)\"",
            "  render: \"tools/seminar-render/build_cases_deck.py\"", "slides:"]
    for i, sp in enumerate(sem["slides"], 1):
        sid = f"s{i:02d}"; slide = prs.slides.add_slide(blank)
        KIND[sp["kind"]](slide, sp)
        label = sp.get("title") or sp.get("kicker") or sp["kind"]
        fname = f"{sid}-{sp['kind']}.md"
        deck += [f"  - id: {sid}", f"    file: slides/{fname}",
                 f"    type: {sp['kind']}", f"    assertion: \"{label}\""]
        (sld / fname).write_text(
            f"---\nid: {sid}\ntype: {sp['kind']}\nassertion: \"{label}\"\n---\n\n"
            f"# {label}\n\n(См. tools/seminar-render/spec_{sem['dir'].replace('-','')}.py — "
            f"слайд {sid}. Рендер из спека.)\n", encoding="utf-8")
    (root / "deck.yaml").write_text("\n".join(deck) + "\n", encoding="utf-8")
    out = root / "rendered"; out.mkdir(exist_ok=True)
    prs.save(str(out / f"{sem['dir']}.pptx"))
    print(f"{sem['dir']}: {len(sem['slides'])} slides -> {out / (sem['dir']+'.pptx')}")

if __name__ == "__main__":
    import importlib.util
    here = Path(__file__).parent
    for spec_file in ["spec_sem03.py", "spec_sem04.py"]:
        p = here / spec_file
        st = importlib.util.spec_from_file_location(spec_file[:-3], p)
        m = importlib.util.module_from_spec(st); st.loader.exec_module(m)
        build(m.SEMINAR)
