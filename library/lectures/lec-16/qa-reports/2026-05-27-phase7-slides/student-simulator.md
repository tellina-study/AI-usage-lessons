# Student simulator (in-lecture, ИУ6 3 курс) — Лекция 16

**Verdict:** APPROVE-WITH-POLISH

## TL;DR

В зале сидел внимательно первые ~45 минут — keystone-матрица за 5 сек считалась, кейсы Ambyint / MethaneSAT / Aramco держали. К 55-й минуте устал на Q4 (s30/s31 «squeezed» layout — изображение и текст втиснуты в нижнюю половину, ощущение «отчёт», а не «слайд»). К Россия-разделу (s35-s38) восстановился, потому что наконец-то знакомые названия. Закрытие s40 + cornerstones s41 — нормальные, но **hero s42 (MethaneSAT карта) выглядит crop'нутой / маленькой** — для финального hero ощущение «обрезали». Главная axis «данные × физика» через 75 минут реально удержалась — это редко.

## 1. Hook (s01-s05)

- **s01 Permian VIIRS hero.** Зацепило. Большая «2 593» цифра справа + ночная картинка факелов слева — за 3 сек понял: «о, это про реальный масштаб, не про красивые роботы». Маленький под-текст «AI в нефтегазе — не «уличить на 5%», а способ закрыть конкретные провалы» — поймал, но требует чтения. Hero работает.
- **s02 cover.** Стандартный, но «Шесть разделов через матрицу данные × физика» уже намёк на структуру. Главный вопрос внизу — длинноват, по-моему я начал читать и пропустил конец «10 documented провалов». ОК.
- **s03 about.** Три карточки Аудитория / Формат / Вы научитесь — структура норм. «12+ рабочих кейсов · 7 разделов» — конкретика хорошая. Bottom-bar «10 разобранных провалов + 12+ рабочих кейсов = инженерный фильтр, не каталог инноваций» — это **меня купило**. Я понял что лекция не «AI спасёт нефтегаз».
- **s04 lecture-map 7 разделов.** Карточки с кругами 1-7 + tag типа «3 кейса · 2 провала» под каждым — отлично. Glossary bar внизу (MRV/OGI/CCS/EGS/SIS) — **спасибо, я слова эти не знаю**. Без этого следующие 60 минут были бы пыткой.
- **s05 keystone 2×2 matrix.** За 5 сек считал: 4 квадранта × 2 оси Данные / Физика; Q1=мультипликатор, Q2=essential, Q3=physics-first, Q4=struggle. **Это лучший keystone из лекций курса, что я видел** — потому что в каждом квадранте уже стоит конкретный vendor / стартап (Ambyint / MethaneSAT / METABRAIN / Northern Lights), а не абстракт. Bottom bar про alternative tool — попал, я уже подсознательно ожидал «когда AI не нужен» секции. **Strong.**

## 2. Section dividers (s06/s13/s21/s28/s34)

- **s06 «Q1 Зрелое производство».** Большая Q1 буква + правая колонка «мультипликатор / самый структурно проваленный». Тэг «3 рабочих кейса · 2 структурных провала · 86% пилотов застряло — статистическая норма». **Очень хорошо** — сразу понятно tone раздела (без таймингов!). Я бы и не догадался что бывает иначе если бы не помнил предыдущие лекции.
- **s13 «Q3 Разведка фронтиров».** Тот же паттерн, ОК. «$50-100M wildcat-скважина» в правой колонке — number stuck.
- **s21 «Q2 Метановая MRV».** ОК, но правая колонка ~4 строки текста — мог бы быть короче. «Один спутник = катастрофическая единичная уязвимость» — это **foreshadow MethaneSAT loss**, я почувствовал «о, что-то произошло». Работает.
- **s28 «Q4 Энергопереход».** «Самый честный квадрант» — нравится формулировка.
- **s34 «Россия — sanctions, insourcing, vertical integration» (full content slide, не divider).** Структурно это **уже не divider, а 2×2 matrix slide** про 4 квадранта в российском контексте. Я ожидал большую букву «Россия» / число / mood — но получил densный 4-секционный слайд. **Чуть сбило с ритма** — другие 4 раздела имели «дыхательный» divider, а Россия сразу контент. Не критично, но pattern break.

## 3. Cases engagement

**Memorable:**
- **s08 Ambyint InfinityRL +15% / 200 скважин** — конкретные числа, baseline указан (100-500 bopd), delta объяснена. И сразу bottom bar «когда не работает: stripper wells <10 bopd». Это **идеальный strong-case template** — успех + граница применимости рядом.
- **s17 BP+Beyond Limits — $20M, 7 лет, 0 кейсов.** Красная панель «Что получили» с большой «7 лет публичных результатов нет» — emotional. Bottom bar «Cognitive AI имитирует геолога — anthropomorphic frame» — клик: понял, почему обещание провалилось.
- **s23 MethaneSAT loss 20 июня 2025.** Timeline слева + 4 урока справа + большая «15,5 / 60 мес = 26% lifetime». Bittersweet. **Это самый emotional slide лекции** — миссия NGO потеряна, $5,7M/мес vs $1,5M/мес планировалось. Долго не забуду.
- **s37 Ransomware +935% год к году + Colonial Pipeline anchor.** Bar chart 100 → 1030, прямой контекст «AI расширяет attack surface», alternatives Dragos/Claroty/Cisco. **Это слайд я бы пересказал родителям.**
- **s10 Роснефть Digital Field Башнефть Илишевское.** «+1 Mt/год» big number + «~1 млрд ₽/год» — конкретно. Caveat «российские KPI = self-reported» — appreciate честность.

**Forgettable:**
- **s24 Post-MethaneSAT (Carbon Mapper / GHGSat / Bridger / SeekOps).** 4 квадрата с 4 vendor — слишком много названий, я запомнил только Carbon Mapper и GHGSat. SeekOps + Project Canary смешались.
- **s33 Refinery plant-wide stagnation.** Слайд маленький / squeezed (картинка явно ужата в верх) + 5-bullet текст справа. Я прочитал заголовок и bottom bar «Q4 структурная проблема» и пошёл дальше.
- **s36 Российский Q1 flagship + средний эшелон.** Татнефть / ЛУКОЙЛ / Сургутнефтегаз вместе в одной правой панели — это 3 компании, каждая = bullet 2-3 строки. Я потерял где конкретный КПИ для Татнефти.

**Emotional:**
- **MethaneSAT loss (s23)** — топ-1 emotional. NGO миссия, $88M бюджет, потеря после 26% lifetime.
- **2020 oil crash 107k jobs за 6 мес (s38)** — узнал что после этого AI программы заморожены 18-24 мес. Контекст «AI не защищает — он эффект усиления» — meaningful.
- **BP+Beyond Limits 7 лет = 0 (s17)** — anger / cynicism к корпоративной AI-PR.

## 4. Charts / diagrams readability

Прочитал:
- **s07 bar chart 86% pilot stuck vs 67% cross-industry** — простой, читается. 5 структурных причин справа полезны.
- **s14 Eni HPC6 vs Aramco METABRAIN** — squeezed layout, маленькие карточки. Прочитал заголовки и числа ($104M / $1,8B), детали типа «AMD MI250X / Grace Hopper» отлетели.
- **s25 4× discrepancy bar chart (4 / 7 / 15 Mt/год)** — прочитал. «41% false negatives» в 9-satellite test 2024 — стук в голове.
- **s31 CCS 190× scale-up gap bar chart Northern Lights vs IEA 2050** — squeezed layout, левая колонка bar занимает половину слайда, правая колонка 6 bullets+1 big number («40%»). Прочитал заголовок и 190× в нижнем bar, но цифру 40% (Gartner 2027 prediction) я ассоциировал не с тем — пришлось перечитать.

Пропустил:
- **s30 Northern Lights image + metrics** — squeezed layout, изображение крошечное (футбольное поле тоже видно, но wave-плакат типа сжат до 1/4 слайда). Я скользнул глазами по «1,5 Mt/год · 7 600 Mt/год IEA target 2050». Понял про 190× gap из bottom bar — на слайде это не сразу очевидно.
- **s32 Fervo EGS image + IPO** — то же squeezed. Запомнил «$1,89 млрд IPO» и забыл всё остальное (Cape Station, hydraulic fracking).

## 5. Hero closing (s42 MethaneSAT global methane map)

**Squeezed.** Hero ОБЯЗАН быть ≥40% площади per CLAUDE.md, но визуально s42 выглядит как обычный 2-column slide с маленькой картинкой слева. Текст справа («Спутник потерян — карта осталась», «Final framing: AI не отступил → измеренный успех + структурная уязвимость в одном кадре») — это **хороший emotional closing**, но визуально не feel «hero». Сравнить с s01 — там «2 593 факельных шлейфа» — большая цифра + большая картинка Permian = hero. На s42 текст в правой колонке + маленькая обрезанная карта = не feels payoff.

**Bridge к Лекции 17 «systematization»** — bottom bar упоминает. ОК.

## 6. Pacing

**Want to stay:**
- s05 keystone — хочется ещё 30 сек посмотреть на матрицу.
- s17 BP+Beyond Limits failure — конкретика, хочется паузу обдумать.
- s23 MethaneSAT loss timeline — хочу прочитать 4 урока медленно.
- s38 2020 crash + Deepwater Horizon — два эмоциональных anchor, нужна пауза.

**Felt rushed:**
- s09 Q1 Vendor landscape — 10+ имён компаний (Ambyint / OspreyData / SLB Avocet / Halliburton DecisionSpace / AspenTech Mtell / Honeywell UOP / Yokogawa / ABB / Emerson + bonus Nabors / NOV / Precision). За 1,5 минуты невозможно усвоить. **Я просто записал «10+ vendors» и пошёл дальше.**
- s20 Methane MRV alphabet — 6 терминов (MRV / OGI / LDAR / OGMP 2.0 / SIL/SIS / bopd/ESP) сразу. Хорошо что включено, но 1,5 минуты — мало. Я перечитал OGI и LDAR, остальное скользнул.
- s24 Post-MethaneSAT players — 4 vendor card одновременно. Хочется или select 2, или 2 раза по 2.

## 7. Russification + terminology

**Хорошо:**
- Quick glossary bar на s04 (MRV, OGI, CCS, EGS, SIS) — без этого зашёл бы в стену из акронимов.
- s20 dedicated alphabet helper slide — спасибо, что ввели 6 терминов до Q2 раздела.
- Brand names (Ambyint, MethaneSAT, Cognite, Eclipse) остались как есть — правильно, это бренды.
- Inline gloss типа «bopd / ESP = баррелей нефти/день / погружной электронасос» — приятно.

**Сбивает:**
- Q1/Q2/Q3/Q4 quadrant labels везде на английском («Q1 Mature», «Q2 Methane», «Q3 Frontier», «Q4 Transition») — на top bar nav, на divider'ах, на keystone, на synthesis s40. Я **выучил** что Q1=зрелое за 5 мин, но первые 3 раза глаз спотыкался. Можно было бы «Q1 / Зрелое», но это nitpick.
- «Custody transfer metering» (s12) — никакого inline gloss. Я **не понял** что это. Из контекста угадал «передача товарной нефти» — но это случайно повезло.
- «Frontier exploration» / «mature production» — frequent. Понимаю, но было бы лучше «разведка фронтиров» / «зрелое производство» (что и используется на divider'ах) везде последовательно.
- s30 «AI helps per-unit cost. AI не масштабирует индустрию.» — calque «per-unit cost» можно было «удельная себестоимость».
- s14 sub-title «Не коммодизируется как облако — стратегический CapEx. Малые операторы вытесняются capital barrier.» — «капитальный барьер» был бы понятнее, чем «capital barrier».
- s27 sub «Когда AI не нужен — OGMP Level 5 (прямое измерение) + custody transfer metering.» — «custody transfer» опять не glossed.
- s30 — слайд маленький, читать сложно, плюс bottom bar «AI helps per-unit cost. AI не масштабирует индустрию.» — англо-русский гибрид.
- **s33 заголовок «Refinery plant-wide stagnation = Q4 структурная проблема»** — «plant-wide» можно «общезаводская». Это L4+ industrial лекция, аудитория универсальная — можно русифицировать сильнее.

Tech acronyms (PINN / DeepONet / FNO / ROM / POD / THMC) — **не помню чтобы видел их на slides**. Возможно только в speaker notes / chapter. На slides из таксономии — PINN всплывает 1 раз на s31 («Physics-informed neural networks (PINN) — research-grade, не commercial»). ОК.

## 8. Numbers density

**Stuck:**
- **2 593 факельных шлейфа Permian (s01)** — главное число hero.
- **86% pilot stuck vs 67% cross-industry (s07)** — clear contrast.
- **+15% / 200 скважин (s08)** — clean delta.
- **$20M / 7 лет / 0 кейсов (s17)** — emotional triple.
- **410 т/ч + 50% над EPA (s22)** — MethaneSAT flagship.
- **15,5 / 60 мес = 26% lifetime (s23)** — MethaneSAT loss.
- **+935% ransomware (s37)** — striking.
- **190× scale-up gap CCS (s31)** — big concept.
- **+1 Mt/год / ~1 млрд ₽/год (s10)** — Башнефть Digital Field.

**Overload:**
- **s14** — 9 чисел в одном слайде (606 PFLOPS, 477 sustained, 14 000 GPU, $104M, 250 млрд параметров, 7 трлн токенов, 90 лет данных, $1,8B, 6 000 сотрудников, 430 use cases). Half я забыл сразу. Squeezed layout не помогает.
- **s11** — 8 чисел между Cognite и C3.ai (~$300M, $2-3B, $94M, +40% YoY, 871 сотрудник, BHC3, $18M из $310M, +48% YoY). Я понял «Cognite — IPO отменён, C3.ai теряет долю», конкретику не удержал.
- **s9** — 10+ vendor names + Nabors PACE-X bonus. Перечисление выматывает.
- **s31** — bar chart Northern Lights 1,5 vs IEA 7 600 (ОК) + 6 bullets + «40% Gartner» + «Sleipner Norway 1996 / 30 лет / $1B+». Choose 3, не 7.

## 9. Failure share perception

**Да, чувство «эта лекция учит говорить нет ИИ» — есть.**

Recall конкретики провалов:
- 86% pilot stuck (s07)
- Aspen Mtell alert fatigue (s07b)
- BP+Beyond Limits $20M (s17)
- IBM+Repsol Kalimba (s18)
- MethaneSAT loss (s23)
- 4× discrepancy (s25)
- CCS 190× gap (s31)
- Refinery stagnation (s32)
- 2020 oil crash 107k jobs (s38)
- Ransomware +935% (s37)
- Cognite + C3.ai declining (s11) — half failure

**+ 6 «когда AI не нужен» критериев (s12)**, **+ alternative-tool slides (s19, s27, s33)**, **+ Q&A Q3 «назовите 3 критерия когда не применять» (s41)**.

Это **structural feel** — не «AI everywhere», а «AI работает в Q1-Q2, осторожно в Q3, опасен в Q4». Курс-обещание выполнено. Strong.

## 10. Boring slides

5 примеров где «в телефон полез / отвлёкся»:

1. **s09 Vendor landscape Q1** — 10+ компаний bullets, без эмоции. Я записал «много vendor» и потерял интерес. Зачем мне как студенту 10 имён, если я не работаю в индустрии?
2. **s11 Cognite + C3.ai** — финансовая хроника двух vendor'ов. ARR $94M, +40% YoY — это для инвестора, не для меня. Главный takeaway («foundation models eat vertical specialists») есть в bottom bar — этого было бы достаточно одним слайдом без чисел.
3. **s14 HPC race Eni vs Aramco** — squeezed layout + 9 чисел + 2 vendor blocks. Я понял «дорого, $100-400M, малых вытесняет». Точная цена / GPU модель / PFLOPS — не запомнил, отвлёкся.
4. **s30 Northern Lights** — squeezed layout, маленькое изображение, 5 bullets + 1 big number («1,5 Mt/год»). Прочитал bottom bar, пошёл дальше.
5. **s33 Refinery plant-wide stagnation** — squeezed layout, картинка-крошка, 5 bullets о причинах stagnation. Bottom bar говорит главное — слайд можно ужать в 2 строки.

## 11. Strong slides

5 примеров где «о, интересно, хочу остаться»:

1. **s05 Keystone 2×2 matrix** — за 5 сек вся axis лекции. Inline definitions «physics certainty / data availability» внизу — clean.
2. **s08 Ambyint InfinityRL** — strong-case template: success metric + verifiable baseline + bottom bar «когда не работает». Это **должно быть лекторный шаблон** для всех кейсов.
3. **s17 BP+Beyond Limits failure** — 2-колоночный «Что обещали (синий) / Что получили (красный)». Visual contrast = понимаешь за 5 сек.
4. **s23 MethaneSAT loss** — timeline + 4 урока. Emotional + структурный lesson.
5. **s12 «Когда AI НЕ нужен в Q1 — 6 структурных критериев»** — 6 пронумерованных карточек, каждая = 1 fail-mode. Bottom bar «Главный навык курса: уметь сказать нет». Это **меня купило**, как «вот ради чего я слушаю».

## 12. End retention test

Без перечитывания:

**Q1. Главная axis лекции?**
Матрица 2×2: данные (high/low) × физика (high/low). 4 квадранта: Q1 mature production = AI мультипликатор; Q2 methane MRV = AI essential; Q3 frontier exploration = physics-first AI augmentation; Q4 energy transition = AI и физика struggle вместе. + alternative tool за каждым AI-внедрением.

**Q2. 3 documented failures?**
1. BP + Beyond Limits $20M за 7 лет = 0 кейсов (vendor concentration + anthropomorphic overpromise);
2. MethaneSAT loss 20 июня 2025 после 26% lifetime (SPOF, hardware reliability, AI зависит от upstream sensor hardware);
3. 86% AI-проектов в энергетике застряли в пилоте (data quality / legacy IT / talent / safety culture / ROI horizon mismatch).

**Q3. 2 case где AI essential (не augmentation)?**
1. **MethaneSAT / Carbon Mapper / GHGSat methane MRV** — слияние спутник + аэро + ground sensors + атрибуция малой утечки = классической альтернативы нет, AI essential;
2. **Permian методан 410 т/ч detection** — без AI бы не выявили (EPA inventory 50% занижала).

**Q4. 2 alternative (не-AI) инструмента?**
1. **Eclipse / INTERSECT / CMG** physics-based reservoir simulators — для регуляторных submissions mandatory, ML не сертифицируется;
2. **Picarro G2210-i / FLIR GFx320 ground OGI** — для OGMP Level 5 direct measurement compliance + custody transfer mass flow meter.

**Q5. 1 case «здесь AI не нужен»?**
**BOP / PRV / ESD = SIS (Safety Instrumented Systems) под IEC 61511 SIL3/SIL4.** Детерминированно + сертифицируется, ML не сертифицируется. Deepwater Horizon 2010 = alarm bypass culture anchor.

**Retention: hit 5/5.** Это **сильно лучше среднего курса** — обычно после лекции остаются 2-3 числа и 1 vibe.

## Recommendation для Phase 8 revision

**Verdict: APPROVE-WITH-POLISH.** Лекция сильная, axis работает, retention 5/5. Полировка:

1. **HIGH — fix «squeezed» layout on s16 (SLB Lumi), s22 (MethaneSAT 4 марта), s30 (Northern Lights), s31 (CCS 190× gap), s32 (Fervo), s33 (Refinery), s38 (2020 crash), s42 (hero closing).** Все эти слайды визуально занимают только верхнюю или нижнюю половину холста — нижняя или верхняя половина пустая. Особенно критично для **s42 hero** — должен быть ≥40% area per CLAUDE.md hero-rule. Запросить у designer'а уточнение `slide_height` / layout — возможно baseline image embed size слишком мал.
2. **MEDIUM — densify Q1 vendor landscape s09 OR break in two.** 10+ vendor names за 1,5 мин — выматывает. Choose 5 anchor vendors per category, остальное в speaker notes.
3. **MEDIUM — s11 Cognite/C3.ai numbers overload.** 8 финансовых чисел для не-инвестора overkill. Choose 3 striking numbers (Cognite IPO cancel 2023, C3.ai O&G 5.9% revenue, C3.ai pivot to federal/defence).
4. **LOW — Russification polish on s12, s14, s27, s30, s33.** «custody transfer / capital barrier / per-unit cost / plant-wide» — inline gloss или RU перевод. **Не критично**, но user правил каждую лекцию L1-L9 + L10 — preempt.
5. **LOW — s34 «Россия» — pattern break.** Этот слайд имеет divider-style top-bar + tag «По 4 квадрантам keystone-матрицы», но контент уже 2×2 matrix. Решить: либо отдельный divider s34a с большой буквой «РФ» + tag «3 программы · санкции · vertical integration», либо снять divider-feel и сразу контент. Сейчас smooth pattern до s33 ломается.
6. **LOW — s24 Post-MethaneSAT 4 vendors** — может стать s24a (Carbon Mapper + GHGSat — спутники) + s24b (Bridger + SeekOps + Project Canary — наземные/аэро). Сейчас 4 одновременно — overload.

**Не критично, можно одобрять deck с polish-round 1.**
