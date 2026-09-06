"""Лекция 5 — Band 4 (Раздел 6 Governance/финал s44-s49 + ELI5 s44b).

Palette Ocean LOCKED, motif «Ocean rounded box», Gold >=1x/slide.
s49 = hero payoff (>=40% area, замкнутая петля с человеком в центре).
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


def s44(p):
    return build_section_divider(
        p, here_idx=6,
        subtitle="Управление — капстоун, отвечающий на хук-парадокс",
        bridge="Почему сборка почти бесплатна, а ценность — нет. Здесь мы "
               "поднимаемся на уровень организации и собираем петлю целиком.",
        sid="s44", tag="2 провала · развязка",
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
             "на выходе. У AI-продукта новая переменная — стоимость каждого "
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
    widths = [5.35, 4.0, 2.6, 1.4]
    labels = ["много инициатив", "гейт 1", "гейт 2", "профинансированы"]
    cols = [LIGHT, MID, TEAL, GOLD]
    for i, (w, lb, col) in enumerate(zip(widths, labels, cols)):
        y = 2.25 + i * 0.68
        x = 0.80 + (5.5 - w) / 2
        filled_rect(s, x, y, w, 0.52, SURFACE, stroke=col, stroke_pt=1.6,
                    radius=True, radius_adj=0.10)
        text_box(s, x=x, y=y, w=w, h=0.52, text=lb, size=11.5, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # right: unit economics
    ocean_box(s, 6.85, 1.60, 5.95, 1.85, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    text_box(s, x=7.10, y=1.75, w=5.45, h=0.4, text="Unit-экономика AI-продукта",
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
             text="Deloitte: 75% — модель должна измениться · 42% низкий/нулевой ROI",
             size=11, italic=True, color=SLATE)
    # right: maturity scale
    ocean_box(s, 7.15, 1.60, 5.65, 3.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    text_box(s, x=7.40, y=1.75, w=5.15, h=0.4, text="Зрелость 0–5 (maturity)",
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
                  "уровень 3 из 5 — сигнал против хайпа: даже крупный игрок не "
                  "заявляет вершину шкалы.",
             size=12, color=DEEP, line_spacing=1.18)
    gold_callout(
        s, 0.55, 5.35, 12.25, 0.72,
        "Пять независимых источников сходятся в одном: выигрывает не тот, у "
        "кого лучше модель, а тот, кто перестроил команды и управление под неё.",
        size=12.5, bold=True)
    notes_with_sources(s, "s46")
    return s


def s47(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "60% исследовали → 20% пилот → 5% успех: это 25% среди дошедших, не «95% провал»",
                size=18, w=12.3, h=0.85)
    # left: real MIT funnel chart + logo
    photo_in_box(s, "s47-mit-real-source.png", 0.55, 1.60, 2.75, 1.55, pad=0.14)
    ocean_box(s, 0.55, 3.30, 2.75, 2.10, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.6)
    text_box(s, x=0.70, y=3.45, w=2.45, h=1.85,
             text="«95% провал» — заголовок, который не переживает "
                  "калибровку: успех среди дошедших до пилота — 25%, не 5%.",
             size=12, bold=True, color=DEEP, line_spacing=1.18,
             anchor=MSO_ANCHOR.MIDDLE)
    ocean_box(s, 3.55, 1.60, 4.35, 3.80, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    add_image(s, CHARTS / "c-mit-funnel.png", 3.75, 2.30, 3.95, 2.45,
              preserve_aspect=True)
    # right: 4 questions
    ocean_box(s, 8.15, 1.60, 4.65, 3.80, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=8.40, y=1.75, w=4.15, h=0.5,
             text="4 вопроса к любой громкой цифре провала AI",
             size=13, bold=True, color=MID, line_spacing=1.1)
    qs = ["1. Каков денаминатор?", "2. Что считается «провалом»?",
          "3. Каков конфликт интересов автора?",
          "4. Прослеживается ли к первоисточнику с методологией?"]
    for i, qq in enumerate(qs):
        text_box(s, x=8.40, y=2.45 + i * 0.66, w=4.15, h=0.62, text=qq,
                 size=12.5, color=DEEP, line_spacing=1.1)
    gold_callout(
        s, 0.55, 5.55, 12.25, 0.62,
        "BCG: 60% компаний не отслеживают ни одного финансового KPI, "
        "привязанного к ценности AI — вот почему цифры провалов так легко "
        "раздуваются.",
        size=12, bold=True)
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
                  "ручная проверка (14× выше цели 50/1000). 6 лет маркетинга "
                  "«автономный AI» без раскрытия масштаба труда (скрытая "
                  "человеческая стоимость).",
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
    text_box(s, x=0.55, y=y0, w=12.25, h=0.42, text="Фаза × что AI меняет × что остаётся из классики",
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
    notes_with_sources(s, "s48")
    return s


def s49(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Сборка бесплатна — дефицит теперь: суждение, а не исполнение",
                size=22, w=12.3, h=0.85)
    # HERO >=40%: closed gold loop with a person at center
    import math
    cx, cy, r = 3.35, 3.20, 1.62
    steps = ["Исследование", "Дизайн", "Сборка", "Измерение", "Поддержка",
             "Управление"]
    centers = []
    for i in range(6):
        ang = math.pi / 2 - i * (2 * math.pi / 6)
        centers.append((cx + r * math.cos(ang), cy - r * math.sin(ang)))
    for i in range(6):
        x1, y1 = centers[i]
        x2, y2 = centers[(i + 1) % 6]
        connector(s, x1, y1, x2, y2, color=GOLD, width=3.0)
    for i, (nx, ny) in enumerate(centers):
        circle(s, nx - 0.26, ny - 0.26, 0.52, GOLD, stroke=WHITE, stroke_pt=1.6)
        text_box(s, x=nx - 0.85, y=ny + 0.28, w=1.7, h=0.34, text=steps[i],
                 size=9, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    circle(s, cx - 0.55, cy - 0.55, 1.10, GOLD_TINT, stroke=GOLD, stroke_pt=2.2)
    icon(s, "users", cx - 0.35, cy - 0.35, 0.70, "gold")
    text_box(s, x=cx - 1.0, y=cy + 0.60, w=2.0, h=0.35, text="человек в центре",
             size=11, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    # right: checklist
    ocean_box(s, 6.35, 1.55, 6.45, 3.65, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    text_box(s, x=6.60, y=1.68, w=5.95, h=0.4,
             text="Чек-лист «прежде чем делать фазу AI-first»", size=14,
             bold=True, color=MID)
    checks = [
        "1. Классика на месте?", "2. Стоит ли доверие цены?",
        "3. Есть эталонный набор и eval?", "4. Есть guardrail-метрика?",
        "5. Поэтапная раскатка + откат?", "6. Гарантирована эскалация к человеку?",
        "7. Кто отвечает?", "8. Данные безопасны?",
    ]
    for i, c in enumerate(checks):
        col_i = i % 2
        row_i = i // 2
        x = 6.60 + col_i * 3.0
        y = 2.25 + row_i * 0.68
        icon(s, "circle-check", x, y, 0.30, "teal")
        text_box(s, x=x + 0.40, y=y - 0.02, w=2.6, h=0.5, text=c, size=11.5,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    text_box(s, x=6.60, y=4.95, w=5.95, h=0.35,
             text="Парный семинар: та же петля на учебном AI-продукте",
             size=11.5, italic=True, color=SLATE)
    gold_callout(
        s, 0.55, 5.35, 12.25, 0.80,
        "Когда исполнение почти бесплатно, дефицитный ресурс — суждение: "
        "отличить сигнал от шума и удержать намерение и ответственность на "
        "человеке.",
        size=13.5, bold=True)
    notes_with_sources(s, "s49")
    return s
