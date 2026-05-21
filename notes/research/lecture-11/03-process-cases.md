# 03 — Кейсы AI в процессном производстве

**Summary.** 17 verifiable кейсов в процессном производстве (химия/нефтехимия, металлургия, фарма/биотех, цемент, удобрения, пиво/напитки). Формат как файл 02. Используй для плана §3 «Процессное производство — где AI работает иначе». Процессное ≠ дискретное: continuous flow, soft sensors, MPC/RL гибрид, regulatory weight (FDA/REACH/ATEX). Кейсы с `[VFY-day-of]` — переверить на день лекции.

---

## A. Химия / нефтехимия

### A1. BASF — AI-driven formulation + Soft Sensors (Geismar, Germany; 2023-2026)
- **Тип задачи.** (a) Formulation optimization — R&D ускорение. (b) AI-enabled «soft sensors» — real-time оценка quality parameters без физических лабораторных samples.
- **Inputs/outputs.** 150 years of chemical knowledge → AI knowledge base; sensor + process data → quality prediction → operator advice / setpoint suggestion.
- **Эффект.** Formulation research 18 месяцев → 3 недели (claim). Soft sensors на Geismar site: **-30% batch defects**, improved consistency без increased testing costs. R&D costs -30%, time-to-market -40% (через AI formulation).
- **Failure mode.** Public — не disclosed; общее ограничение soft sensors — drift при отклонении сырья от training distribution (см. файл 04).
- **Дата.** Geismar deployment: 2023-2024. Imperial-BASF spinout (R&D acceleration): июль 2024. XtalPi automated formulation testing: 2024-2025 (Shanghai Innovation Campus).
- **Источники:**
  - [basf.com — AI digitalization](https://www.basf.com/global/en/who-we-are/digitalization/artificial-intelligence);
  - [basf.com — 5 AI BASF success stories](https://www.basf.com/us/en/media/featured-articles/technology/ai-basf-success-stories);
  - [chiefaiofficer — BASF 18 months to 3 weeks](https://chiefaiofficer.com/blog/how-basf-cut-chemical-research-from-18-months-to-3-weeks-using-150-years-of-ai-data/);
  - [soci.org — Imperial-BASF spinout](https://www.soci.org/news/2024/7/basf-and-imperial-college-spinout);
  - [chemcopilot.com — AI formulations chemical](https://www.chemcopilot.com/blog/how-ai-optimizes-formulations-in-the-chemical-industry).

### A2. Yokogawa + JSR — FKDPP autonomous distillation column (35 days, 2022)
- **Тип задачи.** Reinforcement Learning контроль distillation column в production.
- **Inputs/outputs.** Sensor data → RL policy → valve actions. PID/APC compromise resolved by RL.
- **Эффект.** **35 дней автономной работы (840 hours)** на JSR production plant, январь-февраль 2022. Demonstrated RL can be safely applied. Контроль операций beyond PID + APC capability.
- **Дата.** 2022-01-17 — 2022-02-21. Award: Japan Industrial Technology Prime Minister's Prize 2023.
- **Failure mode.** Single-process scope (one column); replicating across plants — substantial domain-engineering work.
- **Источники:**
  - [Yokogawa press 2023](https://www.yokogawa.com/news/press-releases/2023/2023-03-15/);
  - [Yokogawa SE Asia press 2022](https://www.yokogawa.com/sg/news/press-releases/2022/2022-03-22/);
  - [JSR press 2022](https://www.jsr.co.jp/jsr_e/news/2022/20220322.html);
  - [BusinessWire — 35 days](https://www.businesswire.com/news/home/20220321005003/en/In-a-World-First-Yokogawa-and-JSR-Use-AI-to-Autonomously-Control-a-Chemical-Plant-for-35-Consecutive-Days).

### A3. Dow Chemical — ML process optimization (2023-2026)
- **Тип задачи.** ML-driven process optimization, formulation.
- **Эффект.** Disclosed как «active leveraging», но specific production-deployment metrics — limited public detail.
- **Failure mode / альтернатива.** Не disclosed; общая dynamics — Dow осторожно отделяет R&D AI от production-control AI.
- **Источник:** [chemcopilot.com — How AI optimizes formulations](https://www.chemcopilot.com/blog/how-ai-optimizes-formulations-in-the-chemical-industry); [azorobotics.com — ML chemical processes](https://www.azorobotics.com/Article.aspx?ArticleID=765).

### A4. Sasol — Coal-to-liquids + AI optimization (2024-2025)
- **Тип задачи.** Энергоэффективность и process consistency на крупнейших coal-to-liquids facilities (South Africa Secunda).
- **Public detail metrics** — ограничен; **требует дополнительной верификации** перед использованием в лекции.

### A5. ExxonMobil — AI refinery operations (2024-2025)
- **Тип задачи.** Refinery process optimization, anomaly detection.
- **Public detail metrics** ограничен. **Требует дополнительной верификации.**

### A6. Shell — AI exploration / refining (2024-2025)
- **Тип задачи.** Refinery anomaly detection; AI for trading; (downstream + upstream).
- **Эффект.** Shell имеет public AI-portfolio (десятки use cases), но production-control specific metrics — ограничено.
- **Источник для общего контекста:** Shell sustainability + tech reports, [shell.com tech library] — стоит достать конкретные numbers перед лекцией.

### A7. SABIC — Petrochemicals AI (2024-2025)
- **Тип задачи.** Process optimization, predictive maintenance.
- **Public detail metrics** ограничен.

---

## B. Металлургия

### B1. ArcelorMittal — Hot rolling + blast furnace AI (2024-2025)
- **Тип задачи.** AI алгоритмы на blast furnaces, rolling mills, continuous casters.
- **Inputs/outputs.** Multi-sensor → process control suggestion → operator action.
- **Эффект.** ArcelorMittal cited as one of patent leaders в digital steel (574 filed since 2005, ArcelorMittal + POSCO + JFE + Tata + IBM). Hot strip mill для AHSS, Line Pipe, Stainless.
- **Failure mode.** Production-specific AI metrics — ограниченные публикации. **Требует verification.**
- **Источники:**
  - [globenewswire — Digital Transformation Steel Industry Patents](https://www.globenewswire.com/news-release/2025/01/02/3003408/28124/en/Dtigital-Transformation-in-Steel-Industry-Patent-Landscape-Report-2024-Comprehensive-Analysis-of-574-Patents-Filed-Since-2005-Featuring-ArcelorMittal-POSCO-JFE-Steel-Tata-Steel-and.html);
  - [steel-technology — Top 6 steel companies adopting AI](https://www.steel-technology.com/articles/top-6-steel-companies-adopting-ai);
  - [gmk.center — Robots near blast furnace AI](https://gmk.center/en/posts/robots-near-the-blast-furnace-artificial-intelligence-in-steel-industry/).

### B2. POSCO — Edge ML + Smart Factory (2024-2025)
- **Тип задачи.** Edge inference на 180 rolling mill assets; failure detection independent of corporate network.
- **Эффект.** +5% production efficiency, -10% energy consumption, +3% yield в hot-rolled steel.
- **Дата.** 180 edge nodes deployed 2024.
- **Failure mode.** Edge AI requires local model maintenance; drift detection требует human-in-the-loop.
- **Источники:**
  - [steel-technology — Leading Steel Companies AI](https://www.steel-technology.com/articles/top-6-steel-companies-adopting-ai);
  - [Manufacturing Digital — POSCO digital transform o9](https://manufacturingdigital.com/articles/how-o9-will-digitally-transform-poscos-planning-processes).

### B3. Tata Steel — Smart Factory Program (2024-2025)
- **Тип задачи.** Yield prediction, fuel optimization, workforce analytics, equipment life prediction.
- **Эффект.** **-20% downtime, -15% maintenance cost** (заявка). Tata Steel — лидер digital steelmaking в Азии.
- **Дата.** Active 2024-2025; goal — leader в digital steelmaking by 2025.
- **Failure mode.** Не disclosed; cross-plant rollout requires per-site recalibration.
- **Источник:** [aiexpert.network — Tata Steel AI Transformation](https://aiexpert.network/case-study-tata-steels-ai-transformation/); [whalesbook — Tata Steel AI Global Edge](https://www.whalesbook.com/news/English/industrial-goodsservices/Tata-Steel-Uses-AI-to-Sharpen-Global-Edge/69e8d0abbca97ee106a0379c).

### B4. Nucor — AI in mini-mill steel (2024-2025)
- **Тип задачи.** Predictive maintenance в EAF (electric arc furnace), quality optimization scrap blending.
- **Public detail metrics** ограничен.

### B5. Нурникель — AI на mining + processing (флотация / grinding) (2024-2025)
- **Тип задачи.** Optimisation grinding & flotation; production efficiency на добыче nickel/copper/PGM.
- **Эффект.** AI solutions для grinding/flotation **уже достигли industrial-operation stage**. Норникель — agreement с Газпром нефть (ноябрь 2024) для services по well productivity на Северо-Соленинском GCF.
- **Failure mode.** Не disclosed.
- **Источники:**
  - [nornickel.ru — gas production efficiency Nov 2024](https://nornickel.ru/news-and-media/press-releases-and-news/nornikel-povysit-effektivnost-dobychi-gaza-blagodarya-noveyshim-tekhnologiyam/);
  - [prometall.info — ММК НЛМК Норникель Северсталь внедряют ИИ](https://www.prometall.info/corp/kak_mmk_nlmk_nornikel_i_severstal_vnedryayut_u_sebya_ii).

### B6. ММК + Северсталь + НЛМК — AI implementation overview (2024-2025)
- **Тип задачи.** AI «как новый стабильный способ повышения операционной эффективности» (industry citation).
- **Эффект.** Деталь — limited public-verifiable production-deployment metrics. Финансовый контекст: 2024-2025 — глубокий кризис отрасли (Severstal profit -55% в 2024); steel prices -18% в 2024, -8.5% в 2025. AI как cost-reduction lever — but limited transparency on results.
- **Источник:** [prometall.info — Как ММК, НЛМК, Норникель, Северсталь внедряют ИИ](https://www.prometall.info/corp/kak_mmk_nlmk_nornikel_i_severstal_vnedryayut_u_sebya_ii); [vc.ru — металлурги 2025 кризис](https://vc.ru/invest/2068530-severstal-nlmk-mmk-nornikel-aktcii-metalurghov-2025).

---

## C. Фарма / биотех

### C1. Pfizer — Vox + golden-batch process (2024-2025)
- **Тип задачи.** Real-time anomaly detection, golden-batch identification, operator recommendation.
- **Inputs/outputs.** Manufacturing sensor data + historical batch records → AWS Bedrock + SageMaker → recommend actions to operators.
- **Эффект.** **+20 000 vaccine doses per batch** (Pfizer mRNA prediction algorithm 2024). LLM-based assistance для process engineering.
- **Failure mode.** Pfizer claims «recommend actions» (human-in-loop), не autonomous control — consistent с FDA 21 CFR Part 11 (см. файл 04).
- **Дата.** 2024-2025.
- **Источник:** [healthtechmagazine — AI drug manufacturing](https://healthtechmagazine.net/article/2025/02/ai-in-drug-manufacturing-perfcon); [kitameraki — Pfizer pharma manufacturing AI](https://www.kitameraki.com/post/pfizer-and-others-leading-the-pharmaceutical-manufacturing-with-ai-and-technology).

### C2. Moderna — OpenAI generative AI + mRNA design (2024-2025)
- **Тип задачи.** mRNA + DNA sequence design assistance; logistics decisions; QC steps automation.
- **Эффект.** Не disclosed точные numbers; стратегическое partnership Moderna-OpenAI announced 2024 для streamline operations.
- **Failure mode.** Не disclosed.
- **Источник:** [kitameraki — Pfizer/Moderna pharma AI](https://www.kitameraki.com/post/pfizer-and-others-leading-the-pharmaceutical-manufacturing-with-ai-and-technology).

### C3. Novartis — process optimization + digital twin (2024-2025)
- **Public detail metrics** ограничен в moих результатах поиска. Рекомендую verify перед лекцией.

### C4. Genentech / Roche — AI batch optimization (2024-2025)
- **Public detail metrics** ограничен.

**Regulatory кросс-cut для фармы (см. файл 04 детальнее):**
- **FDA 21 CFR Part 11** — для electronic records & signatures: audit trails, electronic record integrity, validated systems. К 2024-2025: FDA frequently cited missing audit trails, corrupted records, lack of validation. AI usage в pharma doubled 2022-2023; к 2025 — >60% pharma companies имеют pilot AI в clinical/manufacturing.
- **AI cannot be the final decision-maker — maintain human-in-the-loop** (industry guidance).
- **GAMP®5** требует validation each AI system, characterized like other software.

---

## D. Цемент / стройматериалы

### D1. Holcim — AI kiln + 100 plants rollout (2024-2026)
- **Тип задачи.** Predictive maintenance + kiln optimization.
- **Inputs/outputs.** Sensor data (temperature, fuel flow, gas composition) → C3 AI platform → setpoint suggestions / failure prediction.
- **Эффект.** June 2024: announce расширение AI на 100+ plants за 4 года. На момент объявления — installed at 45 plants. Digital twin cement plant world-first launched.
- **Failure mode.** Не disclosed публично.
- **Источник:** [holcim.com — Smart Operations AI](https://www.holcim.com/who-we-are/our-stories/smart-operations-ai); [globalcement — AI cement Apr 2025](https://www.globalcement.com/news/item/18712-update-on-artificial-intelligence-in-the-cement-sector-april-2025).

### D2. CEMEX — Optimitive investment + AI kiln (2024-2026)
- **Тип задачи.** AI kiln control via Optimitive (Spanish AI software vendor).
- **Эффект.** **10% energy savings, ROI 18 months** (general industry claim для AI kiln control). McKinsey: up to 10% throughput + energy efficiency improvement в autonomous mode на North American cement plant.
- **Источник:** [globalcement — AI cement 2025](https://www.globalcement.com/news/item/18712-update-on-artificial-intelligence-in-the-cement-sector-april-2025).

### D3. LafargeHolcim — AI alternative fuel management (2024-2026)
- **Тип задачи.** Optimization mix of alternative fuels in kiln operations.
- **Эффект.** AI-optimized kiln firing reduces CO2 by 2-5% per tonne of clinker. Это значимая environmental метрика.
- **Источник:** [ifactoryapp — AI Alternative Fuel Cement 2026](https://ifactoryapp.com/industries/cement-plant/ai-alternative-fuel-management-cement-manufacturing-2026); [advaiya — Digital cement plants](https://advaiya.com/digital-transformation-cement-plants-kiln-monitoring-predictive-supply-chain/).

### D4. Heidelberg Materials — AI in concrete production (2024-2025)
- **Тип задачи.** Concrete mix optimization + carbon footprint reduction.
- **Public detail ограничен** в моих search results.

---

## E. Удобрения / пищевая / напитки

### E1. AB InBev — Brewery AI (см. файл 02 D2 — overlap)
- **Note.** AB InBev — beverage производство классифицируется как **process** на стадии brewing (continuous flow), но **discrete** на packaging. Можно использовать в обоих разделах.
- **Ключевая метрика:** +60% beer volume per filtration cycle (Google Cloud + Beer Garage).

### E2. Heineken — AI flavour QC + fermentation (2024-2025)
- **Public detail ограничен.**

### E3. Diageo — AI maturation/blending (2024-2025)
- **Public detail ограничен.**

### E4. Yara — AI fertilizer production + precision agriculture (2024-2025)
- **Public detail metrics для production-side** ограничен. Yara имеет crop-prescription AI (Atfarm, FarmCare), что больше agriculture-side; production-side AI — less public.

### E5. Nutrien — fertilizer production AI (2024-2025)
- **Public detail metrics ограничен** для production AI specifically.

### E6. Сибур — Marketplace технологического моделирования (2025-2026)
- **Тип задачи.** Внутренний marketplace для tech-моделирования; будет включать AI-models для process simulation.
- **Эффект.** Launch v1 — Q1 2025; basic functionality к 2026 (полностью). Команды компании приглашены создавать models с Q2 2025.
- **Контекст.** Российская нефтехимия активно ищет import-substitution AI tools (100% critical infrastructure → domestic software к 2027 — government goal).
- **Источник:** [comnews.ru — Сибур маркетплейс моделирования 2026](https://www.comnews.ru/content/236580/2024-11-29/2024-w48/1008/2026-g-sibur-zapustit-marketpleys-tekhnologicheskogo-modelirovaniya); [comnews — Нефтяная отрасль импортозамещение к 2027](https://www.comnews.ru/content/236864/2024-12-16/2024-w51/1008/neftyanaya-otrasl-importozamestit-soft-k-2027-g); [sozvezdye — Газпром нефть СИБУР автоматизация](https://sozvezdye.org/%D0%B3%D0%B0%D0%B7%D0%BF%D1%80%D0%BE%D0%BC-%D0%BD%D0%B5%D1%84%D1%82%D1%8C-%D1%81%D0%B8%D0%B1%D1%83%D1%80-%D0%B8-%D0%B4%D1%80%D1%83%D0%B3%D0%B8%D0%B5-%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8/).

### E7. Газпром нефть + СИБУР — joint конференции по автоматизации (сентябрь 2024)
- **Тип задачи.** Координация отраслевая по автоматизации oil/gas refining.
- **Эффект.** XIV «Модернизация НПЗ и НХП». Discussion automation как priority.
- **Источник:** [oilandgasgeology — конференция](https://oilandgasgeology.ru/%D0%B3%D0%B0%D0%B7%D0%BF%D1%80%D0%BE%D0%BC-%D0%BD%D0%B5%D1%84%D1%82%D1%8C-%D1%81%D0%B8%D0%B1%D1%83%D1%80-%D0%B8-%D0%B4%D1%80%D1%83%D0%B3%D0%B8%D0%B5-%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8/).

---

## Cross-cutting observations для плана §3

1. **Процессное → soft sensors + MPC/RL гибрид + predictive maintenance.** Не CV-inspection (это дискретное). Не assembly robotics. Это про *invisible quality* (формула, доля примесей, выход реакции).
2. **Regulatory weight выше в процессном** — FDA 21 CFR Part 11 (pharma), REACH (chemicals), ATEX (взрывоопасные), HACCP (пища). Все требуют traceability, что хуже совместимо с black-box ML. См. файл 04.
3. **Российские process companies — public-disclosure скудна.** Норникель, СИБУР упоминают AI; ММК/Северсталь/НЛМК — общие декларации без production metrics. Это **анти-pattern в reporting**, не доказательство отсутствия adoption.
4. **Цемент — самый «mature use case AI kiln control».** 10% energy savings, ROI 18 months — relatively well-replicable.
5. **Foreshadow в lec-12:** Holcim digital twin cement plant world-first — это уже digital twin territory; **бросить crumb в lec-12**, не разворачивать здесь.
