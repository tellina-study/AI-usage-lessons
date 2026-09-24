#!/usr/bin/env bash
# tools/presentation-build/pptx_to_png.sh
#
# Converts a .pptx to a PDF (headless LibreOffice) and then rasterizes it to per-slide PNGs
# (pdftoppm). Sources render-env.sh internally -- callers do not need to (and should not need
# to) source it themselves.
#
# Usage:
#   tools/presentation-build/pptx_to_png.sh <input.pptx> <output-dir> [dpi=150] [first-page] [last-page]
#
# Output: <output-dir>/<basename>.pdf and <output-dir>/<basename>-s-NN.png (pdftoppm's own
# numbering; NN is zero-padded to the page count's width).
#
# Process ordering note (notes/mcp-limitations.md #sem03-render-1): if you are BUILDING the
# .pptx with a python-pptx script first, do that as a separate, earlier step/Bash-tool-call --
# don't chain "build .pptx" and "call this script" inside one shell where you've already sourced
# render-env.sh for some other reason. This script itself is safe either way (render-env.sh
# preserves PYTHONPATH), but keeping build and convert as two separate calls stays the simplest
# mental model and matches how every prior lecture/seminar render actually happened.

set -euo pipefail

usage() {
  echo "Usage: $0 <input.pptx> <output-dir> [dpi=150] [first-page] [last-page]" >&2
  exit 1
}

[ $# -ge 2 ] || usage
IN_PPTX="$1"
OUT_DIR="$2"
DPI="${3:-150}"
FIRST_PAGE="${4:-}"
LAST_PAGE="${5:-}"

[ -f "$IN_PPTX" ] || { echo "[pptx_to_png] ERROR: input not found: $IN_PPTX" >&2; exit 1; }
mkdir -p "$OUT_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$SCRIPT_DIR/render-env.sh"

command -v soffice >/dev/null 2>&1 || { echo "[pptx_to_png] ERROR: soffice not on PATH after sourcing render-env.sh -- run tools/presentation-build/render-bootstrap.sh first." >&2; exit 1; }
command -v pdftoppm >/dev/null 2>&1 || { echo "[pptx_to_png] ERROR: pdftoppm not on PATH after sourcing render-env.sh -- run tools/presentation-build/render-bootstrap.sh first." >&2; exit 1; }

BASENAME="$(basename "$IN_PPTX" .pptx)"

# Isolated LibreOffice profile dir, unique per invocation -- avoids colliding with a real home
# directory or with a parallel conversion in another session, WITHOUT touching $HOME (see
# render-env.sh's own header for why that distinction matters here).
PROFILE_DIR="$(mktemp -d -t render-lo-profile-XXXXXX)"
trap 'rm -rf "$PROFILE_DIR"' EXIT

echo "[pptx_to_png] converting $IN_PPTX -> $OUT_DIR/$BASENAME.pdf ..." >&2
soffice --headless --norestore -env:UserInstallation="file://$PROFILE_DIR/lo_profile" \
  --convert-to pdf --outdir "$OUT_DIR" "$IN_PPTX" >&2

PDF_PATH="$OUT_DIR/$BASENAME.pdf"
[ -f "$PDF_PATH" ] || { echo "[pptx_to_png] ERROR: expected PDF was not produced: $PDF_PATH" >&2; exit 1; }

PAGE_ARGS=()
[ -n "$FIRST_PAGE" ] && PAGE_ARGS+=(-f "$FIRST_PAGE")
[ -n "$LAST_PAGE" ] && PAGE_ARGS+=(-l "$LAST_PAGE")

echo "[pptx_to_png] rasterizing -> $OUT_DIR/$BASENAME-s-*.png at ${DPI}dpi ..." >&2
pdftoppm -png -r "$DPI" "${PAGE_ARGS[@]}" "$PDF_PATH" "$OUT_DIR/$BASENAME-s"

COUNT=$(ls "$OUT_DIR/$BASENAME-s"*.png 2>/dev/null | wc -l)
if [ "$COUNT" -eq 0 ]; then
  echo "[pptx_to_png] ERROR: pdftoppm produced 0 PNGs -- conversion did not actually work." >&2
  exit 1
fi
echo "[pptx_to_png] done: $COUNT PNG(s) written to $OUT_DIR (PDF: $PDF_PATH)" >&2
