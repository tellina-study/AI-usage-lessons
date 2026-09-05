"""
Build script for Семинар 2 — «Воронка решений: когда ИИ, каким и на чём».

Ocean Gradient v3 design system, matched to library/seminars/sem-01 patterns
(reused helpers: text_box, ocean_box, icon, chip, filled_rect, multipara_box,
dashed_box, speaker_notes). Runs idempotently — re-running rebuilds sem-02.pptx
from scratch.

Source-of-truth: deck.yaml + slides/*.md (31 slides).
Canvas: 13.333" x 7.5" (16:9).

Toolchain notes (this environment — no apt/sudo, no system libreoffice, no
PowerPoint MCP):
  - python-pptx / pymupdf / cairosvg / segno installed in user site-packages;
    PYTHONPATH must include that dir (see run instructions / iteration-log.md).
  - cairosvg needs LD_LIBRARY_PATH pointed at the LO sysroot's libcairo.
  - PPTX->PDF via portable LibreOffice; PDF->PNG via pymupdf (fitz).

Gotcha (see notes/mcp-limitations.md [#sem01-render-1]): literal "\\n" inside a
single python-pptx text run does not reliably line-break under LibreOffice —
always use multipara_box (tf.add_paragraph() per line) for multi-line text.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, "/home/harness/harness-control-data/accounts/256/claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages")

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt
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
NEG_TINT = RGBColor(0xFB, 0xEA, 0xEA)
NEG_LINE = RGBColor(0xB0, 0x4A, 0x4A)
POS_TINT = RGBColor(0xE9, 0xF5, 0xF2)

# === Constants ===
SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "rendered/assets"
ICONS = ASSETS / "icons/rendered"
SHOTS = ROOT / "assets/screenshots"
SLIDES_DIR = ROOT / "slides"
OUT = ROOT / "rendered/sem-02.pptx"
FONT_HEAD = "Arial"
FONT_BODY = "Arial"
FONT_MONO = "Courier New"

FUNNEL_STEPS = [
    "ИИ или обычный код?",
    "Встроить или делать своё?",
    "Разовый вызов, RAG или агент?",
    "Внешний API или локальный инференс?",
]


# ============================================================
# Helpers (ported from library/seminars/sem-01/rendered/build_sem01.py)
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


def disable_shadow(shp):
    sppr = shp._element.spPr
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    for el in sppr.findall(ns + "effectLst"):
        sppr.remove(el)
    etree.SubElement(sppr, ns + "effectLst")
    # python-pptx autoshapes carry a <p:style> with <a:effectRef idx="2">
    # pointing at the theme's shadow effect — LibreOffice's PDF export applies
    # this theme effect even when spPr has an explicit empty <a:effectLst/>.
    # Removing <p:style> entirely is the reliable fix (see notes/mcp-limitations.md).
    pns = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
    style_el = shp._element.find(pns + "style")
    if style_el is not None:
        shp._element.remove(style_el)


def text_box(slide, x, y, w, h, text, *,
             size=16, bold=False, italic=False, color=DEEP,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             font=FONT_BODY, line_spacing=1.15):
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
    return tb


def multipara_box(slide, x, y, w, h, paragraphs, *,
                   anchor=MSO_ANCHOR.TOP, align=PP_ALIGN.LEFT):
    """Each item in `paragraphs` is a dict of text_box-style kwargs.
    Uses tf.add_paragraph() per line — literal \\n in one run does not
    line-break reliably under LibreOffice (notes/mcp-limitations.md #sem01-render-1)."""
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


def dashed_box(slide, x, y, w, h, *, fill=SURFACE, stroke=LIGHT, stroke_pt=1.6,
               radius_pt=12.0, dash="dash"):
    shp = ocean_box(slide, x, y, w, h, fill=fill, stroke=stroke, stroke_pt=stroke_pt,
                     radius_pt=radius_pt)
    ln = shp.line._get_or_add_ln()
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    dash_el = etree.SubElement(ln, ns + "prstDash")
    dash_el.set("val", dash)
    return shp


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
    else:
        return slide.shapes.add_picture(str(path), Inches(x), Inches(y))


def icon(slide, name, color_hex, size_px, x, y, w_in):
    path = ICONS / f"{name}-{color_hex}-{size_px}.png"
    return add_image(slide, path, x, y, w=w_in, h=w_in)


def add_image_coverfit(slide, path, x, y, w, h):
    """Full-bleed / hero image helper: fills the (x,y,w,h) box exactly like
    CSS `object-fit: cover` — no stretch distortion (see notes/mcp-limitations.md
    [#73-render-1]: passing both width= and height= to add_picture() stretches
    non-proportionally). Reads real pixel size via Pillow, sizes the picture by
    the constraining dimension, then crops the overflow off-slide via
    pic.crop_left/right/top/bottom so the box is filled edge-to-edge without
    warping the photo's aspect ratio."""
    from PIL import Image
    path = Path(path)
    if not path.exists():
        print(f"WARNING: missing image {path}")
        return None
    img_w_px, img_h_px = Image.open(path).size
    img_ratio = img_w_px / img_h_px
    box_ratio = w / h
    if img_ratio > box_ratio:
        # image wider than box -> constrain by height, crop left/right
        pic = slide.shapes.add_picture(str(path), Inches(x), Inches(y), height=Inches(h))
        rendered_w_in = h * img_ratio
        excess_in = rendered_w_in - w
        frac = (excess_in / rendered_w_in) / 2.0
        pic.crop_left = frac
        pic.crop_right = frac
        pic.left = Inches(x)
        pic.width = Inches(w)
    else:
        # image taller than box -> constrain by width, crop top/bottom
        pic = slide.shapes.add_picture(str(path), Inches(x), Inches(y), width=Inches(w))
        rendered_h_in = w / img_ratio
        excess_in = rendered_h_in - h
        frac = (excess_in / rendered_h_in) / 2.0
        pic.crop_top = frac
        pic.crop_bottom = frac
        pic.top = Inches(y)
        pic.height = Inches(h)
    return pic


def slide_title(slide, text, *, y=0.45, h=1.0, w=12.23, x=0.55, size=28,
                color=DEEP, bold=True, line_spacing=1.15, align=PP_ALIGN.LEFT):
    text_box(slide, x=x, y=y, w=w, h=h, text=text,
             size=size, bold=bold, color=color, line_spacing=line_spacing,
             align=align)


def gold_callout(slide, x, y, w, h, text, *, size=14, bold=True):
    filled_rect(slide, x, y, w, h, GOLD_TINT, stroke=GOLD, stroke_pt=1.2,
                radius=True, radius_adj=0.12)
    text_box(slide, x=x + 0.2, y=y + 0.06, w=w - 0.4, h=h - 0.12, text=text,
             size=size, bold=bold, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.LEFT, line_spacing=1.22)


def speaker_notes(slide, text):
    tf = slide.notes_slide.notes_text_frame
    tf.text = text


def load_notes(slide_id):
    files = list(SLIDES_DIR.glob(f"{slide_id}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding="utf-8")
    # NB: '\n## ' (2 hashes + space) does NOT match '### Self-check' — the
    # Self-check subsection is INSIDE '## Speaker notes' and must be kept
    # verbatim in the PPTX notes (orchestrator check 2026-09-05: earlier
    # truncation at '### Self-check' silently dropped tails on 22/31 slides).
    m = re.search(r"## Speaker notes\s*\n(.*?)(?=\n## |\Z)", md, re.DOTALL)
    notes = m.group(1).strip() if m else ""
    notes = re.sub(r"\n+---\s*$", "", notes)
    return notes.strip()


def mini_funnel(slide, x, y, w, h, active_idx):
    """Compact 4-step funnel-progress widget for section dividers + s02 keystone.
    active_idx: 0-3 for step highlight, or None for s26 (all equal, no highlight)."""
    n = 4
    gap = 0.14
    step_h = (h - gap * (n - 1)) / n
    max_w = w
    min_w = w * 0.5
    for i in range(n):
        sw = max_w - (max_w - min_w) * (i / (n - 1))
        sx = x + (w - sw) / 2
        sy = y + i * (step_h + gap)
        is_active = (active_idx is not None and i == active_idx)
        fill = GOLD if is_active else SURFACE
        stroke = GOLD if is_active else LIGHT
        txt_color = DEEP if is_active else SLATE
        filled_rect(slide, sx, sy, sw, step_h, fill, stroke=stroke, stroke_pt=1.4,
                    radius=True, radius_adj=0.3)
        text_box(slide, sx + 0.12, sy, sw - 0.24, step_h, text=FUNNEL_STEPS[i],
                 size=10, bold=is_active, color=txt_color, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)


def negative_card(slide, x, y, w, h, title, body_paras, *, icon_name="x-circle"):
    filled_rect(slide, x, y, w, h, NEG_TINT, stroke=NEG_LINE, stroke_pt=1.4,
                radius=True, radius_adj=0.06)
    pad = 0.22
    icon(slide, icon_name, "21295C", 64, x + pad, y + pad, 0.4)
    text_box(slide, x + pad + 0.52, y + pad - 0.02, w - 2 * pad - 0.52, 0.45,
             text=title, size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.1)
    multipara_box(slide, x + pad, y + pad + 0.58, w - 2 * pad, h - pad - 0.6, body_paras)


def positive_card(slide, x, y, w, h, title, body_paras, *, icon_name="circle-check"):
    filled_rect(slide, x, y, w, h, POS_TINT, stroke=TEAL, stroke_pt=1.4,
                radius=True, radius_adj=0.06)
    pad = 0.22
    icon(slide, icon_name, "028090", 64, x + pad, y + pad, 0.4)
    text_box(slide, x + pad + 0.52, y + pad - 0.02, w - 2 * pad - 0.52, 0.45,
             text=title, size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.1)
    multipara_box(slide, x + pad, y + pad + 0.58, w - 2 * pad, h - pad - 0.6, body_paras)


def footer_note(slide, text, *, y=7.02):
    text_box(slide, 0.55, y, 12.23, 0.4, text=text, size=12, italic=True, color=LIGHT,
              line_spacing=1.15)


def quote_block(slide, x, y, w, h, text, *, size=15):
    ocean_box(slide, x, y, w, h, fill=SURFACE, stroke=LIGHT)
    pad = 0.24
    icon(slide, "quote", "1C7293", 64, x + pad, y + pad - 0.05, 0.32)
    text_box(slide, x + pad, y + pad + 0.32, w - 2 * pad, h - pad * 2 - 0.32,
             text=text, size=size, italic=True, color=DEEP, line_spacing=1.28,
             anchor=MSO_ANCHOR.TOP)


# ============================================================
# Section-divider builder (s05 / s10 / s15 / s21)
# ============================================================

def build_divider(p, sid, number, title, frame_phrase, active_idx):
    s = blank(p)
    set_slide_bg(s, WHITE)
    # Big background number, upper-left, kept clear of the title band below it
    text_box(s, -0.1, -0.65, 4.6, 3.6, text=number, size=280, bold=True,
             color=SOFT_GREY, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.BOTTOM,
             line_spacing=0.9)
    # Title + frame phrase, mid-left, clear of the number's descender
    text_box(s, 0.6, 3.05, 7.1, 1.4, text=title, size=36, bold=True, color=DEEP,
             line_spacing=1.1)
    gold_callout(s, 0.6, 4.55, 6.75, 1.1, frame_phrase, size=15)
    # Mini funnel progress, right
    mini_funnel(s, 8.15, 1.15, 4.6, 4.85, active_idx)
    text_box(s, 8.15, 6.15, 4.6, 0.3, text="воронка решений", size=11, italic=True,
             color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes(sid))
    return s


# ============================================================
# Slide builders — s01..s29 (+ reserves s28a/s28b)
# ============================================================

def build_s01(p):
    """Hero cover — full-bleed real photo (source-of-truth: visual.pattern =
    hero_cover_real_photo). Real NASA/Wikimedia photo of engineers at work,
    darkened bottom third for legibility, title + subtitle only (no icons,
    no decorative shapes — source explicitly forbids them)."""
    s = blank(p)
    set_slide_bg(s, DEEP)
    img_path = SHOTS / "s01-nasa-engineers-real.jpg"
    if img_path.exists():
        add_image_coverfit(s, img_path, 0, 0, SLIDE_W_IN, SLIDE_H_IN)
    # darken bottom third for text legibility (same recipe as build_s29)
    overlay = filled_rect(s, 0, 4.6, SLIDE_W_IN, 2.9, DEEP)
    overlay.fill.fore_color.rgb = DEEP
    try:
        alpha = etree.SubElement(overlay.fill.fore_color._xFill.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr"),
            "{http://schemas.openxmlformats.org/drawingml/2006/main}alpha")
        alpha.set("val", "80000")
    except Exception:
        pass
    text_box(s, 0.6, 4.85, 7.6, 0.45, text="СЕМИНАР 2", size=16, bold=True,
             color=GOLD, align=PP_ALIGN.LEFT)
    multipara_box(s, 0.6, 5.3, 12.1, 1.35, [
        {"text": "Воронка решений: когда ИИ, каким и на чём", "size": 34, "bold": True,
         "color": WHITE, "line_spacing": 1.12},
    ])
    text_box(s, 0.6, 6.35, 11.6, 0.7,
             text="Четыре выбора, которые инженер проходит прежде, чем открыть редактор кода",
             size=16, italic=True, color=RGBColor(0xC8, 0xD2, 0xDF), line_spacing=1.3)
    text_box(s, 0.6, 7.1, 11.6, 0.32, text="NASA / Cory Huston · Wikimedia Commons · общественное достояние",
             size=10.5, italic=True, color=RGBColor(0xC8, 0xD2, 0xDF))
    speaker_notes(s, load_notes("s01"))


def build_s02(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Воронка из четырёх выборов", size=30)
    text_box(s, 0.55, 1.15, 12.23, 0.55,
             text="Правильный ответ зависит от вводных, которых в постановке почти никогда нет",
             size=15.5, italic=True, color=MID, line_spacing=1.2)

    # Vertical funnel ladder, left ~55%
    fx, fy, fw = 0.6, 2.05, 6.7
    top_h = 0.7
    filled_rect(s, fx + 1.0, fy, fw - 2.0, top_h, DEEP, radius=True, radius_adj=0.12)
    text_box(s, fx + 1.0, fy, fw - 2.0, top_h, text="Задача от заказчика", size=14.5,
             bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    steps = [
        ("1", "ИИ или обычный код?", LIGHT, 6.5),
        ("2", "Встроить в существующее приложение или делать своё?", MID, 5.4),
        ("3", "Разовый вызов модели, RAG или агент?", TEAL, 4.3),
        ("4", "Внешний API или локальный инференс?", DEEP, 3.3),
    ]
    sy = fy + top_h + 0.22
    step_h = 0.92
    gap = 0.16
    for num, label, col, sw in steps:
        sx = fx + (fw - sw) / 2
        filled_rect(s, sx, sy, sw, step_h, col, radius=True, radius_adj=0.10)
        badge = filled_rect(s, sx + 0.14, sy + (step_h - 0.4) / 2, 0.4, 0.4, GOLD,
                             radius=True, radius_adj=0.5)
        text_box(s, sx + 0.14, sy + (step_h - 0.4) / 2, 0.4, 0.4, text=num, size=15,
                 bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, sx + 0.68, sy, sw - 0.85, step_h, text=label, size=13.5, bold=True,
                 color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
        sy += step_h + gap

    # Right column — thesis card
    rx = 7.65
    ocean_box(s, rx, 2.05, 5.15, 4.35, fill=SURFACE, stroke=TEAL, stroke_pt=1.6)
    icon(s, "compass", "065A82", 96, rx + 0.28, 2.3, 0.55)
    text_box(s, rx + 0.28, 3.0, 4.6, 1.1,
             text="Ни один выбор не решается «по умолчанию» — он решается заново для каждой задачи",
             size=16, bold=True, color=DEEP, line_spacing=1.25)
    gold_callout(s, rx + 0.28, 4.25, 4.6, 1.05,
                 "Главный навык — не помнить схему, а вовремя задать вопрос, который изменит ответ",
                 size=13.5)
    text_box(s, rx + 0.28, 5.55, 4.6, 0.75,
             text="Сегодня — 7 постановок, почти в каждой ответ поменяется хотя бы раз",
             size=12.5, italic=True, color=SLATE, line_spacing=1.25)
    speaker_notes(s, load_notes("s02"))


def build_s03(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "RAG одним потоком", size=28)
    text_box(s, 0.55, 1.05, 9.5, 0.5,
             text="Нужен, когда база знаний большая и меняется — и не помещается в один запрос",
             size=15, italic=True, color=MID, line_spacing=1.2)
    chip(s, 11.15, 1.0, 1.65, 0.42, "Лекция 3 →", fill=TEAL, size=11.5)

    steps = [
        ("search", "Вопрос пользователя"),
        ("database", "Поиск фрагментов\nв базе знаний"),
        ("layers", "Фрагменты →\nв контекст модели"),
        ("sparkles", "Модель генерирует\nответ"),
    ]
    grid_y = 2.35
    grid_h = 2.9
    n = 4
    gap_arrow = 0.55
    cw = (12.23 - gap_arrow * (n - 1)) / n
    for i, (ic, lbl) in enumerate(steps):
        cx = 0.55 + i * (cw + gap_arrow)
        ocean_box(s, cx, grid_y, cw, grid_h)
        icon(s, ic, "065A82", 96, cx + (cw - 0.6) / 2, grid_y + 0.35, 0.6)
        lines = lbl.split("\n")
        paras = [{"text": ln, "size": 13.5, "bold": True, "color": DEEP,
                  "align": PP_ALIGN.CENTER, "line_spacing": 1.15} for ln in lines]
        multipara_box(s, cx + 0.12, grid_y + 1.15, cw - 0.24, 1.6, paras, align=PP_ALIGN.CENTER)
        chip(s, cx + 0.14, grid_y + grid_h - 0.5, 0.34, 0.34, str(i + 1), fill=GOLD,
             color=DEEP, size=13)
        if i < n - 1:
            ax = cx + cw + 0.06
            arrow = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(ax),
                Inches(grid_y + grid_h / 2 - 0.16), Inches(gap_arrow - 0.12), Inches(0.32))
            arrow.fill.solid(); arrow.fill.fore_color.rgb = TEAL
            arrow.line.fill.background()
            disable_shadow(arrow)

    ocean_box(s, 0.55, 5.55, 12.23, 1.05, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, 5.55, 11.6, 1.05,
             text="Когда нужен: база большая и меняется",
             size=17, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s03"))


def build_s04(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Агент циклом", size=28)
    text_box(s, 0.55, 1.05, 9.5, 0.5,
             text="Нужен, когда несколько шагов и действия во внешних системах",
             size=15, italic=True, color=MID, line_spacing=1.2)
    chip(s, 11.15, 1.0, 1.65, 0.42, "Лекция 3 →", fill=TEAL, size=11.5)

    # Circular 4-step layout using 4 corner cards + center loop icon
    cx0, cy0, r_w = 6.67, 3.75, 4.7
    positions = [
        (cx0 - r_w / 2 - 1.55, 2.0, "git-fork", "Строит план"),
        (cx0 + r_w / 2 - 1.55, 2.0, "wrench", "Вызывает внешний\nинструмент (API,\nпоиск, код)"),
        (cx0 + r_w / 2 - 1.55, 3.9, "circle-check", "Проверяет\nрезультат вызова"),
        (cx0 - r_w / 2 - 1.55, 3.9, "route", "Решает, что\nделать дальше"),
    ]
    card_w, card_h = 3.1, 1.6
    for i, (cx, cy, ic, lbl) in enumerate(positions):
        ocean_box(s, cx, cy, card_w, card_h)
        icon(s, ic, "065A82", 96, cx + 0.16, cy + 0.16, 0.44)
        chip(s, cx + card_w - 0.48, cy + 0.14, 0.32, 0.32, str(i + 1), fill=GOLD,
             color=DEEP, size=11.5)
        lines = lbl.split("\n")
        paras = [{"text": ln, "size": 12, "bold": True, "color": DEEP,
                  "line_spacing": 1.1} for ln in lines]
        multipara_box(s, cx + 0.16, cy + 0.68, card_w - 0.32, card_h - 0.78, paras)

    # Center loop badge
    loop_sz = 1.0
    lcx = cx0 - loop_sz / 2
    lcy = 2.0 + card_h + 0.05
    filled_rect(s, lcx, lcy, loop_sz, loop_sz, TEAL, radius=True, radius_adj=0.5)
    icon(s, "repeat", "FFFFFF", 48, lcx + 0.2, lcy + 0.2, 0.6)
    text_box(s, cx0 - 1.1, lcy + loop_sz + 0.04, 2.2, 0.3, text="цикл повторяется",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.CENTER)

    ocean_box(s, 0.55, 5.95, 12.23, 1.05, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, 5.95, 11.6, 1.05,
             text="Когда нужен: несколько шагов и действия во внешних системах",
             size=16.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s04"))


def build_s05(p):
    build_divider(p, "s05", "1", "ИИ или обычный код?",
                  "Полный кейс · блиц-кейс · два случая из жизни", 0)


def build_s06(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Документы поставщиков", size=28)
    quote_block(s, 0.55, 1.15, 12.23, 1.55,
                "«Вот два примера входящих документов от двух наших поставщиков за "
                "последний месяц. Форматы почти идентичные. Напишите нам автоматическое "
                "извлечение данных из таких документов».", size=15)

    grid_y = 2.75
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 2.55
    docs = [("A", ["Дата", "№ накладной", "Позиция", "Сумма"]),
            ("Б", ["Дата", "№ накладной", "Позиция", "Сумма"])]
    for i, (label, cols) in enumerate(docs):
        cx = 0.55 + i * (cw + gap)
        ocean_box(s, cx, grid_y, cw, ch)
        text_box(s, cx + 0.22, grid_y + 0.16, cw - 0.44, 0.35,
                 text=f"Документ поставщика {label}", size=13.5, bold=True, color=MID)
        table_y = grid_y + 0.65
        row_h = 0.42
        table_w = cw - 0.44
        col_w = table_w / len(cols)
        for ci, colname in enumerate(cols):
            hx = cx + 0.22 + ci * col_w
            filled_rect(s, hx, table_y, col_w - 0.04, row_h, MID, radius=False)
            text_box(s, hx, table_y, col_w - 0.04, row_h, text=colname, size=10.5,
                     bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        for r in range(2):
            ry = table_y + row_h * (r + 1) + 0.03 * r
            for ci in range(len(cols)):
                hx = cx + 0.22 + ci * col_w
                filled_rect(s, hx, ry, col_w - 0.04, row_h, SURFACE, stroke=SOFT_GREY, stroke_pt=0.8)
                text_box(s, hx, ry, col_w - 0.04, row_h, text="24.03.2026" if ci == 0 else "—",
                         size=10, color=SLATE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.55, 5.75, 12.23, 0.4, text="Одинаковые колонки, одинаковый формат дат",
             size=12.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    ocean_box(s, 0.55, 6.3, 12.23, 0.85, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, 6.3, 11.6, 0.85, text="Нужен ли здесь ИИ?", size=22, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s06"))


def build_s07(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Полный корпус — три года, все поставщики", size=25)
    quote_block(s, 0.55, 1.05, 12.23, 1.0,
                "«Запросили полный корпус: три года, все поставщики».", size=15)

    grid_y = 2.25
    gap = 0.22
    n = 4
    cw = (12.23 - gap * (n - 1)) / n
    ch = 2.15
    variants = [
        ("A", ["Дата", "№ накл.", "Сумма"]),
        ("Б", ["Date", "Invoice#", "Total"]),
        ("В", ["Период", "Заказ", "Итого, ₽"]),
        ("Г", ["№", "от", "итого"]),
    ]
    for i, (label, cols) in enumerate(variants):
        cx = 0.55 + i * (cw + gap)
        ocean_box(s, cx, grid_y, cw, ch, stroke=TEAL)
        text_box(s, cx + 0.14, grid_y + 0.12, cw - 0.28, 0.3,
                 text=f"Поставщик {label}", size=11.5, bold=True, color=MID)
        row_h = 0.36
        table_y = grid_y + 0.52
        col_w = (cw - 0.28) / len(cols)
        for ci, colname in enumerate(cols):
            hx = cx + 0.14 + ci * col_w
            filled_rect(s, hx, table_y, col_w - 0.03, row_h, TEAL)
            text_box(s, hx, table_y, col_w - 0.03, row_h, text=colname, size=8,
                     bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                     line_spacing=0.95)
        ry = table_y + row_h + 0.03
        for ci in range(len(cols)):
            hx = cx + 0.14 + ci * col_w
            filled_rect(s, hx, ry, col_w - 0.03, row_h, SURFACE, stroke=SOFT_GREY, stroke_pt=0.7)
    text_box(s, 0.55, grid_y + ch + 0.1, 12.23, 0.35, text="Форматы разъехались — разные колонки, разные форматы дат",
             size=12, italic=True, color=SLATE, align=PP_ALIGN.CENTER)

    q_y = grid_y + ch + 0.55
    ocean_box(s, 0.55, q_y, 12.23, 0.65, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, q_y, 11.6, 0.65, text="Кто передумал? Почему?", size=18, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    verdict_y = q_y + 0.8
    verdict_h = 7.15 - verdict_y
    ocean_box(s, 0.55, verdict_y, 12.23, verdict_h, fill=SURFACE, stroke=MID, stroke_pt=1.6)
    icon(s, "workflow", "065A82", 96, 0.8, verdict_y + (verdict_h - 0.5) / 2, 0.5)
    multipara_box(s, 1.5, verdict_y + 0.12, 10.9, verdict_h - 0.24, [
        {"text": "Гибрид: LLM-извлечение по вариативному входу + жёсткая валидация кодом на выходе",
         "size": 15.5, "bold": True, "color": DEEP, "line_spacing": 1.2},
        {"text": "Урок: два примера — не выборка", "size": 13, "italic": True, "color": GOLD,
         "bold": True, "space_after": 2},
    ], anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s07"))


def build_s08(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Персоналка в логах", size=28)
    quote_block(s, 0.55, 1.1, 12.23, 1.0,
                "«Нужно вычистить персональные данные из логов приложения перед "
                "передачей их внешнему подрядчику на анализ производительности».", size=14.5)
    ocean_box(s, 0.55, 2.35, 12.23, 0.65, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.3)
    text_box(s, 0.85, 2.35, 11.6, 0.65, text="Одна технология на всё, или нет?",
             size=18, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    grid_y = 3.25
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 2.65
    ocean_box(s, 0.55, grid_y, cw, ch, stroke=TEAL)
    icon(s, "hash", "028090", 96, 0.55 + 0.25, grid_y + 0.22, 0.55)
    text_box(s, 0.55 + 0.95, grid_y + 0.22, cw - 1.2, 0.55, text="Regex", size=17,
             bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.55 + 0.25, grid_y + 1.0, cw - 0.5, 1.5,
             text="Телефоны, email — чёткий формат, дёшево и надёжно",
             size=14.5, color=DEEP, line_spacing=1.3)

    rx = 0.55 + cw + gap
    ocean_box(s, rx, grid_y, cw, ch, stroke=MID)
    icon(s, "search", "065A82", 96, rx + 0.25, grid_y + 0.22, 0.55)
    text_box(s, rx + 0.95, grid_y + 0.22, cw - 1.2, 0.55, text="NER / LLM", size=17,
             bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, rx + 0.25, grid_y + 1.0, cw - 0.5, 1.5,
             text="Имена людей, косвенные упоминания в свободном тексте — нужен контекст",
             size=14.5, color=DEEP, line_spacing=1.3)

    footer_y = grid_y + ch + 0.25
    ocean_box(s, 0.55, footer_y, 12.23, 0.75, fill=SURFACE, stroke=LIGHT)
    text_box(s, 0.85, footer_y, 11.6, 0.75,
             text="Ответ — гибрид, и граница проходит внутри одной задачи",
             size=15.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s08"))


def build_s09(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Из жизни: провал и успех", size=28)
    text_box(s, 0.55, 1.05, 12.23, 0.5,
             text="Vendor-метрика точности ≠ метрика, измеренная независимо на своих данных",
             size=14.5, italic=True, color=MID)

    grid_y = 1.75
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 2.85
    negative_card(s, 0.55, grid_y, cw, ch, "Epic Sepsis Model", [
        {"text": "Заявленный AUC 0.76–0.83 vs реальный 0.63 (Michigan Medicine, 38 455 госпитализаций)",
         "size": 13, "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "Пропущено 67% реальных случаев сепсиса", "size": 13, "bold": True, "color": DEEP,
         "line_spacing": 1.25, "space_after": 6},
        {"text": "Алерты — на 18% всех госпитализированных пациентов", "size": 13, "color": DEEP,
         "line_spacing": 1.25},
    ], icon_name="x-circle")

    rx = 0.55 + cw + gap
    positive_card(s, rx, grid_y, cw, ch, "Ramp, merchant classification", [
        {"text": "Вручную: покрытие 3% заявок (2023) → 1,5% (2024)", "size": 13, "color": DEEP,
         "line_spacing": 1.25, "space_after": 6},
        {"text": "После LLM-агента: обработка < 10 сек", "size": 13, "bold": True, "color": DEEP,
         "line_spacing": 1.25, "space_after": 6},
        {"text": "~99% изменений корректны · ~25% заявок обоснованно отклоняются", "size": 13,
         "color": DEEP, "line_spacing": 1.25},
    ], icon_name="circle-check")

    takeaway_y = grid_y + ch + 0.3
    ocean_box(s, 0.55, takeaway_y, 12.23, 1.15, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, takeaway_y, 11.6, 1.15,
             text="Ramp — замена ручной обработки с мизерным покрытием, не замена работавшего "
                  "regex-решения",
             size=17, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
    speaker_notes(s, load_notes("s09"))


def build_s10(p):
    build_divider(p, "s10", "2", "Встроить или делать своё?",
                  "Полный кейс без единственного ответа · блиц-кейс · случаи из жизни",
                  1)


def build_s11(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Помощник поддержки", size=28)
    quote_block(s, 0.55, 1.3, 12.23, 1.7,
                "«Сделайте нам ИИ-помощника для операторов техподдержки — подсказки "
                "ответов на тикеты, поиск похожих обращений в истории».", size=17)

    # Ocean box wraps the icon + supporting line to fill the middle mass
    mid_y = 3.3
    mid_h = 1.55
    ocean_box(s, 0.55, mid_y, 12.23, mid_h, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    icon(s, "monitor", "065A82", 96, 0.95, mid_y + (mid_h - 0.9) / 2, 0.9)
    text_box(s, 2.15, mid_y, 10.2, mid_h,
             text="Операторы весь рабочий день живут в интерфейсе helpdesk-системы",
             size=16, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)

    q_y = mid_y + mid_h + 0.3
    ocean_box(s, 0.55, q_y, 12.23, 1.35, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.5)
    text_box(s, 0.85, q_y, 11.6, 1.35, text="Где должен жить этот помощник?", size=26,
             bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s11"))


def build_s12(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Закрытый вендор", size=28)
    quote_block(s, 0.55, 1.05, 12.23, 1.0,
                "«У вендора вашей helpdesk-системы нет открытого API и нет возможности "
                "кастомизации».", size=14)

    grid_y = 2.25
    gap = 0.28
    cw = (12.23 - gap * 2) / 3
    ch = 3.9
    options = [
        ("split", "Решение сбоку", "Расширение браузера или вторая панель",
         "Два места одновременно, риск: оператор не будет пользоваться"),
        ("repeat", "Смена вендора", "Helpdesk-система с открытым API",
         "Миграция данных, переобучение команды, риск простоя"),
        ("route", "Пересмотр задачи", "Асинхронный помощник, готовит черновики заранее",
         "Оператор открывает готовое там, где удобно, но нужен отдельный процесс"),
    ]
    for i, (ic, title, desc, cost) in enumerate(options):
        cx = 0.55 + i * (cw + gap)
        ocean_box(s, cx, grid_y, cw, ch)
        icon(s, ic, "065A82", 96, cx + (cw - 0.55) / 2, grid_y + 0.24, 0.55)
        text_box(s, cx + 0.16, grid_y + 0.95, cw - 0.32, 0.5, text=title, size=15,
                 bold=True, color=MID, align=PP_ALIGN.CENTER, line_spacing=1.1)
        text_box(s, cx + 0.16, grid_y + 1.5, cw - 0.32, 1.1, text=desc, size=12,
                 color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.25)
        filled_rect(s, cx + 0.14, grid_y + ch - 1.35, cw - 0.28, 1.15, GOLD_TINT,
                    stroke=GOLD, stroke_pt=1.1, radius=True, radius_adj=0.1)
        text_box(s, cx + 0.24, grid_y + ch - 1.28, cw - 0.48, 1.0, text=f"Цена: {cost}",
                 size=10.5, italic=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.2,
                 anchor=MSO_ANCHOR.MIDDLE)

    footer_y = grid_y + ch + 0.2
    ocean_box(s, 0.55, footer_y, 12.23, 0.6, fill=SURFACE, stroke=LIGHT)
    text_box(s, 0.85, footer_y, 11.6, 0.6, text="Единственно верного ответа нет",
             size=15, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s12"))


def build_s13(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Описания товаров", size=28)
    quote_block(s, 0.55, 1.2, 12.23, 1.2,
                "«Маркетинг просит отдельный ИИ-сервис для генерации описаний товаров».",
                size=16)

    row_y = 2.85
    row_h = 1.9
    ocean_box(s, 0.55, row_y, 12.23, row_h, fill=SURFACE, stroke=TEAL, stroke_pt=1.6)
    icon(s, "store", "065A82", 96, 0.9, row_y + (row_h - 0.85) / 2, 0.85)
    icon(s, "arrow-right", "F0AB00", 64, 2.15, row_y + (row_h - 0.5) / 2, 0.5)
    icon(s, "zap", "F0AB00", 96, 3.05, row_y + (row_h - 0.85) / 2, 0.85)
    multipara_box(s, 4.2, row_y, 7.6, row_h, [
        {"text": "Кнопка «сгенерировать описание»", "size": 20, "bold": True, "color": DEEP,
         "line_spacing": 1.2, "space_after": 6},
        {"text": "в существующей админке каталога, которой маркетинг и так пользуется каждый день",
         "size": 15, "color": DEEP, "line_spacing": 1.3},
    ], anchor=MSO_ANCHOR.MIDDLE)

    fn_y = row_y + row_h + 0.4
    ocean_box(s, 0.55, fn_y, 12.23, 1.15, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, fn_y, 11.6, 1.15,
             text="Отдельный продукт — не отдельный продукт: второй логин и вкладка убивают использование",
             size=16, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
    speaker_notes(s, load_notes("s13"))


def build_s14(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Из жизни: Kite vs GitHub Copilot", size=26)

    grid_y = 1.5
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 2.65
    negative_card(s, 0.55, grid_y, cw, ch, "Kite (standalone)", [
        {"text": "~500 000 бесплатных пользователей на пике", "size": 13, "color": DEEP,
         "line_spacing": 1.25, "space_after": 6},
        {"text": "Закрылся в ноябре 2022 года", "size": 13, "bold": True, "color": DEEP,
         "line_spacing": 1.25, "space_after": 6},
        {"text": "«Разработчики не платят за инструменты»", "size": 13, "italic": True,
         "color": DEEP, "line_spacing": 1.25},
    ], icon_name="x-circle")

    rx = 0.55 + cw + gap
    positive_card(s, rx, grid_y, cw, ch, "GitHub Copilot (встроен)", [
        {"text": "~20 млн пользователей к июлю 2025 (из 100+ млн на GitHub)", "size": 13,
         "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "~4,7 млн платных подписчиков к январю 2026", "size": 13, "bold": True,
         "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "~90% компаний Fortune 100", "size": 13, "color": DEEP, "line_spacing": 1.25},
    ], icon_name="circle-check")

    takeaway_y = grid_y + ch + 0.28
    ocean_box(s, 0.55, takeaway_y, 12.23, 0.95, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, takeaway_y, 11.6, 0.95,
             text="Встроенность в уже существующий рабочий поток победила отдельный продукт "
                  "при технологии сравнимого класса",
             size=16, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)

    fn_y = takeaway_y + 0.95 + 0.22
    ocean_box(s, 0.55, fn_y, 12.23, 0.8, fill=SURFACE, stroke=LIGHT)
    text_box(s, 0.85, fn_y, 11.6, 0.8,
             text="Humane AI Pin — привлечено ~$241 млн, продан за $116 млн · Rabbit R1 — "
                  "~100 000 устройств, активно пользуются ~5%",
             size=12, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)
    speaker_notes(s, load_notes("s14"))


def build_s15(p):
    build_divider(p, "s15", "3", "Разовый вызов, RAG или агент?",
                  "Кейс-лестница из трёх ступеней · блиц-кейс · случаи из жизни", 2)


def build_s16(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Протоколы встреч", size=28)
    ocean_box(s, 0.55, 1.25, 12.23, 2.1, fill=SURFACE, stroke=TEAL, stroke_pt=1.6)
    icon(s, "file-text", "065A82", 96, 0.9, 1.6, 0.8)
    icon(s, "arrow-right", "F0AB00", 64, 2.05, 1.85, 0.5)
    icon(s, "list-checks", "065A82", 96, 2.85, 1.6, 0.8)
    multipara_box(s, 4.0, 1.55, 8.5, 1.7, [
        {"text": "Транскрипт встречи → структурированный протокол", "size": 18, "bold": True,
         "color": DEEP, "line_spacing": 1.2, "space_after": 6},
        {"text": "Какие решения приняты, какие поручения даны, какие сроки", "size": 13.5,
         "color": SLATE, "line_spacing": 1.25, "space_after": 6},
        {"text": "У вас есть полный транскрипт одной встречи целиком", "size": 13.5,
         "bold": True, "italic": True, "color": MID, "line_spacing": 1.25},
    ])
    v_y = 3.65
    ocean_box(s, 0.55, v_y, 12.23, 1.0, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, v_y, 11.6, 1.0,
             text="Один разовый вызов модели — RAG и агент были бы избыточным усложнением",
             size=17, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    # ladder-position indicator (step 1 of 3), reused/extended by s17/s18
    lad_y = 4.95
    ladder_row(s, lad_y, 1)
    speaker_notes(s, load_notes("s16"))


def ladder_row(slide, y, active_step, ch=1.55):
    """3-step architecture ladder used across s16/s17/s18 (progressive reveal)."""
    labels = ["Разовый вызов", "RAG", "Агент"]
    n = 3
    gap = 0.3
    cw = (12.23 - gap * (n - 1)) / n
    for i, lbl in enumerate(labels):
        cx = 0.55 + i * (cw + gap)
        is_done = (i < active_step)
        is_now = (i == active_step - 1)
        fill = GOLD if is_now else (SURFACE if not is_done else SOFT_GREY)
        stroke = GOLD if is_now else LIGHT
        filled_rect(slide, cx, y, cw, ch, fill, stroke=stroke, stroke_pt=1.5,
                    radius=True, radius_adj=0.12)
        text_box(slide, cx, y + 0.18, cw, 0.5, text=lbl, size=15.5, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER)
        if i < n - 1:
            ax = cx + cw + 0.04
            arrow = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(ax),
                Inches(y + ch / 2 - 0.11), Inches(gap - 0.08), Inches(0.22))
            arrow.fill.solid(); arrow.fill.fore_color.rgb = TEAL
            arrow.line.fill.background()
            disable_shadow(arrow)


def build_s17(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "База протоколов растёт", size=26, y=0.35, h=0.6)
    quote_block(s, 0.55, 0.95, 12.23, 0.85,
                "«Теперь хотим спрашивать: что мы решали по проекту X за последние полгода?»",
                size=13.5)

    # growing stack illustration
    stack_y = 2.0
    stack_h = 1.25
    n_cards = 5
    base_w = 0.48
    gap = 0.24
    for i in range(n_cards):
        cw = base_w + i * 0.14
        cx = 0.7 + i * (base_w + gap)
        ch = 0.4 + i * 0.17
        filled_rect(s, cx, stack_y + stack_h - ch, cw, ch,
                    LIGHT if i < n_cards - 1 else GOLD, radius=True, radius_adj=0.15)
    text_box(s, 0.7, stack_y + stack_h + 0.06, 4.6, 0.3, text="растёт со временем →",
             size=10.5, italic=True, color=SLATE)

    icon(s, "database", "065A82", 96, 6.3, stack_y + 0.2, 0.85)
    multipara_box(s, 7.4, stack_y + 0.05, 5.3, 1.15, [
        {"text": "Весь объём уже не помещается", "size": 14.5, "bold": True, "color": DEEP,
         "line_spacing": 1.15, "space_after": 3},
        {"text": "в один запрос к модели", "size": 14.5, "bold": True, "color": DEEP,
         "line_spacing": 1.15},
    ])

    q_y = 3.6
    ocean_box(s, 0.55, q_y, 12.23, 0.55, fill=SURFACE, stroke=LIGHT)
    text_box(s, 0.85, q_y, 11.6, 0.55, text="Кто передумал? Почему?", size=15.5, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    v_y = q_y + 0.68
    ocean_box(s, 0.55, v_y, 12.23, 0.65, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, v_y, 11.6, 0.65, text="Теперь обоснован RAG",
             size=16, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    ladder_row(s, v_y + 0.82, 2, ch=1.05)
    speaker_notes(s, load_notes("s17"))


def build_s18(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Поручения — сами в таск-трекер", size=27)
    quote_block(s, 0.55, 1.05, 12.23, 0.9,
                "«И пусть поручения из протокола сами автоматически раскладываются "
                "по задачам в таск-трекере».", size=13.5)

    ill_y = 2.15
    ocean_box(s, 0.55, ill_y, 12.23, 1.35, fill=SURFACE, stroke=TEAL, stroke_pt=1.6)
    icon(s, "file-text", "065A82", 96, 0.9, ill_y + 0.35, 0.65)
    icon(s, "arrow-right", "F0AB00", 64, 1.95, ill_y + 0.5, 0.45)
    icon(s, "list-checks", "065A82", 96, 2.75, ill_y + 0.35, 0.65)
    text_box(s, 3.8, ill_y + 0.25, 8.7, 0.9,
             text="создать задачу → назначить исполнителя → проверить срок",
             size=15, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)

    v_y = 3.75
    ocean_box(s, 0.55, v_y, 12.23, 1.35, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.5)
    multipara_box(s, 0.85, v_y + 0.16, 11.6, 1.05, [
        {"text": "Архитектурный выбор двигают конкретные новые требования", "size": 17,
         "bold": True, "color": DEEP, "line_spacing": 1.2, "space_after": 4},
        {"text": "Начинайте с простейшего варианта и усложняйте только тогда, когда простой "
                 "закрыть требование не может", "size": 13, "italic": True, "color": DEEP,
         "line_spacing": 1.2},
    ])

    ladder_row(s, 5.35, 3)
    speaker_notes(s, load_notes("s18"))


def build_s19(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Еженедельный дайджест", size=28)
    quote_block(s, 0.55, 1.1, 12.23, 1.0,
                "«Нужен еженедельный дайджест по рабочим чатам и почте команды — "
                "что обсуждали, что решили».", size=14.5)

    grid_y = 2.35
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 1.95
    positive_card(s, 0.55, grid_y, cw, ch, "Агент — нужен", [
        {"text": "Обход нескольких источников по расписанию", "size": 13.5, "color": DEEP,
         "line_spacing": 1.25, "space_after": 6},
        {"text": "Многошаговая задача с обращением к внешним системам", "size": 13.5,
         "color": DEEP, "line_spacing": 1.25},
    ], icon_name="circle-check")

    negative_card(s, 0.55 + cw + gap, grid_y, cw, ch, "RAG — не нужен", [
        {"text": "Источники обходятся напрямую по расписанию, не по произвольному запросу",
         "size": 13.5, "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "Суммаризация — один вызов модели после сбора", "size": 13.5, "color": DEEP,
         "line_spacing": 1.25},
    ], icon_name="x-circle")

    footer_y = grid_y + ch + 0.35
    ocean_box(s, 0.55, footer_y, 12.23, 1.15, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, footer_y, 11.6, 1.15, text="RAG ≠ «у нас много источников»",
             size=20, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s19"))


def build_s20(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Из жизни: фреймворк и класс задач для агента", size=23)

    grid_y = 1.5
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 2.75
    negative_card(s, 0.55, grid_y, cw, ch, "Octomind: «Why we no longer use LangChain»", [
        {"text": "12+ месяцев LangChain в проде → отказ (17.06.2024)", "size": 12.5,
         "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "Дебаг фреймворка дороже разработки фич", "size": 12.5, "bold": True,
         "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "Негибкие абстракции → замена на прямые модульные вызовы LLM API",
         "size": 12.5, "color": DEEP, "line_spacing": 1.25},
    ], icon_name="x-circle")

    rx = 0.55 + cw + gap
    positive_card(s, rx, grid_y, cw, ch, "Где агент необходим", [
        {"text": "Deep Research — поиск и синтез по многим источникам с уточнением запроса",
         "size": 12.5, "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "Coding-агенты — правка кода → запуск тестов → итерация по результату",
         "size": 12.5, "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "В обоих случаях одного вызова физически недостаточно", "size": 12.5,
         "bold": True, "color": DEEP, "line_spacing": 1.25},
    ], icon_name="circle-check")

    takeaway_y = grid_y + ch + 0.3
    ocean_box(s, 0.55, takeaway_y, 12.23, 1.15, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, takeaway_y, 11.6, 1.15,
             text="Прямые вызовы API иногда дают больше контроля, чем абстракция, которая "
                  "должна была его упростить",
             size=17, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
    speaker_notes(s, load_notes("s20"))


def build_s21(p):
    build_divider(p, "s21", "4", "Внешний API или локальный инференс?",
                  "Кейс-трёхходовка · случаи из жизни", 3)


def build_s22(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Саммаризация звонков продаж", size=27)
    ocean_box(s, 0.55, 1.35, 12.23, 2.4, fill=SURFACE, stroke=TEAL, stroke_pt=1.6)
    icon(s, "phone", "065A82", 96, 0.9, 1.75, 0.85)
    icon(s, "arrow-right", "F0AB00", 64, 2.15, 2.0, 0.5)
    icon(s, "file-text", "065A82", 96, 2.95, 1.75, 0.85)
    multipara_box(s, 4.1, 1.75, 8.3, 1.7, [
        {"text": "Записи звонков менеджеров по продажам →", "size": 17, "bold": True,
         "color": DEEP, "line_spacing": 1.2, "space_after": 6},
        {"text": "карточка звонка: выявленная потребность клиента, возражения, договорённости",
         "size": 14, "color": SLATE, "line_spacing": 1.3},
    ])

    v_y = 4.15
    ocean_box(s, 0.55, v_y, 12.23, 1.15, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.5)
    text_box(s, 0.85, v_y, 11.6, 1.15, text="Какая архитектура? Где считать?",
             size=24, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    # 3-step calls ladder position indicator (step 1 of 3)
    calls_ladder_row(s, 5.75, 1)
    speaker_notes(s, load_notes("s22"))


def calls_ladder_row(slide, y, active_step):
    """3-step ход indicator for the calls trilogy (s22/s23/s24)."""
    labels = ["Облачный frontier?", "Персональные данные", "Шаблон полей → локальная модель"]
    n = 3
    gap = 0.3
    cw = (12.23 - gap * (n - 1)) / n
    ch = 1.0
    for i, lbl in enumerate(labels):
        cx = 0.55 + i * (cw + gap)
        is_now = (i == active_step - 1)
        is_done = (i < active_step - 1)
        fill = GOLD if is_now else (SOFT_GREY if is_done else SURFACE)
        stroke = GOLD if is_now else LIGHT
        filled_rect(slide, cx, y, cw, ch, fill, stroke=stroke, stroke_pt=1.5,
                    radius=True, radius_adj=0.15)
        text_box(slide, cx + 0.12, y, cw - 0.24, ch, text=f"Ход {i+1}: {lbl}", size=12.5,
                 bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.1)
        if i < n - 1:
            ax = cx + cw + 0.04
            arrow = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(ax),
                Inches(y + ch / 2 - 0.11), Inches(gap - 0.08), Inches(0.22))
            arrow.fill.solid(); arrow.fill.fore_color.rgb = TEAL
            arrow.line.fill.background()
            disable_shadow(arrow)


def build_s23(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Персональные данные в звонках", size=26)
    quote_block(s, 0.55, 1.15, 12.23, 1.5,
                "«Мы прослушали несколько реальных звонков внимательно. Клиенты в "
                "разговоре иногда диктуют номера телефонов, адреса доставки, а в паре "
                "случаев — паспортные данные для оформления договора».", size=14)

    reg_y = 2.95
    ocean_box(s, 0.55, reg_y, 12.23, 2.15, fill=NEG_TINT, stroke=NEG_LINE, stroke_pt=1.5)
    icon(s, "shield-alert", "21295C", 64, 0.85, reg_y + 0.25, 0.5)
    text_box(s, 1.5, reg_y + 0.2, 10.9, 0.5,
             text="ФЗ № 420-ФЗ (с 30.05.2025)", size=17, bold=True, color=DEEP)
    multipara_box(s, 1.5, reg_y + 0.75, 10.9, 1.3, [
        {"text": "Повторная утечка персональных данных — оборотный штраф 1-3% годовой выручки",
         "size": 14, "bold": True, "color": DEEP, "line_spacing": 1.25, "space_after": 4},
        {"text": "(минимум 20 млн, максимум 500 млн ₽)", "size": 12.5, "color": SLATE,
         "line_spacing": 1.2, "space_after": 6},
        {"text": "Обязанность уведомить Роскомнадзор в течение 24 часов", "size": 13,
         "italic": True, "color": DEEP, "line_spacing": 1.2},
    ])

    q_y = reg_y + 2.4
    ocean_box(s, 0.55, q_y, 12.23, 0.6, fill=SURFACE, stroke=LIGHT)
    text_box(s, 0.85, q_y, 11.6, 0.6, text="Кто передумал? Почему?", size=16, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    calls_ladder_row(s, q_y + 0.75, 2)
    speaker_notes(s, load_notes("s23"))


def build_s24(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Задача сузилась до шаблона", size=28)
    quote_block(s, 0.55, 1.1, 12.23, 1.15,
                "«Давайте посмотрим на задачу трезво: на выходе нам нужна не свободная "
                "беседа, а структурированная выжимка по фиксированному шаблону из "
                "нескольких полей».", size=13.5)

    v_y = 2.5
    ocean_box(s, 0.55, v_y, 12.23, 1.3, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.5)
    icon(s, "cpu", "21295C", 64, 0.85, v_y + 0.35, 0.6)
    text_box(s, 1.65, v_y + 0.14, 10.8, 1.0,
             text="Небольшая локальная модель (7-8 млрд параметров) справляется — "
                  "данные не покидают периметр компании",
             size=15.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)

    grid_y = 4.05
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 1.85
    ocean_box(s, 0.55, grid_y, cw, ch, stroke=TEAL)
    text_box(s, 0.55 + 0.22, grid_y + 0.18, cw - 0.44, ch - 0.36,
             text="(а) «сложно для человека» ≠ «сложно для модели»",
             size=14.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
    ocean_box(s, 0.55 + cw + gap, grid_y, cw, ch, stroke=TEAL)
    text_box(s, 0.55 + cw + gap + 0.22, grid_y + 0.18, cw - 0.44, ch - 0.36,
             text="(б) чувствительность данных выясняется вопросами, а не предполагается",
             size=14.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)

    calls_ladder_row(s, grid_y + ch + 0.25, 3)
    speaker_notes(s, load_notes("s24"))


def build_s25(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Из жизни: утечка и малые модели в проде", size=24)

    grid_y = 1.55
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 2.85
    negative_card(s, 0.55, grid_y, cw, ch, "Samsung, 2023", [
        {"text": "Разрешили ChatGPT 11.03.2023", "size": 12.5, "color": DEEP,
         "line_spacing": 1.25, "space_after": 6},
        {"text": "К 30.03 (~19 дней) — 3 утечки: 2× код производства, 1× транскрипт совещания",
         "size": 12.5, "bold": True, "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "Полный запрет генеративного ИИ на устройствах (май 2023) + своя внутренняя система",
         "size": 12.5, "color": DEEP, "line_spacing": 1.25},
    ], icon_name="x-circle")

    rx = 0.55 + cw + gap
    positive_card(s, rx, grid_y, cw, ch, "Малые модели в проде", [
        {"text": "JetBrains full-line completion — локальная модель ~100 МБ, в проде с апреля 2024",
         "size": 12.5, "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "Apple on-device — ~3 млрд параметров (WWDC 2024)", "size": 12.5,
         "bold": True, "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "Frontier (GPT/Claude/Gemini) — сотни миллиардов параметров, только облако",
         "size": 12.5, "italic": True, "color": SLATE, "line_spacing": 1.25},
    ], icon_name="circle-check")

    takeaway_y = grid_y + ch + 0.3
    ocean_box(s, 0.55, takeaway_y, 12.23, 1.15, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, takeaway_y, 11.6, 1.15,
             text="Frontier-модели — сотни миллиардов параметров, доступны только через облако. "
                  "Малые модели уже работают локально в проде",
             size=16, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
    speaker_notes(s, load_notes("s25"))


def build_s26(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Разберите вашу задачу", size=28)

    # Left: mini funnel, no highlight (all equal)
    mini_funnel(s, 0.55, 1.4, 4.6, 4.6, None)

    # Right: 4 numbered steps
    steps = [
        "Какой выбор воронки здесь стоит острее всего?",
        "Каких вводных не хватает, чтобы сделать этот выбор обоснованно?",
        "Что было на самом деле — изменило ли это выбор?",
        "Какие риски у выбранного решения (лексика Лекции 1)?",
    ]
    sx = 5.6
    sw = 7.15
    sy = 1.4
    sh = 1.0
    gap = 0.14
    for i, text in enumerate(steps):
        ocean_box(s, sx, sy, sw, sh)
        chip(s, sx + 0.16, sy + (sh - 0.42) / 2, 0.42, 0.42, str(i + 1), fill=GOLD,
             color=DEEP, size=15)
        text_box(s, sx + 0.75, sy, sw - 0.95, sh, text=text, size=13.5, bold=True,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)
        sy += sh + gap

    inv_y = sy + 0.1
    ocean_box(s, sx, inv_y, sw, 0.75, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, sx + 0.2, inv_y, sw - 0.4, 0.75,
             text="Кто может поделиться реальной задачей со своей работы?",
             size=13.5, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.2)
    speaker_notes(s, load_notes("s26"))


def build_s27(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Памятка «Воронка решений + красные флаги»", size=24)

    gap = 0.3
    lw = 5.6
    rw = 12.23 - lw - gap
    ly = 1.35
    lh = 5.5

    ocean_box(s, 0.55, ly, lw, lh, stroke=MID, stroke_pt=1.6)
    text_box(s, 0.55 + 0.22, ly + 0.16, lw - 0.44, 0.4,
             text="Четыре вопроса воронки", size=15.5, bold=True, color=MID)
    qs = [
        "Нужен ли здесь ИИ вообще, или задачу лучше решает обычный код?",
        "Встраиваем в существующее приложение или делаем своё?",
        "Если своё — разовый вызов модели, RAG или агент?",
        "Внешний API или локальный инференс?",
    ]
    qy = ly + 0.7
    qh = (lh - 0.85) / 4
    for i, q in enumerate(qs):
        chip(s, 0.55 + 0.22, qy + 0.06, 0.36, 0.36, str(i + 1), fill=MID, size=13)
        text_box(s, 0.55 + 0.7, qy, lw - 0.9, qh, text=q, size=12.5, color=DEEP,
                 line_spacing=1.2, anchor=MSO_ANCHOR.MIDDLE)
        qy += qh

    rx = 0.55 + lw + gap
    ocean_box(s, rx, ly, rw, lh, fill=SURFACE, stroke=GOLD, stroke_pt=1.6)
    text_box(s, rx + 0.22, ly + 0.16, rw - 0.44, 0.4,
             text="Красный флаг на каждый вопрос", size=15.5, bold=True, color=GOLD)
    flags = [
        "Выбор по 2-3 показанным примерам без запроса на весь объём данных",
        "Vendor-KPI без знаменателя — цифра эффекта без базы расчёта",
        "Отдельный продукт там, где нужна кнопка в существующем интерфейсе",
        "RAG или агент выбраны потому что модно, а не по новому требованию",
        "Чувствительность данных не проверена до архитектурного выбора",
        "«Сложно для человека» принято за «сложно для модели» без проверки",
    ]
    fy = ly + 0.68
    fh = (lh - 0.83) / 6
    for i, flag in enumerate(flags):
        icon(s, "alert-triangle", "F0AB00", 64, rx + 0.2, fy + (fh - 0.28) / 2, 0.28)
        text_box(s, rx + 0.58, fy, rw - 0.78, fh, text=flag, size=10.8, color=DEEP,
                 line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)
        fy += fh
    speaker_notes(s, load_notes("s27"))


def build_s28(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Домашнее чтение (необязательное)", size=27)

    grid_y = 1.5
    gap = 0.28
    cw = (12.23 - gap * 2) / 3
    ch = 5.15
    cards = [
        ("handshake", "Сага Klarna, 2023-2025",
         "AI-ассистент поддержки: от впечатляющего старта до признания «мы зашли слишком "
         "далеко» и возврата к найму людей."),
        ("building-2", "NYC MyCity chatbot, 2024",
         "Городской чат-бот для малого бизнеса, дававший юридически некорректные советы. "
         "Расследование The Markup."),
        ("banknote", "Бонус, для настроения",
         "Автосалон подключил чат-бот на стороннем API без ограждений — и чат-бот "
         "«продал» внедорожник за один доллар."),
    ]
    for i, (ic, title, desc) in enumerate(cards):
        cx = 0.55 + i * (cw + gap)
        is_recommended = (i == 0)
        if is_recommended:
            ocean_box(s, cx, grid_y, cw, ch, stroke=GOLD, stroke_pt=2.0)
            chip(s, cx + cw - 1.35, grid_y + 0.2, 1.15, 0.34, "ГЛАВНОЕ", fill=GOLD,
                 color=DEEP, size=10.5)
        else:
            ocean_box(s, cx, grid_y, cw, ch)
        icon(s, ic, "065A82", 96, cx + (cw - 0.6) / 2, grid_y + 0.3, 0.6)
        text_box(s, cx + 0.2, grid_y + 1.15, cw - 0.4, 0.9, text=title, size=15, bold=True,
                 color=MID, align=PP_ALIGN.CENTER, line_spacing=1.2)
        text_box(s, cx + 0.2, grid_y + 2.15, cw - 0.4, ch - 2.35, text=desc, size=12.5,
                 color=DEEP, line_spacing=1.32)
    footer_note(s, "Ссылки — в брифе семинара. Klarna — редкий случай, когда одна компания "
                   "прошла все четыре выбора воронки на одном продукте", y=6.9)
    speaker_notes(s, load_notes("s28"))


def build_s28a(p):
    """Reserve slide — no visible 'reserve' marker (per task brief)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Klarna, 2023-2025: одна история — четыре развилки", size=22)

    rows = [
        ("1", "ИИ или нет", "Типовые тикеты — формализуемы, хороший кандидат; но "
         "оптимизация по стоимости уронила качество"),
        ("2", "Встроить или своё", "Ассистент в существующем канале поддержки, внешний "
         "API (OpenAI) — не отдельный продукт"),
        ("3", "Паттерн", "Чат-ассистент с эскалацией к человеку, не автономный агент"),
        ("4", "Инференс", "Внешний облачный API с клиентскими данными поддержки"),
    ]
    ry = 1.3
    rh = 0.92
    gap = 0.1
    for num, label, desc in rows:
        ocean_box(s, 0.55, ry, 12.23, rh, stroke=TEAL)
        chip(s, 0.75, ry + (rh - 0.4) / 2, 0.4, 0.4, num, fill=MID, size=14)
        text_box(s, 1.3, ry + 0.1, 2.4, rh - 0.2, text=label, size=13.5, bold=True,
                 color=MID, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
        text_box(s, 3.85, ry + 0.1, 8.75, rh - 0.2, text=desc, size=12, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)
        ry += rh + gap

    facts_y = ry + 0.05
    ocean_box(s, 0.55, facts_y, 12.23, 0.85, fill=SURFACE, stroke=LIGHT)
    text_box(s, 0.8, facts_y, 11.7, 0.85,
             text="Запуск февраль 2024 · 30 дней: 2,3 млн чатов, 67% обращений автоматизировано · "
                  "заявлено «700 агентов»/$40М (2024) → «853 агента»/$60М (Q3 2025) — знаменатель не раскрыт",
             size=11, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)

    quote_y = facts_y + 1.0
    ocean_box(s, 0.55, quote_y, 12.23, 0.85, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, quote_y, 11.6, 0.85,
             text="«We went too far» — CEO Себастьян Семятковски, Bloomberg, май 2025",
             size=15, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s28a"))


def build_s28b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Дедупликация новостей", size=28)
    quote_block(s, 0.55, 1.1, 12.23, 1.0,
                "«Поток новостей из многих источников — нужно склеивать сообщения об "
                "одном и том же событии в одну карточку».", size=14.5)

    grid_y = 2.35
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 1.95
    positive_card(s, 0.55, grid_y, cw, ch, "Fuzzy-matching / shingling — ~90%", [
        {"text": "Сравнение текстов по перекрывающимся фрагментам без обращения к модели",
         "size": 13.5, "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "Дёшево и предсказуемо", "size": 13.5, "bold": True, "color": DEEP,
         "line_spacing": 1.25},
    ], icon_name="filter")

    negative_card(s, 0.55 + cw + gap, grid_y, cw, ch, "LLM — только остаток", [
        {"text": "Два сообщения об одном событии написаны разными словами почти без общих "
         "фрагментов", "size": 13.5, "color": DEEP, "line_spacing": 1.25, "space_after": 6},
        {"text": "Перефраз без лексического пересечения", "size": 13.5, "italic": True,
         "color": DEEP, "line_spacing": 1.25},
    ], icon_name="sparkles")

    footer_y = grid_y + ch + 0.35
    ocean_box(s, 0.55, footer_y, 12.23, 1.15, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.85, footer_y, 11.6, 1.15,
             text="Сначала дешёвый детерминированный фильтр — ИИ на то, что он не взял",
             size=18, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s28b"))


def build_s29(p):
    s = blank(p)
    set_slide_bg(s, DEEP)
    img_path = SHOTS / "s-closing-gpu-real.jpg"
    if img_path.exists():
        add_image(s, img_path, 0, 0, w=SLIDE_W_IN, h=SLIDE_H_IN)
    # darken bottom third for text legibility
    overlay = filled_rect(s, 0, 4.9, SLIDE_W_IN, 2.6, DEEP)
    overlay.fill.fore_color.rgb = DEEP
    try:
        alpha = etree.SubElement(overlay.fill.fore_color._xFill.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr"),
            "{http://schemas.openxmlformats.org/drawingml/2006/main}alpha")
        alpha.set("val", "82000")
    except Exception:
        pass
    multipara_box(s, 0.6, 5.15, 11.6, 1.9, [
        {"text": "Сегодня вы решали, что строить.", "size": 26, "bold": True, "color": WHITE,
         "line_spacing": 1.2, "space_after": 4},
        {"text": "Лекция 2 — как модель устроена внутри", "size": 26, "bold": True, "color": GOLD,
         "line_spacing": 1.2},
    ])
    text_box(s, 0.6, 6.95, 11.6, 0.35,
             text="Wikimedia Commons · CC BY 2.0", size=10.5, italic=True,
             color=RGBColor(0xC8, 0xD2, 0xDF))
    speaker_notes(s, load_notes("s29"))


# ============================================================
# Orchestrate
# ============================================================

BUILDERS = [
    ("s01", build_s01), ("s02", build_s02), ("s03", build_s03), ("s04", build_s04),
    ("s05", build_s05), ("s06", build_s06), ("s07", build_s07), ("s08", build_s08),
    ("s09", build_s09), ("s10", build_s10), ("s11", build_s11), ("s12", build_s12),
    ("s13", build_s13), ("s14", build_s14), ("s15", build_s15), ("s16", build_s16),
    ("s17", build_s17), ("s18", build_s18), ("s19", build_s19), ("s20", build_s20),
    ("s21", build_s21), ("s22", build_s22), ("s23", build_s23), ("s24", build_s24),
    ("s25", build_s25), ("s26", build_s26), ("s27", build_s27), ("s28", build_s28),
    ("s28a", build_s28a), ("s28b", build_s28b), ("s29", build_s29),
]


def main():
    p = setup_pres()
    for sid, fn in BUILDERS:
        try:
            fn(p)
        except Exception as e:
            print(f"ERROR building {sid}: {e}")
            raise
    OUT.parent.mkdir(parents=True, exist_ok=True)
    p.save(str(OUT))
    print(f"Saved {OUT} — {len(BUILDERS)} slides")


if __name__ == "__main__":
    main()
