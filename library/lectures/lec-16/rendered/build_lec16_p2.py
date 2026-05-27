"""
Part 2 of Lec-16 build — sections 4-7 (s28-s42).
Imports helpers from build_lec16.py.
"""
from build_lec16 import *


# ====================================================================
# SECTION 4: Q4 energy transition (s28-s33)
# ====================================================================

def s28_q4_divider(p):
    return section_divider(
        p, "Q4", "Энергопереход: CCS + EGS",
        "Здесь AI и физика буксуют вместе. Длинный горизонт, мало данных, низкая определённость физики. Самый честный квадрант.",
        "2 рабочих пилота · 2 структурных провала · 190× разрыв масштабирования",
        section_idx=4, large_size=200, label_color=GOLD)


def s29_northern_lights(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Northern Lights CCS — 0,02% от необходимого масштаба",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "СП Equinor + Shell + TotalEnergies. Коммерческий запуск 2024. Эугарден, Норвегия.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    img = ASSETS / "screenshots" / "s29-nl.jpg"
    add_image_aspect(slide, img, 0.65, 2.0, 5.7, 4.0)
    attribution(slide, "Wikimedia Commons / Zypres · CC-BY-SA 4.0", x=0.65, y=6.05, w=5.7)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("Метрики Northern Lights:", {"size": 14, "bold": True, "color": MID}),
        ("· Мощность фазы 1: 1,5 млн т CO₂/год", {"size": 12, "color": DEEP}),
        ("· В эксплуатации с 2024", {"size": 12, "color": DEEP}),
        ("· Источники CO₂: Microsoft, Heidelberg Materials, Yara", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Сравнение с масштабом:", {"size": 14, "bold": True, "color": MID}),
        ("1,5 млн т/год", {"size": 24, "bold": True, "color": LIGHT}),
        ("vs", {"size": 14, "color": SLATE}),
        ("7 600 млн т/год (цель IEA на 2050)", {"size": 24, "bold": True, "color": GOLD}),
        ("", {"size": 4}),
        ("= 0,02% от необходимого масштаба", {"size": 14, "bold": True, "color": RED_WARN}),
        ("= 190× разрыв масштабирования к 2050", {"size": 12, "color": DEEP, "italic": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "AI снижает удельную стоимость (моделирование пласта, выявление утечек). AI НЕ масштабирует индустрию — нужно 5000+ Northern Lights к 2050.",
                 size=12)
    add_notes(slide, "См. slides/s29-northern-lights-ccs.md speaker notes.")


def s30_fervo_egs(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Fervo Energy EGS — IPO 12 мая 2026, потолок роста в 40 раз",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Единственная возобновляемая базовая мощность, доступная при сегодняшних технологиях. Драйвер: AI-нагрузки требуют стабильное питание 24/7.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    img = ASSETS / "screenshots" / "s30-fervo2.jpg"
    add_image_aspect(slide, img, 0.65, 2.0, 5.7, 3.5)
    attribution(slide, "Fervo Energy / Cape Station Utah · 2026", x=0.65, y=5.55, w=5.7)
    img2 = ASSETS / "charts" / "s30-fervo-gap.png"
    add_image_aspect(slide, img2, 0.65, 5.85, 5.7, 0.45)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("IPO 12 мая 2026:", {"size": 14, "bold": True, "color": MID}),
        ("$1,89 млрд", {"size": 28, "bold": True, "color": GOLD}),
        ("привлечено в IPO; оценка $7,7 млрд", {"size": 12, "italic": True, "color": DEEP}),
        ("", {"size": 6}),
        ("Cape Station Юта ($206 млн):", {"size": 13, "bold": True, "color": MID}),
        ("· Пилот 2024 → коммерческий 2026", {"size": 12, "color": DEEP}),
        ("· Распределённое измерение температуры", {"size": 12, "color": DEEP}),
        ("· ГРП → замкнутый цикл", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Драйвер:", {"size": 13, "bold": True, "color": MID}),
        ("· Google, Microsoft, Meta — покупатели PPA", {"size": 12, "color": DEEP}),
        ("· AI ЦОДы → 24/7 чистая базовая мощность", {"size": 12, "color": DEEP}),
        ("· Потенциал EGS в США 150 ГВт vs текущие 3,7 ГВт", {"size": 12, "color": GOLD, "bold": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Замкнутый цикл: AI-гиганты спонсируют EGS чтобы запитать AI ЦОДы. Самореферентное расширение AI-инфраструктуры.",
                 size=12)
    add_notes(slide, "См. slides/s30-fervo-egs.md speaker notes.")


def s31_ccs_scale_gap(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "CCS — 190× разрыв масштабирования: инженерия vs политика",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "AI снижает удельную стоимость. AI не масштабирует индустрию. На 100-летнем горизонте AI легко галлюцинирует.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    img = ASSETS / "charts" / "s29-ccs-gap.png"
    add_image_aspect(slide, img, 0.7, 2.0, 5.6, 4.2)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("Где AI галлюцинирует на 100-летнем горизонте:", {"size": 13, "bold": True, "color": MID}),
        ("· Миграция шлейфа CO₂ через 50-100 лет", {"size": 11, "color": DEEP}),
        ("· Многофазный поток в неизвестных формациях", {"size": 11, "color": DEEP}),
        ("· Целостность покрышки — сценарии вне обучения", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("Прогноз Gartner на 2027:", {"size": 13, "bold": True, "color": MID}),
        ("40%", {"size": 28, "bold": True, "color": GOLD}),
        ("агентских AI-проектов будут отменены к 2027", {"size": 12, "italic": True, "color": DEEP}),
        ("", {"size": 4}),
        ("Sleipner Норвегия, 1996:", {"size": 13, "bold": True, "color": MID}),
        ("· Старейший CCS, $1 млрд+ инвестиций", {"size": 11, "color": DEEP}),
        ("· 30 лет данных — эмпирическая база", {"size": 11, "color": DEEP}),
        ("· AI как дополнение — да; AI-прогноз на 100 лет — нет.", {"size": 11, "color": DEEP, "bold": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Обратная атмосферная задача на 100-летнем горизонте = AI легко галлюцинирует. PINN (нейросети с встроенной физикой) — исследовательский уровень, не коммерческий.",
                 size=12)
    add_notes(slide, "См. slides/s31-ccs-scale-gap-hallucination.md speaker notes.")


def s32_refinery_q4(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Общезаводская стагнация НПЗ = структурная проблема Q4",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Многослойная физика (масса + энергия + реакция + коррозия) ломает ML-суррогаты на нестандартных режимах.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 5.5, 4.45)
    img = ASSETS / "screenshots" / "s33-honeywell.jpg"
    add_image_aspect(slide, img, 0.65, 2.0, 5.2, 4.1)
    attribution(slide, "Honeywell Process Solutions · 2025", x=0.65, y=6.10, w=5.2)
    rounded_box(slide, 6.2, 1.85, 6.63, 4.45)
    multiline_box(slide, 6.4, 1.95, 6.3, 4.3, [
        ("Кейс Yokogawa Idemitsu:", {"size": 14, "bold": True, "color": MID}),
        ("· 2018+: пилот на одной колонне дистилляции — успех", {"size": 12, "color": DEEP}),
        ("· Общезаводской пилот → тихо закрыт", {"size": 12, "color": RED_WARN}),
        ("", {"size": 6}),
        ("Многоюнитная координация:", {"size": 14, "bold": True, "color": MID}),
        ("· 100+ установок в типичном НПЗ", {"size": 12, "color": DEEP}),
        ("· Масса + энергия + реакция + коррозия = 4 физики", {"size": 12, "color": DEEP}),
        ("· ML-суррогат ломается при смене сырья, сезонных колебаниях", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Срок жизни vs деградация ML:", {"size": 14, "bold": True, "color": MID}),
        ("40-50 лет жизни месторождения", {"size": 16, "bold": True, "color": LIGHT}),
        ("vs 1-2 года деградации ML-модели", {"size": 16, "bold": True, "color": GOLD}),
        ("Стоимость переобучения > выгода на нестандартных режимах.", {"size": 11, "color": DEEP, "italic": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Это не провал Q1 — это структурный Q4. Многослойная физика + длинный горизонт + частое переобучение = ML-суррогат не выживает.",
                 size=12)
    add_notes(slide, "См. slides/s32-refinery-q4-stagnation.md speaker notes.")


def s33_q4_alternatives_sis(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Альтернатива Q4: классическая инженерия + детерминированная безопасность",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "3 категории. Для регуляторных отчётов — физически прослеживаемое обязательно. AI не принимается.",
             size=13, italic=True, color=LIGHT)
    alts = [
        ("Физика для CCS / геомеханики", "Eclipse / INTERSECT / CMG GEM /\nVisage / Abaqus / Plaxis.\nМиграция шлейфа 100 лет — физическое моделирование обязательно.", MID),
        ("Классический APC для НПЗ\n(Advanced Process Control)", "Honeywell Profit Controller /\nEmerson DeltaV / AspenTech aspenONE.\nMPC + RTO — проверены 30 лет, не AI.", LIGHT),
        ("SIS для критичной безопасности", "SIL3/SIL4 по IEC 61511.\nГолосование 3oo2 (три из двух) + периодические проверки.\nML НЕ сертифицируется.\nDeepwater Horizon 2010 — обход тревог как якорь.", GOLD),
    ]
    a_w = 4.05
    a_h = 4.5
    gap = 0.1
    x0 = 0.5
    y0 = 1.85
    for i, (name, body, accent) in enumerate(alts):
        x = x0 + i * (a_w + gap)
        rounded_box(slide, x, y0, a_w, a_h, stroke=accent, stroke_w=2)
        rectangle(slide, x, y0, a_w, 0.85, fill=accent)
        text_box(slide, x+0.15, y0, a_w-0.3, 0.85, name,
                 size=13, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x+0.2, y0+1.0, a_w-0.4, a_h - 1.15, body,
                 size=12, color=DEEP, line_spacing=1.4)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "SIL3 = 0,001–0,0001 PFD (вероятность отказа по требованию). ML-модель не проверяема воспроизводимо под IEC 61511. Инженерное правило.",
                 size=12)
    add_notes(slide, "См. slides/s33-q4-alternatives-sis.md speaker notes.")


# ====================================================================
# SECTION 5: Россия (s34-s36)
# ====================================================================

def s34_russia_divider(p):
    """s34 — Russia section divider with mini-matrix."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    roadmap_bar(slide, current_section=5)
    text_box(slide, 0.5, 0.7, 12.33, 0.85,
             "Россия — санкции, внутренняя разработка, вертикальная интеграция",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.5, 12.33, 0.4,
             "По 4 квадрантам матрицы. После марта 2022 — структурный сдвиг.",
             size=13, italic=True, color=LIGHT)
    # Mini-matrix Russia x Quadrants
    quads = [
        ("Q1 Зрелое", "Роснефть Digital Field\nна Башнефть Илишевское\n+1 млн т/год нефти", MID),
        ("Q3 Разведка", "Газпром нефть Cognitive Geo\nс IBM Research Brazil 2019–2022\n→ внутренняя разработка после ухода IBM", LIGHT),
        ("Q2 Метан", "EU 2024/1787 не применяется\nк компаниям РФ через импорт\nсоответствие с 2027", TEAL),
        ("Q4 Переход", "CCS / EGS — ограниченные\nпилоты. Санкции блокируют\nзамкнутую AI-инфраструктуру", GOLD),
    ]
    q_w = 6.0
    q_h = 2.0
    gap = 0.2
    x0 = 0.5
    y0 = 2.0
    for i, (name, body, accent) in enumerate(quads):
        col = i % 2
        row = i // 2
        x = x0 + col * (q_w + gap)
        y = y0 + row * (q_h + gap)
        rounded_box(slide, x, y, q_w, q_h, stroke=accent, stroke_w=2)
        rectangle(slide, x, y, 0.15, q_h, fill=accent)
        text_box(slide, x + 0.3, y + 0.1, q_w - 0.4, 0.5, name,
                 size=14, bold=True, color=DEEP)
        text_box(slide, x + 0.3, y + 0.6, q_w - 0.4, q_h - 0.7, body,
                 size=11, color=DEEP, line_spacing=1.35)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Вертикальная интеграция — необходимость, не выбор. Российский путь ближе к Sinopec / CNOOC, чем к Aramco / ExxonMobil на основе поставщиков.",
                 size=12)
    add_notes(slide, "См. slides/s34-russia-divider.md speaker notes.")


def s35_gazprom_cognitive_geo(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Газпром нефть Cognitive Geologist — ключевой российский кейс Q3",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "С IBM Research Brazil 2019–2022 → внутренняя разработка после ухода IBM. Выжил там, где BP+Beyond Limits + IBM+Repsol провалились.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    multiline_box(slide, 0.7, 1.95, 5.7, 4.3, [
        ("Метрики Cognitive Geo:", {"size": 14, "bold": True, "color": MID}),
        ("", {"size": 6}),
        ("Геологический цикл:", {"size": 13, "bold": True, "color": DEEP}),
        ("3-4 месяца → минуты", {"size": 22, "bold": True, "color": GOLD}),
        ("", {"size": 6}),
        ("Ямал 2024:", {"size": 13, "bold": True, "color": DEEP}),
        ("· Первая нефть нового поля", {"size": 12, "color": DEEP}),
        ("· Сокращение вдвое времени до первой нефти", {"size": 12, "color": DEEP}),
        ("· +40% проектов к 2030 (цель)", {"size": 12, "color": DEEP, "bold": True}),
        ("", {"size": 6}),
        ("Структурный успех:", {"size": 13, "bold": True, "color": MID}),
        ("Узкая задача (предварительная сейсмика) + измеримая база (месяцы → минуты) + контроль старшего эксперта.", {"size": 11, "color": DEEP, "italic": True}),
    ], line_spacing=1.25)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("Партнёрство AIQ:", {"size": 14, "bold": True, "color": MID}),
        ("· Совместное предприятие ADNOC + G42 + Presight", {"size": 12, "color": DEEP}),
        ("· AIQ оценка ~$1,4 млрд+ (2025)", {"size": 12, "color": DEEP, "bold": True}),
        ("· Aramco + Groq — родственная AI-сделка", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Контраст с провалами:", {"size": 13, "bold": True, "color": MID}),
        ("· BP + Beyond Limits — один поставщик + когнитивное переобещание", {"size": 11, "color": DEEP}),
        ("· IBM + Repsol — универсальный в узкой области", {"size": 11, "color": DEEP}),
        ("· Cognitive Geo — узкая задача + кастом + контроль старшего = успех.", {"size": 11, "color": DEEP, "bold": True}),
        ("", {"size": 6}),
        ("Оговорка:", {"size": 13, "bold": True, "color": GOLD}),
        ("Российские KPI — самоотчёт. Та же оговорка что для Aramco.", {"size": 11, "color": DEEP, "italic": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Структурный паттерн успеха Q3: узкая задача + измеримая база + контроль старшего эксперта. Антропоморфная рамка («AI имитирует геолога») = красный флаг.",
                 size=12)
    add_notes(slide, "См. slides/s35-gazprom-cognitive-geo.md speaker notes.")


def s36_rosneft_detail(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Российский Q1: ключевой кейс + средний эшелон",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Структурный разрыв в раскрытии — корпоративные пресс-релизы вместо обязательной отчётности SEC 10-K.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    rectangle(slide, 0.5, 1.85, 6.0, 0.55, fill=MID)
    text_box(slide, 0.65, 1.85, 5.7, 0.55, "Роснефть Digital Field детально",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 0.7, 2.55, 5.6, 3.75, [
        ("Башнефть Илишевское — ключевой кейс:", {"size": 13, "bold": True, "color": MID}),
        ("· 23 продукта (10 коммерциализованных)", {"size": 12, "color": DEEP}),
        ("· +1 млн т/год дополнительной нефти", {"size": 12, "color": DEEP, "bold": True}),
        ("· ~1 млрд ₽/год эффект", {"size": 12, "color": DEEP}),
        ("· +60% удалённо управляемых объектов", {"size": 12, "color": DEEP}),
        ("· +5% энергоэффективности", {"size": 12, "color": DEEP}),
        ("· −5% логистики", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Структурный путь:", {"size": 13, "bold": True, "color": MID}),
        ("· Roxar (Schlumberger) ушёл в 2022", {"size": 11, "color": DEEP}),
        ("· Внутренняя разработка — единственный путь", {"size": 11, "color": DEEP}),
    ], line_spacing=1.25)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    rectangle(slide, 6.7, 1.85, 6.13, 0.55, fill=LIGHT)
    text_box(slide, 6.85, 1.85, 5.83, 0.55, "Татнефть · ЛУКОЙЛ · Сургутнефтегаз",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    multiline_box(slide, 6.9, 2.55, 5.83, 3.75, [
        ("Татнефть:", {"size": 13, "bold": True, "color": MID}),
        ("· Программа «АнтиХрупкий» (управление устойчивостью)", {"size": 11, "color": DEEP}),
        ("· Нижнекамск НПЗ — частичное внедрение AI", {"size": 11, "color": DEEP}),
        ("· Публичное раскрытие ограничено", {"size": 11, "color": DEEP, "italic": True}),
        ("", {"size": 6}),
        ("ЛУКОЙЛ:", {"size": 13, "bold": True, "color": MID}),
        ("· Волго-Урал — внутренние команды без поставщика", {"size": 11, "color": DEEP}),
        ("· Подробных KPI публично нет", {"size": 11, "color": DEEP, "italic": True}),
        ("", {"size": 6}),
        ("Сургутнефтегаз:", {"size": 13, "bold": True, "color": MID}),
        ("· Cognitive Pilot + экосистема Sberbank", {"size": 11, "color": DEEP}),
        ("· Консервативное раскрытие", {"size": 11, "color": DEEP, "italic": True}),
        ("", {"size": 6}),
        ("Структурный разрыв:", {"size": 13, "bold": True, "color": GOLD}),
        ("Без обязательной отчётности по образцу SEC — оценка только качественная.", {"size": 11, "color": DEEP}),
    ], line_spacing=1.2)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Российский паттерн работающего Q1: нацкомпания + внутренние команды + узкая задача + измеримая база. Зависимость от поставщика = риск (Roxar ушёл 2022).",
                 size=12)
    add_notes(slide, "См. slides/s36-rosneft-detail-other-noc.md speaker notes.")


# ====================================================================
# SECTION 6: Cross-cutting (s37-s38)
# ====================================================================

def s37_cyber_935(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Шифровальщики против нефтегаза +935% год к году (апр 2024 → апр 2025)",
             size=22, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Отчёт Zscaler ThreatLabz 2025. Встречный тренд AI-расширения — безопасность фаза 1, не фаза 4.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    img = ASSETS / "charts" / "s37-cyber-935.png"
    add_image_aspect(slide, img, 0.7, 2.0, 5.6, 4.2)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    multiline_box(slide, 6.9, 1.95, 5.83, 4.3, [
        ("Якорь Colonial Pipeline 2021:", {"size": 14, "bold": True, "color": MID}),
        ("· VPN-аккаунт без MFA (многофакторной аутентификации) — единая точка входа", {"size": 12, "color": DEEP}),
        ("· Шифровальщик DarkSide → 6 дней остановки", {"size": 12, "color": DEEP}),
        ("· 50% поставок топлива на Восточном побережье", {"size": 12, "color": DEEP}),
        ("· $4,4 млн выкупа уплачено (часть возвращена)", {"size": 12, "color": DEEP, "bold": True}),
        ("", {"size": 6}),
        ("Защитные AI-альтернативы:", {"size": 13, "bold": True, "color": MID}),
        ("· Платформа OT-безопасности Dragos", {"size": 11, "color": DEEP}),
        ("· Claroty + Nozomi Networks — мониторинг SCADA", {"size": 11, "color": DEEP}),
        ("· Cisco SecureX, CrowdStrike Falcon", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("Встречный вывод:", {"size": 13, "bold": True, "color": GOLD}),
        ("AI расширяет поверхность атаки. Защитный AI (выявление аномалий) — необходим, но недостаточен.", {"size": 11, "color": DEEP, "italic": True}),
    ], line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Безопасность — фаза 1 (периметр + MFA + сегментация), НЕ фаза 4 (наложение AI-защиты). Сначала базовое, потом AI.",
                 size=12)
    add_notes(slide, "См. slides/s37-cyber-935-percent.md speaker notes.")


def s38_2020_crash_deepwater(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Цикл отрасли > цикл AI-хайпа. Deepwater Horizon = якорь.",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Кризис 2020 — 107 тыс. рабочих мест за 6 мес + Deepwater Horizon 2010 — два сквозных якоря.",
             size=13, italic=True, color=LIGHT)
    rounded_box(slide, 0.5, 1.85, 6.0, 4.5)
    rectangle(slide, 0.5, 1.85, 6.0, 0.55, fill=LIGHT)
    text_box(slide, 0.65, 1.85, 5.7, 0.55, "Нефтяной кризис 2020",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    img = ASSETS / "charts" / "s38-2020-crash.png"
    add_image_aspect(slide, img, 0.65, 2.5, 5.7, 2.2)
    multiline_box(slide, 0.65, 4.75, 5.7, 1.5, [
        ("107 000 рабочих мест потеряно за 6 мес = 9,7% индустрии", {"size": 12, "bold": True, "color": GOLD}),
        ("· Фьючерсы WTI: −$37 (отрицательные) на короткое время", {"size": 11, "color": DEEP}),
        ("· AI-программы заморожены на 18-24 мес", {"size": 11, "color": DEEP}),
        ("· Рынок труда не восстановился полностью к 2024", {"size": 11, "color": DEEP}),
    ], line_spacing=1.3)
    rounded_box(slide, 6.7, 1.85, 6.13, 4.5)
    rectangle(slide, 6.7, 1.85, 6.13, 0.55, fill=RED_WARN)
    text_box(slide, 6.85, 1.85, 5.83, 0.55, "Deepwater Horizon 2010",
             size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    img2 = ASSETS / "screenshots" / "wm-deepwater-horizon-oil-spill.jpg"
    add_image_aspect(slide, img2, 6.85, 2.5, 5.83, 2.2)
    multiline_box(slide, 6.85, 4.75, 5.83, 1.5, [
        ("11 погибших + $60 млрд = 20% годовой выручки BP", {"size": 12, "bold": True, "color": GOLD}),
        ("· Выброс на скважине Macondo — Мексиканский залив", {"size": 11, "color": DEEP}),
        ("· Отказ BOP (противовыбросового превентора)", {"size": 11, "color": DEEP}),
        ("· Культура обхода тревог (показания Andrea Fleytas)", {"size": 11, "color": DEEP, "bold": True}),
    ], line_spacing=1.3)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Дорожная карта AI должна тестироваться на устойчивость к циклу отрасли и культуре обхода тревог (усталость от ложных тревог → обход тревог — тот же паттерн на 2 разных шкалах).",
                 size=12)
    add_notes(slide, "См. slides/s38-2020-crash-deepwater.md speaker notes.")


# ====================================================================
# SECTION 7: Closing (s39-s42)
# ====================================================================

def s39_synthesis_matrix(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "4-квадрантный синтез: 10 разобранных провалов + работающие кейсы",
             size=24, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Возврат к матрице. AI в нефтегазе — не одна история, а четыре.",
             size=13, italic=True, color=LIGHT)
    # 4 quadrants with works + fails
    quads = [
        ("Q2 Метан — AI необходим", "Работает:\n· MethaneSAT (15,5 мес до потери)\n· Carbon Mapper Tanager-1\n· GHGSat — группировка 13 спутников\n· Bridger авиа-LiDAR\n\nПровалы (2):\n· Потеря MethaneSAT 20 июня 2025\n· 4× разрыв с EPA", TEAL),
        ("Q1 Зрелое — AI как мультипликатор", "Работает:\n· Ambyint +15% / 200 скважин\n· Honeywell UOP 310+ установок\n· Роснефть Digital Field +1 млн т/год\n\nПровалы (2):\n· 86% пилотов застряло\n· Aspen Mtell — усталость от тревог", MID),
        ("Q4 Переход — буксуют вместе", "Работает (ограниченно):\n· Northern Lights 1,5 млн т/год\n· Fervo IPO $1,89 млрд\n\nПровалы (2):\n· CCS 190× разрыв масштабирования\n· Общезаводская стагнация НПЗ", GOLD),
        ("Q3 Разведка — сначала физика", "Работает:\n· Eni HPC6 / Aramco METABRAIN\n· SLB Lumi / ExxonMobil Discovery 6\n· Газпром Cognitive Geo\n\nПровалы (2):\n· BP+Beyond Limits — 7 лет 0\n· IBM+Repsol Kalimba", LIGHT),
    ]
    q_w = 6.0
    q_h = 2.2
    gap_x = 0.2
    gap_y = 0.15
    x0 = 0.5
    y0 = 1.85
    for i, (name, body, accent) in enumerate(quads):
        col = i % 2
        row = i // 2
        x = x0 + col * (q_w + gap_x)
        y = y0 + row * (q_h + gap_y)
        rounded_box(slide, x, y, q_w, q_h, stroke=accent, stroke_w=2.5)
        rectangle(slide, x, y, q_w, 0.4, fill=accent)
        text_box(slide, x+0.15, y, q_w-0.3, 0.4, name,
                 size=12, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x+0.2, y+0.5, q_w-0.4, q_h-0.6, body,
                 size=9, color=DEEP, line_spacing=1.25)
    gold_callout(slide, 0.5, 6.5, 12.33, 0.55,
                 "Когда работает: Q1 мультипликатор + Q2 необходим. Когда осторожно: Q3 как дополнение. Когда опасно: Q4 длинный горизонт + критичная безопасность (SIS).",
                 size=12)
    add_notes(slide, "См. slides/s39-synthesis-matrix.md speaker notes.")


def s40_three_cornerstones(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "3 опорных концепта — мост к Лекции 17",
             size=26, bold=True, color=DEEP, line_spacing=1.1)
    text_box(slide, 0.5, 1.3, 12.33, 0.4,
             "Каждый переносим на любую следующую отрасль, не только нефтегаз.",
             size=13, italic=True, color=LIGHT)
    corners = [
        ("1", "AI-суждение как структурная задача", "Главный навык — не «как запустить AI», а «как определить, применим ли». Для нефтегаза: матрица 2×2 данные × физика. Для любой отрасли: 2-3-мерная таксономия. Без диагностики AI = азартная ставка.", MID),
        ("2", "Альтернатива как исходный уровень", "Каждое AI-внедрение имеет параллельный не-AI вариант. Для нефтегаза 6 категорий: Eclipse, Picarro, OGI, классический APC, SIS, федеративное обучение. AI добавляется ТОЛЬКО если улучшает базовый уровень.", TEAL),
        ("3", "Цикл отрасли > цикл AI-хайпа", "Нефтяной кризис 2020: 107 тыс. рабочих мест за 6 мес → AI заморожены 18-24 мес. Дорожная карта AI должна быть устойчивой к отраслевому циклу. AI не защищает — он усиливает эффект.", GOLD),
    ]
    c_w = 12.33
    c_h = 1.55
    gap = 0.1
    x0 = 0.5
    y0 = 1.85
    for i, (num, title, body, accent) in enumerate(corners):
        y = y0 + i * (c_h + gap)
        rounded_box(slide, x0, y, c_w, c_h, stroke=accent, stroke_w=2)
        circle(slide, x0 + 0.15, y + 0.3, 0.9, 0.9, fill=accent)
        text_box(slide, x0 + 0.15, y + 0.3, 0.9, 0.9, num,
                 size=32, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x0 + 1.3, y + 0.15, c_w - 1.5, 0.5, title,
                 size=16, bold=True, color=DEEP)
        text_box(slide, x0 + 1.3, y + 0.7, c_w - 1.5, c_h - 0.85, body,
                 size=12, color=DEEP, line_spacing=1.35)
    gold_callout(slide, 0.5, 6.7, 12.33, 0.55,
                 "Эти три опорных концепта — переносимые диагностические инструменты. Лекция 17 — систематизация: несущие оси L11-L16 как универсальные шаблоны.",
                 size=12)
    add_notes(slide, "См. slides/s40-three-cornerstones.md speaker notes.")


def s41_qa(p):
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.85,
             "Q&A",
             size=44, bold=True, color=DEEP, line_spacing=1.05)
    text_box(slide, 0.5, 1.4, 12.33, 0.4,
             "3 ключевых вопроса для выходного билета — обсуждаем в малых группах, потом общий слайд.",
             size=14, italic=True, color=LIGHT)
    questions = [
        ("Q1", "Для какого квадранта матрицы данные × физика AI является НЕОБХОДИМЫМ (а не дополнением)? Конкретный кейс + почему классической физики недостаточно?", TEAL),
        ("Q2", "Приведите 2 разобранных провала из лекции + выученные уроки. (Любые 2 из 10: BP+Beyond Limits, IBM+Repsol, потеря MethaneSAT, 86% застряло, Aspen — усталость от тревог, 4× разрыв, CCS 190×, стагнация НПЗ, кризис 2020, кибер +935%.)", LIGHT),
        ("Q3", "Когда в нефтегазе НЕ применять AI — назовите 3 критерия с примерами из 6 на лекции.", GOLD),
    ]
    q_w = 12.33
    q_h = 1.4
    gap = 0.15
    x0 = 0.5
    y0 = 2.0
    for i, (qn, body, accent) in enumerate(questions):
        y = y0 + i * (q_h + gap)
        rounded_box(slide, x0, y, q_w, q_h, stroke=accent, stroke_w=2)
        rectangle(slide, x0, y, 1.3, q_h, fill=accent)
        text_box(slide, x0, y + 0.4, 1.3, 0.6, qn,
                 size=28, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x0 + 1.5, y + 0.15, q_w - 1.7, q_h - 0.3, body,
                 size=12, color=DEEP, line_spacing=1.35, anchor=MSO_ANCHOR.MIDDLE)
    gold_callout(slide, 0.5, 6.75, 12.33, 0.5,
                 "Дополнительно для семинара: сравните Eni HPC6 ($104 млн, AMD, Италия) vs ExxonMobil Discovery 6 ($200-400 млн, NVIDIA, США) vs Aramco METABRAIN (250 млрд параметров, внутренний Саудовский).",
                 size=12)
    add_notes(slide, "См. slides/s41-qa.md speaker notes.")


def s42_hero_methanesat_map(p):
    """s42 — closing hero: MethaneSAT global methane map."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    # Hero image LEFT (60% width × 5.5" = ~44% area)
    img = ASSETS / "screenshots" / "s42-methanesat.png"
    add_image_aspect(slide, img, 0.5, 0.4, 7.8, 5.4)
    attribution(slide, "EDF / MethaneSAT data via Google Earth Engine · февраль 2026",
                x=0.5, y=5.85, w=7.8)
    # Title + text RIGHT
    multiline_box(slide, 8.4, 0.5, 4.6, 5.5, [
        ("Спутник потерян —", {"size": 22, "bold": True, "color": DEEP}),
        ("карта осталась.", {"size": 26, "bold": True, "color": GOLD}),
        ("", {"size": 12}),
        ("Горько-сладкая развязка:", {"size": 13, "bold": True, "color": MID}),
        ("· 20 июня 2025 — потеря MethaneSAT", {"size": 11, "color": DEEP}),
        ("· ~2 000 файлов данных за 15,5 мес → ретроспективный реестр", {"size": 11, "color": DEEP, "italic": True}),
        ("", {"size": 8}),
        ("Финальная рамка:", {"size": 13, "bold": True, "color": MID}),
        ("AI в нефтегазе — это", {"size": 12, "color": DEEP}),
        ("измеримый успех", {"size": 13, "bold": True, "color": DEEP}),
        ("+ структурная уязвимость", {"size": 13, "bold": True, "color": GOLD}),
        ("в одном кадре.", {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Хороший инженер строит честный портфельный обзор, не одиночный квадрант.", {"size": 10, "color": DEEP, "italic": True}),
    ], line_spacing=1.2)
    gold_callout(slide, 0.5, 6.4, 12.33, 0.7,
                 "Мост к Лекции 17 — систематизация. Несущие оси L11–L16 как универсальные шаблоны.",
                 size=14)
    add_notes(slide, "См. slides/s42-hero-methanesat-map.md speaker notes.")


# ====================================================================
# Build orchestration
# ====================================================================

def build_all():
    """Assemble full 43-slide deck."""
    p = setup_pres()
    # Section 0 (s01-s05): 5 slides
    s01_hero_permian(p)
    s02_cover(p)
    s03_about(p)
    s04_lecture_map(p)
    s05_keystone_matrix(p)
    # Section 1 (s06-s12): 7 slides incl s07b → 8
    s06_q1_divider(p)
    s07_pilot_stuck(p)
    s07b_aspen_alert_fatigue(p)
    s08_ambyint(p)
    s09_vendor_landscape(p)
    s10_rosneft_digital_field(p)
    s11_cognite_c3ai(p)
    s12_q1_no_ai_criteria(p)
    # Section 2 (s13-s19): 7 slides
    s13_q3_divider(p)
    s14_hpc_eni_aramco(p)
    s15_slb_lumi(p)
    s16_exxon_discovery6(p)
    s17_bp_beyond_limits(p)
    s18_ibm_repsol(p)
    s19_q3_alternatives(p)
    # Section 3 (s20-s27): 8 slides
    s20_methane_alphabet(p)
    s21_q2_divider(p)
    s22_methanesat_permian(p)
    s23_methanesat_loss(p)
    s24_post_methanesat_players(p)
    s25_4x_discrepancy(p)
    s26_eu_vs_epa(p)
    s27_q2_alternatives(p)
    # Section 4 (s28-s33): 6 slides
    s28_q4_divider(p)
    s29_northern_lights(p)
    s30_fervo_egs(p)
    s31_ccs_scale_gap(p)
    s32_refinery_q4(p)
    s33_q4_alternatives_sis(p)
    # Section 5 (s34-s36): 3 slides
    s34_russia_divider(p)
    s35_gazprom_cognitive_geo(p)
    s36_rosneft_detail(p)
    # Section 6 (s37-s38): 2 slides
    s37_cyber_935(p)
    s38_2020_crash_deepwater(p)
    # Section 7 (s39-s42): 4 slides
    s39_synthesis_matrix(p)
    s40_three_cornerstones(p)
    s41_qa(p)
    s42_hero_methanesat_map(p)

    p.save(str(OUT))
    print(f"Saved {OUT} with {len(p.slides)} slides")


if __name__ == "__main__":
    build_all()
