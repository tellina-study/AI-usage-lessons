# Лекция 11: AI в дискретном и процессном производстве — v1 plan

## Метаданные

- Lecture 11 | Module 2 | 75 мин + Q&A (~5 мин буфер)
- LO: LO1a, LO1b, LO2, LO7, LO8 (split LO1; manifest mapping LO1+LO2+LO7+LO8)
- Audience: студенты-инженеры 3 курса (универсальная, generic — без named institutions)
- Issue: #127 | Status: v1 (Phase 1 draft, до critique) | Date: 2026-05-21
- Keystone axis: **«Discrete vs Process — две модели производства»** (research/05 Вариант C + injection decision-framework в §4 из Варианта D)
- Hook A primary: Tesla Giga Press + Musk «humans are underrated» (2018). Hook B backup: GE Predix $4B + Foxconn Wisconsin «8th wonder» split-screen

---

## Topics Covered

Дискретное (CV, PdM, коботы, generative process planning, индустриальные foundation-модели) + процессное (мягкие сенсоры, MPC/RL гибрид, PdM на edge, FDA Part 11 / ATEX) + failure-таксономия (hype-collapse, over-automation, distribution drift, pilot purgatory) + decision-framework AI vs не-AI + российский контекст (КАМАЗ, Норникель, СИБУР).

## Prerequisites

Лекция 3 (архитектуры AI-систем — edge AI на PLC, foundation-модели); Лекция 6 (generative CAD/CAM — граница «AI до производства» vs «в производстве»); Лекция 7 (HITL, FDA, GxP — symmetric для §3.4); Лекция 9 (mission-critical AI, OODA, F-35 ALIS — one-line callback в §3.3). **Активный словарь:** distribution shift, FP/FN, accuracy/precision/recall, edge vs cloud, HITL, GxP, regression baseline.

## Normative References

- **ISA-95 / Purdue Model** — 5-уровневая иерархия (L0 process ↔ L4 ERP); опорная сетка в §3, **не** keystone.
- **IEC 62443** — industrial cybersecurity (edge AI рядом с PLC не расширяет attack surface).
- **FDA 21 CFR Part 11** — electronic records / audit trail (фарма); запрет autonomous batch release.
- **GAMP®5 + ICH Q8-Q11** — фарма-валидация AI как software.
- **ATEX / IECEx** — взрывоопасные зоны; в Zone 0 non-certified AI-hardware запрещён.
- **ISO 9001 + Six Sigma + DOE** — альтернативный QA-инструмент; DOE даёт защищаемую traceability.
- **ГОСТ Р 57700.37-2021** — цифровые двойники (РФ); foreshadow к Лекции 12.
- **Доктринальный фон:** Bainbridge «Ironies of Automation» (1983) — automation paradox.

## Learning Objectives

1. **LO1a (Remember).** Назвать два типа производства (дискретное / процессное) и для каждого 3-4 dominating 2026-инструмента AI с направлением adoption.
2. **LO1b (Apply).** Для конкретного кейса определить колонну (discrete / process), AI-стек, и структурный риск на стыке.
3. **LO2.** Критически оценить vendor-claim «AI -70% downtime / +60% efficiency» — отличить demo от production-baseline, запросить **3 уточняющих вопроса** (baseline, окно измерения, intervention list). Canonical: Tesla 2018 Musk admit. Backup: Foxconn FoxBrain «80% configuration work» (self-claim).
4. **LO7.** Описать regulatory landscape (FDA Part 11 в фарма, ATEX в химии, ISO 9001 / Six Sigma в discrete), различить «decision support» vs «autonomous controller», обозначить позицию инженера.
5. **LO8 (центральный, failure-bucket).** Сформулировать **≥5 критериев** «AI не нужен / не работает», применить к учебному кейсу, предложить non-AI альтернативу (SPC, DOE, MPC, RCM, physics-sim, rules-vision). §4 — payoff.

---

## Несущая ось (keystone) — ENFORCED

**Ось.** «Дискретное vs Процессное — две модели производства». Производство — две parallel ветви с **разной физикой, организационной культурой, регуляторной картой**; AI применяется по-разному; failure modes разные. Engineer-выпускник обязан уметь сказать, в какой колонне работает, какой AI-стек применим.

**Keystone slide (§0, после cover + lecture-map, до первого погружения).** Заголовок: «Две модели производства. AI входит в обе — но по-разному». Двухколонная схема: **Левая Дискретное** (иконка авто, «дискретные единицы → CV, коботы, generative process planning»; failure-метка «Tesla 2018»). **Правая Процессное** (иконка ректификационной колонны, «непрерывный поток → мягкие сенсоры, MPC/RL, PdM»; failure-метка «F-35 ALIS $44 000/час»). **Соединительный пояс:** foundation-модели, agentic-копилоты, **pilot purgatory** (95% не доходят до production, MIT Sloan 2025).

**Counter-check.** Заголовок и 1-я строка — про **саму ось**, не про устройство курса / защиту подхода / recap. Если методолог скажет «keystone про другое» — STOP, структурный gap (lec-04 cost ~5 циклов).

**Hot zones провалов.** «Model ↔ reality» — distribution shift при смене продукта (§2 CV) / сырья (§3 RL) / pilot→production (§1). «Discrete ↔ process» — AB InBev (continuous brewing + discrete packaging требуют двух стеков). «AI ↔ оператор» — automation paradox (Bainbridge 1983), Toyota Jidoka stance, HITL по FDA/ATEX.

**Connection к LO8.** LO8 — центральный. Keystone делает критерии «AI не нужен» видимыми сразу: failure-метки под обеими колоннами + pilot purgatory в поясе. §4 — payoff.

**Что НЕ делать:** сводить discrete только к CV-QC / process только к RL; концентрировать failure в §4; «магическая пилюля + дисклеймер»; keystone про «AI-революцию» (провозглашение, не ось).

---

## Hook (8 мин)

**A primary — Tesla GigaCast + Musk 2018.** Hero: Tesla Giga Press underbody real photo (research/06 C1; Tier 2 Wikipedia Commons или Tier 3 Tesla press). Narrative: Giga Press запущен 2020; май 2024 — Tesla отступила от next-gen gigacasting для Model 2. Это **вторая** отмена — апрель 2018, кризис Model 3, Маск: «**Excessive automation… my mistake. Humans are underrated**». Central question: если Tesla отступила дважды, GE сожгла $4B на Predix, 95% пилотов не доходят до production (MIT Sloan 2025) — **где AI работает, где нет, как инженер должен решать?**

**B backup — GE Predix + Foxconn Wisconsin** split-screen (если Tesla licensing не закрывается). Anti-signal hook («8th wonder» Trump 2018 → 1 500 рабочих 2024 → Microsoft Fairwater). Решение A vs B — Phase 5 после acquisition attempt.

**Hook НЕ делает:** «AI трансформирует производство» (hype-positive); abstract framework без anchored image; empirical test на 2026-модели.

---

## Структура (5 разделов + Q&A)

### Раздел 0 — Hook + keystone + lecture-map (5-7 мин)

**Цель.** Зацепить Tesla retreat; предъявить ось discrete vs process; задать central question.

**Sub-sections:** 0.1 Cover + LO + roadmap (1 мин); 0.2 Hook hero — Tesla Giga Press + Musk quote + 2024 retreat (3-4 мин); 0.3 Keystone двух моделей (1 мин); 0.4 Lecture-map + glossary mini — 12 acronyms × 2 колонки: ISA-95, MES, SCADA, PLC, OEE, SPC, MPC, APC, PdM, RL, CV, soft sensor (1-2 мин).

**Connection к keystone:** §0 **есть** keystone. Failure-bucket: ~30% (Tesla retreat + 2 failure-маркера). **Slides:** s01-s05.

### Раздел 1 — Что общее для обеих моделей (12 мин)

**Цель.** Adoption landscape 2025-2026 + индустриальные foundation-модели + pilot purgatory как universal + 3 canonical hype-collapses. Общий failure-слой для обеих колонн. **Slides:** s06-s12. **Failure-bucket:** ~42%.

**Sub-sections:**
- 1.1 (3 мин) — **Adoption landscape.** McKinsey State of AI 2025: 78% используют AI, **только 5.5% high performers** (EBIT >5%). 2/3 в pilot purgatory. **Рыночные оценки расходятся**: Markets and Markets $34.18B→$155.04B (CAGR 35.3%); Fortune $7.6B; Precedence $8.57B. **Pedagogical point**: vendor estimates расходятся в 5×; читайте methodology. `[VFY-day-of]`.
- 1.2 (4 мин) — **Индустриальные foundation-модели.** Siemens Industrial Foundation Model (Hannover Messe 2025, 150 PB engineering data + 1 000+ AI-патентов); Foxconn FoxBrain (Llama 3.1 70B derivative, injection-molding параметры). **Критичная граница:** foundation-модели в industry — **augmentation tool для инженера**, **не autonomous controller**. Помогают разбирать чертежи, отвечать на эксплуатационные вопросы — **не управляют станком напрямую**. Первый трендовый разрыв с consumer LLM.
- 1.3 (5 мин) — **Hype-collapses canonical trio.** **GE Predix (2011-2020):** $4B+, «be everything to everyone», собственное промышленное облако против AWS, развал 2018, продажа частями. Урок: industrial AI ≠ general cloud AI; size of investment ≠ результат. **IBM Watson Health + Manufacturing (2018-2022):** «-47% downtime, -48% defect rate» маркетинг → продан за parts за $1B (2022). Демо-product gap. **Foxconn Wisconsin (2018-2024):** «8th wonder of the world», $10B обещано, $3B subsidy → 10 000 рабочих стали 1 500 → LCD → coffee kiosks → fish farming considered → Microsoft AI data center на руинах ($3.3B, май 2024). Anti-signal: «чудо» от главы государства предсказывает провал.


### Раздел 2 — Дискретное производство deep-dive (17 мин). **Slides:** s13-s22. **Failure-bucket:** ~47%.

- 2.1 (4 мин) — **CV-инспекция.** **BMW GenAI4Q (Regensburg, 2025):** bespoke catalogue per vehicle; «FACTORY OF THE YEAR 2024». **TSMC:** wafer defect detection 95% accuracy, +10-15% yield. **Boeing 737 (2024+):** CV на fuselage + photo-driven part validation (декабрь 2025). **Anti-кейс:** AI inspection **не предотвратил** door-plug blow-out Alaska Airlines 737 MAX 9 (январь 2024); mechanics reinstalled improperly; FAA cap 38/мес; Everett delayed 12 мес; Spirit AeroSystems 50 jets rework. **Урок:** CV — последняя линия защиты, не первая. Без upstream sign-off + audit trail AI не починит. «Garbage in, garbage out».
- 2.2 (3 мин) — **PdM на discrete.** Tata Steel: -20% downtime / -15% maintenance cost (заявка). BMW AIQX: realtime sensor+image. **Honest reality check:** vendor обещает -25-40% / -50-70%; McKinsey 2025 — большинство not capturing value; ROI 8-14 мес; только 5.5% high performers.
- 2.3 (3 мин) — **Коботы + worker-augmentation.** Hyundai + Boston Dynamics: Spot для exterior QC; Atlas humanoid first commercial deployment в HMGMA. Foxconn FoxBrain: «~80% configuration work» — vendor self-claim (LO2 hook). Toyota GAIA: 8 000 (2023) → 10 000 (2024) AI models by employees; 10 000 hours saved. **Jidoka 2.0:** AI = augmentation, не replacement.
- 2.4 (4 мин) — **Tesla 2018 — canonical over-automation.** Q1 2018: target 2 500 Model 3/week → 2 020. Apr 13: Musk «excessive automation… my mistake. **Humans are underrated**». Failed: conveyor system Model 3 («we got rid of that whole thing»); robotic «fluffer» для fiberglass mats; over-automated battery module. **Корневая причина (IMD):** заменял людей там, где variability — feature, не bug. **Структурный урок:** automation paradox (Bainbridge 1983) — чем больше автоматизация, тем критичнее остающиеся operators. **Альтернатива:** Toyota Production System + Jidoka. **Follow-up:** GigaCast retreat 2024 — Tesla опять push, опять retreat. Компании не учатся «один раз».
- 2.5 (3 мин) — **Границы CV.** Low-contrast defects (CV brittle); distribution shift при смене продукта (часто 5+ моделей per plant); scarce defect labels (1-2% rate → class imbalance). **Альтернативы:** physical signal amplification (structured/polarized light, X-ray, thermography) **до** ML; rules-based vision для controlled environments — 60-70% inspection workloads достаточно.


### Раздел 3 — Процессное производство deep-dive (17 мин). **Slides:** s23-s30. **Failure-bucket:** ~41%.

- 3.1 (4 мин) — **Мягкие сенсоры + AI-formulation.** **BASF Geismar (2023-2024):** soft sensors дают real-time оценку quality parameters без physical lab samples; **-30% batch defects** без increased testing. R&D formulation 18 мес → 3 недели. **Pfizer Vox (2024-2025):** GenAI на AWS Bedrock + SageMaker; identify «golden batch» parameters, detect anomalies, **recommend actions to operators**. **+20 000 vaccine doses per batch** (mRNA). «Recommend», не autonomous — consistent с FDA Part 11.
- 3.2 (4 мин) — **MPC / RL.** **Yokogawa + JSR FKDPP (2022):** first production-precedent RL в chemical plant — 35 days (840 ч) автономного контроля distillation column. Разрешает компромисс output quality / energy / throughput в нелинейной системе — то, что PID/APC не могли. Japan PM Prize 2023. **CIRL (2024-2026):** PID в deep RL (BASF + Royal Academy of Engineering) — гибрид, не «RL вместо PID». **RL distribution drift:** batch transitions (OOD → unsafe); смена feedstock (stale policy); seasonal shifts; equipment wear. **Альтернатива:** MPC — explicit model, объясним, validated; dominates process control. RL дополняет на high-level scheduling.
- 3.3 (3 мин) — **PdM + edge AI.** **POSCO 180 edge nodes (2024):** failure detection independently of corporate network; +5% efficiency, -10% energy, +3% yield. Edge ≠ cloud: latency (1-10 мс), resilience, bandwidth (4K@30fps), privacy. **Holcim 100 plants (2024-2026):** kiln optimization + PdM (C3 AI). **CEMEX + Optimitive: 10% energy savings, ROI 18 мес; -2-5% CO2 per tonne clinker.** **F-35 ALIS callback (lec-09):** заявлял -25-40% cost; реальность $44 000/час (выше F-22), GAO критика, заменён ODIN. **Уроки PdM:** работает где (a) feedback loop fast, (b) ground truth available, (c) FP ≤ FN cost. Long MTBF + safety-critical → preventive + CBM.
- 3.4 (3 мин) — **Regulatory blockers.** **FDA 21 CFR Part 11 (фарма):** electronic records → audit trail + validated systems + traceable changes. Black-box ML — нет audit trail. **AI не может быть final decision-maker; HITL обязателен**. GAMP®5 validation. Работает: batch quality prediction → operator approval. Не работает: autonomous AI batch release. **ATEX:** AI помогает в predictive monitoring gas / temp / dust — не заменяет ATEX-certified hardware. В Zone 0 non-certified AI hardware запрещён физически. **Урок:** Regulation уже есть; AI должен fit existing frameworks; audit trail обязателен.
- 3.5 (3 мин) — **Российский контекст** (public-verifiable only). **Норникель:** AI на flotation/grinding достиг industrial-operation stage; ноябрь 2024 — agreement с Газпром нефть. **СИБУР Marketplace технологического моделирования** (Q1 2025 → 2026 full); контекст импортозамещения (100% critical infrastructure → domestic software к 2027). **ММК / НЛМК / Северсталь:** общие декларации без specific metrics; параллельный кризис отрасли (Severstal profit -55% в 2024). **Pedagogical point:** public-disclosure скудна → анти-pattern в reporting, не proof отсутствия adoption. Различать PR statement и измеримый эффект — LO2.


### Раздел 4 — Карта решения «когда AI не нужен» + альтернативы (13 мин)

**Цель.** PEAK failure-bucket section + payoff лекции для LO8. Синтез: 10 критериев + альтернативные инструменты + hybrid patterns + decision framework. Студент должен унести applicable mental model. **Slides:** s31-s35. **Failure-bucket:** ~100%.

**Sub-sections:**
- 4.1 (4 мин) — **10 критериев «AI не подходит / не работает»** (slide-of-the-day, читаются вслух): (1) MTBF >1 year — insufficient data для PdM; (2) FP cost >10× FN — SPC + RCM лучше; (3) regulatory audit-trail — black-box не работает, explainable / hybrid; (4) SIL 2/3 safety — ML certification сложнее; (5) known physics — CFD/FEA/kinetics надёжнее; (6) operator distrust — workaround неизбежен (Toyota proof); (7) pilot без go-criteria — 80-95% pilot purgatory; define baseline + go/no-go до pilot; (8) ATEX Zone 0 — physical hardware restriction; (9) DOE-acceptable + few variables — DOE предпочтительнее; (10) demo-hype без 6-mo production track record — buyer beware. **3 уточняющих вопроса:** baseline до AI; measurement window; intervention list.
- 4.2 (4 мин) — **Альтернативные инструменты.** SPC + Six Sigma — large-batch QC, univariate, pharma-friendly; DOE — formulation / parameter opt, ≤10 variables; MPC / PID — process control, explicit dynamic model, regulatory-friendly; RCM + CBM — reliability engineering; physics-based simulation (CFD/FEA/kinetics) — extrapolation, audit; rules-based vision — controlled environments (60-70% inspection workloads достаточно).
- 4.3 (3 мин) — **Hybrid patterns.** PINN (physics-informed NN); CIRL (PID в RL архитектуре, BASF); ML over SPC (ML reduces FP rate, SPC limits OOD); PLC + edge ML coprocessor (POSCO).
- 4.4 (2 мин) — **5-step framework для инженера** (flow-chart): (1) identify class (discrete / process); (2) map alternatives; (3) apply 10 criteria; (4) pilot с explicit go-criteria + baseline; (5) production с HITL + audit trail.

**Working cases (callbacks к §2 + §3):** BASF Geismar, Yokogawa-JSR, POSCO, BMW GenAI4Q, Tesla 2018, Boeing 737, F-35 ALIS служат иллюстрациями к 10 критериям. Новых cases не вводим.

### Раздел 5 — Замыкание + Q&A (5-7 мин). **Slides:** s36-s39. **Failure-bucket:** ~17%.

- 5.1 (1-2 мин) — Recap двухколонной схемы. Discrete → CV + коботы + copilots, failure = over-automation / distribution shift. Process → soft sensors + MPC/RL + PdM + regulatory, failure = drift / FDA/ATEX. Общее: foundation-модели как augmentation, pilot purgatory universal, 10 критериев + альтернативы. **Failure-callback:** «Завтра вендор обещает -70% downtime — задайте 3 вопроса (baseline / окно / intervention list)».
- 5.2 (2 мин) — Bridge к Лекции 12. **Closing hero** BMW Werk + digital-twin overlay (research/06 C1 s39). «Сегодня — отдельные инструменты; Лекция 12 (AI в автоматизации + digital twins) — сшивка: BMW 30+ plants digital-twin-ready, Holcim world-first cement digital twin. ГОСТ Р 57700.37-2021 даёт regulatory ground. Foreshadow Лекции 13 — supply chain AI».
- 5.3 (2-3 мин) — Q&A. Типичные вопросы: «просят внедрить AI, я не уверен» → 5-step framework; «SPC vs ML» → регуляторная среда + count of variables; «RL vs MPC» → high-level scheduling vs control loop, safe-fallback к MPC mandatory.

---

## Mandates carry-forward (ENFORCED — §3.7c)

- [x] **Hero images.** s01 — Tesla Giga Press (Tier 3 Tesla newsroom → Tier 2 Wikipedia Commons → Tier 4 YouTube → Tier 6 news); backup GE+Foxconn WI split. s39 — BMW Werk + digital-twin overlay (Tier 3 BMW press «Virtual Factory NVIDIA GTC Paris»); backup NVIDIA Omniverse Foxconn / Holcim. 6-tier mandatory; никаких stylized cards ([[no-mock-fallbacks]]); per-image log в `iteration-log.md`.
- [x] **Russification.** Acronyms (ISA-95, SCADA, MES, PLC, OEE, APC, MPC, RL, CV, FDA, ATEX, GMP, SPC, DOE, RCM, CBM, PINN, CIRL, FKDPP, HITL, PdM, AOI) — inline gloss при первом упоминании. Замены: «predictive maintenance» → «прогностическое обслуживание»; «soft sensor» → «мягкий сенсор»; «pilot purgatory» → «застревание на пилотной стадии»; «distribution shift» → «сдвиг распределения»; «foundation model» → «фундаментальная модель». Deep latin-token scan на каждой revision. Canonical таблица 45+ — `tools/presentation-build/README.md` §5.8.
- [x] **Real-image acquisition** — ≥15-18 real images / 35 slides. Per-section sketch: §1 Siemens Hannover / GE timeline / Foxconn WI split; §2 BMW / TSMC / Boeing / Tesla 2018 / Toyota / Hyundai-BD; §3 BASF Geismar / Pfizer mRNA / Yokogawa / POSCO / Holcim / refinery aerial; §4 mermaid + 2 real screenshots. Charts: market / pilot purgatory / ALIS / TSMC. Mermaid: ISA-95 / 5-step framework / soft-sensor / CIRL.
- [x] **Anonymization.** Audience generic «студенты-инженеры 3 курса (универсальная, не отраслевые)»; без МГТУ / ИУ6 / Бауман / кафедра. Career-angle — родовое «профильные технические университеты» без названий (lec-06/07).

---

## Slide density + media

**Total ~35.** §0 s01-s05 / §1 s06-s12 / §2 s13-s22 / §3 s23-s30 / §4 s31-s35 / §5 s36-s39.

**Media coverage ≥50%** (≥18 / 35). Иконки НЕ считаются. Hero real ×2 (s01, s39) mandatory. Real production photos ≥10 (Siemens Hannover, BMW, TSMC, Boeing, Tesla 2018, Toyota, BASF, Pfizer, Yokogawa, POSCO, Holcim, refinery). Real SCADA/HMI ≥3 (Pfizer Vox, Yokogawa, POSCO, Tata Steel). QuickChart ≥4 (market estimates, pilot purgatory, ALIS cost, TSMC yield). Mermaid ≥3 (ISA-95, soft-sensor, CIRL, framework, criteria matrix). **Total ≥22 / 35 ≈ 63%**.

---

## Failure-bucket strict-in distribution (mandatory)

| Раздел | Strict-in content | Min | % |
|---|---|---|---|
| §0 (7) | Tesla retreat hook + 2 failure-маркера в keystone | ~2.5 | ~35% |
| §1 (12) | GE Predix + IBM Watson + Foxconn Wisconsin + pilot-purgatory stats | ~5 | ~42% |
| §2 (17) | Tesla 2018 + Boeing 737 door plug + CV границы | ~8 | ~47% |
| §3 (17) | F-35 ALIS callback + RL drift + FDA/ATEX | ~7 | ~41% |
| §4 (13) | 10 критериев + альтернативы + hybrids + framework — целиком | ~13 | ~100% |
| §5 (5-7) | Failure-callback в recap + Q&A | ~1 | ~17% |
| **Total** | | **~36.5 / 75** | **~49%** ✓ ≥30% |

**Counter-check.** Total ~49%, distributed по 5 разделам (min §5 = 17%); §4 = 36% всех failure-минут, не concentrate.

**Holistic check (3 artifacts):**
- Chapter ~10-12k слов: target ~40-50% failure (~4-5k слов): §1 ~1 200 + §2 ~1 200 + §3 ~1 000 + §4 ~2 500.
- Slides ~35: ≥10 strict-in (s01, s09-s11, s15, s18-s19, s22, s26-s27, s28, s30, s31-s35) ~13-15 = 37-43%.
- Speech ~5k слов / 75 мин: ≥22 мин (natural ~36.5 = 49%).

---

## Cornerstone concepts (7 терминов)

Унифицированы в 3 артефактах; glossary lock после Phase 4: (1) «дискретное / процессное производство» — inline gloss; (2) «прогностическое обслуживание» (PdM) — НЕ «predictive maintenance»; (3) «компьютерное зрение для контроля качества» (CV-инспекция); (4) «мягкие сенсоры» (soft sensors); (5) «обучение с подкреплением» (RL); (6) «многоуровневая модель ISA-95 / иерархия Purdue»; (7) «застревание на пилотной стадии» (pilot purgatory) — culturally-loaded McKinsey термин.

Secondary: SCADA, PLC, индустриальная фундаментальная модель, склонность доверять автомату (automation bias), эталонная разметка (ground truth), сдвиг распределения (distribution shift).

---

## Anti-patterns (lec-4/8/9 lessons)

1. ❌ Discrete = только CV-QC (counter: §2.1=4 мин; §2.2-2.4 ≥10 мин не-CV).
2. ❌ Process = только RL (RL ≤4 мин из 17).
3. ❌ «Магическая пилюля + общий дисклеймер» — каждый кейс failure-mode **рядом**.
4. ❌ Англицизмы в visible body. Deep latin-token scan mandatory.
5. ❌ Hero без real image. 6-tier acquisition; stylized card = mock = FAIL.
6. ❌ Failure concentrate только в §4 (counter: §0 35% / §1 42% / §2 47% / §3 41% / §4 100% / §5 17%).
7. ❌ Vendor self-claim как proof (Foxconn «80%» — LO2 pedagogical hook).
8. ❌ Specific numbers без `[VFY-day-of]`.
9. ❌ Lec-09 OODA structural copy — keystone НЕ имеет horizontal Sense→Decide→Act chain.
10. ❌ Designer extras («Лектору», тайминг, «Вы здесь», `[VERIFY-DAY-OF]`, LO codes в visible body). Scaffold — frontmatter / speaker_notes only.

---

## Risk register

| # | Risk | P×I | Mitigation |
|---|---|---|---|
| R1 | Tesla hero не licensable (Tesla aggressive с brand). | M×H | Hook B backup (GE+Foxconn WI split). Tier 2 Wikipedia Commons CC-BY-SA — legal-safe. Phase 5 6-tier attempt; fail → B без редизайна. |
| R2 | Российский контекст тонкий — feedback «нет российских кейсов». | M×M | §3.5 (3 мин) Норникель/СИБУР/ММК-НЛМК-Северсталь; pedagogical reframe — public-disclosure скудна = анти-pattern в reporting, не absence adoption. |
| R3 | §4 (13 мин) overload — 10 + 6 + 4 + 5 items. | M-H×H | 5-step как visual anchor s34; 10 критериев = slide-of-the-day s31, читать вслух медленно; альтернативы = matrix; hybrid = 3 examples. Детали в chapter. |
| R4 | Methodology-critic: keystone Variant C ≈ lec-09 OODA? | L-M×H | Plan явно разница: OODA = decision-loop через 3 stage внутри mission; discrete/process = taxonomy types производства с разной физикой. Different mental object. |
| R5 | Volatile numbers устаревают между Phase 1 и lecture day. | M×M | `[VFY-day-of]` markers; orchestrator 1-page refresh за 1-2 дня; список research/07 §5 (9 items). |

---

## Self-check (перед commit)

- [x] Anti-anglicism в plan sam (acronyms с inline gloss, narrative RU). [x] Anonymization — 0 named institutions. [x] Failure-bucket ~49% strict-in, distributed по 5 разделам (min §5 17%). [x] Keystone в §0 ДО первого погружения; заголовок про **ось**. [x] Hook A + B backup. [x] Cornerstones (7 + secondary).

**Конец Plan v1.** Next: Phase 1 critique (methodology-critic + reader-text-only) → Plan v2 → USER GATE A → Phase 2 chapter.
