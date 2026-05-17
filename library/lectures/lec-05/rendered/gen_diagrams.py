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


def person(cx, cy, r, fill, ring=DEEP):
    """Geometric person glyph (rsvg has no emoji font) — head + shoulders
    clipped to a circle badge."""
    cid = f"clip{abs(int(cx*7+cy*13)):x}"
    head_r = r * 0.34
    return (
        f'<defs><clipPath id="{cid}">'
        f'<circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath></defs>'
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
        f'stroke="{ring}" stroke-width="3"/>'
        f'<g clip-path="url(#{cid})">'
        f'<circle cx="{cx}" cy="{cy - r*0.30}" r="{head_r}" '
        f'fill="#FFFFFF"/>'
        f'<ellipse cx="{cx}" cy="{cy + r*0.78}" rx="{r*0.62}" '
        f'ry="{r*0.58}" fill="#FFFFFF"/></g>')


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


# ---- d16: credit inspector — reason codes line-by-line (chapter §3.3) ----
def d16():
    W, H = 1180, 470
    parts = [f'<rect width="{W}" height="{H}" fill="none"/>']
    # LEFT — interpretable inspector (shows the calculation)
    parts.append(
        f'<rect x="14" y="14" width="556" height="{H-28}" rx="18" '
        f'fill="{SURF}" stroke="{TEAL}" stroke-width="3"/>')
    parts.append(
        f'<circle cx="92" cy="86" r="34" fill="{TEAL}"/>'
        f'<text x="92" y="96" font-family="{FONT}" font-size="34" '
        f'fill="#FFFFFF" font-weight="700" text-anchor="middle">✓</text>')
    parts.append(
        f'<text x="148" y="72" font-family="{FONT}" font-size="24" '
        f'font-weight="700" fill="{DEEP}">Интерпретируемая модель</text>'
        f'<text x="148" y="102" font-family="{FONT}" font-size="19" '
        f'fill="{SLATE}">инспектор показывает расчёт построчно</text>')
    codes = [
        ("Высокая долговая нагрузка", "−18"),
        ("Короткая кредитная история", "−9"),
        ("Стабильная занятость", "+6"),
    ]
    cy = 160
    for lab, w in codes:
        col = GOLD if w.startswith("−") else MID
        parts.append(
            f'<rect x="44" y="{cy}" width="496" height="62" rx="10" '
            f'fill="#FFFFFF" stroke="{GREY}" stroke-width="1.5"/>')
        parts.append(
            f'<text x="66" y="{cy+39}" font-family="{FONT}" font-size="20" '
            f'fill="{DEEP}">{lab}</text>')
        parts.append(
            f'<text x="516" y="{cy+39}" font-family="{FONT}" font-size="23" '
            f'font-weight="700" fill="{col}" text-anchor="end">{w}</text>')
        cy += 74
    parts.append(
        f'<text x="292" y="442" font-family="{FONT}" font-size="20" '
        f'font-weight="700" fill="{TEAL}" text-anchor="middle">'
        f'«Отказ: причина — долговая нагрузка» (reason codes)</text>')
    # RIGHT — black box (says "no", refuses to explain)
    parts.append(
        f'<rect x="610" y="14" width="556" height="{H-28}" rx="18" '
        f'fill="{SURF}" stroke="{GOLD}" stroke-width="3"/>')
    parts.append(
        f'<rect x="660" y="150" width="456" height="150" rx="14" '
        f'fill="{DEEP}"/>')
    parts.append(
        f'<text x="888" y="242" font-family="{FONT}" font-size="40" '
        f'font-weight="700" fill="#FFFFFF" text-anchor="middle">'
        f'? ? ?</text>')
    parts.append(
        f'<text x="888" y="72" font-family="{FONT}" font-size="24" '
        f'font-weight="700" fill="{DEEP}" text-anchor="middle">'
        f'Чёрный ящик</text>'
        f'<text x="888" y="102" font-family="{FONT}" font-size="19" '
        f'fill="{SLATE}" text-anchor="middle">говорит «нет», '
        f'объяснить отказывается</text>')
    parts.append(
        f'<text x="888" y="360" font-family="{FONT}" font-size="20" '
        f'font-weight="700" fill="{GOLD}" text-anchor="middle">'
        f'«Отказано». Почему — неизвестно</text>'
        f'<text x="888" y="392" font-family="{FONT}" font-size="18" '
        f'fill="{SLATE}" text-anchor="middle">'
        f'в регулируемой отрасли недопустимо по закону</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
           f'height="{H}" viewBox="0 0 {W} {H}">' + "".join(parts) + "</svg>")
    render("d16-inspector-reason-codes", svg, W, H)


# ---- d22: grounding — student guesses vs opens reference (chapter §4.3) ----
def d22():
    W, H = 1180, 430
    parts = [f'<rect width="{W}" height="{H}" fill="none"/>']
    # LEFT — without grounding (confident guess)
    parts.append(
        f'<rect x="14" y="14" width="556" height="{H-28}" rx="18" '
        f'fill="{SURF}" stroke="{GOLD}" stroke-width="3"/>')
    parts.append(
        f'<text x="292" y="58" font-family="{FONT}" font-size="23" '
        f'font-weight="700" fill="{DEEP}" text-anchor="middle">'
        f'Без grounding</text>')
    parts.append(person(120, 190, 44, GOLD))
    parts.append(
        f'<path d="M196 150 h300 v96 h-220 l-40 34 v-34 h-40 z" '
        f'fill="#FFFFFF" stroke="{GOLD}" stroke-width="2"/>')
    parts.append(
        f'<text x="346" y="188" font-family="{FONT}" font-size="20" '
        f'fill="{DEEP}" text-anchor="middle">«Ставка примерно</text>'
        f'<text x="346" y="216" font-family="{FONT}" font-size="20" '
        f'fill="{DEEP}" text-anchor="middle">7,5%…» (уверенно)</text>')
    parts.append(
        f'<text x="292" y="332" font-family="{FONT}" font-size="20" '
        f'font-weight="700" fill="{GOLD}" text-anchor="middle">'
        f'правдоподобно ≠ верно</text>'
        f'<text x="292" y="364" font-family="{FONT}" font-size="18" '
        f'fill="{SLATE}" text-anchor="middle">'
        f'источник — статистика обучающего текста</text>')
    # RIGHT — with grounding (opens the reference first)
    parts.append(
        f'<rect x="610" y="14" width="556" height="{H-28}" rx="18" '
        f'fill="{SURF}" stroke="{TEAL}" stroke-width="3"/>')
    parts.append(
        f'<text x="888" y="58" font-family="{FONT}" font-size="23" '
        f'font-weight="700" fill="{DEEP}" text-anchor="middle">'
        f'С grounding</text>')
    parts.append(person(716, 190, 44, TEAL))
    # open reference book (drawn, not glyph)
    parts.append(
        f'<rect x="800" y="138" width="118" height="118" rx="8" '
        f'fill="#FFFFFF" stroke="{MID}" stroke-width="2.5"/>'
        f'<line x1="859" y1="138" x2="859" y2="256" stroke="{MID}" '
        f'stroke-width="2.5"/>'
        f'<line x1="814" y1="166" x2="850" y2="166" stroke="{LIGHT}" '
        f'stroke-width="3"/><line x1="814" y1="190" x2="850" y2="190" '
        f'stroke="{LIGHT}" stroke-width="3"/><line x1="814" y1="214" '
        f'x2="850" y2="214" stroke="{LIGHT}" stroke-width="3"/>'
        f'<line x1="868" y1="166" x2="904" y2="166" stroke="{GOLD}" '
        f'stroke-width="3.5"/><line x1="868" y1="190" x2="904" y2="190" '
        f'stroke="{LIGHT}" stroke-width="3"/><line x1="868" y1="214" '
        f'x2="904" y2="214" stroke="{LIGHT}" stroke-width="3"/>')
    parts.append(
        f'<path d="M946 150 h188 v96 h-120 l-34 30 v-30 h-34 z" '
        f'fill="#FFFFFF" stroke="{TEAL}" stroke-width="2"/>'
        f'<text x="1040" y="190" font-family="{FONT}" font-size="19" '
        f'fill="{DEEP}" text-anchor="middle">«По тарифу</text>'
        f'<text x="1040" y="216" font-family="{FONT}" font-size="19" '
        f'fill="{DEEP}" text-anchor="middle">с.12: 8,3%»</text>')
    parts.append(
        f'<text x="888" y="332" font-family="{FONT}" font-size="20" '
        f'font-weight="700" fill="{TEAL}" text-anchor="middle">'
        f'сначала открыл справочник → потом ответил</text>'
        f'<text x="888" y="364" font-family="{FONT}" font-size="18" '
        f'fill="{SLATE}" text-anchor="middle">'
        f'источник — проверяемый документ (можно показать)</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
           f'height="{H}" viewBox="0 0 {W} {H}">' + "".join(parts) + "</svg>")
    render("d22-grounding-student", svg, W, H)


# ---- d26b: three sellers analogy (collaborative / content / hybrid) ----
def d26b():
    W, H = 1180, 360
    parts = [f'<rect width="{W}" height="{H}" fill="none"/>']
    sellers = [
        (MID, "Collaborative",
         "«Брали то же, что вы —", "ещё взяли вот это»",
         "помнит ПАТТЕРН поведения,", "не знает товар"),
        (TEAL, "Content-based",
         "«Похоже по описанию", "на вашу любимую вещь»",
         "знает КАТАЛОГ наизусть,", "не знает толпу"),
        (DEEP, "Hybrid",
         "«И что брали похожие,", "и что похоже + контекст»",
         "совмещает оба + ситуацию", "(вечер пятницы, телефон)"),
    ]
    cw = 372
    for i, (col, name, q1, q2, d1, d2) in enumerate(sellers):
        x = 20 + i * (cw + 14)
        parts.append(
            f'<rect x="{x}" y="14" width="{cw}" height="{H-28}" rx="16" '
            f'fill="{SURF}" stroke="{col}" stroke-width="3"/>')
        parts.append(person(x + 58, 74, 34, col))
        parts.append(
            f'<text x="{x+108}" y="84" font-family="{FONT}" font-size="24" '
            f'font-weight="700" fill="{col}">{name}</text>')
        parts.append(
            f'<text x="{x+30}" y="158" font-family="{FONT}" font-size="20" '
            f'fill="{DEEP}">{q1}</text>'
            f'<text x="{x+30}" y="186" font-family="{FONT}" font-size="20" '
            f'fill="{DEEP}">{q2}</text>')
        parts.append(
            f'<rect x="{x+22}" y="224" width="{cw-44}" height="96" rx="10" '
            f'fill="#FFFFFF" stroke="{GREY}" stroke-width="1.5"/>'
            f'<text x="{x+38}" y="262" font-family="{FONT}" '
            f'font-size="18" fill="{SLATE}">{d1}</text>'
            f'<text x="{x+38}" y="290" font-family="{FONT}" '
            f'font-size="18" fill="{SLATE}">{d2}</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
           f'height="{H}" viewBox="0 0 {W} {H}">' + "".join(parts) + "</svg>")
    render("d26b-three-sellers", svg, W, H)


# ---- d31: password can be changed, face cannot (chapter §6.3) ----
def d31():
    W, H = 1480, 360
    parts = [f'<rect width="{W}" height="{H}" fill="none"/>']
    # LEFT — password leaked → can rotate (reversible)
    parts.append(
        f'<rect x="14" y="14" width="690" height="{H-28}" rx="18" '
        f'fill="{SURF}" stroke="{TEAL}" stroke-width="3"/>')
    parts.append(
        f'<text x="359" y="58" font-family="{FONT}" font-size="26" '
        f'font-weight="700" fill="{DEEP}" text-anchor="middle">'
        f'Пароль</text>')
    parts.append(
        f'<rect x="180" y="98" width="360" height="84" rx="12" '
        f'fill="#FFFFFF" stroke="{MID}" stroke-width="2.5"/>'
        f'<text x="360" y="154" font-family="{FONT}" font-size="34" '
        f'fill="{MID}" font-weight="700" text-anchor="middle">'
        f'••••••••</text>')
    parts.append(
        f'<text x="359" y="248" font-family="{FONT}" font-size="46" '
        f'fill="{TEAL}" text-anchor="middle">↻</text>')
    parts.append(
        f'<text x="359" y="312" font-family="{FONT}" font-size="25" '
        f'font-weight="700" fill="{TEAL}" text-anchor="middle">'
        f'Утёк → сменил. ОБРАТИМО</text>')
    # vs
    parts.append(
        f'<text x="740" y="200" font-family="{FONT}" font-size="34" '
        f'font-weight="700" fill="{SLATE}" text-anchor="middle">vs</text>')
    # RIGHT — biometrics leaked → cannot reissue (irreversible)
    parts.append(
        f'<rect x="776" y="14" width="690" height="{H-28}" rx="18" '
        f'fill="{SURF}" stroke="{GOLD}" stroke-width="3"/>')
    parts.append(
        f'<text x="1121" y="58" font-family="{FONT}" font-size="26" '
        f'font-weight="700" fill="{DEEP}" text-anchor="middle">'
        f'Лицо / отпечаток</text>')
    parts.append(
        f'<circle cx="1121" cy="148" r="52" fill="#FFFFFF" '
        f'stroke="{GOLD}" stroke-width="3.5"/>'
        f'<circle cx="1103" cy="136" r="6" fill="{DEEP}"/>'
        f'<circle cx="1139" cy="136" r="6" fill="{DEEP}"/>'
        f'<path d="M1098 164 Q1121 185 1144 164" fill="none" '
        f'stroke="{DEEP}" stroke-width="4.5" stroke-linecap="round"/>')
    parts.append(
        f'<text x="1121" y="252" font-family="{FONT}" font-size="44" '
        f'font-weight="700" fill="{GOLD}" text-anchor="middle">✕</text>')
    parts.append(
        f'<text x="1121" y="312" font-family="{FONT}" font-size="25" '
        f'font-weight="700" fill="{GOLD}" text-anchor="middle">'
        f'Утекло → новое не выдать. НЕОБРАТИМО</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
           f'height="{H}" viewBox="0 0 {W} {H}">' + "".join(parts) + "</svg>")
    render("d31-password-vs-face", svg, W, H)


if __name__ == "__main__":
    d08()
    d11()
    d26()
    d16()
    d22()
    d26b()
    d31()
