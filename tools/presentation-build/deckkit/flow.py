# -*- coding: utf-8 -*-
"""РАСКЛАДКА-ПОТОК: блоки кадра сверху вниз, по надписи на блок.

Одна из ДВУХ раскладок тела, которые держит этот пакет, и обе настоящие:

* ПОТОК (этот модуль, из lec-06) — единица блок: абзац, буллит, цитата,
  ТАБЛИЦА. У каждого своя надпись и свой отступ; кегль ОДИН на всё тело,
  наибольший, при котором тело влезает. Таблица встаёт там, где стояла в
  файле. Умеет разрезать тело на две колонки по перекосу высот.
* ПРОГОН (`metrics.fit_runs` + `prims.text_runs`, из lec-07) — единица
  абзац внутри ОДНОЙ надписи; кегли внутри разные (заголовок блока, тело,
  подпись) и масштабируются вместе. Таблиц не знает.

Перевести одну на другую нельзя, не потеряв: поток — таблицы и цитаты,
прогон — иерархию кеглей внутри тела. Поэтому их две, и выбор раскладки —
решение деки, а не ядра.
"""
from pptx.enum.text import PP_ALIGN

from . import metrics, prims, report, tables
# Имя модуля сокращено: у `fit_blocks` есть свой параметр `floor` (пол
# кегля ЭТОЙ раскладки), и он затенял бы модуль внутри функции.
from . import floor as vis_floor
from .markup import plain, runs_md
from .slidefile import blk_kind, blk_width
from .theme import DEEP, GOLD, MID, OUTLINE, TEAL

LS = 1.24                 # межстрочный в потоке
FLOOR = 8.0               # ниже кегль тела не опускается: будет вылет
READABLE = None           # порог «с задних рядов не читается» берётся у
                          # `vis_floor` В МОМЕНТ ВЫЗОВА (`vis_floor._floor`),
                          # а не застывает здесь при импорте: иначе `VIS_PT`,
                          # поднятый декой, не делает ничего. Своим числом он
                          # тоже не стоит: 13,0, стоявшие здесь, валили сборку
                          # на теле в 12,5 пт — то есть ВЫШЕ курсового порога
                          # проекции, — и это был второй голос об одном пороге
GAP_BLOCK = 0.16          # просвет между блоками
HI = 17.0                 # верхний кегль тела
COL_GAP = 0.40            # между двумя колонками тела
INDENT = 0.42             # отступ цитаты и буллита
ACCENT_DELTA = 0.5        # полужирное на полпункта крупнее


def para_h(text, size, w):
    """Высота абзаца. Мерится по АКЦЕНТНОМУ кеглю: `**полужирное**`
    набирается на полпункта крупнее (`notes/mcp-limitations.md` [#223-10]),
    и мера по светлому там недомеривает."""
    bold = "**" in text
    return metrics.est_h(plain(_blk_text(text)),
                         size + (ACCENT_DELTA if bold else 0.0),
                         w, LS, bold)


def _blk_text(text):
    if text.startswith(">"):
        return "\n".join(l.lstrip("> ").rstrip() for l in text.split("\n"))
    return text


def block_h(kind, val, size, w):
    if kind == "table":
        _, hs, _ = tables.table_geom(val, tables.tbl_size(val, size, w), w)
        return sum(hs)
    return para_h(val, size, blk_width(kind, w))


def blocks_h(blocks, size, w):
    h = sum(block_h(k, v, size, w) for k, v in blocks)
    return h + GAP_BLOCK * max(0, len(blocks) - 1)


def blocks_frames(blocks, size, w):
    """Блоки потока → `(куски, ширина рамки)` для `metrics.wrap_risk`.

    Таблица пропускается нарочно: её перенос идёт по ячейкам со своей мерой
    ширины столбцов и своим предупреждением `[столбец]`, и мерить её
    абзацной рамкой значило бы считать риск не там, где он есть."""
    out = []
    for kind, val in blocks:
        if kind == "table":
            continue
        bold = "**" in val
        out.append(([(plain(_blk_text(val)),
                      size + (ACCENT_DELTA if bold else 0.0), bold, False)],
                    blk_width(kind, w)))
    return out


def blocks_line_h(blocks, size):
    """Высота одной строки тела — тем кеглем, которым набран самый крупный
    блок. Столько стоит ОДИН несовпавший перенос."""
    bold = any("**" in v for _k, v in blocks)
    return (size + (ACCENT_DELTA if bold else 0.0)) * LS * metrics.LH / 72.0 \
        * metrics.SAFE


def fit_blocks(blocks, w, h, *, tag="", hi=HI, floor=FLOOR,
               readable=READABLE):
    """Наибольший кегль, при котором тело влезает в w × h.

    Два РАЗНЫХ исхода на дне лестницы, и различать их обязательно. Тело не
    влезло — `[высота]`. Тело влезло, а подбор всё равно упёрся в пол из-за
    `tbl_ok` (таблице при большем кегле не хватает ширины столбцов) —
    `[кегль]`. Прежде второе выходило как `[высота]` с ОТРИЦАТЕЛЬНЫМ вылетом
    («2,81" против 3,25"»): ложная тревога, по которой сессия раздела резала
    бы текст, который влезает."""
    readable = vis_floor._floor(readable)
    f = hi
    while f > floor:
        if blocks_h(blocks, f, w) <= h and tables.tbl_ok(blocks, f, w):
            break
        f -= 0.5
    if f <= floor:
        over = blocks_h(blocks, floor, w)
        if over > h:
            report.warn(
                f"[высота] {tag}: не влезает даже при {floor:.1f} пт — "
                f"{over:.2f}\" против {h:.2f}\" (вылет {over - h:.2f}\")")
        else:
            report.warn(
                f"[кегль] {tag}: тело опущено до пола {floor:.1f} пт не "
                "высотой, а таблицей — её столбцам при большем кегле не "
                f"хватает ширины; само тело занимает {over:.2f}\" из "
                f"{h:.2f}\"")
    elif f < readable:
        report.warn(f"[кегль] {tag}: тело ужалось до {f:.1f} пт "
                    f"(< {readable:.1f})")
    vis_floor.pt(f, tag, "тело потоком")
    metrics.check_thin_margin(blocks_frames(blocks, f, w), h,
                              blocks_h(blocks, f, w),
                              blocks_line_h(blocks, f), tag)
    return f


def flow(s, blocks, x, y, w, size, tag, *, accent=MID):
    """Блоки кадра одним потоком сверху вниз, в порядке файла.
    Возвращает занятую высоту."""
    cy = y
    for i, (kind, val) in enumerate(blocks):
        if kind == "table":
            ts = tables.tbl_size(val, size, w)
            tables.check_cols(val, ts, w, f"{tag}/таблица{i}")
            cy += tables.draw_table(s, x, cy, val, ts, w,
                                    f"{tag}/таблица{i}") + GAP_BLOCK
            continue
        bw = blk_width(kind, w)
        bx = x + (INDENT if kind in ("quote", "bullet") else 0.0)
        bh = para_h(val, size, bw)
        if kind == "quote":
            prims.rect(s, x, cy, 0.07, bh, GOLD, count="цитата")
        elif kind == "bullet":
            prims.rect(s, x + 0.10, cy + size / 72.0 * 0.55, 0.11, 0.11,
                       TEAL, radius=True, radius_adj=0.5, count="буллит")
        runs = runs_md(_blk_text(val) if kind != "quote"
                       else plain(_blk_text(val)),
                       size=size, color=DEEP, accent=accent,
                       accent_size=size + ACCENT_DELTA)
        prims.text_runs(s, bx, cy, bw, bh, runs, ls=LS, tag=f"{tag}/блок{i}")
        cy += bh + GAP_BLOCK
    return cy - y


# ── разрез тела на две колонки ──────────────────────────────────────


def is_head(kind, val):
    """Блок целиком полужирный — это вопрос или подзаголовок, а не абзац."""
    return (kind == "para" and val.startswith("**") and val.endswith("**")
            and val.count("**") == 2)


def cuts_of(blocks):
    """Места, где тело можно разрезать на колонки.

    Разрез сразу ПОСЛЕ подзаголовка запрещён: на `s102` он оставил вопрос
    «Что от этого стало с работой?» внизу левой колонки, а ответ на него —
    вверху правой. Если запрет не оставил ни одного места, он снимается:
    разрез где-то быть обязан, и выбор наугад хуже выбора по высотам."""
    ok = [i for i in range(1, len(blocks)) if not is_head(*blocks[i - 1])]
    return ok or list(range(1, len(blocks))) or [1]


def col_pair(hs, i):
    """Высоты левой и правой колонок при разрезе перед блоком `i`."""
    return (sum(hs[:i]) + GAP_BLOCK * (i - 1),
            sum(hs[i:]) + GAP_BLOCK * (len(hs) - i - 1))


def split_two(blocks, size, w, h=None):
    """Где разрезать тело на две колонки — и влезает ли хоть один разрез.

    Разрез ищется ПО ПЕРЕКОСУ, то есть по разнице высот колонок. Сумма
    высот обеих колонок от места разреза не зависит (блоки те же, просветов
    всегда на два меньше, чем блоков), поэтому «высокая колонка ниже» и
    «высоты ближе друг к другу» — одно и то же требование; по ЧИСЛУ БЛОКОВ
    тело не делится никогда.

    `h` задана — сначала отбираются разрезы, которые в неё ВЛЕЗАЮТ, и
    перекос считается уже среди них. Это и значит не мельчить кегль там, где
    ровный разрез не влез, а соседний влезает."""
    hs = [block_h(k, v, size, w) for k, v in blocks]
    cuts = cuts_of(blocks)
    fit = [i for i in cuts if max(col_pair(hs, i)) <= h] if h else []
    pool = fit or cuts
    best = min(pool, key=lambda i: abs(col_pair(hs, i)[0]
                                       - col_pair(hs, i)[1]))
    return best, (bool(fit) if h else True)


def two_columns(s, blocks, x, y, w, h, tag, *, hi=HI, floor=FLOOR,
                readable=READABLE, col_gap=COL_GAP):
    """Тело в две колонки с разделительной линейкой. Кегль подбирается так,
    чтобы нашёлся разрез, влезающий в высоту."""
    readable = vis_floor._floor(readable)
    cw = (w - col_gap) / 2
    f = hi
    while f > floor:
        if tables.tbl_ok(blocks, f, cw) and split_two(blocks, f, cw, h)[1]:
            break
        f -= 0.5
    i, ok = split_two(blocks, f, cw, h)
    if not ok:
        over = max(col_pair([block_h(k, v, f, cw) for k, v in blocks], i))
        report.warn(f"[высота] {tag}: две колонки не влезают даже при "
                    f"{f:.1f} пт — {over:.2f}\" против {h:.2f}\"")
    elif f < readable:
        report.warn(f"[кегль] {tag}: две колонки ужались до {f:.1f} пт "
                    f"(< {readable:.1f})")
    if ok:
        hs = [block_h(k, v, f, cw) for k, v in blocks]
        for side, part, used in (("лев", blocks[:i], col_pair(hs, i)[0]),
                                 ("прав", blocks[i:], col_pair(hs, i)[1])):
            metrics.check_thin_margin(blocks_frames(part, f, cw), h, used,
                                      blocks_line_h(part, f),
                                      f"{tag}/{side}")
    flow(s, blocks[:i], x, y, cw, f, f"{tag}/лев")
    flow(s, blocks[i:], x + cw + col_gap, y, cw, f, f"{tag}/прав")
    prims.rect(s, x + cw + col_gap / 2 - 0.005, y, 0.01, h, OUTLINE,
               count="линейка")
    return f, i
