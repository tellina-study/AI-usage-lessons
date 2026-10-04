# Reader simulator (text-only, student perspective) — plan-v1 Лекция 16

**Дата:** 2026-05-27
**Reader profile:** студент 3 курса ИУ6 МГТУ Баумана, общий технический бэкграунд, без нефтегазовой специализации (знаю что такое скважина, переработка, СПГ на бытовом уровне; никогда не работал с reservoir simulators / OGI / methane MRV)
**Verdict:** **APPROVE-WITH-POLISH**

## TL;DR

Plan читается **интересно**, особенно блок про methane satellites (MethaneSAT loss + 4× discrepancy — это реально цепляет, я бы пересказывал друзьям) и failures по BP/IBM. Но **keystone 2×2 matrix я в первые 2 раза не понял** — «physics certainty» звучит как философия, а не инженерия; пришлось доходить из примеров Q3 vs Q2. Раздел про Россию воспринимается органично (sanctions context работает), а Раздел 4 (Q4 transition) — тяжеловесный и местами скучный. Главная слабость для меня — перегруз vendor-таблицами и слишком много англицизмов без расшифровки в первой половине.

## 1. Hook + keystone (первая страница)

**Hook (s01 Permian VIIRS):** «Это нефть и газ, которые мы экспортируем во вселенную бесплатно» — **понравилось**. Сразу понял: речь про утечки/факелы, видно с орбиты. Хороший заход, картинка spaceview = эпично.

**Keystone matrix (s05):** **не понял с первого прохода**. Конкретно:

- «**Доступность данных**» — OK, интуитивно. «Много скважин — много данных». Понятно.
- «**Определённость физики**» — **что это?** Я читаю plan и в Q2 говорится «physics certainty low потому что methane plume physics не закрыта». Но я не знаю, что такое «закрыта» в смысле физики. Это про «есть PDE с гарантированной точностью» или «есть модель, которая на 95% точна»? Plan сам в Risk 1 признаёт: «студент может не понять» и предлагает 500-700 слов в chapter — **этого мало для keystone**, который должен быть понятен СРАЗУ на слайде. Слайду нужен **inline gloss** в keystone bottom bar: «physics certainty = есть ли численная модель, дающая надёжный референс».

- **Q1 vs Q3 я понял быстро.** Mature field — много скважин, физика отработана. Frontier — мало скважин, физика «high» но мало точек данных.
- **Q2 (methane) — высокая data, низкая physics?** Pусь contraintuitive: я знаю что methane = небольшая молекула, диффузия физика классическая. Plan честно говорит «atmospheric physics частично закрыта». Это **важно сказать ОЧЕВИДНО на keystone**, иначе студент думает «physics low = плохо изучено» и матрица ломается.
- **Q4 — оба low.** Понял благодаря CCS 100-летнего horizon как пример. ОК.

**После прочтения Раздела 0** — однокурснику объясню так: «Это таблица 2×2 где AI работает по-разному в 4 разных режимах нефтегаза. Запомню после раздела 1 окончательно, но keystone в s05 нужно более наглядным».

**Хочется ли продолжить?** Да — но больше из любопытства к спутникам и провалам, чем к keystone'у.

## 2. Section flow

**Естественные переходы:**
- Раздел 0 → 1 (Q1) — логично, «начнём с самого понятного».
- Раздел 1 (Q1) → 2 (Q3) — **OK с usado**. Связка «спускаемся в data-беднейший квадрант» — естественна. Я понял почему: «давайте от ESP пойдём к разведке, потому что разведка сложнее».
- Раздел 2 (Q3) → 3 (Q2) — «возвращаемся в data-rich квадрант, но физика разрозненная» — **понятно, нравится зигзаг**. Surprising что methane не Q1 (data много), а Q2 — потому что фьюжн данных как ML problem.
- Раздел 3 → 4 (Q4) — natural «самый честный квадрант».
- Раздел 4 → 5 (Россия) — **transitions feels добавлено**. Я ждал что Россия будет интегрирована в каждый раздел (как в Лекции 13?), а тут — отдельная плитка. Plan говорит «все 4 квадранта в санкционном режиме» — это работает, но именно как **отдельная глобальная перспектива**, не «ещё один квадрант».

**Логика order Q1 → Q3 → Q2 → Q4 — justified?** Кажется да. Мне понравилось: «легко → ультра-сложно (HPC) → middle с твистом (Q2) → энд-режим». Альтернативный «Q1→Q2→Q3→Q4» был бы менее dramatic. **OK.**

**Раздел 5 (Россия + cross-cutting):** feels organic — sanctions = real angle. **НО:** Cybersecurity в этой же секции (s37) feels squeezed. Ransomware +935% + Colonial Pipeline — это **сам по себе мощный topic**, заслуживает либо отдельного слайда в Разделе 6 closing, либо own mini-section. В рамках «Россия» это смешано.

## 3. Engagement check (cases)

### Memorable (вспомню через сутки):

- **MethaneSAT loss 20 июня 2025** — 13 месяцев из 5+ лет. Это **drama**. Запомню: «потеряли спутник через 13 месяцев, EU regulator не может на 1 спутник опираться». Очень сильный case.
- **Permian Basin: 410 t/h, 50% выше EPA estimates** — конкретно, шокирует, есть story «гэп между industry и regulator».
- **BP + Beyond Limits $20M cognitive AI → vendor пивотировал в healthcare** — comedy + лесон. «Anthropomorphic overpromise» — звучит как термин я выучу.
- **Северная Лайтс CCS 1.5 Mt vs IEA 7.6 Gt = 0.02%, gap 190×** — числовая драма, цепляет.
- **86% pilot stuck (McKinsey)** — это **самый цитируемый stat у меня будет**. Простой, шокирующий, не требует контекста.
- **Газпром нефть Cognitive Geo: геология 3-4 месяца → minutes** — конкретно, понятно, contextуально из-за санкций.

### Forgettable (читал, кивал, забыл):

- **Eni HPC6: 14k AMD MI250X, 606 PFLOPS, Top500 #5, $104M.** Запомню «итальянский суперкомп», но цифры — overload. На фоне ExxonMobil Discovery 6 (4k Grace Hopper) я **путаюсь, кто что**.
- **SLB Lumi vs Petrel vs Delfi** — 3 продукта одного вендора. **Какой из них AI, какой не?** Запутался.
- **Honeywell UOP Connect — 310+ units, 100+ sites, plan 750+.** Хорошо, что есть baseline «total global refineries ~700», но всё равно — почему я должен запомнить именно UOP, а не Aspen или DeltaV? **Mode vs brand confusion** — plan сам флагует это.
- **OspreyData, SLB Avocet, Halliburton DecisionSpace** — упомянуты но без анкера, пройдут мимо.
- **Aspen Mtell 10 days production saved** — забуду «10 days». Caveat про alert fatigue лучше запоминается.

### Emotional hook:

- **MethaneSAT loss** — **тревога** + сочувствие («столько лет строили — и потеряли»).
- **Deepwater Horizon 2010 alarm bypass** (упоминается mentioned в plans bonus) — **mорdid любопытство**.
- **Permian Basin VIIRS night satellite** — **awe**. Хочу увидеть картинку.
- **Газпром Cognitive Geo** — **professional curiosity**, как российский tech ведёт себя под sanctions.
- **Северная Лайтс 190× gap** — **скептицизм** к energy transition narrative. Это полезный hook для критического мышления.

## 4. Failures bucket

**Видно ли ≥30%?** Когда читаешь plan **последовательно**, failures **очень видны** — особенно s11 (86% pilot), s17-s18 (BP/IBM), s22 (MethaneSAT), s24 (4× discrepancy), s30-s31 (CCS gap + refinery). Я бы сказал «лекция про failures — там примеров много». **Это хорошо, mission accomplished.**

**Most memorable failures (для меня):**
1. **MethaneSAT loss** — single-point-of-failure, lecture-defining moment.
2. **BP + Beyond Limits** — comedy + lesson «cognitive AI = marketing».
3. **86% pilot stuck** — universal stat, я буду цитировать.
4. **4× discrepancy (MethaneSAT vs EPA)** — structural gap, не «AI ошибся».

**Weak failures:**
- **Cognite IPO postpone, $94M ARR vs cancelled $2-3B valuation** — для меня (3-курсника) звучит как finance jargon. «Ну, postpone IPO бывает». Не выученный урок, а финансовая news. Plan сам говорит «inline в s11 + chapter», нет own slide — **это правильно** что не отдельный слайд.
- **C3.ai O&G vertical declining (5.9% FY24 → declining FY25)** — то же. Cijfers, jargon, нет mind-blowing moment. **Inline OK, не slide.**
- **Refinery AI stagnation (s31)** — abstract. «Multi-physics constraints, mass+energy+reaction+corrosion lose consistency». **Понятно для специалиста, не для меня.** Нужны конкретные before/after или конкретный failed pilot имя.

**Чувствую ли что лекция учит «говорить нет неподходящему ИИ»?** **Да, явно.** 6 критериев «здесь AI не нужен» (mature field + senior team / SIL3-SIL4 / OGMP Level 5 / frontier без analog / stripper wells / custody transfer) — это рамка which makes sense. Это **не «вот ещё одна industry где AI везде»** — это **где работает, где нет, и почему**. **Big plus.**

## 5. Termin / glossary needs

Англицизмы, **с которыми я столкнусь впервые** и буду гуглить:

- **«Downhole»** — внутрискважинный? Догадался по контексту, но gloss нужен в первом упоминании.
- **«Basin / play / wildcat»** — «1 wildcat = $50-100M». **Что такое wildcat?** Догадался: «wildcat well» = разведочная скважина в новом месте. Нужен gloss.
- **«Shut-in / curtailment»** — plan переводит, ОК.
- **«Stripper wells <10 bopd»** — «истощённые скважины, мало добычи». bopd = barrels of oil per day. Нужен gloss на оба термина.
- **«ESP (electric submersible pump)»** — ОК, plan расшифровывает.
- **«FPSO Stabroek Block Guyana»** — **FPSO** что такое? Plan расшифровывает в allowlist (плавучая платформа), но я не знаю, дойдёт ли расшифровка до слайда. **Подкладывать inline gloss обязательно.**
- **«BOP / PRV / ESD / SIS / SIL3 / SIL4»** — куча безопасностных аббревиатур. Plan acronym allowlist даёт gloss, **но в s11/s12 надо обеспечить inline gloss первого упоминания**.
- **«OGI / OGMP Level 4/5 / MRV / LDAR»** — methane regulation alphabet soup. **Самое тяжёлое.** В Разделе 3 за 5 минут летит 5 аббревиатур. Нужно либо schema «who is who» в начале Раздела 3, либо сильные glosses.
- **«PINN (physics-informed neural network)»** — упоминается «research-grade». Я хочу узнать, что это, но plan не раскрывает.
- **«SCADA + PID + APC»** — automation jargon. PID — слышал в курсе автоматики, APC — нет.
- **«Foundation model»** — слышал. Но «domain foundation model» SLB Lumi — это новое для меня. Plan flags это в Russification table — хорошо.
- **«4D seismic imaging»** — что это? 4-я ось — время? Plan не говорит. **Нужно gloss один раз.**
- **«Plume migration»** — догадался («распространение облака CO₂»). Gloss нужен.
- **«Custody transfer metering»** — финансовая метрология. Не знал.

**Recommendation:** в chapter Q2/Q3 deep-dive **первое упоминание каждой аббревиатуры — с inline glos one-line**. На слайдах в Разделе 3 — **dedicated «methane MRV alphabet» slide** или footer-glossary.

## 6. Numbers

### Memorable (запомню после первого чтения):

- **86% pilot stuck** — universal.
- **190× scale-up gap для CCS** — drama.
- **4× discrepancy MethaneSAT vs EPA** — concrete.
- **+15% production Ambyint на 200 скважин** — простое.
- **$50-100M per wildcat** — anchor для понимания «sparse data».
- **20-30 лет field life vs 1-2 года ML model decay** — **ключевая мысль**, цитата-кандидат.
- **107 000 jobs lost 2020 oil crash** — visceral.
- **Ransomware +935%** — shock.
- **Газпром Cognitive Geo: 3-4 месяца → minutes** — конкретно.

### Overload / skipped:

- **MethaneSAT 410 t/h = 3.6 Mt/год = 50% выше EPA** — **три baseline за одно утверждение**. Я выберу одну (50%), остальное забуду. **Plan ОК что baseline есть** — но **на слайде должно быть ОДНО число**.
- **«New Mexico 1.2% intensity vs Texas 3.1%»** — что такое «intensity»? Доля? Лошадиные силы? Plan не раскрывает.
- **Eni HPC6: 14 000 MI250X, 606 PFLOPS, $104M, Top500 #5 из 500** — **четыре цифры подряд**. Top500 #5 — это **memorable** anchor, оставить только её + одну техническую.
- **Aramco METABRAIN: 250B параметров, 7T токенов, 90 лет данных, 6 000 employees, 430 use cases, $1.8B 2024, vs $440B revenue = 0.4%** — **ОЧЕНЬ много цифр в одном слайде**. Скажу честно: это будет «текст бля», я не запомню ничего кроме «250B + Aramco». **Слайду нужен один-два числа + остальное в notes.**
- **Roснефть Башнефть Илишевское: 23 software products, 10 commercial, +60% remotely-controlled, +5% energy efficiency, -5% logistics, +1 Mt/год, ~1B руб./год, +5.9% vs Башнефть total ~17 Mt/год 2023** — **семь чисел в одном слайде**. Хуже чем Aramco. **Cut 2-3 metric'а, keep most striking.**
- **Honeywell UOP: 310+ units / 100+ sites / plan 750+ within year, total global refineries ~700** — 4 числа, ОК но почти overload.

### Shocking vs «just data»:

- **190× CCS gap** = **shocking**. Если IEA target 7.6 Gt и сейчас 40 Mt = 0.5%, то «нам нужно увеличить в 190 раз за 25 лет» — это **physically невозможно** имхо. Это **lesson, не stat**.
- **Permian VIIRS 2 593 plumes** — shocking из-за визуала.
- **Ambyint +15%** — «just data», нормальный bump.

## 7. Где скучно

**Конкретные секции / темы, где я отвлекался:**

1. **«Инструменты на каждом уровне таксономии» секция (lines 116-199 в plan).** Это **vendor list overload**: Q1 = 6 vendors, Q3 = 7 vendors, Q2 = 8 vendors, Q4 = 6 vendors, cross-cutting infrastructure = ещё 5+ vendors. Я после 3-го забываю первого. **Знаю что это plan-internal для downstream agents (не для слайда),** но если хотя бы 30% этого попадёт в speech как «Aspen, Ambyint, Osprey, Halliburton, SLB Avocet, Honeywell UOP» — будет alphabet soup. **Recommendation:** в chapter — оставить full list; в slides — **максимум 2-3 vendor per слайд** + остальные **в speech как throwaway mention**.

2. **Раздел 4 (Q4) — Refinery AI stagnation (s31).** Абстрактно. «Multi-physics constraints (mass+energy+reaction+corrosion) — ML surrogates lose consistency на edge cases» — звучит как **PhD thesis abstract, не лекция для 3-курсника**. Нужен конкретный case: «Yokogawa попробовала на одной колонне — успех. Попробовала plant-wide — failed на ____ (имя plant, год, что произошло)». Без этого я просто слышу слова и не запоминаю.

3. **Hero illustrations + 6-tier acquisition разделы (lines 449+).** Это **producer-internal**, нормально что в plan'е. Но **я как читатель** их перелистываю.

4. **Open questions / `[VFY-day-of]` lists.** 10 вопросов для fact-checker — много. Понимаю что это **flagging для downstream**, не для меня. ОК что в plan'е, но я **бы prioritized 3-4 ключевых для prominent display**, остальные глубже в plan.

5. **Раздел 5, slide s36 (Cognitive Pilot + Татнефть/ЛУКОЙЛ/Сургутнефтегаз).** «АнтиХрупкий завод Нижнекамск, ЛУКОЙЛ Volga-Ural, Сургутнефтегаз — limited public info `[VFY-day-of]`». Если info limited, **зачем этот слайд?** Лучше cut и оставить **Газпром нефть + Роснефть как main RU cases**. Cognitive Pilot — agricultural случай transferable to O&G — это **stretch**, который меня confuses ('причём тут сельхоз?').

6. **Long word combinations.** «Российский case — Роснефть Digital Field Башнефть Илишевское» — три уровня вложенности. Tongue-twister.

## 8. Keystone retention test

Без перечитывания, отвечаю как студент:

- **Главная axis лекции?** Двумерная матрица: **доступность данных × определённость физики**. 4 квадранта, AI работает по-разному в каждом.

- **В каком квадранте AI essential (не augmentation)?** **Q2 (high data, low physics) — methane MRV.** Потому что **нет классической физики для cross-source data fusion** (satellite + aerial + drone + ground OGI). Без AI не получится integrated map.

- **В каком квадранте AI doesn't work / опасен?** Знаю что **Q4 (energy transition)** — оба low, hallucination риск, 100-летний horizon. Plus **safety-critical SIS (BOP/PRV/ESD)** — НЕ AI, deterministic only под SIL3/SIL4. Это **критерий через все квадранты**, не только Q4.

- **Назови 2 case study, которые ты помнишь:**
  1. **MethaneSAT loss** (Q2, июнь 2025, single point of failure, EU regulator lesson).
  2. **BP + Beyond Limits** (Q3, $20M cognitive AI, vendor пивотировал, anthropomorphic overpromise).

**Verdict retention test:** **passing.** Keystone в моей голове сохранён, базовый mapping case-to-quadrant работает.

## Recommendation для Phase 1 revision

### Top priority (P0)

1. **Keystone «physics certainty» одной строкой на s05.** Plan сам признаёт risk в Risk 1. Inline gloss на keystone bottom bar: **«physics certainty = есть ли установившаяся численная модель, дающая надёжный ground truth»**. Без этого keystone «трогает но не оседает» для 3-курсника.

### High priority (P1)

2. **Раздел 3 (methane MRV) — добавить «alphabet soup» опорный слайд.** В первом упоминании Раздела 3: что такое OGI, OGMP Level 4/5, MRV, LDAR. 5 аббревиатур за 30 секунд — слишком. Лучше отдельный helper slide / dedicated chapter sub-section в начале Раздела 3.

3. **s11 (Aramco METABRAIN) + s10 (Роснефть Башнефть) — cut numbers на слайде до 2-3.** Сейчас 7+ чисел на каждом — overload. Остальное — в speaker notes / chapter.

4. **s36 (Cognitive Pilot + Татнефть/ЛУКОЙЛ/Сургутнефтегаз с `[VFY-day-of]`)** — слайд слабый. Либо cut, либо заменить на сильный 1-кейс slide (только Газпром OR только Роснефть deep-dive).

5. **s31 (refinery AI stagnation) — добавить named pilot failure case.** Сейчас abstract. Конкретный «Pilot X на refinery Y попробовал plant-wide ML controller, проект закрыли в году Z из-за ____» — даст retention. Без этого slide читается как теоретическая нота.

### Polish (P2)

6. **Cybersecurity (s37) переместить или дать own micro-section.** Currently «squeezed» в Раздел 5 Россия. Ransomware +935% + Colonial — заслуживают either own slide в Разделе 6 closing OR own section divider («Cross-cutting risk» 2-3 слайда).

7. **Inline gloss первого упоминания для:** wildcat, FPSO, 4D seismic, plume migration, downhole, basin/play, stripper well, bopd, intensity (методан context), PINN. Plan уже имеет Russification table — добавить «when first appears, inline gloss» как Phase 2 mandate.

8. **«Инструменты на каждом уровне таксономии» — в chapter оставить full, в slides — max 2-3 vendor per slide.** Plan §-named speech-narrative → слайд check уже есть, but explicit ceiling «не более 3 vendor per visible slide» сэкономит retention.

9. **Connect Раздел 5 (Россия) к keystone сильнее.** Currently «4 квадранта в санкционном режиме» — это claim, но без structural mapping. Slide s33 section divider — добавить mini-matrix recap «как Россия дислоцируется по 4 квадрантам» (например: Q3 Газпром Cognitive Geo заменяет SLB Lumi; Q2 — no MethaneSAT, no EU pressure; etc.). Это сделает Раздел 5 не «дополнительный кусок», а **organic 5-я перспектива**.

10. **«Top replacements» Russification table — добавить inline brief gloss для top-15 терминов на КАЖДОМ слайде first-use.** Plan уже flags «pre-GATE deep latin-token scan» — но glossing first-use должно быть policy, не just check.

### Что в plan'е сильно (keep как есть)

- **Failures bucket structure — отлично** (10 documented + 6 ограничений + 6 critериев + 6 alternatives). Это **дидактический backbone** курса. **Don't touch.**
- **Hook (Permian VIIRS night)** — strong, keep.
- **MethaneSAT loss как central drama** — keep, expand if anything.
- **190× CCS gap** — visceral, keep как Q4 anchor.
- **Q1 → Q3 → Q2 → Q4 order** — works, drama justified.
- **Anonymization section** — proper, follows lec-09 lesson.
- **Closing s39 (MethaneSAT first global methane map, февраль 2026) bittersweet payoff** — strong поэтический jewel. Keep.

---

**Final verdict: APPROVE-WITH-POLISH.** Plan engaging, не boring overall, **строит критическое мышление вместо AI-восторга** — это main quality. Главный gap — keystone «physics certainty» не self-explanatory + перегруз цифрами на 2-3 ключевых slides + alphabet soup в Разделе 3. 10 правок выше (5 high priority + 5 polish) сделают этот plan «обчитываемым студентом без преподавателя».
