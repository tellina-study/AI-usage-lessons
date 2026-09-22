"""
Build script for Семинар 4 v4 — «Сборка кодинг-агента: лестница роста конфигурации»
(issue #201, раунд 4 — раскол на два семинара, 49 слайдов, полная пересборка).

Source-of-truth: deck.yaml + slides/s01..s49-*.md (49 slides). Direct python-pptx
build (not PowerPoint MCP), per notes/mcp-limitations.md [#54-1/#54-2/#54-3]:
MCP has no list_shapes, format_runs is buggy, no update_shape_position.

Canvas: 13.333" x 7.5" (16:9). Ocean Gradient v3 palette, LOCKED.

v4 change over v3 (72 slides): deck.yaml split into two seminars (R4-0/R4-1/R4-3).
Раздел 0 (открытие, s01-s07) + Раздел 1 (файл инструкций, 3 кейса, s08-s26) +
Раздел 2 (память, 3 кейса, s27-s46) + Раздел 3 (закрытие, s47-s49). Stages
3-7 (хук/скилл/MCP/субагент/процесс) moved to sem-05, out of scope here.

No live terminal — every "terminal snapshot" is either a verbatim transcription
of a real captured command output (assets/captures/*.txt) or, where explicitly
marked illustrative in the source .md, a text/card layout that does NOT imitate
a terminal, exactly as each slide's own Visual section specifies.
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
GREY_FILL = RGBColor(0xE4, 0xE9, 0xEF)

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
# Generic low-level helpers (reused pattern from v3 build_sem04.py)
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
    """Cheap diagnostic — estimates whether `text` at `size`pt fits in a box of
    width_in x height_in, prints OVERFLOW WARNING if not. Not pixel-perfect,
    deliberately conservative — catches box/text mismatches in one build pass."""
    if not text or width_in <= 0:
        return
    char_w = size * char_w_factor / 72.0
    chars_per_line = max(1, int(width_in / char_w))
    lines_needed = 0
    for para in text.split("\n"):
        n = len(para)
        lines_needed += max(1, -(-n // chars_per_line))
    line_h = size * line_h_factor / 72.0
    capacity = height_in / line_h if line_h > 0 else 0
    if lines_needed > capacity + 0.15:
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
    'strike': True). Real paragraph objects (tf.add_paragraph()), not literal
    '\\n' — needed for correct per-line CENTER alignment in LibreOffice render
    (see notes/mcp-limitations.md — literal \\n + align=CENTER does not
    center independently per visual line)."""
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


def auto_header(slide, section_label, title):
    """header() with size/height picked from title length, returns the y
    coordinate where slide content may safely start."""
    n = len(title)
    if n <= 65:
        size, h = 22, 0.8
    elif n <= 95:
        size, h = 19, 0.95
    elif n <= 125:
        size, h = 16.5, 1.1
    elif n <= 160:
        size, h = 14.5, 1.3
    elif n <= 200:
        size, h = 13, 1.5
    else:
        size, h = 12, 1.7
    header(slide, section_label, title, title_size=size, title_h=h)
    return 0.7 + h + 0.18


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


def criterion_plate(slide, x, y, w, h, items, *, title="ЗДЕСЬ ЕЩЁ РАНО", size=10.6):
    filled_rect(slide, x, y, w, h, RGBColor(0xEE, 0xF2, 0xF6), stroke=SOFT_GREY, stroke_pt=1.0,
                radius=True, radius_adj=0.1)
    pad = 0.18
    text_box(slide, x + pad, y + 0.05, w - 2 * pad, 0.24, text=title, size=10.5,
             bold=True, color=SLATE)
    bullet = "  ·  "
    body = bullet.join(items)
    _fits(body, size, w - 2 * pad, h - 0.33, label="criterion_plate")
    text_box(slide, x + pad, y + 0.28, w - 2 * pad, h - 0.33, text=body, size=size,
             color=DEEP, line_spacing=1.2)


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


def two_basket_frame(slide, x, y, w, h, left_title, left_slots, right_title, right_slots, *,
                      right_highlight=False):
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


def slot_row5(slide, x, y, w, h, slots, *, accent_idx=()):
    """5 numbered slots in one row — shared by s07 (co-built) and s48 (static
    recap). accent_idx = tuple of gold-accented slot indices, rest muted grey."""
    ocean_box(slide, x, y, w, h)
    pad = 0.26
    n = 5
    gap = 0.18
    cw = (w - 2 * pad - gap * (n - 1)) / n
    top = y + pad
    slot_h = h - 2 * pad
    cx = x + pad
    for i, (label, desc) in enumerate(slots):
        gold = i in accent_idx
        fill = GOLD_TINT if gold else GREY_FILL
        stroke = GOLD_DARK if gold else SLATE
        filled_rect(slide, cx, top, cw, slot_h, fill, stroke=stroke,
                    stroke_pt=1.5 if gold else 1.1, radius=True, radius_adj=0.12)
        text_box(slide, cx, top + 0.1, cw, 0.28, text=str(i + 1), size=13, bold=True,
                 color=(GOLD_DARK if gold else SLATE), align=PP_ALIGN.CENTER)
        paras = [{"text": ln, "size": 12.3, "bold": True,
                   "color": (GOLD_DARK if gold else DEEP), "align": PP_ALIGN.CENTER,
                   "line_spacing": 1.05} for ln in label.split("\n")]
        multipara_box(slide, cx + 0.06, top + 0.42, cw - 0.12, 0.58, paras)
        text_box(slide, cx + 0.07, top + 1.02, cw - 0.14, slot_h - 1.1, text=desc,
                 size=9.2, italic=True, color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.08)
        cx += cw + gap


# ============================================================
# Divider helpers — section-level (s08) and case-level (s09/s15/s21/s27)
# ============================================================

def strip_pills(slide, x, y, w, n, active_idx):
    gap = 0.12
    pw = (w - gap * (n - 1)) / n
    cx = x
    for i in range(n):
        cur = (i == active_idx)
        col = GOLD if cur else RGBColor(0x3E, 0x4C, 0x8A)
        filled_rect(slide, cx, y, pw, 0.28, col, radius=True, radius_adj=0.4)
        cx += pw + gap


def divider_bg(s, *, icon_name=None):
    gradient_rect(s, 0, 0, SLIDE_W_IN, SLIDE_H_IN,
                   [(0, DEEP), (55000, MID), (100000, LIGHT)])
    if icon_name:
        icon_x, icon_y, icon_w = 10.85, 5.35, 1.35
        filled_rect(s, icon_x - 0.3, icon_y - 0.3, icon_w + 0.6, icon_w + 0.6,
                    RGBColor(0x0B, 0x14, 0x3A), radius=True, radius_adj=0.18)
        icon(s, icon_name, "F0AB00", 128, icon_x, icon_y, icon_w)


def divider_section(p, slide_id, *, title, case_lines, tag, active_idx, total,
                     icon_name):
    """pattern: section_divider, section-level overview (s08)."""
    s = blank(p)
    divider_bg(s, icon_name=icon_name)
    strip_pills(s, 0.55, 0.55, 11.2, total, active_idx)
    text_box(s, 0.85, 1.75, 10.5, 1.1, text=title, size=38, bold=True, color=WHITE,
             line_spacing=1.05)
    ly = 3.05
    for line in case_lines:
        filled_rect(s, 0.9, ly, 0.14, 0.14, GOLD, radius=True, radius_adj=0.5)
        text_box(s, 1.2, ly - 0.12, 8.8, 0.42, text=line, size=16.5, color=RGBColor(0xE1, 0xE9, 0xF6))
        ly += 0.56
    tag_w = 5.6
    filled_rect(s, 0.9, ly + 0.25, tag_w, 0.55, RGBColor(0x0B, 0x14, 0x3A), stroke=GOLD,
                stroke_pt=1.2, radius=True, radius_adj=0.28)
    text_box(s, 0.9 + 0.28, ly + 0.25, tag_w - 0.56, 0.55, text=tag.upper(), size=11.5,
             bold=True, color=GOLD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes(slide_id))
    return s


def divider_case(p, slide_id, *, title, meaning, tag, case_idx, case_total, icon_name):
    """pattern: section_divider, case-level (s09/s15/s21) — 3-pill strip of
    cases within the current раздел, current case gold, others muted."""
    s = blank(p)
    divider_bg(s, icon_name=icon_name)
    strip_pills(s, 0.9, 0.6, 5.6, case_total, case_idx)
    text_box(s, 0.9, 2.15, 9.8, 1.15, text=title, size=36, bold=True, color=WHITE,
             line_spacing=1.05)
    text_box(s, 0.95, 3.42, 9.6, 0.9, text=meaning, size=17, italic=True,
             color=RGBColor(0xCF, 0xDC, 0xEC), line_spacing=1.3)
    tag_w = 6.0
    filled_rect(s, 0.95, 4.35, tag_w, 0.6, RGBColor(0x0B, 0x14, 0x3A), stroke=GOLD,
                stroke_pt=1.2, radius=True, radius_adj=0.28)
    text_box(s, 0.95 + 0.28, 4.35, tag_w - 0.56, 0.6, text=tag.upper(), size=11.5,
             bold=True, color=GOLD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes(slide_id))
    return s


def divider_section_and_case(p, slide_id, *, big_title, subtitle, meaning, tag, icon_name):
    """pattern: section_divider — combined раздел+case divider (s27 only)."""
    s = blank(p)
    divider_bg(s, icon_name=icon_name)
    text_box(s, 0.9, 1.55, 10.6, 0.9, text=big_title, size=36, bold=True, color=WHITE,
             line_spacing=1.05)
    text_box(s, 0.9, 2.42, 10.6, 0.7, text=subtitle, size=22, bold=True, color=GOLD,
             line_spacing=1.05)
    text_box(s, 0.95, 3.32, 9.9, 0.85, text=meaning, size=16.5, italic=True,
             color=RGBColor(0xCF, 0xDC, 0xEC), line_spacing=1.3)
    tag_w = 5.6
    filled_rect(s, 0.95, 4.25, tag_w, 0.55, RGBColor(0x0B, 0x14, 0x3A), stroke=GOLD,
                stroke_pt=1.2, radius=True, radius_adj=0.28)
    text_box(s, 0.95 + 0.28, 4.25, tag_w - 0.56, 0.55, text=tag.upper(), size=11.5,
             bold=True, color=GOLD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes(slide_id))
    return s


# ============================================================
# Reusable pattern-level slide builders
# ============================================================

def question_slide(p, slide_id, *, label, title, question, options, opt_h=1.5,
                    note="разбор — на следующем слайде", scenario=None):
    """pattern: reflection_question / question_with_option_cards — gold
    question callout + N option cards + neutral note (no table, no highlight,
    per R3-4)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, label, title)
    if scenario:
        text_box(s, 0.55, y, 12.23, 0.85, text=scenario, size=12, italic=True,
                 color=SLATE, line_spacing=1.22)
        y += 0.95
    qh = 1.3 if len(question) > 220 else (1.1 if len(question) > 140 else 0.85)
    gold_callout(s, 0.55, y, 12.23, qh, question, size=14, anchor=MSO_ANCHOR.MIDDLE)
    y += qh + 0.22
    n = len(options)
    gap = 0.16
    cw = (12.23 - gap * (n - 1)) / n
    cx = 0.55
    for label_txt in options:
        ocean_box(s, cx, y, cw, opt_h, fill=SURFACE, stroke=SOFT_GREY, stroke_pt=1.1)
        lines = label_txt.split("\n")
        paras = [{"text": ln, "size": 12.5, "bold": True, "color": DEEP,
                   "align": PP_ALIGN.CENTER, "line_spacing": 1.15} for ln in lines]
        multipara_box(s, cx + 0.08, y, cw - 0.16, opt_h, paras, anchor=MSO_ANCHOR.MIDDLE)
        cx += cw + gap
    text_box(s, 0.55, y + opt_h + 0.16, 12.23, 0.35, text=note, size=12, italic=True,
             color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes(slide_id))
    return s


def answer_slide(p, slide_id, *, label, title, context_q, headers, rows, col_w,
                  gold_rows, footer, table_h=3.9, header_size=10.3, cell_size=10.0,
                  footer_h=0.95, footer_size=13.5):
    """pattern: answer_breakdown — small context question + reveal table with
    gold target row(s) + gold footer plate with the target answer / criterion."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, label, title)
    text_box(s, 0.55, y, 12.23, 0.3, text=f"вопрос для контекста: «{context_q}»",
             size=11.3, italic=True, color=SLATE)
    y += 0.4
    reveal_table(s, 0.55, y, 12.23, table_h, headers, rows, col_w,
                 row_highlight={i: "gold" for i in gold_rows},
                 header_size=header_size, cell_size=cell_size)
    fy = y + table_h + 0.16
    gold_callout(s, 0.55, fy, 12.23, footer_h, footer, size=footer_size,
                 anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes(slide_id))
    return s


def criteria_slide(p, slide_id, *, label, title, items, boundary_text, extra_note=None):
    """pattern: criteria_checklist_and_boundary — checklist + explicit
    boundary/bridge text (shared by s34/s40/s46)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, label, title)
    n = len(items)
    row_h = 0.56
    ocean_box(s, 0.55, y, 12.23, n * row_h + 0.3)
    iy = y + 0.18
    for it in items:
        filled_rect(s, 0.78, iy + 0.08, 0.22, 0.22, TEAL, radius=True, radius_adj=0.25)
        _fits(it, 13.5, 11.3, row_h - 0.1, label="criteria_slide item")
        text_box(s, 1.14, iy, 11.4, row_h - 0.08, text=it, size=13.5, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.18)
        iy += row_h
    by = y + n * row_h + 0.3 + 0.2
    bh = 7.0 - by - (0.7 if extra_note else 0)
    gold_callout(s, 0.55, by, 12.23, bh, boundary_text, size=13, anchor=MSO_ANCHOR.MIDDLE)
    if extra_note:
        text_box(s, 0.55, by + bh + 0.1, 12.23, 0.55, text=extra_note, size=11.3,
                 italic=True, color=SLATE, line_spacing=1.2)
    speaker_notes(s, load_notes(slide_id))
    return s


def scenario_pain_slide(p, slide_id, *, label, title, scenario, bottom_line, note=None):
    """pattern: scenario_pain — a big narrative scenario block + one bold
    pain-summary line (shared by s35/s41)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, label, title)
    sh = 7.0 - y - 1.15 - (0.35 if note else 0)
    ocean_box(s, 0.55, y, 12.23, sh)
    _fits(scenario, 14, 11.7, sh - 0.4, label="scenario_pain")
    text_box(s, 0.9, y + 0.2, 11.5, sh - 0.4, text=scenario, size=14, color=DEEP,
             line_spacing=1.32, anchor=MSO_ANCHOR.MIDDLE)
    by = y + sh + 0.18
    gold_callout(s, 0.55, by, 12.23, 0.85, bottom_line, size=15, anchor=MSO_ANCHOR.MIDDLE,
                 align=PP_ALIGN.CENTER)
    if note:
        text_box(s, 0.55, by + 0.85 + 0.08, 12.23, 0.3, text=note, size=10.5,
                 italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes(slide_id))
    return s


# ============================================================
# Раздел 0 — Открытие (s01-s07)
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


def build_growth_staircase_bare(slide, x, y, w, h, *, bar_lo, bar_hi, bar_gold,
                                 number_color, gold_number_color, baseline_color,
                                 show_numbers=True):
    """Unlabeled ascending staircase — hero motif for s01 (bars only, no
    filenames/stage names — 'семь ступеней лестницы, без подписей')."""
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
             text="Один сквозной кейс, две развилки харнесса на трёх реальных решениях",
             size=15.5, italic=True, color=RGBColor(0xCF, 0xDC, 0xEC), align=PP_ALIGN.CENTER)

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

    hero_x, hero_y, hero_w, hero_h = 0.55, 3.55, 12.23, 3.35  # ~41% of slide area
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


def build_s02(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Открытие",
           "Часть требований видно, открыв редактор. Часть — нет, сколько угодно смотри в код",
           title_size=18)
    two_basket_frame(s, 0.55, 1.95, 12.23, 3.35, "видно в коде", [None, None, None],
                      "нигде не будет видно", [None, None, None])
    gold_callout(s, 0.55, 5.5, 12.23, 1.3,
                 "«Заказчик просит лендинг с формой заявки на демо-урок. Одна страница, "
                 "два поля, кнопка. Назовите вслух: что вообще должно быть у этой задачи, "
                 "чтобы вы могли сказать ‘готово’ и показать её заказчику? Не как это "
                 "устроено внутри — а что должно существовать.»", size=14.5)
    speaker_notes(s, load_notes("s02"))


def build_s03(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Открытие",
           "Шесть требований делятся ровно пополам: три увидит в коде любой, три не "
           "будут видны нигде", title_size=19)
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
    header(s, "Раздел 0 · Сквозной кейс",
           "Репозиторий буквально пуст, а агент не задал ни одного уточняющего вопроса — "
           "и то, чего он не знал, решил за вас молча", title_size=15)
    half_w = 5.85
    y1 = 1.85
    h1 = 1.55
    terminal_card(s, 0.55, y1, half_w, h1, [
        ("$ ls -la signup-landing/", TEAL, True),
        ("total 8", CODE_FG),
        ("drwxr-xr-x 2 harness harness 4096 Sep 20 12:45 .", CODE_FG),
        ("drwxr-xr-x 3 harness harness 4096 Sep 20 12:45 ..", CODE_FG),
    ], size=11)
    text_box(s, 0.55, y1 + h1 + 0.03, half_w, 0.24, text="реальный вывод, не макет",
             size=10.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    rx = 0.55 + half_w + 0.33
    ocean_box(s, rx, y1, half_w, h1)
    text_box(s, rx + 0.2, y1 + 0.12, half_w - 0.4, h1 - 0.24,
             text="«собери лендинг с формой заявки на демо-урок: статическая HTML-страница, "
                  "сборка Vite (npm run build → dist/), поля формы — имя и email, тест на "
                  "Playwright, который проверяет, что форма не отправляется с пустыми "
                  "обязательными полями (tests/form.spec.ts)»",
             size=11, italic=True, color=DEEP, line_spacing=1.24)
    y2 = y1 + h1 + 0.32
    gold_callout(s, 0.55, y2, 12.23, 0.95,
                 "«Уточняющий вопрос не задавался. Все параметры задачи… были однозначно "
                 "выводимы из текста задачи, поэтому работа была начата сразу, без уточнений.»",
                 size=13.5, anchor=MSO_ANCHOR.MIDDLE)
    y3 = y2 + 0.95 + 0.22
    h3 = 2.0
    terminal_card(s, 0.55, y3, half_w, h3, [
        ("index.html", CODE_FG), ("src/main.js", CODE_FG),
        ("package.json", CODE_FG), ("tests/form.spec.ts", CODE_FG),
    ], title="что создал", size=12)
    terminal_card(s, rx, y3, half_w, h3, [
        ("npm install", CODE_FG),
        ("npm run build          # → dist/", CODE_FG),
        ("npm run test:e2e       # playwright test", CODE_FG),
    ], title="из финального ответа", size=12)
    speaker_notes(s, load_notes("s04"))


def build_s05(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Первый вопрос классу",
           "Первый блок конфигурации выбирают из восьми вариантов на экране — и «ничего» "
           "среди них не менее весомый вариант, чем остальные семь", title_size=15)
    gold_callout(s, 0.55, 1.85, 12.23, 1.55,
                 "«Перед вами репозиторий, который агент только что собрал, и вам с этим же "
                 "агентом доделывать этот сайт дальше, неделями. Выберите, какой блок "
                 "конфигурации вы добавите первым — из карточек ниже — так, чтобы он закрывал "
                 "реальную боль, а не запас на будущее.»", size=14, anchor=MSO_ANCHOR.MIDDLE)
    opts = ["файл\nинструкций", "память", "хук", "скилл", "MCP-\nдоступ", "субагент",
            "процесс\nпроверки", "ничего"]
    y2 = 3.7
    n = len(opts)
    gap = 0.16
    cw = (12.23 - gap * (n - 1)) / n
    cx = 0.55
    for i, label in enumerate(opts):
        ocean_box(s, cx, y2, cw, 1.55, fill=SURFACE, stroke=SOFT_GREY, stroke_pt=1.1)
        text_box(s, cx + 0.05, y2, cw - 0.1, 1.55, text=label, size=13, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)
        cx += cw + gap
    text_box(s, 0.55, 5.55, 12.23, 0.4,
             text="разбор — на следующем слайде", size=12, italic=True, color=SLATE,
             align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s05"))


def build_s06(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Разбор первого вопроса",
           "Бремя доказательства лежит на том, кто усложняет, а не на том, кто остаётся внизу",
           title_size=19)
    y = 1.75
    text_box(s, 0.55, y, 12.23, 0.32,
             text="вопрос для контекста: «Какой блок конфигурации добавить первым?»",
             size=11.5, italic=True, color=SLATE)
    y += 0.42
    headers = ["Прозвучавший вариант", "Где это работает", "Почему здесь ещё рано — и что вместо"]
    rows = [
        ["«Файл инструкций — так делают в хороших проектах»",
         "Когда есть накопленное знание, которого нет в коде",
         "«Так делают» — не триггер, а инерция. Вместо: дождаться сигнала. Через пятнадцать "
         "минут этот ответ станет верным — но потому, что сработает конкретный сигнал"],
        ["«Хук — поставлю защиту заранее, на будущее»",
         "Когда риск конкретной команды уже стал реальным",
         "Вы ещё не знаете, какие команды в этом проекте рискованны: защищаете гипотезу, а не "
         "факт. Вместо: назвать команду и инцидент, от которого защищаетесь"],
        ["«MCP — подключу к трекеру задач, пригодится»",
         "Когда доступ наружу нужен повторно и из нескольких сессий",
         "Самый дорогой из семи блоков — по контексту и по поверхности атаки. Вместо: обычная "
         "команда в терминале, пока не доказано, что её не хватает"],
        ["«Ничего»", "На нулевой ступени — всегда",
         "Не рано: это и есть ответ. Перестаёт быть верным ровно тогда, когда появится первое "
         "реальное расхождение между тем, что знаете вы, и тем, что знает агент"],
    ]
    table_h = 4.1
    reveal_table(s, 0.55, y, 12.23, table_h, headers, rows, [0.26, 0.28, 0.46],
                 row_highlight={3: "gold"}, header_size=10, cell_size=10)
    y += table_h + 0.18
    gold_callout(s, 0.55, y, 12.23, 0.65,
                 "бремя доказательства лежит на том, кто усложняет, а не на том, кто остаётся внизу",
                 size=15)
    speaker_notes(s, load_notes("s06"))


def build_s07(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Раздел 0 · Опорная карта",
        "Из пяти слотов экипировки агента сегодня подробно разбираются два — инструкции-"
        "правила и память; остальные три и оба практических слоя — дальше, Семинаром 5")
    slots = [
        ("память", "что агент помнит между сессиями"),
        ("инструкции-\nправила", "файл-конвенция проекта + журнал задач"),
        ("скиллы", "переиспользуемые процедуры под повторяющиеся задачи"),
        ("субагенты", "делегирование с отдельным контекстным окном"),
        ("доступ\nнаружу (MCP)", "доступ к внешним системам"),
    ]
    slot_h = 1.95
    slot_row5(s, 0.55, y, 12.23, slot_h, slots, accent_idx=(0, 1))
    y2 = y + slot_h + 0.2
    text_box(s, 0.55, y2, 12.23, 0.55,
             text="Сегодня подробно — два. Дальше, Семинар 5: скиллы, субагенты, доступ "
                  "наружу + хук, процесс.",
             size=14.5, italic=True, bold=True, color=MID, align=PP_ALIGN.CENTER,
             line_spacing=1.2)
    y3 = y2 + 0.6
    gold_callout(s, 0.55, y3, 12.23, 7.0 - y3,
                 "«Оставайтесь на самой нижней ступени, которая закрывает требование задачи. "
                 "Поднимайтесь на следующую только тогда, когда можете назвать требование, "
                 "которое текущая ступень не закрывает. Каждый подъём оплачивается новой "
                 "стоимостью, новыми режимами отказа и новой поверхностью атаки.»",
                 size=13, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s07"))


# ============================================================
# Раздел 1 — Файл инструкций (s08-s26)
# ============================================================

def build_s08(p):
    return divider_section(p, "s08",
        title="Раздел 1 · файл инструкций",
        case_lines=["Кейс 1.1 · роль агента и репозиторий",
                    "Кейс 1.2 · базовые процессы: гейты и цикл улучшения",
                    "Кейс 1.3 · вложенные файлы по подпапкам"],
        tag="Один файл, три развилки", active_idx=1, total=4, icon_name="file-text")


def build_s09(p):
    return divider_case(p, "s09",
        title="Кейс 1.1 · роль агента и репозиторий",
        meaning="Что писать в пустой файл, пока не случилось ни одной реальной сессии",
        tag="1 контролируемый эксперимент · 1 честный пробел",
        case_idx=0, case_total=3, icon_name="file-text")


def build_s10(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.1 · Роль и репозиторий",
        "Первый инстинкт — открыть пустой файл и начать с описания структуры "
        "репозитория; привычка сильная, но это ровно та фраза «так делают в хороших "
        "проектах», которую занятие проверяет впервые")
    half_w = 5.85
    h1 = 2.1
    terminal_card(s, 0.55, y, half_w, h1, [
        ("index.html", CODE_FG), ("package.json", CODE_FG),
        ("src/main.js", CODE_FG), ("tests/form.spec.ts", CODE_FG),
    ], title="дерево на входе в кейс", size=12.5)
    rx = 0.55 + half_w + 0.33
    ocean_box(s, rx, y, half_w, h1)
    text_box(s, rx + 0.2, y + 0.14, half_w - 0.4, h1 - 0.28,
             text="Разработчик открывает пустой CLAUDE.md и по привычке тянется первым "
                  "делом написать «Repository overview» — из чего собран сайт, где лежит "
                  "форма, какая структура папок.",
             size=13, color=DEEP, line_spacing=1.3)
    y2 = y + h1 + 0.25
    gold_callout(s, 0.55, y2, 12.23, 1.55,
                 "«В одном из прошлых проектов раздел "
                 "«Overview» пережил рефакторинг и два месяца спустя продолжал описывать "
                 "структуру, которой больше не существовало — агент один раз отредактировал "
                 "не тот файл, поверив описанию, а не факту.»",
                 size=13.5, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s10"))


def build_s11(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.1 · Исследование",
        "Repository overview измеримо не помогает и стоит контекста — кроме "
        "единственного подтверждённого исключения: репозитория без другой документации "
        "вообще")
    headers = ["Источник", "Тезис", "Сила доказательства"]
    rows = [
        ["Gloaguen et al., arXiv:2602.11988",
         "«Repository overviews… are not helpful» — «шагов до первого релевантного файла» "
         "не падает; cost +20–23% без прироста success",
         "Сильное: контролируемый эксперимент с честным третьим плечом «файла нет вообще»"],
        ["Та же работа, абляция",
         "Удалили существующую документацию (README) — LLM-сгенерированный overview стал "
         "полезен (+2,7%)",
         "Подтверждает механизм: overview вреден потому, что дублирует то, что уже доступно "
         "иначе"],
        ["Lulla et al., arXiv:2601.20404",
         "AGENTS.md с фокусом на недискаверабельные конвенции: −28,6% runtime, −16,6% "
         "tokens (124 PR)",
         "Умеренно-сильное «за» файл — но это НЕ про общее описание структуры"],
        ["Shepard & Albrecht, arXiv:2606.20512",
         "Статичное written-once guidance (28,3% resolve) хуже динамически "
         "верифицированного (33,0%, p<0,001)",
         "Косвенное — подтверждает логику «непроверенное статично хуже»"],
    ]
    table_h = 3.55
    reveal_table(s, 0.55, y, 12.23, table_h, headers, rows, [0.2, 0.42, 0.38],
                 row_highlight={0: "gold"}, header_size=10.3, cell_size=9.7)
    y += table_h + 0.14
    text_box(s, 0.55, y, 12.23, 0.4,
             text="это явление называют presence paradox — сам факт присутствия текста в "
                  "контексте создаёт свою стоимость независимо от того, использует ли его "
                  "агент (термин используется дальше без повторного объяснения)",
             size=10.8, italic=True, color=MID, align=PP_ALIGN.CENTER, line_spacing=1.2)
    y += 0.44
    gold_callout(s, 0.55, y, 12.23, 7.0 - y,
                 "«Прямых экспериментов с намеренно устаревшим или неверным repository "
                 "overview не найдено — это пробел в исследованиях, не установленный факт. "
                 "Анекдот коллеги — правдоподобный, но не измеренный случай.»",
                 size=11.5, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s11"))


def build_s12(p):
    return question_slide(p, "s12", label="Кейс 1.1 · Вопрос",
        title="Перед пустым CLAUDE.md выбор из пяти вариантов — и «пока ничего» среди "
              "них не менее весомый вариант, чем остальные четыре",
        question="«Перед вами пустой CLAUDE.md для signup-landing. Выберите, что из "
                  "перечисленного вы включите в файл прямо сейчас, до первой реальной "
                  "сессии агента — из карточек ниже.»",
        options=["подробное описание\nструктуры репозитория", "список технологий\nи "
                 "зависимостей", "инструкцию, где лежит\nформа и как её найти",
                 "неочевидную конвенцию,\nкоторую агент не угадает сам",
                 "пока ничего — до\nпервого реального сигнала"],
        opt_h=1.75)


def build_s13(p):
    headers = ["Вариант", "Где это работает", "Почему здесь ещё рано — и что вместо"]
    rows = [
        ["«Подробное описание структуры репозитория»",
         "Почти нигде для агента — разве что документация для новых людей в команде",
         "Агент выведет структуру сам за секунды; описание устареет при первом "
         "рефакторинге. Эксперимент: +20–23% cost, без прироста success. Вместо: не писать"],
        ["«Список технологий и зависимостей»",
         "Когда версии критичны и не видны из package.json (редко)",
         "В большинстве случаев тоже выводимо за секунды. Вместо: не писать, если версии "
         "видны в манифесте"],
        ["«Инструкция, где лежит форма и как её найти»",
         "Почти нигде на таком маленьком репозитории",
         "Четыре файла, вся структура на одном экране — находимость не проблема"],
        ["«Неочевидная конвенция, которую агент не угадает сам»",
         "Когда конвенция реально есть и реально невыводима",
         "На этом шаге такой конвенции ещё нет — проект только начался. Появится — "
         "записать её, и только её"],
        ["«Пока ничего — до первого реального сигнала»",
         "Здесь и сейчас",
         "Целевой ответ. Перестаёт быть верным, когда появится конкретная невыводимая "
         "вещь — не раньше"],
    ]
    return answer_slide(p, "s13", label="Кейс 1.1 · Разбор",
        title="Правильный ответ на этом шаге — не какой текст написать, а пока никакой: "
              "файл остаётся пустым, потому что триггер ещё не сработал",
        context_q="Что включить в файл прямо сейчас?", headers=headers, rows=rows,
        col_w=[0.24, 0.3, 0.46], gold_rows=[4],
        footer="Всё, что агент выведет из кода за секунды, в файл не идёт никогда — не "
               "«пока рано», а вообще. Общее описание роли/архитектуры оправданно только "
               "там, где нет вообще другой документации; у signup-landing она будет — "
               "значит, оснований нет.",
        table_h=3.75, footer_h=1.05, footer_size=12)


def build_s14(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.1 · Решение",
        "CLAUDE.md остаётся пустым — не из лени, а потому что нет сигнала; первый "
        "настоящий сигнал придёт через неделю")
    terminal_card(s, 0.55, y, 12.23, 2.35, [
        ("index.html", CODE_FG), ("package.json", CODE_FG),
        ("src/main.js", CODE_FG), ("tests/form.spec.ts", CODE_FG),
        ("# CLAUDE.md — не создан", CODE_MUTED, True),
    ], title="дерево репозитория — без изменений", size=13)
    y2 = y + 2.35 + 0.25
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2,
                 "«Файл пуст не потому, что мы ленивы, а потому что нет сигнала. Первый "
                 "настоящий сигнал появится через неделю.»",
                 size=17, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s14"))


def build_s15(p):
    return divider_case(p, "s15",
        title="Кейс 1.2 · базовые процессы",
        meaning="Первая реальная боль — заявка не доходит, тест зелёный",
        tag="4 препринта-консенсус · 1 контринтуитивный результат",
        case_idx=1, case_total=3, icon_name="file-text")


def build_s16(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.2 · Базовые процессы",
        "Заказчик пишет: заявка не пришла — тест зелёный, «готово» сказано, а тест "
        "проверяет только пустые поля; записанный текстовый гейт не изменил поведение "
        "при повторе")
    bh = 1.85
    ocean_box(s, 0.55, y, 12.23, bh)
    text_box(s, 0.8, y + 0.14, 11.7, bh - 0.28,
             text="Блок 1. Заказчик: «отправил заявку — она не пришла». Агент читает код, "
                  "правит обработчик в src/main.js, прогоняет автотест — зелёный — "
                  "отчитывается: «Готово». tests/form.spec.ts проверяет ровно одно: что "
                  "форма не отправляется с пустыми полями. Про доставку он не знает "
                  "ничего. Заказчик пишет снова: не доходит.",
             size=13, color=DEEP, line_spacing=1.28)
    y2 = y + bh + 0.2
    ocean_box(s, 0.55, y2, 12.23, bh)
    text_box(s, 0.8, y2 + 0.14, 11.7, bh - 0.28,
             text="Блок 2. Команда записывает в CLAUDE.md текстовый гейт: «Всегда прогоняй "
                  "тесты и вручную проверяй результат перед ‘готово’». Неделю спустя, "
                  "новая сессия, другой баг: автотест зелёный — снова «готово», руками не "
                  "проверено.",
             size=13, color=DEEP, line_spacing=1.28)
    y3 = y2 + bh + 0.18
    gold_callout(s, 0.55, y3, 12.23, 7.0 - y3, "«Правило было. Поведение — нет.»",
                 size=18, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s16"))


def build_s17(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Кейс 1.2 · Исследование",
        "Текстовый гейт без тулинга не просто бесполезен, а вреден — регрессии выросли "
        "почти до 10%; self-repair с реальной проверкой работает, голая самокритика "
        "систематически вредит", title_size=13.5, title_h=0.62)
    y = 0.7 + 0.62 + 0.14
    text_box(s, 0.55, y, 12.23, 0.26, text="исследование — гейты", size=12, bold=True,
             color=MID)
    y += 0.3
    h1_headers = ["Источник", "Тезис", "Сила"]
    h1_rows = [
        ["SWE-Gate/SpecBench/CapCode/Verification Horizon (4 препринта 2609–2606)",
         "Согласие 4+ независимых 2026-препринтов: агенты систематически «обходят» "
         "видимые тестовые гейты, разрыв растёт со сложностью задачи",
         "Сильное — межисследовательский консенсус"],
        ["TDAD, arXiv:2603.17973",
         "Чисто процедурная инструкция «сначала пиши тесты» без тулинга увеличила "
         "регрессии до 9,94% — хуже, чем вообще без инструкции",
         "Сильное и контринтуитивное"],
        ["Rethinking Agent-Generated Tests, arXiv:2602.07900",
         "Манипуляция промптом ради частоты тестов — без значимого эффекта на resolution "
         "rate (6 моделей, SWE-bench Verified)",
         "Умеренное — нулевой результат"],
        ["Agent Scaffolding Beats Model Upgrades",
         "Архитектура харнесса (test-gated retries, CI-enforcement) даёт +20 п.п.; смена "
         "модели — ~1 п.п.",
         "Сильное — механизм против модели"],
    ]
    th1 = 2.5
    reveal_table(s, 0.55, y, 12.23, th1, h1_headers, h1_rows, [0.32, 0.46, 0.22],
                 row_highlight={1: "gold"}, header_size=9.5, cell_size=8.8)
    y += th1 + 0.16
    text_box(s, 0.55, y, 12.23, 0.26, text="исследование — цикл «улучшение»", size=12,
             bold=True, color=MID)
    y += 0.3
    h2_headers = ["Источник", "Тезис", "Сила"]
    h2_rows = [
        ["Self-planning, arXiv:2303.06689",
         "Планирование перед кодом: +25,4% pass@1 (HumanEval/MBPP, не repo-scale)",
         "Умеренно-сильное «за»"],
        ["LLMs Cannot Self-Correct, ICLR'24; CRITIC, 2305.11738",
         "Самокоррекция без внешнего сигнала систематически ухудшает результат",
         "Сильное «против» голого self-review"],
        ["arXiv:2604.10508",
         "Self-repair с внешним сигналом (реальный прогон теста/компилятора): "
         "+4,9…+30 п.п.",
         "Сильное «за» — с реальной проверкой"],
    ]
    th2 = 1.75
    reveal_table(s, 0.55, y, 12.23, th2, h2_headers, h2_rows, [0.32, 0.46, 0.22],
                 row_highlight={2: "gold"}, header_size=9.5, cell_size=8.8)
    y += th2 + 0.14
    gold_callout(s, 0.55, y, 12.23, 7.0 - y,
                 "«Нет контролируемого эксперимента именно на изолированную фразу-гейт в "
                 "CLAUDE.md — только best-practice наблюдения практиков.»",
                 size=11, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s17"))


def build_s18(p):
    return question_slide(p, "s18", label="Кейс 1.2 · Вопрос",
        title="Гейт-фраза уже есть и не сработала — выбор из пяти вариантов, что делать "
              "дальше, чтобы реально сработало в следующей сессии",
        question="«У вас гейт-фраза в CLAUDE.md уже есть, а поведение агента не "
                  "изменилось — заявка снова не проверена руками. Выберите, что вы "
                  "сделаете дальше — из карточек ниже — так, чтобы это реально сработало "
                  "в следующей сессии.»",
        options=["перепишу фразу\nкапсом / жёстче", "продублирую фразу\nвторым пунктом",
                 "заведу отдельный\nфайл-чеклист рядом",
                 "передам проверку\nмеханизму вне текста",
                 "смирюсь — сработает\nне всегда, это норма"],
        opt_h=1.75)


def build_s19(p):
    headers = ["Вариант", "Где работает", "Почему рано — и что вместо"]
    rows = [
        ["«Капсом / жёстче»", "Нигде системно",
         "TDAD: усиление формулировки без тулинга не помогает и иногда вредит — "
         "регрессии выросли до 9,94%. Формулировка — не механизм"],
        ["«Продублирую вторым пунктом»", "Иногда чуть повышает шанс прочитать",
         "Правило остаётся просьбой. Каждая лишняя строка стоит контекста в каждой "
         "сессии (presence paradox, кейс 1.1)"],
        ["«Отдельный файл-чеклист»", "Помогает человеку помнить, слабо помогает агенту",
         "Тот же класс решения — снова текст, снова просьба, не обязательна к "
         "построчному следованию"],
        ["«Передам механизму вне текста»", "Системно работает: CI/harness-enforcement "
         "даёт +20 п.п.",
         "Верное направление — но сам механизм не тема сегодня, это Семинар 5. Сегодня "
         "фиксируем: текст сам по себе ненадёжен"],
        ["«Смирюсь, это нормально»", "Приемлемо для некритичных предпочтений",
         "Для правила, чьё нарушение стоит дорого — «смирюсь» означает решение не решать"],
    ]
    # Fix 5 (review-раунд v4): формула «правила в промпте — просьбы, правила в коде —
    # законы» сделана безусловной частью разбора (раньше звучала только в реакции на
    # ответ «капсом» из зала) — вынесена первой фразой в footer, не спрятана в ветку.
    return answer_slide(p, "s19", label="Кейс 1.2 · Разбор",
        title="Честный ответ сегодня: мы всё равно запишем гейт текстом, потому что это "
              "лучше, чем ничего, но прямо скажем себе, что он ненадёжен",
        context_q="Гейт не сработал — что дальше?", headers=headers, rows=rows,
        col_w=[0.22, 0.32, 0.46], gold_rows=[3],
        footer="Правила в промпте — это просьбы, правила в коде — это законы: текстовый "
               "гейт — просьба, и сегодня мы записываем именно просьбу. Приемлемый "
               "первый шаг, пока нарушение редкое; нарушено дважды на критичном "
               "действии — сигнал для эскалации к механическому уровню (Семинар 5). Цикл "
               "«улучшение»: агент, смотрящий сам на свой код, — не делать так; агент, "
               "прогоняющий реальную проверку, — делать так всегда.",
        table_h=3.35, footer_h=1.7, footer_size=10.8)


def build_s20(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.2 · Решение",
        "Итоговый файл — тринадцать строк: критерий готово, гейт-предупреждение, "
        "честная оговорка предела; AGENTS.md — симлинк на тот же файл")
    half_w = 6.7
    h1 = 4.55
    terminal_card(s, 0.55, y, half_w, h1, [
        ("# CLAUDE.md", TEAL, True),
        ("", CODE_FG),
        ("signup-landing: статический лендинг с формой заявки на демо-урок.", CODE_FG),
        ("Готово = npm run build код 0, npx playwright test зелёный,", CODE_FG),
        ("форма реально отправляет заявку на проде.", CODE_FG),
        ("", CODE_FG),
        ("## Safety / scope boundaries", TEAL, True),
        ("- Никогда не запускать деплой на прод без явного запроса.", CODE_FG),
        ("", CODE_FG),
        ("## Build, test, verify", TEAL, True),
        ("- To verify: открыть dist/index.html после сборки, вручную", CODE_FG),
        ("  отправить форму с заполненными и с пустыми полями.", CODE_FG),
    ], size=11, line_spacing=1.28)
    rx = 0.55 + half_w + 0.3
    rw = 12.23 - half_w - 0.3
    numbered_card(s, rx, y, rw, h1, [
        "Файл грузится в начало каждой сессии целиком (официальный ориентир — до 200 "
        "строк, наш итог — 13)",
        "@-импорты организуют файл, но не экономят контекст — импортированное всё равно "
        "грузится целиком",
        "AGENTS.md — симлинк на тот же файл (ln -s CLAUDE.md AGENTS.md). Острый край: "
        "cp -R без -P на macOS разыменовывает симлинк во вторую копию молча — копировать "
        "через cp -a / git clone / git archive",
    ], size=12)
    speaker_notes(s, load_notes("s20"))


def build_s21(p):
    return divider_case(p, "s21",
        title="Кейс 1.3 · вложенные файлы",
        meaning="Месяц спустя репозиторий подрос — дробить файл или нет",
        tag="1650 сессий · 5 задокументированных issue",
        case_idx=2, case_total=3, icon_name="file-text")


def build_s22(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.3 · Вложенные файлы",
        "Разработчик выносит правила тестов в tests/CLAUDE.md и ждёт, что агент "
        "подхватит его сам, когда работает именно в этой папке — логично звучит, но "
        "стоит проверить, что там реально происходит с загрузкой")
    half_w = 5.85
    h1 = 2.2
    terminal_card(s, 0.55, y, half_w, h1, [
        ("tests/", TEAL, True),
        ("  form.spec.ts", CODE_FG),
        ("  wizard.spec.ts", CODE_FG),
        ("  page-objects/form.page.ts", CODE_FG),
        ("  # своя конвенция именования + Page Object", CODE_MUTED),
    ], title="месяц спустя: tests/ подрос", size=11.5)
    rx = 0.55 + half_w + 0.33
    ocean_box(s, rx, y, half_w, h1)
    text_box(s, rx + 0.2, y + 0.14, half_w - 0.4, h1 - 0.28,
             text="«Вынесу эти правила в отдельный tests/CLAUDE.md — короче, релевантнее "
                  "контексту, корневой файл не разбухнет.» Кладёт файл в подпапку, ожидая "
                  "автоматической подхватки.",
             size=12.5, color=DEEP, line_spacing=1.28)
    y2 = y + h1 + 0.3
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2,
                 "«Логично звучит. Давайте проверим, что там на самом деле происходит с "
                 "загрузкой.»", size=16, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s22"))


def build_s23(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.3 · Исследование",
        "Вложенный файл грузится on-demand, только по факту чтения — не по факту "
        "нахождения в папке; контролируемое исследование не нашло пользы от разбиения, "
        "а практика показывает регулярные отказы вплоть до архитектурного предела")
    mh = 0.95
    ocean_box(s, 0.55, y, 12.23, mh)
    text_box(s, 0.75, y + 0.1, 11.85, mh - 0.2,
             text="Механизм (офиц. документация Claude Code): корневой и все родительские "
                  "CLAUDE.md грузятся при старте сессии автоматически. Вложенные грузятся "
                  "on-demand — только когда агент реально читает файл оттуда. /context — "
                  "единственный надёжный способ проверить, что реально загружено.",
             size=11.3, color=DEEP, line_spacing=1.22)
    y += mh + 0.18
    headers = ["Источник", "Тезис", "Сила"]
    rows = [
        ["McMillan, arXiv:2605.10039 (1650 сессий Claude Code CLI)",
         "Ни одна из 4 структурных переменных не дала значимого эффекта после "
         "multiple-testing correction; для size/conflict — свидетельство ОТСУТСТВИЯ "
         "эффекта",
         "Сильное и контринтуитивное"],
        ["Claude Code #2571", "Вложенный CLAUDE.md не подхватывается автоматически, "
         "воспроизводимо; закрыт «not planned»", "Прямое наблюдение"],
        ["Claude Code #6972", "Документация вводит в заблуждение — пользователи ждут "
         "eager-загрузку, на деле on-demand", "Прямое наблюдение"],
        ["Cursor, форум", "Сотрудник Cursor признал баг в nested-функциональности",
         "Прямое, другой инструмент"],
        ["Codex CLI #13288, #12115", "Ненадёжная подгрузка без явного --cd",
         "Прямое, другой инструмент"],
        ["GitHub Copilot CLI #3051", "Не баг, а документированный структурный предел: "
         "discovery только вдоль прямого пути cwd→git-root", "Самое жёсткое: "
         "архитектурное ограничение"],
    ]
    th = 2.85
    reveal_table(s, 0.55, y, 12.23, th, headers, rows, [0.28, 0.46, 0.26],
                 row_highlight={0: "gold", 5: "teal"}, header_size=9.3, cell_size=8.6)
    speaker_notes(s, load_notes("s23"))


def build_s24(p):
    return question_slide(p, "s24", label="Кейс 1.3 · Вопрос",
        title="Как гарантировать, что агент реально прочитает конвенции из "
              "tests/CLAUDE.md — выбор из пяти вариантов",
        question="«Выберите, как вы гарантируете, что агент реально прочитает конвенции "
                  "из tests/CLAUDE.md, когда работает именно в этой папке — из карточек "
                  "ниже.»",
        options=["положу файл в tests/\nи доверюсь автозагрузке",
                 "явно попрошу агента\nпрочитать файл в начале задачи",
                 "продублирую содержимое\nв корневом CLAUDE.md",
                 "проверю через /context,\nчто реально загружено",
                 "объединю всё в один\nфайл в корне, пока не мешает"],
        opt_h=1.75)


def build_s25(p):
    headers = ["Вариант", "Где работает", "Почему рано — и что вместо"]
    rows = [
        ["«Доверюсь автозагрузке»", "Никогда гарантированно",
         "Вложенные файлы грузятся on-demand, только по факту чтения. Задокументированные "
         "отказы — системная категория: #2571, #6972, Cursor, Codex CLI, жёсткий предел "
         "Copilot CLI #3051"],
        ["«Явно попрошу прочитать в начале задачи»", "Работает, требует ручной "
         "дисциплины каждый раз",
         "Надёжнее автозагрузки, но перекладывает ответственность на человека — то, от "
         "чего мы уходили в кейсе 1.1"],
        ["«Продублирую в корневой»", "Работает всегда — корень грузится при старте",
         "Снова presence paradox: продублированная строка стоит контекста в каждой "
         "сессии, в любой папке"],
        ["«Проверю через /context»", "Единственный надёжный способ узнать факт",
         "Диагностика, не решение — проверяет, сработало ли, не гарантирует в следующий "
         "раз"],
        ["«Объединю в один файл в корне, пока не вырос»", "Здесь и сейчас — репозиторий "
         "маленький",
         "Целевой ответ. Исследование (1650 сессий) не нашло значимого эффекта ни у одной "
         "структурной переменной"],
    ]
    return answer_slide(p, "s25", label="Кейс 1.3 · Разбор",
        title="Редкое сочетание: контролируемое исследование не нашло пользы даже там, "
              "где здравый смысл её обещал, а практика показывает регулярные отказы "
              "вплоть до архитектурного предела",
        context_q="Как гарантировать, что файл прочитан?", headers=headers, rows=rows,
        col_w=[0.28, 0.28, 0.44], gold_rows=[4],
        footer="Пока корневой файл помещается в разумный объём (до пятидесяти-семидесяти "
               "строк), дробление по подпапкам не нужно никогда. Даже при росте объёма "
               "дробить стоит только после того, как явно проверено — через /context или "
               "наблюдаемое поведение, — что инструмент реально грузит вложенный файл.",
        table_h=3.55, footer_h=1.3, footer_size=11.5)


def build_s26(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.3 · Решение",
        "Репозиторий остаётся с одним корневым файлом; три кейса — три решения знания, "
        "известного заранее, но есть знание другого рода, которое появляется по ходу "
        "работы — это раздел второй, память")
    terminal_card(s, 0.55, y, 12.23, 2.65, [
        ("AGENTS.md", CODE_FG), ("CLAUDE.md", CODE_FG), ("index.html", CODE_FG),
        ("package.json", CODE_FG), ("src/main.js", CODE_FG),
        ("tests/form.spec.ts", CODE_FG),
        ("# tests/CLAUDE.md — не появляется", CODE_MUTED, True),
    ], title="дерево репозитория — без изменений", size=11)
    y2 = y + 2.65 + 0.18
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2,
                 "«Три кейса, один и тот же файл: мы решили, чего в него не писать "
                 "заранее; написали то, что узнали на реальной боли; и решили не дробить "
                 "его, пока это не доказанная польза. Всё это — знание, которое у вас уже "
                 "было до работы, записанное заранее. Но есть знание другого рода: то, "
                 "что появляется по ходу самой работы. Его нельзя записать заранее, "
                 "потому что вы его ещё не знаете. Это раздел второй — память.»",
                 size=13, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s26"))


# ============================================================
# Раздел 2 — Память (s27-s50, review-раунд: +s28/s29 Fix 1, +s37/s44 Fix 4)
# ============================================================

def build_s27(p):
    return divider_section_and_case(p, "s27",
        big_title="Раздел 2 · память",
        subtitle="Кейс 2.1 · плоский файл",
        meaning="Между сессиями агент не хранит ни бита — если это не лежит на диске",
        tag="3 кейса по восходящей сложности", icon_name="database")


def build_s28(p):
    """pattern: problem_scenario — Fix 1 (review-раунд v4): проблема кейса 2.1,
    выделена в отдельный слайд (раньше была склеена с вопросом на одном слайде,
    нарушая обязательный паттерн проблема → исследование → вопрос → разбор)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.1 · Плоский файл",
        "Уже отклонённое решение всплывает снова, потому что разговор, в котором его "
        "приняли, закончился — а его содержимое нигде не осталось")
    sh = 2.0
    ocean_box(s, 0.55, y, 12.23, sh)
    text_box(s, 0.78, y + 0.14, 11.8, sh - 0.55,
             text="Третья сессия за две недели. Заказчик прислал заявку с опечаткой в "
                  "домене почты, форма её приняла. Разработчик просит доработать "
                  "валидацию. Агент предлагает подключить стороннюю библиотеку валидации "
                  "форм — ту самую, которую уже обсуждали и отклонили: форма из двух "
                  "полей, хватает нативных required/pattern и двадцати строк своего кода.",
             size=13, color=DEEP, line_spacing=1.28)
    text_box(s, 0.78, y + sh - 0.4, 11.8, 0.34,
             text="Агент предлагает её так, будто вопрос никогда не поднимался. Для него "
                  "он и не поднимался.", size=11, italic=True, color=SLATE)
    y += sh + 0.22
    gold_callout(s, 0.55, y, 12.23, 7.0 - y,
                 "«Агент не нарушил правило. В файле инструкций этого правила не было и "
                 "не могло быть — решение родилось в разговоре, а разговор кончился. Это "
                 "не «забыл»: модель не имеет состояния между вызовами.»",
                 size=13.5, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s28"))


def build_s29(p):
    """pattern: research_evidence (short bridge) — Fix 1 (review-раунд v4): presence
    paradox из кейса 1.1 (см. build_s11), перенесённый на DECISIONS.md. Не новое
    измерение — явная связка «мы это уже видели»."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.1 · Исследование",
        "Presence paradox из кейса 1.1 применяется и здесь: то, что лежит в "
        "DECISIONS.md, стоит контекста в каждой сессии независимо от того, нужна ли эта "
        "запись сегодня")
    half_w = 5.85
    h1 = 2.5
    ocean_box(s, 0.55, y, half_w, h1)
    text_box(s, 0.55 + 0.2, y + 0.14, half_w - 0.4, h1 - 0.28,
             text="Кейс 1.1: Gloaguen et al. — сам факт присутствия текста в контексте "
                  "создаёт стоимость (+20–23%), независимо от того, помогает ли он решить "
                  "задачу. Мы назвали это presence paradox.",
             size=12.5, color=DEEP, line_spacing=1.28)
    rx = 0.55 + half_w + 0.33
    filled_rect(s, rx, y, half_w, h1, SURFACE, stroke=GOLD, stroke_pt=1.4, radius=True,
                radius_adj=0.06)
    text_box(s, rx + 0.2, y + 0.14, half_w - 0.4, h1 - 0.28,
             text="DECISIONS.md — не исключение. Каждая строка грузится в контекст в "
                  "каждой следующей сессии, не только когда она реально нужна. Тридцать "
                  "записей о разных темах — цена уже заметна, даже если задача касается "
                  "только одной из них.",
             size=12.5, color=DEEP, line_spacing=1.28)
    y += h1 + 0.25
    text_box(s, 0.55, y, 12.23, 0.6,
             text="прямого измерения именно на журналах решений не проводилось — это "
                  "перенос уже установленного механизма на новый объект, не отдельное "
                  "новое исследование",
             size=11.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.25)
    y += 0.7
    gold_callout(s, 0.55, y, 12.23, 7.0 - y,
                 "если запись не бесплатна — точно ли туда идёт вообще всё, что можно "
                 "туда положить?", size=14.5, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s29"))


def build_s30(p):
    """pattern: question_with_option_cards — Fix 1 (review-раунд v4): теперь только
    вопрос+карточки; сценарий и диагностика переехали на build_s28, исследование —
    на build_s29 (см. обязательный паттерн проблема → исследование → вопрос → разбор)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.1 · Вопрос",
        "Выберите, куда записать отклонённое решение — из карточек ниже — так, чтобы не "
        "объяснять его в третий раз")
    text_box(s, 0.55, y, 12.23, 0.35,
             text="напоминание: отклонённая библиотека валидации всплыла снова — решение "
                  "родилось в разговоре и нигде не осталось",
             size=11, italic=True, color=SLATE)
    y += 0.42
    qh = 1.3
    gold_callout(s, 0.55, y, 12.23, qh,
                 "«Вы второй раз за две недели объясняете агенту, почему в этой форме "
                 "нет сторонней библиотеки валидации. Выберите, куда записать это "
                 "решение — из карточек ниже — так, чтобы не объяснять его в третий раз, "
                 "и обоснуйте, почему не в тот файл инструкций, который мы только что "
                 "завели.»", size=13, anchor=MSO_ANCHOR.MIDDLE)
    y += qh + 0.2
    opts = ["дописать\nв CLAUDE.md", "сказать агенту\n«запомни это»",
            "завести\nDECISIONS.md", "поставить систему\nпамяти", "ничего — сам\nзапомнит"]
    n = len(opts)
    gap = 0.16
    cw = (12.23 - gap * (n - 1)) / n
    cx = 0.55
    opt_h = 7.0 - y
    for label in opts:
        ocean_box(s, cx, y, cw, opt_h, fill=SURFACE, stroke=SOFT_GREY, stroke_pt=1.1)
        paras = [{"text": ln, "size": 12, "bold": True, "color": DEEP,
                   "align": PP_ALIGN.CENTER, "line_spacing": 1.15} for ln in label.split("\n")]
        multipara_box(s, cx + 0.08, y, cw - 0.16, opt_h, paras, anchor=MSO_ANCHOR.MIDDLE)
        cx += cw + gap
    speaker_notes(s, load_notes("s30"))


def build_s31(p):
    headers = ["Вариант", "Где это работает", "Почему здесь ещё рано — и что вместо"]
    rows = [
        ["«Допишу в CLAUDE.md»", "Механически сработает: файл читается каждую сессию",
         "Смешивает стабильные правила и растущий лог решений. На десятке решений файл "
         "выйдет за ориентир в 200 строк. Вместо: развести слои по авторству"],
        ["«Ничего, агент сам запомнит»", "Нигде: это не настройка, которую забыли "
         "включить",
         "Модель не имеет состояния между вызовами по конструкции. Вместо: решить, кто и "
         "куда пишет"],
        ["«Скажу агенту ‘запомни это’»", "Для личного предпочтения — идеально",
         "Половина ответа. Уходит в авто-память: машинно-локальный слой без "
         "синхронизации и код-ревью"],
        ["«Заведу DECISIONS.md»", "Для командного решения с обоснованием — именно то, "
         "что нужно",
         "Вторая половина ответа. Требует писать «почему», а не «что»"],
        ["«Поставлю систему памяти»", "На десятках-сотнях записей, нескольких "
         "пользователях",
         "Рано на порядок: на малых корпусах простой файл регулярно конкурентен со "
         "сложными системами"],
    ]
    return answer_slide(p, "s31", label="Кейс 2.1 · Разбор",
        title="Командное решение с обоснованием идёт в DECISIONS.md, личное предпочтение "
              "— в авто-память, выводимое из кода — никуда",
        context_q="Куда записать отклонённое решение — и почему не в файл инструкций?",
        headers=headers, rows=rows, col_w=[0.24, 0.3, 0.46], gold_rows=[],
        footer="целевой ответ — оба механизма разом, с разделением ролей",
        table_h=3.7, footer_h=0.7, footer_size=15)


def build_s32(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.1 · Совместное формирование",
        "Не всё, что узнал агент, вообще стоит записывать — третья корзина такая же "
        "законная, как первые две")
    bh = 2.7
    basket_row(s, 0.55, y, 12.23, bh, [
        ("авто-память", ["Разработчик просит отвечать\nкоротко, без преамбул"]),
        ("DECISIONS.md", ["Не подключаем стороннюю библиотеку\nвалидации — форма из двух "
                           "полей", "Своего бэкенда не делаем — заявка\nуходит на внешний "
                           "сервис приёма форм"]),
        ("никуда", ["Обработчик формы лежит\nв src/main.js",
                     "19 сентября тест упал из-за\nтаймаута, увеличили ожидание"]),
    ], highlight_idx=2)
    y2 = y + bh + 0.25
    terminal_card(s, 0.55, y2, 12.23, 7.0 - y2, [
        ("## 2026-09-20 — не подключаем библиотеку валидации форм", TEAL, True),
        ("Форма — два поля (имя, email), хватает нативных required/pattern в", CODE_FG),
        ("index.html. Сторонняя библиотека — лишняя зависимость ради этого объёма.", CODE_FG),
    ], title="собранная запись — реальный файл демо-репозитория", size=11.5)
    speaker_notes(s, load_notes("s32"))


def build_s33(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.1 · Решение",
        "Два параллельных механизма, не один: авто-память живёт вне репозитория, "
        "DECISIONS.md — git-трекнутый лог «почему» внутри него")
    half_w = 6.7
    h = 4.45
    terminal_card(s, 0.55, y, half_w, h, [
        ("# Decisions", TEAL, True),
        ("", CODE_FG),
        ("Append-only log of why, in date order.", CODE_MUTED),
        ("", CODE_FG),
        ("## 2026-09-20 — не подключаем библиотеку валидации форм", TEAL, True),
        ("Форма — два поля (имя, email), хватает нативных required/pattern", CODE_FG),
        ("в index.html. Сторонняя библиотека — лишняя зависимость и лишние", CODE_FG),
        ("килобайты в сборке ради этого объёма.", CODE_FG),
    ], title="DECISIONS.md — целиком", size=11)
    rx = 0.55 + half_w + 0.3
    rw = 12.23 - half_w - 0.3
    th = 2.65
    terminal_card(s, rx, y, rw, th, [
        ("AGENTS.md", CODE_FG), ("CLAUDE.md", CODE_FG),
        ("DECISIONS.md", GOLD, True), ("index.html", CODE_FG),
        ("package.json", CODE_FG), ("src/main.js", CODE_FG),
        ("tests/form.spec.ts", CODE_FG),
    ], title="дерево кейса 2.1", size=10.5)
    ry2 = y + th + 0.2
    ocean_box(s, rx, ry2, rw, h - th - 0.2)
    text_box(s, rx + 0.18, ry2 + 0.12, rw - 0.36, h - th - 0.4,
             text="diff создания файла: +DECISIONS.md (новый), git add + commit — "
                  "команда, а не агент, решает, когда коммитить журнал решений.",
             size=10.8, italic=True, color=SLATE, line_spacing=1.25)
    speaker_notes(s, load_notes("s33"))


def build_s34(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.1 · Три слоя",
        "Разница между слоями не в формате — оба markdown, — а в том, кто инициирует "
        "запись и кто её потом увидит")
    headers = ["", "Файл инструкций", "Авто-память", "DECISIONS.md"]
    rows = [
        ["Кто автор", "вы, заранее", "агент, по ходу", "вы, в момент решения"],
        ["Где живёт", "в репозитории, git", "вне репозитория, на этой машине",
         "в репозитории, git"],
        ["Что грузится", "целиком, каждую сессию", "индекс: первые 200 строк / 25 КБ",
         "ничего автоматически"],
        ["Проходит код-ревью", "да", "нет", "да"],
        ["Переживает смену машины", "да", "нет", "да"],
        ["Что туда идёт", "стабильные правила и границы", "предпочтения, подтверждённые "
         "подходы", "решения и их «почему»"],
    ]
    th = 3.55
    reveal_table(s, 0.55, y, 12.23, th, headers, rows, [0.22, 0.26, 0.26, 0.26],
                 header_size=11.5, cell_size=10.5)
    y += th + 0.16
    text_box(s, 0.55, y, 12.23, 0.75,
             text="индекс памяти — только индекс  ·  агент сам пропускает выводимое из "
                  "кода  ·  сжатие контекста переживают только файлы на диске",
             size=12.5, italic=True, color=MID, align=PP_ALIGN.CENTER, line_spacing=1.25)
    speaker_notes(s, load_notes("s34"))


def build_s35(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.1 · Провал и эффективность",
        "Память по умолчанию читается как доверенный контекст, а не как данные — и "
        "включение памяти не обязательно улучшает результат")
    half_w = 7.6
    h1 = 2.15
    failure_card(s, 0.55, y, half_w, h1, icon_name="alert-triangle",
                 header_text="Отравление памяти — SpAIware (сентябрь 2024)",
                 body="Внешний текст с вложенной инструкцией → долговременная память → "
                      "активация в последующих сессиях, эксфильтрация переписки. Вектор "
                      "закрыт в версии 1.2024.247; структурный принцип остался.",
                 body_size=11.5, header_size=12.5)
    rx = 0.55 + half_w + 0.28
    rw = 12.23 - half_w - 0.28
    ocean_box(s, rx, y, rw, h1)
    text_box(s, rx + 0.18, y + 0.14, rw - 0.36, h1 - 0.28,
             text="≈48% всех последующих обращений к памяти захвачено (MemoryGraft, "
                  "2025; до отравления — 0%). В смежном эксперименте 5 подложенных "
                  "документов управляют выводом в >90% случаев.",
             size=11.5, color=DEEP, line_spacing=1.26)
    y2 = y + h1 + 0.2
    headers = ["Замер", "Значение", "База сравнения"]
    rows = [
        ["Популярная система памяти на бенчмарке долговременной памяти",
         "46,0% с памятью против 57,6% без", "та же система, память выключена"],
        ["Шесть систем памяти против «весь текст сессии в один файл»",
         "проигрыш плоскому файлу на 25–67 пунктов", "тот же плоский файл"],
        ["Дискреционность записи", "17% (4 задачи из 24) — модель отказалась записать "
         "нужный факт", "те же 24 задачи"],
    ]
    th2 = 1.85
    reveal_table(s, 0.55, y2, 12.23, th2, headers, rows, [0.42, 0.32, 0.26],
                 row_highlight={0: "gold"}, header_size=10.3, cell_size=9.8)
    speaker_notes(s, load_notes("s35"))


def build_s36(p):
    return criteria_slide(p, "s36", label="Кейс 2.1 · Критерий и граница",
        title="Плоского файла достаточно, пока история решений влезает в контекст "
              "целиком и связей между записями ещё нет",
        items=[
            "Задача одноразовая, второй сессии по этому контексту не будет.",
            "Весь нужный контекст помещается в одно контекстное окно без потерь.",
            "Правила проекта стабильны и укладываются в файл инструкций короче 200 строк.",
            "Никто не повторяет вручную одну и ту же правку из сессии в сессию.",
            "Нет нескольких участников, которым нужно делиться контекстом асинхронно.",
            "Факт выводим из кода или истории изменений.",
        ],
        boundary_text="Плоский DECISIONS.md перестаёт справляться, когда записей "
                       "набралось настолько много, что найти нужную линейным чтением "
                       "дольше, чем переобъяснить решение заново, — и между записями "
                       "появились связи, для которых в append-only логе физически "
                       "некуда положить.")


def build_s37(p):
    """pattern: section_divider — Fix 4 (review-раунд v4): кейс 2.2 получает свой
    divider, по образцу кейсов 1.1/1.2/1.3/2.1 (у которых он уже был)."""
    return divider_case(p, "s37",
        title="Кейс 2.2 · структурированная вики-память",
        meaning="Тот же DECISIONS.md, но разросшийся — плоский лог больше не хранит связей",
        tag="1 контрпример структуре · 4 честных издержки",
        case_idx=1, case_total=3, icon_name="git-branch")


def build_s38(p):
    return scenario_pain_slide(p, "s38", label="Кейс 2.2 · Вики-память",
        title="Файл технически на месте, но пользоваться им дольше, чем не "
              "пользоваться — линейный лог не хранит связей между записями",
        scenario="Прошло четыре месяца. Новый разработчик в команде просит агента "
                 "добавить капчу на форму: появился спам. Агент листает DECISIONS.md "
                 "целиком (тридцать восемь записей) и предлагает решение, которое "
                 "противоречит более раннему решению №14: «не добавляем сторонние "
                 "виджеты в форму, см. запись №3». Агент нашёл запись №3, но не нашёл "
                 "запись №31 — она отменяет часть решения №3 конкретно для случая "
                 "антиспама, дописана двумя месяцами позже, в другом конце файла, без "
                 "единой отсылки назад.",
        bottom_line="Разработчик открывает файл сам и тратит на линейное чтение "
                     "тридцати восьми записей больше времени, чем ушло бы на то, чтобы "
                     "заново передумать вопрос с нуля.",
        note="Пример иллюстративный — реального разросшегося DECISIONS.md на 38 "
             "записей не захвачено.")


def build_s39(p):
    return question_slide(p, "s39", label="Кейс 2.2 · Вопрос",
        title="Тридцать восемь записей и потерянная связь между двумя из них — повод "
              "выбрать, как реорганизовать журнал решений, а не заводить его заново",
        question="«DECISIONS.md разросся до тридцати восьми записей, и в нём уже есть "
                  "решение, которое отменяет часть более раннего решения, — без единой "
                  "ссылки между ними. Выберите, как реорганизовать этот файл — из "
                  "карточек ниже — так, чтобы агент быстро находил нужное решение и "
                  "видел связи между решениями. Обоснуйте выбор.»",
        options=["оставить как есть —\nпросто грепать",
                 "разбить на тематические\nфайлы со ссылками",
                 "поставить графовую/\nвекторную систему памяти",
                 "завести один общий\nSUMMARY.md, переписываемый целиком",
                 "агент сам найдёт\nчерез поиск по репозиторию"],
        opt_h=1.75)


def build_s40(p):
    headers = ["Вариант", "Где это работает", "Почему здесь ещё рано — и что вместо"]
    rows = [
        ["«Оставить как есть, просто грепать»", "Пока записей десятки и они "
         "укладываются в контекст целиком",
         "Деградация плоской памяти со временем задокументирована кросс-источниками "
         "(~72 ч, −14 п.п.); наш файл уже перерос эту границу"],
        ["«Разбить на тематические файлы со сквозными ссылками»", "Именно этот случай",
         "Целевой ответ, но не бесплатный — структура сама создаёт новую нагрузку "
         "(staleness, дублирование, поддержка)"],
        ["«Поставлю графовую/векторную систему памяти»", "На больших "
         "многопользовательских корпусах с семантическим поиском",
         "Контрпример прямо про наш масштаб: файловое хранилище обошло graph-based "
         "систему на LoCoMo. Рано на порядок"],
        ["«Один общий SUMMARY.md, переписываемый целиком»", "Для совсем маленького "
         "проекта",
         "Переписывание целиком убивает append-only гарантию — история решения "
         "невосстановима"],
        ["«Агент сам найдёт через поиск по репозиторию»", "Для фактов, выводимых из "
         "кода",
         "Решения — не факты кода. «Сам найдёт» — то же заблуждение, что «сам "
         "запомнит»"],
    ]
    return answer_slide(p, "s40", label="Кейс 2.2 · Разбор",
        title="Разбить на тематические файлы со сквозными ссылками — целевой ответ, но "
              "не бесплатный: структура сама создаёт новую нагрузку",
        context_q="Как реорганизовать разросшийся журнал решений?", headers=headers,
        rows=rows, col_w=[0.26, 0.28, 0.46], gold_rows=[1],
        footer="целевой ответ — разбить на тематические файлы со сквозными ссылками, со "
               "списком реальных издержек, а не как безусловный апгрейд",
        table_h=3.65, footer_h=0.85, footer_size=13)


def build_s41(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.2 · Решение",
        "Запись явно ссылается на связанную запись — то, чего в плоском append-only "
        "логе не было в принципе")
    half_w = 5.0
    h = 3.5
    terminal_card(s, 0.55, y, half_w, h, [
        ("memory/decisions/", TEAL, True),
        ("  index.md        ← оглавление тем + ссылки", CODE_FG),
        ("  validation.md   ← решения по валидации формы", CODE_FG),
        ("  backend.md      ← решения о том, чего мы НЕ делаем", CODE_FG),
        ("  deploy.md", CODE_FG),
    ], size=11.5)
    rx = 0.55 + half_w + 0.3
    rw = 12.23 - half_w - 0.3
    terminal_card(s, rx, y, rw, h, [
        ("## 2026-09-20 — не подключаем библиотеку валидации форм", TEAL, True),
        ("Форма — два поля, хватает нативных required/pattern.", CODE_FG),
        ("См. также: 2026-11-30 (антиспам) — это решение НЕ", CODE_FG),
        ("распространяется на защиту от спама, другой механизм.", CODE_FG),
        ("", CODE_FG),
        ("## 2026-11-30 — антиспам через honeypot-поле, без капчи", TEAL, True),
        ("Отменяет часть решения от 2026-09-20 для случая антиспама.", CODE_FG),
    ], title="validation.md — пример записи", size=10.3)
    y2 = y + h + 0.2
    text_box(s, 0.55, y2, 12.23, 7.0 - y2,
             text="иллюстративный пример, не захваченный вживую — ждёт реальной сессии",
             size=11.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s41"))


def build_s42(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.2 · Провал и издержки",
        "Структура — не гарантированный выигрыш и не бесплатный апгрейд: простое "
        "файловое хранилище обошло графовую систему памяти, а сама структура добавляет "
        "свою собственную нагрузку")
    text_box(s, 0.55, y, 12.23, 0.5,
             text="почти все источники ниже — свежие непроверенные препринты 2026 года; "
                  "цифры — «заявлено в препринте», а не установленный факт",
             size=10.8, italic=True, color=SLATE, line_spacing=1.2)
    y += 0.55
    headers = ["Система", "LoCoMo (долговременная память)"]
    rows = [["Простое файловое хранилище (grep/чтение файлов)", "74,0%"],
            ["Mem0 (graph-based)", "68,5%"]]
    th = 1.5
    reveal_table(s, 0.55, y, 12.23, th, headers, rows, [0.72, 0.28],
                 row_highlight={0: "gold"}, header_size=11.5, cell_size=13)
    y += th + 0.14
    text_box(s, 0.55, y, 12.23, 0.4,
             text="объяснение авторов: модели тренированы на файловых операциях как на "
                  "самом привычном инструменте", size=11, italic=True, color=SLATE)
    y += 0.45
    items = [
        "Staleness — сводка в оглавлении расходится с содержимым тематического файла.",
        "Duplication — устаревшие версии одного и того же факта накапливаются вместо "
        "замены.",
        "Отсутствие каскадного удаления — удалили факт в одном файле, производные "
        "записи в других остались жить как верные.",
        "Maintenance burden — кто-то должен реально ходить и поддерживать структуру "
        "актуальной.",
    ]
    criterion_plate(s, 0.55, y, 12.23, 7.0 - y, items,
                     title="ЧЕСТНО НАЗВАННЫЕ НЕДОСТАТКИ ВИКИ-ПАМЯТИ", size=11)
    speaker_notes(s, load_notes("s42"))


def build_s43(p):
    return criteria_slide(p, "s43", label="Кейс 2.2 · Критерий и мост",
        title="Единиц-десятков тематических файлов, которые правят один-два человека, "
              "достаточно — полноценная система памяти требует замеров на своём "
              "масштабе, не общего совета",
        items=[
            "Число тематических файлов — единицы-десятки, не сотни.",
            "Поиск нужной записи — по имени темы или простому grep, а не по смысловой "
            "близости.",
            "Участников, одновременно правящих память, — один-два.",
            "Никто не просил «найди решения, похожие по смыслу на…».",
        ],
        boundary_text="Смена оси: всё в этом и предыдущем кейсе — про решения, которые "
                       "живут навсегда. Что происходит с памятью одной задачи, пока она "
                       "ещё не закончена?")


def build_s44(p):
    """pattern: section_divider — Fix 4 (review-раунд v4): кейс 2.3 получает свой
    divider, по образцу кейсов 1.1/1.2/1.3/2.1/2.2 (у которых он уже есть)."""
    return divider_case(p, "s44",
        title="Кейс 2.3 · операционная память",
        meaning="Смена оси: не решения навсегда, а ход одной задачи между её сессиями",
        tag="21 120 траекторий · 1 кейс-стади n=1",
        case_idx=2, case_total=3, icon_name="clipboard-check")


def build_s45(p):
    return scenario_pain_slide(p, "s45", label="Кейс 2.3 · Задачная память",
        title="Вторая сессия многошаговой задачи начинается не с продолжения, а с "
              "повторного анализа с нуля — и с конфликта с уже принятыми по ходу "
              "мелкими решениями",
        scenario="Разработчик ставит агенту задачу на несколько сессий: разбить форму "
                 "signup-landing на пошаговый визард (имя → email → подтверждение), "
                 "сохранив всю текущую валидацию. Шесть шагов, первая сессия обрывается "
                 "на середине, контекст сжимается. Вторая сессия: агент, не имея под "
                 "рукой ничего, кроме кода и сжатой сводки, заново анализирует форму с "
                 "нуля и предлагает план, который на треть повторяет уже сделанное и на "
                 "треть противоречит мелким решениям, принятым по ходу первой сессии — "
                 "например, переписать email-валидацию, которую договорились не трогать.",
        bottom_line="Разработчик тратит начало второй сессии не на продолжение работы, "
                     "а на то, чтобы заново объяснить, что уже сделано.")


def build_s46(p):
    return question_slide(p, "s46", label="Кейс 2.3 · Вопрос",
        title="Агент после сжатия контекста или в новой сессии должен продолжить с "
              "того места, где остановился, а не начать заново",
        question="«Вторая сессия по одной и той же многошаговой задаче начинается с "
                  "того, что агент заново анализирует форму с нуля — и предлагает "
                  "переделать то, что уже решили не трогать. Выберите, куда и как "
                  "записывать ход этой задачи — из карточек ниже — так, чтобы агент "
                  "после сжатия контекста или в новой сессии продолжил с того места, "
                  "где остановился. Обоснуйте выбор.»",
        options=["надеяться на\nконтекстное окно",
                 "записать план\nв DECISIONS.md",
                 "завести один файл\nна задачу",
                 "завести папку на задачу\nс файлом под каждый шаг",
                 "попросить агента\n«продолжи с того места»"],
        opt_h=1.75)


def build_s47(p):
    headers = ["Вариант", "Где это работает", "Почему здесь ещё рано — и что вместо"]
    rows = [
        ["«Не сжимать, не закрывать сессию»", "Для задачи, целиком укладывающейся в "
         "одну короткую сессию",
         "Контекстное окно конечно; на многошаговой задаче рано или поздно случится "
         "сжатие или разрыв сессии — это отсутствие стратегии"],
        ["«Записать план в DECISIONS.md»", "Никогда — не тот слой памяти",
         "DECISIONS.md — про «почему» для решений, которые остаются в силе навсегда; "
         "статус одной задачи туда не относится"],
        ["«Один файл на задачу: план + лог хода + результаты»", "Ровно наш случай",
         "Целевой ответ для этого масштаба"],
        ["«Папка на задачу с файлом под каждый шаг»", "Параллельные подзадачи, "
         "несколько субагентов, разросшийся лог",
         "Оверинжиниринг для одной линейной задачи здесь и сейчас. Паттерн реально "
         "масштабируется до папки"],
        ["«Попросить ‘продолжи с того места’»", "Внутри одной непрерывной сессии, до "
         "сжатия",
         "После сжатия или в новой сессии буквально нечего продолжать — просьба "
         "адресована памяти, которой не существует"],
    ]
    return answer_slide(p, "s47", label="Кейс 2.3 · Разбор",
        title="Один файл на задачу — план, лог хода, результаты — целевой ответ для "
              "линейной задачи с одним агентом и одним разработчиком",
        context_q="Куда записывать ход многошаговой задачи?", headers=headers,
        rows=rows, col_w=[0.26, 0.3, 0.44], gold_rows=[2],
        footer="целевой ответ — один файл на задачу, с явным уточнением, что это "
               "упрощённая версия паттерна, масштабируемого до папки",
        table_h=3.65, footer_h=0.85, footer_size=12.5)


def build_s48(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.3 · Решение",
        "Файл задачи ссылается на журнал решений, а не дублирует его — и это осознанное "
        "упрощение паттерна, полностью раскрываемого в другом месте")
    terminal_card(s, 0.55, y, 12.23, 4.35, [
        ("# Задача: разбить форму на пошаговый визард", TEAL, True),
        ("", CODE_FG),
        ("## План", TEAL, True),
        ("1. [x] Разметка трёх шагов (имя / email / подтверждение)", CODE_FG),
        ("2. [x] Перенос текущей валидации без изменений", CODE_FG),
        ("3. [ ] Состояние текущего шага (JS)", CODE_FG),
        ("4. [ ] Кнопки «назад»/«далее»", CODE_FG),
        ("5. [ ] Тесты на переключение шагов", CODE_FG),
        ("6. [ ] Ручная проверка полного прохождения", CODE_FG),
        ("", CODE_FG),
        ("## Лог хода", TEAL, True),
        ("- 2026-09-20: шаги 1–2 закрыты. Договорились НЕ трогать email-", CODE_FG),
        ("  валидацию — обсуждалась в DECISIONS.md (2026-09-20), тут перенос.", CODE_FG),
        ("- 2026-09-22: начат шаг 3, не закончен — контекст сжат в середине.", CODE_FG),
        ("", CODE_FG),
        ("## Результаты (заполняется по завершении)", TEAL, True),
        ("—", CODE_FG),
    ], title=".tasks/active/signup-wizard.md", size=9.7, line_spacing=1.12)
    y2 = y + 4.35 + 0.15
    text_box(s, 0.55, y2, 12.23, 7.45 - y2,
             text="иллюстративный пример, не захваченный вживую — ждёт реальной "
                  "многошаговой сессии владельца · упрощение до файла — масштабируется "
                  "до папки, подробнее за пределами этого занятия",
             size=10.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.2)
    speaker_notes(s, load_notes("s48"))


def build_s49(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.3 · Провал",
        "Плохой план хуже отсутствия плана вообще — и это подтверждено количественно, "
        "а не только интуицией")
    headers = ["Источник", "Результат"]
    rows = [
        ["Evaluating Plan Compliance, 21 120 траекторий, SWE-bench Verified/Pro",
         "«bad plans hurt performance more than no plan at all»; комплаенс к плану "
         "падает ~на 13 п.п. на сложном бенчмарке"],
        ["Fresh Memory, Stale Plans, 30 контролируемых живых сценариев",
         "без проверки актуальности плана исполнитель действовал по устаревшему плану "
         "во всех 30 случаях (100%)"],
    ]
    th1 = 1.9
    reveal_table(s, 0.55, y, 12.23, th1, headers, rows, [0.42, 0.58],
                 header_size=11, cell_size=10.3)
    y += th1 + 0.18
    failure_card(s, 0.55, y, 12.23, 1.85, icon_name="alert-octagon",
                 header_text="Кейс-стади «Index Sickness» (n=1, честная оговорка)",
                 body="Реальный проект, 391 сессия за месяц. Решение — физическое "
                      "разделение baseline-инструкций и append-only лога сессии. "
                      "Результат: объём AI-инструкций сократился ~на 75%, рецидивов не "
                      "было за следующие ~150 сессий. n=1 action research одного "
                      "автора, не контролируемый эксперимент.",
                 body_size=12, header_size=13)
    y += 1.85 + 0.18
    text_box(s, 0.55, y, 12.23, 7.0 - y,
             text="практика «файл/папка на задачу» пока не мейнстрим — 2853 реальных "
                  "репозитория, доминируют статические context-файлы",
             size=11.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.25)
    speaker_notes(s, load_notes("s49"))


def build_s50(p):
    return criteria_slide(p, "s50", label="Кейс 2.3 · Критерий",
        title="Одного файла на задачу достаточно, пока задача линейная и её ведёт один "
              "агент и один разработчик — иначе оправдан переход к папке",
        items=[
            "Задача линейная: шаги идут по порядку, не параллельно.",
            "Работает один агент (без субагентов/параллельных веток) и один "
            "разработчик.",
            "Лог хода помещается в разумный файл (сотни строк, не тысячи) без потери "
            "читаемости.",
            "Результатов и артефактов на выходе немного — не нужен отдельный файл на "
            "каждый.",
        ],
        boundary_text="Если хотя бы половина пунктов неверна — переход к папке на "
                       "задачу оправдан.",
        extra_note="честная оговорка: паттерн «файл/папка на задачу» пока не мейнстрим "
                    "(2853 реальных репозитория, доминируют статические context-файлы) "
                    "— практику продвигают отдельные лидеры, это не общепринятая норма")


# ============================================================
# Раздел 3 — Закрытие (s51-s53)
# ============================================================

def build_s51(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Раздел 3 · Синтез",
        "Шесть развилок сегодняшнего занятия — три про файл инструкций, три про "
        "память — отвечали на один и тот же скрытый вопрос")
    headers = ["Кейс", "Развилка", "Что мы записали"]
    rows = [
        ["1.1", "Роль агента и общее описание репозитория",
         "Ничего — до первого реального сигнала"],
        ["1.2", "Базовые процессы: гейт «готово» + цикл улучшения",
         "Гейт-фраза текстом в CLAUDE.md"],
        ["1.3", "Вложенные файлы инструкций по подпапкам",
         "Не дробим — один файл в корне"],
        ["2.1", "Плоский файл памяти (DECISIONS.md)",
         "Решение записано в файл + авто-память"],
        ["2.2", "Структурированная вики-память",
         "Тематические файлы со сквозными ссылками"],
        ["2.3", "Операционная задачная память",
         "Один файл на задачу: план + лог + результаты"],
    ]
    th = 3.65
    reveal_table(s, 0.55, y, 12.23, th, headers, rows, [0.1, 0.42, 0.48],
                 header_size=12, cell_size=12.3)
    y += th + 0.2
    text_box(s, 0.55, y, 12.23, 7.0 - y,
             text="Всё в правом столбце — текст, который агент читает и может учесть.",
             size=19, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s51"))


def build_s52(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Раздел 3 · Охват",
        "Сегодня закрыты подробно два слота харнесса из пяти; оставшиеся три плюс оба "
        "механических слоя, которые превращают просьбу в барьер, — материал Семинара 5")
    slots = [
        ("память", "что агент помнит между сессиями"),
        ("инструкции-\nправила", "файл-конвенция проекта + журнал задач"),
        ("скиллы", "переиспользуемые процедуры под повторяющиеся задачи"),
        ("субагенты", "делегирование с отдельным контекстным окном"),
        ("доступ\nнаружу (MCP)", "доступ к внешним системам"),
    ]
    slot_h = 1.95
    slot_row5(s, 0.55, y, 12.23, slot_h, slots, accent_idx=(0, 1))
    y2 = y + slot_h + 0.25
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2,
                 "Семинар 5: скиллы · субагенты · доступ наружу (MCP) + хук · процесс",
                 size=16, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s52"))


def build_s53(p):
    """pattern: closing_question — Fix 3 (review-раунд v4): композиция намеренно
    ОТЛИЧАЕТСЯ от build_s51 (полная таблица шести развилок), а не является её
    уменьшенной копией с вырезанным столбцом. Здесь: тонкая строка-перечень БЕЗ
    таблицы/рамки/столбца ответов + доминирующий крупный вопрос + подпись."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Раздел 3 · Перенос",
        "Перенесите шесть сегодняшних решений на свой репозиторий — и проверьте, какое "
        "из них держится только на просьбе текстом")
    # Тонкая строка-перечень кейсов — НЕ таблица, без рамки, без столбца ответов.
    text_box(s, 0.55, y, 12.23, 0.55,
             text="1.1  →  1.2  →  1.3  →  2.1  →  2.2  →  2.3",
             size=15, color=MID, align=PP_ALIGN.CENTER)
    text_box(s, 0.55, y + 0.5, 12.23, 0.35,
             text="роль и репозиторий · базовые процессы · вложенные файлы · плоский "
                  "файл · вики-память · задачная память",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    y2 = y + 1.05
    # Крупный доминирующий вопрос — без карточек-вариантов, без таблицы под ним.
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2 - 0.55,
                 "«По каждой развилке — то, что у вас уже принято, это просьба текстом, "
                 "которую агент технически может обойти? Или нужен барьер?»",
                 size=20, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    text_box(s, 0.55, 7.0 - 0.5, 12.23, 0.4, text="«Не вслух. Не на бумаге. Себе.»",
             size=13, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s53"))


# ============================================================
# Main
# ============================================================

SEQ = [f"s{i:02d}" for i in range(1, 54)]


def main():
    p = setup_pres()
    for sid in SEQ:
        fn = globals()[f"build_{sid}"]
        fn(p)
    p.save(str(OUT))
    print(f"Saved {OUT} — {len(p.slides)} slides")


if __name__ == "__main__":
    main()
