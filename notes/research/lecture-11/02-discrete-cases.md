# 02 — Кейсы AI в дискретном производстве

**Summary.** 18 verifiable кейсов в дискретном производстве (автомобиле/машиностроение, электроника/полупроводники, aerospace assembly, consumer goods, российский контекст). Формат: компания / задача / inputs→outputs / measured эффект / failure mode / дата / источник. Используй как сырьё для плана §2 «Дискретное производство — что работает». Кейсы с `[VFY-day-of]` — переверить на день лекции.

---

## A. Автомобиле- и машиностроение

### A1. Tesla Gigafactory — Optimus humanoid assembly + Giga Press (2020-2026)
- **Тип задачи.** (a) Робототехническая сборка авто (модели Y, 3, S/X) — заявка high-automation. (b) Giga Press: single-piece aluminum casting underbody — replaces 70+ smaller parts.
- **Inputs/outputs.** Vision + force-torque sensors на роботах сборки; CAD-модель → cast aluminum part Giga Press 6000-9000 tonn.
- **Эффект.** Giga Press: Idra Group 2018, Tesla с 2020 в Model Y; снижение part count на 70+. Optimus: к 2025 — «hundreds» of units built (заявка 10 млн/год к 2027 на новой Giga Texas facility, ноябрь 2025).
- **Failure mode.** **2024 GigaCast retreat** — Tesla отказался от single-piece gigacasted underbody для Model 2 (small-vehicle platform). Вернулся к трёх-секционной схеме (front+back gigacasted, middle steel+aluminum frame). См. файл 04 «Tesla over-automation 2018» (canonical).
- **Дата.** Giga Press: 2020+. Optimus production: 2025-2026. GigaCast retreat: 2024-05.
- **Источники:**
  - [CNBC — Tesla retreats from gigacasting](https://www.cnbc.com/2024/05/01/tesla-retreats-from-next-generation-gigacasting-manufacturing-process.html);
  - [Wikipedia — Giga Press](https://en.wikipedia.org/wiki/Giga_Press);
  - [helpforce.ai — Optimus 10M/year Giga Texas](https://helpforce.ai/news/tesla-optimus-robot-factory-giga-texas);
  - [Jalopnik — Gigacasting explained](https://www.jalopnik.com/1927366/tesla-gigacasting-explained/).

### A2. BMW iFactory + GenAI4Q (Regensburg, 2024-2025)
- **Тип задачи.** GenAI-quality inspection: bespoke per-vehicle inspection catalogue.
- **Inputs/outputs.** Vehicle configuration + production history → tailored inspection sequence + priorities для конкретного авто.
- **Эффект.** Plant Regensburg признан «FACTORY OF THE YEAR 2024» (excellent large-series assembly). Trained personnel inspect every car, но AI defines what matters most.
- **Failure mode.** Не disclosed публично; известно, что AI Quality Platform AIQX «still requires human verification».
- **Дата.** GenAI4Q launch — 2025, partner: Datagon AI (Munich startup). Digital twins для **всех 30+ BMW plants** — 2024-2025.
- **Источники:**
  - [BMW press — GenAI4Q](https://www.press.bmwgroup.com/global/article/detail/T0449729EN/artificial-intelligence-as-a-quality-booster?language=en);
  - [Automotivemanufacturingsolutions — BMW Regensburg GenAI](https://www.automotivemanufacturingsolutions.com/smart-factory/bmw-regensburg-deploys-genai-to-reinvent-quality-checks/649724);
  - [BMW iFactory page](https://www.bmwgroup.com/en/company/production.html).

### A3. Volkswagen Digital Production Platform (DPP) + AWS (2019-2025+)
- **Тип задачи.** Industrial cloud для AI factory deployment scale.
- **Inputs/outputs.** Сенсоры/камеры с 43 заводов → AI applications (1200+) для quality, energy, scheduling.
- **Эффект.** -12% energy costs в Познань (Polska); «double-digit million range» savings от стандартизации. Real-time image analysis в Wolfsburg, Ingolstadt — каждый компонент проверяется vs configuration.
- **Failure mode.** Не disclosed; известно, что cross-plant model rollout требует per-site recalibration.
- **Дата.** Партнёрство с AWS продлено август 2025 на 5 лет.
- **Источники:**
  - [Volkswagen Group — AWS DPP press](https://www.volkswagen-group.com/en/press-releases/more-efficient-smarter-more-resilient-volkswagen-group-collaborates-with-aws-to-help-transform-production-for-the-age-of-ai-19774);
  - [aws.amazon.com — VW case study](https://aws.amazon.com/solutions/case-studies/volkswagen-dpp-generativeai/);
  - [WardsAuto — VW AWS 5-year extension](https://www.wardsauto.com/news/archive-auto-volkswagen-group-AWS-partnership-AI-cost-savings/758911/);
  - [aimagazine — VW 43 global factories](https://aimagazine.com/news/how-vw-group-aws-are-scaling-ai-across-43-global-factories).

### A4. Toyota — Global AI Accelerator (GAIA) + Jidoka 2.0 (2024-2026)
- **Тип задачи.** Democratisation AI tools для line workers: factory employees create models themselves.
- **Inputs/outputs.** Local AI models (vision, sensor) discovered by workers → save manual labor; defect prevention.
- **Эффект.** Number of AI models создано factory employees: 8000 (2023) → 10 000 (2024). Saved manual work claim — 10 000 hours/year.
- **Failure mode.** Не disclosed; философия — «not replace workers, augment them», что reduces ambitions for full autonomous lines.
- **Дата.** GAIA launch — 2025.
- **Источники:**
  - [chiefaiofficer.com — Toyota saved 10 000 hours](https://chiefaiofficer.com/blog/how-toyota-gave-ai-tools-to-factory-workers-and-saved-10000-hours/);
  - [industryweek — Toyota Jidoka Future](https://www.industryweek.com/operations/continuous-improvement/article/55336191/toyotas-jidoka-prinicple-and-the-future-of-work);
  - [klover.ai — Toyota AI strategy](https://www.klover.ai/toyota-ai-strategy-analysis-of-ai-driven-dominance-in-automative/).

### A5. Hyundai + Boston Dynamics — Spot + Atlas (2022-2026)
- **Тип задачи.** Quadruped Spot — inspection, predictive maintenance walks. Atlas — humanoid manipulation на сборочной линии.
- **Inputs/outputs.** Cameras + LiDAR на Spot → heat-map issues, gauge readings. Atlas: vision + manipulation → assembly of components.
- **Эффект.** Spot deployed в Hyundai Motor Group Metaplant America (HMGMA), Bryan County GA — exterior quality inspection в weld shop. Spot operational in 40+ countries.
- **Дата.** Atlas humanoid: first commercial deployment to Hyundai Robotics Metaplant Application Center (RMAC) — все 2026 fleet committed (январь 2026). Hyundai $26B US investment + новая robotics factory 30 000 robots/year.
- **Failure mode.** Не disclosed; Atlas — still pilot, не replacement.
- **Источники:**
  - [bostondynamics.com — Hyundai expand collaboration](https://bostondynamics.com/news/boston-dynamics-hyundai-motor-group-expand-collaboration-drive-mobility-manufacturing-innovation/);
  - [hyundai.news — Factory Safety Service Robot Spot](https://www.hyundai.news/eu/articles/press-releases/factory-safety-service-robot-boston-dynamics.html);
  - [siliconangle — Hyundai Boston Dynamics humanoid](https://siliconangle.com/2026/01/06/hyundai-boston-dynamics-join-forces-bring-humanoid-robots-factories/);
  - [hyundaimotorgroup.com — AI Robotics Strategy CES 2026](https://www.hyundaimotorgroup.com/en/news/CONT0000000000198146);
  - [newatlas — Atlas Hyundai factories](https://newatlas.com/ai-humanoids/boston-dynamics-production-atlas-hyundai/).

### A6. Ford Cologne EV Plant — AI quality + retooling (2024-2025)
- **Тип задачи.** EV-line conversion ICE→BEV; AI-driven quality control на E-Tourneo Courier и Capri assembly.
- **Inputs/outputs.** Computer vision на linejoint inspection; AI scheduling для component handover.
- **Эффект.** EV-line restart 2024 после $2B retooling Cologne. Specific AI numbers `[VFY-day-of]` — не нашёл публичных metrics через быстрый search; стоит докопать.
- **Failure mode.** EV-demand под-target (общий Ford EV slowdown 2024-2025).
- Источник прямой для AI — требует дополнительной верификации; общедоступная информация про retooling: [Ford Cologne EV plant announcements 2024](https://media.ford.com/) (помечен как требующий **дополнительной верификации** перед использованием в lecture).

### A7. JLR (Jaguar Land Rover) — predictive defect detection (2024-2025)
- **Тип задачи.** Visual + acoustic анализ на финальной inspection.
- **Эффект.** Заявка: -25% defect leakage rate; не нашёл конкретный публичный source для production deployment. **Требует дополнительной верификации.**
- *Лучше использовать BMW/VW кейсы как more verifiable.*

---

## B. Электроника / полупроводники

### B1. TSMC — Deep Learning Defect Detection + Yield Optimization
- **Тип задачи.** Wafer defect detection + classification; yield prediction; supply chain orchestration.
- **Inputs/outputs.** Billions of wafer images → defect class + position; sensor data → yield prediction → process parameter tuning.
- **Эффект.** 95% accuracy на defect classification; +10-15% yield улучшение; AI agents автономно орчестрируют fab operations.
- **Дата.** TSMC Arizona fab — volume production late 2024; Japan Kumamoto fab — end of 2024.
- **Failure mode.** Не disclosed public; общеотраслевая проблема — distribution shift при transition к новым process nodes (3nm→2nm).
- **Источники:**
  - [Indium.tech — AI Semiconductor Fabrication](https://www.indium.tech/blog/ai-advantage-semiconductor-fabrication-defect-detection-yield-optimization/);
  - [klover.ai — TSMC AI Agents](https://www.klover.ai/tsmc-uses-ai-agents-10-ways-to-use-ai-in-depth-analysis-2025/);
  - [TSMC 2024 Annual Report](https://investor.tsmc.com/static/annualReports/2024/english/index.html).

### B2. Foxconn — FoxBrain + Smart Manufacturing
- **Тип задачи.** Injection-molding parameter tuning, defect detection, mold design ramp-up, agentic robot control.
- **Inputs/outputs.** FoxBrain (Llama 3.1 70B derivative) + sensor + vision → mold parameters; robotic manipulator instruction.
- **Эффект.** «Software performs ~80% of work to configure equipment for fresh production run». Cutting product dev timelines by half (claim). NVIDIA DGX SuperPOD training infra; Nurabot nursing robot (адаптация для других sectors).
- **Дата.** FoxBrain unveiled март 2025; Computex 2025 demo май 2025.
- **Failure mode.** Foxconn CEO **Young Liu (май 2025)**: «AI and robotics will take over assembly lines» — но конкретный production-replacement scope не disclosed; **disruption-warning** для low-end manufacturing jobs (см. файл 07 цитаты).
- **Источники:**
  - [foxconn.com — Computex 2025](https://www.foxconn.com/en-us/press-center/press-releases/latest-news/1601);
  - [manufacturingdive.com — FoxBrain](https://www.manufacturingdive.com/news/foxconn-apple-deepseek-llm-ai-model-foxbrain/742231/);
  - [9to5mac — Foxconn AI replacing humans](https://9to5mac.com/2025/05/21/foxxconn-ai-and-robotics-replace-humans/);
  - [theregister — Foxconn predicts AI destroys low-end jobs](https://www.theregister.com/2025/05/20/foxconn_chair_ai_manufacturing_predictions/).

### B3. Samsung Austin / Texas — fab vision QC (2024-2025)
- **Тип задачи.** Wafer + packaging defect detection.
- **Эффект.** Cмежные сообщения о применении AI в semiconductor packaging (Samsung Foundry); public detail metrics ограничены. Самый verifiable аспект — Samsung Texas $17B fab.
- *Менее verifiable чем TSMC; использовать как secondary mention.*

### B4. Intel — оборудование fab + agentic agents (2024-2025)
- **Тип задачи.** Anomaly detection в process equipment.
- **Public detail metrics ограничены.** Использовать как secondary mention.

---

## C. Aerospace assembly (без overlap с lec-09 mission systems)

### C1. Boeing — AI quality inspection 737 (Renton, Everett, 2024+)
- **Тип задачи.** CV-based defect detection на fuselage + composite materials.
- **Inputs/outputs.** Machine vision cameras + AI algorithms → real-time defect detection (cracks, misalignments, irregularities).
- **Эффект.** Deployed early 2024 на 737 Renton/Everett line; планы — South Carolina. 787 Dreamliner assembly: AI-enhanced scanning detects micro-fractures composite materials. Photo-driven AI part validation tool — декабрь 2025.
- **Failure mode (важно для лекции).** Boeing 737 MAX 9 door-plug blow-out — январь 2024. Boeing mechanics в Renton **reinstalled door plug improperly**. AI quality system это **не предотвратил**. FAA capped 737 production at 38/month. Production at Everett delayed 12 months. **Boeing Spirit AeroSystems** (Wichita) — about 50 jets needed rework due to improperly drilled holes. См. файл 04 подробнее.
- **Источники:**
  - [Avioradar — Boeing AI inspection](https://avioradar.net/en/boeing-introduces-an-ai-tool-that-speeds-up-and-improves-quality-inspection/);
  - [boeing.com — photo-driven AI](https://www.boeing.com/features/2025/12/engineers-use-photo-driven-ai-to-simplify-part-validation);
  - [NPR — Boeing whistleblower quality](https://www.npr.org/2024/01/24/1226666911/boeings-quality-control-draws-criticism-as-a-whistleblower-alleges-lapses-at-fac);
  - [FlightGlobal — Everett 737 Max delayed 12 months](https://www.flightglobal.com/airframers/everett-737-max-line-remains-on-hold-even-as-boeing-eyes-future-rate-rises/165329.article);
  - [NPR — Boeing timeline 2024 problems](https://www.npr.org/2024/03/20/1239132703/boeing-timeline-737-max-9-controversy-door-plug);
  - [orcalean.com — From 737 to Future Boeing AI/Automation](https://www.orcalean.com/article/from-737-to-the-future-how-boeing-uses-automation-and-ai-to-optimize-manufacturing).

### C2. Airbus China Innovation Centre + Accenture (2023-2025)
- **Тип задачи.** AI computer vision для final assembly inspection.
- **Inputs/outputs.** Video feeds → deep learning recognizes когда manufacturing task завершён (e.g., wing attachment — timestamped).
- **Эффект.** Improves consistency defect detection across production lines.
- **Failure mode.** Не disclosed publicly. Айрбас в целом более conservative deploy than Boeing.
- **Источник:** [Accenture — Computer Vision Manufacturing Airbus](https://www.accenture.com/ca-en/case-studies/technology/airbus).

### C3. Rolls-Royce — Predictive QC на engine assembly
- **Тип задачи.** Quality в blade manufacturing + assembly (engineering side overlap с lec-06; здесь — production-side вы).
- *Подробнее в lec-09 для engine-level + MRO scope; здесь только foreshadow.*

---

## D. Consumer goods / упаковка

### D1. P&G — Supply Chain 3.0 + touchless quality (2024-2026)
- **Тип задачи.** Touchless planning / touchless quality / touchless flow в warehouse + manufacturing.
- **Эффект.** ICT budget ~$1.1B/year (2024). AI applications embedded across value chain — molecular research → manufacturing → supply chain → consumer engagement.
- **Failure mode.** Не disclosed.
- **Источник:** [klover.ai — P&G AI 10 ways](https://www.klover.ai/procter-gamble-uses-ai-agents-10-ways-to-use-ai-in-depth-analysis-2025/).

### D2. AB InBev — AI optimisation brewery (2023-2025)
- **Тип задачи.** Filtration process optimization, predictive maintenance, energy efficiency.
- **Inputs/outputs.** Sensor data → model predicts optimal filtration → flow rate adjustment.
- **Эффект.** **+60% beer volume per filtration cycle** (Google Cloud partnership). Bevi chatbot в Brazil: 205 000 queries; +159% engagement в 4 месяца. Beck's Autonomous — первый beer + marketing campaign целиком сделан AI.
- **Failure mode.** Не disclosed; общее AI-market в beverages: $10.8B (2024) → $50B+ к 2030.
- **Источник:** [klover.ai — AB InBev AI strategy](https://www.klover.ai/anheuser-busch-ai-strategy-analysis-of-dominance-in-beverage/); [ab-inbev.com — Transforming beer industry](https://www.ab-inbev.com/news-media/transforming-the-beer-industry).

### D3. Coca-Cola — Microsoft AI supply chain partnership $1.1B (2024)
- **Тип задачи.** Supply chain optimization + automated flavor development.
- **Эффект.** Y3000 — beverage created with AI assistance (PR-driven, не production-impacting).
- **Источники:** [Supply Chain Dive — Coca-Cola Microsoft AI $1.1B](https://www.supplychaindive.com/news/coca-cola-ai-artificial-intelligence-microsoft/714889/); [Marketing Dive — Coca-Cola AI beverage](https://www.marketingdive.com/news/soda-artificial-intelligence-AI-coca-cola-launches-beverage-AB-InBev/693376/).

### D4. Unilever, Heineken — AI quality flavour (2024-2025)
- **Тип задачи.** Sensorial flavour QC, batch consistency check.
- **Public detail ограничено.** Использовать как secondary mention.

---

## E. Российский контекст (public-verifiable only)

### E1. КАМАЗ — autonomous trucks «Маяк-2.5» + assembly automation (2024-2025)
- **Тип задачи.** Конечно беспилотные грузовики (Level-3 ADAS) + AI на production line.
- **Эффект.** 2024: производство 54 600+ commercial vehicles (+3% YoY). 41 677 heavy trucks (включая 6506 K5). К концу 2024 — 18 trucks Level-3 ADAS; 10 единиц — реальная commercial cargo transportation на М-11 «Нева». В 2025 — «Маяк-2.5» обновлённый model + М-12 «Восток» + ЦКАД.
- **Failure mode.** Не disclosed; AI integration scope на production line — `[VFY-day-of]` (нужны public-verifiable metrics).
- **Источники:**
  - [tadviser.ru — Беспилотный автомобиль КамАЗ](https://www.tadviser.ru/index.php/%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82:%D0%91%D0%B5%D1%81%D0%BF%D0%B8%D0%BB%D0%BE%D1%82%D0%BD%D1%8B%D0%B9_%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C_%D0%9A%D0%B0%D0%BC%D0%90%D0%97);
  - [realnoevremya — Маяк-2.5 2025](https://realnoevremya.ru/news/332992-kamaz-predstavit-obnovlennye-bespilotnye-gruzoviki-mayak-25-v-2025-godu);
  - [ixbt.com — КАМАЗ итоги 2024](https://www.ixbt.com/news/2025/01/20/nuzhno-bolshe-kamazov-legendarnyj-rossijskij-proizvoditel-podvjol-itogi-2024-goda.html).

### E2. АвтоВАЗ — public-verified AI production application
- **Поиск не нашёл** specific public-verifiable AI production deployment с metrics (2024-2025).
- **Использование в лекции:** упомянуть как «отсутствует public-verifiable disclosure» — это сам по себе сигнал о состоянии российского транспорта.
- *Лучше не выдумывать кейсы; см. CLAUDE.md instruction.*

### E3. Ростсельмаш — combine assembly AI inspection
- **Поиск не нашёл** public-verifiable metric (2024-2025).
- *Скип, либо оставить только как «отрасль активно adoptит AI» без specific cases.*

### E4. ОДК (Объединённая Двигателестроительная Корпорация)
- **Поиск не нашёл** public-verifiable AI production application с metrics.
- *Скип.*

### E5. Норникель — AI в flotation/grinding (применимо к процессному, см. файл 03)
- Перенесён в process-кейсы.

---

## Cross-cutting observations для плана §2

1. **Главный pattern дискретного производства:** AI = **vision + scheduling + worker augmentation tool**. Не autonomous controller.
2. **Большие предприятия (>$10B revenue) ведут.** SMEs — массово в pilot, но рост ROI пока ограничен.
3. **Российский контекст:** verifiable AI-deployment на public-уровне у КАМАЗ (автономные грузовики, не assembly line); у автозаводов **отсутствие public disclosure — само по себе сигнал**.
4. **Foxconn — extreme case.** Public statement May 2025: AI заменит low-end labour. Это **owner statement**, не реальный измеряемый эффект пока.
5. **Boeing 737 — анти-кейс:** AI inspection не предотвратил door-plug fail. Это переход к failure-bucket (файл 04).
