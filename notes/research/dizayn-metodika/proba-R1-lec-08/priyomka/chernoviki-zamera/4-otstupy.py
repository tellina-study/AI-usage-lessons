# -*- coding: utf-8 -*-
"""Сколько разных левых отступов от поля живёт в колоде и сколько фигур ушло ЗА поле."""
import sys, statistics
from collections import Counter
from pptx import Presentation

MX = 39.6
TOL = 1.0

for path in sys.argv[1:]:
    prs = Presentation(path); W = prs.slide_width/12700.0
    otstupy = Counter(); za_polem = 0; vsego = 0; kadrov_s_begletsami = 0
    na_kadr = []
    for s in prs.slides:
        nk = set(); beg = 0
        for sh in s.shapes:
            if None in (sh.left, sh.width): continue
            l = sh.left/12700.0; w = sh.width/12700.0
            if w < 6 or w >= W - 1: continue        # подложки во всю ширину не считаем
            vsego += 1
            d = round(l - MX, 1)
            nk.add(round(d))
            otstupy[round(d)] += 1
            if l < MX - TOL:
                za_polem += 1; beg += 1
        if beg: kadrov_s_begletsami += 1
        na_kadr.append(len(nk))
    top = ", ".join(f"{k:+d}×{v}" for k, v in otstupy.most_common(7))
    print(f"{path.split('/')[-1]:26s} отступов от поля: {len(otstupy):3d} разных · "
          f"на кадре медиана {statistics.median(na_kadr):4.1f} · "
          f"за полем {za_polem:4d}/{vsego} фигур, кадров {kadrov_s_begletsami}/{len(na_kadr)}")
    print(f"{'':26s}   частые: {top}")
