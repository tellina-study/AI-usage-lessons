# Failures & limits — AI в сельском хозяйстве 2026

> Назначение: первичный источник failure-bucket контента для Лекции 10 «AI в АПК».  
> Правило курса: ≥30% содержания лекции — провалы, ограничения, антипаттерны, альтернативы (CLAUDE.md, AI-Failure & Judgment Rule).  
> Структура: каждый кейс — **факт → цифра → причина → выученный урок → класс bucket → источники**.  
> Класс bucket для удобной разметки в strict-in: `collapse / overpromise / hallucination / connectivity / fairness / sustainability / right-to-repair / RU-impact / robotics-econ / adversarial / knowledge-loss / regulatory / vendor-lock`.

---

## Раздел A. Коллапс vertical farming как класса — 2022–2026

«AI-managed vertical farms спасут мир от голода» — главное обещание 2018–2021. Итог: ~$3 млрд+ потерянного капитала, ≥14 банкротств в 2025-м, **91% год-к-году падение венчурных инвестиций** в indoor farming. Это не «отдельные провалы», а коллапс категории — AI-оптимизация не смогла переломить фундаментальную unit-economics.

### F1. AppHarvest (Чаптер 11, июль 2023) — $700 млн+ в дым

- **Что:** AppHarvest, флагман американского indoor-фермерства, подал на Chapter 11 24 июля 2023. На пике котировался ≈$1 млрд через SPAC (Novus Capital, 2021). В совете директоров — Марта Стюарт, Дж.Д. Вэнс (тогда автор «Hillbilly Elegy», ныне вице-президент США), David Lee (бывший CFO Impossible Foods).
- **Цифры:** долг $341 млн при текущих активах всего $110.6 млн; SPAC-сделка дала ≈$475 млн валовой выручки; акция упала с пиковых $26 (2021) до $0.57 в конце 2022, кратковременно отскакивала на хайпе ИИ-акций до $2.60 (февраль 2023) — это ровно тот «AI-rally», в который инвесторы покупались на разрешение «AI-роботы спасут юнит-экономику», — но рассыпалась обратно.
- **Причины:**
  1. Высокие OPEX (энергия, LED, отопление в Кентукки).
  2. **Tomato brown rugose fruit virus (ToBRFV)** прокатился по флагманской площадке в Морхеде — «dramatic effect» на производство по словам тогдашнего COO Tony Martin. Closed environment не спас, скорее усугубил: вирус один раз проникнув, разносится по всему контуру.
  3. AI-робототехническая уборка преподносилась как преимущество — не закрыла дельту в стоимости энергии и труда.
- **Выученный урок:** AI-system, оптимизирующая параметры в идеальной модели, бессильна перед биологическим патогеном внутри замкнутого контура — closed environment превращает локальную вспышку в total loss. Closed loop = high blast radius. И SPAC-капитал на хайпе АI ≠ долговременная unit-economics.
- **Класс bucket:** collapse / overpromise
- **Sources:**
  - [Indoor farming company AppHarvest files for bankruptcy — Agriculture Dive](https://www.agriculturedive.com/news/appharvest-bankruptcy-indoor-farming-martha-stewart-jd-vance/689039/)
  - [Why Did AppHarvest Go Bankrupt — Financhill](https://financhill.com/blog/investing/why-did-appharvest-go-bankrupt)
  - [AppHarvest IPO via Novus SPAC — The Street](https://www.thestreet.com/investing/appharvest-plans-nasdaq-ipo-through-novus-capital-spac-deal)
  - [Tomato Brown Rugose Fruit Virus — NCBI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9366064/)

### F2. Plenty Unlimited (Chapter 11, март 2025) — почти $1 млрд от SoftBank, Walmart, Bezos в утиль

- **Что:** Plenty Unlimited подала на Chapter 11 23 марта 2025. Закрыла флагманский завод в Compton (Калифорния) в декабре 2024 — спустя 19 месяцев после открытия в мае 2023. Тогда называла его «самой технологически продвинутой indoor vertical farm в мире», 4.5 млн фунтов зелени в год на one city block. Эмерджила из банкротства за 53 дня с DIP-финансированием $20.7 млн.
- **Цифры:** общий привлечённый капитал ≈$940 млн–$1 млрд. Инвесторы: SoftBank Investment Advisers, Walmart, Jeff Bezos (через Bezos Expeditions). Оценка упала с $1.9 млрд (январь 2022) до <$15 млн в начале 2025 — **99% валюаций-коллапс**. Штат после Compton сжат до ≈66 не-юнионизированных сотрудников.
- **Причины:** «There is a big gap between what consumers are willing to pay for leafy greens and the costs of vertical farming». Energy cost в Калифорнии съел AI-оптимизацию. Pivot к клубнике (Ричмонд, VA) — последний шанс на другую margin-категорию.
- **Выученный урок:** «AI-оптимизированный» rooming с LED в Калифорнии стоит дороже, чем salad-mix мерчандайз на полке Whole Foods. Чем плотнее свет и AI-контроль, тем хуже unit-economics на товар с премией <$1.50/кг. Спасает не AI, а pivot в другой product mix.
- **Класс bucket:** collapse / overpromise
- **Sources:**
  - [Plenty files for bankruptcy after raising nearly $1B — TechCrunch](https://techcrunch.com/2025/03/24/vertical-farming-company-plenty-files-for-bankruptcy-after-raising-nearly-1b/)
  - [Plenty closes Compton — The Packer](https://www.thepacker.com/news/industry/plenty-closes-compton-leafy-greens-farm-focus-strawberries)
  - [Plenty Unlimited Chapter 11 Filing — Elevenflo](https://elevenflo.com/blog/plenty-unlimited-bankruptcy)
  - [Bezos-, Softbank-backed Plenty bankruptcy — Bloomberg Law](https://news.bloomberglaw.com/bankruptcy-law/bezos-softbank-backed-vertical-farmer-plenty-files-bankruptcy)
  - [Compton Farm announcement — Compton Chamber of Commerce](https://www.comptonchamberofcommerce.org/post/vertical-farming-company-plenty-closing-up-its-compton-farm)

### F3. Bowery Farming (ABC-процесс, ноябрь 2024)

- **Что:** Bowery Farming — на пике 2021 г. оценена в $2.3 млрд, поддерживалась Наталией Портман и Джастином Тимберлейком (celebrity backing) — прекратила деятельность 4 ноября 2024. Не классический Chapter 11, а ABC (Assignment for the Benefit of Creditors) под управлением Sherwood Partners. 187 сотрудников уволено (104 в Бетлехеме, PA; 83 в Ноттингеме, MD).
- **Цифры:** >$700 млн венчурного капитала привлечено. **$70 млн объект в Locust Grove, Джорджия (200 000 ft²) — крупнейший vertical-farm объект в истории, ушедший в ликвидацию**, $32 млн нового оборудования так и не запустили. Marzo 2025 — аукцион в Arlington, Texas: оборудование, никогда не использованное.
- **Причины:** «struggling to secure financing in recent months», «devastating plant disease outbreak» (вновь биологический фактор), «weak demand».
- **Выученный урок:** $32 млн оборудования не пошло в эксплуатацию вообще — это структурный сигнал не «AI не сработал», а «business model не сработал ДО того, как AI успел сработать». Capex first, AI после — догонять было нечем.
- **Класс bucket:** collapse / overpromise
- **Sources:**
  - [Bowery Farming closes, lays off workers — Agriculture Dive](https://www.agriculturedive.com/news/celebrity-backed-indoor-farming-company-bowery-closes-lays-off-187-workers/732282/)
  - [Bowery Georgia farm heads to liquidation — Fertilizer Daily](https://www.fertilizerdaily.com/20251114-bowery-farmings-70m-georgia-vertical-farm-heads-to-liquidation-as-startups-collapse-triggers-nationwide-sell-offs/)
  - [Bowery Farming is ceasing operations — TechCrunch](https://techcrunch.com/2024/11/04/bowery-farming-is-ceasing-operations/)

### F4. Infarm (банкротство в Германии, Нидерландах, UK — сентябрь 2023)

- **Что:** Infarm — берлинская «vertical farm-as-a-service» внутри супермаркетов — официально объявлена банкротом в Нидерландах 19 сентября 2023; Германия + UK — параллельно; Дания + Франция — exit. Полный уход из Европы.
- **Цифры:** Привлекла ≈$500 млн (Sifted: «raised $500m and then disappeared»). На пике — 2 декабря 2021 — оценена ≈$1 млрд (unicorn). Сократила >50% штата в ноябре 2022; получила ≈$40–50 млн от Qatar Investment Authority как life support. Канадский Торонто-объект продолжает.
- **Причины:** официальное заявление — «energy prices escalated» (≈2× в Европе после начала 2022); supply-chain нарушения; «economic environment».
- **Выученный урок:** Энергозависимая AI-агро-модель в регионе с волатильной энергией = exit risk на каждом скачке цен. Geopolitical-zerstörung modeli (война в Украине → удвоение цен энергии в Европе) топит сразу всю Европейскую сеть. AI здесь не виноват — но без него модель тем более не работает.
- **Класс bucket:** collapse / connectivity-energy-shock
- **Sources:**
  - [Infarm raised $500m and disappeared — Sifted](https://sifted.eu/articles/infarm-raised-500m-and-disappeared)
  - [Dutch arm of Infarm declared bankrupt — Sifted](https://sifted.eu/articles/infarm-bankrupt-netherlands)
  - [Infarm abandons Europe — Just-Food](https://www.just-food.com/news/infarm-abandons-europe-for-regions-better-suited-for-indoor-farming/)
  - [Infarm declared bankrupt — Agfunder News](https://agfundernews.com/infarm-declared-bankrupt-rumored-to-have-raised-50m-from-middle-east-say-industry-source)

### F5. Fifth Season (закрытие 31 октября 2022) — robotics first, business model потом

- **Что:** Pittsburgh-стартап с AI-роботикой для индорной зелени. Прекратил деятельность 31 октября 2022. ≈100 сотрудников. Поставлял salad-kits в сотни магазинов.
- **Цифры:** $35 млн от Drive Capital, 99 Tartans, Reinforced Ventures, Alumni Ventures, Grit Ventures. Объект — 60 000 ft² в Braddock, PA. Планировал экспансию в Колумбус, Огайо — отменена.
- **Причины:** «challenging macroeconomic environment»; робота-first архитектура с высокими CapEx не дала эффекта unit-margin.
- **Выученный урок:** «AI + robotics-first» в leafy greens = долгий cash-burn, не отбиваемый ни одной разумной price-premium для салата. Это не «AI плохой» — это «AI решает не ту задачу, которая является constraint бизнеса».
- **Класс bucket:** collapse / robotics-econ
- **Sources:**
  - [Robotic vertical farming startup Fifth Season shuts down — Agfunder News](https://agfundernews.com/robotic-vertical-farming-startup-fifth-season-shuts-down)
  - [Fifth Season shuts down — Technical.ly](https://technical.ly/startups/fifth-season-shutting-down/)
  - [Fifth Season shutdown — Vertical Farm Daily](https://www.verticalfarmdaily.com/article/9473615/vertical-farming-robotics-startup-fifth-season-shuts-down/)

### F6. Kalera (Chapter 11, апрель 2023) + AeroFarms (Chapter 11, июнь 2023)

- **Что:** Kalera (Орландо, FL) — Chapter 11 4 апреля 2023 в Южном округе Техаса; активы проданы Sandton Capital Partners; liquidating trust для unsecured creditors. AeroFarms (Newark, NJ) — Chapter 11 июнь 2023, $50–100 млн обязательств; вышли из банкротства, превратив Newark-объект в R&D, а production переместили в Danville, VA.
- **Цифры (AeroFarms):** долг 30 инвесторам >$3 млн; ранее обсуждалась SPAC-merger при оценке $1.2 млрд (отменена в 2021); всего привлекли ≈$238 млн (включая Ingka Group, David Chang, David Petraeus).
- **Причины:** «significant industry and capital market headwinds», «attempts to raise sufficient capital have fallen short».
- **Выученный урок:** Когда «капитал-market headwinds» убивает компанию, AI-стек становится curve fit без денег на разворачивание. Если бизнес выживает только на постоянном вливании капитала, любая просадка макро = смерть.
- **Класс bucket:** collapse / overpromise
- **Sources:**
  - [Kalera files Chapter 11 — AgWeb](https://www.agweb.com/news/business/technology/vertical-farmer-kalera-files-chapter-11-bankruptcy)
  - [Kalera liquidating bankruptcy plan — Bloomberg Law](https://news.bloomberglaw.com/bankruptcy-law/vertical-farmer-kalera-gets-liquidating-bankruptcy-plan-approved)
  - [AeroFarms files Chapter 11 — Bloomberg Law](https://news.bloomberglaw.com/bankruptcy-law/indoor-vertical-farmer-aerofarms-files-for-chapter-11-bankruptcy)
  - [AeroFarms bankruptcy analysis — Jersey Digs](https://jerseydigs.com/aerofarms-files-bankruptcy/)
  - [AeroFarms financials — NJBIZ](https://njbiz.com/is-bankruptcy-filing-just-a-temporary-setback-for-aerofarms/)

### F7. Iron Ox + Bright Farms + Upward Farms — серия мелких смертей

- **Iron Ox** (Калифорния, робот-greenhouse) — ноябрь 2022, увольнения ≈50 человек (≈половина штата); закрыли farms-line, оставили «engineering & technology» как cash-runway сохранение. Это не банкротство, но фактический pivot из farm в lab.
- **Bright Farms** — Chapter 11 июнь 2023; вышла в сентябре 2023; рефинансирована в августе 2025, но крупнейший инвестор вышел в декабре 2025 → закрытие Danville, VA. Серия «zombie-recovery».
- **Upward Farms** — на пороге банкротства / closure.
- **Выученный урок:** банкротство в vertical farming — не one-shot event, а procession of zombie-pivot, refinance, second collapse. Маркеры «выжил» и «не выжил» меняются 2–3 раза за 24 месяца. Это сигнал об отсутствии моментуса инноваций category-level: каждый игрок отдельно ищет нишу, но категория не масштабируется.
- **Класс bucket:** collapse / overpromise
- **Sources:**
  - [Iron Ox lays off ~50 — TechCrunch](https://techcrunch.com/2022/11/03/iron-ox-lays-off-50-amounting-to-nearly-half-its-staff/)
  - [14 Vertical Farms Bankrupt in 2025 — Foodlore](https://foodlore.blog/why-vertical-farms-go-bankrupt/)
  - [Why Vertical Farms Keep Failing — AGEYE](https://ageyetech.com/news/vertical-farming-failures-lessons-learned)

### F8. Фундаментальные ограничения vertical farming как класса

Согласно Nature paper (см. Hannah Ritchie) и систематическому обзору MDPI/Sustainability, единственная стоимость освещения в vertical farm для риса/пшеницы — ~**100× рыночная цена этих культур** при энергии $0.10/кВт·ч. Замена ламп каждые 5–10 лет. Тысячи квадратных футов LED не победят бесплатное солнце.

- **Выученный урок:** Любая AI-оптимизация работает на знаменателе. Если знаменатель (стоимость энергии) фундаментально выше в 100×, AI не может закрыть разрыв даже на 30%. Закон термодинамики важнее ML.
- **Класс bucket:** collapse / sustainability (energy)
- **Sources:**
  - [Vertical farming substack — Hannah Ritchie](https://hannahritchie.substack.com/p/vertical-farming)
  - [Towards Sustainable Vertical Farming — MDPI](https://www.mdpi.com/2071-1050/17/18/8142)
  - [Vertical Farming Energy Consumption Per Kg 2025 — Farmonaut](https://farmonaut.com/blogs/vertical-farming-energy-consumption-per-kg-2025-cea)

---

## Раздел B. Generative AI hallucinations в agronomy advice

### F9. ChatGPT/Bard рекомендуют неправильное время применения гербицида (Nature Food, 2024)

- **Что:** Исследовательская группа из США, Великобритании, Кении, Нигерии, Колумбии опубликовала в Nature Food (май 2024) анализ точности GPT-3.5/4.0 для агросоветов фермерам Африки. Тестировали типичные вопросы (fall armyworm, sowing time, пестициды).
- **Цифры:** ChatGPT systematically выдаёт «inaccurate information related to planting time, seed rate, and fertilizer application rate and timing». В одном из задокументированных кейсов **ChatGPT предложил применить гербицид в неправильное окно — что привело бы к significant crop damage**. По pesticide-вопросам про fall armyworm рекомендации были «ambiguous».
- **Причины:**
  1. RAG-grounding отсутствует у consumer-LLM — модель полагается на pre-training corpus, который не включает локализованные US-EPA / EU-EFSA / Россельхознадзор labels.
  2. Confident-tone делает hallucination опасной — фермер без агрономического бэкграунда не различит правильный совет от уверенно-неправильного.
- **Выученный урок:** **«Confident wrong»** опаснее «admitted-don't-know». LLM в agronomy advisory ОБЯЗАНА быть либо RAG-grounded в местных нормативах с цитатами, либо явно отказываться. «Generic chatbot для фермеров» — антипаттерн категории.
- **Класс bucket:** hallucination
- **Sources:**
  - [GPT inaccuracies in agriculture — Phys.org](https://phys.org/news/2024-05-gpt-inaccuracies-agriculture-crop-losses.html)
  - [Be Wary of Relying on Chat GPT for Agricultural Questions — UC Weed Science](https://ucanr.edu/blog/uc-weed-science-weed-control-management-ecology-and-minutia/article/be-wary-relying-chat-gpt)
  - [For Farmers, Are AI Chatbots Worth the Risk? — Ambrook](https://ambrook.com/offrange/technology/chatgpt-risks-and-rewards-for-farmers)
  - [Farmers Are Tentatively Embracing AI — Ambrook](https://ambrook.com/offrange/technology/ChatGPT-AI-farming-hallucinations)

### F10. Plantix — даже 90% точность даёт ≥10% mismatch на dose-критичных диагнозах

- **Что:** Plantix позиционирует accuracy >90% (vs 60–70% у человека-эксперта), полевые трайлы в Индии и Вьетнаме дают 85–90%.
- **Цифры:** 10–15% misdiagnosis — на масштабе 10 млн+ загрузок в год это сотни тысяч неправильных рекомендаций.
- **Причины:** image quality, освещение, варианты культуры; misdiagnosis особенно в early infections, когда визуальная картина disease ≈ nutrient deficiency. App может предложить fungicide, когда нужен только калий, и наоборот.
- **Выученный урок:** Даже хорошая визуальная модель в режиме «90% правильно» означает, что 1 из 10 фермеров получит неправильный совет — а в pesticide-context это ROI-разрушающее событие. Threshold accuracy ≠ deployment readiness — нужна uncertainty-aware рекомендация: «не уверен — спроси эксперта».
- **Класс bucket:** hallucination / overpromise
- **Sources:**
  - [Plantix Role in Disease Management — JETIR](https://www.jetir.org/papers/JETIRGV06074.pdf)
  - [Detecting and managing crop pests with AI — GSMA M4D](https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/programme/agritech/detecting-and-managing-crop-pests-and-diseases-with-ai-insights-from-plantix/)
  - [Best Plant Disease Identification Apps — FarmstandApp](https://www.farmstandapp.com/30754/7-best-plant-disease-identification-apps-for-farmers/)

### F11. «Дай мне рекомендации из этих 10 PDF по моему урожаю» — антипаттерн misuse LLM

- **Что:** Типичная попытка фермера/консультанта: «я загрузил в ChatGPT 10 PDF (агро-руководств, лабораторных отчётов, погодных архивов) — дай рекомендацию».
- **Проблемы:** (1) разрозненные источники → конфликтующие нормы (Россельхознадзор vs EU-EFSA vs Indian Council of Agricultural Research); (2) модель не различает «эта норма для климатической зоны X» vs «для зоны Y», даёт усреднённое; (3) confident-tone маскирует тот факт, что ground-truth не существует — есть локальные нормы, не глобальные; (4) tokenization теряет числовые таблицы.
- **Выученный урок:** PDF-RAG для agronomy advisory без явного «source-locality» в каждом ответе — magnet hallucination. Бесполезно «больше PDF» — нужно «лучше структурированных данных + явное reasoning о применимости к конкретной зоне». Это не задача LLM, это задача expert-system с LLM в качестве UI.
- **Класс bucket:** hallucination / knowledge-loss
- **Sources:**
  - [RAGged Edges: Double-Edged Sword of Retrieval-Augmented Chatbots — arXiv](https://arxiv.org/pdf/2403.01193)
  - [Phantom Transfer: Data-level Defences Insufficient — arXiv](https://arxiv.org/pdf/2602.04899)

---

## Раздел C. Computer vision edge cases — модели ломаются в поле

### F12. CV-модели не выдерживают пыль, дождь, освещение — научный консенсус 2024–2025

- **Что:** Систематический обзор MDPI Agriculture (2024) и arXiv 2508.19511 (август 2025, «Weed Detection in Challenging Field Conditions: Semi-Supervised Framework for Overcoming Shadow Bias») фиксируют: «environmental conditions such as variations in lighting, shadows, dust, or humidity directly affect the vision system's performance».
- **Цифры/механизм:** Color — самый нестабильный признак для plant identification; модели страдают от **shadow bias** (учатся ошибочно классифицировать тени как растительность); морфологическое сходство crop ↔ weed на early growth stages дополнительно ломает классификацию. Деградация качества изображения → классификационные ошибки → снижение overall accuracy.
- **Связь с провалом FarmWise / Naïo:** именно проблема «модели, обученные в тепличных условиях, плохо работают в поле» — структурная причина того, что FarmWise (CV-weed-robot, $30M+ raised) вошёл в restructuring и closure в 2025, а Naïo Technologies (Тулуза) — в judicial recovery в июне 2025, упав с €4 млн выручки (2021) до €2.4 млн (2024).
- **Выученный урок:** «Computer vision robust к пыли/дождю/тени» — обещание, а не реальность. **Без infrared/thermal sensors + ансамблей + on-device adaptation** модели «90% accuracy в тестах» дают 50–60% в реальном поле — exactly та цифра, которая выводит юнит-экономику фермера в минус. Альтернатива: механические weeders без CV (Lemken, Kverneland) — менее «smart», но deterministically robust.
- **Класс bucket:** overpromise / robotics-econ
- **Sources:**
  - [Weed Detection in Challenging Field Conditions — arXiv 2508.19511](https://arxiv.org/pdf/2508.19511)
  - [Computer Vision for Site-Specific Weed Management Review — MDPI](https://www.mdpi.com/2077-0472/15/21/2296)
  - [FarmWise Announces Wind Down — IGrowNews](https://igrownews.com/farmwise-latest-news/)
  - [FarmWise closure leaves farmers in limbo — Farm Progress](https://www.farmprogress.com/technology/farmwise-closure-leaves-farmers-in-limbo-as-ag-tech-faces-investment-hurdles)
  - [Naïo Technologies financials — aginsights](https://www.aginsights.blog/naio-technologies-france/)

### F13. Monarch Tractor — «autonomous» оказался не autonomous (ноябрь 2025)

- **Что:** Monarch Tractor (Калифорния, autonomous electric tractor, основан выходцами Tesla + Carlo Mondavi) — корпоративный мемо в ноябре 2025: до 102 увольнений, риск shutdown. Идахо-дилер Burks Tractor подал иск, заявив, что Monarch продал «defective» машины 2024 года, которые «unable to operate autonomously» — обещанная функциональность не работала.
- **Цифры:** Привлекли $220 млн+ ($133 млн в 2024). Потеряли контрактного производителя Foxconn в начале 2025.
- **Причины:** Тяжёлый pivot из hardware-OEM в SaaS-autonomy для существующих тракторов — «timing of the transition puts Monarch at risk of shut down».
- **Выученный урок:** Маркетинг продукта как «autonomous» при том, что autonomy не выдержит судебной проверки — структурная trap для всей категории. AI-autonomy in agriculture — это не yes/no, а градиент с десятками edge cases, каждый из которых может привести к иску от дилера. Demo ≠ deployment.
- **Класс bucket:** overpromise / robotics-econ / regulatory
- **Sources:**
  - [Monarch Tractor preps for layoffs — TechCrunch](https://techcrunch.com/2025/11/19/monarch-tractor-preps-for-layoffs-and-warns-employees-it-may-shut-down/)
  - [Monarch Tractor sued over non-autonomous tractors — TechCrunch](https://techcrunch.com/2025/11/18/monarch-tractor-sued-over-tractors-that-were-unable-to-operate-autonomously/)
  - [Monarch Tractor warns 102 staff — TechBuzz AI](https://www.techbuzz.ai/articles/monarch-tractor-warns-102-staff-of-layoffs-possible-shutdown)
  - [Electric Tractor Innovator Sued by Dealer — Farm Equipment](https://www.farm-equipment.com/articles/24747-electric-tractor-innovator-monarch-tractors-is-sued-by-dealer-lays-off-staff)

### F14. Strawberry-harvesting robot — экономика всё ещё не сходится

- **Цифры (2024):** Один робот-сборщик клубники — $200 000–350 000 capex; annualized capex + maintenance $68 000–130 000 в год. Адресуемый ручной труд в США — $50 млрд; роботы занимают <5%. Калифорния: $43 000 на акр в год только на picking-labor.
- **Реальная цифра:** «Harvesting is the last great unsolved problem in agricultural robotics», harvesting robots «still struggle with tasks humans master in days».
- **Выученный урок:** Когда у задачи есть human baseline «обучается за дни», robotics-ML стек не догоняет за годы и десятки миллионов R&D. Pilot ≠ production. Десятки strawberry-startup в pilot, единицы — в commercial revenue stream. Альтернатива: H-2A guest worker programs + ergonomic improvements (стульчатые комбайны), пока robotics не догонит.
- **Класс bucket:** robotics-econ
- **Sources:**
  - [Harvesting Robots: $6.9B Market — RobotToday](https://robottoday.com/article/harvesting-robots-a-6-9-billion-market-and-the-last-frontier-of-farm-automation)
  - [Modular autonomous strawberry picking — J. Field Robotics](https://onlinelibrary.wiley.com/doi/full/10.1002/rob.22229)
  - [DailyRobotics strawberry harvester — Agfunder News](https://agfundernews.com/dailyrobotics-gears-up-for-commercial-launch-in-california-in-2026-with-robotic-strawberry-harvester)

---

## Раздел D. Connectivity / edge-network ограничения

### F15. 18% американских ферм без интернета вообще, ≤40% на стабильном fixed-line

- **Цифры:** 18% американских ферм — no internet access at all; только 40% — fixed (DSL/cable/fiber); остальные — на cellular/satellite. **39% rural Americans без широкополосного доступа** vs 4% urban. Только 69% rural имеют stable broadband. Развёртывание broadband на farmland даст $65 млрд/год через прирост yields при стоимости $35–40 млрд (BroadbandNow).
- **Связь с AI:** Любая cloud-AI pipeline (Climate FieldView, Granular, ClimateAI) предполагает 24/7 uplink. Для 60% фермеров США это либо невозможно, либо unreliable.
- **Выученный урок:** Маркетинговый сценарий «AI optimizes your tractor in real-time через cloud» — фантазия для большинства farms. **Edge-AI / TinyML** — единственная реалистичная архитектура; «cloud-first AI for agriculture» = архитектурная ошибка. **Альтернатива:** offline-first edge ML (Edge Impulse, TinyML на ESP32/STM32) с периодической синхронизацией; именно то, что Россия и Африка вынуждены делать де-факто.
- **Класс bucket:** connectivity
- **Sources:**
  - [Internet connectivity troubles plague farmers — Feedstuffs](https://www.feedstuffs.com/agribusiness-news/internet-connectivity-troubles-plague-farmers)
  - [Missed Connections — Ambrook Offrange](https://ambrook.com/offrange/technology/internet-access-broadband-rural-smart-farming)
  - [Deploying Broadband to Rural Farmland — BroadbandNow](https://broadbandnow.com/report/deploying-broadband-rural-farmland)
  - [Affordable Precision Agriculture: TinyML Review — arXiv 2603.15085](https://arxiv.org/pdf/2603.15085)

### F16. Starlink — спасение или новая зависимость?

- **Что:** Starlink стал де-факто backbone для рассредоточенных ферм, особенно после ухода John Deere из РФ и в Африке.
- **Цифры:** $90/мес «excess capacity», $120/мес «limited», конгест-сборы $100–1000 единовременно; железо $175 self-install. Reliability проблемы: снег, дождь, физические obstructions; «video calls failed», «documents failed to save».
- **Выученный урок:** Spar single-vendor — single point of failure. Илон Маск в одностороннем порядке прекращает Starlink для Украины в критическом моменте — а та же логика применима к фермерам в любой юрисдикции, попавшей в Twitter-спор. **AI-агро без redundant connectivity = бизнес на одной вертикальной верёвке**. Альтернатива: hybrid (cellular + LoRa + Starlink) + edge buffering.
- **Класс bucket:** connectivity / vendor-lock
- **Sources:**
  - [Starlink internet from rural savior to unreliable luxury — XDA](https://www.xda-developers.com/starlink-internet-rural-savior-unreliable-luxury/)
  - [Starlink Internet Service 2024 Review — CircleID](https://circleid.com/guides/starlink-internet-service)

### F17. GPS-jamming и spoofing в Финляндии (Россия-EU border) делают AI-тракторы «unfarmable»

- **Что:** Stanford GPS Lab observations (ITM 2025): начиная с 2022, российские EW-станции, направленные на Украину, имеют побочный эффект — джемят GNSS-сигнал в Финляндии, Эстонии, Латвии, Литве. В апреле 2023 — джамминг в 15 регионах РФ против украинских дронов.
- **Цифры:** **>122 000 авиа-рейсов с GNSS-interference только за первые 4 месяца 2025**. Финские фермеры: «areas of farms are reportedly unfarmable using GNSS-based tractors and combines because of the interference from Russian EW installations». ICAO Assembly осудил Россию в октябре 2025.
- **Выученный урок:** Прецизионное земледелие (auto-steer, variable-rate seeding/spraying) полностью завязано на GNSS. Электронная война = делает AI-стек агро бесполезным на сотни километров. **Альтернатива:** RTK с земным radio-link, dual-frequency GNSS (L1/L5), INS (inertial) fusion — но всё это дороже и сложнее. Прецизионное земледелие — civilian victim военной электроники.
- **Класс bucket:** connectivity / adversarial / RU-impact
- **Sources:**
  - [GNSS Spoofing in Russia 2023-2024 — Stanford ITM 2025](https://web.stanford.edu/group/scpnt/gpslab/pubs/papers/Lo_ION_ITM_2025_Russia_Spoofing.pdf)
  - [GNSS jamming — Wikipedia](https://en.wikipedia.org/wiki/GNSS_jamming)
  - [Recent GPS jamming in regions of geopolitical conflict — GPS World](https://www.gpsworld.com/innovation-recent-gps-jamming-in-regions-of-geopolitical-conflict/)
  - [Electronic Warfare Puts Commercial GPS Users on Notice — Dark Reading](https://www.darkreading.com/cybersecurity-operations/electronic-warfare-commercial-gps-users-notice)

---

## Раздел E. Vendor lock-in, right-to-repair и «AI-driven equipment = monopolization»

### F18. FTC v. John Deere (январь 2025) — иск за антиконкурентные практики ремонта

- **Что:** 15 января 2025 FTC + Illinois и Minnesota Attorneys General подали иск против Deere & Co. за «unfair practices» — десятилетиями ограничивающих способность фермеров и независимых ремонтников чинить оборудование Deere. Только Deere-authorized dealers имеют доступ к software repair tool (Service ADVISOR), который требуется для всех full-functional repairs. Федеральный судья отклонил попытку Deere прекратить дело, trial expected later 2026.
- **Контекст:** Nebraska — один из ранних штатов (2017), где обсуждали Right to Repair; National Farmers Union + локалы в Iowa, Nebraska, Missouri, Ohio, Wisconsin — годы advocacy. Апрель 2026: Deere settle отдельный class-action lawsuit.
- **Выученный урок:** **Чем больше AI и telematics в трактор, тем сильнее vendor lock-in.** Фермер не «покупает» $500k комбайн с AI-стеком — он «лицензирует» право его использовать пока Deere разрешает. Тот же паттерн, что у Tesla с FSD subscription. Альтернатива: open-source farming hardware (Farm Hack, OGGM), но эти решения 10× дешевле и 10× менее «smart».
- **Класс bucket:** right-to-repair / vendor-lock / regulatory
- **Sources:**
  - [FTC Sues Deere & Company — FTC Press Release](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-states-sue-deere-company-protect-farmers-unfair-corporate-tactics-high-repair-costs)
  - [John Deere and Right to Repair Over the Years — PIRG](https://pirg.org/resources/john-deere-and-right-to-repair-over-the-years/)
  - [FTC sues John Deere — NPR](https://www.npr.org/2025/01/15/nx-s1-5260895/john-deere-ftc-lawsuit-right-to-repair-tractors)
  - [Deere Settles Class Action Right-to-Repair Lawsuit — Farm Policy News](https://farmpolicynews.illinois.edu/2026/04/deere-settles-class-action-right-to-repair-lawsuit/)

### F19. John Deere remote-brick столен(ых) в Украине тракторов (май 2022)

- **Что:** Российские военные украли 27 единиц техники John Deere из Мелитополя; перевезли в Чечню (≈800 км). На месте — техника не стартовала. **Deere дистанционно «забрикала» все 27 устройств** через GPS + VIN-locking.
- **Цифры:** **$5 млн потерянных Deere-machines** для воровавших; для Deere — proof-of-concept удалённого contol.
- **Двойная оптика:**
  1. С точки зрения Украины — это успешное anti-theft применение AI/IoT.
  2. С точки зрения concerns: эта же technology означает, что Deere может «забрикать» оборудование любого фермера, не оплатившего подписку, не подписавшего EULA-обновление, оказавшегося под санкциями. Россия после 2022 — точно этот сценарий: техника перестала получать updates, parts, и medical repair tool.
- **Выученный урок:** **«AI security feature» сегодня = «AI control surface» завтра.** Тот же mechanism, который благодаря которому украденный комбайн не работает в Чечне, является основанием тревоги для каждого фермера: ваш трактор может быть brickовать удалённо. Право собственности на оборудование становится фиктивным. CSO Online прямо указал на этот «agriculture security concerns».
- **Класс bucket:** right-to-repair / vendor-lock / RU-impact
- **Sources:**
  - [John Deere disables Ukraine tractors — The Register](https://www.theregister.com/2022/05/02/ukrainian_tractors_deere/)
  - [Remote bricking raises agriculture security concerns — CSO Online](https://www.csoonline.com/article/572811/remote-bricking-of-ukrainian-tractors-raises-agriculture-security-concerns.html)
  - [John Deere remotely disables $5M stolen tractors — LADBible](https://www.ladbible.com/news/latest-john-deere-remotely-deactivates-tractors-stolen-by-russian-army-20220510)

### F20. Российский провал импортных AI-систем (2022→н.в.)

- **Что:** John Deere прекратил поставки оборудования и сервисных частей в Россию + Беларусь с февраля 2022 — добровольное корпоративное решение, не санкционная обязанность (USDA fact sheet: agricultural equipment не входит в санкционный режим). Climate FieldView, Bayer-owned, в России фактически не действует; Bayer закрыл seed deals → потеря исторических полевых данных у российских агро-холдингов. Microsoft + Amazon ушли в 2022 (Yandex попытался заместить).
- **Цифры:** Российский импорт тракторов и комбайнов **упал на 40% относительно 2013**; продажи агро-машин в РФ Q1 2025 — $473.3 млн (–32.9% YoY). **35 000 фермерских хозяйств закрылись за 5 лет**. В Ростовской области в 2024 — >400 фермеров вышли из бизнеса.
- **Выученный урок:** Зависимость от иностранных AI-стэков (Climate FieldView, John Deere telematics, IBM Food Trust) превратилась в moment of catastrophic failure при политическом разрыве. **Российский опыт — это natural experiment**: что бывает, когда импортный AI-стек отключается. Альтернатива «отечественная замена» работает медленно (Сбер, Яндекс.Аграрная аналитика, Cognitive Pilot) и в ограниченных сегментах. **Урок для всех стран периферии: AI-зависимость = политический риск.**
- **Класс bucket:** RU-impact / vendor-lock / regulatory
- **Sources:**
  - [John Deere Suspends Shipments to Russia — Deere Press](https://www.deere.com/en/stories/featured/john-deere-suspends-shipments-to-russia/)
  - [Deere Concludes Sale of Russian Leasing Arm — DTNPF](https://www.dtnpf.com/agriculture/web/ag/equipment/article/2023/03/14/deere-concludes-sale-russian-leasing)
  - [OFAC Food Security Fact Sheet: Russia](https://ofac.treasury.gov/media/924341/download)
  - [Санкции уничтожают агросектор России — Обозреватель](https://www.obozrevatel.com/ekonomika-glavnaya/analytics-and-forecasts/sanktsii-unichtozhayut-agrosektor-rossii-fermeryi-ostalis-dazhe-bez-traktorov.htm)
  - [Как чиновники и санкции разрушают сельское хозяйство — НГС](https://ngs.ru/text/economics/2025/03/27/75267146/)

### F21. FCC ban DJI/Autel + ag-spray drone ground risk (декабрь 2025)

- **Что:** 22 декабря 2025 FCC добавила все foreign-made drones + UAS-критические компоненты в Covered List → запрет на новые product authorizations. DJI занимает **80% всех ag-spray drone flights в США**; китайские в целом — ~90% рынка дронов.
- **Цифры:** В 2024 — 10.3 млн акров обработаны спрей-дронами в США, ≈$215 млн revenue от custom applications. Не-китайские альтернативы в среднем в **2.5× дороже**.
- **Выученный урок:** Vendor lock-in на geopolitical уровне: AI-стек агро-дрона перестаёт работать не потому что AI стал хуже, а потому что геополитика отрезала supply chain. Стратегия «купи DJI и спокойно живи» — не работает. Альтернатива (Skydio для США, Autel для других, Geo-scan для РФ) дороже и хуже, но «суверенна». Та же логика, что у F20.
- **Класс bucket:** vendor-lock / regulatory / connectivity
- **Sources:**
  - [Ag spray drones face Chinese tech ban — North Dakota Monitor](https://northdakotamonitor.com/2025/08/17/ag-spray-drones-are-just-taking-off-but-a-ban-on-chinese-tech-could-ground-the-industry/)
  - [FCC ban new foreign-made drones — CBS News](https://www.cbsnews.com/news/fcc-ban-new-foreign-made-drones-china-balks/)
  - [Stefanik Countering CCP Drones Act — Press Release](https://stefanik.house.gov/2024/9/stefanik-s-countering-ccp-drones-act-passes-house)
  - [Farmers brace for shortages after FCC drone ban — Farm Progress](https://www.farmprogress.com/technology/farmers-brace-for-shortages-after-fcc-drone-ban)

---

## Раздел F. Fairness / bias в loan + insurance AI

### F22. USDA discriminatory lending pattern — 2024 $2.2 млрд payout

- **Что:** Discrimination Financial Assistance Program (IRA Section 22007, авторизован Biden в 2022; первые выплаты — 2024) — компенсация фермерам, столкнувшимся с дискриминацией в USDA-lending до 2021. ≈43 000 фермеров получили выплаты до $500 000; средняя — $82 000; общий объём программы $2.2 млрд.
- **Цифры (NPR analysis 2022):** Из всех демографических групп самый низкий рейтинг одобрения — Black farmers: одобрено 36% заявок, отклонено 16% (выше всех). Для white farmers — одобрено 72%, отклонено 4%.
- **Угол AI:** На этих исторически biased данных уже строятся AI credit-scoring системы (Apollo Agriculture в Африке, Esusfarm с Microsoft, ICTU + Springer 2024). Историческая bias запекается в обучающую выборку → AI воспроизводит дискриминацию scale-fully.
- **Доп. развитие:** В июле 2025 USDA отменил «socially disadvantaged» preference — действовавший >30 лет — заявив, что «discrimination has been sufficiently addressed». Black Farmer Discrimination case (Pride v. USDA) ведётся, federal judge отклонил motion to dismiss.
- **Выученный урок:** Если ground-truth выборка исторически дискриминативна, ML-модель воспроизведёт ту же дискриминацию даже без явной race-feature. **AI fairness требует counterfactual reasoning о data generation process, не просто demographic parity post-hoc**. Альтернатива: human-in-the-loop + бессмысленные decisioning только из защищённых данных + audit.
- **Класс bucket:** fairness / regulatory
- **Sources:**
  - [Black farmer discrimination Pride v USDA — PELaws](https://www.pelaws.com/black-farmer-discrimination)
  - [USDA $2B Discrimination Payout — Agriculture Dive](https://www.agriculturedive.com/news/usda-black-minority-farmers-discrimination-payments/723051/)
  - [USDA Ends Race and Gender Consideration — Civil Eats](https://civileats.com/2025/07/10/usda-ends-consideration-of-race-and-gender-for-grants-and-loans/)
  - [USDA issues payments to Black farmers — NPR](https://www.npr.org/2024/08/02/nx-s1-5060394/usda-issues-payments-to-address-discrimination-against-black-farmers)

### F23. FCA UK Consumer Duty 2024 — AI risk concerns в финуслугах (insurance/lending)

- **Что:** Bank of England Survey 2024: 75% UK firms используют AI (vs 58% в 2022). FCA не вводит «bespoke AI rulebook» — применяет existing Consumer Duty.
- **Концерны:** «AI-driven discriminatory outcomes in credit scoring or insurance pricing»; «data bias and representativeness»; «explainability»; «bad consumer outcomes». Перенос на agriculture: insurance pricing для фермеров строится на satellite + climate data; если модель систематически переоценивает risk для smallholders в конкретных регионах — это discriminatory outcome.
- **Выученный урок:** AI в agri-insurance/lending без explicit fairness audit = высокий regulatory risk. Тот же FCA framework доходит до того, что фермер может оспорить отказ в credit, ссылаясь на Consumer Duty — это новая категория юридических рисков для AgriFin-tech.
- **Класс bucket:** fairness / regulatory
- **Sources:**
  - [AI Update — FCA](https://www.fca.org.uk/publication/corporate/ai-update.pdf)
  - [AI in UK Financial Services 2024 — Bank of England](https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024)
  - [Navigating FCA AI Rules — Formiti](https://www.formiti.com/data-privacy-news/the-fca-s-ai-reckoning-how-uk-financial-services-can-navigate-the-2026-accountability-crisis)

---

## Раздел G. Sustainability paradox — AI сам по себе уничтожает water/energy ресурсы для агро

### F24. Data centers в Айове против иригации

- **Цифры:** Айова — **104 дата-центра** (76 в Des Moines area), привлечены налоговыми льготами + дешёвой энергией. Один центр потребляет 300 000–1 250 000 галлонов воды/день. **В 2024 один дата-центр в Айове потребил 1 млрд галлонов** — водоснабжение всей Айовы на 5 дней. Microsoft использовал **48.7 млн галлонов** на свои West Des Moines DC через сентябрь 2025. Meta в Альтуне — до **16% муниципального водоснабжения**.
- **Сравнение:** Microsoft в West Des Moines — 2–7% месячного забора Water Works. Lawn watering + irrigation — ≈40% в peak. То есть AI-data-centers пока меньше irrigation, но **растут двузначными темпами**.
- **AI training cost:** Training GPT-3 в US datacenters Microsoft — **700 000 литров пресной воды**. Прогноз AI water usage к 2027 — **6.6 млрд м³**. 2/3 дата-центров с 2022 — в water-stressed регионах.
- **Парадокс:** Чтобы AI помог агро экономить воду через precision irrigation, AI-training потребляет воду в количествах, сопоставимых с irrigation. Net-positive ROI водяной — открытый вопрос.
- **Выученный урок:** «AI для устойчивости» имеет собственный environmental footprint. Net-zero claim надо считать end-to-end, не только на user-side. **Альтернатива:** smaller models, edge inference (что и так нужно по reason F15), on-device training.
- **Класс bucket:** sustainability
- **Sources:**
  - [Iowa Grapples with Data Centers and Water — InformationWeek](https://www.informationweek.com/sustainability/iowa-grapples-with-data-centers-and-demand-for-water)
  - [Energy, water use as data centers expand in Iowa — Business Record](https://www.businessrecord.com/energy-water-use-under-close-watch-as-data-centers-expand-in-iowa/)
  - [How Much Water Do AI Data Centers Really Use — Undark](https://undark.org/2025/12/16/ai-data-centers-water/)
  - [Data Center Water Use Environmental Impact — AKCP](https://www.akcp.com/index.php/2025/09/02/truth-about-data-water-footprint-of-data-centers/)
  - [Data Centers and Water Consumption — EESI](https://www.eesi.org/articles/view/data-centers-and-water-consumption)

---

## Раздел H. Carbon credit / sustainability AI inflation

### F25. Verra phantom credits — 94% rainforest offsets «worthless» (Guardian/Die Zeit/SourceMaterial, январь 2023)

- **Что:** 9-месячное расследование The Guardian + Die Zeit + SourceMaterial: из rainforest offset credits Verra (мировой лидер voluntary offsets market, $2 млрд/год) **>90% — «phantom credits», не представляющие реальных carbon reductions**. Кэмбриджское исследование 2022 показало: угроза лесам была переоценена **в среднем на 400%** в Verra-проектах.
- **Связь с AI:** AI-стартапы (Pachama, Sylvera, NCX, BeZero Carbon) используются как «AI-verifier» для carbon credits. Foodwatch обнаружил, что один из Pachama-projects (Bosques Amazónicos в Перу) **переоценил предотвращённое обезлесение в 8 раз**, и сам поставщик BAM признал, что harvesters уничтожали лес, за который им платили за защиту.
- **Indigo Ag soil carbon:** Заявляет 2 млн метрических тонн verified soil carbon impact (5 cropов). Но фундаментальная критика: soil carbon measurement из satellite/MRV — это inference, не direct measurement; неточность ≥20–30% в любую сторону.
- **Выученный урок:** AI-MRV (Monitoring, Reporting, Verification) для carbon-claims — это inference с большой uncertainty, marketed как «precise measurement». **«AI сказал X тонн CO2» — это hypothesis, не fact**. Whitewashing carbon-credit + AI-veneer = scaled greenwashing.
- **Класс bucket:** overpromise / sustainability / regulatory
- **Sources:**
  - [Verra Phantom Credits — Business & Human Rights Resource](https://www.business-humanrights.org/en/latest-news/new-investigations-calls-phantom-credits-90-of-rainforest-carbon-offsets-certified-by-leading-global-standard-incl-companys-reaction/)
  - [94% Forest Carbon Offsets are Phantom — EcoWatch](https://www.ecowatch.com/phantom-credits-verra.html)
  - [The Carbon Con — Source Material](https://www.source-material.org/vercompanies-carbon-offsetting-claims-inflated-methodologies-flawed/)
  - [Soil carbon credits emerge from disillusionment — Trellis](https://trellis.net/article/indigo-ag-boomitra-soil-carbon-credits/)

---

## Раздел I. Adversarial attacks / data poisoning в agricultural AI

### F26. Data poisoning угроза в outsourced training (2024 ScienceDirect)

- **Что:** «Security threats to agricultural artificial intelligence: Position and perspective» (Computers and Electronics in Agriculture, 2024) + «Seeds of Deception: Securing AI-Driven Agriculture» (ICAIR 2024) формулируют: когда training outsourced 3rd-party, attacker может implantить backdoor через poisoning trainset. Detection в outsourcing-сценариях «extremely challenging».
- **Реальный impact:** Backdoor может вызывать misclassification disease detection — фермер не лечит, теряет урожай. GMO-репозитории в облаке → exposed to AI exploitation.
- **Adversarial patches на remote sensing:** Springer Nature 2024 (Multi-patch Adversarial Attack on Remote Sensing) + MDPI 2025 (Spatially Adaptive Mini-Patch Attacks on Object Detection в satellite) — академические работы показывают, что **adversarial patches могут сбить классификацию crop/satellite imagery**. Применимость к agriculture monitoring + crop insurance fraud — прямая.
- **Выученный урок:** **AI-pipeline в agriculture редко учитывает access control и data integrity** (цитата ScienceDirect). Любая supply chain trust-issue (3rd-party data labeler, cloud-trained foundation model) — это enable adversarial vector. Альтернатива: on-premise training, in-house data labeling, model integrity verification (вес-signature).
- **Класс bucket:** adversarial
- **Sources:**
  - [Security threats to agricultural AI — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0168169924009487)
  - [Seeds of Deception: Securing AI-Driven Agriculture — ICAIR 2024](https://papers.academic-conferences.org/index.php/icair/article/download/4386/3948/15749)
  - [Multi-patch Adversarial Attack for Remote Sensing — Springer](https://link.springer.com/chapter/10.1007/978-981-97-2303-4_25)
  - [Spatially Adaptive Mini-Patch Attacks — MDPI Electronics](https://www.mdpi.com/2079-9292/14/17/3433)

---

## Раздел J. AI vs traditional agronomy — где «дед сказал — лучше любого ML»

### F27. Опыт фермеров cover crops > наивные ML-рекомендации

- **Что:** Nature Food 2021, farmer-led trial 1522 strip-years across 78 farms 9 US states 5 years — cover crops улучшают soil health индикаторы (но эффект медленный, малый, накапливающийся 5+ лет). Critical finding: **experienced cover crop users (>5 лет опыта) — самые низкие costs и самые высокие profitability** vs новые adopters.
- **Что это значит:** Тонкое знание «когда сеять cover, какой mix, как terminate, как соотнести с следующей культурой» — приобретается годами наблюдения за **локальной**: климатом, почвой, drainage, weed pressure. Этот knowledge — tacit, не documented. AI-модель, обученная на агрегированных trial data, **систематически усредняет** локальную специфику и даёт «average» рекомендацию.
- **Выученный урок:** Microclimate intuition + многолетняя память о поле — ground truth, который ML не может построить из satellite + IoT за 1 сезон. **AI rich там, где есть много исторических данных + slowly-changing dynamics; AI беден там, где critical knowledge — tacit + ultra-local**. Альтернатива: AI как «augment», предлагает hypothesis; фермер с 20-летним опытом проверяет / отклоняет. Не «AI prescribes — farmer executes».
- **Класс bucket:** knowledge-loss / overpromise
- **Sources:**
  - [Large-scale farmer-led experiment cover crops — Nature Food](https://www.nature.com/articles/s43016-021-00222-y)
  - [Experience Plays A Role in Cover Crop Profitability — Soil Health Partnership](https://www.soilhealthpartnership.org/blog-story/experience-plays-a-role-in-cover-crop-profitability/)
  - [Understanding farmer knowledge of soil — Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/21683565.2023.2270451)

### F28. Small dataset → deep learning overfit → классические методы выигрывают

- **Что:** Систематический review (Tandfonline 2023, Nature Sci.Rep. 2025, PMC 11667600) фиксирует: для большинства agricultural yield forecasting **классические ML (Random Forest, XGBoost) обходят deep learning** на типичных farm-level datasets. CNN/LSTM «not advantageous for crop yield forecast when compared to XGBoost, especially for small feature datasets».
- **Цифры:** Random Forest R²=0.875 для irish potatoes, 0.817 для кукурузы; для cotton XGBoost — лучший. Deep models — «risk of overfitting and as a result, lower model performance in practice».
- **Выученный урок:** «Deep learning everywhere» — антипаттерн в agriculture. Datasets обычно мелкие (одно поле, 5–10 лет), feature-set ограничен — это **режим, где interpretable классические методы доминируют**. AI-консалтинги, продающие «нейронку для вашей фермы», нередко проигрывают XGBoost-моделям, которые фермер мог бы себе позволить за бесплатно через scikit-learn. **Альтернатива:** XGBoost + cross-validation + interpretable feature importance.
- **Класс bucket:** overpromise / knowledge-loss
- **Sources:**
  - [Is deeper always better? Evaluating DL for yield forecasting with small data — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10482790/)
  - [Comparative study ML models in crop yield — Discover Agriculture (Springer)](https://link.springer.com/article/10.1007/s44279-025-00335-z)
  - [Deep learning for crop yield prediction: systematic review — Tandfonline](https://www.tandfonline.com/doi/full/10.1080/01140671.2022.2032213)

---

## Раздел K. Health & safety — autonomous tractor & drone accidents

### F29. California ban на driverless tractors — safety vs productivity argument

- **Что:** Калифорния поддерживает запрет на driverless tractors / autonomous farm robots; нарушения — до $16 285, при injury/death — до $25 000 per occurrence. **Ни одного государственного штрафа по этой норме не выписано** (декабрь 2025). Фермеры лоббируют отмену запрета.
- **Цифры контекста:** Tractor overturns — leading cause of agricultural fatalities, ~**130 смертей в год** в США (OSHA). Tractor-related в целом — ~90 смертей в год primarily через rollover.
- **Угол AI:** Регуляторика отстаёт от технологии — статус «autonomous tractor» юридически неоднозначен (см. F13: Monarch sued за obraz «autonomous», который не работал). Если случится первая массовая авария «autonomous tractor», регуляторный backlash может «заморозить» категорию на 5+ лет.
- **Выученный урок:** Регуляторная неопределённость + единичная авария = категорический риск для всей AI-категории. Та же история с self-driving cars (Uber-incident 2018 в Tempe заморозил AV-индустрию на 18 месяцев). Альтернатива: «supervised autonomy» (оператор обязан быть на/в машине) — это снижает productivity ROI, но позволяет постепенный rollout.
- **Класс bucket:** regulatory / robotics-econ
- **Sources:**
  - [California's ban on driverless tractors — NBC Bay Area](https://www.nbcbayarea.com/news/local/autonomous-farming-agriculture-equipment-california/3878319/)
  - [Tractor Safety Laws Struggle to Keep Up — Valley Ag Voice](https://www.valleyagvoice.com/tractor-safety-laws-struggle-to-keep-up-with-automation/)
  - [Protecting Agricultural Workers from Tractor Hazards — OSHA](https://www.osha.gov/sites/default/files/publications/OSHA3835.pdf)
  - [REDECA framework for agricultural tractor drivers — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12136288/)

### F30. Drone incidents в agriculture — растущая популяция, статистика молчит [VFY-day-of]

- **Что:** US drone fleet — ~800 000 зарегистрированных как of октября 2024 (DoT/FAA). Ag-spray drones — 10.3M акров в 2024 (рост >50% YoY). Pilots обязаны report accident в FAA в течение 10 дней при serious injury / loss consciousness / property damage >$500.
- **Что НЕ найдено:** прозрачной публичной статистики «ag-drone accidents → injuries» — это **пробел в данных**. Известны единичные случаи (XAG drone crash after takeoff в Facebook-группе пользователей), no aggregated reporting. NTSB накапливает данные по UAS-инцидентам, но не разбивает на ag vs hobby.
- **Выученный урок:** Industry growing 50%+ YoY без granular safety data — recipe для безотчетного roll-out. AI-autonomy в ag-spray означает, что drone летит над полем без human-in-the-loop; failure mode (battery, controller, wind gust) приводит к падению с pesticide-tank. Никто пока не считал, сколько worker-injuries это даёт.
- **Класс bucket:** regulatory / safety
- **Sources:**
  - [How many drone injuries/deaths — FAA FAQ](https://www.faa.gov/faq/how-many-people-have-had-life-threating-injures-or-been-killed-small-uas-or-drone-falling-them)
  - [Drone Injuries and Safety Recommendations — UF/IFAS](https://ask.ifas.ufl.edu/publication/AE560)
  - [When do I need to report accident — FAA](https://www.faa.gov/faq/when-do-i-need-report-accident)
  - [Drone Accidents Personal Injury — Heidari Law](https://www.heidarilawgroup.com/blog/drone-accidents-and-personal-injury-legal-rights-and-responsibilities/)

---

## Раздел L. Сводный антипаттерн-каталог (для использования в strict-in блоках)

Каждый из следующих антипаттернов — это **критерий «здесь AI не нужен / не применим»** или сравнение с правильной альтернативой. Готов для прямого вкрапления в chapter / slides / speech как strict-in блок.

| # | Антипаттерн | Правильная альтернатива (не-AI или другой AI/метод) |
|---|---|---|
| AP1 | «Generic LLM (ChatGPT/Bard) как farm advisor» | RAG-grounded в local regulator (USDA-EPA, EU-EFSA, Россельхознадзор); явный отказ при low confidence; human-in-the-loop экстеншн-агент |
| AP2 | «AI optimizes vertical farm — экономика сойдётся» | Открытый грунт + greenhouse при energy <$0.10/кВт·ч; vertical только для high-value crops (микрозелень, медицинская конопля, фарма-травы) |
| AP3 | «Cloud-AI tractor 24/7 telemetry» | Edge-AI на устройстве + периодическая sync; TinyML; offline-first |
| AP4 | «Deep learning everywhere для yield» | XGBoost + Random Forest для small datasets; interpretable, audit-friendly |
| AP5 | «AI MRV → carbon credits» | Direct soil sampling + transparent uncertainty bands; AI как hypothesis, не как fact |
| AP6 | «AI-driven equipment = vendor solution» | Open-source farming hardware (Farm Hack, Open Source Ecology); right-to-repair compliance |
| AP7 | «Generic chatbot UX для smallholders» | Голосовое interface на local language + voice-first (Digital Green/Microsoft EsusFarm); USSD/SMS fallback |
| AP8 | «Computer vision weed detection в любых условиях» | Mechanical weeder (Lemken, Kverneland) + manual oversight; CV только при стабильной освещённости + IR/thermal fusion |
| AP9 | «AI replaces farmer's microclimate intuition» | AI augments (предлагает hypothesis), farmer validates; ground-truth остаётся у фермера, AI обучается у него, не наоборот |
| AP10 | «AI for sustainability — net positive автоматически» | End-to-end LCA включая обучение модели + data center water; small models, edge inference |
| AP11 | «Single-vendor satellite/comms» | Hybrid (cellular + LoRa + Starlink + RTK ground link); redundancy |
| AP12 | «AI credit scoring без fairness audit» | Counterfactual fairness audit + human-in-the-loop отказы + право апеллировать |
| AP13 | «Closed-loop indoor farm = pest-free» | Open-grown с IPM + crop rotation; closed loop ↑ blast radius при одной точечной инфекции (ToBRFV → AppHarvest) |
| AP14 | «Autonomous tractor без operator» | Supervised autonomy + явный disclosure capability / non-capability; не маркетировать demo как production (Monarch lesson) |
| AP15 | «Foreign foundation model для local advisory» | Локализованная fine-tune + культурно-климатическая адаптация; ↑ risk vendor lock + sanctions cut-off (Russia 2022 lesson) |

---

## Итог / Самые недокументированные пробелы

**1. Drone safety statistics в agriculture** — растёт 50%+ YoY, no granular data; нужен FAA + OSHA mandatory reporting [VFY-day-of].  
**2. Real impact of AI credit-scoring bias на smallholders в Африке / Индии** — Apollo Agriculture + Esusfarm заявляют millions farmers served, но independent audit fairness отсутствует.  
**3. Adversarial-attacks в production deployment** — академические работы есть, реальные incidents (если кто-то атаковал crop insurance modeling) не публикуются — асимметрия информации.  
**4. End-to-end LCA AI-pipeline в agriculture** — никто не считает total water/energy footprint AI-обучения + inference + data transfer + edge devices vs offset gains от precision irrigation. Net-positive — недоказанное утверждение.  
**5. Tacit knowledge fermierов как «training data»** — захват tacit knowledge старого поколения фермеров (cover crops, soil intuition, microclimate) в AI до того, как поколение уйдёт — узкое окно (10–20 лет).
