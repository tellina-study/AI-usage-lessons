# Лекция 9: AI в авиакосмической отрасли и оборонном комплексе — v2 plan

## Метаданные

- **Lecture:** 9 | **Module:** 2 | **Duration:** 75 мин + Q&A (~5 мин буфер)
- **LO:** LO1a, LO1b, LO2, LO3, LO7 (5 LO — split LO1)
- **Audience:** студенты ИУ МГТУ 3 курса — будущие инженеры КБ, ракетно-космических предприятий, военной индустрии, dual-use стартапов
- **Issue:** #118 | **Status:** v2 (Phase 1 critique synthesis closed)
- **Date:** 2026-05-20
- **Keystone axis:** **OODA — Sense → Decide → Act** + инъекции: dual-use bridge (фон в Р0) + L1-L5 ladder (visual в Р4)
- **Hook:** **A primary** (BEFORE/AFTER satellite, evergreen + политически нейтральный); **B backup** (F-35 ALIS failure-first) — если satellite licensing не закроется на Phase 5

---

## Changes from v1 (Phase 1 critique closure)

**P0 fixes (2 — BLOCKING для Phase 2, closed):**

- **P0-1** Glossary mini-slide добавлен в Р0 после keystone (6 acronyms × 2 колонки): SAR, ATR, ISR, EW, LAWS, OODA. Остальные (HITL, HOOL, HOTL, CCA, AMRAAM, V-BAT, MCAS, IFF, BPSA, HALE, GNSS, EOCL, FedRAMP, IL4/IL6, ROE, IHL) — inline-расшифровка при первом упоминании в chapter + speech. **Mandate-line для book-editor Phase 2:** «расшифровывать каждый acronym при первом упоминании в chapter». **Mandate-line для presentation-designer Phase 5:** «glossary slide делается mini-style — компактный, 6 определений в 2 колонки, не полноценный slide».
- **P0-2** Р2 Decide vendor-cut: 13 → **5-6 working cases** (Palantir MSS, Scale Donovan/Defense Llama, Helsing Altra, Anthropic-Palantir-AWS partnership, Russian C2 — выбран Svod **OR** Glaz-Groza с single-source CSIS caveat). Honorable mentions (Helsing Centaur, NASA FDL FOXES, Scale Thunderforge, DAGGER++, ZOV Maps, Cohere classified) — одной строкой в boxed-list, не разворачивать.

**P1 fixes (4, closed):**

- **P1-1** LO1 split на LO1a (Remember) + LO1b (Apply); итого 5 LO согласно lec-07 паттерну.
- **P1-2** Р4 pacing rebalanced: 4.3 ICRC + 4.4 Stop Killer Robots → одна sub-section «International civil society stance» (3-4 мин); 4.1 L1-L5 ladder = 4 мин; 4.6 HITL trio = 3 мин; остальные по 2 мин; Anthropic+OpenAI ban перенесён в 4.5 «Big-tech defense posture shift».
- **P1-3** L1-L5 ladder operational definitions добавлены явно (см. §«L1-L5 ladder definitions»).
- **P1-4** HITL/HOOL/HOTL visual mandate в Р4.6 для Phase 5 designer (trio + примеры per уровень из L1-L5 mapping).

**P2 fixes (9, closed):**

- **P2-1** Lancet backup mandate для LO2 в Phase 2 brief.
- **P2-2** Hook decision final: A primary (BEFORE/AFTER sat), B backup (ALIS failure-first).
- **P2-3** 7 критериев redistributed: 2 в Р1 (Sense), 2 в Р2 (Decide), 1-2 в Р3 (Act); consolidated matrix-slide в Р5.1 (2 мин recap).
- **P2-4** Russian context 22-25% **принято**, не резать.
- **P2-5** DoD Directive 3000.09 — строка в Normative References + краткое упоминание в Р4.2 (UN GGE context, US position).
- **P2-6** Anthropic-Palantir-AWS + OpenAI removed-ban перенесены из Р2 → Р4.5 «Big-tech defense posture shift» (2024-2025 narrative bound к Maven walkout).
- **P2-7** Cognitive Pilot (КАМАЗ autonomous trucking) добавлен в Р3 одной строкой как Russian civilian dual-use counterpoint.
- **P2-8** OODA-sourcing (John Boyd, USAF, 1976) — одна строка в §«Несущая ось → keystone».
- **P2-9** Sber GigaChat на ISS — **удалён** из Р1 Russian context (single-source unverified, не критичен для narrative).

---

## Topics Covered

ISR / спутниковая аналитика / on-orbit edge AI / predictive maintenance / mission planning + target ID / CCA / drone autonomy / missile defense / LAWS-treaty / Russian военно-космический AI-слой + один civilian dual-use case.

## Prerequisites

Лекция 3 (foundation models, on-device inference); Лекция 4 (copilot/agent риски в safety-critical); Лекция 6 (topology optimization, generative design); Лекция 7 (симметричная Russian-context модель FDA+mosmed.ai → DoD+Роскосмос/ВКА; HITL); Лекция 8 (generative модели).

## Normative References

- **Международное.** UN GGE on LAWS (UNGA 161-3-13 Nov 2024; 156-5-8 Nov 2025; rolling text Sept 2025). ICRC position paper 2024. Stop Killer Robots briefs 2025.
- **США.** **DoD Directive 3000.09 (Autonomy in Weapon Systems, 2012, updated 2023)** — US policy на autonomous lethal action, требует HITL для kinetic engagement в большинстве scenarios. Replicator/DAWG programmatics. NIST AI RMF.
- **РФ.** Presidential Decree #116 (Feb 2026, Commission on AI Development). National AI Decree May 2024. Минобороны AI department (структура не публичная).
- **Стандарты.** ARP4754A / DO-178C (safety-critical software для civil aviation).

## Learning Objectives

1. **LO1a (Remember).** Назвать 3 звена OODA (Sense, Decide, Act) и для каждого — 2-4 dominating 2026 tools/programs + направление adoption (растёт / стабильно / переоценено).
2. **LO1b (Apply).** Для конкретного aerospace/defense кейса определить, в каком звене OODA AI работает наиболее эффективно, и где на стыке звеньев возникает структурный риск провала.
3. **LO2.** Критически оценить заявление вендора «autonomous targeting» — отличить demo-condition perf от production-deployment perf. **Canonical case:** Lancet ATR rollback (Russian). **Backup case** (если day-of dispute): Russian Lancet → IDF Lavender Gaza shift, или DARPA X-62A scripted-scenario reveal.
4. **LO3.** Сформулировать ≥5 критериев «здесь AI не нужен / опасен» для safety-critical aerospace/defense контекста, применить их к учебному кейсу. Критерии распределены по разделам (Sense / Decide / Act) с consolidation в Р5.1.
5. **LO7.** Описать LAWS-treaty landscape (UN GGE timeline, ICRC + civil society stance, votes breakdown), различить «autonomous decision support» vs «autonomous lethal engagement» через L1-L5 ladder + HITL/HOOL/HOTL trio, обозначить позицию инженера на этой границе.

---

## Несущая ось → keystone (ENFORCED — Лекция 4 lesson)

- **Ось:** **OODA — Sense → Decide → Act.** Каждая боевая или гражданская aerospace-задача — цепочка из трёх звеньев; AI вторгается в каждое по-разному; провалы случаются преимущественно **на стыках звеньев**.
- **OODA sourcing (P2-8 fix):** John Boyd, USAF, 1976. Изначально для air-combat decision-making; теперь — универсальная decision-loop модель в military doctrine, cyber-security, business strategy. Это **50-летняя инженерная модель**, не выдумка для лекции.
- **Keystone slide в Р0** = первый content slide после cover/lecture-map, **ДО** первого погружения. Горизонтальная цепочка Sense → Decide → Act с тремя иконками; под каждым звеном — три строки «где AI работает / не работает / где граница». Заголовок: **«Три звена цепи. AI входит в каждое — но по-разному»**. Заголовок и 1-я строка — про саму ось, **НЕ** про устройство курса, защиту подхода или recap.
- **Каждый раздел = мотивированный спуск/подъём по оси:** Р1 Sense; Р2 Decide; Р3 Act; Р4 meta-уровень «где Act обрезано регулированием» (LAWS, L1-L5); Р5 callback к keystone.
- **Dual-use bridge как фон** (из Опции В): на keystone — тонкая серая лента вдоль цепочки «гражданское ↔ военное». Указывает, что те же Sense/Decide/Act работают в обе стороны.

---

## L1-L5 Autonomy Ladder — operational definitions (P1-3 fix)

Эта лестница появляется в Р4.1 как центральный visual меты-раздела. Каждый уровень имеет **операциональное определение** через «что делает AI / что делает человек», и привязан к конкретному 2026 примеру:

| Level | AI does | Human does | 2026 example |
|---|---|---|---|
| **L1 — Assistive** | **выдаёт** information / detections | decides whether to act | Palantir MSS analyst surface |
| **L2 — Semi-auto perception** | **рекомендует** action (target lock, route) | authorises каждое action | Saker Scout target lock confirmation |
| **L3 — Supervised autonomy** | **executes** action в pre-authorised envelope | supervises, может intervene | Anduril Fury wingman (CCA Increment 1) |
| **L4 — Pre-authorised auto-engage** | **engages** target по pre-set rules of engagement (ROE) | может intervene, но не required в loop | Patriot auto mode, S-400 auto ROE |
| **L5 — Full LAWS** | **executes lethal action** без human authorisation | вне loop | **Currently debated, not deployed** — даже Lavender (Gaza) формально требует human approval перед strike (минимальный, ~20 sec review per case — но human всё равно в loop, formally L4-edge) |

**Pedagogical note для chapter:** граница L4↔L5 — это **место юридических дебатов** UN GGE; L3↔L4 — это **место engineering debate** «pre-authorisation envelope насколько узок?». Студент должен уметь сказать, **где именно** на лестнице сидит конкретная система.

---

## HITL / HOOL / HOTL trio (P1-4 fix)

Эта триада появляется в Р4.6 как **центральная mental model** регулирования. Visual mandate для Phase 5 designer: одна картинка с тремя human-стиками относительно AI-цикла.

- **HITL — Human-In-The-Loop.** Human в каждом decision-point. AI **не действует** без явного human authorisation. Mapping на L1-L5 ladder: **L1, L2**. Пример: Palantir MSS analyst, Saker Scout operator confirmation.
- **HOOL — Human-On-The-Loop.** Human **supervises** AI-цикл, может intervene в любой момент, но не required в каждом decision-point. Mapping: **L3, L4**. Пример: Fury CCA wingman (pilot oversees), Patriot auto ROE (operator monitors).
- **HOTL — Human-Out-of-The-Loop.** Human **вне execution-loop**, не имеет real-time intervention capability. Mapping: **L5** (по определению treaty-discussion).

**Что в этом важно для инженера-выпускника:** граница HOOL → HOTL — это **то, на что заточены DoD Directive 3000.09 + UN GGE rolling text + ICRC position**. Engineering decision «сколько ms у оператора на intervention» формально определяет, в какой кат-ии (HOOL vs HOTL) живёт ваша система.

---

## Инструменты на каждом уровне таксономии (ENFORCED L4+ — Лекция 4 lesson)

### Sense (sensor / ISR / on-orbit edge AI)

- **Tools 2026.** Maxar Sentry (NGA Luno); BlackSky Gen-3 + Spectra AI; Planet Labs (NRO EOCL); Slingshot Agatha + TALOS (space domain awareness — photometric fingerprinting спутников); ESA Φ-sat-2. **Russian:** TerraTech, ScanEx, Sputnix Zorkiy-2M.
- **Adoption:** растёт быстро; «AI-derived detections in hours» → «predictive intelligence перед событием». On-orbit edge ML: от Φ-sat-1 demo к operational constellations.
- **Anti-hype:** sensor-side работает лучше остальных звеньев (ground-truth доступна, FP относительно дёшев). Но **бренд ≠ режим работы**: «Maxar Sentry» = suite ML+multi-sensor tipping (Electro-Optical + Synthetic Aperture Radar + Automatic Identification System), не one model; «AI-derived» часто = classic CV + change detection.
- **Volatile** (`[VFY-day-of]`): NRO EOCL contract values, SDA Tranche 3 launch schedule, BlackSky subscription.

### Decide (mission planning, target ID, fusion, decision support)

- **Tools 2026 (5-6 working — P0-2 cut applied).**
  1. **Palantir MSS (Maven Smart System)** — US flagship, ~$1.3B ceiling до 2029; история Maven 2017-2026 от Google walkout до Palantir consolidation.
  2. **Scale AI Donovan / Defense Llama** — foundation models для defense; first LLM в US classified network XVIII Airborne Corps 2023; Defense Llama Nov 2024.
  3. **Helsing Altra** — EU land combat fusion, €12B valuation.
  4. **Anthropic-Palantir-AWS partnership** (Nov 2024) — Claude на IL6 classified. **Note:** narrative-bound в Р4.5 как часть Big-tech defense posture shift, не как stand-alone tool case.
  5. **Russian C2 — Svod OR Glaz-Groza** (CSIS-documented, **single-source caveat**) — попытка Russian Palantir-equivalent; выбран один из двух (final choice — book-editor Phase 2 на основе depth source coverage). Не оба.
- **Honorable mentions (one-line bullets в boxed-list, не разворачивать):** Helsing Centaur (AI fighter pilot test Saab Gripen E), Scale Thunderforge, NASA FDL FOXES, DAGGER++, ZOV Maps, Cohere classified deployments. Студент видит «есть ещё и эти», не учит их детали.
- **Adoption:** растёт по числу контрактов; LLM hype outpaces verifiable ground truth.
- **Anti-hype:** **LLM hallucinations + automation bias = главный риск**. Здесь «accuracy 90%» ≠ «90% правильных решений» — cost-asymmetry FP↔FN космическая (один числовой пример в chapter: Lavender 37 000 detected × 10% FP = 3700 неправильно помеченных людей). Decide-tools = smart accelerators для analyst, не replacement для commander. Инфраструктура (FedRAMP HIGH, IL4/IL6, SC2S/SIPR/JWICS — три уровня secrecy compartmentation) — отделена в свой блок, не часть AI capability.
- **Volatile:** Palantir MSS ceiling, Anduril valuation, Helsing valuation, Thunderforge scope.

### Act (autonomy на платформе)

- **Tools 2026.** Anduril Fury YFQ-44A (first flight Oct 2025, production Mar 2026); Shield AI V-BAT + Hivemind ($198M USCG 2024, Indian Army Jan 2026); DARPA X-62A VISTA; Saker Scout (Ukraine, 64 autonomous targets); Anduril Roadrunner + Barracuda; Lockheed Skunk Works AI battle mgmt. **Russian:** Geran-2 (NVIDIA Jetson wreckage; Alabuga >5000/мес), Lancet ATR rollback. **Russian civilian dual-use (P2-7 fix):** **Cognitive Pilot (КАМАЗ autonomous trucking)** — civilian-side analogue Geran-2 autonomy; one paragraph, balances defense-heavy Russian narrative. **Chinese:** CETC Atlas (96 drones / 1 operator), Jiu Tian mothership.
- **Adoption:** растёт количество platforms; **большая часть** combat-strikes остаётся operator-in-loop или semi-auto terminal guidance, **не** fully-autonomous swarms. Counter-drone AI — explosive (асимметрия $300 drone vs $3M Patriot).
- **Anti-hype:** **hype far ahead of true autonomous engagement**. «96-drone swarm / 1 планшет» = centralized многоканальное управление, не decentralized peer-to-peer (где каждый drone имеет ML on-board и общается с соседями без central uplink). CCA — collaborative, supervised pilots overhead. «AI заменит pilots» overhyped: X-62A = narrow scripted scenario.
- **Volatile:** Fury production rate, Replicator delivered count, Geran-2 monthly production, Shield AI valuation diff sources.

### Инфраструктура (отделена от capability)

CI/SAST для embedded autonomy + edge compute (NVIDIA Jetson Orin NX) + DO-178C/ARP4754A safety cert + FedRAMP IL4/IL6. **Не AI capability** — плитка под капабилитис, один слайд.

---

## Outline

### Раздел 0 — Keystone + glossary + roadmap (5 мин)

**Цель.** Предъявить ось OODA как карту лекции; зацепить hook'ом; снять glossary-блокер перед Р1.

**Hook (final, P2-2):** **A primary** — BEFORE/AFTER object detection на свежем спутниковом снимке (Maxar/Planet, CC-licenced). Evergreen, политически нейтрален (Sudan port construction или Arctic ice change). **B backup** — F-35 ALIS → ODIN провал, failure-first hook. Если на Phase 5 satellite licensing не закроется (Wikimedia / direct vendor) — переключаемся на B без структурного редизайна. Hook C (X-62A dogfight) и D (drone footage с targeting) **отклонены** (C — AI-восторг; D — этически непригоден).

**Keystone slide.** Горизонтальная цепочка Sense → Decide → Act + тонкая dual-use лента вдоль. Заголовок: **«Три звена цепи. AI входит в каждое — но по-разному»**. OODA-sourcing footnote: «Boyd, USAF, 1976».

**Glossary mini-slide (P0-1 fix).** Сразу после keystone. **6 acronyms × 2 колонки**:
- SAR — Synthetic Aperture Radar (радар с синтезированной апертурой)
- ATR — Automatic Target Recognition (автоматическое распознавание целей)
- ISR — Intelligence, Surveillance, Reconnaissance (разведка, наблюдение, разведзадачи)
- EW — Electronic Warfare (радиоэлектронная борьба)
- LAWS — Lethal Autonomous Weapon Systems (летальные автономные системы)
- OODA — Observe-Orient-Decide-Act (рамка Boyd 1976)

Все остальные acronyms (HITL, HOOL, HOTL, CCA, AMRAAM, V-BAT, MCAS, IFF, BPSA, HALE, GNSS, EOCL, FedRAMP, IL4/IL6, ROE, IHL, Bayesian NN) — **inline-расшифровка при первом упоминании** в chapter/speech. Mandate в Phase 2 brief.

**Roadmap slide.** 4 содержательных раздела + 1 граничный + Q&A; LO сверху, тайминг внизу.

**Media-rich слайды Р0:** (1) hook BEFORE/AFTER satellite; (2) keystone OODA chain visualization; (3) glossary mini-slide; (4) roadmap — lecture-map.

### Раздел 1 — Sense (12 мин)

**Цель.** Показать звено Sense как «там, где AI работает лучше всего», и сразу обозначить границы.

**Working cases (4-5).** Maxar Sentry (ML над 250 PB архивом + multi-sensor tipping EO/SAR/AIS, NGA Luno contract); BlackSky Gen-3 + Spectra AI (change detection); ESA Φ-sat-2 (remote-upgradable on-orbit models); Slingshot Aerospace Agatha + TALOS (photometric fingerprinting спутников для SDA — space domain awareness, отличается от ISR target-focused); Rolls-Royce IntelligentEngine + Airbus Skywise (predictive maintenance — ~400 prevented events/year; 11 600 ВС к концу 2024).

**Strict-in failures (3).**

- **F-35 ALIS** — high FP, $44k/ч cost-per-flight-hour (выше F-22), final ALIS June 2024, ODIN rollout до 2025-26. Урок: predictive maintenance требует (a) быстрый feedback loop, (b) ground truth, (c) FP-cost < FN-cost — ALIS нарушил все три + adversarial UX. Альтернатива (ODIN): меньший scope + government-owned + disconnected mode + HITL для flight authorisation. **Cross-cutting urok.**
- **SAR ATR adversarial attacks** — physical scatterer perturbations реальны (металлические уголки, специально размещённые на технике, обманывают classifier). Урок: accuracy benchmark обманчив — adversary defines test-time distribution. Альтернатива: multi-sensor fusion + Bayesian neural networks (uncertainty-aware classification, callback к Лекции 2-3) + ensemble.
- **GPS spoofing civil aviation** — Latvia 820 cases 2024 (vs 26 в 2022); spillover на non-combatants. Урок: GNSS-only = single point of failure. Альтернатива: multi-GNSS + INS + eLORAN.

**Russian context (P2-9 applied — Sber GigaChat removed).** TerraTech (BRICS agriculture monitoring); ScanEx (3.5M+ archive, единственный direct-receiving; Moscow court ban на >2m distribution); Sputnix (Zorkiy-2M, 2.5m / 4 spectral bands).

**«Когда не AI для Sense» — 2 критерия (P2-3 fix, distribute):**
1. **Low-data domain или distribution shift inevitable** → ML не выучит надёжно; classic signal processing + multi-sensor fusion дешевле.
2. **High-stakes single-sensor decision без redundancy** → AI = single point of failure; нужна gate human authorisation либо independent sensor channel (cf. ALIS without HITL flight gate).

**Media-rich:** (5) Maxar Sentry BEFORE/AFTER detection; (6) on-orbit edge AI architecture mermaid; (7) Skywise dashboard screenshot; (8) F-35 ALIS cost-per-flight-hour QuickChart bar (vs F-22).

### Раздел 2 — Decide (14 мин)

**Цель.** Показать звено Decide как «там, где LLM-hype опасен», и почему «accuracy %» — не та метрика. **(P0-2 cut applied — 13 → 5 working cases.)**

**Working cases (5).**

1. **Palantir MSS** (multi-source fusion + AI target nomination, ~$1.3B ceiling через 2029; история Maven 2017-2026 от Google walkout до Palantir).
2. **Scale AI Donovan + Defense Llama** (first LLM в US classified network XVIII Airborne Corps 2023; Defense Llama Nov 2024 — foundation models для defense).
3. **Helsing Altra** — EU land combat fusion, €12B valuation.
4. **Anthropic-Palantir-AWS partnership Nov 2024** — Claude на IL6. **Note:** wider narrative этого partnership разбирается в Р4.5 (Big-tech defense posture shift); здесь — tooling fact.
5. **Russian Svod OR Glaz-Groza** — CSIS-documented C2 stack (попытка Russian Palantir-equivalent); deploy в units с Fall 2025. Явный single-source caveat — CSIS + Russian official press, independent verification limited. Выбран **один**, не оба. **Final choice — book-editor Phase 2** на основе глубины источников.

**Honorable mentions (one-line boxed-list, не разворачивать):** Helsing Centaur, Scale Thunderforge, NASA FDL FOXES, DAGGER++, ZOV Maps, Cohere classified deployments.

**Strict-in failures (3).**

- **IDF Lavender (Gaza 2023-24)** — 37 000 помечены; 90% accuracy (IDF self-assessment) → **~3700 false positives**; «officers devoted almost no resources» к double-checking (среднее время review ~20 sec); авторизация до 15-20 civilian casualties per junior Hamas operative. Урок: **«accuracy %» — wrong metric для life-and-death**; AI снимает фрикцию decision-making → масштабирует темпы → снимает качество deliberation. Альтернатива: AI ассистирует triage; human keeps authority; calibrated uncertainty + abstention.
- **USS Vincennes / Iran Air 655 (1988, 290 KIA)** — Aegis корректно классифицировал track как climbing, экипаж под стрессом доложил «descending into attack». Урок: UI под combat stress — не панацея; тестировать под predicted failure modes. **Cross-applies к LLM decision support** — confident BS = high-risk confident BS в high-stakes.
- **Russian Lancet ATR rollback (2022-24)** — marketing «autonomously find and hit target»; реальность: AI guidance off после initial deployment, videos без "Target Locked" UI (CSIS analysis). Урок: **demo ≠ production**; ML perf в narrow distribution не переносится на full battlefield variance. Альтернатива: operator-in-loop с tracking-assist. **Pedagogically особо ценен** — LO2 canonical case.

**«Когда не AI для Decide» — 2 критерия (P2-3 fix, distribute):**
1. **Long-tail edge cases где ML confidence низкая** → automation bias масштабирует ошибки; нужна structured abstention («AI говорит "не знаю" и эскалирует»).
2. **High-stakes life-and-death без redundancy / HITL** → cost-asymmetry FP↔FN неприемлемо большая для шиuro statistical decision (Lavender — canonical anti-example).

**Media-rich:** (9) Palantir MSS UI screenshot (если public); (10) Lavender 37k/3700 FP infographic QuickChart; (11) Vincennes 1988 Aegis UI + decision-timeline mermaid; (12) Lancet "Target Locked" BEFORE/AFTER; (13) Russian C2 stack drawio.

### Раздел 3 — Act (14 мин)

**Цель.** Показать звено Act как «там, где hype далеко впереди реальности», но adoption всё-таки растёт.

**Working cases (4-5).** Anduril Fury YFQ-44A (CCA Increment 1; first flight Oct 31, 2025; AIM-120 AMRAAM long-range air-to-air; production Mar 2026 на Arsenal-1 $1B Ohio); Shield AI V-BAT + Hivemind (Group 3 VTOL, 12+ ч endurance, EW-resistant; $198M USCG July 2024; Indian Army Jan 2026); DARPA ACE X-62A VISTA (first AI vs manned F-16 Sept 2023, 2000 ft @ 1200 mph; 21 test flights; Kendall flew May 2024); Saker Scout Ukraine (64 autonomous targets, 10 km, CV-based ID, EW-resistant; Brave1 ecosystem 300+ AI dev; first fully unmanned ground op Dec 2024); CETC Atlas swarm China + Jiu Tian mothership (1 оператор / 96-drone combat cycle; HALE — high altitude long endurance — mothership 100-150 loitering munitions June 2025).

**Strict-in failures (3).**

- **Boeing 737 MAX MCAS (2018-19, 346 KIA)** — single AoA (Angle of Attack) sensor + opacity + repeated trim commands. Не AI строго, но **canonical anti-pattern** для safety-critical AI. Уроки: redundancy + transparency + FMEA/FTA + software не лечит hardware. Альтернатива: double sensor + disengage path + training.
- **Patriot 2003** (RAF Tornado GR4 + USN F/A-18C) + **Ukrainian F-16 Patriot 2024** — automation bias + IFF (Identification Friend or Foe) unresolved. Урок: «лучше человека» = ослабленный oversight; mitigation системная (deconfliction + IFF + doctrinal training), не single ML upgrade.
- **DoD Replicator missed scale (2023-25)** — цель thousands к Aug 2025; реальность Sept 2025 «hundreds». Урок: hardware scales быстрее software integration; multi-vendor autonomy = system engineering challenge. Альтернатива: DAWG honest slowing.

**Russian context.** Geran-2 — NVIDIA Jetson onboard (wreckage); Alabuga >5000/мес; anti-radar variant Mar 2026. **«Autonomy» claims частично подтверждены, но большая часть strikes остаётся operator+GPS guided.** Sanctions evasion — Shreya Life Sciences (India) 1111 Dell серверов через third countries 2024. Урок: **hardware supply-chain = strategic risk**, свои чипы могут оказаться в чужих weapons.

**Russian civilian dual-use case (P2-7 fix).** **Cognitive Pilot** — российская компания, автономные системы для КАМАЗ-грузовиков, тракторов (СберАгро), снегоуборочной техники. Civilian-side analogue Geran-2 autonomy: те же CV/ML pipelines, тот же sensor stack (camera + LiDAR + radar), но **applied к гражданскому транспорту**. Балансирует Russian defense-heavy narrative — показывает, что российский AI **не сводится к военному**.

**«Когда не AI для Act» — 1-2 критерия (P2-3 fix, distribute):**
1. **Autonomy не нужна, человек медленнее но безопаснее** → MCAS canonical anti-example (single sensor + auto trim был «решением» проблемы, которой могло не быть в первую очередь).
2. **COTS sensor дешевле + reliable** → не делать ML на проблеме, которая решается hardware redundancy (cf. AoA на 737 MAX — second sensor стоил бы порядки меньше всех trim-AI).

**Media-rich:** (14) Fury YFQ-44A production photo (Arsenal-1); (15) Shield AI V-BAT + Hivemind architecture mermaid; (16) X-62A VISTA cockpit + dogfight timeline; (17) Geran-2 wreckage с Jetson — Ukrainian recovery (public CSIS); (18) Boeing 737 MAX MCAS single-AoA mermaid; (19) Atlas/Jiu Tian illustration; (20) Replicator delivered-count QuickChart promise vs delivery.

### Раздел 4 — Граница и регулирование (15-17 мин, целиком strict-in)

**Цель.** Показать «где звено Act обрезано регулированием»; L1-L5 ladder + HITL/HOOL/HOTL trio как visual для LAWS-границы.

**Содержание (6 sub-sections — P1-2 rebalance applied, ICRC+SKR combined).**

- **4.1. L1-L5 ladder (4 мин).** Центральный visual всего раздела. Operational definitions per level (см. §«L1-L5 Autonomy Ladder» выше). Mapping: MSS=L1; Saker Scout=L2; Fury supervised CCA=L3; Patriot auto ROE=L4; LAWS=L5 (currently debated). Над L4 — visual marker «treaty negotiation zone». **DoD Directive 3000.09 (P2-5):** US policy формально требует HITL для kinetic, что ставит US системы по умолчанию в L1-L3, с явным waiver-процессом для L4.
- **4.2. UN GGE timeline (2 мин).** UNGA 5 Nov 2024 **161/3/13**; 6 Nov 2025 **156/5/8**. Sept 2025 GGE — 42 states joint statement, rolling text. UN SG target: treaty by **2026**. Against: Belarus, NK, Russia. Abstainers: China, India, Iran, Israel, Ukraine. **DoD Directive 3000.09 brief mention** — US position в этом контексте.
- **4.3. International civil society stance (3-4 мин)** — **combined ICRC + Stop Killer Robots (P1-2 fix).** ICRC: prohibit (a) unpredictable AWS, (b) AWS против persons; restrict остальные. «Ceding life-and-death decisions to machines is dehumanizing»; «не weapon system, а humans using it must comply with IHL». Stop Killer Robots — 30 countries full ban. Эти две organisations — основной non-state pressure on treaty negotiations.
- **4.4. Project Maven walkout 2018 (2 мин).** Google leak Mar 2018; 4000+ letter; ~12 резигнировали; контракт не продлён. Anduril/Palantir/Scale подобрали. Урок: **personal ethics ≠ industry regulation**. Опция «не работать на DoD» теперь редкая.
- **4.5. Big-tech defense posture shift 2024-2025 (2 мин) (P2-6 narrative bound).** OpenAI removed military ban Jan 2024. Anthropic-Palantir-AWS partnership Nov 2024 (Claude IL6 classified). Microsoft Azure Government, Cohere classified. **Narrative arc:** Maven walkout (2018) → vendor-replacement (Anduril/Palantir 2018-2024) → Big-tech возврат (2024-2025). Урок: industry ethics drift in 6 years.
- **4.6. HITL / HOOL / HOTL — engineering pattern для LAWS-edge (3 мин) (P1-4 fix).** Trio visual (см. §«HITL/HOOL/HOTL trio» выше) + конкретные примеры per уровень из L1-L5 mapping. Engineering takeaway: «сколько ms у оператора на intervention» = formal definition границы HOOL → HOTL. Calibrated uncertainty + abstention + structured outputs + mandatory human gates для kinetic action.
- **4.7. Russia votes против UN LAWS resolutions (1 мин).** Geopolitical context для студента-инженера в РФ. Дать факт + сказать «инженер делает свой выбор внутри этих рамок».

**Pacing total:** 4 + 2 + 3-4 + 2 + 2 + 3 + 1 = **17-18 мин** (резать 4.4 или 4.5 до 1.5 мин если жёсткий перебор; кандидаты на резку явные). Раздел 5 можно сжать до 8 мин если перебор сохраняется (5.2 + 5.3 сжимаются легко).

**Important note для chapter:** **LAWS-блок применим к не-LAWS работе студента.** Критерии «pre-authorised limits / human gates» работают для любой автономной системы (промышленный робот, автомобиль, безопасность критической инфраструктуры) — LAWS просто частный case с высокой видимостью. Это **обязательно явно сказать** в chapter §4 + speech, иначе студент LAWS-блок воспринимает как «не для меня».

**Media-rich:** (21) L1-L5 ladder с примерами per level; (22) UN GGE voting world map; (23) ICRC + SKR side-by-side positions; (24) Maven walkout timeline + Big-tech shift; (25) HITL/HOOL/HOTL trio drawio.

### Раздел 5 — Q&A + payoff (8-10 мин)

**Цель.** Закрыть лекцию практическими критериями + career angle + reading list, callback к keystone.

- **5.1. 7 критериев «когда не AI» — consolidation matrix (2 мин) (P2-3 fix).** На одном слайде — все 7 критериев, распределённые по OODA (2 Sense / 2 Decide / 2 Act / 1 cross-cutting LAWS-boundary):
  - **Sense (2):** (1) Low-data domain или distribution shift inevitable; (2) High-stakes single-sensor без redundancy.
  - **Decide (2):** (3) Long-tail edge cases с low ML confidence (need abstention); (4) High-stakes life-and-death без HITL.
  - **Act (2):** (5) Autonomy не нужна, человек медленнее но безопаснее; (6) COTS sensor дешевле + reliable.
  - **Cross-cutting (1):** (7) Если граница HOOL → HOTL пройдена — это treaty-territory, не engineering.
  Lecturer проходит matrix 30 sec/критерий = 3.5 мин с recap. Detailed критерии разнесены по разделам как «закрывающий takeaway» в конце каждого OODA-блока.
- **5.2. Career angle (3 мин).** МГТУ ИУ + ВКА им. Можайского + dual-use стартапы (VisionLabs, Cognitive Pilot) + civilian path (Роскосмос TerraTech / commercial sat analytics). **Без агитации.** Если упомянуть кафедру слушателя (ИУ-2/ИУ-6) — engagement выше.
- **5.3. Reading list (2 мин).** Scharre *Army of None* (CNAS); CSIS Russia drone ecosystem (Bondar Apr 2026); Abraham +972 (Lavender); ICRC position paper 2024; DARPA ACE briefings; GAO F-35 ALIS/ODIN; Stop Killer Robots briefs 2025.
- **5.4. Closing callback (1 мин).** «Цепь Sense → Decide → Act — каждое звено имеет свои AI-инструменты, границы и failure modes. Инженер держит её в голове целиком».

**Media-rich слайды:** (26) 7-критериев consolidation matrix; (27) career-map drawio; (28) closing callback — keystone repeated as bookend.

---

## Провалы, ограничения и альтернативы (ENFORCED — ≥30% strict-in)

**11 strict-in failure блоков** (детали — в Outline по разделам): F-35 ALIS, SAR ATR adversarial, GPS spoofing civil aviation (Р1); IDF Lavender, USS Vincennes 1988, Lancet ATR rollback (Р2); Boeing 737 MAX MCAS, Patriot 2003 + Ukr F-16 2024, Replicator missed scale (Р3); Maven walkout, Big-tech shift, UN GGE + ICRC + SKR (Р4 целиком).

**Бюджет strict-in (re-counted после P0-2 cut + P1-2 rebalance):**

- Р4 (целиком strict-in): 17 мин = **23%** + 5 слайдов.
- Failure-блоки в Р1-3 (8 блоков × 2-3 мин): ~18-22 мин = **24-29%** + 6-8 слайдов.
- Р5 критерии consolidation: 2 мин = **3%** + 1 слайд.
- Criteria distributed в Р1/Р2/Р3 OODA-closing (2+2+1-2 критерия × ~30 sec each): ~4 мин = **5%** дополнительно (counted в Р1-3 strict-in бюджете, не двойной).

**Суммарно strict-in:** ~37-41 мин из 75 = **49-55%**; ~12-14 из ~28-30 слайдов = **40-45%**; chapter ~35-40% слов (target). **Comfortable margin** над ≥30% по всем 3 артефактам holistic.

**Counter-check.** Если на Phase 3/7 strict-in доля <30% или сконцентрирована в одном артефакте — verdict REVISE. P0-2 vendor-cut **не уменьшил** strict-in бюджет (резали working cases, failure-блоки нетронуты). P1-2 rebalance **увеличил** общий бюджет (Р4 17 мин vs v1 15 мин).

---

## Assessment

LO7 («этическая оценка применений ИИ») покрывается Разделом 4 + Разделом 5 критериями. LO1b (Apply) — добавлен в v2, явно проверяется в case-study упражнении (Phase 5 brief: один OODA-кейс для класса разобрать). Семинар sem-09 — отдельная задача (не в scope); anticipated case study на одном failure-блоке (Lavender adversarial review process, или Lancet hardening vs premature deployment).

---

## Slide-budget превью (для Phase 5)

- Total ~30-33 слайдов (cut от v1 ~32-35 за счёт Р2 vendor-cut + ICRC/SKR combine); media-rich **17-19** (55-60%, выше ≥50% порога с запасом).
- Section dividers: 6 (Р0-Р5); cover + lecture-map + Q&A: 3; glossary mini-slide: 1; content: ~20-23; pacing ~2-2.5 мин/content slide.
- **Lec-N-1 pattern compliance:** match lec-08 (cover + lecture-map + section dividers + dedicated Q&A; top progress bar только на dividers + cover).
- **Mandate для designer (P0-1):** glossary slide — **mini-style** (компактный, 6 acronyms × 2 колонки), не полноценный slide с illustrative imagery.
- **Mandate для designer (P1-4):** HITL/HOOL/HOTL trio в Р4.6 — **визуально separate slide** с тремя human-стиками относительно AI-цикла, не bullet-list.

---

## Phase 2 brief readiness (book-editor handoff)

Все вопросы plan-v1 closed:

1. **Hook финал** — A primary, B backup. ✓
2. **ALIS placement** — Sense (predictive maintenance side) cross-cutting, один callback в Act. ✓
3. **Раздел 4 pacing** — rebalanced (4.1=4 мин; 4.6=3 мин; ICRC+SKR combined в 4.3=3-4 мин). ✓
4. **Russian context volume** — 22-25% принято. ✓
5. **Wisk Aero / eVTOL** — не включать как case (consensus). ✓
6. **DoD Directive 3000.09** — строка в Normative + mention в Р4.2 (US position в UN GGE). ✓

**Mandates явно зафиксированы для book-editor Phase 2:**

- Расшифровывать каждый acronym при первом упоминании в chapter (P0-1).
- LO1b (Apply) — добавить в учебные цели chapter, обеспечить case-study экзампл в §3 или §5.
- L1-L5 operational definitions использовать в chapter §4.1 (см. таблицу выше).
- HITL/HOOL/HOTL trio — отдельный sub-section в chapter §4.6 с mapping на L1-L5.
- LO2 canonical case = Lancet primary; ALIS scripted-scenario backup (если Lancet day-of dispute).
- Russian civilian Cognitive Pilot — один параграф в §3 как dual-use balance.
- Sber GigaChat ISS **удалено** из chapter (P2-9).
- Anthropic-Palantir + OpenAI ban — narrative-bound в §4.5 «Big-tech defense posture shift», в §2 — только tooling fact без timeline-context.
- LAWS-блок (§4) явно сказать «эти критерии применимы к любой автономной системе, не только weapons».
- OODA-sourcing (Boyd 1976) — одна фраза в chapter §0 / §1 для credibility.

---

## References (key sources, full list — research files 01-04)

- **Defense One** (June 2025) — Maxar Sentry launch.
- **Yuval Abraham, +972 / Local Call** (Apr 2024) — Lavender investigation.
- **GAO-20-316, GAO-22-105943** — F-35 ALIS reports.
- **CSIS** (Bondar, Apr 2026) — Russia sovereign drone ecosystem.
- **CSIS** — Russia probably hasn't used AI weapons in Ukraine (Lancet rollback canonical source).
- **DARPA** — ACE AI vs human dogfight world first.
- **Stop Killer Robots** — UNGA 161-3-13 + 156-5-8 voting results.
- **ICRC** — Position paper on autonomous weapons (2024).
- **Army Recognition** (Mar 2026) — Anduril $20B Lattice contract.
- **USNI Proceedings** (July 2018) — Vincennes human-machine team failure.
- **DoD Directive 3000.09** (2012, updated 2023) — Autonomy in Weapon Systems policy.
- **Scharre, P.** *Army of None* (CNAS, 2018) — autonomous weapons foundational reading.
- **John Boyd** — OODA loop original paper (USAF, 1976).
