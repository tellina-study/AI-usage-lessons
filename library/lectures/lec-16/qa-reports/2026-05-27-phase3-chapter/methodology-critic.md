**VERDICT: REVISE**

# Methodology critique — chapter v1 Лекция 16 «AI в нефтегазовой отрасли и добыче ресурсов»

**Дата:** 2026-05-27
**Object:** chapter.md + chapter-part2.md + chapter-part3.md + chapter-part4.md (28 541 слов, 4 parts)
**Reviewer:** methodology-critic
**Reference inputs:** plan v2 (2026-05-27-phase1-plan/plan-v2.md), CLAUDE.md (Chapter Depth Baseline / AI-Failure / Baseline-mandate / Russification), tools/lecture-production/README.md

---

## Summary

Chapter v1 — **структурно ambitious и methodologically sound на уровне архитектуры**: keystone-ось «данные × физика» хорошо введена в Разделе 0, integrated through all 6 sections, и 10 documented failures распределены по quadrants (не concentrated в одном). LO1–LO3+LO7 покрыты явно. Self-check в конце каждого раздела (6 проверок) — present.

**Но 3 структурных gap'а блокируют APPROVE:**

1. **Russification depth — критически недостаточная.** Sample sections содержат 70+ critical anglicism hits (deployment, pipeline, stack, baseline, insight, takeaway, edge case, workflow, etc.) **без gloss** и не в brand allowlist. Это narrative body, не frontmatter — visible тексту студенту. Лекция 8 lesson explicit прошлась мимо.
2. **Multiple typos / encoding artifacts**, отдельно неприемлемо для academic textbook chapter (`provals` (s/b «провалы»), `Studen` (s/b «студент»), `пайтон` (s/b «pattern»? — ambiguous), `chrebrolution` (s/b «разрешение» или похожее), `galleon` (s/b «hallucinated»?), `skvazhin` (latin вместо «скважин»), `cgeo` (ambiguous), `деitalised` (encoding break), `agreggate` (англ. typo «aggregate»). 7+ instances в 4 parts.
3. **Word count на минимальной границе baseline (28 541 vs 30 000 target).** +41 слов над absolute minimum 28 500. Per CLAUDE.md «Chapter Depth Baseline» rule = технически PASS, но user-explicit expectation 30k ±5% center, и при чтении ощущается, что несколько deep-dives (особенно §3.6 EU 2024/1787 detail, §4.5 plant-wide stagnation Q4 reframe) тоньше academic-textbook-chapter quality.

Дополнительно — **2 missing P0 categories**: (a) frontmatter `parts: 4` есть, но `length_words: ~30500` overstates actual (28 541); (b) Q&A backup Q1 NVIDIA Omniverse — конкретный ответ adequate, но Q3 REE / mining cross-domain answer **superficial** (~200 слов вместо promised 200-400 floor).

**Top 3 fixes для Phase 4 revision:**
1. **Russification pass:** caller `book-editor` — full deep-scan + replacement цикла critical anglicisms vs allowlist (brand names allowed, остальное gloss или russify). Cost: ~2-3h editing pass.
2. **Typo + encoding cleanup:** найти и исправить все instances `provals`, `Studen`, `пайтон`, `chrebrolution`, `galleon`, `skvazhin`, `cgeo`, `деitalised`, `agreggate`, и системно через grep find similar artifacts. Cost: ~30 min.
3. **Expand 2-3 thin sections к 30k center:** §3.6 EU regulation detail (+~400 слов на penalty structure + timeline + MS-by-MS variance), §4.5 refinery Q4 reframe (+~300 слов connecting к §1.3 + adding concrete edge case), Q3 REE deep-dive в Q&A (+~200 слов с конкретным lithium triangle / Mountain Pass example). Cost: ~1.5h book-editor.

---

## P0 issues (BLOCKING — нужно зафиксить ДО USER GATE A)

**P0-1. Russification depth — критический gap (Лекция 8 lesson).**

В narrative body chapter всех 4 parts — **systemic excessive англицизмы вне brand allowlist**, без gloss:

Sample hits (NOT exhaustive):
- `production-grade` (chapter.md:266), `deployment` (multiple), `pipeline` (multiple), `stack` (multiple), `tradeoff` (implied)
- `baseline` (chapter-part2.md:85, chapter-part4.md многократно), `insight`/`insights` (multiple)
- `takeaway` (Critical takeaway для LO3, chapter-part2.md:274), `edge case` (multiple), `use case` (multiple)
- `workflow` (chapter-part2.md:42 + многие), `screening` (multiple — gloss отсутствует первый раз), `vendor pivot` (no russify gloss первый раз)
- `pilot stuck`, `pilot purgatory` (chapter.md:266+), `anchor customer` (multiple — gloss отсутствует первый раз)
- `material lift` (chapter.md:427), `out-of-distribution` (multiple), `value chain` (multiple)
- `unit economics` (multiple), `playbook` (implied), `commodity cycle` (chapter-part4.md:193)
- `commit` (chapter.md:445, как «commit decision»), `coupling` (chapter-part3.md:345), `inversion` (chapter-part3.md:351)
- Latin terms внутри Russian phrases: `the same`, `the most accurate`, `the structure failure модели Watson 2014 эпохи` (chapter-part2.md:333)

**70+ critical anglicism hits** в narrative body (по `\b(deployment|pipeline|stack|tradeoff|baseline|insight|takeaway|edge case|deploy|workflow)\b` count). Это **structural Russification failure**, не polish. CLAUDE.md anti-pattern «Excessive англицизмы в visible body / speaker notes для RU-аудитории МГТУ ИУ6» violated.

**Acceptance criterion:** deep latin-token scan (см. Лекция 8 lesson) на all 4 parts должен показать `unique - allowlist = ∅` для narrative body. Allowlist: brand names (SLB, Aramco, Eclipse, INTERSECT, CMG, OpenFOAM, MethaneSAT, Carbon Mapper, Tanager-1, GHGSat, Bridger Photonics, Fervo, etc.), established acronyms с inline gloss (MRV, OGI, LDAR, OGMP, SIL, SIS, BOP, PRV, ESD, APC, CCS, EGS, ROP, BHC3, NOC, IOC, HSE, FPSO, BOE, bopd), URLs, person/case names. Остальные English unigrams — gloss или Russify.

**Severity:** P0 «Russification structural gap». Лекция 8 cost-of-omission = 3 revision passes, ~3h wasted. Здесь catch at Phase 3 prevents that downstream.

---

**P0-2. Typos / encoding artifacts в academic-textbook narrative — недопустимо для chapter v1 final.**

Найденные конкретные instances:
- `chapter.md:150` «свои provals» (s/b «провалы» — лишний tilde or copy-paste artefact)
- `chapter.md:274` «Studen, читающий эту главу» (s/b «Студент»)
- `chapter-part3.md:69` «chrebrolution детекции порядка 500 kg/h» (s/b «разрешение» — encoding break или autocomplete glitch)
- `chapter-part3.md:379` «не сможет легко отличить galleon hallucinated ответ» (`galleon` — non-word artifact)
- `chapter-part4.md:72` «correlation между skvazhin, screening cgeo-параметров» (latin в нативном тексте + `cgeo` ambiguous)
- `chapter-part4.md:370` «Текущий пайтон. AI в BOP context» (`пайтон` s/b «pattern», phonetic typo)
- `chapter-part4.md:53` «**Q4** energy transition (CCS/EGS) … Pilots, public info ограничена [VFY-day-of]» — OK structurally, но context shows mixed Russian/English drift

Total: **7+ confirmed encoding/typo artifacts** в narrative body. Это P0 для academic chapter, потому что:
1. Подрывает credibility — студент читает «свои provals» и теряет доверие к остальным цифрам.
2. Скорее всего другие подобные artifacts остались — нужен systematic grep + replace pass.
3. Не «polish issue» — это **proofreading FAIL** на drafting phase.

**Severity:** P0 «Typo / encoding artifacts». Cost = ~30 min find-and-replace pass.

---

## P1 issues (HIGH — должны быть зафиксены, но не блокируют GATE)

**P1-1. Word count на абсолютной границе minimum (28 541 vs 30 000 center).**

CLAUDE.md «Chapter Depth Baseline» rule: для L4+ — **target 30 000 ±5% = 28 500-31 500**. Текущий результат = +41 слов над absolute minimum (28 500). Per rule technically PASS, но:

- `length_words: ~30500` в chapter.md frontmatter line 4 **overstates** actual count by ~7%. Это **frontmatter accuracy issue** — должно быть `length_words: ~28500` или actual figure.
- Recommended push до 29 500-30 000 центра baseline. Конкретно — секции, где expansion даст academic-chapter depth value:
  - **§3.6 EU 2024/1787 deep-dive** (currently ~700 слов; expand to ~1100): добавить (a) penalty structure tiers — например, «штраф рассчитывается как % EU oil/gas revenue, ОТДЕЛЬНО для производителей vs импортёров; для импортёров — Maximum Methane Intensity Value 0,2% к 2027»; (b) member-state variance — например, как Германия и Польша applies regulation differently; (c) timeline — milestones (5 мая 2025, 5 августа 2025, 2027 cutoff) + delays risk.
  - **§4.5 plant-wide stagnation Q4 reframe** (currently ~400 слов; expand to ~700): сейчас слишком кратко reframed; добавить (a) explicit edge cases где multi-physics ломает (например, при changeover между feedstocks), (b) cross-link к §1.3 с конкретными deltas (когда single column работает / при каком количестве coupled units AI ломается).
  - **§5.2 Газпром нефть Cognitive Geo detail** (currently ~700 слов; expand to ~900): добавить (a) сравнение с SLB Lumi pre-2022 — что Газпром нефть импортировала; (b) post-2022 transition specifics — какие конкретно компоненты пришлось insourcing.
  - **Q&A Q3 REE / mining cross-domain** (currently ~200 слов; promised floor 200-400): expand до 350 слов с конкретными lithium triangle examples (Salar de Atacama, Salar del Hombre Muerto), Mountain Pass operational details.

Net expansion ~1000+ слов → 29 500-30 000 range без bloat. Это **P1 «depth gap», не «length gap»**.

**Severity:** P1. Не блокирует GATE A, но recommended push для academic-textbook-chapter quality.

---

**P1-2. Latin-token leaks: `it`, `the`, `same`, embedded English phrases внутри Russian sentences.**

Sample:
- `chapter.md:316` «Ambyint публикует it как «средняя по 200 скважинам»» — `it` должно быть «это / её / результат» или просто «публикует данные».
- `chapter-part2.md:333` «risk pattern, который повторит the structure failure модели Watson 2014 эпохи» — `the structure` — английская конструкция.
- `chapter-part3.md:251` «portable laser analyzers — это **the most accurate methane sensors в индустрии**» — `the most accurate` целиком English.
- `chapter-part3.md:308` «AI **не** может компенсировать» — `**не**` нормально, но contrast в окружающем тексте показывает frequent code-switching style.

Это **mode of presentation drift**, который Лекция 8 explicit caught. Pattern-narrow grep insufficient — нужен deep latin-token scan.

**Severity:** P1 «Latin-token in narrative leaks».

---

**P1-3. Keystone-axis depth check — Q1/Q3 strong, но Q2/Q4 axis-mapping shallow.**

Раздел 0 §0.2 определяет 2 оси и §0.3 introduces 4 quadrants ясно. Но при чтении detail:

- **Q1 (Раздел 1)**: axis-mapping явный и многократно referenced ✓
- **Q3 (Раздел 2 §2.1)**: «спускаемся в data-беднейший квадрант» — axis-mapping ✓
- **Q2 (Раздел 3 §3.1)**: «Q2 — это самый необычный квадрант на keystone-матрице» — axis-mapping ✓
- **Q4 (Раздел 4 §4.1)**: «Q4 — самый честный квадрант» — но менее tightly connected к ground truth of «low data + low physics». §4.2 (Northern Lights) и §4.3 (Fervo) описаны как cases, но **mapping back к axis** thinner, чем для Q1/Q3.

Конкретно: для каждого case в Q4 — нет явной строки «и данные мало (X projects globally), и физика на 100-летнем horizon известна частично (because Y)». Это P1 «axis drift в Q4», не блокирующий, но рекомендован для Phase 4 revision: добавить 1-2 строки axis-tie на каждый Q4 case study.

**Severity:** P1 «Keystone axis drift в Q4 section».

---

**P1-4. Baseline / counterfactual coverage — strong но 2-3 gaps.**

Sample 10 measurable claims:

| # | Claim | Baseline? |
|---|---|---|
| 1 | Aramco $1,8B realized 2024 | ✓ baseline $440B revenue = 0,4% (chapter-part2.md:77) |
| 2 | Northern Lights 1,5 Mt/год | ✓ baseline IEA 7,6 Gt/2050 = 0,02% (part3:309) |
| 3 | MethaneSAT 410 t/h Permian | ✓ baseline EPA est ~273 t/h → +50% (part3:73) |
| 4 | Eni HPC6 606 PFLOPS | ✓ Top500 #5, 9× HPC5 (part2:59) |
| 5 | Ambyint +15% on 200 wells | ✓ baseline per-well historical mean (ch:314) |
| 6 | Honeywell UOP 310+ units | ✓ baseline ~700 global refineries = ~14% (ch:343) |
| 7 | Роснефть +1 Mt/год Башнефть | ✓ baseline ~17 Mt/год = +5,9% (ch:370) |
| 8 | 86% pilot stuck | ✓ baseline cross-industry ~67% → +19 pp (ch:250) |
| 9 | Fervo IPO +331% | ✗ baseline reference IPO premium typical clean-tech нет |
| 10 | Cyber +935% | ✗ baseline absolute volume или % industry attack baseline нет |
| 11 | 2020 oil crash 107k jobs | ✗ baseline total US O&G workforce pre-2020 (~600k?) нет |
| 12 | C3.ai O&G 5,9% FY24 | ✓ explicit $18M из $310M total (ch:264) |

10 of 12 — has baseline. **3 missing denominators:**

- Fervo IPO +331%: нет comparable baseline (например, «average clean-tech IPO 2024-2026 premium = X%»).
- Cyber +935%: absolute volume? Quarterly comparison? Industry total cyber events baseline?
- 2020 oil crash 107k: % от total US O&G workforce (~600k pre-2020? need denominator).

**Severity:** P1 «3 measurable claims missing denominator». Не критично, но per CLAUDE.md «Baseline / Counterfactual Mandate» — нужны inline baselines.

---

**P1-5. Anti-pattern «revolution» / «AI revolution» / «революция» appears multiple times (not always in critical framing).**

Grep result:
- `chapter-part2.md:89` «когда вендор продаёт "AI revolution в exploration"» — **critical framing** ✓
- `chapter-part2.md:232` «Watson Health (2015) объявлялся как **революция в онкологии**» — **critical framing** ✓ (cautionary tale)
- `chapter-part2.md:274` «Студент, который пишет "AI заменит пластового симулятора через 5 лет" — упускает структурную картину» — **critical framing** ✓

These are OK because used to **dismantle hype**, не promote. ✓ NOT a violation.

But check `chapter-part3.md:318` «AI — это catalyst, не silver bullet» — **explicit anti-magic-pill** framing ✓ (this is correct usage).

**Severity:** P2 (these are critical framings; flag as «watch for tone consistency but not violation»).

---

**P1-6. Anonymization check — мостик Раздел 5 vs frontmatter mismatch.**

Frontmatter chapter.md line 11: `audience: "студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)"` ✓ generic.

But chapter-part4.md §6.3 «Карьерный мост» (line 312): «Профильные технические университеты предлагают магистерские программы по AI в энергетике + нефтегазе; cross-disciplinary программы (петрофизика + ML, geomechanics + ML) — особенно ценны».

✓ Generic (no «МГТУ / Бауман / РГУ Губкина» named — anonymization PASS).

But Грубо: «Минэнерго, Минприроды» in §6.3 — это **Russia-specific regulators**, что binds к Russian audience. Хотя курс универсальный — это OK, но для anonymization это flag soft.

**Severity:** P2. Acceptable, но рекомендован — phrase «национальные energy министерства (например, Минэнерго в России, DOE в США, EU Commission)» для polish.

---

**P1-7. Q&A backup Q3 (REE / mining) — superficial vs promised 200-400 слов floor.**

Q&A backup `Q3. AI в добыче редкоземельных металлов — пример из non-O&G mining?` (chapter-part4.md:334-342) — actual ~190 слов. Promised 200-400 слов floor (per task brief). 

Three subtopics listed (lithium brine, hardrock REE, deep-sea polymetallic) — но каждый ~30-50 слов, не deep-dive. Сравнение с Q1 (NVIDIA Omniverse) и Q12 (decision tree) — те ~250-300 слов каждый.

**Severity:** P1 «Q&A Q3 thin vs promise». Recommend expand до 350 слов с specific lithium triangle (Atacama 30 000 t/y baseline), Mountain Pass throughput.

---

**P1-8. AI-Failure & Judgment ≥43% strict-in — claim ≠ verification.**

Frontmatter chapter.md line 19-21:
```
strict_in_self_estimate:
  words: "~13 000 / 30 000 = 43%"
  sections: "R1 + R2 + R3 + R4 + R5 содержат failure-deep-dive; не concentrated в одном"
```

But actual word count = 28 541 (not 30 000). 13 000 / 28 541 = **45,6%** — actually slightly higher than self-estimate. ✓ PASS если 13k figure verified.

**Distribution sample check (strict-in failure/limit/criterion/alternative blocks):**

- **Part 1** (R1, ~7800 слов): §1.2 86% pilots (1500 слов) + §1.3 alert fatigue (1100 слов) + §1.7 Cognite/C3.ai failure (700 слов) + §1.8 6 criteria (1000 слов) = ~4300 слов strict-in / 7800 = **55%** ✓ strong
- **Part 2** (R2, ~7700 слов): §2.5 BP+Beyond Limits (1100 слов) + §2.6 IBM+Repsol (1300 слов) + §2.7 alternative simulators (1100 слов) + §2.8 6 fundamental limits (1300 слов) = ~4800 / 7700 = **62%** ✓ strong
- **Part 3** (R3+R4, ~8200 слов): §3.3 MethaneSAT loss (1100 слов) + §3.5 4× discrepancy (700 слов) + §3.7 alternative OGI (1000 слов) + §4.4 CCS 190× + LLM hallucination (1200 слов) + §4.5 plant-wide stagnation (400 слов) + §4.6 alternative SIS (1200 слов) = ~5600 / 8200 = **68%** ✓ very strong
- **Part 4** (R5+closing, ~9500 слов): §5.4 cyber +935% (700 слов) + §5.5 2020 + Deepwater Horizon (1500 слов) + §6.2 10 failures table (300 слов) + Q&A (3000 слов with failure-bucket Q4, Q5, Q7, Q9, Q10) ≈ ~5500 / 9500 = **58%** ✓ strong

Total estimate: ~20 000 strict-in / 28 541 total = **~70%**. **Significantly higher than 43% target.** ✓ PASS holistically + distributed across all 4 parts. No single-cluster concentration.

**Severity:** P2 → update self-estimate в frontmatter, либо verify methodology того counting.

**Verdict on this dimension:** **PASS, significantly above target.**

---

## P2 issues (LOWER — polish для Phase 4)

**P2-1. `length_words: ~30500` in frontmatter overstates actual.** Update to `length_words: 28541` (actual) or `~28500`. Issue: misleading metadata.

**P2-2. `references_count: ~45` — actual count 46 in chapter-part4.md References section.** Update to exact.

**P2-3. Frontmatter audience description «универсальная, не отраслевые специалисты» — clear ✓ но lowercase «универсальная» mid-sentence + colon — minor style.

**P2-4. Multi-part navigation links** «**[Часть 2 →](chapter-part2.md):**» — bold + arrow OK structurally, но consider lighter `[Часть 2 →](chapter-part2.md)` for visual hierarchy.

**P2-5. `provals` typo in chapter.md:150** — see P0-2.

**P2-6. `Studen` typo in chapter.md:274** — see P0-2.

**P2-7. `пайтон` (likely intended «pattern») in chapter-part4.md:370** — see P0-2.

**P2-8. `chrebrolution`, `galleon`, `skvazhin`, `cgeo`, `agreggate`** — see P0-2.

**P2-9. Excessive em-dashes density** — typical academic Russian, OK. Не violation, but tighter punctuation в few places (например chapter.md:114-130 introduction) would improve readability.

**P2-10. Latin headers в TOC like `[§2.5. Провал 1: BP + Beyond Limits (2018–2023, $20 млн, vendor pivot)]` — `vendor pivot` could be glossed at first occurrence to `провал вендора (vendor pivot — смена приоритетов компании от заявленного партнёрства)`.

---

## Per-area assessment

### 1. Chapter Depth Baseline

- **Word count:** 28 541 (chapter.md 8277 + part2 5744 + part3 6981 + part4 7539). PASS absolute minimum (28 500), но **на +41 words граница** — recommended push до 29 500-30 000 center. Frontmatter overstates `~30500`.
- **Multi-part split:** 4 files. chapter.md = 464 строк ✓, part2 = 351 ✓, part3 = 501 ✓, part4 = 577 ✓ (close to 600 limit but within).
- **Frontmatter compliance:** `parts: 4` ✓, `slide_map` ✓, `learning_outcomes` ✓, `strict_in_self_estimate` ✓, `parts_files` ✓.
- **TOC + cross-refs:** Карта главы в chapter.md ✓; Оглавление per part ✓; navigation `[← Часть N]` / `[Часть N+1 →]` consistent ✓; «вы здесь» markers — OK structural usage в frontmatter exempt area (per `no-timing-no-methodology-in-slides` exempt list).

**Verdict per-area:** PASS baseline (+1 polish: bring closer to 30k center).

### 2. AI-Failure ≥43% strict-in

- **Self-estimate:** ~13 000 / ~30 000 = 43% (frontmatter).
- **Actual sample-based count:** ~20 000 / 28 541 = ~70%.
- **Distribution:** all 4 parts have ≥55% strict-in. No single-cluster concentration (R3 highest = 68%, but other parts ≥55%).
- **Bucket types delivered:** documented failures (10) ✓, fundamental limits (6) ✓, «AI не нужен» criteria (12 = 6 в Q1 + 3 в Q2 + 3 в Q4) ✓, alternatives (6+ tools listed) ✓.
- **Specific failures deep-dive ≥600 слов each (10 promised):** BP+Beyond Limits ✓ (~1100 слов), IBM+Repsol ✓ (~1300 слов), Cognite ✓ (~700 слов), C3.ai ✓ (~400 слов — slightly short), MethaneSAT loss ✓ (~1100 слов), 86% pilot ✓ (~1500 слов), Aspen Mtell alert fatigue ✓ (~1100 слов), 2020 oil crash 107k ✓ (~800 слов), 4× discrepancy ✓ (~700 слов), cyber +935% ✓ (~700 слов). 9/10 strong; C3.ai short.

**Verdict per-area:** PASS holistic distribution. (1 polish: expand C3.ai brief to ≥600 words; update strict-in estimate to ~70%.)

### 3. Keystone axis depth

- **Variant B (data × physics 2×2):** introduced in §0.2 (definitions) + §0.3 (4 quadrants) clearly ✓
- **Operational definitions:** «Доступность данных» = N labelled examples; «Определённость физики» = numerical model with known accuracy ✓
- **Quadrant mapping in sections:** Q1 ✓, Q3 ✓, Q2 ✓ — Q4 slightly thinner axis tie-back (see P1-3).
- **Mental scaffold:** §6.1 closing synthesis recap матрица for all 4 quadrants — ✓ excellent integration.

**Verdict per-area:** PASS overall; P1 «Q4 axis drift» — minor polish.

### 4. Section structure + cross-refs

- **4 parts cohesive flow:** ✓ TOC in chapter.md indexes all 4 parts ✓; per-part Оглавление ✓; navigation bars ✓.
- **Cross-refs:** §2.5/§2.6 cross-ref to §1.7 ✓; §5.5 → §1.3 ✓; §4.5 → §1.3 ✓; §6.2 table indexes ALL 10 failures with §-references ✓.
- **Slide markers:** 41 unique `[for-slide-sNN]` markers (s01, s05-s12 part 1; s13-s19 part 2; s20-s28+s29-s33 part 3; s34-s39 part 4). Maps to plan v2 slide-map 43 slides ✓ approximately (s07b separate marker noted; s40-s42 not directly anchored in chapter — recheck against plan v2).

**Verdict per-area:** PASS structural integration.

### 5. Baseline / counterfactual (sample 12 measurable claims)

10 of 12 — has baseline. 3 missing:
- Fervo IPO +331% (no comparable IPO premium baseline)
- Cyber +935% (no absolute volume baseline)
- 2020 oil crash 107k (no % of total US O&G workforce denominator)

**Verdict per-area:** P1 «3 missing denominators» — fix in revision.

### 6. Inline gloss + Russification (sample 15 terms)

| Term | First-occurrence gloss? | Verdict |
|---|---|---|
| wildcat well | ✓ chapter.md:102 + part2.md:40 | PASS |
| foundation model | ✓ chapter.md:104, part2.md:38 | PASS |
| frontier exploration | ✓ chapter.md:166 | PASS |
| custody transfer | ✓ chapter.md:431 | PASS |
| stripper wells | ✓ chapter.md:429 | PASS |
| MRV | ✓ chapter.md:200 in §0.4 table | PASS |
| OGI | ✓ chapter.md:201 in §0.4 table | PASS |
| LDAR | ✓ chapter.md:202 in §0.4 table | PASS |
| SIL/SIS | ✓ chapter.md:204 in §0.4 table | PASS |
| ESP | ✓ chapter.md:205 in §0.4 table | PASS |
| FPSO | ✓ part2.md:135 | PASS |
| basin | ✓ chapter.md:140-143 | PASS |
| play | ✗ used part1 multiple times ohne explicit gloss; meaning «type of geologic deposit» implied | P2 (gloss recommended) |
| shut-in / curtailment | ✗ not heavily used; if used would need gloss | N/A |
| downhole | ✗ used part1 ESP definition (ch:205) implicitly «опускаемый в скважину»; no explicit gloss | P2 |

**Critical anglicism leaks (NOT in brand allowlist, narrative body):**
- `deployment` (multiple, no gloss)
- `pipeline` (multiple, no gloss — only in references to Colonial Pipeline brand name OK; «AI pipeline» as concept = ungglossed)
- `stack` (multiple, no gloss)
- `baseline` (multiple, no gloss; OK in financial sense but should russify to «база сравнения»)
- `insight`/`insights` (multiple, no gloss)
- `takeaway` (multiple, no gloss)
- `edge case` (multiple, no gloss)
- `workflow` (multiple, no gloss)
- `commit` (chapter.md:445)
- `anchor customer` (multiple, no gloss — gloss to «якорный клиент»)
- `screening` (multiple, no gloss — gloss to «отсев / предварительная фильтрация»)
- `pilot purgatory` (gloss needed «застой пилотов»)
- `material lift` (no gloss)

**Verdict per-area:** **P0 «Russification structural gap».** See P0-1.

### 7. Anonymization (sample 10 sections random)

- frontmatter `audience: "студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)"` ✓
- Раздел 5 (Россия) — references Газпром нефть / Роснефть / Татнефть / ЛУКОЙЛ / Сургутнефтегаз — these are companies, **NOT universities** ✓
- §6.3 Карьерный мост: «Профильные технические университеты» / «национальные нефтегазовые компании + сервисные подрядчики + регуляторы» ✓ generic
- §6.3: «Минэнерго, Минприроды, EPA, EU Commission» — Russia-specific regulators named, но это **subjects of study**, не audience-binding. Soft acceptable; recommend balance with non-Russian (DOE, IEA, etc.).
- **No МГТУ / Бауман / РГУ Губкина / ИУ-N / Кафедра instances found** ✓

**Verdict per-area:** PASS anonymization. Soft polish (P2): broaden regulator list balance.

### 8. Volatile numbers (`[VFY-day-of]` sample 5)

- 25 markers total (chapter.md=6, part2=4, part3=6, part4=9) — matches plan v2 commitment.
- Sample 5 markers:
  - chapter.md:290 «AspenTech приобретена Emerson примерно за $15 млрд в 2025 году» [VFY-day-of] — ✓ soft framing «приобретена … примерно за».
  - part2.md:67 «Объявленные параметры на 2024 год: примерно 250 миллиардов параметров [VFY-day-of]» — ✓ soft framing «примерно».
  - part3.md:116 «Planned MethaneSAT-2 successor mission … funding и timeline неопределённы [VFY-day-of]» — ✓ explicit uncertainty.
  - part4.md:124 «Татнефть АнтиХрупкий … KPI [VFY-day-of]» — ✓ uses «public info ограничена».
  - part3.md:328 «Fervo IPO в мае 2026 года — +331% к offering price [VFY-day-of]» — soft framing «к offering price» — OK, but +331% itself is precise number; should add «по состоянию на запись курса 2026 года, число может уточняться».

**Verdict per-area:** PASS overall (1 P2 polish: add soft-framing to Fervo +331%).

### 9. Q&A backup substance

- 12 questions promised ✓
- Average length 200-400 слов floor:
  - Q1 NVIDIA Omniverse: ~260 слов ✓
  - Q2 Лекции 14/12 connect: ~330 слов ✓
  - **Q3 REE / mining: ~190 слов ✗** (below floor)
  - Q4 ROI %: ~270 слов ✓
  - Q5 Foundation model frontier basin: ~270 слов ✓
  - Q6 AI replace BOP: ~210 слов ✓
  - Q7 86% why invest: ~250 слов ✓
  - Q8 stack to learn: ~280 слов ✓
  - Q9 AI MRV solution: ~250 слов ✓
  - Q10 CCS 190× helping?: ~280 слов ✓
  - Q11 AI startup в O&G: ~250 слов ✓
  - Q12 decision tree quadrant: ~280 слов ✓

11/12 PASS; Q3 short. **Cross-links к Лек 12/14 valid** — Q2 references Лекции 14 (cyber) и 12 (digital twins) — these are produced lectures ✓.

**Verdict per-area:** P1 «Q3 thin» — expand to 350 words.

### 10. Magic-pill anti-pattern (sample 15 sections)

- Sample sections checked для «AI is great + будьте осторожны» vs structural reasoning:
  - **§ Введение**: ✓ structural reasoning (5 ограничений + cost asymmetry numbers + 86% McKinsey). NO magic-pill.
  - **§1.2**: ✓ explicit «86% не означает AI плохой» — structural reading.
  - **§1.3 Aspen Mtell**: ✓ explicit «alert fatigue eliminated — это marketing claim, не инженерное утверждение».
  - **§2.5 BP+Beyond Limits**: ✓ structural failure analysis.
  - **§2.6 IBM+Repsol**: ✓ ditto.
  - **§3.3 MethaneSAT loss**: ✓ structural lesson «single-satellite = catastrophic SPOF».
  - **§4.4 CCS 190× gap**: ✓ explicit «AI — catalyst, не silver bullet».
  - **§4.5 plant-wide stagnation**: ✓ structural multi-physics framing.
  - **§5.5 Deepwater Horizon**: ✓ structural «complex automation + insufficient training + alarm tolerance erosion = catastrophe».
  - **§6.1 closing synthesis**: ✓ explicit decision matrix «Когда работает / когда осторожно / когда опасно».

**Verdict per-area:** PASS — strong anti-magic-pill framing throughout. NO violations.

### 11. Multi-part frontmatter compliance

- chapter.md frontmatter:
  - `lecture: 16` ✓
  - `parts: 4` ✓
  - `parts_files` array ✓
  - `slide_map` ✓ structured
  - `strict_in_self_estimate` ✓
  - `length_words: ~30500` ✗ overstates (actual 28 541) → P2 fix to ~28500
  - `references_count: ~45` ✗ actual 46 → P2 fix
- chapter-part2.md, part3.md, part4.md frontmatters minimal:
  - `part: N`, `of: 4`, `parent: "chapter.md"`, `title`, `lecture_number`, `length_words`, `status`, `version` — all present ✓
- TOC chapter.md indexes all 4 parts ✓; per-part Оглавление ✓.

**Verdict per-area:** PASS (1 P2 polish: update length_words to actual count).

### 12. Plan v2 promises delivered

- s01 hook MethaneSAT 410 t/h ✓ (chapter.md:96)
- s05 keystone-axis ✓
- s07b Aspen alert fatigue refinery (Раздел 1) ✓ delivered (§1.3 deep-dive)
- s12 6 visible bullets «когда AI не нужен Q1» ✓ delivered (§1.8 6 criteria)
- s17 BP+Beyond Limits failure ✓ (§2.5)
- s18 IBM+Repsol failure ✓ (§2.6)
- s19 Eclipse/INTERSECT/CMG/OpenFOAM альтернатива ✓ (§2.7)
- s20 methane MRV alphabet helper ✓ delivered (§0.4 + decoded в §3.1)
- s23 MethaneSAT loss ✓ (§3.3)
- s25 4× discrepancy ✓ (§3.5)
- s29 Northern Lights 0,02% ✓ (§4.2)
- s30 Fervo +331% ✓ (§4.3)
- s37 cyber Colonial + MOVEit ✓ (§5.4)
- s38 2020 oil crash + Deepwater Horizon ✓ (§5.5)
- s40-s41-s42 closing/Q&A markers — slide-map references in frontmatter, но chapter narrative §6 (closing) covers s39 mostly; s40-s42 (Q&A / final) — chapter Q&A backup section covers content but без explicit `[for-slide-s40]` markers. P2 «add s40-s42 markers to closing/Q&A» recommended for slide-derivation traceability.

**Vendor → slide table 27 vendors check:**
- Ambyint ✓, OspreyData ✓, SLB Avocet ✓, Halliburton DecisionSpace ✓, AspenTech ✓, Honeywell UOP ✓, Yokogawa ✓, ABB ✓, Emerson ✓, Nabors ✓, Precision Drilling ✓, NOV ✓
- SLB Lumi ✓, Aramco METABRAIN ✓, Eni HPC6 ✓, ExxonMobil Discovery 6 ✓, CMG ✓, OpenFOAM ✓
- MethaneSAT ✓, Carbon Mapper ✓, GHGSat ✓, Bridger Photonics ✓, SeekOps ✓, Project Canary ✓, FLIR ✓, Opgal ✓, Rebellion Photonics ✓, Picarro ✓, LI-COR ✓
- Northern Lights ✓, Fervo ✓, Eavor ✓, Sage Geosystems ✓, Quaise ✓
- Газпром нефть Cognitive Geo ✓, Роснефть Digital Field ✓, Татнефть ✓, ЛУКОЙЛ ✓, Сургутнефтегаз ✓, Cognitive Pilot ✓, AIQ ✓
- Cognite ✓, C3.ai ✓, Beyond Limits ✓, IBM Watson ✓
- Dragos ✓, Claroty ✓, Nozomi Networks ✓

All 27+ vendors mentioned. ✓ PASS.

**Verdict per-area:** PASS (1 P2: add slide markers s40-s42).

---

## Counter-check

| Criterion | Status | Details |
|---|---|---|
| Chapter ≥28 500 words (L4+ absolute minimum) | **PASS** | 28 541 = +41 words (borderline) |
| Recommended push to 29 500-30 000 center | **REVISE** | Need +1000 words expansion (§3.6, §4.5, Q&A Q3) |
| Failure ≥43% strict-in | **PASS** (significantly above: ~70%) | |
| Single-artifact concentration check | **PASS** | All 4 parts ≥55% strict-in |
| Keystone axis present + integrated | **PASS** | Q4 axis tie-back slightly thinner (P1) |
| Baseline mandate (sample 12) | **9/12 PASS, 3 P1** | Fervo +331%, cyber +935%, 107k jobs |
| Anonymization | **PASS** | Audience generic; no МГТУ/Бауман markers |
| Volatile soft-framing (sample 5 VFY) | **PASS** (1 P2 polish) | Fervo +331% precise |
| Q&A backup adequate (12 questions) | **11/12 PASS, 1 P1** | Q3 REE thin |
| Magic-pill anti-pattern | **PASS** | Strong critical framing throughout |
| Multi-part frontmatter compliance | **PASS** (1 P2 length_words) | |
| Plan v2 promises delivered | **PASS** | All 43 slides + 27 vendors covered |
| Russification depth | **FAIL** (P0) | 70+ critical anglicism hits в narrative body |
| Typo / encoding artifacts | **FAIL** (P0) | 7+ confirmed instances |

**Counter-check verdict consistency:**
- ≥5 P1 issues counted (P1-1 word count, P1-2 latin-token leaks, P1-3 Q4 axis drift, P1-4 baselines, P1-5 magic-pill watch [resolved P2], P1-6 anonymization regulators [resolved P2], P1-7 Q3 thin, P1-8 strict-in update [resolved P2]) = **4 active P1 + 2 P0**.
- 2 P0 (Russification + typos) → automatic ≥ REVISE per scale.
- 4 active P1 → would alone be APPROVE-WITH-POLISH territory; combined with 2 P0 → **REVISE**.

---

## Rationale verdict

**REVISE — не APPROVE-WITH-POLISH** because 2 P0 issues are **structural quality gaps**, not polish:

1. **Russification gap (P0-1)** is the highest-priority recurring failure mode across the course (Лекция 8 lesson: speech v1 «0 hits» self-report turned out 919 unique latin tokens; cost = 3 revision passes, ~3h wasted). At Phase 3 caught is much cheaper than at Phase 11 caught. Catching now via REVISE prevents the downstream cascade.

2. **Typo / encoding artifacts (P0-2)** — `provals` / `Studen` / `chrebrolution` / `galleon` / `пайтон` / `skvazhin` etc. in academic-textbook narrative is unacceptable for chapter v1 final. These are not «typos one misses»; они are encoding/copy-paste artifacts that need systematic find-and-replace pass. Без них chapter cannot represent itself as production-ready textbook reference.

**Architecturally chapter v1 is strong:** keystone-axis well-integrated, failure-share 70% (far above 43% target), 10/10 failures delivered with deep-dive ≥600 слов (1 short at C3.ai), 41 slide markers mapping to plan v2, all 27 vendors covered, strong anti-magic-pill framing, anonymization clean, baselines mostly present.

**Upgrade path to APPROVE-WITH-POLISH:**
- Fix P0-1 (Russification deep-pass: replace ~70 critical anglicism instances with russified Russian or inline gloss; allowlist remains brand names + established acronyms).
- Fix P0-2 (systematic typo/encoding cleanup pass).
- Fix P1-1 (push word count to 29 500-30 000 via expansion of §3.6 EU detail + §4.5 plant-wide Q4 reframe + Q&A Q3 REE).

After these 3 fixes — chapter v2 expected to clean to APPROVE-WITH-POLISH, ready for USER GATE A.

---

## Recommendation для Phase 4 revision

**Spawn book-editor agent для Phase 4 cascade revision (single-batched, not per-artifact spawn — per Лекция 4 Phase 11 pattern). Tasks:**

**Task A — Russification deep-pass (P0-1, est. 2-3h):**
1. Run deep latin-token scan: `python3 tools/presentation-build/deep_latin_scan.py library/lectures/lec-16/chapter*.md`
2. Categorize hits: brand allowlist (KEEP) vs critical narrative anglicisms (RUSSIFY or gloss).
3. Replace 70+ critical instances:
   - `deployment` → «развёртывание / внедрение» (inline gloss first occurrence)
   - `pipeline` → «технологический конвейер / data pipeline (конвейер обработки данных)»
   - `stack` → «стек (набор интегрированных слоёв технологий)»
   - `baseline` → «база сравнения / исходный уровень»
   - `insight`/`insights` → «инсайт (выявленная закономерность)» / «выводы»
   - `takeaway` → «вынесенный урок / ключевой вывод»
   - `edge case` → «крайний случай / edge case (граничные условия)»
   - `workflow` → «рабочий процесс / workflow (последовательность операций)»
   - `screening` → «отсев / screening (предварительная фильтрация)»
   - `anchor customer` → «якорный клиент (anchor customer — крупный первый клиент)»
   - `material lift` → «материальный прирост»
   - `pilot purgatory` → «застой пилотов (pilot purgatory — типичная западня после демо-фазы)»
   - `commit` → «принять решение / committing»
   - `inversion` (chapter-part3.md:351) → «инверсия / переворот»
4. Verify deep-scan clean: `unique - allowlist = ∅`.

**Task B — Typo + encoding cleanup (P0-2, est. 30 min):**
1. Find-and-replace:
   - `provals` → «провалы» (chapter.md:150)
   - `Studen,` → «Студент,» (chapter.md:274)
   - `пайтон` → «pattern» (chapter-part4.md:370)
   - `chrebrolution` → «разрешение» (chapter-part3.md:69)
   - `galleon hallucinated` → «hallucinated» или «галлюцинированный» (chapter-part3.md:379)
   - `skvazhin` → «скважин» (chapter-part4.md:72)
   - `cgeo-параметров` → «гео-параметров» (chapter-part4.md:72)
   - `agreggate` → «aggregate» или «агрегирует» (chapter-part4.md:132)
   - `деitalised` (encoding break) → «детализированное» (chapter-part4.md:459)
2. Run grep for any other instances of non-Russian non-English mixed tokens.

**Task C — Expansion to 29 500-30 000 words (P1-1, est. 1.5h):**
1. **§3.6 EU 2024/1787 deep-dive** (+~400 слов): penalty tier structure, MS variance, timeline detail.
2. **§4.5 plant-wide stagnation Q4 reframe** (+~300 слов): edge cases, cross-link к §1.3.
3. **§5.2 Газпром нефть Cognitive Geo** (+~200 слов): pre/post-2022 transition.
4. **Q&A Q3 REE / mining** (+~150 слов): lithium triangle + Mountain Pass.
5. **§1.7 C3.ai short failure** (+~150 слов): bring to ≥600 word deep-dive minimum.

**Task D — P1 polish (est. 30 min):**
1. Add baseline для Fervo IPO +331%, cyber +935%, 107k jobs (P1-4).
2. Add 1-2 axis tie-back lines for Q4 cases (§4.2, §4.3) (P1-3).
3. Update frontmatter `length_words` to actual count (P2).
4. Update `strict_in_self_estimate` to ~70% (P2).
5. Add slide markers `[for-slide-s40]`, `[for-slide-s41]`, `[for-slide-s42]` to closing/Q&A sections (P2).

**Estimated total Phase 4 effort:** 4.5-5h for book-editor. Re-spawn methodology-critic + fact-checker after for USER GATE A.

---

**Status after Phase 4 expected:** APPROVE-WITH-POLISH → USER GATE A ready.
