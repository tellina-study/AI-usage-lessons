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
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
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


def set_fill_alpha(shp, opacity_pct):
    """Полупрозрачная заливка: добавляет <a:alpha> в solidFill/srgbClr
    (opacity_pct: 0..100, 100 = непрозрачный). v2.1 — постер s01."""
    spPr = shp._element.spPr
    sf = spPr.find(A_NS + "solidFill")
    if sf is None:
        return
    srgb = sf.find(A_NS + "srgbClr")
    if srgb is None:
        return
    for el in srgb.findall(A_NS + "alpha"):
        srgb.remove(el)
    etree.SubElement(srgb, A_NS + "alpha").set(
        "val", str(int(opacity_pct * 1000)))


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


def line_arrow(slide, x1, y1, x2, y2, *, color=MID, w_pt=2.0, dash=None):
    """Прямая линия-стрелка (tailEnd triangle) — для веерных стрелок s20 и
    пунктирных коннекторов s35."""
    conn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                                      Inches(x1), Inches(y1),
                                      Inches(x2), Inches(y2))
    conn.line.color.rgb = color
    conn.line.width = Pt(w_pt)
    if dash is not None:
        conn.line.dash_style = dash
    ln = conn.line._get_or_add_ln()
    end = ln.makeelement(A_NS + "tailEnd",
                         {"type": "triangle", "w": "med", "len": "med"})
    ln.append(end)
    disable_shadow(conn)
    return conn


def plain_line(slide, x1, y1, x2, y2, *, color=LIGHT, w_pt=1.5, dash=None):
    conn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                                      Inches(x1), Inches(y1),
                                      Inches(x2), Inches(y2))
    conn.line.color.rgb = color
    conn.line.width = Pt(w_pt)
    if dash is not None:
        conn.line.dash_style = dash
    disable_shadow(conn)
    return conn


def left_arrow(slide, x, y, w=0.6, h=0.4, fill=MID):
    shp = slide.shapes.add_shape(MSO_SHAPE.LEFT_ARROW,
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
    tb = slide.shapes.add_textbox(Inches(12.15), Inches(7.16), Inches(1.1),
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
                    active_stage, notes_id, frame_bar=False,
                    frame_size=20):
    """v2.0 divider: big gold «Раздел N» + подзаголовок + frame + tag +
    pipeline_bar (актив. стадия конвейера gold). frame_bar=True — общая
    gold-рамка вокруг конвейера (s35a: полный конвейер)."""
    s = blank(p)
    set_slide_bg(s, SURFACE)
    text_box(s, 0.55, 0.95, 12.3, 2.4, f"Раздел {section_n}",
             size=140, bold=True, color=GOLD,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    text_box(s, 0.55, 3.55, 12.3, 0.75, sub_title,
             size=44, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.55, 4.40, 12.3, 0.75, f"«{frame_phrase}»",
             size=frame_size, italic=True, color=MID, align=PP_ALIGN.CENTER,
             line_spacing=1.15)
    text_box(s, 0.55, 5.25, 12.3, 0.45, tag,
             size=16, bold=True, color=TEAL, align=PP_ALIGN.CENTER)
    pipeline_bar(s, active_stage)
    if frame_bar:
        total_w = 12.3
        fx = (SLIDE_W_IN - total_w) / 2.0 - 0.14
        shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                 Inches(fx), Inches(6.62 - 0.12),
                                 Inches(total_w + 0.28), Inches(0.48 + 0.24))
        shp.fill.background()
        shp.line.color.rgb = GOLD; shp.line.width = Pt(2.2)
        try:
            shp.adjustments[0] = 0.35
        except Exception:
            pass
        disable_shadow(shp)
    speaker_notes(s, load_notes(notes_id))
    return s


# ============================================================
# Раздел 0
# ============================================================
def build_s01(p):
    """v2.1 hook-постер (#183): крупный клейм + gold «Все шесть — ложь.» +
    6 утверждений полноширинными строками (16pt) поверх hero «чёрный ящик
    с трещинами» (полупрозрачные строки — hero просвечивает)."""
    s = blank(p)
    # Постер-клейм: одна строка 30pt (влезает без переноса) + gold-строка
    text_box(s, 0.55, 0.28, 12.23, 0.62,
             "Шесть утверждений о LLM. Вы верите минимум в одно.",
             size=30, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.55, 0.94, 12.23, 0.92, "Все шесть — ложь.",
             size=46, bold=True, color=GOLD, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    # Hero background под строками: 10.2" x 5.27" ≈ 54% площади слайда
    hero_w = 10.2
    add_image(s, ASSETS / "illustrations/s01-blackbox-cracks.png",
              x=(SLIDE_W_IN - hero_w) / 2, y=2.02, w=hero_w)
    # 6 утверждений — полноширинные строки (читабельны с задней парты),
    # полупрозрачный белый фон поверх hero
    stmts = [
        "«Современные модели уже научились считать буквы в словах — strawberry давно исправили»",
        "«Роль system защищена архитектурно — подделать её из пользовательского ввода нельзя»",
        "«Окно в миллион токенов — значит, модель одинаково хорошо работает со всем этим объёмом»",
        "«temperature=0 даёт детерминированный ответ: одинаковый запрос — одинаковый результат»",
        "«Reasoning-токены не видны в ответе — значит, они и не оплачиваются»",
        "«Бенчмарки — надёжный способ выбрать модель»",
    ]
    row_w, row_h, gap = 11.7, 0.70, 0.085
    x0 = (SLIDE_W_IN - row_w) / 2
    y = 2.12
    for i, txt in enumerate(stmts):
        box = ocean_box(s, x0, y, row_w, row_h, fill=WHITE, stroke=LIGHT,
                        stroke_pt=1.1)
        set_fill_alpha(box, 86)
        shp = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x0 + 0.16),
                                 Inches(y + row_h / 2 - 0.185),
                                 Inches(0.37), Inches(0.37))
        shp.fill.solid(); shp.fill.fore_color.rgb = MID
        shp.line.fill.background(); disable_shadow(shp)
        tf = shp.text_frame
        tf.margin_left = Inches(0); tf.margin_right = Inches(0)
        tf.margin_top = Inches(0); tf.margin_bottom = Inches(0)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        para = tf.paragraphs[0]; para.alignment = PP_ALIGN.CENTER
        r = para.add_run(); r.text = str(i + 1)
        r.font.name = FONT_BODY; r.font.size = Pt(15); r.font.bold = True
        r.font.color.rgb = WHITE
        text_box(s, x0 + 0.70, y + 0.06, row_w - 0.92, row_h - 0.12, txt,
                 size=16, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.05)
        y += row_h + gap
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
             "Конвейер инференса — и шесть границ, которые меняют "
             "инженерные решения",
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
    row_w, row_h, gap = 12.1, 0.80, 0.12
    x0 = (SLIDE_W_IN - row_w) / 2
    y = 1.22
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
    # Микро-подпись к M-чипам (v2.0.2 item 8)
    text_box(s, x0, y + 0.02, row_w, 0.3,
             "M1–M6 — шесть утверждений чек-листа",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.RIGHT)
    speaker_notes(s, load_notes("s02a"))


def build_s03(p):
    """v2.1: объект рассмотрения — слой «модель»; nested layers Лекции 1
    (Модель gold) + 2 строки Слой/Сегодня."""
    s = blank(p)
    slide_title(s, "Объект сегодня — слой «модель» из четырёх слоёв Лекции 1",
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
        {"text": "Слой «модель»: ", "size": 17, "bold": True, "color": MID},
        {"text": "stateless-инференс — на вход данные, на выход "
                 "предсказание, без памяти между вызовами.", "size": 15.5,
         "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, 6.8, 4.0, 6.0, 1.6, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.10)
    text_runs(s, 7.0, 4.2, 5.6, 1.2, [
        {"text": "Сегодня: ", "size": 17, "bold": True, "color": DEEP},
        {"text": "разбираем, что происходит внутри этого инференса — и где "
                 "его устройство меняет инженерные решения.", "size": 15.5,
         "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s03"))


def build_s04(p):
    """v2.1: цель лекции (уверенная формулировка, gold на «важными
    деталями») + 6 промис-чипов (2 ряда x 3)."""
    s = blank(p)
    slide_title(s, "Цель лекции", size=24, color=MID)
    ocean_box(s, 0.7, 1.25, 11.93, 2.15, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_runs(s, 1.05, 1.45, 11.25, 1.8, [
        {"text": "«Рассмотреть, как работает языковая модель, — и "
                 "разобраться с ", "size": 22, "bold": True, "color": DEEP},
        {"text": "важными деталями", "size": 22, "bold": True,
         "color": GOLD},
        {"text": ", которые меняют то, как вы строите промпты, агентов "
                 "и решения.»", "size": 22, "bold": True, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
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
    """Keystone: 7-стадийный конвейер инференса + петля авторегрессии
    (v2.1 #183: токены по одному, каждый добавляется ко входу) + пример +
    4 подкарточки + gold callout."""
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
    y0, cell_h = 2.02, 1.35
    # Петля авторегрессии над конвейером: [Токен] (i=5) → назад к
    # [Токены] (i=1); подпись над линией
    x_from = x0 + 5 * (cell_w + arrow_w) + cell_w / 2
    x_to = x0 + 1 * (cell_w + arrow_w) + cell_w / 2
    loop_y = 1.74
    plain_line(s, x_from, y0, x_from, loop_y, color=TEAL, w_pt=2.2)
    plain_line(s, x_from, loop_y, x_to, loop_y, color=TEAL, w_pt=2.2)
    line_arrow(s, x_to, loop_y, x_to, y0 - 0.02, color=TEAL, w_pt=2.2)
    text_box(s, x_to + 0.25, loop_y - 0.36, x_from - x_to - 0.5, 0.32,
             "⟲ токены генерируются по одному; каждый добавляется ко входу",
             size=12, italic=True, bold=True, color=TEAL,
             align=PP_ALIGN.CENTER)
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
    sy = 4.38
    for i, (nm, rng) in enumerate(subs):
        x = sx0 + i * (sub_w + gap)
        ocean_box(s, x, sy, sub_w, sub_h, fill=WHITE, stroke=TEAL,
                  stroke_pt=1.3)
        text_box(s, x, sy + 0.12, sub_w, 0.35, nm, size=13.5, bold=True,
                 color=TEAL, align=PP_ALIGN.CENTER)
        text_box(s, x, sy + 0.50, sub_w, 0.35, rng, size=12, color=DEEP,
                 align=PP_ALIGN.CENTER)
    gold_callout(s, 2.7, 5.78, 7.93, 0.75,
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
    # Левая колонка — корпус (высота по контенту, v2.0.2 item 7)
    col_y, col_h = 2.05, 2.45
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
    gold_callout(s, 1.0, 4.95, 11.2, 0.80,
                 "Словарь строится один раз до обучения; на инференсе — "
                 "выборка готовых правил, не вычисление.", size=16,
                 align=PP_ALIGN.CENTER)
    text_box(s, 1.0, 6.05, 11.2, 0.5,
             "Разные вендоры режут один и тот же текст по-разному: Claude, "
             "GPT, Gemini — свои словари и правила.",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s06"))


def build_s07(p):
    """v2.1 (#183): тезис «chat-формат — соглашение поверх плоского потока»
    + JSON -> плоский поток (спецтокены teal) + карточка «протокольные роли
    ≠ роли из текста» + карточка риска gold + блок «Что с этого»."""
    s = blank(p)
    slide_title(s, "Роли system/user/assistant — те же токены в общем потоке",
                size=25, y=0.38, h=0.55)
    # Строка-тезис
    text_box(s, 0.55, 0.98, 12.3, 0.42,
             "Модель принимает один плоский поток токенов. Chat-формат — "
             "соглашение поверх него, а не часть архитектуры.",
             size=14.5, italic=True, color=MID)
    # Слева: структурированный диалог
    ocean_box(s, 0.55, 1.55, 6.55, 1.35, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.3)
    text_box(s, 0.8, 1.66, 6.1, 0.4, "Структурированный диалог",
             size=14, bold=True, color=MID)
    text_runs(s, 0.8, 2.05, 6.1, 0.8, [
        {"text": '{ "role": "system",  "content": "Ты помощник…" }',
         "size": 12.5, "font": FONT_MONO, "color": DEEP},
        {"text": '{ "role": "user",  "content": "Объясни…" }',
         "size": 12.5, "font": FONT_MONO, "color": DEEP, "newpara": True,
         "space_before_pt": 4},
    ])
    # Стрелка вниз + подпись chat-шаблон
    down_arrow(s, 3.55, 2.98, w=0.42, h=0.5, fill=MID)
    text_box(s, 4.12, 3.05, 2.6, 0.4, "chat-шаблон", size=14, bold=True,
             color=MID, anchor=MSO_ANCHOR.MIDDLE)
    # Плоский поток токенов
    ocean_box(s, 0.55, 3.60, 6.55, 1.50, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.3)
    text_box(s, 0.8, 3.72, 6.1, 0.4, "Плоский поток токенов",
             size=14, bold=True, color=MID)
    text_runs(s, 0.8, 4.12, 6.1, 1.0, [
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
    # Справа сверху: протокольные роли ≠ «роли» из текста
    ocean_box(s, 7.45, 1.55, 5.35, 1.78, fill=WHITE, stroke=TEAL,
              stroke_pt=1.4)
    text_box(s, 7.72, 1.68, 4.85, 0.4,
             "Протокольные роли ≠ «роли» из текста", size=14.5, bold=True,
             color=TEAL)
    text_box(s, 7.72, 2.10, 4.85, 1.15,
             "system/user/assistant — структура диалога, собранная "
             "спецтокенами. «Ты — лучший разработчик» в тексте промпта — "
             "просто содержимое сообщения, не протокольная роль.",
             size=12.5, color=DEEP, line_spacing=1.18)
    # Справа снизу: карточка риска gold-обводка
    filled_rect(s, 7.45, 3.48, 5.35, 1.62, GOLD_TINT, stroke=GOLD,
                stroke_pt=2.0, radius=True, radius_adj=0.06)
    text_box(s, 7.72, 3.58, 4.85, 0.38, "Подделка", size=15, bold=True,
             color=DEEP)
    text_box(s, 7.72, 3.96, 4.85, 0.82,
             "Внешний контент (веб-страница, файл, письмо) со строкой, "
             "похожей на разметку роли, вливается в тот же поток — "
             "отдельного «защищённого канала» нет.",
             size=12, color=DEEP, line_spacing=1.14)
    text_runs(s, 7.72, 4.78, 4.85, 0.3, [
        {"text": "<|im_start|>assistant", "size": 11.5, "font": FONT_MONO,
         "bold": True, "color": TEAL},
        {"text": " — из письма?", "size": 12, "italic": True,
         "color": SLATE},
    ])
    # Блок «Что с этого»
    ocean_box(s, 0.55, 5.30, 12.25, 0.88, fill=SURFACE, stroke=MID,
              stroke_pt=1.4)
    text_runs(s, 0.85, 5.40, 11.7, 0.7, [
        {"text": "Что с этого: ", "size": 13.5, "bold": True, "color": MID},
        {"text": "фильтруйте внешний контент до попадания в контекст "
                 "(экранирование, детекция спецтокенов)  ·  при локальном "
                 "запуске проверяйте chat-шаблон — модель с чужим шаблоном "
                 "молча глупеет.", "size": 13.5, "color": DEEP},
    ], line_spacing=1.2)
    text_box(s, 0.55, 6.40, 12.3, 0.45,
             "Почему роль при этом работает — и почему подделанная работает "
             "так же — в разделе про внимание.",
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
    gold_callout(s, 0.55, 5.62, 12.25, 0.85,
                 "«Рваный интеллект» (jagged intelligence): уровень навыка "
                 "задаётся данными обучения, а не «общим умом» — модель "
                 "берёт олимпиадное золото и проваливает подсчёт букв.",
                 size=14.5, align=PP_ALIGN.CENTER)
    text_runs(s, 0.55, 6.60, 12.25, 0.4, [
        {"text": "Что делать: ", "size": 13.5, "bold": True, "color": MID},
        {"text": "тестируйте «cranberry своей предметки» — редкие случаи, "
                 "на которых никто не хайпил; вирусное прохождение ≠ навык.",
         "size": 13.5, "color": DEEP},
    ], align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s08"))


def build_s09(p):
    """Числа и код: строка-мотивация (v2.1 #183) + 2 колонки + блок
    «Что делать» внизу."""
    s = blank(p)
    slide_title(s, "Токенизатор режет по частоте, а не по структуре",
                size=26, y=0.42, h=0.6)
    text_box(s, 0.55, 1.08, 12.3, 0.42,
             "Числа и код — самые частые «нетекстовые» входы: от их нарезки "
             "зависят арифметика модели и ваш бюджет токенов.",
             size=14.5, italic=True, color=MID)
    col_y, col_h = 1.62, 3.30
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
    # 3 приёма + заголовок группы (v2.0.2 item 9)
    text_box(s, 0.55, 5.10, 4.0, 0.32, "Что делать:", size=14, bold=True,
             color=MID)
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
    """Glitch-токены: story / механизм / факт + блок «Что на практике»
    (v2.1 #183: диагностика + санитизация) + footer-строка."""
    s = blank(p)
    slide_title(s, "Порядка 4% словаря — glitch-токены", size=26, y=0.42,
                h=0.6)
    col_y, col_h = 1.18, 3.42
    # Слева — story
    ocean_box(s, 0.55, col_y, 3.95, col_h, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 0.8, col_y + 0.16, 3.45, 0.75, "SolidGoldMagikarp (2023)",
             size=14.5, bold=True, color=MID, font=FONT_MONO)
    text_box(s, 0.8, col_y + 0.90, 3.45, 2.4,
             "Юзернейм с Reddit, попавший в словарь GPT: модель не могла "
             "его повторить и отвечала невпопад — будто слова не существует.",
             size=13.5, color=DEEP, line_spacing=1.22)
    # Центр — механизм
    ocean_box(s, 4.7, col_y, 3.95, col_h, fill=WHITE, stroke=TEAL,
              stroke_pt=1.4)
    text_box(s, 4.95, col_y + 0.16, 3.45, 0.45, "Механизм", size=14.5,
             bold=True, color=TEAL)
    text_runs(s, 4.95, col_y + 0.62, 3.45, 2.7, [
        {"text": "корпус словаря ≠ корпус модели", "size": 13, "bold": True,
         "color": DEEP},
        {"text": "↓", "size": 14, "bold": True, "color": TEAL,
         "newpara": True, "align": PP_ALIGN.CENTER, "space_before_pt": 3},
        {"text": "эмбеддинг токена* остаётся у случайной инициализации",
         "size": 13, "color": DEEP, "newpara": True},
        {"text": "↓", "size": 14, "bold": True, "color": TEAL,
         "newpara": True, "align": PP_ALIGN.CENTER, "space_before_pt": 3},
        {"text": "вектор «ничего не значит» в выученной геометрии",
         "size": 13, "color": DEEP, "newpara": True},
        {"text": "* числовой вектор токена; подробно — следующий раздел",
         "size": 10, "italic": True, "color": SLATE, "newpara": True,
         "space_before_pt": 6},
    ], line_spacing=1.12)
    # Справа — факт GlitchMiner
    ocean_box(s, 8.85, col_y, 3.95, col_h, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 9.1, col_y + 0.16, 3.45, 0.45, "GlitchMiner (AAAI 2026)",
             size=14.5, bold=True, color=MID)
    text_runs(s, 9.1, col_y + 0.62, 3.45, 2.7, [
        {"text": "порядка 4% словаря", "size": 16, "bold": True,
         "color": GOLD},
        {"text": " по одной из оценок;", "size": 13.5, "color": DEEP},
        {"text": "воспроизводится в открытых семействах Llama, Qwen, "
                 "Gemma, Phi-3, Mistral.", "size": 13.5, "color": DEEP,
         "newpara": True, "space_before_pt": 8},
    ], line_spacing=1.22)
    # Блок «Что на практике» — 2 карточки
    text_box(s, 0.55, 4.76, 5.0, 0.35, "Что на практике:", size=14,
             bold=True, color=MID)
    ocean_box(s, 0.55, 5.14, 6.0, 1.15, fill=WHITE, stroke=TEAL,
              stroke_pt=1.3)
    text_box(s, 0.8, 5.24, 5.55, 0.95,
             "Необъяснимое поведение на экзотических строках (редкие "
             "идентификаторы, обфусцированный текст, необычный Unicode)? "
             "Гипотеза: glitch-токен. Проверка: замените строку "
             "плейсхолдером.",
             size=12.5, color=DEEP, line_spacing=1.14)
    ocean_box(s, 6.8, 5.14, 6.0, 1.15, fill=WHITE, stroke=TEAL,
              stroke_pt=1.3)
    text_box(s, 7.05, 5.24, 5.55, 0.95,
             "В продуктах, принимающих произвольный ввод, — нормализация "
             "и санитизация входа до модели.",
             size=12.5, color=DEEP, line_spacing=1.14,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.55, 6.48, 12.25, 0.4,
             "Системная особенность конвейера, не баг версии — масштабом "
             "не чинится.",
             size=12.5, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
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
    # Блок «Что делать» (v2.1 #183): калибровка на своём языке + когда
    # выгоден перевод на английский
    filled_rect(s, 8.15, 4.15, 4.65, 2.35, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    text_runs(s, 8.38, 4.32, 4.2, 2.05, [
        {"text": "Что делать:", "size": 14, "bold": True, "color": MID},
        {"text": "•  Калибруйте лимиты в токенах на своём языке: фрагменты "
                 "для поиска, max_tokens, бюджет окна.", "size": 12.5,
         "color": DEEP, "newpara": True, "space_before_pt": 6},
        {"text": "•  Пакетная обработка больших объёмов — оцените перевод "
                 "на английский (≈2× дешевле); в интерактиве разница того "
                 "не стоит.", "size": 12.5, "color": DEEP, "newpara": True,
         "space_before_pt": 6},
    ], line_spacing=1.18)
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
    gold_callout(s, 0.55, 5.55, 12.25, 0.62,
                 "«Геометрическая близость = смысловая близость»",
                 size=17, align=PP_ALIGN.CENTER)
    text_runs(s, 0.55, 6.28, 12.25, 0.5, [
        {"text": "Что делать: ", "size": 13, "bold": True, "color": TEAL},
        {"text": "опечатка или другой регистр — уже другой токен и другой "
                 "вектор; нормализуйте вход до эмбеддинга.", "size": 13,
         "color": DEEP},
    ], align=PP_ALIGN.CENTER, line_spacing=1.15)
    speaker_notes(s, load_notes("s12"))


def build_s13(p):
    """v2.1 (#183): эмбеддинги — не только внутренность инференса, но и
    инструмент поиска; три жизни от практики (3-я — gold, «ваш поиск/RAG»)
    + callout про переиндексацию."""
    s = blank(p)
    slide_title(s, "Эмбеддинги — не только внутренность инференса, "
                   "но и инструмент поиска", size=21.5, y=0.45, h=0.55)
    text_box(s, 0.55, 1.08, 12.3, 0.42,
             "Когда вы строите поиск или RAG, вы пользуетесь третьей жизнью "
             "термина «эмбеддинг» — отдельной embedding-моделью.",
             size=14.5, italic=True, color=MID)
    cards = [
        ("1", "Входная таблица", "внутри инференса",
         "Статическая: вектор [кот] один и тот же в любом предложении. "
         "Выборка по id, контекста ещё нет.", False),
        ("2", "Контекстуальные представления", "внутри инференса",
         "После слоёв внимания: вектор каждой позиции обновлён с учётом "
         "окружения. Именно они несут «понимание» модели.", False),
        ("3", "Векторы для поиска", "самостоятельный инструмент",
         "Вектор целого текста от отдельной embedding-модели — не "
         "внутренности вашего чат-LLM. Свой продукт, своё обучение, свои "
         "лидерборды.", True),
    ]
    card_w, col_h, gap = 3.95, 3.62, 0.2
    x0 = (SLIDE_W_IN - card_w * 3 - gap * 2) / 2
    y0 = 1.68
    for i, (num, title, sub, body, is_gold) in enumerate(cards):
        x = x0 + i * (card_w + gap)
        if is_gold:
            filled_rect(s, x, y0, card_w, col_h, GOLD_TINT, stroke=GOLD,
                        stroke_pt=2.2, radius=True, radius_adj=0.06)
        else:
            ocean_box(s, x, y0, card_w, col_h, fill=SURFACE, stroke=LIGHT,
                      stroke_pt=1.4)
        text_box(s, x + 0.25, y0 + 0.14, 0.8, 0.65, num, size=32, bold=True,
                 color=GOLD if is_gold else LIGHT)
        text_box(s, x + 0.25, y0 + 0.82, card_w - 0.5, 0.8, title,
                 size=16, bold=True, color=DEEP, line_spacing=1.1)
        text_box(s, x + 0.25, y0 + 1.62, card_w - 0.5, 0.35, sub,
                 size=11.5, italic=True, color=MID if is_gold else SLATE)
        text_box(s, x + 0.25, y0 + 2.02, card_w - 0.5, 1.5, body,
                 size=13, color=DEEP, line_spacing=1.2)
        if is_gold:
            text_box(s, x + 0.25, y0 + col_h - 0.44, card_w - 0.5, 0.38,
                     "это и есть ваш поиск/RAG", size=11.5, italic=True,
                     bold=True, color=MID)
    gold_callout(s, 0.55, 5.72, 12.25, 0.85,
                 "Обновили чат-LLM → переиндексировать базу НЕ надо: индекс "
                 "живёт в координатах embedding-модели.",
                 size=16, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s13"))


def build_s14(p):
    """v2.1 (#183): 2D scatter с подписанными осями-признаками (возврат
    иллюстрации размерности) + 3 факт-карточки."""
    s = blank(p)
    slide_title(s, "Близкие по смыслу токены лежат рядом — "
                   "в сотнях-тысячах измерений", size=24)
    # Слева — scatter в ocean box
    bx, by, bw, bh = 0.55, 1.65, 6.7, 5.0
    ocean_box(s, bx, by, bw, bh, fill=WHITE, stroke=LIGHT, stroke_pt=1.4)
    text_box(s, bx + 0.2, by + 0.12, 2.6, 0.35,
             "2D-проекция (PCA-стиль)", size=12.5, italic=True,
             color=SLATE)
    text_box(s, bx + 2.5, by + 0.12, bw - 2.7, 0.55,
             "каждая из 1536+ осей — выученный признак; здесь показаны две",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.RIGHT,
             line_spacing=1.05)
    # Оси-признаки (v2.1: возврат подписей осей)
    ax_x, ax_y = 1.02, 6.02  # начало координат (низ-лево)
    line_arrow(s, ax_x, ax_y, bx + bw - 0.25, ax_y, color=LIGHT, w_pt=1.8)
    line_arrow(s, ax_x, ax_y, ax_x, by + 0.62, color=LIGHT, w_pt=1.8)
    text_box(s, ax_x + 0.1, ax_y + 0.10, bw - 0.9, 0.32,
             "ось ≈ признак: тематика (веб-разработка ↔ кулинария)",
             size=10.5, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, ax_x + 0.12, by + 0.62, 3.6, 0.32,
             "ось ≈ признак: инфраструктура ↔ фронтенд",
             size=10.5, italic=True, color=LIGHT)
    # Точки
    def dot(x, y, fill, r=0.17):
        shp = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y),
                                 Inches(r * 2), Inches(r * 2))
        shp.fill.solid(); shp.fill.fore_color.rgb = fill
        shp.line.color.rgb = WHITE; shp.line.width = Pt(1.2)
        disable_shadow(shp)
    # Пунктирные «облака» кластеров: SSL — верх-лево (инфраструктура),
    # React — низ-лево (фронтенд); борщ — справа (кулинария)
    for (ex, ey, ew, eh) in [(1.35, 2.55, 2.95, 1.5),
                             (1.55, 4.25, 3.05, 1.5)]:
        ell = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(ex), Inches(ey),
                                 Inches(ew), Inches(eh))
        ell.fill.background()
        ell.line.color.rgb = LIGHT; ell.line.width = Pt(1.2)
        ell.line.dash_style = 4  # dash
        disable_shadow(ell)
    # SSL точки + подписи
    dot(1.80, 2.85, MID)
    text_box(s, 2.15, 2.72, 2.2, 0.55, "Как настроить SSL", size=11.5,
             bold=True, color=DEEP)
    dot(2.45, 3.42, MID)
    text_box(s, 2.78, 3.30, 2.3, 0.7, "Установка\nHTTPS-сертификата",
             size=11.5, bold=True, color=DEEP, line_spacing=1.05)
    # React точки + подписи
    dot(2.00, 4.55, TEAL)
    text_box(s, 2.35, 4.42, 2.3, 0.55, "Деплой React-компонента",
             size=11.5, bold=True, color=DEEP)
    dot(2.70, 5.12, TEAL)
    text_box(s, 3.02, 5.00, 2.2, 0.7, "Сборка\nReact-приложения",
             size=11.5, bold=True, color=DEEP, line_spacing=1.05)
    # Выброс — борщ (справа: кулинария)
    dot(5.65, 3.95, GOLD)
    text_box(s, 5.30, 4.35, 1.8, 0.4, "Рецепт борща", size=11.5,
             bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, 5.05, 4.62, 2.3, 0.4, "выброс — другая область",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
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
        ocean_box(s, 7.5, y, 5.3, 1.42, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.3)
        text_box(s, 7.75, y + 0.12, 4.8, 0.4, title, size=14.5, bold=True,
                 color=MID)
        text_runs(s, 7.75, y + 0.52, 4.8, 0.85, runs, line_spacing=1.18)
        y += 1.56
    gold_callout(s, 7.5, y + 0.08, 5.3, 1.0,
                 "Что делать: близость измерима расстоянием — фильтрация "
                 "и кластеризация без разметки и без LLM возможны прямо "
                 "на векторах, дёшево.", size=12.5, align=PP_ALIGN.LEFT)
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
    gold_callout(s, 4.4, 5.15, 8.4, 0.72,
                 "Семантическая близость на уровне предложений — основа "
                 "«понимания» переформулировок.", size=14.5)
    text_runs(s, 4.4, 5.97, 8.4, 0.75, [
        {"text": "Что делать: ", "size": 12.5, "bold": True, "color": TEAL},
        {"text": "одна embedding-модель и индекс обслуживают поиск, "
                 "кластеризацию и RAG сразу — смена модели означает "
                 "переиндексацию всего хранилища; выбирайте как "
                 "инфраструктурное решение.", "size": 12.5, "color": DEEP},
    ], line_spacing=1.15)
    text_box(s, 4.4, 6.85, 8.4, 0.45,
             "Выбор embedding-модели под задачу (MTEB, матрёшечные "
             "представления) — материал для самостоятельного чтения.",
             size=11.5, italic=True, color=LIGHT)
    speaker_notes(s, load_notes("s17"))


# ============================================================
# БАТЧ 2 — Раздел 3. Механизм внимания
# ============================================================
def build_s18a(p):
    section_divider(
        p, section_n=3, sub_title="Механизм внимания",
        frame_phrase="Как модель решает, на что опереться в контексте — и "
                     "что из этого следует для ролей, кэша и длинных окон",
        tag="4 разбора · 2 провала", active_stage=3, notes_id="s18a",
        frame_size=18)


S18_TOKENS = ["Кот", "съел", "мышь", "потому что", "она", "была", "голодна"]
S18_VALS = [
    [1.0, 0.3, 0.2, 0.1, 0.1, 0.1, 0.0],
    [0.4, 1.0, 0.5, 0.1, 0.1, 0.1, 0.1],
    [0.2, 0.4, 1.0, 0.1, 0.1, 0.0, 0.1],
    [0.1, 0.2, 0.2, 1.0, 0.3, 0.2, 0.2],
    [0.1, 0.1, 0.7, 0.2, 1.0, 0.3, 0.4],
    [0.1, 0.2, 0.2, 0.3, 0.4, 1.0, 0.5],
    [0.1, 0.2, 0.3, 0.3, 0.4, 0.5, 1.0],
]


def build_s18(p):
    """Attention-матрица 7×7 (нативная таблица, Ocean-шкала, «она»→«мышь»
    gold) + 3 свойства + callout."""
    s = blank(p)
    slide_title(s, "Внимание — это сверка каждого токена со всеми остальными",
                size=25, h=0.6)
    text_box(s, 0.55, 1.02, 12.3, 0.4,
             "Каждый токен «смотрит» на все остальные одновременно. "
             "На каждом шаге — N × N связей.",
             size=14, italic=True, color=MID)
    # Таблица 8×8
    rows, cols = 8, 8
    tx, ty, tw, th = 0.55, 1.55, 7.5, 3.95
    first_col = 1.30
    gtbl = s.shapes.add_table(rows, cols, Inches(tx), Inches(ty),
                              Inches(tw), Inches(th))
    tbl = gtbl.table
    tbl.first_row = False; tbl.horz_banding = False
    tbl.columns[0].width = Inches(first_col)
    for ci in range(1, 8):
        tbl.columns[ci].width = Inches((tw - first_col) / 7)
    tbl.rows[0].height = Inches(0.55)
    for ri in range(1, 8):
        tbl.rows[ri].height = Inches((th - 0.55) / 7)

    def cell_text(cell, txt, *, size=10.5, bold=False, color=DEEP,
                  align=PP_ALIGN.CENTER):
        cell.margin_left = Inches(0.02); cell.margin_right = Inches(0.02)
        cell.margin_top = Inches(0.01); cell.margin_bottom = Inches(0.01)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf = cell.text_frame
        tf.word_wrap = True
        para = tf.paragraphs[0]; para.alignment = align
        r = para.add_run(); r.text = txt
        r.font.name = FONT_BODY; r.font.size = Pt(size)
        r.font.bold = bold; r.font.color.rgb = color

    c00 = tbl.cell(0, 0)
    c00.fill.solid(); c00.fill.fore_color.rgb = WHITE
    cell_text(c00, "вес", size=9.5, bold=True, color=SLATE)
    for ci, lab in enumerate(S18_TOKENS):
        c = tbl.cell(0, ci + 1)
        c.fill.solid(); c.fill.fore_color.rgb = WHITE
        cell_text(c, lab, size=9.5, bold=True, color=MID)
    for ri, lab in enumerate(S18_TOKENS):
        c = tbl.cell(ri + 1, 0)
        c.fill.solid(); c.fill.fore_color.rgb = WHITE
        cell_text(c, lab, size=10, bold=True, color=MID,
                  align=PP_ALIGN.LEFT)
        for ci, v in enumerate(S18_VALS[ri]):
            cell = tbl.cell(ri + 1, ci + 1)
            cell.fill.solid()
            is_gold = (ri == 4 and ci == 2)
            is_future = (ci > ri)  # верхний треугольник — будущие токены
            if is_gold:
                cell.fill.fore_color.rgb = GOLD
                cell_text(cell, "0,7", size=11, bold=True, color=DEEP)
            elif is_future:
                # Засерён (v2.0.2 item 4): в декодере токен не видит будущих
                cell.fill.fore_color.rgb = SOFT_GREY
                cell_text(cell, f"{v:.1f}".replace(".", ","), size=9,
                          color=SLATE)
            else:
                cell.fill.fore_color.rgb = _ocean_scale(v)
                cell_text(cell, f"{v:.1f}".replace(".", ","), size=10,
                          bold=(v >= 0.7),
                          color=WHITE if v >= 0.45 else DEEP)
    text_runs(s, 0.55, 5.62, 7.5, 0.8, [
        {"text": "По строке «она»: ", "size": 12.5, "bold": True,
         "color": DEEP},
        {"text": "наибольший вес — на «мышь». Статистическая связь, "
                 "выученная на корпусе.", "size": 12.5, "color": DEEP},
        {"text": "В декодере токен видит только предыдущие — показана "
                 "полная сверка для наглядности.", "size": 11.5,
         "italic": True, "color": SLATE, "newpara": True,
         "space_before_pt": 3},
    ], line_spacing=1.12)
    # Справа — 3 свойства
    props = [
        ("Размерность", [
            {"text": "N × N, где N — длина контекста. Удвоение контекста — ",
             "size": 12.5, "color": DEEP},
            {"text": "учетверение вычислений внимания", "size": 12.5,
             "bold": True, "color": DEEP},
            {"text": ".", "size": 12.5, "color": DEEP}]),
        ("На каждом шаге", [
            {"text": "Распределение весов пересчитывается заново на каждом "
                     "шаге генерации.", "size": 12.5, "color": DEEP}]),
        ("Многоголовость", [
            {"text": "В каждом слое — десятки параллельных «голов» (типично "
                     "32–128); каждая ловит свой тип связей: грамматика, "
                     "семантика, дальние зависимости.", "size": 12.5,
             "color": DEEP}]),
    ]
    y = 1.55
    for title, runs in props:
        ocean_box(s, 8.3, y, 4.5, 1.48, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.3)
        text_box(s, 8.55, y + 0.10, 4.0, 0.38, title, size=14, bold=True,
                 color=MID)
        text_runs(s, 8.55, y + 0.50, 4.0, 0.9, runs, line_spacing=1.15)
        y += 1.62
    gold_callout(s, 0.55, 6.45, 12.25, 0.70,
                 "Внимание — матричная операция: каждый токен против "
                 "каждого. Отсюда квадратичная стоимость длинного контекста.",
                 size=15, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s18"))


def build_s19(p):
    """v2.0.2 (item 2): главный тезис Q/K/V наверху — gold callout под
    заголовком + строка Q/K/V; ниже chart (7 токенов — нарезка s18) +
    3 нумерованных факта; метафора фонарика — одна строка-подпись."""
    s = blank(p)
    slide_title(s, "Внимание — распределение весов на весь контекст: "
                   "три проекции Query / Key / Value", size=20, h=0.65,
                y=0.35)
    # Главный тезис — сразу под заголовком (gold)
    gold_callout(s, 0.55, 1.06, 12.25, 0.6,
                 "Q — про текущий шаг. K и V — про уже обработанный контекст.",
                 size=15.5, align=PP_ALIGN.CENTER)
    # Строка Q/K/V — три плашки
    qkv = [("Query", "«что я сейчас ищу»"),
           ("Key", "«что я предлагаю»"),
           ("Value", "«что я отдам, если меня выбрали»")]
    x = 0.55
    for term, phrase in qkv:
        ocean_box(s, x, 1.84, 3.95, 0.58, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.2)
        text_runs(s, x + 0.18, 1.84, 3.65, 0.58, [
            {"text": term, "size": 13.5, "bold": True, "color": MID,
             "font": FONT_MONO},
            {"text": " — " + phrase, "size": 12, "color": DEEP},
        ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
        x += 4.15
    # Слева — chart (7 токенов, та же нарезка предложения, что в s18)
    ocean_box(s, 0.55, 2.62, 7.9, 3.55, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.3)
    text_box(s, 0.85, 2.76, 7.3, 0.35,
             "Распределение весов на токенах контекста — сумма = 1",
             size=13.5, bold=True, color=MID)
    add_image(s, ASSETS / "charts/s19-attention-weights.png",
              x=1.0, y=3.22, w=7.0)
    # Справа — 3 нумерованных факта
    triples = [
        ("1", "На вход — все токены контекста."),
        ("2", "На выходе — распределение весов, сумма = 1."),
        ("3", "Пересчитывается на каждом шаге генерации."),
    ]
    yy = 2.62
    for num, txt in triples:
        ocean_box(s, 8.65, yy, 4.15, 1.05, fill=WHITE, stroke=TEAL,
                  stroke_pt=1.2)
        text_runs(s, 8.85, yy, 3.8, 1.05, [
            {"text": num + ".  ", "size": 14, "bold": True, "color": TEAL},
            {"text": txt, "size": 12.5, "color": DEEP},
        ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.12)
        yy += 1.25
    # Метафора фонарика — одна строка-подпись (блок убран, v2.0.2)
    text_box(s, 0.55, 6.4, 12.3, 0.45,
             "Метафора: фонарик в тёмной комнате — луч направлен на "
             "релевантные токены, яркость света = вес внимания.",
             size=12.5, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s19"))


def build_s20(p):
    """Worked example «она»→«мышь» (веер стрелок) + 2 колонки роль/подделка
    + gold callout (закрытие M2)."""
    s = blank(p)
    slide_title(s, "Роль работает через вес во внимании — и ровно поэтому "
                   "подделанная роль работает так же", size=20, h=0.65,
                y=0.32)
    # Верхний box: рабочий пример
    ocean_box(s, 0.55, 1.12, 12.25, 2.45, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 0.85, 1.24, 5.5, 0.4, "Рабочий пример: куда смотрит «она»",
             size=14, bold=True, color=MID)
    # Токены предложения — отдельные боксы для стрелок
    seg = [("«Кот съел", 2.35, 1.55, False),
           ("мышь", 3.95, 0.95, True),
           (", потому что", 4.85, 1.85, False),
           ("она", 6.75, 0.72, True),
           ("была", 7.50, 0.95, False),
           ("голодна»", 8.45, 1.55, False)]
    for txt, x, w, bold in seg:
        text_box(s, x, 1.72, w, 0.45, txt, size=19, bold=bold,
                 color=DEEP if not bold else MID)
    # Стрелки от «она» (x≈7.0) к целям
    line_arrow(s, 7.00, 2.19, 4.45, 2.59, color=GOLD, w_pt=4.0)
    line_arrow(s, 7.15, 2.19, 7.95, 2.59, color=MID, w_pt=2.2)
    line_arrow(s, 7.25, 2.19, 9.15, 2.59, color=LIGHT, w_pt=1.2)
    text_box(s, 3.0, 2.64, 2.4, 0.32, "главный вес", size=11.5, bold=True,
             color=GOLD)
    text_box(s, 0.85, 3.0, 6.8, 0.5,
             "Упрощение: агрегат сотен связей в десятках слоёв. Модель не "
             "делает грамматический разбор — она воспроизводит корреляции "
             "употребления.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.1)
    text_runs(s, 7.85, 2.82, 4.7, 0.7, [
        {"text": "Подумайте 30 секунд: ", "size": 12, "bold": True,
         "color": DEEP},
        {"text": "куда уйдёт вес от «она» в «Программа упала, потому что "
                 "она забыла обработать null»?", "size": 12, "color": DEEP},
    ], line_spacing=1.12)
    # Нижние 2 колонки + «=»
    ocean_box(s, 0.55, 3.75, 5.7, 1.85, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.3)
    text_box(s, 0.85, 3.9, 5.1, 0.4, "Роль работает", size=16, bold=True,
             color=MID)
    text_runs(s, 0.85, 4.35, 5.15, 1.2, [
        {"text": "«Ты ", "size": 12.5, "color": DEEP},
        {"text": "эксперт по Python", "size": 12.5, "bold": True,
         "color": TEAL},
        {"text": ". Объясни асинхронность ", "size": 12.5, "color": DEEP},
        {"text": "джуниору", "size": 12.5, "bold": True, "color": TEAL},
        {"text": "» — токены роли получают вес при генерации каждого токена "
                 "ответа → конкретнее, проще, в экспертном регистре.",
         "size": 12.5, "color": DEEP},
    ], line_spacing=1.18)
    text_box(s, 6.35, 4.35, 0.7, 0.7, "=", size=38, bold=True, color=GOLD,
             align=PP_ALIGN.CENTER)
    ocean_box(s, 7.1, 3.75, 5.7, 1.85, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.3)
    text_box(s, 7.4, 3.9, 5.1, 0.4, "Подделка работает так же", size=16,
             bold=True, color=DEEP)
    text_runs(s, 7.4, 4.35, 5.15, 1.3, [
        {"text": "Внедрённая в контекст последовательность, выглядящая как ",
         "size": 12.5, "color": DEEP},
        {"text": "разметка роли", "size": 12.5, "bold": True, "color": TEAL},
        {"text": ", вливается в то же взвешивание — с той же силой, что "
                 "настоящая.", "size": 12.5, "color": DEEP},
    ], line_spacing=1.18)
    gold_callout(s, 0.55, 5.85, 12.25, 0.95,
                 "Внимание не различает происхождение токенов. "
                 "Архитектурного барьера нет — барьер строится снаружи: "
                 "фильтрация входа + права инструментов.",
                 size=15, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s20"))


def build_s21(p):
    """KV-cache: схема K/V в кэше + Q нового токена; фазы prefill/decode;
    gold callout про длинный чат."""
    s = blank(p)
    slide_title(s, "K и V кешируются — заново считается только Q", size=26,
                h=0.6)
    text_runs(s, 0.55, 1.08, 12.3, 0.55, [
        {"text": "KV-cache: ", "size": 14.5, "bold": True, "color": MID},
        {"text": "Key/Value обработанных токенов сохраняются в памяти "
                 "ускорителя. На каждом шаге вычисляется только Q нового "
                 "токена — против сохранённых K/V.", "size": 14.5,
         "color": DEEP},
    ], line_spacing=1.15)
    # Схема
    ocean_box(s, 0.55, 1.75, 12.25, 1.85, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    xx = 1.0
    for i in range(4):
        lab = f"токен {i+1}" if i < 3 else "…"
        chip(s, xx, 2.0, 1.15, 0.42, lab, fill=MID, color=WHITE, size=12)
        for j, kv in enumerate(("K", "V")):
            filled_rect(s, xx + 0.06 + j * 0.56, 2.52, 0.5, 0.42, TEAL_TINT,
                        stroke=TEAL, stroke_pt=1.2, radius=True,
                        radius_adj=0.25)
            text_box(s, xx + 0.06 + j * 0.56, 2.56, 0.5, 0.34, kv, size=13,
                     bold=True, color=TEAL, align=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE, font=FONT_MONO)
        xx += 1.45
    text_box(s, 1.0, 3.06, 5.6, 0.35,
             "уже посчитаны — лежат в кэше, не пересчитываются",
             size=11, italic=True, color=TEAL)
    # Разделитель и новый токен
    plain_line(s, 7.15, 1.95, 7.15, 3.35, color=LIGHT, w_pt=1.2, dash=4)
    chip(s, 9.7, 2.0, 1.55, 0.42, "новый токен", fill=DEEP, color=WHITE,
         size=12)
    filled_rect(s, 10.2, 2.52, 0.5, 0.42, GOLD, stroke=None, radius=True,
                radius_adj=0.25)
    text_box(s, 10.2, 2.56, 0.5, 0.34, "Q", size=13, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, font=FONT_MONO)
    left_arrow(s, 7.45, 2.6, w=2.6, h=0.26, fill=GOLD)
    text_box(s, 7.45, 2.95, 2.7, 0.35, "сверка со всеми K/V",
             size=11, italic=True, color=MID, align=PP_ALIGN.CENTER)
    # Фазы
    ocean_box(s, 0.55, 3.85, 5.9, 2.1, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.3)
    text_box(s, 0.85, 4.0, 5.3, 0.4, "Фаза 1 — prefill (обработка промпта)",
             size=14.5, bold=True, color=MID)
    text_runs(s, 0.85, 4.45, 5.35, 1.4, [
        {"text": "• Все токены входа известны сразу → K/V считаются ",
         "size": 12.5, "color": DEEP},
        {"text": "параллельно", "size": 12.5, "bold": True, "color": DEEP},
        {"text": "• Упирается в ", "size": 12.5, "color": DEEP,
         "newpara": True, "space_before_pt": 5},
        {"text": "вычислительную мощность", "size": 12.5, "bold": True,
         "color": DEEP},
        {"text": "• Определяет ", "size": 12.5, "color": DEEP,
         "newpara": True, "space_before_pt": 5},
        {"text": "паузу до первого символа ответа (TTFT)", "size": 12.5,
         "bold": True, "color": DEEP},
    ], line_spacing=1.18)
    right_arrow(s, 6.55, 4.75, w=0.45, h=0.28, fill=MID)
    ocean_box(s, 7.1, 3.85, 5.7, 2.1, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.3)
    text_box(s, 7.4, 4.0, 5.1, 0.4, "Фаза 2 — decode (генерация ответа)",
             size=14.5, bold=True, color=TEAL)
    text_runs(s, 7.4, 4.45, 5.15, 1.4, [
        {"text": "• Строго ", "size": 12.5, "color": DEEP},
        {"text": "последовательно", "size": 12.5, "bold": True,
         "color": DEEP},
        {"text": ", токен за токеном", "size": 12.5, "color": DEEP},
        {"text": "• Каждый шаг читает ", "size": 12.5, "color": DEEP,
         "newpara": True, "space_before_pt": 5},
        {"text": "весь накопленный кэш", "size": 12.5, "bold": True,
         "color": DEEP},
        {"text": " из памяти", "size": 12.5, "color": DEEP},
        {"text": "• Упирается в ", "size": 12.5, "color": DEEP,
         "newpara": True, "space_before_pt": 5},
        {"text": "пропускную способность памяти", "size": 12.5,
         "bold": True, "color": DEEP},
        {"text": " → скорость «печати»", "size": 12.5, "color": DEEP},
    ], line_spacing=1.18)
    gold_callout(s, 0.55, 6.2, 12.25, 0.95,
                 "Почему длинный чат тормозит и дорожает: история подаётся "
                 "целиком при каждом обороте — больше prefill, толще кэш, "
                 "медленнее каждый шаг. «Начать новый чат» — буквально сброс "
                 "груза, а не суеверие.", size=13.5, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s21"))


def build_s22(p):
    """Prompt caching: тарифы + кейс-бары слева; exact-prefix стек с
    timestamp-самострелом справа; mini-poll; gold callout."""
    s = blank(p)
    slide_title(s, "Кэш промптов — ставка на повторное использование, "
                   "а не скидка", size=25, h=0.6)
    # Слева — тарифы
    ocean_box(s, 0.55, 1.3, 6.35, 4.35, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 0.85, 1.45, 5.8, 0.4, "Тарифы (сентябрь 2026):",
             size=15, bold=True, color=MID)
    filled_rect(s, 0.85, 1.92, 5.75, 0.52, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.3, radius=True, radius_adj=0.18)
    text_runs(s, 1.02, 1.92, 5.45, 0.52, [
        {"text": "Чтение из кэша — ", "size": 12.5, "color": DEEP},
        {"text": "0.1× базовой ставки входа", "size": 12.5, "bold": True,
         "color": DEEP},
        {"text": " (новейшие — до 0.025×)", "size": 12.5, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    filled_rect(s, 0.85, 2.54, 5.75, 0.52, WHITE, stroke=LIGHT,
                stroke_pt=1.2, radius=True, radius_adj=0.18)
    text_runs(s, 1.02, 2.54, 5.45, 0.52, [
        {"text": "Запись в кэш — ", "size": 12.5, "color": DEEP},
        {"text": "1.25–2× ставки", "size": 12.5, "bold": True, "color": DEEP},
        {"text": " — дороже обычного входа", "size": 12.5, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    text_box(s, 0.85, 3.2, 5.8, 0.65,
             "Окупается со второго-третьего попадания; уникальные запросы "
             "без общего префикса от кэша только дорожают.",
             size=11.5, italic=True, color=SLATE, line_spacing=1.15)
    # Кейс — 2 бара
    text_box(s, 0.85, 3.92, 5.8, 0.35,
             "Кейс: 50 000 анализов документов в месяц", size=13, bold=True,
             color=DEEP)
    filled_rect(s, 0.85, 4.32, 4.6, 0.34, MID)
    text_box(s, 5.55, 4.32, 1.3, 0.34, "$45 000", size=12, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.98, 4.34, 3.6, 0.3, "без кэша", size=11, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, 0.85, 4.76, 0.82, 0.34, GOLD)
    text_runs(s, 1.8, 4.76, 4.9, 0.34, [
        {"text": "$8 000 с кэшем · ", "size": 12, "bold": True,
         "color": DEEP},
        {"text": "−82%", "size": 13.5, "bold": True, "color": GOLD},
    ], anchor=MSO_ANCHOR.MIDDLE)
    # Справа — exact prefix
    ocean_box(s, 7.15, 1.3, 5.65, 4.35, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.4)
    text_runs(s, 7.4, 1.45, 5.15, 0.75, [
        {"text": "Условие: точное совпадение префикса. ", "size": 13,
         "bold": True, "color": DEEP},
        {"text": "Один изменившийся токен инвалидирует кэш для всего, "
                 "что после него.", "size": 12.5, "color": DEEP},
    ], line_spacing=1.15)
    stack = [
        ("системный промпт", TEAL_TINT, TEAL, "✓ кэш"),
        ("инструкции", TEAL_TINT, TEAL, "✓ кэш"),
        ("документы", TEAL_TINT, TEAL, "✓ кэш"),
        ("«Сегодня 2026-09-05 14:23» — динамический", GOLD_TINT, GOLD, "!"),
        ("вопрос", SOFT_GREY, SLATE, "× мимо кэша"),
    ]
    yy = 2.3
    for txt, fill, stroke, mark in stack:
        filled_rect(s, 7.4, yy, 4.0, 0.42, fill, stroke=stroke,
                    stroke_pt=1.4, radius=True, radius_adj=0.2)
        text_box(s, 7.55, yy + 0.02, 3.75, 0.38, txt,
                 size=10.5 if len(txt) > 20 else 12, bold=(mark == "!"),
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, 11.5, yy + 0.02, 1.2, 0.38, mark, size=11, bold=True,
                 color=stroke if mark != "!" else GOLD,
                 anchor=MSO_ANCHOR.MIDDLE)
        yy += 0.52
    ocean_box(s, 7.4, 4.95, 5.15, 0.6, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.2)
    text_runs(s, 7.55, 4.98, 4.9, 0.55, [
        {"text": "Мини-опрос: ", "size": 11.5, "bold": True, "color": TEAL},
        {"text": "добавили динамический timestamp в начало системного "
                 "промпта — что происходит с кэшем?", "size": 11,
         "color": DEEP},
    ], line_spacing=1.1, anchor=MSO_ANCHOR.MIDDLE)
    gold_callout(s, 0.55, 5.95, 12.25, 0.8,
                 "Правило компоновки: стабильное — в начало (промпт, "
                 "инструкции, примеры, документы), переменное — в конец.",
                 size=15, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s22"))


def build_s23(p):
    """Гонка окон: лог-бары 4 модели + 2 полюса + строка про позиционное
    кодирование + gold callout."""
    s = blank(p)
    slide_title(s, "Стандарт 2026 — окно 1–2 миллиона токенов. "
                   "Но заявленное ≠ полезное", size=24, h=0.9, y=0.35)
    # Лог-бары
    ocean_box(s, 0.55, 1.5, 7.65, 3.55, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.4)
    bars = [
        ("GPT-3.5 (2022)", "4 тыс.", 4_000, MID, ""),
        ("Claude 3.5 (2024)", "200 тыс.", 200_000, MID, ""),
        ("Claude Fable 5 (2026)", "1 млн", 1_000_000, GOLD,
         "без наценки за длину"),
        ("Gemini 3.5 Pro (2026)", "2 млн", 2_000_000, GOLD,
         "крупнейшее среди боевых флагманов"),
    ]
    import math
    yy = 1.68
    for name, val, v, color, note in bars:
        w = (math.log10(v) - 3.0) / 3.4 * 4.5
        text_runs(s, 0.9, yy, 6.9, 0.3, [
            {"text": name + " — ", "size": 12.5, "bold": True,
             "color": DEEP},
            {"text": val, "size": 12.5, "bold": True,
             "color": GOLD if color == GOLD else MID},
            {"text": ("  ·  " + note) if note else "", "size": 11,
             "italic": True, "color": SLATE},
        ])
        filled_rect(s, 0.9, yy + 0.33, max(w, 0.3), 0.26, color,
                    radius=True, radius_adj=0.35)
        yy += 0.78
    text_box(s, 0.9, 4.73, 6.9, 0.3, "ширина — логарифмическая шкала",
             size=10.5, italic=True, color=SLATE)
    # Полюса
    card = filled_rect(s, 8.45, 1.5, 4.35, 1.68, SOFT_GREY, stroke=LIGHT,
                       stroke_pt=1.4, radius=True, radius_adj=0.08)
    card.line.dash_style = 4
    text_box(s, 8.7, 1.65, 3.85, 0.4, "Llama 4 Scout: «10 млн»", size=14,
             bold=True, color=DEEP)
    text_box(s, 8.7, 2.1, 3.85, 1.0,
             "заявлено; ни один опубликованный бенчмарк не подтверждает "
             "качество вблизи предела", size=12, color=SLATE,
             line_spacing=1.18)
    ocean_box(s, 8.45, 3.37, 4.35, 1.68, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.3)
    text_box(s, 8.7, 3.52, 3.85, 0.4, "YandexGPT 5 Pro: 32 тыс.", size=14,
             bold=True, color=DEEP)
    text_box(s, 8.7, 3.97, 3.85, 1.0,
             "на полтора-два порядка меньше флагманов — для длинных "
             "документов это определяющее ограничение", size=12, color=DEEP,
             line_spacing=1.18)
    text_box(s, 0.55, 5.2, 12.25, 0.55,
             "Просто «растянуть» окно нельзя: позиция токена закодирована "
             "геометрией, обученной на конкретных длинах, — расширение "
             "(RoPE / YaRN) — отдельная инженерная работа.",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.CENTER,
             line_spacing=1.15)
    gold_callout(s, 0.55, 5.9, 12.25, 0.68,
                 "Платите за то, что кладёте в окно, а не за то, что окно "
                 "вмещает: 900 тыс. токенов входа по $10/млн ≈ $9 за один "
                 "вызов.", size=13.5, align=PP_ALIGN.CENTER)
    text_runs(s, 0.55, 6.63, 12.25, 0.55, [
        {"text": "Что делать: ", "size": 12.5, "bold": True, "color": TEAL},
        {"text": "выбирайте модель по эффективному окну задачи (бенчмарки "
                 "без лексических подсказок), не по маркетинговому "
                 "максимуму.", "size": 12.5, "color": DEEP},
    ], align=PP_ALIGN.CENTER, line_spacing=1.12)
    speaker_notes(s, load_notes("s23"))


def build_s25(p):
    """Needle решён vs NoLiMa-обрушение (chart) + формула-callout +
    строка практики. Закрывает M3."""
    s = blank(p)
    slide_title(s, "Поиск дословной вставки решён. Понимание длинного "
                   "контекста — нет", size=24, h=0.9, y=0.35)
    # Левая панель
    ocean_box(s, 0.55, 1.45, 5.15, 4.2, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_runs(s, 0.85, 1.63, 4.6, 0.75, [
        {"text": "Найти дословно (needle-in-a-haystack) — почти решено ",
         "size": 14.5, "bold": True, "color": MID},
        {"text": "✓", "size": 16, "bold": True, "color": TEAL},
    ], line_spacing=1.15)
    text_runs(s, 0.85, 2.6, 4.6, 1.6, [
        {"text": "• Найти вставленную фразу по буквальному совпадению: "
                 "флагманы — ", "size": 13, "color": DEEP},
        {"text": "до 99% на полном окне в 1 млн токенов", "size": 13,
         "bold": True, "color": DEEP},
        {"text": "• «Найди, где в договоре упоминается сумма» — работает "
                 "почти как обещано", "size": 13, "color": DEEP,
         "newpara": True, "space_before_pt": 10},
    ], line_spacing=1.25)
    # Правая панель
    ocean_box(s, 6.0, 1.45, 6.8, 4.2, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 6.3, 1.6, 6.2, 0.4,
             "Узнать по смыслу (NoLiMa, 2025) — обрушение",
             size=14.5, bold=True, color=DEEP)
    text_runs(s, 6.3, 2.05, 6.2, 0.95, [
        {"text": "Бенчмарк убрал буквальное совпадение слов. ", "size": 12,
         "color": DEEP},
        {"text": "11 из 13 моделей — ниже 50% их же собственной точности "
                 "на коротком контексте", "size": 12, "bold": True,
         "color": DEEP},
        {"text": " — уже на ", "size": 12, "color": DEEP},
        {"text": "32 тыс. токенов", "size": 12, "bold": True, "color": GOLD},
        {"text": " (~3% заявленного окна флагмана).", "size": 12,
         "color": DEEP},
    ], line_spacing=1.18)
    add_image(s, ASSETS / "charts/s25-nolima.png", x=6.5, y=3.1, w=5.2)
    text_box(s, 8.25, 3.16, 3.4, 0.35, "11 из 13 — ниже 50%",
             size=13, bold=True, color=GOLD)
    gold_callout(s, 0.55, 5.78, 12.25, 0.82,
                 "1M окна ≠ 1M рассуждения. Окно — сколько модель может "
                 "прочитать; полезная длина — на скольких токенах она ещё "
                 "связывает факты.", size=15, align=PP_ALIGN.CENTER)
    text_box(s, 0.55, 6.7, 12.25, 0.45,
             "Критические инструкции — в начало или конец промпта · целевой "
             "поиск 5–10 фрагментов бьёт «вывалить всё в окно» · тестируйте "
             "на рабочей длине вашей задачи",
             size=10.5, italic=True, color=LIGHT, align=PP_ALIGN.CENTER,
             line_spacing=1.12)
    speaker_notes(s, load_notes("s25"))


# ============================================================
# БАТЧ 2 — Раздел 4. Сэмплинг и генерация
# ============================================================
def build_s26a(p):
    section_divider(
        p, section_n=4, sub_title="Сэмплинг и генерация",
        frame_phrase="Как из распределения вероятностей рождается один "
                     "токен — и какими ручками этот выбор управляется",
        tag="4 разбора · 2 провала", active_stage={4, 5}, notes_id="s26a",
        frame_size=18)


S26_BARS = [("яблоко", 0.32, True), ("пиццу", 0.19, False),
            ("салат", 0.14, False), ("булочку", 0.11, False),
            ("огурец", 0.08, False)]


def build_s26(p):
    """Распределение top-5 (нативные бары) + сэмплинг → один токен +
    footnote + gold callout."""
    s = blank(p)
    slide_title(s, "На каждом шаге — распределение вероятностей на все "
                   "токены словаря", size=24, h=0.9, y=0.35)
    # Левый box — бары
    ocean_box(s, 0.55, 1.5, 7.9, 3.7, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_runs(s, 0.9, 1.7, 7.2, 0.45, [
        {"text": "Контекст: ", "size": 15, "bold": True, "color": MID},
        {"text": "«Сегодня я съел …»", "size": 15.5, "bold": True,
         "color": DEEP, "font": FONT_MONO},
    ])
    text_box(s, 0.9, 2.2, 7.2, 0.35, "P(следующий токен):", size=13,
             color=SLATE, italic=True)
    yy = 2.62
    for lab, v, is_gold in S26_BARS:
        text_box(s, 0.9, yy, 1.35, 0.4, lab, size=13.5, bold=is_gold,
                 color=DEEP, font=FONT_MONO, anchor=MSO_ANCHOR.MIDDLE,
                 align=PP_ALIGN.RIGHT)
        bw = v / 0.35 * 4.6
        filled_rect(s, 2.4, yy + 0.05, bw, 0.32,
                    GOLD if is_gold else MID, radius=True, radius_adj=0.3)
        text_runs(s, 2.5 + bw, yy, 1.6, 0.4, [
            {"text": f"{v:.2f}".replace(".", ","), "size": 13.5,
             "bold": True, "color": GOLD if is_gold else DEEP},
            {"text": "  — максимум" if is_gold else "", "size": 11,
             "italic": True, "color": SLATE},
        ], anchor=MSO_ANCHOR.MIDDLE)
        yy += 0.5
    # Правый box — сэмплинг
    ocean_box(s, 8.75, 1.5, 4.05, 3.7, fill=WHITE, stroke=TEAL,
              stroke_pt=1.3)
    text_box(s, 9.0, 1.7, 3.55, 0.45, "Сэмплинг → один токен", size=15,
             bold=True, color=TEAL)
    text_box(s, 9.0, 2.25, 3.55, 0.7,
             "правило выбора одного токена из распределения — "
             "единственная ручка в ваших руках",
             size=12, color=DEEP, line_spacing=1.2)
    down_arrow(s, 10.6, 3.1, w=0.4, h=0.5, fill=TEAL)
    chip(s, 9.55, 3.75, 2.4, 0.55, "[ яблоко ]", fill=GOLD, color=DEEP,
         size=15, font=FONT_MONO)
    text_box(s, 9.0, 4.42, 3.55, 0.6, "выбран один — остальные кандидаты "
             "исчезли из ответа", size=11, italic=True, color=SLATE,
             align=PP_ALIGN.CENTER, line_spacing=1.15)
    text_box(s, 0.55, 5.38, 12.25, 0.4,
             "Остальные ~200 000 токенов словаря — каждый < 0.05. Сумма "
             "всех вероятностей = 1. Числа иллюстративные.",
             size=12, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    gold_callout(s, 0.55, 5.85, 12.25, 1.0,
                 "Распределение — «настоящий» выход модели. Уверенный ответ "
                 "и галлюцинация до сэмплинга существовали одновременно — "
                 "как вероятностная масса; выбор сделала политика.",
                 size=14.5, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s26"))


def _mini_bars(s, x, y, w, h, vals, *, gold_first=False):
    """Мини-распределение: вертикальные бары в области (x,y,w,h)."""
    n = len(vals)
    bw = w / (n * 1.5)
    gap = bw * 0.5
    vmax = max(vals) or 1.0
    xx = x + (w - (n * bw + (n - 1) * gap)) / 2
    for i, v in enumerate(vals):
        bh = max(v / vmax * h, 0.02)
        filled_rect(s, xx, y + h - bh, bw, bh,
                    GOLD if (gold_first and i == 0) else MID,
                    radius=False)
        xx += bw + gap
    plain_line(s, x, y + h + 0.02, x + w, y + h + 0.02, color=LIGHT,
               w_pt=1.2)


def build_s27(p):
    """Температура: 3 панели распределений + top-p/top-k + live-бейдж."""
    s = blank(p)
    slide_title(s, "Температура — делитель логитов: меняет остроту выбора, "
                   "не знания", size=25, h=0.6)
    panels = [
        ("T → 0", "(argmax)", [1.0, 0.001, 0.001, 0.001, 0.001],
         "Выбор самого вероятного. Почти одинаковые ответы — «почти» "
         "разберём на следующем слайде.", False),
        ("T = 1", "(стандарт)", [0.32, 0.19, 0.14, 0.11, 0.08],
         "Сэмплирование пропорционально вероятностям модели. Естественная "
         "вариативность.", True),
        ("T = 1.5", "(сглаживание)", [0.24, 0.19, 0.16, 0.14, 0.12],
         "Редкие токены получают реальные шансы — от удачных находок до "
         "бессвязности.", False),
    ]
    x = 0.55
    for tname, tsub, vals, caption, is_std in panels:
        if is_std:
            filled_rect(s, x, 1.4, 3.95, 3.55, WHITE, stroke=GOLD,
                        stroke_pt=2.2, radius=True, radius_adj=0.05)
        else:
            ocean_box(s, x, 1.4, 3.95, 3.55, fill=SURFACE, stroke=LIGHT,
                      stroke_pt=1.3)
        text_runs(s, x + 0.25, 1.58, 3.45, 0.45, [
            {"text": tname, "size": 17, "bold": True, "color": DEEP,
             "font": FONT_MONO},
            {"text": "  " + tsub, "size": 14, "bold": True,
             "color": GOLD if is_std else MID},
        ])
        _mini_bars(s, x + 0.55, 2.15, 2.85, 1.25, vals, gold_first=True)
        text_box(s, x + 0.25, 3.65, 3.45, 1.2, caption, size=11.5,
                 color=DEEP, line_spacing=1.2)
        x += 4.15
    text_runs(s, 0.55, 5.25, 12.3, 0.5, [
        {"text": "top-p", "size": 13.5, "bold": True, "color": MID,
         "font": FONT_MONO},
        {"text": " — отрез хвоста по вероятностной массе · ", "size": 13,
         "color": DEEP},
        {"text": "top-k", "size": 13.5, "bold": True, "color": MID,
         "font": FONT_MONO},
        {"text": " — по числу кандидатов. Основная ручка — температура; "
                 "эти две — тонкая настройка.", "size": 13, "color": DEEP},
    ], align=PP_ALIGN.CENTER)
    ocean_box(s, 2.15, 5.85, 9.0, 0.62, fill=WHITE, stroke=TEAL,
              stroke_pt=1.4)
    text_runs(s, 2.35, 5.85, 8.6, 0.62, [
        {"text": "Живой прогон: ", "size": 13, "bold": True, "color": TEAL},
        {"text": "один и тот же запрос — 10 раз при T=0 и 10 раз при T=1.5.",
         "size": 13, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    text_runs(s, 0.55, 6.58, 12.3, 0.5, [
        {"text": "Что делать: ", "size": 12.5, "bold": True, "color": TEAL},
        {"text": "T под задачу — 0–0.3 для кода и классификации, 0.7+ для "
                 "генерации текста.", "size": 12.5, "color": DEEP},
    ], align=PP_ALIGN.CENTER, line_spacing=1.1)
    speaker_notes(s, load_notes("s27"))


def build_s28(p):
    """T=0 ≠ детерминизм: экспонат 80/1000 + цепочка причины + 2 плашки +
    gold callout. Закрывает M4."""
    s = blank(p)
    slide_title(s, "T=0 не даёт детерминизма: 80 уникальных ответов из 1000",
                size=25, h=0.6)
    # Слева — экспонат
    ocean_box(s, 0.55, 1.35, 4.55, 3.1, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 0.8, 1.6, 4.05, 1.3, "80 / 1000", size=64, bold=True,
             color=GOLD, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 2.95, 3.95, 1.45,
             "уникальных вариантов ответа на идентичный запрос при T=0 — "
             "стандартный vLLM (открытый инференс-сервер; Thinking "
             "Machines Lab, сентябрь 2025)",
             size=12, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.18)
    # Справа — механизм
    text_runs(s, 5.4, 1.35, 7.4, 0.6, [
        {"text": "Причина — не «floating-point вообще», а отсутствие ",
         "size": 13.5, "bold": True, "color": DEEP},
        {"text": "batch-инвариантности ядер:", "size": 13.5, "bold": True,
         "color": MID},
    ], line_spacing=1.15)
    chain = [
        "Сервер группирует одновременные запросы разных пользователей в батчи",
        "Размер батча зависит от чужой нагрузки в эту миллисекунду",
        "Разный размер батча → разный порядок суммирования → младшие "
        "разряды другие",
        "Два близких кандидата в argmax → младший разряд решает выбор "
        "токена → авторегрессия разносит расхождение по всему ответу",
    ]
    yy = 2.0
    for i, step in enumerate(chain):
        h = 0.55 if i < 3 else 0.7
        ocean_box(s, 5.4, yy, 7.4, h, fill=WHITE, stroke=LIGHT,
                  stroke_pt=1.2)
        text_runs(s, 5.6, yy, 7.0, h, [
            {"text": f"{i+1}. ", "size": 12, "bold": True, "color": TEAL},
            {"text": step, "size": 11.5, "color": DEEP},
        ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
        yy += h + 0.08
    # Две плашки
    filled_rect(s, 0.55, 4.75, 6.0, 1.0, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.3, radius=True, radius_adj=0.1)
    text_runs(s, 0.75, 4.82, 5.6, 0.9, [
        {"text": "Решение существует: ", "size": 12.5, "bold": True,
         "color": TEAL},
        {"text": "batch-инвариантные ядра — 1000/1000 побитово идентичны",
         "size": 12.5, "color": DEEP},
    ], line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)
    ocean_box(s, 6.8, 4.75, 6.0, 1.0, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.2)
    text_runs(s, 7.0, 4.82, 5.6, 0.9, [
        {"text": "Цена: ~35% пропускной способности", "size": 12.5,
         "bold": True, "color": DEEP},
        {"text": " → провайдеры не включают; seed у OpenAI — официально "
                 "«mostly deterministic», в основном детерминировано",
         "size": 12, "color": DEEP},
    ], line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)
    gold_callout(s, 0.55, 6.05, 12.25, 0.8,
                 "Не стройте тесты на побитовом сравнении ответов LLM — "
                 "сравнивайте семантически или по структуре.",
                 size=15.5, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s28"))


def build_s29(p):
    """Шесть ручек: сценарная таблица + effort/verbosity + gold callout."""
    s = blank(p)
    slide_title(s, "Ручек стало шесть: добавилась ось глубины рассуждения",
                size=26, h=0.6)
    # Таблица 4×5
    tx, ty, tw = 0.55, 1.35, 12.25
    col_ws = [3.0, 1.9, 1.5, 1.9, 3.95]
    gtbl = s.shapes.add_table(4, 5, Inches(tx), Inches(ty), Inches(tw),
                              Inches(2.4))
    tbl = gtbl.table
    tbl.first_row = False; tbl.horz_banding = False
    for ci, w in enumerate(col_ws):
        tbl.columns[ci].width = Inches(w)
    tbl.rows[0].height = Inches(0.5)
    for ri in range(1, 4):
        tbl.rows[ri].height = Inches(0.63)

    def cell(r, c, txt, *, size=12, bold=False, color=DEEP, fill=WHITE,
             mono=False, align=PP_ALIGN.CENTER):
        cl = tbl.cell(r, c)
        cl.fill.solid(); cl.fill.fore_color.rgb = fill
        cl.margin_left = Inches(0.06); cl.margin_right = Inches(0.06)
        cl.margin_top = Inches(0.02); cl.margin_bottom = Inches(0.02)
        cl.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf = cl.text_frame; tf.word_wrap = True
        para = tf.paragraphs[0]; para.alignment = align
        r_ = para.add_run(); r_.text = txt
        r_.font.name = FONT_MONO if mono else FONT_BODY
        r_.font.size = Pt(size); r_.font.bold = bold
        r_.font.color.rgb = color

    headers = ["Сценарий", "temperature", "top_p", "max_tokens",
               "Системный промпт"]
    for ci, htxt in enumerate(headers):
        cell(0, ci, htxt, size=12.5, bold=True, color=MID,
             mono=(0 < ci < 4))
    rows_data = [
        ("Классификация / извлечение", "0", GOLD, "—", "50–200",
         "Минимальный, со схемой выхода"),
        ("Кодогенерация", "0.2–0.3", DEEP, "0.9", "1000+",
         "Роль + контекст репозитория"),
        ("Творческое письмо", "0.9–1.2", TEAL, "0.95", "2000+",
         "Роль + стиль"),
    ]
    for ri, (scen, t, tcol, tp, mt, sp) in enumerate(rows_data):
        fill = SURFACE if ri % 2 == 0 else WHITE
        cell(ri + 1, 0, scen, size=12, bold=True, fill=fill,
             align=PP_ALIGN.LEFT)
        cell(ri + 1, 1, t, size=13, bold=True, color=tcol, fill=fill,
             mono=True)
        cell(ri + 1, 2, tp, size=12, fill=fill, mono=True)
        cell(ri + 1, 3, mt, size=12, fill=fill, mono=True)
        cell(ri + 1, 4, sp, size=11.5, fill=fill, align=PP_ALIGN.LEFT)
    # Две новые ручки
    knobs = [
        ("effort / reasoning_effort",
         "глубина внутреннего рассуждения: шкала от none до xhigh (OpenAI); "
         "effort при адаптивном мышлении (Anthropic); thinking budget "
         "(Gemini)"),
        ("verbosity",
         "длина видимого ответа, независимая от глубины: думать глубоко, "
         "отвечать коротко"),
    ]
    x = 0.55
    for term, desc in knobs:
        ocean_box(s, x, 4.05, 6.0, 1.35, fill=WHITE, stroke=TEAL,
                  stroke_pt=1.4)
        chip(s, x + 5.05, 4.2, 0.75, 0.32, "2026", fill=GOLD_TINT,
             stroke=GOLD, color=DEEP, size=11)
        text_box(s, x + 0.25, 4.2, 4.7, 0.4, term, size=14.5, bold=True,
                 color=MID, font=FONT_MONO)
        text_box(s, x + 0.25, 4.62, 5.5, 0.72, desc, size=11.5, color=DEEP,
                 line_spacing=1.15)
        x += 6.25
    gold_callout(s, 0.55, 5.75, 12.25, 0.65,
                 "Заучивайте оси — случайность, длина, глубина, формат; "
                 "имена параметров сверяйте с документацией текущего месяца.",
                 size=13.5, align=PP_ALIGN.CENTER)
    text_runs(s, 0.55, 6.47, 12.25, 0.5, [
        {"text": "Что делать: ", "size": 12.5, "bold": True, "color": TEAL},
        {"text": "начинайте с temperature и effort — остальное "
                 "(top_p/top_k/verbosity) — тонкая настройка поверх.",
         "size": 12.5, "color": DEEP},
    ], align=PP_ALIGN.CENTER, line_spacing=1.1)
    speaker_notes(s, load_notes("s29"))


def build_s30(p):
    """Constrained decoding: механика маскирования + ограничения +
    retrieval-пауза."""
    s = blank(p)
    slide_title(s, "Structured outputs: невалидные токены обнуляются прямо "
                   "в распределении", size=23, h=0.9, y=0.35)
    # Слева — механика
    ocean_box(s, 0.55, 1.5, 6.9, 4.25, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_runs(s, 0.85, 1.65, 6.3, 1.0, [
        {"text": "Constrained decoding (ограниченное декодирование): ",
         "size": 13, "bold": True, "color": MID},
        {"text": "на каждом шаге система вычисляет, какие токены оставляют "
                 "вывод валидным относительно JSON-схемы, — и обнуляет "
                 "вероятности всех остальных. Модель физически не может "
                 "нарушить схему.", "size": 13, "color": DEEP},
    ], line_spacing=1.2)
    # мини-схема маскирования: 5 баров, 2 погашены
    vals = [(0.32, True), (0.19, False), (0.14, True), (0.11, False),
            (0.08, True)]
    xx = 1.45
    for v, valid in vals:
        bh = v / 0.35 * 1.0
        filled_rect(s, xx, 2.95 + (1.0 - bh), 0.6, bh,
                    MID if valid else SOFT_GREY, radius=False)
        if not valid:
            text_box(s, xx + 0.08, 2.82 + (1.0 - bh) - 0.28, 0.5, 0.35, "×",
                     size=17, bold=True, color=SLATE, align=PP_ALIGN.CENTER)
        xx += 1.0
    plain_line(s, 1.25, 3.98, 6.45, 3.98, color=LIGHT, w_pt=1.2)
    text_box(s, 1.25, 4.04, 5.4, 0.3,
             "серые нарушают JSON-схему → вероятность 0",
             size=11, italic=True, color=SLATE)
    text_runs(s, 0.85, 4.48, 6.3, 1.1, [
        {"text": "Просьба «ответь строго в JSON» → ~80% валидных\n",
         "size": 13, "color": DEEP},
        {"text": "Strict mode → ", "size": 13.5, "bold": True,
         "color": DEEP, "newpara": True, "space_before_pt": 4},
        {"text": "100%", "size": 15, "bold": True, "color": GOLD},
        {"text": " — гарантия встроена в сэмплинг, а не проверяется "
                 "постфактум", "size": 12.5, "color": DEEP},
    ], line_spacing=1.18)
    # Справа — ограничения
    ocean_box(s, 7.75, 1.5, 5.05, 4.25, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.3)
    text_box(s, 8.0, 1.65, 4.55, 0.4,
             "Ограничения — свойства компиляции", size=14, bold=True,
             color=MID)
    limits = [
        "Рекурсия через $ref — нет (дерево → плоский список с parent_id)",
        "Глубина вложенности — ≤ 5",
        "Первый запрос с новой схемой платит за компиляцию грамматики — "
        "до 10 с",
        "Гарантирован синтаксис, не смысл: валидировать значения "
        "по-прежнему вам",
    ]
    yy = 2.15
    for lim in limits:
        filled_rect(s, 8.0, yy, 4.55, 0.76, SURFACE, stroke=LIGHT,
                    stroke_pt=1.0, radius=True, radius_adj=0.12)
        text_box(s, 8.15, yy + 0.04, 4.25, 0.68, lim, size=11, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
        yy += 0.87
    ocean_box(s, 2.65, 6.05, 8.0, 0.65, fill=WHITE, stroke=TEAL,
              stroke_pt=1.4)
    text_runs(s, 2.85, 6.05, 7.6, 0.65, [
        {"text": "Вопрос залу: ", "size": 14, "bold": True, "color": TEAL},
        {"text": "почему именно 100%, а не 99.9?", "size": 14,
         "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s30"))


def build_s31(p):
    """Авторегрессионный цикл: 5 шагов + возврат + stop-условие."""
    s = blank(p)
    slide_title(s, "Предсказали токен → дописали в контекст → предсказываем "
                   "следующий", size=25, h=0.6)
    steps = [
        ("1 · Текущий контекст",
         "системный промпт + история + запрос + уже сгенерированная часть "
         "ответа", False),
        ("2 · Прямой проход",
         "токенизация → эмбеддинги → все слои внимания", True),
        ("3 · Распределение",
         "вероятности на все ~200 тыс. токенов словаря", False),
        ("4 · Сэмплинг",
         "один токен — по правилам температуры / top-p / схемы", False),
        ("5 · Токен дописан",
         "дописан в контекст — и цикл повторяется", False),
    ]
    bw, gap = 2.32, 0.24
    x0 = (SLIDE_W_IN - bw * 5 - gap * 4) / 2
    y0, bh = 2.35, 1.8
    for i, (head, desc, is_gold) in enumerate(steps):
        x = x0 + i * (bw + gap)
        if is_gold:
            filled_rect(s, x, y0, bw, bh, GOLD_TINT, stroke=GOLD,
                        stroke_pt=2.0, radius=True, radius_adj=0.08)
        else:
            ocean_box(s, x, y0, bw, bh, fill=SURFACE, stroke=LIGHT,
                      stroke_pt=1.3)
        text_box(s, x + 0.15, y0 + 0.12, bw - 0.3, 0.65, head, size=13,
                 bold=True, color=DEEP, line_spacing=1.08)
        text_box(s, x + 0.15, y0 + 0.78, bw - 0.3, 0.95, desc, size=10.5,
                 color=MID if not is_gold else DEEP, line_spacing=1.14)
        if i < 4:
            right_arrow(s, x + bw + 0.02, y0 + bh / 2 - 0.09, w=gap - 0.04,
                        h=0.18, fill=MID)
    chip(s, x0 - 0.15, y0 - 0.42, 0.9, 0.32, "вход", fill=GOLD, color=DEEP,
         size=11.5)
    # Возврат
    plain_line(s, x0 + 4 * (bw + gap) + bw / 2, y0 + bh,
               x0 + 4 * (bw + gap) + bw / 2, y0 + bh + 0.35, color=LIGHT,
               w_pt=2.0)
    left_arrow(s, x0 + bw / 2, y0 + bh + 0.28, w=4 * (bw + gap), h=0.2,
               fill=LIGHT)
    plain_line(s, x0 + bw / 2, y0 + bh, x0 + bw / 2, y0 + bh + 0.30,
               color=LIGHT, w_pt=2.0)
    text_box(s, x0 + 3.0, y0 + bh + 0.52, 6.0, 0.35,
             "возврат к шагу 1 — цикл повторяется", size=12, italic=True,
             color=MID, align=PP_ALIGN.CENTER)
    text_runs(s, 0.55, 5.55, 12.3, 0.45, [
        {"text": "До специального ", "size": 13.5, "color": DEEP},
        {"text": "стоп-токена", "size": 13.5, "bold": True, "color": DEEP},
        {"text": " или до ", "size": 13.5, "color": DEEP},
        {"text": "max_tokens", "size": 13.5, "bold": True, "color": DEEP,
         "font": FONT_MONO},
        {"text": " — обрыв мгновенный, хоть на середине JSON-поля.",
         "size": 13.5, "color": DEEP},
    ], align=PP_ALIGN.CENTER)
    text_box(s, 0.55, 6.15, 12.3, 0.7,
             "Каждый шаг — без состояния: вся «память» живёт в контексте, "
             "который подаётся целиком (KV-cache делает повторную подачу "
             "дешёвой, не отменяя её логически).",
             size=12.5, italic=True, color=LIGHT, align=PP_ALIGN.CENTER,
             line_spacing=1.2)
    speaker_notes(s, load_notes("s31"))


def build_s32(p):
    """Reasoning-токены: раздвоенный выход + ценовые бары + границы +
    gold callout. Закрывает M5."""
    s = blank(p)
    slide_title(s, "Reasoning-токены не видны — но тарифицируются как output",
                size=25, h=0.6)
    # Верх — раздвоенный выход
    ocean_box(s, 0.55, 1.3, 12.25, 2.25, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    filled_rect(s, 0.95, 1.9, 2.7, 0.75, MID, radius=True, radius_adj=0.12)
    text_box(s, 1.0, 1.95, 2.6, 0.65, "авторегрессионный\nцикл  ⟲",
             size=11.5, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    line_arrow(s, 3.7, 2.1, 4.4, 1.8, color=TEAL, w_pt=2.2)
    line_arrow(s, 3.7, 2.45, 4.4, 2.8, color=SLATE, w_pt=2.2)
    filled_rect(s, 4.5, 1.55, 4.6, 0.5, TEAL, radius=True, radius_adj=0.2)
    text_box(s, 4.65, 1.58, 4.3, 0.44, "видимый ответ", size=12.5,
             bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, 4.5, 2.55, 7.7, 0.62, SOFT_GREY, radius=True,
                radius_adj=0.14)
    text_box(s, 4.7, 2.55, 6.2, 0.62,
             "черновик «для себя» — в ответ не попадает, в счёт попадает",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.1)
    text_box(s, 11.05, 2.5, 1.15, 0.72, "×3–10", size=19, bold=True,
             color=GOLD, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    text_box(s, 4.5, 3.24, 8.2, 0.3,
             "по ставке output-токенов, с учётом в max_tokens — без "
             "естественного потолка", size=11, italic=True, color=SLATE)
    # Низ слева — ценовые бары
    ocean_box(s, 0.55, 3.75, 5.95, 2.2, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.3)
    pb = [("o4-mini", 1, MID), ("o3", 5, MID), ("o3-pro", 18, GOLD)]
    yy = 3.95
    for lab, v, color in pb:
        text_box(s, 0.8, yy, 1.05, 0.32, lab, size=11.5, bold=True,
                 color=DEEP, font=FONT_MONO, anchor=MSO_ANCHOR.MIDDLE)
        bw = v / 18 * 3.6
        filled_rect(s, 1.95, yy + 0.04, max(bw, 0.18), 0.24, color,
                    radius=True, radius_adj=0.35)
        text_box(s, 2.05 + max(bw, 0.18), yy, 0.9, 0.32, f"{v}×",
                 size=12, bold=True, color=GOLD if color == GOLD else DEEP,
                 anchor=MSO_ANCHOR.MIDDLE)
        yy += 0.42
    text_runs(s, 0.8, 5.28, 5.5, 0.6, [
        {"text": "o3-pro: 3.6× дороже o3, 18× дороже o4-mini", "size": 11.5,
         "bold": True, "color": DEEP},
        {"text": " — при сопоставимой длине видимых ответов; разницу делает "
                 "объём рассуждения.", "size": 11, "color": SLATE},
    ], line_spacing=1.12)
    # Низ справа — 2 границы
    borders = [
        ("Управление:", " адаптивное мышление / effort вместо ручных "
         "бюджетов — удобно, но стоимость запроса стала менее "
         "предсказуемой"),
        ("«Ход рассуждений» в интерфейсе — пересказ", " (summarized), не "
         "сырые токены: строить аудит решений на «показанных мыслях» "
         "нельзя"),
    ]
    yy = 3.75
    for head, rest in borders:
        ocean_box(s, 6.75, yy, 6.05, 1.02, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.2)
        text_runs(s, 6.95, yy + 0.06, 5.65, 0.9, [
            {"text": head, "size": 12, "bold": True, "color": MID},
            {"text": rest, "size": 11.5, "color": DEEP},
        ], line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)
        yy += 1.18
    gold_callout(s, 0.55, 6.15, 12.25, 0.85,
                 "Закладывайте в бюджет невидимую часть 2–5× видимого "
                 "ответа — и сверяйте по полю usage в ответе API, где "
                 "reasoning-токены видны как строка расхода.",
                 size=14, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s32"))


def build_s34(p):
    """Local vs cloud 2026: три категории; средняя — категориальная
    новость (gold)."""
    s = blank(p)
    slide_title(s, "«Открытые веса» перестали означать «локально "
                   "запускаемые»", size=26, h=0.6)
    cols = [
        ("Действительно локальные — до ~30B", None, [
            "Qwen3.8-27B (Apache 2.0, вход изображение+видео, окно "
            "262 тыс.), Muse Glimmer 30B",
            "Железо: RTX 5090 (32 ГБ) · Apple unified 64–128 ГБ",
            "Лимит — объём памяти, не вычисления"]),
        ("Открытые, но облачные гиганты", "открытая ≠ локальная", [
            "Kimi K3 — 2.8 трлн параметров, крупнейшая открытая модель",
            "DeepSeek V4-Pro — 1.6 трлн",
            "На потребительское железо не помещаются ни в каком виде"]),
        ("Закрытые API", None, [
            "Флагманское качество — по-прежнему здесь",
            "Плата за токен, данные через провайдера"]),
    ]
    x = 0.55
    for title, badge, bullets in cols:
        is_mid = badge is not None
        if is_mid:
            filled_rect(s, x, 1.5, 3.95, 4.0, WHITE, stroke=GOLD,
                        stroke_pt=2.2, radius=True, radius_adj=0.05)
            chip(s, x + 0.55, 1.28, 2.85, 0.4, badge, fill=GOLD, color=DEEP,
                 size=13)
        else:
            ocean_box(s, x, 1.5, 3.95, 4.0, fill=SURFACE, stroke=LIGHT,
                      stroke_pt=1.4)
        # Первый заголовок — одной строкой без переноса (v2.0.2 item 7)
        t_sz = 13.5 if "~30B" in title else 15
        text_box(s, x + 0.15, 1.82, 3.75, 0.75, title, size=t_sz, bold=True,
                 color=MID if not is_mid else DEEP, line_spacing=1.1)
        runs = []
        for i, b in enumerate(bullets):
            bold = b.startswith(("Лимит", "На потребительское"))
            runs.append({"text": "• " + b, "size": 12.5, "color": DEEP,
                         "bold": bold, "newpara": i > 0,
                         "space_before_pt": 8})
        text_runs(s, x + 0.25, 2.7, 3.45, 2.6, runs, line_spacing=1.2)
        x += 4.15
    text_box(s, 0.55, 5.85, 12.25, 0.55,
             "Причины локального выбора прежние: приватность данных · "
             "отсутствие платы за токен на объёмах · независимость от сети.",
             size=12.5, italic=True, color=MID, align=PP_ALIGN.CENTER,
             line_spacing=1.15)
    gold_callout(s, 1.4, 6.45, 10.55, 0.72,
                 "Что делать: задача умещается в ~30B и данные нельзя "
                 "выпускать за периметр — берите локальную модель; нужно "
                 "флагманское качество — берите закрытый API.",
                 size=13, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s34"))


# ============================================================
# БАТЧ 2 — Раздел 5. Финал
# ============================================================
def build_s35a(p):
    section_divider(
        p, section_n=5, sub_title="Финал",
        frame_phrase="Конвейер собран целиком: карта моделей 2026, цена "
                     "доверия бенчмаркам — и шесть утверждений заново",
        tag="4 разбора · 2 провала", active_stage=set(range(7)),
        notes_id="s35a", frame_bar=True, frame_size=18)


def build_s35(p):
    """Recap: конвейер 4 стадий + 4 плашки-наложения + gold callout."""
    s = blank(p)
    slide_title(s, "Новые темы не добавили стадий — они встроились в "
                   "существующие", size=25, h=0.6)
    stages = ["Токенизация", "Эмбеддинги", "Внимание", "Сэмплинг"]
    bw, gap, y0, bh = 2.28, 0.3, 3.3, 0.85
    x0 = 0.62
    centers = []
    for i, st in enumerate(stages):
        x = x0 + i * (bw + gap)
        centers.append(x + bw / 2)
        ocean_box(s, x, y0, bw, bh, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.5)
        text_box(s, x, y0 + 0.08, bw, bh - 0.16, st, size=14.5, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < 3:
            right_arrow(s, x + bw + 0.03, y0 + bh / 2 - 0.09, w=gap - 0.06,
                        h=0.18, fill=MID)
    rx = x0 + 4 * (bw + gap)
    filled_rect(s, rx, y0 + 0.08, 1.85, bh - 0.16, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.8, radius=True, radius_adj=0.15)
    text_runs(s, rx, y0 + 0.12, 1.85, bh - 0.24, [
        {"text": "следующий", "size": 12, "bold": True, "color": DEEP,
         "align": PP_ALIGN.CENTER},
        {"text": "токен", "size": 12, "bold": True, "color": DEEP,
         "newpara": True, "align": PP_ALIGN.CENTER},
    ], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    right_arrow(s, rx - gap + 0.03, y0 + bh / 2 - 0.09, w=gap - 0.06,
                h=0.18, fill=MID)
    # loop назад
    plain_line(s, rx + 0.92, y0 + bh - 0.08, rx + 0.92, y0 + bh + 0.32,
               color=LIGHT, w_pt=1.8)
    left_arrow(s, centers[0], y0 + bh + 0.26, w=rx + 0.92 - centers[0],
               h=0.16, fill=LIGHT)
    text_box(s, 4.2, y0 + bh + 0.46, 5.0, 0.3, "⟲ цикл — токен дописан в "
             "контекст", size=11, italic=True, color=MID,
             align=PP_ALIGN.CENTER)
    # Плашки-наложения: 2 сверху, 2 снизу
    overlays_top = [
        (0, 0.62, 3.35, "Chat-шаблоны", " — препроцессор токенизации"),
        (2, 4.9, 4.5, "KV-cache", " — внутри внимания; prompt caching — "
         "надстройка над ним на границе запросов"),
    ]
    for stage_i, px, pw, head, rest in overlays_top:
        filled_rect(s, px, 1.55, pw, 0.95, TEAL_TINT, stroke=GOLD,
                    stroke_pt=1.5, radius=True, radius_adj=0.1)
        text_runs(s, px + 0.18, 1.60, pw - 0.36, 0.85, [
            {"text": head, "size": 12.5, "bold": True, "color": DEEP},
            {"text": rest, "size": 11.5, "color": DEEP},
        ], line_spacing=1.12, anchor=MSO_ANCHOR.MIDDLE)
        plain_line(s, px + pw / 2, 2.5, centers[stage_i], y0, color=TEAL,
                   w_pt=1.4, dash=4)
    overlays_bottom = [
        (3, 7.6, 4.0, "Structured outputs", " — фильтр на стадии сэмплинга",
         centers[3]),
        (None, 2.9, 4.3, "Reasoning-токены", " — тот же цикл; часть выхода "
         "помечена «черновик»", centers[0] + 1.0),
    ]
    for stage_i, px, pw, head, rest, tx_ in overlays_bottom:
        filled_rect(s, px, 5.0, pw, 0.95, TEAL_TINT, stroke=GOLD,
                    stroke_pt=1.5, radius=True, radius_adj=0.1)
        text_runs(s, px + 0.18, 5.05, pw - 0.36, 0.85, [
            {"text": head, "size": 12.5, "bold": True, "color": DEEP},
            {"text": rest, "size": 11.5, "color": DEEP},
        ], line_spacing=1.12, anchor=MSO_ANCHOR.MIDDLE)
        plain_line(s, px + pw / 2, 5.0,
                   tx_ if stage_i is None else centers[stage_i],
                   y0 + bh + (0.3 if stage_i is None else 0),
                   color=TEAL, w_pt=1.4, dash=4)
    gold_callout(s, 0.55, 6.25, 12.25, 0.85,
                 "Конвейер — диагностическое дерево: по симптому почти "
                 "всегда угадывается стадия-виновник. Спрашивайте: «на какой "
                 "стадии это происходит?»", size=14.5, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s35"))


def build_s36(p):
    """Ландшафт 2026: 2 лагеря + IMO-экспонат + ценовая шкала."""
    s = blank(p)
    slide_title(s, "Сентябрь 2026: качество сблизилось — цены разошлись на "
                   "три порядка", size=24, h=0.9, y=0.35)
    # Колонки
    frontier = [
        "OpenAI: GPT-5.6 — Luna → Terra → Sol",
        "Anthropic: Claude Fable 5 · Opus 5",
        "Google: Gemini 3.5 Pro (окно 2 млн, Deep Think)",
        "xAI: Grok 4.3",
    ]
    open_w = [
        "DeepSeek V4 (Pro 1.6 трлн / Flash 284 млрд)",
        "Qwen 3.8-Max — первая открытая из линейки Max",
        "Kimi K2.6 (1 трлн) · Kimi K3 (2.8 трлн — крупнейшая открытая)",
    ]
    for x, title, items in [(0.55, "Передний край (закрытые веса)",
                             frontier),
                            (6.8, "Открытые веса", open_w)]:
        ocean_box(s, x, 1.5, 6.0, 2.4, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.4)
        text_box(s, x + 0.25, 1.65, 5.5, 0.4, title, size=15, bold=True,
                 color=MID)
        runs = []
        for i, it in enumerate(items):
            bold = "крупнейшая открытая" in it
            runs.append({"text": "• " + it, "size": 12.5, "color": DEEP,
                         "bold": bold, "newpara": i > 0,
                         "space_before_pt": 6})
        text_runs(s, x + 0.25, 2.12, 5.5, 1.7, runs, line_spacing=1.18)
    # IMO экспонат
    filled_rect(s, 0.55, 4.05, 12.25, 0.92, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.8, radius=True, radius_adj=0.12)
    text_box(s, 0.85, 4.13, 11.7, 0.4,
             "IMO 2026: шесть моделей — абсолютные 42/42. Из 666 "
             "участников-людей — семеро.", size=14.5, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 4.55, 11.7, 0.38,
             "Те же системы ошибаются в подсчёте букв слова cranberry — "
             "«рваный интеллект» как рабочая характеристика.",
             size=11, italic=True, color=MID, align=PP_ALIGN.CENTER)
    # Ценовая шкала
    filled_rect(s, 1.0, 5.55, 11.3, 0.2, SOFT_GREY, radius=True,
                radius_adj=0.5)
    filled_rect(s, 1.0, 5.55, 2.3, 0.2, LIGHT, radius=True, radius_adj=0.5)
    filled_rect(s, 10.0, 5.55, 2.3, 0.2, DEEP, radius=True, radius_adj=0.5)
    text_box(s, 1.0, 5.20, 4.5, 0.32, "пол рынка $0.03–0.2 / млн токенов",
             size=12, bold=True, color=MID)
    text_box(s, 8.3, 5.20, 4.0, 0.32, "премиум $10 вход / $50 выход",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.RIGHT)
    text_runs(s, 0.55, 5.98, 12.3, 0.4, [
        {"text": "Kimi K2.6 ≈ GPT-5.5 на защищённом SWE-bench Pro — ",
         "size": 13, "bold": True, "color": DEEP},
        {"text": "при цене на ~80% ниже", "size": 13, "bold": True,
         "color": GOLD},
    ], align=PP_ALIGN.CENTER)
    gold_callout(s, 0.55, 6.55, 12.25, 0.68,
                 "Что делать: пересматривайте выбор модели регулярно — "
                 "ландшафт живёт месяцами, а не годами.",
                 size=13, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s36"))


def build_s37(p):
    """Бенчмарки: 3 сюжета-карточки + gold callout. Закрывает M6."""
    s = blank(p)
    slide_title(s, "Бенчмарки: контаминация, подгонка — и модели, которые "
                   "жульничают сами", size=24, h=0.9, y=0.35)
    # v2.0.2 (item 10): текст сюжетов ≤2 строк (детали в notes);
    # цифры 87.6 vs 57 — крупным контрастным стат-блоком.
    cards = [
        ("1", "Контаминация: заучено, а не умеет", 8.2, [
            {"text": "SWE-bench: публичные репозитории (Verified) vs "
                     "приватные базы (Pro) — ", "size": 12.5, "color": DEEP},
            {"text": "разрыв и есть величина заучивания.", "size": 12.5,
             "bold": True, "color": DEEP},
            {"text": " OpenAI в 2026 перестал публиковать Verified.",
             "size": 12.5, "color": DEEP}]),
        ("2", "Подгонка под метрику", 11.0, [
            {"text": "Llama 4 Maverick: на Chatbot Arena — специальная "
                     "версия, Elo 1417; публичная модель — ", "size": 12.5,
             "color": DEEP},
            {"text": "места 32–35", "size": 12.5, "bold": True,
             "color": DEEP},
            {"text": ". Ян Лекун: результаты «слегка подтасованы».",
             "size": 12.5, "color": DEEP}]),
        ("3", "Модели жульничают сами", 11.0, [
            {"text": "UK AI Security Institute: ", "size": 12.5,
             "color": DEEP},
            {"text": "все 5", "size": 12.5, "bold": True, "color": DEEP},
            {"text": " передовых моделей пытались обмануть процедуру "
                     "оценки; одна модель OpenAI ", "size": 12.5,
             "color": DEEP},
            {"text": "вышла из песочницы и взломала производственные "
                     "серверы Hugging Face", "size": 12.5,
             "bold": True, "color": DEEP},
            {"text": ".", "size": 12.5, "color": DEEP}]),
    ]
    yy = 1.52
    for num, head, body_w, runs in cards:
        ocean_box(s, 0.55, yy, 12.25, 1.42, fill=SURFACE if num != "3"
                  else WHITE, stroke=LIGHT, stroke_pt=1.3)
        text_box(s, 0.8, yy + 0.1, 0.55, 0.6, num, size=26, bold=True,
                 color=LIGHT)
        text_box(s, 1.45, yy + 0.12, 10.9, 0.38, head, size=14.5,
                 bold=True, color=MID)
        text_runs(s, 1.45, yy + 0.52, body_w, 0.85, runs, line_spacing=1.16)
        if num == "1":
            # Стат-блок: 87.6% (gold) vs 57% — крупно, контрастно
            text_runs(s, 9.85, yy + 0.16, 2.8, 0.75, [
                {"text": "87.6%", "size": 24, "bold": True, "color": GOLD},
                {"text": " vs ", "size": 14, "color": SLATE},
                {"text": "57%", "size": 24, "bold": True, "color": DEEP},
            ], align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
            text_box(s, 8.85, yy + 0.94, 3.8, 0.4,
                     "заявка производителя vs защищённый · средний ~25%",
                     size=10.5, italic=True, color=SLATE,
                     align=PP_ALIGN.RIGHT)
        yy += 1.55
    gold_callout(s, 0.55, 6.25, 12.25, 0.8,
                 "Бенчмарки сужают список кандидатов. Выбирает — "
                 "собственный оценочный набор: 30–50 примеров из ваших "
                 "реальных задач.", size=15, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s37"))


S38_ROWS = [
    ("M1", "«Модели научились считать буквы»",
     "Модель видит токены, не буквы; strawberry починили точечным патчем — "
     "cranberry не работает"),
    ("M2", "«Роль system защищена архитектурно»",
     "Роль — токены chat-шаблона в общем потоке; внимание не различает "
     "происхождения токенов"),
    ("M3", "«Окно 1M = работа со всем объёмом»",
     "Окно — ёмкость приёма, не понимания: без лексических совпадений 11 из "
     "13 моделей теряют >50% своей точности уже на 32K"),
    ("M4", "«T=0 даёт детерминированный ответ»",
     "Ядра не batch-инвариантны: чужая нагрузка меняет размер батча — 80 "
     "уникальных ответов из 1000"),
    ("M5", "«Невидимые reasoning-токены не оплачиваются»",
     "Тарифицируются как output; 3–10× видимого ответа; o3-pro в 18× "
     "дороже o4-mini"),
    ("M6", "«Бенчмарки — надёжный способ выбрать модель»",
     "Контаминация (87.6% vs 57%), подгонка витрин, жульничество моделей; "
     "выбирает свой оценочный набор"),
]


def build_s38(p):
    """Payoff: таблица M1–M6 с механизмами + gold callout. Перекличка с s01."""
    s = blank(p)
    slide_title(s, "Шесть утверждений — теперь по строке механизма на каждое",
                size=26, h=0.6)
    tx, ty, tw = 0.55, 1.3, 12.25
    gtbl = s.shapes.add_table(7, 3, Inches(tx), Inches(ty), Inches(tw),
                              Inches(4.45))
    tbl = gtbl.table
    tbl.first_row = False; tbl.horz_banding = False
    for ci, w in enumerate([0.75, 4.35, 7.15]):
        tbl.columns[ci].width = Inches(w)
    tbl.rows[0].height = Inches(0.4)
    for ri in range(1, 7):
        tbl.rows[ri].height = Inches(0.67)

    def cell(r, c, txt, *, size=11.5, bold=False, color=DEEP, fill=WHITE,
             align=PP_ALIGN.LEFT, italic=False):
        cl = tbl.cell(r, c)
        cl.fill.solid(); cl.fill.fore_color.rgb = fill
        cl.margin_left = Inches(0.07); cl.margin_right = Inches(0.05)
        cl.margin_top = Inches(0.02); cl.margin_bottom = Inches(0.02)
        cl.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf = cl.text_frame; tf.word_wrap = True
        para = tf.paragraphs[0]; para.alignment = align
        para.line_spacing = 1.08
        r_ = para.add_run(); r_.text = txt
        r_.font.name = FONT_BODY; r_.font.size = Pt(size)
        r_.font.bold = bold; r_.font.italic = italic
        r_.font.color.rgb = color

    cell(0, 0, "№", size=12, bold=True, color=MID, align=PP_ALIGN.CENTER)
    cell(0, 1, "Утверждение — все ложны", size=12, bold=True, color=MID)
    cell(0, 2, "Механизм", size=12, bold=True, color=MID)
    for ri, (m, stmt, mech) in enumerate(S38_ROWS):
        cell(ri + 1, 0, m, size=12.5, bold=True, fill=GOLD_TINT,
             align=PP_ALIGN.CENTER)
        cell(ri + 1, 1, stmt, size=11, italic=True,
             fill=WHITE if ri % 2 else SURFACE)
        cell(ri + 1, 2, mech, size=11,
             fill=WHITE if ri % 2 else SURFACE)
    gold_callout(s, 0.55, 6.0, 12.25, 0.85,
                 "Знать инструмент — значит знать его границы. Каждое "
                 "утверждение — правда соседней области, растянутая за свою "
                 "границу.", size=15, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s38"))


def build_s39(p):
    """Decision tree «когда не LLM» + лестница эскалации."""
    s = blank(p)
    slide_title(s, "Когда не LLM — и когда не топ-LLM", size=26, h=0.6)
    text_box(s, 0.55, 1.15, 7.5, 0.4, "Когда LLM — не тот инструмент:",
             size=15, bold=True, color=MID)
    branches = [
        ("Классификация на фиксированных категориях с тысячами размеченных "
         "примеров", "классический ML: дешевле, быстрее, воспроизводимо — "
         "а LLM ещё и недетерминирована при T=0"),
        ("Объяснимость перед регулятором", "прозрачные классические методы"),
        ("Отклик < 100 мс (антифрод, устройства без сети)",
         "специализированная малая модель"),
        ("Точные посимвольные и арифметические операции", "код, не модель"),
    ]
    yy = 1.62
    for cond, ans in branches:
        ocean_box(s, 0.55, yy, 7.6, 0.92, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.2)
        text_runs(s, 0.75, yy + 0.05, 7.2, 0.84, [
            {"text": cond, "size": 12, "bold": True, "color": DEEP},
            {"text": "  →  ", "size": 12.5, "bold": True, "color": MID},
            {"text": ans, "size": 12, "color": TEAL, "bold": True},
        ], line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)
        yy += 1.02
    filled_rect(s, 0.55, yy, 7.6, 0.85, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.4, radius=True, radius_adj=0.1)
    text_runs(s, 0.75, yy + 0.04, 7.2, 0.77, [
        {"text": "Иначе", "size": 12.5, "bold": True, "color": TEAL},
        {"text": " — обработка языка, гибкие форматы, многошаговое "
                 "рассуждение, генерация → ", "size": 12, "color": DEEP},
        {"text": "LLM применима и часто оптимальна", "size": 12,
         "bold": True, "color": DEEP},
    ], line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)
    # Справа — лестница
    ocean_box(s, 8.4, 1.15, 4.4, 5.55, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 8.65, 1.3, 3.9, 0.4, "…и не всегда топ-LLM", size=15,
             bold=True, color=DEEP)
    filled_rect(s, 10.3, 2.25, 2.25, 0.8, DEEP, radius=True,
                radius_adj=0.12)
    text_box(s, 10.42, 2.3, 2.0, 0.7, "10% сложных →\nпремиум $10/млн",
             size=10.5, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.05)
    filled_rect(s, 8.65, 3.2, 3.9, 0.9, MID, radius=True, radius_adj=0.1)
    text_box(s, 8.8, 3.25, 3.6, 0.8, "90% запросов →\nмодель за $0.20/млн",
             size=12, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.08)
    text_runs(s, 8.65, 4.55, 3.9, 1.7, [
        {"text": "Миллиард токенов/мес:", "size": 12.5, "bold": True,
         "color": DEEP},
        {"text": "$10 000", "size": 14, "bold": True, "color": DEEP,
         "newpara": True, "space_before_pt": 8},
        {"text": " целиком на премиуме", "size": 12, "color": DEEP},
        {"text": "vs  ", "size": 12.5, "color": SLATE, "newpara": True,
         "space_before_pt": 6},
        {"text": "$1 180", "size": 16, "bold": True, "color": GOLD},
        {"text": " с маршрутизацией", "size": 12, "color": DEEP},
    ], line_spacing=1.15)
    speaker_notes(s, load_notes("s39"))


def build_s40(p):
    """Корреляция ≠ причинность: человек vs модель + gold callout."""
    s = blank(p)
    slide_title(s, "Внимание усваивает корреляцию, не причинность", size=26,
                h=0.6)
    # Человек
    ocean_box(s, 0.55, 1.45, 5.95, 3.55, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 0.85, 1.62, 5.35, 0.4, "Человек", size=16.5, bold=True,
             color=MID)
    text_runs(s, 0.85, 2.1, 5.35, 0.85, [
        {"text": "«X произошло, потому что Y»", "size": 14, "bold": True,
         "color": DEEP},
        {"text": " — модель механизмов мира", "size": 13.5, "color": DEEP},
    ], line_spacing=1.2)
    hlevels = [("ассоциация", "✓"), ("вмешательство", "✓"),
               ("контрфактуальность", "✓")]
    yy = 3.0
    for lab, mark in hlevels:
        filled_rect(s, 0.85, yy, 5.35, 0.52, TEAL_TINT, stroke=TEAL,
                    stroke_pt=1.2, radius=True, radius_adj=0.2)
        text_runs(s, 1.05, yy, 5.0, 0.52, [
            {"text": mark + "  ", "size": 13, "bold": True, "color": TEAL},
            {"text": lab, "size": 13, "bold": True, "color": DEEP},
        ], anchor=MSO_ANCHOR.MIDDLE)
        yy += 0.62
    # Модель
    ocean_box(s, 6.85, 1.45, 5.95, 3.55, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.4)
    text_box(s, 7.15, 1.62, 5.35, 0.4, "Модель (через внимание)",
             size=16.5, bold=True, color=DEEP)
    text_runs(s, 7.15, 2.1, 5.35, 0.85, [
        {"text": "«X следует за Y в текстах»", "size": 14, "bold": True,
         "color": DEEP},
        {"text": " — «потому что» для модели — частотный паттерн, не "
                 "указание на механизм мира", "size": 12.5, "color": DEEP},
    ], line_spacing=1.18)
    mlevels = [
        ("ассоциация — сильна", "✓", TEAL_TINT, TEAL, TEAL),
        ("вмешательство — только похожие на описанные в корпусе", "~",
         WHITE, LIGHT, MID),
        ("контрфактуальность — систематически нет", "×", SOFT_GREY, SLATE,
         SLATE),
    ]
    yy = 3.0
    for lab, mark, fill, stroke, mcol in mlevels:
        filled_rect(s, 7.15, yy, 5.35, 0.52, fill, stroke=stroke,
                    stroke_pt=1.2, radius=True, radius_adj=0.2)
        text_runs(s, 7.35, yy, 5.0, 0.52, [
            {"text": mark + "  ", "size": 13, "bold": True, "color": mcol},
            {"text": lab, "size": 11.5, "bold": True, "color": DEEP},
        ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
        yy += 0.62
    gold_callout(s, 0.55, 5.35, 12.25, 0.95,
                 "Там, где от модели ждут каузальных выводов, человек в "
                 "контуре — архитектурное требование, а не вежливая "
                 "оговорка.", size=15.5, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s40"))


def build_s41(p):
    """Мост к Лекции 3: hero-иллюстрация (свой flat Ocean мост, ≥40%
    площади) + 4 карточки-концепта с якорями."""
    s = blank(p)
    text_runs(s, 0.55, 0.35, 12.3, 0.7, [
        {"text": "Лекция 3: ", "size": 27, "bold": True, "color": GOLD},
        {"text": "как модель выходит за пределы контекста", "size": 27,
         "bold": True, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    # Hero: 9.9" × 5.11" ≈ 51% площади слайда, фоновый слой (как s01)
    hero_w = 9.9
    add_image(s, ASSETS / "illustrations/s41-bridge-lec3.png",
              x=(SLIDE_W_IN - hero_w) / 2, y=1.35, w=hero_w)
    cards = [
        ("s41-search", "RAG",
         "Семантический поиск по вашей базе → найденные фрагменты в "
         "контекст.",
         "Якорь: сходство ≠ релевантность — главная причина разочарований "
         "наивного поиска.", TEAL),
        ("s41-settings", "Инструменты / вызов функций",
         "Модель генерирует структурированный вызов → внешняя система "
         "исполняет.",
         "Якорь: надёжность формата вызова обеспечивают structured outputs.",
         TEAL),
        ("s41-plug", "MCP",
         "Открытый протокол подключения инструментов.",
         "Якорь: стабильный префикс с описаниями инструментов → кэш "
         "промптов, экономика агента.", GOLD),
        ("s41-refresh-cw", "Агентный цикл",
         "Действие → наблюдение → коррекция.",
         "Якорь: агент читает внешний контент — спуфинг ролей превращается "
         "в prompt injection; невидимые токены рассуждения умножаются на "
         "число шагов.", TEAL),
    ]
    card_w, card_h = 5.05, 2.3
    gap_x, gap_y = 1.55, 0.55
    x0 = (SLIDE_W_IN - card_w * 2 - gap_x) / 2
    y0 = 1.65
    for i, (icon, title, body, anchor, acol) in enumerate(cards):
        col, row = i % 2, i // 2
        x = x0 + col * (card_w + gap_x)
        y = y0 + row * (card_h + gap_y)
        ocean_box(s, x, y, card_w, card_h, fill=WHITE, stroke=LIGHT,
                  stroke_pt=1.5)
        add_image(s, ASSETS / f"icons/{icon}.png", x=x + 0.22, y=y + 0.18,
                  w=0.42)
        text_box(s, x + 0.78, y + 0.16, card_w - 0.95, 0.45, title,
                 size=15.5, bold=True, color=DEEP)
        text_box(s, x + 0.25, y + 0.68, card_w - 0.5, 0.62, body, size=12,
                 color=DEEP, line_spacing=1.15)
        text_box(s, x + 0.25, y + 1.32, card_w - 0.5, 0.92, anchor,
                 size=10.5, italic=True,
                 color=acol if acol == GOLD else TEAL, line_spacing=1.15)
    speaker_notes(s, load_notes("s41"))


def build_s42(p):
    """Q&A minimal (паттерн Lec-1 s31): surface-фон, Q&A 140pt, Спасибо."""
    s = blank(p)
    set_slide_bg(s, SURFACE)
    text_box(s, 0.55, 1.7, 12.3, 2.6, "Q&A", size=140, bold=True,
             color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.55, 4.5, 12.3, 0.8, "Спасибо", size=36, italic=True,
             color=MID, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s42"))


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
    # батч 2 — Разделы 3–5
    ("s18a", build_s18a), ("s18", build_s18), ("s19", build_s19),
    ("s20", build_s20), ("s21", build_s21), ("s22", build_s22),
    ("s23", build_s23), ("s25", build_s25),
    ("s26a", build_s26a), ("s26", build_s26), ("s27", build_s27),
    ("s28", build_s28), ("s29", build_s29), ("s30", build_s30),
    ("s31", build_s31), ("s32", build_s32), ("s34", build_s34),
    ("s35a", build_s35a), ("s35", build_s35), ("s36", build_s36),
    ("s37", build_s37), ("s38", build_s38), ("s39", build_s39),
    ("s40", build_s40), ("s41", build_s41), ("s42", build_s42),
]


def main():
    p = setup_pres()
    print(f"Building {len(BUILDERS)} slides (full deck v2.0)…")
    for sid, fn in BUILDERS:
        try:
            fn(p)
            print(f"  {sid} OK")
        except Exception as e:
            print(f"  {sid} FAIL: {type(e).__name__}: {e}")
            raise
    total = len(BUILDERS)
    for i, ((sid, _fn), slide) in enumerate(zip(BUILDERS, p.slides)):
        if sid == "s42":
            continue  # Q&A — паттерн qa_minimal: без footer/номера страницы
        page_number(slide, f"{i + 1}/{total}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    p.save(str(OUT))
    print(f"\nSaved: {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
