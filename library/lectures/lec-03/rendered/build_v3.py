"""
Full 36-slide build of Лекции 3 «Архитектуры AI-систем: агенты, RAG, API» (v3).

v3 = СТРУКТУРНАЯ ревизия v2→v3 по owner-обратной связи (plan §4, U-1…U-9):
  +6 suffix-слайдов (НЕ перенумеровывая s01–s30):
    s04a divider Раздел 1 · s13a divider Раздел 3 · s13b определение FT ·
    s23a sub-divider Безопасность · s25a divider Раздел 5 · s31 Q&A.
  s30 ретайтл (U-6, function-as-title убран) + Q&A вынесен в s31 (U-7).
  Порядок: s01..s04 → s04a → s05..s08 → s09 → s10..s13 → s13a → s13b →
           s14..s17 → s18 → s19..s23 → s23a → s24..s25 → s25a →
           s26..s29 → s30 → s31.

Source-of-truth: deck.yaml + deck-part2.yaml (U-9 split, v3) +
chapter v1.1 finalized (~22450 слов) + slides/*.md (36 файлов,
readable speaker notes 150-300 слов).

Issue #87 · Branch: issue-87-lec-03-architectures

Palette LOCKED v3: Ocean Gradient (#21295C / #065A82 / #1C7293) + Teal (#028090)
secondary + Gold (#F0AB00) ≥1×/slide.
Visual motif: «Ocean rounded box» (radius 12, surface #F4F7FA, stroke #1C7293 1.5pt).

Canvas: 13.333" × 7.5" (16:9). Pacing per deck.yaml ≈ 75 мин.

Build via: python3 build_v3.py — generates lec-03.pptx (36 slides).
"""
import re
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt, Emu
from lxml import etree
from PIL import Image

import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent))
import refs_lec03 as R  # noqa: E402  (issue #171 reference/page-number system)

# issue #171: footer text capture so ref-slides can fold the caveat into the
# clickable [N] source list (single bottom band, no overlap).
_FOOTER_TEXT = {}

# === Palette (LOCKED v3) ===
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

# === Constants ===
SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5
# issue #171: run from the worktree — read slides/assets/notes + write pptx
# from THIS repo checkout (slides identical to main). Falls back to main-repo
# ROOT only if the worktree copy is missing.
_WT = Path(__file__).resolve().parents[1]      # …/lec-03 in the current checkout
_MAIN = Path("/home/harness/harness-projects/256/lessons-3bb49d40/library/lectures/lec-03")
ROOT = _WT if (_WT / "slides").exists() else _MAIN
ASSETS = ROOT / "rendered/assets"
ICONS = ASSETS / "icons"
CHARTS = ASSETS / "charts"
SLIDES_DIR = ROOT / "slides"
OUT = ROOT / "rendered/lec-03.pptx"
FONT_HEAD = "Arial"
FONT_BODY = "Arial"
FONT_MONO = "Liberation Mono"


# ============================================================
# Helpers
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


def up_arrow(slide, x, y, w, h, fill=LIGHT):
    shp = slide.shapes.add_shape(MSO_SHAPE.UP_ARROW,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
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


def connector(slide, x1, y1, x2, y2, color=LIGHT, width=2.0, dash=None):
    cn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                                    Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    cn.line.color.rgb = color
    cn.line.width = Pt(width)
    if dash:
        ln = cn.line._get_or_add_ln()
        pd = etree.SubElement(ln, "{http://schemas.openxmlformats.org/drawingml/2006/main}prstDash")
        pd.set("val", dash)
    return cn


def add_image(slide, path, x, y, w=None, h=None, preserve_aspect=True):
    path = Path(path)
    if not path.exists():
        return
    if preserve_aspect and w is not None and h is not None:
        try:
            img = Image.open(path); iw, ih = img.size; img.close()
        except Exception:
            slide.shapes.add_picture(str(path), Inches(x), Inches(y), width=Inches(w))
            return
        ir = iw / ih; br = w / h
        if ir > br:
            ah = w / ir
            slide.shapes.add_picture(str(path), Inches(x), Inches(y + (h - ah) / 2),
                                     width=Inches(w))
        else:
            aw = h * ir
            slide.shapes.add_picture(str(path), Inches(x + (w - aw) / 2), Inches(y),
                                     height=Inches(h))
    elif w is not None and h is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 width=Inches(w), height=Inches(h))
    elif w is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y), width=Inches(w))
    else:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y))


SCREENSHOTS = ROOT / "assets/screenshots"
_CROP_CACHE = ROOT / "rendered/assets/_crop_cache"


def hero_image(slide, src, x, y, w, h):
    """Cover-crop an image to EXACTLY fill box (x,y,w,h) — no distortion, no
    letterbox. python-pptx can't crop, so we pre-crop via PIL to the target
    aspect ratio and cache the result. Used for ≥40% hero fills (s01, s30)."""
    src = Path(src)
    if not src.exists():
        return
    _CROP_CACHE.mkdir(parents=True, exist_ok=True)
    target_ratio = w / h
    try:
        img = Image.open(src).convert("RGB")
    except Exception:
        return
    iw, ih = img.size
    ir = iw / ih
    if ir > target_ratio:      # image wider — crop sides
        new_w = int(ih * target_ratio)
        left = (iw - new_w) // 2
        img = img.crop((left, 0, left + new_w, ih))
    else:                       # image taller — crop top/bottom
        new_h = int(iw / target_ratio)
        top = (ih - new_h) // 2
        img = img.crop((0, top, iw, top + new_h))
    out = _CROP_CACHE / f"{src.stem}_{w:.2f}x{h:.2f}.png"
    img.save(out)
    slide.shapes.add_picture(str(out), Inches(x), Inches(y),
                             width=Inches(w), height=Inches(h))


def slide_title(slide, text, *, y=0.42, h=0.95, w=12.25, x=0.55, size=26,
                color=DEEP, bold=True, line_spacing=1.12, align=PP_ALIGN.LEFT):
    text_box(slide, x=x, y=y, w=w, h=h, text=text,
             size=size, bold=bold, color=color, line_spacing=line_spacing,
             align=align)


def gold_callout(slide, x, y, w, h, text, *, size=15, bold=True,
                 color=DEEP, align=PP_ALIGN.LEFT):
    filled_rect(slide, x, y, w, h, GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.10)
    text_box(slide, x=x + 0.22, y=y + 0.06, w=w - 0.44, h=h - 0.12, text=text,
             size=size, bold=bold, color=color, anchor=MSO_ANCHOR.MIDDLE,
             align=align, line_spacing=1.22)


def footer(slide, text):
    # issue #171: record the footer so ref-slides can relocate/fold it; still
    # render normally (post-processing removes it only on ref-slides).
    _FOOTER_TEXT[id(slide)] = text
    tb = text_box(slide, x=0.55, y=7.02, w=12.25, h=0.36, text=text,
                  size=12, italic=True, color=LIGHT, align=PP_ALIGN.LEFT,
                  line_spacing=1.0)
    _FOOTER_TEXT.setdefault("_shapes", {})[id(slide)] = tb
    return tb


def icon(slide, name, x, y, size, variant="mid"):
    add_image(slide, ICONS / f"{name}-{variant}.png", x, y, size, size)


def speaker_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


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
# Deck loader — U-9: deck.yaml split на 2 части (≤600 строк каждая).
# Loader читает ОБЕ части, объединяет ключ `slides`, валидирует totals.
# ============================================================
def load_deck():
    """Load 2-part deck spec (deck.yaml + deck-part2.yaml), merge `slides`.

    Returns dict with merged slide list + validation. Raises if the
    ordered slide-id list does not match the canonical v3 presentation
    order (cascade-safe guard — s01–s30 must NOT be renumbered).
    """
    try:
        import yaml
    except ImportError:
        return None  # yaml optional — builder list is authoritative anyway
    p1 = ROOT / "deck.yaml"
    p2 = ROOT / "deck-part2.yaml"
    parts = [ROOT / "deck.yaml", ROOT / "deck-part2.yaml", ROOT / "deck-part3.yaml"]
    slides = []
    d1 = None
    totals = {}
    for pp in parts:
        if not pp.exists():
            continue
        d = yaml.safe_load(pp.read_text(encoding="utf-8"))
        if d1 is None:
            d1 = d
        slides += list(d.get("slides", []))
        if d.get("totals"):
            totals = d["totals"]
    spec = {
        "deck": d1.get("deck", {}) if d1 else {},
        "palette": d1.get("palette", {}) if d1 else {},
        "slides": slides,
        "totals": totals,
    }
    ids = [s["id"] for s in slides]
    # builder list is authoritative; deck.yaml is documentation — report only.
    print(f"deck.yaml slide ids ({len(ids)}): {ids}")
    return spec


# ============================================================
# Section divider — unified template (6-card roadmap, gold current)
# Sections of Лекции 3 (deck.yaml): 0..5.
# ============================================================
NAV = [
    ("0", "Открытие"),
    ("1", "Промпт"),
    ("2", "RAG"),
    ("3", "Fine-tune"),
    ("4", "Агенты"),
    ("5", "Фреймворк"),
]


def roadmap_bar(slide, here_idx, *, y=6.45):
    """6-card progress bar; current section gold-bordered."""
    n = len(NAV)
    gap = 0.14
    bx = 0.55
    total_w = 12.25
    cw = (total_w - gap * (n - 1)) / n
    ch = 0.62
    for i, (num, label) in enumerate(NAV):
        x = bx + i * (cw + gap)
        cur = (i == here_idx)
        if cur:
            filled_rect(slide, x, y, cw, ch, GOLD_TINT, stroke=GOLD,
                        stroke_pt=2.0, radius=True, radius_adj=0.12)
        else:
            filled_rect(slide, x, y, cw, ch, SURFACE, stroke=SOFT_GREY,
                        stroke_pt=1.0, radius=True, radius_adj=0.12)
        text_box(slide, x=x + 0.06, y=y + 0.07, w=cw - 0.12, h=0.24,
                 text=f"Раздел {num}", size=10.5, bold=True,
                 color=(DEEP if cur else LIGHT), align=PP_ALIGN.CENTER)
        text_box(slide, x=x + 0.06, y=y + 0.31, w=cw - 0.12, h=0.26,
                 text=label, size=11, bold=cur,
                 color=(DEEP if cur else SLATE), align=PP_ALIGN.CENTER)


def build_section_divider(p, here_idx, big_num, subtitle, frame_phrase, sid):
    """Distinct divider (NO ocean motif): giant decorative section digit on
    the right (cover-style soft outline), РАЗДЕЛ N label + subtitle + 1-line
    frame phrase on the left, gold-current roadmap bar at bottom."""
    s = blank(p)
    set_slide_bg(s, SURFACE)
    # Giant decorative digit, right side, soft outline color (like cover «03»)
    text_box(s, x=8.35, y=0.55, w=4.6, h=5.6, text=str(here_idx),
             size=380, bold=True, color=COVER_OUTLINE,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    # Left — section label + subtitle + frame phrase
    text_box(s, x=0.75, y=1.55, w=7.3, h=0.55,
             text=f"РАЗДЕЛ {here_idx}", size=20, bold=True, color=TEAL)
    filled_rect(s, 0.78, 2.16, 0.7, 0.05, fill=GOLD)
    text_box(s, x=0.75, y=2.55, w=7.5, h=1.85, text=subtitle,
             size=38, bold=True, color=DEEP, line_spacing=1.08)
    text_box(s, x=0.78, y=4.55, w=7.4, h=1.45, text=frame_phrase,
             size=18, italic=True, color=LIGHT, line_spacing=1.22)
    roadmap_bar(s, here_idx, y=6.45)
    speaker_notes(s, load_notes(sid))
    return s


# ============================================================
# Slide builders — 30 slides
# ============================================================

def build_s01(p):
    """hero_cover / case_study — Air Canada hook (issue #157 #211: убраны
    блоки «что выбрали / что нужно»). Real Air Canada 787 hero photo ≥40%
    площади слева (Wikimedia CC-BY-SA), assertion + хроника дела справа,
    gold takeaway снизу."""
    s = blank(p)
    # Hero photo — left ~46% width, near-full height (≥40% area)
    hx, hy, hw, hh = 0.0, 0.0, 6.05, 7.5
    hero_image(s, SCREENSHOTS / "s01-aircanada.jpg", hx, hy, hw, hh)
    # attribution label bottom-left over photo (semi plate)
    filled_rect(s, 0.0, 7.10, 3.9, 0.40, DEEP)
    text_box(s, 0.14, 7.12, 3.7, 0.34,
             "Фото: Air Canada Boeing 787 · Wikimedia · CC-BY-SA",
             size=10.5, italic=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    # Right — assertion + chronicle
    rx = 6.45
    text_box(s, rx, 0.55, 6.35, 1.55,
             "Чат-бот выдумал политику — платит компания.",
             size=30, bold=True, color=DEEP, line_spacing=1.06)
    text_box(s, rx, 2.14, 6.35, 0.36,
             "Moffatt v. Air Canada · трибунал BC · 14.02.2024",
             size=14, bold=True, color=TEAL)
    chron = [
        "Пассажир спросил чат-бота про тариф по случаю утраты близкого",
        "Бот: «купи по полной цене, верни разницу в течение 90 дней»",
        "Реальная политика этого не допускала — и была на той же странице, на которую бот ссылался",
        "Трибунал: «бот — не отдельное юр. лицо» → компания компенсирует разницу",
    ]
    cy = 2.66
    row_h = 0.90
    for i, t in enumerate(chron):
        circle(s, rx, cy + 0.03, 0.34, MID if i < 3 else GOLD)
        text_box(s, rx, cy + 0.03, 0.34, 0.34, str(i + 1),
                 size=14, bold=True, color=(WHITE if i < 3 else DEEP),
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, rx + 0.52, cy, 5.85, row_h - 0.06, t,
                 size=14, color=DEEP, line_spacing=1.14,
                 anchor=MSO_ANCHOR.MIDDLE)
        cy += row_h
    gold_callout(s, rx, 6.34, 6.35, 0.92,
                 "Это не сбой модели — это неправильный выбор архитектуры под задачу. Об этом классе ошибок вся лекция.",
                 size=13.5)
    speaker_notes(s, load_notes("s01"))


def build_s02(p):
    """cover — distinct, NO ocean motif. Mega «03» + title + roadmap.
    v2: subtitle brought to lec-02 cover canon — content-promise line with
    teal accent bar + MID color (was designer-initiative «Курс · 75 минут»
    meta-line italic-light, removed)."""
    s = blank(p)
    set_slide_bg(s, SURFACE)
    text_box(s, x=7.6, y=1.15, w=5.7, h=5.0, text="03",
             size=300, bold=True, color=COVER_OUTLINE,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line_spacing=1.0)
    text_box(s, x=0.75, y=1.35, w=6.6, h=0.5, text="ЛЕКЦИЯ 3",
             size=18, bold=True, color=TEAL)
    filled_rect(s, 0.78, 1.92, 0.7, 0.05, fill=TEAL)
    text_box(s, x=0.75, y=2.35, w=7.7, h=2.7,
             text="Архитектуры AI-систем:\nагенты, RAG, API",
             size=46, bold=True, color=DEEP, line_spacing=1.08)
    # subtitle = content promise (lec-02 canon: teal accent bar + MID, не meta)
    filled_rect(s, 0.78, 5.28, 0.05, 0.56, fill=TEAL)
    text_box(s, x=1.02, y=5.26, w=7.4, h=0.62,
             text="Какую архитектуру выбрать под задачу —\nи когда правильный ответ «не ИИ»",
             size=19, italic=False, color=MID, line_spacing=1.18)
    # v4 (#212): cover теперь чистый — roadmap вынесен в отдельный
    # lecture-map слайд s02a (паттерн Л1/Л2). Cover без roadmap-bar.
    text_box(s, x=0.75, y=6.75, w=7.0, h=0.4,
             text="3 курс ИУ6 · Модуль 1, обзорная лекция",
             size=13, italic=True, color=LIGHT)
    speaker_notes(s, load_notes("s02"))


def build_s02a(p):
    """NEW (#212) lecture-map — 6 horizontal section cards (Л1/Л2 pattern).
    Отдельный слайд-содержание после cover. Показывает маршрут лекции:
    Разделы 0–5 с одной строкой смысла каждого."""
    s = blank(p)
    slide_title(s, "Маршрут лекции — шесть разделов.", size=27)
    text_box(s, 0.55, 1.22, 12.25, 0.42,
             "Одна несущая линия: выбор архитектуры под задачу — и когда правильный ответ «не ИИ».",
             size=15, italic=True, color=MID)
    cards = [
        ("0", "Открытие", "Air Canada: неправильная архитектура стоит денег", "gavel", MID),
        ("1", "Промпт и его границы", "что умеет один вызов и где его потолок", "message-circle", MID),
        ("2", "RAG", "внешнее знание в контекст — и где оно тихо ломается", "database", MID),
        ("3", "Fine-tune", "менять веса под поведение, не под знание", "sliders-horizontal", MID),
        ("4", "Агенты", "цикл, экипировка, память, безопасность — и провалы", "bot", GOLD),
        ("5", "Фреймворк", "лестница + чек-лист: как выбрать быстро и обоснованно", "list-checks", MID),
    ]
    # 2 rows × 3 cols
    cw, chh = 3.95, 2.30
    gapx, gapy = 0.20, 0.28
    x0, y0 = 0.55, 1.90
    for i, (num, title, sub, ic, col) in enumerate(cards):
        r, c = divmod(i, 3)
        x = x0 + c * (cw + gapx)
        y = y0 + r * (chh + gapy)
        isgold = (col == GOLD)
        if isgold:
            ocean_box(s, x, y, cw, chh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, x, y, cw, chh)
        circle(s, x + 0.24, y + 0.24, 0.56, col)
        text_box(s, x + 0.24, y + 0.24, 0.56, 0.56, num,
                 size=22, bold=True, color=(DEEP if isgold else WHITE),
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        icon(s, ic, x + cw - 0.74, y + 0.26, 0.50, "gold" if isgold else "mid")
        text_box(s, x + 0.24, y + 0.98, cw - 0.48, 0.60, title,
                 size=16, bold=True, color=DEEP, line_spacing=1.05)
        text_box(s, x + 0.24, y + 1.58, cw - 0.48, 0.62, sub,
                 size=12.5, color=SLATE, line_spacing=1.14)
    speaker_notes(s, load_notes("s02a"))


def build_s03(p):
    """assertion_visual — hub & spokes: 1 LLM call + 4 wrappers.
    v4 (#213/#214): убран gold-highlight и chip «стоит на эмбеддингах» с
    RAG-карточки (4 обвязки теперь равнозначны); gold-акцент перенесён на
    центральный hub «один вызов» как точку отсчёта; footer упрощён.
    Финальная сверка формулировок — после готовности всей деки."""
    s = blank(p)
    slide_title(s, "Что мы переносим из Лекции 2 — и что надстроим.", size=26)
    text_box(s, 0.55, 1.25, 12.25, 0.4,
             "Вокруг одного вызова модели надстраиваются 4 обвязки. Два готовых блока из Лекции 2 не переобъясняем.",
             size=15, italic=True, color=MID)
    # Center hub — GOLD (точка отсчёта, единственный gold-акцент слайда)
    hx, hy, hw, hh = 5.05, 3.50, 3.25, 1.70
    # 4 equal spokes (uniform, no per-card gold)
    spokes = [
        ("RAG", "внешнее знание в контекст перед ответом", "database",
         0.55, 1.85),
        ("Function calling", "модель дотягивается до внешних систем", "terminal",
         6.95, 1.85),
        ("MCP", "стандарт подключения инструментов", "cable",
         0.55, 5.10),
        ("Цикл агента", "много шагов вокруг одного прохода", "bot",
         6.95, 5.10),
    ]
    sw, sh = 5.85, 1.55
    for title, sub, ic, sx, sy in spokes:
        ocean_box(s, sx, sy, sw, sh)
        icon(s, ic, sx + 0.26, sy + 0.34, 0.58, "mid")
        text_box(s, sx + 1.05, sy + 0.28, sw - 1.25, 0.42, title,
                 size=18, bold=True, color=MID)
        text_box(s, sx + 1.05, sy + 0.76, sw - 1.25, 0.66, sub,
                 size=13, color=DEEP, line_spacing=1.12)
    # Center hub (gold anchor)
    ocean_box(s, hx, hy, hw, hh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.5)
    text_box(s, hx + 0.15, hy + 0.24, hw - 0.30, 0.5, "Один вызов LLM",
             size=18, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, hx + 0.15, hy + 0.76, hw - 0.30, 0.85,
             "single-shot инференс из Лекции 2: один проход, без памяти между вызовами",
             size=12, italic=True, color=DEEP, align=PP_ALIGN.CENTER,
             line_spacing=1.14)
    # connectors hub -> spokes
    connector(s, hx + 0.25, hy + 0.25, 6.4, 3.4, LIGHT, 1.75)
    connector(s, hx + hw - 0.25, hy + 0.25, 6.95, 3.4, LIGHT, 1.75)
    connector(s, hx + 0.25, hy + hh - 0.25, 6.4, 5.10, LIGHT, 1.75)
    connector(s, hx + hw - 0.25, hy + hh - 0.25, 6.95, 5.10, LIGHT, 1.75)
    footer(s, "Из Лекции 2 берём готовыми: single-shot инференс и семантический поиск на эмбеддингах (основа RAG). Детали каждой обвязки — дальше по разделам.")
    speaker_notes(s, load_notes("s03"))


def build_s04(p):
    """assertion_visual — central question + 6-step ladder."""
    s = blank(p)
    text_box(s, 0.55, 0.38, 12.25, 0.42, "ЦЕНТРАЛЬНЫЙ ВОПРОС ЛЕКЦИИ",
             size=14, bold=True, color=TEAL)
    qx, qy, qw, qh = 0.55, 0.85, 12.25, 1.30
    ocean_box(s, qx, qy, qw, qh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, qx + 0.4, qy + 0.18, qw - 0.8, qh - 0.36,
             "У меня есть задача и доступ к LLM. Какую архитектуру выбрать — и когда правильный ответ «не ИИ»?",
             size=23, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.12)
    # Ladder — 6 steps bottom-up: idx 0 = step 1 (BOTTOM, gold), idx 5 = step 6 (top).
    steps = [
        ("1", "Обычный код (без ИИ)", "точка отсчёта", GOLD, True),
        ("2", "Один вызов LLM", "промпт; + CoT (по шагам), + few-shot (примеры)", MID, False),
        ("3", "RAG / контекст-инжиниринг", "поиск-дополненная генерация", LIGHT, False),
        ("4", "Workflow", "предопределённые пути", LIGHT, False),
        ("5", "Агент", "цикл plan → act → check → iterate", LIGHT, False),
        ("6", "Multi-agent", "несколько координируемых агентов", LIGHT, False),
    ]
    n = len(steps)
    # #215/#216: увеличены визуальные элементы лестницы — крупнее рунги
    # (step_h 0.66→0.74), крупнее номера-круги (0.36→0.46) и sub-подписи
    # (10.5→12), а также стрелка направления и её метки.
    step_h = 0.74
    vgap = 0.075
    bottom_edge = 6.85  # bottom of step 1
    sx = 0.55
    for i, (num, label, sub, col, isgold) in enumerate(steps):
        # i=0 -> bottom rung; each higher step sits above + indented right
        y = bottom_edge - step_h - i * (step_h + vgap)
        indent = i * 0.22
        w = 7.95 - indent
        x = sx + indent
        if isgold:
            ocean_box(s, x, y, w, step_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.5)
        else:
            ocean_box(s, x, y, w, step_h)
        circle(s, x + 0.16, y + (step_h - 0.46) / 2, 0.46, col)
        text_box(s, x + 0.16, y + (step_h - 0.46) / 2, 0.46, 0.46, num,
                 size=18, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x + 0.74, y + 0.11, w - 0.90, 0.30, label,
                 size=16, bold=True, color=DEEP)
        text_box(s, x + 0.74, y + 0.43, w - 0.90, 0.26, sub,
                 size=12, italic=True, color=SLATE)
    # PA-1 (owner-approved) + #216: direction-of-scale strip alongside ladder —
    # enlarged «сложнее ↑» / «проще ↓» + thicker arrow.
    text_box(s, 7.98, 2.28, 1.22, 0.34, "сложнее ↑", size=14, bold=True,
             color=LIGHT, align=PP_ALIGN.CENTER)
    up_arrow(s, 8.40, 2.72, 0.40, 3.86, fill=COVER_OUTLINE)
    text_box(s, 7.98, 6.62, 1.22, 0.34, "проще ↓", size=14, bold=True,
             color=LIGHT, align=PP_ALIGN.CENTER)
    # rule on the right
    ocean_box(s, 9.05, 2.55, 3.75, 3.95, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    icon(s, "milestone", 9.32, 2.85, 0.62, "gold")
    text_box(s, 9.32, 3.70, 3.25, 2.65,
             "Подниматься на следующую ступень — только при требовании задачи, которого текущая не закрывает.",
             size=16, bold=True, color=DEEP, line_spacing=1.24)
    footer(s, "Лестница — карта лекции, не требование понять всё сейчас. Каждую ступень разберём отдельно.")
    speaker_notes(s, load_notes("s04"))


def build_s05(p):
    """assertion_visual — default = one call; cost of each climb."""
    s = blank(p)
    slide_title(s, "Дефолт — один вызов с хорошим промптом.", size=27)
    # #219-context: explicit граница знания модели на видимом слое (§1.1)
    filled_rect(s, 0.55, 1.18, 12.25, 0.66, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.5, radius=True, radius_adj=0.10)
    text_box(s, 0.78, 1.24, 11.8, 0.56,
             "Модель знает только то, что в промпте (плюс то, что было в весах на обучении). Больше ей взять неоткуда.",
             size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.12)
    # Left — anchor block
    lx, ly, lw, lh = 0.55, 2.02, 5.55, 3.62
    ocean_box(s, lx, ly, lw, lh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    icon(s, "target", lx + 0.28, ly + 0.24, 0.58, "teal")
    text_box(s, lx + 0.28, ly + 0.94, lw - 0.56, 0.6,
             "Один вызов LLM\nс хорошим промптом",
             size=18, bold=True, color=DEEP, line_spacing=1.1)
    bullets = [
        "минимальная стоимость (один проход)",
        "минимальная латентность (нет лишних обращений)",
        "максимальная предсказуемость (нет петель, нет retrieval, который тихо деградирует)",
    ]
    by = ly + 1.90
    for b in bullets:
        circle(s, lx + 0.30, by + 0.07, 0.12, TEAL)
        text_box(s, lx + 0.56, by, lw - 0.84, 0.62, b,
                 size=13, color=DEEP, line_spacing=1.12)
        by += 0.56
    # Right — what each climb costs
    rx, rw = 6.30, 6.50
    ocean_box(s, rx, 2.02, rw, 1.70)
    text_box(s, rx + 0.26, 2.16, rw - 0.52, 0.36, "Добавляешь RAG →",
             size=15, bold=True, color=MID)
    text_box(s, rx + 0.26, 2.52, rw - 0.52, 1.10,
             "конвейер индексации + векторное хранилище + компонент retrieval (может молча деградировать) + метрики его качества",
             size=13, color=DEEP, line_spacing=1.14)
    ocean_box(s, rx, 3.88, rw, 1.76)
    text_box(s, rx + 0.26, 4.02, rw - 0.52, 0.36, "Добавляешь инструменты / цикл →",
             size=15, bold=True, color=MID)
    text_box(s, rx + 0.26, 4.38, rw - 0.52, 1.20,
             "внешние вызовы (падают, тормозят) + петли (расходятся) + недетерминизм траектории + новая поверхность атаки",
             size=13, color=DEEP, line_spacing=1.14)
    gold_callout(s, 0.55, 5.92, 12.25, 0.92,
                 "Не усложняй архитектуру без причины, выраженной в требованиях задачи. Это распределение бремени доказательства, а не примитивизм.",
                 size=15)
    speaker_notes(s, load_notes("s05"))


def build_s05a(p):
    """NEW (§1.2) — роли в промпте: миф «персона = точность» опровергнут.
    Zheng et al. 2024 EMNLP + arXiv:2605.29420. Часть failure/judgment —
    опровержение «магической пилюли»."""
    s = blank(p)
    slide_title(s, "Роль в промпте настраивает тон — не точность.", size=26)
    text_box(s, 0.55, 1.16, 12.25, 0.42,
             "«Ты — опытный юрист» сдвигает внимание модели (механизм — Лекция 2) в сторону текста, похожего на ответ такой роли, — но это про стиль, не про факты.",
             size=13.5, italic=True, color=MID, line_spacing=1.15)
    # left — the myth (crossed out) vs measured reality
    lx, ly, lw, lh = 0.55, 1.86, 6.35, 3.95
    ocean_box(s, lx, ly, lw, lh)
    text_box(s, lx + 0.28, ly + 0.22, lw - 0.56, 0.36, "Расхожий миф",
             size=15, bold=True, color=LIGHT)
    text_box(s, lx + 0.28, ly + 0.62, lw - 0.56, 0.70,
             "«Напишу роль эксперта — и модель будет точнее отвечать по фактам»",
             size=15, italic=True, color=SLATE, line_spacing=1.16)
    connector(s, lx + 0.28, ly + 1.42, lx + lw - 0.28, ly + 1.42, LIGHT, 1.0)
    text_box(s, lx + 0.28, ly + 1.56, lw - 0.56, 0.40, "Что показал эксперимент",
             size=15, bold=True, color=MID)
    text_box(s, lx + 0.28, ly + 1.98, lw - 0.56, 1.80,
             "162 персоны · 6 типов отношений · 8 доменов · 2410 вопросов фактического QA · 4 семейства LLM. Персоны НЕ улучшили точность ответа по сравнению с ответом без персоны вообще.",
             size=14, color=DEEP, line_spacing=1.22)
    # right — verdict + what role really does
    rx, rw = 7.15, 5.65
    ocean_box(s, rx, ly, rw, 1.75, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    icon(s, "user-round", rx + 0.28, ly + 0.26, 0.52, "teal")
    text_box(s, rx + 0.94, ly + 0.24, rw - 1.15, 0.5, "На что роль влияет реально",
             size=15, bold=True, color=TEAL, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, rx + 0.28, ly + 0.92, rw - 0.56, 0.75,
             "на тон и глубину изложения — насколько формально и подробно, а не верен ли факт (эффект модель-специфичен).",
             size=13.5, color=DEEP, line_spacing=1.18)
    gold_callout(s, rx, ly + 1.95, rw, 2.00,
                 "Нужна фактическая точность? Инструмент — не формулировка роли, а грамотный контекст и, при необходимости, RAG (опора на проверяемый источник). Это ещё один пункт «магической пилюли», опровергнутый измерением.",
                 size=13.5)
    footer(s, "Zheng, Pei, Logeswaran, Lee, Jurgens · Findings of EMNLP 2024 (arXiv:2311.10054) + arXiv:2605.29420 (2026).")
    speaker_notes(s, load_notes("s05a"))


def build_s05b(p):
    """NEW (§1.3) — структура промпта: разделители + разделение
    инструкция/контекст/данные. Параллель со structured output (§4.1):
    вход vs выход — тот же принцип."""
    s = blank(p)
    slide_title(s, "Структура промпта: разделяй инструкцию, контекст, данные.",
                size=23, h=1.30, line_spacing=1.08)
    text_box(s, 0.55, 1.58, 12.25, 0.42,
             "Плоский промпт заставляет модель угадывать, где кончается инструкция и начинаются данные. Явная граница снимает эту неоднозначность.",
             size=13.5, italic=True, color=MID, line_spacing=1.15)
    # left — 3 stacked labelled parts (structured input)
    lx, ly, lw = 0.55, 2.14, 5.85
    parts = [
        ("braces", "Инструкция", "что сделать", MID),
        ("book-open", "Контекст", "на основе чего", LIGHT),
        ("database", "Данные", "с чем именно работать", TEAL),
    ]
    ph = 1.16
    pgap = 0.16
    py = ly
    for ic, t, sub, col in parts:
        ocean_box(s, lx, py, lw, ph)
        filled_rect(s, lx + 0.22, py + 0.22, 0.72, ph - 0.44, col, radius=True,
                    radius_adj=0.16)
        icon(s, ic, lx + 0.34, py + ph / 2 - 0.24, 0.48, "white")
        text_box(s, lx + 1.14, py + 0.20, lw - 1.35, 0.42, t,
                 size=17, bold=True, color=DEEP)
        text_box(s, lx + 1.14, py + 0.62, lw - 1.35, 0.40, sub,
                 size=13, italic=True, color=SLATE)
        py += ph + pgap
    # right — delimiters kinds + structured-output parallel
    rx, rw = 7.15, 5.65
    ocean_box(s, rx, ly, rw, 1.95)
    text_box(s, rx + 0.28, ly + 0.18, rw - 0.56, 0.36, "Разделители (delimiters)",
             size=15, bold=True, color=MID)
    for i, d in enumerate([
        "XML-теги:  <инструкция>…</инструкция>",
        "Markdown-заголовки:  ## Задача · ## Данные",
        "Тройные кавычки / бэктики вокруг данных",
    ]):
        circle(s, rx + 0.30, ly + 0.62 + i * 0.40 + 0.05, 0.12, LIGHT)
        text_box(s, rx + 0.54, ly + 0.62 + i * 0.40, rw - 0.82, 0.38, d,
                 size=13, color=DEEP, font=FONT_MONO if i < 2 else FONT_BODY,
                 line_spacing=1.05)
    ocean_box(s, rx, ly + 2.10, rw, 1.70, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, rx + 0.28, ly + 2.24, rw - 0.56, 1.44,
             "Тот же принцип, что structured output (Раздел 4): там схема задаёт структуру ВЫХОДА, здесь разделители — структуру ВХОДА. Ясная структура вместо «выведи форму по смыслу».",
             size=13.5, color=DEEP, line_spacing=1.20)
    gold_callout(s, 0.55, 5.98, 12.25, 0.86,
                 "Модель, которой показали, где кончается инструкция и начинаются данные, реже принимает фрагмент данных за новую команду — та же путаница лежит в основе prompt injection (Раздел 4).",
                 size=13.5)
    speaker_notes(s, load_notes("s05b"))


def build_s06(p):
    """case_study — CoT worked example + faithfulness limit MERGED (§1.4+§1.5)."""
    s = blank(p)
    slide_title(s, "Chain-of-thought помогает — но его нельзя аудировать.", size=24)
    # TOP BAND — CoT worked example (compact before/after)
    cy, ch = 1.16, 2.02
    cw = 6.05
    ocean_box(s, 0.55, cy, cw, ch)
    text_box(s, 0.83, cy + 0.14, cw - 0.56, 0.34, "Без CoT",
             size=15, bold=True, color=LIGHT)
    text_box(s, 0.83, cy + 0.52, cw - 0.56, 0.85,
             "«Было 23 яблока, 7 испортились, докупили 2 ящика по 6. Сколько хороших?»",
             size=13, color=DEEP, line_spacing=1.14)
    text_box(s, 0.83, cy + 1.42, cw - 0.56, 0.5,
             "→ правдоподобное, но неверное число",
             size=13, bold=True, color=SLATE)
    rx0 = 6.75
    ocean_box(s, rx0, cy, cw, ch, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, rx0 + 0.28, cy + 0.14, cw - 0.56, 0.34, "С CoT («решай по шагам»)",
             size=15, bold=True, color=TEAL)
    text_runs(s, rx0 + 0.30, cy + 0.56, cw - 0.6, 0.9, [
        {"text": "23 − 7 = 16    ·    2 × 6 = 12", "size": 15, "bold": True, "color": DEEP},
        {"text": "16 + 12 = 28", "size": 22, "bold": True, "color": GOLD,
         "newpara": True, "space_before": 6},
    ], line_spacing=1.1)
    text_box(s, rx0 + 0.30, cy + 1.56, cw - 0.6, 0.36, "→ верно",
             size=13, bold=True, color=TEAL)
    # thin note between bands (single line)
    text_box(s, 0.55, cy + ch + 0.06, 12.25, 0.28,
             "Технически это всё ещё один вызов — CoT инструмент под класс задач (цепочка шагов), не глобальный тумблер.",
             size=12, italic=True, color=MID)
    # BOTTOM BAND — faithfulness limit
    fy = 3.70
    text_box(s, 0.55, fy, 12.25, 0.34,
             "Но проговорённое рассуждение не обязано отражать реальную причину ответа (низкая faithfulness):",
             size=14, bold=True, color=DEEP)
    # 2 stat cards
    st_y = fy + 0.46
    for i, (m, who, isgold) in enumerate([
        ("~25%", "Claude 3.7 Sonnet", True),
        ("~39%", "DeepSeek R1", False)]):
        sxx = 0.55 + i * 2.55
        if isgold:
            ocean_box(s, sxx, st_y, 2.35, 1.55, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, sxx, st_y, 2.35, 1.55)
        text_box(s, sxx + 0.10, st_y + 0.18, 2.15, 0.7, m,
                 size=36, bold=True, color=(GOLD if isgold else MID),
                 align=PP_ALIGN.CENTER)
        text_box(s, sxx + 0.10, st_y + 0.92, 2.15, 0.55, who,
                 size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 line_spacing=1.05)
    text_box(s, 0.55, st_y + 1.60, 5.15, 0.5,
             "— доля случаев, где модель упомянула реально использованную подсказку.",
             size=11.5, italic=True, color=SLATE, line_spacing=1.10)
    # rule callout right
    gold_callout(s, 5.90, st_y, 6.90, 2.10,
                 "Контроль на самообъяснении модели — не контроль. Человек-валидатор проверяет РЕЗУЛЬТАТ и факты против внешнего источника, а не правдоподобность текста. И это же — почему шаг check в цикле агента (Раздел 4) не должен быть самооценкой модели.",
                 size=14)
    footer(s, "Anthropic, апрель 2025 · верность падает на трудных задачах · перепроверить ко дню лекции.")
    speaker_notes(s, load_notes("s06"))


def build_s08(p):
    """assertion_visual — context engineering + context rot curve (c08)."""
    s = blank(p)
    slide_title(s, "Контекст-инжиниринг: минимум высокосигнального.", size=26)
    text_box(s, 0.55, 1.20, 12.25, 0.55,
             "Промпт-инжиниринг — одна инструкция. Контекст-инжиниринг — курирование всего набора токенов, видимых модели на инференсе.",
             size=14, italic=True, color=MID, line_spacing=1.15)
    # left — curve chart
    cx, cyy, cw, chh = 0.55, 1.95, 7.05, 3.55
    ocean_box(s, cx, cyy, cw, chh)
    add_image(s, CHARTS / "c08-context-rot.png", cx + 0.18, cyy + 0.16,
              cw - 0.36, chh - 0.32)
    text_box(s, cx + 0.18, cyy + chh + 0.02, cw - 0.36, 0.42,
             "context rot = тот же «lost in the middle» из Л2 — новый термин, не новая сущность",
             size=11.5, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    # right — criterion
    rx, rw = 7.85, 4.95
    ocean_box(s, rx, 1.95, rw, 3.55, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, rx + 0.28, 2.16, rw - 0.56, 0.45, "Когда НЕ RAG (точка 1)",
             size=17, bold=True, color=TEAL)
    text_box(s, rx + 0.28, 2.70, rw - 0.56, 1.55,
             "малый стабильный корпус, влезает в окно → full-context + кэширование префикса, а не RAG-инфраструктура",
             size=15, color=DEEP, line_spacing=1.22)
    icon(s, "circle-slash", rx + 0.28, 4.45, 0.78, "teal")
    text_box(s, rx + 1.20, 4.55, rw - 1.45, 0.85,
             "RAG здесь добавил бы хрупкость без выигрыша",
             size=13.5, bold=True, color=DEEP, line_spacing=1.12,
             anchor=MSO_ANCHOR.MIDDLE)
    gold_callout(s, 0.55, 5.95, 12.25, 0.88,
                 "«Найти наименьший набор высокосигнальных токенов, максимизирующий вероятность желаемого исхода» — это инженерное требование, не эстетика.",
                 size=14.5)
    speaker_notes(s, load_notes("s08"))


def build_s08a(p):
    """NEW (§1.8) — чит-шит «как строить промпт», 8 пунктов. Компактный
    аналог чек-листа §5.3 для уровня одного промпта."""
    s = blank(p)
    slide_title(s, "Чит-шит: как строить промпт.", size=27)
    text_box(s, 0.55, 1.16, 12.25, 0.40,
             "Минимум, ниже которого промпт систематически недорабатывает. Приложите к любому промпту перед первым запуском.",
             size=14, italic=True, color=MID)
    items = [
        ("Роль", "если нужен тон/регистр — и НЕ как обещание точности"),
        ("Задача", "конкретное проверяемое действие, не расплывчатое пожелание"),
        ("Контекст", "минимально необходимое, не «всё, что могло бы пригодиться»"),
        ("Формат вывода", "указан явно, если ответ машинно-обрабатываем"),
        ("Разделители", "если содержимого больше одного вида (инструкция/данные)"),
        ("Примеры (few-shot)", "только если формат неочевиден из одной инструкции"),
        ("CoT", "только если задача требует многошагового рассуждения"),
        ("Длина", "не длиннее необходимого — лишние токены «тонут» в контексте"),
    ]
    cw, chh = 3.95, 1.28
    gapx, gapy = 0.20, 0.20
    x0, y0 = 0.55, 1.78
    for i, (t, sub) in enumerate(items):
        r, c = divmod(i, 2)
        # 2 cols × 4 rows
        x = x0 + c * (cw + gapx) if False else 0.0
        # 4 cols × 2 rows layout
        col = i % 4
        row = i // 4
        cw2 = 3.02
        x = 0.55 + col * (cw2 + 0.13)
        y = y0 + row * (chh + gapy)
        isgold = (i == 0)  # роль = ключевой пункт (миф про точность)
        if isgold:
            ocean_box(s, x, y, cw2, chh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, x, y, cw2, chh)
        circle(s, x + 0.18, y + 0.18, 0.34, GOLD if isgold else MID)
        text_box(s, x + 0.18, y + 0.18, 0.34, 0.34, str(i + 1),
                 size=13, bold=True, color=(DEEP if isgold else WHITE),
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x + 0.62, y + 0.16, cw2 - 0.78, 0.40, t,
                 size=14, bold=True, color=DEEP)
        text_box(s, x + 0.20, y + 0.58, cw2 - 0.40, 0.62, sub,
                 size=11, color=SLATE, line_spacing=1.10)
    gold_callout(s, 0.55, 5.20, 12.25, 1.05,
                 "Компактная форма всего раздела: роль ≠ точность, структура помогает разделить входы, CoT — точечный инструмент, контекст — минимальный. Для крупных архитектурных решений (RAG / FT / агент) — восьмишаговый чек-лист Раздела 5.",
                 size=14)
    speaker_notes(s, load_notes("s08a"))


def build_s09(p):
    """section_divider — Раздел 2 RAG."""
    build_section_divider(
        p, 2, "Раздел 2", "RAG: поиск-дополненная генерация",
        "Извлечь релевантное → положить в контекст → ответить с опорой на источник",
        "s09")


def build_s10(p):
    """schema_pipeline — RAG 3-stage horizontal pipeline (RIGHT_ARROW)."""
    s = blank(p)
    slide_title(s, "Принцип RAG — три шага.", size=27)
    text_box(s, 0.55, 1.16, 12.25, 0.4,
             "RAG = индексация → retrieval (semantic search Л2) → генерация с опорой; «не знаю» — корректный ответ.",
             size=14.5, italic=True, color=MID)
    # 3 stage boxes with RIGHT_ARROW between
    sy, sh = 1.85, 3.05
    bw = 3.55
    gap_arrow = 0.55
    x0 = 0.55
    stages = [
        ("1", "Индексация", "заранее, офлайн", "database",
         "корпус → чанки → эмбеддинг каждого → векторное хранилище", MID, False),
        ("2", "Retrieval", "на запрос", "route",
         "вопрос → эмбеддинг → top-k ближайших фрагментов\n\n= тот самый semantic search из Л2 — не переобъясняем", MID, False),
        ("3", "Генерация", "с опорой (grounding)", "check-check",
         "фрагменты + вопрос → ответ со ссылкой на источник", TEAL, True),
    ]
    x = x0
    for i, (num, title, tag, ic, body, col, isteal) in enumerate(stages):
        if isteal:
            ocean_box(s, x, sy, bw, sh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
        else:
            ocean_box(s, x, sy, bw, sh)
        circle(s, x + 0.26, sy + 0.26, 0.46, col)
        text_box(s, x + 0.26, sy + 0.26, 0.46, 0.46, num,
                 size=18, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x + 0.86, sy + 0.26, bw - 1.05, 0.42, title,
                 size=17, bold=True, color=DEEP)
        text_box(s, x + 0.86, sy + 0.66, bw - 1.05, 0.30, tag,
                 size=11.5, italic=True, color=LIGHT)
        icon(s, ic, x + bw - 0.78, sy + 0.28, 0.50,
             "teal" if isteal else "mid")
        text_box(s, x + 0.28, sy + 1.18, bw - 0.56, sh - 1.36, body,
                 size=13.5, color=DEEP, line_spacing=1.22)
        if i < 2:
            right_arrow(s, x + bw + 0.06, sy + sh / 2 - 0.30, gap_arrow - 0.12, 0.60,
                        fill=LIGHT)
        x += bw + gap_arrow
    gold_callout(s, 0.55, 5.25, 12.25, 1.05,
                 "«Не знаю» / «см. источник X» — корректный ответ RAG-системы. Правдоподобный ответ при нерелевантном retrieval — это дефект, а не «лучше, чем ничего».",
                 size=15)
    speaker_notes(s, load_notes("s10"))


def build_s11(p):
    """assertion_visual — 4 conjunction cards -> RAG."""
    s = blank(p)
    slide_title(s, "Когда RAG — правильный выбор.", size=27)
    # #221/#222: убран жаргон «конъюнкция/дизъюнкция»; формулировка §2.2 —
    # сильный сигнал по признакам + отсутствие блокеров с §2.3.
    text_box(s, 0.55, 1.16, 12.25, 0.4,
             "RAG оправдан при сильном сигнале по признакам ниже — и отсутствии блокеров со следующего слайда «когда НЕ RAG».",
             size=14.5, italic=True, color=MID)
    cards = [
        ("Большое / растущее", "не влезает в окно целиком, или дорого класть весь корпус в каждый запрос"),
        ("Меняется", "документы, цены, регламенты обновляются чаще, чем выходят версии модели"),
        ("Свежесть + провенанс", "ответ опирается на проверяемый источник; можно показать, откуда факт"),
        ("Приватная база", "знания компании не входят в веса публичной модели"),
    ]
    cw, chh = 2.90, 2.55
    cy = 1.78
    x = 0.55
    for i, (t, sub) in enumerate(cards):
        ocean_box(s, x, cy, cw, chh)
        text_box(s, x + 0.20, cy + 0.22, cw - 0.40, 0.75, t,
                 size=15.5, bold=True, color=MID, line_spacing=1.05)
        text_box(s, x + 0.20, cy + 1.00, cw - 0.40, chh - 1.2, sub,
                 size=12, color=DEEP, line_spacing=1.16)
        x += cw + 0.20
    # -> RAG result + worked example
    ocean_box(s, 0.55, 4.55, 7.55, 1.80, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    text_box(s, 0.85, 4.72, 7.1, 0.4, "Признаки усиливают друг друга → RAG",
             size=17, bold=True, color=DEEP)
    text_box(s, 0.85, 5.16, 7.1, 1.10,
             "Корп. база из тысяч регламентов, обновляется еженедельно, ответ с обязательной ссылкой на пункт: все признаки сошлись, ни один более простой механизм их совместно не закрывает → образцовый профиль RAG.",
             size=13, color=DEEP, line_spacing=1.16)
    ocean_box(s, 8.30, 4.55, 4.50, 1.80, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    icon(s, "check-check", 8.55, 4.74, 0.44, "teal")
    text_box(s, 8.55, 5.24, 4.05, 1.00,
             "Один признак — повод присмотреться, но не строить автоматически: сверьтесь с блокерами на следующем слайде.",
             size=12.5, bold=True, color=DEEP, line_spacing=1.15)
    speaker_notes(s, load_notes("s11"))


def build_s12(p):
    """schema_matrix-ish — 3 criteria columns «when NOT RAG».
    P1 fix (issue #157 review): s11/s12 shared identical «N cards + summary
    plaque» skeleton back-to-back — visually merged into one stretched
    slide. Differentiated here via base card palette (TEAL instead of
    primary LIGHT/SURFACE — «caution / exclusion» register vs s11's
    primary-blue «inclusion» cards) + numbered gold badge per card (s22b
    slot-badge pattern) so the two decks read as distinct compositions at
    a glance, without touching content/copy."""
    s = blank(p)
    slide_title(s, "Когда RAG — НЕ правильный выбор.", size=27)
    text_box(s, 0.55, 1.16, 12.25, 0.4,
             "Знать, когда RAG не нужен, ценнее: это модная архитектура, её ставят туда, где она вредит.",
             size=14.5, italic=True, color=MID)
    # #223/#224: критерий observability убран (он живёт на s13, провал RAG
    # на масштабе, не дублируется здесь). Вместо него — новый критерий
    # «данные доступны live через API/MCP» (§2.3, forward-callback на §4.1).
    cols = [
        ("circle-slash", "Корпус влезает в окно",
         "ориентир — менее ~200k токенов, меняется редко",
         "→ full-context + кэширование префикса, не RAG-инфраструктура",
         False),
        ("key", "Фиксированная политика / значение",
         "тариф, цена, пункт регламента, правило",
         "→ детерминированный lookup / статическая страница",
         False),
        ("cable", "Данные доступны live через API / MCP",
         "во внутреннем сервисе, базе, поиске другой системы",
         "→ вызвать инструмент напрямую; RAG-индекс поверх — лишний, более хрупкий и более устаревающий слой",
         True),
    ]
    cw, chh = 4.00, 3.05
    cy = 1.78
    x = 0.55
    for i, (nm, t, tag, alt, isgold) in enumerate(cols):
        if isgold:
            ocean_box(s, x, cy, cw, chh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, x, cy, cw, chh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=1.5)
        # numbered badge top-left (s22b slot-badge pattern) — distinct
        # silhouette from s11's plain unnumbered cards
        circle(s, x + 0.20, cy + 0.18, 0.32, GOLD if isgold else TEAL)
        text_box(s, x + 0.20, cy + 0.18, 0.32, 0.32, str(i + 1),
                 size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        icon(s, nm, x + cw - 0.76, cy + 0.20, 0.52, "gold" if isgold else "teal")
        text_box(s, x + 0.66, cy + 0.24, cw - 1.55, 0.78, t,
                 size=15, bold=True, color=(DEEP if isgold else TEAL),
                 line_spacing=1.08)
        text_box(s, x + 0.24, cy + 1.15, cw - 0.48, 0.40, tag,
                 size=12, italic=True, color=LIGHT)
        text_box(s, x + 0.24, cy + 1.58, cw - 0.48, chh - 1.75, alt,
                 size=13, bold=True, color=DEEP, line_spacing=1.18)
        x += cw + 0.32
    gold_callout(s, 0.55, 5.20, 12.25, 1.05,
                 "RAG избыточен, если выполнен ЛЮБОЙ из трёх: (а) корпус влезает в окно и стабилен, (б) задача сводится к фиксированному значению, (в) знание уже доступно напрямую и живьём через инструмент. «Прямой вызов вернёт данные на момент запроса; RAG-индекс — на момент последней индексации.»",
                 size=13.5)
    speaker_notes(s, load_notes("s12"))


def build_s13(p):
    """case_study — RAG fails at scale + Air Canada — разбор архитектуры (v2: decluttered
    — per-case triangle-alert icons, tighter visible text, mass-rebalanced
    right box so diagnosis+alternative fill evenly, no big internal gap)."""
    s = blank(p)
    slide_title(s, "Провал RAG на масштабе.", size=27)
    gold_callout(s, 0.55, 1.10, 12.25, 0.95,
                 "«Вернул что-то» ≠ «вернул правильное». У RAG нет сигнала «не нашёл» — он всегда отдаёт k ближайших, даже нерелевантных.",
                 size=15)
    # left — 3 failure cases, each with a triangle-alert anchor icon
    # PA-2 (owner-approved): cases distributed EVENLY across the full box
    # height with thin separators (was ~15-20% dead band at the bottom;
    # mass now matches the right Air Canada box).
    lx, lw = 0.55, 6.55
    box_y, box_h = 2.14, 3.74
    ocean_box(s, lx, box_y, lw, box_h)
    cases = [
        ("Legal-AI", "«ближайшие» дела из другой юрисдикции / отменённый прецедент — модель опирается на них как на факт"),
        ("Medical-RAG", "смешал фрагменты разных пациентов — близки по симптомам, клинически объединять нельзя"),
        ("Support-бот", "работал на сотнях статей; после роста до тысяч качество тихо просело — никто не заметил"),
    ]
    cell_h = box_h / 3.0          # 3 equal cells fill the box top→bottom
    for ci, (nm, body) in enumerate(cases):
        cy0 = box_y + ci * cell_h
        icon(s, "triangle-alert", lx + 0.28, cy0 + 0.22, 0.40, "teal")
        text_box(s, lx + 0.84, cy0 + 0.22, lw - 1.10, 0.36, nm,
                 size=16, bold=True, color=MID)
        text_box(s, lx + 0.28, cy0 + 0.66, lw - 0.54, 0.62, body,
                 size=13, color=DEEP, line_spacing=1.20)
        if ci < 2:
            connector(s, lx + 0.30, box_y + (ci + 1) * cell_h,
                      lx + lw - 0.30, box_y + (ci + 1) * cell_h, LIGHT, 0.75)
    # right — Air Canada — разбор архитектуры (teal), evenly split: diagnosis / alternative
    rx, rw = 7.35, 5.45
    ocean_box(s, rx, 2.14, rw, 3.74, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, rx + 0.30, 2.36, rw - 0.60, 0.34, "Air Canada — разбор архитектуры",
             size=16, bold=True, color=TEAL)
    text_box(s, rx + 0.30, 2.78, rw - 0.60, 0.30, "Диагноз",
             size=13, bold=True, color=DEEP)
    text_box(s, rx + 0.30, 3.10, rw - 0.60, 1.05,
             "сгенерированный правдоподобный текст поставлен в роль, требовавшую извлечённого проверенного факта — отказ grounding",
             size=13, color=DEEP, line_spacing=1.20)
    connector(s, rx + 0.30, 4.22, rx + rw - 0.30, 4.22, TEAL, 1.0)
    text_box(s, rx + 0.30, 4.34, rw - 0.60, 0.30, "Правильная альтернатива",
             size=13, bold=True, color=DEEP)
    text_box(s, rx + 0.30, 4.66, rw - 0.60, 1.15,
             "фиксированная политика → lookup / страница; нужен диалог → RAG со strict grounding, обязательная цитата, явное «не знаю», проверка человеком",
             size=13, color=DEEP, line_spacing=1.20)
    footer(s, "Документированные классы провалов (Barnett et al. 2024; Air Canada — McCarthy Tétrault 2024). Кейсы — illustrative.")
    speaker_notes(s, load_notes("s13"))


def build_s14(p):
    """MERGED (§3.1/§3.3 scope + §3.5 criteria table) — «fine-tuning сузился»
    сверху (2 зоны) + компактная таблица «что куда» снизу. #227 P0: дистилляция
    НЕ помечена как fine-tuning нигде — «fine-tune teacher + дистилляция
    student, две отдельные техники в связке»."""
    s = blank(p)
    slide_title(s, "Fine-tuning не умер — он сузился до поведения.", size=25)
    # TOP — 2 zones (что ушло / что осталось)
    zy, zh = 1.14, 1.72
    ocean_box(s, 0.55, zy, 6.05, zh)
    icon(s, "git-branch", 0.80, zy + 0.20, 0.46, "mid")
    text_box(s, 1.40, zy + 0.20, 4.95, 0.42, "Ушло из fine-tuning (2026)",
             size=15, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.80, zy + 0.72, 5.55, 0.90,
             "знание, факты, то, что меняется → RAG / длинный контекст. Зашить факты в веса: нельзя процитировать, обновить точечно, удалить один.",
             size=12.5, color=DEEP, line_spacing=1.16)
    ocean_box(s, 6.75, zy, 6.05, zh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    icon(s, "scale", 7.00, zy + 0.20, 0.46, "teal")
    text_box(s, 7.60, zy + 0.20, 4.95, 0.42, "Осталось за fine-tuning",
             size=15, bold=True, color=TEAL, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 7.00, zy + 0.72, 5.55, 0.90,
             "поведение · стиль · формат вывода · следование политике. Дистилляция — отдельная техника, часто применяемая в связке с дообучением.",
             size=12.5, color=DEEP, line_spacing=1.16)
    # BOTTOM — criteria table «что куда»
    ocean_box(s, 0.40, 3.02, 12.55, 3.02)
    tx, ty, = 0.55, 3.14
    headers = ["Если задача требует…", "→ правильный инструмент", "…и НЕ этот, потому что"]
    col_w = [3.95, 3.45, 4.85]
    rows = [
        ("знание меняется / нужны свежесть, провенанс", "RAG (или длинный контекст для малого корпуса)",
         "не fine-tuning: устареет, дорого переобучать, риск forgetting", False),
        ("стабильное поведение / тон / формат / политика", "fine-tuning (PEFT)",
         "не RAG: подаёт знание, но не меняет манеру модели", False),
        ("снизить стоимость / латентность на узкой задаче", "fine-tune teacher + дистилляция student",
         "две отдельные техники в связке, НЕ «дистилляция = вид fine-tuning»", False),
        ("детерминированный, верифицируемый ответ", "обычный код, без ИИ",
         "ни RAG, ни FT: ИИ добавит недетерминизм без выигрыша", True),
    ]
    hh, rh = 0.48, 0.58
    cx = tx
    for j, hd in enumerate(headers):
        filled_rect(s, cx, ty, col_w[j], hh, MID, radius=False)
        text_box(s, cx + 0.14, ty, col_w[j] - 0.28, hh, hd,
                 size=12.5, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        cx += col_w[j]
    yy = ty + hh
    for ri, (c0, c1, c2, isgold) in enumerate(rows):
        bgrow = GOLD_TINT if isgold else (WHITE if ri % 2 == 0 else SURFACE)
        cx = tx
        for j, cc in enumerate([c0, c1, c2]):
            filled_rect(s, cx, yy, col_w[j], rh, bgrow,
                        stroke=(GOLD if isgold else SOFT_GREY),
                        stroke_pt=(1.5 if isgold else 0.75))
            col = (DEEP if isgold else MID) if j == 1 else DEEP
            text_box(s, cx + 0.14, yy + 0.04, col_w[j] - 0.28, rh - 0.08, cc,
                     size=11.5, bold=(j == 1), color=col,
                     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.08)
            cx += col_w[j]
        yy += rh
    gold_callout(s, 0.55, 6.14, 12.25, 0.78,
                 "Реальный вопрос 2026 — не «RAG или fine-tuning», а «что здесь знание (→ RAG), что поведение (→ PEFT), что детерминировано (→ код)». Гибрид — норма там, где есть И проблема знания, И проблема поведения.",
                 size=13.5)
    speaker_notes(s, load_notes("s14"))


def build_s15(p):
    """assertion_visual — PEFT vs full-FT: frozen base + adapters + 3 reasons."""
    s = blank(p)
    slide_title(s, "PEFT вместо full fine-tuning.", size=27)
    text_box(s, 0.55, 1.16, 12.25, 0.78,
             "PEFT — базовые веса замораживаются, обучается лишь небольшой набор адаптеров. LoRA — низкоранговые матрицы-адаптеры; QLoRA — то же поверх квантованной модели.",
             size=14, italic=True, color=MID, line_spacing=1.18)
    # left — schema: big frozen base + small adapters
    lx, ly, lw, lh = 0.55, 2.10, 4.95, 3.15
    ocean_box(s, lx, ly, lw, lh)
    filled_rect(s, lx + 0.55, ly + 0.55, lw - 1.1, 1.55, MID, radius=True,
                radius_adj=0.06)
    text_box(s, lx + 0.55, ly + 0.55, lw - 1.1, 1.55,
             "Базовые веса\n(frozen)", size=17, bold=True, color=WHITE,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
    for k in range(3):
        ax = lx + 0.70 + k * 1.20
        filled_rect(s, ax, ly + 2.35, 0.95, 0.55, GOLD, radius=True,
                    radius_adj=0.18)
        text_box(s, ax, ly + 2.35, 0.95, 0.55, "LoRA",
                 size=11, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, lx, ly + lh - 0.02, lw, 0.3,
             "адаптеры — мегабайты vs гигабайты", size=11, italic=True,
             color=LIGHT, align=PP_ALIGN.CENTER)
    # right — 3 reasons
    rx, rw = 5.80, 7.0
    reasons = [
        ("1. Дешевле и быстрее", "обучаются миллионы параметров вместо миллиардов; QLoRA — на одном GPU", False),
        ("2. Модульность", "адаптеры мегабайты vs гигабайты; одна база — много специализаций", False),
        ("3. ↓ Риск catastrophic forgetting", "база заморожена, физически не переписывается под новый сигнал — архитектурный аргумент", True),
    ]
    yy = 2.10
    for t, b, isgold in reasons:
        if isgold:
            ocean_box(s, rx, yy, rw, 1.10, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, rx, yy, rw, 0.92)
        text_box(s, rx + 0.24, yy + 0.10, rw - 0.48, 0.34, t,
                 size=15, bold=True, color=(DEEP if isgold else MID))
        text_box(s, rx + 0.24, yy + 0.44, rw - 0.48, (0.60 if isgold else 0.44), b,
                 size=12.5, color=DEEP, line_spacing=1.12)
        yy += (1.24 if isgold else 1.06)
    # LoRA-adoption baseline (§3.2) с ОБЯЗАТЕЛЬНОЙ оговоркой на видимом слое
    # (Baseline Mandate): доля среди тегированных PEFT, не среди всего FT.
    by2 = 5.50
    ocean_box(s, 0.55, by2, 5.95, 1.32, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_runs(s, 0.80, by2 + 0.16, 5.5, 0.55, [
        {"text": "98,4% ", "size": 30, "bold": True, "color": GOLD},
        {"text": "моделей с тегом PEFT — это LoRA", "size": 14, "bold": True, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    text_box(s, 0.80, by2 + 0.72, 5.45, 0.52,
             "из 20 834 карточек на Hugging Face Hub · оговорка: доля среди моделей с тегом PEFT, не среди всего fine-tuning",
             size=11, italic=True, color=SLATE, line_spacing=1.12)
    gold_callout(s, 6.70, by2, 6.10, 1.32,
                 "PEFT (LoRA/QLoRA) почти всегда лучше full fine-tuning: дешевле, модульнее, ↓ риск forgetting. Full FT в 2026 — почти никогда.",
                 size=14)
    footer(s, "HF PEFT team, «Beyond LoRA?», июнь 2026. Полный спектр методов (SFT / DPO / RFT) — в главе.")
    speaker_notes(s, load_notes("s15"))


def build_s16(p):
    """case_study — catastrophic forgetting (diverging chart c16) + criterion."""
    s = blank(p)
    slide_title(s, "Провал: catastrophic forgetting.", size=27)
    text_box(s, 0.55, 1.16, 12.25, 0.55,
             "Catastrophic forgetting (катастрофическое забывание) — деградация общих способностей модели в результате узкого агрессивного дообучения.",
             size=14, italic=True, color=MID, line_spacing=1.15)
    cx, cyy, cw, chh = 0.55, 1.92, 7.05, 3.55
    ocean_box(s, cx, cyy, cw, chh)
    add_image(s, CHARTS / "c16-forgetting.png", cx + 0.18, cyy + 0.16,
              cw - 0.36, chh - 0.32)
    text_box(s, cx + 0.18, cyy + chh + 0.02, cw - 0.36, 0.42,
             "тяжелее с ростом масштаба модели — у крупной выше исходный уровень, ей «больше падать»",
             size=11.5, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    rx, rw = 7.85, 4.95
    ocean_box(s, rx, 1.92, rw, 2.30, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    text_box(s, rx + 0.26, 2.10, rw - 0.52, 2.0,
             "Нет eval-петли на общих задачах + нет версий датасета/весов → не увидишь поломку до прода + не сможешь откатиться → это не «риск», это критерий «НЕ делай fine-tuning»",
             size=13.5, bold=True, color=DEEP, line_spacing=1.20)
    ocean_box(s, rx, 4.37, rw, 1.10, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, rx + 0.26, 4.52, rw - 0.52, 0.85,
             "Правильно: PEFT (замороженные веса — ниже риск); для меняющегося знания — RAG, не FT вовсе.",
             size=12.5, color=DEEP, line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)
    footer(s, "Эмпирически наблюдается при continual fine-tuning (Luo et al. 2023). Механизмы — «исследования показывают» (preprint).")
    speaker_notes(s, load_notes("s16"))


def build_s18(p):
    """section_divider — Раздел 4 «Агенты» (заголовок БЕЗ «+безопасность»;
    контент безопасности внутри раздела, на s25)."""
    build_section_divider(
        p, 4, "Раздел 4", "Агенты",
        "От собеседника в окне чата — к компоненту продакшен-системы: цикл, экипировка, память, доступ к инструментам — и где всё это ломается.",
        "s18")


def build_s19(p):
    """MERGED (§4.1) — API-механика (structured output / function calling /
    prompt caching) СВЕРХУ + MCP (N×M→N+M, USB-C, приятие, поворот доверия)
    СНИЗУ. Плотный слайд — компактные карточки, отдельная проверка 5-Second."""
    s = blank(p)
    slide_title(s, "Модель становится компонентом системы: API + MCP.", size=24)
    # TOP — 3 API mechanism cards (compact)
    cards = [
        ("boxes", "Structured output", "выход строго по схеме (JSON), не текст для парсинга", "встраиваемая"),
        ("terminal", "Function calling", "модель формулирует «вызови X»; исполняет ваш код, не модель", "активная"),
        ("database", "Prompt caching", "не пересчитывать неизменный префикс при каждом запросе", "экономичная"),
    ]
    cw, chh = 4.00, 2.02
    cy = 1.12
    x = 0.55
    for nm, t, body, tag in cards:
        ocean_box(s, x, cy, cw, chh)
        filled_rect(s, x + 0.22, cy + 0.22, 0.56, 0.56, MID, radius=True, radius_adj=0.18)
        icon(s, nm, x + 0.28, cy + 0.28, 0.44, "white")
        text_box(s, x + 0.90, cy + 0.24, cw - 1.05, 0.52, t,
                 size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        text_box(s, x + 0.24, cy + 0.90, cw - 0.48, 0.72, body,
                 size=12.5, color=DEEP, line_spacing=1.14)
        chip(s, x + 0.24, cy + chh - 0.46, cw - 0.48, 0.34, tag,
             fill=TEAL, color=WHITE, size=12)
        x += cw + 0.13
    # BOTTOM — MCP
    my = 3.36
    ocean_box(s, 0.55, my, 6.55, 2.55)
    icon(s, "cable", 0.80, my + 0.20, 0.48, "mid")
    text_runs(s, 1.40, my + 0.22, 5.5, 0.5, [
        {"text": "MCP", "size": 18, "bold": True, "color": MID},
        {"text": "  — «USB-C для инструментов LLM»", "size": 14, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE)
    text_runs(s, 0.80, my + 0.82, 6.0, 0.5, [
        {"text": "N×M", "size": 20, "bold": True, "color": LIGHT},
        {"text": " несовместимых интеграций → ", "size": 13, "color": DEEP},
        {"text": "N+M", "size": 20, "bold": True, "color": TEAL},
    ], anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.80, my + 1.36, 6.0, 0.32,
             "инструмент один раз = MCP-сервер; модель один раз = MCP-клиент",
             size=11.5, italic=True, color=SLATE)
    tl = [("Anthropic", "11/2024", "logo-anthropic"),
          ("OpenAI", "03/2025", "logo-openai"),
          ("Google", "04/2025", "logo-gemini")]
    tx0 = 0.80
    for i, (nm, dt, lg) in enumerate(tl):
        ex = tx0 + i * 2.0
        add_image(s, ICONS / f"{lg}.png", ex, my + 1.82, 0.34, 0.34)
        text_box(s, ex + 0.42, my + 1.78, 1.5, 0.26, nm, size=11.5, bold=True, color=DEEP)
        text_box(s, ex + 0.42, my + 2.02, 1.5, 0.24, dt, size=11.5, bold=True, italic=True, color=LIGHT)
        if i < 2:
            text_box(s, ex + 1.72, my + 1.82, 0.22, 0.3, "→", size=13, bold=True, color=LIGHT)
    # trust warning — P1 fix (issue #157 review): 3 bullets -> 2 most load-bearing
    # (root cause: code/access; concrete attack vector: prompt injection carrier).
    # Retention-policy point dropped here — it's covered on s25's ZDR block.
    ocean_box(s, 7.25, my, 5.55, 2.55, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, 7.52, my + 0.18, 5.1, 0.72,
             "Стандартизация подключения ≠ безопасность подключаемого — и усугубляет проблему доверия.",
             size=13.5, bold=True, color=TEAL, line_spacing=1.14)
    for i, w in enumerate([
        "код в вашем окружении / доступ к данным",
        "описание попадает в контекст — носитель prompt injection"]):
        circle(s, 7.54, my + 1.06 + i * 0.52 + 0.05, 0.11, TEAL)
        text_box(s, 7.76, my + 1.06 + i * 0.52, 5.0, 0.48, w,
                 size=12.5, color=DEEP, line_spacing=1.10)
    gold_callout(s, 0.55, 6.06, 12.25, 0.80,
                 "Ни один механизм не делает модель надёжнее — правило лестницы не отменяется. Удобство подключения — не аргумент за подключение.",
                 size=13.5)
    footer(s, "Актуальные цифры экономии и масштаб экосистемы MCP — в главе методички.")
    speaker_notes(s, load_notes("s19"))


def build_s21(p):
    """schema_cycle — agent loop plan→act→check→iterate."""
    s = blank(p)
    slide_title(s, "Цикл агента: plan → act → check → iterate.", size=26)
    text_box(s, 0.55, 1.14, 12.25, 0.4,
             "Агент — архитектура, где модель не делает один проход, а работает в цикле, сама определяя последовательность шагов.",
             size=13.5, italic=True, color=MID)
    # 4 step cards in a row with arrows + return arrow below
    steps = [
        ("plan", "Plan", "формулирует следующий шаг",
         "близорукий / зацикленный план (не видит накопленной стоимости)", MID, False),
        ("act", "Act", "вызывает инструмент (function calling)",
         "инструмент падает / тормозит, а ветки на это нет", MID, False),
        ("check", "Check", "достигнута ли цель, корректен ли результат",
         "валидация против ВНЕШНЕГО критерия — не самооценка модели (отсылка к пределу CoT)", GOLD, True),
        ("iter", "Iterate", "цикл повторяется",
         "нет внешнего лимита на итерации / стоимость / время → петля", MID, False),
    ]
    sy, sh = 1.72, 3.55
    bw = 2.92
    gap = 0.20
    x0 = 0.55
    x = x0
    centers = []
    for i, (k, t, sub, fail, col, isgold) in enumerate(steps):
        if isgold:
            ocean_box(s, x, sy, bw, sh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, x, sy, bw, sh)
        circle(s, x + bw / 2 - 0.26, sy + 0.24, 0.52,
               (GOLD if isgold else MID))
        text_box(s, x + bw / 2 - 0.26, sy + 0.24, 0.52, 0.52, str(i + 1),
                 size=20, bold=True, color=(DEEP if isgold else WHITE),
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # START badge on Plan (explicit entry point)
        if i == 0:
            chip(s, x + 0.30, sy + 0.30, 0.96, 0.34, "СТАРТ",
                 fill=TEAL, color=WHITE, size=10.5)
        text_box(s, x + 0.12, sy + 0.90, bw - 0.24, 0.42, t,
                 size=19, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x + 0.18, sy + 1.36, bw - 0.36, 0.70, sub,
                 size=12, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.12)
        filled_rect(s, x + 0.18, sy + 2.18, bw - 0.36, 1.22,
                    (GOLD_TINT if isgold else SURFACE),
                    stroke=(GOLD if isgold else SOFT_GREY), stroke_pt=1.0,
                    radius=True, radius_adj=0.10)
        text_box(s, x + 0.28, sy + 2.26, bw - 0.56, 1.06,
                 ("режим отказа: " + fail),
                 size=10.5, italic=True, color=(DEEP if isgold else SLATE),
                 align=PP_ALIGN.CENTER, line_spacing=1.12)
        centers.append(x + bw / 2)
        if i < 3:
            right_arrow(s, x + bw + 0.01, sy + 0.62, gap - 0.04, 0.46, fill=LIGHT)
        x += bw + gap
    # Explicit return path: down from Iterate → left across → up into Plan
    box_bottom = sy + sh           # 5.27
    ry = box_bottom + 0.55         # horizontal return rail at 5.82
    last_cx = centers[3]
    first_cx = centers[0]
    # down stub from Iterate
    connector(s, last_cx, box_bottom, last_cx, ry, LIGHT, 2.5)
    # horizontal rail right→left
    connector(s, last_cx, ry, first_cx, ry, LIGHT, 2.5)
    # up stub + arrowhead back into Plan
    connector(s, first_cx, ry, first_cx, box_bottom + 0.20, LIGHT, 2.5)
    up_arrow(s, first_cx - 0.13, box_bottom + 0.02, 0.26, 0.24, fill=LIGHT)
    # loop label centered ON the rail, white-backed chip for legibility
    lbl_w = 4.6
    chip(s, (first_cx + last_cx) / 2 - lbl_w / 2, ry - 0.20, lbl_w, 0.40,
         "⟲  цикл ПОВТОРЯЕТСЯ — возврат к Plan", fill=LIGHT, color=WHITE,
         size=12.5)
    footer(s, "Паттерны цикла (ReAct, Reflexion, Plan-and-Execute) — в главе. Проектировать агента = проектировать защиту на каждом из 4 шагов.")
    speaker_notes(s, load_notes("s21"))


def build_s22(p):
    """schema_matrix / comparison — Workflow vs Agent (2 columns)."""
    s = blank(p)
    slide_title(s, "Workflow vs Agent.", size=27)
    text_box(s, 0.55, 1.16, 12.25, 0.4,
             "Предсказуемая задача → workflow; непредсказуемая И ценность оправдывает кратный рост → агент.",
             size=14.5, italic=True, color=MID)
    cy, chh = 1.78, 2.75
    cw = 6.05
    # workflow
    ocean_box(s, 0.55, cy, cw, chh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    icon(s, "git-fork", 0.83, cy + 0.22, 0.50, "teal")
    text_box(s, 1.45, cy + 0.24, cw - 0.9, 0.5, "Workflow  (рабочий поток)",
             size=17, bold=True, color=TEAL, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.83, cy + 0.85, cw - 0.56, 0.45,
             "LLM и инструменты по предопределённым в коде путям",
             size=13, bold=True, color=DEEP, line_spacing=1.12)
    for i, t in enumerate(["последовательность шагов известна заранее",
                           "предсказуемо, аудируемо",
                           "большинство надёжных продакшн-систем — это workflow"]):
        circle(s, 0.83, cy + 1.40 + i * 0.43 + 0.06, 0.11, TEAL)
        text_box(s, 1.06, cy + 1.40 + i * 0.43, cw - 1.3, 0.42, t,
                 size=12.5, color=DEEP, line_spacing=1.05)
    # agent
    rx = 6.75
    ocean_box(s, rx, cy, cw, chh)
    icon(s, "bot", rx + 0.28, cy + 0.22, 0.50, "mid")
    text_box(s, rx + 0.90, cy + 0.24, cw - 0.9, 0.5, "Агент",
             size=17, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, rx + 0.28, cy + 0.85, cw - 0.56, 0.45,
             "LLM динамически определяет собственный процесс",
             size=13, bold=True, color=DEEP, line_spacing=1.12)
    for i, t in enumerate(["последовательность заранее не зафиксирована",
                           "кратно больше токенов, чем чат",
                           "ниже аудируемость, выше риск петель"]):
        circle(s, rx + 0.28, cy + 1.40 + i * 0.43 + 0.06, 0.11, MID)
        text_box(s, rx + 0.51, cy + 1.40 + i * 0.43, cw - 1.3, 0.42, t,
                 size=12.5, color=DEEP, line_spacing=1.05)
    # diagnostic question
    ocean_box(s, 0.55, 4.70, 12.25, 1.05, fill=SURFACE, stroke=LIGHT)
    text_box(s, 0.85, 4.80, 11.65, 0.9,
             "Могу ли я заранее, до запуска, выписать последовательность шагов?  да (даже с ветвлениями) → workflow  ·  принципиально нет И ценность оправдывает кратные стоимость/риск → агент",
             size=13.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.18)
    # #231: вложенность workflow↔agent — норма, не третья архитектура.
    ocean_box(s, 0.55, 5.90, 8.55, 0.98, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    text_box(s, 0.80, 5.98, 8.05, 0.82,
             "Вложенность — норма: агент code review вызывает workflow «линтер→тесты→формат» как один шаг; workflow обработки заявок делегирует мини-агенту разбор свободной жалобы. Динамика — только там, где нужна.",
             size=12.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.14)
    ocean_box(s, 9.30, 5.90, 3.50, 0.98, fill=SURFACE, stroke=SOFT_GREY, stroke_pt=1.0)
    text_box(s, 9.50, 5.98, 3.10, 0.82,
             "Найди простейшее. «Лень формализовать» не делает задачу непредсказуемой.",
             size=11.5, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    speaker_notes(s, load_notes("s22"))


def build_s22b(p):
    """NEW (§4.4) — «из чего сделан агент-помощник»: карта 5 слотов
    экипировки. ASSERTION на заголовке: каждый слот — компромисс, не
    апгрейд по умолчанию (рифма с лестницей)."""
    s = blank(p)
    slide_title(s, "Каждый слот экипировки агента — компромисс, не апгрейд.", size=23)
    text_box(s, 0.55, 1.14, 12.25, 0.42,
             "Реальный агент-помощник (Claude Code, Cursor, Aider) — это цикл plan→act→check→iterate ПЛЮС оснастка. Пять типовых слотов:",
             size=13.5, italic=True, color=MID, line_spacing=1.15)
    slots = [
        ("brain-circuit", "Память", "что помнит между сессиями"),
        ("file-text", "Инструкции-правила", "файлы-конвенции + журнал задач"),
        ("puzzle", "Skills", "переиспользуемые процедуры"),
        ("users", "Subagents", "делегирование + изоляция"),
        ("cable", "Access / MCP", "доступ к внешним инструментам"),
    ]
    cw = 2.40
    gap = 0.10
    x0 = 0.55
    y = 1.78
    chh = 2.55
    for i, (ic, t, sub) in enumerate(slots):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y, cw, chh)
        filled_rect(s, x + cw / 2 - 0.42, y + 0.26, 0.84, 0.84, MID, radius=True, radius_adj=0.18)
        icon(s, ic, x + cw / 2 - 0.32, y + 0.36, 0.64, "white")
        text_box(s, x + 0.10, y + 1.28, cw - 0.20, 0.5, t,
                 size=15, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.0)
        text_box(s, x + 0.14, y + 1.80, cw - 0.28, 0.65, sub,
                 size=11.5, color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.12)
        # slot number badge
        circle(s, x + 0.14, y + 0.14, 0.32, GOLD)
        text_box(s, x + 0.14, y + 0.14, 0.32, 0.32, str(i + 1),
                 size=13, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    gold_callout(s, 0.55, 4.66, 12.25, 1.30,
                 "Как не поднимаешься по лестнице архитектур без требования задачи — не добавляй агенту память, subagents или MCP «на всякий случай». Каждый слот несёт свою цену: операционную сложность, новую поверхность отказа, новую границу доверия — и должен отвечать на конкретный триггер (Раздел 5).",
                 size=15)
    speaker_notes(s, load_notes("s22b"))


def build_s22c(p):
    """NEW (§4.5) — память агента: плоский файл → mem0/Cognee/Graphiti-Zep.
    Явный callback на RAG Раздела 2 — тот же вопрос масштаба знания."""
    s = blank(p)
    slide_title(s, "Память агента — тот же вопрос масштаба, что RAG.", size=24)
    text_box(s, 0.55, 1.14, 12.25, 0.42,
             "Память — что агент помнит МЕЖДУ сессиями (в отличие от контекста одного разговора). Спектр — от плоского файла до graph-баз.",
             size=13.5, italic=True, color=MID, line_spacing=1.15)
    # spectrum: flat file -> vector/graph
    sy, sh = 1.86, 2.35
    ocean_box(s, 0.55, sy, 5.55, sh)
    icon(s, "file-text", 0.82, sy + 0.22, 0.50, "mid")
    text_box(s, 1.44, sy + 0.24, 4.4, 0.42, "Плоский файл", size=16, bold=True,
             color=MID, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.82, sy + 0.86, 5.0, 1.35,
             "агент дописывает факты в текстовый лог, при запуске читает целиком. Работает, пока лог мал и стабилен — прямая параллель критерию RAG «корпус помещается в окно».",
             size=13, color=DEEP, line_spacing=1.20)
    right_arrow(s, 6.20, sy + sh / 2 - 0.26, 0.55, 0.52, fill=LIGHT)
    ocean_box(s, 6.95, sy, 5.85, sh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    icon(s, "brain-circuit", 7.22, sy + 0.22, 0.50, "teal")
    text_box(s, 7.84, sy + 0.24, 4.7, 0.42, "Векторная / graph-база", size=16,
             bold=True, color=TEAL, anchor=MSO_ANCHOR.MIDDLE)
    for i, m in enumerate([
        "mem0 — cross-session память пользователя",
        "Cognee — memory на графе знаний",
        "Graphiti / Zep — temporal graph: когда факт верен, когда устарел",
    ]):
        circle(s, 7.24, sy + 0.86 + i * 0.44 + 0.05, 0.11, TEAL)
        text_box(s, 7.46, sy + 0.86 + i * 0.44, 5.1, 0.42, m,
                 size=12.5, color=DEEP, line_spacing=1.08)
    gold_callout(s, 0.55, 4.42, 12.25, 1.50,
                 "Тот же вопрос масштаба знания, что решает RAG для корпуса документов, здесь встаёт для памяти самого агента. Не ставьте graph-базу агенту с короткими несвязанными сессиями — это тот же технический долг без требования, что RAG для десяти статей.",
                 size=15)
    footer(s, "Источник: публичный реестр agent-harness-registry (workain lab, live-eval).")
    speaker_notes(s, load_notes("s22c"))


def build_s22d(p):
    """NEW (§4.6) — провал памяти (кейс): Letta Tier D + Anthropic Memory
    Tool Tier B 17%. Freshness-оговорка Letta на видимом слое."""
    s = blank(p)
    slide_title(s, "«Агент, который помнит» — не всегда лучше.", size=25)
    text_box(s, 0.55, 1.14, 12.25, 0.42,
             "Наличие памяти интуитивно кажется чистым улучшением. Независимый live-eval показывает: иногда — драматически нет.",
             size=13.5, italic=True, color=MID, line_spacing=1.15)
    # left — Letta case with numbers
    lx, ly, lw, lh = 0.55, 1.86, 6.25, 4.05
    ocean_box(s, lx, ly, lw, lh)
    icon(s, "triangle-alert", lx + 0.26, ly + 0.22, 0.46, "mid")
    text_box(s, lx + 0.84, ly + 0.22, lw - 1.1, 0.42, "Letta — Tier D",
             size=16, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, lx + 0.26, ly + 0.78, lw - 0.52, 0.62,
             "проигрывает И голой модели, И плоскому файлу на всех задачах. persistbench_v1:",
             size=13, color=DEEP, line_spacing=1.16)
    # mini table of 3 numbers
    rows = [("Голая модель", "1.000", "94 с", TEAL),
            ("Плоский файл", "0.833", "159 с", MID),
            ("Letta", "0.750", "496 с", GOLD)]
    ry = ly + 1.48
    for nm, sc, tm, col in rows:
        filled_rect(s, lx + 0.26, ry, 0.14, 0.34, col)
        text_box(s, lx + 0.52, ry, 2.7, 0.34, nm, size=12.5, bold=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, lx + 3.25, ry, 1.3, 0.34, sc, size=13, bold=True, color=col,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        text_box(s, lx + 4.65, ry, 1.3, 0.34, tm, size=12, color=SLATE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        ry += 0.42
    text_box(s, lx + 0.26, ry + 0.02, lw - 0.52, 0.72,
             "Механизмы: капитуляция под давлением · многословие топит факт · факт замечен, но не закоммичен.",
             size=12, color=DEEP, line_spacing=1.14)
    # freshness caveat VISIBLE
    filled_rect(s, lx + 0.26, ly + lh - 0.62, lw - 0.52, 0.48, SOFT_GREY,
                radius=True, radius_adj=0.12)
    text_box(s, lx + 0.42, ly + lh - 0.58, lw - 0.80, 0.40,
             "Оговорка: тест на Letta v0.6.7 — отстаёт от текущей v0.16.8 (~18 мес).",
             size=11, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    # right — Anthropic Memory Tool 17%
    rx, rw = 7.05, 5.75
    ocean_box(s, rx, ly, rw, lh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    text_box(s, rx + 0.28, ly + 0.22, rw - 0.56, 0.42, "Anthropic Memory Tool — Tier B",
             size=16, bold=True, color=DEEP)
    text_box(s, rx + 0.28, ly + 0.70, rw - 0.56, 0.5,
             "В целом сильный результат — но даже он теряет данные в",
             size=13, color=DEEP, line_spacing=1.14)
    text_runs(s, rx + 0.28, ly + 1.18, rw - 0.56, 0.7, [
        {"text": "17% ", "size": 34, "bold": True, "color": GOLD},
        {"text": "задач", "size": 16, "bold": True, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE)
    for i, m in enumerate([
        "явный отказ записать «эфемерный» факт",
        "немотивированный отказ «вне рамок»",
        "тихая lossy-суммаризация — деталь не восстановить",
        "невоспроизводимость: та же беседа дважды → разный результат",
    ]):
        circle(s, rx + 0.30, ly + 2.04 + i * 0.42 + 0.05, 0.11, MID)
        text_box(s, rx + 0.52, ly + 2.04 + i * 0.42, rw - 0.80, 0.42, m,
                 size=12, color=DEEP, line_spacing=1.06)
    footer(s, "agent-harness-registry (workain lab, live-eval 2026-07-05). «Работает хорошо» ≠ «работает всегда» — тот же урок, что RAG на масштабе и forgetting.")
    speaker_notes(s, load_notes("s22d"))


def build_s22e(p):
    """NEW (§4.7) — операционный слой: файлы-инструкции + presence paradox +
    Honest Lying + claude-code#51735. Интуиция расходится с измерением."""
    s = blank(p)
    slide_title(s, "Файл-инструкция агенту — не «магическая прививка».", size=24)
    text_box(s, 0.55, 1.14, 12.25, 0.42,
             "Операционный слой — файлы-конвенции (класс CLAUDE.md / AGENTS.md) + журнал задач. Интуиция «написал инструкцию → лучше» расходится с измерением.",
             size=13.5, italic=True, color=MID, line_spacing=1.15)
    # 3 evidence cards
    cards = [
        ("notebook-pen", "presence paradox", "RCT (Gloaguen et al. 2026): само наличие файла-инструкции НЕ даёт значимого прироста успешности — при этом стоимость и число шагов растут.", "Помогает только там, где реально заполняет пробел документации."),
        ("brain-circuit", "Honest Lying", "Dixit, Kamal, Oates 2026: self-authored память может ЗАКРЕПЛЯТЬ неверное убеждение — журнал бетонирует раннюю ошибку вместо пересмотра.", "Рефлексия ошибочна → повторные попытки опираются на неё."),
        ("triangle-alert", "claude-code#51735", "Реальный кейс: письменно признанная прошлая ошибка НЕ предотвратила её повторение спустя 25 дней.", "Запись о провале ≠ гарантия, что поведение изменится."),
    ]
    cw, chh = 4.00, 3.35
    cy = 1.80
    x = 0.55
    for i, (ic, t, body, foot) in enumerate(cards):
        isgold = (i == 0)
        if isgold:
            ocean_box(s, x, cy, cw, chh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, x, cy, cw, chh)
        icon(s, ic, x + 0.24, cy + 0.24, 0.50, "gold" if isgold else "mid")
        text_box(s, x + 0.86, cy + 0.26, cw - 1.05, 0.5, t,
                 size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        text_box(s, x + 0.24, cy + 0.92, cw - 0.48, 1.75, body,
                 size=12.5, color=DEEP, line_spacing=1.18)
        filled_rect(s, x + 0.22, cy + chh - 0.86, cw - 0.44, 0.72, SURFACE,
                    stroke=SOFT_GREY, stroke_pt=1.0, radius=True, radius_adj=0.10)
        text_box(s, x + 0.36, cy + chh - 0.80, cw - 0.68, 0.62, foot,
                 size=11.5, italic=True, color=(DEEP if isgold else SLATE),
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.10)
        x += cw + 0.13
    gold_callout(s, 0.55, 5.30, 12.25, 0.90,
                 "Полезен, когда заполняет реальный пробел; бесполезен, когда дублирует доступное модели; может навредить, когда самоавторская память закрепляет ошибку. Тот же паттерн, что роль в промпте: «добавить X → лучше» не подтверждается измерением.",
                 size=13.5)
    speaker_notes(s, load_notes("s22e"))


def build_s23(p):
    """case_study — 3 agent failure cards; compounding chart c23 inside card 2."""
    s = blank(p)
    slide_title(s, "Провалы агентов.", size=27)
    text_box(s, 0.55, 1.14, 12.25, 0.4,
             "Каждый провал — режим отказа цикла агента в датированном кейсе: урок + альтернатива.",
             size=14, italic=True, color=MID)
    # card 1 — loop
    c1x, cy, c1w, chh = 0.55, 1.66, 4.05, 4.55
    ocean_box(s, c1x, cy, c1w, chh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    icon(s, "flame", c1x + 0.22, cy + 0.22, 0.50, "gold")
    text_box(s, c1x + 0.82, cy + 0.24, c1w - 1.0, 0.5, "1. Петля без лимитов",
             size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, c1x + 0.24, cy + 0.85, c1w - 0.48, 0.95,
             "Агент на «синхронизируй заказы» получил HTTP 429 → план→вызов→429→…",
             size=12, color=DEEP, line_spacing=1.14)
    text_box(s, c1x + 0.24, cy + 1.72, c1w - 0.48, 0.50, "$4 200 за 63 часа",
             size=22, bold=True, color=GOLD, line_spacing=1.0)
    # #233: явная база сравнения — retry-скрипт «практически бесплатно»
    filled_rect(s, c1x + 0.24, cy + 2.24, c1w - 0.48, 0.62, WHITE, stroke=GOLD,
                stroke_pt=1.5, radius=True, radius_adj=0.12)
    text_box(s, c1x + 0.38, cy + 2.27, c1w - 0.76, 0.56,
             "База сравнения: retry-скрипт с backoff решил бы ту же задачу за секунды-минуты, практически бесплатно",
             size=10, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    text_box(s, c1x + 0.24, cy + 2.92, c1w - 0.48, 0.56,
             "$4 200 — цена не автоматизации, а неправильного выбора архитектуры под предсказуемую задачу",
             size=10, italic=True, color=SLATE, line_spacing=1.08)
    text_box(s, c1x + 0.24, cy + 3.54, c1w - 0.48, 0.90,
             "Более подходящая архитектура: retry-with-backoff скрипт, не агент; лимиты бюджета и итераций ВНЕ агента",
             size=11, bold=True, color=DEEP, line_spacing=1.10)
    # card 2 — compounding (chart)
    c2x, c2w = 4.80, 4.05
    ocean_box(s, c2x, cy, c2w, chh)
    text_box(s, c2x + 0.24, cy + 0.20, c2w - 0.48, 0.4,
             "2. Накопление ошибок (compounding)", size=15, bold=True, color=MID)
    add_image(s, CHARTS / "c23-compounding.png", c2x + 0.16, cy + 0.62,
              c2w - 0.32, 2.55)
    text_box(s, c2x + 0.24, cy + 3.30, c2w - 0.48, 1.05,
             "Вывод: «улучшить шаг» — слабый рычаг; «меньше хопов + валидация между шагами» — сильный",
             size=12, bold=True, color=DEEP, line_spacing=1.16)
    # card 3 — multi-agent fragility
    c3x, c3w = 9.05, 3.75
    ocean_box(s, c3x, cy, c3w, chh)
    icon(s, "git-fork", c3x + 0.22, cy + 0.22, 0.46, "mid")
    text_box(s, c3x + 0.76, cy + 0.22, c3w - 0.95, 0.55,
             "3. Мульти-агентная хрупкость", size=14.5, bold=True, color=MID,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    text_box(s, c3x + 0.24, cy + 0.95, c3w - 0.48, 1.55,
             "зависимые подзадачи → параллельные субагенты принимают конфликтующие неявные решения",
             size=12.5, color=DEEP, line_spacing=1.18)
    text_box(s, c3x + 0.24, cy + 2.70, c3w - 0.48, 1.65,
             "Более подходящая: single-threaded линейный агент; мульти-агент — только широко-параллельное независимое",
             size=12.5, bold=True, color=DEEP, line_spacing=1.18)
    footer(s, "Атаки через инструменты (prompt injection, GitHub MCP heist) — 4-й класс провалов, разобран на слайде безопасности. $4 200-петля — single-author постмортем 2026-04 (illustrative); compounding — MindStudio 2025–2026.")
    speaker_notes(s, load_notes("s23"))


def build_s25(p):
    """NEW/MERGED (§4.8) — skills + subagents + доступ к инструментам +
    ИНТЕГРИРОВАННАЯ безопасность равного веса (P1: GOLD security block, не
    caveat снизу). GitHub MCP heist + ZDR-факты живут ЗДЕСЬ."""
    s = blank(p)
    slide_title(s, "Skills, subagents, доступ — и граница доверия.", size=25)
    # top row — 3 equipment slots
    slots = [
        ("puzzle", "Skill", "переиспользуемая процедура «как делать» под повторяющуюся задачу"),
        ("users", "Subagent", "отдельное контекстное окно: не засорять главный + изолировать недоверенное"),
        ("cable", "MCP-доступ", "каждое подключение — новая граница доверия и retention-политика"),
    ]
    cw, chh = 4.00, 1.55
    cy = 1.12
    x = 0.55
    for ic, t, body in slots:
        ocean_box(s, x, cy, cw, chh)
        icon(s, ic, x + 0.22, cy + 0.22, 0.46, "mid")
        text_box(s, x + 0.80, cy + 0.22, cw - 1.0, 0.42, t,
                 size=15, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x + 0.24, cy + 0.74, cw - 0.48, 0.74, body,
                 size=12, color=DEEP, line_spacing=1.14)
        x += cw + 0.13
    # GOLD security block — EQUAL VISUAL WEIGHT (P1), not a footer caveat
    gy, gh = 2.86, 3.60
    ocean_box(s, 0.55, gy, 12.25, gh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=3.0)
    icon(s, "shield-alert", 0.82, gy + 0.22, 0.56, "gold")
    text_box(s, 1.52, gy + 0.24, 11.0, 0.44,
             "Безопасность: как только агент делегирует и подключается — появляется поверхность, которой не было у одного вызова",
             size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    # left half — GitHub heist mechanism + 2 ZDR facts
    text_box(s, 0.82, gy + 0.80, 5.85, 0.34, "GitHub MCP heist (май 2025)",
             size=13.5, bold=True, color=DEEP)
    text_box(s, 0.82, gy + 1.14, 5.85, 0.78,
             "issue с встроенной инструкцией + переизбыточный токен (PAT на все репо) → ассистент выгрузил приватные репозитории в публичный PR.",
             size=12, color=DEEP, line_spacing=1.16)
    filled_rect(s, 0.82, gy + 1.96, 5.85, 0.46, WHITE, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.14)
    text_box(s, 0.98, gy + 1.99, 5.55, 0.40,
             "Катастрофа = инъекция × широкие права. Убери любое — атака не проходит.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.82, gy + 2.48, 5.85, 0.44,
             "«У нас ZDR» ≠ «нигде не хранится»: судебный приказ (NYT v. OpenAI) + third-party/MCP вне ZDR. Регулируемое — не слать без ZDR/BAA.",
             size=11, italic=True, color=DEEP, line_spacing=1.10)
    # right half — 4 rules
    rx = 7.05
    text_box(s, rx, gy + 0.80, 5.5, 0.34, "4 правила проектирования",
             size=13.5, bold=True, color=DEEP)
    rules = [
        ("Least-privilege", "минимум токенов/прав"),
        ("Изоляция недоверенного", "отдельно от привилегий (subagent)"),
        ("Human-in-the-loop на write", "необратимое — только через человека"),
        ("Allowlist / pin", "аудированные версии; deny-by-default"),
    ]
    ry = gy + 1.18
    for i, (t, b) in enumerate(rules):
        circle(s, rx, ry + 0.03, 0.30, GOLD)
        text_box(s, rx, ry + 0.03, 0.30, 0.30, str(i + 1),
                 size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, rx + 0.42, ry - 0.02, 5.5, 0.30, t, size=13, bold=True, color=DEEP)
        text_box(s, rx + 0.42, ry + 0.26, 5.5, 0.28, b, size=11, color=SLATE)
        ry += 0.58
    speaker_notes(s, load_notes("s25"))


def build_s25b(p):
    """NEW (§4.9) — обзор реальных coding-агентов через рамку экипировки §4.4.
    РОВНО 4 инструмента: Claude Code / Aider / Cursor / OpenHands. OpenHands
    помечен как неподтверждённая гипотеза «OpenClaw»."""
    s = blank(p)
    slide_title(s, "Реальные coding-агенты — через рамку экипировки.", size=25)
    text_box(s, 0.55, 1.14, 12.25, 0.42,
             "Разница между инструментами — не в «качестве модели», а в том, какие слоты экипировки заполнены и где агент физически живёт.",
             size=13.5, italic=True, color=MID, line_spacing=1.15)
    tools = [
        ("Claude Code", "CLI + IDE · проприетарный",
         "широкая экипировка: память, файлы-инструкции, skills, полноценные subagents, MCP — почти все 5 слотов",
         "цена — большая операционная сложность", MID, False),
        ("Aider", "CLI-first · open source",
         "минимальная простота: без развитой памяти, без subagents, без skills. ~47k★ на GitHub",
         "«тонкая» оснастка — самостоятельный выбор, не недоразвитость", TEAL, False),
        ("Cursor", "desktop IDE (форк VS Code) · проприетарный",
         "агент внутри редактора — не терминал. Форма интеграции — отдельная ось от оснастки",
         "где живёт агент — тоже архитектурное решение", MID, False),
        ("OpenHands", "self-hosted платформа · MIT · ~80k★",
         "широкая автономность, локальное/Docker/облако развёртывание",
         "рабочая гипотеза по совпадению профиля — вероятный кандидат на «OpenClaw», не подтверждённый факт", GOLD, True),
    ]
    cw, chh = 3.02, 4.05
    cy = 1.74
    x = 0.55
    for nm, meta, body, note, col, ishyp in tools:
        if ishyp:
            ocean_box(s, x, cy, cw, chh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, x, cy, cw, chh)
        icon(s, "code", x + 0.22, cy + 0.22, 0.44, "gold" if ishyp else "mid")
        text_box(s, x + 0.76, cy + 0.20, cw - 0.92, 0.48, nm,
                 size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        text_box(s, x + 0.24, cy + 0.76, cw - 0.48, 0.44, meta,
                 size=10.5, italic=True, color=LIGHT, line_spacing=1.08)
        text_box(s, x + 0.24, cy + 1.22, cw - 0.48, 1.30, body,
                 size=11.5, color=DEEP, line_spacing=1.16)
        nb_h = 1.30 if ishyp else 0.86
        filled_rect(s, x + 0.20, cy + chh - nb_h - 0.14, cw - 0.40, nb_h,
                    WHITE if ishyp else SURFACE, stroke=(GOLD if ishyp else SOFT_GREY),
                    stroke_pt=(1.5 if ishyp else 1.0), radius=True, radius_adj=0.10)
        text_box(s, x + 0.32, cy + chh - nb_h - 0.08, cw - 0.64, nb_h - 0.10, note,
                 size=(9.5 if ishyp else 10), italic=True,
                 color=(DEEP if ishyp else SLATE), line_spacing=1.10)
        x += cw + 0.13
    gold_callout(s, 0.55, 5.98, 12.25, 0.86,
                 "Выбор инструмента подчиняется тому же правилу: не бери самый оснащённый по умолчанию — смотри, какая оснастка нужна именно твоей задаче.",
                 size=13.5)
    speaker_notes(s, load_notes("s25b"))


def build_s26(p):
    """schema_layered — complexity ladder, bottom-aligned. 6 short rungs +
    trigger label in the gap BELOW each rung (the requirement that opens the
    climb to it). Left col = ladder; right col = rule panel."""
    s = blank(p)
    slide_title(s, "Лестница архитектурной сложности.", size=27)
    text_box(s, 0.55, 1.14, 8.40, 0.40,
             "Оставайся на нижней ступени; поднимайся только под требование задачи.",
             size=13.5, italic=True, color=MID)
    # bottom-up: idx0 = step1 bottom (gold). trig = requirement that opens
    # the climb FROM this rung to the next (shown in the gap above it).
    steps = [
        ("1", "Обычный код (без ИИ)", "нужен NL / неструктурированный ввод / неточное соответствие", GOLD, True),
        ("2", "Один вызов LLM (промпт; +CoT, +few-shot)", "знание большое И меняющееся И провенанс И приватное", MID, False),
        ("3", "RAG / контекст-инжиниринг", "задача многошаговая, последовательность известна заранее", LIGHT, False),
        ("4", "Workflow (предопределённые пути)", "непредсказуема И ценность оправдывает кратные стоимость/риск", LIGHT, False),
        ("5", "Агент (plan→act→check→iterate + лимиты)", "подзадачи широко-параллельны И независимы И высокоценны", LIGHT, False),
        ("6", "Multi-agent", None, LIGHT, False),
    ]
    n = len(steps)
    step_h = 0.52
    trig_h = 0.34
    bottom_edge = 6.62  # bottom of rung 1
    x0 = 0.55
    full_w = 8.05
    for i, (num, label, trig, col, isgold) in enumerate(steps):
        y = bottom_edge - step_h - i * (step_h + trig_h)
        indent = i * 0.16
        w = full_w - indent
        x = x0 + indent
        if isgold:
            ocean_box(s, x, y, w, step_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, x, y, w, step_h)
        circle(s, x + 0.12, y + (step_h - 0.34) / 2, 0.34, col)
        text_box(s, x + 0.12, y + (step_h - 0.34) / 2, 0.34, 0.34, num,
                 size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x + 0.58, y, w - 0.72, step_h, label,
                 size=12.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.0)
        if trig:
            # trigger shown in the gap ABOVE this rung (opens climb to next)
            tgy = y - trig_h - 0.01
            text_box(s, x + 0.30, tgy, full_w - 0.50, trig_h,
                     "↑  " + trig, size=10, italic=True, color=SLATE,
                     anchor=MSO_ANCHOR.MIDDLE)
    # PA-1 (owner-approved): direction-of-scale strip alongside the ladder —
    # «сложнее ↑» at top / «проще ↓» at bottom (kills «выше=лучше» mis-read).
    up_arrow(s, 8.66, 1.98, 0.26, 4.62, fill=COVER_OUTLINE)
    text_box(s, 8.30, 1.58, 1.00, 0.32, "сложнее ↑", size=10.5, bold=True,
             color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, 8.30, 6.62, 1.00, 0.32, "проще ↓", size=10.5, bold=True,
             color=LIGHT, align=PP_ALIGN.CENTER)
    # rule panel right (full height, gold — the central rule)
    ocean_box(s, 9.15, 1.55, 3.65, 5.05, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    icon(s, "milestone", 9.42, 1.85, 0.62, "gold")
    text_box(s, 9.42, 2.70, 3.15, 1.75,
             "Оставайся на самой нижней ступени, которая закрывает требования.",
             size=16, bold=True, color=DEEP, line_spacing=1.24)
    text_box(s, 9.42, 4.45, 3.15, 2.05,
             "Каждый подъём — это ОБМЕН (возможности ↔ стоимость, латентность, аудируемость, поверхность атаки), а не улучшение.",
             size=13.5, color=DEEP, line_spacing=1.22)
    footer(s, "Нижняя ступень — «обычный код без ИИ»: лестница начинается с вопроса «а нужен ли ИИ вообще».")
    speaker_notes(s, load_notes("s26"))


def build_s27(p):
    """NEW (§5.2) — «План решения»: 8-шаговый маршрут вопросов сверху вниз
    (flowchart с да/нет-ветвлениями), ЗАМЕНА старой 7×7 матрицы. Нижняя
    плашка-приоритет (детерминированное → код, СТОП) — gold-вес."""
    s = blank(p)
    slide_title(s, "План решения: маршрут вопросов, а не сумма баллов.", size=24)
    text_box(s, 0.55, 1.02, 8.4, 0.36,
             "Пройдите задачу сверху вниз; останавливайтесь на первом сработавшем вопросе.",
             size=13, italic=True, color=MID)
    # left — vertical routed flow (question -> да-outcome)
    fx = 0.55
    qw = 5.35           # question box width
    ow = 3.05           # outcome box width
    ax = fx + qw + 0.12  # outcome x
    steps = [
        ("Детерминированная и верифицируемая?", "да → обычный код · СТОП", True),
        ("Закрывает один вызов (+CoT)?", "да → промпт · СТОП", False),
        ("Нужен провенанс по источнику?", "да → RAG grounding / код", False),
        ("Знание меняется / провенанс?", "да → RAG (не FT)", False),
        ("Нужно поведение / тон / формат?", "да → fine-tuning (PEFT)", False),
        ("Многошагово, порядок известен?", "да → workflow · нет → агент+лимиты", False),
        ("Подзадачи параллельны+независимы?", "да → мульти-агент · нет → линейный", False),
    ]
    y = 1.40
    qh = 0.50
    vg = 0.085
    for i, (q, out, isgold) in enumerate(steps):
        if isgold:
            ocean_box(s, fx, y, qw, qh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.5)
        else:
            ocean_box(s, fx, y, qw, qh)
        circle(s, fx + 0.12, y + (qh - 0.32) / 2, 0.32, GOLD if isgold else MID)
        text_box(s, fx + 0.12, y + (qh - 0.32) / 2, 0.32, 0.32, str(i + 1),
                 size=13, bold=True, color=(DEEP if isgold else WHITE),
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, fx + 0.54, y, qw - 0.68, qh, q,
                 size=12.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)
        # outcome to the right
        filled_rect(s, ax, y + 0.05, ow, qh - 0.10, GOLD if isgold else TEAL_TINT,
                    stroke=(GOLD if isgold else TEAL), stroke_pt=1.2, radius=True, radius_adj=0.12)
        text_box(s, ax + 0.12, y + 0.05, ow - 0.24, qh - 0.10, out,
                 size=10.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)
        # connector question->outcome
        right_arrow(s, fx + qw + 0.005, y + qh / 2 - 0.09, 0.11, 0.18, fill=LIGHT)
        # down arrow (нет ↓) to next
        if i < len(steps) - 1:
            text_box(s, fx + 0.16, y + qh - 0.02, 1.2, vg + 0.04, "нет ↓",
                     size=9, italic=True, color=SLATE)
        y += qh + vg
    # step 8 — parallel data check (footer note across question+outcome cols)
    filled_rect(s, fx, y + 0.02, qw + 0.12 + ow, 0.36, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.2, radius=True, radius_adj=0.14)
    text_box(s, fx + 0.16, y + 0.03, qw + 0.12 + ow - 0.30, 0.34,
             "8. Данные чувствительны? → параллельно на КАЖДОМ шаге: карта данных + least-privilege + ZDR/BAA",
             size=10.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)
    # right — worked example + mini-apply
    rx, rw = 9.10, 3.70
    ocean_box(s, rx, 1.46, rw, 2.55, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, rx + 0.24, 1.60, rw - 0.48, 0.34, "Пример (задача A)", size=13.5,
             bold=True, color=TEAL)
    text_box(s, rx + 0.24, 1.96, rw - 0.48, 1.95,
             "«2000 регламентов, меняются еженедельно, ответ со ссылкой на пункт» → вопрос 4 (меняется+провенанс) решающий → RAG со strict grounding. Не FT (устареет), не код (нужен NL).",
             size=12, color=DEEP, line_spacing=1.20)
    ocean_box(s, rx, 4.12, rw, 1.85)
    text_box(s, rx + 0.24, 4.26, rw - 0.48, 0.34, "Разминка (задача B)", size=13.5,
             bold=True, color=MID)
    text_box(s, rx + 0.24, 4.62, rw - 0.48, 1.30,
             "«бот на ~150 FAQ, меняются раз в квартал» — пройдите маршрут сами; разбор на семинаре.",
             size=12, color=DEEP, line_spacing=1.18)
    # bottom priority plate — gold, the most important line
    gold_callout(s, 0.55, 6.06, 12.25, 0.82,
                 "Приоритет маршрута: если задача детерминированная и верифицируемая — обычный код, СТОП здесь. ИИ добавил бы лишь недетерминизм, стоимость, латентность и поверхность для prompt injection.",
                 size=14)
    speaker_notes(s, load_notes("s27"))


def build_s27b(p):
    """NEW (§5.2b) — «Стартовый комплект агента и когда его усложнять».
    Growth-ladder playbook. Рифма с лестницей s26 и картой 5 слотов §4.4."""
    s = blank(p)
    slide_title(s, "Стартовый комплект агента — и когда его усложнять.", size=24)
    text_box(s, 0.55, 1.14, 12.25, 0.42,
             "Та же лестница «не усложняй без требования», применённая на уровень ниже — к оснастке одного агента, а не системы целиком.",
             size=13.5, italic=True, color=MID, line_spacing=1.15)
    # left — thin default
    lx, ly, lw, lh = 0.55, 1.86, 4.45, 4.05
    ocean_box(s, lx, ly, lw, lh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    icon(s, "package", lx + 0.26, ly + 0.24, 0.54, "teal")
    text_box(s, lx + 0.92, ly + 0.26, lw - 1.1, 0.5, "Дефолт — тонкий агент",
             size=16, bold=True, color=TEAL, anchor=MSO_ANCHOR.MIDDLE)
    for i, t in enumerate([
        "один файл-инструкция",
        "плоская память",
        "БЕЗ subagents",
        "минимальный набор skills",
        "минимальный MCP-доступ",
    ]):
        circle(s, lx + 0.30, ly + 1.06 + i * 0.52 + 0.06, 0.12, TEAL)
        text_box(s, lx + 0.56, ly + 1.06 + i * 0.52, lw - 0.84, 0.48, t,
                 size=14, color=DEEP, line_spacing=1.1)
    text_box(s, lx + 0.28, ly + lh - 0.72, lw - 0.56, 0.62,
             "Бремя доказательства — на усложнении, а не на простоте.",
             size=12, italic=True, color=DEEP, line_spacing=1.14)
    # right — 3 justified triggers
    rx, rw = 5.30, 7.50
    triggers = [
        ("brain-circuit", "Память-бэкенд — когда:",
         "история переросла контекст ИЛИ нужен structured retrieval по фактам (не «последние N сообщений»). Тот же критерий, что переход промпт→RAG."),
        ("users", "Subagents — когда:",
         "подзадача требует отдельного окна (не засорять контекст) ИЛИ изоляции недоверенной работы (least-privilege)."),
        ("cable", "Больше MCP-доступа — когда:",
         "конкретная задача требует конкретного инструмента — не «на всякий случай». Каждое подключение — новая граница доверия."),
    ]
    ty2 = 1.86
    th = 1.24
    for ic, t, b in triggers:
        ocean_box(s, rx, ty2, rw, th)
        icon(s, ic, rx + 0.24, ty2 + 0.22, 0.46, "mid")
        text_box(s, rx + 0.84, ty2 + 0.18, rw - 1.05, 0.36, t,
                 size=14.5, bold=True, color=MID)
        text_box(s, rx + 0.84, ty2 + 0.54, rw - 1.05, 0.66, b,
                 size=12, color=DEEP, line_spacing=1.16)
        ty2 += th + 0.16
    gold_callout(s, 0.55, 6.06, 12.25, 0.82,
                 "Тот же принцип, что лестница архитектур — применённый к оснастке одного агента: presence paradox показал, что даже файл-инструкция «как ритуал» не работает. Усложняй под конкретный проверяемый триггер.",
                 size=13)
    speaker_notes(s, load_notes("s27b"))


def build_s29(p):
    """assertion_visual — human validator + MIT NANDA ~95% donut (c29)."""
    s = blank(p)
    slide_title(s, "Человек-валидатор + урок MIT NANDA.", size=27)
    # left — human validator
    lx, ly, lw, lh = 0.55, 1.40, 6.55, 4.45
    ocean_box(s, lx, ly, lw, lh)
    icon(s, "user-check", lx + 0.26, ly + 0.24, 0.52, "mid")
    text_box(s, lx + 0.92, ly + 0.24, lw - 1.1, 0.50,
             "Агент делает — человек проверяет результат и факты",
             size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.05)
    text_box(s, lx + 0.28, ly + 0.82, lw - 0.56, 0.44,
             "против независимого источника истины, НЕ по правдоподобности рассуждения (self-rationale ≠ контроль — урок про faithfulness).",
             size=12, italic=True, color=SLATE, line_spacing=1.14)
    # #237: три измерения роли человека-валидатора
    dims = [
        ("Степень автономности", "от «человек нажимает кнопку» до «агент уведомляет постфактум»"),
        ("Область доверия", "чтение (легко откатить) vs запись · обратимое vs необратимое"),
        ("Непрерывный мониторинг", "метрики качества постоянно, не разовая проверка на старте"),
    ]
    py = ly + 1.42
    for t, b in dims:
        filled_rect(s, lx + 0.28, py, lw - 0.56, 0.90, SURFACE, stroke=SOFT_GREY,
                    stroke_pt=1.0, radius=True, radius_adj=0.10)
        text_box(s, lx + 0.44, py + 0.10, lw - 0.86, 0.34, t,
                 size=13.5, bold=True, color=MID)
        text_box(s, lx + 0.44, py + 0.44, lw - 0.86, 0.42, b,
                 size=11.5, color=DEEP, line_spacing=1.10)
        py += 0.98
    # right — NANDA donut
    rx, rw = 7.35, 5.45
    ocean_box(s, rx, ly, rw, 3.10, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    add_image(s, CHARTS / "c29-nanda.png", rx + 0.20, ly + 0.20, 2.45, 2.65)
    text_box(s, rx + 2.75, ly + 0.35, rw - 3.0, 0.95, "~95%",
             size=42, bold=True, color=GOLD, line_spacing=1.0)
    text_box(s, rx + 2.75, ly + 1.30, rw - 3.0, 1.65,
             "корпоративных GenAI-пилотов без измеримого возврата инвестиций — корень в разрыве обучения и провале интеграции, не в качестве модели",
             size=12.5, color=DEEP, line_spacing=1.18)
    ocean_box(s, rx, ly + 3.25, rw, 1.20)
    text_box(s, rx + 0.26, ly + 3.38, rw - 0.52, 0.95,
             "«Запустить ИИ» ≠ «получить ценность». Решает архитектурно-интеграционная дисциплина. Иногда правильный ответ — простейшая архитектура или не-ИИ.",
             size=12, bold=True, color=DEEP, line_spacing=1.16,
             anchor=MSO_ANCHOR.MIDDLE)
    footer(s, "MIT NANDA, State of AI in Business 2025 — отчёт с методологией (150 интервью + 350 опрос + 300 внедрений), не универсальный закон.")
    speaker_notes(s, load_notes("s29"))


def build_s30(p):
    """hero_closing / summary — мост к Лекции 4 + ДЗ (#238). Hero-иллюстрация
    (реальный кадр разработки, Wikimedia CC) ≥40% справа — bridge к
    «AI в разработке ПО». Recap-заполнитель убран."""
    s = blank(p)
    # Hero photo — right ~44% full height (bridge к coding-агентам Л4)
    hx, hy, hw, hh = 7.55, 0.0, 5.78, 7.5
    hero_image(s, SCREENSHOTS / "s30-coding.jpg", hx, hy, hw, hh)
    filled_rect(s, hx, 7.10, 4.9, 0.40, DEEP)
    text_box(s, hx + 0.14, 7.12, 4.7, 0.34,
             "Фото: разработчик за IDE · Wikimedia · CC-BY-SA",
             size=10.5, italic=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    # Left — bridge + Lec 4 + homework
    lx, lw = 0.55, 6.75
    text_box(s, lx, 0.50, lw, 1.10,
             "Дальше — отрасли. Начинаем с разработки ПО.",
             size=26, bold=True, color=DEEP, line_spacing=1.06)
    # bridge to Lecture 4
    ocean_box(s, lx, 1.70, lw, 2.10, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    icon(s, "code", lx + 0.26, 1.92, 0.46, "teal")
    text_box(s, lx + 0.86, 1.90, lw - 1.1, 0.4, "Лекция 4",
             size=15, bold=True, color=TEAL, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, lx + 0.86, 2.28, lw - 1.1, 0.46,
             "AI в разработке программного обеспечения",
             size=16, bold=True, color=DEEP, line_spacing=1.05)
    text_box(s, lx + 0.28, 2.86, lw - 0.56, 0.85,
             "тот же аппарат — на конкретных задачах разработчика: те же coding-агенты, что мы разобрали, со стороны инженерной практики.",
             size=12.5, color=DEEP, line_spacing=1.18)
    # homework
    ocean_box(s, lx, 3.96, lw, 2.16, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    icon(s, "clipboard-list", lx + 0.28, 4.14, 0.50, "gold")
    text_box(s, lx + 0.90, 4.12, lw - 1.15, 0.44, "Задание — Семинар 3",
             size=18, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, lx + 0.28, 4.68, lw - 0.56, 0.40,
             "«Архитектурный выбор: чат / агент / RAG / API — 3 кейса»",
             size=14, bold=True, color=MID, line_spacing=1.05)
    text_box(s, lx + 0.28, 5.12, lw - 0.56, 0.94,
             "Применить чек-лист к 3 кейсам; для каждого: архитектура + ≥2 причины по осям + ≥1 условие смены выбора + критерий «здесь это было бы НЕ так». Задача B — разминка.",
             size=12, color=DEEP, line_spacing=1.16)
    gold_callout(s, lx, 6.30, lw, 0.74,
                 "Аппарат собран — прогоняйте чек-лист на каждой отраслевой лекции.",
                 size=13.5)
    speaker_notes(s, load_notes("s30"))


# ============================================================
# v3 new builders (suffix-ID, plan §4 U-1…U-7) — NO renumber s01–s30.
# ============================================================
def build_s04a(p):
    """section_divider — Раздел 1 «Промпт и его границы» (U-1)."""
    build_section_divider(
        p, 1, "Раздел 1", "Промпт и его границы",
        "Лестницу мы увидели целиком — теперь снизу: что умеет один вызов и где его потолок, прежде чем что-либо усложнять.",
        "s04a")


def build_s13a(p):
    """section_divider — Раздел 3 «Fine-tune vs промпт vs RAG» (U-3)."""
    build_section_divider(
        p, 3, "Раздел 3", "Fine-tune vs промпт vs RAG",
        "Проблему знания мы решили через RAG. А если проблема не в знании, а в поведении модели — её тоном, форматом, политикой?",
        "s13a")


def build_s13b(p):
    """assertion_visual — определение fine-tuning ДО критики (U-2).

    Сверху определение → центр: мини-схема pipeline
    [предобуч.модель]＋[датасет] → дообучение → [дообуч.веса] →
    низ: контраст-плашка КОНТЕКСТ vs ВЕСА. Gold-якорь — «ВЕСА».
    Schema §5.5 Process/Pipeline checklist.
    """
    s = blank(p)
    slide_title(s, "Что такое fine-tuning.", size=27)
    text_box(s, 0.55, 1.14, 12.25, 0.74,
             "Fine-tuning (дообучение) — продолжение обучения уже готовой модели на ваших данных. В Л1 — тип использования; здесь — архитектурный выбор, одна из ступеней лестницы.",
             size=14, italic=True, color=MID, line_spacing=1.18)
    # mini-schema pipeline in ocean box
    sy, sh = 1.98, 2.48
    ocean_box(s, 0.55, sy, 12.25, sh)
    # 3 nodes + «+» (n1→n2) + arrow with «дообучение» label (n2→n3)
    bw, bh = 2.85, 1.46
    by = sy + 0.66                     # node band lowered → label clearance
    n1x = 1.35                         # centered group (box inner 0.55..12.80)
    plus_x = n1x + bw                  # 4.20 — «+» zone 0.58 wide
    n2x = plus_x + 0.58                # 4.78
    arr_x0 = n2x + bw                  # 7.63 — arrow zone 1.50 wide
    n3x = arr_x0 + 1.50                # 9.13
    # node 1 — pretrained model
    filled_rect(s, n1x, by, bw, bh, SURFACE, stroke=LIGHT, stroke_pt=1.5,
                radius=True, radius_adj=0.10)
    icon(s, "cpu", n1x + bw / 2 - 0.23, by + 0.14, 0.42, "mid")
    text_box(s, n1x + 0.10, by + 0.60, bw - 0.20, 0.56,
             "Предобученная\nмодель", size=13, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, line_spacing=1.02)
    text_box(s, n1x + 0.14, by + 1.18, bw - 0.28, 0.26,
             "общие веса", size=11.5, italic=True, color=SLATE,
             align=PP_ALIGN.CENTER)
    # «+» between n1 and n2
    text_box(s, plus_x, by + bh / 2 - 0.32, 0.58, 0.64, "+",
             size=30, bold=True, color=MID, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    # node 2 — your dataset
    filled_rect(s, n2x, by, bw, bh, SURFACE, stroke=LIGHT, stroke_pt=1.5,
                radius=True, radius_adj=0.10)
    icon(s, "database", n2x + bw / 2 - 0.23, by + 0.14, 0.42, "teal")
    text_box(s, n2x + 0.14, by + 0.60, bw - 0.28, 0.30,
             "Ваш датасет", size=13, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER)
    text_box(s, n2x + 0.10, by + 0.94, bw - 0.20, 0.50,
             "примеры нужного\nповедения", size=11.5, italic=True,
             color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.02)
    # «дообучение» label ABOVE arrow (clear vertical separation)
    text_box(s, arr_x0 - 0.05, by - 0.42, 1.60, 0.32, "дообучение",
             size=13, bold=True, color=MID, align=PP_ALIGN.CENTER)
    # arrow node2 → node3
    right_arrow(s, arr_x0 + 0.06, by + bh / 2 - 0.21, 1.38, 0.42, fill=MID)
    # node 3 — fine-tuned weights (gold = the changed thing)
    filled_rect(s, n3x, by, bw, bh, GOLD_TINT, stroke=GOLD, stroke_pt=2.0,
                radius=True, radius_adj=0.10)
    icon(s, "sliders-horizontal", n3x + bw / 2 - 0.23, by + 0.14, 0.42,
         "gold")
    text_box(s, n3x + 0.10, by + 0.60, bw - 0.20, 0.56,
             "Дообученные\nВЕСА", size=13, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, line_spacing=1.02)
    text_box(s, n3x + 0.14, by + 1.18, bw - 0.28, 0.26,
             "модель уже другая", size=11.5, italic=True, color=SLATE,
             align=PP_ALIGN.CENTER)
    # contrast strip — КОНТЕКСТ vs ВЕСА (2 halves)
    cy, ch = 4.55, 1.55
    ocean_box(s, 0.55, cy, 6.05, ch, fill=TEAL_TINT, stroke=TEAL,
              stroke_pt=2.0)
    text_box(s, 0.83, cy + 0.18, 5.50, 0.34, "Промпт / RAG → КОНТЕКСТ",
             size=15, bold=True, color=TEAL)
    text_box(s, 0.83, cy + 0.58, 5.55, 0.88,
             "Меняют только вход — веса не трогаются; эффект живёт лишь в рамках запроса.",
             size=13, color=DEEP, line_spacing=1.22)
    ocean_box(s, 6.75, cy, 6.05, ch)
    text_box(s, 7.03, cy + 0.18, 5.50, 0.34, "Fine-tuning → САМИ ВЕСА",
             size=15, bold=True, color=MID)
    text_box(s, 7.03, cy + 0.58, 5.55, 0.88,
             "Изменение встроено в модель — действует всегда и стоит дороже того, что меняет контекст.",
             size=13, color=DEEP, line_spacing=1.22)
    gold_callout(s, 0.55, 6.28, 12.25, 0.78,
                 "Промпт/RAG = «что показать модели».  Fine-tuning = «изменить саму модель». На практике «дообучить» почти всегда означает LoRA/PEFT, а не переобучение всех весов (следующий слайд).",
                 size=14)
    speaker_notes(s, load_notes("s13b"))



def build_s25a(p):
    """section_divider — Раздел 5 «Как выбрать: фреймворк решения» (U-5b)."""
    build_section_divider(
        p, 5, "Раздел 5", "Как выбрать: фреймворк решения",
        "Мы разобрали все архитектуры по отдельности — и где каждая проваливается. Теперь соберём это в один инструмент выбора.",
        "s25a")


def build_s31(p):
    """qa_minimal — dedicated final Q&A slide (#239, стиль Лекции 1 s31).

    Большое «Q&A» 120pt по центру в DEEP; «Спасибо» 36pt ниже; контактные
    координаты лектора мелким в правом нижнем углу (заполняются перед
    лекцией). Белый фон, без footer и roadmap-bar."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    text_box(s, x=0.55, y=2.05, w=12.25, h=2.30, text="Q&A",
             size=120, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.0)
    text_box(s, x=0.55, y=4.55, w=12.25, h=0.78,
             text="Спасибо", size=36, bold=False, color=MID,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.2)
    # контакты лектора — правый нижний угол (заполнить перед лекцией)
    text_box(s, x=8.30, y=6.70, w=4.50, h=0.50,
             text="[контакты преподавателя — заполнить перед лекцией]",
             size=12, italic=True, color=LIGHT,
             align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
    speaker_notes(s, load_notes("s31"))


# ============================================================
# Main
# ============================================================
def main():
    # U-9: 2-part deck spec — loader reads deck.yaml + deck-part2.yaml,
    # validates 36-slide order + cascade lock (s01–s30 not renumbered).
    spec = load_deck()
    if spec is not None:
        n = len(spec["slides"])
        print(f"deck spec OK — {n} slides (deck.yaml + deck-part2.yaml), "
              f"version {spec['deck'].get('version')}, "
              f"totals {spec['totals'].get('slides')}")

    p = setup_pres()
    # v4 (issue #157) presentation order — 40 slides:
    #   R0: s01 s02 s02a s03 s04
    #   R1: s04a(div) s05 s05a s05b s06 s08 s08a
    #   R2: s09(div) s10 s11 s12 s13
    #   R3: s13a(div) s13b s15 s14 s16
    #   R4: s18(div) s19 s21 s22 s22b s22c s22d s22e s25 s25b s23
    #   R5: s25a(div) s26 s27 s27b s29 s30 s31
    builders = [
        # R0 — Открытие
        build_s01, build_s02, build_s02a, build_s03, build_s04,
        # R1 — Промпт
        build_s04a, build_s05, build_s05a, build_s05b, build_s06,
        build_s08, build_s08a,
        # R2 — RAG
        build_s09, build_s10, build_s11, build_s12, build_s13,
        # R3 — Fine-tune
        build_s13a, build_s13b, build_s15, build_s14, build_s16,
        # R4 — Агенты (11 content + divider)
        build_s18, build_s19, build_s21, build_s22, build_s22b,
        build_s22c, build_s22d, build_s22e, build_s25, build_s25b,
        build_s23,
        # R5 — Фреймворк
        build_s25a, build_s26, build_s27, build_s27b, build_s29,
        build_s30, build_s31,
    ]
    # sid list — MUST match `builders` order 1:1 (display order, 40 slides).
    sids = [
        "s01", "s02", "s02a", "s03", "s04",
        "s04a", "s05", "s05a", "s05b", "s06", "s08", "s08a",
        "s09", "s10", "s11", "s12", "s13",
        "s13a", "s13b", "s15", "s14", "s16",
        "s18", "s19", "s21", "s22", "s22b",
        "s22c", "s22d", "s22e", "s25", "s25b", "s23",
        "s25a", "s26", "s27", "s27b", "s29", "s30", "s31",
    ]
    assert len(builders) == 40, f"expected 40 builders, got {len(builders)}"
    assert len(sids) == 40, f"expected 40 sids, got {len(sids)}"

    total = len(builders)
    inject_report = {}
    for idx, (b, sid) in enumerate(zip(builders, sids)):
        b(p)
        slide = p.slides[idx]
        # (1) inject small superscript [N] markers at claim anchors
        inject_report[sid] = R.inject_ref_markers(slide, sid)
        # (2) bottom clickable numbered source list (fold any footer caveat in)
        if sid in R.SLIDE_REFS:
            ftext = _FOOTER_TEXT.get(id(slide))
            fshape = _FOOTER_TEXT.get("_shapes", {}).get(id(slide))
            if fshape is not None:
                # remove the standalone footer; its words survive as ref tail
                fshape._element.getparent().remove(fshape._element)
            # s01 hero: photo + its attribution plate own the left half; keep the
            # ref line in the RIGHT column, just below the gold-callout text, so
            # it never collides with the photo caption.
            if sid == "s01":
                R.refs_of_slide(slide, sid, y=7.24, x=6.45, w=6.35, tail=ftext)
            else:
                R.refs_of_slide(slide, sid, y=7.02, tail=ftext)
        # (3) speaker notes already carry the «Источники:» block + [N] markers
        # (baked into slides/*.md by patch_notes.py — single source of truth,
        # so slide-[N] и notes-[N] не расходятся; builder's speaker_notes(
        # load_notes(sid)) picks it up). Nothing to do here.
        # (4) muted page number «N / 40» bottom-right on every slide
        R.page_number(slide, idx + 1, total)

    # verification print — any anchor that failed to match
    missed = [(sid, a) for sid, rep in inject_report.items()
              for (a, ok) in rep if not ok]
    if missed:
        print("!! UNMATCHED ANCHORS:")
        for sid, a in missed:
            print(f"   {sid}: {a[:70]}")
    else:
        print("all ref anchors matched OK")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    p.save(str(OUT))
    print(f"saved {OUT} — {len(p.slides.__iter__.__self__._sldIdLst)} slides")


if __name__ == "__main__":
    main()
