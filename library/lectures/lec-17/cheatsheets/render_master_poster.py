"""
render_master_poster.py — A1 master-map cheat-sheet (Карточка #4).

Reuses the IDENTICAL coordinate system from
library/lectures/lec-17/rendered/scatter_coords.py (zero drift with deck s38).
On top of the base scatter it adds, for the printed A1 poster:
  - quadrant color zones + zone labels (closed-loop / regulator-capped /
    classical-wins / warning)
  - per-point one-line callout (главный провал / успех отрасли)
  - module-color legend
  - title + footer (применение плаката)

Output: cheatsheets/assets/master-poster-a1.png  (high-res for print, ~200dpi).

MCP limitation #69-svg-fallback: literal SVG + rsvg-convert = exact Ocean
palette + reproducible bit-for-bit.
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DECK_RENDER = HERE.parent / "rendered"
sys.path.insert(0, str(DECK_RENDER))

from scatter_coords import POINTS, QUADRANTS  # noqa: E402  (identical coords)

OUT = HERE / "assets"
OUT.mkdir(parents=True, exist_ok=True)

# --- Ocean palette (LOCKED v3) ---
DEEP = "#21295C"
MID = "#065A82"
LIGHT = "#1C7293"
TEAL = "#028090"
GOLD = "#F0AB00"
SURFACE = "#F4F7FA"
SLATE = "#6B7685"
WHITE = "#FFFFFF"

# Quadrant tint zones (CANON Phase 8a — identical to deck render_scatter.py):
#   UR = closed-loop success (green) | UL = WARNING (gold) |
#   LR = regulatory-capped FILLED (blue) | LL = classical (grey)
UR_TINT = "#E4F1E8"   # closed-loop success = soft green-teal
UL_TINT = "#FCEFD6"   # WARNING (low fit + high autonomy) = soft gold
LL_TINT = "#ECEFF3"   # classical wins = soft grey
LR_TINT = "#E6EEF5"   # regulatory-capped (filled) = soft blue

# Per-point callout (главный провал / успех отрасли) — RU, baseline inline.
# Keyed by scatter_coords key. Brand allowlist: Symbotic, AlphaFold, Galactica,
# Monarch, See & Spray, Copilot, Stripe Radar, Waymo, Cruise — оставлены латиницей.
CALLOUTS = {
    "L4_SE":        "Copilot: автодополнение ✓; штучная архитектура ✗",
    "L5_fin":       "Stripe Radar: фрод-скоринг под надзором ✓",
    "L7_med":       "Epic Sepsis: демо ≠ клиника ✗",
    "L9_aero":      "F-35 ALIS: привязка к вендору ✗",
    "L6_cad":       "генеративный дизайн как советник",
    "L8_creat":     "Getty/NYT: утечка обуч. данных",
    "L10_seespray": "−50% гербицида (1→0,5 фунт/акр) ✓",
    "L10_monarch":  "открытое поле, 102 сокращения (38%) ✗",
    "L11_manuf":    "Tesla 2018: переавтоматизация",
    "L12_auto":     "двойник как мост; пропуск ступени ✗",
    "L13_wh":       "Symbotic: закрытый склад ✓",
    "L13_taxi":     "Cruise: расширение домена → отзыв 2024 ✗",
    "L13_swan":     "редкое событие: классика/человек выигрывает",
    "L14_cyber":    "CrowdStrike без канарейки → 8,5М машин ✗",
    "L15_alpha":    "AlphaFold: закрытая задача ✓",
    "L15_galac":    "текст ≠ эксперимент → отозвана за 3 дня ✗",
    "L16_oil":      "AI как советник; безопасность капает автономию",
}

# Quadrant zone descriptive labels for the poster (RU) — CANON Phase 8a:
#   UR = closed-loop success | UL = WARNING | LR = CAPPED | LL = classical.
# Positions avoid collisions with legend (UL upper area) and clustered points.
ZONE_LABELS = {
    "UR": ("AI РАБОТАЕТ И АВТОНОМНО", "зрелые закрытые-петли успехи", 0.74, 0.955, TEAL),
    "UL": ("ЗОНА ПРЕДУПРЕЖДЕНИЯ", "низкая применимость × высокая автономия", 0.27, 0.955, GOLD),
    "LL": ("«КЛАССИКА ВЫИГРЫВАЕТ»", "AI не нужен / не применим", 0.27, 0.40, SLATE),
    "LR": ("AI РАБОТАЕТ, АВТОНОМИЯ КАПНУТА", "регулятор ограничивает уровень", 0.755, 0.075, MID),
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_poster_svg(width=2380, height=1680):
    # A1 landscape aspect = 84.1:59.4 ≈ 1.4158. 2380x1680 ≈ 1.4167 (≈200dpi).
    # Generous insets for title/footer/axis labels.
    L, R = 250, width - 90
    T, B = 150, height - 200
    pw, ph = R - L, B - T

    def px(nx):
        return L + nx * pw

    def py(ny):
        return B - ny * ph

    P = []
    P.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="Liberation Sans, Arial, sans-serif">'
    )
    P.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="{WHITE}"/>')

    # --- Title band ---
    P.append(
        f'<text x="{width/2}" y="74" font-size="52" font-weight="bold" '
        f'fill="{DEEP}" text-anchor="middle">Карта 17 отраслей курса — применимость ИИ × автономия</text>'
    )
    P.append(
        f'<text x="{width/2}" y="116" font-size="28" fill="{LIGHT}" '
        f'text-anchor="middle">Опорная карточка #4 · плакат A1 · итоговая лекция курса AI-usage-lessons v1.0</text>'
    )

    # --- Quadrant tint zones (CANON: warning = UPPER-LEFT) ---
    midx, midy = px(0.5), py(0.5)
    # warning zone (upper-left) — gold dashed border emphasis
    P.append(
        f'<rect x="{L}" y="{T}" width="{midx-L}" height="{midy-T}" fill="{UL_TINT}" '
        f'stroke="{GOLD}" stroke-width="4" stroke-dasharray="14,8"/>'
    )
    P.append(f'<rect x="{midx}" y="{T}" width="{R-midx}" height="{midy-T}" fill="{UR_TINT}"/>')
    P.append(f'<rect x="{L}" y="{midy}" width="{midx-L}" height="{B-midy}" fill="{LL_TINT}"/>')
    # regulatory-capped zone (lower-right) — filled, solid blue border
    P.append(
        f'<rect x="{midx}" y="{midy}" width="{R-midx}" height="{B-midy}" fill="{LR_TINT}" '
        f'stroke="{MID}" stroke-width="3" stroke-dasharray="none"/>'
    )

    # --- Zone labels (corners) ---
    for key, (label, desc, qx, qy, col) in ZONE_LABELS.items():
        P.append(
            f'<text x="{px(qx)}" y="{py(qy)}" font-size="27" font-weight="bold" '
            f'fill="{col}" text-anchor="middle" opacity="0.85">{esc(label)}</text>'
        )
        P.append(
            f'<text x="{px(qx)}" y="{py(qy)+30}" font-size="20" fill="{SLATE}" '
            f'text-anchor="middle" opacity="0.9">{esc(desc)}</text>'
        )

    # --- Plot border + mid grid ---
    P.append(f'<rect x="{L}" y="{T}" width="{pw}" height="{ph}" fill="none" stroke="{LIGHT}" stroke-width="2"/>')
    P.append(f'<line x1="{midx}" y1="{T}" x2="{midx}" y2="{B}" stroke="{SLATE}" stroke-width="1.2" stroke-dasharray="6,6" opacity="0.5"/>')
    P.append(f'<line x1="{L}" y1="{midy}" x2="{R}" y2="{midy}" stroke="{SLATE}" stroke-width="1.2" stroke-dasharray="6,6" opacity="0.5"/>')

    # --- Axis labels (inside as scale markers + direction arrows) ---
    P.append(f'<text x="{(L+R)/2}" y="{B+74}" font-size="34" font-weight="bold" fill="{DEEP}" text-anchor="middle">Применимость ИИ  →</text>')
    P.append(f'<text x="{L+6}" y="{B+44}" font-size="22" fill="{SLATE}" text-anchor="start">детерминированный non-AI</text>')
    P.append(f'<text x="{R-6}" y="{B+44}" font-size="22" fill="{SLATE}" text-anchor="end">полный AI</text>')
    P.append(f'<text x="{70}" y="{(T+B)/2}" font-size="34" font-weight="bold" fill="{DEEP}" text-anchor="middle" transform="rotate(-90 70 {(T+B)/2})">Автономия  L0 → L5  ↑</text>')
    P.append(f'<text x="{L-30}" y="{B-6}" font-size="22" fill="{SLATE}" text-anchor="middle">L0</text>')
    P.append(f'<text x="{L-30}" y="{T+22}" font-size="22" fill="{SLATE}" text-anchor="middle">L5</text>')

    # --- Legend (module colors) — lower-left classical zone (sparse), boxed
    # so it doesn't read as a data point; keeps the warning UL zone clean.
    lx0, ly0 = L + 24, midy + 56
    P.append(f'<rect x="{lx0-12}" y="{ly0-40}" width="320" height="130" rx="10" '
             f'fill="{WHITE}" stroke="{LIGHT}" stroke-width="1.5" opacity="0.92"/>')
    legend = [(DEEP, "Модуль 1 (L1–L8)"), (TEAL, "Модуль 2 (L9–L12)"), (GOLD, "Модуль 3 (L13–L17)")]
    for i, (c, txt) in enumerate(legend):
        yy = ly0 + i * 38
        P.append(f'<rect x="{lx0}" y="{yy-18}" width="24" height="24" rx="5" fill="{c}"/>')
        P.append(f'<text x="{lx0+34}" y="{yy}" font-size="22" fill="{DEEP}">{esc(txt)}</text>')

    # Per-point label-side override to avoid collisions in the dense cluster.
    # "left" = text placed to the LEFT of the dot (anchor end).
    # Warning cluster (Monarch/robotaxi/Galactica) sits near the centre divider
    # → labels LEFT so they stay inside the warning (upper-left) zone.
    # L14 LEFT so its callout doesn't collide with L7 médecина to the right.
    LEFT_LABEL = {"L16_oil", "L11_manuf", "L10_monarch", "L13_taxi", "L15_galac",
                  "L14_cyber"}
    # Per-point vertical label nudge (px) to separate near-coincident rows.
    # Warning cluster vertical lanes: Monarch(top) / robotaxi(mid) / Galactica(low).
    # Lower-right CAPPED cluster: L9(top) / L7(mid) / L14(low) avoid collision.
    LABEL_DY = {
        "L11_manuf": -6, "L9_aero": -2,
        "L10_monarch": -10, "L13_taxi": 26, "L15_galac": 62,
        "L7_med": 30, "L14_cyber": 64,
    }

    # --- Points + callouts ---
    for (key, x, y, color_raw, label, batch, kind) in POINTS:
        color = color_raw if color_raw.startswith("#") else "#" + color_raw
        cx, cy = px(x), py(y)
        r = 16
        if kind == "fail":
            P.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{WHITE}" stroke="{color}" stroke-width="5"/>')
            P.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.4}" fill="{color}"/>')
        elif kind == "near0":
            P.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{WHITE}" stroke="{color}" stroke-width="5" stroke-dasharray="5,5"/>')
        else:
            P.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>')

        # Primary label (отрасль), bold
        anchor = "start"
        lx = cx + r + 12
        if x > 0.76 or key in LEFT_LABEL:
            anchor = "end"
            lx = cx - r - 12
        ly = cy - 4 + LABEL_DY.get(key, 0)
        if kind == "near0":
            anchor = "middle"
            lx = cx
            ly = cy - r - 14
        P.append(
            f'<text x="{lx}" y="{ly}" font-size="23" font-weight="bold" fill="{DEEP}" '
            f'text-anchor="{anchor}">{esc(label)}</text>'
        )
        # Callout line under label
        co = CALLOUTS.get(key)
        if co:
            cly = ly + 26
            if kind == "near0":
                cly = ly - 26
            P.append(
                f'<text x="{lx}" y="{cly}" font-size="17" fill="{SLATE}" '
                f'text-anchor="{anchor}">{esc(co)}</text>'
            )

    # --- Footer ---
    fy = height - 96
    P.append(f'<rect x="{L}" y="{fy-34}" width="{R-L}" height="84" rx="14" fill="{SURFACE}" stroke="{LIGHT}" stroke-width="2"/>')
    P.append(
        f'<text x="{L+28}" y="{fy}" font-size="22" font-weight="bold" fill="{DEEP}" text-anchor="start">'
        f'Повесьте плакат на стену.</text>'
    )
    P.append(
        f'<text x="{L+28}" y="{fy+32}" font-size="19" fill="{LIGHT}" text-anchor="start">'
        f'Для новой отрасли карта даёт аналогии по координатам: «похоже на See &amp; Spray по закрытой петле» '
        f'или «похоже на робот-такси — домен недостаточен». Каждая точка — недели разбора кейсов и провалов.</text>'
    )

    P.append("</svg>")
    return "\n".join(P)


def main():
    svg = build_poster_svg()
    svg_path = OUT / "master-poster-a1.svg"
    png_path = OUT / "master-poster-a1.png"
    svg_path.write_text(svg, encoding="utf-8")
    # SVG viewBox is 2380×1680; render at 4960×3500 px → ≥150 dpi when placed
    # into A1 (33.11 × 23.39"). Vector source = no quality loss on upscale.
    subprocess.run(
        ["rsvg-convert", "-w", "4960", "-h", "3500", "-f", "png",
         str(svg_path), "-o", str(png_path)],
        check=True,
    )
    print("Master poster rendered (150dpi @ A1):", png_path)


if __name__ == "__main__":
    main()
