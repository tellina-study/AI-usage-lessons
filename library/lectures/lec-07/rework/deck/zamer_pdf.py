#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Замер СОБРАННОГО PDF деки: мелкий текст, заголовки в две строки,
полупустые коробки, перехлёст картинки с гранью коробки.

Числа этого прогона — единственные, на которые в отчёте о раскладке можно
ссылаться: собственные числа сборщика трижды за эту работу расходились с
тем, что вышло на экран (`deckkit/pdfmeasure.py`, шапка).

    python3 zamer_pdf.py [путь к pdf]
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))

from deckkit import pdfmeasure as pm        # noqa: E402

FLOOR = 12.0
BOX_FILL = 0.75        # ниже этой доли заполнения коробка «полупустая»


def titles_wrapped(pages):
    """Кадры, у которых заголовок встал в две строки и больше."""
    out = []
    for n, st, _box in pages:
        runs = pm.text_runs(st)
        if not runs:
            continue
        ytop = max(y for _s, _c, _x, y in runs)
        sz = max(s for s, _c, _x, y in runs if y > ytop - 1)
        lh = sz * 1.08 * 1.19
        ys = sorted({round(y, 1) for s, _c, x, y in runs
                     if abs(s - sz) < 0.2 and x < 45 and y > ytop - 3.2 * lh},
                    reverse=True)
        lines = 1
        for a, b in zip(ys, ys[1:]):
            if abs((a - b) - lh) < lh * 0.35:
                lines += 1
            else:
                break
        if lines > 1:
            out.append((n, sz, lines))
    return out


def motif_boxes(pages, fill="#f4f7fa", min_w=550.0, min_h=50.0):
    """Коробка мотива ТЕЛА и доля её высоты, занятая текстом.

    Отбирается по ширине: полоса плашек и боксы схемы залиты той же
    поверхностью, но ни один из них не бывает шире 550 пт, а коробка тела —
    уже 900. Без этого отбора в счёт попадали плашки, у которых «пустая
    высота» ничего не значит: их высота и считается по содержимому."""
    out = []
    for n, st, _box in pages:
        runs = pm.text_runs(st)
        for bb, fl, _sk, _op in pm.paths(st):
            if pm.rgb(fl) != fill or (bb[2] - bb[0]) < min_w \
                    or (bb[3] - bb[1]) < min_h:
                continue
            inside = [(y, sz) for sz, _c, x, y in runs
                      if bb[0] <= x <= bb[2] and bb[1] <= y <= bb[3]]
            if not inside:
                continue
            # Высота текста — НЕ размах базовых линий. Размах у блока в две
            # строки равен ОДНОМУ межстрочному, а у блока в одну строку —
            # нулю: коробка с единственной строкой читалась как «заполнена
            # на 0 %», а с двумя — как «на половину». Именно так и вышел
            # кадр 66 («41 %»), который глазами полон. Берётся число строк,
            # помноженное на ИЗМЕРЕННЫЙ шаг строк — медиану расстояний
            # между соседними базовыми линиями этой же коробки; у
            # единственной строки шага взять неоткуда, и тогда её высотой
            # считается её собственный кегль.
            ys = sorted({round(y, 1) for y, _sz in inside}, reverse=True)
            steps = sorted(a - b for a, b in zip(ys, ys[1:]))
            pitch = steps[len(steps) // 2] if steps else \
                max(sz for _y, sz in inside)
            used = len(ys) * pitch
            h = bb[3] - bb[1]
            out.append((n, h, used / h if h else 0.0))
    return out


def body_lines(pages, bpg=1, fill="#f4f7fa", min_w=550.0, min_h=50.0):
    """Строки ТЕЛА внутри коробки мотива: знаков в строке и сколько колонок.

    Длина строки — то, из-за чего две колонки и заводились: 135 знаков в
    строке против 49 у Лекции 6 (замер круга #229). Мерится по собранному
    PDF: знаки одной строки — прогоны с одной координатой `y` внутри
    коробки; колонка узнаётся по левому краю строк — два устойчивых края,
    разнесённых больше чем на 100 пт, и есть две колонки.

    Отбор коробки тот же, что у `motif_boxes`, и по той же причине: полоса
    плашек и боксы схемы залиты той же поверхностью, но уже 550 пт."""
    out = []
    for n, st, _box in pages:
        runs = pm.text_runs(st, bpg=bpg)
        for bb, fl, _sk, _op in pm.paths(st):
            if pm.rgb(fl) != fill or (bb[2] - bb[0]) < min_w \
                    or (bb[3] - bb[1]) < min_h:
                continue
            inside = [(g, x, y) for sz, g, x, y in runs
                      if bb[0] <= x <= bb[2] and bb[1] <= y <= bb[3]
                      and sz <= 17.5]
            if not inside:
                continue
            # Колонки — по ЛЕВОМУ КРАЮ СТРОК, а не по краю прогонов:
            # строка набирается многими прогонами (слово — прогон), их `x`
            # идут по всей её длине, и разрыв между словами разреженной
            # строки читался как граница колонки. Левый край строки у всех
            # строк одной колонки один и тот же, поэтому край берётся как
            # минимум `x` на высоте. Разнос больше 100 пт — разные колонки:
            # это заведомо больше отступа цитаты или буллита (0,42" = 30 пт)
            # и заведомо меньше просвета между колонками.
            rows = {}
            for _g, x, y in inside:
                k = round(y, 1)
                rows[k] = min(rows.get(k, x), x)
            lefts = sorted(set(round(v) for v in rows.values()))
            cuts = [(a + b) / 2 for a, b in zip(lefts, lefts[1:])
                    if b - a > 100]
            # Строка считается ВНУТРИ КОЛОНКИ. Без этого левая и правая
            # строки одной высоты складывались в одну «строку» двойной
            # длины — и замер двух колонок показывал ровно то, что они
            # должны были устранить.
            lines = {}
            for g, x, y in inside:
                k = (sum(1 for c in cuts if x > c), round(y, 1))
                lines[k] = lines.get(k, 0) + g
            out.append((n, max(lines.values()), len(cuts) + 1, len(lines)))
    return out


def media_cuts(pages, stroke="#1c7293"):
    """Картинки, пересекающие грань обведённой коробки."""
    out = []
    for n, st, _box in pages:
        boxes = [bb for bb, _f, sk, _o in pm.paths(st)
                 if pm.rgb(sk) == stroke and (bb[2] - bb[0]) > 200]
        for nm, ib, skew in pm.images(st):
            for bb in boxes:
                area, dx, dy = pm.overlap(ib, bb)
                inside = (ib[0] >= bb[0] - 1 and ib[1] >= bb[1] - 1
                          and ib[2] <= bb[2] + 1 and ib[3] <= bb[3] + 1)
                if area > 100 and not inside:
                    out.append((n, nm, round(dx, 1), round(dy, 1),
                                round(area), skew))
    return out


def main():
    pdf = sys.argv[1] if len(sys.argv) > 1 else str(HERE / "lec-07-karkas.pdf")
    pages = pm.pages(pdf)
    bpg = pm.glyph_bytes(Path(pdf).read_bytes())
    hist, by = pm.size_hist(pdf)
    lo, tot, frac = pm.below(hist, FLOOR)
    small = sorted(n for n, p in by.items() if any(s < FLOOR - 1e-9 for s in p))
    print(f"кадров: {len(pages)}; байт на знак в этом файле: {bpg}")
    print(f"знаков ниже {FLOOR:.0f} пт: {lo} из {tot} = {100 * frac:.1f}% "
          f"— на {len(small)} кадрах: {small}")
    print("  ярусы: " + (" · ".join(f"{s:g}пт×{hist[s]}"
                                    for s in sorted(hist) if s < FLOOR)
                         or "нет"))
    tw = titles_wrapped(pages)
    print(f"\nзаголовков в две строки и более: {len(tw)} — "
          + ", ".join(f"кадр {n} ({s:g} пт, {l} стр.)" for n, s, l in tw))
    boxes = motif_boxes(pages)
    half = [b for b in boxes if b[2] < BOX_FILL]
    bad = [b for b in boxes if b[2] < 0.5]
    print(f"\nкоробок мотива тела: {len(boxes)}; заполнены меньше чем на "
          f"{100 * BOX_FILL:.0f}%: {len(half)}; меньше чем наполовину: "
          f"{len(bad)}")
    for n, h, f in sorted(half, key=lambda b: b[2])[:12]:
        print(f"  кадр {n}: коробка {h:.0f} пт, текст занял {100 * f:.0f}%")
    bl = body_lines(pages, bpg)
    if bl:
        two = [b for b in bl if b[2] >= 2]
        worst = max(bl, key=lambda b: b[1])
        print(f"\nкоробок тела со строками: {len(bl)}; в две колонки и "
              f"более: {len(two)}; самая длинная строка {worst[1]} знаков "
              f"(кадр {worst[0]})")
        print("  десять самых длинных строк: " + " · ".join(
            f"кадр {b[0]}: {b[1]} зн./{b[2]} кол."
            for b in sorted(bl, key=lambda b: -b[1])[:10]))
    cuts = media_cuts(pages)
    print(f"\nкартинок, пересекающих грань коробки: {len(cuts)}")
    for c in cuts:
        print(f"  кадр {c[0]}: {c[1]} перехлёст {c[2]}×{c[3]} пт "
              f"({c[4]} кв. пт)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
