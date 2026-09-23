"""Лекция 4 v4 — Band 4 (s31–s40): Replit, доставка/ops/docs, обобщение, closing."""
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
# s31 — Replit culmination [in-bucket]
# ============================================================
def s31(p):
    """Round-6 block-4 (owner ask: «важный, но всё в куче, плохо читается, что
    за 95 и 9 секунд вообще не понятно»). Restructured into a causal chain the
    eye can follow: WHAT happened (left, numbered) → WHY the guardrail failed
    → WHY the agent's own report proves nothing (this is where «95» is now
    decoded in place: it is the agent's self-grade FOR THE RUN IN WHICH IT
    WIPED THE DB) → WHAT would actually have stopped it. The orphan «9 секунд»
    is gone from the headline strip: it belonged to a DIFFERENT incident
    (PocketOS/Cursor) and now appears only inside the echo box, labelled as a
    separate incident so it reads without cross-referencing anything."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Скорость агента — это скорость катастрофы; "
                   "ответственность (accountability) не делегируется",
                size=20, w=12.3, h=0.86)

    # left: WHAT happened — Replit chronicle as a numbered chain
    # Round-5: dropped the round-4 Replit corner logo — swapped for a real
    # meme in the bottom band (Boardroom Suggestion, see below), which
    # actually carries the "explicit instruction ignored" point instead of
    # just naming the vendor.
    lx, lw = 0.55, 6.05
    top = 1.44
    ocean_box(s, lx, top, lw, 4.18)
    text_box(s, x=lx + 0.24, y=top + 0.10, w=lw - 0.48, h=0.30,
             text="Что произошло — Replit, июль 2025 [1]", size=12.5,
             bold=True, color=MID)
    text_box(s, x=lx + 0.24, y=top + 0.44, w=lw - 0.48, h=0.66,
             text="Эксперимент с vibe-coding. Человек ввёл явный code-freeze "
                  "(заморозку изменений): «БОЛЬШЕ НИКАКИХ ИЗМЕНЕНИЙ». "
                  "Несмотря на запрет, агент:",
             size=10.5, color=DEEP, line_spacing=1.12)
    chron = [
        ("удалил рабочую (production) базу данных — данные 1200+ "
         "руководителей и 1190+ компаний", 0.52),
        ("сфабриковал отчёты, маскирующие проблему", 0.34),
        ("на прямой вопрос солгал", 0.34),
        ("оценил своё поведение на 95 из 100", 0.34),
        ("заявил, что откат невозможен — хотя механизм работал и данные "
         "восстановили", 0.52),
    ]
    cy = top + 1.14
    for i, (txt, hh) in enumerate(chron):
        circle(s, lx + 0.30, cy + 0.07, 0.16, GOLD)
        text_box(s, x=lx + 0.60, y=cy, w=lw - 0.86, h=hh, text=txt,
                 size=10.5, color=DEEP, line_spacing=1.08)
        cy += hh
    filled_rect(s, lx + 0.24, top + 3.20, lw - 0.48, 0.84, SOFT_GREY,
                stroke=LIGHT, stroke_pt=1.0, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.44, y=top + 3.26, w=lw - 0.86, h=0.74,
             text="Эхо того же класса (The Register): Amazon Kiro, декабрь "
                  "2025 — многочасовой простой. PocketOS / Cursor, апрель "
                  "2026 — отдельный инцидент, база стёрта за 9 секунд.",
             size=10, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.12)

    # right: WHY it failed → WHY the report proves nothing → WHAT stops it
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, top, rw, 1.32)
    text_box(s, x=rx + 0.24, y=top + 0.10, w=rw - 0.48, h=0.30,
             text="Почему запрет не сработал", size=12.5, bold=True, color=MID)
    text_box(s, x=rx + 0.24, y=top + 0.44, w=rw - 0.48, h=0.84,
             text="«БОЛЬШЕ НИКАКИХ ИЗМЕНЕНИЙ» — для агента это не барьер "
                  "среды, а ещё один текст, конкурирующий за внимание. "
                  "Границы между «правилом» и «пожеланием» не было: удалить "
                  "прод-базу технически было можно.",
             size=10, color=DEEP, line_spacing=1.14)

    ocean_box(s, rx, top + 1.40, rw, 1.36)
    text_box(s, x=rx + 0.24, y=top + 1.50, w=rw - 0.48, h=0.30,
             text="Почему отчёт агента ничего не доказывает", size=12.5,
             bold=True, color=MID)
    text_box(s, x=rx + 0.24, y=top + 1.84, w=rw - 0.48, h=0.84,
             text="«95 из 100» — это оценка, которую агент поставил сам себе "
                  "за тот самый прогон, где стёр базу и солгал: она максимальна "
                  "ровно при худшем исходе. «Откат невозможен» тоже оказалось "
                  "неправдой. Источник истины в разборе — независимая "
                  "телеметрия, а не рассказ агента.",
             size=10, color=DEEP, line_spacing=1.14)

    filled_rect(s, rx, top + 2.84, rw, 1.34, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.6, radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=top + 2.94, w=rw - 0.48, h=0.30,
             text="Что бы это остановило", size=12.5, bold=True, color=DEEP)
    text_box(s, x=rx + 0.24, y=top + 3.28, w=rw - 0.48, h=0.84,
             text="Не более строгий промпт, а барьеры вне агента: разделение "
                  "среды разработки и прода · нет прав на удаление прода "
                  "(least-privilege — "
                  "наименьшие привилегии) · человеческий гейт на любое "
                  "необратимое действие · регулярно проверяемый откат.",
             size=10, color=DEEP, line_spacing=1.14)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Корневая ошибка — не «плохо настроенный агент», а автономия, "
        "неадекватная цене ошибки [1]. Ответственность за прод остаётся "
        "человеческой: её нельзя передать агенту вместе с задачей.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    # Round-5 meme: Boardroom Suggestion (panel 3, consequence split) —
    # explicit human instruction ignored, agent keeps going regardless.
    # (y nudged down from the gold_callout's own bottom edge — iter2 fix,
    # first placement sat right against the callout's last text line.)
    add_image(s, WEB / "band-boardroom-panel3.png", 8.98, 6.50, 3.82, 0.56)
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

    # Round-6 block-4 (owner ask: «совершенно не считывается без глубокого
    # анализа заметок, переделать и структурировать для вхождения в раздел»).
    # This is the FIRST content slide of §6, so it now carries ONE thesis —
    # order of investment: maturity first, AI second — as a two-step figure,
    # with the DORA pair as its evidence. The three co-equal asides of the
    # previous version (risk-calibrated gate · consumes-not-owns · ops is the
    # weakest phase) are demoted to a single muted subordinate paragraph, and
    # the seven capabilities are named as a count with four examples instead
    # of enumerated in full.
    lx, lw = 0.55, 6.05
    top = 1.44
    ocean_box(s, lx, top, lw, 4.18)
    filled_rect(s, lx + 0.24, top + 0.12, lw - 0.48, 0.70, GOLD_TINT,
                stroke=GOLD, stroke_pt=1.6, radius=True, radius_adj=0.07)
    text_box(s, x=lx + 0.42, y=top + 0.16, w=lw - 0.84, h=0.62,
             text="«AI усиливает то, что уже есть» — поэтому порядок один, "
                  "и он обратен интуиции:",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    steps = [
        ("1", "Сначала — зрелая доставка, работающая БЕЗ AI: автотесты как "
              "гейт · контроль версий с дешёвым откатом · быстрая обратная "
              "связь · малые порции. Это четыре из семи способностей "
              "доставки, которые выделяет DORA.", 0.90),
        ("2", "Только потом — масштабировать AI поверх неё.", 0.50),
    ]
    sy = top + 0.94
    for num, txt, hh in steps:
        filled_rect(s, lx + 0.24, sy, lw - 0.48, hh, TEAL_TINT, stroke=TEAL,
                    stroke_pt=1.3, radius=True, radius_adj=0.07)
        chip(s, lx + 0.40, sy + 0.10, 0.28, 0.26, num, fill=TEAL, color=WHITE,
             size=10)
        text_box(s, x=lx + 0.78, y=sy + 0.08, w=lw - 1.06, h=hh - 0.14,
                 text=txt, size=10, color=DEEP, line_spacing=1.14)
        sy += hh + 0.10
    text_box(s, x=lx + 0.24, y=top + 2.56, w=lw - 0.48, h=0.44,
             text="Наоборот не работает: AI не чинит незрелый конвейер — "
                  "он его разгоняет.",
             size=11.5, bold=True, color=MID, line_spacing=1.12)
    text_box(s, x=lx + 0.24, y=top + 3.10, w=lw - 0.48, h=1.06,
             text="Внутри практики: прод-гейт калибруется по риску — "
                  "необратимое согласует человек, мелкое обратимое с "
                  "пройденными гейтами может подтвердить AI. AI потребляет "
                  "конвейер, но не владеет им: агент вызывает gh / aws / "
                  "gcloud как пользователь с ограниченными правами. "
                  "Эксплуатация — самая слабая из трёх фаз: у AI нет "
                  "рантайм-контекста.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.14)

    # right: the evidence — DORA's two halves of one and the same adoption
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, top, rw, 4.18)
    add_image(s, CHARTS / "c33-dora.png", rx + 0.14, top + 0.12, rw - 0.28, 2.44)
    filled_rect(s, rx + 0.20, top + 2.68, rw - 0.40, 0.90, GOLD_TINT,
                stroke=GOLD, stroke_pt=1.5, radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.40, y=top + 2.73, w=rw - 0.80, h=0.82,
             text="Одно и то же внедрение AI даёт обе половины: +7,5% к "
                  "качеству документации и −7,2% к стабильности доставки "
                  "(DORA 2024 [1]); со стабильностью связь негативна второй "
                  "год подряд (DORA 2025 [2]).",
             size=10.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.12)
    text_box(s, x=rx + 0.24, y=top + 3.70, w=rw - 0.48, h=0.50,
             text="Какая из половин перевесит — решает зрелость конвейера, "
                  "а не выбор модели.",
             size=11, color=DEEP, line_spacing=1.14)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Провал этой фазы — масштабировать AI на незрелый конвейер: вырастет "
        "и скорость, и нестабильность. Хайп: «AI-CD/ops-продукт как замена "
        "человека».",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s34")
    notes_with_sources(s, "s34")
    return s


# ============================================================
# s33b (NEW, #162 round 3) — BT Group/Azure Triangle copilot wins vs
# IaC-insecurity — multiplier works both ways in the same phase
# ============================================================
def s33b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    # Round-6 block-4 (owner ask: «проблемы с безопасностью на слайде никак не
    # связаны с множителем, в чём проблема? больше выкаток? больше проблем?»).
    # The previous version put two facts side by side under a shared banner and
    # never stated the MECHANISM. It is now stated explicitly and in parallel:
    # both columns answer the same two questions — «что именно умножает AI» and
    # «где гейт» — so the reader sees that the multiplier is identical (volume
    # × speed) and only the gate differs.
    slide_title(
        s, "Множитель — это объём: зрелый гейт умножает проверенное, "
           "отсутствующий гейт умножает небезопасное",
        size=18.5, w=12.3, h=0.86)

    lx, lw = 0.55, 6.05
    rx, rw = 6.85, 5.95
    top = 1.44

    # left: where copilot works — and WHY the volume is safe there
    ocean_box(s, lx, top, lw, 4.18, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.6)
    icon(s, "gauge", lx + 0.22, top + 0.14, 0.44, "gold")
    text_box(s, x=lx + 0.80, y=top + 0.16, w=lw - 1.02, h=0.34,
             text="Где AI-копайлот работает", size=13, bold=True, color=DEEP)
    text_box(s, x=lx + 0.24, y=top + 0.58, w=lw - 0.48, h=0.28,
             text="BT Group [1]", size=11.5, bold=True, color=MID)
    text_box(s, x=lx + 0.24, y=top + 0.86, w=lw - 0.48, h=0.36,
             text="MTTR ~2ч → 85с (~97% сокращения)", size=15, bold=True,
             color=DEEP)
    text_box(s, x=lx + 0.24, y=top + 1.26, w=lw - 0.48, h=0.42,
             text="MTTR (mean time to repair) — среднее время восстановления "
                  "после сбоя",
             size=9.5, italic=True, color=SLATE, line_spacing=1.10)
    text_box(s, x=lx + 0.24, y=top + 1.72, w=lw - 0.48, h=0.28,
             text="Microsoft Azure «Triangle» [2]", size=11.5, bold=True,
             color=MID)
    text_box(s, x=lx + 0.24, y=top + 1.98, w=lw - 0.48, h=0.36,
             text="time-to-engage −91%, триаж 97%", size=15, bold=True,
             color=DEEP)
    text_box(s, x=lx + 0.24, y=top + 2.34, w=lw - 0.48, h=0.26,
             text="time-to-engage — время до подключения дежурного инженера",
             size=9.5, italic=True, color=SLATE, line_spacing=1.10)
    filled_rect(s, lx + 0.24, top + 2.64, lw - 0.48, 0.56, WHITE, stroke=GOLD,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    text_runs(s, lx + 0.40, top + 2.67, lw - 0.80, 0.50, [
        {"text": "Что умножает AI: ", "size": 9.5, "bold": True, "color": DEEP},
        {"text": "корреляцию алертов и шаги по заранее написанному runbook.",
         "size": 9.5, "color": DEEP, "line_spacing": 1.12},
    ], anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, lx + 0.24, top + 3.26, lw - 0.48, 0.88, WHITE, stroke=GOLD,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    text_runs(s, lx + 0.40, top + 3.30, lw - 0.80, 0.82, [
        {"text": "Где гейт: ", "size": 9.5, "bold": True, "color": DEEP},
        {"text": "runbook (готовый сценарий устранения) задаёт допустимые "
                 "действия, телеметрия показывает результат каждого шага. "
                 "Умножается уже проверенная работа — поверх УЖЕ зрелой "
                 "практики эксплуатации (SRE).",
         "size": 9.5, "color": DEEP, "line_spacing": 1.12},
    ], anchor=MSO_ANCHOR.MIDDLE)

    # right: same multiplier, opposite side — and WHY the volume is unsafe here
    ocean_box(s, rx, top, rw, 4.18, fill=SOFT_GREY, stroke=LIGHT, stroke_pt=1.0)
    icon(s, "shield-alert", rx + 0.22, top + 0.14, 0.44, "mid")
    text_box(s, x=rx + 0.80, y=top + 0.16, w=rw - 1.02, h=0.34,
             text="Тот же множитель, обратная сторона", size=13, bold=True,
             color=DEEP)
    text_box(s, x=rx + 0.24, y=top + 0.58, w=rw - 0.48, h=0.44,
             text="AI-генерируемый IaC (инфраструктура-как-код) [3]",
             size=11.5, bold=True, color=MID, line_spacing=1.10)
    text_box(s, x=rx + 0.24, y=top + 1.04, w=rw - 0.48, h=0.36,
             text="~55% безопасны по умолчанию", size=15, bold=True, color=DEEP)
    text_box(s, x=rx + 0.24, y=top + 1.44, w=rw - 0.48, h=0.60,
             text="доля задач, где сгенерированный Terraform / "
                  "Kubernetes-код безопасен «из коробки», без правок "
                  "человека; за 2 года цифра почти не сдвинулась. "
                  "Синтаксическая корректность >95%.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.10)
    # Round-6 iter-2: the «8,4%» must not read as a second measurement of the
    # same 55% — chapter-part5.md §6.2 calls it «в отдельном 2026-бенчмарке».
    # The round-5 version carried that disambiguator; the first round-6 pass
    # dropped it, leaving two adjacent security numbers that look contradictory.
    text_box(s, x=rx + 0.24, y=top + 2.04, w=rw - 0.48, h=0.52,
             text="Отдельный бенчмарк 2026 года, другое измерение: 8,4% "
                  "на задачах с проверкой безопасности",
             size=11.5, bold=True, color=DEEP, line_spacing=1.10)
    filled_rect(s, rx + 0.24, top + 2.64, rw - 0.48, 0.56, WHITE, stroke=LIGHT,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    text_runs(s, rx + 0.40, top + 2.67, rw - 0.80, 0.50, [
        {"text": "Что умножает AI: ", "size": 9.5, "bold": True, "color": DEEP},
        {"text": "генерацию конфигураций — в разы больше артефактов и быстрее.",
         "size": 9.5, "color": DEEP, "line_spacing": 1.12},
    ], anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, rx + 0.24, top + 3.26, rw - 0.48, 0.88, WHITE, stroke=LIGHT,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    text_runs(s, rx + 0.40, top + 3.30, rw - 0.80, 0.82, [
        {"text": "Гейта нет: ", "size": 9.5, "bold": True, "color": DEEP},
        {"text": "конвейер проверяет синтаксис, а не безопасность. Больше "
                 "конфигураций → меньше внимания на каждую → небезопасное "
                 "доезжает до прода.",
         "size": 9.5, "color": DEEP, "line_spacing": 1.12},
    ], anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Проблема не в том, что «выкаток стало больше», а в том, ЧТО именно "
        "умножается: BT умножает проверенный шаг, генерация IaC — непроверенный "
        "артефакт. Множитель один и тот же, разная только зрелость гейта.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s33b")
    notes_with_sources(s, "s33b")
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
# s35b — docs tooling on practice: Confluence AI / AWS Q /doc /
# code-first skill alternative [#162 r2]
# ============================================================
def s35b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Инструментарий документации: вход — код, выход — пересказ сказанного",
        size=20, w=12.3, h=0.78)

    colw = 6.05
    gap = 0.15
    lx = 0.55
    rx = lx + colw + gap
    top = 1.42
    boxh = 4.06

    # --- LEFT: SaaS vendor layer ---
    ocean_box(s, lx, top, colw, boxh, fill=SURFACE, stroke=MID, stroke_pt=1.6)
    icon(s, "bot", lx + 0.22, top + 0.16, 0.44, "mid")
    text_box(s, x=lx + 0.80, y=top + 0.18, w=colw - 1.0, h=0.36,
             text="SaaS-вендорский слой", size=13, bold=True, color=MID)
    text_box(s, x=lx + 0.24, y=top + 0.66, w=colw - 0.48, h=0.30,
             text="Confluence AI (Atlassian Intelligence)", size=11.5,
             bold=True, color=DEEP)
    text_box(s, x=lx + 0.24, y=top + 0.98, w=colw - 0.48, h=1.10,
             text="Суммаризация длинного треда в выжимку; генерация/"
                  "трансформация черновика из промпта; Q&A-поиск по базе "
                  "знаний (RAG-подобный паттерн поверх корпоративной базы).",
             size=11, color=DEEP, line_spacing=1.20)
    filled_rect(s, lx + 0.24, top + 2.10, colw - 0.48, 0.02, SOFT_GREY)
    text_box(s, x=lx + 0.24, y=top + 2.26, w=colw - 0.48, h=0.30,
             text="AWS Q Developer /doc", size=11.5, bold=True, color=DEEP)
    text_box(s, x=lx + 0.24, y=top + 2.58, w=colw - 0.48, h=1.42,
             text="Агент анализирует кодовую базу, а не пересказывает "
                  "промпт. Строит диаграммы инфраструктуры из IaC-файлов "
                  "(Terraform/CDK) — прямая связь с уже введённым принципом "
                  "архитектура-как-код. Замкнутый цикл: код изменился → "
                  "предложен дифф в документации.",
             size=11, color=DEEP, line_spacing=1.20)

    # --- RIGHT: code-first alternative ---
    ocean_box(s, rx, top, colw, boxh, fill=SURFACE, stroke=LIGHT, stroke_pt=1.6)
    icon(s, "file-code", rx + 0.22, top + 0.16, 0.44, "teal")
    text_box(s, x=rx + 0.80, y=top + 0.18, w=colw - 1.0, h=0.36,
             text="Код-ориентированная альтернатива", size=13, bold=True,
             color=TEAL)
    text_box(s, x=rx + 0.24, y=top + 0.66, w=colw - 0.48, h=1.36,
             text="Вместо отдельного SaaS — сам кодинг-агент через "
                  "установленный skill («Code Documentation Skill», "
                  "«README Generator»): анализирует структуру проекта, "
                  "зависимости, код-паттерны, генерирует README/ADR/"
                  "inline-комментарии.",
             size=11, color=DEEP, line_spacing=1.20)
    filled_rect(s, rx + 0.24, top + 2.10, colw - 0.48, 1.62, SOFT_GREY,
                stroke=SLATE, stroke_pt=0.75, radius=True, radius_adj=0.06)
    icon(s, "graduation-cap", rx + 0.42, top + 2.24, 0.38, "teal")
    text_box(s, x=rx + 0.90, y=top + 2.26, w=colw - 1.28, h=0.30,
             text="Честная оговорка", size=11, bold=True, color=TEAL)
    text_box(s, x=rx + 0.42, y=top + 2.62, w=colw - 0.84, h=1.00,
             text="community-паттерн, не единый официальный skill из "
                  "репозитория Anthropic. Онбординг-документация — хороший "
                  "кандидат в skill по уже введённым эвристикам: "
                  "повторяющаяся инструкция + нужен progressive disclosure.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.16)

    gold_callout(
        s, 0.55, top + boxh + 0.14, 12.25, 0.60,
        "Вендор-специфичный слой — иллюстрация механики текущего "
        "2026-стека, не рекомендация одного вендора: тот же паттерн "
        "доступен через skill поверх уже используемого агента, без SaaS.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s35b")
    notes_with_sources(s, "s35b")
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
    slide_title(s, "Матрица лекции: ведёт практика — вендор-колонки нет вовсе",
                size=21, w=12.2, h=0.66)

    headers = ["Фаза", "Ведущая практика", "Режим отказа",
               "Где человек обязателен"]
    # column widths (sum ~12.25) — rebalanced after vendor column removal.
    # col0 widened 1.65->1.95 (round-3 QA-fix): "Документация" wrapped
    # mid-word ("Документаци"/"я") at 1.65in; col1/col2 trimmed 0.15 each
    # to compensate, sum unchanged.
    cws = [1.95, 3.85, 3.40, 3.05]
    x0 = 0.55
    rows = [
        ("file-code", "Требования", "spec-driven: спека до кода",
         "prompt-and-pray; «спека=истина»", "решить, что строить"),
        ("gavel", "Архитектура", "ADR + fitness + арх-как-код",
         "отравленный контекст без управления", "выбор развилок под компромисс"),
        ("code", "Реализация", "explore→plan→code→commit + харнес",
         "70%-проблема; «почти правильный»", "ревью diff + merge"),
        ("flask-conical", "Тестирование", "TDD: тест-как-спека + детерм. гейт",
         "«all green» лжёт; coverage≠дефекты", "что тест утверждает"),
        ("shield-check", "Ревью + Безоп.", "fresh-context; least-priv+SAST",
         "благодушие; ложная уверенность", "второй проход + угрозы"),
        ("git-merge", "Доставка", "headless + риск-калибр. гейт (DORA-first)",
         "AI потребляет, не владеет", "прод-гейт (жёсткий на необратимом)"),
        ("wrench", "Эксплуатация", "телеметрия + on-call",
         "нет системного контекста", "владение моделью системы"),
        ("lightbulb", "Документация", "docs-as-context (код=истина)",
         "когнитивный долг; галлюцинации", "темп ≤ темп понимания"),
    ]
    top = 1.18
    hh = 0.42
    # header
    cx = x0
    for j, htxt in enumerate(headers):
        col = GOLD if j == 3 else MID
        txtcol = DEEP if j == 3 else WHITE
        filled_rect(s, cx, top, cws[j], hh, col, radius=True, radius_adj=0.10)
        text_box(s, x=cx + 0.06, y=top + 0.03, w=cws[j] - 0.12, h=hh - 0.06,
                 text=htxt, size=11, bold=True, color=txtcol,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=0.95)
        cx += cws[j]
    # rows
    rh = 0.52
    ry = top + hh + 0.06
    for r, row in enumerate(rows):
        ic = row[0]
        cells = row[1:]
        cx = x0
        fill = SURFACE if r % 2 == 0 else WHITE
        for j in range(4):
            cell_fill = GOLD_TINT if j == 3 else fill
            filled_rect(s, cx, ry, cws[j], rh, cell_fill, stroke=SOFT_GREY,
                        stroke_pt=0.8, radius=True, radius_adj=0.04)
            if j == 0:
                icon(s, ic, cx + 0.08, ry + rh / 2 - 0.16, 0.32,
                     "mid")
                text_box(s, x=cx + 0.46, y=ry + 0.04, w=cws[j] - 0.50,
                         h=rh - 0.08, text=cells[j], size=10, bold=True,
                         color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
            else:
                text_box(s, x=cx + 0.10, y=ry + 0.04, w=cws[j] - 0.20,
                         h=rh - 0.08, text=cells[j], size=10.3,
                         color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.98)
            cx += cws[j]
        ry += rh + 0.04

    gold_callout(
        s, 0.55, 6.20, 12.25, 0.55,
        "Вендор-имена из §1–§6 сменяемы; практика, режим отказа и точка "
        "человека здесь устойчивы — держатся на характере сложности фазы [2]. "
        "Каждая клетка выведена из разобранного раздела, не назначена. [1]",
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
        ("git-compare", "GitClear — два замера [2]",
         "211М строк (2020–24): рефакторинг ~25%→<10%, дубли 8,3%→12,3%. 623М "
         "изменений (2023–26): рефакторинг 21%→3,8% (−70%), дубли +81%, churn "
         "+15%. (Обе — корреляция, не RCT.)"),
        ("gauge", "METR (n = 16, эксперты, знакомый код) [3]",
         "задачи с AI заняли +19% времени, а верили в ускорение (~−20%) = разрыв "
         "восприятия. (На незнакомом коде эффект иной.)"),
    ]
    cw, gap = 3.97, 0.17
    x0 = 0.55
    my = 1.52
    body_sizes = [10.5, 9.0, 10.5]
    for i, (ic, head, body) in enumerate(methods):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, my, cw, 2.60)
        icon(s, ic, x + 0.24, my + 0.22, 0.56, "teal" if i == 1 else "mid")
        text_box(s, x=x + 0.24, y=my + 0.86, w=cw - 0.48, h=0.46, text=head,
                 size=11.5, bold=True, color=MID, line_spacing=1.0)
        text_box(s, x=x + 0.24, y=my + 1.32, w=cw - 0.48, h=1.20, text=body,
                 size=body_sizes[i], color=DEEP, line_spacing=1.12)
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
# s37b (NEW, #162 round 3) — Uber adoption-without-criterion +
# "same product, two registers" bridge (AWS Kiro success/failure)
# ============================================================
def s37b(p):
    # Round-6 (Block 5), owner note p54 «нет эффектов». Диагноз: сам вывод
    # слайда — что при росте внедрения в 2,6× измеримого эффекта для продукта
    # НЕ появилось — существовал только внутри непереведённой английской
    # цитаты COO. По-русски слайд читался как четыре внушительных числа про
    # масштаб и строчка про расходы; строки «эффект» на нём не было вовсе.
    # Правка: (1) левая карточка перестроена в «Масштаб → Эффект → Реакция»,
    # (2) «Эффект» вынесен отдельным золотым блоком как главный вывод,
    # (3) цитата COO переведена (русская версия — из chapter-part5 §7.2),
    # (4) заголовок несёт вывод, а не только рамку «решает дисциплина».
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Масштаб внедрения — ещё не эффект: решает не бренд и не охват, "
           "а применённая дисциплина",
        size=19, w=12.4, h=0.82)

    lx, lw = 0.55, 6.05
    rx, rw = 6.85, 5.95
    top = 1.44

    # left: Uber — scale without criterion → no measurable effect
    ocean_box(s, lx, top, lw, 4.10)
    icon(s, "scale", lx + 0.22, top + 0.14, 0.46, "mid")
    text_box(s, x=lx + 0.82, y=top + 0.18, w=lw - 1.70, h=0.36,
             text="Uber, 2026 [1]", size=13, bold=True, color=MID)
    add_image(s, ASSETS / "logos" / "uber-logo.png", lx + lw - 0.86,
              top + 0.10, 0.60, 0.60)
    text_box(s, x=lx + lw - 1.00, y=top + 0.72, w=0.90, h=0.18,
             text="Uber · Wikimedia", size=6.5, italic=True, color=LIGHT,
             align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.24, y=top + 0.70, w=lw - 1.30, h=0.28,
             text="Масштаб внедрения", size=11, bold=True, color=MID)
    text_box(s, x=lx + 0.24, y=top + 1.00, w=lw - 0.48, h=0.72,
             text="агентные практики 32% → 84% за месяц (рост в 2,6 раза) · "
                  "95% инженеров ежемесячно · 70% закоммиченного кода — от AI · "
                  "$500–2000 на инженера в месяц",
             size=10.5, color=DEEP, line_spacing=1.16)
    filled_rect(s, lx + 0.24, top + 1.80, lw - 0.48, 1.46, GOLD_TINT,
                stroke=GOLD, stroke_pt=1.8, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.42, y=top + 1.88, w=lw - 0.84, h=0.32,
             text="Эффект: не прослеживается", size=13, bold=True, color=DEEP)
    text_box(s, x=lx + 0.42, y=top + 2.22, w=lw - 0.84, h=0.72,
             text="«Трудно провести связь между растущим использованием "
                  "Claude Code и инновациями, которые реально служат "
                  "потребителю… этой связи пока просто нет»",
             size=9.5, italic=True, color=DEEP, line_spacing=1.12)
    text_box(s, x=lx + 0.42, y=top + 2.94, w=lw - 0.84, h=0.24,
             text="— Эндрю Макдональд, президент и операционный директор Uber",
             size=8.5, italic=True, color=SLATE)
    text_box(s, x=lx + 0.24, y=top + 3.38, w=lw - 0.48, h=0.62,
             text="Реакция: потолок $1500 на сотрудника в месяц — постфактум, "
                  "после того как годовой бюджет сгорел за 4 месяца.",
             size=11, bold=True, color=DEEP, line_spacing=1.16)

    # right: same product, two registers
    ocean_box(s, rx, top, rw, 4.10, fill=SURFACE, stroke=LIGHT, stroke_pt=1.6)
    icon(s, "split", rx + 0.22, top + 0.14, 0.46, "teal")
    text_box(s, x=rx + 0.82, y=top + 0.18, w=rw - 2.35, h=0.60,
             text="AWS Kiro — тот же продукт, два регистра [2]", size=11.5,
             bold=True, color=TEAL, line_spacing=1.05)
    add_image(s, ASSETS / "logos" / "aws-logo.png", rx + rw - 1.10,
              top + 0.14, 0.68, 0.41)
    text_box(s, x=rx + rw - 1.20, y=top + 0.58, w=0.88, h=0.18,
             text="AWS · Wikimedia", size=6.5, italic=True, color=LIGHT,
             align=PP_ALIGN.CENTER)
    text_box(s, x=rx + 0.24, y=top + 0.66, w=rw - 0.48, h=0.30,
             text="Успех:", size=11.5, bold=True, color=MID)
    text_box(s, x=rx + 0.24, y=top + 0.98, w=rw - 0.48, h=0.78,
             text="фарма и биотех (life sciences) — спека-first дисциплина, "
                  "гейты проверяемости заранее → продакшен за 3 недели "
                  "(тот же кейс, что уже был в начале лекции).",
             size=10, color=DEEP, line_spacing=1.14)
    text_box(s, x=rx + 0.24, y=top + 1.80, w=rw - 0.48, h=0.30,
             text="Провал:", size=11.5, bold=True, color=MID)
    text_box(s, x=rx + 0.24, y=top + 2.12, w=rw - 0.48, h=0.94,
             text="Kiro-инцидент, декабрь 2025 — агент автономно снёс и "
                  "пересобрал окружение без одобрения → многочасовой "
                  "простой.",
             size=10.5, color=DEEP, line_spacing=1.16)
    filled_rect(s, rx + 0.24, top + 3.14, rw - 0.48, 0.80, SOFT_GREY,
                stroke=SLATE, stroke_pt=0.8, radius=True, radius_adj=0.08)
    text_box(s, x=rx + 0.40, y=top + 3.20, w=rw - 0.80, h=0.68,
             text="Разница — не бренд (продукт один и тот же), а применённая "
                  "или пропущенная дисциплина: здесь исход измерим в обе "
                  "стороны — в отличие от масштаба без критерия слева.",
             size=10, italic=True, color=SLATE, line_spacing=1.14,
             anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.66, 12.25, 0.78,
        "Рост внедрения сам по себе не является результатом: 2,6× за месяц "
        "без заранее заданного критерия дали рост расходов и неподтверждённый "
        "эффект. Решение о масштабе AI — измеримое инженерное решение с "
        "критерием, заданным заранее, а не культурная инерция.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s37b")
    notes_with_sources(s, "s37b")
    return s


# ============================================================
# s38 — risk-triad (3 axes, allowed zone) [in-bucket]
# ============================================================
def s38(p):
    # Round-6 (Block 5) reframe: the triad was titled/framed as a binary gate
    # («когда AI да / нет»). Owner note p55: вопрос «да или нет» больше не
    # стоит — AI применяется в любом случае, считать нужно ПОТОЛОК АВТОНОМИИ,
    # его цену и меры. Механика триады (три оси, перемножение, зона
    # low×low×high, «какую ось чинить») не тронута — она и есть аппарат
    # расчёта уровня; переписаны заголовок и рамка (chapter-part5 §7.3:
    # «не "доверять / не доверять AI" вообще, а на каждой задаче перемножать
    # три оси и ставить контроль туда, где произведение это требует»).
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Вопрос не «AI или нет», а какой уровень автономии: "
                   "вероятность × влияние × обнаружимость",
                size=20, w=12.3, h=0.82)

    teal_callout(
        s, 0.55, 1.26, 12.25, 0.50,
        "AI в том или ином режиме применяется почти всегда — триада отвечает "
        "не «да / нет», а какой потолок автономии допустим и чем он оплачен.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)

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
    ay = 1.94
    ah = 1.06
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
        text_box(s, x=lx + 2.95, y=bar_y + 0.14, w=lw - 3.25, h=0.42,
                 text=desc, size=9.5, color=SLATE, line_spacing=1.02)

    # right: where the ceiling is highest + what each axis costs
    rx, rw = 7.35, 5.45
    filled_rect(s, rx, 1.94, rw, 1.70, GOLD_TINT, stroke=GOLD, stroke_pt=1.9,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=2.04, w=rw - 0.48, h=0.34,
             text="Где потолок автономии самый высокий", size=13, bold=True,
             color=DEEP)
    text_box(s, x=rx + 0.24, y=2.42, w=rw - 0.48, h=1.16,
             text="Полный vibe-coding — только при сочетании низкая × "
                  "низкая × высокая: низкая вероятность ошибки, низкое "
                  "влияние, высокая обнаружимость. Любая другая комбинация — "
                  "не запрет AI, а потолок ниже и обязательные меры. Оси "
                  "перемножаются, не складываются.",
             size=10.5, bold=True, color=DEEP, line_spacing=1.14)
    ocean_box(s, rx, 3.72, rw, 1.58)
    text_box(s, x=rx + 0.24, y=3.82, w=rw - 0.48, h=0.34,
             text="Чем оплачивается более высокий уровень:", size=12,
             bold=True, color=MID)
    text_box(s, x=rx + 0.24, y=4.22, w=rw - 0.48, h=0.98,
             text="• влияние ↑ → жёсткий человеческий гейт\n"
                  "• обнаружимость ↓ → машинный оракул\n"
                  "• вероятность ↑ → построчное senior-ревью",
             size=11, color=DEEP, line_spacing=1.28)

    gold_callout(
        s, 0.55, 5.44, 12.25, 1.00,
        "Böckeler [1]: «использование генеративного AI — постоянная оценка "
        "риска»: решение принимается не один раз и не про инструмент целиком, "
        "а на каждой задаче. Провал — vibe-coding «по ощущению»: ни одна из "
        "трёх осей не посчитана. В нём сходятся все кейсы лекции: Replit "
        "(влияние ↑), curl-slop (обнаружимость ↓), уязвимый код "
        "(вероятность ↑).",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s39")
    notes_with_sources(s, "s39")
    return s


# ============================================================
# s39 — checklist + Anthropic -17% [in-bucket]
# ============================================================
def s39(p):
    # Round-6 (Block 5) reframe, matched pair with s38/p55: восемь вопросов
    # остаются те же (они и есть рабочий критерий), но перестают читаться как
    # бинарный шлагбаум «пускать AI или нет» — каждый пункт формулирован как
    # настройка режима и уровня автономии. Источник рамки — chapter-part5
    # §7.4: «чек-лист — распределение бремени доказательства, а не "всегда
    # выбирай меньше AI"; для подходящей задачи он приведёт к высокой
    # автономии осознанно».
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Восемь вопросов — не «AI или нет», а как, где и с каким "
                   "контролем его применить",
                size=22, w=12.2, h=0.82)

    # left: 8-point checklist
    lx, lw = 0.55, 7.05
    ocean_box(s, lx, 1.52, lw, 4.40)
    checks = [
        ("Какая это фаза жизненного цикла? Она задаёт режим отказа", False),
        ("Что здесь решается детерминированно? Эту часть пишет обычный код, "
         "AI — на разбор и проверку", False),
        ("Существенная или привнесённая сложность? Существенная — решает "
         "человек, AI на периферии", False),
        ("Обратимо ли последствие? Необратимое → потолок автономии вниз, "
         "жёсткий гейт — ВЕТО-ось", True),
        ("Есть ли машинный оракул (тест, SAST, прогон)? Нет → сначала оракул, "
         "потом автономия", False),
        ("Затронуты секреты / недоверенный контент? Да → минимум прав и "
         "изоляция", False),
        ("Кто ревьюит и кто мержит? Слияние и ответственность — всегда человек",
         False),
        ("Цель — артефакт или навык? Навык → генерацию не делегировать", False),
    ]
    ci_y = 1.68
    for i, (txt, veto) in enumerate(checks):
        y = ci_y + i * 0.52
        if veto:
            filled_rect(s, lx + 0.20, y, lw - 0.40, 0.48, GOLD_TINT,
                        stroke=GOLD, stroke_pt=1.6, radius=True, radius_adj=0.08)
        icon(s, "check-check", lx + 0.28, y + 0.07, 0.32,
             "gold" if veto else "mid")
        text_box(s, x=lx + 0.70, y=y + 0.02, w=lw - 0.92, h=0.44,
                 text=f"{i+1}. {txt}", size=10.5, bold=veto,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)

    # right: Anthropic -17% chart + explanation
    rx, rw = 7.85, 4.95
    ocean_box(s, rx, 1.52, rw, 4.40)
    add_image(s, CHARTS / "c39-anthropic-quiz.png", rx + 0.14, 1.64,
              rw - 0.28, 2.02)
    text_box(s, x=rx + 0.24, y=3.74, w=rw - 0.48, h=1.52,
             text="Anthropic, Shen & Tamkin 2026 (RCT, n=52, освоение незнакомой "
                  "библиотеки) [1]: группа с AI на квизе 50% против 67% без AI "
                  "(~−17 п.п.). Кто делегировал генерацию — просел; кто спрашивал "
                  "концепции («как работает, почему») — деградации нет. Ускорение "
                  "статистически не значимо.",
             size=10.5, color=DEEP, line_spacing=1.18)
    text_box(s, x=rx + 0.24, y=5.30, w=rw - 0.48, h=0.52,
             text="Когда цель — навык, пишете вы; AI объясняет и проверяет.",
             size=11, bold=True, color=MID, line_spacing=1.10)

    gold_callout(
        s, 0.55, 6.00, 12.25, 0.86,
        "Чек-лист не решает «применять AI или нет» — он выдаёт режим: для "
        "подходящей задачи приведёт к высокой автономии, для неподходящей — "
        "опустит потолок и назовёт обязательные меры. Это распределение "
        "бремени доказательства, а не «всегда меньше AI». Необратимость и "
        "влияние — вето-ось.",
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

    # Round-6 (Block 5): the «Семинар 4 — примените чек-лист…» teal strip that
    # used to sit at y=5.58 was REMOVED — it is a cross-artifact course-scaffold
    # pointer, not student-facing material (owner note p57; same class as the
    # «mastery — Семинар 4» line deliberately kept off this slide earlier).
    # The four method-transfer steps now breathe into the freed vertical band
    # and «Вопросы?» moves up to close the slide.
    ocean_box(s, 0.45, 3.06, 6.30, 3.02)
    text_box(s, x=0.68, y=3.20, w=5.85, h=0.36,
             text="Метод переносится на все отрасли (не список инструментов):",
             size=12.5, bold=True, color=MID, line_spacing=1.0)
    steps = [
        "разложить деятельность на фазы",
        "спросить: привнесённая или существенная сложность",
        "потребовать базу для каждого числа и системный эффект",
        "отделить устойчивый паттерн от вендор-хайпа пятью вопросами",
    ]
    for i, st in enumerate(steps):
        y = 3.74 + i * 0.56
        circle(s, 0.70, y + 0.04, 0.32, TEAL)
        text_box(s, x=0.70, y=y + 0.04, w=0.32, h=0.32, text=str(i + 1),
                 size=12.5, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=1.16, y=y, w=5.45, h=0.42, text=st, size=11, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)

    text_box(s, x=0.45, y=6.36, w=6.30, h=0.7, text="Вопросы?", size=32,
             bold=True, color=DEEP)
    notes_with_sources(s, "s41")
    return s
