# -*- coding: utf-8 -*-
"""Независимый замер пола кегля по СОБРАННОМУ PDF — против счёта сборки.

Весь спор §3.9 прожарки был об этом: сборка говорила «один кадр ниже пола»,
PDF показывал шесть. После правки `tables.py` число сборки обязано сойтись
с числом PDF — и проверяется это повторным замером по файлу, а не
самоотчётом сборки.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[6]
                       / "tools" / "presentation-build"))
from deckkit import floor, pdfmeasure as pm, slidefile

PDF = sys.argv[1] if len(sys.argv) > 1 else "lec-07-karkas.pdf"
ids = [slidefile.read_slide(f).sid
       for f in slidefile.slide_files(Path("slides"))]
hist, by = pm.size_hist(PDF)
lo, tot, frac = pm.below(hist, floor.VIS_PT)
small = sorted(n for n, p in by.items()
               if any(s < floor.VIS_PT - 1e-9 for s in p))
print(f"порог пола видимого слоя: {floor.VIS_PT:.0f} пт")
print(f"знаков ниже пола: {lo} из {tot} = {100 * frac:.1f}%")
print(f"КАДРОВ ниже пола по PDF: {len(small)} — {small}")
for n in small:
    sizes = sorted(s for s in by[n] if s < floor.VIS_PT - 1e-9)
    sid = ids[n - 1] if n <= len(ids) else "?"
    print(f"  стр {n:>3}  {sid:<14} кегли "
          + ", ".join(f"{s:g} пт×{by[n][s]}" for s in sizes))
