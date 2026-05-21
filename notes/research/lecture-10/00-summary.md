# Research Summary — Лекция 10 «AI в сельском хозяйстве»

> Сводка по 4 research-документам (01-real-applications, 02-failures-and-limits, 03-trends-2026, 04-russian-context). Цель — отобрать материал для плана v1: топ-кейсы, топ-тренды, топ-провалы, кандидаты в keystone-ось, scope cuts.
>
> Дата: 2026-05-21. Worktree: `/tmp/lec-10-wt`. Issue: #126.

---

## 1. Top-15 кейсов для лекции

Отбор по принципу: (а) есть verifiable метрики ≥ 2025; (б) покрывает один из ключевых таксономических уровней (поле / роботы / животноводство / supply chain / advisory); (в) баланс success/failure/mixed/connectivity/russian; (г) даёт несомненный inженерный урок.

| # | Кейс | Сегмент | Bucket | Зачем в лекции |
|---|---|---|---|---|
| 1 | **John Deere See & Spray Ultimate** | Полевые культуры / целевой спрей | **success** | 5 млн акров 2025; –50% гербицидов; +2 bu/A. Канонический success-case современного prescription-AI. Vendor-lock + retrofit ограничения — оговорки. |
| 2 | **Carbon Robotics LaserWeeder G2** | Robotics / weeding | **success-narrow** | 250k акров обработано; 15 млрд weeds уничтожено; $1.4М на машину. Замена химии физикой через CV — конкретная альтернатива. |
| 3 | **xarvio FIELD MANAGER (BASF)** | Agronomy decision support | **success** | 130k фермеров, 20 млн га, 100 стран. Японский outcome-based rice yield guarantee 2025 — production-уровень advisory. |
| 4 | **Climate FieldView (Bayer)** | Farm data management | **success-with-caveats** | 250 млн акров / 23 страны; >50% US corn/soy/cotton. Хороший пример vendor lock-in и US-Midwest bias за пределами Corn Belt. |
| 5 | **Monarch Tractor MK-V** | Autonomous tractor | **failure-strict-in** | Иски Idaho-дилера ноябрь 2025: «sold defective tractors unable to operate autonomously». 102 увольнения, риск shutdown. Канонический demo-≠-production урок. |
| 6 | **Plenty Unlimited (Chapter 11, март 2025)** | Vertical farming | **failure-strict-in** | $940M–$1B потеряно; valuation $1.9B → <$15M (99%). Compton закрыт через 19 мес. AI-оптимизация не победила unit-economics LED-зелени. |
| 7 | **AppHarvest (Chapter 11, июль 2023)** | Indoor / greenhouse | **failure-strict-in** | $700M+ в дым; ToBRFV virus прошёл по closed environment. Урок: closed loop ↑ blast radius при биологическом patогене. |
| 8 | **Allflex SenseHub + CattleEye** | Животноводство / здоровье | **success** | 2 млн коров smonitored на SenseHub (milestone 2025); CattleEye — lameness detection из CCTV (60 ферм, 11 000 коров). Конкретный продакшен пример. |
| 9 | **Cargill CMAX + CarVe + 2026 BIG AI Award** | Supply chain / agentic | **success** | Predictive port logistics + CV для protein yield; победитель 2026 BIG AI Excellence Award. Agentic в commodity ladder. |
| 10 | **Tract (Cargill+ADM+Olam+LDC)** | Supply-chain intelligence | **success-emerging** | €18.6M Series A 2025; 4 anchor customers (competitors!). Backbone для agentic procurement / Scope-3. |
| 11 | **Plantix (PEAT/Helm AG)** | Disease detection (smartphone advisory) | **mixed** | 10 млн загрузок, 7 млн пользователей Индия, >90% accuracy vs 60–70% человек-эксперт. 10–15% misdiagnosis = сотни тысяч неправильных рекомендаций в год — урок об uncertainty-aware deployment. |
| 12 | **Cognitive Agro Pilot (РФ)** | Автопилот комбайнов / CV | **mixed / russian** | 1200+ установок; +25% производительности, –13% потерь (заявлено). 4 иска фермеров на 12,7 млн ₽ в 2025 — CV не работает в пыли. Учебный российский case-study. |
| 13 | **John Deere remote-brick стола техники в Мелитополе (май 2022)** | Connectivity / vendor-lock | **connectivity / russian** | 27 единиц на $5М удалённо «забрикано». Двойная оптика: anti-theft vs vendor-control. |
| 14 | **F18 GPS-jamming в Финляндии / Эстонии (2022→)** | Connectivity / adversarial | **connectivity / russian** | >122 000 авиа-рейсов с GNSS-interference (Q1 2025). Финские поля «unfarmable using GNSS-based tractors» — точное земледелие как civilian victim EW. |
| 15 | **FTC v. John Deere (январь 2025)** | Right-to-repair / vendor-lock | **failure-strict-in** | FTC + IL + MN AG иск за десятилетние ограничения ремонта. Trial ожидается 2026. Чем больше AI, тем сильнее lock-in. |

Дополнительные narrow cases для иллюстраций (вне топ-15, but used in slides): Saga Robotics Thorvald (UV-C ночные роботы для клубники, 20% UK market), Tevel Aerobotics (flying apple pickers), Solinftec Solix (24/7 solar autonomy), Aigen Element gen2 (solar mechanical weeder, $50k), ИТЭЛМА (спутниковый автопилот РФ), РСХБ «Своё Фермерство» (10 000 партнёров).

---

## 2. Top-5 трендов 2026 (лекционно-релевантные)

Из ~30 трендов 03-trends-2026 отобрано 5, которые (а) показывают качественный сдвиг 2024→2026, (б) пригодны для пояснения студенту-инженеру 3 курса, (в) имеют конкретные доказательные точки.

1. **Foundation models приходят в АПК с задержкой 2–3 года.** TerraMind (IBM + ESA, 2025) — «GPT-3 момент» для Earth observation, 1 трлн токенов pretrain; Prithvi-EO 2.0 для agricultural monitoring. Agriculture-specific (AgriFM, AgriGPT, AgroBench) — на стадии «GPT-1». Урок: домен догоняет общую AI-индустрию с лагом — это **окно для инженерных решений на проверенных архитектурах**, но и риск устаревания на горизонте 5 лет.

2. **Agentic AI лидирует в commodity trading и procurement, отстаёт on-farm.** McKinsey: «leading players are redesigning their commercial, hedging, logistics, and risk workflows for agentic AI» — Cargill, ADM, COFCO. Revenue.ai whitepaper: –25..35% hedge slippage, +40% faster quote turnaround у early adopters. **On-farm agentic — всё ещё PoC**: «один agent оркестрирует ферму от посева до сбора» не существует в 2026. Причина: traders measure outcome в basis-points (короткий feedback loop), farmers — в сезонах. Конкретный урок: AI поднимается по supply chain (где быстрый measurable ROI), стопорится в поле.

3. **Specialization побеждает generic.** Robots, выжившие 2025–26 — узкие: Tevel = ripeness apple picker, Saga = ночные UV-C на клубнике, Solinftec = 24/7 solar field-bot. Generic «farm robot» = failure pattern (Monarch MK-V, FarmWise, Naïo в judicial recovery). **Урок для инженера**: «универсальный AI-помощник для фермера» — антипаттерн категории.

4. **EU AI Act = первая регуляторная стрелка, дошедшая до commercial enforcement в АПК.** Действует с августа 2024; **agricultural machinery с AI safety components** = high-risk classification. Producers (XAG, AGCO, Bonsai, Naïo) нуждаются в compliance teams. Liability cascade: производитель трактора + AI provider + фермер — кто отвечает за autonomous collision? Конкретный пример прикладной регуляторики, который инженер должен учитывать в design.

5. **USDA Climate-Smart Commodities отменён (апрель 2025) = federal policy = tail risk для AgTech.** $3.1B программа Biden-era свёрнута Trump-administration; некоторые проекты под AMP выжили, многие — collapsed. **Урок**: business model, опирающаяся на public funding, fragile. Investor sentiment 2025–26 — preference к unit economics over policy-tailwind plays.

---

## 3. Top-10 failure-cases для strict-in bucket (≥30% mandate)

Эти кейсы строго in-bucket — с явным уроком, ограничением или альтернативой; готовы к прямому вкраплению в chapter / slides / speech как failure-блоки.

| # | Failure case | Strict-in урок | Альтернатива |
|---|---|---|---|
| 1 | **Vertical farming collapse 2022–26** (AppHarvest, Plenty, Bowery, Infarm, AeroFarms, Kalera, Fifth Season + 14 банкротств 2025 на $1.37B+) | AI-оптимизация работает на знаменателе. Если знаменатель (стоимость LED-энергии ≈ 100× рыночная цена культуры) фундаментально выше, AI не закрывает разрыв даже на 30%. Закон термодинамики важнее ML. | Открытый грунт или greenhouse при энергии < $0.10/кВт·ч; vertical только для high-value crops (микрозелень, медицинская конопля, фарма-травы). |
| 2 | **ChatGPT/Bard hallucinations в agronomy advisory (Nature Food 2024)** | Confident-wrong опаснее admitted-don't-know. Generic LLM как «farm advisor» — антипаттерн категории. | RAG-grounded в local regulator (USDA-EPA, EU-EFSA, Россельхознадзор) + явный отказ при low confidence + human-in-the-loop экстеншн-агент. |
| 3 | **Plantix 10–15% misdiagnosis на dose-критичных диагнозах** | Threshold accuracy ≠ deployment readiness. На масштабе 10 млн+ загрузок — сотни тысяч ошибочных pesticide-рекомендаций в год. | Uncertainty-aware рекомендация: «не уверен — спроси эксперта»; calibrated confidence + abstention. |
| 4 | **Monarch Tractor «autonomous» не autonomous (ноябрь 2025)** | Маркетинг как «autonomous», который не выдержит судебной проверки — структурная trap. Demo ≠ production. | Supervised autonomy + явный disclosure capability / non-capability на каждое заявление. |
| 5 | **18% американских ферм без интернета вообще** + GNSS-jamming в Финляндии | Cloud-AI pipeline 24/7 uplink — фантазия для большинства farms. «Cloud-first AI for agriculture» = архитектурная ошибка. | Edge-AI / TinyML / offline-first; hybrid (cellular + LoRa + Starlink + RTK ground link) для redundancy. |
| 6 | **FTC v. John Deere (январь 2025) + remote-brick Мелитополь (май 2022)** | Чем больше AI и telematics в трактор, тем сильнее vendor lock-in. «AI security feature» сегодня = «AI control surface» завтра. | Open-source farming hardware (Farm Hack, Open Source Ecology) + right-to-repair compliance; multi-vendor стратегия. |
| 7 | **USDA discriminatory lending → $2.2B payout (2024)** | На исторически biased данных строятся AI credit-scoring системы — historical bias запекается в обучающую выборку, AI воспроизводит дискриминацию scale-fully. | Counterfactual fairness audit + human-in-the-loop отказы + право апеллировать. |
| 8 | **Data centers vs irrigation (Айова: 1 центр = 1 млрд галлонов / год)** | «AI для устойчивости» имеет собственный environmental footprint. Net-positive ROI водяной — открытый вопрос. | Smaller models + edge inference + on-device training; считать end-to-end LCA, не только user-side. |
| 9 | **Verra phantom credits — 94% rainforest offsets «worthless»** (Pachama overestimate в 8 раз) | AI-MRV для carbon-claims — это inference с большой uncertainty, marketed как «precise measurement». Scaled greenwashing. | Direct soil sampling + transparent uncertainty bands; AI как hypothesis, не как fact. |
| 10 | **Cognitive Agro Pilot vs пыль — 4 иска фермеров на 12,7 млн ₽ (РФ 2025)** | CV-система, заявленная для уборки, не работает в условиях, для которых маркетируется. ИТЭЛМА (спутниковый стек) — структурно другая альтернатива на той же платформе («Кировец»). | GNSS / RTK-based навигация когда CV ломается; mechanical / спутниковая альтернатива «AI не нужен, спутник проще»; pre-purchase verification физических условий. |

Дополнительно (используются как минор-блоки): Iron Ox closure, Bowery $70M Georgia liquidation Nov 2025, Naïo Technologies judicial recovery (€4M → €2.4M revenue), FarmWise wind-down, FCC ban DJI ag-drone supply, California ban на driverless tractors, US Climate-Smart Commodities cancellation, Russian госпрограмма «Цифровое сельское хозяйство» — цель удвоения производительности не достигнута (АПК в 2024 −3,2%).

---

## 4. Главные tensions / противоречия / открытые вопросы 2026

1. **Closed-loop vs open-environment AI.** Медтех (Лекция 7) — controlled environment, AI работает. АПК — open environment, AI ломается там же, где промышленность ожидает success. Это **фундаментальный сдвиг**, который курс должен явно артикулировать.

2. **Specialization vs generalist tradeoff.** Generic farm robot не работает; но и десятки специализированных роботов — это **«робот для каждой задачи»** = unmanageable parc. Открытый вопрос: где правильная грануляция?

3. **Vendor lock-in как стратегический риск.** John Deere remote-shutdown в Мелитополе — successful anti-theft с точки зрения Украины; пример vendor control с точки зрения фермера, который потерял доступ к технике. Та же логика для российских хозяйств, у которых FieldView отключили. Где граница «полезной безопасности» и «политического риска»?

4. **AI как net-positive для устойчивости vs AI как net-negative water/energy burner.** Data centers в Айове vs irrigation; GPT-3 training = 700 000 литров воды. Net-positive — недоказанное утверждение для значительной части AI-стека.

5. **Smallholder gap.** Gates Foundation $1.4B на climate adaptation в Африке + Южной Азии (COP30 2025); AIM for Scale — 40М индийских фермеров на SMS-advisories. Vs Cropin Sage GenAI (PepsiCo, Walmart). Но **gap между smallholder и large-farm AI остаётся**: data, sensor infra, connectivity — barriers не решены.

6. **Federal policy = tail risk.** Climate-Smart cancellation, FCC ban DJI ag-drones — каждое политическое решение перевыставляет ROI-картину для целых классов решений. Plan-надёжность business model страдает.

7. **Regulatory вакуум vs over-regulation.** EU AI Act = first commercial enforcement в АПК; но «human-centric» подход provides minimal consideration to environmental / biodiversity / animal welfare. US — отстаёт, USDA AI Strategy FY2025-26 формальна. РФ — «АПК будущего» 2026–2030 в формате декларации.

---

## 5. Candidate narrative-оси (keystone-axis options)

### Option A. «Closed-loop vs open-environment AI: почему AgTech ломается там, где медтех работает»

**Pro.** Прямой контраст с Лекцией 7 (медицина = controlled, AI работает). Объясняет, **почему** vertical farming collapsed, **почему** Cognitive Pilot ломается в пыли, **почему** computer vision weeders не выдерживают полевые условия. Глубокий, инженерно-нагруженный.

**Con.** Не покрывает supply chain / agentic / advisory полностью; для этих сегментов вторичен. Может быть слишком теоретический.

### Option B. «Where AI saves vs where AI fails: economics of agricultural AI» (success/failure dichotomy)

**Pro.** Прямо соответствует AI-Failure & Judgment Content Rule (≥30%). Лёгкий для понимания студентом. Естественно даёт structured failure-блоки.

**Con.** Не несущая методологическая ось — это **scoring rubric**, а не **концептуальный каркас**. Не помогает выбрать архитектуру.

### Option C. «Foundation models встречают неструктурированную среду: 4 слоя адаптации»

**Pro.** Современная, актуальна 2026, прямо про FM-сдвиг (TerraMind, AgriFM, AgriGPT). 4 слоя — natural taxonomy.

**Con.** Узка для лекции: foundation models — только часть АПК AI; vertical farming, robotics, advisory — не вписываются естественно. Риск over-academic.

### Option D. «Vertical farming катастрофа как урок unit-economics для AI-driven industry»

**Pro.** Драматичный, единый исторический нарратив. Понятен бизнес-аудитории.

**Con.** Узка — это **один кейс на лекцию**, не несущая ось. Перекос на failure без покрытия success-кейсов.

### Option E. **«Agentic AI поднимается по supply chain, robotics стопорится в поле»** — **РЕКОМЕНДУЕМАЯ**

**Pro.** Прямо отражает 2026-наблюдение (Top-trend #2 + #3): где AI реально создаёт ценность (commodity trading, supply-chain optimization, demand forecasting — короткий feedback loop, measurable ROI) vs где он pilot-ует уже 10 лет без commercial breakthrough (universal farm robot, vertical farming). Объясняет одновременно success (Cargill CMAX, Tract, See & Spray на 5М акров) и failure (Plenty, Monarch, vertical farming collapse). Естественно даёт 5 уровней: **поле → робот → животноводство → supply chain → retail/потребитель** — таксономическая лестница, где AI penetration растёт по мере удаления от биологической непредсказуемости.

**Con.** Не покрывает явно регуляторику + российский контекст — нужно как «meta-уровень» сверху лестницы. Менее теоретически элегантна, чем Option A.

### Финальная рекомендация: **Option E** + injection «closed-loop vs open-environment» из Option A как объяснительный механизм на 2-3 уровнях лестницы (vertical farming + robotics provals).

---

## 6. Что НЕ войдёт в лекцию (scope cuts)

| Что отрезаем | Почему |
|---|---|
| Глубокая теория RL для autonomous tractors | Не нужно инженерам уровня 3-курса; в Лекции 2 уже было про архитектуры. |
| Foundation model architecture details (AgriFM Video Swin Transformer) | Уровень детализации не соответствует overview-лекции; в Лекции 3 покрыто общее. |
| AlphaFold + CRISPR-GPT для plant breeding | Пограничный сегмент с биотехом; не работает как ось АПК-лекции, заслуживает отдельной лекции по биотеху, если она будет. |
| BlackSky / Maxar / Planet Labs в подробностях | Перекрытие с Лекцией 9 (ISR, sense-уровень) — там разобрано глубоко; в L10 — кратко в контексте precision agriculture monitoring. |
| EU AI Act полный compliance breakdown | Слишком юридически; достаточно 1 абзаца «high-risk classification + liability cascade». Глубже — в Лекции 16 (регуляторика и этика, если такая будет). |
| Полная panoram of all 37 named cases в research-01 | Невозможно за 75 минут; в лекцию идут 15 топ-кейсов + 10 narrow для иллюстраций (см. §1). |
| Cropin / Tradesprint / Procuresprint detailed agentic flows | Один обобщённый блок про agentic-в-supply-chain (через Cargill + Tract); не уходим в технические детали SaaS-продуктов. |
| LAWS-adjacent применения дронов в АПК | Хотя FCC ban DJI пересекается с темой Лекции 9, в L10 — только как пример vendor lock-in, не LAWS. |
| Полная теория carbon credits markets | Достаточно одного блока Verra phantom credits + Indigo as case; глубже — отдельная тема. |
| MES / ZIIoT / Жировой комбинат Русагро | Слишком отраслево-узко; в L10 упомянуть Русагро Тех + Прогресс Агро +5% ROI как РФ-success примеры, без MES-deep-dive. |
| Гидропоника / аквапоника / специфическая агрономия | Лекция про AI, не про agronomy — упоминаем только в контексте vertical farming collapse как business model issue. |

---

## 7. Ключевые источники for fact-check (приоритет)

Цитировать в plan и chapter, верифицировать перед лекцией ([VFY-day-of] для метрик ≤ 1 мес давности):

1. **John Deere See & Spray** — пресс-релиз deere.com/en/news/all-news/see-spray-technology-across-5-million-acres/ (2025-11), AgTechNavigator 2025-11-10.
2. **Monarch Tractor lawsuit + layoffs** — TechCrunch 2025-11-18 + 2025-11-19; Farm Equipment 24747 (Burks Tractor v. Monarch).
3. **Plenty bankruptcy** — TechCrunch 2025-03-24, Bloomberg Law, Sifted.
4. **AppHarvest + ToBRFV** — Agriculture Dive 689039, NCBI PMC9366064.
5. **Carbon Robotics LaserWeeder G2** — businesswire 2025-02-10, geekwire.com 2025.
6. **Allflex SenseHub 2M cows** — merck-animal-health-usa.com/newsroom/2-million-cows-monitored.
7. **Cargill 2026 BIG AI Award** — cargill.com/2026/cargill-wins-2026-big-artificial-intelligence-excellence-award.
8. **Plantix metrics** — plantix.net + Wikipedia + JETIR papers.
9. **Cognitive Agro Pilot иски** — RTVI ii-dal-sboj-fermery-..., Фонтанка 2026-01-26.
10. **John Deere Мелитополь remote-brick** — The Register 2022-05-02, CSO Online 572811.
11. **FTC v. John Deere** — ftc.gov/news-events/news/press-releases/2025/01/.
12. **ChatGPT in agronomy hallucinations** — Phys.org 2024-05 + Nature Food 2024.
13. **GNSS jamming in Finland/Baltics** — Stanford GPS Lab ITM 2025 paper.
14. **USDA Climate-Smart cancellation** — usda.gov/about-usda/news/press-releases/2025/04/14/.
15. **EU AI Act applied to agrifood** — Cambridge EJRR + FoodTimes.

---

## 8. Cross-cutting наблюдения для plan-v1

1. **Лекция должна быть структурирована вокруг таксономической лестницы**, а не по «успех/провал» (то это разбито в каждый уровень).
2. **Vertical farming — пиковый failure-case**, но рассыпан по разным разделам (unit-economics → раздел Robotics-econ; closed-loop ToBRFV → раздел Open-vs-closed; SPAC pump → раздел Hype patterns), а не один блок.
3. **Российский слой** — встроен в каждый уровень лестницы как параллельный track (Cognitive Pilot vs CV-roboты; ИТЭЛМА vs autonomous tractors; РСХБ vs Cargill agentic; ЭФКО vs Cropin), не отдельный раздел в конце.
4. **Anti-AI критерии** — собраны в финальном разделе (~5 явных «когда не AI»), но материал для каждого готовится по ходу лекции.
5. **Hero-image для s01** — кандидаты: See & Spray Ultimate в работе (Deere press URL → og:image), LaserWeeder в поле, или Cognitive Pilot на «Кировце» в Краснодарском крае.
6. **Hero для s39** — bridge к Лекции 11 (дискретное и процессное производство): робот в поле → шасси на конвейере; либо общий процессный pipeline «от поля до тарелки» (показывает связь с next).

---

**Word count:** ~1500.
**Coverage:** все 4 research-документа проанализированы; ключевые tensions выделены; keystone-кандидаты с pro/con; failure-bucket подготовлен на ≥30%.
