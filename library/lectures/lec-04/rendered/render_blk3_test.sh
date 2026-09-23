#!/bin/bash
# Fast 3-slide iteration render for round-6 block 3.
# Usage: render_blk3_test.sh <iter-tag>   → snapshots/r6b3/<tag>-{1,2,3}.png
set -e
REND=/tmp/lec04-block3-testing/library/lectures/lec-04/rendered
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export HOME=/tmp/claude-blk3
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-maxim-levko-1be11ee3/.local/lib/python3.12/site-packages:$PYTHONPATH
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
TAG=${1:-iter}
OUT=/tmp/claude-blk3/blk3-test
mkdir -p "$OUT" "$REND/snapshots/r6b3"
cd "$REND" && python3 build_blk3_test.py
rm -f "$OUT/_test_blk3.pdf"
timeout 200 $SOFF --headless -env:UserInstallation=file:///tmp/claude-blk3/loprofile_test \
  --convert-to pdf --outdir "$OUT" "$REND/_test_blk3.pptx" >/dev/null 2>&1
python3 - "$OUT/_test_blk3.pdf" "$REND/snapshots/r6b3" "$TAG" <<'PY'
import sys, fitz
pdf, outdir, tag = sys.argv[1], sys.argv[2], sys.argv[3]
doc = fitz.open(pdf)
for i in range(len(doc)):
    doc[i].get_pixmap(dpi=120).save(f"{outdir}/{tag}-{i+1}.png")
    print(f"rendered {outdir}/{tag}-{i+1}.png")
PY
