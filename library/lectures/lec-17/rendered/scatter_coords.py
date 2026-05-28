"""
scatter_coords.py — MASTER coordinate system for the Лекция 17 signature visual.

ONE source of truth for the 2D scatter «Применимость ИИ × Автономия L0→L5».
Reused IDENTICALLY across 7 scatter slides (progressive reveal = same plane,
layers added):
  s01 — hero (full 18 points, no annotations, Ocean gradient bg)
  s03 — empty axes + 4 labeled quadrants (no points)
  s22 — batch 1 (4 points)
  s23 — batch 1+2 (8 points)
  s24 — batch full (~18 points, L13 trio + bimodal highlighted)
  s28 — empty quadrants highlighted (lower-right warning)
  s38 — A1 master poster (full, quadrant color zones)

COORDINATE CONVENTION (normalized 0..1):
  x = Применимость ИИ (AI fit): 0 = детерминированный non-AI → 1 = full AI
  y = Автономия L0→L5: 0 = L0 (человек делает всё) → 1 = L5 (полная автономия)

MODULE COLOR CODING (P1: navy/teal/gold = three distinguishable):
  M1 (L1-L8)   → #21295C Ocean primary DEEP (navy)
  M2 (L9-L12)  → #028090 Teal secondary
  M3 (L13-L17) → #F0AB00 Gold highlight

Bimodal industries get MULTIPLE points (L10 agro, L13 logistics, L15 science).

CANON quadrant geometry (Phase 8a chapter v3, source of truth):
  upper-right (high fit + high autonomy)  = closed-loop SUCCESS (green)
  upper-left  (low fit  + high autonomy)  = WARNING / empty-dangerous (gold/red)
  lower-right (high fit + low  autonomy)  = CAPPED / regulatory ceiling, FILLED (blue)
  lower-left  (low fit  + low  autonomy)  = classical / non-AI (grey)
"""

# Module colors (hex, no '#')
M1 = "21295C"   # L1-L8 (navy — P1 contrast fix)
M2 = "028090"   # L9-L12 (teal)
M3 = "F0AB00"   # L13-L17 (gold)

# Each point: (key, x, y, module_color, short_label, batch, kind)
#   batch: 1 = s22 starter, 2 = s23 middle, 3 = s24 final
#   kind: "ok" (success/closed-loop), "fail" (open-env failure),
#         "capped" (regulatory-capped), "near0" (black-swan / classical)
# Layout logic (CANON — Phase 8a chapter v3):
#   - closed-loop успехи: upper-right (high fit, high autonomy)
#   - regulatory-capped:  lower-right (high fit, autonomy regulator-capped → low-y)
#   - open-env провалы:   upper-left (low fit + ATTEMPTED high autonomy → high-y, low-x)
#   - classical wins / black-swan: lower-left / near origin

# Labels are INDUSTRY-NAMED (no lecture L-codes — visible-layer rule).
POINTS = [
    # --- BATCH 1 (s20) — 4 starter points, one per family ---
    ("L4_SE",      0.92, 0.78, M1, "разработка ПО",         1, "ok"),
    ("L5_fin",     0.78, 0.62, M1, "финансы (фрод)",        1, "ok"),
    ("L7_med",     0.70, 0.30, M1, "медицина",              1, "capped"),
    ("L9_aero",    0.66, 0.40, M2, "авиакосмос",            1, "capped"),

    # --- BATCH 2 (s21) — +4 middle, incl. bimodal agro ---
    ("L6_cad",     0.50, 0.34, M1, "CAD/CAM",               2, "capped"),
    ("L8_creat",   0.62, 0.55, M1, "креатив",               2, "ok"),
    # agro BIMODAL: See & Spray (closed-loop success, UR) vs
    # Monarch (open-field — attempted high autonomy at low fit → WARNING upper-left)
    ("L10_seespray", 0.86, 0.72, M2, "See & Spray",         2, "ok"),
    ("L10_monarch",  0.27, 0.74, M2, "Monarch (провал)",    2, "fail"),
    ("L11_manuf",  0.55, 0.42, M2, "производство",          2, "capped"),

    # --- BATCH 3 (s22) — final set + logistics trio ---
    ("L12_auto",   0.60, 0.50, M2, "автоматизация",         3, "ok"),
    # logistics TRIO: warehouse L4 closed-loop (UR), urban robotaxi (open
    # environment — attempted autonomy at low fit → WARNING upper-left),
    # black swan L0 near origin (lower-left classical/human).
    ("L13_wh",     0.90, 0.82, M3, "склад (Symbotic)",      3, "ok"),
    ("L13_taxi",   0.34, 0.70, M3, "робот-такси",           3, "fail"),
    ("L13_swan",   0.20, 0.10, M3, "чёрный лебедь",         3, "near0"),
    ("L14_cyber",  0.66, 0.32, M3, "кибербез",              3, "capped"),
    # science BIMODAL: AlphaFold closed-world (UR) vs
    # Galactica (open-world hypothesis — attempted autonomy at low fit → WARNING upper-left)
    ("L15_alpha",  0.88, 0.66, M3, "AlphaFold",             3, "ok"),
    ("L15_galac",  0.30, 0.66, M3, "Galactica (провал)",    3, "fail"),
    ("L16_oil",    0.46, 0.30, M3, "нефтегаз",              3, "capped"),
]

# Convenience accessors -------------------------------------------------
def points_in_batches(max_batch):
    """Return points whose batch <= max_batch (progressive reveal)."""
    return [p for p in POINTS if p[5] <= max_batch]


def all_points():
    return list(POINTS)


# Quadrant labels (for s03 keystone reveal + s38 zones) -----------------
# (label, x_center, y_center, descriptor)
# CANON (Phase 8a chapter v3):
#   UR = closed-loop success | UL = WARNING (low fit + high autonomy) |
#   LR = CAPPED (high fit + low autonomy, regulatory ceiling — FILLED) |
#   LL = classical / non-AI.
QUADRANTS = {
    "UR": ("AI работает и автономно", 0.78, 0.80, "зрелые успехи"),
    "UL": ("зона предупреждения", 0.22, 0.80, "низкая применимость × высокая автономия"),
    "LL": ("«классика выигрывает»", 0.22, 0.18, "AI не нужен"),
    "LR": ("AI работает, автономия ограничена", 0.78, 0.18, "регулятором"),
}
