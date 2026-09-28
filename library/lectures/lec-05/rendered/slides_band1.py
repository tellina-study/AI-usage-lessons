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
    eli5_overview, meme_in_box, photo_in_box, check_point, src,
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
             text="Недели работы → часы [1]", size=14, bold=True, color=MID,
             line_spacing=1.02, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 1.18, y=1.30 + fact_h - 0.42, w=lw - 1.40, h=0.34,
             text="внутренний опыт Anthropic", size=10.5, italic=True,
             color=SLATE)
    ocean_box(s, lx, 1.30 + fact_h + 0.16, lw, fact_h, fill=SURFACE,
              stroke=LIGHT, stroke_pt=1.5)
    icon(s, "funnel", lx + 0.24, 1.30 + fact_h + 0.16 + 0.20, 0.80, "teal")
    text_box(s, x=lx + 1.18, y=1.30 + fact_h + 0.16 + 0.16, w=lw - 1.40, h=0.75,
             text="~95% пилотов — ноль отдачи [2]", size=14, bold=True,
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
    refs_of_slide(s, "s01")
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
    ocean_box(s, 0.55, 1.34, 12.25, 3.00, fill=SURFACE, stroke=MID,
              stroke_pt=1.6)
    text_box(s, x=0.85, y=1.44, w=6.0, h=0.30, text="Цикл продукта (Лекция 5)",
             size=13, bold=True, color=MID)
    text_box(s, x=0.85, y=1.74, w=6.0, h=0.30,
             text="откуда берётся уверенность, что стоит писать этот код",
             size=11, italic=True, color=SLATE)
    # GATE-B fix (audit 2026-09-07): the upper-left quadrant of this box used
    # to be ~45-50% blank — "Цикл продукта" was only NAMED, never SHOWN. Add
    # a compact 6-node mini-loop (small-scale reuse of the s03 icon-loop
    # pattern) so the thesis box's own hero content — the loop itself — is
    # visible here, not just in the caption line below it. This is the
    # lecture's highest-stakes bridge slide (central-question payload).
    import math
    mcx, mcy, mr = 2.05, 2.78, 0.66
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
        circle(s, nx - 0.20, ny - 0.20, 0.40, WHITE, stroke=MID, stroke_pt=1.2)
        icon(s, ic, nx - 0.125, ny - 0.125, 0.25, "mid")
    chip(s, 3.35, 2.57, 1.05, 0.42, "6 фаз", fill=GOLD, color=DEEP, size=12)
    icon(s, "layers", 0.85, 3.74, 0.44, "teal")
    text_box(s, x=1.42, y=3.70, w=5.35, h=0.55,
             text="исследование → дизайн → сборка/запуск → измерение → "
                  "эксплуатация → управление → снова исследование",
             size=11, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
    # inner small loop box nested inside "build" area
    ocean_box(s, 7.05, 1.80, 5.50, 2.10, fill=WHITE, stroke=GOLD,
              stroke_pt=1.8)
    icon(s, "git-branch", 7.30, 2.00, 0.46, "teal")
    text_box(s, x=7.90, y=2.00, w=4.45, h=0.30,
             text="Цикл кода (Лекция 4)", size=12.5, bold=True, color=DEEP)
    text_box(s, x=7.90, y=2.34, w=4.45, h=0.30,
             text="как надёжно писать код с ИИ", size=11, italic=True,
             color=SLATE)
    text_box(s, x=7.30, y=2.90, w=5.05, h=0.80,
             text="спека → ADR → план → PR → инцидент",
             size=13, italic=True, color=MID, line_spacing=1.2,
             anchor=MSO_ANCHOR.TOP)

    # ПРАВКА #212: несущая мысль слайда (формулировка владельца) — она же
    # первая строка Body в slides/s04-*.md, поэтому занимает золотой слот.
    # Прежний золотой текст про «единицу работы» живёт в заметках докладчика.
    gold_callout(
        s, 0.55, 4.46, 12.25, 0.90,
        "Чтобы пользовательская ценность состоялась — то есть продукт "
        "работал, был внедрён и кем-то выбран, — цикл кода приходится "
        "обернуть в ещё один цикл. Без внешнего цикла выходит собранное и "
        "никем не используемое: код есть, продукта нет.",
        size=13, bold=True)

    ocean_box(s, 0.55, 5.42, 12.25, 1.52)
    text_box(s, x=0.85, y=5.52, w=11.65, h=1.32,
             text="Когда ИИ сделал сборку почти бесплатной — что стало "
                  "настоящим узким местом продукта, и на каждой фазе цикла: "
                  "какая классическая дисциплина остаётся, что ИИ ускоряет, "
                  "и где AI-first ломается?",
             size=16.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.16)
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
        sid="s07", tag="1 база · 2 практики · 2 провала",
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
             text="Стив Бланк — методология Customer Development [1]",
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
    refs_of_slide(s, "s08")
    notes_with_sources(s, "s08")
    return s


# ============================================================
# s09 - BASE-2: The Mom Test (3 rules + contrast)
# ============================================================
def s09(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Даже мать соврёт — если вопрос сконструирован неправильно [1]",
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
    y0 = 1.48
    for i, (ic, head, body) in enumerate(rules):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 1.72)
        icon(s, ic, x + 0.24, y0 + 0.14, 0.46, "mid")
        text_box(s, x=x + 0.24, y=y0 + 0.70, w=cw - 0.48, h=0.48, text=head,
                 size=13, bold=True, color=DEEP, line_spacing=1.05)
        text_box(s, x=x + 0.24, y=y0 + 1.18, w=cw - 0.48, h=0.48, text=body,
                 size=10.5, italic=True, color=SLATE, line_spacing=1.05)

    # contrast: bad vs good question
    by = 3.32
    filled_rect(s, 0.55, by, 5.95, 1.12, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.07)
    text_box(s, x=0.80, y=by + 0.11, w=5.45, h=0.32, text="Плохо",
             size=12, bold=True, color=SLATE)
    text_box(s, x=0.80, y=by + 0.46, w=5.45, h=0.58,
             text="«Заплатили бы $20 в месяц?»", size=13.5, italic=True,
             color=SLATE, line_spacing=1.1)
    filled_rect(s, 6.75, by, 6.05, 1.12, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.6, radius=True, radius_adj=0.07)
    text_box(s, x=7.00, y=by + 0.11, w=5.55, h=0.32, text="Хорошо",
             size=12, bold=True, color=TEAL)
    text_box(s, x=7.00, y=by + 0.46, w=5.55, h=0.58,
             text="«Сколько вы платите сегодня за ближайший аналог?»",
             size=13.5, bold=True, color=DEEP, line_spacing=1.1)

    # ПРАВКА #212: определение JTBD вынесено в видимый слой (правило курса —
    # определение доставлено, только если оно на слайде или в речи).
    # Прежняя золотая плашка (качественное vs количественное) целиком
    # сохранена в заметках докладчика.
    gold_callout(
        s, 0.55, 4.58, 12.25, 0.92,
        "JTBD (Jobs-to-be-Done), «работа, на которую нанимают продукт» — "
        "смежная рамка Кристенсена: спрашиваем не о предпочтениях, а об "
        "обстоятельстве последней покупки, и получаем таймлайн решения, а не "
        "список мнений.",
        size=12.5, bold=True)

    check_point(
        s, 0.55, 5.64, 12.25,
        "«Как вам идея — ассистент, который сам разбирает вашу почту?» "
        "Какое из трёх правил нарушил этот вопрос и как переспросить, "
        "чтобы получить факт?",
        h=0.88, size=12.5)
    refs_of_slide(s, "s09")
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
         "Perplexity Deep Research: 2 часа → ~30 минут [1]"),
        ("layout-list", "Синтез интервью",
         "Dovetail — кластеризация болей в масштабе [2]"),
        ("database", "Reference dataset (эталонный набор)",
         "курируемая коллекция «запрос → правильный ответ»"),
    ]
    cw, gap = 3.95, 0.20
    x0 = 0.55
    y0 = 1.48
    for i, (ic, head, body) in enumerate(blocks):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 1.95)
        icon(s, ic, x + 0.24, y0 + 0.18, 0.52, "mid")
        text_box(s, x=x + 0.24, y=y0 + 0.82, w=cw - 0.48, h=0.48, text=head,
                 size=12, bold=True, color=MID, line_spacing=1.05)
        text_box(s, x=x + 0.24, y=y0 + 1.34, w=cw - 0.48, h=0.52, text=body,
                 size=11, color=DEEP, line_spacing=1.10)
        if i == 0:
            chip(s, x + cw - 1.55, y0 + 0.18, 1.30, 0.36, "проверь источник",
                 fill=GOLD, color=DEEP, size=9)

    gold_callout(
        s, 0.55, 3.62, 12.25, 0.70,
        "97% исследователей используют ИИ — лишь ~8% доверяют ИИ-персонам "
        "как данным [3]",
        size=14.5, bold=True, align=PP_ALIGN.CENTER)

    filled_rect(s, 0.55, 4.46, 12.25, 1.28, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    text_box(s, x=0.85, y=4.56, w=11.65, h=1.08,
             text="Обязательная практика: проверять важные данные напрямую "
                  "по источнику до использования в решении. Синтетические "
                  "пользователи — только пре-исследование (пилотаж гайда, "
                  "черновик персон, генерация гипотез), никогда не "
                  "доказательство для решения «продолжать/остановить».",
             size=12.5, color=DEEP, line_spacing=1.15,
             anchor=MSO_ANCHOR.MIDDLE)

    check_point(
        s, 0.55, 5.90, 12.25,
        "ИИ-персона прошла ваш сценарий знакомства с продуктом целиком и "
        "назвала функцию отличной. Что в устройстве такого источника мешает "
        "ему сказать «нет»?",
        h=0.88, size=12.5)
    refs_of_slide(s, "s10")
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

    # LEFT: «зеркало согласия» + ПРАВКА #212 — количественная оценка
    # подхалимства (раньше на слайде не было ни одной цифры).
    lx, lw = 0.55, 4.55
    ocean_box(s, lx, 1.48, lw, 3.88, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    icon(s, "smile", lx + lw / 2 - 0.42, 1.64, 0.84, "light")
    text_box(s, x=lx + 0.25, y=2.58, w=lw - 0.50, h=0.34,
             text="Зеркало согласия", size=14, bold=True, color=MID,
             align=PP_ALIGN.CENTER)
    stats = [("72–91%", "при явном согласии", GOLD),
             ("7–28%", "при явном несогласии", LIGHT)]
    for i, (num, lbl, col) in enumerate(stats):
        sx = lx + 0.22 + i * 2.10
        filled_rect(s, sx, 3.02, 1.90, 0.98,
                    (GOLD_TINT if i == 0 else SURFACE), stroke=col,
                    stroke_pt=1.6, radius=True, radius_adj=0.10)
        text_box(s, x=sx, y=3.10, w=1.90, h=0.48, text=num, size=21,
                 bold=True, color=(DEEP if i == 0 else col),
                 align=PP_ALIGN.CENTER)
        text_box(s, x=sx + 0.05, y=3.60, w=1.80, h=0.34, text=lbl, size=9.5,
                 color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.0)
    text_box(s, x=lx + 0.25, y=4.12, w=lw - 0.50, h=0.86,
             text="Сдвиг тона ответа модели к позитиву («feedback positivity», "
                  "5 моделей) — это не «частота отрицательного ответа».",
             size=11, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.14)
    src(s, lx + 0.25, 5.00, lw - 0.50,
        "Sharma и др., 2023 — Figure 1, ICLR 2024", size=9.5,
        align=PP_ALIGN.CENTER)

    rx, rw = 5.35, 7.45
    crit = [
        "Высокая цена ошибки «продолжать/остановить»",
        "Нужно реальное прошлое, не правдоподобное",
        "Нужна валидация обязательством, не мнением",
    ]
    text_box(s, x=rx, y=1.48, w=rw, h=0.40,
             text="Когда живое интервью строго лучше ИИ-синтеза", size=14,
             bold=True, color=MID)
    for i, c in enumerate(crit):
        y = 1.98 + i * 0.82
        ocean_box(s, rx, y, rw, 0.68, fill=SURFACE, stroke=MID, stroke_pt=1.3)
        text_box(s, x=rx + 0.65, y=y, w=rw - 0.85, h=0.68, text=f"{i+1}. {c}",
                 size=13, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        icon(s, "shield-alert", rx + 0.14, y + 0.14, 0.40, "mid")
    text_box(s, x=rx, y=4.52, w=rw, h=0.84,
             text="У синтетического собеседника нет реального прошлого, "
                  "способного противоречить формулировке вопроса, — поэтому "
                  "несогласие он не производит в принципе.",
             size=12.5, color=DEEP, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.56, 12.25, 0.92,
        "ИИ-резюме теряет 20-40% деталей интервью (Torres) [1], если пропущен "
        "шаг «сначала по отдельности» — прослеживаемый до конкретного шага "
        "сбой, не расплывчатое «ИИ иногда ошибается».",
        size=13, bold=True)
    refs_of_slide(s, "s11")
    notes_with_sources(s, "s11")
    return s


# ============================================================
# s12 - FAILURE on-point #1: synthetic users (NN/g)
# ============================================================
def s12(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Одна и та же задача: реальные люди — 3 из 7, синтетическая панель — 7 из 7 [1]",
        size=20, w=12.2, h=0.85)

    # LEFT: real meme (Trade Offer — GATE-B fix, replaces Surprised Pikachu:
    # lec-2 collision + weak affect-fit, see arc-meme-layout-audit.md) — the
    # false 7/7 "offer" vs the 3/7 that actually decides
    from _helpers import meme_in_box
    meme_in_box(s, "s12-trade-offer.jpg", 0.55, 1.55, 4.55, 3.15, pad=0.14)

    # RIGHT: split comparison 3/7 vs 7/7
    rx, rw = 5.35, 7.45
    text_box(s, x=rx, y=1.52, w=rw, h=0.38,
             text="NN/g: контролируемое сравнение на сценарии знакомства "
                  "с продуктом",
             size=12.5, bold=True, color=MID, line_spacing=1.05)
    ocean_box(s, rx, 1.98, rw, 1.05, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=rx + 0.24, y=2.06, w=3.0, h=0.36,
             text="Реальные люди", size=12.5, bold=True, color=MID)
    for i in range(7):
        cxx = rx + 0.28 + i * 0.42
        ok = i < 3
        icon(s, "check-check" if ok else "x", cxx, 2.45, 0.36,
             "mid" if ok else "light")
    text_box(s, x=rx + 3.35, y=2.18, w=rw - 3.6, h=0.7,
             text="3 из 7 — «надуманно и бесполезно»", size=12, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)

    ocean_box(s, rx, 3.18, rw, 1.05, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.8)
    text_box(s, x=rx + 0.24, y=3.26, w=3.0, h=0.36,
             text="Синт-панель", size=12.5, bold=True, color=DEEP)
    for i in range(7):
        cxx = rx + 0.28 + i * 0.42
        icon(s, "check-check", cxx, 3.65, 0.36, "gold")
    text_box(s, x=rx + 3.35, y=3.38, w=rw - 3.6, h=0.7,
             text="7 из 7 — «меняет правила игры»", size=12, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    text_box(s, x=rx, y=4.36, w=rw, h=0.38,
             text="Одна и та же фича — противоположные вердикты",
             size=12.5, italic=True, color=SLATE)

    gold_callout(
        s, 0.55, 5.12, 12.25, 1.05,
        "Критерий: синтетический выход дисквалифицирован для решения "
        "«продолжать/остановить» по построению, а не из-за невезения "
        "прогона. Альтернатива: до-исследовательская роль + реальное "
        "тестирование 5-8 участников.",
        size=13, bold=True)
    refs_of_slide(s, "s12")
    notes_with_sources(s, "s12")
    return s


# ============================================================
# s13a - FAILURE on-point #3: IBM Watson for Oncology
# ============================================================
def s13a(p):
    """ПРАВКА #212: тип слайда сменён case_study -> comparison. Глава §1.9
    переписана как ДВА НЕЗАВИСИМЫХ провала одной корпорации с разными
    корневыми причинами (данные vs управление проектом); две равные колонки
    передают это точнее, чем одна линейная история про «$62 млн».
    Колонка A — Primary mid, колонка B — Teal: два механизма отказа должны
    читаться как разные, а не как оттенки одного."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Один бренд, два провала: данные подвели одну систему, "
                   "закупка — другую",
                size=19, w=12.3, h=0.62, y=0.36)

    chip(s, 0.55, 1.14, 2.95, 0.42, "IBM Watson Health", fill=MID,
         color=WHITE, size=13)

    cols = [
        dict(x=0.55, stroke=MID, tint=MID_TINT, ivar="mid", icn="flask-conical",
             head="Случай A — Watson for Oncology",
             sub="Memorial Sloan Kettering, с 2012",
             bullets=[
                 "Коммерческий запуск 2015; внутренние документы: "
                 "рекомендации «небезопасные и некорректные»",
                 "Бевацизумаб гипотетическому пациенту с активным "
                 "кровотечением — вопреки предупреждению производителя",
             ],
             cause="Причина: обучен на малом числе синтетических, "
                   "гипотетических кейсов горстки онкологов MSK — не на "
                   "реальных исходах [2]",
             ccol=MID,
             stat="STAT News · 25 июля 2018 [1]", stat_gold=False),
        dict(x=6.75, stroke=TEAL, tint=TEAL_TINT, ivar="teal",
             icn="file-warning",
             head="Случай B — Oncology Expert Advisor",
             sub="MD Anderson, 2013–2016",
             bullets=[
                 "Контракт через 12 продлений вырос с $2,4 млн до "
                 "$39,2 млн IBM + $23 млн PwC",
                 "Закрыт в сентябре 2016 — без единого пролеченного пациента",
             ],
             cause="Причина по аудиту University of Texas System: обход "
                   "конкурсных закупочных процедур + дефицит донорского "
                   "финансирования ≈ $11,6 млн — не про данные и не про "
                   "модель",
             ccol=TEAL,
             stat="≈ $62 млн  →  0 пациентов", stat_gold=True),
    ]
    cw = 6.05
    for c in cols:
        x = c["x"]
        ocean_box(s, x, 1.70, cw, 3.60, fill=SURFACE, stroke=c["stroke"],
                  stroke_pt=1.6)
        icon(s, c["icn"], x + 0.24, 1.86, 0.50, c["ivar"])
        text_box(s, x=x + 0.86, y=1.86, w=cw - 1.10, h=0.32, text=c["head"],
                 size=13, bold=True, color=c["ccol"], line_spacing=1.05)
        text_box(s, x=x + 0.86, y=2.19, w=cw - 1.10, h=0.28, text=c["sub"],
                 size=10.5, italic=True, color=SLATE, line_spacing=1.0)
        by = 2.56
        for b in c["bullets"]:
            text_box(s, x=x + 0.26, y=by, w=cw - 0.52, h=0.56, text="• " + b,
                     size=11.5, color=DEEP, line_spacing=1.14)
            by += 0.60
        filled_rect(s, x + 0.26, 3.80, cw - 0.52, 0.42,
                    (GOLD_TINT if c["stat_gold"] else WHITE),
                    stroke=(GOLD if c["stat_gold"] else LIGHT),
                    stroke_pt=(1.6 if c["stat_gold"] else 1.0), radius=True,
                    radius_adj=0.14)
        text_box(s, x=x + 0.26, y=3.80, w=cw - 0.52, h=0.42, text=c["stat"],
                 size=(14 if c["stat_gold"] else 11), bold=c["stat_gold"],
                 italic=(not c["stat_gold"]),
                 color=(DEEP if c["stat_gold"] else SLATE),
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        filled_rect(s, x + 0.26, 4.32, cw - 0.52, 0.86, c["tint"],
                    stroke=c["stroke"], stroke_pt=1.2, radius=True,
                    radius_adj=0.09)
        text_box(s, x=x + 0.42, y=4.36, w=cw - 0.84, h=0.78, text=c["cause"],
                 size=10.5, bold=True, color=DEEP, line_spacing=1.10,
                 anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.50, 12.25, 0.94,
        "Два независимых механизма отказа одной корпорации: непригодные "
        "данные против несостоятельного управления проектом. Не всякий "
        "дорогой провал с ИИ на обложке объясняется самим ИИ.",
        size=13, bold=True)
    refs_of_slide(s, "s13a")
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
        "Ссылки на несуществующие статьи + сфабрикованная цитата суда [1]",
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
                  "цитатами, ~90% — в 2025 году [2]",
             size=12, color=DEEP, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.10, 12.25, 0.95,
        "Урок: вывод модели в discovery-фазе — неверифицированный черновик, "
        "не источник фактов. Критерий: итоговый документ внешнему заказчику "
        "требует 100% проверки каждой ссылки, не выборочной.",
        size=12.5, bold=True)
    refs_of_slide(s, "s13")
    notes_with_sources(s, "s13")
    return s
