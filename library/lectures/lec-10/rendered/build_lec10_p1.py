"""
Part 1: s01-s14 — Раздел 0 (Открытие) + L1 «Поле».
14 слайдов: hook + cover + lecture-map + glossary + keystone + Р1 divider + 8 content.
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
        "AI-управляемая ферма обещала революцию. 19 месяцев — и закрылась.",
        size=24)

    # LEFT panel — открытие май 2023 (use vertical-farm interior photo)
    ocean_box(s, 0.6, 1.7, 5.95, 4.0)
    photo_p = ASSETS / "photos" / "p10-vertical-farm.jpg"
    if photo_p.exists():
        add_image(s, photo_p, 0.85, 1.95, w=5.45, h=3.5)
    text_box(s, 0.85, 5.5, 5.45, 0.3, "май 2023 · Plenty Compton открытие",
             size=12, italic=True, bold=True, color=MID,
             align=PP_ALIGN.CENTER)

    # RIGHT panel — закрытие декабрь 2024 (use chart of valuation collapse)
    ocean_box(s, 6.8, 1.7, 5.95, 4.0)
    chart_p = ASSETS / "charts" / "c01-plenty-collapse.png"
    if chart_p.exists():
        add_image(s, chart_p, 7.0, 1.85, w=5.6, h=3.4)
    text_box(s, 7.0, 5.5, 5.6, 0.3, "декабрь 2024 · закрытие · Ch. 11 март 2025",
             size=12, italic=True, bold=True, color=GOLD,
             align=PP_ALIGN.CENTER)

    # Bottom data strip — 3 mega-numbers
    ocean_box(s, 0.6, 5.95, 12.13, 0.9, fill=GOLD_TINT, stroke=GOLD)
    text_runs(s, 0.8, 6.05, 3.8, 0.8, [
        {"text": "$940M", "size": 26, "bold": True, "color": GOLD},
        {"newpara": True, "text": "потерь капитала",
         "size": 11, "italic": True, "color": DEEP},
    ], align=PP_ALIGN.CENTER)
    text_runs(s, 4.7, 6.05, 3.9, 0.8, [
        {"text": "$1,9 млрд → <$15M", "size": 22, "bold": True, "color": DEEP},
        {"newpara": True, "text": "коллапс оценки –99% за 3 года",
         "size": 11, "italic": True, "color": MID},
    ], align=PP_ALIGN.CENTER)
    text_runs(s, 8.7, 6.05, 3.9, 0.8, [
        {"text": "19 месяцев", "size": 26, "bold": True, "color": GOLD},
        {"newpara": True, "text": "от открытия до закрытия",
         "size": 11, "italic": True, "color": DEEP},
    ], align=PP_ALIGN.CENTER)

    add_footer(s, "Источники: Plenty press май 2023; TechCrunch 2025-03-24; Bloomberg Law 2025")
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
             "Лекция 10 · AI в инженерных задачах · 3 курс",
             size=18, italic=True, color=MID)

    # Title
    text_box(s, 6.0, 2.3, 6.8, 3.0,
             "AI в сельском хозяйстве",
             size=44, bold=True, color=DEEP, line_spacing=1.15)

    # Subtitle / scope
    text_box(s, 6.0, 4.5, 6.8, 1.2,
             "От поля к полке: пять уровней лестницы\nи пять анти-ИИ критериев",
             size=20, italic=True, color=LIGHT, line_spacing=1.3)

    # Duration
    text_box(s, 6.0, 6.0, 6.8, 0.5, "75 минут · Q&A",
             size=18, italic=True, color=LIGHT)

    # Decorative icon
    icon_p = ASSETS / "icons" / "sprout-96.png"
    if icon_p.exists():
        add_image(s, icon_p, 11.7, 6.4, w=0.85, h=0.85)

    add_speaker_notes(s,
        "Это титульный слайд десятой лекции — седьмой отраслевой главы курса. "
        "АПК — одна из тех областей, где ИИ обещает революцию каждые два-три "
        "года, и каждый раз новое поколение vendor'ов утверждает, что вот сейчас "
        "точно получится. К две тысячи двадцать шестому году мы накопили "
        "достаточно успехов и достаточно провалов, чтобы построить чёткий "
        "инженерный аппарат различения. Тон лекции — trust-but-verify: ни "
        "евангелизм, ни диссидентство. Мы разберём пять уровней лестницы AI в "
        "АПК — от открытого поля до supermarket-полки — назовём по имени "
        "каждое работающее решение и каждый провал, и в финале сформулируем "
        "пять анти-ИИ критериев, которые операционно отвечают на вопрос «когда "
        "не AI».")
    return s


def build_remaining_p1(prs, H):
    """Continue with s03-s14."""
    DEEP, MID, LIGHT, TEAL = H["DEEP"], H["MID"], H["LIGHT"], H["TEAL"]
    SURFACE, WHITE, GOLD = H["SURFACE"], H["WHITE"], H["GOLD"]
    COVER_OUTLINE, GOLD_TINT, TEAL_TINT, LIGHT_TINT = H["COVER_OUTLINE"], H["GOLD_TINT"], H["TEAL_TINT"], H["LIGHT_TINT"]
    SOFT_GREY, DARK_GREY = H["SOFT_GREY"], H["DARK_GREY"]
    ASSETS = H["ASSETS"]
    MSO_SHAPE, MSO_ANCHOR, PP_ALIGN = H["MSO_SHAPE"], H["MSO_ANCHOR"], H["PP_ALIGN"]
    Inches, Pt = H["Inches"], H["Pt"]
    blank, set_slide_bg, text_box, text_runs = H["blank"], H["set_slide_bg"], H["text_box"], H["text_runs"]
    ocean_box, filled_rect, hr_line, add_arrow = H["ocean_box"], H["filled_rect"], H["hr_line"], H["add_arrow"]
    add_image, add_speaker_notes, add_progress_bar = H["add_image"], H["add_speaker_notes"], H["add_progress_bar"]
    add_footer, add_assertion_title = H["add_footer"], H["add_assertion_title"]
    load_speaker_notes, section_divider = H["load_speaker_notes"], H["section_divider"]
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
    add_assertion_title(s, "Карта лекции — лестница пяти уровней от поля к полке", size=26)

    # 7 horizontal cards
    cards = [
        ("0. Открытие", "Hook + keystone + глоссарий", ""),
        ("1. L1 Поле", "Открытая биология", "14 мин"),
        ("2. L2 Робот", "Specialization > generic", "15 мин"),
        ("3. L3 Животное", "Semi-closed indiv.-level", "12 мин"),
        ("4. L4 Цепочка", "Агентный ИИ лидер", "10 мин"),
        ("4-bis. Среда", "Связь · lock-in · регуляторика", "8 мин"),
        ("5. L5 Полка", "+ 5 критериев + payoff", "6 мин"),
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
                     size=11, italic=True, color=GOLD, bold=True,
                     align=PP_ALIGN.CENTER)

    # Central question banner
    ocean_box(s, 0.6, 5.0, 12.13, 1.6, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 5.08, 11.63, 0.4,
             "Центральный вопрос лекции:",
             size=14, italic=True, color=DARK_GREY, bold=True)
    text_box(s, 0.85, 5.5, 11.63, 1.0,
             "Где на лестнице L1→L5 ИИ работает, где ломается — и какой класс\n"
             "решения / альтернатива применимы на каждой ступени?",
             size=18, italic=True, color=DEEP, line_spacing=1.3)

    add_speaker_notes(s, load_speaker_notes("s03"))

    # ============ s04 glossary mini ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Два режима ИИ и пять L4-терминов — единый язык лекции", size=24)

    # LEFT: closed-loop vs open-environment
    text_box(s, 0.6, 1.5, 5.95, 0.4, "Среда применения ИИ",
             size=16, bold=True, color=MID)
    ocean_box(s, 0.6, 2.0, 5.95, 2.0, fill=TEAL_TINT, stroke=TEAL)
    text_box(s, 0.85, 2.15, 5.45, 0.4, "Замкнутый контур (closed-loop)",
             size=18, bold=True, color=DEEP)
    text_box(s, 0.85, 2.55, 5.45, 1.4,
             "Контролируемая среда (теплица, фабрика, склад). "
             "Все переменные измеряются. ИИ оптимизирует параметры. "
             "Промышленное применение зрелое.",
             size=12, color=DARK_GREY, italic=True, line_spacing=1.3)

    ocean_box(s, 0.6, 4.1, 5.95, 2.0)
    text_box(s, 0.85, 4.25, 5.45, 0.4, "Открытая среда (open-environment)",
             size=18, bold=True, color=DEEP)
    text_box(s, 0.85, 4.65, 5.45, 1.4,
             "Открытая биологическая среда (поле, луг). "
             "Погода, переменное освещение, пыль, тени. ИИ работает в узких задачах. "
             "Универсальная «autonomous farm» — банкротится.",
             size=12, color=DARK_GREY, italic=True, line_spacing=1.3)

    # RIGHT: 5 L4 terms
    text_box(s, 6.85, 1.5, 5.95, 0.4, "5 терминов цепочки поставок",
             size=16, bold=True, color=MID)
    terms = [
        ("Агентный ИИ", "ML + RAG + конвейер действий с человеком в петле"),
        ("bp (basis points)", "1 bp = 0,01%. Метрика проскальзывания сделок"),
        ("Проскальзывание сделки", "Разрыв между планом сделки и фактом исполнения"),
        ("Scope-3 выбросы", "Косвенные выбросы по цепочке поставок"),
        ("AI-MRV", "ИИ-мониторинг, отчёт, верификация — климат-учёт"),
    ]
    term_y = 2.0
    for i, (term, defn) in enumerate(terms):
        ocean_box(s, 6.85, term_y, 5.95, 0.8, fill=LIGHT_TINT)
        text_box(s, 7.05, term_y + 0.08, 1.95, 0.4, term,
                 size=12, bold=True, color=DEEP)
        text_box(s, 9.0, term_y + 0.08, 3.7, 0.6, defn,
                 size=10, color=MID, italic=True, line_spacing=1.25)
        term_y += 0.85

    add_speaker_notes(s, load_speaker_notes("s04"))

    # ============ s05 keystone ladder ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Лестница ИИ — пять уровней. На каждой ступени работает по-разному", size=22)

    # 5 ladder steps stacked vertically — larger boxes
    levels = [
        ("L5", "Полка / магазин", "Полностью оцифрованная среда. ИИ зрел.",
         "Walmart Eden 2017+, Tesco 2017+, X5 2020+", GOLD),
        ("L4", "Цепочка поставок", "Контролируемые грузопотоки + быстрая обратная связь",
         "Cargill CMAX, Tract, Olam, Walmart×Cropin", TEAL),
        ("L3", "Животное", "Полузакрытая среда + измерения на уровне особи",
         "SenseHub 2M коров, CattleEye, DeLaval V310", LIGHT),
        ("L2", "Робот", "Специализация работает; универсальный — банкротится",
         "LaserWeeder G2, Saga UV-C, Tevel · против Monarch/FarmWise", MID),
        ("L1", "Поле", "Открытая биология — самая трудная",
         "See & Spray работает · Plenty/AppHarvest/Bowery провалились", DEEP),
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
    text_box(s, 10.5, 1.7, 2.0, 0.4, "↑ движение по лестнице",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.2)
    arrows_text = [
        ("↑ контролируемость", "среды растёт"),
        ("↑ измеримая отдача", "ROI растёт"),
        ("↑ предсказуемость", "результата растёт"),
        ("↓ биология", "неопределённость падает"),
    ]
    ay = 2.25
    for hdr, dsc in arrows_text:
        text_box(s, 10.4, ay, 2.2, 0.3, hdr, size=12, bold=True, color=GOLD)
        text_box(s, 10.4, ay + 0.3, 2.2, 0.5, dsc,
                 size=9, color=DARK_GREY, italic=True, line_spacing=1.2)
        ay += 0.95

    add_footer(s, "Несущая ось всей лекции · L11 кибер-физическое производство — следующая")
    add_speaker_notes(s, load_speaker_notes("s05"))

    # ============ s06 section1 divider — L1 Поле ============
    section_divider(prs, 1, "Раздел 1 — L1 «Поле»",
        "Открытая биологическая среда: где ИИ работает узко — и где ломается даже здесь",
        current_section=1,
        caption="14 минут · 5 рабочих кейсов · 3 провала · разбираем по строгим критериям")
    s_last = prs.slides[-1]
    add_speaker_notes(s_last, load_speaker_notes("s06"))

    # ============ s07 See & Spray ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "See & Spray Ultimate — каноничный успех L1", size=24)

    # Left photo
    ocean_box(s, 0.6, 1.6, 7.4, 4.5)
    p = ASSETS / "photos" / "p07-john-deere-sprayer.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.85, w=6.9, h=4.0)
    text_box(s, 0.85, 5.85, 6.9, 0.25, "John Deere ExactApply + See & Spray Ultimate · ноябрь 2025",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Right data cards
    cards = [
        ("5M акров", "сезон 2025", "> штат Нью-Джерси", GOLD),
        ("–50%", "контактных гербицидов", "~31 млн галлонов / сезон", MID),
        ("+2,0 бушеля", "сои с акра", "лучшие случаи до 4,8", LIGHT),
    ]
    cy = 1.6
    for big, lbl, sub, color in cards:
        ocean_box(s, 8.2, cy, 4.55, 1.2, fill=LIGHT_TINT if color != GOLD else GOLD_TINT)
        text_box(s, 8.4, cy + 0.1, 2.4, 0.5, big, size=22, bold=True, color=color)
        text_box(s, 8.4, cy + 0.6, 2.4, 0.4, lbl, size=12, color=DEEP, italic=True)
        text_box(s, 10.9, cy + 0.3, 1.7, 0.7, sub,
                 size=10, color=MID, italic=True, align=PP_ALIGN.RIGHT, line_spacing=1.2)
        cy += 1.3

    # Spec card
    ocean_box(s, 8.2, 5.5, 4.55, 0.7, fill=SURFACE)
    text_box(s, 8.4, 5.6, 4.25, 0.5,
             "36 камер · нейросеть на 40 млн изображений · NVIDIA Jetson на устройстве · <50 мс",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.3)

    add_footer(s, "Источники: AgTechNavigator 2025-11-10; пресс-релиз John Deere ноябрь 2025; GrowIWM 2024")
    add_speaker_notes(s, load_speaker_notes("s07"))

    # ============ s08 vendor matrix L1 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Платформы L1 — пять вендоров, разные режимы. Бренд ≠ режим работы",
        size=22)

    # 5×4 matrix
    headers = ["Платформа", "География", "Режим работы", "Бизнес-модель"]
    rows = [
        ("BASF xarvio", "ЕС, Япония (рис)", "Подписка + советы", "Оплата за акр"),
        ("Climate FieldView", "США (вышел из РФ 2022)", "Хранилище данных", "250 млн акров подписок"),
        ("Syngenta Cropwise", "Глобально", "Интеграция Bayer Forward", "В составе пакета"),
        ("Granular (Corteva)", "США", "Управление хозяйством", "Облачный сервис"),
        ("Taranis", "Глобально", "Компьютерное зрение + дроны", "Оплата за акр"),
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

    # Sidebar callout: BASF Japan rice
    ocean_box(s, 0.6, 5.5, 12.13, 1.2, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 5.6, 11.5, 0.4,
             "BASF xarvio в Японии — гарантия урожайности риса · октябрь 2025 (пресс-релиз p-25-191)",
             size=12, bold=True, color=DEEP)
    text_box(s, 0.85, 6.0, 11.5, 0.65,
             "Первый случай гарантированной урожайности под ИИ-советы: BASF выплачивает компенсацию "
             "при недоборе урожая. Закрытый контур данных + страховой механизм = единственный известный к 2026 году пример.",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.3)

    add_footer(s, "Источник: пресс-релиз BASF p-25-191 октябрь 2025 · TAdviser FieldView 2022")
    add_speaker_notes(s, load_speaker_notes("s08"))

    # ============ s09 foundation models ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Базовые модели 2026 — TerraMind и Prithvi-EO 2.0 меняют порог входа",
        size=22)

    # Left: Sentinel-2 imagery
    ocean_box(s, 0.6, 1.6, 6.3, 4.7)
    p = ASSETS / "photos" / "p09-sentinel-brazil.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.85, w=5.8, h=4.2)
    text_box(s, 0.85, 6.1, 5.8, 0.25,
             "Sentinel-2 / Copernicus (ESA, CC-BY-SA): класс данных для TerraMind",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Right: foundation-model architecture stack
    text_box(s, 7.2, 1.6, 5.6, 0.5, "Архитектура: базовая модель + поиск (RAG)",
             size=16, bold=True, color=MID)

    stack = [
        ("4. Поиск релевантных данных", "под специфику хозяйства", LIGHT_TINT, LIGHT),
        ("3. Дообучение (~1 000 изобр.)", "под культуру/регион", LIGHT_TINT, LIGHT),
        ("2. TerraMind / Prithvi", "предобученные IBM-NASA / ESA", GOLD_TINT, GOLD),
        ("1. Sentinel-2 мультиспектр", "10 м разрешение, 12 каналов", LIGHT_TINT, LIGHT),
    ]
    sy = 2.15
    for label, sub, fill, stroke in stack:
        ocean_box(s, 7.2, sy, 5.6, 0.85, fill=fill, stroke=stroke)
        text_box(s, 7.4, sy + 0.1, 5.2, 0.35, label,
                 size=13, bold=True, color=DEEP)
        text_box(s, 7.4, sy + 0.45, 5.2, 0.35, sub,
                 size=10, color=MID, italic=True)
        sy += 0.95

    # Bottom risk callout
    ocean_box(s, 0.6, 6.4, 12.13, 0.5, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.8, 6.45, 11.8, 0.4,
             "⚠ Концентрация у вендоров: вся индустрия L1 строится на 2-3 моделях IBM / NASA / ESA",
             size=12, bold=True, color=GOLD,
             anchor=MSO_ANCHOR.MIDDLE)

    add_speaker_notes(s, load_speaker_notes("s09"))

    # ============ s10 vertical farming collapse ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Вертикальные фермы — провал не из-за плохого ИИ. AppHarvest, Plenty, Bowery",
        size=22)

    # Top: chart
    ocean_box(s, 0.6, 1.5, 6.3, 4.0)
    c = ASSETS / "charts" / "c10-vf-losses.png"
    if c.exists():
        add_image(s, c, 0.85, 1.7, w=5.8, h=3.7)

    # Right: 3 cards
    cards = [
        ("AppHarvest", "Тепличный, нерентабельный 2023", "$600 млн потерь"),
        ("Plenty", "Compton ИИ-фабрика 19 мес → банкротство", "$940 млн, –99% оценки"),
        ("Bowery", "Коллапс перед IPO, ноябрь 2024", "$672 млн потерь"),
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
             "$1,37 млрд+ потерь, 14 банкротств 2025. Не сработала арифметика энергии.",
             size=14, bold=True, color=DEEP)
    text_box(s, 0.85, 6.2, 11.6, 0.45,
             "Контроллеры микроклимата работали. Компьютерное зрение распознавало. Модель предсказывала. LED ≈ 100× энергии солнца — AP1 термодинамика > ИИ.",
             size=12, color=DARK_GREY, italic=True, line_spacing=1.3)

    add_footer(s, "Источники: TechCrunch 2025-03-24, 2024-11-04 (Bowery); Agriculture Dive 689039 (AppHarvest)")
    add_speaker_notes(s, load_speaker_notes("s10"))

    # ============ s11 5-Why thermodynamics ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Пять «почему» — почему ИИ не закрыл термодинамический разрыв",
        size=24)

    # Chain of 5 steps with arrows
    steps = [
        ("1. Почему\nзакрылась?", "Капитал\nкончился", MID),
        ("2. Почему\nкапитал?", "Юнит-эконом.\nне работает", MID),
        ("3. Почему\nне работает?", "Стоимость\nLED-энергии\n100× солнца", GOLD),
        ("4. Почему\n100×?", "Закон\nтермодинамики", DEEP),
        ("5. Может\nИИ закрыть?", "Нет:\nэффект 5-15%\nпри разрыве 100×", GOLD),
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

    # Bottom takeaway
    ocean_box(s, 0.6, 4.6, 12.13, 1.9, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 4.75, 11.6, 0.5,
             "Корневая причина: разрыв в два порядка. Никакая модель не закроет.",
             size=18, bold=True, color=DEEP)
    text_box(s, 0.85, 5.3, 11.6, 0.45,
             "0,5 (солнце→LED) × 0,7 (LED→растение) × 0,3 (растение→выход) ≈ 10,5% от начала до конца. "
             "ИИ оптимизирует знаменатель (5-15%); разрыв в числителе.",
             size=12, color=DARK_GREY, italic=True, line_spacing=1.3)
    text_box(s, 0.85, 5.8, 11.6, 0.6,
             "AP1 в строгой форме: «когда ИИ оптимизирует неверно сформулированную целевую функцию — лучше не ИИ».",
             size=12, bold=True, italic=True, color=GOLD, line_spacing=1.3)

    add_footer(s, "Анализ Hannah Ritchie · журнал MDPI Sustainability, 2024")
    add_speaker_notes(s, load_speaker_notes("s11"))

    # ============ s12 ChatGPT hallucinations ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "ChatGPT и Bard как агроном — «уверенно ошибочны» в десятках процентов",
        size=22)

    # Left: study summary
    ocean_box(s, 0.6, 1.5, 6.0, 5.0)
    text_box(s, 0.85, 1.65, 5.5, 0.5,
             "Tzachor et al., Nature Food, май 2024",
             size=14, bold=True, color=DEEP)
    text_box(s, 0.85, 2.15, 5.5, 0.4,
             "Reichman University · 184 вопроса о пестицидах",
             size=11, italic=True, color=MID)
    hr_line(s, 0.85, 2.6, 5.3, color=LIGHT, weight=1.0)

    results = [
        ("GPT-3.5", "32%", "правильно"),
        ("GPT-4", "44%", "правильно"),
        ("Bard", "29%", "правильно"),
    ]
    ry = 2.85
    for model, pct, lbl in results:
        text_box(s, 1.0, ry, 1.8, 0.4, model, size=13, bold=True, color=DEEP)
        text_box(s, 2.8, ry, 1.5, 0.4, pct, size=18, bold=True, color=GOLD)
        text_box(s, 4.3, ry, 2.0, 0.4, lbl, size=11, italic=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
        ry += 0.55

    text_box(s, 0.85, 4.7, 5.5, 1.6,
             "Остальные 56-71% ответов — уверенно неверны: модель не «не знает», "
             "а выдаёт уверенный ответ с неверной дозировкой / неподходящим препаратом. "
             "Режим отказа — не «модель плохая», а «применение не в её режиме».",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.4)

    # Right: Anti-pattern AP4 + alternative
    ocean_box(s, 6.8, 1.5, 5.95, 5.0, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 7.05, 1.65, 5.5, 0.5,
             "AP4 — категорический анти-паттерн",
             size=14, bold=True, color=GOLD)
    text_box(s, 7.05, 2.15, 5.5, 0.8,
             "Обобщённый LLM в роли советника-агронома —\n"
             "категорически неприменим. Не «надо доработать»; это другой класс задач.",
             size=12, color=DEEP, italic=True, line_spacing=1.3)

    hr_line(s, 7.05, 3.05, 5.4, color=GOLD, weight=1.5)
    text_box(s, 7.05, 3.2, 5.5, 0.4,
             "Альтернатива: ИИ с проверкой источников (RAG)",
             size=14, bold=True, color=DEEP)
    alts = [
        "Ограниченная база знаний хозяйства",
        "Поиск + цитата источника",
        "Откалиброванная уверенность: «не знаю» когда не знает",
        "След проверки для каждой рекомендации",
    ]
    ay = 3.65
    for a in alts:
        text_box(s, 7.25, ay, 5.3, 0.45, "• " + a,
                 size=11, color=DEEP, line_spacing=1.3)
        ay += 0.45

    text_box(s, 7.05, 5.65, 5.5, 0.6,
             "+ человек в петле: финальную рекомендацию подтверждает агроном",
             size=11, bold=True, italic=True, color=GOLD, line_spacing=1.3)

    add_footer(s, "Источник: Tzachor et al., Nature Food, май 2024; Phys.org 2024-05")
    add_speaker_notes(s, load_speaker_notes("s12"))

    # ============ s13 Plantix ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Plantix — 10-15% ошибочной диагностики × 10 млн+ загрузок = ~100 тыс. неверных рекомендаций / год",
        size=18)

    # Left: stylized phone UI mock-up + stats
    ocean_box(s, 0.6, 1.6, 5.5, 5.0)
    # Phone frame outline
    text_box(s, 0.85, 1.8, 5.0, 0.4, "Plantix · мобильное приложение",
             size=14, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, 0.85, 2.2, 5.0, 0.4, "10+ миллионов загрузок",
             size=11, italic=True, color=MID, align=PP_ALIGN.CENTER)
    # Fake phone screen
    ocean_box(s, 1.8, 2.7, 3.1, 3.5, fill=DEEP, stroke=DEEP)
    text_box(s, 1.95, 2.85, 2.8, 0.4, "[ камера ]",
             size=11, italic=True, color=WHITE, align=PP_ALIGN.CENTER)
    ocean_box(s, 1.95, 3.3, 2.8, 1.5, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 2.05, 3.4, 2.6, 1.3,
             "Фото листа\nсоевой\n— анализ —",
             size=11, italic=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.3,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 1.95, 4.9, 2.8, 0.45,
             "Диагноз:\nантракноз",
             size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, line_spacing=1.2)
    text_box(s, 1.95, 5.5, 2.8, 0.45,
             "Уверенность: 87%",
             size=10, italic=True, color=GOLD, align=PP_ALIGN.CENTER)

    # Right: breakdown
    ocean_box(s, 6.4, 1.6, 6.4, 2.4)
    text_box(s, 6.65, 1.75, 6.0, 0.5, "Чем плохо «85-90% точности»",
             size=15, bold=True, color=DEEP)
    text_box(s, 6.65, 2.25, 6.0, 1.7,
             "• Самооценка вендора (нет независимого аудита)\n"
             "• 10-15% ошибочной диагностики = 1-1,5 млн ошибок / год\n"
             "• Дозо-критичные ошибки (другой препарат)\n"
             "• Хроническое допущение ложных срабатываний в советнике",
             size=11, color=DARK_GREY, line_spacing=1.5)

    ocean_box(s, 6.4, 4.15, 6.4, 2.45, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 6.65, 4.3, 6.0, 0.5, "AP3 + альтернатива",
             size=15, bold=True, color=GOLD)
    text_box(s, 6.65, 4.85, 6.0, 1.7,
             "AP3: пороговая точность ≠ готовность к внедрению.\n"
             "Альтернатива — откалиброванная уверенность + отказ:\n"
             "  • выдавать только при ≥90% уверенности,\n"
             "  • иначе — «направить к специалисту»,\n"
             "  • + разделение по критичности дозы.",
             size=11, color=DEEP, italic=True, line_spacing=1.4)

    add_footer(s, "Plantix.net (интерфейс); данные Frontiers in Plant Science 2020 + самоотчёт Plantix")
    add_speaker_notes(s, load_speaker_notes("s13"))

    # ============ s14 РФ context L1 ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L1 в РФ — ExactFarming и Прогресс Агро при индексе цифровизации 27,2",
        size=22)

    # Left: chart
    ocean_box(s, 0.6, 1.5, 6.0, 4.5)
    c = ASSETS / "charts" / "c14-rus-digi.png"
    if c.exists():
        add_image(s, c, 0.85, 1.7, w=5.5, h=4.1)

    # Right: 2 cards working + 1 caveat
    cards = [
        ("ExactFarming", "12 700 хозяйств · 9,8 млн га", "Управление полями + мониторинг", MID),
        ("ГК «Прогресс Агро»", "+5% рентабельности", "Внутренний замер 2024", LIGHT),
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
             "AP6 — Climate FieldView вышел из РФ в 2022",
             size=13, bold=True, color=GOLD)
    text_box(s, 0.85, 6.55, 11.6, 0.3,
             "Политический риск L1: облачные сервисы с зарубежной зависимостью могут отключиться по решению вендора или санкций.",
             size=10, color=DARK_GREY, italic=True, line_spacing=1.3)

    add_footer(s, "Источники: Яков и Партнёры 2024 · ExactFarming.com · TAdviser 2022")
    add_speaker_notes(s, load_speaker_notes("s14"))

    return prs
