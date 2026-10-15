# -*- coding: utf-8 -*-
"""ОБРАЗЦОВАЯ РАСКЛАДКА: самая маленькая дека, задействующая всё ядро.

Зачем она есть, если раскладка — дело деки. По двум причинам, и ни одна не
про удобство:

1. САМОПРОВЕРКЕ нужна раскладка. Проба вида «кадр, у которого текст не
   влезает» ставится ФАЙЛОМ кадра и доказывает мерой то, что увидит
   настоящая дека, — а для этого файл надо через что-то собрать. Прогонять
   пробы через раскладку живой лекции нельзя: тогда самопроверка ядра
   зависела бы от деки, которую ядро обслуживает.
2. НОВОЙ ДЕКЕ нужен образец. Без него первая страница работы над декой —
   чтение чужой папки, ровно то, с чего этот пакет и начался
   (`tools/seminar-production/README.md` §8 про то же в семинарах).

Чем она НЕ является: это не «общая раскладка курса». Раскладка каждой деки
своя — см. `README.md`, раздел «Что остаётся за декой». Здесь ровно столько,
чтобы каждая единица ядра была вызвана хотя бы раз, и ни строкой больше.

Геометрия — `Geometry`: поля, верх тела, подвал, колонка кадра. У двух
настоящих дек эти числа РАЗНЫЕ (тело от 1,46 против 1,34, подвал на 6,94
против 7,00), и это не расхождение, которое надо сводить: это разная
раскладка под разный материал.
"""
from dataclasses import dataclass

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import (columns, figure, flow, markup, media, metrics, plates,
               prims, report, scheme, slidefile, tables, wrap)
from .theme import DEEP, GOLD, LIGHT, MID, SLIDE_H, SLIDE_W, WHITE


@dataclass(frozen=True)
class Geometry:
    mx: float = 0.55                 # поле слева и справа
    title_y: float = 0.40
    title_h: float = 0.92
    body_top: float = 1.46
    foot_y: float = 6.94
    foot_h: float = 0.50
    media_w: float = 4.30
    col_gap: float = 0.34
    gap: float = 0.20
    hero_top: float = 0.10
    hero_w: float = 7.58
    tick_w: float = 1.05
    tick_h: float = 0.055
    wrap_gap: float = 0.10           # просвет между низом снимка и телом,
                                     # вернувшим себе полную ширину
    body_pt: float = 15.0            # номинальный кегль тела: по нему
                                     # мерится пол проекции

    @property
    def full_w(self):
        return SLIDE_W - 2 * self.mx

    @property
    def body_bot(self):
        return self.foot_y - 0.12


G = Geometry()
CONTENT_TYPES = {"case", "norm", "comparison", "summary", "map", "question"}


def heading(s, sl, g=G, *, size=27.0, width=None, color=DEEP):
    """Заголовок-утверждение. Кегль подбирается под длину строки ИЗ ФАЙЛА:
    заголовки правятся в `slides/`, и подгонять их руками нельзя."""
    if not sl.title:
        report.warn(f"[заголовок] {sl.sid}: поле `title` пусто")
        return g.body_top
    w = g.full_w if width is None else width
    sz = metrics.fit_size(sl.title, w, g.title_h, hi=size, lo=19.0,
                          floor=15.0, bold=True, ls=1.08,
                          tag=f"{sl.sid}/заголовок")
    prims.text_box(s, g.mx, g.title_y, w, g.title_h, sl.title, size=sz,
                   bold=True, color=color, ls=1.08,
                   tag=f"{sl.sid}/заголовок")
    # Акцент садится под НАСТОЯЩУЮ высоту заголовка, а не под рамку: у
    # однострочного заголовка рамка на полдюйма выше текста, и акцент по
    # рамке попадал под коробку мотива.
    sl.tick_y = min(g.title_y + metrics.est_h(sl.title, sz, w, 1.08, True)
                    + 0.07, g.body_top - 0.17)
    return g.body_top


def gold_tick(s, sid, x, y, g=G):
    prims.rect(s, x, y, g.tick_w, g.tick_h, GOLD, count="акцент")
    report.GOLD_SEEN.add(sid)


def footer(s, sl, g=G):
    """Подвал: источник живыми ссылками. Подпись hero или предъявленного
    документа идёт сюда же последним сегментом — место источника в деке
    одно. `media_document` (О18, #229) включает подпись и там, где кадр не
    hero: документ зал обязан мочь проверить независимо от размера."""
    src = str(sl.meta.get("source") or "").strip()
    cap = str(sl.meta.get("media_caption") or "").strip()
    if cap and (sl.meta.get("media_hero") or sl.meta.get("media_document")):
        src = f"{src} · {cap}" if src and src != "—" else cap
    if not src or src == "—":
        return
    runs = [{"text": vis, "size": 11.0, "italic": True,
             "color": MID if url else LIGHT, "url": url}
            for vis, url in markup.source_parts(src)]
    if not runs:
        return
    # Высота подвала мерится ОДИН раз и на один порог — порог самой рамки.
    # Два порога на одну меру давали два предупреждения разной строгости об
    # одном дефекте, и счёт в отчёте перестал значить то, что обещает.
    flat = "".join(r["text"] for r in runs)
    e = metrics.est_h(flat, 11.0, g.full_w, 1.12, italic=True)
    if e > g.foot_h + 0.02:
        report.warn(
            f"[высота] {sl.sid}/подвал: источник не влезает в подвал — "
            f"{len(flat)} знаков, оценка {e:.2f}\" против {g.foot_h:.2f}\"")
    prims.text_runs(s, g.mx, g.foot_y, g.full_w, g.foot_h, runs, ls=1.12,
                    tag=f"{sl.sid}/подвал", quiet=True)


def check_prims(sl, kind):
    """Примитив объявлен на кадре, который его не рисует. Молчать нельзя:
    сессия раздела написала бы полосу плашек и не узнала, что её нет."""
    for f, name in (("blocks", "плашки"), ("scheme", "схема"),
                    ("columns", "столбцы"), ("matrix_empty", "матрица"),
                    ("figure", "число")):
        if sl.meta.get(f):
            report.warn(
                f"[{name}] {sl.sid}: поле `{f}` объявлено на кадре типа "
                f"«{kind}» — оно рисуется только на содержательных кадрах")


def cover(p, sl, root, g=G):
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    check_prims(sl, "cover")
    img = media.media_path(sl.meta, root, sl.sid)
    hero = img is not None and bool(sl.meta.get("media_hero"))
    ty, gy, tw = 1.70, 1.28, g.full_w
    if hero:
        x_box, _ = media.place_hero(s, sl.sid, sl.meta, img, SLIDE_W - g.mx,
                                    g.hero_top, g.body_bot, g.hero_w)
        tw, ty, gy = x_box - g.col_gap - g.mx, 1.10, 0.68
    runs = []
    for i, (kind, t) in enumerate(slidefile.body_blocks(sl)):
        sz = {"head": 34.0, "cap": 12.5}.get(kind, 17.0)
        for j, r in enumerate(markup.inline_runs(
                t, sz, DEEP if kind != "cap" else LIGHT)):
            r.setdefault("italic", kind == "cap")
            # Абзац начинает ПЕРВЫЙ прогон строки, а не пустой разделитель
            # после предыдущей: разделитель нёс кегль ПРЕДЫДУЩЕЙ строки, а
            # мера берёт по абзацу максимум — и абзац тела за заголовком в
            # 34 пт мерился как набранный 34-м.
            r["newpara"] = bool(i and j == 0)
            if r["newpara"]:
                r["space_before"] = 12
            runs.append(r)
    if runs:
        prims.text_runs(s, g.mx, ty, tw, (g.body_bot - ty) if hero else 4.20,
                        runs, ls=1.22, tag=f"{sl.sid}/обложка")
    prims.rect(s, g.mx, gy, 1.60, 0.07, GOLD, count="акцент")
    report.GOLD_SEEN.add(sl.sid)
    footer(s, sl, g)
    return s


def divider(p, sl, root, g=G):
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    prims.rect(s, 0, 0, 0.17, SLIDE_H, MID, count="полоса")
    check_prims(sl, "divider")
    y = 1.05
    for kind, t in slidefile.body_blocks(sl):
        if kind == "head":
            sz = metrics.fit_size(t, g.full_w, 1.05, hi=30.0, lo=20.0,
                                  floor=16.0, bold=True, ls=1.10,
                                  tag=f"{sl.sid}/дивайдер-имя")
            h = metrics.est_h(t, sz, g.full_w, 1.10, True)
            prims.text_box(s, g.mx + 0.22, y, g.full_w, h, t, size=sz,
                           bold=True, color=DEEP, ls=1.10,
                           tag=f"{sl.sid}/дивайдер-имя")
            y += h + 0.10
            gold_tick(s, sl.sid, g.mx + 0.22, y, g)
            y += 0.30
        else:
            h = metrics.est_h(t, 15.5, g.full_w - 0.22, 1.24)
            prims.text_runs(s, g.mx + 0.22, y, g.full_w - 0.22, h + 0.04,
                            markup.inline_runs(t, 15.5, DEEP), ls=1.24,
                            tag=f"{sl.sid}/дивайдер-тело")
            y += h + 0.18
        if y > g.foot_y - 0.2:
            report.warn(f"[высота] {sl.sid}/дивайдер: текст дошёл до подвала "
                        f"— {y:.2f}\" при пределе {g.foot_y:.2f}\"")
            break
    footer(s, sl, g)
    return s


def content(p, sl, root, g=G):
    """Содержательный кадр: заголовок · плашки · схема · число · столбцы ·
    тело · подвал. Тело идёт ПОТОКОМ, когда в нём есть таблица, и ПРОГОНОМ, когда
    нет: таблицу прогон не умеет, а иерархию кеглей внутри тела не умеет
    поток."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    img = media.media_path(sl.meta, root, sl.sid)
    hero = img is not None and bool(sl.meta.get("media_hero"))
    col_bot, body_w = g.body_bot, g.full_w
    media_bot, draw_img = 0.0, None       # низ боковой иллюстрации и её
                                          # отложенный вызов: в режиме
                                          # обтекания коробка тела идёт во
                                          # всю ширину, то есть и под
                                          # снимком, и накрыла бы его
    if hero:
        x_box, col_bot = media.place_hero(
            s, sl.sid, sl.meta, img, SLIDE_W - g.mx, g.hero_top, g.body_bot,
            g.hero_w)
        body_w = x_box - g.col_gap - g.mx
        y = heading(s, sl, g, width=body_w)
    else:
        y = heading(s, sl, g)
        if img:
            mw, mh = media.media_box_size(
                media.img_ar(img, sl.sid), sl.media_w or g.media_w,
                min(3.40, g.body_bot - y))
            body_w = g.full_w - mw - g.col_gap
            draw_img = (g.mx + body_w + g.col_gap, y, mw, mh)
            media_bot = y + mh

    is_content = str(sl.meta.get("type") or "case") in CONTENT_TYPES
    pl = plates.plates_of(sl) if is_content else []
    if pl:
        y += plates.draw_plates(s, sl.sid, pl, g.mx, y, body_w) + g.gap
    sch = scheme.scheme_of(sl) if is_content else None
    if sch:
        scheme.check_scheme(sl.sid, sch, body_w)
        y += scheme.draw_scheme(s, sl.sid, sch, g.mx, y, body_w) + g.gap
    fig = figure.figure_of(sl) if is_content else None
    if fig:
        figure.check_figure(sl.sid, fig, body_w)
        y += figure.draw_figure(s, sl.sid, fig, g.mx, y, body_w) + g.gap
    cols = columns.columns_of(sl) if is_content else None
    if cols:
        ch = max(columns.MIN_H, min(col_bot - y, columns.MAX_H))
        columns.draw_columns(s, sl.sid, cols, g.mx, y, body_w, ch)
        y += ch + g.gap

    heading_ord, blocks = slidefile.body_ordered(sl)
    tables.apply_matrix_empty(sl.sid, sl.meta, blocks)
    avail = col_bot - y
    has_table = any(k == "table" for k, _ in blocks)
    if blocks and avail > 0.35 and has_table:
        size = flow.fit_blocks(blocks, body_w, avail, tag=f"{sl.sid}/тело")
        flow.flow(s, blocks, g.mx, y, body_w, size, f"{sl.sid}/тело")
    elif avail > 0.35:
        runs, first = [], True
        for kind, t in slidefile.body_blocks(sl):
            sz = {"head": 20.0, "cap": 12.0, "bullet": 15.0}.get(kind, 15.0)
            if not first:
                runs.append({"text": "", "size": sz, "newpara": True,
                             "space_before": 7})
            first = False
            for r in markup.inline_runs(t, sz, LIGHT if kind == "cap"
                                        else DEEP):
                if kind == "cap":
                    r["italic"] = True
                if kind == "head":
                    r["bold"] = True
                runs.append(r)
        if runs:
            # Тело, начавшееся РЯДОМ со снимком, обтекает его: узкая надпись
            # рядом, широкая под ним. Ветка здесь, а не в ядре, потому что
            # обтекание — раскладка, и образец обязан показать её целиком.
            wrapped, y_bot = None, media_bot + g.wrap_gap
            if not hero and img and y < media_bot:
                wrapped = wrap.fit_runs_wrap(
                    runs, body_w - 0.08, media_bot - y, g.full_w - 0.08,
                    col_bot - y_bot, body_w - 0.08, avail, ls=1.26,
                    tag=f"{sl.sid}/тело", proj_base=g.body_pt)
            pushed = None
            if not wrapped and not hero and img and y < media_bot:
                # Рядом со снимком не поместился ни один блок — тело уходит
                # под него целиком. Та же проверка «кегль не падает».
                pushed = wrap.fit_pushed(
                    runs, g.full_w - 0.08, col_bot - y_bot,
                    body_w - 0.08, avail, ls=1.26, tag=f"{sl.sid}/тело",
                    proj_base=g.body_pt)
            if wrapped or pushed:
                # Коробка мотива начинается там, где начинается ТЕКСТ: при
                # обтекании от верха тела, при уходе под снимок — от первой
                # строки под ним.
                top = wrapped[2] if wrapped else []
                bot = wrapped[3] if wrapped else runs
                box_y = y if wrapped else y_bot
                prims.ocean_box(s, g.mx - 0.14, box_y - 0.10,
                                g.full_w + 0.28, g.body_bot - box_y + 0.10)
                if top:
                    prims.text_runs(s, g.mx + 0.04, y, body_w - 0.08,
                                    media_bot - y, top, ls=1.26,
                                    tag=f"{sl.sid}/тело-рядом")
                prims.text_runs(s, g.mx + 0.04, y_bot, g.full_w - 0.08,
                                col_bot - y_bot, bot, ls=1.26,
                                tag=f"{sl.sid}/тело-под")
            else:
                metrics.fit_runs(runs, body_w - 0.08, avail, ls=1.26,
                                 tag=f"{sl.sid}/тело", proj_base=g.body_pt)
                prims.ocean_box(s, g.mx - 0.14, y - 0.10, body_w + 0.28,
                                min(avail + 0.18, g.body_bot - y + 0.10))
                prims.text_runs(s, g.mx + 0.04, y, body_w - 0.08, avail,
                                runs, ls=1.26, tag=f"{sl.sid}/тело")
    elif blocks:
        report.warn(f"[высота] {sl.sid}/тело: места под тело не осталось "
                    f"({avail:.2f}\") — примитивы съели кадр")
    if draw_img:
        media.draw_media(s, sl.sid, img, *draw_img)
    gold_tick(s, sl.sid, g.mx, sl.tick_y or (g.title_y + 0.98), g)
    footer(s, sl, g)
    return s


BUILDERS = {"cover": cover, "divider": divider}


def build(slides_dir, out, *, root=None, only=None, g=G):
    """Собрать деку из каталога кадров. Возвращает число собранных кадров."""
    root = root or slides_dir
    p = prims.new_deck()
    n = 0
    for f in slidefile.slide_files(slides_dir, only):
        sl = slidefile.read_slide(f)
        if sl is None:
            continue
        kind = str(sl.meta.get("type") or "case").strip()
        s = BUILDERS.get(kind, content)(p, sl, root, g)
        markup.notes_with_links(s, sl.notes)
        if sl.sid not in report.GOLD_SEEN:
            report.warn(f"[золото] {sl.sid}: золотого акцента на кадре нет")
        n += 1
    metrics.font_gaps()
    p.save(str(out))
    return n
