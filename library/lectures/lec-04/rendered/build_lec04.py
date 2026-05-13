"""
Full 29-slide build of Лекции 4 «AI в медицине и фармацевтике» (Phase 6 visual loop).

Source-of-truth: deck.yaml v2 + chapter v2 (status=reviewed, 12,692 слов) +
slides/*.md (29 файлов с readable speaker notes 150-300 слов).

Issue #73 · Branch: issue-73-lec-04-medicine-production

Palette LOCKED v3: Ocean Gradient (#21295C / #065A82 / #1C7293) + Teal (#028090)
secondary + Gold (#F0AB00) ≥1×/slide.
Visual motif: «Ocean rounded box» (radius 12, surface #F4F7FA, stroke #1C7293 1.5pt).

Canvas: 13.333" × 7.5" (16:9). Pacing per deck.yaml ≈ 75 мин.

Build via: python3 build_lec04.py — generates lec-04.pptx.
"""
import re
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
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
SLATE   = RGBColor(0x6B, 0x76, 0x85)
COVER_OUTLINE = RGBColor(0xD9, 0xE2, 0xEC)
GOLD_TINT = RGBColor(0xFE, 0xF5, 0xE0)
TEAL_TINT = RGBColor(0xE6, 0xF2, 0xF4)
SOFT_GREY = RGBColor(0xE5, 0xEA, 0xF0)
DARK_GREY = RGBColor(0x4A, 0x55, 0x6B)
GREEN_OK  = RGBColor(0x2E, 0x8B, 0x57)
RED_WARN  = RGBColor(0xC0, 0x39, 0x2B)

# === Constants ===
SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5
ROOT = Path("/home/levko/AI-usage-lessons/library/lectures/lec-04")
ASSETS = ROOT / "assets"
SLIDES_DIR = ROOT / "slides"
OUT = ROOT / "rendered/lec-04.pptx"
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
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def disable_shadow(shp):
    sppr = shp._element.spPr
    for el in sppr.findall("{http://schemas.openxmlformats.org/drawingml/2006/main}effectLst"):
        sppr.remove(el)
    etree.SubElement(sppr, "{http://schemas.openxmlformats.org/drawingml/2006/main}effectLst")


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
        adj = max(0.04, min(0.25, (radius_pt / 72.0) / max(min(w, h) / 2.0, 0.5)))
        shp.adjustments[0] = adj
    except Exception:
        pass
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    shp.line.color.rgb = stroke; shp.line.width = Pt(stroke_pt)
    disable_shadow(shp)
    return shp


def filled_rect(slide, x, y, w, h, fill, *, stroke=None, stroke_pt=0.0, radius=False, radius_adj=0.16):
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


def right_arrow(slide, x, y, w, h, fill=MID, stroke=None):
    """Right-pointing arrow shape for pipelines."""
    shp = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(1.0)
    disable_shadow(shp)
    return shp


def chip(slide, x, y, w, h, text, *, fill=MID, stroke=None, color=WHITE, size=14, bold=True):
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
    tf.margin_top = Inches(0.04); tf.margin_bottom = Inches(0.04)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.word_wrap = False
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = text
    r.font.name = FONT_BODY; r.font.size = Pt(size)
    r.font.bold = bold; r.font.color.rgb = color
    disable_shadow(shp)
    return shp


def add_image(slide, path, x, y, w=None, h=None, preserve_aspect=True):
    """Add image to slide.

    When both w and h are passed AND preserve_aspect=True (default), the
    image is fit inside the (w, h) bounding box without distortion — the
    constraining dimension determines the scale, and the image is centered
    along the unconstrained dimension. This avoids non-proportional
    stretching (which was the bug per user feedback 2026-05-13).

    Set preserve_aspect=False to use legacy stretch-to-fit behavior.
    """
    if not Path(path).exists():
        return
    if preserve_aspect and w is not None and h is not None:
        try:
            img = Image.open(path)
            img_w, img_h = img.size
            img.close()
        except Exception:
            # Fallback: if PIL can't open (e.g. exotic format), use width-only
            slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                     width=Inches(w))
            return
        img_ratio = img_w / img_h
        box_ratio = w / h
        if img_ratio > box_ratio:
            # Image wider than box — constrain by width, center vertically
            actual_h = w / img_ratio
            y_offset = (h - actual_h) / 2
            slide.shapes.add_picture(str(path), Inches(x), Inches(y + y_offset),
                                     width=Inches(w))
        else:
            # Image taller than box — constrain by height, center horizontally
            actual_w = h * img_ratio
            x_offset = (w - actual_w) / 2
            slide.shapes.add_picture(str(path), Inches(x + x_offset), Inches(y),
                                     height=Inches(h))
    elif w is not None and h is not None:
        # Legacy stretch-to-fit (explicit opt-in via preserve_aspect=False)
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 width=Inches(w), height=Inches(h))
    elif w is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y), width=Inches(w))
    else:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y))


def slide_title(slide, text, *, y=0.45, h=1.15, w=12.3, x=0.55, size=26,
                color=DEEP, bold=True, line_spacing=1.18, align=PP_ALIGN.LEFT):
    text_box(slide, x=x, y=y, w=w, h=h, text=text,
             size=size, bold=bold, color=color, line_spacing=line_spacing,
             align=align)


def gold_callout(slide, x, y, w, h, text, *, size=15, bold=True):
    box = filled_rect(slide, x, y, w, h, GOLD_TINT, stroke=GOLD, stroke_pt=1.2,
                      radius=True, radius_adj=0.12)
    text_box(slide, x=x + 0.2, y=y + 0.08, w=w - 0.4, h=h - 0.16, text=text,
             size=size, bold=bold, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.LEFT, line_spacing=1.25)


def speaker_notes(slide, text):
    notes = slide.notes_slide
    tf = notes.notes_text_frame
    tf.text = text


def load_notes(slide_id):
    """Extract Speaker notes block from slide markdown (verbatim copy)."""
    files = list(SLIDES_DIR.glob(f"{slide_id}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding='utf-8')
    notes_match = re.search(r'## Speaker notes\s*\n(.*?)(?=\n## |\n---\s*\n## |\Z)', md, re.DOTALL)
    notes = notes_match.group(1).strip() if notes_match else ""
    notes = re.sub(r'\n+---\s*$', '', notes)
    return notes.strip()


# ============================================================
# Slide builders — 29 slides
# ============================================================

def build_s01(p):
    s = blank(p)
    text_box(s, x=0.55, y=0.6, w=5.9, h=2.6,
             text="AI ставит метку патологии на рентгене за ~3 секунды — локально в браузере, без облака.",
             size=26, bold=True, color=DEEP, line_spacing=1.20)
    text_box(s, x=0.55, y=3.4, w=5.9, h=1.2,
             text="Это narrow CV, не ChatGPT. Узкая модель решает одну задачу — классификацию рентгена.",
             size=15, italic=True, color=MID, line_spacing=1.30)
    text_runs(s, 0.55, 5.0, 5.9, 1.7, [
        {"text": "На экране — ", "size": 15, "color": DEEP},
        {"text": "Chester AI", "size": 15, "color": MID, "bold": True},
        {"text": " (Cohen et al., 2019, Mila/McGill).", "size": 15, "color": DEEP},
        {"newpara": True, "text": "~3 сек инференса", "size": 15, "color": GOLD, "bold": True},
        {"text": "  ·  ", "size": 15, "color": DEEP},
        {"text": "локально в браузере", "size": 15, "color": TEAL, "bold": True},
        {"newpara": True, "text": "18 патологий: пневмония, кардиомегалия, ателектаз…",
         "size": 14, "color": SLATE, "italic": True},
    ], line_spacing=1.35)
    box_x, box_y, box_w, box_h = 6.65, 0.55, 6.3, 4.6
    ocean_box(s, box_x, box_y, box_w, box_h)
    pad = 0.18
    img_w = box_w - 2 * pad
    img_h = img_w * 720.0 / 1200.0
    if img_h > box_h - 2 * pad:
        img_h = box_h - 2 * pad
        img_w = img_h * 1200.0 / 720.0
    img_x = box_x + (box_w - img_w) / 2
    img_y = box_y + (box_h - img_h) / 2
    add_image(s, ASSETS / "backup/chester-pneumonia-result.png", img_x, img_y, img_w, img_h)
    text_box(s, x=box_x, y=box_y + box_h + 0.05, w=box_w, h=0.4,
             text="Chester AI · mlmed.org/tools/xray/ · тепловая карта + 18 классов",
             size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, x=0.55, y=7.0, w=12.3, h=0.35,
             text="Cohen et al. 2019 (arXiv:1901.11210) · резервный PNG (живой демо — при наличии интернета)",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s01"))


def build_s02(p):
    s = blank(p)
    set_slide_bg(s, SURFACE)
    text_box(s, x=8.0, y=2.0, w=5.3, h=5.5, text="04",
             size=320, bold=True, color=COVER_OUTLINE,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line_spacing=1.0)
    text_box(s, x=0.7, y=1.0, w=6.5, h=0.55, text="ЛЕКЦИЯ",
             size=18, bold=True, color=TEAL, align=PP_ALIGN.LEFT)
    filled_rect(s, 0.72, 1.55, 0.7, 0.05, fill=TEAL)
    text_box(s, x=0.7, y=2.0, w=8.5, h=2.6, text="AI в медицине\nи фармацевтике",
             size=58, bold=True, color=DEEP, line_spacing=1.05, align=PP_ALIGN.LEFT)
    filled_rect(s, 0.7, 5.45, 0.05, 0.55, fill=TEAL)
    text_box(s, x=0.95, y=5.45, w=10.5, h=0.6,
             text="Какие AI-обещания в медицине сбылись — и кто отвечает за ошибки.",
             size=20, color=MID, italic=False, align=PP_ALIGN.LEFT, line_spacing=1.25)
    text_box(s, x=0.95, y=6.15, w=10.5, h=0.35,
             text="Курс «AI в разных индустриях»  ·  75 мин  ·  13 мая 2026",
             size=14, italic=True, color=LIGHT, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s02"))


def build_s03(p):
    s = blank(p)
    text_box(s, x=0.55, y=0.35, w=12.3, h=0.65,
             text="ПОДНИМИТЕ РУКИ",
             size=24, bold=True, color=GOLD, align=PP_ALIGN.LEFT, line_spacing=1.1)
    slide_title(s, "Сначала — ваша оценка, потом — данные.", y=0.95, size=24)
    card_y = 1.95
    card_h = 4.8
    card_w = 4.05
    gap = 0.15
    q1_x = 0.55
    ocean_box(s, q1_x, card_y, card_w, card_h)
    add_image(s, ASSETS / "icons/lucide-hand-blue.png",
              x=q1_x + 0.30, y=card_y + 0.30, w=0.85, h=0.85)
    text_box(s, x=q1_x + 1.25, y=card_y + 0.35, w=card_w - 1.35, h=0.30,
             text="Q1  ·  один вариант",
             size=12, bold=True, color=MID)
    text_box(s, x=q1_x + 0.30, y=card_y + 1.3, w=card_w - 0.6, h=1.2,
             text="Сколько AI-устройств одобрено FDA к концу 2025?",
             size=17, bold=True, color=DEEP, line_spacing=1.20)
    chips1 = ["< 100", "100 – 500", "500 – 1 000", "> 1 000"]
    chip_y = card_y + 2.85
    chip_h = 0.42
    chip_w = card_w - 0.6
    for i, ctxt in enumerate(chips1):
        y = chip_y + i * (chip_h + 0.05)
        chip(s, q1_x + 0.30, y, chip_w, chip_h, ctxt, fill=MID, color=WHITE, size=13)
    q2_x = q1_x + card_w + gap
    ocean_box(s, q2_x, card_y, card_w, card_h)
    add_image(s, ASSETS / "icons/lucide-stethoscope-blue.png",
              x=q2_x + 0.30, y=card_y + 0.30, w=0.85, h=0.85)
    text_box(s, x=q2_x + 1.25, y=card_y + 0.35, w=card_w - 1.35, h=0.30,
             text="Q2  ·  личный опыт",
             size=12, bold=True, color=TEAL)
    text_box(s, x=q2_x + 0.30, y=card_y + 1.3, w=card_w - 0.6, h=1.2,
             text="Получали медицинский результат с участием AI за год?",
             size=17, bold=True, color=DEEP, line_spacing=1.20)
    chips2 = ["Да", "Нет", "Не уверен(а)"]
    cy = card_y + 2.85
    for i, ctxt in enumerate(chips2):
        y = cy + i * (chip_h + 0.05)
        chip(s, q2_x + 0.30, y, chip_w, chip_h, ctxt, fill=WHITE, color=TEAL,
             stroke=TEAL, size=13)
    q3_x = q2_x + card_w + gap
    ocean_box(s, q3_x, card_y, card_w, card_h)
    add_image(s, ASSETS / "icons/lucide-scale-blue.png",
              x=q3_x + 0.30, y=card_y + 0.30, w=0.85, h=0.85)
    text_box(s, x=q3_x + 1.25, y=card_y + 0.35, w=card_w - 1.35, h=0.30,
             text="Q3  ·  доверие",
             size=12, bold=True, color=MID)
    text_box(s, x=q3_x + 0.30, y=card_y + 1.3, w=card_w - 0.6, h=1.2,
             text="Доверяете AI-диагнозу больше, чем человеческому?",
             size=17, bold=True, color=DEEP, line_spacing=1.20)
    chips3 = ["Да", "Нет", "Зависит"]
    for i, ctxt in enumerate(chips3):
        y = cy + i * (chip_h + 0.05)
        chip(s, q3_x + 0.30, y, chip_w, chip_h, ctxt, fill=MID, color=WHITE, size=13)
    text_box(s, x=0.55, y=7.0, w=12.3, h=0.35,
             text="Запомните свои ответы — сравним с реальностью на следующем слайде.",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s03"))


def build_s04(p):
    s = blank(p)
    slide_title(s, "AI в медицине — уже не «будущее», а рабочая инфраструктура.", size=24)
    # P1-24: s04 differentiates from s07 — здесь poll reveal (mega-stat 1 451),
    # на s07 — полный growth chart.
    chart_x, chart_y, chart_w, chart_h = 0.55, 1.85, 7.3, 4.7
    ocean_box(s, chart_x, chart_y, chart_w, chart_h)
    text_box(s, x=chart_x + 0.3, y=chart_y + 0.20, w=chart_w - 0.6, h=0.40,
             text="FDA — AI/ML-устройства, одобренные для медицины",
             size=14, bold=True, color=DEEP, line_spacing=1.20)
    text_box(s, x=chart_x + 0.3, y=chart_y + 0.65, w=chart_w - 0.6, h=0.35,
             text="накопленным итогом · к концу 2025",
             size=12, italic=True, color=LIGHT)
    # Mega-stat reveal (1 451) — gold, dominant.
    text_box(s, x=chart_x + 0.3, y=chart_y + 1.20, w=chart_w - 0.6, h=2.0,
             text="1 451",
             size=140, bold=True, color=GOLD, line_spacing=1.0,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP)
    text_box(s, x=chart_x + 0.3, y=chart_y + 3.25, w=chart_w - 0.6, h=0.40,
             text="одобрено к концу 2025",
             size=15, italic=True, color=DEEP, align=PP_ALIGN.CENTER)
    # 3 secondary stats.
    sub_y = chart_y + 3.85
    sub_w = (chart_w - 0.6) / 3
    sub_stats = [
        ("76%", "радиология (CV)"),
        ("+295", "новых в 2025"),
        ("+258", "новых в 2024"),
    ]
    for i, (val, lbl) in enumerate(sub_stats):
        x = chart_x + 0.3 + i * sub_w
        text_box(s, x=x, y=sub_y, w=sub_w, h=0.45,
                 text=val, size=22, bold=True, color=MID,
                 align=PP_ALIGN.CENTER, line_spacing=1.0)
        text_box(s, x=x, y=sub_y + 0.45, w=sub_w, h=0.35,
                 text=lbl, size=11, italic=True, color=SLATE,
                 align=PP_ALIGN.CENTER)
    info_x, info_y, info_w, info_h = chart_x + chart_w + 0.25, 1.85, 4.9, 4.7
    ocean_box(s, info_x, info_y, info_w, info_h)
    text_box(s, x=info_x + 0.3, y=info_y + 0.20, w=info_w - 0.6, h=0.45,
             text="mosmed.ai — 5 лет работы",
             size=16, bold=True, color=DEEP, line_spacing=1.10)
    text_box(s, x=info_x + 0.3, y=info_y + 0.70, w=info_w - 0.6, h=0.35,
             text="ДЗМ Москвы → MosMedAI (май 2024)",
             size=10, italic=True, color=LIGHT)
    stats = [
        ("14 млн+", "исследований", GOLD),
        ("74", "региона РФ", MID),
        ("2 000+", "медорганизаций", MID),
        ("18 млн+", "изображений", MID),
        ("70", "AI-сервисов", MID),
        ("11", "нац. стандартов", MID),
    ]
    grid_y = info_y + 1.25
    cell_w = (info_w - 0.6) / 2
    for i, (val, lbl, color) in enumerate(stats):
        col = i % 2
        row = i // 2
        cx = info_x + 0.3 + col * cell_w
        cy = grid_y + row * 1.05
        text_box(s, x=cx, y=cy, w=cell_w, h=0.55,
                 text=val, size=22, bold=True, color=color, line_spacing=1.05)
        text_box(s, x=cx, y=cy + 0.55, w=cell_w, h=0.40,
                 text=lbl, size=11, color=SLATE, italic=True)
    text_box(s, x=0.55, y=7.0, w=12.3, h=0.35,
             text="FDA AI/ML list (к концу 2025, theimagingwire.com 10.12.2025) · Remedium 2025 · mos.ru AI Leaders Award.",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s04"))


def build_s05(p):
    s = blank(p)
    qbox_x, qbox_y, qbox_w, qbox_h = 0.55, 0.6, 12.25, 3.0
    ocean_box(s, qbox_x, qbox_y, qbox_w, qbox_h)
    text_box(s, x=qbox_x + 0.5, y=qbox_y + 0.35, w=qbox_w - 1.0, h=0.45,
             text="ЦЕНТРАЛЬНЫЙ ВОПРОС ЛЕКЦИИ",
             size=14, bold=True, color=TEAL, align=PP_ALIGN.LEFT)
    text_runs(s, qbox_x + 0.5, qbox_y + 0.85, qbox_w - 1.0, qbox_h - 1.1, [
        {"text": "Какие AI-обещания в медицине ", "size": 30, "color": DEEP, "bold": True},
        {"text": "реально сбылись", "size": 30, "color": GOLD, "bold": True},
        {"text": " к 2026 году — и ", "size": 30, "color": DEEP, "bold": True},
        {"text": "кто отвечает", "size": 30, "color": GOLD, "bold": True},
        {"text": ", когда AI-диагноз ошибочен?", "size": 30, "color": DEEP, "bold": True},
    ], line_spacing=1.25, anchor=MSO_ANCHOR.MIDDLE)
    rm_x, rm_y, rm_w, rm_h = 0.55, 3.85, 6.5, 2.9
    ocean_box(s, rm_x, rm_y, rm_w, rm_h)
    text_box(s, x=rm_x + 0.3, y=rm_y + 0.2, w=rm_w - 0.6, h=0.4,
             text="Маршрут лекции — 4 раздела",
             size=14, bold=True, color=MID)
    roadmap = [
        ("1", "Карта AI в медицине"),
        ("2", "AI-диагностика как зеркало"),
        ("3", "Разработка лекарств — обещания vs реальность"),
        ("4", "Этика и ответственность"),
    ]
    rm_item_y = rm_y + 0.75
    for i, (num, label) in enumerate(roadmap):
        y = rm_item_y + i * 0.50
        filled_rect(s, rm_x + 0.30, y, 0.45, 0.45, MID, radius=True, radius_adj=0.5)
        text_box(s, x=rm_x + 0.30, y=y, w=0.45, h=0.45,
                 text=num, size=15, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rm_x + 0.85, y=y + 0.05, w=rm_w - 1.1, h=0.40,
                 text=label, size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    img_x, img_y, img_w, img_h = 7.30, 3.85, 5.5, 2.9
    ocean_box(s, img_x, img_y, img_w, img_h)
    # Real medical photo (Unsplash CC0) — врач+ноутбук+стетоскоп. Контент,
    # не баннер: studio-quality иллюстрация связки AI(ноутбук) + медицина(стетоскоп).
    add_image(s, ASSETS / "photos/s05-doctor-laptop.jpg",
              x=img_x + 0.2, y=img_y + 0.25, w=img_w - 0.4, h=img_h - 0.85)
    text_box(s, x=img_x + 0.2, y=img_y + img_h - 0.50, w=img_w - 0.4, h=0.35,
             text="Врач + ноутбук + стетоскоп — где AI встречает клиническую работу",
             size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, x=0.55, y=6.95, w=12.3, h=0.35,
             text="Стейкс: $22–38 млрд (2025), прогноз > $100 млрд к 2030 (MarketsAndMarkets, Towards Healthcare).",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s05"))


def build_s06(p):
    s = blank(p)
    slide_title(s, "AI в медицине — 4 разные индустрии, не один набор инструментов.", size=24)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="Модальность данных × охват = карта применений",
             size=15, italic=True, color=MID)
    grid_x, grid_y, grid_w, grid_h = 1.65, 1.95, 10.45, 4.6
    cell_w = grid_w / 2
    cell_h = grid_h / 2
    cells = [
        ("AI-диагностика", "КТ · МРТ · рентген · дермато-скан",
         "mosmed.ai · IDx-DR · Aidoc",
         "lucide-scan-blue.png", MID, 0, 0),
        ("Популяционная визуализация", "Скрининговые программы",
         "MASAI (Швеция) · BreastScreen",
         "lucide-heart-pulse-blue.png", LIGHT, 1, 0),
        ("Персонализированная медицина", "Геномный AI · клинические решения",
         "Tempus · Foundation Med · Webiomed",
         "lucide-pill-blue.png", LIGHT, 0, 1),
        ("Разработка лекарств + эпид.", "Генеративная химия · структуры белков",
         "AlphaFold · Insilico · Generate Bio",
         "lucide-flask-conical-blue.png", MID, 1, 1),
    ]
    for title, sub, exs, icon, color, col, row in cells:
        x = grid_x + col * cell_w
        y = grid_y + row * cell_h
        ocean_box(s, x + 0.1, y + 0.1, cell_w - 0.2, cell_h - 0.2)
        add_image(s, ASSETS / "icons" / icon, x=x + 0.3, y=y + 0.30, w=0.7, h=0.7)
        text_box(s, x=x + 1.15, y=y + 0.25, w=cell_w - 1.35, h=0.75,
                 text=title, size=16, bold=True, color=color, line_spacing=1.15)
        text_box(s, x=x + 0.3, y=y + 1.25, w=cell_w - 0.5, h=0.55,
                 text=sub, size=13, color=DEEP, italic=True)
        text_box(s, x=x + 0.3, y=y + 1.80, w=cell_w - 0.5, h=0.50,
                 text=exs, size=12, color=SLATE)
    # Gold dots — AI-диагностика (top-left) и Разработка лекарств (bottom-right).
    filled_rect(s, grid_x + 0.15, grid_y + 0.15, 0.18, 0.18, GOLD, radius=True, radius_adj=0.5)
    filled_rect(s, grid_x + cell_w + 0.15, grid_y + cell_h + 0.15, 0.18, 0.18, GOLD, radius=True, radius_adj=0.5)
    text_box(s, x=grid_x, y=grid_y + grid_h + 0.1, w=grid_w, h=0.35,
             text="◄ один пациент        ОХВАТ        популяция / фарма ►",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER, italic=True)
    text_box(s, x=0.40, y=grid_y, w=1.15, h=grid_h,
             text="МОДАЛЬНОСТЬ\n\n▲ изображения /\n   сигналы\n\n\n▼ текст /\n   молекулы",
             size=10, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)
    text_box(s, x=0.55, y=7.10, w=12.3, h=0.35,
             text="Фокус лекции — квадранты с золотыми точками: AI-диагностика + разработка лекарств.",
             size=12, italic=True, color=GOLD, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s06"))


def build_s07(p):
    s = blank(p)
    slide_title(s, "За 10 лет — от 6 до 1 451 AI-устройства, одобренных FDA.", size=24)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="Это инфраструктура, не футурология.",
             size=15, italic=True, color=MID)
    chart_x, chart_y, chart_w, chart_h = 0.55, 1.95, 9.0, 4.7
    ocean_box(s, chart_x, chart_y, chart_w, chart_h)
    img_w = chart_w - 0.4
    img_h = img_w * 540.0 / 900.0
    if img_h > chart_h - 0.8:
        img_h = chart_h - 0.8
        img_w = img_h * 900.0 / 540.0
    img_x = chart_x + (chart_w - img_w) / 2
    img_y = chart_y + 0.30
    add_image(s, ASSETS / "charts/c1-fda-bar.png", img_x, img_y, img_w, img_h)
    text_box(s, x=chart_x + 0.3, y=chart_y + chart_h - 0.40, w=chart_w - 0.6, h=0.35,
             text="AI/ML-устройства, одобренные FDA для медицины · накопленным итогом · к концу 2025.",
             size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    info_x, info_y, info_w, info_h = chart_x + chart_w + 0.25, 1.95, 3.45, 4.7
    ocean_box(s, info_x, info_y, info_w, info_h)
    text_box(s, x=info_x + 0.3, y=info_y + 0.3, w=info_w - 0.6, h=0.45,
             text="Ключевые числа", size=15, bold=True, color=DEEP)
    text_box(s, x=info_x + 0.3, y=info_y + 0.85, w=info_w - 0.6, h=0.7,
             text="1 451", size=44, bold=True, color=GOLD, line_spacing=1.0)
    text_box(s, x=info_x + 0.3, y=info_y + 1.45, w=info_w - 0.6, h=0.35,
             text="накопленным итогом · к концу 2025", size=10, italic=True, color=SLATE)
    text_box(s, x=info_x + 0.3, y=info_y + 1.95, w=info_w - 0.6, h=0.5,
             text="76%", size=32, bold=True, color=MID, line_spacing=1.0)
    text_box(s, x=info_x + 0.3, y=info_y + 2.45, w=info_w - 0.6, h=0.35,
             text="радиология (CV)", size=11, italic=True, color=SLATE)
    text_box(s, x=info_x + 0.3, y=info_y + 2.95, w=info_w - 0.6, h=0.5,
             text="+295", size=32, bold=True, color=MID, line_spacing=1.0)
    text_box(s, x=info_x + 0.3, y=info_y + 3.45, w=info_w - 0.6, h=0.35,
             text="новых в 2025", size=11, italic=True, color=SLATE)
    text_box(s, x=info_x + 0.3, y=info_y + 3.95, w=info_w - 0.6, h=0.65,
             text="Перелом — 2022–2024:\nэкспоненциальный рост",
             size=11, italic=True, color=GOLD, line_spacing=1.20)
    text_box(s, x=0.55, y=7.0, w=12.3, h=0.35,
             text="FDA AI/ML list (fda.gov, к концу 2025) · JAMA Network Open systematic review 2025 · The Imaging Wire 10.12.2025.",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s07"))


def build_s08(p):
    s = blank(p)
    slide_title(s, "Медицина — инструктивный пример для инженера.", size=24)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="Высокие ставки + строгое регулирование + прозрачные операционные метрики.",
             size=15, italic=True, color=MID)
    cards = [
        ("Высокие ставки",
         "Ошибка модели → ошибка диагноза → вред пациенту.",
         "Калибровка уверенности модели, audit-trail, fallback-сценарии.",
         "lucide-alert-triangle-blue.png", MID),
        ("Строгое регулирование",
         "FDA SaMD · EU AI Act high-risk · Росздравнадзор.",
         "Регуляторные навыки переносятся в финансы, авто, авиа.",
         "lucide-shield-blue.png", LIGHT),
        ("Прозрачные операционные метрики",
         "mosmed.ai: 14 млн+ исследований · 74 региона · 70 сервисов.",
         "Метрики измеримы — не маркетинговая оценка.",
         "lucide-coins-blue.png", MID),
    ]
    card_y = 2.0
    card_h = 4.4
    card_w = 4.05
    gap = 0.15
    for i, (title, line1, line2, icon, color) in enumerate(cards):
        x = 0.55 + i * (card_w + gap)
        ocean_box(s, x, card_y, card_w, card_h)
        add_image(s, ASSETS / "icons" / icon, x=x + 0.30, y=card_y + 0.35, w=1.0, h=1.0)
        text_box(s, x=x + 0.30, y=card_y + 1.50, w=card_w - 0.6, h=0.75,
                 text=title, size=20, bold=True, color=color, line_spacing=1.20)
        text_box(s, x=x + 0.30, y=card_y + 2.35, w=card_w - 0.6, h=1.1,
                 text=line1, size=14, color=DEEP, line_spacing=1.30)
        text_box(s, x=x + 0.30, y=card_y + 3.40, w=card_w - 0.6, h=0.95,
                 text=line2, size=12, italic=True, color=SLATE, line_spacing=1.30)
    gold_callout(s, 0.55, 6.55, 12.3, 0.55,
                 "→ Регуляторные навыки переносятся: PCI DSS · ФЗ-152 · ISO 26262 · DO-178C.",
                 size=14)
    speaker_notes(s, load_notes("s08"))


def build_s09(p):
    s = blank(p)
    slide_title(s, "AI-диагностика — это компьютерное зрение, не LLM.", size=24)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="изображение → метка с оценкой уверенности. Это не LLM.",
             size=15, italic=True, color=MID)
    pipe_y = 2.0
    pipe_h = 2.6
    # Gold on stage 2 «Модель» — central message of slide: «CV CNN/ViT, не LLM».
    stages = [
        ("Вход", "Изображение\nDICOM / PNG / JPEG\n(препроцессинг)", LIGHT),
        ("Модель", "CNN / ViT\n(не LLM)\nдообучение на мед. данных", GOLD),
        ("Выход", "Вероятность +\nтепловая карта / bbox\n(Grad-CAM*)", MID),
        ("Внедрение", "Врач: решение\n+ верификация + подпись", DEEP),
    ]
    total_w = 12.3
    n = len(stages)
    arrow_w = 0.55
    stage_w = (total_w - (n - 1) * arrow_w) / n
    pipe_x = 0.55
    for i, (title, body, color) in enumerate(stages):
        x = pipe_x + i * (stage_w + arrow_w)
        is_gold = (color == GOLD)
        fill_color = GOLD_TINT if is_gold else SURFACE
        stroke = GOLD if is_gold else LIGHT
        ocean_box(s, x, pipe_y, stage_w, pipe_h, fill=fill_color, stroke=stroke)
        filled_rect(s, x + 0.20, pipe_y + 0.20, stage_w - 0.40, 0.55, color, radius=True, radius_adj=0.20)
        text_box(s, x=x + 0.20, y=pipe_y + 0.20, w=stage_w - 0.40, h=0.55,
                 text=f"{i+1}. {title}",
                 size=15, bold=True, color=WHITE if not is_gold else DEEP,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=x + 0.20, y=pipe_y + 0.85, w=stage_w - 0.40, h=pipe_h - 1.0,
                 text=body, size=13, color=DEEP, line_spacing=1.30,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < n - 1:
            ax = x + stage_w + 0.05
            right_arrow(s, ax, pipe_y + pipe_h / 2 - 0.25, arrow_w - 0.10, 0.50,
                        fill=MID)
    sample_x, sample_y, sample_w, sample_h = 0.55, 4.85, 12.3, 2.3
    ocean_box(s, sample_x, sample_y, sample_w, sample_h)
    text_box(s, x=sample_x + 0.3, y=sample_y + 0.15, w=sample_w - 0.6, h=0.35,
             text="Пример: CheXNet — 121-слойная DenseNet, 14 патологий грудной клетки (Rajpurkar et al. 2017)",
             size=13, bold=True, color=DEEP)
    img_h = 1.6
    img_w = img_h * 1200.0 / 720.0
    img_x = sample_x + 0.3
    img_y = sample_y + 0.55
    add_image(s, ASSETS / "backup/chester-pneumonia-result.png", img_x, img_y, img_w, img_h)
    text_box(s, x=sample_x + 3.2, y=sample_y + 0.65, w=sample_w - 3.5, h=1.5,
             text="Изображение → CNN/ViT → вектор вероятностей + тепловая карта. Тепловая карта = Grad-CAM (Selvaraju 2017): какие пиксели вносили вклад в предсказание. Врач принимает решение, AI — помощник.",
             size=13, color=DEEP, line_spacing=1.40)
    text_box(s, x=0.55, y=7.20, w=12.3, h=0.30,
             text="*Grad-CAM — визуальная интерпретация решения модели. DenseNet — CNN-архитектура. Rajpurkar arXiv:1711.05225 · Selvaraju arXiv:1610.02391.",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s09"))


def build_s10(p):
    s = blank(p)
    slide_title(s, "Для медицинского AI «точности» (accuracy) недостаточно.", size=24)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="Чувствительность · специфичность · распространённость · PPV. Sens/spec не зависят от prev; PPV — зависит.",
             size=13, italic=True, color=MID)
    cm_x, cm_y, cm_w, cm_h = 0.55, 1.85, 5.7, 4.2
    ocean_box(s, cm_x, cm_y, cm_w, cm_h)
    text_box(s, x=cm_x + 0.3, y=cm_y + 0.15, w=cm_w - 0.6, h=0.35,
             text="Матрица ошибок 2 × 2",
             size=14, bold=True, color=DEEP)
    mat_x = cm_x + 0.85
    mat_y = cm_y + 0.95
    mat_w = cm_w - 1.05
    mat_h = cm_h - 1.15
    cell_w = mat_w / 2
    cell_h = (mat_h - 0.5) / 2
    text_box(s, x=mat_x, y=mat_y, w=mat_w, h=0.30,
             text="предсказание AI →",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    text_box(s, x=mat_x, y=mat_y + 0.30, w=cell_w, h=0.30,
             text="положит.",
             size=12, bold=True, color=MID, align=PP_ALIGN.CENTER)
    text_box(s, x=mat_x + cell_w, y=mat_y + 0.30, w=cell_w, h=0.30,
             text="отрицат.",
             size=12, bold=True, color=MID, align=PP_ALIGN.CENTER)
    text_box(s, x=cm_x + 0.15, y=mat_y + 0.85, w=0.7, h=cell_h,
             text="истина\n↓\nболен",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=cm_x + 0.15, y=mat_y + 0.85 + cell_h, w=0.7, h=cell_h,
             text="здоров",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    # Ocean palette per anti-pattern #3 (no red/green semaphore).
    # TP = Ocean light; TN = Ocean mid; FP = gold accent (highlight common error); FN = navy (significant miss).
    tp_fill = RGBColor(0xE3, 0xEE, 0xF3)  # Light Ocean tint
    tn_fill = RGBColor(0xD9, 0xE2, 0xEC)  # Cover outline
    fn_fill = RGBColor(0xD7, 0xDB, 0xE4)  # Navy tint (significant)
    fp_fill = GOLD_TINT
    filled_rect(s, mat_x, mat_y + 0.75, cell_w, cell_h, tp_fill,
                stroke=LIGHT, stroke_pt=0.8)
    text_box(s, x=mat_x, y=mat_y + 0.85, w=cell_w, h=0.30,
             text="TP",
             size=20, bold=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, x=mat_x, y=mat_y + 1.20, w=cell_w, h=0.40,
             text="истинно-полож.\nправильно нашли",
             size=10, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.25)
    filled_rect(s, mat_x + cell_w, mat_y + 0.75, cell_w, cell_h, fn_fill,
                stroke=DEEP, stroke_pt=0.8)
    text_box(s, x=mat_x + cell_w, y=mat_y + 0.85, w=cell_w, h=0.30,
             text="FN",
             size=20, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, x=mat_x + cell_w, y=mat_y + 1.20, w=cell_w, h=0.40,
             text="ложно-отрицат.\nпропустили больного",
             size=10, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.25)
    filled_rect(s, mat_x, mat_y + 0.75 + cell_h, cell_w, cell_h, fp_fill,
                stroke=GOLD, stroke_pt=0.8)
    text_box(s, x=mat_x, y=mat_y + 0.85 + cell_h, w=cell_w, h=0.30,
             text="FP",
             size=20, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, x=mat_x, y=mat_y + 1.20 + cell_h, w=cell_w, h=0.40,
             text="ложно-полож.\nложная тревога",
             size=10, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.25)
    filled_rect(s, mat_x + cell_w, mat_y + 0.75 + cell_h, cell_w, cell_h, tn_fill,
                stroke=MID, stroke_pt=0.8)
    text_box(s, x=mat_x + cell_w, y=mat_y + 0.85 + cell_h, w=cell_w, h=0.30,
             text="TN",
             size=20, bold=True, color=MID, align=PP_ALIGN.CENTER)
    text_box(s, x=mat_x + cell_w, y=mat_y + 1.20 + cell_h, w=cell_w, h=0.40,
             text="истинно-отрицат.\nправильно отпустили",
             size=10, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.25)

    mt_x, mt_y, mt_w, mt_h = cm_x + cm_w + 0.30, 1.85, 6.5, 4.2
    ocean_box(s, mt_x, mt_y, mt_w, mt_h)
    text_box(s, x=mt_x + 0.3, y=mt_y + 0.15, w=mt_w - 0.6, h=0.35,
             text="4 метрики — формула + смысл",
             size=14, bold=True, color=DEEP)
    metrics = [
        ("Чувствительность", "TP / (TP+FN)", "доля больных, которых поймал AI"),
        ("Специфичность", "TN / (TN+FP)", "доля здоровых, не напуганных"),
        ("Распространённость",  "(TP+FN) / всего", "как часто болезнь в популяции"),
        ("PPV", "TP / (TP+FP)", "если AI сказал «болен» — насколько верить"),
    ]
    row_y = mt_y + 0.65
    row_h = 0.78
    for i, (name, formula, meaning) in enumerate(metrics):
        ry = row_y + i * row_h
        is_ppv = name.startswith("PPV")
        text_box(s, x=mt_x + 0.3, y=ry, w=2.45, h=0.40,
                 text=name, size=14, bold=True,
                 color=GOLD if is_ppv else DEEP, line_spacing=1.10)
        text_box(s, x=mt_x + 0.3, y=ry + 0.40, w=2.4, h=0.30,
                 text=formula, size=11, italic=True, color=MID,
                 font=FONT_MONO)
        text_box(s, x=mt_x + 2.85, y=ry + 0.05, w=mt_w - 3.1, h=0.65,
                 text=meaning, size=12, color=DEEP, line_spacing=1.30,
                 anchor=MSO_ANCHOR.MIDDLE)
    gold_callout(s, 0.55, 6.15, 12.3, 0.7,
                 "CheXNet (Rajpurkar 2017): чувствительность 0.94–0.96 · специфичность 0.89–0.93 (диапазон). Для расчёта PPV берём sens 0.94 / spec 0.89  →  PPV ~8% при prev 1% (скрининг)  ·  ~78% при prev 30% (госпиталь).",
                 size=12)
    text_box(s, x=0.55, y=6.95, w=12.3, h=0.35,
             text="Та же модель, та же accuracy — разные PPV. Рабочая точка (operating point) зависит от порога + патологии.",
             size=11, italic=True, color=SLATE)
    speaker_notes(s, load_notes("s10"))


def build_s11(p):
    s = blank(p)
    slide_title(s, "Визуализация: AI+врач > врач. Рассуждения: парадокс augmentation.", size=22)
    text_box(s, x=0.55, y=1.10, w=12.3, h=0.40,
             text="Вопрос «AI или врач» поставлен неправильно. Правильный — «какая задача и какой рабочий процесс».",
             size=13, italic=True, color=MID)
    rows = [
        ("Liu et al. 2019",
         "Lancet Digital Health — мета-анализ, 14 проспективных",
         "Мета-анализ по визуализации",
         "объединённая чувствительность: AI 0.87  ·  врач 0.85",
         "Близко к паритету, исторический baseline",
         MID, False),
        ("MASAI 2024–2025",
         "Lancet Digital Health (2024) + Lancet (2025)",
         "РКИ маммографии, n > 100 000 (Швеция)",
         "чувствит. 80.5% (AI) vs 73.8% (стандарт)  ·  нагрузка −44%  ·  интервальный рак −12%",
         "AI+радиолог — значимо лучше каждого по отдельности",
         MID, True),
        ("Goh et al. 2024",
         "JAMA Network Open (окт. 2024)",
         "Клинические рассуждения, 50 врачей",
         "GPT-4 в одиночку 76%  ·  врач+GPT-4 74%  (p = 0.60)",
         "Парадокс augmentation — AI не улучшил рассуждения врача",
         LIGHT, False),
    ]
    row_y = 1.65
    row_h = 1.65
    for i, (study, journal, domain, result, takeaway, color, is_gold) in enumerate(rows):
        ry = row_y + i * (row_h + 0.05)
        stroke = GOLD if is_gold else LIGHT
        fill = GOLD_TINT if is_gold else SURFACE
        ocean_box(s, 0.55, ry, 12.3, row_h, fill=fill, stroke=stroke, stroke_pt=1.8 if is_gold else 1.5)
        text_box(s, x=0.75, y=ry + 0.15, w=3.0, h=0.40,
                 text=study, size=16, bold=True, color=DEEP, line_spacing=1.15)
        text_box(s, x=0.75, y=ry + 0.55, w=3.0, h=0.55,
                 text=journal, size=10, italic=True, color=SLATE, line_spacing=1.20)
        text_box(s, x=4.0, y=ry + 0.15, w=2.7, h=0.30,
                 text="Область", size=10, bold=True, color=SLATE)
        text_box(s, x=4.0, y=ry + 0.45, w=2.7, h=0.95,
                 text=domain, size=12, color=DEEP, line_spacing=1.30)
        result_w = 4.4 if is_gold else 6.0
        text_box(s, x=6.95, y=ry + 0.15, w=result_w, h=0.30,
                 text="Результат", size=10, bold=True, color=SLATE)
        text_box(s, x=6.95, y=ry + 0.40, w=result_w, h=0.55,
                 text=result, size=12, bold=is_gold, color=DEEP, line_spacing=1.30)
        text_box(s, x=6.95, y=ry + 1.00, w=result_w, h=0.55,
                 text="→ " + takeaway, size=12, italic=True,
                 color=GOLD if is_gold else MID, line_spacing=1.30)
        if is_gold:
            filled_rect(s, 11.45, ry + 0.10, 1.35, 0.60, GOLD, radius=True, radius_adj=0.30)
            text_box(s, x=11.45, y=ry + 0.10, w=1.35, h=0.60,
                     text="ПОБЕДА", size=14, bold=True, color=WHITE,
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.55, y=6.85, w=12.3, h=0.45,
             text="Liu 2019 doi: 10.1016/S2589-7500(19)30123-2  ·  MASAI Lancet 2025  ·  Goh JAMA Netw Open 2024.",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s11"))


def build_s12(p):
    s = blank(p)
    slide_title(s, "mosmed.ai — обещание сбылось на уровне эксплуатации.", size=24)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="5 лет в эксплуатации · 14 млн+ исследований · 74 региона · 70 AI-сервисов.",
             size=14, italic=True, color=MID)
    pipe_y = 1.85
    pipe_h = 1.3
    stages = [
        ("Снимок", "КТ / МРТ / рентген", LIGHT),
        ("mosmed.ai\nоблако", "федеративная AI-платформа", MID),
        ("AI-анализ", "70 сервисов\n43 области", MID),
        ("Врач + 2-е мнение", "решение\n+ верификация", GOLD),
    ]
    n = len(stages)
    arrow_w = 0.5
    stage_w = (12.3 - (n - 1) * arrow_w) / n
    pipe_x = 0.55
    for i, (title, body, color) in enumerate(stages):
        x = pipe_x + i * (stage_w + arrow_w)
        is_gold = (color == GOLD)
        fill = GOLD_TINT if is_gold else SURFACE
        stroke = GOLD if is_gold else LIGHT
        ocean_box(s, x, pipe_y, stage_w, pipe_h, fill=fill, stroke=stroke)
        text_box(s, x=x + 0.15, y=pipe_y + 0.20, w=stage_w - 0.30, h=0.45,
                 text=title, size=14, bold=True,
                 color=GOLD if is_gold else color,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)
        text_box(s, x=x + 0.15, y=pipe_y + 0.70, w=stage_w - 0.30, h=0.55,
                 text=body, size=11, color=DEEP, italic=True,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
        if i < n - 1:
            ax = x + stage_w + 0.05
            right_arrow(s, ax, pipe_y + pipe_h / 2 - 0.20, arrow_w - 0.10, 0.40, fill=MID)
    grid_x, grid_y, grid_w, grid_h = 0.55, 3.40, 12.3, 3.2
    cell_w = (grid_w - 0.30) / 3
    cell_h = (grid_h - 0.15) / 2
    cells = [
        ("14 млн+", "исследований за 5 лет", True),
        ("2 000+", "медорганизаций", False),
        ("74", "региона РФ", False),
        ("18 млн+", "обработанных изображений", False),
        ("70", "AI-сервисов на 43 областях", False),
        ("11", "нац. стандартов · 300+ датасетов", False),
    ]
    for i, (val, lbl, is_gold) in enumerate(cells):
        col = i % 3
        row = i // 3
        x = grid_x + col * (cell_w + 0.15)
        y = grid_y + row * (cell_h + 0.15)
        fill = GOLD_TINT if is_gold else SURFACE
        stroke = GOLD if is_gold else LIGHT
        ocean_box(s, x, y, cell_w, cell_h, fill=fill, stroke=stroke)
        text_box(s, x=x + 0.20, y=y + 0.20, w=cell_w - 0.40, h=0.80,
                 text=val, size=32, bold=True,
                 color=GOLD if is_gold else MID, line_spacing=1.05,
                 align=PP_ALIGN.LEFT)
        text_box(s, x=x + 0.20, y=y + 0.90, w=cell_w - 0.40, h=0.55,
                 text=lbl, size=12, italic=True, color=SLATE, line_spacing=1.30)
    text_box(s, x=0.55, y=6.85, w=12.3, h=0.40,
             text="mos.ru AI Leaders Award · Remedium 2025 · Healthcare ME 2026. Федеративная платформа: Сбер AI Lab, Care Mentor AI, Третье Мнение, Webiomed.",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s12"))


def build_s13(p):
    s = blank(p)
    slide_title(s, "Смещение (bias) = следствие дизайна, а не баг.", size=24)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="AI хорошо работает в распределении обучения. За его пределами — может проваливаться несправедливо.",
             size=14, italic=True, color=MID)
    cards = [
        ("Дерматология — тон кожи",
         ["Механизм: датасеты обучения (ISIC) перепредставляют светлую кожу",
          "Доказательство: Daneshjou 2022 — чувствит. ↓ 20–30% на коже Фитцпатрика V–VI",
          "Исправление: дообучение на DDI закрыло разрыв; AI > дерматолога на тёмной коже"],
         "lucide-eye-blue.png", "Daneshjou 2022, Science Advances"),
        ("Пульсоксиметр — расовое смещение",
         ["Механизм: датчик систематически завышает SpO2 на тёмной коже",
          "Доказательство: Sjoding 2020 NEJM — гипоксия чаще пропускается у Black-пациентов",
          "Что значит для AI: модели с SpO2 на входе наследуют ошибку датчика"],
         "lucide-alert-triangle-blue.png", "Sjoding 2020, NEJM · FDA Safety 2021"),
    ]
    card_y = 1.85
    card_h = 4.55
    card_w = 6.05
    for i, (title, lines, icon, source) in enumerate(cards):
        x = 0.55 + i * (card_w + 0.20)
        ocean_box(s, x, card_y, card_w, card_h)
        add_image(s, ASSETS / "icons" / icon, x=x + 0.35, y=card_y + 0.35, w=0.85, h=0.85)
        text_box(s, x=x + 1.35, y=card_y + 0.40, w=card_w - 1.50, h=0.75,
                 text=title, size=19, bold=True, color=DEEP, line_spacing=1.18)
        line_y = card_y + 1.50
        for j, line in enumerate(lines):
            ly = line_y + j * 0.95
            filled_rect(s, x + 0.45, ly + 0.18, 0.12, 0.12, MID, radius=True, radius_adj=0.5)
            text_box(s, x=x + 0.70, y=ly, w=card_w - 0.95, h=0.85,
                     text=line, size=13, color=DEEP, line_spacing=1.35)
        text_box(s, x=x + 0.45, y=card_y + card_h - 0.45, w=card_w - 0.9, h=0.35,
                 text=source, size=11, italic=True, color=LIGHT)
    gold_callout(s, 0.55, 6.55, 12.3, 0.55,
                 "→ Валидационный набор должен покрывать целевую популяцию. Не академическая тонкость — профессиональная ответственность.",
                 size=14)
    speaker_notes(s, load_notes("s13"))


def build_s14(p):
    s = blank(p)
    text_box(s, x=0.55, y=0.5, w=12.3, h=0.5,
             text="МЫ ПРОШЛИ ПОЛОВИНУ",
             size=14, bold=True, color=TEAL, align=PP_ALIGN.CENTER)
    text_box(s, x=0.55, y=0.95, w=12.3, h=0.60,
             text="AI-диагностика — обещание сбылось (mosmed.ai: 14 млн+ исследований, 74 региона).",
             size=18, italic=True, color=MID, align=PP_ALIGN.CENTER, line_spacing=1.30)
    qbox_x, qbox_y, qbox_w, qbox_h = 1.5, 1.95, 10.3, 2.5
    ocean_box(s, qbox_x, qbox_y, qbox_w, qbox_h)
    text_runs(s, qbox_x + 0.4, qbox_y + 0.4, qbox_w - 0.8, qbox_h - 0.8, [
        {"text": "Разработка лекарств — ", "size": 26, "color": DEEP, "bold": True},
        {"text": "обещали в 10 раз быстрее.", "size": 26, "color": GOLD, "bold": True},
        {"newpara": True, "text": "Что реально к 2026 году?",
         "size": 26, "color": DEEP, "bold": True, "align": PP_ALIGN.CENTER},
    ], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.30)
    a_y = 4.8
    a_h = 1.7
    a_w = 3.9
    # Removed inline slide IDs (s12)/(s17a)/(s17b) — designer extra; switched cream-yellow
    # backgrounds → Ocean surface, gold accent only on stroke + question mark.
    anchors = [
        ("✓", "mosmed.ai", "обещание сбылось",
         "lucide-check-circle-blue.png", TEAL, False),
        ("?", "Rentosertib", "Phase IIa с рецензированием",
         "lucide-help-circle-blue.png", GOLD, True),
        ("?", "DSP-1181", "программа закрыта",
         "lucide-help-circle-blue.png", GOLD, True),
    ]
    total_anchor_w = a_w * 3 + 0.4
    a_start_x = (SLIDE_W_IN - total_anchor_w) / 2
    for i, (mark, name, sub, icon, color, is_gold) in enumerate(anchors):
        x = a_start_x + i * (a_w + 0.2)
        # Ocean surface + gold stroke (not gold_tint fill) per P1-4.
        fill = SURFACE
        stroke = GOLD if is_gold else LIGHT
        ocean_box(s, x, a_y, a_w, a_h, fill=fill, stroke=stroke,
                  stroke_pt=2.0 if is_gold else 1.5)
        add_image(s, ASSETS / "icons" / icon, x=x + 0.25, y=a_y + 0.25, w=0.7, h=0.7)
        text_box(s, x=x + 1.1, y=a_y + 0.25, w=a_w - 1.30, h=0.45,
                 text=mark + "  " + name, size=18, bold=True,
                 color=color, line_spacing=1.10)
        text_box(s, x=x + 1.1, y=a_y + 0.75, w=a_w - 1.30, h=0.40,
                 text=sub, size=12, italic=True, color=DEEP, line_spacing=1.25)
    text_box(s, x=0.55, y=6.85, w=12.3, h=0.40,
             text="Промежуточная пересборка. Дальше — где AI ускоряет разработку лекарств и две истории.",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s14"))


def build_s15(p):
    s = blank(p)
    slide_title(s, "AI ускоряет открытие, не клинические испытания.", size=24)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="10–15 лет · $1–2 млрд · ~6.7% успеха. AI ускоряет стадии 1–3.",
             size=14, italic=True, color=MID)
    pipe_y = 2.65
    pipe_h = 2.6
    stages = [
        ("1. Поиск\nмишени", "AlphaFold\nAlphaProteo", "lucide-target-blue.png", LIGHT, True),
        ("2. Поиск\nкандидатов", "Insilico\nExscientia\nGenerate Bio", "lucide-flask-conical-blue.png", MID, True),
        ("3. Оптимиз.\nкандидатов", "Симуляция\n+ ML", "lucide-sparkles-blue.png", MID, True),
        ("4. Доклинич.\nиспытания", "Прогноз\nтоксичности", "lucide-microscope-blue.png", DEEP, False),
        ("5. Клинич.\nI/II/III", "Стратиф.\nпациентов", "lucide-users-blue.png", DEEP, False),
    ]
    n = len(stages)
    arrow_w = 0.42
    stage_w = (12.3 - (n - 1) * arrow_w) / n
    pipe_x = 0.55
    banner_y = pipe_y - 0.50
    ai_banner_w = stage_w * 3 + arrow_w * 2
    filled_rect(s, pipe_x, banner_y, ai_banner_w, 0.40, GOLD_TINT,
                stroke=GOLD, stroke_pt=1.0, radius=True, radius_adj=0.30)
    text_box(s, x=pipe_x, y=banner_y, w=ai_banner_w, h=0.40,
             text="AI ускоряет значительно (4–5 лет → 12–18 месяцев)",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    grey_x = pipe_x + ai_banner_w + arrow_w
    grey_w = stage_w * 2 + arrow_w
    filled_rect(s, grey_x, banner_y, grey_w, 0.40, SOFT_GREY,
                stroke=SLATE, stroke_pt=1.0, radius=True, radius_adj=0.30)
    text_box(s, x=grey_x, y=banner_y, w=grey_w, h=0.40,
             text="AI помогает слабо — это биология",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    for i, (title, body, icon, color, is_ai) in enumerate(stages):
        x = pipe_x + i * (stage_w + arrow_w)
        fill = SURFACE
        stroke = GOLD if is_ai else LIGHT
        ocean_box(s, x, pipe_y, stage_w, pipe_h, fill=fill, stroke=stroke)
        add_image(s, ASSETS / "icons" / icon,
                  x=x + (stage_w - 0.7) / 2, y=pipe_y + 0.20, w=0.7, h=0.7)
        text_box(s, x=x + 0.10, y=pipe_y + 1.00, w=stage_w - 0.20, h=0.55,
                 text=title, size=14, bold=True, color=color,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)
        text_box(s, x=x + 0.10, y=pipe_y + 1.55, w=stage_w - 0.20, h=1.0,
                 text=body, size=11, color=DEEP, italic=True,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.30)
        if i < n - 1:
            ax = x + stage_w + 0.05
            right_arrow(s, ax, pipe_y + pipe_h / 2 - 0.20, arrow_w - 0.10, 0.40, fill=MID)
    gold_callout(s, 0.55, 5.55, 12.3, 0.55,
                 "→ ~90% отсева на клинических — AI не меняет. Это биология, а не алгоритм.",
                 size=14)
    text_box(s, x=0.55, y=6.25, w=12.3, h=0.6,
             text="«AI ускорил дизайн молекулы» (подтверждено) ≠ «AI ускорил одобрение препарата» (не подтверждено).",
             size=14, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.25)
    text_box(s, x=0.55, y=6.95, w=12.3, h=0.35,
             text="DiMasi 2016 J Health Econ · Wouters 2020 JAMA · Mullard 2024 Nature Reviews Drug Discovery.",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s15"))


def build_s16(p):
    s = blank(p)
    slide_title(s, "AlphaFold: 200 млн+ структур. AlphaProteo: связующие белки de novo.", size=22)
    text_box(s, x=0.55, y=1.10, w=12.3, h=0.40,
             text="Задача 50-летней давности — решена · Нобель по химии 2024 (Hassabis + Jumper + Baker).",
             size=13, italic=True, color=MID)
    card_x = 0.55
    card_w = 7.5
    card_h = 1.55
    cards = [
        ("База AlphaFold",
         "200M+",
         "структур белков",
         "alphafold.ebi.ac.uk · открытый, бесплатный доступ", MID, True),
        ("AlphaProteo (сент. 2024)",
         "88%",
         "успешных связываний BHRF1",
         "Первый AI-связующий для VEGF-A · аффинность в 3–300×", MID, True),
        ("AlphaFold 3 (Nature 2024)",
         "+50%",
         "точности на PoseBusters",
         "Взаимодействия белок–лиганд · diffusion-based", DEEP, False),
    ]
    for i, (title, num, sub, foot, color, is_gold) in enumerate(cards):
        y = 1.85 + i * (card_h + 0.10)
        fill = GOLD_TINT if is_gold else SURFACE
        stroke = GOLD if is_gold else LIGHT
        ocean_box(s, card_x, y, card_w, card_h, fill=fill, stroke=stroke)
        text_box(s, x=card_x + 0.30, y=y + 0.20, w=card_w - 0.60, h=0.45,
                 text=title, size=15, bold=True, color=DEEP, line_spacing=1.10)
        text_box(s, x=card_x + 0.30, y=y + 0.65, w=2.4, h=0.85,
                 text=num, size=44, bold=True,
                 color=GOLD if is_gold else MID, line_spacing=1.0)
        text_box(s, x=card_x + 2.8, y=y + 0.65, w=card_w - 3.1, h=0.40,
                 text=sub, size=13, bold=True, color=DEEP, line_spacing=1.20)
        text_box(s, x=card_x + 2.8, y=y + 1.05, w=card_w - 3.1, h=0.45,
                 text=foot, size=11, italic=True, color=SLATE, line_spacing=1.25)
    img_x, img_y, img_w, img_h = 8.30, 1.85, 4.55, 4.95
    ocean_box(s, img_x, img_y, img_w, img_h)
    cx = img_x + img_w / 2
    cy = img_y + img_h / 2 - 0.2
    filled_rect(s, img_x + 0.3, img_y + 0.5, img_w - 0.6, img_h - 1.2,
                RGBColor(0xE6, 0xEC, 0xF2), radius=True, radius_adj=0.05)
    colors = [LIGHT, MID, DEEP, TEAL, GOLD]
    for j, col in enumerate(colors):
        offs_x = -0.7 + j * 0.35
        offs_y = -0.4 + (j % 2) * 0.5
        for k in range(5):
            x = cx + offs_x + k * 0.18
            y = cy + offs_y + (k % 2) * 0.12
            filled_rect(s, x, y, 0.28, 0.28, col, radius=True, radius_adj=0.5)
    text_box(s, x=img_x + 0.2, y=img_y + img_h - 0.55, w=img_w - 0.4, h=0.40,
             text="3D-структура белка (схематично)",
             size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    filled_rect(s, 10.0, 1.20, 2.9, 0.45, GOLD, radius=True, radius_adj=0.30)
    text_box(s, x=10.0, y=1.20, w=2.9, h=0.45,
             text="Нобель по химии 2024",
             size=12, bold=True, color=WHITE,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.55, y=6.95, w=12.3, h=0.35,
             text="Jumper et al. Nature 2021 · Abramson et al. Nature May 2024 · Watson et al. arXiv:2409.08022 · alphafold.ebi.ac.uk.",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s16"))


def build_s17a(p):
    s = blank(p)
    slide_title(s, "Rentosertib — первый AI-препарат с рецензированным Phase IIa.", size=22)
    text_box(s, x=0.55, y=1.10, w=12.3, h=0.40,
             text="Nature Medicine, июнь 2025 · PMID 40461817 · Insilico Medicine (ISM001-055)",
             size=13, italic=True, color=MID)
    tl_y = 2.4
    tl_h = 2.5
    events = [
        ("2020–2022", "Поиск мишени с AI\n→ доклинический кандидат",
         "~18 месяцев против 4–5 лет", LIGHT, False),
        ("Окт. 2024", "Объявлены топ-результаты\nPhase IIa",
         "Пресс-релиз Insilico", MID, False),
        ("Июнь 2025", "Nature Medicine\nрецензированное РКИ n=71",
         "21 центр в Китае · ИЛФ", GOLD, True),
    ]
    n = len(events)
    arrow_w = 0.50
    total_w = 12.3
    box_w_norm = (total_w - (n - 1) * arrow_w) / (n + 0.5)
    box_w_pivot = box_w_norm * 1.5
    box_widths = [box_w_norm, box_w_norm, box_w_pivot]
    x_cursor = 0.55
    text_box(s, x=0.55, y=tl_y - 0.45, w=12.3, h=0.35,
             text="ВРЕМЯ →",
             size=11, italic=True, color=SLATE)
    for i, ((date, body, sub, color, is_pivot), bw) in enumerate(zip(events, box_widths)):
        x = x_cursor
        h = tl_h
        if is_pivot:
            h = tl_h + 0.3
            fill = SURFACE
            stroke = GOLD
            sw = 2.5
        else:
            fill = SURFACE
            stroke = LIGHT
            sw = 1.5
        ocean_box(s, x, tl_y if not is_pivot else tl_y - 0.15, bw, h,
                  fill=fill, stroke=stroke, stroke_pt=sw)
        date_size = 18 if is_pivot else 14
        body_size = 16 if is_pivot else 12
        sub_size = 13 if is_pivot else 11
        text_box(s, x=x + 0.20, y=(tl_y - 0.15 if is_pivot else tl_y) + 0.20,
                 w=bw - 0.4, h=0.50,
                 text=date, size=date_size, bold=True,
                 color=GOLD if is_pivot else color, line_spacing=1.10)
        text_box(s, x=x + 0.20, y=(tl_y - 0.15 if is_pivot else tl_y) + 0.80,
                 w=bw - 0.4, h=1.10,
                 text=body, size=body_size, bold=is_pivot, color=DEEP,
                 line_spacing=1.30)
        text_box(s, x=x + 0.20, y=(tl_y - 0.15 if is_pivot else tl_y) + 1.85,
                 w=bw - 0.4, h=0.55,
                 text="— " + sub, size=sub_size, italic=True,
                 color=GOLD if is_pivot else SLATE, line_spacing=1.30)
        if i < n - 1:
            ax = x + bw + 0.05
            text_box(s, x=ax, y=tl_y + tl_h / 2 - 0.20, w=arrow_w - 0.10, h=0.40,
                     text="—", size=24, bold=True, color=SLATE,
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        x_cursor += bw + arrow_w
    gold_callout(s, 0.55, 5.20, 12.3, 0.75,
                 "60 мг 1× в день → +98.4 мл ФЖЕЛ (форсиров. жизн. ёмкость лёгких) vs −20.3 мл плацебо (12 недель)  ·  Δ ~118 мл. ИЛФ — клинически значимо.",
                 size=12)
    # P1-17 — RU drug discovery context (chapter §3.3, 300-word block).
    ru_y, ru_h = 6.05, 0.95
    ocean_box(s, 0.55, ru_y, 12.3, ru_h)
    text_runs(s, 0.85, ru_y + 0.10, 11.7, ru_h - 0.20, [
        {"text": "Российский контекст (2024–2025, доклинические): ", "size": 12,
         "color": TEAL, "bold": True},
        {"text": "Сбер AI Lab + AIRI + Р-Фарм — Альянс №1 CD137 онкология (май 2024); "
                 "Альянс №2 Альцгеймер (ноябрь 2025); MADD (ИТМО+Сбер, EMNLP 2025); "
                 "DiMA (AIRI, ICML 2025).",
         "size": 11, "color": DEEP},
        {"newpara": True,
         "text": "Все программы — доклинические: 0 препаратов российской разработки в клинических испытаниях на май 2026.",
         "size": 11, "italic": True, "color": SLATE},
    ], line_spacing=1.30)
    text_box(s, x=0.55, y=7.05, w=12.3, h=0.35,
             text="PubMed 40461817 · NCT05938920 · Nature Medicine июнь 2025 · MADD EMNLP 2025 · DiMA ICML 2025.",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s17a"))


def build_s17b(p):
    s = blank(p)
    slide_title(s, "DSP-1181 — проверка реальностью: AI ускорил дизайн, не клинику.", size=22)
    text_box(s, x=0.55, y=1.10, w=12.3, h=0.40,
             text="«Первый AI-разработанный препарат в клинических испытаниях» (2020) → Phase 1 закрыта (2022).",
             size=13, italic=True, color=MID)
    tl_y = 2.4
    tl_h = 2.5
    events = [
        ("Январь 2020", "Вход в Phase 1\nExscientia + Sumitomo",
         "ОКР · Япония · 12 мес vs 4–5 лет", LIGHT, False),
        ("2022", "Phase 1\nЗАКРЫТА",
         "Причина не указана", DARK_GREY, True),
        ("Май 2026", "Статус Synapse:\nпрограмма закрыта",
         "Текущий R&D-статус", DEEP, False),
    ]
    n = len(events)
    arrow_w = 0.50
    total_w = 12.3
    box_w_norm = (total_w - (n - 1) * arrow_w) / (n + 0.5)
    box_w_pivot = box_w_norm * 1.5
    box_widths = [box_w_norm, box_w_pivot, box_w_norm]
    x_cursor = 0.55
    text_box(s, x=0.55, y=tl_y - 0.45, w=12.3, h=0.35,
             text="ВРЕМЯ →",
             size=11, italic=True, color=SLATE)
    for i, ((date, body, sub, color, is_pivot), bw) in enumerate(zip(events, box_widths)):
        x = x_cursor
        h = tl_h
        if is_pivot:
            h = tl_h + 0.3
            # Pivot card: Ocean surface + navy text + grey stroke for «closed/discontinued».
            # No red palette per anti-pattern #3 (P1-5).
            fill = SURFACE
            stroke = DARK_GREY
            sw = 2.5
        else:
            fill = SURFACE
            stroke = LIGHT
            sw = 1.5
        ocean_box(s, x, tl_y if not is_pivot else tl_y - 0.15, bw, h,
                  fill=fill, stroke=stroke, stroke_pt=sw)
        date_size = 18 if is_pivot else 14
        body_size = 16 if is_pivot else 12
        sub_size = 13 if is_pivot else 11
        text_box(s, x=x + 0.20, y=(tl_y - 0.15 if is_pivot else tl_y) + 0.20,
                 w=bw - 0.4, h=0.50,
                 text=date, size=date_size, bold=True,
                 color=DARK_GREY if is_pivot else color, line_spacing=1.10)
        # «✕ DISCONTINUED» — navy bold (no red) with strikethrough-style icon prefix.
        body_with_strike = ("✕ " + body) if is_pivot else body
        text_box(s, x=x + 0.20, y=(tl_y - 0.15 if is_pivot else tl_y) + 0.80,
                 w=bw - 0.4, h=1.10,
                 text=body_with_strike, size=body_size, bold=is_pivot,
                 color=DEEP if is_pivot else DEEP,
                 line_spacing=1.30)
        text_box(s, x=x + 0.20, y=(tl_y - 0.15 if is_pivot else tl_y) + 1.85,
                 w=bw - 0.4, h=0.55,
                 text="— " + sub, size=sub_size, italic=True,
                 color=DARK_GREY if is_pivot else SLATE, line_spacing=1.30)
        if i < n - 1:
            ax = x + bw + 0.05
            text_box(s, x=ax, y=tl_y + tl_h / 2 - 0.20, w=arrow_w - 0.10, h=0.40,
                     text="—", size=24, bold=True, color=SLATE,
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        x_cursor += bw + arrow_w
    insight_y = 5.45
    insight_h = 1.4
    ocean_box(s, 0.55, insight_y, 12.3, insight_h)
    text_runs(s, 0.85, insight_y + 0.20, 11.7, insight_h - 0.4, [
        {"text": "AI ускорил дизайн молекулы", "size": 16, "color": MID, "bold": True},
        {"text": "  (12 мес vs 4–5 лет) — ", "size": 15, "color": DEEP},
        {"text": "подтверждено.", "size": 15, "color": TEAL, "bold": True},
        {"newpara": True,
         "text": "Клиническая эффективность", "size": 16, "color": MID, "bold": True},
        {"text": "  — отдельная задача биологии.", "size": 15, "color": DEEP},
        {"newpara": True,
         "text": "«AI-препарат = быстро + эффективно»", "size": 13, "italic": True, "color": SLATE},
        {"text": "  — два независимых тезиса, объединённых маркетингом.",
         "size": 13, "italic": True, "color": SLATE},
    ], line_spacing=1.30)
    text_box(s, x=0.55, y=7.05, w=12.3, h=0.35,
             text="Synapse/PatSnap drug profile · Sumitomo 2020 press · CAS Insights · Recursion + Exscientia merger Aug 2024.",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s17b"))


def build_s18(p):
    s = blank(p)
    slide_title(s, "Медицинский AI = высокий риск во всех 3 крупных юрисдикциях.", size=24)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="Подходы отличаются процессами, а не принципами.",
             size=14, italic=True, color=MID)
    cols = [
        ("США (FDA)",
         "lucide-flag-blue.png",
         [("Структура", "SaMD + специальные правила для AI/ML"),
          ("PCCP финализирован", "4 декабря 2024"),
          ("До PCCP", "каждое обновление = новое разрешение (12–18 мес)"),
          ("С PCCP", "вендор заранее декларирует допустимые обновления")],
         False),
        ("ЕС (AI Act)",
         "lucide-flag-blue.png",
         [("Регулятор", "Европейская комиссия + Notified Bodies"),
          ("Основание", "Article 6 + Annex III (высокий риск)"),
          ("⚠ 2 авг. 2026", "Annex III высокий риск → 2.5 мес после лекции"),
          ("⚠ 2 авг. 2027", "MDR — полное соответствие для медицинского AI")],
         True),
        ("РФ (Росздравнадзор)",
         "lucide-flag-blue.png",
         [("Зарегистрировано", "57 AI-медизделий (52 РФ + 5 зарубежных)"),
          ("Ускоренный режим", "1 марта 2025 (ПП РФ № 1684)"),
          ("Первый AI", "Webiomed, 3 апреля 2020"),
          ("Локализация данных", "ФЗ-23, 1 июля 2025")],
         False),
    ]
    col_y = 1.95
    col_h = 4.8
    col_w = 4.05
    gap = 0.15
    for i, (title, icon, items, is_gold) in enumerate(cols):
        x = 0.55 + i * (col_w + gap)
        # Ocean surface + gold stroke (no gold_tint fill — P1-4).
        fill = SURFACE
        stroke = GOLD if is_gold else LIGHT
        ocean_box(s, x, col_y, col_w, col_h, fill=fill, stroke=stroke,
                  stroke_pt=2.0 if is_gold else 1.5)
        add_image(s, ASSETS / "icons" / icon, x=x + 0.30, y=col_y + 0.30, w=0.7, h=0.7)
        text_box(s, x=x + 1.10, y=col_y + 0.35, w=col_w - 1.30, h=0.65,
                 text=title, size=18, bold=True, color=DEEP, line_spacing=1.15)
        item_y = col_y + 1.30
        for j, (key, val) in enumerate(items):
            iy = item_y + j * 0.78
            text_box(s, x=x + 0.30, y=iy, w=col_w - 0.6, h=0.30,
                     text=key, size=11, bold=True,
                     color=GOLD if (is_gold and j >= 2) else MID, line_spacing=1.15)
            text_box(s, x=x + 0.30, y=iy + 0.30, w=col_w - 0.6, h=0.45,
                     text=val, size=12, color=DEEP, line_spacing=1.25)
    gold_callout(s, 0.55, 6.85, 12.3, 0.40,
                 "→ Проектируйте с PCCP в уме: дрейф данных, триггеры переобучения, обновления порогов — план заранее.",
                 size=12)
    text_box(s, x=0.55, y=7.25, w=12.3, h=0.20,
             text="SaMD — Software as Medical Device (категория FDA) · MDR — EU Medical Device Regulation",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s18"))


def build_s19(p):
    s = blank(p)
    slide_title(s, "Используем AI для понимания AI — но проверяем.", size=24)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="Web-чат + критическая оценка ответа.",
             size=14, italic=True, color=MID)
    card_x, card_y, card_w, card_h = 0.55, 1.85, 8.2, 5.0
    ocean_box(s, card_x, card_y, card_w, card_h)
    steps = [
        ("Шаг 1  ·  3 мин",
         "Открой web-чат (ChatGPT / Claude / YandexGPT / GigaChat). Введи промпт ниже:",
         MID),
        ("Шаг 2  ·  3 мин",
         "Отметь карандашом: 1 неточность ИЛИ 1 непроверяемое утверждение ИЛИ 1 слишком абстрактное место.",
         LIGHT),
        ("Шаг 3  ·  4 мин — разбор",
         "Лектор спросит — 2–3 студента читают (1 мин). Лектор покажет эталонный ответ.",
         DEEP),
    ]
    step_y = card_y + 0.35
    for i, (label, body, color) in enumerate(steps):
        sy = step_y + i * 1.05
        filled_rect(s, card_x + 0.30, sy, 0.55, 0.55, color, radius=True, radius_adj=0.5)
        text_box(s, x=card_x + 0.30, y=sy, w=0.55, h=0.55,
                 text=str(i + 1), size=22, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=card_x + 1.0, y=sy + 0.05, w=card_w - 1.2, h=0.30,
                 text=label, size=13, bold=True, color=color, line_spacing=1.10)
        text_box(s, x=card_x + 1.0, y=sy + 0.40, w=card_w - 1.2, h=0.55,
                 text=body, size=13, color=DEEP, line_spacing=1.30)
    prompt_y = card_y + 3.65
    filled_rect(s, card_x + 0.30, prompt_y, card_w - 0.60, 1.20,
                RGBColor(0xF0, 0xF4, 0xF8), stroke=LIGHT, stroke_pt=0.8,
                radius=True, radius_adj=0.05)
    text_box(s, x=card_x + 0.45, y=prompt_y + 0.10, w=card_w - 0.90, h=0.30,
             text="Готовый промпт:",
             size=11, bold=True, color=MID)
    text_box(s, x=card_x + 0.45, y=prompt_y + 0.40, w=card_w - 0.90, h=0.75,
             text="«Объясни мне, что такое чувствительность и специфичность для AI-диагностики на конкретном примере (скрининг маммографии). Объясни как для студента 2 курса техн. вуза, со знанием базовой теории вероятностей.»",
             size=11, italic=True, color=DEEP, font=FONT_MONO, line_spacing=1.40)
    ctrl_x, ctrl_y, ctrl_w, ctrl_h = card_x + card_w + 0.30, 1.85, 4.0, 5.0
    ocean_box(s, ctrl_x, ctrl_y, ctrl_w, ctrl_h)
    text_box(s, x=ctrl_x + 0.30, y=ctrl_y + 0.30, w=ctrl_w - 0.60, h=0.40,
             text="Эталонный ответ (готовится накануне)",
             size=13, bold=True, color=DEEP, line_spacing=1.15)
    filled_rect(s, ctrl_x + 0.30, ctrl_y + 0.85, ctrl_w - 0.60, ctrl_h - 1.6,
                WHITE, stroke=LIGHT, stroke_pt=0.6,
                radius=True, radius_adj=0.03)
    lines = [
        "Чувствительность — доля...",
        "...правильно пойманных AI.",
        "TP / (TP + FN).",
        "",
        "Специфичность — доля...",
        "...правильно отпущенных.",
        "TN / (TN + FP).",
        "",
        "Маммография — пример:",
        "MASAI sens 80.5%, spec 98.5%",
    ]
    for j, ln in enumerate(lines):
        ly = ctrl_y + 1.05 + j * 0.27
        if ly > ctrl_y + ctrl_h - 0.55:
            break
        text_box(s, x=ctrl_x + 0.45, y=ly, w=ctrl_w - 0.90, h=0.27,
                 text=ln, size=11,
                 color=DEEP if ln and not ln.startswith("MASAI") else MID,
                 bold=ln.startswith("MASAI"),
                 line_spacing=1.20)
    text_box(s, x=ctrl_x + 0.30, y=ctrl_y + ctrl_h - 0.45, w=ctrl_w - 0.60, h=0.35,
             text="Готовится преподавателем накануне.",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    gold_callout(s, 0.55, 6.95, 12.3, 0.40,
                 "Цель — критика на уровне абзаца. AI отлично объясняет — это паттерн. AI даёт цифры без источника — антипаттерн.",
                 size=12)
    speaker_notes(s, load_notes("s19"))


def build_s20(p):
    s = blank(p)
    slide_title(s, "В медицинском AI ставки максимальны.", size=24)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="Ошибка модели = ошибка диагноза или назначения = вред пациенту.",
             size=14, italic=True, color=MID)
    img_x, img_y, img_w, img_h = 0.55, 1.85, 5.6, 4.9
    ocean_box(s, img_x, img_y, img_w, img_h)
    # Real medical photo (Unsplash CC0) — врач+пациент: измерение давления.
    # Это содержательная клиническая сцена, не баннер; визуализирует «ставки на пациенте».
    add_image(s, ASSETS / "photos/s20-medical-team.jpg",
              x=img_x + 0.25, y=img_y + 0.30, w=img_w - 0.5, h=img_h - 0.85)
    text_box(s, x=img_x + 0.3, y=img_y + img_h - 0.50, w=img_w - 0.6, h=0.35,
             text="Каждый AI-диагноз заканчивается этим — взаимодействием врача с пациентом.",
             size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    list_x, list_y, list_w, list_h = 6.45, 1.85, 6.35, 4.9
    ocean_box(s, list_x, list_y, list_w, list_h)
    text_box(s, x=list_x + 0.30, y=list_y + 0.25, w=list_w - 0.6, h=0.4,
             text="Что инженер должен знать про границы",
             size=14, bold=True, color=DEEP)
    items = [
        ("Смещение (bias) в медицинском AI",
         "Глубокий разбор: Obermeyer 2019",
         "lucide-scale-blue.png"),
        ("LLM-антипаттерны",
         "NEDA Tessa + adversarial + 40 млн самодиагностик",
         "lucide-message-circle-warning-blue.png"),
        ("Безопасность данных + ответственность",
         "Change Healthcare + рамка 4 актёров",
         "lucide-shield-check-blue.png"),
    ]
    item_y = list_y + 0.95
    for i, (title, sub, icon) in enumerate(items):
        iy = item_y + i * 1.30
        add_image(s, ASSETS / "icons" / icon, x=list_x + 0.30, y=iy + 0.15, w=0.8, h=0.8)
        text_box(s, x=list_x + 1.25, y=iy + 0.10, w=list_w - 1.40, h=0.50,
                 text=str(i + 1) + ".  " + title, size=16, bold=True, color=MID, line_spacing=1.15)
        text_box(s, x=list_x + 1.25, y=iy + 0.65, w=list_w - 1.40, h=0.50,
                 text=sub, size=12, italic=True, color=DEEP, line_spacing=1.30)
    gold_callout(s, 0.55, 6.85, 12.3, 0.50,
                 "→ Думать про границы сразу, на стадии проектирования — не задним числом после первого инцидента.",
                 size=14)
    speaker_notes(s, load_notes("s20"))


def build_s21(p):
    s = blank(p)
    slide_title(s, "Obermeyer 2019 — выбор прокси стал выбором политики.", size=22)
    text_box(s, x=0.55, y=1.10, w=12.3, h=0.40,
             text="Коммерческий AI для 200 млн американцев систематически недооценивал тяжесть болезни у Black-пациентов.",
             size=13, italic=True, color=MID)
    pipe_y = 1.85
    pipe_h = 1.65
    boxes = [
        ("Цель", "Найти пациентов,\nкому нужна\nдоп. помощь", LIGHT),
        ("Прокси", "Расходы на\nпредыдущее\nлечение\n(не тяжесть)", GOLD),
        ("Источник смещения", "Black: −$1 800/год\n(разный доступ)\n→ AI «менее больны»", DARK_GREY),
    ]
    n = 3
    arrow_w = 0.50
    box_w = (12.3 - (n - 1) * arrow_w) / n
    pipe_x = 0.55
    for i, (title, body, color) in enumerate(boxes):
        x = pipe_x + i * (box_w + arrow_w)
        is_proxy = (i == 1)
        fill = GOLD_TINT if is_proxy else SURFACE
        stroke = GOLD if is_proxy else LIGHT
        ocean_box(s, x, pipe_y, box_w, pipe_h, fill=fill, stroke=stroke)
        text_box(s, x=x + 0.20, y=pipe_y + 0.15, w=box_w - 0.40, h=0.40,
                 text=title, size=14, bold=True,
                 color=GOLD if is_proxy else color, line_spacing=1.10)
        text_box(s, x=x + 0.20, y=pipe_y + 0.60, w=box_w - 0.40, h=pipe_h - 0.75,
                 text=body, size=12, color=DEEP, line_spacing=1.35,
                 align=PP_ALIGN.LEFT)
        if i < n - 1:
            ax = x + box_w + 0.05
            right_arrow(s, ax, pipe_y + pipe_h / 2 - 0.20, arrow_w - 0.10, 0.40, fill=MID)
    rc_x, rc_y, rc_w, rc_h = 0.55, 3.7, 6.0, 2.7
    ocean_box(s, rc_x, rc_y, rc_w, rc_h)
    text_box(s, x=rc_x + 0.3, y=rc_y + 0.20, w=rc_w - 0.6, h=0.40,
             text="При одинаковом риск-скоре у Black-пациентов:",
             size=13, bold=True, color=DEEP)
    text_box(s, x=rc_x + 0.3, y=rc_y + 0.75, w=rc_w - 0.6, h=1.0,
             text="+26%",
             size=64, bold=True, color=GOLD, line_spacing=1.0)
    text_box(s, x=rc_x + 0.3, y=rc_y + 1.85, w=rc_w - 0.6, h=0.45,
             text="больше хронических заболеваний",
             size=14, color=DEEP, line_spacing=1.20)
    text_box(s, x=rc_x + 0.3, y=rc_y + rc_h - 0.40, w=rc_w - 0.6, h=0.35,
             text="Science 2019 · n ≈ 200 млн американцев",
             size=11, italic=True, color=LIGHT)
    fix_x, fix_y, fix_w, fix_h = rc_x + rc_w + 0.25, 3.7, 6.05, 2.7
    ocean_box(s, fix_x, fix_y, fix_w, fix_h)
    text_box(s, x=fix_x + 0.3, y=fix_y + 0.20, w=fix_w - 0.6, h=0.40,
             text="Исправление: гибридный прокси (расходы + хронические)",
             size=13, bold=True, color=DEEP)
    text_runs(s, fix_x + 0.3, fix_y + 0.75, fix_w - 0.6, 0.9, [
        {"text": "17.7%", "size": 32, "bold": True, "color": DARK_GREY},
        {"text": "  →  ", "size": 32, "bold": True, "color": SLATE},
        {"text": "46.5%", "size": 32, "bold": True, "color": GOLD},
    ], line_spacing=1.0, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=fix_x + 0.3, y=fix_y + 1.65, w=fix_w - 0.6, h=0.50,
             text="доля Black-пациентов в программах ведения пациентов высокого риска",
             size=11, color=DEEP, line_spacing=1.30)
    text_box(s, x=fix_x + 0.3, y=fix_y + rc_h - 0.40, w=fix_w - 0.6, h=0.35,
             text="−84% смещения  ·  не теория — реальные пациенты",
             size=12, italic=True, color=GOLD)
    gold_callout(s, 0.55, 6.55, 12.3, 0.55,
                 "→ Выбирая прокси, спрашивайте: какие группы имеют систематически разный доступ к ней?",
                 size=14)
    text_box(s, x=0.55, y=7.2, w=12.3, h=0.30,
             text="Obermeyer, Powers, Vogeli, Mullainathan — Science 366, 447 (2019). DOI: 10.1126/science.aax2342.",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s21"))


def build_s22(p):
    s = blank(p)
    slide_title(s, "LLM в медицине ≠ медицинский AI — 3 задокументированных случая.", size=22)
    text_box(s, x=0.55, y=1.10, w=12.3, h=0.40,
             text="Ответственность вендора · состязательные галлюцинации · самодиагностика в массовом масштабе (2025–2026).",
             size=12, italic=True, color=MID)
    cards = [
        ("NEDA Tessa — скандал",
         ["~2018–2022: rule-based, одобрен NEDA",
          "Начало 2023: Cass → генеративный БЕЗ одобрения NEDA",
          "30 мая 2023: скриншоты Maxwell → отключён за 24 часа"],
         "lucide-message-circle-warning-blue.png", "ответственность вендора",
         "Май 2023 · NPR · AI Incident DB #545"),
        ("Состязательные галлюцинации",
         ["6 ведущих LLM, 300 клинических виньеток",
          "С подсаженной фейк-деталью → расширяют её в 83% случаев",
          "Mitigation-промпт → снижает вдвое, но ≠ ноль"],
         "lucide-alert-octagon-blue.png", "галлюцин. 83%",
         "Communications Medicine 2025 (Nature)"),
        ("Самодиагностика в масштабе",
         ["~40 млн американцев использовали ChatGPT для здоровья за 3 месяца",
          "3 из 5 совершеннолетних США",
          "Регулирование за этим не успевает"],
         "lucide-users-blue.png", "40 млн американцев",
         "OpenAI / Gallup 2025 · Becker's Hospital Review"),
    ]
    # P1-7: compressed card heights + footer pulled up so callout не cuts at safe area.
    card_y = 1.80
    card_h = 1.42
    card_w = 12.3
    for i, (title, lines, icon, badge, source) in enumerate(cards):
        y = card_y + i * (card_h + 0.08)
        ocean_box(s, 0.55, y, card_w, card_h)
        add_image(s, ASSETS / "icons" / icon, x=0.85, y=y + 0.22, w=0.85, h=0.85)
        text_box(s, x=1.90, y=y + 0.18, w=4.5, h=0.45,
                 text=title, size=16, bold=True, color=DEEP, line_spacing=1.15)
        filled_rect(s, 1.90, y + 0.66, 2.5, 0.32, GOLD, radius=True, radius_adj=0.30)
        text_box(s, x=1.90, y=y + 0.66, w=2.5, h=0.32,
                 text=badge, size=11, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=1.90, y=y + 1.05, w=4.5, h=0.30,
                 text=source, size=10, italic=True, color=LIGHT, line_spacing=1.20)
        for j, ln in enumerate(lines):
            ly = y + 0.18 + j * 0.38
            filled_rect(s, 6.75, ly + 0.13, 0.10, 0.10, MID, radius=True, radius_adj=0.5)
            text_box(s, x=6.95, y=ly, w=card_w - 6.55, h=0.38,
                     text=ln, size=11, color=DEEP, line_spacing=1.25)
    gold_callout(s, 0.55, 6.55, 12.3, 0.45,
                 "→ Генеративный AI ≠ rule-based AI. Изменения дизайна вендором могут обойти clinical-safety проверку.",
                 size=13)
    text_box(s, x=0.55, y=7.10, w=12.3, h=0.25,
             text="Точная дата переключения на генеративный режим — начало 2023 (источники не дают строгий месяц).",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s22"))


def build_s23(p):
    s = blank(p)
    slide_title(s, "Обучающие данные медицинского AI наследуют риски безопасности.", size=22)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="Change Healthcare (февр. 2024): 190 млн человек, $2.457 млрд на восстановление — медданные мишень №1.",
             size=13, italic=True, color=MID)
    nh_x, nh_y, nh_w, nh_h = 0.55, 1.85, 12.3, 0.8
    ocean_box(s, nh_x, nh_y, nh_w, nh_h)
    text_box(s, x=nh_x + 0.30, y=nh_y + 0.10, w=nh_w - 0.6, h=0.30,
             text="BleepingComputer · 21.02.2024",
             size=10, bold=True, color=MID)
    text_box(s, x=nh_x + 0.30, y=nh_y + 0.35, w=nh_w - 0.6, h=0.40,
             text="UnitedHealth: 190 млн американцев пострадали от утечки данных Change Healthcare 2024",
             size=15, bold=True, color=DEEP, line_spacing=1.20)
    grid_y = 2.85
    grid_h = 1.7
    cells = [
        ("190 млн", "пострадавших американцев (~57% населения США)", False),
        ("$2.457 млрд", "стоимость восстановления UHG, 3 кв. 2024", True),
        ("6 ТБ", "украдено", False),
        ("Несколько недель", "сбои в страховых выплатах США", False),
        ("$22 млн", "выкуп ALPHV/BlackCat", False),
    ]
    n = len(cells)
    gap = 0.12
    cell_w = (12.3 - (n - 1) * gap) / n
    for i, (val, lbl, is_gold) in enumerate(cells):
        x = 0.55 + i * (cell_w + gap)
        fill = GOLD_TINT if is_gold else SURFACE
        stroke = GOLD if is_gold else LIGHT
        ocean_box(s, x, grid_y, cell_w, grid_h, fill=fill, stroke=stroke,
                  stroke_pt=2.0 if is_gold else 1.5)
        text_box(s, x=x + 0.15, y=grid_y + 0.25, w=cell_w - 0.30, h=0.65,
                 text=val, size=24, bold=True,
                 color=GOLD if is_gold else MID, line_spacing=1.05,
                 align=PP_ALIGN.CENTER)
        text_box(s, x=x + 0.15, y=grid_y + 0.95, w=cell_w - 0.30, h=0.60,
                 text=lbl, size=11, italic=True, color=DEEP, line_spacing=1.30,
                 align=PP_ALIGN.CENTER)
    bridge_y = 4.75
    bridge_h = 1.4
    ocean_box(s, 0.55, bridge_y, 12.3, bridge_h)
    text_box(s, x=0.85, y=bridge_y + 0.20, w=11.7, h=0.40,
             text="Связь с AI — обучающие датасеты медицинского AI наследуют те же риски",
             size=14, bold=True, color=DEEP)
    text_box(s, x=0.85, y=bridge_y + 0.65, w=11.7, h=0.65,
             text="mosmed.ai = 18 млн+ изображений → расширяет цели для ransomware. Анонимизация ≠ необратимая (Sweeney 2002 — re-identification губернатора Массачусетса).",
             size=12, color=DEEP, line_spacing=1.40)
    chip_y = 6.30
    chip_w = 3.9
    chip_h = 0.50
    chip_gap = 0.20
    chips = ["HIPAA (US, 1996)", "GDPR (EU, 2016/679)", "ФЗ-152 + ФЗ-23 (1 июля 2025)"]
    chip_x_start = (SLIDE_W_IN - chip_w * 3 - chip_gap * 2) / 2
    for i, c in enumerate(chips):
        x = chip_x_start + i * (chip_w + chip_gap)
        chip(s, x, chip_y, chip_w, chip_h, c, fill=MID, color=WHITE, size=12)
    text_box(s, x=0.55, y=7.05, w=12.3, h=0.30,
             text="UHG newsroom · BleepingComputer · HIPAA Journal · House Energy & Commerce.",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s23"))


def build_s24(p):
    s = blank(p)
    slide_title(s, "Врач решает. AI подсказывает. Конечная ответственность — неделима.", size=22)
    text_box(s, x=0.55, y=1.10, w=12.3, h=0.40,
             text="4 актёра с разной комбинацией: технический контроль × юридическая ответственность.",
             size=13, italic=True, color=MID)
    grid_x, grid_y, grid_w, grid_h = 1.40, 1.85, 10.7, 3.7
    cell_w = grid_w / 2
    cell_h = grid_h / 2
    # Cells per user brief (v3):
    #   Top-left  (col=0, row=0): Регулятор   (высокая ответственность + низкий контроль)
    #   Top-right (col=1, row=0): Врач        (высокая ответственность + высокий контроль) — GOLD
    #   Bottom-left  (col=0, row=1): Оператор (средняя ответственность + средний контроль)
    #   Bottom-right (col=1, row=1): Вендор AI (средняя ответственность + высокий контроль)
    cells = [
        ("Регулятор",
         "Одобряет · проверяет · отзывает разрешения",
         "FDA · EU NB · Росздравнадзор · надзорная роль",
         "lucide-gavel-blue.png", LIGHT, 0, 0, False),
        ("Врач",
         "Конечный диагностический ответ",
         "AI — подсказка, не решение · высокая ответственность",
         "lucide-stethoscope-blue.png", GOLD, 1, 0, True),
        ("Оператор",
         "Выбор вендора · обучение · развёртывание",
         "Больница · клиника · ДЗМ · средний контроль",
         "lucide-building-2-blue.png", MID, 0, 1, False),
        ("Вендор AI",
         "Дизайн модели · заявки на безопасность",
         "Обновления PCCP · пострыночный мониторинг · высокий контроль",
         "lucide-code-blue.png", MID, 1, 1, False),
    ]
    for title, sub, exs, icon, color, col, row, is_gold in cells:
        x = grid_x + col * cell_w
        y = grid_y + row * cell_h
        fill = GOLD_TINT if is_gold else SURFACE
        stroke = GOLD if is_gold else LIGHT
        sw = 2.5 if is_gold else 1.5
        ocean_box(s, x + 0.1, y + 0.1, cell_w - 0.2, cell_h - 0.2,
                  fill=fill, stroke=stroke, stroke_pt=sw)
        add_image(s, ASSETS / "icons" / icon, x=x + 0.30, y=y + 0.30, w=0.7, h=0.7)
        text_box(s, x=x + 1.15, y=y + 0.30, w=cell_w - 1.35, h=0.50,
                 text=title, size=17, bold=True,
                 color=GOLD if is_gold else color, line_spacing=1.15)
        text_box(s, x=x + 0.30, y=y + 0.95, w=cell_w - 0.5, h=0.40,
                 text=sub, size=12, color=DEEP, line_spacing=1.25)
        text_box(s, x=x + 0.30, y=y + 1.35, w=cell_w - 0.5, h=0.55,
                 text=exs, size=9, italic=True, color=SLATE, line_spacing=1.20)
    # Axis label inside grid - horizontal at bottom.
    text_box(s, x=grid_x, y=grid_y + grid_h + 0.1, w=grid_w, h=0.30,
             text="◄ низкий контроль · ТЕХНИЧЕСКИЙ КОНТРОЛЬ · высокий контроль ►",
             size=11, bold=True, color=DEEP, align=PP_ALIGN.CENTER, italic=True)
    # Axis label inside grid - vertical on left.
    text_box(s, x=0.40, y=grid_y, w=0.9, h=grid_h,
             text="ОТВЕТ-\nСТВЕН-\nНОСТЬ\n\n▲ высокая\n\n\n▼ низкая",
             size=10, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)
    cl_y = 6.0
    cl_h = 1.0
    ocean_box(s, 0.55, cl_y, 12.3, cl_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    text_runs(s, 0.85, cl_y + 0.20, 11.7, cl_h - 0.4, [
        {"text": "Врач ставит диагноз. AI подсказывает. Конечная клиническая ответственность — ",
         "size": 17, "color": DEEP, "bold": True},
        {"text": "неделима.", "size": 17, "color": GOLD, "bold": True},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.20)
    text_box(s, x=0.55, y=7.10, w=12.3, h=0.30,
             text="Price 2019 Stanford TLR · Gerke et al. 2020 (Elsevier) · EU AI Act 2024/1689.",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s24"))


def build_s26(p):
    s = blank(p)
    slide_title(s, "3 главных вывода — медицинский AI к 2026 году.", size=24)
    text_box(s, x=0.55, y=1.20, w=12.3, h=0.40,
             text="Работающая инфраструктура + конкретная рамка ответственности.",
             size=14, italic=True, color=MID)
    cards = [
        ("✓",
         "AI-диагностика работает",
         ["mosmed.ai — 14 млн+ исследований",
          "FDA — 1 451 устройство (к концу 2025)",
          "MASAI — нагрузка −44%",
          "CV-пайплайн уровня 2017–2024"],
         "lucide-activity-blue.png", "", MID, False),
        ("~",
         "Разработка лекарств — частично",
         ["AlphaFold решена · Нобель 2024",
          "Rentosertib — Phase IIa подтверждён",
          "DSP-1181 — программа закрыта",
          "Отсев на клинических не изменился"],
         "lucide-flask-conical-blue.png", "", MID, True),
        ("→",
         "Ответственность — на враче",
         ["AI подсказывает, врач решает",
          "Инженер делает её выполнимой",
          "3 принципа → черновик чек-листа",
          "Личная версия → Лекция 14"],
         "lucide-users-blue.png", "", DEEP, False),
    ]
    card_y = 1.95
    card_h = 4.6
    card_w = 4.05
    gap = 0.15
    for i, (mark, title, lines, icon, los, color, is_gold) in enumerate(cards):
        x = 0.55 + i * (card_w + gap)
        fill = GOLD_TINT if is_gold else SURFACE
        stroke = GOLD if is_gold else LIGHT
        ocean_box(s, x, card_y, card_w, card_h, fill=fill, stroke=stroke,
                  stroke_pt=2.0 if is_gold else 1.5)
        add_image(s, ASSETS / "icons" / icon, x=x + 0.30, y=card_y + 0.35, w=1.1, h=1.1)
        text_box(s, x=x + 1.55, y=card_y + 0.45, w=card_w - 1.70, h=0.85,
                 text=mark, size=46, bold=True,
                 color=GOLD if is_gold else color, line_spacing=1.0)
        text_box(s, x=x + 0.30, y=card_y + 1.65, w=card_w - 0.6, h=0.85,
                 text=title, size=18, bold=True, color=DEEP, line_spacing=1.20)
        line_y = card_y + 2.55
        for j, ln in enumerate(lines):
            ly = line_y + j * 0.42
            filled_rect(s, x + 0.30, ly + 0.13, 0.10, 0.10, color, radius=True, radius_adj=0.5)
            text_box(s, x=x + 0.50, y=ly, w=card_w - 0.65, h=0.40,
                     text=ln, size=12, color=DEEP, line_spacing=1.30)
        # LO label removed per P1-12 (No Extra Content Rule).
    gold_callout(s, 0.55, 6.85, 12.3, 0.45,
                 "→ 3 вывода = заготовка для черновика чек-листа на следующей лекции. Не финальный синтез — заготовка.",
                 size=13)
    speaker_notes(s, load_notes("s26"))


def build_s27(p):
    s = blank(p)
    set_slide_bg(s, SURFACE)
    img_x, img_y, img_w, img_h = 0.55, 0.85, 5.5, 5.8
    ocean_box(s, img_x, img_y, img_w, img_h)
    # Real photo (Unsplash CC0): врач в халате, стетоскоп — символизирует
    # «врач принимает решение». Не баннер; реальная клиническая визуальная связка.
    add_image(s, ASSETS / "photos/s27-doctor-patient.jpg",
              x=img_x + 0.30, y=img_y + 0.40, w=img_w - 0.6, h=img_h - 1.10)
    text_box(s, x=img_x + 0.30, y=img_y + img_h - 0.65, w=img_w - 0.6, h=0.35,
             text="Врач — тот, кто берёт ответственность за пациента.",
             size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    ph_x, ph_y, ph_w, ph_h = 6.30, 0.85, 6.50, 5.8
    ocean_box(s, ph_x, ph_y, ph_w, ph_h)
    text_runs(s, ph_x + 0.4, ph_y + 0.6, ph_w - 0.8, ph_h - 1.2, [
        {"text": "Врач ставит диагноз.", "size": 30, "color": DEEP, "bold": True},
        {"newpara": True, "text": "AI подсказывает.", "size": 30, "color": MID, "bold": True},
        {"newpara": True, "text": "Инженер делает так,", "size": 30, "color": DEEP, "bold": True},
        {"newpara": True, "text": "чтобы врач мог", "size": 30, "color": DEEP, "bold": True},
        {"newpara": True, "text": "по-настоящему", "size": 36, "color": GOLD, "bold": True},
        {"text": " решать.", "size": 30, "color": DEEP, "bold": True},
    ], line_spacing=1.30, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=ph_x + 0.4, y=ph_y + ph_h - 0.50, w=ph_w - 0.8, h=0.40,
             text="Возврат к центральному вопросу — ответ.",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.LEFT)
    text_box(s, x=0.55, y=6.85, w=12.3, h=0.40,
             text="Прозрачность · валидированная популяция · audit-trail — три инженерных принципа в копилку Лекции 9.",
             size=12, italic=True, color=MID, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s27"))


def build_s28(p):
    s = blank(p)
    slide_title(s, "Что дальше: Лекция 6 + черновик чек-листа.", size=22)
    text_box(s, x=0.55, y=1.10, w=12.3, h=0.40,
             text="3 принципа сегодня — основа для черновика чек-листа на следующей лекции по этике.",
             size=13, italic=True, color=MID)
    # P1-16: navigation badge «1-2-3-4-К1-6...» removed (No Extra Content Rule —
    # «Вы здесь» markers forbidden).
    card_y = 2.20
    card_h = 3.6
    card_w = 6.0
    gap = 0.30
    ocean_box(s, 0.55, card_y, card_w, card_h)
    add_image(s, ASSETS / "icons/lucide-tractor-blue.png",
              x=0.85, y=card_y + 0.35, w=1.0, h=1.0)
    text_box(s, x=2.0, y=card_y + 0.40, w=card_w - 2.2, h=0.60,
             text="Лекция 6 — Производство и сельское хозяйство",
             size=16, bold=True, color=DEEP, line_spacing=1.20)
    text_box(s, x=0.85, y=card_y + 1.55, w=card_w - 0.5, h=0.55,
             text="Cognitive Agro Pilot — 1 500+ машин",
             size=14, bold=True, color=DEEP, line_spacing=1.20)
    text_runs(s, 0.85, card_y + 2.05, card_w - 0.5, 0.50, [
        {"text": "+30–40%", "size": 24, "bold": True, "color": GOLD},
        {"text": "  эффективности (российский кейс)",
         "size": 13, "color": DEEP, "italic": True},
    ], line_spacing=1.10, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.85, y=card_y + 2.60, w=card_w - 0.5, h=0.35,
             text="Предиктивное обслуживание · контроль качества · физический AI",
             size=11, italic=True, color=LIGHT)
    lc9_x = 0.55 + card_w + gap
    ocean_box(s, lc9_x, card_y, card_w, card_h)
    add_image(s, ASSETS / "icons/lucide-arrow-right-circle-blue.png",
              x=lc9_x + 0.30, y=card_y + 0.35, w=1.0, h=1.0)
    text_box(s, x=lc9_x + 1.45, y=card_y + 0.40, w=card_w - 1.65, h=0.60,
             text="Лекция 9 — Этика и регулирование",
             size=16, bold=True, color=DEEP, line_spacing=1.20)
    text_box(s, x=lc9_x + 0.30, y=card_y + 1.50, w=card_w - 0.5, h=1.50,
             text="3 принципа сегодня\n→ черновик чек-листа на Лекции 9\n→ личная версия на Лекции 14",
             size=13, color=DEEP, line_spacing=1.45)
    gold_callout(s, 0.55, 6.55, 12.3, 0.65,
                 "Опционально: найти 1 случай медицинского AI в новостях + применить рамку 4 актёров. Не оценивается; тренировка навыка.",
                 size=13)
    speaker_notes(s, load_notes("s28"))


def build_s29(p):
    s = blank(p)
    set_slide_bg(s, SURFACE)
    text_box(s, x=0.55, y=1.5, w=12.3, h=2.5,
             text="Q&A?",
             size=160, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    add_image(s, ASSETS / "icons/lucide-help-circle-blue.png",
              x=10.5, y=1.9, w=1.5, h=1.5)
    backups = [
        "1. Кто изменил мнение о медицинском AI?",
        "2. Чей знакомый получал AI-диагноз? Поделитесь.",
        "3. Стартап в медицинском AI — какой первый вопрос про валидацию?",
    ]
    chip_y = 4.85
    chip_h = 0.65
    chip_w = 12.3
    for i, b in enumerate(backups):
        cy = chip_y + i * (chip_h + 0.08)
        ocean_box(s, 0.55, cy, chip_w, chip_h)
        text_box(s, x=0.85, y=cy, w=chip_w - 0.6, h=chip_h,
                 text=b, size=14, italic=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.20)
    text_box(s, x=0.55, y=7.10, w=12.3, h=0.30,
             text="Курс «AI в разных индустриях» · Семинар-04 — разбор кейса · консультации",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s29"))


# ============================================================
# Main
# ============================================================
def main():
    p = setup_pres()
    builders = [
        build_s01, build_s02, build_s03, build_s04, build_s05,
        build_s06, build_s07, build_s08,
        build_s09, build_s10, build_s11, build_s12, build_s13,
        build_s14, build_s15, build_s16, build_s17a, build_s17b, build_s18,
        build_s19,
        build_s20, build_s21, build_s22, build_s23, build_s24,
        build_s26, build_s27, build_s28, build_s29,
    ]
    for fn in builders:
        fn(p)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    p.save(str(OUT))
    print(f"Saved: {OUT}")


if __name__ == "__main__":
    main()
