# Reader Text-Only Report — Лекция 15 (plan-v1) — 2026-05-27

**VERDICT: APPROVE-WITH-POLISH**

(Plan is structurally strong, central question clear, keystone choice defensible. Главные issues — terminology overload в §2-3 без inline glossary, и §4 «8 минут подряд failure» pedagogically heavy. Не REVISE — base structure не нужно перестраивать; список конкретных fixes ниже.)

---

## First impression (3-4 sentences)

Открыл план и сразу понял две вещи: «AlphaFold-Nobel рядом с Galactica-shame» — это **сильный hook**, я моментально вижу tension лекции. Тема «AI в науке» казалась расплывчатой до того, как я прочёл keystone Variant A — «лестница 6 ступеней цикла» — после этого я могу представить, **о чём каждый раздел**. Однако к Разделу 2 я уже встретил ~12 незнакомых названий (CASP, GNoME, MatterGen, Boltz, A-Lab, Aurora, GraphCast, Pangu, FourCastNet, AlphaProof, FrontierMath, IDP) — и боюсь, что **на лекции я не успею всё это «уложить»**. Раздел 4 (Write+Review) после трёх case-heavy разделов читается как «8 минут провалов подряд» — структурно мощно, но pedagogically тяжело.

---

## Mental hooks formed (3-5 items — что я унёс из чтения plan'а)

1. **«Две стороны медали»**: AI в науке = Нобелевский прорыв (AlphaFold) **и одновременно** академический позор (Galactica, paper mills, fake citations в NeurIPS). Это не два разных лагеря — это **одна реальность**.
2. **«Лестница 6 ступеней»**: Hypothesis → Design → Experiment → Analyse → Write → Review. AI на каждой работает **по-разному**: где-то breakthrough, где-то augmentation, где-то vetoed. **Это диагностический инструмент**, который я могу применить к своему research-таску.
3. **«Closed-world vs open-world»**: AI надёжно работает там, где есть verifiable ground truth (fold проверяется кристаллографией, weather — через 24 часа). Там, где нет — AI hallucinates. *(Note: я понял это как parallel concept к Variant B, но даже в Variant A plan'е этот фильтр упоминается как «keystone критерий A» в s32, что хорошо.)*
4. **Peer review — это **критически человеческая** задача**. NeurIPS 2025: 100+ fake citations в принятых статьях. Это страшно — значит **завтра я могу столкнуться с LLM-generated bibliography от коллаборатора**. Что делаю? Проверяю каждую цитату через DOI.
5. **Альтернативы существуют и они зрелые**: Bayesian Optimization 30+ лет, DFT/MD first-principles для chemistry, classical signal processing для LIGO. **AI — не всегда правильный инструмент**, даже когда модно.

---

## Confusions / undefined terms

### P0 — критические (нужен inline glossary до или при первом упоминании)

1. **CASP** (упоминается в Worked example 1, GDT_TS metric). У меня **нулевой контекст**. Что это? Что значит «median GDT_TS 92»? Откуда я знаю, что 92 >> 60? Нужна одна фраза: «CASP — биеннальное соревнование по предсказанию белковых структур; GDT_TS — метрика accuracy 0-100».
2. **IDP (intrinsically disordered protein)** (s23, Worked example 1 anti-hype). Я не знаю, что такое «intrinsically disordered region»; почему 22% hallucination там — это failure? Нужна фраза: «IDP — белки/области, не имеющие стабильной 3D-структуры; принципиально другой класс задачи».
3. **DFT / MD** (упоминается 6+ раз как «альтернатива»). Я не знаю, что DFT = Density Functional Theory, MD = Molecular Dynamics. Если это **основная альтернатива в s24, s33, s34**, я должен понимать, что это **first-principles quantum chemistry simulation**, не «другой ML».
4. **Bayesian Optimization + Gaussian Process** (s11, s33, s34) — упоминается как «классическая 30+ лет методика». Что она делает? Что значит «design-of-experiments»? Без 1-2 строк объяснения я воспринимаю это как «ещё одно непонятное название».
5. **«Closed-world / open-world»** в Variant A (s32 категория A). В plan'е объяснено в Variant B (keystone alternative), но если **владелец выбирает Variant A**, то в s32 этот термин используется **без предварительной motivation**. Нужно ввести его раньше — где-то в s03 (keystone slide) или s04 (glossary slide есть, но в plan'е перечислены только акронимы, не категории).

### P1 — желательны (создают friction, но не блокируют)

6. **A-Lab Berkeley** — я не знаю, что такое «automatic synthesis lab». Lab? Что робот делает? Один screen-shot или схема нужны (это в media plan уже есть, но в plan'е narrative я не понимаю, **что именно автоматизировано**).
7. **Coscientist** (CMU Boiko) — vs DeepMind Co-Scientist. Это **разные** системы (CMU 2023 vs DeepMind 2026), названия путаются. Нужно явно: «Coscientist (CMU, 2023) — не путать с Co-Scientist (DeepMind, 2026)».
8. **FrontierMath** — упоминается как «<2% → 52%», но я не знаю, **что это за benchmark**. Кто его делает? Какие задачи? Одна фраза в glossary.
9. **ECMWF** — «Aurora операционно в ECMWF с 2026». ECMWF — что это? Если это weather forecasting agency, скажи это явно.
10. **ICMJE** — «AI не может быть автором». Кто этот ICMJE и почему его правила обязательны? Одна фраза.
11. **Boltz-1 / Boltz-2** vs AlphaFold 3 — я понимаю, что Boltz — open-source альтернатива, но **что именно она делает по-другому**? Если она «уже most-used model in своём классе», то почему AlphaFold ещё нужен?
12. **«Replicability crisis»** — упоминается с числами (psychology 36%, economics 61%) в § failure-bucket, но **не объяснено, что это такое** в narrative plan body.

### P2 — мелочи (не критично)

13. **Allen Institute MICrONS** — «1 cubic mm mouse visual cortex». Зачем? Что это решает? (это deep, не для plan'а; для chapter — OK).
14. **«Peer review hallucinations»** — звучит как oxymoron. Имеется в виду, что AI-сгенерированные reviews hallucinate? Или что peer reviewers пропускают halluc'ы? Двусмысленно.

---

## Narrative flow concerns

### Concern 1: §2 — terminology overload (P0)

15 мин, 8 слайдов (s12-s19), и в нём упомянуты:
- AlphaFold 2 + 3 + DB + Multimer
- Boltz-1, Boltz-2
- GNoME + A-Lab + Palgrave critique
- MatterGen
- Aurora + GraphCast + Pangu + FourCastNet + ECMWF
- AlphaProof + AlphaGeometry 2 + IMO + FrontierMath
- CASP, GDT_TS, IDP

Это **15-20 новых названий за 15 минут**. На лекции я **гарантированно** потеряю нить. План §2 нужно либо **сократить** (один представитель weather моделей, не 4), либо явно **сигнализировать «это список, запомни 3 имени из этих 20»** (как 14-я лекция делала с MITRE ATLAS — она хорошо явно выделяла главное). На plan'е я не вижу, **что я должен запомнить из §2 как минимум**.

### Concern 2: §4 — 8.5 мин failure подряд (P1)

Раздел 4 — failure-share 70.8%. Sliding: NotebookLM (positive 2 мин) → Frontiers крыса → NeurIPS fake citations → Sakana → ICMJE rule. Это **8 мин строгого failure**. На лекции я устаю как студент: «AI плохой, AI плохой, AI плохой». Pedagogically это сильно (mission course: «AI ≠ магическая пилюля»), но **flow** становится heavy. Идея: добавить в начало §4 одну явную позитивную ноту: «Elicit/Consensus — реально работают и я лично использую — НО (failure cluster)». Сейчас в plan'е это есть в s26-s27, но в одну строку «augmentation, не synthesis». Если **развернуть позитив** до 3 мин, и сократить failure cluster до 7 мин — будет более balanced.

### Concern 3: §5 — 87.5% failure-share, но это **именно полезная часть** (нет P)

§5 — 10.5 мин failure-strict из 12. Я читаю plan и **не устаю** — потому что это **критерии и альтернативы**, не «ещё провал». Это actionable framework. Здесь high failure-share OK, потому что качество failure-bucket'а **applicable**, не narrative. Сильная часть лекции.

### Concern 4: Hero «две сторон медали» — рискованный визуал (P1)

Side-by-side hero (Nobel + Galactica) — *концептуально* сильный, но **визуально может выглядеть слабо**: одна половина — официальная Nobel photo (royal venue, формальная), другая — screenshot заголовка статьи. Это **разные жанры**. Я представляю s01 — это будет «политипажный коллаж». Backup в risk register (R1) — switch на single AlphaFold ribbon — может быть **лучше**. Не обязательно делать «обе стороны на cover»; концепт «двух сторон медали» можно ввести **на s02-s03** через текст, а на s01 — single strong hero.

### Concern 5: 3 keystone варианта в plan'е — для меня **избыточно** (P2)

Я как читатель plan'а вижу 3 варианта keystone и теряюсь: **какая лекция будет на самом деле?** Это decision для владельца, но для меня (reader) это создаёт неопределённость о content'е. Если возможно — после Phase 1 critique владелец **решает**, и в plan-v2 остаётся **один** keystone (с pp-1 предложением «отвергнутые варианты см. archive»).

### Concern 6: §3 (Analyse) — feels тонким (P2)

12 мин на «AI в data analysis» — exoplanet detection + Allen brain map + LIGO + AlphaFold IDP + альтернативы + worked example. Это **5 разных доменов** за 12 мин. Каждый из них достоин full slide (хорошо), но **связь между ними не очевидна**. Что эти 3 успеха объединяет? «Закрытые задачи с большим dataset». Если эта **общая mental model** не введена явно в начале §3, разные кейсы выглядят как list.

---

## What I'd want before lecture (gaps in prerequisites)

1. **Краткое введение в peer review** (что это процесс, как работает, что значит «прошёл peer review» vs «препринт»). У меня **общее представление**, но specific facts (acceptance rates, double-blind, reviewer scores 1-10) я не знаю. Без этого §4 (Write+Review) теряет depth.
2. **Что такое replication crisis** (одна страница) — это общенаучный контекст, и план ссылается на него (psychology 36%, economics 61%, AI/ML 24-50%) без объяснения, почему это важно для AI-in-science.
3. **Базовое представление DFT / MD / first-principles** — если §5 (когда AI не нужен) опирается на «классическая физика лучше» как альтернативу, я должен знать, что **классическая физика дешевле + объясним + точнее чем ML**, и почему. Это 1-2 параграфа.
4. **AlphaFold timeline** (2018 CASP13 → 2020 CASP14 → 2024 AF3 → Nobel) — я знаю что AlphaFold революционен, но **хронологии не помню**. Одна visual timeline (это в media plan, s14 — open-source debate timeline; добавить **сюда же** или в s12 общую AlphaFold timeline).
5. **CASP benchmark + GDT_TS metric** — без этого я не понимаю baseline в Worked example 1. Это можно объяснить **через GDT_TS как «accuracy метрика 0-100, где 100 = perfect match»** в одной фразе.
6. **Что такое Lean (formal math interface)** в Worked example 2 (AlphaProof). «AlphaProof — RL-based formal math reasoning (interface с Lean)». Lean — это что? Programming language? Theorem prover? Одна фраза.

---

## Specific recommendations для revision

### P0 — обязательно ДО Phase 2 (book-editor)

**P0.1.** Расширить **s04 glossary** до 12-15 терминов (currently 6-8). Добавить inline definitions для:
- CASP («биеннальное соревнование по предсказанию белковых структур»)
- GDT_TS («метрика accuracy в CASP, 0-100, где 100 = perfect match»)
- IDP («intrinsically disordered protein — белок/область без стабильной 3D-структуры»)
- DFT / MD («Density Functional Theory / Molecular Dynamics — first-principles quantum chemistry simulation»)
- Bayesian Optimization + Gaussian Process («байесовский поиск оптимума в design-of-experiments»)
- ECMWF («European Centre for Medium-Range Weather Forecasts — operational forecasting hub»)
- FrontierMath («Epoch AI benchmark высшей математики, 100+ задач, человек-эксперт ~20%»)
- ICMJE («International Committee of Medical Journal Editors — устанавливает правила авторства»)
- closed-world / open-world (введённый явно как **педагогический термин** независимо от выбора keystone)

**P0.2.** В §2 (Experiment) явно сигнализировать «что запомнить минимум»:
- AlphaFold 2/3 (один — Nobel-tier breakthrough)
- GNoME + A-Lab (один пример claims vs critique)
- Aurora (weather, один пример operational AI)
- AlphaProof (один пример formal math)
- **4 имени, не 20.** Остальные — «вот ландшафт» для chapter, не для memorization.

**P0.3.** Coscientist (CMU) vs Co-Scientist (DeepMind) — явное disambiguation в plan body. Сейчас они появляются в разных слайдах (s07 vs s09), но я **пропустил различие** при первом чтении.

### P1 — желательно в plan-v2

**P1.1.** Решить keystone (Variant A / B / C) **до plan-v2 finalize**. План с 3 вариантами для reader — избыточный.

**P1.2.** §4 rebalance — положительную часть (Elicit/Consensus/NotebookLM useful) развернуть до 3 мин (currently ~1.5); failure cluster сократить до 7-7.5 мин. Сохраняет ≥50% failure-share, но добавляет «positive ground» before negative deep-dive.

**P1.3.** §3 — общее introductory предложение **что объединяет 3 кейса** (exoplanet + brain + LIGO). Например: «На фазе Analyse AI работает там, где данные большие + задача узко определена + ground truth доступен. Все 3 кейса — именно такие».

**P1.4.** Hero s01 — re-think «две стороны медали». Рассмотреть **single hero AlphaFold ribbon** + concept «двух сторон» вводится **на s02 или s03** через text + side-by-side small visuals. Тяжелее backup-plan, но визуально cleaner.

**P1.5.** Worked example 2 (AlphaProof IMO silver) — упомянуть что **Lean — это** (proof assistant / formal language), иначе reader не понимает, что значит «formal math reasoning».

**P1.6.** В s32 (4 категории критериев) явно label закрытый/открытый мир как **A**, и в s04 glossary его определить независимо от Variant A/B choice. Тогда reader понимает термин **из любого варианта keystone**.

### P2 — nice-to-have

**P2.1.** Open question #4 (Sakana s10 + s30 merge или нет) — рекомендую **merge**. Currently два слайда о Sakana (s10 deep-dive criticisms, s30 ICLR workshop). Один deep-dive слайд (s30 расширенный) — sufficient; s10 заменить на **общий summary of hypothesis-gen failures** (включая Sakana как один пример).

**P2.2.** Open question #5 (Co-Scientist Nature May 2026) — keep как secondary mention (one slide s07). Если retract до лекции — orchestrator updates 1-pager. Не первичный кейс, как **рамкой**, не как core proof.

**P2.3.** «AI peer review hallucinations» в s30 — переименовать, потому что это **двусмысленно**. Явное: «AI-generated reviews содержат hallucinated points» — это другое явление, чем «reviewers пропускают halluc'ы в reviewed papers». Plan смешивает оба (s29 — fake citations в submitted papers; s30 — Sakana hallucinates в auto-reviewing своих papers). Разделить эти 2 failure mode явно.

**P2.4.** §6 closing — «завтра коллаборатор даёт LLM bibliography. Что делаете?» — отличный actionable hook. Сделать это **прямо текстом на s38**, не narration-only.

---

## Сводка

- **Slides с P0 issues:** 5 (s04 glossary insufficient; s12-s19 §2 terminology overload; s23 IDP без context; s24/s33/s34 DFT/MD/BO без intro; s32 «closed/open-world» term unanchored if Variant A keystone).
- **Slides с P1 (понятно с трудом):** 4 (s01 hero pattern; §3 connection unclear; §4 imbalanced; Coscientist vs Co-Scientist confusion).
- **Slides с P2 (мелочи):** ~6 (Allen MICrONS context; replicability crisis intro; Lean intro; Sakana s10+s30 merge; «peer review hallucinations» wording; s38 explicit text).

### Топ-5 fixes до Phase 2

1. **Expand s04 glossary** to 12-15 terms with inline definitions (CASP, IDP, DFT, MD, BO+GP, ECMWF, FrontierMath, ICMJE, closed/open-world).
2. **§2 явно label «3-4 имени запомнить минимум»** — иначе terminology overload убивает retention.
3. **§4 rebalance** — positive ground 3 мин + failure cluster 7-7.5 мин (currently 1.5+8.5 = pedagogically heavy).
4. **Keystone choice locked** до plan-v2 (Variant A рекомендую — самый интуитивный; «closed/open-world» становится sub-concept в s32).
5. **Disambiguate Coscientist (CMU 2023) vs Co-Scientist (DeepMind 2026)** — явная callout в s07/s09.

---

## Self-containedness note (как студент через 2 недели — text-only режим)

В text-only режиме это **plan**, не chapter и не лекция, поэтому 2-weeks-after test не полностью применим. Тем не менее: если бы я через 2 недели читал ТОЛЬКО этот plan body — **я понял бы central question + keystone + 5-step framework** (это сильно). Я **НЕ** восстановил бы детали §2 (15-20 названий без glossary) и §3 (3 домена без unifying mental model). §4-§5 — applicable framework — retention OK. **Self-containedness estimate plan'а: ~70% при условии что keystone locked.**
