#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Рендер деки ЧАСТЯМИ: по куску кадров за вызов, потом склейка.

`soffice --convert-to pdf` на всей деке дважды вешал машину на часы
(`notes/mcp-limitations.md` [#223-6], [#229-2]) — не по времени, а по памяти:
процесс упирается в `memory.high` и дросселируется бесконечно. Кусок кадров
в ту же память укладывается, поэтому рендер здесь идёт частями, каждая со
своим таймаутом, а PDF склеивается `pdfunite`.

Склейка идёт по ПОРЯДКУ КАДРОВ деки, а не по именам файлов: порядок задаёт
`slidefile.slide_files`, он же порядок сборки, и брать его надо оттуда.

    python3 render_parts.py                 # вся дека частями по 20
    python3 render_parts.py --size 10       # кусок мельче
    python3 render_parts.py --pdf out.pdf   # куда положить склейку
"""
import argparse
import subprocess
import sys
from pathlib import Path

import build_lec07 as B
from deckkit import render as rnd, report, slidefile

HERE = Path(__file__).resolve().parent
PARTS = HERE / "parts"


def chunks(ids, n):
    return [ids[i:i + n] for i in range(0, len(ids), n)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", type=int, default=20)
    ap.add_argument("--pdf", default=str(HERE / "lec-07-karkas.pdf"))
    ap.add_argument("--timeout", type=int, default=560)
    a = ap.parse_args()
    PARTS.mkdir(exist_ok=True)
    ids = [f.name.split("-")[0]
           for f in slidefile.slide_files(B.SLIDES_DIR)]
    pdfs = []
    for i, part in enumerate(chunks(ids, a.size), 1):
        out = PARTS / f"part{i:02d}.pptx"
        keep = report.snapshot()
        B.build(only=",".join(part), out=out)
        report.restore(keep)
        if rnd.render(out, PARTS / f"snaps{i:02d}", timeout=a.timeout):
            print(f"часть {i}: рендер не вышел")
            return 1
        pdfs.append(str(out.with_suffix(".pdf")))
        print(f"часть {i}: {len(part)} кадров готово")
    r = subprocess.run(["bash", "-lc",
                        ". /home/harness/.local/lo-portable-env.sh && "
                        f"pdfunite {' '.join(pdfs)} {a.pdf}"],
                       timeout=180, capture_output=True, text=True)
    if r.returncode:
        print(f"склейка: код {r.returncode}\n{r.stderr[-400:]}")
        return 1
    print(f"склеено: {a.pdf}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
