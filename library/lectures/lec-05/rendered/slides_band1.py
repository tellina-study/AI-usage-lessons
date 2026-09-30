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
        s, "Сборка стала почти бесплатной — и почти никто не превратил это в пользу",
        size=21, w=12.2, h=0.80, y=0.30)

    # GATE-B fix: hero meme was only ~16.5% of slide area (4.65x3.55 in a
    # split layout) — under the 40% hero mandate. Rebuilt as a dominant
    # right-side hero (7.65x5.30 = ~40.5% of the 13.333x7.5 canvas) with the
    # two-fact metaphor compressed into a narrow left column instead of a
    # second equal-weight box, so the meme is unambiguously the hero, not a
    # co-equal panel.
    # ПРАВКА #212: высоты подобраны под РЕАЛЬНУЮ длину подписи-источника —
    # у второго факта она в три строки (добавлен знаменатель: доля от всех
    # организаций, а не от дошедших до пилота), поэтому его рамка выше первой.
    # Равные высоты выдавливали последнюю строку за границу рамки.
    lx, lw = 0.55, 4.35
    ocean_box(s, lx, 1.26, lw, 1.28, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    icon(s, "clock", lx + 0.24, 1.26 + 0.24, 0.78, "mid")
    text_box(s, x=lx + 1.18, y=1.34, w=lw - 1.40, h=0.52,
             text="Недели работы → часы [1]", size=14, bold=True, color=MID,
             line_spacing=1.02, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 1.18, y=1.94, w=lw - 1.40, h=0.32,
             text="внутренний опыт Anthropic", size=10.5, italic=True,
             color=SLATE)
    ocean_box(s, lx, 2.68, lw, 1.92, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    icon(s, "funnel", lx + 0.24, 2.68 + 0.24, 0.78, "teal")
    text_box(s, x=lx + 1.18, y=2.78, w=lw - 1.40, h=0.76,
             text="~95% организаций — нулевая отдача [2]", size=14, bold=True,
             color=TEAL, line_spacing=1.02, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 1.18, y=3.58, w=lw - 1.40, h=0.94,
             text="Массачусетский технологический институт, лето 2025 — "
                  "доля от всех организаций, а не от дошедших до пилота",
             size=9.5, italic=True, color=SLATE, line_spacing=1.06)
    gold_callout(
        s, lx, 4.76, lw, 2.02,
        "Оба факта правдивы одновременно: сборка стала почти бесплатной, а "
        "превращение сборки в ценность — нет. Разрыв между ними и есть "
        "предмет лекции; он разрешится в самом конце.",
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
    # ПРАВКА #212: петля поднята (cy 2.85 → 2.55), иначе подпись нижнего узла
    # «Измерение» уходила под рамку мема, которую пришлось сузить по картинке.
    cx, cy, r = 3.15, 2.55, 1.55
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
    meme_in_box(s, "s02-one-does-not-simply.jpg", 1.52, 4.92, 3.35, 1.48,
                pad=0.10)

    # title block, right. ПРАВКА #212: колонка расширена (6.40 → 7.25) и кегль
    # снижен (30 → 27) — русский заголовок «ИИ-продукт…» длиннее прежнего
    # латинского и в старую рамку не помещался: он налезал на строку с
    # раскрытием аббревиатуры и на золотую плашку.
    rx, rw = 5.78, 7.25
    text_box(s, x=rx, y=1.34, w=rw, h=0.48, text="ЛЕКЦИЯ 5",
             size=20, bold=True, color=TEAL)
    text_box(s, x=rx, y=1.86, w=rw, h=1.92,
             text="ИИ-продукт: полный жизненный цикл — от намерения до эксплуатации",
             size=27, bold=True, color=DEEP, line_spacing=1.05)
    text_box(s, x=rx + 0.03, y=3.84, w=rw - 0.06, h=0.34,
             text="ИИ — искусственный интеллект", size=13, bold=True,
             color=TEAL)
    text_box(s, x=rx + 0.03, y=4.22, w=rw - 0.06, h=0.40,
             text="Курс «Осознанное применение ИИ» · инженеры-студенты 3 курса",
             size=13.5, italic=True, color=LIGHT)
    gold_callout(
        s, rx, 4.76, rw, 0.90,
        "Шесть разделов — шесть стрелок одной петли. Код из Лекции 4 — один "
        "шаг внутри неё, и теперь самый дешёвый из всех.",
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
        ("search", "1. Исследование", "откуда берётся гипотеза"),
        ("pencil", "2. Дизайн", "гипотеза становится артефактом"),
        ("hammer", "3. Сборка и запуск", "артефакт становится продуктом"),
        ("ruler", "4. Измерение", "сработало ли это на самом деле"),
        ("headphones", "5. Поддержка", "работает без остановки"),
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
        # ПРАВКА #212: замыкающее ребро названо в золотой плашке словами
        # («золотая стрелка возврата»), поэтому оно обязано читаться как
        # стрелка: меньше подрезка, заметно большая толщина. Прежние 2.6pt
        # при подрезке 0.62 с каждой стороны оставляли золотой огрызок.
        is_return = (i == 5)  # Управление(5) -> Исследование(0)
        pad = 0.50 if is_return else 0.62
        sx1, sy1 = x1 + ux * pad, y1 + uy * pad
        sx2, sy2 = x2 - ux * pad, y2 - uy * pad
        connector(s, sx1, sy1, sx2, sy2,
                  color=(GOLD if is_return else LIGHT),
                  width=(5.5 if is_return else 2.2),
                  arrow_end=True)
        if is_return:
            # подпись ровно у этого ребра, снаружи кольца (Р4: на схеме
            # не должно быть линии, про которую непонятно, что она значит)
            mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
            ox, oy = mx - cx, my - cy
            on = (ox ** 2 + oy ** 2) ** 0.5 or 1.0
            lx2, ly2 = mx + ox / on * 0.55, my + oy / on * 0.55
            text_box(s, x=lx2 - 0.48, y=ly2 - 0.15, w=0.96, h=0.30,
                     text="возврат", size=10, bold=True, color=GOLD,
                     align=PP_ALIGN.CENTER)
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
        y = 1.50 + i * 0.68
        text_box(s, x=rx, y=y, w=rw, h=0.56,
                 text=f"{name} — {desc}", size=13, bold=True, color=DEEP,
                 line_spacing=1.0)
    gold_callout(
        s, 7.15, 5.42, 5.65, 1.18,
        "Золотая стрелка возврата: управление снова питает исследование. "
        "Это замкнутая петля, а не одноразовый линейный процесс — поэтому "
        "карта нарисована кругом.",
        size=12.5, bold=True)
    notes_with_sources(s, "s03")
    return s


# ============================================================
# s04 - ПЕРЕСОБРАН (issue #212): «зачем продукту цикл и что без него»
# Прежний слайд (мост из Лекции 4 + центральный вопрос) забракован
# владельцем: «ценность не понятна, кроме как сказать, что используем то,
# что было в лекции 4». Содержание взято из chapter.md §0.3a — раздела,
# которого на слайдах не было вовсе. Мост из Лекции 4 сжат до одной
# подчинённой строки под заголовком; центральный вопрос переехал на s06.
# ============================================================
def s04(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Зачем продукту цикл: без него ошибку находят слишком поздно",
                size=22, w=12.25, h=0.66, y=0.24)
    # мост из Лекции 4 — подчинённая строка, а не смысл слайда. Аббревиатуры
    # ADR / PR раскрыты словами (Р5): «архитектурное решение», «запрос на
    # слияние» — голая латиница на видимом слое недопустима.
    text_box(s, x=0.55, y=0.94, w=12.25, h=0.36,
             text="Цикл кода из Лекции 4 — спецификация, архитектурное "
                  "решение, план, запрос на слияние, запись об инциденте — "
                  "целиком лежит внутри одной из этих фаз, «сборки и запуска».",
             size=11.5, italic=True, color=SLATE, line_spacing=1.04)

    # ── левая колонка: пять вопросов ↔ фазы (связка с картой лекции s03) ──
    lx, lw = 0.55, 6.10
    text_box(s, x=lx, y=1.36, w=lw, h=0.46,
             text="Пять вопросов, на которые продукт отвечает наблюдением, а не мнением",
             size=11.5, bold=True, color=TEAL, line_spacing=1.02)
    questions = [
        ("Нужно ли это кому-то вообще", "фаза 1 · исследование"),
        ("Сможет ли человек этим воспользоваться и не пострадает ли тот, "
         "о ком не подумали", "фаза 2 · дизайн"),
        ("Можем ли мы это сделать и безопасно выпустить",
         "фаза 3 · сборка и запуск"),
        ("Выберут ли это настолько, чтобы за это платить",
         "фазы 4 и 6 · измерение, управление"),
        ("Держатся ли эти ответы через квартал", "фаза 5 · поддержка"),
    ]
    for i, (q, phase) in enumerate(questions):
        y = 1.86 + i * 0.64
        ocean_box(s, lx, y, lw, 0.60, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.3)
        circle(s, lx + 0.16, y + 0.15, 0.30, MID)
        text_box(s, x=lx + 0.16, y=y + 0.17, w=0.30, h=0.28, text=str(i + 1),
                 size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        text_box(s, x=lx + 0.58, y=y + 0.02, w=lw - 0.76, h=0.38, text=q,
                 size=11, bold=True, color=DEEP, line_spacing=0.96,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=lx + 0.58, y=y + 0.38, w=lw - 0.76, h=0.20, text=phase,
                 size=9.5, italic=True, color=TEAL)
    text_box(s, x=lx + 0.04, y=5.10, w=lw - 0.08, h=0.70,
             text="Первые четыре — риски продукта по Марти Кагану; пятый "
                  "открывается только после запуска. У каждого своя фаза: "
                  "цикл и есть минимальный набор мест, где на эти вопросы "
                  "отвечают.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.08)

    # ── правая колонка: механизм отсутствия цикла, три подписанные рамки ──
    rx, rw = 6.95, 5.85

    def framed(y, h, head, body, *, stroke=MID, body_size=11, head_color=TEAL):
        ocean_box(s, rx, y, rw, h, fill=SURFACE, stroke=stroke, stroke_pt=1.4)
        text_box(s, x=rx + 0.22, y=y + 0.08, w=rw - 0.44, h=0.30, text=head,
                 size=12.5, bold=True, color=head_color)
        text_box(s, x=rx + 0.22, y=y + 0.42, w=rw - 0.44, h=h - 0.52,
                 text=body, size=body_size, color=DEEP, line_spacing=1.10)

    framed(1.36, 1.72, "Когда цикла нет",
           "Вопросы не исчезают — их место занимают допущения, обычно "
           "оптимистичные.\n"
           "Ошибка тоже не исчезает — сдвигается только момент, когда её "
           "находят.\n"
           "Находят её после того, как сборка оплачена, релиз состоялся, "
           "а откат стоит дороже самой ошибки.")
    framed(3.16, 1.48, "Цена позднего обнаружения",
           "От требований до выпуска стоимость исправления расходится до ста "
           "раз в крупных проектах и примерно вчетверо в небольших (Барри "
           "Боэм, 1981).\n"
           "Цикл не устраняет ошибку в гипотезе: он двигает её обнаружение "
           "туда, где она стоит разговор, а не сборку.",
           body_size=10.5)
    framed(4.72, 1.14, "Изнутри команды это не выглядит провалом",
           "Собрали — никто не пользуется · дошли до пилота и застряли · "
           "работает, но не выбрано · внедрили, а через квартал перестали "
           "открывать. Сборка во всех четырёх случаях прошла успешно.",
           stroke=TEAL, body_size=10.5)

    gold_callout(
        s, 0.55, 5.92, 12.25, 0.98,
        "Дороговизна сборки работала невольным заслоном: пока изготовление "
        "стоило недели, оно само заставляло думать заранее. Искусственный "
        "интеллект обнулил именно её — и у команд, у которых явного цикла не "
        "было никогда, не осталось ничего, что удерживало бы от пропуска "
        "этих вопросов. Воронка из начала лекции — 60% организаций пробуют, "
        "20% доходят до пилота, 5% внедряют — не парадокс, а следствие.",
        size=12, bold=True)
    notes_with_sources(s, "s04")
    return s


# ============================================================
# s06 - KEYSTONE: асимметрия стоимости и доверия (несущая ось лекции)
# issue #212: s05 (петля + три первоисточника) снят владельцем как повтор
# уже введённой идеи; его несущий аргумент сжат здесь в одну подписанную
# строку. Центральный вопрос лекции переехал сюда с s04 и переписан
# утверждением — вопросов на слайдах не остаётся (Р2).
# ============================================================
def s06(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Искусственный интеллект меняет каждую стрелку — но не одинаково",
                size=22, w=12.25, h=1.00, y=0.24)

    rows = [
        ("hammer", "Строить", "фаза сборки и запуска",
         "стоимость упала почти до нуля: черновик кода, макета, плана "
         "исследования", GOLD, "gold"),
        ("ruler", "Измерять и делать выводы", "фаза измерения",
         "стоимость та же, а доверие к результату упало: сам инструмент "
         "измерения стал вероятностным", LIGHT, "light"),
        ("eye", "Наблюдать за работой продукта", "фаза поддержки",
         "наблюдать стало быстрее, но само наблюдение уязвимо: подменённые "
         "данные на входе ведут к уверенному неверному выводу", TEAL, "teal"),
    ]
    for i, (ic, name, phase, desc, col, av) in enumerate(rows):
        y = 1.30 + i * 0.94
        ocean_box(s, 0.55, y, 12.25, 0.82, fill=SURFACE, stroke=col,
                  stroke_pt=1.6)
        icon(s, ic, 0.80, y + 0.18, 0.46, av)
        # ПРАВКА #212: имя строки получило собственную высоту под две строки,
        # подпись фазы опущена под него — прежде «Наблюдать за работой
        # продукта» переносилось и налезало на «фаза поддержки».
        text_box(s, x=1.44, y=y + 0.05, w=3.95, h=0.40, text=name, size=13.5,
                 bold=True, color=DEEP, line_spacing=0.96,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=1.44, y=y + 0.48, w=3.95, h=0.26, text=phase, size=9.5,
                 italic=True, color=TEAL)
        text_box(s, x=5.52, y=y + 0.10, w=7.05, h=0.62, text=desc, size=12.5,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.08)

    # сжатый аргумент снятого s05 — одна подписанная строка, без схемы
    filled_rect(s, 0.55, 4.10, 12.25, 0.72, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.10)
    text_box(s, x=0.85, y=4.18, w=11.65, h=0.58,
             text="Одну и ту же петлю независимо описали трижды: в статистике "
                  "качества (Деминг, 1939), в военной авиации (Бойд, 1970-е) "
                  "и в стартапах (Райс, 2011). Это структурное свойство любой "
                  "системы, которая учится в неопределённости, а не "
                  "методология одного автора.",
             size=11, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.08)

    gold_callout(
        s, 0.55, 4.92, 12.25, 0.94,
        "Мета-паттерн всех шести разделов: у каждой стрелки есть классическая "
        "дисциплина, и искусственный интеллект её не отменяет. Он меняет, "
        "сколько эта дисциплина стоит и насколько ей можно верить без "
        "проверки.",
        size=13, bold=True)

    ocean_box(s, 0.55, 5.98, 12.25, 0.88, fill=WHITE, stroke=MID,
              stroke_pt=1.6)
    text_box(s, x=0.85, y=6.06, w=11.65, h=0.72,
             text="Каждая из шести фаз дальше разбирается по одной и той же "
                  "схеме: какая классическая дисциплина за неё отвечает, что "
                  "в ней удешевил искусственный интеллект, и где подход "
                  "«сначала ИИ» ломается.",
             size=13, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.12)
    notes_with_sources(s, "s06")
    return s


# ============================================================
# s07 - section divider Р1 Discovery
# ============================================================

def s07(p):
    return build_section_divider(
        p, here_idx=1,
        subtitle="Исследование — есть ли проблема и у кого",
        bridge="Цель фазы одна: выяснить, существует ли проблема и у кого "
               "именно, пока решение ещё не построено. Пропустить её можно — "
               "тогда ответ придёт в день запуска, когда деньги и месяцы уже "
               "потрачены, а вернуть их нечем.",
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
    """ПРАВКА #212 (замечания владельца): раздел начинается с цели и
    необходимости работы (Р3), неподписанные ромбики и голая аббревиатура
    BML сняты (Р4/Р5), место дисциплины относительно петли лекции названо
    прямо — это был буквальный вопрос владельца «альтернатива циклу
    создания продукта или что?». Билдер приведён к slides/s08-*.md."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Проверить гипотезу стоит нескольких разговоров — "
                   "не проверить стоит всей разработки",
                size=21, w=12.25, h=0.78, y=0.13)

    # ── ЗАЧЕМ ЭТА РАБОТА ──────────────────────────────────────────────
    filled_rect(s, 0.55, 1.02, 12.25, 0.86, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.6, radius=True, radius_adj=0.08)
    icon(s, "target", 0.78, 1.24, 0.42, "teal")
    text_runs(s, 1.38, 1.06, 11.28, 0.78, [
        {"text": "ЗАЧЕМ ЭТА РАБОТА   ", "size": 10.5, "bold": True,
         "color": TEAL},
        {"text": "Исследование отвечает на один вопрос: существует ли "
                 "проблема и у кого именно. Ответ придёт в любом случае — "
                 "либо от восьми разговоров за две недели, либо от рынка в "
                 "день запуска, когда разработка уже оплачена.",
         "size": 12.5, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.14)

    # ── Слева: названная дисциплина + формат гипотезы ─────────────────
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.98, lw, 3.05, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    icon(s, "compass", lx + 0.24, 2.12, 0.46, "mid")
    text_box(s, x=lx + 0.84, y=2.12, w=lw - 1.08, h=0.58,
             text="Развитие клиента (Customer Development)", size=13,
             bold=True, color=MID, line_spacing=1.06)
    src(s, lx + 0.84, 2.56, lw - 1.08,
        "Стив Бланк — дисциплина поиска ответа «что и для кого строить»",
        size=9.5)
    text_box(s, x=lx + 0.26, y=2.92, w=lw - 0.52, h=0.98,
             text="Правило, ради которого она существует: внутри офиса "
                  "фактов нет, факты снаружи. Но выйти наружу мало: без "
                  "записанной заранее гипотезы возвращаются с впечатлениями, "
                  "подтверждающими то, во что верили до выхода.",
             size=11, color=DEEP, line_spacing=1.14)
    ocean_box(s, lx + 0.22, 3.96, lw - 0.44, 0.60, fill=GOLD_TINT,
              stroke=GOLD, stroke_pt=1.6)
    text_box(s, x=lx + 0.30, y=3.96, w=lw - 0.60, h=0.60,
             text="мы верим X → проверим через Y → к дате Z получим ответ "
                  "да или нет",
             size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.08)
    text_box(s, x=lx + 0.26, y=4.62, w=lw - 0.52, h=0.36,
             text="Дата — не оформление: без неё «проверим» не имеет срока.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.05)

    # ── Справа: два правила разговора + пара «плохо → хорошо» ─────────
    rx, rw = 6.75, 6.05
    ocean_box(s, rx, 1.98, rw, 3.05, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=rx + 0.26, y=2.12, w=rw - 0.52, h=0.32,
             text="Два правила разговора", size=13, bold=True, color=MID)
    src(s, rx + 0.26, 2.44, rw - 0.52,
        "книга «The Mom Test», Роб Фитцпатрик", size=9.5)
    rules = [
        ("history", "Спрашивать о конкретном прошлом, а не о мнении про "
                    "будущее"),
        ("handshake", "Засчитывать обязательство — время, репутацию, "
                      "деньги, — а не комплимент"),
    ]
    ry = 2.78
    for ic, txt in rules:
        filled_rect(s, rx + 0.26, ry, rw - 0.52, 0.64, WHITE, stroke=LIGHT,
                    stroke_pt=1.2, radius=True, radius_adj=0.12)
        icon(s, ic, rx + 0.42, ry + 0.15, 0.34, "light")
        text_box(s, x=rx + 0.92, y=ry, w=rw - 1.20, h=0.64, text=txt,
                 size=11, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.12)
        ry += 0.74
    ocean_box(s, rx + 0.26, 4.30, rw - 0.52, 0.66, fill=TEAL_TINT,
              stroke=TEAL, stroke_pt=1.4)
    text_runs(s, rx + 0.40, 4.30, rw - 0.80, 0.66, [
        {"text": "Плохо: ", "size": 10.5, "bold": True, "color": SLATE},
        {"text": "«Заплатили бы 20 долларов в месяц?»   →   ", "size": 10.5,
         "color": DEEP},
        {"text": "Хорошо: ", "size": 10.5, "bold": True, "color": TEAL},
        {"text": "«Сколько вы платите сегодня за ближайший аналог?»",
         "size": 10.5, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.12)

    # ── Место дисциплины относительно петли лекции ────────────────────
    gold_callout(
        s, 0.55, 5.18, 12.25, 1.10,
        "Это не альтернатива циклу разработки и не второй процесс рядом с "
        "ним. Цикл отвечает на вопрос «как быстро проверять», эта "
        "дисциплина — на вопрос «что и у кого проверять». Она работает на "
        "первой стрелке петли, до того как что-то построено.",
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
    """ПРАВКА #212 (замечания владельца, Р6/Р7): устаревшие оценки экономии
    времени и состав инструментов заменены практиками 2026 года и поданы
    сравнением «без ИИ / с ИИ» по шагам фазы. ИИ-персоны больше не
    появляются ниоткуда: у них названное место на шкале «кто на том конце
    разговора». Эталонный набор снят — он вводится своим слайдом в
    Разделе 3 (s24b), здесь он был непонятной отсылкой вперёд."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Что ИИ изменил в исследовании к 2026 году — "
                   "и что не изменил",
                size=22, w=12.25, h=0.58, y=0.13)

    # ── Таблица-сравнение по шагам фазы ───────────────────────────────
    col_x = [0.55, 3.30, 8.00]
    col_w = [2.60, 4.55, 4.80]
    for x, w, t in zip(col_x, col_w, ["ШАГ ФАЗЫ", "БЕЗ ИИ", "С ИИ — 2026"]):
        filled_rect(s, x, 0.82, w, 0.32, MID, radius=True, radius_adj=0.12)
        text_box(s, x=x + 0.08, y=0.82, w=w - 0.16, h=0.32, text=t,
                 size=9.5, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)

    rows = [
        ("file-search", "Кабинетный поиск",
         "собрать, что уже известно о рынке и о боли",
         "Аналитик читает отчёты, публикации и форумы — дни работы",
         "Режим глубокого исследования сам планирует поиск, читает сотни "
         "источников и отдаёт отчёт со ссылками за 2–30 минут. Есть у всех "
         "основных помощников, включая бесплатные тарифы с лимитом"),
        ("headphones", "Сам разговор", "",
         "Каждое интервью исследователь проводит лично; восемь разговоров — "
         "недели календаря",
         "Вопросы задаёт модель, отвечает живой человек — разговоров за тот "
         "же срок кратно больше"),
        ("layout-list", "Сведение разговоров", "",
         "Расшифровка вручную, темы выписываются глазами",
         "Расшифровка стала бесплатным приложением к созвону; инструменты "
         "непрерывно пересобирают темы по всему накопленному корпусу, а не "
         "по одному звонку"),
    ]
    ry = 1.22
    for ic, name, gloss, was, now in rows:
        rh = 0.78
        ocean_box(s, col_x[0], ry, col_w[0], rh, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.3)
        icon(s, ic, col_x[0] + 0.16, ry + 0.10, 0.32, "mid")
        text_box(s, x=col_x[0] + 0.54, y=ry + 0.08, w=col_w[0] - 0.66,
                 h=0.34, text=name, size=11, bold=True, color=MID,
                 line_spacing=1.04)
        if gloss:
            text_box(s, x=col_x[0] + 0.14, y=ry + 0.42, w=col_w[0] - 0.28,
                     h=0.32, text=gloss, size=8.5, italic=True, color=SLATE,
                     line_spacing=1.04)
        ocean_box(s, col_x[1], ry, col_w[1], rh, fill=WHITE, stroke=SOFT_GREY,
                  stroke_pt=1.2)
        text_box(s, x=col_x[1] + 0.16, y=ry, w=col_w[1] - 0.32, h=rh,
                 text=was, size=10, color=SLATE, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.14)
        ocean_box(s, col_x[2], ry, col_w[2], rh, fill=TEAL_TINT, stroke=TEAL,
                  stroke_pt=1.4)
        text_box(s, x=col_x[2] + 0.16, y=ry, w=col_w[2] - 0.32, h=rh,
                 text=now, size=10, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.14)
        ry += rh + 0.08

    # ── Шкала «кто на том конце разговора» ────────────────────────────
    text_box(s, x=0.55, y=3.80, w=12.25, h=0.30,
             text="Кто на том конце разговора", size=12.5, bold=True,
             color=MID)
    lad = [
        ("человек ↔ человек", "классическое интервью", MID, SURFACE),
        ("человек ↔ модель", "спрашивает машина, отвечает живой человек",
         TEAL, TEAL_TINT),
        ("модель ↔ модель",
         "ИИ-персона: отвечает тоже машина — живого человека в цепочке нет "
         "ни разу", GOLD, GOLD_TINT),
    ]
    lw_ = 3.97
    for i, (t1, t2, col, fill) in enumerate(lad):
        x = 0.55 + i * (lw_ + 0.17)
        ocean_box(s, x, 4.14, lw_, 0.86, fill=fill, stroke=col, stroke_pt=1.7)
        text_box(s, x=x + 0.12, y=4.20, w=lw_ - 0.24, h=0.28, text=t1,
                 size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 line_spacing=1.02)
        text_box(s, x=x + 0.12, y=4.50, w=lw_ - 0.24, h=0.46, text=t2,
                 size=9.5, color=SLATE, align=PP_ALIGN.CENTER,
                 line_spacing=1.08)
    text_runs(s, 0.55, 5.08, 12.25, 0.30, [
        {"text": "Опрос 150 исследователей, май 2026:   ", "size": 10.5,
         "italic": True, "color": SLATE},
        {"text": "81%", "size": 11.5, "bold": True, "color": DEEP},
        {"text": " регулярно применяют ИИ в работе   ·   ", "size": 10.5,
         "color": DEEP},
        {"text": "8%", "size": 11.5, "bold": True, "color": DEEP},
        {"text": " — как отвечающего участника   ·   ", "size": 10.5,
         "color": DEEP},
        {"text": "28%", "size": 11.5, "bold": True, "color": DEEP},
        {"text": " отвергают его прямо", "size": 10.5, "color": DEEP},
    ], align=PP_ALIGN.CENTER, line_spacing=1.05)

    # ── Что не изменилось: граница кабинетного поиска ─────────────────
    gold_callout(
        s, 0.55, 5.48, 12.25, 1.26,
        "Ссылка в отчёте не доказательство, пока её не открыли. Измерено на "
        "53\u00a0090 ссылках из отчётов десяти моделей и исследовательских "
        "агентов: 3–13% ссылок выдуманы — их нет даже в веб-архиве, они не "
        "существовали никогда, и не открываются ещё от 5 до 18%. Отсюда прямая "
        "арифметика: при самом низком измеренном уровне 3% отчёт с 50 "
        "ссылками содержит хотя бы одну несуществующую с вероятностью 78%. "
        "Deloitte сдала правительству Австралии отчёт за "
        "440\u00a0000\u00a0австралийских долларов именно с таким содержимым.",
        size=12, bold=True)
    refs_of_slide(s, "s10")
    notes_with_sources(s, "s10")
    return s

# ============================================================
# s11 - ИИ LIMITS: synthetic sycophancy, live-interview criteria
# ============================================================

def s11(p):
    """ПРАВКА #212: формулировки приведены к slides/s11-*.md и очищены от
    англицизмов («go/no-go» → «продолжать или остановить», «валидация» →
    «проверка», английский термин из подписи к числам снят)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Синтетический собеседник не может произвести несогласие",
                size=22, w=12.25, h=0.58, y=0.13)

    # ── Слева: измеренный сдвиг тона ──────────────────────────────────
    lx, lw = 0.55, 4.55
    ocean_box(s, lx, 0.92, lw, 4.32, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    icon(s, "smile", lx + lw / 2 - 0.40, 1.06, 0.80, "light")
    text_box(s, x=lx + 0.25, y=1.96, w=lw - 0.50, h=0.34,
             text="Зеркало согласия", size=14, bold=True, color=MID,
             align=PP_ALIGN.CENTER)
    stats = [("72–91%", "когда собеседник\nявно соглашается", GOLD),
             ("7–28%", "когда собеседник\nявно возражает", LIGHT)]
    for i, (num, lbl, col) in enumerate(stats):
        sx = lx + 0.22 + i * 2.10
        filled_rect(s, sx, 2.40, 1.90, 1.12,
                    (GOLD_TINT if i == 0 else SURFACE), stroke=col,
                    stroke_pt=1.6, radius=True, radius_adj=0.10)
        text_box(s, x=sx, y=2.50, w=1.90, h=0.48, text=num, size=21,
                 bold=True, color=(DEEP if i == 0 else col),
                 align=PP_ALIGN.CENTER)
        text_box(s, x=sx + 0.05, y=3.00, w=1.80, h=0.46, text=lbl, size=9.5,
                 color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.06)
    text_box(s, x=lx + 0.25, y=3.66, w=lw - 0.50, h=0.92,
             text="Это доля случаев, в которых тон ответа модели сдвигается "
                  "к позитиву (5 моделей). Не «частота отрицательного "
                  "ответа» — именно сдвиг тона.",
             size=11, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.14)
    src(s, lx + 0.25, 4.70, lw - 0.50, "Sharma и соавторы, 2023 — рисунок 1",
        size=9.5, align=PP_ALIGN.CENTER)

    # ── Справа: три признака + причина ────────────────────────────────
    rx, rw = 5.35, 7.45
    text_box(s, x=rx, y=0.96, w=rw, h=0.36,
             text="Когда живой разговор строго лучше синтеза", size=14,
             bold=True, color=MID)
    crit = [
        "Высока цена ошибки в решении «продолжать или остановить»",
        "Нужно реальное прошлое, а не правдоподобное",
        "Нужна проверка обязательством, а не мнением",
    ]
    for i, c in enumerate(crit):
        y = 1.44 + i * 0.82
        ocean_box(s, rx, y, rw, 0.68, fill=SURFACE, stroke=MID, stroke_pt=1.3)
        text_box(s, x=rx + 0.65, y=y, w=rw - 0.85, h=0.68,
                 text=f"{i+1}. {c}", size=13, bold=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE)
        icon(s, "shield-alert", rx + 0.14, y + 0.14, 0.40, "mid")
    text_box(s, x=rx, y=4.00, w=rw, h=1.24,
             text="У синтетического собеседника нет реального прошлого, "
                  "способного противоречить формулировке вопроса, — поэтому "
                  "несогласие он не производит в принципе. Сложите это со "
                  "сдвигом тона слева: ответ смещён не просто в сторону "
                  "«да», а в сторону «да» о событии, которого никогда не "
                  "было.",
             size=12.5, color=DEEP, line_spacing=1.18)

    gold_callout(
        s, 0.55, 5.44, 12.25, 1.00,
        "Пересказ интервью теряет 20–40% деталей, если пропущен шаг "
        "«сначала каждое по отдельности», — прослеживаемый до конкретного "
        "шага сбой, а не расплывчатое «ИИ иногда ошибается».",
        size=13, bold=True)
    refs_of_slide(s, "s11")
    notes_with_sources(s, "s11")
    return s

# ============================================================
# s12 - FAILURE on-point #1: synthetic users (NN/g)
# ============================================================


def s12(p):
    """ПРАВКА #212 (Р9): слайд-кейс начинается с краткого описания случая —
    человек, читающий только экран, должен понять, о чём речь, до того как
    увидит выводы. Вопрос залу снят (Р2). Мем снят: его собственные подписи
    на 3,5 дюймах не читались, а сравнение 3/7 против 7/7 на полную ширину
    и есть главный образ слайда."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Одна и та же задача: реальные люди — 3 из 7, панель ИИ-персон "
           "— 7 из 7 [1]",
        size=21, w=12.25, h=0.92, y=0.13)

    # ── ЧТО ПРОИЗОШЛО ─────────────────────────────────────────────────
    filled_rect(s, 0.55, 1.10, 12.25, 1.04, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.6, radius=True, radius_adj=0.07)
    icon(s, "file-text", 0.78, 1.42, 0.42, "teal")
    text_runs(s, 1.38, 1.14, 11.28, 0.96, [
        {"text": "ЧТО ПРОИЗОШЛО   ", "size": 10.5, "bold": True,
         "color": TEAL},
        {"text": "Nielsen Norman Group — исследовательская группа, которая "
                 "с 1998 года занимается удобством интерфейсов, — взяла один "
                 "сценарий первого знакомства с продуктом и прогнала его "
                 "дважды: с живыми участниками и с панелью ИИ-персон, "
                 "сгенерированных под тот же профиль. Сравнивали две "
                 "величины: сколько шагов сценария доведено до конца и как "
                 "оценены одни и те же функции.",
         "size": 11.5, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.14)

    # ── Два прогона одного сценария ───────────────────────────────────
    rows = [
        dict(name="Живые участники", done=3, fill=SURFACE, stroke=MID,
             var="mid", verdict="3 из 7 шагов доведены до конца"),
        dict(name="Панель ИИ-персон", done=7, fill=GOLD_TINT, stroke=GOLD,
             var="gold", verdict="отчиталась о 7 из 7"),
    ]
    ry = 2.28
    for r in rows:
        ocean_box(s, 0.55, ry, 12.25, 1.18, fill=r["fill"],
                  stroke=r["stroke"], stroke_pt=1.7)
        text_box(s, x=0.85, y=ry, w=3.20, h=1.18, text=r["name"], size=13,
                 bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        for i in range(7):
            cxx = 4.15 + i * 0.58
            ok = i < r["done"]
            icon(s, "check-check" if ok else "x", cxx, ry + 0.38, 0.42,
                 r["var"] if ok else "light")
        text_box(s, x=8.60, y=ry, w=4.00, h=1.18, text=r["verdict"],
                 size=13, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.10)
        ry += 1.34

    ocean_box(s, 0.55, 4.96, 12.25, 0.58, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.3)
    text_runs(s, 0.80, 4.96, 11.75, 0.58, [
        {"text": "Об одной и той же функции:   ", "size": 11.5,
         "italic": True, "color": SLATE},
        {"text": "«надуманно и бесполезно»", "size": 12.5, "bold": True,
         "color": MID},
        {"text": "  — живые участники,   ", "size": 11.5, "color": SLATE},
        {"text": "«изменяет правила игры»", "size": 12.5, "bold": True,
         "color": DEEP},
        {"text": "  — ИИ-персоны", "size": 11.5, "color": SLATE},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.10)

    gold_callout(
        s, 0.55, 5.68, 12.25, 1.10,
        "Расхождение здесь не в одной измеряемой величине, а сразу в обеих, "
        "на одном и том же материале: дело не в неудачном прогоне — такой "
        "выход дисквалифицирован для решения «продолжать или остановить» по "
        "построению. Альтернатива: оставить панели до-исследовательскую "
        "роль, а решение опереть на тест с 5–8 живыми участниками — размер, "
        "который уже вскрывает большинство проблем удобства.",
        size=12.5, bold=True)
    refs_of_slide(s, "s12")
    notes_with_sources(s, "s12")
    return s

# ============================================================
# s13a - FAILURE on-point #3: IBM Watson for Oncology
# ============================================================

def s13a(p):
    """ПРАВКА #212 (Р9 + расхождение билдера с исходником): слайд начинается
    с краткого описания случая, и на нём остаётся ОДИН кейс — тот, что учит
    применению (данные). Управленческая половина (Oncology Expert Advisor,
    MD Anderson) снята отсюда по решению, записанному во frontmatter
    slides/s13a-*.md: она уже живёт строкой-якорем на s22, где работает как
    отсутствующий порог гейта «продолжать или закрыть»."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Помощник врача, обученный на придуманных случаях: "
                   "рекомендации назвали небезопасными",
                size=21, w=12.25, h=0.92, y=0.13)

    # ── ЧТО ПРОИЗОШЛО ─────────────────────────────────────────────────
    filled_rect(s, 0.55, 1.10, 12.25, 1.02, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.6, radius=True, radius_adj=0.07)
    icon(s, "file-text", 0.78, 1.42, 0.42, "teal")
    text_runs(s, 1.38, 1.14, 11.28, 0.94, [
        {"text": "ЧТО ПРОИЗОШЛО   ", "size": 10.5, "bold": True,
         "color": TEAL},
        {"text": "С 2012 года компания IBM вместе с онкологическим центром "
                 "Memorial Sloan Kettering разрабатывала Watson for Oncology "
                 "— систему, подсказывающую врачу схему лечения рака. С 2015 "
                 "года её продавали больницам по всему миру. 25 июля 2018 "
                 "года издание STAT News опубликовало утёкшие внутренние "
                 "документы компании.",
         "size": 11.5, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.14)

    cw_ = 6.05
    left, right = 0.55, 6.75

    # ── Что показали документы ────────────────────────────────────────
    ocean_box(s, left, 2.22, cw_, 2.50, fill=SURFACE, stroke=MID,
              stroke_pt=1.6)
    icon(s, "file-warning", left + 0.24, 2.36, 0.46, "mid")
    text_box(s, x=left + 0.84, y=2.40, w=cw_ - 1.08, h=0.34,
             text="Что показали документы", size=13, bold=True, color=MID)
    by = 2.88
    for b, bh in [("Сотрудники в переписке называли рекомендации системы "
                   "«небезопасными и некорректными»", 0.62),
                  ("Разобранный пример: препарат назначен гипотетическому "
                   "пациенту с активным кровотечением — вопреки прямому "
                   "предупреждению производителя против такого применения",
                   0.92)]:
        text_box(s, x=left + 0.26, y=by, w=cw_ - 0.52, h=bh,
                 text="• " + b, size=11.5, color=DEEP, line_spacing=1.14)
        by += bh + 0.14

    # ── Почему так вышло ──────────────────────────────────────────────
    ocean_box(s, right, 2.22, cw_, 2.50, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.6)
    icon(s, "flask-conical", right + 0.24, 2.36, 0.46, "teal")
    text_box(s, x=right + 0.84, y=2.40, w=cw_ - 1.08, h=0.34,
             text="Почему так вышло", size=13, bold=True, color=TEAL)
    bw = 2.25
    bx1 = right + 0.26
    bx2 = right + cw_ - 0.26 - bw
    for bx, t in [(bx1, "придуманные случаи\n(на них обучали)"),
                  (bx2, "реальные исходы лечения\n(на них не обучали)")]:
        ocean_box(s, bx, 2.86, bw, 0.58, fill=WHITE, stroke=LIGHT,
                  stroke_pt=1.3)
        text_box(s, x=bx + 0.06, y=2.86, w=bw - 0.12, h=0.58, text=t,
                 size=9.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.06)
    gx, gw = bx1 + bw, bx2 - (bx1 + bw)
    connector(s, gx + 0.08, 3.15, gx + gw - 0.08, 3.15, color=SLATE,
              width=1.4, dash="dash")
    icon(s, "x", gx + gw / 2 - 0.10, 3.05, 0.20, "gold")
    text_box(s, x=gx, y=3.46, w=gw, h=0.22, text="сверки нет", size=8.5,
             italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    text_box(s, x=right + 0.26, y=3.70, w=cw_ - 0.52, h=0.96,
             text="Обучали на небольшом числе придуманных случаев, "
                  "размеченных горсткой врачей одной клиники: материал "
                  "правдоподобный, непротиворечивый и полностью выдуманный. "
                  "Мнение горстки врачей при этом выдано за отраслевой "
                  "стандарт.",
             size=11, color=DEEP, line_spacing=1.14)

    gold_callout(
        s, 0.55, 4.90, 12.25, 1.22,
        "Тот же класс сбоя, что двумя слайдами раньше: правдоподобный "
        "материал принят за реальный. Разница только в цене ошибки — здесь "
        "она измеряется в людях, а не в возвращённом гонораре. Чем выше "
        "цена ошибки, тем строже требование: материал, на котором строится "
        "решение, должен прослеживаться до зафиксированного прошлого, а не "
        "до правдоподобного.",
        size=12.5, bold=True)
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
