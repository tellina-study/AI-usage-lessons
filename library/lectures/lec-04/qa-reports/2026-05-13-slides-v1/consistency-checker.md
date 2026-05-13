# Consistency Check — Chapter v2 ↔ Slides v1 — Лекция 4

**Date:** 2026-05-13
**Phase:** 7 — после Slides v1 рендера (commit `aa4567d`); chapter v2 финализирован (commit `5c4b06c`).
**Mode:** `chapter+slides` (speech не существует — пропущено).
**Artifacts reviewed:**

- `library/lectures/lec-04/chapter.md` (722 строки, ~12,692 слов, status=reviewed).
- `library/lectures/lec-04/deck.yaml` (412 строк, 29 slides — `s01–s24`, `s26–s29`; `s25` отсутствует — merged в s18 на этапе плана v2).
- `library/lectures/lec-04/slides/*.md` (29 файлов, 1,199 строк суммарно).
- `library/lectures/lec-04/rendered/snapshots/*.png` (29 файлов — vision только в случае needed, structural focus здесь).
- `notes/lecture-4-review/plan-v2.md` (1,513 строк, post-USER-GATE 0 reference).

**Verdict:** **REVISE**

**Обоснование verdict'а.** Найдено **1 P0**, **6 P1** и **9 P2** discrepancies. P0 — терминологический разрыв с собственным glossary chapter'а («medical AI» декларирован как запрещённый синоним для `AI-диагностика` в #1 glossary, но при этом используется и в chapter, и в slides 25+ раз; это блокирующий вопрос — chapter сам себе противоречит, slides воспроизводят разрыв). Без этого fix terminology lock после Phase 4 USER GATE остаётся нерабочим. Остальные P1 — частичные mismatches цифр (CheXNet 0.96/0.93 vs 0.94–0.96/0.89–0.93), LO mapping расхождения между deck.yaml и slide frontmatter, frame mapping inconsistency у s11. Counter-check: ≥5 P1 issues — verdict не может быть APPROVE-WITH-POLISH, в соответствии с обновлённым CLAUDE.md правилом.

---

## Severity counts

| Severity | Count |
|---|---|
| **P0** (factual contradiction / coverage gap / glossary lock breach) | 1 |
| **P1** (significant drift, требует sync до user gate) | 6 |
| **P2** (minor inconsistency, можно зафиксировать в polish round) | 9 |

---

## Number consistency matrix

| Claim | Chapter (lines) | Slides | Match? |
|---|---|---|---|
| **FDA 1 451 cumulative end-2025** | §intro L86, §0.2 L110, §1.2 L162, §1.2 L164, §1.2 L170, §3.5 L392, §6.1 L566 | s04 (L5, L30, L34), s07 (L5, L13, L20, L28, L32), s26 (L31) — все `1 451` / `1,451` | **✓** consistent |
| **mosmed 14M+ исследований, 74 региона, 70 сервисов, 18M изображений, 11 стандартов, 300 датасетов, 2000+ медорг.** | §0.2 L112, §1.2 L166, §2.4 L271–279 | s04 (L40 — все 7 чисел), s12 (L33, L39, L41), s08 (L32 — частичный set 14M/74 регионов/70 сервисов), s14 callback (L31 — 14M+/74) | **✓** consistent (mosmed.ai operational metrics aligned) |
| **mosmed: «4 млрд руб/год» — запрещённое число** | §1.2 L168 — explicit отказ от цифры | **0 mentions в slides** | **✓** correctly excluded |
| **Rentosertib: +98.4 mL FVC vs −20.3 mL placebo, n=71, 21 China sites, 12 weeks, 60 mg QD** | §3.3 L352 (полный set с CI) | s17a (L13, L32, L38 — все ключевые числа: +98.4, −20.3, n=71, 21 China, 12 weeks, 60 mg) | **✓** consistent |
| **AlphaFold 200M+ structures; AlphaProteo 88% BHRF1; 3–300× affinity; AlphaFold 3 +50% PoseBusters; Нобель 2024** | §3.2 L340, L342, L344; §6.1 L568; glossary L607 | s16 (L13, L30, L34, L42, L44), s26 (L31 — Нобель 2024) | **✓** consistent |
| **MASAI 80.5% vs 73.8%, 6.4 vs 5.0/1000, 44% workload, 12% interval cancer, spec 98.5%** | §intro L86, §2.3 L245–247, L250; §6.1 L566 | s11 (L13, L33, L41 — все числа), s26 (L31 — 44% workload в card) | **✓** consistent |
| **Obermeyer: 17.7% → 46.5%, 26% chronic illness, 84% bias reduction, ~200M Americans, $1 800/year** | §5.2 L456, L458, L462, L466; §self-check L553 | s21 (L13, L28, L32) — full set | **✓** consistent |
| **Goh JAMA: n=50, median 76% vs 74%, p=0.60** | §2.3 L252 — точное число «76%»/«74%», n=50, p=0.60 | s11 (L33 — «GPT-4 alone 76.3% vs doctor+GPT-4 73.7%», speech L43 — «семьдесят шесть/семьдесят четыре») | **⚠ P1** (s11 visual карточка использует 76.3 / 73.7 — это десятичные дроби, которых в chapter нет; chapter говорит просто «76%» и «74%». Хотя 76.3/73.7 могут быть точнее, они в chapter не verifiable. **Recommendation:** или sync slide visual к «76%/74%», или добавить «76.3/73.7» в chapter с источником.) |
| **Change Healthcare: 190M Americans (≈57% US pop), $2.457B, 6 TB, $22M ransom, multi-week, ALPHV/BlackCat, Feb 21 2024** | §5.4 L500, L504–508 | s23 (L5, L13, L29, L33, L39) — full set | **✓** consistent |
| **DSP-1181: Jan 2020 entry → 2022 discontinued, ~12 месяцев design, 4–5 лет traditional, OCD target** | §3.4 L374, L376, L378 | s17b (L29, L32, L39, L41) — full set | **✓** consistent |
| **AI ускоряет stages 1–3 с 4–5 лет до 12–18 месяцев** | §3.1 L334 | s15 (L41) — sync с «двенадцати-восемнадцати месяцев» | **✓** consistent |
| **Drug discovery: 10–15 лет, $1–2B, ~6.7% Phase 1→approval** | §3.1 L313; glossary L601 | s15 (L5, L29, L33, L37) | **✓** consistent |
| **PCCP финальная гайданс 4 декабря 2024 + 12–18 месяцев old submission** | §intro L86, §3.5 L398; glossary L609 | s18 (L33 — «4 декабря 2024»; L39 — «двенадцать–восемнадцать месяцев»; L41 — Aug 2026/2027 dates) | **✓** consistent |
| **EU AI Act 2 августа 2026 (Annex III high-risk) / 2 августа 2027 (MDR)** | §intro L86, §1.3 L182, §3.5 L393, L400 | s08 (L42 — «2 августа 2026 … через два с половиной месяца»), s18 (L33 — gold highlight + L41) | **✓** consistent |
| **РФ: 57 registered AI medical devices (52 RU + 5 foreign), Expedited procedure 1 марта 2025 (ПП РФ № 1684), Webiomed 3 апреля 2020** | §intro L86, §3.5 L394 | s18 (L33, L43) | **✓** consistent |
| **ФЗ-23 data localization — 1 июля 2025** | §intro L86, §5.4 L517; glossary L615 | s18 (L43), s23 (L33, L43) | **✓** consistent |
| **CheXNet sens/spec для pneumonia subset** | §2.2 L229 — «sens ≈ 0.94–0.96, spec ≈ 0.89–0.93 в зависимости от cut», L231 — «sens=0.94, spec=0.89 (более скромные числа для усреднённой ситуации)» | s10 (L13, L18, L20, L32, L42) — visual использует «sens 0.96, spec 0.93», speech (L42) использует «sens 0.94–0.96 и spec 0.89–0.93»; PPV examples (8% prev 1%, 78% prev 30%) — consistent | **⚠ P1** (s10 visual карточка показывает «CheXNet sens 0.96, spec 0.93» как **headline**, но chapter L229 эксплицитно предупреждает, что это **«не headline metric»**, а зависит от threshold. Chapter PPV-расчёт сделан на sens=0.94/spec=0.89. Visual presents «лучшие» числа из диапазона как точку — chapter явно их не приводит как single operating point.) |
| **Cognitive Agro Pilot 1500+ машин, +30–40% эффективности** | §6.2 L578 | s28 (L13, L32, L38) | **✓** consistent |
| **AlphaProteo Sep 2024 + AlphaFold 3 Nature May 2024 (8 мая)** | §3.2 L342, L344 | s16 (L34, L42, L44) | **✓** consistent |
| **Tessa: March 2023 (Cass switch к generative) + 30 мая 2023 (Sharon Maxwell screenshots) + 24h suspend** | §5.3 L477, L478 | s22 (L34, L40) | **✓** consistent |
| **Adversarial hallucination 83% (Communications Medicine 2025, 6 LLMs, 300 vignettes)** | §5.3 L484 | s22 (L34, L42) | **✓** consistent |
| **40M Americans use ChatGPT for healthcare** | §5.3 L488 | s22 (L34, L44) | **✓** consistent |
| **Obermeyer Science 366, 447–453 (2019), DOI 10.1126/science.aax2342** | §5.2 L454; refs L699 | s21 (L20, L32, L36 — speech) | **✓** consistent |

**Сводно:** числа крепко synced. P1 wobbles — только в CheXNet (s10 visual headline picks «лучшие» числа диапазона, противоречит chapter методическому комментарию) и Goh (s11 visual использует 76.3/73.7, chapter — 76/74).

---

## Terminology drift

### D1 — «medical AI» canonical lock breach (P0)

**Severity:** P0

**Where:** glossary chapter §entry #1 (L600) vs весь chapter + slides.

**Issue.** Chapter glossary entry #1 явно декларирует:

> **AI-диагностика** … Запрещённые синонимы: «medical AI» (слишком широко).

Однако и chapter, и slides последовательно используют именно «medical AI» / «медицинский AI» как universal label для всей категории medical-AI вообще (не как синоним AI-диагностики). В chapter — 25 mentions; в slides — 18+ mentions (s01 learning_goal, s08 speaker notes L36/L40, s10 learning_goal, s18 visible content L37 + L39 + L41, s20 speech L38, s21 speaker note L36, s22 assertion L5/30 + speech L38, s23 speech L33/41/43, s26 title L23, s28 speech L40, s29 speech L31/35/37/39).

Контекст важен: chapter и slides используют «medical AI» **не как синоним AI-диагностики**, а как **категория-зонтик** для всего поля «AI в медицине». То есть фактическая semantic — корректна, и glossary entry #1 — over-restrictive (or wrongly framed). Это **внутреннее самопротиворечие chapter glossary**, которое slides просто наследуют.

**Recommendation.**

Один из двух fix'ов — нужен USER decision:

- **Option A (предпочтительнее, минимизирует cascade):** обновить glossary entry #1 — заменить formulation на «*«medical AI»* — общая категория-зонтик; **AI-диагностика** — narrow подкатегория (CV для imaging tasks).» То есть: «medical AI» discarded as запрещённый — это легитимный umbrella term, а «AI-диагностика» — конкретный narrow subset. **Cascade:** 0 mentions нужно правит в chapter+slides; правка только glossary entry.
- **Option B:** оставить запрет, тогда cascade — заменить все 25+18 mentions на «AI в медицине» / «медицинский CV» / «medical-AI category» (длинный grep). **Cascade:** 40+ правок.

**Не decide unilaterally** — orchestrator MUST propose это в USER GATE explicitly per glossary lock enforcement rule.

**PROPOSED GLOSSARY UPDATE (needs user approval):**

```yaml
# glossary entry #1, AFTER (option A):
AI-диагностика:
  ru: AI-диагностика
  en: AI medical imaging / AI medical diagnostics
  definition: |
    Narrow подкатегория medical AI — применение AI (преимущественно computer vision)
    для анализа медицинских изображений или сигналов с целью диагноза.
    Не путать с CADe (FDA-узкая subcategory, см. #11).
  aliases_allowed: ["AI medical diagnostics", "AI medical imaging"]
  parent_category: "medical AI (общий umbrella term)"
```

---

### D2 — variations нижних регистров: mosmed.ai vs MosMedAI vs mosmedai (P2)

**Severity:** P2

**Where:** chapter L28, L34, L168, L170, L180, L188, L190, L264, L266, L268, L280, L290, L302; slides multiple.

**Issue.** Chapter использует обе формы: `mosmed.ai` (canonical lowercase, in glossary entry #20) + `MosMedAI` (после federal launch May 2024, marketing name) + `mosmedai` (without dot — L28, L34, видимо typo / nav-anchor artifact).

Slides последовательно используют `mosmed.ai` (canonical) и `MosMedAI` (только когда говорят про federal launch — s04 L40, s12 L37).

**Recommendation.** P2 — semantic OK (`MosMedAI` — после federal launch valid). Но `mosmedai` без точки (chapter L28, L34) — artifact. Не блокирует, но clean при следующей правке.

---

### D3 — «Insilico Medicine Rentosertib» vs «Insilico Rentosertib» (P2)

**Severity:** P2

**Where:** chapter L350 (full name «Insilico Medicine Rentosertib (ISM001-055 / INS018_055)»), L354, L356 («Rentosertib», без «Medicine»), L380 («Rentosertib»). Slides s17a (L20, L24, L28 — short form «Rentosertib» + один long в speech L36). Glossary entry #21 = «Insilico Rentosertib (ISM001-055 / INS018_055)».

**Issue.** Inconsistent употребление — иногда «Insilico Rentosertib», иногда просто «Rentosertib». Glossary canonical = «Insilico Rentosertib».

**Recommendation.** P2 — semantic не страдает (контекст всегда ясен). Можно нормализовать в polish round к glossary form при первом упоминании per artifact.

---

### D4 — «4-actor framework» vs «четыре актора» / «четыре актора» (P2)

**Severity:** P2

**Where:** chapter §5.5 L527 («4-actor framework»), L535 («четыре акторами»); slides s24 L21/L37 («4-actor framework»). Mixed English+Russian phrasing.

**Issue.** Minor — orthography mix. Не критично для семантики.

**Recommendation.** Polish — кодифицировать canonical «4-actor framework» как technical term (in glossary entry #25 — хотя там сейчас «Healthcare operator role», не «4-actor framework»; добавить новую запись).

---

### D5 — «medical AI» в title слайда s26 несовместим с self-declared chapter glossary lock (P1)

**Severity:** P1 (subset of D1)

**Where:** s26 title L23 — «# 3 takeaways — медицинский AI к 2026 году».

**Issue.** Title слайда — самое заметное место. После исправления D1 (option A) — стабильно; без fix D1 — это самый видимый pointer на glossary breach.

**Recommendation.** Резолвится автоматически после D1 fix.

---

## Central question + callbacks alignment

**Chapter callback chain:**

- Central question (chapter §Центральный вопрос L74): «Какие AI-обещания в медицине реально сбылись к 2026 году — и кто отвечает, когда AI-диагноз оказывается ошибочным?»
- Frames в §0.3 L120; §2.4 mosmed bridge L282; §3.0 methodology frame L309; §5.5 callback L537; §6.1 closing L572.

**Slides callback chain (deck.yaml ordering):**

- s05 (frame): «Какие AI-обещания в медицине сбылись к 2026 — и кто отвечает, когда AI-диагноз ошибочен?» — **точная копия chapter formulation** (минус слова «реально» и «оказывается»). ✓
- s12 (1st payoff arc — mosmed): speech L41 — «обещание AI-диагностики сбылось в operational форме». ✓
- s14 (mid-lecture re-orientation): L27 — «Мы прошли половину. AI-диагностика — обещание сбылось.» + speech L35–37 explicit callback к s12/s07/s01. ✓
- s17a (positive case): «первый AI-designed drug с peer-reviewed positive Phase IIa». ✓
- s17b (reality check): «AI ускорил design; clinical efficacy — отдельная задача». ✓
- s24 (4-actor answer to central q): assertion + speech L37 «центральная секция для центрального вопроса лекции». ✓
- s27 (final payoff): «Врач ставит диагноз. AI подсказывает.» speech L36 explicit «возвращаемся к центральному вопросу лекции». ✓

**Coverage:** chain `s05 → s12 → s14 → s17a → s17b → s24 → s27` — solid. **Minor P2:** s05 assertion drops two slight modifier words («реально», «оказывается») compared to chapter canonical formulation. Эти модификаторы semantically важны — «реально сбылись» означает «не просто заявлены». Полностью harmless, но если нужна точная sync — s05 assertion → «Какие AI-обещания в медицине **реально** сбылись к 2026 — и кто отвечает, когда AI-диагноз **оказывается** ошибочным?» **P2.**

**Sequence ordering — chapter vs slides:**

| Chapter | Slide(s) | Notes |
|---|---|---|
| §0.1 (Chester demo) | s01 | ✓ |
| §0.2 (poll + reveal) | s03 + s04 (paired) | ✓ |
| §0.3 (frame) | s05 (central question) | ✓ |
| §1.1 (4 types) | s06 | ✓ |
| §1.2 (FDA scale + mosmed) | s07 (FDA growth) — note s04 already revealed mosmed. **Minor narrative duplication:** mosmed metrics shown в s04 (poll reveal) и затем в s07 (FDA chart) и снова в s08 (instructive case) и в s12 (deep-dive). Это not a P1 — chapter §1.2 mirrors this structure (cumulative re-mention is intentional). | ✓ |
| §1.3 (instructive case) | s08 | ✓ |
| §2.1 (CV technical) | s09 | ✓ |
| §2.2 (sens/spec/prev/PPV) | s10 | ✓ |
| §2.3 (Liu / MASAI / Goh) | s11 | ✓ |
| §2.4 (mosmed.ai deep) | s12 | ✓ |
| §2.5 (bias CV) | s13 | ✓ |
| §3.0 (methodology frame) | s14 (mid-lecture callback) | ✓ |
| §3.1 (pipeline) | s15 | ✓ |
| §3.2 (AlphaFold + AlphaProteo) | s16 | ✓ |
| §3.3 (Rentosertib + RU context) | s17a | ⚠ **P1.** Chapter §3.3 включает significant material про RU AI-drug discovery landscape (AIDD Center, Alliance #1 CD137, Alliance #2 Alzheimer, MADD EMNLP 2025, DiMA ICML 2025) — это ~300 слов chapter §3.3 L358–368. **Slide s17a фокусируется только на Insilico Rentosertib — RU context не покрыт в visible content, и в speech L36-42 тоже не упомянут.** Это содержательный gap: chapter явно вводит «Alliance #1/#2», «MADD», «DiMA» как verifiable RU peer-reviewed achievements; slides пропускают. См. coverage gap C1 ниже. |
| §3.4 (DSP-1181) | s17b | ✓ |
| §3.5 (regulation 3-jurisdiction + PCCP) | s18 (merged) | ✓ (s18 явно merged s18+s25 из v1 plan; chapter содержит больше PCCP detail, но это ожидаемо для chapter vs slide compactness) |
| §4.1 + §4.2 (micro-exercise) | s19 | ✓ |
| §5.1 (transition) | s20 | ✓ |
| §5.2 (Obermeyer) | s21 | ✓ |
| §5.3 (LLM anti-patterns) | s22 | ✓ |
| §5.4 (data security) | s23 | ✓ |
| §5.5 (4-actor) | s24 | ✓ |
| §6.1 (3 takeaways) | s26 | ✓ |
| §6.1 closing line | s27 | ✓ |
| §6.2 (что дальше) | s28 | ✓ |
| Q&A | s29 | ✓ |

Note: deck has **29 slides** (s01–s24, s26–s29). s25 deliberately omitted — merged into s18 per plan-v2 P1-3 fix. **Verified:** no orphan reference to s25 anywhere in chapter / slides / speaker notes.

---

## Coverage gaps

### C1 — RU AI drug discovery landscape (§3.3, chapter L358–368) missing from slides (P1)

**Severity:** P1

**Where:** chapter §3.3 contains a ~300-word block on Russian AI drug discovery: AIDD Center (Сбер+AIRI, Q1 2025), Alliance #1 (CD137 oncology, Сбер+AIRI+Р-Фарм, May 2024), Alliance #2 (Alzheimer, AIRI+Р-Фарм+Сбер, Nov 2025), MADD (EMNLP 2025 Findings), DiMA (ICML 2025). Includes explicit qualifier (L366): «Ни одного российского AI-designed препарата в клинических испытаниях Phase I+ на май 2026 — все RU-программы preclinical».

In slides — `references` list of s17a includes `madd-emnlp-2025` and `dima-icml-2025`, but visible content + speaker notes of s17a are **fully focused on Insilico Rentosertib** without RU context. The disclaimer about RU stage difference (chapter L366) — completely missing from slides.

**Impact:** Universal audience (студенты-инженеры 3 курса) — это российская audience. Chapter offers RU parallel deliberately, slides drop it. Risk: in-room student asks «А что в России делается?» — лектор не имеет slide anchor, должен импровизировать.

**Recommendation.**

Two options:

- **Option A (minimal):** add 1–2 sentence speaker note к s17a (after current speech ends): «Российский контекст: на май 2026 AIDD Center работает (Сбер + AIRI), MADD opensource на EMNLP 2025, DiMA на ICML 2025 — но все RU-программы на preclinical, не на Phase I+. Не путать «РФ Rentosertib» — таких нет.» **No new slide.**
- **Option B (substantive):** add s17c slide для RU context (cost: +1 min + new slide rendering).

Orchestrator decision — recommend **Option A** if duration target ≤ 75 min is tight. Plan-v2 v2 already condensed (Phase 5 final).

### C2 — DSP-1181 OCD target detail в speech но не в visible s17b content (P2)

**Severity:** P2

**Where:** chapter §3.4 L374 — explicitly «препарата для обсессивно-компульсивного расстройства»; s17b visible content L32 — Event 1 says «Phase 1 entry (Japan, OCD)» visible. ✓ (already covered).

**Recommendation.** No gap. Skip.

### C3 — Recursion + Exscientia merger 8 Aug 2024 omitted from slides s17b (P2)

**Severity:** P2

**Where:** chapter §3.4 L382 explicitly cites Recursion + Exscientia merger ($688M, Aug 8, 2024, closed Nov 2024) as adjacent context. Slide s17b `references` lists `recursion-2024-pr` but speaker notes L37-46 don't mention merger directly.

**Impact:** Minor — merger context useful but not load-bearing for s17b's reality-check function.

**Recommendation.** P2 polish — add one sentence к s17b speaker notes если есть room: «Adjacent сигнал — Recursion + Exscientia merger 8 августа 2024 ($688M all-stock), demonstrating that standalone AI drug discovery business — трудная экономика.»

### C4 — chapter §3.0 methodological frame (peer-reviewed vs self-reported attribution rule) not surfaced на dedicated slide (P2)

**Severity:** P2

**Where:** chapter §3.0 L309 introduces an explicit methodological rule: peer-reviewed metrics без атрибуции; self-reported industry metrics — с явной атрибуцией. Slides apply rule (s16 mentions «DeepMind заявляет», s17a mentions «Insilico заявляет», «self-reported» — speech L40) but **the rule itself** has no anchor slide.

**Impact:** Low — методологическая рамка применяется, но studentам объясняется только косвенно через speech.

**Recommendation.** P2 — можно добавить 1–2 sentence в speaker notes s14 (mid-lecture re-orientation): «По ходу §3 — peer-reviewed данные мы будем цитировать как факты; self-reported industry claims (Insilico “18 месяцев”, DeepMind “2M+ users”) — с явной атрибуцией.» Не блокирует.

### C5 — chapter glossary entries #17 (ePHI) и #18 (Деперсонализация) — никакой slide их явно не объясняет, хотя s23 их использует (P2)

**Severity:** P2

**Where:** chapter glossary L616 (ePHI), L617 (Деперсонализация). s23 visible content L43 — «HIPAA защищает PHI и ePHI».

**Impact:** Low. Glossary serves self-study readers, slide audience может полагаться на лектора для inline definition.

**Recommendation.** No action. Glossary covers; slide speech mentions PHI/ePHI inline.

---

## LO mapping consistency

**Chapter LO declaration (§Учебные цели L62–68):**

- LO1 — классифицировать 4 типа AI applications + 1 пример each.
- LO2 — оценить применимость на основе клинических данных (Liu, MASAI, Goh).
- LO3 — проанализировать этическую дилемму ответственности via 4-actor.
- LO4 — применить AI web-chat для разъяснения sens/spec.
- LO8 (framing) — сформулировать 3 принципа responsible AI как input для Lec 9 черновика.

**Deck.yaml header LO declaration (L16):** `[LO1, LO2, LO3, LO4, LO8]` — ✓ exact match.

**Per-slide LO comparison (deck.yaml vs slide frontmatter):**

| Slide | deck.yaml LOs | slide frontmatter LOs | Match? |
|---|---|---|---|
| s01 | [LO1] | [LO1] | ✓ |
| s02 | [] | [] | ✓ |
| s03 | [] | [] | ✓ |
| s04 | [LO1] | [LO1] | ✓ |
| s05 | [LO1] | [LO1] | ✓ |
| s06 | [LO1] | [LO1] | ✓ |
| s07 | [LO1] | [LO1] | ✓ |
| s08 | [LO2] | [LO2] | ✓ |
| s09 | [LO1] | [LO1] | ✓ |
| s10 | [LO1, LO2] | [LO1, LO2] | ✓ |
| s11 | [LO2, LO3] | [LO2, LO3] | ✓ |
| s12 | [LO1, LO2] | [LO1, LO2] | ✓ |
| s13 | [LO3] | [LO3] | ✓ |
| s14 | [] | [] | ✓ |
| s15 | [LO1, LO2] | [LO1, LO2] | ✓ |
| s16 | [LO1, LO2] | [LO1, LO2] | ✓ |
| s17a | [LO1, LO2] | [LO1, LO2] | ✓ |
| s17b | [LO2, LO3] | [LO2, LO3] | ✓ |
| s18 | [LO3] (deck.yaml L7) | **[LO3, LO8]** (slide L7) | ⚠ **P1** |
| s19 | [LO4, LO2, LO3] | [LO4, LO2, LO3] | ✓ |
| s20 | [LO3] (deck.yaml) | **[LO3, LO8]** (slide L7) | ⚠ **P1** |
| s21 | [LO3] (deck.yaml) | **[LO3, LO8]** (slide L7) | ⚠ **P1** |
| s22 | [LO3] (deck.yaml) | **[LO3, LO8]** (slide L7) | ⚠ **P1** |
| s23 | [LO3] (deck.yaml) | **[LO3, LO8]** (slide L7) | ⚠ **P1** |
| s24 | [LO3, LO8] | [LO3, LO8] | ✓ |
| s26 | [LO1, LO2, LO3, LO8] | [LO1, LO2, LO3, LO8] | ✓ |
| s27 | [LO8] | [LO8] | ✓ |
| s28 | [LO8] | [LO8] | ✓ |
| s29 | [] | [] | ✓ |

### LO mapping P1 — drift between deck.yaml и slide frontmatter

**Severity:** P1 (single P1 — 5 slides affected с identical drift pattern).

**Issue.** Slides s18, s20, s21, s22, s23 — slide frontmatter declares `[LO3, LO8]`; deck.yaml declares only `[LO3]`. Plan-v2 references confirm LO8 framing is intentional in these slides (per L588, L612, L798, L823, L839, L864, L883, L908, L925, L948, L966, L1011, L1058 — see plan-v2 grep above). The deck.yaml entries are simply incomplete and out of sync with slide frontmatter.

**Impact.** Medium. LO8 framing is the central downstream-hook for Lec 9 — under-declaring LO8 в deck.yaml means student-facing course doc has wrong LO traceability matrix. The slides themselves correctly carry LO8 framing.

**Recommendation.** Update `deck.yaml` to add `LO8` к slides s18, s20, s21, s22, s23. Single mechanical fix.

**LO8 framing — chapter ↔ slides alignment check:**

- Chapter §Учебные цели L68: «LO8 (framing) … сформулировать три принципа ответственного использования AI в медицине, которые послужат **входом для черновика чек-листа** на Лекции 9 … Это не финальный синтез — финал делается на Лекции 9 и в индивидуальном задании к Лекции 14.»
- Chapter §6.3 L580–590: explicit «вход в копилку Лекции 9», «3 наблюдения», «не финал».
- Slide s24 speech L45: «Эти три инженерных принципа войдут в финальный takeaway на следующем слайде».
- Slide s26 speech L37–39: «Конкретные три принципа — transparency + calibration; validation set покрывает deployment population; audit-trail + post-market monitoring — это input для черновика чек-листа на лекции 9 “Этика и регулирование”. Не финальный синтез — input.»
- Slide s28 speech L40: «Три принципа responsibility … это не финальный синтез, а input для черновика чек-листа, который вы создадите на Лекции 9 “Этика и регулирование”».

**Conclusion:** LO8 framing — **exactly aligned** между chapter §Учебные цели + §6.3 и slides s24/s26/s28 (downstream-hook, не финал). ✓

---

## Frame mapping consistency

**Plan-v2 §Frame Coverage Matrix declares 6 frames:** LO / LLM pattern / LLM anti-pattern / Другой AI / Безопасность / Человек vs AI.

**Per-slide frame mapping (slide frontmatter only; deck.yaml does not carry `frame_mapping` field):**

| Slide | Frames declared | Plan-v2 frame mapping | Match? |
|---|---|---|---|
| s01 | Другой AI, Безопасность | Другой AI + Безопасность (L133) | ✓ |
| s02 | [] | — (cover slide, no frame) | ✓ |
| s03 | Человек vs AI | — (plan-v2 doesn't enumerate s03 frame) | ✓ |
| s04 | Другой AI, Безопасность | Другой AI + Безопасность (L229) | ✓ |
| s05 | Человек vs AI, Другой AI | LO1 + framing LO8 + Человек vs AI (L266) | ✓ |
| s06 | Другой AI | LO1 + Другой AI (L311) | ✓ |
| s07 | Другой AI, Безопасность | LO1 + Безопасность (L356) | ✓ (s07 plan also adds Безопасность via FDA enforcement angle) |
| s08 | Безопасность, Человек vs AI | LO2, LO8 framing, Безопасность, Человек vs AI (L396) | ✓ |
| s09 | Другой AI | LO1 + Другой AI (L439) | ✓ |
| s10 | Другой AI, Человек vs AI | LO1 + LO2 + Другой AI + Человек vs AI (L485) | ✓ |
| s11 | Человек vs AI, Другой AI, **LLM pattern** | LO2 + LO3 + Человек vs AI + Другой AI + LLM augmentation gap (L526) | ⚠ **P1** (see below) |
| s12 | Другой AI, Безопасность, Человек vs AI | LO1 + LO2 + Другой AI + Безопасность + Человек vs AI (L573) | ✓ |
| s13 | LLM anti-pattern, Безопасность, Человек vs AI | LO3 + LO6 + Безопасность + Человек vs AI + setup LLM anti-pattern (L612) | ⚠ **P2** (see below) |
| s14 | Человек vs AI, Другой AI | — (mid-lecture re-orientation, plan-v2 doesn't enumerate) | ✓ |
| s15 | Другой AI | LO1 + LO2 + Другой AI (L691) | ✓ |
| s16 | Другой AI | LO1 + LO2 + Другой AI (L733) | ✓ |
| s17a | Другой AI, Человек vs AI | LO1 + LO2 + Другой AI + Человек vs AI + central question payoff positive (L781) | ✓ |
| s17b | Человек vs AI, LLM anti-pattern, Безопасность | LO2 + LO3 + LO8 framing + Человек vs AI + LLM anti-pattern adaptation + Безопасность + central question payoff reality (L823) | ✓ |
| s18 | Безопасность, Человек vs AI | LO3 + LO8 framing + Безопасность + Человек vs AI (L864) | ✓ |
| s19 | LLM pattern, LLM anti-pattern | LO4 + LO2 + LO3 + LLM pattern + LLM anti-pattern (L908) | ✓ |
| s20 | Безопасность, Человек vs AI | LO3 + LO8 framing (L948) | ✓ |
| s21 | Безопасность, Человек vs AI, LLM anti-pattern | LO3 + LO6 + Безопасность + Человек vs AI (L991) | ⚠ **P2** (see below) |
| s22 | LLM anti-pattern, Безопасность, Человек vs AI | LO3 + LO6 + LO8 framing + LLM anti-pattern + Безопасность + Человек vs AI (L1039) | ✓ |
| s23 | Безопасность, Человек vs AI | LO3 + LO8 + Безопасность (L1084) | ✓ |
| s24 | Человек vs AI, Безопасность | LO3 + LO8 framing + Человек vs AI (L1131) | ✓ |
| s26 | Другой AI, Человек vs AI, Безопасность | All LOs + all frames + LO8 framing (L1177) | ✓ |
| s27 | Человек vs AI | LO8 framing + Человек vs AI (L1212) | ✓ |
| s28 | Безопасность, Другой AI | LO transition + LO8 framing forward (L1247) | ✓ (plan-v2 не enumerates explicit frames для s28; slide frontmatter adds Безопасность via privacy callback) |
| s29 | [] | — | ✓ |

### Frame mapping P1 — s11 has «LLM pattern» but Goh JAMA is augmentation GAP, не pattern

**Severity:** P1

**Where:** s11 frame_mapping declares `["Человек vs AI", "Другой AI", "LLM pattern"]`. Plan-v2 L526 explicitly says «**LLM augmentation gap**» (a specific phenomenon: users underloading AI), не «LLM pattern».

**Issue.** «LLM pattern» в plan-v2 frame taxonomy (per L88) — это **positive** category («объясни как студенту» успешный паттерн). Goh JAMA's finding (GPT-4 alone > doctor+GPT-4) — это **augmentation gap**, который ближе к «LLM anti-pattern» (workflow failure) или к новой frame «augmentation gap». Назвать его «LLM pattern» — terminological confusion: даёт студенту incorrect categorization.

**Recommendation.** Change s11 frame_mapping from `["Человек vs AI", "Другой AI", "LLM pattern"]` к `["Человек vs AI", "Другой AI", "LLM anti-pattern"]` или к `["Человек vs AI", "Другой AI"]` (drop the LLM frame for this slide, since Goh phenomenon is augmentation gap, not «pattern»). Sync с plan-v2 L526 verbatim.

### Frame mapping P2 — s13 has «LLM anti-pattern» but actual content is CV bias (P2)

**Severity:** P2

**Where:** s13 frame_mapping declares `["LLM anti-pattern", "Безопасность", "Человек vs AI"]`. But s13 content is **CV bias** (dermatology skin tone + pulse oximeter sensor) — это **CV / sensor anti-pattern**, не LLM. Plan-v2 L612 instead says «LO3 + LO6 + Безопасность + Человек vs AI + setup для LLM anti-pattern» — «setup для» means bridging к §5.3 LLM anti-patterns; не that s13 itself is LLM anti-pattern.

**Issue.** Frame label «LLM anti-pattern» on s13 is misleading because the slide isn't about LLMs.

**Recommendation.** Change s13 frame_mapping from `["LLM anti-pattern", "Безопасность", "Человек vs AI"]` к, например, `["Другой AI", "Безопасность", "Человек vs AI"]` (CV bias = «Другой AI» — non-LLM anti-pattern in CV/sensor domain) or к `["LLM anti-pattern (setup)", "Безопасность", "Человек vs AI"]` if semantic «setup для» is intended. Easier — drop the LLM tag for s13.

### Frame mapping P2 — s21 has «LLM anti-pattern» but Obermeyer is tabular AI bias, не LLM (P2)

**Severity:** P2

**Where:** s21 frame_mapping declares `["Безопасность", "Человек vs AI", "LLM anti-pattern"]`. But Obermeyer 2019 is **тaбличной AI** (Optum Impact Pro algorithm — gradient boosting / regression model on healthcare cost features). Chapter §5.2 explicitly contrasts с LLM (chapter L468 «Obermeyer — bias в табличной AI-модели. В LLM bias проявляется иначе»).

**Issue.** Labeling s21 as «LLM anti-pattern» — incorrect taxonomy. Obermeyer случай — **табличный AI bias**, не LLM.

**Recommendation.** Change s21 frame_mapping from `["Безопасность", "Человек vs AI", "LLM anti-pattern"]` к `["Безопасность", "Человек vs AI", "Другой AI"]` или просто `["Безопасность", "Человек vs AI"]`. Drop LLM tag.

---

## Cross-reference consistency

**Chapter cross-refs to other lectures:**

- Лекция 1 (chapter L78, L100, L120, L296, L338, L437) — multiple callbacks (YOLO в зале, frame «где AI работает», галлюцинации, Нобель referenced).
- Лекция 2 (chapter L437) — критическая оценка AI-ответа на технических деталях.
- Лекция 3 (chapter L437, L466) — финансовые данные + bias кредитного скоринга параллель.
- Коллоквиум 1 = Лекция 5 (chapter L576, §6.2).
- Лекция 6 (chapter L578) — production + agriculture, Cognitive Agro Pilot.
- Лекция 7 (chapter L437) — Практикум 1.
- Лекция 9 (chapter L68, L156, L296, §6.3 L580–590) — Этика и регулирование, LO8 финал.
- Лекция 12 (chapter L437) — Практикум 2.
- Лекция 14 (chapter L68, L590) — Будущее AI, personal version чек-листа.

**Slides cross-refs to other lectures:**

- s05 speech L38 — Лекция 1 + Лекция 9 + Лекция 14 ✓
- s11 (нет explicit cross-ref в speech; covered through chapter) ✓
- s14 mid-lecture re-orientation — implicit callback to s01/s07/s12 ✓
- s19 speech L44 — «третье микро-упражнение здесь, Практикум 1 будет на лекции 7» ⚠ **P2** (chapter L437 says «четвёртое микро-упражнение в курсе». s19 says «третье»). См. P2 below.
- s20 speech L40 — «На лекции 9 “Этика и регулирование” … черновик чек-листа; на лекции 14 “Будущее AI”» ✓
- s24 speech L45 — «3 инженерных принципа войдут в финальный takeaway на следующем слайде» (intra-deck) ✓
- s26 speech L39 — «input для черновика чек-листа на лекции 9 “Этика и регулирование”» ✓
- s27 speech L38 — «копилку лекции 9. На лекции 14 — финальный личный чек-лист» ✓
- s28 speech L36 — «Коллоквиум 1, пятая лекция»; speech L38 — Лекция 6 «AI в производстве и сельском хозяйстве»; speech L40 — Лекция 9 + Лекция 14 ✓
- s29 speech L37 — «семинар sem-04», «копилка лекции 9» ✓

### Cross-ref P2 — micro-exercise count mismatch (P2)

**Severity:** P2

**Where:**
- Chapter §4.2 L437: «Это **четвёртое** микро-упражнение в курсе; на **Лекции 7** будет Практикум 1 …, а на Лекции 12 — Практикум 2».
- Slide s19 speech L44: «**четвёртое микро-упражнение здесь, Практикум 1 будет на лекции 7**.» — WAIT, let me re-read.

Actually re-checking s19 speech: «Эта дисциплина критической оценки — то, что мы будем тренировать весь курс; **четвёртое микро-упражнение здесь**, Практикум 1 будет на лекции 7.» ✓ matches chapter «четвёртое».

So no mismatch actually. Removed P2 flag — verified consistent.

**Final cross-ref consistency:** **0 issues**. ✓

---

## References parity

**Chapter `Источники` section** has 62 numbered references (per deck.yaml `references_count: 62`).

**Spot check key references appearing in slide `references` lists vs chapter:**

| Reference key (slide) | Chapter source (line) | Match? |
|---|---|---|
| `cohen-2019-chester` (s01) | refs L634 | ✓ |
| `rajpurkar-2017-chexnet` (s01, s09, s10) | refs L652 | ✓ |
| `wang-2017-cxr8` (s01) | refs L636 | ✓ |
| `fda-aiml-list-2025` (s04, s07) | refs L642 | ✓ |
| `imaging-wire-2025` (s04, s07) | refs L643 | ✓ |
| `mos-ru-2025` (s04, s12) | refs L645 | ✓ |
| `remedium-2025` (s04, s12) | refs L646 | ✓ |
| `markets-and-markets-2025` (s05) | refs L637 | ✓ |
| `towards-healthcare-2025` (s05) | refs L638 | ✓ |
| `eu-ai-act-2024-1689` (s08, s18, s24) | refs L694 | ✓ |
| `fda-pccp-2024` (s08, s18) | refs L693 | ✓ |
| `jama-network-open-2025` (s07) | refs L644 | ✓ |
| `selvaraju-2017-gradcam` (s09) | refs L653 | ✓ |
| `liu-2019-lancet` (s11) | refs L654 | ✓ |
| `masai-2024-lancet` (s11) | refs L655 | ✓ |
| `hofvind-2025-lancet` (s11) | refs L656 | ✓ |
| `goh-2024-jama` (s11) | refs L657 | ✓ |
| `healthcare-me-2026` (s12) | refs L647 | ✓ |
| `webiomed-2026` (s12, s18) | refs L648, L696 | ✓ |
| `daneshjou-2022-science-advances` (s13) | refs L659 | ✓ |
| `adamson-2018-jama-derm` (s13) | refs L658 | ✓ |
| `sjoding-2020-nejm` (s13) | refs L660 | ✓ |
| `dimasi-2016-jhe` (s15) | refs L664 | ✓ |
| `wouters-2020-jama` (s15) | refs L665 | ✓ |
| `mullard-2024-nrdd` (s15) | refs L666 | ✓ |
| `jumper-2021-nature` (s16) | refs L667 | ✓ |
| `abramson-2024-nature` (s16) | refs L668 | ✓ |
| `watson-2024-alphaproteo` (s16) | refs L669 | ✓ |
| `alphafold-db` (s16) | refs L670 | ✓ |
| `insilico-nature-medicine-2025` (s17a) | refs L671 | ✓ |
| `pubmed-40461817` (s17a) | refs L672 | ✓ |
| `prnewswire-2024` (s17a) | refs L673 | ✓ |
| `madd-emnlp-2025` (s17a) | refs L688 | ✓ |
| `dima-icml-2025` (s17a) | refs L689 | ✓ |
| `synapse-patsnap-dsp1181` (s17b) | refs L674 | ✓ |
| `sumitomo-2020-pr` (s17b) | refs L675 | ✓ |
| `cas-insights-2024` (s17b) | refs L676 | ✓ |
| `recursion-2024-pr` (s17b) | refs L677 | ✓ |
| `vniiimt-2024` (s18) | refs L695 | ✓ |
| `obermeyer-2019-science` (s21) | refs L699 | ✓ |
| `berkeley-news-2019` (s21) | **NOT in refs list** (chapter mentions Berkeley URL nowhere in refs section, only as Wiki link) | ⚠ **P2** |
| `stat-news-2019` (s21) | **NOT in refs list** | ⚠ **P2** |
| `npr-2023-tessa` (s22) | refs L700 | ✓ |
| `ai-incident-db-545` (s22) | refs L701 | ✓ |
| `comm-medicine-2025` (s22) | refs L704 | ✓ |
| `beckers-2025` (s22) | refs L705 | ✓ |
| `gallup-2025` (s22) | refs L706 | ✓ |
| `uhg-2024` (s23) | refs L707 | ✓ |
| `bleeping-computer-2024` (s23) | refs L708 | ✓ |
| `hipaa-journal-2024` (s23) | refs L709 | ✓ |
| `sweeney-2002` (s23) | refs L711 | ✓ |
| `price-2019-stanford` (s24) | refs L712 | ✓ |
| `gerke-2020-elsevier` (s24) | refs L713 | ✓ |

### Refs parity P2 — `berkeley-news-2019` + `stat-news-2019` cited in slide s21 references list, но в chapter §Источники не указаны как numbered refs (P2)

**Severity:** P2

**Where:** Slide s21 `references` list (L10) includes `berkeley-news-2019` + `stat-news-2019`. These URLs appear in s21 illustration sources (L18, L19) and slide speaker notes do not cite them directly. Chapter §5.2 refs section L699 only lists Obermeyer Science paper itself (#48).

**Impact:** Low. The URLs are used as illustration sources only, не as primary citations in chapter prose.

**Recommendation.** P2 — orchestrator may either (a) add Berkeley News + STAT News entries в chapter refs section (as supporting press coverage), or (b) leave as-is and treat slide references field как «illustration sources» (semi-formal). Option (b) — less work, acceptable per current methodological convention.

---

## DISCREPANCIES — summary list

### D1 — «medical AI» glossary lock breach
**Severity:** P0. See Terminology Drift §D1.

### D2 — `mosmedai` (no dot) artifact in chapter
**Severity:** P2. See §D2.

### D3 — «Insilico Rentosertib» vs «Rentosertib» mix
**Severity:** P2. See §D3.

### D4 — «4-actor framework» Russian/English mix
**Severity:** P2. See §D4.

### D5 — s26 title carries «медицинский AI» glossary tension
**Severity:** P1 (subset of D1).

### D6 — Goh «76.3 / 73.7» в slide vs «76/74» в chapter
**Severity:** P1. See Number consistency matrix row Goh.

**Recommendation.** Sync s11 visual to «76% / 74%» per chapter, or add «76.3/73.7» к chapter §2.3 with source.

### D7 — CheXNet «sens 0.96 / spec 0.93» в s10 visual vs chapter's «sens ≈ 0.94–0.96, spec ≈ 0.89–0.93»
**Severity:** P1. See Number consistency matrix row CheXNet.

**Recommendation.** Change s10 visual gold-info-card к «CheXNet pneumonia: sens 0.94–0.96, spec 0.89–0.93 → PPV ~8% при prev 1%, ~78% при prev 30%». Speech уже corrected.

### D8 — RU AI drug discovery landscape missing from slides
**Severity:** P1. See Coverage Gaps §C1.

### D9 — LO8 missing from deck.yaml for s18, s20, s21, s22, s23
**Severity:** P1 (5 slides aggregated). See LO mapping section.

### D10 — s11 frame_mapping has «LLM pattern» for what is actually augmentation gap
**Severity:** P1. See Frame mapping §s11.

### D11 — s13 frame_mapping has «LLM anti-pattern» for CV bias
**Severity:** P2. See Frame mapping §s13.

### D12 — s21 frame_mapping has «LLM anti-pattern» for tabular AI bias
**Severity:** P2. See Frame mapping §s21.

### D13 — s05 assertion drops «реально» / «оказывается» from canonical central question
**Severity:** P2. See Central question §s05.

### D14 — Recursion + Exscientia merger context omitted from s17b speaker notes
**Severity:** P2. See Coverage Gaps §C3.

### D15 — methodology rule (peer-reviewed vs self-reported attribution) не surfaced на dedicated slide
**Severity:** P2. See Coverage Gaps §C4.

### D16 — berkeley-news-2019 + stat-news-2019 not in chapter refs section
**Severity:** P2. See Refs parity.

---

## Top fixes per artifact

### Chapter
- **D1 (P0):** Update glossary entry #1 to make «medical AI» an umbrella category (option A) or do mass-rename (option B). USER decision required.
- **D8 (P1):** No fix needed in chapter (chapter already covers RU drug discovery); change is in slides side.
- **D16 (P2):** Optionally add `berkeley-news-2019` + `stat-news-2019` к §Источники §Раздел 5 as supporting press refs.

### Slides
- **D7 (P1):** Update s10 visual gold-info-card к «sens 0.94–0.96, spec 0.89–0.93» (per chapter §2.2 L229).
- **D6 (P1):** Update s11 visual «GPT-4 alone 76.3% vs doctor+GPT-4 73.7%» к «GPT-4 alone 76% vs doctor+GPT-4 74%» (per chapter §2.3 L252).
- **D8 (P1):** Add 1–2 sentence к s17a speaker notes covering RU drug discovery context (AIDD, MADD, DiMA + preclinical-stage disclaimer).
- **D10 (P1):** Change s11 frame_mapping `["Человек vs AI", "Другой AI", "LLM pattern"]` → `["Человек vs AI", "Другой AI"]`.
- **D11 (P2):** Change s13 frame_mapping — drop «LLM anti-pattern», replace with «Другой AI».
- **D12 (P2):** Change s21 frame_mapping — drop «LLM anti-pattern», replace with «Другой AI».
- **D13 (P2):** Sync s05 assertion к canonical «Какие AI-обещания в медицине **реально** сбылись к 2026 — и кто отвечает, когда AI-диагноз **оказывается** ошибочным?»
- **D14 (P2):** Optionally add Recursion+Exscientia mention к s17b speaker notes.

### deck.yaml
- **D9 (P1):** Add `LO8` к learning_outcomes lists for slides s18, s20, s21, s22, s23.

### Glossary
- **D1 (P0):** Update entry #1 (medical AI relationship) — see PROPOSED GLOSSARY UPDATE above. **USER approval needed before applying.**

---

## Pass-through items (validated consistent)

- Central question text vs s05 vs s27 closing — solid alignment (modulo D13 minor word drop).
- mosmed.ai operational metrics — 14M+ / 74 регионов / 70 сервисов / 18M+ изображений — uniformly applied (chapter + s04 + s08 + s12 + s14).
- Rentosertib clinical numbers — fully synced (chapter ↔ s17a).
- Obermeyer numbers — fully synced (chapter §5.2 ↔ s21).
- MASAI numbers — fully synced.
- Change Healthcare numbers — fully synced.
- FDA PCCP 4 Dec 2024 + EU 2 Aug 2026 / 2 Aug 2027 + ФЗ-23 1 July 2025 — fully synced.
- AlphaFold 200M+ / Nobel 2024 / Hassabis+Jumper+Baker — fully synced.
- 4-actor framework structure (Doctor / Operator / Vendor / Regulator с technical control × legal liability осями) — chapter §5.5 ↔ s24 — solid.
- LO8 framing as «input для черновика Lec 9, не финал» — explicit и uniformly applied (chapter §Учебные цели + §6.3 ↔ s24 + s26 + s28).
- s25 orphan reference — **0 mentions** в slides / chapter / speaker notes. Deletion clean.
- References list per slide — 50+ refs verified against chapter §Источники, all primary citations present.

---

## Phase 7 outcome

- **Verdict:** **REVISE.**
- **Blocking issue:** D1 (glossary self-contradiction on «medical AI») requires USER decision before USER GATE 2.
- **Significant drifts (5):** D6, D7, D8, D9, D10 — all fixable mechanically once decided. Each is a P1.
- **Polish backlog (9 items):** D2, D3, D4, D5, D11, D12, D13, D14, D15, D16 — defer to polish round between USER GATE 2 and Phase 8.

**Recommended orchestrator workflow:**

1. Bring D1 (glossary lock decision) к USER as standalone question — option A или B — with cascade-of-changes table.
2. Spawn `presentation-designer` for D7 (s10 numbers fix) + D6 (s11 numbers fix) + D9 (deck.yaml LO8 additions) + D10/D11/D12 (frame_mapping cleanup) + D8 (s17a speaker notes RU context add) — single revision pass.
3. After revision, re-run `consistency-checker` (Phase 7.5) for sign-off, then proceed к pre-user-gate walkthrough.
4. Polish items (D2–D5, D13–D16) can be batched with any later Phase 8 minor touches without blocking USER GATE 2.

Expected next-revision verdict (after D1 + 5 P1 fixed): **APPROVE-WITH-POLISH**.

---

*Report length: ~3,400 слов. Generated 2026-05-13, mode=`chapter+slides`, source-of-truth=chapter v2 (commit 5c4b06c), slides v1 (commit aa4567d).*
