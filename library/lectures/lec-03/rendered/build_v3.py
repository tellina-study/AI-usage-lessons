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
ROOT = Path("/home/levko/AI-usage-lessons/library/lectures/lec-03")
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
    text_box(slide, x=0.55, y=7.02, w=12.25, h=0.36, text=text,
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.LEFT,
             line_spacing=1.0)


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
    d1 = yaml.safe_load(p1.read_text(encoding="utf-8"))
    d2 = yaml.safe_load(p2.read_text(encoding="utf-8"))
    slides = list(d1.get("slides", [])) + list(d2.get("slides", []))
    spec = {
        "deck": d1.get("deck", {}),
        "palette": d1.get("palette", {}),
        "motif": d1.get("motif", {}),
        "typography": d1.get("typography", {}),
        "glossary_lock": d1.get("glossary_lock", []),
        "slides": slides,
        "totals": d2.get("totals", {}),
        "ai_failure_judgment": d2.get("ai_failure_judgment", {}),
    }
    ids = [s["id"] for s in slides]
    expected = (
        ["s01", "s02", "s03", "s04", "s04a"]
        + [f"s{n:02d}" for n in range(5, 9)]
        + ["s09", "s10", "s11", "s12", "s13", "s13a", "s13b"]
        + [f"s{n:02d}" for n in range(14, 24)]
        + ["s23a", "s24", "s25", "s25a"]
        + [f"s{n:02d}" for n in range(26, 31)]
        + ["s31"]
    )
    assert ids == expected, (
        f"deck slide order mismatch (cascade lock):\n got={ids}\n exp={expected}"
    )
    tot = spec["totals"].get("slides")
    assert tot == 36, f"deck-part2 totals.slides={tot}, expected 36"
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
    ("4", "API · агенты"),
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
    """case_study — Air Canada hook. Left chronicle, right architecture contrast."""
    s = blank(p)
    slide_title(s, "Чат-бот выдумал политику — платит компания.", size=27)
    icon(s, "gavel", 11.7, 0.40, 0.78, "mid")
    # Left — chronicle in ocean box
    lx, ly, lw, lh = 0.55, 1.50, 6.85, 4.55
    ocean_box(s, lx, ly, lw, lh)
    text_box(s, lx + 0.30, ly + 0.24, lw - 0.60, 0.40,
             "Дело Moffatt v. Air Canada · трибунал · 14.02.2024",
             size=15, bold=True, color=MID, line_spacing=1.05)
    chron = [
        "Пассажир спросил чат-бота про тариф по случаю утраты близкого",
        "Бот: «купи по полной цене, верни разницу в течение 90 дней»",
        "Реальная политика этого не допускала — и была на той же странице, на которую бот ссылался",
        "Трибунал: «бот — не отдельное юр. лицо» → компания компенсирует разницу",
    ]
    cy = ly + 0.85
    row_h = (lh - 1.05) / 4
    for i, t in enumerate(chron):
        circle(s, lx + 0.30, cy + 0.05, 0.32, MID)
        text_box(s, lx + 0.30, cy + 0.05, 0.32, 0.32, str(i + 1),
                 size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, lx + 0.80, cy, lw - 1.10, row_h - 0.08, t,
                 size=14, color=DEEP, line_spacing=1.16,
                 anchor=MSO_ANCHOR.MIDDLE)
        cy += row_h
    # Right — architecture contrast (2 blocks, full height match)
    rx, rw = 7.65, 5.15
    ocean_box(s, rx, 1.50, rw, 2.18)
    icon(s, "message-square-warning", rx + 0.28, 1.70, 0.52, "mid")
    text_box(s, rx + 0.95, 1.76, rw - 1.15, 0.4, "ЧТО ВЫБРАЛИ",
             size=14, bold=True, color=LIGHT, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, rx + 0.28, 2.42, rw - 0.56, 1.15,
             "Генеративный чат — архитектура, которая по своей природе сочиняет правдоподобный текст",
             size=15, color=DEEP, line_spacing=1.18)
    ocean_box(s, rx, 3.87, rw, 2.18, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    icon(s, "key", rx + 0.28, 4.07, 0.52, "teal")
    text_box(s, rx + 0.95, 4.13, rw - 1.15, 0.4, "ЧТО БЫЛО НУЖНО",
             size=14, bold=True, color=TEAL, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, rx + 0.28, 4.79, rw - 0.56, 1.15,
             "Детерминированный lookup фиксированной политики — статическая страница или таблица правил",
             size=15, color=DEEP, line_spacing=1.18)
    gold_callout(s, 0.55, 6.22, 12.25, 0.66,
                 "Это не сбой модели. Это неправильный выбор архитектуры под задачу — об этом классе ошибок вся лекция.",
                 size=15)
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
    roadmap_bar(s, 0, y=6.45)
    speaker_notes(s, load_notes("s02"))


def build_s03(p):
    """assertion_visual — hub & spokes: 1 LLM call + 4 wrappers."""
    s = blank(p)
    slide_title(s, "Что мы переносим из Лекции 2 — и что надстроим.", size=26)
    text_box(s, 0.55, 1.25, 12.25, 0.4,
             "Вокруг одного вызова модели надстраиваются 4 обвязки — RAG стоит прямо на эмбеддингах Л2.",
             size=15, italic=True, color=MID)
    # Center hub
    hx, hy, hw, hh = 5.05, 3.50, 3.25, 1.65
    # 4 spokes (bigger, with icons; RAG = gold)
    spokes = [
        ("RAG", "retrieval = semantic search Л2 §2 + LLM сверху", "database",
         0.55, 1.85, GOLD, True),
        ("Function calling", "модель дотягивается до внешних систем", "terminal",
         6.95, 1.85, LIGHT, False),
        ("MCP", "стандарт подключения инструментов", "cable",
         0.55, 5.10, LIGHT, False),
        ("Цикл агента", "много шагов вокруг одного прохода", "bot",
         6.95, 5.10, LIGHT, False),
    ]
    sw, sh = 5.85, 1.55
    for title, sub, ic, sx, sy, col, isgold in spokes:
        if isgold:
            ocean_box(s, sx, sy, sw, sh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, sx, sy, sw, sh)
        icon(s, ic, sx + 0.26, sy + 0.30, 0.58, "gold" if isgold else "mid")
        text_box(s, sx + 1.05, sy + 0.24, sw - 1.25, 0.42, title,
                 size=18, bold=True, color=(DEEP if isgold else MID))
        text_box(s, sx + 1.05, sy + 0.68, sw - 1.25, 0.72, sub,
                 size=12.5, color=DEEP, line_spacing=1.10)
        if isgold:
            chip(s, sx + 1.05, sy + sh - 0.42, 3.0, 0.32,
                 "↑ стоит на эмбеддингах Л2 §2", fill=GOLD, color=DEEP,
                 size=10)
    # Center hub
    ocean_box(s, hx, hy, hw, hh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, hx + 0.15, hy + 0.26, hw - 0.30, 0.5, "Один вызов LLM",
             size=18, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, hx + 0.15, hy + 0.80, hw - 0.30, 0.75,
             "single-shot инференс (Л2 §4): один проход, без памяти",
             size=12, italic=True, color=MID, align=PP_ALIGN.CENTER,
             line_spacing=1.10)
    # connectors hub -> spokes
    connector(s, hx + 0.25, hy + 0.25, 6.4, 3.4, LIGHT, 1.75)
    connector(s, hx + hw - 0.25, hy + 0.25, 6.95, 3.4, LIGHT, 1.75)
    connector(s, hx + 0.25, hy + hh - 0.25, 6.4, 5.10, LIGHT, 1.75)
    connector(s, hx + hw - 0.25, hy + hh - 0.25, 6.95, 5.10, LIGHT, 1.75)
    footer(s, "RAG = semantic search из Л2 §2 + LLM сверху. Single-shot и semantic search не переобъясняем — это готовые блоки. Детали — Раздел 2.")
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
    step_h = 0.66
    vgap = 0.075
    bottom_edge = 6.78  # bottom of step 1
    sx = 0.55
    for i, (num, label, sub, col, isgold) in enumerate(steps):
        # i=0 -> bottom rung; each higher step sits above + indented right
        y = bottom_edge - step_h - i * (step_h + vgap)
        indent = i * 0.22
        w = 7.95 - indent
        x = sx + indent
        if isgold:
            ocean_box(s, x, y, w, step_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, x, y, w, step_h)
        circle(s, x + 0.14, y + (step_h - 0.36) / 2, 0.36, col)
        text_box(s, x + 0.14, y + (step_h - 0.36) / 2, 0.36, 0.36, num,
                 size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x + 0.62, y + 0.10, w - 0.78, 0.28, label,
                 size=15, bold=True, color=DEEP)
        text_box(s, x + 0.62, y + 0.38, w - 0.78, 0.24, sub,
                 size=10.5, italic=True, color=SLATE)
    # PA-1 (owner-approved): direction-of-scale label alongside the ladder —
    # «сложнее ↑» at top, «проще ↓» at bottom (removes the «выше=лучше»
    # mis-read; the climb is harder, not better). Labels sit in the clear
    # zone between the question box (ends 2.15) and ladder bottom (6.78).
    text_box(s, 8.02, 2.22, 1.12, 0.30, "сложнее ↑", size=12, bold=True,
             color=LIGHT, align=PP_ALIGN.CENTER)
    up_arrow(s, 8.42, 2.62, 0.30, 3.92, fill=COVER_OUTLINE)
    text_box(s, 8.02, 6.58, 1.12, 0.30, "проще ↓", size=12, bold=True,
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
    text_box(s, 0.55, 1.22, 12.25, 0.4,
             "Любой подъём по лестнице оплачивается требованием задачи — это бремя доказательства.",
             size=15, italic=True, color=MID)
    # Left — anchor block
    lx, ly, lw, lh = 0.55, 1.78, 5.55, 3.85
    ocean_box(s, lx, ly, lw, lh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    icon(s, "target", lx + 0.28, ly + 0.26, 0.62, "teal")
    text_box(s, lx + 0.28, ly + 1.02, lw - 0.56, 0.6,
             "Один вызов LLM\nс хорошим промптом",
             size=19, bold=True, color=DEEP, line_spacing=1.1)
    bullets = [
        "минимальная стоимость (один проход)",
        "минимальная латентность (нет лишних обращений)",
        "максимальная предсказуемость (нет петель, нет retrieval, который тихо деградирует)",
    ]
    by = ly + 2.05
    for b in bullets:
        circle(s, lx + 0.30, by + 0.07, 0.12, TEAL)
        text_box(s, lx + 0.56, by, lw - 0.84, 0.62, b,
                 size=13.5, color=DEEP, line_spacing=1.12)
        by += 0.58
    # Right — what each climb costs
    rx, rw = 6.30, 6.50
    ocean_box(s, rx, 1.78, rw, 1.78)
    text_box(s, rx + 0.26, 1.95, rw - 0.52, 0.36, "Добавляешь RAG →",
             size=15, bold=True, color=MID)
    text_box(s, rx + 0.26, 2.32, rw - 0.52, 1.15,
             "конвейер индексации + векторное хранилище + компонент retrieval (может молча деградировать) + метрики его качества",
             size=13, color=DEEP, line_spacing=1.14)
    ocean_box(s, rx, 3.72, rw, 1.91)
    text_box(s, rx + 0.26, 3.89, rw - 0.52, 0.36, "Добавляешь инструменты / цикл →",
             size=15, bold=True, color=MID)
    text_box(s, rx + 0.26, 4.26, rw - 0.52, 1.28,
             "внешние вызовы (падают, тормозят) + петли (расходятся) + недетерминизм траектории + новая поверхность атаки",
             size=13, color=DEEP, line_spacing=1.14)
    gold_callout(s, 0.55, 5.92, 12.25, 0.92,
                 "Не усложняй архитектуру без причины, выраженной в требованиях задачи. Это распределение бремени доказательства, а не примитивизм.",
                 size=15)
    speaker_notes(s, load_notes("s05"))


def build_s06(p):
    """case_study — CoT before/after contrast."""
    s = blank(p)
    slide_title(s, "Chain-of-thought (пошаговое рассуждение).", size=27)
    text_box(s, 0.55, 1.18, 12.25, 0.55,
             "CoT — попросить модель не отвечать сразу, а сначала рассуждать по шагам. Технически это всё ещё один вызов — изменён только промпт.",
             size=14, italic=True, color=MID, line_spacing=1.15)
    cy, ch = 1.95, 3.05
    cw = 6.05
    # without CoT
    ocean_box(s, 0.55, cy, cw, ch)
    text_box(s, 0.83, cy + 0.20, cw - 0.56, 0.4, "Без CoT",
             size=18, bold=True, color=LIGHT)
    text_box(s, 0.83, cy + 0.68, cw - 0.56, 1.15,
             "Задача: «Было 23 яблока, 7 испортились, докупили 2 ящика по 6. Сколько хороших?»",
             size=14, color=DEEP, line_spacing=1.18)
    text_box(s, 0.83, cy + 2.05, cw - 0.56, 0.85,
             "→ модель выдаёт правдоподобное, но неверное число",
             size=14, bold=True, color=SLATE, line_spacing=1.15)
    # with CoT
    rx = 6.75
    ocean_box(s, rx, cy, cw, ch, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, rx + 0.28, cy + 0.20, cw - 0.56, 0.4, "С CoT  («решай по шагам»)",
             size=18, bold=True, color=TEAL)
    steps = ["23 − 7 = 16", "2 × 6 = 12", "16 + 12 = 28"]
    sy = cy + 0.72
    for i, st in enumerate(steps):
        last = (i == 2)
        text_box(s, rx + 0.32, sy, cw - 0.6, 0.5, st,
                 size=(24 if last else 18), bold=True,
                 color=(GOLD if last else DEEP))
        sy += (0.62 if not last else 0.5)
    text_box(s, rx + 0.32, cy + 2.45, cw - 0.6, 0.4, "→ верно",
             size=15, bold=True, color=TEAL)
    # v2 (#9): assertion-bearing gold plate raised to neighbour level
    # (h≈1.1, size 15 — matches s05/s08/s14 callouts; was thin 0.92/14.5).
    gold_callout(s, 0.55, 5.16, 12.25, 1.10,
                 "CoT — инструмент под класс задач, не глобальный тумблер. Когда НЕ нужен: прямое извлечение факта, простая классификация — удлиняет ответ (дороже, медленнее) и иногда уводит в правдоподобную ошибку.",
                 size=15)
    footer(s, "Поможет ли CoT именно вашей задаче — или там ответ извлекается напрямую?")
    speaker_notes(s, load_notes("s06"))


def build_s07(p):
    """case_study — CoT faithfulness limit (chart c07)."""
    s = blank(p)
    slide_title(s, "Предел CoT: текст ≠ мысль.", size=27)
    text_box(s, 0.55, 1.16, 12.25, 0.55,
             "Faithfulness (верность рассуждения) — степень, в которой проговорённая цепочка отражает реальные факторы, повлиявшие на ответ.",
             size=14, italic=True, color=MID, line_spacing=1.15)
    # left — chart
    cx, cyy, cww, chh = 0.55, 1.92, 7.05, 3.95
    ocean_box(s, cx, cyy, cww, chh)
    add_image(s, CHARTS / "c07-faithfulness.png", cx + 0.18, cyy + 0.16,
              cww - 0.36, chh - 0.32)
    # right — experiment + rule
    rx, rw = 7.85, 4.95
    ocean_box(s, rx, 1.92, rw, 1.55)
    text_box(s, rx + 0.26, 2.08, rw - 0.52, 1.25,
             "Эксперимент: задачу дали дважды — без подсказки и с подсказкой, меняющей ответ. Когда подсказка изменила ответ — упомянула ли её модель?",
             size=13, color=DEEP, line_spacing=1.16)
    gold_callout(s, rx, 3.62, rw, 2.25,
                 "Контроль на самообъяснении модели — не контроль. Человек проверяет результат и факты против внешнего источника, а не правдоподобность текста. Верность падает на трудных задачах.",
                 size=14)
    footer(s, "Источник: Anthropic, апрель 2025. Freshness — quarterly; перепроверить ко дню лекции.")
    speaker_notes(s, load_notes("s07"))


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
             "context rot = тот же «lost in the middle» из Л2 §3 — новый термин, не новая сущность",
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
         "вопрос → эмбеддинг → top-k ближайших фрагментов\n\n= тот самый semantic search из Л2 §2 — не переобъясняем", MID, False),
        ("3", "Генерация с опорой", "grounding", "check-check",
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
        text_box(s, x + 0.86, sy + 0.26, bw - 1.5, 0.42, title,
                 size=17, bold=True, color=DEEP)
        text_box(s, x + 0.86, sy + 0.66, bw - 1.5, 0.30, tag,
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
    text_box(s, 0.55, 1.16, 12.25, 0.4,
             "RAG оправдан, когда 4 признака складываются ОДНОВРЕМЕННО (конъюнкция, не дизъюнкция).",
             size=14.5, italic=True, color=MID)
    cards = [
        ("Большое / растущее", "не влезает в окно целиком, или дорого класть весь корпус в каждый запрос"),
        ("Меняется", "документы, цены, регламенты обновляются чаще, чем выходят версии модели"),
        ("Свежесть + провенанс", "ответ опирается на проверяемый источник; можно показать, откуда факт"),
        ("Приватная база", "знания компании не входят в веса публичной модели"),
    ]
    cw, chh = 2.78, 2.55
    cy = 1.78
    x = 0.55
    for i, (t, sub) in enumerate(cards):
        ocean_box(s, x, cy, cw, chh)
        text_box(s, x + 0.20, cy + 0.22, cw - 0.40, 0.75, t,
                 size=15.5, bold=True, color=MID, line_spacing=1.05)
        text_box(s, x + 0.20, cy + 1.00, cw - 0.40, chh - 1.2, sub,
                 size=12, color=DEEP, line_spacing=1.16)
        if i < 3:
            circle(s, x + cw + 0.015, cy + chh / 2 - 0.21, 0.42, GOLD)
            text_box(s, x + cw + 0.015, cy + chh / 2 - 0.21, 0.42, 0.42, "И",
                     size=17, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE)
        x += cw + 0.42
    # -> RAG result + worked example
    ocean_box(s, 0.55, 4.55, 7.4, 1.78, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    text_box(s, 0.85, 4.74, 7.0, 0.4, "Все 4 ОДНОВРЕМЕННО → RAG",
             size=17, bold=True, color=DEEP)
    text_box(s, 0.85, 5.18, 7.0, 1.05,
             "Корп. база из тысяч регламентов, обновляется еженедельно, ответ с обязательной ссылкой на пункт: все 4 признака ✓ → образцовый профиль RAG.",
             size=13, color=DEEP, line_spacing=1.18)
    ocean_box(s, 8.15, 4.55, 4.65, 1.78, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    icon(s, "check-check", 8.40, 4.78, 0.50, "teal")
    text_box(s, 8.40, 5.35, 4.20, 0.95,
             "Один признак сам по себе RAG не оправдывает — нужна конъюнкция.",
             size=14.5, bold=True, color=DEEP, line_spacing=1.15)
    speaker_notes(s, load_notes("s11"))


def build_s12(p):
    """schema_matrix-ish — 3 criteria columns «when NOT RAG»."""
    s = blank(p)
    slide_title(s, "Когда RAG — НЕ правильный выбор.", size=27)
    text_box(s, 0.55, 1.16, 12.25, 0.4,
             "Знать, когда RAG не нужен, ценнее: это модная архитектура, её ставят туда, где она вредит.",
             size=14.5, italic=True, color=MID)
    cols = [
        ("circle-slash", "1. Корпус влезает в окно",
         "ориентир — менее ~200k токенов, меняется редко",
         "→ full-context + кэширование префикса, не RAG-инфраструктура",
         LIGHT, "mid", False),
        ("key", "2. Отдать фиксированную политику / значение",
         "тариф, цена, пункт регламента, правило",
         "→ детерминированный lookup / статическая страница",
         LIGHT, "mid", False),
        ("bomb", "3. Нет наблюдения за retrieval",
         "observability отсутствует",
         "→ скрытая бомба: не падает с ошибкой, а уверенно отвечает неправильно — отложенный невидимый отказ",
         GOLD, "gold", True),
    ]
    cw, chh = 4.00, 3.05
    cy = 1.78
    x = 0.55
    for nm, t, tag, alt, col, var, isgold in cols:
        if isgold:
            ocean_box(s, x, cy, cw, chh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, x, cy, cw, chh)
        icon(s, nm, x + 0.24, cy + 0.24, 0.52, var)
        text_box(s, x + 0.90, cy + 0.26, cw - 1.05, 0.78, t,
                 size=15, bold=True, color=(DEEP if isgold else MID),
                 line_spacing=1.08)
        text_box(s, x + 0.24, cy + 1.15, cw - 0.48, 0.40, tag,
                 size=12, italic=True, color=LIGHT)
        text_box(s, x + 0.24, cy + 1.58, cw - 0.48, chh - 1.75, alt,
                 size=13, bold=True, color=DEEP, line_spacing=1.18)
        x += cw + 0.32
    gold_callout(s, 0.55, 5.20, 12.25, 1.05,
                 "RAG оправдан только когда выполнены все три условия: (а) проще механизмы не справляются, (б) нужна генерация, а не фиксированное значение, (в) есть процесс измерения качества retrieval.",
                 size=14.5)
    speaker_notes(s, load_notes("s12"))


def build_s13(p):
    """case_study — RAG fails at scale + Air Canada revisited (v2: decluttered
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
    # right — Air Canada revisited (teal), evenly split: diagnosis / alternative
    rx, rw = 7.35, 5.45
    ocean_box(s, rx, 2.14, rw, 3.74, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, rx + 0.30, 2.36, rw - 0.60, 0.34, "Air Canada revisited",
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
             "фиксированная политика → lookup / страница; нужен диалог → RAG со strict grounding, обязательная цитата, явное «не знаю», human-review",
             size=13, color=DEEP, line_spacing=1.20)
    footer(s, "Документированные классы провалов (Barnett et al. 2024; Air Canada — McCarthy Tétrault 2024). Кейсы — illustrative.")
    speaker_notes(s, load_notes("s13"))


def build_s14(p):
    """assertion_visual — fine-tuning narrowed (2 zones)."""
    s = blank(p)
    slide_title(s, "Fine-tuning не умер — он сузился.", size=27)
    text_box(s, 0.55, 1.16, 12.25, 0.78,
             "Fine-tuning (дообучение) — доп. обучение готовой модели на своих данных, меняются веса. В Л1 — тип использования; здесь — архитектурный выбор, одна из ступеней лестницы.",
             size=14, italic=True, color=MID, line_spacing=1.18)
    # 2 zones
    zy, zh = 2.08, 3.05
    ocean_box(s, 0.55, zy, 6.05, zh)
    icon(s, "git-branch", 0.83, zy + 0.24, 0.52, "mid")
    text_box(s, 1.50, zy + 0.28, 4.85, 0.45, "Ушло из fine-tuning  (в 2026)",
             size=16, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.83, zy + 0.95, 5.50, 0.55, "→ знание, факты, то, что меняется → RAG / длинный контекст",
             size=14, bold=True, color=DEEP, line_spacing=1.15)
    text_box(s, 0.83, zy + 1.70, 5.50, 1.15,
             "Зашить факты в веса: нельзя процитировать, нельзя обновить точечно, нельзя удалить один",
             size=12.5, italic=True, color=SLATE, line_spacing=1.16)
    ocean_box(s, 6.75, zy, 6.05, zh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    icon(s, "scale", 7.03, zy + 0.24, 0.52, "teal")
    text_box(s, 7.70, zy + 0.28, 4.85, 0.45, "Осталось за fine-tuning",
             size=16, bold=True, color=TEAL, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 7.03, zy + 0.95, 5.50, 1.9,
             "поведение · стиль · формат вывода · следование политике · дистилляция (меньшая модель учится у большей)",
             size=14, bold=True, color=DEEP, line_spacing=1.30)
    gold_callout(s, 0.55, 5.25, 12.25, 1.0,
                 "Реальный вопрос 2026 — не «RAG или fine-tuning», а «что здесь знание (→ RAG), что поведение (→ FT)». FT сузился, а не исчез.",
                 size=15)
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
    # v2 (#9): add assertion-bearing gold plate to neighbour level — slide
    # had NO bottom gold callout (assertion was only in the reason-3 tint
    # box); fills the dead band 5.6→7.0, matches s14/s17 callouts.
    gold_callout(s, 0.55, 5.62, 12.25, 1.05,
                 "PEFT (LoRA/QLoRA) почти всегда лучше full fine-tuning: дешевле, модульнее и заметно снижает риск catastrophic forgetting — full FT в 2026 почти никогда.",
                 size=15)
    footer(s, "Полный спектр методов настройки поведения (SFT / DPO / RFT) — в главе.")
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


def build_s17(p):
    """schema_matrix — criteria table «что куда» (4 rows)."""
    s = blank(p)
    slide_title(s, "Критерии: что куда.", size=27)
    text_box(s, 0.55, 1.14, 12.25, 0.4,
             "Знание меняется → RAG; поведение/тон/формат → PEFT; детерминированное → код. Гибрид — норма 2026.",
             size=14.5, italic=True, color=MID)
    # Ocean motif wrapper behind the table (drawn first, sits behind cells)
    ocean_box(s, 0.40, 1.55, 12.55, 4.30)
    # table
    tx, ty, tw = 0.55, 1.70, 12.25
    headers = ["Если задача требует…", "→ правильный инструмент", "…и НЕ этот, потому что"]
    col_w = [4.05, 3.30, 4.90]
    rows = [
        ("знание меняется / нужны свежесть, провенанс", "RAG (или длинный контекст для малого корпуса)",
         "не fine-tuning: устареет, дорого переобучать, риск forgetting", False),
        ("стабильное поведение / тон / формат / политика", "fine-tuning (PEFT)",
         "не RAG: подаёт знание, но не меняет манеру модели", False),
        ("снизить стоимость / латентность на узкой задаче", "дистилляция (fine-tuning)",
         "не RAG/промпт: не уменьшают размер модели", False),
        ("детерминированный, верифицируемый ответ", "обычный код, без ИИ",
         "ни RAG, ни FT: ИИ добавит недетерминизм без выигрыша", True),
    ]
    hh = 0.55
    rh = 0.84
    # header row
    cx = tx
    for j, hd in enumerate(headers):
        filled_rect(s, cx, ty, col_w[j], hh, MID, radius=False)
        text_box(s, cx + 0.14, ty, col_w[j] - 0.28, hh, hd,
                 size=13, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.0)
        cx += col_w[j]
    yy = ty + hh
    for ri, (c0, c1, c2, isgold) in enumerate(rows):
        bgrow = GOLD_TINT if isgold else (WHITE if ri % 2 == 0 else SURFACE)
        cx = tx
        cells = [c0, c1, c2]
        for j, cc in enumerate(cells):
            filled_rect(s, cx, yy, col_w[j], rh, bgrow,
                        stroke=(GOLD if isgold else SOFT_GREY),
                        stroke_pt=(1.5 if isgold else 0.75))
            mid_col = (DEEP if isgold else MID) if j == 1 else DEEP
            text_box(s, cx + 0.16, yy + 0.06, col_w[j] - 0.32, rh - 0.12, cc,
                     size=12.5, bold=(j == 1), color=mid_col,
                     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.10)
            cx += col_w[j]
        yy += rh
    gold_callout(s, 0.55, yy + 0.16, 12.25, 1.05,
                 "Гибрид — норма 2026 там, где у задачи ОДНОВРЕМЕННО есть и проблема знания, и проблема поведения. Не «больше компонентов лучше» — знание и поведение разнесены по правильным механизмам.",
                 size=14)
    speaker_notes(s, load_notes("s17"))


def build_s18(p):
    """section_divider — Раздел 4."""
    build_section_divider(
        p, 4, "Раздел 4", "API · tools · MCP · агенты + безопасность",
        "От собеседника в окне чата — к компоненту продакшен-системы. И кто видит данные в цепочке.",
        "s18")


def build_s19(p):
    """assertion_visual — API layer: 3 mechanism cards."""
    s = blank(p)
    slide_title(s, "API-слой: модель как компонент системы.", size=27)
    text_box(s, 0.55, 1.16, 12.25, 0.4,
             "3 механизма делают модель: встраиваемой, активной, экономически жизнеспособной.",
             size=14.5, italic=True, color=MID)
    cards = [
        ("boxes", "Structured output",
         "модель обязана вернуть ответ строго по схеме (JSON), а не свободный текст",
         "→ выход = валидные данные, не текст для парсинга", "встраиваемая"),
        ("terminal", "Function calling",
         "модель возвращает «вызови инструмент X с аргументами Y»; исполняет ваш код, не модель",
         "→ модель активная в системе", "активная"),
        ("database", "Prompt caching",
         "переиспользовать вычисленное состояние неизменного префикса",
         "→ не переплачивать за повторяемую часть", "экономически жизнеспособная"),
    ]
    cw, chh = 4.00, 3.35
    cy = 1.78
    x = 0.55
    for nm, t, body, arrow, tag in cards:
        ocean_box(s, x, cy, cw, chh)
        filled_rect(s, x + 0.24, cy + 0.24, 0.62, 0.62, MID, radius=True,
                    radius_adj=0.18)
        icon(s, nm, x + 0.30, cy + 0.30, 0.50, "white")
        text_box(s, x + 0.98, cy + 0.30, cw - 1.15, 0.55, t,
                 size=16, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.0)
        text_box(s, x + 0.24, cy + 1.05, cw - 0.48, 1.05, body,
                 size=12.5, color=DEEP, line_spacing=1.16)
        text_box(s, x + 0.24, cy + 2.15, cw - 0.48, 0.62, arrow,
                 size=13, bold=True, color=MID, line_spacing=1.12)
        chip(s, x + 0.24, cy + chh - 0.62, cw - 0.48, 0.42, tag,
             fill=TEAL, color=WHITE, size=12.5)
        x += cw + 0.32
    gold_callout(s, 0.55, 5.32, 12.25, 0.98,
                 "Ни один из трёх не делает модель надёжнее или аудируемее — они расширяют, что модель может, не меняя её недетерминированной природы. Правило лестницы не отменяется.",
                 size=14.5)
    speaker_notes(s, load_notes("s19"))


def build_s20(p):
    """assertion_visual — MCP: N×M→N+M + adoption + trust warning."""
    s = blank(p)
    slide_title(s, "MCP — стандарт подключения инструментов.", size=26)
    text_box(s, 0.55, 1.14, 12.25, 0.55,
             "MCP (Model Context Protocol) — открытый стандарт: единый способ подключать инструменты, данные и контекст к LLM. «USB-C для инструментов LLM».",
             size=13.5, italic=True, color=MID, line_spacing=1.15)
    # left — N×M -> N+M + adoption timeline
    lx, ly, lw, lh = 0.55, 1.92, 6.05, 3.95
    ocean_box(s, lx, ly, lw, lh)
    icon(s, "cable", lx + 0.26, ly + 0.22, 0.55, "mid")
    text_runs(s, lx + 0.95, ly + 0.28, lw - 1.15, 0.85, [
        {"text": "N×M", "size": 22, "bold": True, "color": LIGHT},
        {"text": " несовместимых интеграций → ", "size": 14, "color": DEEP},
        {"text": "N+M", "size": 22, "bold": True, "color": TEAL},
        {"text": " через MCP", "size": 14, "color": DEEP},
    ], line_spacing=1.1, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, lx + 0.26, ly + 1.20, lw - 0.52, 0.6,
             "инструмент один раз = MCP-сервер; модель один раз = MCP-клиент",
             size=12, italic=True, color=SLATE, line_spacing=1.12)
    text_box(s, lx + 0.26, ly + 1.90, lw - 0.52, 0.32,
             "Мини-таймлайн принятия:", size=12.5, bold=True, color=MID)
    tl = [("Anthropic", "11/2024", "logo-anthropic"),
          ("OpenAI", "03/2025", "logo-openai"),
          ("Google", "04/2025", "logo-gemini"),
          ("независимый фонд", "→", None)]
    ty = ly + 2.30
    tw_each = (lw - 0.52) / 4
    for i, (nm, dt, lg) in enumerate(tl):
        ex = lx + 0.26 + i * tw_each
        if lg:
            add_image(s, ICONS / f"{lg}.png", ex + tw_each / 2 - 0.21, ty, 0.42, 0.42)
        else:
            circle(s, ex + tw_each / 2 - 0.21, ty, 0.42, LIGHT)
        text_box(s, ex, ty + 0.46, tw_each, 0.26, nm,
                 size=10, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, ex, ty + 0.70, tw_each, 0.24, dt,
                 size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
        if i < 3:
            text_box(s, ex + tw_each - 0.12, ty + 0.05, 0.24, 0.32, "→",
                     size=14, bold=True, color=LIGHT, align=PP_ALIGN.CENTER)
    # right — warning
    rx, rw = 6.80, 6.0
    ocean_box(s, rx, 1.92, rw, 3.95, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, rx + 0.26, 2.10, rw - 0.52, 0.75,
             "Стандартизация подключения ≠ безопасность подключаемого — и усугубляет проблему доверия.",
             size=14.5, bold=True, color=TEAL, line_spacing=1.14)
    warns = [
        "код в вашем окружении / доступ к данным",
        "описание попадает в контекст модели — носитель prompt injection (инъекция в промпт; разбор — s25)",
        "ещё одна граница доверия и retention-политика",
    ]
    wy = 2.95
    for w in warns:
        circle(s, rx + 0.28, wy + 0.07, 0.12, TEAL)
        text_box(s, rx + 0.54, wy, rw - 0.82, 0.72, w,
                 size=12.5, color=DEEP, line_spacing=1.14)
        wy += 0.80
    gold_callout(s, 0.55, 5.95, 12.25, 0.88,
                 "Удобство подключения — не аргумент за подключение. Аргумент — требование задачи и приемлемость новой границы доверия.",
                 size=14.5)
    footer(s, "Принятие/масштаб экосистемы MCP — перепроверить ко дню лекции.")
    speaker_notes(s, load_notes("s20"))


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
         "валидация против ВНЕШНЕГО критерия — не самооценка модели (callback s07)", GOLD, True),
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
    gold_callout(s, 0.55, 5.92, 8.55, 0.92,
                 "Найди простейшее решение. «Лень формализовать» не делает задачу непредсказуемой.",
                 size=14)
    ocean_box(s, 9.30, 5.92, 3.50, 0.92, fill=SURFACE, stroke=SOFT_GREY,
              stroke_pt=1.0)
    text_box(s, 9.50, 6.00, 3.10, 0.78,
             "Мульти-агент по умолчанию — не апгрейд (дебат — в главе)",
             size=11.5, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    speaker_notes(s, load_notes("s22"))


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
    text_box(s, c1x + 0.24, cy + 1.82, c1w - 0.48, 0.7, "$4 200 за 63 часа",
             size=26, bold=True, color=GOLD, line_spacing=1.0)
    text_box(s, c1x + 0.24, cy + 2.55, c1w - 0.48, 0.72,
             "Почему: агент не «видит» ни стоимости, ни времени, ни повторяемости",
             size=11.5, italic=True, color=SLATE, line_spacing=1.12)
    text_box(s, c1x + 0.24, cy + 3.30, c1w - 0.48, 1.05,
             "Правильно: задача предсказуема → retry-with-backoff скрипт, не агент; budget/loop-лимиты ВНЕ агента",
             size=12, bold=True, color=DEEP, line_spacing=1.14)
    # card 2 — compounding (chart)
    c2x, c2w = 4.80, 4.05
    ocean_box(s, c2x, cy, c2w, chh)
    text_box(s, c2x + 0.24, cy + 0.20, c2w - 0.48, 0.4,
             "2. Reliability compounding", size=15, bold=True, color=MID)
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
             "Правильно: single-threaded линейный агент; мульти-агент — только широко-параллельное независимое",
             size=12.5, bold=True, color=DEEP, line_spacing=1.18)
    footer(s, "$4 200-петля — single-author постмортем 2026-04 (illustrative, числа округлены); reliability compounding — MindStudio 2025–2026.")
    speaker_notes(s, load_notes("s23"))


def build_s24(p):
    """schema_pipeline — data-flow chain map + 2 facts + rule (v2: subtype
    reclassified architecture→pipeline; decluttered — definitions moved to
    notes, USER-actor icon added at «ваши данные», more whitespace)."""
    s = blank(p)
    slide_title(s, "Кто видит данные в цепочке.", size=27)
    text_box(s, 0.55, 1.14, 12.25, 0.40,
             "Каждое звено — своя граница доверия и своя retention-политика. Данные за периметром живут не по вашим правилам.",
             size=14, italic=True, color=MID, line_spacing=1.15)
    # data-flow chain (USER actor at the head; pipeline of trust boundaries)
    cx, cyy, cw, chh = 0.55, 1.78, 12.25, 1.78
    ocean_box(s, cx, cyy, cw, chh)
    chain = [("ваши данные", "user-check"), ("агент", "bot"),
             ("инструмент", "terminal"), ("внешний API", "cable"),
             ("провайдер", "database"), ("подрядчики", "link")]
    n = len(chain)
    node_w = 1.74
    gap = (cw - 0.5 - n * node_w) / (n - 1)
    nx = cx + 0.25
    ny = cyy + 0.34
    for i, (lab, ic) in enumerate(chain):
        is_user = (i == 0)
        col = GOLD if is_user else (MID if i < 5 else LIGHT)
        filled_rect(s, nx, ny, node_w, 0.86, col, radius=True, radius_adj=0.14)
        icon(s, ic, nx + node_w / 2 - 0.20, ny + 0.10, 0.28,
             "deep" if is_user else "white")
        text_box(s, nx, ny + 0.44, node_w, 0.38, lab, size=12.5, bold=True,
                 color=(DEEP if is_user else WHITE),
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < n - 1:
            ax = nx + node_w + 0.02
            right_arrow(s, ax, ny + 0.28, gap - 0.04, 0.30, fill=LIGHT)
        nx += node_w + gap
    text_box(s, cx + 0.25, cyy + chh - 0.34, cw - 0.5, 0.28,
             "золото = вы (точка отсчёта); каждая стрелка — новая retention-граница",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    # 2 fact panels — short visible text (full detail in speaker notes)
    fy, fh = 3.80, 1.55
    ocean_box(s, 0.55, fy, 6.05, fh)
    icon(s, "gavel", 0.83, fy + 0.22, 0.46, "mid")
    text_box(s, 1.45, fy + 0.24, 4.95, 0.46, "Судебный приказ переживает вашу политику",
             size=14, bold=True, color=MID, line_spacing=1.05,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.83, fy + 0.86, 5.55, 0.60,
             "суд может обязать хранить логи поверх договорных «30 дней» (NYT v. OpenAI)",
             size=12.5, color=DEEP, line_spacing=1.14)
    ocean_box(s, 6.75, fy, 6.05, fh)
    icon(s, "eye-off", 7.03, fy + 0.22, 0.46, "mid")
    text_box(s, 7.65, fy + 0.24, 4.95, 0.46, "ZDR покрывает не всё",
             size=14, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 7.03, fy + 0.86, 5.55, 0.60,
             "вне ZDR: third-party, Files, batch, MCP — а агент это и есть third-party",
             size=12.5, color=DEEP, line_spacing=1.14)
    gold_callout(s, 0.55, 5.58, 12.25, 0.92,
                 "«У нас ZDR» ≠ «нигде ничего не хранится». Контрмера — карта данных по каждой фиче, не галочка. Регулируемое — не слать без ZDR/BAA.",
                 size=14.5)
    footer(s, "ZDR (Zero Data Retention) — провайдер не хранит содержимое; least-privilege — минимум прав. BAA — договор об обработке. Хронология retention — в главе.")
    speaker_notes(s, load_notes("s24"))


def build_s25(p):
    """case_study — tool attacks: mechanism map + 2 cases + 4 rules."""
    s = blank(p)
    slide_title(s, "Атаки через инструменты.", size=27)
    text_box(s, 0.55, 1.14, 12.25, 0.55,
             "Prompt injection (инъекция в промпт) — текст во внешних данных модель интерпретирует как инструкцию. Модель не отличает «данные» от «команды».",
             size=13.5, italic=True, color=MID, line_spacing=1.15)
    # left — mechanism flow + 1 primary case + lesson (v2: decluttered,
    # tool-poisoning detail moved to speaker notes, more whitespace)
    lx, ly, lw, lh = 0.55, 1.92, 6.55, 3.95
    ocean_box(s, lx, ly, lw, lh)
    # mechanism flow
    flow = ["недоверенный\nконтент", "контекст\nмодели", "исполняется\nкак команда"]
    fw = (lw - 0.5 - 2 * 0.30) / 3
    fx = lx + 0.25
    for i, t in enumerate(flow):
        filled_rect(s, fx, ly + 0.28, fw, 0.96,
                    (GOLD if i == 2 else MID), radius=True, radius_adj=0.12)
        text_box(s, fx, ly + 0.28, fw, 0.96, t, size=12, bold=True,
                 color=(DEEP if i == 2 else WHITE), align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.08)
        if i < 2:
            right_arrow(s, fx + fw + 0.02, ly + 0.58, 0.26, 0.40, fill=LIGHT)
        fx += fw + 0.30
    icon(s, "triangle-alert", lx + 0.28, ly + 1.52, 0.40, "mid")
    text_box(s, lx + 0.84, ly + 1.50, lw - 1.10, 0.34, "GitHub MCP heist",
             size=15, bold=True, color=MID)
    text_box(s, lx + 0.28, ly + 1.96, lw - 0.54, 0.86,
             "issue с инструкцией + переизбыточный токен → ассистент выгрузил приватные репозитории",
             size=13, color=DEEP, line_spacing=1.18)
    filled_rect(s, lx + 0.28, ly + 2.96, lw - 0.56, 0.80, GOLD_TINT,
                stroke=GOLD, stroke_pt=1.5, radius=True, radius_adj=0.10)
    text_box(s, lx + 0.46, ly + 3.02, lw - 0.92, 0.68,
             "Катастрофа = инъекция × широкие права. Убери любой из двух — атака не проходит.",
             size=13.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.14)
    # right — 4 rules
    rx, rw = 7.35, 5.45
    ocean_box(s, rx, ly, rw, lh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, rx + 0.28, ly + 0.20, rw - 0.56, 0.36, "4 правила проектирования",
             size=15, bold=True, color=TEAL)
    rules = [
        ("Least-privilege", "минимально необходимые токены/доступы"),
        ("Изоляция недоверенного контента", "отдельно от привилегий"),
        ("Human-in-the-loop на write", "необратимое только через подтверждение человека"),
        ("Allowlist / pin", "только аудированные; фиксировать версии/хеши; deny-by-default"),
    ]
    ry = ly + 0.68
    for i, (t, b) in enumerate(rules):
        circle(s, rx + 0.28, ry + 0.04, 0.32, TEAL)
        text_box(s, rx + 0.28, ry + 0.04, 0.32, 0.32, str(i + 1),
                 size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, rx + 0.72, ry, rw - 0.95, 0.34, t,
                 size=13.5, bold=True, color=DEEP)
        text_box(s, rx + 0.72, ry + 0.34, rw - 0.95, 0.40, b,
                 size=11.5, color=SLATE, line_spacing=1.05)
        ry += 0.80
    footer(s, "Tool poisoning / rug-pull и полная CVE-хронология MCP-инцидентов — в главе/notes, не на видимом слое.")
    speaker_notes(s, load_notes("s25"))


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
    """schema_matrix — COMPRESSED decision matrix 5 axes × 5 architectures
    (v2: owner-decision, was 7×7 cryptic). Readable words, solid semantic
    color (gold=strong / teal=weak), per-column icons, dominant gold plate."""
    s = blank(p)
    slide_title(s, "Матрица выбора.", size=26, y=0.30, h=0.56)
    text_box(s, 0.55, 0.86, 12.25, 0.30,
             "Матрица — структура для аргумента, не сумма баллов. Заливка: золото = сильная сторона, бирюза = слабая.",
             size=12.5, italic=True, color=MID)
    # 5 columns (architectures) + axis col; 5 rows (carrying criteria)
    cols = [
        ("Критерий ↓", None),
        ("Промпт", "terminal"),
        ("RAG", "database"),
        ("Fine-tune", "git-branch"),
        ("Агент", "bot"),
        ("Код (без ИИ)", "check-check"),
    ]
    col_w = [2.70] + [1.95] * 5   # sum = 2.70 + 9.75 = 12.45
    # sem: g = strong (gold solid), t = weak (teal solid), n = neutral (surface)
    rows = [
        ("Знание\nбольшое / меняется",
         [("мало", "t"), ("да", "g"), ("нет", "t"), ("через RAG", "n"), ("—", "n")]),
        ("Свежесть /\nпровенанс",
         [("нет", "t"), ("да + цитата", "g"), ("нет", "t"), ("да", "g"), ("детерм.", "g")]),
        ("Стоимость",
         [("низкая", "g"), ("средняя", "n"), ("высокая разово", "t"), ("кратно выше", "t"), ("минимум", "g")]),
        ("Аудируемость",
         [("средняя", "n"), ("высокая", "g"), ("низкая", "t"), ("низкая", "t"), ("полная", "g")]),
        ("Недетерминизм /\nриск петель",
         [("низкий", "g"), ("низкий", "g"), ("низкий", "g"), ("высокий", "t"), ("нет", "g")]),
    ]
    tx, ty = 0.55, 1.24
    hh = 0.76
    rh = 0.70
    table_h = hh + 5 * rh
    # Ocean motif wrapper behind the matrix (drawn first, behind cells)
    ocean_box(s, 0.40, 1.12, 12.55, table_h + 0.22)
    # header row — icons per column + label
    cx = tx
    for j, (c, ic) in enumerate(cols):
        filled_rect(s, cx, ty, col_w[j], hh, DEEP if j == 0 else MID,
                    radius=False)
        if ic:
            icon(s, ic, cx + col_w[j] / 2 - 0.21, ty + 0.09, 0.30, "white")
            text_box(s, cx + 0.04, ty + 0.42, col_w[j] - 0.08, 0.32, c,
                     size=14, bold=True, color=WHITE,
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                     line_spacing=0.95)
        else:
            text_box(s, cx + 0.10, ty, col_w[j] - 0.18, hh, c,
                     size=14, bold=True, color=WHITE,
                     align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE)
        cx += col_w[j]
    yy = ty + hh
    for ri, (axis, cells) in enumerate(rows):
        cx = tx
        filled_rect(s, cx, yy, col_w[0], rh, SURFACE, stroke=SOFT_GREY,
                    stroke_pt=1.0)
        text_box(s, cx + 0.12, yy, col_w[0] - 0.20, rh, axis,
                 size=14, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.0)
        cx += col_w[0]
        for j, (txt, sem) in enumerate(cells):
            if sem == "g":
                bg, fg, bd = GOLD, DEEP, True
            elif sem == "t":
                bg, fg, bd = TEAL, WHITE, True
            else:
                bg, fg, bd = SURFACE, SLATE, False
            filled_rect(s, cx, yy, col_w[j + 1], rh, bg, stroke=WHITE,
                        stroke_pt=1.5)
            text_box(s, cx + 0.05, yy, col_w[j + 1] - 0.10, rh, txt,
                     size=15, bold=bd, color=fg,
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                     line_spacing=0.95)
            cx += col_w[j + 1]
        yy += rh
    # Dominant gold bottom plate — the actual main message of the slide
    py = yy + 0.20
    plate_h = 7.06 - py
    filled_rect(s, 0.40, py, 12.55, plate_h, GOLD_TINT, stroke=GOLD,
                stroke_pt=3.0, radius=True, radius_adj=0.08)
    icon(s, "check-check", 0.74, py + (plate_h - 0.52) / 2, 0.52, "gold")
    text_box(s, 1.50, py + 0.14, 11.15, plate_h - 0.28,
             "Детерминированная, верифицируемая, повторяемая задача → обычный код, без ИИ. "
             "ИИ добавил бы лишь недетерминизм + стоимость + латентность + поверхность для prompt injection.",
             size=17, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.20)
    speaker_notes(s, load_notes("s27"))


def build_s28(p):
    """summary — 8-step checklist + worked example + mini-apply."""
    s = blank(p)
    slide_title(s, "Чек-лист «прежде чем строить».", size=27)
    # left — 8-step checklist
    lx, ly, lw, lh = 0.55, 1.35, 7.05, 5.45
    ocean_box(s, lx, ly, lw, lh)
    items = [
        "Решается обычным кодом (детерм., верифиц.)? → не добавляй ИИ",
        "Хватит одного промпта (+few-shot/CoT)? → остановись здесь",
        "Знание меняется / нужны свежесть, провенанс? → RAG, не FT",
        "Нужно стабильное поведение / тон / формат? → fine-tuning (PEFT)",
        "Корпус влезает в окно и стабилен? → длинный контекст + кэш",
        "Предсказуема → workflow. Непредсказуема и ценна → агент+лимиты",
        "Подзадачи независимы и параллельны? → мульти-агент; иначе линейный",
        "Данные чувствительны? → карта данных + least-privilege + ZDR/BAA",
    ]
    iy = ly + 0.30
    for i, it in enumerate(items):
        circle(s, lx + 0.28, iy + 0.04, 0.34, MID)
        text_box(s, lx + 0.28, iy + 0.04, 0.34, 0.34, str(i + 1),
                 size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, lx + 0.74, iy, lw - 1.0, 0.58, it,
                 size=12.5, color=DEEP, line_spacing=1.10)
        iy += 0.625
    # right — apply blocks
    rx, rw = 7.85, 4.95
    ocean_box(s, rx, 1.35, rw, 2.0, fill=TEAL_TINT, stroke=TEAL, stroke_pt=2.0)
    text_box(s, rx + 0.26, 1.50, rw - 0.52, 0.34, "Worked example (задача A)",
             size=14, bold=True, color=TEAL)
    text_box(s, rx + 0.26, 1.86, rw - 0.52, 1.40,
             "«2000 регламентов, обновляются еженедельно, ответ со ссылкой на пункт» → шаги 3+8 → RAG со strict grounding. Причины: ось «частота изменений» + ось «провенанс»",
             size=12, color=DEEP, line_spacing=1.16)
    ocean_box(s, rx, 3.50, rw, 1.85)
    text_box(s, rx + 0.26, 3.64, rw - 0.52, 0.34, "Mini-apply (задача B)",
             size=14, bold=True, color=MID)
    text_box(s, rx + 0.26, 3.99, rw - 0.52, 1.30,
             "«бот техподдержки на ~150 коротких FAQ, меняются раз в квартал, ответы из утверждённых формулировок» — пройдите чек-лист сами за 2 минуты",
             size=12, color=DEEP, line_spacing=1.16)
    gold_callout(s, 7.85, 5.50, 4.95, 1.30,
                 "Сначала попытка — потом сверка. Сформулируйте ответ (архитектура + ≥2 причины по осям + ≥1 условие смены) ДО разбора.",
                 size=12.5)
    speaker_notes(s, load_notes("s28"))


def build_s29(p):
    """assertion_visual — human validator + MIT NANDA ~95% donut (c29)."""
    s = blank(p)
    slide_title(s, "Человек-валидатор + урок MIT NANDA.", size=27)
    # left — human validator
    lx, ly, lw, lh = 0.55, 1.40, 6.55, 4.45
    ocean_box(s, lx, ly, lw, lh)
    icon(s, "user-check", lx + 0.26, ly + 0.24, 0.56, "mid")
    text_box(s, lx + 0.96, ly + 0.26, lw - 1.15, 0.55,
             "Агент делает — человек проверяет результат и факты",
             size=15.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.08)
    pts = [
        "против независимого источника истины",
        "на значимых решениях — ДО того, как станет действием",
        "НЕ «убедительно ли звучит рассуждение» (callback s07: self-rationale ≠ контроль)",
        "это шаг check цикла агента + пункт 8 чек-листа + human-in-the-loop на write",
    ]
    py = ly + 1.05
    for t in pts:
        circle(s, lx + 0.30, py + 0.07, 0.12, MID)
        text_box(s, lx + 0.56, py, lw - 0.84, 0.78, t,
                 size=13, color=DEEP, line_spacing=1.14)
        py += 0.82
    # right — NANDA donut
    rx, rw = 7.35, 5.45
    ocean_box(s, rx, ly, rw, 3.10, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    add_image(s, CHARTS / "c29-nanda.png", rx + 0.20, ly + 0.20, 2.45, 2.65)
    text_box(s, rx + 2.75, ly + 0.35, rw - 3.0, 0.95, "~95%",
             size=42, bold=True, color=GOLD, line_spacing=1.0)
    text_box(s, rx + 2.75, ly + 1.30, rw - 3.0, 1.65,
             "корпоративных GenAI-пилотов без измеримого ROI — корень в learning gap и провале интеграции, не в качестве модели",
             size=12.5, color=DEEP, line_spacing=1.18)
    ocean_box(s, rx, ly + 3.25, rw, 1.20)
    text_box(s, rx + 0.26, ly + 3.38, rw - 0.52, 0.95,
             "«Запустить ИИ» ≠ «получить ценность». Решает архитектурно-интеграционная дисциплина. Иногда правильный ответ — простейшая архитектура или не-ИИ.",
             size=12, bold=True, color=DEEP, line_spacing=1.16,
             anchor=MSO_ANCHOR.MIDDLE)
    footer(s, "MIT NANDA, State of AI in Business 2025 — отчёт с методологией (150 интервью + 350 опрос + 300 внедрений), не универсальный закон.")
    speaker_notes(s, load_notes("s29"))


def build_s30(p):
    """summary — bridge to industry lectures + homework (v3 U-6/U-7:
    retitled from function-as-title «Мост к отраслям + задание» to a
    content thesis; Q&A removed → moved to dedicated s31)."""
    s = blank(p)
    slide_title(s, "AI-архитектура — несущая ось отраслевых лекций.",
                size=27)
    # bridge box (top, full width)
    bx, by, bw, bh = 0.55, 1.30, 12.25, 1.62
    ocean_box(s, bx, by, bw, bh)
    icon(s, "route", bx + 0.28, by + 0.26, 0.50, "mid")
    text_box(s, bx + 0.98, by + 0.20, bw - 1.2, 0.46,
             "Модуль 1 закрыт:  Л1 (что такое AI) → Л2 (почему промпт работает) → Л3 (как собрать систему и КАК ВЫБРАТЬ)",
             size=14, bold=True, color=DEEP, line_spacing=1.1,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, bx + 0.98, by + 0.74, bw - 1.2, 0.78,
             "Дальше — отраслевые Лекции 4–17: тот же вопрос в новой обёртке — «какая архитектура и почему именно она, и при каком условии ответ был бы другим»",
             size=13, color=DEEP, line_spacing=1.16)
    # homework block — full width (Q&A column removed, rebalanced mass)
    hx, hy, hw, hh = 0.55, 3.15, 12.25, 2.85
    ocean_box(s, hx, hy, hw, hh, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    icon(s, "clipboard-list", hx + 0.32, hy + 0.30, 0.58, "gold")
    text_box(s, hx + 1.04, hy + 0.28, hw - 1.34, 0.5,
             "Задание — Семинар 3", size=20, bold=True, color=DEEP,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, hx + 1.04, hy + 0.82, hw - 1.34, 0.46,
             "«Архитектурный выбор: чат / агент / RAG / API — 3 кейса»",
             size=15, bold=True, color=MID, line_spacing=1.1)
    text_box(s, hx + 0.42, hy + 1.42, hw - 0.84, 1.30,
             "Применить восьмишаговый чек-лист к 3 кейсам; для каждого: архитектура + ≥2 причины по осям матрицы + ≥1 условие смены выбора + критерий «здесь это было бы НЕ так».  Mini-apply задача B (s28) — разминка перед семинаром.",
             size=14, color=DEEP, line_spacing=1.28)
    # closing takeaway strip (gold-bold thesis, one line)
    gold_callout(s, 0.55, 6.30, 12.25, 0.72,
                 "Аппарат для центрального вопроса собран — прогоняйте чек-лист на каждой отраслевой лекции.",
                 size=15, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s30"))


# ============================================================
# v3 new builders (suffix-ID, plan §4 U-1…U-7) — NO renumber s01–s30.
# ============================================================
def build_subdivider_security(p, sid):
    """Sub-divider Безопасность (U-5a): stays in Раздел 4 (giant «4»,
    roadmap gold on Раздел 4), but distinct subtitle + «· БЕЗОПАСНОСТЬ»
    on the section label. Same template family as build_section_divider."""
    s = blank(p)
    set_slide_bg(s, SURFACE)
    text_box(s, x=8.35, y=0.55, w=4.6, h=5.6, text="4",
             size=380, bold=True, color=COVER_OUTLINE,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    text_box(s, x=0.75, y=1.55, w=7.3, h=0.55,
             text="РАЗДЕЛ 4 · БЕЗОПАСНОСТЬ", size=20, bold=True, color=TEAL)
    filled_rect(s, 0.78, 2.16, 0.7, 0.05, fill=GOLD)
    text_box(s, x=0.75, y=2.55, w=7.5, h=1.85,
             text="Кто видит данные в цепочке", size=38, bold=True,
             color=DEEP, line_spacing=1.08)
    text_box(s, x=0.78, y=4.50, w=7.4, h=1.55,
             text="Разобрали, надёжен ли агент. Теперь — другой вопрос: агент действует через инструменты и внешние API, так кто видит ваши данные и кто может прислать команду?",
             size=18, italic=True, color=LIGHT, line_spacing=1.22)
    roadmap_bar(s, 4, y=6.45)
    speaker_notes(s, load_notes(sid))
    return s


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
    icon(s, "cpu", n1x + bw / 2 - 0.23, by + 0.18, 0.46, "mid")
    text_box(s, n1x + 0.14, by + 0.72, bw - 0.28, 0.34,
             "Предобученная модель", size=14, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER)
    text_box(s, n1x + 0.14, by + 1.04, bw - 0.28, 0.30,
             "общие веса", size=12, italic=True, color=SLATE,
             align=PP_ALIGN.CENTER)
    # «+» between n1 and n2
    text_box(s, plus_x, by + bh / 2 - 0.32, 0.58, 0.64, "+",
             size=30, bold=True, color=MID, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    # node 2 — your dataset
    filled_rect(s, n2x, by, bw, bh, SURFACE, stroke=LIGHT, stroke_pt=1.5,
                radius=True, radius_adj=0.10)
    icon(s, "database", n2x + bw / 2 - 0.23, by + 0.18, 0.46, "teal")
    text_box(s, n2x + 0.14, by + 0.72, bw - 0.28, 0.34,
             "Ваш датасет", size=14, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER)
    text_box(s, n2x + 0.14, by + 1.04, bw - 0.28, 0.30,
             "примеры нужного поведения", size=12, italic=True,
             color=SLATE, align=PP_ALIGN.CENTER)
    # «дообучение» label ABOVE arrow (clear vertical separation)
    text_box(s, arr_x0 - 0.05, by - 0.42, 1.60, 0.32, "дообучение",
             size=13, bold=True, color=MID, align=PP_ALIGN.CENTER)
    # arrow node2 → node3
    right_arrow(s, arr_x0 + 0.06, by + bh / 2 - 0.21, 1.38, 0.42, fill=MID)
    # node 3 — fine-tuned weights (gold = the changed thing)
    filled_rect(s, n3x, by, bw, bh, GOLD_TINT, stroke=GOLD, stroke_pt=2.0,
                radius=True, radius_adj=0.10)
    icon(s, "sliders-horizontal", n3x + bw / 2 - 0.23, by + 0.18, 0.46,
         "gold")
    text_box(s, n3x + 0.14, by + 0.72, bw - 0.28, 0.34,
             "Дообученные ВЕСА", size=14, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER)
    text_box(s, n3x + 0.14, by + 1.04, bw - 0.28, 0.30,
             "модель уже другая", size=12, italic=True, color=SLATE,
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
                 "Промпт/RAG = «что показать модели».  Fine-tuning = «изменить саму модель».",
                 size=15)
    speaker_notes(s, load_notes("s13b"))


def build_s23a(p):
    """section_divider (sub) — Безопасность в Разделе 4 (U-5a)."""
    build_subdivider_security(p, "s23a")


def build_s25a(p):
    """section_divider — Раздел 5 «Как выбрать: фреймворк решения» (U-5b)."""
    build_section_divider(
        p, 5, "Раздел 5", "Как выбрать: фреймворк решения",
        "Мы разобрали все архитектуры по отдельности — и где каждая проваливается. Теперь соберём это в один инструмент выбора.",
        "s25a")


def build_s31(p):
    """qa_minimal — dedicated final Q&A slide (U-7).

    Mirrors lec-02 s29 dedicated Q&A: huge centered «Вопросы» in DEEP,
    «Спасибо за внимание» in MID, quiet reminder bottom. White bg,
    no footer / no roadmap-bar — visual quiet for open Q&A. Ocean motif
    NOT used (cover-family quiet, like lec-02 dedicated Q&A)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    text_box(s, x=0.55, y=2.20, w=12.25, h=2.30, text="Вопросы",
             size=120, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.0)
    text_box(s, x=0.55, y=4.70, w=12.25, h=0.78,
             text="Спасибо за внимание", size=32, bold=False, color=MID,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.2)
    text_box(s, x=0.55, y=6.40, w=12.25, h=0.50,
             text="Семинар 3 «Архитектурный выбор» — на следующей неделе.  Дополнительные вопросы — на e-mail.",
             size=14, italic=True, color=LIGHT,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.2)
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
    # plan §4 presentation order — suffix slides inserted WITHOUT renumber:
    #   s01..s04 → s04a → s05..s08 → s09 → s10..s13 → s13a → s13b →
    #   s14..s17 → s18 → s19..s23 → s23a → s24..s25 → s25a →
    #   s26..s29 → s30 → s31  (36 total)
    builders = [
        build_s01, build_s02, build_s03, build_s04,
        build_s04a,                                   # +U-1 divider Р1
        build_s05, build_s06, build_s07, build_s08,
        build_s09, build_s10, build_s11, build_s12, build_s13,
        build_s13a,                                   # +U-3 divider Р3
        build_s13b,                                   # +U-2 определение FT
        build_s14, build_s15, build_s16, build_s17,
        build_s18, build_s19, build_s20, build_s21, build_s22, build_s23,
        build_s23a,                                   # +U-5a sub-div Безоп.
        build_s24, build_s25,
        build_s25a,                                   # +U-5b divider Р5
        build_s26, build_s27, build_s28, build_s29,
        build_s30,                                    # ретайтл U-6, Q&A→s31
        build_s31,                                    # +U-7 dedicated Q&A
    ]
    assert len(builders) == 36, f"expected 36 builders, got {len(builders)}"
    for b in builders:
        b(p)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    p.save(str(OUT))
    print(f"saved {OUT} — {len(p.slides.__iter__.__self__._sldIdLst)} slides")


if __name__ == "__main__":
    main()
