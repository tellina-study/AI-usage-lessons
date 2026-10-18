# -*- coding: utf-8 -*-
"""Низкоуровневые примитивы: фигуры, надписи, картинки.

Объединение примитивов двух сборщиков. Где они совпадали посимвольно
(`ocean_box`, скругление, заливка, обводка) — взята общая версия; где
расходились — расхождение разобрано ниже по месту, в комментарии к функции.

Ничего в этом модуле не решает, ГДЕ стоит фигура: раскладка — дело деки.
Здесь только «нарисовать то, что сказали, и не нарисовать больше».
"""
from pathlib import Path

from lxml import etree
from PIL import Image
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

from . import metrics, report
from .theme import (DEEP, LIGHT, MOTIF_RADIUS_PT, OUTLINE, SLATE, SURFACE,
                    TEAL, WHITE, FONT, MID, SLIDE_H, SLIDE_W)

_A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
_P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"

# Снимать ли `<p:style>` с автофигуры. РАЗНОГЛАСИЕ ДВУХ СБОРЩИКОВ, и
# разобрано оно в пользу lec-06 — см. `no_shadow`. Флаг существует ровно для
# одного: регрессия на доставленной деке Лекции 7 должна воспроизвести её
# как есть, вместе с этим её дефектом. Новая дека ставит True и не трогает.
STRIP_THEME_STYLE = True


def no_shadow(shp):
    """Снять тень с автофигуры.

    РАЗНОГЛАСИЕ. `build_lec07.py` убирает `effectLst`/`effectRef` из `spPr` и
    ставит `shadow.inherit = False`. `build_lec06_p1.py` (правленный в
    `build_v4._no_shadow`) вдобавок УДАЛЯЕТ сам элемент `<p:style>`.

    Прав lec-06, и это измерено, а не выведено. `shapes.add_shape` кладёт
    рядом со `spPr` элемент `<p:style>` со ссылкой на эффект темы
    (`<a:effectRef idx="2">`); LibreOffice читает ссылку темы и рисует тень
    по ней, игнорируя пустой список эффектов в самой фигуре
    (`notes/mcp-limitations.md` [#223-8], статус `active`). Поиск
    `effectRef` внутри `spPr`, который делает lec-07, не находит ничего:
    `effectRef` лежит не в `spPr`, а внутри `<p:style>`, то есть это
    холостая строка.

    Замерено на доставленных файлах: в деке Лекции 7 на первых двадцати
    кадрах 112 автофигур несут `<p:style>` с `effectRef idx="2"` — то есть
    мягкую тень темы на каждом мотиве, плашке и стрелке; в деке Лекции 6 —
    ни одной. Сессия Лекции 7 этой записи каталога не видела: она лежит на
    неслитой ветке `issue-223-lec-06-rework`.

    Следствие для этапа 2: перевод Лекции 7 на это ядро СНИМЕТ с её кадров
    тень. Это видимая правка к лучшему, но всё же видимая правка, и её надо
    принимать глазами, а не протащить вместе с переводом."""
    el = shp._element
    if STRIP_THEME_STYLE:
        for e in el.spPr.findall(_A + "effectLst"):
            el.spPr.remove(e)
        etree.SubElement(el.spPr, _A + "effectLst")
        for st in el.findall(_P + "style"):
            el.remove(st)
    else:
        # Путь lec-07, ровно как он был: `effectRef` ищется в `spPr`, где его
        # нет (он внутри `<p:style>`), то есть эта половина холостая; пустой
        # `effectLst` ставит потом `shadow.inherit = False`.
        for tag in ("effectLst", "effectRef"):
            for e in el.spPr.findall(_A + tag):
                el.spPr.remove(e)
        try:
            shp.shadow.inherit = False
        except Exception:
            pass


# ── фигуры ──────────────────────────────────────────────────────────


def rect(s, x, y, w, h, fill, *, stroke=None, stroke_pt=1.0,
         radius=False, radius_adj=0.14, count="плашка"):
    st = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shp = s.shapes.add_shape(st, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
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
    no_shadow(shp)
    if count:
        report.PRIM[count] += 1
    return shp


def ocean_box(s, x, y, w, h, *, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5,
              radius_pt=MOTIF_RADIUS_PT, count="мотив"):
    """Мотив деки: океанская скруглённая коробка. Радиус 12 пт.

    Формула скругления у двух сборщиков совпадала посимвольно: радиус задан
    в ПУНКТАХ и переводится в долю от половины короткой стороны, с зажимом
    0,03…0,25. Доля без перевода давала бы у коробки 1" и коробки 6" разную
    на глаз скруглённость при одном числе."""
    shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                             Inches(x), Inches(y), Inches(w), Inches(h))
    try:
        shp.adjustments[0] = max(0.03, min(0.25,
                                 (radius_pt / 72.0) / max(min(w, h) / 2.0, 0.4)))
    except Exception:
        pass
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.color.rgb = stroke
    shp.line.width = Pt(stroke_pt)
    no_shadow(shp)
    if count:
        report.PRIM[count] += 1
    return shp


def _plain_arrow(s, shape, x, y, w, h, color):
    shp = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    no_shadow(shp)
    report.PRIM["стрелка"] += 1
    return shp


def arrow(s, x, y, w, h, color=LIGHT):
    return _plain_arrow(s, MSO_SHAPE.RIGHT_ARROW, x, y, w, h, color)


def arrow_lr(s, x, y, w, h, color=TEAL):
    return _plain_arrow(s, MSO_SHAPE.LEFT_RIGHT_ARROW, x, y, w, h, color)


def arrow_d(s, x, y, w, h, color=MID):
    return _plain_arrow(s, MSO_SHAPE.DOWN_ARROW, x, y, w, h, color)


def chip(s, x, y, w, h, text, *, fill=MID, stroke=None, color=WHITE,
         size=13, bold=True, tag=""):
    """Чип: скруглённая плашка с текстом внутри самой фигуры.

    Из lec-06. В lec-07 чипов нет вовсе, и это не упущение: деке Лекции 7
    они не понадобились. Примитив остаётся в ядре, потому что встречается в
    корпусе 25 раз из 73 сборщиков."""
    shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                             Inches(x), Inches(y), Inches(w), Inches(h))
    try:
        shp.adjustments[0] = 0.42
    except Exception:
        pass
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(1.3)
    tf = shp.text_frame
    tf.margin_left = tf.margin_right = Inches(0.07)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.word_wrap = True
    for i, line in enumerate(text.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.CENTER
        p.line_spacing = 1.05
        r = p.add_run()
        r.text = line
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.color.rgb = color
    no_shadow(shp)
    e = metrics.est_h(text, size, w - 0.14, 1.05, bold)
    if e > h + 0.02:
        report.warn(f"[чип] {tag or '?'}: «{text[:36]}…» оценка "
                    f"{e:.2f}\" > {h:.2f}\"")
    report.PRIM["чип"] += 1
    return shp


# ── надписи ─────────────────────────────────────────────────────────


def _frame(s, x, y, w, h, anchor):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = Inches(0.0)
    tf.margin_top = tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    return tb, tf


def text_box(s, x, y, w, h, text, *, size=16, bold=False, italic=False,
             color=DEEP, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             ls=1.18, tag="", quiet=False):
    """Однородная надпись: одно начертание, один кегль, `\\n` — абзац.

    РАЗНОГЛАСИЕ. lec-06 меряет высоту без курсива (`_est_height(text, size,
    w, ls, bold)`), lec-07 — с курсивом. Взят lec-07: курсив Liberation Sans
    у части слов шире прямого до 1,32, и мера по прямому там недомеривает на
    строку. XML надписи от этого не меняется — расходятся только
    предупреждения, то есть доставленная дека Лекции 6 не двинулась, а
    молчавшие её предупреждения заговорили."""
    e = metrics.est_h(text, size, w, ls, bold, italic)
    if e > h + 0.02 and not quiet:
        report.warn(
            f"[высота] {tag or '?'}: рамка {w:.2f}×{h:.2f}\" кегль "
            f"{size:.1f} — оценка {e:.2f}\" > {h:.2f}\"  «{text[:40]}…»")
    metrics.check_width(text, size, w, tag, bold, italic)
    tb, tf = _frame(s, x, y, w, h, anchor)
    for i, line in enumerate(text.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = ls
        r = p.add_run()
        r.text = line
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
    return tb


def text_runs(s, x, y, w, h, runs, *, ls=1.18, align=PP_ALIGN.LEFT,
              anchor=MSO_ANCHOR.TOP, tag="", quiet=False,
              link_bucket="подвал"):
    """Смешанный набор: список словарей `text · size · bold · italic ·
    color · url · underline · newpara · space_before · align · ls`.

    Высота считается `metrics.runs_h` по тем же словарям — то есть вместе с
    отбивкой абзацев. Это не косметика: мера без отбивки пропускала кадр,
    у которого последний абзац печатался ПОВЕРХ строки источника.

    `quiet=True` снимает ЗДЕСЬ проверку высоты — и только её: ставится
    вызывающим, который ту же высоту уже измерил и уже сказал о ней своим
    предупреждением. Один дефект обязан давать одно предупреждение.
    Проверка ширины под `quiet` НЕ уходит: это другой дефект."""
    paras = metrics.runs_paras(runs)
    e = metrics.runs_h(runs, w, ls)
    if e > h + 0.02 and not quiet:
        head = "".join(t for t, *_ in paras[0][0])
        report.warn(
            f"[высота] {tag or '?'}: прогон {w:.2f}×{h:.2f}\" — оценка "
            f"{e:.2f}\" > {h:.2f}\"  «{head[:40]}…»")
    for pieces, _sb in paras:
        metrics.check_width_segs(pieces, w, tag)
    tb, tf = _frame(s, x, y, w, h, anchor)
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = ls
    n = 0
    for cfg in runs:
        if cfg.get("newpara"):
            p = tf.add_paragraph()
            p.alignment = cfg.get("align", align)
            p.line_spacing = cfg.get("ls", cfg.get("line_spacing", ls))
            if cfg.get("space_before"):
                p.space_before = Pt(cfg["space_before"])
        r = p.add_run()
        r.text = cfg["text"]
        r.font.name = FONT
        r.font.size = Pt(cfg.get("size", 16))
        r.font.bold = cfg.get("bold", False)
        r.font.italic = cfg.get("italic", False)
        r.font.color.rgb = cfg.get("color", DEEP)
        if cfg.get("underline"):
            r.font.underline = True
        if cfg.get("url"):
            r.hyperlink.address = cfg["url"]
            r.font.underline = True
            n += 1
    if n and link_bucket:
        report.LINKS[link_bucket] += n
    return tb


def apply_links(tb, runs, tag=""):
    """Поставить гиперссылки на прогоны УЖЕ созданной надписи.

    Нужна там, где надпись создана не `text_runs` этого модуля. Совпадение
    череды прогонов со чередой словарей ПРОВЕРЯЕТСЯ: не совпало —
    предупреждение, а не молча расставленные не туда ссылки."""
    rr = [r for p in tb.text_frame.paragraphs for r in p.runs]
    if len(rr) != len(runs):
        report.warn(f"[ссылка] {tag}: прогонов {len(rr)} при {len(runs)} "
                    "словарях — ссылки не поставлены")
        return 0
    n = 0
    for r, cfg in zip(rr, runs):
        if cfg.get("underline"):
            r.font.underline = True
        if cfg.get("url"):
            r.hyperlink.address = cfg["url"]
            n += 1
    return n


# ── картинки ────────────────────────────────────────────────────────


def img_size(path):
    with Image.open(path) as im:
        return im.size


def fit(path, box_w, box_h):
    """Вписать изображение в рамку без искажения → (dx, dy, w, h)."""
    iw, ih = img_size(path)
    ar = iw / max(1, ih)
    if ar > box_w / box_h:
        w, h = box_w, box_w / ar
    else:
        h, w = box_h, box_h * ar
    return ((box_w - w) / 2, (box_h - h) / 2, w, h)


def add_image(s, path, x, y, box_w, box_h, *, tag=""):
    """Вписанная картинка по центру рамки. Возвращает (x, y, w, h).

    Файла нет — на экране остаётся рамка с честной надписью, а запись уходит
    в `report.MISSING_MEDIA`. Молча пустое место хуже: кадр, которого нет,
    неотличим от кадра, который забыли поставить."""
    path = Path(path)
    if not path.exists():
        report.MISSING_MEDIA.append(f"{tag or '?'}: нет файла {path}")
        ocean_box(s, x, y, box_w, box_h, fill=WHITE, stroke=OUTLINE)
        text_box(s, x + 0.2, y + box_h / 2 - 0.3, box_w - 0.4, 0.6,
                 "место под изображение —\nфайла нет на диске", size=13,
                 italic=True, color=SLATE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, tag=tag)
        return (x, y, box_w, box_h)
    dx, dy, w, h = fit(path, box_w, box_h)
    s.shapes.add_picture(str(path), Inches(x + dx), Inches(y + dy),
                         width=Inches(w), height=Inches(h))
    report.PRIM["кадр"] += 1
    return (x + dx, y + dy, w, h)


def add_image_cover(s, path, x, y, w, h, *, tag=""):
    """Картинка заполняет рамку целиком, с обрезкой по длинной стороне."""
    path = Path(path)
    if not path.exists():
        report.MISSING_MEDIA.append(f"{tag or '?'}: нет файла {path}")
        rect(s, x, y, w, h, OUTLINE)
        return None
    iw, ih = img_size(path)
    src, dst = iw / ih, w / h
    pic = s.shapes.add_picture(str(path), Inches(x), Inches(y),
                               width=Inches(w), height=Inches(h))
    if src > dst:                       # источник шире — срезать по бокам
        cut = (1 - dst / src) / 2
        pic.crop_left = pic.crop_right = cut
    elif src < dst:                     # источник выше — срезать верх и низ
        cut = (1 - src / dst) / 2
        pic.crop_top = pic.crop_bottom = cut
    report.PRIM["кадр"] += 1
    return pic


def new_deck(presentation_cls=None):
    from pptx import Presentation
    p = (presentation_cls or Presentation)()
    p.slide_width = Inches(SLIDE_W)
    p.slide_height = Inches(SLIDE_H)
    return p


def blank(p):
    return p.slides.add_slide(p.slide_layouts[6])


def set_slide_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def speaker_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text or ""
