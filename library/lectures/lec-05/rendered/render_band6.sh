#!/bin/bash
# Usage: render_band6.sh [page1 page2 ...]  — рендер ТОЛЬКО полосы 6.
# Собственный временный pptx (/tmp/b6-check.pptx) и собственный каталог
# снимков (/tmp/b6-png): в rendered/ параллельно работает другой агент, и ни
# lec-05.pptx, ни snapshots/ трогать нельзя.
set -e
REND=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export HOME=/tmp/claude-999
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages:$PYTHONPATH
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
OUT=/tmp/claude-999/lec05-snap-b6
PNG=/tmp/b6-png
rm -rf "$OUT"; mkdir -p "$OUT" "$PNG"
python3 "$REND/build_band6.py"
timeout 280 $SOFF --headless -env:UserInstallation=file:///tmp/claude-999/loprofile_lec05b6 \
  --convert-to pdf --outdir "$OUT" /tmp/b6-check.pptx >/dev/null 2>&1
PAGES="$*"
python3 - "$OUT/b6-check.pdf" "$PNG" "$PAGES" <<'PY'
import sys, pymupdf
pdf, outdir, pages = sys.argv[1], sys.argv[2], sys.argv[3].split()
doc = pymupdf.open(pdf)
print("pdf pages:", len(doc))
idxs = [int(p)-1 for p in pages] if pages else range(len(doc))
for i in idxs:
    if 0 <= i < len(doc):
        doc[i].get_pixmap(dpi=150).save(f"{outdir}/b6-{i+1:02d}.png")
        print(f"rendered {i+1}")
PY
