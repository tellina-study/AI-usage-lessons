# Phase 7 critique — synthesis для Slides v1 (Лекция 11)

**Дата:** 2026-05-21
**Branch:** issue-127-lec-11-manufacturing
**Input:** 39 slides + PPTX v1 (commit 5a6378e)
**Critics (5 parallel):**
- presentation-critic — **REJECT**, 3 P0 + 13 P1 (commit 1b4534b)
- fact-checker — **REVISE**, 2 P0 + 8 P1 + 6 P2 (commit 59fe5bf)
- consistency-checker — **REVISE**, 4 P0 + 5 P1 + 3 P2 (commit 7990dde)
- student-simulator — **APPROVE-WITH-POLISH** (commit 21ff958)
- reader-simulator rendered — **APPROVE-CLEAN**, 87% self-contained, 2 P1 (commit 7155c0d)

---

## Combined verdict — **REJECT → REVISE-HEAVY**

Worst verdict (presentation-critic REJECT) overrides. ~9 P0 + ~28 P1 across 5 critics. **Не polish — структурная revision required.**

Kernel preserved (что критики confirm):
- ✓ Lec-09 pattern compliance 10/12 PASS (lecture-map, glossary, 5 dividers, dedicated Q&A)
- ✓ Schema geometry passes (s05 keystone, s22, s25 CIRL, s32, s33, s34, s35)
- ✓ Failure-bucket strict-in ~61% (target ≥30%)
- ✓ 7/7 cornerstone retention (reader-rendered after 2 нед)
- ✓ 75-мин attention hold (student-sim)
- ✓ Real images 10/39 Wikimedia Tier 2 acquisition

---

## Block A — P0 issues (9 total — MUST FIX)

### P0-1 [presentation]. Typo «Sertification» ×2 на s09 (critical literacy gap в core OT/IT schema)
- **Source:** `slides/s09-ot-it-split.md` визуальная карточка
- **Fix:** «Certification» (correct English) или «Сертификация» (RU canonical) — choose RU per Russification mandate.

### P0-2 [presentation]. `[VFY-day-of]` маркеры visible на s07 + s08 footer
- **Source:** rendered PPTX visible body footer.
- **Fix:** remove from visible body. `[VFY-day-of]` — internal verification marker для frontmatter / orchestrator, не student-facing.

### P0-3 [presentation]. Hero structural gap — s01 = 31% площади, s39 = 32.5% (target ≥40%, designer self-report FALSE)
- **Source:** [[hero-images-required]] mandate ≥40% area.
- **Fix:** resize Tesla Giga Press на s01 + BMW Welt на s39 до ≥40% площади slide. Designer self-report «s01 ≥40% ✓ / s39 ≥40% ✓» — оркестратор visual sweep confirms FALSE.

### P0-4 [fact]. s07 «Deloitte 2025: 42% / $7,2M sunk cost» — wrong attribution
- **Chapter v4 fixed это на S&P Global 46% / $7M (P0-1 в chapter v3 critique).**
- **Fix:** s07 → «S&P Global Market Intelligence (AI Experiences Survey 2025): **46% PoCs scrapped before production**, средние невозвратные затраты ~**7 миллионов долларов**». Update slide source.

### P0-5 [fact]. s11 «Reality check на февраль 2026» — anachronism (лекция в мае 2026)
- **Fix:** s11 → «Май 2026 (текущий момент)» или «На дату подготовки лекции (май 2026)» с `[VFY-day-of]` marker.

### P0-6 [consistency]. s29 Норникель overclaim «industrial stage»
- **Chapter v4 (line 815) honest hedge:** «пилотная / ранняя промышленная стадия; OEE-критерий >12 мес SLA не верифицируемо из открытых источников».
- **Fix:** s29 → align с chapter honest hedge — «пилот / ранняя промышленная, точные метрики не раскрываются».

### P0-7 [consistency]. s29 Газпром нефть attribution к Норникелю
- **Chapter v4 clarified:** Норникель собственные операции **vs** Газпром нефть Северо-Соленинское — это **отдельные компании**.
- **Fix:** s29 → разделить attribution или удалить Газпром нефть с slide Норникеля (оставить только в speaker notes как aside).

### P0-8 [consistency]. §4.3 worked examples gap — slides has только Pfizer
- **Chapter v4 (§4.3 + §4.3b + §4.3c):** 3 worked examples — **Pfizer Vox pass** (existing slide) + **авиадвигатель MTBF 8 fail** (missing) + **brewery packaging pass** (missing).
- Reader-rendered тоже flagged: «brewery в slides отсутствует, "avionics fail" = F-35 ALIS callback».
- **Fix:** добавить **s34b** «Авиадвигатель MTBF 8 — рамка отсекает» (avionics fail) **+** **s34c** «Brewery packaging CV-QC — рамка пропускает» (brewery pass). 5-step framework apply per slide. Без этих slides §4 payoff неполный — рамка-как-фильтр работает только в одну сторону.

### P0-9 [consistency]. s32 11 критериев vs chapter §4.1 = 10 + 1 бонус
- **Chapter §4.1:** 4 категории × 3+2+3+2 = 10 + 1 «бонус» SIL 2/3.
- **Slides s32:** 3+2+3+3 = 11.
- **Fix:** align s32 со chapter — 10 + 1 бонус (или 4 категории suporeo 3+2+3+2).

---

## Block B — P1 issues (significant — ~28 total)

### P1-1 [presentation]. Designer-extras leaks (17 hits orchestrator-INDEPENDENT regex; designer self-report «0» FALSE)
- **Leaks:** LO codes на 5 slides (s02/s21/s29/s32), §4 cross-refs на 4 slides (s16/s22/s24/s30), «callback s16» на s20, «возвращаемся в разделах» на s04.
- **Fix:** **independent regex grep** на rendered PPTX visible body — все scaffold-фразы 0:
  - `«Лектору»` / `«Вы здесь»` / `тайминг` / `[VFY]` / `[FACT-CHECK]` / `LO[1-9]` / `§[0-9]` / `→ s[0-9]+` / `(s[0-9][0-9])` / «course-scaffold» / «не вводи* нов» / «возвращаемся [0-9N]» / «— в главе» / «в материалах лекции» / «это payoff» / «callback» / «точк* возврата».

### P1-2 [presentation]. Deep latin-token scan: 620 unique / 1149 occurrences (**2.8× хуже Лекции 8 v1**)
- Critical anglicisms на ~28/39 slides.
- Student-sim confirms: «s11/s12/s22/s26/s30 — 30-40% смысловых слов латиницей».
- **Fix:** deep Russification sweep с anti-anglicism mandate. Target: `unique - whitelist ≤ 30`. Whitelist: brand names + acronyms с inline gloss + verbatim quotes.

### P1-3 [presentation]. Modul typo s39
- **Fix:** «Модуль» (RU correct).

### P1-4 [fact]. s18 Atlas attribution HMGMA vs chapter RMAC
- **Chapter v4:** Robotics Manufacturing Application Center (RMAC).
- **Fix:** s18 → RMAC, not HMGMA.

### P1-5 [fact]. s10 FoxBrain «derivative + DeepSeek techniques» — regression
- **Chapter v4 (P1-10):** «обучен на основе Llama 3.1 70B методом дистилляции; в сравнении с дистилляционной моделью DeepSeek — небольшое отставание».
- **Fix:** s10 → align с chapter v4 wording.

### P1-6 [fact]. s14 TSMC 95%/+10-15% as TSMC-disclosed
- **Chapter v4 (P2-F2):** «на типичных AOI-линиях полупроводникового производства» (illustrative, не TSMC IR).
- **Fix:** s14 → soften attribution.

### P1-7 [fact]. s11 Optimus numbers «10-20K к 2025, $30K»
- **Chapter v4 (P1-11):** «несколько тысяч к концу 2025, миллион к 2027, $25K; полное масштабирование отложено до V3 reveal late 2026; точное количество не disclose».
- **Fix:** s11 → align с chapter v4 + add `[VFY-day-of]` marker.

### P1-8 [fact]. SYSTEMIC: 0 `[VFY-day-of]` markers на slides vs 33 в chapter
- 14+ volatile claims need markers (market sizes, vendor counts, deployments).
- **Fix:** add `[VFY-day-of]` markers на speaker notes (НЕ visible body — это P0-2 уже). Or use small footnote indicator if absolutely needed.

### P1-9 [fact]. s18 Toyota GAIA 10K hours not tagged как vendor claim
- **Fix:** mark «по заявлению Toyota — без независимого аудита» в notes.

### P1-10 [consistency]. Vendor Q5 trifurcation
- chapter §5.2 «Прошлые провалы» / s35 «4 вопроса» / s38 «5-й вопрос Архитектурный класс» — **три разных формулировки** одного и того же концепта.
- **Fix:** unify — chapter и slides и speech используют **5 vendor questions** with same names:
  1. Базовая линия до AI?
  2. Окно измерения?
  3. Перечень вмешательств (люди-процесс-tech)?
  4. OEE метрика до/после?
  5. **3 documented failures за last 24 months в той же индустрии?** (per chapter v5)
- s35 и s38 либо same 5 questions либо явная split (s35 = 4 + s38 = 5-й callback).

### P1-11 [consistency + student-sim]. Cornerstone drift «OT/IT раскол» (canonical) vs «OT-IT раскол» (s30, s37)
- **Fix:** unify на «OT/IT раскол» (slash, not dash).

### P1-12 [student-sim]. Шрифт мелкий на s14, s24, s27, s29, s39 (5 slides сжаты)
- **Fix:** resize text → 14-18pt body, 24-30pt headlines. Recheck via 50% zoom test.

### P1-13 [reader-rendered]. s39 hero typography мелкая
- **Fix:** hero text overlay readable at 50% zoom.

### P1-14 [student-sim]. s07 connection between «14×» (Pertama Partners aggregate) и 5.5%/95%/80%/42% — implicit
- **Fix:** explicit connecting headline или sub-text «эти 4 цифры друг друга поддерживают» / «совокупный сигнал».

### P1-15 [student-sim]. s10 layout — Siemens фото конкурирует с 3 карточками
- **Fix:** demote 3 cards в notes или resize/relocate Siemens image.

### P1-16 [student-sim]. s25 CIRL диаграмма требует 20 сек для понимания (5-second test fail)
- **Fix:** add explicit annotation «PID внутри RL, не вместо» в diagram + simplify visual hierarchy.

### P1-17 [student-sim]. s32 11 критериев перегружен (за раз не запомнить)
- **Fix:** group в 4 категории column-wise (already chapter §4.1 grouping) — show 4 column headers + 10 criteria + 1 bonus visually grouped, not flat list.

### P1-18 [presentation]. s35-s38 cross-redundancy (vendor questions repeat across multiple slides)
- **Fix:** consolidate.

### P1-19 [presentation]. s10 Foxconn quote dominates visual
- **Fix:** demote quote → callout / sidebar instead of central.

### P1-20 [reader-rendered]. s08 visible «[VFY-day-of]» leak в footnote — same as P0-2 already covered.

---

## Block C — P2 (apply if cheap, ~12 items)

- s24 crowded, s10/s17/s28 notes trim 10% (reader-rendered)
- s10 Layout reversed hierarchy (presentation-critic)
- Visual polish (font weights, contrast tweaks)
- Acquisition tier audit per image (per Pre-USER-GATE B Лекция 8 mandate)

---

## Block D — что НЕ менять (stable kernel)

- ❌ НЕ переписывать keystone (Variant C Discrete vs Process — confirmed valid).
- ❌ НЕ удалять real images (10 Wikimedia Tier 2 confirmed acquired).
- ❌ НЕ менять 39-slide structure / Lec-09 pattern compliance.
- ❌ НЕ удалять existing failure-bucket slides (61% strict-in confirmed).
- ❌ НЕ менять cornerstones canonical list (только fix drift «OT/IT раскол»).

---

## Phase 8 revision brief (presentation-designer v2)

**Priority order:**

1. **P0 (9) MUST FIX:**
   - Typo «Sertification» s09 (~1 мин)
   - `[VFY-day-of]` visible leaks s07+s08 (~5 мин)
   - Hero resize s01 + s39 to ≥40% area (~15 мин)
   - s07 Deloitte → S&P Global wording (~5 мин)
   - s11 «февраль 2026» → «май 2026» (~5 мин)
   - s29 Норникель overclaim + Газпром отделить (~10 мин)
   - **Add s34b «Авиадвигатель MTBF 8 fail» + s34c «Brewery packaging CV-QC pass»** (~30 мин — new slides design + render)
   - s32 11→10+1 align с chapter (~10 мин)

2. **P1 systemic (3 critical):**
   - Designer-extras leak sweep — orchestrator-INDEPENDENT regex verify (~30 мин)
   - Deep Russification pass: 620 unique → ≤30 (~60-90 мин — main work)
   - Add `[VFY-day-of]` markers в speaker notes на 14+ volatile claims (~10 мин)

3. **P1 fact (5):**
   - s18 RMAC (not HMGMA)
   - s10 FoxBrain distillation wording
   - s14 TSMC illustrative attribution
   - s11 Optimus numbers update
   - s18 Toyota GAIA vendor-claim tag

4. **P1 consistency (3):**
   - Vendor Q5 unify (~15 мин)
   - Cornerstone «OT/IT раскол» fix (~5 мин)

5. **P1 layout (8):**
   - Font resize s14/s24/s27/s29/s39
   - s39 hero typography
   - s07 connection headline
   - s10 Siemens image vs 3 cards balance
   - s25 CIRL diagram annotation + simplify
   - s32 group 4 categories visually
   - s35-s38 cross-redundancy consolidate
   - s10 Foxconn quote demote

6. **P2 polish (~12):**
   - s24 crowded, notes trim 10% на s10/s17/s28
   - Visual contrast polish

**Total estimated:** 4-6 ч single presentation-designer spawn.

**Final deck size projection:** 39 → **41 slides** (+2 from s34b + s34c worked examples).

**Output target:** revised PPTX + PDF + 41 PNG snapshots + iteration-log.md, status `reviewed`, version v2.

**Post-revision:** Pre-USER-GATE B walkthrough (visual sweep + designer-extras grep + deep latin scan + hero check + real-image verification) → USER GATE B presentation.
