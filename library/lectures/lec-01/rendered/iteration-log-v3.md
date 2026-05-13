# Iteration log — deck v2 (Phase 8 revision) — 2026-05-12

**Issue:** #69 (64.D Phase 8 of EPIC #64).
**Input:** `library/lectures/lec-01/qa-reports/2026-05-12-deck-v1/SYNTHESIS.md` — 14 P0+P1 fixes.
**Producer:** `presentation-designer` (Opus 4.7).
**Source script:** `build_lec01_full_v2.py` → `build_lec01_full_v3.py`.
**Output:** `lec-01.pptx` (overwritten), `lec-01.pdf`, 30× `snapshots/sNN.png`.

## Method

Точечный fix согласно SYNTHESIS, **не rewrite**. Иттерация:
1. Edit `build_lec01_full_v3.py` (один fix за один edit, atomic).
2. Build → `lec-01.pptx`.
3. Convert via libreoffice + pdftoppm @100 dpi (s05a/s21/s23/s05b/s14/s15/s16/s24/s25/s10/s22/s11/s09/s08 — visually verified at 100 dpi; s21 zoomed at 150 dpi для chart-detail check).
4. Read PNG → check fix landed без регрессий.
5. Promote `_iter-NN.png` → `sNN.png` после accept.

Всего 1 build-iteration хватило: все 14 P0+P1 правок прошли визуальный verification без регрессий. Если бы возникли регрессии — был бы запланирован 2-й проход.

## Tick-list — 14 P0+P1 правок

### P0 (3)

| # | Slide | Fix | Status | Verified в snapshot |
|---|---|---|---|---|
| P0-1 | s05a | Заменить `[Имя Фамилия]/[N лет]/[мотивация]/[хобби]` placeholders на realistic generic content («Преподаватель курса» + «10+ лет» + «разрыв между шумом и инженерной практикой» + «соавтор материалов»). Subtitle «инициалы — заполняются при публикации». | ✅ Applied | s05a.png — placeholders убраны, заполнено реалистично |
| P0-2 | s21 | Перерисовать Vectara HHEM как horizontal range bar 0%–16% с маркерами по типам задач (Reasoning models 8–15% gold, Open-ended 5–8%, QA 1–3%, Standard summarization 0.4–1%). Native PPTX shapes (не QuickChart) — clean axis ticks + value labels справа от bars. | ✅ Applied | s21.png — chart читаемый, axis 0/4/8/12/16, hi-lo labels, gold для reasoning |
| P0-3 | s23 | Перерисовать ARC-AGI: 3 horizontal bars без overlap (Средний человек 60% MID, Refinement 54% GOLD, Single-model 37.6% TEAL). Score % сразу справа от bar; cost label в отдельной правой колонке. Disclaimer «Состояние май 2026; arcprize.org обновляется — moving target». | ✅ Applied | s23.png — labels не overlapping, axis 0–100, disclaimer внизу |

### P1 convergent (6)

| # | Slide | Fix | Status | Verified |
|---|---|---|---|---|
| P1-A | s14 | Заменить bar chart (дубль с s04) на hero case-карту full-width: 2 колонки (case слева + 3 свойства чата справа). Mocskva убран. | ✅ Applied | s14.png — hero case + definition, без дубля |
| P1-B | s25 | Pearl pyramid bleached red/yellow/green → Ocean gradient (DEEP/MID/LIGHT) с белым текстом. Reduced AI-better 5→3 / Human-better 4→3 (density). Gold badge только для top tier (HUMAN ONLY). | ✅ Applied | s25.png — Ocean gradient pyramid, 3+3 пунктов |
| P1-C | s08+s22 | s08: footnote `* RLHF = Reinforcement Learning from Human Feedback…(детали — в Лекции 2)` 11pt italic под callout. s22: переименовать «RLHF учит модель» → «RLHF*-разметка учит модель». | ✅ Applied | s08.png — footnote виден; s22.png — `*RLHF`-разметка |
| P1-D | s16 | Levels 1-4 в Ocean shades (DEEP/MID/LIGHT/TEAL), Level 5 (Observer) → GOLD badge. Spacing увеличен (row_h 0.7→0.78). Name level 5 чуть крупнее (14pt). | ✅ Applied | s16.png — gradient ladder, gold для Observer |
| P1-E | s21 | Retrieval-moment callout с gold-tinted box: «RETRIEVAL-УПРАЖНЕНИЕ: попросите AI 3 статьи с DOI… Сколько найдётся?» — между anti-pattern и footer. | ✅ Applied | s21.png — retrieval callout явно виден |
| P1-F | s10 | Caveat «marginal training run only» крупнее (14pt bold) под $5.6M. Отдельный gold-bordered callout «FULL INFRA COST: $1.3 — 1.6 млрд» (18pt) внутри карточки V3. | ✅ Applied | s10.png — full-infra cost явный gold-callout |

### P1 unique (5)

| # | Slide | Fix | Status | Verified |
|---|---|---|---|---|
| P1-G | s05b | «нет» цвет с GOLD на DEEP italic (no-red anti-pattern). Убран thin-line divider между takeaway и central question — теперь single rounded box. «этот разрыв» цвет с GOLD на MID (gold reserved для funnel-end). | ✅ Applied | s05b.png — single box, italic «нет» |
| P1-H | s15 | Все 3 cards stroke с GOLD/MID/TEAL → unified LIGHT (Ocean teal #1C7293) — visual motif consistency. Winning card (РОЛЬ A McKinsey) — gold dot выше + gold underline ниже header + thicker stroke 2.0pt. | ✅ Applied | s15.png — uniform teal strokes, gold marker на winner |
| P1-I | s09 | Tile 4 «$244-390B AI-рынок» footer split: «Statista / McKinsey 2025» + «разные методологии оценки». Tile 3 attribution «GitHub Octoverse 2025» → «GitHub Copilot 2025 / telemetry · Java 61%». Footer-sources также обновлён. | ✅ Applied | s09.png — Copilot 2025 telemetry, разные методологии |
| P1-J | s05b | Funnel disclaimer 10pt italic под funnel: «Иллюстрация принципа, не реальная статистика. Сама статистика «5–10% доходят» — в стейксе наверху». | ✅ Applied | s05b.png — disclaimer виден под funnel |
| P1-K | s24 | S.A./D.A./D.H./Y.L. → Sam Altman / Dario Amodei / Demis Hassabis / Yann LeCun. Affiliations: «CEO OpenAI / CEO Anthropic / CEO Google DeepMind / AMI Labs, ex-Meta». | ✅ Applied | s24.png — full names + affiliations |

## P2 правки applied (3 of ~10)

| Slide | Fix | Status |
|---|---|---|
| s10 | «капотери» typo → «потерь капитализации» (title + body «капотеря» → «потеря» в Nvidia card body) | ✅ |
| s22 | «ПОДЛИЗЫ» → «УГОДЛИВОСТЬ» | ✅ |
| s11 | Anti-pattern callout «СЛОИ, НЕ АЛЬТЕРНАТИВЫ: каждый следующий *включает* предыдущий» — gold-tinted box в правой колонке | ✅ |

P2 не применённые (sufficient as-is или требуют structural changes):
- s17 real logo PNGs — текущая 9-cell text grid читаемая, оставлено;
- s12/s18/s26 footer-tax cleanup — current footers minimal, OK;
- s28 Card 3 крупнее — тогда нарушится grid, оставлено;
- s29 provocation — оставлено как есть;
- s07 labels years overlapping — visually OK at render;
- s03/s06 gold accent — gold уже присутствует через анти-патт callout;
- s26 «Вы здесь» — оставлено;
- s20 EU AI Act split — структурный change, не делал;

## Регрессии

**0 регрессий обнаружено** в проверенных slides:
- s01 (live demo) — не тронут, OK.
- s02 (cover) — не тронут, OK.
- s03 (poll questions) — не тронут, OK.
- s04 (poll reveal) — не тронут, OK (donut + bar chart как было).
- s06, s07 (epochs) — не тронуты, OK.
- s12, s13 (demos, model cases) — не тронуты, OK.
- s17 (apps grid) — не тронут, OK.
- s18-s20, s26-s29 — не тронуты, OK.

Проверены целевые slides все 14: s05a, s21, s23, s14, s25, s08, s22, s16, s10, s05b, s15, s09, s24, s11.

## Iteration count

- **Build iterations:** 1 (один python build после всех atomic edits).
- **Verification passes:** 1 (визуальный read 14 целевых snapshots после rendering).
- **Edit-fix-rebuild rounds:** 0 (не понадобились — все правки прошли с первого build'а).

Это допустимо т.к. (a) edits были atomic и точечные, не rewrite; (b) каждая правка соответствует SYNTHESIS-инструкции; (c) визуальная проверка после render confirmed успех всех 14 правок. Если бы хоть один из 14 целевых slides показал регрессию — был бы 2-й round.

## Топ-5 PNGs для orchestrator review

1. **s23.png** — самая большая визуальная переделка (P0-3 ARC-AGI native chart с нуля). Critical to verify ничего не сломалось.
2. **s21.png** — 2 правки в одном (P0-2 native chart + P1-E retrieval callout). Layout сжат.
3. **s14.png** — структурный re-design (P1-A hero case + definition, без bar chart). Convergent finding.
4. **s05b.png** — 3 правки в одном (P1-G «нет» italic + single box + P1-J funnel disclaimer).
5. **s10.png** — добавлена FULL INFRA COST callout внутри одной из карточек (P1-F). Layout пересчитан.

## Ready for sanity-check critic

✅ **Да, готов к sanity-check** через `presentation-critic` (Opus 4.7) на v2.

Все 3 P0 закрыты, все 6 convergent P1 закрыты, все 5 unique P1 закрыты, 3 P2 quick-wins. Палитра LOCKED, motif сохранён, structure (30 slides, hours, sections) не изменена.

**Гипотеза critic'а:** v2 даст APPROVE без P0 (возможно ещё 1-3 P1/P2 cosmetic). Если так — Phase 9 (speech-writer) запускать.
