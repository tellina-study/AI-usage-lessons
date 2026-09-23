"""Лекция 4 v4 — Band 2 (s11–s20): требования-провал, архитектура, реализация."""
from _helpers import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    right_arrow, circle, chip, connector, add_image, icon, slide_title,
    gold_callout, teal_callout, footer, src, speaker_notes, load_notes, notes_with_sources, refs_of_slide,
    build_section_divider, ref_list, refs_of, link_run, URLS,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE, COVER_OUTLINE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, MID_TINT, ICONS, CHARTS, ASSETS, WEB,
    FONT_MONO,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

SCR = ASSETS / "screenshots"


# ============================================================
# s11 — prompt-and-pray (iceberg hero + case + second failure)
# ============================================================
def s11(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "prompt-and-pray: баг не в коде, а в требовании, которое никто не проверил",
        size=22, w=12.2, h=0.85)

    # left: iceberg ironic illustration
    lx, lw = 0.55, 4.55
    ocean_box(s, lx - 0.05, 1.55, lw + 0.10, 4.05, fill=WHITE, stroke=LIGHT)
    add_image(s, SCR / "s11-iceberg.jpg", lx + 0.08, 1.66, lw - 0.06, 3.05)
    text_box(s, x=lx + 0.12, y=4.78, w=lw - 0.12, h=0.78,
             text="Видимое «работает на демо» — вершина; под водой — десятки "
                  "невысказанных допущений, по которым модель взяла дефолт.",
             size=11, italic=True, color=MID, line_spacing=1.12,
             align=PP_ALIGN.CENTER)

    # right: case analysis
    rx, rw = 5.35, 7.45
    ocean_box(s, rx, 1.55, rw, 1.95)
    text_runs(s, rx + 0.24, 1.68, rw - 0.48, 1.72, [
        {"text": "prompt-and-pray", "size": 14, "bold": True, "color": MID},
        {"text": " — один расплывчатый промпт («сделай систему бронирования») "
                 "и надежда. Это пропуск дисциплины: нет артефакта-требований, нет "
                 "человеческого чекпойнта между намерением и кодом.",
         "size": 12, "color": DEEP},
        {"text": "Модель молча достраивает решения: бронь в прошлом? пересечение "
                 "броней? кто отменяет чужую? часовые пояса? — по каждому берёт "
                 "правдоподобный дефолт. «Работает» на демо, ломается на первом "
                 "реальном конфликте.",
         "size": 12, "color": DEEP, "newpara": True, "space_before": 6,
         "line_spacing": 1.14},
    ])
    # coварство strip
    filled_rect(s, rx, 3.62, rw, 0.78, TEAL_TINT, stroke=TEAL, stroke_pt=1.4,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=3.70, w=rw - 0.48, h=0.64,
             text="Код корректен относительно того, что модель предположила. "
                  "Баг не в коде — в том, что предположения никто не проверил; в "
                  "коде их не видно.",
             size=11.5, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.12)
    # second failure — overclaim спека=истина
    filled_rect(s, rx, 4.50, rw, 1.04, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.05)
    text_runs(s, rx + 0.24, 4.56, rw - 0.48, 0.92, [
        {"text": "Зеркальная крайность (Encarnacao, «The Emperor's New Code»): ",
         "size": 10.5, "bold": True, "color": SLATE, "line_spacing": 1.12},
        {"text": "«спека = единственная истина, код можно не читать». Но спека "
                 "недоопределяет поведение; «перегенерирую из спеки» — новая "
                 "догадка, не тот же продукт. Код остаётся источником истины.",
         "size": 10.5, "color": DEEP, "line_spacing": 1.12},
    ])

    gold_callout(
        s, 0.55, 5.70, 12.25, 0.58,
        "Узкое место — не способность модели писать код, а точность "
        "формулирования намерения (существенная сложность, Brooks [1]). "
        "Альтернатива — не «без AI», а вернуть человеческий чекпойнт: требования, "
        "принятые до кода [2].",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s12")
    notes_with_sources(s, "s12")
    return s


# ============================================================
# s12 — section divider Раздел 2 (Архитектура)
# ============================================================
def s12(p):
    return build_section_divider(
        p, here_idx=2,
        subtitle="Архитектура — до кода, и ею надо управлять",
        bridge="После требований — не сразу код, а архитектура: решить, из чего "
               "собрать систему. Это существенная сложность, ведёт человек; "
               "ведущие практики — ADR, fitness-функции, архитектура-как-код — "
               "учат управлять ею с AI, а не делегировать её AI.",
        sid="s13",
        tag="Тонкая фаза · ведёт человек · 1 провал")


# ============================================================
# s13 — architecture necessity (3-node chain + failure) [in-bucket]
# ============================================================
def s13(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "После требований — архитектура, а не сразу код",
                size=25, w=12.0, h=0.85)

    # left: three-node chain, middle highlighted
    lx, lw = 0.55, 6.10
    ocean_box(s, lx, 1.55, lw, 4.05)
    nodes = [
        ("что нужно", "требования", LIGHT, False),
        ("из чего собрать", "архитектура", GOLD, True),
        ("как писать", "код", LIGHT, False),
    ]
    ny = 1.85
    nw = lw - 0.60
    for i, (name, sub, col, hi) in enumerate(nodes):
        y = ny + i * 1.02
        if hi:
            filled_rect(s, lx + 0.30, y, nw, 0.86, GOLD_TINT, stroke=GOLD,
                        stroke_pt=2.0, radius=True, radius_adj=0.08)
        else:
            filled_rect(s, lx + 0.30, y, nw, 0.86, SURFACE, stroke=col,
                        stroke_pt=1.3, radius=True, radius_adj=0.08)
        text_box(s, x=lx + 0.52, y=y + 0.12, w=nw - 0.60, h=0.36, text=name,
                 size=15, bold=True, color=DEEP)
        text_box(s, x=lx + 0.52, y=y + 0.48, w=nw - 0.60, h=0.32, text=sub,
                 size=11.5, italic=True, color=(MID if hi else SLATE))
        if hi:
            text_box(s, x=lx + lw - 1.6, y=y + 0.08, w=1.35, h=0.7,
                     text="нельзя\nпропускать", size=10.5, bold=True,
                     color=GOLD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                     line_spacing=0.95)
        if i < 2:
            text_box(s, x=lx + 0.30, y=y + 0.84, w=nw, h=0.20, text="▼",
                     size=13, bold=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.30, y=4.98, w=nw, h=0.52,
             text="Продукт фазы — малое число трудных, труднообратимых развилок: "
                  "границы компонентов, модель данных, приоритет качеств.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.08)

    # right: failure of skipping the phase
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, 1.55, rw, 4.05)
    text_box(s, x=rx + 0.24, y=1.68, w=rw - 0.48, h=0.40,
             text="Перепрыгнуть к коду →", size=13.5, bold=True, color=MID)
    filled_rect(s, rx + 0.24, 2.18, rw - 0.48, 1.10, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    icon(s, "triangle-alert", rx + 0.42, 2.34, 0.46, "light")
    text_box(s, x=rx + 1.02, y=2.30, w=rw - 1.30, h=0.94,
             text="Эрозия архитектуры — разрыв между задуманным и реализованным, "
                  "деградация сопровождаемости.",
             size=12, color=DEEP, line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, rx + 0.24, 3.42, rw - 0.48, 1.40, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    icon(s, "bomb", rx + 0.42, 3.58, 0.46, "light")
    text_box(s, x=rx + 1.02, y=3.52, w=rw - 1.30, h=1.24,
             text="Когнитивный долг кодовой базы (Thoughtworks Radar, кольцо "
                  "Hold [2]): разрыв между устройством системы и пониманием команды "
                  "— «живёт в головах», не в артефактах. Средство, названное "
                  "Radar — архитектурные fitness-функции [3].",
             size=11.5, color=DEEP, line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.66,
        "«Решить, что строить» — существенная сложность (Brooks, «No Silver "
        "Bullet», 1986 [1]): выбор под компромисс не делегируется. AI полезен только "
        "на периферии — варианты, объяснение паттерна, черновик диаграммы.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s14")
    notes_with_sources(s, "s14")
    return s


# ============================================================
# s14 — architecture approaches matrix (4 cols × 4 rows)
# ============================================================
def s14(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Четыре практики управлять архитектурой с AI (инструменты вторичны)",
        size=23, w=12.2, h=0.82)

    cols = [
        ("gavel", "ADR", MID),
        ("shield-check", "Fitness-функция", TEAL),
        ("layout-grid", "C4 / арх-как-код", MID),
        ("refresh-cw", "Эволюционная арх.", TEAL),
    ]
    rows = [
        ("Что это",
         ["Полстраницы неизменяемой записи на решение (контекст·решение·"
          "статус·последствия); хранит «почему»",
          "Автопроверка архитектурной характеристики на каждом коммите "
          "(«оплата не зависит от UI»; «ответ < 200 мс»)",
          "Архитектура машиночитаемо (C4: Context/Container/Component/Code; "
          "DSL — PlantUML/Mermaid/Structurizr)",
          "ADR + fitness-функции + арх-как-код вместе = инкрементальность + "
          "управляемое изменение"]),
        ("Кто предписывает",
         ["Найгард 2011 [1]; Radar — ADOPT [4]",
          "Thoughtworks; Ребекка Парсонс [4]",
          "Саймон Браун (C4) [3]; Structurizr",
          "Форд, Парсонс, Кюа [2]"]),
        ("Роль AI (вторично)",
         ["редактирует, сверяет — но решает и обосновывает человек",
          "удобно писать fitness-функции; они же валидируют сгенерированный код",
          "читает как контекст, порождает диаграммы; drift-detection — "
          "Structurizr (модель vs код)",
          "исполняет внутри каждой из трёх практик"]),
        ("Где человек",
         ["автор развилки = автор ADR",
          "решает, какой инвариант критичен",
          "владеет текстовой моделью",
          "держит направление эволюции"]),
    ]
    x0 = 0.55
    total = 12.25
    gap = 0.14
    cw = (total - gap * 3) / 4     # ~2.95
    top = 1.50
    # header row with icons
    hh = 0.72
    for i, (ic, name, col) in enumerate(cols):
        x = x0 + i * (cw + gap)
        filled_rect(s, x, top, cw, hh, col, radius=True, radius_adj=0.10)
        icon(s, ic, x + 0.14, top + 0.10, 0.5, "white")
        text_box(s, x=x + 0.72, y=top + 0.08, w=cw - 0.82, h=hh - 0.10,
                 text=name, size=12.5, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.98)
    # body rows
    row_h = [0.98, 0.62, 0.72, 0.50]
    ry = top + hh + 0.08
    for r, (label, cells) in enumerate(rows):
        rh = row_h[r]
        # row label chip on far-left overlap? Instead put label as tiny left tab
        for i in range(4):
            x = x0 + i * (cw + gap)
            fill = SURFACE if r % 2 == 0 else WHITE
            filled_rect(s, x, ry, cw, rh, fill, stroke=SOFT_GREY, stroke_pt=1.0,
                        radius=True, radius_adj=0.05)
            if i == 0:
                text_box(s, x=x + 0.12, y=ry + 0.04, w=cw - 0.24, h=0.22,
                         text=label.upper(), size=8.5, bold=True, color=LIGHT)
                tb_y = ry + 0.26
                tb_h = rh - 0.30
            else:
                tb_y = ry + 0.08
                tb_h = rh - 0.14
            text_box(s, x=x + 0.12, y=tb_y, w=cw - 0.24, h=tb_h,
                     text=cells[i], size=9.5, color=DEEP, line_spacing=1.04)
        ry += rh + 0.06

    gold_callout(
        s, 0.55, 5.94, 12.25, 0.66,
        "Устойчивый паттерн: автоматический архитектурный контроль на каждом "
        "коммите. Вендорский хайп: «наш продукт сам обеспечит архитектуру». "
        "Человек владеет «почему», AI кодирует и проверяет.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s15", y=7.08)
    notes_with_sources(s, "s15")
    return s


# ============================================================
# s15 — poisoned context (cycle + caveat + alternative) [in-bucket]
# ============================================================
def s15(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Отравленный контекст: AI не отличает «так сложилось» от «так правильно»",
        size=22, w=12.2, h=0.82)

    # top caveat #261 band
    filled_rect(s, 0.55, 1.44, 12.25, 0.56, TEAL_TINT, stroke=TEAL, stroke_pt=1.5,
                radius=True, radius_adj=0.06)
    text_box(s, x=0.80, y=1.51, w=11.75, h=0.44,
             text="Это происходит, КОГДА архитектура не описана и нет процесса "
                  "управления ею. При выстроенных практиках (ADR, fitness-функции, "
                  "арх-как-код) петля разрывается.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    # left: poisoning cycle
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 2.14, lw, 3.42)
    text_box(s, x=lx + 0.24, y=2.24, w=lw - 1.00, h=0.36,
             text="Петля отравления (Böckeler 2026, Thoughtworks) [1]",
             size=12.5, bold=True, color=MID)
    icon(s, "flame", lx + lw - 0.66, 2.20, 0.44, "gold")
    loop = [
        ("плохой дизайн", GOLD, True),
        ("AI копирует («как принято здесь»)", MID, False),
        ("дизайн хуже", LIGHT, False),
        ("AI копирует ещё увереннее", MID, False),
    ]
    ly = 2.70
    for i, (txt, col, start) in enumerate(loop):
        y = ly + i * 0.62
        filled_rect(s, lx + 0.30, y, lw - 0.60, 0.48,
                    (GOLD_TINT if start else SURFACE),
                    stroke=(GOLD if start else col), stroke_pt=(1.8 if start else 1.2),
                    radius=True, radius_adj=0.10)
        if start:
            circle(s, lx + 0.40, y + 0.13, 0.22, GOLD)
        text_box(s, x=lx + (0.74 if start else 0.48), y=y + 0.03, w=lw - 1.1,
                 h=0.42, text=txt, size=11.5, bold=start, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE)
        if i < 3:
            text_box(s, x=lx + 0.30, y=y + 0.46, w=lw - 0.60, h=0.16, text="↓",
                     size=12, bold=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.24, y=5.16, w=lw - 0.48, h=0.34,
             text="Böckeler честно: «у нас пока нет хорошего способа это смягчить».",
             size=10.5, italic=True, color=SLATE)

    # right: alternative (3 plates, bridge to s14)
    rx, rw = 6.85, 5.95
    alts = [
        ("user-check", "Человек владеет развилками",
         "утверждает решения и отвечает за них; AI может быть полноценным "
         "соавтором или автором черновика — но не подписывает."),
        ("gavel", "ADR [2]",
         "человеко-написанный контекст «решили X, потому что Y, отвергли Z» — "
         "разделяемое понимание против отравления."),
        ("shield-check", "Fitness-функции + модульный код [3]",
         "детерминированные инварианты ломают петлю; чёткие компоненты дают "
         "управляемый контекст."),
    ]
    ay = 2.14
    for i, (ic, head, body) in enumerate(alts):
        y = ay + i * 1.16
        ocean_box(s, rx, y, rw, 1.04)
        icon(s, ic, rx + 0.22, y + 0.24, 0.5, "teal")
        text_box(s, x=rx + 0.86, y=y + 0.12, w=rw - 1.06, h=0.34, text=head,
                 size=12.5, bold=True, color=MID)
        text_box(s, x=rx + 0.86, y=y + 0.46, w=rw - 1.06, h=0.52, text=body,
                 size=10.5, color=DEEP, line_spacing=1.10)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "AI видит паттерн и продолжает его — не отличает хороший пример от плохого. "
        "Чем хуже существующая архитектура, тем сильнее AI её закрепляет.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    # Round-5 meme: X, X Everywhere (Buzz/Woody) — "плохой паттерн везде",
    # reinforcing the loop's own repetition. Bottom band, right of ref list.
    add_image(s, WEB / "band-x-everywhere.png", 9.57, 6.40, 3.23, 0.64)
    refs_of_slide(s, "s16")
    notes_with_sources(s, "s16")
    return s


# ============================================================
# s16 — section divider Раздел 3 (Реализация)
# ============================================================
def s16(p):
    return build_section_divider(
        p, here_idx=3,
        subtitle="Реализация — дисциплина и харнес",
        bridge="Здесь AI пишет код, и фаза сильна — но сильна при дисциплине. "
               "Три практики держат надёжность: дробить на малые проверяемые "
               "единицы, вести постоянный слой памяти в репозитории и окружать "
               "модель детерминированным харнесом.",
        sid="s17",
        tag="Сильная фаза · три практики · 2 провала")


# ============================================================
# s17 — small units + explore→plan→code→commit pipeline
# ============================================================
def s17(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Дисциплина работы: малые проверяемые единицы + цикл explore→plan→code→commit",
        size=21, w=12.3, h=0.82)

    # pipeline main visual — 4 stages with RIGHT_ARROW
    stages = [
        ("scan-search", "explore", "исследовать код"),
        ("clipboard-list", "plan", "принять план"),
        ("code", "code", "писать"),
        ("git-merge", "commit", "зафиксировать"),
    ]
    n = len(stages)
    x0 = 0.55
    total = 12.25
    aw = 0.55                       # arrow width
    sw = (total - aw * (n - 1)) / n  # stage width ~2.65
    py = 1.55
    ph = 1.28
    for i, (ic, name, owner) in enumerate(stages):
        x = x0 + i * (sw + aw)
        locked = i < 2
        ocean_box(s, x, py, sw, ph,
                  fill=(GOLD_TINT if locked else SURFACE),
                  stroke=(GOLD if locked else MID), stroke_pt=1.6)
        icon(s, ic, x + 0.20, py + 0.18, 0.5, "gold" if locked else "mid")
        text_box(s, x=x + 0.80, y=py + 0.18, w=sw - 0.95, h=0.42, text=name,
                 size=15, bold=True, color=DEEP, font="DejaVu Sans Mono")
        text_box(s, x=x + 0.20, y=py + 0.72, w=sw - 0.36, h=0.44, text=owner,
                 size=11, italic=True, color=SLATE)
        if i < n - 1:
            right_arrow(s, x + sw + 0.03, py + ph / 2 - 0.14, aw - 0.06, 0.28,
                        fill=LIGHT)
    text_box(s, x=0.55, y=2.90, w=12.25, h=0.32,
             text="Порядок принудителен: генерация до исследования и плана — "
                  "это prompt-and-pray на уровне кода.   — цикл explore→plan→"
                  "code→commit, Anthropic [1]",
             size=11.5, italic=True, bold=True, color=MID, align=PP_ALIGN.CENTER)

    # bottom-left: small units
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 3.36, lw, 2.14)
    icon(s, "split", lx + 0.24, 3.50, 0.5, "mid")
    text_box(s, x=lx + 0.88, y=3.54, w=lw - 1.10, h=0.40,
             text="Малые проверяемые единицы", size=13, bold=True, color=MID)
    text_box(s, x=lx + 0.24, y=4.02, w=lw - 0.48, h=1.42,
             text="Каждый кусок реализуем и проверяем в изоляции: AI получает "
                  "детерминированный self-check, человек — маленький diff, который "
                  "реально можно отревьюить. Osmani [2]: чем меньше предложение AI, "
                  "тем реальнее ревью; гигантский diff человек не читает.",
             size=11, color=DEEP, line_spacing=1.16)

    # bottom-right: role split
    rx, rw = 6.85, 5.95
    filled_rect(s, rx, 3.36, rw, 1.02, TEAL_TINT, stroke=TEAL, stroke_pt=1.4,
                radius=True, radius_adj=0.06)
    text_runs(s, rx + 0.24, 3.46, rw - 0.48, 0.86, [
        {"text": "AI берёт привнесённую сложность", "size": 12, "bold": True,
         "color": TEAL},
        {"text": " (boilerplate, типовой обработчик). ", "size": 12,
         "color": DEEP},
        {"text": "Человек — существенную", "size": 12, "bold": True,
         "color": DEEP},
        {"text": ": что строим, что рискованно, что корректно, можно ли слить. [3]",
         "size": 12, "color": DEEP},
    ])
    filled_rect(s, rx, 4.50, rw, 1.00, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=4.58, w=rw - 0.48, h=0.86,
             text="AI участвует в двух философиях — в редакторе (синхронно) и "
                  "асинхронно (изолированно → PR); это свойство режима, "
                  "разберём вторично.",
             size=11, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.12)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Дисциплина цикла и малого diff — не бюрократия, а способ удержать AI в "
        "зоне, где человек реально контролирует результат.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s18")
    notes_with_sources(s, "s18")
    return s


# ============================================================
# s17b (NEW, #162 round 3) — Gemini CLI self-review failure case study
# ============================================================
def s17b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Cаморевью — обязательный шаг между code и commit, не факультативная привычка",
        size=19, w=12.3, h=0.82)

    # left: incident chronology
    lx, lw = 0.55, 6.55
    ocean_box(s, lx, 1.44, lw, 4.10)
    icon(s, "bug", lx + 0.22, 1.58, 0.46, "mid")
    text_box(s, x=lx + 0.82, y=1.62, w=lw - 1.60, h=0.36,
             text="Google Gemini CLI, июль 2025 [1]", size=13, bold=True,
             color=MID)
    add_image(s, ASSETS / "logos" / "gemini-logo.png", lx + lw - 0.62, 1.56,
              0.36, 0.36)
    text_box(s, x=lx + lw - 0.90, y=1.94, w=0.92, h=0.16,
             text="Google Gemini", size=6.5, italic=True, color=LIGHT,
             align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.24, y=2.06, w=lw - 0.48, h=0.30,
             text="AI Incident Database, Report 6120 / Incident 1178",
             size=10, italic=True, color=SLATE)
    text_box(s, x=lx + 0.24, y=2.44, w=lw - 0.48, h=1.30,
             text="Пользователь попросил переместить файлы в новую папку. Агент "
                  "выполнил mkdir, не проверил результат — решил, что папка уже "
                  "существует, и цепочка move перезаписала почти все файлы "
                  "пользователя в один оставшийся.",
             size=11.5, color=DEEP, line_spacing=1.18)
    filled_rect(s, lx + 0.24, 3.82, lw - 0.48, 1.50, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.4, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.46, y=3.92, w=lw - 0.9, h=1.30,
             text="«I have completely and catastrophically failed you. My "
                  "review of the commands confirms my gross incompetence.»",
             size=11.5, italic=True, color=DEEP, line_spacing=1.20,
             font=FONT_MONO, anchor=MSO_ANCHOR.MIDDLE)

    # right: mechanism contrast + scale
    rx, rw = 7.30, 5.50
    ocean_box(s, rx, 1.44, rw, 1.86, fill=SOFT_GREY, stroke=LIGHT, stroke_pt=1.0)
    icon(s, "circle-slash", rx + 0.22, 1.60, 0.42, "mid")
    text_box(s, x=rx + 0.78, y=1.62, w=rw - 1.0, h=0.34,
             text="Другой механизм отказа", size=12, bold=True, color=DEEP)
    text_box(s, x=rx + 0.24, y=2.04, w=rw - 0.48, h=1.18,
             text="Не «слишком много прав» (как Replit) — здесь пропущена "
                  "конкретная «проверка»: агент не верифицировал промежуточный "
                  "результат и построил следующий шаг на ложном допущении.",
             size=11, color=DEEP, line_spacing=1.16)

    ocean_box(s, rx, 3.50, rw, 2.04)
    icon(s, "gauge", rx + 0.22, 3.64, 0.42, "teal")
    text_box(s, x=rx + 0.78, y=3.66, w=rw - 1.0, h=0.34,
             text="Масштаб (для контраста)", size=12, bold=True, color=TEAL)
    text_box(s, x=rx + 0.24, y=4.10, w=rw - 0.48, h=0.44, text="~11%",
             size=24, bold=True, color=DEEP)
    text_box(s, x=rx + 0.24, y=4.58, w=rw - 0.48, h=0.88,
             text="живых бэкенд-обновлений у Uber (2026) выкатываются агентом "
                  "без человека в цикле.",
             size=11, color=DEEP, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Саморевью — обязательный шаг explore→plan→code→commit: перечитать diff "
        "и проверить результат, прежде чем коммитить.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s17b")
    notes_with_sources(s, "s17b")
    return s


# ============================================================
# s18 — persistent memory layer (architecture: dev ↔ repo → agent)
# ============================================================
def s18(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Постоянный слой инструкций — не память: агент читает его каждую сессию",
        size=20, w=12.3, h=0.82)
    text_box(s, x=0.55, y=1.24, w=12.25, h=0.26,
             text="Четыре смежных, но разных понятия: инструкции (AGENTS.md) · "
                  "курирование контекста сессии · операционная история · память "
                  "(слот 1) — не путать.",
             size=10.5, italic=True, color=SLATE)

    # architecture row: DEVELOPER — REPO — AGENT
    ay = 1.55
    ah = 1.60
    # developer (human, curates)
    dx, dw = 0.55, 2.70
    ocean_box(s, dx, ay, dw, ah)
    icon(s, "user-check", dx + dw / 2 - 0.32, ay + 0.22, 0.64, "teal")
    text_box(s, x=dx + 0.1, y=ay + 0.94, w=dw - 0.2, h=0.34, text="РАЗРАБОТЧИК",
             size=12.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, x=dx + 0.1, y=ay + 1.24, w=dw - 0.2, h=0.30, text="курирует слой",
             size=10.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    # repo (persistent layer)
    rx2, rw2 = 4.10, 5.10
    ocean_box(s, rx2, ay, rw2, ah, fill=SURFACE, stroke=MID, stroke_pt=1.8)
    icon(s, "database", rx2 + 0.22, ay + 0.20, 0.5, "mid")
    text_box(s, x=rx2 + 0.82, y=ay + 0.22, w=rw2 - 1.0, h=0.36,
             text="РЕПОЗИТОРИЙ — постоянный слой", size=12.5, bold=True,
             color=MID)
    text_box(s, x=rx2 + 0.24, y=ay + 0.66, w=rw2 - 0.48, h=0.86,
             text="AGENTS.md (стандарт agents.md, Linux Foundation [1]; команды "
                  "сборки/тестов, стиль, guardrails; аналог CLAUDE.md) · "
                  "память-заметки · операционная история задач. "
                  "Правило: вести командами, а не объяснениями.",
             size=10.5, color=DEEP, line_spacing=1.12)
    # agent (stateless, reads each session)
    gx, gw = 9.55, 3.25
    ocean_box(s, gx, ay, gw, ah)
    icon(s, "bot", gx + gw / 2 - 0.32, ay + 0.22, 0.64, "mid")
    text_box(s, x=gx + 0.1, y=ay + 0.94, w=gw - 0.2, h=0.34,
             text="АГЕНТ (stateless)", size=12.5, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER)
    text_box(s, x=gx + 0.1, y=ay + 1.24, w=gw - 0.2, h=0.30,
             text="читает слой каждую сессию", size=10.5, italic=True,
             color=SLATE, align=PP_ALIGN.CENTER)
    # arrows
    connector(s, dx + dw, ay + ah / 2, rx2, ay + ah / 2, color=TEAL, width=2.4)
    right_arrow(s, rx2 + rw2 + 0.02, ay + ah / 2 - 0.14, 0.30, 0.28, fill=MID)

    # context-engineering block
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 3.36, lw, 2.14)
    text_box(s, x=lx + 0.24, y=3.48, w=lw - 0.48, h=0.36,
             text="context-engineering — 3 примитива курирования (Anthropic) [3]",
             size=12.5, bold=True, color=MID)
    prims = ["JIT-извлечение", "компакция", "память-заметки"]
    px = lx + 0.30
    for pr in prims:
        chip(s, px, 3.92, 1.85, 0.42, pr, fill=TEAL, color=WHITE, size=11)
        px += 1.95
    text_box(s, x=lx + 0.24, y=4.50, w=lw - 0.48, h=0.92,
             text="Принцип: больше контекста ≠ лучше. Правильно курировать, а не "
                  "только накапливать.",
             size=11, color=DEEP, line_spacing=1.14)

    # failure: context rot
    rx3, rw3 = 6.85, 5.95
    filled_rect(s, rx3, 3.36, rw3, 2.14, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.05)
    icon(s, "flame", rx3 + 0.24, 3.50, 0.5, "light")
    text_box(s, x=rx3 + 0.88, y=3.54, w=rw3 - 1.10, h=0.40,
             text="context rot (Chroma, 18 моделей) [2]", size=12.5, bold=True,
             color=DEEP)
    text_box(s, x=rx3 + 0.24, y=4.04, w=rw3 - 0.48, h=0.78,
             text="Точность извлечения падает нелинейно с ростом входа — "
                  "деградация начинается ДО переполнения окна. «Несвежий "
                  "контекст гниёт».",
             size=11, color=DEEP, line_spacing=1.14)
    text_box(s, x=rx3 + 0.24, y=4.86, w=rw3 - 0.48, h=0.58,
             text="База: демо памяти — пик ~172k против ~334k токенов без памяти "
                  "— cookbook-демонстрация направления, не контролируемый множитель.",
             size=10, italic=True, color=SLATE, line_spacing=1.1)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Контекст живёт в репозитории, а не в промпте. Устойчивый паттерн — "
        "курируемый постоянный слой; хайп — «наш AGENTS.md сам всё решит».",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    # Round-5 meme: Monkey Puppet — the silent-failure mode of compaction
    # (a rejected decision can vanish from the summary with no error).
    add_image(s, WEB / "band-monkey-puppet.png", 9.92, 6.40, 2.88, 0.64)
    refs_of_slide(s, "s19")
    notes_with_sources(s, "s19")
    return s


# ============================================================
# s18b (NEW, #162 round 3) — honest curation limits: compaction loses
# silently, JIT symmetric fail, stale AGENTS.md worse than none
# ============================================================
def s18b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Курирование не устраняет риск — оно меняет один риск на другой",
        size=21, w=12.3, h=0.82)

    cards = [
        ("layers", "Компакция теряет молча",
         "Суммаризация — с потерями: отклонённое решение («библиотеку X не "
         "использовать») может исчезнуть из резюме без ошибки — агент "
         "предложит именно то, от чего отказались."),
        ("circle-help", "JIT не спросит о неизвестном",
         "Агент подгружает то, о чём догадался спросить; то, о существовании "
         "чего не знает, — не запросит никогда. Симметричный предел той же "
         "техники."),
        ("shield-alert", "Несвежий AGENTS.md вреднее отсутствующего",
         "Отсутствие файла агент компенсирует вопросом; устаревшему — "
         "доверяет буквально: устаревшая команда сборки, снятое ограничение, "
         "которому агент следует."),
    ]
    cw, gap = 3.97, 0.17
    x0 = 0.55
    top = 1.44
    for i, (ic, head, body) in enumerate(cards):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, top, cw, 3.30)
        icon(s, ic, x + 0.24, top + 0.20, 0.48, "mid")
        text_box(s, x=x + 0.24, y=top + 0.82, w=cw - 0.48, h=0.62, text=head,
                 size=13, bold=True, color=MID, line_spacing=1.06)
        text_box(s, x=x + 0.24, y=top + 1.46, w=cw - 0.48, h=1.72, text=body,
                 size=10.5, color=DEEP, line_spacing=1.18)

    filled_rect(s, 0.55, 4.92, 12.25, 0.60, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.08)
    text_box(s, x=0.79, y=4.99, w=11.8, h=0.46,
             text="Ни одна техника курирования не устраняет риск — каждая "
                  "меняет один риск на другой. Это предел самой техники.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Решение, которое нельзя терять молча, не доверяют компакции сессии — "
        "его фиксируют в постоянном слое инструкций.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s18b")
    notes_with_sources(s, "s18b")
    return s


# ============================================================
# s19 — harness gate (model in centre, deterministic frame + feedback loop)
# ============================================================
def s19(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Детерминированный каркас-гейт вокруг недетерминированной модели",
                size=23, w=12.2, h=0.82)

    # left: model surrounded by frame
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.55, lw, 3.95)
    # frame checks (top row)
    checks = ["линтеры", "структурные тесты", "fitness-функции",
              "SAST-гейт", "least-privilege", "sandbox"]
    cx = lx + 0.28
    cyr = 1.72
    per = 3
    cwid = (lw - 0.56 - 0.2 * (per - 1)) / per
    for i, ch in enumerate(checks):
        col = i % per
        row = i // per
        x = lx + 0.28 + col * (cwid + 0.2)
        y = cyr + row * 0.56
        chip(s, x, y, cwid, 0.44, ch, fill=MID, color=WHITE, size=9.5)
    # model in centre
    circle(s, lx + lw / 2 - 0.62, 3.02, 1.24, GOLD_TINT, stroke=GOLD,
           stroke_pt=2.0)
    icon(s, "cpu", lx + lw / 2 - 0.34, 3.16, 0.56, "gold")
    text_box(s, x=lx + lw / 2 - 0.9, y=3.72, w=1.8, h=0.34,
             text="МОДЕЛЬ", size=11.5, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.28, y=4.40, w=lw - 0.56, h=0.86,
             text="Надёжность — не «дать модели больше свободы», а сузить "
                  "пространство её решений. Модель недетерминирована (один промпт "
                  "→ разные ответы); харнес детерминирован (тест либо прошёл, "
                  "либо нет).",
             size=10.5, color=DEEP, line_spacing=1.12, align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.28, y=5.24, w=lw - 0.56, h=0.24,
             text="— Böckeler 2026, harness engineering [1]",
             size=9, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # right: feedback loop + honest limit
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, 1.55, rw, 1.95)
    text_box(s, x=rx + 0.24, y=1.66, w=rw - 0.48, h=0.36,
             text="Петля обратной связи — главный механизм", size=12.5,
             bold=True, color=MID)
    text_box(s, x=rx + 0.24, y=2.06, w=rw - 0.48, h=1.36,
             text="Агент буксует → это сигнал о дыре в каркасе → добавить "
                  "недостающее обратно:\n"
                  "• не хватило команды → в AGENTS.md\n"
                  "• нарушен инвариант → fitness-функция [3]\n"
                  "• небезопасно → SAST-гейт",
             size=11, color=DEEP, line_spacing=1.22)
    # honest limit (in-bucket)
    filled_rect(s, rx, 3.62, rw, 0.90, TEAL_TINT, stroke=TEAL, stroke_pt=1.5,
                radius=True, radius_adj=0.06)
    text_runs(s, rx + 0.24, 3.72, rw - 0.48, 0.72, [
        {"text": "Guardrails ≠ верификация. ", "size": 12, "bold": True,
         "color": TEAL},
        {"text": "Линтер знает, что код отформатирован — не знает, решает ли он "
                 "правильную задачу. Каркас не проверяет поведение.",
         "size": 11.5, "color": DEEP, "line_spacing": 1.12},
    ])
    # three layers
    filled_rect(s, rx, 4.64, rw, 0.86, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.06)
    text_runs(s, rx + 0.24, 4.71, rw - 0.48, 0.74, [
        {"text": "Три слоя, ни один не заменяет другой: харнес + поведенческие "
                 "тесты + человек на merge. ", "size": 11.5, "bold": True,
         "color": DEEP, "line_spacing": 1.10},
        {"text": "Willison: «отревьюй — или это не разработка» (vibe-engineering) [2].",
         "size": 10, "italic": True, "color": LIGHT},
    ], anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Недетерминированную модель держит детерминированный каркас: сужаем "
        "пространство решений, а не даём больше свободы.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20")
    notes_with_sources(s, "s20")
    return s


# ============================================================
# s20b — Skills (AGENTS.md vs SKILL.md comparison + honest cross-vendor limit)
# ============================================================
def s20b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "В разработке skill окупается на редкой, но повторяемой процедуре",
        size=20, w=12.25, h=0.60)

    # ---- LEFT: three genuinely common dev skills (majority of visual weight)
    lx, lw = 0.55, 7.30
    text_box(s, x=lx, y=1.08, w=lw, h=0.28,
             text="ЧТО В РАЗРАБОТКЕ ДЕЙСТВИТЕЛЬНО ВЫНОСЯТ В SKILL",
             size=12, bold=True, color=LIGHT)

    dev_skills = [
        ("terminal", "teal", TEAL,
         "Прогон проверок одной командой",
         "Линтер → проверка типов → тесты (ruff/mypy/pytest либо "
         "eslint/tsc/vitest) вызываются одним обращением, а не "
         "восстанавливаются заново под конвенции конкретного репозитория."),
        ("database", "mid", MID,
         "Одноразовая база под интеграционный тест",
         "Как поднять настоящий Postgres или Kafka в контейнере на время "
         "прогона и погасить после. Процедура записана — агент не "
         "вспоминает конфигурацию по памяти."),
        ("file-code", "teal", TEAL,
         "Сборка документации по коду",
         "Пройти структуру проекта и зависимости, собрать README и записи "
         "об архитектурных решениях. Шагов много, нужно редко — ровно тот "
         "профиль, ради которого skill и заводят."),
    ]
    cy, chh, cgap = 1.38, 1.22, 0.10
    for ic, var, col, head, body in dev_skills:
        ocean_box(s, lx, cy, lw, chh)
        icon(s, ic, lx + 0.22, cy + 0.16, 0.44, var)
        text_box(s, x=lx + 0.82, y=cy + 0.14, w=lw - 1.04, h=0.30,
                 text=head, size=13, bold=True, color=col)
        text_box(s, x=lx + 0.82, y=cy + 0.48, w=lw - 1.04, h=0.62,
                 text=body, size=11, color=DEEP, line_spacing=1.12)
        cy += chh + cgap

    # example line — one token per card, same convention as the deck's matrices
    text_runs(s, lx, cy + 0.08, lw, 0.28, [
        {"text": "Пример:  ", "size": 10, "bold": True, "color": SLATE},
        {"text": "lint+type-check+test skill", "size": 9,
         "italic": True, "color": TEAL, "font": FONT_MONO},
        {"text": "  ·  ", "size": 9, "color": SLATE},
        {"text": "testcontainers-docker skill", "size": 9, "italic": True,
         "color": MID, "font": FONT_MONO},
        {"text": "  ·  ", "size": 9, "color": SLATE},
        {"text": "README Generator skill", "size": 9, "italic": True,
         "color": TEAL, "font": FONT_MONO},
    ])

    # ---- RIGHT: the boundary — when a skill is the WRONG answer
    rx, rw = 8.05, 4.77
    ocean_box(s, rx, 1.08, rw, 1.56, fill=SOFT_GREY, stroke=SLATE,
              stroke_pt=1.2)
    icon(s, "circle-slash", rx + 0.20, 1.18, 0.40, "mid")
    text_box(s, x=rx + 0.72, y=1.20, w=rw - 0.92, h=0.28,
             text="Когда skill не нужен", size=12.5, bold=True, color=DEEP)
    # each line kept short enough to NOT wrap — a wrapped bullet loses its
    # hanging indent here and reads as a fifth item (visual-loop iter 2).
    text_box(s, x=rx + 0.22, y=1.58, w=rw - 0.44, h=1.08,
             text="• нужно каждый ход (сборка, тесты) — это AGENTS.md\n"
                  "• разовая задача — достаточно попросить в чате\n"
                  "• один факт, а не процедура — строка в AGENTS.md\n"
                  "• «обо всём сразу» — модель не выберет такой skill",
             size=10.5, color=DEEP, line_spacing=1.30)

    # loading-mode mechanic — kept, but compact (this is WHY the split works)
    my = 3.02
    filled_rect(s, rx, my, rw, 1.10, SURFACE, stroke=LIGHT, stroke_pt=1.2,
                radius=True, radius_adj=0.08)
    text_runs(s, rx + 0.20, my + 0.14, rw - 0.40, 0.88, [
        {"text": "AGENTS.md", "size": 11, "bold": True, "color": MID},
        {"text": " — в контексте каждый ход, платите за него всегда.",
         "size": 10.5, "color": DEEP},
        {"text": "SKILL.md", "size": 11, "bold": True, "color": TEAL,
         "newpara": True, "space_before": 4},
        {"text": " — грузится только по вызову, до вызова стоит ноль.",
         "size": 10.5, "color": DEEP},
    ], line_spacing=1.14)

    text_box(s, x=rx, y=4.34, w=rw, h=1.10,
             text="Честно: формат открыт (Agent Skills standard) и "
                  "подтверждён у Codex CLI, но у Cursor слоя «по требованию» "
                  "нет — там правила, активные всегда. «Инструмент "
                  "поддерживает skills» стоит уточнять.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Правило разделения: нужно каждый ход — в AGENTS.md; редко, но "
        "подробно — в skill; один раз — просто скажите в чате.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20b")
    notes_with_sources(s, "s20b")
    return s


# ============================================================
# s20c — MCP for coding agent (agent centre + 3 servers + Lethal Trifecta bridge)
# ============================================================
def s20c(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "MCP убирает человека-мост — ценой более узкого доступа к системе",
        size=20, w=12.3, h=0.60)

    # top: agent + 3 MCP server cards
    ay = 1.26
    ah = 1.42
    # agent centre-left small box
    agx, agw = 0.55, 2.10
    ocean_box(s, agx, ay, agw, ah)
    icon(s, "bot", agx + agw / 2 - 0.27, ay + 0.14, 0.54, "mid")
    text_box(s, x=agx + 0.06, y=ay + 0.74, w=agw - 0.12, h=0.28,
             text="АГЕНТ", size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, x=agx + 0.06, y=ay + 1.02, w=agw - 0.12, h=0.40,
             text="встроенно: файлы + шелл", size=9.5, italic=True,
             color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.05)

    cards = [
        ("boxes", "GitHub MCP", "задачи, заявки на слияние (pull request), "
         "сборки — по наборам инструментов, включаемым выборочно"),
        ("scan-search", "Playwright MCP", "браузер: структурное дерево "
         "элементов вместо снимка экрана; кликает, заполняет формы"),
        ("link", "Filesystem MCP", "класс серверов: доступ к директориям "
         "ВНЕ рабочей копии — соседний репозиторий, общий диск"),
    ]
    cx0 = agx + agw + 0.55
    ctotal = 13.333 - 0.55 - cx0
    cgap = 0.18
    ccw = (ctotal - cgap * 2) / 3
    # single connector rail ABOVE the cards (clear of all body text), agent → cards
    rail_y = ay - 0.14
    connector(s, agx + agw / 2, ay, agx + agw / 2, rail_y, color=TEAL,
              width=1.6, dash="dash")
    connector(s, agx + agw / 2, rail_y, cx0 + 2 * (ccw + cgap) + ccw / 2, rail_y,
              color=TEAL, width=1.6, dash="dash")
    for i, (ic, name, body) in enumerate(cards):
        x = cx0 + i * (ccw + cgap)
        ocean_box(s, x, ay, ccw, ah)
        icon(s, ic, x + 0.18, ay + 0.12, 0.40, "teal")
        text_box(s, x=x + 0.66, y=ay + 0.14, w=ccw - 0.82, h=0.32,
                 text=name, size=12, bold=True, color=MID)
        text_box(s, x=x + 0.18, y=ay + 0.52, w=ccw - 0.36, h=0.82,
                 text=body, size=9.5, color=DEEP, line_spacing=1.10)
        connector(s, x + ccw / 2, rail_y, x + ccw / 2, ay, color=TEAL,
                  width=1.6, dash="dash")

    # ---- MCP vs direct API / command line: an MCP server is a SUBSET ----
    ny = ay + ah + 0.14
    nh = 1.08
    ocean_box(s, 0.55, ny, 12.25, nh)
    text_box(s, x=0.79, y=ny + 0.10, w=5.10, h=0.28,
             text="MCP уже, чем прямой доступ", size=12.5, bold=True,
             color=MID)
    # two stacked bars: full interface vs the curated MCP toolset
    b1y = ny + 0.42
    filled_rect(s, 0.79, b1y, 4.90, 0.26, SOFT_GREY, stroke=SLATE,
                stroke_pt=0.75, radius=True, radius_adj=0.30)
    text_box(s, x=0.91, y=b1y + 0.01, w=4.70, h=0.24,
             text="полный интерфейс системы: её API и команда в терминале",
             size=9, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)
    b2y = b1y + 0.32
    filled_rect(s, 0.79, b2y, 2.15, 0.26, MID, radius=True, radius_adj=0.30)
    text_box(s, x=0.91, y=b2y + 0.01, w=1.95, h=0.24,
             text="набор инструментов MCP", size=9, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=3.06, y=b2y + 0.01, w=2.60, h=0.24,
             text="— подмножество, а не весь интерфейс", size=9,
             italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=6.00, y=ny + 0.12, w=6.60, h=0.86,
             text="Сервер публикует не весь интерфейс системы, а отобранный "
                  "набор инструментов: чего в наборе нет — агенту недоступно, "
                  "даже если система это умеет. Плюс каждая схема инструмента "
                  "занимает контекст постоянно — поэтому там, где у агента уже "
                  "есть шелл, узкая команда часто дешевле MCP-вызова.",
             size=10, color=DEEP, line_spacing=1.14)

    # ---- risk  →  mitigation (explicit, sequential) ----
    by = ny + nh + 0.14
    bh = 1.52
    lwb = 5.75
    ocean_box(s, 0.55, by, lwb, bh, fill=SOFT_GREY, stroke=SLATE, stroke_pt=1.2)
    icon(s, "shield-alert", 0.77, by + 0.12, 0.40, "mid")
    text_box(s, x=1.25, y=by + 0.14, w=lwb - 0.92, h=0.28,
             text="Опасность: одно подключение — два угла из трёх",
             size=11, bold=True, color=DEEP)
    text_box(s, x=0.77, y=by + 0.46, w=lwb - 0.44, h=1.00,
             text="Смертельная тройка (Lethal Trifecta): доступ к данным + "
                  "канал наружу + недоверенный контент. Один сервер обычно "
                  "даёт первые два разом, а третий приходит тем же каналом. "
                  "Задокументировано: спрятанные в публичных задачах "
                  "инструкции выводили данные приватных репозиториев через "
                  "создаваемые заявки на слияние.",
             size=9.5, color=DEEP, line_spacing=1.10)

    right_arrow(s, 6.42, by + bh / 2 - 0.20, 0.50, 0.40, fill=GOLD)

    rwb = 5.75
    rxb = 7.05
    ocean_box(s, rxb, by, rwb, bh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=1.5)
    icon(s, "shield-check", rxb + 0.22, by + 0.12, 0.40, "teal")
    text_box(s, x=rxb + 0.70, y=by + 0.14, w=rwb - 0.92, h=0.28,
             text="Чем закрывается", size=11.5, bold=True, color=TEAL)
    text_box(s, x=rxb + 0.22, y=by + 0.44, w=rwb - 0.44, h=1.02,
             text="1. Только чтение по умолчанию — инструменты записи "
                  "пропускаются, даже если агент их запросил.\n"
                  "2. Запись открывают под конкретную задачу, отдельным "
                  "решением, а не настройкой из коробки.\n"
                  "3. Минимум подключённых серверов — меньше углов и "
                  "контекста.",
             size=9.5, color=DEEP, line_spacing=1.10)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Это риск, а не удобство: по умолчанию — только чтение, а доступ на "
        "запись открывают осознанно и под задачу.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20c")
    notes_with_sources(s, "s20c")
    return s


# ============================================================
# s20d — Git conventions as contract (commit / branch / PR cards)
# ============================================================
def s20d(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Git-конвенции — договорённость команды, а не требование git",
        size=19, w=12.3, h=0.58)

    x0 = 0.55
    total = 12.25

    # ---- what a "convention" even is: the meaning before the syntax ----
    dy = 1.06
    ocean_box(s, x0, dy, total, 0.78, fill=TEAL_TINT, stroke=TEAL,
              stroke_pt=1.4)
    icon(s, "users", x0 + 0.20, dy + 0.18, 0.42, "teal")
    text_box(s, x=x0 + 0.76, y=dy + 0.10, w=total - 0.96, h=0.62,
             text="Сам git безразличен к тому, что написано в сообщении "
                  "коммита и как названа ветка, — он ничего из этого не "
                  "проверяет. Конвенция — добровольная договорённость "
                  "команды, записанная в AGENTS.md: оформлять историю "
                  "одинаково, чтобы её могли разобрать и человек, и "
                  "программа. Агент следует только той договорённости, "
                  "которую видит записанной.",
             size=11, color=DEEP, line_spacing=1.14)

    # ---- three conventions: what it IS, and what breaks without it ----
    cy = 1.94
    ch = 3.30
    gap = 0.20
    cw = (total - gap * 2) / 3
    cols = [
        ("git-compare", "Коммит", MID, "mid",
         "Заранее согласованный вид первой строки коммита: сначала помета "
         "«что это за изменение», потом описание.",
         "feat(auth): вход по одноразовому коду\nfix(api): не терять "
         "заголовок при повторе",
         "Помету читает не человек, а программа: по ней сами собираются "
         "список изменений релиза и новый номер версии (fix → 2.4.1, "
         "feat → 2.5.0). Агент коммитит на порядок чаще человека — "
         "перечитывать каждый коммит глазами уже некому."),
        ("git-branch", "Ветка", TEAL, "teal",
         "Тип задачи, косая черта, короткое описание строчными буквами. Для "
         "веток агента — отдельные приставки.",
         "claude/security-patch\nai/refactor-auth-flow",
         "Имя ветки — единственное, что ревьюер видит до того, как открыл "
         "изменения. Приставка сразу говорит, что ветку вёл агент, и на "
         "такие ветки можно повесить своё правило. Без договорённости "
         "список веток — это «test2» и «fix-final»."),
        ("git-pull-request", "Описание", MID, "mid",
         "Заявка на слияние (pull request) — окно, где изменения "
         "показывают человеку до попадания в общий код.",
         "Зачем → Что изменилось → Что не трогали →\n"
         "Чем проверено → Риски → Что отложено",
         "Ревьюер тратит время на проверку, а не на восстановление "
         "замысла. Больше всего экономит строка «что не трогали»: не искать "
         "побочные эффекты там, где их не было. Без шаблона каждая заявка "
         "оформлена по-своему. Шаблон агент заполняет по ходу работы."),
    ]
    for i, (ic, tag, col, var, what, mono, why) in enumerate(cols):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, cy, cw, ch)
        chip(s, x + 0.20, cy + 0.14, 1.55, 0.34, tag, fill=col, color=WHITE,
             size=11)
        icon(s, ic, x + cw - 0.62, cy + 0.12, 0.40, var)
        text_box(s, x=x + 0.20, y=cy + 0.58, w=cw - 0.40, h=0.20,
                 text="ЧТО ЭТО", size=9, bold=True, color=LIGHT)
        text_box(s, x=x + 0.20, y=cy + 0.80, w=cw - 0.40, h=0.52,
                 text=what, size=9.5, color=DEEP, line_spacing=1.14)
        filled_rect(s, x + 0.20, cy + 1.36, cw - 0.40, 0.42, WHITE,
                    stroke=SOFT_GREY, stroke_pt=1.0, radius=True,
                    radius_adj=0.10)
        text_box(s, x=x + 0.30, y=cy + 1.42, w=cw - 0.60, h=0.32,
                 text=mono, size=8, color=SLATE, font=FONT_MONO,
                 line_spacing=1.12)
        text_box(s, x=x + 0.20, y=cy + 1.86, w=cw - 0.40, h=0.20,
                 text="ЗАЧЕМ ЭТО НУЖНО", size=9, bold=True, color=LIGHT)
        text_box(s, x=x + 0.20, y=cy + 2.08, w=cw - 0.40, h=1.10,
                 text=why, size=9.5, color=DEEP, line_spacing=1.12)

    text_box(s, x=x0, y=cy + ch + 0.10, w=total, h=0.30,
             text="Правило, общее для всех трёх: агент никогда не коммитит "
                  "прямо в общую ветку — каждая задача получает свою. То же, "
                  "что курс требует от людей.",
             size=10.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER,
             line_spacing=1.08)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Договорённость, которая нигде не записана, не работает: агент "
        "следует только тому правилу, которое видит в AGENTS.md.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20d")
    notes_with_sources(s, "s20d")
    return s


# ============================================================
# s20e — Task logging layer: 3 patterns matrix (schema_matrix)
# ПРАВКА (issue #162, student-simulator QA 2026-09-19): 5-строчная матрица
# не проходила 5-секундный тест (слишком плотно для visible-слоя). Сокращено
# до 3 самых контрастных критериев (Solo vs команда / Длительность задачи /
# Аудит-след) + компактная строка примеров (1 токен на колонку). Полная
# 5-строчная таблица остаётся в главе §3.3e и в speaker notes (не тронуты).
# ============================================================
def s20e(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Логирование наращивают под задачу, а не берут максимум",
        size=20, w=12.3, h=0.60)

    x0 = 0.55
    total = 12.25
    gap = 0.16
    cw = (total - gap * 2) / 3

    # progression caption — the ordering principle, stated outright
    text_box(s, x=x0, y=1.06, w=total, h=0.26,
             text="СЛОЖНОСТЬ НАРАСТАЕТ СЛЕВА НАПРАВО:  один файл  →  набор "
                  "файлов в одной папке  →  структура папок",
             size=11, bold=True, color=LIGHT)

    # columns ordered simple → elaborate; header fill darkens with complexity
    cols = [
        ("list-ordered", "(а) Один файл — общий лог", LIGHT),
        ("clipboard-list", "(б) Папка, файл на задачу", MID),
        ("file-stack", "(в) Папка на задачу + файлы", DEEP),
    ]
    rows = [
        ("Один или команда",
         ["Команда — общая хронология, но частые конфликты слияния",
          "Команда среднего размера — конфликтов меньше",
          "Один разработчик или малая команда; плодит директории"]),
        ("Длительность задачи",
         ["Короткие, частые",
          "«1 окно контекста = 1 заявка на слияние»",
          "Долгоживущая, сложная"]),
        ("Аудит-след",
         ["Хронологический — «что и когда»",
          "Частичный — итог + структурированные поля",
          "Детальный — промежуточные шаги мышления"]),
    ]
    examples = ["notes/decisions.md", "Backlog.md", "notes/research/*.md"]

    top = 1.30
    hh = 0.52
    for i, (ic, name, col) in enumerate(cols):
        x = x0 + i * (cw + gap)
        filled_rect(s, x, top, cw, hh, col, radius=True, radius_adj=0.12)
        icon(s, ic, x + 0.14, top + 0.06, 0.40, "white")
        text_box(s, x=x + 0.62, y=top + 0.03, w=cw - 0.72, h=hh - 0.06,
                 text=name, size=11.5, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.98)

    row_h = [0.80, 0.58, 0.72]
    ry = top + hh + 0.06
    for r, (label, cells) in enumerate(rows):
        rh = row_h[r]
        for i in range(3):
            x = x0 + i * (cw + gap)
            fill = SURFACE if r % 2 == 0 else WHITE
            filled_rect(s, x, ry, cw, rh, fill, stroke=SOFT_GREY, stroke_pt=1.0,
                        radius=True, radius_adj=0.06)
            if i == 0:
                text_box(s, x=x + 0.14, y=ry + 0.04, w=cw - 0.28, h=0.24,
                         text=label.upper(), size=12, bold=True, color=LIGHT)
                tb_y = ry + 0.30
                tb_h = rh - 0.36
            else:
                tb_y = ry + 0.07
                tb_h = rh - 0.14
            text_box(s, x=x + 0.14, y=tb_y, w=cw - 0.28, h=tb_h,
                     text=cells[i], size=14, color=DEEP, line_spacing=1.06)
        ry += rh + 0.06

    # compact example line — one token per column, not a full sentence
    ey = ry + 0.00
    text_runs(s, x0, ey, total, 0.30, [
        {"text": "Пример:  ", "size": 11, "bold": True, "color": SLATE},
        {"text": examples[0], "size": 11, "italic": True, "color": LIGHT,
         "font": FONT_MONO},
        {"text": "   ·   ", "size": 11, "color": SLATE},
        {"text": examples[1], "size": 11, "italic": True, "color": MID,
         "font": FONT_MONO},
        {"text": "   ·   ", "size": 11, "color": SLATE},
        {"text": examples[2], "size": 11, "italic": True, "color": DEEP,
         "font": FONT_MONO},
    ])

    # ---- the fourth option: keep the log in the tracker, not in the repo ----
    ny = ey + 0.32
    nh = 1.14
    lwn = 8.20
    ocean_box(s, x0, ny, lwn, nh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=1.4)
    icon(s, "layout-grid", x0 + 0.18, ny + 0.08, 0.38, "teal")
    text_box(s, x=x0 + 0.64, y=ny + 0.09, w=lwn - 0.84, h=0.26,
             text="Четвёртый вариант — лог в трекере (Jira, Linear, "
                  "GitHub Issues)",
             size=11, bold=True, color=TEAL)
    text_runs(s, x0 + 0.18, ny + 0.44, lwn - 0.36, 0.64, [
        {"text": "За: ", "size": 9.5, "bold": True, "color": TEAL},
        {"text": "виден нетехническим участникам, ложится в уже принятый "
                 "процесс команды, не засоряет репозиторий.",
         "size": 9.5, "color": DEEP},
        {"text": "Против: ", "size": 9.5, "bold": True, "color": DEEP,
         "newpara": True, "space_before": 2},
        {"text": "лежит вне файлового контекста агента — нужен мост через "
                 "MCP или API; лишняя внешняя зависимость и сетевой вызов "
                 "вместо локального чтения.",
         "size": 9.5, "color": DEEP},
    ], line_spacing=1.08)

    rxn = x0 + lwn + 0.10
    rwn = total - lwn - 0.10
    filled_rect(s, rxn, ny, rwn, nh, SOFT_GREY, stroke=SLATE, stroke_pt=0.75,
                radius=True, radius_adj=0.08)
    text_runs(s, rxn + 0.16, ny + 0.10, rwn - 0.32, 0.94, [
        {"text": "Вообще не лог задач: ", "size": 9.5, "bold": True,
         "color": SLATE},
        {"text": "встроенный TodoWrite/Task* живёт внутри одной сессии; "
                 "история коммитов как единственный лог — рабочий, но нигде "
                 "не формализованный вариант.",
         "size": 9.5, "italic": True, "color": SLATE},
    ], line_spacing=1.08)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Критерий составной: кто работает + как долго живёт задача + зачем "
        "нужен аудит-след — а не то, что первым попалось.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20e")
    notes_with_sources(s, "s20e")
    return s


# ============================================================
# s20f — git worktree: «своя папка на сессию» как СХЕМА (#162 r6)
# Round-6: пример «~2 часа» перестал быть главным героем слайда —
# основной носитель смысла теперь диаграмма «без worktree / с worktree»
# (одна строка «ИСТОРИЯ .git» намеренно одинакова в обеих панелях).
# ============================================================
def _down_arrow(s, cx, y, h=0.22, w=0.17, fill=LIGHT):
    """Вертикальная стрелка потока для схемы s20f (аналог right_arrow)."""
    shp = s.shapes.add_shape(MSO_SHAPE.DOWN_ARROW,
                             Inches(cx - w / 2), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    try:
        from _helpers import disable_shadow
        disable_shadow(shp)
    except Exception:
        pass
    return shp


def s20f(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "У каждой параллельной сессии — своя папка; общая у них только история",
        size=20, w=12.3, h=0.58)

    # ---------- geometry of the two-panel schema ----------
    labx, labw = 0.55, 1.00
    pax, pbx, pw = 1.66, 7.38, 5.42
    ptop, phh = 0.98, 2.88
    pad = 0.16
    innw = pw - pad * 2
    cw = (innw - 0.12 * 2) / 3            # session chip / folder cell width

    r1y, r1h = 1.38, 0.54                 # СЕССИИ
    r2y, r2h = 2.14, 0.62                 # ФАЙЛЫ В РАБОТЕ
    r3y, r3h = 2.98, 0.54                 # ИСТОРИЯ .git

    # ---------- row labels (сетка читается один раз, не дважды) ----------
    for yy, hh, lab in ((r1y, r1h, "СЕССИИ"),
                        (r2y, r2h, "ФАЙЛЫ\nВ РАБОТЕ"),
                        (r3y, r3h, "ИСТОРИЯ\n.git")):
        text_box(s, x=labx, y=yy - 0.06, w=labw, h=hh + 0.12,
                 text=lab, size=9.5, bold=True, color=LIGHT,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.06)

    sessions = ["Сессия A", "Сессия B", "Сессия C"]

    # =========== PANEL A — без worktree ===========
    ocean_box(s, pax, ptop, pw, phh, fill=WHITE, stroke=SLATE, stroke_pt=1.2)
    icon(s, "triangle-alert", pax + pad, ptop + 0.06, 0.34, "gold")
    text_box(s, x=pax + pad + 0.44, y=ptop + 0.06, w=pw - pad * 2 - 0.44, h=0.30,
             text="Без worktree — одна папка на всех", size=12, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    for i, name in enumerate(sessions):
        x = pax + pad + i * (cw + 0.12)
        chip(s, x, r1y, cw, r1h, name, fill=MID, color=WHITE, size=11)
        _down_arrow(s, x + cw / 2, r1y + r1h + 0.02, 0.20, 0.17, SLATE)

    filled_rect(s, pax + pad, r2y, innw, r2h, SOFT_GREY, stroke=SLATE,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    icon(s, "file-stack", pax + pad + 0.14, r2y + 0.13, 0.34, "mid")
    text_box(s, x=pax + pad + 0.56, y=r2y + 0.06, w=innw - 0.70, h=0.24,
             text="одна рабочая копия на всех", size=10.5, bold=True,
             color=DEEP)
    text_box(s, x=pax + pad + 0.56, y=r2y + 0.30, w=innw - 0.70, h=0.26,
             text="незакоммиченные правки лежат в одних и тех же файлах",
             size=9.5, color=SLATE)
    _down_arrow(s, pax + pw / 2, r2y + r2h + 0.06, 0.20, 0.17, SLATE)

    filled_rect(s, pax + pad, r3y, innw, r3h, SOFT_GREY, stroke=SLATE,
                stroke_pt=1.2, radius=True, radius_adj=0.09)
    icon(s, "git-branch", pax + pad + 0.14, r3y + 0.09, 0.34, "mid")
    text_box(s, x=pax + pad + 0.56, y=r3y + 0.04, w=innw - 0.70, h=r3h - 0.08,
             text="одна история репозитория", size=10.5, bold=True, color=DEEP,
             anchor=MSO_ANCHOR.MIDDLE)

    text_box(s, x=pax, y=ptop + phh + 0.06, w=pw, h=0.36,
             text="Что ломается: одна сессия незаметно переключает рабочее "
                  "дерево другой — claude-code #60295. Курс терял на этом часы.",
             size=10, color=SLATE, line_spacing=1.12)

    # =========== PANEL B — с worktree ===========
    ocean_box(s, pbx, ptop, pw, phh, fill=SURFACE, stroke=TEAL, stroke_pt=1.6)
    icon(s, "shield-check", pbx + pad, ptop + 0.06, 0.34, "teal")
    text_box(s, x=pbx + pad + 0.44, y=ptop + 0.06, w=pw - pad * 2 - 0.44, h=0.30,
             text="С worktree — своя папка каждой сессии", size=12, bold=True,
             color=TEAL, anchor=MSO_ANCHOR.MIDDLE)

    folders = ["/wt-a", "/wt-b", "/wt-c"]
    for i, (name, path_) in enumerate(zip(sessions, folders)):
        x = pbx + pad + i * (cw + 0.12)
        chip(s, x, r1y, cw, r1h, name, fill=MID, color=WHITE, size=11)
        _down_arrow(s, x + cw / 2, r1y + r1h + 0.02, 0.20, 0.17, TEAL)
        filled_rect(s, x, r2y, cw, r2h, TEAL_TINT, stroke=TEAL, stroke_pt=1.3,
                    radius=True, radius_adj=0.10)
        text_box(s, x=x + 0.06, y=r2y + 0.06, w=cw - 0.12, h=0.24,
                 text=path_, size=10.5, bold=True, color=TEAL,
                 font=FONT_MONO, align=PP_ALIGN.CENTER)
        text_box(s, x=x + 0.06, y=r2y + 0.30, w=cw - 0.12, h=0.26,
                 text="своя ветка", size=9.5, color=SLATE,
                 align=PP_ALIGN.CENTER)
        _down_arrow(s, x + cw / 2, r2y + r2h + 0.06, 0.20, 0.17, TEAL)

    filled_rect(s, pbx + pad, r3y, innw, r3h, SOFT_GREY, stroke=SLATE,
                stroke_pt=1.2, radius=True, radius_adj=0.09)
    icon(s, "git-branch", pbx + pad + 0.14, r3y + 0.09, 0.34, "mid")
    text_box(s, x=pbx + pad + 0.56, y=r3y + 0.04, w=innw - 0.70, h=r3h - 0.08,
             text="история та же — этот уровень не изменился", size=10.5,
             bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    text_box(s, x=pbx, y=ptop + phh + 0.06, w=pw, h=0.36,
             text="Что меняется: разведены только файлы. Ветки и коммиты "
                  "общие — папка не копия репозитория, а вид на ту же историю.",
             size=10, color=SLATE, line_spacing=1.12)

    # ---------- bottom band: команды · принуждение · честная оговорка ----------
    by, bh = 4.32, 1.20
    c1x, c1w = 0.55, 4.10
    c2x, c2w = 4.80, 3.50
    c3x, c3w = 8.50, 4.30

    ocean_box(s, c1x, by, c1w, bh)
    text_box(s, x=c1x + 0.18, y=by + 0.08, w=c1w - 0.36, h=0.22,
             text="Две команды — и папка готова", size=10.5, bold=True,
             color=MID)
    for i, line in enumerate(["git worktree add --detach /wt-a <коммит>",
                              "cd /wt-a && git checkout -b задача-A"]):
        text_box(s, x=c1x + 0.18, y=by + 0.34 + i * 0.25, w=c1w - 0.36, h=0.23,
                 text=line, size=9, color=SLATE, font=FONT_MONO,
                 line_spacing=1.0)
    text_box(s, x=c1x + 0.18, y=by + 0.86, w=c1w - 0.36, h=0.26,
             text="Дешевле клонирования: история не дублируется.",
             size=9.5, italic=True, color=SLATE)

    ocean_box(s, c2x, by, c2w, bh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=1.4)
    icon(s, "lock", c2x + 0.16, by + 0.10, 0.32, "teal")
    text_box(s, x=c2x + 0.54, y=by + 0.10, w=c2w - 0.70, h=0.22,
             text="Не на честном слове", size=10.5, bold=True, color=TEAL)
    text_box(s, x=c2x + 0.16, y=by + 0.38, w=c2w - 0.32, h=0.64,
             text="Claude Code блокирует правки с рабочей директорией вне "
                  "назначенной папки: соседнюю сессию нельзя задеть даже по "
                  "ошибке.",
             size=9.5, color=DEEP, line_spacing=1.12)

    filled_rect(s, c3x, by, c3w, bh, SOFT_GREY, stroke=SLATE, stroke_pt=0.9,
                radius=True, radius_adj=0.07)
    text_box(s, x=c3x + 0.16, y=by + 0.10, w=c3w - 0.32, h=0.22,
             text="Граница: общий .git — общий замок", size=10.5, bold=True,
             color=SLATE)
    text_box(s, x=c3x + 0.16, y=by + 0.36, w=c3w - 0.32, h=0.72,
             text="Файлы разведены, а .git один на всех: 8 из 13 параллельных "
                  "агентов потеряли несохранённую работу на замке "
                  ".git/index.lock. При 5 сессиях — изредка, при 10+ — "
                  "почти наверняка.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.12)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Механика worktree старше любого AI-агента; новое — только частота: "
        "параллельные сессии делают общую папку дорогой ошибкой каждый день.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20f", size=8.0)
    notes_with_sources(s, "s20f")
    return s


# ============================================================
# s20g (NEW, #162 round 3) — Register .env case + permissions.deny
# Bash-bypass limit + Gitleaks/TruffleHog 3-layer defense
# ============================================================
def s20g(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Секреты — отдельный контракт: .gitignore не значит «агент тоже не прочитает»",
        size=18.5, w=12.3, h=0.82)

    lx, lw = 0.55, 6.55
    rx, rw = 7.30, 5.50
    top = 1.44

    # --- LEFT: Register incident + permissions.deny limit ---
    ocean_box(s, lx, top, lw, 1.98)
    icon(s, "key", lx + 0.22, top + 0.14, 0.46, "mid")
    text_box(s, x=lx + 0.82, y=top + 0.18, w=lw - 1.06, h=0.36,
             text="The Register, 2026-01-28 [1]", size=12.5, bold=True,
             color=MID)
    text_box(s, x=lx + 0.24, y=top + 0.62, w=lw - 0.48, h=0.80,
             text="Claude Code (v2.1.12) читал .env вопреки и .gitignore, и "
                  ".claudeignore — предупреждает об учётных данных, но всё "
                  "равно печатает содержимое. Минимум 4 открытых тикета.",
             size=10.5, color=DEEP, line_spacing=1.14)
    filled_rect(s, lx + 0.24, top + 1.44, lw - 0.48, 0.48, TEAL_TINT,
                stroke=TEAL, stroke_pt=1.2, radius=True, radius_adj=0.10)
    text_box(s, x=lx + 0.40, y=top + 1.49, w=lw - 0.80, h=0.38,
             text='«"Ignored by git" and "ignored by Claude Code" are two '
                  'different things.»',
             size=9.5, italic=True, color=DEEP, font=FONT_MONO,
             anchor=MSO_ANCHOR.MIDDLE)

    ocean_box(s, lx, top + 2.14, lw, 1.90, fill=SOFT_GREY, stroke=LIGHT,
              stroke_pt=1.0)
    icon(s, "shield-alert", lx + 0.22, top + 2.28, 0.44, "mid")
    text_box(s, x=lx + 0.80, y=top + 2.30, w=lw - 1.04, h=0.36,
             text="permissions.deny не блокирует Bash", size=12, bold=True,
             color=DEEP)
    text_box(s, x=lx + 0.24, y=top + 2.72, w=lw - 0.48, h=1.20,
             text="deny(Read(./.env)) блокирует встроенный file-tool — но "
                  "`cat .env` через Bash обходит правило. Два независимых "
                  "контракта: закрытие требует OS-level sandboxing.",
             size=10.5, color=DEEP, line_spacing=1.16)

    # --- RIGHT: 3-layer defense ---
    layers = [
        ("1", "pre-commit hook (Gitleaks)", "локально, быстро — но обходим "
         "--no-verify: рекомендательный барьер, не обязывающий."),
        ("2", "CI-gate (Gitleaks + TruffleHog verified)", "на каждый PR — "
         "обязывающий гейт: CI не обойти веткой мимо хука."),
        ("3", "server-side push-protection", "на уровне git-хостинга — "
         "устойчив даже к обходу клиентских хуков."),
    ]
    ocean_box(s, rx, top, rw, 4.10, fill=SURFACE, stroke=MID, stroke_pt=1.6)
    icon(s, "lock", rx + 0.22, top + 0.16, 0.46, "teal")
    text_box(s, x=rx + 0.82, y=top + 0.20, w=rw - 1.04, h=0.36,
             text="3-слойная защита", size=13, bold=True, color=MID)
    ly = top + 0.72
    for num, head, body in layers:
        circle(s, rx + 0.24, ly, 0.36, MID)
        text_box(s, x=rx + 0.24, y=ly, w=0.36, h=0.36, text=num, size=13,
                 bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rx + 0.72, y=ly - 0.02, w=rw - 0.98, h=0.32, text=head,
                 size=11.5, bold=True, color=DEEP, line_spacing=1.0)
        text_box(s, x=rx + 0.72, y=ly + 0.32, w=rw - 0.98, h=0.62, text=body,
                 size=10, color=DEEP, line_spacing=1.14)
        ly += 1.10

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "То, что коммитить, и то, что агенту разрешено читать, — два разных, "
        "независимо настраиваемых контракта; закрытие одного не закрывает другой.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20g")
    notes_with_sources(s, "s20g")
    return s


# ============================================================
# s20 — 70% problem (curve + 3 numbers) [in-bucket]
# ============================================================
def s20(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "70%-проблема: AI ускоряет первые 70%, но не последние 30% — понимание",
        size=22, w=12.2, h=0.82)

    # left: 70% curve concept
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.52, lw, 4.02)
    # a simple two-part bar showing 70% fast / 30% hard
    by = 1.98
    filled_rect(s, lx + 0.30, by, (lw - 0.60) * 0.70, 0.70, TEAL,
                radius=True, radius_adj=0.10)
    filled_rect(s, lx + 0.30 + (lw - 0.60) * 0.70, by, (lw - 0.60) * 0.30, 0.70,
                GOLD, radius=True, radius_adj=0.10)
    text_box(s, x=lx + 0.30, y=by + 0.16, w=(lw - 0.60) * 0.70, h=0.4,
             text="первые ~70% — быстро, дёшево", size=11, bold=True,
             color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 0.30 + (lw - 0.60) * 0.70, y=by + 0.10,
             w=(lw - 0.60) * 0.30, h=0.5,
             text="последние 20–30%", size=10, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 0.30, y=by + 0.80, w=lw - 0.60, h=0.90,
             text="Последние 20–30% — краевые случаи, обработка ошибок, "
                  "безопасность, интеграция, поведение под нагрузкой — остаются "
                  "такими же трудными и требуют senior-надзора. Разрыв "
                  "структурный: специфика системы отсутствует в обучающих данных.",
             size=10.5, color=DEEP, line_spacing=1.14)
    filled_rect(s, lx + 0.30, 3.86, lw - 0.60, 1.44, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.6, radius=True, radius_adj=0.05)
    text_box(s, x=lx + 0.52, y=3.96, w=lw - 1.04, h=1.28,
             text="«Почти правильный» код дороже явно неправильного: он проходит "
                  "беглый взгляд и ломается на краевом случае. Работа смещается с "
                  "написания на отладку чужой правдоподобной логики.",
             size=11, bold=True, color=DEEP, line_spacing=1.16,
             anchor=MSO_ANCHOR.MIDDLE)

    # right: three numbers with baseline
    rx, rw = 6.85, 5.95
    nums = [
        ("Stack Overflow 2025: 66%",
         "разработчиков назвали главной фрустрацией «решения почти правильные, но "
         "не совсем».", 0.82),
        ("GitClear · два независимых замера [2]",
         "211 млн строк (2020–24): клоны 8,3→12,3%, рефакторинг ~25→<10%, "
         "churn 3,3→5,7%.\n"
         "623 млн изменений (2023–26): рефакторинг 21→3,8% (−70%), дубли "
         "40,3→73,0/млн строк (+81%), churn +15%.\n"
         "(Оба — корреляция, не RCT.)",
         1.30),
        ("Парадокс знания (Osmani) [1]",
         "seniors оспаривают вывод AI, juniors принимают («карточный домик») — AI "
         "усиливает опытных больше.", 0.72),
    ]
    ny = 1.48
    for i, (head, body, bh) in enumerate(nums):
        y = ny
        ocean_box(s, rx, y, rw, 0.32 + bh)
        text_box(s, x=rx + 0.24, y=y + 0.08, w=rw - 0.48, h=0.30, text=head,
                 size=12, bold=True, color=MID)
        text_box(s, x=rx + 0.24, y=y + 0.40, w=rw - 0.48, h=bh - 0.06,
                 text=body, size=10, color=DEEP, line_spacing=1.10)
        ny += 0.32 + bh + 0.10

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Альтернатива — малые проверяемые единицы + харнес + читать diff до "
        "accept; метрики дублирования и churn в CI как гейт. Merge — всегда человек.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    # Round-5 meme: Hide the Pain Harold (both panels — same face, same
    # smile, the point is that NOTHING visibly changes) — "почти правильный
    # код" looks fine right up until it doesn't.
    add_image(s, WEB / "band-hide-the-pain-harold-merged.png", 8.01, 6.40,
              4.79, 0.64)
    refs_of_slide(s, "s21")
    notes_with_sources(s, "s21")
    return s
