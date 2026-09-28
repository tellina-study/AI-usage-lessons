"""Лекция 5 — Band 4 (Раздел 6 Governance/финал s44-s49 + ELI5 s44b).

Palette Ocean LOCKED, motif «Ocean rounded box», Gold >=1x/slide.
s49 = hero payoff (>=40% area, замкнутая петля с человеком в центре).
"""
from _helpers import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    right_arrow, circle, chip, connector, icon, slide_title,
    gold_callout, teal_callout, notes_with_sources, refs_of_slide,
    build_section_divider,
    eli5_overview, meme_in_box, photo_in_box, add_image, check_point, src,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE, COVER_OUTLINE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, CHARTS,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt


def s44(p):
    return build_section_divider(
        p, here_idx=6,
        subtitle="Управление — замыкающий раздел: отвечает на парадокс из начала лекции",
        bridge="Почему сборка почти бесплатна, а ценность — нет. Здесь мы "
               "поднимаемся на уровень организации и собираем петлю целиком.",
        sid="s44", tag="1 база · 2 практики · 2 провала",
        meme_name="s44-sad-pablo.jpg")


def s44b(p):
    return eli5_overview(
        p, "s44b", title="Управление простыми словами", icon_name="scale",
        cards=[
            ("Что это",
             "Уровень организации: не «как сделать один продукт», а «во что "
             "вообще вкладывать деньги» — и остановить то, что не окупается."),
            ("Зачем",
             "Ресурсы ограничены. Тот же гейт «продолжать / убить», что и для "
             "одной функции, поднимается на уровень капитала между многими "
             "инициативами."),
            ("Ментальная модель",
             "Воронка портфеля: много идей на входе, немного профинансированных "
             "на выходе. У ИИ-продукта новая переменная — стоимость каждого "
             "запроса против его ценности."),
        ])


def s45(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Тот же go/kill-гейт — но теперь распределяет капитал между многими инициативами",
                size=19, w=12.3, h=0.85)
    # portfolio funnel
    ocean_box(s, 0.55, 1.60, 6.05, 3.55, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=0.80, y=1.72, w=5.5, h=0.4, text="Воронка портфеля",
             size=13.5, bold=True, color=MID)
    # GATE-B fix (audit 2026-09-07): "профинансированы" was wrapping
    # mid-word ("профинансиро-ваны") because the bottom funnel box was
    # narrower than the label needed at this font size. Widened the box
    # (1.7->2.3in) AND shortened the label ("профинансированы" ->
    # "профинансировано") AND dropped its font size slightly so it now
    # fits on one line without truncating any funnel-taper visual logic.
    widths = [5.35, 4.0, 2.6, 2.3]
    labels = ["много инициатив", "гейт 1", "гейт 2", "профинансировано"]
    sizes = [11.5, 11.5, 11.5, 10.5]
    cols = [LIGHT, MID, TEAL, GOLD]
    for i, (w, lb, col, sz) in enumerate(zip(widths, labels, cols, sizes)):
        y = 2.25 + i * 0.68
        x = 0.80 + (5.5 - w) / 2
        filled_rect(s, x, y, w, 0.52, SURFACE, stroke=col, stroke_pt=1.6,
                    radius=True, radius_adj=0.10)
        text_box(s, x=x, y=y, w=w, h=0.52, text=lb, size=sz, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # right: unit economics
    ocean_box(s, 6.85, 1.60, 5.95, 1.85, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    text_box(s, x=7.10, y=1.75, w=5.45, h=0.4, text="Unit-экономика ИИ-продукта",
             size=14, bold=True, color=TEAL)
    text_box(s, x=7.10, y=2.25, w=5.45, h=1.1,
             text="Новая переменная — стоимость на запрос против ценности на "
                  "запрос. Каждое обращение к модели стоит денег.",
             size=12.5, color=DEEP, line_spacing=1.18)
    filled_rect(s, 6.85, 3.65, 5.95, 1.50, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.07)
    text_box(s, x=7.10, y=3.78, w=5.45, h=1.25,
             text="Финансовый KPI на входе в пилот: «снизим стоимость тикета "
                  "с X₽ до Y₽ при CSAT ≥ Z; N тикетов, M недель, владелец — "
                  "Иванов».",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.15)
    gold_callout(
        s, 0.55, 5.35, 12.25, 0.72,
        "Портфельное управление = Stage-Gate, поднятый на уровень капитала: та же "
        "дисциплина «воронка, не туннель», но между продуктами, а не внутри "
        "одного.",
        size=12.5, bold=True)
    notes_with_sources(s, "s45")
    return s


def s46(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Узкое место сместилось с технологии на операционную модель организации",
                size=19, w=12.3, h=0.85)
    # 5 sources converge
    ocean_box(s, 0.55, 1.60, 6.35, 3.55, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    srcs = ["Deloitte", "Сбер", "Gartner", "McKinsey", "Forrester"]
    for i, sname in enumerate(srcs):
        y = 1.85 + i * 0.60
        chip(s, 0.85, y, 1.85, 0.44, sname, fill=LIGHT, color=WHITE, size=12)
        connector(s, 2.75, y + 0.22, 5.05, 2.95, color=SOFT_GREY, width=1.2)
    filled_rect(s, 4.15, 2.55, 2.5, 0.80, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.10)
    text_box(s, x=4.20, y=2.62, w=2.4, h=0.65, text="операционная модель",
             size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    text_box(s, x=0.80, y=4.85, w=5.9, h=0.3,
             text="Deloitte: 75% — модель должна измениться · 42% низкий/нулевой ROI [1]",
             size=11, italic=True, color=SLATE)
    # right: maturity scale
    ocean_box(s, 7.15, 1.60, 5.65, 3.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    text_box(s, x=7.40, y=1.75, w=5.15, h=0.4, text="Зрелость 0–5",
             size=14, bold=True, color=TEAL)
    for i in range(6):
        x = 7.45 + i * 0.85
        cur = (i == 3)
        col = GOLD if cur else SOFT_GREY
        filled_rect(s, x, 2.55, 0.70, 0.70, (GOLD_TINT if cur else SURFACE),
                    stroke=col, stroke_pt=(2.0 if cur else 1.0), radius=True,
                    radius_adj=0.12)
        text_box(s, x=x, y=2.70, w=0.70, h=0.4, text=str(i), size=15,
                 bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, x=7.45, y=3.35, w=2.4, h=0.5, text="Сбер здесь →",
             size=11.5, bold=True, color=DEEP)
    text_box(s, x=7.40, y=3.95, w=5.15, h=1.1,
             text="Операторы → оркестраторы. Сбер сам ставит себя на "
                  "уровень 3 из 5 [2] — сигнал против хайпа: даже крупный игрок не "
                  "заявляет вершину шкалы.",
             size=12, color=DEEP, line_spacing=1.18)
    gold_callout(
        s, 0.55, 5.25, 12.25, 0.72,
        "Пять независимых источников сходятся в одном: выигрывает не тот, у "
        "кого лучше модель, а тот, кто перестроил команды и управление под неё.",
        size=12.5, bold=True)
    check_point(
        s, 0.55, 6.08, 12.25,
        "Вам показывают заголовок «95% ИИ-пилотов провалились». Какой первый "
        "вопрос вы задаёте этой цифре?",
        h=0.80, size=12.5)
    refs_of_slide(s, "s46")
    notes_with_sources(s, "s46")
    return s


def s47(p):
    """GATE-B fix (audit 2026-09-07): this is the single most important
    payoff of the s01 hook's own headline stat ("~95% pilots return nothing")
    — but the funnel chart previously occupied only ~1/3 of the slide,
    competing equally with a MIT campus stock photo and a 4-question
    sidebar. Rebuilt so the 60->20->5 funnel is the unambiguous visual
    dominant (wide top band, ~46% of slide area) with the debunk statement
    directly under it; MIT photo + 4-question checklist demoted to a
    slimmer bottom row. Facts unchanged."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "60% исследовали → 20% пилот → 5% успех: это 25% среди дошедших, не «95% провал» [1]",
                size=18, w=12.3, h=0.72, y=0.28)
    # TOP: the funnel chart is now the dominant visual — full-width, tall
    ocean_box(s, 0.55, 1.20, 12.25, 3.15, fill=SURFACE, stroke=GOLD,
              stroke_pt=2.0)
    add_image(s, CHARTS / "c-mit-funnel.png", 1.35, 1.40, 10.65, 2.75,
              preserve_aspect=True)
    # debunk statement directly under the funnel — the payoff stated in words
    gold_callout(
        s, 0.55, 4.50, 12.25, 0.72,
        "«95% провал» — заголовок, который не переживает калибровку: успех "
        "среди дошедших до пилота — 25%, не 5% [2, 3].",
        size=14, bold=True, align=PP_ALIGN.CENTER)
    # BOTTOM ROW: MIT source photo (small) + 4-question checklist + BCG note
    photo_in_box(s, "s47-mit-real-source.png", 0.55, 5.35, 2.55, 1.55, pad=0.12)
    ocean_box(s, 3.25, 5.35, 5.35, 1.55, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=3.48, y=5.45, w=4.9, h=0.32,
             text="4 вопроса к любой громкой цифре провала ИИ",
             size=11.5, bold=True, color=MID, line_spacing=1.0)
    qs = ["1. Каков знаменатель?", "2. Что считается «провалом»?",
          "3. Каков конфликт интересов автора? [3]",
          "4. Прослеживается ли к первоисточнику?"]
    for i, qq in enumerate(qs):
        text_box(s, x=3.48, y=5.82 + i * 0.27, w=4.9, h=0.26, text=qq,
                 size=10, color=DEEP, line_spacing=1.0)
    filled_rect(s, 8.75, 5.35, 4.05, 1.55, GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.08)
    # ПРАВКА #212 (фактическая): цифра принадлежит BCG AI Radar 2025
    # (январь 2025, выборка 1803), а НЕ сентябрьскому отчёту BCG.
    text_box(s, x=8.95, y=5.45, w=3.65, h=1.35,
             text="BCG AI Radar 2025 (январь 2025, 1803 руководителя): 60% "
                  "компаний не отслеживают ни одного финансового KPI, "
                  "привязанного к ценности ИИ [5].",
             size=10.5, bold=True, color=DEEP, line_spacing=1.15,
             anchor=MSO_ANCHOR.MIDDLE)
    refs_of_slide(s, "s47")
    notes_with_sources(s, "s47")
    return s


def s48(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "«Автономный» магазин: 700 из 1000 транзакций требовали ручной проверки против цели 50",
                size=17, w=12.3, h=0.85)
    # top: Just Walk Out
    photo_in_box(s, "s48-amazon-real-source.png", 0.55, 1.50, 3.35, 1.85)
    ocean_box(s, 4.10, 1.50, 3.55, 1.85, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    add_image(s, CHARTS / "c-jwo.png", 4.30, 1.65, 3.15, 1.55,
              preserve_aspect=True)
    ocean_box(s, 7.85, 1.50, 4.95, 1.85, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.6)
    text_box(s, x=8.10, y=1.62, w=4.45, h=1.65,
             text="Just Walk Out (Amazon), с 2018: 700/1000 транзакций — "
                  "ручная проверка (14× выше цели 50/1000) [1]. 6 лет маркетинга "
                  "«автономный ИИ» без раскрытия масштаба труда (скрытая "
                  "человеческая стоимость) [2].",
             size=11.5, bold=True, color=DEEP, line_spacing=1.15,
             anchor=MSO_ANCHOR.MIDDLE)
    # bottom: 6-phase summary matrix
    phases = [("Исследование", "синтез, кабинет.", "интервью"),
              ("Дизайн", "генерация", "требов. безоп."),
              ("Сборка/запуск", "код ≈ бесплатно", "ревью, kill-гейт"),
              ("Измерение", "оценки (evals)", "рандомизация"),
              ("Поддержка", "трейсинг", "эскалация"),
              ("Управление", "операц. модель", "стоим./запрос")]
    cw = 12.25 / 6
    y0 = 3.65
    # header
    filled_rect(s, 0.55, y0, 12.25, 0.42, MID, radius=True, radius_adj=0.05)
    text_box(s, x=0.55, y=y0, w=12.25, h=0.42, text="Фаза × что ИИ меняет × что остаётся из классики",
             size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    for i, (ph, ai, cl) in enumerate(phases):
        x = 0.55 + i * cw
        ocean_box(s, x + 0.02, y0 + 0.48, cw - 0.04, 1.35, fill=SURFACE,
                  stroke=LIGHT, stroke_pt=1.0)
        text_box(s, x=x + 0.08, y=y0 + 0.56, w=cw - 0.16, h=0.4, text=ph,
                 size=10.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 line_spacing=0.95)
        text_box(s, x=x + 0.08, y=y0 + 1.00, w=cw - 0.16, h=0.34, text=ai,
                 size=9, color=TEAL, align=PP_ALIGN.CENTER, line_spacing=0.95)
        text_box(s, x=x + 0.08, y=y0 + 1.42, w=cw - 0.16, h=0.34, text=cl,
                 size=9, color=SLATE, align=PP_ALIGN.CENTER, line_spacing=0.95)
    refs_of_slide(s, "s48")
    notes_with_sources(s, "s48")
    return s


def s49(p):
    """ПРАВКА #212: слайд разгружен — чек-лист «прежде чем делать фазу
    AI-first» и блок вопросов уехали на новые s54/s55, здесь остаётся только
    keystone-payoff: разрешение парадокса + что изменилось / что осталось
    человеческим. Визуал понижен с hero до обычного Ocean-блока: замыкающий
    hero всей деки теперь на последнем слайде (s55), см. slides/s49-*.md и
    slides/s55-*.md.
    """
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Сборка бесплатна — дефицит теперь: суждение, а не исполнение",
                size=21, w=12.3, h=0.66, y=0.30)

    # РЯД A: реальное фото (обычный визуал, не hero) + разрешение парадокса
    photo_in_box(s, "s49-missioncontrol-crop.png", 0.55, 1.12, 6.25, 1.92,
                 pad=0.09)
    src(s, 0.58, 3.10, 6.25,
        "Центр управления NASA, Apollo 16 — решение принимают люди", size=9.5)

    ocean_box(s, 7.05, 1.12, 5.75, 1.92, fill=SURFACE, stroke=MID,
              stroke_pt=1.5)
    text_box(s, x=7.30, y=1.26, w=5.25, h=0.32,
             text="Разрешение парадокса, с которого начали",
             size=13, bold=True, color=MID)
    text_box(s, x=7.30, y=1.66, w=5.25, h=1.24,
             text="Сборка стала почти бесплатной — правда. Успех редок — тоже "
                  "правда, но точнее: 25% среди дошедших до пилота, а не 5% "
                  "«всех».",
             size=12.5, color=DEEP, line_spacing=1.18)

    # РЯД B: что изменилось / что осталось человеческим
    changed = ["Стоимость сборки", "Скорость исследования",
               "Скорость прототипа", "Скорость наблюдения"]
    human = ["Намерение",
             "Суждение о сигнале против шума",
             "Ответственность за каждый ответ продукта",
             "Решение «здесь ИИ не тот инструмент»",
             "Управление с названным владельцем"]

    ocean_box(s, 0.55, 3.42, 6.25, 2.02, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.5)
    icon(s, "repeat", 0.80, 3.56, 0.40, "teal")
    text_box(s, x=1.34, y=3.58, w=5.2, h=0.32, text="Что изменилось",
             size=13.5, bold=True, color=TEAL)
    for i, t in enumerate(changed):
        y = 4.04 + i * 0.34
        circle(s, 0.86, y + 0.09, 0.13, TEAL)
        text_box(s, x=1.18, y=y, w=5.4, h=0.30, text=t, size=12, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE)

    ocean_box(s, 7.05, 3.42, 5.75, 2.02, fill=SURFACE, stroke=MID,
              stroke_pt=1.5)
    icon(s, "users", 7.30, 3.56, 0.40, "mid")
    text_box(s, x=7.84, y=3.58, w=4.7, h=0.32,
             text="Что осталось человеческим", size=13.5, bold=True,
             color=MID)
    for i, t in enumerate(human):
        y = 3.94 + i * 0.29
        circle(s, 7.36, y + 0.08, 0.13, GOLD)
        text_box(s, x=7.68, y=y, w=4.95, h=0.28, text=t, size=11.5,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.66, 12.25, 0.82,
        "Когда сборка бесплатна, дефицитный ресурс — не исполнение, "
        "а суждение.",
        size=15, bold=True, align=PP_ALIGN.CENTER)
    notes_with_sources(s, "s49")
    return s


