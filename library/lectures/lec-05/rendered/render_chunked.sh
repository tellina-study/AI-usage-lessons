#!/bin/bash
# Запасной рендер: та же дека, но почанково.
#
# Зачем: на нагруженной машине LibreOffice не вытягивает все 56 слайдов за один
# заход — процесс уходит в непрерываемое ожидание на подкачке и погибает по
# таймауту, не написав ни страницы и ни слова в лог (notes/mcp-limitations.md
# [#212-1]). Части по 14 слайдов конвертируются за ~40 секунд каждая.
#
# Usage: render_chunked.sh [размер_части]     (по умолчанию 14)
# На выходе: lec-05.pdf (56 страниц) + snapshots/slide-01..56.png @150dpi.
set -e
REND=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
CHUNK=${1:-14}
export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export HOME=/tmp/claude-999
export PYTHONPATH=/home/harness/harness-control-data/accounts/256/claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages:$PYTHONPATH
SOFF=/home/harness/.local/libreoffice-portable/program/soffice
CH=/tmp/lec05-chunks

# Ни одного живого soffice: два процесса на одном профиле встают намертво ([#212-2]).
# (зомби `[soffice.bin] <defunct>` безвреден и в счёт не идёт — отсюда фильтр по состоянию)
if [ "$(ps -o stat= -C soffice.bin 2>/dev/null | grep -vc '^Z')" != "0" ]; then
  echo "ОТКАЗ: soffice уже запущен. Дождитесь или снимите его по PID, потом повторите." >&2; exit 1
fi
rm -rf "$CH"; mkdir -p "$CH" "$REND/snapshots"
LEC05_CHUNK_DIR="$CH" python3 "$REND/build_chunks.py" "$CHUNK"

for f in "$CH"/part-*.pptx; do
  i=$(basename "$f" .pptx); rm -rf "/tmp/lo-prof-$i"
  timeout 600 $SOFF --headless -env:UserInstallation="file:///tmp/lo-prof-$i" \
    --convert-to pdf --outdir "$CH" "$f" >/dev/null 2>&1
  [ -f "$CH/$i.pdf" ] || { echo "ОТКАЗ: $i не сконвертировался" >&2; exit 1; }
  echo "готово: $i"
done

python3 - "$CH" "$REND" <<'PY'
import sys, glob, os, pymupdf
ch, rend = sys.argv[1], sys.argv[2]
out = pymupdf.open()
for f in sorted(glob.glob(os.path.join(ch, "part-*.pdf"))):
    d = pymupdf.open(f); out.insert_pdf(d); d.close()
out.save(os.path.join(rend, "lec-05.pdf")); out.close()
d = pymupdf.open(os.path.join(rend, "lec-05.pdf"))
for i in range(d.page_count):
    d[i].get_pixmap(dpi=150).save(os.path.join(rend, "snapshots", f"slide-{i+1:02d}.png"))
print(f"lec-05.pdf — {d.page_count} страниц; снимков — {d.page_count}")
PY
