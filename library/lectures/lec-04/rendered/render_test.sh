#!/bin/bash
# Usage: render_test.sh <name>  (renders _test_<name>.pptx -> snapshots/r5/<name>.png)
set -e
REND=/home/harness/harness-projects/256/.worktrees/folder-288/lesson4-de299d-0fac50ac/library/lectures/lec-04/rendered
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export HOME=/tmp/claude-999
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages:$PYTHONPATH
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
NAME=$1
OUT=/tmp/claude-999/lec04-test-snap
mkdir -p "$OUT" "$REND/snapshots/r5"
timeout 120 $SOFF --headless -env:UserInstallation=file:///tmp/claude-999/loprofile_lec04test \
  --convert-to pdf --outdir "$OUT" "$REND/_test_${NAME}.pptx" >/dev/null 2>&1
python3 - "$OUT/_test_${NAME}.pdf" "$REND/snapshots/r5/${NAME}.png" <<'PY'
import sys, pymupdf
pdf, out = sys.argv[1], sys.argv[2]
doc = pymupdf.open(pdf)
doc[0].get_pixmap(dpi=150).save(out)
print("rendered", out)
PY
