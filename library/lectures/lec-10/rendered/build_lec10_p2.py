"""
Part 2: s15-s21 + s17 + s16a — Раздел 2 «L2 Робот». 8 слайдов: divider + LaserWeeder +
price-ladder формы разбора + 4 cases + РФ-параллель.
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

    # ============ s15 section2 divider — автономная и роботизированная техника в поле ============
    section_divider(prs, 2, "Раздел 2. Автономная и роботизированная техника в поле",
        "L2 «Робот» — узкая специализация работает; универсальный «autonomous farm robot» банкротится.",
        current_section=2,
        caption="LaserWeeder working case + РФ-параллель CV vs sensor-fusion · 4 working specialization cases · 3 провала (Monarch, FarmWise, strawberry)")
    s_last = prs.slides[-1]
    add_speaker_notes(s_last, load_speaker_notes("s15"))

    # ============ s16 LaserWeeder G2 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Carbon Robotics LaserWeeder G2 — каноничный успех L2",
        size=24)

    # Left: hero photo — REAL Carbon Robotics LaserWeeder G2 (Tier 1 og:image,
    # carbonrobotics.com/laserweeder-g2). Replaces FarmWise Titan cross-contamination
    # (architecture.md K-2.1: that file is reused on s20 as the FAILURE case).
    ocean_box(s, 0.6, 1.5, 7.5, 4.3)
    p = ASSETS / "photos" / "p16-laserweeder-g2-real.jpg"
    if p.exists():
        add_image(s, p, 0.9, 1.7, w=6.75, h=3.8)
    text_box(s, 0.9, 5.55, 6.75, 0.25,
             "Carbon Robotics LaserWeeder G2. Источник: carbonrobotics.com/laserweeder-g2",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Right: 5 KPI cards — метрики + архитектура + цена FP (данные §2.2 часть 2)
    kpis = [
        ("250 000 акров", "≈0,028% из 900M акров US ag", GOLD),
        ("15 млрд", "сорняков уничтожено", DEEP),
        ("$1,4 млн / машина", "крупные овощные и органические хозяйства", LIGHT),
        ("240 Вт лазер", "+ CNN на 40 млн изображений", MID),
        ("≈$90-100/акр", "цена FP — оценка по USDA NASS, не прямой источник", TEAL),
    ]
    cy = 1.5
    card_h = 0.78
    for big, lbl, color in kpis:
        fill = GOLD_TINT if color == GOLD else (TEAL_TINT if color == TEAL else LIGHT_TINT)
        ocean_box(s, 8.3, cy, 4.45, card_h, fill=fill)
        text_box(s, 8.5, cy + 0.05, 4.1, 0.4, big, size=17, bold=True, color=color)
        text_box(s, 8.5, cy + 0.44, 4.1, 0.32, lbl,
                 size=9.5, color=DEEP, italic=True, line_spacing=1.0)
        cy += card_h + 0.065

    # Bottom-left: Economics plashki — Braga Fresh / Triangle Farms, «было → стало → %»
    # (3 explicit short paragraphs each — avoids word-wrap overflow found in iter.1)
    plashka_y = 5.95
    plashka_h = 0.66
    plashka_w = 5.965
    ocean_box(s, 0.6, plashka_y, plashka_w, plashka_h, fill=LIGHT_TINT, stroke=LIGHT, stroke_pt=1.0)
    text_runs(s, 0.78, plashka_y + 0.06, plashka_w - 0.36, plashka_h - 0.12,
        [
            {"text": "Braga Fresh: ", "size": 11, "bold": True, "color": DEEP},
            {"text": "$900/акр → $550/акр", "size": 11, "bold": True, "color": MID},
            {"text": "ручная $282,28 + LaserWeeder $267,72", "size": 9, "italic": True,
             "color": DARK_GREY, "newpara": True},
            {"text": "−39% совокупных затрат на прополку", "size": 11, "bold": True,
             "color": GOLD, "newpara": True},
        ], anchor=MSO_ANCHOR.TOP, line_spacing=1.08)

    tri_x = 6.765
    ocean_box(s, tri_x, plashka_y, plashka_w, plashka_h, fill=LIGHT_TINT, stroke=LIGHT, stroke_pt=1.0)
    text_runs(s, tri_x + 0.18, plashka_y + 0.06, plashka_w - 0.36, plashka_h - 0.12,
        [
            {"text": "Triangle Farms: ", "size": 11, "bold": True, "color": DEEP},
            {"text": "$900/акр → $232,12/акр", "size": 11, "bold": True, "color": MID},
            {"text": "ручная прополка (аругула) устранена полностью", "size": 9, "italic": True,
             "color": DARK_GREY, "newpara": True},
            {"text": "экономия $251,27/акр", "size": 11, "bold": True, "color": GOLD, "newpara": True},
        ], anchor=MSO_ANCHOR.TOP, line_spacing=1.08)

    # Synthesis line — herbicide range + industry-wide ≈40% (shortened to fit 1 line @10pt)
    synth_y = plashka_y + plashka_h + 0.07
    ocean_box(s, 0.6, synth_y, 12.13, 0.3, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, synth_y + 0.02, 11.6, 0.26,
             "Гербицид (исследования себестоимости, США): $200-400/акр/год · Western Growers: прополка дешевле ≈40% после года",
             size=10, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Источники: Carbon Robotics businesswire 2025-02-10 · carbonrobotics.com/laserweeder-g2 · GeekWire 2025 · Western Growers Case Study, март 2024")
    add_speaker_notes(s, load_speaker_notes("s16"))

    # ============ s16a LaserWeeder — форма разбора: цена ошибок + 2 режима ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "LaserWeeder — цена ошибок и два классических режима, $/акр/год",
        size=22)

    step_x = 0.6
    step_w = 12.13
    half_w = (step_w - 0.2) / 2.0

    # Ступень 1 — цена двух ошибок
    s1_y = 1.5
    s1_h = 1.35
    ocean_box(s, step_x, s1_y, half_w, s1_h, fill=TEAL_TINT, stroke=TEAL)
    text_box(s, step_x + 0.18, s1_y + 0.1, half_w - 0.36, 0.32,
             "FP — выжигание культуры", size=13, bold=True, color=DEEP)
    text_box(s, step_x + 0.18, s1_y + 0.46, half_w - 0.36, 0.36,
             "≈$90-100/акр", size=22, bold=True, color=TEAL)
    text_box(s, step_x + 0.18, s1_y + 0.88, half_w - 0.36, 0.42,
             "оценка по USDA NASS (шпинат $487М/52 800 акров × ≤1% подавления роста культуры) — не прямой источник",
             size=10, italic=True, color=DARK_GREY, line_spacing=1.15)

    s1b_x = step_x + half_w + 0.2
    ocean_box(s, s1b_x, s1_y, half_w, s1_h, fill=SOFT_GREY, stroke=DARK_GREY)
    text_box(s, s1b_x + 0.18, s1_y + 0.1, half_w - 0.36, 0.32,
             "FN — пропущенный сорняк", size=13, bold=True, color=DEEP)
    text_box(s, s1b_x + 0.18, s1_y + 0.46, half_w - 0.36, 0.36,
             "не опубликовано", size=20, bold=True, color=DARK_GREY)
    text_box(s, s1b_x + 0.18, s1_y + 0.88, half_w - 0.36, 0.42,
             "вендором — пробел хуже, чем у See & Spray (там есть хотя бы качественная оценка)",
             size=10, italic=True, color=DARK_GREY, line_spacing=1.15)

    # Ступень 2 — два классических режима
    s2_y = s1_y + s1_h + 0.14
    s2_h = 1.25
    ocean_box(s, step_x, s2_y, half_w, s2_h, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, step_x + 0.18, s2_y + 0.1, half_w - 0.36, 0.32,
             "Гербицид (классика)", size=13, bold=True, color=DEEP)
    text_box(s, step_x + 0.18, s2_y + 0.46, half_w - 0.36, 0.36,
             "$200-400/акр/год", size=20, bold=True, color=MID)
    text_box(s, step_x + 0.18, s2_y + 0.86, half_w - 0.36, 0.38,
             "синтез исследований себестоимости (США) · лук Орегон/Айдахо $77,65/акр только химия",
             size=10, italic=True, color=DARK_GREY, line_spacing=1.15)

    ocean_box(s, s1b_x, s2_y, half_w, s2_h, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, s1b_x + 0.18, s2_y + 0.1, half_w - 0.36, 0.32,
             "Ручная прополка (классика)", size=13, bold=True, color=DEEP)
    text_box(s, s1b_x + 0.18, s2_y + 0.46, half_w - 0.36, 0.36,
             "$900/акр/год", size=20, bold=True, color=MID)
    text_box(s, s1b_x + 0.18, s2_y + 0.86, half_w - 0.36, 0.38,
             "базовый уровень для органических листовых культур (baby leaf) — Western Growers Case Study, март 2024",
             size=10, italic=True, color=DARK_GREY, line_spacing=1.15)

    # Ступень 3 — модель против режимов (было → стало → итог)
    s3_y = s2_y + s2_h + 0.14
    s3_h = 1.35
    ocean_box(s, step_x, s3_y, half_w, s3_h, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, step_x + 0.18, s3_y + 0.1, half_w - 0.36, 0.32,
             "Braga Fresh", size=13, bold=True, color=DEEP)
    text_runs(s, step_x + 0.18, s3_y + 0.46, half_w - 0.36, 0.82,
        [
            {"text": "$900/акр → ", "size": 16, "bold": True, "color": DEEP},
            {"text": "$550/акр", "size": 16, "bold": True, "color": MID},
            {"text": "ручная $282,28 + LaserWeeder $267,72", "size": 10, "italic": True,
             "color": DARK_GREY, "newpara": True},
            {"text": "−39% совокупных затрат на прополку", "size": 14, "bold": True,
             "color": GOLD, "newpara": True},
        ], line_spacing=1.2)

    ocean_box(s, s1b_x, s3_y, half_w, s3_h, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, s1b_x + 0.18, s3_y + 0.1, half_w - 0.36, 0.32,
             "Triangle Farms (аругула)", size=13, bold=True, color=DEEP)
    text_runs(s, s1b_x + 0.18, s3_y + 0.46, half_w - 0.36, 0.82,
        [
            {"text": "$900/акр → ", "size": 16, "bold": True, "color": DEEP},
            {"text": "$232,12/акр", "size": 16, "bold": True, "color": MID},
            {"text": "ручная прополка устранена полностью", "size": 10, "italic": True,
             "color": DARK_GREY, "newpara": True},
            {"text": "экономия $251,27/акр", "size": 14, "bold": True, "color": GOLD, "newpara": True},
        ], line_spacing=1.2)

    # Строка под ступенью 3 — отраслевой синтез
    s3n_y = s3_y + s3_h + 0.08
    text_box(s, step_x + 0.1, s3n_y, step_w - 0.2, 0.3,
             "По отрасли в целом (Western Growers) — снижение затрат на прополку ≈40% после первого года эксплуатации",
             size=10.5, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Ступень 4 — что переехало (вывод, во всю ширину)
    s4_y = s3n_y + 0.32
    s4_h = 0.75
    ocean_box(s, step_x, s4_y, step_w, s4_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    text_box(s, step_x + 0.25, s4_y + 0.1, step_w - 0.5, s4_h - 0.2,
             "Что переехало: экономика доказана убедительнее всего в органических листовых культурах "
             "(baby leaf, аругула) — не как общее заявление «для крупных овощных хозяйств». Для "
             "товарных пропашных культур (кукуруза, соя) и культур с густой посадкой тем же способом "
             "она не доказана.",
             size=12, bold=True, italic=True, color=DEEP, line_spacing=1.2, anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Источники: USDA NASS Vegetables Annual Summary 2025/2026 · Western Growers Case Study, март 2024 · Carbon Robotics businesswire 2025-02-10")
    add_speaker_notes(s, load_speaker_notes("s16a"))

    # ============ s17 Cognitive Pilot vs ИТЭЛМА — RU parallel ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Cognitive Pilot и ИТЭЛМА — это не ИИ против не-ИИ; это два разных класса ИИ",
        size=20)

    # Chart banner — own QuickChart comparison (c17-cogn-vs-itelma.png, Phase 3 K-4):
    # two equal-width bars (несравнимые по природе величины — установки vs точность,
    # поэтому длина бруса НЕ кодирует величину, это чисто категорийный разделитель) —
    # каждая строка несёт свой настоящий показатель текстом.
    cp = ASSETS / "charts" / "c17-cogn-vs-itelma.png"
    if cp.exists():
        add_image(s, cp, 0.6, 1.15, w=12.13, h=0.9)

    # 2-column architecture comparison
    col_w = 5.95; col_h = 4.3
    cy = 2.15

    # LEFT: Cognitive Pilot CV
    ocean_box(s, 0.6, cy, col_w, col_h, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.8, cy + 0.1, col_w - 0.4, 0.5, "Cognitive Pilot · компьютерное зрение",
             size=15, bold=True, color=DEEP)
    text_box(s, 0.8, cy + 0.55, col_w - 0.4, 0.4, "«Что я вижу»",
             size=11, italic=True, color=MID)
    hr_line(s, 0.8, cy + 1.05, col_w - 0.4, color=LIGHT, weight=1.0)
    text_box(s, 0.8, cy + 1.2, col_w - 0.4, 0.4,
             "1700+ установок (трактора, комбайны)",
             size=12, bold=True, color=DEEP)
    text_box(s, 0.8, cy + 1.6, col_w - 0.4, 0.4,
             "4 иска фермеров (~12,7 млн ₽)",
             size=12, bold=True, color=GOLD)
    text_box(s, 0.8, cy + 2.05, col_w - 0.4, 0.5,
             "Режим отказа:", size=11, italic=True, color=MID)
    text_box(s, 0.8, cy + 2.45, col_w - 0.4, 2.0,
             "• пыль закрывает камеры\n"
             "• сдвиг от теней меняет освещение\n"
             "• распознавание крайних рядов сбивается\n"
             "• эталонная разметка ≠ полевые условия\n"
             "• краевые случаи не в обучающем наборе",
             size=11, color=DARK_GREY, line_spacing=1.5)

    # RIGHT: ИТЭЛМА Квадро
    ocean_box(s, 6.85, cy, col_w, col_h, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, cy + 0.1, col_w - 0.4, 0.5, "ИТЭЛМА Квадро · слияние сенсоров",
             size=15, bold=True, color=DEEP)
    text_box(s, 7.05, cy + 0.55, col_w - 0.4, 0.4, "Навигация + инерциальные + поправки: «где я нахожусь»",
             size=11, italic=True, color=MID)
    hr_line(s, 7.05, cy + 1.05, col_w - 0.4, color=GOLD, weight=1.0)
    text_box(s, 7.05, cy + 1.2, col_w - 0.4, 0.4,
             "ГЛОНАСС + GPS + Galileo + BeiDou",
             size=12, bold=True, color=DEEP)
    text_box(s, 7.05, cy + 1.6, col_w - 0.4, 0.4,
             "RTK-коррекция: точность 2-5 см",
             size=12, bold=True, color=GOLD)
    text_box(s, 7.05, cy + 2.05, col_w - 0.4, 0.5,
             "Почему работает:", size=11, italic=True, color=MID)
    text_box(s, 7.05, cy + 2.45, col_w - 0.4, 2.0,
             "• сенсоры не зависят от освещения\n"
             "• несколько систем = резервирование\n"
             "• ГЛОНАСС работает в РФ независимо\n"
             "• стабильность в пыли / тумане / ночью\n"
             "• совместима с детерминистическим вождением",
             size=11, color=DARK_GREY, line_spacing=1.5)

    add_footer(s, "Источники: RTVI 2025 (иски Cognitive Pilot); Фонтанка 2026-01-26 (ИТЭЛМА)")
    add_speaker_notes(s, load_speaker_notes("s17"))

    # ============ s18 4 узких победы L2 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Узкие победы L2 — Solinftec, Saga UV-C, Tevel, AGCO Outrun",
        size=22)

    cases = [
        ("Solinftec Solix", "+243% год к году в 2025",
         "Самоотчёт вендора: ≤98%\nсокращения контактных гербицидов",
         "tractor"),
        ("Saga UV-C", "20% клубники в Великобритании",
         "Ультрафиолетовая ночная обработка.\nНе сбор — контроль болезней",
         "leaf"),
        ("Tevel", "Дроны-сборщики яблок",
         "Узкая ниша — летающие\nдроны для сбора яблок",
         "package"),
        ("AGCO PTx Outrun", "Дооснащение смешанного парка",
         "AGCO-модуль для смешанного\nпарка тракторов (не только AGCO)",
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
             "Паттерн специализации: каждое решение — узкое и измеримое",
             size=13, bold=True, color=DEEP)
    text_box(s, 0.85, 6.45, 11.6, 0.35,
             "⚠ Не путать: Saga UV-C ≠ Saga для сбора. Эти 20% клубники в Великобритании — контроль болезней, не сбор.",
             size=11, italic=True, color=GOLD, line_spacing=1.3)

    add_footer(s, "Источники: Solinftec.com · sagarobotics.com · tevel-tech.com · agcocorp.com 2025")
    add_speaker_notes(s, load_speaker_notes("s18"))

    # ============ s19 Monarch failure timeline ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Monarch Tractor — «автономный» при сломанной автономии",
        size=24)

    # Timeline 2018-2026 — compact, fits within 0.6-12.73 inches
    events = [
        ("2018", "Основание", "Livermore, CA", LIGHT),
        ("2022", "Демо MK-V", "Большая PR-волна", MID),
        ("сент. 2025", "Иск Burks Tractor", "10 тракторов · $773 088\n«не может работать\nавтономно»", GOLD),
        ("нояб. 2025", "102 сокращения", "~38% (102 / ~270\nпосле 10% cut нояб. 2024)", GOLD),
        ("апр. 2026", "Поглощение\nCaterpillar", "Конец независимости", DEEP),
    ]

    tline_y = 2.0
    n = len(events)
    # Tighter range — pull endpoints inward
    line_x_start = 1.4
    line_x_end = 11.9
    line_w = line_x_end - line_x_start
    # Draw horizontal line
    hr_line(s, line_x_start, tline_y, line_w, color=LIGHT, weight=2.5)
    # Card dimensions — compact (1.3" tall, was 1.8") to free room for the
    # photo + headline row below (K-3/K-4: s19 was promised Monarch MK-V photo
    # + TechCrunch иск headline, built with neither — Phase 3 fix).
    card_w = 2.05
    card_h = 1.3
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
        ocean_box(s, x - card_w/2, tline_y + 0.3, card_w, card_h,
                  fill=GOLD_TINT if color == GOLD else LIGHT_TINT, stroke=color)
        text_box(s, x - card_w/2 + 0.05, tline_y + 0.4, card_w - 0.1, 0.45, hdr,
                 size=11, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.15)
        text_box(s, x - card_w/2 + 0.05, tline_y + 0.88, card_w - 0.1, 0.65, desc,
                 size=9, color=DARK_GREY, italic=True, align=PP_ALIGN.CENTER, line_spacing=1.2)

    # Photo + headline row (K-4: оба файла — реальный Monarch MK-V и настоящий
    # заголовок TechCrunch — ранее не подключались, кадр собирался без изображений).
    photo_row_y = tline_y + 0.3 + card_h + 0.25  # = 3.85
    pcol_w = 5.95
    mp = ASSETS / "photos" / "p19-monarch-mkv-real.jpg"
    photo_h = 1.45
    if mp.exists():
        add_image(s, mp, 0.6, photo_row_y, w=pcol_w, h=photo_h)
    text_box(s, 0.6, photo_row_y + photo_h + 0.04, pcol_w, 0.2,
             "Monarch MK-V. Источник: Monarch press, публикация TechCrunch, 2025-11-18",
             size=9.5, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Right: real TechCrunch headline, quoted verbatim (not a screenshot —
    # no headless-browser capture available; honestly presented as a text quote).
    hx = 6.85
    ocean_box(s, hx, photo_row_y, pcol_w, photo_h, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, hx + 0.2, photo_row_y + 0.12, pcol_w - 0.4, 0.3,
             "TechCrunch · 18 ноября 2025", size=11, bold=True, color=MID)
    text_box(s, hx + 0.2, photo_row_y + 0.45, pcol_w - 0.4, photo_h - 0.6,
             "«Monarch Tractor sued over tractors that were "
             "‘unable to operate autonomously’»",
             size=14, bold=True, italic=True, color=DEEP, line_spacing=1.2)
    text_box(s, hx + 0.2, photo_row_y + photo_h - 0.28, pcol_w - 0.4, 0.22,
             "Дословный заголовок статьи об иске Burks Tractor",
             size=9.5, italic=True, color=LIGHT)

    # Bottom takeaway
    takeaway_y = photo_row_y + photo_h + 0.35  # ≈ 5.70
    ocean_box(s, 0.6, takeaway_y, 12.13, 1.05, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, takeaway_y + 0.1, 11.6, 0.35,
             "Анти-паттерн: демо ≠ промышленное внедрение",
             size=15, bold=True, color=DEEP)
    text_box(s, 0.85, takeaway_y + 0.46, 11.6, 0.55,
             "«Автономный» в маркетинге = юридическая ловушка, если фактическое поведение зависит от оператора.\n"
             "Каждое обещание автономии проверяется независимым тестом оператора → если нужен оператор, автономия частичная.",
             size=10.5, color=DARK_GREY, italic=True, line_spacing=1.25)

    add_footer(s, "Источники: TechCrunch 2025-11-18, 2025-11-19, 2026-04-15")
    add_speaker_notes(s, load_speaker_notes("s19"))

    # ============ s20 FarmWise + Naïo ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "FarmWise свернул работу + Naïo –40% — открытая среда ломает компьютерное зрение",
        size=20)

    # Left: cause
    ocean_box(s, 0.6, 1.5, 6.0, 4.6, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.85, 1.65, 5.5, 0.5, "Причина провалов CV-стека (компьютерное зрение)",
             size=14, bold=True, color=DEEP)
    p = ASSETS / "photos" / "p20-farmwise-titan.jpg"
    if p.exists():
        add_image(s, p, 0.85, 2.2, w=5.5, h=2.0)
    text_box(s, 0.85, 4.25, 5.5, 0.3,
             "FarmWise Titan FT35 · свернул работу в 2025",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 4.6, 5.5, 1.4,
             "FarmWise свернул работу 2025\nNaïo €4 млн → €2,4 млн (–40%)\n"
             "Компьютерное зрение, обученное в тепличных условиях:\n"
             "• сдвиг от теней (arXiv 2508.19511)\n"
             "• переменное освещение\n"
             "• пыль / туман",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.4)

    # Right: alternative
    ocean_box(s, 6.8, 1.5, 6.0, 4.6, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, 1.65, 5.5, 0.5, "AP2b — детерминированная альтернатива",
             size=15, bold=True, color=DEEP)
    p = ASSETS / "photos" / "p20-tractor-mower.jpg"
    if p.exists():
        add_image(s, p, 7.05, 2.2, w=5.5, h=2.0)
    text_box(s, 7.05, 4.25, 5.5, 0.3,
             "Lemken / Kverneland — механический культиватор",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, 7.05, 4.6, 5.5, 1.4,
             "Механические культиваторы как детерминированный\n"
             "вариант:\n"
             "• стебле-определение механикой\n"
             "• междурядная обработка\n"
             "• работает в любую погоду\n"
             "• стоимость в 3-5× меньше CV-робота",
             size=11, color=DEEP, italic=True, line_spacing=1.4)

    add_footer(s, "Источники: Farm Progress 2025; arXiv 2508.19511 (shadow bias); Lemken / Kverneland press")
    add_speaker_notes(s, load_speaker_notes("s20"))

    # ============ s21 Strawberry economics ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Робот-сборщик клубники — 10 лет пилотов, не промышленного внедрения",
        size=22)

    # Left photo + chart
    ocean_box(s, 0.6, 1.5, 6.0, 5.1)
    p = ASSETS / "photos" / "p21-strawberry-picker.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.75, w=5.5, h=4.0)
    text_box(s, 0.85, 5.8, 5.5, 0.3,
             "Ручной сбор клубники (Wikimedia Commons, CC-BY-SA)",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 6.15, 5.5, 0.3,
             "«Сбор урожая — последняя великая нерешённая задача»",
             size=11, italic=True, bold=True, color=GOLD, align=PP_ALIGN.CENTER)

    # Right: 4 number-cards
    nums = [
        ("$200-350 тыс.", "капитальные затраты\nна одного робота", GOLD),
        ("$68-130 тыс.", "годовая амортизация\nодного робота", DEEP),
        ("$43 тыс. / акр", "стоимость ручного\nсбора в Калифорнии", LIGHT),
        ("<5% рынка", "роботы × $50 млрд\nадресуемого рынка труда", MID),
    ]
    cy = 1.5
    for big, lbl, color in nums:
        ocean_box(s, 6.8, cy, 6.0, 1.2, fill=LIGHT_TINT if color != GOLD else GOLD_TINT)
        text_box(s, 7.0, cy + 0.1, 2.8, 0.6, big,
                 size=22, bold=True, color=color)
        text_box(s, 9.85, cy + 0.2, 2.85, 0.85, lbl,
                 size=11, color=DEEP, italic=True, line_spacing=1.3)
        cy += 1.3

    add_footer(s, "Источники: Wikimedia Commons; RobotToday market analysis 2024")
    add_speaker_notes(s, load_speaker_notes("s21"))
