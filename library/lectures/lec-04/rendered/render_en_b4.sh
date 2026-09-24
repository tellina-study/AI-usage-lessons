#!/bin/bash
# EN-sync block 4 local render helper — same pipeline as render_b4.sh, but for
# the EN deck. Usage: render_en_b4.sh [page1 page2 ...]   (no pages = all)
set -e
REND="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export HOME=/tmp/claude-999
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages:$PYTHONPATH
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
OUT=/tmp/claude-999/lec04-enb4-snap
rm -rf "$OUT"; mkdir -p "$OUT" "$REND/snapshots/en-b4"
timeout 300 $SOFF --headless -env:UserInstallation=file:///tmp/claude-999/loprofile_lec04enb4 \
  --convert-to pdf --outdir "$OUT" "$REND/lec-04-en.pptx" >/dev/null 2>&1
python3 - "$OUT/lec-04-en.pdf" "$REND/snapshots/en-b4" "$*" <<'PY'
import sys, pymupdf
pdf, outdir, pages = sys.argv[1], sys.argv[2], sys.argv[3].split()
doc = pymupdf.open(pdf)
print("pages in pdf:", len(doc))
idxs = [int(p)-1 for p in pages] if pages else range(len(doc))
for i in idxs:
    if 0 <= i < len(doc):
        doc[i].get_pixmap(dpi=110).save(f"{outdir}/slide-{i+1:02d}.png")
        print(f"rendered slide {i+1}")
PY
cp "$OUT/lec-04-en.pdf" "$REND/lec-04-en.pdf"
echo "PDF copied to $REND/lec-04-en.pdf"
