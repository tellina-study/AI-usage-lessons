"""Лекция 4 v4 — Band 3 (s21–s30): анти-хайп, тестирование, ревью+безопасность."""
from _helpers import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    right_arrow, circle, chip, connector, add_image, icon, slide_title,
    gold_callout, teal_callout, footer, src, speaker_notes, load_notes, notes_with_sources, refs_of_slide,
    build_section_divider, ref_list, refs_of, link_run, URLS,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE, COVER_OUTLINE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, MID_TINT, ICONS, CHARTS, ASSETS,
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
             text="Verified (~500 задач, публичный код) — топ ~88–89%. Pro "
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
             text="Ценность TDD — структура (спека-тест + гейт), а не ритуал "
                  "форсить порядок агенту. Böckeler [2]: TDD-first в agent-loop — "
                  "отсутствие выигрыша + ~3× токенов («я перестала велеть "
                  "агентам писать тесты первыми»).",
             size=11, color=DEEP, line_spacing=1.12)
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
    ocean_box(s, lx, 1.52, lw, 4.02)
    icon(s, "eye-off", lx + 0.24, 1.66, 0.5, "mid")
    text_box(s, x=lx + 0.88, y=1.70, w=lw - 1.10, h=0.40,
             text="Complacency (Radar, кольцо Hold) [1]", size=12.5, bold=True,
             color=MID)
    text_box(s, x=lx + 0.24, y=2.20, w=lw - 0.48, h=0.92,
             text="Некритичное принятие AI-кода, падение критического мышления. "
                  "CodeCrash (arXiv:2504.14119) [3]: вводящие в заблуждение "
                  "комментарии роняют рассуждение модели (~−23% на "
                  "CRUXEVAL / LIVECODEBENCH).",
             size=11, color=DEEP, line_spacing=1.14)
    filled_rect(s, lx + 0.24, 3.16, lw - 0.48, 1.00, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.4, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.46, y=3.26, w=lw - 0.9, h=0.82,
             text="AI-ревью ~19% F1 (SWR-Bench) — и это подаётся только против "
                  "human-review baseline (низко + высокий уровень ложных "
                  "срабатываний).",
             size=11.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.14)
    text_box(s, x=lx + 0.24, y=4.28, w=lw - 0.48, h=1.14,
             text="Stenberg: AI-анализаторы «в правильных руках» находят реальные "
                  "баги — виновата архитектура процесса, не AI.",
             size=11, italic=True, color=SLATE, line_spacing=1.14)

    # right: curl-slop asymmetry
    rx, rw = 6.10, 6.70
    ocean_box(s, rx, 1.52, rw, 4.02)
    icon(s, "package-x", rx + 0.24, 1.66, 0.5, "mid")
    text_box(s, x=rx + 0.88, y=1.70, w=rw - 1.10, h=0.40,
             text="curl-slop как DDoS на сопровождающих [2]", size=12.5, bold=True,
             color=MID)
    text_box(s, x=rx + 0.24, y=2.20, w=rw - 0.48, h=0.58,
             text="Поток LLM-сгенерированных «отчётов об уязвимостях» в "
                  "bug-bounty curl.",
             size=11.5, color=DEEP, line_spacing=1.14)
    # asymmetry main visual
    filled_rect(s, rx + 0.24, 2.82, rw - 0.48, 1.06, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.8, radius=True, radius_adj=0.06)
    text_runs(s, rx + 0.46, 2.94, rw - 0.9, 0.9, [
        {"text": "Асимметрия стоимости: ", "size": 13, "bold": True,
         "color": DEEP},
        {"text": "сгенерировать правдоподобный фейк — секунды; опровергнуть — "
                 "часы сопровождающего.",
         "size": 12.5, "bold": True, "color": DEEP, "line_spacing": 1.14},
    ])
    text_box(s, x=rx + 0.24, y=4.00, w=rw - 0.48, h=1.44,
             text="Числа: доля валидных отчётов >15% → <5% (~1 на 20–30); объём "
                  "вырос кратно; программа приостановлена и возвращена на "
                  "HackerOne в марте 2026.",
             size=11, color=DEEP, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "AI не «сделал спам злее» — он снял ограничитель, и сменилась экономика "
        "процесса. Альтернатива: машинно-проверяемый барьер на входе "
        "(воспроизводимый PoC), а не ручной разбор каждого текста.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
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
    text_box(s, x=rx + 0.88, y=1.70, w=rw - 1.10, h=0.40,
             text="CamoLeak (prompt injection в dev-агенте · Legit Security) [2]",
             size=12.5, bold=True, color=MID, line_spacing=1.0)
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
    refs_of_slide(s, "s31")
    notes_with_sources(s, "s31")
    return s
