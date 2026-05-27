"""
Slide builders for Лекции 15 — part 2 (s12-s25).
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


# ========== SECTION 2 — Experiment (s12-s19) ==========

def s12_section2_divider(p):
    """s12 — section 2 divider (Phase 8: top bar removed; tags 6→4; methodology strip)."""
    slide = blank(p)
    set_slide_bg(slide, SURFACE)

    text_box(slide, 0.5, 1.5, 5.0, 3.0, "§2",
             size=200, bold=True, color=GOLD, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)
    multiline_box(slide, 5.5, 1.7, 7.3, 4.0, [
        ("Раздел 2", {"size": 22, "bold": True, "color": MID}),
        ("Experiment", {"size": 42, "bold": True, "color": DEEP}),
        ("Эксперимент", {"size": 26, "color": LIGHT, "italic": True}),
        ("", {"size": 12}),
        ("Прорывы нобелевского уровня",
            {"size": 18, "color": DEEP}),
        ("и их трещины.", {"size": 18, "bold": True, "color": GOLD, "italic": True}),
    ], line_spacing=1.2)

    # Phase 8: trim 6→4 tags + narrower spacing (canonical Nobel-tier subset)
    tags = [
        ("AlphaFold + Нобель", GOLD),
        ("GNoME / A-Lab", TEAL),
        ("Aurora 5000×", LIGHT),
        ("AlphaProof IMO", MID),
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

    attribution(slide, "Лестница цикла · ступень 3 · 4 working cases · 3 трещины", y=6.95)

    add_notes(slide, "Раздел 2 — Experiment. Это самый сильный успех AI в науке. Здесь — нобелевский прорыв и одновременно три неочевидные трещины.\n\nAlphaFold взял Нобелевскую премию по химии 2024 за предсказание трёхмерной структуры белков. Это конкретный AI-продукт в формулировке Нобеля — первый в истории. Boltz-1 — открытая модель конкурент AlphaFold 3 от MIT. GNoME от DeepMind предсказала 380 тысяч стабильных материалов. A-Lab Berkeley синтезировал 41 из 58 за 17 дней. Aurora — Microsoft модель погоды в 5000 раз быстрее эталона ECMWF. AlphaProof+AlphaGeometry 2 взяли серебро на Международной математической олимпиаде 2024.\n\nИ трещины. Палгрейв и Шуп в январе 2024 проверили 36 проб A-Lab — 35 содержат ошибки. ECMWF использует собственную AIFS оперативно с 25 февраля 2025, не Aurora. AlphaFold даёт 22% галлюцинаций в IDP-регионах. AlphaProof решил P1, P2, P6, но не P3 и P5 (комбинаторика). Каждый прорыв с трещиной.\n\nЦель раздела — показать оба измерения. Не «AI взял Нобель, теперь всё решено», но и не «всё провалилось». Реальный инженерный взгляд: где AI работает, и где даже AlphaFold не работает.")


def s13_alphafold_timeline(p):
    """s13 — AlphaFold timeline + Recursion-Roche industry impact."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "AlphaFold 3 — 8 мая 2024. Нобель — 9 октября 2024. Каскад: $12B.")

    # Two laureate photos
    add_image(slide, IMG / "s13-hassabis-nobel.jpg", 0.5, 1.5, 2.5, 2.8)
    text_box(slide, 0.5, 4.3, 2.5, 0.3, "Демис Хассабис",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(slide, 0.5, 4.6, 2.5, 0.3, "DeepMind",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)

    add_image(slide, IMG / "s13-baker-nobel.jpg", 3.2, 1.5, 2.5, 2.8)
    text_box(slide, 3.2, 4.3, 2.5, 0.3, "Дэвид Бейкер",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(slide, 3.2, 4.6, 2.5, 0.3, "University of Washington",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)

    # AlphaFold ribbon
    add_image(slide, IMG / "s13-alphafold3-frame.png", 5.9, 1.5, 3.2, 3.0)
    text_box(slide, 5.9, 4.5, 3.2, 0.3, "Послойное предсказание AlphaFold 3",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)

    # Timeline right column
    rounded_box(slide, 9.3, 1.5, 3.6, 3.0, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 9.5, 1.65, 3.2, 2.8, [
        ("Хронология:", {"size": 13, "bold": True, "color": GOLD}),
        ("", {"size": 4}),
        ("декабрь 2021", {"size": 11, "bold": True, "color": MID}),
        ("Recursion + Roche — $150M upfront",
            {"size": 11, "color": DEEP}),
        ("до 40 программ × >$300M = до $12B", {"size": 10, "italic": True, "color": SLATE}),
        ("", {"size": 6}),
        ("8 мая 2024", {"size": 11, "bold": True, "color": MID}),
        ("AlphaFold 3 / Isomorphic Labs",
            {"size": 11, "color": DEEP}),
        ("Nature 630, статья 06792", {"size": 10, "italic": True, "color": SLATE}),
        ("", {"size": 6}),
        ("9 октября 2024", {"size": 12, "bold": True, "color": GOLD}),
        ("Нобелевская премия по химии",
            {"size": 12, "bold": True, "color": DEEP}),
        ("Hassabis + Jumper + Baker", {"size": 10, "italic": True, "color": SLATE}),
    ], line_spacing=1.15)

    # Bottom takeaway
    rounded_box(slide, 0.5, 5.5, 12.33, 1.2, fill=SURFACE, stroke=LIGHT, stroke_w=2)
    multiline_box(slide, 0.8, 5.6, 11.8, 1.05, [
        ("Каскад нобелевской премии:",
            {"size": 13, "bold": True, "color": MID}),
        ("AlphaFold — первая в истории Нобелевская премия по фундаментальной науке за конкретный AI-продукт. 13 лет от научной публикации до Нобеля — рекордно короткий цикл.",
            {"size": 13, "color": DEEP, "italic": True}),
    ], line_spacing=1.2)

    attribution(slide,
        "© Nobel Foundation 2024 + © DeepMind/Isomorphic Labs 2024 · Recursion 8-K SEC dec 2021",
        y=6.95)

    add_notes(slide, "AlphaFold — это центральный позитивный кейс лекции и самый сильный успех AI в науке. Разберём timeline.\n\nДекабрь 2021. Recursion Pharmaceuticals подписывает многомиллиардное партнёрство с Roche. 40 программ drug discovery с использованием AlphaFold-based структурных предсказаний, минимум $300 миллионов upfront, до $12 миллиардов суммарной потенциальной выплаты по достижении milestone'ов. Это первый каскадный коммерческий эффект AlphaFold.\n\n8 мая 2024. Google DeepMind и Isomorphic Labs опубликовали AlphaFold 3 в Nature, paper s41586-024-06792-0. Расширение от только-белок к белок-лиганд, белок-нуклеиновая кислота, antibody-antigen. Это уже не один тип структур, а вся биомолекулярная экосистема.\n\n9 октября 2024. Шведская королевская академия наук объявила Нобелевскую премию по химии. Половина — Дэвид Бейкер из Вашингтонского университета за вычислительное проектирование белков. Вторая половина разделена между Демисом Хассабисом и Джоном Джампером из DeepMind за AlphaFold.\n\nЭто исторически первая Нобелевская премия по фундаментальной науке, в формулировке которой стоит конкретный AI-продукт. 13 лет от научной публикации AlphaFold 1 (2018) до Нобеля — рекордно короткий цикл. Обычно Нобель присуждают за работы 20-30-летней давности.\n\nКаскад: AlphaFold показал, что AI в науке способен на структурный прорыв нобелевского уровня в закрытой задаче, где доступна эталонная разметка через PDB.")


def s14_alphafold_db(p):
    """s14 — AlphaFold DB scale + open-source debate."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "200M структур vs 200K в PDB. 1000× — но AlphaFold 3 был закрыт.")

    # AlphaFold ribbon
    add_image(slide, IMG / "s14-alphafold-ribbon.png", 0.3, 1.5, 6.0, 4.0)
    attribution(slide, "AlphaFold 2 ribbon (Wikimedia CC-BY-SA) · alphafold.ebi.ac.uk",
                x=0.3, y=5.55, w=6.0)

    # Scale comparison + timeline right
    rounded_box(slide, 6.7, 1.5, 6.3, 2.0, fill=SURFACE, stroke=LIGHT, stroke_w=2)
    multiline_box(slide, 6.9, 1.7, 5.9, 1.85, [
        ("Масштаб ускорения:", {"size": 13, "bold": True, "color": MID}),
        ("", {"size": 4}),
        ("PDB (1971-): 200 тысяч структур за 53 года", {"size": 13, "color": DEEP}),
        ("AlphaFold DB (2021-): 200 миллионов за 4 года",
            {"size": 14, "bold": True, "color": GOLD}),
        ("Ускорение — 1000×",
            {"size": 17, "bold": True, "color": GOLD, "italic": True}),
        ("(каждая известная белковая последовательность из UniProt)",
            {"size": 11, "italic": True, "color": SLATE}),
    ], line_spacing=1.2)

    # Дискуссия об открытом коде
    rounded_box(slide, 6.7, 3.7, 6.3, 2.6, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 6.9, 3.85, 5.9, 2.4, [
        ("Открытый код — дискуссия:", {"size": 13, "bold": True, "color": GOLD}),
        ("", {"size": 4}),
        ("8 мая 2024", {"size": 11, "bold": True, "color": MID}),
        ("AlphaFold 3 — закрытая (только сервер Isomorphic)",
            {"size": 12, "color": DEEP}),
        ("", {"size": 4}),
        ("ноябрь 2024", {"size": 11, "bold": True, "color": MID}),
        ("Открытое письмо 1000+ учёных",
            {"size": 12, "color": DEEP}),
        ("«Невоспроизводимая наука для академии»",
            {"size": 11, "italic": True, "color": SLATE}),
        ("", {"size": 4}),
        ("ноябрь 2024 → февраль 2025", {"size": 11, "bold": True, "color": MID}),
        ("Академический доступ → публичный некоммерческий",
            {"size": 12, "color": DEEP}),
    ], line_spacing=1.15)

    attribution(slide,
        "Источники: alphafold.ebi.ac.uk · Nature 2024-2025 · Nature News editorial ноябрь 2024",
        y=6.95)

    add_notes(slide, "AlphaFold DB — это самая большая структурная база данных в истории биологии. Разберём масштаб и open-source debate.\n\nProtein Data Bank, PDB, открылся в 1971 году. Это база экспериментально определённых трёхмерных структур белков — рентгеновская кристаллография, NMR, cryo-EM. За 53 года к 2024 году PDB накопил около 200 тысяч структур. Это медленный процесс: каждая структура требует месяцев или лет экспериментальной работы.\n\nAlphaFold DB запустилась в 2021 году. К 2024 — 200 миллионов структур. Это в тысячу раз больше, чем PDB накопил за половину века. И это покрывает каждую известную белковую последовательность в базе UniProt — фактически весь известный протеом всех изученных организмов.\n\nНо AlphaFold 3 при запуске был закрыт. 8 мая 2024 года Isomorphic Labs выкатил систему только через сервер с ограниченным API. Без открытых весов, без локального запуска. Это вызвало серьёзное недовольство в академическом сообществе.\n\nВ ноябре 2024 года было опубликовано открытое письмо за подписями более тысячи учёных. Главная претензия — невоспроизводимая наука. Если работа использует AlphaFold 3, но AlphaFold 3 закрыт, никто не может независимо проверить результаты.\n\nИзменение позиции произошло поэтапно. С ноября 2024 — академический non-commercial доступ. С февраля 2025 — публичный non-commercial. Коммерческое использование по-прежнему требует лицензии Isomorphic. Это компромисс, но открытость возросла под давлением сообщества.")


def s15_boltz_open_source(p):
    """s15 — Boltz-1 open-source catches up to AlphaFold 3."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Boltz-1 — открытый конкурент AlphaFold 3. К концу 2025 — догнал.")

    # Chart left
    img = CHARTS / "s15-boltz-vs-af3.png"
    add_image(slide, img, 0.4, 1.5, 7.5, 4.2)

    # Right column: Boltz timeline + meaning (Phase 8: Russified)
    rounded_box(slide, 8.0, 1.5, 5.0, 4.2, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 8.2, 1.7, 4.6, 4.0, [
        ("Хронология:", {"size": 13, "bold": True, "color": GOLD}),
        ("", {"size": 4}),
        ("декабрь 2024", {"size": 11, "bold": True, "color": MID}),
        ("Boltz-1 — MIT", {"size": 12, "color": DEEP}),
        ("Wohlwend, Corso et al.", {"size": 10, "italic": True, "color": SLATE}),
        ("Полностью открытый код + веса", {"size": 11, "color": DEEP}),
        ("", {"size": 6}),
        ("осень 2025", {"size": 11, "bold": True, "color": MID}),
        ("Boltz-2 → почти-AlphaFold 3", {"size": 12, "color": DEEP}),
        ("в академическом внедрении", {"size": 10, "italic": True, "color": SLATE}),
        ("", {"size": 6}),
        ("Закономерность повторяется:",
            {"size": 12, "bold": True, "color": GOLD}),
        ("• Stable Diffusion vs DALL-E 2",
            {"size": 10, "color": DEEP}),
        ("• LLaMA vs GPT-4",
            {"size": 10, "color": DEEP}),
        ("• Boltz vs AlphaFold 3", {"size": 10, "color": DEEP}),
        ("", {"size": 4}),
        ("Если достаточно хороша —", {"size": 10, "italic": True, "color": MID}),
        ("открытая обгоняет закрытую.", {"size": 11, "bold": True, "color": GOLD}),
    ], line_spacing=1.15)

    attribution(slide,
        "Источники: Corso, Wohlwend et al. biorxiv 2024.11.19.624167 (Boltz-1) · Wohlwend et al. biorxiv 2025 (Boltz-2)",
        y=6.95)

    add_notes(slide, "Boltz-1 — это очень важный кейс открытой альтернативы. В декабре 2024 группа из MIT, авторы Wohlwend, Corso и коллеги, выпустили Boltz-1. Это полностью открытый аналог AlphaFold 3: открытый код, открытые веса, полная документация. Они работали с публикацией AlphaFold 3 как с reference и реконструировали архитектуру.\n\nК концу 2025 года Boltz-2, следующая версия, обогнала AlphaFold 3 по академическому внедрению. То есть в реальных научных работах учёные стали чаще использовать Boltz, чем закрытый AlphaFold 3.\n\nВажные нюансы. По строгим бенчмаркам Boltz-1 чуть-чуть уступает AlphaFold 3 в нескольких задачах: белок-лиганд (76 против 72 GDT_TS), antibody-antigen (68 против 64). По чисто-белковым структурам они практически равны.\n\nЗакономерность повторяется в истории AI. Когда Stable Diffusion вышел открытым в августе 2022, он был немного хуже DALL-E 2 от OpenAI. Через год Stable Diffusion обогнал DALL-E по реальному использованию. Когда LLaMA вышел открытым в феврале 2023, он уступал GPT-4. Через год open-source альтернативы стали стандартом de facto.\n\nЭто закономерность: если открытая альтернатива достаточно хороша (на 80-90% от закрытой), она обгоняет закрытую по реальному внедрению. Причина простая — open-source модели можно дообучать, проверять, модифицировать, использовать без зависимости от вендора. Для научной работы это критично.\n\nУрок для инженера: при выборе AI-инструмента для научной задачи всегда оценивайте, есть ли открытая альтернатива. Часто она есть и работает.")


def s16_gnome_alab(p):
    """s16 — GNoME + A-Lab; 41 of 58 in 17 days (canonical numbers)."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "GNoME 380 тысяч стабильных. A-Lab 41 из 58 за 17 дней.")

    # Chart left
    img = CHARTS / "s16-gnome-alab.png"
    add_image(slide, img, 0.4, 1.5, 7.5, 3.5)

    # Right column: GNoME architecture + A-Lab details
    rounded_box(slide, 8.0, 1.5, 5.0, 3.5, fill=SURFACE, stroke=LIGHT, stroke_w=2)
    multiline_box(slide, 8.2, 1.65, 4.6, 3.3, [
        ("Архитектура GNoME:", {"size": 13, "bold": True, "color": MID}),
        ("Графовая нейросеть (GNN)", {"size": 11, "color": DEEP}),
        ("+ 6 раундов активного обучения",
            {"size": 11, "bold": True, "color": GOLD}),
        ("(выбор кандидатов на следующий раунд)",
            {"size": 10, "italic": True, "color": SLATE}),
        ("", {"size": 6}),
        ("Масштаб vs альтернатив:",
            {"size": 13, "bold": True, "color": MID}),
        ("• Materials Project — 48k", {"size": 11, "color": DEEP}),
        ("• Open Quantum Materials — 60k", {"size": 11, "color": DEEP}),
        ("• GNoME — 380k стабильных",
            {"size": 11, "bold": True, "color": GOLD}),
        ("  (44× больше Materials Project)",
            {"size": 10, "italic": True, "color": SLATE}),
        ("", {"size": 6}),
        ("A-Lab Berkeley (Цеймански):",
            {"size": 13, "bold": True, "color": MID}),
        ("58 кандидатов из GNoME",
            {"size": 11, "color": DEEP}),
        ("17 дней автономный синтез",
            {"size": 11, "color": DEEP}),
        ("41 из 58 успешно (71%)",
            {"size": 12, "bold": True, "color": GOLD}),
    ], line_spacing=1.15)

    # Bottom narrative
    rounded_box(slide, 0.4, 5.15, 12.63, 1.5, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 0.7, 5.3, 12.0, 1.3, [
        ("Что это значит:", {"size": 13, "bold": True, "color": GOLD}),
        ("GNoME — графовая нейросеть с 6 раундами активного обучения предсказала 380 тысяч стабильных материалов — в 44 раза больше Materials Project. A-Lab Berkeley синтезировал 41 из 58 кандидатов автономно за 17 дней. Это самый быстрый темп открытия материалов в истории.",
            {"size": 13, "color": DEEP, "italic": True}),
    ], line_spacing=1.2)

    attribution(slide,
        "Источники: Merchant et al. Nature 2023 (GNoME) · Szymanski et al. Nature 2023 (A-Lab)",
        y=6.95)

    add_notes(slide, "Второй центральный позитивный кейс раздела — GNoME и A-Lab Berkeley. Это материаловедение, не структурная биология, но архитектура и масштаб одного порядка с AlphaFold.\n\nGNoME — Graph Networks for Materials Exploration — это система от DeepMind, опубликованная в Nature в 2023 году. Архитектура — графовая нейросеть с активным обучением. Modify: не «22 итерации» как часто пишут в популярной литературе — а ровно 6 раундов активного обучения. В каждом раунде модель предсказывает наиболее перспективных кандидатов, эти кандидаты проверяются через DFT (density functional theory) расчёты, результаты возвращаются как новые обучающие данные.\n\nИтоговый масштаб: 2,2 миллиона кандидатов изначально, из них 380 тысяч предсказаны как стабильные. Для сравнения: Materials Project — основная база материалов в исследованиях — содержит около 48 тысяч соединений. Open Quantum Materials — 60 тысяч. GNoME в 44 раза больше Materials Project.\n\nA-Lab Berkeley, опубликован Цеймански и коллегами в Nature 2023 года. Это автономная лаборатория синтеза материалов. 58 кандидатов из GNoME были выбраны для синтеза. За 17 дней автономной работы лаборатория синтезировала 41 из 58 — успешность 71%.\n\nЭто канонические числа в материалах: 41 из 58 за 17 дней. Запомните их. В популярных пересказах часто пишут «36 из 57», но Nature 2023 paper говорит именно 41 из 58.\n\nЭто прорыв подлинного масштаба. Самый быстрый темп открытия новых материалов в истории. Закрытый мир (физика твёрдого тела + DFT) делает задачу решаемой через AI.")


def s17_palgrave_critique(p):
    """s17 — Palgrave critique of A-Lab; 35 of 36 contain errors."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Палгрейв и Шуп проверили 36 проб A-Lab. 35 содержали ошибки.")

    # Pie chart of error breakdown
    img = CHARTS / "s17-palgrave.png"
    add_image(slide, img, 0.3, 1.5, 7.0, 4.0)

    # Right column: 3 error types details
    rounded_box(slide, 7.5, 1.5, 5.5, 4.0, fill=SURFACE, stroke=RED_WARN, stroke_w=2)
    multiline_box(slide, 7.7, 1.65, 5.1, 3.8, [
        ("3 типа ошибок (35 из 36):",
            {"size": 14, "bold": True, "color": RED_WARN}),
        ("", {"size": 6}),
        ("1. Неверная фаза (12 проб)",
            {"size": 12, "bold": True, "color": DEEP}),
        ("Кристаллическая структура отличается от предсказанной",
            {"size": 11, "italic": True, "color": MID}),
        ("", {"size": 4}),
        ("2. Производные известных (15 проб)",
            {"size": 12, "bold": True, "color": DEEP}),
        ("Соединение помечено как «новое», но это известная фаза",
            {"size": 11, "italic": True, "color": MID}),
        ("", {"size": 4}),
        ("3. Отсутствие функции (8 проб)",
            {"size": 12, "bold": True, "color": DEEP}),
        ("Соединение существует, но без проверки целевого свойства",
            {"size": 11, "italic": True, "color": MID}),
        ("", {"size": 6}),
        ("Только 1 из 36 — полное открытие",
            {"size": 13, "bold": True, "color": RED_WARN}),
        ("(новая фаза + новая функция + воспроизводимо)",
            {"size": 10, "italic": True, "color": SLATE}),
    ], line_spacing=1.15)

    # Bottom takeaway
    rounded_box(slide, 0.3, 5.6, 12.73, 1.05, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 0.6, 5.7, 12.13, 0.9, [
        ("Главный урок:", {"size": 13, "bold": True, "color": GOLD}),
        ("Предсказание ≠ открытие. AI предсказывает кристаллографически стабильные структуры. Открытие требует проверки функции, проверки новизны, воспроизведения. Без человека в петле остановки конвейера на каждой пробе — каскад ошибочных «открытий».",
            {"size": 13, "color": DEEP, "italic": True}),
    ], line_spacing=1.2)

    attribution(slide,
        "Источник: Palgrave & Schoop ChemRxiv январь 2024 (CC-BY) · ответ Szymanski et al. в Nature",
        y=6.95)

    add_notes(slide, "Это критическая трещина в кейсе A-Lab. Помните результат: 41 из 58 за 17 дней. Это выглядит как нобелевский прорыв в материаловедении. В январе 2024 года Palgrave и Schoop из Ливерпуля и Принстона опубликовали в ChemRxiv тщательный пересмотр результатов A-Lab.\n\nИх метод — взяли 36 заявленных синтезированных кандидатов, проверили каждый через рентгеновскую дифракцию и литературный поиск. Результат: 35 из 36 содержали хотя бы одну из трёх типов ошибок.\n\nТип 1, 12 проб — неверная фаза. Кристаллическая структура того, что синтезировано, отличается от предсказанной GNoME. Возможно, синтезирована действительно другая фаза того же химического состава.\n\nТип 2, 15 проб — производные известных соединений. То, что A-Lab объявил «новым материалом», по литературному поиску оказался известным соединением, известной фазой или производной известной структуры.\n\nТип 3, 8 проб — отсутствие функции. Соединение действительно существует, но не было проверено целевое свойство, ради которого его «искали». Например, заявленный полупроводник не был протестирован на полупроводниковые свойства.\n\nТолько 1 из 36 — полное открытие в строгом смысле: новая фаза + новая функция + воспроизводимый синтез.\n\nГлавный урок для инженера: предсказание не равно открытие. AI хорошо предсказывает кристаллографически стабильные структуры — это в пределах его обучения. Но открытие в науке требует проверки функции, проверки новизны через тщательный литературный поиск, воспроизведения через независимый эксперимент. Без человека в петле остановки конвейера на каждой пробе — каскад ошибочных «открытий» с тяжёлыми последствиями для следующих циклов поиска.")


def s18_aurora_ecmwf(p):
    """s18 — Aurora 5000× faster but ECMWF AIFS is operational."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Aurora 5000× быстрее эталона. Но ECMWF использует AIFS — свою модель.")

    # Atmospheric model schematic
    add_image(slide, IMG / "s18-atmospheric-model.png", 0.3, 1.5, 5.5, 3.5)
    attribution(slide, "Wikimedia · Схема атмосферной модели (CC-BY-SA)",
                x=0.3, y=5.05, w=5.5)

    # Aurora speed chart
    img = CHARTS / "s18-aurora-speed.png"
    add_image(slide, img, 6.0, 1.5, 7.0, 3.5)

    # ECMWF logo + text (Phase 8: Russified)
    rounded_box(slide, 0.3, 5.4, 12.73, 1.3, fill=SURFACE, stroke=GOLD, stroke_w=2)
    add_image(slide, IMG / "s18-ecmwf.png", 0.45, 5.55, 1.1, 1.05)
    multiline_box(slide, 1.7, 5.5, 11.3, 1.15, [
        ("Что говорит ECMWF (Европейский центр среднесрочных прогнозов):",
            {"size": 12, "bold": True, "color": GOLD}),
        ("AIFS оперативна с 25 февраля 2025 — собственная AI-модель ECMWF, не Aurora. IFS физика (1979-) + AIFS работают параллельно. Редкие события (ураганы, аномальные холода) системно недопредставлены в AI-моделях; политическим решениям нужен физический эталон.",
            {"size": 12, "color": DEEP, "italic": True}),
    ], line_spacing=1.18)

    attribution(slide,
        "Источники: Bodnar et al. arxiv 2405.13063 (Aurora) · ECMWF news 25 февраля 2025 (AIFS)",
        y=6.95)

    add_notes(slide, "Aurora — это пример классического случая «5000× быстрее на бенчмарке, но непригоден для production». Разберём.\n\nMicrosoft Research в мае 2024 опубликовал Aurora — большую foundation model атмосферной физики. Архитектура — transformer с временной размерностью, обученный на ~миллионе часов реанализа ECMWF плюс спутниковые данные. В бенчмарке на стандартных метеорологических переменных (температура, давление, ветер) Aurora показывает 5000-кратное ускорение по сравнению с эталоном IFS (Integrated Forecasting System) ECMWF.\n\nЭто валидное число для конкретного бенчмарка. Но это НЕ оперативная замена.\n\n25 февраля 2025 года ECMWF объявил, что собственная AI-модель — AIFS (Artificial Intelligence Forecasting System) — стала оперативной. Это значит, что AIFS теперь используется для реальных прогнозов параллельно с физической IFS. Aurora НЕ используется ECMWF оперативно.\n\nПочему? Tail events. То есть редкие, но критически важные события — ураганы, аномальные похолодания, наводнения — системно недопредставлены в обучающих данных AI-моделей. Если в обучении было мало 50-летних штормов, модель будет плохо их предсказывать. А именно эти tail events — то, ради чего нужны метеопрогнозы для критических политических решений (эвакуация населения, закрытие аэропортов).\n\nECMWF использует AIFS для повседневных прогнозов, где она хороша. Физическую IFS — как baseline, особенно для оценки tail risks. Это разумная архитектура: AI для скорости, физика для надёжности.\n\nДля инженера урок: «5000× быстрее» в бенчмарке не значит «можно деплоить в продакшн». Прежде чем заменить физическую модель AI-моделью, проверьте distribution shift на критических редких событиях.")


def s19_alphaproof_imo(p):
    """s19 — AlphaProof + AlphaGeometry 2 silver at IMO 2024."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "AlphaProof + AlphaGeometry 2 = 28 из 42 = серебро IMO 2024.")

    # IMO logo
    add_image(slide, IMG / "s19-imo-logo.png", 0.4, 1.5, 3.0, 2.2)
    attribution(slide, "© Wikimedia · International Mathematical Olympiad",
                x=0.4, y=3.8, w=3.0)

    # Per-problem chart
    img = CHARTS / "s19-alphaproof-imo.png"
    add_image(slide, img, 3.7, 1.5, 6.0, 3.5)

    # Right column: details
    rounded_box(slide, 10.0, 1.5, 3.0, 3.5, fill=SURFACE, stroke=LIGHT, stroke_w=2)
    multiline_box(slide, 10.15, 1.65, 2.7, 3.3, [
        ("AlphaProof:", {"size": 12, "bold": True, "color": MID}),
        ("Reinforcement learning",
            {"size": 11, "color": DEEP}),
        ("+ formal Lean theorem prover",
            {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("Решены:", {"size": 12, "bold": True, "color": GOLD}),
        ("P1, P2, P6 (по 7 баллов)",
            {"size": 11, "bold": True, "color": DEEP}),
        ("", {"size": 4}),
        ("AlphaGeometry 2:",
            {"size": 12, "bold": True, "color": MID}),
        ("LLM + symbolic solver",
            {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("Решена:", {"size": 12, "bold": True, "color": GOLD}),
        ("P4 (7 баллов)",
            {"size": 11, "bold": True, "color": DEEP}),
        ("", {"size": 4}),
        ("Не решены:", {"size": 12, "bold": True, "color": RED_WARN}),
        ("P3 и P5 (комбинаторика)",
            {"size": 11, "color": DEEP}),
    ], line_spacing=1.15)

    # Bottom narrative
    rounded_box(slide, 0.4, 5.4, 12.63, 1.25, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 0.7, 5.5, 12.03, 1.1, [
        ("Что это значит — и чего не значит:",
            {"size": 13, "bold": True, "color": GOLD}),
        ("28 из 42 баллов = серебро. Формальная математика — закрытый мир: доказательства проверяются Lean-верификатором. Время решения: 4-7 часов на задачу vs 90 минут у человека. P3 и P5 (комбинаторика) — нерешённая граница: задачи требуют конструктивных приёмов, не покрытых обучением.",
            {"size": 13, "color": DEEP, "italic": True}),
    ], line_spacing=1.18)

    attribution(slide,
        "Источник: DeepMind blog июль 2024 · Nature DOI 10.1038/s41586-025-09833-y (AlphaProof)",
        y=6.95)

    add_notes(slide, "AlphaProof — третий значимый кейс раздела Experiment. В июле 2024 года DeepMind объявила, что AlphaProof в комбинации с AlphaGeometry 2 решила 4 из 6 задач Международной математической олимпиады 2024 года. Общий результат — 28 баллов из 42, что соответствует серебряной медали среди людей-участников.\n\nАрхитектура. AlphaProof — это reinforcement learning система, которая работает с формальным верификатором Lean. Доказательство задачи представляется как последовательность формальных шагов в Lean; модель учится предлагать следующий шаг, верификатор проверяет корректность. Это похоже на AlphaGo в Go: пространство ходов очень большое, но проверка корректности дешёвая.\n\nAlphaGeometry 2 — это другая система, LLM в комбинации с symbolic solver для геометрических задач. Опубликована в Nature в январе 2024.\n\nКонкретное распределение задач IMO 2024. AlphaProof решила P1, P2 и P6 — три задачи из шести, по 7 баллов каждая, итого 21. AlphaGeometry 2 решила P4 — геометрическая задача — ещё 7 баллов. Итого 28. P3 и P5 — комбинаторика — обе нерешённые.\n\nКлючевые ограничения. Первое — время. На каждую задачу AlphaProof тратила 4-7 часов вычислений на GPU. Человеку-участнику даётся 90 минут. То есть AI не «решает быстрее», он использует значительно больше вычислений.\n\nВторое — комбинаторика остаётся нерешённой границей. P3 и P5 — комбинаторные задачи. Это задачи, где доказательство требует нахождения хитрой комбинаторной конструкции — не «применить известную технику», а «придумать новую». На этом классе AlphaProof пока не сходится.\n\nФормальная математика — это закрытый мир. Доказательства проверяются Lean-верификатором, нет амбигвитета. Поэтому AI работает в этой области. Но даже в закрытом мире остаются классы задач, где автоматизация не справляется.")


# ========== SECTION 3 — Analyse (s20-s25) ==========

def s20_section3_divider(p):
    """s20 — section 3 divider (Phase 8: top bar removed; tags 5→4; methodology strip)."""
    slide = blank(p)
    set_slide_bg(slide, SURFACE)

    text_box(slide, 0.5, 1.5, 5.0, 3.0, "§3",
             size=200, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)
    multiline_box(slide, 5.5, 1.7, 7.3, 4.0, [
        ("Раздел 3", {"size": 22, "bold": True, "color": MID}),
        ("Analyse", {"size": 42, "bold": True, "color": DEEP}),
        ("Анализ данных", {"size": 26, "color": LIGHT, "italic": True}),
        ("", {"size": 12}),
        ("Узкие задачи,",
            {"size": 18, "color": DEEP}),
        ("эталонная разметка,", {"size": 18, "color": DEEP}),
        ("надёжные применения.", {"size": 18, "bold": True, "color": MID}),
    ], line_spacing=1.2)

    # Phase 8: trim 5→4 tags + narrower
    tags = [
        ("CNN экзопланеты", LIGHT),
        ("MICrONS", MID),
        ("LIGO + конформное", TEAL),
        ("AlphaFold IDP трещина", RED_WARN),
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

    attribution(slide, "Лестница цикла · ступень 4 · 4 working cases", y=6.95)

    add_notes(slide, "Раздел 3 — Analyse, анализ данных. Это надёжные применения AI в науке. Узкие задачи: дано большое количество размеченных или полуразмеченных данных, нужно найти паттерн.\n\nЧетыре кейса. Обнаружение экзопланет через CNN на light curves TESS и Kepler — задача из 2018 года, 1 595 высокоуверенных кандидатов (Huang & Jiang 2025). Allen MICrONS — нейронная коннектомика, один кубический миллиметр зрительной коры мыши. LIGO ML-конвейер для гравитационных волн с конформным предсказанием — калиброванный 95% доверительный интервал. И трещина — AlphaFold даёт 22% галлюцинаций в IDP-регионах. Используете AlphaFold для интерфейсов с разупорядоченными белками без оговорки — публикуете загрязнённый результат.\n\nЗакрываем раздел разобранным примером WE-TESS — пятишаговая рамка от классификации задачи к валидации на отложенных. Это применимая рамка для ML-развёртывания в analyse-фазе.")


def s21_exoplanet_cnn(p):
    """s21 — CNN exoplanet detection (Phase 8: Huang & Jiang 1595 cascade fix)."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Экзопланеты CNN: 1 595 высокоуверенных кандидатов TESS, 83,9% точность.")

    # TESS satellite image
    add_image(slide, IMG / "s21-tess.jpg", 0.4, 1.5, 4.5, 3.0)
    attribution(slide, "© NASA TESS 2018+ (CC-PD)", x=0.4, y=4.55, w=4.5)

    # AUC chart
    img = CHARTS / "s21-cnn-auc.png"
    add_image(slide, img, 5.0, 1.5, 5.5, 3.0)

    # Right column: details
    rounded_box(slide, 10.6, 1.5, 2.5, 3.0, fill=SURFACE, stroke=LIGHT, stroke_w=2)
    multiline_box(slide, 10.75, 1.65, 2.2, 2.8, [
        ("Числа:", {"size": 13, "bold": True, "color": MID}),
        ("", {"size": 4}),
        ("кандидаты TESS", {"size": 11, "color": DEEP}),
        ("из миссий 2018+", {"size": 10, "italic": True, "color": SLATE}),
        ("", {"size": 4}),
        ("CNN → ранжирование", {"size": 11, "color": DEEP}),
        ("", {"size": 2}),
        ("1 595 высокоуверенных",
            {"size": 11, "bold": True, "color": GOLD}),
        ("(точность 83,9%)",
            {"size": 11, "bold": True, "color": GOLD}),
        ("", {"size": 4}),
        ("Pre-trained Kepler → TESS",
            {"size": 11, "color": MID}),
        ("(перенос обучения)",
            {"size": 10, "italic": True, "color": SLATE}),
    ], line_spacing=1.15)

    # Bottom narrative
    rounded_box(slide, 0.4, 5.3, 12.63, 1.35, fill=SURFACE, stroke=LIGHT, stroke_w=2)
    multiline_box(slide, 0.7, 5.4, 12.0, 1.2, [
        ("Почему это надёжный кейс:",
            {"size": 13, "bold": True, "color": MID}),
        ("Эталонная разметка — подтверждённые транзиты из Kepler (8 000+ примеров). Узкая задача — бинарная классификация: транзит / шум. Привычное обучение с учителем — CNN на временных рядах. AUC от BLS (Kovács et al. 2002) 78% → pre-trained CNN 89% → custom CNN на TESS+Kepler 92%. Не «новый AI», а зрелое ML.",
            {"size": 12, "color": DEEP, "italic": True}),
    ], line_spacing=1.2)

    attribution(slide,
        "Источники: Shallue & Vanderburg ApJ 155 (2018) · Huang & Jiang arxiv 2512.00967",
        y=6.95)

    add_notes(slide, "Первый кейс раздела Analyse — обнаружение экзопланет через CNN. Это эталонный пример надёжного применения AI в науке. Не громкий, не «нобелевский», но именно тот класс, в котором AI работает безупречно.\n\nКонтекст. TESS — Transiting Exoplanet Survey Satellite, запущен NASA в 2018 году. Наблюдает яркость звёзд во времени. Когда планета проходит между звездой и наблюдателем, яркость на короткое время падает — это транзит. Обнаружение транзитов в зашумлённых временных рядах — задача с десятилетиями традиции в астрономии.\n\nКлассический алгоритм BLS (Box Least Squares) — формализован Kovács, Zucker, Mazeh в 2002 году (Astronomy & Astrophysics 391): точность ранжирования 78% AUC. Pre-trained CNN — модель, обученная на Kepler missions (предыдущий проект NASA), потом дообученная на TESS — 89% AUC. Custom CNN, специально построенный на joint TESS+Kepler train set — 92% AUC.\n\nКонкретные цифры из работы Huang & Jiang arxiv 2512.00967 (2025). Через CNN ранжирование выделено 1 595 высокоуверенных кандидатов. Точность бинарной классификации (транзит vs шум) на тестовой выборке — 83,9%.\n\nПочему это надёжный кейс? Три причины. Первая — эталонная разметка. Каждый кандидат, который мы используем для тренировки, был независимо подтверждён радиовелосиметрическим следованием — то есть наземные телескопы измерили доплеровское смещение звезды и подтвердили наличие планеты. Это ground truth, который не зависит от модели.\n\nВторая — узкая задача. Бинарная классификация: есть транзит или нет. Не «понять, что такое планета», не «обобщить на новые типы объектов». Очень узкая задача с чёткой метрикой.\n\nТретья — это привычное обучение с учителем, не «новый AI». CNN на временных рядах — стандартная техника с 2010-х. Здесь нет foundation modelling, нет multi-modal, нет LLM. Это инженерная задача, решённая инженерными методами.\n\nУрок: в Analyse-фазе чаще всего работает старое доброе ML. Foundation models — это маркетинг. Узкое CNN с правильной разметкой — это деньги.")


def s22_allen_microns(p):
    """s22 — Allen MICrONS connectome project."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "Allen MICrONS: 1 мм³ коры мыши — 120k нейронов, 500M синапсов.")

    # Allen Institute photo
    add_image(slide, IMG / "s22-allen-institute.jpg", 0.4, 1.5, 4.0, 2.5)
    attribution(slide, "© Allen Institute 2025", x=0.4, y=4.05, w=4.0)

    # Connectome MRI visualization
    add_image(slide, IMG / "s22-connectome.png", 4.6, 1.5, 4.0, 2.5)
    attribution(slide, "MRI Tractography — нервные пути · Wikimedia", x=4.6, y=4.05, w=4.0)

    # Mouse brain
    add_image(slide, IMG / "s22-mouse-brain.jpg", 8.8, 1.5, 4.2, 2.5)
    attribution(slide, "Wikimedia · мышиный мозг", x=8.8, y=4.05, w=4.2)

    # Numbers
    rounded_box(slide, 0.4, 4.5, 12.63, 1.4, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 0.7, 4.65, 12.0, 1.2, [
        ("Allen MICrONS, апрель 2025 — Nature 640 (2025):",
            {"size": 13, "bold": True, "color": GOLD}),
        ("Один кубический миллиметр зрительной коры мыши = 120 000 анатомических нейронов · 500 миллионов синапсов · 4 километра аксонов.",
            {"size": 14, "color": DEEP, "italic": True}),
        ("Задача невозможна без AI: U-Net + transformer для сегментации каждой клетки на десятках тысяч слоёв электронной микроскопии.",
            {"size": 13, "color": MID, "italic": True}),
    ], line_spacing=1.18)

    # Limitation
    rounded_box(slide, 0.4, 6.05, 12.63, 0.6, fill=SURFACE, stroke=LIGHT, stroke_w=1.5)
    text_box(slide, 0.7, 6.1, 12.0, 0.55,
             "Граница: 1 мм³ vs 500 мм³ мозга мыши = 500× масштабирование требует тысячи GPU-часов. Полный мозг мыши пока недосягаем.",
             size=12, italic=True, color=DEEP)

    attribution(slide, "Источник: Allen Institute / MICrONS Consortium Nature 640 (2025)", y=6.85)

    add_notes(slide, "Второй кейс надёжной аналитики — Allen Institute MICrONS, нейронная коннектомика. Опубликован в Nature 640 в апреле 2025 года. Это самый детальный участок мозга, когда-либо реконструированный с клеточным разрешением.\n\nКонтекст. Цель MICrONS — построить полную карту связей нейронов в маленьком участке мозга мыши. Конкретно — один кубический миллиметр зрительной коры. Это маленькая область, но плотность данных огромная.\n\nЧисла. 120 тысяч анатомических нейронов в этом миллиметре. Между ними — 500 миллионов синаптических связей. Длина всех аксонов и дендритов вместе — около 4 километров в одном миллиметре ткани.\n\nКак это сделано. Образец мозга мыши заморозили, нарезали на сверхтонкие срезы — десятки тысяч слоёв толщиной несколько нанометров каждый. Каждый слой сфотографировали через электронный микроскоп. Получили терабайты изображений. Эти изображения нужно сегментировать — найти границы каждой клетки, каждого синапса, каждого аксона. Вручную это невозможно: годы работы тысяч аспирантов.\n\nAI делает сегментацию автоматически. Архитектура — комбинация U-Net (стандартная архитектура для сегментации изображений с 2015 года) и transformer (для учёта контекста между слоями). Результат — алгоритмическая реконструкция 3D-структуры каждого нейрона и синапса.\n\nЭто пример задачи, невозможной без AI. Не «можно ускорить» — просто буквально невозможно. Объём данных слишком велик для ручной обработки.\n\nГраница. Эта работа — 1 кубический миллиметр. Полный мозг мыши — около 500 кубических миллиметров. Чтобы масштабировать с 1 до 500, нужно в 500 раз больше вычислений. Это тысячи GPU-часов и петабайты данных. Технически возможно за десятилетие, но не сегодня.\n\nУрок: AI расширяет границы того, что можно физически проанализировать. Раньше мы могли реконструировать одну нервную клетку — теперь сотню тысяч. Это не «AI делает науку», это «AI делает доступным то, что раньше требовало нереалистичных трудозатрат».")


def s23_ligo_ml(p):
    """s23 — LIGO ML pipeline with conformal prediction."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "LIGO ML: CNN + конформное предсказание = калиброванный 95% интервал.")

    # LIGO control room
    add_image(slide, IMG / "s23-ligo.jpg", 0.4, 1.5, 4.5, 2.5)
    attribution(slide, "© LIGO/Caltech 2024 · LLO Control Room", x=0.4, y=4.05, w=4.5)

    # Black holes
    add_image(slide, IMG / "s23-blackholes.jpg", 5.1, 1.5, 4.5, 2.5)
    attribution(slide, "Caltech-MIT-LIGO/SXS · столкновение чёрных дыр", x=5.1, y=4.05, w=4.5)

    # Conformal interval chart
    img = CHARTS / "s23-conformal.png"
    add_image(slide, img, 9.8, 1.5, 3.2, 2.5)

    # Bottom narrative
    rounded_box(slide, 0.4, 4.5, 12.63, 2.15, fill=SURFACE, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 0.7, 4.65, 12.0, 2.0, [
        ("Что такое конформное предсказание (conformal prediction):",
            {"size": 14, "bold": True, "color": GOLD}),
        ("", {"size": 4}),
        ("Метод даёт калиброванный 95% доверительный интервал на каждое предсказание модели — БЕЗ предположений о нормальности распределения данных.",
            {"size": 13, "color": DEEP}),
        ("", {"size": 4}),
        ("Архитектура LIGO 2024+: CNN сначала ранжирует кандидаты сигналов на потоке. Конформное предсказание даёт интервал «вероятность гравитационной волны 0.7-0.9 с p<0.05». Matched filter (классический метод 1949 года, фильтр Винера) выполняет финальную атрибуцию параметров источника.",
            {"size": 12, "color": MID}),
        ("", {"size": 4}),
        ("AI здесь дополняет — не заменяет — 80-летнее наследие классической обработки сигналов.",
            {"size": 13, "bold": True, "color": GOLD, "italic": True}),
    ], line_spacing=1.18)

    attribution(slide,
        "Источники: Ashton et al. arxiv 2504.17587 (conformal prediction LIGO) · North 1943 (matched filter)",
        y=6.95)

    add_notes(slide, "LIGO — третий кейс раздела Analyse. Гравитационные волны. И здесь принципиально важная архитектура: AI дополняет наследие классической обработки сигналов, не заменяет.\n\nКонтекст. LIGO регистрирует крошечные деформации пространства-времени, вызванные катаклизмическими событиями — слиянием чёрных дыр или нейтронных звёзд. Поток данных огромный, событий мало. Задача — найти редкие сигналы в огромном шумовом фоне.\n\nКлассический метод — matched filter, фильтр согласованной свёртки. Опубликован North в 1943 году в техническом отчёте Bell Labs, развит Wiener'ом параллельно. 80 лет в эксплуатации. Принцип: знаем форму ожидаемого сигнала (предсказанную общей теорией относительности), фильтруем шум, ищем максимальное совпадение.\n\nAI добавляет два слоя. Первый — CNN для первичной фильтрации потока. Сотни тысяч кандидатов сигналов в секунду. CNN отбирает топ-100, которые отправляются на matched filtering.\n\nВторой — конформное предсказание для калиброванного доверительного интервала. Это критическая особенность работы Ashton et al. (arxiv 2504.17587, 2025).\n\nЧто такое конформное предсказание. Это статистический метод, который даёт калиброванный 95% доверительный интервал на каждое предсказание модели, не делая предположений о нормальности распределения. Конкретно: вместо «модель предсказывает событие с вероятностью 0.85», она даёт «событие с вероятностью 0.7-0.9, p<0.05». Это калиброванный диапазон.\n\nПочему важно. Гравитационные волны — редкие события, и каждое требует независимой атрибуции — какие массы, какое расстояние, какая ориентация. Калиброванный интервал означает, что когда модель говорит 95% уверенности, это действительно 95% реальной частоты. Не «иногда модель overconfident».\n\nФинальная атрибуция параметров — masses, distance, sky location — остаётся за matched filtering. AI делает первичный отбор кандидатов; физика делает финальное измерение.\n\nЭто архитектура «AI дополняет, не заменяет». 80 лет наследия классической обработки сигналов работают, AI расширяет их возможности. Урок инженеру: не выбрасывайте старые проверенные методы при добавлении AI. Используйте их вместе.")


def s24_alphafold_idp(p):
    """s24 — AlphaFold IDP hallucination crack (22% in disordered regions)."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "AlphaFold даёт 22% галлюцинаций в IDP-регионах. Паркинсон публикуете загрязнённо.")

    # Protein structure image
    add_image(slide, IMG / "s24-protein-structure.png", 0.5, 1.5, 4.0, 3.5)
    attribution(slide, "Wikimedia · стандартная белковая структура (CC-BY)", x=0.5, y=5.05, w=4.0)

    # IDP details right column
    rounded_box(slide, 4.8, 1.5, 4.0, 3.5, fill=SURFACE, stroke=RED_WARN, stroke_w=2)
    multiline_box(slide, 5.0, 1.65, 3.6, 3.3, [
        ("IDP — Intrinsically Disordered Protein",
            {"size": 13, "bold": True, "color": RED_WARN}),
        ("", {"size": 4}),
        ("Что это:", {"size": 12, "bold": True, "color": MID}),
        ("Белок без стабильной 3D-структуры; существует как ансамбль конформаций",
            {"size": 11, "color": DEEP, "italic": True}),
        ("", {"size": 4}),
        ("Распространённость:", {"size": 12, "bold": True, "color": MID}),
        ("30-40% человеческого протеома",
            {"size": 11, "color": DEEP}),
        ("содержит IDP-регионы",
            {"size": 11, "color": DEEP}),
        ("", {"size": 4}),
        ("Конкретный пример:",
            {"size": 12, "bold": True, "color": MID}),
        ("α-Синуклеин (белок Паркинсона)",
            {"size": 11, "color": DEEP}),
        ("Полностью IDP в нативной форме",
            {"size": 11, "italic": True, "color": MID}),
        ("AlphaFold даёт правдоподобную, но фантомную структуру",
            {"size": 11, "italic": True, "color": RED_WARN}),
    ], line_spacing=1.15)

    # pLDDT thresholds + mitigation right
    rounded_box(slide, 9.1, 1.5, 4.0, 3.5, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    multiline_box(slide, 9.3, 1.65, 3.6, 3.3, [
        ("pLDDT пороги:", {"size": 13, "bold": True, "color": GOLD}),
        ("", {"size": 4}),
        ("> 90 — очень высокая уверенность",
            {"size": 11, "color": DEEP}),
        ("70-90 — уверенность приемлемая",
            {"size": 11, "color": DEEP}),
        ("50-70 — низкая уверенность",
            {"size": 11, "color": DEEP}),
        ("< 50 — IDP или галлюцинация",
            {"size": 11, "bold": True, "color": RED_WARN}),
        ("", {"size": 6}),
        ("Mitigation:", {"size": 13, "bold": True, "color": GOLD}),
        ("• Фильтровать по pLDDT > 70",
            {"size": 11, "color": DEEP}),
        ("• NMR для подтверждения",
            {"size": 11, "color": DEEP}),
        ("• AlphaFold-Multimer + ансамбли",
            {"size": 11, "color": DEEP}),
        ("• Маркировать IDP-регионы явно",
            {"size": 11, "bold": True, "color": GOLD}),
    ], line_spacing=1.15)

    # Bottom warning
    rounded_box(slide, 0.5, 5.65, 12.53, 1.0, fill=SURFACE, stroke=RED_WARN, stroke_w=2)
    text_box(slide, 0.8, 5.75, 12.03, 0.85,
             "Главная ошибка инженера: использовать AlphaFold для IDP-регионов без оговорки → публикация фантомной структуры → каскад загрязнённых работ.",
             size=13, bold=True, color=RED_WARN, italic=True, anchor=MSO_ANCHOR.MIDDLE)

    attribution(slide,
        "Источники: Akdel et al. Nature Struct Mol Biol 2022 · Gopalan & Narayanan arxiv 2510.15939 (2025)",
        y=6.95)

    add_notes(slide, "AlphaFold IDP — это критическая трещина в самом успешном AI-в-науке кейсе. Каждый инженер, использующий AlphaFold, должен понимать это ограничение.\n\nIDP — Intrinsically Disordered Protein, внутренне разупорядоченный белок. Это белок, не имеющий стабильной трёхмерной структуры. Существует как ансамбль быстро меняющихся конформаций. Не одна форма — облако форм.\n\nЭто не редкая аномалия. 30-40% человеческого протеома содержит IDP-регионы. Многие белки, играющие ключевую роль в регуляции, передаче сигнала, развитии заболеваний, имеют значительные IDP-компоненты.\n\nКонкретный пример. α-Синуклеин — белок, ассоциированный с болезнью Паркинсона. В нативной форме полностью неупорядочен. Однако AlphaFold даёт правдоподобную трёхмерную структуру для α-синуклеина. Если вы возьмёте эту структуру и спроектируете на её основе лекарство, попадаете в проблему: структура не отражает реальное поведение белка в клетке.\n\nКонкретные цифры. Работа Akdel et al. в Nature Structural & Molecular Biology 2022 года — 22% галлюцинаций в IDP-регионах для AlphaFold 2. Работа Gopalan & Narayanan arxiv 2025 года — детальный анализ для AlphaFold 3, аналогичные цифры, не улучшилось значимо.\n\nMitigation. Главный инструмент — pLDDT score, который AlphaFold выдаёт для каждой аминокислоты. pLDDT > 90 — очень высокая уверенность модели. 70-90 — приемлемо. 50-70 — низкая. Меньше 50 — это либо IDP, либо галлюцинация модели.\n\nРекомендация для научной работы. Первое — всегда фильтровать предсказания по pLDDT > 70. Второе — для критических задач (особенно дизайн лекарств) подтверждать NMR или другим экспериментальным методом. Третье — использовать AlphaFold-Multimer для белковых комплексов и ансамбли (несколько предсказаний с разной инициализацией) для оценки конформационной гетерогенности. Четвёртое — явно маркировать IDP-регионы в любой публикации.\n\nГлавная инженерная ошибка — использовать AlphaFold для IDP-регионов без оговорки. Это публикация фантомной структуры. Следующая работа использует ваш результат как ground truth, цикл загрязнения распространяется.")


def s25_we_tess(p):
    """s25 — walked example WE-TESS: 5-step ML deployment framework."""
    slide = blank(p)
    set_slide_bg(slide, WHITE)
    slide_header(slide,
        "WE-TESS: 5-шаговая рамка ML-развёртывания в Analyse-фазе.")

    # Input task at top
    rounded_box(slide, 0.5, 1.5, 12.33, 0.6, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    text_box(slide, 0.5, 1.5, 12.33, 0.6,
             "Задача: «Нужно обнаружить экзопланеты в light curves TESS» — какую модель использовать?",
             size=14, bold=True, color=DEEP, italic=True,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    # 5 steps in horizontal flow (Phase 8: Russified labels + canonical numbers)
    steps = [
        ("1", "Пересечение данных", "Совпадают ли\nраспределения\nTESS ↔ Kepler?", LIGHT,
            "Спектры схожи — pre-train на Kepler работает"),
        ("2", "Наличие разметки", "8 000+\nподтверждённых\nтранзитов в Kepler", MID,
            "Большой эталонный набор готов"),
        ("3", "Затраты GPU", "CPU 7 дней\nили A100 4 часа", TEAL,
            "A100 окупается уже на одном запуске"),
        ("4", "Базовая AUC", "BLS (Kovács 2002)\n→ 78% базовый уровень", MID,
            "Любая модель должна обогнать"),
        ("5", "Валидация на отложенной", "1 595\nвысокоуверенных", GOLD,
            "Pre-trained CNN дообучить лучше"),
    ]
    card_w = 2.42
    gap = 0.05
    x0 = 0.5
    y_card = 2.4
    for i, (num, title, desc, color, learn) in enumerate(steps):
        x = x0 + i * (card_w + gap)
        rounded_box(slide, x, y_card, card_w, 3.5, fill=SURFACE, stroke=color, stroke_w=2)
        # Number circle
        circle(slide, x + (card_w - 0.65) / 2, y_card + 0.15, 0.65, 0.65, fill=color)
        text_box(slide, x, y_card + 0.15, card_w, 0.65, num,
                 size=24, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        # Title
        text_box(slide, x + 0.1, y_card + 0.95, card_w - 0.2, 0.35, title,
                 size=12, bold=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
        # Desc
        multiline_box(slide, x + 0.1, y_card + 1.4, card_w - 0.2, 0.95, [
            (desc, {"size": 10, "color": MID, "italic": True}),
        ], align=PP_ALIGN.CENTER, line_spacing=1.2)
        # Lesson
        text_box(slide, x + 0.1, y_card + 2.4, card_w - 0.2, 1.0, learn,
                 size=9, color=DEEP, align=PP_ALIGN.CENTER, italic=True,
                 anchor=MSO_ANCHOR.TOP)

    # Bottom takeaway
    rounded_box(slide, 0.5, 6.05, 12.33, 0.6, fill=GOLD_TINT, stroke=GOLD, stroke_w=2)
    text_box(slide, 0.7, 6.1, 12.03, 0.5,
             "Универсальная рамка для любой задачи Analyse-фазы. Применима за пределами астрономии — везде, где есть размеченный базовый уровень.",
             size=13, bold=True, color=DEEP, italic=True, anchor=MSO_ANCHOR.MIDDLE)

    attribution(slide, "Источники: Shallue & Vanderburg ApJ 2018 · Huang & Jiang arxiv 2512.00967 (2025)",
                y=6.95)

    add_notes(slide, "WE-TESS — наш второй разобранный пример. Это универсальная рамка ML-развёртывания в Analyse-фазе. Применима за пределами астрономии.\n\nКонтекст. Команда астрономов хочет автоматически обнаруживать экзопланеты в light curves TESS. Это уже работающая задача — Shallue & Vanderburg показали 89% AUC в 2018 году. Вопрос: какая модель и какие шаги.\n\nШаг 1 — пересечение данных. Совпадают ли распределения TESS и Kepler? У них разные звёзды-цели, разные кадении наблюдений (30 минут vs 2 минуты), но спектральный диапазон похож. Можно делать pre-train на Kepler и дообучать на TESS. Это transfer learning (перенос обучения), проверенная техника.\n\nШаг 2 — наличие разметки. Доступны ли размеченные данные? Да. Kepler оставил 8 000+ подтверждённых транзитов с независимой валидацией через радиовелосиметрию. Это большой обучающий набор.\n\nШаг 3 — затраты GPU vs CPU. На CPU тренировка занимает 7 дней; на A100 — 4 часа. A100 окупается уже на одном запуске. Выбираем GPU.\n\nШаг 4 — базовая AUC. Какая модель уже работает? BLS алгоритм Kovács 2002 — 78% AUC. Это базовый уровень, который надо обогнать. Любая модель ниже — провал.\n\nШаг 5 — валидация на отложенной выборке. После тренировки тестируем на полностью отдельных TESS surveys, которых модель не видела. 1 595 высокоуверенных кандидатов. Точность 83,9% на тестовой выборке.\n\nИтоговый выбор: pre-trained CNN на Kepler, дообученный на TESS. Лучшее соотношение стоимости и качества по сравнению с custom CNN с нуля.\n\nЭта пятишаговая рамка применима к любой задаче Analyse-фазы. Замените «TESS» на ваш домен, «Kepler» на близкий уже-размеченный домен, «BLS Kovács 2002» на классический baseline вашей области. Шаги те же.\n\nГлавный урок: ML-развёртывание в науке — это инженерия, не магия. Существуют отработанные методы, baseline'ы, validation практики. Используйте их.")
