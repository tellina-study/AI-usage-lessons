# -*- coding: utf-8 -*-
"""Поля по полосам: где начинается и кончается содержание в каждой полосе кадра."""
import sys, statistics
from pptx import Presentation

def polosy(s, W, H):
    """группирует фигуры в горизонтальные полосы по вертикальному перекрытию"""
    figs = []
    for sh in s.shapes:
        try:
            if None in (sh.left, sh.top, sh.width, sh.height): continue
            l, t = sh.left/12700.0, sh.top/12700.0
            w, h = sh.width/12700.0, sh.height/12700.0
        except Exception: continue
        if w < 6 or h < 4: continue
        if w > W - 2: continue
        if l < -50 or l > W + 50: continue
        figs.append((t, t+h, l, l+w))
    figs.sort()
    bands, cur = [], []
    for f in figs:
        if cur and f[0] < max(c[1] for c in cur) - 2:   # перекрываются по вертикали
            cur.append(f)
        else:
            if cur: bands.append(cur)
            cur = [f]
    if cur: bands.append(cur)
    return [(min(c[2] for c in b), max(c[3] for c in b), len(b)) for b in bands]

for path in sys.argv[1:]:
    prs = Presentation(path); W = prs.slide_width/12700.0; H = prs.slide_height/12700.0
    razb_l, razb_r = [], []
    podr = []
    for i, s in enumerate(prs.slides, 1):
        b = polosy(s, W, H)
        b = [x for x in b if x[2] >= 1]
        if len(b) < 2: continue
        lefts = [round(x[0], 1) for x in b]
        rights = [round(x[1], 1) for x in b]
        dl = max(lefts) - min(lefts)
        dr = max(rights) - min(rights)
        razb_l.append(dl); razb_r.append(dr)
        podr.append((i, len(b), dl, dr, lefts, rights))
    if not razb_l: continue
    print(f"{path.split('/')[-1]:28s} поле слева гуляет: медиана {statistics.median(razb_l):6.1f} пт (макс {max(razb_l):6.1f}) · "
          f"справа: медиана {statistics.median(razb_r):6.1f} пт (макс {max(razb_r):6.1f})")
    if "proba-R3" in path:
        for i, n, dl, dr, L, Rr in podr:
            m = " <<<" if max(dl, dr) > 12 else ""
            print(f"      к-{i:02d}: полос {n}, слева ±{dl:5.1f}, справа ±{dr:5.1f}{m}")
            if max(dl, dr) > 12:
                print(f"            левые края полос:  {L}")
                print(f"            правые края полос: {Rr}")
