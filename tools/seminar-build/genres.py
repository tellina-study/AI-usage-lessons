"""Именованная библиотека жанровых приёмов деки семинара.

Это та самая библиотека, о которой канон (`tools/presentation-build/
seminar-deck-kit.md`) говорит: дека собирается ИЗ ИМЕНОВАННЫХ ПРИЁМОВ, приём
выбирается по полю `visual.pattern`, а не по типу слайда и не по набору
блоков. Семинар 5 собирался пятью универсальными раскладками — владелец
отклонил деку («сплошные таблицы странные, текст наложенный сам на себя»),
и правило завелось именно тогда.

Занятие НЕ добавляет сюда функцию под каждое своё имя приёма: имён у деки
двадцать, жанров — десять, и большинство имён честно падает в `content`
(заголовок-утверждение, схема, блоки в порядке источника) — потому что
различие между ними уже несёт роль блока (`roles.quote_role`), а не
отдельная раскладка. Своё у занятия — ТАБЛИЦА СООТВЕТСТВИЯ
`visual.pattern → жанр` в `deck-config.yaml` (`genres:`), и там же решение
по каждому новому имени.

Две обложки — `cover` и `cover_centered` — это не параметр одной функции, а
два разных приёма: у Семинара 6 заголовок прижат влево и подзаголовок
отмечен тиловой планкой, у Семинара 7 оба отцентрованы по полотну.
Свести их в одну функцию с четырьмя числами из конфига значило бы
вернуть ровно то, против чего заведено правило: раскладку, настраиваемую
снаружи, вместо приёма с именем.
"""

from pptx.enum.text import PP_ALIGN
from pptx.util import Inches
from pptx.enum.text import MSO_ANCHOR

import deck_config as D
import deck_kit as K
import metrics as M
from roles import (ITALIC_LINE, block_drawer, compose, measure, split_question,
                   unseen)


def g_divider(sl, sid, title, blocks, pattern, assertion="", meta=None):
    """Дивайдер уровня РАЗДЕЛА — градиент, золотая полоса, номерной значок,
    смысловая строка, дорожная карта ступеней. Дивайдер называет ПРОБЛЕМУ,
    не решение (правило А2 канона семинаров §3)."""
    _, stage = D.where(sid)
    stages = D.sections_for(sid)[1]
    tag, badge = D.tag_for(sid, meta), D.badge_for(sid)
    K.divider_bg(sl)
    K.strip_pills(sl, D.LEFT, 0.5, 11.3, len(stages), stage if stage is not None else -1)

    meaning = []
    for kind, b in blocks:
        for ln in (b if kind == "quote" else ([b] if kind == "para" else [])):
            rest = K.plain(ln)
            if rest.lower().startswith(K.plain(title).lower()):
                rest = rest[len(K.plain(title)):].strip(" ·—–-.,;:!?")
            if rest and rest != tag:
                meaning.append(rest)
    if not meaning and assertion:
        meaning = [K.plain(assertion)]
    unseen(sid, pattern, blocks, {"quote", "para"},
           "на развилке рисуются только заголовок, смысловая строка и ярлык")

    tw = 10.0
    th = M.text_h(K.plain(title), 34, tw, spacing=1.05, bold=True)
    mh = (M.block_h(meaning, 17, 10.4, spacing=1.32, space_after=4)
          + M.line_h(17, 1.32)) if meaning else 0.0
    tag_h = 0.55 if tag else 0.0
    total = th + (mh + 0.34 if meaning else 0) + (tag_h + 0.30 if tag_h else 0)
    y = 1.25 + max((5.2 - total) / 2, 0.0)

    if badge:
        K.divider_badge(sl, badge, cy=y + th / 2)
    K.text_box(sl, 1.68, y, tw, th, title, size=34, bold=True, color=K.WHITE,
               spacing=1.05)
    y += th + 0.34
    if meaning:
        K.text_box(sl, D.LEFT + 0.35, y, 10.4, mh, meaning, size=17, italic=True,
                   color=K.ON_DARK, spacing=1.32, space_after=4)
        y += mh + 0.30
    if tag_h:
        K.tag_plate(sl, D.LEFT + 0.35, y, tag)
    if stage is not None:
        K.roadmap(sl, stages, stage)
    K.slide_number_mark(sl, D.slide_number(sid), on_dark=True)


def g_case_divider(sl, sid, title, blocks, pattern, assertion=""):
    """Дивайдер уровня КЕЙСА — легче разделительного на три вещи: без
    золотого номерного значка (кейс внутри ступени — не повод для сквозного
    счёта), без дорожной карты блоков занятия (зал уже видел, где он), без
    строки ярлыка. Вместо карты блоков — дорожка кейсов текущей ступени
    (`case_track`/`case_idx` конфига), тем же примитивом `K.roadmap`.

    Реплика кейса рисуется из `title` (H1 слайда), а не из блока-цитаты: на
    дивайдерах H1 и первая строка цитаты совпадают дословно, и рисовать оба
    значило бы напечатать одну фразу дважды. Вторая содержательная строка
    (приписка с источником цитаты, второй абзац) идёт ниже, мельче и
    приглушённее. Накопление СКЛЕИВАЕТ все непустые несовпадающие строки —
    перезапись последней роняла 2/3 текста второго абзаца."""
    K.divider_bg(sl)
    extra_parts = []
    title_key = K.plain(title).lower().strip(" «».")
    for kind, b in blocks:
        if kind != "quote":
            continue
        for ln in b:
            plain_ln = K.plain(ln).strip()
            if not plain_ln:
                continue
            if plain_ln.lower().strip(" «».") == title_key:
                continue
            extra_parts.append(plain_ln)
    extra = " ".join(extra_parts) if extra_parts else None
    if extra:
        m = ITALIC_LINE.match(extra)
        if m:
            extra = m.group(1).strip()

    tw = 10.6
    th = M.text_h(K.plain(title), 30, tw, spacing=1.18, bold=True)
    eh = (M.text_h(extra, 14, tw, spacing=1.3) + 0.22) if extra else 0.0
    total = th + eh
    y = 1.35 + max((4.5 - total) / 2, 0.0)

    K.text_box(sl, 1.35, y, tw, th, title, size=30, bold=True, color=K.WHITE,
               spacing=1.18)
    y += th + 0.2
    if extra:
        K.text_box(sl, 1.35, y, tw, eh, extra, size=14, italic=True,
                   color=K.ON_DARK_MUTE, spacing=1.3, rich=False)

    idx = D.case_idx().get(sid)
    if idx is not None:
        K.roadmap(sl, D.case_track(), idx)
    K.slide_number_mark(sl, D.slide_number(sid), on_dark=True)


def _cover_bg(sl, sid, title, *, tw, size, align=None):
    """Общее у обеих обложек: градиент DEEP→MID→LIGHT, заголовок, золотая
    полоса и hero-схема во всю ширину снизу, если она объявлена. Различие
    двух приёмов — ниже, в их собственных функциях; здесь только то, что у
    них действительно одно, иначе сведение превратилось бы в настройку."""
    K.gradient_rect(sl, 0, 0, K.W_IN, K.H_IN,
                    [(0, (0x21, 0x29, 0x5C)), (55000, (0x06, 0x5A, 0x82)),
                     (100000, (0x1C, 0x72, 0x93))])
    kw = {"align": align} if align is not None else {}
    K.text_box(sl, 0.9, 0.3, tw, 1.42, title, size=size, bold=True, color=K.WHITE,
               anchor=MSO_ANCHOR.MIDDLE, spacing=1.08, **kw)
    K.rect(sl, 0, 2.02, K.W_IN, 0.07, K.GOLD)
    y, bottom = 2.34, D.BOTTOM
    hero = D.figure_for(sid)
    if hero:
        from PIL import Image
        iw, ih = Image.open(hero).size
        fh = K.W_IN * ih / iw
        sl.shapes.add_picture(str(hero), Inches(0), Inches(K.H_IN - fh),
                              width=Inches(K.W_IN))
        bottom = K.H_IN - fh - 0.2
    return y, bottom


def g_cover(sl, sid, title, blocks, pattern, assertion=""):
    """Обложка Семинаров 5–6: заголовок прижат влево, подзаголовок отмечен
    тиловой планкой, центральный вопрос — в золотой коробке под ним. Номера
    занятия на видимом слое нет (отменённое исключение, issue 225)."""
    y, bottom = _cover_bg(sl, sid, title, tw=8.0, size=33)
    unseen(sid, pattern, blocks, {"quote"},
           "на обложке рисуются иллюстрация и центральный вопрос")
    quotes = [b for k, b in blocks if k == "quote"]
    if quotes:
        lines = [l for q in quotes for l in q]
        question = [l for l in lines if K.plain(l).rstrip("»\"' ").endswith("?")]
        rest = [l for l in lines if l not in question]
        if rest:
            h = M.block_h([K.plain(l) for l in rest], 15, 11.5, space_after=4)
            K.rect(sl, 0.9, y + 0.04, 0.035, h - 0.08, K.TEAL)
            K.text_box(sl, 1.2, y, 11.2, h, rest, size=15, color=K.ON_DARK,
                       space_after=4)
            y += h + 0.26
        if question:
            K.form_question(sl, 0.9, y, 11.5, question, size=17,
                            max_h=max(bottom - y, 0.7),
                            label=f"{sid} центральный вопрос")
    K.slide_number_mark(sl, D.slide_number(sid), on_dark=True)


def g_cover_centered(sl, sid, title, blocks, pattern, assertion=""):
    """Обложка Семинара 7: заголовок и подзаголовок отцентрованы по полотну,
    подзаголовок стоит в середине свободной полосы, тиловой планки нет.
    «Чистая» обложка — на ней нет ни содержания кейсов, ни номера занятия, и
    пустота читается как отступ, а не как дыра на месте снятого."""
    y, bottom = _cover_bg(sl, sid, title, tw=11.5, size=32, align=PP_ALIGN.CENTER)
    unseen(sid, pattern, blocks, {"quote"},
           "на обложке рисуются иллюстрация (если есть) и подзаголовок")
    quotes = [b for k, b in blocks if k == "quote"]
    if quotes:
        lines = [l for q in quotes for l in q]
        question = [l for l in lines if K.plain(l).rstrip("»\"' ").endswith("?")]
        rest = [l for l in lines if l not in question]
        if rest:
            h = M.block_h([K.plain(l) for l in rest], 18, 11.5, space_after=4)
            ry = (y + bottom) / 2 - h / 2
            K.text_box(sl, 0.9, ry, 11.5, h, rest, size=18, color=K.ON_DARK,
                       align=PP_ALIGN.CENTER, space_after=4)
            y = ry + h + 0.26
        if question:
            K.form_question(sl, 0.9, y, 11.5, question, size=17,
                            max_h=max(bottom - y, 0.7),
                            label=f"{sid} центральный вопрос")
    K.slide_number_mark(sl, D.slide_number(sid), on_dark=True)


def g_question(sl, sid, title, blocks, pattern, assertion=""):
    """Вопрос залу — дословный вопрос в золотой коробке, карточки вариантов
    под ним, ни одна не подсвечена. Единственное место с золотой заливкой;
    форма обязана оставаться редкой (канон §1)."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
    drawers = []
    for kind, b in blocks:
        if kind == "quote":
            scene, question, found = split_question(b)
            if not found:
                d = block_drawer(kind, b, sid, pattern)
                if d:
                    drawers.append(d)
                continue
            if scene:
                drawers.append(lambda sl, y, mh, s_=scene: K.form_speech(
                    sl, D.LEFT, y, D.WIDTH, s_, max_h=mh, label=f"{sid} сцена"))
            if question:
                drawers.append(lambda sl, y, mh, q=question: K.form_question(
                    sl, D.LEFT, y, D.WIDTH, q, max_h=mh, label=f"{sid} вопрос"))
        elif kind == "cards":
            drawers.append(lambda sl, y, mh, c=b: K.option_row(
                sl, D.LEFT, y, D.WIDTH, c, highlight_idx=None,
                max_h=min(mh or 1.8, 1.8), label=f"{sid} варианты"))
        else:
            d = block_drawer(kind, b, sid, pattern)
            if d:
                drawers.append(d)
    compose(sl, sid, y0, drawers, bottom=D.BOTTOM)
    K.slide_number_mark(sl, D.slide_number(sid))


# Доли колонок оси занятия заданы ЯВНО: таблица, возвращающаяся несколько раз
# за занятие, иначе пересчитывалась бы по своему содержимому на каждом
# возврате и выглядела бы другой таблицей (канон §4).
AXIS_COLS = (0.13, 0.27, 0.27, 0.33)


def _gold_quote_rule(sid, blocks):
    """Правило «цитата этого слайда — формула, не реплика»: `all` — все
    цитаты слайда, `last` — только последняя. Нужно там, где единственная
    подпись-итог слайда начинается с «ёлочки» и потому опознаётся как тихая
    реплика докладчика."""
    rule = D.table("gold_quote_sids").get(sid)
    total = sum(1 for k, _ in blocks if k == "quote") if rule == "last" else 0
    return rule, total


def g_axis_table(sl, sid, title, blocks, pattern, assertion=""):
    """Ось занятия и её возврат: таблица с явными долями колонок."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
    drawers = []
    gold_rule, quote_total = _gold_quote_rule(sid, blocks)
    quote_i = -1
    for kind, b in blocks:
        if kind == "table" and len(b[0]) == len(AXIS_COLS):
            inner = D.WIDTH - 0.4
            cols = [c * inner for c in AXIS_COLS]
            drawers.append(lambda sl, y, mh, h_=b[0], r_=b[1], c=cols: K.table_card(
                sl, D.LEFT, y, D.WIDTH, h_, r_, col_w=c, max_h=mh, label=f"{sid} ось"))
            continue
        role = None
        if kind == "quote" and gold_rule:
            quote_i += 1
            if gold_rule == "all" or (gold_rule == "last" and quote_i == quote_total - 1):
                role = "formula"
        d = block_drawer(kind, b, sid, pattern, role=role)
        if d:
            drawers.append(d)
    compose(sl, sid, y0, drawers)
    K.slide_number_mark(sl, D.slide_number(sid))


def g_criteria(sl, sid, title, blocks, pattern, assertion=""):
    """Граница применимости — таблица на две колонки становится двумя
    плашками бок о бок: «когда нужен · когда не нужен» прямой формой
    (правило А7)."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
    tables = [b for k, b in blocks if k == "table"]
    others = [(k, b) for k, b in blocks if k != "table"]
    force = D.table("quote_role_force")

    # Порядок блоков берётся ИЗ ФАЙЛА: врезка, написанная после таблицы,
    # рисуется под таблицей. Прежде все врезки выносились наверх скопом, и
    # слайд читался выводом вперёд доказательства — на Семинаре 7 предел
    # применимости и закрытие строки оси оказались НАД критериями, из которых
    # они следуют. Замечено владельцем, круг 9 (2026-10-15).
    first_table = next((i for i, (k, _) in enumerate(blocks) if k == "table"), len(blocks))
    pre = [(k, b) for i, (k, b) in enumerate(blocks) if k != "table" and i < first_table]
    post = [(k, b) for i, (k, b) in enumerate(blocks) if k != "table" and i > first_table]

    drawers = []
    for kind, b in pre:
        if kind == "quote":
            drawers.append(block_drawer(kind, b, sid, pattern, role=force.get(sid)))

    if len(tables) == 1 and len(tables[0][0]) == 2:
        headers, rows = tables[0]
        left = [r[0] for r in rows if len(r) > 0 and r[0].strip() and r[0].strip() != "—"]
        right = [r[1] for r in rows if len(r) > 1 and r[1].strip() and r[1].strip() != "—"]
        gap, cw = 0.3, (D.WIDTH - 0.3) / 2

        def pair(sl, y, mh, h_=headers, l_=left, r_=right, cw=cw, gap=gap):
            tall = max(measure(lambda s2, yy, m2, it=it, t=t, a=a: K.criterion_plate(
                           s2, D.LEFT, yy, cw, t, it, max_h=m2, accent=a), y, mh)
                       for t, it, a in ((h_[0], l_, K.SLATE), (h_[1], r_, K.GOLD_DARK)))
            K.criterion_plate(sl, D.LEFT, y, cw, h_[0], l_, max_h=mh, min_h=tall,
                              accent=K.SLATE, label=f"{sid} рано")
            K.criterion_plate(sl, D.LEFT + cw + gap, y, cw, h_[1], r_, max_h=mh,
                              min_h=tall, accent=K.GOLD_DARK, label=f"{sid} не нужно")
            return tall
        drawers.append(pair)
    else:
        accents = [None, K.GOLD_DARK, K.MID]
        for i, (headers, rows) in enumerate(tables):
            drawers.append(lambda sl, y, mh, h_=headers, r_=rows, a=accents[min(i, 2)]:
                           K.table_card(sl, D.LEFT, y, D.WIDTH, h_, r_, max_h=mh,
                                        accent=a, label=f"{sid} критерии"))

    for kind, b in post:
        if kind == "quote":
            drawers.append(block_drawer(kind, b, sid, pattern, role=force.get(sid)))
    for kind, b in others:
        if kind in ("bullets", "code", "cards", "para"):
            drawers.append(block_drawer(kind, b, sid, pattern))
    compose(sl, sid, y0, drawers)
    K.slide_number_mark(sl, D.slide_number(sid))


def g_closing(sl, sid, title, blocks, pattern, assertion=""):
    """Закрытие — вопрос открытия, заданный второй раз, и схема сразу под
    ним. Приём Семинара 5 (`closing_question_partial`/`transfer_exercise`);
    на Семинарах 6 и 7 ни одному имени не назначен, держится в библиотеке
    потому, что закрытие, РАЗРЕШАЮЩЕЕ занятие вместо инвентаризации, — одно
    из шести правил сторителлинга (канон §4.1, болезнь 4)."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
    drawers = []
    first = True
    for kind, b in blocks:
        if kind == "quote" and first:
            first = False
            drawers.append(lambda sl, y, mh, q=b: K.form_question(
                sl, D.LEFT, y, D.WIDTH, q, size=15.5, max_h=mh,
                label=f"{sid} вопрос открытия"))
            fig = D.figure_for(sid)
            if fig:
                drawers.append(lambda sl, y, mh, p=fig: K.figure(
                    sl, p, D.LEFT, y, D.WIDTH, mh if mh else 3.2, label=sid))
            continue
        d = block_drawer(kind, b, sid, pattern)
        if d:
            drawers.append(d)
    compose(sl, sid, y0, drawers)
    K.slide_number_mark(sl, D.slide_number(sid))


def g_content(sl, sid, title, blocks, pattern, assertion=""):
    """Содержательный слайд по умолчанию: заголовок-утверждение, схема (если
    объявлена), блоки в порядке источника. Жанр для БОЛЬШИНСТВА имён приёмов
    любой деки — различие между ними несёт роль блока, а не раскладка.

    `fig_after` конфига переносит схему ПОСЛЕ блоков: когда заголовок обещает
    собранный файл, первым читается код, а схема-компаньон — вторым."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
    drawers = []
    fig = D.figure_for(sid)
    fig_after = bool(fig) and sid in set(D.CFG.get("fig_after") or ())
    fig_ceiling = (D.BOTTOM - y0) if not blocks else K.FIG_NATURAL_H
    if fig and not fig_after:
        drawers.append(lambda sl, y, mh, p=fig: K.figure(
            sl, p, D.LEFT, y, D.WIDTH, mh if mh else fig_ceiling, label=sid))
    gold_rule, quote_total = _gold_quote_rule(sid, blocks)
    force = D.table("quote_role_force")
    quote_i = -1
    for kind, b in blocks:
        role = None
        if kind == "quote" and sid in force:
            role = force[sid]
        elif kind == "quote" and gold_rule:
            quote_i += 1
            if gold_rule == "all" or (gold_rule == "last" and quote_i == quote_total - 1):
                role = "formula"
        d = block_drawer(kind, b, sid, pattern, role=role)
        if d:
            drawers.append(d)
    if fig_after:
        drawers.append(lambda sl, y, mh, p=fig: K.figure(
            sl, p, D.LEFT, y, D.WIDTH, mh if mh else K.FIG_NATURAL_H, label=sid))
    compose(sl, sid, y0, drawers)
    K.slide_number_mark(sl, D.slide_number(sid))


TRACK_LABELS = ("база", "кромка")


def g_base_edge(sl, sid, title, blocks, pattern, assertion=""):
    """База и кромка на одном экране: две дорожки из одной таблицы на две
    колонки. Если таблицы нет — предупреждение и обычная раскладка, а не
    тихо пустой слайд."""
    left, right, labels, terms, rest = [], [], TRACK_LABELS, [], []
    for kind, b in blocks:
        if kind == "table" and not left and not right:
            headers, rows = b
            if headers and len(headers) >= 2 and any(K.plain(h).strip() for h in headers):
                labels = (K.plain(headers[0]).strip() or TRACK_LABELS[0],
                          K.plain(headers[1]).strip() or TRACK_LABELS[1])
            for r in rows:
                if len(r) > 0 and r[0].strip():
                    left.append(r[0].strip())
                if len(r) > 1 and r[1].strip():
                    right.append(r[1].strip())
            continue
        if kind == "cards" and not terms:
            terms = b
            continue
        rest.append((kind, b))

    if not (left and right):
        M._WARNINGS.append(f"ПРИЁМ [{sid} base_and_edge]: в «## Visual» нет таблицы "
                           f"из двух колонок — слайд собран обычной раскладкой")
        return g_content(sl, sid, title, blocks, pattern, assertion)

    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
    drawers = [lambda sl, y, mh: K.base_edge_tracks(
        sl, D.LEFT, y, D.WIDTH, left, right, left_label=labels[0],
        right_label=labels[1], terms=terms, max_h=mh, label=f"{sid} дорожки")]
    for kind, b in rest:
        d = block_drawer(kind, b, sid, pattern)
        if d:
            drawers.append(d)
    compose(sl, sid, y0, drawers, bottom=D.BOTTOM, center=1.0)
    K.slide_number_mark(sl, D.slide_number(sid))


# ── Реестр имён приёмов ─────────────────────────────────────────────────────
#
# Ключи — имена ЖАНРОВ, которыми конфиг занятия называет приём в `genres:`.
# Имя `content` — умолчание: имя приёма, не названное в конфиге, рисуется им.
GENRES = {
    "divider": g_divider,
    "case_divider": g_case_divider,
    "cover": g_cover,
    "cover_centered": g_cover_centered,
    "question": g_question,
    "axis_table": g_axis_table,
    "criteria": g_criteria,
    "closing": g_closing,
    "content": g_content,
    "base_edge": g_base_edge,
}

# Жанры, которые рисуют объявленную слайдом схему. Нужно аудиту: слайд,
# объявивший схему под приёмом, который её не рисует, не сработает никогда —
# и молча.
DRAWS_FIGURE = {"content", "closing", "cover", "cover_centered"}


def genre_name(pattern):
    return (D.table("genres").get(pattern)) or "content"


def genre_fn(pattern):
    name = genre_name(pattern)
    if name not in GENRES:
        M._WARNINGS.append(
            f"ЖАНР НЕИЗВЕСТЕН [{pattern} → {name}]: в deck-config.yaml назван "
            f"жанр, которого в библиотеке нет ({'/'.join(sorted(GENRES))}) — "
            f"слайд собран обычной раскладкой")
        return g_content
    return GENRES[name]


def draws_figure(pattern):
    return genre_name(pattern) in DRAWS_FIGURE
