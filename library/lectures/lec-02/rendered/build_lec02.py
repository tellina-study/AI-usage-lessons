"""
Лекция 2 v2.0 (issue #183) — БАТЧ 1: Разделы 0–2, слайды s01–s17 (20 шт).

Source-of-truth: deck.yaml v2.0.1 + slides/*.md (v2 sources).
Порядок: s01 s02 s02a s03 s04 s04b | s05a s05 s06 s07 s08 s09 s10 s11 |
         s12a s12 s13 s14 s15 s17.
Батч 2 (Разделы 3–5) добавит s18a…s42 в этот же файл.

v2.0 key changes vs v1.8:
- Новая арка: чек-лист 6 заблуждений (s01 REWORK — checklist hook c hero
  «чёрный ящик с трещинами»), s04 REWORK (вопрос v2 + 6 промис-чипов).
- Keystone s04b: 7-стадийный inference-конвейер; на дивайдерах вместо
  6-секционного roadmap_bar — pipeline_bar (7 стадий, активная gold,
  без «вы здесь», без минут).
- s02a: 6 горизонтальных карточек-строк + M-чипы overlay (единственное
  место с M-метками кроме s38).
- НОВЫЕ слайды: s07 chat-шаблоны, s09 числа и код, s10 glitch-токены,
  s13 «три жизни», s15 similarity-граница (heatmap = PowerPoint-таблица
  с Ocean-заливкой ячеек, не картинка).
- Refs-registry v1.8 удалён: в v2-источниках нет [N]-маркеров, а
  auto-shrink ломал моноширинные [100][000][0] на s09.

Pipeline: python-pptx direct (канонический production-путь по
notes/mcp-limitations.md [#71-1] — full rebuild each iteration).
Palette LOCKED: Ocean #21295C/#065A82/#1C7293 + teal #028090 + gold #F0AB00.
Canvas 13.333"x7.5" (16:9).
"""
import re
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt
from lxml import etree

# === Palette (LOCKED, mirrored from deck.yaml v2.0.1) ===
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
SLATE_PN  = RGBColor(0x5B, 0x66, 0x78)

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

A_NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


# ============================================================
# Helpers (ported from v1.8 builder; refs system dropped)
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
    for el in sppr.findall(A_NS + "effectLst"):
        sppr.remove(el)
    etree.SubElement(sppr, A_NS + "effectLst")


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
    para = tf.paragraphs[0]
    para.alignment = align
    para.line_spacing = line_spacing
    r = para.add_run()
    r.text = text
    r.font.name = font; r.font.size = Pt(size)
    r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color
    return tb


def text_runs(slide, x, y, w, h, runs, *,
              align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
              line_spacing=1.15, font=FONT_BODY):
    """runs: list of dicts {text, size, bold, italic, color, font, newpara,
    align, line_spacing, space_after_pt}."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    para = tf.paragraphs[0]
    para.alignment = align
    para.line_spacing = line_spacing
    for cfg in runs:
        if cfg.get("newpara"):
            para = tf.add_paragraph()
            para.alignment = cfg.get("align", align)
            para.line_spacing = cfg.get("line_spacing", line_spacing)
            if cfg.get("space_before_pt"):
                para.space_before = Pt(cfg["space_before_pt"])
        r = para.add_run()
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


def filled_rect(slide, x, y, w, h, fill, *, stroke=None, stroke_pt=0.0,
                radius=False, radius_adj=0.16):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shp = slide.shapes.add_shape(shape_type, Inches(x), Inches(y),
                                 Inches(w), Inches(h))
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


def chip(slide, x, y, w, h, text, *, fill=MID, stroke=None, color=WHITE,
         size=14, bold=True, stroke_pt=1.2, font=FONT_BODY):
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
        shp.line.width = Pt(stroke_pt)
    tf = shp.text_frame
    tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.02); tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.word_wrap = False
    para = tf.paragraphs[0]; para.alignment = PP_ALIGN.CENTER
    r = para.add_run(); r.text = text
    r.font.name = font; r.font.size = Pt(size)
    r.font.bold = bold; r.font.color.rgb = color
    disable_shadow(shp)
    return shp


def add_image(slide, path, x, y, w=None, h=None):
    """Prefer only one of w/h — both stretches non-proportionally
    (notes/mcp-limitations.md #73-render-1)."""
    if not Path(path).exists():
        return
    if w is not None and h is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 width=Inches(w), height=Inches(h))
    elif w is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 width=Inches(w))
    elif h is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 height=Inches(h))
    else:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y))


def slide_title(slide, text, *, y=0.5, h=1.0, w=12.3, x=0.55, size=26,
                color=DEEP, bold=True, line_spacing=1.18,
                align=PP_ALIGN.LEFT):
    text_box(slide, x, y, w, h, text,
             size=size, bold=bold, color=color, line_spacing=line_spacing,
             align=align)


def gold_callout(slide, x, y, w, h, text, *, size=15, bold=True,
                 align=PP_ALIGN.LEFT):
    filled_rect(slide, x, y, w, h, GOLD_TINT, stroke=GOLD, stroke_pt=1.2,
                radius=True, radius_adj=0.12)
    text_box(slide, x + 0.2, y + 0.06, w - 0.4, h - 0.12, text,
             size=size, bold=bold, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=align, line_spacing=1.22)


def right_arrow(slide, x, y, w=0.6, h=0.4, fill=MID):
    shp = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    disable_shadow(shp)
    return shp


def down_arrow(slide, x, y, w=0.4, h=0.45, fill=MID):
    shp = slide.shapes.add_shape(MSO_SHAPE.DOWN_ARROW,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    disable_shadow(shp)
    return shp


def outline_big_text(slide, x, y, w, h, text, *, size=200, stroke=GOLD,
                     stroke_pt=2.6, align=PP_ALIGN.LEFT):
    """Decorative outline numeral: white fill + gold stroke via a:ln XML."""
    tb = text_box(slide, x, y, w, h, text, size=size, bold=True,
                  color=WHITE, align=align, line_spacing=0.95)
    r = tb.text_frame.paragraphs[0].runs[0]
    rPr = r._r.get_or_add_rPr()
    ln = rPr.makeelement(A_NS + "ln", {"w": str(int(stroke_pt * 12700))})
    sf = etree.SubElement(ln, A_NS + "solidFill")
    clr = etree.SubElement(sf, A_NS + "srgbClr")
    clr.set("val", "F0AB00" if stroke == GOLD else str(stroke))
    rPr.insert(0, ln)
    return tb


def speaker_notes(slide, text):
    """Readable paragraphs: blank-line-separated blocks each become one
    notes paragraph; single newlines collapse to spaces."""
    tf = slide.notes_slide.notes_text_frame
    tf.clear()
    blocks = [b.strip() for b in re.split(r'\n\s*\n', text.strip()) if b.strip()]
    if not blocks:
        blocks = [""]
    for i, block in enumerate(blocks):
        one = re.sub(r'\s*\n\s*', ' ', block)
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.text = one


def load_notes(slide_id):
    files = sorted(SLIDES_DIR.glob(f"{slide_id}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding='utf-8')
    m = re.search(r'## Speaker notes\s*\n(.*?)(?=\n## |\Z)', md, re.DOTALL)
    notes = m.group(1).strip() if m else ""
    return re.sub(r'\n+---\s*$', '', notes).strip()


def page_number(slide, n, *, color=SLATE_PN):
    tb = slide.shapes.add_textbox(Inches(12.45), Inches(7.16), Inches(0.8),
                                  Inches(0.28))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = False
    para = tf.paragraphs[0]
    para.alignment = PP_ALIGN.RIGHT
    r = para.add_run(); r.text = str(n)
    r.font.name = FONT_BODY; r.font.size = Pt(10)
    r.font.italic = True; r.font.color.rgb = color
    return tb


# ============================================================
# v2.0 pipeline progress bar (dividers) — 7 стадий конвейера s04b.
# Активная стадия(и) gold. Без «вы здесь», без минут.
# ============================================================
PIPE_STAGES = ["Текст", "Токены", "Векторы", "LLM",
               "Распределение", "Токен", "Текст"]


def pipeline_bar(slide, active, *, y=6.62, bar_h=0.48):
    """active: int index or set of indices highlighted gold."""
    if isinstance(active, int):
        active = {active}
    n = len(PIPE_STAGES)
    arrow_w = 0.24
    total_w = 12.3
    cell_w = (total_w - arrow_w * (n - 1)) / n
    start_x = (SLIDE_W_IN - total_w) / 2.0
    for i, label in enumerate(PIPE_STAGES):
        x = start_x + i * (cell_w + arrow_w)
        is_act = i in active
        fill = GOLD if is_act else SOFT_GREY
        color = DEEP if is_act else SLATE
        filled_rect(slide, x, y, cell_w, bar_h, fill, radius=True,
                    radius_adj=0.28)
        sz = 11 if len(label) < 12 else 9.5
        text_box(slide, x - 0.05, y + 0.06, cell_w + 0.1, bar_h - 0.12,
                 label, size=sz, bold=is_act, color=color,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < n - 1:
            ax = x + cell_w + 0.03
            right_arrow(slide, ax, y + bar_h / 2 - 0.07, w=arrow_w - 0.06,
                        h=0.14, fill=LIGHT)


def section_divider(p, *, section_n, sub_title, frame_phrase, tag,
                    active_stage, notes_id):
    """v2.0 divider: big gold «Раздел N» + подзаголовок + frame + tag +
    pipeline_bar (актив. стадия конвейера gold)."""
    s = blank(p)
    set_slide_bg(s, SURFACE)
    text_box(s, 0.55, 0.95, 12.3, 2.4, f"Раздел {section_n}",
             size=140, bold=True, color=GOLD,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    text_box(s, 0.55, 3.55, 12.3, 0.75, sub_title,
             size=44, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.55, 4.45, 12.3, 0.5, f"«{frame_phrase}»",
             size=20, italic=True, color=MID, align=PP_ALIGN.CENTER)
    text_box(s, 0.55, 5.25, 12.3, 0.45, tag,
             size=16, bold=True, color=TEAL, align=PP_ALIGN.CENTER)
    pipeline_bar(s, active_stage)
    speaker_notes(s, load_notes(notes_id))
    return s


# ============================================================
# Раздел 0
# ============================================================
def build_s01(p):
    """Checklist hook: 6 карточек-заблуждений поверх hero «чёрный ящик
    с трещинами» (собственная flat-иллюстрация, Ocean, ≥40% площади)."""
    s = blank(p)
    # Title: gold highlight на «верны?»
    text_runs(s, 0.55, 0.42, 12.3, 0.85, [
        {"text": "Сколько из этих утверждений ", "size": 30, "bold": True,
         "color": DEEP},
        {"text": "верны?", "size": 30, "bold": True, "color": GOLD},
    ], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Hero background: 9.9" x 5.11" = 50.6 кв.дюйма ≈ 51% площади слайда.
    # Центральная щель между колонками карточек оставлена шире (0.95"),
    # чтобы «ящик с трещинами» и «?» читались между ними.
    hero_w = 9.9
    add_image(s, ASSETS / "illustrations/s01-blackbox-cracks.png",
              x=(SLIDE_W_IN - hero_w) / 2, y=1.42, w=hero_w)

    # 6 карточек 2 колонки x 3 ряда поверх hero
    stmts = [
        "«Современные модели уже научились считать буквы в словах — strawberry давно исправили»",
        "«Роль system защищена архитектурно — подделать её из пользовательского ввода нельзя»",
        "«Окно в миллион токенов — значит, модель одинаково хорошо работает со всем этим объёмом»",
        "«temperature=0 даёт детерминированный ответ: одинаковый запрос — одинаковый результат»",
        "«Reasoning-токены не видны в ответе — значит, они и не оплачиваются»",
        "«Бенчмарки — надёжный способ выбрать модель»",
    ]
    card_w, card_h = 5.35, 1.52
    gap_x, gap_y = 0.95, 0.22
    x0 = (SLIDE_W_IN - card_w * 2 - gap_x) / 2
    y0 = 1.62
    for i, txt in enumerate(stmts):
        col, row = i % 2, i // 2
        x = x0 + col * (card_w + gap_x)
        y = y0 + row * (card_h + gap_y)
        ocean_box(s, x, y, card_w, card_h, fill=WHITE, stroke=LIGHT,
                  stroke_pt=1.4)
        # Номер — кружок MID с белой цифрой
        badge = slide_num = slide_shape = None
        shp = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x + 0.14),
                                 Inches(y + card_h / 2 - 0.21),
                                 Inches(0.42), Inches(0.42))
        shp.fill.solid(); shp.fill.fore_color.rgb = MID
        shp.line.fill.background(); disable_shadow(shp)
        tf = shp.text_frame
        tf.margin_left = Inches(0); tf.margin_right = Inches(0)
        tf.margin_top = Inches(0); tf.margin_bottom = Inches(0)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        para = tf.paragraphs[0]; para.alignment = PP_ALIGN.CENTER
        r = para.add_run(); r.text = str(i + 1)
        r.font.name = FONT_BODY; r.font.size = Pt(16); r.font.bold = True
        r.font.color.rgb = WHITE
        text_box(s, x + 0.70, y + 0.10, card_w - 0.88, card_h - 0.20, txt,
                 size=12.5, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.14)
    speaker_notes(s, load_notes("s01"))


def build_s02(p):
    """Cover v2: большая «02» outline gold + title + subtitle новой арки +
    hero motif (4-стадийная конвейер-иконка справа)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    # «02» — outline gold, декоративная, справа
    outline_big_text(s, 9.15, 0.30, 4.1, 3.4, "02", size=230,
                     align=PP_ALIGN.CENTER)
    # Тег лекции
    text_box(s, 0.7, 1.05, 8.0, 0.5, "ЛЕКЦИЯ 2", size=18, bold=True,
             color=TEAL)
    filled_rect(s, 0.72, 1.58, 0.7, 0.05, TEAL)
    # Title
    text_box(s, 0.7, 2.0, 8.6, 2.3,
             "Как работают современные\nбольшие модели",
             size=44, bold=True, color=DEEP, line_spacing=1.08)
    # Subtitle — новая арка
    filled_rect(s, 0.7, 4.55, 0.05, 0.62, GOLD)
    text_box(s, 0.95, 4.55, 10.6, 0.75,
             "Проверяем ментальную модель: конвейер inference и шесть границ",
             size=20, italic=True, color=MID, line_spacing=1.22)
    # Hero motif: 4-стадийная конвейер-иконка (токен / вектор / внимание /
    # распределение)
    icons = [("[ ]", "токен"), ("0.21", "вектор"), ("⇄", "внимание"),
             ("%", "распределение")]
    pipe_y = 5.75
    cx = 0.95
    for i, (glyph, label) in enumerate(icons):
        shp = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx), Inches(pipe_y),
                                 Inches(0.78), Inches(0.78))
        shp.fill.solid()
        shp.fill.fore_color.rgb = MID if i != 2 else TEAL
        shp.line.fill.background(); disable_shadow(shp)
        tf = shp.text_frame
        tf.margin_left = Inches(0); tf.margin_right = Inches(0)
        tf.margin_top = Inches(0); tf.margin_bottom = Inches(0)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        para = tf.paragraphs[0]; para.alignment = PP_ALIGN.CENTER
        r = para.add_run(); r.text = glyph
        r.font.name = FONT_MONO; r.font.size = Pt(15); r.font.bold = True
        r.font.color.rgb = WHITE
        text_box(s, cx - 0.45, pipe_y + 0.88, 1.7, 0.35, label,
                 size=11.5, color=LIGHT, align=PP_ALIGN.CENTER)
        if i < 3:
            right_arrow(s, cx + 0.92, pipe_y + 0.30, w=0.5, h=0.18,
                        fill=LIGHT)
        cx += 1.58
    speaker_notes(s, load_notes("s02"))


# M-чипы на карте: индекс раздела -> список меток
S02A_MCHIPS = {1: ["M1", "M2"], 3: ["M2", "M3"], 4: ["M4", "M5"], 5: ["M6"]}
S02A_ROWS = [
    ("0", "Введение", "чек-лист, рамка и конвейер целиком", True),
    ("1", "Токенизация", "как модель видит ваш текст", False),
    ("2", "Эмбеддинги", "пространство смыслов и граница похожести", False),
    ("3", "Механизм внимания", "что важно сейчас: роли, кэш, длинный контекст", False),
    ("4", "Сэмплинг", "от распределения к токену: температура, детерминизм, невидимые токены", False),
    ("5", "Финал", "сборка конвейера, ландшафт моделей, чек-лист заново", False),
]


def build_s02a(p):
    """Карта лекции v2: 6 горизонтальных карточек-СТРОК (сверху вниз, по
    источнику) + M-чипы overlay; активный Раздел 0 — gold-обводка."""
    s = blank(p)
    set_slide_bg(s, SURFACE)
    slide_title(s, "Карта лекции — 6 разделов", size=28,
                align=PP_ALIGN.CENTER, y=0.42, h=0.7)
    row_w, row_h, gap = 12.1, 0.84, 0.12
    x0 = (SLIDE_W_IN - row_w) / 2
    y = 1.35
    for i, (num, name, desc, active) in enumerate(S02A_ROWS):
        if active:
            ocean_box(s, x0, y, row_w, row_h, fill=WHITE, stroke=GOLD,
                      stroke_pt=2.5)
        else:
            ocean_box(s, x0, y, row_w, row_h, fill=WHITE, stroke=LIGHT,
                      stroke_pt=1.2)
        text_box(s, x0 + 0.25, y, 0.6, row_h, num, size=30, bold=True,
                 color=GOLD if active else LIGHT,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        text_runs(s, x0 + 1.05, y, row_w - 3.0, row_h, [
            {"text": name, "size": 17, "bold": True, "color": DEEP},
            {"text": "  —  " + desc, "size": 13.5, "italic": True,
             "color": SLATE},
        ], anchor=MSO_ANCHOR.MIDDLE)
        # M-чипы справа
        chips = S02A_MCHIPS.get(i, [])
        cx = x0 + row_w - 0.25 - 0.62 * len(chips)
        for mc in chips:
            chip(s, cx, y + row_h / 2 - 0.16, 0.54, 0.32, mc,
                 fill=GOLD_TINT, stroke=GOLD, color=DEEP, size=12)
            cx += 0.62
        y += row_h + gap
    speaker_notes(s, load_notes("s02a"))


def build_s03(p):
    """Recap-рамка: nested layers Лекции 1 (Модель gold) + 2 строки
    Известное/Сегодня."""
    s = blank(p)
    slide_title(s, "Фиксируем рамку: всё сегодняшнее — внутри слоя «модель»",
                size=26)
    # Nested layers слева, bottom-aligned (внешний = Приложение)
    base_x, bottom = 0.85, 6.75
    layers = [  # (label, w, h, fill, stroke, stroke_pt)
        ("Приложение", 5.5, 5.0, WHITE, LIGHT, 1.2),
        ("Агент", 4.6, 3.9, SURFACE, LIGHT, 1.2),
        ("Чат", 3.7, 2.8, TEAL_TINT, TEAL, 1.2),
        ("Модель", 2.8, 1.7, GOLD_TINT, GOLD, 2.2),
    ]
    for label, w, h, fill, stroke, sp in layers:
        x = base_x + (5.5 - w) / 2
        y = bottom - h
        ocean_box(s, x, y, w, h, fill=fill, stroke=stroke, stroke_pt=sp)
        text_box(s, x, y + 0.06, w, 0.4, label, size=14,
                 bold=(label == "Модель"),
                 color=DEEP if label == "Модель" else LIGHT,
                 align=PP_ALIGN.CENTER)
    # Справа — 2 строки
    ocean_box(s, 6.8, 2.0, 6.0, 1.6, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.3)
    text_runs(s, 7.0, 2.2, 5.6, 1.2, [
        {"text": "Известное: ", "size": 17, "bold": True, "color": MID},
        {"text": "модель — stateless-инференс: на вход данные, на выход "
                 "предсказание, без памяти между вызовами.", "size": 15.5,
         "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, 6.8, 4.0, 6.0, 1.6, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.10)
    text_runs(s, 7.0, 4.2, 5.6, 1.2, [
        {"text": "Сегодня: ", "size": 17, "bold": True, "color": DEEP},
        {"text": "границы точного понимания того, что внутри этого "
                 "инференса.", "size": 15.5, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s03"))


def build_s04(p):
    """Центральный вопрос v2 + 6 промис-чипов (2 ряда x 3)."""
    s = blank(p)
    slide_title(s, "Центральный вопрос лекции", size=24, color=MID)
    ocean_box(s, 0.7, 1.25, 11.93, 2.15, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 1.05, 1.45, 11.25, 1.8,
             "«Насколько точна ваша ментальная модель LLM — и какие из "
             "внутренних механизмов, которые вы знаете приблизительно, "
             "при точном понимании меняют то, как вы строите промпты, "
             "агентов и решения?»",
             size=21, bold=True, color=DEEP, line_spacing=1.25,
             anchor=MSO_ANCHOR.MIDDLE)
    promises = [
        "почему исправленный strawberry ничего не доказывает",
        "почему роль работает — и подделывается",
        "что на деле умеет окно 1M",
        "почему T=0 не даёт одинаковых ответов",
        "сколько стоят невидимые токены",
        "чем заменить веру в бенчмарки",
    ]
    card_w, card_h = 3.93, 1.15
    gap_x, gap_y = 0.27, 0.28
    x0 = (SLIDE_W_IN - card_w * 3 - gap_x * 2) / 2
    y0 = 3.85
    for i, txt in enumerate(promises):
        col, row = i % 3, i // 3
        x = x0 + col * (card_w + gap_x)
        y = y0 + row * (card_h + gap_y)
        ocean_box(s, x, y, card_w, card_h, fill=WHITE, stroke=LIGHT,
                  stroke_pt=1.2)
        filled_rect(s, x + 0.16, y + 0.18, 0.09, card_h - 0.36, GOLD)
        text_box(s, x + 0.42, y + 0.08, card_w - 0.6, card_h - 0.16, txt,
                 size=13, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.15)
    speaker_notes(s, load_notes("s04"))


def build_s04b(p):
    """Keystone: 7-стадийный inference-конвейер + пример + 4 подкарточки +
    gold callout."""
    s = blank(p)
    slide_title(s, "Поток данных в LLM — туда и обратно", size=26)
    stages = [  # (name, example, caption)
        ("Текст", "«Привет»", "слова"),
        ("Токены", "[Прив][ет]", "id из словаря"),
        ("Векторы", "vec₁, vec₂", "числа"),
        ("LLM", "внимание", "инференс"),
        ("Распределение", "p(токен | контекст)", "вероятности"),
        ("Токен", "выбран", "выбор"),
        ("Текст", "ответ", "обратно в текст"),
    ]
    n = len(stages)
    arrow_w = 0.30
    total_w = 12.5
    cell_w = (total_w - arrow_w * (n - 1)) / n
    x0 = (SLIDE_W_IN - total_w) / 2
    y0, cell_h = 1.75, 1.35
    for i, (name, ex, cap) in enumerate(stages):
        x = x0 + i * (cell_w + arrow_w)
        is_llm = (name == "LLM")
        ocean_box(s, x, y0, cell_w, cell_h,
                  fill=GOLD_TINT if is_llm else SURFACE,
                  stroke=GOLD if is_llm else LIGHT,
                  stroke_pt=2.2 if is_llm else 1.4)
        nm_sz = 13 if len(name) < 12 else 10.5
        text_box(s, x - 0.06, y0 + 0.12, cell_w + 0.12, 0.4, name,
                 size=nm_sz, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        ex_sz = 10.5 if len(ex) < 14 else 8.5
        text_box(s, x - 0.10, y0 + 0.62, cell_w + 0.20, 0.6, ex,
                 size=ex_sz, color=MID, align=PP_ALIGN.CENTER,
                 font=FONT_MONO, line_spacing=1.1)
        text_box(s, x - 0.15, y0 + cell_h + 0.08, cell_w + 0.30, 0.5, cap,
                 size=10.5, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
        if i < n - 1:
            right_arrow(s, x + cell_w + 0.03, y0 + cell_h / 2 - 0.08,
                        w=arrow_w - 0.06, h=0.16, fill=MID)
    # 4 подкарточки разделов
    subs = [("Раздел 1", "Текст → Токены"), ("Раздел 2", "Токены → Векторы"),
            ("Раздел 3", "LLM: внимание"), ("Раздел 4", "Распределение → Токен")]
    sub_w, sub_h, gap = 2.95, 0.95, 0.22
    sx0 = (SLIDE_W_IN - sub_w * 4 - gap * 3) / 2
    sy = 4.15
    for i, (nm, rng) in enumerate(subs):
        x = sx0 + i * (sub_w + gap)
        ocean_box(s, x, sy, sub_w, sub_h, fill=WHITE, stroke=TEAL,
                  stroke_pt=1.3)
        text_box(s, x, sy + 0.12, sub_w, 0.35, nm, size=13.5, bold=True,
                 color=TEAL, align=PP_ALIGN.CENTER)
        text_box(s, x, sy + 0.50, sub_w, 0.35, rng, size=12, color=DEEP,
                 align=PP_ALIGN.CENTER)
    gold_callout(s, 2.7, 5.65, 7.93, 0.75,
                 "Слова — только на границах; внутри — векторы.",
                 size=17, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s04b"))


# ============================================================
# Раздел 1 — Токенизация
# ============================================================
def build_s05a(p):
    section_divider(
        p, section_n=1, sub_title="Токенизация",
        frame_phrase="Как модель видит ваш текст",
        tag="4 разбора · 3 провала", active_stage=1, notes_id="s05a")


def token_chips_runs(pairs):
    """[(text, color)] -> run dicts моноширинно."""
    return [{"text": t, "size": 16, "bold": True, "color": c,
             "font": FONT_MONO} for t, c in pairs]


def build_s05(p):
    """3 примера разметки + gold callout + caption."""
    s = blank(p)
    slide_title(s, "Токен — id из словаря модели: не буква и не слово",
                size=26)
    rows = [
        ([("cat", DEEP)], [("[cat]", MID)], "1 токен"),
        ([("tokenization", DEEP)], [("[token]", MID), ("[ization]", TEAL)],
         "2 токена"),
        ([("клубника", DEEP)],
         [("[к]", MID), ("[луб]", TEAL), ("[ника]", LIGHT)],
         "3 токена (o200k_base)"),
    ]
    y = 1.75
    for src, toks, cnt in rows:
        ocean_box(s, 0.9, y, 11.5, 0.92, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.3)
        runs = token_chips_runs(src)
        runs.append({"text": "   →   ", "size": 16, "color": SLATE})
        runs += token_chips_runs(toks)
        runs.append({"text": "   →   ", "size": 16, "color": SLATE})
        runs.append({"text": cnt, "size": 17, "bold": True, "color": DEEP})
        text_runs(s, 1.25, y + 0.12, 10.9, 0.68, runs,
                  anchor=MSO_ANCHOR.MIDDLE)
        y += 1.12
    gold_callout(s, 0.9, 5.35, 11.5, 0.75,
                 "«В среднем: 1 токен ≈ 4 символа EN ≈ 2 символа RU»",
                 size=17, align=PP_ALIGN.CENTER)
    text_box(s, 0.9, 6.35, 11.5, 0.5,
             "Словарь и модель — два разных артефакта: словарь строится до "
             "обучения модели, отдельным алгоритмом на своём корпусе.",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s05"))


def build_s06(p):
    """BPE: 2 колонки корпус -> словарь + gold callout + caption."""
    s = blank(p)
    slide_title(s, "BPE — компромисс между алфавитом и словарём", size=26)
    text_box(s, 0.55, 1.30, 12.3, 0.5,
             "Не все буквы (длинно) и не все слова (незнакомое выпадает) — "
             "частые подпоследовательности.",
             size=16, italic=True, color=MID)
    # Левая колонка — корпус
    col_y, col_h = 2.05, 2.75
    ocean_box(s, 1.0, col_y, 4.7, col_h, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 1.3, col_y + 0.18, 4.1, 0.45, "Обучающий корпус",
             size=17, bold=True, color=MID)
    text_runs(s, 1.3, col_y + 0.75, 4.1, 2.0, [
        {"text": "low", "size": 16, "font": FONT_MONO, "color": DEEP},
        {"text": "lower", "size": 16, "font": FONT_MONO, "color": DEEP,
         "newpara": True, "space_before_pt": 6},
        {"text": "newest", "size": 16, "font": FONT_MONO, "color": DEEP,
         "newpara": True, "space_before_pt": 6},
        {"text": "widest", "size": 16, "font": FONT_MONO, "color": DEEP,
         "newpara": True, "space_before_pt": 6},
    ])
    right_arrow(s, 6.05, col_y + col_h / 2 - 0.25, w=1.1, h=0.5, fill=MID)
    # Правая колонка — BPE-словарь
    ocean_box(s, 7.5, col_y, 4.7, col_h, fill=WHITE, stroke=TEAL,
              stroke_pt=1.4)
    text_box(s, 7.8, col_y + 0.18, 4.1, 0.45, "BPE-словарь",
             size=17, bold=True, color=TEAL)
    text_runs(s, 7.8, col_y + 0.75, 4.1, 2.0, [
        {"text": "low", "size": 16, "font": FONT_MONO, "color": DEEP},
        {"text": " · ", "size": 16, "color": SLATE},
        {"text": "er", "size": 16, "font": FONT_MONO, "color": TEAL},
        {"text": " · ", "size": 16, "color": SLATE},
        {"text": "new", "size": 16, "font": FONT_MONO, "color": DEEP},
        {"text": " · ", "size": 16, "color": SLATE},
        {"text": "est", "size": 16, "font": FONT_MONO, "color": TEAL},
        {"text": " · ", "size": 16, "color": SLATE},
        {"text": "wid", "size": 16, "font": FONT_MONO, "color": DEEP},
        {"text": "+ одиночные символы, частые слоги, целые слова",
         "size": 12.5, "italic": True, "color": SLATE,
         "newpara": True, "space_before_pt": 12},
    ])
    gold_callout(s, 1.0, 5.15, 11.2, 0.80,
                 "Словарь строится один раз до обучения; на inference — "
                 "выборка готовых правил, не вычисление.", size=16,
                 align=PP_ALIGN.CENTER)
    text_box(s, 1.0, 6.25, 11.2, 0.5,
             "Разные вендоры режут один и тот же текст по-разному: Claude, "
             "GPT, Gemini — свои словари и правила.",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s06"))


def build_s07(p):
    """Chat-шаблоны: JSON -> плоский поток (спецтокены teal) + карточка
    риска gold-обводка + caption."""
    s = blank(p)
    slide_title(s, "Роли system/user/assistant — те же токены в общем потоке",
                size=25)
    # Слева: структурированный диалог
    ocean_box(s, 0.55, 1.65, 6.55, 1.45, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.3)
    text_box(s, 0.8, 1.78, 6.1, 0.4, "Структурированный диалог",
             size=14, bold=True, color=MID)
    text_runs(s, 0.8, 2.18, 6.1, 0.85, [
        {"text": '{ "role": "system",  "content": "Ты помощник…" }',
         "size": 12.5, "font": FONT_MONO, "color": DEEP},
        {"text": '{ "role": "user",  "content": "Объясни…" }',
         "size": 12.5, "font": FONT_MONO, "color": DEEP, "newpara": True,
         "space_before_pt": 4},
    ])
    # Стрелка вниз + подпись chat-шаблон
    down_arrow(s, 3.55, 3.22, w=0.45, h=0.55, fill=MID)
    text_box(s, 4.15, 3.30, 2.6, 0.4, "chat-шаблон", size=14, bold=True,
             color=MID, anchor=MSO_ANCHOR.MIDDLE)
    # Плоский поток токенов
    ocean_box(s, 0.55, 3.95, 6.55, 1.55, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.3)
    text_box(s, 0.8, 4.08, 6.1, 0.4, "Плоский поток токенов",
             size=14, bold=True, color=MID)
    text_runs(s, 0.8, 4.50, 6.1, 1.2, [
        {"text": "<|im_start|>system", "size": 12.5, "font": FONT_MONO,
         "bold": True, "color": TEAL},
        {"text": " Ты помощник… ", "size": 12.5, "font": FONT_MONO,
         "color": DEEP},
        {"text": "<|im_end|>", "size": 12.5, "font": FONT_MONO,
         "bold": True, "color": TEAL},
        {"text": "<|im_start|>user", "size": 12.5, "font": FONT_MONO,
         "bold": True, "color": TEAL, "newpara": True,
         "space_before_pt": 6},
        {"text": " Объясни… ", "size": 12.5, "font": FONT_MONO,
         "color": DEEP},
        {"text": "<|im_end|>", "size": 12.5, "font": FONT_MONO,
         "bold": True, "color": TEAL},
    ])
    # Справа: карточка риска gold-обводка
    filled_rect(s, 7.45, 1.65, 5.35, 3.85, GOLD_TINT, stroke=GOLD,
                stroke_pt=2.0, radius=True, radius_adj=0.06)
    text_box(s, 7.75, 1.90, 4.8, 0.45, "Подделка", size=18, bold=True,
             color=DEEP)
    text_box(s, 7.75, 2.45, 4.8, 2.2,
             "Внешний контент (веб-страница, файл, письмо) со строкой, "
             "похожей на разметку роли, вливается в тот же поток токенов — "
             "отдельного «защищённого канала» для ролей нет.",
             size=15, color=DEEP, line_spacing=1.25)
    text_runs(s, 7.75, 4.85, 4.8, 0.6, [
        {"text": "<|im_start|>assistant", "size": 12, "font": FONT_MONO,
         "bold": True, "color": TEAL},
        {"text": " — из письма?", "size": 12.5, "italic": True,
         "color": SLATE},
    ])
    text_box(s, 0.55, 6.35, 12.3, 0.5,
             "Почему роль при этом работает — и почему подделанная работает "
             "так же — вторая половина ответа в разделе про внимание.",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s07"))


def build_s08(p):
    """Strawberry 2026: механизм слева + 3 факт-карточки + callout."""
    s = blank(p)
    slide_title(s, "GPT-5.5 отвечает на strawberry — и ошибается на cranberry",
                size=25)
    # Слева — механизм
    ocean_box(s, 0.55, 1.7, 5.6, 3.78, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 0.85, 1.95, 5.0, 0.45, "Механизм — слепота к буквам",
             size=15, bold=True, color=MID)
    text_runs(s, 0.85, 2.55, 5.0, 1.0, [
        {"text": "strawberry", "size": 17, "font": FONT_MONO, "color": DEEP},
        {"text": "  →", "size": 17, "color": SLATE},
        {"text": "[st]", "size": 17, "font": FONT_MONO, "bold": True,
         "color": MID, "newpara": True, "space_before_pt": 8},
        {"text": "[raw]", "size": 17, "font": FONT_MONO, "bold": True,
         "color": TEAL},
        {"text": "[berry]", "size": 17, "font": FONT_MONO, "bold": True,
         "color": LIGHT},
    ])
    text_runs(s, 0.85, 3.85, 5.0, 1.0, [
        {"text": "Модель видит ", "size": 17, "color": DEEP},
        {"text": "3 токена", "size": 17, "bold": True, "color": DEEP},
        {"text": ", не 10 букв.", "size": 17, "color": DEEP},
    ])
    # Справа — 3 факт-карточки
    cards = [
        ("GPT-5.2 · дек 2025", "«в strawberry две r»", False),
        ("GPT-5.5 · апр 2026", "strawberry ✓  /  cranberry ✗ — «две r» вместо трёх", True),
        ("StrawberryBench", "847 вопросов, 7 уровней сложности — системная проверка вместо вирусного вопроса", False),
    ]
    y = 1.7
    for title, body, is_gold in cards:
        if is_gold:
            filled_rect(s, 6.5, y, 6.3, 1.1, GOLD_TINT, stroke=GOLD,
                        stroke_pt=2.0, radius=True, radius_adj=0.10)
        else:
            ocean_box(s, 6.5, y, 6.3, 1.1, fill=WHITE, stroke=LIGHT,
                      stroke_pt=1.2)
        text_box(s, 6.75, y + 0.10, 5.85, 0.38, title, size=14, bold=True,
                 color=DEEP if is_gold else MID)
        text_box(s, 6.75, y + 0.47, 5.85, 0.58, body, size=13, color=DEEP,
                 line_spacing=1.12)
        y += 1.26
    gold_callout(s, 0.55, 5.75, 12.25, 0.85,
                 "«Рваный интеллект» (jagged intelligence): успех на "
                 "впечатляющей задаче ≠ надёжность на простой.",
                 size=16, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s08"))


def build_s09(p):
    """Числа и код: 2 колонки + 3 приёма внизу."""
    s = blank(p)
    slide_title(s, "Токенизатор режет по частоте, а не по структуре",
                size=26)
    col_y, col_h = 1.7, 3.35
    # Колонка «Числа»
    ocean_box(s, 0.55, col_y, 6.0, col_h, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 0.85, col_y + 0.18, 5.4, 0.45, "Числа", size=18, bold=True,
             color=MID)
    text_runs(s, 0.85, col_y + 0.80, 5.45, 2.4, [
        {"text": "1000000", "size": 17, "font": FONT_MONO, "color": DEEP},
        {"text": " → ", "size": 17, "color": SLATE},
        {"text": "[100]", "size": 17, "font": FONT_MONO, "bold": True,
         "color": MID},
        {"text": "[000]", "size": 17, "font": FONT_MONO, "bold": True,
         "color": TEAL},
        {"text": "[0]", "size": 17, "font": FONT_MONO, "bold": True,
         "color": LIGHT},
        {"text": "Чанки по 3 цифры слева направо ≠ разряды.",
         "size": 15, "color": DEEP, "newpara": True, "space_before_pt": 12},
        {"text": "Нарезка справа налево улучшает арифметику; "
                 "задача-специфичные схемы — ", "size": 15, "color": DEEP,
         "newpara": True, "space_before_pt": 10},
        {"text": "до +33% точности", "size": 15.5, "bold": True,
         "color": GOLD},
        {"text": " к стандартной нарезке.", "size": 15, "color": DEEP},
    ], line_spacing=1.22)
    # Колонка «Код»
    ocean_box(s, 6.8, col_y, 6.0, col_h, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 7.1, col_y + 0.18, 5.4, 0.45, "Код", size=18, bold=True,
             color=TEAL)
    text_runs(s, 7.1, col_y + 0.80, 5.45, 2.4, [
        {"text": "GPT-2: ", "size": 15, "bold": True, "color": DEEP},
        {"text": "16 токенов", "size": 15.5, "bold": True, "color": MID},
        {"text": " на отступ 4-го уровня.", "size": 15, "color": DEEP},
        {"text": "GPT-4: ", "size": 15, "bold": True, "color": DEEP,
         "newpara": True, "space_before_pt": 12},
        {"text": "пробелы группами — словарь чинится, но не под все задачи "
                 "сразу.", "size": 15, "color": DEEP},
    ], line_spacing=1.22)
    # 3 приёма
    tips = ["Разделители разрядов («1 234 567»)",
            "Вычисления — в инструмент",
            "Единообразные отступы"]
    tip_w, gap = 3.95, 0.2
    x0 = (SLIDE_W_IN - tip_w * 3 - gap * 2) / 2
    for i, t in enumerate(tips):
        x = x0 + i * (tip_w + gap)
        ocean_box(s, x, 5.45, tip_w, 0.85, fill=WHITE, stroke=TEAL,
                  stroke_pt=1.3)
        text_box(s, x + 0.15, 5.53, tip_w - 0.3, 0.7, t, size=13.5,
                 bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
    speaker_notes(s, load_notes("s09"))


def build_s10(p):
    """Glitch-токены: story / механизм / факт + callout."""
    s = blank(p)
    slide_title(s, "Порядка 4% словаря — glitch-токены", size=26)
    col_y, col_h = 1.75, 3.7
    # Слева — story
    ocean_box(s, 0.55, col_y, 3.95, col_h, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 0.8, col_y + 0.18, 3.45, 0.75, "SolidGoldMagikarp (2023)",
             size=15, bold=True, color=MID, font=FONT_MONO)
    text_box(s, 0.8, col_y + 0.95, 3.45, 2.5,
             "Юзернейм с Reddit, попавший в словарь GPT: модель не могла "
             "его повторить, отвечала невпопад.",
             size=14, color=DEEP, line_spacing=1.25)
    # Центр — механизм
    ocean_box(s, 4.7, col_y, 3.95, col_h, fill=WHITE, stroke=TEAL,
              stroke_pt=1.4)
    text_box(s, 4.95, col_y + 0.18, 3.45, 0.45, "Механизм", size=15,
             bold=True, color=TEAL)
    text_runs(s, 4.95, col_y + 0.70, 3.45, 2.8, [
        {"text": "корпус словаря ≠ корпус модели", "size": 14, "bold": True,
         "color": DEEP},
        {"text": "↓", "size": 16, "bold": True, "color": TEAL,
         "newpara": True, "align": PP_ALIGN.CENTER, "space_before_pt": 4},
        {"text": "эмбеддинг токена* остаётся у случайной инициализации",
         "size": 14, "color": DEEP, "newpara": True},
        {"text": "↓", "size": 16, "bold": True, "color": TEAL,
         "newpara": True, "align": PP_ALIGN.CENTER, "space_before_pt": 4},
        {"text": "вектор «ничего не значит» в выученной геометрии",
         "size": 14, "color": DEEP, "newpara": True},
        {"text": "* числовой вектор токена; подробно — следующий раздел",
         "size": 10.5, "italic": True, "color": SLATE, "newpara": True,
         "space_before_pt": 8},
    ], line_spacing=1.15)
    # Справа — факт GlitchMiner
    ocean_box(s, 8.85, col_y, 3.95, col_h, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 9.1, col_y + 0.18, 3.45, 0.45, "GlitchMiner (AAAI 2026)",
             size=15, bold=True, color=MID)
    text_runs(s, 9.1, col_y + 0.70, 3.45, 2.8, [
        {"text": "порядка 4% словаря", "size": 17, "bold": True,
         "color": GOLD},
        {"text": " по одной из оценок;", "size": 14, "color": DEEP},
        {"text": "воспроизводится в открытых семействах Llama, Qwen, "
                 "Gemma, Phi-3, Mistral.", "size": 14, "color": DEEP,
         "newpara": True, "space_before_pt": 8},
    ], line_spacing=1.25)
    gold_callout(s, 0.55, 5.85, 12.25, 0.75,
                 "Системная особенность конвейера, не баг версии.",
                 size=17, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s10"))


def build_s11(p):
    """Стоимость языков: QuickChart bar слева + динамика и callout справа."""
    s = blank(p)
    slide_title(s, "Русский текст стоит ≈2× дороже английского", size=26)
    # Chart (980x560) — в ocean box
    box_x, box_y, box_w, box_h = 0.55, 1.7, 7.3, 4.55
    ocean_box(s, box_x, box_y, box_w, box_h, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.3)
    img_w = 6.9
    add_image(s, ASSETS / "charts/s11-tokens-per-char-v2.png",
              x=box_x + 0.2, y=box_y + 0.28, w=img_w)
    text_box(s, box_x + 0.2, box_y + 0.28 + img_w * 560 / 980 + 0.06,
             img_w, 0.35, "словари GPT-семейства",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    # Справа — динамика
    ocean_box(s, 8.15, 1.7, 4.65, 2.2, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.3)
    text_runs(s, 8.4, 1.9, 4.15, 1.8, [
        {"text": "Переход на o200k_base:", "size": 15, "bold": True,
         "color": MID},
        {"text": "примерно ", "size": 15, "color": DEEP, "newpara": True,
         "space_before_pt": 8},
        {"text": "−35%", "size": 17, "bold": True, "color": DEEP},
        {"text": " нелатинским языкам — разрыв сокращается, но не исчезает.",
         "size": 15, "color": DEEP},
    ], line_spacing=1.25)
    gold_callout(s, 8.15, 4.15, 4.65, 2.1,
                 "Любой лимит в токенах калибруйте на своём языке: "
                 "разбиение на фрагменты, max_tokens, окно.", size=15)
    speaker_notes(s, load_notes("s11"))


# ============================================================
# Раздел 2 — Эмбеддинги
# ============================================================
def build_s12a(p):
    section_divider(
        p, section_n=2, sub_title="Эмбеддинги",
        frame_phrase="Пространство смыслов — и граница похожести",
        tag="4 разбора · 1 провал", active_stage=2, notes_id="s12a")


def build_s12(p):
    """Эмбеддинг = выборка из входной таблицы."""
    s = blank(p)
    slide_title(s, "Каждому токену — вектор из входной таблицы модели",
                size=26)
    # Главная схема
    ocean_box(s, 0.55, 1.95, 8.0, 3.05, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    # [кот] чип
    chip(s, 0.95, 3.05, 1.1, 0.62, "[кот]", fill=MID, color=WHITE, size=17,
         font=FONT_MONO)
    right_arrow(s, 2.2, 3.22, w=0.55, h=0.28, fill=MID)
    # входная таблица — мини-грид 3x2
    tbl_x, tbl_y = 2.95, 2.50
    text_box(s, tbl_x - 0.15, tbl_y - 0.42, 2.6, 0.38, "входная таблица",
             size=13, bold=True, color=MID, align=PP_ALIGN.CENTER)
    for ri in range(3):
        for ci in range(2):
            fill = TEAL_TINT if ri == 1 else WHITE
            filled_rect(s, tbl_x + ci * 1.15, tbl_y + ri * 0.55, 1.1, 0.5,
                        fill, stroke=LIGHT, stroke_pt=1.0)
    text_box(s, tbl_x, tbl_y + 0.55, 1.1, 0.5, "[кот]", size=11,
             bold=True, color=DEEP, font=FONT_MONO, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, tbl_x + 1.15, tbl_y + 0.55, 1.1, 0.5, "→ вектор", size=10,
             color=TEAL, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    right_arrow(s, 5.5, 3.22, w=0.55, h=0.28, fill=MID)
    text_box(s, 6.15, 2.92, 2.3, 0.9, "[ 0.21, −0.45,\n0.88, …, 0.13 ]",
             size=14, bold=True, color=DEEP, font=FONT_MONO,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.15)
    text_box(s, 0.85, 4.45, 7.4, 0.45,
             "выучен на тренировке вместе с остальными весами; после "
             "обучения таблица фиксирована",
             size=12, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    # Mini-callout размерностей
    ocean_box(s, 8.85, 1.95, 3.95, 3.05, fill=WHITE, stroke=TEAL,
              stroke_pt=1.3)
    text_box(s, 9.1, 2.15, 3.45, 0.4, "Размерности", size=15, bold=True,
             color=TEAL)
    text_runs(s, 9.1, 2.60, 3.45, 2.1, [
        {"text": "text-embedding-3-small — 1536", "size": 13, "color": DEEP,
         "font": FONT_MONO},
        {"text": "text-embedding-3-large — 3072", "size": 13, "color": DEEP,
         "font": FONT_MONO, "newpara": True, "space_before_pt": 6},
        {"text": "внутренние размерности флагманов не публикуются; "
                 "порядок — тысячи", "size": 12.5, "italic": True,
         "color": SLATE, "newpara": True, "space_before_pt": 8},
    ], line_spacing=1.2)
    gold_callout(s, 0.55, 5.55, 12.25, 0.90,
                 "«Геометрическая близость = смысловая близость»",
                 size=18, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s12"))


def build_s13(p):
    """Три жизни эмбеддинга: 3 вертикальные карточки + callout."""
    s = blank(p)
    slide_title(s, "«Эмбеддинг» — это три разные сущности", size=26)
    cards = [
        ("1", "Входная таблица",
         "Статическая: вектор [кот] один и тот же в любом предложении. "
         "Выборка по id, контекста ещё нет.", False),
        ("2", "Контекстуальные представления",
         "После слоёв внимания: вектор каждой позиции обновлён с учётом "
         "окружения. Именно они несут «понимание» модели.", False),
        ("3", "Векторы для поиска",
         "Вектор целого текста от отдельной embedding-модели — не "
         "внутренности вашего чат-LLM. Свой продукт, своё обучение, свои "
         "лидерборды.", True),
    ]
    card_w, col_h, gap = 3.95, 3.55, 0.2
    x0 = (SLIDE_W_IN - card_w * 3 - gap * 2) / 2
    y0 = 1.7
    for i, (num, title, body, is_gold) in enumerate(cards):
        x = x0 + i * (card_w + gap)
        if is_gold:
            filled_rect(s, x, y0, card_w, col_h, GOLD_TINT, stroke=GOLD,
                        stroke_pt=2.2, radius=True, radius_adj=0.06)
        else:
            ocean_box(s, x, y0, card_w, col_h, fill=SURFACE, stroke=LIGHT,
                      stroke_pt=1.4)
        text_box(s, x + 0.25, y0 + 0.18, 0.8, 0.7, num, size=34, bold=True,
                 color=GOLD if is_gold else LIGHT)
        text_box(s, x + 0.25, y0 + 0.95, card_w - 0.5, 0.85, title,
                 size=16.5, bold=True, color=DEEP, line_spacing=1.12)
        text_box(s, x + 0.25, y0 + 1.85, card_w - 0.5, 1.6, body,
                 size=13, color=DEEP, line_spacing=1.22)
        if is_gold:
            text_box(s, x + 0.25, y0 + col_h - 0.48, card_w - 0.5, 0.4,
                     "самая частая путаница", size=11.5, italic=True,
                     bold=True, color=MID)
    gold_callout(s, 0.55, 5.65, 12.25, 0.85,
                 "Обновили LLM → переиндексировать базу НЕ надо: индекс "
                 "живёт в координатах embedding-модели.",
                 size=16, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s13"))


def build_s14(p):
    """Пространство эмбеддингов: 2D scatter (фигуры) + 3 факт-карточки."""
    s = blank(p)
    slide_title(s, "Близкие по смыслу токены лежат рядом — "
                   "в сотнях-тысячах измерений", size=24)
    # Слева — scatter в ocean box
    bx, by, bw, bh = 0.55, 1.65, 6.7, 5.0
    ocean_box(s, bx, by, bw, bh, fill=WHITE, stroke=LIGHT, stroke_pt=1.4)
    text_box(s, bx + 0.2, by + 0.12, bw - 0.4, 0.35,
             "2D-проекция (PCA-стиль)", size=12.5, italic=True,
             color=SLATE)
    # Кластер SSL (верх-лево): 2 точки
    def dot(x, y, fill, r=0.17):
        shp = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y),
                                 Inches(r * 2), Inches(r * 2))
        shp.fill.solid(); shp.fill.fore_color.rgb = fill
        shp.line.color.rgb = WHITE; shp.line.width = Pt(1.2)
        disable_shadow(shp)
    # Пунктирные «облака» кластеров
    for (ex, ey, ew, eh, lab) in [
            (1.05, 2.35, 2.9, 1.55, "кластер SSL"),
            (4.05, 4.05, 3.0, 1.55, "кластер React")]:
        ell = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(ex), Inches(ey),
                                 Inches(ew), Inches(eh))
        ell.fill.background()
        ell.line.color.rgb = LIGHT; ell.line.width = Pt(1.2)
        ell.line.dash_style = 4  # dash
        disable_shadow(ell)
    # SSL точки + подписи
    dot(1.55, 2.75, MID)
    text_box(s, 1.90, 2.62, 2.2, 0.55, "Как настроить SSL", size=11.5,
             bold=True, color=DEEP)
    dot(2.30, 3.30, MID)
    text_box(s, 2.62, 3.18, 2.3, 0.7, "Установка\nHTTPS-сертификата",
             size=11.5, bold=True, color=DEEP, line_spacing=1.05)
    # React точки + подписи
    dot(4.55, 4.45, TEAL)
    text_box(s, 4.88, 4.32, 2.3, 0.55, "Деплой React-компонента",
             size=11.5, bold=True, color=DEEP)
    dot(5.30, 5.00, TEAL)
    text_box(s, 5.60, 4.88, 2.2, 0.7, "Сборка\nReact-приложения",
             size=11.5, bold=True, color=DEEP, line_spacing=1.05)
    # Выброс — борщ
    dot(1.55, 5.75, GOLD)
    text_box(s, 1.90, 5.62, 2.0, 0.5, "Рецепт борща", size=11.5,
             bold=True, color=DEEP)
    text_box(s, 1.90, 5.95, 2.4, 0.4, "выброс — другая область",
             size=10, italic=True, color=SLATE)
    # Справа — 3 факт-карточки
    facts = [
        ("Размерность", [
            {"text": "Публичные embedding-модели: ", "size": 13,
             "color": DEEP},
            {"text": "1536–3072", "size": 14.5, "bold": True, "color": GOLD},
            {"text": " измерения; внутренние у флагманов — порядка тысяч.",
             "size": 13, "color": DEEP}]),
        ("Обучение", [
            {"text": "Координаты не задаются вручную: похожие контексты "
                     "употребления → близкие векторы.", "size": 13,
             "color": DEEP}]),
        ("Проекция", [
            {"text": "Увидеть пространство можно только через PCA/t-SNE — "
                     "2D-картинка теряет часть структуры.", "size": 13,
             "color": DEEP}]),
    ]
    y = 1.65
    for title, runs in facts:
        ocean_box(s, 7.5, y, 5.3, 1.55, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.3)
        text_box(s, 7.75, y + 0.12, 4.8, 0.4, title, size=14.5, bold=True,
                 color=MID)
        text_runs(s, 7.75, y + 0.55, 4.8, 0.9, runs, line_spacing=1.2)
        y += 1.73
    speaker_notes(s, load_notes("s14"))


# ---- s15 heatmap (нативная PowerPoint-таблица, заливка Ocean-шкалой) ----
S15_LABELS_ROW = ["Как настроить SSL", "Установка HTTPS-сертификата",
                  "Деплой React-компонента", "Сборка React-приложения",
                  "Рецепт борща"]
S15_LABELS_COL = ["SSL", "HTTPS", "React-к.", "React-п.", "Борщ"]
S15_VALS = [
    [1.00, 0.85, 0.18, 0.20, 0.08],
    [0.85, 1.00, 0.22, 0.19, 0.07],
    [0.18, 0.22, 1.00, 0.78, 0.12],
    [0.20, 0.19, 0.78, 1.00, 0.10],
    [0.08, 0.07, 0.12, 0.10, 1.00],
]


def _ocean_scale(v):
    """0..1 -> RGB по шкале SURFACE -> LIGHT -> DEEP."""
    stops = [(0.0, (0xF4, 0xF7, 0xFA)), (0.5, (0x1C, 0x72, 0x93)),
             (1.0, (0x21, 0x29, 0x5C))]
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        if v <= t1:
            f = (v - t0) / (t1 - t0)
            return RGBColor(*(int(a + (b - a) * f) for a, b in zip(c0, c1)))
    return RGBColor(*stops[-1][1])


def build_s15(p):
    """Similarity-граница: heatmap 5x5 (таблица с Ocean-заливкой) +
    failure-карточка + callout."""
    s = blank(p)
    slide_title(s, "Высокое сходство — «об одном и том же», "
                   "не «с одинаковым смыслом»", size=24)
    # Таблица 6x6
    rows, cols = 6, 6
    tx, ty, tw, th = 0.55, 1.7, 7.15, 4.35
    gtbl = s.shapes.add_table(rows, cols, Inches(tx), Inches(ty),
                              Inches(tw), Inches(th))
    tbl = gtbl.table
    tbl.first_row = False; tbl.horz_banding = False
    tbl.columns[0].width = Inches(2.55)
    for ci in range(1, 6):
        tbl.columns[ci].width = Inches((tw - 2.55) / 5)
    tbl.rows[0].height = Inches(0.55)
    for ri in range(1, 6):
        tbl.rows[ri].height = Inches((th - 0.55) / 5)

    def cell_text(cell, txt, *, size=12, bold=False, color=DEEP,
                  align=PP_ALIGN.CENTER):
        cell.margin_left = Inches(0.03); cell.margin_right = Inches(0.03)
        cell.margin_top = Inches(0.02); cell.margin_bottom = Inches(0.02)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf = cell.text_frame
        tf.word_wrap = True
        para = tf.paragraphs[0]; para.alignment = align
        r = para.add_run(); r.text = txt
        r.font.name = FONT_BODY; r.font.size = Pt(size)
        r.font.bold = bold; r.font.color.rgb = color

    # Угловая ячейка
    tbl.cell(0, 0).fill.solid()
    tbl.cell(0, 0).fill.fore_color.rgb = WHITE
    cell_text(tbl.cell(0, 0), "cosine similarity", size=10.5, bold=True,
              color=SLATE, align=PP_ALIGN.LEFT)
    # Заголовки колонок
    for ci, lab in enumerate(S15_LABELS_COL):
        c = tbl.cell(0, ci + 1)
        c.fill.solid(); c.fill.fore_color.rgb = WHITE
        cell_text(c, lab, size=11.5, bold=True, color=MID)
    # Строки
    for ri, lab in enumerate(S15_LABELS_ROW):
        c = tbl.cell(ri + 1, 0)
        c.fill.solid(); c.fill.fore_color.rgb = WHITE
        cell_text(c, lab, size=11.5, bold=True, color=MID,
                  align=PP_ALIGN.LEFT)
        for ci, v in enumerate(S15_VALS[ri]):
            cell = tbl.cell(ri + 1, ci + 1)
            cell.fill.solid()
            cell.fill.fore_color.rgb = _ocean_scale(v)
            txt_color = WHITE if v >= 0.45 else DEEP
            hot = (v in (0.85, 0.78))
            cell_text(cell, f"{v:.2f}".replace(".", ","), size=12,
                      bold=(v >= 0.7), color=txt_color)
    # Справа — failure-карточка gold
    filled_rect(s, 8.05, 1.7, 4.75, 2.6, GOLD_TINT, stroke=GOLD,
                stroke_pt=2.2, radius=True, radius_adj=0.07)
    text_runs(s, 8.35, 1.95, 4.2, 2.1, [
        {"text": "«Как настроить SSL»", "size": 15.5, "bold": True,
         "color": DEEP},
        {"text": "  ↔", "size": 15.5, "bold": True, "color": MID},
        {"text": "«Как отключить SSL»", "size": 15.5, "bold": True,
         "color": DEEP, "newpara": True, "space_before_pt": 4},
        {"text": "Очень высокое сходство — противоположный практический "
                 "смысл.", "size": 14, "color": DEEP, "newpara": True,
         "space_before_pt": 10},
    ], line_spacing=1.2)
    # Мини-легенда шкалы
    text_box(s, 8.05, 4.5, 4.75, 0.35, "шкала: 0 — светлое · 1 — тёмное",
             size=11, italic=True, color=SLATE)
    gold_callout(s, 0.55, 6.3, 12.25, 0.8,
                 "Similarity — сигнал кандидатов; релевантность — отдельная "
                 "задача: реранкер, гибрид, фильтры.",
                 size=15.5, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s15"))


def build_s17(p):
    """Сборка раздела: путь туда-обратно + 2 карточки + callout + caption."""
    s = blank(p)
    slide_title(s, "Эмбеддинги — фундамент понимания: модель работает "
                   "с векторами, не строками", size=23)
    # Слева — вертикальная схема
    bx, by, bw, bh = 0.55, 1.6, 3.5, 5.35
    ocean_box(s, bx, by, bw, bh, fill=SURFACE, stroke=LIGHT, stroke_pt=1.4)
    steps = ["слова", "токены", "векторы", "LLM", "векторы", "токены",
             "слова"]
    step_h, ar_h = 0.52, 0.15
    total = len(steps) * step_h + (len(steps) - 1) * ar_h
    yy = by + (bh - total) / 2
    for i, st in enumerate(steps):
        is_llm = (st == "LLM")
        filled_rect(s, bx + 0.55, yy, bw - 1.1, step_h,
                    GOLD if is_llm else (WHITE if i % 2 == 0 else TEAL_TINT),
                    stroke=GOLD if is_llm else LIGHT,
                    stroke_pt=1.6 if is_llm else 1.0,
                    radius=True, radius_adj=0.35)
        text_box(s, bx + 0.55, yy + 0.05, bw - 1.1, step_h - 0.1, st,
                 size=14, bold=True, color=DEEP if not is_llm else DEEP,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < len(steps) - 1:
            down_arrow(s, bx + bw / 2 - 0.09, yy + step_h + 0.01, w=0.18,
                       h=ar_h - 0.02, fill=MID)
        yy += step_h + ar_h
    # Справа — 2 карточки
    cards = [
        ("Перефразирования и синонимы",
         "«Как настроить SSL» и «Установка HTTPS-сертификата» — близкие "
         "векторы → модель отвечает одинаково; то же с «авто» и «машина»."),
        ("Межъязыковая близость",
         "«клубника» и strawberry — близкие векторы → ответ корректен "
         "независимо от языка запроса."),
    ]
    y = 1.6
    for title, body in cards:
        ocean_box(s, 4.4, y, 8.4, 1.55, fill=WHITE, stroke=LIGHT,
                  stroke_pt=1.3)
        text_box(s, 4.7, y + 0.13, 7.8, 0.4, title, size=15, bold=True,
                 color=MID)
        text_box(s, 4.7, y + 0.55, 7.8, 0.9, body, size=13.5, color=DEEP,
                 line_spacing=1.2)
        y += 1.75
    gold_callout(s, 4.4, 5.15, 8.4, 0.95,
                 "Семантическая близость на уровне предложений — основа "
                 "«понимания» переформулировок.", size=15.5)
    text_box(s, 4.4, 6.35, 8.4, 0.55,
             "Выбор embedding-модели под задачу (MTEB, матрёшечные "
             "представления) — материал для самостоятельного чтения.",
             size=12, italic=True, color=LIGHT)
    speaker_notes(s, load_notes("s17"))


# ============================================================
# Build (батч 1 = 20 слайдов; батч 2 добавит s18a…s42)
# ============================================================
BUILDERS = [
    ("s01", build_s01), ("s02", build_s02), ("s02a", build_s02a),
    ("s03", build_s03), ("s04", build_s04), ("s04b", build_s04b),
    ("s05a", build_s05a), ("s05", build_s05), ("s06", build_s06),
    ("s07", build_s07), ("s08", build_s08), ("s09", build_s09),
    ("s10", build_s10), ("s11", build_s11),
    ("s12a", build_s12a), ("s12", build_s12), ("s13", build_s13),
    ("s14", build_s14), ("s15", build_s15), ("s17", build_s17),
]


def main():
    p = setup_pres()
    print(f"Building {len(BUILDERS)} slides (batch 1)…")
    for sid, fn in BUILDERS:
        try:
            fn(p)
            print(f"  {sid} OK")
        except Exception as e:
            print(f"  {sid} FAIL: {type(e).__name__}: {e}")
            raise
    for i, slide in enumerate(p.slides):
        page_number(slide, i + 1)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    p.save(str(OUT))
    print(f"\nSaved: {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
