"""
Build script for Семинар 4 v5 — «Сборка кодинг-агента: день-0 база или жди сигнала»
(issue #201, раунд 5 — смена оси + R5-1..R5-4, 52 слайда, полная пересборка).

Source-of-truth: deck.yaml + slides/s01..s57-*.md (52 slides). Direct python-pptx
build (not PowerPoint MCP), per notes/mcp-limitations.md [#54-1/#54-2/#54-3]:
MCP has no list_shapes, format_runs is buggy, no update_shape_position.

Canvas: 13.333" x 7.5" (16:9). Ocean Gradient v3 palette, LOCKED.

v5 change over v4 (53 slides): REWORK-REQUIREMENTS-v5.md.
  R5-0 — новая ось «день-0 база vs жди сигнала» заменяет «тонкий агент: жди
    триггер для всего» (переразгибала тезис Лекции 3).
  R5-1 — визуальная унификация дивайдеров: macro (раздел, gold, шире, с
    номерным значком) явно отличается от micro (кейс, teal, уже, без значка).
  R5-2 — раздел 0 (s02-s04) переписан: задача заказчика → открытая дискуссия
    → spec.md → сквозной кейс с новым поворотом (структура, не критерий).
  R5-3 — во всех 6 кейсах вопрос звучит ДО исследования (было наоборот);
    кейсы 2.2/2.3 получили новые отдельные research-слайды.
  R5-4 — README-плашка кейса 1.1 поднята в заметный gold-блок разбора.

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
TEAL_TINT = RGBColor(0xE0, 0xF1, 0xF2)

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
# Generic low-level helpers (unchanged from v4)
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
    width_in x height_in, prints OVERFLOW WARNING if not."""
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
    (see notes/mcp-limitations.md [#201-1])."""
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
    line_h = size * line_spacing * 1.18 / 72.0  # +18% safety margin (see [#201-2])
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
            tint = GOLD_TINT if row_highlight[ri] == "gold" else TEAL_TINT
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
    """5 numbered slots in one row — shared by s08 (co-built) and s56 (static
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
# Divider helpers — R5-1: macro (раздел, gold, wide) explicitly differs from
# micro (кейс, teal, narrow, no badge). Hybrid combines both on one slide (s28).
# ============================================================

def strip_pills(slide, x, y, w, n, active_idx, *, active_color=GOLD,
                 inactive_color=RGBColor(0x3E, 0x4C, 0x8A), pill_h=0.28):
    gap = 0.12
    pw = (w - gap * (n - 1)) / n
    cx = x
    for i in range(n):
        cur = (i == active_idx)
        col = active_color if cur else inactive_color
        filled_rect(slide, cx, y, pw, pill_h, col, radius=True, radius_adj=0.4)
        cx += pw + gap


def divider_bg(s, *, icon_name=None):
    gradient_rect(s, 0, 0, SLIDE_W_IN, SLIDE_H_IN,
                   [(0, DEEP), (55000, MID), (100000, LIGHT)])
    if icon_name:
        icon_x, icon_y, icon_w = 10.85, 5.35, 1.35
        filled_rect(s, icon_x - 0.3, icon_y - 0.3, icon_w + 0.6, icon_w + 0.6,
                    RGBColor(0x0B, 0x14, 0x3A), radius=True, radius_adj=0.18)
        icon(s, icon_name, "F0AB00", 128, icon_x, icon_y, icon_w)


def divider_badge_macro(s, number):
    """Gold circular badge with the раздел number — macro-level marker (R5-1),
    the one visual element ONLY macro/hybrid dividers carry."""
    cx, cy, r = 1.0, 1.55, 0.38
    circ = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - r), Inches(cy - r),
                               Inches(2 * r), Inches(2 * r))
    circ.fill.solid(); circ.fill.fore_color.rgb = GOLD
    circ.line.fill.background()
    disable_shadow(circ)
    text_box(s, cx - r, cy - r, 2 * r, 2 * r, text=str(number), size=26, bold=True,
             color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def divider_section_macro(p, slide_id, *, title, case_lines, tag, active_idx, total,
                           icon_name):
    """pattern: section_divider_macro (R5-1) — раздел-уровень. Wide GOLD
    4-segment progress-bar at top + gold numbered badge next to the title.
    Visually heavier than case-level dividers (see divider_case_micro)."""
    s = blank(p)
    divider_bg(s, icon_name=icon_name)
    strip_pills(s, 0.55, 0.45, 11.2, total, active_idx, active_color=GOLD)
    divider_badge_macro(s, active_idx)
    text_box(s, 1.65, 1.65, 9.7, 1.1, text=title, size=36, bold=True, color=WHITE,
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


def divider_case_micro(p, slide_id, *, title, meaning, tag, case_idx, case_total,
                        icon_name):
    """pattern: section_divider_micro (R5-1) — кейс-уровень. Narrow TEAL
    3-segment progress-bar, no numbered badge, smaller title than macro —
    visually lighter, marking a sub-level within the current раздел."""
    s = blank(p)
    divider_bg(s, icon_name=icon_name)
    strip_pills(s, 0.9, 0.6, 4.6, case_total, case_idx, active_color=TEAL)
    text_box(s, 0.9, 2.15, 9.8, 1.1, text=title, size=33, bold=True, color=WHITE,
             line_spacing=1.05)
    text_box(s, 0.95, 3.38, 9.6, 0.9, text=meaning, size=16, italic=True,
             color=RGBColor(0xCF, 0xDC, 0xEC), line_spacing=1.3)
    tag_w = 6.0
    filled_rect(s, 0.95, 4.32, tag_w, 0.55, RGBColor(0x0B, 0x14, 0x3A), stroke=TEAL,
                stroke_pt=1.2, radius=True, radius_adj=0.28)
    text_box(s, 0.95 + 0.28, 4.32, tag_w - 0.56, 0.55, text=tag.upper(), size=11,
             bold=True, color=TEAL, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes(slide_id))
    return s


def divider_hybrid(p, slide_id, *, big_title, subtitle, meaning, tag, icon_name,
                    macro_idx, macro_total, micro_idx, micro_total, case_lines=None):
    """pattern: section_divider_hybrid (R5-1, s28 only) — combined раздел+кейс
    divider. Carries BOTH the macro badge+wide-gold-strip AND the narrower
    teal case-strip, so both levels are legible on one slide.

    `case_lines`, if given, renders the раздел-level three-case preview list
    (same gold-bullet composition as `divider_section_macro`'s own
    `case_lines`, e.g. s09) between `meaning` and the tag — Fix 3 (round-6
    QA): s09 previews all three раздел-1 cases, s28 previously did not preview
    раздел-2's three cases, an asymmetry between the two macro-level
    dividers."""
    s = blank(p)
    divider_bg(s, icon_name=icon_name)
    strip_pills(s, 0.55, 0.42, 11.2, macro_total, macro_idx, active_color=GOLD)
    divider_badge_macro(s, macro_idx)
    strip_pills(s, 0.95, 0.84, 4.2, micro_total, micro_idx, active_color=TEAL,
                pill_h=0.2)
    text_box(s, 1.65, 1.58, 9.5, 0.85, text=big_title, size=32, bold=True, color=WHITE,
             line_spacing=1.05)
    text_box(s, 1.65, 2.38, 9.5, 0.65, text=subtitle, size=19, bold=True, color=TEAL,
             line_spacing=1.05)
    text_box(s, 0.95, 3.22, 9.9, 0.85, text=meaning, size=15, italic=True,
             color=RGBColor(0xCF, 0xDC, 0xEC), line_spacing=1.3)
    tag_y = 4.15
    if case_lines:
        ly = 4.18
        for line in case_lines:
            filled_rect(s, 0.95, ly, 0.13, 0.13, GOLD, radius=True, radius_adj=0.5)
            text_box(s, 1.24, ly - 0.11, 8.8, 0.38, text=line, size=14,
                     color=RGBColor(0xE1, 0xE9, 0xF6))
            ly += 0.44
        tag_y = ly + 0.16
    tag_w = 5.6
    filled_rect(s, 0.95, tag_y, tag_w, 0.55, RGBColor(0x0B, 0x14, 0x3A), stroke=GOLD,
                stroke_pt=1.2, radius=True, radius_adj=0.28)
    text_box(s, 0.95 + 0.28, tag_y, tag_w - 0.56, 0.55, text=tag.upper(), size=11,
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
    no digit — R5-3: vote happens blind, research comes after)."""
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
    boundary/bridge text."""
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
    """pattern: scenario_pain / problem_scenario — a big narrative scenario
    block + one bold pain-summary line. NO question, NO cards (R5-3: those
    live on the next slide)."""
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
# Раздел 0 — Открытие (s01-s08)
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
             text="День-0 база или жди сигнала — шесть развилок одного сквозного кейса",
             size=15.5, italic=True, color=RGBColor(0xCF, 0xDC, 0xEC), align=PP_ALIGN.CENTER)

    q_y = 2.08
    q_h = 1.3
    filled_rect(s, 1.0, q_y, SLIDE_W_IN - 2.0, q_h, RGBColor(0x0B, 0x14, 0x3A),
                stroke=GOLD, stroke_pt=1.8, radius=True, radius_adj=0.12)
    text_box(s, 1.4, q_y + 0.1, SLIDE_W_IN - 2.8, q_h - 0.2,
             text="«Что в конфигурации агента стоит закладывать сразу, на день 0, как "
                  "базовую практику — а что нельзя знать заранее, потому что оно "
                  "специфично для вашего проекта?»",
             size=16, italic=True, bold=True, color=GOLD, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.26)

    hero_x, hero_y, hero_w, hero_h = 0.55, 3.68, 12.23, 3.22  # ~41% of slide area
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
    y = auto_header(s, "Раздел 0 · Задача от заказчика",
        "Задача приходит в формулировке заказчика: что должно получиться — есть, "
        "устройства кода, критериев готовности и границ действий — нет")
    qh = 1.55
    ocean_box(s, 0.55, y, 12.23, qh)
    text_box(s, 0.85, y + 0.16, 11.6, qh - 0.32,
             text="«Нужен лендинг с формой заявки на демо-урок: одна статическая страница, "
                  "поля ‘имя’ и ‘email’, кнопка отправки. Своего бэкенда "
                  "нет — присылайте заявку на наш сервис приёма форм.»",
             size=16, italic=True, color=DEEP, line_spacing=1.32, anchor=MSO_ANCHOR.MIDDLE)
    y2 = y + qh + 0.3
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2 - 0.4,
                 "«Отдаём эту формулировку агенту как есть — или сначала фиксируем "
                 "требования?»", size=19, anchor=MSO_ANCHOR.MIDDLE,
                 align=PP_ALIGN.CENTER)
    text_box(s, 0.55, 7.0 - 0.32, 12.23, 0.3, text="открытая дискуссия, не голосование",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s02"))


def build_s03(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Раздел 0 · spec.md",
        "Требования раскладываются на функциональные и нефункциональные и ложатся в "
        "spec.md первым коммитом; README описывает устройство репозитория и заводится "
        "тем же коммитом")
    terminal_card(s, 0.55, y, 12.23, 3.4, [
        ("# spec.md — signup-landing", TEAL, True),
        ("", CODE_FG),
        ("## Функциональные требования", TEAL, True),
        ("- Статическая страница-лендинг, форма заявки на демо-урок", CODE_FG),
        ("- Поля: имя (обязательное), email (обязательное)", CODE_FG),
        ("- Кнопка отправки; без бэкенда — заявка уходит на внешний сервис", CODE_FG),
        ("", CODE_FG),
        ("## Нефункциональные требования", TEAL, True),
        ("- Критерий приёмки: форма реально доставляет заявку — проверено", CODE_FG),
        ("  на проде, а не только «тест зелёный»", CODE_FG),
        ("- Граница действий: не деплоить на прод без явного запроса", CODE_FG),
    ], size=11, line_spacing=1.24)
    y2 = y + 3.4 + 0.12
    text_box(s, 0.55, y2, 12.23, 0.3, text="иллюстративный пример, не захваченный артефакт",
             size=10.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    y2 += 0.38
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2,
                 "«README.md заводится тем же коммитом, отдельно от spec.md. Спека — "
                 "требования к продукту. README — устройство репозитория для того, кто в "
                 "него зайдёт: человек или агент.»", size=13, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s03"))


def build_s04(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Сквозной кейс",
           "Агент собрал работающий прототип по спеке без единого уточняющего вопроса "
           "— и структуру репозитория при этом выбрал сам, потому что spec.md её не "
           "описывает", title_size=14.5)
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
                  "обязательными полями (tests/form.spec.ts)» — по содержанию совпадает "
                  "со spec.md",
             size=10.3, italic=True, color=DEEP, line_spacing=1.22)
    y2 = y1 + h1 + 0.32
    gold_h = 1.05
    gold_callout(s, 0.55, y2, 12.23, gold_h,
                 "«Уточняющий вопрос не задавался. Все параметры задачи были однозначно "
                 "выводимы из текста задачи, поэтому работа была начата сразу, без "
                 "уточнений.»  — строка из захваченной сессии",
                 size=13, anchor=MSO_ANCHOR.MIDDLE)
    y3 = y2 + gold_h + 0.22
    h3 = 2.25
    terminal_card(s, 0.55, y3, half_w, h3, [
        ("index.html", CODE_FG), ("src/main.js", CODE_FG),
        ("package.json", CODE_FG), ("tests/form.spec.ts", CODE_FG),
    ], title="создано агентом", size=12)
    terminal_card(s, rx, y3, half_w, h3, [
        ("npm install", CODE_FG),
        ("npm run build          # → dist/", CODE_FG),
        ("npm run test:e2e       # playwright test", CODE_FG),
    ], title="из финального ответа", size=12)
    speaker_notes(s, load_notes("s04"))


def build_s05(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Два режима",
           "Настраивая агента в новом репозитории, каждый работает в одном из двух "
           "режимов — заложить базу сразу или дождаться реальной проблемы", title_size=19)
    text_box(s, 0.55, 1.75, 12.23, 0.3,
             text="Короткий срез по залу, прежде чем идти дальше.",
             size=12.5, italic=True, color=SLATE)
    gold_callout(s, 0.55, 2.1, 12.23, 0.85,
                 "«Когда вы настраиваете нового агента в новом репозитории — какой из "
                 "двух режимов вам обычно ближе?»", size=15, anchor=MSO_ANCHOR.MIDDLE,
                 align=PP_ALIGN.CENTER)
    y2 = 3.2
    half_w = 5.85
    ocean_box(s, 0.55, y2, half_w, 3.0, fill=SURFACE, stroke=LIGHT)
    text_box(s, 0.75, y2 + 0.15, half_w - 0.4, 0.4, text="A · «Закладываю базу сразу»",
             size=15, bold=True, color=MID)
    text_box(s, 0.75, y2 + 0.7, half_w - 0.4, 1.5,
             text="гейт готовности («что считается сделано»)\n\nтрекинг задач и решений",
             size=13, color=DEEP, line_spacing=1.4)
    rx = 0.55 + half_w + 0.33
    ocean_box(s, rx, y2, half_w, 3.0, fill=SURFACE, stroke=LIGHT)
    text_box(s, rx + 0.2, y2 + 0.15, half_w - 0.4, 0.4, text="B · «Жду, пока не заболит»",
             size=15, bold=True, color=MID)
    text_box(s, rx + 0.2, y2 + 0.7, half_w - 0.4, 1.8,
             text="обзор репозитория\n\nвложенные файлы конвенций\n\nсложная, "
                  "многоуровневая память",
             size=13, color=DEEP, line_spacing=1.4)
    text_box(s, 0.55, y2 + 3.0 + 0.15, 12.23, 0.35,
             text="разбор — на следующем слайде", size=12, italic=True, color=SLATE,
             align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s05"))


def build_s06(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Раздел 0 · Разбор двух режимов",
        "Оба режима рабочие — вопрос в том, к какому типу решения они применяются: "
        "специфичное для проекта ждёт сигнала, универсальная гигиена заводится сразу")
    two_basket_frame(s, 0.55, y, 12.23, 3.0,
                      "специфичное для проекта — ждать сигнала",
                      ["обзор репозитория", "вложенные файлы конвенций",
                       "сложная, многоуровневая память"],
                      "универсальная гигиена — день 0",
                      ["гейт готовности", "трекинг задач и решений"],
                      right_highlight=True)
    y2 = y + 3.0 + 0.25
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2,
                 "«Лекция 3 говорила про тонкого агента — про отказ от структурной "
                 "сложности: субагентов, скиллов, внешнего доступа. Там сигнал нужен. "
                 "Универсальная гигиена — другая категория: здесь ‘жди боли’ работает "
                 "против вас.»", size=12.8, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s06"))


def build_s07(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Раздел 0 · Что заведено в первый день",
        "Кроме спеки и README в репозиторий в тот же день кладётся ещё три вещи — ни "
        "одна из них не ждала сигнала")
    rows = [
        ["spec.md + README.md", "что должно получиться и как устроен репозиторий — "
         "первым коммитом, до задачи агенту"],
        ["CLAUDE.md", "файл инструкций агенту. В первый день в нём одна строка: "
         "критерий «готово» и требование проверить результат руками. Описания "
         "устройства репозитория в нём нет — для него ещё нет причины"],
        ["DECISIONS.md", "журнал решений проекта: что решили и почему. Чтобы "
         "отклонённый вариант не пришлось разбирать заново через месяц"],
        ["Практика файла-на-задачу", "на многошаговую задачу — отдельный файл с "
         "планом и отметками о ходе работы"],
    ]
    th = 3.35
    table_card(s, 0.55, y, 12.23, th, ["Что заведено", "Зачем именно сразу"],
               rows, [0.28, 0.72], header_size=12, cell_size=12.5)
    y += th + 0.2
    gold_callout(s, 0.55, y, 12.23, 0.95,
                 "Каждое из этого стоит сегодня одной строки. Цена отсутствия заранее "
                 "неизвестна и обнаруживается задним числом: сигнала, по которому "
                 "стало бы понятно, что пора, может не быть вовсе.",
                 size=12.5, anchor=MSO_ANCHOR.MIDDLE)
    y += 0.95 + 0.12
    text_box(s, 0.55, y, 12.23, 0.4,
             text="Дальше все четыре встречаются в работе поимённо — каждое в своей "
                  "развилке.",
             size=11.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s07"))


def build_s08(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Раздел 0 · Опорная карта",
        "Конфигурация агента раскладывается на пять слотов; сегодняшний проект "
        "задействует два — инструкции-правила и память")
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
             text="Сегодня в работе — два. Скиллы, субагенты, доступ наружу и "
                  "механические слои (хук, процесс) — Семинар 5.",
             size=14.5, italic=True, bold=True, color=MID, align=PP_ALIGN.CENTER,
             line_spacing=1.2)
    y3 = y2 + 0.6
    gold_callout(s, 0.55, y3, 12.23, 7.0 - y3,
                 "«Оставайтесь на самой нижней ступени, которая закрывает требование "
                 "задачи. Поднимайтесь на следующую только тогда, когда можете назвать "
                 "требование, которое текущая ступень не закрывает. Каждый подъём "
                 "оплачивается новой стоимостью, новыми режимами отказа и новой "
                 "поверхностью атаки.»",
                 size=13, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s08"))


# ============================================================
# Раздел 1 — Файл инструкций (s09-s27)
# ============================================================

def build_s09(p):
    return divider_section_macro(p, "s09",
        title="Раздел 1 · файл инструкций",
        case_lines=["Кейс 1.1 · роль агента и репозиторий",
                    "Кейс 1.2 · базовые процессы: гейты и цикл улучшения",
                    "Кейс 1.3 · вложенные файлы по подпапкам"],
        tag="Один файл, три развилки", active_idx=1, total=4, icon_name="file-text")


def build_s10(p):
    return divider_case_micro(p, "s10",
        title="Кейс 1.1 · роль агента и репозиторий",
        meaning="Чем заполняется пустой файл инструкций",
        tag="первое решение по конфигурации",
        case_idx=0, case_total=3, icon_name="file-text")


def build_s11(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.1 · Роль и репозиторий",
        "Прототип собран, следующая сессия будет завтра — в CLAUDE.md уже есть строка "
        "гейта готовности, остальное пусто, а стандартный первый раздел такого файла "
        "называется «Repository overview»")
    half_w = 5.85
    h1 = 3.35
    terminal_card(s, 0.55, y, half_w, h1, [
        ("README.md", CODE_FG), ("spec.md", CODE_FG), ("DECISIONS.md", CODE_FG),
        ("index.html", CODE_FG), ("package.json", CODE_FG),
        ("src/main.js", CODE_FG), ("tests/form.spec.ts", CODE_FG),
        ("CLAUDE.md ← гейт есть, остальное пусто", GOLD, True),
        ("AGENTS.md → симлинк на CLAUDE.md, заведён на дне 0", CODE_MUTED),
    ], title="состояние репозитория", size=11.5)
    rx = 0.55 + half_w + 0.33
    ocean_box(s, rx, y, half_w, h1)
    text_box(s, rx + 0.2, y + 0.16, half_w - 0.4, h1 - 0.32,
             text="Прототип работает, задач по нему ещё на несколько дней. Разработчик "
                  "заводит CLAUDE.md, чтобы агент в следующих сессиях работал с проектом "
                  "одинаково, и открывает файл — там одна строка, гейт готовности, "
                  "остальное пусто.",
             size=13, color=DEEP, line_spacing=1.3, anchor=MSO_ANCHOR.MIDDLE)
    y2 = y + h1 + 0.25
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2,
                 "Первый раздел, с которого такой файл обычно начинается, — «Repository "
                 "overview»: из чего собран сайт, где лежит форма, какая структура папок. "
                 "Так устроено большинство файлов инструкций, которые можно открыть в "
                 "публичных репозиториях.",
                 size=13.5, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s11"))


def build_s12(p):
    return question_slide(p, "s12", label="Кейс 1.1 · Вопрос",
        title="Выбор из пяти вариантов: что из перечисленного попадёт в файл сейчас, "
              "перед следующей сессией",
        question="«Перед вами пустой CLAUDE.md репозитория signup-landing. Выберите из "
                  "карточек, что попадёт в файл сейчас, перед следующей сессией агента.»",
        options=["подробное описание\nструктуры репозитория", "список технологий\nи "
                 "зависимостей", "инструкцию, где лежит\nформа и как её найти",
                 "неочевидную конвенцию,\nкоторую агент не угадает сам",
                 "пока ничего — до\nпервого реального сигнала"],
        opt_h=1.75)


def build_s13(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.1 · Исследование и разбор",
        "Repository overview измеримо не повышает успешность и стоит контекста — а "
        "структурированное описание, если оно нужно, живёт в README.md и не дублируется "
        "в CLAUDE.md", )
    headers = ["Источник", "Тезис", "Сила"]
    rows = [
        ["Gloaguen et al., arXiv:2602.11988",
         "«are not helpful» — шагов до файла не падает; cost +20–23% без прироста success",
         "Сильное: контролируемый эксперимент"],
        ["Та же работа, абляция",
         "Убрали README — LLM-overview стал полезен (+2,7%)",
         "Подтверждает механизм"],
        ["Lulla et al., arXiv:2601.20404",
         "AGENTS.md про недискаверабельные конвенции: −28,6% runtime (124 PR)",
         "Умеренно «за» — не общее описание"],
        ["Shepard & Albrecht, arXiv:2606.20512",
         "Статичное guidance (28,3%) хуже верифицированного (33,0%, p<0,001)",
         "Косвенное"],
    ]
    th1 = 1.7
    reveal_table(s, 0.55, y, 12.23, th1, headers, rows, [0.28, 0.5, 0.22],
                 row_highlight={0: "gold"}, header_size=9.5, cell_size=9.0)
    y += th1 + 0.12
    headers2 = ["Вариант", "Где работает", "Почему рано — что вместо"]
    rows2 = [
        ["«Описание структуры»", "Почти нигде", "Агент выведет сам за секунды; устареет"],
        ["«Список технологий»", "Версии критичны, не видны", "Обычно тоже выводимо"],
        ["«Инструкция, где форма»", "Почти нигде на малом репо",
         "Шесть файлов — вся структура на одном экране"],
        ["«Неочевидная конвенция»", "Когда реально есть", "Такой конвенции ещё нет"],
        ["«Пока ничего — до сигнала»", "Здесь и сейчас", "ЦЕЛЕВОЙ ОТВЕТ"],
    ]
    th2 = 1.65
    reveal_table(s, 0.55, y, 12.23, th2, headers2, rows2, [0.3, 0.28, 0.42],
                 row_highlight={4: "gold"}, header_size=9.3, cell_size=8.8)
    y += th2 + 0.22
    gold_callout(s, 0.55, y, 12.23, 7.0 - y,
                 "README, не AGENTS.md: структурированное описание репозитория должно "
                 "существовать — этот кейс не отменяет потребность в нём, он называет "
                 "место. Оно живёт в README.md, заведённом первым коммитом, а не "
                 "дублируется в CLAUDE.md. Отдельный «Repository overview» в файле "
                 "инструкций не нужен: описание уже есть, просто в другом файле.",
                 size=12, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s13"))


def build_s14(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.1 · Решение",
        "Описания структуры репозитория в CLAUDE.md не появляется: сигнала для него "
        "нет — а первое содержимое у файла появится уже в следующем кейсе, и по другой "
        "причине")
    terminal_card(s, 0.55, y, 12.23, 3.4, [
        ("README.md", CODE_FG), ("spec.md", CODE_FG), ("DECISIONS.md", CODE_FG),
        ("index.html", CODE_FG), ("package.json", CODE_FG),
        ("src/main.js", CODE_FG), ("tests/form.spec.ts", CODE_FG),
        ("CLAUDE.md        ← заведён, по-прежнему пуст", GOLD, True),
        ("AGENTS.md        → симлинк на CLAUDE.md, заведён на дне 0", CODE_MUTED),
    ], title="состояние репозитория", size=11.5)
    y2 = y + 3.4 + 0.22
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2,
                 "«Описания структуры репозитория в файле нет: сигнала для него нет. "
                 "Пусто — не навсегда: часть содержимого CLAUDE.md появится в нём уже на "
                 "этой неделе, и по другой причине — не по сигналу, а как базовая "
                 "практика.»",
                 size=15.5, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s14"))


def build_s15(p):
    return divider_case_micro(p, "s15",
        title="Кейс 1.2 · базовые процессы",
        meaning="Гейт готовности и цикл «план → код → улучшение» — то, что лежит в "
                "файле с первого дня",
        tag="гейт готовности в файле инструкций",
        case_idx=1, case_total=3, icon_name="file-text")


def build_s16(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.2 · Базовые процессы",
        "Гейт готовности лежит в CLAUDE.md с дня 0 — и дважды подряд «готово» прозвучало "
        "до того, как доставку заявки проверили руками")
    bh = 1.85
    ocean_box(s, 0.55, y, 12.23, bh)
    text_box(s, 0.8, y + 0.14, 11.7, bh - 0.28,
             text="День 0: гейт готовности записан в CLAUDE.md тем же днём, что и "
                  "spec.md — «Всегда прогоняй тесты и вручную проверяй результат перед "
                  "тем как сказать ‘готово’».",
             size=13, color=DEEP, line_spacing=1.28, anchor=MSO_ANCHOR.MIDDLE)
    y2 = y + bh + 0.2
    ocean_box(s, 0.55, y2, 12.23, bh)
    text_box(s, 0.8, y2 + 0.14, 11.7, bh - 0.28,
             text="Первая неделя: заказчик — «заявка не пришла». Агент читает код, правит "
                  "обработчик, прогоняет тест — зелёный — «Готово». Тест проверяет только "
                  "пустые поля. Разработчик напоминает про гейт — агент проверяет руками, "
                  "чинит. Через два дня, другой баг — то же самое: тест зелёный, руками не "
                  "проверено.",
             size=12.3, color=DEEP, line_spacing=1.26, anchor=MSO_ANCHOR.MIDDLE)
    y3 = y2 + bh + 0.18
    gold_callout(s, 0.55, y3, 12.23, 7.0 - y3,
                 "«Гейт-фраза лежала в файле все эти дни и загружалась в начало каждой "
                 "сессии. Оба раза «готово» прозвучало до ручной проверки.»",
                 size=15, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s16"))


def build_s17(p):
    return question_slide(p, "s17", label="Кейс 1.2 · Вопрос",
        title="Гейт-фраза уже есть с самого начала и не сработала — выбор из пяти "
              "вариантов, что делать дальше",
        question="«У вас гейт-фраза в CLAUDE.md есть с самого начала, а поведение агента "
                  "всё равно расходится с ней второй раз подряд — заявка снова не "
                  "проверена руками. Выберите, что вы сделаете дальше — из карточек "
                  "ниже — так, чтобы это реально сработало в следующей сессии.»",
        options=["перепишу фразу\nкапсом / жёстче", "продублирую фразу\nвторым пунктом",
                 "заведу отдельный\nфайл-чеклист рядом",
                 "передам проверку\nмеханизму вне текста",
                 "смирюсь — сработает\nне всегда, это норма"],
        opt_h=1.75)


def build_s18(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Кейс 1.2 · Исследование и разбор (1/2)",
        "Текстовый гейт без тулинга не просто бесполезен, а вреден — регрессии выросли "
        "почти до 10%; ни один вариант, кроме передачи проверки механизму, не решает "
        "проблему системно",
        title_size=12, title_h=0.85)
    y = 0.7 + 0.85 + 0.08
    h1_headers = ["Источник", "Тезис", "Сила"]
    h1_rows = [
        ["SWE-Gate/SpecBench/CapCode/Verif. Horizon (4 препринта)",
         "Согласие 4+ независимых исследований: агенты обходят видимые гейты",
         "Сильное — консенсус"],
        ["TDAD, arXiv:2603.17973",
         "«Сначала пиши тесты» без тулинга — регрессии до 9,94%, хуже отсутствия",
         "Сильное и контринтуитивное"],
        ["Rethinking Agent-Generated Tests",
         "Манипуляция промптом ради частоты тестов — без значимого эффекта",
         "Умеренное — нулевой результат"],
        ["Agent Scaffolding Beats Model Upgrades",
         "Архитектура харнесса даёт +20 п.п.; смена модели — ~1 п.п.",
         "Сильное — механизм против модели"],
    ]
    th1 = 1.6
    reveal_table(s, 0.55, y, 12.23, th1, h1_headers, h1_rows, [0.32, 0.46, 0.22],
                 row_highlight={1: "gold"}, header_size=8.6, cell_size=8.0)
    y += th1 + 0.1
    h2_headers = ["Источник", "Тезис", "Сила"]
    h2_rows = [
        ["Self-planning, 2303.06689", "Планирование перед кодом: +25,4% pass@1",
         "Умеренно-сильное «за»"],
        ["LLMs Cannot Self-Correct, ICLR'24", "Самокоррекция без сигнала ухудшает",
         "Сильное «против» self-review"],
        ["arXiv:2604.10508", "Self-repair с реальной проверкой: +4,9…+30 п.п.",
         "Сильное «за» — с проверкой"],
    ]
    th2 = 1.35
    reveal_table(s, 0.55, y, 12.23, th2, h2_headers, h2_rows, [0.3, 0.48, 0.22],
                 row_highlight={2: "gold"}, header_size=8.6, cell_size=8.0)
    y += th2 + 0.08
    text_box(s, 0.55, y, 12.23, 0.32,
             text="Честный пробел: нет контролируемого эксперимента именно на "
                  "изолированную фразу-гейт в CLAUDE.md — только best-practice "
                  "наблюдения практиков.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.15)
    y += 0.36
    headers3 = ["Вариант", "Где работает", "Почему рано — что вместо"]
    rows3 = [
        ["«Капсом / жёстче»", "Нигде системно", "TDAD: регрессии выросли до 9,94%"],
        ["«Продублирую вторым пунктом»", "Иногда чуть повышает шанс прочитать",
         "Presence paradox: лишняя строка стоит контекста"],
        ["«Отдельный файл-чеклист»", "Помогает человеку, слабо — агенту",
         "Тот же класс решения — снова текст, снова просьба"],
        ["«Передам механизму вне текста»", "Системно работает: +20 п.п.",
         "Верное направление — механизм на следующем слайде"],
        ["«Смирюсь, это нормально»", "Приемлемо для некритичных предпочтений",
         "Для правила, чьё нарушение стоит дорого — решение не решать"],
    ]
    th3 = 1.65
    reveal_table(s, 0.55, y, 12.23, th3, headers3, rows3, [0.28, 0.3, 0.42],
                 row_highlight={3: "teal"}, header_size=8.6, cell_size=7.8)
    speaker_notes(s, load_notes("s18"))


def build_s19(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.2 · Исследование и разбор (2/2)",
        "Правила в промпте — просьбы, правила в коде — законы; текстовый гейт ловит "
        "честную ошибку, но не держится под давлением")
    gold_callout(s, 0.55, y, 12.23, 0.85,
                 "Правила в промпте — это просьбы, правила в коде — это законы. То, что "
                 "мы написали, не стало законом от того, что мы записали его проактивно.",
                 size=13.5, anchor=MSO_ANCHOR.MIDDLE)
    y += 0.85 + 0.16
    text_box(s, 0.55, y, 12.23, 0.3, text="МОЖНО ЛИ СЕГОДНЯ ОБОЙТИСЬ БЕЗ ХУКА",
             size=12.5, bold=True, color=MID)
    y += 0.36
    rows = [
        ["Что гейт даёт", "Ловит честную ошибку — «никто не вспомнил», не «агент "
         "обошёл проверку». Сработал 1 раз из 3: когда про него напомнили вслух"],
        ["Чего не даёт", "Не держится под давлением — срок, спешка. TDAD: усиление "
         "текста подняло регрессии до 9,94%; механизм даёт +20 п.п., модель — ~1 п.п."],
        ["Где граница", "Хук нужен, когда цена нарушения высокая и предсказуемая — "
         "названы конкретное действие, команда и ущерб"],
        ["Где мы в проекте", "Действие названо: «готово» без проверки, дважды подряд, "
         "цена — сорванная доставка к показу. Текста хватает ровно до этого места"],
    ]
    th = 2.55
    table_card(s, 0.55, y, 12.23, th, [], rows, [0.22, 0.78],
               header_size=10, cell_size=10.3)
    y += th + 0.14
    gold_callout(s, 0.55, y, 12.23, 0.95,
                 "Зачем знать про хук, если сегодня его не ставим. Затем, чтобы не "
                 "принять текстовый гейт за решение. Хук нужен не «для надёжности», а "
                 "как ответ на названное действие с названной ценой: назвали — пора, "
                 "не назвали — текста хватает.",
                 size=11, anchor=MSO_ANCHOR.MIDDLE)
    y += 0.95 + 0.12
    text_box(s, 0.55, y, 12.23, 0.4,
             text="Цикл «улучшение»: «посмотри на свой код» — не делать никогда; "
                  "«прогони реальную проверку и поправь по факту» — делать всегда.",
             size=11, italic=True, color=DEEP, line_spacing=1.2)
    speaker_notes(s, load_notes("s19"))


def build_s20(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.2 · Решение",
        "Итоговый файл — пятнадцать строк: критерий готово, гейт-предупреждение, "
        "честная оговорка предела и один разовый шаг, без которого тесты падают не по "
        "делу; AGENTS.md — симлинк на тот же файл")
    half_w = 7.05
    h1 = 7.02 - y          # держим карточки внутри слайда: 15 строк выше прежних 12
    terminal_card(s, 0.55, y, half_w, h1, [
        ("# CLAUDE.md", TEAL, True),
        ("", CODE_FG),
        ("signup-landing: статический лендинг с формой заявки на демо-урок.", CODE_FG),
        ("Готово = npm run build код 0, npx playwright test зелёный, форма", CODE_FG),
        ("отправлена руками из собранного dist/ — и заполненная, и пустая.", CODE_FG),
        ("", CODE_FG),
        ("## Safety / scope boundaries", TEAL, True),
        ("- Никогда не запускать деплой на прод без явного запроса.", CODE_FG),
        ("", CODE_FG),
        ("## Build, test, verify", TEAL, True),
        ("- To verify: открыть dist/index.html после сборки и отправить форму", CODE_FG),
        ("  руками — с заполненными и с пустыми полями.", CODE_FG),
        ("- Один раз на машину, до первого npx playwright test: npm ci, затем", CODE_FG),
        ("  npx playwright install chromium. Без второй команды падают все", CODE_FG),
        ("  тесты сразу и не по делу.", CODE_FG),
    ], size=9.8, line_spacing=1.2)
    rx = 0.55 + half_w + 0.3
    rw = 12.23 - half_w - 0.3
    numbered_card(s, rx, y, rw, h1, [
        "Файл грузится в начало каждой сессии целиком (официальный ориентир — до 200 "
        "строк, наш итог — 15)",
        "@-импорты организуют файл, но не экономят контекст",
        "AGENTS.md — симлинк на тот же файл (ln -s CLAUDE.md AGENTS.md). Острый край: "
        "поведение cp -R на симлинке стандартом не задано (POSIX.1-2024); -P фиксирует "
        "намерение, -L ломает симлинк гарантированно",
    ], size=11.5)
    speaker_notes(s, load_notes("s20"))


def build_s21(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.2 · Что ещё заводится сразу",
        "Гейт — не единственная дешёвая база: ещё три практики заводятся в первый день "
        "и не ждут сигнала")
    items = [
        "создай — прожарь — улучши — покажи и согласуй: черновик плана, фиксированный "
        "список вопросов (самая простая версия? допущения? преждевременная "
        "абстракция? владелец файла? не склеены ли риски?), правки, согласование до "
        "начала работы. Живой пример — команда курса: цикл записан в её файле "
        "инструкций как обязательный",
        "журнал хода работы по задаче, в любом виде — файл на задачу, список шагов, "
        "простой лог. Форма не важна, важно, что он есть — всё, что живёт только в "
        "сессии, к следующей сессии недоступно (подробный разбор — раздел про память)",
        "правило записывается вместе с причиной — строка «почему» рядом с каждым "
        "правилом: какой случай его породил. Без причины правило читается как "
        "вкусовщина и снимается первым; с названной ценой — это готовый критерий, "
        "когда текст пора подпирать механизмом",
    ]
    numbered_card(s, 0.55, y, 12.23, 4.55, items, size=12.3)
    y2 = y + 4.55 + 0.22
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2,
                 "Ни одна из трёх не требует сигнала и не стоит почти ничего в первый "
                 "день. Поэтому их и заводят сразу — вместе с гейтом, а не вместо него.",
                 size=13, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s21"))


def build_s22(p):
    return divider_case_micro(p, "s22",
        title="Кейс 1.3 · вложенные файлы",
        meaning="Месяц спустя репозиторий подрос — дробить файл по подпапкам или нет",
        tag="форма файла, а не содержимое",
        case_idx=2, case_total=3, icon_name="file-text")


def build_s23(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.3 · Два куска знания",
        "За месяц накопились два куска знания разной природы — конвенция целой папки и "
        "деталь про одну функцию, — и разработчик поступает с обоими одинаково: "
        "заводит вложенные файлы инструкций")
    half_w = 5.85
    h1 = 3.25
    ocean_box(s, 0.55, y, half_w, h1)
    text_box(s, 0.75, y + 0.14, half_w - 0.4, h1 - 0.28,
             text="Конвенция папки tests/ — как называются файлы проверок и что со "
                  "страницей работают через объект страницы, а не через селекторы "
                  "напрямую. Нужна всякий раз, когда трогают тесты.\n\n"
                  "Деталь про одну функцию — submitForm() в src/main.js при таймауте "
                  "повторяет запрос один раз, поэтому обработчик на сервере обязан "
                  "быть идемпотентным. Нужна тому, кто правит эту функцию, и больше "
                  "никому.",
             size=11.8, color=DEEP, line_spacing=1.26)
    rx = 0.55 + half_w + 0.33
    terminal_card(s, rx, y, half_w, h1, [
        ("tests/CLAUDE.md     ← конвенция папки", GOLD, True),
        ("src/CLAUDE.md       ← деталь про функцию", GOLD, True),
        ("", CODE_FG),
        ("«Вынесу каждое туда, где оно применяется —", CODE_MUTED),
        (" короче, релевантнее контексту, корневой", CODE_MUTED),
        (" файл не разбухнет.»", CODE_MUTED),
    ], title="что сделал разработчик", size=10.8)
    y2 = y + h1 + 0.22
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2,
                 "«Оба файла лежат в подпапках. Расчёт — что агент прочитает их сам, "
                 "когда будет работать в этих папках.»",
                 size=14, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s23"))


def build_s24(p):
    return question_slide(p, "s24", label="Кейс 1.3 · Вопрос",
        title="Куда положить каждый из двух кусков знания, чтобы агент получил его "
              "тогда, когда оно нужно, и не платил за него в остальных сессиях",
        scenario="Два куска знания: конвенция для всей папки tests/ и деталь про одну "
                  "функцию в src/main.js. Карточек можно выбрать несколько.",
        question="«Выберите из карточек, куда положить каждый кусок, чтобы агент "
                  "получил его тогда, когда оно нужно, и не платил за него в остальных "
                  "сессиях.»",
        options=["вложенный файл\nинструкций в самой папке",
                 "правило с объявленным\nшаблоном путей",
                 "комментарий\nрядом с самим кодом",
                 "отдельный документ +\nуказатель в корневом файле",
                 "дописать в\nкорневой файл инструкций"],
        opt_h=1.75)


def build_s25(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 1.3 · Исследование (1/2)",
        "«Куда положить» — это вопрос «дойдёт ли текст до агента и сколько он стоит»; "
        "у пяти каналов пять разных ответов, и три инструмента из четырёх независимо "
        "сошлись на объявленном шаблоне путей")
    headers = ["Канал", "Когда доходит", "Гарантия", "Цена контекста"]
    rows = [
        ["Корневой файл + @-импорты", "при старте сессии", "есть",
         "платится всегда"],
        ["Правило с шаблоном путей", "когда файл подходит под шаблон", "условная — "
         "триггер явный", "ноль до срабатывания"],
        ["Комментарий рядом с кодом", "когда агент открыл файл", "следует из "
         "механизма", "ноль сверх читаемого"],
        ["Вложенный файл в подпапке", "если инструмент так умеет", "НЕТ ни в одном "
         "из 4 инструментов", "ноль до срабатывания"],
        ["Отдельный документ без указателя", "если агент догадается", "нет",
         "ноль — и ноль доставки"],
    ]
    th = 2.15
    reveal_table(s, 0.55, y, 12.23, th, headers, rows, [0.3, 0.26, 0.24, 0.2],
                 row_highlight={3: "gold"}, header_size=9.5, cell_size=8.9)
    y += th + 0.1
    headers2 = ["Инструмент", "Объявленный шаблон путей", "«Просто положи файл в папку»"]
    rows2 = [
        ["Claude Code", ".claude/rules/*.md, поле paths:", "вложенный CLAUDE.md — "
         "#2571 закрыт «not planned»"],
        ["Cursor", ".cursor/rules/*.mdc, поле globs:", "вложенные AGENTS.md — "
         "признанный баг"],
        ["VS Code (Copilot)", ".instructions.md, поле applyTo:", "вложенные "
         "AGENTS.md — экспериментально, выключено по умолчанию"],
        ["Copilot CLI", "—", "рекурсивного обнаружения нет вовсе — #3051"],
    ]
    th2 = 1.85
    reveal_table(s, 0.55, y, 12.23, th2, headers2, rows2, [0.2, 0.34, 0.46],
                 header_size=9.3, cell_size=8.6)
    y += th2 + 0.1
    text_box(s, 0.55, y, 12.23, 7.15 - y,
             text="Обещание «агенты автоматически читают ближайший файл в дереве "
                  "каталогов» даёт стандарт agents.md — описание типичного поведения, "
                  "не требование к инструменту. Обещание не выполняется, потому что "
                  "его никто и не давал.",
             size=11, italic=True, color=SLATE, line_spacing=1.22)
    speaker_notes(s, load_notes("s25"))


def build_s26(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Кейс 1.3 · Исследование (2/2) и разбор",
        "Ни одно из двух контролируемых измерений не нашло, что распределение "
        "документации улучшает результат — канал выбирается по доставке и цене",
        title_size=11.5, title_h=0.85)
    y = 0.7 + 0.85 + 0.08
    headers = ["Источник", "Тезис", "Сила"]
    rows = [
        ["McMillan, 2605.10039 (1650 сессий)",
         "Ни одна из 4 структурных переменных не дала эффекта",
         "Сильное и контринтуитивное"],
        ["Khatri, 2607.27250 (288 прогонов)",
         "Файл нет/каждый ход/раздельные документы — все в пределах 2 п.п., значимости нет",
         "Сильное по замыслу, слабое по мощности"],
        ["Vasilopoulos, 2602.20478 (283 сессии)",
         "Единственный построенный целиком свод: ядро + документы по требованию",
         "Слабое — один человек, без контроля"],
        ["Он же, про режим отказа",
         "«Агенты доверяют документации абсолютно» — устаревание главный режим отказа",
         "Прямое наблюдение владельца"],
    ]
    th1 = 1.6
    reveal_table(s, 0.55, y, 12.23, th1, headers, rows, [0.28, 0.5, 0.22],
                 row_highlight={0: "gold"}, header_size=8.5, cell_size=7.9)
    y += th1 + 0.08
    text_box(s, 0.55, y, 12.23, 0.42,
             text="Честно про пробел: «не нашли эффекта» ≠ «эффекта нет»; гарантия "
                  "комментария в коде выведена из механизма, не измерена; шаблон путей "
                  "— тоже условная загрузка, не гарантия.",
             size=9.3, italic=True, color=SLATE, line_spacing=1.15)
    y += 0.46
    headers2 = ["Вариант", "Где работает", "Почему рано — что вместо"]
    rows2 = [
        ["«Вложенный файл в папке»", "Нигде гарантированно",
         "Единственный вариант без гарантии во всех 4 инструментах"],
        ["«Правило с шаблоном путей»", "Когда у класса файлов есть конвенция",
         "Верно, но не у нас — конвенция tests/ помещается в 2 строки"],
        ["«Комментарий рядом с кодом»", "Всегда — для знания про код",
         "Часть целевого ответа — единственный канал, где доставка следует из механизма"],
        ["«Документ + указатель в корне»", "Когда документ есть и его поддерживают",
         "Часть целевого ответа — и ответ на «где живёт свод»"],
        ["«Дописать в корневой файл»", "Когда знание нужно в каждой сессии",
         "Presence paradox: строка про tests/ стоит контекста и без тестов"],
    ]
    th2 = 1.65
    reveal_table(s, 0.55, y, 12.23, th2, headers2, rows2, [0.26, 0.28, 0.46],
                 row_highlight={2: "gold", 3: "gold"}, header_size=8.5, cell_size=7.8)
    y += th2 + 0.1
    gold_callout(s, 0.55, y, 12.23, 7.3 - y,
                 "Знание про функцию — в код. Про класс файлов — в правило с шаблоном "
                 "путей. Про весь проект — в корень, коротко, указателями. Вложенный "
                 "файл в подпапке — единственное место, куда знание класть не надо.",
                 size=10.5, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s26"))


def build_s27(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Кейс 1.3 · Решение",
        "Корневой файл остался тем же, на пятнадцать строк — деталь ушла комментарием "
        "к функции, конвенция тестов уже в самих тестах, ни одного вложенного файла "
        "инструкций не завелось",
        title_size=12, title_h=1.0)
    y = 0.7 + 1.0 + 0.1
    terminal_card(s, 0.55, y, 12.23, 2.8, [
        ("README.md · spec.md · DECISIONS.md", CODE_FG),
        ("CLAUDE.md              ← те же 15 строк, не выросли", CODE_FG),
        ("AGENTS.md              → симлинк на CLAUDE.md", CODE_FG),
        ("index.html · package.json", CODE_FG),
        ("src/main.js  ← комментарий к submitForm(): повтор при", GOLD, True),
        ("               таймауте, обработчик обязан быть идемпотентным", GOLD, True),
        ("tests/  form.spec.ts, delivery.spec.ts, page-objects/form.page.ts", CODE_FG),
        ("# tests/CLAUDE.md и src/CLAUDE.md — не появляются", CODE_MUTED, True),
    ], title="состояние репозитория, месяц 1", size=9.6, line_spacing=1.16)
    y += 2.8 + 0.12
    headers = ["Адрес", "Когда включать", "Когда рано"]
    rows = [
        ["Комментарий в коде", "сразу, без сигнала", "никогда не рано"],
        ["Правило с шаблоном путей", "конвенция класса файлов не помещается в корень",
         "пока конвенция в две строки"],
        ["Указатель-свод в корне", "документ уже есть и его есть кому поддерживать",
         "указатель без документа"],
        ["Вложенный файл в подпапке", "никогда как единственная гарантия",
         "всегда, пока /context не проверен"],
    ]
    th = 1.55
    reveal_table(s, 0.55, y, 12.23, th, headers, rows, [0.26, 0.4, 0.34],
                 header_size=9.5, cell_size=9.0)
    y += th + 0.14
    gold_callout(s, 0.55, y, 12.23, 7.3 - y,
                 "«Три развилки, один и тот же файл: решили, чего в него не писать "
                 "заранее; записали гейт готовности, заведённый на дне 0; и решили, что "
                 "у знания есть адрес — и вложенная папка им не является. Но есть "
                 "знание другого рода: то, что появляется по ходу самой работы. Это "
                 "раздел второй — память.»",
                 size=11, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s27"))


# ============================================================
# Раздел 2 — Память (s28-s54)
# ============================================================

def build_s28(p):
    return divider_hybrid(p, "s28",
        big_title="Раздел 2 · память",
        subtitle="Кейс 2.1 · плоский файл",
        meaning="Между сессиями агент не хранит ни бита — если это не лежит на диске",
        tag="журнал решений проекта",
        icon_name="database", macro_idx=2, macro_total=4, micro_idx=0, micro_total=3,
        case_lines=[
            "Кейс 2.1 · плоский файл",
            "Кейс 2.2 · структурированная вики-память",
            "Кейс 2.3 · операционная память",
        ])


def build_s29(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.1 · Плоский файл",
        "Конец первой недели: отклонённое решение по валидации всплывает снова — "
        "DECISIONS.md заведён на дне 0, но записи об этом решении в нём нет")
    sh = 2.55
    ocean_box(s, 0.55, y, 12.23, sh)
    text_box(s, 0.78, y + 0.14, 11.8, sh - 0.28,
             text="Конец первой недели работы над signup-landing. Заказчик прислал заявку "
                  "с опечаткой в домене почты, форма её приняла. Разработчик просит агента "
                  "ужесточить проверку. Агент предлагает подключить стороннюю библиотеку "
                  "валидации форм — ту самую, которую обсуждали и отклонили несколько дней "
                  "назад: форма из двух полей, хватает нативных required/pattern.",
             size=13.5, color=DEEP, line_spacing=1.3, anchor=MSO_ANCHOR.MIDDLE)
    y += sh + 0.22
    gold_callout(s, 0.55, y, 12.23, 7.0 - y,
                 "«DECISIONS.md заведён на дне 0, в тот же день, что spec.md и README. "
                 "Записи про библиотеку валидации в нём нет: решение прозвучало в рабочем "
                 "обсуждении и на диск не попало. Модель между вызовами не хранит ни бита "
                 "— то, чего нет в файле, во второй сессии не существует.»",
                 size=14, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s29"))


def build_s30(p):
    return question_slide(p, "s30", label="Кейс 2.1 · Вопрос",
        title="Выберите, куда записать отклонённое решение — из карточек ниже — так, "
              "чтобы не объяснять его в третий раз",
        scenario="напоминание: отклонённая библиотека валидации всплыла снова — решение "
                 "родилось в разговоре и нигде не осталось, даже при уже заведённом "
                 "DECISIONS.md",
        question="«Вы второй раз за две недели объясняете агенту, почему в этой форме "
                  "нет сторонней библиотеки валидации. Выберите, куда записать это "
                  "решение — из карточек ниже — так, чтобы не объяснять его в третий раз, "
                  "и обоснуйте, почему не в тот файл инструкций, который мы только что "
                  "завели.»",
        options=["дописать\nв CLAUDE.md", "сказать агенту\n«запомни это»",
                 "записать в\nDECISIONS.md — он уже есть", "поставить систему\nпамяти",
                 "ничего — сам\nзапомнит"],
        opt_h=1.6)


def build_s31(p):
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
    speaker_notes(s, load_notes("s31"))


def build_s33(p):
    headers = ["Вариант", "Где это работает", "Почему здесь ещё рано — и что вместо"]
    rows = [
        ["«Допишу в CLAUDE.md»", "Механически сработает: файл читается каждую сессию",
         "Смешивает стабильные правила и растущий лог решений. На десятке решений файл "
         "выйдет за ориентир в 200 строк"],
        ["«Ничего, агент сам запомнит»", "Нигде: это не настройка, которую забыли "
         "включить",
         "Модель не имеет состояния между вызовами по конструкции"],
        ["«Скажу агенту ‘запомни это’»", "Для личного предпочтения — идеально",
         "Половина ответа. Уходит в авто-память: машинно-локальный слой без "
         "синхронизации и код-ревью"],
        ["«Запишу в DECISIONS.md — он уже есть»", "Для командного решения с "
         "обоснованием — именно то, что нужно",
         "Вторая половина ответа. Дело не в создании, а в дисциплине: писать «почему», "
         "а не «что»"],
        ["«Поставлю систему памяти»", "На десятках-сотнях записей, нескольких "
         "пользователях",
         "Рано на порядок: на малых корпусах простой файл регулярно конкурентен со "
         "сложными системами"],
    ]
    return answer_slide(p, "s33", label="Кейс 2.1 · Разбор",
        title="Командное решение с обоснованием идёт в DECISIONS.md, личное предпочтение "
              "— в авто-память, выводимое из кода — никуда",
        context_q="Куда записать отклонённое решение — и почему не в файл инструкций?",
        headers=headers, rows=rows, col_w=[0.24, 0.3, 0.46], gold_rows=[],
        footer="целевой ответ — оба механизма разом, с разделением ролей",
        table_h=3.7, footer_h=0.7, footer_size=15)


def build_s34(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.1 · Совместное формирование",
        "Не всё, что узнал агент, вообще стоит записывать — третья корзина такая же "
        "законная, как первые две")
    bh = 2.7
    basket_row(s, 0.55, y, 12.23, bh, [
        ("авто-память", ["Разработчик просит отвечать\nкоротко, без преамбул"]),
        ("DECISIONS.md", ["Сторонний виджет валидации в форму\nне добавляем — форма из "
                           "двух полей", "Своего бэкенда не делаем — заявка\nуходит на "
                           "внешний сервис приёма форм"]),
        ("никуда", ["Обработчик формы лежит\nв src/main.js",
                     "24 сентября тест упал из-за\nтаймаута, увеличили ожидание"]),
    ], highlight_idx=2)
    y2 = y + bh + 0.25
    terminal_card(s, 0.55, y2, 12.23, 7.0 - y2, [
        ("## 2026-09-24 — сторонние виджеты в форму не добавляем", TEAL, True),
        ("Форма — два поля (имя, email), хватает нативных required/pattern в", CODE_FG),
        ("index.html. Сторонний виджет — лишняя зависимость и лишние килобайты", CODE_FG),
        ("в сборке ради этого объёма.", CODE_FG),
    ], title="собранная запись — реальный файл демо-репозитория (коммит 94c5378)", size=11.5)
    speaker_notes(s, load_notes("s34"))


def build_s35(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.1 · Решение",
        "Новое — не файл (он заведён на дне 0), а первая содержательная запись в нём, "
        "датированная днём, когда решение записали")
    half_w = 6.7
    h = 4.45
    terminal_card(s, 0.55, y, half_w, h, [
        ("# Decisions", TEAL, True),
        ("", CODE_FG),
        ("Append-only log of why, in date order.", CODE_MUTED),
        ("", CODE_FG),
        ("## 2026-09-24 — сторонние виджеты в форму не добавляем", TEAL, True),
        ("Форма — два поля (имя, email), хватает нативных required/pattern", CODE_FG),
        ("в index.html. Сторонний виджет — лишняя зависимость и лишние", CODE_FG),
        ("килобайты в сборке ради этого объёма.", CODE_FG),
    ], title="DECISIONS.md — целиком", size=11)
    rx = 0.55 + half_w + 0.3
    rw = 12.23 - half_w - 0.3
    terminal_card(s, rx, y, rw, h, [
        ("README.md", CODE_FG), ("spec.md", CODE_FG),
        ("DECISIONS.md", GOLD, True),
        ("CLAUDE.md", CODE_FG), ("AGENTS.md", CODE_FG), ("index.html", CODE_FG),
        ("package.json", CODE_FG), ("src/main.js", CODE_FG),
        ("tests/form.spec.ts", CODE_FG),
        ("tests/delivery.spec.ts", CODE_FG),
        ("tests/page-objects/form.page.ts", CODE_FG),
    ], title="состояние репозитория, неделя 1", size=10.5)
    speaker_notes(s, load_notes("s35"))


def build_s32(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.1 · Четыре слоя",
        "Разница между слоями не в формате, а в том, кто инициирует запись, кто её "
        "потом увидит и по какому механизму она вообще попадает в контекст")
    headers = ["", "Файл инстр.", "Авто-память", "DECISIONS.md", "Сложная система"]
    rows = [
        ["Кто автор", "вы, заранее", "агент, по ходу", "вы, в момент решения",
         "сервис, сам"],
        ["Где живёт", "в репо, git", "вне репо, на машине", "в репо, git",
         "вне репо, отдельно"],
        ["Что грузится", "целиком, каждую сессию", "индекс: 200 строк / 25 КБ",
         "ничего автоматически", "ничего автоматически"],
        ["Код-ревью", "да", "нет", "да", "нет"],
        ["Смена машины", "да", "нет", "да", "да, если доступен"],
        ["Что туда идёт", "стабильные правила", "предпочтения, подходы",
         "решения и «почему»", "что сервис счёл достойным"],
    ]
    th = 3.55
    reveal_table(s, 0.55, y, 12.23, th, headers, rows, [0.19, 0.2, 0.2, 0.2, 0.21],
                 header_size=10, cell_size=9.2)
    y += th + 0.16
    text_box(s, 0.55, y, 12.23, 0.75,
             text="индекс памяти — только индекс  ·  агент сам пропускает выводимое из "
                  "кода  ·  сжатие контекста переживают только файлы на диске  ·  "
                  "усложнение слоя само по себе результата не улучшает",
             size=11.5, italic=True, color=MID, align=PP_ALIGN.CENTER, line_spacing=1.2)
    speaker_notes(s, load_notes("s32"))


def build_s36(p):
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
    speaker_notes(s, load_notes("s36"))


def build_s37(p):
    return criteria_slide(p, "s37", label="Кейс 2.1 · Критерий и граница",
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


def build_s38(p):
    return divider_case_micro(p, "s38",
        title="Кейс 2.2 · структурированная вики-память",
        meaning="Тот же DECISIONS.md, четыре месяца спустя",
        tag="структура журнала решений",
        case_idx=1, case_total=3, icon_name="git-branch")


def build_s39(p):
    return scenario_pain_slide(p, "s39", label="Кейс 2.2 · Вики-память",
        title="Четвёртый месяц: в DECISIONS.md двести записей, две из них относятся к "
              "одному вопросу — и ни одна не ссылается на другую",
        scenario="Четвёртый месяц работы над signup-landing. На форму пошёл спам; в "
                 "команде к этому времени работает ещё один разработчик, который прежних "
                 "обсуждений не застал, и он просит агента поставить защиту.\n\n"
                 "Агент читает DECISIONS.md — двести записей — и отвечает по "
                 "записи от 26 сентября: «сторонние виджеты в форму не добавляем». Значит, "
                 "капча отпадает, и агент предлагает обсуждать вопрос заново.\n\n"
                 "Запись от 28 ноября — «антиспам делаем honeypot-полем, без капчи» — "
                 "лежит на полторы сотни записей ниже, ближе к концу файла, и "
                 "закрывает ровно этот случай. Ни "
                 "сентябрьская запись не ссылается на ноябрьскую, ни ноябрьская на "
                 "сентябрьскую.",
        bottom_line="«Обе записи лежат в одном файле. В плоском append-only логе найти "
                     "обе можно только линейным чтением всех двухсот.»",
        note="Пример иллюстративный — реального DECISIONS.md на 200 записей не захвачено.")


def build_s40(p):
    return question_slide(p, "s40", label="Кейс 2.2 · Вопрос",
        title="Разросшийся журнал решений и потерянная связь между двумя записями — "
              "повод выбрать, как его реорганизовать, а не заводить заново",
        question="«DECISIONS.md разросся, и в нём уже есть решение, которое отменяет "
                  "часть более раннего решения, — без единой ссылки между ними. "
                  "Выберите, как реорганизовать этот файл — из карточек ниже — так, "
                  "чтобы агент быстро находил нужное решение и видел связи между "
                  "решениями, а не листал линейный лог с начала. Обоснуйте выбор.»",
        options=["оставить как есть —\nпросто грепать",
                 "разбить на отдельные\nфайлы со ссылками",
                 "поставить графовую/\nвекторную систему памяти",
                 "завести один общий\nSUMMARY.md, переписываемый целиком",
                 "агент сам найдёт\nчерез поиск по репозиторию"],
        opt_h=1.75)


def build_s41(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.2 · Исследование",
        "Плоская память деградирует со временем, а структура может окупаться именно "
        "для агента там, где не окупается для человека — но «умнее» не значит «лучше»")
    text_box(s, 0.55, y, 12.23, 0.5,
             text="почти все источники ниже — свежие непроверенные препринты 2026 года; "
                  "цифры — «заявлено в препринте», а не установленный факт",
             size=10.8, italic=True, color=SLATE, line_spacing=1.2)
    y += 0.58
    ocean_box(s, 0.55, y, 12.23, 1.55)
    text_box(s, 0.78, y + 0.12, 11.75, 1.31,
             text="MEMTIER (arXiv:2605.03675): плоская память деградирует на горизонте "
                  "порядка 72 часов работы — минус 14 п.п. успешности вызовов "
                  "инструментов (насыщение контекста, temporal decay, semantic drift). "
                  "Логика «raw sources → wiki → schema»: у человека вики умирает — "
                  "поддержка дороже ценности; у агента стоимость правки полутора "
                  "десятков файлов близка к нулю.",
             size=11.3, color=DEEP, line_spacing=1.24)
    y += 1.55 + 0.18
    headers = ["Система", "LoCoMo (долговременная память)"]
    rows = [["Файловое хранилище (авто-индекс + поиск по смыслу, не только grep)", "74,0%"],
            ["Mem0 (graph-based)", "68,5%"]]
    th = 1.3
    reveal_table(s, 0.55, y, 12.23, th, headers, rows, [0.72, 0.28],
                 row_highlight={0: "gold"}, header_size=11.5, cell_size=13)
    y += th + 0.14
    text_box(s, 0.55, y, 12.23, 7.0 - y,
             text="Летта-контрпример: простое хранилище обошло графовую систему памяти "
                  "— модели тренированы на файловых операциях как на самом привычном "
                  "инструменте.",
             size=11.5, italic=True, color=SLATE, line_spacing=1.25)
    speaker_notes(s, load_notes("s41"))


def build_s42(p):
    headers = ["Вариант", "Где это работает", "Почему здесь ещё рано — и что вместо"]
    rows = [
        ["«Оставить как есть, просто грепать»", "Пока записей десятки и они "
         "укладываются в контекст целиком",
         "Деградация плоской памяти со временем задокументирована (~72 ч, −14 п.п.); "
         "наш файл уже перерос эту границу"],
        ["«Разбить на отдельные файлы (по одному на решение) со сквозными ссылками»", "Именно этот случай",
         "Целевой ответ, но не бесплатный — структура сама создаёт новую нагрузку "
         "(staleness, дублирование, поддержка)"],
        ["«Поставлю графовую/векторную систему памяти»", "На больших "
         "многопользовательских корпусах с семантическим поиском",
         "Контрпример прямо про наш масштаб: файловое хранилище обошло graph-based "
         "систему на LoCoMo"],
        ["«Один общий SUMMARY.md, переписываемый целиком»", "Для совсем маленького "
         "проекта",
         "Переписывание целиком убивает append-only гарантию"],
        ["«Агент сам найдёт через поиск по репозиторию»", "Для фактов, выводимых из "
         "кода",
         "Решения — не факты кода. «Сам найдёт» — то же заблуждение, что «сам "
         "запомнит»"],
    ]
    return answer_slide(p, "s42", label="Кейс 2.2 · Разбор",
        title="Разбить на отдельные файлы (по одному на решение) со сквозными ссылками — "
              "целевой ответ, но не бесплатный: структура сама создаёт новую нагрузку",
        context_q="Как реорганизовать разросшийся журнал решений?", headers=headers,
        rows=rows, col_w=[0.26, 0.28, 0.46], gold_rows=[1],
        footer="целевой ответ — разбить на отдельные файлы (по одному на решение) со "
               "сквозными ссылками, со списком реальных издержек, а не как безусловный апгрейд",
        table_h=3.65, footer_h=0.85, footer_size=13)


def build_s43(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.2 · Решение",
        "Практика ADR: одно решение — один нумерованный файл, а связь между решениями "
        "— строка в разделе Status, которую инструмент проставляет сразу в обе стороны")
    half_w = 4.7
    h = 3.5
    terminal_card(s, 0.55, y, half_w, h, [
        ("doc/adr/", TEAL, True),
        ("  0001-record-architecture-...md", CODE_FG),
        ("  ...", CODE_MUTED),
        ("  0031-storonnie-vidzhety-...md", CODE_FG),
        ("  ...", CODE_MUTED),
        ("  0187-antispam-honeypot-...md", GOLD, True),
        ("  README.md   ← adr generate toc", CODE_FG),
    ], size=10.8)
    rx = 0.55 + half_w + 0.28
    rw = 12.23 - half_w - 0.28
    terminal_card(s, rx, y, rw, h, [
        ("# 187. Антиспам — honeypot-поле, без капчи", TEAL, True),
        ("Date: 2026-11-28", CODE_MUTED),
        ("", CODE_FG),
        ("## Status", TEAL, True),
        ("Accepted", CODE_FG),
        ("Amends [31. Сторонние виджеты не добавляем]", GOLD, True),
        ("## Context / Decision / Consequences", CODE_MUTED),
        ("...", CODE_MUTED),
    ], title="ноябрьская запись — по шаблону adr-tools", size=9.8)
    y2 = y + h + 0.18
    gold_callout(s, 0.55, y2, 12.23, 0.7,
                 "adr new -l \"31:Amends:Amended by\" ... — и в файл 31 инструмент "
                 "сам дописал встречную строку Amended by [187...]. Обе ссылки написал "
                 "инструмент, а не автор записи.",
                 size=11, anchor=MSO_ANCHOR.MIDDLE)
    y2 += 0.7 + 0.14
    text_box(s, 0.55, y2, 12.23, 7.0 - y2,
             text="Источник практики: ADR — Майкл Найгард, 2011; adr-tools. Сила "
                  "доказательства: задокументированная практика для людей (4500+ ADR в "
                  "750 проектах), но контролируемого измерения «ADR помогают агенту» "
                  "нет. Содержимое записей иллюстративное, ждёт живой сессии.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.22)
    speaker_notes(s, load_notes("s43"))


def build_s44(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.2 · Контрпример: что именно измерили",
        "Файловое хранилище обошло графовую память — но измеряли вопросы по длинному "
        "диалогу, а не поиск связанного решения в журнале проекта")
    ocean_box(s, 0.55, y, 12.23, 1.05)
    text_box(s, 0.75, y + 0.1, 11.85, 0.85,
             text="LoCoMo — бенчмарк памяти в очень длинных диалогах (Maharana и др., "
                  "2024): переписка двух собеседников, до 35 сессий, ~300 реплик, ~9 "
                  "тыс. токенов. Доля вопросов о фактах переписки с верным ответом.",
             size=10.8, color=DEEP, line_spacing=1.2)
    y += 1.05 + 0.14
    headers = ["Система", "LoCoMo (долговременная память)"]
    rows = [["Файловое хранилище Letta (авто-индекс + поиск по смыслу, не только grep)",
              "74,0%"],
            ["Mem0, графовый вариант (число из публикации Mem0)", "68,5%"]]
    th = 1.3
    reveal_table(s, 0.55, y, 12.23, th, headers, rows, [0.72, 0.28],
                 row_highlight={0: "gold"}, header_size=11, cell_size=12)
    y += th + 0.14
    text_box(s, 0.55, y, 12.23, 0.4,
             text="объяснение авторов: модели тренированы на файловых операциях как на "
                  "самом привычном инструменте", size=11, italic=True, color=SLATE)
    y += 0.45
    items = [
        "Это не один прогон — числа из двух разных публикаций; авторы Letta сами "
        "называют такое сравнение «яблоки с апельсинами».",
        "«Файловое хранилище» — не «только grep»: файл индексируется, поиск по смыслу "
        "у агента был.",
        "Задача другая: измеряли вопросы о фактах переписки, а не поиск связанного "
        "решения в журнале решений проекта. Наш случай никто не мерил.",
    ]
    criterion_plate(s, 0.55, y, 12.23, 7.0 - y, items,
                     title="ЧЕГО ЭТОТ РЕЗУЛЬТАТ НЕ ГОВОРИТ", size=11)
    speaker_notes(s, load_notes("s44"))


def build_s45(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.2 · Цена структуры — на нашем же doc/adr/",
        "Четыре издержки структуры — не общие категории, а конкретные файлы нашего же "
        "doc/adr/: сгенерированное оглавление, лишняя запись, осиротевшее обоснование "
        "и ручная сверка")
    cards = [
        ("clock", "Устаревание (staleness)",
         "README.md собран командой adr generate toc в октябре. Записи с 0188 по 0200 "
         "в него не попали, а выглядит он полным."),
        ("git-fork", "Дублирование (duplication)",
         "Кто-то не нашёл 0187 и завёл 0193 «Пороги антиспама» про тот же honeypot. "
         "Обе Accepted, ссылки между ними нет."),
        ("git-branch", "Нет каскадного удаления",
         "0031 отменили — статус и ссылки перевелись. Но 0187 обоснована фразой "
         "«запрещено решением 31» и осталась Accepted."),
        ("cog", "Нагрузка на поддержку",
         "Двести решений — двести файлов: номер, дата, статус, ссылки, регенерация "
         "оглавления. Заметить дубль не делает никто."),
    ]
    cw = (12.23 - 0.3) / 2
    ch = 2.0
    for i, (icon_name, header_text, body) in enumerate(cards):
        cx = 0.55 + (i % 2) * (cw + 0.3)
        cy = y + (i // 2) * (ch + 0.2)
        failure_card(s, cx, cy, cw, ch, icon_name=icon_name, header_text=header_text,
                     body=body, body_size=11, header_size=13)
    y2 = y + 2 * ch + 0.2 + 0.18
    text_box(s, 0.55, y2, 12.23, 7.0 - y2,
             text="У человека эта нагрузка обычно убивает вики — наблюдение, не "
                  "измерение. У агента правка полутора десятков файлов за проход "
                  "стоит почти ноль — но это гипотеза о механизме. Структура — "
                  "компромисс, не бесплатный апгрейд.",
             size=10.8, italic=True, color=SLATE, line_spacing=1.2,
             align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s45"))


def build_s46(p):
    return criteria_slide(p, "s46", label="Кейс 2.2 · Критерий и мост",
        title="Единицы связей на запись и один-два человека, правящих память, — "
              "структуры достаточно; полноценная система памяти требует замеров на "
              "своём масштабе, не общего совета",
        items=[
            "Связей у записи — единицы, а не десятки: их видно в разделе Status.",
            "Поиск нужной записи — по номеру, названию файла или простому grep, а не "
            "по смысловой близости.",
            "Участников, одновременно правящих память, — один-два.",
            "Никто не просил «найди решения, похожие по смыслу на…».",
        ],
        boundary_text="Смена оси: всё в этом и предыдущем кейсе — про решения, которые "
                       "живут навсегда. Что происходит с памятью одной задачи, пока она "
                       "ещё не закончена?")


def build_s47(p):
    return divider_case_micro(p, "s47",
        title="Кейс 2.3 · операционная память",
        meaning="Смена оси: не решения навсегда, а ход одной задачи между её сессиями",
        tag="память одной задачи",
        case_idx=2, case_total=3, icon_name="clipboard-check")


def build_s48(p):
    return scenario_pain_slide(p, "s48", label="Кейс 2.3 · Задачная память",
        title="Файл задачи заведён на дне 0 и план в нём отмечен по первым шагам — а "
              "договорённость о том, как делать следующий шаг, принятая по ходу первой "
              "сессии, в него не попала",
        scenario="Практика «файл на задачу» заведена на дне 0, вместе с DECISIONS.md: на "
                 "каждую многошаговую задачу — свой файл с планом и логом хода. Задача: "
                 "разбить форму на пошаговый визард — имя, email, подтверждение, — "
                 "сохранив всю текущую валидацию. Файл создан перед началом работы, план "
                 "расписан на шесть шагов.\n\n"
                 "Первая сессия закрывает шаги 1-2. По ходу шага 2 видно, что значения "
                 "полей надо где-то держать между шагами, и в рабочем обсуждении — не "
                 "в плане — выбирается способ: состояние визарда хранить одним объектом "
                 "в sessionStorage, ключ signup-wizard. В лог хода выбранный способ не "
                 "попадает. Сессия обрывается в середине шага 3 — контекст сжимается.\n\n"
                 "Вторая сессия. Агент открывает файл: план на месте, шаги 1-2 отмечены "
                 "выполненными. Про sessionStorage в файле нет ни строки. Агент делает "
                 "шаг 3 самым коротким способом — держит состояние в переменной модуля. "
                 "Тесты шага 5 зелёные. Расхождение всплывает на шаге 6: перезагрузка "
                 "страницы на третьем шаге очищает форму.",
        bottom_line="«На входе во вторую сессию у агента есть ровно то, что лежит в "
                     "файле: шесть шагов плана и две отметки о выполнении. Договорённость "
                     "про хранение состояния осталась в контексте первой сессии, "
                     "которого больше нет.»")


def build_s49(p):
    return question_slide(p, "s49", label="Кейс 2.3 · Вопрос",
        title="Файл задачи существовал с самого начала и всё равно ввёл в заблуждение "
              "— выбор из пяти вариантов",
        question="«Файл задачи существовал с самого начала, план в нём выглядит "
                  "актуальным — первые шаги отмечены сделанными. И всё равно вторая "
                  "сессия делает шаг 3 не так, как договорились в первой. Выберите, что "
                  "нужно сделать иначе — из карточек ниже — так, чтобы файл задачи не "
                  "вводил в заблуждение, а реально отражал ход работы. Обоснуйте "
                  "выбор.»",
        options=["надеяться на\nконтекстное окно",
                 "записать план\nв DECISIONS.md",
                 "правило в CLAUDE.md:\nдоговорённость — сразу в файл",
                 "завести папку на задачу\nс файлом под каждый шаг",
                 "попросить агента\n«продолжи с того места»"],
        opt_h=1.75)


def build_s50(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.3 · Исследование",
        "От Pokémon до recitation — практика структурированных заметок о ходе задачи "
        "известна и работает; и она объясняет, почему наш файл всё равно подвёл")
    ocean_box(s, 0.55, y, 12.23, 2.55)
    text_box(s, 0.78, y + 0.14, 11.75, 2.27,
             text="Anthropic, инженерный блог: «structured note-taking» — агент играет "
                  "в Pokémon тысячи шагов подряд, ведя простые структурированные "
                  "заметки, переживая сбросы контекста без потери прогресса. Manus, "
                  "«recitation»: агент непрерывно переписывает todo.md в конец "
                  "контекста — снижает уход от цели. metasphere-agents: файл на задачу "
                  "в .tasks/active/, архивируется в .tasks/done/ по завершении.",
             size=12, color=DEEP, line_spacing=1.28)
    y2 = y + 2.55 + 0.2
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2,
                 "«Есть измерение на большом числе траекторий: план в среднем помогает. "
                 "Но дословная цитата авторов — ‘плохой план вреднее отсутствия "
                 "плана вообще’. Полную картину с цифрами покажу на слайде провала.»",
                 size=13, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s50"))


def build_s51(p):
    headers = ["Вариант", "Где это работает", "Почему рано — и что вместо"]
    rows = [
        ["«Не сжимать, не закрывать сессию»", "Для задачи, целиком укладывающейся в "
         "одну короткую сессию",
         "Контекстное окно конечно; на многошаговой задаче рано или поздно случится "
         "сжатие или разрыв сессии — это отсутствие стратегии"],
        ["«Записать план в DECISIONS.md»", "Никогда — не тот слой памяти",
         "DECISIONS.md — про решения, которые остаются в силе навсегда; статус одной "
         "задачи туда не относится"],
        ["«Правило в CLAUDE.md: договорённость — сразу в файл задачи»", "Ровно наш "
         "случай — файл уже есть, не хватило строки в инструкциях",
         "Целевой ответ. Адресат — агент, который файл и так ведёт, не память "
         "разработчика"],
        ["«Папка на задачу с файлом под каждый шаг»", "Параллельные подзадачи, "
         "несколько субагентов, разросшийся лог",
         "Оверинжиниринг для одной линейной задачи здесь и сейчас"],
        ["«Попросить ‘продолжи с того места’»", "Внутри одной непрерывной сессии, до "
         "сжатия",
         "После сжатия или в новой сессии буквально нечего продолжать"],
    ]
    return answer_slide(p, "s51", label="Кейс 2.3 · Разбор",
        title="Целевой ответ — строка в CLAUDE.md, обязывающая агента дописывать "
              "договорённость в файл задачи в момент, когда она прозвучала",
        context_q="Файл задачи ввёл в заблуждение — что сделать иначе?", headers=headers,
        rows=rows, col_w=[0.26, 0.3, 0.44], gold_rows=[2],
        footer="целевой ответ — строка в CLAUDE.md, адресованная агенту, с явной "
               "оговоркой об упрощении до файла",
        table_h=3.65, footer_h=0.85, footer_size=12.5)


def build_s52(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Кейс 2.3 · Решение",
        "Новое в этом кейсе — не файл, а три строки в CLAUDE.md: они говорят агенту, "
        "когда в этот файл писать")
    half_w = 4.6
    h = 3.9
    terminal_card(s, 0.55, y, half_w, h, [
        ("## Задачная память", TEAL, True),
        ("- файл .tasks/active/<задача>.md:", CODE_FG),
        ("  план, лог хода, результаты", CODE_FG),
        ("- договорённость дописывать в", CODE_FG),
        ("  «Лог хода» сразу, тем же ответом", CODE_FG),
        ("- в начале и в конце сессии сверять", CODE_FG),
        ("  план с репозиторием, строка", CODE_FG),
        ("  «Сверено: <дата>»", CODE_FG),
    ], title="CLAUDE.md — добавлено", size=10.2, line_spacing=1.22)
    rx = 0.55 + half_w + 0.28
    rw = 12.23 - half_w - 0.28
    terminal_card(s, rx, y, rw, h, [
        ("# Задача: разбить форму на пошаговый визард", TEAL, True),
        ("", CODE_FG),
        ("## План", TEAL, True),
        ("1. [x] Разметка трёх шагов", CODE_FG),
        ("2. [x] Перенос текущей валидации", CODE_FG),
        ("3. [ ] Состояние текущего шага (JS)", CODE_FG),
        ("", CODE_FG),
        ("## Лог хода", TEAL, True),
        ("- 2027-01-26: шаги 1-2 закрыты. Состояние", GOLD, True),
        ("  визарда — sessionStorage, ключ signup-", GOLD, True),
        ("  wizard. Решено по ходу, в плане нет.", GOLD, True),
        ("- 2027-01-28: начат шаг 3 — контекст сжат.", CODE_FG),
        ("", CODE_FG),
        ("## Сверено", TEAL, True),
        ("2027-01-28: план сверен, расхождений нет.", CODE_FG),
    ], title=".tasks/active/signup-wizard.md", size=9.3, line_spacing=1.12)
    y2 = y + h + 0.15
    text_box(s, 0.55, y2, 12.23, 7.45 - y2,
             text="иллюстративный пример, не захваченный вживую · правило в тексте — "
                  "просьба, не закон · упрощение до файла — масштабируется до папки, "
                  "подробнее за пределами этого занятия",
             size=10.3, italic=True, color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.2)
    speaker_notes(s, load_notes("s52"))


def build_s53(p):
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
    speaker_notes(s, load_notes("s53"))


def build_s54(p):
    return criteria_slide(p, "s54", label="Кейс 2.3 · Критерий",
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
# Раздел 3 — Закрытие (s55-s57)
# ============================================================

def build_s55(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Раздел 3 · Синтез",
        "Шесть развилок сегодняшнего занятия делились на два типа: специфичное для "
        "проекта (ждать сигнала) и универсальная гигиена (заводить сразу, на день 0)")
    headers = ["Кейс", "Развилка", "Что мы записали", "Когда"]
    rows = [
        ["1.1", "Роль агента и общее описание репозитория",
         "Ничего — до первого реального сигнала", "по сигналу"],
        ["1.2", "Базовые процессы: гейт «готово» + цикл улучшения",
         "Гейт-фраза текстом в CLAUDE.md", "сразу"],
        ["1.3", "Вложенные файлы инструкций по подпапкам",
         "Правило трёх адресов: функция → код, класс файлов → шаблон, проект → "
         "корень", "по сигналу"],
        ["2.1", "Плоский файл памяти (DECISIONS.md)",
         "Решение записано в файл + авто-память", "сразу"],
        ["2.2", "Структурированная вики-память",
         "Отдельные файлы (ADR) со сквозными ссылками", "по сигналу"],
        ["2.3", "Операционная задачная память",
         "Один файл на задачу: план + лог + результаты", "сразу"],
    ]
    th = 3.65
    reveal_table(s, 0.55, y, 12.23, th, headers, rows, [0.08, 0.37, 0.4, 0.15],
                 row_highlight={0: "teal", 2: "teal", 4: "teal", 1: "gold", 3: "gold",
                                5: "gold"},
                 header_size=11.5, cell_size=11.3)
    y += th + 0.2
    text_box(s, 0.55, y, 12.23, 7.0 - y,
             text="Три развилки ждали реального сигнала. Три — не нуждались в сигнале "
                  "вообще, их стоило завести сразу.",
             size=17, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s55"))


def build_s56(p):
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
    speaker_notes(s, load_notes("s56"))


def build_s57(p):
    """pattern: closing_question — composition deliberately DIFFERS from
    build_s55 (full six-row table), not a shrunk copy of it. Thin arrow-list
    line + dominant large question + tag-line."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    y = auto_header(s, "Раздел 3 · Перенос",
        "Перенесите шесть сегодняшних решений на свой репозиторий — и проверьте, какое "
        "из них реально день-0-база, а какое вы отложили без причины или завели раньше "
        "времени без сигнала")
    text_box(s, 0.55, y, 12.23, 0.4,
             text="1.1  →  1.2  →  1.3  →  2.1  →  2.2  →  2.3",
             size=14, color=MID, align=PP_ALIGN.CENTER)
    y2 = y + 0.45
    gold_callout(s, 0.55, y2, 12.23, 7.0 - y2 - 0.55,
                 "«По каждой развилке спросите: это действительно день-0-база — то, "
                 "что стоило завести сразу, независимо от конкретики проекта? Или вы "
                 "завели это раньше времени, без реального сигнала, просто по "
                 "привычке? А может, наоборот — что-то из универсальной гигиены вы "
                 "всё ещё откладываете без всякой причины?»",
                 size=16.5, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    text_box(s, 0.55, 7.0 - 0.5, 12.23, 0.4, text="«Не вслух. Не на бумаге. Себе.»",
             size=13, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s57"))


# ============================================================
# Main
# ============================================================

SEQ = [f"s{i:02d}" for i in range(1, 58)]


def main():
    p = setup_pres()
    for sid in SEQ:
        fn = globals()[f"build_{sid}"]
        fn(p)
    p.save(str(OUT))
    print(f"Saved {OUT} — {len(p.slides)} slides")


if __name__ == "__main__":
    main()
