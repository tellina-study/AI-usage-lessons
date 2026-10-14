#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка и рендер ТОЛЬКО входа (s01…s05) в свой файл.

Отдельный выход нужен потому, что `build_lec07.py --only` пишет в
`lec-07-karkas.pptx` — общий файл деки, который собирают и другие сессии.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import build_lec07 as B                                    # noqa: E402
from deckkit import render as rnd, report                  # noqa: E402

IDS = "s01,s02,s03,s04,s05"
OUT = HERE / "vkhod.pptx"


def main():
    n = B.build(only=IDS, out=OUT)
    report.report(n, OUT.name)
    rnd.verify_links(OUT)
    if "--render" in sys.argv:
        return rnd.render(OUT, HERE / "snaps", timeout=400)
    return 0


if __name__ == "__main__":
    sys.exit(main())
