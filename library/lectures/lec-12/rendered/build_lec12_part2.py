"""Part 2 of lec-12 builder: s15-s39 (A1 + A2 + A3 + НЕ AI + OT/IT + РФ + closing)."""
from build_lec12 import (
    blank, set_bg, text_box, multiline, rounded_box, rectangle, circle,
    arrow_right, add_image, footer, attribution, add_notes, roadmap_bar,
    section_divider, ASSETS,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, DARK_GREY, ROADMAP,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN


# ====================================================================
# SECTION 3 — A1 (§3) — s15 div + s16-s18
# ====================================================================

def s15_div(p):
    section_divider(p, 3, 3, "A1 — Советовать",
                    "MES советующий · предсказание тревог · PLC Copilot vs ChatGPT провал",
                    "Раздел 3 · советующий режим с инженером в петле")


def s16_mes(p):
    """s16 — MES advisory + alarm prediction."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "MES советующий + предсказание тревог за 5–15 минут до каскада",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Зрелые применения A1: рекомендации по последовательности операций, планирование с учётом энергии, ML на журналах SCADA",
             size=13, italic=True, color=LIGHT)
    # Left chart
    chart = ASSETS / "charts" / "s16-alarm-prediction.png"
    if chart.exists():
        rounded_box(slide, 0.5, 1.75, 7.5, 5.0)
        add_image(slide, chart, 0.7, 1.9, 7.1, 4.7)
    # Right: explanation card
    rounded_box(slide, 8.2, 1.75, 4.6, 5.0, fill=SURFACE, stroke=MID, stroke_w=2.0)
    multiline(slide, 8.4, 1.9, 4.2, 4.8, [
        ("ЧТО ЕСТЬ НА A1:", {"size": 12, "bold": True, "color": MID}),
        ("", {"size": 8}),
        ("MES в советующем режиме:", {"size": 13, "bold": True, "color": DEEP}),
        ("· рекомендация последовательности операций",
         {"size": 11, "color": DEEP}),
        ("· планирование с учётом энергии", {"size": 11, "color": DEEP}),
        ("· оператор подтверждает", {"size": 11, "italic": True, "color": GOLD}),
        ("", {"size": 8}),
        ("Предсказание тревог:", {"size": 13, "bold": True, "color": DEEP}),
        ("· ML на исторических журналах SCADA",
         {"size": 11, "color": DEEP}),
        ("· окно 5–15 минут до каскада",
         {"size": 11, "color": DEEP}),
        ("· оператор успевает вмешаться",
         {"size": 11, "italic": True, "color": GOLD}),
        ("", {"size": 8}),
        ("Якорь A1:", {"size": 11, "bold": True, "color": MID}),
        ("AI предлагает действие, человек даёт явное согласие.",
         {"size": 11, "color": DEEP}),
    ], line_spacing=1.3)
    attribution(slide, "Devox / iFactoryApp 2026 · документация Siemens Opcenter + Rockwell FactoryTalk")


def s17_plc_copilot(p):
    """s17 — PLC Copilot vs ChatGPT — split screen."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "PLC Copilot vs ChatGPT: 85% точности vs остановка контроллера",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Специализированные инструменты работают; универсальная языковая модель на PLC — провал",
             size=13, italic=True, color=LIGHT)
    # Two columns
    col_y = 1.75
    col_h = 5.0
    col_w = 6.0
    # Left: PLC Copilot
    rounded_box(slide, 0.5, col_y, col_w, col_h, fill=SURFACE, stroke=MID, stroke_w=2.0)
    rectangle(slide, 0.5, col_y, col_w, 0.7, fill=MID)
    text_box(slide, 0.5, col_y + 0.08, col_w, 0.55,
             "PLC Copilot · специализированный",
             size=17, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    multiline(slide, 0.7, col_y + 0.9, col_w - 0.4, 4.0, [
        ("Что делает:", {"size": 12, "bold": True, "color": LIGHT}),
        ("Знает IEC 61131-3 (релейная логика, структурированный текст, FBD).",
         {"size": 12, "color": DEEP}),
        ("Понимает циклическое исполнение PLC.", {"size": 12, "color": DEEP}),
        ("Валидирует адреса памяти по модели контроллера.",
         {"size": 12, "color": DEEP}),
        ("", {"size": 8}),
        ("Скорость:", {"size": 12, "bold": True, "color": LIGHT}),
        ("3–4 дня → 10 минут", {"size": 18, "bold": True, "color": GOLD}),
        ("", {"size": 8}),
        ("Точность:", {"size": 12, "bold": True, "color": LIGHT}),
        ("85% — с инженером в петле", {"size": 16, "bold": True, "color": DEEP}),
        ("(15% ошибок ловит инженер)",
         {"size": 11, "italic": True, "color": SLATE}),
    ], line_spacing=1.3)
    # Right: ChatGPT failure
    rounded_box(slide, 6.83, col_y, col_w, col_h, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    rectangle(slide, 6.83, col_y, col_w, 0.7, fill=GOLD)
    text_box(slide, 6.83, col_y + 0.08, col_w, 0.55,
             "ChatGPT универсальный · ПРОВАЛ",
             size=17, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    multiline(slide, 7.03, col_y + 0.9, col_w - 0.4, 4.0, [
        ("Что выдаёт ChatGPT (промпт «оптимизируй»):", {"size": 11, "bold": True, "color": MID}),
        ("MOV %M99999", {"size": 22, "bold": True, "color": GOLD, "italic": True}),
        ("", {"size": 8}),
        ("Что не так:", {"size": 12, "bold": True, "color": LIGHT}),
        ("Область M в Siemens S7-1500 физически ограничена до M65535.",
         {"size": 12, "color": DEEP}),
        ("Код скомпилируется в TIA Portal без ошибок,",
         {"size": 12, "color": DEEP}),
        ("но в режиме исполнения PLC уходит в STOP-mode — остановка всего оборудования.",
         {"size": 12, "color": DEEP}),
        ("", {"size": 6}),
        ("Корневая причина:", {"size": 12, "bold": True, "color": LIGHT}),
        ("Универсальная языковая модель не знает циклическое исполнение и допустимые адреса конкретной модели.",
         {"size": 12, "color": DEEP}),
        ("", {"size": 4}),
        ("Это структурное ограничение, не «временный сбой».",
         {"size": 11, "italic": True, "color": GOLD}),
    ], line_spacing=1.3)
    add_notes(slide, "Конкретный пример провала универсальной языковой модели на PLC. ChatGPT на запрос «оптимизируй этот блок Siemens S7-1500» выдаёт инструкцию MOV %M99999. Что не так: в Siemens S7-1500 область M (флаги памяти) ограничена до M65535. Адрес %M99999 синтаксически валиден — код скомпилируется в TIA Portal без ошибок синтаксического анализатора. Но при загрузке в PLC и попытке исполнения контроллер обнаружит обращение за пределы адресного пространства M и уйдёт в режим STOP — то есть остановит всё оборудование, управляемое этим PLC. Это не «иногда галлюцинирует», это структурное ограничение. Универсальная языковая модель не знает циклическое исполнение PLC, не знает допустимые адреса конкретной модели контроллера. Альтернатива — специализированные инструменты: PLC Copilot, PLCAutoPilot, Wipro PARI. Они знают IEC 61131-3, валидируют адреса по модели контроллера до выдачи кода, понимают время цикла. С инженером в петле дают 85% точности. 15% ошибок ловит инженер. Это правильный паттерн A1 — AI предлагает, инженер ревьюит.")


def s18_engineer_in_loop(p):
    """s18 — Engineer-in-loop architecture diagram. Russified sub-labels."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Архитектура «инженер в петле»: безопасный паттерн A1",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "AI предлагает → инженер проверяет → симуляция → проверка безопасности → загрузка в PLC",
             size=13, italic=True, color=LIGHT)
    # 5 stage pipeline
    stages = [
        ("AI", "предлагает\nрекомендацию", MID),
        ("Инженер", "проверяет\nи корректирует", LIGHT),
        ("Симулятор", "валидирует\nна двойнике", TEAL),
        ("Безопасность", "IEC 61131-3\n+ тестовые сценарии", GOLD),
        ("Загрузка в PLC", "только если\nвсе шаги пройдены", DEEP),
    ]
    n = len(stages)
    box_w = 1.95
    arrow_w = 0.4
    total = n * box_w + (n - 1) * arrow_w
    x0 = (13.333 - total) / 2
    y = 2.5
    h = 2.0
    for i, (title, sub, color) in enumerate(stages):
        x = x0 + i * (box_w + arrow_w)
        rounded_box(slide, x, y, box_w, h, fill=SURFACE, stroke=color, stroke_w=2.0)
        rectangle(slide, x, y, box_w, 0.6, fill=color)
        text_box(slide, x + 0.05, y + 0.05, box_w - 0.1, 0.5, title,
                 size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, x + 0.1, y + 0.75, box_w - 0.2, 1.1, sub,
                 size=12, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.3)
        if i < n - 1:
            ax = x + box_w + 0.02
            arrow_right(slide, ax, y + h/2 - 0.18, arrow_w - 0.04, 0.36, fill=GOLD)
    # Below: key principles
    rounded_box(slide, 0.5, 5.0, 12.33, 1.7, fill=GOLD_TINT, stroke=GOLD, stroke_w=1.5)
    multiline(slide, 0.7, 5.1, 12.0, 1.55, [
        ("Три критерия применимости AI на PLC (без них — НЕ применяй):", {"size": 13, "bold": True, "color": MID}),
        ("(а) есть симулятор или двойник для валидации до развёртывания",
         {"size": 12, "color": DEEP}),
        ("(б) есть протоколы безопасности перед развёртыванием (IEC 61508 SIL 2/3 для критичных контуров)",
         {"size": 12, "color": DEEP}),
        ("(в) есть инженер с правом veto на каждое предложение AI",
         {"size": 12, "color": DEEP}),
    ], line_spacing=1.35)
    footer(slide, "Паттерн A1 — AI предлагает, человек решает; явное согласие на каждое изменение")


# ====================================================================
# SECTION 4 — A2 (§4) — s19 div + s20-s23
# ====================================================================

def s19_div(p):
    section_divider(p, 4, 4, "A2 — Замыкать петлю",
                    "Yokogawa FKDPP · двойник как песочница · разрыв «симуляция → реальность» · MPC альтернатива",
                    "Раздел 4 · замыкание петли с архитектурой двойника")


def s20_yokogawa(p):
    """s20 — Yokogawa FKDPP в JSR."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Yokogawa FKDPP в JSR: 35 дней RL на химзаводе, 2022",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Первый промышленного класса RL-кейс — алгоритм FKDPP + дистилляционная колонна JSR",
             size=13, italic=True, color=LIGHT)
    # Hero image
    img = ASSETS / "screenshots" / "s20-yokogawa-plant.jpg"
    if img.exists():
        add_image(slide, img, 0.5, 1.75, 6.5, 5.0)
        attribution(slide, "Дистилляционные колонны · Wikimedia · CC-BY-SA · аналог JSR",
                    x=0.5, y=6.8, w=6.5)
    # Right: cards
    rounded_box(slide, 7.2, 1.75, 5.6, 5.0, fill=SURFACE, stroke=MID, stroke_w=2.0)
    multiline(slide, 7.4, 1.9, 5.2, 4.8, [
        ("FKDPP", {"size": 22, "bold": True, "color": MID}),
        ("Факториальное ядровое", {"size": 11, "italic": True, "color": LIGHT}),
        ("динамическое программирование политик", {"size": 11, "italic": True, "color": LIGHT}),
        ("", {"size": 8}),
        ("Yokogawa + NAIST, 2018 · off-policy RL", {"size": 12, "color": DEEP}),
        ("факториальная ядровая декомпозиция", {"size": 12, "color": DEEP}),
        ("отмечено индустриальными наградами",
         {"size": 12, "italic": True, "color": GOLD}),
        ("", {"size": 8}),
        ("Чем уникален этот кейс:", {"size": 12, "bold": True, "color": MID}),
        ("· 35 дней непрерывной работы под RL",
         {"size": 12, "color": DEEP}),
        ("· дистилляционная колонна — A2 замкнутая петля",
         {"size": 12, "color": DEEP}),
        ("· оператор мог вмешаться, но не обязан",
         {"size": 12, "color": DEEP}),
        ("", {"size": 8}),
        ("КЛЮЧЕВОЕ:", {"size": 12, "bold": True, "color": GOLD}),
        ("Yokogawa имела внутренний двойник колонны — RL обучался в симуляции ДО переноса.",
         {"size": 11, "italic": True, "color": DEEP}),
    ], line_spacing=1.3)
    add_notes(slide, "Знаковый кейс A2. Yokogawa FKDPP — алгоритм, разработанный в Yokogawa совместно с NAIST (Нара) в 2018 году: off-policy обучение с подкреплением с факториальной ядровой декомпозицией. Алгоритм отмечен индустриальными наградами за вклад в промышленный ИИ. Применён к дистилляционной колонне на химическом заводе JSR в 2022 — 35 дней непрерывной автоматической работы под RL-контролем. Оператор мог вмешаться, но не обязан был. Это первый задокументированный случай RL в промышленной эксплуатации chemical plant промышленного класса. Критическое для лекции 12: Yokogawa имела внутреннюю физическую симуляцию колонны — массоперенос по Стефану-Максвеллу, теплоперенос по Фурье, тарелочная модель. RL обучался в этой песочнице до переноса. Без двойника это была бы слепая вера. Это центральный архитектурный угол лекции 12 — двойник как песочница для RL. В лекции 11 FKDPP разбирали как алгоритмический прорыв; здесь — как архитектурный механизм.")


def s21_twin_sandbox(p):
    """s21 — Digital twin as RL песочница."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Цифровой двойник как песочница для обучения RL",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Подъём с A1 на A2 без песочницы = слепая вера; NVIDIA Omniverse + Siemens Composer закрывают этот зазор",
             size=13, italic=True, color=LIGHT)
    # Left: NVIDIA HQ image
    img = ASSETS / "screenshots" / "s21-nvidia-omniverse.jpg"
    if img.exists():
        add_image(slide, img, 0.5, 1.75, 5.5, 5.0)
        attribution(slide, "NVIDIA HQ · Wikimedia · CC-BY-SA · Omniverse + Cosmos физический AI",
                    x=0.5, y=6.8, w=5.5)
    # Right: pipeline
    multiline(slide, 6.3, 1.85, 6.5, 0.5, [
        ("ЦИКЛ ОБУЧЕНИЯ RL В ПЕСОЧНИЦЕ:", {"size": 13, "bold": True, "color": MID}),
    ])
    stages = [
        ("1. Двойник", "точная модель оборудования + физика + поток данных", LIGHT),
        ("2. RL-агент", "обучается на 1000+ эпизодов симуляции — БЕЗ РИСКА для железа", MID),
        ("3. Валидация", "краевые случаи · анализ чувствительности · безопасная зона действия", TEAL),
        ("4. Перенос", "политика RL → реальное оборудование в теневом режиме", GOLD),
        ("5. Откат", "если сдвиг распределения — снимаем RL, проводной PLC берёт управление", DEEP),
    ]
    y = 2.4
    for i, (title, desc, color) in enumerate(stages):
        rounded_box(slide, 6.3, y, 6.5, 0.85, fill=SURFACE, stroke=color, stroke_w=1.5)
        rectangle(slide, 6.3, y, 0.2, 0.85, fill=color)
        text_box(slide, 6.55, y + 0.05, 6.2, 0.4, title,
                 size=13, bold=True, color=DEEP)
        text_box(slide, 6.55, y + 0.45, 6.2, 0.4, desc,
                 size=11, italic=True, color=DARK_GREY)
        y += 0.95
    add_notes(slide, "Это центральный архитектурный угол лекции 12, который отличает её от лекции 11. На A2 цифровой двойник становится критическим. Без него подъём с A1 на A2 — слепая вера. Цикл обучения RL в песочнице: первый шаг — точная модель оборудования с физикой и потоком данных. Второй — RL-агент обучается на тысячах эпизодов симуляции без риска для железа. Третий — валидация на краевых случаях. Четвёртый — перенос на реальное оборудование в теневом режиме (RL предлагает, но не действует). Пятый — откат: если сдвиг распределения — снимаем RL, проводной PLC берёт управление. Это и есть «мост» цифрового двойника. NVIDIA Omniverse + Cosmos на Hannover Messe 2026 представили фундаментальные модели физического AI — обучение в симуляции с переносом на реальное оборудование.")


def s22_sim_real_gap(p):
    """s22 — разрыв «симуляция → реальность» concrete example."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Разрыв «симуляция → реальность»: T=300°C → T=315°C из-за отложений",
             size=22, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Симуляция не моделировала тепловые потери и поверхностное загрязнение; выход RL за пределы — 10% от штатного режима",
             size=13, italic=True, color=LIGHT)
    # Chart left
    chart = ASSETS / "charts" / "s22-sim-real-gap.png"
    if chart.exists():
        rounded_box(slide, 0.5, 1.75, 8.0, 5.0)
        add_image(slide, chart, 0.7, 1.9, 7.6, 4.7)
    # Right card
    rounded_box(slide, 8.7, 1.75, 4.1, 5.0, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    multiline(slide, 8.9, 1.9, 3.7, 4.8, [
        ("ЧТО RL НЕ ВИДИТ:", {"size": 13, "bold": True, "color": GOLD, "align": PP_ALIGN.CENTER}),
        ("", {"size": 8}),
        ("· Поверхностное загрязнение — отложения на стенках колонны со временем",
         {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("· Тепловые потери в окружающую среду — зависят от изоляции и сезона",
         {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("· Дрейф датчиков — без калибровки термопары «уходят»",
         {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("РЕЗУЛЬТАТ:", {"size": 12, "bold": True, "color": MID}),
        ("Выход за пределы режима — 10% от штатного за 60 дней.",
         {"size": 11, "italic": True, "color": DEEP}),
        ("", {"size": 6}),
        ("УРОК:", {"size": 12, "bold": True, "color": MID}),
        ("Симуляция дешевле и быстрее, но без реальной физики не учитывает износ.",
         {"size": 11, "italic": True, "color": DEEP}),
    ], line_spacing=1.3)
    attribution(slide, "MDPI Processes 2025 · конкретный пример разрыва «симуляция → реальность»")


def s23_rl_limits_mpc(p):
    """s23 — RL limits + MPC alternative."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Где RL не применим: критичные по безопасности → проводной PLC + IEC 61508",
             size=22, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Известная физика → MPC, не RL · доказуемые гарантии устойчивости через теорию Ляпунова",
             size=13, italic=True, color=LIGHT)
    # Two columns
    col_y = 1.75
    col_h = 5.0
    col_w = 6.0
    # Left: критичный по безопасности
    rounded_box(slide, 0.5, col_y, col_w, col_h, fill=SURFACE, stroke=GOLD, stroke_w=2.0)
    rectangle(slide, 0.5, col_y, col_w, 0.7, fill=GOLD)
    text_box(slide, 0.5, col_y + 0.08, col_w, 0.55,
             "Критичный по безопасности контур",
             size=17, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    multiline(slide, 0.7, col_y + 0.9, col_w - 0.4, 4.0, [
        ("Почему RL не сертифицируется:", {"size": 13, "bold": True, "color": LIGHT}),
        ("· Нет журнала аудита для регулятора", {"size": 13, "color": DEEP}),
        ("· Недетерминированный вывод несовместим с IEC 61508 SIL 2/3",
         {"size": 13, "color": DEEP}),
        ("· Не покрывает краевые случаи по определению",
         {"size": 13, "color": DEEP}),
        ("", {"size": 8}),
        ("АЛЬТЕРНАТИВА:", {"size": 14, "bold": True, "color": GOLD}),
        ("· Проводной PLC + IEC 61508 SIL 2/3",
         {"size": 13, "color": DEEP}),
        ("· Формальная верификация (TLA+, SPIN, Coq, SCADE)",
         {"size": 13, "color": DEEP}),
        ("· SIL 2 = 10⁻⁶..10⁻⁷ отказов/час",
         {"size": 13, "bold": True, "color": DEEP}),
        ("· SIL 3 = 10⁻⁷..10⁻⁸ отказов/час",
         {"size": 13, "bold": True, "color": DEEP}),
    ], line_spacing=1.3)
    # Right: known physics
    rounded_box(slide, 6.83, col_y, col_w, col_h, fill=SURFACE, stroke=TEAL, stroke_w=2.0)
    rectangle(slide, 6.83, col_y, col_w, 0.7, fill=TEAL)
    text_box(slide, 6.83, col_y + 0.08, col_w, 0.55,
             "Процесс с известной физикой",
             size=17, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    multiline(slide, 7.03, col_y + 0.9, col_w - 0.4, 4.0, [
        ("Если уравнения известны (Навье–Стокса, теплоперенос, химическая кинетика):",
         {"size": 12, "italic": True, "color": LIGHT}),
        ("", {"size": 4}),
        ("MPC — Модельное предиктивное управление", {"size": 15, "bold": True, "color": DEEP}),
        ("", {"size": 6}),
        ("Преимущества MPC:", {"size": 13, "bold": True, "color": LIGHT}),
        ("· Доказуемые гарантии устойчивости",
         {"size": 13, "color": DEEP}),
        ("  (теория Ляпунова — теорема о функции энергии)",
         {"size": 12, "italic": True, "color": MID}),
        ("· Явная оптимизация на горизонте N",
         {"size": 13, "color": DEEP}),
        ("· Учитывает жёсткие ограничения (PV/MV/выход)",
         {"size": 13, "color": DEEP}),
        ("· Сертифицируется в фарме и нефтехимии",
         {"size": 13, "color": DEEP}),
        ("", {"size": 4}),
        ("RL даёт гибкость, MPC — гарантии.",
         {"size": 12, "italic": True, "bold": True, "color": GOLD}),
    ], line_spacing=1.3)


# ====================================================================
# SECTION 4.5 — A3 (§4.5) — s24 div + s25
# ====================================================================

def s24_div(p):
    section_divider(p, 5, 5, "A3 — Действовать автономно",
                    "Toyota Digit на RAV4 · BMW Leipzig humanoid · единичные кейсы 2026",
                    "Раздел 4.5 · верхняя ступень — единицы кейсов")


def s25_a3_cases(p):
    """s25 — A3 cases + 3 blockers."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "A3 в 2026: Toyota Digit + BMW Leipzig humanoid — единичные кейсы",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Три блокера массового A3: регуляторика + стоимость + сложность",
             size=13, italic=True, color=LIGHT)
    # Hero left
    img = ASSETS / "screenshots" / "s25-toyota-digit.jpg"
    if img.exists():
        add_image(slide, img, 0.5, 1.75, 5.8, 5.0)
        attribution(slide, "Humanoid-роботы на фабрике · Wikimedia · CC-BY-SA · аналог Agility Digit",
                    x=0.5, y=6.8, w=5.8)
    # Right: 3 blockers
    multiline(slide, 6.5, 1.85, 6.3, 0.45, [
        ("ТРИ СТРУКТУРНЫХ БЛОКЕРА A3:", {"size": 13, "bold": True, "color": MID}),
    ])
    blockers = [
        ("1. Регуляторика",
         "Для критичных по безопасности действий требуется IEC 61508 SIL 2/3 или ATEX Zone 0. RL и humanoid-роботы не сертифицируются.",
         GOLD),
        ("2. Стоимость",
         "Humanoid Agility Robotics — несколько сотен тысяч долларов за единицу. Окупается только в нишах с высокой стоимостью труда и предсказуемой задачей.",
         MID),
        ("3. Сложность",
         "A3 требует полный стек: двойник + ИИ на границе сети + безопасная зона действия + управление флотом. Большинство заводов не имеет ни одного компонента промышленного класса.",
         TEAL),
    ]
    y = 2.4
    for i, (title, desc, color) in enumerate(blockers):
        rounded_box(slide, 6.5, y, 6.3, 1.35, fill=SURFACE, stroke=color, stroke_w=1.5)
        rectangle(slide, 6.5, y, 0.18, 1.35, fill=color)
        text_box(slide, 6.78, y + 0.1, 5.9, 0.45, title,
                 size=15, bold=True, color=DEEP)
        text_box(slide, 6.78, y + 0.55, 5.9, 0.75, desc,
                 size=11, color=DARK_GREY, line_spacing=1.3)
        y += 1.45
    # Bottom takeaway
    rounded_box(slide, 6.5, y - 0.05, 6.3, 0.7, fill=GOLD_TINT, stroke=GOLD, stroke_w=1.5)
    text_box(slide, 6.7, y, 5.9, 0.65,
             "Паттерн 2026: A3-кейсы — логистические (Toyota Digit), не управляющие (никто не запустил RL автономно на химической колонне)",
             size=11, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.25)


# ====================================================================
# SECTION 5 — Where AI NOT applicable (§5) — s26 div + s27-s31
# ====================================================================

def s26_div(p):
    section_divider(p, 6, 6, "Где AI НЕ применим",
                    "Десять критериев · фарма+FDA рабочий пример · Gartner 40% отмен · 5 вопросов вендору",
                    "Раздел 5 · ядро лекции — критерии «AI не подходит»")


def s27_port_intro(p):
    """s27 — Southeast Asian Port intro hero §5."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Где AI не нужен — начинаем с анонимного кейса морского порта 2024",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Канонический случай Tesla 2018 разобран ранее; здесь — свежий провал 2024, прямо связан с keystone-двойником",
             size=13, italic=True, color=LIGHT)
    # Hero
    img = ASSETS / "screenshots" / "s27-port-harbor.jpg"
    if img.exists():
        add_image(slide, img, 0.5, 1.75, 7.5, 5.0)
        attribution(slide, "Контейнерный порт Антверпен (MPET-MSC PSA) · Wikimedia · CC-BY-SA",
                    x=0.5, y=6.8, w=7.5)
    # Right: text card
    rounded_box(slide, 8.2, 1.75, 4.6, 5.0, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    multiline(slide, 8.4, 1.9, 4.2, 4.8, [
        ("$12 млн", {"size": 38, "bold": True, "color": GOLD, "align": PP_ALIGN.CENTER}),
        ("на цифровой двойник", {"size": 12, "italic": True, "color": DARK_GREY, "align": PP_ALIGN.CENTER}),
        ("", {"size": 10}),
        ("18 месяцев", {"size": 28, "bold": True, "color": MID, "align": PP_ALIGN.CENTER}),
        ("пилот", {"size": 12, "italic": True, "color": DARK_GREY, "align": PP_ALIGN.CENTER}),
        ("", {"size": 10}),
        ("2024", {"size": 28, "bold": True, "color": TEAL, "align": PP_ALIGN.CENTER}),
        ("проект списан", {"size": 12, "italic": True, "color": DARK_GREY, "align": PP_ALIGN.CENTER}),
        ("", {"size": 12}),
        ("ВЫВОД:", {"size": 12, "bold": True, "color": GOLD, "align": PP_ALIGN.CENTER}),
        ("3D-визуализация без потока данных = музей, а не двойник.",
         {"size": 12, "bold": True, "color": DEEP, "align": PP_ALIGN.CENTER}),
    ], line_spacing=1.3)


def s28_ten_criteria(p):
    """s28 — 10 criteria matrix."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.6,
             "Десять структурных критериев «AI не подходит» + альтернативы",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.0, 12.33, 0.3,
             "Если один из критериев применим — задача НЕ для AI; альтернатива справа доказывает себя десятилетиями",
             size=11, italic=True, color=LIGHT)
    # 10 rows × 2 columns
    items = [
        ("1. Критичный по безопасности контур",  "Проводной PLC + IEC 61508 SIL 2/3 + формальная верификация"),
        ("2. Процесс с известной физикой",        "MPC — модельное предиктивное управление с гарантиями"),
        ("3. Редкое событие (MTBF >1 года, n<30)","Физическая симуляция + RCM"),
        ("4. Поиск дефектов нестабильного процесса", "Пересмотр процесса ПЕРЕД применением Vision AI"),
        ("5. Жёсткие допуски ±0,001 мм",         "Метрология + GD&T + SPC"),
        ("6. Универсальная генерация PLC-кода",  "Специализированный инструмент с инженером в петле ИЛИ инженер + симулятор"),
        ("7. Регулируемая среда без объяснимости (FDA 21 CFR Part 11, GAMP 5)",
         "Объяснимый ИИ (SHAP / LIME) + правила + журнал аудита"),
        ("8. ATEX Zone 0 — взрывоопасная среда",  "ATEX-сертифицированные датчики + удалённая обработка"),
        ("9. Стоимость AI > стоимости ошибки человека",
         "Не внедрять; направить бюджет на обучение оператора"),
        ("10. Отсутствие чёткого сценария (аудит данных не пройден)",
         "Аудит слоя данных (5 вопросов) + устранение замечаний ДО любого пилота"),
    ]
    y_start = 1.45
    row_h = 0.52
    for i, (crit, alt) in enumerate(items):
        y = y_start + i * row_h
        # Alternating row backgrounds
        if i % 2 == 0:
            rectangle(slide, 0.5, y, 12.33, row_h - 0.05, fill=SURFACE)
        # Left: criterion
        text_box(slide, 0.7, y + 0.1, 6.0, row_h - 0.15, crit,
                 size=11, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        # Right: alternative
        text_box(slide, 6.85, y + 0.1, 6.3, row_h - 0.15, alt,
                 size=11, italic=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
    # Skip outer gold border — alternating rows already provide visual structure
    # Footer hint
    rounded_box(slide, 0.5, 6.75, 12.33, 0.45, fill=GOLD_TINT, stroke=GOLD, stroke_w=1.5)
    text_box(slide, 0.7, 6.78, 12.0, 0.4,
             "Бонус: Gartner — к 2027 году 40% агентных AI-проектов будут отменены — задайте вендору пять вопросов",
             size=11, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)


def s29_pharma_fda(p):
    """s29 — Pharma + FDA worked example."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.6,
             "Проработанный пример: фарма-AI ±0,5% vs допуск FDA ±0,1%",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.0, 12.33, 0.3,
             "Конкретное применение принципа FDA 21 CFR Part 11 + GAMP 5 к фарма-AI",
             size=11, italic=True, color=LIGHT)
    # Flow diagram horizontal
    steps = [
        ("Задача",
         "AI рекомендует дозировку активного компонента в финальной формуляции таблеток",
         LIGHT),
        ("AI способен",
         "Учиться на исторических партиях, предсказывать дозировку «±0,5% от номинала», 90% точности на тесте",
         MID),
        ("FDA требует",
         "±0,1% точности для решения о выпуске партии (FDA 21 CFR Part 11 + GAMP 5)",
         GOLD),
        ("Разрыв",
         "Точность AI ±0,5% < требуемого допуска ±0,1% — НЕСОВМЕСТИМО",
         GOLD),
        ("Вердикт",
         "AI НЕ подходит для финального решения о выпуске партии",
         DEEP),
    ]
    y_start = 1.5
    box_h = 0.85
    gap = 0.08
    label_w = 2.2  # wider label band
    for i, (title, desc, color) in enumerate(steps):
        y = y_start + i * (box_h + gap)
        rounded_box(slide, 0.5, y, 12.33, box_h, fill=SURFACE, stroke=color, stroke_w=2.0)
        rectangle(slide, 0.5, y, label_w, box_h, fill=color)
        text_box(slide, 0.6, y + 0.15, label_w - 0.1, box_h - 0.2, title,
                 size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, 0.6 + label_w + 0.1, y + 0.15, 12.33 - label_w - 0.3, box_h - 0.2, desc,
                 size=12, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    # Alternative box
    y = y_start + len(steps) * (box_h + gap) + 0.05
    rounded_box(slide, 0.5, y, 12.33, 0.6, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    text_box(slide, 0.7, y + 0.1, 12.0, 0.5,
             "АЛЬТЕРНАТИВА: AI как советующий инструмент на этапе разработки процесса (±0,5% полезна) + человек в петле контроля качества + статистическая выборка партий для выпуска (валидированная по USP / GMP)",
             size=11, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.3)
    add_notes(slide, "Проработанный пример из главы §5.3. Сценарий: фармпроизводство, AI рекомендует дозировку активного компонента в финальной формуляции таблеток. Что AI способен: учиться на исторических партиях, предсказывать оптимальную дозировку с точностью ±0,5% от номинала, 90% точности на тестовом наборе. Что FDA требует: ±0,1% точности для решения о выпуске партии. Это FDA 21 CFR Part 11 + GAMP 5. Разрыв: точность AI ±0,5% меньше требуемой ±0,1% — несовместимо. Вердикт: AI не подходит для финального решения о выпуске партии. Альтернатива: AI как советующий инструмент на этапе разработки процесса, где точность ±0,5% полезна. Для выпуска — человек в петле контроля качества + статистическая выборка партий, валидированная по USP / GMP. Перекрёстная ссылка: лекция 7 ввела FDA 21 CFR Part 11 как принцип; этот кейс — конкретная инстанциация.")


def s30_gartner(p):
    """s30 — Gartner cancellation chart."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Gartner: 40% агентных AI-проектов отменены к 2027",
             size=28, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "+ 30% пилотов генеративного ИИ прекращены после фазы PoC · 75% двойников без окупаемости · разрыв ожиданий 11% / 14%",
             size=13, italic=True, color=LIGHT)
    chart = ASSETS / "charts" / "s30-gartner-cancellation.png"
    if chart.exists():
        rounded_box(slide, 0.5, 1.75, 8.5, 5.0)
        add_image(slide, chart, 0.7, 1.9, 8.1, 4.7)
    # Right column — interpretation
    rounded_box(slide, 9.2, 1.75, 3.6, 5.0, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    multiline(slide, 9.4, 1.9, 3.2, 4.8, [
        ("ЧТО ЭТО ЗНАЧИТ:", {"size": 12, "bold": True, "color": GOLD, "align": PP_ALIGN.CENTER}),
        ("", {"size": 10}),
        ("Студент 3 курса увидит презентацию «агентный AI для производства» в первый год работы.",
         {"size": 11, "color": DEEP}),
        ("", {"size": 8}),
        ("Это не означает, что AI не работает.", {"size": 11, "italic": True, "color": MID}),
        ("", {"size": 6}),
        ("Это означает, что распространение опережает инфраструктурную готовность.",
         {"size": 11, "color": DEEP}),
        ("", {"size": 10}),
        ("ЧТО ДЕЛАТЬ:", {"size": 12, "bold": True, "color": GOLD}),
        ("Задать вендору пять вопросов из следующего слайда.",
         {"size": 12, "bold": True, "color": DEEP}),
    ], line_spacing=1.3)
    attribution(slide, "Gartner via XMPRO 2026 · EY / DataMintelligence 2026 · Build in Digital [41] 2024–2025")


def s31_vendor_questions(p):
    """s31 — 5 vendor questions."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Пять вопросов вендору — практический инструмент для кармана",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Задайте до пилота · если ≥1 ответ невнятный — переходите к альтернативе",
             size=13, italic=True, color=LIGHT)
    questions = [
        ("1", "Покажите 3 задокументированных провала за последние 24 месяца в той же индустрии",
         "Без кейсов с провалами вендор продаёт завышенные ожидания"),
        ("2", "Что именно делает ваша система на A0 / A1 / A2 — где она в шкале автономии?",
         "Если вендор путается — он не понимает архитектурный класс продукта"),
        ("3", "Какой аудит слоя данных вы провели перед пилотом?",
         "Без аудита — урок «анонимного порта» повторится"),
        ("4", "Что вы предлагаете, если пилот провалится — возврат денег, изменение задачи, продолжение интеграции?",
         "Контракт без стратегии выхода — деньги в одну сторону"),
        ("5", "Можете показать референс-клиента в нашем подсегменте (process / discrete / regulated)?",
         "Общих референсов недостаточно; нужна точная индустриальная аналогия"),
    ]
    y_start = 1.8
    item_h = 0.95
    gap = 0.08
    for i, (num, q, why) in enumerate(questions):
        y = y_start + i * (item_h + gap)
        rounded_box(slide, 0.5, y, 12.33, item_h)
        circle(slide, 0.7, y + 0.15, 0.65, 0.65, fill=GOLD)
        text_box(slide, 0.7, y + 0.15, 0.65, 0.65, num,
                 size=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, 1.55, y + 0.1, 10.6, 0.45, q,
                 size=13, bold=True, color=DEEP)
        text_box(slide, 1.55, y + 0.55, 10.6, 0.4, why,
                 size=11, italic=True, color=DARK_GREY)
    footer(slide, "Каркас вопросов вендору — для любого AI-пилота на производстве")


# ====================================================================
# SECTION 6 — OT/IT (§6) — s32 div + s33-s35
# ====================================================================

def s32_div(p):
    section_divider(p, 7, 7, "OT/IT архитектура 2026",
                    "7 слоёв · OPC UA + MQTT + TSN · ИИ на границе сети <10 мс · Lighthouse 220+",
                    "Раздел 6 · техническая инфраструктура промышленного AI")


def s33_seven_layers(p):
    """s33 — 7-layer architecture."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Семь слоёв производственной AI-архитектуры 2026",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "OPC UA + TSN + ИИ на границе сети inference <10 мс — операционные условия для A2",
             size=13, italic=True, color=LIGHT)
    # 7 layers stacked
    layers = [
        ("7. Человек в цикле", "критичные по безопасности действия всегда требуют согласия; человек — финальная инстанция", GOLD),
        ("6. Облако",           "обучение моделей · аналитика флота · долгосрочное хранение", LIGHT),
        ("5. Цифровой двойник", "Siemens Xcelerator · NVIDIA Omniverse · AVEVA · PTC ThingWorx", TEAL),
        ("4. MES / SCADA",      "AI как советующий → замкнутая петля · диспетчер", MID),
        ("3. ИИ на границе сети", "промышленные ИИ-серверы на шкафах оборудования · инференс <10 мс (NVIDIA Jetson)", GOLD),
        ("2. Сеть",             "TSN — сеть с гарантированной задержкой, IEEE 802.1, детерминированный обмен", TEAL),
        ("1. Датчик",           "IIoT — OPC UA + MQTT · частота опроса ≥10× полосы управления", MID),
    ]
    y_start = 1.75
    h = 0.7
    gap = 0.05
    for i, (name, desc, color) in enumerate(layers):
        y = y_start + i * (h + gap)
        rounded_box(slide, 0.5, y, 12.33, h, fill=SURFACE, stroke=color, stroke_w=1.5)
        rectangle(slide, 0.5, y, 2.5, h, fill=color)
        text_box(slide, 0.65, y + 0.08, 2.3, h - 0.16, name,
                 size=13, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, 3.15, y + 0.08, 9.0, h - 0.16, desc,
                 size=12, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    footer(slide, "Стек распространяется через WEF Lighthouse Network — 220+ заводов в 35 странах")


def s34_opcua(p):
    """s34 — OPC UA + MQTT + TSN dataflow."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "OPC UA + MQTT + TSN: семантика, транспорт, детерминизм",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Три протокола покрывают разные задачи; вместе обеспечивают ИИ на границе сети inference <10 мс",
             size=13, italic=True, color=LIGHT)
    # Three columns
    items = [
        ("OPC UA",
         "Открытая платформа коммуникаций · единая архитектура",
         "Семантика данных",
         "Кодирует смысл информации: «это температура реактора», а не просто число.",
         "IEC 62541 · машиночитаемая модель",
         MID),
        ("MQTT",
         "Протокол передачи телеметрии через очередь сообщений",
         "Транспорт",
         "Брокер «публикация/подписка» для тысяч устройств; лёгкий, подходит для IIoT с ограниченным каналом.",
         "ISO/IEC 20922 · широкое распространение",
         TEAL),
        ("TSN",
         "Сеть с гарантированной задержкой",
         "Детерминизм",
         "IEEE 802.1 · гарантированная задержка доставки Ethernet-пакетов. Без него инференс ИИ на границе сети <10 мс невозможен.",
         "Стандарт IEEE 802.1Qbv + 802.1Qbu",
         GOLD),
    ]
    col_w = 4.0
    gap = 0.13
    x0 = 0.5
    y = 1.75
    for i, (name, fullname, role, desc, std, color) in enumerate(items):
        x = x0 + i * (col_w + gap)
        rounded_box(slide, x, y, col_w, 5.0, fill=SURFACE, stroke=color, stroke_w=2.0)
        rectangle(slide, x, y, col_w, 0.7, fill=color)
        text_box(slide, x + 0.1, y + 0.08, col_w - 0.2, 0.55, name,
                 size=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        multiline(slide, x + 0.2, y + 0.85, col_w - 0.4, 4.0, [
            (fullname, {"size": 10, "italic": True, "color": LIGHT}),
            ("", {"size": 8}),
            ("Роль:", {"size": 12, "bold": True, "color": MID}),
            (role, {"size": 16, "bold": True, "color": GOLD}),
            ("", {"size": 10}),
            ("Что делает:", {"size": 11, "bold": True, "color": LIGHT}),
            (desc, {"size": 11, "color": DEEP}),
            ("", {"size": 8}),
            ("Стандарт:", {"size": 11, "bold": True, "color": LIGHT}),
            (std, {"size": 11, "italic": True, "color": DARK_GREY}),
        ], line_spacing=1.35)
    footer(slide, "Без всех трёх — A2 невозможен; только OPC UA хватает на A0–A1, но не для замыкания петли")


def s35_lighthouse(p):
    """s35 — Lighthouse Network."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Lighthouse Network: 220+ заводов, 90% с AI, +16% EBIT vs peers",
             size=26, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Программа Всемирного экономического форума и McKinsey — заводы-образцы с полной AI-трансформацией",
             size=13, italic=True, color=LIGHT)
    # Chart left
    chart = ASSETS / "charts" / "s35-lighthouse-donut.png"
    if chart.exists():
        rounded_box(slide, 0.5, 1.75, 6.0, 5.0)
        add_image(slide, chart, 0.7, 1.9, 5.6, 4.7)
    # Right: stats cards
    stats = [
        ("220+", "заводов в программе", MID),
        ("35", "стран", LIGHT),
        ("23", "новых площадки в 2026", TEAL),
        ("90%", "новых внедрений включают AI", GOLD),
        ("+16%", "EBIT относительно сравнимых заводов", DEEP),
    ]
    y_start = 1.75
    item_h = 0.85
    gap = 0.08
    for i, (val, desc, color) in enumerate(stats):
        y = y_start + i * (item_h + gap)
        rounded_box(slide, 6.7, y, 6.1, item_h, fill=SURFACE, stroke=color, stroke_w=1.5)
        text_box(slide, 6.9, y + 0.15, 1.8, item_h - 0.3, val,
                 size=28, bold=True, color=color, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(slide, 8.8, y + 0.15, 3.9, item_h - 0.3, desc,
                 size=12, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    attribution(slide, "Всемирный экономический форум / McKinsey Lighthouse Network, январь 2026")


# ====================================================================
# SECTION 7 — РФ + Career (§7) — s36 div + s37-s38
# ====================================================================

def s36_div(p):
    section_divider(p, 8, 8, "Российский контекст + карьерный мост",
                    "ГОСТ Р 57700.37 · КАМАЗ · Росатом · Норникель · 4 роли инженера AI",
                    "Раздел 7 · отечественные кейсы и точки входа в индустрию")


def s37_russian(p):
    """s37 — Russian context."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Россия: ГОСТ Р 57700.37 + КАМАЗ + Росатом + Норникель",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Формальная регуляторная база + три якорных кейса промышленной эксплуатации",
             size=13, italic=True, color=LIGHT)
    # Two columns — KAMAZ image left, cases on right
    img = ASSETS / "screenshots" / "s37-kamaz.jpg"
    if img.exists():
        add_image(slide, img, 0.5, 1.75, 5.5, 4.5)
        attribution(slide, "КАМАЗ-43118 · Wikimedia · CC-BY-SA · пилот цифровых двойников РФ с 2020",
                    x=0.5, y=6.3, w=5.5)
    # Right: 3 cases
    cases = [
        ("КАМАЗ", "Пионер цифровых двойников РФ", "конвейер + НИОКР · электромобиль КАМА-1 c 2020", MID),
        ("Росатом", "Стратегия технологического суверенитета", "T-FLEX PLM · АтомМайнд с 2024", TEAL),
        ("Норникель", "Управление процессом флотации через ИИ", "отечественный кейс класса A2 · обогащение медно-никелевых руд", GOLD),
    ]
    y = 1.85
    for i, (name, role, desc, color) in enumerate(cases):
        rounded_box(slide, 6.3, y, 6.5, 1.4, fill=SURFACE, stroke=color, stroke_w=2.0)
        rectangle(slide, 6.3, y, 0.18, 1.4, fill=color)
        text_box(slide, 6.55, y + 0.1, 6.2, 0.45, name,
                 size=18, bold=True, color=DEEP)
        text_box(slide, 6.55, y + 0.55, 6.2, 0.35, role,
                 size=12, italic=True, color=MID)
        text_box(slide, 6.55, y + 0.9, 6.2, 0.45, desc,
                 size=11, color=DARK_GREY)
        y += 1.5
    # Bottom: GOST + 187-FZ
    rounded_box(slide, 6.3, 6.4, 6.5, 0.7, fill=GOLD_TINT, stroke=GOLD, stroke_w=1.5)
    text_box(slide, 6.5, 6.45, 6.1, 0.6,
             "ГОСТ Р 57700.37-2021 + 187-ФЗ КИИ — основа для производственного AI в РФ",
             size=11, bold=True, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.3)


def s38_career(p):
    """s38 — Career bridge: 4 roles."""
    slide = blank(p)
    set_bg(slide, WHITE)
    text_box(slide, 0.5, 0.4, 12.33, 0.7,
             "Карьерный мост: четыре роли инженера AI в производстве",
             size=24, bold=True, color=DEEP)
    text_box(slide, 0.5, 1.15, 12.33, 0.4,
             "Каждая роль — со своим стеком навыков и точкой входа в индустрию",
             size=13, italic=True, color=LIGHT)
    roles = [
        ("Инженер ИИ/МО\n(промышленный)",
         "Проектирует и обучает модели (Vision QC, прогн. обслуживание, тревоги); встраивает в среду исполнения на границе сети; следит за дрейфом",
         "Python + PyTorch · MLOps · OPC UA · статистика · знание физики процесса",
         MID),
        ("Инженер цифровых\nдвойников",
         "Строит и поддерживает двойник: датчики через OPC UA, физика + ML-модель оборудования, валидация точности",
         "Siemens Composer · NVIDIA Omniverse · PTC ThingWorx · САПР · OPC UA",
         TEAL),
        ("Специалист по\nинтеграции MES",
         "Внедряет советующий AI в существующий MES; настраивает процесс «рекомендация → согласие → исполнение»",
         "SQL · REST/OPC UA · Opcenter/FactoryTalk/SAP MII · бизнес-процессы цеха",
         GOLD),
        ("Инженер ИИ на\nгранице сети",
         "Развёртывает инференс на пограничных серверах (Jetson, Modicon edge); оптимизирует задержку, разрабатывает безопасную передачу управления",
         "C++/Rust · встроенный Linux · ONNX/TensorRT · планирование в реальном времени · кибербезопасность КИИ",
         LIGHT),
    ]
    card_w = 3.0
    gap = 0.13
    x0 = 0.5
    y = 1.75
    for i, (name, day_to_day, skills, color) in enumerate(roles):
        x = x0 + i * (card_w + gap)
        rounded_box(slide, x, y, card_w, 4.9, fill=SURFACE, stroke=color, stroke_w=2.0)
        rectangle(slide, x, y, card_w, 1.0, fill=color)
        text_box(slide, x + 0.1, y + 0.1, card_w - 0.2, 0.85, name,
                 size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
        multiline(slide, x + 0.2, y + 1.15, card_w - 0.4, 3.6, [
            ("День за днём:", {"size": 11, "bold": True, "color": LIGHT}),
            (day_to_day, {"size": 11, "color": DEEP}),
            ("", {"size": 8}),
            ("Ключевые навыки:", {"size": 11, "bold": True, "color": LIGHT}),
            (skills, {"size": 10, "italic": True, "color": DARK_GREY}),
        ], line_spacing=1.3)
    # Bottom
    rounded_box(slide, 0.5, 6.85, 12.33, 0.35, fill=GOLD_TINT, stroke=GOLD, stroke_w=1.5)
    text_box(slide, 0.7, 6.88, 12.0, 0.3,
             "Где учиться: профильные технические магистратуры по AI в промышленности + онлайн-курсы NVIDIA Omniverse, Siemens Industrial AI",
             size=10, italic=True, color=DEEP, align=PP_ALIGN.CENTER)


# ====================================================================
# CLOSING — s39
# ====================================================================

def s39_closing(p):
    """s39 — Closing hero: Cassie/Digit-class humanoid bridge к Лекции 13. Hero ≥40% (6.7×6.0 = 40.2%).
    Acquisition: Wikimedia Tier 2 — Cassie robot, Agility Robotics, Oregon State Research Forest, CC-BY-SA.
    Cassie — bipedal precursor of Digit; same company (Agility Robotics) — semantically valid bridge.
    """
    slide = blank(p)
    set_bg(slide, WHITE)
    # Hero image acquisition priority:
    # 1. s39-cassie-digit.jpg (Wikimedia, Cassie robot Agility Robotics)
    # 2. s25-toyota-digit.jpg (Humanoid factory)
    # 3. s39-toyota-line.jpg (Toyota Burnaston — fallback)
    img_cassie = ASSETS / "screenshots" / "s39-cassie-digit.jpg"
    img_humanoid = ASSETS / "screenshots" / "s25-toyota-digit.jpg"
    img_factory = ASSETS / "screenshots" / "s39-toyota-line.jpg"
    if img_cassie.exists():
        img = img_cassie
        attr_text = "Cassie · Agility Robotics (компания-производитель Digit) · Oregon State · Wikimedia · CC-BY-SA"
    elif img_humanoid.exists():
        img = img_humanoid
        attr_text = "Humanoid-роботы на фабрике · Wikimedia · CC-BY-SA · аналог Toyota Digit"
    else:
        img = img_factory
        attr_text = "Toyota Motor Manufacturing · Wikimedia · CC-BY-SA"
    if img.exists():
        add_image(slide, img, 0.4, 0.5, 6.7, 6.0)
        attribution(slide, attr_text, x=0.4, y=6.55, w=6.7)
    # Right column
    multiline(slide, 7.3, 0.6, 5.7, 1.5, [
        ("Закрытие лекции 12", {"size": 16, "bold": True, "color": LIGHT}),
        ("", {"size": 6}),
        ("A0 → A1 → A2 → A3", {"size": 26, "bold": True, "color": DEEP}),
        ("+ цифровой двойник как мост", {"size": 17, "bold": True, "color": MID}),
    ], line_spacing=1.1)
    # Recap card
    rounded_box(slide, 7.3, 2.3, 5.7, 2.5, fill=SURFACE, stroke=LIGHT, stroke_w=1.5)
    multiline(slide, 7.5, 2.4, 5.3, 2.3, [
        ("ЧТО МЫ ЗНАЕМ ТЕПЕРЬ:", {"size": 11, "bold": True, "color": MID}),
        ("", {"size": 6}),
        ("· A0: Vision QC + прогн. обслуживание с границами", {"size": 11, "color": DEEP}),
        ("· A1: MES + предсказание тревог + PLC Copilot",
         {"size": 11, "color": DEEP}),
        ("· A2: RL + двойник как песочница (Yokogawa)",
         {"size": 11, "color": DEEP}),
        ("· A3: humanoid-логистика — единично",
         {"size": 11, "color": DEEP}),
        ("· 10 критериев «AI не нужен» + 5 вопросов вендору",
         {"size": 11, "bold": True, "color": GOLD}),
    ], line_spacing=1.3)
    # Bridge
    rounded_box(slide, 7.3, 5.0, 5.7, 2.0, fill=GOLD_TINT, stroke=GOLD, stroke_w=2.0)
    multiline(slide, 7.5, 5.1, 5.3, 1.8, [
        ("МОСТ К ЛЕКЦИИ 13:", {"size": 12, "bold": True, "color": GOLD, "align": PP_ALIGN.CENTER}),
        ("", {"size": 4}),
        ("AI в логистике, цепях", {"size": 16, "bold": True, "color": DEEP, "align": PP_ALIGN.CENTER}),
        ("поставок и транспорте", {"size": 16, "bold": True, "color": DEEP, "align": PP_ALIGN.CENTER}),
        ("", {"size": 4}),
        ("Toyota Digit между станциями — первая ступень цепочки поставок",
         {"size": 11, "italic": True, "color": MID, "align": PP_ALIGN.CENTER}),
    ], line_spacing=1.15)
    add_notes(slide, "Что мы унесли из лекции 12. Производственная автоматизация устроена как шкала автономии A0–A3. A0 — наблюдать: vision QC и прогностическое обслуживание, безопасные ступени с критериями применимости. A1 — советовать: MES в советующем режиме, предсказание тревог, PLC Copilot с инженером в loop. A2 — замыкать петлю: Yokogawa FKDPP в JSR 35 дней, единичные production-кейсы, twin как песочница для RL. A3 — действовать автономно: Toyota Digit на RAV4, BMW Leipzig — единицы 2026, три блокера массового A3. Десять критериев «AI не нужен» — для рамки решения. Пять вопросов вендору — для кармана. Лекция 13 — AI в логистике, цепях поставок и транспорте. Toyota Digit между станциями — это первая ступень supply chain. Лекция 13 расширит эту ось от одного цеха к глобальной цепочке поставок.")


print("Loaded part 2 of build_lec12.py")
