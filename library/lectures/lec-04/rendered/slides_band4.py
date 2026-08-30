"""Лекция 4 v4 — Band 4 (s31–s40): Replit, доставка/ops/docs, обобщение, closing."""
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
# s31 — Replit culmination [in-bucket]
# ============================================================
def s31(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Скорость агента — это скорость катастрофы; accountability не делегируется",
                size=21, w=12.3, h=0.82)

    # left: Replit chronicle
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.52, lw, 4.02)
    text_box(s, x=lx + 0.24, y=1.64, w=lw - 0.48, h=0.66,
             text="Июль 2025, эксперимент vibe-coding (Replit; Fortune, "
                  "23.07.2025). Человек ввёл явный code-freeze: «БОЛЬШЕ НИКАКИХ "
                  "ИЗМЕНЕНИЙ». Несмотря на запрет, агент:",
             size=11.5, bold=True, color=MID, line_spacing=1.1)
    chron = [
        "удалил рабочую (production) БД (1200+ руководителей, 1190+ компаний)",
        "сфабриковал отчёты, маскирующие проблему",
        "на прямой вопрос солгал",
        "оценил своё поведение на 95 из 100",
        "заявил, что откат невозможен — хотя механизм работал, данные восстановили",
    ]
    cy = 2.30
    for i, txt in enumerate(chron):
        y = cy + i * 0.44
        circle(s, lx + 0.30, y + 0.06, 0.16, GOLD)
        text_box(s, x=lx + 0.60, y=y - 0.02, w=lw - 0.86, h=0.42, text=txt,
                 size=10.5, color=DEEP, line_spacing=1.05)
    filled_rect(s, lx + 0.24, 4.60, lw - 0.48, 0.78, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.44, y=4.68, w=lw - 0.86, h=0.64,
             text="Эхо того же класса (The Register): Amazon Kiro (дек. 2025) — "
                  "многочасовой простой · PocketOS / Cursor (апр. 2026) — стёр БД "
                  "за 9 секунд.",
             size=10.5, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.1)

    # right: 3 collapsing pillars
    rx, rw = 6.85, 5.95
    pillars = [
        ("Промпт ≠ контроль",
         "«БОЛЬШЕ НИКАКИХ ИЗМЕНЕНИЙ» для агента — не барьер среды, а текст, "
         "конкурирующий за внимание. Нет архитектурной границы между «правилом» "
         "и «пожеланием»."),
        ("Самооценка ≠ проверка",
         "«95/100» антикоррелирована с реальностью (максимальна при худшем исходе)."),
        ("Отчёт агента ≠ доказательство",
         "источник истины в постмортеме — независимая телеметрия, не нарратив агента."),
    ]
    py = 1.52
    hs = [1.30, 0.92, 0.92]
    yy = py
    for i, (head, body) in enumerate(pillars):
        ocean_box(s, rx, yy, rw, hs[i] - 0.06)
        text_box(s, x=rx + 0.24, y=yy + 0.10, w=rw - 0.48, h=0.34, text=head,
                 size=12.5, bold=True, color=MID)
        text_box(s, x=rx + 0.24, y=yy + 0.44, w=rw - 0.48, h=hs[i] - 0.54,
                 text=body, size=11, color=DEEP, line_spacing=1.14)
        yy += hs[i]
    filled_rect(s, rx, yy + 0.02, rw, 0.66, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=yy + 0.08, w=rw - 0.48, h=0.56,
             text="«95/100» при худшем результате · «9 секунд»", size=13,
             bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)

    gold_callout(
        s, 0.55, 5.70, 12.25, 0.60,
        "Безопасность уровня D не живёт в промпте — она живёт вне агента: "
        "dev/prod-изоляция, жёсткий человеческий гейт на деструктив, least-privilege, "
        "проверенный откат. Корневая ошибка — автономия, неадекватная цене "
        "ошибки [1]. Accountability не делегируется.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s32")
    notes_with_sources(s, "s32")
    return s


# ============================================================
# s32 — section divider Раздел 6 (Доставка · Ops · Docs)
# ============================================================
def s32(p):
    return build_section_divider(
        p, here_idx=6,
        subtitle="Доставка · Эксплуатация · Документация",
        bridge="Три завершающие фазы цикла. Доставка и эксплуатация — тонкие: их "
               "вход — состояние реального мира (конвейер, прод, телеметрия), "
               "которого нет в тексте. Документация — единственный светлый "
               "пятачок карты, но и у него есть цена.",
        sid="s33",
        tag="Две тонкие фазы + светлый пятачок · 3 провала")


# ============================================================
# s33 — CI/CD DORA-first + both halves [in-bucket]
# ============================================================
def s33(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Доставка — DORA-first: сначала зрелый конвейер, потом масштабировать AI",
                size=21, w=12.3, h=0.82)

    # left: DORA-first practice
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.52, lw, 4.02)
    text_box(s, x=lx + 0.24, y=1.62, w=lw - 0.48, h=1.08,
             text="Ведёт не инструмент, а порядок: сначала семь зрелых "
                  "delivery-способностей DORA — платформенная инженерия · "
                  "автотесты · контроль версий · быстрая обратная связь · "
                  "слабо-связанная архитектура · документация · малые порции — "
                  "потом масштабировать AI. «AI усиливает то, что уже есть».",
             size=11, color=DEEP, line_spacing=1.14)
    filled_rect(s, lx + 0.24, 2.80, lw - 0.48, 0.56, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.4, radius=True, radius_adj=0.07)
    text_box(s, x=lx + 0.46, y=2.87, w=lw - 0.9, h=0.44,
             text="Внутри — жёсткий человеческий прод-гейт (выкатка необратима).",
             size=11.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 0.24, y=3.46, w=lw - 0.48, h=0.74,
             text="AI потребляет конвейеры, но не владеет ими — нет "
                  "«AI-CD-продукта»; агент вызывает gh / aws / gcloud как "
                  "ограниченный по правам пользователь.",
             size=11, color=DEEP, line_spacing=1.12)
    filled_rect(s, lx + 0.24, 4.30, lw - 0.48, 1.08, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.05)
    icon(s, "wrench", lx + 0.42, 4.42, 0.44, "light")
    text_box(s, x=lx + 1.00, y=4.36, w=lw - 1.3, h=0.98,
             text="Эксплуатация — слабейшая фаза цикла: нет системного и "
                  "рантайм-контекста; отчёт агента о состоянии ≠ источник истины "
                  "(эхо Replit).",
             size=11, color=DEEP, line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)

    # right: DORA both halves chart + failure
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, 1.52, rw, 4.02)
    add_image(s, CHARTS / "c33-dora.png", rx + 0.14, 1.66, rw - 0.28, 2.40)
    filled_rect(s, rx + 0.20, 4.14, rw - 0.40, 1.20, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.5, radius=True, radius_adj=0.05)
    text_runs(s, rx + 0.40, 4.22, rw - 0.8, 1.06, [
        {"text": "+ throughput и +7,5% документации — но −7,2% стабильности "
                 "доставки", "size": 11, "bold": True, "color": DEEP,
         "line_spacing": 1.12},
        {"text": " (DORA 2024) [1]", "size": 9.5, "italic": True, "color": LIGHT},
        {"text": "; негативная связь второй год подряд (DORA 2025) [2]. Провал: "
                 "масштабировать AI на незрелый конвейер → множитель DORA в "
                 "худшую сторону.", "size": 11, "bold": True, "color": DEEP,
         "line_spacing": 1.12},
    ], anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "AI-множитель работает в обе стороны. Устойчивый паттерн: DORA-first + "
        "человеческий прод-гейт. Хайп: «AI-CD/ops-продукт как замена человека».",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s34")
    notes_with_sources(s, "s34")
    return s


# ============================================================
# s34 — docs bright spot [in-bucket]
# ============================================================
def s34(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Документация — единственный чистый плюс AI, но и у него есть парная цена",
                size=21, w=12.3, h=0.82)

    # left: bright spot (gold accent)
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.52, lw, 4.02, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.8)
    icon(s, "lightbulb", lx + 0.24, 1.66, 0.5, "gold")
    text_box(s, x=lx + 0.88, y=1.70, w=lw - 1.10, h=0.40,
             text="Светлый пятачок", size=13, bold=True, color=DEEP)
    text_box(s, x=lx + 0.24, y=2.20, w=lw - 0.48, h=1.24,
             text="Единственная фаза с чистым положительным системным эффектом "
                  "AI. Почему: доминирует привнесённая сложность; цена ошибки "
                  "асимметрично низка; встроен человеческий контроль — доки читают.",
             size=11.5, color=DEEP, line_spacing=1.18)
    filled_rect(s, lx + 0.24, 3.48, lw - 0.48, 1.06, WHITE, stroke=GOLD,
                stroke_pt=1.4, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.46, y=3.58, w=lw - 0.9, h=0.90,
             text="DORA 2024 [1]: +7,5% к качеству документации. База: цитируется "
                  "только в паре с −7,2% стабильности доставки (у эффекта AI "
                  "почти всегда парная цена); стабильность негативна второй год.",
             size=11, bold=True, color=DEEP, line_spacing=1.14,
             anchor=MSO_ANCHOR.MIDDLE)

    # right: 2 failures
    rx, rw = 6.85, 5.95
    fails = [
        ("bomb", "Когнитивный долг (Radar, Hold)",
         "генерация документации обгоняет понимание: текста много, понимания "
         "меньше. Именованное средство — архитектурные fitness-функции "
         "(Форд/Парсонс): держат «почему» в проверяемом виде."),
        ("triangle-alert", "Онбординг-доки галлюцинируют настройку / развёртывание",
         "Böckeler [2]: «AI не может волшебно заменить хорошо документированную и "
         "автоматизированную настройку»."),
    ]
    heights = [1.84, 1.30]
    yy = 1.52
    for i, (ic, head, body) in enumerate(fails):
        h = heights[i]
        ocean_box(s, rx, yy, rw, h)
        icon(s, ic, rx + 0.24, yy + 0.20, 0.5, "mid")
        text_box(s, x=rx + 0.88, y=yy + 0.20, w=rw - 1.10, h=0.56, text=head,
                 size=12.5, bold=True, color=MID, line_spacing=1.05)
        text_box(s, x=rx + 0.24, y=yy + 0.78, w=rw - 0.48, h=h - 0.86,
                 text=body, size=10.5, color=DEEP, line_spacing=1.12)
        yy += h + 0.10
    filled_rect(s, rx, 4.86, rw, 0.68, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=4.92, w=rw - 0.48, h=0.58,
             text="Вторично: Confluence AI · AWS Q /doc · JetBrains "
                  "KDoc/Javadoc.",
             size=10.5, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Практика: docs-as-context — код остаётся источником истины, "
        "документация — контекст; темп генерации ≤ темп понимания. "
        "Документация-как-контекст — да; документация-как-истина — нет.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s35")
    notes_with_sources(s, "s35")
    return s


# ============================================================
# s35 — section divider Раздел 7 (Обобщение)
# ============================================================
def s35(p):
    return build_section_divider(
        p, here_idx=7,
        subtitle="Обобщение — дисциплина по фазам",
        bridge="Мы прошли все фазы; теперь свернём их в рабочий аппарат: матрицу "
               "«фаза × ведущая практика × где человек обязателен», триангуляцию "
               "независимых измерений, компактный risk-triad и чек-лист «когда "
               "AI да, когда нет».",
        sid="s36",
        tag="Аппарат решения · практика × человек")


# ============================================================
# s36 — synthesis matrix (8 phases × 5 cols)
# ============================================================
def s36(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Матрица лекции: ведёт практика, вендор — сменяемый столбец",
                size=22, w=12.2, h=0.66)

    headers = ["Фаза", "Ведущая практика", "Режим отказа",
               "Где человек обязателен", "Вендор (вторично)"]
    # column widths (sum ~12.25)
    cws = [1.55, 3.15, 2.75, 2.65, 2.15]
    x0 = 0.55
    rows = [
        ("file-code", "Требования", "spec-driven: спека до кода",
         "prompt-and-pray; «спека=истина»", "решить, что строить",
         "Kiro, Spec-Kit, plan mode"),
        ("gavel", "Архитектура", "ADR + fitness + арх-как-код",
         "отравленный контекст без управления", "выбор развилок под компромисс",
         "нет продукта; Structurizr"),
        ("code", "Реализация", "explore→plan→code→commit + харнес",
         "70%-проблема; «почти правильный»", "ревью diff + merge",
         "Cursor, Junie, Copilot"),
        ("flask-conical", "Тестирование", "TDD: тест-как-спека + детерм. гейт",
         "«all green» лжёт; coverage≠дефекты", "что тест утверждает",
         "AWS Q /test, Qodo"),
        ("shield-check", "Ревью + Безоп.", "fresh-context; least-priv+SAST",
         "благодушие; ложная уверенность", "второй проход + угрозы",
         "Copilot review; Big Sleep"),
        ("git-merge", "Доставка", "headless + прод-гейт (DORA-first)",
         "AI потребляет, не владеет", "продакшен-гейт", "Actions; gh / CLI"),
        ("wrench", "Эксплуатация", "телеметрия + on-call",
         "нет системного контекста", "владение моделью системы",
         "AWS Q CloudWatch"),
        ("lightbulb", "Документация", "docs-as-context (код=истина)",
         "когнитивный долг; галлюцинации", "темп ≤ темп понимания",
         "Confluence AI, Q /doc"),
    ]
    top = 1.18
    hh = 0.42
    # header
    cx = x0
    for j, htxt in enumerate(headers):
        col = GOLD if j == 3 else (SOFT_GREY if j == 4 else MID)
        txtcol = DEEP if j in (3, 4) else WHITE
        filled_rect(s, cx, top, cws[j], hh, col, radius=True, radius_adj=0.10)
        text_box(s, x=cx + 0.06, y=top + 0.03, w=cws[j] - 0.12, h=hh - 0.06,
                 text=htxt, size=10.5, bold=True, color=txtcol,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=0.95)
        cx += cws[j]
    # rows
    rh = 0.485
    ry = top + hh + 0.05
    for r, row in enumerate(rows):
        ic = row[0]
        cells = row[1:]
        cx = x0
        fill = SURFACE if r % 2 == 0 else WHITE
        for j in range(5):
            cell_fill = fill
            if j == 3:
                cell_fill = GOLD_TINT
            elif j == 4:
                cell_fill = SOFT_GREY
            filled_rect(s, cx, ry, cws[j], rh, cell_fill, stroke=SOFT_GREY,
                        stroke_pt=0.8, radius=True, radius_adj=0.04)
            if j == 0:
                icon(s, ic, cx + 0.08, ry + rh / 2 - 0.16, 0.32,
                     "mid")
                text_box(s, x=cx + 0.46, y=ry + 0.04, w=cws[j] - 0.50,
                         h=rh - 0.08, text=cells[j], size=10, bold=True,
                         color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
            else:
                col = SLATE if j == 4 else DEEP
                sz = 9 if j == 4 else 9.3
                text_box(s, x=cx + 0.08, y=ry + 0.03, w=cws[j] - 0.16,
                         h=rh - 0.06, text=cells[j], size=sz,
                         color=col, anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.96)
            cx += cws[j]
        ry += rh + 0.03

    gold_callout(
        s, 0.55, 6.06, 12.25, 0.55,
        "Заменится только столбец-иллюстрация. Ведущая практика, режим отказа и "
        "точка человека устойчивы — держатся на характере сложности фазы [2]. Каждая "
        "клетка выведена из разобранного раздела, не назначена. [1]",
        size=11.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s37", y=7.08)
    notes_with_sources(s, "s37")
    return s


# ============================================================
# s37 — triangulation (3 methods converge) [in-bucket]
# ============================================================
def s37(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Три независимых метода сходятся: индивидуальная выгода AI ≠ системное качество",
        size=20, w=12.4, h=0.82)

    methods = [
        ("radar", "DORA (n ≈ 5000, системный) [1]",
         "~90% отчётов: throughput положительный, но связь AI со стабильностью "
         "негативна второй год подряд. Линза: «AI усиливает то, что уже есть»."),
        ("git-compare", "GitClear (211 млн строк) [2]",
         "рефакторинг ~25% → <10%; дубликаты 8,3% → 12,3%; churn вырос. Три "
         "маркера накопления техдолга. (Корреляция, не RCT.)"),
        ("gauge", "METR (n = 16, эксперты, знакомый код) [3]",
         "задачи с AI заняли +19% времени, а верили в ускорение (~−20%) = разрыв "
         "восприятия. (На незнакомом коде эффект иной.)"),
    ]
    cw, gap = 3.97, 0.17
    x0 = 0.55
    my = 1.52
    for i, (ic, head, body) in enumerate(methods):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, my, cw, 2.60)
        icon(s, ic, x + 0.24, my + 0.22, 0.56, "teal" if i == 1 else "mid")
        text_box(s, x=x + 0.24, y=my + 0.86, w=cw - 0.48, h=0.56, text=head,
                 size=12, bold=True, color=MID, line_spacing=1.05)
        text_box(s, x=x + 0.24, y=my + 1.44, w=cw - 0.48, h=1.06, text=body,
                 size=10.5, color=DEEP, line_spacing=1.14)
        # arrow down toward centre
        right_arrow(s, x + cw / 2 - 0.14, my + 2.62, 0.28, 0.22, fill=GOLD)

    # convergence strip
    filled_rect(s, 0.55, 4.42, 12.25, 0.94, GOLD_TINT, stroke=GOLD, stroke_pt=1.7,
                radius=True, radius_adj=0.05)
    text_box(s, x=0.80, y=4.50, w=11.75, h=0.80,
             text="Сила — в сходимости независимых методов: у DORA, GitClear и "
                  "METR разные слепые пятна, поэтому вероятность, что все три "
                  "ошиблись одинаково, мала. Общий вывод надёжнее любого "
                  "одиночного числа.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.14)

    gold_callout(
        s, 0.55, 5.56, 12.25, 0.56,
        "Вывод один: методика важнее инструмента. Практика — CI-гейт на "
        "дублирование и churn; измерять системный эффект, а не ощущение.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s38")
    notes_with_sources(s, "s38")
    return s


# ============================================================
# s38 — risk-triad (3 axes, allowed zone) [in-bucket]
# ============================================================
def s38(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "risk-triad: «когда AI да / нет» = вероятность × влияние × обнаружимость",
                size=21, w=12.3, h=0.82)

    # left: three axes with scale markers inside
    lx, lw = 0.55, 6.50
    axes = [
        ("Вероятность ошибки", "низкая → высокая",
         "растёт с незнакомостью задачи (ось SWE-bench Pro)"),
        ("Влияние ошибки", "низкое → высокое",
         "необратимость, безопасность, деньги, данные"),
        ("Обнаружимость", "низкая → высокая",
         "есть ли тест-оракул, SAST, ревью, которые поймают ошибку"),
    ]
    ay = 1.48
    ah = 1.08
    for i, (name, scale, desc) in enumerate(axes):
        y = ay + i * (ah + 0.08)
        ocean_box(s, lx, y, lw, ah)
        text_box(s, x=lx + 0.24, y=y + 0.10, w=lw - 0.48, h=0.30,
                 text=f"{i+1}. {name}", size=13, bold=True, color=MID)
        # scale bar with arrow (markers below the bar, arrow at end of bar)
        bar_y = y + 0.46
        bar_w = lw - 1.10
        filled_rect(s, lx + 0.24, bar_y, bar_w, 0.14, SOFT_GREY,
                    radius=True, radius_adj=0.5)
        right_arrow(s, lx + 0.24 + bar_w + 0.04, bar_y - 0.05, 0.44, 0.24,
                    fill=TEAL)
        text_box(s, x=lx + 0.24, y=bar_y + 0.18, w=2.6, h=0.24, text=scale,
                 size=10, italic=True, color=TEAL)
        text_box(s, x=lx + 2.95, y=bar_y + 0.16, w=lw - 3.25, h=0.42,
                 text=desc, size=9.5, color=SLATE, line_spacing=1.02)

    # right: allowed zone + which axis to fix
    rx, rw = 7.35, 5.45
    filled_rect(s, rx, 1.48, rw, 1.62, GOLD_TINT, stroke=GOLD, stroke_pt=1.9,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=1.58, w=rw - 0.48, h=0.34,
             text="Зона допустимого vibe-coding", size=13, bold=True, color=DEEP)
    text_box(s, x=rx + 0.24, y=1.96, w=rw - 0.48, h=1.06,
             text="ТОЛЬКО низкая × низкая × высокая (низкая вероятность × низкое "
                  "влияние × высокая обнаружимость). Любая другая комбинация → "
                  "дисциплина. Оси перемножаются, не складываются.",
             size=11, bold=True, color=DEEP, line_spacing=1.16)
    ocean_box(s, rx, 3.24, rw, 1.66)
    text_box(s, x=rx + 0.24, y=3.34, w=rw - 0.48, h=0.34,
             text="Триада подсказывает, что чинить:", size=12, bold=True,
             color=MID)
    fixes = [
        "влияние ↑ → жёсткий человеческий гейт, потолок автономии вниз",
        "обнаружимость ↓ → добавить машинный оракул",
        "вероятность ↑ → senior-ревью",
    ]
    for i, fx in enumerate(fixes):
        text_box(s, x=rx + 0.24, y=3.74 + i * 0.38, w=rw - 0.48, h=0.34,
                 text=f"• {fx}", size=11, color=DEEP, line_spacing=1.02)

    gold_callout(
        s, 0.55, 5.06, 12.25, 0.90,
        "Böckeler [1]: «использование генеративного AI — постоянная оценка риска». "
        "Провал — vibe-coding «по ощущению»: игнор всех трёх осей. В нём сходятся "
        "все кейсы лекции: Replit (влияние ↑), curl-slop (обнаружимость ↓), "
        "уязвимый код (вероятность ↑).",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s39")
    notes_with_sources(s, "s39")
    return s


# ============================================================
# s39 — checklist + Anthropic -17% [in-bucket]
# ============================================================
def s39(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Чек-лист «когда AI да / когда нет» + что это значит лично для вас",
                size=22, w=12.2, h=0.82)

    # left: 8-point checklist
    lx, lw = 0.55, 7.05
    ocean_box(s, lx, 1.52, lw, 4.60)
    checks = [
        ("Какая это фаза жизненного цикла?", False),
        ("Можно ли решить без AI (детерминированно)? Да → не добавляйте AI", False),
        ("Существенная или привнесённая сложность? Существенная → человек", False),
        ("Обратимо ли последствие? Необратимое → жёсткий человеческий гейт — ВЕТО-ось", True),
        ("Есть ли машинный оракул (тест, SAST, прогон)? Нет → не доверять", False),
        ("Затронуты секреты / недоверенный контент? Да → least-priv + изоляция", False),
        ("Кто ревьюит и мержит? Merge и accountability — всегда человек", False),
        ("Цель — артефакт или навык? Навык → не делегировать генерацию", False),
    ]
    ci_y = 1.72
    for i, (txt, veto) in enumerate(checks):
        y = ci_y + i * 0.535
        if veto:
            filled_rect(s, lx + 0.20, y, lw - 0.40, 0.48, GOLD_TINT,
                        stroke=GOLD, stroke_pt=1.6, radius=True, radius_adj=0.08)
        icon(s, "check-check", lx + 0.28, y + 0.06, 0.34,
             "gold" if veto else "mid")
        text_box(s, x=lx + 0.72, y=y + 0.03, w=lw - 0.94, h=0.44,
                 text=f"{i+1}. {txt}", size=11, bold=veto,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)

    # right: Anthropic -17% chart + explanation
    rx, rw = 7.85, 4.95
    ocean_box(s, rx, 1.52, rw, 4.60)
    add_image(s, CHARTS / "c39-anthropic-quiz.png", rx + 0.14, 1.66,
              rw - 0.28, 2.10)
    text_box(s, x=rx + 0.24, y=3.82, w=rw - 0.48, h=2.24,
             text="Anthropic, Shen & Tamkin 2026 (RCT, n=52, освоение незнакомой "
                  "библиотеки) [1]: группа с AI на квизе 50% против 67% без AI "
                  "(~−17 п.п.). Кто делегировал генерацию — просел; кто спрашивал "
                  "концепции («как работает, почему») — деградации нет. Ускорение "
                  "статистически не значимо.",
             size=11, color=DEEP, line_spacing=1.20)

    gold_callout(
        s, 0.55, 6.20, 12.25, 0.55,
        "Чек-лист — распределение бремени доказательства, не «всегда меньше AI»: "
        "для подходящей задачи он приведёт к высокой автономии. Необратимость и "
        "влияние — вето-ось. При обучении писать должны вы, роль AI — объяснять и проверять.",
        size=11.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s40", y=7.14)
    notes_with_sources(s, "s40")
    return s


# ============================================================
# s40 — hero closing + bridge + Q&A
# ============================================================
def s40(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    # HERO right half — engineering/review environment photo
    hx, hy, hw, hh = 7.05, 0.0, 6.283, 7.5
    add_image(s, SCR / "s40-closing.jpg", hx, hy, hw, hh, preserve_aspect=False)

    # left: carrying thought + bridges
    slide_title(s, "AI меняет цену написания кода — не цену понимания и ответственности",
                size=22, w=6.35, h=1.1, x=0.45, y=0.42)

    gold_callout(
        s, 0.45, 1.72, 6.30, 1.20,
        "AI меняет цену написания кода, но не цену понимания, что строить и кто "
        "за это отвечает. Он касается каждой фазы по-разному — и надёжность даёт "
        "не инструмент, а дисциплина по фазам.",
        size=12.5, bold=True)

    ocean_box(s, 0.45, 3.06, 6.30, 2.36)
    text_box(s, x=0.68, y=3.16, w=5.85, h=0.36,
             text="Метод переносится на все отрасли (не список инструментов):",
             size=12, bold=True, color=MID, line_spacing=1.0)
    steps = [
        "разложить деятельность на фазы",
        "спросить: привнесённая или существенная сложность",
        "потребовать базу для каждого числа и системный эффект",
        "отделить устойчивый паттерн от вендор-хайпа пятью вопросами",
    ]
    for i, st in enumerate(steps):
        y = 3.56 + i * 0.44
        circle(s, 0.70, y + 0.02, 0.30, TEAL)
        text_box(s, x=0.70, y=y + 0.02, w=0.30, h=0.30, text=str(i + 1),
                 size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=1.14, y=y, w=5.45, h=0.40, text=st, size=10.5, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)

    # bridge to seminar + Q&A
    filled_rect(s, 0.45, 5.58, 6.30, 0.62, TEAL_TINT, stroke=TEAL, stroke_pt=1.4,
                radius=True, radius_adj=0.08)
    text_box(s, x=0.68, y=5.66, w=5.85, h=0.48,
             text="Семинар 4 — примените чек-лист к реальным кейсам своими руками.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.45, y=6.36, w=6.30, h=0.7, text="Вопросы?", size=30,
             bold=True, color=DEEP)
    notes_with_sources(s, "s41")
    return s
