#!/bin/bash
# Generate the small set of icon-color-size combos build_sem03.py needs that
# are NOT already present in sem-02's shared icon library (SLATE #6B7685 for
# "muted/no" states, and zap in the dark-gold GOLD_DARK #8A6200 accent).
# Recolor pattern per notes/mcp-limitations.md lesson (sem-02 P1 fix): only
# touch stroke="..." and currentColor tokens, NEVER fill="..." — Lucide
# icons use fill="none" on the root <svg>, and blanket-replacing fill breaks
# outline icons (smile/compass circles filled solid instead of outlined).
set -e
source /tmp/claude-999/render-env.sh
cd "$(dirname "$0")"
SVG_DIR="svg"
OUT_DIR="rendered"
mkdir -p "$OUT_DIR"

# name:hex pairs needed beyond what sem-02 already rendered
NEEDED=(
  "hash:6B7685"
  "help-circle:6B7685"
  "x-circle:6B7685"
  "zap:8A6200"
)
SIZES=(64 72 96)

for pair in "${NEEDED[@]}"; do
  name="${pair%%:*}"
  hexval="${pair##*:}"
  svg_src="$SVG_DIR/${name}.svg"
  if [ ! -f "$svg_src" ]; then
    echo "MISSING SVG: $svg_src" >&2
    continue
  fi
  tmp_svg="/tmp/icon-${name}-${hexval}.svg"
  sed -E "s/stroke=\"currentColor\"/stroke=\"#${hexval}\"/g; s/stroke=\"#[0-9A-Fa-f]{3,6}\"/stroke=\"#${hexval}\"/g" \
    "$svg_src" > "$tmp_svg"
  for sz in "${SIZES[@]}"; do
    out_png="$OUT_DIR/${name}-${hexval}-${sz}.png"
    rsvg-convert -w "$sz" -h "$sz" -f png "$tmp_svg" -o "$out_png"
    echo "Wrote $out_png"
  done
done
