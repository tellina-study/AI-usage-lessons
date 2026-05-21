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
    section_divider(prs, 3, "Раздел 3 — L3 «Животное»",
        "Полузакрытая среда + измерения на уровне особи. ИИ работает стабильнее, чем на L1-L2.",
        current_section=3,
        caption="12 минут · 4 рабочих кейса + 3 анти-хайп урока · РФ-параллель")
    add_speaker_notes(prs.slides[-1], load_speaker_notes("s22"))

    # ============ s23 SenseHub 2M cows ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Allflex SenseHub — 2 миллиона коров с сенсорами", size=26)

    # Left: photo
    ocean_box(s, 0.6, 1.5, 6.5, 5.1)
    p = ASSETS / "photos" / "p23-cow-ear-tag.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.75, w=6.0, h=4.0)
    text_box(s, 0.85, 5.85, 6.0, 0.3,
             "Сенсор-бирка · Wikimedia (Cow with ear tag, CC-BY-SA)",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 6.2, 6.0, 0.3,
             "+ ошейник-акселерометр + облачная аналитика",
             size=10, italic=True, color=MID, align=PP_ALIGN.CENTER)

    # Right: 3-step flow + 5 alerts
    text_box(s, 7.3, 1.6, 5.4, 0.4, "ИИ-конвейер (раннее предупреждение)",
             size=14, bold=True, color=MID)

    flow_steps = [
        ("1. Сенсор", "Акселерометр · 5-7 лет батарея", LIGHT),
        ("2. Облако", "ML-классификация поведения", MID),
        ("3. Сигнал фермеру", "Раннее предупреждение, не назначение", GOLD),
    ]
    fy = 2.15
    for hdr, sub, color in flow_steps:
        ocean_box(s, 7.3, fy, 5.4, 0.75, fill=LIGHT_TINT if color != GOLD else GOLD_TINT, stroke=color)
        text_box(s, 7.5, fy + 0.1, 5.0, 0.3, hdr,
                 size=13, bold=True, color=DEEP)
        text_box(s, 7.5, fy + 0.4, 5.0, 0.3, sub,
                 size=10, color=MID, italic=True)
        fy += 0.85

    # Alerts row
    text_box(s, 7.3, 4.85, 5.4, 0.4, "5 классов сигналов",
             size=13, bold=True, color=DEEP)
    alerts = ["эструс", "отёл", "хромота", "мастит", "пневмония"]
    ax = 7.3
    aw = 1.0
    for al in alerts:
        ocean_box(s, ax, 5.3, aw, 0.5, fill=GOLD_TINT, stroke=GOLD)
        text_box(s, ax, 5.3, aw, 0.5, al, size=10, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        ax += aw + 0.08

    # Bottom: augmentation principle
    ocean_box(s, 7.3, 6.0, 5.4, 0.65, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.5, 6.1, 5.0, 0.45,
             "ИИ = усиление человека, не замена",
             size=12, bold=True, color=GOLD,
             anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Источник: Merck Animal Health, 2025 — рубеж 2 млн молочных коров")
    add_speaker_notes(s, load_speaker_notes("s23"))

    # ============ s24 CattleEye + DeLaval + Birdoo ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "CattleEye + DeLaval VMS V310 + Cargill Birdoo — 3 рабочих кейса", size=22)

    cards = [
        ("CattleEye", "60 ферм · 11 000 коров", "Видеонаблюдение + ИИ в облаке:\nоценка хромоты · сеть GEA >250 000", LIGHT),
        ("DeLaval VMS V310", "99,8% успешного подключения", "998/1000 успешных подключений\nруки доильного аппарата", GOLD),
        ("Cargill Birdoo", ">95% точность", "Компьютерное зрение для оценки\nвеса · экономия 10-30 г корма / бройлера", MID),
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

    add_footer(s, "Источники: Fortune 2025-06 (CattleEye GEA); DeLaval press 2025-04; Cargill.com 2025")
    add_speaker_notes(s, load_speaker_notes("s24"))

    # ============ s25 Cainthus + tie-stall + Holstein-bias ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Cainthus, привязное содержание, голштинский уклон — 3 анти-хайп урока L3",
        size=20)

    lessons = [
        ("Cainthus (Cargill 2018)", "Анонс ≠ внедрение",
         "Публичных производственных метрик нет. Брендированный пресс-релиз, но 0 измеримых данных по развёртыванию к 2026 году.",
         "alert-circle"),
        ("Привязное содержание", "Архитектура ломает компьютерное зрение",
         "Алгоритм работает на беспривязном (свободном) содержании, не на привязном.\n"
         "Большая часть РФ-коров содержится привязно.",
         "lock"),
        ("Голштинский уклон", "Обучающие данные ≠ местные породы",
         "ИИ обучен на голштинской / фризской породе. Ярославская, Якутская, Холмогорская — другая морфология.\n"
         "Способности ИИ ≠ применимость ИИ.",
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
             "Главный урок: способности ИИ ≠ применимость ИИ. Архитектура хозяйства + порода — переменные применимости.",
             size=11, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Источники: Wikimedia Commons (Holstein); пресс-релиз Cargill 2018")
    add_speaker_notes(s, load_speaker_notes("s25"))

    # ============ s26 РФ L3 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L3 в РФ — Connectome.ai + санкционная неопределённость молочного ИИ-стека",
        size=20)

    # Left: working case
    ocean_box(s, 0.6, 1.5, 6.0, 5.0, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.85, 1.65, 5.5, 0.5, "Работает — Connectome.ai",
             size=15, bold=True, color=DEEP)
    icon_p = ASSETS / "icons" / "scan-96.png"
    if icon_p.exists():
        add_image(s, icon_p, 0.85 + (5.5 - 0.9) / 2, 2.2, w=0.9, h=0.9)
    text_box(s, 0.85, 3.3, 5.5, 0.4, "Резидент Сколково",
             size=12, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 3.8, 5.5, 1.6,
             "Узкая задача компьютерного зрения:\nконтроль отёлов телят\n+ ранний сигнал на помощь",
             size=12, color=DEEP, italic=True, line_spacing=1.4,
             align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 5.5, 5.5, 0.9,
             "Паттерн: узкая ниша + CV +\nизмеримая безопасность животного",
             size=10, color=DARK_GREY, italic=True, line_spacing=1.4,
             align=PP_ALIGN.CENTER)

    # Right: vapor risk
    ocean_box(s, 6.8, 1.5, 6.0, 5.0, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, 1.65, 5.5, 0.5, "Под вопросом — DeLaval / GEA / Lely",
             size=15, bold=True, color=DEEP)
    text_box(s, 7.05, 2.15, 5.5, 0.4, "Серый статус облачной аналитики",
             size=11, italic=True, color=MID)
    text_box(s, 7.05, 2.65, 5.5, 2.4,
             "• Оборудование физически у фермеров\n"
             "• Облачная аналитика зависит от Европы\n"
             "• Прецедент: Climate FieldView 2022 →\n"
             "  Microsoft Azure 2024 (для оборонки)\n"
             "• Лобня 2026 — замещение оборудования\n"
             "  начато (4 млрд ₽), ИИ-стек — отд. трек",
             size=11, color=DEEP, line_spacing=1.5)
    text_box(s, 7.05, 5.15, 5.5, 1.3,
             "F9 — риск «пара»: вендор может отключить ИИ-функционал по решению санкций или лицензий, "
             "не уведомив пользователей заранее.",
             size=11, bold=True, italic=True, color=GOLD, line_spacing=1.4)

    add_footer(s, "Источники: Connectome.ai (Сколково); BUSINESS-stat 2026 Лобня · TAdviser FieldView")
    add_speaker_notes(s, load_speaker_notes("s26"))

    # ============ s27 section4 divider ============
    section_divider(prs, 4, "Раздел 4 — L4 «Цепочка поставок»",
        "Агентный ИИ лидирует. Результат измеряется в долях процента за минуты, не в сезонах.",
        current_section=4,
        caption="10 минут · Cargill CMAX + Tract + провал USDA + РФ-параллель")
    add_speaker_notes(prs.slides[-1], load_speaker_notes("s27"))

    # ============ s28 Cargill CMAX ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Cargill CMAX — премия BIG AI Excellence Award 2026", size=24)

    # Photo left
    ocean_box(s, 0.6, 1.5, 7.0, 5.1)
    p = ASSETS / "photos" / "p28-grain-port.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.75, w=6.5, h=4.0)
    text_box(s, 0.85, 5.85, 6.5, 0.3,
             "Зерновой порт и силосы · Tilbury (Wikimedia, CC-BY-SA)",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 6.2, 6.5, 0.3,
             "ИИ оптимизирует прогноз для порта и судоходную логистику",
             size=10, italic=True, color=MID, align=PP_ALIGN.CENTER)

    # Right: KPIs
    kpis = [
        ("70+ стран", "география операций", LIGHT),
        ("1000+ объектов", "складов / портов / силосов", MID),
        ("BIG AI 2026", "Excellence Award на уровне L4", GOLD),
    ]
    cy = 1.5
    for big, lbl, color in kpis:
        ocean_box(s, 7.8, cy, 4.95, 1.2, fill=LIGHT_TINT if color != GOLD else GOLD_TINT)
        text_box(s, 8.0, cy + 0.15, 4.6, 0.5, big,
                 size=22, bold=True, color=color)
        text_box(s, 8.0, cy + 0.65, 4.6, 0.4, lbl,
                 size=12, color=DEEP, italic=True)
        cy += 1.3

    ocean_box(s, 7.8, 5.4, 4.95, 1.25, fill=SURFACE)
    text_box(s, 8.0, 5.55, 4.55, 0.4, "Принцип успеха: узкость агентного ИИ",
             size=12, bold=True, color=DEEP)
    text_box(s, 8.0, 5.95, 4.55, 0.65,
             "Одно действие на агента (хеджирование / маршрут) + человек в петле для сделок >$10 млн номинала",
             size=10, color=DARK_GREY, italic=True, line_spacing=1.4)

    add_footer(s, "Источник: пресс-релиз Cargill 2026 BIG AI Excellence Award")
    add_speaker_notes(s, load_speaker_notes("s28"))

    # ============ s29 hedge pseudo-flow ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Как агент хеджирует — упрощённая схема в 4 шага",
        size=24)

    steps = [
        ("1. Сенсор", "Вектор состояния:\nцена + погода + валюта",
         "входные данные", "database"),
        ("2. Расчёт", "Распределение цен\n5/30/90 дней + неопределённость",
         "ML-модель", "brain"),
        ("3. Решение", "4 действия:\nкупить / продать /\nдержать / хеджировать\n+ человек при >$10 млн",
         "Слой действий", "settings"),
        ("4. Обратная связь", "bp за минуты,\nонлайн-обучение",
         "Цикл замыкается", "trending-up"),
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
             "Пример: проскальзывание сократилось с 45 bp до 8 bp",
             size=15, bold=True, color=DEEP)
    text_box(s, 0.85, 6.0, 11.6, 0.8,
             "На сделке $5 млн номинала: (45–8) × 0,01% × $5 млн = $1850 за сделку. "
             "При 20 сделках в месяц = ~$37 тыс. экономии. ROI узкого агентного ИИ — 1-2 месяца.\n"
             "Это работает, потому что задача узкая (тайминг хеджирования), обратная связь быстрая, человек — только для крупных сделок.",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.4)

    add_footer(s, "Пример: McKinsey 2025 hedging report — типичное ручное проскальзывание")
    add_speaker_notes(s, load_speaker_notes("s29"))

    # ============ s30 Tract + Olam + Walmart + Tesco ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Tract + Olam Mindsprint + Walmart × Cropin + Tesco",
        size=24)

    cards = [
        ("Tract", "€18,6 млн раунд A",
         "Icos Capital · 4 якорных инвестора:\nCargill + ADM + Olam + LDC.\nХранилище данных, НЕ агент.",
         "database"),
        ("Olam Procuresprint", "Агентная закупка",
         "Узкая закупочная задача:\nцена + поставщики + контракты\nкак агент.",
         "package"),
        ("Walmart × Cropin", "США + ЮАР",
         "(не Индия) — аналитика\nцепочки поставок и ESG-отчёт.",
         "globe"),
        ("Tesco AI", "−30% пищевых отходов",
         "С 2017 — Tesco AI для\nпрогноза скоропортящихся.",
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
             "⚠ Не путать: Tract = хранилище данных (инфраструктура соответствия), не агентный ИИ.",
             size=12, bold=True, color=GOLD)
    text_box(s, 0.85, 6.5, 11.6, 0.3,
             "Конкуренты совместно строят инфраструктуру соответствия — редкий прецедент коллаборации Cargill+ADM+Olam+LDC.",
             size=10, italic=True, color=DARK_GREY)

    add_footer(s, "Источники: пресс-релиз Tract 2024-08; FreshPlaza; пресс-релиз Wipro 2026 (Mindsprint)")
    add_speaker_notes(s, load_speaker_notes("s30"))

    # ============ s31 USDA + Verra ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "USDA Climate-Smart отменён + 94% призрачных кредитов Verra",
        size=22)

    # Left: USDA cancellation
    ocean_box(s, 0.6, 1.5, 6.0, 5.0, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 1.65, 5.5, 0.5, "Апрель 2025 — USDA отменил",
             size=14, bold=True, color=GOLD)
    text_box(s, 0.85, 2.15, 5.5, 0.4, "программу Climate-Smart Commodities",
             size=11, italic=True, color=MID)
    nums = [
        ("$3,1 млрд", "финансирование"),
        ("135 проектов", "отменены"),
        ("14 000 ферм", "потеряли поддержку"),
        ("3,2 млн акров", "вышли из программы"),
    ]
    ny = 2.65
    for big, lbl in nums:
        text_box(s, 1.05, ny, 1.8, 0.4, big, size=16, bold=True, color=DEEP)
        text_box(s, 2.95, ny, 3.3, 0.4, lbl, size=12, italic=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
        ny += 0.55
    text_box(s, 0.85, 5.45, 5.5, 1.0,
             "Федеральная политика = хвостовой риск\nдля бизнес-моделей, зависящих от субсидий",
             size=11, bold=True, italic=True, color=DEEP, line_spacing=1.4, align=PP_ALIGN.CENTER)

    # Right: Verra
    ocean_box(s, 6.8, 1.5, 6.0, 5.0)
    text_box(s, 7.05, 1.65, 5.5, 0.5, "Январь 2023 — 94% призрачных у Verra",
             size=14, bold=True, color=DEEP)
    text_box(s, 7.05, 2.15, 5.5, 0.4, "The Guardian + Die Zeit + SourceMaterial",
             size=11, italic=True, color=MID)
    c = ASSETS / "charts" / "c31-verra-phantom.png"
    if c.exists():
        add_image(s, c, 7.0, 2.6, w=5.7, h=3.0)
    text_box(s, 7.05, 5.8, 5.7, 0.7,
             "94% лесных кредитов Verra → нет реального снижения CO₂.\n"
             "AP7: AI-MRV без прямых измерений = масштабное «зелёное мошенничество».",
             size=11, bold=True, italic=True, color=GOLD, line_spacing=1.4)

    add_footer(s, "Источники: USDA press 2025-04-14; The Guardian 2023-01; SourceMaterial 2023")
    add_speaker_notes(s, load_speaker_notes("s31"))

    # ============ s32 РФ L4 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L4 в РФ — X5 паритет, Магнит гибрид, РСХБ — «пар»",
        size=22)

    c = ASSETS / "charts" / "c32-rus-retail.png"
    if c.exists():
        add_image(s, c, 0.6, 1.5, w=6.4, h=4.5)

    # Right cards
    cards = [
        ("X5 «Перекрёсток»", "ML с 2020 · 200+ факторов", "Мировой уровень. Работает.", LIGHT),
        ("Магнит F&R", "Гибрид: прогноз ✓, пополнение — пилот",
         "Прогнозирование на 46 РЦ янв 2026 — в эксплуатации.\nПополнение на 3 РЦ — пилот.", MID),
        ("РСХБ ИИ-сервисы", "Заявлены, метрик нет",
         "Риск «пара»: декларации без производственных метрик.", GOLD),
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
             "Паттерн: паритет L4-L5 при отставании L1-L2. GigaChat — демо-эпизод, не внедрение.",
             size=12, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Источники: Habr Магнит 2026-01; TAdviser X5 Tech 2024")
    add_speaker_notes(s, load_speaker_notes("s32"))

    # ============ s33 section4bis divider — Среда ============
    # Use just "4" — title клейс different by «Раздел 4-bis»
    section_divider(prs, 4, "Раздел 4-bis — Среда",
        "Сквозные темы: связь · привязка к вендору · регуляторика. Без них ни одна ступень не работает.",
        current_section=5,
        caption="8 минут · связь + двойная оптика привязки + ЕС/USDA/РФ")
    add_speaker_notes(prs.slides[-1], load_speaker_notes("s33"))

    # ============ s34 Connectivity + GNSS ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Связь — 18% ферм без интернета + помехи навигации в I кв. 2025",
        size=22)

    # Top: 3 mega-numbers
    nums = [
        ("18%", "американских ферм\nбез интернета", GOLD),
        ("123 000", "авиа-рейсов с помехами\nнавигации, I кв. 2025", DEEP),
        ("апр. 2026", "запрет Starlink в РФ", LIGHT),
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
    text_box(s, 7.05, 3.5, 5.5, 0.5, "AP5 + альтернатива",
             size=15, bold=True, color=GOLD)
    text_box(s, 7.05, 4.0, 5.5, 0.8,
             "AP5: облако-первый подход для отсутствия сети =\n"
             "архитектурная ошибка.",
             size=12, color=DEEP, italic=True, line_spacing=1.4)
    hr_line(s, 7.05, 4.85, 5.5, color=GOLD, weight=1.0)
    text_box(s, 7.05, 5.0, 5.5, 0.4, "Альтернатива: ML на устройстве (edge / TinyML)",
             size=12, bold=True, color=DEEP)
    text_box(s, 7.05, 5.45, 5.5, 0.8,
             "• вывод модели прямо на устройстве\n"
             "• минимальная связь с облаком\n"
             "• работает в условиях помех навигации",
             size=10, color=DARK_GREY, italic=True, line_spacing=1.5)

    add_footer(s, "Источники: Stanford GPS Lab ITM 2025; ICAO 2025 (Швейцария / Финляндия / Эстония)")
    add_speaker_notes(s, load_speaker_notes("s34"))

    # ============ s30b vendor lock-in double optic ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Привязка к вендору — двойная оптика John Deere",
        size=24)

    # Left: anti-theft success
    ocean_box(s, 0.6, 1.5, 6.0, 5.0, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.85, 1.65, 5.5, 0.5, "Май 2022 — успех против кражи",
             size=15, bold=True, color=LIGHT)
    text_box(s, 0.85, 2.15, 5.5, 0.4, "Мелитополь, оккупированная территория",
             size=11, italic=True, color=MID)
    text_box(s, 0.85, 2.65, 5.5, 1.5,
             "Удалённая блокировка John Deere:\n"
             "27 единиц техники\n"
             "на $5 млн стали\n"
             "кирпичом по решению производителя.",
             size=12, color=DEEP, italic=True, line_spacing=1.4)
    p = ASSETS / "photos" / "p30b-fpv-drone.jpg"
    if p.exists():
        add_image(s, p, 0.85, 4.5, w=5.5, h=1.7)
    text_box(s, 0.85, 6.25, 5.5, 0.3,
             "ИИ-функция безопасности — успех в этой петле",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Right: control surface optic
    ocean_box(s, 6.8, 1.5, 6.0, 5.0, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, 1.65, 5.5, 0.5, "Янв. 2025 — FTC против Deere",
             size=15, bold=True, color=GOLD)
    text_box(s, 7.05, 2.15, 5.5, 0.4, "Десятилетние ограничения ремонта",
             size=11, italic=True, color=MID)
    text_box(s, 7.05, 2.65, 5.5, 1.8,
             "Один и тот же механизм:\n"
             "удалённая блокировка = безопасность сегодня =\n"
             "поверхность контроля завтра. Фермер\n"
             "не может ремонтировать без\n"
             "разрешения вендора.",
             size=12, color=DEEP, italic=True, line_spacing=1.4)
    hr_line(s, 7.05, 4.5, 5.5, color=GOLD, weight=1.2)
    text_box(s, 7.05, 4.65, 5.5, 0.4, "Декабрь 2025 — FCC запретил DJI",
             size=13, bold=True, color=DEEP)
    text_box(s, 7.05, 5.05, 5.5, 1.4,
             "80% сельхоз-дронов в США потеряли\n"
             "легальный статус. Одно решение FCC —\n"
             "привязка к вендору стала геополитическим риском.",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.5)

    add_footer(s, "Источники: The Register 2022-05-02; CSO Online 572811; пресс-релиз FTC 2025-01-15")
    add_speaker_notes(s, load_speaker_notes("s30b"))

    # ============ s35 regulatory 3-col ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Регуляторика — EU AI Act vs USDA vs «АПК будущего»",
        size=22)

    cols = [
        ("EU AI Act", "Регламент 2024/1689",
         "• Сельхозтехника — высокий риск\n"
         "• Февр. 2025 — оператор обязан\n"
         "• ИИ-грамотность обязательна\n"
         "• Цепь ответственности: вендор → оператор",
         "Строгий, исполнимый", GOLD),
        ("USDA AI Strategy", "FY2025-26",
         "• Формальная декларация\n"
         "• Climate-Smart отменена\n"
         "• Нет обязательной ИИ-грамотности\n"
         "• Нет классификации высокого риска",
         "Формальная, слабое принуждение", DEEP),
        ("РФ «АПК будущего»", "Распоряж. 31.12.2025",
         "• Декларативная программа\n"
         "• Предыдущая (АПК 2024) –3,2%\n"
         "• Нет измеримых показателей\n"
         "• Нет ответственности вендора",
         "Декларативная, непроверенная", LIGHT),
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

    add_footer(s, "Источники: Cambridge EJRR 2024; USDA AI Strategy FY2025-26; Распоряжение Правительства РФ 31.12.2025")
    add_speaker_notes(s, load_speaker_notes("s35"))

    # ============ s36 section5 divider — Полка ============
    section_divider(prs, 5, "Раздел 5 — L5 «Полка» + 5 критериев",
        "Розничный ИИ зрел + пять анти-ИИ критериев + чек-лист + карьерный ландшафт + замыкание к Plenty.",
        current_section=6,
        caption="6 минут · L5 + 5 критериев + чек-лист + возврат к Plenty Compton")
    add_speaker_notes(prs.slides[-1], load_speaker_notes("s36"))

    # ============ s37s L5 retail ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L5 — Walmart Eden + Tesco AI + X5 «Перекрёсток»",
        size=24)

    cards = [
        ("Walmart Eden", "ML с 2017",
         "Прогноз скоропортящихся +\nмаршруты свежести на 11 000+ магазинов",
         GOLD),
        ("Tesco AI", "−30% пищевых отходов с 2017",
         "Ежедневный прогноз на ~3500\nсупермаркетов Великобритании",
         MID),
        ("X5 «Перекрёсток»", "ML с 2020 · 200+ факторов",
         "Российский флагман L5.\nМировой уровень.",
         LIGHT),
    ]
    card_w = 3.95; card_h = 3.5; gap = 0.18
    sx = 0.6; sy = 1.6
    for i, (name, kpi, desc, color) in enumerate(cards):
        x = sx + i * (card_w + gap)
        ocean_box(s, x, sy, card_w, card_h,
                  fill=GOLD_TINT if color == GOLD else LIGHT_TINT, stroke=color)
        icon_p = ASSETS / "icons" / "shopping-cart-96.png"
        if icon_p.exists():
            add_image(s, icon_p, x + (card_w - 0.9) / 2, sy + 0.25, w=0.9, h=0.9)
        text_box(s, x + 0.15, sy + 1.3, card_w - 0.3, 0.4, name,
                 size=15, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x + 0.15, sy + 1.75, card_w - 0.3, 0.5, kpi,
                 size=13, bold=True, color=color, align=PP_ALIGN.CENTER, line_spacing=1.2)
        text_box(s, x + 0.2, sy + 2.4, card_w - 0.4, 1.0, desc,
                 size=10, color=DARK_GREY, italic=True, align=PP_ALIGN.CENTER, line_spacing=1.4)

    # Bottom — supermarket aisle photo + caveat
    ocean_box(s, 0.6, 5.4, 6.0, 1.5)
    p = ASSETS / "photos" / "p37s-supermarket-aisle.jpg"
    if p.exists():
        add_image(s, p, 0.85, 5.55, w=5.5, h=1.2)

    ocean_box(s, 6.8, 5.4, 6.0, 1.5, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, 5.55, 5.5, 0.4,
             "⚠ Оговорка: L5 ≠ агро-готовность",
             size=13, bold=True, color=GOLD)
    text_box(s, 7.05, 5.95, 5.5, 0.9,
             "Успех на L5 — это розничный ИИ, не сельскохозяйственный.\n"
             "Большая часть L5 — не агро-специфика. Опыт ≠ агро-инструмент.",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.4)

    add_footer(s, "Источники: Walmart corporate 2025; Tesco AI annual report; X5 Tech 2024")
    add_speaker_notes(s, load_speaker_notes("s37s"))

    # ============ s38s 5 criteria matrix ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Пять анти-ИИ критериев — главный вывод лекции",
        size=24)

    # 5 row matrix: criterion / example / alternative
    rows_data = [
        ("AP1", "Термодинамика > ИИ", "Plenty Compton: $940 млн потерь",
         "Не ИИ · открытое поле или\nдругая юнит-экономика"),
        ("AP3", "Точность ≠ внедрение", "Plantix 85% × 10 млн = ~100 тыс. ошибок",
         "Откалиброванная уверенность +\nотказ от ответа"),
        ("AP4", "Универсальный LLM как советник", "Tzachor: 56-71% неверны",
         "ИИ с проверкой источников +\nчеловек в петле"),
        ("AP6", "ИИ-техника = привязка к вендору", "Deere $5 млн + FTC + запрет DJI",
         "Открытые стандарты / мульти-вендор"),
        ("AP7", "AI-MRV без прямых измерений", "Verra: 94% призрачных кредитов",
         "Отбор почвы + спутниковая физика"),
    ]

    # Header row
    matrix_x = 0.6
    matrix_y = 1.5
    headers = ["№", "Критерий «когда не ИИ»", "Пример провала", "Альтернатива"]
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
             "Также: AP2a (выбор архитектуры внутри ИИ) · AP2b (детерминистическая альтернатива) · AP5 (облако-первый вне сети)",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    add_speaker_notes(s, load_speaker_notes("s38s"))

    # ============ s35c checklist 5 blocks ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Чек-лист проверки перед покупкой ИИ-решения",
        size=24)

    blocks = [
        ("Классификация задачи", "1. Узкая или универсальная?",
         "2. Закрытый контур или открытая среда?"),
        ("Промышленное состояние", "3. Производственные метрики vs анонсы?",
         "4. Независимая проверка есть?"),
        ("Ответственность", "5. Цепь ответственности вендора?",
         "6. SLA на отказы ИИ-функционала?"),
        ("Привязка к вендору", "7. Открытые стандарты данных?",
         "8. Совместимость с другими вендорами?"),
        ("Связь", "9. Резерв на устройстве при\n   отсутствии интернета?",
         "10. Альтернатива GNSS-навигации?"),
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
                 f"Блок {i+1}", size=12, bold=True, color=DEEP,
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
             "Оценка: 8-10 «да» = покупать/пилотировать · 5-7 = с условиями · ≤4 = отказать",
             size=14, bold=True, color=DEEP)
    text_box(s, 0.85, 6.55, 11.6, 0.3,
             "Ответ — не словами вендора, а внешними источниками: независимые аудиты, пресс-релизы FTC, отраслевые отчёты.",
             size=10, italic=True, color=DARK_GREY)

    add_speaker_notes(s, load_speaker_notes("s35c"))

    # ============ s36c career landscape ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Карьерный ландшафт — L1-L5 сегменты + российский рынок",
        size=24)

    segments = [
        ("L1 Поле", "John Deere · Bayer · BASF\nClimate · Taranis · Granular",
         "Cognitive Pilot · ИТЭЛМА\nЭФКО · Геоскан · ExactFarming", LIGHT),
        ("L2 Робот", "Carbon Robotics · Saga · Tevel\nAGCO · Aigen", "(точечные RU стартапы)", MID),
        ("L3 Животное", "DeLaval · GEA · Lely\nCargill Birdoo · Allflex", "Connectome.ai · Сколково pipeline", LIGHT),
        ("L4 Цепочка", "Cargill CMAX · Tract · Olam\nADM · Walmart×Cropin", "X5 Tech · Магнит digital\nРусагро Тех · РСХБ.цифра", GOLD),
        ("L5 Полка", "Walmart Eden · Tesco AI\nWooliesX · Carrefour AI", "X5 «Перекрёсток»\n(мировой уровень)", MID),
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
        text_box(s, x + 0.1, sy + 0.85, seg_w - 0.2, 0.4, "Международные",
                 size=10, bold=True, color=MID, align=PP_ALIGN.CENTER)
        text_box(s, x + 0.15, sy + 1.25, seg_w - 0.3, 1.5, intl,
                 size=10, color=DEEP, italic=True, align=PP_ALIGN.CENTER, line_spacing=1.4)
        # RU
        text_box(s, x + 0.1, sy + 3.0, seg_w - 0.2, 0.4, "Российские",
                 size=10, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
        text_box(s, x + 0.15, sy + 3.4, seg_w - 0.3, 1.3, ru,
                 size=10, color=DEEP, italic=True, align=PP_ALIGN.CENTER, line_spacing=1.4)

    add_footer(s, "Рыночный ландшафт без агитации. Родовая форма — «профильные технические университеты»")
    add_speaker_notes(s, load_speaker_notes("s36c"))

    # ============ s37 closing hero ============
    s = blank(prs); set_slide_bg(s, WHITE)

    # Top callback box
    ocean_box(s, 0.6, 0.4, 12.13, 2.5, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 0.55, 11.6, 0.5,
             "Возврат к началу лекции (Plenty Compton):",
             size=13, italic=True, color=GOLD, bold=True)
    text_box(s, 0.85, 1.05, 11.6, 0.7,
             "Plenty не закрылась из-за плохого ИИ.",
             size=26, bold=True, color=DEEP)
    text_box(s, 0.85, 1.8, 11.6, 0.7,
             "Plenty закрылась из-за термодинамики LED.",
             size=26, bold=True, color=GOLD)
    text_box(s, 0.85, 2.55, 11.6, 0.3,
             "Контроллер работал. Компьютерное зрение распознавало. Модель обучалась. LED ≈ 100× энергии солнца — AP1.",
             size=11, italic=True, color=DARK_GREY)

    # Mid: main payoff
    text_box(s, 0.6, 3.15, 12.13, 1.0,
             "Инженер держит лестницу в голове целиком,",
             size=22, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.3)
    text_box(s, 0.6, 3.65, 12.13, 0.9,
             "выбирая правильный инструмент для каждой ступени, и зная, где ИИ не работает и почему.",
             size=18, color=MID, italic=True, align=PP_ALIGN.CENTER, line_spacing=1.4)

    # Bottom: hero image + bridge
    ocean_box(s, 0.6, 4.7, 6.5, 2.0)
    p = ASSETS / "photos" / "p20-farmwise-titan.jpg"
    if p.exists():
        add_image(s, p, 0.85, 4.85, w=6.0, h=1.7)
    text_box(s, 0.85, 6.6, 6.0, 0.3,
             "Carbon Robotics LaserWeeder G2 · от поля до фабрики",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Bridge box
    ocean_box(s, 7.3, 4.7, 5.45, 2.0, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 7.5, 4.85, 5.05, 0.4, "Переход к Лекции 11",
             size=14, bold=True, color=DEEP)
    text_box(s, 7.5, 5.3, 5.05, 1.3,
             "L11 — кибер-физическое\n"
             "производство. Закрытый контур\n"
             "как L4-L5 + физический контакт\n"
             "ИИ с продуктом как L2. Прогностич.\n"
             "обслуживание · робото-сборка · контроль качества.",
             size=11, color=DEEP, italic=True, line_spacing=1.4)

    add_footer(s, "Спасибо. Дальше — вопросы и ответы · Carbon Robotics, businesswire 2025-02-10")
    add_speaker_notes(s, load_speaker_notes("s37"))

    # ============ s38 dedicated Q&A ============
    s = blank(prs); set_slide_bg(s, WHITE)

    # Big Q&A typography
    text_box(s, 0.6, 0.5, 12.13, 2.5, "Вопросы и ответы",
             size=64, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             font=H["FONT_HEAD"])

    text_box(s, 0.6, 3.2, 12.13, 0.5, "10 минут на обсуждение",
             size=18, italic=True, color=MID, align=PP_ALIGN.CENTER)

    # 3 backup prompts
    text_box(s, 0.6, 4.3, 12.13, 0.4, "Резервные вопросы",
             size=14, bold=True, color=MID, align=PP_ALIGN.CENTER)

    prompts = [
        ("Plenty и Bowery", "Почему именно вертикальные фермы в США?\nВ закрытой среде США vs Япония vs ОАЭ?"),
        ("Агентный ИИ", "Где ещё агентный ИИ работает\nв инженерных задачах — кроме хеджирования?"),
        ("Cognitive и ИТЭЛМА", "Можно ли построить гибридное решение\nCV + слияние сенсоров или это разные парадигмы?"),
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
