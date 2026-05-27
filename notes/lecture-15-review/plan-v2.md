# Лекция 15: AI в научных исследованиях — план v2

## Метаданные

- **Лекция:** 15 (Модуль 3) — 75 мин + Q&A ~5 мин
- **Учебные результаты (LO):** LO4 (анализ литературы и формулирование задач), LO5 (этика и ответственная разработка), LO6 (критическое мышление и оценка применимости), LO8 (применять и создавать — выбор инструмента и альтернативы)
- **Аудитория:** студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)
- **Issue:** #143 — `issue-143-lec-15`
- **Статус:** v2 (Phase 1 critique applied — methodology REVISE + fact-checker REVISE addressed; owner decisions #1-#4 integrated)
- **Дата:** 2026-05-27
- **Несущая ось (LOCKED по owner decision #1):** **Variant A — «Лестница научного цикла»** (6 ступеней: Hypothesis → Design → Experiment → Analyse → Write → Review). Название «Лестница» оставлено по owner decision (acceptance of «третья лестница после lec-13/14» risk; differentiation поддерживается отдельной таблицей сравнения — см. § «Keystone differentiation table»).
- **Hook A основной (LOCKED по owner decision #2):** AlphaFold 3 → Нобелевская премия по химии 2024 (Hassabis, Jumper, Baker) **рядом** с Galactica 2022 (трёхдневный позор) — side-by-side hero «две стороны медали».
- **Hook B запасной:** Sakana «The AI Scientist v2» — paper прошёл peer review на workshop ICLR 2025, но содержит «hallucinations, faked results, overestimated novelty».

---

## Changelog v1 → v2

### Owner decisions (LOCKED 2026-05-27)

- **#1 Keystone:** Variant A «Лестница научного цикла» — окончательно. Название не меняется (owner accepts risk «третья лестница»). Variant B / C переведены в § «Альтернативные keystone варианты (rejected)». Добавлена явная таблица сравнения lec-13 vs lec-14 vs lec-15 (см. § «Keystone differentiation table»).
- **#2 Hero s01:** Side-by-side «две стороны медали» — final. Добавлена § «Hero design mitigation strategy» с 4 mitigation tactics для split-attention risk и backup fallback (single hero AlphaFold ribbon).
- **#3 Co-Scientist:** Secondary (1 line, `[VFY-day-of]`) — НЕ dedicated slide s07. Primary Hypothesis case — Sakana failures. Slot s07 consolidated (см. изменения в Outline §1).
- **#4 RU context:** Глубже — 2-3 кейса × ~5 мин. AIRI + Sber AI Lab + Yandex Research + РНФ AI4Science grants + AI Russia 2030 Strategy. Без named universities (МГТУ / Сколтех / ВШЭ / РАН). См. § «Российский контекст AI-в-науке».

### P0 fixes (BLOCKING — applied)

- **P0-1 Worked examples:** reframed claim «6 worked examples» → «3 applicable walked examples + 4 case-study deep-dives». Добавлены 2 новых applicable: WE-1 (grant idea decision tree, §1) + WE-2 (collaborator bibliography 4-step verification, §4). WE-3 (catalyst pipeline, §5) заполнен propylene oxidation specific. s25 «спектральные сигналы» переписан в full TESS transit search walked example.
- **P0-2 Keystone differentiation:** добавлена таблица сравнения lec-13 vs lec-14 vs lec-15 по 6 dimensions; Variant A locked; Variant B/C — short paragraph каждый в отдельной секции.
- **P0-3 A-Lab Berkeley numbers:** все упоминания «36 of 57» → **«41 of 58 in 17 days»** (Nature Szymanski et al. Nov 2023, doi.org/10.1038/s41586-023-06734-w). Cascade-check phrase добавлена в Phase 2 brief.
- **P0-4 Allen MICrONS conflation:** s21 reframed с **одним primary case (MICrONS Apr 2025: 1 mm³ visual cortex, 84K neurons + 500M synapses + 4km axons)**. Brain Knowledge Platform и UCSF+Allen 1300 mouse brain regions упоминаются одной строкой, без conflation.

### P1 fixes (cascade-applicable — applied)

- **P1-1 §2 strict-in:** добавлены 3 inline failure callbacks (s12 IDP regions, s18 Aurora extreme weather miss, s19 AlphaProof time-cost) → §2 strict-in ~33% (было 23%).
- **P1-2 §4+§5 cognitive overload:** s33 reframed как success story (DFT 50+ лет / GP 60+ / BO 40+ / OR-Tools 70+); s37 recap inline positive markers (AlphaFold 200M + Aurora 5000× + IMO silver); s31 inline positive measure.
- **P1-3 Hero mitigation:** добавлена § «Hero design mitigation strategy» — uniform visual treatment / single composite image / bridging caption / fallback к single hero.
- **P1-4 Phase 2 chapter brief:** rewritten 600+ слов — section word budgets + Q&A backup 15 questions + cornerstones lock list 12 terms + references breakdown + cross-reference policy + multi-part split boundaries + per-section failure-bucket targets.
- **P1-5 s25 spectra:** переписан в walked example TESS transit search (5-step framework).
- **P1-6 §2 terminology overload:** s04 glossary 6-8 → 15 terms (CASP, IDP, DFT/MD, BO/GP, ECMWF, FrontierMath, ICMJE, IMO, closed/open-world, paper mill, HITL, ground truth, hallucination).
- **P1-7 §4 rebalance:** 1.5+8.5 → 3+7.5 — s26+s27+s31 inline positive measures.
- **P1-8 Coscientist vs Co-Scientist disambiguation:** explicit в s09 + glossary s04; numbers convention lock — оба separately.
- **P1-9 Nobel date:** 8 октября 2024 → **9 октября 2024**.
- **P1-10 Palgrave framing:** **36 success samples examined, 35 of 36 had errors** (incorrect crystal structure assignment / derivatives mislabeled / no demonstrated functionality). Update s17 и Numbers convention lock #16.
- **P1-11 Coscientist GPT-4:** → **GPT-4 + Claude both** (Nature 2023 primary text).
- **P1-12 ECMWF claim soften:** **AIFS operationally с 2024 (ECMWF own)**; Aurora/GraphCast/Pangu/FourCastNet — benchmark / evaluation references, **не confirmed operational deployments**. `[VFY]` flag.
- **P1-13 Inline `[VFY-day-of]`:** добавлены inline маркеры в outline (s13, s19, s26, Co-Scientist).
- **P1-14 RU context depth:** см. Decision #4 above.

### P2 fixes (applied where easy)

- **P2-1 Russification table:** 22 → 28 entries (добавлено: backbone → остов, scaffold → каркасный фрагмент, binding affinity → сила связывания, zero-shot → без обучения, fine-tuning → дообучение, in-context learning → обучение по контексту).
- **P2-2 Sakana cherry-pick mechanics:** explicit в s10 — «Sakana пишет ≈100 papers per cycle; human curator selects 3 to submit — это **не autonomous наука**, это AI-augmented с heavy human gate».
- **P2-3 Lec-16 bridge soften:** «**частично** closed-world (geophysics, sub-surface modeling) + частично open (reservoir characterization)».
- **P2-5 Сколтех:** removed. AIRI / Sber AI Lab / Yandex Research = brands OK (whitelisted).
- **P2-6 «Раздел 0» → «Введение»:** rename для consistency с lec-13/14 pattern.

---

## Topics Covered

Фундаментальные модели для науки (предсказание структуры белков AlphaFold 2/3, погода Aurora/GraphCast/Pangu, материалы GNoME/MatterGen) + автономные лаборатории (Coscientist, A-Lab, Emerald Cloud Lab) + формальная математика (AlphaProof, AlphaGeometry 2, FrontierMath) + генерация гипотез и черновиков статей (Sakana AI Scientist v1/v2, DeepMind Co-Scientist secondary, Gemini for Science) + помощь в обзоре литературы (Elicit, Consensus, Semantic Scholar, NotebookLM, PaperQA) + LLM-разметка экспериментальных данных (астрофизика — детекция экзопланет TESS/Kepler, нейронаука — Allen MICrONS, гравитационные волны LIGO) + провалы и границы (Galactica 2022, A-Lab Palgrave critique 2024, Sakana hallucinations, Frontiers «крыса» 2024, NeurIPS 2025 100+ fake citations) + российский контекст (AIRI, Sber AI Lab, Yandex Research, РНФ AI4Science grants, AI Russia 2030 Strategy) + альтернативы (байесовская оптимизация, first-principles DFT/MD, классическое рецензирование, OR-Tools для научной логистики).

## Prerequisites

- **Лекция 1** — типы AI-систем, понятие галлюцинации, промптинг (Role+Task+Context). Эта основа критична — мы много раз возвращаемся к «галлюцинация ≠ ошибка», «модель не знает истины, только распределение слов».
- **Лекция 2** — архитектура трансформеров, эмбеддинги, матрица внимания. Нужно для понимания, почему AlphaFold (transformer-based) даёт хорошее предсказание fold, но не понимает биологию.
- **Лекция 3** — архитектуры AI-систем (агенты, RAG, API). Нужно для понимания Coscientist (агентная архитектура с tool-use) и литературных поисковиков (RAG над arXiv/PubMed).
- **Лекция 7** — AI в медицине (HITL, доказательная медицина). Параллельный пример «AI в науке требует HITL» — drug discovery как пограничный кейс.
- **Лекция 11** — провалы pilot purgatory, парадокс автоматизации. Та же логика «95% не доходят» применяется к научным AI-стартапам.

## Normative References

- **Nobel Prize Chemistry 2024** (9 октября 2024) — Baker / Hassabis / Jumper за computational protein design и protein structure prediction. **Доктринальный референс**: первый Нобель за breakthrough, enabled by AI.
- **NeurIPS / ICLR / Nature / Science кодексы публикации** — текущие требования к AI-использованию (обязательное disclosure, запрет на полностью AI-generated review).
- **NSF AI Code of Conduct** (US National Science Foundation, обновлено 2025) — рамки responsible AI в federally-funded research; обязательное disclosure AI-tooling в grant proposals.
- **EU AI Act (2024)** — научные применения попадают в разные tier'ы в зависимости от deployment; foundation models под §51-§55, scientific research как «limited risk» — но peer review и медицинские применения могут попадать в «high risk».
- **Frontiers / Elsevier / Springer Nature AI policies 2024-2025** — каждое издательство опубликовало свою политику по AI-generated content (Frontiers: 2024 retraction rat-anatomy paper как прецедент; Springer: must disclose).
- **DOE Genesis Mission ($320M, декабрь 2025)** — институционализация AI4Science в США; интегрированная American Science and Security Platform.
- **GAMP®5, FDA 21 CFR Part 11** — символично из Лекции 11; здесь применяется к AI в drug discovery (AlphaFold-based pipelines в pharma).
- **ICMJE Recommendations** (Уведомление о CRediT-таксономии) — авторство, AI-tools нельзя называть автором.
- **Российский контекст:** Указ Президента РФ № 145 («AI Russia 2030» — Стратегия развития искусственного интеллекта до 2030 года) и приказы Минобрнауки 2024-2025 по AI в науке (impact на гранты РНФ AI4Science).

## Learning Objectives

1. **LO4 (Помнить + Применять).** Назвать ≥4 класса AI-инструментов для научной работы (фундаментальные модели для предметной области, автономные лаборатории, литературные RAG-помощники, LLM-разметка данных), для каждого — 2-3 dominating 2026-инструмента с направлением внедрения (растёт быстро / растёт медленно / зрелый / провалился). Применить классификацию к учебному кейсу.
2. **LO5 (Оценивать).** Сформулировать ≥3 этических риска применения AI в науке: (a) галлюцинированные цитаты в публикациях (paper mill), (b) автоматический peer review без disclosure, (c) использование AI как «co-author» в обход ICMJE. Обосновать, почему disclosure обязательно.
3. **LO6 (Анализировать + Оценивать, ЦЕНТРАЛЬНЫЙ — failure-bucket).** Применить «лестницу научного цикла» (см. keystone) к гипотетической исследовательской задаче, показать **на какой ступени AI работает, на какой требуется HITL, на какой AI вреден**. Различить «AI-augmented research» и «AI-autonomous research». Сформулировать ≥4 категории критериев «AI не нужен в науке» (closed-world vs open-world / training distribution coverage / verifiability / ethical risk).
4. **LO8 (Применять и создавать).** Для конкретного кейса (предложит лектор: «нужно найти 10 релевантных статей по теме X», «нужно сгенерировать гипотезу для гранта», «нужно обработать спектральные данные») выбрать AI-инструмент, обозначить границы, **предложить не-AI альтернативу** (байесовская оптимизация, DFT/MD first-principles, классический научный руководитель, OR-Tools). Применить 3 уточняющих вопроса к вендору (как в Лекциях 11/13/14): baseline / окно измерения / change-control.

---

## Несущая ось — Variant A «Лестница научного цикла» (LOCKED)

**Зачем это keystone.** Научная работа структурно делится на 6 ступеней: формулирование гипотезы (Hypothesis) → планирование эксперимента (Design) → проведение эксперимента (Experiment) → анализ данных (Analyse) → написание (Write) → рецензирование (Review). AI «входит» в каждую ступень **по-разному**: где-то как helper (Write — литературное оформление), где-то как breakthrough (Experiment — AlphaFold заменяет годы wet-lab), где-то с **серьёзными рисками** (Review — галлюцинированные цитаты, fake peer review), где-то **категорически не работает** (Hypothesis в open-world domains). Лестница — диагностический инструмент: задайте каждой ступени вопрос «здесь AI augmentation, autonomous или vetoed?».

**Как распределяет 75 мин.** Введение (7 мин) — hook (AlphaFold Nobel рядом с Galactica позором) + keystone-слайд лестницы. Раздел 1 (10 мин) — Hypothesis + Design (Sakana как primary failure case + Coscientist как proof-of-concept, BO как зрелая альтернатива; Co-Scientist secondary one-liner). Раздел 2 (15 мин) — Experiment (AlphaFold 2/3 + GNoME + Aurora — самый сильный успех AI в науке, с inline failure callbacks). Раздел 3 (12 мин) — Analyse (LLM-разметка экзопланет / brain map / gravitational waves — solid use case). Раздел 4 (12 мин) — Write + Review (NotebookLM + Elicit + Consensus как augmentation, но **fake citations NeurIPS 2025**, Frontiers «крыса», Sakana scandals — самое тяжёлое failure-clustering). Раздел 5 (12 мин) — критерии «AI не нужен в науке» + альтернативы + worked example «catalyst pipeline» + российский контекст. Раздел 6 (6 мин) — закрытие + мост к Лекции 16.

**Cyclical, не sequential.** Это критическое различие от lec-13 (среда — sequential) и lec-14 (автономия — sequential). Научная работа **итеративна**: Review (peer review revisions) часто возвращает работу к Analyse или даже Experiment. Лестница — phase-of-work fit, не строгий порядок.

### Keystone differentiation table (lec-13 vs lec-14 vs lec-15)

| Аспект | Lec-13 «среда» | Lec-14 «автономия» | Lec-15 «цикл» |
|---|---|---|---|
| Что измеряет ось | Сложность среды (предсказуемость) | Уровень доверия в loop (control authority) | Стадия научной работы (phase) |
| Тип единицы | Внешний контекст | Control delegation | Workflow phase |
| Пример L1/L2 | Закрытый склад / открытая улица | Видит / Видит+Решает | Hypothesis / Design |
| Что решает ось | «Где AI применим» | «Кто принимает решение» | «На какой фазе AI помогает / вредит» |
| Sequential / cyclical | Sequential | Sequential | **Cyclical** (итеративный) |
| Aspect of decision | Environment fit | Control delegation | Phase-of-work fit |

**Подчёркивание для критика:** lec-15 — единственная **cyclical** ось из трёх. Это операционное различие, не визуальное.

---

## Альтернативные keystone варианты (rejected, для справки)

### Variant B — «Closed-world vs Open-world: где AI silently works, где он silently fails» (REJECTED)

Гениально-простой бинарный фильтр: AI в науке надёжно работает в **closed-world** задачах (well-defined structure, finite alphabet, validation via experiment); **open-world** — биология организменного уровня, социальные науки, история науки — AI не работает. **Почему rejected:** Variant A более интуитивен в качестве teaching tool для 75-мин лекции; closed/open-world сохранён как **критерий A в Разделе 5** (§5.4 категории «AI не нужен»), не keystone. Также: термин «closed-world» имеет established meaning в logic / AI planning (closed-world assumption в Prolog) — может создать confusion.

### Variant C — «Discovery × Validation × Production triple» (REJECTED)

Триплет фаз: Discovery (гипотезы / просев), Validation (проверка / peer review), Production (публикация / integration). **Почему rejected:** менее наглядно, чем линейная Лестница; границы фаз размыты (drug discovery от GNoME до synthesis в A-Lab — это одновременно Discovery и Validation); пересечение с lec-5 pilot purgatory снижает differentiation. Triple переведён в Раздел 5 как **дополнительная mental model** для рассмотрения одного кейса с другой стороны (не keystone).

---

## Инструменты на каждом уровне таксономии (Variant A — Лестница цикла)

### Уровень 1 — Hypothesis (формулирование гипотез)

- **Sakana AI Scientist v1 / v2** (Sakana AI, август 2024 / апрель 2025) — режим «автономный генератор идей». Adoption-направление: **внимание есть, продакшна нет** — workshop paper прошёл peer review (один из трёх, ICLR 2025), но содержит галлюцинации, faked results. **Primary case для уровня 1 в лекции.**
- **DeepMind Co-Scientist** (Google DeepMind, Nature May 2026, `[VFY-day-of]`) — multi-agent debate-and-rank архитектура. Adoption-направление: **emerging, paper свежий**. **Secondary mention** (1 предложение в s06, не dedicated slide; downgrade по owner decision #3 — risk if retracted к лекции).
- **Gemini for Science** (Google, 2026) — research suite на базе Gemini для life sciences. Adoption-направление: **запущен 2026, ранняя стадия**.
- **Anti-hype оговорка:** генерация гипотез — самый **open-world** этап. AI на этом уровне работает как brainstorm partner, **не как proven научный руководитель**. Hypothesis quality всё ещё требует научного руководителя.

### Уровень 2 — Design (планирование эксперимента)

- **Coscientist** (Carnegie Mellon, Boiko et al., Nature декабрь 2023) — LLM-driven автономная chemistry лаборатория, **GPT-4 + Claude both** (per Nature 2023 primary text), tool-use. Adoption-направление: **proof-of-concept, не production**. **NB: не путать с DeepMind Co-Scientist** (см. уровень 1).
- **Emerald Cloud Lab + Strateos** — remote-controlled cloud labs, ECL имеет 200+ instruments. Adoption-направление: **зрелый сервис, но не autonomous** — учёный по-прежнему пишет protocol.
- **Bayesian Optimization (BO) + Gaussian Process (GP)** — **классическая** альтернатива design-of-experiments; не AI в современном LLM-смысле, но матстатистика. Adoption-направление: **зрелый mainstream**, особенно в materials и chemistry (40+ лет BO, 60+ лет GP).
- **Anti-hype оговорка:** ни одна autonomous лаборатория не достигла «full autonomy» в смысле «работает без supervision». Coscientist делает narrow tasks (synthesis известных компаундов); novel hypothesis discovery — нет.

### Уровень 3 — Experiment (проведение эксперимента / симуляция)

**Это самый сильный успех AI в науке — большинство breakthroughs здесь.**

- **AlphaFold 2 / 3** (DeepMind / Isomorphic Labs, 2020 / май 2024) — Nobel 2024. Adoption-направление: **mainstream в structural biology**; 200M+ protein structures publicly available (AlphaFold DB). AF3 closed-source при запуске → ноябрь 2024 academic open → февраль 2025 publicly available (non-commercial).
- **Boltz-1 / Boltz-2** (MIT, Corso/Wohlwend et al., декабрь 2024) — fully open-source AlphaFold-3-конкурент (MIT license, commercial use allowed). Adoption-направление: **растёт быстро среди академии и biotech'ов**.
- **GNoME** (DeepMind, ноябрь 2023, Nature) — 2.2M predicted materials, 380k stable. **A-Lab Berkeley** automatic synthesis **41 of 58 compounds in 17 days** (Nature Szymanski et al. Nov 2023). Adoption-направление: **disputed** — Palgrave critique January 2024.
- **MatterGen** (Microsoft Research, 2024, Nature) — generative inverse design materials. Adoption-направление: **emerging, open-source**.
- **Aurora** (Microsoft, июнь 2024, Nature) — foundation model для atmosphere; 1.3B parameters; weather + air pollution; 5000× быстрее чем traditional numerical. Adoption-направление: **benchmark reference, не confirmed operational deployment** (см. P1-12 fix).
- **GraphCast** (DeepMind 2023) + **Pangu-Weather** (Huawei 2022) + **FourCastNet** (NVIDIA) — benchmark / evaluation references. **ECMWF runs own AIFS model operationally since 2024** (open-weights); Aurora/GraphCast/Pangu/FourCastNet — competitors, **не confirmed operational deployments в ECMWF** `[VFY-day-of]`.
- **AlphaProof + AlphaGeometry 2** (DeepMind, июль 2024) — IMO 2024 silver medal (28/42 points), AG2 — gold-level на geometry. Adoption-направление: **в активном развитии**, FrontierMath 2024→2025 рост с <2% до 52.4% (GPT-5.5 Pro май 2026, `[VFY-day-of]`); **но 4+ hours per problem vs human 90 min** — time-cost остаётся существенным.
- **Anti-hype оговорка:** AlphaFold — Nobel-grade успех, но **не Nobel = не финал**. AlphaFold предсказывает **fold**, не **function**; не работает на IDP (intrinsically disordered proteins) — **22% hallucinations** в IDP regions согласно analysis 2024. Drug docking всё ещё требует validation.

### Уровень 4 — Analyse (анализ данных)

- **ML-classifiers для exoplanet detection** (TESS + Kepler) — Convolutional Neural Networks классифицируют transit signals. 2025: модель идентифицировала 2 449 high-confidence planets из 3 987 candidates, 83.9% accuracy.
- **Allen Institute MICrONS project** — 1 mm³ visual cortex (мышь) с 84K neurons, 500M synapses, 4km axons (April 2025). Brain Knowledge Platform 2025 (34M brain cells) и ChatGPT-like AI для 1300 mouse brain regions (UCSF+Allen October 2025) — **отдельные параллельные проекты**, упоминаются одной строкой.
- **Machine learning pipelines для LIGO** — gravitational wave detection через CNN + uncertainty quantification (conformal prediction). Adoption-направление: **зрелый mainstream в astrophysics**.
- **Anti-hype оговорка:** ML-классификаторы на data analysis — это **narrow ML, не foundation models**. Большая часть «AI в science discovery» в analyse-фазе — это привычный supervised learning. Это не «AI делает науку» — это «AI ускоряет одну стандартную задачу».

### Уровень 5 — Write (написание статьи)

- **NotebookLM** (Google, 2023, расширение 2024-2026) — RAG-tool для personal corpus; в 2025 добавлен Audio Overview (podcast-style). Adoption-направление: **mainstream академический инструмент**, 17M+ MAU end 2025 `[VFY-day-of]`.
- **PaperQA / Elicit / Consensus / Semantic Scholar / Scite** — literature review augmentation; Elicit (138M papers + 545k clinical trials), Consensus (peer-reviewed direct answers), Semantic Scholar (214M papers). Adoption-направление: **mainstream**.
- **Anti-hype оговорка:** эти инструменты — **augmentation для поиска**, не **замена синтеза**. Любая ML-generated bibliography требует verify-каждой-цитаты. Cost-of-omission: NeurIPS 2025 100+ fake citations прошли peer review.

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
- **DeepMind Co-Scientist** — Nature May 2026 paper свежий; status verify → `[VFY-day-of]`.
- **ECMWF AIFS operational status + competitor benchmarks** — `[VFY-day-of]`.

---

## Outline

### Введение — Hook + keystone + lecture-map (7 мин, slides s01-s05)

**Цель.** Зацепить **двумя картинками рядом**: Nobel-prize 2024 (Hassabis, Jumper, Baker) и Galactica-3-day-shame 2022. Предъявить keystone «лестница научного цикла». Раздел нумеруется как «Введение» (lec-14 pattern).

**Slides:**
- s01 (cover, hero) — Hero **«две стороны медали»** side-by-side: левая половина — Hassabis + Jumper + Baker на Nobel ceremony (декабрь 2024); правая — скриншот заголовка MIT Technology Review «Why Meta's Galactica only survived three days online» (Heaven, ноябрь 2022).
- s02 (lecture-map) — 6 разделов лекции по лестнице цикла. **Section divider** для §1 явно показан.
- s03 (keystone) — **Лестница из 6 ступеней (vertical)**: Hypothesis → Design → Experiment → Analyse → Write → Review; рядом каждой ступени — статус AI 2026 (augmentation / autonomous / vetoed). **Cyclical visual hint** (стрелка от Review обратно к Hypothesis).
- s04 (glossary) — **15 must-know terms** (расширено с 6-8): foundation model, RAG, hallucination, peer review, replication crisis, closed-world / open-world, IDP (Intrinsically Disordered Protein), ground truth, CASP, DFT, MD, BO, GP, ECMWF, FrontierMath, ICMJE, IMO, paper mill, HITL.
- s05 (central question) — «Где AI делает прорыв в науке, где он создаёт paper mill, и как инженер должен решать?»

**Bucket-tag:** mixed (Nobel = success, Galactica = failure — оба явно).

**Strict-in failure-share:** ~35% (Galactica hook = 2 мин strict-in / 7 мин).

### Раздел 1 — Hypothesis + Design (10 мин, slides s06-s11)

**Цель.** Показать AI на «открытом» этапе цикла — гипотезы и planning. Это пока **самая хайповая** и **самая хрупкая** зона. **Section divider s06 (Раздел 1).**

**Slides:**
- s06 (section divider) — «Раздел 1 — Hypothesis + Design: где AI продаётся за autonomy, но даёт narrow help» **+ Sakana AI Scientist v1/v2 intro + Co-Scientist one-line secondary mention** (Nature May 2026, multi-agent debate-and-rank, `[VFY-day-of]`). Этим slide consolidate s06+s07 после owner downgrade Co-Scientist.
- s07 — **WE-1 (NEW APPLICABLE WORKED EXAMPLE)** — «Ваш научный руководитель просит идею для гранта в materials science. Sakana AI Scientist v2 даст 50 candidates за вечер; ваш PhD-руководитель — 3 идеи за месяц. **Walked tree 6 шагов**: (1) classify task (open-world?) → (2) coverage check (is materials в training distribution?) → (3) verification path (DFT? synthesis?) → (4) ethical risk (IRB? authorship?) → (5) HITL design (AI screens → human selects → human submits) → (6) submission integrity (disclose AI use?)». См. § «Worked examples» подробно.
- s08 — Gemini for Science (Google 2026) — research suite на базе Gemini для life sciences; ERA package (CDC forecasting benchmark).
- s09 — Coscientist (CMU Boiko 2023, Nature) — **GPT-4 + Claude both** autonomous chemistry; works на synthesis известных компаундов, novel discovery — нет. **NB: не путать с DeepMind Co-Scientist** (s06).
- s10 — **Failure-deep-dive Sakana**: workshop paper passed peer review (1 of 3), but external audit показал «hallucinations, faked results, overestimated novelty». **Cherry-pick mechanics explicit**: Sakana пишет ≈100 papers per cycle; human curator selects 3 to submit — это **не autonomous наука**, это AI-augmented с heavy human gate.
- s11 — **Альтернатива**: Bayesian Optimization + Gaussian Process для design-of-experiments; **зрелая 40+ лет методика**, не «AI» в LLM-смысле; в materials и chemistry часто **лучше**, чем deep RL.

**Bucket-tag:** mixed (capability + failure + alt-tool + applicable worked example).

**Strict-in failure-share:** ~45% (Sakana failures + альтернатива BO = 4.5 мин strict-in / 10 мин).

### Раздел 2 — Experiment: самый сильный успех AI в науке (15 мин, slides s12-s19)

**Цель.** Главная капитальная глава лекции. Здесь AI **реально дал Nobel-grade прорывы**. Но обязательны inline failure callbacks (P1-1 fix).

**Slides:**
- s12 (section divider) — «Раздел 2 — Experiment: Nobel-grade успех + inline failures» **+ AlphaFold 2 → 3 intro**. AF3 расширил до DNA / RNA / ligands / ions; protein-ligand interaction +50% accuracy. **Inline failure callback (P1-1):** «но IDP regions — 22% hallucinations» (forward-cross-link s23).
- s13 — AlphaFold DB — **200M+ protein structures publicly available `[VFY-day-of]`**. Hero: скриншот DB website.
- s14 — Open-source debate AlphaFold 3 (closed at launch → academic Nov 2024 → public Feb 2025 non-commercial). 1000+ scientists letter за open. Critic: **Isomorphic Labs $3B deals (Lilly + Novartis) — commercial reasons preserved**.
- s15 — Boltz-1 / Boltz-2 (MIT, декабрь 2024) — fully open MIT license; уже **most-used model в своём классе**.
- s16 — GNoME (DeepMind 2023, Nature) — 2.2M materials predicted, 380k stable. **A-Lab Berkeley** — **41 of 58 synthesized in 17 days** (P0-3 fix, canonical).
- s17 — **Failure-deep-dive A-Lab Palgrave critique** (P1-10 fix): **Palgrave-Schoop ChemRxiv январь 2024 examined 36 success samples, found 35 of 36 had errors**: incorrect crystal structure assignment, derivatives mislabeled as novel, no demonstrated functionality. **Lesson**: prediction ≠ proven novelty.
- s18 — Aurora + GraphCast + Pangu + FourCastNet — **benchmark / evaluation references**; ECMWF runs own AIFS operationally since 2024 (open-weights). Aurora 5000× faster than ECMWF baseline `[VFY]`. **Inline failure callback (P1-1):** «но Aurora **systematically** misses extreme weather events (Hurricane Milton 2024 case study — under-prediction intensity)».
- s19 — AlphaProof + AlphaGeometry 2 (IMO 2024 silver, 28/42) → FrontierMath rise (<2% 2024 → **52.4% GPT-5.5 Pro май 2026 `[VFY-day-of]`**). **Inline failure callback (P1-1):** «но AlphaProof has 4+ hours per problem vs human 90 min; FrontierMath 52% means 48% still unsolved».

**Bucket-tag:** capability-heavy, но **обязательно failure-deep-dive в s17 + s14 commercial debate + inline callbacks s12/s18/s19**.

**Strict-in failure-share:** ~33% (A-Lab critic + AlphaFold open-source debate + 3 inline failure callbacks = 5 мин strict-in / 15 мин) — boosted с 23%.

### Раздел 3 — Analyse: solid use cases в data analysis (12 мин, slides s20-s25)

**Цель.** Показать **подъём AI в data analysis** — astrophysics / neuroscience / gravitational waves. Этот фронт **самый продакшнабельный**, потому что задачи **узкие и закрытые**.

**Slides:**
- s20 (section divider) — «Раздел 3 — Analyse: data analysis solid use cases» **+ Exoplanet detection через CNN intro**. TESS + Kepler; 2025 модель — 2 449 high-confidence planets из 3 987 candidates, 83.9% accuracy.
- s21 — **Allen Institute MICrONS** (April 2025, P0-4 fix) — **1 mm³ mouse visual cortex; 84K neurons + 500M synapses + 4km axons**. One-liner: «параллельно — Brain Knowledge Platform (34M brain cells, 2025) и ChatGPT-like AI для 1300 mouse brain regions (UCSF+Allen Oct 2025) — отдельные проекты».
- s22 — Gravitational waves: ML pipeline combination с conformal prediction для uncertainty quantification (LIGO 2024+).
- s23 — AlphaFold limitations deep-dive: 22% hallucinations в IDP regions; α-synuclein не captured; lipid environment не моделируется.
- s24 — **Альтернативы AI в analyse**: classical signal processing (matched filtering для GW), DFT/MD first-principles для chemistry, classical statistical methods.
- s25 — **Walked example уровень 4 (P0-1 / P1-5 fix)** — **TESS transit search (replaces «спектральные сигналы»)**: «Вам дали 1000 hours TESS data; decision: pre-trained NASA Kepler CNN classifier vs train свой CNN vs Bayesian Optimization над classical signal-detection. **Walked 5-step framework**: (1) data overlap analysis (Kepler train ≠ TESS source distribution?); (2) label availability check (есть confirmed planets для labels?); (3) GPU cost estimate (custom CNN training — недели на 8 GPUs; pre-trained — часы; classical — минуты); (4) false-positive rate baseline (**classical = 78% AUC, NASA Kepler CNN = 89% AUC**); (5) verification on held-out 100 hours».

**Bucket-tag:** mixed (capability + failure + alt-tool + applicable worked example).

**Strict-in failure-share:** ~35% (AlphaFold IDP limits + альтернативы + worked example = 4 мин strict-in / 12 мин).

### Раздел 4 — Write + Review: где AI vs академическая интегрита (12 мин, slides s26-s31)

**Цель.** **Самая концентрированная failure-зона лекции**. Здесь AI **активно создаёт риск** для научного метода. Если у студента остаётся только одно воспоминание из лекции — должно быть «не давайте LLM-generated bibliography в peer review без verification». Rebalance §4: 1.5+8.5 → 3+7.5 (P1-7 fix).

**Slides:**
- s26 (section divider) — «Раздел 4 — Write + Review: где AI vs академическая интегрита» **+ NotebookLM augmentation intro**. NotebookLM (Google) — RAG над personal corpus, audio overview; **17M+ MAU 2025 `[VFY-day-of]`**. **Inline positive measure (P1-7):** «NotebookLM позволяет студентам обобщать 50+ источников за 1 час vs typical 1 неделя manual reading».
- s27 — Elicit / Consensus / Semantic Scholar — literature review tools; Elicit 138M papers + 545k trials. **Inline positive measure (P1-7):** «Elicit cuts literature review time **4× per validated user study** (Elicit benchmark 2024, `[VFY]`)»; **используют как стартовую точку, не финал**.
- s28 — **WE-2 (NEW APPLICABLE WORKED EXAMPLE, P0-1)** — «Коллаборатор присылает paper draft с LLM-generated bibliography 47 citations. **Walked 4-step verification workflow**: (1) DOI-resolve каждую цитату (10 минут); (2) проверить relevance к claim (random sample 10, 30 минут); (3) GPTZero analysis на drafting style; (4) request raw source documents от collaborator (refuse to co-author если не предоставлены)». См. § «Worked examples» подробно.
- s29 — **Failure**: Frontiers retraction 2024 — Midjourney-generated rat anatomy с распухшими гениталиями; «protemns», «zxpens». Disclosed в paper, не пойман peer reviewers. Retraction 3 days post-publication.
- s30 — **Failure**: NeurIPS 2025 — **100+ fake citations** пробились в принятые papers (53 papers); 24.52% acceptance rate; ICLR 2026 — 50+ similar. **GPTZero estimate**: half показывали AI-generated drafting signs.
- s31 — **ICMJE rule + публикационные policies**: Frontiers / Springer / Elsevier требуют disclosure; AI не может быть автором. **5 этических критериев** disclosure / verifiability / authorship / liability / replicability. **Inline positive measure (P1-7):** «правильно используемые: AI-tools на write-level cut bibliography prep 5× vs manual».

**Bucket-tag:** failure-heavy, но с inline positive ground + applicable worked example.

**Strict-in failure-share:** ~62% (Frontiers + NeurIPS + WE-2 verification = 7.5 мин strict-in / 12 мин) — slightly ниже v1's 70% из-за rebalance positive ground.

### Раздел 5 — Когда AI не нужен в науке: критерии + альтернативы + worked example + RU context (12 мин, slides s32-s37)

**Цель.** PEAK failure-bucket section. Payoff для LO6 + LO8. Это **applicable mental model**, который студент уносит. **Добавлен RU context inline (Decision #4).**

**Slides:**
- s32 (section divider) — «Раздел 5 — Когда AI не нужен в науке» **+ 4 категории критериев «AI не нужен / вреден»**:
  - **A. Closed/Open-world дисциплина** — если задача требует understanding mechanisms, а не предсказания паттернов → AI не работает (биология, психология, история).
  - **B. Training distribution coverage** — если ваша domain underrepresented в training data → AI hallucinates (медицинские специальности, rare diseases, новые материалы).
  - **C. Verifiability** — если результат не может быть проверен независимо (peer review, citation сетки) → AI создаёт fake records.
  - **D. Ethical risk** — если применение нарушает authorship / disclosure / IRB → не применять.
- s33 — **5 альтернатив AI в науке matrix (P1-2 success story framing)**: «5 проверенных 30-70 лет альтернатив, работающих сегодня»:
  - **Bayesian Optimization / Gaussian Process** — design-of-experiments (vs RL/agentic); **BO 40+ лет, GP 60+**.
  - **DFT / MD first-principles** — материалы и chemistry (vs GNoME-style ML); **DFT >50 лет**.
  - **Classical statistical methods** — psychology, biology (vs LLM analysis).
  - **Operational Research / OR-Tools** — scientific logistics (vs reinforcement learning); **OR 70+ лет**.
  - **Human peer review (с улучшениями)** — academic integrity (vs LLM peer review).
- s34 — **WE-3 (REWRITTEN APPLICABLE, P0-1) — Catalyst pipeline (propylene oxidation specific)**: «Ваш научный руководитель просит: "построй AI-pipeline для предсказания свойств новых катализаторов propylene oxidation"». **Walked 5-step framework**:
  - Step 1: classify task — closed-world (catalysis = quantum chemistry well-defined);
  - Step 2: map alternatives — DFT first-principles vs GP-BO vs GNoME-style ML;
  - Step 3: apply 4 criteria — training coverage есть (Materials Project), verifiability есть (synthesis в lab), ethics OK;
  - Step 4: HITL design — AI screens 5000 candidates → human selects top 10 → synthesis confirms 3;
  - Step 5: pre-publication verify каждую predicted property через DFT calculation **до** статьи.
- s35 — **3 уточняющих вопроса к AI-вендору в науке**: (1) baseline до AI (classical method); (2) reproducibility — published code / data / weights; (3) failure cases — где модель **не работает** explicit.
- s36 — **5-step framework** (повторение, applicable artefact): classify → map alternatives → apply 4 criteria → HITL design → pre-publication verify.
- s37 (NEW) — **Российский контекст AI-в-науке (Decision #4)**: **AIRI** (Институт искусственного интеллекта) — AI4Science research direction; **Sber AI Lab** — scientific tools / climate modeling; **Yandex Research** — academic publications + open-source models; **РНФ AI4Science grants 2024-2025** + **AI Russia 2030 Strategy** (Указ Президента РФ № 145) как regulatory frame. См. § «Российский контекст AI-в-науке» подробно.

**Bucket-tag:** failure-heavy + criteria + alternatives + worked example + RU context.

**Strict-in failure-share:** ~75% (всё кроме worked example positive part + RU context positive frame = 9 мин strict-in / 12 мин) — slightly ниже v1's 90% из-за added RU positive content.

### Раздел 6 — Замыкание + Q&A + мост к Лекции 16 (6 мин, slides s38-s39)

**Цель.** Закрыть лестницу с явным failure-callback. Мост к Лекции 16 (AI в нефтегазе). Dedicated Q&A slide s38 (lec-13/14 pattern).

**Slides:**
- s38 (Q&A dedicated slide) — Recap лестницы цикла с failure-маркерами под каждой ступенью **+ failure-callback (mandatory)**: «Завтра вы получаете LLM-сгенерированную bibliography от коллаборатора. **Что делаете?** — verify каждую цитату через DOI; запрашиваете source documents; **отказываетесь подписать paper если не можете проверить**». **Inline positive recap (P1-2 fix):** «AlphaFold 200M structures + Aurora 5000× speed + AlphaProof IMO silver — failure cluster ≠ AI в науке не работает».
- s39 — **Closing hero** + мост к Лекции 16: AlphaFold DB website screenshot (200M structures = «биология теперь чуть больше известна — но финальная карта далека») → next: AI в нефтегазе (Лекция 16) — **частично closed-world (geophysics, sub-surface modeling) + частично open (reservoir characterization)** (P2-3 fix).

**Bucket-tag:** failure-recall + bridge + positive ground.

**Strict-in failure-share:** ~35% (failure-callback recap = ~2 мин strict-in / 6 мин).

---

## Hero design mitigation strategy (для side-by-side s01)

**Owner decision #2 accepted:** side-by-side hero «две стороны медали» (Nobel ceremony + Galactica retraction screenshot). Methodology critic flagged split-attention risk (P1-3). Mitigation tactics:

1. **Uniform visual treatment.** Same color grade (slight desaturation / cool tones) для обеих половин; same caption typography (Anthropic font system); same 4px stroke border `#1C7293` (Ocean palette stroke). Subjects look like «one composition», not two pasted images.

2. **Single composite image at export.** Designer создаёт **одну** 2560×720 composite image (PNG / WebP), затем resize к 1280×720 slide size. Не два отдельных image-placeholder в PowerPoint — это даёт chance for slight misalignment at render. Composite = single asset.

3. **Caption design — bridging arrow.** Single caption string посередине slide: «AlphaFold Nobel 2024 ⇄ Galactica retraction 2022». Не два caption (по одному на половину) — это усиливает «two unrelated photos» perception. Bidirectional arrow ⇄ — visual bridge между Nobel (capability) и Galactica (failure).

4. **Backup fallback (decision-tree для Phase 5 designer).** Если designer Phase 5 не справляется с composite (визуально слабо / split attention остаётся) → switch к **single hero AlphaFold ribbon structure** (DeepMind press image, Tier 1 og:image) на s01, **Galactica callback на s02 как inline screenshot**. Document fallback decision в `iteration-log.md`. Не try-and-revert через Phase 5+ rounds — escalate к orchestrator после round 2.

**6-tier acquisition приоритеты (для composite):**
- Левая половина (Nobel): Tier 1 og:image nobelprize.org/chemistry/2024 → Tier 2 Wikipedia Commons «Nobel Prize Chemistry 2024 laureates» → Tier 3 DeepMind blog post → Tier 6 Google Images.
- Правая половина (Galactica): Tier 6 fair-use screenshot MIT Technology Review headline (technologyreview.com/2022/11/18/1063487/meta-large-language-model-ai-only-survived-three-days-gpt-3-science) → Tier 4 Wayback Machine snapshot.

**Attribution label visible:** «Nobel Prize Chemistry 2024 © Nobel Foundation | Galactica retraction headline © MIT Technology Review 2022 (fair-use educational excerpt)».

---

## Worked examples (3 applicable walked + 4 case-study deep-dives)

**P0-1 fix:** reframed claim. Plan-v1 claimed «6 worked examples» but only 1 был applicable walked. Plan-v2 explicit: **3 applicable walked** (each с decision tree, baseline, verification — LO8 coverage) + **4 case-study deep-dives** (для LO4 / LO5 / LO6 — narrative).

### Applicable walked examples (LO8 — Применять и создавать)

#### WE-1 (§1, s07) — Grant idea decision tree

**Контекст:** «Ваш научный руководитель просит идею для гранта в materials science. У вас есть выбор: Sakana AI Scientist v2 даст 50 candidates за вечер; ваш PhD-руководитель — 3 идеи за месяц. Что выбрать?»

**Walked 6-step decision tree:**

1. **Classify task** — open-world (novel idea generation в materials science = open-world поскольку «novel» по определению outside training distribution).
2. **Coverage check** — is materials science в Sakana training distribution? Public papers — да, но **novel directions** outside training mode. Hypotheses ≠ patterns mining.
3. **Verification path** — каждая Sakana hypothesis требует DFT calculation OR synthesis в lab. 50 candidates × 2 hours DFT each = 100 hours compute. Реалистично screen 10 candidates per week максимум.
4. **Ethical risk** — если используете Sakana output как hypothesis в grant proposal → ICMJE disclosure требование? IRB ↓ depends on institution. NSF AI Code of Conduct требует disclosure.
5. **HITL design** — AI screens 50 → human selects 5 (по domain expertise) → DFT validates 5 → 1-2 makes it в grant. Это **AI-augmented**, не «AI generates grants».
6. **Submission integrity** — disclose AI use в proposal narrative; cite Sakana version + date; explain human-AI division of labor.

**Outcome:** не replacement руководителя, но **augmentation 50→5 candidate filtering**. Time saved = ~3 weeks; quality gain depends on human selection.

**Baseline counter-claim:** до Sakana — PhD-руководитель + grad student brainstorm — 3-5 ideas / month at $50k salary. Sakana — 50 ideas / evening at $200 API cost. **But ≥45 of 50 are noise** (per Sakana own disclosure). Effective rate similar.

#### WE-2 (§4, s28) — Collaborator bibliography 4-step verification

**Контекст:** «Коллаборатор присылает paper draft с LLM-generated bibliography 47 citations. Co-author position предлагается. Что делать?»

**Walked 4-step verification workflow:**

1. **DOI-resolve каждую цитату.** Open arXiv / DOI / Crossref. **Time:** ~10 минут для 47 cites при tooling (Zotero auto-resolve). **Fail criteria:** ≥3 fake DOIs → STOP, refuse to co-author.
2. **Проверить relevance к claim** (random sample 10 of 47). Прочитать abstract + relevant section; verify что цитата supports claim в draft. **Time:** ~30 минут. **Fail criteria:** ≥3 «irrelevant cites» → STOP, raise concerns.
3. **GPTZero analysis на drafting style.** Run bibliography section + introduction + conclusion through GPTZero. Если ≥70% «likely AI-generated» — это signal что collaborator не verified manually. **Time:** 5 минут.
4. **Request raw source documents** от collaborator (PDF copies of key 10 papers). Если refused → STOP, **refuse to co-author**. Это red flag indicating collaborator не has source material himself.

**Outcome decision tree:**
- Все 4 steps pass → co-author OK с disclosed AI-tools-used в author notes (ICMJE compliance).
- Step 1 fails (fake DOIs) → escalate to PI / journal editor; не co-author.
- Step 2-4 fail → request rework + verify; не co-author until corrected.

**Baseline counter-claim:** до 2023 manual bibliography prep — ~4 hours для 47 cites; LLM-generated draft → 5 minutes; **verification overhead — 45 минут**. Net time save vs manual = ~3 часа per paper, но only if verification done properly.

#### WE-3 (§5, s34) — Catalyst pipeline (propylene oxidation specific)

**Контекст:** «Ваш научный руководитель просит: "построй AI-pipeline для предсказания свойств новых катализаторов propylene oxidation"». **Domain-honest:** propylene oxidation = closed-world задача (catalysis = quantum chemistry well-defined).

**Walked 5-step framework:**

1. **Classify task** — closed-world (catalysis governed by DFT + thermodynamics; outputs verifiable through synthesis).
2. **Map alternatives** — (a) DFT first-principles (Vienna ab initio Simulation Package, **>50 лет theory**), (b) GP-BO over reaction parameter space (**40-60 лет**), (c) GNoME-style ML inverse design (foundation model, 2023+).
3. **Apply 4 criteria** — training coverage есть (Materials Project + Open Catalyst Project, 1.2M datapoints); verifiability есть (synthesis в lab, characterization); ethics OK (no IRB issues); training distribution: propylene oxidation underrepresented vs general transition metal catalysis — **flag risk**.
4. **HITL design** — AI screens 5000 candidates (GNoME-style) → human selects top 50 (по synthesizability + cost-of-precursors) → DFT validates 50 (1 week, 50 GPU-hours) → top 10 → synthesis в lab confirms 3.
5. **Pre-publication verify** — для каждого claimed «novel catalyst» property: (a) DFT energy stability calculation; (b) synthesis в lab; (c) XRD characterization; (d) catalytic activity test. **All 4 confirmed** до paper submission.

**Baseline counter-claim:** до AI screening — manual literature + intuition-driven trial-and-error = 1-2 candidates synthesized per PhD year. AI-screening + HITL = 3 candidates per quarter (4× speedup, **with verification gates**). Without HITL → Palgrave critique repeats (35 of 36 «novel» were derivatives — see s17).

### Case-study deep-dives (LO4 / LO5 / LO6 — narrative)

#### Case 1: AlphaFold 2 → AlphaFold 3 → Nobel Prize Chemistry 2024

**Кто/где/когда:** DeepMind / Isomorphic Labs; AlphaFold 2 (2020) → AlphaFold 3 (8 мая 2024, Nature paper) → Нобелевская премия по химии (**9 октября 2024**, Stockholm).
**Измеримый результат с baseline:** AlphaFold 2 на CASP14 (декабрь 2020) — median GDT_TS ~92; baseline до AF2 — лучшие методы ~60 GDT_TS = **+53% improvement vs prior best**. AlphaFold 3 для protein-ligand interactions: +50% accuracy vs prior best. AlphaFold DB: 200M+ predicted structures publicly available; baseline до AlphaFold — PDB ~200k experimentally solved structures = **1000× больше structures** (predicted).
**Источник:** Nature paper Jumper et al. 2021, Abramson et al. 2024; nobelprize.org.

#### Case 2: AlphaProof + AlphaGeometry 2 — IMO 2024 silver

**Кто/где/когда:** DeepMind, июль 2024.
**Измеримый результат с baseline:** IMO 2024: **28/42 points = silver medal level** (4 of 6 problems). Baseline до этого: AI не доходил до bronze (12/42). AlphaProof решил **сложнейшую проблему турнира** (только 5 человек её решили). **But:** 4+ hours per problem vs human 90 min; AlphaProof + AG2 на 1 балл ниже gold cutoff.
**Источник:** DeepMind blog, Nature paper 2025, arxiv 2502.03544.

#### Case 3 (Mixed): GNoME + A-Lab Berkeley + Palgrave critique

**Кто/где/когда:** DeepMind GNoME (Nature ноябрь 2023) → A-Lab Berkeley synthesis (Nature ноябрь 2023, **Szymanski et al. doi.org/10.1038/s41586-023-06734-w**) → Palgrave-Schoop critique (**ChemRxiv январь 2024**).
**Измеримый результат с baseline:** GNoME: 2.2M predicted materials, 380k stable; baseline — Materials Project ~50k materials с DFT = **44× больше candidates**. A-Lab: **41 of 58 target compounds synthesized in 17 days** (P0-3 canonical, was 36/57 — wrong in v1). Manual chemistry baseline: один target — недели до месяцев работы PhD. **Palgrave critique (P1-10):** examined **36 success samples, found 35 of 36 had errors**: incorrect crystal structure assignment, derivatives mislabeled as novel, no demonstrated functionality.
**Источник:** Merchant et al. (Nature 2023), Szymanski et al. (Nature 2023), Palgrave-Schoop ChemRxiv 2024.

#### Case 4 (Failure cluster): Galactica + Frontiers + NeurIPS + Sakana

**Galactica (Meta, 15-17 ноября 2022):** demo жил 3 дня; false science claims, bomb-making instructions, fabricated citations. Source: MIT Technology Review (Heaven 2022), arxiv 2211.09085.

**Frontiers «крыса» retraction (февраль 2024):** опубликовано 13 февраля → retraction 16 февраля (3 дня). Rat anatomy via Midjourney; «protemns» / «zxpens». IF >5 indexed journal. Source: phys.org, VentureBeat 2024.

**NeurIPS 2025 fake citations:** 100+ fake citations в 53 papers of NeurIPS 2025 (15 000 submissions, 24.52% acceptance, ~3 700 accepted). Source: arxiv 2602.05930, GPTZero analysis.

**Sakana AI Scientist v2 (апрель 2025):** 1 of 3 papers passed ICLR 2025 workshop peer review (scores 6, 7, 6 = 6.33 average, 55th percentile). Cherry-pick mechanics (P2-2): Sakana writes ~100 papers per cycle; human curator selects 3 to submit. External audit показал «hallucinations, faked results, overestimated novelty». Source: Sakana blog 2025, TechCrunch March 12 2025, arxiv 2504.08066.

---

## Российский контекст AI-в-науке (~5 мин в s37)

**Owner decision #4:** глубже — 2-3 кейса × ~5 мин. **0 named universities** (no МГТУ / Сколтех / ВШЭ / РАН). **Brand-whitelist OK:** AIRI / Sber AI Lab / Yandex Research / РНФ / AI Russia 2030 Strategy.

### Case A — AIRI (Институт искусственного интеллекта)

**Гloss:** AIRI — Институт искусственного интеллекта (Россия, основан 2021). **AI4Science research direction:** работа в protein structure prediction (open-source AlphaFold-clones), medical imaging, climate modeling. Publications в Nature, Nature Communications 2024-2025 (cite: arxiv, AIRI press). **Adoption-направление:** **emerging research; не production-scale yet**. **Failure / limit:** AIRI focus — papers, не industrial deployment; gap между research output и industry usage в РФ.

### Case B — Sber AI Lab

**Gloss:** Sber AI Lab — research направление в Сбере. **AI4Science applications:** scientific tools для climate modeling, energy demand forecasting; collaboration с research институтами. **Adoption-направление:** **корпоративный R&D + research grants**. **Failure / limit:** Sber AI Lab focus примарно на банковские / корпоративные tasks; AI4Science — secondary; ограниченная open-source publication relative to Yandex Research.

### Case C — Yandex Research

**Gloss:** Yandex Research — academic publications + open-source models (YaLM, RuGPT family). **AI4Science contributions:** YaLM-family models used в Russian academic research; open weights enable RU-language scientific writing tools. **Adoption-направление:** **mainstream в Russian academic community; growing internationally**. **Failure / limit:** YaLM-100B (2022) — open weights, but training data primarily Russian/English internet; not specialized for scientific domains (vs Galactica's focus on papers — но Galactica retraction shows that approach risks).

### Regulatory / funding frame

- **РНФ AI4Science grants 2024-2025** — Российский научный фонд выделил отдельный приоритет на AI4Science проекты; ~20-30 грантов annually (~₽5-15M each). **Pedagogical context.**
- **AI Russia 2030 Strategy** — Указ Президента РФ № 145 (национальная стратегия развития ИИ до 2030 года) — научные применения попадают в приоритеты «новые материалы», «биомедицина», «энергетика».

### Failure / limits в RU context

- **Compute gap:** российские исследователи имеют ограниченный доступ к large GPU clusters; AlphaFold 3 / GNoME-style training в РФ — ограниченно (требует $1M+ compute).
- **Citation visibility:** Russian-language papers underrepresented в Semantic Scholar / Google Scholar — это limit на «LLM literature review» tools (которые тренируются на English-dominant corpus).
- **Open-source dependency:** российские исследователи широко используют AlphaFold / Boltz-1 / NotebookLM — но **создание independent foundation models** уровня DeepMind / OpenAI пока вне reach.

**Pedagogical lesson:** студент-инженер в РФ → знает classical методы (BO / DFT / OR-Tools = mainstream globally and в РФ) + использует open-source foundation models (AlphaFold, Boltz-1) + следит за AIRI / Sber AI Lab / Yandex Research publications + понимает compute / data / regulatory limits.

---

## Часть 2 — продолжение в `plan-v2-part2.md`

В части 2 — оставшиеся разделы плана (см. полный TOC ниже):

- § Провалы, ограничения и альтернативы (ENFORCED ≥30%)
- § Sections roadmap
- § Numbers convention lock (25 canonical claims)
- § Russification таблица (28 entries)
- § Media plan ≥50%
- § Hero plan для s01 + s39 (краткий) — см. также § «Hero design mitigation strategy» в части 1
- § Сравнение vs Lec-{N-1}, Lec-{N-2}
- § Anti-dependencies (vs lec-12/13/14/16/7)
- § Anonymization
- § Risk register (14 rows)
- § Plan-level mandates carry-forward checklist
- § Self-check
- § Длина plan'а
- § Phase 2 chapter brief carry-forward (rewritten 600+ words)
- § Open questions для owner (closed)

**См.** `plan-v2-part2.md`.

