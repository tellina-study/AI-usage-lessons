# Phase 4c critique — synthesis для Chapter v3 (Лекция 11)

**Дата:** 2026-05-21
**Branch:** issue-127-lec-11-manufacturing
**Input:** chapter.md v3 (commit b5b0084, 29 822 слова)
**Critics:**
- methodology-critic v3 — REVISE, 2 P0 + 7 P1 + 7 P2 (commit f4bd8ce)
- fact-checker v3 — APPROVE-WITH-POLISH, 1 P0 + 5 P1 + 6 P2 (commit ade7234)

---

## Combined verdict — **REVISE**

3 P0 (2 methodology + 1 fact) + 12 P1 (7 + 5) + 13 P2 (7 + 6). Все P0 — fixable, не structural. P1 dominated by Russification regression на NEW content (101 hits) — это **carry-forward risk в slides + speech**, должно закрыться v4.

**Kernel preserved** (methodology confirms): keystone Variant C, 5 разделов, LO mapping, 8+ cornerstones, 5 mandated fundamentals + 4 new (Sim2Real / Constrained RL / V-model / DO-178C) — глубоко covered. 3 worked examples достигли рамка-как-фильтр.

**Failure-bucket strict-in independent recount:** **~75-80% chapter words** (methodology sample 23/24 strict-in). Comfortably ≥30%. Не блокер.

---

## Block A — P0 (3 — MUST FIX)

### P0-1 [methodology]. §3.5 buffer-copy duplicate (lines 815/819 ≡ 823/825)
- **Issue:** verbatim параграфы СИБУР + ММК/НЛМК/Северсталь скопированы дважды (expansion artifact).
- **Fix:** удалить duplicates, оставить одну версию each. Проверить flow §3.5.

### P0-2 [methodology]. §4.4 ↔ §4.5 swapped в body vs TOC
- **Issue:** TOC говорит §4.4 → §4.5; body имеет §4.5 на line 1068 → §4.4 на line 1084. Payoff LO8 misordered.
- **Fix:** swap body sections back: §4.4 (5-step framework) перед §4.5 (failure-pattern matrix), согласно TOC. Verify links.

### P0-3 [fact]. §2.4 Sakichi Toyoda Type-G loom 1924 → 1925
- **Issue:** Chapter «1924 — патентует Type-G»; реально Type-G completed November 1925; patents filed Nov-Dec 1924.
- **Fix:** «1924 — патенты Type-G; 1925 — первый Type-G loom completed». Sources: Toyota Global Website history; JPO.

---

## Block B — P1 (12 — significant)

### P1-1 [methodology]. **Russification regression — 101 anglicism hits в NEW content** (critical)
- **Issue:** v2 had 0 narrative anglicisms outside whitelist; v3 expansion added 101 hits в new sub-sections. Carry-forward risk в slides + speech.
- **Hot zones:**
  - §1.3 Tesla Optimus narrative
  - §2.3 Rethink Robotics Baxter + UAW
  - §3.2 ExxonMobil refinery
  - §3.3 Edge Tier 1-4 taxonomy (English subheaders Tier 1 / Tier 2 / Tier 3 / Tier 4)
  - §3.4 FDA warning letters
  - §3.6 RL drift detection methods (4 triggers)
  - Q11 (CFO ROI), Q13 (Sim2Real gap), Q14 (legacy PLC)
- **Fix:** deep sweep по 7 hot zones — RU canonical + inline gloss первое упоминание + post-sweep deep latin-token scan target: 0 narrative anglicisms outside whitelist.

### P1-2 [methodology]. Worked examples asymmetric (2 pass + 1 fail vs better 1 pass + 2 fail)
- **Issue:** Brewery packaging CV-QC = pass; Pfizer Vox = pass; Avionics MTBF 8 = fail. Critic argues better balance is **1 pass + 2 fail** так как LO8 о «когда AI не нужен».
- **Fix decision:** **REJECT this P1** — keep current 2 pass + 1 fail. Rationale: 4 категории критериев + 6 альтернатив + 5-step framework — уже demonstrate fail-direction; worked examples должны balance positive (где AI работает с границами) + negative (где AI не работает). 2 pass + 1 fail отражает реальное распределение в industry. Сохранить как есть. **Не fix.**

### P1-3 [methodology]. Cyrillic+Latin hybrid typo «глаz» (line 139)
- **Fix:** «глаз» (все буквы кириллица).

### P1-4 [methodology]. Recursive parens «застревание на пилотной стадии (застревание на пилотной стадии)» (line 112)
- **Fix:** удалить дублирующий paren — оставить одну версию.

### P1-5 [methodology]. Q11 CFO ROI curriculum drift
- **Issue:** Q11 «Как доказать ROI от AI на shop floor финансовому директору?» — management-oriented, не engineering.
- **Fix:** **REWRITE Q11** на engineering-side: «Как измерить OEE до и после AI-внедрения чтобы получить честный baseline?» (метрика, не финансы) ИЛИ заменить на новый Q11 «Что обязан спросить инженер у поставщика AI-решения помимо ROI?» (4 vendor questions deep).

### P1-6 [methodology]. Edge inference Tier 1-4 taxonomy — English subheaders
- **Fix:** Tier 1 → «Уровень 1 (правило-ориентированные пороги)», Tier 2 → «Уровень 2 (классический ML на edge-шлюзе)», Tier 3 → «Уровень 3 (глубокое обучение на edge AI-ускорителе)», Tier 4 → «Уровень 4 (гибрид edge+облако)».

### P1-7 [methodology]. §3.4 FDA warning letters — real + speculation mixed
- **Issue:** Chapter cites FDA Form 483 examples Eli Lilly / Pfizer но specific 2022-2023 AI-related citations not source-verifiable.
- **Fix:** реformulate как «иллюстрационная формулировка типичной FDA-citation на data integrity для AI/ML» БЕЗ specific company attribution — illustrative pattern, не actual incidents. Или verify через FOIA если есть time (recommend: generalize).

### P1-8 [fact, was P1-1 fact]. §1.3 IBM Watson Health $5B → $4B
- **Issue:** Chapter says «более 5 млрд» — IBM PRNewswire 2016 says «more than $4 billion» (Truven $2.6B + Merge $1B + Phytel/Explorys undisclosed).
- **Fix:** «суммарно более 4 миллиардов долларов» per IBM-disclosed.

### P1-9 [fact, was P1-2 fact]. §2.4 GM Hamtramck timeline 1985-1989 → 1985-1990
- **Issue:** Roger Smith retired August 1990, не 1989.
- **Fix:** «1985-1990» или «конец 1980-х».

### P1-10 [fact, was P1-3 fact]. §1.2 FoxBrain «DeepSeek techniques» → distillation method
- **Issue:** FoxBrain distilled from Llama 3.1; comparisons to DeepSeek distilled models. Не «using DeepSeek techniques».
- **Fix:** «обучен на основе Llama 3.1 70B методом дистилляции; в сравнении с дистилляционной моделью DeepSeek — небольшое отставание (per Hon Hai release April 2025)».

### P1-11 [fact, was P1-4 fact]. §1.3 Tesla Optimus «сотни» soften
- **Issue:** Tesla не disclose specific unit counts publicly.
- **Fix:** «pilot deployments, точное количество не disclose; полное production scale-up отложен до V3 reveal (запланирован late 2026)». Tag `[VFY-day-of]`.

### P1-12 [fact, was P1-5 fact]. §1.2 Honeywell MRO copilot — нет specific press, generalize
- **Issue:** Honeywell investor 8-K filings не выделяют «MRO copilot» как specific product.
- **Fix:** «отрасль (включая Honeywell, GE Aerospace) обсуждает дорожные карты MRO copilots; production-deployed examples в полётно-сертифицированных операциях не подтверждены» — без specific Honeywell attribution.

---

## Block C — P2 (13 — apply if cheap)

### Methodology P2
- **P2-M1.** Tesla Optimus 4th hype case overlap с s09b — coordinate в Phase 5 slides, не chapter polish.
- **P2-M2.** GM Hamtramck referenced дважды (§1.1 + §2.4) — оставить, разные ракурсы.
- **P2-M3.** ATEX equipment categories block (lines 757-769) — heavy English markers, можно частично русифицировать (Zone 0/1/2 — это standard, оставить; II 1G / II 2G — оставить как certification code).
- **P2-M4.** Bainbridge 4 ironies headings — добавить RU перевод.
- **P2-M5.** Edge inference 4-tier overlap с §4.2 matrix — fine, cross-reference.
- **P2-M6.** Brewery worked example italics — нормализовать форматирование.
- **P2-M7.** Optimus dating Q1 2026 — `[VFY-day-of]` tag нужен (закрывается в P1-11 fact fix).

### Fact P2
- **P2-F1.** §2.4 Tesla Shanghai opening — «март 2020» → «декабрь 2019 — январь 2020».
- **P2-F2.** §2.1 TSMC abstain rate 8-12% — generic «на типичных AOI-линиях».
- **P2-F3.** §3.4 FDA Eli Lilly / Pfizer Form 483 — обобщить (закрывается в P1-7 methodology fix).
- **P2-F4.** §3.4 Pepperl+Fuchs «ExTech» → «VisuNet / BPC3200 ATEX-certified».
- **P2-F5.** §2.1 BAAL attribution — добавить «(ServiceNow AI Research, ex-Element AI)».
- **P2-F6.** §1.3 IBM Watson MSKCC pushback — добавить «MSKCC впоследствии заявила, что эти случаи были частью system testing» для balanced framing.

---

## Block D — что НЕ менять (stable kernel)

- ❌ НЕ переписывать keystone Variant C (confirmed valid).
- ❌ НЕ менять 5-section structure / LO mapping.
- ❌ НЕ переделывать 3 worked examples (P1-2 rejected — keep 2 pass + 1 fail).
- ❌ НЕ удалять Tesla Optimus 4th hype case / GM Hamtramck / Bainbridge / Rethink Baxter (kernel of expansion).
- ❌ НЕ снижать word count (target 30k удерживать).

---

## Phase 4d revision brief (book-editor v4)

**Priority order:**
1. **P0 (3) MUST FIX:**
   - P0-1 §3.5 удалить duplicate paragraphs (~10 мин)
   - P0-2 §4.4 ↔ §4.5 swap body to match TOC (~10 мин)
   - P0-3 §2.4 Toyoda 1924 → 1924-1925 date fix (~5 мин)

2. **P1 Russification deep sweep на 7 hot zones (~30-40 мин):** Tesla Optimus / Rethink+UAW / ExxonMobil / Edge Tier taxonomy / FDA letters / RL drift / Q11+Q13+Q14. Post-sweep deep latin-token scan target: 0 narrative anglicisms outside whitelist.

3. **P1 misc:**
   - P1-3 «глаz» typo (~1 мин)
   - P1-4 recursive parens (~1 мин)
   - P1-5 Q11 CFO ROI rewrite to engineering-side (~10 мин)
   - P1-6 Tier 1-4 RU subheaders (~5 мин)
   - P1-7 FDA letters generalize (~5 мин)

4. **P1 fact (5):**
   - P1-8 IBM Watson $5B → $4B (~2 мин)
   - P1-9 GM Hamtramck 1985-1990 (~2 мин)
   - P1-10 FoxBrain distillation reformulate (~5 мин)
   - P1-11 Tesla Optimus «сотни» soften (~5 мин)
   - P1-12 Honeywell MRO generalize (~5 мин)

5. **P2 apply if cheap (~15 мин):** Tesla Shanghai date / TSMC generic / Pepperl+Fuchs / BAAL / MSKCC balanced framing / Bainbridge ironies RU headings / brewery italics.

**Total estimated:** ~1.5 ч single book-editor spawn.

**Output target:** `library/lectures/lec-11/chapter.md` v4 (status: reviewed, version: v4), word count stays at ~29.8k ±200 (small fluctuations from polish, не shrink).

**Post-revision:** Pre-USER-GATE A walkthrough (orchestrator) → USER GATE A re-present.
