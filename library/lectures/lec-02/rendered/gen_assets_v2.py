#!/usr/bin/env python3
"""Asset generation for lec-02 v2.0 batch 1: s11 chart (QuickChart POST) +
s01 hero illustration (own SVG -> PNG via PyMuPDF)."""
import json
import urllib.request
from pathlib import Path

ASSETS = Path("/home/harness/harness-projects/256/.worktrees/folder-288/lesson2-3f2b0b82/library/lectures/lec-02/rendered/assets")

# ---------------------------------------------------------------- s11 chart
def gen_s11_chart():
    cfg = {
        "type": "bar",
        "data": {
            "labels": ["Английский", "Русский", "Китайский", "Python-код"],
            "datasets": [{
                "data": [0.25, 0.5, 0.8, 0.4],
                "backgroundColor": ["#065A82", "#F0AB00", "#065A82", "#028090"],
                "borderRadius": 4,
            }],
        },
        "options": {
            "indexAxis": "y",
            "plugins": {
                "legend": {"display": False},
                "datalabels": {
                    "anchor": "end", "align": "end",
                    "color": "#21295C",
                    "font": {"size": 26, "weight": "bold"},
                    "formatter": "___FMT___",
                },
            },
            "scales": {
                "x": {
                    "min": 0, "max": 1.0,
                    "title": {"display": True, "text": "токены на символ",
                              "color": "#1C7293", "font": {"size": 22}},
                    "ticks": {"color": "#1C7293", "font": {"size": 20}},
                    "grid": {"color": "#E5EAF0"},
                },
                "y": {
                    "ticks": {"color": "#21295C",
                              "font": {"size": 24, "weight": "bold"}},
                    "grid": {"display": False},
                },
            },
        },
    }
    body = json.dumps({
        "chart": json.dumps(cfg).replace('"___FMT___"',
            "function(v){return '≈'+v.toString().replace('.',',');}"),
        "width": 980, "height": 560, "format": "png",
        "backgroundColor": "white", "version": "4",
    }).encode()
    req = urllib.request.Request("https://quickchart.io/chart",
                                 data=body,
                                 headers={"Content-Type": "application/json"})
    out = ASSETS / "charts/s11-tokens-per-char-v2.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(req, timeout=60) as r:
        out.write_bytes(r.read())
    print("s11 chart:", out, out.stat().st_size, "bytes")


# ------------------------------------------------------------- s01 hero SVG
S01_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="1240" height="640" viewBox="0 0 1240 640">
  <!-- Модель как чёрный ящик с трещинами - приглушённая ocean-иллюстрация -->
  <!-- вход: поток текста слева -->
  <g stroke="#b9cbdd" stroke-width="10" stroke-linecap="round">
    <line x1="40"  y1="280" x2="200" y2="280"/>
    <line x1="70"  y1="330" x2="200" y2="330"/>
    <line x1="40"  y1="380" x2="200" y2="380"/>
  </g>
  <path d="M215 330 l70 0 l0 -22 l55 42 l-55 42 l0 -22 l-70 0 z" fill="#b9cbdd"/>
  <!-- сам чёрный ящик (приглушённый ocean-тон, темнее для метафоры) -->
  <rect x="370" y="120" width="500" height="420" rx="36" fill="#b8c9db" stroke="#8aa3bd" stroke-width="6"/>
  <!-- трещины -->
  <g stroke="#F0AB00" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M470 120 l-18 70 l38 44 l-20 58"/>
    <path d="M770 540 l24 -78 l-40 -48 l18 -52"/>
    <path d="M870 300 l-64 12 l-30 -40"/>
  </g>
  <g stroke="#f4f7fa" stroke-width="6" fill="none" stroke-linecap="round">
    <path d="M620 120 l10 52 l-30 36"/>
    <path d="M370 400 l56 -6 l30 34"/>
  </g>
  <!-- вопросительный знак в центре ящика -->
  <text x="620" y="392" font-family="DejaVu Sans" font-size="200" font-weight="bold"
        fill="#f4f7fa" text-anchor="middle">?</text>
  <!-- выход: поток справа -->
  <path d="M900 330 l70 0 l0 -22 l55 42 l-55 42 l0 -22 l-70 0 z" fill="#b9cbdd"/>
  <g stroke="#b9cbdd" stroke-width="10" stroke-linecap="round">
    <line x1="1040" y1="280" x2="1200" y2="280"/>
    <line x1="1040" y1="330" x2="1170" y2="330"/>
    <line x1="1040" y1="380" x2="1200" y2="380"/>
  </g>
</svg>"""


def gen_s01_hero():
    import pymupdf
    svg_path = ASSETS / "illustrations/s01-blackbox-cracks.svg"
    png_path = ASSETS / "illustrations/s01-blackbox-cracks.png"
    svg_path.parent.mkdir(parents=True, exist_ok=True)
    svg_path.write_text(S01_SVG, encoding="utf-8")
    doc = pymupdf.open(str(svg_path))
    page = doc[0]
    pix = page.get_pixmap(matrix=pymupdf.Matrix(1.6, 1.6), alpha=True)
    pix.save(str(png_path))
    print("s01 hero:", png_path, png_path.stat().st_size, "bytes")


if __name__ == "__main__":
    gen_s01_hero()
    gen_s11_chart()
