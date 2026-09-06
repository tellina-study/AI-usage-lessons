"""Лекция 5 — Band 2 (Раздел 2 Design s14-s20 + Раздел 3 Build/Launch s21-s27,
плюс ELI5-обзоры s14b, s21b).

Palette Ocean LOCKED, motif «Ocean rounded box», Gold >=1x/slide.
NO timing / NO methodology / NO English phase labels / NO photo-attribution on
visible layer. Memes: real imgflip templates via assets/memes; real photos via
assets/screenshots. Sources -> speaker notes only.
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
# Раздел 2. Design / прототип
# ============================================================
def s14(p):
    return build_section_divider(
        p, here_idx=2,
        subtitle="Дизайн — гипотеза становится артефактом",
        bridge="Как гипотеза из исследования превращается в конкретный "
               "артефакт, который можно показать человеку. Здесь же "
               "закладывается безопасность — в дизайн-брифе, а не патчем после "
               "того, как что-то пошло не так.",
        sid="s14", tag="2 базы · 2 провала",
        meme_name="s14-drake.jpg")


def s14b(p):
    return eli5_overview(
        p, "s14b", title="Дизайн простыми словами", icon_name="pencil",
        cards=[
            ("Что это",
             "Гипотеза становится дешёвым черновиком: наброском экрана, "
             "кликабельным прототипом — тем, что можно показать человеку."),
            ("Зачем",
             "Черновик не жалко выбросить. Понять «не работает» на бумаге — "
             "копейки; понять то же самое после релиза — очень дорого."),
            ("Ментальная модель",
             "Два ромба: сначала ищем правильную проблему, потом правильное "
             "решение. Частая ошибка — прыгнуть сразу к решению."),
        ])


def s15(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Два алмаза: сначала правильная проблема, потом правильное решение",
                size=22, w=12.2, h=0.85)
    # two diamonds
    def diamond(cx, top_lbl, bot_lbl, col):
        y0, dw, dh = 2.05, 2.7, 2.0
        pts = [(cx, y0), (cx + dw / 2, y0 + dh / 2), (cx, y0 + dh),
               (cx - dw / 2, y0 + dh / 2)]
        # draw as a rounded box tilted look — approximate with a filled diamond
        sh = s.shapes.add_shape(MSO_SHAPE.DIAMOND, Inches(cx - dw / 2),
                                Inches(y0), Inches(dw), Inches(dh))
        sh.fill.solid(); sh.fill.fore_color.rgb = SURFACE
        sh.line.color.rgb = col; sh.line.width = Pt(1.8)
        from _helpers import disable_shadow
        disable_shadow(sh)
        text_box(s, x=cx - dw / 2 + 0.2, y=y0 + 0.30, w=dw - 0.4, h=0.4,
                 text=top_lbl, size=12.5, bold=True, color=col,
                 align=PP_ALIGN.CENTER)
        text_box(s, x=cx - dw / 2 + 0.2, y=y0 + dh - 0.70, w=dw - 0.4, h=0.4,
                 text=bot_lbl, size=12.5, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER)
    diamond(3.35, "Расширяем\nпроблему", "Сужаем:\nодна проблема", MID)
    diamond(7.65, "Расширяем\nрешение", "Сужаем:\nодно решение", TEAL)
    text_box(s, x=1.90, y=1.62, w=3.0, h=0.35, text="Правильная проблема",
             size=13, bold=True, color=MID, align=PP_ALIGN.CENTER)
    text_box(s, x=6.20, y=1.62, w=3.0, h=0.35, text="Правильное решение",
             size=13, bold=True, color=TEAL, align=PP_ALIGN.CENTER)
    right_arrow(s, 5.05, 2.90, 0.55, 0.28, fill=LIGHT)
    text_box(s, x=9.35, y=2.85, w=3.4, h=1.3,
             text="Double Diamond\n(Design Council UK)\n\nDesign Thinking — "
                  "его 5-шаговая версия того же каркаса",
             size=12, color=DEEP, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)
    gold_callout(
        s, 0.55, 4.60, 12.25, 1.35,
        "Частая ошибка: конвергировать на решении, не проверив саму проблему "
        "— перепрыгнуть первый алмаз. Дешёвый прототип нужен именно для того, "
        "чтобы это вскрыть до траты денег на разработку.",
        size=14, bold=True)
    notes_with_sources(s, "s15")
    return s


def s16(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Эвристики Нильсена — линтер для UX, не замена тестированию",
                size=22, w=12.2, h=0.85)
    heur = [
        "Видимость статуса системы",
        "Соответствие языку пользователя",
        "Контроль и свобода (отмена)",
        "Консистентность",
        "Предотвращение ошибок",
    ]
    ocean_box(s, 0.55, 1.55, 6.75, 3.55)
    icon(s, "circle-check", 0.80, 1.75, 0.55, "mid")
    text_box(s, x=1.55, y=1.80, w=5.6, h=0.4, text="Топ-5 из 10 эвристик",
             size=15, bold=True, color=MID)
    for i, h in enumerate(heur):
        y = 2.45 + i * 0.50
        chip(s, 0.80, y, 0.42, 0.34, str(i + 1), fill=GOLD, color=DEEP, size=12)
        text_box(s, x=1.40, y=y - 0.02, w=5.6, h=0.4, text=h, size=13,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    # right: design system as guardrail
    ocean_box(s, 7.55, 1.55, 5.25, 1.90, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.6)
    icon(s, "shield-check", 7.80, 1.78, 0.55, "teal")
    text_box(s, x=8.50, y=1.82, w=4.1, h=0.4, text="Дизайн-система = guardrail",
             size=14, bold=True, color=TEAL)
    text_box(s, x=7.80, y=2.45, w=4.8, h=0.9,
             text="Удерживает генеративную свободу в рамках "
                  "провалидированного бренда.",
             size=12.5, color=DEEP, line_spacing=1.15)
    gold_callout(
        s, 7.55, 3.65, 5.25, 1.45,
        "Метафора: эвристики — как линтер для интерфейса. Ловят типовые "
        "проблемы до траты денег на исследование — но не заменяют тест на "
        "живом пользователе.",
        size=12.5, bold=True)
    notes_with_sources(s, "s16")
    return s


def s17(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "AI для дивергенции, человек для конвергенции",
                size=24, w=12.2, h=0.85)
    # funnel: 2-4 AI directions -> 1 human-refined
    ocean_box(s, 0.55, 1.60, 6.55, 3.05, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=0.80, y=1.72, w=6.0, h=0.4, text="Генерация направлений",
             size=13.5, bold=True, color=MID)
    for i in range(4):
        x = 0.85 + i * 1.55
        filled_rect(s, x, 2.25, 1.30, 0.95, WHITE, stroke=LIGHT, stroke_pt=1.2,
                    radius=True, radius_adj=0.10)
        icon(s, "monitor-smartphone", x + 0.42, 2.42, 0.45, "light")
        text_box(s, x=x, y=3.02, w=1.30, h=0.25, text=f"вариант {i+1}",
                 size=9.5, color=SLATE, align=PP_ALIGN.CENTER)
    right_arrow(s, 3.05, 3.55, 1.0, 0.30, fill=GOLD)
    filled_rect(s, 2.55, 3.95, 2.0, 0.55, GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.12)
    text_box(s, x=2.55, y=4.02, w=2.0, h=0.4, text="1 доработанное",
             size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    # right: tools
    ocean_box(s, 7.35, 1.60, 5.45, 3.05, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.5)
    text_box(s, x=7.60, y=1.72, w=5.0, h=0.4, text="Инструменты 2025–26",
             size=13.5, bold=True, color=TEAL)
    text_box(s, x=7.60, y=2.20, w=5.0, h=0.5,
             text="v0 (Vercel) · Figma Make · Google Stitch · bolt.new",
             size=12.5, color=DEEP, line_spacing=1.15)
    text_box(s, x=7.60, y=2.95, w=5.0, h=1.5,
             text="• 2–4 направления за минуты (было — день ручного "
                  "вайрфрейминга)\n• Figma Make подтягивает собственные "
                  "компоненты команды — меньше переделки",
             size=12, color=DEEP, line_spacing=1.18)
    gold_callout(
        s, 0.55, 4.85, 12.25, 1.05,
        "Конвергенция требует суждения о конкретном контексте, которого нет в "
        "обучающих данных: AI расширяет пространство вариантов, а выбор и "
        "проверку на живом пользователе оставляем человеку.",
        size=13, bold=True)
    notes_with_sources(s, "s17")
    return s


def s18(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "29% соответствие WCAG на 21 880 оценках — платформа важнее промпта",
                size=21, w=12.3, h=0.85)
    # left: real WCAG donut chart
    ocean_box(s, 0.55, 1.55, 4.85, 3.55, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    add_image(s, CHARTS / "c-wcag-29.png", 0.85, 1.75, 4.25, 3.15,
              preserve_aspect=True)
    # right: pigeon meme + facts
    meme_in_box(s, "s18-pigeon.jpg", 5.65, 1.55, 3.55, 3.55, pad=0.12)
    ocean_box(s, 9.45, 1.55, 3.35, 3.55, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=9.68, y=1.70, w=2.9, h=1.4,
             text="21 880 оценок WCAG на AI-интерфейсах:\n\n• контраст 26,8%\n"
                  "• использование цвета 19,2%",
             size=11.5, color=DEEP, line_spacing=1.2)
    text_box(s, x=9.68, y=3.35, w=2.9, h=1.6,
             text="«Сделай доступным» в промпте не гарантирует результат — "
                  "решают дефолты платформы, а не текст запроса.",
             size=11.5, italic=True, color=SLATE, line_spacing=1.18)
    gold_callout(
        s, 0.55, 5.30, 12.25, 0.80,
        "Дизайн для НЕДЕТЕРМИНИРОВАННОГО вывода: тот же ввод → разный вывод → "
        "ломает эвристику консистентности; нужны человеко-контрольные точки.",
        size=13, bold=True)
    notes_with_sources(s, "s18")
    return s


def s19(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Защита появилась почти через два года после запуска — уже после трагедии",
                size=21, w=12.3, h=0.85)
    # left: clown meme (retrofit)
    meme_in_box(s, "s19-clown.jpg", 0.55, 1.55, 3.75, 4.30, pad=0.14)
    # right: real logo + timeline + facts
    photo_in_box(s, "s19-characterai-real-source.png", 4.55, 1.55, 3.15, 1.45,
                 pad=0.20)
    ocean_box(s, 7.90, 1.55, 4.90, 1.45, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=8.15, y=1.62, w=4.4, h=0.34, text="Character.AI",
             size=14, bold=True, color=MID)
    text_box(s, x=8.15, y=2.02, w=4.4, h=0.9,
             text="14-летний пользователь погиб после месяцев общения с "
                  "AI-персонажем (02.2024).",
             size=12, color=DEEP, line_spacing=1.15)
    # timeline strip
    stages = ["Запуск", "Трагедия\n02.2024", "Иск\n10.2024", "Защита\n11.2025"]
    xs = [4.85, 6.85, 8.85, 10.85]
    for i, (st, x) in enumerate(zip(stages, xs)):
        col = GOLD if i == 3 else LIGHT
        circle(s, x, 3.55, 0.30, col, stroke=WHITE, stroke_pt=1.5)
        text_box(s, x=x - 0.55, y=3.95, w=1.40, h=0.5, text=st, size=10,
                 bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=0.9)
        if i < 3:
            connector(s, x + 0.30, 3.70, xs[i + 1], 3.70, color=SOFT_GREY,
                      width=2.0)
    gold_callout(
        s, 4.55, 4.75, 8.25, 1.10,
        "Корень — не рантайм-баг, а отсутствующее требование в дизайн-брифе: "
        "MVP оптимизировал вовлечённость без вопроса «кто может пострадать». "
        "Критерий: защита уязвимых — в MVP, а не патчем после трагедии.",
        size=12.5, bold=True)
    notes_with_sources(s, "s19")
    return s


def s20(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Найдено случайно: та же анкета с другой датой рождения — мгновенное приглашение",
                size=19, w=12.3, h=0.85)
    # left: hard-coded filter concept
    ocean_box(s, 0.55, 1.60, 6.05, 3.35, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    icon(s, "cog", 1.05, 1.95, 0.9, "mid")
    text_box(s, x=2.20, y=2.05, w=4.1, h=0.75,
             text="Фильтр с жёстко зашитым правилом «дата рождения»",
             size=13, bold=True, color=DEEP, line_spacing=1.1)
    filled_rect(s, 0.90, 3.05, 5.35, 0.80, GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.08)
    text_box(s, x=1.15, y=3.15, w=4.9, h=0.62,
             text="Женщины 55+ / мужчины 60+ → автоотказ",
             size=13, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.90, y=4.00, w=5.4, h=0.8,
             text="Обнаружено случайно: переподача той же анкеты с другой "
                  "датой рождения → мгновенное приглашение.",
             size=12, italic=True, color=SLATE, line_spacing=1.15)
    # right: EEOC
    ocean_box(s, 6.85, 1.60, 5.95, 1.55, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.8)
    icon(s, "scale", 7.10, 1.85, 0.6, "gold")
    text_box(s, x=7.85, y=1.85, w=4.7, h=0.55, text="$365 000",
             size=24, bold=True, color=DEEP)
    text_box(s, x=7.10, y=2.55, w=5.5, h=0.5,
             text="EEOC, 9 авг. 2023 — первое урегулирование по AI-дискриминации",
             size=11.5, italic=True, color=SLATE, line_spacing=1.1)
    gold_callout(
        s, 6.85, 3.35, 5.95, 1.60,
        "Контраст с Character.AI: там дизайн НЕ заложил защиту; здесь дизайн "
        "ЗАЛОЖИЛ конкретное вредное правило. Критерий: автоматизация решения о "
        "людях → аудит признаков на дискриминацию ДО релиза.",
        size=12.5, bold=True)
    notes_with_sources(s, "s20")
    return s


# ============================================================
# Раздел 3. Build / Launch
# ============================================================
def s21(p):
    return build_section_divider(
        p, here_idx=3,
        subtitle="Сборка и запуск — схлопнутая стрелка",
        bridge="Здесь AI меняет больше всего — стоимость самого написания "
               "кода. Но раздел начинается не с этого факта, а с классической "
               "дисциплины релиза: как выкатывать безопасно и когда "
               "остановиться.",
        sid="s21", tag="2 базы · 2 провала",
        meme_name="s21-expanding-brain.jpg")


def s21b(p):
    return eli5_overview(
        p, "s21b", title="Сборка и запуск простыми словами", icon_name="sliders-horizontal",
        cards=[
            ("Что это",
             "Артефакт становится работающим продуктом у пользователей. AI "
             "сделал само написание кода почти бесплатным."),
            ("Зачем механика запуска",
             "Раз строить дёшево — цена ошибки теперь не «написать», а "
             "«выкатить не то на всех сразу». Нужно включать понемногу и "
             "быстро откатывать."),
            ("Ментальная модель",
             "Запуск — это кран, а не рубильник: 1% → 10% → 100%, следим за "
             "реакцией. И держим наготове решение «убить», а не «дорабатывать "
             "вечно»."),
        ])


def s22(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Та же механика — но здесь решение убить продукт, а не флаг переключить",
                size=20, w=12.3, h=0.85)
    # flow of primitives
    prim = ["Feature flag", "Canary", "Staged rollout", "Rollback"]
    gloss = ["переключатель", "канарейка", "поэтапно", "откат"]
    cw, gap = 2.72, 0.28
    x0, y0 = 0.55, 1.70
    for i, (pr, gl) in enumerate(zip(prim, gloss)):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 1.15, fill=SURFACE, stroke=MID, stroke_pt=1.4)
        text_box(s, x=x + 0.10, y=y0 + 0.20, w=cw - 0.20, h=0.4, text=pr,
                 size=13.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x=x + 0.10, y=y0 + 0.68, w=cw - 0.20, h=0.34, text=gl,
                 size=10.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
        if i < 3:
            right_arrow(s, x + cw + 0.02, y0 + 0.44, gap - 0.04, 0.26,
                        fill=LIGHT)
    text_box(s, x=0.55, y=2.98, w=12.25, h=0.35,
             text="Эти примитивы вы знаете из инженерной раскатки (CI/CD)",
             size=12.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    # new content card
    ocean_box(s, 1.55, 3.65, 10.25, 1.30, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.6)
    icon(s, "scale", 1.80, 3.95, 0.55, "gold")
    text_box(s, x=2.55, y=3.78, w=9.0, h=1.05,
             text="НОВОЕ здесь — чьё и по каким критериям решение они "
                  "обслуживают: MVP (Райс) = обучение, не отгрузка. "
                  "Stage-Gate go/kill (Купер) — «воронка, не туннель»: пороги "
                  "провала записаны числом заранее.",
             size=12.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.15)
    gold_callout(
        s, 0.55, 5.25, 12.25, 0.85,
        "Общий смысл: скорость запуска покупается ограниченным «радиусом "
        "поражения» — сколько пользователей задето, если новое окажется плохим.",
        size=13, bold=True)
    notes_with_sources(s, "s22")
    return s


def s23(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "+200% кода на инженера — но лишь 16% PR получили содержательное ревью",
                size=20, w=12.3, h=0.85)
    # left: real contrast chart
    ocean_box(s, 0.55, 1.55, 6.15, 3.55, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    add_image(s, CHARTS / "c-review-bottleneck.png", 0.80, 1.80, 5.65, 3.05,
              preserve_aspect=True)
    # right: facts
    ocean_box(s, 6.95, 1.55, 5.85, 3.55, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=7.20, y=1.72, w=5.4, h=0.4, text="Измерение Anthropic",
             size=14, bold=True, color=MID)
    text_box(s, x=7.20, y=2.25, w=5.4, h=2.6,
             text="• Реализация: недели/месяцы → минуты агентного исполнения\n\n"
                  "• Объём кода на инженера: +200% год к году\n\n"
                  "• Содержательное человеческое ревью до слияния: лишь ~16% PR",
             size=13, color=DEEP, line_spacing=1.25)
    gold_callout(
        s, 0.55, 5.30, 12.25, 0.80,
        "Дефицитный ресурс сместился к двум человеческим концам: точность "
        "намерения на входе и качество суждения на выходе — узкое место теперь "
        "ревью, а не написание.",
        size=13, bold=True)
    notes_with_sources(s, "s23")
    return s


def s24(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Запуск — это не «включить», а передача контроля по ступеням",
                size=22, w=12.3, h=0.85)
    # ladder of 3 steps
    steps = [
        ("v1", "Высокий контроль / низкая агентность", "маршрутизирует"),
        ("v2", "Предлагает решения на утверждение человека", "человек в петле"),
        ("v3", "Автоматически, с возвратом к человеку", "заслужено трассами"),
    ]
    for i, (v, head, sub) in enumerate(steps):
        y = 4.25 - i * 0.95
        w = 5.5 + i * 0.9
        col = [LIGHT, MID, GOLD][i]
        filled_rect(s, 0.70, y, w, 0.80, SURFACE, stroke=col, stroke_pt=1.6,
                    radius=True, radius_adj=0.08)
        chip(s, 0.90, y + 0.22, 0.75, 0.36, v, fill=col, color=WHITE, size=13)
        text_box(s, x=1.80, y=y + 0.10, w=w - 1.2, h=0.4, text=head, size=12.5,
                 bold=True, color=DEEP)
        text_box(s, x=1.80, y=y + 0.46, w=w - 1.2, h=0.3, text=sub, size=10.5,
                 italic=True, color=SLATE)
    # right explainer
    ocean_box(s, 7.75, 1.55, 5.05, 3.05, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.5)
    text_box(s, x=8.00, y=1.70, w=4.6, h=0.9, text="CC/CD против привычного CI/CD",
             size=14, bold=True, color=TEAL, line_spacing=1.1)
    text_box(s, x=8.00, y=2.55, w=4.6, h=1.9,
             text="CC/CD — Continuous Calibration/Development (непрерывная "
                  "калибровка). Релиз версионируется по уровню агентности, а "
                  "не по набору функций. Лестница агентности: Copilot, Cursor.",
             size=12.5, color=DEEP, line_spacing=1.2)
    gold_callout(
        s, 0.70, 5.05, 12.10, 0.95,
        "«Если не тестировали при высоком контроле — не готовы давать высокую "
        "агентность»: автономию агент заслуживает трассами исполнения, а не "
        "сразу по умолчанию.",
        size=13, bold=True)
    notes_with_sources(s, "s24")
    return s


def s25(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Удвоив скорость генерации, вы удваиваете очередь на ревью — не пропускную способность",
                size=19, w=12.3, h=0.85)
    # tilted scales metaphor
    ocean_box(s, 0.55, 1.60, 6.55, 3.40, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    icon(s, "scale", 3.15, 1.85, 1.1, "mid")
    filled_rect(s, 0.95, 3.25, 2.65, 0.80, GOLD_TINT, stroke=GOLD, stroke_pt=1.4,
                radius=True, radius_adj=0.10)
    text_box(s, x=1.05, y=3.35, w=2.45, h=0.6, text="генерация\nдёшево и быстро",
             size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             line_spacing=1.0, anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, 4.05, 3.25, 2.65, 0.80, SOFT_GREY, stroke=LIGHT, stroke_pt=1.4,
                radius=True, radius_adj=0.10)
    text_box(s, x=4.15, y=3.35, w=2.45, h=0.6, text="верификация\nне ускорилась",
             size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             line_spacing=1.0, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.95, y=4.20, w=5.7, h=0.7,
             text="Сгенерировать правдоподобный код — секунды; проверить его — "
                  "не ускорилось.",
             size=12, italic=True, color=SLATE, line_spacing=1.12)
    # right: 70% problem
    ocean_box(s, 7.35, 1.60, 5.45, 3.40, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    text_box(s, x=7.60, y=1.75, w=5.0, h=0.4, text="Проблема 70%",
             size=14, bold=True, color=TEAL)
    text_box(s, x=7.60, y=2.30, w=5.0, h=2.4,
             text="Опытный разработчик переосмысливает AI-вывод и тратит время "
                  "на переделку.\n\nНовичок отправляет «карточный домик кода», "
                  "который выглядит правдоподобно, но рассыпается под "
                  "нагрузкой.",
             size=12.5, color=DEEP, line_spacing=1.25)
    gold_callout(
        s, 0.55, 5.15, 12.25, 0.85,
        "Отгрузка без eval-гейта или плана отката — это не скорость, это "
        "отложенная цена: ревью не масштабируется вместе с генерацией.",
        size=13, bold=True)
    notes_with_sources(s, "s25")
    return s


def s26(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "0% → 100% одним шагом — минуя канареечную раскатку целиком",
                size=21, w=12.3, h=0.85)
    # left: balloon meme
    meme_in_box(s, "s26-balloon.jpg", 0.55, 1.55, 3.55, 4.30, pad=0.14)
    # right: real logo + staged vs direct
    photo_in_box(s, "s26-google-real-source.png", 4.35, 1.55, 3.05, 1.35,
                 pad=0.24)
    ocean_box(s, 7.65, 1.55, 5.15, 1.35, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=7.90, y=1.62, w=4.65, h=0.34, text="Google AI Overviews, май 2024",
             size=13, bold=True, color=MID)
    text_box(s, x=7.90, y=2.00, w=4.65, h=0.85,
             text="Раскатан на 100% поиска США одним шагом. Без eval-гейта. "
                  "Отключить пользователю нельзя.",
             size=11.5, color=DEEP, line_spacing=1.15)
    # staged bar
    stages = ["1%", "10%", "25%", "50%", "100%"]
    for i, st in enumerate(stages):
        x = 4.45 + i * 1.65
        col = SOFT_GREY if i < 4 else GOLD_TINT
        filled_rect(s, x, 3.30, 1.45, 0.60, col, stroke=LIGHT, stroke_pt=1.2,
                    radius=True, radius_adj=0.14)
        text_box(s, x=x, y=3.38, w=1.45, h=0.44, text=st, size=13, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER)
        if i < 4:
            right_arrow(s, x + 1.47, 3.48, 0.16, 0.24, fill=LIGHT)
    text_box(s, x=4.45, y=4.00, w=8.35, h=0.4,
             text="правильная канареечная раскатка (перепрыгнута)",
             size=11.5, italic=True, color=SLATE)
    gold_callout(
        s, 4.35, 4.65, 8.45, 1.20,
        "На 1% трафика паттерн («ешьте камни» — сатира The Onion; «клей на "
        "пиццу» — шутка на Reddit) всплыл бы за дни во внутреннем мониторинге. "
        "Вместо этого — публичное осмеяние сразу на 100% аудитории.",
        size=12.5, bold=True)
    notes_with_sources(s, "s26")
    return s


def s27(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "2,5–3 года на 0,7% сети — и решение остановиться было правильным",
                size=20, w=12.3, h=0.85)
    # left: real logo + tiny segment
    photo_in_box(s, "s27-mcdonalds-real-source.png", 0.55, 1.60, 3.05, 1.55,
                 pad=0.22)
    ocean_box(s, 0.55, 3.30, 3.05, 2.10, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=0.80, y=3.45, w=2.55, h=0.9, text="0,7%",
             size=40, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(s, x=0.70, y=4.45, w=2.75, h=0.85,
             text="~100 из ≈13 786 ресторанов США",
             size=11.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER,
             line_spacing=1.1)
    # right: facts
    ocean_box(s, 3.85, 1.60, 8.95, 3.05, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=4.15, y=1.75, w=8.4, h=0.4, text="McDonald's × IBM — голосовой приём заказов",
             size=14, bold=True, color=MID)
    text_box(s, x=4.15, y=2.30, w=8.4, h=2.2,
             text="• 2,5–3 года пилота на 0,7% сети\n\n"
                  "• Вирусные провалы: бекон в мороженом, 9 чаёв вместо одного\n\n"
                  "• Закрыт июнь 2024 — цель (голосовая автоматизация) "
                  "осталась, вендорский подход убит",
             size=13, color=DEEP, line_spacing=1.25)
    gold_callout(
        s, 3.85, 4.80, 8.95, 1.05,
        "Зеркало предыдущего кейса: там пропустили пилот целиком и выкатили на "
        "всех; здесь пилот был долгим — и его сигнал использовали правильно, "
        "приняв дисциплинированное решение «убить», а не масштабировать провал.",
        size=12.5, bold=True)
    notes_with_sources(s, "s27")
    return s
