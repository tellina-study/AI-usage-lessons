"""
Part 1: s01-s14 — Раздел 0 (Открытие) + L1 «Поле».
14 слайдов: hook + cover + lecture-map + glossary + keystone + Р1 divider + 8 content.
(EN render — visible strings translated per glossary; docstrings/comments left RU as inert.)
"""

def build_part1(prs, H):
    DEEP, MID, LIGHT, TEAL = H["DEEP"], H["MID"], H["LIGHT"], H["TEAL"]
    SURFACE, WHITE, GOLD = H["SURFACE"], H["WHITE"], H["GOLD"]
    COVER_OUTLINE, GOLD_TINT, TEAL_TINT, LIGHT_TINT = H["COVER_OUTLINE"], H["GOLD_TINT"], H["TEAL_TINT"], H["LIGHT_TINT"]
    SOFT_GREY, DARK_GREY, RED_WARN = H["SOFT_GREY"], H["DARK_GREY"], H["RED_WARN"]
    ASSETS = H["ASSETS"]
    MSO_SHAPE, MSO_ANCHOR, PP_ALIGN = H["MSO_SHAPE"], H["MSO_ANCHOR"], H["PP_ALIGN"]
    Inches, Pt = H["Inches"], H["Pt"]

    blank = H["blank"]; set_slide_bg = H["set_slide_bg"]; text_box = H["text_box"]
    text_runs = H["text_runs"]; ocean_box = H["ocean_box"]; filled_rect = H["filled_rect"]
    hr_line = H["hr_line"]; add_arrow = H["add_arrow"]; add_image = H["add_image"]
    add_speaker_notes = H["add_speaker_notes"]; add_progress_bar = H["add_progress_bar"]
    add_footer = H["add_footer"]; add_assertion_title = H["add_assertion_title"]
    load_speaker_notes = H["load_speaker_notes"]; section_divider = H["section_divider"]
    disable_shadow = H["disable_shadow"]

    # ============== s01 hook — Plenty Compton split-frame ==============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "An AI-run farm promised a revolution. 19 months later — it shut down.",
        size=24)

    # LEFT panel — открытие май 2023 (use vertical-farm interior photo)
    ocean_box(s, 0.6, 1.7, 5.95, 4.0)
    photo_p = ASSETS / "photos" / "p10-vertical-farm.jpg"
    if photo_p.exists():
        add_image(s, photo_p, 0.85, 1.95, w=5.45, h=3.5)
    text_box(s, 0.85, 5.5, 5.45, 0.3, "May 2023 · Plenty Compton opening",
             size=12, italic=True, bold=True, color=MID,
             align=PP_ALIGN.CENTER)

    # RIGHT panel — закрытие декабрь 2024 (use chart of valuation collapse)
    ocean_box(s, 6.8, 1.7, 5.95, 4.0)
    chart_p = ASSETS / "charts" / "c01-plenty-collapse.png"
    if chart_p.exists():
        add_image(s, chart_p, 7.0, 1.85, w=5.6, h=3.4)
    text_box(s, 7.0, 5.5, 5.6, 0.3, "December 2024 · shutdown · Ch. 11 March 2025",
             size=12, italic=True, bold=True, color=GOLD,
             align=PP_ALIGN.CENTER)

    # Bottom data strip — 3 mega-numbers
    ocean_box(s, 0.6, 5.95, 12.13, 0.9, fill=GOLD_TINT, stroke=GOLD)
    text_runs(s, 0.8, 6.05, 3.8, 0.8, [
        {"text": "$940M", "size": 26, "bold": True, "color": GOLD},
        {"newpara": True, "text": "capital lost",
         "size": 11, "italic": True, "color": DEEP},
    ], align=PP_ALIGN.CENTER)
    text_runs(s, 4.7, 6.05, 3.9, 0.8, [
        {"text": "$1.9B → <$15M", "size": 22, "bold": True, "color": DEEP},
        {"newpara": True, "text": "valuation collapse –99% in 3 years",
         "size": 11, "italic": True, "color": MID},
    ], align=PP_ALIGN.CENTER)
    text_runs(s, 8.7, 6.05, 3.9, 0.8, [
        {"text": "19 months", "size": 26, "bold": True, "color": GOLD},
        {"newpara": True, "text": "from opening to shutdown",
         "size": 11, "italic": True, "color": DEEP},
    ], align=PP_ALIGN.CENTER)

    add_footer(s, "Sources: Plenty press May 2023; TechCrunch 2025-03-24; Bloomberg Law 2025")
    add_speaker_notes(s, load_speaker_notes("s01"))

    # ============== s02 cover ==============
    s = blank(prs); set_slide_bg(s, WHITE)

    # Decorative «10» outline — huge, left
    text_box(s, 0.0, 0.5, 6.5, 7.0, "10",
             size=400, bold=True, color=COVER_OUTLINE,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE,
             font=H["FONT_HEAD"], line_spacing=0.9)

    # Meta top right
    text_box(s, 6.0, 1.5, 6.8, 0.5,
             "Lecture 10 · AI in Agriculture · Year 3",
             size=18, italic=True, color=MID)

    # Title
    text_box(s, 6.0, 2.3, 6.8, 3.0,
             "AI in Agriculture",
             size=44, bold=True, color=DEEP, line_spacing=1.15)

    # Subtitle / scope
    text_box(s, 6.0, 4.5, 6.8, 1.2,
             "From field to shelf: the five-level ladder\nand five anti-AI criteria",
             size=20, italic=True, color=LIGHT, line_spacing=1.3)

    # Duration
    text_box(s, 6.0, 6.0, 6.8, 0.5, "Q&A at the end",
             size=18, italic=True, color=LIGHT)

    # Decorative icon
    icon_p = ASSETS / "icons" / "sprout-96.png"
    if icon_p.exists():
        add_image(s, icon_p, 11.7, 6.4, w=0.85, h=0.85)

    add_speaker_notes(s,
        "This is the title slide of Lecture 10 — the seventh industry chapter of the "
        "course. Agriculture is one of those fields where AI promises a revolution "
        "every two or three years, and each time a new generation of vendors claims "
        "that this time it will really work. By 2026 we have accumulated enough "
        "successes and enough failures to build a clear engineering apparatus for "
        "telling them apart. The tone of the lecture is trust-but-verify: neither "
        "evangelism nor contrarianism. We will walk through five levels of the AI "
        "ladder in agriculture — from the open field to the supermarket shelf — name "
        "every working solution and every failure by name, and in the finale we will "
        "formulate five anti-AI criteria that operationally answer the question of "
        "\"when not AI\".")
    return s


def build_remaining_p1(prs, H):
    """Continue with s03-s14."""
    return None


# Original build_part1 was setup for s01+s02 only. Let me extend
def build_part1_full(prs, H):
    """Build s01-s14 — all of Раздел 0 + L1."""
    # First — call basic builders defined above
    build_part1(prs, H)

    # Then continue with s03-s14 in same module
    DEEP, MID, LIGHT, TEAL = H["DEEP"], H["MID"], H["LIGHT"], H["TEAL"]
    SURFACE, WHITE, GOLD = H["SURFACE"], H["WHITE"], H["GOLD"]
    COVER_OUTLINE, GOLD_TINT, TEAL_TINT, LIGHT_TINT = H["COVER_OUTLINE"], H["GOLD_TINT"], H["TEAL_TINT"], H["LIGHT_TINT"]
    SOFT_GREY, DARK_GREY = H["SOFT_GREY"], H["DARK_GREY"]
    ASSETS = H["ASSETS"]
    MSO_SHAPE, MSO_ANCHOR, PP_ALIGN = H["MSO_SHAPE"], H["MSO_ANCHOR"], H["PP_ALIGN"]
    blank, set_slide_bg, text_box, text_runs = H["blank"], H["set_slide_bg"], H["text_box"], H["text_runs"]
    ocean_box, filled_rect, hr_line, add_arrow = H["ocean_box"], H["filled_rect"], H["hr_line"], H["add_arrow"]
    add_image, add_speaker_notes, add_progress_bar = H["add_image"], H["add_speaker_notes"], H["add_progress_bar"]
    add_footer, add_assertion_title = H["add_footer"], H["add_assertion_title"]
    load_speaker_notes, section_divider = H["load_speaker_notes"], H["section_divider"]
    SECTIONS = H["SECTIONS"]

    # ============ s03 lecture-map ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Lecture map — the five-level ladder from field to shelf", size=26)

    # 7 horizontal cards
    cards = [
        ("0. Opening", "Hook + axis + glossary", ""),
        ("1. L1 Field", "Open biology", "5 cases · 3 failures"),
        ("2. L2 Robot", "Specialization > generality", "4 cases · 3 failures"),
        ("3. L3 Animal", "Semi-closed environment, individual", "4 cases · 3 lessons"),
        ("4. L4 Chain", "Agentic AI leads", "4 cases · 2 failures"),
        ("4-bis. Environment", "Connectivity · lock-in · regulation", "3 sub-blocks"),
        ("5. L5 Shelf", "+ 5 criteria + closing", "L5 + 5 AP + checklist"),
    ]
    n = len(cards)
    col_w = 1.72; col_h = 2.7; gap = 0.06
    total_w = n * col_w + (n - 1) * gap
    start_x = (13.333 - total_w) / 2
    y = 1.8
    for i, (title, desc, dur) in enumerate(cards):
        x = start_x + i * (col_w + gap)
        ocean_box(s, x, y, col_w, col_h)
        text_box(s, x + 0.1, y + 0.15, col_w - 0.2, 0.55, title,
                 size=13, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.1)
        text_box(s, x + 0.1, y + 0.85, col_w - 0.2, 1.3, desc,
                 size=10, color=MID, italic=True, line_spacing=1.2,
                 align=PP_ALIGN.CENTER)
        if dur:
            text_box(s, x + 0.1, y + col_h - 0.45, col_w - 0.2, 0.3, dur,
                     size=10, italic=True, color=LIGHT, bold=True,
                     align=PP_ALIGN.CENTER)

    # Central question banner
    ocean_box(s, 0.6, 5.0, 12.13, 1.6, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 5.08, 11.63, 0.4,
             "Central question of the lecture:",
             size=14, italic=True, color=DARK_GREY, bold=True)
    text_box(s, 0.85, 5.5, 11.63, 1.0,
             "Where on the L1→L5 ladder does AI work, where does it break — and which\n"
             "class of solution / alternative applies at each rung?",
             size=18, italic=True, color=DEEP, line_spacing=1.3)

    add_speaker_notes(s, load_speaker_notes("s03"))

    # ============ s04 glossary mini ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Two AI modes and five L4 terms — the shared language of the lecture", size=24)

    # LEFT: closed-loop vs open-environment
    text_box(s, 0.6, 1.5, 5.95, 0.4, "AI operating environment",
             size=16, bold=True, color=MID)
    ocean_box(s, 0.6, 2.0, 5.95, 2.0, fill=TEAL_TINT, stroke=TEAL)
    text_box(s, 0.85, 2.15, 5.45, 0.4, "Closed-loop",
             size=18, bold=True, color=DEEP)
    text_box(s, 0.85, 2.55, 5.45, 1.4,
             "Controlled environment (greenhouse, factory, warehouse). "
             "Every variable is measured. AI optimizes parameters. "
             "Production deployment is mature.",
             size=12, color=DARK_GREY, italic=True, line_spacing=1.3)

    ocean_box(s, 0.6, 4.1, 5.95, 2.0)
    text_box(s, 0.85, 4.25, 5.45, 0.4, "Open environment",
             size=18, bold=True, color=DEEP)
    text_box(s, 0.85, 4.65, 5.45, 1.4,
             "Open biological environment (field, meadow). "
             "Weather, variable lighting, dust, shadows. AI works in narrow tasks. "
             "The generic \"autonomous farm\" goes bankrupt.",
             size=12, color=DARK_GREY, italic=True, line_spacing=1.3)

    # RIGHT: 5 L4 terms — gold accent on first item (AP1 P1-presentation)
    text_box(s, 6.85, 1.5, 5.95, 0.4, "5 supply-chain terms",
             size=16, bold=True, color=MID)
    terms = [
        ("Agentic AI", "ML + retrieval (RAG) + action pipeline + human-in-the-loop", True),
        ("bp (basis point)", "1 bp = 0.01%. A metric of trade slippage", False),
        ("Slippage", "The gap between the planned trade and its actual execution", False),
        ("Scope-3 emissions", "Indirect emissions across the supply chain", False),
        ("AI-MRV", "AI monitoring, reporting, verification — climate accounting", False),
    ]
    term_y = 2.0
    for term, defn, is_gold in terms:
        fill = GOLD_TINT if is_gold else LIGHT_TINT
        stroke = GOLD if is_gold else LIGHT
        ocean_box(s, 6.85, term_y, 5.95, 0.8, fill=fill, stroke=stroke)
        text_box(s, 7.05, term_y + 0.08, 2.15, 0.4, term,
                 size=12, bold=True, color=GOLD if is_gold else DEEP)
        text_box(s, 9.2, term_y + 0.08, 3.5, 0.6, defn,
                 size=10, color=MID, italic=True, line_spacing=1.25)
        term_y += 0.85

    add_speaker_notes(s, load_speaker_notes("s04"))

    # ============ s05 keystone ladder ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "The AI ladder — five levels. Each rung works differently", size=22)

    # 5 ladder steps stacked vertically — larger boxes
    levels = [
        ("L5", "Shelf / store", "Fully digitized environment. AI is mature.",
         "Walmart Eden 2017+, Tesco 2017+, X5 2020+", GOLD),
        ("L4", "Supply chain", "Controlled goods flows + fast feedback",
         "Cargill CMAX, Tract, Olam, Walmart×Cropin", TEAL),
        ("L3", "Animal", "Semi-closed environment + individual-level measurement",
         "SenseHub 2M cows, CattleEye, DeLaval V310", LIGHT),
        ("L2", "Robot", "Specialization works; the generic one goes bankrupt",
         "LaserWeeder G2, Saga UV-C, Tevel · vs Monarch/FarmWise", MID),
        ("L1", "Field", "Open biology — the hardest",
         "See & Spray works · Plenty/AppHarvest/Bowery failed", DEEP),
    ]
    step_w = 9.5; step_h = 0.85; gap = 0.08
    start_x = 0.6
    start_y = 1.6
    for i, (lid, title, desc, examples, color) in enumerate(levels):
        y = start_y + i * (step_h + gap)
        # Indent each row slightly to suggest a "ladder"
        indent = i * 0.0
        # Step box
        ocean_box(s, start_x + indent, y, step_w, step_h,
                  fill=LIGHT_TINT if color != GOLD else GOLD_TINT, stroke=color)
        # Level badge
        text_box(s, start_x + indent + 0.15, y + 0.2, 0.7, 0.5, lid,
                 size=26, bold=True, color=color,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Title
        text_box(s, start_x + indent + 1.0, y + 0.08, 3.0, 0.4, title,
                 size=15, bold=True, color=DEEP)
        # Desc
        text_box(s, start_x + indent + 1.0, y + 0.45, 3.0, 0.35, desc,
                 size=10, color=MID, italic=True, line_spacing=1.2)
        # Examples
        text_box(s, start_x + indent + 4.1, y + 0.22, step_w - 4.3, 0.45,
                 examples, size=11, italic=True, color=DARK_GREY, line_spacing=1.3)

    # Right-side axis indicator
    ocean_box(s, 10.3, 1.6, 2.4, 4.6, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 10.5, 1.7, 2.0, 0.4, "↑ moving up the ladder",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.2)
    arrows_text = [
        ("↑ controllability", "of environment rises"),
        ("↑ measurable return", "ROI rises"),
        ("↑ predictability", "of outcome rises"),
        ("↓ biology", "uncertainty falls"),
    ]
    ay = 2.25
    for hdr, dsc in arrows_text:
        text_box(s, 10.4, ay, 2.2, 0.3, hdr, size=12, bold=True, color=GOLD)
        text_box(s, 10.4, ay + 0.3, 2.2, 0.5, dsc,
                 size=9, color=DARK_GREY, italic=True, line_spacing=1.2)
        ay += 0.95

    add_footer(s, "↑ environment controllability ↔ ↑ AI penetration · next — L11 cyber-physical manufacturing")
    add_speaker_notes(s, load_speaker_notes("s05"))

    # ============ s06 section1 divider — L1 Поле ============
    section_divider(prs, 1, "Section 1 — L1 \"Field\"",
        "Open biological environment: where AI works narrowly — and where it breaks even here",
        current_section=1,
        caption="1 working case + 3 vendor matrix · 3 failures (vertical farming, ChatGPT, Plantix) · 2 anti-AI criteria")
    s_last = prs.slides[-1]
    add_speaker_notes(s_last, load_speaker_notes("s06"))

    # ============ s07 See & Spray ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "See & Spray Ultimate — the canonical L1 success", size=24)

    # Left photo
    ocean_box(s, 0.6, 1.6, 7.4, 4.5)
    p = ASSETS / "photos" / "p07-john-deere-sprayer.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.85, w=6.9, h=4.0)
    text_box(s, 0.85, 5.85, 6.9, 0.25, "John Deere ExactApply + See & Spray Ultimate · November 2025",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Right data cards — увеличенный шрифт (P0-7: spec text ≥14pt) + baselines
    cards = [
        ("5M acres", "2025 season", "≈0.55% of 900M-acre US ag total", GOLD),
        ("–50%", "contact herbicides", "from baseline ≈1 lb/acre AI → ≈0.5 lb", MID),
        ("+2.0 bushels", "soybeans per acre", "from US avg ≈177 bu/A = +1.1%", LIGHT),
    ]
    cy = 1.6
    for big, lbl, sub, color in cards:
        ocean_box(s, 8.2, cy, 4.55, 1.2, fill=LIGHT_TINT if color != GOLD else GOLD_TINT)
        text_box(s, 8.4, cy + 0.08, 2.4, 0.55, big, size=26, bold=True, color=color)
        text_box(s, 8.4, cy + 0.65, 2.4, 0.4, lbl, size=14, color=DEEP, italic=True)
        text_box(s, 10.9, cy + 0.3, 1.75, 0.85, sub,
                 size=12, color=MID, italic=True, align=PP_ALIGN.RIGHT, line_spacing=1.25)
        cy += 1.3

    # Spec card — увеличенный шрифт ≥14pt
    ocean_box(s, 8.2, 5.5, 4.55, 0.85, fill=SURFACE)
    text_box(s, 8.4, 5.58, 4.25, 0.7,
             "36 cameras · CNN on millions of images (>1M) · NVIDIA Jetson edge · <50 ms",
             size=12, color=DARK_GREY, italic=True, line_spacing=1.35)

    add_footer(s, "Sources: AgTechNavigator 2025-11-10; John Deere press release November 2025; GrowIWM 2024")
    add_speaker_notes(s, load_speaker_notes("s07"))

    # ============ s08 vendor matrix L1 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L1 platforms — five vendors, different modes. Brand ≠ operating mode",
        size=22)

    # 5×4 matrix
    headers = ["Platform", "Geography", "Operating mode", "Business model"]
    rows = [
        ("BASF xarvio", "EU, Japan (rice)", "Subscription + advisory", "Pay per acre"),
        ("Climate FieldView", "US (left Russia 2022)", "Data warehouse", "250M acres of subscriptions"),
        ("Syngenta Cropwise", "Global", "Bayer Forward integration", "Bundled in a package"),
        ("Granular (Corteva)", "US", "Farm management", "Cloud service"),
        ("Taranis", "Global", "Computer vision + drones", "Pay per acre"),
    ]
    matrix_x = 0.6
    matrix_y = 1.6
    col_widths = [2.5, 2.3, 2.8, 2.5]
    row_h = 0.55

    # Header row
    cx = matrix_x
    for i, (hdr, w) in enumerate(zip(headers, col_widths)):
        ocean_box(s, cx, matrix_y, w, row_h, fill=DEEP, stroke=DEEP)
        text_box(s, cx, matrix_y, w, row_h, hdr,
                 size=12, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        cx += w + 0.05

    # Data rows
    for ri, row in enumerate(rows):
        cx = matrix_x
        ry = matrix_y + row_h + 0.05 + ri * (row_h + 0.05)
        fill = SURFACE if ri % 2 == 0 else LIGHT_TINT
        for ci, (val, w) in enumerate(zip(row, col_widths)):
            ocean_box(s, cx, ry, w, row_h, fill=fill, stroke=LIGHT, stroke_pt=0.5)
            is_gold = (ci == 1 and ri == 1)  # FieldView выход из РФ — gold highlight
            text_box(s, cx + 0.1, ry, w - 0.2, row_h, val,
                     size=10, bold=(ci == 0), color=GOLD if is_gold else DEEP,
                     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)
            cx += w + 0.05

    # Sidebar callout: BASF Japan rice (ключевая точка — остальные 4 для self-study)
    ocean_box(s, 0.6, 5.5, 12.13, 1.4, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 5.6, 11.5, 0.4,
             "★ Key point on this slide — BASF xarvio in Japan: a rice-yield guarantee (October 2025)",
             size=13, bold=True, color=GOLD)
    text_box(s, 0.85, 6.0, 11.5, 0.85,
             "The first case of a guaranteed yield under AI advisory: BASF pays compensation "
             "if the harvest falls short. A closed data loop + an insurance mechanism = the only known example as of 2026.\n"
             "The other 4 platforms in the matrix are for self-study; the \"brand ≠ operating mode\" criterion applies to each.",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.35)

    add_footer(s, "Source: BASF press release p-25-191 October 2025 · TAdviser FieldView 2022")
    add_speaker_notes(s, load_speaker_notes("s08"))

    # ============ s09 foundation models — simplified, 3 key claims ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Foundation models 2026 — the barrier to entry dropped by 2-3 orders of magnitude",
        size=22)

    # Left (55%): Sentinel-2 imagery + short formula
    ocean_box(s, 0.6, 1.5, 6.5, 4.0)
    p = ASSETS / "photos" / "p09-sentinel-brazil.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.7, w=6.0, h=3.0)
    text_box(s, 0.85, 4.75, 6.0, 0.4,
             "Sentinel-2 / Copernicus (ESA, CC-BY-SA) — the data class for TerraMind",
             size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Short formula below image
    ocean_box(s, 0.6, 5.7, 6.5, 1.2, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.85, 5.8, 6.0, 0.4,
             "TerraMind (IBM + ESA, 2025)",
             size=15, bold=True, color=DEEP)
    text_box(s, 0.85, 6.2, 6.0, 0.65,
             "\"GPT-3 for Earth observation\". A team of 3\n"
             "fine-tunes on thousands of images instead of millions.",
             size=12, color=DARK_GREY, italic=True, line_spacing=1.3)

    # Right (45%): 2 callouts
    # Callout 1 — vendor concentration risk (GOLD)
    ocean_box(s, 7.3, 1.5, 5.45, 2.6, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.5, 1.65, 5.05, 0.4,
             "Vendor concentration risk",
             size=16, bold=True, color=GOLD)
    text_box(s, 7.5, 2.15, 5.05, 1.9,
             "The entire L1 industry runs on 2-3 foundation models\n"
             "(IBM / NASA / ESA).\n\n"
             "A model shutting down = teams lose\n"
             "capabilities all at once.",
             size=13, color=DEEP, italic=True, line_spacing=1.5)

    # Callout 2 — advisor architecture
    ocean_box(s, 7.3, 4.3, 5.45, 2.6, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 7.5, 4.45, 5.05, 0.4,
             "The 2026 advisor architecture",
             size=16, bold=True, color=MID)
    text_box(s, 7.5, 4.95, 5.05, 1.9,
             "Foundation model (TerraMind)\n"
             "+ retrieval (RAG) to the local regulator\n"
             "+ LLM generation\n"
             "+ explicit abstention at low confidence.",
             size=13, color=DEEP, italic=True, line_spacing=1.5)

    add_footer(s, "Sources: IBM Research, April 2025; NASA Earth Observatory 2025")
    add_speaker_notes(s, load_speaker_notes("s09"))

    # ============ s10 vertical farming collapse ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Vertical farms — a failure not caused by bad AI. AppHarvest, Plenty, Bowery",
        size=22)

    # Top: chart
    ocean_box(s, 0.6, 1.5, 6.3, 4.0)
    c = ASSETS / "charts" / "c10-vf-losses.png"
    if c.exists():
        add_image(s, c, 0.85, 1.7, w=5.8, h=3.7)

    # Right: 3 cards — с baseline counterfactuals
    cards = [
        ("AppHarvest", "Greenhouse, unprofitable 2023", "$475M SPAC + $341M debt ≈ $816M"),
        ("Plenty", "Compton AI factory 19 mo → bankruptcy", "$940M of $1B+ raised since 2014; –99% valuation"),
        ("Bowery", "Collapse before IPO, November 2024", ">$700M raised; $32M never-used Locust Grove"),
    ]
    cy = 1.5
    for name, ev, money in cards:
        ocean_box(s, 7.2, cy, 5.55, 1.2)
        text_box(s, 7.4, cy + 0.1, 5.15, 0.4, name,
                 size=15, bold=True, color=DEEP)
        text_box(s, 7.4, cy + 0.5, 5.15, 0.4, ev,
                 size=11, color=MID, italic=True)
        text_box(s, 7.4, cy + 0.85, 5.15, 0.3, money,
                 size=13, bold=True, color=GOLD)
        cy += 1.3

    # Bottom insight
    ocean_box(s, 0.6, 5.7, 12.13, 1.0, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 5.8, 11.6, 0.4,
             "$1.37B+ in losses, 14 bankruptcies in 2025. The energy arithmetic did not work.",
             size=14, bold=True, color=DEEP)
    text_box(s, 0.85, 6.2, 11.6, 0.45,
             "The climate controllers worked. Computer vision recognized. The model predicted. LED ≈ 100× the energy of sunlight — AP1 thermodynamics > AI.",
             size=12, color=DARK_GREY, italic=True, line_spacing=1.3)

    add_footer(s, "Sources: TechCrunch 2025-03-24, 2024-11-04 (Bowery); Agriculture Dive 689039 (AppHarvest)")
    add_speaker_notes(s, load_speaker_notes("s10"))

    # ============ s11 5-Why thermodynamics ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Five \"whys\" — why AI did not close the thermodynamic gap",
        size=24)

    # Chain of 5 steps with arrows
    steps = [
        ("1. Why did\nit close?", "Capital\nran out", MID),
        ("2. Why the\ncapital?", "Unit economics\ndon't work", MID),
        ("3. Why don't\nthey work?", "Cost of\nLED energy\n100× sunlight", GOLD),
        ("4. Why\n100×?", "Law of\nthermodynamics", DEEP),
        ("5. Can AI\nclose it?", "No:\neffect 5-15%\nvs a 100× gap", GOLD),
    ]
    step_w = 2.15; step_h = 2.6; gap = 0.2
    sx = 0.6
    sy = 1.7
    for i, (q, a, color) in enumerate(steps):
        ocean_box(s, sx, sy, step_w, step_h,
                  fill=GOLD_TINT if color == GOLD else LIGHT_TINT, stroke=color)
        text_box(s, sx + 0.1, sy + 0.15, step_w - 0.2, 0.9, q,
                 size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.2)
        hr_line(s, sx + 0.2, sy + 1.1, step_w - 0.4, color=color, weight=1.2)
        text_box(s, sx + 0.1, sy + 1.2, step_w - 0.2, step_h - 1.3, a,
                 size=13, bold=(color == GOLD), color=color, align=PP_ALIGN.CENTER, line_spacing=1.25,
                 anchor=MSO_ANCHOR.MIDDLE)

        if i < 4:
            add_arrow(s, sx + step_w, sy + step_h/2 - 0.15, gap, 0.3, fill=LIGHT)
        sx += step_w + gap

    # Bottom takeaway — увеличен gap от steps (P1-4 student-sim)
    ocean_box(s, 0.6, 4.9, 12.13, 1.9, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 5.0, 11.6, 0.5,
             "Root cause: a two-order-of-magnitude gap. No model will close it.",
             size=18, bold=True, color=DEEP)
    text_box(s, 0.85, 5.55, 11.6, 0.45,
             "0.5 (sun→LED) × 0.7 (LED→plant) × 0.3 (plant→yield) ≈ 10.5% end-to-end. "
             "AI optimizes the denominator (5-15%); the gap is in the numerator.",
             size=12, color=DARK_GREY, italic=True, line_spacing=1.3)
    text_box(s, 0.85, 6.1, 11.6, 0.6,
             "AP1 in its strict form: \"when AI optimizes an incorrectly formulated objective function — better not AI\".",
             size=12, bold=True, italic=True, color=GOLD, line_spacing=1.3)

    add_footer(s, "Analysis by Hannah Ritchie · MDPI Sustainability, 2024")
    add_speaker_notes(s, load_speaker_notes("s11"))

    # ============ s12 ChatGPT hallucinations ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "ChatGPT and Bard as agronomists — \"confidently wrong\" in tens of percent of cases",
        size=22)

    # Left: study summary
    ocean_box(s, 0.6, 1.5, 6.0, 5.0)
    text_box(s, 0.85, 1.65, 5.5, 0.5,
             "Tzachor et al., Nature Food, November 2023",
             size=14, bold=True, color=DEEP)
    text_box(s, 0.85, 2.15, 5.5, 0.4,
             "Reichman University · 184 questions (publication 11.2023, press 05.2024)",
             size=11, italic=True, color=MID)
    hr_line(s, 0.85, 2.6, 5.3, color=LIGHT, weight=1.0)

    results = [
        ("GPT-3.5", "32%", "correct"),
        ("GPT-4", "44%", "correct"),
        ("Bard", "29%", "correct"),
    ]
    ry = 2.85
    for model, pct, lbl in results:
        text_box(s, 1.0, ry, 1.8, 0.4, model, size=13, bold=True, color=DEEP)
        text_box(s, 2.8, ry, 1.5, 0.4, pct, size=18, bold=True, color=GOLD)
        text_box(s, 4.3, ry, 2.0, 0.4, lbl, size=11, italic=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
        ry += 0.55

    text_box(s, 0.85, 4.7, 5.5, 1.6,
             "The other 56-71% of answers are confidently wrong: the model does not say \"I don't know\", "
             "it produces a confident answer with the wrong dosage / an unsuitable chemical. "
             "The failure mode is not \"the model is bad\", but \"the application is outside its mode\".",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.4)

    # Right: Anti-pattern AP4 + alternative
    ocean_box(s, 6.8, 1.5, 5.95, 5.0, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, 1.65, 5.5, 0.5,
             "AP4 — a categorical anti-pattern",
             size=14, bold=True, color=GOLD)
    text_box(s, 7.05, 2.15, 5.5, 0.8,
             "A generic LLM in the role of agronomist advisor —\n"
             "categorically inapplicable. Not \"needs more work\"; this is a different class of task.",
             size=12, color=DEEP, italic=True, line_spacing=1.3)

    hr_line(s, 7.05, 3.05, 5.4, color=GOLD, weight=1.5)
    text_box(s, 7.05, 3.2, 5.5, 0.4,
             "Alternative: AI with source verification (RAG)",
             size=14, bold=True, color=DEEP)
    alts = [
        "A bounded farm knowledge base",
        "Retrieval + source citation",
        "Calibrated confidence: \"I don't know\" when it doesn't",
        "An audit trail for every recommendation",
    ]
    ay = 3.65
    for a in alts:
        text_box(s, 7.25, ay, 5.3, 0.45, "• " + a,
                 size=11, color=DEEP, line_spacing=1.3)
        ay += 0.45

    text_box(s, 7.05, 5.65, 5.5, 0.6,
             "+ human-in-the-loop: the final recommendation is confirmed by an agronomist",
             size=11, bold=True, italic=True, color=GOLD, line_spacing=1.3)

    add_footer(s, "Source: Tzachor et al., Nature Food, November 2023 (press coverage Phys.org 2024-05)")
    add_speaker_notes(s, load_speaker_notes("s12"))

    # ============ s13 Plantix ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Plantix — 10-15% misdiagnosis × 10M+ downloads = ~100k wrong recommendations / year",
        size=18)

    # Left: stylized phone UI mock-up + stats
    ocean_box(s, 0.6, 1.6, 5.5, 5.0)
    # Phone frame outline
    text_box(s, 0.85, 1.8, 5.0, 0.4, "Plantix · mobile app",
             size=14, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 2.2, 5.0, 0.4, "10+ million downloads",
             size=11, italic=True, color=MID, align=PP_ALIGN.CENTER)
    # Fake phone screen
    ocean_box(s, 1.8, 2.7, 3.1, 3.5, fill=DEEP, stroke=DEEP)
    text_box(s, 1.95, 2.85, 2.8, 0.4, "[ camera ]",
             size=11, italic=True, color=WHITE, align=PP_ALIGN.CENTER)
    ocean_box(s, 1.95, 3.3, 2.8, 1.5, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 2.05, 3.4, 2.6, 1.3,
             "Photo of a\nsoybean leaf\n— analysis —",
             size=11, italic=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.3,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 1.95, 4.9, 2.8, 0.45,
             "Diagnosis:\nanthracnose",
             size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, line_spacing=1.2)
    text_box(s, 1.95, 5.5, 2.8, 0.45,
             "Confidence: 87%",
             size=10, italic=True, color=GOLD, align=PP_ALIGN.CENTER)

    # Right: breakdown
    ocean_box(s, 6.4, 1.6, 6.4, 2.4)
    text_box(s, 6.65, 1.75, 6.0, 0.5, "What's wrong with \"85-90% accuracy\"",
             size=15, bold=True, color=DEEP)
    text_box(s, 6.65, 2.25, 6.0, 1.7,
             "• Vendor self-report (no independent audit)\n"
             "• 10-15% misdiagnosis = 1-1.5M errors / year\n"
             "• Dose-critical errors (wrong chemical)\n"
             "• Chronic acceptance of false positives in an advisor",
             size=11, color=DARK_GREY, line_spacing=1.5)

    ocean_box(s, 6.4, 4.15, 6.4, 2.45, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 6.65, 4.3, 6.0, 0.5, "AP3 + alternative",
             size=15, bold=True, color=GOLD)
    text_box(s, 6.65, 4.85, 6.0, 1.7,
             "AP3: threshold accuracy ≠ readiness for deployment.\n"
             "Alternative — calibrated confidence + abstention:\n"
             "  • output only at ≥90% confidence,\n"
             "  • otherwise — \"refer to a specialist\",\n"
             "  • + partition by dose criticality.",
             size=11, color=DEEP, italic=True, line_spacing=1.4)

    add_footer(s, "Plantix.net (interface); data from Frontiers in Plant Science 2020 + Plantix self-report")
    add_speaker_notes(s, load_speaker_notes("s13"))

    # ============ s14 РФ context L1 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L1 in Russia — ExactFarming and Progress Agro at a digitalization index of 27.2",
        size=22)

    # Left: chart
    ocean_box(s, 0.6, 1.5, 6.0, 4.5)
    c = ASSETS / "charts" / "c14-rus-digi.png"
    if c.exists():
        add_image(s, c, 0.85, 1.7, w=5.5, h=4.1)

    # Right: 2 cards working + 1 caveat
    cards = [
        ("ExactFarming", "12,700 farms · 9.8M ha", "Field management + monitoring", MID),
        ("Progress Agro group", "+5% profitability", "Internal measurement 2024", LIGHT),
    ]
    cy = 1.5
    for name, key, sub, color in cards:
        ocean_box(s, 6.8, cy, 6.0, 1.4)
        text_box(s, 7.0, cy + 0.1, 5.7, 0.4, name,
                 size=15, bold=True, color=color)
        text_box(s, 7.0, cy + 0.55, 5.7, 0.4, key,
                 size=13, bold=True, color=GOLD)
        text_box(s, 7.0, cy + 0.95, 5.7, 0.35, sub,
                 size=10, italic=True, color=MID)
        cy += 1.55

    # Bottom: AP6 inline politicial risk
    ocean_box(s, 0.6, 6.1, 12.13, 0.8, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 6.2, 11.6, 0.4,
             "AP6 — Climate FieldView left Russia in 2022",
             size=13, bold=True, color=GOLD)
    text_box(s, 0.85, 6.55, 11.6, 0.3,
             "L1 political risk: cloud services with foreign dependencies can be cut off by a vendor decision or by sanctions.",
             size=10, color=DARK_GREY, italic=True, line_spacing=1.3)

    add_footer(s, "Sources: Yakov & Partners 2024 · ExactFarming.com · TAdviser 2022")
    add_speaker_notes(s, load_speaker_notes("s14"))

    return prs
