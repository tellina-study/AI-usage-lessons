#!/bin/bash
# Usage: render.sh [page1 page2 ...]  (no pages = all slides in current build)
# Renders lec-05.pptx -> PDF (isolated profile) -> PNG @150dpi in snapshots/.
set -e
REND=/home/harness/harness-projects/256/.worktrees/folder-288/pldlc-lesson5-c5cc1586/library/lectures/lec-05/rendered
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export HOME=/tmp/claude-999
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages:$PYTHONPATH
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
OUT=/tmp/claude-999/lec05-snap
rm -rf "$OUT"; mkdir -p "$OUT" "$REND/snapshots"
timeout 260 $SOFF --headless -env:UserInstallation=file:///tmp/claude-999/loprofile_lec05 \
  --convert-to pdf --outdir "$OUT" "$REND/lec-05.pptx" >/dev/null 2>&1
PAGES="$*"
python3 - "$OUT/lec-05.pdf" "$REND/snapshots" "$PAGES" <<'PY'
import sys, pymupdf
pdf, outdir, pages = sys.argv[1], sys.argv[2], sys.argv[3].split()
doc = pymupdf.open(pdf)
idxs = [int(p)-1 for p in pages] if pages else range(len(doc))
for i in idxs:
    if 0 <= i < len(doc):
        doc[i].get_pixmap(dpi=150).save(f"{outdir}/slide-{i+1:02d}.png")
        print(f"rendered slide {i+1}")
PY
cp "$OUT/lec-05.pdf" "$REND/lec-05.pdf"
echo "PDF copied to $REND/lec-05.pdf"
