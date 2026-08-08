#!/bin/bash
# Usage: recolor.sh <icon-name> <hexcolor-no-hash> <size-px>
# Reads src/<icon-name>.svg, recolors stroke=currentColor -> #HEX, writes rendered/<icon-name>-<hex>-<size>.png
set -e
source /tmp/claude-999/render-env.sh
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NAME="$1"; HEX="$2"; SIZE="${3:-96}"
SRC="$DIR/src/$NAME.svg"
OUT="$DIR/rendered/${NAME}-${HEX}-${SIZE}.png"
TMP="/tmp/claude-999/scratch-${NAME}-${HEX}.svg"
mkdir -p /tmp/claude-999/scratch 2>/dev/null || true
sed "s/currentColor/#${HEX}/g" "$SRC" > "$TMP"
rsvg-convert -w "$SIZE" -h "$SIZE" -f png "$TMP" -o "$OUT"
echo "$OUT"
