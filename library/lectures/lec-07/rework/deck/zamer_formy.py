#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Замер кадров, которым меняют ФОРМУ, — по собранному PDF. Issue #229.

Зачем отдельный прогон, когда рядом есть `zamer_diyeta.py` и `zamer_pdf.py`.
Тот первый считает разделы 4–6 целиком и к списку кадров не сводится; второй
смотрит кегли и коробки, но не слова. Перевод кадра на новую форму надо
принимать ОДНИМ числом на кадр и до/после: слов по PDF, предел 140, кегль
ниже пола, блокирующие. Иначе «форма снимает слова» остаётся обещанием —
а замер по файлу кадра тут не годится вовсе, потому что форма переносит
текст между фронтматтером и рисунком, и счёт по «## Видимый текст слайда»
этого не видит.

    python3 zamer_formy.py s45 s49c          # замерить эти кадры
    python3 zamer_formy.py --out до s45 s49c # сохранить замер под именем
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))

import build_lec07 as B                       # noqa: E402
from deckkit import pdfmeasure as pm, render as rnd, report  # noqa: E402

OUT = HERE / "zamer-formy"
FLOOR = 12.0


def measure(sids):
    OUT.mkdir(exist_ok=True)
    report.reset()
    pptx = OUT / "f.pptx"
    B.build(only=",".join(sids), out=pptx)
    blocking = list(report.blocking())
    other = list(report.other())
    if rnd.render(pptx, OUT / "snaps", timeout=560):
        print("рендер не вышел")
        return None
    pdf = pptx.with_suffix(".pdf")
    doc = fitz.open(pdf)
    words = [len(p.get_text().split()) for p in doc]
    # Кегли — тем же измерителем собранного PDF, которым меряет вся сборка.
    # `size_hist` отдаёт ПАРУ: счётчик по всей деке и по кадрам. Берём
    # первый — доля знаков ниже пола считается по всему, что видит зал.
    hist, by_page = pm.size_hist(pdf)
    low, tot, share = pm.below(hist, FLOOR)
    return {"кадры": sids, "слов": words,
            "блокирующих": blocking, "прочих": len(other),
            "знаков ниже 12": low, "знаков всего": tot,
            "доля ниже 12": round(share, 4),
            "кегли по кадрам": {str(k): sorted(v) for k, v in by_page.items()}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sids", nargs="+")
    ap.add_argument("--out")
    a = ap.parse_args()
    r = measure(a.sids)
    if not r:
        sys.exit(1)
    for sid, w in zip(r["кадры"], r["слов"]):
        print(f"{sid:<7} слов по PDF {w:>4}{'  ⚠ ПРЕДЕЛ 140' if w > 140 else ''}")
    print(f"блокирующих {len(r['блокирующих'])} · прочих {r['прочих']} "
          f"· знаков ниже {FLOOR:.0f} пт {r['знаков ниже 12']} из "
          f"{r['знаков всего']} ({100 * r['доля ниже 12']:.1f}%)")
    for b in r["блокирующих"]:
        print("  " + b)
    if a.out:
        (OUT / f"{a.out}.json").write_text(
            json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
