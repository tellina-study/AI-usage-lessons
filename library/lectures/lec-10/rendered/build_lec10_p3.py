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
    section_divider(prs, 3, "Точное животноводство",
        "L3 — уровень «животное». Полузакрытая среда + измерения на уровне особи. ИИ работает стабильнее, чем на L1-L2.",
        current_section=3,
        caption="4 working cases (SenseHub, CattleEye, DeLaval, Birdoo) · 3 анти-хайп урока (Cainthus, tie-stall, Holstein-bias)")
    add_speaker_notes(prs.slides[-1], load_speaker_notes("s22"))

    # ============ s22a Precision livestock — what stage (D2) ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Точное животноводство — что это за стадия", size=26, y=0.3)

    ocean_box(s, 0.6, 1.0, 12.13, 1.0)
    text_box(s, 0.85, 1.08, 11.6, 0.3,
             "Точное животноводство (precision livestock farming)",
             size=15, bold=True, color=DEEP)
    text_box(s, 0.85, 1.40, 11.6, 0.52,
             "Наблюдение и решения — по отдельному животному, а не по стаду в среднем. "
             "То же «точное», что в земледелии — только единица не участок поля, а голова.",
             size=11, italic=True, color=MID, line_spacing=1.2)

    # Row 2: что измеряют / какой вопрос
    ocean_box(s, 0.6, 2.10, 5.95, 1.45, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.8, 2.20, 5.55, 0.35, "Что измеряют", size=13, bold=True, color=DEEP)
    text_box(s, 0.8, 2.55, 5.55, 0.95,
             "Активность · руминация · температура\nПоходка · вес · корм и вода\nУдой · репродуктивный цикл · отёл",
             size=11, color=DEEP, italic=True, line_spacing=1.3)

    ocean_box(s, 6.68, 2.10, 6.05, 1.45, fill=TEAL_TINT, stroke=TEAL)
    text_box(s, 6.88, 2.20, 5.65, 0.35, "Какой вопрос решают", size=13, bold=True, color=DEEP)
    text_box(s, 6.88, 2.55, 5.65, 0.95,
             "Что сейчас с этим животным — и нужно ли вмешаться:\n"
             "осмотреть · вызвать ветеринара ·\nизолировать · осеменить · вывести из стада",
             size=11, color=DEEP, italic=True, line_spacing=1.3)

    # Row 3: 4 способа получения данных
    text_box(s, 0.6, 3.65, 12.13, 0.3, "Как получают данные",
             size=13, bold=True, color=MID)
    methods = [
        ("eye", "Визуальное наблюдение", "Обход стада и осмотр на проходе — основной способ и сегодня"),
        ("clipboard-check", "Плановый осмотр ветеринара", "По графику или по вызову, с физическим обследованием"),
        ("radar", "Бирка-датчик / ошейник", "Акселерометр и термодатчик — круглосуточно, не выборочно"),
        ("camera", "Камера над проходом", "Съёмка походки на выходе из доильного зала, без контакта"),
    ]
    card_w = (12.13 - 3 * 0.15) / 4
    mx = 0.6
    for icon_name, title, body in methods:
        ocean_box(s, mx, 4.00, card_w, 1.5)
        icon_p = ASSETS / "icons" / f"{icon_name}-96.png"
        if icon_p.exists():
            add_image(s, icon_p, mx + (card_w - 0.5) / 2, 4.12, w=0.5, h=0.5)
        text_box(s, mx + 0.1, 4.70, card_w - 0.2, 0.35, title,
                 size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, mx + 0.12, 5.05, card_w - 0.24, 0.42, body,
                 size=9.5, color=DARK_GREY, italic=True, align=PP_ALIGN.CENTER, line_spacing=1.2)
        mx += card_w + 0.15

    # Row 4: решение и место в цикле
    ocean_box(s, 0.6, 5.65, 12.13, 1.2, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 5.72, 11.6, 0.3, "Решение стадии и её место в цикле",
             size=13, bold=True, color=GOLD)
    text_box(s, 0.85, 6.02, 11.6, 0.78,
             "Вмешаться или нет — и чем: вызов ветеринара, лечение, изоляция, осеменение, выбраковка.\n"
             "Стоит параллельно полю и до переработки — первая стадия, где среда частично управляема (вентиляция, кормление задаёт хозяйство).\n"
             "Обратная связь — часы-дни, не сезон: поэтому здесь ИИ работает устойчивее, чем на L1-L2.",
             size=10, color=DEEP, italic=True, line_spacing=1.2)

    add_speaker_notes(s, load_speaker_notes("s22a"))

    # ============ s22b Precision livestock — without model (D1) ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Как это решают без модели — шесть классических режимов L3", size=22, y=0.3)

    text_box(s, 0.6, 1.0, 12.13, 0.4,
             "Шесть способов, которыми ферма и сегодня решает — без обученной модели:",
             size=14, italic=True, color=MID)

    regimes = [
        ("1", "Визуальное наблюдение зоотехника",
         "Обход стада с осмотром: дёшево на малом поголовье, нереализуемо на тысячах голов."),
        ("2", "Плановые осмотры ветеринара",
         "Регулярная проверка по графику: надёжно, но отклонение найдено не раньше следующего планового дня."),
        ("3", "Расчёт по среднему + журнал",
         "Отклонение видно по групповым показателям — с задержкой и без адреса на конкретное животное."),
        ("4", "Физическое взвешивание выборки",
         "Несколько голов на весах — результат переносится на всё поголовье (птица, откорм)."),
        ("5", "Доильный зал с оператором",
         "Человек сам присоединяет аппарат — и по ходу работы замечает состояние вымени."),
        ("6", "Общинный зоотехник с рассылкой",
         "Режим мелких хозяйств, где доход с головы слишком мал для датчика."),
    ]
    card_w = (12.13 - 2 * 0.15) / 3
    card_h = 1.8
    rx0, ry0 = 0.6, 1.7
    for i, (num, title, body) in enumerate(regimes):
        row, col = divmod(i, 3)
        x = rx0 + col * (card_w + 0.15)
        y = ry0 + row * (card_h + 0.15)
        ocean_box(s, x, y, card_w, card_h, fill=LIGHT_TINT if row == 0 else TEAL_TINT,
                  stroke=LIGHT if row == 0 else TEAL)
        text_box(s, x + 0.12, y + 0.1, 0.5, 0.4, num + ".", size=18, bold=True, color=GOLD)
        text_box(s, x + 0.12, y + 0.52, card_w - 0.24, 0.5, title,
                 size=12.5, bold=True, color=DEEP, line_spacing=1.1)
        text_box(s, x + 0.12, y + 1.02, card_w - 0.24, 0.72, body,
                 size=9.5, color=DARK_GREY, italic=True, line_spacing=1.2)

    bottom_y = ry0 + 2 * (card_h + 0.15) + 0.05
    ocean_box(s, 0.6, bottom_y, 12.13, 0.75, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, bottom_y + 0.1, 11.6, 0.55,
             "Общий знаменатель — $/год на то же стадо. Дальше — три режима на одном знаменателе "
             "+ порог стада + сегмент 1-10 коров.",
             size=12, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)

    add_speaker_notes(s, load_speaker_notes("s22b"))

    # ============ s23 SenseHub 2M cows ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Allflex SenseHub — 2 млн коров с сенсорами (≈0,75% из 265 млн молочных коров в мире)", size=22)

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
    text_box(s, 7.3, 1.6, 5.4, 0.3, "ИИ-конвейер (раннее предупреждение)",
             size=14, bold=True, color=MID)

    flow_steps = [
        ("1. Сенсор", "Акселерометр · 5-7 лет батарея", LIGHT),
        ("2. Облако", "ML-классификация поведения", MID),
        ("3. Сигнал фермеру", "Раннее предупреждение, не назначение", GOLD),
    ]
    fy = 1.95
    for hdr, sub, color in flow_steps:
        ocean_box(s, 7.3, fy, 5.4, 0.68, fill=LIGHT_TINT if color != GOLD else GOLD_TINT, stroke=color)
        text_box(s, 7.5, fy + 0.08, 5.0, 0.3, hdr,
                 size=14, bold=True, color=DEEP)
        text_box(s, 7.5, fy + 0.38, 5.0, 0.28, sub,
                 size=11, color=MID, italic=True)
        fy += 0.73

    # Alerts row
    text_box(s, 7.3, 4.15, 5.4, 0.28, "5 классов сигналов",
             size=13, bold=True, color=DEEP)
    alerts = ["эструс", "отёл", "хромота", "мастит", "пневмония"]
    ax = 7.3
    aw = 1.0
    for al in alerts:
        ocean_box(s, ax, 4.45, aw, 0.45, fill=GOLD_TINT, stroke=GOLD)
        text_box(s, ax, 4.45, aw, 0.45, al, size=10.5, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        ax += aw + 0.08

    # NEW: цена ошибки и сравнение с визуальным наблюдением
    text_box(s, 7.3, 4.98, 5.4, 0.28, "Цена ошибки и сравнение с визуальным наблюдением",
             size=11.5, bold=True, color=DEEP)
    plate_w = (5.4 - 0.15) / 2
    ocean_box(s, 7.3, 5.30, plate_w, 1.05, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 7.42, 5.36, plate_w - 0.24, 0.3, "FP", size=11, bold=True, color=DEEP)
    text_box(s, 7.42, 5.64, plate_w - 0.24, 0.68,
             "Лишний вызов вета: $50-200/визит. До 733 алертов/год на стадо "
             "при посредственной специфичности.",
             size=9.5, color=DARK_GREY, italic=True, line_spacing=1.15)
    ocean_box(s, 7.3 + plate_w + 0.15, 5.30, plate_w, 1.05, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 7.42 + plate_w + 0.15, 5.36, plate_w - 0.24, 0.3, "FN", size=11, bold=True, color=DEEP)
    text_box(s, 7.42 + plate_w + 0.15, 5.64, plate_w - 0.24, 0.68,
             "Пропущенный мастит: $500-1500/случай (эффект за лактацию); "
             "прямые издержки ниже — $250-450.",
             size=9.5, color=DARK_GREY, italic=True, line_spacing=1.15)

    text_box(s, 7.3, 6.40, 5.4, 0.35,
             "$/год на стадо (100 голов): SenseHub $4 600-5 700 vs визуальное наблюдение + вет $1 500-2 500",
             size=9.5, bold=True, italic=True, color=MID, line_spacing=1.15)

    # Bottom: augmentation principle (compact, one line)
    text_box(s, 7.3, 6.76, 5.4, 0.22,
             "ИИ = усиление человека, не замена",
             size=10.5, bold=True, italic=True, color=GOLD)

    add_footer(s, "Источники: Merck Animal Health 2025; Allflex/sensehub.co.nz pricing 2026; MSU/California dairy economics")
    add_speaker_notes(s, load_speaker_notes("s23"))

    # ============ s23a SenseHub — three regimes + threshold (mandatory form triple) ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Три режима L3 на одном стаде — и порог, где экономика переворачивается", size=21, y=0.3)

    # Ступень 1 — цена ошибки (recap)
    text_box(s, 0.6, 1.0, 12.13, 0.25, "Ступень 1 — цена ошибки (recap)", size=12, bold=True, color=MID)
    plate_w1 = (12.13 - 0.15) / 2
    ocean_box(s, 0.6, 1.28, plate_w1, 0.72, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.75, 1.33, plate_w1 - 0.3, 0.62,
             "FP — лишний вызов вета: $50-200/визит; до 733 алертов/год на стадо",
             size=10, color=DEEP, italic=True, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)
    ocean_box(s, 0.6 + plate_w1 + 0.15, 1.28, plate_w1, 0.72, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.75 + plate_w1 + 0.15, 1.33, plate_w1 - 0.3, 0.62,
             "FN — пропущенный мастит: $500-1500/случай за лактацию; прямые издержки ниже — $250-450",
             size=10, color=DEEP, italic=True, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)

    # Ступень 2 — три режима $/год на стадо 100 голов
    text_box(s, 0.6, 2.18, 12.13, 0.25,
             "Ступень 2 — три режима, один знаменатель: $/год на стадо в 100 голов", size=12, bold=True, color=MID)
    plate_w2 = (12.13 - 2 * 0.15) / 3
    regimes3 = [
        ("SenseHub (ИИ)",
         "$46-57/голова/год → $4 600-5 700/год.\n+ неучтённая цена накопленных FP-алертов — фактически выше",
         GOLD_TINT, GOLD),
        ("Визуальное наблюдение + вет",
         "$1 500-2 500/год на 100 голов — классический режим.\nДешевле в 2-3 раза при этом поголовье",
         LIGHT_TINT, LIGHT),
        ("Общинный зоотехник + SMS",
         "Другая единица — расходы разделены между\nтысячами фермеров (AIM for Scale). Числа $/год-\nна-стадо в открытых источниках нет",
         TEAL_TINT, TEAL),
    ]
    rx = 0.6
    for title, body, fill, stroke in regimes3:
        ocean_box(s, rx, 2.46, plate_w2, 1.25, fill=fill, stroke=stroke)
        text_box(s, rx + 0.12, 2.52, plate_w2 - 0.24, 0.42, title, size=11.5, bold=True, color=DEEP, line_spacing=1.1)
        text_box(s, rx + 0.12, 2.96, plate_w2 - 0.24, 0.7, body, size=9.5, color=DARK_GREY, italic=True, line_spacing=1.2)
        rx += plate_w2 + 0.15

    # Ступень 3 — порог стада
    text_box(s, 0.6, 3.86, 12.13, 0.25,
             "Ступень 3 — порог стада, где экономика переворачивается", size=12, bold=True, color=MID)
    plate_w3 = (12.13 - 0.15) / 2
    ocean_box(s, 0.6, 4.14, plate_w3, 0.95, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.75, 4.19, plate_w3 - 0.3, 0.3, "100 голов", size=12, bold=True, color=DEEP)
    text_box(s, 0.75, 4.50, plate_w3 - 0.3, 0.55,
             "$4 600-5 700/год против $1 500-2 500/год → ROI отрицательный, классика выигрывает",
             size=9.5, color=DARK_GREY, italic=True, line_spacing=1.15)
    ocean_box(s, 0.6 + plate_w3 + 0.15, 4.14, plate_w3, 0.95, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.75 + plate_w3 + 0.15, 4.19, plate_w3 - 0.3, 0.3, "500+ голов", size=12, bold=True, color=GOLD)
    text_box(s, 0.75 + plate_w3 + 0.15, 4.50, plate_w3 - 0.3, 0.55,
             "$23 000-28 500/год — малая доля затрат; экономия от раннего выявления → ROI положительный",
             size=9.5, color=DEEP, italic=True, line_spacing=1.15)

    # Ступень 4 (вывод) — сегмент 1-10 коров, доход с головы
    ocean_box(s, 0.6, 5.25, 12.13, 1.35, fill=TEAL_TINT, stroke=TEAL)
    text_box(s, 0.85, 5.33, 11.6, 0.3, "Что переехало — сегмент 1-10 коров (Восточная Африка)",
             size=12.5, bold=True, color=TEAL)
    text_runs(s, 0.85, 5.68, 11.6, 0.85, [
        {"text": "Доход с коровы — $200-500/год. Любая технология дороже $46/голову/год потребляет ", "size": 11, "color": DEEP, "italic": True},
        {"text": "9-29% годового дохода", "size": 11, "bold": True, "color": GOLD},
        {"text": "с головы — экономически невозможно.\nРаботает только общинный зоотехник + SMS: AIM for Scale (Gates Foundation) — 40 млн фермеров в Индии через SMS, без AI-оборудования на голову.", "size": 11, "color": DEEP, "italic": True, "newpara": True},
    ], line_spacing=1.25)

    add_footer(s, "Источники: Allflex/sensehub.co.nz pricing 2026 · MSU/California dairy economics · AIM for Scale, Gates Foundation")
    add_speaker_notes(s, load_speaker_notes("s23a"))

    # ============ s24 CattleEye + DeLaval + Birdoo ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "CattleEye + DeLaval VMS V310 + Cargill Birdoo — 3 рабочих кейса", size=22)

    cards = [
        ("CattleEye", "60 ферм · 11 000 коров", "Видеонаблюдение + ИИ в облаке:\nоценка хромоты · сеть GEA >250 000", LIGHT),
        ("DeLaval VMS V310", "99,8% успешного подключения", "998/1000 успешных подключений\nруки доильного аппарата", GOLD),
        ("Cargill Birdoo", ">95% точность", "Компьютерное зрение для оценки\nвеса · экономия 10-30 г корма / бройлера", MID),
    ]
    # Real product images — named изделия, не родовые коровы (K-2 fix):
    #   CattleEye — GEA official product page (CV bounding-box detection on cow)
    #   DeLaval VMS V310 — press photo via DairyReporter launch article
    #   Cargill Birdoo — official brand asset via PR Newswire press release
    product_images = [
        ("p24-cattleeye-ui.jpg", 1200, 675),
        ("p24-delaval-vms.jpg", 1200, 630),
        ("p24-birdoo-logo.png", 600, 315),
    ]
    card_w = 3.95; card_h = 4.5; gap = 0.18
    sx = 0.6
    sy = 1.6
    img_h = 1.75
    for i, (name, kpi, desc, color) in enumerate(cards):
        x = sx + i * (card_w + gap)
        ocean_box(s, x, sy, card_w, card_h, fill=LIGHT_TINT if color != GOLD else GOLD_TINT, stroke=color)
        fname, nat_w, nat_h = product_images[i]
        p = ASSETS / "photos" / fname
        if p.exists():
            img_w = img_h * (nat_w / nat_h)
            img_w = min(img_w, card_w - 0.3)
            img_h_eff = img_w * (nat_h / nat_w)
            add_image(s, p, x + (card_w - img_w) / 2, sy + 0.2, w=img_w, h=img_h_eff)
        text_box(s, x + 0.15, sy + 2.15, card_w - 0.3, 0.45, name,
                 size=15, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x + 0.15, sy + 2.65, card_w - 0.3, 0.5, kpi,
                 size=15, bold=True, color=GOLD if color != GOLD else DEEP,
                 align=PP_ALIGN.CENTER)
        text_box(s, x + 0.2, sy + 3.2, card_w - 0.4, 1.2, desc,
                 size=10, color=DARK_GREY, italic=True,
                 align=PP_ALIGN.CENTER, line_spacing=1.4)

    add_footer(s, "Источники: Fortune 2025-06; DeLaval press 2025-04; Cargill.com 2025 · Фото: gea.com/cattleeye; DairyReporter 2019; PR Newswire 2022")
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
        if icon_name == "lock":
            # Привязное содержание — real tie-stall barn photo, not a generic icon.
            photo_p = ASSETS / "photos" / "p25-tiestall-barn.jpg"
            if photo_p.exists():
                add_image(s, photo_p, 0.7, sy + 0.25, w=1.25, h=1.0)
            else:
                icon_p = ASSETS / "icons" / f"{icon_name}-96.png"
                if icon_p.exists():
                    add_image(s, icon_p, 0.85, sy + 0.3, w=0.9, h=0.9)
        else:
            icon_p = ASSETS / "icons" / f"{icon_name}-96.png"
            if icon_p.exists():
                add_image(s, icon_p, 0.85, sy + 0.3, w=0.9, h=0.9)
        text_box(s, 2.1, sy + 0.15, 3.95, 0.4, name,
                 size=14, bold=True, color=DEEP)
        text_box(s, 2.1, sy + 0.55, 3.95, 0.4, key,
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
    section_divider(prs, 4, "Агрологистика и товарный трейдинг",
        "L4 — уровень «цепочка». Агентный ИИ лидирует. Результат измеряется в долях процента за минуты, не в сезонах.",
        current_section=4,
        caption="4 working cases (Cargill CMAX, Tract, Olam, Walmart×Cropin) · 2 провала (USDA, Verra) · РФ-параллель (X5/Магнит/РСХБ)")
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

    # Right: KPIs — с baseline counterfactuals
    kpis = [
        ("70+ стран", "из 195 (≈36% мира) · ~155k штат", LIGHT),
        ("1000+ объектов", "склады / порты / силосы Cargill", MID),
        ("BIG AI 2026", "Excellence Award на уровне L4", GOLD),
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
    text_box(s, 8.0, 5.6, 4.55, 0.4, "Принцип успеха: узость агента",
             size=14, bold=True, color=DEEP)
    text_box(s, 8.0, 6.0, 4.55, 0.7,
             "Одно действие на агента (хеджирование / маршрут) + человек в петле для сделок >$10 млн номинала.",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.4)

    add_footer(s, "Источник: пресс-релиз Cargill, апрель 2026 (BIG AI Excellence Award)")
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
        ("3. Решение", "4 действия:\nкупить / продать /\nдержать / хеджировать\n+ человек при >$10 млн номинала",
         "Слой действий", "settings"),
        ("4. Обратная связь", "bp (базисный пункт) за минуты,\nонлайн-обучение",
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
        ("$3,1 млрд", "финансирование · ≈$23M / проект ср."),
        ("135 проектов", "отменены"),
        ("14 000 ферм", "потеряли поддержку"),
        ("3,2 млн акров", "≈0,36% от 900M акров US ag"),
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
    # Decorative digit stays plain "4" — "4-bis" as a literal string overflows at 400pt.
    section_divider(prs, 4, "Инфраструктурные условия: связь, привязка к вендору, регуляторика",
        "Сквозной meta-уровень: всё, без чего ни одна ступень не работает.",
        current_section=5,
        caption="3 sub-блока (связь / vendor lock-in двойная оптика / регуляторика) · 3 анти-ИИ критерия (AP5, AP6, AP7)")
    add_speaker_notes(prs.slides[-1], load_speaker_notes("s33"))

    # ============ s34 Connectivity + GNSS ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Связь — 18% ферм без интернета + помехи навигации в I кв. 2025",
        size=22)

    # Top: 3 mega-numbers — с baselines
    nums = [
        ("18%", "≈360k из 2M ферм США\nбез интернета (vs <1% urban)", GOLD),
        ("123 000", "≈1,2% от 10M рейсов\nQ1 2025 (vs <1k Q1 2022)", DEEP),
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

    # Left: anti-theft success — real news photo (CNN, Melitopol story, May 2022)
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
    p = ASSETS / "photos" / "p30b-melitopol-tractor.jpg"
    if p.exists():
        add_image(s, p, 0.85, 4.5, w=5.5, h=1.55)
    text_box(s, 0.85, 6.1, 5.5, 0.3,
             "John Deere в Украине · CNN, 2022-05-01 — ИИ-функция безопасности, успех в этой петле",
             size=9, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Right: control surface optic — real photos (The Register / DJI.com official)
    ocean_box(s, 6.8, 1.5, 6.0, 5.0, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, 1.65, 4.2, 0.5, "Янв. 2025 — FTC против Deere",
             size=14, bold=True, color=GOLD)
    text_box(s, 7.05, 2.15, 4.2, 0.4, "Десятилетние ограничения ремонта",
             size=10.5, italic=True, color=MID)
    ftc_p = ASSETS / "photos" / "p30b-ftc-deere-tractors.jpg"
    if ftc_p.exists():
        add_image(s, ftc_p, 11.4, 1.65, w=1.25, h=0.712)
    text_box(s, 7.05, 2.65, 5.5, 1.75,
             "Один и тот же механизм:\n"
             "удалённая блокировка = безопасность сегодня =\n"
             "поверхность контроля завтра. Фермер\n"
             "не может ремонтировать без\n"
             "разрешения вендора.",
             size=11.5, color=DEEP, italic=True, line_spacing=1.35)
    hr_line(s, 7.05, 4.5, 5.5, color=GOLD, weight=1.2)
    text_box(s, 7.05, 4.65, 4.2, 0.4, "Декабрь 2025 — FCC запретил DJI",
             size=12.5, bold=True, color=DEEP)
    dji_p = ASSETS / "photos" / "p30b-dji-agras.png"
    if dji_p.exists():
        add_image(s, dji_p, 11.5, 4.62, w=1.1, h=1.1)
    text_box(s, 7.05, 5.1, 5.5, 1.35,
             "80-90% сельхоз-дронов в США потеряли\n"
             "легальный статус. Одно решение FCC —\n"
             "привязка к вендору стала геополитическим риском.",
             size=10.5, color=DARK_GREY, italic=True, line_spacing=1.4)

    add_footer(s, "Фото: CNN 2022-05-01; The Register 2025-01-15; dji.com/t40 · Источники: The Register 2022-05-02; CSO Online 572811; пресс-релиз FTC 2025-01-15")
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
        if i == 0:
            # EU AI Act column — real EU flag badge (Wikimedia Commons, Flag of Europe.svg)
            flag_p = ASSETS / "photos" / "p35-eu-flag.jpg"
            if flag_p.exists():
                add_image(s, flag_p, x + col_w - 0.65, sy + 0.12, w=0.5, h=0.333)
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

    add_footer(s, "Источники: Cambridge EJRR 2024; USDA AI Strategy FY2025-26; Распоряжение Правительства РФ 31.12.2025; флаг ЕС — Wikimedia Commons")
    add_speaker_notes(s, load_speaker_notes("s35"))

    # ============ s36 section5 divider — Полка ============
    section_divider(prs, 5, "Управление спросом в розничной цепочке",
        "L5 — уровень «полка». Розничный ИИ зрел + пять анти-ИИ критериев + чек-лист + карьерный ландшафт + замыкание к Plenty.",
        current_section=6,
        caption="L5 кратко (Walmart, Tesco, X5, Магнит F&R) + 5 критериев + чек-лист + карьера + closing callback")
    add_speaker_notes(prs.slides[-1], load_speaker_notes("s36"))

    # ============ s37s L5 retail — hero photo + 2×2 grid (D1 Магнит F&R as 4th card) ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L5 — Walmart Eden + Tesco AI + X5 «Перекрёсток» + Магнит F&R (гибрид)",
        size=20, y=0.25)

    # Hero context photo — real supermarket aisle (fully digitised retail environment)
    ocean_box(s, 0.6, 1.1, 12.13, 0.92, fill=SURFACE, stroke=LIGHT)
    hero_p = ASSETS / "photos" / "p37s-supermarket-aisle.jpg"
    if hero_p.exists():
        add_image(s, hero_p, 0.68, 1.16, w=0.70, h=0.80)
    text_box(s, 1.55, 1.2, 10.9, 0.3,
             "L5 — полностью оцифрованная среда: у каждого товара (SKU) есть цифровой след",
             size=12, bold=True, color=DEEP)
    text_box(s, 1.55, 1.55, 10.9, 0.4,
             "Проход супермаркета с напольной навигацией — среда, где каждое действие фиксируется в реальном времени",
             size=10, italic=True, color=MID, line_spacing=1.2)

    cards = [
        ("Walmart Eden", "ML с 2017",
         "Прогноз скоропортящихся +\nмаршруты свежести на 11 000+ магазинов",
         GOLD),
        ("Tesco AI", "−30% пищевых отходов",
         "С 2017 — ежедневный прогноз\nна ~3500 супермаркетов Великобритании",
         MID),
        ("X5 «Перекрёсток»", "ML с 2020 · 200+ факторов",
         "Российский флагман L5.\nМировой уровень.",
         LIGHT),
        ("Магнит F&R (гибрид)", "Прогноз ✓ · Пополнение — пилот",
         "Прогнозирование на 46 РЦ январь 2026 — в эксплуатации.\nПополнение — пилот на 3 РЦ.",
         TEAL),
    ]
    # 2×2 grid
    card_w = 6.0; card_h = 2.18; gap_x = 0.18; gap_y = 0.13
    sx = 0.6; sy = 2.2
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
            add_image(s, icon_p, x + 0.2, y + 0.2, w=0.6, h=0.6)
        text_box(s, x + 0.95, y + 0.18, card_w - 1.1, 0.4, name,
                 size=14, bold=True, color=DEEP)
        text_box(s, x + 0.95, y + 0.58, card_w - 1.1, 0.35, kpi,
                 size=12, bold=True, color=color, line_spacing=1.2)
        text_box(s, x + 0.2, y + 1.0, card_w - 0.4, 1.1, desc,
                 size=10.5, color=DARK_GREY, italic=True, line_spacing=1.3)

    # Bottom caveat row (compact)
    ocean_box(s, 0.6, 6.57, 12.13, 0.42, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 6.60, 11.6, 0.35,
             "⚠ Оговорка: L5 — розничный ИИ, не агро. Магнит F&R — нюанс «гибрид»: прогноз в промышленной эксплуатации, пополнение — пилот.",
             size=10.5, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Walmart corporate 2025 · Tesco AI annual report · X5 Tech 2024 · Habr Магнит 2026-01")
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
        ("L3 Животное", "DeLaval · GEA · Lely\nCargill Birdoo · Allflex", "Connectome.ai · Сколково", LIGHT),
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

    # ============ s37 closing hero (hero photo ≥40% area + number-refrain) ============
    s = blank(prs); set_slide_bg(s, WHITE)

    # Compact top callback (Plenty Compton)
    text_box(s, 0.6, 0.16, 12.13, 0.38,
             "Plenty не закрылась из-за плохого ИИ.",
             size=20, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, 0.6, 0.56, 12.13, 0.38,
             "Plenty закрылась из-за термодинамики LED.",
             size=20, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(s, 0.6, 0.96, 12.13, 0.24,
             "Контроллер работал. CV распознавало. LED ≈ 100× энергии солнца — AP1.",
             size=10, italic=True, color=DARK_GREY, align=PP_ALIGN.CENTER)

    # Hero photo frame — LaserWeeder G2 (same canonical success-case photo as s16,
    # letterbox-cropped for this band; ≥40% of slide area)
    ocean_box(s, 0.6, 1.24, 12.13, 4.05, fill=SURFACE, stroke=LIGHT)
    p = ASSETS / "photos" / "p37-laserweeder-hero-crop.jpg"
    if p.exists():
        add_image(s, p, 0.68, 1.32, w=11.97, h=3.894)
    text_box(s, 0.6, 5.33, 12.13, 0.25,
             "Carbon Robotics LaserWeeder G2 · февраль 2025 · carbonrobotics.com",
             size=10.5, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Main payoff
    text_box(s, 0.6, 5.62, 12.13, 0.33,
             "Инженер держит лестницу в голове — и знает, где ИИ не работает и почему.",
             size=16, bold=True, color=DEEP, align=PP_ALIGN.CENTER)

    # Bridge to Lec-11
    text_box(s, 0.6, 5.98, 12.13, 0.28,
             "Дальше — Лекция 11: кибер-физическое производство (L11).",
             size=12, italic=True, color=MID, align=PP_ALIGN.CENTER)

    # Number-refrain (сквозная линия лекции)
    ocean_box(s, 0.6, 6.30, 12.13, 0.32, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.6, 6.30, 12.13, 0.32,
             "18 из 45 случаев этой лекции — исход приписывают ИИ, а причина другая (40%)",
             size=11.5, bold=True, color=GOLD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    add_footer(s, "Спасибо. Дальше — вопросы и ответы")
    add_speaker_notes(s, load_speaker_notes("s37"))

    # ============ s38 dedicated Q&A ============
    s = blank(prs); set_slide_bg(s, WHITE)

    # Big Q&A typography
    text_box(s, 0.6, 0.5, 12.13, 2.5, "Вопросы и ответы",
             size=64, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             font=H["FONT_HEAD"])

    text_box(s, 0.6, 3.2, 12.13, 0.5, "Резервные вопросы про термодинамику VF, agentic AI scope, ИТЭЛМА vs Cognitive Pilot, foundation models",
             size=14, italic=True, color=MID, align=PP_ALIGN.CENTER)

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
