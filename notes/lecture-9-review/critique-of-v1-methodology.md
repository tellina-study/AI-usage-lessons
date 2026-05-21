# methodology-critic — критика plan-v1.md (Phase 1)

**Дата:** 2026-05-20
**Критик:** methodology-critic
**Target:** `notes/lecture-9-review/plan-v1.md` (218 строк, ~3000 слов)
**Verdict:** **APPROVE-WITH-POLISH**
**Counter-check:** strict-in ≥30% PASS (структурно ≥48% time, ≥38% slides); keystone-axis ENFORCED PASS; tools-per-taxonomy L4+ PASS (с замечаниями).

---

## TL;DR

План v1 — методически крепкий: ось OODA предъявлена корректным keystone-слайдом в Разделе 0 ДО первого погружения; tools-per-taxonomy L4+ соблюдено для всех трёх звеньев с anti-hype и volatile-разметкой; strict-in failure budget структурно выше порога ≥30% с холистическим распределением по 3 артефактам. Главные проблемы — **3 P1 issue, 6 P2**: (1) LO1 формулировка смешивает «3 уровня OODA» и «adoption direction», что комбинирует Remember+Apply Bloom-levels в одном LO; (2) Раздел 4 «7 sub-sections × 2 мин» — pacing нереалистичен, нужно сократить; (3) glossary-слайд (SAR/ATR/ISR/EW/LAWS/OODA) упомянут только косвенно в R6 митигации plan-of-attack, в plan-v1 не присутствует. Hook A (BEFORE/AFTER sat) — методически корректный выбор, B как fallback тоже OK. Phase 2 (chapter draft) можно начинать после устранения P1 issue.

---

## P0 issues (must fix перед Phase 2)

**Нет P0 issue.** Плановый артефакт не содержит keystone-axis-нарушений (Лекция 4 lesson cost), tools-per-taxonomy ENFORCED L4+ соблюдено, AI-Failure ≥30% strict-in структурно достижимо в каждом из 3 артефактов.

---

## P1 issues (should fix)

### P1-1 — LO1 смешивает Remember + Apply, нарушает Bloom-level чёткость

**Где:** строка 27.
**Текст плана:**
> «**LO1.** Указать 3 уровня OODA и для каждого назвать 2-4 dominating 2026 tool/program + направление adoption.»

**Проблема:** LO1 объединяет (а) **Remember** (назвать уровни и tools) + (б) **Apply/Analyze** (определить направление adoption). Это разные Bloom-levels, оцениваются по-разному. Для intermediate-лекции (L4-L12) LO1 как Remember-only — слабо; как Apply — нужно вынести отдельно.

**Evidence:** Лекция 7 (intermediate, аналог по уровню) разделяет LO1 (Remember-классификация) и LO2 (Apply-оценка применимости) — см. `library/lectures/lec-07/chapter.md` строки 62-65. Это методически корректное разделение.

**Recommendation:** разбить LO1 на:
- **LO1a (Remember).** «Назвать 3 звена OODA и для каждого — 2-4 dominating 2026 tools/programs.»
- **LO1b (Apply).** «Для конкретного aerospace кейса определить, в каком звене OODA AI работает / на стыке звеньев происходит провал.»

Это даёт LO1, LO1b, LO2, LO3, LO7 — пять LO, что согласуется с lec-07 паттерном.

---

### P1-2 — Раздел 4 «7 sub-sections × 2 мин» — pacing нереалистичен

**Где:** строки 137-149 (Раздел 4 — 15 мин).
**Текст плана:**
> «**Содержание (7 sub-sections × ~2 мин).** … 4.1 L1-L5 ladder; 4.2 UN GGE timeline; 4.3 ICRC position; 4.4 Stop Killer Robots; 4.5 Maven + Nimbus; 4.6 HITL pattern; 4.7 Russia votes.»

**Проблема:** 2 мин/sub-section — это **один слайд + 90 секунд устной речи** на каждую тему. Для большинства sub-sections это physically OK (UN GGE timeline, ICRC, SKR могут жить как «короткие референсы»), но 4.1 L1-L5 ladder + 4.5 Maven walkout + 4.6 HITL pattern — это **полноценные педагогические блоки**, требующие ≥3-4 мин каждый (с mapping examples и discussion).

Cognitive load для финального раздела (студент уже потратил 45 мин активного внимания) дополнительно отягощает плотность.

**Evidence:** Lec-07 § 4.1-4.6 (этический раздел аналогичного веса) — 6 sub-sections + Раздел 5 на ~25 мин content time, не 15. Lec-04 reflection документировала, что финальные этические разделы требуют буфера на Q&A-внутри-раздела.

**Recommendation:**
- Слить 4.3 ICRC position + 4.4 Stop Killer Robots в один sub-section «4.3 ICRC + SKR positions» (они тематически параллельны).
- Дать 4.1 L1-L5 ladder ≥3 мин (это центральный visual всего раздела — нельзя оставить 2 мин).
- Дать 4.6 HITL pattern ≥3 мин (это центральный engineering takeaway).
- Итого 6 sub-sections × средне 2.5 мин = 15 мин — реалистично. Либо: расширить раздел до 17 мин и сжать Раздел 5 до 8 мин (5.2 career + 5.3 reading сжимаются легко).

---

### P1-3 — Glossary-слайд (SAR/ATR/ISR/EW/LAWS/OODA) отсутствует в plan-v1

**Где:** plan-v1 в целом; в plan-of-attack R6 митигация упомянута, но в v1 не отражена.
**Проблема:** аэрокосмос-специфичная терминология (SAR, ATR, ISR, EW, CCA, IFF, MCAS, ALIS/ODIN, FedRAMP, IL4/IL6, SC2S/SIPR/JWICS, AoA, GNSS, LAWS, AWS, OODA, ROE, IHL) — это **20+ аббревиатур**, разбросанных по плану. Студент ИУ 3 курса знает базовый авиакосмический минимум, но **не знает defense-acronyms**. Missing-Fundamentals check (CLAUDE.md ENFORCED от Лекции 4) требует явного glossary-слайда либо inline-explain каждой аббревиатуры.

**Evidence:**
- Plan-of-attack R6 (строки 139-141) формулировал: «методолог Phase 3 ловит missing-fundamentals явно».
- Plan-v1 строки 47-66 (Tools-per-taxonomy) используют SAR, ATR, EW, IL4/IL6, SC2S/SIPR/JWICS, EOCL, ARP4754A, DO-178C **без определения**.
- Lec-07 имеет inline-разъяснение терминов (CXR, FDA-cleared, PCCP) на первом упоминании.

**Recommendation:** добавить в Раздел 0 (или как часть Sense divider в Р1) **glossary-слайд**: «Defense/aerospace alphabet soup — что значит каждая аббревиатура». 6-8 ключевых терминов: SAR / ATR / ISR / EW / OODA / LAWS / HITL / CCA. Альтернатива — explicit inline-разъяснение на первом упоминании каждого acronym, и зафиксировать это требование в Phase 2 brief для book-editor.

**Cost-of-omission:** на Phase 3 methodology-critic chapter точно flag-нет missing-fundamentals — это back-and-forth между designer и writer.

---

## P2 issues (polish)

### P2-1 — LO2 ссылается на canonical case Lancet, но это **Russian** case

**Где:** строка 28.
**Текст:** «LO2. … canonical case: Lancet ATR rollback.»
**Проблема:** хороший pedagogical выбор, но в LO явно зафиксирован Russian case. Это OK, но note: если на Phase 3 fact-checker найдёт single-source caveat у Lancet ATR rollback claim — fallback canonical case должен быть наготове (DARPA X-62A demo-scripted-scenario или F-35 ALIS как cross-cutting).

**Recommendation:** в Phase 2 brief — designate Lancet как primary + ALIS scripted-scenario как backup canonical case.

---

### P2-2 — Hook B (ALIS failure-first) недооценён

**Где:** строки 79-84.
**Текст:** «B. F-35 ALIS → ODIN провал — … Failure-first hook, прямо служит AI-Failure rule, но **mood депрессивный**.»

**Проблема:** «mood депрессивный» — слабое возражение против hook'а, который **align с курсовой миссией** («учить говорить нет неподходящему ИИ»). Failure-first opening **методологически сильнее** для course mission, чем visual-wow «как AI это делает». Курс не учит AI-enthusiasm — учит judgment.

Сравнить: Lec-7 Chapter уже задаёт failure-first нарратив в опенере (см. строка 85 chapter.md: «Если научиться оценивать AI здесь, остальные индустрии становятся методически легче»).

**Recommendation:** не отвергать B на основании «mood». Если визуал A не доходит (Wikimedia-licensing fail, политическая чувствительность), B — strong alternative. Зафиксировать оба как parallel candidates для Phase 5 designer brief. Final pick — после визуал-fact-checker'а Wikimedia доступности.

---

### P2-3 — Раздел 5 (10 мин на 4 sub-sections) tight, но workable

**Где:** строки 154-161.
**Проблема:** 5.1 (7 критериев) — это **4 мин**. Каждый критерий = 30 секунд. Это **очень быстро** — критерии должны быть либо visual-checklist (один слайд, lecturer прочитывает), либо разнесены по разделам как «вывод из секции» с финальным consolidation slide. 5.2 career + 5.3 reading + 5.4 closing — 6 мин, OK.

**Recommendation:** 7 критериев — **visual checklist-слайд** + 30-секундный recap каждого. ИЛИ — разместить каждый критерий как «закрывающий takeaway» в конце соответствующего звена OODA (Sense → 2 критерия; Decide → 2; Act → 1; LAWS → 2), а в Разделе 5 — consolidation as single slide. Это improves retention (distributed retrieval vs end-loaded list).

---

### P2-4 — Russian context 22-25% — выше zip-fixed target 15-20%

**Где:** строка 201 (open question 4).
**Текст:** «Russian context — 15-20% объёма? Сейчас ~7-8 из 32 = 22-25% — чуть выше target.»

**Проблема:** план явно выше target, но не критично — Bauman audience-relevant, симметрично lec-07 (FDA+mosmed.ai). **Принять без редактуры**, но зафиксировать в Phase 2 brief: если на Phase 3 reader-simulator сообщит «overweighted Russian content» — резать TerraTech BRICS slide или Sber GigaChat ISS slide (последний — single-source caveat anyway).

**Recommendation:** Phase 2 chapter — taxonomy «1 RU case per section + 1 cross-cutting (Geran-2 sanctions)», не больше. Не давать >2 RU cases в одном разделе.

---

### P2-5 — DoD Directive 3000.09 — open question оставлена designer'у

**Где:** строка 203 (open question 6).
**Текст:** «DoD Directive 3000.09 — отдельный слайд в Разделе 4 или достаточно одной строки в Normative References?»

**Проблема:** это **content decision**, не visual. План должен решить, не оставлять открытым для Phase 5 designer'а.

**Recommendation:** **строка в Normative References** + briefly mention в 4.6 HITL sub-section (раз сам Directive описывает HITL requirement). Отдельный слайд избыточен для 75-мин лекции.

---

### P2-6 — Anthropic-Palantir + OpenAI removed-ban — расположены в Р2 Decide, но это meta-level fact (industry ethics)

**Где:** строки 56, 111.
**Проблема:** оба факта (Anthropic removed military ban Jan 2024; OpenAI removed Jan 2024) — meta-level industry shifts, не Decide-tools per se. Сейчас они появляются в Р2 (Decide) как working cases, но их methodology-роль — **показать industry-ethics drift** (от Maven walkout 2018 до 2024 mass-adoption).

**Recommendation:** перенести Anthropic-Palantir + OpenAI ban-removal в Р4 §4.5 (Maven walkout + Nimbus) — там это естественно встроится в narrative «personal ethics ≠ industry regulation». В Р2 оставить Claude IL6 deployment как tooling fact без timeline-context. Это улучшает story arc (chronological flow в Р4) и снимает дублирование.

---

## Strengths (что хорошо)

1. **Keystone-axis ENFORCED — полностью соблюдено** (строки 34-39). Заголовок keystone «Три звена цепи. AI входит в каждое — но по-разному» — про **саму ось**, НЕ про устройство курса / защиту подхода. Каждый раздел = motivated спуск по оси (Sense → Decide → Act → Граница → callback). Лекция 4 lesson cost полностью предотвращена.

2. **Tools-per-taxonomy L4+ ENFORCED — соблюдено для каждого звена** (строки 45-68):
   - Sense: 5+ tools 2026, adoption направление, anti-hype «бренд ≠ режим работы», volatile-метки `[VFY-day-of]`.
   - Decide: 5+ tools, anti-hype «LLM hallucinations + automation bias», инфраструктура (FedRAMP, IL4/6, SC2S) **отделена**.
   - Act: 5+ tools, anti-hype «hype far ahead of true autonomous engagement», Russian + Chinese для контраста.
   - Инфраструктура (DO-178C, ARP4754A, edge compute) — **отделена** в свой блок, не смешана.

3. **AI-Failure ≥30% strict-in структурно достижимо** в каждом артефакте (counter-check ниже).

4. **Cross-lecture handoffs** — корректно зафиксированы (строка 16): Lec-3 foundation models, Lec-4 copilot/agent риски, Lec-6 topology optimization, Lec-7 symmetric Russian-context model, Lec-8 generative модели.

5. **Hook A выбор обоснован** методически: 2026-evergreen visual, политически нейтрален, ставит вопрос «как AI это делает?». Не повторяет Лекция-2 ошибку с outdated empirical test (strawberry). B как fallback документирован — антипаттерн «only one option» избегнут.

6. **Strongest 5 cases (working) + strongest 5 failures (research) — все попали в plan**:
   - Working: Maxar Sentry ✓ (Р1), Rolls-Royce + Airbus Skywise ✓ (Р1), Anduril Fury ✓ (Р3), X-62A VISTA ✓ (Р3). Note: 5й — Helsing Altra placed in Р2 (Decide), что разумно.
   - Failures: Lavender ✓ (Р2), MCAS ✓ (Р3), ALIS ✓ (Р1 cross-cutting), Vincennes ✓ (Р2), Lancet ✓ (Р2).

7. **Volatile числа корректно размечены `[VFY-day-of]`** (строки 50, 57, 64) — не оставлены на видимом слое для устаревания между datapoint и lecture day.

8. **Russian context симметричен** западному (строки 47, 54, 61, 103, 118, 133): single-source caveats явно отмечены (Sber GigaChat ISS, Svod/Glaz-Groza, Lancet videos). Aerostate явно отсутствует (правильно — `00-summary.md` строка 141).

9. **Reading list (5.3)** — академически сильный (Scharre, CSIS, Abraham, ICRC, DARPA, GAO, SKR) — балансированный, не однобокий.

---

## Recommendations (конкретные fixes с указанием строк)

| # | Issue | Строка | Fix |
|---|---|---|---|
| P1-1 | LO1 mixes Bloom-levels | 27 | Разбить на LO1a (Remember) + LO1b (Apply); итого 5 LO |
| P1-2 | Раздел 4 pacing 2 мин × 7 | 141 | Слить 4.3+4.4; дать 4.1, 4.6 по ≥3 мин; либо +2 мин из Раздела 5 |
| P1-3 | Glossary missing | (новое) | Добавить glossary slide в Р0 либо inline-explain mandate в Phase 2 brief |
| P2-1 | LO2 Lancet backup | 28 | Phase 2 brief — designate ALIS scripted backup |
| P2-2 | Hook B недооценён | 80-83 | Hold both A+B parallel; final pick — после Wikimedia availability check |
| P2-3 | 7 критериев в 4 мин | 157 | Distribute критерии по разделам + consolidation slide в Р5 |
| P2-4 | RU 22-25% | 201 | Принять; зафиксировать taxonomy «1 RU case / section» |
| P2-5 | 3000.09 open | 203 | Decide: строка в Normative + mention в 4.6 HITL |
| P2-6 | Anthropic+OpenAI ban | 56, 111 | Перенести в Р4 §4.5 Maven walkout narrative |

---

## Counter-check report

### AI-Failure ≥30% strict-in — PASS (структурно)

**Independent verification (не верю plan-self-report 39.5%):**

| Раздел | Strict-in time | Strict-in slides |
|---|---|---|
| Р0 keystone | 0 | 0 |
| Р1 Sense | 3 failure blocks × ~2 мин = 6 мин | 1 explicit (ALIS chart, slide 7); 2 implicit (SAR, GPS — no own slide) |
| Р2 Decide | 3 failure blocks × ~2-3 мин = 7-8 мин | 3 explicit (Lavender slide 9, Vincennes slide 10, Lancet slide 11) |
| Р3 Act | 3 failure blocks × ~2-3 мин = 7-8 мин | 2 explicit (MCAS slide 17, Replicator slide 19) |
| Р4 целиком strict-in | 15 мин | 5 (slides 20-24) |
| Р5 критерии (5.1) | 4 мин | 1 (slide 25 checklist) |
| **TOTAL** | **39-41 мин из 70 content** = **56-59%** | **12 explicit из ~27 content slides** = **44%** |

Plan-self-report (~48-56% time, ~38-44% slides) — **подтверждается независимо**. Margin над 30% — comfortable.

**Холистичность across 3 артефактов** (plan-level promise):
- chapter ~35-40% слов — **PASS plan-level** (нужно verify Phase 3).
- slides ~38-44% — **PASS plan-level**.
- speech ~30% (5k слов × 30% = 1500 слов) — **PASS plan-level**.

**Counter-check.** No single-artifact concentration. Раздел 4 (целиком strict-in) распределён по всем 3 артефактам — не сконцентрирован в одной книге или одном deck.

---

### Keystone-axis ENFORCED — PASS

Строки 34-39:
- Keystone slide = **первый content slide** после cover/lecture-map, ДО любого погружения ✓
- Заголовок «Три звена цепи. AI входит в каждое — но по-разному» — про **саму ось**, НЕ про устройство курса / защиту подхода / recap ✓
- Каждый раздел = motivated спуск/подъём по оси ✓
- Dual-use лента как тонкий фон (не отдельная ось) — корректное вложение Опции В ✓

Лекция 4 cost-of-omission (~5 циклов deck) **полностью предотвращена**.

---

### Tools-per-taxonomy L4+ ENFORCED — PASS

| Уровень оси | Tools 2026 (2-4+) | Adoption direction | Anti-hype | Volatile→`[VFY-day-of]` | Infra отделена |
|---|---|---|---|---|---|
| Sense | 5 (Maxar, BlackSky, Planet, Slingshot, Φ-sat-2) + 3 RU | растёт ✓ | «бренд ≠ режим работы», «AI-derived часто = classic CV» ✓ | NRO EOCL, SDA T3, BlackSky subs ✓ | (CI/SAST отделено в блок) ✓ |
| Decide | 5 (Palantir MSS, Scale Donovan, Helsing, Anthropic, Anduril Lattice) + 4 RU | растёт ✓ | «LLM hallucinations + automation bias», «accuracy 90% ≠ 90% решений», «инфраструктура отдельно» ✓ | Palantir MSS ceiling, Anduril, Helsing, Thunderforge ✓ | FedRAMP / IL4/6 / SC2S / SIPR / JWICS — **отделено** ✓ |
| Act | 5 (Fury, V-BAT, X-62A, Saker, Roadrunner) + 3 RU + 2 CN | растёт ✓ | «hype far ahead of true autonomous engagement», «96-drone = centralized, не decentralized» ✓ | Fury rate, Replicator delivered, Geran-2 monthly, Shield AI valuation ✓ | DO-178C / ARP4754A / Jetson — отделено ✓ |
| Инфраструктура | (отдельный блок) | — | — | — | **Не AI capability — плитка под капабилитис, один слайд** ✓ |

**§-named speech-narrative → slide check** (строки 141-149, Раздел 4): 4.1 L1-L5 ladder → slide 20 ✓; 4.2 UN GGE timeline → slide 21 ✓; 4.3 ICRC → slide 22 ✓; 4.4 SKR → slide 22 (combined) ✓; 4.5 Maven → slide 23 ✓; 4.6 HITL → slide 24 ✓; 4.7 Russia votes → slide 21 voting map ✓. **No §-named narrative без слайда**.

PASS, без owner-обоснований устных якорей.

---

### Holistic across 3 artifacts (plan-level promise)

- chapter strict-in target 35-40% слов — committed in plan, **verifiable Phase 3**.
- slides strict-in target 38-44% — committed, **verifiable Phase 7**.
- speech strict-in target ≥30% — committed in plan-of-attack §4, **verifiable Phase 10**.

**Plan-level: PASS.** Actual will be re-checked in Phases 3, 7, 10. Если на любой phase actual <30% или single-artifact concentration → verdict REVISE.

---

## Verdict justification

- **0 P0** issues.
- **3 P1** issues (LO Bloom-mix, Р4 pacing, glossary missing) — все **fixable до Phase 2 без перепланирования**.
- **6 P2** issues — polish.

**Counter-check 5+ P1 → REVISE catch-all:** 3 P1 < 5 → **APPROVE-WITH-POLISH** корректно.

**Phase 2 (chapter draft) можно начинать** ПОСЛЕ устранения 3 P1 в plan-v2 (или решения отложить в Phase 2 brief как explicit instructions для book-editor). Рекомендую: P1-1 (LO разбить) + P1-3 (glossary mandate) — решить в plan-v2 минимальной редактурой; P1-2 (Раздел 4 pacing) — можно решить либо в plan-v2, либо в Phase 5 design brief как explicit «4.3+4.4 combined, 4.1+4.6 priority slides».

**Не рекомендуется** возвращать в Phase 1 для полной переработки — это polish-уровень изменений, не структурных.
