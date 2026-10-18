#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Альбомный кроп пациента для `dve-storony-priyoma.md` (поле `media_2`).

Оригинал `s22-rentgenkabinet-pacient-u-pribora.jpg` (1920x2017, ar≈1,05) —
портретный, и у него уже есть своя роль (`s22-divider-analiz-dannykh.md`):
трогать сам файл нельзя. Режиму участников (§8, #262) нужен снимок ближе к
альбомному аспекту первого фото (врач, ≈0,71) — портретный роняет подпись
через `spill` (#264) и съедает бюджет высоты тела кадра. Решение — отдельный
кроп, не новая добыча и не правка источника: верх (потолок, трубы аппарата)
срезан, пациент и стол остались полностью.

    python3 make_crop_dve_storony.py
"""
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
SRC = HERE / "s22-rentgenkabinet-pacient-u-pribora.jpg"
OUT = HERE / "dve-storony-pacient-landscape.jpg"
TARGET_AR = 0.707  # аспект первого снимка (врач, s35)


def main():
    im = Image.open(SRC)
    w, h = im.size
    new_h = int(w * TARGET_AR)
    crop_top = h - new_h
    cropped = im.crop((0, crop_top, w, h))
    cropped.save(OUT, quality=92)
    print(f"{OUT.name}: {cropped.size[0]}x{cropped.size[1]}, "
          f"ar={cropped.size[1] / cropped.size[0]:.4f}")


if __name__ == "__main__":
    main()
