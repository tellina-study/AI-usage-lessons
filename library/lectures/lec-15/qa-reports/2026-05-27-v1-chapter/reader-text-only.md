# Reader Text-Only Report — Лекция 15 chapter v1.0 — 2026-05-27

**VERDICT: APPROVE-WITH-POLISH**

Read in `text-only` mode as 3rd-year ИУ6 МГТУ engineering student doing self-study (без преподавателя). 3 files, ~28 600 слов total.

---

## 1. Verdict rationale

**APPROVE-WITH-POLISH**, не APPROVE-CLEAN. Главу можно отдавать в Phase 3 critic-review и переходить к рендеру, но в текущей версии есть P1-вещи, которые я **сам бы хотел увидеть починенными до того, как меня заставят это читать самостоятельно**. Большинство P1 — это (а) терминологические скользкие места, где мне нужно лазить за определением, (б) места, где сами WE-3 / §3 чрезмерно chemistry-heavy для универсального инженера-3-курсника, (в) поразительное количество англицизмов в тексте — особенно во второй половине Части 2 и Части 3.

Главное: **я понимаю керистоун, я понимаю центральный вопрос, я могу ответить на self-check, я могу применить framework к своей задаче**. Это основной критерий пригодности материала для self-study, и он выполнен. Поэтому не REVISE.

Но: chapter ощущается **отчётливо двухсортным**. Часть 1 (Введение + §1 + §2) — отшлифованная, читается как textbook. Часть 2-3 — менее polished, plenty англицизмов, иногда страдает структура абзацев. Это не блокер, но это polishing work.

---

## 2. First impression (per файл, 3-4 предложения каждый)

### Часть 1 (chapter.md, ~13 200 слов)

Открыл — увидел длинную, но логично разбитую структуру с TOC. Hook «9 октября 2024 / 17 ноября 2022» зацепил **сразу** — это два конкретных события, которые я могу запомнить, а не абстракции. Sakana как «третья сторона медали» — appreciated, потому что без неё была бы примитивная дихотомия «good AI / bad AI». Glossary из 15 терминов в §0.4 — нормально, но **я бы хотел его в виде таблицы**, а не нумерованного списка — текущий формат сложно перечитывать. Керистоун (лестница цикла) понятен с первого захода, и сразу даётся critical distinction «лестница циклична, не линейна» с явным контрастом с lec-13/14 — это полезное упоминание для меня как студента, который только что прошёл эти лекции.

### Часть 2 (chapter-part2.md, ~10 000 слов)

§3 (Analyse) — **скучнее** чем §2, но это **по делу**. Автор сам пишет «Этот раздел отличается по тону: меньше скандалов, больше повседневной утилитарности» — и это honest. Я не ожидал драматизма от exoplanet CNN. §3.5 (AlphaFold IDP deep-dive) — это перекрытие с §2.1, перечитал ту же информацию дважды, **слегка раздражает**. §4 (Write+Review) — попал в **сильное место главы**: Frontiers крыса + NeurIPS fake citations + Sakana = три кейса подряд, эмоционально насыщенные, я **помню детали**. WE-2 (collaborator bibliography) — самый actionable example, я могу его сделать завтра.

### Часть 3 (chapter-part3.md, ~9 000 слов)

§5 — **payoff раздел**. Здесь синтез всего предыдущего в applicable framework. 5-step framework + 3 questions к вендору — это то, что я унесу из лекции в реальную работу. WE-3 (propylene oxidation) — chemistry-heavy и **я следил с трудом**, но general logic читается. §5.6 (Russian context) — отдельный, выделенный, **достаточно honest** в признании compute gap / citation visibility / open-source dependency. Замыкание §6 + Personal pledge + Reflection prompt — emotional anchor работает. Q&A backup — 18 вопросов, в среднем 50-100 слов, **я не скучал**. Источники — list of ~70 visible (заявлено ~120), нормально, но **inline DOI ссылки могли бы быть более consistent**.

---

## 3. Mental hooks formed (что я унёс из главы)

Я попробовал перечислить, что я **бы вспомнил через 2 недели после прочтения, если бы мне дали blank sheet**:

1. **Лестница научного цикла из 6 ступеней (Hypothesis → Design → Experiment → Analyse → Write → Review), циклична, не линейна.** + matrix «augmentation / autonomous / vetoed» применима к каждой ступени.
2. **AlphaFold = Nobel 2024 (Бейкер + Хассабис + Джампер), AlphaFold DB = 200M структур vs PDB = 200k экспериментальных за 50 лет (×1000 acceleration); НО fold ≠ function + IDP ~22% галлюцинаций.**
3. **A-Lab Berkeley: 41 of 58 за 17 дней + Palgrave-Schoop critique: 35 of 36 имели ошибки.** Это canonical парадоксальная пара — prediction ≠ discovery.
4. **Frontiers «крыса» + NeurIPS 100+ fake citations: AI-generated content проходит peer review.** Verify, verify, verify — особенно citations через DOI.
5. **5-step framework: classify → map alternatives → 4 criteria → HITL design → pre-publication verify.** Альтернативы: BO/GP, DFT/MD, classical statistics, OR-Tools, human peer review.

Дополнительные hooks (помню частично):
- Sakana cherry-pick 100→3 = не autonomous, AI-augmented с heavy human gate.
- AlphaProof IMO silver — но 4+ часа на задачу vs 90 минут у человека; FrontierMath 2% → 52% за 18 месяцев.
- Aurora 5000× быстрее ECMWF, но ECMWF не deploy (data assimilation + extreme weather + operational reliability).
- WE-2: 4-step verification — DOI resolution, sample 10 relevance, GPTZero, request raw PDFs.
- ICMJE: AI не автор, disclosure обязательна.

Это сильное retention. Большинство hooks **single-sentence reproducible**, что есть характеристика хорошего pedagogical material.

---

## 4. Confusions / undefined terms

### Termings, где я споткнулся

**P0 — undefined / нужно лезть наружу:**

1. **GDT_TS** (§2.1) — определено внутри текста как «Global Distance Test Total Score», и описан смысл «100 = идентичность, 90+ = на уровне эксперимента, 60 = общая форма». **OK**, но это происходит **в середине абзаца**, и я бы предпочёл inline-callout «GDT_TS = ...» более явно. Прохожий читатель может пропустить.
2. **pLDDT** (§2.2) — определено как «predicted Local Distance Difference Test, 0-100», но это **второе** изобретение в той же главе после GDT_TS — два очень похожих acronym в одном разделе слегка путают. Я бы поставил inline disclaimer «pLDDT — это **per-residue confidence**, в отличие от GDT_TS, который measures overall accuracy против эксперимента».
3. **Lean** (§2.7) — упомянуто как «формальный язык математики», но **не объяснено**, что это такое, кто его сделал, почему он formal. Я не знаю Lean. Мне нужно ~1 предложение «Lean — это **proof assistant** (формальный верификатор доказательств), разработанный Microsoft Research; программа автоматически проверяет, что доказательство строго следует из аксиом».
4. **conformal prediction** (§3.4) — определено как «statistical method для uncertainty quantification», и есть пример с 95% confidence interval. Но это всё ещё **новое для меня имя** — я бы хотел знать, **чем оно отличается** от классических confidence intervals (которые я знаю из статистики). Одно предложение про distribution-free nature было бы полезным.
5. **acquisition function / Expected Improvement / Upper Confidence Bound** (§1.6) — упомянуто mimocходом без определения. Я знаю, что такое функция, но **что именно «Expected Improvement» вычисляет** — не очевидно из текста. Это **deep mathematics**, и автор, видимо, считает их за «known terms», но я как студент-инженер не уверен, что мне их объясняли в курсе.

**P1 — defined только in passing:**

6. **MSA (multiple sequence alignment)** (§2.1) — упомянуто как «proxy для evolutionary information» с пояснением через «co-evolution signals». Я понял **что это делает**, но **что это такое технически** (как алгоритм) — нет. Одного предложения «MSA — это таблица аминокислот, где строки = гомологичные белки разных организмов, столбцы = эволюционно соответствующие позиции» хватило бы.
7. **homology modeling / ab initio folding** (§2.1) — определены через сравнение, но это сравнение **очень техническое**, и я не уверен, что понял разницу полностью. Если автор хотел дать context до AlphaFold 2, хватило бы простой схемы «два пути: либо копировать готовую structure похожего белка (homology), либо считать physics с нуля (ab initio)».
8. **U-Net / transformer-based methods** (§3.3) — упомянуто как «specialized deep learning», но не объяснено, что U-Net — это специфическая CNN-архитектура. Я знаю transformers (lec-02), но U-Net — не уверен, что нам объясняли.
9. **conformal prediction в LIGO + general** (§3.4) — отдельно повторяется в широком контексте «calibrated confidence interval». OK, но **смешано с** general uncertainty quantification — что именно делает conformal prediction уникальным, остаётся unclear.
10. **GROBID + Crossref API** (§4.5) — это **technical detail** «automated citation verification implementation». Я не знаю GROBID. Для контекста этого раздела достаточно, но один-предложение gloss бы помог.

**P2 — мелкое:**

11. **VASP, Quantum ESPRESSO** (§5.3) — упомянуты как «industry standard DFT tools». Для меня (не chemist) это **просто имена**. OK для context.
12. **CGCNN** (§5.3) — Crystal Graph Convolutional Neural Network from MIT, brief gloss inline. OK.
13. **BoTorch, Ax** (Q17) — упомянуто как «BO library». Я бы как читатель ожидал ещё одно слово.

### Terms, где **glossary §0.4 сработал хорошо**:

- Foundation model, RAG, hallucination, peer review, reproducibility crisis, closed/open-world, IDP, ground truth, CASP, DFT/MD, BO/GP, ECMWF, FrontierMath, ICMJE, IMO. **Все 15 — действительно покрыты, и я мог бы их objaснить после первого прочтения.**

### Total verdict:

**~10 undefined / under-defined terms**, в основном domain-specific (Lean, MSA, U-Net, conformal prediction, acquisition function, GROBID, VASP). Это **не блокирует** общее понимание, но **снижает self-study depth**. Если бы я готовился к РК — мне пришлось бы делать дополнительные lookup'ы.

---

## 5. Narrative flow concerns

### Где я скучал

- **§3.3 (MICrONS) + параллельные проекты (Brain Knowledge Platform + UCSF Allen 1300 mouse brain) one-liner.** Я понимаю, **зачем** автор их упоминает (избежать confusion для студента), но это **сухая выгрузка трёх проектов**. Я бы их **сократил до одного предложения** или объединил в таблицу.
- **§3.4 (LIGO) — short секция, но повторяет ту же мысль «augmentation, not replacement».** Что и §3.2, и §3.3. К 3-му случаю я уже понял pattern; повторение не добавило.

### Где я запутался

- **§3.5 (AlphaFold IDP deep-dive)** — это **повторение** того, что уже было в §2.1 (inline callback) + §3 introduction (как cross-reference из §2). Я **дважды прочитал, что AlphaFold не работает на IDP**, прежде чем понял, что это намеренное повторение для §3.5 deep-dive. **Polish recommendation**: §3.5 stub должен начинаться с явного «в §2.1 мы упомянули... здесь deep-dive» — и **продолжать с deep technical content**, а не с переформулировки той же базовой мысли.
- **§5.6 Russian context** — структура «Case A / B / C» + «Regulatory frame» + «Limits» + «Pedagogical meaning» + «Concrete examples» — это **5 подразделов внутри одного §5.6**. Это **слишком много** для одного level-3 раздела. Я **потерял navigation** к концу. Рекомендация: разбить на §5.6.1 / .6.2 / .6.3 или сократить examples к 1-2.

### Где я был перегружен

- **§4 (Write+Review) — конец секции (§4.5 NeurIPS + §4.6 ICMJE).** Failure cluster (Frontiers + NeurIPS + Sakana boundary) идёт подряд **~5500 слов про negative outcomes**. Это **emotionally heavy**, и к ICMJE §4.6 я устал. **§4.6 могла бы быть короче** — 5 этических критериев + jurisdictional context + Sakana boundary case = ~1200 слов, можно сократить до ~700-800.
- **WE-3 (catalyst propylene oxidation, §5.3) — chemistry-heavy для универсального инженера.** Я следил **по общей логике**, но термины (Vienna Ab initio Simulation Package, Quantum ESPRESSO, BET surface area, gas chromatography, thermogravimetric analysis) — это **all chemistry vocabulary**, и я не уверен, что внутренне ими оперирую. **Рекомендация**: либо упростить chemistry до minimal-jargon level («GP-BO over 5000 candidates + DFT validation + lab synthesis — 4 months for 3 confirmed catalysts vs 1-2 per year manual»), либо явно пометить раздел «требует chemistry background».

### Где **flow работает отлично**

- **Часть 1 целиком** — Введение → §1 → §2 → переход к Части 2 — это **textbook quality**. Hook отлично, керистоун отлично, §1 (failure) → §2 (success) — правильная контрастная структура.
- **WE-2 collaborator bibliography (§4.3)** — 4-step framework + emotional setup («это неудобная ситуация») + decision tree outcomes — **the strongest walked example в главе**.
- **§6 Замыкание + Personal pledge + Bridge to Lec-16** — clean wrap-up, mental closure achieved.

---

## 6. Walked examples assessment

### WE-1: дерево решения «идея для гранта» (§1.5)

- **Applicable?** Да, но **partially**. Я **не делал** грантовое предложение, и контекст «у вас есть руководитель + дедлайн через 3 месяца» — это PhD/магистратура scenario, не bachelor 3-курсный. **Я бы applied к моей реальной ситуации** — например, выбор темы курсовой / магистерской.
- **Strengths**: 6-step decision tree clean, Baseline counter-claim («3-5 идей в месяц = $50k vs 50 за вечер = $200, но 45 шумом») — это **memorable framing**. Pedagogical insight в конце про «AI как expansion of search space» vs «AI как генератор готовых идей» — **прекрасный** distinction.
- **Weaknesses**: Шаг 4 (Ethical risk) ссылается на NSF AI Code of Conduct — для меня это **американская реалия**, не российская. Краткое упоминание Минобрнауки приказов было бы балансом.

### WE-2: collaborator bibliography 4-step verification (§4.3)

- **Applicable?** Да, **полностью**. Я могу применить **завтра**, как только меня позовут в research group. 4-step workflow конкретен, временные оценки даны (10/30/5 минут + request PDFs), fail criteria явные («≥3 fake DOIs → STOP»).
- **Strengths**: Лучший walked example в главе. Emotional setup («это неудобная ситуация, collaborator обычно senior») делает его memorable. Outcome decision tree (all 4 pass / step 1 fail / step 2-4 fail) — clean. Disclosure follow-up как additional consideration — appreciate.
- **Weaknesses**: Step 3 (GPTZero) — это **single tool reference**, и я знаю, что GPTZero имеет high false-positive rate. Автор сам признаёт это, но я бы предпочёл **2-3 alternative AI-text detectors** для cross-validation.

### WE-3: catalyst pipeline propylene oxidation (§5.3)

- **Applicable?** **Нет, прямо**. Я не chemistry-major; propylene oxidation для меня — это **слово**. **Логика workflow** (AI screens 5000 → human selects 50 → DFT validates 50 → lab confirms 3) — applicable как **мета-pattern**.
- **Translatable?** Да, если воспринимать как **HITL design pattern**, а не как конкретный chemistry workflow. Но текст пишется **с предположением chemistry literacy**, что для универсального студента-инженера не выполнено.
- **Strengths**: 5-step framework cleanly demonstrated. Realistic timeline (4 months for 3 catalysts vs 1-2 per year baseline) даёт concrete benefit number. HITL gates явные.
- **Weaknesses**: Слишком много chemistry terminology без gloss (VASP, Quantum ESPRESSO, BET surface area, gas chromatography, propylene oxide industrial scale). **Polish recommendation**: либо добавить «techniqueA — это [one-sentence gloss]», либо заменить на **более universal example** (например, machine learning pipeline для предсказания свойств композитных материалов — closer to универсальный инженер).

### WE-TESS: transit search 5-step framework (§3.7)

- **Applicable?** Partially. Astronomy domain, и я не astronomer, но **logic translatable**. 5-step framework — data overlap → label availability → compute cost → baseline → held-out validation — это **универсальный pattern** для любого ML deployment decision. Автор явно пишет «applicable to ANY ML deployment in new domain» в конце.
- **Strengths**: 5-step framework действительно генерализуется. Specific numbers (AUC 0.78 vs 0.89 vs 0.92) дают concrete sense of marginal gains. «Classical BLS лучше CNN в 4 specific situations» — appreciated nuance.
- **Weaknesses**: Astronomy specific terminology (TESS, Kepler, TOI catalog, BLS, transit dip) — это **domain vocabulary**, но автор объясняет inline. ОК.

### Сводка по walked examples:

- **WE-2** — лучший, **applicable + memorable + actionable**.
- **WE-1** — strong, нужен российский context tweak.
- **WE-TESS** — strong как мета-pattern.
- **WE-3** — chemistry-heavy, **least accessible** для универсального студента.

---

## 7. What I'd want before chapter (gaps in prerequisites)

Prerequisites declared в frontmatter: lec-01 / lec-02 / lec-03 / lec-07 / lec-11. Я их **знаю** (как simulator-студент). Но есть **дополнительные prerequisites, не declared, но needed**:

1. **Базовое знакомство с peer review process** — что такое recension, что такое retraction, в чём cycle submission → review → revision → acceptance. Автор предполагает, что я **знаю**, что peer review устроен так-то. Для bachelor 3-курсника это **может быть не очевидно** — я никогда не публиковал статью. **Recommendation**: 1-абзаца briefing в §0.1 или ссылка на 1-pager про peer review process.
2. **Базовая статистика** — t-test, ANOVA, p-value. Автор упоминает их без объяснения в §5.2. ОК для bachelor 3-курсника, **но**: aspirant из non-математического track может не помнить. **Recommendation**: либо явно «known from intro statistics», либо inline 1-sentence reminder.
3. **DFT — что это, what it does** — автор glosses «density functional theory» как «first-principles quantum mechanical calculation». Для меня (3-курсник ИУ6, computer engineering) это **просто слова**. Я знаю Шрёдингера на уровне «есть уравнение Шрёдингера», но **не знаю**, как DFT работает практически. **Recommendation**: 2-3 sentence explainer «DFT решает уравнение Шрёдингера для многих электронов через approximation плотности; результат — энергии и forces для каждой атомной конфигурации».
4. **Bayesian Optimization mathematical foundation** — что такое prior, posterior, acquisition function. Я знаю Байеса (теорема), но **BO как метод** — не уверен, что прошёл. **Recommendation**: 1-paragraph краткое введение в §1.6 до того, как переходить к catalyst optimization example.
5. **AI-как-co-author этика — академическая интегрита basics**. Автор предполагает понимание «authorship integrity», «plagiarism», «research misconduct». Bachelor 3-курсник может не быть знаком с этими нормами на formal уровне. **Recommendation**: 2-3 sentences в §0.1 о том, что научная работа имеет established norms (Vancouver group, Helsinki Declaration analog), которые AI применение challenges.

---

## 8. Russification concerns (англицизмы, которые отвлекают)

Это **слабое место главы**. Я насчитал десятки англицизмов, которые **могли бы быть переведены без потери смысла**, и которые **раздражают RU-читателя**.

### High-frequency offenders (subjective sample, ~30-50 случаев каждый):

- **augmentation, autonomous** — это **термины лекции**, OK. Но автор иногда пишет «augmentation» там, где «помощь» / «augment» / «дополнение» работало бы.
- **closed-world / open-world** — **термины лекции**, OK. (В glossary §0.4 определены.)
- **workflow** — везде. «Workflow» — это **процесс работы / последовательность шагов**. Используется ~30+ раз. Можно русифицировать.
- **pipeline** — «pipeline detection» / «AI pipeline» / «training pipeline». Можно «конвейер» / «процесс» / «последовательность шагов».
- **deploy / deployment** — «not deployed operationally» / «production deployment». Можно «развёрнут» / «внедрён» / «в эксплуатации».
- **mainstream** — «mainstream в Russian academic community». Можно «массовый» / «широко используемый».
- **paper** vs «статья» — иногда «paper», иногда «статья». **Inconsistent**.
- **benchmark** — «benchmark задачи» / «benchmark reference». Можно «эталонный тест» / «эталон».
- **inference** — «Aurora inference latency». Можно «вывод модели» / «прямой проход».
- **performance** — везде. Можно «производительность» / «качество».
- **adoption** — везде в §5.6. Можно «внедрение» / «распространение».
- **insight** — везде. Можно «вывод» / «прозрение» / «понимание».
- **trade-off / tradeoff** — «трейдоff между recall и precision». Этот terms можно «компромисс».

### Specific egregious sentences:

- §3.4: «conformal prediction даёт **calibrated confidence interval**» — это **double англицизм**. Можно «дает откалиброванный доверительный интервал».
- §3.6: «**mature methods rarely become obsolete; они become components в larger pipelines**» — это **полу-английская фраза**, calque «become». Можно «зрелые методы редко устаревают; они становятся компонентами больших pipelines» (или ещё проще «больших систем»).
- §4.1: «**reliable citation tracing внутри corpus**» — два англицизма подряд.
- §4.5: «**parsing paper PDFs или LaTeX source**» — fine, но «парсинг PDF-файлов статей» проще.
- §5.6: «**adapting foreign foundation models > developing from scratch**» — это **shorthand-английская фраза**. Можно «адаптация чужих foundation-моделей > разработка с нуля».
- Часть 3 в целом — **много half-English sentences**. К примеру в §6: «**Те, кто их не делает, eventually wrapped в retraction scandals и career damage**» — это calque, не русский.

### Mixed pattern (English term + Russian glue):

- «**AI Russia 2030 Strategy** — macro-policy framework» — OK, term name English.
- «**arguments for / arguments against** в community в 2025-2026» — два английских sub-clauses.
- «**не translates direct к biology** / social sciences / cosmology» — Russian construction with English verb.

### Recommendation P1:

**Pass 1: replace 30-50 highest-frequency offenders.** workflow / pipeline / deploy / mainstream / benchmark / inference / performance / adoption / insight / tradeoff — заменить на русские эквиваленты везде, где это не term-of-art из glossary §0.4.

**Pass 2: re-read each chapter section out loud.** Specifically looking for half-English sentences. Если предложение читается как «русский каркас + английские bricks» — переписать.

**Estimated impact**: ~100-150 word replacements. Doable за 1-2 hours focused editing. **Это снижает cognitive load чтения для RU-аудитории на ~15-20%**.

### Acceptable English terms (keep):

- Brand names: AlphaFold, GNoME, A-Lab Berkeley, Aurora, GraphCast, Pangu-Weather, FourCastNet, Boltz, Coscientist, Co-Scientist, Sakana AI Scientist, ICMJE, NeurIPS, ICLR, CASP, IMO, FrontierMath, RDF, DFT, MD, BO, GP, HITL, RAG, LLM, IDP, MSA, U-Net, transformer, CNN, NotebookLM, Elicit, Consensus, Semantic Scholar, PaperQA, Scite, NSF, NIH, EU AI Act, AIRI, Sber AI Lab, Yandex Research, РНФ, AI Russia 2030 — **keep, это собственные имена**.
- Established acronyms with inline gloss: GDT_TS, pLDDT, ICMJE, NSF — **keep**, but verify inline gloss первого появления.

---

## 9. Specific recommendations для revision (P0/P1/P2)

### P0 (must fix до Phase 3 critic):

**Нет P0.** Глава полностью читаема, ни одного места не блокирует базовое понимание. Strict-in 45.9%, multi-part 30 200 слов, керистоун явен, framework applicable — Phase 3 critic должен видеть как functional draft.

### P1 (should fix до finalization):

1. **P1-1: Russification pass** (см. §8 выше). 30-50 высокочастотных англицизмов → русские эквиваленты + re-read parts 2-3 out loud для half-English sentences. **Estimated effort**: 1-2 hours.
2. **P1-2: §3.5 IDP deep-dive — eliminate redundancy с §2.1.** §3.5 должна начинаться с «Здесь deep-dive причин IDP-проблемы» и переходить **непосредственно** к technical detail (training data composition + PDB bias + per-residue confidence + drug docking impact + α-synuclein concrete case). Текущий вариант повторяет высокоуровневый pitch.
3. **P1-3: §5.6 Russian context — split or compact.** Текущие 5 подразделов overloaded. Либо разбить на §5.6.1-.6.5 with clear headers, либо сократить «Конкретные примеры успешного применения» (3 examples) к 1-2.
4. **P1-4: WE-3 chemistry vocabulary — gloss or simplify.** Inline «VASP — это industry-standard DFT software package», «Quantum ESPRESSO — open-source alternative», «BET surface area — мера площади поверхности catalyst, важная для catalytic activity». Либо WE-3 переключить на материал, ближе к универсальному студенту-инженеру (composites, semiconductors, не пропилен-окисление).
5. **P1-5: Lean / proof assistant — gloss в §2.7.** Одно предложение «Lean — это proof assistant (формальный верификатор доказательств) от Microsoft Research; программа автоматически проверяет, что доказательство строго следует из аксиом».
6. **P1-6: MSA / homology modeling / ab initio folding — short gloss в §2.1.** 2-3 предложения briefing до AlphaFold-specific content.
7. **P1-7: acquisition function / Expected Improvement / UCB — gloss в §1.6.** Одно предложение «acquisition function (e.g., Expected Improvement) — функция, которая для каждого кандидата $x$ вычисляет ожидаемую полезность измерения $f(x)$ для нахождения максимума; модель балансирует exploitation (там где предсказан high $f$) и exploration (там где модель не уверена)».
8. **P1-8: conformal prediction — distinguish from classical CI в §3.4.** Одно предложение «conformal prediction отличается от классических confidence intervals тем, что **distribution-free** (не предполагает, что residuals нормально распределены) и даёт **finite-sample coverage guarantees**».
9. **P1-9: §0.4 glossary — convert from numbered list to table.** Структура «Term | Definition | First example» more reference-friendly.

### P2 (polish, optional):

10. **P2-1: §3.3 параллельные проекты one-liner** — слишком сухие, либо удалить, либо объединить в table.
11. **P2-2: §4.6 ICMJE — slightly compress.** Текущие ~1200 слов могут быть ~700-800 без потери смысла; emotional fatigue в конце §4 высокий.
12. **P2-3: §5.6 Russian context добавить 1 line каждый case A/B/C про «specific publication или product»** — make concrete vs abstract («AIRI in 2024 published X в Nature Communications about Y» лучше «AIRI имеет publications в Nature Communications 2024-2025»).
13. **P2-4: WE-1 add inline reference к Минобрнауки приказам** — balance NSF AI Code of Conduct.
14. **P2-5: Q&A backup expansion** — Bonus Q16-Q18 (existing) полезные; consider Q19 «Что делать, если я нахожу AlphaFold-prediction для своего drug target имеет low pLDDT в IDP region — продолжать docking?» — applicable.

---

## 10. Structural cuts assessment

**Не требуется major structural cuts**. Verdict APPROVE-WITH-POLISH, не REVISE.

Минорные cuts, которые могли бы рассмотреться:

- §3.3 параллельные проекты блок (Brain Knowledge Platform + UCSF Allen 1300) — **сократить до one line** ИЛИ удалить как «не central к Lecture».
- §4.6 ICMJE — **компактировать с ~1200 до ~700-800 слов**.
- §5.6 «Конкретные примеры» (3 examples в конце) — **сократить до 1-2 examples**.

Никакой полный раздел не следует cut. Структура (Intro + 6 lestnice steps + Closing) — clean и nothing redundant на architectural уровне.

---

## Final reader notes (orchestrator-ready)

**Что я хорошо запомню через 2 недели**:
- 6-step ladder + cyclic vs linear (different from lec-13/14).
- AlphaFold Nobel + IDP problem + AlphaFold DB 200M vs PDB 200k.
- A-Lab 41/58 vs Palgrave-Schoop 35/36.
- Frontiers крыса + NeurIPS 100+ fake citations.
- 5-step framework + 3 vendor questions.
- WE-2 (collaborator bibliography) — applicable завтра.

**Что я **могу забыть** через 2 недели**:
- Coscientist (CMU) vs Co-Scientist (DeepMind) — точная attribution.
- Aurora 5000× number — могу забыть, чем 5000 measures.
- AlphaProof time-cost (4+ часа per problem).
- 5 категорий критериев «AI не нужен» — могу путать с 5-step framework.
- Russian context AIRI / Sber / Yandex specifics.
- ICMJE 4 rules — могу помнить лишь, что disclosure + AI ≠ author.

**Что я **не унесу** без преподавателя**:
- WE-3 chemistry detail (если меня спросят в QA «какой VASP» — не вспомню).
- Lean / formal math как concrete tool (помню что AlphaProof использует Lean, но что с этим делать — нет).
- conformal prediction technical detail.
- Exact mechanics of MSA в AlphaFold.
- Что именно Aurora «5000× быстрее» measures на operational уровне.

**Это нормально для self-study chapter**. Сильное retention достигнуто на mental hooks; technical depth — backup в источниках для тех, кто хочет копнуть глубже.

---

**Reviewer**: reader-simulator (mode=text-only), perspective = 3rd-year ИУ6 МГТУ engineering student без отраслевого background.
**Date**: 2026-05-27.
**Chapter version**: v1.0 (Phase 2 initial draft from plan-v2).
