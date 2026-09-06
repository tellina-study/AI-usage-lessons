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


# ================================================================ batch 2
def _quickchart(cfg, out_name, w, h):
    body = json.dumps({
        "chart": json.dumps(cfg), "width": w, "height": h,
        "format": "png", "backgroundColor": "white", "version": "4",
    }).encode()
    req = urllib.request.Request("https://quickchart.io/chart", data=body,
                                 headers={"Content-Type": "application/json"})
    out = ASSETS / out_name
    out.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(req, timeout=60) as r:
        out.write_bytes(r.read())
    print(out_name, out.stat().st_size, "bytes")


def gen_s19_chart():
    """Веса внимания на 7 токенов — та же нарезка предложения, что в
    матрице s18 («потому что» единым токеном); сумма = 1, «мышь» gold.
    (v2.0.2 item 5: унификация токенизации s18↔s19.)"""
    labels = ["Кот", "съел", "мышь", "потому что", "она", "была",
              "голодна"]
    vals = [0.04, 0.05, 0.40, 0.06, 0.10, 0.14, 0.21]
    colors = ["#065A82"] * 7
    colors[2] = "#F0AB00"
    cfg = {
        "type": "bar",
        "data": {"labels": labels, "datasets": [{
            "data": vals, "backgroundColor": colors, "borderRadius": 3}]},
        "options": {
            "plugins": {
                "legend": {"display": False},
                "datalabels": {"anchor": "end", "align": "end",
                               "color": "#21295C",
                               "font": {"size": 22, "weight": "bold"},
                               "formatter": "___FMT___"},
            },
            "scales": {
                "y": {"min": 0, "max": 0.5,
                      "ticks": {"color": "#1C7293", "font": {"size": 18}},
                      "grid": {"color": "#E5EAF0"}},
                "x": {"ticks": {"color": "#21295C",
                                "font": {"size": 21, "weight": "bold"}},
                      "grid": {"display": False}},
            },
        },
    }
    body = json.dumps({
        "chart": json.dumps(cfg).replace('"___FMT___"',
            "function(v){return v.toString().replace('.',',');}"),
        "width": 980, "height": 400, "format": "png",
        "backgroundColor": "white", "version": "4",
    }).encode()
    req = urllib.request.Request("https://quickchart.io/chart", data=body,
                                 headers={"Content-Type": "application/json"})
    out = ASSETS / "charts/s19-attention-weights.png"
    with urllib.request.urlopen(req, timeout=60) as r:
        out.write_bytes(r.read())
    print("s19 chart:", out, out.stat().st_size, "bytes")


def gen_s25_chart():
    """NoLiMa: 13 моделей, точность на 32K как % их же базовой; 11 ниже
    пунктира 50% (gold)."""
    vals = [58, 53, 47, 44, 41, 38, 35, 33, 30, 27, 24, 20, 15]
    colors = ["#028090" if v >= 50 else "#065A82" for v in vals]
    cfg = {
        "type": "bar",
        "data": {"labels": [""] * 13, "datasets": [{
            "data": vals, "backgroundColor": colors, "borderRadius": 2}]},
        "options": {
            "plugins": {
                "legend": {"display": False},
                "datalabels": {"display": False},
                "annotation": {"annotations": {"half": {
                    "type": "line", "yMin": 50, "yMax": 50,
                    "borderColor": "#F0AB00", "borderWidth": 4,
                    "borderDash": [10, 7],
                    "label": {"enabled": True,
                              "content": "50% базовой точности",
                              "backgroundColor": "#F0AB00",
                              "color": "#21295C",
                              "font": {"size": 19, "weight": "bold"},
                              "position": "end"},
                }}},
            },
            # Шрифты: канвас 980px показан на слайде в 4.6" →
            # 1px ≈ 0.338pt; минимум 11pt (projector sub-label) ⇒ ≥33px.
            "scales": {
                "y": {"min": 0, "max": 100,
                      "title": {"display": True,
                                "text": ["% от базовой", "точности модели"],
                                "color": "#1C7293", "font": {"size": 33}},
                      "ticks": {"color": "#1C7293", "font": {"size": 33}},
                      "grid": {"color": "#E5EAF0"}},
                "x": {"title": {"display": True,
                                "text": "13 моделей · контекст 32 тыс. токенов",
                                "color": "#1C7293", "font": {"size": 33}},
                      "grid": {"display": False}},
            },
        },
    }
    _quickchart(cfg, "charts/s25-nolima.png", 980, 480)


# ------------------------------------------------------------- s41 hero SVG
# Solid fills only (#183-1: PyMuPDF рендерит linearGradient чёрным).
S41_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="1240" height="640" viewBox="0 0 1240 640">
  <!-- Мост от конвейера Лекции 2 (левый берег) к миру агентов Лекции 3 (правый) -->
  <!-- левый берег -->
  <rect x="0" y="430" width="330" height="210" rx="18" fill="#b8c9db"/>
  <!-- конвейер на левом берегу: 4 блока-стадии -->
  <g fill="#8aa3bd">
    <rect x="30"  y="360" width="60" height="44" rx="8"/>
    <rect x="102" y="360" width="60" height="44" rx="8"/>
    <rect x="174" y="360" width="60" height="44" rx="8"/>
  </g>
  <rect x="246" y="360" width="60" height="44" rx="8" fill="#F0AB00"/>
  <!-- правый берег -->
  <rect x="910" y="430" width="330" height="210" rx="18" fill="#b8c9db"/>
  <!-- агентный граф на правом берегу -->
  <g stroke="#8aa3bd" stroke-width="7" fill="none">
    <line x1="990" y1="330" x2="1080" y2="390"/>
    <line x1="1080" y1="390" x2="1170" y2="330"/>
    <line x1="1080" y1="390" x2="1080" y2="300"/>
  </g>
  <circle cx="990"  cy="330" r="30" fill="#b9cbdd"/>
  <circle cx="1170" cy="330" r="30" fill="#b9cbdd"/>
  <circle cx="1080" cy="300" r="26" fill="#b9cbdd"/>
  <circle cx="1080" cy="390" r="36" fill="#F0AB00"/>
  <!-- пролёт моста -->
  <rect x="290" y="470" width="660" height="26" fill="#8aa3bd"/>
  <!-- центральный пилон -->
  <rect x="601" y="150" width="38" height="420" rx="10" fill="#b8c9db"/>
  <!-- ванты (gold) -->
  <g stroke="#F0AB00" stroke-width="8" fill="none" stroke-linecap="round">
    <line x1="620" y1="170" x2="330" y2="470"/>
    <line x1="620" y1="240" x2="430" y2="470"/>
    <line x1="620" y1="310" x2="520" y2="470"/>
    <line x1="620" y1="170" x2="910" y2="470"/>
    <line x1="620" y1="240" x2="810" y2="470"/>
    <line x1="620" y1="310" x2="720" y2="470"/>
  </g>
  <!-- поток по мосту: стрелка слева направо -->
  <path d="M400 508 l360 0 l0 -16 l60 30 l-60 30 l0 -16 l-360 0 z" fill="#f4f7fa" opacity="0.9"/>
</svg>"""


def gen_s41_hero():
    import pymupdf
    svg_path = ASSETS / "illustrations/s41-bridge-lec3.svg"
    png_path = ASSETS / "illustrations/s41-bridge-lec3.png"
    svg_path.parent.mkdir(parents=True, exist_ok=True)
    svg_path.write_text(S41_SVG, encoding="utf-8")
    doc = pymupdf.open(str(svg_path))
    pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(1.6, 1.6), alpha=True)
    pix.save(str(png_path))
    print("s41 hero:", png_path, png_path.stat().st_size, "bytes")


def gen_s41_icons():
    """Lucide icons для 4 карточек s41: search / cog / plug / refresh-cw,
    recolor в Ocean mid, 96px PNG (PyMuPDF)."""
    import pymupdf
    icons = {"search": "search", "settings": "settings", "plug": "plug",
             "refresh-cw": "refresh-cw"}
    outdir = ASSETS / "icons"
    outdir.mkdir(parents=True, exist_ok=True)
    for name, slug in icons.items():
        url = (f"https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/"
               f"{slug}.svg")
        with urllib.request.urlopen(url, timeout=30) as r:
            svg = r.read().decode()
        svg = svg.replace("currentColor", "#065A82")
        sp = outdir / f"s41-{name}.svg"
        sp.write_text(svg, encoding="utf-8")
        doc = pymupdf.open(str(sp))
        pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(4, 4), alpha=True)
        pix.save(str(outdir / f"s41-{name}.png"))
        print("icon", name, "OK")


if __name__ == "__main__":
    import sys
    if "--batch2" in sys.argv:
        gen_s19_chart()
        gen_s25_chart()
        gen_s41_hero()
        gen_s41_icons()
    else:
        gen_s01_hero()
        gen_s11_chart()
