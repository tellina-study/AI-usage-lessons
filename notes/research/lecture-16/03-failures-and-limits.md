# Провалы, ограничения и альтернативы: AI в нефтегазе

**Назначение.** Документированные failures + фундаментальные limits + критерии «здесь ИИ не нужен» + alternative не-AI инструменты. Это ≥30% бюджета лекции (per AI-Failure & Judgment Content Rule). Каждый случай — что обещали, что вышло, что выучили, с baseline где возможно.

## Структура

- §1. Documented failure cases (corporate-level)
- §2. Fundamental limits AI в нефтегазе
- §3. Критерии «здесь ИИ не нужен / не применим»
- §4. Alternative (не-AI) инструменты
- §5. Историческая каноническая катастрофа (Deepwater Horizon)

---

## §1. ДОКУМЕНТИРОВАННЫЕ ПРОВАЛЫ

### 1.1. BP + Beyond Limits cognitive AI ($20M, 2018-?)

**Что обещали (2018):**
- BP стал largest client + investor; $20M инвестиций.
- AI «absorb learnings of geologists and petroleum engineers and imitate their decision-making».
- Технология из deep space exploration missions (NASA JPL roots) — для offshore exploration.
- «Accelerate operational insight and process automation across operations».

**Что вышло (2018-2025):**
- Публичных результатов roll-out не объявлено за 7 лет.
- Beyond Limits переключился с oil&gas на general industrial AI; пивот в healthcare, manufacturing 2023+.
- BP не обновил кейс на сайте после 2019 (нужна верификация [VFY-day-of]).
- 2020 oil crash + BP «Beyond Petroleum» rebrand → digital teams restructured.

**Выученный урок:**
1. **«Cognitive AI» (symbolic + ML hybrid) обещанная generalizable autonomy НЕ материализовалась** в нефтегазе. Это был ML-marketing 2018 epoch.
2. Single-customer investor (BP) — concentrated bet, vendor pivot оставил BP без commercial product.
3. **«Имитировать decision-making геологов»** = anthropomorphic overpromise. Реальные геологи делают decision на основе implicit knowledge которые тяжело кодифицировать.

### 1.2. IBM Watson + Repsol Kalimba (2014-2017+)

**Что обещали (2014):**
- 30 лет exploration data analyzed Watson cognitive.
- Запуск результатов «в первой половине 2016».
- IBM Cognitive Environments Laboratory (NYC) + Repsol Technology Centre (Madrid).

**Что вышло (2016-2022):**
- Конкретных результатов и метрик публично не объявлено.
- IBM Watson Industry Solutions — широкая stagnation 2018-2022 (см. также Watson Health unwound 2022).
- Repsol перешёл на собственные ML tools — Repsol Lumen platform (2020+, без IBM).
- Партнёрство тихо завершилось.

**Выученный урок:**
1. **General-purpose «cognitive computing» platforms** (Watson era) НЕ scaled в narrow domain как O&G exploration.
2. **30 лет data analyzed** — звучит впечатляюще, но без specific business question metric выводы не actionable.
3. **Hype cycle 2014-2016** (Watson «winning Jeopardy») → реальное commercial use дает ≤10% от ожиданий.

### 1.3. Cognite IPO postpone (2023 → 2025+)

**Что обещали (2021-2023):**
- Cognite (spin-off из Aker BP, 2017) — IPO planned 2023, valuation $2-3B.
- ARR rapidly growing; «digital twin platform для всех industrial verticals».

**Что вышло (2023-2025):**
- **IPO cancelled 2023** из-за market conditions, capital intensive growth.
- Continues burn cash несмотря на ARR $94M (2024, +40% YoY).
- **871 employees April 2026** (после restructuring); Aker ASA earnings calls 2024-2025 — IPO timing uncertain.
- Aker BP остаётся anchor customer (260k time series, 1.5 trillion data points в Cognite Data Fusion).

**Выученный урок:**
1. **Industrial AI SaaS** vertical в O&G — недостаточно стандартизированный TAM для прибыльного scale.
2. Aker BP — anchor «friendly customer» оплачивает развитие, но **independent monetization** проблематична.
3. **ARR growth ≠ profitability** — burn rate vs revenue ratio критичен; Cognite не достиг unit economics.

### 1.4. C3.ai oil&gas vertical declining (2024-2025)

**Что обещали (2018-2021):**
- Strategic partnerships с **Shell** (ML for trading, predictive maintenance), **Baker Hughes** (BHC3 JV), **Engie**.
- BHC3 JV — joint venture Baker Hughes + C3.ai для oil&gas vertical AI.

**Что вышло (2024-2025):**
- **FY24:** Oil&Gas vertical **5.9% от revenue** (~$18M из $310M total).
- **FY25:** «non-Oil&Gas revenue +48% YoY» → **O&G declining absolute terms**.
- BHC3 JV restructured к 2023 — Baker Hughes отступил от exclusive partnership.
- C3.ai сам стек испытывает: shifted к Federal/Defense vertical для роста.

**Выученный урок:**
1. **Industry-specific vertical AI компании** в нефтегазе не достигли scale в эпоху hyperscalers + foundation models.
2. **Generic foundation models (SLB Lumi, Aramco METABRAIN)** едят рынок vertical specialists.
3. **«Strategic partnership»** ≠ revenue traction; Baker Hughes JV не стал commercial product.

### 1.5. MethaneSAT loss (июнь 2025) — Y2025 mission failure

**Что обещали (март 2024 launch):**
- $88M+ mission, EDF + Harvard, first env-NGO-owned satellite.
- High-precision wide-area methane measurement; precision 500 kg/h.
- 5+ years operational design life.

**Что вышло:**
- **Контакт потерян 20 июня 2025** — через ~13 месяцев работы (15% of designed lifetime).
- Loss attributed to spacecraft anomaly (детали не публичны).
- 2 000+ data files released, 10 scientific papers, 180+ scenes — но primary mission interrupted.

**Выученный урок:**
1. **Single-satellite mission** = catastrophic single point of failure для regulatory MRV infrastructure.
2. **Even with successful launch + good first-year data**, hardware reliability — fundamental constraint.
3. **Regulatory enforcement (EU Methane Reg)** не может опираться на 1 satellite; resilience needs constellation (GHGSat 16 satellites — better model).
4. **AI без stable upstream data source** не работает; methane regulators теперь scramble к alternative data sources (Carbon Mapper Tanager-1).

### 1.6. AI pilot-to-production gap (McKinsey 2024 / BCG 2025) — индустриальный паттерн

**Что обещали (industry-wide 2018-2022):**
- Все super-majors: «AI добавит $X billion value к нашим operations».
- McKinsey 2020: AI добавит **$425B value к global O&G к 2030**.
- Pilots flourished (>1000 piloted AI projects по different operators).

**Что вышло (2024-2025):**
- **McKinsey 2024: ~86% AI projects в energy НЕ выходят из pilot phase**.
- BCG: 60% компаний не получают «material value» от AI investments.
- DNV/Accenture 2024: **15%** O&G professionals говорят их орг used AI в live day-to-day ops; **3%** report «highly integrated, advanced use».
- **47%** AI use остаётся в planning/piloting stage.
- Energy market — только **21% орг** имеют data quality для production-grade AI.

**Причины структурные:**
- **60-80% AI project time** = data cleaning, not modeling.
- Legacy IT system integration cost **3-5× initial AI software cost**.
- Talent gap — нужны люди понимающие и AI, и domain (geology / drilling / refining).
- Organizational resistance + risk-averse safety culture.
- **Slow ROI realization** — O&G планирует на 20-30 лет horizon, не quarterly.

**Выученный урок (фундаментальный):**
- **Pilot ≠ production**. Большинство демонстраций AI на одном well / pad / unit не масштабируются на 1000+ wells.
- **Без data foundation, AI = vapor**.
- **86% failure rate** — это не «AI плохой», это «вертикаль НЕ готова к production-grade AI без серьезной infrastructure prework».

### 1.7. 2020 oil crash + digital team cuts

**Что было до:**
- 2018-2019: super-majors агрессивно набирали digital/AI teams.
- BP «Beyond Petroleum» (2017+) — digital innovation теми.
- Shell New Energies + technology accelerators.
- Chevron CTO + digital transformation office.

**Что вышло (март-октябрь 2020):**
- **107 000 jobs lost** в US O&G/chemicals (Deloitte).
- **BP: 10 000 layoffs** (15% workforce), digital teams sliced.
- **Shell: 9 000 layoffs**, including digital и new energies team.
- **Chevron, ExxonMobil, ConocoPhillips** — major cuts.
- Cognite, C3.ai pipelines compressed.
- **Многие AI projects сворачивались** или становились maintenance-only.

**Выученный урок:**
- **Industry cyclicality > AI hype cycle**. Oil price ниже $30 — digital teams cuts first (non-essential).
- **Talent loss** — после 2020 senior digital practitioners moved к tech, finance; recovery slow.
- **2021-2024 recovery** не вернула pre-2020 staffing levels; AI initiatives консолидированы у super-majors которые могли позволить.

### 1.8. Methane MRV crisis — Industry vs Regulator (2024-2025)

**Discrepancy:**
- **MethaneSAT measurements: US O&G methane эмиссии 4× выше EPA estimates** (15 Mt vs ~4 Mt EPA inventory).
- **Permian:** 50% выше official EPA.
- **OGI ground surveys vs aerial:** aerial 4× выше OGI на тех же sites (BC validation).
- **9-satellite single-blind test (2024):** 0 false positives, но только **58% correctly identified**; **41 false negatives** (missed real emissions).

**Что это значит:**
- Industry reporting based на EPA emission factors **systematically underestimates**.
- Satellite + aerial AI **detection methods inconsistent друг с другом**.
- **No agreed ground truth** — методологические fights между operators, regulators, NGOs.

**Выученный урок:**
- **AI MRV — promising, но НЕ ready для contract enforcement** без cross-validation protocols.
- **EU Methane Reg 2024/1787** требует OGMP 2.0 Level 4/5 — но это де-факто mandates triangulation (satellite + aerial + ground).
- **Regulator-Industry disagreement** на factor 4 — это **structural gap**, не engineering polish.

### 1.9. Refinery AI process control — stagnation в complex multi-physics

**Что обещали (2010s-2020s):**
- Yokogawa Idemitsu: «AI controllers will autonomously operate complex units».
- Honeywell, ABB, Emerson — AI-augmented APC (advanced process control).

**Что вышло (2024):**
- Real-world deployment **на narrow loops** (single column controls, one heater) — успешно.
- **Cross-unit / plant-wide AI orchestration** — стагнирует, не достигла unmanned vision.
- Один Idemitsu case study — упоминается как demonstration, не norm.

**Выученный урок:**
- **Multi-physics constraints** (mass + energy + reaction kinetics + corrosion) — ML суррогаты теряют consistency на edge cases.
- **Operator override остаётся** required regulation в большинстве jurisdictions.

### 1.10. Cybersecurity AI counter-trend (2024-2025)

**Контекст:**
- Ransomware attacks на oil&gas **+935% между April 2024 и April 2025** (Zscaler).
- Causes: OT/IT convergence создает attack surface; AI/digital deployment **увеличивает attack surface**.
- Colonial Pipeline 2021 — caused by flat OT/IT network, no MFA on VPN.
- Shell MOVEit breach 2022; 2024 vendor compromise customer data leak.

**Гэп:**
- AI deployments в нефтегазе **редко включают AI-security-by-design**.
- Defensive AI (anomaly detection в OT) отстаёт от offensive AI (automated reconnaissance, phishing).

**Выученный урок:**
- **AI добавляет complexity → attack surface растёт**.
- **Безопасность** должна быть phase 1, не phase 4.

---

## §2. ФУНДАМЕНТАЛЬНЫЕ ОГРАНИЧЕНИЯ AI в нефтегазе

### 2.1. Sparse data + frontier exploration

**Проблема:**
- Каждое scientific well = **$50-100M cost** (offshore deepwater).
- Нельзя «собрать ещё data». Sample size for frontier basin ≈ 1-5 wells.
- ML modelям нужны ≥1000s samples; transfer learning от established basins **не generalizes** на новую geology (Tarim vs Permian — radically different mineralogy, pore physics).

**Последствие:**
- Frontier exploration: **AI augments, но НЕ replaces** classical interpretation.
- Foundation models trained на Permian → fail on East African Rift basin (no analog).

### 2.2. Black-box models в HSE решениях

**Проблема:**
- Safety-critical decisions (blowout prevention, evacuation triggers) требуют **traceability** и **auditability**.
- ML model — «black box»; нельзя в regulator подтвердить «почему» решение было принято.
- EU Methane Regulation 2024/1787 — explicit audit trail mandates.

**Последствие:**
- ML в HSE остаётся **decision-support**, не **decision-authority**.
- Industry uses **physics-based deterministic** для BOP, alarm systems (SIL3/SIL4 certified).

### 2.3. Cost asymmetry: cost-optimization vs safety AI

**Проблема:**
- AI для cost optimization (production, drilling speed) — успех = +5-15% efficiency.
- AI для safety (alarm prediction, BOP control) — успех = **0 incidents**; одна missed event = catastrophe.
- **Different ROI structures, different criteria** — confused при общем «AI in O&G» narrative.

**Последствие:**
- Vendors продвигают AI для cost (easier ROI story); regulators ограничивают AI для safety.
- **Operators confuse** оба применения → AI deployment без structural HSE distinction.

### 2.4. Long planning horizons vs short-term ML model decay

**Проблема:**
- Field life **20-30 лет**; reservoir properties slowly evolve.
- ML models trained на historical production decay 1-2 года (data drift).
- **Maintenance overhead** — нужен continuous retraining.

**Последствие:**
- **TCO для ML model lifecycle** часто > savings от ML predictions.
- Cognite Data Fusion problem — keep all data fresh, retrain models requires significant data engineering staff.

### 2.5. Multi-physics simulation surrogate gap

**Проблема:**
- Reservoir simulation = coupled fluid + heat + chemistry + geomechanics.
- ML surrogate (deep learning trained на Eclipse/INTERSECT/CMG output) — accelerates 50-80% calendar time, но...
- **Loses physical consistency** на extrapolation: new injection scenarios, new well placement → unphysical results (negative pressures, mass violation).

**Последствие:**
- **Physics-informed neural networks (PINN)** — попытка решить, но scale to industrial reservoir пока research-grade.
- Operators **сохраняют classical simulators** как ground truth, ML = screening.

### 2.6. Hallucination в LLM-based agents для production

**Проблема:**
- LLM operator-assistant tools («Lucy», SLB Lumi agents) — hallucinate в edge cases.
- **Gartner 2027 prediction: 40% agentic AI projects fail** из-за cost overruns + poor risk controls.
- O&G operations — high-stakes; one wrong recommendation → equipment damage, safety event.

**Последствие:**
- **Human-in-loop mandatory** для agentic AI в production.
- Trust calibration — operators либо over-trust (skip review) либо under-trust (ignore) — оба плохо.

---

## §3. КРИТЕРИИ «ЗДЕСЬ ИИ НЕ НУЖЕН / НЕ ПРИМЕНИМ»

### 3.1. Хорошо известная geology + proven reservoir

**Когда не нужен AI:**
- Mature field, история production 30+ лет, well-characterized.
- Classical reservoir simulation (Eclipse) + experienced reservoir engineers → достаточная accuracy.
- AI добавляет complexity без material lift.

**Альтернатива:** Eclipse / INTERSECT / CMG + experienced team.

### 3.2. Safety-critical deterministic решения

**Когда не нужен AI:**
- Blowout prevention (BOP control).
- Pressure relief valve sizing.
- Emergency shutdown logic (SIS — Safety Instrumented Systems).
- Fire suppression activation.

**Почему:** регуляция требует SIL3/SIL4 certification = deterministic, traceable, auditable. ML невозможно certify под current frameworks (ISA-84, IEC 61511).

**Альтернатива:** Physics-based + rule-based + redundant hardware (3oo2 voting, etc.).

### 3.3. Compliance reporting под EU Methane Regulation

**Когда не нужен AI:**
- Source-level emissions quantification под OGMP 2.0 Level 4/5 — ground OGI + portable analyzer + verified mass balance.
- ML estimation **не приемлемо** как primary methodology — нужна direct measurement.

**Почему:** Regulator audit requires explainable provenance. AI estimate = «derived value» с uncertainty bands — не accepts как «measured».

**Альтернатива:** Hand-held OGI cameras + portable Quantification (Picarro, LI-COR) + mass balance computation.

### 3.4. Frontier exploration без analog data

**Когда не нужен AI:**
- New petroleum basin (first wildcat); zero training data.
- Salt-related plays (Gulf of Mexico ultra-deepwater) — каждый case unique.
- Pre-salt Brazil — early exploration was geological interpretation, ML now applicable только после 5-10 wells.

**Альтернатива:** Senior geophysicist + classical seismic interpretation + analog basin reasoning.

### 3.5. Operational decision на edge / cost-justifiable

**Когда не нужен AI:**
- Stripper wells (<10 bopd output) — лекторное предупреждение per well низкий, ML deployment ROI отрицательный.
- Small operators без data infrastructure.

**Альтернатива:** Rule-based monitoring, periodic field visits.

### 3.6. Когда proxy (cheap sensor + AI) ≠ replacement direct measurement

**Когда AI не подходит:**
- Custody transfer metering — direct mass flow meter required (regulatory).
- Allocation между partner companies — direct measurement required.
- Allocation между jurisdictions для taxation.

---

## §4. ALTERNATIVE (не-AI / другой класс AI) ИНСТРУМЕНТЫ

### 4.1. Physics-based simulators (vs ML surrogate)

| Tool | Provider | Назначение |
|---|---|---|
| Eclipse | SLB | Industry standard reservoir simulation |
| INTERSECT | SLB | Next-gen high-resolution Eclipse |
| CMG (IMEX, STARS, GEM) | Computer Modelling Group | Compositional, thermal, EOR |
| OpenFOAM | open-source | CFD; CCS modelling |

**Когда использовать:** mature reservoirs, complex EOR, hydraulic fracturing modelling, regulatory submissions требующие physics traceability.

### 4.2. Optical Gas Imaging (OGI) cameras + human inspectors (vs satellite AI)

| Tool | Provider | Назначение |
|---|---|---|
| FLIR GFx320 | Teledyne FLIR | Hand-held OGI camera |
| Opgal EyeCGas | Opgal | Hand-held QOGI (quantification) |
| Rebellion Photonics | Honeywell | Fixed hyperspectral |

**Когда:** EPA Method 21, EU LDAR programmes, OGMP Level 5 verification, custody-grade measurement.

### 4.3. LiDAR + classical CV (vs deep learning) для ROW monitoring

- **Aerial LiDAR** (e.g., Riegl, Optech) — pipeline ROW vegetation encroachment, third-party intrusion detection.
- Classical CV + edge detection + rule-based — proven, less false positives than deep learning в low-data regimes.

### 4.4. Domain expert geology + classical interpretation

- **Senior petroleum geologists** with 20+ years experience + classical seismic interpretation (Kingdom, Petrel manual).
- Implicit knowledge не codifiable в ML — pattern recognition based на geology training.

### 4.5. SCADA + classical control loops (vs ML controllers)

- **PID loops + override controllers** — proven, certifiable, regulator-friendly.
- **APC (Advanced Process Control)** — model-based, deterministic, in-between classical и ML.
- Honeywell Profit Controller, Emerson DeltaV — APC mainstream alternatives к ML.

### 4.6. Federated learning + privacy-preserving ML (vs centralized AI)

- Когда data sharing impossible (cross-operator competition):
- **Federated learning** — share model updates, не raw data.
- **Differential privacy** — add noise to outputs.
- Только early-stage в O&G; demonstrated в banking, healthcare.

---

## §5. ИСТОРИЧЕСКАЯ КАНОНИЧЕСКАЯ КАТАСТРОФА — DEEPWATER HORIZON 20 АПРЕЛЯ 2010

**Не AI failure напрямую, но автоматизация + human factors lessons.**

### Что произошло
- Macondo well, BP-operated, Transocean rig в Gulf of Mexico.
- Negative pressure test misinterpreted.
- Gas kick → blowout → explosion → 11 deaths, 4.9 million barrels spilled в 87 дней.
- **$60+ billion** total cost для BP, criminal charges, decade of cleanup.

### Automation + alarm lessons (relevant к AI today)
1. **Alarm system bypassed** — general alarm set to bypass «to prevent waking workers with false alarms». Когда methane shot вверх, **no audio/visual warning** → workers had no escape signal.
2. **Independent alarms — no coordinated automation**. Каждый sensor отдельная sigма, **no cross-correlation** chain that would say «3 sensors anomalous → trigger alarm».
3. **Operator response — confusion**. Andrea Fleytas (23, bridge officer, <2 years rig experience) видела massive alarm panel, не уверена что triggering response — afraid causing «false alarm» disrupting operations.
4. **Negative pressure test misinterpretation** — кстати classical engineering test (не AI); but team complacent, missed signal.

### Lesson для AI в HSE today
1. **Alert fatigue REAL** — Aspen Mtell claim «eliminates» это marketing. False positives **disable trust** в систему; затем real positive missed.
2. **Cross-sensor correlation** — AI strong (vs independent alarms 2010). **Но** AI requires verification + audit trail.
3. **Operator training matters больше чем AI sophistication**. Junior operator с simple system > senior с complex AI.
4. **Bypass culture** — Macondo bypass был «temporary», стал permanent. AI alarms — operators будут bypass если false positive rate высокий.

### Pattern repeats?
- Texas City refinery explosion 2005 (BP) — automation + alarm + human factors.
- Buncefield 2005 (UK) — tank overflow, gauge failed.
- San Bruno pipeline 2010 (PG&E) — SCADA missed.
- **Pattern:** complex automation + insufficient operator training + alarm tolerance erosion = catastrophe.

**AI добавляет complexity** — без structural improvements в operator training и organizational safety culture, AI просто ускоряет old failure modes.

---

## §6. SUMMARY — Что забрать в Phase 1 plan

### 6.1. Сильнейшие failure cases для chapter (по nominee)

1. **86% AI projects pilot stuck** (McKinsey 2024) — structural pattern, не one-off.
2. **BP + Beyond Limits** — single-vendor concentrated bet, vendor pivot.
3. **2020 oil crash → digital cuts** — industry cyclicality > hype.
4. **MethaneSAT loss июнь 2025** — recent, high-profile, regulatory infrastructure dependent.
5. **C3.ai O&G vertical declining** — vertical AI loses к foundation models.
6. **Cognite IPO postpone** — industrial AI SaaS unit economics not proven.
7. **Methane MRV factor 4 discrepancy** — engineering trust crisis, regulatory enforcement gap.
8. **IBM Watson + Repsol** — early cognitive overpromise.
9. **Refinery AI process control stagnation** — multi-physics constraints fundamental.
10. **Cybersecurity ransomware +935% 2024-2025** — AI counter-trend, attack surface growing.
11. **Deepwater Horizon 2010 — historical anchor** для automation + human factors.

### 6.2. Сильнейшие limits

- Sparse data (1 well = $50-100M).
- Black-box vs HSE auditability.
- Cost-asymmetry cost-optim vs safety.
- Long horizons vs model decay.
- Multi-physics surrogate inconsistency.
- LLM hallucination в high-stakes ops.

### 6.3. Сильнейшие critéria «AI не нужен»

- Mature fields + experienced engineers.
- Safety-critical deterministic logic (SIL3/SIL4).
- Compliance reporting requires direct measurement.
- Frontier exploration без analog data.
- Stripper wells (cost-asymmetry).
- Custody transfer metering.

### 6.4. Сильнейшие alternatives

- Eclipse/INTERSECT/CMG (vs ML reservoir surrogate).
- OGI hand-held + portable quant (vs satellite AI MRV).
- Senior geologist + classical interpretation (vs AI auto-interpretation).
- PID + APC (vs ML controllers).

---

## Источники

- [BP-Beyond Limits partnership 2018](https://www.bp.com/en/global/corporate/news-and-insights/press-releases/bp-invests-in-new-artificial-intelligence-technology.html)
- [JPT BP+Beyond Limits cognitive AI](https://onepetro.org/JPT/article/70/10/26/208584/BP-and-Startup-Beyond-Limits-Try-To-Prove-That)
- [IBM Watson + Repsol 2014 launch](https://medium.com/@oilandgas360/ibm-watson-not-just-for-winning-jeopardy-e5d1270fdfac)
- [McKinsey 86% AI pilots stuck (in BCG analysis)](https://www.bcg.com/publications/2025/ai-first-future-of-oil-and-gas-companies)
- [Pilot-to-production 33% scaling rate](https://astrafy.io/the-hub/blog/technical/scaling-ai-from-pilot-purgatory-why-only-33-reach-production-and-how-to-beat-the-odds)
- [Hidden truth AI in O&G (15% live ops, 3% advanced)](https://www.domesticoperating.com/blog/2025/04/17/the-hidden-truth-about-ai-in-oil-and-gas/)
- [2020 oil crash 107k jobs (Fortune)](https://fortune.com/2020/10/05/oil-gas-jobs-transition-climate-coronavirus/)
- [2020 oil crash CNN coverage](https://www.cnn.com/2020/10/08/business/oil-gas-jobs)
- [MethaneSAT loss June 2025](https://www.methanesat.org/project-updates/2025-was-year-highs-lows-and-hope-methanesat)
- [Cognite IPO uncertain 2025 (Seeking Alpha)](https://seekingalpha.com/article/4748220-aker-asa-cognite-ipo-pushed-out)
- [Aker BP + Cognite Atlas AI (260k time series)](https://www.cognite.com/en/customers/aker-bp)
- [C3.ai FY24/FY25 oil&gas decline](https://www.sec.gov/Archives/edgar/data/0001577526/000162828025028158/ex991-fy25xq4earnings.htm)
- [Methane MRV 4× discrepancy (MethaneSAT vs EPA)](https://www.methanesat.org/project-updates/new-data-show-us-oil-and-gas-methane-emissions-over-four-times-higher-epa-estimates)
- [9-satellite single-blind methane test 2024](https://amt.copernicus.org/articles/17/765/2024/amt-17-765-2024.pdf)
- [BC LDAR aerial vs OGI 4× discrepancy](https://www.highwoodemissions.com/bulletin/research-digest-017/)
- [Deepwater Horizon alarm bypass (EHS)](https://www.ehs.com/blogs/deepwater-horizon-an-ongoing-lesson-in-safety/)
- [Deepwater Horizon human factors (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0925753514001076)
- [Colonial Pipeline cyber attack lessons](https://www.proarch.com/blog/the-colonial-pipeline-attack-lesson-learned)
- [Ransomware O&G +935% 2024-2025](https://www.cybersecuritydive.com/news/zscaler-ransomware-report-manufacturing-targeted/756147/)
- [BOP physics-based vs probabilistic safety](https://www.sciencedirect.com/topics/engineering/blowout-prevention)
- [Sparse data + AI generalization O&G](https://pubs.acs.org/doi/10.1021/acsomega.3c09229)
- [Agentic AI hallucination risk (DataRobot)](https://www.datarobot.com/blog/llm-hallucinations-agentic-ai/)
- [LLM agent hallucination survey 2025](https://arxiv.org/html/2509.18970v1)
- [Reservoir simulation Eclipse INTERSECT CMG comparison](https://www.petropt.com/articles/reservoir-management-software-guide/)
