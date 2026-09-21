"""
Build script for Семинар 4 v2 — «Сборка кодинг-агента: лестница роста конфигурации»
(issue #201, раунд 2, полная пересборка на новом deck.yaml/slides, 65 слайдов).

Source-of-truth: deck.yaml + slides/*.md (65 slides, rework/section-0..7). Direct
python-pptx build (not PowerPoint MCP), per notes/mcp-limitations.md
[#54-1/#54-2/#54-3]: MCP has no list_shapes, format_runs is buggy, no
update_shape_position. Full-rebuild via python-pptx sidesteps all three.

Canvas: 13.333" x 7.5" (16:9). Ocean Gradient v3 palette, LOCKED.

No live terminal on this seminar — every "terminal snapshot" on these slides is
either a *verbatim* transcription of a real captured command output
(library/seminars/sem-04/assets/captures/*.txt, dated 2026-09-20/21) or, where
no capture exists (7 positions flagged [ДОСЪЁМКА:...] in frontmatter
visual.backup only, never on the visible slide), a text/card layout that does
NOT imitate a terminal — exactly as each slide's own Visual section specifies.
The 7 no-capture positions: s10, s14 (content is FINAL per fix-pass — used
as-is), s21, s24, s42, s59, s60 (s60's review.md panel is derived from the
real capture 34 verdict already used on s54 — not invented).

v2 fixes over v1 (owner lessons from round 1, issue #201):
  - ONE shared builder for all 7 stage dividers (build_stage_divider) from the
    very start — v1 had a bespoke second function for two dividers that drifted.
  - Hero on s01 AND s65 (not just s01) is >=40% of slide area from the first
    render, not a later fix-pass.
  - Zero self-reference to "курс"/"лекция N"/"семинар" as a course artefact in
    VISIBLE text (mentions of "Лекция 3" as a content fact the audience
    already attended are fine and appear in speaker notes / a few visible
    facilitator asides that are part of the pedagogical script itself, per the
    slides/*.md source — never a meta "as covered in this course" aside).
  - Deep-latin-scan run before declaring done (see iteration-log.md).
"""
import re
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt, Emu
from lxml import etree

# === Palette (LOCKED Ocean Gradient v3) ===
DEEP    = RGBColor(0x21, 0x29, 0x5C)
MID     = RGBColor(0x06, 0x5A, 0x82)
LIGHT   = RGBColor(0x1C, 0x72, 0x93)
TEAL    = RGBColor(0x02, 0x80, 0x90)
SURFACE = RGBColor(0xF4, 0xF7, 0xFA)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
GOLD    = RGBColor(0xF0, 0xAB, 0x00)
SLATE   = RGBColor(0x6B, 0x76, 0x85)
GOLD_TINT = RGBColor(0xFE, 0xF5, 0xE0)
SOFT_GREY = RGBColor(0xE5, 0xEA, 0xF0)
CODE_BG = RGBColor(0x16, 0x1C, 0x30)
CODE_FG = RGBColor(0xE3, 0xE9, 0xF2)
CODE_MUTED = RGBColor(0x8B, 0x9B, 0xB4)
GOLD_DARK = RGBColor(0x8A, 0x62, 0x00)  # WCAG-safe dark-gold for text/icons on
                                         # light bg (gold #F0AB00 text fails
                                         # WCAG AA on SURFACE/WHITE — known
                                         # palette defect, see
                                         # project_ocean_palette_gold_contrast_defect)
DENY_RED_SAFE = RGBColor(0x8A, 0x2A, 0x2A)  # NOT a palette addition — used
                                             # ONLY as icon-free text color for
                                             # literal "deny"/blocked quotes

# === Constants ===
SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "rendered/assets"
ICONS = ASSETS / "icons/rendered"
SEM02_ICONS = ROOT.parent / "sem-02/rendered/assets/icons/rendered"
SEM03_ICONS = ROOT.parent / "sem-03/rendered/assets/icons/rendered"
SLIDES_DIR = ROOT / "slides"
OUT = ROOT / "rendered/sem-04.pptx"
FONT_HEAD = "Arial"
FONT_BODY = "Arial"
FONT_MONO = "Consolas"


# ============================================================
# Generic low-level helpers
# ============================================================

def setup_pres():
    p = Presentation()
    p.slide_width = Inches(SLIDE_W_IN)
    p.slide_height = Inches(SLIDE_H_IN)
    return p


def blank(p):
    return p.slides.add_slide(p.slide_layouts[6])


def set_slide_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def _fits(text, size, width_in, height_in, *, line_h_factor=1.28, char_w_factor=0.52,
          label=""):
    """Cheap diagnostic (not pixel-perfect, deliberately conservative) — estimates
    whether `text` at `size`pt fits in a box of width_in x height_in, and prints an
    OVERFLOW WARNING if not. Used across the deck to catch text/box mismatches in
    one build pass instead of eyeballing all 65 PNGs by hand."""
    if not text or width_in <= 0:
        return
    char_w = size * char_w_factor / 72.0
    chars_per_line = max(1, int(width_in / char_w))
    # count words to allow wrap; approximate by splitting on existing newlines too
    lines_needed = 0
    for para in text.split("\n"):
        n = len(para)
        lines_needed += max(1, -(-n // chars_per_line))  # ceil
    line_h = size * line_h_factor / 72.0
    capacity = height_in / line_h if line_h > 0 else 0
    if lines_needed > capacity + 0.15:  # small tolerance
        print(f"OVERFLOW WARNING [{label}]: '{text[:40]}...' needs ~{lines_needed} "
              f"lines ({size}pt in {width_in:.2f}in) but box height {height_in:.2f}in "
              f"fits only ~{capacity:.1f}")


def disable_shadow(shp):
    sppr = shp._element.spPr
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    for el in sppr.findall(ns + "effectLst"):
        sppr.remove(el)
    etree.SubElement(sppr, ns + "effectLst")


def _strike(run):
    rPr = run._r.get_or_add_rPr()
    rPr.set("strike", "sngStrike")


def text_box(slide, x, y, w, h, text, *,
             size=16, bold=False, italic=False, color=DEEP,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             font=FONT_BODY, line_spacing=1.15, strike=False):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    r = p.add_run()
    r.text = text
    r.font.name = font; r.font.size = Pt(size)
    r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color
    if strike:
        _strike(r)
    return tb


def multipara_box(slide, x, y, w, h, paragraphs, *,
                   anchor=MSO_ANCHOR.TOP, align=PP_ALIGN.LEFT):
    """Each item in `paragraphs` is a dict of text_box-style kwargs (+ optional
    'strike': True)."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for i, cfg in enumerate(paragraphs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = cfg.get("align", align)
        p.line_spacing = cfg.get("line_spacing", 1.15)
        p.space_after = Pt(cfg.get("space_after", 0))
        r = p.add_run()
        r.text = cfg["text"]
        r.font.name = cfg.get("font", FONT_BODY)
        r.font.size = Pt(cfg.get("size", 14))
        r.font.bold = cfg.get("bold", False)
        r.font.italic = cfg.get("italic", False)
        r.font.color.rgb = cfg.get("color", DEEP)
        if cfg.get("strike"):
            _strike(r)
    return tb


def ocean_box(slide, x, y, w, h, *, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5,
              radius_pt=12.0):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    try:
        adj = max(0.04, min(0.25, (radius_pt / 72.0) / max(min(w, h) / 2.0, 0.5)))
        shp.adjustments[0] = adj
    except Exception:
        pass
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    shp.line.color.rgb = stroke; shp.line.width = Pt(stroke_pt)
    disable_shadow(shp)
    return shp


def filled_rect(slide, x, y, w, h, fill, *, stroke=None, stroke_pt=0.0,
                 radius=False, radius_adj=0.16):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shp = slide.shapes.add_shape(shape_type, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(stroke_pt)
    if radius:
        try:
            shp.adjustments[0] = radius_adj
        except Exception:
            pass
    disable_shadow(shp)
    return shp


def dashed_box(slide, x, y, w, h, *, fill=SURFACE, stroke=GOLD, stroke_pt=1.8,
               radius_pt=12.0, dash="dash"):
    shp = ocean_box(slide, x, y, w, h, fill=fill, stroke=stroke, stroke_pt=stroke_pt,
                     radius_pt=radius_pt)
    ln = shp.line._get_or_add_ln()
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    dash_el = etree.SubElement(ln, ns + "prstDash")
    dash_el.set("val", dash)
    return shp


def gradient_rect(slide, x, y, w, h, stops):
    """Linear gradient rectangle (45deg, top-left -> bottom-right)."""
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.line.fill.background()
    disable_shadow(shp)
    sppr = shp._element.spPr
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    for tag in ("noFill", "solidFill", "gradFill", "blipFill", "pattFill"):
        for el in sppr.findall(ns + tag):
            sppr.remove(el)
    grad = etree.SubElement(sppr, ns + "gradFill")
    grad.set("rotWithShape", "1")
    gs_lst = etree.SubElement(grad, ns + "gsLst")
    for pos, color in stops:
        gs = etree.SubElement(gs_lst, ns + "gs")
        gs.set("pos", str(int(pos)))
        clr = etree.SubElement(gs, ns + "srgbClr")
        clr.set("val", "%02X%02X%02X" % (color[0], color[1], color[2]))
    lin = etree.SubElement(grad, ns + "lin")
    lin.set("ang", "2700000")
    lin.set("scaled", "1")
    return shp


def lerp_color(c_lo, c_hi, t):
    t = max(0.0, min(1.0, t))
    return RGBColor(
        int(c_lo[0] + (c_hi[0] - c_lo[0]) * t),
        int(c_lo[1] + (c_hi[1] - c_lo[1]) * t),
        int(c_lo[2] + (c_hi[2] - c_lo[2]) * t),
    )


def chip(slide, x, y, w, h, text, *, fill=MID, stroke=None, color=WHITE, size=13, bold=True):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    try:
        shp.adjustments[0] = 0.5
    except Exception:
        pass
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(1.2)
    tf = shp.text_frame
    tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.03); tf.margin_bottom = Inches(0.03)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.word_wrap = False
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = text
    r.font.name = FONT_BODY; r.font.size = Pt(size)
    r.font.bold = bold; r.font.color.rgb = color
    disable_shadow(shp)
    return shp


def add_image(slide, path, x, y, w=None, h=None):
    path = Path(path)
    if not path.exists():
        print(f"WARNING: missing image {path}")
        return None
    if w is not None and h is not None:
        return slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                        width=Inches(w), height=Inches(h))
    elif w is not None:
        return slide.shapes.add_picture(str(path), Inches(x), Inches(y), width=Inches(w))
    elif h is not None:
        return slide.shapes.add_picture(str(path), Inches(x), Inches(y), height=Inches(h))
    else:
        return slide.shapes.add_picture(str(path), Inches(x), Inches(y))


def icon_path(name, color_hex, size_px):
    local = ICONS / f"{name}-{color_hex}-{size_px}.png"
    if local.exists():
        return local
    for shared in (SEM03_ICONS, SEM02_ICONS):
        cand = shared / f"{name}-{color_hex}-{size_px}.png"
        if cand.exists():
            return cand
    return local


def icon(slide, name, color_hex, size_px, x, y, w_in):
    path = icon_path(name, color_hex, size_px)
    return add_image(slide, path, x, y, w=w_in, h=w_in)


def slide_title(slide, text, *, y=0.68, h=1.05, w=12.23, x=0.55, size=25,
                 color=DEEP, bold=True, line_spacing=1.14, align=PP_ALIGN.LEFT):
    text_box(slide, x=x, y=y, w=w, h=h, text=text,
             size=size, bold=bold, color=color, line_spacing=line_spacing,
             align=align)


def gold_callout(slide, x, y, w, h, text, *, size=14, bold=True, anchor=MSO_ANCHOR.MIDDLE,
                  align=PP_ALIGN.LEFT):
    filled_rect(slide, x, y, w, h, GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.1)
    text_box(slide, x=x + 0.22, y=y + 0.08, w=w - 0.44, h=h - 0.16, text=text,
             size=size, bold=bold, color=DEEP, anchor=anchor,
             align=align, line_spacing=1.22)


def speaker_notes(slide, text):
    tf = slide.notes_slide.notes_text_frame
    tf.text = text


def load_notes(slide_id):
    files = list(SLIDES_DIR.glob(f"{slide_id}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding="utf-8")
    m = re.search(r"## Speaker notes\s*\n(.*?)(?=\n## |\n---\s*\n## |\Z)", md, re.DOTALL)
    notes = m.group(1).strip() if m else ""
    notes = re.sub(r"\n+---\s*$", "", notes)
    return notes.strip()


def section_tag(slide, x, y, text, *, color=TEAL):
    text_box(slide, x, y, 11.5, 0.32, text=text.upper(), size=11.5, bold=True,
             color=color, align=PP_ALIGN.LEFT)


def header(slide, section_label, title, *, title_size=24, title_h=1.05):
    section_tag(slide, 0.55, 0.36, section_label)
    slide_title(slide, title, y=0.7, size=title_size, h=title_h)


def footer_note(slide, text, *, y=7.02):
    text_box(slide, 0.55, y, 12.23, 0.38, text=text, size=11.5, italic=True,
             color=LIGHT, align=PP_ALIGN.LEFT)


def terminal_card(slide, x, y, w, h, lines, *, title=None, size=13, line_spacing=1.32):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    try:
        shp.adjustments[0] = 0.035
    except Exception:
        pass
    shp.fill.solid(); shp.fill.fore_color.rgb = CODE_BG
    shp.line.color.rgb = LIGHT; shp.line.width = Pt(1.2)
    disable_shadow(shp)
    pad = 0.22
    ty = y + pad
    if title:
        text_box(slide, x + pad, ty, w - 2 * pad, 0.3, text=title, size=11,
                 bold=True, color=TEAL, font=FONT_MONO)
        ty += 0.34
    paras = []
    avail_w = w - 2 * pad
    char_w = size * 0.56 / 72.0  # monospace: chars are wider than proportional text
    chars_per_line = max(1, int(avail_w / char_w))
    est_lines = 0
    for text, color, *rest in lines:
        bold = rest[0] if rest else False
        paras.append({"text": text, "size": size, "font": FONT_MONO, "color": color,
                       "bold": bold, "line_spacing": line_spacing, "space_after": 2})
        est_lines += max(1, -(-max(len(text), 1) // chars_per_line))
    line_h = size * line_spacing * 1.18 / 72.0  # +18% safety margin — empirically
                                                  # LibreOffice/Consolas render taller
                                                  # than the naive pt-based estimate
                                                  # (caught a real overflow on s28 that
                                                  # the unpadded formula missed)
    needed_h = est_lines * line_h + len(lines) * (2 / 72.0)
    avail_h = y + h - pad - ty
    if needed_h > avail_h:
        print(f"OVERFLOW WARNING [terminal_card]: needs ~{needed_h:.2f}in "
              f"({len(lines)} lines @ {size}pt mono) but box gives {avail_h:.2f}in "
              f"(title={title!r})")
    multipara_box(slide, x + pad, ty, w - 2 * pad, y + h - pad - ty, paras)
    return shp


code_card = terminal_card


def table_card(slide, x, y, w, h, headers, rows, col_w, *, row_highlight=None,
               header_size=12, cell_size=12.5, row_align=None):
    ocean_box(slide, x, y, w, h)
    pad = 0.2
    header_h = 0.36 if headers else 0.0
    inner_w = w - 2 * pad
    cols_x = [x + pad]
    for cw in col_w[:-1]:
        cols_x.append(cols_x[-1] + inner_w * cw)
    if headers:
        for i, htext in enumerate(headers):
            cw = inner_w * col_w[i]
            text_box(slide, cols_x[i], y + pad, cw - 0.08, header_h, text=htext,
                     size=header_size, bold=True, color=SLATE,
                     align=(row_align[i] if row_align else PP_ALIGN.LEFT))
    row_y0 = y + pad + header_h + (0.06 if headers else 0)
    row_h = (h - pad - header_h - (0.06 if headers else 0) - pad) / max(len(rows), 1)
    for ri, row in enumerate(rows):
        ry = row_y0 + ri * row_h
        if row_highlight and ri in row_highlight:
            tint = GOLD_TINT if row_highlight[ri] == "gold" else RGBColor(0xE4, 0xF1, 0xF2)
            filled_rect(slide, x + 0.06, ry, w - 0.12, row_h, tint)
        for ci, ctext in enumerate(row):
            cw = inner_w * col_w[ci]
            _fits(ctext, cell_size, cw - 0.1, row_h, label=f"table_card row{ri}col{ci}")
            text_box(slide, cols_x[ci], ry, cw - 0.1, row_h, text=ctext,
                     size=cell_size, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                     line_spacing=1.15, align=(row_align[ci] if row_align else PP_ALIGN.LEFT))
        if ri < len(rows) - 1:
            ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                Inches(x + pad), Inches(ry + row_h), Inches(x + w - pad), Inches(ry + row_h))
            ln.line.color.rgb = SOFT_GREY; ln.line.width = Pt(0.75)


def option_row(slide, x, y, w, h, options, *, highlight_idx=None, size=13):
    n = len(options)
    gap = 0.16
    cw = (w - gap * (n - 1)) / n
    cx = x
    for i, label in enumerate(options):
        hl = (highlight_idx is not None and i == highlight_idx)
        box = dashed_box if hl else ocean_box
        box(slide, cx, y, cw, h, fill=(GOLD_TINT if hl else SURFACE),
            stroke=(GOLD_DARK if hl else SOFT_GREY), stroke_pt=1.4 if hl else 1.2)
        _fits(label.replace("\n", " "), size, cw - 0.2, h, label="option_row")
        color = GOLD_DARK if hl else DEEP
        lines = label.split("\n")
        paras = [{"text": ln, "size": size, "bold": hl, "color": color,
                   "align": PP_ALIGN.CENTER, "line_spacing": 1.2, "space_after": 2}
                  for ln in lines]
        multipara_box(slide, cx + 0.1, y, cw - 0.2, h, paras, anchor=MSO_ANCHOR.MIDDLE)
        cx += cw + gap


def reveal_table(slide, x, y, w, h, headers, rows, col_w, *, row_highlight=None,
                  header_size=11, cell_size=11.3):
    table_card(slide, x, y, w, h, headers, rows, col_w, row_highlight=row_highlight,
               header_size=header_size, cell_size=cell_size)


def numbered_card(slide, x, y, w, h, items, *, size=13, number_color=TEAL, fill=SURFACE,
                   stroke=LIGHT):
    ocean_box(slide, x, y, w, h, fill=fill, stroke=stroke)
    pad = 0.24
    row_h = (h - 2 * pad) / len(items)
    for i, item in enumerate(items):
        ry = y + pad + i * row_h
        text_box(slide, x + pad, ry, 0.5, row_h, text=f"{i + 1}", size=size + 4,
                 bold=True, color=number_color, anchor=MSO_ANCHOR.MIDDLE)
        _fits(item, size, w - 2 * pad - 0.55, row_h, label="numbered_card")
        text_box(slide, x + pad + 0.55, ry, w - 2 * pad - 0.55, row_h, text=item,
                 size=size, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.22)
        if i < len(items) - 1:
            ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                Inches(x + pad), Inches(ry + row_h), Inches(x + w - pad), Inches(ry + row_h))
            ln.line.color.rgb = SOFT_GREY; ln.line.width = Pt(0.6)


def failure_card(slide, x, y, w, h, *, icon_name, header_text, body, gold=False,
                  footnote=None, header_size=14, body_size=12.5):
    box = dashed_box if gold else ocean_box
    stroke = GOLD_DARK if gold else LIGHT
    box(slide, x, y, w, h, stroke=stroke, stroke_pt=1.6 if gold else 1.4,
        fill=GOLD_TINT if gold else SURFACE)
    pad = 0.22
    icon(slide, icon_name, "8A6200" if gold else "21295C", 96, x + pad, y + pad, 0.4)
    text_box(slide, x + pad + 0.54, y + pad - 0.02, w - 2 * pad - 0.54, 0.38,
             text=header_text, size=header_size, bold=True, color=GOLD_DARK if gold else DEEP)
    body_y = y + pad + 0.44
    body_h = h - pad - 0.44 - pad - (0.28 if footnote else 0)
    _fits(body, body_size, w - 2 * pad, body_h, label="failure_card body")
    text_box(slide, x + pad, body_y, w - 2 * pad, body_h, text=body, size=body_size,
             color=DEEP, line_spacing=1.28)
    if footnote:
        text_box(slide, x + pad, y + h - pad - 0.26, w - 2 * pad, 0.26,
                 text=footnote, size=10, italic=True, color=SLATE)


def criterion_plate(slide, x, y, w, h, items, *, title="ЗДЕСЬ ЕЩЁ РАНО", gold_last=False,
                     size=10.6):
    filled_rect(slide, x, y, w, h, RGBColor(0xEE, 0xF2, 0xF6), stroke=SOFT_GREY, stroke_pt=1.0,
                radius=True, radius_adj=0.1)
    pad = 0.18
    text_box(slide, x + pad, y + 0.05, w - 2 * pad, 0.24, text=title, size=10.5,
             bold=True, color=SLATE)
    bullet = "  ·  "
    body = bullet.join(items)
    color = DEEP
    _fits(body, size, w - 2 * pad, h - 0.33, label="criterion_plate")
    if gold_last:
        # render all but last normally, last one in gold-dark bold via multipara trick
        paras = [{"text": bullet.join(items[:-1]) + bullet, "size": size, "color": SLATE,
                   "line_spacing": 1.2}]
        tb = text_box(slide, x + pad, y + 0.28, w - 2 * pad, h - 0.33, text="",
                       size=size, color=SLATE)
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r1 = p.add_run(); r1.text = bullet.join(items[:-1]) + bullet
        r1.font.size = Pt(size); r1.font.color.rgb = SLATE; r1.font.name = FONT_BODY
        r2 = p.add_run(); r2.text = items[-1]
        r2.font.size = Pt(size); r2.font.color.rgb = GOLD_DARK; r2.font.bold = True
        r2.font.name = FONT_BODY
        return
    text_box(slide, x + pad, y + 0.28, w - 2 * pad, h - 0.33, text=body, size=size,
             color=color, line_spacing=1.2)


def placeholder_badge(slide, x, y, w, h, note):
    dashed_box(slide, x, y, w, h, fill=SURFACE, stroke=GOLD_DARK, stroke_pt=1.4)
    icon(slide, "clock", "8A6200", 64, x + (w - 0.4) / 2, y + 0.2, 0.4)
    text_box(slide, x + 0.3, y + 0.72, w - 0.6, h - 0.9, text=note, size=11.5,
             italic=True, color=GOLD_DARK, align=PP_ALIGN.CENTER, line_spacing=1.22)


# ============================================================
# Ladder motif (shared by s01 hero, s64 recap-tree, s07/s08 map)
# ============================================================

LADDER_STAGES = [
    ("0", "signup-landing/", "пусто"),
    ("1", "CLAUDE.md", "файл инструкций"),
    ("2", "DECISIONS.md", "память"),
    ("3", ".claude/settings.json", "хук"),
    ("4", "skills/deploy/", "скилл"),
    ("5", ".mcp.json", "MCP"),
    ("6", "agents/diff-reviewer.md", "субагент"),
    ("7", "Tasks/", "процесс"),
]

STAGE_TITLES = [
    "файл инструкций", "память", "хук", "скилл",
    "доступ наружу (MCP)", "субагент", "процесс",
]


def build_growth_staircase(slide, x, y, w, h, *, bar_lo, bar_hi, bar_gold,
                            label_color, gold_label_color, number_color,
                            gold_number_color, sublabel_color, baseline_color):
    """8-step ascending staircase from the real captured tree stages
    (captures/21-27-tree-stage*.txt) — shared hero motif for s01 and s65."""
    n = len(LADDER_STAGES)
    gap = 0.14
    chip_w = (w - gap * (n - 1)) / n
    bottom_reserve = 0.62
    top_reserve = 0.34
    baseline_y = y + h - bottom_reserve
    bar_max_h = h - bottom_reserve - top_reserve
    unit = bar_max_h / n
    ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x), Inches(baseline_y),
                                     Inches(x + w), Inches(baseline_y))
    ln.line.color.rgb = baseline_color; ln.line.width = Pt(1.4)
    cx = x
    for i, (num, fname, label) in enumerate(LADDER_STAGES):
        last = (i == n - 1)
        bar_h = max(0.14, (i + 1) * unit)
        bar_y = baseline_y - bar_h
        color = bar_gold if last else lerp_color(bar_lo, bar_hi, i / (n - 2))
        filled_rect(slide, cx, bar_y, chip_w, bar_h, color, radius=True, radius_adj=0.14)
        text_box(slide, cx - 0.07, bar_y - 0.32, chip_w + 0.14, 0.3, text=fname,
                 size=9.3, bold=last, color=(gold_label_color if last else label_color),
                 align=PP_ALIGN.CENTER, line_spacing=1.0)
        text_box(slide, cx - 0.07, baseline_y + 0.05, chip_w + 0.14, 0.28, text=num,
                 size=12.5, bold=True, color=(gold_number_color if last else number_color),
                 align=PP_ALIGN.CENTER)
        text_box(slide, cx - 0.1, baseline_y + 0.32, chip_w + 0.2, 0.3, text=label,
                 size=8.5, italic=True, color=sublabel_color, align=PP_ALIGN.CENTER,
                 line_spacing=1.0)
        cx += chip_w + gap


# ============================================================
# Shared pattern-level builder — ONE function for ALL 7 stage dividers
# ============================================================

def build_stage_divider(p, slide_id, *, stage_num, title, meaning, tag):
    """pattern: section_divider — single shared builder for s09/s16/s23/s32/
    s39/s48/s57 (owner-mandated fix over v1, which had a second bespoke
    function for two dividers that drifted from this one)."""
    s = blank(p)
    gradient_rect(s, 0, 0, SLIDE_W_IN, SLIDE_H_IN,
                   [(0, DEEP), (55000, MID), (100000, LIGHT)])
    # ladder strip at top: stage_num highlighted gold, earlier stages "passed",
    # later stages dim — same 7-cell strip on every divider, never elsewhere.
    strip_y = 0.55
    n = 7
    gap = 0.12
    cw = (12.23 - gap * (n - 1)) / n
    cx = 0.55
    for i in range(n):
        cur = (i + 1 == stage_num)
        passed = (i + 1 < stage_num)
        col = GOLD if cur else (RGBColor(0x5A, 0x6C, 0xA6) if passed else RGBColor(0x2C, 0x38, 0x72))
        filled_rect(s, cx, strip_y, cw, 0.3, col, radius=True, radius_adj=0.35)
        text_box(s, cx, strip_y, cw, 0.3, text=str(i + 1), size=11, bold=True,
                 color=(DEEP if cur else RGBColor(0xC7, 0xD2, 0xE8)), align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        cx += cw + gap
    text_box(s, 0.9, 2.15, 2.6, 2.0, text=str(stage_num), size=170, bold=True,
             color=RGBColor(0x3A, 0x4A, 0x86), align=PP_ALIGN.LEFT,
             anchor=MSO_ANCHOR.MIDDLE, font=FONT_HEAD)
    text_box(s, 3.3, 2.15, 8.6, 1.25, text=title, size=40, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    text_box(s, 3.35, 3.42, 8.6, 0.85, text=meaning, size=17, italic=True,
             color=RGBColor(0xCF, 0xDC, 0xEC), line_spacing=1.3)
    tag_w = 6.55
    tag_h = 1.0 if len(tag) > 55 else 0.6
    filled_rect(s, 3.35, 4.35, tag_w, tag_h, RGBColor(0x0B, 0x14, 0x3A), stroke=GOLD,
                stroke_pt=1.2, radius=True, radius_adj=0.28)
    text_box(s, 3.35 + 0.28, 4.35, tag_w - 0.56, tag_h, text=tag.upper(), size=11.5, bold=True,
             color=GOLD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
    icon_x, icon_y, icon_w = 10.55, 5.15, 1.55
    filled_rect(s, icon_x - 0.32, icon_y - 0.32, icon_w + 0.64, icon_w + 0.64,
                RGBColor(0x0B, 0x14, 0x3A), radius=True, radius_adj=0.18)
    icon(s, DIVIDER_ICON[stage_num], "F0AB00", 128, icon_x, icon_y, icon_w)
    speaker_notes(s, load_notes(slide_id))
    return s


DIVIDER_ICON = {1: "file-text", 2: "database", 3: "shield-check", 4: "puzzle",
                5: "network", 6: "user-round", 7: "clipboard-check"}


def build_growth_staircase_bare(slide, x, y, w, h, *, bar_lo, bar_hi, bar_gold,
                                 number_color, gold_number_color, baseline_color,
                                 show_numbers=True):
    """Unlabeled variant for s01 hero — bars only (+ optional ordinal), no
    filenames/stage names ('семь ступеней лестницы, без подписей')."""
    n = len(LADDER_STAGES)
    gap = 0.16
    chip_w = (w - gap * (n - 1)) / n
    bottom_reserve = 0.3 if show_numbers else 0.05
    baseline_y = y + h - bottom_reserve
    bar_max_h = h - bottom_reserve - 0.1
    unit = bar_max_h / n
    ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x), Inches(baseline_y),
                                     Inches(x + w), Inches(baseline_y))
    ln.line.color.rgb = baseline_color; ln.line.width = Pt(1.4)
    cx = x
    for i in range(n):
        last = (i == n - 1)
        bar_h = max(0.16, (i + 1) * unit)
        bar_y = baseline_y - bar_h
        color = bar_gold if last else lerp_color(bar_lo, bar_hi, i / (n - 2))
        filled_rect(slide, cx, bar_y, chip_w, bar_h, color, radius=True, radius_adj=0.16)
        if show_numbers:
            text_box(slide, cx - 0.05, baseline_y + 0.03, chip_w + 0.1, 0.26, text=str(i),
                     size=11.5, bold=last, color=(gold_number_color if last else number_color),
                     align=PP_ALIGN.CENTER)
        cx += chip_w + gap


# ============================================================
# Раздел 0 — Открытие (s01-s08)
# ============================================================

def build_s01(p):
    s = blank(p)
    gradient_rect(s, 0, 0, SLIDE_W_IN, SLIDE_H_IN,
                   [(0, DEEP), (50000, MID), (100000, LIGHT)])
    text_box(s, 8.9, 0.05, 4.2, 1.9, text="04", size=170, bold=True,
             color=RGBColor(0x33, 0x42, 0x7C), align=PP_ALIGN.RIGHT, font=FONT_HEAD,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0, 0.32, SLIDE_W_IN, 0.36, text="СЕМИНАР 4",
             size=13, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(s, 0, 0.68, SLIDE_W_IN, 0.9, text="Сборка кодинг-агента",
             size=44, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    text_box(s, 1.0, 1.5, SLIDE_W_IN - 2.0, 0.4,
             text="Семь ступеней конфигурации на одном сквозном кейсе",
             size=15.5, italic=True, color=RGBColor(0xCF, 0xDC, 0xEC), align=PP_ALIGN.CENTER)

    # Central question — the single textual block of the slide, verbatim.
    q_y = 2.08
    q_h = 1.15
    filled_rect(s, 1.15, q_y, SLIDE_W_IN - 2.3, q_h, RGBColor(0x0B, 0x14, 0x3A),
                stroke=GOLD, stroke_pt=1.8, radius=True, radius_adj=0.12)
    text_box(s, 1.55, q_y + 0.1, SLIDE_W_IN - 3.1, q_h - 0.2,
             text="«У вас репозиторий и агент, который в нём работает — какой блок "
                  "конфигурации добавить первым, и как понять, что следующий добавлять "
                  "ещё рано?»",
             size=16.5, italic=True, bold=True, color=GOLD, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.28)

    # Hero: 8-stage growth staircase, UNLABELED — >=40% of slide area.
    hero_x, hero_y, hero_w, hero_h = 0.55, 3.55, 12.23, 3.35  # 12.23*3.35=40.97in^2 ~= 41.0%
    text_box(s, hero_x, hero_y - 0.34, 8.0, 0.28,
             text="ПУСТАЯ ДИРЕКТОРИЯ  →  СЕМЬ ДОБАВЛЕНИЙ, ПОКА БЕЗ ИМЁН",
             size=11.5, bold=True, color=RGBColor(0x9C, 0xAE, 0xC9))
    build_growth_staircase_bare(s, hero_x, hero_y, hero_w, hero_h,
        bar_lo=(0x3A, 0x4A, 0x86), bar_hi=(0x6B, 0x7F, 0xC2), bar_gold=GOLD,
        number_color=RGBColor(0xB9, 0xC8, 0xDE), gold_number_color=GOLD,
        baseline_color=RGBColor(0x4A, 0x5C, 0x96), show_numbers=True)
    text_box(s, hero_x, hero_y + hero_h + 0.06, 12.0, 0.3,
             text="Реальные 7 стадий демо-репозитория signup-landing/ (git ls-tree по коммитам) "
                  "· источник: captures/21–27",
             size=9.5, italic=True, color=RGBColor(0x8A, 0x9B, 0xC0))
    speaker_notes(s, load_notes("s01"))


def two_basket_frame(slide, x, y, w, h, left_title, left_slots, right_title, right_slots, *,
                      right_highlight=False, why=None):
    gap = 0.32
    col_w = (w - gap) / 2
    ocean_box(slide, x, y, w, h)
    pad = 0.24
    text_box(slide, x + pad, y + pad - 0.04, col_w - pad, 0.32, text=left_title.upper(),
             size=13, bold=True, color=MID)
    rx = x + col_w + gap
    box_color = GOLD_DARK if right_highlight else MID
    text_box(slide, rx, y + pad - 0.04, col_w - pad, 0.32, text=right_title.upper(),
             size=13, bold=True, color=box_color)
    n = max(len(left_slots), len(right_slots))
    top = y + pad + 0.4
    slot_h = (h - pad - 0.4 - pad) / n
    for i in range(n):
        sy = top + i * slot_h * 0.98
        if i < len(left_slots):
            item = left_slots[i]
            fill = SURFACE if item else RGBColor(0xEE, 0xF1, 0xF5)
            stroke = LIGHT if item else SOFT_GREY
            filled_rect(slide, x + pad, sy, col_w - pad - 0.1, slot_h * 0.86, fill,
                        stroke=stroke, stroke_pt=1.1, radius=True, radius_adj=0.18)
            if item:
                text_box(slide, x + pad + 0.14, sy, col_w - pad - 0.38, slot_h * 0.86,
                         text=item, size=11.8, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                         line_spacing=1.15)
        if i < len(right_slots):
            item = right_slots[i]
            fill = GOLD_TINT if (item and right_highlight) else (SURFACE if item else RGBColor(0xEE, 0xF1, 0xF5))
            stroke = GOLD_DARK if (item and right_highlight) else (LIGHT if item else SOFT_GREY)
            filled_rect(slide, rx, sy, col_w - pad - 0.1, slot_h * 0.86, fill,
                        stroke=stroke, stroke_pt=1.3 if right_highlight else 1.1,
                        radius=True, radius_adj=0.18)
            if item:
                text_box(slide, rx + 0.14, sy, col_w - pad - 0.38, slot_h * 0.86,
                         text=item, size=11.8, bold=right_highlight, color=(GOLD_DARK if right_highlight else DEEP),
                         anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)


def build_s02(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Открытие", "Занятие начинается не с конфигурации агента, а с требований задачи",
           title_size=23)
    two_basket_frame(s, 0.55, 1.95, 12.23, 3.35, "видно в коде", [None, None, None],
                      "нигде не будет видно", [None, None, None])
    gold_callout(s, 0.55, 5.5, 12.23, 1.3,
                 "«Заказчик просит лендинг с формой заявки на демо-урок. Одна страница, "
                 "два поля, кнопка. Назовите вслух: что вообще должно быть у этой задачи, "
                 "чтобы вы могли сказать "
                 "‘готово’ и показать её заказчику? Не как это устроено внутри — а что "
                 "должно существовать.»", size=14.5)
    speaker_notes(s, load_notes("s02"))


def build_s03(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Требования", "Шесть требований делятся ровно пополам: три увидит в коде любой, три не будут видны нигде",
           title_size=21)
    two_basket_frame(s, 0.55, 1.85, 12.23, 4.1, "видно в коде",
                      ["поля формы: имя и email, оба обязательные",
                       "чем собирается — сборка в статику",
                       "чем проверяется — тест: форма не отправляется с пустыми полями"],
                      "нигде не будет видно",
                      ["что считается «готово»",
                       "чего агент не делает сам — деплой без явного запроса",
                       "как убедиться руками, что заявка реально доставлена"],
                      right_highlight=True)
    text_box(s, 0.55, 6.15, 12.23, 0.4, text="3 + 3", size=22, bold=True, color=GOLD_DARK,
             align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s03"))


def build_s04(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Сквозной кейс", "Репозиторий буквально пуст, и задача агенту поставлена одним запросом, целиком",
           title_size=21)
    half_w = 5.85
    terminal_card(s, 0.55, 2.0, half_w, 3.4, [
        ("$ ls -la signup-landing/", TEAL, True),
        ("total 8", CODE_FG),
        ("drwxr-xr-x 2 harness harness 4096 Sep 20 12:45 .", CODE_FG),
        ("drwxr-xr-x 3 harness harness 4096 Sep 20 12:45 ..", CODE_FG),
    ])
    text_box(s, 0.55, 5.55, half_w, 0.3, text="реальный вывод, не макет", size=11.5,
             italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    rx = 0.55 + half_w + 0.33
    ocean_box(s, rx, 2.0, half_w, 3.85)
    text_box(s, rx + 0.24, 2.22, half_w - 0.48, 3.4,
             text="«собери лендинг с формой заявки на демо-урок: статическая HTML-страница, "
                  "сборка Vite (npm run build → dist/), поля формы — имя и email, тест на "
                  "Playwright, который проверяет, что форма не отправляется с пустыми "
                  "обязательными полями (tests/form.spec.ts)»",
             size=15.5, italic=True, color=DEEP, line_spacing=1.42)
    speaker_notes(s, load_notes("s04"))


def build_s05(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Поворот", "Агент не задал ни одного уточняющего вопроса — всё, чего он не знал, он решил за вас молча",
           title_size=19)
    gold_callout(s, 0.55, 1.85, 12.23, 0.95,
                 "«Уточняющий вопрос не задавался. Все параметры задачи… были однозначно "
                 "выводимы из текста задачи, поэтому работа была начата сразу, без уточнений.»",
                 size=14.5, anchor=MSO_ANCHOR.MIDDLE)
    half_w = 5.85
    terminal_card(s, 0.55, 3.0, half_w, 1.85, [
        ("index.html", CODE_FG), ("src/main.js", CODE_FG),
        ("package.json", CODE_FG), ("tests/form.spec.ts", CODE_FG),
    ], title="создано")
    rx = 0.55 + half_w + 0.33
    terminal_card(s, rx, 3.0, half_w, 1.85, [
        ("npm install", CODE_FG),
        ("npm run build          # → dist/", CODE_FG),
        ("npm run test:e2e       # playwright test", CODE_FG),
    ], title="из финального ответа")
    gold_callout(s, 0.55, 5.05, 12.23, 0.85,
                 "«Все 4 прогнал и они зелёные» — запомните эту строку", size=15)
    speaker_notes(s, load_notes("s05"))


def build_s06(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Первый вопрос классу", "Бремя доказательства лежит на том, кто усложняет, а не на том, кто остаётся внизу",
           title_size=20)
    gold_callout(s, 0.55, 1.78, 12.23, 1.05,
                 "«Перед вами репозиторий, который агент только что собрал, и вам с этим же "
                 "агентом доделывать этот сайт дальше, неделями. Какой блок конфигурации вы "
                 "добавите первым — и почему именно его?»", size=14, anchor=MSO_ANCHOR.MIDDLE)
    opts = ["файл\nинструкций", "память", "хук", "скилл", "MCP-\nдоступ", "субагент",
            "процесс\nпроверки", "ничего"]
    y2 = 3.0
    n = len(opts)
    gap = 0.14
    cw = (12.23 - gap * (n - 1)) / n
    cx = 0.55
    for i, label in enumerate(opts):
        ocean_box(s, cx, y2, cw, 1.05, fill=SURFACE, stroke=SOFT_GREY, stroke_pt=1.1)
        text_box(s, cx + 0.05, y2, cw - 0.1, 1.05, text=label, size=11, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
        cx += cw + gap
    headers = ["Прозвучало", "Где работает", "Почему здесь ещё рано"]
    rows = [
        ["файл инструкций — «так делают»", "есть накопленное знание вне кода", "«так делают» — не триггер, а инерция"],
        ["хук — «защита на будущее»", "риск конкретной команды уже реален", "защищаете гипотезу, а не факт"],
        ["MCP — «пригодится»", "доступ нужен повторно, из нескольких сессий", "самый дорогой блок — по контексту и по поверхности атаки"],
        ["ничего", "на нулевой ступени — всегда", "не рано: это и есть ответ"],
    ]
    reveal_table(s, 0.55, 4.25, 12.23, 2.55, headers, rows, [0.28, 0.32, 0.4],
                 row_highlight={3: "gold"})
    speaker_notes(s, load_notes("s06"))


def cobuilding_map(slide, x, y, w, h, *, slots, grey_slots, rule_text=None):
    """5 numbered white slots + 2 grey practical-layer slots, shared by
    s07 (empty) / s08 (filled)."""
    ocean_box(slide, x, y, w, h)
    pad = 0.26
    n = 5
    gap = 0.16
    total_slots = n + len(grey_slots)
    row_gap = 0.16
    cw = (w - 2 * pad - row_gap * (total_slots - 1)) / total_slots
    top = y + pad
    slot_h = 1.55 if rule_text is None else 1.35
    cx = x + pad
    for i in range(n):
        label, desc = slots[i] if slots[i] else (None, None)
        fill = SURFACE if label else RGBColor(0xEE, 0xF1, 0xF5)
        stroke = LIGHT if label else SOFT_GREY
        filled_rect(slide, cx, top, cw, slot_h, fill, stroke=stroke, stroke_pt=1.2,
                    radius=True, radius_adj=0.12)
        text_box(slide, cx, top + 0.08, cw, 0.3, text=str(i + 1), size=13, bold=True,
                 color=MID, align=PP_ALIGN.CENTER)
        if label:
            paras = [{"text": ln, "size": 11.5, "bold": True, "color": DEEP,
                       "align": PP_ALIGN.CENTER, "line_spacing": 1.05} for ln in label.split("\n")]
            multipara_box(slide, cx + 0.06, top + 0.4, cw - 0.12, 0.55, paras)
            text_box(slide, cx + 0.06, top + 0.92, cw - 0.12, slot_h - 0.98, text=desc or "",
                     size=8.8, italic=True, color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.05)
        cx += cw + row_gap
    for j, gslot in enumerate(grey_slots):
        label, desc = gslot if gslot else (None, None)
        fill = RGBColor(0xE4, 0xE9, 0xEF) if label else RGBColor(0xEE, 0xF1, 0xF5)
        filled_rect(slide, cx, top, cw, slot_h, fill, stroke=SLATE, stroke_pt=1.0,
                    radius=True, radius_adj=0.12)
        if label:
            text_box(slide, cx + 0.06, top + 0.2, cw - 0.12, 0.5, text=label, size=11.5,
                     bold=True, color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.05)
            text_box(slide, cx + 0.06, top + 0.7, cw - 0.12, slot_h - 0.78, text=desc or "",
                     size=8.8, italic=True, color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.05)
        cx += cw + row_gap
    if rule_text:
        ry = top + slot_h + 0.2
        gold_callout(slide, x + pad, ry, w - 2 * pad, y + h - pad - ry, rule_text, size=12.5,
                     anchor=MSO_ANCHOR.MIDDLE)


def build_s07(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Опорная карта", "Экипировка агента — это пять слотов поверх базового цикла «планируй → действуй → проверяй → повторяй»",
           title_size=18)
    cobuilding_map(s, 0.55, 1.95, 12.23, 4.85, slots=[None] * 5, grey_slots=[None, None])
    speaker_notes(s, load_notes("s07"))


def build_s08(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Правило лестницы", "Оставайтесь на самой нижней ступени, которая закрывает требование задачи",
           title_size=20)
    slots = [
        ("память", "что агент помнит между сессиями"),
        ("инструкции-\nправила", "файл-конвенция проекта + журнал задач"),
        ("скиллы", "переиспользуемые процедуры"),
        ("субагенты", "делегирование с отдельным окном"),
        ("доступ\nнаружу (MCP)", "доступ к внешним системам"),
    ]
    grey = [("хук", "усиление слота 2"), ("процесс", "операционализация «проверяй»")]
    cobuilding_map(s, 0.55, 1.85, 12.23, 4.95, slots=slots, grey_slots=grey,
                    rule_text="«Оставайтесь на самой нижней ступени, которая закрывает требование задачи. "
                              "Поднимайтесь на следующую только тогда, когда можете назвать требование, которое "
                              "текущая ступень не закрывает. Каждый подъём оплачивается новой стоимостью, новыми "
                              "режимами отказа и новой поверхностью атаки.»")
    speaker_notes(s, load_notes("s08"))


# ============================================================
# Ступень 1 — Файл инструкций (s09-s15)
# ============================================================

def build_s09(p):
    build_stage_divider(p, "s09", stage_num=1, title="Ступень 1 · файл инструкций",
        meaning="Записываем только то, чего агент не выведет из кода",
        tag="3 хода совместного формирования · 1 контролируемый эксперимент")


def scenario_top_text(text, *, h=1.55, size=14):
    def render(s, y):
        ocean_box(s, 0.55, y, 12.23, h)
        text_box(s, 0.55 + 0.26, y + 0.16, 12.23 - 0.52, h - 0.32, text=text, size=size,
                 color=DEEP, line_spacing=1.32, anchor=MSO_ANCHOR.MIDDLE)
        return y + h + 0.2
    return render


def build_s10(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 1 · Сценарий-боль", "«Готово» для агента — «собралось и тест зелёный»; «готово» для вас — «заявка доставлена на проде»",
           title_size=17)
    y = 1.75
    ocean_box(s, 0.55, y, 12.23, 0.92)
    text_box(s, 0.81, y, 11.7, 0.92,
             text="Новая сессия, неделю спустя. Заказчик: «отправил заявку с сайта — она не "
                  "пришла». Агент читает код, правит обработчик в src/main.js, запускает тест — "
                  "тест зелёный — и отчитывается: «Готово, тест проходит».",
             size=11.8, color=DEEP, line_spacing=1.22, anchor=MSO_ANCHOR.MIDDLE)
    y += 0.92 + 0.1
    dashed_box(s, 0.55, y, 12.23, 0.42, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.81, y, 11.7, 0.42,
             text="а tests/form.spec.ts проверяет ровно одно — что форма НЕ отправляется с пустыми обязательными полями",
             size=10.8, italic=True, color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE)
    y += 0.42 + 0.1
    gold_callout(s, 0.55, y, 12.23, 0.85,
                 "«Агент починил форму, прогнал тест, тест зелёный, агент говорит "
                 "‘готово’. А заявка на проде по-прежнему не доходит — тест проверяет "
                 "совсем другое. Где должно быть записано, что считается ‘готово’, чтобы "
                 "агент в следующей сессии не сделал ровно то же самое?»", size=11.5)
    y += 0.85 + 0.1
    option_row(s, 0.55, y, 12.23, 0.5,
               ["ответить\nв чате", "README.md", "файл инструкций\nCLAUDE.md",
                "комментарий\nв тесте", "переписать\nсам тест"], size=10.3)
    y += 0.5 + 0.12
    headers = ["Вариант", "Где работает", "Почему ещё рано"]
    rows = [
        ["ответить в чате", "внутри одной сессии", "следующая начинается с пустого контекста"],
        ["README.md", "если человек откроет и прочитает", "агент читает файл инструкций, хочет он того или нет"],
        ["полное описание архитектуры", "если агент не понимает устройство", "он сам его собрал; после рефакторинга начнёт врать"],
        ["комментарий в тесте", "локально в файле теста", "правило уровня проекта должно жить в файле уровня проекта"],
        ["переписать сам тест", "лучший из неправильных", "проверяет доставку, но не объяснит границу деплоя"],
    ]
    reveal_table(s, 0.55, y, 12.23, 6.95 - y, headers, rows, [0.24, 0.32, 0.44], header_size=9.3, cell_size=9.3)
    speaker_notes(s, load_notes("s10"))


def build_s11(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 1 · Совместное формирование, ход 1", "Первая строка, которую зал хочет записать в файл инструкций, — команды сборки и теста",
           title_size=18)
    terminal_card(s, 0.55, 1.95, 12.23, 2.4, [
        ("# CLAUDE.md", CODE_MUTED, True),
        ("", CODE_FG),
        ("## …", CODE_MUTED),
        ("", CODE_FG),
        ("## …", CODE_MUTED),
    ], title="пустой каркас")
    gold_callout(s, 0.55, 4.55, 12.23, 0.95, "«Одну строку, которую точно надо записать. Кто?»",
                 size=16, align=PP_ALIGN.CENTER)
    text_box(s, 0.55, 5.7, 12.23, 0.4, text="строка вписывается на глазах у зала — без правки и без оценки",
             size=12, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s11"))


def build_s12(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 1 · Совместное формирование, ход 2", "Имена скриптов придумал сам агент — строка про команды почти ничего не добавляет, но платит контекстом",
           title_size=16)
    half_w = 5.85
    ocean_box(s, 0.55, 1.95, half_w, 1.7)
    text_box(s, 0.55 + 0.2, 1.95 + 0.2, half_w - 0.4, 1.3,
             text="build: npm run build\ntest: npx playwright test", size=15,
             color=SLATE, line_spacing=1.4, strike=True, font=FONT_MONO)
    rx = 0.55 + half_w + 0.33
    terminal_card(s, rx, 1.95, half_w, 1.7, [
        ("npm install", CODE_FG),
        ("npm run build          # → dist/", CODE_FG),
        ("npm run test:e2e       # playwright test", CODE_FG),
    ], title="из финального ответа агента")
    text_box(s, rx, 3.72, half_w, 0.3, text="имена скриптов придумал он сам", size=11,
             italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    dashed_box(s, 0.55, 3.95, 12.23, 0.62, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.8, 3.95, 11.7, 0.62,
             text="вместо неё остаётся: как проверить, что правка реально работает, а не только компилируется",
             size=12.5, italic=True, color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE)
    gold_callout(s, 0.55, 4.75, 12.23, 0.85, "«Вычёркиваем? Оставляем?»", size=17, align=PP_ALIGN.CENTER)
    footer_note(s, "Измеренная надбавка присутствия файла к стоимости и числу шагов — 20–23% относительно работы вовсе без файла", y=6.75)
    speaker_notes(s, load_notes("s12"))


def build_s13(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 1 · Совместное формирование, ход 3", "В файл идут ровно те три требования, которые зал сам отложил в группу «нигде не будет видно»",
           title_size=17)
    half = 5.85
    ocean_box(s, 0.55, 1.95, half, 4.0, fill=RGBColor(0xF4, 0xF6, 0xF9), stroke=SOFT_GREY)
    text_box(s, 0.75, 2.1, half - 0.4, 0.3, text="ШЕСТЬ ТРЕБОВАНИЙ (раздел 0)", size=11, bold=True, color=SLATE)
    items6 = ["поля формы: имя и email", "чем собирается", "чем проверяется",
              "что считается «готово»", "чего агент не делает сам", "как убедиться руками"]
    for i, it in enumerate(items6):
        gold = i >= 3
        ry = 2.5 + i * 0.55
        filled_rect(s, 0.75, ry, half - 0.4, 0.46, GOLD_TINT if gold else SURFACE,
                    stroke=GOLD_DARK if gold else SOFT_GREY, stroke_pt=1.2, radius=True, radius_adj=0.2)
        text_box(s, 0.9, ry, half - 0.7, 0.46, text=it, size=11.5,
                 color=GOLD_DARK if gold else SLATE, bold=gold, anchor=MSO_ANCHOR.MIDDLE)
    rx = 0.55 + half + 0.33
    numbered_card(s, rx, 1.95, half, 4.0, [
        "определение «готово» — одна строка",
        "граница действий: не выкладывать на прод без явного запроса",
        "как убедиться руками, что заявка дошла",
    ], size=13.5)
    text_box(s, 0.55, 6.1, 12.23, 0.4, text="3 из 6", size=20, bold=True, color=GOLD_DARK, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s13"))


def build_s14(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 1 · Решение", "Итоговый файл инструкций — восемнадцать строк и ровно три содержательных пункта, ни одного выводимого из кода",
           title_size=17)
    left_w = 6.85
    code_card(s, 0.55, 1.85, left_w, 4.85, [
        ("# CLAUDE.md", CODE_FG, True),
        ("", CODE_FG),
        ("signup-landing: статический лендинг с формой", CODE_MUTED),
        ("заявки на демо-урок.", CODE_MUTED),
        ("", CODE_FG),
        ("## Safety / scope boundaries", TEAL, True),
        ("- Никогда не запускать деплой на прод без", GOLD),
        ("  явного запроса — это касается и критерия", GOLD),
        ("  «готово» ниже: сам критерий не повод", GOLD),
        ("  инициировать деплой.", GOLD),
        ("", CODE_FG),
        ("## Definition of done", TEAL, True),
        ("- npm run build код 0, npx playwright test", GOLD),
        ("  зелёный, форма реально доставляет заявку —", GOLD),
        ("  проверяется на уже задеплоенной версии.", GOLD),
        ("", CODE_FG),
        ("## Build, test, verify", TEAL, True),
        ("- Открыть dist/index.html после сборки,", GOLD),
        ("  вручную отправить форму с заполненными и", GOLD),
        ("  с пустыми полями.", GOLD),
    ], size=10.3, line_spacing=1.18)
    rx = 0.55 + left_w + 0.3
    rw = 12.23 - left_w - 0.3
    terminal_card(s, rx, 1.85, rw, 2.35, [
        ("AGENTS.md", CODE_FG), ("CLAUDE.md", CODE_FG), ("index.html", CODE_FG),
        ("package.json", CODE_FG), ("src/main.js", CODE_FG), ("tests/form.spec.ts", CODE_FG),
    ], title="дерево ступени 1", size=11)
    dashed_box(s, rx, 4.35, rw, 0.6, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, rx + 0.15, 4.35, rw - 0.3, 0.6,
             text="ln -s CLAUDE.md AGENTS.md — один источник правды", size=11, italic=True,
             color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE)
    ocean_box(s, rx, 5.1, rw, 1.6, fill=SURFACE, stroke=TEAL, stroke_pt=1.1)
    text_box(s, rx + 0.16, 5.22, rw - 0.32, 1.35,
             text="грузится целиком в начало каждой сессии · уровни конкатенируются, "
                  "а не перекрываются · @-импорты не экономят контекст · ориентир — до 200 строк",
             size=10.5, color=DEEP, line_spacing=1.3)
    speaker_notes(s, load_notes("s14"))


def build_s15(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 1 · Провал / ограничение", "Сам факт наличия файла инструкций не покупает успех, но покупается контекстом всегда",
           title_size=18)
    headers = ["Плечо (против «файла нет», arXiv:2602.11988)", "Эффект на успех", "Значимость"]
    rows = [
        ["файл сгенерирован моделью", "−0,5%", "незначимо (p=87%)"],
        ["то же, другая связка модель/агент", "−2%", "незначимо (p=37%)"],
        ["файл написан разработчиком", "+2,4%", "незначимо (p=21%)"],
        ["стоимость и число шагов, любое плечо", "+20…23%", "значимо"],
        ["файл от модели, репозитории без документации", "+2,7%", "подтверждённое исключение"],
    ]
    reveal_table(s, 0.55, 1.85, 12.23, 2.35, headers, rows, [0.48, 0.26, 0.26],
                 row_highlight={3: "gold"}, header_size=10.5, cell_size=10.5)
    hw = 5.85
    failure_card(s, 0.55, 4.35, hw, 1.55, icon_name="quote",
                 header_text="Позиция разработчика движка",
                 body="«Bloated CLAUDE.md files cause Claude to ignore your actual instructions!»",
                 body_size=12)
    rx = 0.55 + hw + 0.33
    dashed_box(s, rx, 4.35, hw, 1.55, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, rx + 0.2, 4.5, hw - 0.4, 0.7, text="68%", size=40, bold=True, color=GOLD_DARK)
    text_box(s, rx + 0.2, 5.2, hw - 0.4, 0.62,
             text="точность следования инструкциям при 500 одновременных инструкциях (база — "
                  "малое число инструкций), IFScale, arXiv:2507.11538",
             size=10.5, italic=True, color=DEEP, line_spacing=1.2)
    criterion_plate(s, 0.55, 6.05, 12.23, 0.85, [
        "задача поставлена полно и разово", "крошечный репозиторий",
        "всё выводимое из кода в файл не идёт", "правило, недопустимое к нарушению — не сюда",
        "процедура нужна не каждой сессии — это скилл"])
    speaker_notes(s, load_notes("s15"))


# ============================================================
# Ступень 2 — Память (s16-s22)
# ============================================================

def build_s16(p):
    build_stage_divider(p, "s16", stage_num=2, title="Ступень 2 · память",
        meaning="Знание, которое появляется по ходу работы и исчезает вместе с сессией",
        tag="2 хода совместного формирования · 1 документированное отравление памяти · 3 замера против интуиции")


def build_s17(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 2 · Сценарий-боль", "Уже отклонённое решение всплывает снова — разговор, в котором его приняли, закончился",
           title_size=17)
    y = 1.75
    ocean_box(s, 0.55, y, 12.23, 0.95)
    text_box(s, 0.81, y, 11.7, 0.95,
             text="Третья сессия за две недели. Заказчик прислал заявку с опечаткой в домене — "
                  "форма её приняла. Агент предлагает подключить стороннюю библиотеку валидации — "
                  "ту самую, которую уже обсуждали и отклонили.",
             size=11.8, color=DEEP, line_spacing=1.22, anchor=MSO_ANCHOR.MIDDLE)
    y += 0.95 + 0.1
    dashed_box(s, 0.55, y, 12.23, 0.4, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.81, y, 11.7, 0.4, text="он предлагает её так, будто вопрос никогда не поднимался — для него он и не поднимался",
             size=10.8, italic=True, color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE)
    y += 0.4 + 0.1
    gold_callout(s, 0.55, y, 12.23, 0.85,
                 "«Вы второй раз за две недели объясняете агенту, почему в этой форме нет "
                 "сторонней библиотеки — то самое решение, которое уже отклонили. Куда это должно "
                 "попасть, чтобы не объяснять в третий раз — и почему не в тот файл инструкций, "
                 "который мы только что завели?»", size=11.2)
    y += 0.85 + 0.1
    option_row(s, 0.55, y, 12.23, 0.5,
               ["дописать\nCLAUDE.md", "сказать «запомни\nэто»", "завести\nDECISIONS.md",
                "поставить систему\nпамяти", "ничего — сам\nзапомнит"], size=9.8)
    y += 0.5 + 0.12
    headers = ["Вариант", "Где работает", "Почему ещё рано / нюанс"]
    rows = [
        ["дописать CLAUDE.md", "сработает механически", "файл читается целиком каждую сессию — ориентир 200 строк"],
        ["агент сам запомнит", "никогда", "между вызовами модель не хранит ни одного бита"],
        ["«запомни это»", "половина ответа", "уходит в авто-память — без синхронизации и ревью"],
        ["завести DECISIONS.md", "вторая половина", "дисциплина писать «почему», а не «что»"],
        ["система памяти", "разумный импульс", "замеры дальше покажут более сложную картину"],
    ]
    reveal_table(s, 0.55, y, 12.23, 6.95 - y, headers, rows, [0.24, 0.28, 0.48], header_size=9.3, cell_size=9.3)
    speaker_notes(s, load_notes("s17"))


def basket_row(slide, x, y, w, h, baskets, *, highlight_idx=None):
    """baskets: list of (title, [items or empty])."""
    n = len(baskets)
    gap = 0.24
    cw = (w - gap * (n - 1)) / n
    for i, (title, items) in enumerate(baskets):
        bx = x + i * (cw + gap)
        hl = (highlight_idx == i)
        box = dashed_box if hl else ocean_box
        box(slide, bx, y, cw, h, fill=(GOLD_TINT if hl else SURFACE),
            stroke=(GOLD_DARK if hl else LIGHT))
        text_box(slide, bx + 0.16, y + 0.12, cw - 0.32, 0.34, text=title.upper(), size=12.5,
                 bold=True, color=(GOLD_DARK if hl else MID), align=PP_ALIGN.CENTER)
        iy = y + 0.55
        ih = (h - 0.65) / max(len(items), 1)
        for it in items:
            filled_rect(slide, bx + 0.14, iy + 0.04, cw - 0.28, ih - 0.1,
                        WHITE if hl else RGBColor(0xEC, 0xF0, 0xF5), stroke=SOFT_GREY,
                        stroke_pt=0.9, radius=True, radius_adj=0.2)
            _fits(it, 10.3, cw - 0.48, ih - 0.1, label="basket_row item")
            text_box(slide, bx + 0.24, iy + 0.04, cw - 0.48, ih - 0.1, text=it, size=10.3,
                     color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.12)
            iy += ih
        if hl:
            text_box(slide, bx + 0.16, y + h - 0.32, cw - 0.32, 0.28, text="это тоже ответ",
                     size=10.5, italic=True, bold=True, color=GOLD_DARK, align=PP_ALIGN.CENTER)


def build_s18(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 2 · Совместное формирование, ход 1", "Не всё, что узнал агент, вообще стоит записывать — третья корзина такая же законная, как первые две",
           title_size=17)
    basket_row(s, 0.55, 1.95, 12.23, 1.5,
               [("авто-память", []), ("DECISIONS.md", []), ("никуда", [])])
    facts = [
        "«Не подключаем стороннюю библиотеку валидации — форма из двух полей»",
        "«Разработчик просит отвечать коротко, без преамбул»",
        "«Обработчик формы лежит в src/main.js»",
        "«19 сентября тест упал из-за таймаута, увеличили ожидание»",
        "«Своего бэкенда не делаем — заявка уходит на внешний сервис приёма форм»",
    ]
    numbered_card(s, 0.55, 3.65, 12.23, 2.65, facts, size=12.3)
    text_box(s, 0.55, 6.45, 12.23, 0.4, text="В какую?", size=17, bold=True, color=MID,
             align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s18"))


def build_s19(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 2 · Совместное формирование, ход 1 завершён", "Командное решение с обоснованием — в репозиторий; личное предпочтение — в авто-память; выводимое — никуда",
           title_size=15.5)
    baskets = [
        ("авто-память", ["отвечать коротко,\nбез преамбул — личное предпочтение"]),
        ("DECISIONS.md", ["не подключаем библиотеку\nвалидации — командное решение",
                           "своего бэкенда не делаем —\nрешение, неотличимое от недоделки"]),
        ("никуда", ["обработчик формы в src/main.js —\nвыводимо из кода",
                     "19 сент. тест упал из-за таймаута —\n«что», а не «почему»"]),
    ]
    basket_row(s, 0.55, 1.85, 12.23, 2.7, baskets, highlight_idx=2)
    ocean_box(s, 0.55, 4.75, 12.23, 1.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
    text_box(s, 0.75, 4.88, 12.0, 0.3, text="ХОД 2 · ЗАПИСЬ СОБИРАЕТСЯ ПО ЧАСТЯМ", size=11,
             bold=True, color=TEAL)
    text_box(s, 0.75, 5.25, 12.0, 0.95, text="дата?  →  формулировка решения одной строкой?  →  причина?",
             size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s19"))


def build_s20(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 2 · Решение", "Журнал решений — append-only лог «почему», а не второй файл инструкций",
           title_size=19)
    left_w = 6.85
    code_card(s, 0.55, 1.95, left_w, 3.0, [
        ("# Decisions", CODE_FG, True),
        ("", CODE_FG),
        ("Append-only log of why, in date order.", GOLD),
        ("", CODE_FG),
        ("## 2026-09-20 — не подключаем библиотеку", TEAL, True),
        ("   валидации форм", TEAL, True),
        ("Форма — два поля (имя, email), хватает", CODE_MUTED),
        ("нативных required/pattern в index.html.", CODE_MUTED),
        ("Сторонняя библиотека — лишняя зависимость", CODE_MUTED),
        ("и лишние килобайты в сборке ради этого объёма.", CODE_MUTED),
    ], size=11.5)
    rx = 0.55 + left_w + 0.3
    rw = 12.23 - left_w - 0.3
    terminal_card(s, rx, 1.95, rw, 2.65, [
        ("AGENTS.md", CODE_FG), ("CLAUDE.md", CODE_FG), ("DECISIONS.md", GOLD, True),
        ("index.html", CODE_FG), ("package.json", CODE_FG), ("src/main.js", CODE_FG),
        ("tests/form.spec.ts", CODE_FG),
    ], title="дерево ступени 2", size=11)
    dashed_box(s, rx, 4.75, rw, 0.7, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, rx + 0.16, 4.75, rw - 0.32, 0.7, text="diff создания файла — 7 добавленных строк",
             size=11.5, italic=True, color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s20"))


def build_s21(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 2 · Три слоя записи", "Разница между слоями не в формате — оба markdown, — а в том, кто инициирует запись и кто её потом увидит",
           title_size=17)
    headers = ["", "Файл инструкций (ступень 1)", "Авто-память", "DECISIONS.md"]
    rows = [
        ["Кто автор", "вы, заранее", "агент, по ходу", "вы, в момент решения"],
        ["Где живёт", "в репозитории, git", "вне репозитория, на машине", "в репозитории, git"],
        ["Что грузится", "целиком, каждую сессию", "индекс: 200 строк / 25 КБ", "ничего автоматически"],
        ["Код-ревью", "да", "нет", "да"],
        ["Смена машины", "переживает", "не переживает", "переживает"],
        ["Что туда идёт", "стабильные правила", "предпочтения, подходы", "решения и их «почему»"],
    ]
    reveal_table(s, 0.55, 1.85, 12.23, 3.85, headers, rows, [0.16, 0.3, 0.27, 0.27],
                 row_highlight={0: "teal"}, header_size=11, cell_size=10.8)
    ocean_box(s, 0.55, 5.85, 12.23, 0.95, fill=SURFACE, stroke=TEAL, stroke_pt=1.1)
    text_box(s, 0.75, 5.97, 11.8, 0.75,
             text="индекс памяти — только индекс · агент сам пропускает выводимое из кода · "
                  "сжатие контекста переживают только файлы на диске",
             size=11.5, color=DEEP, line_spacing=1.28, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s21"))


def build_s22(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 2 · Провал / ограничение", "Память по умолчанию читается как доверенный контекст, а не как данные",
           title_size=18)
    hw = 5.85
    failure_card(s, 0.55, 1.85, hw, 2.05, icon_name="alert-triangle",
                 header_text="Отравление памяти — SpAIware, сентябрь 2024",
                 body="Внешний текст с вложенной инструкцией → долговременная память → активация "
                      "в последующих сессиях, эксфильтрация переписки. Вектор закрыт в 1.2024.247; "
                      "структурный принцип остался.", body_size=11)
    rx = 0.55 + hw + 0.33
    dashed_box(s, rx, 1.85, hw, 2.05, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, rx + 0.2, 1.98, hw - 0.4, 0.6, text="≈48%", size=32, bold=True, color=GOLD_DARK)
    text_box(s, rx + 0.2, 2.55, hw - 0.4, 1.2,
             text="всех последующих обращений к памяти захвачено (MemoryGraft, 2025; база — 0% "
                  "до отравления). 5 подложенных документов управляют выводом в >90% случаев.",
             size=10.8, italic=True, color=DEEP, line_spacing=1.22)
    headers = ["Замер", "Значение", "База сравнения"]
    rows = [
        ["популярная система памяти на бенчмарке", "46,0% с памятью против 57,6% без", "та же система, память выключена"],
        ["6 систем против «весь текст сессии в файл»", "проигрыш на 25–67 пунктов", "тот же плоский файл"],
        ["дискреционность записи", "17% (4 из 24) — отказ записать факт", "те же 24 задачи"],
    ]
    reveal_table(s, 0.55, 4.1, 12.23, 1.85, headers, rows, [0.4, 0.3, 0.3], header_size=10, cell_size=9.8)
    criterion_plate(s, 0.55, 6.1, 12.23, 0.8, [
        "задача одноразовая", "весь контекст влезает в одно окно", "правила стабильны и укладываются в файл",
        "факт выводим из кода"], size=10)
    speaker_notes(s, load_notes("s22"))


# ============================================================
# Ступень 3 — Хук (s23-s31)
# ============================================================

def build_s23(p):
    build_stage_divider(p, "s23", stage_num=3, title="Ступень 3 · хук",
        meaning="Правило, которое исполняет среда, а не согласие модели",
        tag="5 вопросов совместного формирования · 3 реальных срабатывания · 2 CVE · 5 причин молчаливого отказа")


def build_s24(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 3 · Сценарий-боль", "Правило было записано и загружено — и всё равно нарушено",
           title_size=19)
    y = 1.78
    ocean_box(s, 0.55, y, 12.23, 1.15)
    text_box(s, 0.81, y + 0.1, 11.7, 0.95,
             text="Завтра показ сайта заказчику. Накануне в файл инструкций добавлена строка: "
                  "«Перед показом правки идут через отдельную ветку, прямых коммитов в main нет.» "
                  "Вечером, в спешке, агент правит валидацию формы и делает git commit прямо на main.",
             size=12, color=DEEP, line_spacing=1.24, anchor=MSO_ANCHOR.MIDDLE)
    y += 1.15 + 0.14
    gold_callout(s, 0.55, y, 12.23, 0.95,
                 "«Завтра показ. В файле инструкций написано: перед показом — только через "
                 "отдельную ветку. Агент только что закоммитил правку прямо в main. Текстом всё "
                 "было сказано правильно. Что вы сделаете, чтобы это стало НЕВОЗМОЖНЫМ, а не просто "
                 "маловероятным?»", size=12)
    y += 0.95 + 0.14
    option_row(s, 0.55, y, 12.23, 0.58,
               ["переписать\nправило капсом", "проверять руками\nпосле коммита",
                "защита ветки\nна сервере", "хук, который среда\nисполняет сама",
                "забрать у агента\nдоступ к git"], size=10.3)
    y += 0.58 + 0.14
    # v2 fix (qa-reports/2026-09-21-v2, P2 #4) — unify table shape with the
    # other scenario_question slides (s06/s10/s17/s58): 3-column "Вариант /
    # Где работает / Почему ещё рано" instead of the one-off 2-column
    # "Вариант / Оценка" + side callout. Content unchanged — the "Оценка"
    # text is split across the "где"/"почему" axis (rework/section-3-khuk.md
    # §A.4), and the side-box punchline is folded into the highlighted row.
    headers = ["Вариант", "Где работает", "Почему ещё рано"]
    rows = [
        ["переписать капсом", "нигде механически — эмфаза не создаёт барьера",
         "не превращает просьбу в закон — делает её просьбой заглавными буквами"],
        ["проверять руками", "хватает, пока коммитов немного",
         "не масштабируется на каждый коммит"],
        ["защита ветки на сервере", "работает — нужный слой",
         "обратная связь приходит поздно — коммит уже создан локально"],
        ["хук, который исполняет среда", "здесь — именно то, что нужно",
         "целевой ответ: правила в коде — законы, а в промпте — просьбы"],
        ["забрать доступ к git", "когда готовы коммитить руками",
         "рабочий вариант, но убирает риск вместе с пользой"],
    ]
    reveal_table(s, 0.55, y, 12.23, 6.95 - y, headers, rows, [0.24, 0.28, 0.48],
                 header_size=9.3, cell_size=9.3, row_highlight={3: "gold"})
    speaker_notes(s, load_notes("s24"))


def build_s25(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 3 · Совместное формирование, вопросы 1–2", "Проверять надо до вызова и только на одном инструменте",
           title_size=19)
    numbered_card(s, 0.55, 1.95, 5.85, 2.6, [
        "Проверять до или после?", "Вешаем на все инструменты или на один?"], size=14)
    code_card(s, 0.55 + 5.85 + 0.33, 1.95, 12.23 - 5.85 - 0.33, 2.6, [
        ("{", CODE_FG),
        ('  "hooks": {', CODE_FG),
        ('    "PreToolUse": [          // ← вопрос 1', GOLD),
        ("      {", CODE_FG),
        ('        "matcher": "Bash",   // ← вопрос 2', GOLD),
        ("        …", CODE_MUTED),
    ], size=11.5)
    ocean_box(s, 0.55, 4.85, 12.23, 1.5, fill=SURFACE, stroke=TEAL, stroke_pt=1.1)
    text_box(s, 0.75, 4.98, 11.8, 1.25,
             text="в жизненном цикле агента задокументировано свыше 30 событий — от старта сессии "
                  "до удаления рабочей копии; для старта нужны единицы. Чем шире условие срабатывания, "
                  "тем дороже ошибка в самой логике хука.", size=13, color=DEEP, line_spacing=1.3,
             anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s25"))


def build_s26(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 3 · Совместное формирование, вопросы 3–4", "Привычная команда получения ветки падает в свежем репозитории",
           title_size=17)
    left_w = 5.85
    numbered_card(s, 0.55, 1.95, left_w, 2.7, [
        "Откуда хук узнает команду?  →  jq -r '.tool_input.command'",
        "Как узнать ветку?  →  git symbolic-ref --short HEAD",
    ], size=12)
    rx = 0.55 + left_w + 0.33
    rw = 12.23 - left_w - 0.33
    terminal_card(s, rx, 1.95, rw, 2.7, [
        ("$ git init -q -b main", TEAL, True),
        ("$ git symbolic-ref --short HEAD", TEAL, True),
        ("main", CODE_FG),
        ("(exit code: 0)", CODE_MUTED),
        ("", CODE_FG),
        ("$ git rev-parse --abbrev-ref HEAD", CODE_MUTED, True),
        ("fatal: ambiguous argument 'HEAD': unknown", DENY_RED_SAFE),
        ("revision or path not in the working tree.", DENY_RED_SAFE),
        ("(exit code: 128)", DENY_RED_SAFE, True),
    ], size=10.3, line_spacing=1.24)
    text_box(s, rx + 0.05, 1.95 + 2.7 + 0.08, rw - 0.1, 0.3,
             text="rev-parse — команда, которую называет зал — перечёркнута после показа вывода",
             size=10.5, italic=True, color=SLATE, strike=False)
    ocean_box(s, 0.55, 4.95, 12.23, 1.4, fill=SURFACE, stroke=GOLD_DARK, stroke_pt=1.2)
    text_box(s, 0.75, 5.06, 11.8, 1.18,
             text="«Падение проверки — это не блокировка: это просто отсутствие блокировки. "
                  "Внешне — ничего. Абсолютно то же самое ‘ничего’, которое вы видите, когда "
                  "проверка прошла успешно.»", size=13.5, italic=True, color=DEEP,
             line_spacing=1.32, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s26"))


def build_s27(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 3 · Совместное формирование, вопрос 5", "Гейт, чей отказ молчалив, не считается установленным, пока его не заставили отказать громко",
           title_size=16)
    gold_callout(s, 0.55, 1.85, 12.23, 0.85, "«А если это вообще ещё не git-репозиторий? Что должен вернуть хук?»",
                 size=16, align=PP_ALIGN.CENTER)
    option_row(s, 0.55, 2.9, 12.23, 0.75, ["разрешить молча", "заблокировать", "спросить человека"],
               highlight_idx=2, size=14)
    terminal_card(s, 0.55, 3.9, 12.23, 1.55, [
        ("=== каталог: /tmp/no-repo-demo (git init НЕ выполнялся) ===", CODE_MUTED),
        ('{"permissionDecision":"ask",', GOLD, True),
        (' "permissionDecisionReason":"WARNING: branch-protection gate', GOLD),
        ('  inactive — this is not a git repository yet (no .git found),', GOLD),
        ('  so this hook cannot check anything…"}', GOLD),
    ], size=11)
    gold_callout(s, 0.55, 5.65, 12.23, 1.0,
                 "гейт, чей отказ молчалив, не считается установленным, пока его не заставили "
                 "отказать громко", size=15, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s27"))


def build_s28(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 3 · Решение", "Собранный хук — обычный файл проекта, который коммитится и работает в любом свежем клоне",
           title_size=17)
    left_w = 6.85
    code_card(s, 0.55, 1.85, left_w, 4.9, [
        ("{", CODE_FG),
        ('  "hooks": {', CODE_FG),
        ('    "PreToolUse": [           // ← 1: до вызова', GOLD),
        ("      {", CODE_FG),
        ('        "matcher": "Bash",   // ← 2: только команды', GOLD),
        ("        \"hooks\": [", CODE_FG),
        ("          {", CODE_FG),
        ('            "type": "command",', CODE_FG),
        ("            \"command\": \"jq -r '.tool_input.command' |", CODE_MUTED),
        ("              …", CODE_MUTED),
        ("              grep -qE git\\\\s+commit   // ← 3: команда из JSON", GOLD),
        ("              …git rev-parse --is-inside-work-tree… → ask  // ← 5", GOLD),
        ("              branch=$(git symbolic-ref --short HEAD) // ← 4", GOLD),
        ('              …[ "$branch" = "main" ] → deny…",', GOLD),
        ('            "timeout": 10', CODE_FG),
        ("          }", CODE_FG),
        ("        ]", CODE_FG),
        ("      }", CODE_FG),
        ("    ]", CODE_FG),
        ("  }", CODE_FG),
        ("}", CODE_FG),
    ], size=9.6, line_spacing=1.2)
    rx = 0.55 + left_w + 0.3
    rw = 12.23 - left_w - 0.3
    terminal_card(s, rx, 1.9, rw, 1.95, [
        ("AGENTS.md", CODE_FG), ("CLAUDE.md", CODE_FG), ("DECISIONS.md", CODE_FG),
        (".claude/settings.json", GOLD, True), ("index.html …", CODE_FG),
    ], title="дерево ступени 3", size=10.8)
    ocean_box(s, rx, 4.05, rw, 2.2, fill=SURFACE, stroke=TEAL, stroke_pt=1.1)
    text_box(s, rx + 0.16, 4.18, rw - 0.32, 1.95,
             text="это НЕ git-хук: версионируется и активен в любом свежем клоне · решение "
                  "возвращается полем allow/deny/ask · код возврата 2 блокирует безусловно, "
                  "даже поверх allow · списки хуков между уровнями объединяются, а не перекрываются",
             size=11, color=DEEP, line_spacing=1.32)
    speaker_notes(s, load_notes("s28"))


def build_s29(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 3 · Три срабатывания подряд", "Полная проверка барьера — запрещает то, что должно, и пропускает то, что должно",
           title_size=17)
    gap = 0.24
    cw = (12.23 - gap * 2) / 3
    y, h = 2.15, 3.5
    ocean_box(s, 0.55, y, cw, h)
    text_box(s, 0.55 + 0.16, y + 0.16, cw - 0.32, 0.3, text="1 · ВЕТКА MAIN", size=12, bold=True, color=MID)
    text_box(s, 0.55 + 0.2, y + 0.75, cw - 0.4, h - 1.3,
             text="permissionDecision: deny\n\n«BLOCKED: direct commit to main/master. "
                  "Create a feature branch first.»", size=13, color=DENY_RED_SAFE, bold=True,
             line_spacing=1.4, anchor=MSO_ANCHOR.MIDDLE)
    x2 = 0.55 + cw + gap
    ocean_box(s, x2, y, cw, h)
    text_box(s, x2 + 0.16, y + 0.16, cw - 0.32, 0.3, text="2 · ПОСЛЕ SWITCH -C", size=12, bold=True, color=MID)
    text_box(s, x2 + 0.2, y + 0.75, cw - 0.4, h - 1.3,
             text="=== HOOK OUTPUT (stdout) ===\n\n=== hook exit code: 0 (empty "
                  "stdout = hook did not block) ===", size=12, color=CODE_MUTED, font=FONT_MONO,
             line_spacing=1.35, anchor=MSO_ANCHOR.MIDDLE)
    x3 = x2 + cw + gap
    dashed_box(s, x3, y, cw, h, fill=GOLD_TINT, stroke=GOLD_DARK, stroke_pt=1.8)
    text_box(s, x3 + 0.16, y + 0.16, cw - 0.32, 0.3, text="3 · КОММИТ РЕАЛЬНО ЛЁГ", size=12, bold=True, color=GOLD_DARK)
    text_box(s, x3 + 0.2, y + 0.75, cw - 0.4, h - 1.55,
             text="[fix-form-field a666b27] fix: second\nform field\n 1 file changed, 8 insertions(+)\n"
                  " create mode 100644 src/validate.js", size=11.5, color=DEEP, font=FONT_MONO,
             line_spacing=1.3, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x3 + 0.2, y + h - 0.55, cw - 0.4, 0.4, text="и это важнее первых двух", size=12.5,
             italic=True, bold=True, color=GOLD_DARK)
    text_box(s, 0.55, y + h + 0.35, 12.23, 0.5,
             text="все три кадра — реальные захваченные выводы, ни один не нарисован",
             size=12, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s29"))


def build_s30(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 3 · Провал, слой 1", "Конфигурация агента — это исполняемый код, срабатывающий до подтверждения доверия к папке",
           title_size=18)
    ocean_box(s, 0.55, 1.85, 12.23, 1.7)
    text_box(s, 0.8, 2.0, 5.5, 1.4,
             text="CVE-2025-59536\n\n21.07.2025 обнаружено → 26.08.2025 патч → 29.08.2025 публикация",
             size=13, bold=True, color=DEEP, line_spacing=1.3)
    text_box(s, 6.5, 2.0, 5.5, 1.4,
             text="вредоносный хук на событие старта сессии в чужом файле настроек срабатывает, как "
                  "только жертва клонировала репозиторий и запустила агента",
             size=11.3, italic=True, color=DEEP, line_spacing=1.28)
    failure_card(s, 0.55, 3.7, 12.23, 1.35, icon_name="alert-octagon",
                 header_text="CVE-2026-21852",
                 body="подменённый базовый адрес API в чужом файле настроек перехватывал ключ "
                      "пользователя в открытом виде — тоже до подтверждения доверия.", body_size=11.5)
    dashed_box(s, 0.55, 5.2, 12.23, 1.7, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.8, 5.35, 11.7, 1.4,
             text="Обе закрыты. Но официальная документация прямо перечисляет, что именно "
                  "запускается ДО прохождения диалога доверия — и хуки в этом списке есть. Это "
                  "осознанный задокументированный компромисс, а не недоработка.",
             size=14.5, color=DEEP, line_spacing=1.36, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s30"))


def build_s31(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 3 · Провал, слои 2–3", "Когда гейт не срабатывает, не происходит ничего — а именно так выглядит и успешно пройденный гейт",
           title_size=16.5)
    numbered_card(s, 0.55, 1.85, 12.23, 2.15, [
        "одно невалидное условие срабатывания отключает ВСЕ хуки файла целиком",
        "скрипт хука удалён, переименован или потерял право на выполнение",
        "условие не совпало из-за регистра или незаякоренного шаблона",
        "таймаут — это тихое «разрешить»",
        "вызовы инструментов субагента не запускают хуки родительской сессии",
    ], size=11.3)
    headers = ["Обход намерением", "Механика"]
    rows = [
        ["git switch feature-x && git commit …", "получает отказ по СТАРОЙ ветке — хук читает ветку до выполнения всей команды"],
        ["запрет на команду чтения секрета", "не мешает прочитать файл инструментом чтения шагом раньше"],
    ]
    reveal_table(s, 0.55, 4.15, 12.23, 1.4, headers, rows, [0.4, 0.6], header_size=10.5, cell_size=10.5)
    criterion_plate(s, 0.55, 5.7, 12.23, 1.15, [
        "проверку дешевле сделать в сборке/линтере", "правило по сути не механизируемо",
        "соло-разработчик с низким радиусом поражения",
        "хук — не отдельный слот, а механическое усиление слоя правил"], size=10.5, gold_last=True)
    speaker_notes(s, load_notes("s31"))


# ============================================================
# Ступень 4 — Скилл (s32-s38)
# ============================================================

def build_s32(p):
    build_stage_divider(p, "s32", stage_num=4, title="Ступень 4 · скилл",
        meaning="Процедура, которая грузится только тогда, когда нужна",
        tag="1 задача на исправление · 307 подтверждённых случаев вреда · аудит 3984 скиллов")


def build_s33(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 4 · Сценарий-боль", "Файл инструкций облагает налогом каждый запрос процедурой, нужной в 1 сессии из 10",
           title_size=16)
    ocean_box(s, 0.55, 1.8, 12.23, 1.15)
    text_box(s, 0.8, 1.9, 6.3, 0.95, text="14 строк → 54 строки", size=22, bold=True, color=DEEP,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 7.0, 1.9, 5.5, 0.95,
             text="ориентир 200 · деплой ≈ 1 сессия из 10", size=13.5, italic=True, color=SLATE,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.3)
    numbered_card(s, 0.55, 3.1, 12.23, 1.0, [
        "собрать → прогнать тест формы → опубликовать → открыть прод-URL и отправить заявку руками → записать в журнал"], size=11.5)
    gold_callout(s, 0.55, 4.25, 12.23, 1.0,
                 "«В файле инструкций накопилась процедура деплоя на сорок строк. Она нужна раз в "
                 "две недели, а грузится в каждую сессию. Куда её вынести — и как сделать так, чтобы "
                 "агент сам понял, когда её открыть?»", size=12.5)
    option_row(s, 0.55, 5.4, 12.23, 0.55,
               ["оставить\nкак есть", "отдельный файл\n+ импорт", "отдельный файл,\nнапоминать вручную",
                "скилл с\nописанием-триггером", "хук"], size=10, highlight_idx=3)
    text_box(s, 0.55, 6.15, 12.23, 0.5,
             text="«сделаю хуком» — продуктивная путаница: хук исполняет среда, скилл остаётся знанием, которое можно не учесть",
             size=11.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s33"))


def build_s34(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 4 · Задача на исправление", "Описание — единственный канал, по которому модель выбирает нужный скилл среди потенциально сотни установленных",
           title_size=16)
    hw = 5.85
    terminal_card(s, 0.55, 1.9, hw, 1.5, [
        ("deploy: deploy", DENY_RED_SAFE, True),
    ], title="фронтматтер", size=16)
    text_box(s, 0.55, 3.5, hw, 0.35, text="система подставила имя файла вместо отсутствующего описания",
             size=10.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    rx = 0.55 + hw + 0.33
    ocean_box(s, rx, 1.9, hw, 1.5)
    multipara_box(s, rx + 0.2, 1.9 + 0.15, hw - 0.4, 1.2, [
        {"text": "«Helps with documents»", "size": 13, "color": SLATE, "strike": True,
         "align": PP_ALIGN.CENTER, "space_after": 6},
        {"text": "«Processes data»", "size": 13, "color": SLATE, "strike": True,
         "align": PP_ALIGN.CENTER, "space_after": 6},
        {"text": "«Does stuff with files»", "size": 13, "color": SLATE, "strike": True,
         "align": PP_ALIGN.CENTER},
    ])
    gold_callout(s, 0.55, 3.95, 12.23, 1.25,
                 "«Перед вами скилл, чьё описание — его собственное имя. Описание — единственный "
                 "канал, по которому модель выбирает нужный скилл среди потенциально сотни "
                 "установленных. Что именно вы допишете, чтобы он начал срабатывать?»", size=12.5)
    option_row(s, 0.55, 5.4, 12.23, 0.9, ["что делает", "когда\nиспользовать", "когда НЕ\nиспользовать"], size=14)
    speaker_notes(s, load_notes("s34"))


def build_s35(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 4 · Совместное формирование, ход 3", "Описание — это поисковый запрос вашего будущего «я», забывшего детали через полгода",
           title_size=16.5)
    ocean_box(s, 0.55, 1.9, 12.23, 2.3)
    paras = [
        {"text": "[что делает] ", "size": 13, "bold": True, "color": MID, "space_after": 4},
        {"text": "«Деплоит лендинг signup-landing на прод — сборка, smoke-тест формы, "
                 "публикация, проверка прод-URL. ", "size": 13, "color": DEEP, "space_after": 4},
        {"text": "[когда использовать] ", "size": 13, "bold": True, "color": TEAL, "space_after": 4},
        {"text": "Используй, когда пользователь просит задеплоить, выкатить или опубликовать сайт — ",
         "size": 13, "color": DEEP, "space_after": 4},
        {"text": "[когда НЕ использовать] ", "size": 13, "bold": True, "color": GOLD_DARK, "space_after": 4},
        {"text": "не для обычных правок кода без деплоя.»", "size": 13, "color": DEEP},
    ]
    # multipara_box treats each dict as its own paragraph; use one flowing paragraph via a single textbox instead
    tb = s.shapes.add_textbox(Inches(0.75), Inches(2.05), Inches(11.8), Inches(1.7))
    tf = tb.text_frame; tf.word_wrap = True
    p0 = tf.paragraphs[0]; p0.line_spacing = 1.4
    for cfg in paras:
        r = p0.add_run(); r.text = cfg["text"]
        r.font.size = Pt(cfg["size"]); r.font.bold = cfg.get("bold", False)
        r.font.color.rgb = cfg["color"]; r.font.name = FONT_BODY
    text_box(s, 0.75, 3.85, 11.8, 0.3, text="так и лежит в демо-репозитории, слово в слово",
             size=10.5, italic=True, color=SLATE)
    ocean_box(s, 0.55, 4.4, 12.23, 1.5, fill=SURFACE, stroke=TEAL, stroke_pt=1.1)
    text_box(s, 0.75, 4.55, 11.8, 0.3, text="ТЕЛО СКИЛЛА · ПЯТЬ ШАГОВ", size=11, bold=True, color=TEAL)
    text_box(s, 0.75, 4.9, 11.8, 0.9,
             text="собрать → прогнать тест формы → опубликовать → открыть прод-URL и отправить "
                  "заявку руками → записать в журнал, что задеплоено (единственный новый)",
             size=12.5, color=DEEP, line_spacing=1.3)
    speaker_notes(s, load_notes("s35"))


def build_s36(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 4 · Решение", "Процедура переезжает целиком: сорок строк вырезаются из файла инструкций в тот же момент",
           title_size=17)
    left_w = 6.85
    code_card(s, 0.55, 1.85, left_w, 4.9, [
        ("---", CODE_MUTED),
        ("name: deploy", CODE_FG),
        ("description: Деплоит лендинг signup-landing на", GOLD),
        ("  прод — сборка, smoke-тест формы, публикация,", GOLD),
        ("  проверка прод-URL. Используй, когда", GOLD),
        ("  пользователь просит задеплоить, выкатить", GOLD),
        ("  или опубликовать сайт — не для обычных", GOLD),
        ("  правок кода без деплоя.", GOLD),
        ("---", CODE_MUTED),
        ("", CODE_FG),
        ("# deploy", TEAL, True),
        ("1. Собрать: npm run build (код 0).", CODE_FG),
        ("2. Прогнать smoke-тест: npx playwright test.", CODE_FG),
        ("3. Опубликовать: wrangler pages deploy dist", CODE_FG),
        ("   --project-name signup-landing.", CODE_FG),
        ("4. Открыть прод-URL, вручную отправить форму.", CODE_FG),
        ("5. Записать в Tasks/<date>_<slug>/log.md.", CODE_FG),
    ], size=10.6, line_spacing=1.24)
    rx = 0.55 + left_w + 0.3
    rw = 12.23 - left_w - 0.3
    terminal_card(s, rx, 1.9, rw, 2.0, [
        ("AGENTS.md", CODE_FG), ("CLAUDE.md", CODE_FG), ("DECISIONS.md", CODE_FG),
        (".claude/settings.json", CODE_FG), (".claude/skills/deploy/SKILL.md", GOLD, True),
    ], title="дерево ступени 4", size=10.5)
    dashed_box(s, rx, 4.1, rw, 2.15, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, rx + 0.18, 4.25, rw - 0.36, 1.85,
             text="переехало, а не скопировалось:\n\nсорок строк вырезаются из файла "
                  "инструкций в тот же момент, когда появляется скилл",
             size=13, bold=True, color=GOLD_DARK, line_spacing=1.35)
    speaker_notes(s, load_notes("s36"))


def build_s37(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 4 · Три уровня и две проверки", "Скилл проверяется в обе стороны: что срабатывает, когда надо, и что молчит, когда не надо",
           title_size=17)
    headers = ["Уровень", "Когда грузится", "Стоимость", "Содержимое"]
    rows = [
        ["1. Метаданные", "всегда, при старте", "≈100 токенов", "имя + описание"],
        ["2. Инструкции", "только при срабатывании", "<5000 токенов", "тело файла скилла"],
        ["3. Ресурсы и код", "только при обращении", "0, пока не открыт", "вложенные файлы, скрипты"],
    ]
    reveal_table(s, 0.55, 1.85, 12.23, 1.95, headers, rows, [0.2, 0.28, 0.24, 0.28], header_size=11, cell_size=11)
    hw = 5.85
    failure_card(s, 0.55, 4.0, hw, 1.55, icon_name="check-circle-2",
                 header_text="Положительная проверка",
                 body="в новой сессии попросить «задеплой сайт» — скилл должен открыться сам",
                 body_size=12)
    rx = 0.55 + hw + 0.33
    dashed_box(s, rx, 4.0, hw, 1.55, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, rx + 0.22, 4.12, hw - 0.44, 0.34, text="ОТРИЦАТЕЛЬНАЯ ПРОВЕРКА · эту обычно пропускают",
             size=10.5, bold=True, color=GOLD_DARK)
    text_box(s, rx + 0.22, 4.5, hw - 0.44, 0.95,
             text="в новой сессии попросить починить мелкий баг в вёрстке — скилл открываться НЕ должен",
             size=12, color=DEEP, line_spacing=1.28)
    speaker_notes(s, load_notes("s37"))


def build_s38(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 4 · Провал / ограничение", "Скиллы вредят не тогда, когда очевидно нерелевантны, а ровно тогда, когда кажутся релевантными",
           title_size=17)
    headers = ["Замер (SkillsBench/SWE-Skills-Bench, arXiv:2608.11888)", "Значение"]
    rows = [
        ["подтверждённых случаев сбоя, вызванного скиллом", "307"],
        ["функциональных провалов, из них 68,8% (86 из 125) — кажущиеся релевантными", "125"],
        ["регрессий по стоимости, до +451% токенов", "182"],
        ["падение доли успеха на задачах", "16 из 84"],
    ]
    reveal_table(s, 0.55, 1.82, 6.0, 2.15, headers, rows, [0.72, 0.28], header_size=9.3, cell_size=10,
                 row_highlight={1: "gold"})
    rx = 6.78
    ocean_box(s, rx, 1.82, 6.0, 2.15, fill=SURFACE, stroke=TEAL, stroke_pt=1.1)
    text_box(s, rx + 0.2, 1.95, 5.6, 1.9,
             text="скилл как чужой код: аудит 3984 скиллов (5 фев 2026) — 36% с изъяном, 13,4% "
                  "(534) критических; 76 подтверждённых нагрузок, 91% с инъекцией в промпт; "
                  "февраль 2026 — первая координированная кампания, 30+ скиллов в волне.",
             size=10.6, color=DEEP, line_spacing=1.28)
    dashed_box(s, 0.55, 4.15, 12.23, 0.75, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.75, 4.15, 11.8, 0.75,
             text="динамическая подстановка контекста: команда выполняется, а вывод попадает в "
                  "контекст ДО того, как модель увидела сам скилл", size=12.5, italic=True,
             color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE)
    criterion_plate(s, 0.55, 5.1, 12.23, 1.75, [
        "нужно каждой сессии — это файл инструкций", "процедура одноразовая — дешевле попросить подробно",
        "правило недопустимо нарушить ни разу — это хук", "нужен изолированный бюджет контекста — субагент",
        "количество скиллов — не сигнал качества, а сигнал будущей проблемы выбора"], size=10.3)
    speaker_notes(s, load_notes("s38"))


# ============================================================
# Ступень 5 — Доступ наружу / MCP (s39-s47)
# ============================================================

def build_s39(p):
    build_stage_divider(p, "s39", stage_num=5, title="Ступень 5 · доступ наружу (MCP)",
        meaning="Первый блок, который смотрит за пределы репозитория",
        tag="4 хода совместного формирования · 7 замеров стоимости · 3 слоя провала · рамка смертельного трио")


def build_s40(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 5 · Сценарий-боль", "Правильный ответ — не одна проверка, а последовательность из трёх, и порядок имеет значение",
           title_size=17)
    ocean_box(s, 0.55, 1.8, 12.23, 1.25)
    text_box(s, 0.8, 1.92, 11.7, 1.0,
             text="Сайт живёт третий месяц. Заказчик заводит задачи прямо в репозитории. Почти "
                  "каждая сессия начинается одинаково: открыть браузер, скопировать текст задачи, "
                  "вставить в чат — и скопировать результат обратно в комментарий. Несколько раз в неделю.",
             size=12, color=DEEP, line_spacing=1.26, anchor=MSO_ANCHOR.MIDDLE)
    gold_callout(s, 0.55, 3.2, 12.23, 1.05,
                 "«Агенту теперь регулярно нужно смотреть открытые issue репозитория и готовить "
                 "черновики правок. Вы почти готовы подключить официальный сервер доступа к "
                 "трекеру. Что вы проверите ДО того, как это сделать?»", size=12.5)
    option_row(s, 0.55, 4.4, 12.23, 0.58,
               ["ничего — сервер\nофициальный", "сколько токенов\nон добавит",
                "какие права\nдаю токену", "не хватит ли\nобычной команды",
                "сколько у сервера\nзвёзд"], size=10.3)
    text_box(s, 0.55, 5.15, 12.23, 0.35, text="ПОСЛЕДОВАТЕЛЬНОСТЬ ИЗ ТРЁХ ПРОВЕРОК",
             size=11, bold=True, color=TEAL, align=PP_ALIGN.CENTER)
    numbered_card(s, 0.55, 5.55, 12.23, 1.3, [
        "нужно ли подключение вообще", "с какими правами", "по какой цене в контексте"], size=13.5)
    speaker_notes(s, load_notes("s40"))


def build_s41(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 5 · Совместное формирование, ходы 1–2", "Из всего, что даёт широкий персональный токен, нашему списку операций нужен один репозиторий и две операции",
           title_size=15)
    hw = 5.85
    numbered_card(s, 0.55, 1.9, hw, 2.6, [
        "читать открытые issue", "писать комментарий к issue", "создавать черновик правки"], size=13)
    rx = 0.55 + hw + 0.33
    ocean_box(s, rx, 1.9, hw, 2.6)
    items = [("все репозитории пользователя, включая приватные", True, True),
             ("чтение и запись", True, False),
             ("управление настройками", True, False),
             ("удаление", True, False)]
    iy = 2.1
    for text, strike, emph in items:
        text_box(s, rx + 0.2, iy, hw - 0.4, 0.5, text=text,
                 size=13.5 if emph else 12.5, bold=emph, color=SLATE, strike=strike, line_spacing=1.15)
        iy += 0.58
    gold_callout(s, 0.55, 4.7, 12.23, 1.1,
                 "остаётся: один репозиторий · чтение issue · создание черновика правки", size=15,
                 align=PP_ALIGN.CENTER)
    text_box(s, 0.55, 6.0, 12.23, 0.4, text="«Запомните вид этого экрана»", size=13, italic=True,
             color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s41"))


def build_s42(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 5 · Совместное формирование, ходы 3–4", "Проверенный сервер идёт в репозиторий и проходит ревью; непроверенный эксперимент остаётся только у вас",
           title_size=15)
    hw = 5.85
    ocean_box(s, 0.55, 1.95, hw, 1.9)
    text_box(s, 0.75, 2.1, hw - 0.4, 0.4, text="«Где хранить ключ?»", size=13.5, bold=True, color=MID)
    code_card(s, 0.55 + 0.2, 2.6, hw - 0.4, 1.1, [
        ('"GITHUB_PERSONAL_ACCESS_TOKEN":', CODE_FG),
        ('  "${GITHUB_PAT}"', GOLD),
    ], size=12)
    rx = 0.55 + hw + 0.33
    option_row(s, rx, 1.95, hw, 1.9,
               ["только у меня\nна этой машине", "в репозиторий,\nдля всех",
                "глобально во всех\nмоих проектах"], size=11)
    ocean_box(s, 0.55, 4.05, 12.23, 1.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.1)
    text_box(s, 0.75, 4.18, 11.8, 1.3,
             text="в репозиторий — для проверенного сервера: подключение становится кодом, видно "
                  "в ревью. Только у меня — для эксперимента: непроверенный сервер не коммитят в "
                  "проект сразу.", size=12.5, color=DEEP, line_spacing=1.3)
    dashed_box(s, 0.55, 5.8, 12.23, 0.95, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.75, 5.8, 11.8, 0.95,
             text="область по умолчанию — личная, не проектная. Чтобы подключение стало кодом "
                  "репозитория, область надо указать явно.", size=12.5, italic=True,
             color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s42"))


def build_s43(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 5 · Решение", "В файле подключения четыре строки существа, и одна из них — о том, откуда берётся ключ, а не какой он",
           title_size=17)
    left_w = 6.85
    code_card(s, 0.55, 1.85, left_w, 3.45, [
        ("{", CODE_FG),
        ('  "mcpServers": {', CODE_FG),
        ('    "github": {', CODE_FG),
        ('      "command": "npx",             // чем запускается', GOLD),
        ('      "args": ["-y",', GOLD),
        ('        "@modelcontextprotocol/server-github"],  // что', GOLD),
        ('      "env": {', CODE_FG),
        ('        "GITHUB_PERSONAL_ACCESS_TOKEN":', GOLD),
        ('          "${GITHUB_PAT}"          // откуда ключ', GOLD),
        ("      }", CODE_FG),
        ("    }", CODE_FG),
        ("  }", CODE_FG),
        ("}", CODE_FG),
    ], size=10.3, line_spacing=1.22)
    dashed_box(s, 0.55, 5.45, left_w, 1.25, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.75, 5.45, left_w - 0.4, 1.25,
             text="за пределами файла: какие права у ключа — один репозиторий, а не вся "
                  "учётная запись. Этого в файле нет, и это самое важное.", size=11.5, italic=True,
             color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.28)
    rx = 0.55 + left_w + 0.3
    rw = 12.23 - left_w - 0.3
    terminal_card(s, rx, 1.9, rw, 4.35, [
        ("AGENTS.md", CODE_FG), ("CLAUDE.md", CODE_FG), ("DECISIONS.md", CODE_FG),
        (".claude/settings.json", CODE_FG), (".claude/skills/deploy/SKILL.md", CODE_FG),
        (".mcp.json", GOLD, True), ("index.html …", CODE_FG),
    ], title="дерево ступени 5 · первый блок, смотрящий наружу", size=11)
    speaker_notes(s, load_notes("s43"))


def build_s44(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 5 · Цена в токенах", "Одно и то же действие стоит 1365 токенов командой в терминале и 44026 через инструмент сервера",
           title_size=16)
    headers = ["Примитив", "Кто инициирует", "Как выглядит"]
    rows = [
        ["Инструменты", "модель — сама решает", "«прочитать открытые issue»"],
        ["Ресурсы", "приложение — по явному упоминанию", "пользователь вставляет ссылку"],
        ["Подсказки", "человек — явной командой", "выбор сценария из меню"],
    ]
    reveal_table(s, 0.55, 1.8, 12.23, 1.55, headers, rows, [0.2, 0.36, 0.44], header_size=10.5, cell_size=10.3)
    headers2 = ["Замер", "Значение", "База сравнения"]
    rows2 = [
        ["связка из 5 серверов без поиска инструментов", "≈55 000 токенов определений", "без серверов — 0"],
        ["то же, с поиском инструментов (по умолчанию)", "минус >85%", "та же связка без поиска"],
        ["реалистичная связка 5 серверов", "26 224 = 13,1% окна 200К", "полное окно 200К"],
        ["аудит 11 серверов (137 инструментов)", "22 945 токенов до сообщения", "пустая сессия"],
        ["один крупный официальный сервер", "80 инструментов, 15 927 токенов", "остальные 10 серверов"],
        ["медиана по выборке 3 875 серверов", "≈2 064 токена на сервер", "сервер не подключён"],
        ["команда в терминале vs инструмент сервера", "1 365 против 44 026", "одинаковый результат"],
    ]
    reveal_table(s, 0.55, 3.45, 12.23, 3.4, headers2, rows2, [0.42, 0.28, 0.3], header_size=9.6, cell_size=9.4,
                 row_highlight={0: "gold", 6: "gold"})
    speaker_notes(s, load_notes("s44"))


def build_s45(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 5 · Ограничение", "Зелёный статус — утверждение о транспорте, а не о работе; проверяется фактическим вызовом",
           title_size=17)
    hw = 5.85
    failure_card(s, 0.55, 1.85, hw, 2.3, icon_name="check-circle-2",
                 header_text="Что индикатор ловит честно",
                 body="процесс не поднялся — «не удалось подключиться». Типичная причина: "
                      "регрессия в незафиксированной транзитивной зависимости.", body_size=12)
    rx = 0.55 + hw + 0.33
    numbered_card(s, rx, 1.85, hw, 2.3, [
        "сервер подключён, но инструментов не отдаёт",
        "сервер отвечает «успех», но не делает заявленного",
        "транспорт жив, а доступ отозван",
    ], size=11)
    dashed_box(s, 0.55, 4.35, 12.23, 1.55, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.8, 4.5, 11.7, 1.25,
             text="ловушка авторизации: если приложение доступа в тестовом статусе, поставщик "
                  "автоматически отзывает токен обновления через 7 дней неактивности. Все вызовы "
                  "падают с ошибкой авторизации — а список серверов продолжает показывать «подключено».",
             size=13, italic=True, color=GOLD_DARK, line_spacing=1.32, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s45"))


def build_s46(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 5 · Провал, слои 1–2", "Если хотя бы одного из трёх элементов нет — атака этого типа невозможна в принципе",
           title_size=17)
    ocean_box(s, 0.55, 1.8, 12.23, 1.65)
    text_box(s, 0.8, 1.92, 11.7, 1.4,
             text="26.05.2025 — публичный issue с вложенной инструкцией → агент читает issue в "
                  "рамках обычной работы → широкий токен даёт доступ к приватным репозиториям → "
                  "содержимое публикуется в автоматически созданном публичном черновике правки.",
             size=12, color=DEEP, line_spacing=1.28, anchor=MSO_ANCHOR.MIDDLE)
    dashed_box(s, 0.55, 3.55, 12.23, 0.55, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.8, 3.55, 11.7, 0.55,
             text="CVE не присвоен — это не баг кода, а токсичный поток агента",
             size=11.5, italic=True, color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE)
    gold_callout(s, 0.55, 4.25, 12.23, 2.35, "", size=1)  # background frame
    text_box(s, 0.75, 4.4, 11.8, 0.35, text="«СМЕРТЕЛЬНОЕ ТРИО» (Саймон Уиллисон, 16.06.2025)",
             size=12.5, bold=True, color=GOLD_DARK, align=PP_ALIGN.CENTER)
    circ_labels = ["доступ к приватным\nданным", "обработка недоверенного\nвнешнего контента", "канал, по которому\nможно отправить наружу"]
    gap = 0.3
    cw = (11.0 - gap * 2) / 3
    cx = 0.55 + (12.23 - (cw * 3 + gap * 2)) / 2
    for lbl in circ_labels:
        shp = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx), Inches(4.85), Inches(cw), Inches(1.15))
        shp.fill.solid(); shp.fill.fore_color.rgb = RGBColor(0x0B, 0x14, 0x3A)
        shp.line.color.rgb = GOLD; shp.line.width = Pt(1.6)
        disable_shadow(shp)
        tf = shp.text_frame; tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        pp = tf.paragraphs[0]; pp.alignment = PP_ALIGN.CENTER
        r = pp.add_run(); r.text = lbl
        r.font.size = Pt(11); r.font.bold = True; r.font.color.rgb = WHITE; r.font.name = FONT_BODY
        cx += cw + gap
    text_box(s, 0.75, 6.15, 11.8, 0.35, text="не хватает хотя бы одного — атака невозможна в принципе",
             size=12, italic=True, bold=True, color=GOLD_DARK, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s46"))


def build_s47(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 5 · Провал, слой 3", "Одобрение инструмента не действует бессрочно: доверие привязано к имени, а не к содержимому",
           title_size=16)
    ocean_box(s, 0.55, 1.82, 12.23, 1.25)
    text_box(s, 0.8, 1.95, 11.7, 1.0,
             text="в момент одобрения сервер отдаёт безобидный набор инструментов, пользователь "
                  "одобряет  →  после одобрения то же имя инструмента, другое поведение. Большинство "
                  "клиентов не перепроверяют определения инструмента при каждом вызове.",
             size=12, color=DEEP, line_spacing=1.26, anchor=MSO_ANCHOR.MIDDLE)
    failure_card(s, 0.55, 3.25, 12.23, 1.35, icon_name="alert-octagon",
                 header_text="postmark-mcp, сентябрь 2025",
                 body="вредоносный пакет несколько недель незаметно ставил скрытую копию каждого "
                      "отправляемого письма на адрес атакующего. Никакого взлома — обновление уже "
                      "одобренного инструмента.", body_size=11.5)
    criterion_plate(s, 0.55, 4.75, 12.23, 2.1, [
        "хватает обычной команды (1365 против 44026 токенов)",
        "разовое или редкое действие, а не повторяющийся доступ",
        "снимка данных достаточно", "доступ нужен только из этой сессии",
        "не готовы поддерживать ещё один процесс с доступом к секретам",
        "стоп-критерий: если подключение достраивает третий элемент трио — не подключайте"],
        size=10.6, gold_last=True)
    speaker_notes(s, load_notes("s47"))


# ============================================================
# Ступень 6 — Кастомный субагент (s48-s56)
# ============================================================

def build_s48(p):
    build_stage_divider(p, "s48", stage_num=6, title="Ступень 6 · кастомный субагент",
        meaning="Делегировать вообще — уже бесплатно; заводить стоит роль с отнятыми правами",
        tag="3 хода совместного формирования · 1 настоящий вердикт BLOCK · таксономия отказов по 1600+ трассам")


def build_s49(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 6 · Такт 1 и такт 2", "Независимость определяется происхождением контекста, а не тоном просьбы",
           title_size=17)
    hw = 5.85
    failure_card(s, 0.55, 1.9, hw, 3.1, icon_name="rotate-ccw",
                 header_text="Такт 1 · самопроверка",
                 body="Правка готова в src/validate.js. Перед выкаткой разработчик просит ТУ ЖЕ "
                      "сессию перепроверить себя «максимально придирчиво». Она честно старается — "
                      "и остаётся тем же контекстом рассуждений, той же цепочкой решений, тем же "
                      "слепым пятном, которое эту правку и породило.", body_size=12)
    rx = 0.55 + hw + 0.33
    ocean_box(s, rx, 1.9, hw, 3.1, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
    text_box(s, rx + 0.22, 1.9 + 0.18, hw - 0.44, 0.34, text="ТАКТ 2 · ОТДЕЛЬНЫЙ АГЕНТ",
             size=12.5, bold=True, color=TEAL)
    text_box(s, rx + 0.22, 1.9 + 0.58, hw - 0.44, 1.2,
             text="Задача уходит в собственное контекстное окно, история рассуждений не видна, "
                  "возвращается только итог.", size=12, color=DEEP, line_spacing=1.3)
    dashed_box(s, rx + 0.16, 1.9 + 1.85, hw - 0.32, 1.05, fill=GOLD_TINT, stroke=GOLD_DARK, stroke_pt=1.6)
    text_box(s, rx + 0.32, 1.9 + 1.85, hw - 0.64, 1.05,
             text="это уже работает из коробки — заводить файл не нужно", size=13, bold=True,
             color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, line_spacing=1.3)
    speaker_notes(s, load_notes("s49"))


def build_s50(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 6 · Такт 3", "Роль приходится переизобретать при каждом вызове, а у универсального субагента есть лишние права",
           title_size=17)
    hw = 5.85
    failure_card(s, 0.55, 1.82, hw, 1.55, icon_name="repeat",
                 header_text="1. Роль собирается заново каждый раз",
                 body="Что проверять, на что смотреть, в каком виде отвечать — вы пишете это в "
                      "третий раз за неделю, каждый раз чуть иначе. Три вердикта несравнимы.", body_size=11)
    rx = 0.55 + hw + 0.33
    failure_card(s, rx, 1.82, hw, 1.55, icon_name="alert-triangle",
                 header_text="2. Полный набор инструментов — включая правку",
                 body="Один раз субагент не просто нашёл проблему, а сам её поправил — по-своему. "
                      "Разработчик узнал об этом из diff.", body_size=11)
    gold_callout(s, 0.55, 3.55, 12.23, 1.15,
                 "«Вы третий раз за неделю просите проверить правку отдельным агентом — и "
                 "каждый раз заново пишете, что проверять. Делегировать вы уже умеете, это ничего "
                 "не стоит. Что теперь нужно завести — и зачем?»", size=12.5)
    option_row(s, 0.55, 4.85, 12.23, 0.6,
               ["ничего — делегирование\nуже есть", "писать запрос\nподробнее каждый раз",
                "сохранить запрос\nв скилл", "кастомный субагент:\nимя + огранич. права",
                "позвать\nколлегу"], size=10, highlight_idx=3)
    text_box(s, 0.55, 5.6, 12.23, 1.1,
             text="«ничего не надо» — правильно НАПОЛОВИНУ: большинству и правда не надо ничего "
                  "заводить; ломается на повторяемости роли и на правах. «Сохраню как скилл» — "
                  "скилл не даёт изоляции контекста и прав.",
             size=11.5, italic=True, color=SLATE, line_spacing=1.3, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s50"))


def build_s51(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 6 · Совместное формирование, ход 2", "«Не правь сам» в теле роли — просьба; строка ограничения инструментов — отнятая возможность",
           title_size=17)
    numbered_card(s, 0.55, 1.85, 12.23, 1.1, [
        "Какие инструменты нужны ревьюеру, чтобы найти проблему в правке?",
        "А править файлы ему нужно?"], size=12.5)
    items = [("чтение файлов ✓", False), ("поиск по содержимому ✓", False),
             ("поиск файлов по именам ✓", False), ("правка файлов", True), ("запись файлов", True)]
    ix = 0.55
    iy = 3.1
    for text, strike in items:
        text_box(s, ix, iy, 12.23, 0.3, text=text, size=12.5, color=(SLATE if strike else DEEP),
                 strike=strike, bold=not strike)
        iy += 0.34
    dashed_box(s, 0.55, iy + 0.08, 12.23, 0.5, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.75, iy + 0.08, 11.8, 0.5, text="остаётся: tools: Read, Grep, Glob",
             size=15, bold=True, color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE, font=FONT_MONO)
    iy2 = iy + 0.08 + 0.5 + 0.18
    table_card(s, 0.55, iy2, 12.23, max(1.05, 6.9 - iy2),
               ["в теле роли: «ты не правишь код сам»", "строка tools: Read, Grep, Glob"],
               [["просьба", "отнятая возможность"]], [0.5, 0.5], header_size=11.5, cell_size=13,
               row_align=[PP_ALIGN.CENTER, PP_ALIGN.CENTER])
    speaker_notes(s, load_notes("s51"))


def build_s52(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 6 · Совместное формирование, ход 3", "Пустой список находок — валидный PASS, а BLOCK требует хотя бы одной конкретной находки",
           title_size=16)
    gold_callout(s, 0.55, 1.85, 12.23, 0.75,
                 "«Что должно быть в ответе, чтобы вердикты трёх разных проверок можно было "
                 "сравнить?»", size=14.5, align=PP_ALIGN.CENTER)
    numbered_card(s, 0.55, 2.8, 12.23, 2.3, [
        "Вердикт первой строкой — PASS или BLOCK",
        "«Что проверено» конкретно — какие файлы прочитаны",
        "Находки: что не так, где, почему важно"], size=14)
    table_card(s, 0.55, 5.3, 12.23, 1.35,
               ["пустой список находок", "BLOCK без конкретной исправимой находки"],
               [["валидный PASS", "не BLOCK"]], [0.5, 0.5], header_size=12, cell_size=15,
               row_align=[PP_ALIGN.CENTER, PP_ALIGN.CENTER])
    speaker_notes(s, load_notes("s52"))


def build_s53(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 6 · Решение", "Строка ограничения инструментов короче всего остального в файле и делает больше всего",
           title_size=18)
    left_w = 6.85
    code_card(s, 0.55, 1.85, left_w, 4.7, [
        ("---", CODE_MUTED),
        ("name: diff-reviewer", CODE_FG),
        ("description: Независимый ревьюер diff'ов. Видит", CODE_MUTED),
        ("  только сам diff и критерии приёмки, не", CODE_MUTED),
        ("  рассуждения автора. Используй перед мержем", CODE_MUTED),
        ("  любого нетривиального изменения.", CODE_MUTED),
        ("tools: Read, Grep, Glob", GOLD, True),
        ("---", CODE_MUTED),
        ("", CODE_FG),
        ("# diff-reviewer", TEAL, True),
        ("", CODE_FG),
        ("Ты не правишь код сам — только находишь", CODE_FG),
        ("проблемы. Начни ответ строкой:", CODE_FG),
        ("VERDICT: PASS | BLOCK", CODE_FG),
        ("", CODE_FG),
        ("Затем: что проверено (конкретно), находки.", CODE_FG),
        ("Пустой список находок — валидный PASS.", CODE_FG),
    ], size=10.6, line_spacing=1.24)
    text_box(s, 0.55, 6.62, left_w, 0.3, text="короче всего остального — и делает больше всего",
             size=10.5, italic=True, color=GOLD_DARK, align=PP_ALIGN.CENTER)
    rx = 0.55 + left_w + 0.3
    rw = 12.23 - left_w - 0.3
    terminal_card(s, rx, 1.9, rw, 1.95, [
        ("AGENTS.md · CLAUDE.md · DECISIONS.md", CODE_FG),
        (".claude/settings.json", CODE_FG),
        (".claude/skills/deploy/SKILL.md", CODE_FG),
        (".mcp.json", CODE_FG),
        (".claude/agents/diff-reviewer.md", GOLD, True),
    ], title="дерево ступени 6", size=10)
    dashed_box(s, rx, 4.05, rw, 2.2, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, rx + 0.18, 4.2, rw - 0.36, 1.9,
             text="вызовы инструментов субагента по сообщённому поведению не запускают хуки "
                  "родительской сессии — без индикатора, что проверки были пропущены",
             size=12, italic=True, color=GOLD_DARK, line_spacing=1.32)
    speaker_notes(s, load_notes("s53"))


def build_s54(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 6 · Живое доказательство", "Ревьюер, видевший только diff, обнаружил, что правка вообще не является правкой",
           title_size=18)
    dashed_box(s, 0.55, 1.82, 12.23, 0.75, fill=GOLD_TINT, stroke=GOLD_DARK, stroke_pt=2.0)
    text_box(s, 0.75, 1.82, 11.8, 0.75, text="VERDICT: BLOCK", size=26, bold=True, color=GOLD_DARK,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    ocean_box(s, 0.55, 2.75, 12.23, 1.5)
    text_box(s, 0.75, 2.85, 11.8, 0.3, text="ПРОВЕРЕНО", size=11.5, bold=True, color=TEAL)
    text_box(s, 0.75, 3.15, 11.8, 1.0,
             text="полный diff src/validate.js, итоговое содержимое файла, поиск использований "
                  "isValidEmail по репозиторию (Grep), список файлов проекта (Glob), "
                  "AGENTS.md/CLAUDE.md — специфичных требований к формату не найдено.",
             size=11.3, color=DEEP, line_spacing=1.28)
    dashed_box(s, 0.55, 4.45, 12.23, 1.9, fill=SURFACE, stroke=GOLD_DARK, stroke_pt=1.4)
    text_box(s, 0.75, 4.58, 11.8, 0.3, text="НАХОДКА 1", size=11.5, bold=True, color=GOLD_DARK)
    text_box(s, 0.75, 4.9, 11.8, 1.35,
             text="«Функция добавлена, но нигде не подключена… isValidEmail нигде не используется "
                  "(ни в этом файле, ни где-либо ещё). То есть фактическое поведение формы этим "
                  "diff'ом не меняется… Diff добавляет мёртвый код, а не фикс.»",
             size=13.5, italic=True, color=DEEP, line_spacing=1.34)
    speaker_notes(s, load_notes("s54"))


def build_s55(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 6 · Провал, слои 1–2", "Отчёт субагента об успехе — это утверждение, а не доказательство",
           title_size=17)
    failure_card(s, 0.55, 1.82, 12.23, 2.15, icon_name="alert-triangle",
                 header_text="claude-code#67730 (2026) и #46727 (апрель 2026)",
                 body="Субагенты возвращали полностью галлюцинированные результаты при НУЛЕ "
                      "реальных вызовов инструментов — включая два выдуманных отчёта «обнаружена "
                      "инъекция в промпт». Смежно: систематические галлюцинации вопреки явной "
                      "инструкции подтверждать перед заявлением о завершении.", body_size=11.5,
                 footnote="родительская сессия доверяет отчёту и строит на нём план — ошибка становится фундаментом")
    headers = ["Категория причин (MAST, arXiv:2503.13657, 1600+ трасс, κ=0,88)", "Доля"]
    rows = [
        ["спецификация задачи и роли", "≈41,8%"],
        ["рассогласование между агентами", "≈36,9%"],
        ["верификация результата", "≈21,3%"],
    ]
    reveal_table(s, 0.55, 4.2, 12.23, 1.85, headers, rows, [0.75, 0.25], header_size=10.5, cell_size=12)
    text_box(s, 0.55, 6.18, 12.23, 0.6, text="доля провальных трасс — 41–87%; ни одна категория не про «модель ошиблась в факте»",
             size=12, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s55"))


def build_s56(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 6 · Провал, слой 3", "Прежде чем спорить о множителе, выясните базу: 15× и 3–10× — обе честные цифры",
           title_size=17)
    hw = 5.85
    ocean_box(s, 0.55, 1.85, hw, 1.75)
    text_box(s, 0.55, 1.95, hw, 0.6, text="15×", size=34, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, 0.55, 2.65, hw, 0.85, text="июнь 2025 · база: обычный чат", size=12.5, italic=True,
             color=SLATE, align=PP_ALIGN.CENTER)
    rx = 0.55 + hw + 0.33
    ocean_box(s, rx, 1.85, hw, 1.75)
    text_box(s, rx, 1.95, hw, 0.6, text="3–10×", size=34, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, rx, 2.65, hw, 0.85, text="январь 2026 · база: одноагентное решение той же задачи",
             size=12.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    text_box(s, 0.55, 3.75, 12.23, 0.4, text="разные базы, обе верны", size=14, bold=True,
             italic=True, color=GOLD_DARK, align=PP_ALIGN.CENTER)
    criterion_plate(s, 0.55, 4.35, 12.23, 2.5, [
        "шаги зависимы, нужен общий контекст", "не резать по фазам одной цепочки решений",
        "задача формулируется заново каждый раз — роли ещё нет", "«независимость» декларируется, но не проверяется",
        "рутинная и дешёвая задача, где надбавка не окупается",
        "главное: разовая проверка — делегируйте встроенным субагентом и не заводите файл"],
        size=10.6, gold_last=True)
    speaker_notes(s, load_notes("s56"))


# ============================================================
# Ступень 7 — Процесс (s57-s63)
# ============================================================

def build_s57(p):
    build_stage_divider(p, "s57", stage_num=7, title="Ступень 7 · процесс",
        meaning="Работу принимают на слово, потому что проверяемой альтернативы не существует",
        tag="3 хода совместного формирования · 3 слоя провала · 1 честное ограничение нашего же решения")


def build_s58(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 7 · Сценарий-боль", "Каждое отдельное утверждение может быть правдой — вместе они складываются в «готово», которого нет",
           title_size=16)
    dashed_box(s, 0.55, 1.78, 12.23, 0.75, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.75, 1.78, 11.8, 0.75,
             text="«Готово, форма отправляет заявку, все тесты прошли, можно показывать.»",
             size=15, bold=True, italic=True, color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)
    headers = ["«все тесты прошли»", "«форма отправляет заявку»", "«готово»"]
    rows = [["какие именно, когда, с каким выводом?", "на проде или только локально?", "по чьему критерию?"]]
    reveal_table(s, 0.55, 2.68, 12.23, 1.3, headers, rows, [0.34, 0.34, 0.32], header_size=11.5, cell_size=11)
    gold_callout(s, 0.55, 4.1, 12.23, 1.15,
                 "«Утро показа. Агент написал: ‘Готово…, можно показывать’. Что из этого вы можете "
                 "проверить ПРЯМО СЕЙЧАС, не читая переписку — и что для этого должно было "
                 "существовать ДО того, как агент это написал?»", size=12)
    option_row(s, 0.55, 5.37, 12.23, 0.55,
               ["поверю — он явно\nзакончил", "прогоню тесты\nсам", "спрошу\n«ты уверен?»",
                "открою прод и\nпроверю руками", "ссылка на коммит +\nжурнал"], size=10, highlight_idx=4)
    text_box(s, 0.55, 6.02, 12.23, 0.5,
             text="«спрошу, уверен ли» — худший из пяти: подхалимство даёт уверенное подтверждение и ноль новой информации",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.25)
    speaker_notes(s, load_notes("s58"))


def build_s59(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 7 · Совместное формирование, ходы 1–2", "Три вещи должны были появиться раньше слова «готово»",
           title_size=17)
    baskets_y = 1.9
    numbered_card(s, 0.55, baskets_y, 12.23, 2.15, [
        "план — до кода. Согласованный до того, как что-то написано.",
        "журнал — по ходу. Не восстановленный по памяти в конце.",
        "вердикт — от того, кто не писал этот код. «А этот у нас уже есть, и он не пустой — BLOCK по нашей же правке».",
    ], size=12.3)
    ocean_box(s, 0.55, 4.3, 12.23, 1.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.1)
    text_box(s, 0.75, 4.42, 11.8, 0.3, text="ХОД 2 · ТРИ ЭЛЕМЕНТА СТРОКИ ЖУРНАЛА", size=11, bold=True, color=TEAL)
    text_box(s, 0.75, 4.78, 11.8, 0.55, text="отметка времени  ·  конкретная выполненная команда  ·  её результат",
             size=14.5, bold=True, color=DEEP)
    text_box(s, 0.75, 5.35, 11.8, 0.35, text="«починил валидацию» — так проверить через неделю нечего",
             size=12, italic=True, color=SLATE, strike=True)
    speaker_notes(s, load_notes("s59"))


def build_s60(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 7 · Решение", "Оба артефакта существовали — и оба не сработали, потому что вердикт пришёл после слияния",
           title_size=17)
    hw = 5.85
    code_card(s, 0.55, 1.9, hw, 2.55, [
        ("## 2026-09-20T12:44:42+00:00", TEAL, True),
        ("Правка src/validate.js: добавлена функция", CODE_FG),
        ("isValidEmail, ужесточён regex — проверка", CODE_FG),
        ("точки в домене (заявка с опечаткой раньше", CODE_FG),
        ("проходила форму).", CODE_FG),
        ("Коммит cf58408 — git commit -m \"fix: tighten", GOLD),
        ("email validation regex …\"", GOLD),
    ], title="log.md", size=10.6, line_spacing=1.24)
    rx = 0.55 + hw + 0.33
    code_card(s, rx, 1.9, hw, 2.55, [
        ("Предмет: diff src/validate.js", CODE_FG),
        ("VERDICT: BLOCK", DENY_RED_SAFE, True),
        ("Проверено: 5 конкретных действий", CODE_FG),
        ("Находки: 3, первая блокирующая —", CODE_FG),
        ("«Diff добавляет мёртвый код, а не фикс»", GOLD),
    ], title="review.md", size=10.6, line_spacing=1.3)
    dashed_box(s, 0.55, 4.65, 12.23, 0.75, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.75, 4.65, 11.8, 0.75, text="слияние в основную ветку произошло РАНЬШЕ вердикта — ровно так выглядит обойдённый процесс",
             size=12.5, italic=True, bold=True, color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE)
    terminal_card(s, 0.55, 5.6, 12.23, 1.55, [
        ("Tasks/README.md · Tasks/review.md.template", CODE_FG),
        ("Tasks/2026-09-20_form-endpoint-fix/", GOLD, True),
        ("  ├── log.md   ├── review.md", GOLD),
    ], title="дерево ступени 7", size=10.5)
    speaker_notes(s, load_notes("s60"))


def build_s61(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 7 · Совместное формирование, ход 3", "Третий круг ревью по одному и тому же артефакту — не признак тщательности, а диагноз",
           title_size=17)
    gold_callout(s, 0.55, 1.85, 12.23, 0.75, "«Сколько кругов ревью?»", size=17, align=PP_ALIGN.CENTER)
    option_row(s, 0.55, 2.85, 12.23, 0.7, ["один", "два", "до победного"], highlight_idx=1, size=15)
    ocean_box(s, 0.55, 3.9, 12.23, 1.1, fill=SURFACE, stroke=TEAL, stroke_pt=1.1)
    text_box(s, 0.75, 3.9, 11.8, 1.1, text="BLOCK  →  починка  →  узкая перепроверка только изменённого",
             size=17, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    dashed_box(s, 0.55, 5.25, 12.23, 1.4, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.75, 5.38, 11.8, 1.15,
             text="третий круг по одному и тому же артефакту — ДИАГНОЗ: слишком широкая "
                  "ответственность, нет автопроверки, размытые критерии. Чинить надо так, чтобы "
                  "четвёртый круг стал структурно невозможен.",
             size=13, italic=True, color=GOLD_DARK, line_spacing=1.32, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s61"))


def build_s62(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 7 · Провал, слой 1", "Разница между 75,8% и 3% — это разница между наличием и отсутствием внешней проверки",
           title_size=16.5)
    headers = ["Условия (ICML 2026, arXiv:2606.09863)", "Доля провалов, отчитанных как «готово»"]
    rows = [
        ["кодинг-агенты, оценивающие себя сами", "75,8%"],
        ["однопользовательские домены другого бенчмарка", "45–48%"],
        ["домен с двойным контролем", "3%"],
        ["разброс между моделями", "13–79%"],
    ]
    reveal_table(s, 0.55, 1.85, 12.23, 2.25, headers, rows, [0.6, 0.4], header_size=11, cell_size=12,
                 row_highlight={0: "gold", 2: "gold"})
    ocean_box(s, 0.55, 4.25, 12.23, 0.85, fill=SURFACE, stroke=TEAL, stroke_pt=1.1)
    text_box(s, 0.75, 4.25, 11.8, 0.85, text="75,8% ↔ 3%  =  разница между наличием и отсутствием внешней проверки",
             size=13.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    dashed_box(s, 0.55, 5.25, 12.23, 1.4, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 0.75, 5.38, 11.8, 1.15,
             text="ни одна из пяти проверенных конфигураций модели-судьи не превысила AUROC 0,65. "
                  "Верификация должна проверять ФАКТ — файл существует, команда выполнена, тест "
                  "прошёл, — а не спрашивать другую модель, выглядит ли это завершённым.",
             size=12.5, italic=True, color=GOLD_DARK, line_spacing=1.3, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s62"))


def build_s63(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 7 · Провал, слои 2–3", "Гейт, который агент может отредактировать, — не гейт",
           title_size=18)
    numbered_card(s, 0.55, 1.8, 12.23, 1.4, [
        "трассировка вызовов в поисках ответа проверяющей функции",
        "перезапись функции замера времени",
        "патч самой функции оценки, чтобы она засчитывала любое решение успешным",
    ], size=11)
    headers = ["Условия (METR, 5 июня 2025)", "Частота"]
    rows = [["одна задача набора", "100% (21 из 21)"], ["в среднем по набору", "30,4% (39 из 128)"],
            ["широкий набор других задач", "0,7%"]]
    reveal_table(s, 0.55, 3.35, 6.0, 1.5, headers, rows, [0.62, 0.38], header_size=9.5, cell_size=10.5)
    dashed_box(s, 6.78, 3.35, 6.0, 1.5, fill=GOLD_TINT, stroke=GOLD_DARK)
    text_box(s, 6.98, 3.48, 5.6, 1.25,
             text="гейт, который агент может отредактировать, — не гейт. Заметки, которые агент "
                  "пишет сам, могут не исправлять ошибку, а закреплять её (эксперимент по "
                  "самоавторской памяти, arXiv:2605.29463).", size=11.5, italic=True, color=GOLD_DARK,
             line_spacing=1.28)
    ocean_box(s, 0.55, 5.0, 12.23, 0.7, fill=SURFACE, stroke=TEAL, stroke_pt=1.0)
    text_box(s, 0.75, 5.0, 11.8, 0.7,
             text="claude-code#51735: документированный, признанный урок не предотвратил повторения той же ошибки через 25 дней",
             size=11.5, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    criterion_plate(s, 0.55, 5.85, 12.23, 1.0, [
        "гейт исполняется вне видимости агента", "самоавторские заметки — не прививка",
        "проверка требует независимого от автора канала",
        "41% (35 из 84) запросов на слияние спринта — чистая бухгалтерия"], size=10.3, gold_last=True)
    speaker_notes(s, load_notes("s63"))


# ============================================================
# Закрытие занятия (s64-s65)
# ============================================================

def build_s64(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Закрытие", "Ни один из семи блоков не появился потому, что «так принято» — у каждого есть дата и сигнал",
           title_size=17)
    left_w = 5.5
    terminal_card(s, 0.55, 1.85, left_w, 3.65, [
        ("CLAUDE.md                 · ступень 1", GOLD),
        ("AGENTS.md                 · ступень 1", GOLD),
        ("DECISIONS.md               · ступень 2", GOLD),
        (".claude/settings.json      · ступень 3", GOLD),
        (".claude/skills/deploy/     · ступень 4", GOLD),
        ("  SKILL.md", CODE_MUTED),
        (".mcp.json                  · ступень 5", GOLD),
        (".claude/agents/            · ступень 6", GOLD),
        ("  diff-reviewer.md", CODE_MUTED),
        ("Tasks/                     · ступень 7", GOLD),
        ("index.html · package.json ·", CODE_MUTED),
        ("src/ · tests/", CODE_MUTED),
    ], title="финальное дерево · ступени семинара", size=10.2, line_spacing=1.25)
    rx = 0.55 + left_w + 0.3
    rw = 12.23 - left_w - 0.3
    ocean_box(s, rx, 1.85, rw, 3.65)
    text_box(s, rx + 0.2, 1.98, rw - 0.4, 0.28, text="КАРТА ЭКИПИРОВКИ · СЛОТЫ ЛЕКЦИИ, ЗАПОЛНЕНА",
             size=10.5, bold=True, color=TEAL)
    # NB (v2 fix — s64 dual-numbering readability, qa-reports/2026-09-21-v2):
    # left tree numbers count SEMINAR STAGES (1-7, "· ступень N"); these map
    # chips count LECTURE SLOTS (1-5, "слот N") — same digits, different axis.
    # Prefixing both with their own word ("ступень" / "слот") disambiguates a
    # skim-read without changing any content.
    recap_items = [
        ("слот 1", "память"), ("слот 2", "инструкции-правила"), ("слот 3", "скиллы"),
        ("слот 4", "субагенты"), ("слот 5", "доступ наружу (MCP)"), ("хук", "усиление слота 2"),
        ("процесс", "операционализация «проверяй»"),
    ]
    ry = 2.32
    row_h = (3.65 - 0.47 - 0.1) / len(recap_items)
    for num, label in recap_items:
        grey = num in ("хук", "процесс")
        chip_w = 0.95 if not grey else 0.9
        num_size = 9.5 if not grey else 11
        filled_rect(s, rx + 0.2, ry + 0.02, chip_w, row_h - 0.1,
                    RGBColor(0xE4, 0xE9, 0xEF) if grey else MID, radius=True, radius_adj=0.3)
        text_box(s, rx + 0.2, ry + 0.02, chip_w, row_h - 0.1, text=num, size=num_size, bold=True,
                 color=SLATE if grey else WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, rx + 0.2 + chip_w + 0.16, ry, rw - 0.4 - chip_w - 0.16, row_h, text=label,
                 size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        ry += row_h
    theses = [
        "Правило, заявленное обязательным без механической проверки в том же изменении, тихо умрёт.",
        "Барьер установлен не тогда, когда файл существует, а когда его видели сработавшим на реальном случае.",
        "Конфигурация — не коллекция. Бремя доказательства лежит на том, кто добавляет, а не на том, кто остаётся внизу.",
    ]
    numbered_card(s, 0.55, 5.65, 12.23, 1.2, theses, size=10.8)
    speaker_notes(s, load_notes("s64"))


def build_s65(p):
    s = blank(p)
    gradient_rect(s, 0, 0, SLIDE_W_IN, SLIDE_H_IN, [(0, DEEP), (55000, MID), (100000, LIGHT)])
    # Hero: same 7-stage ladder as opening (s01), now WITH names — closes the
    # emotional arc; >=40% of slide area.
    hero_x, hero_y, hero_w, hero_h = 0.55, 0.55, 12.23, 3.35  # ~41% area
    build_growth_staircase(s, hero_x, hero_y, hero_w, hero_h,
        bar_lo=(0x3A, 0x4A, 0x86), bar_hi=(0x6B, 0x7F, 0xC2), bar_gold=GOLD,
        label_color=RGBColor(0xD8, 0xE2, 0xF0), gold_label_color=GOLD,
        number_color=WHITE, gold_number_color=GOLD,
        sublabel_color=RGBColor(0x9C, 0xAE, 0xC9), baseline_color=RGBColor(0x4A, 0x5C, 0x96))
    q_y = hero_y + hero_h + 0.35
    filled_rect(s, 0.75, q_y, SLIDE_W_IN - 1.5, 1.9, RGBColor(0x0B, 0x14, 0x3A),
                stroke=GOLD, stroke_pt=1.6, radius=True, radius_adj=0.1)
    tb = s.shapes.add_textbox(Inches(1.05), Inches(q_y + 0.16), Inches(SLIDE_W_IN - 2.1), Inches(1.6))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    pp = tf.paragraphs[0]; pp.line_spacing = 1.32; pp.alignment = PP_ALIGN.CENTER
    r1 = pp.add_run()
    r1.text = ("«У каждого из вас есть свой рабочий или учебный репозиторий. Покажите пальцем в "
               "эту карту дважды. Первый раз — какая ступень там уже стоило бы появиться, судя "
               "по боли, которая у вас реально была, а не про запас. Второй раз — ")
    r1.font.size = Pt(14.5); r1.font.italic = True; r1.font.color.rgb = WHITE; r1.font.name = FONT_BODY
    r2 = pp.add_run()
    r2.text = "какая точно ещё рано.»"
    r2.font.size = Pt(15.5); r2.font.italic = True; r2.font.bold = True; r2.font.color.rgb = GOLD
    r2.font.name = FONT_BODY
    text_box(s, 0.75, q_y + 1.95, SLIDE_W_IN - 1.5, 0.4,
             text="Добавить умеет каждый; сегодня мы семь раз тренировали другое.",
             size=13, italic=True, bold=True, color=RGBColor(0xCF, 0xDC, 0xEC),
             align=PP_ALIGN.CENTER)
    # v2 fix (qa-reports/2026-09-21-v2, P2 #6) — link badge, per rework/
    # section-7-protsess.md §B.4: status open (dedicated clonable build is an
    # owner decision, brief.md open question #2), so this points at the
    # public base template instead, with the honest caption the source
    # mandates ("шаблон, не заполненная сборка") rather than promising an
    # artefact that doesn't exist yet.
    badge_w, badge_h = 9.6, 0.62
    badge_x, badge_y = (SLIDE_W_IN - badge_w) / 2, q_y + 2.42
    filled_rect(s, badge_x, badge_y, badge_w, badge_h, RGBColor(0x0B, 0x14, 0x3A),
                stroke=RGBColor(0x6B, 0x7F, 0xC2), stroke_pt=1.1, radius=True, radius_adj=0.35)
    icon(s, "link", "F0AB00", 64, badge_x + 0.22, badge_y + (badge_h - 0.28) / 2, 0.28)
    text_box(s, badge_x + 0.62, badge_y, badge_w - 0.84, badge_h,
             text="workain/agent-harness-registry — шаблон, не заполненная сборка "
                  "(отдельная клонируемая сборка курса — решение за владельцем)",
             size=10.5, italic=True, color=RGBColor(0xCF, 0xDC, 0xEC), anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.2)
    speaker_notes(s, load_notes("s65"))


# ============================================================
# Main
# ============================================================

SLIDE_BUILDERS = [
    build_s01, build_s02, build_s03, build_s04, build_s05, build_s06, build_s07, build_s08,
    build_s09, build_s10, build_s11, build_s12, build_s13, build_s14, build_s15,
    build_s16, build_s17, build_s18, build_s19, build_s20, build_s21, build_s22,
    build_s23, build_s24, build_s25, build_s26, build_s27, build_s28, build_s29, build_s30, build_s31,
    build_s32, build_s33, build_s34, build_s35, build_s36, build_s37, build_s38,
    build_s39, build_s40, build_s41, build_s42, build_s43, build_s44, build_s45, build_s46, build_s47,
    build_s48, build_s49, build_s50, build_s51, build_s52, build_s53, build_s54, build_s55, build_s56,
    build_s57, build_s58, build_s59, build_s60, build_s61, build_s62, build_s63,
    build_s64, build_s65,
]


def main():
    p = setup_pres()
    for fn in SLIDE_BUILDERS:
        print(f"--- {fn.__name__} ---")
        fn(p)
    assert len(p.slides) == 65, f"expected 65 slides, got {len(p.slides)}"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    p.save(str(OUT))
    print(f"Saved {OUT} with {len(p.slides)} slides")


if __name__ == "__main__":
    main()
