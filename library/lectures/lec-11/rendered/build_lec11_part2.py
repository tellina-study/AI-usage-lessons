"""Part 2: slides s13-s39 for lec-11."""
from pathlib import Path
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

from build_lec11 import (
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, DARK_GREY, RED_WARN, ROADMAP,
    blank, set_slide_bg, text_box, multiline_box, rounded_box,
    rectangle, circle, add_image, footer, attribution,
    section_divider, ASSETS, FONT_BODY,
)


def s13_section2_divider(p):
    section_divider(p, 2, "Дискретное производство",
                    "CV-инспекция · разметка · PdM · коботы · Tesla 2018 · границы",
                    "Раздел 2 · 17 мин · 9 слайдов")


def s14_cv_inspection(p):
    """s14 — three CV cases."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "CV-инспекция в production — три рабочих кейса",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "BMW · TSMC · Boeing — все три зависят от эталонной разметки",
             size=14, italic=True, color=LIGHT)
    cards = [
        ("BMW GenAI4Q", "Regensburg, 2025",
         ["Bespoke catalogue per vehicle", "FACTORY OF THE YEAR 2024", "Partner: Datagon AI"],
         "Каждый автомобиль — свой набор checkpoints", MID, "factory"),
        ("TSMC defect detection", "5nm / 3nm узлы",
         ["95% accuracy", "+10–15% yield", "Сотни миллионов $ в год"],
         "Самый зрелый CV-кейс в производстве чипов", TEAL, "cpu"),
        ("Boeing 737 fuselage", "декабрь 2025",
         ["Post-door-plug crisis", "Photo-driven part validation", "Дополнительный слой"],
         "CV-инспекция критических зон fuselage", GOLD, "shield-check"),
    ]
    card_w = 4.05
    gap = 0.1
    for i, (name, when, bullets, sub, color, icon) in enumerate(cards):
        x = 0.5 + i * (card_w + gap)
        y = 1.75
        rounded_box(slide, x, y, card_w, 4.6)
        rectangle(slide, x, y, card_w, 0.7, fill=color)
        text_box(slide, x, y + 0.05, card_w, 0.6, name,
                 size=17, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.15, y + 0.85, card_w - 0.3, 0.35, when,
                 size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
        # TSMC photo for middle card; icons for others
        if name.startswith("TSMC"):
            img_path = ASSETS / "screenshots" / "s14-tsmc.jpg"
            if img_path.exists():
                add_image(slide, img_path, x + 0.2, y + 1.3, card_w - 0.4, 1.5)
        else:
            # Icon centered
            icon_path = ASSETS / "icons" / f"{icon}.png"
            if icon_path.exists():
                add_image(slide, icon_path, x + card_w/2 - 0.6, y + 1.4, 1.2, 1.2)
        # Bullets
        for j, b in enumerate(bullets):
            text_box(slide, x + 0.25, y + 2.95 + j*0.32, card_w - 0.4, 0.3,
                     "· " + b, size=11, color=DEEP)
        # Sub
        rounded_box(slide, x + 0.2, y + 4.0, card_w - 0.4, 0.5,
                    fill=GOLD_TINT, stroke=GOLD)
        text_box(slide, x + 0.3, y + 4.05, card_w - 0.6, 0.4, sub,
                 size=10, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    # Bottom callout
    rounded_box(slide, 0.5, 6.5, 12.33, 0.55, fill=SURFACE, stroke=LIGHT)
    text_box(slide, 0.7, 6.55, 12.0, 0.5,
             "Общее: defect rate 1–2% → class imbalance → разметка — рычаг (s16)",
             size=13, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    attribution(slide, "BMW Press 2025 · TSMC · Boeing · Wikimedia CC-BY-SA")


def s15_boeing_737(p):
    """s15 — Boeing door plug anti-case."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "CV — последняя линия защиты, не первая",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Alaska Airlines 1282 · Boeing 737 MAX 9 · 5 января 2024",
             size=14, italic=True, color=LIGHT)
    # Photo left
    img_path = ASSETS / "screenshots" / "s15-alaska-737-max9.jpg"
    if img_path.exists():
        rounded_box(slide, 0.5, 1.75, 5.0, 4.2)
        add_image(slide, img_path, 0.65, 1.9, 4.7, 3.9)
        attribution(slide, "Alaska 737 MAX 9 N704AL · Wikimedia CC-BY-SA",
                    x=0.5, y=5.85, w=5.0)
    # Story right
    multiline_box(slide, 5.7, 1.75, 7.2, 5.0, [
        ("Что произошло", {"size": 16, "bold": True, "color": MID}),
        ("Высота 16 000 футов. Door plug — заглушка аварийного выхода — вылетела. Все 171 пассажир и 6 экипажа выжили.", {"size": 12, "color": DEEP}),
        ("", {"size": 8}),
        ("Причина", {"size": 16, "bold": True, "color": MID}),
        ("Механики Boeing Renton сняли door plug для ремонта рядом, не задокументировали, переустановили БЕЗ четырёх крепёжных болтов.", {"size": 12, "color": DEEP}),
        ("", {"size": 8}),
        ("Где была CV-инспекция", {"size": 16, "bold": True, "color": MID}),
        ("AI видит «дверь стоит на месте». Болты ЗАКРЫТЫ обшивкой — AI их физически не видит.", {"size": 12, "color": DEEP}),
        ("", {"size": 8}),
        ("Последствия", {"size": 16, "bold": True, "color": MID}),
        ("FAA cap 38/мес · Spirit AeroSystems — 50 fuselages rework · Everett задержан 12 мес · ~$1B+ direct", {"size": 12, "color": DEEP}),
    ], line_spacing=1.3)
    # Read-out-loud formula
    rounded_box(slide, 0.5, 6.45, 12.33, 0.55, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 6.5, 12.0, 0.45,
             "«CV — последняя линия защиты, не первая. Без upstream sign-off + audit trail AI не починит.»",
             size=14, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def s16_label_cost(p):
    """s16 — label cost vs data volume."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Эталонная разметка — дорого. Данные — дёшево.",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Первый критерий категории «данные» в §4 — есть ли разметка adequate volume",
             size=14, italic=True, color=LIGHT)
    # Left: cheap data
    rounded_box(slide, 0.5, 1.75, 6.0, 4.2, fill=SURFACE, stroke=LIGHT, stroke_w=2.0)
    text_box(slide, 0.7, 1.9, 5.6, 0.5, "ДЁШЕВО — сырые данные",
             size=16, bold=True, color=TEAL)
    multiline_box(slide, 0.85, 2.5, 5.4, 3.4, [
        ("Камеры записывают непрерывно:", {"size": 12, "bold": True, "color": DEEP}),
        ("· 10 ТБ изображений за смену", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Сенсоры IoT:", {"size": 12, "bold": True, "color": DEEP}),
        ("· Температура, давление, вибрация", {"size": 12, "color": DEEP}),
        ("· Гигабайты в день, копейки на ГБ", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("SCADA-архив:", {"size": 12, "bold": True, "color": DEEP}),
        ("· Storage стоит, но данные доступны", {"size": 12, "color": DEEP}),
    ], line_spacing=1.3)
    # Right: expensive labels
    rounded_box(slide, 6.7, 1.75, 6.13, 4.2, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 6.9, 1.9, 5.7, 0.5, "ДОРОГО — эталонная разметка",
             size=16, bold=True, color=GOLD)
    multiline_box(slide, 7.05, 2.5, 5.5, 3.4, [
        ("1 час domain-эксперта:", {"size": 12, "bold": True, "color": DEEP}),
        ("· 500–2000 ₽ в РФ / $50–200 на западе", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Размеченный пример рентгена сварного шва:", {"size": 12, "bold": True, "color": DEEP}),
        ("· 5–15 минут эксперта", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Class imbalance:", {"size": 12, "bold": True, "color": DEEP}),
        ("· Defect rate 1% → 1 дефект на 99 нормальных", {"size": 12, "color": DEEP}),
        ("· Для 1000 дефектов нужно ~100 000 примеров", {"size": 12, "color": DEEP}),
    ], line_spacing=1.3)
    # Bottom: alternatives
    rounded_box(slide, 0.5, 6.1, 12.33, 0.9, fill=SURFACE, stroke=LIGHT)
    text_box(slide, 0.7, 6.15, 12.0, 0.4, "Альтернативы (частично решают):",
             size=12, bold=True, color=MID)
    text_box(slide, 0.7, 6.5, 12.0, 0.5,
             "Synthetic data + transfer learning · Active learning · Rules-based + ML hybrid (rules ловят 70%, ML — оставшиеся 30%)",
             size=12, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)


def s17_pdm_oee(p):
    """s17 — PdM vendor vs reality + OEE callback."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "PdM на дискретном — vendor обещает, McKinsey говорит другое",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "«–25% downtime» ≠ «+25% OEE» — третий вопрос к вендору",
             size=14, italic=True, color=LIGHT)
    # Tata Steel photo top-left
    img_path = ASSETS / "screenshots" / "s17-tata-port-talbot.jpg"
    if img_path.exists():
        rounded_box(slide, 0.5, 1.7, 4.5, 2.4)
        add_image(slide, img_path, 0.65, 1.85, 4.2, 2.15)
        attribution(slide, "Tata Steel Port Talbot · Wikimedia",
                    x=0.5, y=4.05, w=4.5)
    # Vendor promises right
    rounded_box(slide, 5.2, 1.7, 7.6, 2.4, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 5.4, 1.85, 7.2, 0.4, "VENDOR ОБЕЩАЕТ:",
             size=13, bold=True, color=GOLD)
    multiline_box(slide, 5.4, 2.3, 7.2, 1.85, [
        ("Tata Steel: «–20% downtime, –15% maintenance cost»", {"size": 12, "color": DEEP}),
        ("BMW AIQX (2025): «realtime sensor + image fusion»", {"size": 12, "color": DEEP}),
        ("Generic vendors: «–25 до –40% downtime, –50 до –70% reactive maintenance»", {"size": 12, "color": DEEP}),
    ], line_spacing=1.5)
    # McKinsey reality
    rounded_box(slide, 0.5, 4.3, 12.33, 1.3, fill=SURFACE, stroke=MID, stroke_w=2.0)
    text_box(slide, 0.7, 4.4, 12.0, 0.4, "MCKINSEY 2025 REALITY CHECK:",
             size=13, bold=True, color=MID)
    multiline_box(slide, 0.7, 4.8, 12.0, 0.75, [
        ("«Большинство компаний пока не извлекают value от PdM-инвестиций» — прямая цитата.", {"size": 12, "italic": True, "color": DEEP}),
        ("ROI 8–14 мес — это best case, не среднее. Только 5,5% high performers извлекают EBIT-impact.", {"size": 12, "color": DEEP}),
    ], line_spacing=1.4)
    # OEE callback
    rounded_box(slide, 0.5, 5.75, 12.33, 1.3, fill=TEAL_TINT, stroke=TEAL, stroke_w=2.0)
    text_box(slide, 0.7, 5.85, 12.0, 0.4, "OEE CALLBACK — формула:",
             size=13, bold=True, color=TEAL)
    text_box(slide, 0.7, 6.25, 12.0, 0.4, "«–25% downtime ≠ +25% OEE»",
             size=18, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(slide, 0.7, 6.65, 12.0, 0.35,
             "OEE = доступность × производительность × качество. 3-й вопрос к вендору: какой компонент?",
             size=12, color=DEEP, align=PP_ALIGN.CENTER, italic=True)


def s18_cobots_jidoka(p):
    """s18 — cobots + Toyota Jidoka."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Коботы + Toyota Jidoka 2.0",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Augment, не replace — крупнейший auto OEM мира публично отрицает «AI заменяет людей»",
             size=14, italic=True, color=LIGHT)
    # 3 cards
    cards = [
        ("Hyundai + Boston Dynamics", "Spot для exterior QC", "Atlas humanoid — HMGMA, Georgia\nПервое коммерческое развёртывание гуманоида", MID, "cog"),
        ("Toyota GAIA", "8 000 (2023) → 10 000 (2024)", "AI-моделей создано сотрудниками,\nне data scientists. 10 000 часов saved/year", TEAL, "users"),
        ("Toyota Jidoka 2.0", "Официальная позиция", "«Goal of jidoka isn't to replace people\nbut to protect quality, expose issues, free people for judgment»", GOLD, "wrench"),
    ]
    card_w = 4.05
    gap = 0.1
    for i, (name, sub, body, color, icon) in enumerate(cards):
        x = 0.5 + i * (card_w + gap)
        y = 1.7
        rounded_box(slide, x, y, card_w, 4.6)
        rectangle(slide, x, y, card_w, 0.7, fill=color)
        text_box(slide, x, y + 0.05, card_w, 0.6, name,
                 size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.15, y + 0.85, card_w - 0.3, 0.4, sub,
                 size=12, italic=True, color=GOLD, align=PP_ALIGN.CENTER)
        # Icon centered
        icon_path = ASSETS / "icons" / f"{icon}.png"
        if icon_path.exists():
            add_image(slide, icon_path, x + card_w/2 - 0.9, y + 1.45, 1.8, 1.8)
        text_box(slide, x + 0.25, y + 3.6, card_w - 0.4, 0.9, body,
                 size=11, color=DEEP, line_spacing=1.35, align=PP_ALIGN.CENTER)
    # Bottom
    rounded_box(slide, 0.5, 6.45, 12.33, 0.55, fill=SURFACE, stroke=LIGHT, stroke_w=1.5)
    text_box(slide, 0.7, 6.5, 12.0, 0.45,
             "Резкий контраст с Tesla 2018: replace failed, augment работает с 1950-х на том же продукте",
             size=13, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def s19_tesla_2018(p):
    """s19 — Tesla 2018 canonical."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Tesla 2018 — канонический урок automation paradox",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Bainbridge 1983 + Toyota alternative + 2024 reMatch (gigacasting retreat)",
             size=14, italic=True, color=LIGHT)
    # Quote callout top
    rounded_box(slide, 0.5, 1.7, 12.33, 1.1, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 1.85, 12.0, 0.45,
             "13 апреля 2018, твит Маска:",
             size=12, bold=True, color=GOLD)
    text_box(slide, 0.7, 2.3, 12.0, 0.45,
             "«Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated.»",
             size=15, bold=True, italic=True, color=DEEP, align=PP_ALIGN.CENTER)
    # Three lessons grid
    lessons = [
        ("Q1 2018", "Target: 2 500 Model 3 / week\nРеально: 2 020", "Production hell. Маск спал на заводе", MID),
        ("Корневая причина (IMD)", "Tesla заменял людей там,\nгде variability — feature, не bug", "Сборка — miles of edge cases", TEAL),
        ("Bainbridge 1983", "«Ironies of Automation»:\nчем больше автоматизация, тем критичнее операторы", "Навык атрофируется — нештатная не отрабатывается", LIGHT),
    ]
    card_w = 4.05
    gap = 0.1
    for i, (title, body, sub, color) in enumerate(lessons):
        x = 0.5 + i * (card_w + gap)
        y = 3.0
        rounded_box(slide, x, y, card_w, 3.2)
        rectangle(slide, x, y, card_w, 0.6, fill=color)
        text_box(slide, x, y + 0.05, card_w, 0.5, title,
                 size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.2, y + 0.85, card_w - 0.4, 1.5, body,
                 size=12, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.35)
        rounded_box(slide, x + 0.2, y + 2.3, card_w - 0.4, 0.7,
                    fill=GOLD_TINT, stroke=GOLD)
        text_box(slide, x + 0.25, y + 2.35, card_w - 0.5, 0.6, sub,
                 size=11, italic=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Bottom: alternative
    rounded_box(slide, 0.5, 6.4, 12.33, 0.6, fill=TEAL_TINT, stroke=TEAL, stroke_w=2.0)
    text_box(slide, 0.7, 6.45, 12.0, 0.5,
             "Альтернатива: Toyota Production System + Jidoka — работает с 1950-х на том же продукте",
             size=13, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def s20_cv_limits(p):
    """s20 — CV limits + alternatives."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Границы CV-QC + альтернативы ДО ML",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Physical signal amplification → rules-based → ML на остатке",
             size=14, italic=True, color=LIGHT)
    # Left: where CV breaks
    rounded_box(slide, 0.5, 1.7, 5.9, 5.0, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 1.85, 5.5, 0.5, "ГДЕ CV ЛОМАЕТСЯ",
             size=16, bold=True, color=GOLD)
    multiline_box(slide, 0.85, 2.45, 5.4, 4.2, [
        ("Low-contrast defects", {"size": 13, "bold": True, "color": DEEP}),
        ("Микротрещина на алюминии при обычном освещении — невидима. Размытые границы, малая контрастность.", {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("Сдвиг распределения при смене продукта", {"size": 13, "bold": True, "color": DEEP}),
        ("Модель CV для модели A плохо работает на модели B. Заводы с 5+ моделями страдают.", {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("Scarce defect labels", {"size": 13, "bold": True, "color": DEEP}),
        ("Defect rate 1% + редкие типы → модель не видит rare defects (callback s16).", {"size": 11, "color": DEEP}),
    ], line_spacing=1.35)
    # Right: alternatives
    rounded_box(slide, 6.6, 1.7, 6.23, 5.0, fill=SURFACE, stroke=TEAL, stroke_w=2.0)
    text_box(slide, 6.8, 1.85, 5.8, 0.5, "АЛЬТЕРНАТИВЫ — ДО ML",
             size=16, bold=True, color=TEAL)
    multiline_box(slide, 6.95, 2.45, 5.7, 4.2, [
        ("Physical signal amplification:", {"size": 13, "bold": True, "color": MID}),
        ("· Структурированный свет — 3D-микрорельеф", {"size": 11, "color": DEEP}),
        ("· Поляризованный свет — стресс, scratches", {"size": 11, "color": DEEP}),
        ("· Рентген (X-ray) — внутренние дефекты", {"size": 11, "color": DEEP}),
        ("· Тепловидение — горячие точки", {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("Rules-based vision", {"size": 13, "bold": True, "color": MID}),
        ("Простые правила (площадь, контур, цвет). 60–70% inspection workloads в controlled env. Validated за неделю.", {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("Hybrid (рекомендуется):", {"size": 13, "bold": True, "color": GOLD}),
        ("Физика → rules → ML на остатке (10–20%)", {"size": 11, "italic": True, "color": DEEP}),
    ], line_spacing=1.35)


def s21_foxbrain(p):
    """s21 — Foxconn FoxBrain vendor self-claim + 3 questions."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "«80% configuration work» — vendor self-claim, не metric",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "Young Liu, Foxconn chairman, Computex май 2025 — LO2 hook",
             size=14, italic=True, color=LIGHT)
    # Quote big
    rounded_box(slide, 0.5, 1.65, 12.33, 1.4, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 1.85, 12.0, 0.6,
             "«After plugging AI tools into Foxconn's workflows, software now performs roughly 80 percent of the work required to configure equipment for a fresh production run.»",
             size=14, italic=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(slide, 0.7, 2.55, 12.0, 0.4,
             "— Young Liu, Foxconn chairman · Computex 2025",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    # 4 questions
    text_box(slide, 0.5, 3.2, 12.33, 0.5,
             "Четыре уточняющих вопроса к вендору (для кармана)",
             size=18, bold=True, color=MID, align=PP_ALIGN.CENTER)
    questions = [
        ("1", "Baseline до AI", "На какой объём работы сравниваете? Сколько FTE раньше?"),
        ("2", "Окно измерения", "Период оценки — день, неделя, месяц? Особый продукт или средний run?"),
        ("3", "Перечень вмешательств", "Какие AI-инструменты учтены в «80%»? Что автоматизировано, что — частично?"),
        ("4", "OEE-канал", "Availability (быстрее переход)? Performance (выше throughput)? Quality (меньше переделок)?"),
    ]
    q_w = 2.95
    q_gap = 0.1
    for i, (num, title, body) in enumerate(questions):
        x = 0.5 + i * (q_w + q_gap)
        y = 3.85
        rounded_box(slide, x, y, q_w, 3.0)
        circle(slide, x + q_w/2 - 0.4, y + 0.25, 0.8, 0.8, fill=GOLD)
        text_box(slide, x, y + 0.25, q_w, 0.8, num,
                 size=30, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.15, y + 1.15, q_w - 0.3, 0.5, title,
                 size=14, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(slide, x + 0.2, y + 1.75, q_w - 0.4, 1.2, body,
                 size=11, color=DARK_GREY, align=PP_ALIGN.CENTER, line_spacing=1.35)


def s22_discrete_matrix(p):
    """s22 — four failure types discrete."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Четыре типа провалов на дискретном",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Failure-pattern matrix — эмпирическая база для категорий §4",
             size=14, italic=True, color=LIGHT)
    types = [
        ("1. Чрезмерная автоматизация", "Tesla 2018", "Replace там, где variability = feature", "augment, не replace · Jidoka", MID),
        ("2. Сдвиг распределения", "CV модель A → B", "Заводы с 5+ моделями · смена поставщика", "план дообучения · rules-fallback", TEAL),
        ("3. Scarce labels + class imbalance", "Boeing 737 door-plug", "1 дефект на 10 000 · стоимость разметки", "physical signal · rules ДО ML", LIGHT),
        ("4. Vendor self-claim без baseline", "Foxconn «80%»", "Tata «–20% downtime» · BMW AIQX без OEE", "3 вопроса (baseline / окно / вмешательства) + OEE", GOLD),
    ]
    card_w = 6.05
    gap = 0.15
    for i, (name, case, where, lesson, color) in enumerate(types):
        col = i % 2
        row = i // 2
        x = 0.5 + col * (card_w + gap)
        y = 1.8 + row * 2.55
        rounded_box(slide, x, y, card_w, 2.4)
        rectangle(slide, x, y, 0.15, 2.4, fill=color)
        text_box(slide, x + 0.3, y + 0.15, card_w - 0.4, 0.4, name,
                 size=15, bold=True, color=DEEP)
        # Case badge
        rounded_box(slide, x + 0.3, y + 0.65, 2.5, 0.4, fill=GOLD_TINT, stroke=GOLD)
        text_box(slide, x + 0.35, y + 0.68, 2.4, 0.35, "Кейс: " + case,
                 size=11, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.3, y + 1.2, card_w - 0.4, 0.45,
                 "Где видно: " + where,
                 size=11, color=DARK_GREY, italic=True)
        text_box(slide, x + 0.3, y + 1.75, card_w - 0.4, 0.5,
                 "Урок: " + lesson,
                 size=12, bold=True, color=MID)
    footer(slide, "Эти четыре типа становятся критериями категорий «человек», «данные», «стоимость» в §4")


# ========== Section 3 ==========

def s23_section3_divider(p):
    section_divider(p, 3, "Процессное производство",
                    "Мягкие сенсоры · MPC/RL · регуляторика · РФ",
                    "Раздел 3 · 17 мин · 7 слайдов")


def s24_soft_sensors(p):
    """s24 — soft sensors BASF + Pfizer."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Мягкие сенсоры: BASF Geismar + Pfizer Vox",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Cornerstone процессного производства — software-модель вместо лабораторной пробы",
             size=14, italic=True, color=LIGHT)
    # BASF left
    img_path = ASSETS / "screenshots" / "s24-basf-ludwigshafen.jpg"
    rounded_box(slide, 0.5, 1.7, 6.0, 4.5)
    rectangle(slide, 0.5, 1.7, 6.0, 0.6, fill=MID)
    text_box(slide, 0.5, 1.75, 6.0, 0.5, "BASF Geismar · 2023–2024",
             size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if img_path.exists():
        add_image(slide, img_path, 0.7, 2.45, 5.6, 2.2)
        attribution(slide, "BASF Ludwigshafen · Wikimedia CC-BY-SA",
                    x=0.7, y=4.65, w=5.6)
    multiline_box(slide, 0.7, 5.05, 5.6, 1.1, [
        ("–30% batch defects", {"size": 16, "bold": True, "color": GOLD}),
        ("без увеличения тестирования", {"size": 12, "italic": True, "color": DEEP}),
        ("R&D formulation: 18 мес → 3 недели", {"size": 12, "color": DEEP}),
    ], line_spacing=1.3)
    # Pfizer right
    rounded_box(slide, 6.7, 1.7, 6.13, 4.5)
    rectangle(slide, 6.7, 1.7, 6.13, 0.6, fill=TEAL)
    text_box(slide, 6.7, 1.75, 6.13, 0.5, "Pfizer Vox · 2024–2025",
             size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Pfizer Vox — pill icon as illustrative
    pill_path = ASSETS / "icons" / "pill.png"
    if pill_path.exists():
        add_image(slide, pill_path, 9.0, 2.55, 1.5, 1.5)
    text_box(slide, 6.9, 4.1, 5.73, 0.4,
             "GenAI на AWS Bedrock + SageMaker",
             size=11, italic=True, color=DARK_GREY, align=PP_ALIGN.CENTER)
    multiline_box(slide, 6.9, 4.75, 5.73, 1.4, [
        ("+20 000 doses per batch", {"size": 16, "bold": True, "color": GOLD}),
        ("AWS Bedrock + SageMaker", {"size": 11, "italic": True, "color": SLATE}),
        ("«Recommend», не autonomous — FDA Part 11 consistent", {"size": 12, "color": DEEP}),
    ], line_spacing=1.35)
    # What is soft sensor + forward link
    rounded_box(slide, 0.5, 6.35, 12.33, 0.65, fill=SURFACE, stroke=LIGHT)
    text_box(slide, 0.7, 6.4, 12.0, 0.55,
             "Мягкий сенсор: оценивает труднoизмеряемые параметры по легкоизмеряемым (НЕ контроллер). Pfizer Vox станет worked example в §4.",
             size=12, color=DEEP, align=PP_ALIGN.CENTER, italic=True, anchor=MSO_ANCHOR.MIDDLE)


def s25_mpc_rl_cirl(p):
    """s25 — MPC / RL hybrid + CIRL diagram."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "MPC / RL гибрид + CIRL — RL расширяет PID, не замещает",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "Yokogawa-JSR FKDPP: 35 дней автономного RL · BASF CIRL: PID в loss function",
             size=14, italic=True, color=LIGHT)
    # Yokogawa photo top-left
    img_path = ASSETS / "screenshots" / "s25-yokogawa.jpg"
    rounded_box(slide, 0.5, 1.65, 4.0, 2.6)
    rectangle(slide, 0.5, 1.65, 4.0, 0.55, fill=MID)
    text_box(slide, 0.5, 1.7, 4.0, 0.5, "Yokogawa-JSR FKDPP",
             size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if img_path.exists():
        add_image(slide, img_path, 0.65, 2.35, 3.7, 1.5)
    text_box(slide, 0.65, 3.95, 3.7, 0.3,
             "35 дней (840 ч) автономного RL в distillation column · Japan PM Prize 2023",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    # CIRL diagram middle
    rounded_box(slide, 4.7, 1.65, 8.13, 2.6, fill=SURFACE, stroke=TEAL, stroke_w=2.0)
    text_box(slide, 4.9, 1.75, 7.9, 0.4, "CIRL architecture — BASF + Royal Academy of Engineering",
             size=13, bold=True, color=TEAL)
    # Diagram: PID box + RL box + arrow
    rectangle(slide, 5.1, 2.45, 1.8, 1.0, fill=MID)
    text_box(slide, 5.1, 2.55, 1.8, 0.8, "PID controller\n(baseline)\nдетерминированный",
             size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
    # arrow
    rectangle(slide, 7.1, 2.85, 1.0, 0.18, fill=GOLD)
    text_box(slide, 7.0, 3.05, 1.2, 0.3, "в loss",
             size=10, italic=True, color=GOLD, align=PP_ALIGN.CENTER)
    # RL box
    rectangle(slide, 8.3, 2.45, 4.3, 1.0, fill=TEAL)
    text_box(slide, 8.3, 2.55, 4.3, 0.8, "Deep RL\nучит policy с PID как baseline в loss function",
             size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)
    text_box(slide, 4.9, 3.65, 7.9, 0.55,
             "RL adds value в нелинейных зонах. В линейных автоматически совпадает с PID.",
             size=11, italic=True, color=DEEP, align=PP_ALIGN.CENTER)
    # Distinguish from naive interpretations
    rounded_box(slide, 0.5, 4.45, 12.33, 1.1, fill=GOLD_TINT, stroke=GOLD, stroke_w=1.5)
    multiline_box(slide, 0.7, 4.55, 12.0, 0.95, [
        ("Что НЕ есть CIRL:", {"size": 12, "bold": True, "color": GOLD}),
        ("✗ Не «RL вместо PID»  ✗ Не «два контура параллельно»  ✓ RL расширяет PID, не замещает", {"size": 13, "color": DEEP, "align": PP_ALIGN.CENTER}),
    ], line_spacing=1.35)
    # MPC as dominant safe-fallback
    rounded_box(slide, 0.5, 5.7, 12.33, 1.3, fill=TEAL_TINT, stroke=TEAL, stroke_w=2.0)
    multiline_box(slide, 0.7, 5.8, 12.0, 1.15, [
        ("MPC dominates process control:", {"size": 13, "bold": True, "color": TEAL}),
        ("Explicit model · объясним · валидируется регулятором · реагирует на drift автоматически.", {"size": 12, "color": DEEP}),
        ("Правило: RL дополняет MPC на high-level scheduling. На замыкании контура — MPC.", {"size": 12, "bold": True, "color": DEEP}),
    ], line_spacing=1.35)


def s26_rl_drift(p):
    """s26 — RL distribution drift 4 mechanisms."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "RL distribution drift — четыре механизма",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Когда policy, обученная на одном distribution, ломается без warning",
             size=14, italic=True, color=LIGHT)
    drifts = [
        ("1. Batch transitions", "OOD inputs", "RL обучен на steady-state. Переходный режим — out-of-distribution.\nСкачки температуры на старте нового batch.", MID),
        ("2. Смена feedstock", "Stale policy", "Состав сырья меняется. Policy на одном — stale на другом.\nНезаметно: на бумаге норма, качество дрейфует.", TEAL),
        ("3. Seasonal shifts", "Внешняя среда", "Зимняя температура vs летняя влияет на охлаждение.\n«Летом работал, осенью странности».", LIGHT),
        ("4. Equipment wear", "Дрейф объекта", "Катализатор стареет, теплообменник засоряется.\nRL не учится online без переподготовки.", GOLD),
    ]
    card_w = 6.05
    gap = 0.15
    for i, (name, badge, body, color) in enumerate(drifts):
        col = i % 2
        row = i // 2
        x = 0.5 + col * (card_w + gap)
        y = 1.8 + row * 2.3
        rounded_box(slide, x, y, card_w, 2.15)
        rectangle(slide, x, y, 0.15, 2.15, fill=color)
        text_box(slide, x + 0.3, y + 0.15, card_w - 0.4, 0.45, name,
                 size=15, bold=True, color=DEEP)
        rounded_box(slide, x + 0.3, y + 0.7, 2.0, 0.4, fill=GOLD_TINT, stroke=GOLD)
        text_box(slide, x + 0.35, y + 0.73, 1.9, 0.35, badge,
                 size=11, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.3, y + 1.2, card_w - 0.4, 0.9, body,
                 size=11, color=DEEP, line_spacing=1.35)
    # Safe-fallback
    rounded_box(slide, 0.5, 6.5, 12.33, 0.55, fill=TEAL_TINT, stroke=TEAL, stroke_w=2.0)
    text_box(slide, 0.7, 6.55, 12.0, 0.5,
             "Safe-fallback: MPC реагирует на текущие данные, не помнит обучения · MPC mandatory на замыкании контура",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def s27_edge_pdm(p):
    """s27 — edge AI + determinism."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Edge AI + детерминизм edge-вывода",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "POSCO 180 nodes · Holcim 100 plants · Latency = determinism, не только speed",
             size=14, italic=True, color=LIGHT)
    # POSCO left
    img_path = ASSETS / "screenshots" / "s27-posco-tower.jpg"
    rounded_box(slide, 0.5, 1.7, 4.0, 3.5)
    rectangle(slide, 0.5, 1.7, 4.0, 0.55, fill=MID)
    text_box(slide, 0.5, 1.75, 4.0, 0.5, "POSCO · Корея 2024",
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if img_path.exists():
        add_image(slide, img_path, 0.65, 2.4, 3.7, 1.8)
    multiline_box(slide, 0.65, 4.3, 3.7, 0.85, [
        ("180 edge nodes", {"size": 14, "bold": True, "color": GOLD, "align": PP_ALIGN.CENTER}),
        ("+5% efficiency · –10% energy · +3% yield", {"size": 10, "color": DEEP, "align": PP_ALIGN.CENTER}),
    ])
    attribution(slide, "POSCO Tower · Wikimedia", x=0.5, y=5.05, w=4.0)
    # Latency chart right
    chart_path = ASSETS / "charts" / "s27-latency-comparison.png"
    rounded_box(slide, 4.7, 1.7, 8.13, 3.5)
    text_box(slide, 4.9, 1.8, 7.7, 0.4,
             "Latency budget — три уровня:",
             size=13, bold=True, color=MID)
    if chart_path.exists():
        add_image(slide, chart_path, 4.9, 2.25, 7.7, 2.85)
    # Formula
    rounded_box(slide, 0.5, 5.35, 12.33, 0.75, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 5.42, 12.0, 0.65,
             "«Latency = determinism, не только speed»",
             size=18, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Bottom: F-35 ALIS callback
    rounded_box(slide, 0.5, 6.25, 12.33, 0.7, fill=SURFACE, stroke=LIGHT, stroke_w=1.5)
    text_box(slide, 0.7, 6.3, 12.0, 0.6,
             "F-35 ALIS callback (Лекция 9): $44 000/час, заменён ODIN. Defense PdM учит тому же, что промышленный.",
             size=12, italic=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def s28_regulatory(p):
    """s28 — regulatory blockers FDA + ATEX + Указ 250."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Регуляторные блокеры — три карты",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "FDA Part 11 · ATEX · Указ 250 — где AI упирается в сертификацию",
             size=14, italic=True, color=LIGHT)
    regs = [
        ("FDA 21 CFR Part 11", "Фарма, глобально",
         "Audit trail + validated systems + traceable changes.",
         "Black-box ML — нет audit trail.\nAI не может быть final decision-maker.\nHITL обязателен. GAMP®5 validation.",
         "Работает: prediction → operator approval.\nНе работает: autonomous batch release.", MID),
        ("ATEX / IECEx", "Взрывоопасные зоны",
         "Hardware certified для zones (0, 1, 2).",
         "Zone 0: non-certified AI hardware ФИЗИЧЕСКИ запрещён.\nНе вопрос ПО — вопрос hardware.",
         "AI помогает в predictive monitoring gas/temp/dust — не заменяет ATEX hardware.", TEAL),
        ("Указ № 250 (РФ)", "2022",
         "Защита критической информационной инфраструктуры (КИИ).",
         "Deploy AI в РФ-промышленности проходит через КИИ-обвязку.\nFZ-152 на КИИ. Импортозамещение к 2027.",
         "ГОСТ Р 57700.37-2021 (цифровые двойники) — foreshadow к Лекции 12.", GOLD),
    ]
    card_w = 4.05
    gap = 0.1
    for i, (name, scope, req, blocker, works, color) in enumerate(regs):
        x = 0.5 + i * (card_w + gap)
        y = 1.75
        rounded_box(slide, x, y, card_w, 5.0)
        rectangle(slide, x, y, card_w, 0.7, fill=color)
        text_box(slide, x, y + 0.05, card_w, 0.6, name,
                 size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.15, y + 0.85, card_w - 0.3, 0.35, scope,
                 size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
        text_box(slide, x + 0.2, y + 1.3, card_w - 0.4, 0.7, req,
                 size=11, bold=True, color=DEEP, line_spacing=1.3)
        rounded_box(slide, x + 0.2, y + 2.1, card_w - 0.4, 1.4,
                    fill=GOLD_TINT, stroke=GOLD)
        text_box(slide, x + 0.3, y + 2.15, card_w - 0.6, 1.3,
                 "БЛОКЕР:\n" + blocker,
                 size=10, color=DEEP, line_spacing=1.3)
        text_box(slide, x + 0.25, y + 3.65, card_w - 0.5, 1.2, works,
                 size=10, color=DARK_GREY, line_spacing=1.35, italic=True)
    # Bottom
    rounded_box(slide, 0.5, 6.85, 12.33, 0.15, fill=DEEP)


def s29_russian(p):
    """s29 — Russian context."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Российский контекст — публичные кейсы",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Норникель · СИБУР · кризис чёрной металлургии · LO2 — различать PR statement и effect",
             size=14, italic=True, color=LIGHT)
    # Nornickel left
    img_path = ASSETS / "screenshots" / "s29-nornickel.jpg"
    rounded_box(slide, 0.5, 1.7, 6.0, 3.5)
    rectangle(slide, 0.5, 1.7, 6.0, 0.55, fill=MID)
    text_box(slide, 0.5, 1.75, 6.0, 0.5, "Норникель — industrial-operation stage",
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if img_path.exists():
        add_image(slide, img_path, 0.7, 2.4, 5.6, 1.9)
    multiline_box(slide, 0.7, 4.45, 5.6, 0.7, [
        ("AI на flotation / grinding — не пилот, production", {"size": 11, "color": DEEP}),
        ("Нояб 2024: agreement с Газпром нефть", {"size": 11, "color": DEEP}),
    ], line_spacing=1.3)
    attribution(slide, "Nornickel's Bystrinsky Mine · Wikimedia CC-BY-SA",
                x=0.5, y=5.15, w=6.0)
    # Right column
    rounded_box(slide, 6.7, 1.7, 6.13, 3.5)
    rectangle(slide, 6.7, 1.7, 6.13, 0.55, fill=TEAL)
    text_box(slide, 6.7, 1.75, 6.13, 0.5, "СИБУР · ММК / НЛМК / Северсталь",
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 6.9, 2.4, 5.73, 2.7, [
        ("СИБУР Marketplace технологического моделирования", {"size": 13, "bold": True, "color": DEEP}),
        ("Q1 2025 → 2026 full · импортозамещение к 2027", {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("ММК / НЛМК / Северсталь", {"size": 13, "bold": True, "color": DEEP}),
        ("Общие декларации без specific metrics", {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("Параллельный кризис отрасли:", {"size": 12, "bold": True, "color": GOLD}),
        ("Severstal profit –55% в 2024", {"size": 11, "color": DEEP}),
    ], line_spacing=1.35)
    # Bottom: pedagogical point
    rounded_box(slide, 0.5, 5.55, 12.33, 1.45, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 5.65, 12.0, 0.4,
             "PEDAGOGICAL POINT (LO2):",
             size=13, bold=True, color=GOLD)
    multiline_box(slide, 0.7, 6.05, 12.0, 0.9, [
        ("Public-disclosure скудна — это анти-pattern в reporting, НЕ доказательство absence adoption.", {"size": 13, "bold": True, "color": DEEP}),
        ("Различать PR statement и измеримый эффект — LO2 в действии (symmetric для российских и западных вендоров).", {"size": 12, "italic": True, "color": DEEP}),
    ], line_spacing=1.35)


def s30_process_matrix(p):
    """s30 — four failure types process."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Четыре типа провалов на процессном",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Failure-pattern matrix — симметрично §2; основа для критериев §4",
             size=14, italic=True, color=LIGHT)
    types = [
        ("1. RL distribution drift", "Batch transitions / feedstock / сезон / wear",
         "Любая попытка autonomous RL без CIRL-обвязки",
         "RL дополняет MPC на high-level. MPC — safe fallback", TEAL),
        ("2. Regulatory blocker", "FDA Part 11 / ATEX Zone 0 / Указ 250 КИИ",
         "Фарма · химия в Zone 0 · РФ КИИ",
         "Регуляторика already exists. HITL + audit trail mandatory", MID),
        ("3. OT/IT раскол на uncertain edge", "LLM 100–500 мс ≠ PLC 1–10 мс",
         "Любая автоматизация L0–L1 ISA-95 через cloud",
         "Edge ML на копроцессоре, не LLM. Latency = determinism", LIGHT),
        ("4. Vendor PR без metrics", "Общие декларации без public-verifiable ROI",
         "Крупные публичные компании в кризисный квартал",
         "3 вопроса (baseline / окно / вмешательства). Уклончивый ответ — red flag", GOLD),
    ]
    card_w = 6.05
    gap = 0.15
    for i, (name, kasses, where, lesson, color) in enumerate(types):
        col = i % 2
        row = i // 2
        x = 0.5 + col * (card_w + gap)
        y = 1.8 + row * 2.55
        rounded_box(slide, x, y, card_w, 2.4)
        rectangle(slide, x, y, 0.15, 2.4, fill=color)
        text_box(slide, x + 0.3, y + 0.15, card_w - 0.4, 0.4, name,
                 size=15, bold=True, color=DEEP)
        rounded_box(slide, x + 0.3, y + 0.65, card_w - 0.5, 0.4,
                    fill=GOLD_TINT, stroke=GOLD)
        text_box(slide, x + 0.4, y + 0.68, card_w - 0.7, 0.35, "Кейсы: " + kasses,
                 size=10, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.3, y + 1.2, card_w - 0.4, 0.45,
                 "Где видно: " + where,
                 size=11, color=DARK_GREY, italic=True)
        text_box(slide, x + 0.3, y + 1.75, card_w - 0.4, 0.5,
                 "Урок: " + lesson,
                 size=12, bold=True, color=MID, line_spacing=1.3)


# ========== Section 4 ==========

def s31_section4_divider(p):
    section_divider(p, 4, "Карта решения — когда AI не нужен",
                    "4 категории · альтернативы · 5-step framework · Pfizer worked",
                    "Раздел 4 · 12 мин · PAYOFF лекции")


def s32_criteria(p):
    """s32 — four criteria categories."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Четыре категории критериев «AI не подходит»",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "Данные · Стоимость · Регуляторика · Человек — payoff лекции (LO8)",
             size=14, italic=True, color=LIGHT)
    cats = [
        ("A · Данные", "3 критерия",
         ["MTBF >1 года · недостаточно failures",
          "Известная физика · CFD/FEA лучше ML",
          "Эталонная разметка дорогая"],
         "physics-based sim · DOE · SPC", MID),
        ("B · Стоимость", "2 критерия",
         ["FP cost >10× FN · SPC лучше",
          "SIL 2/3 safety-critical · ML cert hard",
          ""],
         "SPC · RCM · rules-based", TEAL),
        ("C · Регуляторика", "3 критерия",
         ["Audit-trail обязателен (FDA, GAMP)",
          "ATEX Zone 0 · hardware restriction",
          "Указ 250 / КИИ"],
         "explainable ML · hybrid · on-premise", LIGHT),
        ("D · Человек", "3 критерия",
         ["Operator distrust → workaround",
          "Pilot без go-criteria · pilot purgatory",
          "Demo-hype без 6-mo production"],
         "Six Sigma · Jidoka · structured pilots", GOLD),
    ]
    card_w = 6.05
    gap = 0.15
    for i, (name, count, items, alts, color) in enumerate(cats):
        col = i % 2
        row = i // 2
        x = 0.5 + col * (card_w + gap)
        y = 1.7 + row * 2.55
        rounded_box(slide, x, y, card_w, 2.4)
        rectangle(slide, x, y, card_w, 0.55, fill=color)
        text_box(slide, x + 0.15, y + 0.05, card_w - 0.3, 0.45, name,
                 size=15, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.15, y + 0.05, card_w - 0.3, 0.45, count,
                 size=11, italic=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.RIGHT)
        # Items
        for j, item in enumerate(items):
            if item:
                text_box(slide, x + 0.25, y + 0.7 + j * 0.35, card_w - 0.5, 0.32,
                         "· " + item, size=11, color=DEEP)
        # Alts
        rounded_box(slide, x + 0.2, y + 1.85, card_w - 0.4, 0.5,
                    fill=GOLD_TINT, stroke=GOLD)
        text_box(slide, x + 0.3, y + 1.9, card_w - 0.6, 0.4,
                 "Альт-вы: " + alts,
                 size=10, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, italic=True)
    # Bottom: 4 vendor questions reminder
    rounded_box(slide, 0.5, 6.85, 12.33, 0.15, fill=DEEP)


def s33_alternatives(p):
    """s33 — alternatives matrix 6×5."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Матрица альтернатив — что использовать ДО ML",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "6 инструментов × 5 столбцов — каждый со своей нишей, regulatory friendly",
             size=14, italic=True, color=LIGHT)
    # Build matrix table
    cols = ["Инструмент", "Когда", "Сильные", "Слабые", "Reg-friendly"]
    rows = [
        ("SPC", "univariate, стабильные", "Дёшево, объяснимо, 100 лет", "Не multi-variate", "✓ FDA / GAMP / ISO"),
        ("DOE", "эксплорация, малые партии", "Causal inference", "Не online", "✓"),
        ("MPC", "process control, online", "Explicit model, reacts к drift", "Нужна точная модель", "✓"),
        ("RCM", "MTBF >1 года", "Объяснимый, calibrated", "Не learning", "✓"),
        ("Physics-sim", "известная физика", "Обобщается, CFD/FEA/kinetics", "Дорогая разработка", "✓"),
        ("Rules-vision", "controlled env", "Validated за неделю", "Не справляется с variability", "✓"),
    ]
    table_x = 0.5
    table_y = 1.65
    table_w = 12.33
    col_widths = [1.7, 2.3, 2.6, 2.6, 3.13]
    row_h = 0.55
    header_h = 0.45
    # Header
    rectangle(slide, table_x, table_y, table_w, header_h, fill=MID)
    cx = table_x
    for j, c in enumerate(cols):
        text_box(slide, cx, table_y + 0.05, col_widths[j], header_h - 0.1, c,
                 size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        cx += col_widths[j]
    # Rows
    for r, row in enumerate(rows):
        ry = table_y + header_h + r * row_h
        bg = SURFACE if r % 2 == 0 else WHITE
        rectangle(slide, table_x, ry, table_w, row_h, fill=bg)
        cx = table_x
        for j, val in enumerate(row):
            color = MID if j == 0 else DEEP
            bold = j == 0
            text_box(slide, cx + 0.1, ry + 0.05, col_widths[j] - 0.2, row_h - 0.1, val,
                     size=11, bold=bold, color=color, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)
            cx += col_widths[j]
    # Hybrid patterns row at bottom
    rounded_box(slide, 0.5, 5.4, 12.33, 1.6, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 5.5, 12.0, 0.4, "HYBRID PATTERNS — в одной строке:",
             size=13, bold=True, color=GOLD)
    multiline_box(slide, 0.7, 5.95, 12.0, 1.0, [
        ("PINN (Physics-Informed NN) — physics constraints в ML loss · CIRL — PID в loss function deep RL (BASF)", {"size": 12, "color": DEEP}),
        ("ML over SPC — статистический baseline + ML на остатке · PLC + edge ML coprocessor (POSCO pattern)", {"size": 12, "color": DEEP}),
    ], line_spacing=1.4)


def s34_pfizer_vox(p):
    """s34 — Pfizer Vox worked example."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Pfizer Vox через 5-step framework — worked example",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "Применяем framework ретроспективно — это готовый инструмент, не abstract theory",
             size=14, italic=True, color=LIGHT)
    steps = [
        ("STEP 1", "Identify class", "ПРОЦЕССНОЕ — continuous bioprocessing.\nmRNA-вакцины: batch process, непрерывный мониторинг.", MID),
        ("STEP 2", "Map alternatives", "SPC: univariate baseline (недостаточен)\nDOE: not suitable (online)\nMPC: control, не покрывает rare anomalies", TEAL),
        ("STEP 3", "Apply 4 cats", "Данные ✓ много batch data + разметка из QC\nСтоимость ✓ FP cost manageable\nРегул. ✓/✗ FDA → recommend mode\nЧеловек ✓ operators обучены", LIGHT),
        ("STEP 4", "Pilot + go-criteria", "+20 000 doses per batch — baseline известен.\nGo-criterion: baseline + ROI within 12 mo.", GOLD),
        ("STEP 5", "Production + HITL", "«Vox recommends actions to operators»\nArchitecture: decision-support, не controller.\nAudit trail для FDA Part 11 — satisfied.", DEEP),
    ]
    card_w = 2.42
    gap = 0.05
    for i, (label, name, body, color) in enumerate(steps):
        x = 0.5 + i * (card_w + gap)
        y = 1.7
        rounded_box(slide, x, y, card_w, 4.8)
        rectangle(slide, x, y, card_w, 0.55, fill=color)
        text_box(slide, x, y + 0.05, card_w, 0.45, label,
                 size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.1, y + 0.65, card_w - 0.2, 0.5, name,
                 size=14, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(slide, x + 0.2, y + 1.3, card_w - 0.4, 3.4, body,
                 size=11, color=DEEP, line_spacing=1.35)
    # Lesson at bottom
    rounded_box(slide, 0.5, 6.65, 12.33, 0.4, fill=GOLD_TINT, stroke=GOLD, stroke_w=1.5)
    text_box(slide, 0.7, 6.7, 12.0, 0.3,
             "Lesson: 5-step framework работает ретроспективно — готовый инструмент для оценки новых проектов",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, italic=True)


def s35_framework(p):
    """s35 — 5-step framework summary."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "5-step framework — ваш инструмент для кармана",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Пять шагов + четыре вопроса к вендору + гибридные паттерны",
             size=14, italic=True, color=LIGHT)
    # 5 steps as horizontal flow
    steps = [
        ("1", "Identify class", "discrete / process?\nкакая физика, регуляторика?"),
        ("2", "Map alternatives", "SPC / DOE / MPC / RCM /\nphysics-sim / rules-vision"),
        ("3", "Apply 4 categories", "Данные · Стоимость ·\nРегуляторика · Человек"),
        ("4", "Pilot + go-criteria", "baseline + measure window +\ngo/no-go threshold ДО старта"),
        ("5", "Production + HITL", "recommend mode safety-critical\nvalidated, traceable"),
    ]
    sw = 2.42
    sg = 0.06
    for i, (num, name, body) in enumerate(steps):
        x = 0.5 + i * (sw + sg)
        y = 1.7
        rounded_box(slide, x, y, sw, 2.6)
        circle(slide, x + sw/2 - 0.4, y + 0.25, 0.8, 0.8, fill=GOLD)
        text_box(slide, x, y + 0.25, sw, 0.8, num,
                 size=30, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.1, y + 1.15, sw - 0.2, 0.5, name,
                 size=14, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(slide, x + 0.15, y + 1.7, sw - 0.3, 0.8, body,
                 size=10, color=DARK_GREY, align=PP_ALIGN.CENTER, line_spacing=1.3)
        # Arrow to next
        if i < 4:
            tri = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,
                                          Inches(x + sw + 0.005),
                                          Inches(y + 1.0),
                                          Inches(0.05),
                                          Inches(0.4))
            tri.fill.solid()
            tri.fill.fore_color.rgb = GOLD
            tri.line.fill.background()
    # 4 vendor questions
    rounded_box(slide, 0.5, 4.5, 12.33, 2.5, fill=SURFACE, stroke=MID, stroke_w=2.0)
    text_box(slide, 0.7, 4.6, 12.0, 0.4, "ЧЕТЫРЕ ВОПРОСА К ВЕНДОРУ — для кармана",
             size=16, bold=True, color=MID, align=PP_ALIGN.CENTER)
    qs = [
        ("1", "Baseline до AI", "на какой объём сравниваете?"),
        ("2", "Окно измерения", "за какой период оценка?"),
        ("3", "Перечень вмешательств", "что реально автоматизировано?"),
        ("4", "OEE-канал", "availability / performance / quality?"),
    ]
    qw = 3.0
    qg = 0.06
    for i, (num, title, body) in enumerate(qs):
        x = 0.5 + i * (qw + qg)
        y = 5.15
        rounded_box(slide, x, y, qw, 1.7)
        text_box(slide, x, y + 0.1, qw, 0.5, num,
                 size=22, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
        text_box(slide, x + 0.1, y + 0.65, qw - 0.2, 0.4, title,
                 size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(slide, x + 0.15, y + 1.1, qw - 0.3, 0.55, body,
                 size=10, italic=True, color=DARK_GREY, align=PP_ALIGN.CENTER, line_spacing=1.3)


# ========== Section 5 ==========

def s36_section5_divider(p):
    section_divider(p, 5, "Замыкание",
                    "Recap · 5 вендор-вопросов · bridge к Лекции 12",
                    "Раздел 5 · 6 мин · 3 слайда")


def s37_recap(p):
    """s37 — recap + failure-callback."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Recap двухколонной схемы + failure-callback",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "Что мы разобрали — discrete | process | universal",
             size=14, italic=True, color=LIGHT)
    # Two columns recap
    col_y = 1.65
    col_h = 3.4
    col_w = 6.0
    rounded_box(slide, 0.5, col_y, col_w, col_h, fill=SURFACE, stroke=MID, stroke_w=1.5)
    rectangle(slide, 0.5, col_y, col_w, 0.5, fill=MID)
    text_box(slide, 0.5, col_y + 0.05, col_w, 0.4, "ДИСКРЕТНОЕ",
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 0.7, col_y + 0.6, col_w - 0.4, 2.8, [
        ("Инструменты:", {"size": 12, "bold": True, "color": MID}),
        ("CV (BMW + TSMC + Boeing) · разметка · PdM · коботы", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("Failure-урок:", {"size": 12, "bold": True, "color": GOLD}),
        ("чрезмерная автоматизация (Tesla 2018)", {"size": 11, "color": DEEP}),
        ("сдвиг распределения · scarce labels", {"size": 11, "color": DEEP}),
        ("vendor self-claim", {"size": 11, "color": DEEP}),
    ], line_spacing=1.3)
    rounded_box(slide, 6.83, col_y, col_w, col_h, fill=SURFACE, stroke=TEAL, stroke_w=1.5)
    rectangle(slide, 6.83, col_y, col_w, 0.5, fill=TEAL)
    text_box(slide, 6.83, col_y + 0.05, col_w, 0.4, "ПРОЦЕССНОЕ",
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 7.03, col_y + 0.6, col_w - 0.4, 2.8, [
        ("Инструменты:", {"size": 12, "bold": True, "color": TEAL}),
        ("мягкие сенсоры · MPC/RL/CIRL · PdM на edge · регуляторика", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("Failure-урок:", {"size": 12, "bold": True, "color": GOLD}),
        ("RL drift · regulatory blocker", {"size": 11, "color": DEEP}),
        ("OT-IT раскол · vendor PR", {"size": 11, "color": DEEP}),
    ], line_spacing=1.3)
    # Universal layer
    rounded_box(slide, 0.5, 5.15, 12.33, 0.8, fill=GOLD_TINT, stroke=GOLD, stroke_w=1.5)
    text_box(slide, 0.7, 5.2, 12.0, 0.35, "ОБЩИЙ СЛОЙ",
             size=12, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(slide, 0.7, 5.55, 12.0, 0.35,
             "Foundation models = augmentation, не controller · 95% не доходят до production · 4 категории + 5-step framework + 4 вопроса",
             size=11, color=DEEP, align=PP_ALIGN.CENTER, italic=True)
    # Callback formula
    rounded_box(slide, 0.5, 6.05, 12.33, 0.95, fill=DEEP)
    multiline_box(slide, 0.7, 6.15, 12.0, 0.85, [
        ("FAILURE-CALLBACK (формула):", {"size": 12, "bold": True, "color": GOLD, "align": PP_ALIGN.CENTER}),
        ("«Завтра вендор обещает –70% downtime — задайте 3 вопроса + 4-й OEE. Если расплывчатые ответы — это demo, не production.»", {"size": 13, "bold": True, "color": WHITE, "align": PP_ALIGN.CENTER, "italic": True}),
    ], line_spacing=1.3)


def s38_qa(p):
    """s38 — Q&A with 5 vendor questions + 3 typical."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Пять вопросов к вендору — для кармана",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Запишите на стикер, наклейте на монитор · работает на любом vendor pitch",
             size=14, italic=True, color=LIGHT)
    # 5 questions horizontal
    qs = [
        ("1", "Baseline до AI", "На какой объём работы / времени / стоимости сравниваете?"),
        ("2", "Окно измерения", "За какой период оценка — день, неделя, месяц?"),
        ("3", "Перечень вмешательств", "Какие AI-инструменты учтены? Что реально автоматизировано?"),
        ("4", "OEE-канал", "Availability / Performance / Quality — какой компонент?"),
        ("5", "Архитектурный класс", "Chat-помощник для оператора или autonomous controller?"),
    ]
    qw = 2.42
    qg = 0.05
    for i, (num, title, body) in enumerate(qs):
        x = 0.5 + i * (qw + qg)
        y = 1.7
        rounded_box(slide, x, y, qw, 2.7)
        circle(slide, x + qw/2 - 0.4, y + 0.2, 0.8, 0.8, fill=GOLD)
        text_box(slide, x, y + 0.2, qw, 0.8, num,
                 size=28, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.1, y + 1.1, qw - 0.2, 0.5, title,
                 size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(slide, x + 0.2, y + 1.6, qw - 0.4, 1.1, body,
                 size=10, color=DARK_GREY, align=PP_ALIGN.CENTER, line_spacing=1.3)
    # Typical student questions
    text_box(slide, 0.5, 4.65, 12.33, 0.5,
             "Типичные студенческие вопросы",
             size=18, bold=True, color=MID, align=PP_ALIGN.CENTER)
    typical = [
        ("«Мне говорят внедрить AI на нашем процессе, но я не уверен»",
         "Пройдите 5-step framework. Если хотя бы шаг не проходит — отчитайтесь руководству. Не запускайте pilot без go-criteria."),
        ("«SPC vs ML — что выбрать?»",
         "FDA + univariate → SPC. Multi-variate + recommend mode + audit trail → ML. Hybrid: SPC + ML over residuals — defensible перед регулятором."),
        ("«RL vs MPC — что лучше?»",
         "MPC dominates control loop. RL дополняет MPC на high-level scheduling. Safe-fallback к MPC mandatory."),
    ]
    for i, (q, a) in enumerate(typical):
        x = 0.5 + i * 4.15
        y = 5.25
        rounded_box(slide, x, y, 4.05, 1.7)
        text_box(slide, x + 0.15, y + 0.15, 3.75, 0.7, "Q. " + q,
                 size=11, bold=True, color=DEEP, italic=True, line_spacing=1.3)
        text_box(slide, x + 0.15, y + 0.85, 3.75, 0.8, "→ " + a,
                 size=10, color=DARK_GREY, line_spacing=1.3)


def s39_closing(p):
    """s39 — closing hero BMW digital twin."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    # Hero image left (50%+ area)
    img_path = ASSETS / "screenshots" / "s39-bmw-welt.jpg"
    if img_path.exists():
        add_image(slide, img_path, 0.5, 0.5, 6.5, 5.0)
    else:
        rectangle(slide, 0.5, 0.5, 6.5, 5.0, fill=SOFT_GREY)
        text_box(slide, 0.5, 2.5, 6.5, 0.6, "[BMW Werk + digital twin]",
                 size=16, color=SLATE, align=PP_ALIGN.CENTER)
    # Caption
    attribution(slide, "BMW Welt / Group · Wikimedia · BMW Digital Twin · NVIDIA GTC Paris 2025",
                x=0.5, y=5.6, w=6.5)
    # Bridge right
    multiline_box(slide, 7.3, 0.7, 5.7, 5.0, [
        ("Лекция 12 — bridge", {"size": 14, "italic": True, "color": GOLD}),
        ("Сшивка инструментов в", {"size": 26, "bold": True, "color": DEEP}),
        ("production-fabric", {"size": 26, "bold": True, "color": DEEP}),
        ("", {"size": 10}),
        ("Сегодня:", {"size": 14, "bold": True, "color": MID}),
        ("CV-инспекция, soft sensors, PdM, foundation models — отдельные инструменты.", {"size": 12, "color": DEEP}),
        ("", {"size": 8}),
        ("Лекция 12:", {"size": 14, "bold": True, "color": MID}),
        ("Цифровые двойники как унифицирующая абстракция · AI в автоматизации · ГОСТ Р 57700.37 в РФ.", {"size": 12, "color": DEEP}),
        ("", {"size": 8}),
        ("Параллели:", {"size": 14, "bold": True, "color": MID}),
        ("BMW 30+ plants · Holcim world-first cement DT · Foxconn-NVIDIA Omniverse", {"size": 12, "italic": True, "color": DARK_GREY}),
    ], line_spacing=1.2)
    # Closing strip bottom
    rounded_box(slide, 0.5, 6.05, 12.33, 1.0, fill=DEEP)
    text_box(slide, 0.7, 6.15, 12.0, 0.4,
             "Спасибо · Лекция 11 · AI в дискретном и процессном производстве",
             size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    text_box(slide, 0.7, 6.6, 12.0, 0.35,
             "Запомните 5 вопросов к вендору — это самая практическая вещь сегодня",
             size=12, italic=True, color=GOLD_TINT, align=PP_ALIGN.CENTER)
