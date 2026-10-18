#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Где ляжет разрез на колонки — замер, а не на глаз.

`twocol.best_cut` берёт САМЫЙ РОВНЫЙ разрез; попадёт он на границу
смысловой группы или в её середину, не говорит ни отчёт, ни снимок. Этот
прогон печатает все законные разрезы с высотами колонок, чтобы правка
текста двигала разрез осознанно.

    python3 vkhod/razrez.py s03
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import build_lec07 as B                                     # noqa: E402
from deckkit import metrics, report, twocol                 # noqa: E402

_orig = twocol.fit_two


def spy(runs, w_col, h, w_plain, h_plain, **kw):
    tag = kw.get("tag", "")
    if tag.endswith("/тело"):
        print(f"{tag}: колонка {w_col:.2f}\" × {h:.2f}\"")
        for i in twocol.cuts_of(runs):
            top, bot = twocol.split_at(runs, i)
            ht = metrics.runs_h(top, w_col, 1.26)
            hb = metrics.runs_h(bot, w_col, 1.26)
            tail = " ".join(str(r.get("text") or "") for r in top)[-46:]
            mark = "  ВЛЕЗАЕТ" if max(ht, hb) <= h else ""
            print(f"  разрез {i:>3}: {ht:5.2f} / {hb:5.2f} "
                  f"скос {abs(ht - hb):4.2f}{mark}   …{tail.strip()}")
    return _orig(runs, w_col, h, w_plain, h_plain, **kw)


twocol.fit_two = spy
B.twocol.fit_two = spy
B.build(only=sys.argv[1], out=HERE / "probe.pptx")
report.reset()
(HERE / "probe.pptx").unlink(missing_ok=True)
