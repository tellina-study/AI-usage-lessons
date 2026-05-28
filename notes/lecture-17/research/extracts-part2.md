# Extracts from 16 industry chapters — Part 2 (L09-L16 + cross-lecture synthesis)

**Continuation of:** `extracts-from-16-chapters.md` (L01-L08 + intro).

**Cross-link:** part 1 (L01-L08) — `extracts-from-16-chapters.md`; cross-lecture synthesis (failure patterns, glossary, 7 criteria, open questions) at end of this file.

---

## L09 — AI в авиакосмической отрасли и оборонном комплексе

**Keystone-axis:** **OODA — Sense → Decide → Act (Boyd 1976)** + dual-use bridge + L1-L5 autonomy ladder.

**Главные cornerstone-концепты (L17 reusable):**
- OODA-цикл — фундаментальная декомпозиция AI-применения.
- L1-L5 autonomy ladder (military adaptation): assistive → supervised → conditional → high → full.
- LAWS (Lethal Autonomous Weapon Systems) regulatory debate.
- HITL / HOOL / HOTL (Human-In/On/Off-The-Loop) — три уровня участия человека.
- SAR (Synthetic Aperture Radar) — alternative to optical для weather/night.
- FMEA / FTA — Failure Mode Effects Analysis / Fault Tree Analysis.
- Dual-use technology — civilian aerospace + defense overlap.

**Documented failures + lessons:**
- **F-35 ALIS ($44k/flight hour baseline 2018).** Software-driven sustainment system; ложное срабатывание дороже пропуска. Урок: high-friction PdM на mission-critical → unsupervised AI ломает operational tempo.
- **JEDI cloud cancellation (DoD).** Vendor lock-in + protest cycle. Урок: government AI procurement structurally slow.
- **ODIN (replacement for ALIS).** Government-owned, disconnected mode, HITL для авторизации полётов. Урок: less ambition + explicit HITL = workable.

**AI-unfit criteria (L9):**
- Lethal autonomous decisions (regulatory + ethical block).
- Mission-critical PdM without human override.
- Single-vendor lock-in для military systems.

**Non-AI alternatives:**
- Human pilot judgment + checklist (CRM).
- SAR vs optical sensor fusion.
- FMEA/FTA classical safety engineering.

**Position на 2D-плоскости:** Aero/defense — high AI fit на Sense (satellite, radar fusion); restricted AI fit на Act (LAWS debate); autonomy capped at L3 для most mission-critical; L4-L5 только в unmanned narrow scenarios.

**Tools (2026):** Palantir AIP, Anduril Lattice, Shield AI Hivemind, Project Maven, Cognitive Pilot (РФ), VisionLabs, Aerostate (RU dual-use weather).

---

## L10 — AI в сельском хозяйстве

**Keystone-axis:** **Лестница AI-проникновения в АПК** — L1 поле → L2 робот → L3 животное → L4 цепочка поставок → L5 потребитель, с injection «closed-loop vs open-environment AI» как объяснительным механизмом провалов.

**Главные cornerstone-концепты (L17 reusable):**
- Closed-loop vs open-environment AI — ключевое различение для capstone.
- See & Spray как канонический success L1 (chiseled task + measurable ROI + clear alternative).
- AgriFM / AgriGPT (исследовательский этап, не commercial).
- Crop Wizard — RAG-grounded advisory, не отдельный foundation model.
- Foundation models в АПК — vendor concentration risk.

**Documented failures + lessons:**
- **Plenty Vertical Farms 2025.** $940M raised, $940M потерь, Chapter 11. Урок: AI optimization не закрывает капитальные расходы и electricity costs vertical farming.
- **Bowery Farming 2024.** $32M never-used capex. Урок: VF as a class — AI не закрывает energy economics.
- **Climate FieldView vendor lock-in.** Bayer-owned, data leaving farm → монополизация. Урок: data ownership в АПК — стратегический риск.
- **Monarch Tractor layoffs 38% (2025).** Autonomous tractor startup. Урок: open-field environment + capital intensity = sustained losses.

**AI-unfit criteria (L10):**
- Mixed canopy / dense growth → CV detection drops 95% → 70-80%.
- Low-margin commodity crops (corn, soy) — subscription doesn't pay back.
- Small farms <500 ha — fixed costs не размываются.
- Organic — no chemicals to selectively spray.
- Open-loop environment с rare events не в training data.

**Non-AI alternatives:**
- LaserWeeder — selective laser destroy, narrow task with measurable ROI.
- Mechanical cultivation (organic).
- Conventional broadcast herbicide (cheap baseline).
- Operations research для logistics (UPS ORION-style).

**Position на 2D-плоскости:** Агро — middle AI fit (closed-loop CV works, open-loop biological fails); autonomy L1-L2 для advisory, L3 в narrow tasks (See & Spray, LaserWeeder), L4-L5 — failed (Monarch, Plenty).

**Tools (2026):** John Deere See & Spray, BASF xarvio, Climate FieldView (Bayer), Carbon Robotics LaserWeeder, Monarch Tractor (deprecated), AgriFM (academic), Crop Wizard.

---

## L11 — AI в дискретном и процессном производстве

**Keystone-axis:** **Дискретное vs Процессное** — две модели производства с разной физикой, культурой, регуляторикой. AI входит в обе, но по-разному.

**Главные cornerstone-концепты (L17 reusable):**
- Дискретное (счётные единицы) vs Процессное (партии / поток).
- Pilot purgatory — 78% используют AI, только 5.5% получают эффект (MIT Sloan 2025).
- ISA-95 + Purdue Model (L0-L4 архитектурные слои; не путать с autonomy levels).
- Soft sensor (мягкий сенсор) — measurement через regression / kernel / NN.
- PAT (Process Analytical Technology, FDA 2004) — real-time process understanding.
- Industrial foundation models — пока не production-ready (2026).
- IEC 61131-3 PLC programming как «правда»; LLM не доверяют.

**Documented failures + lessons:**
- **Tesla 2018 «excessive automation».** Musk признал «humans are underrated». Урок: парадокс автоматизации — automation в зонах человеческой variability ломает throughput.
- **Boeing 737 MAX 9.** AI-augmented quality check missed door plug. Урок: CV not single arbitre safety; root-cause = process discipline.
- **Generic LLM на PLC code.** Confidently wrong syntax + safety-critical errors. Урок: для IEC 61131-3 LLM не подходит как кодогенератор.

**AI-unfit criteria (L11):**
- Safety-critical PLC code (IEC 61508 SIL 2/3).
- Process where ATEX Zone 0 (explosive atmosphere) — cybersecure mandate.
- High-mix low-volume где training data thin.

**Non-AI alternatives:**
- Classical PLC + ladder logic + human verification.
- Six Sigma + statistical process control.
- ISO 9001 audit trail (no AI).
- MPC (Model Predictive Control) с Lyapunov stability — НЕ AI.

**Position на 2D-плоскости:** Manufacturing — high AI fit на narrow CV/PdM (A0); mid на A1 advisory; low на A2 RL (Yokogawa FKDPP rare); rare A3. Autonomy concentrated at L0-L2.

**Tools (2026):** Siemens Industrial Copilot, Cognex VisionPro, Yokogawa FKDPP (RL первое промышленное), GE Predix (deprecated), PTC ThingWorx, КАМАЗ + Cognitive Pilot, Росатом, Норникель.

---

## L12 — AI в автоматизации производства и цифровые двойники

**Keystone-axis:** **Шкала автономии A0→A1→A2→A3 + цифровой двойник как мост** (Наблюдать → Советовать → Замыкать петлю → Действовать автономно).

**Главные cornerstone-концепты (L17 reusable):**
- A0-A3 autonomy scale (production-specific; не путать с ISA-95 L0-L2 архитектурой).
- Digital twin как мост: тестирование решений → хранение состояния → откат + объяснение.
- Sim-to-real gap — критическое для подъёма с A1 на A2.
- ISO/IEC 22989 + SAE J3016 как anchor standards.
- ГОСТ Р 57700.37-2021 «Цифровые двойники изделий».
- NVIDIA Omniverse + Cosmos (foundational models физического AI).
- Siemens Digital Twin Composer (CES 2026).

**Documented failures + lessons:**
- **75% digital twin projects fail.** Cassady на CES 2025 — оценка Gartner. Урок: digital twin без data infrastructure → bait-and-switch.
- **Southeast Asian Port (anonymized case).** Data layer audit показал 60% sensors offline или drift > 30%. Урок: «AI ready» означает «data ready».
- **Yokogawa FKDPP JSR — success после 35 days RL run on chemical plant.** Урок: RL works когда симуляция accurate AND HITL backup.

**AI-unfit criteria (L12):**
- Compliance процессы (FDA 21 CFR Part 11) без validation pathway.
- Cyber-physical systems где OT/IT boundary не cybersecure.
- Unknown physics — нет первопринципной модели для twin.

**Non-AI alternatives:**
- MPC (Model Predictive Control) с теорией Ляпунова.
- Classical SCADA + diferenciaciones engineer alerts.
- ISA-101 HMI design ergonomics.

**Position на 2D-плоскости:** Automation — full A0-A3 spread; AI fit varies by step (high on A0 CV, mid on A1 advisory, narrow A2, rare A3). Capstone-relevant пример autonomy ladder.

**Tools (2026):** Siemens Industrial Copilot + Digital Twin Composer, NVIDIA Omniverse + Cosmos, Yokogawa FKDPP, ABB Ability, Schneider EcoStruxure, Dassault 3DEXPERIENCE Twin, Beckhoff TwinCAT, Ansys Twin Builder.

---

## L13 — AI в логистике и транспорте

**Keystone-axis:** **Лестница структурированности среды (5 уровней)** + 7 критериев decision framework.

| Уровень | Среда | Пример |
|---|---|---|
| L1 | Контролируемая | Склад, порт, рельсы |
| L2 | Полуструктурированная магистраль | Aurora Даллас-Хьюстон, КамАЗ М-11 |
| L3 | Городская улица robotaxi | Waymo, Cruise (failed), Apollo Go |
| L4 | Последняя миля города | Starship, Coco, Zipline, Nuro |
| L5 | Чёрный лебедь / exception | Suez Ever Given, Houthi crisis, COVID |

**Главные cornerstone-концепты (L17 reusable):**
- ODD (Operational Design Domain) — главная дисциплина L3+ систем.
- HD-map vs vision-only (Waymo vs Tesla — философская ставка).
- VRP / TSP / EOQ / safety stock — classical OR альтернативы AI.
- SAE J3016 L0-L5 — автомобильные уровни автономии.
- Структурированность среды — главный предиктор успеха AI (ортогонально SAE).

**Documented failures + lessons:**
- **Cruise Oct 2023.** Pedestrian dragged 20 ft; ODD expansion без validation. Урок: Decide-stage fail (pull-over wrong response); недостаточная ODD discipline.
- **30+ autonomous trucking startups 2017-2022, выжило 3-4.** Embark, Starsky, TuSimple — все провалились. Урок: highway autonomy capital-intensive + brittle business model.
- **Uber Tempe 2018.** Pedestrian killed; safety driver distracted. Урок: HITL не работает когда задача мониторинга — boring.
- **Tesla Autopilot ~50 fatal crashes по NHTSA.** Vision-only stack edge cases. Урок: ODD не enforced.
- **Suez Ever Given (March 2021).** 12% world trade blocked 6 days. Урок: black swan = out-of-distribution; ML не помогает.

**AI-unfit criteria (L13):**
- Open urban environment beyond mapped ODD.
- Black swan / level 5 events.
- Sidewalk robots in snow / vandalism.
- Drone in dense populated areas (FAA blocks).

**Non-AI alternatives:**
- UPS ORION (OR + heuristics) — $300-400M/year savings.
- EOQ + safety stock formulae (Ford Harris 1913).
- Human dispatcher in exception team.
- Scenario planning Shell-style.

**Position на 2D-плоскости:** Logistics — full spread; warehouse high AI fit + autonomy L4; urban robotaxi low AI fit / autonomy L3 only narrow; black swan effectively non-AI domain.

**Tools (2026):** Waymo, Apollo Go, Pony.ai, WeRide, Tesla FSD, Mobileye Chauffeur, Aurora Driver, КамАЗ-54901 + Cognitive Pilot, Symbotic, Amazon Robotics (Sparrow / Sequoia / Proteus / Vulcan), Locus Robotics, ZPMC port cranes, KONUX, Starship Technologies, Coco, Zipline, Nuro, Avride/Nebius, Google OR-Tools, Gurobi, CPLEX.

---

## L14 — AI в телекоммуникациях, сетевой инфраструктуре и кибербезопасности

**Keystone-axis:** **«Лестница автономии AI: Видит → Решает → Действует»** (рабочий термин лекции; canonical refs: Parasuraman, Sheridan & Wickens 2000; SAE J3016; OODA; Endsley 1995).

**Главные cornerstone-концепты (L17 reusable):**
- Три уточняющих вопроса вендору: baseline до AI / окно измерения и методология / change-control и rollback.
- MITRE ATLAS — каталог атак на AI системы (analog OWASP Top 10 для LLMs).
- RIC (RAN Intelligent Controller) — central brain Open RAN.
- Три класса рисков: AI-augmented defense fails / AI as weapon / attacks on AI itself.
- LO-failure как central — minimum 6 critеria «AI не нужен / вреден» (этот LO задаёт фрейм capstone).
- Видит = agentic LLM ok; Решает = RAG + HITL; Действует = по умолчанию rule-based + canary deploy + go/no-go.

**Documented failures + lessons:**
- **CrowdStrike BSOD 19 июля 2024.** Falcon channel file → 8.5M devices crashed, $5B+, Delta cancelled 7000 flights. Урок: Act-level автоматизация без canary deploy + rollback = catastrophic.
- **Cloudflare NOC 18.11.2025.** Config-cascade 5h 38min full restore. Урок: даже well-engineered automation cascades cause hours of outage; rollback as P1.
- **SOAR auto-block phishing.** Vendor pitch: AI блокирует. Reality: high false-positive rate блокирует legitimate emails → adoption stalls.
- **AI-generated phishing 2024.** AI lowered cost-per-attack 95%. Урок: AI as adversary's tool — defender's cost-per-block must also drop.

**AI-unfit criteria (L14):**
- Act-level full-autonomy без canary + rollback + go/no-go gate.
- Decision-level без HITL для high-blast-radius actions.
- Pre-deployment without baseline measurement / change-control documentation.

**Non-AI alternatives:**
- Rule-based + signature match (Snort, YARA) для known threats.
- Human SOC analyst tiering.
- Canary deployment + feature flags.
- Penetration testing classical.

**Position на 2D-плоскости:** Cyber/telecom — high AI fit на Sense (anomaly detection); mid на Decide (RAG+HITL); low на Act (defaults to rule-based). Autonomy strictly bounded by blast radius.

**Tools (2026):** CrowdStrike Falcon, Microsoft Defender XDR, SentinelOne, Darktrace, Palo Alto Cortex XSIAM; AIOps: Datadog AI, Splunk + Cisco AI; Nokia AVA, Ericsson AI, Mavenir RIC; MITRE ATLAS framework.

---

## L15 — AI в научных исследованиях

**Keystone-axis:** **Лестница научного цикла** (Variant A) — Hypothesis → Design → Experiment → Analyse → Write → Review.

**Главные cornerstone-концепты (L17 reusable):**
- Foundation model (фундаментальная модель) — общий термин курса.
- Open-world vs closed-world (научный цикл = смешанный).
- Augmentation (расширение человеческой работы) vs autonomous lab (self-driving lab).
- Hallucinated citations (peer review hallucinations).
- Paper mill (фабрика статей).
- Reproducibility crisis (кризис воспроизводимости).
- HITL для научной проверки.
- Inverse design (обратное проектирование).
- DFT / MD первого принципа — classical computational chemistry альтернатива.
- Bayesian optimization (BO) + Gaussian process (GP).
- AlphaFold Nobel 9 Oct 2024 vs Galactica retracted 17 Nov 2022 — side-by-side framing.

**Documented failures + lessons:**
- **Meta Galactica (15-17 Nov 2022).** Запуск 15 ноября, отозвана 17 ноября после vibrant hallucinations про авторов / источники. Урок: scientific text generation без grounding = paper mill enabler.
- **Hallucinated citations in published papers (2024-2025).** Несколько high-profile retractions where AI invented sources. Урок: citation verification mandatory.
- **Paper mills + AI-amplified.** ScienceDirect retractions сотни в год; AI-amplified production. Урок: peer review system overwhelmed.

**AI-unfit criteria (L15):**
- Hypothesis generation in novel domains (no prior data → hallucinations).
- Citations as facts (always verify).
- Open-world science где physics unknown.
- Peer review «replacement».

**Non-AI alternatives:**
- Classical DFT / MD computational chemistry.
- Bayesian experimental design (formal статистика).
- Human peer review with checklist.
- Pre-registration of hypotheses.

**Position на 2D-плоскости:** Наука — bimodal: closed-world (protein folding, drug-target search) high AI fit + autonomy L3-L4; open-world hypothesis = low AI fit, autonomy L1 only.

**Tools (2026):** AlphaFold3 (DeepMind), Galactica (defunct), Elicit, Consensus, scite.ai, Semantic Scholar AI, OpenReview, AutoML for science; self-driving labs (Coscientist, ChemCrow).

---

## L16 — AI в нефтегазовой отрасли и добыче ресурсов

**Keystone-axis:** **Матрица 2×2 «доступность данных × определённость процессов»**:
- Q1 — зрелое производство (data ✓, process ✓): AI как мультипликатор.
- Q2 — метановая MRV (data ✓, process ✗): AI на baseline measurement.
- Q3 — разведка фронтиров (data ✗, process ✓): AI ограничен моделями физики.
- Q4 — новые опоры (data ✗, process ✗): CCS, EGS — AI experimental.

**Главные cornerstone-концепты (L17 reusable):**
- 2×2 матрица data × process determinism как декомпозиция отрасли.
- Чисто процессное (long horizons, sensor-heavy).
- ATEX Zone 0 + IEC 61508 SIL 2/3 — safety regulatory baseline.
- CCS (Carbon Capture & Storage) + EGS (Enhanced Geothermal) — energy transition AI.
- 24/7 clean power for data centers as new demand driver.
- Drone + LiDAR + computer vision для inspection.
- Methane MRV (Measurement Reporting Verification) — EU CBAM driver.

**Documented failures + lessons:**
- **DeepMind Wind Farm Energy 2019.** Multi-$Mln pilot; never deployed Google-side. Урок: energy optimization pilot ≠ production deployment.
- **Pre-salt drilling AI 2018-2022.** Brazilian deep-water predictions overpromised; classical seismic still works better. Урок: rare events + thin training = ML fails.
- **CCS pilot failures.** Several billion-dollar CCS pilots stopped mid-construction. Урок: economics dominate AI optimization on AI ROI tiny.

**AI-unfit criteria (L16):**
- Black swan oil price events.
- Unknown reservoir physics (Q3).
- New technology без historical data (Q4 EGS / CCS).
- ATEX explosive zone where non-explosive-rated AI hardware fails.

**Non-AI alternatives:**
- Classical seismic interpretation by geophysicist.
- Reservoir simulation (Eclipse, CMG) — physics-based.
- Operations research для drilling schedule.
- ATEX-rated PLC + classical control.

**Position на 2D-плоскости:** Oil/gas — quadrant-dependent; Q1 high AI fit + autonomy L2-L3 (Aramco predictive maintenance); Q4 low AI fit + autonomy L0-L1 (experimental). Long horizon production = process manufacturing extension.

**Tools (2026):** Aramco AI predictive maintenance, Shell digital twin, BP Project ARC, Halliburton DecisionSpace, Schlumberger Delfi, Equinor Volve open dataset, Microsoft Energy Data Services, Carbon Mapper (methane), MethaneSAT.

---

## Сводная таблица: 16 отраслей на 2D-плоскости

| Лекция | Отрасль | Доминирующий AI fit | Типичный autonomy уровень | Position quadrant |
|---|---|---|---|---|
| L01 | Введение (meta) | N/A | N/A | sets axes |
| L02 | Fundamentals (meta) | N/A | N/A | explains why |
| L03 | Архитектуры (meta) | N/A | N/A | tool selection |
| L04 | Software dev | HIGH (code grounded) | L2-L3 (PR-from-spec capped) | upper-right |
| L05 | Финансы / ритейл | MID-HIGH (closed-world) | L1-L3 (advisory + auto-fraud-block) | upper-mid |
| L06 | CAD/CAM | MID (class-dependent) | L1-L3 (optimization L3) | mid |
| L07 | Медицина / фарма | HIGH narrow imaging / LOW open | L1 (HITL mandatory) | upper-left to mid |
| L08 | Креатив | HIGH (mass-prod assets) | L2-L3 (curation) | upper-mid |
| L09 | Aero / defense | HIGH Sense / restricted Act | L1-L3 (LAWS debate caps) | upper-mid; |
| L10 | Агро | MID (closed L1 / open L4-L5) | L1-L3 narrow; failed L4 | mid-low |
| L11 | Manufacturing (discrete / process) | MID (CV high / RL rare) | L0-L2 most | mid |
| L12 | Factory automation + twins | MID (A0-A1 high / A3 rare) | A0-A3 spread | mid-low for A3 |
| L13 | Logistics | HIGH L1 / LOW L5 | L4 warehouse / L3 urban / 0 black swan | bimodal |
| L14 | Telecom / cyber | HIGH Sense / LOW Act | bounded by blast radius | upper-mid Sense, low Act |
| L15 | Science | bimodal closed/open | L3-L4 closed / L1 open | bimodal |
| L16 | Oil/gas | quadrant-dependent | L0-L3 by quadrant | quadrant matrix |

---

## Cross-lecture failure patterns (top-12 для cheat-sheet #3)

1. **Open-world prediction без environmental closed-loop** — Zillow iBuying (L5), Monarch Tractor (L10), Cruise urban robotaxi (L13). Альтернатива: ограничить ODD / pilot scope; classical OR.
2. **Reliability compounding в multi-step agent** — $4,200-петля (L3), agentic SE without budget guard (L4). Альтернатива: budget cap + max-turns + HITL checkpoint.
3. **Vendor demo ≠ production performance** — Devin (L4), IBM Watson Health (L7), Epic Sepsis (L7), Klarna AI CS (L5). Альтернатива: replicate vendor benchmark on your data before commit.
4. **HITL boring → не работает** — Uber Tempe 2018 (L13), F-35 ALIS (L9). Альтернатива: HOOL (Human-On-The-Loop) или rule-based.
5. **Excessive automation in human-variability zones** — Tesla 2018 (L11), Boeing 737 MAX 9 (L11). Альтернатива: Jidoka — augment, don't replace.
6. **Act-level autonomy без canary + rollback** — CrowdStrike BSOD 2024 (L14), Cloudflare 2025 (L14). Альтернатива: canary deploy + feature flags + explicit go/no-go.
7. **Galactica-class scientific hallucination** — Meta Galactica 2022 (L15), citation hallucinations. Альтернатива: grounding (RAG with verified sources) + human review.
8. **Voice / chat fraud / overpromise** — Wendy's drive-thru (L5), Air Canada chatbot (L5), deepfake CEO voice (L8). Альтернатива: rule-based menu + human escalation; C2PA provenance.
9. **Mock + verbatim training data leak** — Getty v. Stability (L8), NYT v. OpenAI (L8). Альтернатива: licensed datasets + provenance audit.
10. **Vendor lock-in для regulated industries** — Climate FieldView (L10), F-35 ALIS (L9), JEDI (L9). Альтернатива: government-owned ODIN-style; data ownership clauses.
11. **Slopsquatting / supply-chain via hallucinated names** — npm/pip name attacks (L4). Альтернатива: SBOM verification; allow-list for imports.
12. **Pilot purgatory / 90-95% projects don't reach production** — MIT Sloan 2025 (L11), Gartner 2025; РФ CNews 90% (L1); 75% digital twin (L12). Альтернатива: explicit GO/NO-GO gates; baseline measurement; PoC budget cap.

---

## Cornerstone glossary candidates (cross-lecture; for cheat-sheet anchor)

- **AI Effect / moving target** (L1) — definitions retreat.
- **Pearl's three levels** (L1) — association / intervention / counterfactual.
- **Narrow vs General AI** (L1) — caveat on AGI predictions.
- **OODA** (L9) — Observe / Orient / Decide / Act.
- **HITL / HOOL / HOTL** (L9, L13) — human participation levels.
- **ODD (Operational Design Domain)** (L13) — discipline of autonomy bounds.
- **Pilot purgatory** (L11) — 90-95% projects fail to reach production.
- **Closed-loop vs open-environment AI** (L10, L7) — explanatory mechanism for failures.
- **Reliability compounding** (L3) — multi-step agent error multiplication.
- **Slopsquatting** (L4) — hallucinated package supply-chain attack.
- **Soft sensor** (L11) — ML-based virtual measurement.
- **Digital twin as bridge** (L12) — sim → real autonomy escalation.
- **Foundation model** (L15) — общий термин.
- **MITRE ATLAS** (L14) — AI attack catalog.
- **Reproducibility crisis** (L15) — science context for AI augmentation.
- **Reward hacking / data poisoning / prompt injection / jailbreak / adversarial examples** (L1, L14) — расширенный security catalog.

---

## 7 критериев AI/non-AI decision (synthesis для cheat-sheet #1)

Cross-lecture distillation:

1. **Closed-loop vs open-environment.** Среда predictable + контрольная петля быстрая → AI fit ↑. Open environment с rare events → AI fit ↓. (L10, L7, L13)
2. **Training data availability + relevance.** Достаточно labeled data + matches deployment distribution → AI fit ↑. Distribution shift / thin training → AI fit ↓. (L1, L2, L7, L9)
3. **Repeatability / volume.** Высокий volume + repeatable task → AI ROI high. One-off / bespoke decisions → human better. (L4, L6, L13)
4. **Cost-of-error / blast radius.** Low cost-of-error → AI tolerable; high cost (safety / regulatory / financial) → HITL or non-AI. (L7, L9, L11, L14)
5. **Ground-truth availability.** Compiler / lab test / market signal as feedback → AI fit ↑. Pearl level 3 questions → AI fit ↓. (L4, L7, L15)
6. **Explainability / audit requirement.** Regulatory mandate (FDA / GDPR / EU AI Act) → AI fit conditional on SHAP / LIME / glass-box. (L7, L11, L14)
7. **Economic case / baseline alternative cost.** AI must beat well-known classical alternative (OR / EOQ / MPC / human expert) on $$ basis. If alternative is good enough → no AI. (L13, L10, L6, L11)

---

## Открытые вопросы для GATE A (load-bearing decisions)

1. **Лестница автономии L0-L5 versus A0-A3 versus 5-level structuredness — какая нумерация для capstone?** Курс уже использует разные нумерации: SAE J3016 L0-L5 (L9, L13), A0-A3 (L12), 5-level structuredness (L13), 4-level A/B/C/D (L4). Для capstone предлагается единая L0→L5 (advisory → fully autonomous) — owner подтверждает?
2. **2D-плоскость финальный naming — «AI fit» подходит, или лучше «AI applicability» / «когда AI работает»?** Семантика та же; формулировка для русско-язычной аудитории + slides title.
3. **Top-12 провалов — final selection.** Предложен список выше; owner может реорганизовать или ограничить top-10 / top-15.
4. **Cheat-sheet #1 — 7 критериев vs 5 vs 10?** Зависит от A4 layout density.
5. **A1 master-poster — каков formal output?** PDF poster generated через какой tool? (PowerPoint export / drawio / SVG via mermaid?)
6. **Lec-12 reflection (#142) и Lec-13 reflection (#140) — должны feed cheat-sheet #3 failure list?** Если да — нужны cross-reference маркеры.
