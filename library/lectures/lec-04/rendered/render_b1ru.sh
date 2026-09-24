#!/bin/bash
# EN-sync block 1 helper: render the CURRENT RU deck pages to PNG for reference.
# Usage: render_b1ru.sh [page1 page2 ...]   (no pages = all)
set -e
REND=/tmp/lec04-en-block1/library/lectures/lec-04/rendered
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export HOME=/tmp/claude-999
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages:$PYTHONPATH
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
OUT=/tmp/claude-999/lec04-b1ru
rm -rf "$OUT"; mkdir -p "$OUT" "$REND/snapshots-ru"
timeout 300 $SOFF --headless -env:UserInstallation=file:///tmp/claude-999/loprofile_lec04b1 \
  --convert-to pdf --outdir "$OUT" "$REND/lec-04.pptx" >/dev/null 2>&1
PAGES="$*"
python3 - "$OUT/lec-04.pdf" "$REND/snapshots-ru" "$PAGES" <<'PY'
import sys, pymupdf
pdf, outdir, pages = sys.argv[1], sys.argv[2], sys.argv[3].split()
doc = pymupdf.open(pdf)
idxs = [int(p)-1 for p in pages] if pages else range(len(doc))
for i in idxs:
    if 0 <= i < len(doc):
        doc[i].get_pixmap(dpi=110).save(f"{outdir}/ru-{i+1:02d}.png")
        print(f"rendered RU slide {i+1}")
PY
