#!/bin/bash
# Usage: render_en.sh [page1 page2 ...]  (no pages = all slides in current build)
# Renders lec-06-en.pptx -> PDF (isolated profile) -> PNG @150dpi in snapshots/.
set -e
REND=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-kulabulan-1a6d2839/.local/lib/python3.12/site-packages:$PYTHONPATH
export HOME=/tmp/claude-999
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
OUT=/tmp/claude-999/lec06-en-snap-$$
rm -rf "$OUT"; mkdir -p "$OUT" "$REND/snapshots"
timeout 900 $SOFF --headless -env:UserInstallation=file:///tmp/claude-999/loprofile_lec06en-$$ \
  --convert-to pdf --outdir "$OUT" "$REND/lec-06-en.pptx" >/dev/null 2>&1
PAGES="$*"
python3 - "$OUT/lec-06-en.pdf" "$REND/snapshots" "$PAGES" <<'PY'
import sys, pymupdf
pdf, outdir, pages = sys.argv[1], sys.argv[2], sys.argv[3].split()
doc = pymupdf.open(pdf)
idxs = [int(p)-1 for p in pages] if pages else range(len(doc))
for i in idxs:
    if 0 <= i < len(doc):
        doc[i].get_pixmap(dpi=150).save(f"{outdir}/en-slide-{i+1:02d}.png")
        print(f"rendered slide {i+1}")
PY
cp "$OUT/lec-06-en.pdf" "$REND/lec-06-en.pdf"
echo "PDF copied to $REND/lec-06-en.pdf"
