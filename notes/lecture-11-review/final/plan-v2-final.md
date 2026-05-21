# Лекция 11: AI в дискретном и процессном производстве — v2 plan (final)

## Метаданные

- Lecture 11 | Module 2 | 75 мин + Q&A (~5 мин буфер)
- LO: LO1a, LO1b, LO2, LO7, LO8 (split LO1; manifest mapping LO1+LO2+LO7+LO8)
- Audience: студенты-инженеры 3 курса (универсальная, generic — без named institutions)
- Issue: #127 | Status: **v2 (Phase 1 critique closed, ready for USER GATE A + Phase 2 chapter draft)** | Date: 2026-05-21
- Keystone axis: **«Дискретное vs Процессное — две модели производства»** (research/05 Вариант C; injection decision-framework в §4 из Варианта D)
- Hook A primary: Tesla Giga Press **BEFORE/AFTER 2018–2024 side-by-side**; Hook B backup: GE Predix + Foxconn Wisconsin split-screen

---

## Changes from v1 (Phase 1 critique closure)

Шесть P1 + пять P2 правок по результатам methodology-critic (REVISE) + reader-text-only critique. Keystone Variant C и LO mapping не менялись.

- **P1-1 closed.** §4 (13 мин) переупакован: 10 критериев → **4 категории** (данные / асимметрия стоимости / регуляторика / человек) ≈ 6 мин; 6 альтернатив → **1 визуальная матрица** 2 мин; 5-step framework + **1 worked example** (Pfizer Vox ретроспективно через рамку) 3 мин; гибриды → 1 строка в §4.4 closure 1 мин. Итого §4 = 12 мин с payoff, без рециклинга 25 элементов.
- **P1-2 closed.** §1 (12 мин) переразвешен 4+4+4: §1.1 мотивация (внедрение + застревание на пилотной стадии) 4 мин; §1.2 фундаментальные модели **с явным объяснением «почему дополнение, а не контроллер»** — задержка, галлюцинации, сертификация 4 мин; §1.3 трио провалов (GE / IBM / Foxconn WI) 4 мин.
- **P1-3 closed.** Доля «провалы/ограничения/альтернативы» (strict-in) recount **честный — ≈44–45%** (не 49%). Per-section recount таблица ниже. §5 поднят с 17% до 25% за счёт явного failure-callback в §5.1 recap.
- **P1-4 closed.** Hook A — **Tesla Giga Press 2018 + 2024 retreat side-by-side**, цитата Маска становится подписью под изображением (не самостоятельный анкер). Tier 2 Wikipedia Commons + Tier 3 Tesla press. Reader-замечание «2024 первым, 2018 как "и в первый раз тоже"» учтено в narrative.
- **P1-5 closed.** Добавлены 5 fundamentals с явными insert-points: **OEE** (§1.1 + §2.2 + §3.4), **эталонная разметка** (§2.1 + §4.1), **OT/IT раскол** (§1.1 + §4.2), **детерминизм edge-вывода** (§3.3), **стоимость разметки vs объём данных** (§2.1 + §4.1).
- **P1-6 closed.** Российский регуляторный scaffold: 1 строка «Указ 250 (КИИ) + ФЗ-152 о персональных данных на КИИ» добавлена в §3.4 нормативный обзор **до** §3.5 РФ deep-dive. ГОСТ Р 57700.37-2021 остаётся foreshadow к Лекции 12.

- **P2-1 closed.** Глоссарий §0.4 сжат до **6 must-know** (ISA-95, MES, SCADA, PLC, OEE, soft sensor) × 2 колонки; остальные acronyms inline при первом упоминании в chapter/speech.
- **P2-2 closed.** Anti-anglicism sweep по plan-v2 narrative — RU-canonical в первом упоминании каждого термина (англ. в скобках для трассировки): «застревание на пилотной стадии (pilot purgatory)», «сдвиг распределения (distribution shift)», «фундаментальная модель (foundation model)», «прогностическое обслуживание (PdM)», «мягкий сенсор (soft sensor)».
- **P2-3 closed.** Lecture-map (s02) и глоссарий (s03) — раздельные слоты, не один.
- **P2-4 closed.** Hook B backup переформулирован без named politician: «глава государства назвал проект "восьмым чудом света" в 2018» → «затем Microsoft Fairwater на тех же руинах».
- **P2-5 closed.** s39 fallback chain: BMW Werk + цифровой двойник Tier-3 → Foxconn-NVIDIA Omniverse Tier-3 backup → Holcim digital-twin Tier-4 ultra-fallback.

---

## Topics Covered

Дискретное производство (компьютерное зрение для контроля качества, прогностическое обслуживание, коботы, индустриальные фундаментальные модели, generative process planning) + процессное (мягкие сенсоры, гибрид MPC/RL, прогностическое обслуживание на границе, регуляторные блокеры FDA Part 11 / ATEX) + таксономия провалов (hype-collapse, чрезмерная автоматизация, сдвиг распределения, застревание на пилотной стадии) + рамка решения «когда AI не нужен» с альтернативными инструментами + российский контекст (КАМАЗ, Норникель, СИБУР).

## Prerequisites

Лекция 3 (архитектуры AI-систем — edge AI на PLC, фундаментальные модели; **критично** для понимания «augmentation vs autonomous controller» в §1.2); Лекция 6 (generative CAD/CAM — граница «AI до производства» vs «в производстве»); Лекция 7 (HITL, FDA, GxP — symmetric для §3.4); Лекция 9 (mission-critical AI, OODA, F-35 ALIS — one-line callback в §3.3, **не самостоятельный кейс**).

**Активный словарь:** сдвиг распределения, FP/FN, точность/полнота, edge vs cloud, HITL, GxP, регрессионная baseline-проверка, OEE.

## Normative References

- **ISA-95 / Purdue Model** — 5-уровневая иерархия (L0 процесс ↔ L4 ERP); опорная сетка в §3, **не** keystone.
- **IEC 62443** — кибербезопасность промышленных систем (edge AI рядом с PLC не расширяет attack surface).
- **FDA 21 CFR Part 11** — электронные записи / audit trail (фарма); запрет autonomous batch release.
- **GAMP®5 + ICH Q8–Q11** — фарма-валидация AI как software.
- **ATEX / IECEx** — взрывоопасные зоны; в Zone 0 non-certified AI-hardware запрещён.
- **ISO 9001 + Six Sigma + DOE** — альтернативный QA-инструмент; DOE даёт защищаемую traceability.
- **Указ Президента РФ № 250 (2022)** — требования по защите критической информационной инфраструктуры (КИИ); регулирует deploy AI на промышленных объектах в РФ.
- **ФЗ-152 «О персональных данных»** на КИИ-объектах — релевантно для систем с биометрией / HMI-логированием операторов.
- **ГОСТ Р 57700.37-2021** — цифровые двойники (РФ); foreshadow к Лекции 12 (не разбираем в §3).
- **Доктринальный фон:** Bainbridge «Ironies of Automation» (1983) — automation paradox; цитируется в §2.4.

## Learning Objectives

1. **LO1a (Remember).** Назвать два типа производства (дискретное / процессное) и для каждого 3–4 dominating 2026-инструмента AI с направлением внедрения.
2. **LO1b (Apply).** Для конкретного кейса определить колонну (дискретное / процессное), AI-стек, и структурный риск на стыке.
3. **LO2 (Evaluate).** Критически оценить vendor-claim «AI –70% downtime / +60% эффективности» — отличить демо от production-baseline, запросить **3 уточняющих вопроса** (baseline, окно измерения, перечень вмешательств). Canonical: Tesla 2018 Musk admit. Backup: Foxconn FoxBrain «80% configuration work» (self-claim).
4. **LO7 (Evaluate).** Описать regulatory landscape (FDA Part 11 в фарма, ATEX в химии, ISO 9001 / Six Sigma в дискретном, Указ 250 в РФ), различить «decision support» vs «autonomous controller» как **два разных архитектурных выбора AI** (чат-помощник для оператора vs замыкание петли управления), обозначить позицию инженера. *Explicit mapping per Phase 1 critique LO matrix.*
5. **LO8 (Apply+Create, центральный, failure-bucket).** Сформулировать **≥4 категории критериев** «AI не нужен / не работает» (данные / асимметрия стоимости / регуляторика / человек), применить к учебному кейсу (Pfizer Vox ретроспективно или hypothetical packaging-line), предложить non-AI альтернативу (SPC, DOE, MPC, RCM, physics-sim, rules-vision). §4 — payoff.

---

## Несущая ось (keystone) — ENFORCED

**Ось.** «Дискретное vs Процессное — две модели производства». Производство — две параллельные ветви с **разной физикой, организационной культурой, регуляторной картой**; AI применяется по-разному; провалы случаются по-разному. Выпускник-инженер обязан уметь сказать, в какой колонне он работает и какой AI-стек применим.

**Keystone slide (§0, после cover + lecture-map + glossary, до первого погружения).** Заголовок: «**Две модели производства. AI входит в обе — но по-разному**». Двухколонная схема:
- **Левая колонна — Дискретное** (иконка авто, «дискретные единицы → CV, коботы, generative process planning»; failure-метка «Tesla 2018»).
- **Правая колонна — Процессное** (иконка ректификационной колонны, «непрерывный поток → мягкие сенсоры, MPC/RL, PdM»; failure-метка «F-35 ALIS $44 000/час»).
- **Соединительный пояс — ОДИН концепт (упрощено по reader-feedback):** «**Застревание на пилотной стадии универсально: 78% компаний используют AI, только 5,5% high performers** (McKinsey State of AI 2025; MIT Sloan 2025 — 95% пилотов не доходят до production)». Фундаментальные модели и agentic-копилоты — это **содержание §1**, не пояс.

**Counter-check.** Заголовок и 1-я строка — про **саму ось**, не про устройство курса / защиту подхода / recap. Пояс декларирует ОДНУ функцию (universal failure-anchor) — не cram-three-things. Если методолог скажет «keystone про другое» — STOP, структурный gap (lec-04 cost ~5 циклов).

**Hot zones провалов.** «Модель ↔ реальность» — сдвиг распределения при смене продукта (§2 CV) / сырья (§3 RL) / pilot→production (§1). «Discrete ↔ process» — AB InBev (непрерывное пивоварение + дискретная упаковка требуют двух стеков). «AI ↔ оператор» — automation paradox (Bainbridge 1983), Toyota Jidoka stance, HITL по FDA/ATEX.

**Connection к LO8.** LO8 — центральный. Keystone делает критерии «AI не нужен» видимыми сразу: failure-метки под обеими колоннами + застревание на пилотной стадии в поясе. §4 — payoff.

**Что НЕ делать:** сводить дискретное только к CV-QC / процессное только к RL; концентрировать провалы в §4; «магическая пилюля + дисклеймер»; keystone про «AI-революцию».

---

## Hook (5–7 мин)

**A primary — Tesla Giga Press BEFORE/AFTER 2018–2024 + Musk-as-caption.**

Hero: **визуальная пара side-by-side** — слева Giga Press underbody photo 2020-launch (Tier 2 Wikipedia Commons / Tier 3 Tesla press kit), справа caption-карточка «**May 2024: Tesla отступила от next-gen gigacasting**» с inline timeline (2018 → 2020 → 2024).

Narrative (по reader-recommendation: **«2024 первым, 2018 как и в первый раз»**): «В мае 2024 Tesla отступила от next-gen gigacasting для Model 2. **Но это вторая** отмена. Первая — апрель 2018, в кризис Model 3, когда Маск признал: *"Excessive automation… my mistake. Humans are underrated"*. Компании не учатся один раз». Цитата Маска — **подпись под изображением**, не отдельный текстовый якорь.

Central question: если Tesla отступила дважды, GE сожгла $4B на Predix, 95% пилотов не доходят до production (MIT Sloan 2025) — **где AI работает, где нет, как инженер должен решать?**

**B backup — GE Predix + Foxconn Wisconsin split-screen** (если Tesla licensing не закрывается на Phase 5). Anti-signal narrative: «глава государства назвал проект "восьмым чудом света" в 2018 → 1 500 рабочих 2024 → Microsoft Fairwater AI datacenter на тех же руинах ($3,3B, май 2024)». Без named politician (P2-4). Решение A vs B — Phase 5 после acquisition attempt.

**Hook НЕ делает:** «AI трансформирует производство» (hype-positive); абстрактный framework без anchored image; empirical test на 2026-моделях.

---

## Структура (5 разделов + Q&A)

### Раздел 0 — Hook + keystone + lecture-map (5–7 мин)

**Цель.** Зацепить Tesla retreat 2018→2024; предъявить ось discrete vs process; задать central question.

**Sub-sections:**
- **0.1 Cover + LO + roadmap** (1 мин)
- **0.2 Hook hero — Tesla Giga Press BEFORE/AFTER side-by-side + Musk-caption + 2024 retreat** (3 мин)
- **0.3 Keystone двух моделей** (1 мин) — заголовок «Две модели производства. AI входит в обе — но по-разному»; пояс = ОДИН концепт (застревание на пилотной стадии).
- **0.4 Lecture-map slide (s02) — раздельно от глоссария** (30 сек)
- **0.5 Glossary mini (s03)** — 6 must-know × 2 колонки: ISA-95, MES, SCADA, PLC, OEE, soft sensor; остальные inline (30 сек)

**Slides:** s01–s05. **Failure-bucket strict-in: ~30%** (Tesla retreat hook = 2 мин strict-in / 7 мин).

**Missing fundamentals introduced:** OEE (в глоссарии), сдвиг распределения (в keystone hot-zones).

**Connection к keystone:** Раздел 0 **есть** keystone — declared explicit.

---

### Раздел 1 — Что общее для обеих моделей (12 мин)

**Цель.** Adoption landscape 2025–2026 + индустриальные фундаментальные модели + застревание на пилотной стадии как universal + 3 canonical hype-collapses. Общий failure-слой для обеих колонн.

**Slides:** s06–s12. **Failure-bucket strict-in: ~38%** (recount: 4,5 мин из 12).

**Sub-sections (rebalanced 4+4+4 per P1-2):**

- **1.1 Adoption landscape + OEE + OT/IT раскол** (4 мин) — McKinsey State of AI 2025: 78% используют AI, **только 5,5% high performers** (EBIT >5%). 2/3 в pilot purgatory. Рыночные оценки расходятся: Markets and Markets $34,18B→$155,04B (CAGR 35,3%); Fortune $7,6B; Precedence $8,57B. **Pedagogical point:** vendor estimates расходятся в 5×; читайте methodology. `[VFY-day-of]`.
  - **NEW: OEE (Overall Equipment Effectiveness)** — central метрика производства = доступность × производительность × качество. Любой vendor-claim «–25% downtime» бессмыслен без OEE-framing. **3-й уточняющий вопрос к вендору: в какой компонент OEE добавляется эффект?** (P1-5 fundamental).
  - **NEW: OT/IT раскол** (30 сек) — фундаментальный structural divide: **OT (Operational Technology)** = PLC, SCADA, детерминированные циклы; **IT (Information Technology)** = облако, AI, eventually-consistent. AI приходит из IT в OT и упирается в этот раскол (P1-5 fundamental). Готовит §3.4 регуляторные блокеры.

- **1.2 Индустриальные фундаментальные модели — augmentation, не controller** (4 мин) — Siemens Industrial Foundation Model (Hannover Messe 2025, 150 PB engineering data + 1 000+ AI-патентов); Foxconn FoxBrain (Llama 3.1 70B derivative, injection-molding параметры).
  - **Критичная граница (explicit per P1-2 + reader-confusion #1):** фундаментальные модели в industry — **augmentation tool для инженера**, **не autonomous controller**. **Три причины:** (a) **задержка вывода** — LLM требует 100–500 мс на запрос, PLC-цикл = 1–10 мс; (b) **галлюцинации** — недетерминированный output несовместим с замыканием control loop; (c) **сертификация** — нет audit trail для SIL 2/3 safety, FDA Part 11, GAMP®5. Помогают разбирать чертежи, отвечать на эксплуатационные вопросы, готовить отчёты — **не управляют станком напрямую**. **Explicit LO7 mapping:** augmentation = chat-helper architecture; autonomous controller = другой архитектурный класс (per Phase 1 critique LO matrix).

- **1.3 Трио hype-collapses** (4 мин) — три истории, три урока:
  - **GE Predix (2011–2020):** $4B+, «be everything to everyone», собственное промышленное облако против AWS, развал 2018, продажа частями. Урок: industrial AI ≠ general cloud AI; size of investment ≠ результат.
  - **IBM Watson Health + Manufacturing (2018–2022):** «–47% downtime, –48% defect rate» маркетинг → продан за parts за $1B (2022). Демо-product gap.
  - **Foxconn Wisconsin (2018–2024):** «восьмое чудо света», $10B обещано, $3B subsidy → 10 000 рабочих стали 1 500 → LCD → coffee kiosks → Microsoft AI datacenter на руинах ($3,3B, май 2024). Anti-signal: «чудо» от главы государства предсказывает провал.

---

### Раздел 2 — Дискретное производство deep-dive (17 мин)

**Slides:** s13–s22. **Failure-bucket strict-in: ~42%** (recount: 7 мин из 17; vendor disclaimers = partial, не strict-in).

- **2.1 CV-инспекция + эталонная разметка + стоимость разметки** (4 мин)
  - BMW GenAI4Q (Regensburg, 2025): bespoke catalogue per vehicle; «FACTORY OF THE YEAR 2024». TSMC: wafer defect detection 95% accuracy, +10–15% yield. Boeing 737 (2024+): CV на fuselage + photo-driven part validation (декабрь 2025).
  - **Anti-кейс:** AI inspection **не предотвратил** door-plug blow-out Alaska Airlines 737 MAX 9 (январь 2024); mechanics reinstalled improperly; FAA cap 38/мес; Everett delayed 12 мес; Spirit AeroSystems 50 jets rework. **Урок (read-out-loud formula):** «**CV — последняя линия защиты, не первая**». Без upstream sign-off + audit trail AI не починит.
  - **NEW: Эталонная разметка (ground truth)** — поднята до cornerstone (P1-5). Inline gloss: «эталонная разметка — это размеченные экспертом примеры, которые модель использует как **истину для обучения и валидации**». В CV-QC проблема: 1–2% defect rate → class imbalance, scarce labels → модели не учат rare defects.
  - **NEW: Стоимость разметки vs объём данных** (P1-5) — raw data дёшев, labels требуют domain expert × hours = дорого. Это **lever для LO8**: критерий #1 в §4.1 «есть ли эталонная разметка adequate volume».

- **2.2 Прогностическое обслуживание на дискретном + OEE снова** (3 мин) — Tata Steel: –20% downtime / –15% maintenance cost (заявка). BMW AIQX: realtime sensor+image fusion. **Honest reality check:** vendor обещает –25–40% / –50–70%; McKinsey 2025 — большинство not capturing value; ROI 8–14 мес; только 5,5% high performers. **OEE callback:** «–25% downtime ≠ +25% OEE» — без availability/performance/quality breakdown vendor-claim не valid.

- **2.3 Коботы + worker-augmentation** (3 мин) — Hyundai + Boston Dynamics: Spot для exterior QC; Atlas humanoid first commercial deployment в HMGMA. Foxconn FoxBrain: «~80% configuration work» — vendor self-claim (LO2 hook: апply 3 уточняющих вопроса). Toyota GAIA: 8 000 (2023) → 10 000 (2024) AI models by employees; 10 000 hours saved. **Jidoka 2.0:** AI = augmentation, не replacement.

- **2.4 Tesla 2018 — canonical over-automation (лекция в лекции — preserved per reader-feedback)** (4 мин) — Q1 2018: target 2 500 Model 3/week → 2 020. Apr 13: Musk «excessive automation… my mistake. **Humans are underrated**». Failed elements: conveyor system Model 3 («we got rid of that whole thing»); robotic «fluffer» для fiberglass mats; over-automated battery module.
  - **Корневая причина (IMD case):** заменял людей там, где variability — feature, не bug.
  - **Структурный урок:** automation paradox (Bainbridge 1983) — чем больше автоматизация, тем критичнее остающиеся operators.
  - **Альтернатива:** Toyota Production System + Jidoka.
  - **Follow-up:** GigaCast retreat 2024 — Tesla опять push, опять retreat. Компании не учатся «один раз».

- **2.5 Границы CV-QC** (3 мин) — Low-contrast defects (CV brittle); сдвиг распределения при смене продукта (часто 5+ моделей per plant); scarce defect labels → callback к §2.1 «стоимость разметки vs объём данных».
  - **Альтернативы:** physical signal amplification (структурированный/поляризованный свет, X-ray, тепловидение) **до** ML; rules-based vision для controlled environments — 60–70% inspection workloads достаточно.

**Connection к keystone:** Раздел 2 = левая колонна keystone. Failure-bucket: Tesla 2018 + Boeing 737 + CV-границы.

---

### Раздел 3 — Процессное производство deep-dive (17 мин)

**Slides:** s23–s30. **Failure-bucket strict-in: ~38%** (recount: 6,5 мин из 17; РФ pedagogical point = partial).

- **3.1 Мягкие сенсоры + AI-formulation** (4 мин) — BASF Geismar (2023–2024): мягкие сенсоры дают real-time оценку quality parameters без physical lab samples; **–30% batch defects** без increased testing. R&D formulation 18 мес → 3 недели. **Pfizer Vox (2024–2025):** GenAI на AWS Bedrock + SageMaker; identify «golden batch» parameters, detect anomalies, **recommend actions to operators**. **+20 000 vaccine doses per batch** (mRNA). «Recommend», не autonomous — consistent с FDA Part 11. **Pfizer Vox станет worked example в §4 (forward link).**

- **3.2 MPC / RL гибрид — с diagram (per reader-confusion #2)** (4 мин) — Yokogawa + JSR FKDPP (2022): first production-precedent RL в chemical plant — 35 дней (840 ч) автономного контроля distillation column. Разрешает компромисс output quality / energy / throughput в нелинейной системе — то, что PID/APC не могли. Japan PM Prize 2023.
  - **CIRL (2024–2026):** **PID внутри loss function deep RL** (BASF + Royal Academy of Engineering) — RL учит политику с PID-баседстейтом как baseline. **Не «RL вместо PID» и не два контура параллельно** — RL расширяет PID, не замещает. Mermaid-диаграмма обязательна (reader-confusion #2).
  - **RL distribution drift:** batch transitions (OOD → unsafe); смена feedstock (stale policy); seasonal shifts; equipment wear.
  - **Альтернатива:** MPC — explicit model, объясним, validated; dominates process control. RL дополняет на high-level scheduling.

- **3.3 PdM + edge AI + детерминизм edge-вывода** (3 мин) — POSCO 180 edge nodes (2024): failure detection independently of corporate network; +5% эффективности, –10% энергии, +3% yield. Holcim 100 plants (2024–2026): kiln optimization + PdM (C3 AI). CEMEX + Optimitive: 10% energy savings, ROI 18 мес; –2–5% CO2 per tonne clinker.
  - **NEW: Детерминизм edge-вывода (P1-5)** — edge ≠ cloud не только по location, а по latency-determinism. PLC-цикл = 1–10 мс детерминированный budget; LLM = 100–500 мс недетерминированный. **«Latency = determinism, не только speed»** — read-out-loud formula. Это связывает §3.3 с §4.2 (PLC + edge ML coprocessor как hybrid pattern).
  - **F-35 ALIS callback (lec-09) — сокращён до 1 строки per reader-feedback #5:** «помните ALIS из лекции 9 — $44 000/час, заменён ODIN; defense PdM учит тому же, что промышленный».
  - **Уроки PdM:** работает где (a) feedback loop fast, (b) эталонная разметка available, (c) FP ≤ FN cost. Long MTBF + safety-critical → preventive + CBM.

- **3.4 Regulatory blockers + Указ 250 + OEE-завершение** (3 мин)
  - **FDA 21 CFR Part 11 (фарма):** электронные записи → audit trail + validated systems + traceable changes. Black-box ML — нет audit trail. **AI не может быть final decision-maker; HITL обязателен**. GAMP®5 validation. Работает: batch quality prediction → operator approval. Не работает: autonomous AI batch release.
  - **ATEX:** AI помогает в predictive monitoring gas/temp/dust — не заменяет ATEX-certified hardware. В Zone 0 non-certified AI hardware запрещён физически.
  - **NEW: Указ Президента РФ № 250 (P1-6)** — требования по защите КИИ; **deploy AI в РФ-промышленности проходит через КИИ-обвязку**: FZ-152 на КИИ-объектах, импортозамещение software к 2027. Готовит §3.5.
  - **OEE-завершение:** регулятор требует **traceability**, что мапится на OEE-breakdown — какой компонент изменился.
  - **Урок:** регуляторика уже есть; AI должен fit existing frameworks; audit trail обязателен.

- **3.5 Российский контекст** (3 мин, public-verifiable only)
  - **Норникель:** AI на flotation/grinding достиг industrial-operation stage; ноябрь 2024 — agreement с Газпром нефть.
  - **СИБУР Marketplace технологического моделирования** (Q1 2025 → 2026 full); контекст импортозамещения (100% КИИ-software → domestic к 2027).
  - **ММК / НЛМК / Северсталь:** общие декларации без specific metrics; параллельный кризис отрасли (Severstal profit –55% в 2024).
  - **Pedagogical point:** public-disclosure скудна → анти-pattern в reporting, не proof отсутствия adoption. Различать PR statement и измеримый эффект — LO2.

**Connection к keystone:** Раздел 3 = правая колонна keystone. Failure-bucket: RL drift + FDA/ATEX + ALIS callback.

---

### Раздел 4 — Карта решения «когда AI не нужен» + альтернативы (12 мин — trimmed per P1-1)

**Цель.** PEAK failure-bucket section + payoff для LO8. Синтез: **4 категории критериев** + альтернативные инструменты (matrix) + worked example + 5-step framework. Студент должен унести applicable mental model.

**Slides:** s31–s35. **Failure-bucket strict-in: ~92%** (recount: 11 из 12 мин; worked example добавлен).

**Sub-sections (re-packed per P1-1):**

- **4.1 Четыре категории критериев «AI не подходит / не работает»** (6 мин — slide s31–s32, 1,5 мин на категорию)

  **A. Данные** — критерии о доступности обучающих данных:
  1. MTBF >1 года — недостаточно failure events для PdM
  2. Известная физика (CFD/FEA/kinetics надёжнее)
  3. Эталонная разметка дорогая (defect rate <1%, expensive labels)
  → **Альтернативы:** physics-based simulation, DOE, SPC

  **B. Асимметрия стоимости** — критерии о цене ошибки:
  4. FP cost >10× FN — SPC + RCM лучше (false alarm дороже missed defect)
  5. SIL 2/3 safety-critical — ML certification сложнее
  → **Альтернативы:** SPC, RCM, rules-based

  **C. Регуляторика** — критерии о normative frameworks:
  6. Audit-trail обязателен (FDA Part 11, GAMP®5) — black-box не работает, нужен explainable / hybrid
  7. ATEX Zone 0 — physical hardware restriction; non-certified AI запрещён
  8. Указ 250 / КИИ — импортозамещение software, ограничения cloud
  → **Альтернативы:** explainable ML, hybrid с rules, on-premise

  **D. Человек** — критерии о людях и процессах:
  9. Operator distrust — workaround неизбежен (Toyota proof, lec-7 HITL)
  10. Pilot без go-criteria — 80–95% pilot purgatory; define baseline + go/no-go ДО pilot
  11. Demo-hype без 6-mo production track record — buyer beware
  → **Альтернативы:** Six Sigma, Jidoka, structured pilots

  **3 уточняющих вопроса к вендору (artifact для кармана, LO2):** (1) baseline до AI; (2) измерительное окно; (3) перечень вмешательств. **Plus 3-й OEE-вопрос:** в какой компонент OEE добавляется эффект (availability / performance / quality)?

- **4.2 Альтернативные инструменты — visual matrix slide** (2 мин — s33)
  - Одна матрица 6×5: SPC + Six Sigma / DOE / MPC / RCM + CBM / physics-based simulation / rules-based vision **× колонки** «когда применим / сильные стороны / слабые / typical accuracy / regulatory friendly».
  - Hybrid patterns в **1 строке закрытия** (P1-1): PINN (physics-informed NN) + CIRL (PID-в-RL, BASF) + ML over SPC + PLC + edge ML coprocessor (POSCO) — 4 примера hybrids, без deep-dive.

- **4.3 Worked example — Pfizer Vox через 5-step framework retrospective (NEW per P1-1)** (3 мин — s34)
  - **Кейс:** «Pfizer хотел детектировать аномалии в mRNA vaccine batches и рекомендовать действия оператору. Применим рамку».
  - **Step 1 — identify class:** процессное (continuous bioprocessing).
  - **Step 2 — map alternatives:** SPC (univariate, baseline), DOE (не подходит — too many variables), MPC (есть, но не покрывает rare anomalies).
  - **Step 3 — apply 4 categories:** Данные ✓ (вакцины — много batch data, эталонная разметка есть из QC); Стоимость ✓ (FP cost manageable — operator review); Регуляторика ✓✗ (FDA Part 11 — **recommend mode, не autonomous batch release**); Человек ✓ (operators обучены).
  - **Step 4 — pilot с go-criteria:** Pfizer заявил +20 000 doses per batch — baseline до AI был известен.
  - **Step 5 — production с HITL:** «Vox recommends actions to operators» — explicit augmentation, не autonomous. Архитектура AI = decision-support, не controller (LO7 mapping).
  - **Lesson:** 5-step framework работает ретроспективно — это **готовый инструмент**, не abstract theory.

- **4.4 5-step framework slide closure** (1 мин — s35)
  - Flow-chart: (1) identify class (discrete/process) → (2) map alternatives → (3) apply 4 категории критериев → (4) pilot с explicit go-criteria + baseline → (5) production с HITL + audit trail.
  - **Hybrids closure (1 строка per P1-1):** «4 hybrid patterns (PINN / CIRL / ML over SPC / PLC+edge ML) — детали в §4.2 + chapter §4.3».

**Working cases (callbacks к §2 + §3):** BASF Geismar, Yokogawa-JSR, POSCO, BMW GenAI4Q, Tesla 2018, Boeing 737, F-35 ALIS, Pfizer Vox — служат иллюстрациями к 4 категориям. Новых cases не вводим.

---

### Раздел 5 — Замыкание + Q&A (6–7 мин)

**Slides:** s36–s39. **Failure-bucket strict-in: ~25%** (поднят с 17% за счёт explicit failure-callback per P1-3).

- **5.1 Recap двухколонной схемы + явный failure-callback** (2 мин)
  - Discrete → CV + коботы + копилоты, failure = чрезмерная автоматизация / сдвиг распределения.
  - Process → мягкие сенсоры + MPC/RL + PdM + регуляторика, failure = drift / FDA/ATEX.
  - Общее: фундаментальные модели как дополнение, застревание на пилотной стадии universal, 4 категории критериев + альтернативы.
  - **Explicit failure-callback (NEW per P1-3):** «**Завтра вендор обещает –70% downtime — задайте 3 вопроса (baseline / окно / перечень вмешательств) + 4-й OEE-вопрос. Если ответы расплывчатые — это demo, не production. 95% пилотов не доходят до production не потому что AI плох, а потому что инженеры не задают эти вопросы**».

- **5.2 Bridge к Лекции 12** (2 мин)
  - **Closing hero** BMW Werk + цифровой двойник overlay (s39).
  - «Сегодня — отдельные инструменты; Лекция 12 (AI в автоматизации + цифровые двойники) — сшивка: BMW 30+ plants digital-twin-ready, Holcim world-first cement digital twin. ГОСТ Р 57700.37-2021 даёт regulatory ground в РФ. Foreshadow Лекции 13 — supply chain AI».

- **5.3 Q&A** (2–3 мин) — Типичные вопросы: «просят внедрить AI, я не уверен» → 5-step framework; «SPC vs ML» → регуляторная среда + count of variables; «RL vs MPC» → high-level scheduling vs control loop, safe-fallback к MPC mandatory.

**Connection к keystone:** Раздел 5 закрывает обе колонны, не только одну.

---

## Plan-level mandates carry-forward checklist (ENFORCED)

- [x] **Hero images.** s01 — Tesla Giga Press BEFORE/AFTER side-by-side (Tier 2 Wikipedia Commons → Tier 3 Tesla press → Tier 4 YouTube → Tier 6 news); backup GE+Foxconn WI split. s39 — BMW Werk + цифровой двойник overlay (Tier 3 BMW press «Virtual Factory NVIDIA GTC Paris»); backup chain BMW → Foxconn-NVIDIA Omniverse Tier-3 → Holcim digital-twin Tier-4. 6-tier mandatory; никаких stylized cards ([[no-mock-fallbacks]]); per-image log в `iteration-log.md`.
- [x] **Russification.** Acronyms (ISA-95, SCADA, MES, PLC, OEE, APC, MPC, RL, CV, FDA, ATEX, GMP, SPC, DOE, RCM, CBM, PINN, CIRL, FKDPP, HITL, PdM, AOI) — inline gloss при первом упоминании. Замены применены в этом plan-v2 narrative: «прогностическое обслуживание», «мягкий сенсор», «застревание на пилотной стадии», «сдвиг распределения», «фундаментальная модель», «эталонная разметка», «детерминизм edge-вывода», «склонность доверять автомату». Deep latin-token scan на каждой revision. Canonical таблица 45+ — `tools/presentation-build/README.md` §5.8.
- [x] **Real-image acquisition.** ≥15–18 real images / 35 slides. Per-section sketch: §1 Siemens Hannover / GE timeline / Foxconn WI split; §2 BMW / TSMC / Boeing / Tesla 2018 side-by-side / Toyota / Hyundai-BD; §3 BASF Geismar / Pfizer mRNA / Yokogawa / POSCO / Holcim / refinery aerial; §4 mermaid + 2 real screenshots. Charts: market / pilot purgatory / ALIS / TSMC. Mermaid: ISA-95 / 5-step framework / мягкий-сенсор / CIRL.
- [x] **Anonymization.** Audience generic «студенты-инженеры 3 курса (универсальная, не отраслевые)»; без МГТУ / ИУ6 / Бауман / кафедра. Career-angle (если будет в chapter) — родовое «профильные технические университеты» без названий (lec-06/07 эталон).
- [x] **Failure-bucket strict-in honest tracking.** Recount табица ниже; partial vs strict-in marking явный. Target ≥30% holistic ✓ (44–45% реально).

---

## Slide density + media

**Total ~35.** §0 s01–s05 / §1 s06–s12 / §2 s13–s22 / §3 s23–s30 / §4 s31–s35 / §5 s36–s39.

**Media coverage ≥50%** (≥18 / 35). Иконки НЕ считаются. Hero real ×2 (s01 BEFORE/AFTER pair, s39) mandatory. Real production photos ≥10 (Siemens Hannover, BMW, TSMC, Boeing, Tesla 2018, Toyota, BASF, Pfizer, Yokogawa, POSCO, Holcim, refinery). Real SCADA/HMI ≥3 (Pfizer Vox, Yokogawa, POSCO, Tata Steel). QuickChart ≥4 (market estimates, pilot purgatory, ALIS cost, TSMC yield). Mermaid ≥3 (ISA-95, мягкий-сенсор data flow, CIRL архитектура, 5-step framework, criteria matrix). **Total ≥22 / 35 ≈ 63%**.

---

## Failure-bucket strict-in distribution table — honest recount (P1-3)

| Раздел | Длительность | Strict-in (полный разбор: контекст + урок + альтернатива) | Partial (маркер / 1-line) | Strict-in мин | % strict-in |
|---|---|---|---|---|---|
| §0 (7 мин) | 7 | Tesla retreat hook (полный разбор 2018+2024 + central question) | 2 failure-маркера в keystone | ~2 | ~30% |
| §1 (12 мин) | 12 | §1.1 OT/IT раскол (фундаментальный лоскут) + §1.3 трио hype-collapses (GE / IBM / Foxconn WI с уроком) | §1.1 vendor-расхождение estimates | ~4,5 | ~38% |
| §2 (17 мин) | 17 | §2.1 Boeing 737 + «CV последняя линия» + стоимость разметки; §2.4 Tesla 2018 (full); §2.5 границы CV + альтернативы | §2.2 PdM vendor reality check; §2.3 Foxconn 80% self-claim (LO2 hook, partial) | ~7 | ~42% |
| §3 (17 мин) | 17 | §3.2 RL drift + альтернативы; §3.3 ALIS callback (1 строка); §3.4 регуляторика FDA/ATEX + Указ 250 + почему AI не controller | §3.5 РФ pedagogical point | ~6,5 | ~38% |
| §4 (12 мин) | 12 | §4.1 4 категории критериев + 3 вопроса + OEE-вопрос; §4.2 matrix альтернатив; §4.3 Pfizer Vox worked example; §4.4 5-step framework | hybrids в 1 строке (partial) | ~11 | ~92% |
| §5 (6–7 мин) | 6,5 | §5.1 explicit failure-callback recap (NEW per P1-3) | bridge к лекции 12 | ~1,6 | ~25% |
| **Total** | **75** | | | **~32,6 / 75** | **~43,5%** ✓ ≥30% (margin ~13,5 п.п.) |

**Counter-check.** Min раздел = §0 ~30% (нижний предел ≥20% ✓). Max = §4 ~92%. Distributed по 5 разделам — нет single-artifact concentration. §4 = 11 мин = 34% всех failure-минут (не concentrate, healthy distribution).

**Holistic check (3 artifacts) — projection:**
- **Chapter ~10–12k слов:** target ~40–45% failure-bucket (~4–5k слов): §1 ~1 100 + §2 ~1 200 + §3 ~1 000 + §4 ~2 500 + §5 callback ~200. Phase 3 methodology-critic re-runs deep scan.
- **Slides ~35:** ≥13 strict-in (s01 hook, s09–s11 трио, s15 Boeing, s17–s18 Tesla 2018, s22 границы CV, s26–s27 RL drift, s28 регуляторика, s31–s35 §4 целиком, s36 recap callback) = 13–15 / 35 = 37–43%.
- **Speech ~5k слов / 75 мин:** ~32–33 мин strict-in = ~43%.

---

## Cornerstone concepts (8 терминов, expanded per P1-5)

Унифицированы в 3 артефактах; glossary lock после Phase 4:

1. «дискретное / процессное производство» — inline gloss
2. «прогностическое обслуживание» (PdM) — НЕ «predictive maintenance»
3. «компьютерное зрение для контроля качества» (CV-инспекция)
4. «мягкий сенсор» (soft sensor)
5. «обучение с подкреплением» (RL)
6. «многоуровневая модель ISA-95 / иерархия Purdue»
7. «застревание на пилотной стадии» (pilot purgatory) — culturally-loaded McKinsey термин
8. **NEW — «эталонная разметка» (ground truth)** — central для §2.1 + §3.3 + §4.1 critierion «данные»

**Secondary (expanded per P1-5):** SCADA, PLC, индустриальная фундаментальная модель, склонность доверять автомату (automation bias), сдвиг распределения (distribution shift), **OEE (Overall Equipment Effectiveness)** — central метрика производства, **OT/IT раскол** — structural divide индустриальной AI, **детерминизм edge-вывода** (latency-determinism), **стоимость разметки vs объём данных** (label cost vs data volume).

---

## Anti-patterns (refined from lec-4/8/9 lessons)

1. ❌ Discrete = только CV-QC (counter: §2.1=4 мин; §2.2–2.4 ≥10 мин не-CV).
2. ❌ Process = только RL (RL ≤4 мин из 17).
3. ❌ «Магическая пилюля + общий дисклеймер» — каждый кейс failure-mode **рядом**, в strict-in count partial credit, не full.
4. ❌ Англицизмы в visible body. Deep latin-token scan mandatory.
5. ❌ Hero без real image. 6-tier acquisition; stylized card = mock = FAIL.
6. ❌ Failure concentrate только в §4 (counter: §0 30% / §1 38% / §2 42% / §3 38% / §4 92% / §5 25%).
7. ❌ Vendor self-claim как proof (Foxconn «80%» — LO2 pedagogical hook).
8. ❌ Specific numbers без `[VFY-day-of]`.
9. ❌ Lec-09 OODA structural copy — keystone НЕ имеет horizontal Sense→Decide→Act chain.
10. ❌ Designer extras («Лектору», тайминг, «Вы здесь», `[VERIFY-DAY-OF]`, LO codes в visible body). Scaffold — frontmatter / speaker_notes only.
11. ❌ **NEW: Keystone belt cram (per reader-confusion #4)** — один концепт в поясе (застревание на пилотной стадии), не три.
12. ❌ **NEW: §4 как recitation list** (per P1-1) — 4 категории + worked example + matrix, не 25 abstract items.
13. ❌ **NEW: Foundation models «augmentation, не controller» без explanation** (per reader-confusion #1) — три причины (задержка / галлюцинации / сертификация) обязательны.
14. ❌ **NEW: CIRL без диаграммы** (per reader-confusion #2) — mermaid mandatory.

---

## Risk register (refined)

| # | Risk | P×I | Mitigation |
|---|---|---|---|
| R1 | Tesla hero не licensable (Tesla aggressive с brand). | M×H | Hook B backup (GE+Foxconn WI split). Tier 2 Wikipedia Commons CC-BY-SA — legal-safe. Phase 5 6-tier attempt; fail → B без редизайна. **NEW: BEFORE/AFTER pair снижает single-image dependency.** |
| R2 | Российский контекст тонкий — feedback «нет российских кейсов». | M×M | §3.5 (3 мин) Норникель/СИБУР/ММК-НЛМК-Северсталь; pedagogical reframe — public-disclosure скудна = анти-pattern в reporting, не absence adoption. **NEW: Указ 250 в §3.4 добавляет regulatory scaffold ДО deep-dive (P1-6).** |
| R3 | §4 (12 мин) overload — снято P1-1, но contingency risk. | L×M | 4 категории как visual anchor s31–s32; matrix альтернатив s33; worked example s34 Pfizer Vox; 5-step framework s35. Hybrids в 1 строке. **Recount: §4 = 12 мин (был 13), 4 категории (было 10 критериев), 1 worked example (было 0). Risk downgraded M-H → L.** |
| R4 | Methodology-critic: keystone Variant C ≈ lec-09 OODA? | L-M×H | Plan явно разница: OODA = decision-loop через 3 stage внутри mission; discrete/process = taxonomy types производства с разной физикой. Different mental object. **Methodology-critic Phase 1 confirmed Variant C валиден.** |
| R5 | Volatile numbers устаревают между Phase 1 и lecture day. | M×M | `[VFY-day-of]` markers; orchestrator 1-page refresh за 1-2 дня; список research/07 §5 (9 items). |
| R6 | **NEW — Worked example Pfizer Vox недостоверен retrospectively.** | L×M | Phase 2 fact-checker re-verifies Pfizer Vox claims (+20 000 doses, FDA Part 11 compliance, AWS Bedrock). Если weak — substitute Tesla 2018 retrospective worked example. |
| R7 | **NEW — Reader confusion CIRL / foundation-model-boundary остаётся в chapter.** | L×M | Phase 2 chapter brief: mermaid CIRL архитектура + explicit «3 причины» в §1.2. Phase 3 reader-text-only re-runs confusion check. |

---

## Phase 2 chapter brief carry-forward (NEW section per task spec)

**Single-paragraph instruction для book-editor Phase 2 chapter draft:**

Глава ~10–12k слов, source-of-truth для slides + speech. **Emphasis на:** (1) keystone discrete/process через всю главу с явным failure-callbacks под каждой колонной; (2) §4 worked example Pfizer Vox через 5-step framework — **развёрнуто ~600–800 слов** как applicable якорь, не теоретический список; (3) **3 причины «foundation model = augmentation, не controller»** (задержка / галлюцинации / сертификация) explicit в §1.2 — без этого reader-confusion #1 переходит в chapter; (4) CIRL архитектура с **mermaid-described**: «PID внутри loss function deep RL» — без двух контуров parallel и не RL вместо PID; (5) failure-bucket strict-in distributed по 5 разделам, target ~42–45% слов; (6) anti-anglicism deep latin-token scan на каждой revision (Russification таблица — `tools/presentation-build/README.md` §5.8). **Cornerstones lock:** 8 main + secondary glossary, no drift. **Carry mandates:** anonymization absolute, 6-tier hero acquisition план для s01 + s39, real-image ≥15–18 / 35 slides. **Что НЕ делать:** keystone про что-то кроме discrete/process; §4 как recitation list; «магическая пилюля» строки в failure-bucket count; named institutions в audience; англицизмы в narrative body.

**Expected chapter section count:** 5 (Введение + §1 общее + §2 дискретное + §3 процессное + §4 рамка решения + §5 замыкание). Каждая section: motivation + content + self-check questions + sources.

---

## Self-check (перед commit)

- [x] **6 P1 fixes closed** (closure block в начале plan).
- [x] **5 P2 fixes closed** (P2-1..P2-5).
- [x] **Anti-anglicism в plan sam** — RU-canonical в первом упоминании (acronyms с inline gloss).
- [x] **Anonymization** — 0 named institutions в audience / career-angle.
- [x] **Failure-bucket honest recount ~43,5%** (не 49%), distributed по 5 разделам (min §0 = 30%, max §4 = 92%).
- [x] **Keystone в §0 ДО первого погружения; заголовок про ось** (Variant C unchanged).
- [x] **Hook A primary BEFORE/AFTER + B backup** без named politician.
- [x] **8 cornerstones + secondary** (+OEE +ground truth +OT/IT +edge latency +label cost vs volume).
- [x] **§4 worked example** Pfizer Vox prescribed.
- [x] **3 причины «foundation = augmentation»** explicit в §1.2.
- [x] **Указ 250** в §3.4 normative scaffold ДО §3.5 РФ deep-dive.
- [x] **CIRL mermaid mandatory** flag в anti-patterns.
- [x] **Phase 2 chapter brief carry-forward** section добавлена.

**Конец Plan v2 final.** Next: USER GATE A → Phase 2 chapter draft (book-editor spawn) с этим plan'ом как input.
