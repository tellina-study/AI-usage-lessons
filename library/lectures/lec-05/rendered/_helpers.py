"""
Shared build helpers for Лекция 5 «AI-продукт: полный жизненный цикл»
(50 slides s01-s49 + s13a, 6-section product-loop roadmap).

Ported from the proven lec-04 _helpers.py (issue #170), adapted for the lec-05
worktree path + 6-section loop roadmap (Discovery/Design/Build-Launch/Measure/
Support/Governance) + lec-05 URL registry.

Palette LOCKED: Ocean Gradient (#21295C / #065A82 / #1C7293) + Teal (#028090)
secondary + Gold (#F0AB00) ≥1×/slide. Motif «Ocean rounded box»
(radius 12, surface #F4F7FA, stroke #1C7293 1.5pt) на каждом content-слайде.

Canvas 13.333" × 7.5" (16:9). Fonts fall back to DejaVu (Cyrillic OK).

Issue #189 · Branch: hc/pldlc-lesson5-c5cc1586
"""
import re
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt
from lxml import etree
from PIL import Image

# === Palette (LOCKED) ===
DEEP    = RGBColor(0x21, 0x29, 0x5C)
MID     = RGBColor(0x06, 0x5A, 0x82)
LIGHT   = RGBColor(0x1C, 0x72, 0x93)
TEAL    = RGBColor(0x02, 0x80, 0x90)
SURFACE = RGBColor(0xF4, 0xF7, 0xFA)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
GOLD    = RGBColor(0xF0, 0xAB, 0x00)
SLATE   = RGBColor(0x5B, 0x66, 0x78)
COVER_OUTLINE = RGBColor(0xD9, 0xE2, 0xEC)
GOLD_TINT = RGBColor(0xFD, 0xF3, 0xDC)
TEAL_TINT = RGBColor(0xE4, 0xF1, 0xF2)
SOFT_GREY = RGBColor(0xE5, 0xEA, 0xF0)
MID_TINT  = RGBColor(0xE1, 0xEA, 0xF0)

# === Constants ===
SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5
ROOT = Path(__file__).resolve().parents[1]      # library/lectures/lec-05
ASSETS = ROOT / "rendered/assets"
ICONS = ASSETS / "icons"
CHARTS = ASSETS / "charts"
SLIDES_DIR = ROOT / "slides"
FONT_HEAD = "DejaVu Sans"
FONT_BODY = "DejaVu Sans"
FONT_MONO = "DejaVu Sans Mono"


# ============================================================
# lec-05: no heavy clickable-URL registry (lec-04 pattern) — this deck uses
# simple inline muted source captions via src() at the point of the claim,
# sourced from each slide's `source:` frontmatter. Kept simple by design.
# ============================================================
URLS = {}


def refs_of(slide, keys, y=6.70, **kw):
    """Unused in lec-05 (kept for signature compat with ported code)."""
    return None

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


# ============================================================
# ПРАВКА 2 (owner refinement) — [N] reference markers "существенно
# меньше" основного текста. After a text frame is built, walk its runs,
# find [N] / [N, M] substrings, and re-split them into a smaller (~52%),
# superscript, muted-colour run. Applied automatically by text_box /
# text_runs / gold_callout / teal_callout so the many baked-in [N] markers
# shrink without rewriting every call site. Bottom ref-lists опускают это
# (они и так мелкие).
# ============================================================
_REF_RE = re.compile(r'\[\d+(?:\s*[,–—-]\s*\d+)*\]')
_AMAIN = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def _run_props(src_run):
    """Read the font props we need to clone from an existing run."""
    f = src_run.font
    sz = f.size
    return {
        "name": f.name,
        "size_pt": (sz.pt if sz is not None else None),
        "bold": f.bold,
        "italic": f.italic,
        "color": (f.color.rgb if (f.color and f.color.type is not None) else None),
    }


def _clone_run_after(anchor_r, props, text, *, ref=False,
                     ref_frac=0.52, ref_color=LIGHT):
    """Insert a new <a:r> right after anchor_r with cloned props (or a
    small superscript muted variant when ref=True)."""
    new_r = etree.SubElement(anchor_r.getparent(), _AMAIN + "r")
    anchor_r.addnext(new_r)
    rpr = etree.SubElement(new_r, _AMAIN + "rPr")
    base = props["size_pt"] or 16.0
    if ref:
        rpr.set("sz", str(int(round(base * ref_frac * 100))))
        rpr.set("baseline", "30000")
        rpr.set("b", "0")
        rpr.set("i", "1")
    else:
        if props["size_pt"] is not None:
            rpr.set("sz", str(int(round(base * 100))))
        if props["bold"] is not None:
            rpr.set("b", "1" if props["bold"] else "0")
        if props["italic"] is not None:
            rpr.set("i", "1" if props["italic"] else "0")
    # font
    if props["name"]:
        for tag in ("latin", "cs", "ea"):
            el = etree.SubElement(rpr, _AMAIN + tag)
            el.set("typeface", props["name"])
    # colour
    col = ref_color if ref else props["color"]
    if col is not None:
        fill = etree.SubElement(rpr, _AMAIN + "solidFill")
        clr = etree.SubElement(fill, _AMAIN + "srgbClr")
        clr.set("val", str(col))
    t = etree.SubElement(new_r, _AMAIN + "t")
    t.text = text
    return new_r


def shrink_refs_in_frame(text_frame, *, ref_frac=0.52, ref_color=LIGHT):
    """Split every [N] marker inside the frame into a small superscript
    muted run. Non-destructive to surrounding text formatting."""
    for para in text_frame.paragraphs:
        # snapshot runs (we mutate the tree while iterating)
        for run in list(para.runs):
            txt = run.text
            if not txt or "[" not in txt:
                continue
            matches = list(_REF_RE.finditer(txt))
            if not matches:
                continue
            props = _run_props(run)
            # first chunk stays in the original run
            run.text = txt[:matches[0].start()]
            anchor = run._r
            pos = matches[0].start()
            for i, m in enumerate(matches):
                # the marker itself (small)
                anchor = _clone_run_after(anchor, props, m.group(),
                                          ref=True, ref_frac=ref_frac,
                                          ref_color=ref_color)
                # the text between this marker and the next (normal)
                nxt = matches[i + 1].start() if i + 1 < len(matches) else len(txt)
                between = txt[m.end():nxt]
                if between:
                    anchor = _clone_run_after(anchor, props, between, ref=False)
                pos = nxt
    return text_frame


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
    # support \n as hard paragraph breaks (#sem01-render-1 workaround)
    lines = text.split("\n")
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    for i, line in enumerate(lines):
        if i > 0:
            p = tf.add_paragraph()
            p.alignment = align
            p.line_spacing = line_spacing
        r = p.add_run()
        r.text = line
        r.font.name = font; r.font.size = Pt(size)
        r.font.bold = bold; r.font.italic = italic
        r.font.color.rgb = color
    shrink_refs_in_frame(tf)
    return tb


def text_runs(slide, x, y, w, h, runs, *,
              align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
              line_spacing=1.15, font=FONT_BODY):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    for cfg in runs:
        if cfg.get("newpara"):
            p = tf.add_paragraph()
            p.alignment = cfg.get("align", align)
            p.line_spacing = cfg.get("line_spacing", line_spacing)
            if cfg.get("space_before") is not None:
                p.space_before = Pt(cfg["space_before"])
        r = p.add_run()
        r.text = cfg["text"]
        r.font.name = cfg.get("font", font)
        r.font.size = Pt(cfg.get("size", 16))
        r.font.bold = cfg.get("bold", False)
        r.font.italic = cfg.get("italic", False)
        r.font.color.rgb = cfg.get("color", DEEP)
    shrink_refs_in_frame(tf)
    return tb


def ocean_box(slide, x, y, w, h, *, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5,
              radius_pt=12.0):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    try:
        adj = max(0.035, min(0.22, (radius_pt / 72.0) / max(min(w, h) / 2.0, 0.5)))
        shp.adjustments[0] = adj
    except Exception:
        pass
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    shp.line.color.rgb = stroke; shp.line.width = Pt(stroke_pt)
    disable_shadow(shp)
    return shp


def filled_rect(slide, x, y, w, h, fill, *, stroke=None, stroke_pt=0.0,
                radius=False, radius_adj=0.16):
    st = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shp = slide.shapes.add_shape(st, Inches(x), Inches(y), Inches(w), Inches(h))
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


def right_arrow(slide, x, y, w, h, fill=MID, stroke=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(1.0)
    disable_shadow(shp)
    return shp


def circle(slide, x, y, d, fill, *, stroke=None, stroke_pt=1.0):
    shp = slide.shapes.add_shape(MSO_SHAPE.OVAL,
                                 Inches(x), Inches(y), Inches(d), Inches(d))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(stroke_pt)
    disable_shadow(shp)
    return shp


def chip(slide, x, y, w, h, text, *, fill=MID, stroke=None, color=WHITE,
         size=13, bold=True):
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
    tf.margin_top = Inches(0.02); tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.word_wrap = False
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = text
    r.font.name = FONT_BODY; r.font.size = Pt(size)
    r.font.bold = bold; r.font.color.rgb = color
    disable_shadow(shp)
    return shp


def connector(slide, x1, y1, x2, y2, color=LIGHT, width=2.0, dash=None,
              arrow_end=False, arrow_len="med", arrow_w="med"):
    """arrow_end=True adds a tailEnd arrowhead at (x2,y2) — used for
    schema_cycle diagrams that need an explicit read direction (e.g. s03
    GATE-B fix: the loop nodes had connecting lines but no arrowheads, so a
    student could not tell the ring had a direction of travel)."""
    cn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                                    Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    cn.line.color.rgb = color
    cn.line.width = Pt(width)
    if dash:
        ln = cn.line._get_or_add_ln()
        pd = etree.SubElement(
            ln, "{http://schemas.openxmlformats.org/drawingml/2006/main}prstDash")
        pd.set("val", dash)
    if arrow_end:
        ln = cn.line._get_or_add_ln()
        tail = etree.SubElement(ln, _AMAIN + "tailEnd")
        tail.set("type", "triangle")
        tail.set("w", arrow_w)
        tail.set("len", arrow_len)
    return cn


def add_image(slide, path, x, y, w=None, h=None, preserve_aspect=True):
    """[#73-render-1] aspect-safe; [#156-1] fixed h-only branch."""
    path = Path(path)
    if not path.exists():
        return
    if preserve_aspect and w is not None and h is not None:
        try:
            img = Image.open(path); iw, ih = img.size; img.close()
        except Exception:
            slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                     width=Inches(w))
            return
        ir = iw / ih; br = w / h
        if ir > br:
            ah = w / ir
            slide.shapes.add_picture(str(path), Inches(x),
                                     Inches(y + (h - ah) / 2), width=Inches(w))
        else:
            aw = h * ir
            slide.shapes.add_picture(str(path), Inches(x + (w - aw) / 2),
                                     Inches(y), height=Inches(h))
    elif w is not None and h is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 width=Inches(w), height=Inches(h))
    elif w is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 width=Inches(w))
    elif h is not None:                          # [#156-1] fix
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 height=Inches(h))
    else:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y))


def slide_title(slide, text, *, y=0.40, h=0.92, w=12.25, x=0.55, size=26,
                color=DEEP, bold=True, line_spacing=1.10, align=PP_ALIGN.LEFT):
    text_box(slide, x=x, y=y, w=w, h=h, text=text,
             size=size, bold=bold, color=color, line_spacing=line_spacing,
             align=align)


def gold_callout(slide, x, y, w, h, text, *, size=15, bold=True,
                 color=DEEP, align=PP_ALIGN.LEFT, stroke_pt=1.5):
    filled_rect(slide, x, y, w, h, GOLD_TINT, stroke=GOLD, stroke_pt=stroke_pt,
                radius=True, radius_adj=0.10)
    text_box(slide, x=x + 0.24, y=y + 0.06, w=w - 0.48, h=h - 0.12, text=text,
             size=size, bold=bold, color=color, anchor=MSO_ANCHOR.MIDDLE,
             align=align, line_spacing=1.20)


def teal_callout(slide, x, y, w, h, text, *, size=14, bold=False,
                 color=DEEP, align=PP_ALIGN.LEFT):
    filled_rect(slide, x, y, w, h, TEAL_TINT, stroke=TEAL, stroke_pt=1.5,
                radius=True, radius_adj=0.10)
    text_box(slide, x=x + 0.24, y=y + 0.06, w=w - 0.48, h=h - 0.12, text=text,
             size=size, bold=bold, color=color, anchor=MSO_ANCHOR.MIDDLE,
             align=align, line_spacing=1.18)


def footer(slide, text):
    text_box(slide, x=0.55, y=7.04, w=12.25, h=0.34, text=text,
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.LEFT,
             line_spacing=1.0)


def src(slide, x, y, w, text, *, size=9, color=LIGHT, align=PP_ALIGN.LEFT,
        h=0.22):
    """Inline muted source caption placed RIGHT AT the material it backs
    (definition / claim / recommendation), not in a bottom footer.
    Small, italic, muted — reads as attribution, not body."""
    text_box(slide, x=x, y=y, w=w, h=h, text=text,
             size=size, italic=True, color=color, align=align,
             line_spacing=1.0)


def icon(slide, name, x, y, size, variant="mid"):
    add_image(slide, ICONS / f"{name}-{variant}.png", x, y, size, size)


MEMES = ASSETS / "memes"
SCR = ASSETS / "screenshots"


def meme_in_box(slide, fname, x, y, w, h, *, pad=0.10):
    """Frame a meme (assets/memes/<fname>) inside an Ocean rounded box —
    on-brand container so the raw meme never floats. Aspect-preserved."""
    ocean_box(slide, x, y, w, h, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    add_image(slide, MEMES / fname, x + pad, y + pad, w - 2 * pad, h - 2 * pad,
              preserve_aspect=True)


def photo_in_box(slide, fname, x, y, w, h, *, pad=0.10, fill=WHITE):
    """Frame a real photo/logo (assets/screenshots/<fname>) in an Ocean box.
    NO attribution caption burned on-slide (owner rule); source lives in the
    .url sidecar + iteration-log only."""
    ocean_box(slide, x, y, w, h, fill=fill, stroke=LIGHT, stroke_pt=1.5)
    add_image(slide, SCR / fname, x + pad, y + pad, w - 2 * pad, h - 2 * pad,
              preserve_aspect=True)


def eli5_overview(p, sid, *, title, cards, icon_name, icon_variant="mid"):
    """«Для чайников» section-overview slide (Directive 3): big left icon +
    3 plain-language cards (Что это / Зачем / Ментальная модель). Dual-audience:
    plain for weaker students, skimmable for the strong majority. Gold accent on
    the first card's label + a gold chip «простыми словами»."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, title, size=26, w=12.0, h=0.85)
    # left hero icon in a soft tile
    filled_rect(s, 0.55, 1.70, 2.75, 3.95, SURFACE, stroke=LIGHT, stroke_pt=1.5,
                radius=True, radius_adj=0.06)
    icon(s, icon_name, 1.35, 2.55, 1.15, icon_variant)
    chip(s, 0.85, 4.55, 2.15, 0.44, "простыми словами", fill=GOLD, color=DEEP,
         size=11.5)
    # 3 cards on the right
    cx, cw = 3.65, 9.15
    ch, gap = 1.18, 0.20
    y0 = 1.70
    for i, (label, body) in enumerate(cards):
        y = y0 + i * (ch + gap)
        lab_col = GOLD if i == 0 else MID
        ocean_box(s, cx, y, cw, ch, fill=SURFACE, stroke=LIGHT, stroke_pt=1.4)
        text_box(s, x=cx + 0.28, y=y + 0.13, w=cw - 0.56, h=0.32, text=label,
                 size=14, bold=True, color=lab_col)
        text_box(s, x=cx + 0.28, y=y + 0.48, w=cw - 0.56, h=ch - 0.58,
                 text=body, size=12.5, color=DEEP, line_spacing=1.12)
    notes_with_sources(s, sid)
    return s


# ============================================================
# ПРАВКА 1 (#269 + #266a) — numbered reference system
# Compact [N] markers at the claim + a small muted CLICKABLE numbered
# source list at the bottom of the slide. URLs come ONLY from the research
# URL map (references-and-req-engineering.md, Deliverable 2).
# ============================================================
def ref_list(slide, entries, *, y=6.70, x=0.55, w=12.25, h=0.60,
             size=8.5, color=LIGHT, line_spacing=1.02, cols=None):
    """Bottom numbered clickable source list.

    entries: list of (num:str, name:str, url:str). Renders «[N] name»
    where name is a clickable hyperlink (run.hyperlink.address = url).
    Muted, italic, small — reads as attribution, never a text-wall.
    Kept to 1–2 visual lines; entries are separated by «   ·   ».
    """
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    p.line_spacing = line_spacing
    for i, (num, name, url) in enumerate(entries):
        # marker [N]
        rm = p.add_run()
        rm.text = f"[{num}] "
        rm.font.name = FONT_BODY; rm.font.size = Pt(size)
        rm.font.bold = True; rm.font.italic = True
        rm.font.color.rgb = MID
        # clickable name
        rn = p.add_run()
        rn.text = name
        rn.font.name = FONT_BODY; rn.font.size = Pt(size)
        rn.font.italic = True
        rn.font.color.rgb = color
        if url:
            try:
                rn.hyperlink.address = url
            except Exception:
                pass
        # separator
        if i < len(entries) - 1:
            rs = p.add_run()
            rs.text = "   ·   "
            rs.font.name = FONT_BODY; rs.font.size = Pt(size)
            rs.font.italic = True
            rs.font.color.rgb = color
    return tb


def link_run(paragraph, text, url, *, size=11, color=MID, bold=False,
             italic=False, font=FONT_BODY):
    """Add a single clickable run to an existing paragraph."""
    r = paragraph.add_run()
    r.text = text
    r.font.name = font; r.font.size = Pt(size)
    r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color
    if url:
        try:
            r.hyperlink.address = url
        except Exception:
            pass
    return r


def page_number(slide, n, total=None, *, color=SLATE):
    """Small muted page-number stamp in the bottom-right corner.

    Placed at the very bottom-right (x≈12.55, y≈7.16), 10pt italic muted, so it
    never overlaps the left-aligned footer / ref-list (x=0.55) nor the roadmap
    bar (ends y≈7.13). Format «N / TOTAL» when total is given, else «N».
    Applied to every slide by the assembler (build_lec04_v4.py) so all 41
    slides carry it without touching per-slide builders."""
    txt = f"{n} / {total}" if total else str(n)
    tb = slide.shapes.add_textbox(Inches(12.33), Inches(7.16), Inches(0.95),
                                  Inches(0.28))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    p.line_spacing = 1.0
    r = p.add_run()
    r.text = txt
    r.font.name = FONT_BODY
    r.font.size = Pt(10)
    r.font.italic = True
    r.font.color.rgb = color
    return tb


def speaker_notes(slide, text):
    """Write notes as readable PARAGRAPHS (ПРАВКА 1, owner refinement):
    split on blank lines → one notes-paragraph each, so notes are never a
    single wall of text."""
    tf = slide.notes_slide.notes_text_frame
    tf.clear()
    # normalise: collapse single newlines inside a paragraph to spaces,
    # split into paragraphs on blank lines.
    blocks = [b.strip() for b in re.split(r'\n\s*\n', text.strip()) if b.strip()]
    if not blocks:
        blocks = [""]
    for i, block in enumerate(blocks):
        # keep intentional hard line breaks inside a "Источники:" block
        if block.lstrip().startswith("Источники:"):
            lines = [ln.rstrip() for ln in block.split("\n")]
            para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            para.text = lines[0]
            for ln in lines[1:]:
                sub = tf.add_paragraph()
                sub.text = ln
            continue
        one = re.sub(r'\s*\n\s*', ' ', block)
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.text = one


def load_notes(slide_id):
    files = list(SLIDES_DIR.glob(f"{slide_id}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding="utf-8")
    m = re.search(r'## Speaker notes\s*\n(.*?)(?=\n## |\n---\s*\n## |\Z)',
                  md, re.DOTALL)
    notes = m.group(1).strip() if m else ""
    notes = re.sub(r'\n+---\s*$', '', notes)
    return notes.strip()


# ============================================================
# lec-05 source handling: SIMPLE — no clickable [N] registry. Each slide's
# `source:` frontmatter (if present) is surfaced as a small muted inline
# caption via src() near the relevant claim (owner rule: no attribution
# LABELS on images, but textual source captions for stats/claims are fine
# and required by fact-integrity). notes_with_sources() reduces to plain
# speaker_notes(load_notes(sid)) plus, if the frontmatter has `source:`,
# one small "Источник:" line appended so the lecturer has it without it
# ever appearing on the visible slide body.
# ============================================================
def _frontmatter_source(sid):
    files = list(SLIDES_DIR.glob(f"{sid}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding="utf-8")
    m = re.search(r'^source:\s*"?(.+?)"?\s*$', md, re.MULTILINE)
    if not m:
        return ""
    line = m.group(1).strip()
    # strip internal-only markers — [FACT-CHECK] / [VFY-day-of] etc. are
    # frontmatter-only bookkeeping tags, NOT allowed in speaker notes body
    # (owner rule: 0 hits in visible body + speaker_notes).
    line = re.sub(r'\s*\[[A-Z-]+(?:-day-of)?\]\s*', ' ', line).strip()
    return line


def refs_of_slide(slide, sid, *, y=None, size=8.5):
    """No-op in lec-05 (no clickable bottom ref-list); kept for call-site
    compatibility with the ported lec-04 slide-builder pattern."""
    return None


def notes_with_sources(slide, sid):
    """Speaker notes + a plain 'Источник:' line from frontmatter, if any."""
    body = load_notes(sid)
    src_line = _frontmatter_source(sid)
    text = f"{body}\n\nИсточник: {src_line}" if src_line else body
    speaker_notes(slide, text)



# ============================================================
# Section divider — unified template (7-card roadmap, gold current)
# Sections of Лекции 5 (product loop): 0..6.
# ============================================================
NAV = [
    ("0", "Введение"),
    ("1", "Исследование"),
    ("2", "Дизайн"),
    ("3", "Сборка и запуск"),
    ("4", "Измерение"),
    ("5", "Поддержка"),
    ("6", "Управление"),
]


def roadmap_bar(slide, here_idx, *, y=6.55):
    """7-card progress bar; current section gold-bordered."""
    n = len(NAV)
    gap = 0.10
    bx = 0.55
    total_w = 12.25
    cw = (total_w - gap * (n - 1)) / n
    ch = 0.58
    for i, (num, label) in enumerate(NAV):
        x = bx + i * (cw + gap)
        cur = (i == here_idx)
        if cur:
            filled_rect(slide, x, y, cw, ch, GOLD_TINT, stroke=GOLD,
                        stroke_pt=2.0, radius=True, radius_adj=0.12)
        else:
            filled_rect(slide, x, y, cw, ch, SURFACE, stroke=SOFT_GREY,
                        stroke_pt=1.0, radius=True, radius_adj=0.12)
        text_box(slide, x=x + 0.02, y=y + 0.05, w=cw - 0.04, h=0.18,
                 text=num, size=10.5, bold=True,
                 color=(DEEP if cur else LIGHT), align=PP_ALIGN.CENTER)
        # longer RU labels need a smaller size + tight wrap to fit 2 lines
        lbl_sz = 8.0 if len(label) > 9 else 9.0
        text_box(slide, x=x + 0.02, y=y + 0.25, w=cw - 0.04, h=0.30,
                 text=label, size=lbl_sz, bold=cur,
                 color=(DEEP if cur else SLATE), align=PP_ALIGN.CENTER,
                 line_spacing=0.92)


def build_section_divider(p, here_idx, subtitle, bridge, sid, tag=None,
                          icon_name=None, meme_name=None):
    """Distinct divider (NO ocean motif): giant decorative section digit on
    the right (soft outline), РАЗДЕЛ N + subtitle + 1-line narrative bridge on
    the left, gold-current roadmap bar at bottom.

    lec-05: `tag` is a short content-tag (e.g. "2 базы · 3 провала" — counts,
    NEVER minutes — see No-Timing-No-Methodology rule) rendered as a gold chip
    under the subtitle. `meme_name` (Directive 2) frames THIS divider's own
    evergreen meme (imgflip template + RU caption) on the right, replacing the
    plain giant digit as the hero. `icon_name` fallback if no meme."""
    s = blank(p)
    set_slide_bg(s, SURFACE)
    if meme_name:
        # meme is the right-side hero, framed in an Ocean box; small ghost digit
        text_box(s, x=10.35, y=0.10, w=2.9, h=1.3, text=str(here_idx),
                 size=90, bold=True, color=COVER_OUTLINE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        meme_in_box(s, meme_name, 8.35, 1.35, 4.45, 4.55, pad=0.14)
    else:
        text_box(s, x=8.55, y=0.20, w=4.5, h=5.8, text=str(here_idx),
                 size=400, bold=True, color=COVER_OUTLINE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.0)
        if icon_name:
            icon(s, icon_name, 9.55, 1.35, 1.6, "light")
    text_box(s, x=0.75, y=1.55, w=7.3, h=0.55,
             text=f"РАЗДЕЛ {here_idx}", size=20, bold=True, color=TEAL)
    # GATE-B fix: removed the decorative gold accent-line under "РАЗДЕЛ N"
    # (named course anti-pattern — decorative underline, no semantic value).
    # The subtitle now simply follows with a bit more top space; the gold
    # chip/tag below still carries this divider's ≥1x gold requirement.
    text_box(s, x=0.75, y=2.62, w=7.3, h=1.75, text=subtitle,
             size=30, bold=True, color=DEEP, line_spacing=1.08)
    if tag:
        chip(s, 0.78, 4.20, 3.6, 0.42, tag, fill=GOLD, color=DEEP, size=12.5)
    text_box(s, x=0.78, y=4.80, w=7.35, h=1.55, text=bridge,
             size=15, italic=True, color=LIGHT, line_spacing=1.16)
    roadmap_bar(s, here_idx, y=6.55)
    notes_with_sources(s, sid)
    return s
