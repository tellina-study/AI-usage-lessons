# -*- coding: utf-8 -*-
"""Разброс вертикалей: сколько различных левых/правых краёв на кадре."""
import sys, statistics
from pptx import Presentation
from pptx.util import Emu

TOL_PT = 4.0  # допуск склейки краёв в пунктах

def klastery(vals, tol):
    vals = sorted(vals)
    out, cur = [], [vals[0]]
    for v in vals[1:]:
        if v - cur[-1] <= tol:
            cur.append(v)
        else:
            out.append(cur); cur = [v]
    out.append(cur)
    return out

def kadry(path):
    prs = Presentation(path)
    W = prs.slide_width / 12700.0
    for i, s in enumerate(prs.slides, 1):
        L, R = [], []
        for sh in s.shapes:
            try:
                if sh.left is None or sh.width is None: continue
                l = sh.left / 12700.0; w = sh.width / 12700.0
            except Exception:
                continue
            if w < 6 or w > W - 2: continue      # мусор и полноширинные подложки
            if l < -50 or l > W + 50: continue
            L.append(round(l, 2)); R.append(round(l + w, 2))
        if not L: 
            yield i, 0, 0, 0.0, 0.0, 0
            continue
        kl, kr = klastery(L, TOL_PT), klastery(R, TOL_PT)
        # разброс внутри кластера = сколько «почти совпало, но не совпало»
        razbros_l = max((max(c) - min(c)) for c in kl)
        razbros_r = max((max(c) - min(c)) for c in kr)
        yield i, len(kl), len(kr), razbros_l, razbros_r, len(L)

for path in sys.argv[1:]:
    print("=" * 70)
    print(path.split("/")[-1])
    vl, vr, rr = [], [], []
    for i, nl, nr, rl, rrr, n in kadry(path):
        vl.append(nl); vr.append(nr); rr.append(max(rl, rrr))
        flag = " <<<" if (nl + nr) > 8 or max(rl, rrr) > TOL_PT * 0.9 else ""
        print(f"  к-{i:02d}: левых {nl}  правых {nr}  "
              f"разброс в кластере {max(rl,rrr):5.2f} пт  (фигур {n}){flag}")
    if vl:
        print(f"  ИТОГ: левых медиана {statistics.median(vl):.1f} (макс {max(vl)}) · "
              f"правых медиана {statistics.median(vr):.1f} (макс {max(vr)}) · "
              f"сумма медиана {statistics.median([a+b for a,b in zip(vl,vr)]):.1f}")
