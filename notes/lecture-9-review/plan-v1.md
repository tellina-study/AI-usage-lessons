# Лекция 9: AI в авиакосмической отрасли и оборонном комплексе — v1 plan

## Метаданные

- **Lecture:** 9 | **Module:** 2 | **Duration:** 75 мин + Q&A (~5 мин буфер) | **LO:** LO1, LO2, LO3, LO7
- **Audience:** студенты ИУ МГТУ 3 курса — будущие инженеры КБ, ракетно-космических предприятий, военной индустрии, dual-use стартапов
- **Issue:** #118 | **Status:** v1 (Phase 1 critique pending) | **Date:** 2026-05-20
- **Keystone axis:** **OODA — Sense → Decide → Act** + инъекции: dual-use bridge (фон в Р0) + L1-L5 ladder (visual в Р4)

## Topics Covered

ISR / спутниковая аналитика / on-orbit edge AI / predictive maintenance / mission planning + target ID / CCA / drone autonomy / missile defense / LAWS-treaty / Russian военно-космический AI-слой.

## Prerequisites

Лекция 3 (foundation models, on-device inference); Лекция 4 (copilot/agent риски в safety-critical); Лекция 6 (topology optimization, generative design); Лекция 7 (симметричная Russian-context модель FDA+mosmed.ai → DoD+Роскосмос/ВКА; HITL); Лекция 8 (generative модели).

## Normative References

- **Международное.** UN GGE on LAWS (UNGA 161-3-13 Nov 2024; 156-5-8 Nov 2025; rolling text Sept 2025). ICRC position paper 2024. Stop Killer Robots briefs 2025.
- **США.** DoD Directive 3000.09 (Autonomy in Weapon Systems, 2023 update). Replicator/DAWG programmatics. NIST AI RMF.
- **РФ.** Presidential Decree #116 (Feb 2026, Commission on AI Development). National AI Decree May 2024. Минобороны AI department (структура не публичная).
- **Стандарты.** ARP4754A / DO-178C (safety-critical software для civil aviation).

## Learning Objectives

1. **LO1.** Указать 3 уровня OODA и для каждого назвать 2-4 dominating 2026 tool/program + направление adoption.
2. **LO2.** Критически оценить заявление вендора «autonomous targeting» — отличить demo-condition perf от production-deployment perf (canonical case: Lancet ATR rollback).
3. **LO3.** Сформулировать ≥5 критериев «здесь AI не нужен / опасен» для safety-critical aerospace/defense контекста и применить их к учебному кейсу.
4. **LO7.** Описать LAWS-treaty landscape (UN GGE timeline, ICRC position, votes breakdown), различить «autonomous decision support» vs «autonomous lethal engagement», обозначить позицию инженера на этой границе.

---

## Несущая ось → keystone (ENFORCED — Лекция 4 lesson)

- **Ось:** **OODA — Sense → Decide → Act.** Каждая боевая или гражданская aerospace-задача — цепочка из трёх звеньев; AI вторгается в каждое по-разному; провалы случаются преимущественно **на стыках звеньев**.
- **Keystone slide в Р0** = первый content slide после cover/lecture-map, ДО первого погружения. Горизонтальная цепочка Sense → Decide → Act с тремя иконками; под каждым звеном — три строки «где AI работает / не работает / где граница». Заголовок: **«Три звена цепи. AI входит в каждое — но по-разному»**. Заголовок и 1-я строка — про саму ось, **НЕ** про устройство курса, защиту подхода или recap.
- **Каждый раздел = мотивированный спуск/подъём по оси**: Р1 Sense; Р2 Decide; Р3 Act; Р4 meta-уровень «где Act обрезано регулированием» (LAWS, L1-L5); Р5 callback к keystone.
- **Dual-use bridge как фон** (из Опции В): на keystone — тонкая серая лента вдоль цепочки «гражданское ↔ военное». Указывает, что те же Sense/Decide/Act работают в обе стороны.

---

## Инструменты на каждом уровне таксономии (ENFORCED L4+ — Лекция 4 lesson)

### Sense (sensor / ISR / on-orbit edge AI)

- **Tools 2026.** Maxar Sentry (NGA Luno); BlackSky Gen-3 + Spectra AI; Planet Labs (NRO EOCL); Slingshot Agatha + TALOS; ESA Φ-sat-2. **Russian:** TerraTech, ScanEx, Sputnix Zorkiy-2M.
- **Adoption:** растёт быстро; «AI-derived detections in hours» → «predictive intelligence перед событием». On-orbit edge ML: от Φ-sat-1 demo к operational constellations.
- **Anti-hype:** sensor-side работает лучше остальных звеньев (ground-truth доступна, FP относительно дёшев). Но **бренд ≠ режим работы**: «Maxar Sentry» = suite ML+multi-sensor tipping, не one model; «AI-derived» часто = classic CV + change detection.
- **Volatile** (`[VFY-day-of]`): NRO EOCL contract values, SDA Tranche 3 launch schedule, BlackSky subscription.

### Decide (mission planning, target ID, fusion, decision support)

- **Tools 2026.** Palantir MSS (~$1.3B ceiling до 2029); Scale Donovan / Defense Llama / Thunderforge (FedRAMP HIGH); Helsing Altra + Centaur (€12B); Anthropic-Palantir-AWS (Claude IL6); Anduril Lattice (mesh OS, $20B/10y ceiling). **Russian:** Svod / Glaz / Groza / ZOV Maps (CSIS-docs, single-source caveat).
- **Adoption:** растёт по числу контрактов; LLM hype outpaces verifiable ground truth. Anthropic + OpenAI removed military bans (Jan 2024).
- **Anti-hype:** **LLM hallucinations + automation bias = главный риск**. Здесь «accuracy 90%» ≠ «90% правильных решений» — cost-asymmetry FP↔FN космическая. Decide-tools = smart accelerators для analyst, не replacement для commander. Инфраструктура (FedRAMP, IL4/6, SC2S/SIPR/JWICS) — отдельно.
- **Volatile:** Palantir MSS ceiling, Anduril valuation, Helsing valuation, Thunderforge scope.

### Act (autonomy на платформе)

- **Tools 2026.** Anduril Fury YFQ-44A (first flight Oct 2025, production Mar 2026); Shield AI V-BAT + Hivemind ($198M USCG 2024, Indian Army Jan 2026); DARPA X-62A VISTA; Saker Scout (Ukraine, 64 autonomous targets); Anduril Roadrunner + Barracuda; Lockheed Skunk Works AI battle mgmt. **Russian:** Geran-2 (NVIDIA Jetson wreckage; Alabuga >5000/мес), Lancet ATR rollback. **Chinese:** CETC Atlas (96 drones / 1 operator), Jiu Tian mothership.
- **Adoption:** растёт количество platforms; **большая часть** combat-strikes остаётся operator-in-loop или semi-auto terminal guidance, **не** fully-autonomous swarms. Counter-drone AI — explosive (асимметрия $300 drone vs $3M Patriot).
- **Anti-hype:** **hype far ahead of true autonomous engagement**. «96-drone swarm / 1 планшет» = centralized многоканальное управление, не decentralized peer-to-peer. CCA — collaborative, supervised pilots overhead. «AI заменит pilots» overhyped: X-62A = narrow scripted scenario.
- **Volatile:** Fury production rate, Replicator delivered count, Geran-2 monthly production, Shield AI valuation diff sources.

### Инфраструктура (отделена от capability)

CI/SAST для embedded autonomy + edge compute (NVIDIA Jetson Orin NX) + DO-178C/ARP4754A safety cert + FedRAMP IL4/IL6. **Не AI capability** — плитка под капабилитис, один слайд.

---

## Outline

### Раздел 0 — Keystone + roadmap (5 мин)

**Цель.** Предъявить ось OODA как карту лекции; зацепить hook'ом.

**Hook кандидаты.**
- **A.** BEFORE/AFTER object detection на свежем спутниковом снимке (Maxar/Planet, CC). Evergreen, политически нейтрален (Sudan port или Arctic ice change). **Моя рекомендация.**
- **B.** F-35 ALIS → ODIN провал — «Вот система, на которую ставили миллиарды. Что пошло не так.» Failure-first hook, прямо служит AI-Failure rule, но mood депрессивный.
- **C.** DARPA X-62A AI dogfight — wow factor high; risk: смотрится как AI-восторг. **Отклоняю.**
- **D.** Drone footage с AI-аннотированием цели — мощно, но политически чувствительно. **Отклоняю.**

**Рекомендация:** A primary; B fallback (если визуал не доходит).

**Keystone slide.** Горизонтальная цепочка Sense → Decide → Act + тонкая dual-use лента вдоль. Заголовок: **«Три звена цепи. AI входит в каждое — но по-разному»**.

**Roadmap slide.** 4 содержательных раздела + 1 граничный + Q&A; LO сверху, тайминг внизу.

**Media-rich слайды:** (1) hook BEFORE/AFTER satellite; (2) keystone OODA chain visualization; (3) roadmap — lecture-map.

### Раздел 1 — Sense (12 мин)

**Цель.** Показать звено Sense как «там, где AI работает лучше всего», и сразу обозначить границы.

**Working cases (4-5).** Maxar Sentry (ML над 250 PB архивом + multi-sensor tipping EO/SAR/AIS, NGA Luno contract); BlackSky Gen-3 + Spectra AI (change detection); ESA Φ-sat-2 (remote-upgradable on-orbit models); Slingshot Aerospace Agatha + TALOS (photometric fingerprinting спутников); Rolls-Royce IntelligentEngine + Airbus Skywise (predictive maintenance — ~400 prevented events/year; 11 600 ВС к концу 2024).

**Strict-in failures (3).**
- **F-35 ALIS** — high FP, $44k/ч cost-per-flight-hour (выше F-22), final ALIS June 2024, ODIN rollout до 2025-26. Урок: predictive maintenance требует (a) быстрый feedback loop, (b) ground truth, (c) FP-cost < FN-cost — ALIS нарушил все три + adversarial UX. Альтернатива (ODIN): меньший scope + government-owned + disconnected mode + HITL для flight authorisation. **Cross-cutting urok.**
- **SAR ATR adversarial attacks** — physical scatterer perturbations реальны. Урок: accuracy benchmark обманчив — adversary defines test-time distribution. Альтернатива: multi-sensor fusion + Bayesian NN + ensemble.
- **GPS spoofing civil aviation** — Latvia 820 cases 2024 (vs 26 в 2022); spillover на non-combatants. Урок: GNSS-only = single point of failure. Альтернатива: multi-GNSS + INS + eLORAN.

**Russian context.** TerraTech (BRICS agriculture monitoring); ScanEx (3.5M+ archive, единственный direct-receiving; Moscow court ban на >2m distribution); Sputnix (Zorkiy-2M, 2.5m / 4 spectral bands). **Sber GigaChat на ISS** — упоминаем **только** с caveat «единственный российский источник, независимо не верифицировано».

**Media-rich:** (4) Maxar Sentry BEFORE/AFTER detection; (5) on-orbit edge AI architecture mermaid; (6) Skywise dashboard screenshot; (7) F-35 ALIS cost-per-flight-hour QuickChart bar (vs F-22).

### Раздел 2 — Decide (14 мин)

**Цель.** Показать звено Decide как «там, где LLM-hype опасен», и почему «accuracy %» — не та метрика.

**Working cases (4-5).** Palantir MSS (multi-source fusion + AI target nomination, ~$1.3B ceiling через 2029, история Maven 2017-2026 от Google до Palantir); Scale AI Donovan + Defense Llama + Thunderforge (first LLM в US classified network XVIII Airborne Corps 2023; Defense Llama Nov 2024; Thunderforge Mar 2025); Helsing Altra + Centaur (land combat fusion + AI fighter pilot test на Saab Gripen E June 2025); Anthropic-Palantir-AWS partnership Nov 2024 (Claude на IL6); NASA FDL FOXES / DAGGER++ (ML для space science decision support).

**Strict-in failures (3).**
- **IDF Lavender (Gaza 2023-24)** — 37 000 помечены; 90% accuracy (IDF self-assessment) → **~3700 false positives**; «officers devoted almost no resources» к double-checking; авторизация до 15-20 civilian casualties per junior Hamas operative. Урок: **«accuracy %» — wrong metric для life-and-death**; AI снимает фрикцию decision-making → масштабирует темпы → снимает качество deliberation. Альтернатива: AI ассистирует triage; human keeps authority; calibrated uncertainty + abstention.
- **USS Vincennes / Iran Air 655 (1988, 290 KIA)** — Aegis корректно классифицировал track как climbing, экипаж под стрессом доложил «descending into attack». Урок: UI под combat stress — не панацея; тестировать под predicted failure modes. **Cross-applies к LLM decision support** — confident BS = high-risk confident BS в high-stakes.
- **Russian Lancet ATR rollback (2022-24)** — marketing «autonomously find and hit target»; реальность: AI guidance off после initial deployment, videos без "Target Locked" UI (CSIS). Урок: **demo ≠ production**; ML perf в narrow distribution не переносится на full battlefield variance. Альтернатива: operator-in-loop с tracking-assist. **Pedagogically особо ценен.**

**Russian context.** Svod / Glaz / Groza / ZOV Maps — CSIS-documented C2 stack (попытка Russian Palantir-equivalent); deploy в units с Fall 2025. Явный single-source caveat — CSIS + Russian official press, independent verification limited.

**Media-rich:** (8) Palantir MSS UI screenshot (если public); (9) Lavender 37k/3700 FP infographic QuickChart; (10) Vincennes 1988 Aegis UI + decision-timeline mermaid; (11) Lancet "Target Locked" BEFORE/AFTER; (12) Russian C2 stack drawio.

### Раздел 3 — Act (14 мин)

**Цель.** Показать звено Act как «там, где hype далеко впереди реальности», но adoption всё-таки растёт.

**Working cases (4-5).** Anduril Fury YFQ-44A (CCA Increment 1; first flight Oct 31, 2025; AIM-120 AMRAAM; production Mar 2026 на Arsenal-1 $1B Ohio); Shield AI V-BAT + Hivemind (Group 3 VTOL, 12+ ч endurance, EW-resistant; $198M USCG July 2024; Indian Army Jan 2026); DARPA ACE X-62A VISTA (first AI vs manned F-16 Sept 2023, 2000 ft @ 1200 mph; 21 test flights; Kendall flew May 2024); Saker Scout Ukraine (64 autonomous targets, 10 km, CV-based ID, EW-resistant; Brave1 ecosystem 300+ AI dev; first fully unmanned ground op Dec 2024); CETC Atlas swarm China + Jiu Tian mothership (1 оператор / 96-drone combat cycle; HALE mothership 100-150 loitering munitions June 2025).

**Strict-in failures (3).**
- **Boeing 737 MAX MCAS (2018-19, 346 KIA)** — single AoA + opacity + repeated trim commands. Не AI строго, но **canonical anti-pattern** для safety-critical AI. Уроки: redundancy + transparency + FMEA/FTA + software не лечит hardware. Альтернатива: double sensor + disengage path + training.
- **Patriot 2003** (RAF Tornado GR4 + USN F/A-18C) + **Ukrainian F-16 Patriot 2024** — automation bias + IFF unresolved. Урок: «лучше человека» = ослабленный oversight; mitigation системная (deconfliction + IFF + doctrinal training), не single ML upgrade.
- **DoD Replicator missed scale (2023-25)** — цель thousands к Aug 2025; реальность Sept 2025 «hundreds». Урок: hardware scales быстрее software integration; multi-vendor autonomy = system engineering challenge. Альтернатива: DAWG honest slowing.

**Russian context.** Geran-2 — NVIDIA Jetson onboard (wreckage); Alabuga >5000/мес; anti-radar variant Mar 2026. **«Autonomy» claims частично подтверждены, но большая часть strikes остаётся operator+GPS guided.** Sanctions evasion — Shreya Life Sciences (India) 1111 Dell серверов через third countries 2024. Урок: **hardware supply-chain = strategic risk**, свои чипы могут оказаться в чужих weapons.

**Media-rich:** (13) Fury YFQ-44A production photo (Arsenal-1); (14) Shield AI V-BAT + Hivemind architecture mermaid; (15) X-62A VISTA cockpit + dogfight timeline; (16) Geran-2 wreckage с Jetson — Ukrainian recovery (public CSIS); (17) Boeing 737 MAX MCAS single-AoA mermaid; (18) Atlas/Jiu Tian illustration; (19) Replicator delivered-count QuickChart promise vs delivery.

### Раздел 4 — Граница и регулирование (15 мин, целиком strict-in)

**Цель.** Показать «где звено Act обрезано регулированием»; L1-L5 ladder как visual для LAWS-границы.

**Содержание (7 sub-sections × ~2 мин).**

- **4.1. L1-L5 ladder** (visual из Опции Б): L1 ассистивный аналитик → L5 fully autonomous LAWS; над L4 — «treaty negotiation here». Mapping: MSS=L1; Saker Scout=L2; Fury supervised CCA=L3; Patriot/S-400 auto под ROE=L4 boundary; LAWS=L5.
- **4.2. UN GGE timeline.** UNGA 5 Nov 2024 **161/3/13**; 6 Nov 2025 **156/5/8**. Sept 2025 GGE — 42 states joint statement, rolling text. UN SG target: treaty by **2026**. Against: Belarus, NK, Russia. Abstainers: China, India, Iran, Israel, Ukraine.
- **4.3. ICRC position.** Prohibit (a) unpredictable AWS, (b) AWS против persons; restrict остальные. «Ceding life-and-death decisions to machines is dehumanizing»; «не weapon system, а humans using it must comply with IHL».
- **4.4. Stop Killer Robots** — 30 countries full ban.
- **4.5. Maven walkout 2018 + Project Nimbus 2024.** Google leak Mar 2018; 4000+ letter; ~12 резигнировали; контракт не продлён. Anduril/Palantir/Scale подобрали. Урок: personal ethics ≠ industry regulation. Опция «не работать на DoD» теперь редкая (OpenAI ban removed Jan 2024; Anthropic-Palantir-AWS Nov 2024).
- **4.6. HITL как инженерный паттерн.** Calibrated uncertainty + abstention; pairwise comparison не free-form; structured outputs с explicit "I don't know"; mandatory human gates для kinetic action.
- **4.7. Russia votes против UN LAWS resolutions** — geopolitical context для студента-инженера в РФ.

**Media-rich:** (20) L1-L5 ladder; (21) UN GGE voting world map; (22) ICRC + SKR side-by-side; (23) Maven walkout timeline; (24) HITL drawio.

### Раздел 5 — Q&A + payoff (10 мин)

**Цель.** Закрыть лекцию практическими критериями + career angle + reading list, callback к keystone.

- **5.1. 7 критериев «когда не AI».** (1) FP-cost >> FN-cost → AI ассистент; (2) Adversarial domain → multi-sensor + abstention; (3) Single-point-of-failure — никогда (737 MAX, RQ-170); (4) Combat stress UI — testing under predicted failure modes (Vincennes); (5) Demo vs production (Lancet); (6) «Human ON the loop» с pre-authorised ROE OK, «OUT» оспаривает treaty; (7) Industry ethics — личный opt-out не масштабируется, legal regulation — рычаг.
- **5.2. Career angle.** МГТУ ИУ + ВКА им. Можайского + dual-use стартапы (VisionLabs, Cognitive Pilot) + civilian path (Роскосмос TerraTech / commercial sat analytics). **Без агитации.**
- **5.3. Reading list.** Scharre *Army of None* (CNAS); CSIS Russia drone ecosystem (Bondar Apr 2026); Abraham +972 (Lavender); ICRC position paper 2024; DARPA ACE briefings; GAO F-35 ALIS/ODIN; Stop Killer Robots briefs 2025.
- **5.4. Closing callback.** «Цепь Sense → Decide → Act — каждое звено имеет свои AI-инструменты, границы и failure modes. Инженер держит её в голове целиком».

**Media-rich слайды:** (25) критерии — dense visual checklist; (26) career-map drawio; (27) closing callback — keystone repeated as bookend.

---

## Провалы, ограничения и альтернативы (ENFORCED — ≥30% strict-in)

**11 strict-in failure блоков** (детали — в Outline по разделам): F-35 ALIS, SAR ATR adversarial, GPS spoofing civil aviation (Р1); IDF Lavender, USS Vincennes 1988, Lancet ATR rollback (Р2); Boeing 737 MAX MCAS, Patriot 2003 + Ukr F-16 2024, Replicator missed scale (Р3); Maven walkout + Nimbus, UN GGE + ICRC + SKR (Р4 целиком).

**Бюджет strict-in:**

- Р4 (целиком strict-in): 15 мин = **20%** + 5 слайдов.
- Failure-блоки в Р1-3 (8 блоков × 2-3 мин): ~16-20 мин = **21-27%** + 6-8 слайдов.
- Р5 критерии: 4 мин из 10 = **5%** + 1 слайд.

**Суммарно strict-in:** ~36-42 мин из 75 = **48-56%**; ~12-14 из ~32 слайдов = **38-44%**; chapter ~35-40% слов. Comfortable margin над ≥30% по всем 3 артефактам holistic.

**Counter-check.** Если на Phase 3/7 strict-in доля <30% или сконцентрирована в одном артефакте — verdict REVISE.

---

## Assessment

LO7 («этическая оценка применений ИИ») покрывается Разделом 4 + Razdelom 5 критериями. Семинар sem-09 — отдельная задача (не в scope); anticipated case study на одном failure-блоке (Lavender adversarial review process, или Lancet hardening vs premature deployment).

---

## Slide-budget превью (для Phase 5)

- Total ~32-35 слайдов; media-rich **18-20** (56-62%, выше ≥50% порога с запасом 2-3 на licence-fail risk).
- Section dividers: 6 (Р0-Р5); cover + lecture-map + Q&A: 3; content: ~22-25; pacing ~2-2.5 мин/content slide.
- **Lec-N-1 pattern compliance:** match lec-08 (cover + lecture-map + section dividers + dedicated Q&A; top progress bar только на dividers + cover).

---

## Open questions для Phase 1 critics

1. **Hook финал — A vs B?** A (BEFORE/AFTER satellite, evergreen, нейтрален) vs B (F-35 ALIS failure-first, depressive mood). Рекомендую A.
2. **ALIS в Sense или в Act?** Сейчас в Sense (predictive maintenance side) как cross-cutting urok. Альтернатива — в Act (F-35 как case). Рекомендую Sense + один callback в Act.
3. **Раздел 4 — 15 мин достаточно?** 7 sub-sections × 2 мин ≈ 14 мин + 1 мин transition. Tight но реально. Кандидат к резке если методолог скажет «плотно»: L1-L5 ladder до 1 слайда без отдельных examples per level.
4. **Russian context — 15-20% объёма?** Сейчас ~7-8 из 32 = **22-25%** — чуть выше targeta, но Bauman audience-relevant. Принять или резать?
5. **Wisk Aero / eVTOL gray zone** — не включён в working cases. Рекомендую: не включать как отдельный case (нет места), но упомянуть строкой в keystone (dual-use лента — пример).
6. **DoD Directive 3000.09** — отдельный слайд в Razdele 4 или достаточно одной строки в Normative References?

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
