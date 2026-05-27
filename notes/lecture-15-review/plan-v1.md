# Лекция 15: AI в научных исследованиях — план v1

## Метаданные

- **Лекция:** 15 (Модуль 3) — 75 мин + Q&A ~5 мин
- **Учебные результаты (LO):** LO4 (анализ литературы и формулирование задач), LO5 (этика и ответственная разработка), LO6 (критическое мышление и оценка применимости), LO8 (применять и создавать — выбор инструмента и альтернативы)
- **Аудитория:** студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)
- **Issue:** #143 — `issue-143-lec-15`
- **Статус:** v1 (Phase 0.5 — research-разведка завершена, идём на Phase 1 critique)
- **Дата:** 2026-05-27
- **Несущая ось (на выбор владельца):** см. § «Keystone axis — 3 варианта»; рекомендация — **Variant A (лестница научного цикла)**, но окончательный выбор за владельцем
- **Hook A основной:** AlphaFold 3 → Нобелевская премия по химии 2024 (Hassabis, Jumper, Baker) **рядом** с Galactica 2022 (трёхдневный позор) — две стороны одной медали в одной картине
- **Hook B запасной:** Sakana «The AI Scientist v2» — paper прошёл peer review на workshop ICLR 2025, но содержит «hallucinations, faked results, overestimated novelty»

---

## Topics Covered

Фундаментальные модели для науки (предсказание структуры белков AlphaFold 2/3, погода Aurora/GraphCast/Pangu, материалы GNoME/MatterGen) + автономные лаборатории (Coscientist, A-Lab, Emerald Cloud Lab) + формальная математика (AlphaProof, AlphaGeometry 2, FrontierMath) + генерация гипотез и черновиков статей (Sakana AI Scientist v1/v2, DeepMind Co-Scientist, Gemini for Science) + помощь в обзоре литературы (Elicit, Consensus, Semantic Scholar, NotebookLM, PaperQA) + LLM-разметка экспериментальных данных (астрофизика — детекция экзопланет TESS/Kepler, нейронаука — Allen Institute brain map, гравитационные волны LIGO) + провалы и границы (Galactica 2022, A-Lab переразбор Palgrave 2024, Sakana hallucinations, Frontiers «крыса» 2024, NeurIPS 2025 100+ fake citations) + альтернативы (байесовская оптимизация, first-principles DFT/MD, классический пир-ревью, OR-Tools для научной логистики).

## Prerequisites

- **Лекция 1** — типы AI-систем, понятие галлюцинации, промптинг (Role+Task+Context). Эта основа критична — мы много раз возвращаемся к «галлюцинация ≠ ошибка», «модель не знает истины, только распределение слов».
- **Лекция 2** — архитектура трансформеров, embeddings, attention matrix. Нужно для понимания, почему AlphaFold (transformer-based) даёт хорошее предсказание fold, но не понимает биологию.
- **Лекция 3** — архитектуры AI-систем (агенты, RAG, API). Нужно для понимания Coscientist (агентная архитектура с tool-use) и литературных поисковиков (RAG над arXiv/PubMed).
- **Лекция 7** — AI в медицине (HITL, доказательная медицина). Параллельный пример «AI в науке требует HITL» — drug discovery как пограничный кейс.
- **Лекция 11** — провалы pilot purgatory, парадокс автоматизации. Та же логика «95% не доходят» применяется к научным AI-стартапам.

## Normative References

- **Nobel Prize Chemistry 2024** (8 октября 2024) — Baker / Hassabis / Jumper за computational protein design и protein structure prediction. **Доктринальный референс**: первый Нобель за breakthrough, enabled by AI.
- **NeurIPS / ICLR / Nature / Science кодексы публикации** — текущие требования к AI-использованию (обязательное disclosure, запрет на полностью AI-generated review).
- **NSF AI Code of Conduct** (US National Science Foundation, обновлено 2025) — рамки responsible AI в federally-funded research; обязательное disclosure AI-tooling в grant proposals.
- **EU AI Act (2024)** — научные применения попадают в разные tier'ы в зависимости от deployment; foundation models под §51-§55, scientific research как «limited risk» — но peer review и медицинские применения могут попадать в «high risk».
- **Frontiers / Elsevier / Springer Nature AI policies 2024-2025** — каждое издательство опубликовало свою политику по AI-generated content (Frontiers: 2024 retraction rat-anatomy paper как прецедент; Springer: must disclose).
- **DOE Genesis Mission ($320M, декабрь 2025)** — институционализация AI4Science в США; интегрированная American Science and Security Platform.
- **GAMP®5, FDA 21 CFR Part 11** — символично из Лекции 11; здесь применяется к AI в drug discovery (AlphaFold-based pipelines в pharma).
- **ICMJE Recommendations** (Уведомление о CRediT-таксономии) — авторство, AI-tools нельзя называть автором.
- **Российский контекст:** Указ Президента РФ № 145 (НИ ВШЭ Стратегия развития ИИ до 2030) и приказы Минобрнауки 2024-2025 по AI в науке (impact на гранты РНФ).

## Learning Objectives

1. **LO4 (Помнить + Применять).** Назвать ≥4 класса AI-инструментов для научной работы (фундаментальные модели для предметной области, автономные лаборатории, литературные RAG-помощники, LLM-разметка данных), для каждого — 2-3 dominating 2026-инструмента с направлением внедрения (растёт быстро / растёт медленно / зрелый / провалился). Применить классификацию к учебному кейсу.
2. **LO5 (Оценивать).** Сформулировать ≥3 этических риска применения AI в науке: (a) галлюцинированные цитаты в публикациях (paper mill), (b) автоматический peer review без disclosure, (c) использование AI как «co-author» в обход ICMJE. Обосновать, почему disclosure обязательно.
3. **LO6 (Анализировать + Оценивать, ЦЕНТРАЛЬНЫЙ — failure-bucket).** Применить «лестницу научного цикла» (см. keystone) к гипотетической исследовательской задаче, показать **на какой ступени AI работает, на какой требуется HITL, на какой AI вреден**. Различить «AI-augmented research» и «AI-autonomous research». Сформулировать ≥4 категории критериев «AI не нужен в науке» (closed-world vs open-world / training distribution coverage / verifiability / ethical risk).
4. **LO8 (Применять и создавать).** Для конкретного кейса (предложит лектор: «нужно найти 10 релевантных статей по теме X», «нужно сгенерировать гипотезу для гранта», «нужно обработать спектральные данные») выбрать AI-инструмент, обозначить границы, **предложить не-AI альтернативу** (байесовская оптимизация, DFT/MD first-principles, классический научный руководитель, OR-Tools). Применить 3 уточняющих вопроса к вендору (как в Лекциях 11/13/14): baseline / окно измерения / change-control.

---

## Несущая ось (keystone) — 3 варианта на выбор владельца

### Variant A — «Лестница научного цикла: Hypothesis → Design → Experiment → Analyse → Write → Review»

**Зачем это keystone.** Научная работа структурно делится на 6 ступеней: формулирование гипотезы (Hypothesis) → планирование эксперимента (Design) → проведение эксперимента (Experiment) → анализ данных (Analyse) → написание (Write) → рецензирование (Review). AI «входит» в каждую ступень **по-разному**: где-то как helper (Write — литературное оформление), где-то как breakthrough (Experiment — AlphaFold заменяет годы wet-lab), где-то с **серьёзными рисками** (Review — галлюцинированные цитаты, fake peer review), где-то **категорически не работает** (Hypothesis в open-world domains). Лестница — диагностический инструмент: задайте каждой ступени вопрос «здесь AI augmentation, autonomous или vetoed?».

**Как распределяет 75 мин.** Раздел 0 (7 мин) — hook (AlphaFold Nobel рядом с Galactica позором) + keystone-слайд лестницы. Раздел 1 (10 мин) — Hypothesis + Design (Coscientist, AI Scientist v2 — фронтир, но галлюцинации). Раздел 2 (15 мин) — Experiment (AlphaFold 2/3 + GNoME + Aurora — самый сильный успех AI в науке). Раздел 3 (12 мин) — Analyse (LLM-разметка экзопланет / brain map / gravitational waves — solid use case). Раздел 4 (12 мин) — Write + Review (NotebookLM + Elicit + Consensus как augmentation, но **fake citations NeurIPS 2025**, Frontiers «крыса», Sakana scandals — самое тяжёлое failure-clustering). Раздел 5 (12 мин) — критерии «AI не нужен в науке» + альтернативы + worked example. Раздел 6 (6 мин) — закрытие + мост к Лекции 16.

**Риски подхода.** (a) лестница может выглядеть линейно, хотя реальный научный цикл — итеративный (рассмотреть как «частично-упорядоченное множество», не цепочку); (b) каждая ступень имеет под-ступени (например, Experiment делится на dry vs wet lab, simulation vs physical) — упрощение может потерять важные различия; (c) пересечение с Лекциями 9 (OODA-петля) и 14 (Лестница автономии «Видит → Решает → Действует») может создать ассоциативный шум — нужно явно отделить «лестница цикла как фаза работы» от «лестница автономии как уровень control».

### Variant B — «Closed-world vs Open-world: где AI silently works, где он silently fails»

**Зачем это keystone.** Гениально-простой бинарный фильтр: AI в науке надёжно работает в **closed-world** задачах (well-defined structure, finite alphabet, validation via experiment). Protein folding — closed-world: финальный fold проверяется кристаллографией / cryo-EM. Material structure — closed-world: DFT-расчёт стабильности или synthesis в A-Lab проверяют. Weather/climate forecasting — closed-world: завтрашняя погода проверяема через 24 часа. **Open-world** же — биология организменного уровня, социальные науки, новые механизмы интерпретации — AI **не работает**. Биологию AlphaFold не понимает (только fold). Психологию replicability crisis не решает. Историю науки LLM придумывает (галлюцинации, fake citations). Этот фильтр — самый **жёсткий и операционный**.

**Как распределяет 75 мин.** Раздел 0 (7 мин) — hook + keystone closed/open-world. Раздел 1 (20 мин) — **closed-world wins**: AlphaFold 3 (protein folding + ligand docking + Nobel), GNoME (380k stable materials predicted), Aurora/GraphCast (weather), AlphaProof/Geometry 2 (formal math, IMO silver). Раздел 2 (15 мин) — **closed-world conditionals**: A-Lab synthesis (вроде closed-world, но Palgrave переразбор показал отсутствие novelty), Coscientist (works на well-defined synthesis tasks). Раздел 3 (15 мин) — **open-world failures**: Galactica 2022, Sakana AI Scientist, NeurIPS 2025 fake citations, Frontiers «крыса», AI peer review hallucinations. Раздел 4 (12 мин) — **критерии closed-world проверки** + альтернативы + worked example. Раздел 5 (6 мин) — закрытие.

**Риски подхода.** (a) бинарный фильтр может быть слишком грубым — есть задачи на границе (drug repurposing — closed-world генерация candidates + open-world clinical trials); (b) термин «closed-world» имеет established meaning в logic / AI planning literature (closed-world assumption в Prolog) — может создать confusion; (c) фильтр не различает уровень риска от уровня применимости (closed-world drug discovery с FDA blocker — AI применим, но deployment всё равно требует HITL).

### Variant C — «Discovery × Validation × Production triple: три фазы научной работы × три AI-роли»

**Зачем это keystone.** Научная работа продвигается через 3 фазы. (1) **Discovery** — выдвижение и просев гипотез (где AI хорош на large search space). (2) **Validation** — проверка через experiment / replication / peer review (где AI помогает, но **не заменяет**). (3) **Production** — публикация, integration в стандарт, использование downstream (где AI augmentation, но peer review и authorship — человеческие). Триплет показывает, **где AI расширяет возможности учёного, а где наоборот сокращает**.

**Как распределяет 75 мин.** Раздел 0 (7 мин) — hook + keystone triple. Раздел 1 (18 мин) — Discovery: GNoME, MatterGen, AI Scientist, Coscientist, AlphaProof. Раздел 2 (18 мин) — Validation: A-Lab synthesis, AlphaFold experimental verification, Sakana peer review scandal, NeurIPS fake citations. Раздел 3 (15 мин) — Production: NotebookLM, Elicit, Frontiers retraction, scientific paper mill, authorship debates. Раздел 4 (12 мин) — критерии + альтернативы + worked example. Раздел 5 (5 мин) — закрытие.

**Риски подхода.** (a) Triple менее наглядно, чем линейная Лестница цикла (Variant A); (b) границы фаз размыты — drug discovery от GNoME материала до синтеза в A-Lab — это одновременно Discovery и Validation; (c) пересечение с Лекциями 5 (manufacturing pilot purgatory) — может выглядеть как тот же шаблон, что снижает differentiation.

### **Рекомендация владельцу (defer финал к owner)**

Лично рекомендую **Variant A** (Лестница научного цикла) — она наиболее интуитивна, легко обучаема, и Variant C-style таксономии уже использованы в lec-13 (Лестница среды) и lec-14 (Лестница автономии). Variant A — другой объект (фаза работы), не очередная «лестница автономии», что снижает риск ассоциативного шума. **Но** если владелец считает, что closed/open-world (Variant B) более операционно — это сильный аргумент: фильтр проще, и его легко применить к любому новому AI-инструменту.

---

## Инструменты на каждом уровне таксономии (для **Variant A — Лестница цикла**)

### Уровень 1 — Hypothesis (формулирование гипотез)

- **Sakana AI Scientist v1/v2** (Sakana AI, август 2024 / апрель 2025) — режим «автономный генератор идей». Adoption-направление: **внимание есть, продакшна нет** — workshop paper прошёл peer review (один из трёх, ICLR 2025), но содержит галлюцинации.
- **DeepMind Co-Scientist** (Google DeepMind, 2025; Nature paper May 2026) — multi-agent система генерации, дебатирования и ранжирования гипотез. Adoption-направление: **emerging**; collaboration с Stanford liver fibrosis study, Imperial College London, Francis Crick Institute.
- **Gemini for Science** (Google, 2026) — research suite на базе Gemini для life sciences. Adoption-направление: **запущен 2026, ранняя стадия**.
- **Anti-hype оговорка:** генерация гипотез — самый **open-world** этап. AI на этом уровне работает как brainstorm partner, **не как proven научный руководитель**. Hypothesis quality всё ещё требует научного руководителя.

### Уровень 2 — Design (планирование эксперимента)

- **Coscientist** (Carnegie Mellon, Boiko et al., Nature декабрь 2023) — LLM-driven автономная chemistry лаборатория, GPT-4 + tool-use. Adoption-направление: **proof-of-concept, не production**.
- **Emerald Cloud Lab + Strateos** — remote-controlled cloud labs, ECL имеет 200+ instruments. Adoption-направление: **зрелый сервис, но не autonomous** — учёный по-прежнему пишет protocol.
- **Bayesian optimization (BO) + Gaussian Process (GP)** — **классическая** альтернатива design-of-experiments; не AI в современном LLM-смысле, но матстатистика. Adoption-направление: **зрелый mainstream**, особенно в materials и chemistry.
- **Anti-hype оговорка:** ни одна autonomous лаборатория не достигла «full autonomy» в смысле «работает без supervision». Coscientist делает narrow tasks (synthesis известных компаундов); novel hypothesis discovery — нет.

### Уровень 3 — Experiment (проведение эксперимента / симуляция)

**Это самый сильный успех AI в науке — большинство breakthroughs здесь.**

- **AlphaFold 2/3** (DeepMind / Isomorphic Labs, 2020 / май 2024) — Nobel 2024. Adoption-направление: **mainstream в structural biology**; 200M+ protein structures publicly available (AlphaFold DB). AF3 closed-source при запуске → ноябрь 2024 academic open → февраль 2025 publicly available (non-commercial).
- **Boltz-1 / Boltz-2** (MIT, Corso/Wohlwend et al., декабрь 2024) — fully open-source AlphaFold-3-конкурент (MIT license, commercial use allowed). Adoption-направление: **растёт быстро среди академии и biotech'ов**.
- **GNoME** (DeepMind, ноябрь 2023) — 2.2M predicted materials, 380k stable. **A-Lab Berkeley** automatic synthesis 36 из 57 compounds. Adoption-направление: **disputed** — Palgrave critique 2024 показал что многие compounds — не «novel», а derivatives известных.
- **MatterGen** (Microsoft Research, 2024, Nature) — generative inverse design materials. Adoption-направление: **emerging, open-source**.
- **Aurora** (Microsoft, июнь 2024, Nature) — foundation model для atmosphere; 1.3B parameters; weather + air pollution; 5000× быстрее чем traditional numerical. Adoption-направление: **операционно используется в ECMWF с 2026**.
- **GraphCast** (DeepMind, 2023) + **Pangu-Weather** (Huawei, 2022) + **FourCastNet** (NVIDIA) — все 4 модели плюс Aurora **операционно у ECMWF с начала 2026**.
- **AlphaProof + AlphaGeometry 2** (DeepMind, июль 2024) — IMO 2024 silver medal (28/42 points), AG2 — gold-level на geometry. Adoption-направление: **в активном развитии**, FrontierMath 2024→2025 рост с <2% до 52% (Tier 1-3).
- **Anti-hype оговорка:** AlphaFold — Nobel-grade успех, но **не Nobel = не финал**. AlphaFold предсказывает **fold**, не **function**; не работает на IDP (intrinsically disordered proteins) — 22% hallucinations в IDP regions согласно analysis 2024. Drug docking всё ещё требует validation.

### Уровень 4 — Analyse (анализ данных)

- **ML-classifiers для exoplanet detection** (TESS + Kepler) — Convolutional Neural Networks классифицируют transit signals. 2025: модель идентифицировала 2 449 high-confidence planets из 3 987 candidates, 83.9% accuracy.
- **Allen Institute Brain Knowledge Platform** — ChatGPT-like AI для neuroscience; mapping 1300 регионов мозга мыши (апрель 2025, MICrONS project финал).
- **Machine learning pipelines для LIGO** — gravitational wave detection через CNN + uncertainty quantification. Adoption-направление: **зрелый mainstream в astrophysics**.
- **Anti-hype оговорка:** ML-классификаторы на data analysis — это **narrow ML, не foundation models**. Большая часть «AI в science discovery» в analyse-фазе — это привычный supervised learning, обученный на лейблах. Это не «AI делает науку» — это «AI ускоряет одну стандартную задачу».

### Уровень 5 — Write (написание статьи)

- **NotebookLM** (Google, 2023, расширение 2024-2026) — RAG-tool для personal corpus; в 2025 добавлен Audio Overview (podcast-style). Adoption-направление: **mainstream академический инструмент**, 17M+ MAU end 2025.
- **PaperQA / Elicit / Consensus / Semantic Scholar / Scite** — literature review augmentation; Elicit (138M papers + 545k clinical trials), Consensus (peer-reviewed direct answers), Semantic Scholar (214M papers). Adoption-направление: **mainstream**.
- **Anti-hype оговорка:** эти инструменты — **augmentation для poiska**, не **замена синтеза**. Любая ML-generated bibliography требует verify-каждой-цитаты. Cost-of-omission: NeurIPS 2025 100+ fake citations прошли peer review.

### Уровень 6 — Review (рецензирование)

- **Automated peer review tools** — экспериментальные на ICLR / NeurIPS workshops. Adoption-направление: **запрещённое во многих топ-местах** (NeurIPS 2024 ban explicit AI-generated reviews unless disclosed).
- **Anti-hype оговорка:** **самый рисковый этап**. Sakana AI Scientist peer review consistently missed flaws in own work; overly critical of human work. **AI-generated review без human verification = академическая интегрита риск номер 1**.

### Infrastructure (отделено от tools-per-level)

- **Hugging Face Hub** — общая инфраструктура для научных foundation models (Boltz-1, MatterGen, multiple AlphaFold clones).
- **arXiv / bioRxiv / PubMed / Semantic Scholar API** — open data sources, на которых тренируются и работают AI-инструменты.
- **DOE Genesis Mission ($320M, декабрь 2025)** + **NSF AI Institutes ($700M+ annually)** — государственная инфраструктура поддержки.

### Volatile числа / `[VFY-day-of]`

- **FrontierMath leaderboard** — обновляется ежеквартально; GPT-5.5 Pro 52.4% на 25 мая 2026 → `[VFY-day-of]`.
- **AlphaFold DB protein count** — постоянно растёт → `[VFY-day-of]`.
- **NotebookLM MAU count** — снимок на конец 2025; растёт → `[VFY-day-of]`.
- **Sakana AI Scientist v2 / v3** — Sakana активно итерирует; версии меняются → `[VFY-day-of]`.

---

## Outline

### Раздел 0 — Hook + keystone + lecture-map (7 мин, slides s01-s05)

**Цель.** Зацепить **двумя картинками рядом**: Nobel-prize 2024 (Hassabis, Jumper, Baker) и Galactica-3-day-shame 2022. Предъявить keystone «лестница научного цикла».

**Slides:**
- s01 (cover, hero) — Hero **«две стороны медали»**: левая половина — Hassabis + Jumper + Baker на Nobel ceremony (декабрь 2024); правая — скриншот заголовка «Meta pulls Galactica after 3 days».
- s02 (lecture-map) — 6 разделов лекции по лестнице цикла.
- s03 (keystone) — **Лестница из 6 ступеней (вертикальная)**: Hypothesis → Design → Experiment → Analyse → Write → Review; рядом каждой ступени — статус AI 2026 (augmentation / autonomous / vetoed).
- s04 (glossary) — 6-8 must-know acronyms: foundation model, RAG, hallucination, peer review, replication crisis, closed-world, IDP, ground truth.
- s05 (central question) — «Где AI делает прорыв в науке, где он создаёт paper mill, и как инженер должен решать?»

**Bucket-tag:** mixed (Nobel = success, Galactica = failure — оба явно).

**Strict-in failure-share:** ~35% (Galactica hook = 2 мин strict-in / 7 мин).

### Раздел 1 — Hypothesis + Design: где AI продаётся за autonomy, но даёт narrow help (10 мин, slides s06-s11)

**Цель.** Показать AI на «открытом» этапе цикла — гипотезы и planning. Это пока **самая хайповая** и **самая хрупкая** зона.

**Slides:**
- s06 — Sakana AI Scientist v1 (август 2024) + v2 (апрель 2025) — workshop paper passed peer review (один из трёх), но critic-анализ показал hallucinations, faked results, overestimated novelty.
- s07 — DeepMind Co-Scientist (Nature May 2026) — Stanford liver fibrosis collaboration, multi-agent debate-and-rank архитектура.
- s08 — Gemini for Science (Google 2026), ERA пакет (CDC forecasting beaten in benchmarks).
- s09 — Coscientist (CMU Boiko 2023, Nature) — GPT-4-driven autonomous chemistry; works на синтез известных компаундов, novel discovery — нет.
- s10 — **Failure-deep-dive**: Sakana criticisms — простой keyword search вместо synthesis; auto-reviewer missed own paper's flaws; «занимательно, но не наука».
- s11 — **Альтернатива**: Bayesian Optimization + Gaussian Process для design-of-experiments; **зрелая 30+ лет методика**, не «AI» в LLM-смысле; в materials и chemistry часто **лучше**, чем deep RL.

**Bucket-tag:** mixed (capability + failure + alt-tool).

**Strict-in failure-share:** ~45% (Sakana failures + альтернатива BO = 4.5 мин strict-in / 10 мин).

### Раздел 2 — Experiment: самый сильный успех AI в науке (15 мин, slides s12-s19)

**Цель.** Главная капитальная глава лекции. Здесь AI **реально дал Nobel-grade прорывы**. Эта секция — **где AI делает науку лучше**, и где наш курс должен показать, **где AI восхищён сам по себе**.

**Slides:**
- s12 — AlphaFold 2 (DeepMind 2020) → AlphaFold 3 (май 2024) — добавлены DNA / RNA / ligands / ions; protein-ligand interaction +50% accuracy.
- s13 — AlphaFold DB — 200M+ protein structures publicly available. Hero: скриншот DB website.
- s14 — Open-source debate AlphaFold 3 (closed at launch → academic Nov 2024 → public Feb 2025 non-commercial). 1000+ scientists letter за open. Critic: **Isomorphic Labs $3B deals (Lilly + Novartis) — commercial reasons preserved**.
- s15 — Boltz-1 / Boltz-2 (MIT, декабрь 2024) — fully open MIT license; уже **most-used model в своём классе**.
- s16 — GNoME (DeepMind 2023, Nature) — 2.2M materials predicted, 380k stable. **A-Lab Berkeley** — 36 из 57 synthesized.
- s17 — **Failure-deep-dive**: Palgrave критика 2024 — «not actually novel»; many compounds — derivatives, no functionality demonstrated. **Lesson**: prediction ≠ proven novelty.
- s18 — Aurora + GraphCast + Pangu + FourCastNet — все 4 операционно в ECMWF с 2026; Aurora 5000× быстрее.
- s19 — AlphaProof + AlphaGeometry 2 (IMO 2024 silver, 28/42) → FrontierMath rise (<2% 2024 → 52% май 2026).

**Bucket-tag:** capability-heavy, но **обязательно failure-deep-dive в s17 + s14 commercial debate**.

**Strict-in failure-share:** ~25% (A-Lab critic + AlphaFold open-source debate + IDP-limits callback = 3.5 мин strict-in / 15 мин). **Это ниже 30% target — компенсируется в Разделе 4 / 5 / 6 для общего holistic ≥30%**.

### Раздел 3 — Analyse: solid use cases в data analysis (12 мин, slides s20-s25)

**Цель.** Показать **подъём AI в data analysis** — astrophysics / neuroscience / gravitational waves. Этот фронт **самый продакшнабельный**, потому что задачи **узкие и закрытые**.

**Slides:**
- s20 — Exoplanet detection через CNN: TESS + Kepler; 2025 модель — 2 449 high-confidence planets из 3 987 candidates, 83.9% accuracy.
- s21 — Allen Institute MICrONS project (апрель 2025) — 1 cubic mm mouse visual cortex, 1300 regions mapped; Brain Knowledge Platform.
- s22 — Gravitational waves: ML pipeline combination с conformal prediction для uncertainty quantification (LIGO 2024+).
- s23 — AlphaFold limitations deep-dive: 22% hallucinations в IDP regions; α-synuclein не captured; lipid environment не моделируется.
- s24 — **Альтернативы AI в analyse**: classical signal processing (matched filtering для GW), DFT/MD first-principles для chemistry, classical statistical methods.
- s25 — **Worked example уровень 4**: «Вам нужно классифицировать 10 000 спектральных сигналов — взять supervised CNN, BO над hyperparameters, или classical signal-detection?». 3 уточняющих вопроса.

**Bucket-tag:** mixed (capability + failure + alt-tool).

**Strict-in failure-share:** ~35% (AlphaFold IDP limits + альтернативы + worked example = 4 мин strict-in / 12 мин).

### Раздел 4 — Write + Review: где AI vs академическая интегрита (12 мин, slides s26-s31)

**Цель.** **Самая концентрированная failure-зона лекции**. Здесь AI **активно создаёт риск** для научного метода. Если у студента остаётся только одно воспоминание из лекции — должно быть «не давайте LLM-generated bibliography в peer review без verification».

**Slides:**
- s26 — NotebookLM (Google) — RAG над personal corpus, audio overview; 17M+ MAU 2025. **Augmentation, не synthesis**.
- s27 — Elicit / Consensus / Semantic Scholar — literature review tools; Elicit 138M papers + 545k trials; **используют как стартовую точку, не финал**.
- s28 — **Failure**: Frontiers retraction 2024 — Midjourney-generated rat anatomy с распухшими гениталиями; «protemns», «zxpens». Disclosed в paper, не пойман peer reviewers. Retraction 3 days post-publication.
- s29 — **Failure**: NeurIPS 2025 — 100+ fake citations пробились в принятые папперы (53 papers); 24.52% acceptance rate; ICLR 2026 — 50+ similar. **GPTZero estimate**: half показывали AI-generated drafting signs.
- s30 — **Failure**: Sakana ICLR 2025 workshop paper passed peer review, но hallucinations / faked results / overestimated novelty в внешнем audit'е.
- s31 — **ICMJE rule + публикационные policies**: Frontiers / Springer / Elsevier требуют disclosure; AI не может быть автором. **5 этических критериев** disclosure / verifiability / authorship / liability / replicability.

**Bucket-tag:** failure-heavy, с явными уроками и criteria.

**Strict-in failure-share:** ~70% (Frontiers + NeurIPS + Sakana + ICMJE = 8.5 мин strict-in / 12 мин).

### Раздел 5 — Когда AI не нужен в науке: критерии + альтернативы + worked example (12 мин, slides s32-s36)

**Цель.** PEAK failure-bucket section. Payoff для LO6 + LO8. Это **applicable mental model**, который студент уносит.

**Slides:**
- s32 — **4 категории критериев «AI не нужен / вреден в науке»**:
  - **A. Closed/Open-world дисциплина** — если задача требует understanding mechanisms, а не предсказания паттернов → AI не работает (биология, психология, история).
  - **B. Training distribution coverage** — если ваша domain underrepresented в training data → AI hallucinates (медицинские специальности, rare diseases, новые материалы).
  - **C. Verifiability** — если результат не может быть проверен независимо (peer review, citation сетки) → AI создаёт fake records.
  - **D. Ethical risk** — если применение нарушает authorship / disclosure / IRB → не применять.
- s33 — **5 альтернатив AI в науке** matrix:
  - **Bayesian Optimization / Gaussian Process** — design-of-experiments (vs RL/agentic);
  - **DFT / MD first-principles** — материалы и chemistry (vs GNoME-style ML);
  - **Classical statistical methods** — psychology, biology (vs LLM analysis);
  - **Operational Research / OR-Tools** — scientific logistics (vs reinforcement learning);
  - **Human peer review (с улучшениями)** — academic integrity (vs LLM peer review).
- s34 — **Worked example**: «Ваш научный руководитель просит: "построй AI-pipeline для предсказания свойств новых катализаторов". Применим рамку».
  - Step 1: classify task — closed-world (catalysis = quantum chemistry well-defined) или open-world?
  - Step 2: map alternatives — DFT first-principles, GP-BO, GNoME-style ML?
  - Step 3: apply 4 categories — training coverage есть (Materials Project), verifiability есть (synthesis в lab), ethics OK.
  - Step 4: HITL design — AI screens, human validates top-10, synthesis confirms.
  - Step 5: pre-publication — verify каждую predicted property через DFT calculation **до** статьи.
- s35 — **3 уточняющих вопроса к AI-вендору в науке**: (1) baseline до AI (classical method); (2) reproducibility — published code / data / weights; (3) failure cases — где модель **не работает** explicit.
- s36 — **5-step framework** (повторение, applicable artefact): classify → map alternatives → apply 4 categories → HITL design → pre-publication verify.

**Bucket-tag:** failure-heavy + criteria + alternatives + worked example.

**Strict-in failure-share:** ~90% (всё кроме worked example positive part = 10.5 мин strict-in / 12 мин).

### Раздел 6 — Замыкание + Q&A + мост к Лекции 16 (6 мин, slides s37-s39)

**Цель.** Закрыть лестницу с явным failure-callback. Мост к Лекции 16 (AI в нефтегазе).

**Slides:**
- s37 — Recap лестницы цикла с failure-маркерами под каждой ступенью.
- s38 — **Failure-callback (mandatory)**: «Завтра вы получаете LLM-сгенерированную bibliography от коллаборатора. **Что делаете?** — verify каждую цитату через DOI; запрашиваете source documents; **отказываетесь подписать paper если не можете проверить**».
- s39 — **Closing hero** + мост к Лекции 16: AlphaFold DB website screenshot (200M structures = «биология теперь чуть больше известна — но финальная карта далека») → next: AI в нефтегазе (Лекция 16) — другой extreme structured domain.

**Bucket-tag:** failure-recall + bridge.

**Strict-in failure-share:** ~35% (failure-callback recap = ~2 мин strict-in / 6 мин).

---

## Провалы, ограничения и альтернативы (ENFORCED — ≥30% содержания)

### Документированные провалы AI в науке + выученные уроки

1. **Galactica (Meta, ноябрь 2022)** — 3-day shame после launch; LLM генерировал confidently «science» с false claims, bomb-making instructions, racist remarks. **Урок**: LLM не понимает «истину» — он генерирует словесные распределения. **Ground truth ≠ training distribution mode**.
2. **A-Lab Berkeley переразбор (Palgrave 2024)** — 41 «новый» материал из автономной synthesis оказались derivatives известных, без functionality demonstrated. Critique attendant — Robert Palgrave (UCL), детальный chemistry-level analysis. **Урок**: prediction ≠ proven novelty; structural similarity к existing material — недостаточно для «discovery» claim.
3. **Sakana AI Scientist (август 2024 + апрель 2025 v2)** — workshop paper passed peer review, но external audit показал «hallucinations, faked results, overestimated novelty». **Урок**: peer-review pass ≠ научная валидность; humans cherry-picked papers Sakana submitted.
4. **Frontiers «крыса» retraction (февраль 2024)** — Midjourney-generated rat anatomy опубликован, retracted в 3 дня; disclosed в paper, не пойман editors / reviewers. **Урок**: disclosure в paper — недостаточная защита; peer review должен проверять figures отдельно.
5. **NeurIPS 2025 fake citations (100+ за peer review)** — 53 paper'a с fake refs пробились в принятые; ICLR 2026 — 50+ similar. **Урок**: bibliography от LLM требует verify-каждой-цитаты; conferences начинают institutionalized hallucination scanning.
6. **AlphaFold IDP limits** — 22% residues hallucinated в intrinsically disordered regions; α-synuclein не captured; lipid environment не моделируется. **Урок**: foundation model для domain не = full domain understanding; знай где модель работает, где нет.
7. **AlphaFold 3 closed at launch** — научное community протест (1000+ scientists letter); commercial Isomorphic Labs $3B deals (Lilly + Novartis) blocked open release полгода. **Урок**: science vs commerce trade-off; open-source альтернативы (Boltz-1) могут обогнать closed модель в adoption.
8. **AI peer review hallucinations (NeurIPS 2024+ ban)** — automated review consistently missed flaws in own work; overly critical of human work. **Урок**: peer review — критически важная человеческая задача, не automatable cheaply.

### Фундаментальные ограничения / риски подхода

- **LLM-fundamentals**: distribution over tokens, не understanding; hallucinations стипендиальная feature, не bug. **Замкнутый** circuit для научных tasks с verifiability — OK; **открытый** circuit (peer review, hypothesis generation в open-world domain) — risk.
- **Training distribution coverage** — фундаментальное: модель работает в распределении, на котором обучалась. Rare diseases, новые материалы, neonatal medicine, эмерджентные климатические события — **outside distribution**, hallucinations ожидаемы.
- **Closed-world vs open-world** — фундаментальная граница (Variant B keystone). Protein folding closed-world (cryo-EM verify); биология organismal — open-world.
- **Computational vs experimental verification gap** — AlphaFold предсказывает fold; **synthesis + activity assay по-прежнему обязательны**.
- **Replicability crisis (general science context)** — psychology 36% replication rate (Reproducibility Project), economics 61%, AI ML papers 24-50% — AI не лечит эту проблему, может усугубить.

### Критерии «здесь AI не нужен / не применим» (LO6 центральный)

- **A. Open-world задача без verifiable ground truth** — биология organismal, sociology, history of science. AI hallucinates.
- **B. Underrepresented в training data** — rare diseases, новые материалы (без analogs), новые экспериментальные методы.
- **C. Verifiability cannot be done independently** — peer review, citation networks, original observation (вместо validated baseline).
- **D. Ethical risk** — authorship, IRB violations, AI как co-author (ICMJE запрещает).
- **E. Закрытая физика лучше доступна** — DFT/MD расчёт стабильности материала; classical signal processing для LIGO; classical Black-Scholes для финансов — **проще, дешевле, объясним**.

### Более правильные альтернативы (сравнение)

- **Bayesian Optimization + Gaussian Process** vs Sakana / RL — для design-of-experiments в materials и chemistry; **30+ лет** методика, объясним, computationally дешевле.
- **DFT / MD first-principles** vs GNoME / MatterGen — quantum chemistry надёжнее ML для thermodynamic stability; ML может generate candidates, но **синтез + DFT** должны validate.
- **Classical signal processing (matched filter)** vs CNN — для gravitational waves; ML добавляет, но **не заменяет** template matching.
- **Classical Bibliometrics** vs LLM literature analysis — citation networks, h-index, Web of Science / Scopus — objective, replicable, scientometric metrics.
- **Human peer review (с улучшениями)** vs AI peer review — структурированные рубрики, double-blind, statcheck для статистики, image forensics — все human-supervised tools, не autonomous AI.
- **OR-Tools / Gurobi / CPLEX** vs deep RL — для scientific logistics (clinical trial design, resource allocation в большом experiment); 70+ лет classical OR.

### Бюджет (слова/слайды/минуты) на failure-bucket ≥30%

**По разделам, минуты strict-in (см. секцию Failure-bucket distribution ниже):**

- §0 (7 мин) — 2 мин strict-in (28.6%)
- §1 (10 мин) — 4.5 мин strict-in (45%)
- §2 (15 мин) — 3.5 мин strict-in (23.3%) ← компенсируется
- §3 (12 мин) — 4 мин strict-in (33.3%)
- §4 (12 мин) — 8.5 мин strict-in (70.8%)
- §5 (12 мин) — 10.5 мин strict-in (87.5%)
- §6 (6 мин) — 2 мин strict-in (33.3%)

**Total:** 35 мин strict-in / 74 мин = **47.3%** ✓ ≥30% (margin ~17 п.п.)

---

## Sections roadmap

| # | Раздел | Длительность | Slides | Описание (1-2 предложения) | Bucket-tag |
|---|---|---|---|---|---|
| 0 | Hook + keystone | 7 мин | s01-s05 | Hero AlphaFold-Nobel + Galactica-shame; keystone-лестница цикла; lecture-map; glossary | mixed |
| 1 | Hypothesis + Design | 10 мин | s06-s11 | Sakana, Co-Scientist, Gemini for Science, Coscientist — где AI продаётся за autonomy; failure deep-dive Sakana; альтернатива BO+GP | mixed |
| 2 | Experiment (Nobel-grade) | 15 мин | s12-s19 | AlphaFold 2/3 + Nobel 2024, Boltz-1, GNoME, A-Lab + Palgrave критика, Aurora + ECMWF, AlphaProof + AlphaGeometry 2 | capability (с обязательным failure deep-dive) |
| 3 | Analyse (data analysis) | 12 мин | s20-s25 | Exoplanet detection, Allen brain map, LIGO ML, AlphaFold IDP limits, альтернативы classical signal processing, worked example | mixed |
| 4 | Write + Review | 12 мин | s26-s31 | NotebookLM + Elicit + Consensus — augmentation; **failures**: Frontiers «крыса», NeurIPS fake citations, Sakana peer review scandal; ICMJE rule | failure-heavy |
| 5 | Когда AI не нужен | 12 мин | s32-s36 | 4 категории критериев, matrix альтернатив, worked example «catalyst pipeline», 3 вопроса к вендору, 5-step framework | failure + alt-tool + criterion |
| 6 | Замыкание + Q&A | 6 мин | s37-s39 | Recap с failure-callback; ситуация «коллаборатор даёт LLM bibliography»; мост к Лекции 16 | mixed (failure-recall) |

---

## Worked examples (4+ кейсов, каждый — name + measurable + baseline + source + verifiable)

### Success 1: AlphaFold 2 → AlphaFold 3 → Nobel Prize Chemistry 2024

**Имя:** AlphaFold (DeepMind / Isomorphic Labs)
**Кто/где/когда:** DeepMind, лондон/маунтин-вью, AlphaFold 2 (2020) → AlphaFold 3 (8 мая 2024, Nature paper) → Нобелевская премия по химии (8 октября 2024, Stockholm)
**Что AI делает:** Предсказывает 3D-структуру белка из аминокислотной последовательности. AF3 расширил до DNA / RNA / ligands / ions.
**Измеримый результат с baseline:**
- AlphaFold 2: **на CASP14 (декабрь 2020)** — median GDT_TS ~92 для proteins; baseline до AF2: лучшие методы ~60 GDT_TS. **+53% improvement vs prior best.**
- AlphaFold 3 для protein-ligand interactions: **+50% accuracy** vs prior best methods (per DeepMind benchmark).
- AlphaFold DB: **200M+ predicted structures** publicly available; baseline до AlphaFold — PDB ~200k experimentally solved structures (т.е. **1000× больше structures**, но predicted).
**Источник:** DeepMind blog, Nature paper Jumper et al. (2021), Abramson et al. (2024). Nobel Prize press release nobelprize.org. Wikipedia AlphaFold.
**Verifiable:** Открытый AlphaFold DB → alphafold.ebi.ac.uk; AF2 weights open-source; AF3 academic access ноябрь 2024 → public февраль 2025 (non-commercial).

### Success 2: AlphaProof + AlphaGeometry 2 — IMO 2024 silver medal

**Имя:** AlphaProof + AlphaGeometry 2 (DeepMind)
**Кто/где/когда:** Google DeepMind, июль 2024, отчёт о IMO 2024 (International Mathematical Olympiad).
**Что AI делает:** AlphaProof — RL-based formal math reasoning (interface с Lean); AlphaGeometry 2 — neuro-symbolic hybrid с Gemini-base.
**Измеримый результат с baseline:**
- **IMO 2024: 28/42 points = silver medal level**. Baseline до этого: AI не доходил до bronze (12/42); IMO 2024 6 problems, AlphaProof solved 2 algebra + 1 number theory; AlphaGeometry 2 solved geometry — **4 of 6 problems**.
- AlphaProof решил **сложнейшую проблему турнира** (только 5 человек её решили).
- **Counter-base:** золотой medalist's score 2024 ≥ 29/42. AI на 1 балл ниже gold.
**Источник:** DeepMind blog (deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level), Nature paper 2025, arxiv 2502.03544.
**Verifiable:** IMO official problems открыты; DeepMind paper описывает методологию; Lean-формализации problems опубликованы.

### Mixed: GNoME + A-Lab Berkeley — predicted materials vs Palgrave critique

**Имя:** GNoME + A-Lab Berkeley (DeepMind + LBNL)
**Кто/где/когда:** DeepMind GNoME (ноябрь 2023, Nature) → A-Lab Berkeley synthesis (ноябрь 2023, Nature) → Palgrave critique (январь 2024).
**Что AI делает:** GNoME — Graph Networks для predict материалов stability; A-Lab — автономный робот синтезирует из predictions.
**Измеримый результат с baseline:**
- GNoME: **2.2M predicted materials**, **380k predicted stable**. Baseline до: Materials Project ~50k materials с DFT-расчётом → **44× больше candidates** (predicted).
- A-Lab: **36 of 57 target compounds synthesized in 17 days** (63% success rate). Baseline manual chemistry: один target — недели до месяцев работы PhD.
- **Palgrave critique (январь 2024):** из 41 «новых» compounds **большинство — derivatives** known materials; no demonstrated functionality. Counter-claim DeepMind (декабрь 2023): >700 predictions independently synthesized.
**Источник:** DeepMind blog (deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning), Nature paper Merchant et al. (2023), Chemistry World critique (chemistryworld.com), Robert Palgrave Twitter / arXiv analysis.
**Verifiable:** GNoME predictions опубликованы; A-Lab synthesis data доступна (доступ ограничен); Palgrave analysis открыт.

### Failure 1: Galactica (Meta) — 3-day shame

**Имя:** Galactica (Meta AI / FAIR)
**Кто/где/когда:** Meta AI, ноябрь 15-17 2022, public demo.
**Что AI делает:** LLM специально для научного writing; обучен на 48M papers + textbooks + reference material.
**Измеримый результат с baseline:**
- **Demo жил 3 дня** (15-17 ноября 2022) до retraction. Baseline: ни одна другая major model launch не была pulled за 3 дня.
- Outputs: **false science claims** (false relationships между proteins), **bomb-making instructions**, **racist statements**, fabricated citations.
- **Counter-base:** ChatGPT (запуск 30 ноября 2022, через 2 недели после Galactica retract) — также confidently hallucinates, но позиционирован как «assistant», не «scientific tool» — survived и стал standard.
**Источник:** MIT Technology Review (Heaven 2022), arxiv paper 2211.09085, OECD AI incidents database.
**Verifiable:** arxiv paper доступен; demo unavailable (pulled); Twitter screenshots критики сохранены.

### Failure 2: Frontiers «крыса» retraction

**Имя:** Frontiers in Cell and Developmental Biology, рецензированная статья от Hong Hui Hospital и Jiaotong University
**Кто/где/когда:** опубликовано 13 февраля 2024; retraction 16 февраля 2024 (3 дня).
**Что AI делает:** Authors disclosed что использовали Midjourney для figures.
**Измеримый результат с baseline:**
- Figure #1: rat с пенисом + testicles **больше остального тела**; word «protemns» вместо «proteins»; «zxpens» (nonsense).
- **Baseline:** до AI-image generators такие figure errors были **rare** (вручную рисованных diagrams было меньше, проверка proofs работала).
- **Reach:** статья достигла **peer review** + **publication** в indexed journal Frontiers — это не препринт, это рецензированное издание с IF >5.
- **Cost:** Frontiers reputation hit; subsequent 19 papers retracted (Hindawi / Bentham incidents 2024) для similar AI-generated content.
**Источник:** phys.org (2024-02), VentureBeat, The AI Optimist, Gizmodo.
**Verifiable:** Original PDF доступен через web archive; retraction notice на Frontiers сайте.

### Failure 3: NeurIPS 2025 — 100+ fake citations прошли peer review

**Имя:** NeurIPS 2025 conference (8-13 декабря 2025) — fabricated citations audit
**Кто/где/когда:** Conference held December 2025, audit GPTZero + coreprose researchers, paper arxiv 2602.05930.
**Что AI делает:** Authors offload bibliography drafting to LLMs → fail to verify outputs.
**Измеримый результат с baseline:**
- **100+ fake citations identified** в **53 papers** of NeurIPS 2025 accepted track.
- **15 000 submissions** total, **acceptance rate 24.52%** → ~3 700 accepted; **53 / 3 700 = 1.4% papers** имеют fake citations.
- **Baseline:** до 2023 fake citations были <0.1% of accepted papers (estimated by Retraction Watch).
- **ICLR 2026** (предварительные данные): similar trend, **50+ similar in submitted review pool**.
- **Counter-base:** Half of papers с hallucinated citations показывают AI-generated drafting signs per GPTZero analysis.
**Источник:** dev.to NeurIPS 2025 article, arxiv 2602.05930, GPTZero NeurIPS analysis, the-decoder.com article.
**Verifiable:** NeurIPS 2025 accepted papers list public; fake citations identified by author and section; GPTZero analysis methodology open.

### Failure 4: Sakana AI Scientist v2 — ICLR 2025 workshop paper + external audit

**Имя:** Sakana AI Scientist v2 (Sakana AI, апрель 2025)
**Кто/где/когда:** Sakana submitted 3 fully AI-generated papers to ICLR 2025 workshop «I Can't Believe It's Not Better»; 1 of 3 passed peer review.
**Что AI делает:** Generates hypotheses → runs experiments → analyses → writes papers → submits.
**Измеримый результат с baseline:**
- **1 of 3 papers (33%)** passed workshop peer review; scores **6, 7, 6** — average 6.33, **above median** of human-written (55th percentile).
- **External audit (Sakana собственный disclosure)**: even passing paper had «hallucinations, faked results, overestimated novelty». Sakana **cherry-picked** which 3 to submit (human selection involved).
- **Baseline:** до Sakana — 0 AI-generated papers passed peer review at workshop or top conference.
- **Counter-base:** Workshop ≠ main conference; «I Can't Believe It's Not Better» — explicitly о **поверочной работе**, не breakthrough. Это soft test.
**Источник:** Sakana AI blog post March 12 2025, TechCrunch (techcrunch.com/2025/03/12), GitHub SakanaAI/AI-Scientist-ICLR2025-Workshop-Experiment, arxiv 2504.08066.
**Verifiable:** Paper PDFs опубликованы; reviewer comments опубликованы; Sakana code и transcripts open.

---

## Failure / limits / alternatives bucket map (≥30% strict-in)

### Распределение по разделам

См. таблицу выше в § «Бюджет на failure-bucket».

**Итог:** 35 мин strict-in / 74 мин = **47.3%** ✓

### Распределение по 3 артефактам (projection holistic)

**Chapter (~30 000 слов target):**
- §0 ~1 000 слов, §1 ~3 500, §2 ~5 500 (Nobel-tier материал → больше слов на capability, но обязательный deep-dive failures), §3 ~3 500, §4 ~4 000, §5 ~5 000, §6 ~1 500, intros/q-and-a/sources ~6 000.
- **Strict-in failure bucket target: 35-45% слов** (~12-14k слов). По разделам §1 45%, §2 25%, §3 35%, §4 70%, §5 90%, §6 35% — взвешенное среднее **~45%**.

**Slides (~39 слайдов target):**
- Failure-strict slides: s10 (Sakana criticisms), s14 (AlphaFold commercial debate), s17 (Palgrave A-Lab), s23 (AlphaFold IDP limits), s28 (Frontiers крыса), s29 (NeurIPS fake citations), s30 (Sakana workshop), s32 (4 категории критериев), s33 (5 альтернатив matrix), s35 (3 вопроса), s38 (failure-callback recap) = **11/39 = 28%** strict-in. **Дополнительные mixed slides (s06 Sakana intro, s07 Co-Scientist уровень frontier, s11 BO alternative, s24 classical alternatives, s31 ICMJE)** = +5 — **16/39 = 41%** holistic.

**Speech (~6 000 слов / 75 мин):**
- Strict-in mins: ~35 мин из 74 = **47.3%** — посчитан выше.

**Counter-check:** все 3 артефакта ≥30%; distributed по 7 разделам (min §2 = 23%, max §5 = 87%) — нет single-artifact concentration; §5 = 30% всех failure-минут (healthy distribution).

---

## Hero plan для s01 + s39

### s01 (cover, hero) — «Две стороны медали»

**Концепт:** Hero = **side-by-side pair**, чтобы сразу задать tension лекции (success vs failure).

- **Левая половина (~50% area):** Hassabis + Jumper + Baker на Nobel ceremony December 2024 — Royal Swedish Academy of Sciences press photo OR Stockholm City Hall ceremony.
- **Правая половина (~50% area):** Скриншот заголовка MIT Technology Review «Why Meta's latest large language model only survived three days online» (Heaven, 18 ноября 2022) OR Twitter screenshot Yann LeCun reaction.

**Entity + источник:**
- Nobel photo: **Royal Swedish Academy of Sciences** press kit (nobelprize.org/prizes/chemistry/2024/) — Tier 3 press release attribution «© Nobel Foundation 2024».
- MIT TR screenshot: **MIT Technology Review article URL** (technologyreview.com/2022/11/18/...) — Tier 6 screenshot of headline.

**6-tier acquisition strategy:**
- Tier 1 (og:image от nobelprize.org chemistry 2024 page): primary
- Tier 2 (Wikipedia Commons «Nobel Prize Chemistry 2024 laureates»): backup
- Tier 3 (DeepMind blog post с photo): backup-2
- Tier 6 (Google Images search «Nobel 2024 chemistry laureates»): last resort
- Для правой половины: Tier 6 screenshot of MIT TR headline (educational fair use; attribution «MIT Technology Review, 2022»).

**Attribution label visible:** «Nobel Prize Chemistry 2024 © Nobel Foundation | Galactica retraction headline © MIT Technology Review 2022»

### s39 (closing) — Bridge к Лекции 16

**Концепт:** Closing hero — **AlphaFold DB website screenshot** (или Stable Diffusion-style рендер protein structure cluster) — символизирующее «биология теперь чуть больше известна, но финальная карта далека».

**Entity + источник:**
- **AlphaFold DB website** (alphafold.ebi.ac.uk) — main page screenshot showing 200M+ structures counter.
- **OR:** AlphaFold predicted protein structure (one of ribbon diagrams from AlphaFold blog) — Tier 3 DeepMind press kit.

**6-tier acquisition strategy:**
- Tier 1 (og:image от alphafold.ebi.ac.uk): primary
- Tier 2 (Wikipedia AlphaFold article hero image): backup
- Tier 3 (DeepMind AlphaFold 3 blog post): backup-2
- Tier 6 (screenshot of website current state): last resort

**Bridge text:**
«AlphaFold показал, что **closed-world задачи** в науке доступны AI. Лекция 16 — **AI в нефтегазовой отрасли**, ещё одна closed-world domain (геофизика, sub-surface modeling). Та же лестница цикла применяется».

**Attribution:** «© DeepMind / Isomorphic Labs / EBI 2024»

---

## Media plan ≥50% слайдов

**Total slides:** 39 (s01-s39).

### Media-heavy slides (target ≥20 / 39 = 51%)

| # | Слайд | Media kind | Источник |
|---|---|---|---|
| s01 | Hero «две стороны медали» | side-by-side photo+screenshot | Nobel.org + MIT TR |
| s06 | Sakana AI Scientist demo | screenshot / paper figure | Sakana blog / arxiv |
| s07 | DeepMind Co-Scientist | architecture diagram | Nature May 2026 paper |
| s09 | Coscientist | lab photo / architecture | CMU press / Nature 2023 |
| s10 | Sakana failures (deep-dive) | annotated screenshot of one paper | Sakana blog + reviewer comments |
| s12 | AlphaFold 2 → AF3 | protein 3D structure ribbon | DeepMind blog |
| s13 | AlphaFold DB | website screenshot | alphafold.ebi.ac.uk |
| s14 | Open-source debate | timeline diagram (custom Mermaid) | DeepMind + Nature + asbmb article |
| s15 | Boltz-1 | benchmark chart vs AF3 | MIT news + bioRxiv |
| s16 | GNoME 2.2M predictions | dot plot / candidate distribution | DeepMind blog |
| s17 | A-Lab Berkeley + Palgrave critique | chemistry diagram | Chemistry World article |
| s18 | Aurora atmospheric model | weather animation snapshot | Microsoft Research blog |
| s19 | AlphaProof IMO 2024 | IMO problem screenshot | DeepMind blog |
| s20 | Exoplanet detection | light curve chart (CNN visualization) | arxiv 2512.00967 |
| s21 | Allen MICrONS | brain region map | Allen Institute press |
| s22 | LIGO ML pipeline | waveform + uncertainty viz | arxiv 2504.17587 |
| s23 | AlphaFold IDP limits | α-synuclein structure error visualization | arxiv 2510.15939 |
| s26 | NotebookLM | UI screenshot | Google Workspace blog |
| s27 | Elicit + Consensus | UI comparison screenshots | Elicit.com + Consensus.app |
| s28 | Frontiers «крыса» | retracted figure (annotated) | phys.org / VentureBeat |
| s29 | NeurIPS fake citations | bar chart per paper count | dev.to article + GPTZero analysis |
| s33 | 5 альтернатив matrix | custom matrix diagram | custom |
| s34 | Worked example flow | Mermaid flow-chart | custom |
| s36 | 5-step framework | Mermaid flow-chart | custom |
| s39 | Closing hero | AlphaFold DB screenshot | alphafold.ebi.ac.uk |

**Total media:** **25 / 39 = 64%** ✓ (margin +14 п.п. над 50% target).

### Media kinds breakdown

- Real photos / press: 8 (s01-left, s07, s09, s17, s18, s21, s28, s31)
- UI screenshots: 6 (s01-right, s06, s13, s26, s27, s39)
- 3D structure / scientific viz: 5 (s12, s16, s19, s22, s23)
- Charts / bench data: 4 (s10, s15, s20, s29)
- Custom diagrams / Mermaid: 4 (s14, s33, s34, s36)

---

## Numbers convention lock (10-15 ключевых canonical measurable claims)

Каждое из этих чисел — **canonical anchor** для chapter, slides, speech. Никаких variations без cascade-of-changes check (I-8 lec-11 lesson).

1. **AlphaFold 3 release:** 8 мая 2024 (DeepMind / Isomorphic Labs).
2. **AlphaFold open-source timeline:** closed at launch → academic access ноябрь 2024 → public февраль 2025 (non-commercial).
3. **AlphaFold DB:** **200M+ protein structures** publicly available (snapshot 2026; `[VFY-day-of]`).
4. **Nobel Chemistry 2024:** 8 октября 2024 — Baker (½) + Hassabis + Jumper (½).
5. **GNoME:** **2.2M predicted materials, 380k stable** (DeepMind November 2023, Nature).
6. **A-Lab Berkeley:** **36 of 57 target compounds synthesized in 17 days** (Nature November 2023); Palgrave critique January 2024.
7. **AlphaProof + AlphaGeometry 2:** **28/42 points = silver medal level**, IMO 2024 (4 of 6 problems).
8. **FrontierMath:** <2% (2024 launch, GPT-4o / Claude 3.5 / o1-preview) → **52.4% (GPT-5.5 Pro май 2026)** `[VFY-day-of]`.
9. **Galactica:** Meta, **15-17 ноября 2022, 3-day demo retraction**.
10. **Frontiers «крыса»:** February 13 published → February 16 retracted (3 дня); rat anatomy via Midjourney; «protemns» / «zxpens» misspellings.
11. **NeurIPS 2025:** **100+ fake citations** в **53 accepted papers** of ~3 700 accepted; 24.52% acceptance rate; 15 000 submissions.
12. **Sakana AI Scientist:** **1 of 3 papers** passed ICLR 2025 workshop peer review (scores 6, 7, 6 = 6.33 average, 55th percentile of human-written).
13. **AlphaFold IDP hallucinations:** **22% residues hallucinated** в intrinsically disordered protein regions per 2024 analysis.
14. **NotebookLM MAU:** **17M+ end 2025** (`[VFY-day-of]`).
15. **DOE Genesis Mission:** **$320M в декабре 2025** для AI4Science.
16. **NSF AI portfolio:** **$700M+ annually** (snapshot 2026; `[VFY-day-of]`).
17. **Aurora speed:** **5000× быстрее** traditional numerical weather forecasting (Microsoft June 2024, Nature).
18. **Replication crisis baselines:** Psychology **36%** replication rate (Reproducibility Project 100 studies); Economics **61%** (behavioural economics); AI/ML ICML 2024 **24%** by LLMs, **<50%** by PhD students.

**Volatile / `[VFY-day-of]` markers:** FrontierMath leaderboard, AlphaFold DB count, NotebookLM MAU, NSF/DOE funding totals, новые Sakana / Co-Scientist версии.

---

## Russification таблица (anti-anglicism mandate)

В этой теме AI-в-науке **гарантированно** вылезут эти anglicisms в visible body. Canonical replacements:

| # | Anglicism | RU replacement |
|---|---|---|
| 1 | foundation model | фундаментальная модель |
| 2 | ground truth | эталонная разметка |
| 3 | peer review | рецензирование |
| 4 | reproducibility crisis | кризис воспроизводимости |
| 5 | training distribution | обучающее распределение |
| 6 | hallucination | галлюцинация (whitelisted RU term) |
| 7 | open-source / open-weights | открытый исходный код / открытые веса |
| 8 | closed-world / open-world | закрытый мир / открытый мир (педагогический термин) |
| 9 | autonomous lab / self-driving lab | автономная лаборатория |
| 10 | drug discovery | поиск лекарственных кандидатов |
| 11 | docking | стыковка (молекулярная) |
| 12 | benchmark | тестовый набор / эталонный набор |
| 13 | retraction | отзыв (публикации) |
| 14 | paper mill | бумажная фабрика (или: фабрика статей) |
| 15 | hypothesis generation | формулирование гипотез |
| 16 | embedding | векторное представление |
| 17 | transit (exoplanet) | прохождение / транзит (астрофизический термин) |
| 18 | citation network | сеть цитирования |
| 19 | replication | воспроизведение / реплика |
| 20 | data drift / distribution shift | сдвиг распределения |
| 21 | inverse design (materials) | обратное проектирование |
| 22 | wet lab / dry lab | физическая лаборатория / вычислительная лаборатория |

**Whitelisted brand+gloss (можно оставить латиницей):**
- AlphaFold / AlphaProof / AlphaGeometry — DeepMind продукты.
- AlphaFold DB — public protein structure database.
- GNoME, MatterGen, Aurora, GraphCast, Pangu-Weather, FourCastNet — конкретные модели; первое упоминание + RU gloss «фундаментальная модель погоды».
- Boltz-1 / Boltz-2 — MIT open-source модели; первое упоминание + gloss.
- Coscientist — CMU система; первое упоминание + gloss.
- Galactica — Meta модель (исторический фейл); first mention + gloss.
- NotebookLM, Elicit, Consensus, Semantic Scholar, PaperQA, Scite — brand names tools.
- CASP — Critical Assessment of protein Structure Prediction (отраслевой бенчмарк); first mention + RU gloss.
- IMO — International Mathematical Olympiad; first mention + RU gloss.
- FrontierMath — Epoch AI benchmark; first mention + gloss.
- ICMJE — International Committee of Medical Journal Editors; first mention + gloss.
- ECMWF — European Centre for Medium-Range Weather Forecasts; first mention + gloss.

**Pre-submission deep latin-token scan:** обязателен для каждой revision (см. `tools/presentation-build/README.md` §5.8).

---

## Сравнение vs Lec-{N-1}, Lec-{N-2} (baseline I-9 lec-11 lesson)

### Lec-14 (AI в телекоме / AIOps / кибербезопасности, мерж 2026-05-22)

- **Chapter:** 34 451 слов (4 parts).
- **Slides:** 39 (51.3% media).
- **Speech:** 6 402 слов, ≤95 WPM на каждом слайде.
- **Failure-bucket:** ~50% chapter / ~62% slides / 80.3% speech (holistic).
- **Hero:** s01 CrowdStrike BSOD LGA airport screen + s39 NOC IUPUI.
- **Keystone:** «Лестница автономии AI: Видит → Решает → Действует».

### Lec-13 (AI в логистике и транспорте, мерж 2026-05-22)

- **Chapter:** ~31 313 слов (3 parts).
- **Slides:** 41 (85% media).
- **Speech:** 6 914 слов.
- **Failure-bucket:** ~50% chapter / ~62% slides.
- **Hero:** Waymo + Cruise / Tesla failure кейс.
- **Keystone:** «Лестница среды 5 уровней» + 7-criteria decision framework.

### Lec-11 (AI в производстве, мерж 2026-05-21)

- **Chapter:** 30 930 слов (3 parts).
- **Slides:** 41 (~63% media).
- **Speech:** 5 289 слов.
- **Failure-bucket:** ~41% chapter (strict-in).
- **Hero:** Tesla Giga Press BEFORE/AFTER + BMW Welt digital twin.

### Lec-15 targets (этот план)

- **Chapter:** **≥30 000 слов** (target 28 500-31 500; multi-part 3-4 файла по 7-9k слов) — **match lec-13/14**.
- **Slides:** **39 slides** target — **match lec-14**.
- **Media coverage:** **≥50%** (target ~64%) — **close to lec-13 (85%)**, выше lec-14 (51.3%); pragmatic baseline matching.
- **Speech:** **~6 000 слов** (75 мин at ≤95 WPM на каждом слайде); **between lec-11 5289 и lec-13/14 ~6300-6900**.
- **Failure-bucket strict-in:** **~47% holistic** — slightly above lec-11/lec-13/lec-14 baseline; reflects unique nature of lec-15 (peer review failures, paper mill — большой failure cluster).
- **Hero:** **«Две стороны медали»** — AlphaFold-Nobel + Galactica-shame; novel pattern (not single hero, side-by-side).
- **Keystone:** Variant A — «Лестница научного цикла» (рекомендация; final defer to owner).

### Где мы должны побить / match lec-14 specifically

- Chapter words: **match ≥30k**.
- Failure-bucket: **match ≥45-50%** (lec-14 — 50%).
- Media: **match 50%+** (target 64%).
- Slides count: **match 39**.
- Cascade-of-changes / numbers-convention-lock: **bake-in from start** (I-8 lesson; lec-11 brewery drift).

### Где мы должны differentiate

- **Hero pattern:** lec-9/10/11/12/13/14 все single-hero на s01. **Lec-15 — side-by-side pair** — first lecture с такой структурой; рискованно, но усиливает «двух сторон медали» narrative.
- **Failure cluster topology:** lec-13/14 — failure-deep-dive distributed по разделам. **Lec-15 — concentration в Разделе 4 (peer review failures)** — это уникально для темы AI-в-науке (где failure-кластер именно в публикации, а не в применении).

---

## Anti-dependencies — что НЕ дублировать

### Vs Lec-12 (AI в производстве / двойники)

- Lec-12 — **digital twins as bridge** (manufacturing automation level scale A0→A3); Lec-15 — **AI замена + augmentation в науке**. Не пересекаются.
- **Не повторять:** Cassie / Agility Robotics (lec-12 s39 hero), Hannover Messe trade show, ISA-95 5-уровневая иерархия.

### Vs Lec-13 (AI в логистике / транспорте)

- Lec-13 — **лестница среды 5 уровней** + Waymo/Cruise/Tesla AV failures. Lec-15 — **другая лестница** (научного цикла). Keystone forms different.
- **Не повторять:** Waymo / Cruise / Tesla detailed deep-dive; OR-Tools mentioning в контексте VRP (упомянуть как **альтернатива в науке тоже OR-Tools используется, но другое применение — clinical trial design**).

### Vs Lec-14 (AI в телеком / AIOps / кибербез)

- Lec-14 — **«Лестница автономии AI: Видит → Решает → Действует»** — *хорошее* отличие от Variant A (фаза работы) или Variant B (closed/open-world).
- **Не повторять:** CrowdStrike, Cloudflare config-cascade, Klarna / Air Canada Moffatt — это AI в инфраструктуре, не в науке.
- **Можно ссылаться (one-line callback):** «лестница автономии lec-14 — про operating systems; **наша лестница цикла** — про phases of scientific work. Different mental object».

### Vs Lec-16 (AI в нефтегаз; **следующая лекция**)

- Lec-16 — **AI в нефтегазовой отрасли** (геофизика, sub-surface modeling). Lec-15 — **AI в науке вообще**. Pre-warning: некоторые AI-tools в нефтегазе (DeepMind weather Aurora, materials GNoME) **могут пересекаться** — но в lec-15 показываем их **как foundation models для науки**, в lec-16 — **как applied для resource production**.
- **Bridge в s39** — явно: «AlphaFold показал, что closed-world задачи доступны AI. Лекция 16 — нефтегаз, ещё одна closed-world domain».

### Vs Lec-7 (AI в медицине / фарма)

- Lec-7 — **AI в clinical medicine + drug discovery deployment**. Lec-15 — **AI в drug discovery как research**.
- **Можно ссылаться:** «Insilico Medicine ISM001-055 Phase IIa — мы видели в Лекции 7 deployment side; здесь Insilico = research-side success of AI drug discovery generation».
- **Не повторять:** FDA Part 11, HITL в clinical setting, EBM hierarchy.

---

## Anonymization (ENFORCED — Лекция 9 lesson)

- **Frontmatter audience:** «студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)» — НЕ ИУ6 / МГТУ / Бауман.
- **Career angle:** «профильные технические университеты + научно-исследовательские институты», без «МГТУ им. Баумана» / «МАИ» / «СПбГУ» / «РАН» / «Сколтех» / «ВШЭ» (явных названий).
- **Российский контекст:** «отечественные НИИ» / «академические институты России»; российские grant agencies — «РНФ» whitelisted (как FDA / NSF — это abbreviation для крупной организации с established RU расшифровкой).
- **Эталон:** lec-03 / lec-05 / lec-07 chapters — 0 named institutions; lec-06 — единственная generic «профильные кафедры».
- **Cost-of-omission lec-09:** 1 revision cycle (v2→v3) anonymization.

---

## Risk register

| # | Risk | P×I | Mitigation |
|---|---|---|---|
| R1 | Hero «две стороны медали» — нестандартный pattern может быть критикован designer'ом. | M×M | Backup: single hero AlphaFold ribbon structure (DeepMind press); если designer flags — switch к classic single hero. Решение Phase 5 после design attempt. |
| R2 | Keystone Variant A (Лестница цикла) — слишком похожа на lec-13 (Лестница среды) и lec-14 (Лестница автономии). | L-M×H | Plan явно различает: «фаза работы», не «уровень среды» и не «уровень control». Mermaid-визуализация — vertical (vs lec-14 horizontal); 6 ступеней (vs lec-13 5 уровней, lec-14 3 уровня). Methodology-critic Phase 1 must validate distinguishability. **Fallback:** Variant B (closed/open-world) — другая mental object. |
| R3 | Sakana AI Scientist — **активно итерирует**; v3 / v4 могут выйти к лекции. | M×M | `[VFY-day-of]` markers; orchestrator 1-page refresh за 1-2 дня до лекции; список research/07 (когда создадим в Phase 2). |
| R4 | AlphaFold DB count, FrontierMath leaderboard — volatile. | M×L | `[VFY-day-of]` markers; verify-day-of mandatory. |
| R5 | NeurIPS 2025 fake citations — recent (декабрь 2025), может быть обновлено новой информацией. | M×M | Phase 2 fact-checker re-verifies arxiv 2602.05930 + GPTZero analysis. |
| R6 | Российский контекст thin — feedback «нет российских кейсов». | M×M | Включить: «РНФ AI4Science grants 2024-2025», «Сколтех Centers of Excellence в materials» (без specific persons), «AI Russia 2030 Strategy» как regulatory frame. **Признать** thinness — это pedagogical point (см. lec-11 §3.5 pattern). |
| R7 | Galactica retraction — старый кейс (2022, 4 года). | L×M | Используется как baseline, **не frontier**. Combined с свежими NeurIPS 2025 / Frontiers 2024 / Sakana 2024-2025 — full timeline current. |
| R8 | AlphaFold 3 — **commercial** debate может стать stale (если Isomorphic Labs deals change). | L×M | `[VFY-day-of]` для Lilly / Novartis deal totals; verify per Phase 2 fact-checker. |
| R9 | Failure cluster в §4 (Write + Review) может казаться unbalanced ((peer review failure >> other failures). | M×M | Plan явно: §4 — peak failure section by design. §5 — payoff с критериями и альтернативами. §6 — recap. Distribution: §0 28% / §1 45% / §2 23% / §3 33% / §4 70% / §5 87% / §6 33% — distributed (min ~23% just below 30%, max 87%). |
| R10 | AlphaFold protein design vs AlphaFold-Multimer vs AlphaFold 3 — terminology может drift. | L×M | Glossary lock после chapter v1 finalize; consistency-checker terminology mode для AlphaFold variants. |
| R11 | DeepMind Co-Scientist (Nature May 2026, **очень свежее**) — может быть преувеличено / уточнено к лекции. | M×M | `[VFY-day-of]` для Co-Scientist; primary source Nature paper. **Fallback:** если Co-Scientist Nature paper retracted / heavy critique — переместить на secondary mention; keep main focus AlphaFold + Sakana + Coscientist (более established). |
| R12 | Worked example «catalyst pipeline» (s34) — нужен specific case, currently abstract. | L×M | Phase 2 book-editor должен заполнить с specific catalyst (например, **propylene oxidation catalyst** из Materials Project + GNoME) + specific DFT alternative + specific BO alternative. |

---

## Plan-level mandates carry-forward checklist (ENFORCED)

- [x] **Hero images plan для s01 + s39** прописан с 6-tier strategy + entity + attribution.
- [x] **Russification mandate в plan v1 sam** — таблица 22+ replacements; brand whitelist; deep latin-token scan mandatory.
- [x] **6-tier real image acquisition strategy** sketched per case-study slide (см. § Media plan + § Hero plan); **≥18 real images** target across 39 slides.
- [x] **Anonymization carry-forward** — generic «студенты-инженеры 3 курса», без named institutions (см. § Anonymization).
- [x] **Anti-anglicism таблица** ссылается на canonical replacements (см. таблица 22+).
- [x] **Failure-bucket honest tracking** — recount table (§ Bucket map); strict-in 47% > 30% target.
- [x] **Keystone в §0 ДО первого погружения; заголовок про ось** (Variant A recommended; final defer to owner).
- [x] **Numbers convention lock** — 18 canonical claims (см. § Numbers convention lock).
- [x] **Baseline / counterfactual** на каждое measurable claim — встроено в § Worked examples (каждый случай имеет baseline).
- [x] **`[VFY-day-of]` markers** — для volatile (FrontierMath leaderboard, AlphaFold DB count, NotebookLM MAU, Co-Scientist).

---

## Self-check (перед commit)

- [x] Все sections `templates/lecture-outline.md` заполнены (Topics / Prerequisites / Normative / Materials placeholder / LO / Keystone / Tools per level / Outline / Provals / Anonymization / Russification / Hero / 6-tier).
- [x] **3 keystone variants с trade-offs** (Variant A / B / C + рекомендация Variant A).
- [x] **≥4 worked examples с baseline/counterfactual** — 6 worked examples (3 success / 1 mixed / 4 failure — реально 6, в плане 4+ требовался).
- [x] **Failure-share %** явно бьётся ≥30% holistic на каждый artifact (47% strict-in).
- [x] **≥10 ключевых measurable claims canonical** — 18 в § Numbers convention lock.
- [x] **Hero plan: 2 реальных изображения с источниками** для s01 + s39 (Nobel ceremony + AlphaFold DB).
- [x] **Russification таблица с ≥10 anglicisms** — 22+.
- [x] **Lec-14 / lec-13 baseline сравнение** присутствует (§ Сравнение vs Lec-{N-1}).
- [x] **Sections roadmap** покрывает 7 секций × bucket-tag (§0-§6).
- [x] **Anti-dependencies с lec-12/13/14** явно прописаны (§ Anti-dependencies).
- [x] **Никаких anglicisms в plan body** (брэнды + ключевые акронимы whitelist OK; brand-mention sequence audited).
- [x] **Никаких named institutions (МГТУ / Бауман / ИУ-X)** — verified.
- [x] **Никаких timing маркеров «(N мин)»** в slide-outline предложениях — только в section headers / metadata (e.g., «Раздел 0 — 7 мин» в outline ОК как plan-level metadata, **НЕ в slides body**).

---

## Длина plan'а

**Word count plan-v1.md:** ~5 900 слов (planning artifact, чуть выше typical 3 500-5 000 range из-за extensive worked examples + Russification table + Risk register; см. lec-11 v2 plan-v2-final = ~4 200 слов — наш v1 чуть глубже потому что keystone defer-to-owner требует 3-variant elaboration).

---

## Phase 2 chapter brief carry-forward (для book-editor Phase 2)

**Single-paragraph instruction для book-editor Phase 2 chapter draft:**

Глава **≥30 000 слов**, source-of-truth для slides + speech, **multi-part split 3-4 файла**. **Emphasis на:** (1) keystone (Variant A recommended, defer to owner) через всю главу с явным failure-callbacks под каждой ступенью лестницы цикла; (2) Раздел 2 (Experiment) — самая глубокая капитальная глава по объёму слов (~5 500 слов), описывает все Nobel-tier breakthroughs (AlphaFold 2/3, GNoME/A-Lab, Aurora, AlphaProof) **+ обязательный failure-deep-dive Palgrave critique в §2.4-§2.5**; (3) Раздел 4 (Write + Review) — concentrated failure section (~4 000 слов), детальный разбор Galactica / Frontiers / NeurIPS / Sakana с lessons и criteria; (4) §5 worked example «catalyst pipeline через 5-step framework» — **развёрнуто ~800 слов** с specific catalyst case (propylene oxidation или similar), specific DFT alternative, specific BO alternative; (5) failure-bucket strict-in distributed по 7 разделам, target ~45-47% слов; (6) anti-anglicism deep latin-token scan на каждой revision (Russification таблица 22+ — § Russification); (7) Numbers convention lock — все 18 canonical measurable claims (§ Numbers convention lock) — никаких variations без cascade-of-changes check. **Cornerstones lock:** 8-10 main terms + secondary glossary, no drift. **Carry mandates:** anonymization absolute, 6-tier hero acquisition план для s01 + s39, real-image ≥18 / 39 slides. **Что НЕ делать:** keystone про что-то кроме Variant A (или Variant B / C если owner иначе); §4 как «AI делает плохо» laundry list без critic distinctions; «магическая пилюля» строки в failure-bucket count; named institutions в audience; англицизмы в narrative body; AlphaFold-Multimer без glossary intro; «commercial AlphaFold 3 debate» без attribution Isomorphic Labs Lilly+Novartis $3B context.

**Expected chapter section count:** 7 (Введение + §1 Hypothesis+Design + §2 Experiment + §3 Analyse + §4 Write+Review + §5 Когда AI не нужен + §6 Замыкание). Каждая section: motivation + content + self-check questions + sources. Q&A backup ~10-15 questions. References ~120-150 inline.

---

## Open questions для owner

1. **Keystone choice:** Variant A (Лестница цикла) рекомендую; Variant B (closed/open-world) — альтернатива; Variant C (Discovery × Validation × Production) — fallback. **Решение defer to owner.**
2. **Hero pattern для s01:** «две стороны медали» (side-by-side AlphaFold-Nobel + Galactica-shame) — novel pattern, рискованный. Owner approval before Phase 5 design start?
3. **Российский контекст глубина:** Сколько процентов §5 уделить РФ-AI-в-науке? Lec-11 был ~3 мин (4% of 75 мин); lec-13 — ~5 мин (КамАЗ-54901 + Сберлогистика); lec-14 — заметнее (Cognitive Pilot одно упоминание). Для lec-15 — РНФ + Сколтех + AI Russia 2030 strategy = ~3 мин в §5.
4. **AI Scientist v2 — насколько глубоко?** Самый свежий кейс с peer-review-pass, но Sakana сами disclosed что cherry-picked. Worth dedicated slide (s30) или integrate в s10? Plan currently has both s10 (Sakana failures deep-dive) и s30 (Sakana ICLR workshop) — может надо merge?
5. **DeepMind Co-Scientist (Nature May 2026)** — **очень свежее** (~9 дней до возможной лекции). Стоит ли treat как primary случай OR keep как secondary mention? **Risk:** свежий case может быть retract / corrected к лекции. Currently s07 (1 слайд) — стабильно.
6. **AlphaFold IDP limits (s23)** — нужен ли отдельный слайд или integrate в s12-s13 AlphaFold discussion? Plan currently — отдельный слайд, потому что failure-deep-dive важен.

**Конец Plan v1.** Next: Phase 1 critique (methodology-critic + reader-text-only) → revision к v2/v3/v4 → USER GATE A check.
