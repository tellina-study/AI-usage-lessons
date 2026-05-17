"""
SVG-literal diagrams for Лекция 5 (project-preferred fallback,
notes/mcp-limitations.md [#69-svg-fallback]: mermaid needs Chrome,
absent in WSL). Full control over Ocean palette + typography.
Run: python3 gen_diagrams.py  → assets/diagrams/*.png
"""
import subprocess
from pathlib import Path

OUT = Path(__file__).parent / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

DEEP = "#21295C"
MID = "#065A82"
LIGHT = "#1C7293"
TEAL = "#028090"
GOLD = "#F0AB00"
SURF = "#F4F7FA"
SLATE = "#5B6678"
GREY = "#E5EAF0"
FONT = "Inter, Arial, sans-serif"


def render(name, svg, w, h):
    p = OUT / (name + ".svg")
    p.write_text(svg, encoding="utf-8")
    subprocess.run(
        ["rsvg-convert", "-w", str(w), "-h", str(h), "-f", "png",
         str(p), "-o", str(OUT / (name + ".png"))], check=True)
    print(name + ".png", "OK")


# ---- d08: time-series decomposition (trend + seasonality + noise) ----
def d08():
    import math
    W, H = 1100, 460
    rows = [
        ("История продаж", DEEP,
         lambda x: 120 + 38 * (x / 1000.0)
         + 32 * math.sin(x / 1000.0 * 6.28 * 4)
         + 9 * math.sin(x * 0.13)),
        ("Тренд — продажи растут", MID, lambda x: 120 + 38 * (x / 1000.0)),
        ("Сезонность — недельный / годовой цикл", TEAL,
         lambda x: 70 + 32 * math.sin(x / 1000.0 * 6.28 * 4)),
        ("Шум — случайные колебания", LIGHT,
         lambda x: 40 + 9 * math.sin(x * 0.13)),
    ]
    parts = [f'<rect width="{W}" height="{H}" fill="none"/>']
    rh = 104
    for i, (label, col, fn) in enumerate(rows):
        y0 = 18 + i * rh
        parts.append(
            f'<rect x="8" y="{y0}" width="{W-16}" height="{rh-16}" rx="14" '
            f'fill="{SURF}" stroke="{LIGHT}" stroke-width="1.5"/>')
        parts.append(
            f'<text x="30" y="{y0+30}" font-family="{FONT}" font-size="20" '
            f'font-weight="700" fill="{col}">{label}</text>')
        pts = []
        for px in range(0, 1001, 12):
            sx = 280 + px * (W - 320) / 1000.0
            sy = y0 + rh - 26 - (fn(px) - 30) * 0.42
            pts.append(f"{sx:.1f},{sy:.1f}")
        parts.append(
            f'<polyline points="{" ".join(pts)}" fill="none" '
            f'stroke="{col}" stroke-width="3.4" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
           f'height="{H}" viewBox="0 0 {W} {H}">' + "".join(parts) + "</svg>")
    render("d08-timeseries-decomp", svg, W, H)


# ---- d11: anomaly cloud + outlier ----
def d11():
    import random
    random.seed(42)
    W, H = 760, 560
    parts = [f'<rect width="{W}" height="{H}" fill="none"/>']
    cx, cy = 330, 320
    # normal cloud
    for _ in range(120):
        a = random.uniform(0, 6.2832)
        r = random.gauss(0, 1) * 95
        x = cx + r * 0.92 * (1 if random.random() > .5 else .8) \
            * (random.random() ** 0.5) * (1 if random.random() > .5 else -1)
        x = cx + random.gauss(0, 70)
        y = cy + random.gauss(0, 62)
        parts.append(
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" '
            f'fill="{LIGHT}" opacity="0.55"/>')
    # boundary ellipse
    parts.append(
        f'<ellipse cx="{cx}" cy="{cy}" rx="168" ry="150" fill="none" '
        f'stroke="{MID}" stroke-width="3" stroke-dasharray="9 7"/>')
    parts.append(
        f'<text x="{cx}" y="{cy+200}" font-family="{FONT}" '
        f'font-size="22" font-weight="700" fill="{MID}" '
        f'text-anchor="middle">«Норма» этого клиента</text>')
    # outlier
    ox, oy = 640, 92
    parts.append(
        f'<circle cx="{ox}" cy="{oy}" r="17" fill="{GOLD}" '
        f'stroke="{DEEP}" stroke-width="3"/>')
    parts.append(
        f'<line x1="{cx+150}" y1="{cy-110}" x2="{ox-22}" y2="{oy+18}" '
        f'stroke="{GOLD}" stroke-width="3" stroke-dasharray="6 6"/>')
    parts.append(
        f'<text x="{ox}" y="{oy-30}" font-family="{FONT}" font-size="21" '
        f'font-weight="700" fill="{DEEP}" text-anchor="middle">'
        f'Выброс — кандидат</text>')
    parts.append(
        f'<text x="{ox}" y="{oy-6}" font-family="{FONT}" font-size="17" '
        f'fill="{SLATE}" text-anchor="middle">'
        f'другая страна · 4:00 · нетипичная сумма</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
           f'height="{H}" viewBox="0 0 {W} {H}">' + "".join(parts) + "</svg>")
    render("d11-anomaly-cloud", svg, W, H)


# ---- d26: user × item matrix (collaborative filtering) ----
def d26():
    W, H = 760, 560
    parts = [f'<rect width="{W}" height="{H}" fill="none"/>']
    cols = ["🛒", "📚", "🎬", "🎧", "👟"]
    n, m = 5, 5
    cw, chh = 110, 78
    x0, y0 = 150, 110
    grid = [
        [1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],   # «вы»
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1],
    ]
    parts.append(
        f'<text x="{x0+cw*m/2}" y="60" font-family="{FONT}" '
        f'font-size="22" font-weight="700" fill="{DEEP}" '
        f'text-anchor="middle">Матрица «пользователь × товар»</text>')
    for j in range(m):
        parts.append(
            f'<text x="{x0+j*cw+cw/2}" y="{y0-16}" font-family="{FONT}" '
            f'font-size="21" fill="{MID}" font-weight="700" '
            f'text-anchor="middle">товар {j+1}</text>')
    for i in range(n):
        is_you = (i == 1)
        parts.append(
            f'<text x="{x0-22}" y="{y0+i*chh+chh/2+7}" '
            f'font-family="{FONT}" font-size="20" '
            f'fill="{GOLD if is_you else MID}" '
            f'font-weight="700" text-anchor="end">'
            f'{"вы" if is_you else f"юзер {i+1}"}</text>')
        for j in range(m):
            v = grid[i][j]
            fill = (GOLD if is_you and v else
                    (MID if v else SURF))
            stroke = GOLD if is_you else GREY
            parts.append(
                f'<rect x="{x0+j*cw}" y="{y0+i*chh}" width="{cw-8}" '
                f'height="{chh-8}" rx="8" fill="{fill}" '
                f'stroke="{stroke}" stroke-width="'
                f'{2.5 if is_you else 1}"/>')
            if v:
                parts.append(
                    f'<text x="{x0+j*cw+(cw-8)/2}" '
                    f'y="{y0+i*chh+(chh-8)/2+9}" font-family="{FONT}" '
                    f'font-size="26" fill="#FFFFFF" font-weight="700" '
                    f'text-anchor="middle">✓</text>')
    yb = y0 + n * chh + 36
    parts.append(
        f'<text x="{W/2}" y="{yb}" font-family="{FONT}" font-size="19" '
        f'fill="{SLATE}" text-anchor="middle">'
        f'«похожие на вас люди брали товар 1 — вероятно, понравится вам»'
        f'</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
           f'height="{H}" viewBox="0 0 {W} {H}">' + "".join(parts) + "</svg>")
    render("d26-user-item-matrix", svg, W, H)


if __name__ == "__main__":
    d08()
    d11()
    d26()
