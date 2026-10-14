#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Контактный лист собранных страниц — чтобы смотреть деку глазами пачками.

Зачем. Три прогона деки отвечают на вопросы «права чисты?», «текст уложился?»,
«снимок есть?», и ни один не отвечает на вопрос «а как это выглядит». Класс
дефектов «кадр собрался чисто, а на экране не читается» ловится только глазом —
но смотреть 101 страницу по одной дорого, а по шесть за взгляд обозримо.

Этим прогоном за 14 октября 2026 найдено: подделка, выданная за снимок (`s01d`);
три расхождения снимка со словом вокруг него (`s11`, `s35`, `s52`); ключевое
число, набранное золотом при контрасте 1,99 : 1 (`s85`, затем ещё пять кадров);
и то, что кадры у предела в 137–140 слов оставляют около 40 % площади пустой,
то есть предел — про чтение, а не про место.

**Лист не заменяет просмотр в полный размер.** Он нужен, чтобы отобрать, что
смотреть крупно: в ячейке 620 точек видно наезд, обрез, пустоту и бледность, но
не видно, читается ли подпись внутри снимка. Найденное в ячейке открывается
отдельно — так и были пойманы все пять расхождений.

    # все страницы куска, по шесть на лист
    python3 kontaktnyy_list.py --pages 'parts-sec/snaps1-2-3-*/k-*.png'

    # только нужные кадры, с подписями по идентификатору кадра
    python3 kontaktnyy_list.py --pages 'parts-sec/snaps4-6-7-*/k-*.png' \\
        --report otchet-4-6-7.txt --ids s53,s54,s65a

`--report` — вывод `render_sec.py`: из него берутся имена файлов кадров в
порядке страниц, и ячейки подписываются идентификатором кадра, а не `k-07.png`.
Без него подписи — имена файлов страниц.
"""
import argparse
import os
import re
from glob import glob

CELL = 620
PER_SHEET = 6
COLS = 3
ROW_LABEL = 26


def pages_of(pattern):
    def num(p):
        m = re.search(r"k-0*(\d+)", os.path.basename(p))
        return (os.path.dirname(p), int(m.group(1)) if m else 0)
    return sorted(glob(pattern), key=num)


def labels_from(report):
    """Имена файлов кадров в порядке страниц — из отчёта render_sec.py."""
    if not report or not os.path.exists(report):
        return []
    out = []
    for line in open(report, encoding="utf-8"):
        m = re.match(r"^\s*\d+\s+(s\S+\.md)\s*$", line)
        if m:
            out.append(m.group(1))
    return out


def sheet(cells, out):
    from PIL import Image, ImageDraw
    rows = (len(cells) + COLS - 1) // COLS
    im = Image.new("RGB", (COLS * CELL, rows * (CELL + ROW_LABEL)), (255, 255, 255))
    d = ImageDraw.Draw(im)
    for i, (path, label) in enumerate(cells):
        try:
            t = Image.open(path).convert("RGB")
        except OSError as e:
            print("  пропущено %s: %s" % (path, e))
            continue
        t.thumbnail((CELL - 8, CELL - 8))
        x = (i % COLS) * CELL + (CELL - t.width) // 2
        y = (i // COLS) * (CELL + ROW_LABEL) + ROW_LABEL - 4
        im.paste(t, (x, y))
        d.text(((i % COLS) * CELL + 6, (i // COLS) * (CELL + ROW_LABEL) + 6),
               "%d  %s" % (i + 1, label[:58]), fill=(0, 0, 0))
    im.save(out, quality=88)
    print("  %s — %d ячеек, %dx%d" % (out, len(cells), im.width, im.height))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", default="parts-sec/snaps*/k-*.png")
    ap.add_argument("--report", default=None, help="вывод render_sec.py для подписей")
    ap.add_argument("--ids", default=None, help="через запятую: s44,s38")
    ap.add_argument("--out", default="kontaktnyy-list", help="основа имени листов")
    a = ap.parse_args()

    pages = pages_of(a.pages)
    if not pages:
        print("страниц не найдено по образцу %r" % a.pages)
        return 1
    names = labels_from(a.report)
    if names and len(names) != len(pages):
        print("ОСТОРОЖНО: в отчёте %d имён, страниц %d — подписи сдвинутся, "
              "беру имена файлов страниц" % (len(names), len(pages)))
        names = []

    cells = []
    for i, p in enumerate(pages):
        label = names[i] if i < len(names) else os.path.basename(p)
        cells.append((p, label))

    if a.ids:
        want = {s.strip() for s in a.ids.split(",") if s.strip()}
        if not names:
            print("--ids требует --report: без него идентификатор кадра неизвестен")
            return 1
        cells = [c for c in cells if c[1].split("-")[0] in want]
        missing = want - {c[1].split("-")[0] for c in cells}
        if missing:
            print("не найдено в этой сборке: %s" % ", ".join(sorted(missing)))
        if not cells:
            return 1

    print("Контактные листы (%d страниц, по %d на лист):" % (len(cells), PER_SHEET))
    for n in range(0, len(cells), PER_SHEET):
        sheet(cells[n:n + PER_SHEET], "%s-%02d.jpg" % (a.out, n // PER_SHEET + 1))
    print("Лист — отбор, а не приёмка: найденное в ячейке открывается в полный "
          "размер отдельно.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
