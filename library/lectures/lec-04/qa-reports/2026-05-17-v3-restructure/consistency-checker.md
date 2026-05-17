# Consistency Checker Report — Лекция 4 — 2026-05-17 (v3 Раздел-0 restructure)

**Issue:** #99 · **Mode:** chapter↔slides (speech.md ещё не создан — Phase 9) · **Scope:** Раздел-0 перестройка s03/s04/s05(+s06/s07), Решение #100 · **Baseline:** 2026-05-16-v1 SYNTHESIS (consistency был APPROVE-WITH-POLISH, 0 drift / 0 orphan / citation CLEAN; P1 = visible §-leak slide-side, должен уйти в v3).

## VERDICT: **REVISE**

Не из-за самой Раздел-0 перестройки (она CLEAN — см. ниже), а из-за **P1 visible §/sNN-leak регрессии, которая по SYNTHESIS должна была уйти в v1→v3**, но сохранилась на ~11 слайдах вне scope перестройки. Решение #100 Deck-wide tone-принцип («на видимом слое 0 §-кодов / (sNN)») нарушен на видимом (рендеримом) слое — это структурный gap, не polish.

| Запрошенный пункт | Результат |
|---|---|
| **book-first integrity** (chapter*.md == ad61db5) | **YES** — `git diff ad61db5 -- chapter*.md` пусто. Designer главу не трогал. |
| **s03 backed-by-chapter** | **YES** — §0.2+§0.4 (определения A/B/C/D дословно §0.4; Л3-связь дословно §0.2). 0 новых утверждений. |
| **s04 backed-by-chapter** | **YES** — §0.3 (ЦВ verbatim; рамка ответа «не хорош/плох, а уровень+конфиг+точка» дословно §0.3; 5 якорей = 5 точек возврата §0.3). |
| **s05 backed-by-chapter** | **YES** — §1.1 line 159 явно даёт control-gradient (A=каждый токен → D=только вход/выход); «радиус/цена/9 секунд» backed chapter-part2 §3.4. Легитимный синтез §1.1+forward-pointer, 0 overclaim. |
| **chapter_ref корректность (32)** | **38/38 §-заголовков резолвятся.** 0 broken/orphan chapter_ref. НО s03 deck.yaml↔slide-file рассинхрон (P2, D3). |
| **terminology vs glossary lock** | **CLEAN** — автокомплит=0, кодинг-агент 34/0, 70/80%-проблема visible-form MATCH, forbidden-англицизмы=0. |
| **5 точек возврата ЦВ** | **CLEAN** — s08/s13/s17/s21+s23/s26 = §1.4/§2.3/§3.5/§4.4+§4.7/§5.2, точно по plan §2.1 fixed + chapter §0.3. |
| **orphan / dangling после слот-реюза s05** | **0** — старая «4-вопроса рамка» не висит orphan; корректно живёт в §1.1→s11/s15/s03-notes. |
| **citation regression** | **0** — числа/источники не тронуты (designer заявил, подтверждено grep). |

## Severity counts
- **P0:** 0
- **P1:** 1 (D1 — visible §/sNN-leak регрессия, вне scope перестройки, но на текущем артефакте)
- **P2:** 2 (D2 — 70/80% form-variants в footer/notes; D3 — s03 deck.yaml↔slide-file chapter_ref рассинхрон)

## Cross-artifact matrix (Раздел-0 restructure focus)

| Концепт / утверждение | Chapter (source of truth) | Slide (v3) | Backed? |
|---|---|---|---|
| Определения A/B/C/D (что делает AI / кто решает / пример) | §0.4 (4 буллета verbatim) | s03 таблица 3 кол. + gold-линза | ✓ дословно |
| Л3-связь «лестница сложности → A→D, ступень под задачу» | §0.2 `[for-slide-s03]` + §0.4 disclaimer | s03 подзаголовок «как лестница сложности из Л3 — ступень под задачу» | ✓ |
| course-scaffold атрибуция (не на видимом слое) | §0.4 disclaimer | s03 — ТОЛЬКО speaker notes (видимый слой чист) | ✓ Решение #100 соблюдён |
| 4-я ось (риск/где человек) отложена | §0.4 / §1.1 | s03 — 3 колонки, 4-я в notes «проявится в Р1–4» | ✓ соответствует plan |
| Центральный вопрос (текст) | §0.3 blockquote | s04 gold-box verbatim | ✓ |
| Рамка ответа «уровень+конфиг+точка» | §0.3 | s04 teal callout дословно | ✓ |
| 5 якорей «где человек обязателен» | §0.3 (5 точек: §1.4/§2.3/§3.5/§4.4+§4.7/§5.2) | s04 именами: почти правильный · merge/ревью · деструктив prod · безопасность · что строить | ✓ имена↔§ соответствуют |
| s05 «цена/радиус ошибки растёт A→D» | §1.1 line 159 (control gradient) + §3.4 (9 сек/необратимое) | s05 title+таблица+gold | ✓ синтез, не overclaim |
| s05 «A=каждый Tab, D=только вход/выход» | §1.1 «A на каждом токене; D только вход (постановка) и выход (merge/прод)» | s05 таблица «Человек контролирует» | ✓ дословно |
| Уровень A: +56% лаб / +7–22% поле / −19% легаси | §1.2 `[for-slide-s06]` | s06 3 контекста + footer | ✓ числа идентичны |
| Граница A↔B «ревью после, не во время» | §1.3 `[for-slide-s07]` | s07 2-кол. таблица + gold | ✓ дословно |

## DISCREPANCIES

### D1 — Visible §/sNN-leak регрессия (вне scope перестройки, но на текущем артефакте)
**Severity:** P1
**Where:** Видимый Body/footer ~11 слайдов: s11 (`рамка §1.1`, `(s13)`, `(s12)`), s12 (`[VFY-day-of]` footer), s15 (`рамка §1.1`, `Лекции 3 §4.5`), s20 (`§2.3`), s21 (`[VFY]` footer), s22 (`[VFY]` footer), s23 (`Лекции 3 §4.6`, `Лекции 3 §4.7`), **s24 (Body-таблица колонка «Точка»: `(§1.4)`, `(§2.3)`, `(§3.4–§3.5)`, `(§4.4, §4.7)`)**, s25 (`§1.5`), s27 (`[VFY-day-of]` footer), s28 (`[VFY-day-of]` footer), s30 (`Лекции 3 §5.2`).
**Issue:** SYNTHESIS 2026-05-16 предписал v1→v3: «Strip ВСЕХ `[VFY]` с видимого слоя» (P0) + «Strip visible §-номера / (sNN) / §-refs чужих лекций из Body+Footer ~16 слайдов» (P1). На текущем артефакте это **не выполнено** для перечисленных слайдов. Решение #100 Deck-wide tone-принцип (ENFORCED, все 32 слайда): «на видимом слое **0**: §-кодов / (sNN) / ссылок-кодов на чужие лекции». s24 — самый серьёзный: §-коды в **видимой Body-таблице** (рендерится на проекцию, не footer), как `**1** (§1.4)`. Раздел-0 (s03/s04/s05/s06/s07) — **чисто** (grep visible-layer = 0); проблема в s11–s30. Это рецидив Л2-R1 P0 / anti-patterns #36–#39.
**Recommendation:** **Slides** (главу НЕ трогать — book-first, chapter верен). Designer revision: убрать с видимого Body/footer все `§N.N`, `(sNN)`, `[VFY*]`, `Лекции 3 §X.X` на s11/s12/s15/s20/s21/s22/s23/s24/s25/s27/s28/s30. Замена: s24-колонка «Точка» → содержательные имена («почти правильный код» / «merge без чтения» / «деструктив на prod» / «уязвимость+утечка»), как на s04; §-refs чужих лекций → «как в Лекции 3»; (sNN) → «далее» / «разберём следующим»; `[VFY*]` → только speaker notes. Speaker notes регистр уже чист — зеркалить.

### D2 — Form-variants «70/80%-проблема» (footer/notes)
**Severity:** P2
**Where:** glossary canon = `70/80%-проблема`. Visible s08 Body (line 7) = `70/80%-проблема` ✓ MATCH. Variant `70%-проблема` ×3 / `80%-проблема` ×1 — в footer-цитате s08 («Osmani 70%-проблема, 2024») + speaker notes + chapter.
**Issue:** Footer-форма `(70%-проблема, 2024)` и notes-форма «70%-проблема» отличаются от canon. **Это исторически корректно** — Osmani назвал «70%-проблема» в 2024, обновил до «80%» в 2025; chapter §1.4 это документирует явно. Видимый главный слой (заголовок плашки s08) использует canon. Не drift в строгом смысле — атрибуция источника сохраняет историческое имя.
**Recommendation:** Report-only, owner-tolerance. Если хочется единообразия — footer оставить «Osmani, 2024» без формы термина. Не блокер.

### D3 — s03 chapter_ref рассинхрон deck.yaml ↔ slide-file
**Severity:** P2
**Where:** `deck.yaml:150` → `chapter_ref: "§0.2, §0.4 [for-slide-s03]"`; `slides/s03-recap-lec3-ladder.md:9` frontmatter → `chapter_ref: "§0.4 [for-slide-s03]"` (без §0.2).
**Issue:** Render-источник (deck.yaml) и авторский slide-file расходятся в метаданном chapter_ref для s03. Содержательно **обе ссылки верны** (§0.2 несёт `[for-slide-s03]` якорь — 2 абзаца про Л3-перенос; §0.4 несёт определения A/B/C/D). Контент s03 опирается на §0.2+§0.4 (полная версия = deck.yaml). Это метаданный дрейф, не влияет на видимый слой и не нарушает book-first; но трекинг-целостность нарушена (которая ссылка канон при будущих cascade-grep?).
**Recommendation:** Sync slide-file frontmatter → `chapter_ref: "§0.2, §0.4 [for-slide-s03]"` (привести к deck.yaml = render-источник = более полная и корректная версия). Designer-правка 1 строки. Не блокер сам по себе, фиксить в той же revision-итерации, что D1.

## Coverage gaps
Нет. Все s03/s04/s05/s06/s07 утверждения backed главой; 0 slide-assertion без опоры. Все 32 chapter_ref резолвятся. 5 точек возврата покрыты. Раздел-0 перестройка структурно консистентна с chapter §0–§1.1.

## Что CLEAN (не фиксить)
- **Book-first integrity:** chapter*.md byte-identical ad61db5. Designer соблюдал book-first.
- **Раздел-0 перестройка (s03/s04/s05/s06/s07) видимый слой:** 0 §-кодов / 0 LO-кодов / 0 disclaimer-leak / 0 VFY — Решение #100 соблюдён в scope перестройки.
- **s05 (наивысший риск перестройки):** тезис «цена/радиус ошибки растёт A→D; A=каждый токен, D=вход/выход» — backed §1.1 line 159 + §3.4. Слот переиспользован корректно, НЕ renumber. 0 overclaim.
- **Terminology vs glossary lock:** автокомплит=0, кодинг-агент консистентен (34/0), perception-gap canon (35× + 1 inline-gloss «разрыв восприятия» = по glossary note), «почти правильный» код 20× консистентно, forbidden-англицизмы (пайплайн/фоллбэк/эдж-кейс/инсайт)=0 (единственный hit — комментарий в deck.yaml документирующий запрет).
- **5 точек возврата ЦВ:** s08→§1.4 / s13→§2.3 / s17→§3.5 / s21частично+s23полный→§4.4+§4.7 / s26→§5.2 — точно по plan §2.1 (fixed: точка4=s21+s23, точка5=s26) + chapter §0.3.
- **Orphan:** 0 — старая «4-вопроса рамка» (бывш. s05) не висит orphan; корректно: §1.1 = канон рамки → применяется на s11/s15 + s03-notes. Нет forward-ref на удалённые/несуществующие слайды.
- **Citation regression:** 0 — числа не тронуты (fact-checker был APPROVE-CLEAN, не регрессировало).

## Топ-фиксов (per artifact)
- **Chapter:** ничего (book-first, source of truth верен, 0 P0 в главе).
- **Slides (одна revision-итерация):**
  1. **[P1]** Strip visible §/sNN/[VFY]/чужие-Л3-§ с Body+footer s11/s12/s15/s20/s21/s22/s23/**s24**/s25/s27/s28/s30 → содержательные имена / «как в Лекции 3» / «далее» / notes-only. **s24 Body-таблица колонка «Точка» — приоритет (рендерится на проекцию).**
  2. **[P2]** Sync `slides/s03-*.md` frontmatter `chapter_ref` → `"§0.2, §0.4 [for-slide-s03]"` (= deck.yaml).
  3. **[P2 report-only]** D2 70/80% footer-форма — owner-tolerance, опционально.
- **Speech:** N/A (Phase 9, ещё не создан).

## Re-QA gate
После slides-revision D1+D3 → re-run consistency (terminology-only mode достаточно для D3; full visible-leak grep для D1) + pre-gate mode=slides перед USER GATE B. Раздел-0 перестройка повторного content-review не требует (CLEAN).
