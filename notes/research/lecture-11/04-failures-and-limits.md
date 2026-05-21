# 04 — Провалы, фундаментальные ограничения и анти-кейсы (failure-bucket ≥30%)

**Summary.** Цель файла — фундамент failure/judgment-блока лекции (≥30% strict-in контента). Каждый кейс содержит: (1) что произошло (документировано); (2) выученный урок; (3) правильная альтернатива / границы применимости / критерий «здесь AI не нужен / не работает». Структура — 8 разделов: hype-collapse, Tesla over-automation, CV-границы, predictive maintenance reality, RL distribution drift, cultural/organizational rejections, regulatory blockers, fundamental physics-vs-ML limits + альтернативные инструменты.

**Принцип отбора.** Доступная публично документация. Никаких выдуманных цифр; если источник тяжело найти — помечено «требует дополнительной верификации». Каждый кейс дает ясный, защищаемый критерий **«здесь AI не нужен / не работает»**.

---

## 1. Hype-collapses: $4-7B сожжённые на корпоративных платформах

### 1.1 GE Predix — $4B+ investment, decade-long collapse (2011-2020)
- **Что произошло.** Predix — индустриальная IoT-платформа GE Digital, ядро 6-летней $4B трансформации GE в digital industrial under CEO Jeffrey Immelt. К 2017: digital revenue target — $15B к 2020. Реальность: revenue dropped to $12B target и далее **GE начал продавать digital business**.
- **Корневые причины (множественные).**
  1. **Diffused strategy.** «Be everything to everyone» — single platform для wide industrial verticals (aviation, healthcare, power, oil&gas) с разными data shapes, regulatory landscapes, integration patterns. Vendor lock-in между verticals не работал.
  2. **Cloud blunder.** Решили build their own Predix cloud data center — конкурировать с AWS/Azure/GCP. Поздно осознали, что это hopeless.
  3. **Pivot 2017.** John Flannery замораживает funding, нанимает investment company чтобы найти customers для digital division. К 2018 — pivot complete, продают части.
- **Урок.**
  1. **Industrial AI ≠ general cloud AI.** Domain-specific data, integration patterns, regulations требуют focus.
  2. **«Hardware company → software platform» — наиболее опасный pivot.** Cultural mismatch (DCF cycles vs SaaS cycles).
  3. **Размер инвестиций ≠ результат.** $4B+ потрачено, value not captured.
- **Альтернатива.** Build narrow domain-specific tools (predictive maintenance для конкретно gas turbines), не platform play. Partner с hyperscale clouds, не compete.
- **Источники:**
  - [boldbusiness.com — Predix hits rough water](https://www.boldbusiness.com/digital/predix-hits-rough-water/);
  - [raypcb.com — GE IoT lessons](https://www.raypcb.com/ge-iot/);
  - [medium.com — Lessons from GE Predix failure](https://medium.com/world-of-iot/lessons-to-learn-from-ges-iot-platform-predix-s-failure-4319bea5e3e7);
  - [platform9.com — Why digital transformations fail GE](https://platform9.com/blog/what-we-can-learn-from-ge-and-why-digital-transformations-fail/).

### 1.2 IBM Watson — manufacturing + healthcare scale-down (2018-2022)
- **Что произошло.** Watson Health «just managed to break even» в 2018 после massive layoffs. В 2019: IBM прекращает development & sales «Watson for Drug Discovery». Pusan National University Hospital + Keimyung University Dongsan Medical Center не renew Watson contracts. Watson Health финально продан за parts в 2022 (Francisco Partners за $1B — fraction исходных инвестиций).
- **Manufacturing-side**: Watson был промоутирован для factory floor с заявкой «-47% downtime, -48% defect rate». Production-scale deployment **не материализовался** в масштабе healthcare-Watson failure.
- **Урок.**
  1. **Demo-to-production gap.** Watson выигрывал Jeopardy! но не лечил пациентов и не оптимизировал production.
  2. **Marketing-driven sales of immature tech.** IBM продавал Watson как ready-product 5+ лет до того, как technology была готова.
  3. **Generalist vs specialist.** Watson обещал быть «AI for everything» — каждое vertical требовало custom integration, fewer wins, dispersed effort.
- **Альтернатива.** Focused specialist tools (e.g., Tempus в oncology, Verily в diabetes); или narrow industrial AI (Uptake, Augury в predictive maintenance).
- **Источники:**
  - [slate.com — IBM Watson sold off for parts](https://slate.com/technology/2022/01/ibm-watson-health-failure-artificial-intelligence.html);
  - [henricodolfing.com — $4B Watson Oncology failure](https://www.henricodolfing.ch/en/case-study-20-the-4-billion-ai-failure-of-ibm-watson-for-oncology/);
  - [Berkeley Corporate Innovation — Rise Fall Resurrection Watson](https://corporateinnovation.berkeley.edu/wp-content/uploads/2020/04/The-Rise-Fall-and-Resurrection-of-IBM-Watson-Health_final.pdf);
  - [eweek — IBM Watson Factory Floor](https://www.eweek.com/innovation/ibm-watson-thinks-its-way-to-factory-floor/).

### 1.3 Foxconn Wisconsin — «8th wonder of the world» → fish farming → Microsoft AI data center (2018-2024)
- **Что произошло.** Июнь 2018: Trump + Foxconn chairman Terry Gou groundbreaking в Mount Pleasant, WI. Заявка: $10B investment, 10 000+ jobs (LCD panel plant). Wisconsin Gov. Walker offered $3B subsidy. Trump: «8th wonder of the world».
- **Реальность 2024.** Промышленный сценарий **полностью обвалился**:
  - 10 000 jobs → ~1500 actual.
  - LCD large screens → smaller screens → AI hub → medical equipment → coffee kiosks → home alarm systems → Google servers → **fish farming + boat storage + handbag exportation considered** (документировано).
  - Mount Pleasant takes on hundreds of millions debt для infrastructure.
- **Foxconn-AI-pivot 2018.** Foxconn активно promoted AI factory of future в Wisconsin context. **Ничего из этого не материализовалось.**
- **Финал**: May 2024, Microsoft покупает site за $3.3B для AI data center «Fairwater» (использует землю Foxconn-failure, не industrial AI). Дополнительные $569M investment в 2025.
- **Урок.**
  1. **Political-driven mega-projects + AI buzzwords ≠ feasibility.** Tax incentives ($3B) перевесили industrial logic.
  2. **«Будем делать AI factory» — flexible promise.** Когда LCD не пошёл, Foxconn быстро переориентировался на «AI» — это был **marketing-shield**, не plan.
  3. **«8th wonder of the world» — anti-signal.** Если глава государства публично объявляет проект чудом — это **predicts failure**, не success.
- **Альтернатива.** Не tax-subsidize one-vendor mega-deals; cluster развитие через университеты и существующих employers.
- **Источники:**
  - [wisconsinwatch — Foxconn moving to AI 2025](https://wisconsinwatch.org/2025/12/wisconsin-foxconn-data-center-energy-trump-ai-congress-lawmakers-republican-democrat/);
  - [techspot — Microsoft repurposing Foxconn](https://www.techspot.com/news/109537-microsoft-repurposing-foxconn-failed-wisconsin-venture-world-most.html);
  - [nbcchicago — What happened to Foxconn $1.2B](https://www.nbcchicago.com/news/local/what-happened-to-foxconn-a-look-at-the-1-2-billion-spent-and-where-it-all-went/3759518/);
  - [fox6now — Foxconn Mount Pleasant 4 years later](https://www.fox6now.com/news/foxconn-mount-pleasant-lcd-plant-4-years-later);
  - [captimes.com — Foxconn fallout bitter politics](https://captimes.com/news/government/foxconn-fallout-includes-bitter-politics-in-mount-pleasant/article_1d3d4390-5f73-5c66-9bb9-06321fd76195.html);
  - [urbanmilwaukee — Mount Pleasant water shortfall](https://urbanmilwaukee.com/2022/01/21/back-in-the-news-mount-pleasant-pays-for-foxconn-water-shortfall/).

### 1.4 «Pilot purgatory» — 60-95% AI initiatives не достигают production (2025-2026)
- **Цифры (verifiable, multiple sources).**
  - **MIT Sloan 2025:** **95% GenAI pilots fail** to scale to production. Infrastructure limitations — 64% of scaling failures. Cost overruns average **380%** at production scale vs pilot projections. Median time pilot→production shutdown: **14 months**.
  - **RAND 2025:** **80.3% AI projects fail** to deliver intended business value. К концу 2025 — $547B из $684B investment delivered no business value.
  - **Deloitte 2025:** **42% компаний** abandoned at least one AI initiative в 2025. Average sunk cost per abandoned initiative: **$7.2M**.
  - **McKinsey State of AI 2025:** 78% organizations use AI; только **5.5%** — AI high performers (>5% EBIT impact); 2/3 — pilot purgatory; only 39% companies report any enterprise-level earnings impact.
  - **S&P Global 2025 survey:** average organization scrapped **46% of AI proof-of-concepts** before production.
- **Manufacturing-specific.** McKinsey «Digital Manufacturing — escaping pilot purgatory» (2023, обновлено 2024) — целое исследование посвящено этой проблеме именно в производстве.
- **Корневые причины.**
  1. **Data quality.** Manufacturing data — siloed, plant-specific, sensor drift, no standardised schemas.
  2. **Workflow rigidity.** Установившиеся процедуры (lean, Six Sigma) не подстраиваются под AI.
  3. **Operating model inertia.** Operations не имеют experimentation budget.
  4. **Measurement gaps.** Нет clear baseline для measuring AI impact.
- **Урок.**
  - **Pilot ≠ production.** Production требует 5-10x более качественных data, infrastructure, ops.
  - **Vendor-driven optimism inflates pilot results** — vendors показывают best-case demos, production reveals worst-case edges.
  - **«Pilot purgatory» — статистический default, не исключение.** Студент должен ожидать, что **большинство** AI-инициатив, что он встретит в начале carrera, окажутся в pilot purgatory.
- **Альтернатива.** Before pilot — define «go to production» criteria + measurable baseline. Если pilot успешен, но баseline plot/criteria не определены — production roll-out не нужен (sunk-cost trap).
- **Источники:**
  - [Pertama — AI Failure 80% 2026](https://www.pertamapartners.com/insights/ai-project-failure-statistics-2026);
  - [medium — 95% AI pilots fail MIT McKinsey](https://medium.com/generative-ai-revolution-ai-native-transformation/mit-says-95-of-ai-pilots-fail-mckinsey-explains-why-agentic-engineering-shows-how-to-fix-it-66a7bb2d8e0d);
  - [astrafy — Pilot Purgatory 33% production](https://astrafy.io/the-hub/blog/technical/scaling-ai-from-pilot-purgatory-why-only-33-reach-production-and-how-to-beat-the-odds);
  - [McKinsey — Digital Manufacturing escaping pilot purgatory PDF](https://www.mckinsey.com/~/media/mckinsey/business%20functions/operations/our%20insights/how%20digital%20manufacturing%20can%20escape%20pilot%20purgatory/digital-manufacturing-escaping-pilot-purgatory.pdf);
  - [McKinsey — State of AI 2025 PDF](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/2025/the-state-of-ai-how-organizations-are-rewiring-to-capture-value_final.pdf);
  - [hpcwire — AI progress slow McKinsey](https://www.hpcwire.com/aiwire/2025/11/12/ai-is-everywhere-but-progress-is-slow-mckinsey-explains-why/).

---

## 2. Tesla over-automation (2018) — canonical manufacturing-AI failure

### 2.1 Что произошло
В Q1 2018 Tesla имела target 2500 Model 3 cars/week. Реальность: **2020 Model 3 cars/week** к концу квартала. «Production hell» persisted months. Apr 13, 2018 — Elon Musk **tweets и intervjuew CBS**:
> «Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. **Humans are underrated.**» — @elonmusk, X/Twitter, 13 April 2018.

В том же интервью CBS — «We had this crazy complex network of conveyor belts and it was not working, **so we got rid of that whole thing**».

### 2.2 Что именно failed
- **Conveyor system for Model 3** — overly complex network of conveyor belts; Tesla **scrapped целиком** и заменили простой manual handling.
- **Robotic «fluffer» station** для попыток автоматически install fiberglass mats на batteries — не работала надёжно.
- **Battery module assembly** — Tesla автоматизировал слишком много стадий, что приводило к bottleneck при failure любого одного робота.

### 2.3 Корневая причина (IMD analysis)
- **Tesla overestimated automation, underestimated humans.**
- Humans на assembly line хороши в: variable contexts, troubleshooting, recovery от ambiguous situations.
- Roboты хороши в: repetitive, well-defined, high-precision, predictable operations.
- Tesla **тried заменить people в zones где human variability — это feature, не bug**.

### 2.4 Урок — структурный (для всей лекции)
1. **«Lights-out factory» — мираж для complex assembly.** Toyota, BMW, Volkswagen — все сохраняют human workers в assembly даже в 2026.
2. **Automation paradox.** Чем более автоматизирована линия, тем **более critical** оставшиеся human operators (Lisanne Bainbridge, 1983 — Ironies of Automation).
3. **Tesla — case-study, который изучают на MBA-курсах.** Является **исходной точкой** для любой дискуссии о manufacturing-automation.

### 2.5 Альтернатива
- **Toyota Production System (TPS) + Jidoka.** «Automation with a human touch». Jidoka = stops the line when defect detected; human verifies and fixes; AI/robots **release humans for higher-judgment tasks**, не replace them.
- **«Human in zones of variability + machines в zones of repetition».** Hard rule.

### 2.6 Источники
- [TechCrunch — Musk humans underrated](https://techcrunch.com/2018/04/13/elon-musk-says-humans-are-underrated-calls-teslas-excessive-automation-a-mistake/);
- [Elon Musk X/Twitter status 984882630947753984](https://x.com/elonmusk/status/984882630947753984);
- [CNBC — Musk admits humans superior to robots](https://www.cnbc.com/2018/04/13/elon-musk-admits-humans-are-sometimes-superior-to-robots.html);
- [Fortune — Tesla CEO humans underrated](https://fortune.com/2018/04/13/tesla-elon-musk-robot-human-model-3/);
- [IMD — Tesla problem overestimating automation](https://www.imd.org/research-knowledge/strategy/articles/teslas-problem-overestimating-automation-underestimating-humans/);
- [Conversation — Tesla problem overestimating automation](https://theconversation.com/teslas-problem-overestimating-automation-underestimating-humans-95388);
- [Business Standard — Humans underrated automation Tesla](https://www.business-standard.com/article/international/humans-are-underrated-excessive-automation-at-tesla-my-mistake-elon-musk-118041400734_1.html).

### 2.7 Follow-up — GigaCast retreat (2024)
- Май 2024: Tesla отказался от next-gen single-piece gigacasting underbody planning для Model 2.
- Причина: technical risk + Model 2 cancellation.
- Возврат к 3-piece (front+back gigacasted + middle aluminum/steel frame).
- **Связь с 2018-уроком:** Tesla не учится «один раз» — даже после 2018 опять пытался push state-of-art automation, опять retreated.
- Источник: [CNBC — Tesla retreats gigacasting](https://www.cnbc.com/2024/05/01/tesla-retreats-from-next-generation-gigacasting-manufacturing-process.html).

---

## 3. Computer Vision границы

### 3.1 Низкоконтрастные дефекты
- **Что не работает.** Low-contrast defects (например, шероховатость на одинаково-окрашенной поверхности, поверхностные micro-cracks в композитах) — minimal contrast difference defect-vs-background → modern CV models **brittle under distribution shift**.
- **Manifestation.** Defect rate 1-2% → десятки тысяч инспекций производят сотни labeled examples → severe class imbalance + overfitting risk.
- **Альтернатива.** Specialised illumination (structured light, polarised light, X-ray), ultrasonic testing, thermography — physical signal amplification, **до** ML decision.

### 3.2 Distribution shift при смене продукта / партии
- **Что не работает.** Model trained on Product A camera distribution **не переносится** на Product B без retrain. Common pitfall: factory rolls out CV inspection на одной linijo, expands ко всей plant, обнаруживает что нужны 5+ separate models — each requiring own labeled dataset.
- **Manifestation.** AOI (Automated Optical Inspection) в PCB strongly suffers: variations в camera optics, illumination, product design.
- **Альтернатива.** Domain adaptation, few-shot adaptation foundation vision models — это **research stage**, не plug-and-play. Production-practice: separate models per product line + retrain pipeline.

### 3.3 False-positive стоимость в continuous process
- **Что не работает.** В continuous process (chemistry, steel rolling) false positive triggers unnecessary intervention — operator останавливает процесс, line is reset, cost = десятки тысяч USD per false alarm.
- **SPC vs ML.** Classical SPC может иметь higher false-positive rate но **predictable, easy-tune**. ML modelled false-positive rate — opaque, requires recalibration.
- **Источник:** [ScienceDirect — SPC vs DL power plant condition monitoring](https://www.sciencedirect.com/science/article/abs/pii/S0098135423002612).

### 3.4 Mislabeling в training data
- **Что не работает.** Manufacturing defect labels часто mislabeled даже специалистами (subjective: «is this scratch a defect или cosmetic acceptable variation?»). ML model trained on noisy labels не превышает inter-rater agreement.
- **Альтернатива.** Active learning с **multi-rater consensus labelling**; explicit «abstain» class; uncertainty-calibrated предсказания.

### 3.5 Boeing 737 — door plug failure (2024) — anti-кейс CV не предотвратил
- **Контекст.** Boeing развернул AI quality inspection на 737 line в Renton/Everett в начале 2024. **Тем не менее**: Jan 2024 — door plug отвалился в полёте Alaska Airlines 737 MAX 9. Mechanics в Renton **reinstalled door plug improperly**. **AI не словил.**
- **Lesson.** CV-inspection — это **последняя линия защиты**, не первая. Если процесс reinstall door plug не имеет proper sign-off + audit trail — AI inspection не закроет gap.
- **FAA cap.** 38 737 max/month, 12 months delay для Everett line. Boeing Spirit AeroSystems — 50 jets needed rework из-за improperly drilled holes.
- **Урок.** AI inspection не заменяет process integrity. «Garbage in, garbage out» — если processes broken, AI на финале не починит.
- **Источники:**
  - [NPR — Boeing whistleblower](https://www.npr.org/2024/01/24/1226666911/boeings-quality-control-draws-criticism-as-a-whistleblower-alleges-lapses-at-fac);
  - [NPR — Boeing Spirit AeroSystems problems](https://www.npr.org/2024/02/05/1228720602/boeing-737-max-spirit-aerosystems-kansas-factory-problems);
  - [NPR — Boeing 2024 timeline](https://www.npr.org/2024/03/20/1239132703/boeing-timeline-737-max-9-controversy-door-plug);
  - [FlightGlobal — Everett 737 Max 12 months delay](https://www.flightglobal.com/airframers/everett-737-max-line-remains-on-hold-even-as-boeing-eyes-future-rate-rises/165329.article).

### 3.6 Источники для CV limits общего scope
- [arXiv — AI-Driven Multi-Stage CV Defect Detection laser-engraved nameplates](https://arxiv.org/html/2503.03395v1);
- [PMC — Few-shot adaptation foundation vision models PCB inspection](https://pmc.ncbi.nlm.nih.gov/articles/PMC12653441/);
- [ScienceDirect — CV defect unseen backgrounds manufacturing](https://www.sciencedirect.com/science/article/abs/pii/S0957417423032517);
- [ScienceDirect — surface defect detection PCBs machine vision review](https://www.sciencedirect.com/science/article/pii/S259012302502506X).

---

## 4. Predictive Maintenance — reality check

### 4.1 Marketing vs reality
- **Маркетинг (vendor / analyst):** -25-40% maintenance cost, -50-70% downtime, ROI 6-14 months.
- **Reality** (McKinsey 2025 «Prediction at scale» и State of AI 2025):
  - 78% organizations используют AI, только 5.5% — high performers с EBIT impact >5%.
  - 2/3 — pilot purgatory.
  - 39% companies report enterprise-level earnings impact.

### 4.2 Где не работает (production-detail)
1. **Slow feedback loop.** Если equipment failure rate — 1 failure/year/asset, model retraining sample size недостаточен для drift detection.
2. **No ground-truth.** «Did we prevent failure?» — counter-factual unknowable.
3. **False-positive expensive.** В steel rolling — false alarm может stop line на 4 часа = $200K-$1M lost throughput.
4. **Equipment heterogeneity.** Каждая turbine, mill, pump имеет own «personality»; one-model-fits-all не работает; per-asset models — high maintenance cost overhead.

### 4.3 Anti-кейс: F-35 ALIS (см. lec-09 для полной истории, кратко здесь)
ALIS (Autonomic Logistics Information System) — Lockheed Martin's predictive maintenance + supply chain manager для F-35. К 2020-м: высокий false-positive rate, неточные данные, плохой UI. GAO: «inaccurate and missing data have at times resulted в system signalling что F-35 should not be flown even though aircraft had no issues». Cost-per-flight-hour вырос до **$44 000** — higher than F-22 Raptor. ALIS заменён на ODIN; ODIN fielding to squadrons задержано до 2025.
- Это **canonical** predictive-maintenance-fail в complex equipment domain.
- Источник: [Air & Space Forces — F-35 dumps ALIS](https://www.airandspaceforces.com/f-35-program-dumps-alis-for-odin/); [GAO-22-105943](https://www.gao.gov/assets/gao-22-105943.pdf).

### 4.4 Урок
1. **PdM полезен там, где (a) feedback loop fast, (b) ground truth available, (c) false-positive cost ≤ false-negative cost.**
2. **Equipment с long MTBF + critical safety — PdM плохо работает.** Use scheduled preventive maintenance + condition-based monitoring instead.
3. **«Reduce downtime by 70%» — slogan, не measurable promise.** Запросить: baseline downtime, measurement window, intervention list.

### 4.5 Альтернатива
- **Condition-based monitoring (CBM)** — simpler thresholds, easier audit.
- **Reliability-Centered Maintenance (RCM)** — engineering approach, не ML.
- **Hybrid:** PdM для high-MTBF rotating equipment (pumps, motors); CBM для slow-degradation (insulation, bearings); preventive для safety-critical (brakes, sensors).

---

## 5. RL distribution drift в process

### 5.1 Где RL ломается
1. **Batch transitions.** RL trained на steady-state operation. При batch start/stop — out-of-distribution; policy может randomly switch к unsafe actions.
2. **Change of feedstock.** Chemical / metallurgical processes имеют batches с varying composition. New feedstock = new dynamics = trained RL policy stale.
3. **Seasonal shifts.** Ambient temperature/humidity влияет на cooling, evaporation, fermentation. RL trained летом не работает зимой без retrain.
4. **Equipment wear.** Heat exchanger fouling, catalyst deactivation, pump wear — process dynamics drift slowly; RL policy decays.

### 5.2 Почему MPC часто лучше RL
- **MPC (Model Predictive Control)** работает с **explicit dynamic model**; объясним; легко validated.
- **RL** — model-free or model-based; policy — black box; trust harder.
- **Industry preference:** MPC dominates process control; RL дополняет на **higher-level scheduling** (Yokogawa FKDPP — это RL на set-point selection, не на direct valve control).
- **Hybrid:** CIRL (Control-Informed RL) — explicit PID integration в RL architecture (BASF + Royal Academy of Engineering).

### 5.3 Урок
1. **RL — promising на high-level scheduling + non-linear optimization;** rarely замещение PID / MPC на low-level loops.
2. **Production-RL требует robust drift detection + safe-fallback to MPC/PID** при out-of-distribution detection.

### 5.4 Источники
- [MDPI — Recent Advances RL Chemical Process Control](https://www.mdpi.com/2227-9717/13/6/1791);
- [ACS — Control-Informed RL Chemical Processes](https://pubs.acs.org/doi/10.1021/acs.iecr.4c03233);
- [PMC — CIRL Chemical Processes](https://pmc.ncbi.nlm.nih.gov/articles/PMC11891910/);
- [ScienceDirect — Hybrid Deep RL Chemical Batch Plants Scheduling Control](https://www.sciencedirect.com/science/article/pii/S2405896325005154);
- [arXiv 2511.16297 — Operation Recipes RL safe chemical control](https://arxiv.org/pdf/2511.16297).

---

## 6. Cultural / organizational rejections

### 6.1 Toyota — slow AI adopter (but for principled reason)
- **Контекст.** Toyota Production System — основан на Jidoka («автоматизация с человеческим прикосновением») + Kaizen (continuous improvement workers-driven). Toyota публично **выступает не за full automation**.
- **2024-2026:** Toyota запустила GAIA (Global AI Accelerator). Философия: **AI as tools for workers, not replacement**. Number of AI models created by employees: 8000 (2023) → 10 000 (2024).
- **Урок.** Toyota не «skeptical to AI» в исходном смысле — она skeptical к **AI как замене человеку**. Это разные позиции. Toyota deploys AI там, где это augments worker judgement; refuses там, где это substitutes judgement.
- **Альтернатива (Toyota's view).** Worker-driven AI development. Если worker не понимает model — model не deployed.
- **Источники:** [chiefaiofficer — Toyota AI workers saved 10000h](https://chiefaiofficer.com/blog/how-toyota-gave-ai-tools-to-factory-workers-and-saved-10000-hours/); [industryweek — Toyota Jidoka Future](https://www.industryweek.com/operations/continuous-improvement/article/55336191/toyotas-jidoka-prinicple-and-the-future-of-work).

### 6.2 Rolled-back deployments
- **AB InBev claim +60% beer volume per cycle** — public PR; production-replication metrics не disclosed. Известно, что **большая часть brewery AI initiatives** в industry pilot-purgatory.
- **Tesla** см. секцию 2.
- **Boeing 737 AI inspection** не предотвратил door plug fail — это **process integrity issue**, не AI rollback, но lesson similar.

### 6.3 Урок для культуры
- **Worker-buy-in is critical.** Если operators видят AI как threat, они **find workarounds**, deactivate alarms, ignore recommendations.
- **AI как «assistance», не «replacement»** — это **proven adoption pattern** (Toyota, Pfizer Vox, BMW GenAI4Q).

---

## 7. Regulatory blockers — где compliance limits AI

### 7.1 FDA 21 CFR Part 11 (pharma) — data integrity + audit trail
- **Что требует.** Electronic records & signatures должны иметь: audit trails, validated systems, secure storage, traceable changes. AI outputs treated as CGMP data.
- **Проблема для AI.** Black-box ML — нет clear audit trail «why model made this decision». FDA frequently citing missing audit trails, corrupted records, lack of system validation в 2024-2025.
- **Industry guidance:** AI cannot be the **final decision-maker**; maintain **human-in-the-loop**. GAMP®5 требует validation each AI system. XAI techniques (SHAP, LIME) integrated для ICH Q8-Q11 compliance.
- **Что работает.** AI для **batch quality prediction** (suggestion to operator); operator имеет final authority + traceable approval.
- **Что не работает.** Autonomous AI batch release.
- **Источники:**
  - [IntuitionLabs — 21 CFR Part 11 AI Compliance Guide](https://intuitionlabs.ai/articles/21-cfr-part-11-ai-compliance);
  - [IntuitionLabs — 21 CFR Part 11 AI Systems](https://intuitionlabs.ai/articles/21-cfr-part-11-compliance-ai-systems);
  - [BioPharm International — Qualifying AI Algorithms Pharma](https://www.biopharminternational.com/view/qualifying-ai-algorithms-in-pharmaceutical-manufacturing);
  - [Nature Scientific Reports — quality-by-design pharma production](https://www.nature.com/articles/s41598-025-27879-w);
  - [PMC — Intelligent information management QbD pharma](https://pmc.ncbi.nlm.nih.gov/articles/PMC12717253/).

### 7.2 REACH / RoHS (chemicals)
- **Что требует.** Substance registration + restricted hazardous substances tracking. Manufacturer must prove chemical composition + safety.
- **Проблема для AI.** Generative formulation AI (BASF, XtalPi) — formulation candidates need separate REACH-registration tests. ML может suggest, не validate.

### 7.3 ATEX / IECEx (explosive environments) — oil/gas, chemistry, grain dust
- **Что требует.** Equipment в hazardous zones — ATEX-certified hardware; specific risk assessments; restricted electrical equipment.
- **AI relevance.** **AI/ML может помочь** в predictive monitoring of gas concentrations, temperatures, dust levels. **Не может заменить** ATEX-certified hardware. AI sensor data **augments** but не replaces — engineered safeguards и оператор control.
- **Где AI не разрешён.** В Zone 0 (постоянно взрывоопасная атмосфера) — equipment limited; non-certified AI inference hardware **запрещён физически**.
- **Источники:** [atex-blog — IoT smart tech ATEX hazardous areas](https://atex-blog.com/2024/09/22/atex-in-the-digital-age-the-role-of-iot-and-smart-technology-in-hazardous-areas/); [roboticstomorrow — Explosion-Proof Robotics ATEX/IECEx 2025](https://www.roboticstomorrow.com/story/2025/11/explosion-proof-robotics-in-atexiecex-environments-progress-challenges-and-practical-pathways/25788/).

### 7.4 HACCP (food safety)
- Similar logic: AI can monitor, but final HACCP audit requires documented procedural integrity. AI can support, не заменить.

### 7.5 Урок regulatory
- **«AI must wait for regulation» — false framing.** Regulation **уже есть**; AI должен fit within существующие frameworks (21 CFR, REACH, ATEX, HACCP, ICH).
- **Black-box ML — anti-pattern в regulated industries.** Explainable AI / hybrid models / human-in-the-loop — must.
- **Audit trail обязателен.** Каждое AI-recommendation/decision должно быть traceable: input data, model version, output, who acted on it, when.

---

## 8. Fundamental limits + альтернативные инструменты — критерии выбора

### 8.1 Physics-based simulation vs ML — когда что
- **Physics-based simulation (CFD, FEA, kinetic models) выигрывает когда:**
  - Phenomenon governed by known equations (Navier-Stokes, heat transfer, chemical kinetics).
  - Need extrapolation beyond training distribution (e.g., predict behaviour в untested conditions).
  - Need explainability + audit ability.
  - Computational cost acceptable.
- **ML выигрывает когда:**
  - Phenomenon governed by ill-known physics (e.g., complex multi-phase reaction).
  - Need real-time decisions (physics too slow).
  - Data abundant в operating envelope.
- **Hybrid (physics-informed ML, PINNs) часто оптимум** — особенно в process industries.

### 8.2 SPC vs deep learning anomaly detection
- **SPC выигрывает когда:**
  - Univariate monitoring sufficient.
  - Need easy operator interpretation + audit.
  - Process под statistical control (Gaussian distribution).
  - Regulatory environment (pharma, food) — SPC accepted, ML — questioned.
- **ML deep learning выигрывает когда:**
  - Multivariate + complex correlations.
  - Non-stationary processes.
  - Defects rare + subtle (low SNR).
- **Hybrid (ML on top of SPC):** ML reduces SPC false-alarm rate; SPC limits ML out-of-distribution.
- **Источники:**
  - [Acerta — SPC vs ML](https://acerta.ai/blog/the-difference-between-machine-learning-spc-and-why-it-matters/);
  - [MDPI — ML for SPC review](https://www.mdpi.com/1099-4300/28/2/151);
  - [PMC — ML for SPC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12939129/);
  - [IJSRM — AI-enabled SPC semiconductor](https://www.ijsrm.net/index.php/ijsrm/article/view/6439).

### 8.3 MPC vs RL в process control
- **MPC выигрывает когда:**
  - Dynamic model available (linear / mild nonlinear).
  - Constraints критичны (safety limits) — MPC handles explicitly.
  - Regulatory requirement audit / explainability.
- **RL выигрывает когда:**
  - High-level scheduling beyond MPC time horizon.
  - Non-convex multi-objective tradeoffs (e.g., quality vs throughput vs energy).
  - Model unknown but simulator available.
- **Hybrid:** MPC inside RL or CIRL — best of both (см. секцию 5).

### 8.4 DOE / Six Sigma vs ML formulation
- **DOE выигрывает когда:**
  - Regulated industries (pharma — DOE accepted by FDA для QbD).
  - Few variables (≤10), need defensible documentation.
  - Need understanding interaction effects vs blackbox prediction.
- **ML/Sequential Learning выигрывает когда:**
  - High-dimensional (≥20 variables) — DOE требует exponential experiments, ML linear.
  - Lots of historical data available.
  - Active learning + Bayesian optimization для efficient exploration.
- **Source:** [Wiley — DOE + ML quality improvement complementary](https://onlinelibrary.wiley.com/doi/abs/10.1002/qre.3025); [citrine.io — DOE or ML](https://citrine.io/doe/); [PMC — ML and DOE product innovation chemical industry](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9225671/); [Wiley Advanced Intelligent Discovery — Experiment Design Drug Development](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aidi.202500087).

### 8.5 Rules-based vision vs deep learning
- **Rules-based:** simple threshold-based detection (e.g., gauge dimensions exceed spec).
- **Выигрывает когда:** defect well-defined, lighting controlled, low variability.
- **Deep learning выигрывает когда:** defect subtle (cosmetic), variability high, large labeled dataset available.
- **Эмпирически:** ~60-70% production manufacturing inspection workloads — rules-based достаточно. ML — для остальных 30-40%.

### 8.6 PLC vs edge ML
- **PLC выигрывает когда:**
  - Hard real-time (≤10ms control loop).
  - Safety-critical (SIL 2/3) — ML certification гораздо труднее.
  - Process well-understood.
- **Edge ML выигрывает когда:**
  - Pattern recognition (vision, acoustic).
  - Slow (≥100ms) control loops.
  - Anomaly detection.
- **Hybrid (PLC + edge ML coprocessor):** PLC executes deterministic logic; edge ML provides advice; operator/PLC make final decision. POSCO architecture именно такой.

---

## Summary — критерии «здесь AI не нужен / не работает»

**Student-friendly декларация — для лекционного слайда:**

> **AI не подходит, если хотя бы один из:**
> 1. Equipment с MTBF >1 year → недостаточно data для PdM.
> 2. False-positive cost >10× false-negative cost → ML rarely калибруется так.
> 3. Regulatory requirement audit-trail каждого решения → black-box ML не работает.
> 4. Process under SIL 2/3 safety → certification ML гораздо сложнее.
> 5. Phenomenon governed by known physics → physics-based simulation надёжнее.
> 6. Operator distrust → workaround неизбежен.
> 7. Pilot ROI без production go-criteria → 80-95% pilot purgatory.
> 8. ATEX Zone 0 → physical hardware restrictions.
> 9. DOE-acceptable + few variables + need understanding → DOE предпочтительнее.
> 10. Demo-driven hype claims без 6-month production track record → buyer beware.

**Альтернативы — must-know toolset для инженера:**
- SPC + Six Sigma — quality control в large-batch processes.
- DOE — formulation, parameter optimization.
- MPC / PID — process control.
- RCM / CBM — reliability engineering.
- Physics-based simulation (CFD, FEA, kinetics) — для extrapolation.
- Rules-based vision — для controlled inspection environments.
- Hybrid PINN / CIRL — где physics+data комбинированы.

**Cross-cut вывод (для keystone-уровня лекции):** AI в производстве — **augmentation tool**, не замена. Engineer's job — знать **где AI применим, где традиционный инструмент лучше, и где cooperation между ними**. Это **критическое суждение** — главная цель курса.
