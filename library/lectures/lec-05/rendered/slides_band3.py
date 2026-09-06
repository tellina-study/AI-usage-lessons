"""Лекция 5 — Band 3 (Раздел 4 Measure s28-s35 + Раздел 5 Support s36-s43,
плюс ELI5-обзоры s28b, s36b).

Palette Ocean LOCKED, motif «Ocean rounded box», Gold >=1x/slide.
NO timing / NO methodology / NO English phase labels / NO photo-attribution.
"""
from _helpers import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    right_arrow, circle, chip, connector, icon, slide_title,
    gold_callout, teal_callout, notes_with_sources, build_section_divider,
    eli5_overview, meme_in_box, photo_in_box, add_image,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE, COVER_OUTLINE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, CHARTS,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt


# ============================================================
# Раздел 4. Measure / Experiment
# ============================================================
def s28(p):
    return build_section_divider(
        p, here_idx=4,
        subtitle="Измерение — стрелка, которой ИИ снизил доверие",
        bridge="Измерение — то место, где «выглядит хорошо» бьёт по продукту "
               "сильнее всего. Формальную дисциплину продуктового эксперимента "
               "многие видят впервые.",
        sid="s28", tag="2 базы · 2 провала",
        meme_name="s28-woman-yelling-cat.jpg")


def s28b(p):
    return eli5_overview(
        p, "s28b", title="Измерение простыми словами", icon_name="ruler",
        cards=[
            ("Что это",
             "Фаза, где вы честно проверяете: сработало изменение или только "
             "кажется. Формальную дисциплину эксперимента многие видят впервые."),
            ("Зачем",
             "«Метрика выросла после релиза» ничего не доказывает — она могла "
             "вырасти сама. Нужен способ отделить причину от совпадения."),
            ("Ментальная модель",
             "Делим пользователей на две случайные группы: одной — новое, "
             "другой — старое. Разница и есть настоящий эффект. Метрику успеха "
             "фиксируем заранее."),
        ])


def s29(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Рандомизация отличает причину от совпадения",
                size=23, w=12.3, h=0.85)
    # two groups split by coin
    ocean_box(s, 0.55, 1.60, 5.35, 3.05, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    circle(s, 2.85, 1.80, 0.55, GOLD_TINT, stroke=GOLD, stroke_pt=1.6)
    icon(s, "circle-help", 2.98, 1.93, 0.30, "gold")
    text_box(s, x=1.55, y=2.45, w=3.0, h=0.3, text="случайное деление",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    for j, (lbl, col, xx) in enumerate([("Контроль", LIGHT, 0.90),
                                        ("Воздействие", TEAL, 3.55)]):
        filled_rect(s, xx, 2.85, 1.45, 1.55, SURFACE, stroke=col, stroke_pt=1.6,
                    radius=True, radius_adj=0.08)
        icon(s, "users", xx + 0.45, 3.05, 0.55, "mid" if j == 0 else "teal")
        text_box(s, x=xx, y=3.75, w=1.45, h=0.4, text=lbl, size=12.5, bold=True,
                 color=col, align=PP_ALIGN.CENTER)
    right_arrow(s, 2.55, 3.45, 0.9, 0.28, fill=LIGHT)
    # right: OEC
    ocean_box(s, 6.15, 1.60, 6.65, 3.05, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    text_box(s, x=6.40, y=1.75, w=6.2, h=0.4,
             text="OEC — метрика, о значении которой договорились заранее",
             size=13.5, bold=True, color=TEAL, line_spacing=1.05)
    text_box(s, x=6.40, y=2.55, w=6.2, h=1.9,
             text="Контролируемый эксперимент (Кохави): гипотеза с механизмом "
                  "→ рандомизация → заранее определённый размер выборки → "
                  "решение.\n\nУчебная ловушка: «время на сайте поддержки» — "
                  "это хорошо или плохо? Направление метрики надо согласовать "
                  "до теста.",
             size=12.5, color=DEEP, line_spacing=1.2)
    gold_callout(
        s, 0.55, 4.85, 12.25, 0.95,
        "Только случайное деление групп даёт причинность: разница между "
        "Control и Treatment вызвана вашим изменением, а не сезоном, рекламой "
        "или везением.",
        size=13, bold=True)
    notes_with_sources(s, "s29")
    return s


def s30(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Три вопроса ловят все восемь ловушек эксперимента",
                size=22, w=12.3, h=0.85)
    # GATE-B fix #11: (a) explicit sub-cluster grouping label per card (до
    # теста / интерпретация / эффект) so the 3-question structure reads
    # without the lecturer; (b) one extra gloss clause per jargon term (SRM /
    # peeking / Twyman) so a first-time reader can follow the visible layer
    # alone, not just the speaker notes.
    cards = [
        ("до теста", "shield-alert", "Настроен ли тест правильно?",
         "SRM (перекос групп) — доли пользователей в группах не совпали с "
         "планом; размер выборки должен быть зафиксирован заранее, а не "
         "подогнан под результат"),
        ("интерпретация", "search", "Правильно ли читаю результат?",
         "peeking (подглядывание) — досрочная проверка результата: 2 "
         "подглядки ≈2× ложных срабатываний, поэтому решение принимается "
         "только на заранее заданный размер выборки"),
        ("эффект", "triangle-alert", "Реален ли сам эффект?",
         "закон Тваймана: слишком красивая или неожиданная цифра обычно "
         "означает ошибку измерения, а не реальный эффект — сначала "
         "перепроверь методологию, потом радуйся результату"),
    ]
    cw, gap = 3.95, 0.20
    x0, y0 = 0.55, 1.75
    for i, (grp, ic, head, body) in enumerate(cards):
        x = x0 + i * (cw + gap)
        chip(s, x + 0.24, y0 - 0.32, cw - 0.48, 0.28, grp.upper(),
             fill=TEAL_TINT, color=TEAL, size=9.5)
        ocean_box(s, x, y0, cw, 2.85)
        chip(s, x + 0.24, y0 + 0.20, 0.5, 0.4, str(i + 1), fill=GOLD,
             color=DEEP, size=15)
        icon(s, ic, x + cw - 0.85, y0 + 0.18, 0.55, "mid")
        text_box(s, x=x + 0.24, y=y0 + 0.80, w=cw - 0.48, h=0.65, text=head,
                 size=13.5, bold=True, color=DEEP, line_spacing=1.05)
        text_box(s, x=x + 0.24, y=y0 + 1.45, w=cw - 0.48, h=1.30, text=body,
                 size=10, italic=True, color=SLATE, line_spacing=1.14)
    gold_callout(
        s, 0.55, 4.80, 12.25, 1.15,
        "A/B (измерение) — это не то же, что feature flag (раскатка): первое "
        "проверяет эффект, второе управляет доступом. И осторожнее с легендами: "
        "тест Bing ≈$100 млн прироста выручки (Kohavi/Thomke, HBR 2017) — это "
        "НЕ «кнопка за $300 млн» (отдельный кейс юзабилити).",
        size=13, bold=True)
    notes_with_sources(s, "s30")
    return s


def s31(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "pass@k стремится к 100%, pass^k — к 0%: одна вероятность, разный вопрос",
                size=20, w=12.3, h=0.85)
    # left: ladder
    ocean_box(s, 0.55, 1.60, 5.35, 3.35, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=0.80, y=1.72, w=4.9, h=0.4, text="3 уровня оценки (Хусейн)",
             size=13.5, bold=True, color=MID)
    ladder = [
        ("1", "Unit-тесты — быстрые, детерминированные", LIGHT),
        ("2", "Человек + LLM-as-judge (модель-судья)", MID),
        ("3", "A/B — только когда продукт зрел", GOLD),
    ]
    for i, (n, txt, col) in enumerate(ladder):
        y = 2.25 + i * 0.85
        filled_rect(s, 0.80, y, 4.85, 0.70, SURFACE, stroke=col, stroke_pt=1.5,
                    radius=True, radius_adj=0.08)
        chip(s, 0.95, y + 0.18, 0.42, 0.34, n, fill=col, color=WHITE, size=12)
        text_box(s, x=1.50, y=y, w=4.05, h=0.70, text=txt, size=11.5,
                 bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.05)
    # right: real pass@k chart
    ocean_box(s, 6.15, 1.60, 6.65, 3.35, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    add_image(s, CHARTS / "c-passk.png", 6.40, 1.85, 6.15, 2.85,
              preserve_aspect=True)
    gold_callout(
        s, 0.55, 5.10, 12.25, 0.90,
        "pass@k = хотя бы 1 успех из k; pass^k = ВСЕ k успешны. "
        "Промышленная надёжность почти всегда требует pass^k — «юнит-тесты для "
        "агента», где вероятностный вывод ломает привычный «прошёл/не прошёл».",
        size=13, bold=True)
    notes_with_sources(s, "s31")
    return s


def s32(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Лодка кружит в лагуне и набирает очки — но никогда не финиширует",
                size=21, w=12.3, h=0.85)
    ocean_box(s, 0.55, 1.60, 5.85, 3.30, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    icon(s, "repeat", 2.85, 2.00, 1.1, "teal")
    text_box(s, x=0.85, y=3.25, w=5.25, h=1.5,
             text="RL-агент в гонке набрал на 20% больше очков людей — кружа в "
                  "лагуне и собирая бонусы, никогда не пересекая финиш. "
                  "Оптимизировал прокси, а не реальную цель.",
             size=12.5, color=DEEP, line_spacing=1.18)
    ocean_box(s, 6.65, 1.60, 6.15, 3.30, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.6)
    text_box(s, x=6.90, y=1.75, w=5.65, h=0.9,
             text="Закон Гудхарта: когда мера становится целью, она перестаёт "
                  "быть хорошей мерой.",
             size=14, bold=True, color=DEEP, line_spacing=1.12)
    text_box(s, x=6.90, y=2.85, w=5.65, h=1.9,
             text="Anthropic: модель обобщила от угодливости к прямому "
                  "редактированию собственной функции вознаграждения.\n\n"
                  "Что остаётся: OEC-дисциплина, guardrail-метрики, закон "
                  "Тваймана — подозрительно идеальный балл теперь скорее баг, "
                  "чем прорыв.",
             size=12, color=DEEP, line_spacing=1.18)
    gold_callout(
        s, 0.55, 5.10, 12.25, 0.85,
        "Взлом награды (reward hacking): модель находит способ «выиграть» прокси-метрику, не "
        "достигая задуманного результата — поэтому мера и цель нельзя путать.",
        size=13, bold=True)
    notes_with_sources(s, "s32")
    return s


def s33(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Все 5 реакций взвешены одинаково ×5 — не только «гнев»",
                size=21, w=12.3, h=0.85)
    # left: change-my-mind meme
    meme_in_box(s, "s33-change-my-mind.jpg", 0.55, 1.55, 4.35, 3.05, pad=0.12)
    # right: 5 equal reactions + timeline + real logo
    photo_in_box(s, "s33-facebook-real-source.png", 5.15, 1.55, 2.55, 1.15,
                 pad=0.18)
    ocean_box(s, 7.95, 1.55, 4.85, 1.15, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=8.20, y=1.62, w=4.35, h=0.95,
             text="Facebook MSI, январь 2018: love/haha/wow/sad/angry — все "
                  "×5 выше лайка (не только гнев).",
             size=12, color=DEEP, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)
    reacts = ["love", "haha", "wow", "sad", "angry"]
    for i, r in enumerate(reacts):
        x = 5.15 + i * 1.56
        filled_rect(s, x, 2.90, 1.42, 0.85, SURFACE, stroke=LIGHT, stroke_pt=1.3,
                    radius=True, radius_adj=0.12)
        text_box(s, x=x, y=2.98, w=1.42, h=0.34, text=r, size=11.5, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER)
        chip(s, x + 0.46, 3.32, 0.5, 0.32, "×5", fill=GOLD, color=DEEP, size=11)
    gold_callout(
        s, 5.15, 3.95, 7.65, 1.90,
        "Прокси вовлечённости без guardrail на дезинформацию скрывал вред ~2 "
        "года: внутренний guardrail (корреляция гнев ↔ дезинформация) "
        "подтверждён к 2019, вес обнулён в сентябре 2019. Урок: guardrail-"
        "метрику надо измерять с первого дня, а не когда вред уже случился.",
        size=12.5, bold=True)
    notes_with_sources(s, "s33")
    return s


def s34(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Сдал бенчмарк формата A ≠ безопасен в проде формата B",
                size=21, w=12.3, h=0.85)
    # two mini-cases
    ocean_box(s, 0.55, 1.60, 6.05, 2.85, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=0.80, y=1.72, w=5.5, h=0.4, text="Медицина", size=14,
             bold=True, color=MID)
    chip(s, 0.80, 2.20, 2.4, 0.5, "86,5% MedQA", fill=GOLD, color=DEEP,
         size=15)
    text_box(s, x=0.80, y=2.90, w=5.5, h=1.4,
             text="Med-PaLM 2 хорош на бенчмарке вопросов-ответов — но "
                  "клиническая безопасность требует ОТДЕЛЬНОГО adversarial "
                  "(состязательного) safety-набора.",
             size=12.5, color=DEEP, line_spacing=1.2)
    ocean_box(s, 6.75, 1.60, 6.05, 2.85, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    text_box(s, x=7.00, y=1.72, w=5.5, h=0.4, text="Право", size=14,
             bold=True, color=TEAL)
    text_box(s, x=7.00, y=2.20, w=5.5, h=0.9,
             text="Stanford RegLab: Lexis+ 17% галлюцинаций, Westlaw 33% — на "
                  "реальных юридических запросах.",
             size=12.5, color=DEEP, line_spacing=1.18)
    filled_rect(s, 7.00, 3.20, 5.55, 0.95, GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.07)
    text_box(s, x=7.25, y=3.30, w=5.1, h=0.75,
             text="Дело Mata v. Avianca (фейковые цитаты) = ChatGPT, НЕ Harvey "
                  "— частая ошибка атрибуции.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.12)
    gold_callout(
        s, 0.55, 4.65, 12.25, 1.20,
        "Бенчмарк — свидетельство о производительности только на формате "
        "задачи именно этого бенчмарка. Альтернатива: состязательные evals на "
        "реальных краевых случаях того домена, где продукт будет работать.",
        size=13, bold=True)
    notes_with_sources(s, "s34")
    return s


def s35(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "A/B остаётся фундаментом — evals и guardrail-метрики теперь обязательны поверх",
                size=20, w=12.3, h=0.85)
    # layered diagram bottom-aligned
    layers = [
        ("Классический A/B (рандомизация)", 6.55, MID, 4.35),
        ("Оценки: eval (offline + online)", 5.0, TEAL, 3.70),
        ("Guardrail-метрики", 3.6, GOLD, 3.05),
    ]
    for txt, w, col, y in layers:
        cx = 0.55 + (6.55 - w) / 2 + 0.0
        x = 0.55 + (6.9 - w) / 2
        filled_rect(s, x, y, w, 0.62, SURFACE, stroke=col, stroke_pt=1.8,
                    radius=True, radius_adj=0.10)
        text_box(s, x=x, y=y, w=w, h=0.62, text=txt, size=12.5, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.55, y=1.65, w=7.0, h=0.4,
             text="Измерение = стрелка, которой ИИ снизил доверие",
             size=13.5, bold=True, color=MID, align=PP_ALIGN.CENTER)
    ocean_box(s, 7.85, 1.65, 4.95, 3.35, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    text_box(s, x=8.10, y=1.85, w=4.5, h=3.0,
             text="• Рандомизация — по-прежнему то, что даёт причинность, а не "
                  "совпадение.\n\n• Оценки (evals) и guardrail-метрики — новые слои "
                  "поверх, а не замена A/B.\n\n• Центральный навык фазы — "
                  "отличать сигнал от шума.",
             size=13, color=DEEP, line_spacing=1.25)
    gold_callout(
        s, 0.55, 5.20, 12.25, 0.80,
        "Мост в поддержку: тот же навык «сигнал ≠ шум» в эксплуатации означает "
        "заметить дрейф раньше, чем он проявится на дашборде.",
        size=13, bold=True)
    notes_with_sources(s, "s35")
    return s


# ============================================================
# Раздел 5. Support / Operate
# ============================================================
def s36(p):
    return build_section_divider(
        p, here_idx=5,
        subtitle="Поддержка — продукт как оркестр",
        bridge="Между «код работает у меня» и «продукт надёжно работает у "
               "миллионов 24/7» — пропасть, и её закрывают процессом "
               "эксплуатации, а не только качеством кода.",
        sid="s36", tag="2 базы · 3 провала",
        meme_name="s36-disaster-girl.jpg")


def s36b(p):
    return eli5_overview(
        p, "s36b", title="Поддержка простыми словами", icon_name="headphones",
        cards=[
            ("Что это",
             "Продукт уже живёт у людей круглосуточно: его надо наблюдать, "
             "чинить сбои и отвечать на жалобы — годами."),
            ("Зачем",
             "«Работает у меня» и «надёжно работает у миллионов 24/7» — разные "
             "вещи. Разрыв закрывают процессом, а не только чистым кодом."),
            ("Ментальная модель",
             "Заранее договариваемся, сколько сбоев допустимо (бюджет на "
             "ошибки). С ИИ сложнее: модель может «тихо деградировать», пока "
             "графики ещё зелёные."),
        ])


def s37(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Ответ с кодом 200 ничего не говорит о том, галлюцинирует ли модель",
                size=20, w=12.3, h=0.85)
    # flow SLI->SLO->error budget
    flow = [("SLI", "показатель"), ("SLO", "цель 99,9%"),
            ("Error budget", "«1 − SLO»")]
    x0, y0 = 0.55, 1.75
    cw, gap = 3.1, 0.35
    for i, (t, sub) in enumerate(flow):
        x = x0 + i * (cw + gap)
        col = GOLD if i == 2 else MID
        ocean_box(s, x, y0, cw, 1.15, fill=SURFACE, stroke=col, stroke_pt=1.5)
        text_box(s, x=x + 0.10, y=y0 + 0.18, w=cw - 0.2, h=0.4, text=t,
                 size=14, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x=x + 0.10, y=y0 + 0.66, w=cw - 0.2, h=0.34, text=sub,
                 size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
        if i < 2:
            right_arrow(s, x + cw + 0.03, y0 + 0.44, gap - 0.06, 0.26,
                        fill=LIGHT)
    text_box(s, x=0.55, y=3.05, w=11.0, h=0.5,
             text="Error budget = «1 − SLO». Пример: 99,9% → 1000 ошибок на "
                  "1 млн запросов за 4 недели. Изменения — ≈70% всех сбоев.",
             size=12.5, color=DEEP, line_spacing=1.15)
    # struck-through 200
    filled_rect(s, 0.55, 3.75, 12.25, 1.10, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    icon(s, "x", 0.85, 4.00, 0.55, "light")
    text_box(s, x=1.60, y=3.90, w=10.9, h=0.85,
             text="SLI «доля ответов с кодом 200» = всё ок? Нет: 200 приходит "
                  "и когда модель уверенно галлюцинирует. Инфраструктурная "
                  "метрика не видит качества ответа.",
             size=13, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.15)
    gold_callout(
        s, 0.55, 5.05, 12.25, 0.90,
        "Дежурства, разбор инцидентов без поиска виноватых, инструкции — вы "
        "это можете знать. Новое здесь: в проде теперь недетерминированная "
        "модель (следующий слайд).",
        size=13, bold=True)
    notes_with_sources(s, "s37")
    return s


def s38(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Трейсинг ловит дрейф галлюцинаций там, где инфра-мониторинг молчит",
                size=20, w=12.3, h=0.85)
    # caption sits ABOVE the icon row with its own clear band (GATE-B fix:
    # was positioned to overlap the magnifier-icon row below it).
    text_box(s, x=0.65, y=1.30, w=11.5, h=0.35,
             text="Трейсинг (камера над каждым узлом): LangSmith · Langfuse · "
                  "Arize Phoenix · Helicone",
             size=12, italic=True, color=SLATE)
    # request path with cameras
    path = ["промпт", "поиск", "инструменты", "ответ"]
    x0, y0 = 0.65, 2.55
    cw, gap = 2.55, 0.55
    for i, node in enumerate(path):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 0.95, fill=SURFACE, stroke=MID, stroke_pt=1.4)
        text_box(s, x=x, y=y0, w=cw, h=0.95, text=node, size=13, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        icon(s, "search", x + cw / 2 - 0.22, y0 - 0.62, 0.44, "teal")
        if i < 3:
            right_arrow(s, x + cw + 0.05, y0 + 0.35, gap - 0.10, 0.25,
                        fill=LIGHT)
    # LLMOps card + PII warning
    ocean_box(s, 0.55, 3.75, 7.55, 1.15, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=0.80, y=3.85, w=7.05, h=0.95,
             text="LLMOps/AgentOps: дрейф данных vs дрейф концепта · runtime "
                  "guardrails · circuit breaker (предохранитель). Guardian "
                  "Agents (категория Gartner) — агенты, следящие за агентами.",
             size=12, color=DEEP, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, 8.30, 3.75, 4.50, 1.15, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.08)
    icon(s, "lock", 8.55, 3.98, 0.5, "gold")
    text_box(s, x=9.20, y=3.85, w=3.4, h=0.95,
             text="Не отправлять регулируемые PII (перс. данные) во внешний "
                  "трейсинг без анонимизации или self-host.",
             size=11.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.12)
    gold_callout(
        s, 0.55, 5.05, 12.25, 0.90,
        "Инфраструктурный мониторинг видит «сервис жив»; трейсинг видит «ответы "
        "деградируют»: дрейф галлюцинаций, сбои поиска, регрессию промптов.",
        size=13, bold=True)
    notes_with_sources(s, "s38")
    return s


def s39(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Дашборды остаются зелёными, пока доверие уже падает недели",
                size=21, w=12.3, h=0.85)
    # left: harold meme
    meme_in_box(s, "s39-harold.jpg", 0.55, 1.55, 3.35, 4.20, pad=0.14)
    # right: silent drift + governance drift
    ocean_box(s, 4.15, 1.60, 8.65, 1.75, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    icon(s, "monitor-smartphone", 4.40, 1.90, 0.6, "teal")
    text_box(s, x=5.20, y=1.78, w=7.35, h=0.4, text="Тихий дрейф",
             size=15, bold=True, color=TEAL)
    text_box(s, x=5.20, y=2.25, w=7.35, h=1.0,
             text="Самые активные пользователи замечают регрессию раньше "
                  "агрегированных метрик — доверие падает раньше, чем двигаются "
                  "дашборды.",
             size=13, color=DEEP, line_spacing=1.18)
    ocean_box(s, 4.15, 3.50, 8.65, 1.55, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=4.40, y=3.62, w=8.15, h=0.4, text="Дрейф правил",
             size=14, bold=True, color=MID)
    text_box(s, x=4.40, y=4.05, w=8.15, h=0.95,
             text="Guardrails (защитные правила) без версионирования молча "
                  "устаревают: правила расходятся с реальностью незаметно.",
             size=12.5, color=DEEP, line_spacing=1.15)
    gold_callout(
        s, 4.15, 5.20, 8.65, 0.70,
        "Что остаётся: эскалация к человеку, ответственность, инцидент-"
        "дисциплина — усилены автономностью ИИ, не отменены ею.",
        size=12.5, bold=True)
    notes_with_sources(s, "s39")
    return s


def s40(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Модель была откалибрована корректно — не было предохранителя на дрейф в реальном времени",
                size=18, w=12.3, h=0.85)
    # left: real chart + logo
    photo_in_box(s, "s40-zillow-real-source.png", 0.55, 1.60, 3.05, 1.30,
                 pad=0.22)
    ocean_box(s, 0.55, 3.10, 3.05, 2.30, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    icon(s, "triangle-alert", 1.55, 3.30, 0.9, "mid")
    text_box(s, x=0.70, y=4.30, w=2.75, h=1.0,
             text="Рынок сдвинулся — дрейф концепта без предохранителя",
             size=12, italic=True, color=SLATE, align=PP_ALIGN.CENTER,
             line_spacing=1.15)
    # right: chart
    ocean_box(s, 3.85, 1.60, 8.95, 3.80, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    add_image(s, CHARTS / "c-zillow.png", 4.15, 1.85, 8.35, 2.55,
              preserve_aspect=True)
    text_box(s, x=4.15, y=4.45, w=8.35, h=0.85,
             text="Zillow Offers, ноябрь 2021: 9680 домов куплено, 3032 "
                  "продано · ~2000 уволенных (~25% штата) · ≈$80 тыс. убытка на "
                  "объект.",
             size=12, color=DEEP, line_spacing=1.15)
    gold_callout(
        s, 0.55, 5.55, 12.25, 0.62,
        "Критерий: модель, совершающая сделки на деньги, требует мониторинга "
        "точности предсказания в реальном времени с автоматическим "
        "предохранителем (circuit breaker), который отключает её при дрейфе.",
        size=12, bold=True)
    notes_with_sources(s, "s40")
    return s


def s41(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "«Бот — отдельное юрлицо» — трибунал отклонил этот довод одной фразой",
                size=20, w=12.3, h=0.85)
    # left: real photo (aircraft)
    photo_in_box(s, "s41-aircanada-real-source.png", 0.55, 1.60, 5.55, 3.05)
    # right: balanced scales concept + verdict
    ocean_box(s, 6.35, 1.60, 6.45, 1.75, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    icon(s, "scale", 6.60, 1.95, 0.9, "mid")
    text_box(s, x=7.65, y=1.80, w=4.9, h=1.4,
             text="Весы в равновесии: ответ бота = статичная страница сайта. "
                  "Одинаковая ответственность за оба.",
             size=13, bold=True, color=DEEP, line_spacing=1.15,
             anchor=MSO_ANCHOR.MIDDLE)
    ocean_box(s, 6.35, 3.55, 6.45, 1.85, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.6)
    text_box(s, x=6.60, y=3.68, w=5.95, h=0.4, text="Air Canada, чат-бот сайта",
             size=13.5, bold=True, color=DEEP)
    text_box(s, x=6.60, y=4.10, w=5.95, h=1.2,
             text="Бот некорректно сообщил о ретроактивной скидке. Трибунал — "
                  "$812,02 CAD: компания отвечает за ответ бота как за любой "
                  "другой контент сайта.",
             size=12, color=DEEP, line_spacing=1.15)
    gold_callout(
        s, 0.55, 5.55, 12.25, 0.62,
        "Ты владеешь каждым ответом бота — не больше, но и ни на грамм меньше "
        "ответственности, чем за любой другой контент сайта.",
        size=12.5, bold=True)
    notes_with_sources(s, "s41")
    return s


def s42(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "10 из 10 журналистов получили один и тот же незаконный совет — не единичный сбой",
                size=18, w=12.3, h=0.85)
    # left: Klarna chart + logo
    photo_in_box(s, "s42-klarna-real-source.png", 0.55, 1.60, 2.55, 1.15,
                 pad=0.16)
    ocean_box(s, 0.55, 2.90, 5.75, 2.50, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    add_image(s, CHARTS / "c-klarna.png", 0.80, 3.10, 5.25, 2.05,
              preserve_aspect=True)
    text_box(s, x=3.25, y=1.72, w=3.05, h=1.0,
             text="Klarna: политика «только ИИ» откатилась (05.2025) — но "
                  "автоматизация выросла до 853 чел.-эквивалентов (усиление "
                  "людей, не замена).",
             size=11.5, color=DEEP, line_spacing=1.15)
    # right: NYC 10/10
    ocean_box(s, 6.55, 1.60, 6.25, 3.05, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.6)
    text_box(s, x=6.80, y=1.72, w=5.75, h=0.4, text="NYC MyCity — гос-бот",
             size=14, bold=True, color=DEEP)
    for i in range(10):
        col_i = i % 5
        row_i = i // 5
        x = 6.85 + col_i * 1.12
        y = 2.25 + row_i * 0.70
        icon(s, "user-x", x, y, 0.48, "gold")
    text_box(s, x=6.80, y=3.70, w=5.75, h=0.85,
             text="10 из 10 журналистов — один и тот же незаконный совет. Мэр "
                  "не отозвал бот сразу.",
             size=12.5, bold=True, color=DEEP, line_spacing=1.15)
    gold_callout(
        s, 0.55, 5.55, 12.25, 0.62,
        "Урок не «ИИ не работает», а «метрика пропускной способности без "
        "гарантированной эскалации к человеку — неверный дизайн».",
        size=12.5, bold=True)
    notes_with_sources(s, "s42")
    return s


def s43(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Эксплуатация — точка, где петля физически замыкается",
                size=22, w=12.3, h=0.85)
    # loop with highlighted return arrow. GATE-B fix: cy/r shrunk (3.55->3.00,
    # 1.75->1.45) so the bottom "Измерение" node + its label fully clear the
    # gold callout starting at y=5.10 (was overlapping/hidden — same class of
    # bug already fixed on s49's hexagon: shrink+raise the loop).
    import math
    cx, cy, r = 3.65, 3.00, 1.45
    steps = ["Исследование", "Дизайн", "Сборка", "Измерение", "Поддержка",
             "Управление"]
    centers = []
    for i in range(6):
        ang = math.pi / 2 - i * (2 * math.pi / 6)
        centers.append((cx + r * math.cos(ang), cy - r * math.sin(ang)))
    for i in range(6):
        x1, y1 = centers[i]
        x2, y2 = centers[(i + 1) % 6]
        # highlight the Support(4)->Discovery(0) return arrow gold
        gold_edge = (i == 4)
        connector(s, x1, y1, x2, y2, color=(GOLD if gold_edge else LIGHT),
                  width=(3.0 if gold_edge else 1.8))
    for i, (nx, ny) in enumerate(centers):
        col = GOLD if i in (0, 4) else MID
        circle(s, nx - 0.24, ny - 0.24, 0.48, col, stroke=WHITE, stroke_pt=1.4)
        text_box(s, x=nx - 0.85, y=ny + 0.26, w=1.7, h=0.34, text=steps[i],
                 size=9, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    # right
    ocean_box(s, 6.35, 1.65, 6.45, 3.05, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    text_box(s, x=6.60, y=1.82, w=5.95, h=2.7,
             text="Поддержка → Продукт замыкает петлю.\n\nСигнал из эксплуатации"
                  "(дрейф, инцидент, жалоба) обновляет reference dataset "
                  "(эталонный набор) и guardrail — а при глубоком сигнале "
                  "возвращает к самому намерению: что мы строим и для кого.",
             size=13, color=DEEP, line_spacing=1.25)
    gold_callout(
        s, 0.55, 5.10, 12.25, 0.85,
        "Наблюдать, интерпретировать, решать — эти шаги остаются человеческими "
        "на каждом витке петли, даже когда исполнение почти бесплатно.",
        size=13, bold=True)
    notes_with_sources(s, "s43")
    return s
