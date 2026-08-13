#!/bin/bash
# Generate full icon-color-size matrix for sem-04 build script.
# Recolor pattern per notes/mcp-limitations.md lesson (sem-02 P1 fix): only
# touch stroke="..." and currentColor tokens, NEVER fill="..." — Lucide
# icons use fill="none" on the root <svg>, and blanket-replacing fill breaks
# outline icons (circles filled solid instead of outlined).
set -e
source /tmp/claude-999/render-env.sh
cd "$(dirname "$0")"
SVG_DIR="svg"
OUT_DIR="rendered"
mkdir -p "$OUT_DIR"

COLORS=(21295C 065A82 1C7293 028090 F0AB00 FFFFFF 6B7685 8A6200)
SIZES=(64 72 96)

count=0
for svg_src in "$SVG_DIR"/*.svg; do
  name=$(basename "$svg_src" .svg)
  for hexval in "${COLORS[@]}"; do
    tmp_svg="/tmp/icon-sem04-${name}-${hexval}.svg"
    sed -E "s/stroke=\"currentColor\"/stroke=\"#${hexval}\"/g; s/stroke=\"#[0-9A-Fa-f]{3,6}\"/stroke=\"#${hexval}\"/g" \
      "$svg_src" > "$tmp_svg"
    for sz in "${SIZES[@]}"; do
      out_png="$OUT_DIR/${name}-${hexval}-${sz}.png"
      rsvg-convert -w "$sz" -h "$sz" -f png "$tmp_svg" -o "$out_png"
      count=$((count+1))
    done
  done
done
echo "Generated $count icon PNGs"
