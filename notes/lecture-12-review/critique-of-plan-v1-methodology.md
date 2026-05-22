---
critique_of: notes/lecture-12-review/plan-v1.md
critic: methodology-critic
verdict: REVISE
created: 2026-05-21
---

# Summary

Plan v1 — методически крепкий черновик. Keystone-axis «лестница автономности L0→L3 + цифровой двойник как мост» предъявляется как несущая ось ДО первого погружения (Section 2 / s02), пронизывает §1–§5 в явных transitions, и логично замыкается на L3 humanoid в §8. Failure-share независимо пересчитан = 41–44% strict-in, размазано по 6 разделам — голистический критерий выполнен. Anti-overlap с Лекцией 11 в основном чистый, но **3 vendor/case дублируются без явной differentiation strategy** (Yokogawa FKDPP, Tesla 2018, ChatGPT-PLC failure) — это P1. Hero plan для s01/s39 проработан с 6-tier acquisition. Locked numbers convention есть, но 4 ключевых числа из research-dump не залочены в Section 11. Главные slabые места: (1) overlap-risk с lec-11 без explicit anti-duplication strategy, (2) L0/L1/L2 раздели по 10 минут — heuristic-tight для глубокой failure-bucket дискуссии + evidence + transition, (3) ось «лестница автономности» нуждается в *явном различении* от ISA-95 L0–L2 (упомянутого в lec-11 §5.3), иначе студент запутается между двумя «уровнями».

# P0 issues (blocking)

(нет)

# P1 issues (high-priority)

## P1-1. Anti-overlap с Лекцией 11 — 3 кейса дублируются без explicit differentiation strategy

**Issue.** Plan v1 переиспользует три ключевых случая из lec-11 без явного объяснения «какая новая грань добавляется в lec-12»:

1. **Yokogawa FKDPP + JSR 35 дней** — lec-11 chapter-part2.md §3.2 даёт **детальный разбор** (FKDPP — Factorial Kernel Dynamic Policy Programming, NAIST 2018, off-policy RL с факториальной ядровой декомпозицией, премия премьер-министра Японии 2023, ~5–10 коммерческих развёртываний). Plan v1 §4 описывает это как «flagship case L2» (s20) и `Yokogawa press release` для hero — это **дублирование**, не **новая грань**.
2. **Tesla 2018 over-automation + Musk «humans are underrated»** — lec-11 §2.4 (chapter-part2.md) — **полный canonical case** с тремя точками провала (fluffer, conveyor network, battery assembly) и IMD-анализом. Plan v1 §5 (s25) восстанавливает Tesla 2018 как «intro к разделу 10 критериев» — рискует **дублировать lec-11 §2.4 narrative** дословно.
3. **ChatGPT-PLC generic failure + purpose-built + engineer-in-loop** — lec-11 chapter-part2.md упомянул *foundation models дополняют, не замещают* (§1.2 trio failures: GE Predix / Watson Health / Foxconn). Plan v1 §3 даёт это как central failure case. Не дублирует buctevenne, но риск — что студент уже видел этот шаблон.

**Evidence.** Lec-11 §5.3 «Мост к Лекции 12» (chapter-part3.md:297) явно говорит: «здесь мы остановимся — это другая лекция»; lec-12 должна **добавить новую грань**, а не повторять. Например: Yokogawa FKDPP в lec-11 = «первый прецедент production RL»; в lec-12 — «*как digital twin был использован Yokogawa для подготовки FKDPP sim-to-real transfer*» (это новая грань). Tesla 2018 в lec-11 = «канонический provider over-automation»; в lec-12 — **этого hero лучше избежать** в §5 (alternative: использовать Southeast Asian Port или fresh 2024–2026 failure case как intro к §5).

**Recommendation:**
- **Yokogawa FKDPP — переориентировать угол.** В §4 (L2) добавить explicit differentiation: «Lec-11 разобрала FKDPP как алгоритмический breakthrough; lec-12 разбирает *архитектурный механизм* — как digital twin (NVIDIA Omniverse / Siemens Composer) служит safe sandbox для RL обучения ДО переноса на JSR-style hardware». Якорь: «без twin — слепая вера; FKDPP получился потому, что Yokogawa имела внутреннюю симуляцию колонны как twin». См. research-dump §5.8 «sim-to-real gap».
- **Tesla 2018 — заменить на свежее.** §5 intro hero не должен быть Tesla 2018 (студент видел в lec-11). Alternatives: (a) **Southeast Asian Port $12M digital twin (2024)** — уже в research-dump §5.2, **direct relevance** к keystone twin; (b) **Foxconn Wisconsin** (упомянут в lec-11, но как *trio failures*, не как deep case) — можно углубить как «over-promised manufacturing AI»; (c) Tesla 2024 GigaCast отступление (lec-11 chapter.md «две отмены Tesla» — это **lec-11 specific framing**).
- **ChatGPT-PLC** — оставить, но добавить explicit cross-reference: «в lec-11 §1.2 обсуждали foundation models как complement; здесь — *конкретный negative case* и *purpose-built альтернатива*». Это OK, потому что lec-11 не вошла глубоко в PLC code generation.

## P1-2. ISA-95 L0–L2 vs «Лестница автономности L0–L3» — riskdouble-meaning

**Issue.** Lec-11 §5.3 (Мост к Лекции 12) ссылается на «ISA-95 уровни L0–L2» как архитектурную модель связи sensor → controller → SCADA. Plan v1 keystone «Лестница автономности AI L0→L3» использует **те же буквенные коды L0/L1/L2/L3** для совершенно другой концепции (уровень доверия к AI). Студент 3 курса, прошедший lec-11, будет **спутывать** две оси.

**Evidence.** Lec-11 chapter-part3.md:305: «На уровнях L0–L2 ISA-95 цифровой двойник связывает данные датчиков с физическим оборудованием». Plan v1 keystone §2: «L0 (наблюдать) → L1 (советовать) → L2 (замыкать петлю) → L3 (действовать автономно)». **Один и тот же символ — разные семантики.**

**Recommendation:** В Section 2 keystone (и на s02 visible slide):
1. **Explicit разделение в первой же строке:** «Это **другие** L0–L2, чем ISA-95 в lec-11. ISA-95 — *слои архитектуры* (поле → контроллер → SCADA → MES); здесь — *степени автономии AI* (наблюдать → советовать → замыкать петлю → автономно)».
2. Альтернатива: **переименовать ось**. Варианты: «Степени делегирования AI» (S0–S3), «Уровни автономии AI» (A0–A3), «Шкала AI-Doверия» (T0–T3). Это убрало бы коллизию полностью. **Default recommendation:** переименовать в **A0–A3 (Autonomy levels)** — соответствует широко используемому SAE J3016 для self-driving + ISO 22989 для AI autonomy levels.

## P1-3. §2/§3/§4 — 10 минут на ступень heuristic-tight для assertion + 4 mini-failure-bucket + transition

**Issue.** §2 (L0) даёт 10 минут на: assertion + 5 evidence claims (Indus Vision 99%+/0.1-2% FP, Deloitte 10:1, cement plant 57x, chemical $2M, automotive -30%/+40%) + 4-минутный failure bucket (FP cascade + vision границы + metrology + rare events) + transition. Это **~2 минуты на каждый smajor evidence point** при условии что 4 мин — failure-bucket. **Cognitive load risk:** студент не успеет интернализировать.

**Evidence.** Mayer multimedia learning — coherence principle: 5+ новых evidence points за 5 минут = overload. Plan v1 §2 (s10–s14) — 5 слайдов / 10 минут = 2 мин/слайд, что укладывается в presentation pacing baseline, но **content density** в самих слайдах высокая: s11 cost-of-FP chart + s13 Deloitte 4-row breakdown table + s14 2-col vector — это 3 «think-hard» слайда подряд.

**Recommendation:**
- Расширить §2 до **11–12 минут** за счёт сжатия §6 (8 → 6–7 мин) — §6 архитектура OT/IT сейчас имеет 4 слайда (s31–s34), можно ужать до 3.
- **Альтернатива:** убрать 1–2 evidence points из §2 (например, automotive -30%/+40% — это duplicate ROI metric с cement plant 57x); сохранить только cement + chemical.
- **Decision matrix для plan v2:** owner choice — extend §2/3/4 by 1 min each = +3 min total, compensate с §6 ±2 + §1 ±1.

## P1-4. Locked numbers list incomplete

**Issue.** Plan v1 Section «Carry-forward» (line 579) locks 14 numbers, но **research-dump §10 ключевые цифры для slides cross-reference чеклист** содержит 15 пунктов. Пропущены / разойдутся между плана и chapter:
- **AI manufacturing market 2030 = $155.04B (CAGR 35.3% 2026–2030)** — research-dump §1 строка 19, **отсутствует в plan locked-numbers**. Если book-editor включит в chapter (а это релевантно для §1 «рынок twin внутри big market AI»), а speech-writer не знает — drift risk.
- **OPC UA + MQTT industrial AI market 2026 = $17.15B** (research-dump §1 строка 21) — отсутствует.
- **PdM программа: инвестиции $200K–$600K, экономия $1.2M–$3.5M, окупаемость 18–36 месяцев** (research-dump §3) — частично есть («10:1 ROI»), но конкретные тики НЕ locked.
- **Tesla 2018: 10% от 5K Model 3/week target** — research-dump §10, plan upоминает только «excessive automation», но точное число не locked.

**Recommendation.** В carry-forward instructions для Phase 2 (book-editor) добавить (после строки 579):
```
- AI manufacturing market 2030 = $155.04 миллиарда (CAGR 35.3%) — research-dump §1.
- OPC UA+MQTT industrial AI market 2026 = $17.15 миллиарда — research-dump §1.
- PdM программа: инвестиции $200K–$600K → экономия $1.2M–$3.5M → окупаемость 18–36 месяцев — research-dump §3.
- Tesla 2018: ~10% от 5K Model 3/week target к концу месяца (200/2000 от 2500 target = ~ratio).
```
И в Section 10 add: «**Numbers lock-list = research-dump §10 + 4 additions выше. Fact-checker верифицирует.**»

## P1-5. §1 Architecture-of-twin — 4-слойная модель не различает «cyber twin» vs «physical twin» vs «digital shadow»

**Issue.** Plan v1 §1 evidence (s06 «архитектура 4 слоёв twin»: physical asset → IIoT sensors → digital model → AI consumers) — это упрощение, опасное для introductory framing. Стандартная литература различает:
- **Digital Model** (модель без живого data feed);
- **Digital Shadow** (одностороннее обновление model ← physical, but no control back);
- **Digital Twin** (двустороннее: model ↔ physical, can simulate control actions back).

**Evidence.** Это — каноническая taxonomy (Kritzinger et al. 2018 «Digital Twin in manufacturing: A categorical literature review»). Не упомянуто в research-dump, но обязано быть в chapter §1, потому что § 1 assertion = «twin — это не CAD, а 4-слойная архитектура» — без этой taxonomy студент не поймёт, **что именно отличает twin от mere CAD-картинки**.

**Recommendation.** В §1 добавить mini-таблицу (можно on s06 vector diagram side):

| Тип | Live data flow | Управляющее действие назад? | Пример |
|---|---|---|---|
| Digital Model | – | – | CAD-чертёж |
| Digital Shadow | physical → digital | – | Monitoring dashboard |
| **Digital Twin** | physical ↔ digital | ✓ (simulate + apply) | Siemens Composer |

И в plan §1 evidence добавить bullet «Kritzinger 2018 taxonomy — 3 уровня; в этой лекции мы говорим о *true digital twin* (двусторонняя петля)».

## P1-6. §7 Российский контекст — отсутствует Lec-11 carry-forward (Норникель flotation + ГОСТ Р 57700.37-2021)

**Issue.** Plan v1 §7 содержит КАМАЗ + Росатом + T-FLEX + АтомМайнд (4 примера). Lec-11 §3.5 «Российский контекст: что публично проверяемо» уже дал **Норникель flotation/измельчение AI** + **ГОСТ Р 57700.37-2021 Цифровые двойники** (lec-11 chapter-part3.md:586). Plan v1 не упоминает ни Норникель ни ГОСТ.

- **Норникель flotation** — релевантно для §7 как process-control case в РФ; синергия с §4 (L2 closed-loop).
- **ГОСТ Р 57700.37-2021 «Цифровые двойники»** — релевантно для всего §1 (что есть twin) и §7 (регуляторика РФ). Это **state-level definition** в РФ — обязано быть упомянуто в lec-12 «цифровые двойники».

**Recommendation.** В §7 evidence добавить:
- «**ГОСТ Р 57700.37-2021 "Цифровые двойники"** — формальная регуляторная база РФ для digital twin (carry-forward от lec-11 §3.5). Lec-12 §1 chapter должна **процитировать определение из ГОСТа** для исключения term drift с международной taxonomy».
- «**Норникель flotation + измельчение AI (carry-forward lec-11 §3.5)** — российский process-control case L2 type (синергия с Yokogawa FKDPP в §4)».

В Section 10 open question #2 уже флагнуто «может добавить Норникель» — превратить в **mandatory carry-forward**, не optional.

## P1-7. L3 humanoid pre-section content vs §0 mention vs §8 closing — fragmentation

**Issue.** Plan v1 распыляет «L3 humanoid» по 3 точкам:
- §0/s02 keystone table — упоминание «Toyota Digit + BMW Leipzig» как L3 example;
- §5 (косвенно, в Tesla Optimus 2024 hardware-soft gap — failure-bucket entry #10);
- §8 (s39 closing hero = Toyota Digit);

И НЕ имеет **dedicated 2-3 минутного раздела** про L3 (Section 10 open question #1 default = «кратко»). Но keystone-axis ось включает L3 как **highest rung**. Если L3 — только namedrop без content depth, ось ощущается **incomplete**.

**Evidence.** L0 / L1 / L2 получают по 10 минут (§§2, 3, 4); L3 — 0 минут direct. Это структурная asymmetry — четыре ступени, но только три раскрыты. Хотя L3 в 2026 = единичные кейсы, что-то про **критерии** «когда L3 запрещён» (то же что §5 даёт для general AI) на 2-3 минуты обязано быть для balance.

**Recommendation.**
- **Опция A (рекомендуется):** добавить **§4.5 «L3 — единичные кейсы и почему ось обрывается на L2 для 95% производства» (2 мин)** между §4 и §5. Content: Toyota Digit RAV4 + BMW Leipzig pilot как **существующие L3 кейсы**; объяснение «почему остальные не L3» (regulatory + cost + complexity). Бюджет: компенсировать сжатием §6 (8 → 6 мин).
- **Опция B:** расширить §0/s02 keystone descriptive до 1 мин больше, дать L3 описание с **именами Toyota Digit / BMW Leipzig + 1-line «почему mostly единично»** там; не делать dedicated section. Бюджет: 0.
- **Опция C (default per Section 10):** оставить как есть, **но в §0 keystone указать явно «L3 в 2026 = единицы кейсов, основная масса L0–L2»**, чтобы ось чувствовалась осознанно асимметричной.

# P2 issues (polish)

## P2-1. Hero для s07 (Siemens Digital Twin Composer) — fallback strategy недостаточен

Plan §1 line 158: «s07: Tier 1 press.siemens.com news release "Siemens unveils Digital Twin Composer at CES 2026". Tier 2: news.siemens.com.»

Только 2 tier. Если press.siemens.com paywall'нут или blokирует hot-link — нет Tier 3-6. Расширить до full 6-tier list (Wikimedia → press kit → YouTube CES 2026 thumb → Wayback → Google Images). Pattern matched с s01/s39 (6-tier explicit).

## P2-2. s05 «3D-картинка ≠ twin» сравнительный композит — risk нечестной картинки

Plan line 156: «s05: composite split-screen. Source: comparison composite». Это **mock-fallback** в дисguise — composite из двух Tier-6 images = synthetic. Recommend: **single real screenshot of bad twin demo** (Tier 1: any vendor's CES booth thumb где видно «marketing 3D без data», например Bentley iTwin презентационный slide) **рядом с** реальным Composer UI (s07).

Альтернатива: **сделать s05 vector diagram «4 layers required» вместо composite** — это методически чище (показывает что нужно), чем сравнение «плохой twin vs хороший twin» (требует найти явный «плохой» twin demo).

## P2-3. Section 6 «Russification таблица» — пропущены 8 anglicism patterns

Plan Section 8 таблица содержит 12 ключевых терминов. Из критических не русифицировано:

- `cascade` (упомянуто 9 раз в plan, не в таблице) → «каскад срабатываний»
- `rollback` → есть «откат» — OK;
- `gap` → «разрыв» в таблице «sim-to-real gap», но `expectation gap` не;
- `data layer audit` → «аудит слоя данных»;
- `worked example` → «проработанный пример» (carry-forward lec-11);
- `closed-loop optimization` → «оптимизация с замкнутой петлёй»;
- `safety envelope` → есть, OK;
- `time scrubbing` → «прокрутка времени» (есть);
- `hero` / `cover` / `roadmap` — meta-tokens, не lecture-body, OK.

Add 4 missing: cascade, expectation gap, data layer audit, worked example.

## P2-4. Bridge text на s39 — formulation drift с research-dump terminology

Plan line 425: «Лекция 13 — от внутрицеховой логистики к цепочке поставок и транспорту». Lec-11 §5.3 (chapter-part3.md:314): «Лекция 13 — AI в цепочках поставок (AI вне завода). Логистика, прогноз спроса, оптимизация со стороны поставщиков».

Drift: lec-11 framing = «AI в цепочках поставок»; plan v1 framing = «логистика и транспорт». Need lock single phrasing — recommend «AI в логистике, цепях поставок и транспорте» (covers оба).

## P2-5. §0 keystone slide table — нагружена

Table в Section 2 keystone (lines 63–68) содержит 5 столбцов: Уровень / Название / Что делает / Кто решает / Пример 2026. На rendered s02 это **5-column table** — visual density risk. Recommend: либо 4 столбца (merge «название» в «уровень: название»), либо использовать **vector diagram of ladder** с 4 steps + side legend (presentation-designer выбирает).

## P2-6. §8 closing — отсутствует Q&A backup mention

Plan v1 Section 10 open question #6 «делать ли Q&A backup аналогично lec-11» — default «да». Это должно быть **carry-forward instruction для Phase 2 chapter expansion**, явно записано в Section 11 «Carry-forward» (line 579). Сейчас не упомянуто.

# Strengths (что хорошо)

- **Keystone-axis формулировка эталонная.** Лестница автономности явно предъявлена в Section 2 ДО первого погружения (Раздел 0/s02), 5 пунктов обоснования, transitions к §1–§4 явно ссылаются на ось.
- **Failure-share calculation transparent.** Section 3 minute-budget table + per-section breakdown + cumulative 33/75 = 44%. Independent recalculation подтвердил 41–44% strict-in range. Размазано по 6 разделам.
- **Anonymization rigorous.** Section 8 ENFORCED: 0 named institutions, generic career framing, lec-06/07 эталон pattern.
- **Hero plan для s01/s39 — 6-tier acquisition strategies явно расписаны** с identifiable Tier-1 URLs (blogs.nvidia.com / press.siemens.com / agilityrobotics.com / toyota.com newsroom).
- **Media plan ≥50% explicit per-slide breakdown** (Section 7 — 14 real-image + 6 chart = 20/33 = 61%).
- **Connection to keystone explicit per section.** Каждый § раздел имеет «Keystone connection + transition к §X+1» phrase — это эталон pattern для lecture-outline templates.
- **Failure inventory ≥10 cases + ≥10 alternatives** — Section 5 имеет structured matrix (case → where in lecture → lesson) + (criterion → alternative → rationale).
- **Russification carry-forward в Section 8** даёт concrete anti-anglicism table для downstream.
- **Cross-link к research-dump explicit** — каждое measurable claim attributed.
- **Frontmatter clean** (`audience` locked, no named institutions, target ≥30k слов записан, hero plan записан).
- **L1 / L2 / L3 examples concrete для 2026** (Toyota Digit / BMW Leipzig / Yokogawa FKDPP / PLC Copilot / Indus Vision), не abstract.

# Specific recommendations

**Priority order (top-7 для plan v2):**

1. **P1-1** Anti-overlap strategy: переориентировать Yokogawa FKDPP angle (twin-as-RL-sandbox); заменить Tesla 2018 hero на Southeast Asian Port или fresh 2024–2026 failure для §5 intro; cross-reference lec-11 ChatGPT-PLC line.
2. **P1-2** L0–L2 collision: rename axis на A0–A3 (Autonomy levels, SAE J3016 + ISO 22989 anchor) OR add explicit «не путать с ISA-95» disclaimer в s02 keystone.
3. **P1-5** Twin taxonomy: добавить Kritzinger 2018 3-уровневую классификацию (Model / Shadow / Twin) в §1 evidence.
4. **P1-6** РФ context: ГОСТ Р 57700.37-2021 + Норникель flotation carry-forward от lec-11 → §7 mandatory, не optional.
5. **P1-7** L3 dedicated 2 min sub-section (§4.5) ИЛИ explicit «mostly L0–L2» disclaimer на s02 keystone.
6. **P1-4** Locked numbers — добавить 4 missing ($155B AI mfg market, $17.15B OPC UA market, PdM $200K–$600K + $1.2M–$3.5M + 18–36 мес, Tesla ~10% target).
7. **P1-3** Pacing: +1 мин в §2/§3/§4 каждый за счёт сжатия §6 (8→6) — или sokraт evidence в §2 (drop automotive, оставить cement+chemical).

**Cross-cutting:**
- В Section 11 carry-forward для Phase 2 (book-editor) explicit instruction: «Chapter §1 — обязательно Kritzinger 2018 taxonomy + ГОСТ Р 57700.37-2021 definition». 
- В carry-forward для Phase 5–6 (designer): «s02 keystone — vector diagram of ladder (НЕ 5-col table) для visual coherence».
- Add Section 11 instruction для Phase 9 (speech-writer): «Q&A backup 12–14 questions per lec-11 эталон — finalize в Phase 9».

# Self-checks

- [x] **Failure-share independently recalculated:** 33 мин / 75 = 44% (план claim) — re-verified bottom-up по minute-budget table. Strict re-evaluation (excluding §6 partial) = 31/75 = 41.3%. Both above 30% threshold. ✓ Distribution: §1 (4), §2 (4), §3 (4), §4 (4), §5 (15), §6 (2) — размазано по 6 разделам, **не сконцентрировано в одном** (holistic check pass). ✓
- [x] **Deep latin-token scan:** 753 unique non-allowlist tokens; top 40 — преимущественно meta-tokens (Tier, hero, plan, lec-, com, real-image, attribution) и domain English (twin, vision, edge, cascade, plant, control). **Narrative-critical anglicisms (cascade=9, audit=10, gap=15, in-loop=8, sim-to-real=8, expectation gap=5, data layer=4+5, safety envelope=5)** должны быть Russified в downstream. Plan Section 8 русифицирует ~12 ключевых; **4 missing** (cascade / expectation gap / data layer audit / worked example) — flagged как P2-3. **Plan-internal: acceptable** (meta-tokens OK, doman acronyms OK).
- [x] **Anti-overlap check vs lec-11:** **Risk medium.** 3 vendor/case дублируются без explicit differentiation (Yokogawa FKDPP, Tesla 2018, ChatGPT-PLC). P1-1 detailed. Bridge text на s39 имеет terminology drift с lec-11 §5.3 (P2-4).
- [x] **Anonymization:** **0 named institutions verified** (grep'нул plan — no «МГТУ» / «Бауман» / «ИУ» / «ВКА» / «МАИ» / «СПбГУ» / «bauman» / «vka»). ✓
- [x] **Hero plan check:** **s01 PASS** — 6-tier acquisition (blogs.nvidia.com → Wikimedia → news.siemens.com → YouTube → Wayback → Google Images), attribution explicit, ≥40% mandate noted. **s39 PASS** — 6-tier (agilityrobotics.com → Wikimedia → Toyota newsroom → Reuters YouTube → Wayback → Google Images), attribution explicit. **s07 FAIL** — только 2 tier (P2-1).
- [x] **L4+ Chapter Depth Baseline:** target 30 000 слов записан в frontmatter (line 14) + carry-forward instruction для book-editor (line 577). ✓
- [x] **Keystone-axis structural check:** **PASS** — ось предъявлена в Section 2 как dedicated keystone-слайд (s02 ДО §1), заголовок «Лестница автономности AI в производстве», 4-step diagram + bridge label «Цифровой двойник — мост». Pre-USER-GATE check point 6 satisfied. ⚠️ caveat — L0–L2 collision с ISA-95 (P1-2).
- [x] **Cross-reference research-dump:** 14 of 15 numbers from research-dump §10 echoed в plan locked-numbers. **1 missing**: $155.04B AI manufacturing market 2030. **3 sub-locks missing**: $17.15B OPC UA market, PdM ranges, Tesla 10%. (P1-4)
- [x] **No designer-extras в plan body:** 0 hits для `[VERIFY-DAY-OF]` / `Лектору` / `Вы здесь` / timing markers / `LO[1-9]` codes / `§\d` cross-refs visible — все Lo-codes в frontmatter only.

---

**Verdict justification (counter-check applied, ENFORCED).** 7 P1 issues > 4 threshold. Per critic Verdict Rule «если ≥5 P1 issues но verdict = APPROVE-WITH-POLISH — STOP, change to REVISE» — **verdict locked at REVISE**, не APPROVE-WITH-POLISH. Initial draft had APPROVE-WITH-POLISH based on argument «3 P1 — strategic, 4 — concrete edits, polish-able» — это override запрещён explicit ENFORCED rule.

**What plan v2 must address (mandatory before Phase 2 chapter draft):**

1. **P1-1 Anti-overlap** — orchestrator/owner decision: переориентировать Yokogawa angle (twin-as-sandbox), заменить Tesla 2018 hero на fresh failure case, cross-reference ChatGPT-PLC. Re-spawn plan if owner chooses defer to chapter.
2. **P1-2 L0–L2 collision** — rename axis (A0–A3 default per SAE J3016 + ISO 22989) OR explicit «не ISA-95» disclaimer на s02. **Не оставлять резолюцию на chapter expansion.**
3. **P1-3 Pacing** — concrete: +1 min к §2/3/4 каждый за счёт сжатия §6, ИЛИ drop redundant evidence.
4. **P1-4 Locked numbers** — concrete: add 4 missing к carry-forward.
5. **P1-5 Twin taxonomy** — concrete: добавить Kritzinger 2018 mini-table в §1 evidence.
6. **P1-6 РФ context** — concrete: добавить ГОСТ Р 57700.37-2021 + Норникель flotation carry-forward в §7.
7. **P1-7 L3 dedicated content** — owner choice: dedicated 2-min §4.5 ИЛИ explicit disclaimer на s02. Не оставлять fragmented across 3 mentions.

**Path to APPROVE-CLEAN:** plan v2 addresses P1-3/4/5/6 (concrete edits, easy) + owner-decision на P1-1/2/7 (strategic, requires 5-10 min thought). Re-spawn methodology-critic для verification → expect APPROVE-CLEAN if все 7 closed.
