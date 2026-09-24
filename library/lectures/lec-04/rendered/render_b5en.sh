#!/bin/bash
# Block-5 EN-sync: rebuild lec-04-en.pptx from source and snapshot PNGs.
# Usage: render_b5en.sh [page1 page2 ...]   (no pages = all)
set -e
REND=/tmp/lec04-en-block5/library/lectures/lec-04/rendered
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export HOME=/tmp/claude-b5
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages:$PYTHONPATH
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
OUT=/tmp/claude-b5/lec04-en-snap
cd "$REND"
python3 build_lec04_en.py
rm -rf "$OUT"; mkdir -p "$OUT" "$REND/snapshots-en-b5"
timeout 400 $SOFF --headless -env:UserInstallation=file:///tmp/claude-b5/loprofile_en \
  --convert-to pdf --outdir "$OUT" "$REND/lec-04-en.pptx" >/dev/null 2>&1
PAGES="$*"
python3 - "$OUT/lec-04-en.pdf" "$REND/snapshots-en-b5" "$PAGES" <<'PY'
import sys, pymupdf
pdf, outdir, pages = sys.argv[1], sys.argv[2], sys.argv[3].split()
doc = pymupdf.open(pdf)
idxs = [int(p)-1 for p in pages] if pages else range(len(doc))
for i in idxs:
    if 0 <= i < len(doc):
        doc[i].get_pixmap(dpi=110).save(f"{outdir}/en-{i+1:02d}.png")
        print(f"rendered EN slide {i+1}")
PY
cp "$OUT/lec-04-en.pdf" "$REND/lec-04-en.pdf"
