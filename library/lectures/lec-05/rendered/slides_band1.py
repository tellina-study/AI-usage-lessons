"""Лекция 5 — Band 1 (Раздел 0 s01-s06 + Раздел 1 Discovery s07-s13a).

Each sNN(p) builds one slide from slides/sNN*.md (visible content +
meme_or_visual brief). Palette Ocean LOCKED, motif «Ocean rounded box»,
Gold >=1x/slide. Meme-forward + minimal text (owner rule): every slide
realizes its meme_or_visual brief as an icon-composition (evergreen,
no photo needed for this band per the briefs themselves).

NO timing / NO methodology / NO superlatives / NO photo-attribution labels
on the visible layer (owner ENFORCED rules) — source lives only in
notes_with_sources() -> speaker notes, never on the slide body.
"""
from _helpers import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    right_arrow, circle, chip, connector, add_image, icon, slide_title,
    gold_callout, teal_callout, footer, src, speaker_notes, load_notes,
    notes_with_sources, refs_of_slide, roadmap_bar, build_section_divider,
    eli5_overview, meme_in_box, photo_in_box,
    NAV, DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE, COVER_OUTLINE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, MID_TINT, ICONS, CHARTS, ASSETS,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

SCR = ASSETS / "screenshots"


# ============================================================
# s01 - hook paradox (hero >=40% area, icon-metaphor)
# ============================================================
def s01(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Сборка почти бесплатна. Почему тогда почти никто не извлекает из этого пользу?",
        size=21, w=12.2, h=0.80, y=0.30)

    # GATE-B fix: hero meme was only ~16.5% of slide area (4.65x3.55 in a
    # split layout) — under the 40% hero mandate. Rebuilt as a dominant
    # right-side hero (7.65x5.30 = ~40.5% of the 13.333x7.5 canvas) with the
    # two-fact metaphor compressed into a narrow left column instead of a
    # second equal-weight box, so the meme is unambiguously the hero, not a
    # co-equal panel.
    lx, lw = 0.55, 4.35
    fact_h = 1.62
    ocean_box(s, lx, 1.30, lw, fact_h, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    icon(s, "clock", lx + 0.24, 1.30 + 0.20, 0.80, "mid")
    text_box(s, x=lx + 1.18, y=1.30 + 0.16, w=lw - 1.40, h=0.75,
             text="Недели работы → часы", size=14, bold=True, color=MID,
             line_spacing=1.02, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 1.18, y=1.30 + fact_h - 0.42, w=lw - 1.40, h=0.34,
             text="внутренний опыт Anthropic", size=10.5, italic=True,
             color=SLATE)
    ocean_box(s, lx, 1.30 + fact_h + 0.16, lw, fact_h, fill=SURFACE,
              stroke=LIGHT, stroke_pt=1.5)
    icon(s, "funnel", lx + 0.24, 1.30 + fact_h + 0.16 + 0.20, 0.80, "teal")
    text_box(s, x=lx + 1.18, y=1.30 + fact_h + 0.16 + 0.16, w=lw - 1.40, h=0.75,
             text="~95% пилотов — ноль отдачи", size=14, bold=True,
             color=TEAL, line_spacing=1.02, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 1.18, y=1.30 + 2 * fact_h + 0.16 - 0.42, w=lw - 1.40,
             h=0.34, text="MIT, лето 2025", size=10.5, italic=True, color=SLATE)
    gold_callout(
        s, lx, 1.30 + 2 * fact_h + 0.16 + 0.18, lw, 2.14,
        "Оба факта правдивы одновременно: сборка стала почти бесплатной, а "
        "превращение сборки в ценность — нет. Держите вопрос — вернёмся к "
        "нему в конце лекции.",
        size=13, bold=True)
    # right: real meme (Spider-Man Pointing at Spider-Man — GATE-B fix,
    # replaces This-Is-Fine: lec-2 collision + tonal mismatch, see
    # notes/lecture-5-review/pdlc/2026-09-07-arc-meme-layout-audit.md) — two
    # simultaneously-true facts pointing at each other, the unambiguous hero
    # (>=40% slide area)
    from _helpers import meme_in_box
    meme_in_box(s, "s01-spiderman-pointing.jpg", 5.15, 1.30, 7.65, 5.30,
                pad=0.18)
    notes_with_sources(s, "s01")
    return s


# ============================================================
# s02 - cover + roadmap (hero >=40% area: circular loop icon)
# ============================================================
def s02(p):
    s = blank(p)
    set_slide_bg(s, SURFACE)
    # decorative circular loop of 6 nodes, upper-left (hero, evergreen)
    cx, cy, r = 3.15, 2.85, 1.55
    import math
    nodes = ["Исследование", "Дизайн", "Сборка\nи запуск", "Измерение",
             "Поддержка", "Управление"]
    centers = []
    for i, label in enumerate(nodes):
        ang = math.pi / 2 - i * (2 * math.pi / 6)
        nx = cx + r * math.cos(ang)
        ny = cy - r * math.sin(ang)
        centers.append((nx, ny))
    # connecting arcs first (behind nodes) so the ring reads as ONE loop
    for i in range(6):
        x1, y1 = centers[i]
        x2, y2 = centers[(i + 1) % 6]
        connector(s, x1, y1, x2, y2, color=LIGHT, width=2.0)
    for i, (label, (nx, ny)) in enumerate(zip(nodes, centers)):
        circle(s, nx - 0.30, ny - 0.30, 0.60, MID if i else GOLD,
               stroke=WHITE, stroke_pt=1.5)
        text_box(s, x=nx - 0.85, y=ny + 0.32, w=1.70, h=0.42, text=label,
                 size=9, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 line_spacing=0.9)
    icon(s, "lightbulb", cx - 0.32, cy - 0.32, 0.64, "gold")

    # real meme (One Does Not Simply) — cover meme, bottom-left, framed
    from _helpers import meme_in_box
    meme_in_box(s, "s02-one-does-not-simply.jpg", 0.75, 4.85, 5.0, 1.55,
                pad=0.10)

    # title block, right
    text_box(s, x=6.55, y=1.55, w=6.35, h=0.5, text="ЛЕКЦИЯ 5",
             size=20, bold=True, color=TEAL)
    text_box(s, x=6.55, y=2.10, w=6.40, h=2.0,
             text="AI-продукт: полный жизненный цикл — от намерения до эксплуатации",
             size=30, bold=True, color=DEEP, line_spacing=1.05)
    text_box(s, x=6.58, y=4.35, w=6.30, h=0.6,
             text="Курс «Осознанное применение ИИ» · инженеры-студенты 3 курса",
             size=14, italic=True, color=LIGHT)
    gold_callout(
        s, 6.55, 5.05, 6.35, 0.78,
        "Шесть разделов — шесть стрелок одной петли: код (Лекция 4) — один "
        "дешёвый шаг внутри неё.",
        size=13, bold=True)
    roadmap_bar(s, 0, y=6.55)
    notes_with_sources(s, "s02")
    return s


# ============================================================
# s03 - lecture map as loop (schema_cycle)
# ============================================================
def s03(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Лекция — это петля, а не список из шести тем",
                size=25, w=12.0, h=0.85)

    import math
    cx, cy, r = 4.15, 4.05, 2.05
    steps = [
        ("search", "1. Исследование", "откуда гипотеза"),
        ("pencil", "2. Дизайн", "гипотеза → артефакт"),
        ("hammer", "3. Сборка и запуск", "артефакт → продукт"),
        ("ruler", "4. Измерение", "сработало ли"),
        ("headphones", "5. Поддержка", "живёт 24/7"),
        ("scale", "6. Управление", "куда вкладывать"),
    ]
    centers = []
    for i in range(6):
        ang = math.pi / 2 - i * (2 * math.pi / 6)
        centers.append((cx + r * math.cos(ang), cy - r * math.sin(ang)))
    # GATE-B fix: connecting arcs BEHIND the boxes so the 6 nodes read as ONE
    # loop (previously floating disconnected boxes — directly contradicted
    # the slide's own claim "петля, а не список"). Arrowheads on every edge
    # show explicit direction of travel (schema_cycle checklist: explicit
    # start + continue). Edge into node 0 is gold — marks the return/restart.
    for i in range(6):
        x1, y1 = centers[i]
        x2, y2 = centers[(i + 1) % 6]
        # shrink the segment toward the box edges so the line doesn't run
        # underneath the box interior (visually cleaner "hop" between boxes)
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy)
        ux, uy = dx / dist, dy / dist
        pad = 0.62
        sx1, sy1 = x1 + ux * pad, y1 + uy * pad
        sx2, sy2 = x2 - ux * pad, y2 - uy * pad
        is_return = (i == 5)  # Управление(5) -> Исследование(0)
        connector(s, sx1, sy1, sx2, sy2,
                  color=(GOLD if is_return else LIGHT),
                  width=(2.6 if is_return else 2.0),
                  arrow_end=True)
    for i, (ic, name, desc) in enumerate(steps):
        nx, ny = centers[i]
        ocean_box(s, nx - 0.70, ny - 0.48, 1.40, 0.96, fill=SURFACE,
                  stroke=MID, stroke_pt=1.3)
        icon(s, ic, nx - 0.24, ny - 0.42, 0.48, "mid")
        text_box(s, x=nx - 0.68, y=ny + 0.06, w=1.36, h=0.40, text=name,
                 size=7.8, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 line_spacing=0.88)
    text_box(s, x=cx - 0.85, y=cy - 0.30, w=1.7, h=0.6, text="Намерение",
             size=12, bold=True, color=GOLD, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)

    # right column: numbered list + return arrow note
    rx, rw = 7.15, 5.65
    for i, (ic, name, desc) in enumerate(steps):
        y = 1.55 + i * 0.62
        text_box(s, x=rx, y=y, w=rw, h=0.56,
                 text=f"{name} — {desc}", size=13, bold=True, color=DEEP,
                 line_spacing=1.0)
    gold_callout(
        s, 7.15, 5.55, 5.65, 1.00,
        "Стрелка возврата: управление снова питает исследование — "
        "замкнутая петля, а не одноразовый линейный процесс.",
        size=12.5, bold=True)
    notes_with_sources(s, "s03")
    return s


# ============================================================
# s04 - bridge from Lec-4 + central question (nested loops)
# ============================================================
def s04(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Цикл кода Лекции 4 — это один шаг внутри цикла продукта",
                size=23, w=12.0, h=0.85)

    # outer big loop box
    ocean_box(s, 0.55, 1.50, 12.25, 2.85, fill=SURFACE, stroke=MID,
              stroke_pt=1.6)
    text_box(s, x=0.80, y=1.62, w=6.0, h=0.35, text="Цикл продукта (Лекция 5)",
             size=13, bold=True, color=MID)
    # GATE-B fix (audit 2026-09-07): the upper-left quadrant of this box used
    # to be ~45-50% blank — "Цикл продукта" was only NAMED, never SHOWN. Add
    # a compact 6-node mini-loop (small-scale reuse of the s03 icon-loop
    # pattern) so the thesis box's own hero content — the loop itself — is
    # visible here, not just in the caption line below it. This is the
    # lecture's highest-stakes bridge slide (central-question payload).
    import math
    mcx, mcy, mr = 2.55, 2.85, 0.72
    mnodes = ["search", "pencil", "hammer", "ruler", "headphones", "scale"]
    mcenters = []
    for i in range(6):
        ang = math.pi / 2 - i * (2 * math.pi / 6)
        mcenters.append((mcx + mr * math.cos(ang), mcy - mr * math.sin(ang)))
    for i in range(6):
        x1, y1 = mcenters[i]
        x2, y2 = mcenters[(i + 1) % 6]
        connector(s, x1, y1, x2, y2,
                  color=(GOLD if i == 5 else LIGHT),
                  width=(2.0 if i == 5 else 1.4), arrow_end=True)
    for i, ic in enumerate(mnodes):
        nx, ny = mcenters[i]
        circle(s, nx - 0.22, ny - 0.22, 0.44, WHITE, stroke=MID, stroke_pt=1.2)
        icon(s, ic, nx - 0.14, ny - 0.14, 0.28, "mid")
    chip(s, 4.55, 2.62, 1.05, 0.42, "6 фаз", fill=GOLD, color=DEEP, size=12)
    icon(s, "layers", 0.85, 3.75, 0.5, "teal")
    text_box(s, x=1.50, y=3.75, w=6.05, h=0.55,
             text="исследование → дизайн → сборка/запуск → измерение → "
                  "эксплуатация → управление → снова исследование",
             size=11, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
    # inner small loop box nested inside "build" area
    ocean_box(s, 7.9, 2.05, 4.65, 2.00, fill=WHITE, stroke=GOLD,
              stroke_pt=1.8)
    text_box(s, x=8.10, y=2.20, w=4.30, h=0.32,
             text="Цикл кода (Лекция 4)", size=11.5, bold=True, color=DEEP)
    text_box(s, x=8.10, y=2.62, w=4.30, h=1.20,
             text="спека → ADR → план → PR → инцидент",
             size=12, italic=True, color=SLATE, line_spacing=1.2,
             anchor=MSO_ANCHOR.TOP)
    icon(s, "git-branch", 8.10, 3.30, 0.5, "teal")

    ocean_box(s, 0.55, 4.35, 12.25, 1.65)
    text_box(s, x=0.85, y=4.48, w=11.65, h=1.4,
             text="Когда ИИ сделал сборку почти бесплатной — что стало "
                  "настоящим узким местом продукта, и на каждой фазе цикла: "
                  "какая классическая дисциплина остаётся, что ИИ ускоряет, "
                  "и где AI-first ломается?",
             size=17, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.18)

    gold_callout(
        s, 0.55, 6.15, 12.25, 0.60,
        "Единица работы Лекции 4 — pull request (запрос на слияние кода). "
        "Единица работы здесь — "
        "гипотеза, эксперимент, релиз-решение.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    notes_with_sources(s, "s04")
    return s


# ============================================================
# s05 - KEYSTONE: loop, 3 independent sources (PDCA/OODA/BML)
# ============================================================
def s05(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Три человека из разных областей нарисовали один и тот же чертёж",
                size=23, w=12.2, h=0.85)

    domains = [
        ("bar-chart-3", "Деминг · статистика качества", "PDCA",
         "планируй → делай → проверяй → корректируй"),
        ("plane", "Бойд · воздушный бой", "OODA",
         "наблюдай → ориентируйся → решай → действуй"),
        ("rocket", "Райс · стартапы", "BML",
         "строй → измеряй → учись"),
    ]
    cw, gap = 3.95, 0.20
    x0 = 0.55
    y0 = 1.55
    for i, (ic, who, tag, seq) in enumerate(domains):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 2.05)
        icon(s, ic, x + 0.24, y0 + 0.20, 0.56, "mid")
        text_box(s, x=x + 0.94, y=y0 + 0.22, w=cw - 1.15, h=0.55, text=who,
                 size=11.5, bold=True, color=MID, line_spacing=1.0)
        chip(s, x + 0.24, y0 + 0.86, 1.15, 0.36, tag, fill=GOLD, color=DEEP,
             size=13)
        text_box(s, x=x + 0.24, y=y0 + 1.32, w=cw - 0.48, h=0.66, text=seq,
                 size=10.5, color=DEEP, line_spacing=1.08)

    # central shared loop symbol below
    cx = 6.67
    circle(s, cx - 0.55, 3.95, 1.10, GOLD_TINT, stroke=GOLD, stroke_pt=2.2)
    icon(s, "repeat", cx - 0.35, 4.15, 0.70, "gold")
    for i in range(3):
        x = x0 + i * (cw + gap) + cw / 2
        connector(s, x, y0 + 2.05, cx, 3.95, color=LIGHT, width=1.4,
                  dash="dash")

    gold_callout(
        s, 0.55, 5.35, 12.25, 0.85,
        "Не сговариваясь — один и тот же чертёж: петля обратной связи как "
        "структурное свойство любой системы, которая учится в условиях "
        "неопределённости.",
        size=13.5, bold=True)
    notes_with_sources(s, "s05")
    return s


# ============================================================
# s06 - KEYSTONE-2: cost/trust asymmetry (axis slide)
# ============================================================
def s06(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "ИИ меняет стоимость и доверие каждой стрелки петли — но не одинаково",
                size=21, w=12.3, h=0.85)

    rows = [
        ("hammer", "Строить", "стоимость почти обнулилась", GOLD, "gold"),
        ("ruler", "Измерять / учиться", "стоимость та же, доверие упало",
         LIGHT, "light"),
        ("search", "Исследовать", "быстрее, но уязвимее к атаке",
         TEAL, "teal"),
    ]
    y0 = 1.55
    for i, (ic, name, desc, col, av) in enumerate(rows):
        y = y0 + i * 1.05
        ocean_box(s, 0.55, y, 12.25, 0.90, fill=SURFACE, stroke=col,
                  stroke_pt=1.6)
        icon(s, ic, 0.80, y + 0.20, 0.5, av)
        text_box(s, x=1.50, y=y + 0.14, w=3.5, h=0.6, text=name, size=15,
                 bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=5.15, y=y + 0.14, w=7.4, h=0.6, text=desc, size=14,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 4.85, 12.25, 0.95,
        "Мета-паттерн, повторяется в каждом из 6 разделов: у каждой стрелки "
        "есть классическая дисциплина — ИИ её не отменяет, а меняет её "
        "стоимость и требуемую степень проверки.",
        size=13.5, bold=True)

    filled_rect(s, 0.55, 5.95, 12.25, 0.75, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.08)
    text_box(s, x=0.85, y=6.08, w=11.65, h=0.55,
             text="Подумайте: на какой стрелке вашей последней задачи "
                  "скорость обогнала ваше реальное доверие к результату?",
             size=12.5, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)
    notes_with_sources(s, "s06")
    return s


# ============================================================
# s07 - section divider Р1 Discovery
# ============================================================
def s07(p):
    return build_section_divider(
        p, here_idx=1,
        subtitle="Исследование — намерение и гипотеза",
        bridge="Откуда вообще берётся гипотеза о том, что строить. У "
               "большинства есть неформальный опыт «спросить у друзей» — и "
               "почти никто не сталкивался с формальной дисциплиной, "
               "объясняющей, почему этот опыт систематически лжёт.",
        sid="s07", tag="2 базы · 3 провала",
        meme_name="s07-distracted-boyfriend.jpg")


# ============================================================
# s07b - ELI5 overview «Исследование для чайников»
# ============================================================
def s07b(p):
    return eli5_overview(
        p, "s07b", title="Исследование простыми словами", icon_name="search",
        cards=[
            ("Что это",
             "Фаза, где вы ищете не решение, а проблему: у кого болит, "
             "насколько сильно и готов ли человек за это платить временем, "
             "репутацией или деньгами."),
            ("Зачем",
             "Построить можно что угодно; ценно только то, что решает реальную "
             "боль реального человека. «Я бы таким пользовался» — не факт."),
            ("Ментальная модель",
             "Внутри офиса нет фактов — факты снаружи. Записываете гипотезу, "
             "выходите к людям, проверяете. ИИ ускоряет сбор, но не заменяет "
             "разговор с настоящим человеком."),
        ])


# ============================================================
# s08 - BASE: Customer Development (4-step flow)
# ============================================================
def s08(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "«Внутри офиса нет фактов» — 4 шага, каждый заканчивается решением",
                size=22, w=12.2, h=0.85)

    steps = [
        ("Исследование", "discovery"), ("Проверка", "validation"),
        ("Создание спроса", "creation"), ("Масштаб", "building"),
    ]
    cw, gap = 2.72, 0.28
    x0 = 0.55
    y0 = 1.85
    for i, (name, gloss) in enumerate(steps):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 1.35, fill=SURFACE, stroke=MID, stroke_pt=1.5)
        text_box(s, x=x + 0.10, y=y0 + 0.12, w=cw - 0.20, h=0.28,
                 text=f"{i+1}", size=14, bold=True, color=GOLD,
                 align=PP_ALIGN.CENTER)
        text_box(s, x=x + 0.06, y=y0 + 0.42, w=cw - 0.12, h=0.34, text=name,
                 size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x=x + 0.10, y=y0 + 0.74, w=cw - 0.20, h=0.26, text=gloss,
                 size=9.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
        icon(s, "diamond", x + cw / 2 - 0.16, y0 + 1.02, 0.32, "gold")
        if i < 3:
            right_arrow(s, x + cw + 0.02, y0 + 0.55, gap - 0.04, 0.26,
                        fill=LIGHT)
    text_box(s, x=0.55, y=y0 + 1.45, w=12.25, h=0.35,
             text="Стив Бланк — методология Customer Development",
             size=12.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)

    # falsifiable-hypothesis card
    ocean_box(s, 1.55, 3.90, 10.25, 1.35, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.6)
    icon(s, "route", 1.80, 4.10, 0.5, "gold")
    text_runs(s, 2.45, 4.08, 9.10, 1.05, [
        {"text": "Фальсифицируемая гипотеза", "size": 14, "bold": True,
         "color": DEEP},
        {"text": "мы верим X → проверим через Y → к дате Z получим ответ да/нет",
         "size": 13, "color": DEEP, "newpara": True, "space_before": 6},
    ])

    gold_callout(
        s, 0.55, 5.55, 12.25, 0.85,
        "BML — двигатель; Customer Development — карта местности, по которой "
        "двигатель едет. Сначала понять, что проверяем и у кого — потом, как "
        "быстро крутить цикл.",
        size=13, bold=True)
    notes_with_sources(s, "s08")
    return s


# ============================================================
# s09 - BASE-2: The Mom Test (3 rules + contrast)
# ============================================================
def s09(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Даже мать соврёт — если вопрос сконструирован неправильно",
                size=23, w=12.2, h=0.85)

    rules = [
        ("message-square-x", "Об их жизни, не о вашей идее",
         "не питчите идею и не просите вердикт"),
        ("history", "О прошлом, не о будущем",
         "гипотетические вопросы провоцируют нечестный оптимизм"),
        ("handshake", "Обязательством, не комплиментом",
         "легитимные сигналы: время, репутация, деньги"),
    ]
    cw, gap = 3.95, 0.20
    x0 = 0.55
    y0 = 1.55
    for i, (ic, head, body) in enumerate(rules):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 1.85)
        icon(s, ic, x + 0.24, y0 + 0.18, 0.5, "mid")
        text_box(s, x=x + 0.24, y=y0 + 0.78, w=cw - 0.48, h=0.50, text=head,
                 size=13, bold=True, color=DEEP, line_spacing=1.05)
        text_box(s, x=x + 0.24, y=y0 + 1.30, w=cw - 0.48, h=0.50, text=body,
                 size=10.5, italic=True, color=SLATE, line_spacing=1.05)

    # contrast: bad vs good question
    by = 3.70
    filled_rect(s, 0.55, by, 5.95, 1.35, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.07)
    text_box(s, x=0.80, y=by + 0.15, w=5.45, h=0.35, text="Плохо",
             size=12.5, bold=True, color=SLATE)
    text_box(s, x=0.80, y=by + 0.52, w=5.45, h=0.75,
             text="«Заплатили бы $20 в месяц?»", size=13.5, italic=True,
             color=SLATE, line_spacing=1.1)
    filled_rect(s, 6.75, by, 6.05, 1.35, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.6, radius=True, radius_adj=0.07)
    text_box(s, x=7.00, y=by + 0.15, w=5.55, h=0.35, text="Хорошо",
             size=12.5, bold=True, color=TEAL)
    text_box(s, x=7.00, y=by + 0.52, w=5.55, h=0.75,
             text="«Сколько вы платите сегодня за ближайший аналог?»",
             size=13.5, bold=True, color=DEEP, line_spacing=1.1)

    gold_callout(
        s, 0.55, 5.35, 12.25, 0.85,
        "Качественное отвечает «почему» на маленькой выборке и порождает "
        "гипотезы; количественное отвечает «сколько» в масштабе и проверяет "
        "уже существующую гипотезу — не иерархия, а разделение труда.",
        size=12.5, bold=True)
    notes_with_sources(s, "s09")
    return s


# ============================================================
# s10 - ИИ: discovery tools 2025-26
# ============================================================
def s10(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Часы → минуты: но ссылки существуют, чтобы их проверяли",
                size=22, w=12.2, h=0.85)

    blocks = [
        ("file-search", "Desk research (кабинетное исследование)",
         "Perplexity Deep Research: 2 часа → ~30 минут"),
        ("layout-list", "Синтез интервью",
         "Dovetail — кластеризация болей в масштабе"),
        ("database", "Reference dataset (эталонный набор)",
         "курируемая коллекция «запрос → правильный ответ»"),
    ]
    cw, gap = 3.95, 0.20
    x0 = 0.55
    y0 = 1.55
    for i, (ic, head, body) in enumerate(blocks):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 2.05)
        icon(s, ic, x + 0.24, y0 + 0.20, 0.56, "mid")
        text_box(s, x=x + 0.24, y=y0 + 0.88, w=cw - 0.48, h=0.50, text=head,
                 size=12, bold=True, color=MID, line_spacing=1.05)
        text_box(s, x=x + 0.24, y=y0 + 1.44, w=cw - 0.48, h=0.55, text=body,
                 size=11, color=DEEP, line_spacing=1.10)
        if i == 0:
            chip(s, x + cw - 1.55, y0 + 0.20, 1.30, 0.36, "проверь источник",
                 fill=GOLD, color=DEEP, size=9)

    gold_callout(
        s, 0.55, 3.90, 12.25, 0.72,
        "97% исследователей используют ИИ — лишь ~8% доверяют ИИ-персонам "
        "как данным",
        size=14.5, bold=True, align=PP_ALIGN.CENTER)

    filled_rect(s, 0.55, 4.85, 12.25, 1.35, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    text_box(s, x=0.85, y=4.98, w=11.65, h=1.10,
             text="Обязательная практика: проверять важные данные напрямую "
                  "по источнику до использования в решении. Синтетические "
                  "пользователи — только пре-исследование (пилотаж гайда, "
                  "черновик персон, генерация гипотез), никогда не "
                  "доказательство для решения «продолжать/остановить».",
             size=12.5, color=DEEP, line_spacing=1.15,
             anchor=MSO_ANCHOR.MIDDLE)
    notes_with_sources(s, "s10")
    return s


# ============================================================
# s11 - ИИ LIMITS: synthetic sycophancy, live-interview criteria
# ============================================================
def s11(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Синтетический собеседник не может произвести несогласие",
                size=22, w=12.2, h=0.85)

    lx, lw = 0.55, 4.30
    ocean_box(s, lx, 1.55, lw, 3.35, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    icon(s, "smile", lx + lw / 2 - 0.55, 1.90, 1.10, "light")
    text_box(s, x=lx + 0.25, y=3.15, w=lw - 0.50, h=1.55,
             text="Зеркало согласия: синтетический собеседник структурно не "
                  "может отразить несогласие — у него нет реального прошлого, "
                  "способного противоречить формулировке вопроса.",
             size=12.5, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.18)

    rx, rw = 5.15, 7.65
    crit = [
        "Высокая цена ошибки «продолжать/остановить»",
        "Нужно реальное прошлое, не правдоподобное",
        "Нужна валидация обязательством, не мнением",
    ]
    text_box(s, x=rx, y=1.55, w=rw, h=0.40,
             text="Когда живое интервью строго лучше ИИ-синтеза", size=14,
             bold=True, color=MID)
    for i, c in enumerate(crit):
        y = 2.10 + i * 0.85
        ocean_box(s, rx, y, rw, 0.70, fill=SURFACE, stroke=MID, stroke_pt=1.3)
        text_box(s, x=rx + 0.65, y=y, w=rw - 0.85, h=0.70, text=f"{i+1}. {c}",
                 size=13, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        icon(s, "shield-alert", rx + 0.14, y + 0.15, 0.42, "mid")

    gold_callout(
        s, 0.55, 5.10, 12.25, 0.95,
        "ИИ-резюме теряет 20-40% деталей интервью (Torres), если пропущен "
        "шаг «сначала по отдельности» — прослеживаемый до конкретного шага "
        "сбой, не расплывчатое «ИИ иногда ошибается».",
        size=13, bold=True)
    notes_with_sources(s, "s11")
    return s


# ============================================================
# s12 - FAILURE on-point #1: synthetic users (NN/g)
# ============================================================
def s12(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Одна и та же задача: реальные люди — 3 из 7, синтетическая панель — 7 из 7",
        size=20, w=12.2, h=0.85)

    # LEFT: real meme (Trade Offer — GATE-B fix, replaces Surprised Pikachu:
    # lec-2 collision + weak affect-fit, see arc-meme-layout-audit.md) — the
    # false 7/7 "offer" vs the 3/7 that actually decides
    from _helpers import meme_in_box
    meme_in_box(s, "s12-trade-offer.jpg", 0.55, 1.55, 4.55, 3.15, pad=0.14)

    # RIGHT: split comparison 3/7 vs 7/7
    rx, rw = 5.35, 7.45
    ocean_box(s, rx, 1.55, rw, 1.05, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=rx + 0.24, y=1.63, w=3.0, h=0.36,
             text="Реальные люди", size=12.5, bold=True, color=MID)
    for i in range(7):
        cxx = rx + 0.28 + i * 0.42
        ok = i < 3
        icon(s, "check-check" if ok else "x", cxx, 2.02, 0.36,
             "mid" if ok else "light")
    text_box(s, x=rx + 3.35, y=1.75, w=rw - 3.6, h=0.7,
             text="3 из 7 — «надуманно и бесполезно»", size=12, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)

    ocean_box(s, rx, 2.75, rw, 1.05, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.8)
    text_box(s, x=rx + 0.24, y=2.83, w=3.0, h=0.36,
             text="Синт-панель", size=12.5, bold=True, color=DEEP)
    for i in range(7):
        cxx = rx + 0.28 + i * 0.42
        icon(s, "check-check", cxx, 3.22, 0.36, "gold")
    text_box(s, x=rx + 3.35, y=2.95, w=rw - 3.6, h=0.7,
             text="7 из 7 — «меняет правила игры»", size=12, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    text_box(s, x=rx, y=3.95, w=rw, h=0.55,
             text="Одна и та же фича — противоположные вердикты",
             size=12.5, italic=True, color=SLATE)

    gold_callout(
        s, 0.55, 4.90, 12.25, 1.05,
        "Критерий: синтетический выход дисквалифицирован для решения "
        "«продолжать/остановить» по построению, а не из-за невезения "
        "прогона. Альтернатива: до-исследовательская роль + реальное "
        "тестирование 5-8 участников.",
        size=13, bold=True)
    notes_with_sources(s, "s12")
    return s


# ============================================================
# s13a - FAILURE on-point #3: IBM Watson for Oncology
# ============================================================
def s13a(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "$62 млн — и ни одного пролеченного пациента",
                size=23, w=12.2, h=0.85)

    # scale visual
    lx = 0.55
    ocean_box(s, lx, 1.55, 5.55, 2.55, fill=SURFACE, stroke=MID,
              stroke_pt=1.5)
    icon(s, "scale", lx + 2.35, 1.70, 0.9, "mid")
    text_box(s, x=lx + 0.25, y=2.70, w=2.4, h=0.75,
             text="$62 млн", size=22, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 2.9, y=2.70, w=2.4, h=0.75,
             text="0 пациентов", size=22, bold=True, color=TEAL,
             align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.25, y=3.55, w=5.05, h=0.45,
             text="MD Anderson: партнёрство закрыто (2016)", size=11.5,
             italic=True, color=SLATE, align=PP_ALIGN.CENTER)

    rx, rw = 6.35, 6.45
    text_box(s, x=rx, y=1.55, w=rw, h=0.35,
             text="IBM Watson for Oncology, с 2012", size=14, bold=True,
             color=MID)
    bullets = [
        "Внутренние документы: рекомендации «небезопасные и некорректные»",
        "Обучен на гипотетических кейсах горстки онкологов MSK — не на "
        "реальных исходах",
    ]
    for i, b in enumerate(bullets):
        y = 2.05 + i * 0.95
        icon(s, "user-x" if i else "users", rx, y, 0.42, "light")
        text_box(s, x=rx + 0.55, y=y - 0.05, w=rw - 0.55, h=0.85, text=b,
                 size=12.5, color=DEEP, line_spacing=1.12)

    gold_callout(
        s, 0.55, 4.35, 12.25, 1.15,
        "Критерий: домен с высокой ценой ошибки + только "
        "синтетические/гипотетические данные под рекомендацией = продукт не "
        "готов, каким бы впечатляющим ни было демо. Альтернатива: система на "
        "доказательных клинических руководствах с прозрачной "
        "трассируемостью источника.",
        size=13, bold=True)
    notes_with_sources(s, "s13a")
    return s


# ============================================================
# s13 - FAILURE on-point #2: Deloitte fabricated research
# ============================================================
def s13(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "A$440 000 отчёт правительству — с выдуманными цитатами внутри",
                size=20, w=12.2, h=0.85)

    lx, lw = 0.55, 6.55
    ocean_box(s, lx, 1.55, lw, 3.30)
    icon(s, "file-x", lx + 0.24, 1.75, 0.6, "mid")
    text_box(s, x=lx + 1.00, y=1.78, w=lw - 1.2, h=0.55,
             text="Deloitte Australia, 2025", size=15, bold=True, color=MID)
    facts = [
        "Ссылки на несуществующие статьи + сфабрикованная цитата суда",
        "Подготовлен через Azure OpenAI без человеческой верификации цитат",
    ]
    for i, f in enumerate(facts):
        y = 2.55 + i * 0.85
        text_box(s, x=lx + 0.28, y=y, w=lw - 0.56, h=0.75, text=f"• {f}",
                 size=12.5, color=DEEP, line_spacing=1.15)

    rx, rw = 7.35, 5.45
    ocean_box(s, rx, 1.55, rw, 1.55, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.8)
    icon(s, "banknote", rx + 0.24, 1.78, 0.55, "gold")
    text_box(s, x=rx + 0.95, y=1.80, w=rw - 1.15, h=0.55,
             text="A$440 000", size=26, bold=True, color=DEEP)
    text_box(s, x=rx + 0.24, y=2.55, w=rw - 0.48, h=0.45,
             text="≈US$290 000 отчёт", size=12, italic=True, color=SLATE)
    filled_rect(s, rx, 3.30, rw, 1.55, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.07)
    text_box(s, x=rx + 0.24, y=3.45, w=rw - 0.48, h=1.25,
             text="База: ~712 судебных решений по миру с ИИ-галлюцинированными "
                  "цитатами, ~90% — в 2025 году",
             size=12, color=DEEP, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.10, 12.25, 0.95,
        "Урок: вывод модели в discovery-фазе — неверифицированный черновик, "
        "не источник фактов. Критерий: итоговый документ внешнему заказчику "
        "требует 100% проверки каждой ссылки, не выборочной.",
        size=12.5, bold=True)
    notes_with_sources(s, "s13")
    return s
