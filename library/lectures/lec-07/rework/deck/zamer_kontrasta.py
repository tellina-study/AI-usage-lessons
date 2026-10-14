#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Контраст цветов палитры на собранных страницах — замер, а не впечатление.

Зачем. 14 октября 2026 приёмка нашла на `s85`, что ЗНАЧЕНИЕ ключевой плашки —
то самое число, по которому назван кадр, — набрано золотом курса `#F0AB00` на
белом. Это **1,99 : 1** при пороге доступности 4,5 : 1 для мелкого текста и
3,0 : 1 для крупного: в зале самое важное число кадра оказывается самым бледным
на нём. Ключевая плашка стоит на 55 кадрах из 101.

Главное про этот класс дефектов: **его не видит ни одна другая проверка**.
Сборка чиста, кегль 15,0 пт, блокирующих предупреждений ноль, `zamer_snimkov.py`
доволен — потому что все три проверки про другое (права, размер, наличие связи).
Поймать это можно либо глазом на проекторе, либо вот этим прогоном.

Что прогон делает. Считает долю пикселей каждого цвета палитры на каждой
собранной странице и печатает контраст этого цвета к двум фонам деки — белому и
поверхности `#F4F7FA`. Цвет, которого на странице заметно много и у которого
контраст ниже порога, — кандидат в дефект.

**Чего прогон НЕ делает, и это важно не перепутать.** Он не отличает текст от
рамки, заливки и черты: золото в деке законно стоит рамкой плашки, чертой под
заголовком и меткой-ярлыком — там низкий контраст дефектом не является, потому
что читать рамку не нужно. Прогон только НАЗЫВАЕТ страницы, где цвет с низким
контрастом присутствует в количестве, похожем на текст; решает глаз. Поэтому
вывод — список адресов для просмотра, а не вердикт.

Решение владельца О3 (`notes/decisions-owner.md`): ключевое число набирается
`1C7293` или `028090` (5,42 и 4,67 против 1,99), золото остаётся рамкой, чертой
и меткой; палитра не меняется ни на один цвет. Этот прогон проверяет, что
решение доехало до кода, — 14 октября оказалось, что не доехало.

    python3 zamer_kontrasta.py                        # по кускам parts-sec/
    python3 zamer_kontrasta.py 'rendered/snaps*/*.png'
"""
import os
import sys
from collections import Counter
from glob import glob

PALETTE = {
    "золото #F0AB00": (240, 171, 0),
    "бирюза #028090": (2, 128, 144),
    "синь #1C7293": (28, 114, 147),
    "тёмная синь #21295C": (33, 41, 92),
    "морская #065A82": (6, 90, 130),
}
GROUNDS = {"белый": (255, 255, 255), "поверхность #F4F7FA": (244, 247, 250)}
AA_SMALL, AA_LARGE = 4.5, 3.0
TOL = 18          # допуск на сжатие в PNG
TEXTISH = 0.0012  # доля страницы, ниже которой цвет — скорее черта, чем текст


def _lin(v):
    v /= 255.0
    return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4


def luminance(c):
    return 0.2126 * _lin(c[0]) + 0.7152 * _lin(c[1]) + 0.0722 * _lin(c[2])


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def page_counts(path):
    from PIL import Image
    im = Image.open(path).convert("RGB")
    im = im.resize((im.width // 2, im.height // 2))
    seen = Counter(im.getdata())  # noqa: совместимость с Pillow < 11
    total = im.width * im.height
    out = {}
    for name, col in PALETTE.items():
        n = sum(
            cnt for px, cnt in seen.items()
            if all(abs(px[i] - col[i]) <= TOL for i in range(3))
        )
        out[name] = n / float(total)
    return out


def main():
    pattern = sys.argv[1] if len(sys.argv) > 1 else "parts-sec/snaps*/*.png"
    pages = sorted(glob(pattern))
    if not pages:
        print("страниц не найдено по образцу %r" % pattern)
        return 1

    print("Контраст цветов палитры к фонам деки (порог AA: %.1f мелкий, %.1f крупный)\n"
          % (AA_SMALL, AA_LARGE))
    low = []
    for name, col in PALETTE.items():
        cells = []
        for gname, g in GROUNDS.items():
            r = contrast(col, g)
            cells.append("%s %.2f%s" % (gname, r, " ⚠" if r < AA_LARGE else ""))
        if min(contrast(col, g) for g in GROUNDS.values()) < AA_SMALL:
            low.append(name)
        print("  %-22s %s" % (name, " · ".join(cells)))

    if not low:
        print("\nЦветов ниже порога нет.")
        return 0

    print("\nНиже порога мелкого текста: %s" % ", ".join(low))
    print("Где они присутствуют в количестве, похожем на текст "
          "(доля страницы > %.2f %%):\n" % (TEXTISH * 100))
    flagged = 0
    for p in pages:
        share = page_counts(p)
        hot = [n for n in low if share.get(n, 0) > TEXTISH]
        if hot:
            flagged += 1
            print("  %-34s %s" % (
                os.path.join(os.path.basename(os.path.dirname(p)), os.path.basename(p)),
                " · ".join("%s %.2f %%" % (n, share[n] * 100) for n in hot)))
    print("\nСтраниц просмотрено %d · названо для просмотра глазами %d"
          % (len(pages), flagged))
    print("Прогон не отличает текст от рамки и черты: золото законно стоит "
          "рамкой плашки, чертой под заголовком и меткой. Решает глаз — это "
          "список адресов, а не вердикт.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
