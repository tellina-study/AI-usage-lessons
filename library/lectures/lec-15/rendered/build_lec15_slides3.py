"""
Slide builders for Лекции 15 — part 3 (s26-s39).
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


# ========== SECTION 4 — Write + Review (s26-s31) ==========

def s26_section4_divider(p):
    """s26 — section 4 divider (Phase 8: top bar removed; tags 5→4; methodology strip)."""
    slide = blank(p)
    set_slide_bg(slide, SURFACE)

    text_box(slide, 0.5, 1.5, 5.0, 3.0, "§4",
             size=200, bold=True, color=RED_WARN, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)
    multiline_box(slide, 5.5, 1.7, 7.3, 4.0, [
        ("Раздел 4", {"size": 22, "bold": True, "color": MID}),
        ("Write + Review", {"size": 42, "bold": True, "color": DEEP}),
        ("Написание и рецензирование", {"size": 24, "color": LIGHT, "italic": True}),
        ("", {"size": 12}),
        ("AI против", {"size": 18, "color": DEEP}),
        ("академической интегриты.", {"size": 18, "bold": True, "color": RED_WARN}),
    ], line_spacing=1.2)

    # Phase 8: trim 5→4 tags + narrower
    tags = [
        ("NotebookLM / Elicit", LIGHT),
        ("Frontiers «крыса»", RED_WARN),
        ("NeurIPS — фейк-цитаты", RED_WARN),
        ("ICMJE правила", TEAL),
    ]
    y_tag = 5.6
    x = 5.5
    for label, color in tags:
        w = len(label) * 0.11 + 0.25
        rounded_box(slide, x, y_tag, w, 0.4, fill=color, stroke=color, stroke_w=0)
        text_box(slide, x, y_tag, w, 0.4, label,
                 size=10, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        x += w + 0.08

    attribution(slide, "Лестница цикла · ступени 5 и 6 · 3 working tools · 2 провала", y=6.95)

    add_notes(slide, "Раздел 4 — Write + Review, написание и рецензирование. Самые острые этические проблемы AI в науке здесь.\n\nЗрелые инструменты работают. NotebookLM — 17 миллионов пользователей, Elicit — 138 миллионов статей в индексе, Consensus.app — 200 миллионов. Это работающее расширение для навигации литературы. Но каждая ссылка, которую вы цитируете, требует ручной проверки.\n\nКонкретный кейс провалов — Frontiers «крыса». 13 февраля 2024 опубликована статья с Midjourney-сгенерированной анатомией крысы. Подписи на фигурах — «protemns» и «zxpens» — несуществующие термины. Отозвана через 3 дня. Раскрытие использования AI в paper не спасло — peer review должен был отдельно проверить фигуры, и не проверил.\n\nNeurIPS 2025 — самый недавний и тревожный кейс. 21 575 поданных, 5 290 принятых (24,52%). 100+ фейковых цитат проникли в 53 принятые статьи. Рецензирование не справилось с массовым AI-помощью.\n\nИ ICMJE — Международный комитет редакторов медицинских журналов — фиксирует базовое правило: AI не может быть автором. Springer, Elsevier, Frontiers, Nature — все имеют политики раскрытия. AI как инструмент с раскрытием — OK; AI как автор — запрещён независимо от качества вывода.")


def s27_notebooklm_elicit(p):
    """s27 — NotebookLM, Elicit, Consensus.app — mature literature tools."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "NotebookLM 17M пользователей. Elicit 138M статей. Расширение работает.")

    # 3 tools as cards
    tools = [
        ("NotebookLM", "Google · 2024", "17 миллионов пользователей",
         "RAG (поиск + генерация) над загруженными PDF; помогает суммировать, цитировать",
         "Каждая ссылка требует ручной проверки", LIGHT),
        ("Elicit", "Ought.io · 2024", "138 миллионов статей в индексе",
         "Систематический обзор за 4× быстрее ручного",
         "Метаанализы не заменимы — но навигация ускоряется", MID),
        ("Consensus.app", "Consensus · 2024", "200 миллионов статей",
         "Поиск по утверждениям: что говорит литература по теме",
         "Низкая воспроизводимость (15%) — фильтр обязателен", TEAL),
    ]
    card_w = 4.1
    gap = 0.1
    x0 = 0.4
    y_card = 1.5
    for i, (name, vendor, scale, desc, caveat, color) in enumerate(tools):
        x = x0 + i * (card_w + gap)
        rounded_box(slide, x, y_card, card_w, 3.5, fill=SURFACE, stroke=color, stroke_w=2)
        multiline_box(slide, x + 0.2, y_card + 0.15, card_w - 0.4, 3.2, [
            (name, {"size": 22, "bold": True, "color": DEEP}),
            (vendor, {"size": 11, "italic": True, "color": SLATE}),
            ("", {"size": 8}),
            ("Масштаб:", {"size": 11, "bold": True, "color": MID}),
            (scale, {"size": 14, "bold": True, "color": GOLD}),
            ("", {"size": 8}),
            ("Что делает:", {"size": 11, "bold": True, "color": MID}),
            (desc, {"size": 11, "color": DEEP, "italic": True}),
            ("", {"size": 8}),
            ("Ограничение:", {"size": 11, "bold": True, "color": RED_WARN}),
            (caveat, {"size": 10, "color": MID, "italic": True}),
        ], line_spacing=1.18)

    # Chart
    img = CHARTS / "s27-literature-tools.png"
    add_image(slide, img, 1.0, 5.2, 11.5, 1.5)

    attribution(slide,
        "Источники: NotebookLM Google blog 2024 · Elicit (Ought.io) 2024 · Consensus.app 2024",
        y=6.95)

    add_notes(slide, "Зрелые литературные инструменты для научной работы. Три canonical examples.\n\nNotebookLM от Google — 17 миллионов пользователей по состоянию на 2025 год. Архитектура — RAG над PDF, которые вы загружаете. Помогает суммировать длинные документы, находить ссылки между ними, цитировать. Это очень полезный инструмент для синтеза материала. Но каждая цитата, которую он выдаёт, требует ручной проверки — модель может перепутать источник.\n\nElicit от Ought.io — 138 миллионов статей в индексе на 2024 год. Систематический обзор литературы за 4 раза быстрее ручного процесса. Очень полезен для аспирантов и постдоков, которые делают обзорные статьи. Но Elicit не делает метаанализ — то есть не делает количественную интеграцию результатов разных исследований. Это критично: систематический обзор без метаанализа — половина работы.\n\nConsensus.app — 200 миллионов статей. Поиск по утверждениям: вы задаёте вопрос (Does meditation help with anxiety?), получаете обзор того, что говорит литература. Очень удобно. Но низкая воспроизводимость в исходных данных — около 15% воспроизводимых исследований в психологии — означает, что фильтр обязателен.\n\nГлавная мысль слайда: это работающие инструменты augmentation. Это не магия и не панацея, но и не Galactica. Они расширяют возможности учёного навигировать по литературе. Финальная синтезирующая работа — за человеком.\n\nКлючевое ограничение для каждого: каждая цитата требует ручной проверки. AI помогает найти; человек проверяет, что найденное действительно говорит то, что заявлено. Это важно: даже когда модель работает хорошо, ошибки в цитировании всё равно встречаются.")


def s28_we2_bibliography(p):
    """s28 — walked example WE-2: bibliography verification 4 steps."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "WE-2: Соавтор прислал 47 LLM-цитат. Четыре шага проверки.")

    # Input task at top
    rounded_box(slide, 0.5, 1.5, 12.33, 0.6, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    text_box(slide, 0.5, 1.5, 12.33, 0.6,
             "Соавтор присылает черновик с 47 цитатами, явно сгенерированными LLM. Что делать?",
             size=14, bold=True, color=DEEP, italic=True,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    # 4 verification steps in flow (Phase 8: cost label Russified)
    steps = [
        ("1", "Проверка DOI", "Через crossref.org\nкаждый DOI существует?\nЕсли нет — фейк", MID,
         "Усилие: ~5 минут"),
        ("2", "Выборка релевантности", "5 случайных DOI:\nстатья говорит о теме?\nЕсли нет — выдумка", LIGHT,
         "Усилие: ~15 минут"),
        ("3", "Детектор GPTZero", "Текст рядом с цитатой —\nсгенерирован LLM?\nLLM = галлюцинации", TEAL,
         "Усилие: ~5 минут"),
        ("4", "Запросить исходные", "Файлы у соавтора:\nесть рабочая копия?\nЕсли нет — отказ", RED_WARN,
         "Усилие: ~20 минут"),
    ]
    card_w = 2.95
    gap = 0.1
    x0 = 0.5
    y_card = 2.4
    for i, (num, title, desc, color, cost) in enumerate(steps):
        x = x0 + i * (card_w + gap)
        rounded_box(slide, x, y_card, card_w, 2.7, fill=SURFACE, stroke=color, stroke_w=2)
        # Number
        circle(slide, x + (card_w - 0.7) / 2, y_card + 0.15, 0.7, 0.7, fill=color)
        text_box(slide, x, y_card + 0.15, card_w, 0.7, num,
                 size=28, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        # Title
        text_box(slide, x + 0.1, y_card + 1.0, card_w - 0.2, 0.4, title,
                 size=14, bold=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        # Desc
        multiline_box(slide, x + 0.15, y_card + 1.45, card_w - 0.3, 0.9, [
            (desc, {"size": 11, "color": MID, "italic": True}),
        ], align=PP_ALIGN.CENTER, line_spacing=1.18)
        # Cost
        rounded_box(slide, x + 0.4, y_card + 2.3, card_w - 0.8, 0.3,
                    fill=GOLD_TINT, stroke=GOLD, stroke_w=1)
        text_box(slide, x + 0.4, y_card + 2.3, card_w - 0.8, 0.3, cost,
                 size=10, bold=True, color=GOLD,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    # Decision branch
    rounded_box(slide, 0.5, 5.4, 12.33, 1.25, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 0.8, 5.5, 11.8, 1.1, [
        ("Критерий решения:", {"size": 13, "bold": True, "color": GOLD}),
        ("Если ≥3 фейковых цитаты найдены → отказ от соавторства. Усилие проверки: ~45 минут. Цена скандала: подорванная репутация на годы.",
            {"size": 14, "color": DEEP, "italic": True}),
        ("Профессиональная строгость > социальная вежливость.",
            {"size": 13, "bold": True, "color": GOLD}),
    ], line_spacing=1.18)

    attribution(slide,
        "Источники: рекомендации ICMJE 2024 · GPTZero · сервис crossref.org для проверки DOI",
        y=6.95)

    add_notes(slide, "WE-2 — третий разобранный пример лекции. Самая болезненная ситуация. Соавтор присылает вам черновик статьи перед подачей в журнал, и вы замечаете, что библиография подозрительно длинная и однородная. 47 цитат, и многие в одном академическом стиле, многие из журналов, которых вы не слышали. Это явно LLM-сгенерированная библиография.\n\nЧто делать. Социальная вежливость подсказывает «давайте подадим, не обижая соавтора». Профессиональная строгость говорит другое.\n\nЧетыре шага проверки. Каждый с критерием провала.\n\nШаг 1. DOI-resolve через crossref.org. Каждый DOI проверяется автоматически — существует ли. Любой DOI, которого нет в crossref, — фейк. Стоимость: 5 минут на скрипт + 47 DOI = 5 минут.\n\nШаг 2. Выборка релевантности. Беру 5 случайных DOI из тех, что прошли шаг 1, и читаю абстракты. Каждая статья должна реально говорить о теме, на которую её цитируют. Если статья реально существует, но не говорит про то, что заявлено в цитате — это confabulation, типичная ошибка LLM. Стоимость: 15 минут.\n\nШаг 3. GPTZero check. Беру весь текст черновика и пропускаю через GPTZero. Если детектор показывает > 80% AI-сгенерированности рядом с цитатами — это сигнал, что соавтор делегировал не только цитирование, но и сам анализ литературы LLM. Стоимость: 5 минут.\n\nШаг 4. Запросить исходные файлы у соавтора. Если соавтор не может показать рабочие записи, выписки, тетрадь чтения литературы — нет рабочей копии. Это значит — он не читал статьи, которые цитирует. Стоимость: 20 минут на разговор.\n\nКритерий решения. Три или больше фейковых цитат найдено — отказ от соавторства. Не «исправим вместе» — отказ. Потому что это сигнал глубокой проблемы методологии соавтора, которая всплывёт ещё несколько раз.\n\nСтоимость 45 минут проверки vs стоимость скандала несколько лет подорванной репутации. Выбор очевиден. Профессиональная строгость важнее социальной вежливости.")


def s29_frontiers_rat(p):
    """s29 — Frontiers retracted rat anatomy figure (Feb 2024)."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Frontiers 13 февраля 2024. «Protemns». «Zxpens». Отозвана через 3 дня.")

    # Big iconic typography for the made-up words (Phase 8: sized down to prevent overflow)
    rounded_box(slide, 0.5, 1.5, 12.33, 2.7, fill=SURFACE, stroke=RED_WARN, stroke_w=3)
    text_box(slide, 0.7, 1.65, 11.93, 0.4,
             "Несуществующие термины на сгенерированном Midjourney рисунке анатомии крысы:",
             size=13, bold=True, color=MID, italic=True)
    multiline_box(slide, 0.7, 2.15, 11.93, 1.95, [
        ("«PROTEMNS»  ·  «ZXPENS»  ·  «CELLLS»",
            {"size": 48, "bold": True, "color": RED_WARN}),
        ("", {"size": 8}),
        ("(на исходной фигуре подписаны как анатомические структуры)",
            {"size": 14, "italic": True, "color": MID}),
    ], align=PP_ALIGN.CENTER, line_spacing=1.0)

    # Хронология + lesson at bottom
    rounded_box(slide, 0.5, 4.4, 6.0, 2.25, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 0.7, 4.55, 5.6, 2.1, [
        ("Хронология:", {"size": 13, "bold": True, "color": GOLD}),
        ("", {"size": 4}),
        ("13 февраля 2024", {"size": 12, "bold": True, "color": MID}),
        ("Опубликована в Frontiers Cell Dev Biol",
            {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("13-15 февраля", {"size": 12, "bold": True, "color": MID}),
        ("Социальные сети vs reddit замечают",
            {"size": 11, "color": DEEP}),
        ("несуществующие термины + анатомические аномалии",
            {"size": 10, "italic": True, "color": SLATE}),
        ("", {"size": 4}),
        ("16 февраля 2024", {"size": 12, "bold": True, "color": RED_WARN}),
        ("Frontiers отозвал статью",
            {"size": 12, "bold": True, "color": RED_WARN}),
    ], line_spacing=1.15)

    rounded_box(slide, 6.7, 4.4, 6.33, 2.25, fill=SURFACE, stroke=RED_WARN, stroke_w=2)
    multiline_box(slide, 6.9, 4.55, 5.93, 2.1, [
        ("Что произошло:",
            {"size": 13, "bold": True, "color": RED_WARN}),
        ("", {"size": 4}),
        ("• Раскрытие использования AI было — авторы указали в статье",
            {"size": 11, "color": DEEP, "italic": True}),
        ("", {"size": 2}),
        ("• Рецензенты не проверили рисунки отдельно — текст одобрен, рисунки пропущены",
            {"size": 11, "color": DEEP, "italic": True}),
        ("", {"size": 2}),
        ("• Урок: рисунки требуют отдельной рецензии как самостоятельный артефакт",
            {"size": 11, "bold": True, "color": RED_WARN, "italic": True}),
    ], line_spacing=1.15)

    attribution(slide,
        "Источник: phys.org 2024-02 · VentureBeat февраль 2024 · Frontiers retraction note",
        y=6.95)

    add_notes(slide, "Frontiers «крыса» — самый виральный кейс провала peer review в эпоху AI в 2024 году. Разберём детально, потому что урок принципиальный.\n\n13 февраля 2024 года в журнале Frontiers in Cell and Developmental Biology была опубликована научная статья с фигурой, которая выглядела как «анатомическая иллюстрация репродуктивной системы крысы». Фигура была сгенерирована Midjourney и содержала несколько критических проблем.\n\nПервая. Анатомия откровенно неправильная. У крысы были изображены гигантские нерелевантные репродуктивные органы — изображение скорее напоминало сюрреалистическую вариацию.\n\nВторая. Подписи на фигуре — «protemns», «zxpens», «celllls» — несуществующие медицинские термины. Это типичная галлюцинация Midjourney на тексте: модель «знает», как выглядит научная подпись, но не имеет понимания семантики.\n\nСтатья прошла peer review. Авторы в paper явно указали использование Midjourney для фигур — раскрытие было. Но рецензенты, видимо, посмотрели на текст и пропустили фигуры. Через 13-15 февраля reddit и Twitter подхватили статью, виральный пост набрал миллионы просмотров.\n\n16 февраля 2024 года Frontiers отозвал статью с retraction note: использование AI было раскрыто авторами, но фигуры не должны были пройти peer review.\n\nГлавный урок инженеру: раскрытие AI в paper не освобождает от проверки. Peer review должен проверять figures как самостоятельный артефакт. Это значит — отдельно смотреть на каждую фигуру, проверять подписи, проверять анатомическую/физическую корректность. Сейчас это часто не делается, потому что figures исторически воспринимались как иллюстрация текста — но в эпоху AI figures могут быть полностью галлюцинированы.\n\nДля автора, использующего AI для научных figures: всегда проверяйте каждую подпись на наличие реальных терминов; всегда показывайте figure эксперту по специальности до подачи; всегда указывайте конкретный prompt и модель в caption.")


def s30_neurips_fake_citations(p):
    """s30 — NeurIPS 2025: 100+ fake citations in 53 accepted papers."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "NeurIPS 2025: 21 575 поданных, 5 290 принятых. 100+ фейк-цитат.")

    # Chart left
    img = CHARTS / "s30-neurips.png"
    add_image(slide, img, 0.3, 1.5, 7.5, 4.0)

    # Right column: scale + impact
    rounded_box(slide, 8.0, 1.5, 5.0, 4.0, fill=SURFACE, stroke=RED_WARN, stroke_w=2)
    multiline_box(slide, 8.2, 1.65, 4.6, 3.8, [
        ("Числа NeurIPS 2025:",
            {"size": 14, "bold": True, "color": RED_WARN}),
        ("", {"size": 6}),
        ("21 575 поданных статей",
            {"size": 13, "bold": True, "color": DEEP}),
        ("5 290 принятых",
            {"size": 13, "bold": True, "color": DEEP}),
        ("Доля принятых — 24,52%",
            {"size": 12, "italic": True, "color": SLATE}),
        ("", {"size": 6}),
        ("Анализ GPTZero Research:",
            {"size": 13, "bold": True, "color": RED_WARN}),
        ("100+ фейковых цитат",
            {"size": 14, "bold": True, "color": GOLD}),
        ("в 53 принятых статьях",
            {"size": 12, "color": DEEP}),
        ("(arxiv 2602.05930)",
            {"size": 10, "italic": True, "color": SLATE}),
        ("", {"size": 6}),
        ("Это около 1% принятых статей",
            {"size": 12, "color": MID, "italic": True}),
        ("содержат прямые фейки",
            {"size": 12, "color": MID, "italic": True}),
    ], line_spacing=1.15)

    # Bottom warning
    rounded_box(slide, 0.3, 5.7, 12.73, 1.0, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 0.6, 5.8, 12.13, 0.9, [
        ("Каскадный эффект:",
            {"size": 13, "bold": True, "color": GOLD}),
        ("Топовая конференция AI пропустила фейки = эти фейки войдут в обучающие данные следующих LLM = следующая итерация рецензирования увидит фейки как «легитимные источники». Это самовоспроизводящееся загрязнение литературы.",
            {"size": 13, "color": DEEP, "italic": True}),
    ], line_spacing=1.18)

    attribution(slide, "Источник: GPTZero Research arxiv 2602.05930 (2026)", y=6.95)

    add_notes(slide, "NeurIPS 2025 fake citations — самый недавний и самый тревожный кейс провала peer review.\n\nNeurIPS — крупнейшая конференция по машинному обучению. В 2025 году получила 21 575 поданных статей и приняла 5 290. Это acceptance rate 24,52%. Это огромный масштаб — несколько тысяч человек-рецензентов, каждая статья проходит 3-4 рецензента.\n\nВ начале 2026 года GPTZero Research опубликовал анализ — arxiv 2602.05930. Они проверили принятые 5 290 статей через комбинацию автоматических детекторов LLM-генерации и ручной проверки DOI. Результат: более 100 фейковых цитат проникли в 53 принятые статьи.\n\nЧто значит «фейковая цитата». Три категории. Первая — DOI не существует. Вторая — DOI существует, но статья не говорит то, что заявлено в цитирующей работе. Третья — соавторы статей-источников не существуют (LLM придумало имя).\n\nЭто 1% от accepted папок. Звучит мало. На самом деле — это ад. Потому что NeurIPS — топовая ML-конференция в мире, и эти статьи теперь будут цитироваться сотнями работ следующего поколения.\n\nКаскадный эффект. Это самовоспроизводящееся загрязнение литературы. Топовая конференция AI пропустила фейки. Эти фейки войдут в обучающие данные следующих LLM. Следующая итерация рецензирования увидит фейки как «легитимные источники» — модели рецензента «знают», что эти статьи прошли peer review NeurIPS.\n\nИ peer review масштабно не справился. 3-4 рецензента на статью с 47 цитатами не могут вручную проверить каждую — это часы работы. Они доверяют автору. В эпоху до AI это работало. В эпоху AI больше не работает.\n\nГлавный урок: per-cite manual verify обязателен в эпоху AI. Каждая принимающая инстанция (конференция, журнал) должна автоматически прогонять каждую цитату через DOI-resolve и спам-фильтр. Это инфраструктурная задача, которая ещё не решена в большинстве систем.\n\nДля автора — те же четыре шага из WE-2: DOI-resolve каждой цитаты, выборочная проверка релевантности, GPTZero check, исходные файлы.")


def s31_icmje_policies(p):
    """s31 — ICMJE rule + publisher policies matrix."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "ICMJE: AI не автор. Пять этических критериев — обязательны.")

    # 5 criteria header
    rounded_box(slide, 0.5, 1.5, 12.33, 0.55, fill=MID)
    text_box(slide, 0.5, 1.5, 12.33, 0.55,
             "5 критериев политик: Раскрытие · Проверяемость · Авторство · Ответственность · Воспроизводимость",
             size=14, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    # 5x4 matrix: criteria as rows, publishers as columns
    publishers = ["Springer", "Elsevier", "Frontiers", "Nature/ICMJE"]
    criteria = [
        ("Раскрытие AI", "Обязательно",
            "Обязательно", "Обязательно", "Обязательно"),
        ("Проверяемость", "Рекомендуется",
            "Рекомендуется", "Обязательно", "Обязательно"),
        ("AI как автор", "Запрещено",
            "Запрещено", "Запрещено", "Запрещено"),
        ("Ответственность", "Авторы (не AI)",
            "Авторы (не AI)", "Авторы (не AI)", "Авторы (не AI)"),
        ("Воспроизводимость", "Рекомендуется",
            "Обязательно", "Обязательно", "Обязательно"),
    ]
    col_w = 2.25
    x0 = 1.0
    y_header = 2.2
    # Column headers
    rectangle(slide, 0.5, y_header, 0.5 + 0.0, 0.5, fill=SURFACE)
    text_box(slide, 0.5, y_header, 0.5, 0.5, "—",
             size=11, color=SLATE, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    for i, pub in enumerate(publishers):
        x = x0 + 2.4 + i * col_w
        rectangle(slide, x, y_header, col_w - 0.05, 0.5, fill=MID)
        text_box(slide, x, y_header, col_w - 0.05, 0.5, pub,
                 size=12, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    # Rows
    y0 = 2.75
    row_h = 0.55
    for i, (crit, *vals) in enumerate(criteria):
        y = y0 + i * row_h
        # Criterion label
        if i % 2 == 0:
            rectangle(slide, 0.5, y, 12.33, row_h, fill=SURFACE)
        rectangle(slide, 0.5, y, 2.85, row_h, fill=DEEP if i % 2 == 0 else MID)
        text_box(slide, 0.6, y, 2.75, row_h, crit,
                 size=12, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE)
        # Values
        for j, val in enumerate(vals):
            x = x0 + 2.4 + j * col_w
            # Color coding
            if "Запрещено" in val:
                color = RED_WARN
                bold = True
            elif "Обязательно" in val:
                color = GOLD
                bold = True
            else:
                color = DEEP
                bold = False
            text_box(slide, x + 0.05, y, col_w - 0.1, row_h, val,
                     size=11, color=color, bold=bold,
                     anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    # Bottom takeaway
    rounded_box(slide, 0.5, 5.7, 12.33, 1.0, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 0.8, 5.8, 11.8, 0.85, [
        ("Главный приём для аспиранта/инженера:",
            {"size": 13, "bold": True, "color": GOLD}),
        ("Открывайте конкретную политику конкретного журнала перед подачей. AI как инструмент с раскрытием — OK; AI как автор — запрещён независимо от качества вывода и независимо от журнала.",
            {"size": 12, "color": DEEP, "italic": True}),
    ], line_spacing=1.18)

    attribution(slide,
        "Источники: рекомендации ICMJE 2024 · политики AI издательств Springer · Elsevier · Frontiers · Nature",
        y=6.95)

    add_notes(slide, "ICMJE и политики издательств — это инфраструктурный слой защиты от AI-злоупотреблений в науке. Разберём.\n\nICMJE — International Committee of Medical Journal Editors, основан в 1978 году. Это организация редакторов медицинских журналов, которая публикует Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals. Их рекомендации стали стандартом de facto для большинства научных журналов в мире.\n\nГлавное правило ICMJE 2023-2024: AI не может быть автором. Никаких исключений, никакой attribution «ChatGPT contributed». Авторство требует трёх вещей: (1) существенный intellectual вклад в работу, (2) одобрение финальной версии, (3) ответственность за content. AI ничего из этого юридически не может.\n\nПять критериев политик. Раскрытие — обязательно для всех крупных издательств. Использование AI должно быть указано в acknowledgments или methods. Конкретность важна: «использован ChatGPT для редактирования английского» — OK; «использован AI» — слишком расплывчато.\n\nПроверяемость — все ли утверждения проверяемы. У Frontiers и Nature это обязательно после кейса «крысы»; у Springer и Elsevier — рекомендация.\n\nAI как автор — запрещено абсолютно всеми. Springer, Elsevier, Frontiers, Nature, ICMJE — все одинаково. Даже если AI сделал значительную работу — нельзя.\n\nОтветственность — у всех у авторов-людей. Если AI галлюцинировал и это попало в paper — ответственность авторов, не AI.\n\nВоспроизводимость — у Elsevier, Frontiers, Nature обязательно (методология должна позволять воспроизведение); у Springer — рекомендация.\n\nДля аспиранта инженерный приём — открывайте конкретную политику конкретного журнала перед подачей. Эти политики часто меняются по мере роста AI. Не полагайтесь на старые знания — проверьте текущий standard.\n\nГлавный приём: AI как инструмент с раскрытием — OK; AI как автор — запрещён независимо от качества вывода и независимо от журнала.")


# ========== SECTION 5 — When AI not needed (s32-s37) ==========

def s32_section5_divider(p):
    """s32 — section 5 divider (Phase 8: top bar removed; tags 5→4; methodology strip)."""
    slide = blank(p)
    set_slide_bg(slide, SURFACE)

    text_box(slide, 0.5, 1.5, 5.0, 3.0, "§5",
             size=200, bold=True, color=TEAL, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)
    multiline_box(slide, 5.5, 1.7, 7.3, 4.0, [
        ("Раздел 5", {"size": 22, "bold": True, "color": MID}),
        ("Когда AI", {"size": 42, "bold": True, "color": DEEP}),
        ("не нужен", {"size": 42, "bold": True, "color": DEEP}),
        ("в науке", {"size": 30, "color": LIGHT, "italic": True}),
        ("", {"size": 10}),
        ("Критерии. Альтернативы.",
            {"size": 16, "color": DEEP}),
        ("Разобранный пример катализатора.",
            {"size": 16, "color": DEEP}),
    ], line_spacing=1.2)

    # Phase 8: trim 5→4 tags + narrower
    tags = [
        ("4 критерия", LIGHT),
        ("WE-3 катализатор", GOLD),
        ("5 зрелых альтернатив", MID),
        ("3 вопроса вендору", TEAL),
    ]
    y_tag = 5.6
    x = 5.5
    for label, color in tags:
        w = len(label) * 0.11 + 0.25
        rounded_box(slide, x, y_tag, w, 0.4, fill=color, stroke=color, stroke_w=0)
        text_box(slide, x, y_tag, w, 0.4, label,
                 size=10, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        x += w + 0.08

    attribution(slide, "Когда применять AI — и когда говорить нет.", y=6.95)

    add_notes(slide, "Раздел 5 — Когда AI не нужен в науке. Самая важная часть лекции с инженерной точки зрения. Помните миссию курса: учить когда применять AI, а когда — нет. Здесь мы конкретизируем «когда нет».\n\nЧетыре категории критериев. Открытый мир без эталонной разметки. Недопредставлен в обучении. Нельзя проверить независимо. Этический риск. Любое срабатывание — повод остановиться.\n\nПять зрелых альтернатив AI работают 30-70 лет. BO+GP в эксперименте — 40 и 60 лет. DFT+MD в материалах — 60+ лет. Классическая статистика в анализе — век и более. OR-Tools в оптимизации — 70+ лет. Человеческое рецензирование — несколько веков.\n\nРазобранный пример WE-3 — катализатор окисления пропилена. Применим пятишаговую рамку, которую мы построили в начале лекции. И покажем три вопроса к вендору AI-инструмента.")


def s33_four_criteria(p):
    """s33 — 4 categories when AI not needed."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Четыре категории «AI не нужен». Любое срабатывание — повод остановиться.")

    # 2x2 grid of criteria
    criteria = [
        ("1", "Открытый мир без эталона",
         "Пространство решений не описано, проверка требует выхода за систему",
         "Пример: гипотеза о роли соц.сетей в политике",
         RED_WARN),
        ("2", "Недопредставлен в обучении",
         "Ваш случай далеко от распределения обучающих данных модели",
         "Пример: новый вид белка не из стандартных семей",
         LIGHT),
        ("3", "Нельзя проверить независимо",
         "Нет альтернативного метода или эксперимента для валидации",
         "Пример: предсказание единственного измерения",
         TEAL),
        ("4", "Этический риск",
         "Использование AI создаёт риск вреда или нарушения норм",
         "Пример: AI в принятии врачебных решений без врача",
         GOLD),
    ]
    card_w = 6.05
    card_h = 2.4
    gap_x = 0.23
    gap_y = 0.25
    x0 = 0.5
    y0 = 1.5
    for i, (num, title, desc, ex, color) in enumerate(criteria):
        row = i // 2
        col = i % 2
        x = x0 + col * (card_w + gap_x)
        y = y0 + row * (card_h + gap_y)
        rounded_box(slide, x, y, card_w, card_h, fill=SURFACE, stroke=color, stroke_w=2)
        # Number circle
        circle(slide, x + 0.2, y + 0.15, 0.9, 0.9, fill=color)
        text_box(slide, x + 0.2, y + 0.15, 0.9, 0.9, num,
                 size=36, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        # Title
        text_box(slide, x + 1.25, y + 0.2, card_w - 1.4, 0.45, title,
                 size=18, bold=True, color=DEEP)
        # Desc
        multiline_box(slide, x + 1.25, y + 0.7, card_w - 1.4, 1.6, [
            (desc, {"size": 13, "color": MID, "italic": True}),
            ("", {"size": 6}),
            (ex, {"size": 12, "color": DEEP}),
        ], line_spacing=1.2)

    # Bottom takeaway
    rounded_box(slide, 0.5, 6.4, 12.33, 0.5, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    text_box(slide, 0.5, 6.4, 12.33, 0.5,
             "Бонус: пятый критерий — закрытая физика проще доступна (DFT, MD, BO+GP). AI становится переусложнением.",
             size=12, bold=True, color=GOLD, italic=True,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    attribution(slide, "Это диагностический вопросник. Любое срабатывание — пауза + рассмотрение альтернативы.", y=6.95)

    add_notes(slide, "Четыре категории «AI не нужен» — это диагностический вопросник для любого нового научного применения AI. Любой ответ «да» на эти вопросы — это повод остановиться и пересмотреть выбор инструмента.\n\nКритерий 1 — открытый мир без эталонной разметки. Это самый строгий критерий. Если пространство возможных решений не описано формально (например, через физические уравнения), и проверка результата требует выхода за пределы системы (например, длительные клинические исследования), AI не работает надёжно. Пример — гипотеза о роли социальных сетей в политическом поведении. Слишком открытая задача, нет ground truth.\n\nКритерий 2 — недопредставлен в обучении. Покрытие. Ваш конкретный случай находится далеко от распределения обучающих данных модели. Это сложно проверить, но критически важно. Пример — новый вид белка, не похожий на стандартные семьи в PDB. AlphaFold там даст предсказание, но с низкой надёжностью. Признаки — модель уверена в своём ответе на очень новом случае; это подозрительно.\n\nКритерий 3 — нельзя проверить независимо. Нет альтернативного метода или эксперимента для валидации. Если у вас есть только одно измерение и одна модель предсказывает, что измерение должно быть таким, вы не можете отличить «модель угадала» от «модель ошиблась». Пример — предсказание единственного измерения без возможности повторения.\n\nКритерий 4 — этический риск. Использование AI создаёт риск вреда или нарушения этических норм. Пример — AI в принятии врачебных решений без врача. ICMJE и медицинские профессиональные сообщества здесь однозначны: AI как инструмент с врачом — OK; AI как замена врача — нельзя.\n\nБонусный пятый критерий — закрытая физика проще доступна. Если у вас задача катализа, и DFT даёт надёжное предсказание, AI становится переусложнением. Зачем тренировать нейросеть, если quantum chemistry уже даёт ответ?\n\nДля любого нового научного применения AI пройдите эти пять вопросов. Любое «да» — пауза, рассмотрение не-AI альтернативы.")


def s34_we3_catalyst(p):
    """s34 — walked example WE-3: catalyst design with BO+GP."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "WE-3 катализатор: GP-BO 5000 → DFT 50 → лаба 3. 4 месяца vs год.")

    # Catalyst image
    add_image(slide, IMG / "s34-catalysts.jpg", 0.5, 1.5, 4.0, 2.7)
    attribution(slide, "© Wikimedia · промышленные катализаторы (CC-BY-SA)", x=0.5, y=4.25, w=4.0)

    # Funnel diagram (custom)
    x_fun = 4.8
    # Step 1: 5000 candidates
    rectangle(slide, x_fun, 1.5, 8.0, 0.6, fill=LIGHT)
    text_box(slide, x_fun, 1.5, 8.0, 0.6,
             "5 000 кандидатов · GP-BO предлагает по композиции",
             size=13, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    # Arrow down
    down_arrow(slide, x_fun + 3.8, 2.15, 0.4, 0.3, fill=DEEP)
    # Step 2: DFT 50
    rectangle(slide, x_fun + 1.0, 2.55, 6.0, 0.6, fill=MID)
    text_box(slide, x_fun + 1.0, 2.55, 6.0, 0.6,
             "50 высокоранжированных · DFT (VASP) расчёты энтальпии",
             size=13, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    down_arrow(slide, x_fun + 3.8, 3.2, 0.4, 0.3, fill=DEEP)
    # Step 3: 5 synthesised
    rectangle(slide, x_fun + 2.0, 3.6, 4.0, 0.6, fill=TEAL)
    text_box(slide, x_fun + 2.0, 3.6, 4.0, 0.6,
             "5 синтезированы · лабораторно",
             size=13, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    down_arrow(slide, x_fun + 3.8, 4.25, 0.4, 0.3, fill=DEEP)
    # Step 4: 3 confirmed
    rectangle(slide, x_fun + 3.0, 4.65, 2.0, 0.6, fill=GOLD)
    text_box(slide, x_fun + 3.0, 4.65, 2.0, 0.6,
             "3 подтверждены",
             size=13, bold=True, color=DEEP,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    # Bottom: tools + timeline
    rounded_box(slide, 0.5, 5.4, 6.0, 1.25, fill=SURFACE, stroke=LIGHT, stroke_w=2)
    multiline_box(slide, 0.7, 5.55, 5.6, 1.05, [
        ("Конкретные инструменты:", {"size": 13, "bold": True, "color": MID}),
        ("• VASP — DFT расчёты", {"size": 11, "color": DEEP}),
        ("• BoTorch / GPyTorch — байесовская оптимизация",
            {"size": 11, "color": DEEP}),
        ("• Materials Project — справочная база",
            {"size": 11, "color": DEEP}),
    ], line_spacing=1.18)

    rounded_box(slide, 6.7, 5.4, 6.33, 1.25, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 6.9, 5.55, 5.93, 1.05, [
        ("Сравнение времени:", {"size": 13, "bold": True, "color": GOLD}),
        ("• Вручную: 1-2 кандидата в год", {"size": 11, "color": DEEP}),
        ("• GP-BO + DFT + лаба: 3 за 4 месяца",
            {"size": 11, "bold": True, "color": GOLD}),
        ("• Ускорение: 10-15× при той же точности",
            {"size": 12, "bold": True, "color": GOLD, "italic": True}),
    ], line_spacing=1.18)

    attribution(slide,
        "Источники: Merchant et al. Nature 2023 (GNoME) · Mockus 1989 (BO) · Kohn 1965 (DFT)",
        y=6.95)

    add_notes(slide, "WE-3 — наш четвёртый и финальный разобранный пример. Применим пятишаговую рамку из начала лекции к конкретной задаче. Это эталонный кейс «AI работает осознанно».\n\nЗадача: подобрать катализатор для окисления пропилена в акролеин. Это промышленно важная реакция — акролеин используется в синтезе акриловой кислоты, которая является базовым сырьём для полимеров.\n\nШаг 1 — classify. Это Hypothesis+Design ступени лестницы. Закрытый мир: пространство кандидатов катализаторов описано (металл + оксидная подложка + промоторы), физика реакций может быть рассчитана через DFT с приемлемой точностью.\n\nШаг 2 — map alternatives. Что есть на рынке? Sakana AI Scientist может предложить 50 кандидатов. BO+GP с initial training на Materials Project — может ранжировать 5000 кандидатов и предложить топ-50 для углублённой проверки. BO+GP лучше: математически обоснованная неопределённость, доказанная работа в катализе (Shields Nature 2021).\n\nШаг 3 — four criteria check. Закрытый мир? Да, DFT даёт ground truth. Покрытие? Materials Project содержит большое количество катализаторов в этой области. Независимая проверка? Да, через synthesis + reactor measurements. Этический риск? Нет. BO+GP проходит все 4 критерия.\n\nШаг 4 — HITL design. Аспирант проверяет каждый из 50 DFT-результатов: разумна ли предсказанная активная фаза, нет ли очевидных ошибок (например, отрицательная энтальпия активации). Это останавливает каскад ошибок.\n\nШаг 5 — pre-publication verify. 5 синтезированных кандидатов тестируются в реакторе. 3 показывают предсказанные характеристики. Эти 3 — открытие, которое можно публиковать.\n\nКонкретные инструменты. VASP — стандартный софт DFT расчётов в материаловедении. BoTorch плюс GPyTorch — Python-библиотеки байесовской оптимизации. Materials Project — справочная база материалов.\n\nСравнение времени. Традиционно постдок открывает 1-2 кандидата катализатора в год. С GP-BO + DFT + автономной лабой — 3 кандидата за 4 месяца. Ускорение 10-15× при той же точности.\n\nЭто эталонный пример «AI работает осознанно». Зрелая байесовская оптимизация, проверенная физика DFT, человек в петле, проверка до публикации. Никаких LLM, никакого «AI Scientist».")


def s35_alternatives_matrix(p):
    """s35 — 5 mature non-AI alternatives matrix."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Пять зрелых альтернатив AI работают 30-70 лет. Не запасные — основные.")

    # 5x4 matrix
    cols = [
        ("Альтернатива", 0.5, 2.6, DEEP),
        ("Год / Возраст", 3.2, 1.6, MID),
        ("Область", 4.85, 2.5, MID),
        ("Сила vs AI", 7.4, 2.5, GOLD),
        ("Типичная задача", 9.95, 3.08, MID),
    ]
    y_header = 1.5
    for label, x, w, color in cols:
        rectangle(slide, x, y_header, w - 0.05, 0.5, fill=color)
        text_box(slide, x, y_header, w - 0.05, 0.5, label,
                 size=12, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    rows = [
        ("BO+GP", "1989 / 36 лет", "Эксперимент + ML",
         "Математическая обоснованность", "Подбор условий реакций"),
        ("DFT + MD", "1965 / 60 лет", "Материалы + химия",
         "Первопринципный расчёт", "Энергия активации катализатора"),
        ("Классич. статистика", "1925 / век", "Анализ данных",
         "Калиброванные p-values + ANOVA",
         "Сравнение групп в эксперименте"),
        ("OR-Tools / Simplex", "1947 / 78 лет", "Оптимизация",
         "Гарантия глобального оптимума",
         "Планирование лабораторных ресурсов"),
        ("Peer review", "Несколько веков", "Рецензия + публикации",
         "Калиброванная коллективная экспертиза",
         "Независимая проверка результата"),
    ]
    y0 = 2.05
    row_h = 0.85
    for i, (name, age, domain, strength, task) in enumerate(rows):
        y = y0 + i * row_h
        if i % 2 == 1:
            rectangle(slide, 0.5, y, 12.53, row_h, fill=SURFACE)
        text_box(slide, 0.6, y, 2.5, row_h, name,
                 size=14, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, 3.3, y, 1.5, row_h, age,
                 size=12, color=MID, anchor=MSO_ANCHOR.MIDDLE, italic=True)
        text_box(slide, 4.95, y, 2.4, row_h, domain,
                 size=11, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, 7.5, y, 2.4, row_h, strength,
                 size=11, bold=True, color=GOLD, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, 10.05, y, 2.98, row_h, task,
                 size=11, color=MID, italic=True, anchor=MSO_ANCHOR.MIDDLE)

    # Bottom takeaway
    rounded_box(slide, 0.5, 6.4, 12.33, 0.55, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    text_box(slide, 0.5, 6.4, 12.33, 0.55,
             "Зрелые методы не устаревают — они становятся частью интегрированного набора. AI расширяет инструментарий, не заменяет его.",
             size=13, bold=True, color=DEEP, italic=True,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    add_notes(slide, "Пять зрелых альтернатив AI работают десятилетиями. Это критический список, который инженер должен помнить, когда оценивает применение AI в науке.\n\nБайесовская оптимизация + гауссовский процесс. 1989 год — формализация Mockus. 36 лет в активном использовании. Область — эксперимент с машинным обучением. Сила vs AI — математическая обоснованность. Типичная задача — подбор условий органических реакций, оптимизация катализаторов.\n\nDFT + MD. Density Functional Theory разработана Kohn в 1965 году, Нобелевская премия 1998 года. Molecular Dynamics — Alder 1957 год. Оба — 60+ лет. Область — материалы и химия. Сила — первопринципный расчёт энергии активации, структуры, динамики. Не предсказание, а расчёт от physical laws. Типичная задача — энергия активации катализатора, фазовая диаграмма сплава.\n\nКлассическая статистика — Fisher ANOVA 1925, t-test 1908. Век и более. Область — анализ данных. Сила — калиброванные p-values, ANOVA для сравнения групп, теория power analysis. Типичная задача — сравнение групп в клиническом эксперименте, проверка значимости эффекта.\n\nOR-Tools / Simplex / linear programming. Dantzig 1947 год. 78 лет. Область — оптимизация. Сила — гарантия глобального оптимума при линейных ограничениях. Типичная задача — планирование лабораторных ресурсов, маршрутизация автоматизированных систем.\n\nPeer review. Несколько веков, формализован в XIX. Область — рецензирование. Сила — калиброванная коллективная экспертиза. Это институциональный метод проверки качества. Никакой AI не заменит коллег по специальности.\n\nГлавный приём — зрелые методы не устаревают. Они становятся частью интегрированного инструментария. AI расширяет, но не заменяет. Когда AI работает с DFT (как в GNoME) — это работает; когда AI пытается заменить DFT — это маркетинг.")


def s36_vendor_questions_framework(p):
    """s36 — 3 vendor questions + 5-step framework summary (Phase 8: Russified)."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "3 вопроса вендору + 5-шаговая рамка — применимый артефакт для кармана.")

    # 3 vendor questions left
    rounded_box(slide, 0.5, 1.5, 6.0, 5.0, fill=SURFACE, stroke=RED_WARN, stroke_w=2)
    text_box(slide, 0.7, 1.65, 5.6, 0.5,
             "3 вопроса к поставщику AI",
             size=18, bold=True, color=RED_WARN)
    questions = [
        ("Q1", "Покажите эталон до AI", "Какие результаты были до внедрения AI? Без базового уровня нельзя оценить улучшение"),
        ("Q2", "Покажите воспроизводимость", "Можно ли получить тот же результат через альтернативный метод? Если нет — это не наука"),
        ("Q3", "Покажите случаи провала", "Где модель ошибается? Где галлюцинирует? Если вендор не знает — он лжёт"),
    ]
    y_q = 2.3
    for num, title, desc in questions:
        rounded_box(slide, 0.7, y_q, 5.6, 1.3, fill=WHITE, stroke=LIGHT, stroke_w=1.5)
        circle(slide, 0.85, y_q + 0.15, 0.6, 0.6, fill=RED_WARN)
        text_box(slide, 0.85, y_q + 0.15, 0.6, 0.6, num,
                 size=16, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        multiline_box(slide, 1.6, y_q + 0.1, 4.6, 1.1, [
            (title, {"size": 13, "bold": True, "color": DEEP}),
            (desc, {"size": 10, "color": MID, "italic": True}),
        ], line_spacing=1.18)
        y_q += 1.4

    # 5-step framework right
    rounded_box(slide, 6.83, 1.5, 6.0, 5.0, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    text_box(slide, 7.03, 1.65, 5.6, 0.5,
             "5-шаговая рамка решения",
             size=18, bold=True, color=GOLD)
    steps = [
        ("1", "Классифицируй", "Открытый или закрытый мир"),
        ("2", "Отобрази альтернативы", "Не-AI и другие AI-методы"),
        ("3", "4 критерия", "Открытость · покрытие · проверяемость · этика"),
        ("4", "Дизайн HITL", "Где человек останавливает конвейер"),
        ("5", "Проверка до публикации", "Каждое измеримое — независимо"),
    ]
    y_s = 2.3
    for num, title, desc in steps:
        rounded_box(slide, 7.03, y_s, 5.6, 0.75, fill=WHITE, stroke=GOLD, stroke_w=1.5)
        circle(slide, 7.15, y_s + 0.1, 0.55, 0.55, fill=GOLD)
        text_box(slide, 7.15, y_s + 0.1, 0.55, 0.55, num,
                 size=18, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        multiline_box(slide, 7.85, y_s + 0.05, 4.7, 0.7, [
            (title, {"size": 12, "bold": True, "color": DEEP}),
            (desc, {"size": 10, "color": MID, "italic": True}),
        ], line_spacing=1.18)
        y_s += 0.83

    attribution(slide,
        "Применима к любой задаче из любого раздела лекции. Распечатайте и носите с собой.",
        y=6.95)

    add_notes(slide, "Финальный applicable artefact лекции. Три вопроса к вендору AI плюс пятишаговая рамка решения. Это то, что можно распечатать и держать в кармане.\n\nТри вопроса к поставщику AI. Когда вы оцениваете коммерческий AI-инструмент для научной работы, задайте эти три вопроса. Если вендор не отвечает на любой из них прямо — это сигнал не покупать.\n\nQ1: покажите эталон до AI. Какие результаты были у вашей лаборатории до того, как вы внедрили этот AI-инструмент? Без baseline невозможно оценить, действительно ли AI улучшает работу или просто меняет процесс. Это самый базовый эксперимент в науке: измерение до vs после. Если вендор не показывает before/after — он либо не измерял, либо измерил и результаты неудобные.\n\nQ2: покажите воспроизводимость. Можно ли получить такой же результат через альтернативный, не-AI метод? Если нет — это не наука. Это или артефакт модели, или результат, который не выдержит независимой проверки. Воспроизводимость через альтернативный метод — фундаментальное требование любой научной публикации.\n\nQ3: покажите случаи провала. Где модель ошибается? В каких сценариях галлюцинирует? Какие классы задач за пределами её возможностей? Если вендор отвечает «модель работает идеально» — он лжёт. Любая ML-модель имеет области надёжности и области сбоев. Если вендор не знает этих границ, он не понимает свой продукт.\n\nПять шагов рамки решения. Помните их из слайдов 5 и 33. Один — классифицируй задачу. Два — отобрази все альтернативы, включая зрелые не-AI. Три — четыре критерия (открытый мир, покрытие, проверяемость, этика). Четыре — спроектируй шлюзы HITL. Пять — проверь до публикации.\n\nЭти восемь пунктов — applicable artefact лекции. Распечатайте, носите с собой. Любой раз, когда коллега или вендор предлагает «применить AI к научной задаче», доставайте эту карточку и проходите по пунктам. Это занимает 10 минут. Это спасает месяцы потерянной работы.")


def s37_ru_context(p):
    """s37 — Russian context: AIRI / Sber / Yandex + decree №490+124."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Российский контекст: AIRI · Sber · Yandex Research + Указ № 490 + № 124.")

    # 3 institutions left column
    text_box(slide, 0.5, 1.5, 6.5, 0.4,
             "Три институциональных центра",
             size=15, bold=True, color=DEEP)

    institutions = [
        ("AIRI", "Институт ИИ (Россия) · независимый · с 2021",
         "AI4Science: структура белков, медицинская визуализация, климатическое моделирование.",
         "Nature Communications 2024-2025",
         IMG / "s37-sber.jpg"),
        ("Sber AI Lab", "Исследовательское направление в Сбере",
         "Научные инструменты: климат, прогноз спроса на энергию; коллаборации с институтами.",
         "Кластер ≈5 000 H100 (откр. данные 2024)",
         IMG / "s37-sber.jpg"),
        ("Yandex Research", "Академические публикации + open-source",
         "YaLM-100B (2022), RuGPT. Открытые веса для русскоязычных научных инструментов.",
         "ICLR · NeurIPS · ICML 2023-2025",
         IMG / "s37-yandex.jpg"),
    ]
    y_i = 1.95
    for name, vendor, scope, marker, img_path in institutions:
        rounded_box(slide, 0.5, y_i, 6.5, 1.3, fill=SURFACE, stroke=LIGHT, stroke_w=1.5)
        multiline_box(slide, 0.7, y_i + 0.1, 6.1, 1.15, [
            (name, {"size": 15, "bold": True, "color": DEEP}),
            (vendor, {"size": 10, "italic": True, "color": SLATE}),
            ("", {"size": 2}),
            (scope, {"size": 11, "color": MID}),
            (marker, {"size": 10, "italic": True, "color": GOLD}),
        ], line_spacing=1.15)
        y_i += 1.4

    # Regulatory + gap right column
    rounded_box(slide, 7.2, 1.5, 5.8, 2.8, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 7.4, 1.65, 5.4, 2.6, [
        ("Регуляторная рамка:",
            {"size": 14, "bold": True, "color": GOLD}),
        ("", {"size": 4}),
        ("Указ № 490 от 10 октября 2019",
            {"size": 12, "bold": True, "color": MID}),
        ("Национальная стратегия развития AI до 2030",
            {"size": 10, "color": DEEP, "italic": True}),
        ("", {"size": 4}),
        ("Указ № 124 от 15 февраля 2024",
            {"size": 12, "bold": True, "color": MID}),
        ("Обновление: AI4Science приоритет",
            {"size": 10, "color": DEEP, "italic": True}),
        ("", {"size": 6}),
        ("РНФ программа AI4Science 2024-",
            {"size": 11, "bold": True, "color": DEEP}),
        ("Гранты на применение AI в исследованиях",
            {"size": 10, "italic": True, "color": SLATE}),
    ], line_spacing=1.15)

    # Compute + citation gap
    rounded_box(slide, 7.2, 4.45, 5.8, 2.15, fill=SURFACE, stroke=RED_WARN, stroke_w=2)
    multiline_box(slide, 7.4, 4.6, 5.4, 2.0, [
        ("Объективные разрывы:",
            {"size": 14, "bold": True, "color": RED_WARN}),
        ("", {"size": 4}),
        ("Вычисления: 20-50× меньше США",
            {"size": 12, "bold": True, "color": DEEP}),
        ("(оценка частных GPU-кластеров)",
            {"size": 10, "italic": True, "color": SLATE}),
        ("", {"size": 4}),
        ("Цитируемость: 3× недопредставлены",
            {"size": 12, "bold": True, "color": DEEP}),
        ("в Semantic Scholar по сравнению с EU",
            {"size": 10, "italic": True, "color": SLATE}),
        ("", {"size": 4}),
        ("Аспиранту: фокус на узкую задачу",
            {"size": 11, "bold": True, "color": GOLD}),
        ("(BO+GP, не фундаментальные модели)",
            {"size": 10, "italic": True, "color": MID}),
    ], line_spacing=1.15)

    attribution(slide,
        "Источники: AIRI publications 2024 · Указ № 490/2019 · Указ № 124/2024 · РНФ AI4Science",
        y=6.95)

    add_notes(slide, "Российский контекст AI в науке. Три институциональных центра, два указа президента, и реальные ограничения, которые надо понимать аспиранту.\n\nAIRI — Институт искусственного интеллекта, основан в 2021 году. Независимая организация (не Сбер, не НТИ), один из ведущих российских AI-исследовательских центров. Работает по нескольким направлениям AI4Science: предсказание структуры белка с открытыми конкурентами AlphaFold и применением к российским биотехнологическим вопросам; медицинская визуализация в сотрудничестве с российскими медицинскими центрами; климатическое моделирование арктических регионов. Публикации в Nature Communications 2024-2025.\n\nSber AI Lab — исследовательское направление в Сбере. Применения AI4Science: климатическое моделирование арктических регионов и Сибири; прогнозирование суточного потребления электроэнергии ЕЭС России; сотрудничество с исследовательскими институтами по AI в материалах. Внутренний кластер оценивается приблизительно в 5 тысяч GPU H100 по открытым данным 2024 года — сопоставим с верхним децилем глобальных академических кластеров. Фокус Сбера — банковские задачи; AI4Science — вторичное направление через коллаборации.\n\nYandex Research — академические публикации плюс open-source. YaLM-100B 2022 года — открытая большая языковая модель на русском, серия RuGPT. Сильный международный послужной список: ICLR, NeurIPS, ICML 2023-2025. Это делает Yandex Research наиболее международно-видимым российским направлением AI-исследований. Открытые веса критичны: они позволяют российским аспирантам строить русскоязычные научные инструменты без зависимости от закрытых вендорских API.\n\nРегуляторная рамка. Указ Президента РФ № 490 от 10 октября 2019 года утвердил Национальную стратегию развития искусственного интеллекта до 2030 года; обновлён Указом № 124 от 15 февраля 2024 года с расширенными целевыми показателями и приоритетом AI4Science. Гранты РНФ AI4Science 2024-2025 — отдельный приоритет — 20-30 грантов ежегодно по 5-15 миллионов рублей.\n\nСтруктурные разрывы. Первый — вычислительный. Обучение фундаментальной модели уровня AlphaFold 3 оценивается в 10-50 миллионов долларов; один раунд — 1-3 миллиона. Сравните с типичным грантом РНФ — около 50-150 тысяч долларов, что хватает на 2-5 процентов одного раунда. Разрыв 20-50 раз.\n\nВторой разрыв — видимость цитирования. Русскоязычные публикации составляют менее 1 процента корпуса Semantic Scholar (214 миллионов статей) против 2-3 процентов мирового научного вывода России. Это 3-кратное недопредставление в данных, на которых обучаются LLM. Инструменты литературного анализа на LLM систематически пропускают русскоязычные исследования.\n\nЧто это значит для аспиранта. Знай классические методы — BO+GP, DFT, статистика — массовые глобально и в РФ. Используй открытые фундаментальные модели — широко доступны, не зависят от вендоров. Следи за AIRI / Sber AI Lab / Yandex Research — отечественные сильные стороны. Понимай ограничения compute и citation. Балансируй международные и российские публикации.")


def s38_qa(p):
    """s38 — Q&A dedicated slide; recap ladder + failure callback."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Q&A. Завтра вы получаете LLM-сгенерированную библиографию. Что делаете?")

    # Big Q&A panel
    rounded_box(slide, 0.5, 1.5, 12.33, 2.2, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.5)
    multiline_box(slide, 0.8, 1.7, 11.8, 1.95, [
        ("Сценарий-вопрос:",
            {"size": 13, "bold": True, "color": GOLD, "italic": True}),
        ("Соавтор присылает черновик статьи с 47 LLM-сгенерированными цитатами.",
            {"size": 18, "bold": True, "color": DEEP}),
        ("Что делаете?",
            {"size": 22, "bold": True, "color": GOLD}),
        ("", {"size": 4}),
        ("→ DOI-проверка каждой ссылки.",
            {"size": 13, "color": DEEP}),
        ("→ Запрос исходных файлов у соавтора.",
            {"size": 13, "color": DEEP}),
        ("→ Отказ от соавторства если не можете проверить.",
            {"size": 13, "bold": True, "color": GOLD, "italic": True}),
    ], line_spacing=1.2)

    # Recap of ladder + positive recap
    rounded_box(slide, 0.5, 4.0, 6.0, 2.6, fill=SURFACE, stroke=LIGHT, stroke_w=2)
    multiline_box(slide, 0.7, 4.15, 5.6, 2.4, [
        ("Лестница цикла — краткое повторение:",
            {"size": 13, "bold": True, "color": MID}),
        ("", {"size": 6}),
        ("1 Гипотеза — расширение, не автономия",
            {"size": 11, "color": DEEP}),
        ("2 Планирование — автономного нет",
            {"size": 11, "color": DEEP}),
        ("3 Эксперимент — Нобель ✓ + Палгрейв ✗",
            {"size": 12, "bold": True, "color": GOLD}),
        ("4 Анализ — узкое ML работает",
            {"size": 11, "color": DEEP}),
        ("5 Текст — расширение с проверкой",
            {"size": 11, "color": DEEP}),
        ("6 Рецензия — запрещён финально",
            {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("Цикл, не прямая.",
            {"size": 12, "bold": True, "color": GOLD, "italic": True}),
    ], line_spacing=1.15)

    # Positive recap right
    rounded_box(slide, 6.7, 4.0, 6.33, 2.6, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 6.9, 4.15, 5.93, 2.4, [
        ("Реальные прорывы — не отменяемые провалами в Тексте и Рецензии:",
            {"size": 13, "bold": True, "color": GOLD}),
        ("", {"size": 4}),
        ("• AlphaFold — Нобель по химии 2024",
            {"size": 12, "color": DEEP}),
        ("• 200M структур в AlphaFold DB (1000× PDB)",
            {"size": 12, "color": DEEP}),
        ("• GNoME — 380K стабильных материалов",
            {"size": 12, "color": DEEP}),
        ("• Aurora — 5000× быстрее эталона",
            {"size": 12, "color": DEEP}),
        ("• AlphaProof — серебро на IMO 2024",
            {"size": 12, "color": DEEP}),
        ("• A-Lab — 41 из 58 за 17 дней",
            {"size": 12, "color": DEEP}),
        ("", {"size": 4}),
        ("Это прорывы. И требуют человека в петле.",
            {"size": 12, "bold": True, "color": GOLD, "italic": True}),
    ], line_spacing=1.15)

    attribution(slide,
        "Открыто для вопросов · ответы по конкретным кейсам и инструментам",
        y=6.95)

    add_notes(slide, "Q&A слайд. Самый острый вопрос — что делать с фейк-цитатами соавтора. И recap лестницы плюс позитивный список прорывов.\n\nСценарий. Завтра — буквально завтра — вы получаете e-mail от коллеги. Он соавтор по статье. Черновик статьи готов, в нём 47 цитат. По характеру цитирования и однородности стиля вы понимаете, что библиография собрана LLM.\n\nЧто делать.\n\nПервое — DOI-проверка каждой ссылки через crossref.org. Скрипт. 5 минут.\n\nВторое — выборочная проверка релевантности. 5 случайных DOI, проверяем, что статьи действительно говорят о теме цитирования. 15 минут.\n\nТретье — запрос исходных файлов у соавтора. «Покажи свою тетрадь чтения по этим статьям». Если нет рабочей копии — нет реального чтения.\n\nЧетвёртое — критерий решения. Три или более фейковых цитат — отказ от соавторства. Не «исправим вместе» — отказ. Профессиональная строгость важнее социальной вежливости.\n\nRecap лестницы. Шесть ступеней. Hypothesis — расширение, но не автономия (Sakana 1%). Design — autonomous discovery? Пока нет (Coscientist делает синтез известных). Experiment — самый сильный успех: Нобель AlphaFold плюс трещина Палгрейва-Шупа. Analyse — узкое ML работает предсказуемо. Write — augmentation с обязательной проверкой каждой ссылки. Review — финально запрещён политикой ICMJE.\n\nЛестница циклическая, не прямая. Рецензент возвращает к анализу; анализ порождает новую гипотезу.\n\nПозитивный recap. Реальные прорывы существуют, и они не отменяемы провалами в Write+Review.\n\nAlphaFold взял Нобель по химии 2024. Первая в истории Нобелевская премия за конкретный AI-продукт в фундаментальной науке. 200 миллионов структур в AlphaFold DB — в тысячу раз больше PDB за полвека. GNoME предсказала 380 тысяч стабильных материалов. Aurora в 5 тысяч раз быстрее эталона ECMWF на бенчмарке. AlphaProof серебро на Международной математической олимпиаде 2024. A-Lab — 41 из 58 кандидатов синтезированы за 17 дней.\n\nЭто прорывы. И они требуют человека в петле. Без человека в петле, который останавливает конвейер на каждой пробе — Палгрейв-Шуп показывает: 35 из 36 содержит ошибки. Прорыв и провал — две стороны одной медали.\n\nОткрыто для ваших вопросов.")


def s39_closing_hero(p):
    """s39 — closing hero: AlphaFold DB + bridge to Лекции 16."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)

    # Hero image full bleed
    img = IMG / "s39-alphafold-db.png"
    add_image(slide, img, 0.0, 0.0, 13.333, 5.0)

    # Overlay caption block bottom-middle
    rectangle(slide, 0.0, 4.6, 13.333, 0.4, fill=DEEP)
    text_box(slide, 0.0, 4.6, 13.333, 0.4,
             "AlphaFold DB · 200 миллионов структур · alphafold.ebi.ac.uk",
             size=14, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    # Bridge text + central question
    rounded_box(slide, 0.5, 5.2, 12.33, 1.5, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.5)
    multiline_box(slide, 0.8, 5.35, 11.8, 1.3, [
        ("Биология теперь чуть больше известна. Финальная карта далека.",
            {"size": 18, "bold": True, "color": DEEP}),
        ("", {"size": 4}),
        ("AlphaFold показал: закрытые задачи доступны AI. Лекция 16 — нефтегаз: частично закрытый (геофизика) + частично открытый (резервуар).",
            {"size": 14, "color": MID, "italic": True}),
    ], line_spacing=1.2)

    attribution(slide,
        "© DeepMind / Isomorphic Labs / EBI 2024 · alphafold.ebi.ac.uk · Wikimedia CC-BY-SA",
        y=6.95)

    add_notes(slide, "Закрывающий слайд. Hero — AlphaFold DB.\n\nAlphaFold показал миру самый важный позитивный кейс в этой лекции. Двести миллионов структур белков, каждая последовательность из UniProt, доступна на alphafold.ebi.ac.uk. Это самая большая структурная база данных в истории биологии. И это первый в истории AI-продукт в формулировке Нобелевской премии по фундаментальной науке.\n\nИ всё же — это только начало. Биология теперь чуть больше известна. Финальная карта далека. Мы знаем структуры всех известных белков, но мы не знаем большинства белок-белковых взаимодействий, не знаем большинства белок-маленькая молекула взаимодействий, не понимаем большинства функций. AlphaFold открыл новый слой, который теперь нужно заполнять.\n\nЭто и есть main pattern AI в науке. Прорыв там, где есть эталонная разметка и закрытый мир. И долгий путь следующих десятилетий заполнения новых классов задач.\n\nМост к лекции 16. Лекция 16 будет про AI в нефтегазе. Это частично закрытый мир — геофизика, сейсмическая интерпретация, есть физические уравнения и эталонные данные. И одновременно частично открытый — резервуар, добыча, сложные нелинейные системы, требующие операторских решений. Этот микс закрытого и открытого делает лекцию 16 принципиально другой, чем лекция 15.\n\nГлавная мысль лекции 15, которую вы должны унести: AI в науке требует суждения. Не «AI решит всё», не «AI ничего не решит» — а «AI решает разное на разных ступенях лестницы». Лестница циклическая. Ваша задача как инженера — диагностировать, на какой ступени вы стоите, и выбирать инструмент осознанно.\n\nСпасибо. Открыто для финальных вопросов.")
