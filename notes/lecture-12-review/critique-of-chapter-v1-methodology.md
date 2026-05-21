---
critique_of: library/lectures/lec-12/chapter*.md (4 files; chapter.md + chapter-part2.md + chapter-part3.md + references.md)
critic: methodology-critic
verdict: REVISE
created: 2026-05-21
lecture: 12
version: v1
issue: 133
---

# Summary

Chapter v1 закрывает **педагогически крепкую и архитектурно зрелую** работу — 8 plan §-секций пройдены, keystone A0→A1→A2→A3 явно предъявлен в §0.1 ДО первого погружения, ISA-95 disambiguation присутствует, Kritzinger 2018 + ГОСТ Р 57700.37-2021 правильно сцеплены, Southeast Asian Port вместо Tesla 2018 как fresh hero, Yokogawa FKDPP в §4.3 переориентирован на **twin-as-sandbox** (anti-overlap с lec-11 §3.2 выполнено), worked example §5.3 фарма+FDA доведён до verdict «AI not applicable + двухслойная альтернатива», 14 Q&A backup на месте, все 13 jargon glosses при первом упоминании, 0 named-institution leaks. Failure-share strict-in ≈40-45% (выше 30% target), distribution holistic (chapter.md ≈39%, part2 ≈49%, part3 ≈46% — все ≥30%).

**Однако** есть **два P0 структурных нарушения, оба попадающих под CLAUDE.md ENFORCED rules**, которые обязывают verdict **REVISE**, не APPROVE-WITH-POLISH:

1. **Word count gap** — 26 908 слов суммарно (excl. frontmatter / headings / nav / source-list / [for-slide-] markers) против обязательного диапазона **28 500–31 500** для **L4–L17 лекции** (CLAUDE.md «Chapter Depth Baseline»). Это **−1 592 слов** (−5,6% от lower bound, −10,3% от target 30k). Plan v2 frontmatter уже зафиксировал `chapter_target_words: 30000`; book-editor сам же написал `length_words: ~28500` в frontmatter chapter.md, но фактический счёт ниже. L4+ owner-waiver **недоступен** per CLAUDE.md решение 2026-05-21 (issue #128).
2. **Deep latin-token scan flags 347 critical anglicism hits в visible body** (top-30 blacklist: production-grade ×23, advisory ×29, edge ×43 в narrative sense, release ×17, shadow ×9, accuracy ×9, workflow ×9, etc.). Book-editor self-report «838 unique tokens, большая часть intentional gloss» **inflated self-report pattern** (Лекция 8 lesson — narrow grep маскирует depth). >5 critical hits в narrative body = P0 «Anti-anglicism mandate violated».

Дополнительно — **6 P1 issues** (см. ниже): internal numbers inconsistency 35-day FKDPP, timing/methodology leak в visible body §4.5 / §5 / §6, designer-extras leak `for-slide-sNN` markers повсюду в visible body, missing-fundamental в §1.2 (Слой 2 «hybrid model» без формулы или конкретного примера PINN), insider phrasing «рабочее правило» в §2.4, ratio plan-v2 hero_s07 не реализован отдельным разделом chapter §1 (Composer time-scrubbing описан, но без UI-screenshot reference в text — небольшой gap).

Counter-check (CLAUDE.md verdict scale): 2 P0 → **REVISE**. Counter-check (5+ P1 → REVISE): 6 P1 → также **REVISE**. Двойное основание для verdict.

---

# Severity counts

- **P0:** 2 (DoD-blocking)
- **P1:** 6 (high-priority)
- **P2:** 7 (polish)

---

# P0 issues (blocking, structural — not polish)

## P0-1. Chapter word count 26 908 < 28 500 lower bound (L4+ baseline violation)

**Severity:** P0 — CLAUDE.md «Chapter Depth Baseline» enforcement.

**Evidence:**
- Independent recount (excluding frontmatter, headings, code blocks, table separators, `[for-slide-sNN]` markers, nav blocks): **chapter.md = 9463 words; chapter-part2.md = 7634 words; chapter-part3.md = 9811 words. Total = 26 908 words.**
- Frontmatter chapter.md line 4: `length_words: ~28500` — sub-agent self-reported lower bound, но даже этот self-report не достигнут на 1 592 слова.
- Plan v2 frontmatter line 21 (`chapter_target_words: 30000`) явно зафиксировал target 30k.
- CLAUDE.md «Chapter Depth Baseline» (новое правило 2026-05-21, issue #128): «L4-L17: ≥30 000 слов mandatory, waiver недоступен. <30k для L4+ → REVISE verdict; <28.5k → P0 BLOCKING». Лекция 12 = L12, попадает в L4-L17 band.

**Cost of omission:** Owner explicit в Лекции 11 review «должен быть как L8/L9, минимум 30k для всех». Лекция 12 = первая полная реализация baseline после rule установлен; недостигнутый minimum = регрессия от Лекции 11 paradigm.

**Recommendation:** добавить ~3 000 слов **строго целевыми расширениями**, а не «воды». Конкретные адреса (по приоритету, ROI на failure-bucket):

1. **§5.2 критерий 1 (safety-critical)** — +200 слов: конкретный case study Bhopal 1984 (chemical disaster) с явной интерпретацией «здесь даже A2 непригоден»; numerical mapping IEC 61508 SIL 2 vs SIL 3 на типы оборудования.
2. **§5.2 критерий 3 (rare-event)** — +250 слов: federated PdM concrete example (200 насосов агрегированно, конкретные numbers); pitfalls гибридного physics+ML augmentation.
3. **§5.3 worked example FDA** — +300 слов: full HPLC <905> Content Uniformity calculation + AV ≤ 15.0 formula пример; cross-ref на Pfizer Vox метрики deployment 2024-2025.
4. **§4.3 twin как sandbox** — +250 слов: domain randomization concrete ranges (heat transfer coeff 0.7–1.2; surface fouling 0–25%); конкретный пример Yokogawa sim-to-real fine-tuning protocol (количество реальных эпизодов до certification).
5. **§3.4 generic LLM PLC** — +300 слов: дополнительные failure modes (timer reset → race conditions; interlock placement в первом/последнем scan-цикле + конкретный пример); сравнительная таблица «ChatGPT vs Claude vs Gemini на PLC» с метриками.
6. **§6.3 edge AI** — +250 слов: concrete latency budget breakdown (sensor read 1ms + transport 2ms + inference 4ms + decision logic 1ms + actuator command 2ms = 10ms total); cybersecurity attack vectors с конкретными CVE.
7. **§7.2 Норникель** — +400 слов: подробная схема flotation control loop с явным mapping A1→A2 transition; CAPEX vs operational savings табличный расчёт.
8. **§2.3 PdM Deloitte** — +200 слов: разворот 57× cement plant ROI с decomposition (avoided unplanned stops × cost per stop = total savings; cost of system); явный mapping на OEE availability компонент.
9. **§4.2 FKDPP алгоритмика** — +200 слов: больше алгоритмических деталей factorial kernel decomposition (без полной математики, но conceptual depth); cross-ref к Лекции 11 §3.2 более precise.
10. **§7.4 careers role 5 (новая) — Industrial AI safety auditor** — +250 слов: новая роль за пределами 4 текущих; описание дня; навыки; growth rate.

Итого ≥2 600 слов targeted depth additions, выводящих ≥30 000.

## P0-2. Deep latin-token scan: 347 critical anglicism hits в visible narrative body

**Severity:** P0 — CLAUDE.md anti-anglicism mandate; `[[russification]]` memory rule; «pattern-narrow grep НЕ достаточен» (Лекция 8 lesson).

**Evidence (top-15 critical hits в narrative body, не source URLs / brand names):**

| Token | Occurrences | Russian alternative |
|---|---|---|
| `edge` (в narrative «edge AI», «edge gateway», «edge device», «edge ROI») | 43 | «на границе сети», «граничные» — partially used, но 43 hits показывают, что Russification incomplete |
| `advisory` | 29 | «советующий», «совещательный режим» |
| `production-grade` | 23 | «промышленного уровня», «production-grade в проверенном смысле» (gloss) |
| `production` | 21 (в narrative sense, not as part of «production-grade») | «промышленная эксплуатация», «выпуск», «эксплуатация» |
| `release` (release decision, release testing) | 17 | «выпуск партии», «решение о выпуске» |
| `case` (use case, edge case) | 14 | «кейс», «случай», «применение» |
| `shadow` (digital shadow, shadow mode) | 9 | «цифровая тень», «теневой режим» |
| `workflow` | 9 | «процесс работы», «последовательность шагов» |
| `accuracy` | 9 | «точность» — already used, но 9 latin hits in body |
| `inference` | 7 | «инференс» (transliteration if jargon needed) или «вывод модели» |
| `governance` | 7 | «управление данными» |
| `closed-loop` | 6 | «замкнутая петля» — already used, но 6 latin hits in body |
| `scrubbing` (time scrubbing) | 6 | «прокрутка времени» — already used as gloss, but pure-latin uses leak |
| `retraining` | 6 | «дообучение» |
| `sim-to-real` (sim-to-real gap) | 5 | «разрыв симуляция-реальность» — already used as gloss, но 5 pure-latin uses |

**Why this matters:** book-editor self-report «production-уровень, capability, hype demo, freelance, out-of-band verification, ... — flagged candidates Phase-4» = осознанное оставление 13+ patterns. Phase-3 critique должна **enforced russify ДО Phase-4** (chapter — book-first source-of-truth; русификация после approval = caskадные правки speech+slides).

**Recommendation:** Phase-3 revision должна сделать **systematic russify pass** с targeted замен. Approach:

1. **Inline gloss strategy**: первое упоминание — «инференс (вывод модели)» / «advisory (советующий режим)» / «release decision (решение о выпуске партии)» — затем русский вариант. **Не** оставлять чисто latin форму на 17-43 occurrences.
2. **Critical replacements (zero retention)**:
   - `production-grade` → «промышленного уровня» (23 → 0)
   - `release` (in body) → «решение о выпуске» / «выпуск партии» (17 → 0)
   - `workflow` → «процесс работы» / «последовательность шагов» (9 → 0)
   - `closed-loop` (latin form) → «замкнутая петля» (6 → 0; gloss оставить «closed-loop control — замкнутая петля» один раз)
3. **Retain-with-gloss (whitelist)**: brand names (Siemens, Yokogawa, NVIDIA, OPC UA, MQTT, TSN — already canonical), `Digital Twin` / `Digital Shadow` / `Digital Model` (Kritzinger taxonomy — proper noun), `safety envelope` (jargon, gloss один раз).

---

# P1 issues (high-priority — must fix before APPROVE)

## P1-1. Internal numbers inconsistency — 35-day FKDPP simulation vs production claim

**Severity:** P1 (factual self-contradiction in core case).

**Evidence:**
- **chapter.md line 125**: «RL обучалось 35 дней в симуляции до того, как его выпустили на реальное оборудование» — claims 35 days was simulation training duration.
- **chapter-part2.md line 222**: «35 дней непрерывной работы под RL-контролем — первый документированный production-grade случай RL в process control» — claims 35 days was production run at JSR (the correct interpretation per Yokogawa press release).
- **chapter-part2.md line 226**: «35 дней без вмешательства оператора» — production run.
- **chapter.md table line 114** (§0.1 keystone): «35 дней 2022» as A2 example — context is JSR production, correct.

Yokogawa press release [27]: 35 days = continuous production-grade RL operation at JSR химзавод 2022. Simulation training duration was thousands of episodes (months of compute, not «35 дней»).

**Recommendation:** chapter.md line 125 fix: «RL обучалось **тысячи эпизодов в симуляции** до того, как его выпустили на реальное оборудование, и потом 35 дней работало непрерывно в production-режиме на JSR (см. §4.2)». Cross-ref forward на §4.2.

## P1-2. Timing/methodology leak в visible body (CLAUDE.md feedback_no_timing_no_methodology_in_slides applies к chapter too)

**Severity:** P1 — CLAUDE.md anti-pattern «timing / methodology in slides» extends к chapter visible body. Owner правит в КАЖДОЙ лекции.

**Evidence (≥4 hits в visible body):**
- `chapter-part2.md:324`: «Этот раздел — **короткий (соответствует 2 минутам устной лекции)**, но концептуально важный» — timing visible.
- `chapter-part3.md:45`: «Это **самый плотный раздел главы по доле failure-bucket** — **пятнадцать минут лекционного времени** посвящены целиком вопросу…» — timing visible.
- `chapter-part3.md:228`: «Этот раздел — операционная карта производственной AI-системы. Он короче других (**соответствует 6 минутам лекции**), но критично важен» — timing visible.
- `chapter.md:232`, `chapter.md:234`, `chapter.md:244`: «**Первый педагогический момент**…», «**Второй педагогический момент**…», «**Третий педагогический момент**…» — methodological scaffolding visible to student.
- `chapter-part3.md:498`: «Шкала A0–A3 — **педагогический инструмент**, а не строгая классификация…» — methodology meta-commentary.

**Why P1:** Chapter — это **textbook-quality референс для self-study**, не lecture-script. Студент, читающий chapter без lectures context, видит «пятнадцать минут устной лекции» — это **break of fourth wall**. Owner explicit в memory rule «НИ timing-маркеров, НИ методических комментариев в visible body».

**Recommendation:** Phase-3 revision — replace timing/methodology meta-commentary с content statements:
- «Этот раздел — короткий, но концептуально важный» (без «соответствует 2 минутам устной лекции»).
- «**Первый аналитический момент** — расходящиеся оценки» / «**Первый показатель критики** — расходящиеся оценки» (без «педагогический момент»).
- «Шкала A0–A3 — **аналитический инструмент**…» (без «педагогический»).

## P1-3. Designer-extras leak `[for-slide-sNN]` markers visible в body (visible на students reading chapter standalone)

**Severity:** P1 — CLAUDE.md «No Extra Content Rule»: «`[VERIFY-DAY-OF]` / LO codes / §X.X / → sNN visible to students в body — frontmatter / speaker_notes only».

**Evidence:** `[for-slide-s01]` / `[for-slide-s02]` / `[for-slide-s03]` ... `[for-slide-s39]` markers разбросаны throughout visible chapter body (~30 instances). Эти markers полезны для **build-deck pipeline** (mapping chapter sections к slides), но **не должны быть visible** при reading chapter standalone.

**Recommendation:** перенести `[for-slide-sNN]` markers в HTML-comments `<!-- for-slide-sNN -->` (Markdown-stripped at render, но preserved для build-deck pipeline grep). Альтернатива — переместить mapping в отдельный artefact `slide-mapping.yaml` (cleaner separation, требует pipeline update).

## P1-4. Missing-fundamental в §1.2 (Слой 2 «физика + ML» — гибридная модель без конкретного примера PINN)

**Severity:** P1 — Missing-Fundamentals check.

**Evidence:** §1.2 «Архитектура четырёх слоёв» вводит «гибридную модель (hybrid model) или физико-информированное машинное обучение (Physics-Informed Machine Learning, PINN)» — но без конкретного формального примера и без объяснения, **как** physics-based loss комбинируется с data-driven loss. Студент 3 курса видит термин, но не имеет mental model «что это означает в формулах или коде».

**Recommendation:** добавить +150 слов в §1.2 (после введения «гибридная модель»):

> **Пример PINN.** Для теплового реактора: data-driven loss L_data = MSE(predicted_T, measured_T) + physics-informed loss L_phys = (∂T/∂t − α·∇²T)² (residual от уравнения теплопроводности). Финальный loss = L_data + λ·L_phys, где λ ≈ 0.1–10 балансирует data-fit и физическую consistency. Эта архитектура работает там, где **физика частично известна, данных недостаточно**: вместо обучения только на наблюдениях, модель **штрафуется** за нарушение физических законов. PINN дают лучшую generalization на out-of-distribution состояния, чем чистый ML, но требуют более долгого обучения (10–100× больше эпизодов градиентного спуска).

## P1-5. Insider phrasing «рабочее правило» в §2.4 (anti-pattern grep match)

**Severity:** P1 — CLAUDE.md anti-pattern catalog «рабочее определение / прикладное X / X в режиме Y».

**Evidence:** `chapter.md:478`: «**Эмпирическое правило для PdM.** **Рабочее правило**: для статистически защитимого ML-предсказания нужны ≥30 событий каждого типа отказа в обучающем наборе».

«Рабочее правило» = insider phrasing, не canonical. Canonical: **«статистическое правило» / «эмпирическое правило» / «правило большого пальца» (rule of thumb)** — все три уже canonical в литературе.

**Recommendation:** заменить «Рабочее правило: для статистически защитимого ML-предсказания нужны ≥30 событий...» → «**Эмпирическое правило ≥30 событий.** Для статистически защитимого ML-предсказания нужны ≥30 событий каждого типа отказа...». Это убирает дублирование «**Эмпирическое правило**. Рабочее правило...» и решает insider-phrasing вопрос.

## P1-6. §1 hero (Siemens Digital Twin Composer time scrubbing) — описан в text, но без явного visual anchor

**Severity:** P1 — plan v2 frontmatter line 22 (`hero_s07_plan`) предусматривает s07 = Siemens Digital Twin Composer screenshot **с явным UI**. Chapter §1.1 line 192 описывает time scrubbing в тексте, но без референс на конкретный visual element для slides Phase 5-8. Это **gap между chapter (text-only) и slides (visual)**, который Phase 6 (presentation-designer) должен будет заполнить через 6-tier image acquisition.

**Evidence:**
- Plan v2 frontmatter: «hero_s07_plan: Siemens Digital Twin Composer screenshot реального UI с time scrubbing. 6-tier acquisition».
- Chapter §1.1 lines 190-192 описывают product + functionality в тексте, но без подсказки producer-агенту: «visual anchor для s07 — UI screenshot Time Scrubbing slider + 2D/3D split view».

**Recommendation:** добавить в §1.1 после описания time scrubbing inline-marker `<!-- visual-anchor: Siemens DT Composer UI screenshot, 6-tier acquisition required for s07 -->` чтобы Phase 6 designer мог точно identify visual scope. Это helps **future-proof** chapter as source-of-truth.

---

# P2 issues (polish)

- **P2-1.** §0.2 (`chapter.md:139–144`) — все 6 базовых аббревиатур имеют inline gloss, но `chapter.md:146` объявляет «добавим в ходе главы следующие термины при первом упоминании: TSN, FKDPP, GAMP 5, ATEX Zone 0, scan-based execution, Lighthouse Network, SHAP / LIME, MTBF, RCM, IEC 61508 SIL 2/3, ГОСТ Р 57700.37-2021, OPC UA FX». Список из 12 терминов, но это **анонс**, а не gloss. При первом упоминании каждого — gloss присутствует (verified). P2: формулировка списка слегка громоздкая, можно упростить «Дополнительные термины (gloss при первом упоминании): TSN, FKDPP, ...».

- **P2-2.** §1.1 line 174: «Werner Kritzinger и соавторы в IFAC-PapersOnLine опубликовали категориальный обзор литературы» — год публикации 2018 явно дан в источнике [15], но в тексте §1.1 не повторён в этом предложении. Inline год полезен для skim.

- **P2-3.** §1.3 (chapter.md:248) — «индустриальный метаверс» введён без gloss (cf. Лекция 8 разбирал industrial metaverse как concept, но Лекция 12 students могут не знать). Добавить gloss inline.

- **P2-4.** §3.4 line 119 «На вид — правдоподобно. Команда `MOV` существует в STL (Statement List)» — STL gloss дан inline, но первый раз STL появляется в `chapter-part2.md:97` без gloss «`ladder logic (LD), structured text (ST), function block diagram (FBD), sequential function chart (SFC)`» — STL появится 20 строк позже. Незначительный, но cleaner — gloss STL в строке 97.

- **P2-5.** §4.5.1 line 336 «Camera array — 3D LiDAR + RGB-стерео» — gloss «LiDAR» (Light Detection And Ranging) и «RGB» (Red-Green-Blue color channels) могут быть полезны для не-аудио/видео-инженерной аудитории.

- **P2-6.** §7.2 (chapter-part3.md:367–392) — КАМАЗ / Росатом / Норникель — три кейса описаны, но без явной таблицы сравнения «cтупень автономии A0 / A1 / A2 / A3 + сектор + ROI + status». Self-check Q2 (`chapter-part3.md:475`) спрашивает «какой из них наиболее зрелый по шкале автономии (A0/A1/A2/A3)?» — но в тексте нет sharp mapping. Сейчас «КАМАЗ ≈ A0/A1 advisory + двойник конвейера», «Росатом ≈ A0 simulation + advisory», «Норникель ≈ A1→A2 transition flotation» — это inference, но не explicit. Таблица в §7.2 сделает self-check tractable.

- **P2-7.** §8 closing (`chapter-part3.md:484-504`) — solid, но Section 11 plan v2 предлагал Q&A blockchain reference (Q4 «MPC vs RL для furnace» уже в Q&A backup; cross-ref на §5.2 критерий 2). Возможна micro-grade clearer cross-link «Q&A Q4 — конкретное worked example MPC vs RL для типичного запроса инженера».

---

# Cross-cutting issues

- **LO coverage:** LO2 / LO5 / LO7 все покрыты. LO2 (оценить вендорское заявление) — §5.4 5 вопросов вендору + §1.6 5 вопросов data audit; LO5 (опишет 7-слойную архитектуру) — §6.1 + §6.2 + §6.3 + §6.4; LO7 (применит структурные критерии) — §5.2 десять критериев + §5.3 worked example. PASS.
- **Cognitive load:** §0.2 шесть аббревиатур + §0.1 четырёхступенчатая шкала + §1.1 Kritzinger taxonomy — это **много** для первых 8 минут. Однако §0.2 phrased как «обязательные термины», §0.3 — roadmap, и aviso «продолжение глоссария по ходу главы» on line 146. ACCEPTABLE.
- **Sequence:** концепты вводятся до использования. Keystone предъявлен в §0.1 ДО первого погружения в A0. ISA-95 disambiguation в §0.1 ДО §1.2 (где 4 слоя архитектуры). Kritzinger taxonomy в §1.1 ДО §1.5 (Southeast Asian Port = shadow-not-twin discussion). PASS.
- **Assertion-evidence:** каждый блок имеет thesis + numbers + lesson. Sample 5 проверены, все pass. PASS.
- **Self-check:** каждый из 5 major разделов (§1, §2, §3, §4, §4.5, §5, §6, §7) имеет 5-question self-check. PASS.
- **Tone:** уважительный «вы»/инженер 3 курса; 0 «магическая пилюля» / «УГАДАЙ» / familiar CTA. PASS.

---

# Strengths

1. **Keystone A0→A1→A2→A3 предъявлен в §0.1 ДО первого погружения** с anchor (SAE J3016 + ISO 22989) и обязательной disambiguation от ISA-95 (Лекция 11 §5.3). Это **structural pass** keystone-axis ENFORCED-check.
2. **Anti-overlap с lec-11 чисто выполнено.** Yokogawa FKDPP в §4.3 переориентирован на **twin-as-sandbox** (architectural angle, lec-11 §3.2 = algorithmic angle). Tesla 2018 = single cross-ref line `chapter.md:84` + `chapter.md:299` («не дублируем нарратив; здесь — другая ошибка»). Southeast Asian Port 2024 = fresh hero §1.5. ChatGPT-PLC cross-ref на lec-11 §1.2 (`chapter-part2.md:139`).
3. **AI-Failure & Judgment Share strict-in ≈40-45% holistic** — все 3 части chapter ≥30% (chapter.md 38.9%, part2 49.3%, part3 45.7%). §5 = densest (15 minutes ≈ 22% lecture timing on failure/limits). Distribution **не** single-cluster — failure-bucket размазан по 8 разделам.
4. **Worked example §5.3 фарма+FDA** доведён до verdict «AI not applicable для финального release decision + двухслойная альтернатива (AI on design + human-in-loop QA с USP <905> testing)». Это **canonical demonstration** «AI vs not-AI» selection logic в regulated domain.
5. **Inline glosses 13/13 jargon терминов** при первом упоминании. PASS.
6. **0 named-institution leaks** (МГТУ / Бауман / Кафедра ИУ / ВКА / МАИ / СПбГУ). PASS.
7. **40 sources inline-referenced** через [N]; references в отдельном файле per CLAUDE.md doc-size-limit. PASS.
8. **14 Q&A backup** с 200-300 word ответами на каждый. PASS.
9. **Bridge к Лекции 13** на §8 с **canonical phrasing** «AI в логистике, цепях поставок и транспорте» (locked phrasing). PASS.

---

# Top-7 specific recommendations (prioritized for Phase-3 revision)

1. **Add ~3 000 words targeted depth** (P0-1) — distribute по 10 sections (см. P0-1 recommendation), exit ≥30 000.
2. **Deep russification pass** (P0-2) — eliminate ≥150 of 347 critical anglicism hits in narrative body (target: 0 «production-grade», 0 «release» in body sense, ≤5 «edge» in non-jargon sense). Phase 4 (slides + speech) should not be doing this work — it's chapter-first source-of-truth.
3. **Fix 35-day FKDPP self-contradiction** (P1-1) — chapter.md:125 → «обучалось тысячи эпизодов в симуляции + 35 дней непрерывная production-эксплуатация на JSR».
4. **Strip timing/methodology meta-commentary в visible body** (P1-2) — 5+ specific replacements.
5. **Move `[for-slide-sNN]` markers в HTML-comments** (P1-3) — preserves build-deck pipeline mapping, eliminates visible-body leak.
6. **Add PINN concrete formula в §1.2** (P1-4) — +150 words с loss formula.
7. **Add A0–A3 mapping table в §7.2** (P2-6) — explicit КАМАЗ / Росатом / Норникель × A0/A1/A2 grid + ROI + status. Self-check Q2 becomes tractable.

---

# Self-checks (verification matrix)

- [x] **Failure-share independently recalculated:** strict-in 44.6% holistic; chapter.md 38.9% / part2 49.3% / part3 45.7% — все ≥30%. PASS (book-editor self-report 54% слегка inflated, но реальный 45% всё равно well above target).
- [x] **Deep latin-token scan:** 1354 unique latin tokens; 984 non-whitelist non-acronym; 347 critical anglicism hits (top: edge ×43, advisory ×29, production-grade ×23, release ×17). **FAIL >5 P0 threshold.**
- [x] **Anti-overlap re-check:** Yokogawa FKDPP angle = twin-as-sandbox (architecture), не algorithmic; Tesla 2018 = single line + cross-ref; Southeast Asian Port = fresh hero. PASS.
- [x] **Anonymization:** 0 named-institution hits с strict regex. PASS.
- [x] **Inline glosses 13/13:** TSN / FKDPP / GAMP 5 / ATEX Zone 0 / scan-based execution / Lighthouse Network / SHAP / LIME / MTBF / RCM / MPC / IEC 61508 SIL / ГОСТ Р 57700.37 / OPC UA FX — все glossed at first mention. PASS.
- [x] **14 Q&A:** Q1-Q14 all present with 200-300 word answers. PASS.
- [x] **Locked numbers (sample 5):** [1] 36.19B→180.28B / 37.87% ✓; [2] $12M / 18 months Southeast Port ✓; [3] 75% failure rate ✓; [4] Yokogawa 35 days **INCONSISTENT** (P1-1); [5] Lighthouse 220+ / +16% EBIT ✓. 4/5 PASS, 1 P1.
- [x] **Word count in band 28 500–31 500:** 26 908 actual. **FAIL (-1 592 from lower bound).**
- [x] **Multi-part structure:** chapter.md = 507 lines ≤600 ✓; chapter-part2.md = 398 ≤600 ✓; chapter-part3.md = 590 ≤600 ✓ (близко к лимиту); references.md = 64 ≤600 ✓. Frontmatter `parts: 3`, `parts_files: [chapter.md, chapter-part2.md, chapter-part3.md, references.md]` consistent. PASS.

---

**Verdict: REVISE.** 2 P0 (word count <28.5k; 347 critical anglicism hits) + 6 P1 (FKDPP self-contradiction, timing/methodology leak, [for-slide-] markers visible, PINN missing, insider phrasing, hero anchor gap). После Phase-3 revision targeting **+~3000 words** + **deep russify pass** + **6 P1 fixes** — re-run methodology critique для подтверждения APPROVE-CLEAN.
