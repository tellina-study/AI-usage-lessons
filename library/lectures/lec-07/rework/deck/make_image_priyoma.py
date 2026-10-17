#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Картинка нулевого кадра блока о человеке (#244, §8): врач и пациент рядом.

Не новая добыча — сшивка ДВУХ уже существующих в этой деке настоящих фото
через `analitika.ryadom()`: `assets/s35-vrach-chitaet-s-ekrana.jpg` (врач,
не вкручено никуда) и `assets/s22-rentgenkabinet-pacient-u-pribora.jpg`
(пациент, вкручено только в s22-divider, визуально далеко по вечеру).
Провенанс каждой половины — в её собственном `.url`; провенанс сшивки —
`assets/priyom-vrach-i-patsient.url`.

Высоты приведены к одной (1131 px, высота меньшего фото) ПЕРЕД сшивкой —
иначе `ryadom()` расположил бы их по центру на разной высоте, но ширина
результата была бы той же; приведение высот делает картинку компактнее
по ширине и не меняет смысла.

    python3 make_image_priyoma.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))

import analitika as A  # noqa: E402
from PIL import Image  # noqa: E402

ASSETS = HERE / "assets"
VYSOTA = 1131


def _k_vysote(put, h):
    im = Image.open(put)
    w = int(im.width * h / im.height)
    tmp = Path("/tmp") / f"_resized_{put.name}"
    im.resize((w, h), Image.LANCZOS).save(tmp, quality=92)
    return tmp


def main():
    vrach = _k_vysote(ASSETS / "s35-vrach-chitaet-s-ekrana.jpg", VYSOTA)
    pacient = _k_vysote(ASSETS / "s22-rentgenkabinet-pacient-u-pribora.jpg",
                        VYSOTA)
    out = A.ryadom(vrach, pacient, ASSETS / "priyom-vrach-i-patsient.jpg",
                   zazor_pt=14, chetkost=1)
    im = Image.open(out)
    print(f"{out}: {im.width}×{im.height}, ar={im.width / im.height:.2f}, "
          f"{out.stat().st_size} Б")
    return 0


if __name__ == "__main__":
    sys.exit(main())
