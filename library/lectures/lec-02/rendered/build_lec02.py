"""
Full 28-slide build of Лекции 2 «Как работают современные большие модели» (Phase 6).

Source-of-truth: deck.yaml v1.0 + chapter v1.1 (status=reviewed) +
slides/*.md (28 файлов с readable speaker notes 150-300 слов).

Pipeline pattern проверен на Лекции 1 v3.x — python-pptx direct
(вместо PowerPoint MCP) для масштаба 28+ slides.

Palette: Ocean Gradient (#21295C / #065A82 / #1C7293) + Teal #028090
secondary + Gold #F0AB00 highlight (≥1× per slide).

Visual motif: «Ocean rounded box» (radius 12, surface #F4F7FA,
stroke #1C7293, padding 16pt) на каждом content slide.

Canvas: 13.333" × 7.5" (16:9). Pacing: 55 active + 8 retrieval +
7 transitions + 5 Q&A = 75 min.
"""
import re
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt
from lxml import etree

# === Palette (LOCKED v1, mirrored from deck.yaml) ===
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

# === Constants ===
SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "rendered/assets"
SLIDES_DIR = ROOT / "slides"
OUT = ROOT / "rendered/lec-02.pptx"
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


def add_image(slide, path, x, y, w=None, h=None):
    if not Path(path).exists():
        return
    if w is not None and h is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 width=Inches(w), height=Inches(h))
    elif w is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y), width=Inches(w))
    else:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y))


def slide_title(slide, text, *, y=0.45, h=1.05, w=12.3, x=0.55, size=26,
                color=DEEP, bold=True, line_spacing=1.18, align=PP_ALIGN.LEFT):
    text_box(slide, x=x, y=y, w=w, h=h, text=text,
             size=size, bold=bold, color=color, line_spacing=line_spacing,
             align=align)


def gold_callout(slide, x, y, w, h, text, *, size=15, bold=True):
    filled_rect(slide, x, y, w, h, GOLD_TINT, stroke=GOLD, stroke_pt=1.2,
                radius=True, radius_adj=0.12)
    text_box(slide, x=x + 0.2, y=y + 0.08, w=w - 0.4, h=h - 0.16, text=text,
             size=size, bold=bold, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.LEFT, line_spacing=1.25)


def teal_callout(slide, x, y, w, h, text, *, size=14, bold=False):
    filled_rect(slide, x, y, w, h, TEAL_TINT, stroke=TEAL, stroke_pt=1.0,
                radius=True, radius_adj=0.12)
    text_box(slide, x=x + 0.18, y=y + 0.08, w=w - 0.36, h=h - 0.16, text=text,
             size=size, bold=bold, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.LEFT, line_spacing=1.25)


def right_arrow(slide, x, y, w=0.6, h=0.4, fill=MID):
    """Render MSO_SHAPE.RIGHT_ARROW between stages."""
    shp = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    disable_shadow(shp)
    return shp


def speaker_notes(slide, text):
    notes = slide.notes_slide
    tf = notes.notes_text_frame
    tf.text = text


# ============================================================
# Speaker notes loader from md
# ============================================================
def load_notes(slide_id):
    """Extract Speaker notes block from slide markdown."""
    files = list(SLIDES_DIR.glob(f"{slide_id}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding='utf-8')
    notes_match = re.search(r'## Speaker notes\s*\n(.*?)(?=\n## |\n---\s*\n## |\Z)', md, re.DOTALL)
    notes = notes_match.group(1).strip() if notes_match else ""
    notes = re.sub(r'\n+---\s*$', '', notes)
    return notes.strip()


# ============================================================
# Roadmap bar (used by cover s02 + divider s13)
# ============================================================
def roadmap_bar(slide, here_idx, *, y=6.7):
    """6-section roadmap bar at bottom of slide.
    Sections: 0 Открытие / 1 Токены / 2 Эмбеддинги / 3 Внимание / 4 Сэмплинг / 5 Финал.
    here_idx: 0..5 — gold highlight on current.
    """
    bar_h = 0.45
    n_cells = 6
    total_w = 12.3
    gap = 0.08
    cell_w = (total_w - gap * (n_cells - 1)) / n_cells
    start_x = 0.55
    labels = [
        "0  Открытие",
        "1  Токены",
        "2  Эмбеддинги",
        "3  Внимание",
        "4  Сэмплинг",
        "5  Финал",
    ]
    for i, label in enumerate(labels):
        x = start_x + i * (cell_w + gap)
        is_here = (i == here_idx)
        fill = GOLD if is_here else SOFT_GREY
        text_color = DEEP if is_here else SLATE
        filled_rect(slide, x, y, cell_w, bar_h, fill, radius=True, radius_adj=0.30)
        text_box(slide, x=x, y=y + 0.08, w=cell_w, h=bar_h - 0.16,
                 text=label, size=11, bold=is_here, color=text_color,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


# ============================================================
# Slide builders
# ============================================================
def build_s01(p):
    """Live tokenizer demo — static screenshot recreation."""
    s = blank(p)
    # Title
    slide_title(s, "Модель видит ваш запрос не буквами — а токенами", size=28)
    # Sub-frame
    text_box(s, x=0.55, y=1.55, w=12.3, h=0.45,
             text="Live tokenizer — 4 коротких примера разметки",
             size=16, italic=True, color=MID, line_spacing=1.2)
    # Tiktokenizer mock embedded in motif
    ocean_box(s, 0.55, 2.1, 12.3, 4.4)
    add_image(s, ASSETS / "diagrams/s01-tiktokenizer-mock.png",
              x=0.75, y=2.25, w=11.9, h=4.15)
    # Footer caption
    text_box(s, x=0.55, y=6.7, w=12.3, h=0.45,
             text="Источник: tiktokenizer.vercel.app (o200k_base, GPT-4o). Live demo доступен, статическая версия — fallback.",
             size=12, italic=True, color=LIGHT, line_spacing=1.25)
    speaker_notes(s, load_notes("s01"))


def build_s02(p):
    """Cover with roadmap."""
    s = blank(p)
    set_slide_bg(s, SURFACE)
    # Big "02" outline gold (decorative) — single digit "2" to fit
    text_box(s, x=9.5, y=0.2, w=4.0, h=5.0, text="2",
             size=420, bold=True, color=COVER_OUTLINE,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line_spacing=1.0)
    # ЛЕКЦИЯ tag
    text_box(s, x=0.7, y=1.0, w=8.0, h=0.55, text="ЛЕКЦИЯ 2",
             size=18, bold=True, color=TEAL, align=PP_ALIGN.LEFT)
    filled_rect(s, 0.72, 1.55, 0.7, 0.05, fill=TEAL)
    # Title — line break tuned semantically
    text_box(s, x=0.7, y=2.0, w=9.0, h=2.6,
             text="Как работают современные\nбольшие модели",
             size=52, bold=True, color=DEEP, line_spacing=1.08, align=PP_ALIGN.LEFT)
    # Subtitle / promise
    filled_rect(s, 0.7, 5.0, 0.05, 0.55, fill=TEAL)
    text_box(s, x=0.95, y=5.0, w=11.5, h=0.7,
             text="4 этапа inference: токенизация · эмбеддинг · внимание · сэмплинг",
             size=20, color=MID, italic=False, align=PP_ALIGN.LEFT, line_spacing=1.25)
    # Hero pipeline icon — 4-stage simple visualization (top right area)
    pipe_y = 5.7
    pipe_x = 0.95
    stages = ["Tk", "Em", "At", "Sm"]
    for i, label in enumerate(stages):
        cx = pipe_x + i * 0.85
        filled_rect(s, cx, pipe_y, 0.55, 0.55, MID, radius=True, radius_adj=0.5)
        text_box(s, x=cx, y=pipe_y + 0.05, w=0.55, h=0.45, text=label,
                 size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < 3:
            text_box(s, x=cx + 0.55, y=pipe_y + 0.05, w=0.30, h=0.45, text="→",
                     size=20, bold=True, color=MID, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Roadmap-bar at bottom (positioned within canvas)
    roadmap_bar(s, here_idx=0, y=6.85)
    speaker_notes(s, load_notes("s02"))


def build_s03(p):
    """Recap Lec-1 — 4 layers with model highlighted."""
    s = blank(p)
    slide_title(s, "Сегодня углубляем слой «модель» из четырёх слоёв Лекции 1", size=26)

    # Left: 4 nested layers (bottom-aligned)
    cx = 0.55
    cy_base = 6.5  # bottom row baseline
    cw_start = 5.5
    ch_unit = 0.65
    # Layer 4 (top — smallest): Приложение
    # Layer 3: Агент
    # Layer 2: Чат
    # Layer 1 (bottom — largest): Модель (gold highlight)
    layers = [
        ("Приложение", 4.5, 1.05),
        ("Агент",       5.0, 1.7),
        ("Чат",         5.5, 2.35),
        ("Модель",      6.0, 3.0),  # bottom, biggest
    ]
    # Render bottom layer (model) first then stack up
    # Model — gold highlight
    base_y = 5.85
    w, h_top = 6.0, 1.0
    ocean_box(s, cx, base_y, w, h_top, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.5)
    text_box(s, x=cx, y=base_y + 0.30, w=w, h=0.5, text="МОДЕЛЬ — углубляем сегодня",
             size=18, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Чат
    chat_y = base_y - 1.0
    ocean_box(s, cx + 0.3, chat_y, w - 0.6, 0.95, fill=SURFACE, stroke=LIGHT)
    text_box(s, x=cx + 0.3, y=chat_y + 0.25, w=w - 0.6, h=0.5, text="Чат",
             size=16, bold=True, color=MID, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Агент
    agent_y = chat_y - 0.95
    ocean_box(s, cx + 0.6, agent_y, w - 1.2, 0.90, fill=SURFACE, stroke=LIGHT)
    text_box(s, x=cx + 0.6, y=agent_y + 0.22, w=w - 1.2, h=0.5, text="Агент",
             size=16, bold=True, color=MID, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Приложение
    app_y = agent_y - 0.90
    ocean_box(s, cx + 0.9, app_y, w - 1.8, 0.85, fill=SURFACE, stroke=LIGHT)
    text_box(s, x=cx + 0.9, y=app_y + 0.20, w=w - 1.8, h=0.5, text="Приложение",
             size=16, bold=True, color=MID, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    text_box(s, x=cx, y=app_y - 0.45, w=w, h=0.4,
             text="(Лекция 1 §3.2)",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Right: bridge
    rx = 6.95
    rw = 6.0
    # What we know
    ocean_box(s, rx, 1.85, rw, 2.2)
    text_box(s, x=rx + 0.25, y=2.0, w=rw - 0.5, h=0.5,
             text="Что мы знаем (Лекция 1 §3.2):",
             size=15, bold=True, color=MID)
    text_box(s, x=rx + 0.25, y=2.55, w=rw - 0.5, h=1.4,
             text="Модель = stateless inference. Вход — данные, выход — предсказание. Между вызовами памяти нет.",
             size=15, color=DEEP, line_spacing=1.3)

    # What we'll learn
    ocean_box(s, rx, 4.3, rw, 2.4, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, x=rx + 0.25, y=4.45, w=rw - 0.5, h=0.5,
             text="Что узнаем сегодня:",
             size=15, bold=True, color=DEEP)
    text_box(s, x=rx + 0.25, y=5.0, w=rw - 0.5, h=1.6,
             text="Что внутри inference. 4 этапа:\nтокенизация → эмбеддинг → внимание → сэмплинг",
             size=15, bold=False, color=DEEP, line_spacing=1.4)

    speaker_notes(s, load_notes("s03"))


def build_s04(p):
    """Central question + 3 promises."""
    s = blank(p)
    # Slide title small at top
    text_box(s, x=0.55, y=0.4, w=12.3, h=0.4,
             text="Главный вопрос лекции",
             size=18, bold=True, color=MID, align=PP_ALIGN.LEFT)
    # Central question — big, ocean box (semantic line break before «и» / after dash)
    ocean_box(s, 0.55, 1.05, 12.3, 1.95)
    text_box(s, x=1.0, y=1.20, w=11.4, h=1.65,
             text='«Что происходит внутри LLM между моим запросом и ответом —\nи какие из этих механизмов меняют, как я её использую?»',
             size=24, bold=True, color=DEEP, italic=False,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.3)

    # Gold-маркер
    filled_rect(s, 4.4, 3.25, 4.5, 0.45, GOLD_TINT, stroke=GOLD, stroke_pt=1.0, radius=True, radius_adj=0.5)
    text_box(s, x=4.4, y=3.30, w=4.5, h=0.35,
             text="3 ответа — финал лекции",
             size=13, bold=True, color=DEEP, italic=True,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # 3 promise boxes
    card_y = 3.95
    card_h = 2.85
    card_w = 3.95
    gap = 0.20
    start_x = 0.55
    promises = [
        ("1", "Почему промпт с ролью\nработает лучше пустого?", "Раздел 3 — внимание"),
        ("2", "Почему AI плохо\nсчитает буквы?", "Раздел 1 — токенизация"),
        ("3", "Почему один запрос\nдаёт разные ответы?", "Раздел 4 — сэмплинг"),
    ]
    for i, (n, q, dest) in enumerate(promises):
        x = start_x + i * (card_w + gap)
        ocean_box(s, x, card_y, card_w, card_h)
        # Number badge — top-left
        filled_rect(s, x + 0.3, card_y + 0.3, 0.7, 0.7, MID, radius=True, radius_adj=0.5)
        text_box(s, x=x + 0.3, y=card_y + 0.32, w=0.7, h=0.65,
                 text=n, size=28, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Question — full width, below the badge (avoids narrow wrapping)
        text_box(s, x=x + 0.25, y=card_y + 1.20, w=card_w - 0.5, h=1.40,
                 text=q, size=18, bold=True, color=DEEP, line_spacing=1.30)
        # Arrow
        text_box(s, x=x + 0.25, y=card_y + 2.40, w=card_w - 0.5, h=0.5,
                 text="→ " + dest,
                 size=15, italic=True, color=MID, line_spacing=1.2)
    speaker_notes(s, load_notes("s04"))


def build_s05(p):
    """What is token — 3 examples + gold callout."""
    s = blank(p)
    slide_title(s, "Токен — id из словаря модели. Не буква и не слово.", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Статистически частая подпоследовательность",
             size=15, italic=True, color=MID)

    # 3 example cards vertical
    ex_y = 2.05
    ex_h = 0.95
    ex_w = 12.3
    gap = 0.15
    examples = [
        ("Пример 1.", "cat", ["cat"], "1 токен / 1 id"),
        ("Пример 2.", "tokenization", ["token", "ization"], "2 токена"),
        ("Пример 3.", "клубника", ["к", "луб", "ника"], "3 токена · o200k_base"),
    ]
    for i, (lbl, word, tokens, count_text) in enumerate(examples):
        y = ex_y + i * (ex_h + gap)
        ocean_box(s, 0.55, y, ex_w, ex_h)
        # Label
        text_box(s, x=0.75, y=y + 0.18, w=1.6, h=0.6,
                 text=lbl, size=14, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
        # Word
        text_box(s, x=2.4, y=y + 0.18, w=2.5, h=0.6,
                 text=word, size=22, bold=True, color=DEEP,
                 font=FONT_MONO, anchor=MSO_ANCHOR.MIDDLE)
        # Arrow
        text_box(s, x=4.95, y=y + 0.18, w=0.5, h=0.6,
                 text="→", size=22, bold=True, color=MID,
                 anchor=MSO_ANCHOR.MIDDLE)
        # Token chips
        cur_x = 5.5
        token_colors = [MID, LIGHT, TEAL]
        for j, tok in enumerate(tokens):
            tw = max(0.8, len(tok) * 0.18 + 0.4)
            col = token_colors[j % len(token_colors)]
            chip(s, cur_x, y + 0.25, tw, 0.45, f"[{tok}]", fill=col, color=WHITE, size=14)
            cur_x += tw + 0.10
        # Count
        text_box(s, x=10.5, y=y + 0.18, w=1.7, h=0.6,
                 text=count_text, size=14, bold=True, color=DEEP,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

    # Gold callout
    gold_callout(s, 0.55, 5.4, 12.3, 0.75,
                 "В среднем: 1 токен ≈ 4 символа в EN ≈ 2 символа в RU",
                 size=18)

    # Poll prompt
    teal_callout(s, 0.55, 6.35, 12.3, 0.75,
                 "Подумайте 15 сек: «сильнее» — 1, 2 или 3 токена? (Проверить через tiktokenizer)",
                 size=14, bold=True)
    speaker_notes(s, load_notes("s05"))


def build_s06(p):
    """BPE before/after — 2 columns."""
    s = blank(p)
    slide_title(s, "BPE — компромисс между алфавитом и словарём", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Словарь строится один раз перед обучением; в inference — lookup",
             size=15, italic=True, color=MID)

    # Two columns
    col_w = 5.5
    col_h = 4.05
    col_y = 2.15
    left_x = 1.0
    right_x = 6.8

    # Before
    ocean_box(s, left_x, col_y, col_w, col_h)
    text_box(s, x=left_x + 0.3, y=col_y + 0.2, w=col_w - 0.6, h=0.5,
             text="Before (обучающий корпус)", size=17, bold=True, color=MID)
    before_items = ["low", "lower", "newest", "widest"]
    for i, item in enumerate(before_items):
        y_i = col_y + 0.95 + i * 0.65
        # Bullet
        filled_rect(s, left_x + 0.45, y_i + 0.25, 0.13, 0.13, MID, radius=True, radius_adj=0.5)
        text_box(s, x=left_x + 0.75, y=y_i, w=col_w - 1.0, h=0.55,
                 text=item, size=22, color=DEEP, font=FONT_MONO,
                 anchor=MSO_ANCHOR.MIDDLE)

    # Big arrow between columns — fill the gap with a proper RIGHT_ARROW shape
    arrow_gap_x = left_x + col_w + 0.05
    arrow_w = right_x - arrow_gap_x - 0.05
    right_arrow(s, arrow_gap_x, col_y + col_h / 2 - 0.30, w=arrow_w, h=0.60, fill=MID)

    # After
    ocean_box(s, right_x, col_y, col_w, col_h, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, x=right_x + 0.3, y=col_y + 0.2, w=col_w - 0.6, h=0.5,
             text="After (BPE-словарь)", size=17, bold=True, color=DEEP)
    after_items = ["low", "er", "new", "est", "wid"]
    for i, item in enumerate(after_items):
        y_i = col_y + 0.95 + i * 0.60
        filled_rect(s, right_x + 0.45, y_i + 0.22, 0.13, 0.13, GOLD, radius=True, radius_adj=0.5)
        text_box(s, x=right_x + 0.75, y=y_i, w=col_w - 1.0, h=0.5,
                 text=item, size=22, color=DEEP, font=FONT_MONO,
                 anchor=MSO_ANCHOR.MIDDLE)

    # Gold callout bottom
    gold_callout(s, 0.55, 6.4, 12.3, 0.65,
                 "BPE-словарь строится один раз до обучения. В inference — lookup готовых правил, не runtime-вычисление.",
                 size=15)
    # Footer caption
    text_box(s, x=0.55, y=7.10, w=12.3, h=0.3,
             text="Sennrich et al. (2016). Альтернативы: WordPiece (BERT), SentencePiece (Llama 2, T5).",
             size=12, italic=True, color=LIGHT)
    speaker_notes(s, load_notes("s06"))


def build_s07(p):
    """Strawberry — split + 3 consequences."""
    s = blank(p)
    slide_title(s, 'AI ошибается в «сколько r в strawberry» — слова не из букв, а из 2-3 токенов', size=24)

    # Left: strawberry split (image)
    ocean_box(s, 0.55, 1.55, 6.2, 4.8)
    add_image(s, ASSETS / "diagrams/s07-strawberry-split.png",
              x=0.75, y=1.7, w=5.8, h=4.5)

    # Right: 3 consequence cards
    rx = 7.0
    rw = 5.85
    cards = [
        ("Подсчёт символов", "«Сколько r в strawberry?» — ломается систематически, неочевидно для пользователя."),
        ("Опечатки", "methodlogy ↦ другие токены, чем methodology. Маленькая опечатка → большой сдвиг в ответе."),
        ("Регистр и пробелы", "cat, ` cat`, Cat, CAT — разные токены, разные id."),
    ]
    cy = 1.55
    ch = 1.50
    cgap = 0.13
    for i, (head, body) in enumerate(cards):
        y = cy + i * (ch + cgap)
        ocean_box(s, rx, y, rw, ch)
        text_box(s, x=rx + 0.25, y=y + 0.12, w=rw - 0.5, h=0.45,
                 text=head, size=18, bold=True, color=MID)
        text_box(s, x=rx + 0.25, y=y + 0.62, w=rw - 0.5, h=0.85,
                 text=body, size=15, color=DEEP, line_spacing=1.30)

    # Gold callout
    gold_callout(s, 0.55, 6.5, 12.3, 0.85,
                 "Для побитово-точных операций — внешний инструмент (Python, regex), не чистый LLM-инференс.",
                 size=18)
    speaker_notes(s, load_notes("s07"))


def build_s08(p):
    """Cross-language tokens/char bar chart."""
    s = blank(p)
    slide_title(s, "Один и тот же текст по-русски стоит в 2× дороже, чем по-английски", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Токены на символ — следствие распределения языков в обучающем корпусе",
             size=15, italic=True, color=MID)

    # Left: bar chart
    ocean_box(s, 0.55, 2.05, 7.5, 4.65)
    add_image(s, ASSETS / "charts/s08-tokens-per-char.png",
              x=0.75, y=2.20, w=7.1, h=4.35)

    # Right: data table-like
    rx = 8.3
    rw = 4.55
    ocean_box(s, rx, 2.05, rw, 4.65)
    text_box(s, x=rx + 0.2, y=2.20, w=rw - 0.4, h=0.45,
             text="Ориентир токены/символ",
             size=15, bold=True, color=MID)
    rows = [
        ("Английский", "0.25", LIGHT),
        ("Русский (gold)", "0.50", GOLD),
        ("Китайский", "0.80", LIGHT),
        ("Python-код", "0.40", TEAL),
    ]
    for i, (lang, val, c) in enumerate(rows):
        ry = 2.85 + i * 0.85
        text_box(s, x=rx + 0.25, y=ry, w=rw * 0.55, h=0.45,
                 text=lang, size=14, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rx + rw * 0.55, y=ry, w=rw * 0.4, h=0.45,
                 text=val, size=18, bold=True, color=c,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

    # Gold callout bottom
    gold_callout(s, 0.55, 6.85, 12.3, 0.55,
                 "API-стоимость RU ≈ 2× от EN. Для batch — переводить в EN, если допустимо.",
                 size=15)
    speaker_notes(s, load_notes("s08"))


def build_s09(p):
    """What is embedding — token to vector."""
    s = blank(p)
    slide_title(s, "Каждому токену сопоставлен вектор — выучен на тренировке, фиксирован", size=24)

    # Top: token-to-vector visualization
    ocean_box(s, 0.55, 1.55, 12.3, 3.6)
    add_image(s, ASSETS / "diagrams/s09-token-to-vector.png",
              x=0.75, y=1.70, w=11.9, h=3.3)

    # Bottom: 2 callouts side-by-side
    bw = 6.0
    by = 5.45
    bh = 1.55
    # Left — dimensions
    ocean_box(s, 0.55, by, bw, bh)
    text_box(s, x=0.75, y=by + 0.1, w=bw - 0.4, h=0.4,
             text="Размерности (ориентир)",
             size=14, bold=True, color=MID)
    rows_dim = [
        ("text-embedding-3-small", "1536 dim"),
        ("text-embedding-3-large", "3072 dim"),
        ("Внутренний эмбеддинг flagship LLM", "тысячи dim"),
    ]
    for i, (name, val) in enumerate(rows_dim):
        y = by + 0.5 + i * 0.32
        text_box(s, x=0.85, y=y, w=bw * 0.65, h=0.30,
                 text=name, size=12, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=0.85 + bw * 0.62, y=y, w=bw * 0.32, h=0.30,
                 text=val, size=12, bold=True, color=TEAL,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

    # Right — gold callout: "близость в пространстве = смысл"
    gold_callout(s, 7.0, by, bw, bh,
                 "Геометрическая близость векторов = семантическая близость токенов.\n«Кот» близко к «собаке» — выучилось из контекстов корпуса.",
                 size=14)
    speaker_notes(s, load_notes("s09"))


def build_s10(p):
    """Sentence similarity 5×5 heatmap."""
    s = blank(p)
    slide_title(s, "Близость в пространстве эмбеддингов = семантическая близость", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="В 2026 это работает на уровне предложений, не только слов",
             size=15, italic=True, color=MID)

    # Heatmap centered
    ocean_box(s, 1.7, 2.05, 10.0, 4.55)
    add_image(s, ASSETS / "diagrams/s10-heatmap.png",
              x=2.0, y=2.20, w=9.4, h=4.30)

    # Footer caption
    text_box(s, x=0.55, y=6.75, w=12.3, h=0.40,
             text="Cosine similarity — мера угла между векторами; диапазон [−1, 1], ближе к 1 — более похожи.",
             size=13, italic=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, x=0.55, y=7.15, w=12.3, h=0.30,
             text="Числа illustrative; воспроизводимы на sentence-transformers/all-MiniLM-L6-v2 (384-dim) или OpenAI text-embedding-3-small (1536-dim).",
             size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s10"))


def build_s11(p):
    """3 uses of embeddings — 3 motif cards horizontal."""
    s = blank(p)
    slide_title(s, "Эмбеддинги дают similarity, clustering и search — основу RAG", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Три практических применения, надстраиваемых над одной embedding-таблицей",
             size=15, italic=True, color=MID)

    # 3 cards horizontal
    card_y = 2.20
    card_h = 4.5
    card_w = 3.95
    gap = 0.20
    start_x = 0.55
    cards = [
        ("magnet", "Similarity", "Поиск похожих",
         "Похожие тикеты в support,\nкейсы в юр-базе,\nрезюме в HR-системе.",
         False),
        ("box", "Clustering", "Кластеризация",
         "k-means — анализ\nжалоб клиентов,\nтематика корпусов.",
         False),
        ("search-check", "Search", "Семантический поиск",
         "Запрос → top-K\nпохожих документов.\n\n→ Основа RAG (Лекция 3)",
         True),
    ]
    for i, (icon, ttl, sub, body, is_gold) in enumerate(cards):
        x = start_x + i * (card_w + gap)
        if is_gold:
            ocean_box(s, x, card_y, card_w, card_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.5)
        else:
            ocean_box(s, x, card_y, card_w, card_h)
        # Icon
        icon_path = ASSETS / f"icons/{icon}.png"
        if icon_path.exists():
            add_image(s, icon_path, x=x + (card_w - 1.0) / 2, y=card_y + 0.35, w=1.0, h=1.0)
        # Title
        text_box(s, x=x + 0.2, y=card_y + 1.55, w=card_w - 0.4, h=0.5,
                 text=ttl, size=22, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER)
        # Subtitle
        text_box(s, x=x + 0.2, y=card_y + 2.10, w=card_w - 0.4, h=0.4,
                 text=sub, size=15, italic=True, color=MID,
                 align=PP_ALIGN.CENTER)
        # Body
        text_box(s, x=x + 0.25, y=card_y + 2.65, w=card_w - 0.5, h=1.7,
                 text=body, size=14, color=DEEP if is_gold else DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.30, bold=is_gold)

    speaker_notes(s, load_notes("s11"))


def build_s12(p):
    """Semantic vs full-text — query + 2 columns."""
    s = blank(p)
    slide_title(s, "Semantic search находит то, что full-text пропустит", size=26)

    # Query
    filled_rect(s, 4.0, 1.45, 5.3, 0.7, GOLD_TINT, stroke=GOLD, stroke_pt=1.5, radius=True, radius_adj=0.25)
    text_box(s, x=4.0, y=1.50, w=5.3, h=0.30,
             text="Запрос",
             size=11, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP)
    text_box(s, x=4.0, y=1.75, w=5.3, h=0.35,
             text="клубника",
             size=22, bold=True, color=DEEP, font=FONT_MONO,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Two result columns
    col_w = 5.8
    col_h = 4.2
    col_y = 2.50
    left_x = 0.55
    right_x = 6.95

    # Full-text
    ocean_box(s, left_x, col_y, col_w, col_h)
    text_box(s, x=left_x + 0.3, y=col_y + 0.15, w=col_w - 0.6, h=0.4,
             text="Full-text (Elasticsearch, Lucene)",
             size=15, bold=True, color=MID)
    full_text_items = [
        ("клубника", True),
        ("клубники (стемминг)", True),
        ("клубнику", True),
        ("strawberry", False),
        ("ягода", False),
        ("лесная земляника", False),
    ]
    for i, (item, found) in enumerate(full_text_items):
        y = col_y + 0.7 + i * 0.50
        mark = "✓" if found else "✗"
        mark_color = TEAL if found else SLATE
        text_box(s, x=left_x + 0.35, y=y, w=0.45, h=0.45,
                 text=mark, size=20, bold=True, color=mark_color,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=left_x + 0.85, y=y, w=col_w - 1.1, h=0.45,
                 text=item, size=14,
                 color=DEEP if found else SLATE,
                 italic=not found,
                 anchor=MSO_ANCHOR.MIDDLE)

    # Semantic
    ocean_box(s, right_x, col_y, col_w, col_h, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, x=right_x + 0.3, y=col_y + 0.15, w=col_w - 0.6, h=0.4,
             text="Semantic (эмбеддинги + ближайшие соседи)",
             size=15, bold=True, color=DEEP)
    semantic_items = [
        ("клубника", "точное"),
        ("клубники", "морфология"),
        ("strawberry", "cross-lang"),
        ("ягода", "родовое"),
        ("лесная земляника", "близкий смысл"),
        ("…", "ещё близкие"),
    ]
    for i, (item, why) in enumerate(semantic_items):
        y = col_y + 0.7 + i * 0.50
        text_box(s, x=right_x + 0.35, y=y, w=0.45, h=0.45,
                 text="✓", size=20, bold=True, color=GOLD,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=right_x + 0.85, y=y, w=col_w * 0.55, h=0.45,
                 text=item, size=14, bold=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=right_x + 0.85 + col_w * 0.55, y=y, w=col_w * 0.4 - 0.85, h=0.45,
                 text=f"— {why}",
                 size=12, italic=True, color=MID,
                 anchor=MSO_ANCHOR.MIDDLE)

    # Gold callout bottom
    gold_callout(s, 0.55, 6.85, 12.3, 0.55,
                 "Base layer RAG — реализация в Лекции 3 (Retrieval-Augmented Generation).",
                 size=15)
    speaker_notes(s, load_notes("s12"))


def build_s13(p):
    """Section 3 divider — big number + roadmap."""
    s = blank(p)
    set_slide_bg(s, SURFACE)

    # Big "Раздел 3" outline gold
    text_box(s, x=0.55, y=1.30, w=12.3, h=2.5,
             text="Раздел 3",
             size=140, bold=True, color=GOLD,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    # Sub-title
    text_box(s, x=0.55, y=3.9, w=12.3, h=0.7,
             text="Механизм внимания",
             size=44, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Assertion
    text_box(s, x=0.55, y=4.75, w=12.3, h=0.5,
             text="Как модель решает, что важно сейчас",
             size=20, italic=True, color=MID,
             align=PP_ALIGN.CENTER)
    # Roadmap-bar (here = section 3)
    roadmap_bar(s, here_idx=3)
    speaker_notes(s, load_notes("s13"))


def build_s14(p):
    """What is attention — flashlight metaphor + bar chart."""
    s = blank(p)
    slide_title(s, "Attention выдаёт распределение весов на все токены контекста (сумма = 1)", size=24)
    text_box(s, x=0.55, y=1.50, w=12.3, h=0.4,
             text="Какие токены сейчас важны для предсказания следующего",
             size=15, italic=True, color=MID)

    # Right: bar chart distribution — DOMINANT, занимает большую часть слайда
    ocean_box(s, 0.55, 2.05, 8.5, 4.6)
    add_image(s, ASSETS / "charts/s14-attention-bars.png",
              x=0.75, y=2.20, w=8.1, h=4.3)
    text_box(s, x=0.55, y=6.70, w=8.5, h=0.4,
             text="Распределение весов на токенах контекста — основное содержание",
             size=14, italic=True, color=MID, align=PP_ALIGN.CENTER)

    # Left/right: 3 facts column + small flashlight metaphor at bottom
    rx = 9.35
    rw = 3.55
    ocean_box(s, rx, 2.05, rw, 3.2)
    text_box(s, x=rx + 0.2, y=2.20, w=rw - 0.4, h=0.4,
             text="3 свойства",
             size=15, bold=True, color=MID)
    facts = [
        "На вход — все токены контекста.",
        "На выходе — распределение, Σ = 1.",
        "Пересчитывается на каждом шаге.",
    ]
    for i, f in enumerate(facts):
        y = 2.70 + i * 0.78
        # Number badge
        filled_rect(s, rx + 0.2, y + 0.05, 0.32, 0.32, MID, radius=True, radius_adj=0.5)
        text_box(s, x=rx + 0.2, y=y + 0.06, w=0.32, h=0.30,
                 text=str(i + 1), size=13, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rx + 0.6, y=y, w=rw - 0.8, h=0.65,
                 text=f, size=14, color=DEEP, line_spacing=1.30, anchor=MSO_ANCHOR.TOP)

    # Flashlight metaphor — small, on the right at bottom
    ocean_box(s, rx, 5.35, rw, 1.50)
    add_image(s, ASSETS / "diagrams/s14-flashlight.png",
              x=rx + 0.15, y=5.45, w=1.3, h=1.3)
    text_box(s, x=rx + 1.50, y=5.55, w=rw - 1.65, h=1.10,
             text="Метафора: фонарик в тёмной комнате — модель «подсвечивает» одни токены ярче других.",
             size=12, italic=True, color=DEEP, line_spacing=1.30, anchor=MSO_ANCHOR.MIDDLE)

    # Caption mid-bottom
    text_box(s, x=0.55, y=7.15, w=12.3, h=0.30,
             text="Без формул. Multi-head, Q/K/V — доп. чтение (Vaswani et al. 2017).",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s14"))


def build_s15(p):
    """Worked example + role effect (Part A + Part B)."""
    s = blank(p)
    slide_title(s, "Role-токены получают повышенный вес в attention", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Часть A — рабочий пример; часть B — эффект роли (1-е из 3 «почему»)",
             size=15, italic=True, color=MID)

    # Part A — top
    pa_y = 2.0
    pa_h = 2.45
    ocean_box(s, 0.55, pa_y, 12.3, pa_h)
    text_box(s, x=0.75, y=pa_y + 0.12, w=12.0, h=0.4,
             text="A. Worked example — куда смотрит «она»",
             size=15, bold=True, color=MID)
    # Sentence with arrows visualization
    # Sentence text
    sent_y = pa_y + 0.65
    text_box(s, x=0.75, y=sent_y, w=12.0, h=0.5,
             text='«Кот съел мышь, потому что она была голодна»',
             size=22, bold=True, color=DEEP, font=FONT_MONO,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Three arrows from "она" → varying strength
    arrows = [("она → мышь", "толстая · главный вес", GOLD, 3.0),
              ("она → была", "средняя", MID, 2.0),
              ("она → голодна", "тонкая", LIGHT, 1.2)]
    ar_y = sent_y + 0.75
    ar_w = 3.85
    ar_h = 0.50
    ar_gap = 0.15
    ar_x_start = (12.3 - (3 * ar_w + 2 * ar_gap)) / 2 + 0.55
    for i, (lbl, why, col, weight) in enumerate(arrows):
        ax = ar_x_start + i * (ar_w + ar_gap)
        # Arrow chip
        filled_rect(s, ax, ar_y, ar_w, ar_h, col, radius=True, radius_adj=0.4)
        text_box(s, x=ax, y=ar_y + 0.05, w=ar_w, h=0.40,
                 text=lbl, size=16, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=ax, y=ar_y + ar_h + 0.02, w=ar_w, h=0.30,
                 text=why, size=12, italic=True, color=DEEP,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Disclaimer
    text_box(s, x=0.75, y=pa_y + pa_h - 0.30, w=12.0, h=0.25,
             text="Упрощение: реальный attention map — сотни связей. Модель смотрит статистически, не делает грамматический разбор.",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Part B — bottom
    pb_y = 4.6
    pb_h = 2.30
    # Two columns side-by-side
    col_w = 6.0
    # Without role
    ocean_box(s, 0.55, pb_y, col_w, pb_h)
    text_box(s, x=0.75, y=pb_y + 0.10, w=col_w - 0.4, h=0.4,
             text="Без роли",
             size=18, bold=True, color=MID)
    text_box(s, x=0.75, y=pb_y + 0.60, w=col_w - 0.4, h=0.55,
             text='«Объясни асинхронность»',
             size=18, color=DEEP, font=FONT_MONO,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.75, y=pb_y + 1.25, w=col_w - 0.4, h=0.95,
             text="→ generic ответ\n(низкий вес role-токенов в attention)",
             size=15, italic=True, color=DEEP, line_spacing=1.3)
    # With role
    ocean_box(s, 6.85, pb_y, col_w, pb_h, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, x=7.05, y=pb_y + 0.10, w=col_w - 0.4, h=0.4,
             text="С ролью",
             size=18, bold=True, color=DEEP)
    text_runs(s, 7.05, pb_y + 0.60, col_w - 0.4, 0.6, [
        {"text": "«Ты ", "size": 18, "color": DEEP, "font": FONT_MONO},
        {"text": "эксперт по Python", "size": 18, "color": GOLD, "font": FONT_MONO, "bold": True},
        {"text": ". Объясни асинхронность ", "size": 18, "color": DEEP, "font": FONT_MONO},
        {"text": "джуниору", "size": 18, "color": GOLD, "font": FONT_MONO, "bold": True},
        {"text": ".»", "size": 18, "color": DEEP, "font": FONT_MONO},
    ], anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=7.05, y=pb_y + 1.25, w=col_w - 0.4, h=0.95,
             text="→ role-токены подсвечены\n(высокий вес в attention)",
             size=15, italic=True, bold=True, color=DEEP, line_spacing=1.3)

    speaker_notes(s, load_notes("s15"))


def build_s16(p):
    """Context window 3-points bar chart."""
    s = blank(p)
    slide_title(s, "Контекстное окно — физический предел того, сколько модель видит одновременно", size=24)
    text_box(s, x=0.55, y=1.55, w=12.3, h=0.4,
             text="Эволюция context window + квадратичная стоимость attention",
             size=15, italic=True, color=MID)

    # Bar chart
    ocean_box(s, 0.55, 2.10, 8.0, 4.45)
    add_image(s, ASSETS / "charts/s16-context-window.png",
              x=0.75, y=2.25, w=7.6, h=4.15)

    # Right: scaling info
    rx = 8.85
    rw = 4.0
    ocean_box(s, rx, 2.10, rw, 4.45)
    text_box(s, x=rx + 0.2, y=2.25, w=rw - 0.4, h=0.4,
             text="Эволюция и стоимость",
             size=15, bold=True, color=MID)
    info_lines = [
        ("2022 → 2026:", "×250 рост"),
        ("Темп:", "×10 / 1-2 года"),
        ("Cost N²:", "1M ≈ 16× от 100k"),
        ("Архитектура:", "ванильная attention"),
    ]
    for i, (lbl, val) in enumerate(info_lines):
        y = 2.85 + i * 0.55
        text_box(s, x=rx + 0.25, y=y, w=rw * 0.5, h=0.4,
                 text=lbl, size=13, italic=True, color=MID,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rx + rw * 0.45, y=y, w=rw * 0.5, h=0.4,
                 text=val, size=13, bold=True, color=DEEP,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    # Big gold N² hint
    filled_rect(s, rx + 0.5, 5.15, rw - 1.0, 1.0, GOLD, radius=True, radius_adj=0.15)
    text_box(s, x=rx + 0.5, y=5.20, w=rw - 1.0, h=0.95,
             text="N²",
             size=44, bold=True, color=WHITE,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Gold callout
    gold_callout(s, 0.55, 6.70, 12.3, 0.70,
                 "Стоимость attention растёт квадратично от длины. 1M ≈ 16× дороже 100k — production-pricing с batching; чистая N²-теория дала бы 100×.",
                 size=15)
    speaker_notes(s, load_notes("s16"))


def build_s17(p):
    """Long-context fails — U-shape curve."""
    s = blank(p)
    slide_title(s, "Большое контекстное окно ≠ хорошее использование контекста", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Lost-in-the-middle effect — модель забывает середину",
             size=15, italic=True, color=MID)

    # U-shape chart
    ocean_box(s, 0.55, 2.0, 8.5, 4.5)
    add_image(s, ASSETS / "charts/s17-u-shape.png",
              x=0.75, y=2.15, w=8.1, h=4.20)

    # Right: explanation
    rx = 9.35
    rw = 3.55
    ocean_box(s, rx, 2.0, rw, 4.5)
    text_box(s, x=rx + 0.2, y=2.15, w=rw - 0.4, h=0.4,
             text="Эксперимент",
             size=14, bold=True, color=MID)
    text_box(s, x=rx + 0.2, y=2.55, w=rw - 0.4, h=1.7,
             text="Factoid вставлен в позицию X (начало / середина / конец) 100k-контекста. Модель отвечает на факт.",
             size=12, color=DEEP, line_spacing=1.30)
    # Results
    text_box(s, x=rx + 0.2, y=4.20, w=rw - 0.4, h=0.4,
             text="Результаты",
             size=14, bold=True, color=MID)
    res_lines = [
        ("Начало:", "~75%", GOLD),
        ("Середина:", "~50%", LIGHT),
        ("Конец:", "~75%", GOLD),
    ]
    for i, (lbl, val, col) in enumerate(res_lines):
        y = 4.65 + i * 0.40
        text_box(s, x=rx + 0.2, y=y, w=rw * 0.6, h=0.35,
                 text=lbl, size=13, italic=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rx + rw * 0.55, y=y, w=rw * 0.4, h=0.35,
                 text=val, size=14, bold=True, color=col,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=rx + 0.2, y=5.95, w=rw - 0.4, h=0.5,
             text="Liu et al. 2023.\nLost in the Middle.\narXiv:2307.03172",
             size=10, italic=True, color=LIGHT, line_spacing=1.20)

    # Gold callout bottom
    gold_callout(s, 0.55, 6.70, 12.3, 0.55,
                 "Инженерный вывод: важное помещайте в начало или в конец промпта, не в середину.",
                 size=15)
    speaker_notes(s, load_notes("s17"))


def build_s18(p):
    """Distribution — top-5 bar chart."""
    s = blank(p)
    slide_title(s, "На каждом шаге модель выдаёт распределение вероятностей на все токены — выбирает один", size=22)

    # Context
    filled_rect(s, 4.5, 1.45, 4.3, 0.65, GOLD_TINT, stroke=GOLD, stroke_pt=1.2, radius=True, radius_adj=0.25)
    text_box(s, x=4.5, y=1.5, w=4.3, h=0.30,
             text="Контекст", size=11, bold=True, color=MID,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP)
    text_box(s, x=4.5, y=1.70, w=4.3, h=0.35,
             text="«Сегодня я съел …»", size=18, bold=True, color=DEEP,
             font=FONT_MONO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Chart
    ocean_box(s, 0.55, 2.30, 8.5, 4.05)
    add_image(s, ASSETS / "charts/s18-distribution.png",
              x=0.75, y=2.45, w=8.1, h=3.75)

    # Right: top-5 table
    rx = 9.35
    rw = 3.55
    ocean_box(s, rx, 2.30, rw, 4.05)
    text_box(s, x=rx + 0.2, y=2.45, w=rw - 0.4, h=0.4,
             text="Top-5 кандидатов",
             size=14, bold=True, color=MID)
    rows = [
        ("яблоко", "0.32", GOLD),
        ("пиццу",  "0.19", LIGHT),
        ("салат",  "0.14", LIGHT),
        ("булочку","0.11", LIGHT),
        ("огурец", "0.08", LIGHT),
    ]
    for i, (tok, p_val, col) in enumerate(rows):
        y = 2.90 + i * 0.45
        text_box(s, x=rx + 0.2, y=y, w=rw * 0.55, h=0.40,
                 text=tok, size=14, color=DEEP, font=FONT_MONO,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rx + rw * 0.55, y=y, w=rw * 0.4, h=0.40,
                 text=p_val, size=16, bold=True, color=col,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=rx + 0.2, y=5.30, w=rw - 0.4, h=0.95,
             text="… остальные ~200k токенов:\nкаждый < 0.05\nΣ = 1",
             size=12, italic=True, color=LIGHT, line_spacing=1.30)

    # Gold callout
    gold_callout(s, 0.55, 6.55, 12.3, 0.55,
                 "Сэмплинг = правило, по которому из распределения выбирается один токен. Дальше — температура.",
                 size=14)
    speaker_notes(s, load_notes("s18"))


def build_s19(p):
    """Temperature — 3 distributions side-by-side."""
    s = blank(p)
    slide_title(s, "Температура: насколько острым будет выбор", size=28)
    text_box(s, x=0.55, y=1.40, w=12.3, h=0.4,
             text="T = 0 (argmax)  ·  T = 1.0 (стандарт)  ·  T = 2.0 (хаос)",
             size=18, italic=True, color=MID)

    # 3 distributions side-by-side
    card_y = 2.00
    card_h = 4.55
    card_w = 4.10
    gap = 0.10
    start_x = 0.55
    descrs = [
        ("T = 0  ·  argmax",
         "Детерминированный\nвыбор — яблоко.\n10 запусков → одинаково.",
         "s19-T0.png", GOLD),
        ("T = 1.0  ·  стандарт",
         "Сэмплирование\nпропорционально P.\nЕстественная вариативность.\n(T = 0.7 — consensus для чата)",
         "s19-T1.png", MID),
        ("T = 2.0  ·  хаос",
         "Распределение сглажено;\nчасто выбираются\nнеожиданные варианты.",
         "s19-T2.png", TEAL),
    ]
    for i, (head, body, img_name, color) in enumerate(descrs):
        x = start_x + i * (card_w + gap)
        is_standard = (i == 1)
        if is_standard:
            ocean_box(s, x, card_y, card_w, card_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.5)
        else:
            ocean_box(s, x, card_y, card_w, card_h)
        # Title
        text_box(s, x=x + 0.2, y=card_y + 0.15, w=card_w - 0.4, h=0.45,
                 text=head, size=18, bold=True, color=color,
                 align=PP_ALIGN.CENTER)
        # Chart image
        img = ASSETS / f"charts/{img_name}"
        if img.exists():
            add_image(s, img, x=x + 0.3, y=card_y + 0.70, w=card_w - 0.6, h=2.30)
        # Body
        text_box(s, x=x + 0.2, y=card_y + 3.10, w=card_w - 0.4, h=1.40,
                 text=body, size=14, color=DEEP, italic=True,
                 align=PP_ALIGN.CENTER, line_spacing=1.30)

    # Bottom-line — single teal callout
    teal_callout(s, 0.55, 6.75, 12.3, 0.65,
                 "Альтернативные ручки: top-p (nucleus) — отрезает редкие токены по Σ; top-k — по числу кандидатов. Достаточно T для start.",
                 size=15)
    speaker_notes(s, load_notes("s19"))


def build_s20(p):
    """4 API knobs — 5×5 matrix."""
    s = blank(p)
    slide_title(s, "4 ручки API под задачу: temperature, top_p, max_tokens, system prompt", size=24)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Подобрать параметры под сценарий обоснованно",
             size=15, italic=True, color=MID)

    # Table
    ocean_box(s, 0.55, 2.05, 12.3, 4.5)
    # Headers row
    headers = ["Сценарий", "temperature", "top_p", "max_tokens", "system_prompt"]
    col_widths = [3.0, 1.7, 1.3, 1.7, 4.20]
    col_xs = [0.7]
    for w in col_widths[:-1]:
        col_xs.append(col_xs[-1] + w)

    # Header row
    header_y = 2.20
    header_h = 0.55
    for i, h in enumerate(headers):
        # Header background
        filled_rect(s, col_xs[i], header_y, col_widths[i], header_h, MID, radius=False)
        text_box(s, x=col_xs[i] + 0.05, y=header_y, w=col_widths[i] - 0.1, h=header_h,
                 text=h, size=13, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Data rows — T-coded colors
    rows = [
        ("Классификация / точное извлечение", "0", "—", "50–200", "Минимальный, со схемой выхода", GOLD),
        ("Кодогенерация", "0.2–0.3", "0.9", "1000+", "Роль + контекст репозитория", LIGHT),
        ("Чат-объяснение пользователю", "0.7", "0.9", "500–1000", "Роль + описание аудитории", LIGHT),
        ("Творческое письмо", "0.9–1.2", "0.95", "2000+", "Роль + описание стиля", TEAL),
    ]
    row_h = 0.85
    for r_i, row in enumerate(rows):
        scenario, t_val, p_val, mt, sp, accent = row
        ry = header_y + header_h + r_i * row_h
        # Alternating fill
        fill_col = SURFACE if r_i % 2 == 0 else WHITE
        for i, w in enumerate(col_widths):
            filled_rect(s, col_xs[i], ry, w, row_h, fill_col, stroke=LIGHT, stroke_pt=0.6)
        # Cell content
        values = [scenario, t_val, p_val, mt, sp]
        for i, v in enumerate(values):
            is_t_col = (i == 1)
            text_color = accent if is_t_col else DEEP
            bold = is_t_col
            size = 13 if i == 0 else (15 if is_t_col else 12)
            align = PP_ALIGN.LEFT if i == 0 or i == 4 else PP_ALIGN.CENTER
            text_box(s, x=col_xs[i] + 0.10, y=ry, w=col_widths[i] - 0.2, h=row_h,
                     text=v, size=size, bold=bold, color=text_color,
                     align=align, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.18)

    # Footer
    text_box(s, x=0.55, y=6.75, w=12.3, h=0.5,
             text="T = 0 практически детерминирует выбор; в production возможна микро-вариативность из-за batching — для большинства задач игнорируема.",
             size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER, line_spacing=1.30)
    speaker_notes(s, load_notes("s20"))


def build_s21(p):
    """Autoregressive loop — 5 steps cycle."""
    s = blank(p)
    slide_title(s, "Цикл: предсказали токен → добавили в контекст → предсказываем следующий", size=24)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Авторегрессионная генерация — длинный ответ из stateless-вызовов",
             size=15, italic=True, color=MID)

    # 5 steps in horizontal flow with return arrow
    step_y = 2.4
    step_h = 2.6
    n_steps = 5
    total_w = 12.3
    gap = 0.15
    step_w = (total_w - gap * (n_steps - 1)) / n_steps
    start_x = 0.55
    steps = [
        ("(1) Текущий\nконтекст",
         "system + история\n+ запрос + уже\nсгенерированное",
         False),
        ("(2) Прямой\nпроход",
         "токенизация →\nэмбеддинг →\nattention",
         True),  # gold
        ("(3) Распределение",
         "вероятности\nна ~200k токенов\nсловаря",
         False),
        ("(4) Сэмплинг",
         "один токен\nпо правилу\nT / top-p / top-k",
         False),
        ("(5) Новый токен\nдобавлен в контекст",
         "...и цикл\nпродолжается",
         False),
    ]
    for i, (head, body, is_gold) in enumerate(steps):
        x = start_x + i * (step_w + gap)
        if is_gold:
            ocean_box(s, x, step_y, step_w, step_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.5)
        else:
            ocean_box(s, x, step_y, step_w, step_h)
        # Step head
        text_box(s, x=x + 0.1, y=step_y + 0.20, w=step_w - 0.2, h=1.05,
                 text=head, size=17, bold=True,
                 color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.20)
        # Body
        text_box(s, x=x + 0.1, y=step_y + 1.30, w=step_w - 0.2, h=1.30,
                 text=body, size=14, italic=True, color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.30)
        # Right arrow between steps
        if i < n_steps - 1:
            right_arrow(s, x + step_w + 0.01, step_y + step_h / 2 - 0.15, w=gap - 0.03, h=0.35, fill=MID)

    # Return arrow at bottom (curved feel via labelled box)
    return_y = step_y + step_h + 0.3
    filled_rect(s, 1.0, return_y, 11.4, 0.60, SURFACE, stroke=LIGHT, stroke_pt=1.5, radius=True, radius_adj=0.3)
    text_box(s, x=1.0, y=return_y + 0.10, w=11.4, h=0.45,
             text="↺ возврат к шагу (1) — пока не дойдём до токена «конец ответа» ИЛИ до max_tokens",
             size=16, italic=True, bold=True, color=MID,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Caption
    text_box(s, x=0.55, y=6.65, w=12.3, h=0.55,
             text="Каждый шаг — stateless. «Память» одного ответа несёт сам контекст, не модель.",
             size=14, italic=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.3)
    speaker_notes(s, load_notes("s21"))


def build_s22(p):
    """Local vs cloud — 2 columns parallel."""
    s = blank(p)
    slide_title(s, "Inference loop одинаков локально и в облаке — но размер модели определяет качество", size=24)
    text_box(s, x=0.55, y=1.50, w=12.3, h=0.4,
             text="Архитектурно — тот же конвейер. Различия — в размере и среде.",
             size=16, italic=True, color=MID)

    # Two columns
    col_w = 6.0
    col_h = 4.50
    col_y = 2.10
    left_x = 0.55
    right_x = 6.85

    # Local
    ocean_box(s, left_x, col_y, col_w, col_h)
    text_box(s, x=left_x + 0.3, y=col_y + 0.15, w=col_w - 0.6, h=0.5,
             text="Local (Ollama, llama.cpp, LM Studio)",
             size=18, bold=True, color=MID)
    text_box(s, x=left_x + 0.3, y=col_y + 0.70, w=col_w - 0.6, h=0.45,
             text="Размер: 1–13B параметров",
             size=15, bold=True, color=DEEP)
    text_box(s, x=left_x + 0.3, y=col_y + 1.15, w=col_w - 0.6, h=1.0,
             text="• Qwen 2.5 1.5B  · Llama 3.2 1B\n• Llama 3.1 8B  · Mistral 7B",
             size=14, color=DEEP, line_spacing=1.40, font=FONT_MONO)
    local_pts = [
        ("Приватность", "запросы не уходят провайдеру", TEAL),
        ("Скорость", "медленнее на consumer hardware", LIGHT),
        ("Контекст", "ограниченное окно", LIGHT),
        ("Цена", "0 за токен (своё железо)", GOLD),
    ]
    for i, (k, v, col) in enumerate(local_pts):
        py = col_y + 2.40 + i * 0.50
        filled_rect(s, left_x + 0.3, py + 0.14, 0.20, 0.20, col, radius=True, radius_adj=0.5)
        text_box(s, x=left_x + 0.62, y=py, w=col_w * 0.35, h=0.4,
                 text=k, size=14, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=left_x + col_w * 0.45, y=py, w=col_w * 0.55, h=0.4,
                 text=v, size=13, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    # Cloud
    ocean_box(s, right_x, col_y, col_w, col_h)
    text_box(s, x=right_x + 0.3, y=col_y + 0.15, w=col_w - 0.6, h=0.5,
             text="Cloud (OpenAI, Anthropic, Yandex, Сбер)",
             size=18, bold=True, color=MID)
    text_box(s, x=right_x + 0.3, y=col_y + 0.70, w=col_w - 0.6, h=0.45,
             text="Размер: 200B+ параметров",
             size=15, bold=True, color=DEEP)
    text_box(s, x=right_x + 0.3, y=col_y + 1.15, w=col_w - 0.6, h=1.0,
             text="• GPT-5, Claude 4.7\n• YandexGPT, GigaChat\n• Gemini",
             size=14, color=DEEP, line_spacing=1.40, font=FONT_MONO)
    cloud_pts = [
        ("Качество", "лучше на сложных задачах", TEAL),
        ("Задержка", "200–500 мс", LIGHT),
        ("Контекст", "до 1M токенов", GOLD),
        ("Цена", "оплата за токены, RU ≈ 2× EN", LIGHT),
    ]
    for i, (k, v, col) in enumerate(cloud_pts):
        py = col_y + 2.40 + i * 0.50
        filled_rect(s, right_x + 0.3, py + 0.14, 0.20, 0.20, col, radius=True, radius_adj=0.5)
        text_box(s, x=right_x + 0.62, y=py, w=col_w * 0.35, h=0.4,
                 text=k, size=14, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=right_x + col_w * 0.45, y=py, w=col_w * 0.55, h=0.4,
                 text=v, size=13, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    speaker_notes(s, load_notes("s22"))


def build_s23(p):
    """Pipeline recap — 4 stages horizontal flow."""
    s = blank(p)
    slide_title(s, "4 этапа inference сложились в pipeline", size=28)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Тот же чёрный ящик из Лекции 1 §3.2 — теперь распакован",
             size=15, italic=True, color=MID)

    # 4 stages horizontal pipeline
    stage_y = 2.50
    stage_h = 3.1
    n = 4
    total_w = 12.3
    gap = 0.35
    stage_w = (total_w - gap * n) / n  # gap between + final arrow at end
    start_x = 0.55
    stages = [
        ("Токенизация", "Текст → id\nиз словаря (BPE)"),
        ("Эмбеддинг", "id → вектор\nиз обученной таблицы"),
        ("Внимание", "Распределение\nвесов на контекст"),
        ("Сэмплинг", "Распределение →\nодин токен (T / p / k)"),
    ]
    for i, (head, body) in enumerate(stages):
        x = start_x + i * (stage_w + gap)
        ocean_box(s, x, stage_y, stage_w, stage_h)
        # Stage number circle
        filled_rect(s, x + (stage_w - 0.85) / 2, stage_y + 0.30, 0.85, 0.85, MID, radius=True, radius_adj=0.5)
        text_box(s, x=x, y=stage_y + 0.37, w=stage_w, h=0.70,
                 text=str(i + 1), size=28, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Head
        text_box(s, x=x + 0.1, y=stage_y + 1.30, w=stage_w - 0.2, h=0.55,
                 text=head,
                 size=20, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Body
        text_box(s, x=x + 0.1, y=stage_y + 1.95, w=stage_w - 0.2, h=1.0,
                 text=body, size=15, italic=True, color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.30)
        # Arrow between
        if i < n - 1:
            right_arrow(s, x + stage_w + 0.05, stage_y + stage_h / 2 - 0.20, w=gap - 0.10, h=0.40, fill=MID)

    # Final arrow → "следующий токен"
    final_x = start_x + n * (stage_w + gap) - gap + 0.05
    if final_x + 1.0 < 13.0:
        right_arrow(s, final_x, stage_y + stage_h / 2 - 0.20, w=0.8, h=0.40, fill=GOLD)
        text_box(s, x=final_x - 0.4, y=stage_y + stage_h + 0.15, w=1.6, h=0.4,
                 text="следующий токен",
                 size=11, bold=True, color=DEEP, italic=True,
                 align=PP_ALIGN.CENTER)

    # Caption bottom
    text_box(s, x=0.55, y=6.85, w=12.3, h=0.4,
             text="Лекция 1 §3.2 называла этот pipeline «inference моделью» — чёрным ящиком. Теперь он перестал быть чёрным.",
             size=13, italic=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.30)
    speaker_notes(s, load_notes("s23"))


def build_s24(p):
    """3 whys payoff — 3 cards."""
    s = blank(p)
    slide_title(s, "3 промиса Лекции 1 — 3 ответа из Лекции 2", size=28)
    # Gold marker
    filled_rect(s, 0.55, 1.45, 12.3, 0.50, GOLD_TINT, stroke=GOLD, stroke_pt=1.0, radius=True, radius_adj=0.25)
    text_box(s, x=0.55, y=1.50, w=12.3, h=0.40,
             text="Payoff Лекции 1 §5.3 — связь обещаний и механизмов",
             size=16, bold=True, color=DEEP, italic=True,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # 3 boxes vertical
    box_y_start = 2.20
    box_h = 1.65
    box_gap = 0.15
    answers = [
        ("1", "Почему промпт с ролью работает лучше пустого?",
         "На уровне attention role-токены получают высокий вес — модель опирается на них при выборе следующих токенов.",
         GOLD),
        ("2", "Почему AI плохо считает буквы?",
         "Токенизатор объединяет буквы в токены. strawberry — 3 токена, не 10 букв. Модель видит токены, не буквы.",
         MID),
        ("3", "Почему один и тот же запрос даёт разные ответы?",
         "Сэмплинг — стохастический выбор из распределения при T > 0. Каждый запуск может выбрать разный токен.",
         TEAL),
    ]
    for i, (n, q, a, col) in enumerate(answers):
        y = box_y_start + i * (box_h + box_gap)
        ocean_box(s, 0.55, y, 12.3, box_h)
        # Number badge
        filled_rect(s, 0.85, y + 0.35, 0.95, 0.95, col, radius=True, radius_adj=0.5)
        text_box(s, x=0.85, y=y + 0.38, w=0.95, h=0.90,
                 text=n, size=44, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Question
        text_box(s, x=2.05, y=y + 0.20, w=10.0, h=0.55,
                 text=q, size=18, bold=True, color=DEEP)
        # Answer
        text_box(s, x=2.05, y=y + 0.80, w=10.0, h=0.85,
                 text=a, size=15, color=DEEP, italic=True, line_spacing=1.30)

    speaker_notes(s, load_notes("s24"))


def build_s25(p):
    """ML vs LLM decision tree."""
    s = blank(p)
    slide_title(s, "LLM — не всегда правильный инструмент. Дерево решений: когда не LLM", size=24)

    # Root
    root_y = 1.65
    root_w = 5.5
    ocean_box(s, (SLIDE_W_IN - root_w) / 2, root_y, root_w, 0.75,
              fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    text_box(s, x=(SLIDE_W_IN - root_w) / 2, y=root_y + 0.10, w=root_w, h=0.55,
             text="Когда LLM — не правильный инструмент?",
             size=18, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # 3 branch arrows down (visual)
    # Branches
    branch_y = 3.0
    branch_h = 2.85
    branch_w = 3.95
    gap = 0.20
    start_x = 0.55
    branches = [
        ("cpu", "Фиксированные классы",
         "Классификация на маленьком наборе категорий (5–20)?",
         "→ Классический ML\nлог. регрессия, XGBoost,\nLightGBM, дообученный BERT"),
        ("file-text", "Интерпретируемость",
         "Нужна интерпретируемость\n(финансы, медицина, страхование)?",
         "→ Прозрачные методы\nлог. регрессия + важность,\nдеревья решений, правила"),
        ("gauge", "Скорость отклика",
         "Время отклика < 100 мс критично\n(антифрод, устройство пользователя)?",
         "→ Специализированная\nмаленькая модель\n(не LLM ≥200 мс)"),
    ]
    for i, (icon, head, cond, action) in enumerate(branches):
        x = start_x + i * (branch_w + gap)
        # Connector line from root
        filled_rect(s, x + branch_w/2 - 0.02, root_y + 0.75, 0.04, branch_y - root_y - 0.75, LIGHT)
        ocean_box(s, x, branch_y, branch_w, branch_h)
        # Icon
        icon_path = ASSETS / f"icons/{icon}.png"
        if icon_path.exists():
            add_image(s, icon_path, x=x + 0.25, y=branch_y + 0.20, w=0.8, h=0.8)
        # Head
        text_box(s, x=x + 1.15, y=branch_y + 0.30, w=branch_w - 1.30, h=0.5,
                 text=head, size=17, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
        # Condition
        text_box(s, x=x + 0.25, y=branch_y + 1.20, w=branch_w - 0.5, h=0.95,
                 text=cond, size=14, color=DEEP, italic=True, line_spacing=1.30)
        # Action
        text_box(s, x=x + 0.25, y=branch_y + 2.10, w=branch_w - 0.5, h=0.80,
                 text=action, size=14, bold=True, color=DEEP, line_spacing=1.30)

    # Else → LLM (bottom green/teal pill)
    else_y = 6.30
    else_w = 9.0
    else_x = (SLIDE_W_IN - else_w) / 2
    filled_rect(s, else_x, else_y, else_w, 0.85, TEAL_TINT, stroke=TEAL, stroke_pt=2.0, radius=True, radius_adj=0.4)
    text_box(s, x=else_x, y=else_y + 0.15, w=else_w, h=0.55,
             text="Иначе — LLM подходит (chat, RAG, generation, многошаговое рассуждение)",
             size=17, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    speaker_notes(s, load_notes("s25"))


def build_s26(p):
    """Attention vs causality — 2 columns Human vs AI."""
    s = blank(p)
    slide_title(s, "Attention статистически смотрит на токены — не понимает причинности", size=24)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="AI считает корреляции в данных, не строит каузальный граф",
             size=16, italic=True, color=MID)

    # 2 columns
    col_w = 6.0
    col_h = 4.85
    col_y = 2.05
    left_x = 0.55
    right_x = 6.85

    # Human
    ocean_box(s, left_x, col_y, col_w, col_h)
    # Icon
    add_image(s, ASSETS / "icons/users.png", x=left_x + 0.3, y=col_y + 0.25, w=0.9, h=0.9)
    text_box(s, x=left_x + 1.3, y=col_y + 0.25, w=col_w - 1.5, h=0.9,
             text="Человек", size=24, bold=True, color=DEEP,
             anchor=MSO_ANCHOR.MIDDLE)

    text_box(s, x=left_x + 0.3, y=col_y + 1.40, w=col_w - 0.6, h=0.65,
             text='«X произошло, потому что Y»',
             size=18, bold=True, italic=True, color=MID,
             font=FONT_MONO, line_spacing=1.25)
    text_box(s, x=left_x + 0.3, y=col_y + 2.20, w=col_w - 0.6, h=0.5,
             text="Модель причинности — строит механизмы.",
             size=16, italic=True, color=DEEP)

    text_box(s, x=left_x + 0.3, y=col_y + 3.10, w=col_w - 0.6, h=1.55,
             text="Опирается на физическую интуицию, доменные знания, знание механизмов мира.",
             size=15, italic=True, color=DEEP, line_spacing=1.30)

    # AI
    ocean_box(s, right_x, col_y, col_w, col_h)
    add_image(s, ASSETS / "icons/brain.png", x=right_x + 0.3, y=col_y + 0.25, w=0.9, h=0.9)
    text_box(s, x=right_x + 1.3, y=col_y + 0.25, w=col_w - 1.5, h=0.9,
             text="AI (через attention)", size=24, bold=True, color=DEEP,
             anchor=MSO_ANCHOR.MIDDLE)

    text_box(s, x=right_x + 0.3, y=col_y + 1.40, w=col_w - 0.6, h=0.65,
             text='«X следует за Y в данных»',
             size=18, bold=True, italic=True, color=MID,
             font=FONT_MONO, line_spacing=1.25)
    text_box(s, x=right_x + 0.3, y=col_y + 2.20, w=col_w - 0.6, h=0.5,
             text="Статистическая корреляция, не причинность.",
             size=16, italic=True, color=DEEP)

    text_box(s, x=right_x + 0.3, y=col_y + 3.10, w=col_w - 0.6, h=1.55,
             text="Замечает паттерн «X и Y часто соседствуют» в обучающих данных — корреляция, не каузальный граф.",
             size=15, italic=True, color=DEEP, line_spacing=1.30)

    # Gold callout bottom — emphasis on insight
    gold_callout(s, 0.55, 7.05, 12.3, 0.40,
                 "Инженерный вывод: для причинных выводов привлекайте domain-эксперта или causal-методы.",
                 size=14)
    speaker_notes(s, load_notes("s26"))


def build_s27(p):
    """Homework — 3 steps + bonus."""
    s = blank(p)
    slide_title(s, "Принесите: 1 запрос × 3 температуры × 3 запуска × анализ", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="ДЗ к Семинару 2 — apply температуры на своей задаче",
             size=16, italic=True, color=MID)

    # 3 step cards
    card_y = 2.05
    card_h = 3.55
    card_w = 3.95
    gap = 0.20
    start_x = 0.55
    cards = [
        ("target", "Шаг 1",
         "Возьмите типовую задачу из своей предметной области.",
         "Конкретный воспроизводимый запрос (не «помоги думать»)."),
        ("sliders-horizontal", "Шаг 2",
         "Запустите в playground на 3 температурах.",
         "T = 0  ·  T = 0.7  ·  T = 1.5\nпо 3 запуска каждой\n(для оценки variance)"),
        ("file-text", "Шаг 3",
         "Принесите одностраничный разбор (1 A4).",
         "Что изменилось / осталось / какую T для production."),
    ]
    for i, (icon, head, body, detail) in enumerate(cards):
        x = start_x + i * (card_w + gap)
        ocean_box(s, x, card_y, card_w, card_h)
        # Icon
        icon_path = ASSETS / f"icons/{icon}.png"
        if icon_path.exists():
            add_image(s, icon_path, x=x + (card_w - 1.1) / 2, y=card_y + 0.30, w=1.1, h=1.1)
        # Head
        text_box(s, x=x + 0.2, y=card_y + 1.55, w=card_w - 0.4, h=0.5,
                 text=head, size=20, bold=True, color=MID,
                 align=PP_ALIGN.CENTER)
        # Body
        text_box(s, x=x + 0.25, y=card_y + 2.10, w=card_w - 0.5, h=0.75,
                 text=body, size=15, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.30)
        # Detail
        text_box(s, x=x + 0.25, y=card_y + 2.85, w=card_w - 0.5, h=0.65,
                 text=detail, size=13, italic=True, color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.35)

    # Playground info — full-width box
    pg_y = 5.85
    ocean_box(s, 0.55, pg_y, 8.4, 1.40, fill=SURFACE, stroke=LIGHT)
    text_box(s, x=0.75, y=pg_y + 0.14, w=8.0, h=0.40,
             text="Playground:  Hugging Face Inference Playground",
             size=15, bold=True, color=MID)
    text_box(s, x=0.75, y=pg_y + 0.58, w=8.0, h=0.40,
             text="Модель: Meta-Llama-3-8B-Instruct (apples-to-apples)",
             size=13, color=DEEP, italic=False)
    text_box(s, x=0.75, y=pg_y + 1.00, w=8.0, h=0.35,
             text="Fallback: Together.ai / Ollama локально   ·   НЕ подойдут: ChatGPT Free, Claude.ai",
             size=12, italic=True, color=LIGHT)

    # Bonus
    filled_rect(s, 9.15, pg_y, 3.70, 1.40, GOLD_TINT, stroke=GOLD, stroke_pt=2.0, radius=True, radius_adj=0.12)
    text_box(s, x=9.30, y=pg_y + 0.12, w=3.5, h=0.40,
             text="БОНУС",
             size=16, bold=True, color=DEEP)
    text_box(s, x=9.30, y=pg_y + 0.54, w=3.5, h=0.80,
             text='«Сколько р в \"строгая регуляризация\"» × 3 модели. Объяснить через токенизацию.',
             size=12, italic=True, color=DEEP, line_spacing=1.30)

    speaker_notes(s, load_notes("s27"))


def build_s28(p):
    """Bridge to Lec 3 + Q&A — 4 concepts preview."""
    s = blank(p)
    slide_title(s, "Лекция 3:  «Агенты, RAG, API — как AI выходит за пределы чата»", size=24)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Все 4 концепции надстраиваются над одним проходом inference",
             size=16, italic=True, color=MID)

    # 2×2 grid
    grid_x = 0.55
    grid_y = 2.05
    cell_w = 6.0
    cell_h = 2.20
    gap = 0.20

    concepts = [
        # (icon, title, sub, body, accent_gold)
        ("search-check", "RAG",
         "Retrieval-Augmented Generation",
         "близость эмбеддингов + LLM → ответ из вашей базы",
         True),
        ("workflow", "Инструменты / Вызов функций",
         "структурированный JSON",
         "LLM генерирует вызов → выполняет внешняя система → результат возвращается",
         False),
        ("arrow-right-left", "MCP",
         "Model Context Protocol",
         "Открытый стандарт подключения инструментов (Anthropic, 2024)",
         False),
        ("repeat-2", "Цикл агента",
         "действуй → наблюдай → корректируй",
         "Модель решает действие, видит результат, корректирует план",
         False),
    ]
    for i, (icon, title, sub, body, is_gold) in enumerate(concepts):
        col = i % 2
        row = i // 2
        x = grid_x + col * (cell_w + gap)
        y = grid_y + row * (cell_h + gap)
        if is_gold:
            ocean_box(s, x, y, cell_w, cell_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
        else:
            ocean_box(s, x, y, cell_w, cell_h)
        # Icon
        icon_path = ASSETS / f"icons/{icon}.png"
        if icon_path.exists():
            add_image(s, icon_path, x=x + 0.25, y=y + 0.30, w=0.95, h=0.95)
        # Title
        text_box(s, x=x + 1.35, y=y + 0.20, w=cell_w - 1.50, h=0.5,
                 text=title, size=22, bold=True, color=DEEP)
        # Subtitle
        text_box(s, x=x + 1.35, y=y + 0.75, w=cell_w - 1.50, h=0.4,
                 text=sub, size=14, italic=True, color=MID)
        # Body
        text_box(s, x=x + 0.30, y=y + 1.30, w=cell_w - 0.50, h=0.85,
                 text=body, size=14, color=DEEP, line_spacing=1.30)

    # Q&A block bottom
    qa_y = 6.75
    filled_rect(s, 0.55, qa_y, 12.3, 0.65, GOLD_TINT, stroke=GOLD, stroke_pt=2.0, radius=True, radius_adj=0.30)
    text_box(s, x=0.85, y=qa_y + 0.05, w=12.0, h=0.30,
             text="Q&A",
             size=18, bold=True, color=DEEP)
    text_box(s, x=0.85, y=qa_y + 0.32, w=12.0, h=0.30,
             text="До 5 минут на вопросы в зале. Дополнительные — на Семинар 2 или e-mail.",
             size=14, color=DEEP, italic=True)

    speaker_notes(s, load_notes("s28"))


# ============================================================
# Build all 28 slides
# ============================================================
def main():
    p = setup_pres()
    builders = [
        build_s01, build_s02, build_s03, build_s04, build_s05, build_s06,
        build_s07, build_s08, build_s09, build_s10, build_s11, build_s12,
        build_s13, build_s14, build_s15, build_s16, build_s17, build_s18,
        build_s19, build_s20, build_s21, build_s22, build_s23, build_s24,
        build_s25, build_s26, build_s27, build_s28,
    ]
    print(f"Building {len(builders)} slides…")
    for i, fn in enumerate(builders, 1):
        try:
            fn(p)
            print(f"  s{i:02d} OK")
        except Exception as e:
            print(f"  s{i:02d} FAIL: {type(e).__name__}: {e}")
            raise
    OUT.parent.mkdir(parents=True, exist_ok=True)
    p.save(str(OUT))
    print(f"\nSaved: {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
