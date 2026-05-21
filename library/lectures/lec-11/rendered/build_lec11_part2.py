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
                    "Машинное зрение · разметка · прогностическое обслуживание · коботы · Tesla 2018 · границы",
                    "Раздел 2 · 17 мин · 9 слайдов")


def s14_cv_inspection(p):
    """s14 — three CV cases."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Контроль качества зрением — три рабочих кейса",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "BMW · TSMC · Boeing — все три зависят от эталонной разметки",
             size=14, italic=True, color=LIGHT)
    cards = [
        ("BMW GenAI4Q", "Регенсбург, 2025",
         ["Индивидуальный каталог под автомобиль", "Премия «Factory of the Year» 2024", "Партнёр: Datagon AI"],
         "Каждый автомобиль — свой набор контрольных точек", MID, "factory"),
        ("TSMC — обнаружение дефектов", "5/3 нм технологии",
         ["95% точность на типичных AOI-линиях", "+10–15% выход годных", "Сотни млн $ в год"],
         "Иллюстративная оценка по индустрии, не TSMC IR", TEAL, "cpu"),
        ("Boeing 737 fuselage", "декабрь 2025",
         ["После кризиса door-plug", "Фото-проверка узлов", "Дополнительный слой контроля"],
         "Зрение для контроля критических зон фюзеляжа", GOLD, "shield-check"),
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
             "Общее: доля брака 1–2% → дисбаланс классов → эталонная разметка — критический рычаг",
             size=13, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    attribution(slide, "BMW Press 2025 · публикации индустрии · Boeing · Wikimedia CC-BY-SA")


def s15_boeing_737(p):
    """s15 — Boeing door plug anti-case."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Зрение — последняя линия защиты, не первая",
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
        ("Высота 16 000 футов. Заглушка аварийного выхода (door plug) вылетела. Все 171 пассажир и 6 членов экипажа выжили.", {"size": 12, "color": DEEP}),
        ("", {"size": 8}),
        ("Причина", {"size": 16, "bold": True, "color": MID}),
        ("Механики Boeing Renton сняли заглушку для ремонта рядом, не задокументировали, переустановили БЕЗ четырёх крепёжных болтов.", {"size": 12, "color": DEEP}),
        ("", {"size": 8}),
        ("Где была зрительная инспекция", {"size": 16, "bold": True, "color": MID}),
        ("AI видит «дверь стоит на месте». Болты ЗАКРЫТЫ обшивкой — AI их физически не видит.", {"size": 12, "color": DEEP}),
        ("", {"size": 8}),
        ("Последствия", {"size": 16, "bold": True, "color": MID}),
        ("Ограничение FAA: 38 самолётов/мес · Spirit AeroSystems — 50 фюзеляжей на доработку · Everett задержан 12 мес · прямые потери ~$1 млрд+", {"size": 12, "color": DEEP}),
    ], line_spacing=1.3)
    # Read-out-loud formula
    rounded_box(slide, 0.5, 6.45, 12.33, 0.55, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 6.5, 12.0, 0.45,
             "«Зрение — последняя линия защиты, не первая. Без формального подписания процедуры и журнала аудита AI ничего не починит.»",
             size=13, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def s16_label_cost(p):
    """s16 — label cost vs data volume."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Эталонная разметка — дорого. Данные — дёшево.",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Первый критерий категории «данные» — есть ли разметка нужного объёма",
             size=14, italic=True, color=LIGHT)
    # Left: cheap data
    rounded_box(slide, 0.5, 1.75, 6.0, 4.2, fill=SURFACE, stroke=LIGHT, stroke_w=2.0)
    text_box(slide, 0.7, 1.9, 5.6, 0.5, "ДЁШЕВО — сырые данные",
             size=16, bold=True, color=TEAL)
    multiline_box(slide, 0.85, 2.5, 5.4, 3.4, [
        ("Камеры записывают непрерывно:", {"size": 12, "bold": True, "color": DEEP}),
        ("· 10 ТБ изображений за смену", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Промышленные сенсоры:", {"size": 12, "bold": True, "color": DEEP}),
        ("· Температура, давление, вибрация", {"size": 12, "color": DEEP}),
        ("· Гигабайты в день, копейки за гигабайт", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Архив SCADA:", {"size": 12, "bold": True, "color": DEEP}),
        ("· Хранилище стоит, но данные доступны", {"size": 12, "color": DEEP}),
    ], line_spacing=1.3)
    # Right: expensive labels
    rounded_box(slide, 6.7, 1.75, 6.13, 4.2, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 6.9, 1.9, 5.7, 0.5, "ДОРОГО — эталонная разметка",
             size=16, bold=True, color=GOLD)
    multiline_box(slide, 7.05, 2.5, 5.5, 3.4, [
        ("1 час профильного эксперта:", {"size": 12, "bold": True, "color": DEEP}),
        ("· 500–2 000 ₽ в РФ / $50–200 на западе", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Размеченный пример рентгена сварного шва:", {"size": 12, "bold": True, "color": DEEP}),
        ("· 5–15 минут эксперта", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Дисбаланс классов:", {"size": 12, "bold": True, "color": DEEP}),
        ("· Доля брака 1% → 1 дефект на 99 нормальных", {"size": 12, "color": DEEP}),
        ("· Для 1 000 дефектов нужно ~100 000 примеров", {"size": 12, "color": DEEP}),
    ], line_spacing=1.3)
    # Bottom: alternatives
    rounded_box(slide, 0.5, 6.1, 12.33, 0.9, fill=SURFACE, stroke=LIGHT)
    text_box(slide, 0.7, 6.15, 12.0, 0.4, "Альтернативы (частично решают):",
             size=12, bold=True, color=MID)
    text_box(slide, 0.7, 6.5, 12.0, 0.5,
             "Синтетические данные + перенос обучения · Активное обучение · Гибрид правил и ML (правила ловят 70%, ML — оставшиеся 30%)",
             size=12, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)


def s17_pdm_oee(p):
    """s17 — PdM vendor vs reality + OEE callback."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Прогностическое обслуживание на дискретном — вендор обещает, McKinsey говорит другое",
             size=22, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "«–25% простоев» ≠ «+25% OEE» — третий вопрос к вендору",
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
    text_box(slide, 5.4, 1.85, 7.2, 0.4, "ВЕНДОР ОБЕЩАЕТ:",
             size=13, bold=True, color=GOLD)
    multiline_box(slide, 5.4, 2.3, 7.2, 1.85, [
        ("Tata Steel: «–20% простоев, –15% затрат на обслуживание»", {"size": 12, "color": DEEP}),
        ("BMW AIQX (2025): «слияние данных сенсоров и изображения в реальном времени»", {"size": 12, "color": DEEP}),
        ("Общие обещания вендоров: «от –25 до –40% простоев, от –50 до –70% реактивного ремонта»", {"size": 12, "color": DEEP}),
    ], line_spacing=1.5)
    # McKinsey reality
    rounded_box(slide, 0.5, 4.3, 12.33, 1.3, fill=SURFACE, stroke=MID, stroke_w=2.0)
    text_box(slide, 0.7, 4.4, 12.0, 0.4, "ПРОВЕРКА РЕАЛЬНОСТИ — McKinsey 2025:",
             size=13, bold=True, color=MID)
    multiline_box(slide, 0.7, 4.8, 12.0, 0.75, [
        ("«Большинство компаний пока не извлекают ценность из инвестиций в прогностическое обслуживание» — прямая цитата.", {"size": 12, "italic": True, "color": DEEP}),
        ("Окупаемость 8–14 мес — это лучший сценарий, не среднее. Только 5,5% с высокой результативностью получают прирост операционной прибыли.", {"size": 12, "color": DEEP}),
    ], line_spacing=1.4)
    # OEE callback
    rounded_box(slide, 0.5, 5.75, 12.33, 1.3, fill=TEAL_TINT, stroke=TEAL, stroke_w=2.0)
    text_box(slide, 0.7, 5.85, 12.0, 0.4, "Формула OEE:",
             size=13, bold=True, color=TEAL)
    text_box(slide, 0.7, 6.25, 12.0, 0.4, "«–25% простоев ≠ +25% OEE»",
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
             "Расширение, не замена — крупнейший автопроизводитель мира публично отрицает «AI заменяет людей»",
             size=14, italic=True, color=LIGHT)
    # 3 cards
    cards = [
        ("Hyundai + Boston Dynamics", "Spot для внешнего контроля качества", "Atlas — гуманоидный робот, центр RMAC (Robotics Manufacturing Application Center).\nПервое коммерческое развёртывание гуманоида.", MID, "cog"),
        ("Toyota GAIA", "8 000 (2023) → 10 000 (2024)", "AI-моделей создано рядовыми сотрудниками, не специалистами по данным.\n10 000 часов в год экономии (по заявлению Toyota — без независимого аудита).", TEAL, "users"),
        ("Toyota Jidoka 2.0", "Официальная позиция", "«Цель Jidoka — не заменить людей, а защитить качество, выявить проблемы и освободить людей для суждения.»", GOLD, "wrench"),
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
             "Резкий контраст с Tesla 2018: «заменить» провалилось, «расширить» работает с 1950-х на том же продукте",
             size=13, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def s19_tesla_2018(p):
    """s19 — Tesla 2018 canonical."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Tesla 2018 — канонический урок парадокса автоматизации",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Bainbridge 1983 + альтернатива Toyota + отступление от gigacasting в 2024",
             size=14, italic=True, color=LIGHT)
    # Quote callout top
    rounded_box(slide, 0.5, 1.7, 12.33, 1.1, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 1.85, 12.0, 0.45,
             "13 апреля 2018, твит Илона Маска:",
             size=12, bold=True, color=GOLD)
    text_box(slide, 0.7, 2.3, 12.0, 0.45,
             "«Да, чрезмерная автоматизация на Tesla была ошибкой. Точнее, моей ошибкой. Людей недооценивают.»",
             size=14, bold=True, italic=True, color=DEEP, align=PP_ALIGN.CENTER)
    # Three lessons grid
    lessons = [
        ("1 кв. 2018", "Цель: 2 500 Model 3 / неделя\nРеально: 2 020", "Производственный ад. Маск спал на заводе", MID),
        ("Корневая причина", "Tesla заменял людей там,\nгде вариативность — особенность, не дефект", "Сборка — мили краевых случаев", TEAL),
        ("Bainbridge 1983", "«Иронии автоматизации»:\nчем больше автоматизации, тем критичнее операторы", "Навык атрофируется — нештатная ситуация не отрабатывается", LIGHT),
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
    # Bottom: alternative + 2024 reMatch
    rounded_box(slide, 0.5, 6.4, 12.33, 0.6, fill=TEAL_TINT, stroke=TEAL, stroke_w=2.0)
    text_box(slide, 0.7, 6.45, 12.0, 0.5,
             "Альтернатива: производственная система Toyota + Jidoka — работает с 1950-х. Май 2024: Tesla отказалась от gigacasting нового поколения для Model 2.",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def s20_cv_limits(p):
    """s20 — CV limits + alternatives."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Границы контроля качества зрением + альтернативы ДО машинного обучения",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Физическое усиление сигнала → правила → ML на остатке",
             size=14, italic=True, color=LIGHT)
    # Left: where CV breaks
    rounded_box(slide, 0.5, 1.7, 5.9, 5.0, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 1.85, 5.5, 0.5, "ГДЕ ЗРЕНИЕ ЛОМАЕТСЯ",
             size=16, bold=True, color=GOLD)
    multiline_box(slide, 0.85, 2.45, 5.4, 4.2, [
        ("Малоконтрастные дефекты", {"size": 13, "bold": True, "color": DEEP}),
        ("Микротрещина на алюминии при обычном освещении — невидима. Размытые границы, малая контрастность.", {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("Сдвиг распределения при смене продукта", {"size": 13, "bold": True, "color": DEEP}),
        ("Модель зрения для модели A плохо работает на модели B. Заводы с 5+ моделями страдают.", {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("Редкие размеченные дефекты", {"size": 13, "bold": True, "color": DEEP}),
        ("Доля брака 1% + редкие типы → модель не видит редкие дефекты.", {"size": 11, "color": DEEP}),
    ], line_spacing=1.35)
    # Right: alternatives
    rounded_box(slide, 6.6, 1.7, 6.23, 5.0, fill=SURFACE, stroke=TEAL, stroke_w=2.0)
    text_box(slide, 6.8, 1.85, 5.8, 0.5, "АЛЬТЕРНАТИВЫ — ДО МЛ",
             size=16, bold=True, color=TEAL)
    multiline_box(slide, 6.95, 2.45, 5.7, 4.2, [
        ("Физическое усиление сигнала:", {"size": 13, "bold": True, "color": MID}),
        ("· Структурированный свет — 3D-микрорельеф", {"size": 11, "color": DEEP}),
        ("· Поляризованный свет — стресс, царапины", {"size": 11, "color": DEEP}),
        ("· Рентген — внутренние дефекты", {"size": 11, "color": DEEP}),
        ("· Тепловидение — горячие точки", {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("Правило-ориентированное зрение:", {"size": 13, "bold": True, "color": MID}),
        ("Простые правила (площадь, контур, цвет). 60–70% задач инспекции в контролируемой среде. Валидируется за неделю.", {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("Гибрид (рекомендуется):", {"size": 13, "bold": True, "color": GOLD}),
        ("Физика → правила → ML на остатке (10–20%)", {"size": 11, "italic": True, "color": DEEP}),
    ], line_spacing=1.35)


def s21_foxbrain(p):
    """s21 — Foxconn FoxBrain vendor self-claim + 4 questions."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "«80% работы по настройке» — заявление вендора, не измеренный показатель",
             size=22, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "Янг Лиу, председатель Foxconn, Computex, май 2025 — упражнение в критической оценке",
             size=14, italic=True, color=LIGHT)
    # Quote big — RU primary
    rounded_box(slide, 0.5, 1.65, 12.33, 1.4, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 1.8, 12.0, 0.55,
             "«После подключения AI-инструментов в рабочие процессы Foxconn софт сейчас выполняет около 80 процентов работы по настройке оборудования к новому производственному запуску.»",
             size=14, italic=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(slide, 0.7, 2.55, 12.0, 0.4,
             "— Янг Лиу, председатель Foxconn · Computex, май 2025",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    # 4 questions
    text_box(slide, 0.5, 3.2, 12.33, 0.5,
             "Четыре уточняющих вопроса к вендору (для кармана)",
             size=18, bold=True, color=MID, align=PP_ALIGN.CENTER)
    questions = [
        ("1", "Базовая линия до AI", "На какой объём работы сравниваете? Сколько сотрудников было раньше?"),
        ("2", "Окно измерения", "Период оценки — день, неделя, месяц? Особый продукт или средний запуск?"),
        ("3", "Перечень вмешательств", "Какие AI-инструменты учтены в «80%»? Что автоматизировано, что — частично?"),
        ("4", "Канал OEE", "Доступность (быстрее переход)? Производительность (выше пропуск)? Качество (меньше переделок)?"),
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
             "Матрица типов провалов — эмпирическая база для рамки решения",
             size=14, italic=True, color=LIGHT)
    types = [
        ("1. Чрезмерная автоматизация", "Tesla 2018", "Замена там, где вариативность = особенность", "Расширять, а не заменять · Jidoka", MID),
        ("2. Сдвиг распределения", "CV модель A → B", "Заводы с 5+ моделями · смена поставщика", "План дообучения · откат на правила", TEAL),
        ("3. Редкая разметка + дисбаланс классов", "Boeing 737 — дверная заглушка", "1 дефект на 10 000 · стоимость разметки", "Физический сигнал · правила ДО ML", LIGHT),
        ("4. Заявление вендора без базовой линии", "Foxconn «80%»", "Tata «–20% простоев» · BMW AIQX без OEE", "3 вопроса (базовая линия / окно / вмешательства) + OEE", GOLD),
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
    footer(slide, "Эти четыре типа становятся критериями категорий «человек», «данные», «стоимость» в рамке решения")


# ========== Section 3 ==========

def s23_section3_divider(p):
    section_divider(p, 3, "Процессное производство",
                    "Мягкие сенсоры · MPC/RL · регуляторика · российский контекст",
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
        ("–30% дефектов в партии", {"size": 16, "bold": True, "color": GOLD}),
        ("без увеличения тестирования", {"size": 12, "italic": True, "color": DEEP}),
        ("Разработка рецептуры: 18 мес → 3 недели", {"size": 12, "color": DEEP}),
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
             "Генеративный AI на платформах AWS Bedrock + SageMaker",
             size=11, italic=True, color=DARK_GREY, align=PP_ALIGN.CENTER)
    multiline_box(slide, 6.9, 4.75, 5.73, 1.4, [
        ("+20 000 доз на партию", {"size": 16, "bold": True, "color": GOLD}),
        ("AWS Bedrock + SageMaker", {"size": 11, "italic": True, "color": SLATE}),
        ("Режим «характеристика», не автономный — совместим с FDA Part 11", {"size": 11, "color": DEEP}),
    ], line_spacing=1.35)
    # What is soft sensor + forward link
    rounded_box(slide, 0.5, 6.35, 12.33, 0.65, fill=SURFACE, stroke=LIGHT)
    text_box(slide, 0.7, 6.4, 12.0, 0.55,
             "Мягкий сенсор: оценивает труднoизмеряемые параметры по легкоизмеряемым (НЕ контроллер). Pfizer Vox станет разобранным примером для рамки решения.",
             size=12, color=DEEP, align=PP_ALIGN.CENTER, italic=True, anchor=MSO_ANCHOR.MIDDLE)


def s25_mpc_rl_cirl(p):
    """s25 — MPC / RL hybrid + CIRL diagram."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Гибрид MPC/RL + CIRL — обучение с подкреплением расширяет PID, не замещает",
             size=22, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "Yokogawa-JSR FKDPP: 35 дней автономного RL · BASF CIRL: PID-контроллер в функции потерь",
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
             "35 дней (840 ч) автономного RL в дистилляционной колонне · Премия PM Японии 2023",
             size=10, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    # CIRL diagram middle — simplified with explicit annotation (P1-16)
    rounded_box(slide, 4.7, 1.65, 8.13, 2.6, fill=SURFACE, stroke=TEAL, stroke_w=2.0)
    text_box(slide, 4.9, 1.75, 7.9, 0.4, "Архитектура CIRL — BASF + Royal Academy of Engineering",
             size=13, bold=True, color=TEAL)
    # Simplified diagram: PID inside RL (not parallel)
    rectangle(slide, 5.1, 2.45, 7.7, 1.4, fill=TEAL)
    text_box(slide, 5.1, 2.55, 7.7, 0.4, "Глубокое обучение с подкреплением (RL)",
             size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    # PID box INSIDE RL
    rectangle(slide, 7.5, 2.95, 2.9, 0.75, fill=MID)
    text_box(slide, 7.5, 3.0, 2.9, 0.65, "PID-контроллер\nв функции потерь",
             size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.2)
    text_box(slide, 4.9, 3.9, 7.9, 0.3,
             "PID внутри RL, не вместо PID и не параллельно — это ключевое различие CIRL.",
             size=11, italic=True, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    # Distinguish from naive interpretations
    rounded_box(slide, 0.5, 4.45, 12.33, 1.1, fill=GOLD_TINT, stroke=GOLD, stroke_w=1.5)
    multiline_box(slide, 0.7, 4.55, 12.0, 0.95, [
        ("Что НЕ есть CIRL:", {"size": 12, "bold": True, "color": GOLD}),
        ("✗ Не «RL вместо PID»  ✗ Не «два контура параллельно»  ✓ RL расширяет PID, не замещает", {"size": 13, "color": DEEP, "align": PP_ALIGN.CENTER}),
    ], line_spacing=1.35)
    # MPC as dominant safe-fallback
    rounded_box(slide, 0.5, 5.7, 12.33, 1.3, fill=TEAL_TINT, stroke=TEAL, stroke_w=2.0)
    multiline_box(slide, 0.7, 5.8, 12.0, 1.15, [
        ("MPC доминирует в управлении процессом:", {"size": 13, "bold": True, "color": TEAL}),
        ("Явная модель · объясним · валидируется регулятором · автоматически реагирует на дрейф.", {"size": 12, "color": DEEP}),
        ("Правило: RL дополняет MPC на верхнеуровневом планировании. На замыкании контура — MPC.", {"size": 12, "bold": True, "color": DEEP}),
    ], line_spacing=1.35)


def s26_rl_drift(p):
    """s26 — RL distribution drift 4 mechanisms."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Дрейф распределения данных в RL — четыре механизма",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Когда стратегия (policy), обученная на одном распределении данных, ломается без предупреждения",
             size=14, italic=True, color=LIGHT)
    drifts = [
        ("1. Переходы между партиями", "Данные вне обучения", "RL обучен на стационарном режиме. Переходный режим — вне распределения обучения.\nСкачки температуры на старте новой партии.", MID),
        ("2. Смена сырья", "Устаревшая стратегия", "Состав сырья меняется. Стратегия на одном составе — устарела для другого.\nНезаметно: на бумаге норма, качество дрейфует.", TEAL),
        ("3. Сезонные сдвиги", "Внешняя среда", "Зимняя температура против летней влияет на охлаждение.\n«Летом работал, осенью странности».", LIGHT),
        ("4. Износ оборудования", "Дрейф объекта", "Катализатор стареет, теплообменник засоряется.\nRL не учится в реальном времени без переподготовки.", GOLD),
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
             "Безопасный откат: MPC реагирует на текущие данные, не помнит обучения · MPC обязателен на замыкании контура",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def s27_edge_pdm(p):
    """s27 — edge AI + determinism."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "AI на крае сети (edge) + детерминизм edge-вывода",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "POSCO — 180 узлов на крае · Holcim — 100 заводов · Задержка = детерминизм, не только скорость",
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
        ("180 edge-узлов", {"size": 14, "bold": True, "color": GOLD, "align": PP_ALIGN.CENTER}),
        ("+5% эффективность · –10% энергия · +3% выход годных", {"size": 10, "color": DEEP, "align": PP_ALIGN.CENTER}),
    ])
    attribution(slide, "POSCO Tower · Wikimedia", x=0.5, y=5.05, w=4.0)
    # Latency chart right
    chart_path = ASSETS / "charts" / "s27-latency-comparison.png"
    rounded_box(slide, 4.7, 1.7, 8.13, 3.5)
    text_box(slide, 4.9, 1.8, 7.7, 0.4,
             "Бюджет задержки — три уровня:",
             size=13, bold=True, color=MID)
    if chart_path.exists():
        add_image(slide, chart_path, 4.9, 2.25, 7.7, 2.85)
    # Formula
    rounded_box(slide, 0.5, 5.35, 12.33, 0.75, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 5.42, 12.0, 0.65,
             "«Задержка = детерминизм, не только скорость»",
             size=18, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Bottom: F-35 ALIS parallel (canonical lesson)
    rounded_box(slide, 0.5, 6.25, 12.33, 0.7, fill=SURFACE, stroke=LIGHT, stroke_w=1.5)
    text_box(slide, 0.7, 6.3, 12.0, 0.6,
             "Параллель из обороны: F-35 ALIS — $44 000/час, заменён системой ODIN. Прогностическое обслуживание учит тому же, что и в промышленности.",
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
         "Журнал аудита + валидированные системы + прослеживаемые изменения.",
         "Чёрный ящик ML — нет журнала аудита.\nAI не может быть конечным принимающим решение.\nЧеловек в цикле (HITL) обязателен. Валидация GAMP®5.",
         "Работает: предсказание → одобрение оператора.\nНе работает: автономный выпуск партии.", MID),
        ("ATEX / IECEx", "Взрывоопасные зоны",
         "Оборудование сертифицировано для зон (0, 1, 2).",
         "Зона 0: несертифицированное AI-оборудование ФИЗИЧЕСКИ запрещено.\nНе вопрос ПО — вопрос оборудования.",
         "AI помогает в прогностическом мониторинге газа/температуры/пыли — не заменяет ATEX-оборудование.", TEAL),
        ("Указ № 250 (РФ)", "2022",
         "Защита критической информационной инфраструктуры (КИИ).",
         "Развёртывание AI в РФ-промышленности проходит через КИИ-обвязку.\nФЗ-152 на КИИ. Импортозамещение к 2027.",
         "ГОСТ Р 57700.37-2021 (цифровые двойники) — переход к Лекции 12.", GOLD),
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
    """s29 — Russian context. Honest hedge на Норникель + separate caveat для Газпром нефти."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Российский контекст — публичные кейсы",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Норникель · СИБУР · кризис чёрной металлургии — различать заявления и измеримый эффект",
             size=14, italic=True, color=LIGHT)
    # Nornickel left — honest hedge
    img_path = ASSETS / "screenshots" / "s29-nornickel.jpg"
    rounded_box(slide, 0.5, 1.7, 6.0, 3.5)
    rectangle(slide, 0.5, 1.7, 6.0, 0.55, fill=MID)
    text_box(slide, 0.5, 1.75, 6.0, 0.5, "Норникель — пилот / ранняя пром. стадия",
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if img_path.exists():
        add_image(slide, img_path, 0.7, 2.4, 5.6, 1.9)
    multiline_box(slide, 0.7, 4.4, 5.6, 0.75, [
        ("AI на флотации / измельчении — заявлена пилотная / ранняя промышленная стадия", {"size": 11, "color": DEEP}),
        ("Точные метрики (OEE-критерий с SLA >12 мес) публично не верифицируемы", {"size": 11, "italic": True, "color": DARK_GREY}),
    ], line_spacing=1.3)
    attribution(slide, "Быстринский ГОК · Норникель · Wikimedia CC-BY-SA",
                x=0.5, y=5.15, w=6.0)
    # Right column
    rounded_box(slide, 6.7, 1.7, 6.13, 3.5)
    rectangle(slide, 6.7, 1.7, 6.13, 0.55, fill=TEAL)
    text_box(slide, 6.7, 1.75, 6.13, 0.5, "СИБУР · ММК / НЛМК / Северсталь",
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 6.9, 2.4, 5.73, 2.7, [
        ("СИБУР — площадка технологического моделирования", {"size": 13, "bold": True, "color": DEEP}),
        ("1 квартал 2025 → полный запуск 2026 · импортозамещение к 2027", {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("ММК / НЛМК / Северсталь", {"size": 13, "bold": True, "color": DEEP}),
        ("Общие декларации без конкретных измеримых показателей", {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("Параллельный кризис отрасли:", {"size": 12, "bold": True, "color": GOLD}),
        ("Прибыль Северстали в 2024 г. –55%", {"size": 11, "color": DEEP}),
    ], line_spacing=1.35)
    # Газпром нефть separation caveat
    rounded_box(slide, 0.5, 5.3, 12.33, 0.4, fill=SURFACE, stroke=LIGHT, stroke_w=1.0)
    text_box(slide, 0.7, 5.33, 12.0, 0.35,
             "Газпром нефть «Северо-Соленинское» — отдельный кейс другой компании, не Норникель",
             size=11, italic=True, color=DARK_GREY, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Bottom: pedagogical point
    rounded_box(slide, 0.5, 5.8, 12.33, 1.2, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 5.9, 12.0, 0.4,
             "Главный методический вывод:",
             size=13, bold=True, color=GOLD)
    multiline_box(slide, 0.7, 6.25, 12.0, 0.75, [
        ("Скудность публичного раскрытия — антипаттерн в отчётности, НЕ доказательство отсутствия применения.", {"size": 12, "bold": True, "color": DEEP}),
        ("Различать заявление для прессы и измеримый эффект — симметрично для российских и западных вендоров.", {"size": 11, "italic": True, "color": DEEP}),
    ], line_spacing=1.3)


def s30_process_matrix(p):
    """s30 — four failure types process."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Четыре типа провалов на процессном",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Матрица типов провалов — симметрично дискретному; основа для критериев рамки решения",
             size=14, italic=True, color=LIGHT)
    types = [
        ("1. Дрейф распределения в RL", "Переходы партий / смена сырья / сезон / износ",
         "Любая попытка автономного RL без CIRL-обвязки",
         "RL дополняет MPC на верхнем уровне. MPC — безопасный откат", TEAL),
        ("2. Регуляторный блокер", "FDA Part 11 / ATEX Зона 0 / Указ 250 КИИ",
         "Фарма · химия в Зоне 0 · РФ КИИ",
         "Регуляторика уже существует. Человек в цикле + журнал аудита обязательны", MID),
        ("3. OT/IT раскол на нечётком крае", "LLM 100–500 мс ≠ PLC 1–10 мс",
         "Любая автоматизация L0–L1 ISA-95 через облако",
         "ML на крае сети, на копроцессоре — не LLM. Задержка = детерминизм", LIGHT),
        ("4. PR вендора без показателей", "Общие декларации без публично проверяемой окупаемости",
         "Крупные публичные компании в кризисный квартал",
         "3 вопроса (база / окно / вмешательства). Уклончивый ответ — красный флаг", GOLD),
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
                    "4 категории · альтернативы · 5-шаговая рамка · разобранный пример Pfizer",
                    "Раздел 4 · 12 мин · 6 слайдов")


def s32_criteria(p):
    """s32 — four criteria categories: 3 + 2 + 3 + 2 = 10 критериев + 1 бонус."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Четыре категории критериев «AI не подходит»",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "Данные · Стоимость · Регуляторика · Человек — 10 критериев + 1 бонус",
             size=14, italic=True, color=LIGHT)
    cats = [
        ("A · Данные", "3 критерия",
         ["Средняя наработка на отказ >1 года — слишком мало отказов",
          "Известная физика — CFD/FEA лучше ML",
          "Эталонная разметка дорогая"],
         "Физические симуляции · план эксперимента (DOE) · статистический контроль (SPC)", MID),
        ("B · Стоимость", "2 критерия",
         ["Цена ложного срабатывания > 10× цены пропуска — SPC лучше",
          "Критичный по безопасности контур — сертификация ML сложна",
          ""],
         "SPC · надёжностно-ориентированное обслуживание (RCM) · правило-ориентированные системы", TEAL),
        ("C · Регуляторика", "3 критерия",
         ["Журнал аудита обязателен (FDA, GAMP)",
          "Взрывоопасная зона 0 (ATEX) — ограничения на оборудование",
          "Указ 250 / критическая инфраструктура (КИИ)"],
         "Объяснимый ML · гибридные подходы · развёртывание на собственной инфраструктуре", LIGHT),
        ("D · Человек", "2 критерия",
         ["Недоверие оператора → обходные пути",
          "Пилот без критериев успеха → застревание на пилотной стадии",
          ""],
         "Six Sigma · Jidoka · структурированные пилоты", GOLD),
    ]
    card_w = 6.05
    gap = 0.15
    for i, (name, count, items, alts, color) in enumerate(cats):
        col = i % 2
        row = i // 2
        x = 0.5 + col * (card_w + gap)
        y = 1.7 + row * 2.4
        rounded_box(slide, x, y, card_w, 2.3)
        rectangle(slide, x, y, card_w, 0.45, fill=color)
        text_box(slide, x + 0.15, y + 0.05, card_w - 0.3, 0.4, name,
                 size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.15, y + 0.05, card_w - 0.3, 0.4, count,
                 size=10, italic=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.RIGHT)
        # Items
        for j, item in enumerate(items):
            if item:
                text_box(slide, x + 0.25, y + 0.55 + j * 0.4, card_w - 0.5, 0.38,
                         "· " + item, size=11, color=DEEP, line_spacing=1.2)
        # Alts
        rounded_box(slide, x + 0.2, y + 1.78, card_w - 0.4, 0.45,
                    fill=GOLD_TINT, stroke=GOLD)
        text_box(slide, x + 0.3, y + 1.82, card_w - 0.6, 0.4,
                 "Альтернативы: " + alts,
                 size=9, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, italic=True)
    # Bonus criterion
    rounded_box(slide, 0.5, 6.6, 12.33, 0.4, fill=GOLD_TINT, stroke=GOLD, stroke_w=1.5)
    text_box(slide, 0.7, 6.63, 12.0, 0.35,
             "БОНУС · 11-й критерий: уровень функциональной безопасности SIL 2/3 — сертификация чёрного ящика ML практически нереализуема",
             size=11, italic=True, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def s33_alternatives(p):
    """s33 — alternatives matrix 6×5."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Матрица альтернатив — что использовать ДО машинного обучения",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "6 инструментов × 5 столбцов — каждый со своей нишей, дружественны регулятору",
             size=14, italic=True, color=LIGHT)
    # Build matrix table
    cols = ["Инструмент", "Когда применять", "Сильные стороны", "Слабые стороны", "Дружественно регулятору"]
    rows = [
        ("SPC", "Один параметр, стабильно", "Дёшево, объяснимо, 100 лет", "Не работает с многомерными", "✓ FDA / GAMP / ISO"),
        ("DOE", "Эксплорация, малые партии", "Причинно-следственный вывод", "Не онлайн", "✓"),
        ("MPC", "Управление процессом онлайн", "Явная модель, реагирует на дрейф", "Нужна точная модель", "✓"),
        ("RCM", "MTBF >1 года", "Объяснимый, откалиброванный", "Не учится", "✓"),
        ("Физ.симуляция", "Известная физика", "Обобщается, CFD/FEA/кинетика", "Дорогая разработка", "✓"),
        ("Зрение на правилах", "Контролируемая среда", "Валидируется за неделю", "Не справляется с вариативностью", "✓"),
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
    text_box(slide, 0.7, 5.5, 12.0, 0.4, "ГИБРИДНЫЕ ПАТТЕРНЫ — в одной строке:",
             size=13, bold=True, color=GOLD)
    multiline_box(slide, 0.7, 5.95, 12.0, 1.0, [
        ("PINN (нейросеть с физическими ограничениями) — физика в функции потерь ML · CIRL — PID в функции потерь глубокого RL (BASF)", {"size": 12, "color": DEEP}),
        ("ML поверх SPC — статистическая база + ML на остатке · PLC + ML-копроцессор на крае (паттерн POSCO)", {"size": 12, "color": DEEP}),
    ], line_spacing=1.4)


def s34_pfizer_vox(p):
    """s34 — Pfizer Vox worked example."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Pfizer Vox через 5-шаговую рамку — разобранный пример",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "Применяем рамку ретроспективно — это готовый инструмент, не абстрактная теория",
             size=14, italic=True, color=LIGHT)
    steps = [
        ("ШАГ 1", "Класс процесса", "ПРОЦЕССНОЕ — непрерывный биопроцесс.\nмРНК-вакцины: партионный процесс, непрерывный мониторинг.", MID),
        ("ШАГ 2", "Альтернативы", "SPC: одномерная база (недостаточна)\nDOE: не подходит (онлайн)\nMPC: управление, не покрывает редкие аномалии", TEAL),
        ("ШАГ 3", "4 категории", "Данные ✓ много данных по партиям + разметка из QC\nСтоимость ✓ цена ложных срабатываний управляема\nРегуляторика ✓/✗ FDA → режим характеристики\nЧеловек ✓ операторы обучены", LIGHT),
        ("ШАГ 4", "Пилот + критерии успеха", "+20 000 доз на партию — база известна.\nКритерий: база + окупаемость в 12 мес.", GOLD),
        ("ШАГ 5", "Прод. эксплуатация + человек в цикле", "«Vox даёт рекомендации операторам»\nАрхитектура: поддержка решения, не контроллер.\nЖурнал аудита для FDA Part 11 — удовлетворён.", DEEP),
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
             "Урок: 5-шаговая рамка работает ретроспективно — готовый инструмент для оценки новых проектов",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, italic=True)


def s34b_avionics_fail(p):
    """s34b — Авиадвигатель MTBF 8 — рамка ОТСЕКАЕТ (worked example: AI не нужен)."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Авиадвигатель MTBF 8 лет — рамка отсекает AI",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "Применяем 5 шагов — рамка работает в обе стороны: ловит, где AI не подходит",
             size=14, italic=True, color=LIGHT)
    steps = [
        ("ШАГ 1", "Класс процесса", "✓",
         "Дискретное.\nГазотурбинный авиационный двигатель — единичное изделие.", MID, True),
        ("ШАГ 2", "Альтернативы", "✓",
         "Базовая линия — RCM:\nвиброанализ + анализ масла + плановый разбор.\nРаботает 50 лет.", TEAL, True),
        ("ШАГ 3", "4 категории", "✗ ДАННЫЕ",
         "MTBF 8 лет → <100 отказов\nза 20 лет эксплуатации.\nЭталонная разметка — миллионы $.", LIGHT, False),
        ("ШАГ 4", "Регуляторика", "✗ SIL/DO-178C",
         "SIL 2 + DO-178C:\nML не сертифицируем как конечный принимающий решение для критичной авиатехники.", GOLD, False),
        ("ШАГ 5", "Человек", "✗",
         "Нет окна для эскалации:\nрешение принимается на земле, не в реальном времени.\nHITL не помогает.", DEEP, False),
    ]
    card_w = 2.42
    gap = 0.05
    for i, (label, name, mark, body, color, pass_step) in enumerate(steps):
        x = 0.5 + i * (card_w + gap)
        y = 1.7
        rounded_box(slide, x, y, card_w, 4.6)
        rectangle(slide, x, y, card_w, 0.55, fill=color)
        text_box(slide, x, y + 0.05, card_w, 0.45, label,
                 size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.1, y + 0.65, card_w - 0.2, 0.45, name,
                 size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        # Pass/Fail mark
        mark_color = TEAL if pass_step else GOLD
        text_box(slide, x + 0.1, y + 1.1, card_w - 0.2, 0.45, mark,
                 size=14, bold=True, color=mark_color, align=PP_ALIGN.CENTER)
        text_box(slide, x + 0.2, y + 1.65, card_w - 0.4, 3.0, body,
                 size=10, color=DEEP, line_spacing=1.3)
    # Conclusion
    rounded_box(slide, 0.5, 6.45, 12.33, 0.55, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 6.5, 12.0, 0.45,
             "Вывод: AI не нужен. Альтернатива — RCM + физические сенсоры (вибрация, масло) + обмен данными по парку",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, italic=True)


def s34c_brewery_pass(p):
    """s34c — Brewery CV-QC — рамка ПРОПУСКАЕТ (worked example: AI подходит)."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Зрение для контроля упаковки на пивоварне — рамка пропускает AI",
             size=22, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "Симметричный пример: рамка работает и положительно — где AI действительно уместен",
             size=14, italic=True, color=LIGHT)
    steps = [
        ("ШАГ 1", "Класс процесса", "✓",
         "Дискретное.\nБутылки/банки —\nштучный счёт.\nСкорость 60 000 в час.", MID, True),
        ("ШАГ 2", "Альтернативы", "✓",
         "Базовая линия — ручной отбор\nи периодический контроль.\nПропускает дефекты этикеток.", TEAL, True),
        ("ШАГ 3", "4 категории", "✓ ДАННЫЕ",
         ">1 млн бутылок/день,\nдефекты ~0,5% → 5 000 размеченных примеров в день.\nКласс-баланс достижим.", LIGHT, True),
        ("ШАГ 4", "Регуляторика", "✓ ISO 22000",
         "ISO 22000 (пищевая безопасность):\nрежим «характеристика» уместен.\nХарактеристика, не финальное решение.", GOLD, True),
        ("ШАГ 5", "Человек", "✓",
         "Очередь сомнительных кейсов\nдля оператора —\nдоля 8–12% штатно.\nЭскалация работает.", DEEP, True),
    ]
    card_w = 2.42
    gap = 0.05
    for i, (label, name, mark, body, color, pass_step) in enumerate(steps):
        x = 0.5 + i * (card_w + gap)
        y = 1.7
        rounded_box(slide, x, y, card_w, 4.6)
        rectangle(slide, x, y, card_w, 0.55, fill=color)
        text_box(slide, x, y + 0.05, card_w, 0.45, label,
                 size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.1, y + 0.65, card_w - 0.2, 0.45, name,
                 size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        # Pass/Fail mark
        mark_color = TEAL if pass_step else GOLD
        text_box(slide, x + 0.1, y + 1.1, card_w - 0.2, 0.45, mark,
                 size=14, bold=True, color=mark_color, align=PP_ALIGN.CENTER)
        text_box(slide, x + 0.2, y + 1.65, card_w - 0.4, 3.0, body,
                 size=10, color=DEEP, line_spacing=1.3)
    # Conclusion
    rounded_box(slide, 0.5, 6.45, 12.33, 0.55, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, 6.5, 12.0, 0.45,
             "Вывод: AI уместен. Внедрить CV-контроль с долей сомнительных кейсов 8–12% и эскалацией оператору",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, italic=True)


def s35_framework(p):
    """s35 — 5-step framework summary."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "5-шаговая рамка — ваш инструмент для кармана",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Пять шагов + четыре вопроса к вендору + гибридные паттерны",
             size=14, italic=True, color=LIGHT)
    # 5 steps as horizontal flow
    steps = [
        ("1", "Класс процесса", "дискретное / процессное?\nкакая физика, регуляторика?"),
        ("2", "Альтернативы", "SPC / DOE / MPC / RCM /\nфиз.симуляция / правила-зрение"),
        ("3", "Применить 4 категории", "Данные · Стоимость ·\nРегуляторика · Человек"),
        ("4", "Пилот + критерии", "база + окно измерения +\nкритерий «идти/не идти» ДО старта"),
        ("5", "Эксплуатация + человек", "режим характеристики\nвалидирован, прослеживается"),
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
    # 5 vendor questions (per chapter §5.2 — unified set, includes 5th about past failures)
    rounded_box(slide, 0.5, 4.5, 12.33, 2.5, fill=SURFACE, stroke=MID, stroke_w=2.0)
    text_box(slide, 0.7, 4.6, 12.0, 0.4, "ПЯТЬ ВОПРОСОВ К ВЕНДОРУ — для кармана",
             size=16, bold=True, color=MID, align=PP_ALIGN.CENTER)
    qs = [
        ("1", "База до AI", "на какой объём сравниваете?"),
        ("2", "Окно измерения", "за какой период оценка?"),
        ("3", "Перечень вмешательств", "что реально автоматизировано?"),
        ("4", "Канал OEE", "доступность / производительность / качество?"),
        ("5", "Прошлые провалы", "≥3 задокументированных провала за 24 мес в той же индустрии?"),
    ]
    qw = 2.4
    qg = 0.05
    for i, (num, title, body) in enumerate(qs):
        x = 0.5 + i * (qw + qg)
        y = 5.15
        rounded_box(slide, x, y, qw, 1.7)
        text_box(slide, x, y + 0.1, qw, 0.5, num,
                 size=20, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
        text_box(slide, x + 0.1, y + 0.65, qw - 0.2, 0.4, title,
                 size=11, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(slide, x + 0.15, y + 1.1, qw - 0.3, 0.55, body,
                 size=9, italic=True, color=DARK_GREY, align=PP_ALIGN.CENTER, line_spacing=1.25)


# ========== Section 5 ==========

def s36_section5_divider(p):
    section_divider(p, 5, "Замыкание",
                    "Краткое замыкание · 5 вопросов вендору · переход к Лекции 12",
                    "Раздел 5 · 6 мин · 3 слайда")


def s37_recap(p):
    """s37 — recap + failure-callback."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Замыкание двухколонной схемы + урок провалов",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.1, 12.33, 0.4,
             "Что мы разобрали — дискретное | процессное | общее",
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
        ("Зрение (BMW + TSMC + Boeing) · разметка · прогностическое обслуживание · коботы", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("Урок провалов:", {"size": 12, "bold": True, "color": GOLD}),
        ("чрезмерная автоматизация (Tesla 2018)", {"size": 11, "color": DEEP}),
        ("сдвиг распределения · редкая разметка", {"size": 11, "color": DEEP}),
        ("заявления вендора без базы", {"size": 11, "color": DEEP}),
    ], line_spacing=1.3)
    rounded_box(slide, 6.83, col_y, col_w, col_h, fill=SURFACE, stroke=TEAL, stroke_w=1.5)
    rectangle(slide, 6.83, col_y, col_w, 0.5, fill=TEAL)
    text_box(slide, 6.83, col_y + 0.05, col_w, 0.4, "ПРОЦЕССНОЕ",
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 7.03, col_y + 0.6, col_w - 0.4, 2.8, [
        ("Инструменты:", {"size": 12, "bold": True, "color": TEAL}),
        ("мягкие сенсоры · MPC/RL/CIRL · обслуживание на крае · регуляторика", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("Урок провалов:", {"size": 12, "bold": True, "color": GOLD}),
        ("дрейф распределения в RL · регуляторный блокер", {"size": 11, "color": DEEP}),
        ("OT/IT раскол · PR-обещания вендора", {"size": 11, "color": DEEP}),
    ], line_spacing=1.3)
    # Universal layer
    rounded_box(slide, 0.5, 5.15, 12.33, 0.8, fill=GOLD_TINT, stroke=GOLD, stroke_w=1.5)
    text_box(slide, 0.7, 5.2, 12.0, 0.35, "ОБЩИЙ СЛОЙ",
             size=12, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(slide, 0.7, 5.55, 12.0, 0.35,
             "Фундаментальные модели = расширение, не контроллер · 95% не доходят до промышленной эксплуатации · 4 категории + 5-шаговая рамка + 5 вопросов",
             size=11, color=DEEP, align=PP_ALIGN.CENTER, italic=True)
    # Closing lesson formula
    rounded_box(slide, 0.5, 6.05, 12.33, 0.95, fill=DEEP)
    multiline_box(slide, 0.7, 6.15, 12.0, 0.85, [
        ("ФОРМУЛА ДЛЯ КАРМАНА:", {"size": 12, "bold": True, "color": GOLD, "align": PP_ALIGN.CENTER}),
        ("«Завтра вендор обещает –70% простоев — задайте 4 вопроса + 5-й о прошлых провалах. Если расплывчатые ответы — это демо, не промышленная эксплуатация.»", {"size": 12, "bold": True, "color": WHITE, "align": PP_ALIGN.CENTER, "italic": True}),
    ], line_spacing=1.3)


def s38_qa(p):
    """s38 — Q&A with 5 vendor questions + 3 typical."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Пять вопросов к вендору — для кармана",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Запишите на стикер, наклейте на монитор · работает на любом предложении вендора",
             size=14, italic=True, color=LIGHT)
    # 5 questions horizontal — unified per chapter §5.2
    qs = [
        ("1", "База до AI", "На какой объём работы / времени / стоимости сравниваете?"),
        ("2", "Окно измерения", "За какой период оценка — день, неделя, месяц?"),
        ("3", "Перечень вмешательств", "Какие AI-инструменты учтены? Что реально автоматизировано?"),
        ("4", "Канал OEE", "Доступность / производительность / качество — какой компонент?"),
        ("5", "Прошлые провалы", "≥3 задокументированных провала за 24 мес в той же индустрии?"),
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
         "Пройдите 5-шаговую рамку. Если хотя бы шаг не проходит — отчитайтесь руководству. Не запускайте пилот без критериев успеха."),
        ("«SPC или ML — что выбрать?»",
         "FDA + один параметр → SPC. Много параметров + режим характеристики + журнал аудита → ML. Гибрид: SPC + ML на остатке — защищается перед регулятором."),
        ("«RL или MPC — что лучше?»",
         "MPC доминирует в контуре управления. RL дополняет MPC на верхнем уровне планирования. Безопасный откат к MPC обязателен."),
    ]
    for i, (q, a) in enumerate(typical):
        x = 0.5 + i * 4.15
        y = 5.25
        rounded_box(slide, x, y, 4.05, 1.7)
        text_box(slide, x + 0.15, y + 0.15, 3.75, 0.7, "В. " + q,
                 size=11, bold=True, color=DEEP, italic=True, line_spacing=1.3)
        text_box(slide, x + 0.15, y + 0.85, 3.75, 0.8, "→ " + a,
                 size=10, color=DARK_GREY, line_spacing=1.3)


def s39_closing(p):
    """s39 — closing hero BMW digital twin. Hero ≥40% area."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    # Hero image left — 8.0 × 5.4 ≈ 43.2% of canvas (target ≥40%)
    img_path = ASSETS / "screenshots" / "s39-bmw-welt.jpg"
    if img_path.exists():
        add_image(slide, img_path, 0.5, 0.5, 8.0, 5.4)
    else:
        rectangle(slide, 0.5, 0.5, 8.0, 5.4, fill=SOFT_GREY)
        text_box(slide, 0.5, 2.5, 8.0, 0.6, "[BMW Welt + digital twin]",
                 size=16, color=SLATE, align=PP_ALIGN.CENTER)
    # Caption
    attribution(slide, "BMW Welt / Group · Wikimedia CC-BY-SA · BMW Digital Twin · NVIDIA GTC Париж 2025",
                x=0.5, y=6.0, w=8.0)
    # Bridge right (narrower column)
    multiline_box(slide, 8.7, 0.6, 4.3, 5.6, [
        ("Лекция 12 — переход", {"size": 13, "italic": True, "color": GOLD}),
        ("Сшивка инструментов в", {"size": 22, "bold": True, "color": DEEP}),
        ("производственную ткань", {"size": 22, "bold": True, "color": DEEP}),
        ("", {"size": 8}),
        ("Сегодня:", {"size": 13, "bold": True, "color": MID}),
        ("Зрение, мягкие сенсоры, прогностическое обслуживание, фундаментальные модели — отдельные инструменты.", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("Лекция 12:", {"size": 13, "bold": True, "color": MID}),
        ("Цифровые двойники как объединяющая абстракция · AI в автоматизации · ГОСТ Р 57700.37 в РФ.", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("Параллели:", {"size": 13, "bold": True, "color": MID}),
        ("BMW 30+ заводов · Holcim — первый в мире цементный двойник · Foxconn — NVIDIA Omniverse", {"size": 11, "italic": True, "color": DARK_GREY}),
    ], line_spacing=1.2)
    # Closing strip bottom
    rounded_box(slide, 0.5, 6.45, 12.33, 0.6, fill=DEEP)
    text_box(slide, 0.7, 6.5, 12.0, 0.3,
             "Спасибо · Лекция 11 · AI в дискретном и процессном производстве",
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    text_box(slide, 0.7, 6.8, 12.0, 0.25,
             "Запомните 5 вопросов к вендору — это самая практическая вещь сегодня",
             size=11, italic=True, color=GOLD_TINT, align=PP_ALIGN.CENTER)
