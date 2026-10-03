#!/bin/bash
# Usage: render_band5.sh [page1 ...]  — worktree-local render of Band 5.
# Собственная копия pptx (/tmp/b5-check.pptx): в этом каталоге параллельно
# работает второй агент и пересобирает lec-05.pptx, поэтому конвертируем
# снимок, а не живой файл. PDF деки НЕ перезаписываем по той же причине.
set -e
REND=/home/harness/harness-projects/256/.worktrees/folder-288/session-cc366806-4c61a8f4/library/lectures/lec-05/rendered
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export HOME=/tmp/claude-999
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages:$PYTHONPATH
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
OUT=/tmp/claude-999/lec05-snap-b5
rm -rf "$OUT"; mkdir -p "$OUT" "$REND/snapshots"
cp "$REND/lec-05.pptx" /tmp/b5-check.pptx
timeout 280 $SOFF --headless -env:UserInstallation=file:///tmp/claude-999/loprofile_lec05b5 \
  --convert-to pdf --outdir "$OUT" /tmp/b5-check.pptx >/dev/null 2>&1
PAGES="$*"
python3 - "$OUT/b5-check.pdf" "$REND/snapshots" "$PAGES" <<'PY'
import sys, pymupdf
pdf, outdir, pages = sys.argv[1], sys.argv[2], sys.argv[3].split()
doc = pymupdf.open(pdf)
print("pdf pages:", len(doc))
idxs = [int(p)-1 for p in pages] if pages else range(len(doc))
for i in idxs:
    if 0 <= i < len(doc):
        doc[i].get_pixmap(dpi=150).save(f"{outdir}/slide-{i+1:02d}.png")
        print(f"rendered slide {i+1}")
PY
