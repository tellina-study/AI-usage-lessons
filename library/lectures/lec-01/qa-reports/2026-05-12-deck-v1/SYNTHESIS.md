# SYNTHESIS — deck v1 (30 slides) Phase 7 — 2026-05-12

**Issue:** #69 (64.D Phase 7 of EPIC #64).
**Артефакт:** `library/lectures/lec-01/rendered/lec-01.pptx` (30 slides, после Phase 6.5 microfix).
**4 критика:** presentation-critic + student-simulator + reader-simulator(rendered) + fact-checker (все Opus 4.7).

## Общий verdict

**APPROVE-WITH-MINOR-FIXES.** Deck v1 — методически и фактически крепкий, все 4 критика положительные. Пилот #55 v3.6 знания применены (palette, motif, typography). **3 P0 блокеров** требуют immediate fix перед показом аудитории.

| Critic | P0 | P1 | P2 | Verdict |
|---|---|---|---|---|
| presentation-critic | **3** | 11 | 14 | APPROVE-WITH-MINOR-FIXES |
| student-simulator | 0 | 5 | — | **«ЗАШЛО»** |
| reader-rendered | 0 | 5 | — | 22/29 self-contained |
| fact-checker | **0** | 3 | 3 | APPROVE-WITH-MINOR-FIXES |
| **После дедупликации** | **3** | **~14** | ~17 | — |

## Convergent findings (≥2 критика согласны)

### КОНВЕРГЕНЦИЯ A — s14 ↔ s04 повтор bar chart (P1)
- **student** (P1): «полез в tg, проверил мессенджер. Самое важное findings — дубль убивает внимание.»
- **presentation-critic** (P2): bar chart «LLM в РФ — multi-select» — отображён, но при повторе — overload.
- **Fix:** на s14 заменить bar chart на **что-то другое** (например, кейс-карточка про разбор нормативного документа крупно + retry icon — потеря дублирования).

### КОНВЕРГЕНЦИЯ B — s25 Pearl + AI/Human density (P1)
- **student** (P1): «слишком плотно. К 50 минуте лекции — много. Полез второй раз в телефон.»
- **presentation-critic** (P1): bleached red/yellow/green pyramid — palette violation. Density — 2 columns + pyramid.
- **Fix:** разбить s25 на 2 слайда ИЛИ использовать Ocean gradient (deep/mid/light) для pyramid + сократить columns.

### КОНВЕРГЕНЦИЯ C — RLHF unexplained on slides (P1)
- **student** (P1 quest): «Что такое RLHF реально на пальцах?»
- **reader** (P1): «расшифровать RLHF прямо на slide (s08/s22) — используется дважды без определения».
- **Fix:** add inline footnote definition «RLHF = Reinforcement Learning from Human Feedback» при первом упоминании на s08.

### КОНВЕРГЕНЦИЯ D — s16 5 levels of autonomy density (P1)
- **student** (P1): «Collaborator/Consultant/Approver проскочили».
- **presentation-critic** (P1): «autonomy ladder — все 5 одинаковы. Уровень 5 (Observer) должен быть gold.»
- **Fix:** Уровень 5 gold + остальные 4 Ocean shades; spacing увеличить.

### КОНВЕРГЕНЦИЯ E — LO7 weak coverage (P1)
- **presentation-critic**: «LO7 покрыт только s19, s21».
- **reader** (P1 implicit): self-study fallback для s21 retrieval упражнение нужен.
- **Fix:** добавить retrieval moment на s21 (declared в deck.yaml как retrieval_moment, но не виден).

### КОНВЕРГЕНЦИЯ F — s10 marginal vs full infra caveat (P1)
- **reader** (P1): «caveat marginal vs full infra cost утоплен мелким шрифтом, через 2 недели забывается».
- **student** (positive): «препод подчеркнул, и я бы это пропустил». Подтверждение.
- **Fix:** увеличить caveat «marginal $5.6M / full $1.3-1.6B» visual weight.

## Уникальные P0 (от presentation-critic)

### P0-1 — s05a UNFILLED PLACEHOLDERS
Слайд содержит литералы `[Имя Фамилия]`, `[N лет]`, `[мотивация]`, `[хобби]`, инициалы «КМ». **Нельзя показывать.** Либо заполнить, либо удалить из показа (speech-only intro).

### P0-2 — s21 Vectara HHEM chart broken
2 длинные tealOcean бары + крошечный gold — нет axis labels, нет числовых значений, нет шкалы. Должен быть horizontal range bar 0%-15% с маркерами по типам задач.

### P0-3 — s23 ARC-AGI bar chart labels overlapping
Labels ($30/задачу, $2.20/задачу, $50–150/час) overlapping. Имена бенчмарков не закреплены под bars. Слайд непригоден.

## Уникальные P1 (от presentation-critic — выборка)

- **s05b** красный «нет» в central question — anti-pattern #2 (без красного).
- **s15** черные strokes у cards вместо teal `#1C7293` (visual motif violation).
- **s25** Pearl pyramid bleached red/yellow/green вместо Ocean gradient.
- **s01** левая колонка пустая — hero metric «31 fps» нужен gold callout.
- **s08** assertion 2 строки с rocky wrap «архитектура.» отдельной строкой.
- **s11** assertion 2 строки rocky.
- **s14** assertion слишком длинный (3 строки).
- **s09** «$244-390B» подпись три уровня в одной строке.
- **s04** donut и bar chart разной visual mass.

## Уникальные P1 (от reader-rendered)

- **s11** добавить anti-pattern callout «слои, не альтернативы».
- **s24** заменить инициалы (S.A./D.A./D.H./Y.L.) на полные имена.
- **Notes** для s01, s12, s21 — добавить self-study fallback блоки.

## Уникальные P1 (от fact-checker)

- **s05b funnel** «100 → 10» добавить disclaimer «*illustration of principle, not real numbers*» или заменить на «100% → 10%».
- **s09** атрибуция «GitHub Octoverse 2025» mismatched (Octoverse 2025 headline TypeScript, не 46% Copilot). Reword to «GitHub Copilot 2025 (telemetry data)».
- **s23** ARC-AGI numbers moving target (по состоянию мая 2026 GPT-5.5 85%) — добавить disclaimer «*state May 2026; arcprize.org updates*».

## Сильные стороны (что НЕ менять)

✅ **Phase 6.5 microfixes confirmed by critics:** s18 ПРИЛОЖЕНИЕ wrap fixed, s22 sycophancy dates 25/28/29 апр correct, s04 datalabels восстановлены.
✅ **Все критические факты verified** (fact-checker через WebSearch — ВЦИОМ, Stack Overflow, DeepSeek timeline, Feng/McDonald/Zhang, Vectara HHEM, Translate, GPT-4o sycophancy, ResNet, Hassabis Nobel — все точно).
✅ **«ЗАШЛО»** общая оценка студента — лучшая первая лекция.
✅ **22/29 self-contained** для self-study.
✅ **0 mentions ИУ6** — universal tone выдержан.
✅ **Layered model s11**, **worked example s18 связь с chapter §3.8**, **callback s27 → s01** — методические gems.
✅ **Pacing** 75 мин с buffer 8.5 мин — реалистично.

## Топ-N правок для Phase 8 revision (приоритезированно)

### P0 (3 — обязательно)
1. **s05a** — заполнить placeholders ИЛИ удалить из показа (speech-only).
2. **s21** — перерисовать Vectara HHEM как horizontal range bar с маркерами задач.
3. **s23** — перерисовать ARC-AGI с labels под bars + цены не overlapping + disclaimer «state May 2026».

### P1 — convergent (6, в приоритете «оба критика согласны»)
4. **s14** — заменить дубль bar chart с s04 на нечто другое (kase-карта крупно).
5. **s25** — разбить на 2 slide ИЛИ Pearl pyramid → Ocean gradient (deep/mid/light) + сократить.
6. **s08 + s22** — RLHF inline footnote definition при первом упоминании.
7. **s16** — Уровень 5 gold + spacing.
8. **s21** — retrieval moment visible на slide (declared в deck.yaml).
9. **s10** — caveat «marginal $5.6M / full $1.3-1.6B» visual weight.

### P1 — unique critical (5)
10. **s05b** — красный «нет» → gold; central question box (1 rounded box).
11. **s15** — черные strokes → Ocean teal; gold underline у winning card.
12. **s09** — split «$244-390B AI-рынок» подпись + Octoverse → Copilot 2025 telemetry.
13. **s05b funnel** — disclaimer «illustration» или «100% → 10%».
14. **s24** — полные имена лидеров (Altman/Amodei/Hassabis/LeCun) вместо инициалов.

### P2 (множество — на усмотрение book-editor / designer inline)
- s17 real logos / 6-cell grid.
- s10 «капотери» typo.
- s22 «ПОДЛИЗЫ» → «УГОДЛИВОСТЬ».
- s12/s18/s26 footer-tax cleanup (anti-pattern #14).
- s28 Card 3 крупнее.
- s29 provocation как assertion на slide.
- s07 labels years overlapping (2012/2017).
- s03/s06/s15 gold accent ≥1×/slide.
- s26 «Вы здесь» в Блок 1.
- s11 anti-pattern callout «слои, не альтернативы».
- s20 EU AI Act + breakeven split.
- s23 disclaimer «moving target».
- + ещё ~5 P2 от critics.

## Recommendation orchestrator'у

✅ **USER GATE 2: APPROVE-WITH-FIXES** — 3 P0 + 6 convergent P1 + 5 unique P1 = 14 правок до финала. P2 на усмотрение.

**Phase 8 plan:**
1. Спавнить `presentation-designer` (Opus 4.7) с топ-14 правок выше → deck v2.
2. Optional: 1 sanity-check critic на v2 (presentation-critic recommended).
3. USER GATE 2 final → Phase 9 (speech-writer).

**Альтернатива (быстрее):** разделить scope на 2 итерации:
- (a) v1.5 — только 3 P0 + 6 convergent P1 (~9 правок, ~30-45 мин designer).
- (b) v2 — все 14 + P2 (~1.5-2 часа designer).
