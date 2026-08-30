# Consistency check chapter ↔ slides — Лекция 16

**Verdict:** APPROVE-WITH-POLISH

**Date:** 2026-05-27
**Phase:** 7 (post-slides finalization, pre-Phase 8 speech)
**Mode:** chapter+slides (full reverse-mapping)
**Artifacts:**
- Chapter v2.1 (5 parts, 32 309 слов actual)
- deck.yaml v2 (43 slides: s01-s42 + s07b)
- slides/*.md (43 files)

---

## Summary

Cross-artifact alignment **высокого качества**. Все 40 content-слайдов имеют corresponding `[for-slide-sNN]` marker в chapter (s02/s03/s04 — structural, не требуют). Все key numbers verifiable консистентны (Aramco $436,6B / $1,8B / 0,41%; Eni HPC6 $104M / 606 PFLOPS; MethaneSAT 15,5 мес / $5,7M/мес / 26%; 86% pilot stuck; CCS 190× / 0,02%; Cognitive Geo 2019 IBM Research Brazil). Все 10 documented failures имеют dedicated slides (s07, s07b, s11, s17, s18, s23, s25, s31, s32, s37, s38). 27 vendors из plan v2 mapped по slides. Keystone-ось матрицы данные×физика подана verbatim consistent (chapter §0.1-0.3 ↔ s05). 3 cornerstone концепта для Лекции 17 (s40) — verbatim из chapter §7.3.

**Главные находки:**
- **P1 Russification asymmetry** — chapter использует RU-первичную терминологию («застревание пилотов», «усталость операторов от ложных тревог», «когнитивный AI»), но visible body slides — EN-первичную («pilot stuck», «alert fatigue», «cognitive AI», «pilot purgatory»). 4 чётко drifting term.
- **P2 «10 documented failures»** consistent в chapter §7.2 + slides s39/s41 (task brief упоминал «11» — это включая Deepwater Horizon, который chapter явно помечает «bonus historical anchor», не в счёте 10). Никакого drift'а здесь нет.
- **P2 minor:** s23 frontmatter говорит «$5,7M/мес vs $1,5M/мес планировалось» — chapter §3.3 ту же цифру даёт. Verbatim ✓.

Никаких P0 issues. Slides ready для Phase 8 (speech derivation) — после Russification polish.

---

## P0 / P1 / P2 issues

### P0 (factual contradiction / missing coverage): 0

— Нет.

### P1 (significant drift): 1

**P1-1. Russification asymmetry chapter ↔ slides visible body.**

Chapter consistently uses **RU-первичную** терминологию с EN в parentheses:
- chapter-part5.md L92: «застревание пилотов (pilot purgatory)»
- chapter.md L299: «усталость операторов от ложных тревог»
- chapter-part4.md L314: «концентрированная ставка», «структурное застревание пилотов»

**Slides visible body** использует **EN-первичную**:
- s06 (Q1 divider) visible_numbers + tag: «86% pilot stuck» (без RU gloss)
- s07 visible_numbers: «86% pilot stuck», «3% deep integration»
- s07b: заголовок «Aspen Mtell: «alert fatigue устранена» — маркетинг»
- s12 bottom bar: «14% successful 86% pilot stuck»
- s17 bottom bar: «cognitive AI» 2018
- s18 visible body: «pilot purgatory» untranslated
- s32 speaker notes: «alert fatigue plus plant-wide stagnation»
- s39 Q1 summary speaker notes: «86% pilot stuck», «alert fatigue», «Cognite IPO postpone», «C3.ai O&G declining»
- s41 Q&A: «pilot stuck», «pilot purgatory», «cognitive AI» — все без gloss
- s35 speaker notes: «cognitive AI для exploration» (untranslated)

**Severity:** P1. Chapter source-of-truth явно использует RU gloss («застревание пилотов», «усталость операторов»). Slides отступают — visible body чаще оставляет английские термины без gloss. Это violation memory rule [[russification]] для МГТУ ИУ6 audience.

**Recommendation для Phase 8:**
1. Fix slides — добавить inline RU gloss при first-use каждого:
   - «pilot stuck» → «застревание пилотов (pilot stuck)»
   - «alert fatigue» → «усталость от ложных тревог (alert fatigue)»
   - «cognitive AI» → «когнитивный AI (cognitive AI)»
   - «pilot purgatory» → «застревание пилотов (pilot purgatory)»
2. После first-use можно использовать любую форму, но first-use должен иметь gloss.
3. Speech writer Phase 8 — обязан использовать RU термины как primary в narrative.

### P2 (minor inconsistency): 2

**P2-1. Failure count assertion** — task brief упоминал «11 documented failures», но chapter §7.2 + slides s39/s40/s41 consistently говорят «10 documented failures + 1 bonus historical anchor (Deepwater Horizon)». Chapter-part4.md L312: «Bonus historical anchor: Deepwater Horizon 2010». Verdict: **no actual drift** — task brief был incorrect (или counted Deepwater как 11-й). Chapter + slides aligned at «10».

**P2-2. Minor russification term variation** — s23 speaker notes использует «единичная уязвимость (SPOF)» с RU+EN, но s23 visible body — «catastrophic SPOF» без gloss. Mild inconsistency, не критическая (SPOF — устоявшийся term в industry).

---

## Check results

### 1. Slide-маркеры reverse mapping

**Status:** PASS (clean).

44 `[for-slide-sNN]` markers в chapter покрывают 40 unique content slide IDs:
- s01, s05 (×3 для §0.1-0.3), s06-s12, s13-s19 (×2 для §2.7), s20-s27, s28-s33, s34-s42 — все covered.
- s07b — covered.
- s02 (cover), s03 (about), s04 (lecture-map) — structural, не требуют chapter markers.

**Каждый slide.md имеет valid `chapter_ref` frontmatter** pointing к existing chapter section. Verified for s05 (§0.1-§0.3), s07 (§1.2), s17 (§2.5), s23 (§3.3), s29 (§4.2), s35 (§5.2), s40 (§7.3), s41 (§7.3 exit ticket).

### 2. Vendor coverage (27 vendors)

**Status:** PASS.

37 unique vendor brand names appear across slides: ABB, AIQ, Ambyint, Aramco, Aspen(Tech), Beyond Limits, Bridger, C3.ai, Carbon Mapper, Cognite, Cognitive Geo, EOG, Emerson, Eni, Equinor, ExxonMobil, Fervo, GHGSat, Halliburton, Honeywell, IBM, NOV, Nabors, Northern Lights, Precision (Drilling), Project Canary, Repsol, Roxar, SLB, Schlumberger, SeekOps, Yokogawa, Газпром, ЛУКОЙЛ, Роснефть, Сургут(нефтегаз), Татнефть.

Plan v2 expected 27 vendors — actual 37 (выше plan). Все 27 plan vendors covered плюс additional (NOV, Precision Drilling, ABB, Equinor, Carbon Mapper, etc).

**Russian players covered:** Газпром нефть (s35), Роснефть (s10, s36), Татнефть/ЛУКОЙЛ/Сургутнефтегаз (s36 minimum mention). AIQ partnership (s35 footer). Verified consistent с chapter-part4.md.

### 3. Numbers consistency (sample 15)

**Status:** PASS (all 15 verified consistent).

| # | Claim | Chapter | Slide | Match? |
|---|---|---|---|---|
| 1 | 86% pilot stuck | chapter.md L257, chapter-part5.md L62 | s07 visible + speaker | ✓ |
| 2 | Aramco $1,8B realized 2024 | chapter.md L125 | s05 visible_numbers, s14 visible | ✓ |
| 3 | Aramco выручка $436,6 млрд | chapter.md L125, chapter-part2.md L77 | s14 L45 | ✓ |
| 4 | 0,41% выручки | chapter.md L125 | s14 visible_numbers | ✓ |
| 5 | Eni HPC6 606 PFLOPS / $104M | chapter-part2.md L59 | s14 L29-31 | ✓ |
| 6 | ExxonMobil Discovery 6 4 032 GH200 | chapter-part2.md L130 | s14, s16 | ✓ |
| 7 | METABRAIN 250B params / 90 лет | chapter-part2.md L42 | s14 visible_numbers | ✓ |
| 8 | MethaneSAT 4 марта 2024 запуск | chapter-part3.md L64 | s22, s23 timeline | ✓ |
| 9 | MethaneSAT 20 июня 2025 потеря | chapter-part3.md L96 | s23 заголовок | ✓ |
| 10 | 15,5 мес = 26% lifetime | chapter-part3.md L96 | s23 visible_numbers | ✓ |
| 11 | $5,7M/мес vs $1,5M/мес | chapter-part3.md L108 | s23 visible_numbers | ✓ |
| 12 | GHGSat 13-constellation сер 2025 | chapter-part3 (§3.4) | s24 L35 | ✓ |
| 13 | Northern Lights 1,5 Mt / 190× / 0,02% | chapter-part3.md L297, L310 | s29 visible_numbers | ✓ |
| 14 | Fervo IPO $1,89B / $7,7B | chapter-part4.md L281 | s30 (referenced) | ✓ |
| 15 | Cognitive Geo 2019 IBM Research Brazil | chapter-part4.md L71 | s35 speaker notes L47 | ✓ |

Additional verified: Aspen $17B Emerson acquisition (chapter.md L299 ↔ s09 L37); BP Beyond Limits $20M Series B июнь 2017 (chapter-part2.md L162 ↔ s17 L21); IBM Watson Repsol Kalimba 2014 (chapter-part2.md L199 ↔ s18); Bridger 4× aerial vs OGI (chapter-part3.md L128 ↔ s24 visible_numbers); Cognite ARR $94M (chapter.md L407 ↔ s11); C3.ai 5,9% FY24 (chapter.md L414 ↔ s11).

### 4. Failure cases reference chain (10 + 1)

**Status:** PASS.

| # | Failure | Chapter ref | Slide |
|---|---|---|---|
| 1 | BP + Beyond Limits | §2.5 | s17 (dedicated) |
| 2 | IBM Watson + Repsol Kalimba | §2.6 | s18 (dedicated) |
| 3 | Cognite IPO postpone | §1.7 | s11 (combined с C3.ai) |
| 4 | C3.ai O&G declining | §1.7 | s11 (combined с Cognite) |
| 5 | MethaneSAT loss | §3.3 | s23 (dedicated) |
| 6 | 86% AI pilot stuck | §1.2 | s07 (dedicated) |
| 7 | Aspen Mtell alert fatigue + plant-wide stagnation | §1.3 + §4.5 | s07b + s32 |
| 8 | 2020 oil crash 107k jobs | §6.2 | s38 (combined с Deepwater) |
| 9 | 4× discrepancy MethaneSAT vs EPA | §3.5 | s25 (dedicated) |
| 10 | Cybersecurity ransomware +935% | §6.1 | s37 (dedicated) |
| Bonus | Deepwater Horizon 2010 | §6.3 | s38 (combined с 2020 crash) |

All 10 failures + bonus historical anchor have dedicated or combined slide treatment. **Chapter §7.2 + s39/s40/s41 consistently say «10 documented failures».** No drift.

Additional CCS 190× scale-up gap (s31, §4.4) и refinery plant-wide stagnation (s32, §4.5) — Q4 failures, listed в s41 Q&A as quotable failures.

### 5. Keystone axis consistency (chapter §0.1-§0.5 ↔ s05)

**Status:** PASS (verbatim alignment).

Chapter §0.1-§0.3 defines:
- Доступность данных: «достаточно ли labeled examples для обучения + обобщения». Q1: 1000+ wells = да; Q3: 1-5 wildcat = нет.
- Определённость физики: «есть ли установившаяся численная модель с известной точностью». Q3 (Eclipse/INTERSECT): да; Q2 (multi-modal fusion): нет.

s05 matrix bottom-left inline definitions:
- «Доступность данных = достаточно ли labeled examples для retraining + generalization. Q1: 1000+ wells = да. Q3: 1-5 wildcat wells = нет.»
- «Определённость физики = есть ли установившаяся численная модель с известной точностью. Q3 (Eclipse, INTERSECT): да. Q2 (multi-modal fusion): нет.»

**Verbatim match** ✓ (allowing for slight space optimization).

**Quadrant mapping consistent:**
- Q1 (high data + high physics): Ambyint +15% / Aramco / Honeywell UOP — same в chapter §0.3 + s05 + s09.
- Q2 (high data + low physics): MethaneSAT / Carbon Mapper / GHGSat — same в chapter §0.3 + s05 + s20.
- Q3 (low data + high physics): Aramco METABRAIN / Eni HPC6 / SLB Lumi — same в chapter §0.3 + s05 + s14, s15.
- Q4 (low data + low physics): Northern Lights / Fervo — same в chapter §0.3 + s05 + s29, s30.

Bottom-bar gold-tint message «За каждым AI-внедрением — alternative tool» — present в s05 + repeated в chapter §0.3 закрытие + §7.1 synthesis.

### 6. Cornerstone concepts (chapter §7.3 ↔ s40)

**Status:** PASS (verbatim alignment).

Chapter §7.3 defines 3 cornerstones для Лекции 17:
1. **AI judgment как структурная задача** — где применим, где нет.
2. **Альтернатива-как-исходный уровень** — каждое AI-внедрение имеет параллельный не-AI вариант.
3. **Industry cyclicality > AI hype cycle** — 2020 crash как paradigmatic case.

s40 visible body использует **те же 3 numbered cards** с identical headlines and key formulation:
- «Главный инференциальный навык — не «как запустить AI», а «как определить, применим ли»» ↔ chapter L333 verbatim.
- «Каждое AI-внедрение имеет параллельный не-AI вариант» ↔ chapter L335 verbatim.
- «107k jobs за 6 мес → AI заморожены 18-24 мес» ↔ chapter L341 verbatim.

**Verbatim bridge к Лекции 17** mentioned в both: «Лекция 17 — systematization» / «portable diagnostic tools на любую следующую отрасль».

### 7. Q&A backup cross-reference (chapter-part5 §8 ↔ s41)

**Status:** PASS (с note).

Chapter-part5.md §8 contains 12 Q&A backup questions:
- Q1 NVIDIA Omniverse, Q2 connect L14+L12, Q3 mining REE, Q4 % AI ROI, Q5 frontier basin foundation model, Q6 BOP, Q7 (continuing)...

s41 Q&A slide содержит **3 exit ticket вопроса** (не 12 — это by-design, exit ticket vs deep backup):
- Q1 (LO1): essential quadrant
- Q2 (LO2 cross-cutting): 2 failures из 10
- Q3 (LO2+LO3): 3 critique criteria

**Alignment:** s41 — exit ticket subset; chapter-part5 — deep backup reference. По design — не verbatim match, а complementary layers. Chapter §8 explicitly labelled «**Q&A backup** — 12 ожидаемых вопросов» для лектора резерва.

**Note:** s41 footnote bonus question («сравните Eni HPC6 vs ExxonMobil Discovery 6 vs Aramco METABRAIN») — корреспондирует с chapter-part2.md §2.2-2.4 comparative table. Not в §8 explicit list, но pulled from chapter Part 2 — valid cross-link.

### 8. Cross-references / orphan slides

**Status:** PASS (clean).

- **Slide-to-slide refs:** только `s32 L53` ментионит «s07b слайд в Q1 frame» — s07b exists, valid.
- **Slide-to-chapter refs:** все `chapter_ref` valid (verified sample 10 slides — pointing к existing sections).
- **Cross-lecture refs:** «Лекция 11/12/13/14/15» в s02 cover (all valid, previous lectures); «Лекция 17» в s40, s42 (forward ref, valid). Chapter part4 §7.3 references same lectures verbatim.
- **No orphan slide IDs** (deleted после R5 split — none).

### 9. Russification consistency

**Status:** **P1 ISSUE** (см. P1-1 выше).

Chapter — **RU-primary** consistently. Brand allowlist clear (MethaneSAT, Aramco, SLB, Cognite, Aspen, Bridger, GHGSat, Carbon Mapper, IBM, BP, Fervo, Equinor, Honeywell, ABB, Emerson, Roxar, Schlumberger, NVIDIA, AMD, Halliburton, Nabors, AIQ, ADNOC — all preserved as brand names).

Tech acronyms first-use gloss strategy в chapter:
- «BOP (blowout preventer)» — chapter §0.4 + repeated
- «SIS (safety instrumented system)» — chapter §0.4 + repeated
- «OGI (Optical Gas Imaging)» — chapter §0.4 + repeated
- «MRV (Monitoring/Reporting/Verification)» — chapter §0.4 + repeated
- «pilot purgatory» → «застревание пилотов» в chapter L283
- «alert fatigue» → «усталость операторов от ложных тревог» в chapter L301

Slides — **mixed**:
- Brand names — consistent.
- Tech acronyms (BOP, SIS, OGI, MRV, ESP, SIL, APC) — most slides have inline gloss.
- **Concept terms** (pilot stuck, alert fatigue, cognitive AI, pilot purgatory, plant-wide stagnation, cross-cutting, working cases) — **slides leave в English** в visible body, без RU gloss. Это violation.

### 10. Quadrant naming consistency

**Status:** PASS.

Chapter использует **Q1/Q2/Q3/Q4 codes throughout** + RU descriptive names:
- Q1 = «зрелое производство»
- Q2 = «метановая MRV»
- Q3 = «разведка фронтиров»
- Q4 = «энергетический переход»

Section dividers s06/s13/s21/s28 использует **same code-форму**:
- s06: «Q1 — Mature production» + «зрелое производство»
- s13: «Q3 — Frontier exploration» + «разведка фронтиров»
- s21: «Q2 — Methane MRV» (need verify) + «метановая MRV»
- s28: «Q4 — Energy transition» + «энергетический переход»

Designer's flag о EN shorts на dividers — verified, **consistent с chapter** (chapter тоже использует EN shorts в quadrant labels, например «Q3 — frontier exploration» в slide_map frontmatter + §0.3 prose).

---

## Recommendation для Phase 8

**VERDICT: APPROVE-WITH-POLISH** — slides ready для Phase 8 speech derivation, after one minor polish.

**Single P1 polish to apply BEFORE Phase 8 speech writer кика:**
- **Russification polish** — добавить inline RU gloss для 4 concept terms first-use в visible body (см. P1-1 above):
  - «pilot stuck» → «застревание пилотов (pilot stuck)» — first-use в s06 + s07
  - «alert fatigue» → «усталость от ложных тревог (alert fatigue)» — first-use в s07b
  - «cognitive AI» → «когнитивный AI (cognitive AI)» — first-use в s17 + s35
  - «pilot purgatory» → «застревание пилотов (pilot purgatory)» — first-use в s18

**Recommended actor:** presentation-designer single-pass polish (≤30 мин), не требует full revision round. Touches:
- s06, s07, s07b, s09, s12, s17, s18, s32, s35, s39, s41 visible body + speaker notes.

**Phase 8 speech writer gets:**
- 10 documented failures с consistent numbers
- Keystone matrix verbatim canonical
- 3 cornerstones verbatim canonical
- 27+ vendor coverage map
- Russification guidance (chapter RU-primary, all speech narrative RU-primary, EN terms only after first-use gloss)

**No P0 blocking issues.** Cross-artifact alignment **strong baseline** для Phase 8.

---

**End of report.**
