"""
Part 3: s22-s38 — L3 Животное + L4 Цепочка + Р4-bis Среда + L5 Полка + closing + Q&A.
17 слайдов.
"""

def build_part3(prs, H):
    DEEP, MID, LIGHT, TEAL = H["DEEP"], H["MID"], H["LIGHT"], H["TEAL"]
    SURFACE, WHITE, GOLD = H["SURFACE"], H["WHITE"], H["GOLD"]
    COVER_OUTLINE, GOLD_TINT, TEAL_TINT, LIGHT_TINT = H["COVER_OUTLINE"], H["GOLD_TINT"], H["TEAL_TINT"], H["LIGHT_TINT"]
    SOFT_GREY, DARK_GREY, RED_WARN = H["SOFT_GREY"], H["DARK_GREY"], H["RED_WARN"]
    ASSETS = H["ASSETS"]
    MSO_SHAPE, MSO_ANCHOR, PP_ALIGN = H["MSO_SHAPE"], H["MSO_ANCHOR"], H["PP_ALIGN"]
    blank, set_slide_bg, text_box, text_runs = H["blank"], H["set_slide_bg"], H["text_box"], H["text_runs"]
    ocean_box, filled_rect, hr_line, add_arrow = H["ocean_box"], H["filled_rect"], H["hr_line"], H["add_arrow"]
    add_image, add_speaker_notes, add_progress_bar = H["add_image"], H["add_speaker_notes"], H["add_progress_bar"]
    add_footer, add_assertion_title = H["add_footer"], H["add_assertion_title"]
    load_speaker_notes, section_divider = H["load_speaker_notes"], H["section_divider"]
    disable_shadow = H["disable_shadow"]
    Inches, Pt = H["Inches"], H["Pt"]

    # ============ s22 section3 divider — L3 Животное ============
    section_divider(prs, 3, "Section 3 — L3 «Animal»",
        "Semi-closed environment + individual-animal measurement. AI works more reliably than at L1-L2.",
        current_section=3,
        caption="4 working cases (SenseHub, CattleEye, DeLaval, Birdoo) · 3 anti-hype lessons (Cainthus, tie-stall, Holstein bias)")
    add_speaker_notes(prs.slides[-1], load_speaker_notes("s22"))

    # ============ s23 SenseHub 2M cows ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Allflex SenseHub — 2M cows with sensors (≈0.75% of 265M dairy cows worldwide)", size=22)

    # Left: photo
    ocean_box(s, 0.6, 1.5, 6.5, 5.1)
    p = ASSETS / "photos" / "p23-cow-ear-tag.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.75, w=6.0, h=4.0)
    text_box(s, 0.85, 5.85, 6.0, 0.3,
             "Sensor ear tag · Wikimedia (Cow with ear tag, CC-BY-SA)",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 6.2, 6.0, 0.3,
             "+ accelerometer collar + cloud analytics",
             size=10, italic=True, color=MID, align=PP_ALIGN.CENTER)

    # Right: 3-step flow + 5 alerts
    text_box(s, 7.3, 1.6, 5.4, 0.4, "AI pipeline (early warning)",
             size=14, bold=True, color=MID)

    flow_steps = [
        ("1. Sensor", "Accelerometer · 5-7 yr battery", LIGHT),
        ("2. Cloud", "ML behavior classification", MID),
        ("3. Alert to farmer", "Early warning, not prescription", GOLD),
    ]
    fy = 2.15
    for hdr, sub, color in flow_steps:
        ocean_box(s, 7.3, fy, 5.4, 0.85, fill=LIGHT_TINT if color != GOLD else GOLD_TINT, stroke=color)
        text_box(s, 7.5, fy + 0.12, 5.0, 0.35, hdr,
                 size=15, bold=True, color=DEEP)
        text_box(s, 7.5, fy + 0.48, 5.0, 0.32, sub,
                 size=12, color=MID, italic=True)
        fy += 0.95

    # Alerts row
    text_box(s, 7.3, 5.05, 5.4, 0.4, "5 alert classes",
             size=14, bold=True, color=DEEP)
    alerts = ["estrus", "calving", "lameness", "mastitis", "pneumonia"]
    ax = 7.3
    aw = 1.0
    for al in alerts:
        ocean_box(s, ax, 5.5, aw, 0.55, fill=GOLD_TINT, stroke=GOLD)
        text_box(s, ax, 5.5, aw, 0.55, al, size=11, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        ax += aw + 0.08

    # Bottom: augmentation principle
    ocean_box(s, 7.3, 6.2, 5.4, 0.6, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.5, 6.25, 5.0, 0.5,
             "AI = augmentation, not replacement",
             size=13, bold=True, color=GOLD,
             anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Source: Merck Animal Health, 2025 — 2M dairy-cow milestone")
    add_speaker_notes(s, load_speaker_notes("s23"))

    # ============ s24 CattleEye + DeLaval + Birdoo ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "CattleEye + DeLaval VMS V310 + Cargill Birdoo — 3 working cases", size=22)

    cards = [
        ("CattleEye", "60 farms · 11,000 cows", "CCTV + cloud AI:\nlameness scoring · GEA network >250,000", LIGHT),
        ("DeLaval VMS V310", "99.8% attachment rate", "998/1000 successful attachments\nof the milking-unit arm", GOLD),
        ("Cargill Birdoo", ">95% accuracy", "Computer vision for weight\nestimation · saves 10-30 g feed / broiler", MID),
    ]
    card_w = 3.95; card_h = 4.5; gap = 0.18
    sx = 0.6
    sy = 1.6
    for i, (name, kpi, desc, color) in enumerate(cards):
        x = sx + i * (card_w + gap)
        ocean_box(s, x, sy, card_w, card_h, fill=LIGHT_TINT if color != GOLD else GOLD_TINT, stroke=color)
        # Photo (cow) for first two
        if i == 0:
            p = ASSETS / "photos" / "p25-dairy-cow.jpg"
            if p.exists(): add_image(s, p, x + 0.15, sy + 0.2, w=card_w - 0.3, h=1.8)
        elif i == 1:
            p = ASSETS / "photos" / "p25-holstein.jpg"
            if p.exists(): add_image(s, p, x + 0.15, sy + 0.2, w=card_w - 0.3, h=1.8)
        else:
            # Birdoo — use chicken-like icon proxy
            icon_p = ASSETS / "icons" / "bird-96.png"
            if icon_p.exists(): add_image(s, icon_p, x + (card_w - 1.0) / 2, sy + 0.6, w=1.0, h=1.0)
        text_box(s, x + 0.15, sy + 2.15, card_w - 0.3, 0.45, name,
                 size=15, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x + 0.15, sy + 2.65, card_w - 0.3, 0.5, kpi,
                 size=15, bold=True, color=GOLD if color != GOLD else DEEP,
                 align=PP_ALIGN.CENTER)
        text_box(s, x + 0.2, sy + 3.2, card_w - 0.4, 1.2, desc,
                 size=10, color=DARK_GREY, italic=True,
                 align=PP_ALIGN.CENTER, line_spacing=1.4)

    add_footer(s, "Sources: Fortune 2025-06 (CattleEye GEA); DeLaval press 2025-04; Cargill.com 2025")
    add_speaker_notes(s, load_speaker_notes("s24"))

    # ============ s25 Cainthus + tie-stall + Holstein-bias ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Cainthus, tie-stall barns, Holstein bias — 3 anti-hype lessons of L3",
        size=20)

    lessons = [
        ("Cainthus (Cargill 2018)", "Announcement ≠ deployment",
         "No public production metrics. A branded press release, but 0 measurable deployment data by 2026.",
         "alert-circle"),
        ("Tie-stall barns", "Barn architecture breaks computer vision",
         "The algorithm works in free-stall (loose) housing, not in tie-stall.\n"
         "Most Russian cows are tie-stall housed.",
         "lock"),
        ("Holstein bias", "Training data ≠ local breeds",
         "AI trained on Holstein / Friesian breeds. Yaroslavl, Yakut, Kholmogory — different morphology.\n"
         "AI capability ≠ AI applicability.",
         "x"),
    ]
    sy = 1.5
    for name, key, desc, icon_name in lessons:
        ocean_box(s, 0.6, sy, 12.13, 1.5)
        icon_p = ASSETS / "icons" / f"{icon_name}-96.png"
        if icon_p.exists():
            add_image(s, icon_p, 0.85, sy + 0.3, w=0.9, h=0.9)
        text_box(s, 2.05, sy + 0.15, 4.0, 0.4, name,
                 size=14, bold=True, color=DEEP)
        text_box(s, 2.05, sy + 0.55, 4.0, 0.4, key,
                 size=13, bold=True, color=GOLD, italic=True)
        text_box(s, 6.5, sy + 0.15, 6.0, 1.25, desc,
                 size=11, color=DARK_GREY, italic=True, line_spacing=1.4,
                 anchor=MSO_ANCHOR.MIDDLE)
        sy += 1.6

    ocean_box(s, 0.6, 6.45, 12.13, 0.4, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 6.5, 11.6, 0.3,
             "Key lesson: AI capability ≠ AI applicability. Barn architecture + breed are the applicability variables.",
             size=11, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Sources: Wikimedia Commons (Holstein); Cargill press release 2018")
    add_speaker_notes(s, load_speaker_notes("s25"))

    # ============ s26 РФ L3 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L3 in Russia — Connectome.ai + sanction uncertainty of the dairy AI stack",
        size=20)

    # Left: working case
    ocean_box(s, 0.6, 1.5, 6.0, 5.0, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.85, 1.65, 5.5, 0.5, "Works — Connectome.ai",
             size=15, bold=True, color=DEEP)
    icon_p = ASSETS / "icons" / "scan-96.png"
    if icon_p.exists():
        add_image(s, icon_p, 0.85 + (5.5 - 0.9) / 2, 2.2, w=0.9, h=0.9)
    text_box(s, 0.85, 3.3, 5.5, 0.4, "Skolkovo resident",
             size=12, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 3.8, 5.5, 1.6,
             "Narrow computer-vision task:\ncalving monitoring of calves\n+ early alert for assistance",
             size=12, color=DEEP, italic=True, line_spacing=1.4,
             align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 5.5, 5.5, 0.9,
             "Pattern: narrow niche + CV +\nmeasurable animal safety",
             size=10, color=DARK_GREY, italic=True, line_spacing=1.4,
             align=PP_ALIGN.CENTER)

    # Right: vapor risk
    ocean_box(s, 6.8, 1.5, 6.0, 5.0, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, 1.65, 5.5, 0.5, "In question — DeLaval / GEA / Lely",
             size=15, bold=True, color=DEEP)
    text_box(s, 7.05, 2.15, 5.5, 0.4, "Gray status of cloud analytics",
             size=11, italic=True, color=MID)
    text_box(s, 7.05, 2.65, 5.5, 2.4,
             "• Equipment physically with farmers\n"
             "• Cloud analytics depends on Europe\n"
             "• Precedent: Climate FieldView 2022 →\n"
             "  Microsoft Azure 2024 (for defense sector)\n"
             "• Lobnya 2026 — equipment substitution\n"
             "  started (₽4B), AI stack — separate track",
             size=11, color=DEEP, line_spacing=1.5)
    text_box(s, 7.05, 5.15, 5.5, 1.3,
             "F9 — \"vapor\" risk: the vendor can switch off AI functionality by sanction or license decision, "
             "without notifying users in advance.",
             size=11, bold=True, italic=True, color=GOLD, line_spacing=1.4)

    add_footer(s, "Sources: Connectome.ai (Skolkovo); BUSINESS-stat 2026 Lobnya · TAdviser FieldView")
    add_speaker_notes(s, load_speaker_notes("s26"))

    # ============ s27 section4 divider ============
    section_divider(prs, 4, "Section 4 — L4 «Supply chain»",
        "Agentic AI leads. Outcome is measured in basis points over minutes, not seasons.",
        current_section=4,
        caption="4 working cases (Cargill CMAX, Tract, Olam, Walmart×Cropin) · 2 failures (USDA, Verra) · Russia parallel (X5/Magnit/RSHB)")
    add_speaker_notes(prs.slides[-1], load_speaker_notes("s27"))

    # ============ s28 Cargill CMAX ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Cargill CMAX — BIG AI Excellence Award 2026", size=24)

    # Photo left
    ocean_box(s, 0.6, 1.5, 7.0, 5.1)
    p = ASSETS / "photos" / "p28-grain-port.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.75, w=6.5, h=4.0)
    text_box(s, 0.85, 5.85, 6.5, 0.3,
             "Grain port and silos · Tilbury (Wikimedia, CC-BY-SA)",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 6.2, 6.5, 0.3,
             "AI optimizes port forecasting and shipping logistics",
             size=10, italic=True, color=MID, align=PP_ALIGN.CENTER)

    # Right: KPIs — с baseline counterfactuals
    kpis = [
        ("70+ countries", "of 195 (≈36% of the world) · ~155k staff", LIGHT),
        ("1000+ sites", "warehouses / ports / silos of Cargill", MID),
        ("BIG AI 2026", "Excellence Award at the L4 level", GOLD),
    ]
    cy = 1.5
    for big, lbl, color in kpis:
        ocean_box(s, 7.8, cy, 4.95, 1.25, fill=LIGHT_TINT if color != GOLD else GOLD_TINT)
        text_box(s, 8.0, cy + 0.12, 4.6, 0.55, big,
                 size=26, bold=True, color=color)
        text_box(s, 8.0, cy + 0.72, 4.6, 0.4, lbl,
                 size=14, color=DEEP, italic=True)
        cy += 1.35

    ocean_box(s, 7.8, 5.55, 4.95, 1.15, fill=SURFACE)
    text_box(s, 8.0, 5.6, 4.55, 0.4, "Success principle: agent narrowness",
             size=14, bold=True, color=DEEP)
    text_box(s, 8.0, 6.0, 4.55, 0.7,
             "One action per agent (hedge / route) + human-in-the-loop for trades >$10M notional.",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.4)

    add_footer(s, "Source: Cargill press release, April 2026 (BIG AI Excellence Award)")
    add_speaker_notes(s, load_speaker_notes("s28"))

    # ============ s29 hedge pseudo-flow ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "How the agent hedges — simplified 4-step flow",
        size=24)

    steps = [
        ("1. Sensor", "State vector:\nprice + weather + currency",
         "input data", "database"),
        ("2. Inference", "Price distribution\n5/30/90 days + uncertainty",
         "ML model", "brain"),
        ("3. Decision", "4 actions:\nbuy / sell /\nhold / hedge\n+ human at >$10M notional",
         "Action layer", "settings"),
        ("4. Feedback", "bp (basis points) over minutes,\nonline learning",
         "Loop closes", "trending-up"),
    ]
    step_w = 2.85; step_h = 3.7; gap = 0.2
    sx = 0.6
    sy = 1.5
    for i, (hdr, body, sub, icon_name) in enumerate(steps):
        x = sx + i * (step_w + gap)
        is_gold = (i == 2)  # decision is the gold-highlighted critical step
        ocean_box(s, x, sy, step_w, step_h,
                  fill=GOLD_TINT if is_gold else LIGHT_TINT,
                  stroke=GOLD if is_gold else LIGHT)
        icon_p = ASSETS / "icons" / f"{icon_name}-96.png"
        if icon_p.exists():
            add_image(s, icon_p, x + (step_w - 0.9) / 2, sy + 0.25, w=0.9, h=0.9)
        text_box(s, x + 0.15, sy + 1.3, step_w - 0.3, 0.45, hdr,
                 size=15, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x + 0.15, sy + 1.8, step_w - 0.3, 1.4, body,
                 size=11, color=DARK_GREY, italic=True,
                 align=PP_ALIGN.CENTER, line_spacing=1.4)
        text_box(s, x + 0.15, sy + step_h - 0.45, step_w - 0.3, 0.35, sub,
                 size=11, bold=True, color=GOLD if is_gold else MID,
                 align=PP_ALIGN.CENTER, italic=True)
        # Arrow to next
        if i < len(steps) - 1:
            add_arrow(s, x + step_w, sy + step_h/2 - 0.15, gap, 0.3, fill=LIGHT)

    # Bottom: worked example
    ocean_box(s, 0.6, 5.4, 12.13, 1.5, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 5.55, 11.6, 0.4,
             "Example: slippage cut from 45 bp to 8 bp",
             size=15, bold=True, color=DEEP)
    text_box(s, 0.85, 6.0, 11.6, 0.8,
             "On a $5M notional trade: (45–8) × 0.01% × $5M = $1,850 per trade. "
             "At 20 trades per month = ~$37k saved. ROI of the narrow agentic AI — 1-2 months.\n"
             "This works because the task is narrow (hedge timing), feedback is fast, and the human is only for large trades.",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.4)

    add_footer(s, "Example: McKinsey 2025 hedging report — typical manual slippage")
    add_speaker_notes(s, load_speaker_notes("s29"))

    # ============ s30 Tract + Olam + Walmart + Tesco ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Tract + Olam Mindsprint + Walmart × Cropin + Tesco",
        size=24)

    cards = [
        ("Tract", "€18.6M Series A",
         "Icos Capital · 4 anchor investors:\nCargill + ADM + Olam + LDC.\nData backbone, NOT an agent.",
         "database"),
        ("Olam Procuresprint", "Agentic procurement",
         "Narrow procurement task:\nprice + suppliers + contracts\nas an agent.",
         "package"),
        ("Walmart × Cropin", "US + South Africa",
         "(not India) — supply-chain\nanalytics and ESG reporting.",
         "globe"),
        ("Tesco AI", "−30% food waste",
         "Since 2017 — Tesco AI for\nperishables forecasting.",
         "trending-down"),
    ]
    card_w = 2.85; card_h = 4.2; gap = 0.18
    sx = 0.6; sy = 1.6
    for i, (name, kpi, desc, icon_name) in enumerate(cards):
        x = sx + i * (card_w + gap)
        ocean_box(s, x, sy, card_w, card_h)
        icon_p = ASSETS / "icons" / f"{icon_name}-96.png"
        if icon_p.exists():
            add_image(s, icon_p, x + (card_w - 0.9) / 2, sy + 0.25, w=0.9, h=0.9)
        text_box(s, x + 0.15, sy + 1.3, card_w - 0.3, 0.45, name,
                 size=14, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x + 0.15, sy + 1.8, card_w - 0.3, 0.5, kpi,
                 size=13, bold=True, color=GOLD, align=PP_ALIGN.CENTER, line_spacing=1.2)
        text_box(s, x + 0.2, sy + 2.5, card_w - 0.4, 1.6, desc,
                 size=10, color=DARK_GREY, italic=True,
                 align=PP_ALIGN.CENTER, line_spacing=1.4)

    # Bottom warning
    ocean_box(s, 0.6, 6.0, 12.13, 0.85, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 6.1, 11.6, 0.4,
             "⚠ Don't confuse: Tract = data backbone (compliance infrastructure), not agentic AI.",
             size=12, bold=True, color=GOLD)
    text_box(s, 0.85, 6.5, 11.6, 0.3,
             "Competitors jointly build compliance infrastructure — a rare Cargill+ADM+Olam+LDC collaboration precedent.",
             size=10, italic=True, color=DARK_GREY)

    add_footer(s, "Sources: Tract press release 2024-08; FreshPlaza; Wipro press release 2026 (Mindsprint)")
    add_speaker_notes(s, load_speaker_notes("s30"))

    # ============ s31 USDA + Verra ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "USDA Climate-Smart canceled + 94% phantom credits at Verra",
        size=22)

    # Left: USDA cancellation
    ocean_box(s, 0.6, 1.5, 6.0, 5.0, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 1.65, 5.5, 0.5, "April 2025 — USDA canceled",
             size=14, bold=True, color=GOLD)
    text_box(s, 0.85, 2.15, 5.5, 0.4, "the Climate-Smart Commodities program",
             size=11, italic=True, color=MID)
    nums = [
        ("$3.1B", "funding · ≈$23M / project avg"),
        ("135 projects", "canceled"),
        ("14,000 farms", "lost support"),
        ("3.2M acres", "≈0.36% of 900M acres US ag"),
    ]
    ny = 2.65
    for big, lbl in nums:
        text_box(s, 1.05, ny, 1.8, 0.4, big, size=16, bold=True, color=DEEP)
        text_box(s, 2.95, ny, 3.3, 0.4, lbl, size=12, italic=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
        ny += 0.55
    text_box(s, 0.85, 5.45, 5.5, 1.0,
             "Federal policy = tail risk\nfor business models dependent on subsidies",
             size=11, bold=True, italic=True, color=DEEP, line_spacing=1.4, align=PP_ALIGN.CENTER)

    # Right: Verra
    ocean_box(s, 6.8, 1.5, 6.0, 5.0)
    text_box(s, 7.05, 1.65, 5.5, 0.5, "January 2023 — 94% phantom at Verra",
             size=14, bold=True, color=DEEP)
    text_box(s, 7.05, 2.15, 5.5, 0.4, "The Guardian + Die Zeit + SourceMaterial",
             size=11, italic=True, color=MID)
    c = ASSETS / "charts" / "c31-verra-phantom.png"
    if c.exists():
        add_image(s, c, 7.0, 2.6, w=5.7, h=3.0)
    text_box(s, 7.05, 5.8, 5.7, 0.7,
             "94% of Verra forest credits → no real CO₂ reduction.\n"
             "AP7: AI-MRV without direct measurement = scaled greenwashing.",
             size=11, bold=True, italic=True, color=GOLD, line_spacing=1.4)

    add_footer(s, "Sources: USDA press 2025-04-14; The Guardian 2023-01; SourceMaterial 2023")
    add_speaker_notes(s, load_speaker_notes("s31"))

    # ============ s32 РФ L4 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L4 in Russia — X5 parity, Magnit hybrid, RSHB — \"vapor\"",
        size=22)

    c = ASSETS / "charts" / "c32-rus-retail.png"
    if c.exists():
        add_image(s, c, 0.6, 1.5, w=6.4, h=4.5)

    # Right cards
    cards = [
        ("X5 «Perekrestok»", "ML since 2020 · 200+ factors", "World-class. Works.", LIGHT),
        ("Magnit F&R", "Hybrid: forecasting ✓, replenishment — pilot",
         "Forecasting on 46 DCs Jan 2026 — in production.\nReplenishment on 3 DCs — pilot.", MID),
        ("RSHB AI services", "Announced, no metrics",
         "\"Vapor\" risk: declarations without production metrics.", GOLD),
    ]
    cy = 1.5
    for name, kpi, desc, color in cards:
        ocean_box(s, 7.3, cy, 5.5, 1.6, fill=GOLD_TINT if color == GOLD else LIGHT_TINT, stroke=color)
        text_box(s, 7.5, cy + 0.1, 5.1, 0.4, name,
                 size=14, bold=True, color=DEEP)
        text_box(s, 7.5, cy + 0.5, 5.1, 0.4, kpi,
                 size=12, bold=True, color=color, italic=True)
        text_box(s, 7.5, cy + 0.95, 5.1, 0.6, desc,
                 size=10, color=DARK_GREY, italic=True, line_spacing=1.4)
        cy += 1.7

    ocean_box(s, 0.6, 6.2, 12.13, 0.7, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 6.3, 11.6, 0.5,
             "Pattern: L4-L5 parity alongside an L1-L2 lag. GigaChat — a demo episode, not deployment.",
             size=12, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Sources: Habr Magnit 2026-01; TAdviser X5 Tech 2024")
    add_speaker_notes(s, load_speaker_notes("s32"))

    # ============ s33 section4bis divider — Среда ============
    # Use just "4" — title клейс different by «Раздел 4-bis»
    section_divider(prs, 4, "Section 4-bis — Environment",
        "Cross-cutting themes: connectivity · vendor lock-in · regulation. Without them, no rung of the ladder works.",
        current_section=5,
        caption="3 sub-blocks (connectivity / vendor lock-in double optic / regulation) · 3 anti-AI criteria (AP5, AP6, AP7)")
    add_speaker_notes(prs.slides[-1], load_speaker_notes("s33"))

    # ============ s34 Connectivity + GNSS ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Connectivity — 18% of farms without internet + GNSS interference in Q1 2025",
        size=22)

    # Top: 3 mega-numbers — с baselines
    nums = [
        ("18%", "≈360k of 2M US farms\nwithout internet (vs <1% urban)", GOLD),
        ("123,000", "≈1.2% of 10M flights\nQ1 2025 (vs <1k Q1 2022)", DEEP),
        ("Apr 2026", "Starlink ban in Russia", LIGHT),
    ]
    nx = 0.6; ny = 1.5
    nw = 3.95
    for big, lbl, color in nums:
        ocean_box(s, nx, ny, nw, 1.5, fill=GOLD_TINT if color == GOLD else LIGHT_TINT, stroke=color)
        text_box(s, nx, ny + 0.15, nw, 0.6, big,
                 size=30, bold=True, color=color, align=PP_ALIGN.CENTER)
        text_box(s, nx, ny + 0.9, nw, 0.55, lbl,
                 size=11, color=DEEP, italic=True, align=PP_ALIGN.CENTER, line_spacing=1.3)
        nx += nw + 0.15

    # Map/photo + alternative
    ocean_box(s, 0.6, 3.3, 6.0, 3.0)
    p = ASSETS / "photos" / "p34-gnss-satellites.png"
    if p.exists():
        add_image(s, p, 0.85, 3.5, w=5.5, h=2.6)
    else:
        p = ASSETS / "photos" / "p34-gps-block.jpg"
        if p.exists():
            add_image(s, p, 0.85, 3.5, w=5.5, h=2.6)

    ocean_box(s, 6.8, 3.3, 6.0, 3.0, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, 3.5, 5.5, 0.5, "AP5 + alternative",
             size=15, bold=True, color=GOLD)
    text_box(s, 7.05, 4.0, 5.5, 0.8,
             "AP5: a cloud-first approach for no-network settings =\n"
             "an architectural error.",
             size=12, color=DEEP, italic=True, line_spacing=1.4)
    hr_line(s, 7.05, 4.85, 5.5, color=GOLD, weight=1.0)
    text_box(s, 7.05, 5.0, 5.5, 0.4, "Alternative: on-device ML (edge / TinyML)",
             size=12, bold=True, color=DEEP)
    text_box(s, 7.05, 5.45, 5.5, 0.8,
             "• model inference right on the device\n"
             "• minimal cloud connectivity\n"
             "• works under GNSS interference",
             size=10, color=DARK_GREY, italic=True, line_spacing=1.5)

    add_footer(s, "Sources: Stanford GPS Lab ITM 2025; ICAO 2025 (Switzerland / Finland / Estonia)")
    add_speaker_notes(s, load_speaker_notes("s34"))

    # ============ s30b vendor lock-in double optic ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Vendor lock-in — the John Deere double optic",
        size=24)

    # Left: anti-theft success
    ocean_box(s, 0.6, 1.5, 6.0, 5.0, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.85, 1.65, 5.5, 0.5, "May 2022 — anti-theft success",
             size=15, bold=True, color=LIGHT)
    text_box(s, 0.85, 2.15, 5.5, 0.4, "Melitopol, occupied territory",
             size=11, italic=True, color=MID)
    text_box(s, 0.85, 2.65, 5.5, 1.5,
             "Remote John Deere lock-out:\n"
             "27 units of machinery\n"
             "worth $5M turned into\n"
             "bricks by the manufacturer's decision.",
             size=12, color=DEEP, italic=True, line_spacing=1.4)
    p = ASSETS / "photos" / "p30b-fpv-drone.jpg"
    if p.exists():
        add_image(s, p, 0.85, 4.5, w=5.5, h=1.7)
    text_box(s, 0.85, 6.25, 5.5, 0.3,
             "AI security feature — a success within this loop",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Right: control surface optic
    ocean_box(s, 6.8, 1.5, 6.0, 5.0, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, 1.65, 5.5, 0.5, "Jan 2025 — FTC v. Deere",
             size=15, bold=True, color=GOLD)
    text_box(s, 7.05, 2.15, 5.5, 0.4, "Decade-long repair restrictions",
             size=11, italic=True, color=MID)
    text_box(s, 7.05, 2.65, 5.5, 1.8,
             "The same mechanism:\n"
             "remote lock-out = security today =\n"
             "a control surface tomorrow. The farmer\n"
             "cannot repair without\n"
             "the vendor's permission.",
             size=12, color=DEEP, italic=True, line_spacing=1.4)
    hr_line(s, 7.05, 4.5, 5.5, color=GOLD, weight=1.2)
    text_box(s, 7.05, 4.65, 5.5, 0.4, "December 2025 — FCC banned DJI",
             size=13, bold=True, color=DEEP)
    text_box(s, 7.05, 5.05, 5.5, 1.4,
             "80-90% of US agricultural drones lost\n"
             "legal status. One FCC decision —\n"
             "vendor lock-in became a geopolitical risk.",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.5)

    add_footer(s, "Sources: The Register 2022-05-02; CSO Online 572811; FTC press release 2025-01-15")
    add_speaker_notes(s, load_speaker_notes("s30b"))

    # ============ s35 regulatory 3-col ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Regulation — EU AI Act vs USDA vs \"Agriculture of the Future\"",
        size=22)

    cols = [
        ("EU AI Act", "Regulation 2024/1689",
         "• Ag machinery — high risk\n"
         "• Feb 2025 — operator obligated\n"
         "• AI literacy mandatory\n"
         "• Liability chain: vendor → operator",
         "Strict, enforceable", GOLD),
        ("USDA AI Strategy", "FY2025-26",
         "• Formal declaration\n"
         "• Climate-Smart canceled\n"
         "• No mandatory AI literacy\n"
         "• No high-risk classification",
         "Formal, weak enforcement", DEEP),
        ("Russia \"Agriculture of the Future\"", "Decree 31.12.2025",
         "• Declarative program\n"
         "• Previous one (Agriculture 2024) –3.2%\n"
         "• No measurable indicators\n"
         "• No vendor liability",
         "Declarative, unverified", LIGHT),
    ]
    col_w = 3.95; col_h = 5.2; gap = 0.18
    sx = 0.6; sy = 1.5
    for i, (name, src, body, summary, color) in enumerate(cols):
        x = sx + i * (col_w + gap)
        ocean_box(s, x, sy, col_w, col_h,
                  fill=GOLD_TINT if color == GOLD else LIGHT_TINT, stroke=color)
        text_box(s, x + 0.15, sy + 0.1, col_w - 0.3, 0.5, name,
                 size=16, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x + 0.15, sy + 0.6, col_w - 0.3, 0.4, src,
                 size=11, italic=True, color=MID, align=PP_ALIGN.CENTER)
        hr_line(s, x + 0.2, sy + 1.05, col_w - 0.4, color=color, weight=1.0)
        text_box(s, x + 0.2, sy + 1.2, col_w - 0.4, 3.0, body,
                 size=11, color=DARK_GREY, line_spacing=1.6)
        ocean_box(s, x + 0.2, sy + col_h - 0.85, col_w - 0.4, 0.7,
                  fill=color, stroke=color)
        text_box(s, x + 0.2, sy + col_h - 0.85, col_w - 0.4, 0.7, summary,
                 size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Sources: Cambridge EJRR 2024; USDA AI Strategy FY2025-26; Decree of the Government of the Russian Federation 31.12.2025")
    add_speaker_notes(s, load_speaker_notes("s35"))

    # ============ s36 section5 divider — Полка ============
    section_divider(prs, 5, "Section 5 — L5 «Shelf» + 5 criteria",
        "Retail AI is mature + five anti-AI criteria + checklist + career landscape + callback to Plenty.",
        current_section=6,
        caption="L5 briefly (Walmart, Tesco, X5) + 5 criteria + checklist + careers + closing callback")
    add_speaker_notes(prs.slides[-1], load_speaker_notes("s36"))

    # ============ s37s L5 retail — 2×2 grid (D1 Магнит F&R as 4th card) ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L5 — Walmart Eden + Tesco AI + X5 «Perekrestok» + Magnit F&R (hybrid)",
        size=22)

    cards = [
        ("Walmart Eden", "ML since 2017",
         "Perishables forecasting +\nfreshness routing across 11,000+ stores",
         GOLD),
        ("Tesco AI", "−30% food waste",
         "Since 2017 — daily forecasting\nfor ~3,500 UK supermarkets",
         MID),
        ("X5 «Perekrestok»", "ML since 2020 · 200+ factors",
         "Russian L5 flagship.\nWorld-class.",
         LIGHT),
        ("Magnit F&R (hybrid)", "Forecasting ✓ · Replenishment — pilot",
         "Forecasting on 46 DCs January 2026 — in production.\nReplenishment — pilot on 3 DCs.",
         TEAL),
    ]
    # 2×2 grid
    card_w = 6.0; card_h = 2.5; gap_x = 0.18; gap_y = 0.15
    sx = 0.6; sy = 1.5
    for i, (name, kpi, desc, color) in enumerate(cards):
        col = i % 2
        row = i // 2
        x = sx + col * (card_w + gap_x)
        y = sy + row * (card_h + gap_y)
        is_teal = (color == TEAL)
        ocean_box(s, x, y, card_w, card_h,
                  fill=GOLD_TINT if color == GOLD else (TEAL_TINT if is_teal else LIGHT_TINT),
                  stroke=color)
        icon_p = ASSETS / "icons" / "shopping-cart-96.png"
        if icon_p.exists():
            add_image(s, icon_p, x + 0.2, y + 0.25, w=0.7, h=0.7)
        text_box(s, x + 1.05, y + 0.2, card_w - 1.2, 0.45, name,
                 size=15, bold=True, color=DEEP)
        text_box(s, x + 1.05, y + 0.65, card_w - 1.2, 0.4, kpi,
                 size=13, bold=True, color=color, line_spacing=1.2)
        text_box(s, x + 0.2, y + 1.15, card_w - 0.4, 1.25, desc,
                 size=11, color=DARK_GREY, italic=True, line_spacing=1.4)

    # Bottom caveat row (compact)
    ocean_box(s, 0.6, 6.85, 12.13, 0.45, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 6.88, 11.6, 0.35,
             "⚠ Caveat: L5 is retail AI, not agriculture. Magnit F&R — the \"hybrid\" nuance: forecasting in production, replenishment a pilot.",
             size=11, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Walmart corporate 2025 · Tesco AI annual report · X5 Tech 2024 · Habr Magnit 2026-01")
    add_speaker_notes(s, load_speaker_notes("s37s"))

    # ============ s38s 5 criteria matrix ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Five anti-AI criteria — the key takeaway of the lecture",
        size=24)

    # 5 row matrix: criterion / example / alternative
    rows_data = [
        ("AP1", "Thermodynamics > AI", "Plenty Compton: $940M in losses",
         "Not AI · open field or\ndifferent unit economics"),
        ("AP3", "Accuracy ≠ deployment", "Plantix 85% × 10M = ~100k errors",
         "Calibrated confidence +\nabstention"),
        ("AP4", "Generic LLM as advisor", "Tzachor: 56-71% wrong",
         "AI with source verification +\nhuman-in-the-loop"),
        ("AP6", "AI equipment = vendor lock-in", "Deere $5M + FTC + DJI ban",
         "Open standards / multi-vendor"),
        ("AP7", "AI-MRV without direct measurement", "Verra: 94% phantom credits",
         "Soil sampling + satellite physics"),
    ]

    # Header row
    matrix_x = 0.6
    matrix_y = 1.5
    headers = ["#", "Criterion \"when not AI\"", "Failure example", "Alternative"]
    col_widths = [0.9, 3.8, 3.85, 3.58]
    row_h = 0.45

    cx = matrix_x
    for hdr, w in zip(headers, col_widths):
        ocean_box(s, cx, matrix_y, w, row_h, fill=DEEP, stroke=DEEP)
        text_box(s, cx, matrix_y, w, row_h, hdr,
                 size=12, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        cx += w + 0.05

    # Data rows
    row_h_data = 0.95
    for ri, (code, crit, example, alt) in enumerate(rows_data):
        cx = matrix_x
        ry = matrix_y + row_h + 0.05 + ri * (row_h_data + 0.05)
        fill = SURFACE if ri % 2 == 0 else LIGHT_TINT
        ocean_box(s, cx, ry, col_widths[0], row_h_data,
                  fill=GOLD, stroke=GOLD)
        text_box(s, cx, ry, col_widths[0], row_h_data, code,
                 size=14, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        cx += col_widths[0] + 0.05
        ocean_box(s, cx, ry, col_widths[1], row_h_data, fill=fill, stroke=LIGHT, stroke_pt=0.5)
        text_box(s, cx + 0.1, ry, col_widths[1] - 0.2, row_h_data, crit,
                 size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.3)
        cx += col_widths[1] + 0.05
        ocean_box(s, cx, ry, col_widths[2], row_h_data, fill=fill, stroke=LIGHT, stroke_pt=0.5)
        text_box(s, cx + 0.1, ry, col_widths[2] - 0.2, row_h_data, example,
                 size=11, color=DARK_GREY, italic=True, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.3)
        cx += col_widths[2] + 0.05
        ocean_box(s, cx, ry, col_widths[3], row_h_data, fill=GOLD_TINT, stroke=GOLD, stroke_pt=0.5)
        text_box(s, cx + 0.1, ry, col_widths[3] - 0.2, row_h_data, alt,
                 size=11, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.3)

    # Bottom: AP2a / AP2b / AP5 inline note
    text_box(s, 0.6, 6.85, 12.13, 0.3,
             "Also: AP2a (architecture choice within AI) · AP2b (deterministic alternative) · AP5 (cloud-first off-grid)",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    add_speaker_notes(s, load_speaker_notes("s38s"))

    # ============ s35c checklist 5 blocks ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Pre-purchase verification checklist for an AI solution",
        size=24)

    blocks = [
        ("Task classification", "1. Narrow or general-purpose?",
         "2. Closed-loop or open environment?"),
        ("Production status", "3. Production metrics vs announcements?",
         "4. Is there independent verification?"),
        ("Accountability", "5. Vendor liability chain?",
         "6. SLA on AI-functionality failures?"),
        ("Vendor lock-in", "7. Open data standards?",
         "8. Interoperability with other vendors?"),
        ("Connectivity", "9. On-device fallback when\n   internet is absent?",
         "10. Alternative to GNSS navigation?"),
    ]
    block_w = 2.42; block_h = 4.5; gap = 0.1
    sx = 0.6; sy = 1.5
    for i, (name, q1, q2) in enumerate(blocks):
        x = sx + i * (block_w + gap)
        ocean_box(s, x, sy, block_w, block_h)
        # Numbered header
        ocean_box(s, x + 0.15, sy + 0.2, block_w - 0.3, 0.55,
                  fill=GOLD, stroke=GOLD)
        text_box(s, x + 0.15, sy + 0.2, block_w - 0.3, 0.55,
                 f"Block {i+1}", size=12, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Block name
        text_box(s, x + 0.15, sy + 0.9, block_w - 0.3, 0.7, name,
                 size=12, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.2)
        # Questions
        hr_line(s, x + 0.2, sy + 1.65, block_w - 0.4, color=LIGHT, weight=1.0)
        text_box(s, x + 0.2, sy + 1.8, block_w - 0.4, 1.3, q1,
                 size=10, color=DEEP, line_spacing=1.4)
        text_box(s, x + 0.2, sy + 3.1, block_w - 0.4, 1.3, q2,
                 size=10, color=DEEP, line_spacing=1.4)

    # Scoring
    ocean_box(s, 0.6, 6.2, 12.13, 0.7, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 6.25, 11.6, 0.3,
             "Scoring: 8-10 \"yes\" = buy/pilot · 5-7 = conditional · ≤4 = reject",
             size=14, bold=True, color=DEEP)
    text_box(s, 0.85, 6.55, 11.6, 0.3,
             "Answer — not in the vendor's words, but from external sources: independent audits, FTC press releases, industry reports.",
             size=10, italic=True, color=DARK_GREY)

    add_speaker_notes(s, load_speaker_notes("s35c"))

    # ============ s36c career landscape ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Career landscape — L1-L5 segments + the Russian market",
        size=24)

    segments = [
        ("L1 Field", "John Deere · Bayer · BASF\nClimate · Taranis · Granular",
         "Cognitive Pilot · ITELMA\nEFKO · Geoscan · ExactFarming", LIGHT),
        ("L2 Robot", "Carbon Robotics · Saga · Tevel\nAGCO · Aigen", "(niche RU startups)", MID),
        ("L3 Animal", "DeLaval · GEA · Lely\nCargill Birdoo · Allflex", "Connectome.ai · Skolkovo", LIGHT),
        ("L4 Supply chain", "Cargill CMAX · Tract · Olam\nADM · Walmart×Cropin", "X5 Tech · Magnit digital\nRusagro Tech · RSHB.digital", GOLD),
        ("L5 Shelf", "Walmart Eden · Tesco AI\nWooliesX · Carrefour AI", "X5 «Perekrestok»\n(world-class)", MID),
    ]
    seg_w = 2.42; seg_h = 4.7; gap = 0.1
    sx = 0.6; sy = 1.5
    for i, (name, intl, ru, color) in enumerate(segments):
        x = sx + i * (seg_w + gap)
        ocean_box(s, x, sy, seg_w, seg_h,
                  fill=GOLD_TINT if color == GOLD else LIGHT_TINT, stroke=color)
        text_box(s, x + 0.1, sy + 0.15, seg_w - 0.2, 0.5, name,
                 size=14, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER)
        hr_line(s, x + 0.2, sy + 0.7, seg_w - 0.4, color=color, weight=1.0)
        # International
        text_box(s, x + 0.1, sy + 0.85, seg_w - 0.2, 0.4, "International",
                 size=10, bold=True, color=MID, align=PP_ALIGN.CENTER)
        text_box(s, x + 0.15, sy + 1.25, seg_w - 0.3, 1.5, intl,
                 size=10, color=DEEP, italic=True, align=PP_ALIGN.CENTER, line_spacing=1.4)
        # RU
        text_box(s, x + 0.1, sy + 3.0, seg_w - 0.2, 0.4, "Russian",
                 size=10, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
        text_box(s, x + 0.15, sy + 3.4, seg_w - 0.3, 1.3, ru,
                 size=10, color=DEEP, italic=True, align=PP_ALIGN.CENTER, line_spacing=1.4)

    add_footer(s, "Market landscape without advocacy. Generic form — \"specialized technical universities\"")
    add_speaker_notes(s, load_speaker_notes("s36c"))

    # ============ s37 closing hero + 5-level ladder recap (D3) ============
    s = blank(prs); set_slide_bg(s, WHITE)

    # Top callback box
    ocean_box(s, 0.6, 0.3, 12.13, 1.9, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 0.4, 11.6, 0.35,
             "Callback to the start of the lecture (Plenty Compton):",
             size=12, italic=True, color=GOLD, bold=True)
    text_box(s, 0.85, 0.8, 11.6, 0.55,
             "Plenty did not close because of bad AI.",
             size=22, bold=True, color=DEEP)
    text_box(s, 0.85, 1.4, 11.6, 0.55,
             "Plenty closed because of LED thermodynamics.",
             size=22, bold=True, color=GOLD)
    text_box(s, 0.85, 1.95, 11.6, 0.25,
             "The controller worked. CV recognized. The model trained. LED ≈ 100× sunlight energy — AP1.",
             size=10, italic=True, color=DARK_GREY)

    # Mid: 5-level mini-ladder recap (D3 — на каждый уровень success / failure)
    text_box(s, 0.6, 2.4, 12.13, 0.35,
             "For each rung of the ladder — what works and what breaks:",
             size=14, bold=True, color=DEEP, align=PP_ALIGN.CENTER, italic=True)

    ladder = [
        ("L1 Field",       "See & Spray (5M acres)",           "Plenty / Bowery (thermodynamics)"),
        ("L2 Robot",       "LaserWeeder G2 (narrow laser)",     "Monarch (demo ≠ deployment)"),
        ("L3 Animal",      "SenseHub (2M cows)",                "Cainthus / tie-stall housing"),
        ("L4 Supply chain", "Cargill CMAX (narrow agent)",      "USDA Climate-Smart / Verra 94%"),
        ("L5 Shelf",       "Walmart Eden / Tesco / X5",         "GNSS jamming Finland"),
    ]
    ladder_x = 0.6
    ladder_y = 2.8
    row_h = 0.42
    # Header
    headers = [("Level", 2.0, DEEP), ("✓ Works", 5.0, LIGHT), ("✗ Breaks", 5.13, GOLD)]
    cx = ladder_x
    for hdr, w, color in headers:
        ocean_box(s, cx, ladder_y, w, row_h, fill=color, stroke=color)
        text_box(s, cx, ladder_y, w, row_h, hdr,
                 size=12, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        cx += w + 0.0
    ladder_y += row_h + 0.03
    for i, (lvl, success, failure) in enumerate(ladder):
        cx = ladder_x
        fill = SURFACE if i % 2 == 0 else LIGHT_TINT
        # Level
        ocean_box(s, cx, ladder_y, 2.0, row_h, fill=fill, stroke=LIGHT, stroke_pt=0.5)
        text_box(s, cx + 0.1, ladder_y, 1.8, row_h, lvl,
                 size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        cx += 2.0
        # Success
        ocean_box(s, cx, ladder_y, 5.0, row_h, fill=fill, stroke=LIGHT, stroke_pt=0.5)
        text_box(s, cx + 0.1, ladder_y, 4.8, row_h, success,
                 size=11, color=DEEP, italic=True, anchor=MSO_ANCHOR.MIDDLE)
        cx += 5.0
        # Failure
        ocean_box(s, cx, ladder_y, 5.13, row_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=0.5)
        text_box(s, cx + 0.1, ladder_y, 4.93, row_h, failure,
                 size=11, color=DARK_GREY, italic=True, anchor=MSO_ANCHOR.MIDDLE)
        ladder_y += row_h + 0.03

    # Bottom: main payoff + bridge to L11
    ocean_box(s, 0.6, 5.5, 6.5, 1.4, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.8, 5.6, 6.1, 0.4,
             "The engineer holds the whole ladder in mind",
             size=14, bold=True, color=DEEP)
    text_box(s, 0.8, 6.0, 6.1, 0.85,
             "and picks the right tool for each rung.\n"
             "Knows where AI does not work — and why.",
             size=12, color=MID, italic=True, line_spacing=1.4)

    # Bridge box
    ocean_box(s, 7.3, 5.5, 5.45, 1.4, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.5, 5.6, 5.05, 0.4, "Transition to Lecture 11",
             size=14, bold=True, color=GOLD)
    text_box(s, 7.5, 6.0, 5.05, 0.9,
             "L11 — cyber-physical manufacturing. A closed loop\n"
             "like L4-L5 + physical contact of AI with the product like L2.",
             size=11, color=DEEP, italic=True, line_spacing=1.4)

    add_footer(s, "Thank you. Next — questions and answers")
    add_speaker_notes(s, load_speaker_notes("s37"))

    # ============ s38 dedicated Q&A ============
    s = blank(prs); set_slide_bg(s, WHITE)

    # Big Q&A typography
    text_box(s, 0.6, 0.5, 12.13, 2.5, "Questions and answers",
             size=64, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             font=H["FONT_HEAD"])

    text_box(s, 0.6, 3.2, 12.13, 0.5, "Backup questions on VF thermodynamics, agentic AI scope, ITELMA vs Cognitive Pilot, foundation models",
             size=14, italic=True, color=MID, align=PP_ALIGN.CENTER)

    # 3 backup prompts
    text_box(s, 0.6, 4.3, 12.13, 0.4, "Backup questions",
             size=14, bold=True, color=MID, align=PP_ALIGN.CENTER)

    prompts = [
        ("Plenty and Bowery", "Why vertical farms specifically in the US?\nIn a closed environment — US vs Japan vs UAE?"),
        ("Agentic AI", "Where else does agentic AI work\nin engineering tasks — besides hedging?"),
        ("Cognitive and ITELMA", "Can a hybrid solution be built\nCV + sensor fusion, or are these different paradigms?"),
    ]
    pw = 3.95; ph = 1.8; gap = 0.15
    sx = 0.6; sy = 4.8
    for i, (q, body) in enumerate(prompts):
        x = sx + i * (pw + gap)
        ocean_box(s, x, sy, pw, ph)
        text_box(s, x + 0.15, sy + 0.1, pw - 0.3, 0.4, q,
                 size=12, bold=True, color=GOLD)
        text_box(s, x + 0.15, sy + 0.55, pw - 0.3, ph - 0.7, body,
                 size=10, color=DARK_GREY, italic=True, line_spacing=1.4)

    add_speaker_notes(s, load_speaker_notes("s38"))

    return prs
