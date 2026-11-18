"""
Part 1: s01-s14 (+ s05a/s05b/s05c/s07c, issue #340) — Раздел 0 (Открытие) + L1 «Поле».
21 слайд: hook + cover + lecture-map + glossary + keystone + 2 обзора отрасли
(цикл «от поля к полке» + четыре силы, Задача 1) + ретроспектива отрасли по
годам (s05c, owner follow-up — коллапс инвестиций −91% YoY + рост цены
консолидации ×~13, честный контраст с «прорывами как в космосе») + Р1 divider
с реальным фото (Задача 2) + 8 content + See & Spray разведён на инженерию
(s07a) и ИИ-модель (s07c, Задача 3).
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

    # ============== s01 hook — Plenty Compton, 2 настоящих фото открытия ==============
    # K-2 fix: оба фото теперь РЕАЛЬНЫЕ Compton-specific (2urbangirls.com, май 2023),
    # не родовое фото вертикальной фермы + не chart, подменявший "AFTER"-кадр.
    # Честного фото закрытия (дек 2024) не найдено за разумный поиск — см.
    # iteration-log-part2.md. Суммарная площадь фото ≥40% (hero-норматив).
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "ИИ-управляемая ферма обещала революцию. 19 месяцев — и закрылась.",
        size=24)

    # LEFT panel (hero) — мэр Комптона Эмма Шариф на церемонии открытия, май 2023
    # Photo AR = 1.5068 (pre-cropped to this ratio) -> w=5.80,h=3.85 preserves AR exactly
    ocean_box(s, 0.6, 1.5, 5.95, 4.4)
    photo_p = ASSETS / "photos" / "p01-plenty-ribboncutting-mayor.jpg"
    if photo_p.exists():
        add_image(s, photo_p, 0.675, 1.63, w=5.80, h=3.85)
    text_box(s, 0.68, 5.53, 5.8, 0.3, "Май 2023 · мэр Комптона Эмма Шариф на церемонии открытия",
             size=10.5, italic=True, bold=True, color=MID,
             align=PP_ALIGN.CENTER, line_spacing=1.05)

    # RIGHT panel — интерьер объекта, та же церемония, май 2023
    # Photo AR = 1.3375 (pre-cropped) -> w=5.15,h=3.85 preserves AR exactly
    ocean_box(s, 6.8, 1.5, 5.95, 4.4)
    photo_p2 = ASSETS / "photos" / "p01-plenty-compton-interior.jpg"
    if photo_p2.exists():
        add_image(s, photo_p2, 7.2, 1.63, w=5.15, h=3.85)
    text_box(s, 6.98, 5.53, 5.49, 0.3, "Май 2023 · интерьер объекта — «История фермерства в Комптоне»",
             size=10.5, italic=True, bold=True, color=MID,
             align=PP_ALIGN.CENTER, line_spacing=1.05)

    # Bottom data strip — 3 mega-numbers (закрытие дек.2024 несёт ТЕКСТ, т.к. честного фото нет)
    ocean_box(s, 0.6, 6.0, 12.13, 0.85, fill=GOLD_TINT, stroke=GOLD)
    text_runs(s, 0.8, 6.08, 3.8, 0.75, [
        {"text": "$940M", "size": 24, "bold": True, "color": GOLD},
        {"newpara": True, "text": "потерь капитала",
         "size": 10.5, "italic": True, "color": DEEP},
    ], align=PP_ALIGN.CENTER)
    text_runs(s, 4.7, 6.08, 3.9, 0.75, [
        {"text": "$1,9 млрд → <$15M", "size": 20, "bold": True, "color": DEEP},
        {"newpara": True, "text": "коллапс оценки –99% за 3 года",
         "size": 10.5, "italic": True, "color": MID},
    ], align=PP_ALIGN.CENTER)
    text_runs(s, 8.7, 6.08, 3.9, 0.75, [
        {"text": "19 месяцев", "size": 24, "bold": True, "color": GOLD},
        {"newpara": True, "text": "от открытия (май 2023) до закрытия (декабрь 2024)",
         "size": 10.5, "italic": True, "color": DEEP},
    ], align=PP_ALIGN.CENTER)

    add_footer(s, "Источники фото: 2urbangirls.com, май 2023. Источники цифр: Plenty press май 2023; "
                  "TechCrunch 2025-03-24; Bloomberg Law 2025")
    add_speaker_notes(s, load_speaker_notes("s01"))

    # ============== s02 cover ==============
    # Issue #340 visual-richness pass (owner: intro — только диаграммы/иконки,
    # без крупных реальных фото). Hero photo заменяет абстрактную декоративную
    # «10» (Lec-9 hero_cover precedent, deckkit cover(): фото + gold accent bar,
    # БЕЗ decorative lecture-number, когда есть реальное фото) — 6-tier Tier 2
    # (Wikimedia Commons), ~39% площади кадра.
    s = blank(prs); set_slide_bg(s, WHITE)

    hero_p = ASSETS / "photos" / "p02-cover-drone-strawberry-field.jpg"
    if hero_p.exists():
        add_image(s, hero_p, 0.5, 0.6, w=5.9, h=6.3)
    else:
        # Fallback — ТОЛЬКО если источник отсутствует (не mock, честный gap):
        # прежняя декоративная «10» на случай отсутствия файла при сборке.
        text_box(s, 0.0, 0.5, 6.5, 7.0, "10",
                 size=400, bold=True, color=COVER_OUTLINE,
                 align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE,
                 font=H["FONT_HEAD"], line_spacing=0.9)

    # Meta top right
    text_box(s, 6.0, 1.5, 6.8, 0.5,
             "Лекция 10 · ИИ в сельском хозяйстве · 3 курс",
             size=18, italic=True, color=MID)

    # Title
    text_box(s, 6.0, 2.3, 6.8, 3.0,
             "ИИ в сельском хозяйстве",
             size=44, bold=True, color=DEEP, line_spacing=1.15)

    # Subtitle / scope
    text_box(s, 6.0, 4.5, 6.8, 1.2,
             "От поля к полке: пять уровней лестницы\nи пять анти-ИИ критериев",
             size=20, italic=True, color=LIGHT, line_spacing=1.3)

    # Gold accent bar — repeated-element consistency with Lec-9 hero_cover
    filled_rect(s, 6.0, 5.78, 1.6, 0.07, GOLD)

    # Duration
    text_box(s, 6.0, 6.0, 6.8, 0.5, "вопросы и ответы в конце",
             size=18, italic=True, color=LIGHT)

    # Decorative icon
    icon_p = ASSETS / "icons" / "sprout-96.png"
    if icon_p.exists():
        add_image(s, icon_p, 11.7, 6.4, w=0.85, h=0.85)

    # Photo provenance — real hyperlink, НЕ подпись под фото (О18, #229):
    # нет footer на cover до этого фото, добавляем минимальную строку только
    # под provenance (12pt italic, LIGHT), r.hyperlink.address проверяем в XML.
    _prov = text_runs(s, 0.5, 6.95, 5.9, 0.3, [
        {"text": "Фото: ", "size": 10.5, "italic": True, "color": LIGHT},
        {"text": "UAV-IQ, Wikimedia Commons, CC BY-SA 4.0",
         "size": 10.5, "italic": True, "color": LIGHT},
    ])
    _prov_runs = [r for p in _prov.text_frame.paragraphs for r in p.runs]
    _prov_runs[-1].font.underline = True
    _prov_runs[-1].hyperlink.address = (
        "https://commons.wikimedia.org/wiki/File:UAV-IQ_Conducting_Drone_"
        "Biological_Control_Operations_in_California.jpg")

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
    # Issue #340 visual-richness pass — owner: интро только диаграммы/иконки,
    # без крупных реальных фото. 5 карточек L1-L5 получают превью-фото своего
    # раздела (переиспользование уже акклиматизированных CC-фото этой же
    # деки — divider hero для s06/s19/s22/s27/s36 — forward-teaser, разнесён
    # на десятки слайдов от полноразмерного hero, честный повтор, не mock).
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Карта лекции — лестница пяти уровней от поля к полке", size=26)

    # 7 horizontal cards; photo=(filename, aspect_w/h) для L1-L5, None для 0/4-bis
    cards = [
        ("0. Открытие", "Зацепка + ось + глоссарий", "", None),
        ("1. L1 Поле", "Открытая биология", "5 кейсов · 3 провала",
         ("p06-crop-sprayer-field-16x9.jpg", 1.778)),
        ("2. L2 Робот", "Специализация > универсальность", "4 кейса · 3 провала",
         ("p16-laserweeder-g2-real.jpg", 1.777)),
        ("3. L3 Животное", "Полузакрытая среда, особь", "4 кейса · 3 урока",
         ("p22-cow-eartag-milking-robot.jpg", 1.333)),
        ("4. L4 Цепочка", "Агентный ИИ лидер", "4 кейса · 2 провала",
         ("p27-grain-terminal-halifax.jpg", 1.333)),
        ("4-bis. Среда", "Связь · привязка · регуляторика", "3 sub-блока", None),
        ("5. L5 Полка", "+ 5 критериев + закрытие", "L5 + 5 AP + чек-лист",
         ("p36-supermarket-shelf-aisle.jpg", 1.333)),
    ]
    n = len(cards)
    col_w = 1.72; col_h = 2.7; gap = 0.06
    total_w = n * col_w + (n - 1) * gap
    start_x = (13.333 - total_w) / 2
    y = 1.8
    for i, (title, desc, dur, photo) in enumerate(cards):
        x = start_x + i * (col_w + gap)
        ocean_box(s, x, y, col_w, col_h)
        if photo:
            fname, ar = photo
            thumb_h = 0.78
            thumb_w = min(col_w - 0.2, thumb_h * ar)
            thumb_h2 = thumb_w / ar
            p = ASSETS / "photos" / fname
            if p.exists():
                add_image(s, p, x + (col_w - thumb_w) / 2, y + 0.08, w=thumb_w, h=thumb_h2)
            text_box(s, x + 0.1, y + 0.92, col_w - 0.2, 0.3, title,
                     size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.0)
            text_box(s, x + 0.1, y + 1.24, col_w - 0.2, 1.05, desc,
                     size=9.5, color=MID, italic=True, line_spacing=1.15,
                     align=PP_ALIGN.CENTER)
        else:
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
             "Центральный вопрос лекции:",
             size=14, italic=True, color=DARK_GREY, bold=True)
    text_box(s, 0.85, 5.5, 11.63, 1.0,
             "Где на лестнице L1→L5 ИИ работает, где ломается — и какой класс\n"
             "решения / альтернатива применимы на каждой ступени?",
             size=18, italic=True, color=DEEP, line_spacing=1.3)

    # Photo provenance (5 превью-фото L1-L5) — real hyperlinks, не подписи
    # под карточками (О18, #229); полные источники — на hero-слайдах своих
    # разделов (s06/s19/s22/s27/s36) + assets/photos/*.url.
    _s03_sources = [
        ("L1: ", "Geograph/Wikimedia CC BY-SA 2.0", "https://commons.wikimedia.org/wiki/File:Crop_sprayer_-_geograph.org.uk_-_3038217.jpg"),
        ("  ·  L2: ", "carbonrobotics.com", "https://www.carbonrobotics.com/laserweeder-g2"),
        ("  ·  L3: ", "Wikimedia, CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Holstein_Friesian_cows_queuing_for_milking_in_an_automatic_milking_system_in_Bron%C3%B3w.jpg"),
        ("  ·  L4: ", "Wikimedia, CC BY 4.0", "https://commons.wikimedia.org/wiki/File:Bulk_carrier_at_Halifax_Grain_Elevator.jpg"),
        ("  ·  L5: ", "Wikimedia, CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Aisle_in_L_Intermarche_supermarket_in_Quebec_City.jpg"),
    ]
    _runs = []
    for prefix, label, _url in _s03_sources:
        _runs.append({"text": prefix, "size": 10, "italic": True, "color": LIGHT})
        _runs.append({"text": label, "size": 10, "italic": True, "color": LIGHT})
    _tb03 = text_runs(s, 0.6, 7.05, 12.13, 0.3, _runs)
    _flat = [r for p in _tb03.text_frame.paragraphs for r in p.runs]
    # Каждый второй run (нечётный индекс) — гиперссылка на источник
    for idx, (_prefix, _label, _url) in enumerate(_s03_sources):
        _flat[idx * 2 + 1].font.underline = True
        _flat[idx * 2 + 1].hyperlink.address = _url

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

    # Issue #340 visual-richness пass: box расширен вниз (прежде заканчивался
    # на 6.1", ниже было ~1.3" свободного места до края кадра — footer на s04
    # не стоит) — один реальный визуальный якорь (open-environment ключевая
    # ось лекции) вместо чисто текстовой карточки.
    ocean_box(s, 0.6, 4.1, 5.95, 2.8)
    text_box(s, 0.85, 4.25, 5.45, 0.4, "Открытая среда (open-environment)",
             size=18, bold=True, color=DEEP)
    text_box(s, 0.85, 4.65, 5.45, 1.4,
             "Открытая биологическая среда (поле, луг). "
             "Погода, переменное освещение, пыль, тени. ИИ работает в узких задачах. "
             "Универсальная «автономная ферма» — банкротится.",
             size=12, color=DARK_GREY, italic=True, line_spacing=1.3)
    _s04_photo = ASSETS / "photos" / "p14-wheat-combine-novosibirsk.jpg"
    if _s04_photo.exists():
        _s04_th = 0.68
        _s04_tw = _s04_th * 1.501
        add_image(s, _s04_photo, 0.85 + 5.45 - _s04_tw, 6.08, w=_s04_tw, h=_s04_th)

    # RIGHT: 5 L4 terms — gold accent on first item (AP1 P1-presentation)
    text_box(s, 6.85, 1.5, 5.95, 0.4, "5 терминов цепочки поставок",
             size=16, bold=True, color=MID)
    terms = [
        ("Агентный ИИ", "ML + поиск (RAG) + конвейер действий + человек в петле", True),
        ("bp (базисный пункт)", "1 bp = 0,01%. Метрика проскальзывания сделок", False),
        ("Проскальзывание", "Разрыв между планом сделки и фактом исполнения", False),
        ("Выбросы Scope-3", "Косвенные выбросы по цепочке поставок", False),
        ("ИИ-MRV", "ИИ-мониторинг, отчёт, верификация — климат-учёт", False),
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

    _s04_prov = text_runs(s, 0.6, 7.05, 12.13, 0.3, [
        {"text": "Фото (открытая среда): ", "size": 10, "italic": True, "color": LIGHT},
        {"text": "Vladislav Nekrasov, Wikimedia Commons, CC BY 4.0",
         "size": 10, "italic": True, "color": LIGHT},
    ])
    _s04_runs = [r for p in _s04_prov.text_frame.paragraphs for r in p.runs]
    _s04_runs[-1].font.underline = True
    _s04_runs[-1].hyperlink.address = "https://commons.wikimedia.org/wiki/File:Колос_и_комбайн.jpg"

    add_speaker_notes(s, load_speaker_notes("s04"))

    # ============ s05 keystone ladder (two rows + вывод-вопрос) ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Лестница ИИ — пять уровней. На каждой ступени работает по-разному", size=20, y=0.3)

    # 5 ladder steps stacked vertically — compacted (shortened labels, not shrunk below
    # readability floor) to leave room for Row1/Row2/вывод below
    levels = [
        ("L5", "Полка / магазин", "Полностью оцифрованная среда. ИИ зрел.",
         "Walmart Eden 2017+, Tesco 2017+, X5 2020+", GOLD),
        ("L4", "Цепочка поставок", "Контролируемые потоки, быстрая связь",
         "Cargill CMAX, Tract, Olam, Walmart×Cropin", TEAL),
        ("L3", "Животное", "Полузакрытая среда, уровень особи",
         "SenseHub 2M коров, CattleEye, DeLaval V310", LIGHT),
        ("L2", "Робот", "Специализация жива; обобщённый — нет",
         "LaserWeeder G2, Saga UV-C, Tevel · против Monarch/FarmWise", MID),
        ("L1", "Поле", "Открытая биология — самая трудная",
         "See & Spray работает · Plenty/AppHarvest/Bowery провалились", DEEP),
    ]
    step_w = 9.5; step_h = 0.62; gap = 0.05
    start_x = 0.6
    start_y = 1.05
    for i, (lid, title, desc, examples, color) in enumerate(levels):
        y = start_y + i * (step_h + gap)
        ocean_box(s, start_x, y, step_w, step_h,
                  fill=LIGHT_TINT if color != GOLD else GOLD_TINT, stroke=color)
        text_box(s, start_x + 0.12, y + 0.1, 0.65, 0.42, lid,
                 size=20, bold=True, color=color,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, start_x + 0.9, y + 0.05, 3.0, 0.28, title,
                 size=13, bold=True, color=DEEP)
        text_box(s, start_x + 0.9, y + 0.34, 3.0, 0.24, desc,
                 size=10, color=MID, italic=True, line_spacing=1.0)
        text_box(s, start_x + 3.95, y + 0.16, step_w - 4.1, 0.34,
                 examples, size=10.5, italic=True, color=DARK_GREY, line_spacing=1.05)

    ladder_h = 5 * step_h + 4 * gap  # == 3.3

    # Right-side axis indicator — matched height to ladder.
    # Issue #340 visual-richness pass: 4 раздельных hdr/desc пар сведены в
    # один компактный список (тот же текст, плотнее раскладка), освобождая
    # ~1.6" под единственное реальное фото этого кадра (owner: s05 — один из
    # четырёх «ядро введения» слайдов, где иллюстрация обязательна даже при
    # максимальной плотности keystone-кадра).
    ocean_box(s, 10.3, start_y, 2.4, ladder_h, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 10.45, start_y + 0.04, 2.1, 0.22, "↑ движение",
             size=11, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.0)
    _s05_photo = ASSETS / "photos" / "p33-john-deere-starfire-gps.jpg"
    if _s05_photo.exists():
        _s05_pw = 2.1
        _s05_ph = _s05_pw / 1.333
        add_image(s, _s05_photo, 10.3 + (2.4 - _s05_pw) / 2, start_y + 0.32,
                   w=_s05_pw, h=_s05_ph)
        _list_y = start_y + 0.32 + _s05_ph + 0.08
    else:
        _list_y = start_y + 0.46
    arrows_text = [
        ("↑ контролируемость среды", GOLD),
        ("↑ ROI растёт", GOLD),
        ("↑ предсказуемость результата", GOLD),
        ("↓ биология — непредсказуемость падает", DARK_GREY),
    ]
    _arrow_runs = []
    for i, (line, color) in enumerate(arrows_text):
        _arrow_runs.append({"text": line, "size": 9.5, "bold": True, "color": color,
                             "newpara": i > 0})
    text_runs(s, 10.4, _list_y, 2.2, ladder_h - (_list_y - start_y), _arrow_runs,
              line_spacing=1.3)
    if _s05_photo.exists():
        _s05_prov_panel = text_runs(s, 10.4, start_y + ladder_h - 0.22, 2.2, 0.2, [
            {"text": "Фото: ", "size": 7.5, "italic": True, "color": DARK_GREY},
            {"text": "John Deere / Wikimedia, CC BY-SA 3.0",
             "size": 7.5, "italic": True, "color": DARK_GREY},
        ])
        _s05_pp_runs = [r for p in _s05_prov_panel.text_frame.paragraphs for r in p.runs]
        _s05_pp_runs[-1].font.underline = True
        _s05_pp_runs[-1].hyperlink.address = "https://commons.wikimedia.org/wiki/File:John_Deere_8295_R_with_StarFire_receiver.jpg"

    # ---- РЯД 1 — измеренная тройка (3 плашки) ----
    row1_y = start_y + ladder_h + 0.12
    row1_h = 1.15
    row1_gap = 0.14
    row1_w = (12.13 - 2 * row1_gap) / 3
    triple = [
        ("$940 млн", "Plenty Compton — потери капитала",
         "$1,9 млрд → <$15 млн (−99% за 19 мес) — закрылась не из-за ИИ"),
        ("5 млн акров", "See & Spray Ultimate — рабочий ИИ",
         "= 0,55% от ≈900М акров пашни США"),
        ("45 bp → 8 bp", "ручное хеджирование vs агент",
         "сконструированный пример для иллюстрации механизма, не измеренный кейс"),
    ]
    rx = 0.6
    for big, lbl, sub in triple:
        ocean_box(s, rx, row1_y, row1_w, row1_h, fill=LIGHT_TINT, stroke=LIGHT)
        text_box(s, rx + 0.12, row1_y + 0.06, row1_w - 0.24, 0.36, big,
                 size=22, bold=True, color=GOLD)
        text_box(s, rx + 0.12, row1_y + 0.44, row1_w - 0.24, 0.26, lbl,
                 size=11, bold=True, color=DEEP, line_spacing=1.0)
        text_box(s, rx + 0.12, row1_y + 0.71, row1_w - 0.24, 0.42, sub,
                 size=10, italic=True, color=MID, line_spacing=1.05)
        rx += row1_w + row1_gap

    # ---- РЯД 2 — честно названный пробел ----
    row2_y = row1_y + row1_h + 0.1
    row2_h = 0.48
    ocean_box(s, 0.6, row2_y, 12.13, row2_h, fill=WHITE, stroke=SOFT_GREY, stroke_pt=1.2)
    text_box(s, 0.85, row2_y + 0.03, 11.6, row2_h - 0.06,
             "Своего свидетельства к этой лекции не найдено — все кейсы ниже рассказаны не от первого лица",
             size=11, italic=True, color=DARK_GREY, anchor=MSO_ANCHOR.MIDDLE)

    # ---- Строка вывода — вопрос вечера (заменяет прежний footer) ----
    vyvod_y = row2_y + row2_h + 0.1
    vyvod_h = 1.0
    ocean_box(s, 0.6, vyvod_y, 12.13, vyvod_h, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, vyvod_y + 0.08, 11.6, 0.4,
             "Привычный ответ — «ИИ приходит в сельское хозяйство».",
             size=13, italic=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, 0.85, vyvod_y + 0.48, 11.6, 0.48,
             "Вопрос вечера — сколько ждать ответа на его действие, и успеет ли он окупиться раньше, чем сменится среда?",
             size=15, bold=True, color=DEEP, line_spacing=1.15)

    add_speaker_notes(s, load_speaker_notes("s05"))

    # ============ s05a — Обзор отрасли: цикл «от поля к полке» (issue #340 Задача 1) ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Обзор отрасли — цикл «от поля к полке»", size=22)
    text_box(s, 0.6, 1.08, 12.13, 0.25,
             "Лестница уровней — наша линза. Стадии ниже — первичны и существовали до неё",
             size=11, italic=True, color=MID)

    # Issue #340 visual-richness pass: icon-row высота слегка уплотнена
    # (0.68"→0.58", текст по-прежнему 1-2 строки умещается свободно), чтобы
    # высвободить место под реальное фото в ряду «Животноводство» ниже —
    # owner-приоритет (s05a — «ядро введения», иллюстрация обязательна).
    def stage_row(label, items, y, icon_w=0.34, box_h=0.58):
        text_box(s, 0.6, y, 12.13, 0.2, label, size=11, bold=True, color=MID)
        row_y = y + 0.22
        n = len(items)
        bw = (12.13 - (n - 1) * 0.32) / n
        bx = 0.6
        for i, (icon, name, gold) in enumerate(items):
            ocean_box(s, bx, row_y, bw, box_h,
                      fill=GOLD_TINT if gold else LIGHT_TINT, stroke=GOLD if gold else LIGHT)
            ip = ASSETS / "icons" / f"{icon}-48.png"
            if ip.exists():
                add_image(s, ip, bx + 0.1, row_y + 0.11, w=icon_w, h=icon_w)
            text_box(s, bx + 0.1 + icon_w + 0.08, row_y + 0.04, bw - icon_w - 0.26, box_h - 0.08, name,
                     size=10.5, bold=True, color=GOLD if gold else DEEP, line_spacing=1.05,
                     anchor=MSO_ANCHOR.MIDDLE)
            if i < n - 1:
                add_arrow(s, bx + bw + 0.02, row_y + box_h / 2 - 0.1, 0.28, 0.2, fill=LIGHT)
            bx += bw + 0.32
        return row_y + box_h

    row1_end = stage_row("Растениеводство — поле", [
        ("sprout", "Севооборот и подготовка почвы", False),
        ("wheat", "Посев", False),
        ("leaf", "Защита растений и питание (точное земледелие)", True),
        ("tractor", "Полевые операции + автономная техника", False),
    ], 1.4)

    # «Животноводство» — ряд расширен под реальное фото (newborn calf + cows,
    # переиспользовано с s26 L3 РФ — честный forward-teaser, 20 слайдов между
    # использованиями, не mock) слева + описание справа.
    row2_y = row1_end + 0.10
    text_box(s, 0.6, row2_y, 12.13, 0.2, "Животноводство — параллельная ветвь", size=11, bold=True, color=MID)
    row2_box_y = row2_y + 0.22
    row2_box_h = 1.05
    ocean_box(s, 0.6, row2_box_y, 12.13, row2_box_h, fill=LIGHT_TINT, stroke=LIGHT)
    _s05a_animal_photo = ASSETS / "photos" / "p26-newborn-calf-cows.jpg"
    _desc_x = 0.8
    if _s05a_animal_photo.exists():
        _ph = row2_box_h - 0.2
        _pw = _ph * 1.332
        add_image(s, _s05a_animal_photo, 0.8, row2_box_y + 0.1, w=_pw, h=_ph)
        _desc_x = 0.8 + _pw + 0.22
    text_box(s, _desc_x, row2_box_y, 0.6 + 12.13 - 0.2 - _desc_x, row2_box_h,
             "Кормопроизводство · содержание поголовья · доение/откорм · ветеринарное "
             "сопровождение · воспроизводство стада",
             size=10.5, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)
    row2_end = row2_box_y + row2_box_h

    conv_y = row2_end + 0.06
    text_box(s, 0.6, conv_y, 12.13, 0.22, "↓ сходятся", size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    row3_end = stage_row("От уборки к полке", [
        ("package", "Послеуборочная обработка и хранение", False),
        ("factory", "Первичная переработка", False),
        ("truck", "Агрологистика и товарный трейдинг", False),
        ("shopping-cart", "Распределительные центры и розница", False),
    ], conv_y + 0.26)

    infra_y = row3_end + 0.06
    ocean_box(s, 0.6, infra_y, 12.13, 0.36, fill=SURFACE)
    text_box(s, 0.8, infra_y, 11.73, 0.36,
             "Сквозь все стадии — связь и спутниковое позиционирование · права на "
             "оборудование и данные · нормативное регулирование",
             size=10, italic=True, color=DARK_GREY, anchor=MSO_ANCHOR.MIDDLE)

    models_y = infra_y + 0.42
    text_box(s, 0.6, models_y, 12.13, 0.2, "Где в цикле появляется модель — шесть мест, не «везде, где написано AI»",
             size=12, bold=True, color=DEEP)
    loci = [
        ("satellite", "Дистанционное зондирование", "спутник/БПЛА → карта индекса вегетации"),
        ("camera", "Распознавание на изображении", "сорняк, болезнь листа, походка животного, партия"),
        ("compass", "Навигация и управление машиной", "траектория, кромка, препятствие"),
        ("trending-up", "Прогноз", "урожайность, цена, спрос, риск болезни"),
        ("settings", "Оптимизация и планирование", "норма внесения, маршрут, состав хеджа"),
        ("clipboard-check", "Документооборот и отчётность", "прослеживаемость партии, выбросы, нормативы"),
    ]
    mcol_w = (12.13 - 2 * 0.12) / 3
    mcol_h = 0.56
    my0 = models_y + 0.22
    for i, (icon, name, ex) in enumerate(loci):
        col = i % 3; row = i // 3
        mx = 0.6 + col * (mcol_w + 0.12)
        my = my0 + row * (mcol_h + 0.06)
        ocean_box(s, mx, my, mcol_w, mcol_h, fill=SURFACE)
        ip = ASSETS / "icons" / f"{icon}-48.png"
        if ip.exists():
            add_image(s, ip, mx + 0.08, my + 0.07, w=0.42, h=0.42)
        text_box(s, mx + 0.56, my + 0.02, mcol_w - 0.64, 0.26, name,
                 size=10.5, bold=True, color=MID, line_spacing=1.0)
        text_box(s, mx + 0.56, my + 0.29, mcol_w - 0.64, 0.25, ex,
                 size=9, italic=True, color=DARK_GREY, line_spacing=1.0)

    add_footer(s, "На поле преобладают первые три места; в трейдинге и рознице — четвёртое, "
                  "пятое, шестое.")

    _s05a_prov = text_runs(s, 0.6, 7.33, 12.13, 0.17, [
        {"text": "Фото (животноводство): ", "size": 8, "italic": True, "color": LIGHT},
        {"text": "Uberprutser, Wikimedia Commons, CC BY-SA 3.0",
         "size": 8, "italic": True, "color": LIGHT},
    ])
    _s05a_pruns = [r for p in _s05a_prov.text_frame.paragraphs for r in p.runs]
    _s05a_pruns[-1].font.underline = True
    _s05a_pruns[-1].hyperlink.address = "https://commons.wikimedia.org/wiki/File:Newborn_calf.jpg"

    add_speaker_notes(s, load_speaker_notes("s05a"))

    # ============ s05b — Куда движется отрасль: четыре силы (issue #340 Задача 1) ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Куда движется отрасль — четыре силы толкают её к новым инструментам", size=20)
    text_box(s, 0.6, 1.08, 12.13, 0.25,
             "Отрасль не в покое. Закрывает ли задачу именно ИИ — решается отдельно и по каждому случаю",
             size=11, italic=True, color=MID)

    forces = [
        ("users", "① Дефицит рабочих рук",
         "Классические режимы держатся на людях: обход контура, обход стада, ручной сбор, оператор в кабине.",
         "$43 000/акр/год", "сбор клубники, Калифорния",
         "H-2A визы дороже и менее предсказуемы; стадо в тысячи голов — визуальный обход упирается в физику.",
         False, LIGHT, LIGHT_TINT),
        ("handshake", "② Консолидация",
         "Укрупняется с двух сторон — поставщики технологий и сами хозяйства.",
         "$3,85 млрд", "MSD / Antelliq 2024 · также $305M+$250M Deere/Blue River+Bear Flag",
         "Инструмент, названный «работающим», почти всегда работает у крупного (< 500 га — порог See & Spray).",
         True, GOLD, GOLD_TINT),
        ("thermometer", "③ Климатическая волатильность",
         "Решение — заранее, результат — на уборке через 5-6 месяцев; чем меньше сезон похож на прошлый, "
         "тем меньше стоит и опыт, и модель, настроенная по старым данным.",
         "Числовой оценки нет", "Волатильность растёт — утверждение остаётся качественным, "
         "цифра к этой лекции не найдена.",
         "", False, SOFT_GREY, WHITE),
        ("shield", "④ Регуляторное и торговое давление",
         "Приходит с двух сторон, минуя поле — от регулятора и от покупателя.",
         "АПК 2024: −3,2%", "EU AI Act 2024/1689 — высокий риск; цель «АПК будущего» (удвоение) не достигнута",
         "Торговая половина работает быстрее регуляторной — отчётность по выбросам заказывает покупатель.",
         False, LIGHT, LIGHT_TINT),
    ]
    cw = (12.13 - 0.2) / 2
    ch = 2.62
    positions = [(0.6, 1.45), (0.6 + cw + 0.2, 1.45), (0.6, 1.45 + ch + 0.15), (0.6 + cw + 0.2, 1.45 + ch + 0.15)]
    for (icon, head, intro, big, sub, foot, gold_foot, color, fill), (px, py) in zip(forces, positions):
        ocean_box(s, px, py, cw, ch, fill=fill, stroke=color if color != WHITE else SOFT_GREY,
                  stroke_pt=1.2 if color == WHITE else 1.5)
        ip = ASSETS / "icons" / f"{icon}-48.png"
        if ip.exists():
            add_image(s, ip, px + 0.16, py + 0.14, w=0.36, h=0.36)
        text_box(s, px + 0.64, py + 0.16, cw - 0.8, 0.32, head, size=13, bold=True, color=DEEP)
        text_box(s, px + 0.16, py + 0.56, cw - 0.32, 0.6, intro,
                 size=9.5, italic=True, color=DARK_GREY, line_spacing=1.15)
        is_gap_card = (fill == WHITE)
        big_color = DARK_GREY if is_gap_card else GOLD
        text_box(s, px + 0.16, py + 1.2, cw - 0.32, 0.4, big,
                 size=11 if is_gap_card else 15, bold=True, color=big_color, line_spacing=1.05)
        text_box(s, px + 0.16, py + 1.64, cw - 0.32, 0.5, sub,
                 size=8.5, italic=True, color=MID, line_spacing=1.15)
        if foot:
            text_box(s, px + 0.16, py + 1.98, cw - 0.32, 0.56, foot,
                     size=8.5, italic=True, color=GOLD if gold_foot else DARK_GREY, line_spacing=1.12)

    add_footer(s, "Провал на этом фоне — не «проблемы не было», а «решение её не закрыло»; успех — "
                  "не «ИИ работает», а «здесь закрыло, и названо почему».")
    add_speaker_notes(s, load_speaker_notes("s05b"))

    # ============ s05c — Ретроспектива отрасли по годам (owner follow-up, issue #340) ============
    # Owner: «где прорывы как в космосе, в десятки раз?» Честный ответ — на стороне
    # производительности их НЕТ в этом материале; есть обвал инвестиций (-91% YoY,
    # AgFunder) и рост ЦЕНЫ консолидации (×~13, не performance). 2 реальных графика
    # (matplotlib, gen_charts_s05c.py) + honest-contrast gold-strip (LaserWeeder ×1.6-3.9).
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Ретроспектива отрасли по годам — не прорыв в десятки раз, а обвал и консолидация",
        size=19)
    text_box(s, 0.6, 1.1, 12.13, 0.25,
             "Космос показывает кратные улучшения производительности год к году. "
             "Здесь другая многолетняя картина — и это тоже часть честного разбора отрасли",
             size=11, italic=True, color=MID)

    cw = (12.13 - 0.2) / 2
    chart_y = 1.4
    chart_box_h = 3.5
    img_h = 2.7
    img_w = img_h * 1.6  # исходный PNG 1600x1000
    iw = min(img_w, cw - 0.3)
    ih = iw / 1.6
    img_bottom = chart_y + 0.1 + ih

    # --- Левая панель: коллапс инвестиций ---
    lx = 0.6
    ocean_box(s, lx, chart_y, cw, chart_box_h)
    c1 = ASSETS / "charts" / "c39-vf-investment-collapse.png"
    if c1.exists():
        add_image(s, c1, lx + (cw - iw) / 2, chart_y + 0.1, w=iw, h=ih)
    text_box(s, lx + 0.12, img_bottom + 0.08, cw - 0.24, 0.6,
             "Общий капитал категории вертикальных ферм за 2018-2024 — ≈$3 млрд. "
             "Только в 2025 году — ≥14 банкротств на ≈$1,37 млрд.",
             size=9.3, italic=True, color=DARK_GREY, line_spacing=1.14)

    # --- Правая панель: цена сделок консолидации ---
    rx = lx + cw + 0.2
    ocean_box(s, rx, chart_y, cw, chart_box_h)
    c2 = ASSETS / "charts" / "c40-consolidation-deals.png"
    if c2.exists():
        add_image(s, c2, rx + (cw - iw) / 2, chart_y + 0.1, w=iw, h=ih)
    text_box(s, rx + 0.12, img_bottom + 0.08, cw - 0.24, 0.6,
             "Также в 2024 году — GEA приобрела CattleEye; сумма сделки не "
             "раскрыта публично.",
             size=9.3, italic=True, color=DARK_GREY, line_spacing=1.14)

    # --- Нижняя полоса: честный контраст — единственный реальный кратный выигрыш ---
    strip_y = chart_y + chart_box_h + 0.12
    strip_h = 1.9
    ocean_box(s, 0.6, strip_y, 12.13, strip_h, fill=GOLD_TINT, stroke=GOLD)
    text_runs(s, 0.82, strip_y + 0.14, 11.7, 0.32, [
        {"text": "Единственный в этой главе измеренный многолетний кратный выигрыш — ",
         "size": 13, "color": DEEP},
        {"text": "LaserWeeder", "size": 13, "bold": True, "color": DEEP},
        {"text": ":", "size": 13, "color": DEEP},
    ], line_spacing=1.15)
    # Фикс честности: $900 — общий baseline ДВУХ отдельных хозяйств (не цепочка
    # 900→550→232 одного хозяйства). База повторена у каждой пары, чтобы это
    # не читалось как последовательное падение.
    text_runs(s, 0.82, strip_y + 0.5, 11.7, 0.4, [
        {"text": "было $900/акр → $550/акр ", "size": 14.5, "bold": True, "color": DEEP},
        {"text": "(Braga Fresh, −39%)", "size": 11, "italic": True, "color": MID},
        {"text": "   ·   было $900/акр → $232/акр ", "size": 14.5, "bold": True, "color": DEEP},
        {"text": "(Triangle Farms, −74%)", "size": 11, "italic": True, "color": MID},
    ], line_spacing=1.15)
    text_box(s, 0.82, strip_y + 0.92, 11.7, 0.24,
             "Два разных хозяйства от одной и той же исходной цены — не цепочка одного "
             "хозяйства; только органические листовые культуры.",
             size=10.5, italic=True, color=DARK_GREY, line_spacing=1.1)
    text_runs(s, 0.82, strip_y + 1.22, 11.7, 0.36, [
        {"text": "Это ×1,6-3,9", "size": 14, "bold": True, "color": GOLD},
        {"text": ", не ×10-20 космической индустрии — и он не переносится на товарные пропашные культуры.",
         "size": 11.5, "italic": True, "color": DARK_GREY},
    ], line_spacing=1.15)

    add_footer(s, "Источники: AgFunder Year-in-Review 2025 · Deere press 2017/2021 (Blue River/Bear Flag) · "
                  "MSD Animal Health press 2024-2025 (Antelliq) · Western Growers Case Study, март 2024")
    add_speaker_notes(s, load_speaker_notes("s05c"))

    # ============ s06 section1 divider — Точное земледелие (L1 Поле) ============
    # N-8 fix: заголовок — термин отрасли («Точное земледелие»), ладдер-ярлык L1 «Поле»
    # ушёл подзаголовком (frame_phrase), не в title. Caption пересчитан по фактическому
    # порядку кадров раздела (s06a..s14): 1 vendor matrix (не 3), 3 анти-ИИ критерия (не 2).
    # Issue #340 Задача 2 — тематическое фото (Tier 2, Wikimedia Commons/Geograph, Hugh
    # Venables, CC BY-SA 2.0): самоходный прыскиватель с развёрнутой штангой над полем
    # пшеницы. Источник не подписан инлайн на слайде (курс-правило) — см. speaker notes +
    # assets/photos/p06-crop-sprayer-field-16x9.jpg.url.
    divider_img_s06 = ASSETS / "photos" / "p06-crop-sprayer-field-16x9.jpg"
    section_divider(prs, 1, "Раздел 1. Точное земледелие",
        "L1 «Поле» — открытая биологическая среда: где ИИ работает узко, и где ломается даже здесь",
        current_section=1,
        caption="See & Spray → vendor matrix (5) → базовые модели → 3 провала "
                "(вертикальные фермы, ChatGPT, Plantix) → РФ · 3 анти-ИИ критерия",
        image_path=divider_img_s06 if divider_img_s06.exists() else None,
        image_caption="Самоходный прыскиватель с развёрнутой штангой над посевами пшеницы")
    s_last = prs.slides[-1]
    add_speaker_notes(s_last, load_speaker_notes("s06"))

    # ============ s06a — что это за стадия (точное земледелие) ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Точное земледелие — что это за стадия", size=24)

    # Term card — full width
    ocean_box(s, 0.6, 1.3, 12.13, 0.95, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.85, 1.4, 11.6, 0.35,
             "Точное земледелие (precision agriculture)",
             size=15, bold=True, color=DEEP)
    text_box(s, 0.85, 1.75, 11.6, 0.45,
             "Защита растений и питание культуры дифференцированно по участкам, а не единой нормой на весь контур. "
             "Термин старше обучаемых моделей — ИИ пришёл в уже существующую практику.",
             size=11, italic=True, color=MID, line_spacing=1.2)

    # Left: data & question
    ocean_box(s, 0.6, 2.4, 5.5, 2.5)
    text_box(s, 0.85, 2.5, 5.0, 0.35, "Какие данные и какой вопрос",
             size=13, bold=True, color=DEEP)
    text_box(s, 0.85, 2.9, 5.0, 1.9,
             "Сорняк и его вид · признаки болезни на листе · индекс вегетации по зонам · "
             "влажность и плодородие почвы · фаза культуры · погода · история обработок.\n\n"
             "Вопрос стадии: что внести, в какой дозе, на каком участке и в какой день — "
             "и где не вносить ничего.",
             size=11, color=DARK_GREY, italic=True, line_spacing=1.3)

    # Right: 4 method icon-cards (2x2)
    methods = [
        ("eye", "Наземный осмотр", "точнее всех, дороже всех по времени"),
        ("plane", "Съёмка с БПЛА", "индексы вегетации, выше разрешение спутника"),
        ("satellite", "Спутник", "Sentinel-1/-2 — регулярное покрытие, грубое разрешение"),
        ("tractor", "Датчики на технике", "камеры штанги, датчики урожайности — в момент прохода"),
    ]
    mcol_w = 2.95; mcol_h = 1.12; mgap = 0.1
    mx0 = 6.3
    for i, (icon, label, sub) in enumerate(methods):
        col = i % 2; row = i // 2
        mx = mx0 + col * (mcol_w + mgap)
        my = 2.4 + row * (mcol_h + mgap)
        ocean_box(s, mx, my, mcol_w, mcol_h)
        ip = ASSETS / "icons" / f"{icon}-48.png"
        if ip.exists():
            add_image(s, ip, mx + 0.12, my + 0.1, w=0.38, h=0.38)
        text_box(s, mx + 0.58, my + 0.1, mcol_w - 0.68, 0.32, label,
                 size=12, bold=True, color=MID)
        text_box(s, mx + 0.12, my + 0.46, mcol_w - 0.24, 0.6, sub,
                 size=9.5, italic=True, color=DARK_GREY, line_spacing=1.1)

    text_box(s, 6.3, 4.98, 5.95, 0.28,
             "+ лабораторный анализ почвы (недели) и метеостанции — вне этих четырёх основных",
             size=9, italic=True, color=LIGHT)

    # Bottom decision band
    ocean_box(s, 0.6, 5.3, 12.13, 1.35, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 5.4, 11.6, 0.35,
             "Решение стадии и почему она первая в цикле",
             size=13, bold=True, color=GOLD)
    text_box(s, 0.85, 5.78, 11.6, 0.8,
             "Решение: назначить обработку — чем, в какой норме, по какому участку; после прохода техники "
             "не отменить. Почему первая: среда не выбрана инженером (солнце, дождь, патоген заданы извне) — "
             "и результат измеряется на уборке, обратная связь приходит через сезон (5-6 месяцев).",
             size=11, color=DEEP, italic=True, line_spacing=1.3)

    add_speaker_notes(s, load_speaker_notes("s06a"))

    # ============ s06b — как это решают без модели (классика Раздела 1) ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Как это решают без модели — классические режимы Раздела 1", size=22)

    # Hero plate — regime #1 blanket spray
    ocean_box(s, 0.6, 1.4, 12.13, 1.3, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, 1.5, 7.3, 0.35, "① Сплошное опрыскивание по регламенту (blanket spray)",
             size=14, bold=True, color=DEEP)
    text_box(s, 0.85, 1.9, 7.3, 0.7,
             "Препарат на всю площадь по календарному плану, независимо от фактического распределения "
             "сорняка. Основная база сравнения для всего раздела.",
             size=11, italic=True, color=DARK_GREY, line_spacing=1.25)
    text_box(s, 8.3, 1.5, 4.2, 0.55, "$65-67/акр",
             size=24, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(s, 8.3, 2.08, 4.2, 0.3, "кукуруза",
             size=11, italic=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, 8.3, 2.4, 4.2, 0.25, "соя — $94/акр (2 прохода)",
             size=10, italic=True, color=MID, align=PP_ALIGN.CENTER)

    # Compact list of remaining 5 regimes
    regimes = [
        ("②", "Осмотр агронома с выборочной обработкой",
         "человек проходит контур, находит очаги; точность высокая, масштабируемость низкая"),
        ("③", "Механическая прополка",
         "культиваторы (Lemken Steketee, Kverneland Onyx), без химии и без модели — $21,23/акр (разброс $12-35)"),
        ("④", "Агротехнические приёмы",
         "севооборот, покровные культуры, сроки сева — подавляют сорняк без обработки"),
        ("⑤", "Внесение по карте урожайности прошлых лет",
         "переменная норма по зонам без обучения на новых данных — уже точное земледелие, но не ИИ"),
        ("⑥", "Консультация extension service",
         "внешняя экспертиза районного агронома вместо собственного решения"),
    ]
    ry = 2.9
    rh = 0.75
    for num, name, desc in regimes:
        ocean_box(s, 0.6, ry, 12.13, rh, fill=SURFACE)
        text_box(s, 0.78, ry + 0.08, 0.45, rh - 0.16, num,
                 size=16, bold=True, color=LIGHT, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, 1.3, ry + 0.07, 4.3, rh - 0.14, name,
                 size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
        text_box(s, 5.75, ry + 0.07, 6.9, rh - 0.14, desc,
                 size=10, italic=True, color=DARK_GREY, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)
        ry += rh + 0.06

    add_footer(s, "Каждый рабочий случай раздела сравнивается с одним из этих шести, а не с нулём. "
                  "Источники: Iowa State Extension 2026; Ohio Farm Custom Rates 2026 (OSU Extension)")
    add_speaker_notes(s, load_speaker_notes("s06b"))

    # ============ s07 See & Spray ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "See & Spray Ultimate — каноничный успех L1", size=22)

    # Left column (55%) — photo + anti-hype callout below
    ocean_box(s, 0.6, 1.3, 6.9, 3.05)
    p = ASSETS / "photos" / "p07-john-deere-sprayer.jpg"
    if p.exists():
        add_image(s, p, 0.8, 1.45, w=6.5, h=2.55)
    text_box(s, 0.8, 4.05, 6.5, 0.25, "John Deere ExactApply + See & Spray Ultimate · ноябрь 2025",
             size=10, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    ocean_box(s, 0.6, 4.45, 6.9, 2.15, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.8, 4.55, 6.5, 0.35,
             "Anti-hype — Avent et al. 2024 (Weed Technology)",
             size=12, bold=True, color=MID)
    text_box(s, 0.8, 4.92, 6.5, 1.6,
             "Независимая проверка не находит статистической разницы в урожайности targeted vs broadcast "
             "(P>0,05). Экономия гербицида реальна и воспроизводима: 62,4% PRE · 28,4% EPOST · 36,5% MPOST. "
             "Crop injury у targeted ниже на до 5 п.п. Прямого перевода п.п. crop injury в бушели или доллары "
             "источники не дают — это пробел, а не домысел.",
             size=10.5, italic=True, color=DARK_GREY, line_spacing=1.3)

    # Right column (45%) — 3 data cards + 2 price plates + spec
    cards = [
        ("5M акров", "сезон 2025", "≈0,55% от 900M акров US ag total", GOLD),
        ("–50%", "гербицидов", "от baseline ≈1 lb/акр → ≈0,5 lb", MID),
        ("+3,9%", "урожайности сои", "от базы ≈50,7 bu/A (не кукуруза, +2,0 bu/A)", LIGHT),
    ]
    cy = 1.3
    for big, lbl, sub, color in cards:
        ocean_box(s, 7.75, cy, 4.98, 0.82, fill=LIGHT_TINT if color != GOLD else GOLD_TINT)
        text_box(s, 7.93, cy + 0.06, 2.1, 0.45, big, size=20, bold=True, color=color)
        text_box(s, 7.93, cy + 0.52, 2.1, 0.28, lbl, size=11, color=DEEP, italic=True)
        text_box(s, 10.1, cy + 0.1, 2.55, 0.62, sub,
                 size=9.5, color=MID, italic=True, align=PP_ALIGN.RIGHT, line_spacing=1.15)
        cy += 0.9

    # 2 price plates — classical regimes
    py = cy + 0.08
    ph = 0.95
    pw = (4.98 - 0.14) / 2
    plates2 = [
        ("$65-67/акр", "сплошной спрей, кукуруза", "соя — $94/акр"),
        ("$21,23/акр", "механ. культивация", "разброс $12-35/акр"),
    ]
    px = 7.75
    for big, lbl, sub in plates2:
        ocean_box(s, px, py, pw, ph, fill=SURFACE)
        text_box(s, px + 0.1, py + 0.06, pw - 0.2, 0.32, big, size=15, bold=True, color=MID)
        text_box(s, px + 0.1, py + 0.4, pw - 0.2, 0.28, lbl, size=9, italic=True, color=DEEP, line_spacing=1.1)
        text_box(s, px + 0.1, py + 0.66, pw - 0.2, 0.26, sub, size=8.5, italic=True, color=LIGHT)
        px += pw + 0.14

    # Spec card
    sy = py + ph + 0.1
    ocean_box(s, 7.75, sy, 4.98, 0.6, fill=SURFACE)
    text_box(s, 7.93, sy + 0.06, 4.7, 0.48,
             "36 камер · CNN-детектор + detection head · >1M изображений · NVIDIA Jetson edge · <50 мс",
             size=10, color=DARK_GREY, italic=True, line_spacing=1.2)

    add_footer(s, "Источники: AgTechNavigator 2025-11-10; Deere press ноябрь 2025; GrowIWM 2024; "
                  "Avent et al. 2024; Iowa State Extension 2026; Ohio Extension 2026")
    add_speaker_notes(s, load_speaker_notes("s07"))

    # ============ s07a — See & Spray, полная форма разбора §4 канона ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "See & Spray — цена ошибок, классика, модель, что переехало", size=20)

    # ① Цена двух ошибок
    text_box(s, 0.6, 1.25, 12.13, 0.25,
             "① Цена двух ошибок — в бушелях с акра на базе ≈50,7 bu/А и в п.п. crop injury",
             size=11, bold=True, color=MID)
    err_w = (12.13 - 0.2) / 2
    ocean_box(s, 0.6, 1.52, err_w, 1.1, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.78, 1.6, err_w - 0.3, 0.35, "≈10-14 → 40 бу/акр", size=18, bold=True, color=GOLD)
    text_box(s, 0.78, 1.97, err_w - 0.3, 0.28, "Пропущенный сорняк (FN)", size=11, bold=True, color=DEEP)
    text_box(s, 0.78, 2.24, err_w - 0.3, 0.35,
             "от базы ≈50,7 бу/акр, умеренная→тяжёлая засорённость; альт. — контроль +10 бу/акр при цене >$70/акр (Миссисипи)",
             size=8.5, italic=True, color=MID, line_spacing=1.1)
    ocean_box(s, 0.6 + err_w + 0.2, 1.52, err_w, 1.1, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.78 + err_w + 0.2, 1.6, err_w - 0.3, 0.35, "≤5 п.п.", size=18, bold=True, color=GOLD)
    text_box(s, 0.78 + err_w + 0.2, 1.97, err_w - 0.3, 0.28, "Повреждение культуры (FP, crop injury)", size=11, bold=True, color=DEEP)
    text_box(s, 0.78 + err_w + 0.2, 2.24, err_w - 0.3, 0.35,
             "targeted ниже broadcast; перевод в бу/$ источники не дают — пробел, не домысел (Avent et al. 2024)",
             size=8.5, italic=True, color=MID, line_spacing=1.1)

    # ② Классика + ③ Модель
    text_box(s, 0.6, 2.78, 12.13, 0.25,
             "② Классические режимы + ③ Модель против них — все в $/акр",
             size=11, bold=True, color=MID)
    trio_w = (12.13 - 0.3) / 3
    trio = [
        ("$65-67/акр", "Сплошной спрей — кукуруза", "соя — $94/акр (2 прохода)", LIGHT, LIGHT_TINT),
        ("$21,23/акр", "Механическая культивация", "разброс $12-35/акр, без химии", LIGHT, LIGHT_TINT),
        ("$1 / $5 за акр", "See & Spray — подписка", "$1 fallow · $5 in-crop", GOLD, GOLD_TINT),
    ]
    tx = 0.6
    for big, lbl, sub, color, fill in trio:
        ocean_box(s, tx, 3.05, trio_w, 1.05, fill=fill, stroke=color)
        text_box(s, tx + 0.12, 3.12, trio_w - 0.24, 0.32, big, size=15, bold=True, color=color if color != GOLD else GOLD)
        text_box(s, tx + 0.12, 3.46, trio_w - 0.24, 0.28, lbl, size=10, bold=True, color=DEEP, line_spacing=1.05)
        text_box(s, tx + 0.12, 3.74, trio_w - 0.24, 0.32, sub, size=9, italic=True, color=MID, line_spacing=1.05)
        tx += trio_w + 0.15

    # ④ Инженерный аппарат (issue #340 Задача 3 — ИИ-модель вынесена отдельно на s07c,
    # здесь только физическое устройство: штанга, камеры, форсунки, механика срабатывания)
    text_box(s, 0.6, 4.28, 12.13, 0.22, "④ Инженерный аппарат", size=11, bold=True, color=MID)
    ocean_box(s, 0.6, 4.5, 12.13, 0.58, fill=SURFACE)
    text_box(s, 0.78, 4.56, 11.8, 0.46,
             "36 камер по штанге (≈2500 кв. футов/сек каждая) → соленоидный клапан форсунки срабатывает "
             "за <50 мс на скорости движения 25 км/ч. Продукт: John Deere See & Spray Ultimate "
             "(ExactApply, R-серия, dual-tank). Как устроена сама модель внутри — на следующем кадре.",
             size=10, color=DARK_GREY, italic=True, line_spacing=1.2)

    # ⑤ Что переехало
    text_box(s, 0.6, 5.2, 12.13, 0.22, "⑤ Что переехало", size=11, bold=True, color=MID)
    half_w = (12.13 - 0.2) / 2
    ocean_box(s, 0.6, 5.42, half_w, 1.5, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.78, 5.5, half_w - 0.3, 0.3, "Подтверждено независимо", size=12, bold=True, color=MID)
    text_box(s, 0.78, 5.82, half_w - 0.3, 1.05,
             "Экономия гербицида: 62,4% PRE · 28,4% EPOST · 36,5% MPOST (Avent et al. 2024). "
             "Crop injury ниже на до 5 п.п. у targeted.",
             size=10, italic=True, color=DARK_GREY, line_spacing=1.25)
    ocean_box(s, 0.6 + half_w + 0.2, 5.42, half_w, 1.5, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.78 + half_w + 0.2, 5.5, half_w - 0.3, 0.3, "Не подтверждено независимо", size=12, bold=True, color=GOLD)
    text_box(s, 0.78 + half_w + 0.2, 5.82, half_w - 0.3, 1.05,
             "Прирост урожайности +2,0 бу/акр (до 4,8 в лучших случаях) — цифра вендора (Deere, AgTechNavigator). "
             "Avent et al. 2024: P>0,05 — различий в урожайности нет.",
             size=10, italic=True, color=DEEP, line_spacing=1.25)

    add_footer(s, "Источники: Avent et al. 2024, Weed Technology; Iowa State Extension 2026; "
                  "Ohio Extension 2026; Deere press ноябрь 2025")
    add_speaker_notes(s, load_speaker_notes("s07a"))

    # ============ s07c — See & Spray, как устроена модель (issue #340 Задача 3) ============
    # Разведено от s07a: s07a — инженерный аппарат (штанга/камеры/форсунки), s07c — чисто
    # ИИ-слой (архитектура/обучение/inference/design rationale). Fact-check: правильная
    # цифра training set — >1 млн изображений (Deere/Blue River primary source); фигура
    # "20 млн / 40+ млн" из чернового абзаца chapter.md §1.1 "Технический deep-dive"
    # относится к LaserWeeder G2 (см. chapter-part2.md §2.2) — НЕ используется здесь.
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "See & Spray — как устроена модель", size=24)

    text_box(s, 0.6, 1.2, 12.13, 0.3,
             "Штанга, камеры и форсунки — на предыдущем кадре. Здесь — только то, что "
             "происходит между кадром камеры и решением «сорняк / не сорняк»",
             size=11, italic=True, color=MID)

    panels = [
        ("cpu", "① Архитектура",
         "Свёрточная нейросеть с детекционным head'ом (CNN backbone + detection head) — "
         "семейство object detection (аналог YOLO / Faster R-CNN), проприетарная реализация "
         "Blue River Technology. Отличает культуру от сорняка по форме листа, текстуре, "
         "плотности, контексту кадра — не по цвету.", LIGHT, LIGHT_TINT),
        ("database", "② Обучение",
         ">1 млн размеченных полевых изображений (первичный источник Deere/Blue River), "
         "собранных из 10 ключевых пшеничных, кукурузных, соевых регионов США за 2011-2020. "
         "Облако участвует только в ночном обновлении весов — не в решении на ходу.", GOLD, GOLD_TINT),
        ("zap", "③ Inference-конвейер",
         "Вход — кадр одной из 36 камер → детекция в реальном времени → сигнал на форсунку. "
         "On-device: edge-GPU класса NVIDIA Jetson на каждом боуме штанги — не облако. "
         "<50 мс от пикселя до решения — часть общего бюджета задержки системы.", LIGHT, LIGHT_TINT),
        ("network", "④ Почему именно так",
         "Cloud-uplink на скорости 25 км/ч при переменной сотовой связи в поле — single point "
         "of failure. Edge ML здесь не упрощение cloud-ML, а структурное архитектурное решение "
         "под задачу: модель живёт там, где принимается решение, а не там, где есть связь.", GOLD, GOLD_TINT),
    ]
    pw = (12.13 - 0.2) / 2
    ph = 2.55
    positions = [(0.6, 1.65), (0.6 + pw + 0.2, 1.65), (0.6, 1.65 + ph + 0.15), (0.6 + pw + 0.2, 1.65 + ph + 0.15)]
    for (icon, head, body, color, fill), (px, py) in zip(panels, positions):
        ocean_box(s, px, py, pw, ph, fill=fill, stroke=color)
        ip = ASSETS / "icons" / f"{icon}-96.png"
        if ip.exists():
            add_image(s, ip, px + 0.2, py + 0.2, w=0.55, h=0.55)
        text_box(s, px + 0.92, py + 0.28, pw - 1.1, 0.4, head,
                 size=15, bold=True, color=color if color != GOLD else GOLD)
        text_box(s, px + 0.22, py + 0.95, pw - 0.44, ph - 1.12, body,
                 size=13, color=DARK_GREY, italic=True, line_spacing=1.42)

    add_footer(s, "Источники: John Deere press (ноябрь 2025); AgTechNavigator (2025-11-10) "
                  "(training provenance: >1 млн, не 40 млн — та цифра принадлежит LaserWeeder G2)")
    add_speaker_notes(s, load_speaker_notes("s07c"))

    # ============ s08 vendor matrix L1 ============
    # K-3/K-4 fix: добавлен РЕАЛЬНЫЙ скриншот xarvio FIELD MANAGER (Apple App Store
    # listing) в правую колонку — честно подписан как иллюстрация платформы, НЕ как
    # точный скриншот японского рисового сервиса (тот скриншотов не публиковал;
    # press-release PDF BASF p-25-191 проверен постранично — только логотипы).
    # Matrix + sidebar text сжаты в левую колонку (~65% ширины), чтобы освободить
    # место для картинки справа.
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Платформы L1 — пять вендоров, разные режимы. Бренд ≠ режим работы",
        size=22)

    LEFT_W = 8.7  # левая колонка: matrix + sidebar text

    # 5×4 matrix (сжат в LEFT_W)
    headers = ["Платформа", "География", "Режим работы", "Бизнес-модель"]
    rows = [
        ("BASF xarvio", "ЕС, Япония (рис)", "Подписка + советы", "Оплата за акр"),
        ("Climate FieldView", "США (вышел из РФ 2022)", "Хранилище данных", "250 млн акров подписок"),
        ("Syngenta Cropwise", "Глобально", "Интеграция Bayer Forward", "В составе пакета"),
        ("Granular (Corteva)", "США", "Управление хозяйством", "Облачный сервис"),
        ("Taranis", "Глобально", "Компьютерное зрение + дроны", "Оплата за акр"),
    ]
    matrix_x = 0.6
    matrix_y = 1.55
    col_widths = [2.1, 1.95, 2.35, 2.1]  # sum 8.5 + 3*0.05 gaps = 8.65 ≈ LEFT_W
    row_h = 0.5

    # Header row
    cx = matrix_x
    for i, (hdr, w) in enumerate(zip(headers, col_widths)):
        ocean_box(s, cx, matrix_y, w, row_h, fill=DEEP, stroke=DEEP)
        text_box(s, cx, matrix_y, w, row_h, hdr,
                 size=11, bold=True, color=WHITE,
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
            text_box(s, cx + 0.08, ry, w - 0.16, row_h, val,
                     size=9.5, bold=(ci == 0), color=GOLD if is_gold else DEEP,
                     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
            cx += w + 0.05
    matrix_bottom = matrix_y + row_h + 0.05 + len(rows) * (row_h + 0.05)  # ≈4.8

    # Sidebar callout (текст, под matrix, той же левой колонки шириной)
    ocean_box(s, 0.6, matrix_bottom + 0.1, LEFT_W, 1.95, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.8, matrix_bottom + 0.2, LEFT_W - 0.4, 0.5,
             "★ Ключевое на слайде — BASF xarvio в Японии: гарантия урожайности риса (октябрь 2025)",
             size=12, bold=True, color=GOLD, line_spacing=1.1)
    text_box(s, 0.8, matrix_bottom + 0.7, LEFT_W - 0.4, 1.3,
             "Первый случай гарантированной урожайности под ИИ-советы: BASF выплачивает компенсацию "
             "при недоборе урожая. Закрытый контур данных + страховой механизм = единственный известный "
             "к 2026 году пример.\n"
             "Остальные 4 платформы матрицы — для самостоятельной проработки; критерий «бренд ≠ режим "
             "работы» применяется к каждой.",
             size=10.5, color=DARK_GREY, italic=True, line_spacing=1.25)

    # RIGHT column — настоящий скриншот xarvio FIELD MANAGER (Apple App Store)
    img_x, img_w = 9.5, 2.65
    shot_p = ASSETS / "photos" / "p08-xarvio-field-manager-map.jpg"
    if shot_p.exists():
        add_image(s, shot_p, img_x, 1.55, w=img_w, h=4.85)
    text_box(s, img_x - 0.15, 6.42, img_w + 0.3, 0.55,
             "xarvio FIELD MANAGER — карта поля по зонам риска. Иллюстрация платформы, "
             "НЕ скриншот японского рисового сервиса (не публиковался)",
             size=8.5, italic=True, color=LIGHT, line_spacing=1.1, align=PP_ALIGN.CENTER)

    add_footer(s, "Источники: пресс-релиз BASF p-25-191 октябрь 2025 · TAdviser FieldView 2022 · "
                  "скриншот — Apple App Store, xarvio FIELD MANAGER")
    add_speaker_notes(s, load_speaker_notes("s08"))

    # ============ s08a — дистанционный мониторинг: дрон и спутник (issue #340) ============
    # Новый working case между See & Spray (исполняет) и xarvio/FieldView (советует):
    # дрон/спутник только наблюдают, решение принимает агроном-скаут. 2 реальных
    # изображения: Wikimedia Commons CC BY-SA 4.0 (дрон-NDVI карта) + NASA SVS public
    # domain (спутниковый композит дерешо Айовы 2020-08-07/11 — прямая иллюстрация
    # 2-недельной задержки NDVI, разобранной в тексте).
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Дистанционный мониторинг посевов — дрон и спутник наблюдают, агроном решает",
        size=19)
    text_box(s, 0.6, 1.1, 12.13, 0.25,
             "Третий класс продуктов первой ступени — между распылением (See & Spray) и "
             "советом (xarvio/FieldView): наблюдает дрон или спутник, решает человек",
             size=10.5, italic=True, color=MID)

    # Ряд 1 — 3 классические плашки
    plate_y = 1.42; plate_h = 0.78
    plate_w = (12.13 - 0.3) / 3
    plates = [
        ("$6,65/акр", "Ручной обход скаута", "разброс $3,82-9,50; предел ≈15-20 тыс. акров/сезон"),
        ("USDA NASS", "Objective Yield Surveys", "гос. эталон — физический обмер делянок"),
        ("Базовый тариф", "Спутниковый снимок без модели", "агроном сам читает карту NDVI"),
    ]
    px = 0.6
    for big, lbl, sub in plates:
        ocean_box(s, px, plate_y, plate_w, plate_h, fill=LIGHT_TINT, stroke=LIGHT)
        text_box(s, px + 0.12, plate_y + 0.06, plate_w - 0.24, 0.3, big, size=15, bold=True, color=MID)
        text_box(s, px + 0.12, plate_y + 0.37, plate_w - 0.24, 0.24, lbl, size=10, bold=True, color=DEEP, line_spacing=1.0)
        text_box(s, px + 0.12, plate_y + 0.58, plate_w - 0.24, 0.2, sub, size=8, italic=True, color=MID, line_spacing=1.0)
        px += plate_w + 0.15

    # Ряд 2 — 2 панели: Дрон / Спутник, каждая с реальным изображением
    panel_y = plate_y + plate_h + 0.12
    panel_h = 3.25
    panel_w = (12.13 - 0.2) / 2

    # Панель «Дрон» — iter2: bullets переведены на text_runs (ключевые цифры bold),
    # иконка plane рядом с заголовком панели — семантический якорь дрона
    ocean_box(s, 0.6, panel_y, panel_w, panel_h, fill=LIGHT_TINT, stroke=LIGHT)
    ip_drone_hdr = ASSETS / "icons" / "plane-48.png"
    if ip_drone_hdr.exists():
        add_image(s, ip_drone_hdr, 0.78, panel_y + 0.06, w=0.26, h=0.26)
    text_box(s, 1.1, panel_y + 0.08, panel_w - 0.7, 0.28, "Дрон", size=14, bold=True, color=MID)
    img_w = 2.6; img_h = img_w * (450 / 854)
    img_drone = ASSETS / "photos" / "p08a-drone-ndvi-map.png"
    if img_drone.exists():
        add_image(s, img_drone, 0.6 + panel_w - img_w - 0.15, panel_y + 0.08, w=img_w, h=img_h)
    text_box(s, 0.6 + panel_w - img_w - 0.15, panel_y + 0.1 + img_h, img_w, 0.22,
             "NDVI-карта с дрона (иллюстрация)", size=7, italic=True, color=LIGHT, line_spacing=1.0)
    drone_lines = [
        ("Sentera FieldAgent — ", "700 акров/час", ", заявлено ", "97%"),
        ("WeedScout 2024: ", "13 000 акров сои", " · ", "99%", " предписаний за 24ч · ", "–64%", " гербицида (база в кг/акр не названа)"),
        ("", "23 мая 2025", " — Deere купил Sentera целиком"),
        ("OCEALIA/senseFly: ", "+10%", " — самоотчёт без контрольной группы"),
        ("XAG: ", "20 млн га", ", ", "+400%", " г/г к 2019"),
    ]
    bullet_w = panel_w - img_w - 0.6
    ly = panel_y + 0.44
    bullet_h = [0.4, 0.62, 0.3, 0.4, 0.32]
    bsize = 10.5
    for parts, bh in zip(drone_lines, bullet_h):
        runs = [{"text": "• ", "size": bsize, "italic": True, "color": DARK_GREY}]
        for i, part in enumerate(parts):
            is_num = (i % 2 == 1)
            runs.append({"text": part, "size": bsize, "italic": True,
                         "bold": is_num, "color": MID if is_num else DARK_GREY})
        text_runs(s, 0.78, ly, bullet_w, bh, runs, line_spacing=1.25)
        ly += bh + 0.12

    # Панель «Спутник» — iter2: text_runs + satellite-иконка у заголовка
    sat_x = 0.6 + panel_w + 0.2
    ocean_box(s, sat_x, panel_y, panel_w, panel_h, fill=GOLD_TINT, stroke=GOLD)
    ip_sat_hdr = ASSETS / "icons" / "satellite-48.png"
    if ip_sat_hdr.exists():
        add_image(s, ip_sat_hdr, sat_x + 0.18, panel_y + 0.06, w=0.26, h=0.26)
    text_box(s, sat_x + 0.5, panel_y + 0.08, panel_w - 0.7, 0.28, "Спутник", size=14, bold=True, color=GOLD)
    simg_w = 2.6; simg_h = simg_w * (1152 / 2048)
    img_sat = ASSETS / "photos" / "p08a-satellite-iowa-derecho.png"
    if img_sat.exists():
        add_image(s, img_sat, sat_x + panel_w - simg_w - 0.15, panel_y + 0.08, w=simg_w, h=simg_h)
    text_box(s, sat_x + panel_w - simg_w - 0.15, panel_y + 0.1 + simg_h, simg_w, 0.3,
             "NASA SVS — дерешо Айовы, NDVI 7/11 авг. 2020", size=6.8, italic=True, color=DEEP, line_spacing=1.0)
    sat_lines = [
        ("Planet Labs PlanetScope — ", "3,7 м/px", " · ", "$0,14-0,73/акр/год", " (в 9-47× дешевле скаута — другой продукт)"),
        ("SatAgro: ", "160 000 га", " сахарной свёклы"),
        ("Gro Intelligence: ", "98%", " от отчёта USDA за 8 лет; в 2022 точнее консенсуса аналитиков"),
        ("", "Дерешо 10 авг 2020", ": снимок обновился через ", "2 недели", " — оценка упала постфактум"),
    ]
    sat_bullet_w = panel_w - simg_w - 0.6
    ly = panel_y + 0.44
    sat_bullet_h = [0.7, 0.3, 0.5, 0.5]
    for parts, bh in zip(sat_lines, sat_bullet_h):
        runs = [{"text": "• ", "size": bsize, "italic": True, "color": DEEP}]
        for i, part in enumerate(parts):
            is_num = (i % 2 == 1)
            runs.append({"text": part, "size": bsize, "italic": True,
                         "bold": is_num, "color": GOLD if is_num else DEEP})
        text_runs(s, sat_x + 0.18, ly, sat_bullet_w, bh, runs, line_spacing=1.25)
        ly += bh + 0.12

    # Полоса снизу — 5 границ применимости
    lim_y = panel_y + panel_h + 0.12
    lim_h = 0.85
    limits = [
        ("users", "Размер хозяйства", "затраты размываются только на большой площади"),
        ("sprout", "Окно стадии роста", "точно только 14-20 дней после посева"),
        ("map", "Разрешение vs поле", "пиксель Sentinel-2 = 100 м²; малое поле — мало пикселей"),
        ("plane", "Регуляторика БПЛА", "FAA Part 107 — оператор в пределах VLOS"),
        ("radar", "Облачность", "срезает 36 теор. снимков до 6-8 пригодных/сезон"),
    ]
    lw = (12.13 - 0.4) / 5
    lx = 0.6
    for icon, lbl, sub in limits:
        ocean_box(s, lx, lim_y, lw, lim_h, fill=SURFACE)
        ip = ASSETS / "icons" / f"{icon}-48.png"
        if ip.exists():
            add_image(s, ip, lx + 0.1, lim_y + 0.08, w=0.26, h=0.26)
        text_box(s, lx + 0.1, lim_y + 0.38, lw - 0.2, 0.22, lbl, size=8.8, bold=True, color=MID, line_spacing=1.0)
        text_box(s, lx + 0.1, lim_y + 0.58, lw - 0.2, 0.26, sub, size=7.3, italic=True, color=DARK_GREY, line_spacing=1.05)
        lx += lw + 0.1

    add_footer(s, "Источники: Iowa State Custom Rate Survey 2026 · Sugar Producer 2019 · Sentera press 2024 · "
                  "Deere press 2025-05-23 · DTN/Progressive Farmer 2020-10-01")
    add_speaker_notes(s, load_speaker_notes("s08a"))

    # ============ s08b — Sentera: 97% кукуруза/хлопок, r<0,30 соя (issue #340) ============
    # Iter2 fix: исходная вёрстка переполняла слайд (карточки банкротств наезжали на
    # footer) — весь вертикальный бюджет пересчитан заново под 7.5" с запасом.
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s, "Sentera — 97% на кукурузе и хлопке, r<0,30 на сое", size=22)

    # Плашка «было·стало»
    hw = (12.13 - 0.2) / 2
    ocean_box(s, 0.6, 1.3, hw, 0.8, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.8, 1.36, hw - 0.4, 0.38, "97%", size=26, bold=True, color=GOLD)
    text_box(s, 0.8, 1.78, hw - 0.4, 0.28, "заявлено Sentera · кукуруза, хлопок (2019)",
             size=9.5, italic=True, color=DEEP, line_spacing=1.05)
    ocean_box(s, 0.6 + hw + 0.2, 1.3, hw, 0.8, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.8 + hw + 0.2, 1.36, hw - 0.4, 0.38, "r<0,30 (R²≈0,10)", size=21, bold=True, color=MID)
    text_box(s, 0.8 + hw + 0.2, 1.78, hw - 0.4, 0.28, "независимо · MSU Extension · соя (2024-2025)",
             size=9.5, italic=True, color=DEEP, line_spacing=1.05)
    text_box(s, 0.6, 2.16, 12.13, 0.24, "Тот же вендор, та же камера, другая культура",
             size=10.5, bold=True, italic=True, color=DARK_GREY, align=PP_ALIGN.CENTER)

    # Мини-таблица 5 методов MSU
    text_box(s, 0.6, 2.46, 12.13, 0.2,
             "Пять методов, двухлетнее исследование MSU Extension 2024-2025", size=10.5, bold=True, color=MID)
    methods = [
        ("Ручной подсчёт", "эталон"),
        ("BeanCam", "r=0,3122 (p=0,0003) — значимо, но слабо"),
        ("Smart Stand", "r<0,30"),
        ("Аэрофото + Agremo", "r<0,30"),
        ("Аэрофото + Sentera", "r<0,30"),
    ]
    mt_y = 2.68; mt_h = 0.29; mt_gap = 0.03
    for i, (name, res) in enumerate(methods):
        fill = SURFACE if i % 2 == 0 else LIGHT_TINT
        ocean_box(s, 0.6, mt_y, 12.13, mt_h, fill=fill, stroke=LIGHT, stroke_pt=0.4)
        text_box(s, 0.78, mt_y, 4.2, mt_h, name, size=10, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, 5.1, mt_y, 7.4, mt_h, res, size=10, italic=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
        mt_y += mt_h + mt_gap
    text_box(s, 0.6, mt_y + 0.02, 12.13, 0.22,
             "Вывод MSU: «старомодный ручной метод остаётся самым точным»",
             size=10, bold=True, italic=True, color=DARK_GREY)

    # Вывод-плашка AP3
    ap_y = mt_y + 0.3
    ocean_box(s, 0.6, ap_y, 12.13, 0.5, fill=TEAL_TINT, stroke=TEAL)
    text_box(s, 0.8, ap_y + 0.05, 11.7, 0.4,
             "Точность — свойство пары (культура, задача), не бренда. Второй раз в разделе (после Plantix) "
             "— AP3: пороговая точность на одной задаче не гарантирует развёртывание на другой.",
             size=10.5, bold=True, color=TEAL, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)

    # 2 карточки банкротств
    bc_y = ap_y + 0.58
    bc_h = 1.72
    bc_w = (12.13 - 0.2) / 2
    ocean_box(s, 0.6, bc_y, bc_w, bc_h)
    ip_bc1 = ASSETS / "icons" / "building-2-48.png"
    if ip_bc1.exists():
        add_image(s, ip_bc1, 0.8, bc_y + 0.1, w=0.24, h=0.24)
    text_box(s, 1.12, bc_y + 0.08, bc_w - 0.72, 0.28, "PrecisionHawk", size=13, bold=True, color=DEEP)
    text_box(s, 0.8, bc_y + 0.36, bc_w - 0.4, 0.24, "Chapter 7 · декабрь 2023", size=10.5, italic=True, color=MID)
    text_box(s, 0.8, bc_y + 0.6, bc_w - 0.4, 0.32, ">$136M привлечено vs ≈$17M долга / ≈$3,8M активов",
             size=9.5, bold=True, color=GOLD, line_spacing=1.1)
    text_box(s, 0.8, bc_y + 0.94, bc_w - 0.4, 0.7,
             "«Мы знали, что сделать PrecisionHawk прибыльной в короткий срок будет непросто» — "
             "бизнес-провал, не провал точности", size=8.8, italic=True, color=DARK_GREY, line_spacing=1.15)
    ocean_box(s, 0.6 + bc_w + 0.2, bc_y, bc_w, bc_h)
    ip_bc2 = ASSETS / "icons" / "building-2-48.png"
    if ip_bc2.exists():
        add_image(s, ip_bc2, 0.8 + bc_w + 0.2, bc_y + 0.1, w=0.24, h=0.24)
    text_box(s, 1.12 + bc_w + 0.2, bc_y + 0.08, bc_w - 0.72, 0.28, "Gro Intelligence", size=13, bold=True, color=DEEP)
    text_box(s, 0.8 + bc_w + 0.2, bc_y + 0.36, bc_w - 0.4, 0.24, "закрытие · май-июнь 2024", size=10.5, italic=True, color=MID)
    text_box(s, 0.8 + bc_w + 0.2, bc_y + 0.6, bc_w - 0.4, 0.32, ">$115M привлечено · –60% штата в марте · расследование SEC",
             size=9.5, bold=True, color=GOLD, line_spacing=1.1)
    text_box(s, 0.8 + bc_w + 0.2, bc_y + 0.94, bc_w - 0.4, 0.7,
             "«Фундаментальное несовпадение продукта и рынка» — та же модель, что точнее консенсуса "
             "аналитиков по урожайности, бизнес всё равно не выжил", size=8.8, italic=True, color=DARK_GREY, line_spacing=1.15)

    add_footer(s, "Источники: Farm Progress «High-tech or hula hoop…»; MSU CANR 2024-2025; "
                  "банкротство PrecisionHawk дек. 2023; закрытие Gro Intelligence май-июнь 2024")
    add_speaker_notes(s, load_speaker_notes("s08b"))

    # ============ s09 foundation models — simplified, 3 key claims ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Базовые модели 2026 — порог входа упал на 2-3 порядка",
        size=22)

    # Left (55%): Sentinel-2 imagery + short formula
    ocean_box(s, 0.6, 1.5, 6.5, 4.0)
    p = ASSETS / "photos" / "p09-sentinel-brazil.jpg"
    if p.exists():
        add_image(s, p, 0.85, 1.7, w=6.0, h=3.0)
    text_box(s, 0.85, 4.75, 6.0, 0.4,
             "Sentinel-2 / Copernicus (ESA, CC-BY-SA) — класс данных для TerraMind",
             size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Short formula below image
    ocean_box(s, 0.6, 5.7, 6.5, 1.2, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 0.85, 5.8, 6.0, 0.4,
             "TerraMind (IBM + ESA, 2025)",
             size=15, bold=True, color=DEEP)
    text_box(s, 0.85, 6.2, 6.0, 0.65,
             "«GPT-3 для Earth observation». Команда из 3 человек\n"
             "дообучает на тысячах изображений вместо миллионов.",
             size=12, color=DARK_GREY, italic=True, line_spacing=1.3)

    # Right (45%): ОДИН callout (issue #340 — трим 1.5→1.0 мин, вендор-риск сжат в 1 строку)
    # Iter2: box высота подогнана под фактический контент (было много пустоты снизу)
    ocean_box(s, 7.3, 1.5, 5.45, 2.95, fill=LIGHT_TINT, stroke=LIGHT)
    text_box(s, 7.5, 1.65, 5.05, 0.4,
             "Архитектура советника 2026",
             size=16, bold=True, color=MID)
    text_box(s, 7.5, 2.15, 5.05, 1.25,
             "Базовая модель (TerraMind)\n"
             "+ поиск (RAG) к локальному регулятору\n"
             "+ LLM генерация\n"
             "+ явный отказ при низкой уверенности.",
             size=13, color=DEEP, italic=True, line_spacing=1.4)
    hr_line(s, 7.5, 3.55, 5.05, color=LIGHT, weight=1.0)
    text_box(s, 7.5, 3.68, 5.05, 0.65,
             "Риск: вся отрасль — на 2-3 моделях IBM/NASA/ESA; закрытие любой из них "
             "одномоментно останавливает всех, кто на ней построен.",
             size=10.5, italic=True, color=GOLD, line_spacing=1.3)

    add_footer(s, "Источники: IBM Research, апрель 2025; NASA Earth Observatory 2025")
    add_speaker_notes(s, load_speaker_notes("s09"))

    # ============ s10 vertical farming collapse — MERGED с прежним s11 (issue #340) ============
    # Владелец одобрил: s10 (провал как класс) + s11 (5-Why) — одна причинная цепочка,
    # искусственно разнесённая на 2 кадра. Собраны в один: ① 3 карточки, ② компактная
    # 5-step chain, ③ одна итоговая GOLD-плашка с числовой декомпозицией. Бывший
    # investment-collapse chart (c10-vf-losses.png) снят — дублировал c39/c40 на s05c
    # (cross-slide redundancy), освободившееся место ушло под ②.
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Вертикальные фермы — провал не из-за плохого ИИ. AppHarvest, Plenty, Bowery",
        size=19)

    # ① 3 горизонтальные карточки
    text_box(s, 0.6, 1.1, 12.13, 0.2, "① Три кейса — капитал и причина", size=11, bold=True, color=MID)
    cards = [
        ("AppHarvest", "$475M SPAC + $341M долга ≈ $816M", "Chapter 11 июль 2023",
         "OPEX отопления Кентукки + ToBRFV вирус в Морхеде", LIGHT, LIGHT_TINT),
        ("Plenty Unlimited", "$940M из $1B+ raised с 2014", "закрыт декабрь 2024",
         "LED energy съел AI-оптимизацию; –99% оценки ($1,9 млрд→<$15M)", GOLD, GOLD_TINT),
        ("Bowery Farming", ">$700M raised", "ABC ноябрь 2024",
         "Capex first, AI после; $32M never-used в Locust Grove", LIGHT, LIGHT_TINT),
    ]
    cw3 = (12.13 - 0.3) / 3
    cx = 0.6
    card_y = 1.32; card_h = 1.85
    for name, money, date, cause, color, fill in cards:
        ocean_box(s, cx, card_y, cw3, card_h, fill=fill, stroke=color)
        text_box(s, cx + 0.14, card_y + 0.12, cw3 - 0.28, 0.32, name, size=14, bold=True, color=DEEP)
        text_box(s, cx + 0.14, card_y + 0.48, cw3 - 0.28, 0.32, money, size=14, bold=True,
                 color=color if color != GOLD else GOLD)
        text_box(s, cx + 0.14, card_y + 0.84, cw3 - 0.28, 0.24, date, size=10.5, italic=True, color=MID)
        text_box(s, cx + 0.14, card_y + 1.12, cw3 - 0.28, 0.68, cause,
                 size=10, italic=True, color=DARK_GREY, line_spacing=1.2)
        cx += cw3 + 0.15

    # ② Компактная цепочка «5 почему»
    chain_y = card_y + card_h + 0.16
    text_box(s, 0.6, chain_y, 12.13, 0.2,
             "② Пять «почему» — от банкротства до термодинамики", size=11, bold=True, color=MID)
    steps = [
        ("Почему закрылась?", "Капитал кончился", MID),
        ("Почему кончился?", "Юнит-экономика не сошлась", MID),
        ("Почему не сошлась?", "60-80% OPEX = LED-энергия", GOLD),
        ("Почему LED так дорог?", "~100× меньше энергии, чем солнце", DEEP),
        ("Закрыл ли это ML?", "Нет: эффект 5-15% при разрыве 100×", GOLD),
    ]
    step_w = 2.18; step_h = 1.75; gap = 0.15
    sx = 0.6
    sy = chain_y + 0.22
    for i, (q, a, color) in enumerate(steps):
        ocean_box(s, sx, sy, step_w, step_h,
                  fill=GOLD_TINT if color == GOLD else LIGHT_TINT, stroke=color)
        text_box(s, sx + 0.1, sy + 0.12, step_w - 0.2, 0.55, q,
                 size=11, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.15,
                 anchor=MSO_ANCHOR.MIDDLE)
        hr_line(s, sx + 0.18, sy + 0.72, step_w - 0.36, color=color, weight=1.0)
        text_box(s, sx + 0.1, sy + 0.8, step_w - 0.2, step_h - 0.9, a,
                 size=11.5, bold=(color != MID), color=color, align=PP_ALIGN.CENTER, line_spacing=1.2,
                 anchor=MSO_ANCHOR.MIDDLE)
        if i < 4:
            add_arrow(s, sx + step_w, sy + step_h/2 - 0.1, gap, 0.2, fill=LIGHT)
        sx += step_w + gap

    # ③ Итоговая GOLD-плашка — числовая декомпозиция + AP1
    final_y = sy + step_h + 0.18
    final_h = 1.1
    ocean_box(s, 0.6, final_y, 12.13, final_h, fill=GOLD_TINT, stroke=GOLD)
    text_runs(s, 0.82, final_y + 0.14, 11.7, 0.36, [
        {"text": "0,5 × 0,7 × 0,3 ≈ 10,5% ", "size": 19, "bold": True, "color": GOLD},
        {"text": "end-to-end (LED × сеть × рост) против 100% у бесплатного солнца",
         "size": 12, "italic": True, "color": DEEP},
    ], line_spacing=1.15)
    text_box(s, 0.82, final_y + 0.58, 11.7, 0.46,
             "AP1 — закон термодинамики важнее ML. ML работает на знаменателе; разрыв — в числителе. "
             "Альтернатива: открытый грунт при энергии <$0,10/кВт·ч; vertical farming — только для high-value crops.",
             size=11.5, bold=True, color=DEEP, line_spacing=1.2)

    add_footer(s, "Источники: TechCrunch 2025-03-24, 2024-11-04; Agriculture Dive 689039; "
                  "AgFunder Year-in-Review 2025; анализ Hannah Ritchie на основе MDPI Sustainability 2024")
    add_speaker_notes(s, load_speaker_notes("s10"))

    # ============ s12 ChatGPT hallucinations ============
    # K-3 fix: добавлена настоящая Figure 1 из Tzachor et al. 2024, Nature Food
    # (og:image с nature.com — единственная не-paywalled иллюстрация статьи). Честно
    # подписана как RLHF-архитектура, НЕ как Q/A-скриншот (такого в открытом доступе нет).
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "ChatGPT как агроном — «уверенно ошибочен» в десятках процентов",
        size=22)

    # Left: study summary + реальная Figure 1 статьи
    ocean_box(s, 0.6, 1.5, 6.0, 5.45)
    text_box(s, 0.85, 1.65, 5.5, 0.5,
             "Tzachor et al., Nature Food, ноябрь 2023",
             size=14, bold=True, color=DEEP)
    text_box(s, 0.85, 2.15, 5.5, 0.4,
             "Reichman University · агрономические Q/A-сценарии (publication 11.2023, press 05.2024)",
             size=11, italic=True, color=MID)
    hr_line(s, 0.85, 2.6, 5.3, color=LIGHT, weight=1.0)

    # Fact-check fix (2026-11-14): прежние цифры по моделям (GPT-3.5 32% / GPT-4 44% /
    # Bard 29% правильно; "остальные 56-71% неверны") не подтверждаются ни
    # первоисточником (Tzachor et al., Nature Food, 11.2023 — качественный кейс-стади
    # на cassava-фермерах Нигерии, не количественный бенчмарк с разбивкой по моделям),
    # ни press-освещением. Цифры придуманы при первой вёрстке и никогда не сверялись.
    # Заменено качественной формулировкой, согласованной с slides/s12-*.md speaker
    # notes ("В среднем — десятки процентов confident-wrong ответов") — без чисел
    # по отдельным моделям.
    # Fact-check fix #2 (2026-11-14, тот же круг): "184 вопроса" unverifiable (убрано
    # выше) и "Bard" — модель НЕ тестировалась ни по abstract, ни по EurekAlert/
    # phys.org, ни по systematic review (все называют только GPT-3.5 и GPT-4.0).
    # Bard убран везде в блоке; пара моделей — (GPT-3.5 и GPT-4.0).
    text_box(s, 0.85, 2.75, 5.4, 2.2,
             "В среднем — десятки процентов confident-wrong ответов "
             "(GPT-3.5 и GPT-4.0): неверная дозировка или препарат, "
             "без сигнала неуверенности.",
             size=16, color=DEEP, line_spacing=1.5,
             anchor=MSO_ANCHOR.MIDDLE)

    # Настоящая Figure 1 статьи (RLHF human-in-the-loop pipeline), AR=2170/1370=1.584
    fig_h, fig_w = 1.55, 1.55 * (2170 / 1370)
    fig_x = 0.6 + (6.0 - fig_w) / 2
    fig_p = ASSETS / "photos" / "p12-tzachor-fig1-rlhf.png"
    if fig_p.exists():
        add_image(s, fig_p, fig_x, 5.05, w=fig_w, h=fig_h)
    text_box(s, 0.78, 6.64, 5.64, 0.3,
             "Figure 1, Tzachor et al. 2024 — RLHF (обучение модели от обратной связи людей), "
             "human-in-the-loop. НЕ Q/A-скриншот — такого статья не публикует",
             size=8, italic=True, color=LIGHT, align=PP_ALIGN.CENTER, line_spacing=1.0)

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

    add_footer(s, "Источник: Tzachor et al., Nature Food, ноябрь 2023 (press coverage Phys.org 2024-05)")
    add_speaker_notes(s, load_speaker_notes("s12"))

    # ============ s13 Plantix ============
    # K-2/K-3 fix: убран stylized primitive-mock телефона (класс "mock", запрещённый
    # правилом no-mock-fallbacks) — заменён НАСТОЯЩИМ официальным скриншотом Plantix
    # из Google Play listing (экран "Instant disease detection" — Bacterial Spot).
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "Plantix — 10-15% ошибочной диагностики × 10 млн+ загрузок = ~100 тыс. неверных рекомендаций / год",
        size=18)

    # Left: настоящий Plantix UI screenshot + caption
    ocean_box(s, 0.6, 1.6, 5.5, 5.0)
    text_box(s, 0.85, 1.72, 5.0, 0.35, "Plantix · мобильное приложение",
             size=13, bold=True, color=DEEP, align=PP_ALIGN.CENTER)

    # Photo AR = 1080/1920 = 0.5625
    shot_h, shot_w = 4.05, 4.05 * (1080 / 1920)
    shot_x = 0.6 + (5.5 - shot_w) / 2
    shot_p = ASSETS / "photos" / "p13-plantix-diagnosis-screen.jpg"
    if shot_p.exists():
        add_image(s, shot_p, shot_x, 2.1, w=shot_w, h=shot_h)
    text_box(s, 0.78, 6.18, 5.34, 0.38,
             "Google Play listing · экран мгновенной диагностики — пример диагноза "
             "«бактериальная пятнистость». 10+ млн загрузок",
             size=9.5, italic=True, color=MID, align=PP_ALIGN.CENTER, line_spacing=1.1)

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

    add_footer(s, "Скриншот — Google Play listing, Plantix; данные Frontiers in Plant Science 2020 + самоотчёт Plantix")
    add_speaker_notes(s, load_speaker_notes("s13"))

    # ============ s14 РФ context L1 — расширено 4-м примером Terra Tech/Pixel.AI (issue #340) ============
    s = blank(prs); set_slide_bg(s, WHITE)
    add_assertion_title(s,
        "L1 в РФ — ExactFarming, Прогресс Агро, Terra Tech при индексе цифровизации 27,2",
        size=19)

    # Left: chart (height matched to new, taller right column) + real photo
    # below (issue #340 visual-richness pass — owner: РФ-слайды только
    # диаграммы/иконки/логотипы, без крупных реальных фото). Chart уплотнён
    # (4.1"→2.3", данные 27,2 vs 75,5 читаются без потери), освобождённое
    # место — честное Tier-2 (Wikimedia Commons) фото пшеничного поля с
    # комбайном, Новосибирская область РФ. Фото заканчивается ДО ap6_y
    # (полноширинная полоса AP6 ниже рисуется поверх левой колонки —
    # pre-existing layering этого слайда; фото обязано не доходить до неё).
    ocean_box(s, 0.6, 1.5, 6.0, 4.85)
    c = ASSETS / "charts" / "c14-rus-digi.png"
    if c.exists():
        add_image(s, c, 0.6 + (6.0 - 5.3) / 2, 1.65, w=5.3, h=2.3)
    _s14_photo = ASSETS / "photos" / "p14-wheat-combine-novosibirsk.jpg"
    if _s14_photo.exists():
        _s14_ph = 1.35
        _s14_pw = _s14_ph * 1.501
        add_image(s, _s14_photo, 0.6 + (6.0 - _s14_pw) / 2, 4.05, w=_s14_pw, h=_s14_ph)

    # Right: 4 compact cards (3 прежних + Terra Tech/Pixel.AI — прямой аналог Planet Labs/Descartes Labs)
    cards = [
        ("ExactFarming", "12 700 хозяйств · 9,8 млн га", "Управление полями + мониторинг", MID, LIGHT_TINT),
        ("АгроСигнал", "мониторинг ГСМ и техники", "Automation, не AI", LIGHT, SURFACE),
        ("ГК «Прогресс Агро»", "+5% рентабельности", "Внутренний замер 2024, не peer-review", LIGHT, LIGHT_TINT),
        ("Terra Tech / Pixel.AI (РКС)", "ошибка ≤3,5% · 2,59 млн га Пантанал · 30 ₽/км²",
         "Нейросеть по спутнику — аналог Planet Labs/Descartes Labs", GOLD, GOLD_TINT),
    ]
    cy = 1.5; card_h = 0.78; card_gap = 0.08
    for name, key, sub, color, fill in cards:
        ocean_box(s, 6.8, cy, 6.0, card_h, fill=fill, stroke=color)
        text_box(s, 7.0, cy + 0.05, 5.6, 0.26, name,
                 size=12.5, bold=True, color=color if color != GOLD else GOLD)
        text_box(s, 7.0, cy + 0.33, 5.6, 0.26, key,
                 size=11, bold=True, color=DEEP, line_spacing=1.0)
        text_box(s, 7.0, cy + 0.59, 5.6, 0.18, sub,
                 size=9, italic=True, color=MID, line_spacing=1.0)
        cy += card_h + card_gap

    # Caveat strip — ВЕГА-Science / ЕФИС ЗСН НЕ нейросети (честная оговорка, issue #340)
    caveat_y = cy + 0.06
    ocean_box(s, 6.8, caveat_y, 6.0, 0.42, fill=WHITE, stroke=SOFT_GREY, stroke_pt=1.0)
    text_box(s, 6.98, caveat_y + 0.03, 5.65, 0.36,
             "Рядом — ВЕГА-Science (индексный NDVI-метод) и Россельхознадзор/ЕФИС ЗСН "
             "(пороговые правила) — это не нейросети, хотя часто попадают в одну категорию «цифровизация АПК».",
             size=7.8, italic=True, color=DARK_GREY, line_spacing=1.1, anchor=MSO_ANCHOR.MIDDLE)

    # Bottom: AP6 inline political risk (height compressed slightly to keep layout inside budget)
    ap6_y = caveat_y + 0.42 + 0.1
    ocean_box(s, 0.6, ap6_y, 12.13, 0.62, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, 0.85, ap6_y + 0.06, 11.6, 0.26,
             "AP6 — Climate FieldView вышел из РФ в 2022",
             size=12, bold=True, color=GOLD)
    text_box(s, 0.85, ap6_y + 0.33, 11.6, 0.26,
             "Политический риск L1: облачные сервисы с зарубежной зависимостью могут отключиться по решению вендора или санкций.",
             size=9, color=DARK_GREY, italic=True, line_spacing=1.15)

    _s14_foot = text_runs(s, 0.5, 7.05, 12.33, 0.30, [
        {"text": "Источники: Яков и Партнёры 2024 · ExactFarming.com · TAdviser 2022 · "
                  "comnews.ru 2022-07-11 (Terra Tech) · фото: ", "size": 11, "italic": True, "color": LIGHT},
        {"text": "Vladislav Nekrasov, Wikimedia Commons, CC BY 4.0",
         "size": 11, "italic": True, "color": LIGHT},
    ], anchor=MSO_ANCHOR.MIDDLE)
    _s14_fruns = [r for p in _s14_foot.text_frame.paragraphs for r in p.runs]
    _s14_fruns[-1].font.underline = True
    _s14_fruns[-1].hyperlink.address = "https://commons.wikimedia.org/wiki/File:Колос_и_комбайн.jpg"

    add_speaker_notes(s, load_speaker_notes("s14"))

    return prs
