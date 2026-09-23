"""Round-6 block-3 fast iteration build: only the three touched slides.

Builds `_test_blk3.pptx` with b3.s23 (display p33, TDD), b3.s25b (display p35,
BDD/trunk-based) and b3.s25c (display p36, локальный тестовый инструментарий)
so the Generate→Convert→Inspect→Fix loop does not pay for a 56-slide
LibreOffice conversion each iteration. Not part of the shipped build.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _helpers import setup_pres, ROOT, page_number  # noqa: E402
import slides_band3 as b3  # noqa: E402

OUT = ROOT / "rendered/_test_blk3.pptx"


def main():
    p = setup_pres()
    builders = [b3.s23, b3.s25b, b3.s25c]
    for fn in builders:
        fn(p)
    for i, slide in enumerate(p.slides, start=1):
        page_number(slide, i, len(builders))
    p.save(str(OUT))
    print(f"saved {OUT} — {len(builders)} slides")


if __name__ == "__main__":
    main()
