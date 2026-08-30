#!/bin/bash
# Usage: render.sh [page1 page2 ...]  (no pages = all 40)
# Renders lec-04.pptx -> PDF (isolated profile) -> PNG @150dpi in snapshots/.
set -e
REND=/home/harness/harness-projects/256/.worktrees/folder-288/lesson4-498d0d8c/library/lectures/lec-04/rendered
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export HOME=/tmp/claude-999
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages:$PYTHONPATH
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
OUT=/tmp/claude-999/lec04-snap
rm -rf "$OUT"; mkdir -p "$OUT" "$REND/snapshots"
timeout 260 $SOFF --headless -env:UserInstallation=file:///tmp/claude-999/loprofile_lec04v4 \
  --convert-to pdf --outdir "$OUT" "$REND/lec-04.pptx" >/dev/null 2>&1
PAGES="$*"
python3 - "$OUT/lec-04.pdf" "$REND/snapshots" "$PAGES" <<'PY'
import sys, pymupdf
pdf, outdir, pages = sys.argv[1], sys.argv[2], sys.argv[3].split()
doc = pymupdf.open(pdf)
idxs = [int(p)-1 for p in pages] if pages else range(len(doc))
for i in idxs:
    if 0 <= i < len(doc):
        doc[i].get_pixmap(dpi=150).save(f"{outdir}/slide-{i+1:02d}.png")
        print(f"rendered slide {i+1}")
PY
cp "$OUT/lec-04.pdf" "$REND/lec-04.pdf"
echo "PDF copied to $REND/lec-04.pdf"
