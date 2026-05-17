# Consistency Checker — Delta re-QA v3.1 — Лекция 4 — 2026-05-17

**Issue:** #99 · **Mode:** chapter↔slides delta (speech.md ещё не создан — Phase 9) · **Scope:** verify v3 REVISE fixes (P1 visible §/sNN/[VFY]-leak; P2 s03 chapter_ref desync) + book-first integrity + counter consistency · **Baseline:** `consistency-checker.md` (v3, VERDICT REVISE — 1 P1 / 2 P2) · **Method:** authoritative visible layer = rendered `lec-04.pptx` XML `<a:t>` runs (independent of slide-file source annotations), not slide-file `.md` raw text.

## VERDICT: **APPROVE-WITH-POLISH**

v3 P1 (visible §/sNN/[VFY]-leak) **CLOSED** на authoritative rendered layer. v3 P2-D3 (s03 chapter_ref desync) **CLOSED**. book-first **INTACT**. Strict-in counters **полностью согласованы** между 4 источниками. Остаётся 1 P2 (D2 70/80% footer-форма) — owner-tolerance, report-only, не регрессия, не блокер (как и в v3).

| Запрошенный пункт | Результат |
|---|---|
| **v3 P1 visible-leak CLOSED?** | **YES** — rendered PPTX visible-layer grep TOTAL = **0** на всех 32 слайдах (8 паттернов: §N.N / bare§ / (sNN) / →sNN / [VFY]/[VERIFY-DAY-OF]/[FACT-CHECK] / Лекции 3 §X.X / LO-код / Раздел N) |
| **s24 Body-таблица §-коды?** | **0** — col header «Точка»→«№»; ячейки = смысловые имена («почти правильный» код / merge без чтения / деструктив без гейта / уязвимый код+утечка). Rendered + slide-file оба чисты. |
| **independent grep TOTAL=0?** | **CONFIRMED** — мой независимый метод (zipfile→XML `<a:t>`-runs, не slide-file md) даёт 0 на rendered проекционном слое |
| **book-first integrity** | **YES** — `git diff ad61db5 -- chapter*.md` пусто (chapter / chapter-part2 / chapter-part3). Designer главу не трогал в v3/v3.1. |
| **s03/s04/s05 backed-by-chapter не сломано** | **YES** — s03 callout «эти три колонки — линза, как читать каждый уровень» = §0.4 (не overclaim); s24 смысловые имена = те же контролы §1.4/§2.3/§3.4–3.5/§4.4,§4.7 без искажения |
| **s29 5 осей = chapter §6.1 канон** | **YES** — Незнакомость кода·Обратимость операции·Критичность/прод·Аудит/ответственность·Цена ошибки (s29 «Аудит/ответственность» = §6.1 «Потребность в аудите/ответственности», семантически тождественно). «Повторяемость» НЕ ось — в pre-filter callout «Сначала отсев: детерминированная, проверяемая, повторяемая» = §6.1 step(1) (перенос Л3 §5.2), claim вне главы не введён |
| **s03 chapter_ref sync (D3)** | **CLOSED** — slide-file frontmatter `§0.2, §0.4 [for-slide-s03]` == deck.yaml:150 `§0.2, §0.4 [for-slide-s03]`. Остальные 31 chapter_ref не разъехались. |
| **strict-in counter консистентность** | **YES** — все 4 источника согласованы (см. ниже) |
| **terminology drift / orphan** | **0** — forbidden-англицизмы rendered = 0; canon-термины консистентны; deck = ровно s01–s32 contiguous; rendered bare-sNN refs = 0 |

## Severity counts
- **P0:** 0
- **P1:** 0 (v3 D1 CLOSED)
- **P2:** 1 (D2 70/80% footer-форма — unchanged, owner-tolerance, report-only; v3 D3 CLOSED)

## Архитектурное замечание (почему rendered, не slide-file)

Slide-file `.md` сохраняют §-refs / `(sNN)` / `[VFY]` в **author/traceability-зоне**: `*italic*` caption-строках и `[Рамка §1.1 ...]` bracket-директивах. Render-pipeline (`build_v2.py`) **резолвит их в естественный язык** для проекции — это та же exempt-логика, что frontmatter:

| Слайд | Source `.md` (author-zone) | Rendered PPTX (проекция) |
|---|---|---|
| s11 | `(callback Лекции 3 §4.3)`, `[Рамка §1.1 для C]`, `(s13)`, `(s12)` | «это вывод Лекции 3, применённый к коду»; «Рамка C: … где обязателен — на ревью pull request и merge · риск — падение надёжности на незнакомом коде» |
| s15 | `*(перенос Лекции 3 §4.5)*`, `[Рамка §1.1 для D]` | «тот же вывод, что в Лекции 3» |
| s20 | `(§2.3-деградация + FP-шум)` | «та же деградация уровня C до D плюс шум ложных тревог» |
| s23 | `Лекции 3 §4.6`, `Лекции 3 §4.7` | «урока Лекции 3»; «сбитый-с-толку посредник (confused-deputy)» |
| s25 | `§1.5; корень провалов лекции` | «инженерного паттерна; корень провалов лекции» |
| s27/s28 | `[VFY-day-of]` | «направление, не точные доли» / «(подтверждено)» |
| s30 | `(перенос Лекции 3 §5.2)` | «обычный код точен и аудируем» |

Decision #100 + v3 P1 нормируют **видимый (рендеримый) слой** — он TOTAL = 0. v3-отчёт перечислял slide-file-строки как leak, но authoritative artifact для USER GATE B = проекция (PPTX); на ней регрессия закрыта. (Метод v3.1 строже и корректнее v3: grep по rendered `<a:t>`, не по сырому md.)

## Strict-in counter consistency (4-источниковый треугольник)

| Источник | s05 | count | share | partial_out |
|---|---|---|---|---|
| `deck.yaml:186` | `in_bucket: true` | — | — | — |
| `deck-part2.yaml` ai_failure_judgment | в `in_bucket_slides` | `count: 15` | «15/32 ≈ 47% / 54.5% мин (42/77)» | 17 слайдов, **без s05** |
| `plan-v2-final.md` §5 | «s05 strict-in [Решение #100 ЗАКРЫТО]» | «15/32» | «46.9% слайдов / 54.5% мин (42/77)» | s05 НЕ в partial→out |
| methodology-critic v3 re-QA (цит. в plan §5 + deck-part2) | judgment-якорь | 15/32 | 46.9% / 54.5% мин | — |

Арифметика: 15 in_bucket + 17 partial_out = 32 ✓ · 15/32 = 46.875% → «47%» (deck) / «46.9%» (plan) согласованное округление ✓ · 54.5% мин (42/77) идентично в deck-part2 + plan ✓. **Все 4 согласованы, рассинхрона нет.**

## Cross-artifact matrix (delta-focus)

| Концепт / число | Chapter (канон) | Slide (v3.1 rendered) | Aligned? |
|---|---|---|---|
| s24 4 точки→контроль (смысловые имена, не §) | §4.8/§6.5 [for-s24]; контроли §1.4/§2.3/§3.4–3.5/§4.4,§4.7 | s24 «№\|риск\|контроль»: ревью+тест / ревью+CI-gate / hard-gate / SAST+least-priv | ✓ имена↔контроли тождественны, 0 §-кодов |
| s29 5 осей выбора | §6.1 (5 осей verbatim) | s29: Незнакомость·Обратимость·Критичность/прод·Аудит/ответств.·Цена ошибки | ✓ канон, 5 осей ровно |
| s29 pre-filter «не AI вовсе» | §6.1 step(1) «детерминированная+верифицируемая → обычный код» (перенос Л3 §5.2) | s29 callout «Сначала отсев: детерминированная, проверяемая, повторяемая → обычный код, без AI» | ✓ «повторяемость» = свойство pre-filter, не 6-я ось; claim вне главы не введён |
| s03 chapter_ref | §0.2 (Л3-перенос) + §0.4 (A/B/C/D) | deck.yaml `§0.2,§0.4` == slide-file fm `§0.2,§0.4` | ✓ D3 closed |
| s05 in_bucket / judgment-якорь | §1.1 line 159 control-gradient + §3.4 | s05 «цена ошибки растёт A→D» (rendered, 0 meta/§) | ✓ strict-in, backed, counter-consistent |
| 70/80%-проблема | §1.4 (Osmani 2024→2025 эволюция документирована) | s08 плашка = canon `70/80%-проблема`; footer = `Osmani (70%-проблема, 2024)` | ✓ historic-correct (D2 P2) |

## DISCREPANCIES

### D2 — Form-variants «70/80%-проблема» footer (UNCHANGED from v3)
**Severity:** P2 (report-only, owner-tolerance, не регрессия, не блокер)
**Where:** rendered s08 — главная плашка = canon `70/80%-проблема` ✓; footer source-атрибуция = `Osmani (70%-проблема, 2024)`.
**Issue:** Footer сохраняет историческое имя термина (Osmani назвал «70% problem» 2024, обновил до «80%» 2025; chapter §1.4 документирует явно). Видимый главный слой использует canon. Атрибуция источника легитимно сохраняет историческое имя — не drift в строгом смысле.
**Recommendation:** Report-only. Опционально: footer → «Osmani, 2024» без формы термина. Не блокер для USER GATE B.

## Coverage gaps
Нет. v3 «что CLEAN» (Раздел-0 backed, 5 точек возврата §0.3, terminology vs glossary lock, orphan=0, citation regression=0) не регрессировало. Все 32 chapter_ref резолвятся; deck = s01–s32 contiguous; rendered orphan sNN = 0.

## Что CLEAN (не фиксить)
- **v3 P1 (D1) CLOSED:** rendered visible-layer §/sNN/[VFY]/чужие-Л3-§/LO-код TOTAL = 0 на всех 32 слайдах (8-паттерновый независимый grep по PPTX `<a:t>`).
- **v3 P2 (D3) CLOSED:** s03 chapter_ref slide-file fm синхронизирован с deck.yaml (`§0.2, §0.4 [for-slide-s03]`).
- **book-first INTACT:** chapter*.md byte-identical ad61db5.
- **s24 Body-таблица:** col «№», смысловые имена контролей — 0 §-кодов в видимых ячейках (приоритетный риск v3 — устранён).
- **s29:** 5 канонических осей §6.1; «повторяемость» корректно перемещена в pre-filter callout (§6.1 step1, перенос Л3 §5.2), не введена как ось, claim вне главы отсутствует.
- **Strict-in counters:** deck.yaml s05:true ↔ deck-part2 count15 ↔ plan §5 ↔ methodology-critic v3 — арифметически и текстуально согласованы.
- **Terminology:** forbidden-англицизмы rendered = 0; canon-термины («почти правильный» код / perception-gap / кодинг-агент / vibe-coding / slopsquatting) консистентны.

## Топ-фиксов (per artifact)
- **Chapter:** ничего (book-first, source of truth верен, 0 P0).
- **Slides:** ничего блокирующего. [P2 report-only, опц.] D2 70/80% footer-форма — owner-tolerance.
- **Speech:** N/A (Phase 9, ещё не создан).

## Re-QA gate
v3 P1+P2-D3 закрыты, book-first цел, counters согласованы → consistency не требует ещё одного раунда. Перед USER GATE B: pre-gate mode=slides (визуальный sweep PNG + notes-read) — standard, не из-за consistency. После Phase 9 (speech) — full 3-артефактный consistency pass.
