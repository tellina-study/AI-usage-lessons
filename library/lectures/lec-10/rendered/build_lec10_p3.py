"""
Part 3: s22-s38 — L3 Животное + Р4 Среда + L4 Полка + closing + Q&A.
12 слайдов (issue #340 v3.9: старый Раздел 4 «Агрологистика и товарный
трейдинг» — s27 divider + s28-s32 — удалён целиком по указанию владельца;
3 дивайдера s22/s33/s36 получили hero-фото через divider_hero()).
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
    FONT_HEAD = H["FONT_HEAD"]

    def divider_hero(number, title, frame_phrase, current_section, caption,
                      image_filename, image_caption, title_size=22):
        """Section divider с hero-фото справа (issue #340, owner note: добавить
        иллюстрации на дивайдеры — s22/s33/s36, было 4 с s27, удалён v3.9).
        Левая колонка — компактный
        decorative number + title + frame_phrase; правая — real photo (6-tier
        acquisition, Wikimedia CC) в ocean box, ≥40% площади слайда, с caption-
        источником. Caption-строка статистики раздела и progress bar — тот же
        паттерн и та же позиция, что у plain-дивайдеров (section_divider)."""
        s = blank(prs); set_slide_bg(s, WHITE)

        # Left column — number (крупный, несёт визуальный вес колонки) + title +
        # frame_phrase идут сразу друг за другом компактно; единственный зазор —
        # внизу, перед caption-строкой (а не растянут между title и frame —
        # см. Visual Mass Balance, «плавающее» пустое пространство).
        text_box(s, 0.5, 0.3, 4.5, 2.3, str(number),
                 size=160, bold=True, color=COVER_OUTLINE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 font=FONT_HEAD, line_spacing=0.9)
        text_box(s, 0.5, 2.65, 4.5, 0.95, title,
                 size=title_size, bold=True, color=DEEP, line_spacing=1.15)
        text_box(s, 0.5, 3.7, 4.5, 1.5, frame_phrase,
                 size=14.5, italic=True, color=MID, line_spacing=1.25)

        # Right column — hero photo (≥40% площади слайда: 7.383×5.55" ≈ 41.0in²
        # из 100in² полного кадра 13.333×7.5"; aspect 1.330 ≈ 4:3 источника —
        # минимальный stretch при cover-crop на этапе подготовки фото).
        box_x, box_w = 5.15, 7.683
        ocean_box(s, box_x, 0.35, box_w, 5.75, fill=SURFACE, stroke=LIGHT)
        p = ASSETS / "photos" / image_filename
        if p.exists():
            add_image(s, p, box_x + 0.15, 0.45, w=box_w - 0.3, h=5.55)
        text_box(s, box_x + 0.15, 6.15, box_w - 0.3, 0.24, image_caption,
                 size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

        # Caption + progress bar
        text_box(s, 0.6, 6.55, 12.13, 0.35, caption,
                 size=12, italic=True, color=LIGHT, align=PP_ALIGN.LEFT)
        add_progress_bar(s, current_section=current_section, y=6.95)
        return s

    # ============ s22 section3 divider — L3 Животное ============
    divider_hero(3, "Точное животноводство",
        "L3 — уровень «животное». Полузакрытая среда + измерения на уровне особи. ИИ работает стабильнее, чем на L1-L2.",
        current_section=3,
        caption="4 working cases (SenseHub, CattleEye, DeLaval, Birdoo) · 3 анти-хайп урока (Cainthus, tie-stall, Holstein-bias)",
        image_filename="p22-cow-eartag-milking-robot.jpg",
        image_caption="Коровы с ушными бирками у автоматической доильной системы · Wikimedia, CC BY-SA 4.0")
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
    # issue #340 round 2 ("фото сплющены — корова"): p23-cow-ear-tag.jpg was a
    # TALL PORTRAIT (1280x1927, AR 0.66) forced into a w=6.0 h=4.0 (AR 1.5)
    # landscape frame — stretching it ~2.3x wider than tall. A straight crop to
    # AR 1.5 would have cut off the cow's legs or head (the animal fills the
    # portrait frame edge-to-edge), so this was re-sourced entirely: a
    # genuinely landscape (AR 1.5, matches the frame exactly, zero crop needed)
    # public-domain USDA photo showing ear tags just as clearly. See
    # p23-cow-eartag-landscape.jpg.url.
    ocean_box(s, 0.6, 1.5, 6.5, 5.1)
    p = ASSETS / "photos" / "p23-cow-eartag-landscape.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.75, w=6.0, h=4.0)
    _s23_cap = text_runs(s, 0.85, 5.85, 6.0, 0.3, [
        {"text": "Holstein с ушными бирками · ", "size": 10, "italic": True, "color": LIGHT},
        {"text": "USDA, Preston Keres, public domain",
         "size": 10, "italic": True, "color": LIGHT},
    ], align=PP_ALIGN.CENTER)
    _s23_cruns = [r for para in _s23_cap.text_frame.paragraphs for r in para.runs]
    _s23_cruns[-1].font.underline = True
    _s23_cruns[-1].hyperlink.address = "https://commons.wikimedia.org/wiki/File:20180124-OSEC-PJK-0944_TONED_(39891699741).jpg"
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

    # ============ s23c SenseHub — engineering vs AI split (issue #340, owner note) ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "SenseHub — ошейник и модель по отдельности", size=24, y=0.3)
    text_box(s, 0.6, 1.0, 12.13, 0.4,
             "Теперь разделим это на слои: что в ошейнике — и что в облаке.",
             size=14, italic=True, color=MID)

    col_w = (12.13 - 0.3) / 2
    col_h = 4.3
    col_y = 1.55
    lx = 0.6
    rx = lx + col_w + 0.3

    # Left column — «Железо» (issue #340 owner follow-up 2026-11-20: реальное фото устройства
    # вместо родового иконки «radar» — официальный product cutout из брошюры Allflex/MSD
    # SenseHub, та самая «ошейник-сенсор», которую описывает текст справа).
    ocean_box(s, lx, col_y, col_w, col_h, fill=LIGHT_TINT, stroke=LIGHT)
    ip = ASSETS / "photos" / "p23c-sensehub-collar-device.jpg"
    _dev_h = 0.75
    _dev_w = _dev_h * (324 / 445)  # native AR of product cutout — no crop needed, no stretch
    if ip.exists():
        # Source photo has a solid black studio backdrop (not transparency) — a thin white
        # mat behind it reads as a deliberate framed product shot, not a stray black square
        # against the card's light-tint fill.
        ocean_box(s, lx + 0.25 - 0.06, col_y + 0.20 - 0.06, _dev_w + 0.12, _dev_h + 0.12,
                  fill=WHITE, stroke=LIGHT, stroke_pt=1.0, radius_pt=4.0)
        add_image(s, ip, lx + 0.25, col_y + 0.20, w=_dev_w, h=_dev_h)
    text_box(s, lx + 1.0, col_y + 0.28, col_w - 1.2, 0.5, "Железо — ошейник-сенсор",
             size=16, bold=True, color=DEEP)
    text_box(s, lx + 0.3, col_y + 1.0, col_w - 0.6, 0.6,
             "Акселерометр + температурный датчик + position-tracking — три измеряемых сигнала",
             size=11.5, color=DEEP, italic=True, line_spacing=1.25)

    ip2 = ASSETS / "icons" / "zap-48.png"
    if ip2.exists():
        add_image(s, ip2, lx + 0.3, col_y + 1.72, w=0.4, h=0.4)
    text_box(s, lx + 0.82, col_y + 1.68, col_w - 1.1, 0.55,
             "Батарея — 5-7 лет работы без замены",
             size=12.5, bold=True, color=GOLD, line_spacing=1.2)

    text_box(s, lx + 0.3, col_y + 2.35, col_w - 0.6, 0.85,
             "Канал передачи данных с фермы в облако — в открытых источниках "
             "Merck/Allflex не детализирован (честно названный пробел)",
             size=10.5, color=DARK_GREY, italic=True, line_spacing=1.25)

    ocean_box(s, lx + 0.2, col_y + col_h - 0.95, col_w - 0.4, 0.78, fill=SURFACE, stroke=LIGHT, stroke_pt=1.0)
    text_box(s, lx + 0.35, col_y + col_h - 0.86, col_w - 0.7, 0.6,
             "Физически один и тот же сенсор — вне зависимости от того, какой "
             "алгоритм обрабатывает сигнал дальше",
             size=10.5, italic=True, color=MID, line_spacing=1.2, anchor=MSO_ANCHOR.MIDDLE)

    # Right column — «Модель»
    ocean_box(s, rx, col_y, col_w, col_h, fill=TEAL_TINT, stroke=TEAL)
    ip3 = ASSETS / "icons" / "cpu-96.png"
    if ip3.exists():
        add_image(s, ip3, rx + 0.25, col_y + 0.22, w=0.6, h=0.6)
    text_box(s, rx + 1.0, col_y + 0.28, col_w - 1.2, 0.5, "Модель — облачный ML-конвейер",
             size=16, bold=True, color=DEEP)
    text_box(s, rx + 0.3, col_y + 1.0, col_w - 0.6, 0.72,
             "Обучение на индивидуальном базовом уровне каждой коровы — первые "
             "недели после установки ошейника",
             size=11.5, color=DEEP, italic=True, line_spacing=1.25)

    ip4 = ASSETS / "icons" / "layers-48.png"
    if ip4.exists():
        add_image(s, ip4, rx + 0.3, col_y + 1.85, w=0.4, h=0.4)
    text_box(s, rx + 0.82, col_y + 1.80, col_w - 1.1, 0.55,
             "Сравнение с опорным уровнем стада И конкретной коровы",
             size=11.5, bold=True, color=TEAL, line_spacing=1.2)

    alerts_row_y = col_y + 2.55
    text_box(s, rx + 0.3, alerts_row_y, col_w - 0.6, 0.3,
             "Классификация отклонения в 5 типов алертов:",
             size=11, bold=True, color=DEEP)
    alerts5 = ["эструс", "отёл", "хромота", "мастит", "BRD"]
    aw = (col_w - 0.6 - 4 * 0.08) / 5
    ax = rx + 0.3
    for al in alerts5:
        ocean_box(s, ax, alerts_row_y + 0.35, aw, 0.42, fill=GOLD_TINT, stroke=GOLD)
        text_box(s, ax, alerts_row_y + 0.35, aw, 0.42, al, size=9, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        ax += aw + 0.08

    ocean_box(s, rx + 0.2, col_y + col_h - 0.95, col_w - 0.4, 0.78, fill=SURFACE, stroke=TEAL, stroke_pt=1.0)
    text_box(s, rx + 0.35, col_y + col_h - 0.86, col_w - 0.7, 0.6,
             "Обновляется отдельно от железа — новая версия модели не требует "
             "замены ошейника на ферме",
             size=10.5, italic=True, color=TEAL, line_spacing=1.2, anchor=MSO_ANCHOR.MIDDLE)

    # Bottom synthesis band
    synth_y = col_y + col_h + 0.15
    ocean_box(s, 0.6, synth_y, 12.13, 0.75, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, synth_y + 0.08, 11.6, 0.6,
             "Почему это разделение важно: цена ошибки (FP/FN), которую разберём дальше, — "
             "свойство модели, а не датчика. Тот же ошейник с другим алгоритмом даёт другую экономику.",
             size=12, bold=True, italic=True, color=DEEP, line_spacing=1.2, anchor=MSO_ANCHOR.MIDDLE)

    _s23c_foot = text_runs(s, 0.5, 7.05, 12.33, 0.30, [
        {"text": "Источники: Merck Animal Health 2025; ", "size": 9.5, "italic": True, "color": LIGHT},
        {"text": "SenseHub product info (Allflex/MSD brochure)",
         "size": 9.5, "italic": True, "color": LIGHT},
        {"text": " — транспортный протокол передачи данных не раскрыт в открытых источниках",
         "size": 9.5, "italic": True, "color": LIGHT},
    ], anchor=MSO_ANCHOR.MIDDLE)
    _s23c_fr = [r for p in _s23c_foot.text_frame.paragraphs for r in p.runs]
    _s23c_fr[1].font.underline = True
    _s23c_fr[1].hyperlink.address = "https://www.allflex.global/wp-content/uploads/2021/06/SH_Allflex_MSD_8_A4_Eng_May_21.pdf"
    add_speaker_notes(s, load_speaker_notes("s23c"))

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
    # v2 (owner follow-up 2026-11-20): переверстано вокруг пары «на чём учили /
    # хорошие метрики» (свободное содержание, голштинская порода — CV работает)
    # vs «на чём сломалось» (привязное содержание — освещение слабое, силуэты
    # перекрыты). Прежняя версия имела только маленькое (1.25"x1.0") превью
    # tie-stall-сарая и НИ ОДНОГО фото Holstein, хотя footer утверждал обратное
    # ("Источники: Wikimedia Commons (Holstein)") — несоответствие исправлено:
    # обе стороны теперь настоящие большие фото со своими источниками. 3 анти-
    # хайп урока сведены в компактную 3-колоночную полосу снизу (полный текст —
    # в speaker notes дословно).
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Cainthus, привязное содержание, голштинский уклон — 3 анти-хайп урока L3",
        size=19)

    PANEL_Y, PANEL_H, PANEL_W = 1.15, 3.35, 5.95
    LX, RX = 0.6, 6.8
    ocean_box(s, LX, PANEL_Y, PANEL_W, PANEL_H, fill=SURFACE)
    ocean_box(s, RX, PANEL_Y, PANEL_W, PANEL_H, fill=SURFACE)
    _p_free = ASSETS / "photos" / "p22-cow-eartag-milking-robot-crop.jpg"
    _p_tie = ASSETS / "photos" / "p25-tiestall-anbindehaltung-crop.jpg"
    _pad = 0.07
    if _p_free.exists():
        add_image(s, _p_free, LX + _pad, PANEL_Y + _pad, w=PANEL_W - 2 * _pad, h=PANEL_H - 2 * _pad)
    if _p_tie.exists():
        add_image(s, _p_tie, RX + _pad, PANEL_Y + _pad, w=PANEL_W - 2 * _pad, h=PANEL_H - 2 * _pad)

    cap_y = PANEL_Y + PANEL_H + 0.06
    text_runs(s, LX, cap_y, PANEL_W, 0.52, [
        {"text": "Свободное содержание, голштинская порода — ", "size": 10.5, "italic": True, "color": DEEP},
        {"text": "CV работает", "size": 11.5, "bold": True, "color": GOLD},
        {"text": " (SenseHub, CattleEye)", "size": 10.5, "italic": True, "color": DEEP},
    ], align=PP_ALIGN.CENTER, line_spacing=1.1)
    text_runs(s, RX, cap_y, PANEL_W, 0.52, [
        {"text": "Привязное содержание — освещение слабое, силуэты перекрыты — ",
         "size": 10.5, "italic": True, "color": DEEP},
        {"text": "CV не работает", "size": 11.5, "bold": True, "color": MID},
    ], align=PP_ALIGN.CENTER, line_spacing=1.1)

    # Вывод-плашка
    ap_y = cap_y + 0.56
    ocean_box(s, 0.6, ap_y, 12.13, 0.56, fill=TEAL_TINT, stroke=TEAL)
    text_box(s, 0.8, ap_y + 0.05, 11.7, 0.46,
             "AI capability ≠ AI applicability: та же модель, рабочая на free-stall в Висконсине, "
             "не работает на tie-stall в Калужской области — причина архитектура хозяйства, не «российский контекст».",
             size=10.5, bold=True, color=TEAL, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)

    # 3 анти-хайп урока — компактная строка (полный текст — в speaker notes)
    row_y = ap_y + 0.64
    row_h = 0.78
    rw = (12.13 - 0.4) / 3
    lessons3 = [
        ("Cainthus (Cargill 2018)", "Анонс ≠ внедрение: публичных production-метрик нет",
         LIGHT_TINT, LIGHT),
        ("Привязное содержание", "Архитектура ломает CV — см. фото справа",
         GOLD_TINT, GOLD),
        ("Голштинский уклон", "Обучен на Holstein; Ярославская/Якутская — другая морфология",
         TEAL_TINT, TEAL),
    ]
    rx = 0.6
    for name, desc, fill, stroke in lessons3:
        ocean_box(s, rx, row_y, rw, row_h, fill=fill, stroke=stroke)
        text_box(s, rx + 0.15, row_y + 0.06, rw - 0.3, 0.26, name,
                 size=10.5, bold=True, color=DEEP, line_spacing=1.0)
        text_box(s, rx + 0.15, row_y + 0.33, rw - 0.3, 0.42, desc,
                 size=8.6, italic=True, color=DARK_GREY, line_spacing=1.1)
        rx += rw + 0.2

    _s25_foot = text_runs(s, 0.5, 7.05, 12.33, 0.30, [
        {"text": "Источники: Chapter v3.1 §3.4; Cargill 2018 (Cainthus); Connecterra independent disambig · фото: ",
         "size": 9, "italic": True, "color": LIGHT},
        {"text": "Holstein free-stall — Wikimedia CC BY-SA 4.0",
         "size": 9, "italic": True, "color": LIGHT},
        {"text": " · ", "size": 9, "italic": True, "color": LIGHT},
        {"text": "tie-stall — Wikimedia CC BY-SA 2.0",
         "size": 9, "italic": True, "color": LIGHT},
    ], anchor=MSO_ANCHOR.MIDDLE)
    _s25_fr = [r for p in _s25_foot.text_frame.paragraphs for r in p.runs]
    _s25_fr[1].font.underline = True
    _s25_fr[1].hyperlink.address = "https://commons.wikimedia.org/wiki/File:Holstein_Friesian_cows_queuing_for_milking_in_an_automatic_milking_system_in_Bron%C3%B3w.jpg"
    _s25_fr[3].font.underline = True
    _s25_fr[3].hyperlink.address = "https://commons.wikimedia.org/wiki/File:Milchvieh_in_Anbindehaltung.jpg"

    add_speaker_notes(s, load_speaker_notes("s25"))

    # ============ s26 РФ L3 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L3 в РФ — Connectome.ai + санкционная неопределённость молочного ИИ-стека",
        size=20)

    # Left: working case
    # Issue #340 visual-richness pass (owner: РФ-слайды только иконки/схемы —
    # без крупных реальных фото). Decorative icon заменён реальным фото
    # новорождённого телёнка (Tier 2, Wikimedia Commons) — предмет именно
    # того контроля, который детектирует CV-система Connectome.ai.
    # Row1 (works/under-question) compressed h 5.0→3.3 to make room for a
    # bottom band (хромота КРС: РГАУ-МСХА+АгроЭко + ЦПС «Объектив»,
    # chapter-part2.md §3.6 [for-slide-s26x-ru]).
    ocean_box(s, 0.6, 1.5, 6.0, 3.3, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.85, 1.65, 5.5, 0.35, "Работает — Connectome.ai",
             size=14, bold=True, color=DEEP)
    _s26_photo = ASSETS / "photos" / "p26-newborn-calf-cows.jpg"
    if _s26_photo.exists():
        _s26_ph = 1.0
        _s26_pw = _s26_ph * 1.332
        add_image(s, _s26_photo, 0.85 + (5.5 - _s26_pw) / 2, 2.05, w=_s26_pw, h=_s26_ph)
    else:
        icon_p = ASSETS / "icons" / "scan-96.png"
        if icon_p.exists():
            add_image(s, icon_p, 0.85 + (5.5 - 0.9) / 2, 2.05, w=0.9, h=0.9)
    text_box(s, 0.85, 3.10, 5.5, 0.26, "Резидент Сколково",
             size=11, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 3.40, 5.5, 1.15,
             "Узкая задача компьютерного зрения: контроль отёлов телят + ранний сигнал на помощь.\n"
             "Паттерн: узкая ниша + CV + измеримая безопасность животного.",
             size=10, color=DEEP, italic=True, line_spacing=1.25,
             align=PP_ALIGN.CENTER)

    # Right: vapor risk
    ocean_box(s, 6.8, 1.5, 6.0, 3.3, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, 1.65, 5.5, 0.35, "Под вопросом — DeLaval / GEA / Lely",
             size=14, bold=True, color=DEEP)
    text_box(s, 7.05, 2.02, 5.5, 0.24, "Серый статус облачной аналитики",
             size=10.5, italic=True, color=MID)
    text_box(s, 7.05, 2.30, 5.5, 1.35,
             "• Оборудование физически у фермеров\n"
             "• Облачная аналитика зависит от Европы\n"
             "• Прецедент: Climate FieldView 2022 →\n"
             "  Microsoft Azure 2024 (для оборонки)\n"
             "• Лобня 2026 — замещение оборудования\n"
             "  начато (4 млрд ₽), ИИ-стек — отд. трек",
             size=10, color=DEEP, line_spacing=1.3)
    text_box(s, 7.05, 3.70, 5.5, 1.00,
             "F9 — риск «пара»: вендор может отключить ИИ-функционал по решению санкций или лицензий, "
             "не уведомив пользователей заранее.",
             size=10, bold=True, italic=True, color=GOLD, line_spacing=1.25)

    # BOTTOM BAND — хромота КРС: РГАУ-МСХА+АгроЭко (primary) + ЦПС «Объектив»
    # (secondary) + явная дизамбигуация 38 vs 42 точек (chapter-part2.md §3.6).
    _s26b_y = 4.95; _s26b_h = 1.95
    ocean_box(s, 0.6, _s26b_y, 12.18, _s26b_h, fill=SURFACE, stroke=TEAL, stroke_pt=1.3)
    text_box(s, 0.75, _s26b_y + 0.08, 11.9, 0.24,
             "Хромота КРС — две российские CV-системы, разной надёжности",
             size=11, bold=True, color=DEEP)

    ocean_box(s, 0.75, _s26b_y + 0.35, 7.15, 1.10, fill=TEAL_TINT, stroke=TEAL)
    text_box(s, 0.90, _s26b_y + 0.42, 6.85, 0.20,
             "РГАУ-МСХА им. Тимирязева + «АгроЭко» — апробация, Нижний Мамон",
             size=10, bold=True, color=DEEP)
    text_box(s, 0.90, _s26b_y + 0.63, 6.85, 0.18,
             "99% идентификация · 97% точки тела · >96% локомоция",
             size=9.5, color=DARK_GREY)
    text_box(s, 0.90, _s26b_y + 0.82, 6.85, 0.18,
             "42 точки тела vs ≤17 у зарубежных аналогов · 12 000 фото / 449 коров",
             size=9.5, color=DARK_GREY)
    text_box(s, 0.90, _s26b_y + 1.01, 6.85, 0.18,
             "Статус: апробация — не серийное внедрение по хозяйствам",
             size=8.5, italic=True, color=LIGHT)

    ocean_box(s, 8.05, _s26b_y + 0.35, 4.73, 1.10, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 8.20, _s26b_y + 0.42, 4.45, 0.20,
             "ЦПС «Объектив» — вторично, менее надёжно",
             size=9.5, bold=True, color=DEEP)
    text_box(s, 8.20, _s26b_y + 0.63, 4.45, 0.18,
             "Каштановка, 3900 голов",
             size=9, color=DARK_GREY)
    text_box(s, 8.20, _s26b_y + 0.82, 4.45, 0.18,
             "Хромота ×2 за 90 дней; 98% — 1 источник",
             size=9, color=DARK_GREY)

    ocean_box(s, 0.75, _s26b_y + 1.51, 11.95, 0.38, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.90, _s26b_y + 1.51, 11.65, 0.38,
             "Не путать: ЦПС «Объектив» заявляет 38 точек — ДРУГОЕ решение, а не опечатка цифры «42» у Тимирязевки",
             size=9.5, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    _s26_foot = text_runs(s, 0.5, 7.05, 12.33, 0.30, [
        {"text": "Источники: Connectome.ai (Сколково); BUSINESS-stat 2026 Лобня · TAdviser FieldView · "
                  "ТАСС + АгроЭко + Техкульт (Тимирязевка); meatinfo.ru (ЦПС «Объектив») · фото: ",
         "size": 10, "italic": True, "color": LIGHT},
        {"text": "Uberprutser, Wikimedia Commons, CC BY-SA 3.0",
         "size": 10, "italic": True, "color": LIGHT},
    ], anchor=MSO_ANCHOR.MIDDLE)
    _s26_fruns = [r for p in _s26_foot.text_frame.paragraphs for r in p.runs]
    _s26_fruns[-1].font.underline = True
    _s26_fruns[-1].hyperlink.address = "https://commons.wikimedia.org/wiki/File:Newborn_calf.jpg"

    add_speaker_notes(s, load_speaker_notes("s26"))

    # ============ s33 section4 divider — Среда ============
    # issue #340 v3.9: старый Раздел 4 «Агрологистика и товарный трейдинг»
    # (s27 divider + s28 Cargill CMAX + s29 hedge pseudo-flow + s30 Tract/
    # Olam/Walmart×Cropin/Tesco + s31 USDA+Verra + s32 РФ L4) удалён целиком
    # по прямому указанию владельца — трейдинг убран из лекции совсем.
    # Walmart×Cropin перенесён в s08a; USDA Climate-Smart cancellation —
    # в новый s08c (оба теперь в Р1). Старый Р4-bis «Среда» стал Р4;
    # current_section сдвинут 5→4 (один card progress-бара убран).
    # Decorative digit stays plain "4" — "4-bis" as a literal string overflows at 130pt.
    # Title shortened for divider-card legibility (full assertion — в slides/s33-*.md);
    # перечень трёх подтем сохранён («связь / вендор / регуляторика»).
    divider_hero(4, "Инфраструктурные условия: связь, вендор, регуляторика",
        "Сквозной meta-уровень: всё, без чего ни одна ступень не работает.",
        current_section=4,
        caption="3 sub-блока (связь / vendor lock-in двойная оптика / регуляторика) · 3 анти-ИИ критерия (AP5, AP6, AP7)",
        image_filename="p33-john-deere-starfire-gps.jpg",
        image_caption="John Deere 8295R со спутниковым приёмником StarFire на крыше кабины · Wikimedia, CC BY-SA 3.0",
        title_size=20)
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
    # issue #340 round 2 ("фото сплющены"): p34-gps-block.jpg is a square
    # (1280x1280, AR 1.0) GPS-satellite render forced into a w=5.5 h=2.6
    # (AR 2.12) frame, stretching it ~2x wider. Re-cropped (see
    # fix_aspect_ratios.py, bias_y=0.35 to keep the full satellite body/panels
    # and trim mostly from the black space above) to the frame's own AR —
    # no code size change needed, p34-gnss-satellites.png never existed on
    # disk so that branch was always dead code and is removed here.
    ocean_box(s, 0.6, 3.3, 6.0, 3.0)
    p = ASSETS / "photos" / "p34-gps-block-crop.jpg"
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
    # issue #340 round 2 ("фото сплющены"): p30b-melitopol-tractor.jpg is AR
    # 1.78 forced into a w=5.5 h=1.55 (AR 3.55) frame — stretching it ~2x
    # wider than tall. Re-cropped to a gentler AR 2.75 (full tractor + both
    # people stay visible, see fix_aspect_ratios.py) and grew the box height
    # 5.0→5.1 / photo height 1.55→2.0 to match — the other 2 images on this
    # slide (p30b-ftc-deere-tractors.jpg, p30b-dji-agras.png) already matched
    # their own small frames exactly and were left untouched.
    ocean_box(s, 0.6, 1.5, 6.0, 5.1, fill=LIGHT_TINT, stroke=LIGHT)
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
    p = ASSETS / "photos" / "p30b-melitopol-tractor-crop.jpg"
    if p.exists():
        add_image(s, p, 0.85, 4.25, w=5.5, h=2.0)
    text_box(s, 0.85, 6.3, 5.5, 0.25,
             "John Deere в Украине · CNN, 2022-05-01 — ИИ-функция безопасности, успех в этой петле",
             size=9, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Right: control surface optic — real photos (The Register / DJI.com official)
    ocean_box(s, 6.8, 1.5, 6.0, 5.1, fill=GOLD_TINT, stroke=GOLD)
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
    divider_hero(5, "Управление спросом в розничной цепочке",
        "L4 — уровень «полка». Розничный ИИ зрел + пять анти-ИИ критериев + чек-лист + карьерный ландшафт + замыкание к Plenty.",
        current_section=5,
        caption="L4 кратко (Walmart, Tesco, X5, Магнит F&R) + 5 критериев + чек-лист + карьера + closing callback",
        image_filename="p36-supermarket-shelf-aisle.jpg",
        image_caption="Ряд полок супермаркета Intermarché, Квебек-Сити · Wikimedia, CC BY-SA 4.0")
    add_speaker_notes(prs.slides[-1], load_speaker_notes("s36"))

    # ============ s37s L4 retail — hero photo + 2×2 grid (D1 Магнит F&R as 4th card) ============
    # issue #340 v3.9: ladder-ярлык поднялся с L5 на L4 (cargo-ступень убрана).
    # Hero photo relocated from deleted s32 (РФ L4 трейдинг-слайд) — тот же
    # реальный Wikimedia снимок «Перекрёсток» (X5 Group), который эта карточка
    # называет по имени ниже; перекрывает прежний generic unattributed
    # p37s-supermarket-aisle.jpg (без .url-источника).
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L4 — Walmart Eden + Tesco AI + X5 «Перекрёсток» + Магнит F&R (гибрид)",
        size=20, y=0.25)

    # Hero context photo — real "Перекрёсток" (X5 Group) supermarket, СПб
    # issue #340 round 2: this thumbnail frame (w=0.62 h=0.60, AR 1.03) was
    # stretching the AR-1.5 source photo. Re-cropped left-biased (keeps the
    # full "Перекрёсток" signage, which sits on the left two-thirds of the
    # source frame — see fix_aspect_ratios.py) instead of a plain center crop
    # that would have pushed the branding partly out of frame. The 3 other
    # candidate files from earlier rounds (p37s-grocery.jpg,
    # p37s-shopping-cart.jpg, p37s-supermarket-aisle.jpg) are unused by this
    # slide (and unreferenced anywhere else in the deck) — left on disk per
    # brief, not deleted.
    ocean_box(s, 0.6, 1.1, 12.13, 0.75, fill=SURFACE, stroke=LIGHT)
    hero_p = ASSETS / "photos" / "p32-perekrestok-supermarket-spb-crop.jpg"
    if hero_p.exists():
        add_image(s, hero_p, 0.68, 1.15, w=0.62, h=0.60)
    text_box(s, 1.45, 1.17, 11.0, 0.28,
             "L4 — полностью оцифрованная среда: у каждого товара (SKU) есть цифровой след",
             size=11.5, bold=True, color=DEEP)
    text_box(s, 1.45, 1.48, 11.0, 0.34,
             "«Перекрёсток» (X5 Group), Санкт-Петербург — среда, где каждое действие фиксируется в реальном времени",
             size=9.5, italic=True, color=MID, line_spacing=1.15)

    cards = [
        ("Walmart Eden", "ML с 2017",
         "Прогноз скоропортящихся +\nмаршруты свежести на 11 000+ магазинов",
         GOLD),
        ("Tesco AI", "−30% пищевых отходов",
         "С 2017 — ежедневный прогноз\nна ~3500 супермаркетов Великобритании",
         MID),
        ("X5 «Перекрёсток»", "ML с 2020 · 200+ факторов",
         "Российский флагман L4.\nМировой уровень.",
         LIGHT),
        ("Магнит F&R (гибрид)", "Прогноз ✓ · Пополнение — пилот",
         "Прогнозирование на 46 РЦ январь 2026 — в эксплуатации.\nПополнение — пилот на 3 РЦ.",
         TEAL),
    ]
    # 2×2 grid — card_h 2.18→1.90, gap_y 0.13→0.10 (issue #340 Задача 2bis:
    # освобождает ≈0.65" для 5-й плашки «Лента»+КОРУС ниже грида)
    card_w = 6.0; card_h = 1.90; gap_x = 0.18; gap_y = 0.10
    sx = 0.6; sy = 1.95
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
            add_image(s, icon_p, x + 0.2, y + 0.18, w=0.55, h=0.55)
        text_box(s, x + 0.92, y + 0.14, card_w - 1.1, 0.36, name,
                 size=13, bold=True, color=DEEP)
        text_box(s, x + 0.92, y + 0.52, card_w - 1.1, 0.32, kpi,
                 size=11, bold=True, color=color, line_spacing=1.15)
        text_box(s, x + 0.2, y + 0.90, card_w - 0.4, 0.90, desc,
                 size=10, color=DARK_GREY, italic=True, line_spacing=1.25)

    # 5TH PLATE — «Лента» + КОРУС Консалтинг (прогноз спроса, 254 гипермаркета),
    # full-width под 2×2 гридом. chapter-part3.md §6.1 [for-slide-s37x-ru].
    _s37b_y = sy + 2 * card_h + gap_y + 0.08
    _s37b_h = 0.62
    ocean_box(s, 0.6, _s37b_y, 12.13, _s37b_h, fill=TEAL_TINT, stroke=TEAL)
    icon_p = ASSETS / "icons" / "shopping-cart-96.png"
    if icon_p.exists():
        add_image(s, icon_p, 0.72, _s37b_y + 0.09, w=0.44, h=0.44)
    text_box(s, 1.28, _s37b_y + 0.06, 10.6, 0.22,
             "«Лента» + КОРУС Консалтинг — прогноз спроса, 254 гипермаркета, 10 итераций за год",
             size=10.5, bold=True, color=DEEP)
    text_box(s, 1.28, _s37b_y + 0.27, 10.6, 0.20,
             "−4% списаний «гастроном» от базы 2020 · +40% точность к прежней системе · +5% доступность акций · >100 факторов",
             size=9, color=DARK_GREY)
    text_box(s, 1.28, _s37b_y + 0.45, 10.6, 0.16,
             "На Microsoft Azure (запуск до 2022); миграция на отечественное облако не подтверждена ни в одном источнике",
             size=8, italic=True, color=TEAL)

    # Bottom caveat row (compact)
    _s37c_y = _s37b_y + _s37b_h + 0.06
    ocean_box(s, 0.6, _s37c_y, 12.13, 0.40, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, _s37c_y + 0.02, 11.6, 0.35,
             "Оговорка: L4 — розничный ИИ, не агро. Магнит F&R — нюанс «гибрид»: прогноз в промышленной эксплуатации, пополнение — пилот.",
             size=10, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    _s37s_foot = text_runs(s, 0.5, 7.05, 12.33, 0.30, [
        {"text": "Walmart corporate 2025 · Tesco AI annual report · X5 Tech 2024 · Habr Магнит 2026-01 · "
                 "КОРУС Консалтинг + retail-loyalty.org + iot.ru («Лента») · фото: ",
         "size": 11, "italic": True, "color": LIGHT},
        {"text": "Wikimedia Commons, CC BY-SA 2.0",
         "size": 11, "italic": True, "color": LIGHT},
    ], anchor=MSO_ANCHOR.MIDDLE)
    _s37s_fruns = [r for p in _s37s_foot.text_frame.paragraphs for r in p.runs]
    _s37s_fruns[-1].font.underline = True
    _s37s_fruns[-1].hyperlink.address = "https://commons.wikimedia.org/wiki/File:Large_experimental_supermarket_Perekrestok_in_St._Petersburg.jpg"

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
        ("AP4", "Универсальный LLM как советник", "Tzachor: десятки % confident-wrong",
         "ИИ с проверкой источников +\nчеловек в петле"),
        ("AP6", "ИИ-техника = привязка к вендору", "Deere $5 млн + FTC + запрет DJI",
         "Открытые стандарты / мульти-вендор"),
        ("AP7", "AI-MRV без прямых измерений", "USDA Climate-Smart отменён: $3,1 млрд",
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
    # issue #340 v3.9: прежняя 5-колоночная раскладка (L1/L2/L3/L4-cargo/
    # L5-полка) слила трейдинг-колонку (Cargill CMAX/Tract/Olam/ADM) с
    # retail-колонкой — теперь 4 колонки, L4 = полка (ladder relabel).
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Карьерный ландшафт — L1-L4 сегменты + российский рынок",
        size=24)

    segments = [
        ("L1 Поле", "John Deere · Bayer · BASF\nClimate · Taranis · Granular",
         "Cognitive Pilot · ИТЭЛМА\nЭФКО · Геоскан · ExactFarming", LIGHT),
        ("L2 Робот", "Carbon Robotics · Saga · Tevel\nAGCO · Aigen", "(точечные RU стартапы)", MID),
        ("L3 Животное", "DeLaval · GEA · Lely\nCargill Birdoo · Allflex", "Connectome.ai · Сколково", LIGHT),
        ("L4 Полка", "Walmart Eden · Tesco AI\nWooliesX · Carrefour AI", "X5 Tech · Магнит digital\n«Лента»+КОРУС (мировой уровень)", GOLD),
    ]
    seg_w = 3.0; seg_h = 4.7; gap = 0.14
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

    # Number-refrain (сквозная линия лекции) — issue #340 v3.9: прежний точный
    # счёт "18 из 45" включал как минимум один кейс из удалённого Раздела 4
    # (Verra); пересчёт по всей деке не делался в этом круге (CLAUDE.md:
    # "структурный разрез без сплошного прохода по счётчикам" — отдельный
    # проход, не угадывание), поэтому плашка заменена на качественное
    # наблюдение без сконструированного числа.
    ocean_box(s, 0.6, 6.30, 12.13, 0.32, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.6, 6.30, 12.13, 0.32,
             "Не каждый случай этой лекции, где называли «ИИ», решающим оказался именно ИИ",
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
        ("Агентный ИИ", "Где ещё агентный ИИ работает\nв инженерных задачах с быстрой обратной связью?"),
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
