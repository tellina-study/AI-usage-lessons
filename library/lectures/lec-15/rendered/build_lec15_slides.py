"""
Slide builders for Лекции 15 — part 1 (s01-s20).
Imports helpers from build_lec15.py.
"""
from build_lec15 import (
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE, GOLD_TINT,
    TEAL_TINT, SOFT_GREY, DARK_GREY, RED_WARN, ROADMAP, ASSETS,
    text_box, multiline_box, rounded_box, rectangle, circle,
    right_arrow, down_arrow, add_image, set_slide_bg, blank,
    add_notes, roadmap_bar, footer, attribution, slide_header,
)
from pptx.util import Inches, Pt
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

IMG = ASSETS / "images"
CHARTS = ASSETS / "charts"


# ========== SECTION 0 — Introduction (s01-s05) ==========

def s01_hero_alphafold_galactica(p):
    """s01 — hero composite: Nobel Chemistry 2024 + Galactica retraction."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)

    # Left half: Stockholm Konserthuset (Nobel ceremony venue)
    img_left2 = IMG / "s01-stockholm-hall.jpg"
    add_image(slide, img_left2, 0.3, 0.5, 6.2, 3.4)
    # Caption-bar overlay (positive side)
    rectangle(slide, 0.3, 3.85, 6.2, 0.5, fill=DEEP)
    text_box(slide, 0.45, 3.9, 5.9, 0.4,
             "9 октября 2024 — Нобель по химии за AlphaFold",
             size=13, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)

    # Center bridging caption ⇄
    rounded_box(slide, 6.4, 1.5, 0.55, 2.0, fill=GOLD, stroke=DEEP, stroke_w=2)
    text_box(slide, 6.4, 1.5, 0.55, 2.0, "⇄",
             size=36, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)

    # Right half: Galactica retraction — replaced visual with text headline card
    # (Original spacebears4.jpeg image was a dog, not Galactica content)
    rounded_box(slide, 6.85, 0.5, 6.2, 3.4, fill=DEEP, stroke=RED_WARN, stroke_w=3)
    multiline_box(slide, 7.05, 0.85, 5.8, 2.7, [
        ("RETRACTED — отозвано",
            {"size": 14, "bold": True, "color": RED_WARN, "italic": True}),
        ("", {"size": 4}),
        ("«Why Meta's Galactica only",
            {"size": 22, "bold": True, "color": WHITE}),
        ("survived three days online»",
            {"size": 22, "bold": True, "color": WHITE}),
        ("", {"size": 6}),
        ("Will Douglas Heaven",
            {"size": 13, "italic": True, "color": WHITE}),
        ("MIT Technology Review · 18 ноября 2022",
            {"size": 12, "italic": True, "color": WHITE}),
        ("", {"size": 6}),
        ("48 млн научных статей в обучении.",
            {"size": 13, "color": WHITE}),
        ("Цитировала несуществующие работы.",
            {"size": 13, "color": WHITE}),
    ], line_spacing=1.2)
    rectangle(slide, 6.85, 3.85, 6.2, 0.5, fill=RED_WARN)
    text_box(slide, 7.0, 3.9, 5.9, 0.4,
             "Запущена 15 ноября — отозвана 17 ноября 2022 — 3 дня public",
             size=12, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)

    # Bottom: assertion + meta
    rounded_box(slide, 0.3, 4.55, 12.73, 1.95, fill=SURFACE, stroke=LIGHT)
    multiline_box(slide, 0.55, 4.7, 12.43, 1.75, [
        ("AlphaFold взял Нобель. Galactica прожила три дня. Различать — задача инженера.",
            {"size": 22, "bold": True, "color": DEEP}),
        ("", {"size": 6}),
        ("Одна эпоха AI-в-науке: структурный прорыв нобелевского уровня и фабрика статей одновременно.",
            {"size": 13, "color": MID, "italic": True}),
        ("Главный навык лекции — различать ситуации AlphaFold и ситуации Galactica.",
            {"size": 13, "color": MID, "italic": True}),
    ], line_spacing=1.2)

    attribution(slide,
        "© Nobel Foundation 2024 (Стокгольм, Konserthuset, Wikimedia) | © MIT Technology Review 2022 (заголовок, fair-use)",
        y=6.75)

    add_notes(slide, "9 октября 2024 года Шведская королевская академия наук объявила лауреатов Нобелевской премии по химии. Половина премии досталась Дэвиду Бейкеру из Вашингтонского университета за вычислительное проектирование белков. Вторая половина разделена между Демисом Хассабисом и Джоном Джампером из DeepMind за AlphaFold — систему предсказания трёхмерной структуры белков по аминокислотной последовательности. Это первая в истории Нобелевская премия по фундаментальной науке, в формулировке которой стоит конкретный AI-продукт.\n\n15 ноября 2022 года, за два года до этого Нобеля, Meta запустила Galactica — большую языковую модель, обученную на 48 миллионах научных статей. Демонстрация в открытом доступе была отозвана 17 ноября 2022 года — прожила три дня публичного доступа. За эти три дня пользователи собрали коллекцию фактических ошибок: Galactica уверенно генерировала научные обзоры про несуществующие исследования, цитировала статьи, которых никогда не было. Заголовок MIT Technology Review от 18 ноября 2022 года — «Why Meta's Galactica only survived three days online» — стал эталонным предостережением.\n\nЭти два события не противоречат друг другу. AlphaFold показал, что AI в науке способен на структурный прорыв нобелевского уровня. Galactica показала, что та же базовая технология, применённая без понимания границ, генерирует фабрику статей и убивает доверие к научной литературе. Главная задача лекции — научить читателя различать ситуации AlphaFold от ситуаций Galactica.")


def s02_cover(p):
    """s02 — cover slide (Phase 8: top bar / LO codes / 75 минут removed)."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)

    # Large decorative «15»
    text_box(slide, 0.5, 1.2, 4.0, 4.5, "15",
             size=240, bold=True, color=ROADMAP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)
    # Title
    multiline_box(slide, 4.5, 1.5, 8.3, 2.0, [
        ("Лекция 15", {"size": 22, "bold": True, "color": LIGHT}),
        ("AI в научных", {"size": 40, "bold": True, "color": DEEP}),
        ("исследованиях", {"size": 40, "bold": True, "color": DEEP}),
    ], line_spacing=1.05)
    # Meta (Phase 8: «75 минут» removed)
    multiline_box(slide, 4.5, 4.4, 8.3, 1.0, [
        ("Модуль 3", {"size": 16, "color": LIGHT}),
        ("Студенты-инженеры 3 курса", {"size": 16, "color": LIGHT}),
    ])
    # Цели — без LO-кодов (Phase 8: они только в frontmatter)
    rounded_box(slide, 4.5, 5.5, 8.3, 1.4)
    multiline_box(slide, 4.7, 5.65, 8.0, 1.2, [
        ("Цели лекции:", {"size": 14, "bold": True, "color": MID}),
        ("Назвать инструменты AI-в-науке по шести ступеням лестницы",
            {"size": 12, "color": DEEP}),
        ("Отличить прорыв от фабрики статей; диагностировать конкретный кейс",
            {"size": 12, "color": DEEP}),
        ("Сформулировать «когда AI не нужен» и предложить альтернативу",
            {"size": 12, "color": DEEP}),
    ], line_spacing=1.2)
    footer(slide, "Курс «Применение AI в инженерии» · 2026")

    add_notes(slide, "Эта лекция — пятнадцатая в курсе и финал первого квартала прикладного модуля. Она встроена в Модуль 3 и опирается на Лекции 1, 2, 3, 7 и 11. Из Лекции 1 вы знаете: галлюцинация — это не сбой, а нормальное поведение модели, генерирующей следующий токен по распределению. Из Лекции 2 — что у трансформеров эмбеддинги — это плотные векторные представления, а матрица внимания — это статистический корреляционный механизм, не понимание. Из Лекции 3 — что агентные архитектуры с использованием инструментов — это RAG над рабочей памятью, не автономный разум. Из Лекции 7 — что человек в петле в медицине обязателен и почему. Из Лекции 11 — что пилот, не доходящий до производства, — это статистическая норма.\n\nНесущая концептуальная ось лекции — лестница научного цикла из шести ступеней: формулирование гипотезы, планирование эксперимента, проведение эксперимента, анализ данных, написание статьи, рецензирование. AI входит в каждую ступень по-разному: где-то как расширение, где-то как автономный прорыв нобелевского уровня, где-то требует человека в петле, где-то категорически противопоказан.\n\nЛестница циклическая. В Лекциях 13 и 14 лестницы были последовательными. Научный цикл устроен иначе: рецензент возвращает работу к анализу или к эксперименту; анализ порождает новую гипотезу. Это свойство самой науки.\n\nЦель лекции — научить вас диагностировать, на какой ступени встроен AI в ваш конкретный случай, и решать осознанно: применять, применять с проверкой, отказаться. Это не лекция «AI в науке — будущее»; это лекция «AI в науке требует суждения».")


def s03_lecture_map(p):
    """s03 — keystone staircase (6 cyclical steps)."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Лестница научного цикла. Шесть ступеней. Цикл, а не прямая.")

    # 6 horizontal staircase cards (Phase 8: bilingual RU primary + EN gloss, Russified role tags)
    steps = [
        ("1", "Гипотеза", "Hypothesis", "расширение", LIGHT),
        ("2", "План", "Design", "расширение", LIGHT),
        ("3", "Эксперимент", "Experiment", "прорыв", GOLD),
        ("4", "Анализ", "Analyse", "зрелое ML", MID),
        ("5", "Текст", "Write", "расширение + проверка", TEAL),
        ("6", "Рецензия", "Review", "запрещён", RED_WARN),
    ]
    card_w = 1.95
    gap = 0.08
    x0 = 0.5
    y_top = 1.5
    for i, (num, ru, en, role, accent) in enumerate(steps):
        x = x0 + i * (card_w + gap)
        # Cards with staircase height variation (visual emphasis on Эксперимент)
        card_h = 3.2 if ru in ["Эксперимент"] else 2.9
        y_card = y_top + (3.2 - card_h)
        rectangle(slide, x, y_card, card_w, card_h, fill=accent)
        # Number on top
        text_box(slide, x + 0.1, y_card + 0.15, card_w - 0.2, 0.7, num,
                 size=44, bold=True, color=WHITE, anchor=MSO_ANCHOR.TOP,
                 align=PP_ALIGN.LEFT)
        # Russian label (primary)
        text_box(slide, x + 0.1, y_card + 0.95, card_w - 0.2, 0.5, ru,
                 size=16, bold=True, color=WHITE)
        # English gloss
        text_box(slide, x + 0.1, y_card + 1.45, card_w - 0.2, 0.4, en,
                 size=13, color=WHITE, italic=True)
        # Role tag (bottom of card)
        rounded_box(slide, x + 0.1, y_card + card_h - 0.55, card_w - 0.2, 0.45,
                    fill=WHITE, stroke=accent, stroke_w=1.5)
        text_box(slide, x + 0.1, y_card + card_h - 0.55, card_w - 0.2, 0.45,
                 role, size=11, bold=True, color=accent,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    # Cyclical return arrow Review → Hypothesis
    rounded_box(slide, 0.5, 5.0, 12.33, 0.7, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    text_box(slide, 0.7, 5.0, 11.93, 0.7,
             "Цикл, не прямая: рецензент возвращает к анализу · из анализа возникает новая гипотеза",
             size=14, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)
    # Curved cyclical arrow indicator
    text_box(slide, 0.5, 5.0, 12.33, 0.7, "⟲",
             size=24, bold=True, color=GOLD,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.RIGHT)

    # Bottom takeaway
    multiline_box(slide, 0.5, 6.0, 12.33, 0.95, [
        ("Главный приём:", {"size": 13, "bold": True, "color": MID}),
        ("Возьмите конкретный случай — спросите лестницу на каждой ступени: «здесь AI расширение, автономно или запрещён?»",
            {"size": 14, "color": DEEP, "italic": True}),
    ], line_spacing=1.2)

    attribution(slide,
        "Научный цикл итеративный — рецензент возвращает к анализу; анализ порождает новую гипотезу.",
        y=6.95)

    add_notes(slide, "Это keystone-слайд лекции. Запомните разделение, потому что мы будем возвращаться к нему весь следующий час с четвертью.\n\nПервая ступень — формулирование гипотезы: что вы хотите узнать и почему это важно. Здесь AI работает как партнёр по мозговому штурму, но не как проверенный научный руководитель. Расширение работает; автономно нет.\n\nВторая — планирование эксперимента: какие переменные, какие контроли, какой статистический анализ. AI работает там, где известные протоколы можно автоматизировать — синтез известных соединений в Coscientist. Autonomous discovery — пока нет.\n\nТретья — проведение эксперимента, лабораторное или вычислительное. Это самый сильный раздел лекции. AlphaFold и Нобель 2024, GNoME 380 тысяч стабильных материалов, Aurora 5000-кратное ускорение. Прорывы нобелевского уровня и одновременно трещины в каждом из этих успехов.\n\nЧетвёртая — анализ данных. AI здесь работает предсказуемо: эталонная разметка есть, задачи узкие. Обнаружение экзопланет, нейронная коннектомика, гравитационные волны. Это привычное обучение с учителем, не «новый AI».\n\nПятая — написание статьи. AI помогает в литературном поиске и обзоре, но требует ручной проверки каждой ссылки. NotebookLM и Elicit — работающее расширение; галлюцинации всё равно случаются.\n\nШестая — рецензирование. AI запрещён для финального решения политикой большинства топ-журналов и конференций.\n\nЛестница циклическая. Это критическое отличие от лекций 13 и 14, где лестницы были последовательными. Научный цикл итеративный: рецензент возвращает работу к анализу; из анализа возникает новая гипотеза.")


def s04_glossary(p):
    """s04 — 8 key terms (Phase 8: trimmed 15→8, larger readable fonts)."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Восемь ключевых терминов. Общий словарь следующего часа.")

    # Three-column header
    cols = [("Термин", 0.5, 2.8), ("Определение", 3.5, 5.5), ("Первый пример", 9.2, 3.83)]
    y_header = 1.45
    for label, x, w in cols:
        rectangle(slide, x, y_header, w, 0.55, fill=MID)
        text_box(slide, x + 0.1, y_header, w - 0.2, 0.55, label,
                 size=15, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)

    # Phase 8: 8 most-used terms (others defined inline elsewhere)
    terms = [
        ("Фундаментальная модель", "Большая ML-модель общего назначения, обученная на огромном корпусе", "AlphaFold · Aurora · GNoME"),
        ("RAG (поиск + генерация)", "LLM отвечает с опорой на найденные документы", "NotebookLM · Elicit"),
        ("Галлюцинация", "Правдоподобный, но неверный вывод — нормальное поведение LLM", "Galactica «цитирует» несуществующее"),
        ("Закрытый / открытый мир", "Закр.: пространство описано, проверка возможна. Откр.: требует выхода", "Закр.: катализ через DFT"),
        ("IDP", "Внутренне разупорядоченный белок — без стабильной 3D-структуры", "AlphaFold даёт 22% галл. в IDP"),
        ("BO + GP", "Байесовская оптимизация + гауссовский процесс (40-60 лет)", "Зрелая альтернатива «AI» в опытах"),
        ("Фабрика статей", "Индустриализированное производство фальшивых публикаций", "Frontiers «крыса» 2024"),
        ("HITL (человек в петле)", "Человек останавливает конвейер на проверке", "AlphaFold + лабораторная валидация"),
    ]
    y0 = 2.1
    row_h = 0.56
    for i, (term, defn, ex) in enumerate(terms):
        y = y0 + i * row_h
        if i % 2 == 1:
            rectangle(slide, 0.5, y, 12.53, row_h, fill=SURFACE)
        text_box(slide, 0.6, y, 2.7, row_h, term,
                 size=13, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, 3.6, y, 5.3, row_h, defn,
                 size=12, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, 9.3, y, 3.63, row_h, ex,
                 size=12, color=MID, italic=True, anchor=MSO_ANCHOR.MIDDLE)

    attribution(slide, "Остальные термины (CASP, DFT, MD, ECMWF, ICMJE, эталонная разметка, рецензирование) определены при первом появлении в разделах лекции.", y=6.85)

    add_notes(slide, "Прежде чем двинемся по разделам, договоримся об общем словаре. Эти пятнадцать терминов встречаются в каждом разделе лекции, и непонимание любого из них блокирует следующие.\n\nФундаментальная модель — большая модель машинного обучения общего назначения, обученная на огромном корпусе и применимая ко многим задачам. AlphaFold для белков, Aurora для атмосферы, GNoME для материалов. RAG — это поиск с генерацией: LLM генерирует ответ с опорой на найденные документы.\n\nГаллюцинация — это не сбой модели, это нормальное поведение LLM. Запомните: галлюцинация — не баг, она встроена в архитектуру. Galactica цитировала несуществующие статьи именно потому.\n\nРецензирование, репликация, кризис воспроизводимости — фундаментальные институциональные термины. Воспроизводимость психологии — 39 из 100, экономика — 61 процент, AI и машинное обучение — от 24 до 50 процентов. AI не лечит эту проблему и может её усугубить.\n\nЗакрытый против открытого мира — это диагностический критерий лекции. Закрытая задача: пространство решений описано через физические уравнения, проверка возможна. Открытая: пространство не описано, проверка требует выхода за систему. Катализ — закрытый; гипотеза о роли социальных сетей — открытый.\n\nIDP — внутренне разупорядоченный белок без стабильной 3D-структуры. AlphaFold там галлюцинирует, и это критично для разработки лекарств. CASP, DFT, MD, BO, GP, ECMWF, ICMJE — институциональные имена. Каждое расписано подробнее по ходу лекции.")


def s05_central_question(p):
    """s05 — central question + 5-step framework preview."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Где AI делает прорыв. Где создаёт фабрику статей. Как решать.")

    # Big central question in Ocean rounded box
    rounded_box(slide, 0.5, 1.5, 12.33, 2.7, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.5)
    multiline_box(slide, 0.8, 1.65, 11.7, 2.45, [
        ("Центральный вопрос лекции", {"size": 12, "bold": True, "color": GOLD, "italic": True}),
        ("", {"size": 4}),
        ("Где AI делает прорыв в науке,", {"size": 22, "bold": True, "color": DEEP}),
        ("где он создаёт фабрику статей,", {"size": 22, "bold": True, "color": DEEP}),
        ("и как инженер должен решать,",
            {"size": 20, "bold": True, "color": MID, "italic": True}),
        ("в какой класс попадает его конкретный случай?",
            {"size": 20, "bold": True, "color": MID, "italic": True}),
    ], line_spacing=1.15)

    # 5-step framework preview
    text_box(slide, 0.5, 4.35, 12.33, 0.4,
             "Ответ — пятишаговая рамка, которую соберём к концу лекции",
             size=14, bold=True, color=MID)
    steps = [
        ("1", "Классифицируй задачу", "открытый или закрытый мир"),
        ("2", "Проверь покрытие", "обучающее распределение модели"),
        ("3", "Спроектируй шлюзы", "человек в петле"),
        ("4", "Проверь до публикации", "альтернативный метод"),
        ("5", "Раскрой использование AI", "ICMJE и журналы"),
    ]
    card_w = 2.42
    gap = 0.05
    x0 = 0.5
    y_steps = 4.85
    for i, (num, title, desc) in enumerate(steps):
        x = x0 + i * (card_w + gap)
        rounded_box(slide, x, y_steps, card_w, 1.7, fill=SURFACE, stroke=LIGHT)
        # Number circle
        circle(slide, x + 0.15, y_steps + 0.15, 0.5, 0.5, fill=MID)
        text_box(slide, x + 0.15, y_steps + 0.15, 0.5, 0.5, num,
                 size=18, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        # Title + desc
        multiline_box(slide, x + 0.2, y_steps + 0.75, card_w - 0.3, 0.8, [
            (title, {"size": 12, "bold": True, "color": DEEP}),
            (desc, {"size": 10, "color": MID, "italic": True}),
        ], line_spacing=1.15)

    attribution(slide, "Эта рамка применима к любому конкретному кейсу AI в науке.", y=6.95)

    add_notes(slide, "Центральный вопрос всей лекции — три части. Где AI в науке действительно делает прорыв. Где он, наоборот, создаёт фабрику статей. И — главное для инженера — как решать, в какой из этих классов попадает ваш конкретный случай.\n\nЭтот вопрос буквально определяет повестку всей лекции. К концу мы построим конкретную рамку из пяти шагов, которую можно применить в инженерной практике в тот же день. Эта рамка не панацея и не алгоритм; это диагностический вопросник.\n\nПервый шаг — классифицировать задачу. Принадлежит ли она открытому миру или закрытому. Открытый мир — когда пространство решений не определено и проверка требует выхода за пределы системы. Закрытый — когда пространство описано, например через физические уравнения, и проверка возможна.\n\nВторой шаг — проверить покрытие. Лежит ли ваш случай в распределении обучающих данных модели или вы экстраполируете далеко за пределы.\n\nТретий — спроектировать шлюзы человека в петле. Где специалист останавливает конвейер и проверяет.\n\nЧетвёртый — проверить каждое измеримое утверждение до публикации через альтернативный метод. Любая цифра, которую вы публикуете, должна быть подтверждена не-AI методом.\n\nПятый — раскрыть использование AI согласно политикам ICMJE и конкретного журнала.\n\nК этой рамке мы возвращаемся в разделе 5 и применяем её на разобранном примере катализатора окисления пропилена.")


# ========== SECTION 1 — Hypothesis + Design (s06-s11) ==========

def s06_section1_divider(p):
    """s06 — section 1 divider (Phase 8: top bar removed)."""
    slide = blank(p)
    set_slide_bg(slide, SURFACE)

    # Big section number
    text_box(slide, 0.5, 1.5, 5.0, 3.0, "§1",
             size=200, bold=True, color=LIGHT, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)
    # Title
    multiline_box(slide, 5.5, 1.7, 7.3, 4.0, [
        ("Раздел 1", {"size": 22, "bold": True, "color": MID}),
        ("Hypothesis + Design", {"size": 42, "bold": True, "color": DEEP}),
        ("Гипотеза и план", {"size": 26, "color": LIGHT, "italic": True}),
        ("", {"size": 12}),
        ("Где AI продаётся за автономию,", {"size": 18, "color": DEEP}),
        ("но даёт узкую помощь.", {"size": 18, "color": DEEP}),
    ], line_spacing=1.2)

    # Section preview tags (Phase 8: Russified)
    tags = [
        ("WE-1 (грант)", LIGHT),
        ("Sakana — отбор лучших", RED_WARN),
        ("Coscientist vs Co-Scientist", MID),
        ("BO + GP альтернатива", TEAL),
    ]
    y_tag = 5.6
    x = 5.5
    for label, color in tags:
        w = len(label) * 0.13 + 0.4
        rounded_box(slide, x, y_tag, w, 0.4, fill=color, stroke=color, stroke_w=0)
        text_box(slide, x, y_tag, w, 0.4, label,
                 size=11, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        x += w + 0.15

    attribution(slide, "Лестница цикла · ступени 1 и 2 · 4 working cases", y=6.95)
    add_notes(slide, "Открываем раздел 1 — Hypothesis и Design, гипотеза и план. Эти две ступени лестницы научного цикла — самые продаваемые в маркетинге AI-в-науке и самые узкие в реальности.\n\nЗа последние два года в материалах появились две системы с почти одинаковыми именами: Coscientist из Carnegie Mellon и Co-Scientist из DeepMind. Coscientist — это робот-химик из 2023 года, который автоматизирует синтез известных соединений. Co-Scientist — это система из 2026 года, которая помогает формулировать гипотезы. Это разные системы для разных задач. Их часто путают.\n\nТретий важный пример — Sakana AI Scientist. В августе 2024 первая версия объявила «полностью автоматический пайплайн от гипотезы до статьи». Через год выяснилось: одна из трёх статей прошла рецензирование на воркшопе ICLR, но «три» — это уже после ручного отбора из ста.\n\nИ зрелая альтернатива — байесовская оптимизация плюс гауссовский процесс, методы с 40-летней и 60-летней историей, которые обгоняют Sakana в материалах и химии. Эту альтернативу часто игнорируют, потому что она не «AI».")


def s07_we1_grant_idea_tree(p):
    """s07 — walked example WE-1: grant idea 6-step decision tree."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Идея для гранта: 6-шаговое дерево решения «Sakana или PhD-руководитель».")

    # Input box at top
    rounded_box(slide, 0.5, 1.5, 12.33, 0.6, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    text_box(slide, 0.5, 1.5, 12.33, 0.6,
             "Аспирант: «нужна идея для гранта NSF к концу месяца» — что делать?",
             size=14, bold=True, color=DEEP, italic=True,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    # 6 steps in horizontal flow with arrows
    steps = [
        ("1", "Классифицируй задачу", "ступень 1 или 2\nлестницы цикла", LIGHT),
        ("2", "Покрытие", "Sakana 50 кандидатов\nили PhD 3 идеи", MID),
        ("3", "Проверка", "обзор литературы\n+ отложенная выборка", MID),
        ("4", "Этика", "кодекс NSF, ICMJE", TEAL),
        ("5", "Человек в петле", "проверяет\nкаждую идею", TEAL),
        ("6", "Раскрытие AI", "в заявке на грант\nявно указано", GOLD),
    ]
    card_w = 1.95
    gap = 0.08
    x0 = 0.5
    y_card = 2.4
    for i, (num, title, desc, color) in enumerate(steps):
        x = x0 + i * (card_w + gap)
        rounded_box(slide, x, y_card, card_w, 2.5, fill=SURFACE, stroke=color, stroke_w=2)
        # Number circle
        circle(slide, x + (card_w - 0.6) / 2, y_card + 0.15, 0.6, 0.6, fill=color)
        text_box(slide, x, y_card + 0.15, card_w, 0.6, num,
                 size=22, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        # Title
        text_box(slide, x + 0.1, y_card + 0.9, card_w - 0.2, 0.4, title,
                 size=12, bold=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        # Desc multi-line
        multiline_box(slide, x + 0.1, y_card + 1.35, card_w - 0.2, 1.0, [
            (desc, {"size": 10, "color": MID, "italic": True}),
        ], align=PP_ALIGN.CENTER, line_spacing=1.15)

    # Bottom takeaway
    rounded_box(slide, 0.5, 5.4, 12.33, 1.3, fill=SURFACE, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 0.8, 5.5, 11.8, 1.15, [
        ("Главный приём:", {"size": 13, "bold": True, "color": GOLD}),
        ("Использовать Sakana для расширения покрытия (50 идей вместо 3), но финальный выбор и развитие — за человеком. Если AI отвергнут на любом шаге — переходим к PhD-руководителю.",
            {"size": 13, "color": DEEP, "italic": True}),
    ], line_spacing=1.2)

    attribution(slide, "Источники: Sakana AI blog 2024-2025 · NSF AI Code of Conduct (январь 2024)", y=6.95)

    add_notes(slide, "Это наш первый разобранный пример — WE-1, грант. Контекст: аспирант пишет заявку на грант NSF, ему нужна сильная идея до конца месяца. Один путь — попросить руководителя или прочитать обзор Nature за два года. Другой — попросить у Sakana пятьдесят кандидатов идей. Какой выбрать?\n\nШаг 1 — классифицируем задачу. Hypothesis или Design? Это Hypothesis. Pure разведка пространства идей — открытый мир. Закрытый мир был бы «оптимизируем известный параметр в известной задаче».\n\nШаг 2 — coverage. Sakana даёт 50 кандидатов автоматически. PhD-руководитель даст 3 хорошо обдуманных идеи. Расширение покрытия — реальная польза AI. Но 50 необдуманных идей бессмысленны без отбора.\n\nШаг 3 — verification. Каждую идею проверяем на двух осях: literature check (не дублирует существующее) и validation на held-out exemplars (имеет смысл с точки зрения базовой физики/биологии задачи).\n\nШаг 4 — ethics. Применим ли NSF AI Code of Conduct? Да: если AI помогал в формулировке заявки, нужно раскрытие. Не запрещено, но обязано быть прозрачно.\n\nШаг 5 — HITL контроль. Каждую из 50 кандидат-идей читает человек. Отбираем 5-10 для углублённого literature search.\n\nШаг 6 — submission integrity. В разделе about-AI заявки указываем, что Sakana использовалась как инструмент мозгового штурма; финальные идеи отобраны и развиты автором.\n\nТакая рамка не отвергает AI — она интегрирует его в существующий процесс с человеком в петле. AI расширяет покрытие; человек отвечает за качество и за подачу.")


def s08_sakana_ai_scientist(p):
    """s08 — Sakana cherry-pick mechanics; 1/3 passed = 1% true rate."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Sakana AI Scientist v2: 1 из 3 прошла. Истинная автономия — 1%.")

    # Sakana logo/screenshot left
    img = IMG / "s08-sakana.png"
    add_image(slide, img, 0.5, 1.5, 5.0, 2.5)
    attribution(slide, "© Sakana AI 2025 (sakana.ai/ai-scientist-v2)", x=0.5, y=4.1, w=5.0)

    # Three metrics breakdown right
    rounded_box(slide, 6.0, 1.5, 6.83, 2.7, fill=SURFACE, stroke=LIGHT)
    multiline_box(slide, 6.2, 1.65, 6.43, 2.5, [
        ("Три разные метрики «1 из 3»", {"size": 16, "bold": True, "color": DEEP}),
        ("", {"size": 6}),
        ("Метрика 1 — отбор:", {"size": 13, "bold": True, "color": MID}),
        ("3% (3 из ~100) — человек отобрал лучшее", {"size": 12, "color": DEEP}),
        ("Метрика 2 — рецензирование:", {"size": 13, "bold": True, "color": MID}),
        ("33% (1 из 3) — приняты на ICLR workshop", {"size": 12, "color": DEEP}),
        ("Метрика 3 — истинная автономия:", {"size": 13, "bold": True, "color": GOLD}),
        ("1% (1 из ~100) — без ручного отбора лучших",
            {"size": 14, "bold": True, "color": GOLD}),
    ], line_spacing=1.25)

    # Bottom narrative
    rounded_box(slide, 0.5, 4.7, 12.33, 1.9, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 0.8, 4.85, 11.8, 1.75, [
        ("Что произошло на самом деле:",
            {"size": 13, "bold": True, "color": GOLD}),
        ("", {"size": 5}),
        ("Sakana v2 (март 2025) сгенерировала около 100 черновиков статей.",
            {"size": 14, "color": DEEP}),
        ("Авторы вручную отобрали 3 лучших для подачи на ICLR workshop.",
            {"size": 14, "color": DEEP}),
        ("1 из 3 прошёл рецензирование. TechCrunch март 2025 уточнил: «значимый эффект ручного отбора лучших».",
            {"size": 14, "color": DEEP}),
        ("Это augmented черновик с тяжёлым человеческим фильтром — не автономная наука.",
            {"size": 14, "bold": True, "color": GOLD, "italic": True}),
    ], line_spacing=1.2)

    attribution(slide, "Источники: Sakana blog 12 марта 2025 · TechCrunch 12 марта 2025 · Yamada et al. arxiv 2504.08066",
                y=6.95)

    add_notes(slide, "Sakana AI Scientist v2 — пример системы, которую часто упоминают как «AI пишет статьи». Давайте разберём, что произошло на самом деле.\n\nВ марте 2025 Sakana опубликовала отчёт. Система сгенерировала примерно сто черновиков статей. Авторы вручную отобрали три лучших для подачи на ICLR workshop. Одна из трёх прошла рецензирование. Это «1 из 3» в материалах часто подаётся как «33% автономия».\n\nНо реальная картина другая. Есть три разные метрики, и они дают три разных ответа.\n\nМетрика 1 — отбор. 3% от 100 — человек отобрал три лучших для подачи. Это уже сильный человеческий фильтр на входе.\n\nМетрика 2 — рецензирование. 33% (1 из 3) — приняты на ICLR workshop. Это число действительно валидное; но это уже после ручного отбора.\n\nМетрика 3 — истинная автономия. Если посчитать долю принятых статей от общего количества сгенерированных Sakana, получим 1% (одна из ста). Это и есть честная цифра автономии без cherry-picking.\n\nTechCrunch в марте 2025 явно процитировал авторов Sakana: «значимый эффект cherry-picking». Это augmented черновик с тяжёлым человеческим фильтром, а не автономная наука. Сами авторы это признают.\n\nДля инженерного применения вывод следующий: используйте Sakana как расширение мозгового штурма (50 идей вместо 3), но никогда не подавайте сгенерированную статью без сильного человеческого фильтра.")


def s09_coscientist_vs_co_scientist(p):
    """s09 — Two systems with same name, different tasks."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Coscientist (CMU 2023) vs Co-Scientist (DeepMind 2026). Не путать.")

    # Left column: Coscientist CMU 2023
    rounded_box(slide, 0.5, 1.5, 6.0, 5.0, fill=SURFACE, stroke=LIGHT, stroke_w=2)
    multiline_box(slide, 0.8, 1.7, 5.5, 4.7, [
        ("Coscientist", {"size": 24, "bold": True, "color": DEEP}),
        ("Carnegie Mellon University · 2023", {"size": 13, "italic": True, "color": MID}),
        ("", {"size": 8}),
        ("Стадия лестницы:", {"size": 12, "bold": True, "color": MID}),
        ("3 Experiment + 2 Design", {"size": 14, "bold": True, "color": DEEP}),
        ("", {"size": 6}),
        ("Архитектура:", {"size": 12, "bold": True, "color": MID}),
        ("GPT-4 + Claude (оба, не один)", {"size": 13, "color": DEEP}),
        ("+ Python для контроля приборов", {"size": 13, "color": DEEP}),
        ("", {"size": 6}),
        ("Задача:", {"size": 12, "bold": True, "color": MID}),
        ("Автоматический синтез", {"size": 13, "color": DEEP}),
        ("известных соединений", {"size": 13, "color": DEEP}),
        ("(palladium-catalysed coupling)", {"size": 12, "italic": True, "color": SLATE}),
        ("", {"size": 6}),
        ("Публикация:", {"size": 12, "bold": True, "color": MID}),
        ("Nature 624 (декабрь 2023)", {"size": 13, "color": DEEP}),
        ("Boiko, MacKnight, Kline, Gomes", {"size": 12, "italic": True, "color": SLATE}),
    ], line_spacing=1.18)

    # Right column: Co-Scientist DeepMind 2026
    rounded_box(slide, 6.83, 1.5, 6.0, 5.0, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 7.13, 1.7, 5.5, 4.7, [
        ("Co-Scientist", {"size": 24, "bold": True, "color": DEEP}),
        ("Google DeepMind · 2026", {"size": 13, "italic": True, "color": MID}),
        ("", {"size": 8}),
        ("Стадия лестницы:", {"size": 12, "bold": True, "color": MID}),
        ("1 Hypothesis (формулирование)", {"size": 14, "bold": True, "color": DEEP}),
        ("", {"size": 6}),
        ("Архитектура:", {"size": 12, "bold": True, "color": MID}),
        ("Multi-agent debate", {"size": 13, "color": DEEP}),
        ("(generator + critic + ranker)", {"size": 13, "color": DEEP}),
        ("", {"size": 6}),
        ("Задача:", {"size": 12, "bold": True, "color": MID}),
        ("Формулировка гипотез", {"size": 13, "color": DEEP}),
        ("в биомедицине", {"size": 13, "color": DEEP}),
        ("(drug repurposing, gene therapy)", {"size": 12, "italic": True, "color": SLATE}),
        ("", {"size": 6}),
        ("Публикация:", {"size": 12, "bold": True, "color": MID}),
        ("DeepMind blog (май 2026)", {"size": 13, "color": DEEP}),
        ("Nature submission (на момент лекции)", {"size": 12, "italic": True, "color": SLATE}),
    ], line_spacing=1.18)

    # Key takeaway at bottom
    text_box(slide, 0.5, 6.65, 12.33, 0.35,
             "Одинаковое имя — две разные системы для двух разных ступеней лестницы. Маркетинг сливает; материал лекции — нет.",
             size=12, bold=True, color=GOLD, italic=True, align=PP_ALIGN.CENTER)

    add_notes(slide, "Эти две системы — Coscientist и Co-Scientist — постоянно путают в материалах. Запомните различение.\n\nCoscientist — Carnegie Mellon, 2023 год. Это робот-химик. Публикация в Nature 624 в декабре 2023 года, авторы Boiko, MacKnight, Kline и Gomes. Архитектура простая: GPT-4 и Claude используются оба, как два разных reasoner-агента, плюс Python для управления лабораторными приборами через стандартные API. Задача — автоматический синтез известных соединений, конкретно palladium-catalysed cross-coupling реакций. Это Design и Experiment ступени лестницы. Закрытая задача: известные реакции, известные приборы, известные критерии успеха.\n\nCo-Scientist — DeepMind, 2026 год. Это система формулирования гипотез в биомедицине. Объявлена в блоге DeepMind в мае 2026, Nature publication submitted и пока в процессе рецензирования — отметка VFY-day-of. Архитектура многоагентная: один LLM-агент генерирует гипотезы, второй критикует, третий ранжирует. Задача — drug repurposing и gene therapy candidates. Это Hypothesis ступень. Открытая задача: пространство гипотез очень велико, проверка требует длительных биологических экспериментов.\n\nДве системы — две разные ступени лестницы, две разные задачи, два разных уровня зрелости. Coscientist работает в проде с 2023; Co-Scientist пока ранний этап с одной публикацией. Маркетинг их сливает, потому что обе DeepMind-style autonomous, но материалы лекции должны их различать.")


def s10_sakana_cherry_pick(p):
    """s10 — failure deep-dive: 4 structural problems of Sakana."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Sakana пишет 100, человек отбирает 3, рецензент пропускает 1. Это расширение, не автономия.")

    # Chart left
    img = CHARTS / "s10-sakana-metrics.png"
    add_image(slide, img, 0.4, 1.5, 6.5, 3.6)
    attribution(slide, "Источник: Sakana blog март 2025; Yamada et al. arxiv 2504.08066",
                x=0.4, y=5.15, w=6.5)

    # 4 structural problems right
    multiline_box(slide, 7.2, 1.5, 5.83, 0.5, [
        ("4 структурные проблемы Sakana:",
            {"size": 16, "bold": True, "color": DEEP}),
    ])
    problems = [
        ("1", "Отбор лучшего из 100 (cherry-pick / отбор)", "100 → 3 человек отобрал — фильтр на входе"),
        ("2", "Галлюцинированные ссылки", "Цитаты на несуществующие статьи в черновиках"),
        ("3", "Фальсифицированные результаты", "Численные результаты не воспроизводятся"),
        ("4", "Преувеличенная новизна", "Идеи повторяют уже опубликованное"),
    ]
    y_prob = 2.1
    for i, (num, title, desc) in enumerate(problems):
        y = y_prob + i * 0.85
        rounded_box(slide, 7.2, y, 5.83, 0.75, fill=SURFACE, stroke=LIGHT)
        # Red bullet
        circle(slide, 7.3, y + 0.1, 0.55, 0.55, fill=RED_WARN)
        text_box(slide, 7.3, y + 0.1, 0.55, 0.55, num,
                 size=16, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        multiline_box(slide, 8.0, y + 0.05, 4.95, 0.7, [
            (title, {"size": 12, "bold": True, "color": DEEP}),
            (desc, {"size": 10, "color": MID, "italic": True}),
        ], line_spacing=1.15)

    # Bottom message
    text_box(slide, 0.5, 5.6, 12.33, 1.0,
             "1% — истинная доля автономной науки. 99% — расширение работы человека, не автоматизация.",
             size=20, bold=True, color=GOLD, italic=True,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    attribution(slide, "Урок для инженера: используйте Sakana как мозговой штурм с человеческим фильтром, никогда — как готовую статью.",
                y=6.95)

    add_notes(slide, "Углубим разбор Sakana. У системы четыре структурные проблемы, которые видны в материалах за 2024-2025 годы.\n\nПервая — cherry-picking. Sakana генерирует около ста черновиков, человек отбирает три лучших. Это сильный фильтр на входе. Без него средняя статья Sakana содержит критические ошибки.\n\nВторая — галлюцинированные ссылки. Черновики цитируют статьи, которых не существует. Это типичное поведение LLM, обученной на корпусе научной литературы: модель «знает», как выглядит правдоподобная цитата, но не имеет проверки реальности.\n\nТретья — фальсифицированные численные результаты. Конкретно в черновиках Sakana v1 (август 2024) были численные таблицы с результатами экспериментов, которые не воспроизводятся при ручной проверке. Это не «ошибка кода» — это галлюцинация в числовом виде.\n\nЧетвёртая — преувеличенная новизна. Идеи Sakana часто повторяют уже опубликованное, но представляются как новые. Это следствие отсутствия глубокого literature search в архитектуре.\n\nИтог — 1% истинной автономии и 99% augmentation. Это полезно для инженера: используйте Sakana как расширение мозгового штурма с обязательным человеческим фильтром. Никогда не подавайте сгенерированную статью без ручной проверки каждого утверждения и каждой ссылки.")


def s11_bo_gp_alternative(p):
    """s11 — BO+GP as mature alternative; 40-year track record."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "BO 40+ лет и GP 60+ лет: зрелая альтернатива, обгоняющая Sakana.")

    # Chart left
    img = CHARTS / "s11-bo-convergence.png"
    add_image(slide, img, 0.3, 1.5, 7.5, 4.2)

    # Tags right
    rounded_box(slide, 8.0, 1.5, 5.0, 4.2, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 8.2, 1.7, 4.6, 4.0, [
        ("Что такое BO+GP?", {"size": 16, "bold": True, "color": DEEP}),
        ("", {"size": 8}),
        ("BO = Bayesian Optimization", {"size": 13, "bold": True, "color": MID}),
        ("Mockus 1989; Jones 1998", {"size": 11, "italic": True, "color": SLATE}),
        ("", {"size": 6}),
        ("GP = Gaussian Process", {"size": 13, "bold": True, "color": MID}),
        ("60+ лет в статистике", {"size": 11, "italic": True, "color": SLATE}),
        ("", {"size": 8}),
        ("Прорывы 2020-2025:",
            {"size": 13, "bold": True, "color": GOLD}),
        ("• Shields et al. Nature 2021", {"size": 11, "color": DEEP}),
        ("  Bayesian reaction opt.", {"size": 10, "italic": True, "color": SLATE}),
        ("• Self-driving labs MIT", {"size": 11, "color": DEEP}),
        ("  ускорение 5-10× в материалах", {"size": 10, "italic": True, "color": SLATE}),
        ("• BoTorch, GPyTorch", {"size": 11, "color": DEEP}),
        ("  open-source инструментарий", {"size": 10, "italic": True, "color": SLATE}),
    ], line_spacing=1.18)

    # Bottom narrative
    rounded_box(slide, 0.3, 5.85, 12.73, 0.9, fill=SURFACE, stroke=GOLD, stroke_w=1.5)
    text_box(slide, 0.5, 5.95, 12.33, 0.75,
             "Урок: «AI» в науке — не один путь. Зрелая байесовская оптимизация — это успех 40-летней давности с математической обоснованностью и ускорением 5-10× в реальных лабораториях.",
             size=13, bold=True, color=DEEP, italic=True,
             anchor=MSO_ANCHOR.MIDDLE)
    attribution(slide,
        "Источники: Mockus 1989 · Jones, Schonlau, Welch 1998 (EGO) · Shields et al. Nature 590 (2021)",
        y=6.95)

    add_notes(slide, "Прежде чем мы покинем раздел Hypothesis+Design, обязательно надо упомянуть зрелую альтернативу — байесовскую оптимизацию плюс гауссовский процесс. Это методы с длинной историей и математической обоснованностью.\n\nБайесовская оптимизация формализована в работе Mockus 1989 года, развита в работе Jones, Schonlau, Welch 1998 года — алгоритм EGO, Efficient Global Optimization. Гауссовский процесс как статистическая модель работает в литературе с 1960-х. Это не «новый AI», а зрелая математика.\n\nПримечательные прорывы 2020-2025. Shields и коллеги в Nature 2021 года применили байесовскую оптимизацию к подбору условий органических реакций — ускорение экспериментальной кампании в 5-10 раз. MIT и аналогичные лаборатории построили self-driving labs — автономные станции синтеза, которые комбинируют BO для выбора следующего эксперимента с роботизированной химией.\n\nOpen-source инструментарий зрелый: BoTorch и GPyTorch — стандартные библиотеки в Python для байесовской оптимизации. Их регулярно используют в материаловедении, разработке катализаторов, биохимии.\n\nГлавная мысль слайда: «AI» в науке — это не один путь. Зрелая байесовская оптимизация для определённых задач значительно эффективнее новейшего LLM. Каждый раз, когда вы рассматриваете применение AI в эксперименте, проверяйте — нет ли уже отработанной альтернативы из классической статистики или оптимизации. Часто есть, и она лучше.")
