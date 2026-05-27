---
part: 2
of: 4
parent: "chapter.md"
title: "Глава 16. Часть 2: Раздел 2 — Q3 разведка фронтиров + HPC-гонка"
lecture_number: 16
length_words: ~7700
status: draft
version: v1
---

---
**Навигация:** [← Часть 1 (Введение + R0 + R1)](chapter.md) | **вы здесь** (Раздел 2 — Q3) | [Часть 3 (R3 + R4) →](chapter-part3.md) | [Часть 4 (R5 + Q&A + источники) →](chapter-part4.md)

---

## Оглавление (Часть 2)

- [§ Раздел 2. Q3 — разведка фронтиров: physics-first, AI augmentation](#-раздел-2-q3--разведка-фронтиров-physics-first-ai-augmentation)
  - [§2.1. Связь с keystone-осью: data-беднейший квадрант](#21-связь-с-keystone-осью-data-беднейший-квадрант)
  - [§2.2. HPC-гонка: Eni HPC6 и Aramco METABRAIN](#22-hpc-гонка-eni-hpc6-и-aramco-metabrain)
  - [§2.3. SLB Lumi — отраслевые foundation models поверх Petrel и Delfi](#23-slb-lumi--отраслевые-foundation-models-поверх-petrel-и-delfi)
  - [§2.4. ExxonMobil Discovery 6: 4D-сейсмика от месяцев к неделям](#24-exxonmobil-discovery-6-4d-сейсмика-от-месяцев-к-неделям)
  - [§2.5. Провал 1: BP + Beyond Limits (2018–2023, $20 млн, vendor pivot)](#25-провал-1-bp--beyond-limits-20182023-20-млн-vendor-pivot)
  - [§2.6. Провал 2: IBM Watson + Repsol Kalimba (2014–2022, тихое сворачивание)](#26-провал-2-ibm-watson--repsol-kalimba-20142022-тихое-сворачивание)
  - [§2.7. Альтернатива: Eclipse / INTERSECT / CMG / OpenFOAM — physics simulators](#27-альтернатива-eclipse--intersect--cmg--openfoam--physics-simulators)
  - [§2.8. Фундаментальные ограничения Q3: sparse data + multi-physics surrogate gap](#28-фундаментальные-ограничения-q3-sparse-data--multi-physics-surrogate-gap)
  - [§2.9. Самопроверка по Q3](#29-самопроверка-по-q3)

## § Раздел 2. Q3 — разведка фронтиров: physics-first, AI augmentation

<!-- for-slide-s13 -->

### §2.1. Связь с keystone-осью: data-беднейший квадрант

[for-slide-s13]

В первом разделе мы изучили квадрант Q1, где данных много и физика известна. AI работает как мультипликатор, но 86% пилотов всё равно застревают. Теперь мы **спускаемся в data-беднейший квадрант** — Q3, разведку фронтиров. Здесь профиль AI кардинально иной: данные структурно мало, физика хорошо описана, и AI вынужден работать **не вместо физики, а поверх неё** — как ускоритель пластовой симуляции, как инструмент предварительного отсеивания (screening) для геолога, как **большая универсальная модель** (foundation model — модель, обученная на огромных универсальных датасетах и затем дообучаемая под узкие задачи), отвечающая на вопросы инженера на естественном языке по 90 годам корпоративных архивов.

**Размер выборки в Q3.** Каждая разведочная скважина в новом районе (англ. **wildcat well** — разведочная скважина в новом неосвоенном районе; на сленге — «дикая кошка», поскольку результат непредсказуем как охота на дикого зверя) стоит **50–100 миллионов долларов** на офшорном глубоководном бурении и существенно меньше — но всё равно $5–20 млн — в наземной разведке. Невозможно «собрать ещё данных» без коммерчески-несостоятельных расходов. **Размер обучающей выборки для нового бассейна** ≈ 1–5 скважин. Это структурно мало для любого современного ML-метода, включая foundation models.

**Что это значит для AI.** Foundation models, обученные на 90 годах данных Saudi Aramco (METABRAIN — мы разберём её в §2.2) или на доступной библиотеке скважин SLB Petrel (Lumi — §2.3), **не обобщаются** на новый бассейн с принципиально иной геологией. Бассейн Tarim в Китае не похож на Пермский. Восточно-африканский рифт не похож ни на тот, ни на другой. Pre-salt Brazil в ранней разведочной фазе — каждый случай уникален. AI здесь даёт **предварительное отсеивание и ускорение существующих рабочих процессов** (foundation model отвечает «вот 5 потенциальных локаций для бурения, проверь их», и **старший геофизик делает финальную интерпретацию**), а не «замену геолога». И всё, что обещало большее — провалилось публично (см. §2.5 BP+Beyond Limits и §2.6 IBM+Repsol).

**HPC-гонка как ответ на разреженные данные.** Если данных мало, но физика известна — это означает, что **симуляционные модели становятся эталонной разметкой**, и ускорение симуляций даёт существенный прирост. Поэтому в Q3 наблюдается **гонка high-performance computing** (HPC — высокопроизводительные вычисления): Aramco тренирует METABRAIN на собственных HPC-кластерах; Eni построила HPC6 (Top500 #5 в декабре 2024 года); ExxonMobil развернула Discovery 6 на 4 032 NVIDIA Grace Hopper Superchip. Это **капитальные инвестиции $100–400 млн** на одну компанию. И они не «коммодизируются как облако гиперскейлеров» — это **стратегическая инфраструктура**, которая определяет конкурентное преимущество в разведке фронтиров на годы вперёд.

**Профиль AI в Q3.**

- **Физика — ground truth.** Eclipse, INTERSECT, CMG (компании Computer Modelling Group), OpenFOAM — классические пластовые симуляторы.
- **AI — ускоритель и инструмент предварительного отсеивания.** Foundation models, ML-суррогаты, deep learning поверх сейсмики.
- **Senior expertise — essential.** Senior geophysicist + classical interpretation в frontier basin = winning move. Без него любая «AI auto-interpretation» проигрывает.
- **Capital intensity HPC.** $100–400 млн на установку — нижний эшелон рынка.

Эта структура — **AI augmentation, не replacement** — повторяется в каждом case study в этом разделе.

### §2.2. HPC-гонка: Eni HPC6 и Aramco METABRAIN

[for-slide-s14]

В декабре 2024 года итальянская нефтегазовая компания Eni запустила суперкомпьютер HPC6 в дата-центре Ferrera Erbognone. **606 PFLOPS пиковой производительности, 477 PFLOPS sustained**; 14 000 графических ускорителей AMD Instinct MI250X; стоимость инсталляции — около **$104 млн** [17]. На декабрьском листинге Top500 (мировом рейтинге суперкомпьютеров) HPC6 занял **5-е место** из примерно 500 — это входит в верхний 1% мирового HPC. HPC6 в **9 раз мощнее** своего предшественника HPC5.

Применения HPC6:

- **Обработка сейсмики** (англ. **seismic processing** — обработка отражённых упругих волн для построения трёхмерной модели подповерхности).
- **Пластовая симуляция** на симуляторах класса INTERSECT — реальная business value на frontier exploration в Anchois (Marocco), Mozambique LNG, Egypt Zohr.
- **Моделирование CCS** — миграция облака CO₂ в подземных хранилищах на десятки и сотни лет (cross-link к Разделу 4 — Q4 energy transition).

**Параллельно — Aramco METABRAIN.** Saudi Aramco в 2024 году разработала и развернула METABRAIN — большую универсальную модель внутреннего использования. Объявленные параметры на 2024 год: **примерно 250 миллиардов параметров** [VFY-day-of] [18,19]. В начале 2024 года в публикациях фигурировала исходная версия 7 миллиардов параметров; к концу 2024 года — 250 миллиардов; в публикациях 2025 года появляются claim'ы 1 триллиона — точные цифры volatile, и студент должен относиться к ним осторожно [VFY-day-of]. Что неизменно:

- Обучение на **7 триллионах токенов**, представляющих **90 лет** operational data Aramco (компания основана в 1933 году как Saudi Standard Oil).
- **6 000 сотрудников обучены** работать с AI-инструментарием на основе METABRAIN.
- **430 use cases** идентифицированы и/или развёрнуты.

**Что Aramco публикует как value.** В Davos в январе 2025 года CEO Aramco Amin H. Nasser заявил, что **AI-инвестиции Aramco принесли $1,8 млрд реализованной стоимости в 2024 году** [20]; кумулятивно за 2023–2024 — $6 млрд; ожидаемая стоимость в 2025 — $3–5 млрд. Каналы создания value: прогностическое обслуживание, оптимизированное бурение, smarter scheduling, улучшенное **управление пластом** (англ. **reservoir management** — управление режимом разработки месторождения для максимизации извлечения).

**Базовая контекстуализация $1,8 млрд.**

- **Aramco выручка 2024 = $436,6 млрд** (полные годовые результаты, опубликованы март 2025; $440 млрд было приближённой оценкой по 2023 году). $1,8B / $436,6B = **0,41% выручки.** AI не «спасает» компанию — добавляет полпроцента к полностью оптимизированной операции.
- **R&D бюджет Aramco ≈ $3,5 млрд/год.** $1,8B realized vs $3,5B R&D = **51% R&D budget** реализованной стоимости (если methodology признать без вопросов). Это **подозрительно высокий** уровень — обычно ROI на R&D не возвращается в один год.
- **Aramco GAIA fund — $1 млрд** на инвестиции в AI-стартапы, часть Aramco $7,5 млрд глобальной venture программы (расширена в январе 2024).
- **Параллельная Aramco $1,5 млрд инвестиция в Groq** (для cloud compute) vs Microsoft $1,5B в G42 (апрель 2024) — параллельные UAE-Saudi AI hub plays.

**Что делать студенту с этими цифрами.** Главный урок:

1. **$1,8B — self-reported, не аудированное число.** Aramco — государственная компания, публикующая консолидированную отчётность, но конкретная разбивка AI value стоимости — корпоративная коммуникация, не аудиторское заключение.
2. **0,4% выручки — это правильный исходный уровень для сравнения.** Если читать «$1,8 млрд» без знаменателя, кажется огромным. С знаменателем — это инкрементальная оптимизация на масштабе огромной компании.
3. **METABRAIN — внутренний продукт.** Aramco **не продаёт METABRAIN** наружу; это конкурентное преимущество, держится внутри. Это типично для NOC-foundation models (Aramco, Газпром нефть Cognitive Geo): они **не конкурируют с SLB Lumi или OpenAI GPT** на открытом рынке.
4. **HPC-гонка не «коммодизируется».** $104 млн на Eni HPC6, оценочно $200–400 млн на ExxonMobil Discovery 6 — это **CapEx на стратегическую инфраструктуру**, не операционные расходы. Только крупные NOC и super-majors могут позволить эту гонку. Малые независимые операторы вытесняются из frontier exploration через capital barrier, не через technology barrier.

**Anti-hype замечание.** Когда вендор продаёт «AI revolution в exploration» — стоит спросить: **какой HPC-кластер** обучает модель? Если ответ — «облачный hyperscaler» — это означает, что обучение **ограничено бюджетом** (cloud GPU аренда $2–4/час за A100; 1 эпоха foundation model на 90 годах данных — это десятки миллионов долларов GPU-времени). Если ответ — «свой HPC» — спросить: чей? Размер? Зачем именно столько? Многие «AI revolution» pitches окажутся pitch'ами поверх 8 GPU H100, что в реальности — не foundation model, а дообученная LLM (large language model — большая языковая модель) среднего размера. Это не плохо. Но это и не «революция».

**GAIA fund Aramco — стратегия вне HPC.** Параллельно с METABRAIN Aramco запустила **GAIA fund** — $1 миллиард на инвестиции в AI-стартапы, часть Aramco $7,5 миллиардов global venture программы (расширена в январе 2024 года). Это означает: Aramco **не пытается заменить весь AI-стек собственными разработками**. METABRAIN — flagship внутренний foundation model для core E&P задач; GAIA — диверсифицированный portfolio AI-стартапов (от drug discovery до autonomous vehicles), часть которых имеет potential cross-application в нефтегазе. Это **двухуровневая AI-стратегия**: ядро внутри + experimentation наружу через VC. Похожий паттерн — у ExxonMobil (Microsoft Azure анкор-партнёрство + множество стартап-инвестиций), у Equinor (AWS + независимые ML-стартапы). Это **state-of-the-art organizational pattern** для крупного NOC / IOC в 2024–2026 годах.

**Геополитический контекст HPC.** Параллельная **Aramco $1,5 млрд инвестиция в Groq** (для cloud compute, апрель 2024 года) vs Microsoft $1,5B в G42 (тоже апрель 2024 года) — это **параллельные UAE-Saudi AI hub plays**. Middle East становится **третьим major AI compute hub** после US и China, и это **прямой структурный driver** для нефтегаз AI, поскольку именно NOC региона имеют capital для финансирования HPC инсталляций такого уровня. К 2026 году видно, что **географическая концентрация frontier-exploration AI** смещается с US-Europe оси к US-Middle East-Russia-China распределённой структуре, и регуляторика США (CHIPS Act, export controls на high-end NVIDIA chips) **усиливает** это смещение, а не замедляет его.

### §2.3. SLB Lumi — отраслевые foundation models поверх Petrel и Delfi

[for-slide-s15]

В сентябре 2024 года SLB (бывшая Schlumberger, переименована в 2022 году) запустила **Lumi** — отраслевую foundation model поверх своей облачной платформы **Delfi** (Delfi — E&P-платформа, оперирующая на AWS / Azure / GCP с 2018+). Lumi обучена на NVIDIA Grace Hopper Superchip; **anchor customers** — Aker BP, Shell, Azule Energy (BP + Eni Angolan joint venture) [21].

**Что Lumi делает.** Foundation model для специфических задач разведки:

- **Petrophysics interpretation** — интерпретация каротажа (well logs); ML заменяет первичную обработку, **senior petrophysicist** делает финальную QC.
- **Seismic auto-tracking** — автоматическая трассировка горизонтов в 3D-сейсмике; ускоряет работу геофизика; не заменяет его в frontier basin.
- **Drilling automation queries** — natural language interface к историческим данным бурения.

**Customers (известные на момент написания):**

- **Shell Offshore Inc.** — Wellbore Insights на Delfi в Gulf of Mexico, cloud-based wellbore dynamics modelling.
- **Aker BP** (Norway) — co-develop digital platform для subsurface workflows. Цель — «reducing costs and shortening planning cycles», конкретные delta не публично раскрыты [VFY-day-of].
- **Azule Energy** (BP + Eni Angola JV) — Delfi для всей E&P операции.

**Финансовая контекстуализация.** SLB digital revenue в 2024 году **превысил $2 млрд** на полный год [22]. Это ~5,7% от total SLB revenue ~$35 млрд. Direction в quarterly earnings calls: «дальнейшее adoption Delfi technology и customers embracing connected and autonomous drilling». Lumi — следующий этап монетизации после Delfi.

**Anti-hype: mode ≠ brand.** Когда инженер слышит «отраслевая foundation model для нефтегаза», он должен помнить: **это режим применения AI**, а не уникальный продукт SLB. Тот же режим реализуют:

- **Aramco METABRAIN** — внутренний продукт, не продаётся.
- **OpenAI / Anthropic** — общие foundation models, fine-tuned под нефтегаз через LoRA или системный промпт.
- **Microsoft Azure ML + Google Cloud Vertex AI** — стек гиперскейлера с доменной донастройкой.
- **Internal models** Газпром нефти (Cognitive Geo), CNPC, Petrobras (если развёрнуты).

Выбор между Lumi и альтернативой — это выбор не «между AI и не-AI», а между **вертикально-интегрированным стеком (SLB Lumi + Petrel + Delfi)** и **дезагрегированным стеком (собственные данные + собственная платформа + LLM от гиперскейлера)**. Для крупного NOC второй вариант часто предпочтительнее (контроль данных, независимость от вендора). Для среднего IOC или сервисного подрядчика — первый.

**Halliburton DecisionSpace и Baker Hughes** — конкуренты SLB в этой нише. Halliburton фокусируется на классической интерпретации сейсмики с ML augmentation; Baker Hughes (после реструктуризации BHC3 JV с C3.ai к 2023 году) сосредотачивается на оборудовании + selective AI применениях.

### §2.4. ExxonMobil Discovery 6: 4D-сейсмика от месяцев к неделям

[for-slide-s16]

В первой половине 2025 года ExxonMobil развернула **Discovery 6** — суперкомпьютер на базе HPE Cray EX4000 с **4 032 NVIDIA Grace Hopper Superchip** [23]. Это **4-кратное** увеличение compute мощности относительно Discovery 5. Капитальные затраты публично не раскрыты, но по аналогии с Eni HPC6 ($104 млн на меньшую систему) оценочно — **$200–400 млн** [VFY-day-of].

**Что Discovery 6 делает.**

- **4D-сейсмика** (англ. **4D seismic** — 3D-сейсмика, повторяемая во времени; четвёртое измерение — время; используется для мониторинга движения флюида в пласте в процессе разработки) — обработка моделей подземных коллекторов **сжимается с месяцев до недель**. Это критично для **активного управления пластом** на действующих месторождениях, где изменения видны в реальном времени.
- **Stabroek Block в Гайане.** ExxonMobil — оператор Stabroek, одного из крупнейших offshore нефтяных открытий 21 века. **Stabroek estimate: 9–11 миллиардов BOE** (barrels of oil equivalent — единица измерения, включающая нефть и газ в эквиваленте баррелей нефти; оценки ExxonMobil 2023–2024 годов; диапазон отражает recoverable resources на разных уровнях геологической уверенности — не «proven», а «discovered recoverable». Для контраста: Permian Basin estimate ExxonMobil-Pioneer 2024 — **16 миллиардов BOE recoverable** в onshore unconventional ресурсе). **Discovery 6 unlock $1+ млрд value** на первых **6 FPSO** в Stabroek; FPSO (Floating Production Storage and Offloading — плавучая платформа добычи-хранения-выгрузки нефти) — типичная единица offshore production capacity.
- Базовая контекстуализация $1B+: первые 6 FPSO составляют примерно **30–40% от планируемой capacity** Stabroek. То есть Discovery 6 покрывает значительную, но не всю value chain.

**Сравнение HPC-гонки в Q3:**

| Параметр | Eni HPC6 | ExxonMobil Discovery 6 | Aramco METABRAIN |
|---|---|---|---|
| Дата запуска | Декабрь 2024 | H1 2025 | Поэтапно 2024–2025 |
| Compute | 14 000 AMD MI250X | 4 032 NVIDIA Grace Hopper | Внутренний HPC + параметры модели 250 млрд (volatile) |
| Capex | $104 млн | $200–400 млн (оценка) | Не раскрыт |
| Top500 | #5 (Дек 2024) | Не входит публично | Не применимо (модель, не HPC рейтинг) |
| Использование | Sеismic + simulation + CCS | 4D-сейсмика + Guyana | Foundation model + 430 use cases |

**Что эта таблица показывает.** Q3 — это **разные стратегии HPC** у каждой крупной компании. Eni выбрал AMD (cost-effective on per-FLOP basis); ExxonMobil выбрал NVIDIA Grace Hopper (доминирующий в ML workloads); Aramco — комбинация HPC + foundation model. Все три — **проприетарные** (closed, не shared). Это означает, что **рынок HPC для нефтегаза не «коммодизируется»**, как hyperscaler cloud — каждый major имеет свой стек, и **малый оператор не может его повторить**.

**Stabroek Block как иллюстрация.** Гайана до 2015 года не была нефтедобывающей страной. С 2015 года ExxonMobil открыл серию крупных месторождений в shallow-to-deepwater Stabroek; к 2024 году Гайана стала одной из быстрорастущих нефтедобывающих стран мира. **AI здесь — критическая часть operational efficiency**, потому что:

1. Каждое FPSO стоит $1–2 млрд. Любая ошибка в расположении или планировании скважины — миллионы долларов лишних расходов.
2. Reservoir behavior в Stabroek **исторически не наблюдался** — это новый бассейн, без long-history production data. AI на 4D-сейсмике помогает **компенсировать sparse data** через быстрый цикл обратной связи: пробурили — увидели реакцию пласта — обновили модель.
3. **Frontier basin profile**: в Stabroek **физика частично известна** (subsurface геология похожа на pre-salt Brazil), **данных мало** (~30 wells на момент 2024). Это **смешанный Q1–Q3 квадрант** — на keystone-матрице ближе к границе.

**Anti-hype в HPC-гонке.** Цифры compute мощности (PFLOPS, количество GPU) **впечатляют, но не равны business value**. ExxonMobil **не публикует** сравнительные результаты «Discovery 5 vs Discovery 6 на одной и той же задаче с тем же бизнес-метрикой». Заявление «4×» означает только **4× compute throughput**, не **4× business value**. Студент должен уметь читать эту разницу: vendor / corporate communication говорит про cycles, business говорит про dollars / barrels / time-to-first-oil.

### §2.5. Провал 1: BP + Beyond Limits (2018–2023, $20 млн, vendor pivot)

[for-slide-s17]

В **июне 2017 года** BP Ventures возглавила раунд **Series B на $20 млн** в Beyond Limits — стартапе из Глендейла (Калифорния), выделившемся из NASA Jet Propulsion Laboratory с claim'ом, что технология **«cognitive AI»** для исследовательских миссий deep space теперь применима в нефтегазе. Активный operational rollout партнёрства — 2018–2022 годы; vendor pivot Beyond Limits с oil&gas в general industrial AI / healthcare / manufacturing — 2022–2023; полная wind-down O&G focus — 2023.

**Что обещали (2018).**

- AI «absorb learnings of geologists and petroleum engineers and imitate their decision-making».
- Технология из deep space exploration (NASA JPL roots) для offshore разведки.
- «Ускорять операционные инсайты и автоматизацию процессов в операциях» (Accelerate operational insight and process automation across operations).
- BP получает приоритетный доступ + influence над продуктовой дорожной картой.

**Что вышло (2018–2025).**

- **Публичных результатов roll-out нет** за 7 лет.
- Beyond Limits **сменил отраслевой focus** с oil&gas на general industrial AI, потом в healthcare и manufacturing в 2023 году.
- BP **не обновил кейс** на своём сайте после 2019 года [VFY-day-of].
- 2020 oil crash + BP «Beyond Petroleum» rebrand → digital teams реструктурированы (см. §5.4 в Части 4).
- К 2024 году ни BP, ни Beyond Limits не отвечают на запросы о статусе партнёрства.

**Выученный урок (три фундаментальных).**

**Первый — «cognitive AI» (символьный + ML гибрид) обещанная generalizable autonomy не материализовалась.** Это был **ML-marketing эпохи 2018 года** — компании присваивали маркетинговое название «cognitive» обычному ML, чтобы дифференцировать себя в момент, когда «ML» уже звучал слишком обще. Реальная архитектура Beyond Limits — комбинация classical rule-based reasoning + ML — не имела фундаментального преимущества над чистым ML. К 2023 году рынок понял это, и Beyond Limits ушёл искать новые ниши.

**Второй — концентрированная ставка на одного клиента.** BP была **якорным инвестором и якорным клиентом**. Это значит: продуктовая дорожная карта Beyond Limits **первоначально оптимизировалась под BP**. Когда BP сократил инвестиции (нефтяной кризис 2020) — у Beyond Limits не оказалось диверсифицированной клиентской базы. **Смена направления вендором оставила BP без коммерческого продукта**, а Beyond Limits — без якорной выручки. Структурная двойная потеря.

**Третий — «имитировать decision-making геологов» = anthropomorphic overpromise.** Реальные геологи делают decision на основе **implicit knowledge**, которое тяжело кодифицировать: pattern recognition после 20 лет работы с одной геологической провинцией, интуиция по аналогам в memory, judgment calls по incomplete data. AI 2018 года не мог имитировать эту работу не потому, что нужны больше параметров — а потому, что **сама задача неправильно поставлена**. Имитация decision-making — это попытка моделировать черный ящик опытного человека; правильная задача — **augmentation**: ускорять рутинные задачи геолога, оставляя ему judgment calls.

**Параллель с Aramco METABRAIN.** METABRAIN, начатая в 2024 году, **не повторяет ошибку Beyond Limits** в одном ключевом аспекте: METABRAIN — **внутренний продукт Aramco**, не продаётся внешне. Aramco не нужно искать новых клиентов; не нужно масштабировать продукт на множество операторов. METABRAIN оптимизируется под **внутренние рабочие процессы Aramco** и не сталкивается с проблемой обобщения. Это структурный аргумент в пользу **инсорсинга AI** (разработки внутри компании) для крупных NOC, против покупки нишевых AI-вендоров. Российский Cognitive Geo (Газпром нефть) — тот же паттерн.

**Что должен сделать студент с BP+Beyond Limits**: не «никогда не покупать AI у вендора», а **читать риск концентрации**. Если вендор имеет 1 якорного клиента = 80% выручки — это красный флаг. Если вендор меняет направление каждые 2 года — красный флаг. Если обещание = «заменить геолога» — красный флаг. Шаг за пределы красных флагов → due diligence.

**Дополнительный угол анализа — почему именно 2017–2018 годы.** BP Series B инвестиция в Beyond Limits — июнь 2017; формальный rollout O&G партнёрства — 2018. Это самый пик ML-маркетинговой эйфории. ImageNet results 2012, AlphaGo 2016, GPT-1 в 2018 (хотя для большинства публики ChatGPT появился в 2022 году). В этом окне **каждая нефтегазовая компания** делала AI-партнёрство для пресс-релиза. Beyond Limits сильно отличался тем, что у него была JPL-родословная (что давало credibility в индустрии, ценящей deep-space heritage); этого было достаточно для BP $20M Series B инвестиции **без жёсткой технической due diligence**. К 2025 году такие инвестиции не происходят в той же manner — индустрия научилась требовать **technical pilot with measurable outcomes** перед инвестицией. Это **positive evolution**, но cost обучения был $20M+ в одном кейсе, и аналогичные cases у других компаний в той же эпохе (Shell+C3.ai, Chevron+Microsoft AI partnerships) принесли similar lessons.

**Стиль failure: тихое сворачивание.** Beyond Limits не «провалился громко» — нет банкротства, нет публичного wind-down. Компания просто **сместила фокус** в healthcare и manufacturing, и BP перестал обновлять кейсы. Это типичный паттерн **soft failure** в индустриальном AI: партнёры не объявляют о провале (это плохо для PR обоих сторон), они просто перестают говорить о партнёрстве. Студент, ищущий evidence для due diligence, должен искать **отсутствие обновлений** как red flag, не только публичные failure announcements. Если на сайте вендора последнее упоминание клиента — 4+ года назад, и нет квартального обновления — это **structural signal**, что партнёрство либо tail-end либо завершено.

### §2.6. Провал 2: IBM Watson + Repsol Kalimba (2014–2022, тихое сворачивание)

[for-slide-s18]

В 2014 году IBM и испанская Repsol объявили партнёрство «Kalimba project» с целью применить **IBM Watson cognitive computing** к 30 годам exploration data Repsol. Проект запустили в IBM Cognitive Environments Laboratory (Нью-Йорк) и Repsol Technology Centre (Мадрид). Объявлены результаты — «в первой половине 2016 года».

**Что обещали (2014).**

- 30 лет exploration data **«analyzed» Watson cognitive**.
- Запуск результатов в 1H 2016.
- Cognitive computing «понимает контекст», «синтезирует insights», «обогащает intuition».

**Что вышло (2016–2022).**

- **Конкретных результатов и метрик публично не объявлено.** В партнёрских пресс-релизах 2016–2018 — generic statements без чисел.
- **IBM Watson Industry Solutions — broad stagnation 2018–2022.** Watson Health unwound в 2022 году (продан Francisco Partners); Watson Financial Services не достиг scale; Watson Industrial — аналогично. К 2022 году IBM перестроил весь Watson portfolio, и «cognitive computing» как маркетинговый зонтик исчез из IBM messaging.
- **Repsol перешёл на собственные ML tools** — платформа **Repsol Lumen** (2020+) без IBM.
- **Партнёрство тихо завершилось** — без официального объявления о завершении, без post-mortem.

**Выученный урок (три фундаментальных).**

**Первый — general-purpose «cognitive computing» platforms (Watson era) не scaled в narrow domain как O&G exploration.** Watson в 2014 году был оптимизирован под general-purpose Q&A (Jeopardy-style) и medical literature analysis. Применение тех же архитектур в нефтегазовой разведке требовало **specialized training data, specialized model architectures, specialized integration** — то, что Watson 2014 года не давал out-of-the-box. IBM не инвестировал в **vertical specialization** на достаточно глубокую инженерию, потому что Watson был **horizontal platform**, и vertical specialization была product line, не R&D priority.

**Второй — «30 лет данных проанализировано» звучит впечатляюще, но без конкретной бизнес-метрики выводы не операционализируемы.** Repsol получил от Watson **инсайты в формате «вот интересные паттерны в ваших данных»**, без привязки к конкретным экономическим решениям («стоит ли бурить вот эту локацию?», «надо ли поднять давление в этой колонне?»). Инсайты без операционализуемости = застревание пилотных проектов (pilot purgatory).

**Третий — Hype cycle 2014–2016 (Watson «выиграл Jeopardy» 2011) → реальное commercial use в 2018+ ≤ 10% от ожиданий.** Это типичный паттерн **hype-to-disappointment** Gartner. Watson 2011 — peak inflated expectations; 2016–2018 — disillusionment; 2022 — Watson Health продан. Параллельный паттерн сейчас разворачивается с **LLM agents в 2024–2025** — это сюжет Раздела 4 §4.5.

**Параллель Aramco METABRAIN vs IBM Watson 2014.** METABRAIN существенно мощнее (250B параметров vs ~100M-1B у Watson 2014 архитектур) и обучен на специализированных нефтегазовых данных (90 лет Aramco). Но **сам паттерн внедрения** — «foundation model для геологов» — может повторить ту же ловушку. Различие — Aramco **сама** разрабатывает и **сама** интегрирует с внутренними рабочими процессами; у Watson + Repsol была **двухсторонняя** интеграция с расходящимися интересами (IBM хотел продать платформу; Repsol хотел бизнес-результаты — разные продуктовые требования).

**Что значит для студента 2026 года.** В 2024–2026 годах та же ловушка может повториться с **LLM-based agents** для нефтегазовых operations. Когда крупный консалтинговый поставщик или software vendor приходит с pitch'ем «foundation model для нефтегаза» — спросить:

1. **Specialized training data** есть? Сколько лет, сколько токенов, какая discipline?
2. **Specialized model architecture** или generic LLM с fine-tuning?
3. **Integration story** — кто интегрирует с существующими SCADA / MES / ERP? Какая стоимость?
4. **Business outcomes** в pilot — specific dollar figures или generic «insights»?
5. **Anchor customer concentration** — кто платит, кто использует, кто получает value? Если разные — risk pattern.

**Параллельный сюжет — IBM Watson Health.** Watson Health (2015) объявлялся как **революция в онкологии**: AI читает медицинскую литературу + клинические протоколы + истории пациентов и рекомендует курсы лечения. После $5+ миллиардов инвестиций и серии партнёрств (MD Anderson Cancer Center, Memorial Sloan Kettering) Watson Health был **продан Francisco Partners в январе 2022 года**. Внутренние оценки IBM Watson Health value на момент продажи — $1+ миллиард, что **на порядок меньше** изначальных ожиданий. Этот параллель **критичен** для нефтегаза: тот же IBM, та же эпоха, та же «cognitive computing» маркетинговая упаковка, та же неспособность scale в narrow domain. Watson + Repsol (нефтегаз) и Watson Health (медицина) — это **два manifestations одной структурной ошибки** IBM в подходе к vertical AI.

**Что отличает 2024–2026 эпоху от 2014–2017.** Современные foundation models (GPT-4, Claude 3, METABRAIN) построены на **существенно более крупных архитектурах** (100M–1B параметров у Watson 2014 vs 10B–250B+ у современных). И обучены на **существенно больших корпусах**. Это **технически** даёт больше capability. Но **paradigmatic ошибки 2014–2017** могут повториться:

- **Generic platform** vs **specialized application**. Любой generic LLM, fine-tuned для нефтегаза, без специализированной архитектуры и без специализированного training corpus — не обыграет специализированный internal model (Aramco METABRAIN).
- **«Инсайты без операционализуемости»**. AI генерирует интересные паттерны, оператор не знает, что с ними делать. Без **явной интеграции с бизнес-процессом** — застревание пилотов.
- **Two-party integration mismatch**. Vendor хочет продать платформу; operator хочет business outcomes. Без **shared incentive structure** (например, vendor compensation tied to operator outcomes) — структурный mismatch.

### §2.7. Альтернатива: Eclipse / INTERSECT / CMG / OpenFOAM — physics simulators

[for-slide-s19]

Это **ключевой раздел LO3** для Q3. Когда AI в frontier exploration буксует — что используют операторы вместо? Ответ: **physics-based simulators**, разработанные за десятилетия и хорошо валидированные.

**Eclipse.** Industry-standard reservoir simulator от SLB. Используется с 1980-х годов; сегодня — **flagship** для большинства мейджоров. Решает coupled fluid + heat + chemistry equations на 3D-сетке пласта. Параметризируется через черные ящики (свойства породы, fluid PVT, kinetics). Скорость — десятки часов до дней на крупной модели; точность — well-characterized.

**INTERSECT.** Next-generation Eclipse от SLB; высокое разрешение, лучше параллелизация. Используется на новейших месторождениях, где требуется высокое разрешение модели.

**CMG (Computer Modelling Group, Калгари).** Конкурент SLB. Три продукта:
- **IMEX** — black-oil reservoir simulator;
- **STARS** — thermal & advanced processes (например, тепловой EOR — enhanced oil recovery);
- **GEM** — compositional simulator (для газоконденсатных систем).
Niche, но stable. Используется в специфических задачах thermal EOR (steam injection в тяжёлой нефти) и compositional модели.

**OpenFOAM.** Open-source CFD (computational fluid dynamics) пакет. Не reservoir simulator per se, но используется для CFD-моделирования в **CCS** (моделирование миграции CO₂ облака), в **multi-phase flow** в производственных коллекторах, в gas plume modelling.

**Когда использовать physics-based simulator вместо ML.**

1. **Mature reservoir + regulatory submission.** Регулятор требует **physics-traceable submission** — Eclipse / INTERSECT даёт это; ML-суррогат не даёт.
2. **Complex EOR scenarios.** Тепловой EOR, газонагнетание, химическое EOR — все три требуют compositional / thermal модели. CMG STARS / GEM — стандарт.
3. **Hydraulic fracturing modelling.** Geomechanics + fluid flow. Eclipse / INTERSECT покрывают; ML только в специфических узких применениях.
4. **CCS plume migration long-horizon.** Eclipse + OpenFOAM (для CFD around injectors) — стандарт. ML на 100-летнем horizon галлюцинирует (см. §4.5 в Части 3 о Q4 hallucination risk).
5. **Frontier basin без analog.** ML не на чем обучать; **physics-based + senior geophysicist + analog-basin reasoning** — единственный workable путь.

**Когда AI augmentation работает поверх physics simulators.**

1. **Screening huge параметров пространства.** Eclipse один прогон занимает дни; ML-суррогат — секунды. Сначала ML screen'ит 10 000 сценариев, затем 10 best — повторно прогоняют в Eclipse для валидации. Это **рабочий гибрид**, используется широко.
2. **Auto-tuning параметров калибровки.** Eclipse параметризуется через нескольких сотен параметров. ML может ускорить процесс **history matching** (подгонки модели к историческим данным добычи) в 50–80 раз.
3. **Quick-look interpretation сейсмики** (foundation models поверх Petrel) — затем senior geophysicist QC.

**PINN — попытка построить мост.** Physics-informed neural networks — класс нейронных сетей, которые **встраивают физические уравнения** в loss function. Идея: получить **speed of ML + consistency of physics**. PINN активно изучается academia с 2019 года, но **scale to industrial reservoir пока research-grade**. К 2026 году PINN — не mainstream commercial product. Это потенциальный мост в будущее, но **не сейчас**.

**Ключевой вывод для LO3.** Разведка фронтиров — это **канонический пример квадранта**, где **альтернативный инструмент (Eclipse / INTERSECT / CMG / OpenFOAM)** часто **лучше** AI-инструмента на основной задаче (регуляторная отчётность, моделирование EOR, долгосрочный CCS). AI добавляется **рядом**, не **вместо**. Студент, который пишет «AI заменит пластового симулятора через 5 лет» — упускает структурную картину. Через 5 лет (2030) Eclipse будет **по-прежнему стандартом**, а AI — полезно ускорять отдельные циклы и предварительное отсеивание.

**История симуляторов как лекция в pacing.** Eclipse был выпущен в 1983 году компанией ECL (Exploration Consultants Limited, затем приобретена Schlumberger). За 40+ лет существования он прошёл через несколько эпох улучшений: black-oil → compositional (1990s), parallel computing support (2000s), GPU-acceleration (2010s), AI-augmented (2020s). На каждом этапе **новая технологическая волна** обещала «заменить Eclipse», и каждый раз — Eclipse абсорбировал новую технологию как **add-on**, не **replacement**. Это **structural pattern индустриальной software**: well-validated incumbent tool не заменяется одним новым подходом; он эволюционирует, абсорбируя полезное. ML / foundation models — следующий этап эволюции, не disruption.

**Старший инженер + классическая интерпретация — экономическая реальность.** Старший геолог с 25+ годами опыта работы с одной геологической провинцией стоит компании $200–500k/год. Foundation model с обучением + интеграцией + поддержкой — $5–20 миллионов/год капзатрат + операционные. Арифметика простая: **5–25 старших геологов** за стоимость одной инсталляции foundation model. Foundation model окупается **только** если она **воспроизводит работу**, эквивалентную 5–25 геологам — что в моменте 2026 года **не доказано** ни одним публичным бенчмарком. Это **экономическая реальность** Q3: AI-augmentation **дополняет**, не **замещает** старшую экспертизу — потому что старшая экспертиза структурно дешевле развёртывания foundation model в пересчёте на одно решение.

**Halliburton — перспектива действующего лидера.** Halliburton, исторически второй крупнейший сервисный подрядчик после SLB, использует AI преимущественно как **augmentation поверх классических рабочих процессов**: ML-assisted сейсмическая интерпретация (где геофизик-человек делает финальный QC), автоматизированный анализ каротажа (но старший петрофизик делает интерпретацию), автоматизация бурения на основе извлечённых паттернов от успешных скважин. Halliburton **намеренно избегает** «foundation model»-маркетинга — отчасти из-за того, что гонку foundation models ведут SLB Lumi и крупные NOC, и у Halliburton **нет капитала для конкуренции** с этим. Это **стратегическое позиционирование**: «человек + классический рабочий процесс + ML-augmentation» vs «foundation model + автоинтерпретация». На горизонте 5 лет — оба подхода могут сосуществовать, и индустрия примет тот, который даст лучшую отдачу на затраты, не тот, который более «модный».

### §2.8. Фундаментальные ограничения Q3: sparse data + multi-physics surrogate gap

[for-slide-s19]

Эти два ограничения — **структурные**, не «полировочные». Их нельзя решить улучшением алгоритма; их можно только обойти через смену задачи или альтернативный инструмент.

**Ограничение 1 — Sparse data в frontier exploration.**

- Каждая wildcat скважина в офшорном глубоководном бурении — $50–100 млн.
- Размер выборки на новый бассейн = 1–5 wells.
- ML моделям нужны ≥1000 примеров для надёжной generalization; foundation models — миллионы–миллиарды токенов.
- **Transfer learning от established basins не generalizes**: бассейн Tarim не похож на Пермский (radically different mineralogy, pore physics, capillary structure).

**Последствие:** AI augments, но **не replaces** classical interpretation в frontier exploration. Foundation models, trained на Пермском бассейне, **fail on East African Rift** или pre-salt Brazil раннее. Это не «модель плохая» — это **fundamental data scarcity**.

**Ограничение 2 — Multi-physics simulation surrogate gap.**

- Пластовая симуляция — это **сцепленные** уравнения: fluid flow + heat + chemistry + geomechanics.
- ML-суррогат, обученный на выходах Eclipse/INTERSECT/CMG, ускоряет calendar time расчётов на 50–80%, но...
- **Loses physical consistency на extrapolation:** новые сценарии закачки, новое размещение скважины, новые fluid properties → нефизические результаты (отрицательные давления, нарушения массового баланса, температуры за пределами phase envelope).

**Последствие:** ML-суррогаты — **инструменты предварительного отсеивания**, не замена классических симуляторов. Операторы **сохраняют классические симуляторы** как эталонную разметку для регуляторной отчётности и для дизайн-решений; ML используется для **ускорения** циклов сценарного анализа.

**Ограничение 3 (ранее в §2.5–2.6) — Anthropomorphic overpromise.**

Когда вендор говорит «AI imitates decision-making геолога» — это категориально неверная задача. Решение геолога базируется на implicit knowledge, накопленном за 20+ лет, которое **не кодифицируется в training set**. AI может ускорять рутинные задачи геолога (сейсмическая трассировка, log interpretation) — но не replicate его judgment calls. BP+Beyond Limits и IBM+Repsol — два manifestation этой ловушки.

**Ограничение 4 — HPC capital barrier.**

$100–400 млн на одну HPC-инсталляцию для frontier exploration AI — это **strategic CapEx**, доступный только крупным NOC и super-majors. Малые независимые операторы вытесняются из frontier exploration через capital barrier, не через technology barrier. Это **структурный сдвиг рынка**: разведка консолидируется у нескольких очень крупных игроков, остальные специализируются на mature / Q1 операциях.

**Ограничение 5 — Long planning horizons vs short-term ML model decay.**

Это **сквозное ограничение** для Q1 + Q3, особо острое в Q3. Срок жизни месторождения 20–30 лет; срок «деградации» (data drift — постепенное расхождение между data, на которой обучена модель, и data, на которой она applied к live operations) обычной ML-модели — 1–2 года. Это значит:

- **Maintenance overhead** — continuous retraining нужен. Это **не "запустил модель один раз"**; это **continuous data engineering operation** на 20+ лет.
- **TCO (total cost of ownership) часто > savings.** Если retraining требует $200k-$500k engineering team per year, а savings $1M-$2M — net positive есть, но gap уже скромный; если savings $300-500k — net negative.
- **Knowledge transfer риск.** Engineers, которые tuned модель в 2024 году — могут покинуть компанию в 2027. Документация retraining processes — frequently overlooked в pilots.

Это **fundamental gap** между ML model lifecycle (1–2 года) и industrial operations lifecycle (20–30 лет). Workarounds — **simpler models** (с меньшей tendency к drift), **explicit drift monitoring**, **federated retraining** across operators (с privacy preservation), **annual model audits** как часть compliance routine. Но фундаментально — это **structural mismatch**, который не закрывается «улучшением алгоритма».

**Ограничение 6 — LLM hallucination в high-stakes ops.**

С 2023–2024 годов LLM-based agents стали активно продвигаться вендорами для нефтегазовых operations. Aramco METABRAIN использует LLM interface для query natural-language across 90-летних архивов; SLB Lumi включает natural-language interface поверх Petrel; Cognite Data Fusion имеет LLM-assisted query layer. Все эти deployments — потенциально подвержены **hallucination**: модель **уверенно генерирует ответ**, который **structurally неверен** для конкретного контекста.

В high-stakes operations это критично:

- Operator спрашивает LLM «увеличение давления injection wells на 5% безопасно для caprock?» → LLM генерирует уверенный ответ, не основанный на actual geomechanics modelling.
- Geologist спрашивает LLM «по этим логам — продуктивная зона?» → LLM соглашается, не имея access к actual log interpretation.
- Operator принимает решение на основе LLM output, **без verification против physics-based model**.

**Прогноз Gartner на 2027: 40% агентских AI-проектов будут отменены** из-за превышения бюджетов и слабого контроля рисков. Для нефтегаза — это **прямое предупреждение**: развёртывание LLM-агентов в промышленной эксплуатации без сильной дисциплины human-in-the-loop = паттерн риска, который повторит ту же структурную ошибку модели Watson эпохи 2014.

### §2.9. Самопроверка по Q3

1. **Объясните парадокс HPC-гонки.** Почему major NOC (Aramco) и major IOC (ExxonMobil) **строят собственные HPC**, вместо того чтобы арендовать GPU у AWS / Azure? Назовите минимум 2 структурные причины.

2. **BP + Beyond Limits — три выученных урока.** Перечислите три фундаментальных урока из провала партнёрства; для каждого приведите конкретное предупреждение, которое инженер должен задать вендору в pitch-фазе.

3. **Frontier basin без analog data — что делать?** Возьмите гипотетический кейс: новый offshore basin в Восточной Африке, 2 пробуренные скважины с минимальными результатами, оператор хочет «применить AI для оптимизации следующего drilling location». Что вы рекомендуете? (Подсказка: смотрите §1.8 критерий 5 и §2.7 список инструментов.)

4. **Сравните Eni HPC6 и Aramco METABRAIN.** Eni HPC6 — суперкомпьютер; Aramco METABRAIN — foundation model. Какая разница в стратегии Q3? Чему служит каждый?

5. **PINN — research-grade или production-ready?** Объясните, что мешает physics-informed neural networks стать mainstream в industrial reservoir simulation в 2026 году. Назовите минимум 2 фундаментальных barrier.

6. **«AI заменит Eclipse через 5 лет» — обоснованное прогнозирование или wishful thinking?** Используйте историю эволюции Eclipse (1983–2024) как evidence base; обсудите structural pattern, в котором well-validated incumbent tool **абсорбирует** новые технологии, не **замещается** ими.

---

**[→ Часть 3 (Раздел 3 — Q2 метановая MRV + Раздел 4 — Q4 энергетический переход)](chapter-part3.md)**
