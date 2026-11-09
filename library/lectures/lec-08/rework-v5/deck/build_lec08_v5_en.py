#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EN build of the Lecture 8 v5 deck (issue #328) — thin wrapper around
`build_lec08_v5.py`'s own `build()`, pointed at `slides-en/` instead of
`slides/`.

Not a fork of the RU builder: all geometry, layout and self-checks stay in
`build_lec08_v5.py` (and the shared `deckkit` core) — this file only swaps
the slide source directory and the output path, and teaches `slidefile`
to recognize the EN body headers (`## Visible slide text` / `## Speaker
notes`) instead of the RU ones the main module already patched in for
`## Заметки`/`## Заметки лектора`.

    python3 build_lec08_v5_en.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))

import build_lec08_v5 as ru          # noqa: E402  (loads deckkit, sets floor.VIS_PT etc.)
from deckkit import render as rnd, report, slidefile  # noqa: E402

slidefile._SEC_VIS = r"##[ \t]*Visible slide text[ \t]*\r?\n(.*?)(?=\n##\s|\Z)"
slidefile._SEC_NOTES = r"##[ \t]*Speaker notes[ \t]*\r?\n(.*?)(?=\n##\s|\Z)"

LEC_ROOT = ru.LEC_ROOT
SLIDES_DIR_EN = LEC_ROOT / "slides-en"
OUT = LEC_ROOT / "rendered" / "lec-08-v5-en.pptx"
SNAPS = LEC_ROOT / "rendered" / "snapshots-en"


def main():
    n = ru.build(out=OUT, slides_dir=SLIDES_DIR_EN, root=LEC_ROOT)
    rnd.verify_built(OUT, partial=False)
    report.report(n, OUT.name)
    rnd.verify_links(OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
