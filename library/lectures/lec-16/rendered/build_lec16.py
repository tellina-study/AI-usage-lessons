"""
Full 43-slide build of Лекции 16 «AI в нефтегазовой отрасли и добыче ресурсов».

Source-of-truth: deck.yaml v1 + chapter v2.1 multi-part (~32k слов) + slides/*.md.

Issue #144 · downstream от chapter (book-first).

Palette LOCKED v3: Ocean Gradient (#21295C / #065A82 / #1C7293) + Teal (#028090)
secondary + Gold (#F0AB00) ≥1×/slide.
Visual motif: «Ocean rounded box» (radius 12, surface #F4F7FA, stroke #1C7293 1.5pt).
Canvas: 13.333" × 7.5" (16:9). Pacing per deck.yaml ≈ 75 мин.

Lec-N-1 паттерн compliance: match lec-13/14 (cover + lecture-map + 7 section dividers +
keystone + выделенный Q&A; top progress bar только на dividers + cover).

Build via:
  python3 build_lec16.py            # generates lec-16.pptx (notes = file refs)
  python3 inject_notes.py           # injects FULL speaker notes from slides/*.md
"""
import re
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt
from PIL import Image
from lxml import etree

# === Palette (LOCKED v3) ===
DEEP    = RGBColor(0x21, 0x29, 0x5C)
MID     = RGBColor(0x06, 0x5A, 0x82)
LIGHT   = RGBColor(0x1C, 0x72, 0x93)
TEAL    = RGBColor(0x02, 0x80, 0x90)
SURFACE = RGBColor(0xF4, 0xF7, 0xFA)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
GOLD    = RGBColor(0xF0, 0xAB, 0x00)
SLATE   = RGBColor(0x6B, 0x76, 0x85)
GOLD_TINT = RGBColor(0xFE, 0xF5, 0xE0)
TEAL_TINT = RGBColor(0xE6, 0xF2, 0xF4)
SOFT_GREY = RGBColor(0xE5, 0xEA, 0xF0)
DARK_GREY = RGBColor(0x4A, 0x55, 0x6B)
RED_WARN = RGBColor(0xC0, 0x39, 0x2B)
ROADMAP = RGBColor(0xD9, 0xE2, 0xEC)

SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5
ROOT = Path(__file__).resolve().parent
ASSETS = ROOT.parent / "assets"
OUT = ROOT / "lec-16.pptx"
FONT_HEAD = "Arial"
FONT_BODY = "Arial"


def disable_shadow(shp):
    sppr = shp._element.spPr
    for el in sppr.findall("{http://schemas.openxmlformats.org/drawingml/2006/main}effectLst"):
        sppr.remove(el)
    etree.SubElement(sppr, "{http://schemas.openxmlformats.org/drawingml/2006/main}effectLst")


def text_box(slide, x, y, w, h, text, *, size=16, bold=False, italic=False,
             color=DEEP, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             font=FONT_BODY, line_spacing=1.15):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    try: p.line_spacing = line_spacing
    except: pass
    r = p.add_run()
    r.text = text
    r.font.name = font; r.font.size = Pt(size)
    r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color
    return tb


def multiline_box(slide, x, y, w, h, lines, *, size=14, bold=False, color=DEEP,
                  align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, font=FONT_BODY,
                  line_spacing=1.25):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for i, line in enumerate(lines):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.alignment = align
        try: p.line_spacing = line_spacing
        except: pass
        if isinstance(line, tuple):
            txt, opts = line
        else:
            txt, opts = line, {}
        r = p.add_run()
        r.text = txt
        r.font.name = opts.get("font", font)
        r.font.size = Pt(opts.get("size", size))
        r.font.bold = opts.get("bold", bold)
        r.font.italic = opts.get("italic", False)
        r.font.color.rgb = opts.get("color", color)
    return tb


def rounded_box(slide, x, y, w, h, *, fill=SURFACE, stroke=LIGHT, stroke_w=1.5):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                  Inches(x), Inches(y), Inches(w), Inches(h))
    shp.adjustments[0] = 0.08
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.color.rgb = stroke
    shp.line.width = Pt(stroke_w)
    disable_shadow(shp)
    return shp


def rectangle(slide, x, y, w, h, *, fill=MID, stroke=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                  Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if stroke:
        shp.line.color.rgb = stroke
    else:
        shp.line.fill.background()
    disable_shadow(shp)
    return shp


def circle(slide, x, y, w, h, *, fill=MID, stroke=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.OVAL,
                                  Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if stroke:
        shp.line.color.rgb = stroke
    else:
        shp.line.fill.background()
    disable_shadow(shp)
    return shp


def add_image_aspect(slide, path, x, y, w, h):
    """Add picture preserving aspect ratio (centered in box)."""
    p = Path(path)
    if not p.exists():
        rectangle(slide, x, y, w, h, fill=SOFT_GREY)
        text_box(slide, x, y+h/2-0.3, w, 0.6, f"[нет: {p.name}]",
                 size=10, color=SLATE, align=PP_ALIGN.CENTER)
        return None
    try:
        with Image.open(p) as img:
            iw, ih = img.size
        img_ratio = iw / ih
        box_ratio = w / h
        if img_ratio > box_ratio:
            new_w = w
            new_h = w / img_ratio
            cx = x
            cy = y + (h - new_h) / 2
        else:
            new_h = h
            new_w = h * img_ratio
            cx = x + (w - new_w) / 2
            cy = y
        return slide.shapes.add_picture(str(p), Inches(cx), Inches(cy),
                                         width=Inches(new_w), height=Inches(new_h))
    except Exception as e:
        print(f"Image fail {path}: {e}")
        rectangle(slide, x, y, w, h, fill=SOFT_GREY)
        return None


def set_slide_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def blank(p):
    return p.slides.add_slide(p.slide_layouts[6])


def setup_pres():
    p = Presentation()
    p.slide_width = Inches(SLIDE_W_IN)
    p.slide_height = Inches(SLIDE_H_IN)
    return p


def add_notes(slide, text):
    notes_tf = slide.notes_slide.notes_text_frame
    notes_tf.text = text


# Roadmap sections for Lec-16: 7 разделов
SECTIONS = ["Keystone", "Q1 Mature", "Q3 Frontier", "Q2 Methane", "Q4 Transition", "Россия", "Сквозные"]


def roadmap_bar(slide, current_section):
    """7-section roadmap bar at top of section dividers + cover."""
    bar_y = 0.20
    bar_h = 0.32
    total_w = 12.33
    seg_w = total_w / 7
    for i, name in enumerate(SECTIONS):
        x = 0.5 + i * seg_w
        is_active = (i == current_section)
        rectangle(slide, x, bar_y, seg_w - 0.05, bar_h,
                  fill=GOLD if is_active else ROADMAP)
        text_box(slide, x, bar_y + 0.04, seg_w - 0.05, bar_h - 0.04,
                 f"{i+1}. {name}", size=10, bold=is_active,
                 color=DEEP if is_active else SLATE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def footer(slide, text, *, y=7.10):
    text_box(slide, 0.5, y, 12.33, 0.35, text,
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.LEFT)


def attribution(slide, text, *, x=0.5, y=6.95, w=12.33):
    text_box(slide, x, y, w, 0.3, text,
             size=10, italic=True, color=SLATE, align=PP_ALIGN.LEFT)


def gold_callout(slide, x, y, w, h, text, *, size=14):
    rounded_box(slide, x, y, w, h, fill=GOLD_TINT, stroke=GOLD, stroke_w=1.5)
    text_box(slide, x+0.2, y+0.08, w-0.4, h-0.15, text,
             size=size, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.LEFT, line_spacing=1.25)


def section_divider(p, q_label, q_title, mood_line, tag_text, section_idx, large_size=160,
                    label_color=GOLD):
    """Section divider with large quadrant label + mood + tag."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    roadmap_bar(slide, current_section=section_idx)
    # Decorative large Q-label (centered in upper area only)
    text_box(slide, 0.5, 1.0, 5.5, 3.6, q_label,
             size=large_size, bold=True, color=label_color, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)
    # Subtitle BELOW Q-label (clear separation)
    text_box(slide, 0.5, 4.85, 5.5, 0.55, q_title,
             size=22, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    # Mood line
    multiline_box(slide, 6.2, 1.5, 6.6, 4.0, [
        (mood_line, {"size": 20, "bold": True, "color": DEEP}),
    ], line_spacing=1.3)
    # Bottom tag (gold tint)
    gold_callout(slide, 0.5, 6.0, 12.33, 0.85, tag_text, size=14)
    return slide


# ====================================================================
# SECTION 0: Введение + keystone (s01-s05)
# ====================================================================

def s01_hero_permian(p):
    """s01 — hero hook: Permian VIIRS satellite. Hero ≥40% area."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    img = ASSETS / "screenshots" / "s01-permian-viirs.jpg"
    add_image_aspect(slide, img, 0.5, 0.4, 7.5, 5.5)
    attribution(slide, "NASA Earth Observatory · VIIRS day-night band · NOAA · 2024",
                x=0.5, y=5.95, w=7.5)
    multiline_box(slide, 8.3, 0.6, 4.6, 5.4, [
        ("2 593", {"size": 72, "bold": True, "color": GOLD}),
        ("факельных шлейфа", {"size": 18, "bold": True, "color": DEEP}),
        ("Пермский бассейн, 2024", {"size": 14, "italic": True, "color": LIGHT}),
        ("", {"size": 10}),
        ("Пик: ~34 000 т/ч метана", {"size": 14, "bold": True, "color": DEEP}),
        ("для всего бассейна", {"size": 12, "color": SLATE}),
        ("", {"size": 10}),
        ("Не аварии — нормальный", {"size": 13, "color": DEEP}),
        ("operational режим.", {"size": 13, "color": DEEP}),
        ("Добыча идёт быстрее,", {"size": 13, "color": DEEP}),
        ("чем строится газовая", {"size": 13, "color": DEEP}),
        ("инфраструктура.", {"size": 13, "color": DEEP}),
    ], line_spacing=1.1)
    gold_callout(slide, 0.5, 6.3, 12.33, 0.8,
                 "AI в нефтегазе — не «улучшалка на 5%», а способ закрыть конкретные провалы. И закрывает либо громко, либо публично проваливается.",
                 size=14)
    add_notes(slide, "См. slides/s01-hook-permian-viirs.md speaker notes.")


def s02_cover(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    roadmap_bar(slide, current_section=-1)
    text_box(slide, 0.5, 1.2, 4.0, 4.5, "16",
             size=240, bold=True, color=ROADMAP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)
    multiline_box(slide, 4.5, 1.5, 8.3, 2.6, [
        ("Лекция 16", {"size": 22, "bold": True, "color": LIGHT}),
        ("AI в нефтегазовой отрасли", {"size": 34, "bold": True, "color": DEEP}),
        ("и добыче ресурсов", {"size": 34, "bold": True, "color": DEEP}),
    ], line_spacing=1.05)
    text_box(slide, 4.5, 4.3, 8.3, 0.5,
             "Шесть разделов через матрицу данные × физика.",
             size=18, italic=True, color=TEAL)
    rounded_box(slide, 4.5, 4.95, 8.3, 1.85)
    multiline_box(slide, 4.7, 5.05, 8.0, 1.7, [
        ("Главный вопрос:", {"size": 12, "bold": True, "color": MID}),
        ("В каком квадранте матрицы «данные × физика» AI",
         {"size": 13, "color": DEEP}),
        ("становится мультипликатором классических методов,",
         {"size": 13, "color": DEEP}),
        ("а где он либо необходим, либо опасен — на материале",
         {"size": 13, "color": DEEP}),
        ("10 documented провалов индустрии 2014–2026?",
         {"size": 13, "bold": True, "color": DEEP}),
    ], line_spacing=1.15)
    footer(slide, "Курс «Применение AI в инженерии» · Студенты-инженеры 3 курса · 2026")
    add_notes(slide, "См. slides/s02-cover.md speaker notes.")


def s03_about(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.8,
             "Курс — про инженерное суждение «когда применять AI, когда отказаться»",
             size=22, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Сегодня — на материале нефтегазовой отрасли.",
             size=14, italic=True, color=LIGHT)
    cards = [
        ("Аудитория", "Студенты-инженеры\n3 курса\n(универсальная,\nне отраслевые\nспециалисты)", LIGHT),
        ("Формат", "42 слайда\n· 10 разобранных\nпровалов\n· 12+ рабочих\nкейсов\n· 7 разделов", MID),
        ("Вы научитесь", "Различать 4 квадранта\nматрицы\n· Критически читать\nвендорские заявления\n· Применять критерии\n«AI не нужен»\n· Альтернативы\nбез AI", TEAL),
    ]
    card_w = 4.0
    gap = 0.15
    x0 = 0.5
    y = 2.0
    for i, (title, body, accent) in enumerate(cards):
        x = x0 + i * (card_w + gap)
        rounded_box(slide, x, y, card_w, 4.6)
        rectangle(slide, x, y, card_w, 0.7, fill=accent)
        text_box(slide, x+0.1, y, card_w-0.2, 0.7, title,
                 size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x+0.2, y+0.9, card_w-0.4, 3.5, body,
                 size=14, color=DEEP, line_spacing=1.35)
    gold_callout(slide, 0.5, 6.85, 12.33, 0.5,
                 "10 разобранных провалов + 12+ рабочих кейсов = инженерный фильтр, не каталог инноваций.",
                 size=13)
    add_notes(slide, "См. slides/s03-about.md speaker notes.")


def s04_lecture_map(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Карта лекции — 7 разделов",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.05, 12.33, 0.4,
             "Не по value chain, а по структуре AI-задачи: данные × физика",
             size=14, italic=True, color=LIGHT)
    sections = [
        ("1", "Keystone", "Матрица", "Данные × физика, 4 квадранта", LIGHT),
        ("2", "Q1 Mature", "3 кейса · 2 провала", "Зрелое производство", MID),
        ("3", "Q3 Frontier", "3 кейса · 2 провала", "Разведка фронтиров", TEAL),
        ("4", "Q2 Methane", "4 системы · 2 провала", "Метановая MRV", GOLD),
        ("5", "Q4 Transition", "2 пилота · 2 провала", "CCS + EGS", LIGHT),
        ("6", "Россия", "3 программы", "Санкции, инсорсинг", MID),
        ("7", "Сквозные риски", "2 провала", "Кибер + кризис 2020", DEEP),
    ]
    card_w = 1.71
    gap = 0.05
    x0 = 0.5
    y = 1.6
    for i, (num, title, dur, desc, accent) in enumerate(sections):
        x = x0 + i * (card_w + gap)
        rounded_box(slide, x, y, card_w, 4.4)
        circle(slide, x + card_w/2 - 0.28, y + 0.15, 0.55, 0.55, fill=accent)
        text_box(slide, x + card_w/2 - 0.28, y + 0.15, 0.55, 0.55, num,
                 size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.1, y + 0.85, card_w - 0.2, 0.5, title,
                 size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.1, y + 1.35, card_w - 0.2, 0.4, dur,
                 size=9, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
        text_box(slide, x + 0.1, y + 1.85, card_w - 0.2, 2.5, desc,
                 size=11, color=DEEP, line_spacing=1.3, align=PP_ALIGN.CENTER)
    gold_callout(slide, 0.5, 6.2, 12.33, 0.85,
                 "Quick glossary: MRV = выявление-учёт-проверка · OGI = оптическая газовая визуализация · CCS = улавливание и хранение углерода · EGS = улучшенные геотермальные системы · SIS = приборная система безопасности",
                 size=10)
    add_notes(slide, "См. slides/s04-lecture-map.md speaker notes.")


def s05_keystone_matrix(p):
    """s05 — KEYSTONE: 2x2 matrix данные × физика."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.3, 12.33, 0.7,
             "Когда AI работает в нефтегазе? Матрица данные × физика",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 0.95, 12.33, 0.4,
             "От разведки фронтиров до спутникового метана — AI имеет 4 разных profile",
             size=13, italic=True, color=LIGHT)
    # Y-axis labels (placed in column на левой стороне)
    text_box(slide, 0.1, 1.7, 1.5, 0.4, "Высокая ↑",
             size=11, bold=True, color=MID, align=PP_ALIGN.CENTER)
    text_box(slide, 0.1, 3.7, 1.5, 0.5, "Данные",
             size=14, bold=True, color=MID, align=PP_ALIGN.CENTER)
    text_box(slide, 0.1, 5.55, 1.5, 0.4, "↓ Низкая",
             size=11, bold=True, color=MID, align=PP_ALIGN.CENTER)
    # X-axis labels
    text_box(slide, 2.0, 6.4, 4.0, 0.4, "← Низкая",
             size=11, bold=True, color=MID, align=PP_ALIGN.CENTER)
    text_box(slide, 5.5, 6.4, 2.5, 0.5, "Физика",
             size=14, bold=True, color=MID, align=PP_ALIGN.CENTER)
    text_box(slide, 7.5, 6.4, 4.0, 0.4, "Высокая →",
             size=11, bold=True, color=MID, align=PP_ALIGN.CENTER)
    # Matrix 2x2
    quad_x0 = 1.7
    quad_y0 = 1.55
    quad_w = 5.0
    quad_h = 2.25
    quads = [
        (0, 0, TEAL_TINT, "Q2 — Метановая MRV", "AI необходим\nMethaneSAT / Carbon Mapper / GHGSat", TEAL),
        (1, 0, SURFACE, "Q1 — Зрелое производство", "AI как мультипликатор\nAmbyint +15% на 200 скважинах", MID),
        (0, 1, GOLD_TINT, "Q4 — Энергопереход", "AI и физика буксуют вместе\nNorthern Lights / Fervo", GOLD),
        (1, 1, SURFACE, "Q3 — Разведка фронтиров", "Physics-first, AI как дополнение\nAramco METABRAIN / Eni HPC6", LIGHT),
    ]
    for col, row, fill, title, body, accent in quads:
        x = quad_x0 + col * (quad_w + 0.2)
        y = quad_y0 + row * (quad_h + 0.15)
        rounded_box(slide, x, y, quad_w, quad_h, fill=fill, stroke=accent, stroke_w=2.5)
        text_box(slide, x + 0.2, y + 0.1, quad_w - 0.4, 0.5, title,
                 size=15, bold=True, color=DEEP)
        text_box(slide, x + 0.2, y + 0.7, quad_w - 0.4, quad_h - 0.85, body,
                 size=12, color=DEEP, line_spacing=1.35)
    gold_callout(slide, 0.5, 7.0, 12.33, 0.45,
                 "За каждым AI-внедрением — alternative tool: физический симулятор, OGI-камера, классическая интерпретация.",
                 size=12)
    add_notes(slide, "См. slides/s05-keystone-matrix.md speaker notes.")


# ====================================================================
# SECTION 1: Q1 mainstream production (s06-s12)
# ====================================================================

def s06_q1_divider(p):
    return section_divider(
        p, "Q1", "Зрелое производство",
        "AI здесь — мультипликатор классических методов. Самый освоенный квадрант. И самый структурно проваленный.",
        "3 рабочих кейса · 2 структурных провала · 86% пилотов застряло — статистическая норма",
        section_idx=1, large_size=200, label_color=MID)


def s07_pilot_stuck(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.8,
             "86% AI-проектов в энергетике застряли в пилоте",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "McKinsey State of AI 2024 — vs cross-industry ~67%. Энергетика на 18 п.п. хуже среднего.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.7, 6.0, 4.6)
    img = ASSETS / "charts" / "s07-pilot-stuck.png"
    add_image_aspect(slide, img, 0.7, 1.85, 5.6, 4.3)
    rounded_box(slide, 6.7, 1.7, 6.13, 4.6)
    multiline_box(slide, 6.9, 1.85, 5.83, 4.4, [
        ("5 структурных причин:", {"size": 14, "bold": True, "color": MID}),
        ("", {"size": 4}),
        ("1. Данные. 60–80% времени AI-проекта = очистка данных. Только 21% энергокомпаний имеют качество для AI промышленного уровня.", {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("2. Legacy IT integration. Стоимость интеграции SCADA/MES/ERP — в 3–5× выше стоимости AI-софта.", {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("3. Дефицит кадров. AI + предметная область. После 2020 крах — 107k jobs потеряно.", {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("4. Культура безопасности. Senior operator отказывает рискованной рекомендации — и часто прав.", {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("5. Горизонт ROI. AI-vendor обещает 12–18 мес; field life 20–30 лет. Несовместимо.", {"size": 11, "color": DEEP}),
    ], line_spacing=1.2)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Это не «AI плохой» — это статистическая норма отрасли. 14% successful vs 86% stuck — инженерный фильтр, а не приговор.",
                 size=12)
    add_notes(slide, "См. slides/s07-86-percent-pilot-stuck.md speaker notes.")


def s07b_aspen_alert_fatigue(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.35, 12.33, 0.85,
             "«Усталость от ложных тревог устранена» — это маркетинг",
             size=22, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.2, 12.33, 0.4,
             "Aspen Mtell на нефтепереработке: 100–500 алертов в день; plant-wide пилоты тихо закрываются.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.7, 5.5, 4.5)
    img = ASSETS / "screenshots" / "s09-aspen.jpg"
    add_image_aspect(slide, img, 0.7, 1.85, 5.1, 4.0)
    attribution(slide, "AspenTech · Aspen Mtell product page", x=0.7, y=5.85, w=5.0)
    rounded_box(slide, 6.2, 1.7, 6.63, 4.5)
    multiline_box(slide, 6.4, 1.8, 6.3, 4.4, [
        ("Маркетинг (AspenTech):", {"size": 13, "bold": True, "color": MID}),
        ("«Снижение незапланированного простоя на 60%»", {"size": 11, "color": DEEP, "italic": True}),
        ("«Усталость операторов устранена»", {"size": 11, "color": DEEP, "italic": True}),
        ("", {"size": 4}),
        ("Реальность на НПЗ:", {"size": 13, "bold": True, "color": RED_WARN}),
        ("· 100–500 alerts/день — оператор перестаёт реагировать", {"size": 11, "color": DEEP}),
        ("· Single-column success → plant-wide пилот тихо закрыт", {"size": 11, "color": DEEP}),
        ("· Honeywell UOP 310+ юнитов / ~700 НПЗ = ~44% rate", {"size": 11, "color": DEEP}),
        ("· Многие НПЗ — «классический APC без AI»", {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("Структурный gap:", {"size": 13, "bold": True, "color": GOLD}),
        ("Multi-physics (масс + энергия + реакция + коррозия) ломает ML-суррогаты на edge cases.", {"size": 11, "color": DEEP}),
    ], line_spacing=1.3)
    gold_callout(slide, 0.5, 6.35, 12.33, 0.55,
                 "Урок: vendor self-report ≠ field reality. Custody transfer, SIS, plant-wide refinery — AI ещё не дошёл.",
                 size=12)
    add_notes(slide, "См. slides/s07b-aspen-alert-fatigue.md speaker notes.")


def s08_ambyint(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Ambyint InfinityRL: +15% на 200 скважинах Permian",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Канадский стартап Калгари (2014), $25M Series B 2022. RL для оптимизации искусственного подъёма.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.8, 6.0, 4.5)
    img = ASSETS / "charts" / "s08-ambyint-delta.png"
    add_image_aspect(slide, img, 0.7, 1.95, 5.6, 4.2)
    rounded_box(slide, 6.7, 1.8, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("Метрики кейса:", {"size": 14, "bold": True, "color": MID}),
        ("· Регионы: Permian + Eagle Ford + Bakken", {"size": 12, "color": DEEP}),
        ("· Тип: штанговые насосы + ЭЦН (mature production)", {"size": 12, "color": DEEP}),
        ("· Baseline: 100–500 bopd per well", {"size": 12, "color": DEEP}),
        ("· Delta: +15% от per-well historical mean", {"size": 12, "color": DEEP, "bold": True}),
        ("· На 200 скважинах: +3 000–15 000 bopd total", {"size": 12, "color": GOLD, "bold": True}),
        ("", {"size": 6}),
        ("Почему это сильный кейс:", {"size": 14, "bold": True, "color": MID}),
        ("1. Verifiable baseline — не «спас $10M» без знаменателя.", {"size": 12, "color": DEEP}),
        ("2. RL поверх классики — augmentation, не замена.", {"size": 12, "color": DEEP}),
        ("3. Узкая область — оптимизация подъёма, не «AI везде».", {"size": 12, "color": DEEP}),
    ], line_spacing=1.3)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Когда Ambyint НЕ работает: stripper wells <10 bopd. +15% = +1,5 bopd; стоимость развёртывания > извлечённой ценности.",
                 size=12)
    add_notes(slide, "См. slides/s08-ambyint-infinityrl.md speaker notes.")


def s09_vendor_landscape(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Ландшафт поставщиков Q1 — 3 группы",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.05, 12.33, 0.4,
             "Тот же режим (прогностическое обслуживание) реализуют 10+ вендоров. Mode ≠ brand.",
             size=13, italic=True, color=LIGHT)
    groups = [
        ("ML-стартапы\nдля производства", LIGHT, [
            "Ambyint (Калгари) — InfinityRL для\nискусственного подъёма",
            "OspreyData (→ Mesquite 2022) —\nexpert-augmented ML для ESP, газлифта",
        ]),
        ("Enterprise\n(NOC + super-majors)", MID, [
            "SLB Avocet — ПО управления\nдобычей с ML с 2020+",
            "Halliburton DecisionSpace\nProduction — аналог. Industrial scale.",
        ]),
        ("Refinery + pipeline", TEAL, [
            "AspenTech Aspen Mtell (Emerson)\n— rising через cross-продажи",
            "Honeywell UOP Connect — 310+\nюнитов / ~700 НПЗ = ~44%",
            "Yokogawa / ABB Genix / Emerson —\nконкуренты",
        ]),
    ]
    col_w = 4.0
    gap = 0.15
    x0 = 0.5
    y = 1.6
    for i, (title, accent, items) in enumerate(groups):
        x = x0 + i * (col_w + gap)
        rounded_box(slide, x, y, col_w, 4.3)
        rectangle(slide, x, y, col_w, 0.95, fill=accent)
        text_box(slide, x+0.1, y+0.1, col_w-0.2, 0.8, title,
                 size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        lines = []
        for j, item in enumerate(items):
            lines.append((f"· {item}", {"size": 11, "color": DEEP}))
            if j < len(items) - 1:
                lines.append(("", {"size": 4}))
        multiline_box(slide, x+0.2, y+1.1, col_w-0.4, 3.0, lines, line_spacing=1.3)
    gold_callout(slide, 0.5, 6.05, 12.33, 0.85,
                 "Bonus — Drilling subset: Nabors PACE-X (4-мильный ствол Bakken) · NOV NOVOS · Precision Drilling AlphaAutomation. Mode = автоматизация бурения; brand вторичен.",
                 size=12)
    add_notes(slide, "См. slides/s09-q1-vendor-landscape.md speaker notes.")


def s10_rosneft_digital_field(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Роснефть Digital Field на Башнефть Илишевское",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.25, 12.33, 0.4,
             "Внутренняя разработка после ухода Roxar / Schlumberger в 2022. Vertical integration default.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.8, 6.0, 4.5)
    multiline_box(slide, 0.7, 1.95, 5.7, 4.3, [
        ("Метрики Илишевского, 2024:", {"size": 14, "bold": True, "color": MID}),
        ("", {"size": 6}),
        ("+1 Mt/год", {"size": 36, "bold": True, "color": GOLD}),
        ("дополнительной нефти (= +5,9% от ~17 Mt/год)", {"size": 11, "italic": True, "color": SLATE}),
        ("", {"size": 8}),
        ("~1 млрд ₽/год", {"size": 24, "bold": True, "color": DEEP}),
        ("дополнительного эффекта", {"size": 11, "italic": True, "color": SLATE}),
        ("", {"size": 8}),
        ("23 продукта (10 коммерциализованных)", {"size": 14, "color": DEEP}),
        ("+60% удалённого управления · +5% энергоэфф. · −5% логистики", {"size": 11, "color": DEEP}),
    ], line_spacing=1.2)
    rounded_box(slide, 6.7, 1.8, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("Контекст: санкции → insourcing", {"size": 14, "bold": True, "color": MID}),
        ("", {"size": 6}),
        ("· После марта 2022 — Roxar (Schlumberger), AspenTech, Honeywell ушли с РФ.", {"size": 12, "color": DEEP}),
        ("", {"size": 4}),
        ("· Vertical integration — необходимость, не выбор.", {"size": 12, "color": DEEP}),
        ("", {"size": 4}),
        ("· Ближе к китайской модели (Sinopec, CNOOC), чем к американской vendor-based.", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Caveat:", {"size": 12, "bold": True, "color": GOLD}),
        ("Российские KPI = self-reported в press release; independent audit ограничен санкциями. Тот же уровень осторожности, что для Aramco $1,8B.", {"size": 11, "italic": True, "color": DEEP}),
    ], line_spacing=1.3)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Башнефть Илишевское — типичное зрелое месторождение Q1: эксплуатируется с 1980-х, ~17 Mt/год исходный уровень. Пилотировать AI на known asset, не на frontier.",
                 size=12)
    add_notes(slide, "См. slides/s10-rosneft-digital-field.md speaker notes.")


def s11_cognite_c3ai(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Cognite + C3.ai: чистые AI-вендоры теряют долю",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.25, 12.33, 0.4,
             "Foundation models едят vertical AI specialists. Адресуемый рынок уже, чем ожидалось.",
             size=13, italic=True, color=LIGHT)
    boxes = [
        ("Cognite (Норвегия, выделён из Aker BP 2017)", LIGHT, [
            "2018: оценка ~$300M",
            "2021–2022: план IPO $2–3B в 2023",
            "2023: IPO отменён — рыночные условия + сжигание капитала",
            "2024: ARR $94M (+40% YoY), 871 сотрудник после реструктуризации",
            "2026: «время IPO неопределённо» (Aker ASA отчёт)",
        ]),
        ("C3.ai (US, основан 2009 Tom Siebel)", TEAL, [
            "BHC3 JV с Baker Hughes (2019) — реструктурирован к 2023",
            "FY24 O&G вертикаль = 5,9% выручки = ~$18M из $310M",
            "FY25: «не-нефтегазовая выручка +48% YoY» → нефтегаз уменьшается",
            "C3.ai сместил фокус на federal/defence",
            "IPO 2020: $42 → пик ~$15B → 2026: ~$3–4B (−70–80% от пика)",
        ]),
    ]
    col_w = 6.0
    gap = 0.33
    x0 = 0.5
    y = 1.8
    for i, (title, accent, items) in enumerate(boxes):
        x = x0 + i * (col_w + gap)
        rounded_box(slide, x, y, col_w, 4.5)
        rectangle(slide, x, y, col_w, 0.7, fill=accent)
        text_box(slide, x+0.15, y, col_w-0.3, 0.7, title,
                 size=13, bold=True, color=WHITE, align=PP_ALIGN.LEFT,
                 anchor=MSO_ANCHOR.MIDDLE)
        lines = []
        for item in items:
            lines.append((f"· {item}", {"size": 12, "color": DEEP}))
            lines.append(("", {"size": 4}))
        multiline_box(slide, x+0.2, y+0.85, col_w-0.4, 3.5, lines, line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Foundation models (SLB Lumi, METABRAIN) поедают узкоспециализированных: (a) большая модель + LoRA > специализированная; (b) крупные NOC разрабатывают свои foundation models.",
                 size=12)
    add_notes(slide, "См. slides/s11-cognite-c3ai-decline.md speaker notes.")


def s12_q1_no_ai_criteria(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.8,
             "Когда AI НЕ нужен в Q1 — 6 структурных критериев",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Distilled из практики последних 5 лет. Каждый — с конкретной альтернативой.",
             size=13, italic=True, color=LIGHT)
    criteria = [
        ("1", "Зрелый пласт + Eclipse", "Senior engineer + классический симулятор дают надёжные ответы. ML — overhead без существенного прироста.", LIGHT),
        ("2", "Stripper wells <10 bopd", "Прибавка +15% = +1,5 bopd; стоимость развёртывания > извлечённой ценности. Юнит-экономика отрицательная.", GOLD),
        ("3", "Custody transfer metering", "Передача товарной нефти. Регулятор требует mass flow meter 0,2% точности. Не black-box ML.", MID),
        ("4", "BOP / PRV / ESD — SIS", "SIL3/SIL4 по IEC 61511 = детерминированно + сертифицируемо. ML не сертифицируется.", TEAL),
        ("5", "Frontier без analog data", "ML не на чем обучать. Senior геофизик + классическая интерпретация (preview Разд. 2).", DEEP),
        ("6", "EU Methane Reg reporting", "Traceability mandated — не black-box ML estimate. Регуляторный compliance.", LIGHT),
    ]
    card_w = 4.0
    card_h = 2.3
    gap_x = 0.15
    gap_y = 0.15
    x0 = 0.5
    y0 = 1.6
    for i, (num, title, body, accent) in enumerate(criteria):
        col = i % 3
        row = i // 3
        x = x0 + col * (card_w + gap_x)
        y = y0 + row * (card_h + gap_y)
        rounded_box(slide, x, y, card_w, card_h, stroke=accent, stroke_w=2)
        circle(slide, x + 0.15, y + 0.15, 0.6, 0.6, fill=accent)
        text_box(slide, x + 0.15, y + 0.15, 0.6, 0.6, num,
                 size=20, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.85, y + 0.2, card_w - 1.0, 0.5, title,
                 size=13, bold=True, color=DEEP)
        text_box(slide, x + 0.2, y + 0.85, card_w - 0.4, card_h - 1.0, body,
                 size=10, color=DEEP, line_spacing=1.3)
    gold_callout(slide, 0.5, 6.65, 12.33, 0.45,
                 "Главный навык курса: уметь сказать «нет» там, где AI не нужен. 14% successful vs 86% pilot stuck — разница часто именно здесь.",
                 size=12)
    add_notes(slide, "См. slides/s12-q1-no-ai-criteria.md speaker notes.")


# ====================================================================
# SECTION 2: Q3 frontier exploration (s13-s19)
# ====================================================================

def s13_q3_divider(p):
    return section_divider(
        p, "Q3", "Разведка фронтиров",
        "Каждая wildcat-скважина = $50–100M. Размер выборки 1–5 скважин. ML не обобщается без аналогов. Physics ground truth, AI как дополнение.",
        "3 рабочих кейса · 2 провала десятилетия · HPC-гонка $100–400M на инсталляцию",
        section_idx=2, large_size=200, label_color=LIGHT)


def s14_hpc_eni_aramco(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "HPC-гонка Q3: $100–400M на инсталляцию",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Не коммодизируется как облако — стратегический CapEx. Малые операторы вытесняются capital barrier.",
             size=13, italic=True, color=LIGHT)
    # Eni HPC6
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    rectangle(slide, 0.5, 1.85, 6.0, 0.55, fill=MID)
    text_box(slide, 0.65, 1.85, 5.7, 0.55, "Eni HPC6 (декабрь 2024)",
             size=15, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    img = ASSETS / "screenshots" / "s14-eni.jpg"
    add_image_aspect(slide, img, 0.65, 2.5, 5.7, 1.7)
    multiline_box(slide, 0.65, 4.3, 5.7, 2.05, [
        ("606 PFLOPS peak · 477 sustained", {"size": 13, "color": DEEP, "bold": True}),
        ("14 000 AMD MI250X GPU", {"size": 12, "color": DEEP}),
        ("$104 млн capex", {"size": 14, "bold": True, "color": GOLD}),
        ("Top500 #5 мирового рейтинга", {"size": 12, "color": DEEP}),
        ("Стратегия: cost-effective per-FLOP (AMD vs NVIDIA)", {"size": 11, "color": SLATE, "italic": True}),
    ], line_spacing=1.3)
    # Aramco METABRAIN
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    rectangle(slide, 6.7, 1.85, 6.13, 0.55, fill=TEAL)
    text_box(slide, 6.85, 1.85, 5.83, 0.55, "Aramco METABRAIN (2024–2025)",
             size=15, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    img2 = ASSETS / "charts" / "s14-aramco-roi.png"
    add_image_aspect(slide, img2, 6.85, 2.5, 5.83, 1.7)
    multiline_box(slide, 6.85, 4.3, 5.83, 2.05, [
        ("~250 млрд параметров [VFY-day-of]", {"size": 13, "color": DEEP, "bold": True}),
        ("7 трлн токенов = 90 лет данных Aramco", {"size": 12, "color": DEEP}),
        ("$1,8 млрд realized 2024 (Davos янв 2025)", {"size": 14, "bold": True, "color": GOLD}),
        ("6 000 сотрудников обучены, 430 use cases", {"size": 12, "color": DEEP}),
        ("Источник: CEO Amin Nasser", {"size": 11, "color": SLATE, "italic": True}),
    ], line_spacing=1.3)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Aramco выручка 2024 = $436,6 млрд → $1,8B / $436,6B = 0,41%. AI добавляет полпроцента к полностью оптимизированной операции.",
                 size=12)
    add_notes(slide, "См. slides/s14-hpc-eni-aramco.md speaker notes.")


def s15_slb_lumi(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "SLB Lumi (сентябрь 2024) — foundation model поверх Petrel + Delfi",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Anchor customers: Aker BP, Shell, Azule Energy. NVIDIA Grace Hopper backend.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 5.5, 4.4)
    img = ASSETS / "screenshots" / "s15-slb2.jpg"
    add_image_aspect(slide, img, 0.65, 2.0, 5.2, 4.05)
    attribution(slide, "SLB / Schlumberger press kit · 2024", x=0.65, y=6.05, w=5.2)
    rounded_box(slide, 6.2, 1.85, 6.63, 4.4)
    multiline_box(slide, 6.4, 1.95, 6.3, 4.25, [
        ("Что Lumi делает:", {"size": 14, "bold": True, "color": MID}),
        ("· Petrophysics interpretation — каротаж", {"size": 12, "color": DEEP}),
        ("· Seismic auto-tracking — трассировка горизонтов", {"size": 12, "color": DEEP}),
        ("· Reservoir characterization preview — фации", {"size": 12, "color": DEEP}),
        ("· Drilling parameter optimization", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Контекст:", {"size": 14, "bold": True, "color": MID}),
        ("· SLB digital revenue 2024 = $2+ млрд = 5,7% от $35 млрд", {"size": 12, "color": DEEP}),
        ("· Halliburton + OpenAI/Anthropic — partnership-driven", {"size": 12, "color": DEEP}),
        ("· Mode «отраслевая foundation model» ≠ brand «Lumi»", {"size": 12, "color": GOLD, "bold": True}),
    ], line_spacing=1.3)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Через 2-3 года: SLB Lumi 2.0 или конкурент. Brand вторичен, mode (foundation model на 80+ лет industry data) первичен.",
                 size=12)
    add_notes(slide, "См. slides/s15-slb-lumi.md speaker notes.")


def s16_exxon_discovery6(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "ExxonMobil Discovery 6 — 4D-сейсмика месяцы → недели",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "HPE Cray EX4000, 4 032 NVIDIA Grace Hopper, 4× compute vs Discovery 5. $200–400M capex [VFY].",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 5.5, 4.4)
    img = ASSETS / "screenshots" / "s16-exxon.png"
    add_image_aspect(slide, img, 0.65, 2.0, 5.2, 4.05)
    attribution(slide, "ExxonMobil corporate press · 2024", x=0.65, y=6.05, w=5.2)
    rounded_box(slide, 6.2, 1.85, 6.63, 4.4)
    multiline_box(slide, 6.4, 1.95, 6.3, 4.25, [
        ("Что делает Discovery 6:", {"size": 14, "bold": True, "color": MID}),
        ("· 4D-сейсмика (3D + время) — месяцы → недели", {"size": 12, "color": DEEP, "bold": True}),
        ("· Активное управление пластом в реальном времени", {"size": 12, "color": DEEP}),
        ("· Stabroek Block Guyana — основной use case", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Stabroek case:", {"size": 14, "bold": True, "color": MID}),
        ("· 6 FPSO (плавучие платформы) к 2026", {"size": 12, "color": DEEP}),
        ("$1 млрд+", {"size": 28, "bold": True, "color": GOLD}),
        ("unlock через быстрое repositioning скважин", {"size": 11, "italic": True, "color": SLATE}),
        ("", {"size": 6}),
        ("Параллель Aramco METABRAIN: тот же mode, разные стратегии (US vs Saudi).", {"size": 11, "color": DEEP, "italic": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Capital barrier: $200–400M для топового HPC исключает 95% операторов. NOC + super-majors only.",
                 size=12)
    add_notes(slide, "См. slides/s16-exxonmobil-discovery6.md speaker notes.")


def s17_bp_beyond_limits(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "BP + Beyond Limits — $20M, vendor pivot 2023",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "BP Ventures Series B июнь 2017 → Beyond Limits pivot в healthcare/manufacturing 2023.",
             size=13, italic=True, color=LIGHT)
    # Left: promises
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    rectangle(slide, 0.5, 1.85, 6.0, 0.55, fill=LIGHT)
    text_box(slide, 0.65, 1.85, 5.7, 0.55, "Что обещали (2018):",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 0.7, 2.55, 5.6, 3.7, [
        ("«AI absorb learnings of geologists", {"size": 13, "italic": True, "color": DEEP}),
        ("and imitate their decision-making».", {"size": 13, "italic": True, "color": DEEP}),
        ("", {"size": 6}),
        ("Heritage:", {"size": 13, "bold": True, "color": MID}),
        ("· NASA JPL ($20M heritage)", {"size": 12, "color": DEEP}),
        ("· Glendale, California 2014", {"size": 12, "color": DEEP}),
        ("· «Cognitive AI» как differentiator", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("BP signals 2018:", {"size": 13, "bold": True, "color": MID}),
        ("· $20M Series B июнь 2017", {"size": 12, "color": DEEP}),
        ("· Beyond Petroleum rebrand attempt", {"size": 12, "color": DEEP}),
        ("· Public commitment", {"size": 12, "color": DEEP}),
    ], line_spacing=1.3)
    # Right: failures
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    rectangle(slide, 6.7, 1.85, 6.13, 0.55, fill=RED_WARN)
    text_box(slide, 6.85, 1.85, 5.83, 0.55, "Что получили (2018–2023):",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 6.9, 2.55, 5.73, 3.7, [
        ("7 лет публичных", {"size": 36, "bold": True, "color": GOLD}),
        ("результатов нет", {"size": 18, "bold": True, "color": DEEP}),
        ("", {"size": 6}),
        ("· 0 кейсов на сайте BP после 2019", {"size": 12, "color": DEEP}),
        ("· 0 публикаций в Society of Petroleum Engineers", {"size": 12, "color": DEEP}),
        ("· Beyond Limits pivot в healthcare/manufacturing 2023", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("3 урока:", {"size": 13, "bold": True, "color": RED_WARN}),
        ("1. Vendor concentration — single small vendor", {"size": 11, "color": DEEP}),
        ("2. Cognitive marketing — anthropomorphic overpromise", {"size": 11, "color": DEEP}),
        ("3. Imitation framing — AI не имитирует, он approximates", {"size": 11, "color": DEEP}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "«Cognitive AI имитирует геолога» = anthropomorphic frame, который скрывает structural fit assessment.",
                 size=12)
    add_notes(slide, "См. slides/s17-bp-beyond-limits-failure.md speaker notes.")


def s18_ibm_repsol(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "IBM Watson + Repsol Kalimba (2014–2022)",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Hype cycle 2014–2016 → реальное commercial use ≤10% от ожиданий. Watson Industry Solutions stagnation 2018–2022.",
             size=13, italic=True, color=LIGHT)
    # Kalimba project
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    rectangle(slide, 0.5, 1.85, 6.0, 0.55, fill=LIGHT)
    text_box(slide, 0.65, 1.85, 5.7, 0.55, "Kalimba project 2014–2022",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 0.7, 2.55, 5.6, 3.7, [
        ("2014:", {"size": 13, "bold": True, "color": MID}),
        ("· IBM + Repsol объявляют партнёрство", {"size": 12, "color": DEEP}),
        ("· Cognitive Environments Lab (NY) + Repsol Tech Centre (Мадрид)", {"size": 12, "color": DEEP}),
        ("· «Cognitive computing для exploration»", {"size": 12, "color": DEEP, "italic": True}),
        ("", {"size": 6}),
        ("2014–2022:", {"size": 13, "bold": True, "color": MID}),
        ("· 30 лет exploration data «analyzed»", {"size": 12, "color": DEEP}),
        ("· Конкретных new discoveries не объявлено", {"size": 12, "color": DEEP}),
        ("· Repsol exploration budget shrunk 2019+", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("2022:", {"size": 13, "bold": True, "color": RED_WARN}),
        ("· Тихое сворачивание", {"size": 12, "color": DEEP, "bold": True}),
    ], line_spacing=1.3)
    # Watson Health parallel
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    rectangle(slide, 6.7, 1.85, 6.13, 0.55, fill=RED_WARN)
    text_box(slide, 6.85, 1.85, 5.83, 0.55, "Watson Health parallel",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 6.9, 2.55, 5.73, 3.7, [
        ("$5 млрд+", {"size": 32, "bold": True, "color": GOLD}),
        ("инвестиций IBM в Watson Health 2015–2021", {"size": 12, "color": DEEP, "italic": True}),
        ("", {"size": 8}),
        ("→ продан Francisco Partners 2022", {"size": 14, "bold": True, "color": DEEP}),
        ("за ~$1 млрд (= 20% от инвестиций)", {"size": 12, "color": DEEP}),
        ("", {"size": 8}),
        ("3 урока:", {"size": 13, "bold": True, "color": RED_WARN}),
        ("1. General-purpose cognitive не scaled в narrow domain", {"size": 11, "color": DEEP}),
        ("2. Hype cycle 2014–2016 → реальное use ≤10% от ожиданий", {"size": 11, "color": DEEP}),
        ("3. SLB Lumi и Aramco METABRAIN — domain-specific = успешнее", {"size": 11, "color": DEEP}),
    ], line_spacing=1.3)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Watson Health → ~$1B продан = $5B инвестиций vs $1B продажа = провал $4B. Indirect анчор: Kalimba не был исключением — он был частью паттерна.",
                 size=12)
    add_notes(slide, "См. slides/s18-ibm-repsol-failure.md speaker notes.")


def s19_q3_alternatives(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Альтернатива Q3: physics-based simulators + senior expertise",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "AI augmentation поверх, не replacement. Через 5 лет Eclipse будет стандартом — не AI-замена.",
             size=13, italic=True, color=LIGHT)
    sims = [
        ("Eclipse (SLB)", "Industry-standard reservoir simulator с 1983.\nMature reservoirs + regulatory submissions.\nCoupled fluid + heat + chemistry equations.", MID),
        ("INTERSECT (SLB)", "Successor для massively parallel HPC.\nLarge models, finer grids.\nReplaces Eclipse на топовых проектах.", LIGHT),
        ("CMG IMEX / STARS / GEM", "Computer Modelling Group (Calgary).\nIMEX black-oil, STARS thermal/EOR, GEM compositional.\nLeader в heavy oil + EOR niche.", TEAL),
        ("OpenFOAM (CFD)", "Open-source CFD для NPV simulation,\ngeomechanics, fracturing modeling.\nResearch + reservoir characterization.", DEEP),
    ]
    sim_w = 6.0
    sim_h = 2.0
    gap = 0.2
    x0 = 0.5
    y0 = 1.85
    for i, (name, body, accent) in enumerate(sims):
        col = i % 2
        row = i // 2
        x = x0 + col * (sim_w + gap)
        y = y0 + row * (sim_h + gap)
        rounded_box(slide, x, y, sim_w, sim_h, stroke=accent, stroke_w=2)
        rectangle(slide, x, y, 0.15, sim_h, fill=accent)
        text_box(slide, x + 0.3, y + 0.1, sim_w - 0.4, 0.5, name,
                 size=14, bold=True, color=DEEP)
        text_box(slide, x + 0.3, y + 0.6, sim_w - 0.4, sim_h - 0.7, body,
                 size=11, color=DEEP, line_spacing=1.35)
    gold_callout(slide, 0.5, 6.15, 12.33, 0.85,
                 "Senior геофизик ($200–500k/год) + classical interpretation > $5–20M foundation model в frontier. PINN = research-grade, не commercial. AI augmentation, не replacement.",
                 size=12)
    add_notes(slide, "См. slides/s19-q3-alternatives.md speaker notes.")


# ====================================================================
# SECTION 3: Q2 methane MRV (s20-s27)
# ====================================================================

def s20_methane_alphabet(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Methane MRV alphabet — 6 must-know терминов",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.05, 12.33, 0.4,
             "Все встретятся в следующих 8 слайдах. Brand names — не глоссируем.",
             size=13, italic=True, color=LIGHT)
    terms = [
        ("MRV", "Monitoring / Reporting / Verification\n= выявление-учёт-проверка\nMandatory под EU 2024/1787.", TEAL),
        ("OGI", "Optical Gas Imaging\n= оптическая газовая визуализация\nIR-камера (FLIR GFx320, Opgal EyeCGas).", MID),
        ("LDAR", "Leak Detection And Repair\n= программа выявления и устранения\n4×/год обходы с OGI + ремонт 5-15 дней.", LIGHT),
        ("OGMP 2.0", "UN Oil & Gas Methane Partnership Level 2.0\nLevel 5 — direct measurement.\n170+ компаний подписали.", GOLD),
        ("SIL / SIS", "Safety Integrity Level / Safety Instrumented System\nIEC 61511. SIL3 = 0,001–0,0001 PFD.\nML не сертифицируется.", DEEP),
        ("bopd / ESP", "Barrels of oil per day / Electric Submersible Pump\n= баррелей нефти/день / погружной электронасос\nStripper wells <10 bopd.", LIGHT),
    ]
    card_w = 4.0
    card_h = 2.3
    gap = 0.15
    x0 = 0.5
    y0 = 1.6
    for i, (acro, body, accent) in enumerate(terms):
        col = i % 3
        row = i // 3
        x = x0 + col * (card_w + gap)
        y = y0 + row * (card_h + gap)
        rounded_box(slide, x, y, card_w, card_h, stroke=accent, stroke_w=2)
        rectangle(slide, x, y, card_w, 0.6, fill=accent)
        text_box(slide, x+0.15, y+0.05, card_w-0.3, 0.5, acro,
                 size=18, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x+0.2, y+0.7, card_w-0.4, card_h - 0.85, body,
                 size=11, color=DEEP, line_spacing=1.3)
    gold_callout(slide, 0.5, 6.65, 12.33, 0.45,
                 "Bonus: AI essential именно потому, что OGI + Picarro + LI-COR покрывают facility-level — atomic detection требует слияния 4 сенсоров.",
                 size=12)
    add_notes(slide, "См. slides/s20-methane-alphabet.md speaker notes.")


def s21_q2_divider(p):
    return section_divider(
        p, "Q2", "Метановая MRV",
        "Данные — петабайты в день. Физика — разорвана. Слияние 4 сенсоров + атрибуция малой утечки — открытая ML-задача. AI необходим. Но один спутник = катастрофическая единичная уязвимость.",
        "4 рабочих системы · 2 провала · регуляторное давление из EU 2024/1787",
        section_idx=3, large_size=200, label_color=TEAL)


def s22_methanesat_permian(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "MethaneSAT (4 марта 2024) — flagship результат Permian",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Первый в истории спутник, владелец которого — экологическая некоммерческая организация. Бюджет $88M.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    img = ASSETS / "screenshots" / "s22-methanesat.png"
    add_image_aspect(slide, img, 0.65, 2.0, 5.7, 3.5)
    attribution(slide, "MethaneSAT / EDF · 2024", x=0.65, y=5.55, w=5.7)
    multiline_box(slide, 0.65, 5.85, 5.7, 0.45, [
        ("Что отличало MethaneSAT:", {"size": 12, "bold": True, "color": MID}),
    ])
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("Технические возможности:", {"size": 13, "bold": True, "color": MID}),
        ("· Wide-area coverage — 200×200 км за один проход", {"size": 11, "color": DEEP}),
        ("· Высокая точность — порог детекции ~500 кг/ч", {"size": 11, "color": DEEP}),
        ("· Открытый доступ через Google Earth Engine", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("Permian flagship результат:", {"size": 13, "bold": True, "color": MID}),
        ("410 т/ч", {"size": 32, "bold": True, "color": GOLD}),
        ("метана = +50% над оценкой EPA", {"size": 12, "italic": True, "color": DEEP}),
        ("", {"size": 4}),
        ("· Нью-Мексико: 1,2% intensity", {"size": 11, "color": DEEP}),
        ("· Техас: 3,1% intensity", {"size": 11, "color": DEEP}),
        ("· ~2 000 data files за 15,5 мес работы", {"size": 11, "color": DEEP}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "+50% над EPA — это не «AI ошибается». Это AI измеряет, а EPA inventory считает по емission factors 30-летней давности.",
                 size=12)
    add_notes(slide, "См. slides/s22-methanesat-permian.md speaker notes.")


def s23_methanesat_loss(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "20 июня 2025 — MethaneSAT потерян после 15,5 месяцев",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "4 марта 2024 запуск → 20 июня 2025 «spacecraft anomaly». 26% от 5-летнего designed lifetime.",
             size=13, italic=True, color=LIGHT)
    # Timeline LEFT
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    rectangle(slide, 0.5, 1.85, 6.0, 0.55, fill=LIGHT)
    text_box(slide, 0.65, 1.85, 5.7, 0.55, "Timeline",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 0.7, 2.55, 5.6, 3.75, [
        ("4 марта 2024", {"size": 14, "bold": True, "color": MID}),
        ("Запуск SpaceX Falcon 9", {"size": 12, "color": DEEP}),
        ("", {"size": 4}),
        ("Март 2024 — июнь 2025", {"size": 14, "bold": True, "color": MID}),
        ("15,5 месяцев операций", {"size": 12, "color": DEEP}),
        ("~2 000 data files собрано", {"size": 12, "color": DEEP}),
        ("", {"size": 4}),
        ("20 июня 2025", {"size": 14, "bold": True, "color": RED_WARN}),
        ("«Spacecraft anomaly» — потеря связи", {"size": 12, "color": DEEP}),
        ("", {"size": 4}),
        ("15,5 / 60 мес designed", {"size": 14, "bold": True, "color": GOLD}),
        ("= 26% lifetime realized", {"size": 12, "color": DEEP}),
        ("", {"size": 4}),
        ("$5,7M/мес realized vs $1,5M/мес планировалось", {"size": 11, "color": DEEP, "italic": True}),
    ], line_spacing=1.2)
    # Lessons RIGHT
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    rectangle(slide, 6.7, 1.85, 6.13, 0.55, fill=RED_WARN)
    text_box(slide, 6.85, 1.85, 5.83, 0.55, "4 урока loss",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 6.9, 2.55, 5.83, 3.75, [
        ("1. SPOF (single point of failure)", {"size": 13, "bold": True, "color": MID}),
        ("Single satellite = catastrophic loss vector. Constellation (GHGSat 13+) — robust.", {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("2. Hardware reliability", {"size": 13, "bold": True, "color": MID}),
        ("Свободный космос ≠ контролируемая лаборатория. 26% lifetime — high risk.", {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("3. Regulator constraint", {"size": 13, "bold": True, "color": MID}),
        ("EU 2024/1787 inspector cannot rely on one source. Diversification mandatory.", {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("4. AI ≠ upstream data", {"size": 13, "bold": True, "color": MID}),
        ("Software работает. Hardware failed. AI зависит от верхнего слоя.", {"size": 11, "color": DEEP}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Урок: regulatory infrastructure требует diversified sensor network, не single satellite. AI зависит от upstream hardware.",
                 size=12)
    add_notes(slide, "См. slides/s23-methanesat-loss.md speaker notes.")


def s24_post_methanesat_players(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Post-MethaneSAT: Carbon Mapper + GHGSat + Bridger + SeekOps",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Диверсифицированный sensor network — то, чем должен был быть MethaneSAT. Несколько провайдеров после loss.",
             size=13, italic=True, color=LIGHT)
    players = [
        ("Carbon Mapper Tanager-1", "Запуск 16 авг 2024.\nPlanet Labs constellation.\nNASA JPL technology.\nFacility-level detection.", TEAL),
        ("GHGSat constellation", "13-satellite по середине 2025.\n25м разрешение.\nFacility-level focus.\nCommercial: ExxonMobil, ConocoPhillips, EOG.", LIGHT),
        ("Bridger Photonics aerial", "Aerial LiDAR (gas mapping).\n4× точнее ground OGI.\nClose-range, slow scan.\nFor LDAR программ.", MID),
        ("SeekOps + Project Canary", "SeekOps — UAV-mounted methane sensors.\nProject Canary — continuous monitoring sites.\nCertification (RSG, MiQ).", GOLD),
    ]
    p_w = 6.0
    p_h = 2.05
    gap = 0.2
    x0 = 0.5
    y0 = 1.85
    for i, (name, body, accent) in enumerate(players):
        col = i % 2
        row = i // 2
        x = x0 + col * (p_w + gap)
        y = y0 + row * (p_h + gap)
        rounded_box(slide, x, y, p_w, p_h, stroke=accent, stroke_w=2)
        rectangle(slide, x, y, p_w, 0.5, fill=accent)
        text_box(slide, x+0.15, y, p_w-0.3, 0.5, name,
                 size=13, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x+0.2, y+0.6, p_w-0.4, p_h - 0.75, body,
                 size=11, color=DEEP, line_spacing=1.3)
    gold_callout(slide, 0.5, 6.15, 12.33, 0.85,
                 "Lesson: один спутник — single point of failure. Диверсифицированный sensor network (satellite + aerial + ground) — robust. EU regulator требует именно этого.",
                 size=12)
    add_notes(slide, "См. slides/s24-post-methanesat-players.md speaker notes.")


def s25_4x_discrepancy(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "4× разрыв industry vs регулятор — methodological gap",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "MethaneSAT measured ~15 Mt/год US O&G. EPA Inventory ~4 Mt. Stanford 2024 aerial ~7 Mt = factor 2.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    img = ASSETS / "charts" / "s25-4x-discrepancy.png"
    add_image_aspect(slide, img, 0.7, 2.0, 5.6, 4.2)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("Что это значит:", {"size": 14, "bold": True, "color": MID}),
        ("· EPA inventory: bottom-up подход, факторы 1990-х.", {"size": 11, "color": DEEP}),
        ("· Stanford aerial: top-down measurements, 2024.", {"size": 11, "color": DEEP}),
        ("· MethaneSAT: spaceborne, всё что меньше 500 кг/ч missed.", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("9-satellite test 2024 (Atmospheric Measurement Techniques):", {"size": 13, "bold": True, "color": MID}),
        ("· 58% emission points identified.", {"size": 11, "color": DEEP}),
        ("· 41% false negatives.", {"size": 11, "color": DEEP, "bold": True}),
        ("· AI не «ошибается» — sensors имеют структурные limit.", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("Это не AI failure:", {"size": 13, "bold": True, "color": GOLD}),
        ("Это structural methodological gap. EPA modernization in progress.", {"size": 11, "color": DEEP, "italic": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Cross-source triangulation = единственный валидный подход. AI essential, но AI ≠ ground truth — он измеряет, факелы факелуют.",
                 size=12)
    add_notes(slide, "См. slides/s25-4x-discrepancy.md speaker notes.")


def s26_eu_vs_epa(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "EU 2024/1787 vs EPA Subpart W — AI MRV рынок развивается асимметрично",
             size=22, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.35, 12.33, 0.4,
             "EU operator рискует штрафом > прибыли от добычи. US operator не торопится инвестировать.",
             size=13, italic=True, color=LIGHT)
    # EU vs EPA boxes
    rounded_box(slide, 0.5, 1.9, 6.0, 4.4)
    rectangle(slide, 0.5, 1.9, 6.0, 0.7, fill=MID)
    text_box(slide, 0.65, 1.9, 5.7, 0.7, "EU 2024/1787 (август 2024)",
             size=15, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 0.7, 2.75, 5.6, 3.5, [
        ("до 20%", {"size": 36, "bold": True, "color": GOLD}),
        ("оборотного штрафа за non-compliance", {"size": 11, "italic": True, "color": SLATE}),
        ("", {"size": 8}),
        ("Ключевые deadlines:", {"size": 13, "bold": True, "color": DEEP}),
        ("· LDAR обязательный — 5 мая 2025", {"size": 12, "color": DEEP}),
        ("· OGMP Level 4/5 reports — 5 авг 2025", {"size": 12, "color": DEEP}),
        ("· Imports compliance — с 2027", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Driver:", {"size": 12, "bold": True, "color": MID}),
        ("Shell, TotalEnergies — фронт enforcement.", {"size": 12, "color": DEEP}),
    ], line_spacing=1.25)
    rounded_box(slide, 6.7, 1.9, 6.13, 4.4)
    rectangle(slide, 6.7, 1.9, 6.13, 0.7, fill=LIGHT)
    text_box(slide, 6.85, 1.9, 5.83, 0.7, "US EPA Subpart W",
             size=15, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 6.9, 2.75, 5.83, 3.5, [
        ("6 мая 2024 final → delay 2034 [VFY]", {"size": 14, "bold": True, "color": DEEP}),
        ("", {"size": 6}),
        ("Что произошло:", {"size": 13, "bold": True, "color": LIGHT}),
        ("· Final rule утверждён 6 мая 2024", {"size": 12, "color": DEEP}),
        ("· Trump administration пересмотр сентябрь 2025", {"size": 12, "color": DEEP}),
        ("· Proposed delay до 2034 для имплементации", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Эффект на рынок:", {"size": 13, "bold": True, "color": LIGHT}),
        ("· US AI MRV рынок ~$200M (2024)", {"size": 12, "color": DEEP}),
        ("· vs EU ~$500M+ к 2026 (estimate)", {"size": 12, "color": DEEP, "bold": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Регуляторика — главный driver Q2. EU жёстко → AI essential. US wait-and-see → AI рынок развивается медленнее.",
                 size=12)
    add_notes(slide, "См. slides/s26-eu-vs-epa-regulation.md speaker notes.")


def s27_q2_alternatives(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Альтернатива Q2: ground OGI + portable analyzers",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Когда AI не нужен — OGMP Level 5 (прямое измерение) + custody transfer metering.",
             size=13, italic=True, color=LIGHT)
    tools = [
        ("FLIR GFx320 / Opgal EyeCGas", "Hand-held OGI cameras.\nIR imaging углеводородов.\n2-3 inspection events/site/год.", LIGHT),
        ("Picarro G2210-i / LI-COR LI-7810", "Portable cavity ring-down spectroscopy.\nDirect measurement, ppb-уровень.\nFor OGMP Level 5 verification.", MID),
        ("Rebellion Photonics", "Fixed-position OGI + analytics.\nContinuous facility-level.\nReplaces AI screening на крупных hub.", TEAL),
        ("EPA Method 21 / EU LDAR", "Detector + sniffer for всех valves, flanges.\n4×/год обходы.\nMandatory под регуляцией.", GOLD),
    ]
    t_w = 6.0
    t_h = 2.0
    gap = 0.2
    x0 = 0.5
    y0 = 1.85
    for i, (name, body, accent) in enumerate(tools):
        col = i % 2
        row = i // 2
        x = x0 + col * (t_w + gap)
        y = y0 + row * (t_h + gap)
        rounded_box(slide, x, y, t_w, t_h, stroke=accent, stroke_w=2)
        rectangle(slide, x, y, 0.15, t_h, fill=accent)
        text_box(slide, x + 0.3, y + 0.1, t_w - 0.4, 0.5, name,
                 size=14, bold=True, color=DEEP)
        text_box(slide, x + 0.3, y + 0.65, t_w - 0.4, t_h - 0.75, body,
                 size=11, color=DEEP, line_spacing=1.35)
    gold_callout(slide, 0.5, 6.15, 12.33, 0.85,
                 "2 criteria когда AI не нужен в Q2: (1) OGMP Level 5 direct measurement compliance — regulator требует точность, не estimate; (2) custody transfer metering — mass flow meter mandatory, не AI.",
                 size=12)
    add_notes(slide, "См. slides/s27-q2-alternatives.md speaker notes.")


# Sectionовая загрузка продолжается в build_lec16_p2.py
if __name__ == "__main__":
    print("This is part 1 — see build_all.py for full assembly.")
