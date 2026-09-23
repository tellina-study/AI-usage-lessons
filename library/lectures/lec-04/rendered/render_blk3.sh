#!/bin/bash
# Block-3 (round 6) local render: lec-04.pptx -> PDF -> PNG @150dpi in snapshots/r6b3/.
# Usage: render_blk3.sh [page1 page2 ...]   (no pages = all)
set -e
REND=/tmp/lec04-block3-testing/library/lectures/lec-04/rendered
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export HOME=/tmp/claude-blk3
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-maxim-levko-1be11ee3/.local/lib/python3.12/site-packages:$PYTHONPATH
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
OUT=/tmp/claude-blk3/lec04-snap
rm -rf "$OUT"; mkdir -p "$OUT" "$REND/snapshots/r6b3"
timeout 400 $SOFF --headless -env:UserInstallation=file:///tmp/claude-blk3/loprofile \
  --convert-to pdf --outdir "$OUT" "$REND/lec-04.pptx" >/dev/null 2>&1
PAGES="$*"
python3 - "$OUT/lec-04.pdf" "$REND/snapshots/r6b3" "$PAGES" <<'PY'
import sys, fitz
pdf, outdir, pages = sys.argv[1], sys.argv[2], sys.argv[3].split()
doc = fitz.open(pdf)
idxs = [int(p)-1 for p in pages] if pages else range(len(doc))
print("pdf pages:", len(doc))
for i in idxs:
    if 0 <= i < len(doc):
        doc[i].get_pixmap(dpi=150).save(f"{outdir}/slide-{i+1:02d}.png")
        print(f"rendered slide {i+1}")
PY
cp "$OUT/lec-04.pdf" "$REND/lec-04.pdf"
echo "PDF copied to $REND/lec-04.pdf"
