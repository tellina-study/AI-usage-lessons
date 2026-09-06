#!/usr/bin/env python3
"""Asset generation for lec-02 v3.0 (issue #183 rework-round2):
- s01 NEW hero meme (two-panel T=0 gag, replaces s01-blackbox-cracks)
- 6 section-divider mini-illustrations (own flat SVG, Ocean palette)
- s31 "gorshochek ne vari" mini-illustration (degenerate repetition loop)
All via own hand-authored SVG -> PNG (PyMuPDF), NOT stock/mermaid — see
notes/mcp-limitations.md [#118-1] (mmdc needs Chrome, unavailable) and
[#157-1] (no rsvg-convert in this sandbox either). PyMuPDF SVG rasterizer
confirmed working (used for s01-blackbox-cracks/s41-bridge-lec3 in v2.x).
"""
from pathlib import Path
import pymupdf

ASSETS = Path("/home/harness/harness-projects/256/.worktrees/folder-288/lesson2-3f2b0b82/library/lectures/lec-02/rendered/assets")
ILL = ASSETS / "illustrations"
ILL.mkdir(parents=True, exist_ok=True)


def render(svg_text: str, name: str, scale: float = 1.6):
    svg_path = ILL / f"{name}.svg"
    png_path = ILL / f"{name}.png"
    svg_path.write_text(svg_text, encoding="utf-8")
    doc = pymupdf.open(str(svg_path))
    page = doc[0]
    pix = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=True)
    pix.save(str(png_path))
    print(name, png_path.stat().st_size, "bytes")


# ============================================================
# s01 — NEW hero meme: T=0 two-panel gag (own flat illustration,
# Ocean palette; NOT a copy of an existing meme format's punchline —
# custom "confident face" -> "puzzled face" composition).
# ============================================================
S01_MEME_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="640" viewBox="0 0 1400 640">
  <!-- Panel divider -->
  <line x1="700" y1="40" x2="700" y2="600" stroke="#1C7293" stroke-width="3" stroke-dasharray="14 10"/>

  <!-- ===== LEFT PANEL: confident face, "Да." ===== -->
  <g>
    <circle cx="330" cy="260" r="175" fill="#F4F7FA" stroke="#1C7293" stroke-width="6"/>
    <!-- confident face: flat, calm eyes + straight mouth -->
    <circle cx="260" cy="230" r="16" fill="#21295C"/>
    <circle cx="400" cy="230" r="16" fill="#21295C"/>
    <path d="M250 320 Q330 360 410 320" stroke="#21295C" stroke-width="10" fill="none" stroke-linecap="round"/>
    <!-- eyebrows: level, sure of itself -->
    <path d="M225 195 L295 195" stroke="#21295C" stroke-width="8" stroke-linecap="round"/>
    <path d="M365 195 L435 195" stroke="#21295C" stroke-width="8" stroke-linecap="round"/>
    <!-- small T=0 badge on chest -->
    <rect x="255" y="455" width="150" height="60" rx="14" fill="#065A82"/>
    <text x="330" y="497" font-family="DejaVu Sans" font-size="34" font-weight="bold" fill="#ffffff" text-anchor="middle">T=0</text>
  </g>

  <!-- ===== RIGHT PANEL: puzzled/surprised face, gold accent ===== -->
  <g>
    <circle cx="1070" cy="260" r="175" fill="#FEF5E0" stroke="#F0AB00" stroke-width="6"/>
    <!-- puzzled face: raised eyebrows + open mouth -->
    <circle cx="1000" cy="225" r="18" fill="#21295C"/>
    <circle cx="1140" cy="225" r="18" fill="#21295C"/>
    <ellipse cx="1070" cy="330" rx="34" ry="26" fill="#21295C"/>
    <!-- one eyebrow raised -->
    <path d="M965 175 Q1000 155 1035 180" stroke="#21295C" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path d="M1105 180 L1175 195" stroke="#21295C" stroke-width="8" stroke-linecap="round"/>
    <!-- sweat-drop style surprise mark -->
    <path d="M1195 165 q14 26 0 40 q-14 -14 0 -40 z" fill="#1C7293"/>
    <!-- gold question mark above -->
    <text x="1070" y="90" font-family="DejaVu Sans" font-size="80" font-weight="bold" fill="#F0AB00" text-anchor="middle">?</text>
  </g>
</svg>"""


def gen_s01_meme():
    render(S01_MEME_SVG, "s01-t0-meme")


# ============================================================
# Section divider mini-illustrations (small, corner-placement,
# Ocean palette, flat compositions — own art, not stock memes).
# ============================================================

S05A_KNIFE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="360" viewBox="0 0 360 360">
  <!-- Toкенизация: нож режет слово на куски -->
  <rect x="30" y="150" width="300" height="70" rx="10" fill="#F4F7FA" stroke="#1C7293" stroke-width="4"/>
  <text x="70" y="197" font-family="DejaVu Sans Mono" font-size="34" font-weight="bold" fill="#21295C">клуб</text>
  <line x1="150" y1="150" x2="150" y2="220" stroke="#F0AB00" stroke-width="4" stroke-dasharray="6 6"/>
  <text x="185" y="197" font-family="DejaVu Sans Mono" font-size="34" font-weight="bold" fill="#065A82">ни</text>
  <line x1="235" y1="150" x2="235" y2="220" stroke="#F0AB00" stroke-width="4" stroke-dasharray="6 6"/>
  <text x="255" y="197" font-family="DejaVu Sans Mono" font-size="34" font-weight="bold" fill="#028090">ка</text>
  <!-- нож сверху -->
  <g transform="rotate(-18 235 90)">
    <polygon points="150,60 300,80 300,100 170,100" fill="#1C7293"/>
    <rect x="120" y="72" width="40" height="24" rx="6" fill="#21295C"/>
  </g>
</svg>"""

S12A_MAP_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="360" viewBox="0 0 360 360">
  <!-- Эмбеддинги: карта смыслов — точки-кластеры на условной карте -->
  <rect x="20" y="20" width="320" height="320" rx="16" fill="#F4F7FA" stroke="#1C7293" stroke-width="4"/>
  <path d="M40 250 Q120 180 180 220 T320 160" stroke="#1C7293" stroke-width="3" fill="none" stroke-dasharray="5 7" opacity="0.6"/>
  <circle cx="110" cy="120" r="34" fill="none" stroke="#065A82" stroke-width="3" stroke-dasharray="4 5"/>
  <circle cx="95" cy="110" r="10" fill="#065A82"/>
  <circle cx="128" cy="135" r="10" fill="#065A82"/>
  <circle cx="240" cy="230" r="38" fill="none" stroke="#028090" stroke-width="3" stroke-dasharray="4 5"/>
  <circle cx="225" cy="220" r="10" fill="#028090"/>
  <circle cx="255" cy="245" r="10" fill="#028090"/>
  <circle cx="270" cy="90" r="12" fill="#F0AB00"/>
  <!-- компас-стрелка как "карта" акцент -->
  <polygon points="290,290 305,255 320,290 305,280" fill="#21295C"/>
</svg>"""

S18A_FLASHLIGHT_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="360" viewBox="0 0 360 360">
  <!-- Внимание: фонарик освещает часть токенов -->
  <g transform="rotate(28 120 300)">
    <rect x="40" y="270" width="120" height="46" rx="10" fill="#21295C"/>
    <polygon points="160,270 260,230 260,356 160,316" fill="#F0AB00" opacity="0.55"/>
  </g>
  <circle cx="255" cy="150" r="14" fill="#065A82" opacity="0.35"/>
  <circle cx="290" cy="190" r="20" fill="#F0AB00"/>
  <circle cx="230" cy="210" r="10" fill="#1C7293" opacity="0.4"/>
  <circle cx="300" cy="120" r="9" fill="#028090" opacity="0.5"/>
</svg>"""

S26A_DICE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="360" viewBox="0 0 360 360">
  <!-- Сэмплинг: кости/рулетка — случайный выбор из распределения -->
  <rect x="50" y="70" width="110" height="110" rx="18" fill="#F4F7FA" stroke="#1C7293" stroke-width="4" transform="rotate(-12 105 125)"/>
  <g transform="rotate(-12 105 125)">
    <circle cx="80" cy="100" r="8" fill="#065A82"/>
    <circle cx="130" cy="100" r="8" fill="#065A82"/>
    <circle cx="80" cy="150" r="8" fill="#065A82"/>
    <circle cx="130" cy="150" r="8" fill="#065A82"/>
    <circle cx="105" cy="125" r="8" fill="#F0AB00"/>
  </g>
  <rect x="190" y="150" width="110" height="110" rx="18" fill="#F4F7FA" stroke="#028090" stroke-width="4" transform="rotate(14 245 205)"/>
  <g transform="rotate(14 245 205)">
    <circle cx="215" cy="175" r="8" fill="#028090"/>
    <circle cx="275" cy="175" r="8" fill="#028090"/>
    <circle cx="245" cy="205" r="8" fill="#028090"/>
    <circle cx="215" cy="235" r="8" fill="#028090"/>
    <circle cx="275" cy="235" r="8" fill="#028090"/>
  </g>
</svg>"""

S33A_MATRYOSHKA_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="360" viewBox="0 0 360 360">
  <!-- Виды и размеры моделей: матрёшка — вложенные размеры -->
  <ellipse cx="180" cy="300" rx="130" ry="46" fill="#21295C"/>
  <path d="M60 300 Q60 120 180 90 Q300 120 300 300 Z" fill="#065A82"/>
  <ellipse cx="180" cy="260" rx="88" ry="34" fill="#1C7293"/>
  <path d="M100 260 Q100 140 180 118 Q260 140 260 260 Z" fill="#1C7293"/>
  <ellipse cx="180" cy="230" rx="52" ry="22" fill="#028090"/>
  <path d="M136 230 Q136 158 180 142 Q224 158 224 230 Z" fill="#028090"/>
  <circle cx="180" cy="168" r="26" fill="#F0AB00"/>
</svg>"""

S35A_PUZZLE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="360" viewBox="0 0 360 360">
  <!-- Финал: собранный пазл (конвейер собран целиком) -->
  <g fill="#065A82">
    <path d="M40 40 h110 v40 a20 20 0 0 1 0 40 v40 h-110 v-40 a20 20 0 0 0 0 -40 z"/>
  </g>
  <g fill="#1C7293">
    <path d="M150 40 h130 v120 h-40 a20 20 0 0 1 -40 0 h-50 z"/>
  </g>
  <g fill="#028090">
    <path d="M40 160 h70 a20 20 0 0 1 40 0 h130 v120 h-240 z"/>
  </g>
  <g fill="#F0AB00">
    <path d="M280 40 h40 v240 h-90 a20 20 0 0 0 -40 0 h-30 v-40 h30 a20 20 0 0 1 40 0 h50 z" opacity="0.94"/>
  </g>
</svg>"""


def gen_dividers():
    render(S05A_KNIFE_SVG, "s05a-tokenize-knife")
    render(S12A_MAP_SVG, "s12a-meaning-map")
    render(S18A_FLASHLIGHT_SVG, "s18a-flashlight")
    render(S26A_DICE_SVG, "s26a-dice")
    render(S33A_MATRYOSHKA_SVG, "s33a-matryoshka")
    render(S35A_PUZZLE_SVG, "s35a-puzzle")


# ============================================================
# s31 — "gorshochek ne vari" mini illustration (degenerate
# repetition loop): a pot boiling over with repeated tokens.
# ============================================================
S31_POT_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="420" height="360" viewBox="0 0 420 360">
  <!-- горшочек -->
  <ellipse cx="210" cy="290" rx="120" ry="26" fill="#21295C"/>
  <path d="M100 200 Q100 300 210 300 Q320 300 320 200 Z" fill="#065A82"/>
  <rect x="90" y="185" width="240" height="26" rx="13" fill="#1C7293"/>
  <!-- ручки -->
  <ellipse cx="80" cy="198" rx="16" ry="10" fill="none" stroke="#1C7293" stroke-width="8"/>
  <ellipse cx="340" cy="198" rx="16" ry="10" fill="none" stroke="#1C7293" stroke-width="8"/>
  <!-- переполнение — повторяющиеся токены "вали вали вали" вылезают через край -->
  <g font-family="DejaVu Sans Mono" font-size="20" font-weight="bold" fill="#F0AB00">
    <text x="130" y="150">каша</text>
    <text x="230" y="120">каша</text>
    <text x="150" y="90">каша</text>
    <text x="250" y="60">каша</text>
    <text x="190" y="35">каша…</text>
  </g>
  <path d="M150 185 Q160 150 140 110 Q170 100 165 60" stroke="#F4F7FA" stroke-width="10" fill="none" stroke-linecap="round" opacity="0.85"/>
  <path d="M270 185 Q260 145 285 105 Q255 95 265 55" stroke="#F4F7FA" stroke-width="10" fill="none" stroke-linecap="round" opacity="0.85"/>
</svg>"""


def gen_s31_pot():
    render(S31_POT_SVG, "s31-gorshochek")




# ============================================================
# v3.0 round-2 additions (main session):
# - s19 chart: пример «Кот съел мышь, потому что ОН был голоден» —
#   лидер весов «Кот» (согласование по роду), gold.
# - s25 верхний ярус: U-кривая (2023) vs плоская линия (2026), QuickChart.
# - s14: «звёздная карта» — иллюстративность пространства эмбеддингов.
# ============================================================
import json
import urllib.request

CHARTS = ASSETS / "charts"


def _quickchart(cfg, out_name, w, h):
    body = json.dumps({
        "chart": json.dumps(cfg),
        "width": w, "height": h, "format": "png",
        "backgroundColor": "white", "version": "4",
    }).encode()
    req = urllib.request.Request("https://quickchart.io/chart", data=body,
                                 headers={"Content-Type": "application/json"})
    out = CHARTS / out_name
    with urllib.request.urlopen(req, timeout=60) as r:
        out.write_bytes(r.read())
    print(out_name, out.stat().st_size, "bytes")


def gen_s19_chart_v3():
    """Веса внимания на 7 токенов нового примера («он был голоден»):
    лидер «Кот» gold — мужской род «он» указывает на «Кот»."""
    labels = ["Кот", "съел", "мышь", "потому что", "он", "был", "голоден"]
    vals = [0.40, 0.05, 0.08, 0.06, 0.10, 0.12, 0.19]
    colors = ["#065A82"] * 7
    colors[0] = "#F0AB00"
    cfg = {
        "type": "bar",
        "data": {"labels": labels, "datasets": [{
            "data": vals, "backgroundColor": colors, "borderRadius": 3}]},
        "options": {
            "plugins": {"legend": {"display": False},
                        "datalabels": {"display": False}},
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
    _quickchart(cfg, "s19-attention-weights.png", 980, 400)


def gen_s25_ucurve():
    """Верхний ярус s25: U-кривая lost-in-the-middle (2023, пунктир) vs
    плоская линия needle-retrieval (2026) — «забывание победили»."""
    labels = ["начало", "", "середина документа", "", "конец"]
    cfg = {
        "type": "line",
        "data": {"labels": labels, "datasets": [
            {"label": "2023 — U-кривая (провал середины)",
             "data": [93, 74, 55, 76, 94], "borderColor": "#1C7293",
             "borderDash": [9, 7], "borderWidth": 4, "fill": False,
             "pointRadius": 5, "pointBackgroundColor": "#1C7293",
             "tension": 0.35},
            {"label": "2026 — плоская линия (needle ~99%)",
             "data": [99, 98, 99, 98, 99], "borderColor": "#028090",
             "borderWidth": 5, "fill": False, "pointRadius": 5,
             "pointBackgroundColor": "#028090", "tension": 0.1},
        ]},
        "options": {
            # Шрифты: канвас 1100px показан на слайде в 6.2" →
            # 1px ≈ 0.406pt; минимум 11pt (projector sub-label) ⇒ ≥28px.
            "plugins": {
                "legend": {"position": "bottom",
                           "labels": {"color": "#21295C",
                                       "font": {"size": 28},
                                       "boxWidth": 30}},
                "datalabels": {"display": False},
            },
            "scales": {
                "y": {"min": 40, "max": 105,
                      "title": {"display": True,
                                "text": ["точность поиска", "вставки, %"],
                                "color": "#1C7293", "font": {"size": 28}},
                      "ticks": {"color": "#1C7293", "font": {"size": 28}},
                      "grid": {"color": "#E5EAF0"}},
                "x": {"ticks": {"color": "#21295C", "font": {"size": 28},
                                "maxRotation": 0, "minRotation": 0},
                      "grid": {"display": False}},
            },
        },
    }
    _quickchart(cfg, "s25-ucurve.png", 1100, 330)


S14_SPACE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="300" viewBox="0 0 360 300">
  <!-- «звёздная карта»: облако точек-звёзд, близость = похожесть смысла -->
  <rect x="4" y="4" width="352" height="292" rx="18" fill="#21295C"/>
  <!-- созвездие 1 (кластер) -->
  <g fill="#F4F7FA">
    <circle cx="80" cy="80" r="7"/>
    <circle cx="120" cy="60" r="5"/>
    <circle cx="110" cy="105" r="6"/>
    <circle cx="150" cy="90" r="4"/>
  </g>
  <path d="M80 80 L120 60 L150 90 L110 105 Z" stroke="#1C7293" stroke-width="2" fill="none" opacity="0.8"/>
  <!-- созвездие 2 (кластер) -->
  <g fill="#F4F7FA">
    <circle cx="95" cy="215" r="6"/>
    <circle cx="140" cy="235" r="7"/>
    <circle cx="130" cy="190" r="4"/>
  </g>
  <path d="M95 215 L130 190 L140 235" stroke="#028090" stroke-width="2" fill="none" opacity="0.85"/>
  <!-- одинокая gold-звезда (выброс) -->
  <g>
    <circle cx="285" cy="140" r="9" fill="#F0AB00"/>
    <path d="M285 118 L285 105 M285 162 L285 175 M263 140 L250 140 M307 140 L320 140" stroke="#F0AB00" stroke-width="3" stroke-linecap="round"/>
  </g>
  <!-- мелкие фоновые звёзды -->
  <g fill="#1C7293">
    <circle cx="220" cy="60" r="3"/>
    <circle cx="250" cy="230" r="3"/>
    <circle cx="190" cy="160" r="2.5"/>
    <circle cx="60" cy="155" r="2.5"/>
    <circle cx="310" cy="70" r="2.5"/>
  </g>
  <text x="180" y="282" font-family="DejaVu Sans" font-size="17" fill="#F4F7FA" text-anchor="middle" font-style="italic">рядом на карте = близко по смыслу</text>
</svg>"""


def gen_s14_space():
    render(S14_SPACE_SVG, "s14-space")


if __name__ == "__main__":
    gen_s01_meme()
    gen_dividers()
    gen_s31_pot()
    gen_s19_chart_v3()
    gen_s25_ucurve()
    gen_s14_space()
    print("done")
