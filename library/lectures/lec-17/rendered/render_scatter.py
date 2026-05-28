"""
render_scatter.py — generate the signature scatter plots as SVG → PNG.

ONE renderer, parameterised, used by 7 slides. Guarantees identical coordinate
system across s01/s03/s22/s23/s24/s28/s38 (MCP limitation #69-svg-fallback:
literal SVG + rsvg-convert = exact palette + reproducible).

Usage:
  python3 render_scatter.py        # renders all variants into assets/charts/
"""
import subprocess
from pathlib import Path

from scatter_coords import POINTS, points_in_batches, QUADRANTS

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "assets" / "charts"
OUT.mkdir(parents=True, exist_ok=True)

# Palette
DEEP = "#21295C"
MID = "#065A82"
LIGHT = "#1C7293"
TEAL = "#028090"
GOLD = "#F0AB00"
SURFACE = "#F4F7FA"
SLATE = "#6B7685"
WHITE = "#FFFFFF"

# Quadrant tint zones (CANON Phase 8a):
#   UR = closed-loop success (green) | UL = WARNING (gold) |
#   LR = regulatory-capped FILLED (blue) | LL = classical (grey)
UR_TINT = "#E4F1E8"   # closed-loop success = soft green-teal
UL_TINT = "#FCEFD6"   # WARNING (low fit + high autonomy) = soft gold
LL_TINT = "#ECEFF3"   # classical wins = soft grey
LR_TINT = "#E6EEF5"   # regulatory-capped (filled) = soft blue


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def svg_to_png(svg_text, name, w, h):
    svg_path = OUT / f"{name}.svg"
    png_path = OUT / f"{name}.png"
    svg_path.write_text(svg_text, encoding="utf-8")
    subprocess.run(
        ["rsvg-convert", "-w", str(w), "-h", str(h), "-f", "png",
         str(svg_path), "-o", str(png_path)],
        check=True,
    )
    return png_path


def build_svg(*, width=1200, height=820, max_batch=0, show_quadrant_labels=False,
              show_zones=False, highlight_ul=False, highlight_ur=False,
              highlight_lr=False, highlight_l13=False,
              highlight_l10=False, gradient_bg=False, point_labels=True,
              title=None, shift_arrows=False):
    """Construct the scatter SVG.

    Plot area is inset to leave room for axis labels.
    Axis: x left→right = AI fit; y bottom→top = autonomy.
    """
    # Plot box (inside the canvas)
    L, R = 150, width - 60
    T, B = 70 if title else 40, height - 80
    pw, ph = R - L, B - T

    def px(nx):
        return L + nx * pw

    def py(ny):
        return B - ny * ph   # invert: y=0 at bottom

    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="Liberation Sans, Arial, sans-serif">'
    )

    # Background
    if gradient_bg:
        parts.append(
            '<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0%" stop-color="{SURFACE}"/>'
            '<stop offset="100%" stop-color="#DCE7F0"/></linearGradient></defs>'
        )
        parts.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="url(#bg)"/>')
    else:
        parts.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="{WHITE}"/>')

    # Quadrant tint zones (s38 + optionally others)
    if show_zones:
        midx = px(0.5)
        midy = py(0.5)
        # UL
        parts.append(f'<rect x="{L}" y="{T}" width="{midx-L}" height="{midy-T}" fill="{UL_TINT}"/>')
        # UR
        parts.append(f'<rect x="{midx}" y="{T}" width="{R-midx}" height="{midy-T}" fill="{UR_TINT}"/>')
        # LL
        parts.append(f'<rect x="{L}" y="{midy}" width="{midx-L}" height="{B-midy}" fill="{LL_TINT}"/>')
        # LR
        parts.append(f'<rect x="{midx}" y="{midy}" width="{R-midx}" height="{B-midy}" fill="{LR_TINT}"/>')

    # Per-corner zone highlights (s28 warning + s25/s26/s27 per-cluster).
    midx = px(0.5)
    midy = py(0.5)
    # Upper-left WARNING zone (s28 main + s26 cluster) — gold dashed emphasis
    if highlight_ul:
        parts.append(
            f'<rect x="{L}" y="{T}" width="{midx-L}" height="{midy-T}" '
            f'fill="{UL_TINT}" stroke="{GOLD}" stroke-width="3.5" stroke-dasharray="10,6"/>'
        )
    # Upper-right closed-loop SUCCESS zone (s25 cluster) — teal solid emphasis
    if highlight_ur:
        parts.append(
            f'<rect x="{midx}" y="{T}" width="{R-midx}" height="{midy-T}" '
            f'fill="{UR_TINT}" stroke="{TEAL}" stroke-width="3.5"/>'
        )
    # Lower-right CAPPED zone (s27 cluster) — blue solid emphasis
    if highlight_lr:
        parts.append(
            f'<rect x="{midx}" y="{midy}" width="{R-midx}" height="{B-midy}" '
            f'fill="{LR_TINT}" stroke="{MID}" stroke-width="3.5"/>'
        )

    # Plot border
    parts.append(
        f'<rect x="{L}" y="{T}" width="{pw}" height="{ph}" fill="none" '
        f'stroke="{LIGHT}" stroke-width="1.5"/>'
    )
    # Mid grid lines (light)
    parts.append(f'<line x1="{px(0.5)}" y1="{T}" x2="{px(0.5)}" y2="{B}" stroke="{SLATE}" stroke-width="0.8" stroke-dasharray="4,4" opacity="0.5"/>')
    parts.append(f'<line x1="{L}" y1="{py(0.5)}" x2="{R}" y2="{py(0.5)}" stroke="{SLATE}" stroke-width="0.8" stroke-dasharray="4,4" opacity="0.5"/>')

    # Axis labels (INSIDE as scale markers + direction arrows)
    # X axis: bottom
    parts.append(f'<text x="{(L+R)/2}" y="{B+50}" font-size="22" font-weight="bold" fill="{DEEP}" text-anchor="middle">Применимость ИИ  →</text>')
    parts.append(f'<text x="{L+4}" y="{B+30}" font-size="15" fill="{SLATE}" text-anchor="start">детерминированный non-AI</text>')
    parts.append(f'<text x="{R-4}" y="{B+30}" font-size="15" fill="{SLATE}" text-anchor="end">полный AI</text>')
    # Y axis: left, rotated
    parts.append(f'<text x="{40}" y="{(T+B)/2}" font-size="22" font-weight="bold" fill="{DEEP}" text-anchor="middle" transform="rotate(-90 40 {(T+B)/2})">Автономия  L0 → L5  ↑</text>')
    parts.append(f'<text x="{75}" y="{B-4}" font-size="15" fill="{SLATE}" text-anchor="middle">L0</text>')
    parts.append(f'<text x="{75}" y="{T+16}" font-size="15" fill="{SLATE}" text-anchor="middle">L5</text>')

    # Quadrant labels (s03 keystone) — warning (UL) is gold
    if show_quadrant_labels:
        for key, (label, qx, qy, desc) in QUADRANTS.items():
            color = GOLD if key == "UL" else DEEP
            wt = "bold"
            parts.append(
                f'<text x="{px(qx)}" y="{py(qy)}" font-size="19" font-weight="{wt}" '
                f'fill="{color}" text-anchor="middle">{esc(label)}</text>'
            )
            parts.append(
                f'<text x="{px(qx)}" y="{py(qy)+24}" font-size="14" fill="{SLATE}" '
                f'text-anchor="middle">({esc(desc)})</text>'
            )

    # Shift arrows (s28) — warning zone is UPPER-LEFT (low fit + high autonomy).
    # Two escape directions from UL: ↓ снизить автономию (→LL); → повысить применимость (→UR).
    if shift_arrows:
        parts.append(f'<defs><marker id="arr" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="{TEAL}"/></marker></defs>')
        # down arrow (reduce autonomy) — sits inside upper-left zone, descends toward LL
        ax = px(0.18)
        parts.append(f'<line x1="{ax}" y1="{py(0.85)}" x2="{ax}" y2="{py(0.55)}" stroke="{TEAL}" stroke-width="3" marker-end="url(#arr)"/>')
        parts.append(f'<text x="{ax+10}" y="{py(0.70)}" font-size="14" font-weight="bold" fill="{TEAL}" text-anchor="start">снизить автономию ↓</text>')
        # right arrow (increase fit) — from upper-left toward upper-right
        ay = py(0.90)
        parts.append(f'<line x1="{px(0.30)}" y1="{ay}" x2="{px(0.60)}" y2="{ay}" stroke="{TEAL}" stroke-width="3" marker-end="url(#arr)"/>')
        parts.append(f'<text x="{px(0.32)}" y="{ay-8}" font-size="14" font-weight="bold" fill="{TEAL}" text-anchor="start">повысить применимость →</text>')

    # Points
    revealed = points_in_batches(max_batch) if max_batch > 0 else []
    for (key, x, y, color_raw, label, batch, kind) in revealed:
        color = color_raw if color_raw.startswith("#") else "#" + color_raw
        cx, cy = px(x), py(y)
        # Determine emphasis
        big = False
        ring = None
        if highlight_l13 and key.startswith("L13"):
            big = True
            ring = GOLD
        if highlight_l10 and key.startswith("L10"):
            big = True
            ring = GOLD
        r = 13 if big else 9
        # failure points: hollow with x-ish stroke
        if kind == "fail":
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{WHITE}" stroke="{color}" stroke-width="3"/>')
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.4}" fill="{color}"/>')
        elif kind == "near0":
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{WHITE}" stroke="{color}" stroke-width="3" stroke-dasharray="3,3"/>')
        else:
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>')
        if ring:
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r+5}" fill="none" stroke="{ring}" stroke-width="2.5"/>')
        # Label
        if point_labels:
            # offset label to avoid overlap with border + ring; flip side near right edge
            off = (r + 5 + 8) if ring else (r + 6)
            anchor = "start"
            lx = cx + off
            if x > 0.78:
                anchor = "end"
                lx = cx - off
            ly = cy + 5
            # nudge near-0 label up
            if kind == "near0":
                ly = cy - r - 6
                anchor = "middle"
                lx = cx
            parts.append(
                f'<text x="{lx}" y="{ly}" font-size="15" fill="{DEEP}" '
                f'text-anchor="{anchor}">{esc(label)}</text>'
            )

    # Title overlay (s01)
    if title:
        parts.append(f'<text x="{(L+R)/2}" y="{T-24}" font-size="24" font-weight="bold" fill="{DEEP}" text-anchor="middle">{esc(title)}</text>')

    # Legend (module colors) — INDUSTRY-NAMED groups (no lecture L-codes).
    if max_batch >= 3 or show_zones:
        ly0 = T + 8
        legend = [
            (DEEP, "Модуль 1 — основы + ранние отрасли"),
            (TEAL, "Модуль 2 — тяжёлая промышленность/оборона"),
            (GOLD, "Модуль 3 — инфраструктура/наука"),
        ]
        lx0 = L + 14
        # legend backdrop for readability over points
        parts.append(f'<rect x="{lx0-8}" y="{ly0-16}" width="332" height="76" rx="6" '
                     f'fill="{WHITE}" stroke="{LIGHT}" stroke-width="1" opacity="0.92"/>')
        for i, (c, txt) in enumerate(legend):
            yy = ly0 + i * 22
            parts.append(f'<rect x="{lx0}" y="{yy-10}" width="14" height="14" rx="3" fill="{c}"/>')
            parts.append(f'<text x="{lx0+20}" y="{yy+2}" font-size="13" fill="{DEEP}">{esc(txt)}</text>')

    parts.append("</svg>")
    return "\n".join(parts)


def main():
    # NAMES MAP TO v2 (37-slide) POSITIONS:
    #   s01 hero | s02 keystone | s20 batch1 | s21 batch2 | s22 batch3-full
    #   s23 cluster-UR (closed-loop) | s24 cluster-UL (open-env) | s25 cluster-LR (high-stakes)
    #   s26 empty-quadrants | s36 master-poster

    # s01 hero — full points, gradient bg, no point labels (clean), title overlay
    svg_to_png(build_svg(max_batch=3, gradient_bg=True, point_labels=False,
                         title="Шестнадцать отраслей — шестнадцать точек одной карты"),
               "s01-hero-scatter", 1280, 860)

    # s02 keystone — empty axes + quadrant labels, no points
    svg_to_png(build_svg(max_batch=0, show_quadrant_labels=True),
               "s02-keystone-quadrants", 1200, 820)

    # s20 — batch 1 (4 points)
    svg_to_png(build_svg(max_batch=1, point_labels=True),
               "s20-batch1", 1200, 820)

    # s21 — batch 1+2 (8+ points), highlight agro bimodal
    svg_to_png(build_svg(max_batch=2, point_labels=True, highlight_l10=True),
               "s21-batch2", 1200, 820)

    # s22 — full ~18 points, highlight logistics trio
    svg_to_png(build_svg(max_batch=3, point_labels=True, highlight_l13=True),
               "s22-batch3-full", 1280, 860)

    # s23 — closed-loop cluster (UPPER-RIGHT success) highlighted
    svg_to_png(build_svg(max_batch=3, highlight_ur=True, point_labels=True),
               "s23-cluster-ur", 1200, 820)

    # s24 — open-environment cluster (UPPER-LEFT warning) highlighted
    svg_to_png(build_svg(max_batch=3, highlight_ul=True, point_labels=True),
               "s24-cluster-ul", 1200, 820)

    # s25 — high-stakes cluster (LOWER-RIGHT regulatory-capped) highlighted
    svg_to_png(build_svg(max_batch=3, highlight_lr=True, point_labels=True),
               "s25-cluster-lr", 1200, 820)

    # s26 — empty quadrants, highlight UPPER-LEFT warning + shift arrows + points
    svg_to_png(build_svg(max_batch=3, highlight_ul=True, shift_arrows=True,
                         point_labels=True),
               "s26-empty-quadrants", 1200, 820)

    # s36 — A1 poster: full points + zones + labels
    svg_to_png(build_svg(width=1600, height=1000, max_batch=3, show_zones=True,
                         point_labels=True),
               "s36-master-poster", 1600, 1000)

    print("All scatter PNGs rendered to", OUT)


if __name__ == "__main__":
    main()
