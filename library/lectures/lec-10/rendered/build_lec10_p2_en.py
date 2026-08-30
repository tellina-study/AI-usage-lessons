"""
Part 2: s15-s21 + s17 — Раздел 2 «L2 Робот». 7 слайдов: divider + LaserWeeder + 4 cases + РФ-параллель.
"""

def build_part2(prs, H):
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

    # ============ s15 section2 divider — L2 Робот ============
    section_divider(prs, 2, "Section 2 — L2 “Robot”",
        "Specialization beats generalization. Narrow wins against generic failures.",
        current_section=2,
        caption="4 working specialization cases · 3 failures (Monarch, FarmWise, strawberry) · Russia parallel CV vs sensor-fusion")
    s_last = prs.slides[-1]
    add_speaker_notes(s_last, load_speaker_notes("s15"))

    # ============ s16 LaserWeeder G2 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Carbon Robotics LaserWeeder G2 — the canonical L2 success",
        size=24)

    # Left: hero "photo" placeholder + spec card (since no real LaserWeeder photo)
    ocean_box(s, 0.6, 1.5, 7.5, 5.1)
    # Use FarmWise-titan as visual stand-in
    p = ASSETS / "photos" / "p20-farmwise-titan.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.75, w=7.0, h=4.2)
    text_box(s, 0.85, 6.05, 7.0, 0.3,
             "AI-driven weeding robot (representative photo · “Titan / LaserWeeder” class)",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Right: 4 KPI cards — с baseline counterfactuals
    kpis = [
        ("250,000 acres", "≈0.028% of 900M acres US ag", GOLD),
        ("15 billion", "weeds killed", DEEP),
        ("$1.4M", "vs sprayer ~$50k + chemicals $200-400/acre → payback 3-4 years at 1k+ acres", LIGHT),
        ("240 W laser", "+ CNN on 40 million images", MID),
    ]
    cy = 1.5
    for big, lbl, color in kpis:
        ocean_box(s, 8.3, cy, 4.45, 1.15, fill=LIGHT_TINT if color != GOLD else GOLD_TINT)
        text_box(s, 8.5, cy + 0.1, 4.1, 0.55, big, size=24, bold=True, color=color)
        text_box(s, 8.5, cy + 0.65, 4.1, 0.45, lbl,
                 size=13, color=DEEP, italic=True)
        cy += 1.25

    # Bottom: principle
    ocean_box(s, 0.6, 6.55, 12.13, 0.4, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 6.58, 11.6, 0.32,
             "Replacing chemistry with physics — a narrow operation substitution, not an “autonomous tractor.” The working L2 pattern.",
             size=13, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Source: Carbon Robotics press release, businesswire 2025-02-10")
    add_speaker_notes(s, load_speaker_notes("s16"))

    # ============ s17 Cognitive Pilot vs ИТЭЛМА — RU parallel ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Cognitive Pilot and ITELMA are not AI vs non-AI; they are two different classes of AI",
        size=20)

    # 2-column architecture comparison
    col_w = 5.95; col_h = 5.0
    cy = 1.5

    # LEFT: Cognitive Pilot CV
    ocean_box(s, 0.6, cy, col_w, col_h, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.8, cy + 0.1, col_w - 0.4, 0.5, "Cognitive Pilot · computer vision",
             size=15, bold=True, color=DEEP)
    text_box(s, 0.8, cy + 0.55, col_w - 0.4, 0.4, "“What I see”",
             size=11, italic=True, color=MID)
    hr_line(s, 0.8, cy + 1.05, col_w - 0.4, color=LIGHT, weight=1.0)
    text_box(s, 0.8, cy + 1.2, col_w - 0.4, 0.4,
             "1700+ installations (tractors, combines)",
             size=12, bold=True, color=DEEP)
    text_box(s, 0.8, cy + 1.6, col_w - 0.4, 0.4,
             "4 farmer lawsuits (~₽12.7M)",
             size=12, bold=True, color=GOLD)
    text_box(s, 0.8, cy + 2.05, col_w - 0.4, 0.5,
             "Failure mode:", size=11, italic=True, color=MID)
    text_box(s, 0.8, cy + 2.45, col_w - 0.4, 2.0,
             "• dust obscures the cameras\n"
             "• shadow shift changes the lighting\n"
             "• edge-row recognition breaks down\n"
             "• benchmark labeling ≠ field conditions\n"
             "• edge cases not in the training set",
             size=11, color=DARK_GREY, line_spacing=1.5)

    # RIGHT: ИТЭЛМА Квадро
    ocean_box(s, 6.85, cy, col_w, col_h, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, cy + 0.1, col_w - 0.4, 0.5, "ITELMA Kvadro · sensor fusion",
             size=15, bold=True, color=DEEP)
    text_box(s, 7.05, cy + 0.55, col_w - 0.4, 0.4, "Navigation + inertial + corrections: “where I am”",
             size=11, italic=True, color=MID)
    hr_line(s, 7.05, cy + 1.05, col_w - 0.4, color=GOLD, weight=1.0)
    text_box(s, 7.05, cy + 1.2, col_w - 0.4, 0.4,
             "GLONASS + GPS + Galileo + BeiDou",
             size=12, bold=True, color=DEEP)
    text_box(s, 7.05, cy + 1.6, col_w - 0.4, 0.4,
             "RTK correction: accuracy 2-5 cm",
             size=12, bold=True, color=GOLD)
    text_box(s, 7.05, cy + 2.05, col_w - 0.4, 0.5,
             "Why it works:", size=11, italic=True, color=MID)
    text_box(s, 7.05, cy + 2.45, col_w - 0.4, 2.0,
             "• sensors do not depend on lighting\n"
             "• multiple systems = redundancy\n"
             "• GLONASS works in Russia independently\n"
             "• stable in dust / fog / at night\n"
             "• compatible with deterministic guidance",
             size=11, color=DARK_GREY, line_spacing=1.5)

    add_footer(s, "Sources: RTVI 2025 (Cognitive Pilot lawsuits); Fontanka 2026-01-26 (ITELMA)")
    add_speaker_notes(s, load_speaker_notes("s17"))

    # ============ s18 4 узких победы L2 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Narrow L2 wins — Solinftec, Saga UV-C, Tevel, AGCO Outrun",
        size=22)

    cases = [
        ("Solinftec Solix", "+243% year over year in 2025",
         "Vendor self-report: ≤98%\nreduction in contact herbicides",
         "tractor"),
        ("Saga UV-C", "20% of UK strawberries",
         "Ultraviolet nighttime treatment.\nNot harvesting — disease control",
         "leaf"),
        ("Tevel", "Apple-picking drones",
         "Narrow niche — flying\ndrones for picking apples",
         "package"),
        ("AGCO PTx Outrun", "Retrofit for mixed fleets",
         "AGCO module for a mixed\ntractor fleet (not AGCO only)",
         "tractor"),
    ]
    card_w = 2.85; card_h = 4.2; gap = 0.18
    sx = 0.6
    sy = 1.6
    for i, (name, kpi, desc, icon_name) in enumerate(cases):
        x = sx + i * (card_w + gap)
        ocean_box(s, x, sy, card_w, card_h)
        icon_p = ASSETS / "icons" / f"{icon_name}-96.png"
        if icon_p.exists():
            add_image(s, icon_p, x + (card_w - 0.85) / 2, sy + 0.25, w=0.85, h=0.85)
        text_box(s, x + 0.15, sy + 1.3, card_w - 0.3, 0.5, name,
                 size=14, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.2)
        text_box(s, x + 0.15, sy + 1.85, card_w - 0.3, 0.6, kpi,
                 size=13, bold=True, color=GOLD, align=PP_ALIGN.CENTER, line_spacing=1.2)
        text_box(s, x + 0.15, sy + 2.5, card_w - 0.3, 1.5, desc,
                 size=10, color=DARK_GREY, italic=True, line_spacing=1.4,
                 align=PP_ALIGN.CENTER)

    # Bottom note about specialization
    ocean_box(s, 0.6, 6.0, 12.13, 0.85, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 6.1, 11.6, 0.35,
             "The specialization pattern: every solution is narrow and measurable",
             size=13, bold=True, color=DEEP)
    text_box(s, 0.85, 6.45, 11.6, 0.35,
             "⚠ Do not confuse: Saga UV-C ≠ Saga for harvesting. Those 20% of UK strawberries are disease control, not harvesting.",
             size=11, italic=True, color=GOLD, line_spacing=1.3)

    add_footer(s, "Sources: Solinftec.com · sagarobotics.com · tevel-tech.com · agcocorp.com 2025")
    add_speaker_notes(s, load_speaker_notes("s18"))

    # ============ s19 Monarch failure timeline ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Monarch Tractor — “autonomous” with autonomy broken",
        size=24)

    # Timeline 2018-2026 — compact, fits within 0.6-12.73 inches
    events = [
        ("2018", "Founded", "Livermore, CA", LIGHT),
        ("2022", "MK-V demo", "Big PR wave", MID),
        ("Sept 2025", "Burks Tractor lawsuit", "10 tractors · $773,088\n“unable to operate\nautonomously”", GOLD),
        ("Nov 2025", "102 layoffs", "~38% (102 / ~270\nafter 10% cut Nov 2024)", GOLD),
        ("Apr 2026", "Caterpillar\nacqui-hire", "End of independence", DEEP),
    ]

    tline_y = 2.0
    n = len(events)
    # Tighter range — pull endpoints inward
    line_x_start = 1.4
    line_x_end = 11.9
    line_w = line_x_end - line_x_start
    # Draw horizontal line
    hr_line(s, line_x_start, tline_y, line_w, color=LIGHT, weight=2.5)
    # Card dimensions
    card_w = 2.05
    # Dots
    for i, (year, hdr, desc, color) in enumerate(events):
        x = line_x_start + (line_w / (n - 1)) * i
        dot_x = x - 0.18
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, H["Inches"](dot_x), H["Inches"](tline_y - 0.18),
                                  H["Inches"](0.36), H["Inches"](0.36))
        dot.fill.solid(); dot.fill.fore_color.rgb = color
        dot.line.color.rgb = WHITE; dot.line.width = H["Pt"](2)
        H["disable_shadow"](dot)
        # Year above
        text_box(s, x - card_w/2, tline_y - 0.95, card_w, 0.4, year,
                 size=13, bold=True, color=color, align=PP_ALIGN.CENTER)
        # Card below
        ocean_box(s, x - card_w/2, tline_y + 0.3, card_w, 1.8,
                  fill=GOLD_TINT if color == GOLD else LIGHT_TINT, stroke=color)
        text_box(s, x - card_w/2 + 0.05, tline_y + 0.4, card_w - 0.1, 0.5, hdr,
                 size=11, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.2)
        text_box(s, x - card_w/2 + 0.05, tline_y + 0.95, card_w - 0.1, 1.1, desc,
                 size=9, color=DARK_GREY, italic=True, align=PP_ALIGN.CENTER, line_spacing=1.3)

    # Bottom takeaway
    ocean_box(s, 0.6, 5.0, 12.13, 1.7, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 5.15, 11.6, 0.4,
             "Anti-pattern: demo ≠ production deployment",
             size=16, bold=True, color=DEEP)
    text_box(s, 0.85, 5.6, 11.6, 1.0,
             "“Autonomous” in marketing = a legal trap if the actual behavior depends on the operator.\n"
             "Every autonomy claim must be checked with an independent operator test → if it requires\n"
             "operator presence, the autonomy is partial.",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.4)

    add_footer(s, "Sources: TechCrunch 2025-11-18, 2025-11-19, 2026-04-15")
    add_speaker_notes(s, load_speaker_notes("s19"))

    # ============ s20 FarmWise + Naïo ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "FarmWise wound down + Naïo –40% — the open environment breaks computer vision",
        size=20)

    # Left: cause
    ocean_box(s, 0.6, 1.5, 6.0, 4.6, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.85, 1.65, 5.5, 0.5, "Why the CV stack (computer vision) failed",
             size=14, bold=True, color=DEEP)
    p = ASSETS / "photos" / "p20-farmwise-titan.jpg"
    if p.exists():
        add_image(s, p, 0.85, 2.2, w=5.5, h=2.0)
    text_box(s, 0.85, 4.25, 5.5, 0.3,
             "FarmWise Titan FT35 · wound down in 2025",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 4.6, 5.5, 1.4,
             "FarmWise wound down 2025\nNaïo €4M → €2.4M (–40%)\n"
             "Computer vision trained under greenhouse conditions:\n"
             "• shadow shift (arXiv 2508.19511)\n"
             "• variable lighting\n"
             "• dust / fog",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.4)

    # Right: alternative
    ocean_box(s, 6.8, 1.5, 6.0, 4.6, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, 1.65, 5.5, 0.5, "AP2b — the deterministic alternative",
             size=15, bold=True, color=DEEP)
    p = ASSETS / "photos" / "p20-tractor-mower.jpg"
    if p.exists():
        add_image(s, p, 7.05, 2.2, w=5.5, h=2.0)
    text_box(s, 7.05, 4.25, 5.5, 0.3,
             "Lemken / Kverneland — mechanical cultivator",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, 7.05, 4.6, 5.5, 1.4,
             "Mechanical cultivators as the deterministic\n"
             "option:\n"
             "• stem detection by mechanics\n"
             "• inter-row cultivation\n"
             "• works in any weather\n"
             "• cost 3-5× lower than a CV robot",
             size=11, color=DEEP, italic=True, line_spacing=1.4)

    add_footer(s, "Sources: Farm Progress 2025; arXiv 2508.19511 (shadow bias); Lemken / Kverneland press")
    add_speaker_notes(s, load_speaker_notes("s20"))

    # ============ s21 Strawberry economics ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Strawberry-picking robot — 10 years of pilots, not production deployment",
        size=22)

    # Left photo + chart
    ocean_box(s, 0.6, 1.5, 6.0, 5.1)
    p = ASSETS / "photos" / "p21-strawberry-picker.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.75, w=5.5, h=4.0)
    text_box(s, 0.85, 5.8, 5.5, 0.3,
             "Manual strawberry harvesting (Wikimedia Commons, CC-BY-SA)",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 6.15, 5.5, 0.3,
             "“Harvesting is the last great unsolved problem”",
             size=11, italic=True, bold=True, color=GOLD, align=PP_ALIGN.CENTER)

    # Right: 4 number-cards
    nums = [
        ("$200-350k", "capital cost\nper robot", GOLD),
        ("$68-130k", "annualized depreciation\nper robot", DEEP),
        ("$43k / acre", "cost of manual\nharvesting in California", LIGHT),
        ("<5% of market", "robots × $50B\naddressable labor market", MID),
    ]
    cy = 1.5
    for big, lbl, color in nums:
        ocean_box(s, 6.8, cy, 6.0, 1.2, fill=LIGHT_TINT if color != GOLD else GOLD_TINT)
        text_box(s, 7.0, cy + 0.1, 2.8, 0.6, big,
                 size=22, bold=True, color=color)
        text_box(s, 9.85, cy + 0.2, 2.85, 0.85, lbl,
                 size=11, color=DEEP, italic=True, line_spacing=1.3)
        cy += 1.3

    add_footer(s, "Sources: Wikimedia Commons; RobotToday market analysis 2024")
    add_speaker_notes(s, load_speaker_notes("s21"))
