#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сколько кадров деки несут НАСТОЯЩУЮ картинку — замер по PPTX, а не по PDF.

Зачем отдельный прогон. Посчитать это по собранному PDF нельзя, и попытка
посчитать врёт В ПОЛЬЗУ ДЕКИ: сборщик растрирует оформление постранично, поэтому
растровый элемент есть на КАЖДОЙ странице и ни один не повторяется между ними.
Замер 14 октября 2026 на деке из 101 кадра дал «101 из 101» — то есть ровно то
число, которое хочется увидеть, и оно неверно. Общих растров, которые можно было
бы отсечь как фон, в таком PDF нет вовсе.

Что считает этот прогон. В PPTX настоящая картинка лежит отдельным файлом в
`ppt/media/`, а кадр ссылается на неё связью в `ppt/slides/_rels/slideN.xml.rels`.
Оформление, плашки, схемы и текст связями не являются — они векторные фигуры.
Поэтому «кадр несёт снимок» здесь значит ровно одно: у кадра есть связь на файл
из `ppt/media/`.

Сверено с независимым счётом по полю `media:` файлов кадров (14 октября 2026,
разделы 1–4 и 6–8): **21 кадр по связям PPTX против 21 по полям** — сходится.
Расхождение в общем числе кадров (71 против 72) было ожидаемым и объяснимым:
дека успела вырасти на кадр между сборкой и замером.

**Чего прогон НЕ проверяет.** Что снимок виден, что он уместного размера и что
слово вокруг него говорит правду. Первые два проверяются глазами на собранной
странице, третье — сверкой О12 (реестр `images.md`): снимок открывается и
сличается с заголовком, телом, подвалом и абзацем заметок. На 25 кадрах эта
сверка нашла пять расхождений, и ни одно из них не нашлось бы ни правами
(все чисты), ни кеглем (все 15,0 пт), ни этим прогоном.

    python3 zamer_snimkov.py                     # по кускам parts-sec/
    python3 zamer_snimkov.py 'rendered/*.pptx'   # по другой сборке
"""
import os
import re
import sys
import zipfile
from glob import glob

SLIDE = re.compile(r"ppt/slides/slide(\d+)\.xml$")
TARGET = re.compile(r'Target="\.\./media/([^"]+)"')


def carriers(path):
    """(всего кадров, кадров со связью на файл из ppt/media/, имена файлов)."""
    z = zipfile.ZipFile(path)
    media = {n for n in z.namelist() if n.startswith("ppt/media/")}
    slides = sorted(
        (n for n in z.namelist() if SLIDE.match(n)),
        key=lambda n: int(SLIDE.match(n).group(1)),
    )
    used, carry = set(), 0
    for s in slides:
        rels = "ppt/slides/_rels/%s.rels" % os.path.basename(s)
        if rels not in z.namelist():
            continue
        names = {
            m.group(1)
            for m in TARGET.finditer(z.read(rels).decode("utf-8", "replace"))
            if "ppt/media/" + m.group(1) in media
        }
        if names:
            carry += 1
            used |= names
    return len(slides), carry, used


def main():
    pattern = sys.argv[1] if len(sys.argv) > 1 else "parts-sec/*.pptx"
    files = sorted(glob(pattern))
    if not files:
        print("сборок не найдено по образцу %r" % pattern)
        return 1
    total = carried = 0
    for p in files:
        n, c, used = carriers(p)
        total, carried = total + n, carried + c
        print("%-28s кадров %3d · со снимком %2d · файлов %2d"
              % (os.path.basename(p), n, c, len(used)))
    print("\nИТОГО: кадров %d · несут настоящую картинку %d (%.0f %%)"
          % (total, carried, 100.0 * carried / total))
    print("Для сравнения: в сданной Лекции 6 снимок несут 35 кадров из 100.")
    print("Прогон говорит только «связь есть». Виден ли снимок, уместен ли он по "
          "размеру и правду ли говорит слово вокруг него — проверяется глазами "
          "и сверкой О12 (см. images.md).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
