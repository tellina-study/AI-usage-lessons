#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Замер видимого слоя разделов 4-6 ПО СОБРАННОМУ PDF, а не по файлу кадра.

Плашки, столбцы, подписи схем и подвал лежат во фронтматтере; счёт по разделу
«## Видимый текст слайда» их не видит и занижает кадр вдвое. Зал видит
страницу PDF — её и считаем.

    python3 zamer_diyeta.py            # собрать разделы 4-6 и замерить
    python3 zamer_diyeta.py --no-build # только замер готового PDF
"""
import argparse
import re
import statistics
import subprocess
import sys
from pathlib import Path

import fitz
import yaml

import build_lec07 as B
from deckkit import render as rnd, report, slidefile

HERE = Path(__file__).resolve().parent
OUT = HERE / "diyeta"
MY = {"4", "5", "6"}


def my_ids():
    ids = []
    for f in slidefile.slide_files(B.SLIDES_DIR):
        fm = yaml.safe_load(re.match(r"^---\n(.*?)\n---", f.read_text(encoding="utf-8"), re.S).group(1))
        if str(fm.get("section") or "").split(".")[0].strip() in MY:
            ids.append(str(fm.get("id")))
    return ids


def build(ids, size=10):
    OUT.mkdir(exist_ok=True)
    pdfs = []
    for i in range(0, len(ids), size):
        part = ids[i:i + size]
        out = OUT / f"d{i // size + 1:02d}.pptx"
        if out.with_suffix(".pdf").exists():
            print(f"кусок {i // size + 1}: уже собран")
            pdfs.append(str(out.with_suffix(".pdf")))
            continue
        keep = report.snapshot()
        B.build(only=",".join(part), out=out)
        report.restore(keep)
        if rnd.render(out, OUT / f"snaps{i // size + 1:02d}", timeout=560):
            print(f"кусок {i // size + 1}: рендер не вышел")
            return None
        pdfs.append(str(out.with_suffix(".pdf")))
        print(f"кусок {i // size + 1}: {len(part)} кадров")
    final = OUT / "diyeta.pdf"
    r = subprocess.run(["bash", "-lc",
                        ". /home/harness/.local/lo-portable-env.sh && "
                        f"pdfunite {' '.join(pdfs)} '{final.absolute()}'"],
                       timeout=180, capture_output=True, text=True)
    if r.returncode:
        print(f"склейка: {r.stderr[-300:]}")
        return None
    return final


def measure(pdf, ids):
    d = fitz.open(pdf)
    rows = []
    for n, p in enumerate(d):
        w = len(p.get_text().split())
        rows.append((ids[n] if n < len(ids) else f"?{n}", w))
    rows.sort(key=lambda r: -r[1])
    print(f"\n{'кадр':<7} {'слов':>5}")
    for i, w in rows:
        print(f"{i:<7} {w:>5}{' ⚠' if w > 140 else ''}")
    v = [w for _, w in rows]
    print(f"\nПО PDF: страниц {len(v)} · медиана {statistics.median(v):.0f}"
          f" · максимум {max(v)} · тяжелее 140: {sum(1 for x in v if x > 140)}"
          f" · тяжелее 200: {sum(1 for x in v if x > 200)}")
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-build", action="store_true")
    a = ap.parse_args()
    ids = my_ids()
    print(f"кадров разделов 4-6: {len(ids)}")
    pdf = OUT / "diyeta.pdf"
    if not a.no_build:
        pdf = build(ids)
        if not pdf:
            return 1
    measure(pdf, ids)
    return 0


sys.exit(main())
