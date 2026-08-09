"""
Build script for Семинар 2 — «Классифицируй и не ошибись: тип AI, чек-лист и провалы».

Format matched to library/lectures/lec-01 v3 Ocean Gradient design system
(palette, Ocean rounded box motif, typography scale) and to
library/seminars/sem-01 build patterns (same helper functions, same
voting-mechanic visual language — hand + camera/YOLO badge explained once,
NOT repeated as a clickable-looking pill on every slide).

Source-of-truth: deck.yaml + slides/*.md.

Canvas: 13.333" x 7.5" (16:9).

Direct python-pptx build (not PowerPoint MCP) — same choice sem-01 made,
per notes/mcp-limitations.md [#54-1/#54-2/#54-3]: MCP has no list_shapes,
format_runs is buggy, no update_shape_position. Full-rebuild-per-iteration
via python-pptx sidesteps all three.

ROUND 2 (reveal-architecture fix, 2026-08-08): presentation-critic REJECT +
student-simulator independently found the SAME P0 — 11 slides combined
question+answer on one static PNG with no click-to-reveal (0 animation
objects in PPTX; python-pptx builder does not support it; no precedent in
notes/mcp-limitations.md). Fix: split every affected slide into a Q-slide
(scenario/question, NO highlighted answer) + an A-slide (same composition,
answer revealed), matching the sem-01 `sXX-q.md`/`sXX+1-a.md` pattern.
26 slides -> 40 slides. 14 originals (s04,s05,s06,s08,s09,s10,s11,s14,s15,
s16,s19,s20,s21,s22 by OLD numbering) split into 28 new slides; the other 12
unchanged slides were renumbered around the split (deck.yaml is the single
source of truth for the new s01..s40 order — do not infer position from
filename alone).
"""
import re
from pathlib import Path

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
CODE_BG = RGBColor(0x1B, 0x22, 0x3B)
CODE_FG = RGBColor(0xE3, 0xE9, 0xF2)
GOLD_DARK = RGBColor(0x8A, 0x62, 0x00)  # WCAG-safe dark-gold for text on light bg
                                         # (gold #F0AB00 text fails WCAG AA on
                                         # SURFACE/WHITE — known palette defect,
                                         # see project_ocean_palette_gold_contrast_defect)

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


# ============================================================
# Helpers (adapted from library/seminars/sem-01/rendered/build_sem01.py)
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
    """Each item in `paragraphs` is a dict of text_box-style kwargs (text/size/...).
    Uses tf.add_paragraph() per line — the ONLY reliable way to force a line break
    (see notes/mcp-limitations.md [#sem01-render-1]: literal \\n in a single run
    does not line-break reliably under LibreOffice)."""
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
    """Embed a pre-rendered recolored icon PNG (square) at x,y with width w_in (height = width, square icons)."""
    path = ICONS / f"{name}-{color_hex}-{size_px}.png"
    return add_image(slide, path, x, y, w=w_in, h=w_in)


def slide_title(slide, text, *, y=0.45, h=1.15, w=12.3, x=0.55, size=28,
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


def code_card(slide, x, y, w, h, lines, *, title=None):
    """Dark code-block card (monospace) inside an Ocean rounded box frame."""
    ocean_box(slide, x, y, w, h, fill=SURFACE, stroke=LIGHT)
    pad = 0.2
    inner_y = y + pad
    if title:
        text_box(slide, x + pad, inner_y, w - 2 * pad, 0.35,
                 text=title, size=13, bold=True, color=MID)
        inner_y += 0.42
    code_h = y + h - pad - inner_y
    filled_rect(slide, x + pad, inner_y, w - 2 * pad, code_h, CODE_BG,
                radius=True, radius_adj=0.06)
    paras = [{"text": ln, "size": 12.5, "font": FONT_MONO, "color": CODE_FG,
              "line_spacing": 1.3} for ln in lines]
    multipara_box(slide, x + pad + 0.15, inner_y + 0.14, w - 2 * pad - 0.3,
                  code_h - 0.28, paras)


def speaker_notes(slide, text):
    tf = slide.notes_slide.notes_text_frame
    tf.text = text


def load_notes(slide_id):
    files = list(SLIDES_DIR.glob(f"{slide_id}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding="utf-8")
    m = re.search(r"## Speaker notes\s*\n(.*?)(?=\n## |\n---\s*\n## |\Z)", md, re.DOTALL)
    notes = m.group(1).strip() if m else ""
    notes = re.sub(r"\n+---\s*$", "", notes)
    return notes.strip()


def section_tag(slide, x, y, text, *, color=TEAL):
    """Small uppercase section-context label (top-left of body slides).
    NOT a timing marker — section name only, per CLAUDE.md no-timing rule."""
    text_box(slide, x, y, 6.0, 0.32, text=text.upper(), size=11.5, bold=True,
             color=color, align=PP_ALIGN.LEFT)


def vote_reference_badge(slide, x, y, *, size=0.34):
    """Compact hand+camera badge — used ONLY on s03 (mechanic explainer) at
    full size and, in this deck, nowhere else at all (sem-01 lesson: repeat
    badges are visual noise once the mechanic is established). Kept as a
    helper in case a future slide needs a small callback."""
    icon(slide, "hand", "F0AB00", 64, x, y, size)
    icon(slide, "camera", "21295C", 64, x + size * 0.68, y + size * 0.10, size * 0.6)


# ============================================================
# Slide builders
# ============================================================

def build_s01(p):
    """hero_cover — real bounding-box photo (IoU ground-truth vs predicted,
    Wikimedia Commons CC BY-SA 4.0), continuing the Lecture 1 YOLO/detection
    thread and foreshadowing the seminar's "find the fake / classify
    correctly" keystone."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    text_box(s, x=0.55, y=0.62, w=6.35, h=0.45,
             text="ПОСЛЕ ЛЕКЦИИ 1 · СЕМИНАР 2",
             size=13, bold=True, color=TEAL, align=PP_ALIGN.LEFT)
    text_box(s, x=0.55, y=1.2, w=6.35, h=2.0,
             text="Классифицируй и не ошибись",
             size=40, bold=True, color=DEEP, line_spacing=1.08)
    text_box(s, x=0.55, y=2.95, w=6.35, h=1.15,
             text="Тип AI, чек-лист и провалы",
             size=20, italic=True, color=MID, line_spacing=1.3)
    text_box(s, x=0.55, y=4.35, w=6.05, h=1.5,
             text="Модель отличает верную рамку от ошибочной по чёткому "
                  "критерию — сегодня вы тренируетесь так же чётко отличать "
                  "модель от чата, чата от агента, а правду AI от уверенно "
                  "поданной неправды.",
             size=13.5, color=SLATE, line_spacing=1.4)
    text_box(s, x=0.55, y=6.85, w=6.35, h=0.4,
             text="МГТУ им. Н.Э. Баумана", size=12, color=SLATE)

    # Hero photo — right 47%, full bleed, dark surround card for contrast
    hero_x, hero_y, hero_w, hero_h = 6.85, 0.0, 6.483, 7.5
    filled_rect(s, hero_x, hero_y, hero_w, hero_h, DEEP)
    img_path = SHOTS / "s01-iou-bbox-real.jpg"
    # source is 600x450 (4:3) — fit width, crop vertical via pptx crop props
    pad = 0.5
    avail_w = hero_w - 2 * pad
    avail_h = hero_h - 2 * pad - 0.55
    pic = add_image(s, img_path, hero_x + pad, hero_y + pad + 0.25, w=avail_w, h=avail_h)
    if pic is not None:
        gold_frame = s.shapes.add_shape(MSO_SHAPE.RECTANGLE,
            pic.left, pic.top, pic.width, pic.height)
        gold_frame.fill.background()
        gold_frame.line.color.rgb = GOLD
        gold_frame.line.width = Pt(2.5)
        disable_shadow(gold_frame)
    text_box(s, hero_x + pad, hero_y + pad - 0.05, avail_w, 0.35,
             text="GROUND TRUTH ПРОТИВ ПРЕДСКАЗАНИЯ", size=11.5, bold=True,
             color=GOLD, align=PP_ALIGN.LEFT)
    text_box(s, hero_x + pad, hero_y + hero_h - pad - 0.1, avail_w, 0.35,
             text="Adrian Rosebrock · Wikimedia Commons · CC BY-SA 4.0",
             size=9, italic=True, color=RGBColor(0xC8, 0xD2, 0xDF),
             align=PP_ALIGN.LEFT)
    speaker_notes(s, load_notes("s01"))


def build_s02(p):
    """Раздел 1 — compact visual recap: task x modality axis (left) +
    2-question checklist + quadrant (right). Not a re-teach — a fast visual
    anchor students already saw on the lecture this morning (s12 + s21 of
    lec-01 deck)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 1 · Общий язык с сегодняшней лекции")
    slide_title(s, "Две оси и один чек-лист — язык, который вы уже знаете", y=0.75, size=26)

    col_y = 1.85
    col_h = 5.0
    gap = 0.28
    col_w = (12.23 - gap) / 2

    # LEFT: task x modality mini-matrix
    lx = 0.55
    ocean_box(s, lx, col_y, col_w, col_h)
    pad = 0.24
    icon(s, "layout-grid", "065A82", 64, lx + pad, col_y + pad, 0.36)
    text_box(s, lx + pad + 0.48, col_y + pad - 0.01, col_w - 2 * pad - 0.48, 0.4,
             text="Тип задачи × модальность", size=15, bold=True, color=MID,
             anchor=MSO_ANCHOR.MIDDLE)
    mini_rows = [
        ("scan", "Распознавание", "изображение", "YOLO-детектор (демо сегодня утром)"),
        ("tag", "Классификация", "текст / данные", "спам-фильтр, скоринг"),
        ("search", "Поиск", "текст", "корпоративная база знаний"),
        ("sparkles", "Генерация", "текст / код", "черновик письма, автодополнение"),
    ]
    ry = col_y + pad + 0.55
    rh = (col_h - (pad + 0.55) - pad) / len(mini_rows)
    for ic, task, mod, ex in mini_rows:
        icon(s, ic, "028090", 64, lx + pad, ry + (rh - 0.34) / 2, 0.34)
        text_box(s, lx + pad + 0.46, ry, 2.05, rh,
                 text=task, size=12.5, bold=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
        text_box(s, lx + pad + 2.55, ry, col_w - 2 * pad - 2.55, rh,
                 text=f"{mod} · {ex}", size=10.5, italic=True, color=SLATE,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)
        ry += rh

    # RIGHT: Q1/Q2 + quadrant compact
    rx = lx + col_w + gap
    ocean_box(s, rx, col_y, col_w, col_h)
    icon(s, "compass", "065A82", 64, rx + pad, col_y + pad, 0.36)
    text_box(s, rx + pad + 0.48, col_y + pad - 0.01, col_w - 2 * pad - 0.48, 0.4,
             text="Чек-лист «2 вопроса + квадрант»", size=15, bold=True,
             color=MID, anchor=MSO_ANCHOR.MIDDLE)
    q_y = col_y + pad + 0.55
    text_box(s, rx + pad, q_y, col_w - 2 * pad, 0.6,
             text="Q1: нужно ли взаимодействие с пользователем?",
             size=12, color=DEEP, line_spacing=1.2)
    text_box(s, rx + pad, q_y + 0.42, col_w - 2 * pad, 0.6,
             text="Q2: нужна ли самостоятельная работа с инструментами?",
             size=12, color=DEEP, line_spacing=1.2)

    quad_y = q_y + 0.98
    quad_h = col_y + col_h - pad - quad_y
    quad_w = col_w - 2 * pad
    qx = rx + pad
    cells = [
        ("Модель", "Нет / Нет", MID),
        ("Чат", "Да / Нет", LIGHT),
        ("Приложение", "Нет / Да", TEAL),
        ("Агент", "Да / Да", DEEP),
    ]
    cw = (quad_w - 0.1) / 2
    ch = (quad_h - 0.1) / 2
    positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for (label, cond, col), (r, c) in zip(cells, positions):
        cx = qx + c * (cw + 0.1)
        cy = quad_y + r * (ch + 0.1)
        filled_rect(s, cx, cy, cw, ch, col, radius=True, radius_adj=0.1)
        text_box(s, cx + 0.12, cy + 0.1, cw - 0.24, 0.4,
                 text=label, size=14, bold=True, color=WHITE)
        text_box(s, cx + 0.12, cy + ch - 0.36, cw - 0.24, 0.3,
                 text=cond, size=10, italic=True, color=RGBColor(0xDD, 0xE6, 0xEE))
    speaker_notes(s, load_notes("s02"))


def build_s03(p):
    """Раздел 2 intro — voting mechanic recap (compact, since sem-01 already
    taught it) + roster of the 6 tools to be classified, as a vertical list
    (distinct layout from sem-01's 2x2 grid, per anti-fatigue requirement)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 2 · Калибровка")
    slide_title(s, "Шесть инструментов — один и тот же вопрос: модель, чат, агент или приложение?", y=0.75, size=23)

    mech_y = 1.85
    ocean_box(s, 0.55, mech_y, 12.23, 0.85, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.5)
    icon(s, "hand", "F0AB00", 64, 0.85, mech_y + 0.2, 0.44)
    icon(s, "camera", "21295C", 64, 1.4, mech_y + 0.27, 0.32)
    text_box(s, 1.95, mech_y + 0.1, 9.8, 0.45,
             text="4 раунда поднятия руки на инструмент — один вариант за раз",
             size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 1.95, mech_y + 0.52, 9.8, 0.28,
             text="где голоса разойдутся — объясняем выбор вслух до официального ответа",
             size=10.5, italic=True, color=SLATE)

    list_y = mech_y + 1.1
    list_h = 7.05 - list_y
    row_gap = 0.1
    n = 6
    row_h = (list_h - row_gap * (n - 1)) / n
    tools = [
        ("scan", "YOLO-детектор — демо Лекции 1", "детекция людей в кадре в реальном времени"),
        ("message-square", "AI-чат для разовой консультации", "например, ChatGPT — уточняющий диалог по тексту"),
        ("mouse-pointer-click", "GitHub Copilot — inline Tab-completion", "подсказка следующей строки кода"),
        ("bot", "GitHub Copilot — Agent-режим", "самостоятельно открывает файлы, правит код, коммитит"),
        ("search", "YandexGPT во врезке поиска", "краткий ответ над обычными результатами"),
        ("inbox", "Агент для 200 PDF-отчётов", "читает файлы, собирает сводную таблицу"),
    ]
    for i, (ic, title, desc) in enumerate(tools):
        ry = list_y + i * (row_h + row_gap)
        ocean_box(s, 0.55, ry, 12.23, row_h)
        text_box(s, 0.75, ry, 0.42, row_h, text=str(i + 1), size=15, bold=True,
                 color=LIGHT, anchor=MSO_ANCHOR.MIDDLE)
        icon(s, ic, "028090", 64, 1.25, ry + (row_h - 0.32) / 2, 0.32)
        text_box(s, 1.72, ry + 0.06, 6.6, row_h - 0.12,
                 text=title, size=13, bold=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
        text_box(s, 8.45, ry + 0.06, 4.15, row_h - 0.12,
                 text=desc, size=10.5, italic=True, color=SLATE,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)
    speaker_notes(s, load_notes("s03"))


def build_s04(p):
    """Раздел 2 — Q-slide for tools 1-2 (YOLO / AI-чат). Round-2 split: NO
    answer badge, NO type label — just the two tool descriptions, so the
    facilitator can show this slide during the vote-before-reveal window
    without leaking the answer (presentation-critic P0 fix).
    Round-3 point fix (visual mass): card height cut from 4.05" to 2.5"
    (2nd pass — 2.7" first pass still left visible dead space above/below
    the description line at rendered PNG inspection). Inner desc-box
    y-offset tightened from 0.95" to 0.78" so the description sits closer
    to the title block instead of centered in an oversized remainder.
    grid_y kept at 2.0 (matches s05/s09 reveal-partner slides, and every
    other card-grid Q-slide in the deck) — a 3rd pass had raised grid_y
    to 3.0 to "balance" the empty band above vs. below the shrunk card,
    but that just relocated the dead space into a full extra inch of
    blank gap between title and card-top, a regression caught on
    independent re-inspection against s05's top-anchored layout. Keeping
    grid_y=2.0 lets the card sit where it always did; the freed height
    only shrinks the card itself and the gap before the hint bar."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 2 · Инструменты 1–2")
    slide_title(s, "Модель, чат, агент или приложение?", y=0.75, size=27)

    grid_y = 2.0
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 2.5
    cards = [
        ("scan", "YOLO-детектор людей в кадре",
         "Детекция людей в кадре в реальном времени — прямая перекличка "
         "с демо Лекции 1."),
        ("message-square", "AI-чат для разовой консультации по тексту",
         "Например, ChatGPT — уточняющий диалог по тексту."),
    ]
    for i, (ic, title, desc) in enumerate(cards):
        cx = 0.55 + i * (cw + gap)
        ocean_box(s, cx, grid_y, cw, ch)
        pad = 0.26
        icon(s, ic, "065A82", 96, cx + pad, grid_y + pad, 0.55)
        text_box(s, cx + pad + 0.7, grid_y + pad - 0.03, cw - 2 * pad - 0.7, 0.9,
                 text=title, size=14.5, bold=True, color=DEEP, line_spacing=1.15,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, cx + pad, grid_y + pad + 0.78, cw - 2 * pad, ch - pad - 0.78 - pad,
                 text=desc, size=13, italic=True, color=SLATE, line_spacing=1.35,
                 anchor=MSO_ANCHOR.MIDDLE)

    hint_y = grid_y + ch + 0.9
    ocean_box(s, 0.55, hint_y, 12.23, 0.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.3)
    icon(s, "hand", "028090", 64, 0.85, hint_y + 0.1, 0.34)
    text_box(s, 1.4, hint_y, 11.2, 0.55,
             text="4 раунда поднятия руки на инструмент — модель? чат? агент? приложение?",
             size=13.5, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s04"))


def build_s05(p):
    """Раздел 2 — A-slide (reveal) for tools 1-2. Same two cards as s04,
    now with answer badges + reasoning. Round-2 split partner of s04."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 2 · Инструменты 1–2 · ответ")
    slide_title(s, "Один проход без диалога — модель. Диалог без инструментов — чат", y=0.75, size=24)

    grid_y = 2.0
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 4.7
    cards = [
        ("scan", "YOLO-детектор людей в кадре", "Модель", MID,
         "Q1 нет — нет диалога на каждый кадр. Q2 нет — один проход "
         "«изображение → детекция» без вызова инструментов.",
         "Прямая перекличка с сегодняшним утренним демо."),
        ("message-square", "AI-чат для разовой консультации по тексту", "Чат", LIGHT,
         "Q1 да — диалог, уточнения. Q2 нет — модель работает с тем, "
         "что дал пользователь, не ходит сама в базы данных.",
         "Разминочный пункт — ожидаемо низкая дискуссия."),
    ]
    for i, (ic, title, answer, col, reasoning, note) in enumerate(cards):
        cx = 0.55 + i * (cw + gap)
        ocean_box(s, cx, grid_y, cw, ch)
        pad = 0.26
        icon(s, ic, "065A82", 96, cx + pad, grid_y + pad, 0.55)
        text_box(s, cx + pad + 0.7, grid_y + pad - 0.03, cw - 2 * pad - 0.7, 0.9,
                 text=title, size=14.5, bold=True, color=DEEP, line_spacing=1.15,
                 anchor=MSO_ANCHOR.MIDDLE)
        badge_y = grid_y + pad + 0.75
        filled_rect(s, cx + pad, badge_y, cw - 2 * pad, 0.55, col, radius=True, radius_adj=0.25)
        text_box(s, cx + pad, badge_y, cw - 2 * pad, 0.55, text=answer, size=18,
                 bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, cx + pad, badge_y + 0.75, cw - 2 * pad, 1.6,
                 text=reasoning, size=12.5, color=DEEP, line_spacing=1.3)
        text_box(s, cx + pad, grid_y + ch - pad - 0.5, cw - 2 * pad, 0.5,
                 text=note, size=11, italic=True, color=SLATE, line_spacing=1.2)
    speaker_notes(s, load_notes("s05"))


def build_s06(p):
    """Раздел 2 — Copilot pair Q-slide (tools 3-4), THE key moment of the
    section. Round-2 split: shared-brand banner + 2 mode descriptions, NO
    answer badges, NO gold connector arrow (that appears only on the
    A-slide s07) — the vote happens against this neutral composition."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 2 · Инструменты 3–4 · ключевой момент")
    slide_title(s, "Один и тот же продукт, два режима использования — что это?", y=0.75, size=24)

    banner_y = 1.85
    ocean_box(s, 0.55, banner_y, 12.23, 0.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.3)
    icon(s, "code-2", "028090", 64, 0.8, banner_y + 0.11, 0.32)
    text_box(s, 1.25, banner_y, 11.3, 0.55,
             text="GitHub Copilot — один и тот же продукт, два режима использования",
             size=13.5, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)

    row_y = banner_y + 0.75
    row_h = 2.05
    gap_v = 0.35
    row_w = 12.23

    rows = [
        ("mouse-pointer-click", "Inline-автодополнение (Tab-completion)",
         "Нажал Tab — получил предложение по текущей строке. Нет диалога, "
         "нет многошагового планирования."),
        ("bot", "Agent-режим (Workspace)",
         "Получает текстовую задачу, сам открывает несколько файлов "
         "проекта, правит код, коммитит."),
    ]
    for i, (ic, title, desc) in enumerate(rows):
        ry = row_y + i * (row_h + gap_v)
        ocean_box(s, 0.55, ry, row_w, row_h)
        pad = 0.26
        icon(s, ic, "065A82", 96, 0.55 + pad, ry + pad, 0.62)
        text_box(s, 0.55 + pad + 0.8, ry + pad - 0.05, row_w - pad - 0.8 - pad, 0.7,
                 text=title, size=15.5, bold=True, color=DEEP, line_spacing=1.15)
        text_box(s, 0.55 + pad + 0.8, ry + pad + 0.62, row_w - pad - 0.8 - pad, 1.1,
                 text=desc, size=12.5, italic=True, color=SLATE, line_spacing=1.32)

    text_box(s, 0.55, row_y + 2 * row_h + gap_v + 0.08, row_w, 0.4,
             text="4 раунда голосования на каждый режим — модель? чат? агент? приложение?",
             size=13, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s06"))


def build_s07(p):
    """Раздел 2 — Copilot pair A-slide (reveal). Same 2 rows as s06, now
    with answer badges + gold connector arrow + closing thesis. Round-2
    split partner of s06."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 2 · Инструменты 3–4 · ключевой момент")
    slide_title(s, "Один инструмент — два режима — два разных типа", y=0.75, size=27)

    # Shared-brand banner
    banner_y = 1.85
    ocean_box(s, 0.55, banner_y, 12.23, 0.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.3)
    icon(s, "code-2", "028090", 64, 0.8, banner_y + 0.11, 0.32)
    text_box(s, 1.25, banner_y, 11.3, 0.55,
             text="GitHub Copilot — один и тот же продукт, два режима использования",
             size=13.5, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)

    row_y = banner_y + 0.75
    row_h = 2.05
    gap_v = 0.35
    row_w = 12.23

    rows = [
        ("mouse-pointer-click", "Inline-автодополнение (Tab-completion)",
         "Приложение", TEAL,
         "Нажал Tab — получил предложение по текущей строке. Нет диалога, "
         "нет многошагового планирования.",
         "Q1 нет · Q2 нет"),
        ("bot", "Agent-режим (Workspace)",
         "Агент", DEEP,
         "Получает текстовую задачу, сам открывает несколько файлов "
         "проекта, правит код, коммитит.",
         "Q1 да · Q2 да"),
    ]
    for i, (ic, title, answer, col, reasoning, qmark) in enumerate(rows):
        ry = row_y + i * (row_h + gap_v)
        ocean_box(s, 0.55, ry, row_w, row_h)
        pad = 0.26
        icon(s, ic, "065A82", 96, 0.55 + pad, ry + pad, 0.62)
        text_box(s, 0.55 + pad + 0.8, ry + pad - 0.05, 6.0, 0.7,
                 text=title, size=15.5, bold=True, color=DEEP, line_spacing=1.15)
        text_box(s, 0.55 + pad + 0.8, ry + pad + 0.62, 6.0, 1.1,
                 text=reasoning, size=12, color=SLATE, line_spacing=1.28)
        badge_x = 0.55 + row_w - pad - 3.1
        filled_rect(s, badge_x, ry + pad, 3.1, 0.6, col, radius=True, radius_adj=0.25)
        text_box(s, badge_x, ry + pad, 3.1, 0.6, text=answer, size=19, bold=True,
                 color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, badge_x, ry + pad + 0.72, 3.1, 0.4, text=qmark, size=11.5,
                 italic=True, color=SLATE, align=PP_ALIGN.CENTER)
        if i == 0:
            arr = s.shapes.add_shape(MSO_SHAPE.DOWN_ARROW,
                Inches(0.55 + row_w / 2 - 0.22), Inches(ry + row_h + 0.02),
                Inches(0.44), Inches(gap_v - 0.04))
            arr.fill.solid(); arr.fill.fore_color.rgb = GOLD
            arr.line.fill.background()
            disable_shadow(arr)

    text_box(s, 0.55, row_y + 2 * row_h + gap_v + 0.08, row_w, 0.4,
             text="Тип определяется режимом использования, а не брендом продукта",
             size=13.5, bold=True, color=GOLD_DARK,
             align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s07"))


def build_s08(p):
    """Раздел 2 — Q-slide for tools 5-6 (YandexGPT snippet / 200-PDF
    agent). Round-2 split: no answer badges. Visual-mass fix applied
    (P1 finding): description text is MIDDLE-anchored in a shorter fixed
    card height instead of top-anchored in a tall card, per presentation-
    critic recommendation (same technique already used on s19-21/s23 in
    round 1).
    Round-3 point fix (visual mass): card height cut from 4.05" to 2.5"
    (2nd pass, same final value as s04 — identical content profile, must
    match). Inner desc-box y-offset tightened from 0.95" to 0.78". grid_y
    kept at 2.0 (matches s04, s05/s09 reveal-partners, and every other
    card-grid Q-slide in the deck) — a 3rd pass had raised grid_y to 3.0
    to "balance" empty space above/below the shrunk card, but that just
    relocated the dead space into a full extra inch of blank gap between
    title and card-top, a regression caught on independent re-inspection
    against s05's top-anchored layout. Keeping grid_y=2.0 lets the card
    sit where it always did; the freed height only shrinks the card
    itself and the gap before the hint bar."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 2 · Инструменты 5–6")
    slide_title(s, "Модель, чат, агент или приложение?", y=0.75, size=27)

    grid_y = 2.0
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 2.5
    cards = [
        ("search", "YandexGPT во врезке Яндекс.Поиска",
         "Сгенерированный краткий ответ над списком обычных результатов поиска."),
        ("inbox", "Агент читает 200 PDF-отчётов",
         "Собирает сводную таблицу — тот же разобранный пример, что на лекции."),
    ]
    for i, (ic, title, desc) in enumerate(cards):
        cx = 0.55 + i * (cw + gap)
        ocean_box(s, cx, grid_y, cw, ch)
        pad = 0.26
        icon(s, ic, "065A82", 96, cx + pad, grid_y + pad, 0.55)
        text_box(s, cx + pad + 0.7, grid_y + pad - 0.03, cw - 2 * pad - 0.7, 0.9,
                 text=title, size=14, bold=True, color=DEEP, line_spacing=1.15,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, cx + pad, grid_y + pad + 0.78, cw - 2 * pad, ch - pad - 0.78 - pad,
                 text=desc, size=13, italic=True, color=SLATE, line_spacing=1.35,
                 anchor=MSO_ANCHOR.MIDDLE)

    hint_y = grid_y + ch + 0.9
    ocean_box(s, 0.55, hint_y, 12.23, 0.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.3)
    icon(s, "hand", "028090", 64, 0.85, hint_y + 0.1, 0.34)
    text_box(s, 1.4, hint_y, 11.2, 0.55,
             text="4 раунда поднятия руки на инструмент — модель? чат? агент? приложение?",
             size=13.5, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s08"))


def build_s09(p):
    """Раздел 2 — A-slide (reveal) for tools 5-6. Same 2 cards as s08, now
    with answer badges + reasoning. Layout mirrors s04/s05 but mirrored
    left-right (visual variety, not identical repeat). Round-2 split
    partner of s08."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 2 · Инструменты 5–6 · ответ")
    slide_title(s, "AI «под капотом» — приложение. Самостоятельная работа с файлами — агент", y=0.75, size=22)

    grid_y = 2.0
    gap = 0.3
    cw = (12.23 - gap) / 2
    ch = 4.7
    cards = [
        ("search", "YandexGPT во врезке Яндекс.Поиска", "Приложение", TEAL,
         "Пользователь не пишет промпт и не ведёт диалог — это функция "
         "поиска, AI работает «под капотом».",
         "Q1 нет · Q2 да"),
        ("inbox", "Агент читает 200 PDF-отчётов → сводная таблица", "Агент", DEEP,
         "Пользователь ставит задачу и утверждает результат; агент "
         "открывает файлы, парсит, дописывает в таблицу.",
         "Q1 да · Q2 да"),
    ]
    for i, (ic, title, answer, col, reasoning, qmark) in enumerate(cards):
        cx = 0.55 + i * (cw + gap)
        ocean_box(s, cx, grid_y, cw, ch)
        pad = 0.26
        icon(s, ic, "065A82", 96, cx + pad, grid_y + pad, 0.55)
        text_box(s, cx + pad + 0.7, grid_y + pad - 0.03, cw - 2 * pad - 0.7, 0.9,
                 text=title, size=14, bold=True, color=DEEP, line_spacing=1.15,
                 anchor=MSO_ANCHOR.MIDDLE)
        badge_y = grid_y + pad + 0.75
        filled_rect(s, cx + pad, badge_y, cw - 2 * pad, 0.55, col, radius=True, radius_adj=0.25)
        text_box(s, cx + pad, badge_y, cw - 2 * pad, 0.55, text=answer, size=18,
                 bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, cx + pad, badge_y + 0.7, cw - 2 * pad, 0.32,
                 text=qmark, size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
        text_box(s, cx + pad, badge_y + 1.1, cw - 2 * pad, 1.5,
                 text=reasoning, size=12.5, color=DEEP, line_spacing=1.32)
    speaker_notes(s, load_notes("s09"))


def build_s10(p):
    """Раздел 3 intro — ЯДРО ЗАНЯТИЯ. Process-style 5-step methodology
    strip (read -> think -> vote -> cold-call -> debrief) sets up the 4
    scenarios that follow. Unchanged content, renumbered s07 -> s10 in
    Round 2 (14 slides split into 28 pushed all following ids forward)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 3 · Ядро занятия")
    slide_title(s, "Четыре инженерных сценария — чек-лист под давлением времени", y=0.75, size=25)

    intro_y = 1.85
    ocean_box(s, 0.55, intro_y, 12.23, 1.0, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.5)
    text_box(s, 0.85, intro_y + 0.14, 11.6, 0.75,
             text="Интуитивный первый ответ здесь иногда неверен — это и есть смысл упражнения",
             size=15.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)

    steps_y = intro_y + 1.35
    steps = [
        ("clock", "30–60 сек", "думаем про себя"),
        ("hand", "4 раунда", "голосуем по квадранту"),
        ("users", "вызов", "2–3 объясняют вслух"),
        ("check-circle-2", "разбор", "официальный ответ"),
    ]
    n = len(steps)
    gap = 0.35
    box_w = (12.23 - gap * (n - 1) - 0.6 * (n - 1)) / n
    arrow_w = 0.6
    cx = 0.55
    step_h = 5.7 - steps_y
    for i, (ic, top, bottom) in enumerate(steps):
        ocean_box(s, cx, steps_y, box_w, step_h)
        icon(s, ic, "065A82", 96, cx + (box_w - 0.55) / 2, steps_y + 0.35, 0.55)
        text_box(s, cx + 0.1, steps_y + 1.15, box_w - 0.2, 0.4,
                 text=top, size=15, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, cx + 0.1, steps_y + 1.65, box_w - 0.2, 0.6,
                 text=bottom, size=11.5, italic=True, color=SLATE,
                 align=PP_ALIGN.CENTER, line_spacing=1.2)
        cx += box_w
        if i < n - 1:
            arr = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,
                Inches(cx + 0.06), Inches(steps_y + step_h / 2 - 0.16),
                Inches(arrow_w - 0.12), Inches(0.32))
            arr.fill.solid(); arr.fill.fore_color.rgb = TEAL
            arr.line.fill.background()
            disable_shadow(arr)
            cx += arrow_w

    text_box(s, 0.55, 6.85, 12.23, 0.4,
             text="После всех четырёх — общий вопрос: где обычный код справился бы не хуже AI?",
             size=12.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s10"))


def quadrant_mini(slide, x, y, w, h, highlight_label, *, orientation="normal"):
    """Small 2x2 quadrant with one cell highlighted GOLD (the correct
    answer), others MID-family neutral. `orientation` swaps which corner
    order is used, purely for visual variety across scenario slides.

    Round-2: `highlight_label=None` renders ALL 4 cells neutral SOFT_GREY —
    used on Q-slides so the vote-before-reveal window shows no visual hint
    of the correct answer (presentation-critic P0 fix — the old single-
    slide version always highlighted the answer cell GOLD, which leaked
    the answer before the hand-raise vote)."""
    labels_normal = [("Модель", 0, 0), ("Чат", 0, 1), ("Приложение", 1, 0), ("Агент", 1, 1)]
    cw = (w - 0.08) / 2
    ch = (h - 0.08) / 2
    for label, r, c in labels_normal:
        cx = x + c * (cw + 0.08)
        cy = y + r * (ch + 0.08)
        is_hl = (highlight_label is not None and label == highlight_label)
        col = GOLD if is_hl else SOFT_GREY
        txt_col = DEEP if is_hl else SLATE
        filled_rect(slide, cx, cy, cw, ch, col, radius=True, radius_adj=0.14)
        text_box(slide, cx, cy, cw, ch, text=label, size=13, bold=is_hl,
                 color=txt_col, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def scenario_slide(p, *, slide_id, section_label, title, icon_name, scenario_text,
                    q1, q2, answer, answer_note, layout, mode="answer"):
    """Shared builder for the 8 Section-3 scenario slides (4 scenarios x
    Q+A pair), with 4 distinct `layout` variants so slides in a row don't
    look identical (sem-01 known bug #5 — structural fatigue from repeated
    identical formats).

    Round-2: `mode="question"` renders the quadrant with NO cell
    highlighted (quadrant_mini highlight_label=None) and replaces the gold
    reveal-callout with a neutral SURFACE/TEAL "think + vote" hint —
    fixing the presentation-critic P0 (quadrant used to show the GOLD
    answer cell on the same slide as the scenario text, before the vote).
    `mode="answer"` is the original reveal behaviour, unchanged."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, section_label)
    slide_title(s, title, y=0.75, size=23)

    quad_label = answer if mode == "answer" else None
    hint_text = "30–60 сек размышления → голосуем по всем 4 углам"

    if layout == "left_text_right_quad":
        card_y = 1.95
        card_h = 4.35
        card_w = 6.5
        ocean_box(s, 0.55, card_y, card_w, card_h)
        pad = 0.28
        icon(s, icon_name, "065A82", 96, 0.55 + pad, card_y + pad, 0.5)
        text_box(s, 0.55 + pad, card_y + pad + 0.65, card_w - 2 * pad, 1.5,
                 text=scenario_text, size=13.5, italic=True, color=DEEP, line_spacing=1.4)
        q_y = card_y + card_h - pad - 1.1
        text_box(s, 0.55 + pad, q_y, card_w - 2 * pad, 0.5,
                 text=f"Q1: {q1}", size=12, bold=True, color=MID, line_spacing=1.2)
        text_box(s, 0.55 + pad, q_y + 0.55, card_w - 2 * pad, 0.5,
                 text=f"Q2: {q2}", size=12, bold=True, color=MID, line_spacing=1.2)

        qx = 0.55 + card_w + 0.3
        qw = 12.23 - card_w - 0.3
        quadrant_mini(s, qx, card_y, qw, card_h - 0.7, quad_label)
        if mode == "answer":
            gold_callout(s, qx, card_y + card_h - 0.55, qw, 0.55, answer_note, size=11.5)
        else:
            ocean_box(s, qx, card_y + card_h - 0.55, qw, 0.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
            text_box(s, qx + 0.15, card_y + card_h - 0.55, qw - 0.3, 0.55,
                     text=hint_text, size=10.5, italic=True, color=MID,
                     anchor=MSO_ANCHOR.MIDDLE)

    elif layout == "top_text_bottom_quad":
        card_y = 1.95
        card_w = 12.23
        ocean_box(s, 0.55, card_y, card_w, 1.85)
        pad = 0.28
        icon(s, icon_name, "065A82", 96, 0.55 + pad, card_y + pad, 0.48)
        text_box(s, 0.55 + pad + 0.65, card_y + pad - 0.02, card_w - 2 * pad - 0.65, 1.6,
                 text=scenario_text, size=13, italic=True, color=DEEP, line_spacing=1.3)
        q_y = card_y + 1.95
        half = (card_w - 0.3) / 2
        ocean_box(s, 0.55, q_y, half, 0.85, fill=SURFACE, stroke=TEAL)
        text_box(s, 0.55 + 0.2, q_y, half - 0.4, 0.85, text=f"Q1: {q1}", size=11.5,
                 bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)
        ocean_box(s, 0.55 + half + 0.3, q_y, half, 0.85, fill=SURFACE, stroke=TEAL)
        text_box(s, 0.55 + half + 0.5, q_y, half - 0.4, 0.85, text=f"Q2: {q2}", size=11.5,
                 bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)

        quad_y = q_y + 1.05
        quad_h = 7.15 - quad_y
        quad_w = 7.6
        quadrant_mini(s, 0.55, quad_y, quad_w, quad_h, quad_label)
        if mode == "answer":
            gold_callout(s, 0.55 + quad_w + 0.3, quad_y, card_w - quad_w - 0.3, quad_h,
                         answer_note, size=12.5)
        else:
            ocean_box(s, 0.55 + quad_w + 0.3, quad_y, card_w - quad_w - 0.3, quad_h,
                      fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
            icon(s, "hand", "028090", 64, 0.55 + quad_w + 0.55, quad_y + 0.3, 0.4)
            text_box(s, 0.55 + quad_w + 0.55, quad_y + 0.85, card_w - quad_w - 0.85, quad_h - 1.0,
                     text=hint_text, size=12.5, italic=True, color=MID, line_spacing=1.35)

    elif layout == "twin_column":
        # Used for scenario 3 — deliberately visually paired with scenario 4
        # (same product pattern, different mode) via matching left column.
        card_y = 1.95
        card_h = 4.9
        card_w = 5.6
        ocean_box(s, 0.55, card_y, card_w, card_h, fill=SURFACE, stroke=TEAL)
        pad = 0.26
        icon(s, icon_name, "028090", 96, 0.55 + pad, card_y + pad, 0.5)
        text_box(s, 0.55 + pad, card_y + pad + 0.65, card_w - 2 * pad, 2.4,
                 text=scenario_text, size=13, italic=True, color=DEEP, line_spacing=1.35)
        text_box(s, 0.55 + pad, card_y + card_h - pad - 0.9, card_w - 2 * pad, 0.9,
                 text=f"Q1: {q1}\nQ2: {q2}".replace("\n", "  ·  "), size=10.5,
                 bold=True, color=MID, line_spacing=1.3)

        rx = 0.55 + card_w + 0.3
        rw = 12.23 - card_w - 0.3
        quadrant_mini(s, rx, card_y, rw, card_h - 0.7, quad_label)
        if mode == "answer":
            gold_callout(s, rx, card_y + card_h - 0.55, rw, 0.55, answer_note, size=11.5)
        else:
            ocean_box(s, rx, card_y + card_h - 0.55, rw, 0.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
            text_box(s, rx + 0.15, card_y + card_h - 0.55, rw - 0.3, 0.55,
                     text=hint_text, size=10.5, italic=True, color=MID,
                     anchor=MSO_ANCHOR.MIDDLE)

    elif layout in ("twin_column_gold", "twin_column_gold_neutral"):
        # Scenario 4 — mirrors "twin_column" (scenario 3) but flips L/R.
        # Answer-mode uses a GOLD-accented right card to visually signal
        # "the payoff of the pair" + a connecting note back to scenario 3.
        # Question-mode (Round 2) uses a plain SURFACE/TEAL right card and
        # NO connecting note (the "second time today" thesis is a reveal,
        # not appropriate before the vote).
        card_y = 1.95
        card_h = 4.35
        rw = 5.6
        rx = 12.23 - rw + 0.55
        qx = 0.55
        qw = 12.23 - rw - 0.3
        quadrant_mini(s, qx, card_y, qw, card_h - 0.7, quad_label)
        if mode == "answer":
            gold_callout(s, qx, card_y + card_h - 0.55, qw, 0.55, answer_note, size=11.5)
        else:
            ocean_box(s, qx, card_y + card_h - 0.55, qw, 0.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
            text_box(s, qx + 0.15, card_y + card_h - 0.55, qw - 0.3, 0.55,
                     text=hint_text, size=10.5, italic=True, color=MID,
                     anchor=MSO_ANCHOR.MIDDLE)

        if mode == "answer":
            ocean_box(s, rx, card_y, rw, card_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.6)
        else:
            ocean_box(s, rx, card_y, rw, card_h, fill=SURFACE, stroke=TEAL, stroke_pt=1.3)
        pad = 0.26
        icon(s, icon_name, "065A82", 96, rx + pad, card_y + pad, 0.5)
        text_box(s, rx + pad, card_y + pad + 0.65, rw - 2 * pad, 2.15,
                 text=scenario_text, size=13, italic=True, color=DEEP, line_spacing=1.32)
        text_box(s, rx + pad, card_y + card_h - pad - 0.55, rw - 2 * pad, 0.55,
                 text=f"Q1: {q1}  ·  Q2: {q2}", size=10.5, bold=True, color=MID, line_spacing=1.25)

        if mode == "answer":
            text_box(s, 0.55, card_y + card_h + 0.2, 12.23, 0.5,
                     text="Второй раз за сегодня: режим использования определяет тип, не бренд",
                     size=14, bold=True, color=GOLD_DARK, align=PP_ALIGN.CENTER)
        else:
            text_box(s, 0.55, card_y + card_h + 0.2, 12.23, 0.5,
                     text="4 раунда поднятия руки — модель? чат? агент? приложение?",
                     size=13, italic=True, color=SLATE, align=PP_ALIGN.CENTER)

    speaker_notes(s, load_notes(slide_id))


def build_s11(p):
    scenario_slide(p, slide_id="s11", section_label="Раздел 3 · Сценарий 1",
        title="Фоновый скрипт проверки орфографии — куда его отнести?",
        icon_name="file-code",
        scenario_text="Раз в час фоновый скрипт автоматически проверяет орфографию во "
                       "всех открытых файлах проекта и дописывает список ошибок в "
                       "текстовый лог — без интерфейса, без диалога, без вашего участия "
                       "в моменте проверки.",
        q1="нужно ли взаимодействие с пользователем?",
        q2="нужна ли самостоятельная работа с инструментами?",
        answer="Модель", answer_note="Q1 нет · Q2 нет — самый чистый случай раздела",
        layout="left_text_right_quad", mode="question")


def build_s12(p):
    scenario_slide(p, slide_id="s12", section_label="Раздел 3 · Сценарий 1 · ответ",
        title="Фоновый скрипт проверки орфографии — разминка",
        icon_name="file-code",
        scenario_text="Раз в час фоновый скрипт автоматически проверяет орфографию во "
                       "всех открытых файлах проекта и дописывает список ошибок в "
                       "текстовый лог — без интерфейса, без диалога, без вашего участия "
                       "в моменте проверки.",
        q1="нужно ли взаимодействие с пользователем?",
        q2="нужна ли самостоятельная работа с инструментами?",
        answer="Модель", answer_note="Q1 нет · Q2 нет — самый чистый случай раздела",
        layout="left_text_right_quad", mode="answer")


def build_s13(p):
    scenario_slide(p, slide_id="s13", section_label="Раздел 3 · Сценарий 2 · наименее очевидный",
        title="Ночной скрипт: баг-репорты → критичность → очереди Jira",
        icon_name="git-branch",
        scenario_text="Скрипт запускается каждую ночь по расписанию. Сам скачивает новые "
                       "баг-репорты, классифицирует каждый по критичности через AI и "
                       "автоматически раскладывает по очередям в Jira. Никто не наблюдает "
                       "за процессом.",
        q1="нужно ли взаимодействие с пользователем?",
        q2="нужна ли самостоятельная работа с инструментами?",
        answer="Приложение",
        answer_note="Q1 нет (работает автономно) · Q2 да (сама вызывает API Jira) — реже всего разбираемый угол",
        layout="top_text_bottom_quad", mode="question")


def build_s14(p):
    scenario_slide(p, slide_id="s14", section_label="Раздел 3 · Сценарий 2 · ответ",
        title="Ночной скрипт: баг-репорты → критичность → очереди Jira",
        icon_name="git-branch",
        scenario_text="Скрипт запускается каждую ночь по расписанию. Сам скачивает новые "
                       "баг-репорты, классифицирует каждый по критичности через AI и "
                       "автоматически раскладывает по очередям в Jira. Никто не наблюдает "
                       "за процессом.",
        q1="нужно ли взаимодействие с пользователем?",
        q2="нужна ли самостоятельная работа с инструментами?",
        answer="Приложение",
        answer_note="Q1 нет (работает автономно) · Q2 да (сама вызывает API Jira) — реже всего разбираемый угол",
        layout="top_text_bottom_quad", mode="answer")


def build_s15(p):
    scenario_slide(p, slide_id="s15", section_label="Раздел 3 · Сценарий 3",
        title="AI-ассистент в IDE: inline-подсказка следующей строки",
        icon_name="mouse-pointer-click",
        scenario_text="Вы пишете код в IDE. AI-ассистент на лету достраивает следующую "
                       "строку — вы видите подсказку серым текстом и нажимаете Tab, чтобы "
                       "принять её.",
        q1="нужно ли взаимодействие с пользователем?",
        q2="нужна ли самостоятельная работа с инструментами?",
        answer="Приложение",
        answer_note="Понимание контекста кода само по себе не означает планирование",
        layout="twin_column", mode="question")


def build_s16(p):
    scenario_slide(p, slide_id="s16", section_label="Раздел 3 · Сценарий 3 · ответ",
        title="AI-ассистент в IDE: inline-подсказка следующей строки",
        icon_name="mouse-pointer-click",
        scenario_text="Вы пишете код в IDE. AI-ассистент на лету достраивает следующую "
                       "строку — вы видите подсказку серым текстом и нажимаете Tab, чтобы "
                       "принять её.",
        q1="нужно ли взаимодействие с пользователем?",
        q2="нужна ли самостоятельная работа с инструментами?",
        answer="Приложение",
        answer_note="Понимание контекста кода само по себе не означает планирование",
        layout="twin_column", mode="answer")


def build_s17(p):
    scenario_slide(p, slide_id="s17", section_label="Раздел 3 · Сценарий 4",
        title="Coding-агент: находит баг, правит код, коммитит",
        icon_name="bot",
        scenario_text="Вы даёте текстовую задачу coding-агенту: «почини баг в обработке "
                       "заказов». Агент сам открывает несколько файлов проекта, находит "
                       "проблему, правит код, запускает тесты и, если всё прошло, делает "
                       "коммит.",
        q1="нужно ли взаимодействие с пользователем?",
        q2="нужна ли самостоятельная работа с инструментами?",
        answer="Агент",
        answer_note="Q1 да (цель + вмешательство) · Q2 да (файлы, тесты, план)",
        layout="twin_column_gold_neutral", mode="question")


def build_s18(p):
    scenario_slide(p, slide_id="s18", section_label="Раздел 3 · Сценарий 4 · ответ",
        title="Coding-агент: находит баг, правит код, коммитит",
        icon_name="bot",
        scenario_text="Вы даёте текстовую задачу coding-агенту: «почини баг в обработке "
                       "заказов». Агент сам открывает несколько файлов проекта, находит "
                       "проблему, правит код, запускает тесты и, если всё прошло, делает "
                       "коммит.",
        q1="нужно ли взаимодействие с пользователем?",
        q2="нужна ли самостоятельная работа с инструментами?",
        answer="Агент",
        answer_note="Q1 да (цель + вмешательство) · Q2 да (файлы, тесты, план)",
        layout="twin_column_gold", mode="answer")


def build_s19(p):
    """Раздел 3 closing — the mandatory not-rhetorical class question: where
    would plain deterministic code do just as well, and what do you do when
    AI fails? This is core AI-Failure & Judgment content (CLAUDE.md >=30%
    rule) — an explicit "AI not needed" criterion slide. Unchanged content,
    renumbered s12 -> s19 in Round 2."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 3 · Вопрос всем классом")
    slide_title(s, "Где обычный код справился бы не хуже — и что делать при сбое AI?", y=0.75, size=23)

    q_y = 1.95
    ocean_box(s, 0.55, q_y, 12.23, 1.35, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.6)
    text_box(s, 0.85, q_y + 0.16, 11.6, 1.05,
             text="Для какого из четырёх сценариев детерминированный скрипт, регулярные "
                  "выражения или готовые правила справились бы не хуже? И что бы вы "
                  "сделали, если бы AI здесь дал сбой?",
             size=15.5, bold=True, color=DEEP, line_spacing=1.3, anchor=MSO_ANCHOR.MIDDLE)

    grid_y = q_y + 1.6
    grid_h = 7.05 - grid_y
    gap = 0.28
    cw = (12.23 - gap) / 2
    cards = [
        ("compass", "Признаки «AI здесь не нужен»",
         ["Простое детерминированное правило (regex, справочник, "
          "порог) справляется не хуже, а результат предсказуем",
          "Цена ошибки высока, а проверка человеком не быстрее, "
          "чем сделать задачу самому",
          "Задача разовая и небольшая — сложность агента не окупается"]),
        ("shield-check", "Что делать при сбое AI",
         ["Проверка человеком перед автоматическим действием",
          "Логирование для отката к предыдущему состоянию",
          "Пороги уверенности — ниже порога решение уходит человеку"]),
    ]
    for i, (ic, title, items) in enumerate(cards):
        cx = 0.55 + i * (cw + gap)
        ocean_box(s, cx, grid_y, cw, grid_h)
        pad = 0.26
        icon(s, ic, "028090", 64, cx + pad, grid_y + pad, 0.4)
        text_box(s, cx + pad + 0.55, grid_y + pad - 0.02, cw - 2 * pad - 0.55, 0.5,
                 text=title, size=14, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
        iy = grid_y + pad + 0.65
        item_h = (grid_h - pad - 0.65 - pad) / len(items)
        for it in items:
            text_box(s, cx + pad, iy, 0.24, item_h, text="—", size=13, bold=True, color=LIGHT)
            text_box(s, cx + pad + 0.28, iy, cw - 2 * pad - 0.28, item_h,
                     text=it, size=11.5, color=DEEP, line_spacing=1.25)
            iy += item_h
    speaker_notes(s, load_notes("s19"))


def build_s20(p):
    """Раздел 4 intro — find-the-fake mechanic explainer + honest-labeling
    disclosure (both answers are author-written for this exercise, not real
    model output) + Sem-1 callback. Unchanged content, renumbered s13 -> s20
    in Round 2."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 4 · Найди подделку")
    slide_title(s, "Один точный факт, одна убедительная выдумка — какая деталь подложена?", y=0.75, size=22)

    mech_y = 1.95
    ocean_box(s, 0.55, mech_y, 12.23, 1.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.4)
    icon(s, "help-circle", "028090", 96, 0.85, mech_y + 0.24, 0.55)
    text_box(s, 1.6, mech_y + 0.18, 10.9, 1.2,
             text="3 раунда: короткий фактический вопрос, два варианта AI-ответа. "
                  "2 раунда поднятия руки — «подделка в А?», «подделка в Б?» — затем "
                  "разбор и обсуждение «что бы вы проверили первым».",
             size=13.5, color=DEEP, line_spacing=1.35, anchor=MSO_ANCHOR.MIDDLE)

    disc_y = mech_y + 1.75
    ocean_box(s, 0.55, disc_y, 12.23, 1.1, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    icon(s, "flag", "F0AB00", 64, 0.85, disc_y + 0.22, 0.4)
    text_box(s, 1.45, disc_y + 0.12, 11.0, 0.9,
             text="Честная маркировка: оба варианта в каждом раунде написаны автором "
                  "методического комплекта — это не реальный вызов модели. Формат и "
                  "стиль имитируют типичный уверенный ответ AI-чата.",
             size=12, italic=True, color=DEEP, line_spacing=1.3, anchor=MSO_ANCHOR.MIDDLE)

    call_y = disc_y + 1.3
    call_h = 7.05 - call_y
    ocean_box(s, 0.55, call_y, 12.23, call_h)
    icon(s, "rotate-ccw", "065A82", 64, 0.85, call_y + (call_h - 0.4) / 2, 0.4)
    text_box(s, 1.5, call_y, 10.9, call_h,
             text="На Семинаре 1 вы делились историями, где AI подвёл — установка "
                  "«AI знает всё» как анти-паттерн. Сегодня тренируем конкретный навык "
                  "для той же установки: как поймать AI на уверенно поданной неправде.",
             size=13, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.35)
    speaker_notes(s, load_notes("s20"))


def fake_round_slide(p, *, slide_id, round_no, question, opt_a, opt_b, fake_letter,
                      explanation, check_hint, layout, mode="answer"):
    """Shared builder for the 3 find-the-fake rounds, now split into a
    Q-slide + A-slide pair per round (Round 2 fix — presentation-critic P0:
    the old single-slide version drew a GOLD border around the fake option
    AND an open gold reveal-panel on the SAME slide as the question, which
    leaked the answer by colour alone before any vote happened). Both
    option cards are ALWAYS identical format (plain text, same box type) —
    sem-01 known bug #3 (asymmetric formats leak the answer) — preserved in
    BOTH modes; `mode="question"` additionally keeps both borders neutral
    LIGHT and omits the reveal panel entirely (replaced by a neutral vote
    hint), `mode="answer"` is the original reveal behaviour."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    tag = f"Раздел 4 · Раунд {round_no} из 3" if mode == "question" else f"Раздел 4 · Раунд {round_no} из 3 · ответ"
    section_tag(s, 0.55, 0.4, tag)
    slide_title(s, question, y=0.75, size=19)

    grid_y = 1.7

    if layout == "side_by_side":
        gap = 0.28
        cw = (12.23 - gap) / 2
        ch = 2.55
        for i, (letter, text) in enumerate([("А", opt_a), ("Б", opt_b)]):
            cx = 0.55 + i * (cw + gap)
            is_fake = (mode == "answer" and letter == fake_letter)
            stroke = GOLD if is_fake else LIGHT
            ocean_box(s, cx, grid_y, cw, ch, stroke=stroke, stroke_pt=1.6 if is_fake else 1.4)
            pad = 0.22
            text_box(s, cx + pad, grid_y + pad - 0.02, cw - 2 * pad, 0.32,
                     text=f"Вариант {letter}", size=14, bold=True, color=MID)
            text_box(s, cx + pad, grid_y + pad + 0.38, cw - 2 * pad, ch - 0.6,
                     text=text, size=11.5, color=DEEP, line_spacing=1.28)
        block_bottom = grid_y + ch
    elif layout == "stacked":
        rh = 1.42
        row_gap = 0.16
        for i, (letter, text) in enumerate([("А", opt_a), ("Б", opt_b)]):
            ry = grid_y + i * (rh + row_gap)
            is_fake = (mode == "answer" and letter == fake_letter)
            stroke = GOLD if is_fake else LIGHT
            ocean_box(s, 0.55, ry, 12.23, rh, stroke=stroke, stroke_pt=1.6 if is_fake else 1.4)
            pad = 0.2
            text_box(s, 0.55 + pad, ry + pad - 0.02, 1.5, 0.3,
                     text=f"Вариант {letter}", size=13.5, bold=True, color=MID)
            text_box(s, 0.55 + pad + 1.65, ry + pad - 0.06, 12.23 - 2 * pad - 1.65, rh - 2 * pad + 0.1,
                     text=text, size=11, color=DEEP, line_spacing=1.22,
                     anchor=MSO_ANCHOR.MIDDLE)
        block_bottom = grid_y + 2 * rh + row_gap

    reveal_y = block_bottom + 0.22
    reveal_h = 7.05 - reveal_y
    if mode == "answer":
        ocean_box(s, 0.55, reveal_y, 12.23, reveal_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.5)
        icon(s, "flag", "F0AB00", 64, 0.78, reveal_y + 0.14, 0.3)
        text_box(s, 1.22, reveal_y + 0.1, 10.9, 0.34,
                 text=f"Подделка: вариант {fake_letter}", size=13.5, bold=True, color=DEEP)
        text_box(s, 1.22, reveal_y + 0.46, 11.3, reveal_h - 0.78,
                 text=explanation, size=10, color=DEEP, line_spacing=1.22)
        text_box(s, 0.78, reveal_y + reveal_h - 0.3, 11.4, 0.28,
                 text=f"Что проверить первым: {check_hint}", size=9.5, italic=True, color=SLATE)
    else:
        ocean_box(s, 0.55, reveal_y, 12.23, reveal_h, fill=SURFACE, stroke=TEAL, stroke_pt=1.4)
        icon(s, "hand", "028090", 64, 0.78, reveal_y + (reveal_h - 0.34) / 2, 0.34)
        text_box(s, 1.35, reveal_y, 10.8, reveal_h,
                 text="2 раунда поднятия руки — подделка в А или в Б?",
                 size=14.5, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes(slide_id))


_ROUND1_KW = dict(
    round_no=1,
    question="Когда вышел первый стабильный релиз Python и кто его автор?",
    opt_a="Первый стабильный релиз Python 1.0 вышел в январе 1994 года. Автор "
          "языка — Гвидо ван Россум, на тот момент сотрудник голландского "
          "института CWI (Centrum Wiskunde & Informatica).",
    opt_b="Первый стабильный релиз Python 1.0 вышел в марте 1995 года. Автор "
          "языка — Гвидо ван Россум, на тот момент сотрудник голландского "
          "института CWI; релиз был приурочен к внутренней конференции CWI "
          "по функциональным языкам.",
    fake_letter="Б",
    explanation="Дата и институт CWI в варианте А верны (26 января 1994). В "
                "варианте Б дата и особенно «приурочен к внутренней конференции "
                "CWI по функциональным языкам» — придуманная деталь: звучит "
                "правдоподобно (реальная организация, реалистичный формат), но "
                "это выдумка — точный факт «утоплен» в несуществующем контексте.",
    check_hint="дата релиза на python.org / Wikipedia",
    layout="side_by_side")

_ROUND2_KW = dict(
    round_no=2,
    question="Что такое HTTP/2 и чем он принципиально отличается от HTTP/1.1?",
    opt_a="HTTP/2 стандартизирован в 2015 году (RFC 7540). Ключевое отличие — "
          "мультиплексирование: несколько запросов и ответов передаются "
          "одновременно по одному TCP-соединению, что устраняет "
          "head-of-line-блокировку на уровне HTTP.",
    opt_b="HTTP/2 стандартизирован в 2015 году (RFC 7540). Ключевое отличие — "
          "переход на протокол UDP вместо TCP, что позволило полностью убрать "
          "задержки установления соединения и сделало HTTP/2 совместимым с "
          "QUIC «из коробки» ещё на этапе стандартизации 2015 года.",
    fake_letter="Б",
    explanation="HTTP/2 работает поверх TCP, не UDP — переход на UDP произошёл "
                "позже, в HTTP/3 (RFC 9114, 2022), поверх QUIC. Мультиплексирование "
                "в варианте А — реальная ключевая черта HTTP/2. Вариант Б смешивает "
                "реальный факт (RFC 7540, 2015) с придуманным техническим "
                "утверждением — синтаксически безупречная неправда.",
    check_hint="номер RFC на ietf.org",
    layout="side_by_side")

_ROUND3_KW = dict(
    round_no=3,
    question="Какая структура лежит в основе B-дерева и какова сложность поиска?",
    opt_a="B-дерево (или B+-дерево) — сбалансированное дерево поиска, где "
          "каждый узел может иметь несколько ключей и потомков. Типичная "
          "сложность поиска — O(log n), где основание логарифма равно порядку "
          "дерева (обычно от десятков до сотен).",
    opt_b="B-дерево (или B+-дерево) — сбалансированное дерево поиска, где "
          "каждый узел может иметь несколько ключей и потомков. Сложность "
          "поиска — O(log n); термин «B» в названии официально означает "
          "«Boeing», поскольку структура была впервые формализована инженерами "
          "Boeing для индексации данных о деталях самолётов в 1970 году.",
    fake_letter="Б",
    explanation="B-дерево описано Bayer & McCreight в 1972 в Boeing Scientific "
                "Research Labs — происхождение буквы «B» реально предмет споров "
                "историков (Bayer, Boeing, balanced — все версии встречаются, и "
                "сам McCreight говорил, что авторы так и не решили). "
                "«Официально означает Boeing» в варианте Б — придуманная "
                "избыточная уверенность там, где единственно верного ответа не "
                "существует. Третий тип галлюцинации: ложная уверенность там, где "
                "спорный факт не имеет официального статуса.",
    check_hint="оригинальная статья Bayer & McCreight, интервью с автором",
    layout="stacked")


def build_s21(p):
    fake_round_slide(p, slide_id="s21", mode="question", **_ROUND1_KW)


def build_s22(p):
    fake_round_slide(p, slide_id="s22", mode="answer", **_ROUND1_KW)


def build_s23(p):
    fake_round_slide(p, slide_id="s23", mode="question", **_ROUND2_KW)


def build_s24(p):
    fake_round_slide(p, slide_id="s24", mode="answer", **_ROUND2_KW)


def build_s25(p):
    fake_round_slide(p, slide_id="s25", mode="question", **_ROUND3_KW)


def build_s26(p):
    fake_round_slide(p, slide_id="s26", mode="answer", **_ROUND3_KW)


def build_s27(p):
    """Раздел 4 closing reflection — "which tell was the most subtle" +
    3-pattern recap (rare-fact drowned in plausible context / real fact +
    fabricated technical claim / false confidence where no single right
    answer exists). Distinct from the 3 round-slides: no vote mechanic,
    pure reflective summary — breaks the repeated-round rhythm. Unchanged
    content, renumbered s17 -> s27 in Round 2."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 4 · Рефлексия")
    slide_title(s, "Три маски галлюцинации — какая была самой незаметной?", y=0.75, size=25)

    grid_y = 1.95
    gap = 0.26
    cw = (12.23 - 2 * gap) / 3
    ch = 3.6
    cards = [
        ("hash", "Раунд 1 · Python", "Точный факт «утоплен» в правдоподобном, но выдуманном контексте (конференция, которой не было)"),
        ("network", "Раунд 2 · HTTP/2", "Реальный факт (RFC, год) смешан с придуманным техническим утверждением (UDP вместо TCP)"),
        ("help-circle", "Раунд 3 · B-дерево", "Ложная уверенность там, где единственно верного ответа не существует"),
    ]
    for i, (ic, title, desc) in enumerate(cards):
        cx = 0.55 + i * (cw + gap)
        ocean_box(s, cx, grid_y, cw, ch)
        pad = 0.22
        icon(s, ic, "028090", 72, cx + (cw - 0.5) / 2, grid_y + pad, 0.5)
        text_box(s, cx + pad, grid_y + pad + 0.65, cw - 2 * pad, 0.4,
                 text=title, size=13, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, cx + pad, grid_y + pad + 1.1, cw - 2 * pad, ch - 1.4,
                 text=desc, size=11, color=SLATE, line_spacing=1.3, align=PP_ALIGN.CENTER)

    q_y = grid_y + ch + 0.3
    q_h = 7.05 - q_y
    ocean_box(s, 0.55, q_y, 12.23, q_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.5)
    text_box(s, 0.85, q_y, 11.6, q_h,
             text="Какой признак галлюцинации из сегодняшних примеров показался вам самым незаметным?",
             size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, line_spacing=1.3)
    speaker_notes(s, load_notes("s27"))


def build_s28(p):
    """Раздел 5 intro — 3-card definitions (bias / sycophancy / distribution
    shift), matching the visual pattern students saw on lec-01 s25 this
    morning (same 3 icons, same layout family) for continuity, plus a note
    that today's vignettes are new (not the canonical GPT-4o example).
    Unchanged content, renumbered s18 -> s28 in Round 2. Round-2 P2 fix
    (presentation-critic): title translated to Russian instead of a
    bare-English H1 — established-term exception covers single bare
    occurrences after glossing, not a whole title in Latin script.
    Round-3 point fix: title still listed three bare English terms
    side-by-side with zero Russian words in between (bias, sycophancy,
    distribution shift) even though the cards below already gloss each
    term inline (e.g. "Bias (смещение)"). Title rewritten fully in
    Russian to match the cards' glossing pattern; English terms remain
    visible in the 3 cards immediately below."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 5 · Три типа провала")
    slide_title(s, "Три типа провала данных: смещение, подстройка, сдвиг распределения", y=0.75, size=22)

    grid_y = 1.9
    gap = 0.28
    cw = (12.23 - 2 * gap) / 3
    ch = 3.5
    cards = [
        ("scale", "Bias (смещение)", "Модель воспроизводит исторический перекос обучающих данных, не оценивает по существу", MID),
        ("smile", "Sycophancy (подстройка)", "Модель подстраивается под ожидание пользователя вместо честной оценки", LIGHT),
        ("trending-down", "Distribution shift (сдвиг распределения)", "Модель тихо деградирует на данных, непохожих на обучающие", TEAL),
    ]
    for i, (ic, title, desc, col) in enumerate(cards):
        cx = 0.55 + i * (cw + gap)
        ocean_box(s, cx, grid_y, cw, ch)
        pad = 0.22
        filled_rect(s, cx + pad, grid_y + pad, 0.62, 0.62, col, radius=True, radius_adj=0.3)
        icon(s, ic, "FFFFFF", 64, cx + pad + 0.13, grid_y + pad + 0.13, 0.36)
        text_box(s, cx + pad + 0.78, grid_y + pad, cw - 2 * pad - 0.78, 0.62,
                 text=title, size=15, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, cx + pad, grid_y + pad + 0.85, cw - 2 * pad, ch - 1.1,
                 text=desc, size=12, color=SLATE, line_spacing=1.32)

    note_y = grid_y + ch + 0.28
    note_h = 7.05 - note_y
    ocean_box(s, 0.55, note_y, 12.23, note_h, fill=SURFACE, stroke=TEAL)
    icon(s, "flag", "028090", 64, 0.85, note_y + (note_h - 0.36) / 2, 0.36)
    text_box(s, 1.45, note_y, 11.0, note_h,
             text="Четыре новые виньетки ниже написаны для этого упражнения — не дословный "
                  "повтор канонических примеров лекции (включая реальный случай GPT-4o "
                  "sycophancy rollback апреля 2025 — этот случай отдельный, реальный).",
             size=11.5, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.3)
    speaker_notes(s, load_notes("s28"))


def vignette_slide(p, *, slide_id, section_label, title, icon_name, story_text,
                    answer_label, answer_col, explanation, layout, mode="answer"):
    """Round-2: `mode="question"` renders ONLY the story card (MIDDLE-
    anchored per the visual-mass P1 fix) plus a neutral vote hint — no
    colored answer-badge/column, matching the presentation-critic P0 fix
    (the old single-slide version put the colored "Bias"/"Sycophancy"/
    "Distribution shift" badge on the same slide as the scenario text,
    before the vote). `mode="answer"` is the original reveal behaviour,
    unchanged layout logic."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, section_label)
    slide_title(s, title, y=0.75, size=22)

    if mode == "question":
        story_y = 1.9
        story_h = 4.35
        ocean_box(s, 0.55, story_y, 12.23, story_h)
        pad = 0.3
        icon(s, icon_name, "065A82", 96, 0.55 + pad, story_y + pad, 0.55)
        text_box(s, 0.55 + pad + 0.75, story_y + pad, 12.23 - 2 * pad - 0.75, story_h - 2 * pad - 0.7,
                 text=story_text, size=13.5, italic=True, color=DEEP, line_spacing=1.42,
                 anchor=MSO_ANCHOR.MIDDLE)
        hint_y = story_y + story_h - pad - 0.55
        ocean_box(s, 0.55 + pad, hint_y, 12.23 - 2 * pad, 0.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.2)
        icon(s, "hand", "028090", 64, 0.55 + pad + 0.15, hint_y + 0.1, 0.34)
        text_box(s, 0.55 + pad + 0.65, hint_y, 12.23 - 2 * pad - 0.8, 0.55,
                 text="Bias? Sycophancy? Distribution shift? Не уверен? — 4 раунда поднятия руки",
                 size=12, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
        speaker_notes(s, load_notes(slide_id))
        return

    if layout == "wide_story_bottom_answer":
        story_y = 1.9
        story_h = 2.75
        ocean_box(s, 0.55, story_y, 12.23, story_h)
        pad = 0.28
        icon(s, icon_name, "065A82", 96, 0.55 + pad, story_y + (story_h - 0.55) / 2, 0.55)
        text_box(s, 0.55 + pad + 0.75, story_y, 12.23 - 2 * pad - 0.75, story_h,
                 text=story_text, size=13.5, italic=True, color=DEEP, line_spacing=1.42,
                 anchor=MSO_ANCHOR.MIDDLE)
        ans_y = story_y + story_h + 0.3
        ans_h = 7.05 - ans_y
        filled_rect(s, 0.55, ans_y, 3.1, ans_h, answer_col, radius=True, radius_adj=0.16)
        text_box(s, 0.55, ans_y, 3.1, ans_h, text=answer_label, size=19, bold=True,
                 color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
        ocean_box(s, 0.55 + 3.3, ans_y, 12.23 - 3.3, ans_h, fill=SURFACE, stroke=LIGHT)
        text_box(s, 0.55 + 3.3 + 0.22, ans_y, 12.23 - 3.3 - 0.44, ans_h,
                 text=explanation, size=12.5, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.35)

    elif layout == "left_answer_right_story":
        row_y = 1.9
        row_h = 4.35
        col_w = 2.9
        filled_rect(s, 0.55, row_y, col_w, row_h, answer_col, radius=True, radius_adj=0.1)
        icon(s, icon_name, "FFFFFF", 96, 0.55 + (col_w - 0.6) / 2, row_y + (row_h - 0.6) / 2 - 0.55, 0.6)
        text_box(s, 0.6, row_y + (row_h - 0.6) / 2 + 0.15, col_w - 0.1, 0.7, text=answer_label, size=18,
                 bold=True, color=WHITE, align=PP_ALIGN.CENTER, line_spacing=1.15)
        sx = 0.55 + col_w + 0.3
        sw = 12.23 - col_w - 0.3
        ocean_box(s, sx, row_y, sw, row_h)
        pad = 0.28
        text_box(s, sx + pad, row_y + pad, sw - 2 * pad, 2.2,
                 text=story_text, size=13, italic=True, color=DEEP, line_spacing=1.4)
        text_box(s, sx + pad, row_y + pad + 2.35, sw - 2 * pad, row_h - pad - 2.35 - pad,
                 text=explanation, size=12, color=SLATE, line_spacing=1.35)

    speaker_notes(s, load_notes(slide_id))


def build_s29(p):
    """Icon Round-2 fix: uses neutral `briefcase` (hiring/resume context)
    instead of `scale` — `scale` is the answer-hinting icon reused on the
    A-slide (s30) for the "Bias" badge; using it here on the Q-slide would
    leak the answer via icon choice before the vote, the same class of
    P0 bug the reveal-architecture fix targets (same reasoning already
    applied correctly to s31, which uses `code` instead of `smile`)."""
    vignette_slide(p, slide_id="s29", section_label="Раздел 5 · Виньетка 1",
        title="Скрининг резюме DevOps-инженеров занижает кандидатов без диплома — почему?",
        icon_name="briefcase",
        story_text="Команда обучила модель ранжирования резюме для отбора кандидатов "
                    "на DevOps-позиции, используя пять лет исторических данных о найме. "
                    "Модель систематически занижает оценку резюме без профильного "
                    "диплома, даже при релевантных сертификатах и опыте — потому что в "
                    "обучающих данных почти все нанятые в прошлом имели профильное "
                    "образование, а кандидаты без диплома реже проходили дальше "
                    "человеческого скрининга на предыдущих этапах.",
        answer_label="Bias (смещение)", answer_col=MID, explanation="",
        layout="wide_story_bottom_answer", mode="question")


def build_s30(p):
    vignette_slide(p, slide_id="s30", section_label="Раздел 5 · Виньетка 1 · ответ",
        title="Скрининг резюме DevOps-инженеров занижает кандидатов без диплома",
        icon_name="scale",
        story_text="Команда обучила модель ранжирования резюме для отбора кандидатов "
                    "на DevOps-позиции, используя пять лет исторических данных о найме. "
                    "Модель систематически занижает оценку резюме без профильного "
                    "диплома, даже при релевантных сертификатах и опыте — потому что в "
                    "обучающих данных почти все нанятые в прошлом имели профильное "
                    "образование, а кандидаты без диплома реже проходили дальше "
                    "человеческого скрининга на предыдущих этапах.",
        answer_label="Bias (смещение)",
        answer_col=MID,
        explanation="Модель воспроизводит исторический перекос — структурное "
                    "предпочтение дипломированных кандидатов на прошлых этапах отбора — "
                    "статистически предсказывая «такие профили обычно отказывали», не "
                    "оценивая кандидата по существу.",
        layout="wide_story_bottom_answer", mode="answer")


def build_s31(p):
    vignette_slide(p, slide_id="s31", section_label="Раздел 5 · Виньетка 2",
        title="AI хвалит код с необработанным пустым массивом — почему?",
        icon_name="code",
        story_text="Разработчик просит AI-ассистента в IDE проверить реализацию "
                    "сортировки. В реализации ошибка — метод не обрабатывает пустой "
                    "массив и упадёт с исключением. Разработчик пишет: «Я уверен, что "
                    "тут всё верно, просто хочу второе мнение для отчёта». AI отвечает: "
                    "«Да, реализация выглядит корректной и эффективной, хорошая "
                    "работа!» — не упоминая проблему с пустым массивом.",
        answer_label="Sycophancy (подстройка)", answer_col=LIGHT, explanation="",
        layout="left_answer_right_story", mode="question")


def build_s32(p):
    vignette_slide(p, slide_id="s32", section_label="Раздел 5 · Виньетка 2 · ответ",
        title="AI хвалит код с необработанным пустым массивом",
        icon_name="smile",
        story_text="Разработчик просит AI-ассистента в IDE проверить реализацию "
                    "сортировки. В реализации ошибка — метод не обрабатывает пустой "
                    "массив и упадёт с исключением. Разработчик пишет: «Я уверен, что "
                    "тут всё верно, просто хочу второе мнение для отчёта». AI отвечает: "
                    "«Да, реализация выглядит корректной и эффективной, хорошая "
                    "работа!» — не упоминая проблему с пустым массивом.",
        answer_label="Sycophancy (подстройка)",
        answer_col=LIGHT,
        explanation="Формулировка запроса («я уверен, что всё верно») задаёт ожидание "
                    "согласия, и модель, обученная через RLHF на предпочтении приятных "
                    "ответов, поддерживает уверенность пользователя вместо того, чтобы "
                    "указать на реальную ошибку.",
        layout="left_answer_right_story", mode="answer")


def build_s33(p):
    """Icon Round-2 fix: uses neutral `ticket` (support-ticket routing
    context) instead of `trending-down` — `trending-down` is the answer-
    hinting icon reused on the A-slide (s34) for "Distribution shift";
    same fix class as s29 (was `scale`) and consistent with s31 (already
    correct, uses `code` not `smile`)."""
    vignette_slide(p, slide_id="s33", section_label="Раздел 5 · Виньетка 3",
        title="Классификатор обращений тихо деградирует на новой линейке продуктов — почему?",
        icon_name="ticket",
        story_text="Компания маршрутизирует обращения в техподдержку по категориям — "
                    "модель обучена на данных 2023 года. В 2026 году компания выпустила "
                    "новую линейку продуктов с новой терминологией. Модель продолжает "
                    "уверенно классифицировать обращения про новые продукты, но "
                    "существенно менее точно — путает категории. Деградацию никто не "
                    "заметил сразу, потому что явных сбоев не было — модель просто "
                    "тише чаще ошибается.",
        answer_label="Distribution shift (сдвиг распределения)", answer_col=TEAL,
        explanation="", layout="wide_story_bottom_answer", mode="question")


def build_s34(p):
    """Round-2 Russification fix (P1, presentation-critic): explanation
    now glosses bias/sycophancy inline in Russian on first bare use at this
    point in the deck (same pattern as s28), instead of leaving bare
    English "bias"/"sycophancy" inside a Russian sentence."""
    vignette_slide(p, slide_id="s34", section_label="Раздел 5 · Виньетка 3 · ответ",
        title="Классификатор обращений тихо деградирует на новой линейке продуктов",
        icon_name="trending-down",
        story_text="Компания маршрутизирует обращения в техподдержку по категориям — "
                    "модель обучена на данных 2023 года. В 2026 году компания выпустила "
                    "новую линейку продуктов с новой терминологией. Модель продолжает "
                    "уверенно классифицировать обращения про новые продукты, но "
                    "существенно менее точно — путает категории. Деградацию никто не "
                    "заметил сразу, потому что явных сбоев не было — модель просто "
                    "тише чаще ошибается.",
        answer_label="Distribution shift (сдвиг распределения)",
        answer_col=TEAL,
        explanation="Модель, обученная на данных одного периода, столкнулась с новым "
                    "распределением входных данных (новая терминология, новые "
                    "категории обращений) и «тихо» деградирует без явного сбоя — "
                    "классический признак сдвига распределения, а не смещения (bias) "
                    "или подстройки (sycophancy).",
        layout="wide_story_bottom_answer", mode="answer")


def build_s35(p):
    """Vignette 4 Q-slide — the deliberately ambiguous one. Dashed gold
    border on the story card carries over to the A-slide (s36) as a
    continuity signal, but here there is NO answer content at all — just
    the story and a neutral vote hint (Round-2 P0 fix: the old single-slide
    version showed both "Sycophancy"/"Distribution shift" cards marked
    "тоже верно" on the same slide as the scenario)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 5 · Виньетка 4 · без единственного ответа")
    slide_title(s, "Стажёр спрашивает про «любимую» библиотеку логирования — и получает согласие", y=0.75, size=20)

    story_y = 1.9
    story_h = 4.35
    dashed_box(s, 0.55, story_y, 12.23, story_h, fill=SURFACE, stroke=GOLD, stroke_pt=1.8)
    pad = 0.3
    icon(s, "help-circle", "F0AB00", 96, 0.55 + pad, story_y + pad, 0.5)
    text_box(s, 0.55 + pad + 0.7, story_y + pad, 12.23 - 2 * pad - 0.7, story_h - 2 * pad - 0.7,
             text="Инженер-стажёр спрашивает AI-ассистента, актуальна ли для нового "
                  "проекта библиотека логирования, которую он использовал в 2023 году. "
                  "Добавляет: «мне она всегда нравилась, надеюсь, она всё ещё топовая». "
                  "AI отвечает: «Да, это отличный и современный выбор, смело "
                  "используйте её» — хотя к 2026 году сообщество в основном перешло на "
                  "библиотеку с лучшей поддержкой структурированных логов, а "
                  "рекомендованная почти не получает обновлений.",
             size=12.5, italic=True, color=DEEP, line_spacing=1.35, anchor=MSO_ANCHOR.MIDDLE)
    hint_y = story_y + story_h - pad - 0.55
    ocean_box(s, 0.55 + pad, hint_y, 12.23 - 2 * pad, 0.55, fill=SURFACE, stroke=GOLD, stroke_pt=1.4)
    icon(s, "hand", "F0AB00", 64, 0.55 + pad + 0.15, hint_y + 0.1, 0.34)
    text_box(s, 0.55 + pad + 0.65, hint_y, 12.23 - 2 * pad - 0.8, 0.55,
             text="Bias? Sycophancy? Distribution shift? Не уверен? — 4 раунда поднятия руки",
             size=12, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s35"))


def build_s36(p):
    """Vignette 4 A-slide (reveal). Visually distinct (dashed gold border,
    no single-color answer badge, both labels shown side by side as
    equally valid) to signal to students this slide behaves differently
    from the previous three before they even read the text. Round-2 split
    partner of s35."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 5 · Виньетка 4 · без единственного ответа")
    slide_title(s, "Стажёр спрашивает про «любимую» библиотеку логирования — и получает согласие", y=0.75, size=20)

    story_y = 1.9
    story_h = 2.85
    dashed_box(s, 0.55, story_y, 12.23, story_h, fill=SURFACE, stroke=GOLD, stroke_pt=1.8)
    pad = 0.28
    icon(s, "help-circle", "F0AB00", 96, 0.55 + pad, story_y + pad, 0.5)
    text_box(s, 0.55 + pad + 0.7, story_y + pad - 0.05, 12.23 - 2 * pad - 0.7, story_h - 0.5,
             text="Инженер-стажёр спрашивает AI-ассистента, актуальна ли для нового "
                  "проекта библиотека логирования, которую он использовал в 2023 году. "
                  "Добавляет: «мне она всегда нравилась, надеюсь, она всё ещё топовая». "
                  "AI отвечает: «Да, это отличный и современный выбор, смело "
                  "используйте её» — хотя к 2026 году сообщество в основном перешло на "
                  "библиотеку с лучшей поддержкой структурированных логов, а "
                  "рекомендованная почти не получает обновлений.",
             size=12, italic=True, color=DEEP, line_spacing=1.32)

    ans_y = story_y + story_h + 0.25
    ans_h = 7.05 - ans_y
    gap = 0.24
    aw = (12.23 - gap) / 2
    both = [
        ("smile", "Sycophancy — тоже верно", LIGHT,
         "Модель уловила эмоциональную привязанность стажёра и подстроила тон ответа под ожидание"),
        ("trending-down", "Distribution shift — тоже верно", TEAL,
         "Модель обучена на данных, где библиотека была современным выбором, и не «знает» о сдвиге экосистемы"),
    ]
    for i, (ic, label, col, desc) in enumerate(both):
        cx = 0.55 + i * (aw + gap)
        ocean_box(s, cx, ans_y, aw, ans_h, stroke=col, stroke_pt=1.6)
        p2 = 0.22
        icon(s, ic, "028090", 64, cx + p2, ans_y + p2, 0.34)
        text_box(s, cx + p2 + 0.44, ans_y + p2 - 0.02, aw - 2 * p2 - 0.44, 0.4,
                 text=label, size=12.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, cx + p2, ans_y + p2 + 0.5, aw - 2 * p2, ans_h - p2 - 0.6,
                 text=desc, size=11, color=SLATE, line_spacing=1.3)
    speaker_notes(s, load_notes("s36"))


def build_s37(p):
    """Раздел 5 closing reflection — "what's more dangerous in your future
    field" — pure discussion prompt, no vote mechanic, breaks rhythm before
    moving to the light bridge section. Unchanged content, renumbered
    s23 -> s37 in Round 2. Round-2 P1 Russification fix (presentation-
    critic): each tile now carries a second, smaller Russian-translation
    line — glossing was on s28 (5 slides earlier at old numbering, ~9 at
    new), too far back for a student to be expected to recall it here."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 5 · Закрывающая рефлексия")
    slide_title(s, "Что опаснее в вашей будущей профессиональной области?", y=0.9, size=27)

    grid_y = 2.15
    gap = 0.26
    cw = (12.23 - 2 * gap) / 3
    ch = 3.55
    cards = [
        ("scale", "Bias", "смещение", MID),
        ("smile", "Sycophancy", "подстройка", LIGHT),
        ("trending-down", "Distribution shift", "сдвиг распределения", TEAL),
    ]
    for i, (ic, label, ru, col) in enumerate(cards):
        cx = 0.55 + i * (cw + gap)
        filled_rect(s, cx, grid_y, cw, ch, col, radius=True, radius_adj=0.14)
        icon(s, ic, "FFFFFF", 96, cx + (cw - 0.95) / 2, grid_y + 0.45, 0.95)
        text_box(s, cx + 0.1, grid_y + ch - 1.05, cw - 0.2, 0.5, text=label, size=16,
                 bold=True, color=WHITE, align=PP_ALIGN.CENTER, line_spacing=1.1)
        text_box(s, cx + 0.1, grid_y + ch - 0.55, cw - 0.2, 0.4, text=ru, size=11.5,
                 italic=True, color=RGBColor(0xE5, 0xEA, 0xF0), align=PP_ALIGN.CENTER)

    prompt_y = grid_y + ch + 0.3
    prompt_h = 7.05 - prompt_y
    ocean_box(s, 0.55, prompt_y, 12.23, prompt_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.4)
    text_box(s, 0.55, prompt_y, 12.23, prompt_h,
             text="Назовите конкретную область своей будущей специализации — не общий ответ",
             size=15, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    speaker_notes(s, load_notes("s37"))


def build_s38(p):
    """Раздел 6 — light bridge to Lecture 2 (tokens/embeddings/attention/
    temperature). Short hook, no depth (per facilitator-guide: намеренно
    короткий крючок, не мини-лекция). Unchanged content, renumbered
    s24 -> s38 in Round 2."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 6 · Мостик к Лекции 2")
    slide_title(s, "Сегодня — снаружи. Дальше — заглянем внутрь модели", y=0.85, size=27)

    body_y = 2.2
    ocean_box(s, 0.55, body_y, 12.23, 3.0)
    pad = 0.32
    text_box(s, 0.55 + pad, body_y + pad, 12.23 - 2 * pad, 2.4,
             text="Сегодня мы тренировались классифицировать AI-системы снаружи — "
                  "по типу задачи, по способу реализации, по типу ошибки. На "
                  "следующей лекции заглянем внутрь: как модель «читает» текст, как "
                  "представляет смысл числами, что заставляет её обращать внимание "
                  "на одни части входа больше, чем на другие, и почему один и тот же "
                  "запрос иногда даёт разные ответы.",
             size=15, color=DEEP, line_spacing=1.45)

    tags_y = body_y + 3.3
    tags = [("hash", "Токены"), ("layers", "Эмбеддинги"), ("scan", "Внимание"), ("gauge", "Температура")]
    gap = 0.24
    tw = (12.23 - gap * (len(tags) - 1)) / len(tags)
    for i, (ic, label) in enumerate(tags):
        cx = 0.55 + i * (tw + gap)
        filled_rect(s, cx, tags_y, tw, 0.95, SURFACE, stroke=TEAL, stroke_pt=1.3, radius=True, radius_adj=0.14)
        icon(s, ic, "028090", 64, cx + (tw - 0.4) / 2, tags_y + 0.14, 0.4)
        text_box(s, cx, tags_y + 0.58, tw, 0.32, text=label, size=12.5, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s38"))


def build_s39(p):
    """Раздел 7 — the handout memo slide, «Как выбрать тип AI за 60 секунд».
    Compiles what already happened (checklist + mini-quadrant + 3 AI-not-
    needed signs + 3 failure types) — explicitly no new material. Unchanged
    content, renumbered s25 -> s39 in Round 2. Round-2 P1 Russification fix
    (presentation-critic): this is a take-home handout the student reads
    without surrounding context, so all three failure-type labels now get
    a FULL Russian gloss — "Dist. shift" was a new abbreviation appearing
    nowhere else in the deck (terminology drift), now normalized to
    "Distribution shift (сдвиг распределения)" matching s28/s37 exactly."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    section_tag(s, 0.55, 0.4, "Раздел 7 · Памятка на вынос")
    slide_title(s, "Как выбрать тип AI за 60 секунд", y=0.85, size=27)

    col_gap = 0.28
    col_w = (12.23 - col_gap) / 2
    col_y = 1.9
    col_h = 5.05

    # LEFT column: 2 questions + mini quadrant
    lx = 0.55
    ocean_box(s, lx, col_y, col_w, col_h)
    pad = 0.24
    text_box(s, lx + pad, col_y + pad, col_w - 2 * pad, 0.8,
             text="Q1: взаимодействие с пользователем?\nQ2: самостоятельная работа с инструментами?".replace("\n", "   "),
             size=11.5, bold=True, color=MID, line_spacing=1.3)
    quad_y = col_y + pad + 0.85
    quad_h = col_h - pad - 0.85 - pad
    cells = [("Модель", 0, 0, MID), ("Чат", 0, 1, LIGHT), ("Приложение", 1, 0, TEAL), ("Агент", 1, 1, DEEP)]
    cw2 = (col_w - 2 * pad - 0.08) / 2
    ch2 = (quad_h - 0.08) / 2
    for label, r, c, col in cells:
        cx = lx + pad + c * (cw2 + 0.08)
        cy = quad_y + r * (ch2 + 0.08)
        filled_rect(s, cx, cy, cw2, ch2, col, radius=True, radius_adj=0.14)
        text_box(s, cx, cy, cw2, ch2, text=label, size=13.5, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # RIGHT column: 3 signs AI not needed + 3 failure types (stacked)
    rx = lx + col_w + col_gap
    ocean_box(s, rx, col_y, col_w, col_h)
    text_box(s, rx + pad, col_y + pad - 0.02, col_w - 2 * pad, 0.35,
             text="AI, возможно, не нужен, если:", size=13, bold=True, color=MID)
    signs = [
        "простое правило (regex, справочник, порог) справится не хуже",
        "цена ошибки высока, а проверка не быстрее, чем сделать самому",
        "задача разовая и небольшая",
    ]
    sy = col_y + pad + 0.42
    for sgn in signs:
        text_box(s, rx + pad, sy, 0.2, 0.5, text="—", size=12, bold=True, color=LIGHT)
        text_box(s, rx + pad + 0.24, sy, col_w - 2 * pad - 0.24, 0.5,
                 text=sgn, size=10.5, color=DEEP, line_spacing=1.2)
        sy += 0.52

    text_box(s, rx + pad, sy + 0.08, col_w - 2 * pad, 0.35,
             text="Три типа провала для проверки:", size=13, bold=True, color=MID)
    fy = sy + 0.5
    fails = [
        ("Bias (смещение)", "воспроизводит перекос данных"),
        ("Sycophancy (подстройка)", "подстраивается под ожидание"),
        ("Distribution shift (сдвиг распределения)", "тихо деградирует на новых данных"),
    ]
    for label, desc in fails:
        text_box(s, rx + pad, fy, col_w - 2 * pad, 0.32, text=label, size=10.5, bold=True, color=TEAL)
        text_box(s, rx + pad, fy + 0.3, col_w - 2 * pad, 0.32,
                 text=desc, size=10, italic=True, color=SLATE, line_spacing=1.15)
        fy += 0.62

    text_box(s, 0.55, col_y + col_h + 0.15, 12.23, 0.4,
             text="Всё, что здесь написано, вы уже видели сегодня — рабочая версия на вынос",
             size=12.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s39"))


def build_s40(p):
    """hero_closing — real GPU photo (Wikimedia Commons CC BY 2.0), bridging
    to Lecture 2's "inside the model" theme (tokens/embeddings/attention run
    on exactly this kind of hardware). Unchanged content, renumbered
    s26 -> s40 in Round 2."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    hero_w = 6.283
    img_path = SHOTS / "s-closing-gpu-real.jpg"
    filled_rect(s, 0, 0, hero_w, 7.5, DEEP)
    pad = 0.4
    avail_w = hero_w - 2 * pad
    avail_h = 7.5 - 2 * pad - 0.5
    pic = add_image(s, img_path, pad, pad + 0.25, w=avail_w, h=avail_h)
    if pic is not None:
        gframe = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, pic.left, pic.top, pic.width, pic.height)
        gframe.fill.background()
        gframe.line.color.rgb = GOLD
        gframe.line.width = Pt(2.5)
        disable_shadow(gframe)
    text_box(s, pad, pad - 0.05, avail_w, 0.3, text="ВНУТРИ МОДЕЛИ", size=11, bold=True,
             color=GOLD, align=PP_ALIGN.LEFT)
    text_box(s, pad, 7.5 - pad - 0.1, avail_w, 0.3,
             text="Mickael Courtiade · Wikimedia Commons · CC BY 2.0",
             size=8.5, italic=True, color=RGBColor(0xC8, 0xD2, 0xDF))

    rx = hero_w + 0.55
    rw = 13.333 - rx - 0.55
    text_box(s, rx, 1.35, rw, 0.5, text="СПАСИБО", size=14, bold=True, color=TEAL)
    text_box(s, rx, 1.85, rw, 2.1,
             text="От классификации снаружи — к тому, что внутри",
             size=27, bold=True, color=DEEP, line_spacing=1.15)
    text_box(s, rx, 3.9, rw, 1.6,
             text="Сегодня вы натренировали чек-лист, поймали галлюцинацию и "
                  "различили три типа провала. На Лекции 2 — токены, эмбеддинги, "
                  "внимание и температура: как это всё работает на кремнии вроде "
                  "этого.",
             size=14.5, color=MID, line_spacing=1.4)
    chip(s, rx, 5.85, 3.3, 0.55, "Лекция 2  →  далее", fill=DEEP, size=14)
    speaker_notes(s, load_notes("s40"))


# ============================================================
# Main
# ============================================================
BUILDERS = [
    build_s01, build_s02, build_s03, build_s04, build_s05,
    build_s06, build_s07, build_s08, build_s09, build_s10,
    build_s11, build_s12, build_s13, build_s14, build_s15,
    build_s16, build_s17, build_s18, build_s19, build_s20,
    build_s21, build_s22, build_s23, build_s24, build_s25,
    build_s26, build_s27, build_s28, build_s29, build_s30,
    build_s31, build_s32, build_s33, build_s34, build_s35,
    build_s36, build_s37, build_s38, build_s39, build_s40,
]


def main():
    p = setup_pres()
    for fn in BUILDERS:
        fn(p)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    p.save(str(OUT))
    print(f"Saved {OUT} ({len(BUILDERS)} slides)")


if __name__ == "__main__":
    main()
