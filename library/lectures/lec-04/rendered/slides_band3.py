"""Лекция 4 v4 — Band 3 (s21–s30): анти-хайп, тестирование, ревью+безопасность."""
from _helpers import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    right_arrow, circle, chip, connector, add_image, icon, slide_title,
    gold_callout, teal_callout, footer, src, speaker_notes, load_notes, notes_with_sources, refs_of_slide,
    build_section_divider, ref_list, refs_of, link_run, URLS,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE, COVER_OUTLINE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, MID_TINT, ICONS, CHARTS, ASSETS, WEB,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

SCR = ASSETS / "screenshots"


# ============================================================
# s21 — REMOVED (round 6, block 3). Display slide 32 «Бренд и бенчмарк-число ≠
# инженерная дисциплина» (SWE-bench Verified/Pro разрыв + Devin/OpenAI/Cursor +
# «пять вопросов к вендорскому числу») удалён по прямому указанию владельца
# («слайд 32 — лишний, убрать»). Разрыв Verified/Pro введён в Лекции 3; вендор-
# скепсис в этой лекции держат s20 (70%-проблема), s37 (триангуляция) и s38
# (risk-triad, «вероятность растёт с незнакомостью задачи»). Chart
# c21-swe-bench.png и meme band-mocking-spongebob.png оставлены в assets —
# их использует EN-дек (slides_band3_en.py).
# ============================================================


# ============================================================
# s22 — section divider Раздел 4 (Тестирование)
# ============================================================
def s22(p):
    return build_section_divider(
        p, here_idx=4,
        subtitle="Тестирование — TDD как дисциплина",
        bridge="Реализация производит код — тестирование производит проверенное "
               "утверждение о его корректности. Ведёт здесь TDD-дисциплина: тест "
               "— исполняемая спецификация, не подверженная ни «почти "
               "правильному», ни разрыву восприятия.",
        sid="s23",
        tag="Сильная при роли · тест-как-спека · 1 провал")


# ============================================================
# s23 — TDD discipline (red-green-refactor cycle + role split + nuance)
# ============================================================
def s23(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "TDD с кодинг-агентом: не ритуал «сначала тест», а пять шагов, "
           "которые работают",
        size=21, w=12.3, h=0.82)

    # left: red-green-refactor cycle
    lx, lw = 0.55, 5.20
    ocean_box(s, lx, 1.40, lw, 4.10)
    text_box(s, x=lx + 0.24, y=1.50, w=lw - 0.48, h=0.34,
             text="Цикл red-green-refactor (Kent Beck, TDD) [1] — человек владеет "
                  "спекой теста", size=12, bold=True, color=MID,
             line_spacing=1.0)
    cyc = [
        ("red", "падающий тест выражает требование", GOLD, True),
        ("green", "код, который его проходит", MID, False),
        ("refactor", "улучшить, сохранив зелёный", TEAL, False),
    ]
    cy0 = 1.96
    for i, (name, desc, col, start) in enumerate(cyc):
        y = cy0 + i * 0.64
        filled_rect(s, lx + 0.28, y, lw - 0.56, 0.54,
                    (GOLD_TINT if start else SURFACE),
                    stroke=col, stroke_pt=(1.8 if start else 1.2),
                    radius=True, radius_adj=0.10)
        if start:
            circle(s, lx + 0.40, y + 0.15, 0.24, GOLD)
        text_box(s, x=lx + (0.76 if start else 0.48), y=y + 0.04, w=1.6, h=0.46,
                 text=name, size=12, bold=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, font="DejaVu Sans Mono")
        text_box(s, x=lx + 2.10, y=y + 0.04, w=lw - 2.42, h=0.46, text=desc,
                 size=10.5, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 0.28, y=3.86, w=lw - 0.56, h=0.18, text="↑ повторяется",
             size=10.5, italic=True, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    # role split
    filled_rect(s, lx + 0.28, 4.14, lw - 0.56, 1.20, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.4, radius=True, radius_adj=0.06)
    text_runs(s, lx + 0.46, 4.26, lw - 0.92, 0.98, [
        {"text": "AI пишет тесты быстро", "size": 11.5, "bold": True,
         "color": TEAL},
        {"text": " — объём (привнесённое). ", "size": 11.5, "color": DEEP},
        {"text": "Человек решает, ЧТО тест должен утверждать", "size": 11.5,
         "bold": True, "color": DEEP},
        {"text": " — существенное.", "size": 11.5, "color": DEEP},
    ])

    # right: what does NOT work → the recipe → tools
    rx, rw = 6.02, 6.78
    filled_rect(s, rx, 1.40, rw, 1.02, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.22, y=1.46, w=rw - 0.44, h=0.28,
             text="Что НЕ работает: приказать агенту писать тесты первыми",
             size=12, bold=True, color=DEEP)
    text_box(s, x=rx + 0.22, y=1.75, w=rw - 0.44, h=0.62,
             text="Böckeler [2]: в цикле агента это дало отсутствие выигрыша и "
                  "примерно втрое больше токенов — «я перестала велеть агентам "
                  "писать тесты первыми». Ценность несёт структура, а не порядок команд.",
             size=10.5, color=DEEP, line_spacing=1.06)

    ocean_box(s, rx, 2.50, rw, 2.58)
    text_box(s, x=rx + 0.22, y=2.57, w=rw - 0.44, h=0.28,
             text="Что работает вместо — рецепт из пяти шагов",
             size=12.5, bold=True, color=MID)
    recipe = [
        ("1", "Человек формулирует, ЧТО тест обязан утверждать",
         " — инвариант или критерий приёмки, до генерации кода."),
        ("2", "Порядок генерации оставьте агенту",
         " — тест и код вместе или код, а следом тест; форсить «сначала тест» не нужно."),
        ("3", "Утверждения теста читает человек",
         ": тест держится за поведение, а не за реализацию (Fowler [3])."),
        ("4", "Прогон — только детерминированный исполнитель",
         " (скрипт или CI с настоящим кодом возврата); «модель сказала: зелёные» — не прогон."),
        ("5", "Гейт — по доле реально пойманных дефектов",
         ", не по проценту покрытия. Каждый инцидент → постоянный регресс-тест."),
    ]
    sy = 2.90
    for i, (num, lead, tail) in enumerate(recipe):
        y = sy + i * 0.43
        filled_rect(s, rx + 0.22, y + 0.03, 0.30, 0.30, TEAL,
                    radius=True, radius_adj=0.28)
        text_box(s, x=rx + 0.22, y=y + 0.05, w=0.30, h=0.28, text=num,
                 size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_runs(s, rx + 0.62, y, rw - 0.86, 0.44, [
            {"text": lead, "size": 11, "bold": True, "color": DEEP},
            {"text": tail, "size": 11, "color": DEEP},
        ], line_spacing=1.06)

    filled_rect(s, rx, 5.16, rw, 0.42, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.07)
    text_box(s, x=rx + 0.22, y=5.21, w=rw - 0.44, h=0.34,
             text="Исполняют (вторично): AWS Q /test · Qodo · JetBrains Junie · "
                  "Anthropic (падающий тест → починка + Stop-hook как гейт).",
             size=10, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Инвариант не «тест написан первым», а «тест существует, утверждает "
        "решённое человеком и прогнан машиной». Willison: «не видел, как "
        "работает — не работающая система».",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s24")
    notes_with_sources(s, "s24")
    return s


# ============================================================
# s24 — all-green lies + coverage vs mutation (Meta chart) [in-bucket]
# ============================================================
def s24(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Зелёные тесты и высокое покрытие могут лгать — гейт нужен честный",
                size=22, w=12.2, h=0.82)

    # left: all-green lies
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.52, lw, 4.02)
    icon(s, "message-square-warning", lx + 0.24, 1.66, 0.5, "mid")
    text_box(s, x=lx + 0.88, y=1.70, w=lw - 1.10, h=0.40,
             text="«all green» лжёт (Fowler) [1]", size=13, bold=True, color=MID)
    text_box(s, x=lx + 0.24, y=2.18, w=lw - 0.48, h=1.00,
             text="«LLM охотно говорит „all tests green“, хотя есть "
                  "падения». Механизм тот же — модель генерирует правдоподобный "
                  "отчёт тем же потокенным сэмплингом.",
             size=11.5, color=DEEP, line_spacing=1.16)
    filled_rect(s, lx + 0.24, 3.24, lw - 0.48, 0.88, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.4, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.46, y=3.34, w=lw - 0.9, h=0.70,
             text="Отчёт AI о прогоне ≠ доказательство прогона. Гейт — "
                  "детерминированный прогон скриптом/CI с настоящим кодом "
                  "возврата, а не слова модели.",
             size=11.5, bold=True, color=DEEP, line_spacing=1.14,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 0.24, y=4.24, w=lw - 0.48, h=1.20,
             text="Coverage обманчиво: строка «затронута» ≠ проверена. Честнее — "
                  "mutation-тестирование: вносят искусственные дефекты-«мутантов» "
                  "и меряют долю убитых. Опасность — закон Гудхарта: AI "
                  "оптимизирует метрику-цель; гейт по coverage → тесты «под "
                  "coverage», не под дефекты.",
             size=11, color=DEEP, line_spacing=1.14)

    # right: Meta chart + numbers
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, 1.52, rw, 4.02)
    add_image(s, CHARTS / "c24-meta-mutation.png", rx + 0.14, 1.66,
              rw - 0.28, 2.55)
    text_box(s, x=rx + 0.24, y=4.28, w=rw - 0.48, h=1.16,
             text="Meta [2]: LLM-генерация покрывает больше классов (32% против "
                  "5,3% у узко-целевого метода), но убивает меньше мутантов "
                  "(2,4% против 15%). Больше тестов и покрытия ≠ лучше "
                  "обнаружение дефектов.",
             size=11, color=DEEP, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Альтернатива: детерминированный прогон как гейт + quality-gate по "
        "mutation score, не по coverage. Инцидент → постоянный регресс-тест.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s25")
    notes_with_sources(s, "s25")
    return s


# ============================================================
# s25b — BDD + trunk-based (2 compact secondary methodologies) [#162 r2]
# ============================================================
def s25b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Ещё две методики на AI-цикл: BDD и trunk-based — что дают и чем "
           "платите",
        size=19, w=12.3, h=0.82)

    colw = 6.05
    gap = 0.15
    lx = 0.55
    rx = lx + colw + gap
    top = 1.24
    boxh = 4.38

    def example(x, text):
        """One concrete micro-example per column — для тех, кто видит впервые."""
        filled_rect(s, x + 0.20, top + 1.24, colw - 0.40, 0.32, SOFT_GREY,
                    stroke=SLATE, stroke_pt=0.75, radius=True, radius_adj=0.16)
        text_box(s, x=x + 0.34, y=top + 1.27, w=colw - 0.68, h=0.28, text=text,
                 size=9.5, italic=True, color=SLATE, line_spacing=1.04,
                 anchor=MSO_ANCHOR.MIDDLE)

    def plus_minus(x, pros, cons, y_plus, y_minus, h_plus, h_minus):
        """Explicit «+ что даёт» / «− чем платите» blocks inside one column."""
        for (yy, hh, sign, label, items, tint, stroke_col, label_col) in (
            (y_plus, h_plus, "+", "ЧТО ДАЁТ", pros, TEAL_TINT, TEAL, TEAL),
            (y_minus, h_minus, "−", "ЧЕМ ПЛАТИТЕ", cons, GOLD_TINT, GOLD, DEEP),
        ):
            filled_rect(s, x + 0.20, yy, colw - 0.40, hh, tint,
                        stroke=stroke_col, stroke_pt=1.4, radius=True,
                        radius_adj=0.06)
            text_runs(s, x + 0.36, yy + 0.06, colw - 0.72, 0.26, [
                {"text": f"{sign}  ", "size": 14, "bold": True,
                 "color": stroke_col},
                {"text": label, "size": 11, "bold": True, "color": label_col},
            ], line_spacing=1.0)
            runs = []
            for j, it in enumerate(items):
                runs.append({"text": ("• " + it), "size": 10.5, "color": DEEP,
                             "newpara": bool(j), "space_before": 4})
            text_runs(s, x + 0.36, yy + 0.34, colw - 0.72, hh - 0.40, runs,
                      line_spacing=1.10)

    # --- LEFT: BDD ---
    ocean_box(s, lx, top, colw, boxh, fill=SURFACE, stroke=MID, stroke_pt=1.6)
    icon(s, "check-check", lx + 0.22, top + 0.14, 0.42, "mid")
    text_box(s, x=lx + 0.78, y=top + 0.16, w=colw - 1.0, h=0.34,
             text="BDD — тест до кода на языке бизнеса", size=13, bold=True,
             color=MID)
    text_box(s, x=lx + 0.22, y=top + 0.54, w=colw - 0.44, h=0.68,
             text="BDD (Behavior-Driven Development, разработка через "
                  "поведение) — сценарий Given-When-Then, который читает и "
                  "правит нетехнический заказчик. Цикл: обсудили примеры → "
                  "записали сценарии → гоняем как тесты.",
             size=10.5, color=DEEP, line_spacing=1.10)
    example(lx, "Given слот свободен · When нажали «Забронировать» · Then "
                "слот занят")
    plus_minus(
        lx,
        ["Пробел в критериях приёмки виден до кода: сценарий читают те, кто "
         "ставит задачу.",
         "Агент генерирует сценарии из критериев приёмки — включая краевые "
         "случаи и проверки безопасности; человек ревьюит."],
        ["Лишний слой: ~27% проектов с открытым кодом, где есть тестовый "
         "фреймворк (68% — Ruby).",
         "Без гайдлайна сценарии от агента деградируют: расплывчатые "
         "Then-шаги, привязка к интерфейсу.",
         "Без нетехнического заказчика рядом — избыточен."],
        top + 1.62, top + 2.92, 1.24, 1.44)

    # --- RIGHT: trunk-based ---
    ocean_box(s, rx, top, colw, boxh, fill=SURFACE, stroke=LIGHT, stroke_pt=1.6)
    icon(s, "git-merge", rx + 0.22, top + 0.14, 0.42, "teal")
    text_box(s, x=rx + 0.78, y=top + 0.16, w=colw - 1.0, h=0.34,
             text="Trunk-based — короткоживущая ветка", size=13, bold=True,
             color=TEAL)
    text_box(s, x=rx + 0.22, y=top + 0.54, w=colw - 0.44, h=0.68,
             text="Trunk-based development — ветка живёт меньше суток (DORA) и "
                  "вливается в основную. Git чинит текстовые конфликты, но не "
                  "смысловые допущения ветки агента.",
             size=10.5, color=DEEP, line_spacing=1.10)
    example(rx, "Ветку claude/fix-auth создали утром — влили до обеда, "
                "за флагом")
    plus_minus(
        rx,
        ["Ветка агента не успевает разойтись с основной по смыслу — а "
         "смысловой дрейф git не чинит.",
         "Маленькие частые изменения: ревью успевает за темпом агентных "
         "коммитов, префикс ветки агента осмыслен."],
        ["Обязательны feature-флаги (включатели функций): без них слияние "
         "незавершённой работы сразу показывает её пользователю.",
         "Нужна страховочная сетка — реальное покрытие тестами и зелёный "
         "детерминированный прогон; без неё частые вливания опаснее долгой "
         "ветки."],
        top + 1.62, top + 2.92, 1.24, 1.44)

    gold_callout(
        s, 0.55, top + boxh + 0.12, 12.25, 0.58,
        "Обе — расширение уже названных практик, а не новая ось: BDD "
        "оправдан там, где есть нетехнический заказчик; trunk-based — там, "
        "где уже есть автоматические проверки и включатели функций.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s25b")
    notes_with_sources(s, "s25b")
    return s


# ============================================================
# s25c — test tooling matrix: API / DB / visual-regression [#162 r2]
# ============================================================
def s25c(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Локальный инструментарий агента: чем закрыть пять его слепых каналов",
        size=20, w=12.3, h=0.78)

    # Five cards, 3 + 2 layout; the sixth cell carries the gold takeaway so the
    # bottom row is not half-empty (visual mass balance).
    cards = [
        ("database", "Данные", "Testcontainers", MID,
         "Поднимает настоящий Postgres / Kafka / Redis в Docker на временном "
         "порту — на машине агента.",
         "Агент проверяет запрос против воображаемой схемы: тест либо не "
         "пишется, либо зелен на заглушке и красен в проде."),
        ("route", "Сеть", "MSW", MID,
         "Перехватывает HTTP внутри процесса: один обработчик и для модульных, "
         "и для сквозных тестов. Вне JS — WireMock (открытый код).",
         "Агент либо бьёт по настоящему API — нестабильно, платно, с "
         "лимитами, — либо не тестирует сетевой код вовсе."),
        ("monitor", "Интерфейс", "Playwright", TEAL,
         "Даёт агенту браузер: не картинку, а дерево элементов страницы "
         "(accessibility) — кликает, заполняет формы, порождает тест.",
         "Агент никогда не видит настоящий интерфейс: отладка фронтенда идёт "
         "вслепую и по сути бессмысленна."),
        ("terminal", "Свои проверки", "skill-обёртка", MID,
         "Упаковывает существующий в репозитории цикл «линтер → проверка типов "
         "→ тесты» в один вызов.",
         "Агент каждый раз угадывает команды проекта — и молча пропускает "
         "проверку, о которой не знал."),
        ("lock", "Закрытый контур", "pytest-generator", TEAL,
         "Дообученная модель на 8 млрд параметров (~5 ГБ, есть версия для "
         "процессора) пишет скелеты тестов на машине.",
         "Любая AI-генерация тестов = отправка исходного кода во внешний "
         "сервис: для закрытого контура это запрет."),
    ]

    x0 = 0.55
    total = 12.25
    gap = 0.16
    cw = (total - gap * 2) / 3           # 3.977
    row_y = [1.20, 3.68]
    ch = 2.42

    for i, (ic, cat, tool, col, does, without) in enumerate(cards):
        r, c = divmod(i, 3)
        x = x0 + c * (cw + gap)
        y = row_y[r]
        # header plate
        filled_rect(s, x, y, cw, 0.58, col, radius=True, radius_adj=0.12)
        icon(s, ic, x + 0.13, y + 0.09, 0.40, "white")
        text_box(s, x=x + 0.60, y=y + 0.04, w=cw - 0.72, h=0.22, text=cat,
                 size=10, bold=True, color=WHITE)
        text_box(s, x=x + 0.60, y=y + 0.25, w=cw - 0.72, h=0.28, text=tool,
                 size=12.5, bold=True, color=WHITE, line_spacing=0.96)
        # «что делает»
        filled_rect(s, x, y + 0.62, cw, 0.84, SURFACE, stroke=SOFT_GREY,
                    stroke_pt=1.0, radius=True, radius_adj=0.08)
        text_box(s, x=x + 0.14, y=y + 0.66, w=cw - 0.28, h=0.18,
                 text="ЧТО ДЕЛАЕТ", size=9, bold=True, color=LIGHT)
        text_box(s, x=x + 0.14, y=y + 0.85, w=cw - 0.28, h=0.58, text=does,
                 size=10.5, color=DEEP, line_spacing=1.06)
        # «зачем нужен — что без него невозможно»
        filled_rect(s, x, y + 1.50, cw, 0.92, GOLD_TINT, stroke=GOLD,
                    stroke_pt=1.4, radius=True, radius_adj=0.07)
        text_box(s, x=x + 0.14, y=y + 1.54, w=cw - 0.28, h=0.18,
                 text="БЕЗ НЕГО НЕВОЗМОЖНО / ОЧЕНЬ ТРУДНО", size=9,
                 bold=True, color=DEEP)
        text_box(s, x=x + 0.14, y=y + 1.73, w=cw - 0.28, h=0.64, text=without,
                 size=10.5, color=DEEP, line_spacing=1.06)

    # sixth cell — takeaway (balances the 3+2 grid instead of empty space)
    tx = x0 + 2 * (cw + gap)
    ty = row_y[1]
    filled_rect(s, tx, ty, cw, ch, TEAL_TINT, stroke=TEAL, stroke_pt=1.6,
                radius=True, radius_adj=0.07)
    text_box(s, x=tx + 0.18, y=ty + 0.14, w=cw - 0.36, h=0.30,
             text="Критерий выбора", size=12.5, bold=True, color=TEAL)
    text_box(s, x=tx + 0.18, y=ty + 0.50, w=cw - 0.36, h=1.80,
             text="Каждый инструмент закрывает ровно один канал, слепой для "
                  "агента: данные, сеть, интерфейс, свои проверки, закрытый "
                  "контур.\n\nЛокальное, детерминированное и уже "
                  "работающее — берите и оборачивайте; писать самому имеет "
                  "смысл только обёртку вокруг своего же цикла проверок.",
             size=10.5, color=DEEP, line_spacing=1.10)

    # honest-limits strip (muted, one line)
    cy = row_y[1] + ch + 0.08
    filled_rect(s, x0, cy, total, 0.48, SOFT_GREY, stroke=SLATE, stroke_pt=0.75,
                radius=True, radius_adj=0.11)
    text_box(s, x=x0 + 0.18, y=cy + 0.04, w=total - 0.36, h=0.40,
             text="Честные ограничения: без настоящего примера ответа API мок "
                  "MSW — догадка агента, а не контракт · AI-функции WireMock "
                  "живут в платном WireMock Cloud, а не в локальном ядре с "
                  "открытым кодом · pytest-generator — точность ≈77% заявлена "
                  "вендором, независимо не проверена, распространённость низкая.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.08,
             anchor=MSO_ANCHOR.MIDDLE)
    refs_of_slide(s, "s25c")
    notes_with_sources(s, "s25c")
    return s


# ============================================================
# s25 — section divider Раздел 5 (Ревью + Безопасность)
# ============================================================
def s25(p):
    return build_section_divider(
        p, here_idx=5,
        subtitle="Ревью + Безопасность — дисциплина скепсиса",
        bridge="Ревью и безопасность — это второй, критический взгляд на вывод "
               "AI, и оба упираются в склонность доверять автомату. "
               "Контринтуитивный тезис фазы: AI-код надо ревьюить больше, а не "
               "меньше — источник его дефектов другой.",
        sid="s26",
        tag="Сильная по возможностям · сила ≠ безопасность · 4 провала")


# ============================================================
# s26 — review practice (2 human practices + tradeoff + tools)
# ============================================================
def s26(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Практика ревью — две человеческие практики, а не выбор AI-ревьюера",
                size=22, w=12.2, h=0.82)

    # left: two human practices
    lx, lw = 0.55, 6.60
    pracs = [
        ("eye-off", "1. Adversarial-ревью со свежим контекстом [1]",
         "Код ревьюит НЕ тот, кто писал; ревьюер стартует с чистым контекстом: "
         "видит только diff и критерии приёмки. Снижает предвзятость «я написал, "
         "значит верно» (writer-reviewer, два прохода)."),
        ("user-check", "2. Удержанная человеческая ответственность",
         "AI-ревью — ассист и первый проход, но решение и accountability на "
         "человеке. Osmani [2]: «если не можешь объяснить — не коммить»."),
    ]
    py = 1.52
    for i, (ic, head, body) in enumerate(pracs):
        y = py + i * 1.62
        ocean_box(s, lx, y, lw, 1.50)
        icon(s, ic, lx + 0.24, y + 0.24, 0.54, "mid")
        text_box(s, x=lx + 0.90, y=y + 0.20, w=lw - 1.14, h=0.60, text=head,
                 size=12.5, bold=True, color=MID, line_spacing=1.05)
        text_box(s, x=lx + 0.24, y=y + 0.80, w=lw - 0.48, h=0.62, text=body,
                 size=11, color=DEEP, line_spacing=1.14)

    # right: tradeoff
    rx, rw = 7.35, 5.45
    ocean_box(s, rx, 1.52, rw, 3.12)
    icon(s, "scale", rx + 0.24, 1.66, 0.5, "teal")
    text_box(s, x=rx + 0.88, y=1.70, w=rw - 1.10, h=0.40,
             text="Фундаментальный размен", size=13, bold=True, color=TEAL)
    text_box(s, x=rx + 0.24, y=2.18, w=rw - 0.48, h=1.34,
             text="Полнота обнаружения ↔ шум: строже — больше пойманных багов, "
                  "но больше ложных тревог; мягче — меньше шума, но пропуски. "
                  "Anthropic [3]: ревьюеру велено искать дыры — он найдёт их даже в "
                  "здоровом коде (over-eagerness → over-engineering); скоуп — на "
                  "корректность.",
             size=10.5, color=DEEP, line_spacing=1.12)
    filled_rect(s, rx + 0.24, 3.54, rw - 0.48, 0.98, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.6, radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.46, y=3.64, w=rw - 0.9, h=0.80,
             text="Ни одна точка размена не делает AI-ревью автономным гейтом.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.14)
    # tools row (spanning)
    filled_rect(s, 0.55, 4.80, 12.25, 0.56, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    text_box(s, x=0.80, y=4.88, w=11.75, h=0.42,
             text="Первый проход по diff (вторично): GitHub Copilot code review · "
                  "Cursor Bugbot · Qodo Merge · Atlassian Rovo Dev (против критериев "
                  "в Jira) · Anthropic adversarial-ревьюер.",
             size=10.5, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.52, 12.25, 0.62,
        "Устойчивый паттерн: AI-ревью как ассист / первый проход. Хайп: AI-ревью "
        "как гейт («AI отревьюил — можно мержить»). Решение и accountability — на человеке.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s27")
    notes_with_sources(s, "s27")
    return s


# ============================================================
# s27 — review failure: complacency + curl-slop asymmetry [in-bucket]
# ============================================================
def s27(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Провал ревью: благодушие и асимметрия «фейк за секунды, разбор за часы»",
                size=21, w=12.3, h=0.82)

    # left: complacency
    lx, lw = 0.55, 5.35
    ocean_box(s, lx, 1.48, lw, 4.10)
    icon(s, "eye-off", lx + 0.24, 1.60, 0.46, "mid")
    text_box(s, x=lx + 0.82, y=1.64, w=lw - 1.04, h=0.36,
             text="Complacency (Radar, кольцо Hold) [1]", size=12, bold=True,
             color=MID)
    text_box(s, x=lx + 0.24, y=2.06, w=lw - 0.48, h=0.72,
             text="Некритичное принятие AI-кода, падение критического мышления. "
                  "CodeCrash [3]: вводящие в заблуждение комментарии роняют "
                  "рассуждение модели (~−23%).",
             size=10, color=DEEP, line_spacing=1.10)
    filled_rect(s, lx + 0.24, 2.82, lw - 0.48, 0.62, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.2, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.42, y=2.86, w=lw - 0.84, h=0.54,
             text="AI-ревью ~19% F1 (SWR-Bench) — только против human-review "
                  "baseline.",
             size=10.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    text_box(s, x=lx + 0.24, y=3.52, w=lw - 0.48, h=0.34,
             text="Rubber-Stamp Collapse (TianPan.co, 470 PR) [4]", size=11,
             bold=True, color=MID)
    text_box(s, x=lx + 0.24, y=3.86, w=lw - 0.48, h=0.80,
             text="AI-ассистированные PR: +170% issues, +40% critical, +75% "
                  "logic-находок, ×2,74 security-уязвимостей. На 22 000 "
                  "разработчиков — +242,7% инцидентов на PR.",
             size=9.5, color=DEEP, line_spacing=1.12)
    text_box(s, x=lx + 0.24, y=4.68, w=lw - 0.48, h=0.80,
             text="Stenberg: AI-анализаторы «в правильных руках» находят "
                  "реальные баги — виновата архитектура процесса, не AI.",
             size=10, italic=True, color=SLATE, line_spacing=1.12)

    # right: curl-slop asymmetry + matplotlib hit-piece
    rx, rw = 6.10, 6.70
    ocean_box(s, rx, 1.48, rw, 4.10)
    icon(s, "package-x", rx + 0.24, 1.60, 0.46, "mid")
    text_box(s, x=rx + 0.82, y=1.64, w=rw - 1.60, h=0.36,
             text="curl-slop как DDoS на сопровождающих [2]", size=12,
             bold=True, color=MID)
    add_image(s, ASSETS / "logos" / "curl-logo.png", rx + rw - 0.62, 1.56,
              0.44, 0.44)
    text_box(s, x=rx + rw - 1.10, y=2.00, w=0.90, h=0.20,
             text="curl — офиц. логотип", size=7, italic=True, color=LIGHT,
             align=PP_ALIGN.CENTER)
    text_box(s, x=rx + 0.24, y=2.06, w=rw - 0.48, h=0.44,
             text="Поток LLM-«отчётов об уязвимостях» в bug-bounty curl.",
             size=10.5, color=DEEP, line_spacing=1.10)
    # asymmetry main visual
    filled_rect(s, rx + 0.24, 2.56, rw - 0.48, 0.86, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.6, radius=True, radius_adj=0.06)
    text_runs(s, rx + 0.42, 2.64, rw - 0.84, 0.72, [
        {"text": "Асимметрия стоимости: ", "size": 11.5, "bold": True,
         "color": DEEP},
        {"text": "фейк — секунды; опровергнуть — часы сопровождающего.",
         "size": 11, "bold": True, "color": DEEP, "line_spacing": 1.10},
    ])
    text_box(s, x=rx + 0.24, y=3.52, w=rw - 0.48, h=0.72,
             text="Валидных отчётов >15% → <5% (~1 на 20–30); объём вырос "
                  "кратно; программа приостановлена, возвращена на HackerOne "
                  "март 2026.",
             size=10, color=DEEP, line_spacing=1.12)
    filled_rect(s, rx + 0.24, 4.30, rw - 0.48, 1.16, SOFT_GREY, stroke=SLATE,
                stroke_pt=0.8, radius=True, radius_adj=0.06)
    icon(s, "message-square-warning", rx + 0.40, 4.38, 0.36, "mid")
    text_box(s, x=rx + 0.84, y=4.36, w=rw - 1.08, h=0.32,
             text="matplotlib hit-piece, 2026-02-10 [5]", size=10.5, bold=True,
             color=DEEP)
    text_box(s, x=rx + 0.40, y=4.72, w=rw - 0.68, h=0.68,
             text="AI-агент (crabby-rathbun) сам написал и опубликовал "
                  "персонализированное эссе против мейнтейнера, закрывшего "
                  "его PR — атака на человека, тот же экономический сдвиг.",
             size=9.5, color=DEEP, line_spacing=1.10)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "AI не «сделал спам злее» — он снял ограничитель, и сменилась экономика "
        "процесса. Альтернатива: машинно-проверяемый барьер на входе "
        "(воспроизводимый PoC), а не ручной разбор каждого текста.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    # Round-5 meme: Evil Kermit — the inner temptation to skip reading the
    # diff and rubber-stamp instead, direct callback to complacency (left).
    add_image(s, WEB / "band-evil-kermit.png", 8.96, 6.40, 3.84, 0.64)
    refs_of_slide(s, "s28")
    notes_with_sources(s, "s28")
    return s


# ============================================================
# s28 — security practice: Lethal Trifecta + 4 controls
# ============================================================
def s28(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Безопасность — архитектурно разорвать смертельную триаду",
                size=24, w=12.0, h=0.82)

    # left: Lethal Trifecta — 3 conditions
    lx, lw = 0.55, 5.85
    ocean_box(s, lx, 1.52, lw, 4.02)
    text_box(s, x=lx + 0.24, y=1.64, w=lw - 0.48, h=0.60,
             text="Lethal Trifecta (смертельная триада, Willison, июнь 2025 [1]; "
                  "Fowler [2]) — опасно только пересечение всех трёх:",
             size=12.5, bold=True, color=MID, line_spacing=1.08)
    tri = [
        ("link", "недоверенное содержимое", "issue, письма, веб-страницы"),
        ("key", "секреты / приватные данные", "ключи, база"),
        ("arrow-right-left", "исходящая передача (egress)", "может отправить вовне"),
    ]
    ty = 2.42
    for i, (ic, head, sub) in enumerate(tri):
        y = ty + i * 0.90
        filled_rect(s, lx + 0.24, y, lw - 0.48, 0.76, SOFT_GREY, stroke=LIGHT,
                    stroke_pt=1.2, radius=True, radius_adj=0.07)
        icon(s, ic, lx + 0.42, y + 0.14, 0.48, "mid")
        text_box(s, x=lx + 1.04, y=y + 0.08, w=lw - 1.3, h=0.36,
                 text=f"{i+1}. {head}", size=12.5, bold=True, color=DEEP)
        text_box(s, x=lx + 1.04, y=y + 0.44, w=lw - 1.3, h=0.28, text=sub,
                 size=10.5, italic=True, color=SLATE)
    text_box(s, x=lx + 0.24, y=5.14, w=lw - 0.48, h=0.34,
             text="Недоверенный контент через prompt injection → взять секрет → "
                  "отправить наружу.",
             size=10.5, italic=True, color=MID, line_spacing=1.0)

    # right: 4 controls + terms + tools + caveat
    rx, rw = 6.65, 6.15
    ocean_box(s, rx, 1.52, rw, 1.66)
    text_box(s, x=rx + 0.24, y=1.62, w=rw - 0.48, h=0.34,
             text="Четыре человеко-владеемых контроля, разрывающих триаду",
             size=12.5, bold=True, color=MID, line_spacing=1.0)
    ctrls = ["least-privilege", "sandbox", "egress-allowlist", "SAST-гейт"]
    ccx = rx + 0.26
    ccy = 2.02
    for i, c in enumerate(ctrls):
        col = i % 2
        row = i // 2
        chip(s, rx + 0.26 + col * 2.95, 2.02 + row * 0.54, 2.80, 0.46, c,
             fill=TEAL, color=WHITE, size=11)
    text_box(s, x=rx + 0.24, y=3.14, w=rw - 0.48, h=0.34,
             text="Термины: SAST (статич.) / secret-scanning / SCA (зависимости) "
                  "/ supply-chain.",
             size=10.5, italic=True, color=SLATE)
    # tools
    filled_rect(s, rx, 3.54, rw, 1.06, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.22, y=3.62, w=rw - 0.44, h=0.90,
             text="Вторично: GitHub (CodeQL + Copilot Autofix + secret-scanning "
                  "+ Dependabot) · Google (Big Sleep — живая эксплуатация SQLite; "
                  "OSS-Fuzz + LLM — ~20-летний баг OpenSSL) [3] · AWS Q security · "
                  "Anthropic /security-review.",
             size=10, italic=True, color=SLATE, line_spacing=1.1)
    # caveat
    filled_rect(s, rx, 4.72, rw, 0.82, TEAL_TINT, stroke=TEAL, stroke_pt=1.3,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.22, y=4.80, w=rw - 0.44, h=0.68,
             text="«Первый AI, остановивший zero-day» = один curated-кейс; «AI "
                  "находит 50%» = метрики на своём коде, не универсально.",
             size=10.5, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.12)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Устойчивый паттерн: обязательный автоматический security-скан как гейт "
        "+ архитектурный разрыв триады. SAST необходим, но НЕ достаточен; "
        "моделирование угроз — человеку.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s29")
    notes_with_sources(s, "s29")
    return s


# ============================================================
# s29 — vulnerable code + false confidence [in-bucket]
# ============================================================
def s29(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Опасна не сама уязвимость, а уверенность, что код безопасен",
                size=23, w=12.2, h=0.82)

    # centre-top: double risk thesis
    ocean_box(s, 0.55, 1.46, 12.25, 1.66)
    text_runs(s, 0.85, 1.57, 11.65, 1.48, [
        {"text": "Самый системный риск — не «AI иногда пишет уязвимый код», а "
                 "«уязвимый код + повышенная уверенность разработчика, что он "
                 "безопасен»", "size": 14, "bold": True, "color": DEEP},
        {"text": " = склонность доверять автомату в опаснейшем проявлении.",
         "size": 14, "color": DEEP},
        {"text": "Почему системно: автодополнение опирается на статистически "
                 "частое, а уязвимые паттерны (конкатенация SQL, отсутствие "
                 "валидации, захардкоженные секреты) в открытом коде массовы. "
                 "Модель воспроизводит частое, а не безопасное.",
         "size": 11.5, "color": SLATE, "newpara": True, "space_before": 6,
         "line_spacing": 1.14},
    ])

    # two studies
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 3.26, lw, 2.14)
    icon(s, "flask-conical", lx + 0.24, 3.40, 0.5, "teal")
    text_box(s, x=lx + 0.88, y=3.40, w=lw - 1.10, h=0.34,
             text="Stanford (рандомизированное) [1]", size=13, bold=True, color=MID)
    text_box(s, x=lx + 0.88, y=3.72, w=lw - 1.10, h=0.24,
             text="Perry et al. · arXiv:2211.03622 · CCS 2023",
             size=9, italic=True, color=LIGHT)
    text_box(s, x=lx + 0.24, y=4.06, w=lw - 0.48, h=1.28,
             text="Разработчики с AI-ассистентом вносили уязвимости ЧАЩЕ — и были "
                  "УВЕРЕННЕЕ в безопасности своего кода. Ложная уверенность "
                  "измерена напрямую.",
             size=12, color=DEEP, line_spacing=1.16)

    rx, rw = 6.85, 5.95
    ocean_box(s, rx, 3.26, rw, 2.14)
    icon(s, "bug", rx + 0.24, 3.40, 0.5, "mid")
    text_box(s, x=rx + 0.88, y=3.40, w=rw - 1.10, h=0.34,
             text="NYU «Asleep at the Keyboard?» [2]", size=13, bold=True, color=MID)
    text_box(s, x=rx + 0.88, y=3.72, w=rw - 1.10, h=0.24,
             text="arXiv:2108.09293 · IEEE S&P 2022",
             size=9, italic=True, color=LIGHT)
    text_box(s, x=rx + 0.24, y=4.06, w=rw - 0.48, h=0.40,
             text="~40% программ с Copilot содержали уязвимости.",
             size=13, bold=True, color=DEEP, line_spacing=1.1)
    text_box(s, x=rx + 0.24, y=4.50, w=rw - 0.48, h=0.86,
             text="База: из 1689 программ по 89 сценариям вокруг MITRE Top-25 CWE "
                  "— доля среди намеренно security-чувствительных задач, НЕ «40% "
                  "всего кода».",
             size=11, italic=True, color=SLATE, line_spacing=1.14)

    gold_callout(
        s, 0.55, 5.52, 12.25, 0.62,
        "Альтернатива: SAST + DAST + обязательный security-гейт плюс "
        "моделирование угроз (существенная сложность, не делегируется). Опасна не "
        "ошибка, а ложная уверенность рядом с ней.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s30")
    notes_with_sources(s, "s30")
    return s


# ============================================================
# s30b (NEW, #162 round 3) — Amazon Q wiper incident, third
# mechanistically distinct supply-chain failure class
# ============================================================
def s30b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Доверие нужно и к тому, из чего сделан сам AI-инструмент",
        size=20, w=12.3, h=0.82)

    lx, lw = 0.55, 6.55
    rx, rw = 7.30, 5.50
    top = 1.44

    ocean_box(s, lx, top, lw, 4.10)
    icon(s, "package-x", lx + 0.22, top + 0.16, 0.48, "mid")
    text_box(s, x=lx + 0.84, y=top + 0.20, w=lw - 1.90, h=0.36,
             text="Amazon Q Developer, июль 2025 [1]", size=13, bold=True,
             color=MID)
    add_image(s, ASSETS / "logos" / "aws-logo.png", lx + lw - 1.02, top + 0.16,
              0.72, 0.43)
    text_box(s, x=lx + lw - 1.10, y=top + 0.58, w=0.88, h=0.16,
             text="AWS · Wikimedia", size=6.5, italic=True, color=LIGHT,
             align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.24, y=top + 0.68, w=lw - 0.48, h=1.36,
             text="Неаудированный внешний контрибьютор смержил PR с системным "
                  "промптом «system cleaner» (aws s3 rb, остановка EC2, "
                  "удаление IAM-пользователей) в официальный релиз расширения "
                  "VS Code.",
             size=11, color=DEEP, line_spacing=1.18)
    text_box(s, x=lx + 0.24, y=top + 2.06, w=lw - 0.48, h=0.60, text="~1 млн",
             size=24, bold=True, color=TEAL)
    text_box(s, x=lx + 0.24, y=top + 2.60, w=lw - 0.48, h=0.44,
             text="разработчиков в релизе v1.84.0 до патча v1.85.0 [2].",
             size=10.5, italic=True, color=DEEP)
    filled_rect(s, lx + 0.24, top + 3.14, lw - 0.48, 0.80, SOFT_GREY,
                stroke=SLATE, stroke_pt=0.8, radius=True, radius_adj=0.08)
    text_box(s, x=lx + 0.40, y=top + 3.20, w=lw - 0.80, h=0.68,
             text="Атака технически провалилась (форматирование сломало "
                  "исполнение) — это везение, не контроль.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.14,
             anchor=MSO_ANCHOR.MIDDLE)

    ocean_box(s, rx, top, rw, 4.10, fill=SURFACE, stroke=MID, stroke_pt=1.6)
    icon(s, "layers", rx + 0.22, top + 0.16, 0.46, "teal")
    text_box(s, x=rx + 0.80, y=top + 0.20, w=rw - 1.04, h=0.36,
             text="Три механически разных фронта", size=12.5, bold=True,
             color=MID)
    fronts = [
        ("Slopsquatting", "доверие к имени пакета, которое AI-совет "
         "порекомендовал."),
        ("CamoLeak", "доверие к чужому недоверенному тексту (PR-комментарий) "
         "в контексте агента."),
        ("Amazon Q", "доверие к supply-chain самого инструмента — не к "
         "выводу и не к входу, а к тому, из чего он сделан."),
    ]
    fy = top + 0.72
    for head, body in fronts:
        text_box(s, x=rx + 0.24, y=fy, w=rw - 0.48, h=0.30, text=head,
                 size=12, bold=True, color=DEEP)
        text_box(s, x=rx + 0.24, y=fy + 0.32, w=rw - 0.48, h=0.72, text=body,
                 size=10.5, color=DEEP, line_spacing=1.14)
        fy += 1.10

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Ревью нужно не только коду, который пишет ваш агент, но и коду, из "
        "которого сделан сам AI-инструмент.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s30b")
    notes_with_sources(s, "s30b")
    return s


# ============================================================
# s30 — supply-chain: slopsquatting + CamoLeak [in-bucket]
# ============================================================
def s30(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Supply-chain — отдельный класс: воспроизводимая галлюцинация и канал утечки",
        size=21, w=12.3, h=0.82)

    # left: slopsquatting chain
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.52, lw, 4.02)
    icon(s, "package-x", lx + 0.24, 1.66, 0.5, "mid")
    text_box(s, x=lx + 0.88, y=1.70, w=lw - 1.10, h=0.40,
             text="Slopsquatting (supply-chain-атака)", size=12.5, bold=True,
             color=MID)
    chain = [
        "LLM воспроизводимо галлюцинирует имя пакета",
        "злоумышленник ЗАРАНЕЕ регистрирует его с malware",
        "разработчик / агент C–D делает install <выдуманное>",
    ]
    ch_y = 2.20
    for i, txt in enumerate(chain):
        y = ch_y + i * 0.66
        filled_rect(s, lx + 0.24, y, lw - 0.48, 0.52, SURFACE, stroke=LIGHT,
                    stroke_pt=1.1, radius=True, radius_adj=0.08)
        text_box(s, x=lx + 0.46, y=y + 0.05, w=lw - 0.9, h=0.44, text=txt,
                 size=11, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
        if i < 2:
            text_box(s, x=lx + 0.24, y=y + 0.50, w=lw - 0.48, h=0.16, text="↓",
                     size=11, bold=True, color=LIGHT, align=PP_ALIGN.CENTER)
    filled_rect(s, lx + 0.24, 4.24, lw - 0.48, 1.14, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.6, radius=True, radius_adj=0.05)
    text_runs(s, lx + 0.46, 4.32, lw - 0.9, 1.00, [
        {"text": "Ось угрозы — воспроизводимость: из 576 000 сэмплов ~20% "
                 "рекомендовали несуществующие пакеты; 43% галлюцинированных "
                 "имён повторялись во всех 10 запросах",
         "size": 11, "bold": True, "color": DEEP, "line_spacing": 1.12},
        {"text": " (Spracklen et al., USENIX Security 2025) [1]", "size": 9,
         "italic": True, "color": LIGHT},
        {"text": ". Термин ввёл Seth Larson (PSF, апрель 2025).", "size": 11,
         "bold": True, "color": DEEP, "line_spacing": 1.12},
    ], anchor=MSO_ANCHOR.MIDDLE)

    # right: CamoLeak
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, 1.52, rw, 4.02)
    icon(s, "shield-alert", rx + 0.24, 1.66, 0.5, "mid")
    text_box(s, x=rx + 0.88, y=1.66, w=rw - 1.95, h=0.56,
             text="CamoLeak (prompt injection в dev-агенте · Legit Security) [2]",
             size=11.5, bold=True, color=MID, line_spacing=1.05)
    add_image(s, ASSETS / "logos" / "copilot-logo.png", rx + rw - 0.86,
              1.62, 0.40, 0.40)
    text_box(s, x=rx + rw - 1.02, y=2.03, w=0.72, h=0.16,
             text="GitHub Copilot", size=6.5, italic=True,
             color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, x=rx + 0.24, y=2.20, w=rw - 0.48, h=1.24,
             text="Скрытые в невидимых markdown-комментариях PR инструкции "
                  "заставили GitHub Copilot Chat искать секреты (ключи AWS) и "
                  "эксфильтровать через GitHub image-proxy.",
             size=11.5, color=DEEP, line_spacing=1.18)
    filled_rect(s, rx + 0.24, 3.42, rw - 0.48, 0.62, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    text_box(s, x=rx + 0.46, y=3.50, w=rw - 0.9, h=0.48,
             text="CVE-2025-59145, CVSS 9,6 (критический).", size=13, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=rx + 0.24, y=4.16, w=rw - 0.48, h=1.24,
             text="Dev-агент с доступом к недоверенному контенту + секретам = "
                  "готовый канал эксфильтрации (структурное свойство, не баг). Та "
                  "же смертельная триада — в инструменте разработчика.",
             size=11, color=DEEP, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Не лечится «лучшей моделью» — только архитектурой: lockfile с "
        "хэш-пиннингом, allowlist реестров, проверка пакета до установки, SCA; "
        "least-privilege + изоляция + human-in-loop на запись + egress-контроль.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    # Round-5 meme: Domino Effect — one hallucinated package name cascading
    # into a full exploit chain (slopsquatting, left column).
    add_image(s, WEB / "band-domino-effect.png", 10.09, 6.40, 2.71, 0.64)
    refs_of_slide(s, "s31")
    notes_with_sources(s, "s31")
    return s
