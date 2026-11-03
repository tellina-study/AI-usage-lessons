# -*- coding: utf-8 -*-
"""Дрожь вертикалей: пары краёв, разведённые на заметно-но-мало."""
import sys, statistics
from pptx import Presentation

DROZH_LO, DROZH_HI = 0.5, 9.0   # пт: видно, что не совпало, но непохоже на замысел

def kraya(s, W):
    L, R = [], []
    for sh in s.shapes:
        try:
            if sh.left is None or sh.width is None: continue
            l = sh.left/12700.0; w = sh.width/12700.0
        except Exception: continue
        if w < 6 or w > W - 2: continue
        if l < -50 or l > W + 50: continue
        L.append(l); R.append(l+w)
    return L, R

def drozh(vals):
    """число пар соседних краёв, разведённых на 0.5..9 пт"""
    v = sorted(vals); n = 0; pary = []
    for a, b in zip(v, v[1:]):
        d = b - a
        if DROZH_LO <= d <= DROZH_HI:
            n += 1; pary.append(round(d, 1))
    return n, pary

for path in sys.argv[1:]:
    prs = Presentation(path); W = prs.slide_width/12700.0
    vsego, podrobno = [], []
    for i, s in enumerate(prs.slides, 1):
        L, R = kraya(s, W)
        if not L: continue
        nl, pl = drozh(L); nr, pr = drozh(R)
        vsego.append(nl+nr); podrobno.append((i, nl+nr, pl+pr))
    if not vsego: continue
    print(f"{path.split('/')[-1]:28s} дрожь: медиана {statistics.median(vsego):4.1f} · "
          f"макс {max(vsego):3d} · кадров с дрожью {sum(1 for v in vsego if v)}/{len(vsego)} · "
          f"всего пар {sum(vsego)}")
    if "proba-R3" in path:
        for i, n, p in podrobno:
            if n: print(f"      к-{i:02d}: {n:2d} пар, разводы {p} пт")
