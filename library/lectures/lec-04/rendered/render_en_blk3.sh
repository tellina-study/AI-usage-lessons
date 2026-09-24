#!/bin/bash
# EN-Sync Block 3 (issue #172 / #162) local render.
# Usage: render_en_blk3.sh <ru|en|blk3> [page1 page2 ...]   (no pages = all)
set -e
MODE="${1:-blk3}"; shift || true
REND=/tmp/lec04-en-block3/library/lectures/lec-04/rendered
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export HOME=/tmp/claude-enb3
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-maxim-levko-1be11ee3/.local/lib/python3.12/site-packages:$PYTHONPATH
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
case "$MODE" in
  ru)   SRC="$REND/lec-04.pptx";           SNAP="$REND/snapshots/en-b3-ru"; PDF=lec-04.pdf ;;
  en)   SRC="$REND/lec-04-en.pptx";        SNAP="$REND/snapshots/en-b3";    PDF=lec-04-en.pdf ;;
  blk3) SRC="$REND/lec-04-en-blk3.pptx";   SNAP="$REND/snapshots/en-b3";    PDF=lec-04-en-blk3.pdf ;;
  *) echo "usage: render_en_blk3.sh <ru|en|blk3> [pages...]"; exit 1 ;;
esac
OUT=/tmp/claude-enb3/snap-$MODE
rm -rf "$OUT"; mkdir -p "$OUT" "$SNAP"
timeout 500 $SOFF --headless -env:UserInstallation=file:///tmp/claude-enb3/loprofile \
  --convert-to pdf --outdir "$OUT" "$SRC" >/dev/null 2>&1
PAGES="$*"
python3 - "$OUT/$PDF" "$SNAP" "$PAGES" <<'PY'
import sys, fitz
pdf, outdir, pages = sys.argv[1], sys.argv[2], sys.argv[3].split()
doc = fitz.open(pdf)
idxs = [int(p)-1 for p in pages] if pages else range(len(doc))
print("pdf pages:", len(doc))
for i in idxs:
    if 0 <= i < len(doc):
        doc[i].get_pixmap(dpi=140).save(f"{outdir}/slide-{i+1:02d}.png")
        print(f"rendered slide {i+1}")
PY
echo "snapshots -> $SNAP"
