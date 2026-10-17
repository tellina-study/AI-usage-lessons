#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сумма timing_min по разделу: `python3 zamer_minut.py 7 8 9 10`."""
import re, sys, yaml
from pathlib import Path
import build_lec07 as B
from deckkit import slidefile

want = set(sys.argv[1:])
tot = {}
for f in slidefile.slide_files(B.SLIDES_DIR):
    m = re.match(r"^---\n(.*?)\n---", f.read_text(encoding='utf-8'), re.S)
    meta = yaml.safe_load(m.group(1)) if m else {}
    sec = str((meta or {}).get('section') or '')
    k = sec.split('.')[0]
    if k in want:
        tot.setdefault(k, []).append(float(meta.get('timing_min') or 0))
for k in sorted(tot, key=int):
    print(f"раздел {k}: кадров {len(tot[k])} · {sum(tot[k]):.2f} мин")
print(f"итого {sum(sum(v) for v in tot.values()):.2f} мин")
