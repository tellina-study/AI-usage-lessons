# Methodology critique — lec-10 plan-v2 (narrow rerun)

**Дата:** 2026-05-21
**Критик:** methodology-critic
**Target:** `notes/lecture-10-review/plan-v2.md` (598 строк, ~3 900 слов)
**Scope:** узкая верификация fix-применения для 6 P1 (v1 methodology) + 3 P0 (v1 reader) + 5 P2 (v1 methodology) + counter-checks без regression.

---

## Verdict

**APPROVE-CLEAN.**

**Counter-check:** 0 P0, 0 новых P1, 1 P2 polish (нестрогий, не блокирующий). ≥5 P1 trigger → не сработал. План структурно готов к Phase 2.

---

## TL;DR

Plan-v2 применяет **все 6 P1 + 3 P0 + 5 P2 fixes** из критики v1 — каждый локализуем по строкам, без regression. Math пересчитан и согласован (5+14+15+12+10+8+6 = 70 мин content + 5 buffer + 10 Q&A = 85 мин, frontmatter consistent). Strict-in 34/70 = 48.6% **проверено независимо** — совпадает с self-report; distribution **холистичен по Р1-Р5** (64/50/29/40/33%), Р4-bis 100% **корректно** оправдан как dedicated meta-failure section. Keystone-axis ENFORCED по-прежнему PASS; tools-per-taxonomy L4+ — нет regression; document size 598 ≤ 600 limit с 2-line маржой.

3 потенциальных слабости отмечены ниже как **информационные ноты** (не issues): (а) Р3 12-мин budget немного оптимистичен относительно 6+3.5+1+пометки = 10.5–11 мин (1-1.5 мин slack); (б) Р4 10-мин budget с inline glossary 5 терминов + 4 working cases + 2 failures + RU context = плотный (но pseudo-flow интегрирован в Cargill case как efficiency); (в) Р4-bis новый раздел добавил 1 cross-section dividing slide к slide-budget (учтено в превью). Ни одна не методически критична для Phase 2.

---

## P1 от v1 — verify fix статус

| # | P1 issue (v1) | Fix applied? | Quality | Evidence (строки plan-v2) |
|---|---|---|---|---|
| **P1-1** | LO1 mixes Remember + Apply | ✅ | full | LO разбит на LO1a (Remember, str. 31) + LO1b (Apply, str. 32) + LO2 + LO5 — итого 4 LO. LO1b явно включает «anti-hype оговорку (брéнд ≠ режим работы; demo ≠ deployment; declared ≠ measured)» — это методически чище чем v1. |
| **P1-2** | Раздел 5 density-bomb (8 sub-сек × 1.75 мин) | ✅ | full | Применён вариант (4) из v1 recommendation: новый **Р4-bis «Среда» (8 мин)** после L4, и Р5 сокращён до **6 мин** (L5 retail 2 + 5 критериев consolidation 2 + payoff career/reading/callback 2). Math: 5+14+15+12+10+8+6 = 70 мин content + 5 buffer + 10 Q&A = 85 мин full (consistent в frontmatter str. 5, бюджет-табл str. 311, заключение str. 598). |
| **P1-3** | Vertical farming F1+F6 split, Tortuga bridge натянут | ✅ | full | F6 удалён из Р2 (str. 182 explicit: «F6 vertical farming **удалён** (consolidated в Р1)»). Vertical farming = 1 deep dive 5 мин в Р1 (str. 164-170): AppHarvest+ToBRFV + Plenty bankruptcy + Bowery + 14 банкротств + Tortuga **как footnote** (str. 168: «business-model lesson, не technical robotics lesson»). Bridge Р1→Р2 переформулирован (str. 170). |
| **P1-4** | Р3 «Животное» overload (10 мин на 4+2 кейсов) | ✅ | full | Р3 расширен до 12 мин (str. 205, явно отмечено «расширено из 10 в v1»). Holstein-bias выделен как 3-й отдельный anti-hype урок в F8 (str. 217-221) с «architecture asymmetry в datasets (transfer learning + локальные labeled data)» для local пород РФ explicit. Р4 сжат до 10 мин compensation (str. 230). |
| **P1-5** | Hook A success-first vs course mission | ✅ | full | Hook primary = B (Plenty Compton split-frame, failure-first, str. 139); fallback = C (Cognitive Pilot vs пыль, str. 141); Hook A перенесён в Р1 как opening working case (str. 143 + 155 «John Deere See & Spray Ultimate BEFORE/AFTER … Visual-wow success-first, переход к остальным L1 working cases»). Hero s01 = Plenty Compton (str. 391-398). |
| **P1-6** | Cognitive Pilot vs ИТЭЛМА «AI не нужен» подмена тезиса | ✅ | full | Все 3 локации v1 (185, 364, 383) изменены. Str. 201 содержит explicit reframe «**НЕ "AI vs не-AI"**, это **архитектурный выбор внутри AI-домена**» с пояснением «**разные функции:** ИТЭЛМА = "**где я нахожусь**" … Cognitive Pilot = "**что я вижу**"». AP2 split на AP2a (str. 337 «architecture choice within AI domain», alternative = sensor-fusion AI на multi-GNSS) + AP2b (str. 338 «genuine не-AI», alternative = mechanical weeders). РФ-урок политического риска иллюстрирован Мелитополем + Climate FieldView (str. 466 «**Главные иллюстрации этого урока — Мелитопольский кейс + Climate FieldView выход**, не Cognitive Pilot vs ИТЭЛМА»). Дополнительный bonus: explicit «нельзя их сравнивать как "один лучше другого"» — методическая чёткость. |

**Все 6 P1 — full fix.**

---

## P0 от reader-simulator — verify fix статус

| # | P0 issue (reader v1) | Fix applied? | Quality | Evidence |
|---|---|---|---|---|
| **P0-1** | Closed-loop operational definition в Cornerstone #2 | ✅ | full | Str. 56-60: «**Closed-loop AI** = AI внутри **feedback-controlled cycle** в **controlled environment**, где (а) среда контролируется … (б) feedback-data достоверны и timely, (в) AI-action возвращается в loop как next-cycle input». 3 явных компонента + примеры курса (медицина L7, фабрика L11, Cargill L4) — operational, не жаргон. Cornerstone #2 (str. 368) повторяет с привязкой «**наша рабочая формулировка для разделения сред**» — Term Canonical-Validity check pass. |
| **P0-2** | Agentic AI inline + pseudo-flow «как agent делает hedge» | ✅ | full | (a) Definition inline str. 113 + str. 235 (Р4 inline glossary): «**Агентный ИИ** = ИИ-агент с inference-циклом + tool-use, не один-shot ответ, выполняет multi-step задачи автономно». (b) Pseudo-flow интегрирован в Cargill case str. 242 как 4-step flow (Сенсор → Inference → Решение [с явным human-in-the-loop для >$10M] → Feedback за минуты-часы); явно отмечено «**узкий агентный ИИ** (одно действие — hedge), не general autonomy» — anti-hype frame. Media-rich list str. 255 включает «(20) "Как агент делает hedge" pseudo-flow diagram (drawio) — **критичный для grounding L4 абстракции**». |
| **P0-3** | Inline glossary 5 jargon terms (agentic, basis-points, hedge slippage, scope-3, AI-MRV) | ✅ | full | Str. 234-239 содержит явный inline glossary block «**Inline glossary (P0-3 fix — must при первом упоминании)**» со всеми 5 терминами + расшифровкой. Плюс basis-points перенесено в keystone section (str. 60) при первом упоминании; hedge slippage — inline в L4 tools str. 111 «–25..35% **hedge slippage** = расхождение …». Reader-simulator финансовый block теперь покрыт. |

**Все 3 P0 — full fix.**

---

## P2 от v1 — verify fix статус

| # | P2 issue (v1) | Fix applied? | Quality | Evidence |
|---|---|---|---|---|
| **P2-1** | AP6+AP7 в основной пятёрке | ✅ | full | Финальная пятёрка Р5.2 str. 326-331: AP1 (термодинамика), AP3 (threshold accuracy), AP4 (generic LLM), **AP6 (vendor lock-in)**, **AP7 (AI-MRV)** — оба «бонус» из v1 теперь в core. AP2a/AP2b/AP5 — inline в Р4-bis (str. 333-339) как architecture-specific. |
| **P2-2** | Cornerstone vs anti-AI mapping таблица | ✅ | full | Отдельный раздел «Cornerstone → Anti-AI critic mapping» str. 345-359 с таблицей 7 cornerstone → AP. Дополнительная нота str. 359 «**Это превращает 2 list-а в 1 system** (concept → application → assessment)». |
| **P2-3** | Q&A budget consistency | ✅ | full | 75 мин content + 10 мин Q&A = 85 мин full — consistent в frontmatter str. 5, бюджет-табл str. 311, заключение str. 598. |
| **P2-4** | Misattribution warnings — отдельный раздел | ✅ | full | Отдельный раздел «Misattribution warnings» str. 377-385 с 5 пунктами: Indigo Ag ≠ Verra; Tract data backbone; Verra phantom credits только rainforest, не all AI-MRV; Saga UV-C ≠ harvest; РСХБ vapor risk format. |
| **P2-5** | Hero s39 single primary | ✅ | full | Primary = Carbon Robotics LaserWeeder G2 (str. 400-402); Fallback = Cargill BIG AI Award; фотомонтаж explicit reject (str. 405). Foreshadow Lec-11 через подпись «**От поля до фабрики: AI-driven cyber-physical systems**». |

**Все 5 P2 — full fix.**

---

## Reader P1/P2/P3 nits — verify fix статус (бонусная проверка)

| # | Reader issue | Fix applied? | Evidence |
|---|---|---|---|
| reader P1-1 | Vertical farming split путает | ✅ | F1+F6 consolidated (см. P1-3 verify выше). |
| reader P1-2 | ToBRFV расшифровать + «closed loop ↑ blast radius» explained | ✅ | Str. 165 явный расшифровка «Tomato Brown Rugose Fruit Virus = томатный коричневый шершавый плодовый вирус» + operational explanation «в контролируемой среде сбой имеет увеличенный радиус поражения, потому что нет естественных барьеров». |
| reader P1-3 | Cognitive Pilot vs ИТЭЛМА «разные функции» | ✅ | Str. 201 «**разные функции:** ИТЭЛМА = "**где я нахожусь**" … Cognitive Pilot = "**что я вижу**"». |
| reader P1-4 | РФ-сводка anchor table | ✅ | s33 (anchor table в Р4-bis) явно в media plan str. 267 «(27) РФ-АПК-AI 2026 summary table (drawio — anchor для exam recall, P1-4 reader fix)». Содержание раскрыто в РФ-блок str. 464. |
| reader P1-5 | F2 ChatGPT context (кто/что/масштаб) | ✅ | Str. 172 «Nature Food 2024 (West/Williams et al.). **Кто/что/масштаб:** исследователи протестировали GPT-3.5 / GPT-4 / Bard на 184 вопросах о применении пестицидов и гербицидов; модели **уверенно рекомендовали** … Это **research finding** (controlled experiment), не documented real-world disaster». |
| reader P1-7 | Controllability operational | ✅ | Str. 54 «**Controllability** в стрелке keystone = **насколько среда поддаётся стандартизации и измерению**. L1 поле — солнце, дождь, патогены неконтролируемы; L5 retail — каждая SKU имеет цифровой след, обороты, цену, остаток». |
| reader P2-1 | DeLaval 99.8% attachment rate расшифрован | ✅ | Str. 103 + 212 «99.8% attachment rate = **то есть доильный аппарат успешно подсоединяется к вымени 998 раз из 1000**». |
| reader P2-4 | Plantix accuracy source explicit | ✅ | Str. 174 «Источник 85-90% accuracy — **self-reported Plantix** (Frontiers in Plant Science 2020 study на dataset images), **не independent field validation**». |
| reader P2-6 | Saga 20% UK = UV-C night, не harvest | ✅ | Str. 95 в tools list, str. 97 в anti-hype, str. 188 в working case, str. 384 в Misattribution — 4-fold redundancy ensures no cascade в downstream artifacts. |
| reader P2-3 | РСХБ format «заявлено, метрик нет» | ✅ | Str. 113, 253, 385 — consistent format. |
| reader P3 typos | berlapping → overlapping; Bra → Бренд; plodовощная → плодоовощная; urожайность → урожайность | ✅ | Все 4 typos исправлены (см. changes table str. 551). |

**Все reader-уровня issues — full fix.**

---

## Новые issues (после restructure)

### P0
**Нет.**

### P1
**Нет.**

### P2 (polish, не блокирующий)

#### P2-v2-1 — Р4 (10 мин) очень плотный с inline glossary block

**Где:** строки 230-255.

**Содержимое Р4:** Inline glossary 5 терминов (≥0.5 мин на чтение лектором) + 4 working cases (5 мин) + 2 failures (4 мин) + RU context (1 мин) ≈ **10.5 мин**. Pseudo-flow интегрирован в Cargill case (3 min из 5 working) — это разумный efficiency, но 5-step pseudo-flow требует ~1.5-2 мин explanation = budget для других 3 working cases (Tract + Olam + Walmart×Cropin) сокращается до ~1 мин на каждый.

**Это не P1** потому что: (а) Phase 5 designer / Phase 10 speech-writer могут implementировать glossary как side-bar slide (быстрая визуальная ссылка, не verbose explanation), (б) inline glossary терминов с английскими брендами (basis-points, hedge slippage) — short enough to skim in 30 sec total если лектор говорит «вот эти 5 терминов — смотрите справа на слайде», (в) 0.5 мин slack inside 10-min budget = acceptable margin для intermediate lecture с extensive jargon.

**Recommendation для Phase 5 (информационно):** designer должен сделать glossary как **single slide с боковой панелью / визуальной cheat-sheet** (не 5 separate slides), чтобы lecturer мог быстро пройти. Не требует plan-v3.

#### P2-v2-2 — Р3 12-мин budget немного оптимистичен

**Где:** строки 205-228.

**Math:** 4 working × 1.5 мин = 6 мин + F8 (2 мин) + F9 (1.5 мин) + RU context (часть включена в F9) + bridge к Р4 не явно ~0.5 мин = ~10-10.5 мин. План говорит 12 мин. 1.5-2 мин slack — может покрыть transitions / discussion pauses, что **хорошо**, но если speech-writer Phase 10 хочет добавить дополнительный context (например, breed-specific data для Holstein-bias), может вылезти.

**Это не P1** потому что: (а) slack — нормально для intermediate lecture с anti-hype heavy блоками, (б) Holstein-bias выделен как 3-я подсекция F8 (str. 220) — занимает explicit time, что план уже учитывает, (в) Q&A 10 мин full даёт runway для пересечения.

**Recommendation для Phase 5/10:** не сокращать Р3, использовать slack для smooth transitions; designer может add 1 transition slide (Р3→Р4 «от концентрированной экономики животноводства к высокому ROI цепочки поставок»).

---

## Counter-check results

### 1. Strict-in distribution (independent re-calc)

| Раздел | Минут content | Strict-in минут (independent) | % strict-in | Single-section >70%? |
|---|---|---|---|---|
| Р0 | 5 | 0 | 0% | — |
| Р1 | 14 | 9 (vertical 5 + ChatGPT 2 + Plantix 2) | 64% | нет |
| Р2 | 15 | 7.5 (Monarch 2.5 + FarmWise 2.5 + strawberry 2.5) | 50% | нет |
| Р3 | 12 | 3.5 (F8 2 + F9 1.5) | 29% | нет |
| Р4 | 10 | 4 (USDA 2 + Verra 2) | 40% | нет |
| Р4-bis | 8 | 8 (3+3+2 connectivity/lock-in/regulatory) | 100% | **dedicated failure section by design** — OK per план str. 315 «**это дизайн раздела** про среду как failure-перспективу; не "over-concentration", а сам по себе failure-themed раздел» |
| Р5 | 6 | 2 (5 критериев consolidation) | 33% | нет |
| Q&A | 10 | — | — | — |
| **TOTAL active** | **70** | **34** | **48.6%** | — |

**Plan self-report 48.6% подтверждается независимо.** Comfortable margin над ≥30% порогом.

**Distribution check без Р4-bis (Р1-Р5 = 64/50/29/40/33%):** **холистично распределено**, нет single-section over-concentration (антипаттерн из v1 critique устранён). Р4-bis 100% — это **корректный thematic design decision** (раздел про среду as failure perspective), не violation rule.

**Holistic across 3 артефактов (plan-level promise):** chapter ≥40% слов, slides ≥40% строевых, speech ≥30%. Plan commits — verify Phase 3/7/10.

**Owner waiver:** L10 ∈ L4-L17 → waiver НЕ доступен. Strict-in mandatory. **PASS.**

### 2. Keystone-axis ENFORCED

Str. 38-78:
- Keystone slide отдельный s02 ДО первого погружения ✓
- Заголовок «**Пять уровней лестницы. AI поднимается от поля к полке — и работает по-разному на каждом**» — про **саму ось**, НЕ устройство курса / защиту / recap ✓
- Каждый раздел = мотивированный подъём по оси (Р1→L1, …, Р4-bis→meta-уровень среды, Р5→L5) — explicit str. 70-78 ✓
- Closed-loop vs open-environment injection с **operational definition** (str. 56-60) — теперь явная, не жаргон ✓

**Нет regression от v1.** Bonus: P0-1 reader fix усиливает keystone clarity (closed-loop operationally defined).

### 3. Tools-per-taxonomy L4+ ENFORCED

| Уровень | Tools 2026 | Adoption | Anti-hype | Volatile→`[VFY-day-of]` | Infra отделена | Mode ≠ brand |
|---|---|---|---|---|---|---|
| L1 | 5 intl + 3 RU ✓ | растёт/стагнирует ✓ | бренд≠режим, US bias, lock-in ✓ | См. str. 91 ✓ | Satellite/GNSS отделены ✓ | ✓ |
| L2 | 8 intl + 3 RU ✓ | растёт в нишах ✓ | demo≠production, specialization, UV-C≠harvest ✓ | См. str. 99 ✓ | GNSS-jamming/FCC отделены ✓ | ✓ |
| L3 | 6 intl + 2 RU ✓ | растёт стабильно, Holstein-bias explicit ✓ | tie-stall/small dairy/breed bias ✓ | См. str. 107 ✓ | Camera/cloud/mobile отделены ✓ | ✓ |
| L4 | 6+ intl + 3 RU ✓ | лидирует ✓ | agentic=узкий, Tract data backbone, declared≠measured ✓ | См. str. 115 ✓ | Cloud/SAP отделены ✓ | ✓ |
| L5 | 5+ intl + 2 RU ✓ | очень высокое ✓ | не agriculture-specific ✓ | См. str. 123 ✓ | ERP/WMS отделены ✓ | ✓ |
| Infra | s35 отдельный | — | — | — | **Не AI capability** — отделено ✓ | — |

**Нет regression.** L4 inline glossary block (str. 234-239) — дополнительный value для intermediate-уровня curriculum.

### 4. Document size

598 строк / 600 limit = **PASS с 2-line маржой**. Document size mandate respected.

### 5. No regression check (Р4 сжат 12→10 мин, Р3 расширен 10→12 мин)

**Р4 (10 мин):** все 4 working cases + 2 failures + inline glossary помещаются плотно но реалистично (см. P2-v2-1 информационная нота выше). Pseudo-flow интегрирован в Cargill case efficiently. **Нет P1 regression** — content density acceptable для intermediate lecture.

**Р3 (12 мин):** дополнительные 2 мин distributed между Holstein-bias explicit + tie-stall barn + small dairy economics + architecture asymmetry для local пород РФ. Math немного оптимистичен (см. P2-v2-2) — slack 1.5 мин для transitions. **Нет regression.**

**Р4-bis (новый 8 мин):** содержит 3 sub-sections с balanced budgets (3+3+2). Нет density-bomb pattern из v1 Р5.

**Slide-budget превью str. 510:** «**Total ~33-36 слайдов** (+1-2 за счёт нового Р4-bis и pseudo-flow hedge); media-rich **22-24**». Section dividers увеличены до 7 (Р0-Р5 + Р4-bis) — math consistent.

### 6. Curriculum Relevance (per-section)

L10 = intermediate (Module 2). Все секции pass per Apply / Analyze Bloom levels:
- LO1a Remember + LO1b Apply — appropriate for intermediate ✓
- LO2 Apply (vendor-claim critical assessment) — appropriate ✓
- LO5 Analyze (≥5 critеria + alternatives) — appropriate ✓
- Нет forward-pointing concept-heavy material — pseudo-flow hedge остаётся overview-level ✓

### 7. Hook Engagement Quality (post-fix)

- **Hook B (Plenty Compton split-frame)** — time-evergreen (factual collapse) ✓; emotionally engaging (драматичный $940M loss, ribbon-cutting → закрытие 19 мес visual contrast) ✓; «висит на экране» worthy (split-frame visually rich) ✓; connected к keystone via L1 closed-environment попытка → AP1 термодинамика ✓; counter-example check vs Lec-9 pattern = symmetric (failure-first) ✓.
- **Hook C (Cognitive Pilot vs пыль)** — fallback documented ✓.

**Hook Engagement check — PASS.** v1 anti-pattern устранён.

### 8. Missing-Fundamentals (post-fix)

Все cornerstone concepts inline defined (str. 363-373). Foundation model + grounded reasoning brief ✓. RAG-grounded inline в AP4 alternative ✓. Edge ML/TinyML inline в AP5 ✓. Multi-agent framework inline в L4 working cases + pseudo-flow (str. 242) ✓. **No P1-level missing.**

### 9. Term Canonical-Validity

«Open-environment vs closed-loop AI» — insider phrasing, но план **явно** маркирует как «**наша рабочая формулировка для разделения сред — см. Cornerstone 2**» (str. 56, 368). Term Canonical-Validity check — **PASS** (rule allows insider phrasing when explicitly flagged).

«Sensor-fusion-AI на multi-GNSS» — descriptive не canonical, но research-04 R2 source терминология; план явно даёт parenthetic explanation «("Итэлма Квадро" — обработка сигналов нескольких созвездий + RTK + Kalman)» (str. 201, 337) — **adequate**.

### 10. Tools / Benchmark Freshness

Volatile markers `[VFY-day-of]` сохранены для всех 5 уровней (см. str. 91, 99, 107, 115, 123) — **нет regression**.

### 11. AI-Failure & Judgment Share (Universal ENFORCED)

**Strict-in: 48.6% (34/70 мин content)** — comfortable margin над 30%. Distribution **холистичен**: 5 разделов с failure-content (P1-9, P2-7.5, P3-3.5, P4-4, P5-2), плюс dedicated Р4-bis 8 мин. **Не single-cluster concentration** (Р4-bis 100% — design choice не bug). **Per CLAUDE.md ENFORCED — PASS plan-level.**

---

## Recommendation

**Phase 2 (chapter draft) — ГОТОВ К НАЧАЛУ.**

Все 6 P1 + 3 P0 + 5 P2 fix-issues применены полностью. Counter-checks pass. Document size 598/600. Никаких новых P0/P1 issues; 2 P2 polish noted информационно для Phase 5/10 designer/speech-writer awareness, не блокирующие.

**Phase 2 brief для book-editor должен включать:**
1. **Plan-v2 как canonical source** — следовать L1→L2→L3→L4→L4-bis→L5 outline без structural deviation.
2. **Closed-loop operational definition** (str. 56-60) — обязательно процитировать дословно при первом упоминании в chapter §0.
3. **Inline glossary 5 jargon terms** (str. 235-239) — каждый термин при первом упоминании в chapter §4 inline gloss, потом freely use.
4. **Misattribution warnings** (str. 379-385) — 5 пунктов как explicit «не делать в chapter».
5. **Strict-in target ≥40% слов** в chapter (verify Phase 3 holistically).
6. **Anonymization** — без ВУЗов / кафедр / городов; «студенты-инженеры 3 курса» (str. 472).
7. **Anti-anglicism mandate** + Russification таблица (str. 481-503) — глубокий latin-token scan на chapter Phase 3.

**Дополнительная methodology-critic re-run на chapter draft (Phase 3)** — рекомендуется проверить strict-in distribution в chapter (chapter-level может отличаться от plan-level из-за text expansion).

---

## Sign-off

Plan-v2 — **structurally sound, ready for Phase 2**.
