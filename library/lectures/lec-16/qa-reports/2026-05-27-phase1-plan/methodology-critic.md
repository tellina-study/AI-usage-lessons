# Methodology critique — plan-v1 Лекция 16

**Дата:** 2026-05-27
**Object:** `notes/lecture-16-review/2026-05-27-phase1-plan/plan-v1.md` (7 927 слов, 568 строк)
**Verdict:** **REVISE**

## Summary

Plan v1 — методически серьёзный документ с честной AI-judgment ориентацией, явным keystone (Variant B data×physics matrix), well-mapped failure budget и тщательным Russification + hero + anonymization подготовкой. Однако **6 P1 issues** требуют фиксов перед chapter draft (counter-check: ≥5 P1 ⇒ verdict REVISE, не APPROVE-WITH-POLISH). Главные риски:

1. **Failure-share 30.0% strict-in slides точно на границе** — единственный реклассификационный шаг (например, s11 = «86% pilot» как mixed pilot-pattern slide вместо pure failure) обрушивает метрику <30% → REVISE при Phase 3 critic. Plan сам это признаёт в Risk 2, но mitigation недостаточен — нужен **structural buffer ≥32%**, не «add 1 slide if check fails».
2. **Keystone-axis Q2 vs Q3 confusion** — Plan Risk 1 идентифицирует, но не решает. Студент 3 курса БЕЗ нефтегаз-домена не интуитивно поймёт, почему methane plume = «low physics certainty» (atmospheric physics закрыта, а fusion modalities — нет). Нужна **explicit operational definition «physics certainty» = «есть ли установившаяся численная модель, дающая ground truth»** на самом s05, а не только в speech.
3. **Раздел 5 (Россия + cybersecurity + 2020 crash в 10 минутах / 5 слайдах) compressed** — s37 пытается смержить 3 структурных темы (cybersecurity +935%, 2020 oil crash 107k jobs, Deepwater Horizon якорь). Это slot для критического содержания (failure bucket), а не «прочее».
4. **Раздел 6 closing/Q&A — 9 минут / 3 слайда — buffer 0%.** s40 = Q&A 10 минут, но pacing уже забит. Нет 5-10% буфера на overflow.
5. **Tools-per-quadrant taxonomy → speech check не закрыт.** Plan §-named «Plan §-named speech-narrative → слайд check (Phase-5)» — заявление, не enforcement. Нет mapping таблицы «vendor → slide ИЛИ spoken anchor». OspreyData, SLB Avocet, Halliburton DecisionSpace, Aker Carbon Capture, Eavor, Sage, Quaise, Татнефть, ЛУКОЙЛ, Сургутнефтегаз — name-dropped но не закреплены за slide/anchor.
6. **6 «здесь AI не нужен» критериев — 4 явных + 2 «inline»** (#5 stripper wells inline в s12, #6 custody transfer inline в s26). Это маскировка структурного критерия в caveat — критик Phase 3 может счесть как partial / disclaimer, не judgment.

Базовая ось правильная, structure coherent, anonymization clean, Russification таблица comprehensive. **REVISE — не REJECT.** Структурный gap небольшой, focal — failure-share buffer + Q2/Q3 definition + Раздел 5 distribution + speech-narrative→slide enforceability table.

## P0 issues (BLOCKING)

**None.** Нет структурных gaps уровня P0. Keystone предъявлен в Разделе 0 на s05 ДО первых quadrant погружений (Раздел 1 = Q1, начинается на s06). AI-Failure bucket ≥30% present (на границе, но present). Chapter target 30 000 слов — explicit. Anonymization clean. Tools-per-quadrant taxonomy present. Все ENFORCED-правила курса в plan acknowledged.

## P1 issues (HIGH — fix before chapter draft)

### P1-1. Failure-share 30.0% strict-in slides — **на границе threshold без structural buffer**

**Где:** plan-v1.md строки 286-300 + Risk 2 (строки 557-561).

**Issue:** 12/40 slides = 30.0% exact. Если Phase 3 methodology-critic реклассифицирует s11 как mixed (например, «86% pilot stuck» это **claim**, а не **named failure cap**; или Cognite IPO postpone маркируется inline в s11, не отдельным failure cap) — метрика падает к 27.5%-29% и triggers REVISE.

Plan Risk 2 говорит «mitigation: если упадёт, добавить s07 caveat → full failure slide ИЛИ конвертировать s38 синтез в failure synthesis». Это **reactive mitigation, не proactive structural buffer.** AI-Failure Rule is fundamental, holistic — нельзя ждать критика, чтобы зафиксить.

**Counter-check:** Plan заявляет minutes 33.3% и chapter 40% as «comfortable cushion». OK для chapter/minutes — но **slides — самый visible артефакт** для USER GATE B; именно тут попадёт пользователь. На границе 30% — пользователь увидит «12 из 40» и заметит. Нужен либо 32%+ buffer на slides, либо честная reclassification как структурное.

**Fix proposal:**
- **Option A (preferred):** Добавить 2 slides → 14/40 = 35%. Кандидаты:
  - **s07b** «Aspen Mtell alert fatigue caveat + threshold tuning failures» (full caveat slide, splits s08 alert fatigue note в самостоятельный structural failure).
  - **s38b** «4 квадранта × 4 failures synthesis matrix» (вместо single s38 synthesis — две slides: одна — keystone return; вторая — failure synthesis).
- **Option B:** Reclassify s09 Honeywell UOP Connect или s28 Northern Lights как hybrid success+structural-limit (Honeywell scope vs 700 global refineries denominator; NL 0.02% needed scale baseline) — но это **partial bucket**, не strict-in, не засчитывается per CLAUDE.md решение #78.

**Severity rationale:** P1 (не P0) потому что метрика technically meets; но без buffer — single critic shift → REVISE downstream.

---

### P1-2. Keystone-axis Q2/Q3 confusion — operational definition «physics certainty» на s05 missing

**Где:** plan-v1.md строки 96-106 (keystone-слайд description) + Risk 1 (строки 551-555).

**Issue:** Plan Risk 1 идентифицирует риск:

> Студент-инженер 3 курса может не понять, почему methane plume physics — «low certainty». Atmospheric methane physics частично закрыта (известны диффузия, photochemistry); но **cross-source fusion physics + multi-sensor methane attribution** — open.

…но mitigation defers к speech + chapter («s05 keystone text expanded»; «chapter §intro spends 500-700 слов»). Это **insufficient on slide itself.** s05 — это keystone-слайд (the foundational mental model). Если на слайде не написано чётко, что «physics certainty» означает в Q2, студент будет blocked в Разделе 3.

Это методический gap на **самом keystone слайде**, что unique-risk — вся лекция спускается с этой оси.

**Fix proposal:** s05 description в plan должен быть extended:
- **Title:** «Когда AI работает в нефтегазе? Матрица: данные × физика»
- **1-я строка под title:** «От frontier exploration до methane MRV — AI имеет 4 разных profile»
- **Operational definition box (bottom-left на матрице):** «Physics certainty = есть ли установившаяся численная модель, дающая ground truth. Q3 (Eclipse, simulators): да. Q2 (multi-modal methane fusion): нет — physics частично закрыта, но cross-source attribution — open ML problem».
- **Bottom bar:** оставить «За каждым AI deployment — alternative tool: Eclipse simulators, OGI cameras, классическая интерпретация»

Plan строка 99 («1-я строка под title») должна это explicit отразить — иначе designer не передаст student.

**Дополнительно:** Q2 как термин в plan — иногда «high data + low physics» (s05), иногда «methane MRV» (Раздел 3 связка). Это разные axes coordinates vs section-name — может путать designer + critic. Plan должен **lock notation**: «Q1=mainstream production, Q2=methane MRV, Q3=frontier exploration, Q4=energy transition» с reference в каждом mention.

---

### P1-3. Раздел 5 «Россия + cross-cutting» — overcompressed (5 slides / 10 min для 3 структурных тем + cybersecurity failure)

**Где:** plan-v1.md строки 262-270 + open question #2 (строка 532-плюс).

**Issue:** Раздел 5 содержит:
- s33 section divider
- s34 Газпром нефть Cognitive Geo (geology 3-4 месяца → минуты, +40% projects к 2030)
- s35 Роснефть Digital Field (Башнефть, 23 software products)
- s36 Cognitive Pilot + Татнефть/ЛУКОЙЛ/Сургутнефтегаз
- s37 cybersecurity (+935% ransomware, Colonial Pipeline, Shell MOVEit) + 2020 oil crash 107k jobs + (chapter якорь) Deepwater Horizon

**s37 несёт 3 разных failure clusters в 1 слайде — это методически перегружено.** Cybersecurity counter-trend (failure 10 в plan budget), 2020 oil crash (failure 7 в plan budget), Deepwater Horizon historical anchor — это **3 отдельных pedagogical units** mashed into one slide за ~2 min lecturing time. Это нарушение cognitive load principle (max 3-5 новых концептов на 5 минут lecture).

Pacing: 5 slides × 10 min = 2 min/slide average — но s33 section divider = 0.5-1 min, s37 = 3 min, остальные = 2 min/slide. Если s37 = 3 min, остаются 2-2.5 min на 3 case slides (s34/s35/s36) — это compressed для Russia-specific deep-dive.

**Plan open question #2 признаёт это:** «Раздел 5 — 10 минут, 5 слайдов — слишком много compressed?»

**Fix proposal — Option A (preferred):** Реорганизовать Раздел 5 в 6 слайдов / 11 minutes:
- s33 section divider — 0.5 min
- s34 Газпром Cognitive Geo — 2.5 min
- s35 Роснефть Digital Field — 2 min
- s36 Cognitive Pilot + ЛУКОЙЛ/Татнефть/Сургутнефтегаз — 1.5 min
- s37a **Cybersecurity counter-trend** (+935% ransomware, Colonial 2021, Shell MOVEit, Dragos/Claroty defensive AI lag) — 2 min
- s37b **2020 oil crash + industry cyclicality** (107k jobs, BP 10k, Shell 9k) → connects к AI hype cycle vs industry reality — 1.5 min

Total: 10 min ⟶ 11 min. Steal 1 min из Раздел 0 (8→7 if cover/lecture-map tight) или Раздел 6 (Q&A 9→8 acceptable if we move 1 question to seminar).

**Option B:** Move Deepwater Horizon якорь полностью в chapter (где плановое — strings 335-336), **drop из s31 reference** ; cybersecurity и 2020 crash остаются в s37 (но clearly как 2 sub-units).

---

### P1-4. Q&A buffer 0% — Раздел 6 9 минут с s40 Q&A не имеет overflow buffer

**Где:** plan-v1.md строка 274-276 + 278.

**Issue:** 75-min total = 75 budget = no buffer. Plan strings 272-276:
- s38 synthesis (return to keystone) — implicit 2-3 min
- s39 closing + hero + bridge к Lec-17 — implicit 1-2 min
- s40 Q&A — implicit 4-6 min

Если Q&A длится 10 minutes (плановое в plan строка 276 «s40 (Q&A): дедицированный Q&A слайд (БЕЗ «10 минут»)»), lecture overflows. Course conventions per Лекция 11/12/13/14 — buffer 5-10% (3.5-7.5 min) для Q&A overflow.

**Fix proposal:** Pacing math должна явно reserve buffer. Возможные:
- Tighten Раздел 0 to 7 min (s03 audience tag — 30 seconds, s04 lecture-map — 1 min sufficient).
- Tighten Раздел 5 (если P1-3 fix берёт минуту обратно).
- Explicitly state в plan «Q&A — 6-8 min discrete + buffer overflow 2 min от sections выше».

Без явного buffer plan — overflow risk near 100% (per Лекция 4/9 lessons).

---

### P1-5. Tools-per-quadrant taxonomy → speech check не enforceable

**Где:** plan-v1.md строка 202-204 («Plan §-named speech-narrative → слайд check (Phase-5)»).

**Issue:** Plan заявляет:

> Каждый named vendor в этом списке появится **либо** на слайде, **либо** в spoken anchor с explicit `[FACT-CHECK]` маркером в speech.md.

Это **claim, не enforcement**. В Tools-per-quadrant таксономии **38 vendor names** (Q1: 6 vendor; Q3: 7; Q2: 8; Q4: 6; cross-cutting: 8; Russia: 5+). Slides list (Outline) явно covers ≈ 22 brand names (Ambyint s07, Aspen s08, Honeywell UOP s09, Роснефть s10, Eni s14, Exxon s15, Aramco+SLB s16, BP+Beyond Limits s17, IBM+Repsol s18, Eclipse/INTERSECT/CMG s19, MethaneSAT s21+s22, Carbon Mapper+GHGSat s23, FLIR+Picarro s26, Northern Lights s28, Fervo s29, Yokogawa s31, Honeywell DeltaV s32, Газпром s34, Роснефть s35, Cognitive Pilot s36, Colonial+Zscaler+Dragos s37).

**Missing slide / spoken-anchor enforcement для:** OspreyData, SLB Avocet, Halliburton DecisionSpace, Precision Drilling AlphaAutomation, NOV NOVOS, ExxonMobil + Aramco + Shell cloud partners (Azure/AWS), AMD vs NVIDIA contest, HPE Cray integration, Eavor, Sage Geosystems, Quaise Energy, Aker Carbon Capture, Bridger Photonics (aircraft LiDAR — 4× точнее ground OGI), SeekOps, Project Canary, Teledyne FLIR vs Opgal vs Rebellion Photonics, LI-COR vs Picarro, Roxar (post-2022 exit), AIQ partnership detail, Татнефть АнтиХрупкий, ЛУКОЙЛ Volga-Ural, Сургутнефтегаз.

Без explicit table-of-coverage (which vendor → which slide ИЛИ which line-in-speech), Phase 5 (designer) или Phase 9 (speech-writer) могут **drop half эти named vendors** quietly → orchestrator грипает: «где Bridger Photonics? plan его упоминал в Q2 tools». Это Лекция 4 lesson — отраслевая taxonomy требует enforcement.

**Fix proposal:** Plan section «Tools-per-quadrant taxonomy» добавляет **Coverage table** в конец:

| Vendor | Quadrant | Slide OR speech-anchor | Why mentioned |
|---|---|---|---|
| Ambyint InfinityRL | Q1 | s07 (slide) | +15% RL производство 200 wells |
| Aspen Mtell | Q1 | s08 (slide) | 10 days saved + alert fatigue caveat |
| OspreyData | Q1 | speech-anchor s09 contextualized | independent operator, без public KPIs |
| ... |  |  |  |
| Eavor closed-loop | Q4 | speech-anchor s29 supplement | next-gen EGS, funding rounds |

Минимум — vendors из «Доминирующие вендоры» каждого квадранта (~15 names) explicit-mapped. Остальные — может быть omitted с явным «not in scope» в plan note.

---

### P1-6. 6 «здесь AI не нужен» критериев — 2 маскированы как inline (caveat в s12, s26) вместо отдельных structural criteria

**Где:** plan-v1.md строки 351-358 (таблица 6 критериев).

**Issue:** 6 критериев таблица:
1. Mature field + Eclipse — s12 (full slide)
2. Safety-critical SIL3/SIL4 — s32 (full slide)
3. OGMP Level 5 compliance — s26 (full slide)
4. Frontier exploration без analog — s19 (full slide)
5. Stripper wells <10 bopd — s12 **inline**
6. Custody transfer metering — s26 **inline**

Критерии #5 и #6 — это not «inline caveat», а **separate structural criteria** (different physics + economics → different decision). Stripper wells ≠ mature field criterion (это про unit-economics + ROI threshold, не про technological maturity). Custody transfer ≠ OGMP compliance (это про regulatory mass flow metering accuracy class 0.2 vs ML estimation, разные categories).

**Risk:** Phase 3 methodology-critic может flag «6 criteria announced, 4 явных + 2 caveats» как «criteria masquerading as inline disclaimer» → **AI-Failure & Judgment Share Check** counts these как partial (not strict-in per решение #78).

**Fix proposal — Option A:** Promote #5 (stripper wells) до отдельной clause в s12 (не «inline», а bullet visible на slide); promote #6 (custody transfer) до отдельной clause в s26.

**Fix proposal — Option B:** Если slide real-estate constrained, decrement to 4 critical criteria explicit + 2 supplemental inline (clearly marked в plan как supplemental).

Either way: **plan документ должен** distinguish (a) **structural «AI не нужен» criteria** (4 cases, 4 slides full coverage) vs (b) **supplemental inline edge-cases**. Currently plan blends.

---

## P2 issues (LOWER — polish, можно отложить)

### P2-1. Anonymization — generic «РГУ нефти и газа / Тюменский ГНГУ» **mentioned in anonymization section as «не упоминать»**

**Где:** строки 393.

**Issue:** Анти-список «НЕ упоминать МГТУ / Бауман / ИУ-N / Кафедра / ВКА Можайского / МАИ / СПбГУ / **РГУ Губкина** / Сколтех / МФТИ / МГУ / **РГУ нефти и газа** / **Тюменский ГНГУ**».

«РГУ Губкина» = «РГУ нефти и газа имени И. М. Губкина» — это **одна институция**, перечислена дважды (разные имена). Plan чист в intent (anti-list inclusive), но для downstream subagent prompt это noise.

**Fix:** Consolidate в одно («РГУ нефти и газа (РГУ Губкина) / Тюменский ГНГУ / любые отраслевые нефтегазовые ВУЗы»).

### P2-2. `[VFY-day-of]` markers count = 10 — high risk если Phase 3 fact-check timeline tight

**Где:** строки 192-199 + Risk 3 (строки 564-567).

**Issue:** Plan flags 10 volatile numbers для day-of verification. Это много, и Phase 3 fact-checker имеет finite bandwidth. Mitigation в Risk 3 говорит «приоритет: METABRAIN, Subpart W». 

**Fix (P2 не P1):** Plan документ должен **rank** 10 markers по priority в Risk 3, не только «critical 2 + остальные». Например:
- **Tier-1 (must verify before chapter):** METABRAIN params, US EPA Subpart W status, Aramco realized value.
- **Tier-2 (verify before slides):** Discovery 6 capex, Cognitive Pilot installations, GHGSat satellite count.
- **Tier-3 (day-of):** Cognite ARR, Honeywell UOP within-year target, IRA Waste Emissions Charge.

### P2-3. Hero s01 fallback «Deepwater Horizon controlled burn» — caveat «catastrophe-framed»

**Где:** строка 459.

**Issue:** Plan acknowledges «может слишком catastrophe-framed для opening» — OK acknowledgement, но не предлагает 2nd fallback. Если Tier-1 NASA VIIRS не достижим (rare, но possible), и Deepwater Horizon ditched, designer должен иметь next option.

**Fix (P2):** Plan строка 459 → добавить 2nd fallback: «или alternative hero — Eagle Ford / Bakken VIIRS plumes (NASA Earth Observatory, 2024)» — same source family, less catastrophic framing.

### P2-4. Slide-маркеры `[for-slide-sNN]` mentioned в Phase 2 notes but без actual policy в plan

**Где:** строка 543.

**Issue:** Notes для downstream phases (строка 543) говорит «Slide-маркеры `[for-slide-sNN]` на каждом ≥150-слов разделе». Это правильное (per Лекция 11+ pattern), но plan не дает coverage map в самом plan (e.g., «§Q1 production optimization в chapter → [for-slide-s07, s08, s09, s10, s11, s12]»).

**Fix (P2):** Add to plan «Notes для downstream phases» — explicit chapter section → slide-маркеры mapping.

### P2-5. Open question «s38b failure synthesis» — already overlaps с P1-1 buffer fix

P2-1 признаёт что s38 synthesis может конвертироваться в 2 slides. Это consistent с P1-1 proposal. P2 status — defer to P1-1 resolution.

---

## Зоны критики (per area)

### 1. Keystone-axis quality

**Verdict: PASS WITH P1-2 FIX.**

- Variant B (data×physics) — strongest distinctive choice для нефтегаза per research 04-keystone-axis-options.md decision matrix (4 variants compared).
- Раздел 0 (s01-s05) предъявляет ось ДО первого погружения. s05 keystone-слайд после hook (s01) + cover (s02) + about (s03) + lecture-map (s04). Раздел 1 (Q1) начинается на s06 после keystone reveal — correct sequence per CLAUDE.md ENFORCED rule.
- Каждый раздел маппирован к квадранту (Раздел 1=Q1, Раздел 2=Q3, Раздел 3=Q2, Раздел 4=Q4) — нет drift.
- **P1-2 fix required:** operational definition «physics certainty» должна быть **на самом s05** (не только в speech/chapter). Без этого Q2 vs Q3 confusion = methodology-critic Phase 7 flag.
- Backup option Variant A (value chain) честно сравнено в research, отвергнуто с conscious rationale — методически legitimate.
- Section order: Q1 → Q3 → Q2 → Q4 (Разделы 1-4) — это descent from «AI multiplier» к «AI essential» к «AI struggles» — pedagogically narrative arc OK. Но **alternative ordering (Q1 → Q2 → Q3 → Q4) тоже defensible** (data-rich first, sparse data later); plan не объясняет выбор Q1→Q3→Q2→Q4. **P2 polish:** explicit rationale в plan для section order.

### 2. AI-Failure & Judgment ≥30%

**Verdict: BORDERLINE — needs P1-1 fix.**

- Slides 30.0% exact (12/40) — на границе, без buffer.
- Minutes 33.3% (25/75) — comfortable.
- Chapter 40% (~12k/30k) — comfortable.
- Holistic distribution: failures distributed по 5 sections (R1=2, R2=3, R3=3, R4=2, R5=1) — нет single-cluster concentration. PASS per CLAUDE.md.
- 10 documented failures table comprehensive; 6 fundamental limits map clean; 6 alternatives map clean; 6 «здесь AI не нужен» criteria present (но 2 inline — P1-6 fix).
- **Counter-check:** strict-in % vs partial — plan correctly applies решение #78 (strict-in only, partial→out). 30.0% slides уже только strict-in.
- **Risk:** методический critic Phase 3 при reclassification 1 slide → fall <30%; **fix P1-1** mandatory для safety buffer.

### 3. Section structure

**Verdict: BORDERLINE — needs P1-3 + P1-4 fixes.**

- 7 разделов (0-6) coherent flow.
- Pacing math correct (75 min = 8+12+13+13+10+10+9).
- Раздел 5 overcompressed — P1-3 fix.
- Раздел 6 buffer 0% — P1-4 fix.
- s38 synthesis pattern (return to keystone) per Лекция 12/13/14 — correct, но опасно single-slide для 4 квадрантов × 4 takeaways (P1-1 alternative fix предлагает split в s38a+s38b).
- s39 hero MethaneSAT global map — bridges к Lec-17 «systematization»; appropriate forward link.

### 4. LO quality

**Verdict: PASS.**

- 8 LO (LO16.1 — LO16.8) — measurable + action verbs (объяснить, различать, назвать, сравнить, применить).
- Each LO ties к specific раздел: LO16.1 (intro Раздел 0), LO16.2 (keystone), LO16.3-LO16.4 (Разделы 1-4 квадранты), LO16.5 (alternatives via Раздел 1-4), LO16.6 (criteria s12+s19+s26+s32), LO16.7 (Раздел 3 регуляторика), LO16.8 (Раздел 5 Россия).
- Aligned с курсовыми LO1/LO2/LO3/LO7 (frontmatter строка 8).
- **Exit ticket Q1-Q3 discriminative:** Q1 (which quadrant essential + why classical physics insufficient) — non-trivial; Q2 (2 documented failures + lessons) — actionable recall; Q3 (3 criteria when NOT to use AI) — judgment-level Bloom. Good.
- **Bonus Q4-Q6** для seminar — appropriate depth.
- **Minor:** LO16.3 «2-3 vendor per квадрант с adoption direction словами (растёт/стагнирует)» — связана с P1-5 (если vendor coverage не enforced, LO16.3 невыполним).

### 5. Tools-per-quadrant

**Verdict: BORDERLINE — needs P1-5 fix.**

- Per quadrant 2-4 vendors named: Q1 (6 vendors), Q2 (8), Q3 (7), Q4 (6) — all ≥ minimum.
- Mode ≠ brand distinguished partially: «predictive maintenance (mode) ≠ Aspen Mtell (brand)» — explicit в Q1 anti-hype. «Foundation model (mode) ≠ SLB Lumi (product)» — implicit, not explicit; **P2 polish**.
- Adoption direction phrasing («растёт» / «стагнирует» / «discontinued») — present для most vendors.
- Anti-hype caveats per quadrant — present, structural.
- Brand allowlist для Russification — comprehensive (companies + products + standards + Russian-specific + acronyms with gloss).
- Volatile numbers `[VFY-day-of]` marked — 7 specific items in §Volatile numbers строки 192-199.
- **P1-5 missing:** vendor → slide-or-speech-anchor enforcement table.

### 6. Baseline / counterfactual

**Verdict: STRONG.**

Sample claims:
- Ambyint +15% production: baseline «per-well historical mean (типичная Permian well 100-500 bopd)» — explicit (s07).
- Aramco $1.8B realized: baseline «vs Aramco revenue $440B = 0.4%» — explicit (s16).
- Honeywell UOP 310+ units / 100+ sites: baseline «total global refineries ~700» — explicit (s09).
- Eni HPC6 606 PFLOPS Top500 #5: baseline «из ~500 supercomputers = top 1%» — explicit (s14).
- ExxonMobil Discovery 6 $1B unlock: baseline «6 FPSO из 16B BOE total ≈ 30-40% capacity» — explicit (s15).
- Northern Lights 1.5 Mt/год: baseline «vs IEA target 7.6 Gt = 0.02%» + «vs global current ~40 Mt/год = 190× scale-up gap» — strong (s28+s30).
- Fervo 150 GW US potential: baseline «vs current US geothermal 3.7 GW = 40× growth» — explicit (s29).
- Cybersecurity +935% ransomware: baseline period «между апрелем 2024 и апрелем 2025» — temporal anchor.
- 2020 oil crash 107 000 jobs: baseline «BP 10 000, Shell 9 000» — example breakdown.
- Роснефть +1 Mt/год: baseline «vs Башнефть total ~17 Mt/год 2023 = +5.9%» — explicit (s10/s35).
- 86% pilot stuck: baseline «60% material value (BCG) + 15% live ops (DNV/Accenture) + 3% advanced» — multi-source triangulation.

**All measurable claims have inline baseline или counterfactual.** Plan demonstrates strong baseline mandate compliance (per memory rule `feedback_baseline_counterfactual`).

**Minor:** MethaneSAT 410 t/h Permian = «50% выше EPA estimates» — baseline EPA inventory ~4 Mt vs MethaneSAT 15 Mt → 4× discrepancy framed. Good. But «3.6 Mt/год» (s21 calculation 410 t/h × hours) — derived number; chapter should show derivation.

### 7. Hero + media plan

**Verdict: PASS.**

- s01 Permian VIIRS night satellite (NASA, public domain, Tier 1) — foreshadows Q2 methane MRV; visible scale промышленности 2 593 plumes 2024. **Foreshadow logic explicit.**
- s39 MethaneSAT first global methane map (EDF/Google Feb 2026, Tier 1) — bittersweet payoff (lost but map remains); bridge к Lec-17 «systematization». **Bridge logic explicit.**
- ≥50% media slides target: plan claims 22/40 real photos + 13 self-rendered = 35/40 = 87.5% visual. Realistic per research (multiple T1/T3 sources identified).
- Backup s39: control room с human-in-loop (Tier 3-4). **P2 fix:** add 2nd s01 fallback (P2-3).
- 6-tier acquisition explicit (строка 519-524).
- Attribution labels mandatory (per `feedback_no_mock_fallbacks`).
- Lec-8 lesson («16 stylized mocks» fail) acknowledged.

### 8. Anonymization

**Verdict: PASS WITH P2-1 CLEANUP.**

- `audience` строго «студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)» — generic.
- Career section: «нефтегазовые компании + сервисные подрядчики + регуляторы + НИИ + операторы данных» — родовое.
- Anti-list comprehensive (но дубликат РГУ Губкина — P2-1).
- Cost-of-omission Лекция 9 (1 revision cycle) explicitly cited.

### 9. Russification prep

**Verdict: STRONG.**

- Top replacement table 30+ entries (foundation model / reservoir simulation / methane MRV / downhole / upstream/midstream/downstream / shut-in / curtailment / frontier exploration / basin / play / mature field / pilot purgatory / ESP / artificial lift / rod pump / gas lift / digital twin / ground truth / automation bias / multi-sensor fusion / decision-support / edge case / compliance / carbon accounting / black-box / hallucination / human-in-the-loop / etc.).
- Brand allowlist comprehensive (companies + products + standards + Russian + acronyms with gloss).
- Pre-GATE deep latin-token scan explicit (per `tools/presentation-build/README.md` §5.8).
- Cost-of-omission Лекция 8 (3 revision passes) cited.
- **Potential P2 add:** Bridger Photonics, SeekOps — отсутствуют в brand allowlist (companies section). Add для consistency.

### 10. Chapter depth realism

**Verdict: PASS.**

- Target ≥30 000 слов (CLAUDE.md ENFORCED для L4+ — Лекция 16 ∈ L4+).
- Multi-part split: 4 файла (chapter.md + chapter-part2.md + chapter-part3.md + chapter-part4.md), 7-8k слов each, ≤600 строк each (per Лекция 11 pattern).
- Failure-share 12 000 слов = 40% — distributed по 4 file parts (~3k per file in failure deep-dives + Раздел 5 1.5k). NOT concentrated в 1 part — PASS holistic check.
- Phase 2 brief explicit (строка 543).
- Phase 3 check explicit «word count <28 500 = P0 BLOCKING» (строка 544).

### 11. Open questions / risks

**Verdict: PARTIALLY ADDRESSED.**

- Risk 1 (Q2 physics certainty confusion) — identified, mitigation acknowledged but **not sufficient on s05 itself** — P1-2 escalation.
- Risk 2 (failure-share 30.0% borderline) — identified, mitigation reactive — **P1-1 escalation**.
- Risk 3 (10 `[VFY-day-of]` markers) — identified, prioritization sparse — **P2-2 polish**.
- 3 open questions от plan writer (строки 526+):
  - Q1 «Aramco METABRAIN parameter count progression» — high-priority `[VFY-day-of]`, P2-2 ranking.
  - Q2 «Cognitive Pilot installations 2024» — same.
  - Q3 «Раздел 5 — слишком много compressed?» — **YES, P1-3 escalation.**

Plan writer's open questions are **honest and matchable к critic findings** — это положительный сигнал, plan-writer не пытается скрыть проблемы.

### 12. Anti-patterns check

**Verdict: PASS.**

- **No timing/methodology в visible body slides:** Plan строка 543, 546 explicit «timing только в frontmatter/deck.yaml»; «no «методически важно» / «на этом этапе студент должен» / timing markers в visible speech». Plan-internal timing pacing math (строки 207, 215, 227, 239, 251, 262, 272, 278) — это **plan-internal pacing**, не «timing на visible slide» — это разрешено per CLAUDE.md (frontmatter/deck.yaml/plan files exempt).
- **No designer-extras language:** Plan не tells designer add «Лектору», «Вы здесь», subtitles, timing footer, callbacks — clean.
- **No magic-pill framing:** Plan структурно AI-judgment-oriented; нет «AI спасёт нефтегаз» / «AI — революция». Quadrant model honest по Q3+Q4 limitations.
- **No insider phrasing flags:** Quadrant labels Q1/Q2/Q3/Q4 — convention (per management literature 2×2 matrix), не insider; «physics certainty» = explicit research term (P1-2 fix добавит operational definition).
- **No anti-pattern grep matches:** «магическая пилюля» / «УГАДАЙ» / «инженер ИУ6» — 0 hits in plan body.

---

## Counter-check (4-level scale enforcement)

- **Failures share 30.0% strict-in:** BORDERLINE — pass technically, no buffer → P1-1 recommend buffer slides for safety.
- **Single-artifact concentration risk:** PASS — failures distributed across 5 sections (R1=2, R2=3, R3=3, R4=2, R5=1) + 40% chapter / 33.3% minutes / 30% slides — все 3 артефакта comply holistic ≥30%.
- **Keystone в section 0:** PASS — s05 = 5th slide в Разделе 0, после s01-s04 (hook/cover/about/lecture-map).
- **Tools-per-quadrant complete:** BORDERLINE — vendor names present per quadrant ≥2-4, но coverage mapping vendor → slide-or-speech enforcement missing (P1-5).
- **Baseline coverage:** PASS — все measurable claims sampled имеют inline baseline или counterfactual.

**P1 count: 6** (P1-1 failure buffer, P1-2 Q2/Q3 keystone definition, P1-3 Раздел 5 compression, P1-4 Q&A buffer 0%, P1-5 tools coverage enforcement, P1-6 «здесь AI не нужен» 2 inline) → ≥5 P1 ⇒ **verdict REVISE (per counter-check rule в methodology-critic.md «если ≥5 P1 issues но verdict = APPROVE-WITH-POLISH — STOP, change to REVISE»).**

---

## Rationale verdict

**REVISE — not APPROVE-WITH-POLISH** потому что 6 P1 issues, и **3 из них structural** (P1-1 failure buffer на самой границе, P1-3 Раздел 5 cognitive overload в s37, P1-5 tools coverage enforcement gap). Plan v1 — methodically serious, не require REJECT и не has P0 blocking gaps; но 6 P1 — это slightly выше threshold за «show-able с known caveats» (APPROVE-WITH-POLISH ≤4 P1 per methodology-critic rules).

**Что должно произойти для upgrade verdict'а:**
1. Plan v2 addresses 6 P1 issues (fix proposals above).
2. Specifically: failure-share buffer brings slides ≥32% (P1-1); keystone s05 has operational definition «physics certainty» on slide (P1-2); Раздел 5 reorganized to 6 slides / 11 minutes OR Deepwater Horizon moved out (P1-3); Q&A buffer 5-8% explicit (P1-4); vendor coverage table mapping every named vendor → slide-or-anchor (P1-5); criteria #5/#6 promoted to bullets visible on s12/s26 (P1-6).
3. P2 issues — polish, can defer без affecting verdict.

**Если P1-1/P1-2/P1-3 fixed → APPROVE-WITH-POLISH** даже если P1-4/P1-5/P1-6 partial.

**Если все 6 P1 fixed → APPROVE-CLEAN.**

---

## Recommendation для Phase 1 revision

### Plan v2 action list

**Required (для REVISE → APPROVE-WITH-POLISH):**

1. **P1-1 (failure buffer):** Either add s07b (Aspen alert fatigue full failure slide) OR split s38 → s38a (keystone return) + s38b (4-quadrant × 4-failures synthesis matrix). Target: **14/40 = 35% strict-in slides.**

2. **P1-2 (Q2/Q3 keystone definition):** Rewrite s05 description в plan строки 96-106 → add operational definition box:
   > «Physics certainty = есть ли установившаяся численная модель, дающая ground truth. Q3 (Eclipse, simulators): да. Q2 (multi-modal methane fusion): нет — physics частично закрыта, но cross-source attribution — open ML problem».
   This text должен быть **на slide visible body**, не только в speech/chapter.

3. **P1-3 (Раздел 5):** Choose Option A (split s37 → s37a cybersecurity + s37b 2020 crash, +1 slide +1 min) OR Option B (drop Deepwater Horizon из s37, move к chapter). Recommend Option A — cybersecurity и 2020 crash оба structural failures, deserve separate cognitive units.

4. **P1-4 (Q&A buffer):** Explicit pacing math redo: Раздел 0 = 7 min, Раздел 5 = 11 min (if P1-3 Option A), Раздел 6 = 9 min split as s38a (1 min) + s38b (1 min) + s39 (2 min) + s40 Q&A (5 min) → 75 + buffer 0; OR 76 total с steal 1 min from Раздел 6 для 5 min Q&A explicit + 3 min hardware buffer.

**Recommended but lower-priority (для APPROVE-CLEAN):**

5. **P1-5 (tools coverage):** Add «Coverage table» в Tools-per-quadrant section с vendor → slide/speech-anchor mapping для ≥15 primary vendors per quadrant.

6. **P1-6 (criteria #5/#6):** Promote stripper wells (#5) и custody transfer (#6) до visible bullets on s12 / s26 — не inline.

**Polish (P2, optional now):**

7. P2-1: Consolidate РГУ Губкина / РГУ нефти и газа anti-list duplicate.
8. P2-2: Rank 10 `[VFY-day-of]` markers in tiers.
9. P2-3: Add 2nd s01 fallback hero candidate (Eagle Ford / Bakken VIIRS).
10. P2-4: Add chapter section → slide-маркеры mapping в Notes для downstream phases.
11. P2-5: Add explicit section-order rationale (Q1→Q3→Q2→Q4 vs Q1→Q2→Q3→Q4).

---

**Files referenced:**
- `/tmp/lec-16-wt/notes/lecture-16-review/2026-05-27-phase1-plan/plan-v1.md`
- `/tmp/lec-16-wt/notes/research/lecture-16/04-keystone-axis-options.md`
- `/tmp/lec-16-wt/notes/research/lecture-16/03-failures-and-limits.md`
- `/home/levko/AI-usage-lessons/CLAUDE.md` (AI-Failure Rule, Chapter Depth, Anti-Patterns, Pre-USER-GATE)
- `/home/levko/AI-usage-lessons/tools/lecture-production/README.md` §3.6
