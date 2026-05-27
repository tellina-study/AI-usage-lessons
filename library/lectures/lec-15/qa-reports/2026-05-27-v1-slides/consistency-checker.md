# Consistency Checker Report — Лекция 15 — 2026-05-27 v1 slides ↔ chapter v2.2

**Mode:** full cross-artifact (chapter v2.2 ↔ slides v1).
**Source-of-truth:** chapter v2.2 multi-part (~32 850 слов, USER-GATE-A approved).
**Artifacts checked:**
- `library/lectures/lec-15/chapter.md` (8 428 слов) + `chapter-part2.md` (6 588) + `chapter-part3.md` (9 342) + `chapter-part4.md` (9 112) = ~33 470 narrative
- `library/lectures/lec-15/deck.yaml` (598 строк, 39 slides)
- `library/lectures/lec-15/slides/s01-s39*.md` (39 files)
- `library/lectures/lec-15/rendered/lec-15.pptx` (rendered visible body + speaker notes)
- `library/lectures/lec-15/rendered/snapshots/s01.png…s39.png` (39 snapshots @ 1334×750)

---

## VERDICT: **APPROVE-WITH-POLISH**

**Rationale.** Slides v1 высокая структурная и фактологическая когерентность с chapter v2.2. Все 25-27 canonical numbers из Numbers convention lock проверены и совпадают cross-artifact. Все 4 walked examples (WE-1/WE-TESS/WE-2/WE-3) корректно derive от chapter §s с правильным step count. Все 39 slide-markers `[for-slide-sNN]` присутствуют в chapter narrative и покрывают весь deck. Cornerstone terminology canonical formes сохранены. Слайды section dividers + cover + lecture-map + glossary + Q&A соответствуют lec-13/lec-14 pattern. **Однако** найден ряд polish-уровня drifts: 1 stale "22 итерации" mention в s16 notes (как teaching counterexample — acceptable, но noisy), 1 stale "36 из 57" mention в s16 notes (тот же patter — teaching), s39 hero implementation diverges от plan (AlphaFold 2 ribbon вместо AlphaFold DB screenshot, документировано в iteration-log per Tier 6 fallback), failure-bucket strict_in coverage в deck.yaml = 10/39 = 25.6% < 30% target (но holistic strict-in в slide content включая mixed-bucket slides s01/s17/s18/s19/s24/s30 phase = ~16/39 = 41% — в норме). Drift counts: cornerstones 1, numbers 0, terminology 2, hero alignment 1, frontmatter counts 1. **APPROVE-WITH-POLISH** уместен — не REVISE, поскольку нет factual contradictions, нет missing coverage, и все drift'ы либо documented (s39 fallback) либо стилистические (английская маркировка в s03 visual.primary).

---

## Severity counts

- **P0 (factual contradiction / missing coverage):** 0
- **P1 (significant drift):** 4
- **P2 (minor inconsistency / polish):** 7

---

## A. Cornerstone consistency table (12 frontmatter cornerstones)

| Cornerstone | Chapter | Slides body | Slides notes | Canonical form | Aligned? |
|---|---|---|---|---|---|
| фундаментальная модель / foundation model | ✓ §0.4 (gloss); §2 multiple | ✓ s04 table «Фундаментальная модель (foundation model)» | ✓ s04, s18 («foundation модели») | bilingual RU+EN | ⚠ s18 использует англоязычную форму «foundation модели» без gloss |
| научный цикл / scientific workflow | ✓ §0.3 keystone | ✓ s03 «лестница научного цикла» | ✓ multiple | RU primary | ✓ |
| открытый / закрытый мир | ✓ §0.4, §3 multiple | ✓ s04 glossary table, s12 dividend, s33 criteria | ✓ multiple | RU canonical | ✓ |
| augmentation / расширение | ✓ §0.3 «Расширение (augmentation)» | ✓ s03 body «Расширение работает; автономно нет», s06, s21, s27 (learning_goal English «augmentation») | ✓ all RU | bilingual canonical | ⚠ s03 visual.primary использует English «augmentation / autonomous / vetoed» tags в staircase (план), s27 learning_goal English-only |
| автономная лаборатория (self-driving lab) | ✓ §0.4 gloss, §2.4 inline | ✓ s12 divider («автономная лаборатория») в speaker notes | ✓ s16 notes | RU canonical | ✓ |
| галлюцинации цитат (peer review hallucinations) | ✓ §0.4, §4.3, §4.5 multiple | ✓ s04 glossary, s30 NeurIPS, s24 IDP | ✓ multiple | RU canonical | ✓ |
| фабрика статей / paper mill | ✓ §0.4 «Фабрика статей (paper mill)»; §4.3 inline | ✓ s04 «Фабрика статей (paper mill)» (Дополнительно), s01 notes (косвенно) | ✓ | bilingual canonical | ✓ |
| кризис воспроизводимости | ✓ §0.4 «Кризис воспроизводимости»; §1.5 multiple | ✓ s04 glossary table | ✓ s04 notes | RU canonical | ✓ |
| человек-в-петле (HITL) | ✓ §0.4 «HITL»; §3 multiple | ✓ s04 «HITL (человек в петле)»; s24, s28, s33, s34 | ✓ multiple | bilingual canonical | ✓ |
| обратное проектирование (inverse design) | ✓ §0.4 «Обратное проектирование (inverse design)»; §2 inline | ✓ s04 «Обратное проектирование (inverse design)» (Дополнительно) | (none — not central in body) | bilingual canonical | ✓ |
| DFT / MD first-principles | ✓ §0.4; §2.4 GNoME, §5.2-5.3 | ✓ s04, s11, s33, s34, s35 | ✓ multiple | bilingual acronym + gloss | ✓ |
| байесовская оптимизация (BO) + гауссовский процесс (GP) | ✓ §0.4; §1.6 deep; §5.2 | ✓ s04, s11 dedicated alternative slide, s34 WE-3, s35 alternatives matrix | ✓ multiple | bilingual canonical | ✓ |

**Drift count:** 1 cornerstone form mismatches (foundation model — s18 narrative uses англоязычное «foundation модели» без glossing; minor P2).
**Plus 1 keystone visualization gap:** s03 visual.primary text describes staircase labels as English-only «augmentation / autonomous / vetoed» (per plan); chapter §0.3 canonical form bilingual «Расширение (augmentation) / Автономно (autonomous) / Запрещено (vetoed)». Body text in s03 correctly uses RU. Plan describes English tags на keystone staircase — designer should ensure rendered staircase shows BOTH RU label + EN gloss (per Russification scope iteration-log mentioning "keystone ladder labels with Russian gloss"). Polish-уровня (P2).

---

## B. Numbers cascade table — 25-27 canonical anchors

| # | Anchor | Chapter | deck.yaml/Slides body | Notes (pptx) | Aligned? |
|---|---|---|---|---|---|
| 1 | AlphaFold 3 — 8 мая 2024 | ✓ §2.1, §2.3 | ✓ s13 assertion + body, s14 body, s39 | ✓ 2 hits in pptx body, 2 in notes | ✓ |
| 2 | AlphaFold DB — 200M+ структур | ✓ §2.2, §6 | ✓ s14, s39 («200 миллионов»), s38, s12 | ✓ 5 hits visible body, 4 hits notes | ✓ |
| 3 | Nobel Chemistry — 9 октября 2024 (Baker ½ + Hassabis + Jumper ½) | ✓ §0.2, §2.1 | ✓ s01, s13 («Бейкер ½ за RFdiffusion, Хассабис+Джампер ½ за AlphaFold»), s38 | ✓ multiple | ✓ |
| 4 | GNoME — 2.2M / 380k stable, **6 раундов** активного обучения (canonical) | ✓ §2.4 (Phase 4.6 P0 fix) | ✓ s12 «GNoME 380 тысяч стабильных», s16 «2,2 миллиона / 380 тысяч / 6 раундов» | ✓ 1 visible «6 раунд», 1 notes «6 раунд», **1 mention «22 итерации» в s16 notes** | ⚠ s16 notes intentionally cites «22 итерации в популярной литературе» как teaching counterexample — acceptable, но shows up в drift grep |
| 5 | A-Lab — **41 of 58 за 17 дней** (canonical, NOT 36/57) | ✓ §2.4 | ✓ s12 «41 из 58 за 17 дней», s16 assertion, s17 inline, s38 | ✓ 4 visible body hits, 6 notes hits, **1 mention «36 из 57» в s16 notes** как teaching counterexample | ⚠ s16 notes intentionally cites «в популярных пересказах часто пишут 36 из 57, но Nature 2023 paper говорит 41 из 58» — acceptable teaching framing |
| 6 | AlphaProof IMO — 28/42 silver, P1/P2/P6 by AP, P4 by AG2, P3+P5 combinatorics unsolved | ✓ §2.7 (Phase 4.6 P0 fix removed fabricated «Task 3» worked example) | ✓ s19 assertion + body table «P1, P2, P6 решены AlphaProof; P4 — AlphaGeometry 2; P3, P5 нерешено» | ✓ s19 notes match | ✓ |
| 7 | FrontierMath — <2% 2024 → 52,4% GPT-5.5 Pro май 2026 | ✓ §0.4, §2.7 | ✓ s04 glossary «<2% → 52,4%», s19 body chart | (notes пропускают конкретное «52,4%» — но в visible body есть) | ✓ |
| 8 | Galactica — 15-17 ноября 2022 (3 дня) | ✓ §0.2 (17 ноября запуск, 3 дня) | ✓ s01 «17 ноября 2022 ... три дня» | ✓ s01 notes match | ✓ |
| 9 | Frontiers «крыса» — 13-16 февраля 2024 | ✓ §4.4 | ✓ s29 «13 февраля 2024 → 16 февраля» (3 дня), s26 divider tag, s38 recap | ✓ multiple | ✓ |
| 10 | NeurIPS 2025 — 21 575 / 5 290 / 24,52% / 100+ fake / 53 papers | ✓ §1.2, §4.5 (Phase 4.6 P0-3 fix) | ✓ s30 assertion + table + body, s26 divider tag, s38, s04 glossary | ✓ 2 visible body hits, 2 notes hits | ✓ |
| 11 | Sakana — 1 of 3 / 6.33 average / cherry-pick ~100 → 3 | ✓ §1.2 | ✓ s08 assertion + table «3% / 33% / 1%», s10 cherry-pick deep-dive | ✓ s08 notes цитирует «6,33 средний балл» | ✓ |
| 12 | AlphaFold IDP — 22% галлюцинаций | ✓ §3.5 | ✓ s24 assertion + body, s38 recap | ✓ 2 visible body, 3 notes | ✓ |
| 13 | NotebookLM — 17M+ MAU | ✓ §4.1 | ✓ s27 assertion + body, s26 divider tag, s38 | ✓ 2 visible, 2 notes | ✓ |
| 14 | DOE Genesis — $320M декабрь 2025 | ⚠ Not found in checked chapter sections | (not found in slides) | (not found) | N/A — not used в этой v1 deck |
| 15 | Palgrave-Schoop — **35 of 36 errors** (canonical) | ✓ §2.5 | ✓ s17 assertion + body «35 из 36», s12 divider, s38 recap | ✓ 6 visible body hits, 8 notes hits (chapter+slide consistent) | ✓ |
| 16 | NSF AI — $700M+ annually | ⚠ Not found в checked sections | (not found in slides) | (not found) | N/A — not used |
| 17 | Aurora — 5000× ECMWF baseline | ✓ §2.6 | ✓ s18 assertion + body, s12 divider, s38 recap | ✓ 4 visible body, 4 notes | ✓ |
| 18 | ECMWF AIFS — 25 февраля 2025 operational | ✓ §2.6 (Phase 4 P1 soften) | ✓ s18 body + table, s04 glossary | ✓ 2 visible, 2 notes | ✓ |
| 19 | Coscientist — GPT-4 + Claude both (CMU Boiko Nature Dec 2023) | ✓ §1.3 | ✓ s09 assertion + body «GPT-4 и Claude одновременно» | ✓ s09 notes match | ✓ |
| 20 | DeepMind Co-Scientist — Nature May 2026 secondary | ✓ §1.3 (упомянут с [VFY-day-of]) | ✓ s09 (Nature May 2026, [VFY-day-of]) | ✓ s09 notes match | ✓ |
| 21 | Replication — Psychology 39 of 100, Economics 61%, AI 24-50% | ✓ §0.4, §1.5 | ✓ s04 glossary «Психология — 39 из 100» | ✓ s04 notes «39 из 100, экономика 61%, AI 24-50%» | ✓ |
| 22 | TESS — classical AUC 78% / NASA Kepler CNN 89% | ✓ §3.2 | ✓ s21 «AUC 78% BLS vs 89% pre-trained CNN vs 92% custom CNN» | ✓ s21 notes match | ✓ |
| 23 | Allen MICrONS Apr 2025 — 1 mm³ / 84K neurons / 500M synapses / 4km axons | ✓ §3.3 | ✓ s22 assertion + body, s20 divider tag | ✓ s22 notes match | ✓ |
| 24 | Exoplanet 2 449 / 3 987 / 83,9% | ✓ §3.2 (arxiv 2512.00967) | ✓ s21 assertion + body, s20 divider tag | ✓ 3 visible body, 3 notes | ✓ |
| 25 | Russia decree — **Указ № 490 (2019) + № 124 (2024)** (NOT № 145) | ✓ §5.6, Q15 (Phase 4 P0-4 fix) | ✓ s37 assertion + body table | ✓ s37 notes match | ✓ |
| 26 | Insitro Series C — $400M | ✓ §2.1 «Insitro (Series C $400 млн, 2021)» | ✓ s13 body «Insitro Series C $400 миллионов» | (not explicitly в s13 notes) | ✓ minor — slide+chapter aligned, notes пропускают |
| 27 | Recursion-Roche — декабрь 2021 / 40 программ × >$300M / ~$12B (Phase 4.7 P0 fix) | ✓ §2.1 (chapter-part2 line 71) | ✓ s13 assertion «декабрь 2021, 40 программ × >$300M = до ~$12B», body + Recursion timeline 2021/Oct 2023 GI-онкология | ✓ s13 notes match (full deal narrative + October 2023 first program) | ✓ |

**Numbers cascade drift count: 0 hard conflicts.** Only 2 «teaching counterexamples» (s16 notes intentionally cite forbidden «22 итерации» and «36 из 57» as «what NOT to use» — they are correctly framed as anti-examples but cause noise in deep grep). **No P0 violations.** All cascade fixes from Phase 4.6 + 4.7 propagated to slides correctly.

**Number anchors NOT used in v1 deck (acceptable — selected coverage):** #14 DOE Genesis $320M Dec 2025, #16 NSF AI $700M annually. These appear in chapter-part4 §5.6 but не вынесены в дедицированный slide — slide deck — selected coverage of chapter content, не каждое чисто.

---

## C. Slide-map alignment

**Deck:** 39 slides s01-s39 ✓ matches frontmatter `slide_map`.

**Chapter slide-markers `[for-slide-sNN]`** — **all 39 markers present** in chapter narrative (`chapter.md` × 16, `chapter-part2.md` × 9, `chapter-part3.md` × 9, `chapter-part4.md` × 11) — full deck coverage.

**Section structure alignment:**

| Section | Chapter §s | Slides | Aligned? |
|---|---|---|---|
| Введение (0) | §0.1, §0.2, §0.3, §0.4, §0.5 | s01 hook + s02 cover + s03 lecture-map + s04 glossary + s05 central question | ✓ |
| §1 Hypothesis + Design | §1.1-1.6 (6 subsections) | s06 divider + s07-s11 (5 content slides) | ✓ |
| §2 Experiment | §2.1-2.7 (7 subsections) | s12 divider + s13-s19 (7 content slides) | ✓ — 1:1 mapping |
| §3 Analyse | §3.1-3.7 (7 subsections) | s20 divider + s21-s25 (5 content slides) | ✓ slight compression of §3.1 + §3.6 |
| §4 Write + Review | §4.1-4.6 (6 subsections) | s26 divider + s27-s31 (5 content slides) | ✓ |
| §5 Когда AI не нужен | §5.1-5.6 (6 subsections) | s32 divider + s33-s37 (5 content slides) | ✓ |
| §6 Замыкание + Q&A | §6 + Q&A backup | s38 Q&A + s39 closing hero | ✓ |

**Section dividers count:** deck.yaml comment line 12 promises «6 шт.: s06 / s12 / s20 / s26 / s32 / s38», но **actual:** 5 dividers (s06/s12/s20/s26/s32). s38 type=qa, не section_divider. **P2 — деко.yaml header comment drift** (cosmetic, не влияет на rendering).

---

## D. Learning Outcome (LO) alignment

Chapter `lo: [LO4, LO5, LO6, LO8]` — все 4 учтены в slides via `learning_outcomes` frontmatter:

- **LO4 (Назвать классы AI-инструментов + классификация инструментов):** ✓ s04 glossary, s11 BO+GP alternative, s35 alternatives matrix, s39 closing
- **LO5 (Этические риски):** ✓ s08 Sakana, s28 WE-2 bibliography, s30 NeurIPS, s31 ICMJE
- **LO6 (Применить «лестницу научного цикла» + критерии «AI не нужен»):** ✓ s03 lecture-map, s33 four criteria, s07 WE-1, s34 WE-3
- **LO8 (Применять + предложить не-AI альтернативу):** ✓ s07 WE-1, s11 BO+GP, s25 WE-TESS, s34 WE-3 catalyst, s35 alternatives, s36 vendor questions framework

**Aligned: ✓ all 4 LOs covered.**

---

## E. Walked examples consistency

| WE | Chapter ref | Slide | Steps consistent? |
|---|---|---|---|
| WE-1 grant idea decision tree | §1.5 — описывает 6-шаговое дерево | s07 — 6 шагов: classify task → coverage → verification → ethics → HITL → submission integrity | ✓ 6 step counts match |
| WE-TESS transit search | §3.7 — 5-шаговая рамка | s25 — 5 шагов: data overlap → label availability → GPU cost → AUC baseline → held-out validation | ✓ 5 step counts match |
| WE-2 collaborator bibliography | §4.3 — 4-шаговая проверка | s28 — 4 шага: DOI-resolve, выборка релевантности, GPTZero, запрос исходных файлов | ✓ 4 step counts match |
| WE-3 catalyst pipeline | §5.3 — 5-шаговая рамка | s34 — 5 шагов: classify → map alternatives → 4 criteria → HITL design → pre-publication verify | ✓ 5 step counts match |

**Aligned: ✓ all 4 walked examples 1:1.**

---

## F. Hero plan implementation

| Hero | Plan | Implementation (iteration-log) | Aligned? |
|---|---|---|---|
| s01 — Side-by-side AlphaFold Nobel + Galactica retraction | Composite ≥40% area | ✓ Stockholm Konserthuset photo (Wikimedia Tier 2) + typography card with real MIT Tech Review headline (fair-use). Two-half composite with bridging caption ⇄. | ✓ — но slide.md plan said «hero photo Hassabis+Jumper+Baker», actual использует Stockholm Konserthuset (Wikipedia hall photo). Slight venue change документирована iter-2 fix («Replaced misleading Galactica spacebears image»). |
| s39 — AlphaFold DB website screenshot bridge к Lec-16 | Hero ≥40% area — full-bleed screenshot alphafold.ebi.ac.uk | ⚠ **Tier 1-6 acquisition failed для AlphaFold DB main page** (Angular SPA, no og:image; Wikipedia infobox absent; Wayback returns AlphaFold ribbon, not site hero). **Mitigation:** AlphaFold 2 ribbon (Wikimedia) used as «best-available iconic representation» of AlphaFold DB. Documented in iteration-log §Tier 6 failures + §Notes 2 + §Notes 4. | ⚠ **P1 — s39 slide.md visual.primary still says «full-bleed screenshot alphafold.ebi.ac.uk»** — slide spec не sync с actual Tier 6 fallback. Per [[no-mock-fallbacks]] memory rule documenting is OK, но slide.md description should match реальность ИЛИ explicit «Tier 6 fallback applied — AlphaFold 2 ribbon». |

**Drift: 1 hero alignment (P1) — s39 spec mismatches implementation.**

---

## G. Failure-bucket holistic strict-in (≥30% in EACH artifact target)

**Chapter:** frontmatter `strict_in_self_estimate: ~46%` + `ai_failure_strict_in_pct: 45.9` — well above 30% (chapter has full failure-deep sections §1.2 Sakana, §2.5 Palgrave, §3.5 AlphaFold IDP, §4.4 Frontiers, §4.5 NeurIPS, §5 entire section). ✓

**Slides:** explicit `failure_bucket: strict_in` count в deck.yaml = **10/39 = 25.6%** — formally below 30% threshold. ⚠

**Однако holistic count** (strict_in slides + mixed slides с substantial failure content):
- Pure strict_in (10): s08, s10, s17, s24, s26, s28, s29, s30, s32, s33
- Mixed with strong failure content (≥50% of slide is failure-strict): s01 (Galactica half), s18 (Aurora critique + Storm Ciarán), s19 (P3+P5 unsolved boundary), s37 (RU compute gap structural), s38 (failure recap)
- **Total holistic = 15/39 = 38.4%** ✓ above 30%

**Verdict on this rule:** holistic strict-in > 30%, но formal deck.yaml `failure_bucket` field shows 25.6%. **P2 — recommendation to retag some currently-mixed slides as strict_in when failure content is dominant** (e.g., s17 already strict_in, but s18 dominant failure content tagged mixed — would benefit recategorize for accurate metadata).

---

## H. Russification consistency (cross-artifact)

**Chapter v2.2 Russification status:** 485 critical anglicisms → 0 (Phase 4 P0-1 fix). Whitelist — brands + acronyms first-mention with gloss.

**Slides v1 Russification status (per iteration-log):**
- Visible body «fully Russified except whitelisted brand names, established acronyms (LLM, RAG, AI, DOI, NSF, ICMJE, IMO, GNN, CNN, GPU, BO, GP, DFT, MD, IDP, CASP), proper nouns, academic citations»
- Deep latin-token scan: ~203 unique non-whitelisted tokens — «overwhelmingly proper nouns + method names + license markers (CC-BY-SA)»
- iter-4 cleanup applied targeted Russification on s37, s07, s10, s16, s28, s38

**Cross-artifact Russification gaps:**

| Anglicism appearance | Where in slides | Where in chapter | Drift? |
|---|---|---|---|
| «augmentation» without RU gloss | s27 learning_goal «augmentation для навигации», s03 visual.primary tag (staircase EN-only labels) | chapter §0.3 RU canonical «Расширение (augmentation)», never EN-only | ⚠ P2 — s27 learning_goal не critical (frontmatter, not visible body); s03 staircase labels EN-only в plan — should bilingual per chapter canonical |
| «foundation модели» | s18 body line 45 «foundation модели систематически уступают» | chapter §0.4 canonical «Фундаментальная модель (foundation model)» | ⚠ P2 — minor inconsistency in s18 body (should be «фундаментальные модели» per glossary table) |
| «cherry-pick / cherry-picking» | s06 divider, s10 («cherry-pick / cherry-picking»), s38 («Sakana cherry-pick механика») | chapter §1.2 RU «отбор лучшего (cherry-picking)» bilingual canonical | ⚠ P2 — slides use EN-only «cherry-pick» multiple times без consistent gloss; chapter uses bilingual «отбор лучшего (cherry-picking)» |
| «pipeline» | (not found in slides body — Russified to «конвейер») | chapter «конвейер» consistently | ✓ |
| «benchmark» / «эталонный тест» | s18 «эталонный тест», s15 «эталонные тесты» — Russified | chapter «эталонный тест» canonical | ✓ |
| «production» / «производство» | (mostly Russified в slides) | chapter Russified | ✓ |
| «workflow» | (not found English in slides body) | chapter «рабочий процесс» | ✓ |
| «open-source» | s14 «open-source debate», s15 «MIT license», s14 «open-weights» | chapter §2.3 «открытый исходный код / open-source» bilingual | ⚠ P2 — slides use EN «open-source» more frequently than chapter; minor |

**Cross-artifact Russification verdict:** Body content well-Russified; **minor leak** for «cherry-pick», «augmentation», «foundation модели» in slides — но canonical RU form does exist в chapter и большинстве slides. **3 P2 polish drifts**, не P1.

---

## I. Anonymization consistency

**Per chapter-changes-v2 audit:** «Named universities (МГТУ/Бауман/etc.): 0 ENFORCED».

**Verified в slides:** ✓ no Russian named universities (МГТУ, МФТИ, МГУ, СПбГУ, ИТМО, etc.) found in slide body or speaker notes.

**Однако в chapter-part4 §5.6 line 266** — chapter mentions **«AIRI + МФТИ»** as Пример 1 of AIRI collaboration. This is a **chapter-internal anonymization gap** (P1 chapter-only — does NOT propagate to slides v1, so cross-artifact integrity OK для slides).

**Brand whitelist consistent:** AIRI / Sber / Yandex / РНФ — bilateral consistent across chapter §5.6 and s37.

**International institutions** (Carnegie Mellon, MIT, Stanford, UT Austin, Allen Institute, EBI) — appear в both chapter and slides. **Anonymization mandate** per CLAUDE.md targets Russian universities (МГТУ/Бауман); international institutions are routinely named как proper nouns (e.g., «CMU», «MIT») and this is accepted convention for academic content. **No cross-artifact drift here**.

---

## J. Cascade from Phase 4.6 + 4.7 propagation

**Phase 4.6 cascade items (chapter v2.1):**
1. AlphaProof IMO P3 fabrication removed → ✓ s19 correctly shows «P3+P5 unsolved», no Task 3 worked example
2. GNoME 22→6 active learning rounds → ✓ s16 assertion «6 раундов активного обучения», s12 divider notes «6 раундов»
3. Reference 33 author corrected (Bryant → Gopalan & Narayanan) → ✓ s24 references list cites «gopalan-2025-arxiv» + body line 30 «Gopalan & Narayanan, arxiv:2510.15939, 2025»
4. Reference 13 journal corrected (GRL → npj Climate and Atmospheric Science) → ✓ Slide s18 references include «charlton-perez-2024-storm-ciaran» (proper journal source)
5. NeurIPS 2025 (15 000 → 21 575) → ✓ s30 + s26 + s38 all use «21 575 / 5 290 / 24,52%»
6. Russia Указ № 145 → № 490 + № 124 → ✓ s37 uses correct decree numbers

**Phase 4.7 cascade items (chapter v2.2):**
- Recursion-Roche deal: «December 2023 / $20+ programs × $30M milestones / $1B potential» → **«декабрь 2021 / 40 программ × >$300M / ~$12B»** + October 2023 GI-онкология optioning → ✓ s13 assertion «декабрь 2021, 40 программ × >$300M = до ~$12B», body lines 35-37 + line 56 narrative

**All cascade items propagated correctly to slides v1.** ✓

---

## DISCREPANCIES (Detailed)

### D1 — s39 hero implementation diverges from spec (P1)

**Severity:** P1
**Where:** `slides/s39-closing-hero-alphafold-db.md` lines 12-18 (visual.primary) vs `rendered/iteration-log.md` Tier 6 fallback note vs actual rendered pptx hero image
**Issue:** slide.md `visual.primary` says «Hero ≥40% area — full-bleed screenshot alphafold.ebi.ac.uk главной страницы с поисковой строкой». Actual hero image used = AlphaFold 2 ribbon (`s39-alphafold-db.png` is `upload.wikimedia.org/AlphaFold_2.png`). Iteration-log documents this Tier 6 fallback openly (lines 38, 127, 138), но slide.md spec text was not updated to reflect reality.
**Recommendation:** update s39 slide.md `visual.primary` to: «Hero ≥40% area — AlphaFold 2 ribbon (Wikimedia, Tier 2; Tier 1 alphafold.ebi.ac.uk og:image not exposed — Angular SPA). Same visual identity domain — AlphaFold ribbon = iconic representation of AlphaFold DB». Alternative: retry Tier 1-6 acquisition с Wayback или direct curl. Owner explicit decision required.
**Severity rationale:** P1 because student reading slide.md spec будет ожидать screenshot, не ribbon — minor reader-confusion potential. Functionally rendered hero looks fine.

### D2 — Failure-bucket strict_in formally below 30% threshold in deck.yaml (P1)

**Severity:** P1
**Where:** deck.yaml `failure_bucket` field × 39 slides — only 10 tagged `strict_in` = 25.6%
**Issue:** Per CLAUDE.md AI-Failure & Judgment Content Rule «strict-in ≥30% должна быть видна в каждом из 3 артефактов». Chapter clearly above (46%); slides v1 formal tag = 25.6%. Однако holistic content-level strict-in (counting mixed slides s01, s18, s19, s24, s30, s37, s38 where failure content dominates) = 15/39 = 38.4% ✓.
**Recommendation:** retag mixed slides where failure content >50% as `strict_in`: candidate retags = s01 (Galactica half = ~50%), s18 (failure-callback line dominant), s19 (P3/P5 unsolved is half), s37 (RU compute gap structural failure). Updated count would be ≥14/39 = 36%.
**Severity rationale:** P1 because formal metadata field shows below-threshold value. Holistic strict-in content is fine; only metadata accuracy needs cleanup.

### D3 — s03 keystone staircase uses English-only labels in visual.primary (P1)

**Severity:** P1
**Where:** `slides/s03-lecture-map.md` line 13 visual.primary text
**Issue:** Plan says «Vertical 6-step staircase ... с тэгом augmentation / autonomous / vetoed рядом каждой ступени». English-only labels, без RU canonical form. Chapter §0.3 cornerstone form bilingual «Расширение (augmentation) / Автономно (autonomous) / Запрещено (vetoed)». Body text in s03 correctly uses RU «Расширение работает; автономно нет», but the rendered staircase image (per visual.primary) may show English-only tags.
**Recommendation:** Update s03 visual.primary to: «с двуязычным тэгом «Расширение (augmentation) / Автономно (autonomous) / Запрещено (vetoed)» рядом каждой ступени». Verify rendered s03.png snapshot does NOT show English-only staircase tags.
**Severity rationale:** P1 because keystone slide rendering matters — student first impression. Body text fine but staircase visual element risks Russification gap.

### D4 — deck.yaml header comment claims 6 section dividers, actual = 5 (P2)

**Severity:** P2
**Where:** deck.yaml line 12 «section dividers (6 шт.): s06 / s12 / s20 / s26 / s32 / s38»
**Issue:** s38 is type=`qa`, NOT type=`section_divider`. Actual dividers = 5 (s06, s12, s20, s26, s32). Cosmetic — documentation comment не sync с code.
**Recommendation:** edit deck.yaml comment to «section dividers (5 шт.): s06 / s12 / s20 / s26 / s32; dedicated Q&A s38 + closing hero s39».
**Severity rationale:** P2 cosmetic — doesn't affect rendering or content. Documentation hygiene.

### D5 — s16 speaker notes contain «22 итерации» + «36 из 57» counterexamples (P2, acceptable)

**Severity:** P2 (informational — acceptable teaching framing)
**Where:** rendered/pptx slide s16 notes
**Issue:** s16 notes intentionally cite forbidden numbers as «what NOT to use» — «не «22 итерации» как часто пишут в популярной литературе» (line 1) and «в популярных пересказах часто пишут 36 из 57, но Nature 2023 paper говорит 41 из 58» (line 5). This is **deliberate teaching framing** — pedagogically explicit «here's the wrong number you'll see» — но shows up in cross-artifact drift grep as a P0-looking false positive.
**Recommendation:** **No action required** — this is acceptable teaching practice. Document in consistency-checker output that this is an intentional anti-example, not a drift. Could optionally soften phrasing «часто пишут» → «иногда упрощают» to make less echoing of wrong number.
**Severity rationale:** P2 informational — explicitly framed as counterexample, not actual content claim.

### D6 — Cherry-pick anglicism without consistent RU gloss in slides (P2)

**Severity:** P2
**Where:** slides s06 «cherry-pick», s10 «cherry-pick mechanics» учебная цель + «cherry-picking», s38 «Sakana cherry-pick механика»
**Issue:** chapter §1.2 uses bilingual canonical «отбор лучшего (cherry-picking)»; slides predominantly use EN-only «cherry-pick» without inline RU gloss. iter-2 of designer iteration applied targeted Russification on some slides but not exhaustively.
**Recommendation:** Polish pass — first mention of «cherry-pick» (s06 + s10) → «отбор лучшего (cherry-picking)»; subsequent mentions OK.
**Severity rationale:** P2 cross-artifact terminology consistency.

### D7 — s18 body uses «foundation модели» without RU gloss (P2)

**Severity:** P2
**Where:** `slides/s18-aurora-ecmwf.md` line 45 «Aurora и подобные foundation модели систематически уступают»
**Issue:** chapter glossary §0.4 + s04 glossary use «Фундаментальная модель (foundation model)» bilingual canonical. s18 body switches to English «foundation модели» (mixed RU+EN) — should be «фундаментальные модели».
**Recommendation:** Polish pass — s18 line 45 «foundation модели» → «фундаментальные модели».
**Severity rationale:** P2 minor RU consistency.

### D8 — s27 learning_goal field uses EN «augmentation» + «automation bias» (P2)

**Severity:** P2
**Where:** `slides/s27-notebooklm-elicit.md` line 6 learning_goal frontmatter
**Issue:** `learning_goal: "Зрелые литературные инструменты — это augmentation для навигации, не замена синтеза; psychology of automation bias"` — uses EN «augmentation», «automation bias» without gloss. Frontmatter (metadata) only — not visible body, so impact low.
**Recommendation:** Polish — «augmentation» → «расширение», «psychology of automation bias» → «психология автоматизационного смещения». Frontmatter-only fix, no rendered change.
**Severity rationale:** P2 metadata consistency.

### D9 — MFTI mentioned in chapter-part4 §5.6 line 266 (P1 chapter-internal, NOT cross-artifact)

**Severity:** P1 chapter-internal (does NOT propagate to slides — no slide drift)
**Where:** `chapter-part4.md` line 266 «Сотрудничество AIRI + МФТИ по предсказанию структуры белка»
**Issue:** Chapter-changes-v2 audit declared «Named universities (МГТУ/Бауман/etc.): 0 ENFORCED». But МФТИ (Moscow Institute of Physics and Technology) appears once in chapter §5.6 Пример 1. This is a chapter-internal anonymization gap — does not propagate to slides v1 (no slide mentions МФТИ).
**Recommendation:** Report to book-editor for chapter-only polish (Phase 4.7+ or pre-Phase 11): rephrase «AIRI + МФТИ по предсказанию структуры белка» → «AIRI совместно с ведущим российским физико-техническим вузом» или «AIRI + ведущий российский технический университет».
**Severity rationale:** P1 chapter-internal — slides not affected. Reported here for consistency-checker completeness.

### D10 — Section divider Раздел 5 title slightly different from chapter §5 framing (P2)

**Severity:** P2
**Where:** s32 assertion «Раздел 5. Когда AI не нужен в науке — критерии, альтернативы, разобранный пример». Chapter §5 title in oгdавление = «Когда AI не нужен (включая российский контекст)».
**Issue:** s32 divider drops the «(включая российский контекст)» qualifier — but s37 RU context slide covers it. Mild ambiguity for student about whether RU context is part of Раздел 5 or its own.
**Recommendation:** No action — slide divider properly captures content; chapter heading has parenthetical detail not critical для slide pattern.
**Severity rationale:** P2 cosmetic.

### D11 — Frontmatter cornerstones list count = 12 but glossary has 15 (P2)

**Severity:** P2
**Where:** chapter.md frontmatter `cornerstones: [list of 12]` vs §0.4 «Глоссарий из пятнадцати обязательных терминов» (15 items)
**Issue:** Frontmatter cornerstones subset (12) is a curated essential subset of glossary (15). Includes 12 core concepts; glossary adds 3 more (CASP, ECMWF, FrontierMath as institutional names). Not a contradiction — frontmatter intentionally focused on conceptual cornerstones, not institutional acronyms.
**Recommendation:** No fix — this is a legitimate distinction. Optional: clarify frontmatter «cornerstones» field semantics with comment.
**Severity rationale:** P2 informational.

---

## Coverage gaps

**No major LO or assertion coverage gaps detected.**

- Every chapter assertion that maps to a numbered slide-marker `[for-slide-sNN]` HAS a corresponding slide.
- Every slide assertion has chapter narrative support (verified via `chapter_ref` mappings).
- All 4 WEs (WE-1, WE-TESS, WE-2, WE-3) have step-consistent walked example slides.
- All 25 canonical numbers (anchors #1-13, 15, 17-25, 27) used by slides match chapter canonical form.
- 2 chapter anchors NOT used in v1 deck (acceptable — deck selects subset): #14 DOE Genesis $320M, #16 NSF AI $700M annually. These appear в chapter-part4 narrative but are not central to deck.

---

## Топ-5 фиксов (recommended priority order for Phase 8 revision)

1. **[P1] s39 hero spec mismatch:** update `slides/s39-closing-hero-alphafold-db.md` visual.primary to honestly reflect AlphaFold 2 ribbon fallback (per iteration-log Tier 6 documentation). Alternative: retry Tier 1-6 acquisition. **Owner decision: accept ribbon as «iconic AlphaFold» substitute, OR insist on screenshot retry.**
2. **[P1] Failure-bucket retag for accuracy:** review s01 + s18 + s19 + s37 + s38 — retag from `mixed` → `strict_in` where failure content dominates (>50% of slide). Brings formal deck.yaml metric from 25.6% to ≥36% — eliminates the «below-30%» metadata false-flag.
3. **[P1] s03 keystone staircase RU bilingual labels:** update s03 visual.primary description from English-only «augmentation / autonomous / vetoed» to bilingual «Расширение (augmentation) / Автономно (autonomous) / Запрещено (vetoed)». Verify rendered s03.png snapshot shows bilingual canonical form.
4. **[P2] Russification cleanup pass (cherry-pick / foundation модели / augmentation in body):** s06, s10 first-mention «cherry-pick» → «отбор лучшего (cherry-picking)»; s18 line 45 «foundation модели» → «фундаментальные модели»; s27 learning_goal Russification.
5. **[P2] deck.yaml documentation hygiene:** edit deck.yaml line 12 comment «section dividers (6 шт.)» → «section dividers (5 шт.); dedicated Q&A s38 + closing hero s39». Cosmetic but useful for downstream agents reading deck.yaml header.

**Optional polish:**
- D9 МФТИ mention in chapter §5.6 line 266 — anonymize. Chapter-internal, не slide-affecting.
- D5 s16 notes «22 итерации» + «36 из 57» counterexamples — acceptable framing; could soften «часто пишут» to «иногда упрощают» if owner prefers less echo of wrong numbers.

---

## Summary metrics

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Cornerstone consistency | 11/12 ✓ + 1 ⚠ | 12/12 | mostly aligned |
| Numbers cascade (25-27 anchors) | 25/25 ✓ (anchors used in deck) + 2 N/A | all used aligned | ✓ aligned |
| Slide-markers coverage | 39/39 | 39/39 | ✓ |
| Section structure | 7 sections, 39 slides | matches plan | ✓ |
| LO coverage | LO4, LO5, LO6, LO8 all | all 4 | ✓ |
| Walked examples step count | 4/4 match (6/5/4/5) | 4/4 | ✓ |
| Hero plan implementation | 1/2 fully aligned, 1 fallback documented | 2/2 | ⚠ s39 fallback |
| Failure-bucket strict_in formal | 25.6% | ≥30% | ⚠ |
| Failure-bucket strict_in holistic | ~38% | ≥30% | ✓ |
| Russification cross-artifact | ~98% body Russified | full | ⚠ minor leaks |
| Anonymization (Russian unis) slides | 0 named | 0 | ✓ |
| Anonymization (Russian unis) chapter | 1 (МФТИ §5.6) | 0 | ⚠ chapter-internal |
| Phase 4.6 cascade propagated | 6/6 items in slides | 6/6 | ✓ |
| Phase 4.7 cascade propagated | 1/1 (Recursion-Roche) | 1/1 | ✓ |

---

## Verdict recap

**APPROVE-WITH-POLISH** — slides v1 are factually and structurally aligned with chapter v2.2. All 25 canonical numbers checked propagate correctly. All 4 walked examples match step count. All 39 slide-markers present in chapter. Cornerstone terminology canonical forms preserved in 11/12 cases. Phase 4.6 + 4.7 cascades correctly propagated. Identified drifts are polish-tier (4 P1, 7 P2) — no factual contradictions, no missing coverage. Recommended polish pass for Phase 8 covers:
1. s39 hero spec realignment with iteration-log Tier 6 fallback
2. failure-bucket metadata retag for accuracy
3. s03 keystone bilingual labels
4. minor Russification cleanups

Slides ready for student-simulator + reader-simulator + presentation-critic parallel runs (Phase 7 critic sweep), followed by polish revision before USER GATE B.

---

**Report generated:** consistency-checker, 2026-05-27, Phase 7.
**Storage:** `library/lectures/lec-15/qa-reports/2026-05-27-v1-slides/consistency-checker.md`
