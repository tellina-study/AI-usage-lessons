# Methodology Critic Report — Лекция 11 Plan v1 — 2026-05-21

**VERDICT: REVISE**

(Counter-check: 6 P1 issues ⇒ verdict ≠ APPROVE-WITH-POLISH. Forced REVISE.)

---

## Top-line summary

Plan v1 — крепкий, ambitiously-scoped, с грамотно подобранным failure-bucket каркасом и industry-real keystone. Variant C («Discrete vs Process») оправдан и структурно отличен от lec-09 OODA. Однако шесть существенных проблем требуют адресации до Phase 2: (1) центральный LO8 формально декларирован, но §4 пакует 10+6+4+5 items в 13 минут — overload, что ставит payoff под угрозу; (2) §1 (12 мин «общее») получает 42% failure-bucket с предположением, что pilot purgatory + GE Predix + IBM Watson + Foxconn WI помещаются в 5 минут — не помещаются; (3) failure-bucket strict-in таблица содержит несколько строк, которые на проверку — «магическая пилюля + предостережение», а не strict-in; (4) Hook A (Tesla 2018 Musk цитата) — старее 8 лет, и без визуального якоря текст-якорь рискует не «висеть на экране»; (5) отсутствует несколько fundamental concepts для отраслевой лекции (OEE, ground-truth определение, edge inference latency как самостоятельный термин с числами, OT/IT divide, label cost vs data volume); (6) keystone-слайд хорош, но «соединительный пояс» — три pop-термина (foundation models, agentic-копилоты, pilot purgatory) — рискует превратиться из несущего glue в декоративный.

---

## P0 issues (BLOCKING — фундаментально мешают Phase 2)

**Нет P0.** План структурно валиден, keystone-axis предъявляется в §0 до первого погружения, заголовок про ось, failure-bucket распределён, hero plan присутствует. Двинуться к chapter можно после P1 fixes.

---

## P1 issues (значимые — должны быть адресованы в Plan v2)

### P1-1. §4 (13 мин) перегружен: 10 + 6 + 4 + 5 = 25 элементов синтеза в 13 минут — payoff лекции под угрозой

**Что не так.** §4 — заявленная PEAK секция failure-bucket и payoff для LO8. Содержит: (a) 10 критериев AI-not-fit; (b) 6 альтернативных инструментов (SPC, DOE, MPC, RCM, physics-sim, rules-vision); (c) 4 hybrid patterns (PINN, CIRL, ML over SPC, PLC+edge); (d) 5-step framework. 25 дискретных elements за 13 минут = 31 секунда на каждый. На таком pacing студент уносит «список», а не «применимый mental model» (см. ваш же R3 «Mitigation» — но он не решает проблему, только переупаковывает).

**Evidence.** §4.1 «slide-of-the-day, читаются вслух» 10 criteria за 4 мин = 24 сек на критерий, при условии что каждый критерий нужно ещё связать с примером из §2-§3. §4.2 — 6 альтернатив за 4 мин = 40 сек на инструмент. Это — recitation, не applicable knowledge.

**Why критично.** LO8 — единственный LO с метрикой «≥5 критериев». Если §4 — recitation, LO8 формально покрыт, но **fails в Bloom Apply**. Это структурный gap, не polish: §4 — это центральный payoff лекции (по вашему же плану).

**Recommendation.** Один из двух fixes для Plan v2:
1. **Сократить + worked example.** 10 → 6 критериев (выберите strongest: MTBF, FP-cost, regulatory audit, known physics, operator distrust, demo-hype). Освободите ~2 мин для **worked example**: студент применяет 6 критериев к hypothetical kейсу (например, «vendor предлагает PdM на pumps с MTBF 3 года» — apply критерий #1). 6 + 4-3 hybrid + 5-step framework + worked example — это applicable.
2. **Растянуть §4 до 15 мин** за счёт §1 (12 → 10 мин, см. P1-2). Тогда 10 критериев + 4 альтернативы (consolidate hybrid с alternatives) + worked example.

### P1-2. §1 (12 мин) overloaded: adoption + 2 foundation models + 3 hype-collapses + pilot purgatory stats — не помещается в 5+4+3 мин

**Что не так.** §1.3 (3 мин) пытается покрыть GE Predix ($4B, decade-long collapse, root causes), IBM Watson Manufacturing ($1B fire-sale), и Foxconn Wisconsin (полная saga 2018-2024 + Microsoft pivot). Каждый из этих — 5+ минут standalone в любой нормальной лекции про hype. 3 мин = 60 сек на кейс. Это reading aloud, не teaching. §1.1 (3 мин) добавляет 5 расходящихся market estimates с pedagogical point — само по себе 2-3 мин.

**Evidence.** Research/04 §1.1 GE Predix занимает ~400 слов / 7 источников. Чтобы дать структурный урок (industrial AI ≠ general cloud AI, hardware→software pivot anti-pattern, $ ≠ результат) — минимум 90 секунд. Аналогично IBM (demo-to-prod gap) и Foxconn WI (anti-signal lesson). Реалистичный budget = 6-7 минут для §1.3, не 3.

**Why критично.** §1 — universal failure-слой («что общее для обеих моделей»). Если он скомкан, студент не получает foundational frame для §2-§3 deep-dives и keystone «pilot purgatory в поясе» осыпается.

**Recommendation.** Plan v2 — переоценить §1: либо (a) сократить trio до **двух** канонических (предлагаю drop IBM Watson manufacturing — там evidence слабее по research/04 §1.2, оставить GE Predix как «$ ≠ result» + Foxconn WI как «anti-signal»); либо (b) растянуть §1 до 15 мин за счёт §0 (с 7 до 5 мин) или §5 (с 7 до 5 мин). NB: nice-to-have — отдельный slide для «3 урока hype-collapse trio», без deep-dive каждого, с QR на chapter.

### P1-3. Failure-bucket strict-in таблица содержит «магическая пилюля + предостережение» строки — strict-in % завышен

**Что не так.** По CLAUDE.md «AI-Failure & Judgment Content Rule»: «не учитывается общие дисклеймеры, однострочные оговорки, "ИИ иногда ошибается" без урока/критерия/альтернативы; "магическая пилюля" с приставкой "но будьте осторожны"». Перепроверка таблицы plan v1 §144-154:

| Раздел | Plan v1 заявил | Recount strict-in (реалистично) | Проблема |
|---|---|---|---|
| §0 (7 мин) | ~2.5 мин / ~35% | ~2 мин / ~28% | Tesla retreat hook = strict-in (failure + lesson). 2 failure-маркера в keystone — это **маркеры**, не разбор; засчитывается partial. |
| §1 (12 мин) | ~5 мин / ~42% | ~5 мин / ~42% — реалистично если §1.3 расширен до 5 мин | Если §1.3 = 3 мин squeezed, реальное «strict-in с уроком» = ~3.5 мин / ~29%. |
| §2 (17 мин) | ~8 мин / ~47% | ~6-7 мин / ~38% | §2.2 PdM «Honest reality check» — это **1 строка**, не разбор; «vendor обещает X, McKinsey говорит большинство not capturing» — это «магическая пилюля + предостережение», не strict-in. §2.3 «Foxconn FoxBrain 80% — vendor self-claim (LO2 hook)» — strict-in (LO2-критерий + 3 уточняющих вопроса). §2.4 Tesla 2018 = canonical strict-in. §2.5 границы CV + альтернативы = strict-in. |
| §3 (17 мин) | ~7 мин / ~41% | ~7 мин / ~41% — реалистично | §3.5 РФ-контекст «public-disclosure скудна = анти-pattern в reporting» — это **pedagogical point на ~1 мин**, не разбор failure. Strict-in доля §3 = 3.4 + 3.4 = ~6.5 мин = ~38%. |
| §4 (13 мин) | ~13 мин / ~100% | ~12 мин / ~92% (worked example нужен — см. P1-1) | Принимается. |
| §5 (5-7 мин) | ~1 мин / ~17% | ~1 мин / ~17% | Failure-callback recap — partial; принимается. |
| **Total** | **~36.5 / 75 ≈ 49%** | **~33-34 / 75 ≈ 44-45%** | Comfortably ≥30%, но не 49%. |

**Why критично.** Self-report «49%» создаёт ложное чувство safety; на rendered artifacts (chapter+slides+speech) распределение может drift'ить — orchestrator подумает «у нас buffer», на деле buffer ~10pp, не 19pp. Лекция 8 lesson: producer self-report drift'ит относительно deep scan.

**Recommendation.** Plan v2 — recount table с явным разделением strict-in (полный разбор: что + урок + альтернатива) vs partial (маркер / 1-line). Целевая метрика — strict-in **per artifact** (chapter+slides+speech) ≥30%, не aggregate. Если §2.2 PdM остаётся 1-минутным маркером — пометить partial, не strict-in.

### P1-4. Hook A («Tesla 2018 Musk humans underrated») — 8-летняя цитата, недостаточно «висит на экране»

**Что не так.** Hook Engagement Quality Check (см. methodology-critic infrastructure):
- **Time-evergreen?** Musk 2018 цитата + 2024 GigaCast retreat — да, evergreen, события не «устаревают».
- **Emotionally engaging?** «Humans are underrated» — strong quote, но цитата не визуальный объект.
- **«Висит на экране» worthy?** ❌ Tesla Giga Press фото есть (s01 hero), но Musk quote — *текст*. Hook нарратив крутится 3-4 минуты — за это время студент успевает прочитать quote 3 раза и заскучать. Нужен второй visual якорь (timeline 2018 → 2024 → ...).
- **Connected to keystone?** ✅ Discrete column, Tesla = canonical failure.
- **Counter-example check vs Lec-1 s01 «AI вокруг нас live demo»** — Lec-1 был live + multi-visual; здесь — статичный photo + quote.

**Evidence.** §0.2 Hook hero 3-4 мин с одним static photo (Giga Press) + Musk quote. Это >180 секунд на single visual. Hook A primary без secondary visual artifact = engagement risk.

**Why критично.** Hook задаёт энергию первых 5 минут. Если hook вял — recovery в §1 требует extra effort. Lec-2 lesson: pivot hook на Phase 8.5 = 5 циклов.

**Recommendation.** Plan v2 — augment Hook A:
1. Tesla Giga Press hero **+ inset timeline** (2018 "humans underrated" → 2020 Giga Press launch → 2024 retreat). Two-stage visual.
2. Или: split-screen — Tesla Giga Press 2020 photo + Musk 2018 quote overlay + 2024 retreat caption. One slide, three timepoints.
3. Альтернатива — переставить Hook B на primary (GE+Foxconn WI split-screen — два real события на split-screen богаче visual). Tesla перенести в §2.4 deep-dive. Но это меняет hook философию от «over-automation» на «hype-collapse», что может ослабить connection к keystone (over-automation — discrete column failure mode). Решение — owner choice; **рекомендую Augmentation (вариант 1)** как minimal change.

### P1-5. Missing fundamentals для отраслевой лекции: OEE, ground-truth (как cornerstone), edge inference latency, OT/IT divide, label cost vs data volume

**Что не так.** Plan §3.7c заявляет «активный словарь: distribution shift, FP/FN, accuracy/precision/recall, edge vs cloud, HITL, GxP, regression baseline». В glossary §0.4 — 12 acronyms (ISA-95, MES, SCADA, PLC, OEE, SPC, MPC, APC, PdM, RL, CV, soft sensor). Однако:

- **OEE (Overall Equipment Effectiveness)** — упомянут только в glossary list, но не explained. Это **central metric** в производстве (availability × performance × quality). Vendor claims «-25% downtime» бессмысленны без OEE-framing — LO2 страдает.
- **Ground truth** — secondary cornerstone, но **не raised до cornerstone**. В §3.3 PdM «(b) ground truth available» — referenced без определения. Для отраслевой лекции про производство (где defect labels noisy, MTBF медленная) — это **fundamental**.
- **Edge inference latency** — qualitatively упомянут в §3.3 (POSCO, «1-10 мс»), но не как самостоятельный концепт «почему PLC vs edge ML — это не только location вопрос, а latency-determinism вопрос». Это **fundamental для discrete-control**.
- **OT/IT divide** — не упомянут вообще. Это **defining structural divide** в индустриальной AI: OT (Operational Technology — PLC, SCADA, deterministic) vs IT (cloud, AI, eventually-consistent). Без него §3 regulatory blockers зависают в воздухе.
- **Label cost vs data volume** — не упомянут. CV-границы §2.5 говорят «scarce defect labels, 1-2% rate». **Почему** — потому что labels требуют domain expert × hours = $$ vs raw data cheap. Это связь к §4 критерию «AI fit».

**Why критично.** Per methodology-critic Missing-Fundamentals Check: «для каждого major концепта introduced — verify dependencies». Отраслевая лекция без OEE — как лекция про LLM без temperature. Без OT/IT divide — regulatory blockers (FDA Part 11 vs ATEX) теряют structural объяснение.

**Recommendation.** Plan v2 — добавить:
1. **OEE** в §1.1 (adoption landscape) — 1 предложение определение + «vendor -25% downtime означает что в OEE? availability +X% или performance +Y%? — это 3-й уточняющий вопрос для LO2». OEE становится cornerstone #8.
2. **Ground truth** — поднять до cornerstone #6 (а PINN/CIRL — в secondary). Inline gloss в §2.5 или §3.3 при первом упоминании.
3. **OT/IT divide** — добавить 30-секундный slide в §1 или §3.1 (перед regulatory). Это даёт scaffold для §3.4.
4. **Edge inference latency как determinism** — расширить §3.3 на 30 сек, явная фраза «latency = determinism, не только speed». Это связывает §3.3 с §4.3 (PLC+edge ML coprocessor).
5. **Label cost vs data volume** — связать в §2.5 с §4.1 критерий «ground truth available» — это lever для LO8 alternative «active learning vs full labeling».

### P1-6. Сечение § order: §3.1 RU regulatory приходит ПОСЛЕ §3.4 FDA/ATEX — но §3.5 РФ упоминает «100% critical infrastructure → domestic software к 2027» без regulatory scaffold

**Что не так.** §3 порядок: 3.1 soft sensors → 3.2 MPC/RL → 3.3 PdM/edge → 3.4 regulatory (FDA, ATEX) → 3.5 РФ контекст. §3.5 говорит про «параллельный кризис отрасли (Severstal profit -55% в 2024)» и «импортозамещение domestic software» — это **regulatory + geopolitical context**. Логически §3.5 не место для regulatory-adjacent контента, оно идёт за §3.4. ОК. **Но** §3.4 fully выкладывает FDA Part 11 + ATEX + GAMP®5 без РФ counterpart (ГОСТ Р 57700.37-2021 упомянут только в Normative References, не в §3). Студент уходит с asymmetry: западные регуляторные frameworks разобраны, РФ — placeholder.

**Why критично.** Course philosophy («где AI, где нет») требует regulatory clarity в обоих контекстах. РФ-студенты заметят асимметрию.

**Recommendation.** Plan v2 — переместить ГОСТ Р 57700.37 callback из normative refs в §3.4 (30-секундный block) или явно в §3.5 как regulatory-aspect of РФ контекста. Или explicit decision «ГОСТ — это lec-12 territory (digital twins regulatory)», и убрать упоминание из lec-11 normative refs. NB: foreshadow в §5.2 («ГОСТ Р 57700.37-2021 даёт regulatory ground») оставляет дверь, но studенту нужен **closure**, не teaser.

---

## P2 issues (polish — для Plan v2 fix или carry-forward)

### P2-1. Glossary §0.4 «12 acronyms × 2 колонки» — 1-2 мин на 12 терминов = 5-10 сек на термин

Cognitive overload. Recommendation: glossary inline-defined при первом use, не upfront в §0.4. Сохранить только «6 must-know» (ISA-95, MES, SPC, MPC, PdM, soft sensor) на keystone slide, остальные — inline.

### P2-2. Anglicism leakage в plan-v1.md narrative

Grep показал: «pilot purgatory» 11×, «distribution shift» 6×, «baseline» 6×, «hype» 4×, «foundation model» 1×. Plan-text — internal artifact, но §3.7c Russification mandate говорит «застревание на пилотной стадии» и «сдвиг распределения». Plan itself drift'ит. Не критично для plan-document, но carry-forward risk для chapter/speech.

**Recommendation.** Plan v2 — заменить в самом тексте plan'а ≥50% употреблений на RU-canonical (хотя бы первое упоминание каждого термина), оставляя ENG-парентезу. Это «walk-the-talk» для downstream agents.

### P2-3. Lecture-map §0.4 + glossary §0.4 — одно slot

«0.4 Lecture-map + glossary mini» — это два artifacts в 1-2 мин. По Lec-N-1 pattern (lec-09), lecture-map = standalone slide (s02a). Discriminate: lecture-map = roadmap (sections), glossary = terms. Не объединять.

### P2-4. Hook backup B narrative — «8th wonder» Trump 2018 → Microsoft Fairwater

Backup hook содержит политически-заряженный narrative (Trump quote). Generic audience phrasing OK (anonymization не нарушено), но политический quote может отвлечь. Если Hook B активируется (R1 mitigation) — переформулировать без named politician, just «глава государства» (anonymization-style applied к hook).

### P2-5. §5.2 «закрывающая hero BMW Werk + digital-twin overlay» — Hook B backup Foxconn-NVIDIA в research/06 С3 — нужен явный sub-fallback для s39 closing tier

Plan §5.2 называет один candidate (BMW). research/06 §s39 даёт backup Holcim или NVIDIA-Foxconn. Plan v2 — явно перенести fallback chain в plan §5.2 или mandates.

---

## Failure-bucket strict-in check — recount

**Заявлено plan v1:** ~49% strict-in.
**Recount (мой):** **~44-45%** strict-in (см. P1-3 таблицу), comfortably ≥30%, но с margin ~14pp, не 19pp.

**Per-section:**
- §0: ~28% (partial credit for failure markers in keystone)
- §1: ~29-42% (depends on §1.3 budget)
- §2: ~38% (vendor disclaimer строки = partial, не strict-in)
- §3: ~38% (РФ pedagogical point = partial)
- §4: ~92% (worked example нужен, см. P1-1)
- §5: ~17% (partial credit)

**Aggregate:** ~33-34 мин / 75 = **44-45%**. **Holistic distributed: yes** (min §5 = 17%, max §4 = 92%, no single-artifact concentration).

**Decision:** Acceptable, but **don't claim 49%**. Plan v2 — honest 44-45% with clear partial vs strict-in marking.

**Per-artifact projection:**
- Chapter ~10-12k слов: 40-45% failure (4-5k слов) — achievable, но требует honest tracking
- Slides ~35: ≥10 strict-in (s09-s11, s15, s18-s19, s22, s26-s27, s30, s31-s35) — **13-14 / 35 = 37-40%** — OK, но margin тонкий
- Speech ~5k / 75 мин: ≥22-25 мин strict-in (~33%) — achievable

---

## Keystone-axis assessment — Variant C works, with one minor tightening

**Verdict.** **Variant C («Discrete vs Process») валиден как несущая ось** для Лекции 11. Plan v1 правильно его выбрал.

**Доводы за:**
1. **Industry-real.** Инженеры реально делят свою работу на discrete vs process; это не academic taxonomy.
2. **Failure modes структурно разные.** Tesla over-automation (discrete) vs F-35 ALIS PdM drift (process) — student видит контраст.
3. **Regulatory landscape natural.** FDA Part 11 (process/pharma) vs CV inspection (discrete) — structurally distinct buckets.
4. **Не дублирует lec-09 OODA.** OODA = horizontal stage-chain внутри mission; D-vs-P = vertical taxonomy of production types. Different mental object — confirmed via lec-09 chapter inspection: lec-09 keystone — «OODA + dual-use bridge + L1-L5 autonomy ladder». Lec-11 keystone — production-type taxonomy. Студент чувствует разные frames.
5. **Bridges natural.** lec-09 (defense mission systems) → lec-11 (production discrete/process) → lec-12 (digital twins — где discrete и process сходятся в virtual representation).

**Минор concern — «соединительный пояс» keystone:**

Plan §47 описывает middle band: «foundation-модели, agentic-копилоты, **pilot purgatory** (95% не доходят до production)». 3 элемента в connecting belt: foundation models (concept) + agentic copilots (concept) + pilot purgatory (statistic). Это — heterogeneous mix. Risk: belt становится «декоративным», а не несущим. Student видит column-A | belt | column-B и спрашивает «belt — это что? тренд? проблема? универсалия?».

**Recommendation.** Plan v2 — keystone belt должна декларировать ОДНУ функцию. Предлагаю: belt = «**Что общее: 78% пользуются AI, 5.5% high performers (McKinsey 2025)**» — это ОДИН statement, signals «оба столбца обсуждают одну и ту же реальность hype vs delivery». Foundation models + agentic copilots можно сдвинуть в §1.2 deep-dive (где они и есть). Pilot purgatory остаётся в belt как numeric anchor.

**Counter-check.** Заголовок: «Две модели производства. AI входит в обе — но по-разному» — ✅ про саму ось, не про устройство курса. 1-я строка — про columns ✅. Pass.

---

## Missing-fundamentals list — конкретно что должно добавиться (см. P1-5)

**Mandatory для Phase 2 chapter:**
1. **OEE** — definition + structural role в LO2 vendor-claim parsing
2. **Ground truth** — promote к cornerstone (#6), inline gloss при первом use в §3.3
3. **OT/IT divide** — 30-секундный block перед §3.4 regulatory (или в §1.2)
4. **Edge inference latency как determinism** — 30 сек extension в §3.3, явное «latency = determinism»
5. **Label cost vs data volume** — связать в §2.5 + §4.1

**Nice-to-have:**
6. **Model drift vs distribution shift** — clarify distinction (drift = slow over time; shift = batch transition / new product). Plan говорит «distribution shift» universally — это imprecise.
7. **Anomaly detection vs SPC** — beyond §8.2 research framing, добавить в §3 явный contrast (5-10 сек).
8. **CBM (condition-based monitoring)** — упомянут в §4.2 как alternative, но не определён. Inline gloss.

---

## LO coverage matrix

| LO | Definition (manifest) | Covered by | Bloom level | Status |
|---|---|---|---|---|
| LO1 | Классифицировать типы AI-решений и сопоставить их с задачами индустрий | LO1a (§0 keystone + §2 + §3) Remember; LO1b (§4 framework Step 1) Apply | Remember+Apply | ✅ covered, two-level split justified |
| LO2 | Оценить применимость AI-решения к конкретной бизнес-задаче | §2.3 Foxconn FoxBrain 80% self-claim + §2.4 Tesla recovery + §3.2 RL drift + §4.1 «3 уточняющих вопроса» | Evaluate | ✅ covered, central pedagogical hook |
| LO7 | Обосновать выбор архитектуры AI (чат, агент, RAG, API, модель) для задачи | §1.2 foundation models / agentic copilots / autonomous-vs-augmentation; §3.4 FDA Part 11 «decision support vs autonomous»; §4.2 alternatives | Evaluate | ⚠️ partial — «выбор архитектуры AI» в narrow sense (chat/agent/RAG) маппится только в §1.2; в plan мощнее звучит как «выбор инструмента вообще» (см. P2-X note) |
| LO8 | Определить роль человека и AI в совместной работе; HITL | §2.3 Toyota Jidoka/GAIA; §2.4 Tesla over-automation lesson; §3.1 Pfizer Vox «recommend, не autonomous»; §3.4 HITL FDA; §4 5-step framework Step 5 | Apply+Create | ✅ central, payoff |

**LO7 caveat.** Plan v1 §38 формулирует LO7: «Описать regulatory landscape... различить decision support vs autonomous controller, обозначить позицию инженера». Это **корректная переинтерпретация** manifest LO7 для отраслевого контекста, но не точно «выбор архитектуры AI». **Recommendation:** Plan v2 — добавить 30-сек block в §1.2 или §3.3 «foundation model как augmentation vs autonomous controller» с явным mapping на LO7 (chat/agent — augmentation; autonomous controller — это другая архитектура). Сейчас LO7 покрыт implicit, не explicit.

---

## Recommendations for Phase 2 chapter

**Carry-forward (что хорошо):**
1. Keystone Variant C — keep. Tighten belt (см. keystone assessment).
2. 5-step framework в §4.4 — keep, **build chapter back-end around it**.
3. Hero plan s01 (Tesla Giga Press) + s39 (BMW Digital Twin) — keep, document 6-tier per-image fallback в iteration-log.md.
4. Anonymization (generic audience) — keep, strict.
5. Russification mandate — keep, **walk-the-talk в plan v2 narrative**.
6. РФ контекст (§3.5) как pedagogical pattern «public-disclosure скудна» — keep, smart framing.

**Caveats для chapter:**
1. **§4 worked example** (P1-1) — chapter должен содержать developed worked example (~500-800 слов) применения 5-step framework к hypothetical kейсу. Это якорь для applicable knowledge.
2. **§1 trimming OR expansion** (P1-2) — выбрать перед chapter draft. Если оставляем 3 hype-collapses, drop IBM Watson; если расширяем — increase chapter §1 word budget.
3. **Failure-bucket honesty** (P1-3) — chapter §4 + §2 + §3 должны явно strict-in tagged. Methodology-critic в Phase 3 будет recount с deep scan.
4. **Missing fundamentals OEE / ground truth / OT-IT** (P1-5) — chapter добавляет inline gloss + structural block.
5. **LO7 explicit mapping** (LO matrix caveat) — chapter §1.2 phrases foundation-model-as-augmentation явно с reference LO7.
6. **Hook A augmentation** (P1-4) — chapter §0 / hook-narrative section имеет two-stage visual (Tesla 2018 + 2024) prescribed.
7. **Anglicism count target** — chapter narrative deep-scan strict-in ≤5 critical anglicisms (Russification mandate §3.7c).
8. **Anonymization** — keep absolute; chapter не упоминает МГТУ / ИУ6 / любые named institutions.

**Phase 2 chapter target:** 10-12k слов; ~40-45% failure-bucket strict-in distributed; 5-step framework + worked example в §4; OEE + ground truth + OT/IT divide добавлены; cornerstones (6-7 main + secondary) glossary lock'нутся.

---

## Top-3 issues (приоритизировано для Plan v2 turn-around)

1. **P1-1** — §4 pacing fix (worked example OR trim). Это критично для LO8 payoff.
2. **P1-3** — failure-bucket recount table с partial vs strict-in marking. Honest tracking для chapter.
3. **P1-5** — добавить OEE, ground-truth, OT/IT divide, edge-latency-determinism — fundamentals для отраслевой лекции.

P1-2 (§1 budget) — следующий, но решается одновременно с P1-1 (если §4 → 15 мин, §1 → 10 мин и vice versa). P1-4 (Hook augmentation) и P1-6 (РФ regulatory closure) — следующие.

---

**Конец Methodology Critic Report. Verdict REVISE. Next: orchestrator merges с reader-simulator critique, decides scope of Plan v2, спавнит book-editor для Plan v2 turn.**
