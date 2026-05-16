VERDICT: APPROVE-WITH-POLISH

# Fact-Checker Report — Лекция 3 «Архитектуры AI-систем», slides (Phase 7 / build-deck Phase 4) — 2026-05-16

**Скоуп:** данные на видимом слое слайдов (`slides/sNN-*.md` + `rendered/snapshots/sNN.png`) + 5 чартов (`rendered/assets/charts/`). База истины — верифицированная глава v1.1 (`chapter.md` + `chapter-part2.md` + `chapter-part3.md`) + `notes/research/lecture-3/{failures-and-limitations,trends-2026,sources}.md`. Live-проверка: WebSearch (Air Canada CRT, MCP timeline).

## Severity counts
- **P0 (неверно / непроверено на видимом слое / direction inversion):** 0
- **P1 (нужна метка / формулировка / illustrative-маркировка):** 2
- **P2 (косметика, форматирование):** 2

Глава v1.1 уже верифицирована; цифры/даты на видимом слое **сходятся с главой**, новых непроверенных чисел слайды НЕ ввели, арифметика на чартах верна, volatile-числа корректно убраны с видимого слоя или помечены «перепроверить ко дню лекции».

---

## Таблица: число / факт на слайде → проверка

| Число / факт | Slide / chart | == глава? | Verdict | Fix |
|---|---|---|---|---|
| Faithfulness Claude 3.7 ~25% | s07 / c07-faithfulness.png | ✓ chapter.md:157 «~25%» дословно; `[VFY quarterly]` | VERIFIED | — |
| Faithfulness DeepSeek R1 ~39% | s07 / c07-faithfulness.png | ✓ chapter.md:157 «~39%» дословно | VERIFIED | — |
| Тильда «~» + footer «Anthropic апр-2025, freshness quarterly, перепроверить ко дню лекции» | s07 visible + c07 | ✓ соответствует `[VFY: CoT 25/39%]` в главе | VERIFIED | — |
| c07 chart: бары 25% / 39%, ось 0–100% | c07-faithfulness.png | ✓ высота баров пропорциональна (25 / 39), без ложной точности | VERIFIED | — |
| Context rot: «точность извлечения ↓ по росту токенов» (видимый текст слайда) | s08 visible body | ✓ chapter.md:171 качественно, без чисел | VERIFIED | — |
| c08 chart: 8k/32k/64k/128k/256k/512k → 97/93/86/76/63/48% | c08-context-rot.png (embedded в s08) | ⚠ глава НЕ даёт эти точечные числа (только «падает»; источник Chroma 2025 — у Chroma свои датасеты, не эти 6 точек) | NEEDS-LABEL | **P1-1** — добавить «схематично / illustrative» к подписи кривой ИЛИ убрать ось-метки токенов; форма (монотонный спад) верна, конкретные % не из главы и не из named-источника |
| Reliability compounding: 5×99% → 0.99⁵ ≈ 95% | s23 visible + c23-compounding.png | ✓ chapter-part3:49,274 «0.99⁵ ≈ 95%» дословно | VERIFIED | — |
| 10 шагов → ≈ 90% | s23 + c23 | ✓ chapter-part3:274 «0.99¹⁰ ≈ 0.904» | VERIFIED | — |
| 20 шагов → ≈ 82% | s23 + c23 | ✓ chapter-part3:274 «n=20 → ≈ 0.818» | VERIFIED | — |
| c23 chart арифметика: точки 1→99%, 5→95%, 10→90%, 15→86%, 20→82% | c23-compounding.png | ✓ 0.99⁵=95.1%, 0.99¹⁰=90.4%, 0.99¹⁵=86.0%, 0.99²⁰=81.8% — все округления корректны | VERIFIED | — |
| $4,200 за 63 часа петля | s23 visible (gold) | ✓ chapter-part3:46 «$4,200 за 63 часа»; footer «single-author постмортем 2026-04, illustrative, числа округлены» | VERIFIED | — |
| Catastrophic forgetting: «цель ↑, общие способности ↓» | s16 + c16-forgetting.png | ✓ chapter-part2:79–82, направление верно | VERIFIED | — |
| «тяжелее с ростом масштаба» | s16 visible (sub-line) | ✓ chapter-part2:82 «с ростом масштаба модели тяжесть забывания возрастает» (Luo et al. arXiv:2308.08747, 2023) | VERIFIED | — |
| c16 chart: цель 55→97, общие 90→42 по 5 эпохам | c16-forgetting.png (embedded s16) | ⚠ конкретные значения — иллюстративные (Luo et al. — эффект, не эти числа); footer s16 пишет «Эмпирически наблюдается… (preprint)» но кривая выглядит как точные данные | NEEDS-LABEL | **P1-2** — добавить «схематично / иллюстрация эффекта» к заголовку чарта c16 (направление и расхождение верны, абсолютные числа не из источника) |
| MIT NANDA ~95% пилотов без ROI | s29 + c29-nanda.png | ✓ chapter-part3:257,276 «~95%», подаётся как заголовок отчёта | VERIFIED | — |
| `[VFY]`-эквивалент на s29 | s29 footer | ✓ «MIT NANDA, State of AI in Business 2025 — отчёт с методологией (150 интервью + 350 опрос + 300 внедрений), не универсальный закон» — точно соответствует `[FACT-CHECK]`-ноте главы (part3:276) | VERIFIED | — |
| c29 donut: 95 / 5, тильда «~95%» на слайде | c29-nanda.png | ✓ 95+5=100, framing «~» + «не закон» присутствует | VERIFIED | — |
| Air Canada / Moffatt, трибунал, 14.02.2024 | s01 visible + s13 | ✓ chapter.md:89 «14 февраля 2024»; **WebSearch: 2024 BCCRT 149, решение 14.02.2024** | VERIFIED (live) | — |
| «купи по полной, возврат в течение 90 дней» | s01 visible | ✓ chapter.md:89 «в течение 90 дней» | VERIFIED | — |
| MCP timeline: Anthropic 11/2024 → OpenAI 03/2025 → Google 04/2025 → независимый фонд | s20 visible | ✓ chapter-part2:194 + research Q4; **WebSearch: Anthropic ноя-2024, OpenAI март-2025, → Agentic AI Foundation/Linux Foundation** | VERIFIED (live) | — |
| MCP N×M → N+M, «USB-C для инструментов» | s20 visible | ✓ chapter-part2:191 дословно | VERIFIED | — |
| Footer s20 «принятие/масштаб экосистемы MCP — перепроверить ко дню лекции» | s20 footer | ✓ соответствует `[VFY quarterly]` главы | VERIFIED | — |
| CoT-пример: 23−7=16; 2×6=12; 16+12=28 | s06 visible | ✓ chapter.md:144 дословно; арифметика 16+12=28 верна | VERIFIED | — |
| «~200k токенов» (когда НЕ RAG) | s12, s28 visible | ✓ chapter.md:284 «менее ~200k токенов» — ориентир, с «~» | VERIFIED | — |
| Worked example «2000 регламентов еженедельно», «~150 FAQ раз в квартал» | s28 visible | ✓ chapter-part3:284 worked examples | VERIFIED | — |
| CVE-номера / vendor-pricing на видимом слое | s24, s25 | ✓ ОТСУТСТВУЮТ — оба слайда явно «CVE-хронология — в главе/notes, не на видимом слое» | VERIFIED (compliant plan §7/§9) | — |
| Volatile (caching %, MCP adoption числа) на видимом как незыблемые | весь deck | ✓ не найдено; MCP-числа — даты-вехи (стабильны) + footer «перепроверить» | VERIFIED (compliant plan §7/§9) | — |

---

## Verified facts (sample) — 27 проверенных пунктов
- ✓ s07/c07: Claude 3.7 ~25%, DeepSeek R1 ~39% — chapter.md:157, Anthropic *Reasoning Models Don't Always Say What They Think* (апр-2025), тильда + freshness-caveat присутствуют.
- ✓ s23/c23: reliability compounding — арифметика на чарте безупречна (0.99⁵=95.1%, 0.99¹⁰=90.4%, 0.99¹⁵=86.0%, 0.99²⁰=81.8%, все округления корректны), == chapter-part3:274.
- ✓ s01/s13: Air Canada 14.02.2024 — live-verified (2024 BCCRT 149, BC Civil Resolution Tribunal), == chapter.md:89.
- ✓ s20: MCP timeline — live-verified (Anthropic ноя-2024 / OpenAI март-2025 / Google апр-2025 / Linux Foundation), == chapter-part2:194.
- ✓ s06: CoT-арифметика 16+12=28 — == chapter.md:144 дословно.
- ✓ s29/c29: NANDA ~95% — подан как «отчёт с методологией, не закон», тильда присутствует, == chapter-part3:276 `[FACT-CHECK]`.
- ✓ s25/s24: 0 CVE-номеров и vendor-pricing на видимом слое — соответствует plan §7/§9.
- ✓ Direction-of-claim: faithfulness падает на трудных задачах ✓; context rot — точность падает с длиной ✓; forgetting — общие способности падают, цель растёт ✓; compounding — надёжность падает с числом шагов ✓. **Инверсий направления НЕ обнаружено.**

## DISPUTED / FALSE facts
**Нет.** P0 = 0. Все числа/даты на видимом слое сходятся с верифицированной главой и/или подтверждены live-поиском. Slides не ввели ни одного непроверенного числа.

## NEEDS-LABEL (P1 — illustrative-маркировка чартов)

### P1-1 — c08-context-rot.png: точечные % не из named-источника
**Что:** чарт показывает конкретные точки 97/93/86/76/63/48% при 8k/32k/64k/128k/256k/512k.
**Issue:** глава §1.4 (chapter.md:171) описывает context rot **только качественно** («точность падает по мере роста токенов»), источник Chroma Research 2025 не привязан к этим 6 точкам — это **схематичная иллюстрация формы**, не данные из исследования. Сама форма (монотонный спад) и направление верны. Риск — студент примет «48% на 512k» за измеренный факт.
**Fix:** подпись кривой на c08 / в s08 visible — добавить «схематично» или «иллюстрация эффекта (форма, не точные значения)»; альтернатива — убрать числовые ось-метки токенов, оставить «больше токенов →». Footer s08 источник Chroma не упоминает — добавить «(эффект — Chroma Research 2025; кривая схематична)».
**Severity:** P1.

### P1-2 — c16-forgetting.png: абсолютные значения иллюстративны
**Что:** чарт показывает цель 55→97 и общие способности 90→42 по 5 эпохам.
**Issue:** Luo et al. (arXiv:2308.08747, 2023) документирует **эффект** (узкий FT ухудшает общие способности, тяжелее с масштабом), не эти конкретные кривые. Footer s16 говорит «Эмпирически наблюдается при continual fine-tuning (Luo et al. 2023)», но визуально кривая выглядит как точные измеренные данные. Направление и расхождение (diverging) — верны и соответствуют главе.
**Fix:** добавить к заголовку c16 / подписи «схематично — иллюстрация эффекта, не данные конкретного исследования». Footer уже близок, но «эмпирически наблюдается» рядом с точной кривой создаёт ложную точность — развести явно.
**Severity:** P1.

## UNVERIFIABLE
**Нет.** Все факты либо подтверждены главой v1.1 (уже верифицированной), либо live-проверены WebSearch. `[VFY quarterly]`-метки на s07/s20 (faithfulness, MCP adoption) корректно перенесены на видимый слой как «перепроверить ко дню лекции» — это не UNVERIFIABLE, это правильная freshness-дисциплина.

## Freshness Pre-Flight (видимый слой)
| Факт | Slide | Cadence | Источник | На видимом «незыблемо»? | Flag day-of |
|---|---|---|---|---|---|
| Faithfulness 25/39% | s07/c07 | quarterly | Anthropic апр-2025 | нет — «~» + footer-caveat | да (уже на слайде) |
| MCP adoption/масштаб | s20 | quarterly | research Q4 | нет — даты-вехи стабильны + footer-caveat | да (footer уже) |
| NANDA ~95% | s29/c29 | yearly+ (report) | MIT NANDA 2025-08 | нет — «отчёт, не закон» | нет (report-headline) |
| $4,200 петля | s23 | single-source | Sattyam Jain 2026-04 | нет — «illustrative» в footer | нет (помечено) |
| Compounding 95/90/82% | s23/c23 | conceptual (математика) | вывод pⁿ | да — но это **математика**, не volatile | нет (закон арифметики) |

Volatile-числа на видимом слое как незыблемые — **не обнаружено**. Freshness-дисциплина соблюдена (тильды + footer-caveats).

## Топ-правок до публикации (приоритет)
1. **P1-1** — c08 / s08: пометить кривую context-rot «схематично / иллюстрация формы»; добавить атрибуцию эффекта (Chroma Research 2025) в footer; либо убрать числовые токен-метки оси.
2. **P1-2** — c16 / s16: пометить кривую catastrophic forgetting «схематично — иллюстрация эффекта, не данные исследования»; развести «эмпирически наблюдается (Luo et al.)» и точную кривую.
3. **P2** (косметика, опционально) — c08 footer на самом чарте источник не подписан (s08 visible footer тоже без Chroma) — единообразить с другими чартами, где источник в footer.
4. **P2** (косметика) — c29-nanda.png: donut без подписи единиц (только «95»/«5»); слайд s29 footer компенсирует — допустимо, но можно добавить «%» на сам donut для autonomy чарта.

---

**Итог:** verdict **APPROVE-WITH-POLISH** — 0 P0, 2 P1 (≤4 → show-able с known caveats). Все числа/даты на видимом слое верны и сходятся с верифицированной главой; арифметика на c07/c23 безупречна; направления claim'ов корректны; CVE/vendor-pricing/volatile-числа корректно убраны с видимого слоя. Два P1 — это illustrative-маркировка двух схематичных чартов (c08, c16), где форма/направление верны, но абсолютные точки не из named-источника и могут быть прочитаны как измеренный факт. Это polish, не структурный gap.
