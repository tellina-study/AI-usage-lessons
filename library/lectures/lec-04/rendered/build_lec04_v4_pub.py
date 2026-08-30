"""Full 41-slide build of Лекция 4 v4.1 «AI в жизненном цикле разработки ПО».

Methodology-first re-spine v4 (owner redirect #264) + edit pass v4.1
(#265/#266/#267/#268/#269): NEW foundations slide s05 (2 practice lists со
ссылками), keystone s06 переделан в ЦИКЛ ФАЗ (совпадает с роадмапом 0–7),
дивайдеры без тег-плашек, спека→требования в фазе требований, reqs
структура+процесс, нумерованная система ссылок [N] + кликабельные URL.

Source-of-truth: deck.yaml + deck-part2.yaml + slides/*.md (visible content +
visual_brief + readable speaker notes 150–300 слов).

Issue #170 · Branch: hc/lesson4-498d0d8c

Palette LOCKED: Ocean Gradient (#21295C / #065A82 / #1C7293) + Teal (#028090)
secondary + Gold (#F0AB00) ≥1×/slide. Motif «Ocean rounded box» на каждом
content-слайде. Canvas 13.333"×7.5" (16:9).

Structure (plan v4 §4):
  Р0 s01–s07 (введение + методическая рамка, без дивайдера) ·
  Р1 [s08] s09–s11 (требования) · Р2 [s12] s13–s15 (архитектура) ·
  Р3 [s16] s17–s21 (реализация) · Р4 [s22] s23–s24 (тестирование) ·
  Р5 [s25] s26–s31 (ревью+безопасность) · Р6 [s32] s33–s34 (доставка·ops·docs) ·
  Р7 [s35] s36–s40 (обобщение).
  7 section-dividers: s08 s12 s16 s22 s25 s32 s35. Keystone = s05.
  Hero required = s01 (METR chart) + s40 (closing photo). s11 iceberg illustration.

Build: python3 build_lec04_v4.py  → lec-04.pptx (40 slides s01..s40 monotonic).
Slide builders split into band modules (slides_band1..4.py), each importing
from _helpers.py. Charts pre-generated via gen_charts_v4.py.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _helpers import setup_pres, ROOT, page_number  # noqa: E402
import slides_band1 as b1  # noqa: E402
import slides_band2 as b2  # noqa: E402
import slides_band3 as b3  # noqa: E402
import slides_band4 as b4  # noqa: E402

OUT = ROOT / "rendered/lec-04-pub.pptx"


def main():
    p = setup_pres()
    # v4.1 (#265/#266/#267/#268/#269): 41 slides.
    # s05 = NEW foundations (b1.s05f); s06 = keystone phase-cycle (b1.s06k);
    # all subsequent builders keep their original function names but their
    # DISPLAY position shifts +1. load_notes keys already shifted to match the
    # renumbered slides/*.md (s05-foundations, s06-keystone, …, s41-bridge-qa).
    builders = []
    # display s01–s10
    builders += [b1.s01, b1.s02, b1.s03, b1.s04, b1.s05f,   # s05 foundations
                 b1.s06k,                                    # s06 keystone
                 b1.s06, b1.s07, b1.s08, b1.s09]             # s07..s10
    # display s11–s20
    builders += [b1.s10,                                     # s11
                 b2.s11, b2.s12, b2.s13, b2.s14, b2.s15,     # s12..s16
                 b2.s16, b2.s17, b2.s18, b2.s19]             # s17..s20
    # display s21–s30
    builders += [b2.s20,                                     # s21
                 b3.s21, b3.s22, b3.s23, b3.s24, b3.s25,     # s22..s26
                 b3.s26, b3.s27, b3.s28, b3.s29]             # s27..s30
    # display s31–s41
    builders += [b3.s30,                                     # s31
                 b4.s31, b4.s32, b4.s33, b4.s34, b4.s35,     # s32..s36
                 b4.s36, b4.s37, b4.s38, b4.s39, b4.s40]     # s37..s41

    assert len(builders) == 41, f"expected 41 builders, got {len(builders)}"
    for fn in builders:
        fn(p)

    # pub build: footer «N / TOTAL» disabled (footer-less).
    # total = len(builders)
    # for i, slide in enumerate(p.slides, start=1):
    #     page_number(slide, i, total)

    n = len(p.slides.__iter__.__self__._sldIdLst)
    assert n == 41, f"expected 41 slides, got {n}"
    p.save(str(OUT))
    print(f"saved {OUT} — {n} slides")


if __name__ == "__main__":
    main()
