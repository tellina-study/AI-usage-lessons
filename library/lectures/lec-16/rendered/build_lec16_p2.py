"""
Part 2 of Lec-16 build — sections 4-7 (s28-s42).
Imports helpers from build_lec16.py.
"""
from build_lec16 import *


# ====================================================================
# SECTION 4: Q4 energy transition (s28-s33)
# ====================================================================

def s28_q4_divider(p):
    return section_divider(
        p, "Q4", "Энергопереход: CCS + EGS",
        "Здесь AI и физика буксуют вместе. Long-horizon, low-data, low-physics-certainty. Самый честный квадрант.",
        "2 рабочих пилота · 2 структурных провала · 190× разрыв масштабирования",
        section_idx=4, large_size=200, label_color=GOLD)


def s29_northern_lights(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Northern Lights CCS — 0,02% от needed scale",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "JV Equinor + Shell + TotalEnergies. Commercial launch 2024. Эугарден, Норвегия.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    img = ASSETS / "screenshots" / "s29-nl.png"
    add_image_aspect(slide, img, 0.65, 2.0, 5.7, 4.0)
    attribution(slide, "Northern Lights JV · 2024", x=0.65, y=6.05, w=5.7)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("Метрики Northern Lights:", {"size": 14, "bold": True, "color": MID}),
        ("· Phase 1 capacity: 1,5 Mt CO₂/год", {"size": 12, "color": DEEP}),
        ("· Operational с 2024", {"size": 12, "color": DEEP}),
        ("· CO₂ источники: Microsoft, Heidelberg Materials, Yara", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Сравнение со scale:", {"size": 14, "bold": True, "color": MID}),
        ("1,5 Mt/год", {"size": 24, "bold": True, "color": LIGHT}),
        ("vs", {"size": 14, "color": SLATE}),
        ("7 600 Mt/год (IEA target 2050)", {"size": 24, "bold": True, "color": GOLD}),
        ("", {"size": 4}),
        ("= 0,02% от needed scale", {"size": 14, "bold": True, "color": RED_WARN}),
        ("= 190× scale-up gap к 2050", {"size": 12, "color": DEEP, "italic": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "AI helps per-unit cost (subsurface modeling, leak detection). AI НЕ масштабирует индустрию — нужно 5000+ Northern Lights к 2050.",
                 size=12)
    add_notes(slide, "См. slides/s29-northern-lights-ccs.md speaker notes.")


def s30_fervo_egs(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Fervo Energy EGS — IPO 12 мая 2026, 40× growth ceiling",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Только renewable baseload, доступный при сегодняшних технологиях. Driver: AI workloads потребляют 24/7 stable power.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    img = ASSETS / "screenshots" / "s30-fervo2.jpg"
    add_image_aspect(slide, img, 0.65, 2.0, 5.7, 3.5)
    attribution(slide, "Fervo Energy / Cape Station Utah · 2026", x=0.65, y=5.55, w=5.7)
    img2 = ASSETS / "charts" / "s30-fervo-gap.png"
    add_image_aspect(slide, img2, 0.65, 5.85, 5.7, 0.45)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("IPO 12 мая 2026:", {"size": 14, "bold": True, "color": MID}),
        ("$1,89 млрд", {"size": 28, "bold": True, "color": GOLD}),
        ("привлечено в IPO; оценка $7,7 млрд", {"size": 12, "italic": True, "color": DEEP}),
        ("", {"size": 6}),
        ("Cape Station Utah ($206M):", {"size": 13, "bold": True, "color": MID}),
        ("· Pilot 2024 → commercial 2026", {"size": 12, "color": DEEP}),
        ("· Distributed temperature sensing", {"size": 12, "color": DEEP}),
        ("· Hydraulic fracking → закрытый цикл", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Driver:", {"size": 13, "bold": True, "color": MID}),
        ("· Google, Microsoft, Meta — PPA buyers", {"size": 12, "color": DEEP}),
        ("· AI data centers → 24/7 clean baseload", {"size": 12, "color": DEEP}),
        ("· US EGS potential 150 GW vs current 3,7 GW", {"size": 12, "color": GOLD, "bold": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Closed-loop: AI tech tycoons спонсируют EGS чтобы запитать AI data centers. Self-referential AI infrastructure expansion cycle.",
                 size=12)
    add_notes(slide, "См. slides/s30-fervo-egs.md speaker notes.")


def s31_ccs_scale_gap(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "CCS 190× scale-up gap — engineering reality vs policy",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "AI helps per-unit cost. AI не масштабирует индустрию. AI на 100-летнем horizon — hallucinate easy.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    img = ASSETS / "charts" / "s29-ccs-gap.png"
    add_image_aspect(slide, img, 0.7, 2.0, 5.6, 4.2)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("Что AI hallucinates на 100-летнем horizon:", {"size": 13, "bold": True, "color": MID}),
        ("· Plume migration CO₂ через 50-100 лет", {"size": 11, "color": DEEP}),
        ("· Multi-phase flow в неизвестных формациях", {"size": 11, "color": DEEP}),
        ("· Caprock integrity — out-of-distribution scenarios", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("Gartner 2027 prediction:", {"size": 13, "bold": True, "color": MID}),
        ("40%", {"size": 28, "bold": True, "color": GOLD}),
        ("agentic AI проектов будут отменены к 2027", {"size": 12, "italic": True, "color": DEEP}),
        ("", {"size": 4}),
        ("Sleipner Norway 1996:", {"size": 13, "bold": True, "color": MID}),
        ("· Oldest CCS, $1B+ инвестиций", {"size": 11, "color": DEEP}),
        ("· 30 лет данных — empirical baseline", {"size": 11, "color": DEEP}),
        ("· AI augmentation — да; AI prediction 100 лет — нет.", {"size": 11, "color": DEEP, "bold": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Inverse atmospheric problem на 100-летнем horizon = AI hallucination easy. Physics-informed neural networks (PINN) — research-grade, не commercial.",
                 size=12)
    add_notes(slide, "См. slides/s31-ccs-scale-gap-hallucination.md speaker notes.")


def s32_refinery_q4(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Refinery plant-wide stagnation = Q4 структурная проблема",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Multi-physics (mass + energy + reaction + corrosion) ломает ML-суррогаты на edge cases.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 5.5, 4.45)
    img = ASSETS / "screenshots" / "s33-honeywell.jpg"
    add_image_aspect(slide, img, 0.65, 2.0, 5.2, 4.1)
    attribution(slide, "Honeywell Process Solutions · 2025", x=0.65, y=6.10, w=5.2)
    rounded_box(slide, 6.2, 1.85, 6.63, 4.45)
    multiline_box(slide, 6.4, 1.95, 6.3, 4.3, [
        ("Yokogawa Idemitsu case:", {"size": 14, "bold": True, "color": MID}),
        ("· 2018+: single-column distillation pilot — success", {"size": 12, "color": DEEP}),
        ("· Plant-wide пилот → тихо закрыт [VFY-day-of]", {"size": 12, "color": RED_WARN}),
        ("", {"size": 6}),
        ("Многоюнитная координация:", {"size": 14, "bold": True, "color": MID}),
        ("· 100+ units в типичном НПЗ", {"size": 12, "color": DEEP}),
        ("· Mass + energy + reaction + corrosion = 4 physics", {"size": 12, "color": DEEP}),
        ("· ML суррогат breaks на feedstock shift, season swing", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Field life vs ML decay:", {"size": 14, "bold": True, "color": MID}),
        ("40-50 лет field life", {"size": 16, "bold": True, "color": LIGHT}),
        ("vs 1-2 года ML model decay", {"size": 16, "bold": True, "color": GOLD}),
        ("Retraining cost > benefit на edge cases.", {"size": 11, "color": DEEP, "italic": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Это не Q1 failure — это Q4-структурный. Multi-physics + long horizon + frequent retraining = ML-суррогат не выживает.",
                 size=12)
    add_notes(slide, "См. slides/s32-refinery-q4-stagnation.md speaker notes.")


def s33_q4_alternatives_sis(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Альтернатива Q4: classical engineering + deterministic safety",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "3 категории. Для regulatory submissions — physics-traceable mandatory. AI не accept.",
             size=13, italic=True, color=LIGHT)
    alts = [
        ("Physics для CCS / геомеханики", "Eclipse / INTERSECT / CMG GEM /\nVisage / Abaqus / Plaxis.\nPlume migration 100 лет — physics-based mandatory.", MID),
        ("Classical APC для refinery", "Honeywell Profit Controller /\nEmerson DeltaV / AspenTech aspenONE.\nMPC + RTO — proven 30 лет, не AI.", LIGHT),
        ("SIS для safety-critical", "SIL3/SIL4 по IEC 61511.\n3oo2 voting + periodic proof tests.\nML НЕ сертифицируется.\nDeepwater Horizon 2010 — alarm bypass anchor.", GOLD),
    ]
    a_w = 4.05
    a_h = 4.5
    gap = 0.1
    x0 = 0.5
    y0 = 1.85
    for i, (name, body, accent) in enumerate(alts):
        x = x0 + i * (a_w + gap)
        rounded_box(slide, x, y0, a_w, a_h, stroke=accent, stroke_w=2)
        rectangle(slide, x, y0, a_w, 0.85, fill=accent)
        text_box(slide, x+0.15, y0, a_w-0.3, 0.85, name,
                 size=13, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x+0.2, y0+1.0, a_w-0.4, a_h - 1.15, body,
                 size=12, color=DEEP, line_spacing=1.4)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "SIL3 = 0,001–0,0001 PFD (probability of failure on demand). ML модель не воспроизводимо проверяемая под IEC 61511. Engineering rule.",
                 size=12)
    add_notes(slide, "См. slides/s33-q4-alternatives-sis.md speaker notes.")


# ====================================================================
# SECTION 5: Россия (s34-s36)
# ====================================================================

def s34_russia_divider(p):
    """s34 — Russia section divider with mini-matrix."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    roadmap_bar(slide, current_section=5)
    text_box(slide, 0.5, 0.7, 12.33, 0.85,
             "Россия — sanctions, insourcing, vertical integration",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.5, 12.33, 0.4,
             "По 4 квадрантам keystone-матрицы. После марта 2022 — структурный shift.",
             size=13, italic=True, color=LIGHT)
    # Mini-matrix Russia x Quadrants
    quads = [
        ("Q1 Mature", "Роснефть Digital Field\nна Башнефть Илишевское\n+1 Mt/год нефти", MID),
        ("Q3 Frontier", "Газпром нефть Cognitive Geo\nс IBM Research Brazil 2019–2022\n→ internal post-IBM exit", LIGHT),
        ("Q2 Methane", "EU 2024/1787 не применяется\nкомпаниям РФ через imports\ncompliance с 2027", TEAL),
        ("Q4 Transition", "CCS / EGS — ограниченные\nпилоты. Sanctions blockуют\nclosed-loop AI infrastructure", GOLD),
    ]
    q_w = 6.0
    q_h = 2.0
    gap = 0.2
    x0 = 0.5
    y0 = 2.0
    for i, (name, body, accent) in enumerate(quads):
        col = i % 2
        row = i // 2
        x = x0 + col * (q_w + gap)
        y = y0 + row * (q_h + gap)
        rounded_box(slide, x, y, q_w, q_h, stroke=accent, stroke_w=2)
        rectangle(slide, x, y, 0.15, q_h, fill=accent)
        text_box(slide, x + 0.3, y + 0.1, q_w - 0.4, 0.5, name,
                 size=14, bold=True, color=DEEP)
        text_box(slide, x + 0.3, y + 0.6, q_w - 0.4, q_h - 0.7, body,
                 size=11, color=DEEP, line_spacing=1.35)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Vertical integration — необходимость, не выбор. Российский путь ближе к Sinopec / CNOOC, чем к Aramco / ExxonMobil vendor-based.",
                 size=12)
    add_notes(slide, "См. slides/s34-russia-divider.md speaker notes.")


def s35_gazprom_cognitive_geo(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Газпром нефть Cognitive Geologist — flagship российский Q3",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "С IBM Research Brazil 2019–2022 → internal development после ухода IBM. Survived where BP+Beyond Limits + IBM+Repsol failed.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    multiline_box(slide, 0.7, 1.95, 5.7, 4.3, [
        ("Метрики Cognitive Geo:", {"size": 14, "bold": True, "color": MID}),
        ("", {"size": 6}),
        ("Геология цикл:", {"size": 13, "bold": True, "color": DEEP}),
        ("3-4 месяца → минуты", {"size": 22, "bold": True, "color": GOLD}),
        ("", {"size": 6}),
        ("Ямал 2024:", {"size": 13, "bold": True, "color": DEEP}),
        ("· First oil из нового поля", {"size": 12, "color": DEEP}),
        ("· Cut twofold время до first oil", {"size": 12, "color": DEEP}),
        ("· +40% projects к 2030 (target)", {"size": 12, "color": DEEP, "bold": True}),
        ("", {"size": 6}),
        ("Структурный success:", {"size": 13, "bold": True, "color": MID}),
        ("Узкая задача (seismic preview) + measurable baseline (months → minutes) + senior expert QC.", {"size": 11, "color": DEEP, "italic": True}),
    ], line_spacing=1.25)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("AIQ partnership:", {"size": 14, "bold": True, "color": MID}),
        ("· ADNOC + G42 + Presight joint venture", {"size": 12, "color": DEEP}),
        ("· AIQ оценка ~$1,4 млрд+ (2025)", {"size": 12, "color": DEEP, "bold": True}),
        ("· Aramco + Groq sister AI deal", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Контраст с failures:", {"size": 13, "bold": True, "color": MID}),
        ("· BP + Beyond Limits — single vendor + cognitive overpromise", {"size": 11, "color": DEEP}),
        ("· IBM + Repsol — general-purpose в narrow domain", {"size": 11, "color": DEEP}),
        ("· Cognitive Geo — narrow task + custom + senior QC = успех.", {"size": 11, "color": DEEP, "bold": True}),
        ("", {"size": 6}),
        ("Caveat:", {"size": 13, "bold": True, "color": GOLD}),
        ("Российские KPI = self-reported. Тот же caveat что Aramco.", {"size": 11, "color": DEEP, "italic": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Структурный паттерн success Q3: узкая задача + measurable baseline + senior expert QC. Anthropomorphic framing («AI имитирует геолога») = красный флаг.",
                 size=12)
    add_notes(slide, "См. slides/s35-gazprom-cognitive-geo.md speaker notes.")


def s36_rosneft_detail(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Российский Q1: flagship + средний эшелон",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Disclosure gap structural — корпоративные пресс-релизы вместо SEC 10-K mandatory.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    rectangle(slide, 0.5, 1.85, 6.0, 0.55, fill=MID)
    text_box(slide, 0.65, 1.85, 5.7, 0.55, "Роснефть Digital Field детально",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 0.7, 2.55, 5.6, 3.75, [
        ("Башнефть Илишевское flagship:", {"size": 13, "bold": True, "color": MID}),
        ("· 23 продукта (10 коммерциализованных)", {"size": 12, "color": DEEP}),
        ("· +1 Mt/год дополнительной нефти", {"size": 12, "color": DEEP, "bold": True}),
        ("· ~1 млрд ₽/год эффект", {"size": 12, "color": DEEP}),
        ("· +60% удалённо управляемых объектов", {"size": 12, "color": DEEP}),
        ("· +5% энергоэффективности", {"size": 12, "color": DEEP}),
        ("· −5% логистики", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Структурный путь:", {"size": 13, "bold": True, "color": MID}),
        ("· Roxar (Schlumberger) ушёл 2022", {"size": 11, "color": DEEP}),
        ("· Internal development = только путь", {"size": 11, "color": DEEP}),
    ], line_spacing=1.25)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    rectangle(slide, 6.7, 1.85, 6.13, 0.55, fill=LIGHT)
    text_box(slide, 6.85, 1.85, 5.83, 0.55, "Татнефть · ЛУКОЙЛ · Сургутнефтегаз",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 6.9, 2.55, 5.83, 3.75, [
        ("Татнефть:", {"size": 13, "bold": True, "color": MID}),
        ("· АнтиХрупкий программа (resilience-driven)", {"size": 11, "color": DEEP}),
        ("· Нижнекамск НПЗ — partial AI deployment", {"size": 11, "color": DEEP}),
        ("· Public disclosure ограничен", {"size": 11, "color": DEEP, "italic": True}),
        ("", {"size": 6}),
        ("ЛУКОЙЛ:", {"size": 13, "bold": True, "color": MID}),
        ("· Волго-Урал — internal teams без vendor", {"size": 11, "color": DEEP}),
        ("· No detailed KPI публично", {"size": 11, "color": DEEP, "italic": True}),
        ("", {"size": 6}),
        ("Сургутнефтегаз:", {"size": 13, "bold": True, "color": MID}),
        ("· Cognitive Pilot + Sberbank ecosystem", {"size": 11, "color": DEEP}),
        ("· Conservative disclosure", {"size": 11, "color": DEEP, "italic": True}),
        ("", {"size": 6}),
        ("Structural gap:", {"size": 13, "bold": True, "color": GOLD}),
        ("Без mandatory SEC-style reporting — оценка только qualitative.", {"size": 11, "color": DEEP}),
    ], line_spacing=1.2)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Российский Q1 working pattern: NOC + internal teams + узкая задача + measurable baseline. Vendor dependency = риск (Roxar exit 2022).",
                 size=12)
    add_notes(slide, "См. slides/s36-rosneft-detail-other-noc.md speaker notes.")


# ====================================================================
# SECTION 6: Cross-cutting (s37-s38)
# ====================================================================

def s37_cyber_935(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Ransomware на нефтегаз +935% год к году",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Zscaler ThreatLabz 2025 report. Counter-trend AI-расширения — безопасность phase 1, не phase 4.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    img = ASSETS / "charts" / "s37-cyber-935.png"
    add_image_aspect(slide, img, 0.7, 2.0, 5.6, 4.2)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("Colonial Pipeline 2021 anchor:", {"size": 14, "bold": True, "color": MID}),
        ("· VPN account без MFA — единый entry point", {"size": 12, "color": DEEP}),
        ("· DarkSide ransomware → 6 дней shutdown", {"size": 12, "color": DEEP}),
        ("· 50% Восточно-побережной топливной поставки", {"size": 12, "color": DEEP}),
        ("· $4,4M ransom paid (часть recovered)", {"size": 12, "color": DEEP, "bold": True}),
        ("", {"size": 6}),
        ("Защитные AI alternatives:", {"size": 13, "bold": True, "color": MID}),
        ("· Dragos OT security platform", {"size": 11, "color": DEEP}),
        ("· Claroty + Nozomi Networks SCADA monitoring", {"size": 11, "color": DEEP}),
        ("· Cisco SecureX, CrowdStrike Falcon", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("Counter-trend insight:", {"size": 13, "bold": True, "color": GOLD}),
        ("AI расширяет attack surface. Defensive AI (anomaly detection) — необходим, но недостаточен.", {"size": 11, "color": DEEP, "italic": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Безопасность — phase 1 (perimeter + MFA + segmentation), НЕ phase 4 (AI-defense overlay). Сначала basics, потом AI.",
                 size=12)
    add_notes(slide, "См. slides/s37-cyber-935-percent.md speaker notes.")


def s38_2020_crash_deepwater(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Industry cyclicality > AI hype cycle. Deepwater Horizon = anchor.",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "2020 crash 107k jobs за 6 мес + Deepwater Horizon 2010 — два cross-cutting anchor.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    rectangle(slide, 0.5, 1.85, 6.0, 0.55, fill=LIGHT)
    text_box(slide, 0.65, 1.85, 5.7, 0.55, "2020 oil crash",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    img = ASSETS / "charts" / "s38-2020-crash.png"
    add_image_aspect(slide, img, 0.65, 2.5, 5.7, 2.2)
    multiline_box(slide, 0.65, 4.75, 5.7, 1.5, [
        ("107 000 jobs lost за 6 мес = 9,7% индустрии", {"size": 12, "bold": True, "color": GOLD}),
        ("· WTI futures: -$37 (negative) на короткое время", {"size": 11, "color": DEEP}),
        ("· AI программы заморожены на 18-24 мес", {"size": 11, "color": DEEP}),
        ("· Job market не восстановился полностью к 2024", {"size": 11, "color": DEEP}),
    ], line_spacing=1.3)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    rectangle(slide, 6.7, 1.85, 6.13, 0.55, fill=RED_WARN)
    text_box(slide, 6.85, 1.85, 5.83, 0.55, "Deepwater Horizon 2010",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    img2 = ASSETS / "screenshots" / "wm-deepwater-horizon-oil-spill.jpg"
    add_image_aspect(slide, img2, 6.85, 2.5, 5.83, 2.2)
    multiline_box(slide, 6.85, 4.75, 5.83, 1.5, [
        ("11 deaths + $60 млрд = 20% годовой выручки BP", {"size": 12, "bold": True, "color": GOLD}),
        ("· Macondo well blowout — Gulf of Mexico", {"size": 11, "color": DEEP}),
        ("· BOP (противовыбросовый превентор) failure", {"size": 11, "color": DEEP}),
        ("· Alarm bypass culture (Andrea Fleytas testimony)", {"size": 11, "color": DEEP, "bold": True}),
    ], line_spacing=1.3)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "AI roadmap должен stress-test индустриальный цикл и культуру обхода тревог (Alert fatigue → alarm bypass — тот же паттерн на 2 разных шкалах).",
                 size=12)
    add_notes(slide, "См. slides/s38-2020-crash-deepwater.md speaker notes.")


# ====================================================================
# SECTION 7: Closing (s39-s42)
# ====================================================================

def s39_synthesis_matrix(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "4-квадрантный синтез: 10 documented failures + working cases",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Возврат к keystone-матрице. AI в нефтегазе — не одна история, а четыре.",
             size=13, italic=True, color=LIGHT)
    # 4 quadrants with works + fails
    quads = [
        ("Q2 Methane — AI essential", "Работает:\n· MethaneSAT (15,5 мес до loss)\n· Carbon Mapper Tanager-1\n· GHGSat 13-constellation\n· Bridger aerial LiDAR\n\nПровалы (2):\n· MethaneSAT loss 20 июня 2025\n· 4× discrepancy", TEAL),
        ("Q1 Mature — AI мультипликатор", "Работает:\n· Ambyint +15% / 200 wells\n· Honeywell UOP 310+ units\n· Роснефть Digital Field +1 Mt/год\n\nПровалы (2):\n· 86% pilot stuck\n· Aspen Mtell alert fatigue", MID),
        ("Q4 Transition — struggle", "Работает (limited):\n· Northern Lights 1,5 Mt/год\n· Fervo IPO $1,89B\n\nПровалы (2):\n· CCS 190× scale-up gap\n· Refinery plant-wide stagnation", GOLD),
        ("Q3 Frontier — physics-first", "Работает:\n· Eni HPC6 / Aramco METABRAIN\n· SLB Lumi / ExxonMobil Discovery 6\n· Газпром Cognitive Geo\n\nПровалы (2):\n· BP+Beyond Limits 7 лет 0\n· IBM+Repsol Kalimba", LIGHT),
    ]
    q_w = 6.0
    q_h = 2.2
    gap_x = 0.2
    gap_y = 0.15
    x0 = 0.5
    y0 = 1.85
    for i, (name, body, accent) in enumerate(quads):
        col = i % 2
        row = i // 2
        x = x0 + col * (q_w + gap_x)
        y = y0 + row * (q_h + gap_y)
        rounded_box(slide, x, y, q_w, q_h, stroke=accent, stroke_w=2.5)
        rectangle(slide, x, y, q_w, 0.4, fill=accent)
        text_box(slide, x+0.15, y, q_w-0.3, 0.4, name,
                 size=12, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x+0.2, y+0.5, q_w-0.4, q_h-0.6, body,
                 size=9, color=DEEP, line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Когда работает: Q1 multiplier + Q2 essential. Когда осторожно: Q3 augmentation. Когда опасно: Q4 long-horizon + safety-critical SIS.",
                 size=12)
    add_notes(slide, "См. slides/s39-synthesis-matrix.md speaker notes.")


def s40_three_cornerstones(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "3 cornerstone концепта — bridge к Лекции 17",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Каждый — portable на любую следующую отрасль, не только нефтегаз.",
             size=13, italic=True, color=LIGHT)
    corners = [
        ("1", "AI judgment как структурная задача", "Главный навык — не «как запустить AI», а «как определить, применим ли». Для нефтегаза: 2×2 matrix данные × физика. Для любой отрасли: 2-3-мерная таксономия. Без диагностики AI = азартная ставка.", MID),
        ("2", "Альтернатива-как-исходный уровень", "Каждое AI-внедрение имеет параллельный не-AI вариант. Для нефтегаза 6 категорий: Eclipse, Picarro, OGI, classical APC, SIS, federated learning. AI добавляется ТОЛЬКО если улучшает baseline.", TEAL),
        ("3", "Industry cyclicality > AI hype cycle", "2020 oil crash: 107k jobs за 6 мес → AI заморожены 18-24 мес. AI-roadmap должен иметь stress-tested устойчивость против отраслевого цикла. AI не защищает — он эффект усиления.", GOLD),
    ]
    c_w = 12.33
    c_h = 1.55
    gap = 0.1
    x0 = 0.5
    y0 = 1.85
    for i, (num, title, body, accent) in enumerate(corners):
        y = y0 + i * (c_h + gap)
        rounded_box(slide, x0, y, c_w, c_h, stroke=accent, stroke_w=2)
        circle(slide, x0 + 0.15, y + 0.3, 0.9, 0.9, fill=accent)
        text_box(slide, x0 + 0.15, y + 0.3, 0.9, 0.9, num,
                 size=32, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x0 + 1.3, y + 0.15, c_w - 1.5, 0.5, title,
                 size=16, bold=True, color=DEEP)
        text_box(slide, x0 + 1.3, y + 0.7, c_w - 1.5, c_h - 0.85, body,
                 size=12, color=DEEP, line_spacing=1.35)
    gold_callout(slide, 0.5, 6.7, 12.33, 0.55,
                 "Эти три cornerstone — переносимые диагностические инструменты. Лекция 17 — systematization: keystone'ы L11-L16 как universal patterns.",
                 size=12)
    add_notes(slide, "См. slides/s40-three-cornerstones.md speaker notes.")


def s41_qa(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Q&A",
             size=44, bold=True, color=DEEP, line_spacing=1.05)
    text_box(slide, 0.5, 1.4, 12.33, 0.4,
             "3 ключевых вопроса для exit ticket — обсуждаем в малых группах, потом общий слайд.",
             size=14, italic=True, color=LIGHT)
    questions = [
        ("Q1", "Для какого квадранта матрицы данные × физика AI является ESSENTIAL (а не augmentation)? Конкретный case + почему классической физики недостаточно?", TEAL),
        ("Q2", "Приведите 2 documented failure из лекции + выученные уроки. (Любые 2 из 10: BP+Beyond Limits, IBM+Repsol, MethaneSAT loss, 86% pilot stuck, Aspen alert fatigue, 4× discrepancy, CCS 190× gap, refinery stagnation, 2020 crash, cyber +935%.)", LIGHT),
        ("Q3", "Когда в нефтегазе НЕ применять AI — назовите 3 критерия с примерами из 6 на лекции.", GOLD),
    ]
    q_w = 12.33
    q_h = 1.4
    gap = 0.15
    x0 = 0.5
    y0 = 2.0
    for i, (qn, body, accent) in enumerate(questions):
        y = y0 + i * (q_h + gap)
        rounded_box(slide, x0, y, q_w, q_h, stroke=accent, stroke_w=2)
        rectangle(slide, x0, y, 1.3, q_h, fill=accent)
        text_box(slide, x0, y + 0.4, 1.3, 0.6, qn,
                 size=28, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x0 + 1.5, y + 0.15, q_w - 1.7, q_h - 0.3, body,
                 size=12, color=DEEP, line_spacing=1.35, anchor=MSO_ANCHOR.MIDDLE)
    gold_callout(slide, 0.5, 6.75, 12.33, 0.5,
                 "Bonus для семинара: сравните Eni HPC6 ($104M, AMD, Italy) vs ExxonMobil Discovery 6 ($200-400M, NVIDIA, US) vs Aramco METABRAIN (250B params, internal Saudi).",
                 size=12)
    add_notes(slide, "См. slides/s41-qa.md speaker notes.")


def s42_hero_methanesat_map(p):
    """s42 — closing hero: MethaneSAT global methane map."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    # Hero image LEFT (60% width × 5.5" = ~44% area)
    img = ASSETS / "screenshots" / "s42-methanesat.png"
    add_image_aspect(slide, img, 0.5, 0.4, 7.8, 5.4)
    attribution(slide, "EDF / MethaneSAT data via Google Earth Engine · февраль 2026",
                x=0.5, y=5.85, w=7.8)
    # Title + text RIGHT
    multiline_box(slide, 8.4, 0.5, 4.6, 5.5, [
        ("Спутник потерян —", {"size": 22, "bold": True, "color": DEEP}),
        ("карта осталась.", {"size": 26, "bold": True, "color": GOLD}),
        ("", {"size": 12}),
        ("Bittersweet payoff:", {"size": 13, "bold": True, "color": MID}),
        ("· 20 июня 2025 — потеря MethaneSAT", {"size": 11, "color": DEEP}),
        ("· ~2 000 data files за 15,5 мес → retrospective inventory", {"size": 11, "color": DEEP, "italic": True}),
        ("", {"size": 8}),
        ("Final framing:", {"size": 13, "bold": True, "color": MID}),
        ("AI в нефтегазе — это", {"size": 12, "color": DEEP}),
        ("измеримый успех", {"size": 13, "bold": True, "color": DEEP}),
        ("+ структурная уязвимость", {"size": 13, "bold": True, "color": GOLD}),
        ("в одном кадре.", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Хороший инженер строит portfolio reading, не single-quadrant.", {"size": 10, "color": DEEP, "italic": True}),
    ], line_spacing=1.2)
    gold_callout(slide, 0.5, 6.4, 12.33, 0.7,
                 "Bridge к Лекции 17 — systematization. Keystone'ы L11–L16 как universal patterns.",
                 size=14)
    add_notes(slide, "См. slides/s42-hero-methanesat-map.md speaker notes.")


# ====================================================================
# Build orchestration
# ====================================================================

def build_all():
    """Assemble full 43-slide deck."""
    p = setup_pres()
    # Section 0 (s01-s05): 5 slides
    s01_hero_permian(p)
    s02_cover(p)
    s03_about(p)
    s04_lecture_map(p)
    s05_keystone_matrix(p)
    # Section 1 (s06-s12): 7 slides incl s07b → 8
    s06_q1_divider(p)
    s07_pilot_stuck(p)
    s07b_aspen_alert_fatigue(p)
    s08_ambyint(p)
    s09_vendor_landscape(p)
    s10_rosneft_digital_field(p)
    s11_cognite_c3ai(p)
    s12_q1_no_ai_criteria(p)
    # Section 2 (s13-s19): 7 slides
    s13_q3_divider(p)
    s14_hpc_eni_aramco(p)
    s15_slb_lumi(p)
    s16_exxon_discovery6(p)
    s17_bp_beyond_limits(p)
    s18_ibm_repsol(p)
    s19_q3_alternatives(p)
    # Section 3 (s20-s27): 8 slides
    s20_methane_alphabet(p)
    s21_q2_divider(p)
    s22_methanesat_permian(p)
    s23_methanesat_loss(p)
    s24_post_methanesat_players(p)
    s25_4x_discrepancy(p)
    s26_eu_vs_epa(p)
    s27_q2_alternatives(p)
    # Section 4 (s28-s33): 6 slides
    s28_q4_divider(p)
    s29_northern_lights(p)
    s30_fervo_egs(p)
    s31_ccs_scale_gap(p)
    s32_refinery_q4(p)
    s33_q4_alternatives_sis(p)
    # Section 5 (s34-s36): 3 slides
    s34_russia_divider(p)
    s35_gazprom_cognitive_geo(p)
    s36_rosneft_detail(p)
    # Section 6 (s37-s38): 2 slides
    s37_cyber_935(p)
    s38_2020_crash_deepwater(p)
    # Section 7 (s39-s42): 4 slides
    s39_synthesis_matrix(p)
    s40_three_cornerstones(p)
    s41_qa(p)
    s42_hero_methanesat_map(p)

    p.save(str(OUT))
    print(f"Saved {OUT} with {len(p.slides)} slides")


if __name__ == "__main__":
    build_all()
