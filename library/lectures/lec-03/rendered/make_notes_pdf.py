"""lec-03 notes-PDF wrapper (issue #171).

`tools/presentation-build/notes_pages_pdf.py` pairs PDF page N with the Nth
slide markdown in NATURAL-sort order (s01, s02, s02a, …). But Лекции 3 build
order (build_v3.py) is pedagogical, not natural-sort: it renders s15 BEFORE
s14 and s23 LATE (after s25/s25b/s25a). Natural-sort would mis-pair notes on 6
pages. This wrapper monkeypatches `slide_md_by_index` with build_v3's exact
order so each slide image gets its OWN notes (incl. the «Источники:» block).

Run: python3 make_notes_pdf.py
"""
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[4] / "tools/presentation-build"
sys.path.insert(0, str(TOOLS))
import notes_pages_pdf as N  # noqa: E402

LECDIR = Path(__file__).resolve().parents[1]        # …/lec-03
SLIDES = LECDIR / "slides"

# build_v3.py display order (MUST match its `sids` list 1:1).
BUILD_ORDER = [
    "s01", "s02", "s02a", "s03", "s04",
    "s04a", "s05", "s05a", "s05b", "s06", "s08", "s08a",
    "s09", "s10", "s11", "s12", "s13",
    "s13a", "s13b", "s15", "s14", "s16",
    "s18", "s19", "s21", "s22", "s22b",
    "s22c", "s22d", "s22e", "s25", "s25b", "s23",
    "s25a", "s26", "s27", "s27b", "s29", "s30", "s31",
]


def _md_by_index(slides_dir):
    out = {}
    for i, sid in enumerate(BUILD_ORDER, start=1):
        files = list(slides_dir.glob(f"{sid}-*.md"))
        if files:
            out[i] = files[0]
    return out


def main():
    N.slide_md_by_index = _md_by_index          # override ordering
    N.build(LECDIR, dpi=150, font_override=None)


if __name__ == "__main__":
    main()
