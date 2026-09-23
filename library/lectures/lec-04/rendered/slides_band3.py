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
# s21 — anti-hype benchmarks (SWE-bench gap chart + 3 overclaims) [in-bucket]
# ============================================================
def s21(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Бренд и бенчмарк-число ≠ инженерная дисциплина",
                size=25, w=12.0, h=0.82)

    # left: SWE-bench gap chart
    lx, lw = 0.55, 5.25
    ocean_box(s, lx, 1.52, lw, 4.02)
    add_image(s, CHARTS / "c21-swe-bench.png", lx + 0.12, 1.66, lw - 0.24, 2.30)
    text_box(s, x=lx + 0.24, y=4.02, w=lw - 0.48, h=1.44,
             text="SWE-bench (эталонный бенчмарк на реальных GitHub issues): "
                  "Verified (~500 задач, публичный код) — топ ~88–89%. Pro "
                  "(приватные, контаминация-устойчивые) — лидер ~64%. Разрыв "
                  "~24 п.п.: доверие числу обратно пропорционально незнакомости и "
                  "критичности вашей задачи.",
             size=11, color=DEEP, line_spacing=1.16)

    # right: 3 overclaims + 5 questions
    rx, rw = 6.05, 6.75
    over = [
        ("Devin (Cognition): 13,86% [1]",
         "vs база 1,96% — но только на 25% бенча (79 из 570 задач), признанная "
         "контаминация, лимит 45 мин; независимо ~15% (3 из 20)."),
        ("OpenAI: «~80% Verified» / «70% больше PR»",
         "сам OpenAI: ~59% «провалов» — дефекты дизайна тестов, не модели; "
         "«70% больше PR» — без знаменателя."),
        ("Cursor: Composer «frontier, 4× быстрее»",
         "собственный блог признаёт: GPT-5 и Sonnet 4.5 «оба превосходят» → "
         "frontier-быстрый, не frontier-лучший."),
    ]
    oy = 1.52
    for i, (head, body) in enumerate(over):
        y = oy + i * 1.02
        ocean_box(s, rx, y, rw, 0.90)
        text_box(s, x=rx + 0.22, y=y + 0.08, w=rw - 0.44, h=0.32, text=head,
                 size=12, bold=True, color=MID)
        text_box(s, x=rx + 0.22, y=y + 0.40, w=rw - 0.44, h=0.48, text=body,
                 size=10.5, color=DEEP, line_spacing=1.08)
    # 5 questions strip
    filled_rect(s, rx, 4.60, rw, 0.94, TEAL_TINT, stroke=TEAL, stroke_pt=1.4,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.22, y=4.68, w=rw - 0.44, h=0.34,
             text="Пять вопросов к любому вендорскому числу:", size=11.5,
             bold=True, color=TEAL)
    text_box(s, x=rx + 0.22, y=5.02, w=rw - 0.44, h=0.48,
             text="1. Какой срез? 2. Контаминация? 3. База сравнения? "
                  "4. Факт или маркетинг? 5. Что мелким шрифтом? [2]",
             size=11, color=DEEP, line_spacing=1.1)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Devin 13,86% — технически истинно ровно на четверти задач. Число может "
        "быть правдой и вводить в заблуждение; высокая цифра не отвечает на "
        "вопрос merge-гейта. Бренд/бенчмарк не заменяет дисциплину.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    # Round-5 meme: Mocking Spongebob — mocking-case echo of the vendor's own
    # overclaim quoted above right ("frontier, 4х быстрее"). Bottom band.
    add_image(s, WEB / "band-mocking-spongebob.png", 9.86, 6.40, 2.94, 0.64)
    refs_of_slide(s, "s22")
    notes_with_sources(s, "s22")
    return s


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
        s, "TDD-как-подход: человек решает, что проверять; прогон — детерминированный",
        size=22, w=12.2, h=0.82)

    # left: red-green-refactor cycle
    lx, lw = 0.55, 5.35
    ocean_box(s, lx, 1.52, lw, 4.02)
    text_box(s, x=lx + 0.24, y=1.64, w=lw - 0.48, h=0.34,
             text="Цикл red-green-refactor (Kent Beck, TDD) [1] — человек владеет "
                  "спекой теста", size=12.5, bold=True, color=MID,
             line_spacing=1.0)
    cyc = [
        ("red", "падающий тест выражает требование", GOLD, True),
        ("green", "код, который его проходит", MID, False),
        ("refactor", "улучшить, сохранив зелёный", TEAL, False),
    ]
    cy0 = 2.06
    for i, (name, desc, col, start) in enumerate(cyc):
        y = cy0 + i * 0.66
        filled_rect(s, lx + 0.30, y, lw - 0.60, 0.54,
                    (GOLD_TINT if start else SURFACE),
                    stroke=col, stroke_pt=(1.8 if start else 1.2),
                    radius=True, radius_adj=0.10)
        if start:
            circle(s, lx + 0.42, y + 0.15, 0.24, GOLD)
        text_box(s, x=lx + (0.78 if start else 0.50), y=y + 0.04, w=1.6, h=0.46,
                 text=name, size=12.5, bold=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, font="DejaVu Sans Mono")
        text_box(s, x=lx + 2.15, y=y + 0.04, w=lw - 2.5, h=0.46, text=desc,
                 size=10.5, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 0.30, y=4.04, w=lw - 0.60, h=0.16, text="↑ повторяется",
             size=10.5, italic=True, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    # role split
    filled_rect(s, lx + 0.30, 4.30, lw - 0.60, 1.06, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.4, radius=True, radius_adj=0.06)
    text_runs(s, lx + 0.50, 4.40, lw - 1.0, 0.9, [
        {"text": "AI пишет тесты быстро", "size": 11.5, "bold": True,
         "color": TEAL},
        {"text": " — объём (привнесённое). ", "size": 11.5, "color": DEEP},
        {"text": "Человек решает, ЧТО тест должен утверждать", "size": 11.5,
         "bold": True, "color": DEEP},
        {"text": " — существенное.", "size": 11.5, "color": DEEP},
    ])

    # right: no-outsource + nuance + tools
    rx, rw = 6.10, 6.70
    ocean_box(s, rx, 1.52, rw, 1.28)
    text_box(s, x=rx + 0.24, y=1.62, w=rw - 0.48, h=0.34,
             text="Проверка не аутсорсится модели", size=12.5, bold=True,
             color=MID)
    text_box(s, x=rx + 0.24, y=1.96, w=rw - 0.48, h=0.80,
             text="Willison / Fowler: «не видел, как работает — не работающая "
                  "система». Тесты гоняет детерминированный исполнитель (скрипт / "
                  "CI), не модель на словах. Инцидент → постоянный регресс-тест.",
             size=11, color=DEEP, line_spacing=1.14)
    # nuance (honest)
    filled_rect(s, rx, 2.92, rw, 1.28, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.05)
    text_box(s, x=rx + 0.24, y=3.02, w=rw - 0.48, h=0.34,
             text="Важный нюанс — структура ≠ ритуал", size=12.5, bold=True,
             color=DEEP)
    text_box(s, x=rx + 0.24, y=3.36, w=rw - 0.48, h=0.80,
             text="Ценность TDD (test-driven development, разработка через "
                  "тестирование) — структура (спека-тест + гейт), а не ритуал "
                  "форсить порядок агенту. Böckeler [2]: TDD-first в agent-loop — "
                  "отсутствие выигрыша + ~3× токенов («я перестала велеть "
                  "агентам писать тесты первыми»).",
             size=10.5, color=DEEP, line_spacing=1.10)
    # Fowler tests-as-guardrails caption
    filled_rect(s, rx, 4.32, rw, 0.52, TEAL_TINT, stroke=TEAL, stroke_pt=1.2,
                radius=True, radius_adj=0.07)
    text_runs(s, rx + 0.22, 4.39, rw - 0.44, 0.40, [
        {"text": "Тесты-как-ограждения (Fowler) [3]: ", "size": 10.5, "bold": True,
         "color": TEAL},
        {"text": "тест форсит интерфейс, не связывая с реализацией — потому "
                 "структура TDD ценна.", "size": 10.5, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE)
    # tools row
    filled_rect(s, rx, 4.96, rw, 0.52, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=5.03, w=rw - 0.48, h=0.40,
             text="Исполняют (вторично): AWS Q /test · Qodo · JetBrains Junie · "
                  "Anthropic (падающий тест → починка + Stop-hook как гейт).",
             size=10, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Устойчивый паттерн: тест-как-исполняемая-спецификация + детерминированный "
        "гейт прогона. Хайп: «AI сам покрыл код тестами».",
        size=13, bold=True, align=PP_ALIGN.CENTER)
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
        s, "Ещё две методики, ложащиеся на AI: BDD (язык бизнеса) и "
           "trunk-based (высокий темп коммитов)",
        size=19, w=12.3, h=0.82)

    colw = 6.05
    gap = 0.15
    lx = 0.55
    rx = lx + colw + gap
    top = 1.46
    boxh = 3.98

    # --- LEFT: BDD ---
    ocean_box(s, lx, top, colw, boxh, fill=SURFACE, stroke=MID, stroke_pt=1.6)
    icon(s, "check-check", lx + 0.22, top + 0.16, 0.44, "mid")
    text_box(s, x=lx + 0.80, y=top + 0.18, w=colw - 1.0, h=0.36,
             text="BDD — тест до кода на языке бизнеса", size=13, bold=True,
             color=MID)
    text_box(s, x=lx + 0.24, y=top + 0.64, w=colw - 0.48, h=1.20,
             text="BDD (Behavior-Driven Development) — тот же принцип «тест "
                  "до кода», что TDD, но читаем нетехническим стейкхолдером. "
                  "Три практики: Discovery (разговоры вокруг примеров) → "
                  "Formulation (примеры → сценарии) → Automation (сценарии "
                  "как тесты). Формат — Given-When-Then (Gherkin) — та же "
                  "структура, что в примере с переговоркой из визуализации "
                  "требований.",
             size=10, color=DEEP, line_spacing=1.10)
    text_box(s, x=lx + 0.24, y=top + 1.92, w=colw - 0.48, h=1.10,
             text="Кто пишет в 2026: агент генерирует Gherkin-сценарии из "
                  "критериев приёмки (включая краевые и security-случаи), "
                  "человек ревьюит. Риск без правил: расплывчатые Then-шаги, "
                  "сценарии, завязанные на UI. Контроль — явный гайдлайн как "
                  "контекст агенту.",
             size=10.5, color=DEEP, line_spacing=1.15)
    filled_rect(s, lx + 0.24, top + 3.08, colw - 0.48, 0.72, SOFT_GREY,
                stroke=SLATE, stroke_pt=0.75, radius=True, radius_adj=0.08)
    text_box(s, x=lx + 0.40, y=top + 3.14, w=colw - 0.80, h=0.60,
             text="Честно: BDD-фреймворки — ~27% OSS-выборки (68% в Ruby), не "
                  "мейнстрим большинства экосистем. Уместен рядом с "
                  "нетехническим стейкхолдером, иначе часто избыточен.",
             size=10, italic=True, color=SLATE, line_spacing=1.12,
             anchor=MSO_ANCHOR.MIDDLE)

    # --- RIGHT: trunk-based ---
    ocean_box(s, rx, top, colw, boxh, fill=SURFACE, stroke=LIGHT, stroke_pt=1.6)
    icon(s, "git-merge", rx + 0.22, top + 0.16, 0.44, "teal")
    text_box(s, x=rx + 0.80, y=top + 0.18, w=colw - 1.0, h=0.36,
             text="Trunk-based — короткоживущая ветка", size=13, bold=True,
             color=TEAL)
    text_box(s, x=rx + 0.24, y=top + 0.64, w=colw - 0.48, h=1.20,
             text="Короткоживущая ветка (<24 часа, DORA), не long-lived. "
                  "Причина: git автоматически разрешает текстовые конфликты, "
                  "но не семантические — ветка агента компилируется против "
                  "допущения, которое основная ветка уже перестала "
                  "поддерживать.",
             size=10.5, color=DEEP, line_spacing=1.15)
    text_box(s, x=rx + 0.24, y=top + 1.92, w=colw - 0.48, h=1.10,
             text="Feature-флаги разрывают связь «когда смержено» и «когда "
                  "пользователь видит фичу» — раскатка отдельно от "
                  "интеграции. Связь с уже введёнными git-конвенциями: те "
                  "отвечают «как называется ветка», trunk-based — «сколько "
                  "она живёт».",
             size=10.5, color=DEEP, line_spacing=1.15)
    filled_rect(s, rx + 0.24, top + 3.08, colw - 0.48, 0.72, SOFT_GREY,
                stroke=SLATE, stroke_pt=0.75, radius=True, radius_adj=0.08)
    text_box(s, x=rx + 0.40, y=top + 3.14, w=colw - 0.80, h=0.60,
             text="AI Agent Source Prefix обретает смысл именно здесь: "
                  "ветка живёт часами — префикс сигналит ревьюеру частое "
                  "ревью маленьких diff.",
             size=10, italic=True, color=SLATE, line_spacing=1.12,
             anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, top + boxh + 0.14, 12.25, 0.58,
        "Обе методики вторичны к уже названным практикам (TDD, "
        "git-конвенции) — не новая ось дисциплины, а расширение той же: "
        "спецификация до кода + короткий цикл интеграции.",
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
        s, "Локальный тестовый инструментарий кодинг-агента: БД, сеть, CI-цикл",
        size=19, w=12.3, h=0.78)

    cols = [
        ("database", "(а) БД — Testcontainers", MID),
        ("route", "(б) Сеть — MSW", MID),
        ("terminal", "(в) CI-цикл — skill-обёртка", MID),
    ]
    rows = [
        ("Что делает",
         ["Реальный Postgres/Kafka/Redis в Docker, эфемерный порт, на машине "
          "агента",
          "Перехват HTTP на уровне процесса — 1 handler для unit/e2e",
          "lint → type-check → test вызывается одной командой"]),
        ("Честная оговорка",
         ["Skill даёт процедуру Docker Compose, не «анализ» БД",
          "Без реального JSON-примера агент «придумывает» форму ответа",
          "Не новый инструмент — упаковка уже работающей инфраструктуры"]),
        ("Готовым / самим",
         ["ГОТОВЫМ — зрелая библиотека",
          "ГОТОВЫМ — зрелая библиотека, с оговоркой",
          "САМИМ — дешевле, чем искать AI-native замену"]),
    ]
    examples = ["testcontainers-docker skill", "mswjs.io handlers",
                "lint+type-check+test skill"]
    x0 = 0.55
    total = 12.25
    gap = 0.16
    cw = (total - gap * 2) / 3
    top = 1.32
    hh = 0.58
    for i, (ic, name, col) in enumerate(cols):
        x = x0 + i * (cw + gap)
        filled_rect(s, x, top, cw, hh, col, radius=True, radius_adj=0.12)
        icon(s, ic, x + 0.14, top + 0.08, 0.40, "white")
        text_box(s, x=x + 0.62, y=top + 0.05, w=cw - 0.72, h=hh - 0.10,
                 text=name, size=10.5, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.96)
    row_h = [1.10, 1.00, 0.66]
    ry = top + hh + 0.08
    for r, (label, cells) in enumerate(rows):
        rh = row_h[r]
        for i in range(3):
            x = x0 + i * (cw + gap)
            fill = SURFACE if r % 2 == 0 else WHITE
            filled_rect(s, x, ry, cw, rh, fill, stroke=SOFT_GREY, stroke_pt=1.0,
                        radius=True, radius_adj=0.06)
            if i == 0:
                text_box(s, x=x + 0.14, y=ry + 0.05, w=cw - 0.28, h=0.24,
                         text=label.upper(), size=12, bold=True, color=LIGHT)
                tb_y = ry + 0.30
                tb_h = rh - 0.36
            else:
                tb_y = ry + 0.06
                tb_h = rh - 0.12
            text_box(s, x=x + 0.14, y=tb_y, w=cw - 0.28, h=tb_h,
                     text=cells[i], size=14 if r < 2 else 12.5, color=DEEP,
                     line_spacing=1.04)
        ry += rh + 0.06

    ey = ry + 0.02
    text_runs(s, x0, ey, total, 0.30, [
        {"text": "Пример:  ", "size": 11, "bold": True, "color": SLATE},
        {"text": examples[0], "size": 10.5, "italic": True, "color": MID,
         "font": "DejaVu Sans Mono"},
        {"text": "   ·   ", "size": 10.5, "color": SLATE},
        {"text": examples[1], "size": 10.5, "italic": True, "color": TEAL,
         "font": "DejaVu Sans Mono"},
        {"text": "   ·   ", "size": 10.5, "color": SLATE},
        {"text": examples[2], "size": 10.5, "italic": True, "color": MID,
         "font": "DejaVu Sans Mono"},
    ])
    ry = ey + 0.30

    # cloud AI-layer contrast strip (muted)
    cy = ry + 0.06
    filled_rect(s, x0, cy, total, 0.56, SOFT_GREY, stroke=SLATE, stroke_pt=0.75,
                radius=True, radius_adj=0.10)
    text_box(s, x=x0 + 0.18, y=cy + 0.05, w=total - 0.36, h=0.46,
             text="Облачный AI-слой (не мейнстрим): WireMock Cloud — AI Skills/"
                  "MCP преимущественно здесь, не в локальном OSS-ядре · "
                  "pytest-generator (Distil Labs) — CPU-only, ≈77% точность "
                  "self-reported.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.08,
             anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, cy + 0.66, 12.25, 0.56,
        "Локальный, детерминированный, уже существующий инструмент — берите и "
        "оборачивайте; облачный AI-слой — с честной оговоркой о разрыве.",
        size=11.5, bold=True, align=PP_ALIGN.CENTER)
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
    """Round-6 block-4: 2 cases → 3. Owner ask — add a third case showing that
    the aggregate «productivity went up» hides a REDISTRIBUTION: juniors gain,
    seniors absorb the new review load. Layout rebuilt 2-col → 3-col so all
    three cases read as parallel instances of one mechanism (AI removed the
    volume limiter; the cost of checking did not fall with it)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Провал ревью: благодушие, асимметрия «фейк — секунды, разбор — часы» "
                   "и сдвиг нагрузки на сеньоров",
                size=20, w=12.3, h=0.86)

    cw = 3.93
    c1, c2, c3 = 0.55, 4.70, 8.85
    top, bh = 1.44, 4.16
    pad = 0.24

    # ---------- column 1: complacency ----------
    ocean_box(s, c1, top, cw, bh)
    icon(s, "eye-off", c1 + pad, top + 0.12, 0.42, "mid")
    text_box(s, x=c1 + 0.74, y=top + 0.12, w=cw - 0.98, h=0.34,
             text="1. Благодушие к AI-коду [1]", size=12, bold=True, color=MID)
    text_box(s, x=c1 + 0.74, y=top + 0.46, w=cw - 0.98, h=0.28,
             text="Thoughtworks Radar — кольцо Hold", size=9, italic=True,
             color=SLATE)
    text_box(s, x=c1 + pad, y=top + 0.88, w=cw - 2 * pad, h=0.70,
             text="Некритичное принятие AI-кода, падение критического "
                  "мышления. CodeCrash [3]: вводящие в заблуждение "
                  "комментарии роняют рассуждение модели (~−23%).",
             size=9.5, color=DEEP, line_spacing=1.12)
    filled_rect(s, c1 + pad, top + 1.62, cw - 2 * pad, 0.66, TEAL_TINT,
                stroke=TEAL, stroke_pt=1.3, radius=True, radius_adj=0.07)
    text_box(s, x=c1 + 0.38, y=top + 1.66, w=cw - 0.76, h=0.58,
             text="AI-ревью ~19% F1 (SWR-Bench) — против человеческого "
                  "ревью как базы.",
             size=9.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    text_box(s, x=c1 + pad, y=top + 2.40, w=cw - 2 * pad, h=0.30,
             text="Rubber-Stamp Collapse, 470 PR [4]", size=10.5, bold=True,
             color=MID)
    text_box(s, x=c1 + pad, y=top + 2.72, w=cw - 2 * pad, h=0.72,
             text="+170% замечаний, +40% критических, ×2,74 уязвимостей; "
                  "на 22 000 разработчиков — +242,7% инцидентов на PR.",
             size=9.5, color=DEEP, line_spacing=1.12)
    text_box(s, x=c1 + pad, y=top + 3.46, w=cw - 2 * pad, h=0.62,
             text="Stenberg: AI-анализаторы «в правильных руках» находят "
                  "реальные баги — сломана архитектура процесса, не модель.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.12)

    # ---------- column 2: curl-slop asymmetry ----------
    ocean_box(s, c2, top, cw, bh)
    icon(s, "package-x", c2 + pad, top + 0.12, 0.42, "mid")
    text_box(s, x=c2 + 0.74, y=top + 0.12, w=cw - 1.30, h=0.62,
             text="2. curl-slop как DDoS на сопровождающих [2]", size=12,
             bold=True, color=MID, line_spacing=1.06)
    add_image(s, ASSETS / "logos" / "curl-logo.png", c2 + cw - 0.56, top + 0.10,
              0.40, 0.40)
    text_box(s, x=c2 + cw - 0.92, y=top + 0.52, w=0.76, h=0.18,
             text="curl — офиц. логотип", size=6.5, italic=True, color=LIGHT,
             align=PP_ALIGN.CENTER)
    text_box(s, x=c2 + pad, y=top + 0.84, w=cw - 2 * pad, h=0.44,
             text="Поток LLM-«отчётов об уязвимостях» в bug-bounty curl.",
             size=9.5, color=DEEP, line_spacing=1.12)
    filled_rect(s, c2 + pad, top + 1.32, cw - 2 * pad, 0.78, GOLD_TINT,
                stroke=GOLD, stroke_pt=1.6, radius=True, radius_adj=0.07)
    text_box(s, x=c2 + 0.38, y=top + 1.36, w=cw - 0.76, h=0.70,
             text="Асимметрия стоимости: фейк — секунды, опровергнуть — "
                  "часы сопровождающего.",
             size=10, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    text_box(s, x=c2 + pad, y=top + 2.22, w=cw - 2 * pad, h=0.72,
             text="Валидных отчётов >15% → <5% (~1 на 20–30); объём вырос "
                  "кратно; программа приостановлена, возвращена на "
                  "HackerOne март 2026.",
             size=9.5, color=DEEP, line_spacing=1.12)
    filled_rect(s, c2 + pad, top + 3.00, cw - 2 * pad, 1.02, SOFT_GREY,
                stroke=SLATE, stroke_pt=0.8, radius=True, radius_adj=0.07)
    icon(s, "message-square-warning", c2 + 0.36, top + 3.08, 0.30, "mid")
    text_box(s, x=c2 + 0.72, y=top + 3.07, w=cw - 1.00, h=0.28,
             text="matplotlib, февраль 2026 [5]", size=9.5, bold=True,
             color=DEEP)
    text_box(s, x=c2 + 0.36, y=top + 3.38, w=cw - 0.72, h=0.58,
             text="AI-агент сам написал и опубликовал эссе против "
                  "мейнтейнера, закрывшего его PR — та же экономика, "
                  "но атака на человека.",
             size=9, color=DEEP, line_spacing=1.10)

    # ---------- column 3 (NEW, round-6): redistribution, not net gain ----------
    ocean_box(s, c3, top, cw, bh)
    icon(s, "scale", c3 + pad, top + 0.12, 0.42, "teal")
    text_box(s, x=c3 + 0.74, y=top + 0.12, w=cw - 0.98, h=0.62,
             text="3. Не прирост, а перераспределение [6]", size=12,
             bold=True, color=MID, line_spacing=1.06)
    text_box(s, x=c3 + pad, y=top + 0.80, w=cw - 2 * pad, h=0.78,
             text="Xu и др.: 2 755 репозиториев GitHub, 1 699 участников, "
                  "12 месяцев до и после Copilot. «Ядро» — топ-25% по "
                  "коммитам ДО, «периферия» — остальные 75%.",
             size=9, italic=True, color=SLATE, line_spacing=1.14)
    filled_rect(s, c3 + pad, top + 1.62, cw - 2 * pad, 0.64, TEAL_TINT,
                stroke=TEAL, stroke_pt=1.3, radius=True, radius_adj=0.07)
    text_box(s, x=c3 + 0.38, y=top + 1.66, w=cw - 0.76, h=0.56,
             text="Периферия (джуны): коммиты +43,5%, PR +17,7%",
             size=10, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    filled_rect(s, c3 + pad, top + 2.32, cw - 2 * pad, 0.64, GOLD_TINT,
                stroke=GOLD, stroke_pt=1.6, radius=True, radius_adj=0.07)
    text_box(s, x=c3 + 0.38, y=top + 2.36, w=cw - 0.76, h=0.56,
             text="Ядро (сеньоры): своих коммитов −19%, ревью чужого +6,5%",
             size=10, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    text_box(s, x=c3 + pad, y=top + 3.06, w=cw - 2 * pad, h=0.28,
             text="Доработка PR после подачи: +2,4%.", size=9.5, color=DEEP)
    text_box(s, x=c3 + pad, y=top + 3.38, w=cw - 2 * pad, h=0.68,
             text="«Суммарно производительность выросла» — но прирост у "
                  "одних, а новая работа по ревью у других, и их втрое "
                  "меньше.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.12)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Во всех трёх AI не «сделал хуже» — он снял ограничитель на объём, а "
        "стоимость проверки осталась прежней. Альтернатива: машинно-проверяемый "
        "барьер на входе и честный учёт того, кто платит за проверку.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    # Round-5 meme: Evil Kermit — the inner temptation to skip reading the
    # diff and rubber-stamp instead, direct callback to complacency (col 1).
    # Round-6: shrunk + moved up so the now 6-entry ref list below clears it.
    add_image(s, WEB / "band-evil-kermit.png", 9.30, 6.38, 3.48, 0.58)
    refs_of_slide(s, "s28", y=7.00, size=7.5)
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

    # Round-6 block-4 (owner ask: «упростить, оставить только самое важное, всё
    # с расшифровками для тех, кто не в курсе»). Kept: the Lethal Trifecta
    # definition + the 4 controls. Dropped from the visible layer: the
    # four-vendor stack paragraph (GitHub/Google/AWS/Anthropic) — that space
    # now carries a full inline decoding of every surviving term. The vendor
    # examples stay in the speaker notes, where ref [3] still anchors them.

    # left: Lethal Trifecta — 3 conditions
    lx, lw = 0.55, 5.85
    top = 1.44
    ocean_box(s, lx, top, lw, 4.18)
    text_box(s, x=lx + 0.24, y=top + 0.10, w=lw - 0.48, h=0.70,
             text="Lethal Trifecta (смертельная триада, Willison, июнь 2025 [1]; "
                  "Fowler [2]) — опасно не каждое свойство по отдельности, "
                  "а пересечение всех трёх:",
             size=12, bold=True, color=MID, line_spacing=1.08)
    tri = [
        ("link", "недоверенное содержимое",
         "issue, письма, веб-страницы — писали их не вы"),
        ("key", "секреты и приватные данные",
         "ключи, токены, доступ к базе"),
        ("arrow-right-left", "исходящая передача (egress — канал наружу)",
         "агент может отправить данные за пределы контура"),
    ]
    ty = top + 0.86
    for i, (ic, head, sub) in enumerate(tri):
        y = ty + i * 0.88
        filled_rect(s, lx + 0.24, y, lw - 0.48, 0.76, SOFT_GREY, stroke=LIGHT,
                    stroke_pt=1.2, radius=True, radius_adj=0.07)
        icon(s, ic, lx + 0.40, y + 0.16, 0.44, "mid")
        text_box(s, x=lx + 0.98, y=y + 0.08, w=lw - 1.24, h=0.34,
                 text=f"{i+1}. {head}", size=11.5, bold=True, color=DEEP)
        text_box(s, x=lx + 0.98, y=y + 0.44, w=lw - 1.24, h=0.28, text=sub,
                 size=10, italic=True, color=SLATE)
    text_box(s, x=lx + 0.24, y=top + 3.56, w=lw - 0.48, h=0.60,
             text="Сошлись все три — получился готовый канал утечки: подмена "
                  "инструкции агента через прочитанный им текст (prompt "
                  "injection) → взять секрет → отправить наружу.",
             size=10, italic=True, color=MID, line_spacing=1.12)

    # right: 4 controls, each decoded inline
    rx, rw = 6.65, 6.15
    ocean_box(s, rx, top, rw, 4.18)
    text_box(s, x=rx + 0.24, y=top + 0.10, w=rw - 0.48, h=0.32,
             text="Четыре контроля, разрывающих триаду",
             size=12.5, bold=True, color=MID, line_spacing=1.0)
    ctrls = [
        ("least-privilege (наименьшие привилегии)",
         "агенту выдаём только те доступы, без которых задачу не решить. "
         "Нет ключа — нечему утекать.", 0.64),
        ("sandbox (изолированное окружение)",
         "агент работает в песочнице: его ошибка физически не достаёт "
         "до прода.", 0.50),
        ("egress-allowlist (белый список получателей)",
         "заранее перечислено, куда вообще разрешено отправлять данные; "
         "всё остальное закрыто.", 0.64),
        ("SAST-гейт (обязательный автоматический скан)",
         "SAST (static application security testing) — статический анализ "
         "кода на уязвимости до запуска; secret-scanning — поиск утёкших "
         "ключей и токенов; SCA (software composition analysis) — проверка "
         "сторонних библиотек (цепочка поставок) на известные уязвимости.",
         1.06),
    ]
    cy = top + 0.48
    for i, (term, expl, hh) in enumerate(ctrls):
        chip(s, rx + 0.24, cy + 0.03, 0.30, 0.28, str(i + 1), fill=TEAL,
             color=WHITE, size=10)
        text_box(s, x=rx + 0.64, y=cy, w=rw - 0.90, h=0.28, text=term,
                 size=11, bold=True, color=DEEP)
        text_box(s, x=rx + 0.64, y=cy + 0.28, w=rw - 0.90, h=hh - 0.28,
                 text=expl, size=9.5, color=SLATE, line_spacing=1.12)
        cy += hh + 0.06
    # caveat — the anti-hype half, kept because it is the judgment of the phase
    filled_rect(s, rx + 0.24, top + 3.58, rw - 0.48, 0.50, TEAL_TINT,
                stroke=TEAL, stroke_pt=1.3, radius=True, radius_adj=0.08)
    text_box(s, x=rx + 0.40, y=top + 3.61, w=rw - 0.80, h=0.44,
             text="«Первый AI, остановивший атаку нулевого дня» — один "
                  "отобранный случай; «AI находит 50% уязвимостей» — "
                  "измерения вендора на своём же коде [3].",
             size=9, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.10)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Устойчивый паттерн: обязательный автоматический скан как гейт + "
        "архитектурный разрыв триады. Скан необходим, но НЕ достаточен: "
        "продумать, что вообще может пойти не так, — работа человека.",
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
