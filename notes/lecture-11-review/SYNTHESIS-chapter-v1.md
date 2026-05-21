# Phase 3 critique — synthesis для Chapter v1 (Лекция 11)

**Дата:** 2026-05-21
**Branch:** issue-127-lec-11-manufacturing
**Input:** chapter.md v1 (commit 9683655, 11 350 слов)
**Critics:**
- methodology-critic — REVISE, 7 P1, 5 P2 (commit 1918aed)
- fact-checker — REVISE, 3 P0, 10 P1, 4 P2 (commit 5aa22a9)
- reader-text-only — Mostly engaging, keystone PASS, 3 confusions (commit 41cdf2c)

---

## Combined verdict — **REVISE**

Counter-check: methodology поймал 7 P1 → принудительно REVISE per ENFORCED rule (≥5 P1). Fact-checker 3 P0 factual → MUST fix перед GATE A. Reader-text-only сигнализирует kernel главы работает (keystone PASS, Tesla opening works, 5-step framework golden) — структурно НЕ переписываем, **fix P0 факты + Russification deep + 5 P1 содержательных**.

**Keystone — Variant C — CONFIRMED valid** обоими critics. Failure-bucket strict-in methodology recount = **66.4%** (chapter words, не minutes; в речь упадёт до ~44% per plan v2). Distributed: min §3 54%, max §1 96.6%. ≥30% mandate с margin ~36 п.п. — **comfortably passed**.

---

## Block A — Fact P0 (3 — MUST FIX, factual errors)

### P0-1. §1.1 Deloitte 42% misattribution → reformulate
- **Current:** «42% компаний отказались от AI-инициатив (Deloitte)»
- **Fact:** Deloitte 2025 State of AI Enterprise = «42% strategy-prepared», не «abandoned»
- **Fix:** заменить на verified figure: **«S&P Global 2025: 46% PoCs scrapped before production»** ([source: S&P Global Market Intelligence AI Experiences Survey 2025]); либо softer reformulation без Deloitte attribution.

### P0-2. §3.6 AB InBev rolled-back — unverified
- **Current:** «AB InBev rolled back несколько AI-инициатив»
- **Fact:** AB InBev публично — success story (+60% filtration). Rollback не подтверждён публично.
- **Fix:** **REMOVE specific AB InBev rollback claim.** Заменить на category-level pattern: «отраслевая закономерность — много AI-внедрений на shop floor откатываются после пилота из-за operator-resistance, конкретные кейсы не раскрываются публично (NDA / репутация)». ИЛИ заменить на verifiable cultural-resistance кейс из research/04.

### P0-3. §3.6 Tata Steel rolled-back при смене сырья — unverified
- **Current:** «Tata Steel вернулся к классической оптимизации после смены сырья»
- **Fact:** Tata Steel — Smart Factory success-story (550+ models в production).
- **Fix:** **REMOVE Tata Steel attribution.** Generalize: «RL distribution drift — фундаментальный паттерн при смене сырья / batch transition; конкретные rolled-back кейсы редко раскрываются (industry-pattern, specifics not publicly disclosed)». ИЛИ — оставить как hypothetical illustrative example без named company.

---

## Block B — Methodology P1 (7 — significant, fix in revision)

### P1-1. Russification depth недостаточна (deep latin-token scan)
- **Findings:** baseline×19, production×38, controller×6, audit trail×8, foundation model×4, **typo «Манfacturing» (Cyrillic М + Latin «anufacturing»)**, plus 9 subheader-фраз в §1.3 на английском («Diffused strategy», «Cloud blunder», «Demo-to-production gap»).
- **Cost-of-omission lec-08:** ~83 мин revision если не закрыть.
- **Fix:** deep sweep — `baseline` → **«базовая линия»** (или «исходный уровень» где контекст не SE), `production` → **«промышленная эксплуатация»** / **«боевой контур»** (зависит контекста), `controller` → **«контроллер»** (или «управляющее устройство»), `audit trail` → **«журнал аудита»** / **«журнал прослеживаемости»**, `foundation model` → **«фундаментальная модель»** (canonical), `manufacturing` typo fix. 9 subheader §1.3 — RU-canonical formulations:
  - «Diffused strategy» → «Рассеянная стратегия» / «Размытая стратегия»
  - «Cloud blunder» → «Облачная ошибка» / «Облачный просчёт»
  - «Demo-to-production gap» → «Разрыв между демо и эксплуатацией»

### P1-2. OT/IT divide thin (one bullet vs fundamental status)
- **Plan v2 P1-5 mandate:** OT/IT divide должен иметь insert-points §1.1 + §4.2 + connection к §3.4.
- **Current:** одно упоминание (§1.1 bullet #4), §3.4 не возвращается к OT/IT lens.
- **Fix:** добавить ~200 слов в §1.1 (fundamental определение: OT = операционные технологии, PLC/SCADA + детерминизм; IT = enterprise, cloud + flexibility; раскол = два мира с разными SLA, security model, тимы) + §3.4 explicit connection (FDA Part 11 / ATEX лежат именно на OT-стороне, edge AI приходится bridge) + §4.2 одна строка в alternative matrix (PLC vs edge ML — это OT vs OT+IT bridge).

### P1-3. §4.3 Pfizer Vox worked example — 4 «Pass» без отсечения
- **Issue:** LO8 Apply+Create требует рамку **как фильтр**, не валидатор. 4 Pass + 3 строки counter — не учит «когда не работает».
- **Fix:** добавить **second mini-worked-example** (~150-200 слов), где рамка **отсекает** AI-применение. Example: **«Predictive maintenance для авиадвигателя на коробке передач, MTBF 8 лет, SIL 2»** — fail на Step 3.A (cost эталонной разметки превышает выгоду от prediction; малая выборка отказов; safety-critical → MPC + RCM лучше). Show рамка работает в обе стороны.

### P1-4. §3.5 Норникель vs §1.1 OEE-критерий self-consistency gap (reader-confusion, methodology too)
- **Issue:** §3.5 утверждает Норникель «in industrial-operation stage» — но §1.1 определяет OEE-критерий как «доказан в production с >12 мес SLA». Self-contradiction или намеренно?
- **Fix:** либо explicit «Норникель — пример где industrial-operation ещё не = доказан-в-production по строгому OEE-критерию» (научный честный hedge), либо удалить «in industrial-operation stage» phrasing и оставить как «pilot stage публично подтверждено».

### P1-5. §0.2 vs §3.3 ISA-95 edge POSCO consistency
- **Issue:** §0.2 говорит edge AI на L1, §3.3 говорит «между L1 и L2».
- **Fix:** unify — POSCO 180 edge nodes operate **«между L1 (sensors) и L2 (SCADA)»**, edge AI не имеет фиксированного ISA-95 уровня (это новый L1.5 / OT-edge).

### P1-6. §2.1 5 концептов unpacked (mislabeling / active learning / multi-rater / abstain / uncertainty)
- **Issue:** 5 концептов в 3 предложения — packed too tight для self-study.
- **Fix:** unpack в ~150 слов с двумя примерами per концепт (mislabeling = «один дефект annotated 3 разными labelers получает 2 разные класса»; active learning = «модель просит labeler метить именно те 100 фото где uncertain»; multi-rater = «5 labelers → mediante consensus»; abstain = «модель отказывается классифицировать → escalate to operator»; uncertainty = «sigmoid output 0.55 = abstain threshold»).

### P1-7. Q&A backup 10 → 8 trim
- **Issue:** mandated 8, doddered 10. Q9 «маленький завод» drifts к управленческой теме.
- **Fix:** trim до 8: keep самые engineering-релевантные, drop Q9 (маленький завод management drift) + Q7 (LLM в process control — overlap с §1.2).

---

## Block C — Fact P1 (10 — should-fix, source hygiene)

### P1-F1. Foxconn Wisconsin 13K vs 10K headlines
- **Fix:** «Walker promised 13 000 (potential), Assembly memo 10 000, scaled back to <1 500 by 2024; actual delivered ~281 jobs до пересмотра (NPR 2020)».

### P1-F2. F-35 ALIS $44k/hour year
- **Fix:** добавить «$44k/час в FY2018 baseline (CBO); снижено до ~$35K по FY2024».

### P1-F3. Hyundai 30 000 Atlas year
- **Fix:** «production target 2028» (chapter говорит 2026 announcement event — correct, но 30K — это 2028 production scale).

### P1-F4. BASF Geismar -30% defects
- **Fix:** soften до «отраслевые ROI cases дают порядок -20-30%» если direct BASF source не найден.

### P1-F5. POSCO +5%/-10%/+3% specifics
- **Fix:** verify через Manufacturing Digital / POSCO IR; если не подтверждено — soften phrasing.

### P1-F6. TSMC +10-15% yield
- **Fix:** verify Indium blog primary + TSMC IR; если не подтверждено — оставить только 95% accuracy.

### P1-F7. Норникель Газпром нефть Северо-Соленинское conflation
- **Fix:** clarify — Норникель собственные операции vs Газпром нефть services.

### P1-F8. СИБУР маркетплейс Q1 2025
- **Fix:** verify launch; если не confirmed — phrase «объявлено», не «запущено».

### P1-F9. КАМАЗ «10 в коммерческой перевозке на М-11»
- **Fix:** verify count.

### P1-F10. `[VFY-day-of]` add для трёх claims (Foxconn Liu 80%, Toyota GAIA 10K, POSCO 180).

---

## Block D — Methodology P2 + Fact P2 (apply if cheap)

- **P2-M1.** §3.5 КАМАЗ Маяк-2.5 — автономные грузовики не на пересечении discrete/process; либо переформулировать как «dual-use» либо переместить в §2.3 коботы/автономия.
- **P2-M2.** §0.2 глоссарий точно 6 — confirm count matches plan v2 (ISA-95, PLC, SCADA, MES, OEE, soft sensor).
- **P2-M3.** §1.2 Honeywell aviation MRO — статус-маркер «roadmap [VFY-day-of]».
- **P2-M4.** §3.2 mermaid CIRL — chapter включает mermaid syntax в код-блоке (academic reference acceptable, но можно вынести в slides notes).
- **P2-M5.** §4.2 matrix как Markdown table — OK для chapter, в slides будет visual.
- **P2-F1.** IBM Watson Health tone «за остатки» — soften.
- **P2-F2.** HMGMA «Брайан» typo → «Брайан-Каунти, Эллабелл».
- **P2-F3.** Pertama Partners citation [10] — secondary OK для RAND aggregator.

---

## Block E — Reader confirmations (carry-forward stable)

- ✅ Tesla 2018 + 2024 двойной opening — works strongly, central question pulls reader.
- ✅ §3.2 CIRL «PID inside RL, не вместо» + mermaid — лучший architectural explainer.
- ✅ §5.2 четыре вопроса к вендору (baseline / окно / перечень / OEE) — golden, лучший take-away.
- ✅ Keystone test PASS — «эта глава учит суждению о применимости AI в производстве через ось дискретное vs процессное» через 2 недели.
- ✅ «CV inspection — последняя линия защиты, не первая» + «Latency = determinism, not speed» + 5-шаговая рамка + 4 вопроса к вендору — это unique take-away.

**Сохранить эти 5 элементов как stable anchors в chapter v2 без изменений.**

---

## Block F — Что НЕ менять (kernel stable)

- ❌ НЕ переписывать keystone (Variant C — Discrete vs Process — confirmed valid обоими critics).
- ❌ НЕ менять 5-section structure / pacing.
- ❌ НЕ менять Tesla opening / 5-step framework / 3 vendor questions.
- ❌ НЕ менять LO mapping (5 LO covered).
- ❌ НЕ менять failure-bucket distribution (passed mandate comfortably).

---

## Phase 4 revision brief (для book-editor v2 spawn)

**Priority order:**
1. **Fact P0 (3) — MUST FIX:** Deloitte / AB InBev / Tata Steel.
2. **Russification deep sweep + 9 subheaders §1.3 + typo «Манfacturing»** (cost-of-omission Лекция 8 lesson).
3. **OT/IT divide deepen** (§1.1 + §3.4 + §4.2) — Plan v2 P1-5 mandate completion.
4. **§4.3 second mini-worked-example** (battery PdM filter case, ~150-200 слов).
5. **§3.5 Норникель self-consistency** (либо honest hedge либо удалить industrial-operation claim).
6. **§0.2 ↔ §3.3 ISA-95 edge POSCO unify** (L1.5 / between L1 and L2).
7. **§2.1 5 концептов unpack** (~150 слов с примерами).
8. **Q&A 10 → 8** (drop Q9 + Q7).
9. **10 Fact P1 source hygiene fixes.**
10. **Apply 5+3 P2 if cheap** (КАМАЗ §2.3 move, IBM tone soften, HMGMA spelling, [VFY-day-of] markers).

**Estimated effort:** single book-editor spawn ~40-50 мин (full citation sweep на revised chapter — ENFORCED §3.6 lecture-production README).

**Output target:** `library/lectures/lec-11/chapter.md` v2 (status: reviewed), ~11.5-12k слов (slightly выше из-за OT/IT deepen + §4.3 second example + §2.1 unpack).

**После Phase 4:** Phase 4.5 pre-USER-GATE walkthrough → USER GATE A.
