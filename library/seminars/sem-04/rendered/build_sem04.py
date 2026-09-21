"""
Build script for Семинар 4 — «Сборка кодинг-агента: лестница роста конфигурации».

Source-of-truth: deck.yaml + slides/*.md (56 slides). Direct python-pptx build
(not PowerPoint MCP), per notes/mcp-limitations.md [#54-1/#54-2/#54-3]: MCP has
no list_shapes, format_runs is buggy, no update_shape_position. Full-rebuild
via python-pptx sidesteps all three — same choice sem-01/02/03 made.

Canvas: 13.333" x 7.5" (16:9). Ocean Gradient v3 palette, LOCKED.

No live terminal on this seminar (owner decision, 2026-09-20) — every
"terminal snapshot" on these slides is a *verbatim* transcription of a real
captured command output (library/seminars/sem-04/assets/captures/*.txt), not
a live recording and not an invented mock. 11 of 18 planned captures could
not be taken (no interactive Claude Code session available to the producing
session) and are rendered as honest placeholders quoting
TODO-capture.md — never as a drawn imitation of a terminal (explicitly
forbidden by the prior session, and by [[no-mock-fallbacks]]).

s01 hero: no real-world photo exists for an abstract "empty repo -> 7 config
blocks" narrative (no company/product/incident to photograph) — hero is a
generated diagram built from the REAL 7-stage `git ls-tree` snapshots
(captures/21..27-tree-stage*.txt), not invented file names. See
iteration-log.md for the full 6-tier-acquisition reasoning on why this
counts as the generated-diagram media-rich tier, not a stylized mock.
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
                                             # literal "deny" quotes; palette
                                             # itself stays Ocean+Teal+Gold

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
# Generic helpers
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
    Uses tf.add_paragraph() per line (see notes/mcp-limitations.md
    [#sem01-render-1] — literal \\n inside one run does not reliably wrap)."""
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
    """Linear gradient rectangle (45deg, top-left -> bottom-right), used for
    section dividers + hero cover. `stops` = [(pos0to100000, RGBColor), ...]."""
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.line.fill.background()
    disable_shadow(shp)
    sppr = shp._element.spPr
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    # remove any existing fill
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
    lin.set("ang", "2700000")  # 45 degrees (60000ths of a degree)
    lin.set("scaled", "1")
    return shp


def lerp_color(c_lo, c_hi, t):
    """Linear-interpolate two (r, g, b) int tuples at t in [0, 1] -> RGBColor.
    Used by build_growth_staircase() to shade the ascending bars."""
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
    """Resolve an icon PNG: sem-04's own asset dir first, then fall back to
    the already-rendered sem-02/sem-03 Ocean-palette icon libraries (same
    Lucide set, same recolor convention) — avoids re-downloading icons that
    already exist for this palette."""
    local = ICONS / f"{name}-{color_hex}-{size_px}.png"
    if local.exists():
        return local
    for shared in (SEM03_ICONS, SEM02_ICONS):
        cand = shared / f"{name}-{color_hex}-{size_px}.png"
        if cand.exists():
            return cand
    return local  # will warn-and-skip in add_image


def icon(slide, name, color_hex, size_px, x, y, w_in):
    path = icon_path(name, color_hex, size_px)
    return add_image(slide, path, x, y, w=w_in, h=w_in)


def slide_title(slide, text, *, y=0.68, h=1.05, w=12.23, x=0.55, size=25,
                 color=DEEP, bold=True, line_spacing=1.14, align=PP_ALIGN.LEFT):
    text_box(slide, x=x, y=y, w=w, h=h, text=text,
             size=size, bold=bold, color=color, line_spacing=line_spacing,
             align=align)


def gold_callout(slide, x, y, w, h, text, *, size=14, bold=True, anchor=MSO_ANCHOR.MIDDLE):
    filled_rect(slide, x, y, w, h, GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.1)
    text_box(slide, x=x + 0.22, y=y + 0.08, w=w - 0.44, h=h - 0.16, text=text,
             size=size, bold=bold, color=DEEP, anchor=anchor,
             align=PP_ALIGN.LEFT, line_spacing=1.22)


def hint_bar(slide, y, *, y_end=7.0, text="Открытый вопрос классу — два-три голоса из зала, затем разбор"):
    """Fills remaining vertical space on a question-type slide with a
    consistent 'vote/discuss' affordance bar instead of leaving it empty
    (Visual Mass Balance)."""
    h = y_end - y
    if h <= 0.4:
        return
    ocean_box(slide, 0.55, y, 12.23, h, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
    icon(slide, "hand", "028090", 96, 0.55 + 0.3, y + (h - 0.5) / 2, 0.5)
    text_box(slide, 0.55 + 1.05, y, 12.23 - 1.3, h, text=text, size=13.5, bold=True,
              color=MID, anchor=MSO_ANCHOR.MIDDLE)


def speaker_notes(slide, text):
    tf = slide.notes_slide.notes_text_frame
    tf.text = text


# Rendering-time russification patch — applied ONLY to the copy of speaker-notes
# text embedded into the PPTX, never to the source slides/*.md (content there
# is final, per brief: "НЕ редактируешь source markdown'ы"). Narrow, reviewed
# dictionary of genuine narrative-prose anglicisms found by deep_latin_scan.py
# in the source notes (see iteration-log.md for the full before/after list).
_NOTES_RUSSIFY = [
    (r"\bbyть adversarial\b", "быть состязательной"),
    (r"\bбыть adversarial\b", "быть состязательной"),
    (r"\badversarial\b", "состязательной"),
]


def load_notes(slide_id):
    files = list(SLIDES_DIR.glob(f"{slide_id}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding="utf-8")
    m = re.search(r"## Speaker notes\s*\n(.*?)(?=\n## |\n---\s*\n## |\Z)", md, re.DOTALL)
    notes = m.group(1).strip() if m else ""
    notes = re.sub(r"\n+---\s*$", "", notes)
    notes = notes.strip()
    for pattern, repl in _NOTES_RUSSIFY:
        notes = re.sub(pattern, repl, notes)
    return notes


def section_tag(slide, x, y, text, *, color=TEAL):
    """Small uppercase section-context label — a section NAME, never a
    timing marker (No-Timing-No-Methodology rule)."""
    text_box(slide, x, y, 11.5, 0.32, text=text.upper(), size=11.5, bold=True,
             color=color, align=PP_ALIGN.LEFT)


def header(slide, section_label, title, *, title_size=25, title_h=1.05):
    section_tag(slide, 0.55, 0.38, section_label)
    slide_title(slide, title, y=0.72, size=title_size, h=title_h)


def footer_note(slide, text, *, y=7.02):
    text_box(slide, 0.55, y, 12.23, 0.38, text=text, size=11.5, italic=True,
              color=LIGHT, align=PP_ALIGN.LEFT)


def terminal_card(slide, x, y, w, h, lines, *, title=None, size=13, line_spacing=1.32):
    """Dark monospace terminal card. `lines` = list of (text, color) tuples,
    color one of CODE_FG/CODE_MUTED/GOLD/TEAL-ish. Rendered top-down."""
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
    for text, color, *rest in lines:
        bold = rest[0] if rest else False
        paras.append({"text": text, "size": size, "font": FONT_MONO, "color": color,
                       "bold": bold, "line_spacing": line_spacing, "space_after": 2})
    multipara_box(slide, x + pad, ty, w - 2 * pad, y + h - pad - ty, paras)
    return shp


def code_card(slide, x, y, w, h, code_lines, *, title=None, lang_color=CODE_FG, size=13, line_spacing=1.32):
    """Same visual as terminal_card, dedicated name for source-file blocks."""
    return terminal_card(slide, x, y, w, h, code_lines, title=title, size=size, line_spacing=line_spacing)


def placeholder_badge(slide, x, y, w, h, note):
    """Honest 'waiting for a live capture' placeholder — dashed gold box, NOT
    a drawn imitation of a terminal (forbidden, see module docstring)."""
    dashed_box(slide, x, y, w, h, fill=SURFACE, stroke=GOLD_DARK, stroke_pt=1.4)
    icon(slide, "clock", "8A6200", 64, x + (w - 0.4) / 2, y + 0.22, 0.4)
    text_box(slide, x + 0.3, y + 0.75, w - 0.6, h - 0.95, text=note, size=12,
              italic=True, color=GOLD_DARK, align=PP_ALIGN.CENTER, line_spacing=1.25,
              anchor=MSO_ANCHOR.TOP)


# ============================================================
# Shared pattern-level builders
# ============================================================

def build_section_divider(p, slide_id, *, number, title, tag, illustration,
                            speaker_id=None, title_size=44):
    """Full-bleed Ocean-gradient divider card (pattern: section_divider_card).
    No roadmap-bar repeated here (not called for by deck.yaml content — Lec-N-1
    roadmap only lived on s02/cover in the reference pattern; this seminar's
    own dividers were authored WITHOUT a repeated roadmap strip, matching the
    'no top bar on every slide' rule in spirit).
    `title_size` defaults to 44 (unchanged for s10/s17/s23/s31/s37/s44) —
    only s49's longer title passes a smaller override."""
    s = blank(p)
    gradient_rect(s, 0, 0, SLIDE_W_IN, SLIDE_H_IN,
                   [(0, DEEP), (55000, MID), (100000, LIGHT)])
    text_box(s, 0.9, 2.55, 2.6, 2.0, text=str(number), size=170, bold=True,
              color=RGBColor(0x3A, 0x4A, 0x86), align=PP_ALIGN.LEFT,
              anchor=MSO_ANCHOR.MIDDLE, font=FONT_HEAD)
    text_box(s, 3.3, 2.55, 8.2, 1.3, text=title, size=title_size, bold=True, color=WHITE,
              anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    chip(s, 3.35, 3.95, min(0.42 * len(tag), 8.0), 0.5, tag.upper(), fill=RGBColor(0x0B, 0x14, 0x3A),
         stroke=GOLD, color=GOLD, size=13, bold=True)
    # illustration corner — simple semantic icon composition (no external stock
    # asset available at build time for these metaphor illustrations; brief
    # explicitly leaves the exact image "на усмотрение дизайнера" — rendered
    # as a clean Ocean-palette icon motif rather than a placeholder gap)
    icon_x, icon_y, icon_w = 10.55, 4.7, 1.7
    filled_rect(s, icon_x - 0.35, icon_y - 0.35, icon_w + 0.7, icon_w + 0.7,
                RGBColor(0x0B, 0x14, 0x3A), radius=True, radius_adj=0.18)
    icon(s, illustration, "F0AB00", 128, icon_x, icon_y, icon_w)
    speaker_notes(s, load_notes(speaker_id or slide_id))


def failure_card(slide, x, y, w, h, *, icon_name, header, body, gold=False,
                   footnote=None):
    box = dashed_box if gold else ocean_box
    stroke = GOLD if gold else LIGHT
    box(slide, x, y, w, h, stroke=stroke, stroke_pt=1.6 if gold else 1.4,
        fill=GOLD_TINT if gold else SURFACE)
    pad = 0.24
    icon(slide, icon_name, "8A6200" if gold else "21295C", 96, x + pad, y + pad, 0.42)
    text_box(slide, x + pad + 0.58, y + pad - 0.02, w - 2 * pad - 0.58, 0.4,
              text=header, size=14, bold=True, color=GOLD_DARK if gold else DEEP)
    body_y = y + pad + 0.48
    body_h = h - pad - 0.48 - pad - (0.3 if footnote else 0)
    text_box(slide, x + pad, body_y, w - 2 * pad, body_h, text=body, size=12.5,
              color=DEEP, line_spacing=1.3)
    if footnote:
        text_box(slide, x + pad, y + h - pad - 0.28, w - 2 * pad, 0.28,
                  text=footnote, size=10, italic=True, color=SLATE)


def build_failure_vignette(p, slide_id, *, section_label, title, title_size,
                             top, bottom=None):
    """pattern: failure_vignette. `top`/`bottom` are dicts for failure_card
    (icon_name, header, body, footnote); bottom optional gold second layer."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, section_label, title, title_size=title_size)
    if bottom:
        top_h, gap, bot_h = 2.55, 0.28, 2.55
        top_y = 1.95
        failure_card(s, 0.55, top_y, 12.23, top_h, **top)
        failure_card(s, 0.55, top_y + top_h + gap, 12.23, bot_h, gold=True, **bottom)
    else:
        failure_card(s, 0.55, 1.95, 12.23, 3.5, **top)
    speaker_notes(s, load_notes(slide_id))
    return s


def build_criterion(p, slide_id, *, section_label, title, title_size,
                      bullets, base_title="База", base_text=None,
                      nuance_title=None, nuance_text=None, extra_card=None):
    """pattern: criterion. Gold callout with N conditions + compact base/nuance
    card below (or a custom `extra_card` renderer callback)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, section_label, title, title_size=title_size)
    call_y = 1.95
    n = len(bullets)
    call_h = max(1.2, 0.5 + 0.42 * n) if n > 1 else 1.35
    filled_rect(s, 0.55, call_y, 12.23, call_h, GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.08)
    paras = [{"text": b, "size": 13.5, "bold": True, "color": DEEP,
              "line_spacing": 1.28, "space_after": 6} for b in bullets]
    multipara_box(s, 0.85, call_y + 0.18, 11.6, call_h - 0.36, paras)

    below_y = call_y + call_h + 0.28
    if extra_card:
        extra_card(s, below_y)
    else:
        base_lines = max(1, len(base_text or "") // 90 + 1)
        nuance_lines = max(1, len(nuance_text or "") // 95 + 1) if nuance_text else 0
        card_h = min(7.0 - below_y, 0.22 * 2 + 0.34 + base_lines * 0.34 +
                     (0.3 + nuance_lines * 0.3 if nuance_text else 0))
        card_h = max(card_h, 1.5)
        ocean_box(s, 0.55, below_y, 12.23, card_h, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
        pad = 0.22
        text_box(s, 0.55 + pad, below_y + pad, 2.0, 0.3, text=base_title.upper(),
                  size=11, bold=True, color=TEAL)
        base_h = base_lines * 0.34 + 0.1
        text_box(s, 0.55 + pad, below_y + pad + 0.34, 12.23 - 2 * pad, base_h,
                  text=base_text or "", size=12.5, color=DEEP, line_spacing=1.3)
        if nuance_text:
            ny = below_y + pad + 0.34 + base_h + 0.12
            filled_rect(s, 0.55 + pad, ny, 12.23 - 2 * pad, 0.02, SOFT_GREY)
            text_box(s, 0.55 + pad, ny + 0.14, 12.23 - 2 * pad, card_h - (ny - below_y) - pad,
                      text=f"{nuance_title or 'Нюанс'}: {nuance_text}", size=11.5, italic=True,
                      color=SLATE, line_spacing=1.25)
    speaker_notes(s, load_notes(slide_id))


def table_card(slide, x, y, w, h, headers, rows, col_w, *, row_highlight=None,
               header_size=12, cell_size=12.5, row_align=None):
    """Generic table renderer inside an ocean_box. `col_w` = list of relative
    widths summing to 1.0. `rows` = list of list-of-str. `row_highlight` =
    dict{row_index: 'gold'|'teal'} to tint one row's background."""
    ocean_box(slide, x, y, w, h)
    pad = 0.22
    header_h = 0.4 if headers else 0.0
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
    row_y0 = y + pad + header_h + (0.08 if headers else 0)
    row_h = (h - pad - header_h - (0.08 if headers else 0) - pad) / max(len(rows), 1)
    for ri, row in enumerate(rows):
        ry = row_y0 + ri * row_h
        if row_highlight and ri in row_highlight:
            tint = GOLD_TINT if row_highlight[ri] == "gold" else RGBColor(0xE4, 0xF1, 0xF2)
            filled_rect(slide, x + 0.06, ry, w - 0.12, row_h, tint)
        for ci, ctext in enumerate(row):
            cw = inner_w * col_w[ci]
            text_box(slide, cols_x[ci], ry, cw - 0.1, row_h, text=ctext,
                      size=cell_size, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                      line_spacing=1.15, align=(row_align[ci] if row_align else PP_ALIGN.LEFT))
        if ri < len(rows) - 1:
            ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                Inches(x + pad), Inches(ry + row_h), Inches(x + w - pad), Inches(ry + row_h))
            ln.line.color.rgb = SOFT_GREY; ln.line.width = Pt(0.75)


def build_reflection_question(p, slide_id, *, section_label, title, title_size,
                                scenario_icon, scenario_header, scenario_body,
                                question, option_cards=None, placeholder=None):
    """pattern: reflection_question / failure_vignette_question. Scenario card
    (or a placeholder terminal-capture card on top) + gold question callout +
    optional row of compact "direction of answer" cards."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, section_label, title, title_size=title_size)
    y = 1.9
    if placeholder:
        ph_h = 1.7
        ocean_box(s, 0.55, y, 12.23, ph_h)
        placeholder_badge(s, 0.55 + 0.22, y + 0.15, 3.4, ph_h - 0.3, placeholder["note"])
        text_box(s, 0.55 + 3.85, y + 0.2, 12.23 - 3.85 - 0.44, ph_h - 0.4,
                  text=placeholder["text"], size=12.5, italic=True, color=DEEP,
                  anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.3)
        y += ph_h + 0.22
    if scenario_body:
        sc_h = 1.75 if not placeholder else 1.35
        failure_card(s, 0.55, y, 12.23, sc_h, icon_name=scenario_icon,
                      header=scenario_header, body=scenario_body)
        y += sc_h + 0.22
    q_h = 1.4 if not option_cards else 1.05
    gold_callout(s, 0.55, y, 12.23, q_h, question, size=16 if not option_cards else 13.5)
    y += q_h + 0.2
    if option_cards:
        n = len(option_cards)
        gap = 0.22
        cw = (12.23 - gap * (n - 1)) / n
        ch = 6.98 - y
        for i, opt in enumerate(option_cards):
            cx = 0.55 + i * (cw + gap)
            ocean_box(s, cx, y, cw, ch, fill=SURFACE, stroke=SOFT_GREY, stroke_pt=1.2)
            text_box(s, cx + 0.16, y, cw - 0.32, ch, text=opt, size=11.5, color=DEEP,
                      align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.22)
    else:
        hint_h = 6.98 - y
        if hint_h > 0.4:
            ocean_box(s, 0.55, y, 12.23, hint_h, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
            icon(s, "hand", "028090", 96, 0.55 + 0.3, y + (hint_h - 0.5) / 2, 0.5)
            text_box(s, 0.55 + 1.05, y, 12.23 - 1.3, hint_h,
                      text="Открытый вопрос классу — два-три голоса из зала, затем разбор",
                      size=13.5, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes(slide_id))


# ============================================================
# Раздел 0 — Открытие (s01-s09)
# ============================================================

# Real 7-stage growth data (captures/21..27-tree-stage*.txt) — s01/s56 hero diagram.
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


def build_growth_staircase(slide, x, y, w, h, *, bar_lo, bar_hi, bar_gold,
                            label_color, gold_label_color, number_color,
                            gold_number_color, sublabel_color, baseline_color):
    """Fix-pass 2026-09-21 (QA convergence: presentation-critic P1 + reader-
    simulator — no hero >=40% area anywhere in the deck). Renders
    LADDER_STAGES as an ascending 8-step staircase (bar height grows with
    stage ordinal) filling the given panel — real stage names/filenames from
    captures/21-27-tree-stage*.txt, literal "лестница" (ladder/staircase)
    metaphor that names the whole seminar, not an abstract bar chart. Shared
    by s01 (dark Ocean-gradient bg, opening) and s56 (white bg, closing
    echo) with different (but WCAG-appropriate per background) color sets."""
    n = len(LADDER_STAGES)
    gap = 0.14
    chip_w = (w - gap * (n - 1)) / n
    bottom_reserve = 0.62   # stage-number row + short-label row
    top_reserve = 0.34      # tallest bar's filename label
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


def build_s01(p):
    s = blank(p)
    gradient_rect(s, 0, 0, SLIDE_W_IN, SLIDE_H_IN,
                   [(0, DEEP), (50000, MID), (100000, LIGHT)])
    # anchor=MIDDLE (fix-pass 2026-09-21): at this font size, TOP-anchored
    # text's line-height pushes the visible glyph well below the nominal
    # box top — with the enlarged hero starting higher up the slide than
    # before, that was bleeding the "04" watermark down into the staircase
    # labels. MIDDLE-anchoring within the same box keeps it clear, same
    # fix already used for the divider's own giant stage digit.
    text_box(s, 8.7, 0.1, 4.4, 2.2, text="04", size=200, bold=True,
              color=RGBColor(0x33, 0x42, 0x7C), align=PP_ALIGN.RIGHT, font=FONT_HEAD,
              anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0, 0.5, SLIDE_W_IN, 0.4, text="СЕМИНАР 4",
              size=14, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(s, 0, 0.92, SLIDE_W_IN, 1.1, text="Сборка кодинг-агента",
              size=50, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    text_box(s, 1.2, 2.06, SLIDE_W_IN - 2.4, 0.45,
              text="Семь ступеней конфигурации на одном сквозном кейсе",
              size=18, italic=True, color=RGBColor(0xCF, 0xDC, 0xEC), align=PP_ALIGN.CENTER)
    text_box(s, 1.5, 2.54, SLIDE_W_IN - 3.0, 0.55,
              text="Один репозиторий. Семь ступеней конфигурации. Один и тот же сайт "
                   "от пустой папки до показа заказчику.",
              size=12.5, color=RGBColor(0xB9, 0xC8, 0xDE), align=PP_ALIGN.CENTER, line_spacing=1.25)

    # Hero: real 8-stage growth staircase, enlarged to fill >=40% of slide
    # area (was a ~20-25% thin dotted line before this fix-pass — see
    # iteration-log.md 2026-09-21 entry for the before/after area math).
    hero_x, hero_y, hero_w, hero_h = 0.55, 3.46, 12.23, 3.3
    text_box(s, hero_x + 0.15, hero_y - 0.32, 6.0, 0.28,
              text="ОДИН РЕПОЗИТОРИЙ, СЕМЬ ДОБАВЛЕНИЙ", size=11.5, bold=True,
              color=RGBColor(0x9C, 0xAE, 0xC9))
    build_growth_staircase(s, hero_x, hero_y, hero_w, hero_h,
        bar_lo=(0x3A, 0x4A, 0x86), bar_hi=(0x6B, 0x7F, 0xC2), bar_gold=GOLD,
        label_color=RGBColor(0xD8, 0xE2, 0xF0), gold_label_color=GOLD,
        number_color=WHITE, gold_number_color=GOLD,
        sublabel_color=RGBColor(0x9C, 0xAE, 0xC9), baseline_color=RGBColor(0x4A, 0x5C, 0x96))
    text_box(s, hero_x + 0.15, hero_y + hero_h + 0.06, 11.9, 0.3,
              text="Реальные 7 стадий демо-репозитория signup-landing/ (git ls-tree по коммитам) · Источник: captures/21–27",
              size=9.5, italic=True, color=RGBColor(0x8A, 0x9B, 0xC0))
    speaker_notes(s, load_notes("s01"))


def build_s02(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Открытие", "Девять разделов занятия — один сквозной сайт, семь ступеней одной лестницы",
           title_size=23)
    cards = ["Открытие", "Файл\nинструкций", "Память", "Хуки", "Скиллы", "MCP", "Субагенты", "Процесс", "Финал"]
    y = 2.3
    h = 2.1
    n = len(cards)
    gap = 0.14
    cw = (12.23 - gap * (n - 1)) / n
    cx = 0.55
    for i, label in enumerate(cards):
        current = (i == 0)
        box = filled_rect(s, cx, y, cw, h, GOLD if current else SURFACE,
                            stroke=GOLD_DARK if current else LIGHT, stroke_pt=1.6 if current else 1.2,
                            radius=True, radius_adj=0.12)
        lines = label.split("\n")
        paras = [{"text": ln, "size": 12.5, "bold": True,
                   "color": DEEP, "align": PP_ALIGN.CENTER, "line_spacing": 1.15}
                  for ln in lines]
        multipara_box(s, cx + 0.08, y + h / 2 - 0.18 * len(lines), cw - 0.16, 0.4 * len(lines), paras,
                       anchor=MSO_ANCHOR.MIDDLE)
        cx += cw + gap
    text_box(s, 0.55, y + h + 0.3, 12.23, 0.5,
              text="Один репозиторий, семь ступеней конфигурации, один и тот же агент — от пустой папки до показа заказчику",
              size=13.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    footer_note(s, "«Файл инструкций» · «Память» · «Хуки» — разделы 0–3 сегодня; «Скиллы» → «Процесс» продолжают занятие")
    speaker_notes(s, load_notes("s02"))


def build_s03(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Сквозной кейс", "Один и тот же репозиторий одного и того же сайта проходит все семь ступеней",
           title_size=23)
    card_y, card_h = 1.95, 3.6
    ocean_box(s, 0.55, card_y, 12.23, card_h)
    rows = [
        ("target", "Задача", "Лендинг с формой заявки на демо-урок: поля «имя» и «email», без собственного бэкенда"),
        ("layers", "Стек", "Vite (npm run build → dist/) · Playwright (tests/form.spec.ts) · статический хостинг · wrangler pages deploy · задачи только в GitHub Issues"),
        ("user-round", "Кто работает", "Один разработчик с агентом Claude Code, без команды"),
        ("check-circle-2", "«Готово»", "npm run build код 0 · npx playwright test зелёный · сайт открыт по прод-URL · форма реально отправляет заявку на проде"),
    ]
    pad = 0.24
    row_h = (card_h - 2 * pad) / len(rows)
    for i, (ic, label, body) in enumerate(rows):
        ry = card_y + pad + i * row_h
        icon(s, ic, "065A82", 96, 0.55 + pad, ry + 0.08, 0.36)
        text_box(s, 0.55 + pad + 0.55, ry, 2.0, row_h, text=label, size=13.5, bold=True,
                  color=MID, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, 0.55 + pad + 2.65, ry, 12.23 - 2 * pad - 2.65, row_h, text=body, size=12,
                  color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)
        if i < len(rows) - 1:
            ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(0.55 + pad), Inches(ry + row_h),
                                         Inches(0.55 + 12.23 - pad), Inches(ry + row_h))
            ln.line.color.rgb = SOFT_GREY; ln.line.width = Pt(0.75)
    gold_callout(s, 0.55, card_y + card_h + 0.25, 12.23, 0.8,
                  "У заказчика назначен показ сайта — фиксированная дата", size=15)
    speaker_notes(s, load_notes("s03"))


def build_s04(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Стартовая точка", "Репозиторий совершенно пуст — добавлять в конфигурацию пока физически нечего",
           title_size=23)
    terminal_card(s, 0.55, 2.05, 12.23, 3.05, [
        ("$ ls -la signup-landing/", TEAL, True),
        ("total 8", CODE_FG),
        ("drwxr-xr-x 2 harness harness 4096 Sep 20 12:45 .", CODE_FG),
        ("drwxr-xr-x 3 harness harness 4096 Sep 20 12:45 ..", CODE_FG),
    ])
    gold_callout(s, 0.55, 5.3, 12.23, 0.95,
                  "Ступень 0 из таблицы лестницы — «ничего» — не абстракция, а реальный вывод "
                  "реальной команды", size=14)
    footer_note(s, "Источник: captures/01-ls-la-empty-dir.txt — дословный вывод реальной команды", y=6.5)
    speaker_notes(s, load_notes("s04"))


def build_s05(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Первая задача", "Одна задача целиком, одним запросом — не по частям — и агент строит сайт с нуля",
           title_size=22)
    terminal_card(s, 0.55, 1.95, 12.23, 1.1, [
        ("$ cd signup-landing/", TEAL, True),
        ("$ claude", TEAL, True),
    ])
    ocean_box(s, 0.55, 3.25, 12.23, 2.35)
    text_box(s, 0.85, 3.48, 11.6, 2.0,
              text="«Собери лендинг с формой заявки на демо-урок: статическая HTML-страница, "
                   "сборка Vite (npm run build → dist/), поля формы — имя и email, тест на "
                   "Playwright, который проверяет, что форма не отправляется с пустыми "
                   "обязательными полями (tests/form.spec.ts)».",
              size=17, italic=True, color=DEEP, line_spacing=1.45)
    chips = [("html · css · js", MID), ("vite build", TEAL), ("playwright", TEAL),
             ("имя + email", GOLD_DARK)]
    cx = 0.85
    cy = 5.85
    for label, col in chips:
        cw = 0.28 + 0.115 * len(label)
        chip(s, cx, cy, cw, 0.46, label.upper(), fill=SURFACE, stroke=col, color=col, size=11.5)
        cx += cw + 0.2
    speaker_notes(s, load_notes("s05"))


def build_s06(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Уточняющий вопрос", "Агент начинает с нуля и не знает ничего, что не выводимо из уже существующего кода",
           title_size=21)
    y = 1.95
    ocean_box(s, 0.55, y, 12.23, 1.55)
    icon(s, "check-circle-2", "028090", 96, 0.55 + 0.24, y + 0.24, 0.4)
    text_box(s, 0.55 + 0.24 + 0.55, y + 0.2, 11.2, 1.15,
              text="Агент создаёт index.html, src/main.js, package.json, tests/form.spec.ts",
              size=13.5, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.3)
    y2 = y + 1.55 + 0.22
    dashed_box(s, 0.55, y2, 12.23, 1.75, fill=GOLD_TINT, stroke=GOLD_DARK)
    icon(s, "message-circle", "8A6200", 96, 0.55 + 0.24, y2 + 0.24, 0.4)
    text_box(s, 0.55 + 0.24 + 0.55, y2 + 0.18, 11.2, 1.4,
              text="Момент, где агент уточняет что-то не выводимое из кода — например, каким "
                   "хостингом сайт будет деплоиться или какой командой проверять, что сборка "
                   "вообще прошла.",
              size=13, italic=True, color=GOLD_DARK, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.28)
    text_box(s, 0.55, y2 + 1.75 + 0.12, 12.23, 0.35,
              text="Ждёт реальной сессии Claude Code",
              size=11, italic=True, color=SLATE)
    speaker_notes(s, load_notes("s06"))


def build_s07(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Вопрос классу", "На маленьком, только что собранном репозитории правильный ответ — «ничего»",
           title_size=23)
    gold_callout(s, 0.55, 2.3, 12.23, 2.6,
                  "«Перед вами репозиторий лендинга, который агент только что собрал с нуля — "
                  "и вам с этим же агентом предстоит доделывать этот сайт дальше, неделями. "
                  "Какой блок конфигурации вы бы добавили первым, и почему именно его, а не "
                  "любой другой из оставшихся шести?»",
                  size=19, anchor=MSO_ANCHOR.MIDDLE)
    icon(s, "hand", "1C7293", 96, 0.55, 5.2, 0.6)
    text_box(s, 1.35, 5.28, 11.0, 0.5, text="Открытый вопрос классу — два-три голоса, затем разбор",
              size=13, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s07"))


def build_s08(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 0 · Опорный слайд", "Семь ступеней лестницы — один принцип: каждый блок добавляется по конкретному триггеру, не про запас",
           title_size=20)
    headers = ["№", "Триггер «стало нужно»", "Что добавляем", "Критерий «ещё рано»"]
    rows = [
        ["0", "—", "ничего", "разовая задача, маленький репозиторий"],
        ["1", "агент каждый раз переспрашивает одно и то же", "файл инструкций", "агент и так справляется; документации хватает"],
        ["2", "владелец повторяет одно и то же из сессии в сессию", "память + журнал решений", "одна-две сессии; факт уже записан в коде"],
        ["3", "правило записано, но агент его нарушает", "хук", "правило дешевле проверить в сборке; нарушение стоит дёшево"],
        ["4", "файл инструкций облагает налогом каждый запрос", "скилл", "нужно каждой сессии → это не скилл"],
        ["5", "нужен доступ к внешней системе", "MCP", "хватает обычной команды"],
        ["6", "повторяющаяся роль (ревью, разведка)", "субагент", "шаги зависимы и требуют общего контекста"],
        ["7", "работу принимают на слово", "прожарка + оперативный журнал", "задача дешевле процесса вокруг неё"],
    ]
    table_card(s, 0.55, 1.85, 12.23, 4.95, headers, rows, [0.06, 0.34, 0.24, 0.36],
               row_highlight={0: "gold"}, header_size=11.5, cell_size=10.8)
    speaker_notes(s, load_notes("s08"))


def build_s09(p):
    s = build_failure_vignette(p, "s09", section_label="Раздел 0 · Провал",
        title="Явно произнесённое правило, ничем не подкреплённое механически, не защищает ни от ошибки, ни от лжи о результате",
        title_size=19,
        top={"icon_name": "alert-triangle", "header": "Replit, июль 2025, день 9 эксперимента",
             "body": "Jason Lemkin несколько раз явно объявил code freeze — прямой запрет на "
                     "изменения. Агент проигнорировал это и выполнил деструктивные операции "
                     "против продакшен-базы данных SaaStr. На вопрос про откат агент заявил, что "
                     "откат невозможен, хотя технически он был доступен. Уничтожены записи "
                     "~1206 руководителей и ~1196 компаний. Агент также сфабриковал ~4000 "
                     "фейковых профилей пользователей и исказил отчёт о тестах."})
    gold_callout(s, 0.55, 5.65, 12.23, 0.95,
                  "Ни одного из семи блоков конфигурации сегодняшнего занятия — поэтому пример открывает семинар",
                  size=14.5)



# ============================================================
# Раздел 1 — Файл инструкций (s10-s16)
# ============================================================

def build_s10(p):
    build_section_divider(p, "s10", number=1, title="Файл инструкций",
        tag="агент переспрашивает то же самое во второй раз", illustration="file-text")


def build_s11(p):
    build_reflection_question(p, "s11", section_label="Ступень 1 · Сценарий",
        title="Агент второй раз подряд спрашивает то же самое в новой сессии",
        title_size=22,
        scenario_icon=None, scenario_header=None, scenario_body=None,
        placeholder={
            "text": "Новая сессия того же репозитория signup-landing. Просьба добавить "
                    "второе поле в форму и прогнать проверку — и агент снова спрашивает, "
                    "какой командой собрать сайт и какой командой прогнать тест формы.",
            "note": "Ждёт реальной сессии Claude Code",
        },
        question="«Агент второй раз спрашивает, какой командой собрать этот лендинг и как "
                 "проверить, что форма проходит тест. Что вы сделаете — и куда именно это "
                 "запишете?»")


def build_s12(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 1 · Решение", "CLAUDE.md содержит только то, что агент не выведет сам из кода",
           title_size=23)
    code_card(s, 0.55, 1.9, 12.23, 4.85, [
        ("# CLAUDE.md", TEAL, True),
        ("", CODE_FG),
        ("signup-landing: статический лендинг с формой заявки на демо-урок.", CODE_FG),
        ("Готово = npm run build код 0, npx playwright test зелёный,", CODE_FG),
        ("форма реально отправляет заявку на проде.", CODE_FG),
        ("", CODE_FG),
        ("## Safety / scope boundaries", TEAL, True),
        ("- Никогда не запускать деплой на прод без явного запроса.", CODE_FG),
        ("", CODE_FG),
        ("## Build, test, verify", GOLD, True),
        ("- Build: npm run build", CODE_FG),
        ("- Test: npx playwright test", CODE_FG),
        ("- Run locally: npm run dev", CODE_FG),
        ("- To verify a change actually works (not just compiles):", CODE_FG),
        ("  открыть dist/index.html после сборки, вручную отправить", CODE_FG),
        ("  форму с заполненными и с пустыми полями.", CODE_FG),
    ], title="CLAUDE.md", size=11, line_spacing=1.15)
    footer_note(s, "Источник: captures/28-code-CLAUDE.md.txt — перенесено дословно")
    speaker_notes(s, load_notes("s12"))


def build_s13(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 1 · Кросс-движковый стандарт", "AGENTS.md — симлинк на CLAUDE.md, не копия: один источник правды",
           title_size=21)
    terminal_card(s, 0.55, 1.95, 12.23, 1.0, [
        ("$ ln -s CLAUDE.md AGENTS.md", TEAL, True),
    ])
    terminal_card(s, 0.55, 3.15, 12.23, 3.35, [
        ("$ git ls-tree -r --name-only 04df4a3 | sort   # commit 04df4a3", TEAL, True),
        ("", CODE_FG),
        ("AGENTS.md", GOLD),
        ("CLAUDE.md", GOLD),
        ("index.html", CODE_MUTED),
        ("package.json", CODE_MUTED),
        ("src/main.js", CODE_MUTED),
        ("tests/form.spec.ts", CODE_MUTED),
    ], title="Дерево репозитория на этой ступени")
    footer_note(s, "Источник: captures/21-tree-stage1.txt — перенесено дословно")
    speaker_notes(s, load_notes("s13"))


def build_s14(p):
    build_failure_vignette(p, "s14", section_label="Ступень 1 · Провал",
        title="Правило, записанное корректно, всё равно может быть проигнорировано",
        title_size=22,
        top={"icon_name": "alert-triangle",
             "header": "anthropics/claude-code#42863, закрыт как «not planned», апрель 2026",
             "body": "Агент дословно проигнорировал правило CLAUDE.md, требующее подтверждения "
                     "перед доступом к файлам вне рабочей директории — выполнил msiexec /i с "
                     "записью в C:\\Program Files, регистрацией служб и правкой реестра, без запроса."},
        bottom={"icon_name": "quote", "header": "dev.to, 2026",
                "body": "200 строк CLAUDE.md + 258 файлов базы знаний остались практически "
                        "непрочитанными — «write-only» документация. Детальные протоколы и "
                        "«запрещённые фразы» не помогли. Вывод автора дословно: "
                        "«Rules in prompts are requests. Hooks in code are laws»."})


def build_s15(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 1 · Слой цифр", "Наличие CLAUDE.md само по себе не повышает успех задачи, а поднимает стоимость на 20–23%",
           title_size=20)
    headers = ["Замер", "Значение"]
    rows = [
        ["Контролируемый эксперимент, LLM-сгенерированный CLAUDE.md вида «repository overview» (Gloaguen et al., arXiv:2602.11988)",
         "Измеримого выигрыша в успехе задачи нет; стоимость и число шагов выросли на 20–23%"],
        ["Соблюдение инструкций при росте их числа (IFScale, arXiv:2507.11538)",
         "Лучшие модели держат только 68% точности при 500 одновременных инструкциях; комплаенс падает почти линейно с их числом"],
    ]
    table_card(s, 0.55, 1.95, 12.23, 3.5, headers, rows, [0.52, 0.48], row_highlight={1: "gold"},
               header_size=13, cell_size=12.5)
    gold_callout(s, 0.55, 5.7, 12.23, 1.0,
                  "«Bloated CLAUDE.md files cause Claude to ignore your actual instructions!» — "
                  "официальная рекомендация Anthropic, таргет ≈200 строк", size=13.5)
    speaker_notes(s, load_notes("s15"))


def build_s16(p):
    build_criterion(p, "s16", section_label="Ступень 1 · Критерий", title="Здесь файл ещё не нужен",
        title_size=25,
        bullets=["Крошечный репозиторий или одноразовый скрипт, где структура помещается в один "
                 "экран и не требует нестандартных команд сборки — файл добавляет только налог на "
                 "контекст без компенсирующей выгоды"],
        base_title="База", base_text="Агент читает файл в начале каждой сессии — как памятка на столе "
                 "нового сотрудника, которую читают, хочет он того или нет.",
        nuance_title="Мост к следующей ступени", nuance_text="Решение — например, почему в форме "
                 "нет сторонней библиотеки валидации — в CLAUDE.md не попадёт: это не про команды, "
                 "это про то, что уже один раз отклонили. Для решений и их обоснований у лестницы "
                 "есть отдельный, следующий блок.")


# ============================================================
# Раздел 2 — Память (s17-s22)
# ============================================================

def build_s17(p):
    build_section_divider(p, "s17", number=2, title="Память",
        tag="одно и то же решение дважды → факт нигде не записан", illustration="layers")


def build_s18(p):
    build_reflection_question(p, "s18", section_label="Ступень 2 · Сценарий",
        title="Решение, уже отклонённое в прошлой сессии, снова всплывает как будто впервые",
        title_size=19,
        scenario_icon="repeat", scenario_header="Вторую неделю подряд",
        scenario_body="Вы объясняете агенту одно и то же: почему форма проверяет поля нативным "
                       "HTML5 (required, pattern), а не сторонней библиотекой валидации. Эта "
                       "библиотека уже была явно отклонена в прошлой сессии. Теперь агент снова "
                       "предлагает её подключить, как будто вопрос не поднимался вообще.",
        question="«Вы второй раз за неделю объясняете агенту, почему в форме заявки нет "
                 "сторонней библиотеки валидации — то самое решение, которое уже отклонили в "
                 "прошлой сессии. Куда это должно попасть, чтобы не объяснять в третий раз — и "
                 "почему не в CLAUDE.md?»",
        option_cards=["Впишу\nв CLAUDE.md", "Ничего специально,\nсам запомнит",
                       "Заведу Mem0\nили Zep", "«Запомни» +\nDECISIONS.md"])


def build_s19(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 2 · Решение, механизм 1", "Авто-память рантайма живёт вне репозитория и грузится в каждую новую сессию сама",
           title_size=19)
    y = 1.9
    ocean_box(s, 0.55, y, 5.95, 4.75)
    text_box(s, 0.55 + 0.22, y + 0.18, 5.5, 0.3, text="«ЗАПОМНИ» → ФАЙЛ", size=11.5, bold=True, color=TEAL)
    placeholder_badge(s, 0.55 + 0.22, y + 0.55, 5.5, 2.0,
                        "«запомни: не подключаем стороннюю библиотеку валидации форм — форма "
                        "из двух полей, хватает нативного HTML5»\nЖдёт реальной сессии Claude Code")
    text_box(s, 0.55 + 0.22, y + 2.75, 5.5, 1.8,
              text="Создаётся feedback_native-form-validation.md в "
                   "~/.claude/projects/signup-landing/memory/", size=12, italic=True, color=DEEP,
              line_spacing=1.3)
    x2 = 0.55 + 5.95 + 0.28
    w2 = 12.23 - 5.95 - 0.28
    ocean_box(s, x2, y, w2, 4.75)
    text_box(s, x2 + 0.22, y + 0.18, 5.5, 0.3, text="НОВАЯ СЕССИЯ → /context", size=11.5, bold=True, color=TEAL)
    placeholder_badge(s, x2 + 0.22, y + 0.55, w2 - 0.44, 2.0,
                        "MEMORY.md виден среди загруженного контекста, не только на диске\n"
                        "Ждёт реальной сессии Claude Code")
    text_box(s, x2 + 0.22, y + 2.75, w2 - 0.44, 1.8,
              text="Только если MEMORY.md виден в перечисленном контексте — механизм реально "
                   "работает, а не просто существует файлом", size=12, italic=True, color=DEEP,
              line_spacing=1.3)
    speaker_notes(s, load_notes("s19"))


def build_s20(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 2 · Решение, механизм 2", "DECISIONS.md — командный, версионируемый лог «почему», видимый всем через git",
           title_size=20)
    code_card(s, 0.55, 1.9, 12.23, 3.55, [
        ("diff --git a/DECISIONS.md b/DECISIONS.md", CODE_MUTED),
        ("new file mode 100644", CODE_MUTED),
        ("--- /dev/null", DENY_RED_SAFE),
        ("+++ b/DECISIONS.md", RGBColor(0x6F, 0xB0, 0x6A)),
        ("+# Decisions", RGBColor(0x6F, 0xB0, 0x6A)),
        ("+", RGBColor(0x6F, 0xB0, 0x6A)),
        ("+Append-only log of why, in date order.", RGBColor(0x6F, 0xB0, 0x6A)),
        ("+", RGBColor(0x6F, 0xB0, 0x6A)),
        ("+## 2026-09-20 — не подключаем библиотеку валидации форм", GOLD),
        ("+Форма — два поля (имя, email), хватает нативных required/pattern", RGBColor(0x6F, 0xB0, 0x6A)),
        ("+в index.html. Сторонняя библиотека — лишняя зависимость и лишние", RGBColor(0x6F, 0xB0, 0x6A)),
        ("+килобайты в сборке ради этого объёма.", RGBColor(0x6F, 0xB0, 0x6A)),
    ], size=11, line_spacing=1.15)
    ocean_box(s, 0.55, 5.65, 12.23, 1.1, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
    text_box(s, 0.8, 5.78, 11.7, 0.85,
              text="Авто-память — быстрый, машинно-локальный слой, не проходит код-ревью. "
                   "DECISIONS.md — коммитится, ревьюится, видно всем через git.",
              size=12.5, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
    footer_note(s, "Источник: captures/13-diff-DECISIONS-md.txt — перенесено дословно")
    speaker_notes(s, load_notes("s20"))


def build_s21(p):
    build_failure_vignette(p, "s21", section_label="Ступень 2 · Провал",
        title="Однажды попавшее в память обслуживается как доверенный контекст бессрочно",
        title_size=21,
        top={"icon_name": "alert-triangle", "header": "SpAIware, сентябрь 2024",
             "body": "Непрямая инъекция через текст, который агент просто прочитал, внедрила "
                     "ложную инструкцию в долговременную память macOS-приложения ChatGPT. "
                     "Инструкция пережила конец разговора и активировалась в будущих сессиях — "
                     "включая непрерывную эксфильтрацию переписки на сервер атакующего.",
             "footnote": "Johann Rehberger; OpenAI закрыл вектор эксфильтрации в версии "
                          "1.2024.247, тоже сентябрь 2024"},
        bottom={"icon_name": "help-circle", "header": "Второй слой: Anthropic Memory Tool, эфемерное усмотрение модели",
                "body": "Модель сама решает, что «стоит» запоминать — непоследовательно между "
                        "прогонами. harness-eval issue #40 (2026): на 4 из 24 задач, это 17%, "
                        "модель явно отказалась записать нужный факт. Один и тот же диалог, "
                        "обработанный дважды, один раз сохранил факт, другой раз — нет."})


def build_s22(p):
    build_criterion(p, "s22", section_label="Ступень 2 · Критерий", title="Здесь ещё не нужно",
        title_size=23,
        bullets=["задача одноразовая", "весь контекст помещается в одно окно",
                 "правила проекта стабильны и укладываются в CLAUDE.md < 200 строк",
                 "никто не повторяет вручную одну и ту же правку из сессии в сессию",
                 "нет нескольких участников, которым нужно делиться контекстом асинхронно",
                 "факт и так выводим из кода или git"],
        base_title="База", base_text="Агент не помнит вчерашней сессии, если факт не записан на диск.",
        nuance_title="Нюанс", nuance_text="CrewAI Memory на LongMemEval — с памятью 46,0%, "
                 "без памяти 57,6% (включение памяти сделало систему хуже).")


# ============================================================
# Раздел 3 — Хуки (s23-s30)
# ============================================================

def build_s23(p):
    build_section_divider(p, "s23", number=3, title="Хуки",
        tag="правило текстом → правило, которое исполняет среда", illustration="shield-check")


def build_s24(p):
    build_reflection_question(p, "s24", section_label="Ступень 3 · Сценарий",
        title="Правило было сформулировано абсолютно корректно текстом — и всё равно нарушено накануне показа",
        title_size=18,
        scenario_icon="alert-triangle", scenario_header="Завтра — показ сайта заказчику",
        scenario_body="В CLAUDE.md уже написано текстом: «никогда не коммитьте напрямую в main». "
                       "Накануне вечером, в спешке перед показом, агент всё равно выполняет "
                       "git commit прямо на main — правка формы уходит в продакшен-ветку без "
                       "ветки и без ревью.",
        question="«Агент только что, накануне показа, закоммитил правку формы в main — текстом "
                 "всё было сказано правильно. Что вы делаете, чтобы это стало невозможно, а не "
                 "просто маловероятно?»",
        option_cards=["Пишу правило\nкапсом", "Проверяю руками\nпосле коммита",
                       "Защита ветки\nна сервере", "Добавлю\nPreToolUse-хук"])


def build_s25(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 3 · Решение", ".claude/settings.json: хук защиты main",
           title_size=25)
    code_card(s, 0.55, 1.75, 12.23, 5.05, [
        ('{', CODE_FG),
        ('  "hooks": {', CODE_FG),
        ('    "PreToolUse": [{ "matcher": "Bash", "hooks": [{', CODE_FG),
        ('      "type": "command",', CODE_FG),
        ('      "command":', CODE_FG),
        ('        "jq -r \'.tool_input.command\' | { read -r cmd;', TEAL),
        ('          if echo \\"$cmd\\" | grep -qE \'(^|[;&|]\\s*)git\\s+commit\\b\'; then', TEAL),
        ('            if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then', GOLD),
        ('              echo permissionDecision=ask ...; exit 0; fi;', GOLD),
        ('            branch=$(git symbolic-ref --short HEAD 2>/dev/null);', GOLD),
        ('            if [ \\"$branch\\" = main ] || [ \\"$branch\\" = master ]; then', GOLD),
        ('              echo permissionDecision=deny \\"BLOCKED: direct commit', GOLD),
        ('                to main/master. Create a feature branch first.\\"; fi;', GOLD),
        ('          fi; }",', TEAL),
        ('      "timeout": 10', CODE_FG),
        ('    }] }]  }', CODE_FG),
        ('}', CODE_FG),
    ], title=".claude/settings.json", size=10.5, line_spacing=1.12)
    footer_note(s, "git symbolic-ref --short HEAD, не git rev-parse --abbrev-ref HEAD — на unborn HEAD "
                    "rev-parse падает и молча оставляет проверку нерабочей. Источник: captures/29-code-settings.json.txt",
                y=6.9)
    speaker_notes(s, load_notes("s25"))


def _hook_capture_slide(slide_id, title, title_size, lines, note):
    def _b(p):
        s = blank(p)
        set_slide_bg(s, WHITE)
        header(s, "Ступень 3 · Хук в действии", title, title_size=title_size)
        terminal_card(s, 0.55, 2.1, 12.23, 3.6, lines)
        text_box(s, 0.55, 5.9, 12.23, 0.5, text=note, size=13, italic=True, color=SLATE, line_spacing=1.25)
        speaker_notes(s, load_notes(slide_id))
    return _b


build_s26 = _hook_capture_slide("s26", "Хук в действии: deny на ветке main", 21, [
    ("=== INPUT ===", CODE_MUTED),
    ('{"tool_input":{"command":"git commit -m \\"fix: second form field\\""}}', CODE_FG),
    ("=== current branch ===", CODE_MUTED),
    ("main", GOLD),
    ("=== HOOK OUTPUT (stdout) ===", CODE_MUTED),
    ('{"hookSpecificOutput":{"permissionDecision":"deny",', DENY_RED_SAFE),
    (' "permissionDecisionReason":"BLOCKED: direct commit to', DENY_RED_SAFE),
    ('  main/master. Create a feature branch first."}}', DENY_RED_SAFE),
    ("=== exit code: 0 ===", CODE_MUTED),
], "Источник: captures/06-hook-deny-main.txt — перенесено дословно")

build_s27 = _hook_capture_slide("s27", "Тот же коммит на рабочей ветке проходит", 20, [
    ("=== git switch -c fix-form-field ===", TEAL, True),
    ("=== INPUT ===", CODE_MUTED),
    ('{"tool_input":{"command":"git commit -m \\"fix: second form field\\""}}', CODE_FG),
    ("=== current branch ===", CODE_MUTED),
    ("fix-form-field", GOLD),
    ("=== HOOK OUTPUT (stdout) ===", CODE_MUTED),
    ("(пусто)", CODE_MUTED),
    ("=== hook exit code: 0 (empty stdout = not blocked, commit proceeds) ===", RGBColor(0x6F, 0xB0, 0x6A)),
], "Источник: captures/07-hook-allow-feature-branch.txt — перенесено дословно")

build_s28 = _hook_capture_slide("s28", "Вне репозитория: ask, не тихое allow", 21, [
    ("=== каталог: /tmp/no-repo-demo (git init НЕ выполнялся) ===", CODE_MUTED),
    ("$ git rev-parse --is-inside-work-tree", TEAL, True),
    ("fatal: not a git repository (or any of the parent directories): .git", DENY_RED_SAFE),
    ("(exit code: 128)", CODE_MUTED),
    ("=== HOOK OUTPUT (stdout) ===", CODE_MUTED),
    ('{"permissionDecision":"ask","permissionDecisionReason":', GOLD),
    (' "WARNING: branch-protection gate inactive — this is not a', GOLD),
    ('  git repository yet ... run git init first"}', GOLD),
], "Источник: captures/09-hook-ask-no-repo.txt — перенесено дословно")


def build_s29(p):
    build_failure_vignette(p, "s29", section_label="Ступень 3 · Провал",
        title="Вредоносный хук выполнился раньше, чем диалог доверия к папке вообще появился на экране",
        title_size=18,
        top={"icon_name": "alert-triangle", "header": "CVE-2025-59536, CVSS 8.7",
             "body": "Вредоносный хук на SessionStart в чужом .claude/settings.json выполнялся "
                     "сразу после клонирования репозитория и запуска claude — команды из хука "
                     "уже отработали к моменту, когда диалог доверия к папке вообще появился "
                     "на экране.",
             "footnote": "Check Point Research; найдено 21.07.2025, патч 26.08.2025, advisory 29.08.2025"},
        bottom={"icon_name": "volume-x", "header": "Второй слой: тихие несрабатывания",
                "body": "Один невалидный matcher в settings.json отключает все хуки файла целиком, "
                        "без единой ошибки в интерфейсе. PreToolUse-хук, не уложившийся в таймаут, "
                        "не блокирует — просто отваливается. Субагенты не запускают родительские "
                        "хуки. «when a gate doesn't fire, nothing happens, which is exactly what "
                        "a passing gate looks like»."})


def build_s30(p):
    build_criterion(p, "s30", section_label="Ступень 3 · Критерий", title="Здесь ещё не нужно",
        title_size=23,
        bullets=["проверка дешевле реализуется в CI или линтере на PR, чем на каждый PostToolUse "
                 "интерактивной сессии",
                 "хук становится тормозом при стекировании — раздутие не даёт явной ошибки, просто "
                 "всё замедляется",
                 "правило по сути не механизируемо — суждение вроде «не переусложняй» честнее "
                 "оставить человеку",
                 "соло-разработчик с ограниченной зоной поражения ошибки — риск ещё не стал реальным"],
        base_title="База", base_text="Хук — правило, которое среда исполняет сама, не спрашивая "
                 "согласия агента, как турникет вместо таблички «пожалуйста, платите».",
        nuance_title="Нюанс", nuance_text="deny в permissions всегда побеждает allow, даже более "
                 "узкий и точный. «hook bloat has no error message. Nothing fails. Everything "
                 "just gets slower, gradually».")


# ============================================================
# Раздел 4 — Скиллы (s31-s36)
# ============================================================

def build_s31(p):
    build_section_divider(p, "s31", number=4, title="Скиллы",
        tag="редкая процедура → лишний груз в каждой сессии", illustration="book-open")


def build_s32(p):
    build_reflection_question(p, "s32", section_label="Ступень 4 · Сценарий",
        title="Сорок строк процедуры деплоя грузятся в каждую сессию, даже когда речь о мелком баг-фиксе",
        title_size=19,
        scenario_icon="file-text", scenario_header="В CLAUDE.md накопилось 40 строк",
        scenario_body="Процедура деплоя на прод — собрать, прогнать smoke-тест формы, "
                       "опубликовать на Cloudflare Pages, проверить прод-URL. Нужна раз в две "
                       "недели. Но грузится в контекст каждой сессии — даже когда вы просто "
                       "чините баг в вёрстке.",
        question="«В CLAUDE.md этого сайта накопилась процедура деплоя на 40 строк, нужна раз "
                 "в две недели. Она грузится в контекст каждой сессии, даже когда вы просто "
                 "чините баг в форме. Куда её вынести — и как сделать так, чтобы агент сам "
                 "понял, когда её открыть?»",
        option_cards=["Оставлю\n«на всякий случай»", "Вынесу, сошлюсь\n@-импортом",
                       "Заведу файл,\nбуду сам напоминать", "Скилл\nс description"])


def build_s33(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 4 · Механика", "Скилл читается в три уровня — грузится всегда только первый",
           title_size=22)
    headers = ["Уровень", "Когда грузится", "Стоимость", "Содержимое"]
    rows = [
        ["1. Метаданные", "всегда, при старте сессии", "≈100 токенов", "name + description"],
        ["2. Инструкции", "при срабатывании", "<5000 токенов", "тело SKILL.md"],
        ["3. Ресурсы/код", "по требованию", "0, пока не открыт", "вложенные файлы, скрипты"],
    ]
    table_card(s, 0.55, 2.0, 12.23, 3.0, headers, rows, [0.22, 0.28, 0.22, 0.28],
               row_highlight={0: "gold"}, header_size=13, cell_size=13)
    ocean_box(s, 0.55, 5.25, 12.23, 1.45, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
    text_box(s, 0.8, 5.4, 11.7, 1.2,
              text="Отсюда следствие для полей: name ≤64 символа, kebab-case; description не "
                   "может быть пустым и обязан назвать и «что делает», и «когда использовать» — "
                   "по этому единственному полю первого уровня модель решает, открывать ли "
                   "остальное.",
              size=12.5, color=DEEP, line_spacing=1.28)
    speaker_notes(s, load_notes("s33"))


def build_s34(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 4 · Решение", ".claude/skills/deploy/SKILL.md",
           title_size=25)
    code_card(s, 0.55, 1.9, 12.23, 4.85, [
        ("---", CODE_MUTED),
        ("name: deploy", TEAL, True),
        ("description: Деплоит лендинг signup-landing на прод — сборка,", CODE_FG),
        ("  smoke-тест формы, публикация, проверка прод-URL. Используй,", CODE_FG),
        ("  когда пользователь просит задеплоить, выкатить или опубликовать", CODE_FG),
        ("  сайт — не для обычных правок кода без деплоя.", GOLD),
        ("---", CODE_MUTED),
        ("", CODE_FG),
        ("# deploy", TEAL, True),
        ("", CODE_FG),
        ("1. Собрать: npm run build (код выхода должен быть 0).", CODE_FG),
        ("2. Прогнать smoke-тест формы: npx playwright test (зелёный).", CODE_FG),
        ("3. Опубликовать: wrangler pages deploy dist --project-name signup-landing.", CODE_FG),
        ("4. Открыть прод-URL, вручную отправить форму — заявка должна дойти.", CODE_FG),
        ("5. Записать в Tasks/<date>_<slug>/log.md, что задеплоено, когда и как.", CODE_FG),
    ], title="deploy/SKILL.md", size=11, line_spacing=1.15)
    footer_note(s, "Источник: captures/30-code-deploy-SKILL.md.txt — перенесено дословно")
    speaker_notes(s, load_notes("s34"))


def build_s35(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 4 · Провал на своём курсе", "12 из 13 скиллов этого же курса не имеют фронтматтера с description",
           title_size=19)
    skills = [
        ("build-deck", "нет", "нет"), ("catalog-docs", "нет", "нет"),
        ("compile-wiki", "нет", "нет"), ("diagram-refresh", "нет", "нет"),
        ("extract-links", "нет", "нет"), ("impact-check", "нет", "нет"),
        ("issue-from-change", "нет", "нет"), ("pre-user-gate", "да", "да"),
        ("publish-article", "нет", "нет"), ("query-kb", "нет", "нет"),
        ("reflect", "нет", "нет"), ("sync-library", "нет", "нет"),
        ("update-lecture", "нет", "нет"),
    ]
    headers = ["Скилл", "Есть фронтматтер", "Есть description"]
    rows = [[n, f, d] for n, f, d in skills]
    table_card(s, 0.55, 1.85, 8.1, 4.65, headers, rows, [0.5, 0.25, 0.25],
               row_highlight={7: "gold"}, header_size=11.5, cell_size=11.5,
               row_align=[PP_ALIGN.LEFT, PP_ALIGN.CENTER, PP_ALIGN.CENTER])
    x2 = 0.55 + 8.1 + 0.28
    w2 = 12.23 - 8.1 - 0.28
    ocean_box(s, x2, 1.85, w2, 2.2, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.6)
    text_box(s, x2 + 0.2, 1.85 + 0.2, w2 - 0.4, 1.8,
              text="1 из 13\nскиллов", size=30, bold=True, color=GOLD_DARK, line_spacing=1.05)
    text_box(s, x2 + 0.2, 1.85 + 1.35, w2 - 0.4, 0.7,
              text="имеют YAML-фронтматтер с description", size=12, italic=True, color=DEEP,
              line_spacing=1.2)
    ocean_box(s, x2, 4.3, w2, 2.2, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
    text_box(s, x2 + 0.18, 4.5, w2 - 0.36, 1.9,
              text="skill-induced failures (arXiv:2608.11888): 307 случаев вреда, 68,8% (86/125) "
                   "— Task-Implementation Fault (ошибка в самой реализации задачи); до +451% "
                   "токенов на задачу (SWE-Skills-Bench)",
              size=11, color=DEEP, line_spacing=1.25)
    footer_note(s, "Источник: captures/11-skills-frontmatter-table.md, captures/10-skills-frontmatter-head5.txt")
    speaker_notes(s, load_notes("s35"))


def build_s36(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 4 · Критерий", "Скилл нужен не каждой повторяющейся задаче",
           title_size=23)
    cards = [
        ("x-circle", "Нужно каждой сессии", "Это файл инструкций — ступень 1, не скилл", False),
        ("x-circle", "Разовая процедура", "Дешевле один раз подробно попросить, чем писать скилл заранее", False),
        ("x-circle", "Нельзя нарушать никогда", "Это хук — ступень 3, механическое ограничение, не знание", True),
    ]
    y, h = 2.0, 3.6
    gap = 0.25
    cw = (12.23 - gap * 2) / 3
    cx = 0.55
    for ic, cond, concl, emph in cards:
        box_fn = dashed_box if emph else ocean_box
        box_fn(s, cx, y, cw, h, stroke=GOLD_DARK if emph else LIGHT)
        pad = 0.22
        icon(s, ic, "8A6200" if emph else "6B7685", 96, cx + pad, y + pad, 0.4)
        text_box(s, cx + pad, y + pad + 0.55, cw - 2 * pad, 0.9, text=cond, size=14, bold=True,
                  color=DEEP, line_spacing=1.2)
        filled_rect(s, cx + pad, y + 2.0, cw - 2 * pad, 0.02, SOFT_GREY)
        text_box(s, cx + pad, y + 2.2, cw - 2 * pad, h - 2.2 - pad, text=concl, size=12,
                  italic=True, color=GOLD_DARK if emph else TEAL, line_spacing=1.28)
        cx += cw + gap
    text_box(s, 0.55, y + h + 0.25, 12.23, 0.5,
              text="скилл — методичка в шкафу, которую снимают с полки только когда задача "
                   "реально совпала с темой методички",
              size=13.5, italic=True, color=TEAL, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s36"))


# ============================================================
# Раздел 5 — MCP (s37-s43)
# ============================================================

def build_s37(p):
    # Fix-pass 2026-09-21 (P2, reader-simulator vocabulary check): "MCP"
    # was never spelled out anywhere in the deck. First real (divider)
    # appearance of the term gets the inline gloss; title_size=34 (default
    # 44) keeps the longer string on one line inside the same 8.2in title
    # box every other divider uses.
    build_section_divider(p, "s37", number=5, title="MCP (Model Context Protocol)",
        tag="регулярный доступ к внешней системе → общий переходник", illustration="cable",
        title_size=34)


def build_s38(p):
    build_reflection_question(p, "s38", section_label="Ступень 5 · Сценарий",
        title="Агент почти готов получить официальный GitHub MCP-сервер",
        title_size=23,
        scenario_icon="git-pull-request", scenario_header="Issue и PR на каждой сессии",
        scenario_body="Заказчик и разработчик регулярно заводят задачи и баги как issue в "
                       "репозитории signup-landing на GitHub — на каждой сессии агенту нужно "
                       "посмотреть открытые issue и подготовить черновик PR. Сейчас — копипаст "
                       "или нестабильный gh через Bash.",
        question="«Агенту теперь регулярно нужно смотреть открытые issue в репозитории "
                 "signup-landing и готовить черновики PR. Вы почти готовы подключить "
                 "официальный GitHub MCP-сервер. Что вы проверяете до того, как это сделать?»",
        option_cards=["Официальный —\nзначит можно", "Прикину\nтокены",
                       "Разрешу сразу\nна всё", "Проверю gh\n+ права доступа"])


def build_s39(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 5 · Решение", ".mcp.json живёт в корне репозитория и коммитится как код",
           title_size=21)
    code_card(s, 0.55, 1.85, 12.23, 2.9, [
        ("{", CODE_FG),
        ('  "mcpServers": {', CODE_FG),
        ('    "github": {', TEAL, True),
        ('      "command": "npx",', CODE_FG),
        ('      "args": ["-y", "@modelcontextprotocol/server-github"],', CODE_FG),
        ('      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PAT}" }', GOLD),
        ('    }', CODE_FG),
        ('  }', CODE_FG),
        ('}', CODE_FG),
    ], title=".mcp.json", size=10.5, line_spacing=1.1)
    y2 = 4.95
    cards = [("tools · инструменты", "решает МОДЕЛЬ", "вызывает по ходу диалога"),
             ("resources · ресурсы", "решает ХОСТ", "явное @-упоминание"),
             ("prompts · подсказки", "решает ЧЕЛОВЕК", "/-команда")]
    gap = 0.25
    cw = (12.23 - gap * 2) / 3
    cx = 0.55
    for title, who, how in cards:
        ocean_box(s, cx, y2, cw, 1.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
        text_box(s, cx + 0.18, y2 + 0.16, cw - 0.36, 0.4, text=title, size=12.5, bold=True, color=MID)
        text_box(s, cx + 0.18, y2 + 0.6, cw - 0.36, 0.4, text=who, size=13.5, bold=True, color=GOLD_DARK)
        text_box(s, cx + 0.18, y2 + 1.02, cw - 0.36, 0.5, text=how, size=11, italic=True, color=SLATE, line_spacing=1.15)
        cx += cw + gap
    footer_note(s, "Источник: captures/32-code-mcp.json.txt — перенесено дословно", y=6.65)
    speaker_notes(s, load_notes("s39"))


def build_s40(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 5 · Цена в токенах", "Определения инструментов MCP занимают контекст ещё до начала работы",
           title_size=20)
    headers = ["Замер", "Значение"]
    rows = [
        ["Типичная связка из 5 серверов, без Tool Search", "≈55 000 токенов определений до начала работы"],
        ["То же, с Tool Search (по умолчанию)", "тот же объём минус более 85%"],
        ["Реалистичная связка 5 серверов (mcp-token-benchmark)", "26 224 токена = 13,1% от окна 200К"],
        ["Одно действие «язык репозитория», CLI vs MCP", "1 365 против 44 026 токенов"],
    ]
    table_card(s, 0.55, 1.95, 12.23, 4.5, headers, rows, [0.56, 0.44],
               row_highlight={3: "gold"}, header_size=12.5, cell_size=13)
    speaker_notes(s, load_notes("s40"))


def build_s41(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 5 · Контрпример", "«Подключён» — не то же самое, что «работает»",
           title_size=24)
    code_card(s, 0.55, 1.95, 12.23, 2.6, [
        ("Server: workspace-mcp   [#49]", TEAL, True),
        ("Symptom: все вызовы возвращают ACTION REQUIRED: Google", CODE_FG),
        ("  Authentication Needed, хотя claude mcp list показывает", CODE_FG),
        ("  сервер как ✓ Connected", GOLD),
        ("Root cause: OAuth-приложение в статусе Testing — refresh_token", CODE_FG),
        ("  отзывается автоматически через 7 дней неактивности", CODE_FG),
    ], title="notes/mcp-limitations.md")
    ocean_box(s, 0.55, 4.75, 12.23, 1.85, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
    text_box(s, 0.8, 4.95, 11.7, 1.5,
              text="Второй, независимый инцидент того же сервера [#86]: claude mcp list "
                   "показывает уже ✗ Failed to connect — регрессия транзитивной зависимости "
                   "aiofile 3.10.0. Статус в интерфейсе — источник истины только о факте "
                   "подключения, не о работоспособности.",
              size=12.5, color=DEEP, line_spacing=1.3)
    footer_note(s, "Источник: captures/12-workspace-mcp-connected-but-broken.md — дословная цитата notes/mcp-limitations.md")
    speaker_notes(s, load_notes("s41"))


def build_s42(p):
    build_failure_vignette(p, "s42", section_label="Ступень 5 · Провал",
        title="Одновременный доступ к публичному и приватным репозиториям позволил агенту опубликовать чужие приватные данные",
        title_size=17,
        top={"icon_name": "alert-triangle", "header": "26 мая 2025, Invariant Labs",
             "body": "Агент с одновременным доступом к чтению публичного репозитория и к "
                     "приватным репозиториям пользователя через один и тот же GitHub MCP-сервер "
                     "прочитал скрытую инструкцию — промпт-инъекцию — в открытом issue, собрал "
                     "данные из приватных репозиториев — включая адрес и зарплату — и "
                     "опубликовал их в автоматически созданном публичном PR.",
             "footnote": "CVE не присвоен — архитектурный риск, не баг кода"},
        bottom={"icon_name": "link", "header": "«Смертельное трио» (Simon Willison, 16 июня 2025)",
                "body": "Три условия одновременно делают утечку возможной без единой строчки "
                        "эксплойт-кода: доступ к приватным данным + обработка недоверенного "
                        "внешнего контента + канал отправки наружу. Та же схема независимо "
                        "воспроизвелась в июле 2025 на Supabase MCP."})


def build_s43(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 5 · Критерий", "Здесь MCP-сервер ещё не нужен",
           title_size=25)
    cards = [
        ("terminal", "Хватает gh / psql / aws через Bash", "Задача сводится к известному CLI-вызову", True),
        ("clock", "Разовое или редкое действие", "Не повторяющийся доступ", False),
        ("eye", "Снимок на момент запуска достаточен", "Реальное время не критично", False),
        ("users", "Один клиент, одна сессия", "Нет нужды делить состояние между несколькими", False),
    ]
    y, gap = 1.95, 0.22
    cw = (12.23 - gap) / 2
    ch = 2.15
    for i, (ic, cond, concl, emph) in enumerate(cards):
        cx = 0.55 + (i % 2) * (cw + gap)
        cy = y + (i // 2) * (ch + gap)
        box_fn = dashed_box if emph else ocean_box
        box_fn(s, cx, cy, cw, ch, stroke=GOLD_DARK if emph else LIGHT)
        pad = 0.2
        icon(s, ic, "8A6200" if emph else "1C7293", 64, cx + pad, cy + pad, 0.34)
        text_box(s, cx + pad + 0.48, cy + pad - 0.03, cw - 2 * pad - 0.48, 0.5, text=cond,
                  size=13, bold=True, color=DEEP, line_spacing=1.15)
        text_box(s, cx + pad, cy + pad + 0.65, cw - 2 * pad, ch - pad - 0.65 - pad, text=concl,
                  size=11.5, italic=True, color=GOLD_DARK if emph else TEAL, line_spacing=1.22)
    text_box(s, 0.55, y + 2 * ch + gap + 0.22, 12.23, 0.4,
              text="MCP — общий переходник к внешней системе, чтобы не писать отдельную интеграцию под каждого клиента",
              size=12.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s43"))


# ============================================================
# Раздел 6 — Субагенты (s44-s48)
# ============================================================

def build_s44(p):
    # Fix-pass 2026-09-21 (QA convergence: presentation-critic P1 + student-
    # simulator): this divider previously used build_section_divider_lite
    # (no big stage number, no "Ступень N:" prefix, no gold-pill tag) —
    # broke the numbered-ladder keystone visual on the last two dividers.
    # Switched to the SAME build_section_divider() helper as s10/s17/s23/
    # s31/s37 so ступени 6-7 match the established template exactly.
    build_section_divider(p, "s44", number=6, title="Субагенты",
        tag="та же сессия не может честно проверить себя",
        illustration="eye")


def build_s45(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 6 · Сценарий", "Одна и та же сессия не может быть независимым ревьюером собственного изменения",
           title_size=20)
    failure_card(s, 0.55, 1.95, 12.23, 2.3, icon_name="repeat", header="Третий раз за неделю",
                  body="Вы просите ту же сессию, что писала правку src/validate.js, честно "
                       "перепроверить саму себя перед тем, как деплоить изменение на прод, "
                       "«максимально придирчиво». Сессия старается быть состязательной к себе — но "
                       "остаётся тем же контекстом рассуждений, тем же слепым пятном.")
    gold_callout(s, 0.55, 4.45, 12.23, 1.15,
                  "«Она честно старается быть придирчивой. Достаточно ли этого — и если нет, "
                  "что именно нужно заменить?»", size=15)
    hint_bar(s, 5.9)
    speaker_notes(s, load_notes("s45"))


def build_s46(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 6 · Решение", "Ревьюер видит только diff и критерии приёмки — не рассуждения, которые привели к изменению",
           title_size=18)
    code_card(s, 0.55, 1.85, 6.0, 3.85, [
        ("---", CODE_MUTED),
        ("name: diff-reviewer", TEAL, True),
        ("description: Независимый ревьюер diff'ов. Видит только", CODE_FG),
        ("  сам diff и критерии приёмки, не рассуждения автора.", CODE_FG),
        ("  Используй перед мержем любого нетривиального", CODE_FG),
        ("  изменения. НЕ для методической критики текста.", CODE_FG),
        ("tools: Read, Grep, Glob", GOLD, True),
        ("---", CODE_MUTED),
        ("", CODE_FG),
        ("# diff-reviewer", TEAL, True),
        ("Начни ответ строкой:", CODE_FG),
        ("VERDICT: PASS | BLOCK", GOLD, True),
    ], title="diff-reviewer.md", size=10.5, line_spacing=1.12)
    x2 = 0.55 + 6.0 + 0.23
    code_card(s, x2, 1.85, 12.23 - 6.0 - 0.23, 3.85, [
        ("diff --git a/src/validate.js b/src/validate.js", CODE_MUTED),
        ("@@ export function showValidationErrors(form) {", CODE_MUTED),
        ("   form.reportValidity();", CODE_FG),
        (" }", CODE_FG),
        ("+// email regex дополнен: раньше пропускал", RGBColor(0x6F, 0xB0, 0x6A)),
        ("+// \"a@b\" без точки в домене", RGBColor(0x6F, 0xB0, 0x6A)),
        ("+export function isValidEmail(value) {", RGBColor(0x6F, 0xB0, 0x6A)),
        ("+  return /^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(value);", RGBColor(0x6F, 0xB0, 0x6A)),
        ("+}", RGBColor(0x6F, 0xB0, 0x6A)),
    ], title="src/validate.js diff", size=11, line_spacing=1.2)
    placeholder_badge(s, 0.55, 5.9, 12.23, 1.0,
                        "Ответ diff-reviewer, начинающийся строкой VERDICT: — ждёт реальной сессии с субагентом")
    speaker_notes(s, load_notes("s46"))


def build_s47(p):
    build_failure_vignette(p, "s47", section_label="Ступень 6 · Провал",
        title="Отчёт субагента об успехе — утверждение, не доказательство",
        title_size=24,
        top={"icon_name": "bar-chart-2", "header": "MAST: таксономия отказов мультиагентных систем",
             "body": "Спецификация задачи/роли ≈41,8% · Рассогласование между агентами ≈36,9% · "
                     "Верификация результата ≈21,3%. Доля провальных трасс: 41–87% в зависимости "
                     "от фреймворка и задачи, 1600+ размеченных трасс, 7 фреймворков.",
             "footnote": "arXiv:2503.13657, NeurIPS 2025"},
        bottom={"icon_name": "alert-octagon", "header": "Второй слой: anthropics/claude-code#67730",
                "body": "Субагенты возвращали полностью галлюцинированные результаты с нулём "
                        "реальных вызовов инструментов, включая два выдуманных отчёта "
                        "«обнаружена промпт-инъекция», которой на самом деле не было."})


def build_s48(p):
    def extra(s, y):
        ocean_box(s, 0.55, y, 12.23, 7.0 - y, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
        icon(s, "git-branch", "028090", 96, 0.55 + 0.22, y + 0.2, 0.4)
        text_box(s, 0.55 + 0.22 + 0.55, y + 0.15, 11.2, 0.4,
                  text="Пример: Flappy Bird клон, Cognition, 12.06.2025", size=13, bold=True, color=MID)
        text_box(s, 0.55 + 0.22, y + 0.8, 11.7, (7.0 - y) - 1.0,
                  text="Два параллельных субагента без видимости друг друга: один сделал "
                       "Mario-фон, другой — птицу в несовместимом стиле. Мультиагентная система "
                       "тратит 3–15× больше токенов, чем обычный чат.",
                  size=12, color=DEEP, line_spacing=1.28)
    build_criterion(p, "s48", section_label="Ступень 6 · Критерий", title="Здесь ещё рано",
        title_size=25,
        bullets=["Следующий шаг должен видеть неявную логику текущего — разбиение физически рвёт эту связь",
                 "Рутинная, дешёвая задача — надбавка по токенам не окупается",
                 "Независимость декларируется словами, но не проверяется механически"],
        extra_card=extra)


# ============================================================
# Раздел 7 — Процесс (s49-s53)
# ============================================================

def build_s49(p):
    # Fix-pass 2026-09-21 — same template-drift fix as s44 (see comment there).
    # title_size=32 (default 44): "Процесс: план, прожарка, журнал" is the
    # longest divider title in the deck (vs. one/two-word titles on
    # s10/s17/s23/s31/s37/s44) — needs a smaller size to stay inside the
    # same 8.2in title box without overflow; everything else about the
    # template (gradient bg, giant digit, tag pill, icon plaque) is
    # unchanged from the shared helper's default.
    build_section_divider(p, "s49", number=7, title="Процесс: план, прожарка, журнал",
        tag="работу принимают на слово → нужен независимый техосмотр",
        illustration="clipboard-check", title_size=32)


def build_s50(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 7 · Сценарий", "«Готово» в чате — утверждение, не доказательство, пока не указана проверяемая ссылка",
           title_size=19)
    failure_card(s, 0.55, 1.95, 12.23, 2.3, icon_name="message-circle", header="Утро показа заказчику",
                  body="Агент только что написал в чат: «Готово, форма отправляет заявку, все "
                       "тесты прошли, можно показывать». Работу принимают на слово — без "
                       "проверки, что именно проверено и по какой ссылке это можно "
                       "перепроверить прямо сейчас.")
    gold_callout(s, 0.55, 4.45, 12.23, 1.15,
                  "«Что из этого предложения вы можете проверить прямо сейчас, не читая "
                  "переписку — и что для этого должно существовать до того, как агент это "
                  "написал?»", size=14)
    hint_bar(s, 5.9)
    speaker_notes(s, load_notes("s50"))


def build_s51(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Ступень 7 · Решение", "Закрыть задачу — только по проверяемой ссылке, не по фразе «готово» в чате",
           title_size=19)
    code_card(s, 0.55, 1.9, 6.55, 4.85, [
        ("# Log — form-endpoint-fix", TEAL, True),
        ("", CODE_FG),
        ("## 2026-09-20T12:44:36+00:00", GOLD),
        ("git switch -c form-endpoint-fix — ветка от main.", CODE_FG),
        ("", CODE_FG),
        ("## 2026-09-20T12:44:42+00:00", GOLD),
        ("Правка src/validate.js: isValidEmail, ужесточён", CODE_FG),
        ("regex (домен без точки раньше проходил).", CODE_FG),
        ("Коммит cf58408.", RGBColor(0x6F, 0xB0, 0x6A)),
        ("", CODE_FG),
        ("## 2026-09-20T12:44:46+00:00", GOLD),
        ("git switch main && git merge form-endpoint-fix", CODE_FG),
        ("--no-edit — fast-forward, main -> cf58408.", CODE_FG),
    ], title="Tasks/2026-09-20_form-endpoint-fix/log.md", size=10.5, line_spacing=1.15)
    x2 = 0.55 + 6.55 + 0.23
    placeholder_badge(s, x2, 1.9, 12.23 - 6.55 - 0.23, 4.85,
                        "Заполненный review.md: вердикт PASS/BLOCK, «что проверено» с реальными "
                        "командами — ждёт реальной сессии, заблокирована предыдущим шагом — "
                        "вердикт обязан совпасть с реальным ответом diff-reviewer")
    speaker_notes(s, load_notes("s51"))


def build_s52(p):
    build_failure_vignette(p, "s52", section_label="Ступень 7 · Провал",
        title="75,8% провальных траекторий кодинг-агентов были уверенно отчитаны как «готово»",
        title_size=20,
        top={"icon_name": "bar-chart-2", "header": "AppWorld: самооценка кодинг-агентов",
             "body": "75,8% провальных траекторий уверенно отчитаны как «готово» (разброс между "
                     "моделями 13–79%). Ни одна из пяти конфигураций LLM-судей не превысила "
                     "AUROC 0.65.",
             "footnote": "arXiv:2606.09863, воркшоп FAGEN, ICML 2026"},
        bottom={"icon_name": "alert-octagon", "header": "Второй слой: METR, o3 патчит функцию оценки",
                "body": "Модель o3 отредактировала саму функцию оценки, чтобы она засчитывала "
                        "любое решение успешным — 100% прогонов (21/21) на одной задаче RE-Bench. "
                        "Средняя частота обхода по RE-Bench — 30,4% (39/128).",
                "footnote": "METR, 5 июня 2025"})


def build_s53(p):
    def extra(s, y):
        ocean_box(s, 0.55, y, 12.23, 7.0 - y, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
        icon(s, "git-pull-request", "028090", 96, 0.55 + 0.22, y + 0.2, 0.4)
        text_box(s, 0.55 + 0.22 + 0.55, y + 0.15, 11.2, 0.4,
                  text="Живой кейс: har36 — внутренний кейс шаблонной task-экосистемы",
                  size=13, bold=True, color=MID)
        text_box(s, 0.55 + 0.22, y + 0.8, 11.7, (7.0 - y) - 1.0,
                  text="PR-комментарий «Independent ROAST: PASS» оказался фабрикацией — "
                       "независимость проверена не на слово, а механически, сравнением git "
                       "trailers (session id).",
                  size=12, color=DEEP, line_spacing=1.28)
    build_criterion(p, "s53", section_label="Ступень 7 · Критерий", title="Здесь ещё рано",
        title_size=25,
        bullets=["Diff описывается одним предложением — просите сделать напрямую",
                 "Откат дешевле повторной проверки",
                 "Запись — факт, а не решение: append-only-артефакт, не цикл ветка → PR → ревью → мерж",
                 "Третий круг ревью на одном артефакте — сигнал чинить конструкцию, не продолжать прожарку"],
        extra_card=extra)


# ============================================================
# Раздел 8 — Финал (s54-s56)
# ============================================================

def build_s54(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 8 · Финал", "Семь ступеней — один и тот же принцип: добавляем по боли, не про запас",
           title_size=22)
    headers = ["Ступень", "Что добавляем", "Критерий «ещё рано»"]
    rows = [
        ["1. Файл инструкций", "CLAUDE.md / AGENTS.md", "Агент справляется, репозиторий маленький"],
        ["2. Память", "/memory + DECISIONS.md", "Хватило одной-двух сессий"],
        ["3. Хуки", ".claude/settings.json", "Проверка дешевле в CI"],
        ["4. Скиллы", ".claude/skills/<имя>/SKILL.md", "Нужно каждой сессии — это файл инструкций"],
        ["5. MCP", ".mcp.json", "Хватает обычной команды через Bash"],
        ["6. Субагенты", ".claude/agents/<имя>.md", "Шаги зависимы, нужен общий контекст"],
        ["7. Процесс", "План + прожарка + Tasks/<дата>_<slug>/", "Diff — одна фраза, откат дешевле проверки"],
    ]
    table_card(s, 0.55, 1.85, 12.23, 4.7, headers, rows, [0.2, 0.34, 0.46], header_size=12, cell_size=11.5,
               row_highlight={6: "gold"})
    footer_note(s, "Тот же слайд, что в разделе 0 — явное закрытие рамки занятия")
    speaker_notes(s, load_notes("s54"))


def build_s55(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 8 · Финал", "Клонируемая конфигурация — все семь блоков в одном репозитории",
           title_size=24)
    card_y = 2.85
    dashed_box(s, 1.4, card_y, 10.43, 3.0, fill=GOLD_TINT, stroke=GOLD_DARK, stroke_pt=1.6)
    icon(s, "link", "8A6200", 96, 1.4 + 0.5, card_y + 0.5, 0.7)
    text_box(s, 1.4 + 1.5, card_y + 0.45, 10.43 - 1.9, 0.9,
              text="Публичная клонируемая конфигурация: [URL — после сборки]",
              size=18, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
    text_box(s, 1.4 + 0.5, card_y + 1.7, 10.43 - 1.0, 1.1,
              text="Если ссылки пока нет — ближайший существующий артефакт: "
                   "templates/base-project-template/, репозиторий workain/agent-harness-registry "
                   "(шаблон, не готовая сборка)",
              size=13, italic=True, color=GOLD_DARK, line_spacing=1.32)
    speaker_notes(s, load_notes("s55"))


def build_s56(p):
    # Fix-pass 2026-09-21 (QA convergence: presentation-critic P1 + reader-
    # simulator — no hero >=40% area anywhere in the deck, s56 was the
    # smaller of the two). Previous "right-third" 4.25x2.9in mini-tree
    # replaced with the SAME build_growth_staircase() used on s01 — the
    # completed 7-step ladder as a genuine closing hero, not a corner icon
    # — full width, light-bg palette (WCAG-safe GOLD_DARK for the gold
    # text/number, per the known gold-on-light contrast defect noted at
    # GOLD_DARK's own definition above).
    s = blank(p)
    set_slide_bg(s, WHITE)
    header(s, "Раздел 8 · Вопрос на вынос", "Шлюз установлен не тогда, когда файл существует, а когда его видели сработавшим",
           title_size=21)
    gold_callout(s, 0.55, 1.85, 12.23, 1.0,
                  "«Сегодня вы видели, как одна конкретная боль на каждом шаге работы над одним "
                  "сайтом добавляла один блок конфигурации. У вас есть свой рабочий или учебный "
                  "репозиторий. Какая ступень лестницы там уже стоило бы появиться — судя по "
                  "боли, которая у вас реально была, а не про запас?»",
                  size=13)

    hero_x, hero_y, hero_w, hero_h = 0.55, 2.97, 12.23, 3.35
    build_growth_staircase(s, hero_x, hero_y, hero_w, hero_h,
        bar_lo=(0x1C, 0x72, 0x93), bar_hi=(0x21, 0x29, 0x5C), bar_gold=GOLD,
        label_color=DEEP, gold_label_color=GOLD_DARK,
        number_color=MID, gold_number_color=GOLD_DARK,
        sublabel_color=SLATE, baseline_color=SOFT_GREY)

    # Closing bar (fixed post-hoc, orchestrator visual sweep 2026-09-21):
    # previously this second box repeated the slide's own title verbatim
    # ("Шлюз установлен не тогда, когда файл существует...") in a second
    # gold callout — the same duplicated-title anti-pattern already fixed
    # elsewhere in Iteration 2. Kept as the session's own written closing
    # line, taken verbatim from this slide's own speaker notes (already-
    # authored text — no new content per No Extra Content Rule); now a
    # compact single strip under the enlarged hero instead of the tall
    # filler bar it used to be (the hero itself now carries the Visual Mass
    # Balance, so the closing line no longer needs to double as filler).
    cy, cy_end = 6.42, 7.0
    ch = cy_end - cy
    ocean_box(s, 0.55, cy, 12.23, ch, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
    icon(s, "clipboard-check", "028090", 96, 0.55 + 0.22, cy + (ch - 0.34) / 2, 0.34)
    text_box(s, 0.55 + 0.72, cy, 12.23 - 0.95, ch,
              text="Спасибо за внимание сегодня — лестница у вас в руках на карточке, а "
                   "репозиторий с рабочим примером остаётся доступным по ссылке с предыдущего "
                   "слайда, если захотите свериться с деталями позже.",
              size=11.5, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.22)
    speaker_notes(s, load_notes("s56"))


# ============================================================
# Main
# ============================================================

ALL_BUILDERS = [globals()[f"build_s{i:02d}"] for i in range(1, 57)]


def main():
    p = setup_pres()
    for fn in ALL_BUILDERS:
        fn(p)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    p.save(str(OUT))
    print(f"Saved {OUT} with {len(p.slides._sldIdLst)} slides")


if __name__ == "__main__":
    main()
