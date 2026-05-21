# Consistency Checker Report — Лекция 11 — 2026-05-21 (Phase 10 full triplet)

**Scope:** chapter v5 (3 parts) ↔ slides v2.1 (41) ↔ speech v1 (5157 words).
**Mode:** full cross-artifact alignment.
**Severity counts:** P0 = 3, P1 = 6, P2 = 7.

## 1. Verdict

**REVISE** — Speech v1 хорошо повторяет chapter narrative и slide-order, but на 3 critical артефакт-pair'ах есть P0 числовые/структурные drift'ы, которые **видны студенту в зале** (категории criteria 10 vs 11, brewery rate 30k vs 60k bottles/hr, vendor questions count 5 vs 4 vs 3+OEE). Это **fix-able в Phase 11 polishing** одним batched edit (правки в slides s32/s34c/s35/s38), но не должно проходить через USER GATE C как есть.

Speech v1 как standalone artifact — strong (см. presentation-critic). Cross-artifact с chapter и slides — drift на структурных якорях, на которых студент будет фокусироваться (рамка решения, vendor questions).

## 2. Top-line summary

- **Cornerstones (10 terms):** все 10 присутствуют в каждом из 3 артефактов с consistent terminology. Minor typographic drift OT/IT — chapter Latin, speech Cyrillic «ОТ и ИТ» (P2).
- **Central question:** identical phrasing в chapter §intro, deck.yaml `central_question`, slide s05, speech opening — **clean**.
- **Numbers (sampled 18):** 15/18 consistent. 3 drift: brewery rate (chapter 30k vs slides/speech 60k = **P0**), Foxconn jobs count (slide 10k vs speech 13k vs chapter 10k contract + 13k potential = **P1**), F-35 ALIS FY2024 figure ($35k missing from speech and slide s27 = **P1**).
- **3 worked examples:** Pfizer Vox + авиадвигатель + brewery — все три present в chapter + slides + speech. Same shape (5-step framework walk). Defect descriptions для brewery diverge между chapter и slides/speech.
- **5-step framework:** consistent steps, names. Slide s35 uses anglophone step labels («Identify class / Map alternatives»), speech uses Russian — typographic drift only.
- **4 categories criteria:** **chapter 10+1 vs slide s32 «11 criteria» vs speech 10 + bonus** — это P0 structural drift на самом payoff слайде лекции.
- **Vendor questions:** **chapter+speech = 5 questions; slide s35 = 4; slide s38 = 5 but with different Q5 («архитектурный класс» vs «прошлые провалы»)** — P0 drift.
- **Roadmap:** 5 sections, identical labels — clean.
- **Attributions:** Musk April 2018, Bainbridge 1983, Toyoda 1924/1925, Toyota GAIA, «8th wonder», Foxconn Young Liu Computex 2025 — все consistent. Minor: slide s21 has Russified «Молодой Лю» (transliteration error of name «Young») vs «Янг Лю» в chapter/speech (P2).
- **References:** chapter has 105 inline sources; speech doesn't cite inline (correct — это spoken format), references stable. No orphan citations.
- **Bridge к Лекции 12:** consistent across chapter §5.3 + slide s39 + speech [s39]. Slight gap: slide s39 mentions Holcim digital-twin + Foxconn-NVIDIA Omniverse, speech mentions only BMW (P2).
- **Pre-flight checklist:** 8 slide references (s01, s07, s08, s10, s11, s12, s19, s21, s25, s28, s32, s34b) — **all valid in deck.yaml**, no orphan refs.

## 3. Cornerstones drift report (3 artifacts)

| Canonical term | Chapter | Slides | Speech | Aligned? |
|---|---|---|---|---|
| Дискретное / процессное производство | 17/15 × | 41 slides body | 19 × | ✓ clean |
| Прогностическое обслуживание (PdM) | 6× «прогн. обсл.»; en «PdM» 2× | s17 «PdM», s27 «edge PdM» | «прогностическое обслуживание» 8× | ✓ clean |
| Компьютерное зрение для контроля качества (CV) | «компьютерное зрение», «CV» mixed | s14/s15/s20 «CV» в slide bodies | «компьютерное зрение» dominant; «CV» 0 | ✓ acceptable (speech avoids CV abbrev intentionally) |
| Мягкий сенсор / soft sensor | 43× combined | s24 body | «мягкий сенсор» 5× | ✓ clean |
| Обучение с подкреплением (RL) | «RL» дominant | s25/s26 «RL» | «обучение с подкреплением» в первом mention, далее «RL» | ✓ acceptable |
| ISA-95 | 12× | s04 glossary, s27 mention | s04 ref + body | ✓ clean |
| OEE | 47× combined | s07/s17/s32/s38 | 11× + «OEE-вопрос» | ✓ clean (component names «доступность / производительность / качество» triple-aligned) |
| Эталонная разметка (ground truth labelling) | 26× | s14/s16/s22 | 6× | ✓ clean — chapter introduces parenthetical «(ground truth labelling)»; slides + speech use Russian short form |
| Застревание на пилотной стадии (pilot purgatory) | 12× combined | s07/s32 «pilot purgatory» (slide bodies use English term) | «застряли на пилоте» 2×, also «pilot purgatory» 1× | ✓ acceptable (chapter is canonical RU, slides import EN, speech uses RU paraphrase) |
| Раскол OT/IT | «OT/IT» Latin in chapter | s09 title «OT/IT раскол» (Latin) | «ОТ и ИТ», «ОТ-стороне» Cyrillic в speech body | **P2 typographic drift** |

**Typographic drift (P2):** OT/IT — chapter Latin throughout (`OT/IT-раскол`, `OT/IT-граница`), slide s09 Latin in title, speech uses **Cyrillic** «ОТ и ИТ» в spoken body. Same concept, no semantic divergence. Recommended fix: keep speech Cyrillic (more natural spoken), but explicitly add note in glossary slide s04 OR pre-flight checklist «произносится "о-тэ" и "ай-тэ"».

## 4. Central question unified?

**✓ YES.**

- Chapter §intro line 92: «Где AI работает, где не работает, и как инженер должен решать?»
- deck.yaml `central_question`: «Где AI работает в производстве, где не работает — и как инженер должен решать, в какой колонне он работает (дискретное / процессное) и какой AI-стек применим?»
- Slide s05 keystone bottom (re-stated visually as 2 columns + universal belt).
- Speech [s01] line 105: «где ИИ работает, где не работает, и как инженер должен решать?»

Three artifacts восстанавливают **identical core formulation**. Slide s05 is the visual operationalization; deck.yaml expands with the discrete/process axis. Clean alignment.

## 5. Numbers drift report (sample of 18 cornerstone facts)

| Fact | Chapter | Slide | Speech | Aligned? |
|---|---|---|---|---|
| McKinsey 78% / 5,5% high performers | §1.1 ✓ | s07 ✓ | line 171 ✓ | ✓ |
| MIT Sloan 95% pilots fail | §intro + §1.1 ✓ | s07/s05 ✓ | line 101, 173 ✓ | ✓ |
| RAND 80,3% | §intro + §1.1 ✓ | s07 ✓ | line 101 ✓ | ✓ |
| S&P 46% / $7M sunk | §1.1 ✓ | not on s07 body | not in speech | **P2 missing in slide+speech** |
| Markets&Markets $34B → $155B | §intro + §1.1 ✓ | s08 ✓ | line 191 ✓ | ✓ |
| Fortune Business Insights $7,6B | §1.1 ✓ | s08 ✓ | line 191 ✓ | ✓ |
| Precedence Research $8,57B | §1.1 ✓ | s08 ✓ | line 191 ✓ | ✓ |
| IBM Watson $4B + sold $1,065B Jan 2022 | §1.3 ✓ ($4B inv, ~$1B sale) | s12 «$4B sunk» | line 261 «миллиард с небольшим, 20% от потраченного» | ✓ |
| GE Predix $4B+ | §1.3 ✓ | s12 ✓ | line 99, 259 ✓ | ✓ |
| Foxconn Wisconsin 3B subsidies / 10000 jobs / 13000 potential | §1.3 ✓ (13k potential, 10k contract) | s12 «10 000 рабочих мест» | line 99 «10000» / line 263 «13000» | **P1 drift in speech**: line 263 says «тринадцать тысяч рабочих мест» as the headline figure (chapter clarifies 13k potential vs 10k contract). Slide says only 10k. Speech opening line 99 says «10 000». Internal speech inconsistency too. |
| Microsoft Fairwater $3,3B + Dec 2025 $569M | §1.3 ✓ | s12 ✓ | line 263 ✓ | ✓ |
| Tesla Optimus pilot scale May 2026 | §1.3 ✓ «десятки единиц» | s11 «несколько десятков» | line 243 «нескольких десятков» | ✓ |
| F-35 ALIS $44k FY2018 → $35k FY2024 | §3.3 chapter-part2 ✓ (both figures) | s27 «$44 000» only | line 547 «44 тысячи» only | **P1: $35k FY2024 missing from slide+speech**. Chapter has the falling-trajectory; slide+speech freeze at original $44k. |
| TSMC 95% defect classification + 10–15% yield | §2.1 ✓ | s14 ✓ | line 289 ✓ | ✓ |
| Foxconn FoxBrain 80% configuration claim | §1.2 ✓ | s21 ✓ | line 423 ✓ | ✓ |
| BASF Geismar –20–30% batch defects | §3.1 chapter-part2 ✓ | s24 «–30% batch defects» (single point) | line 471 «двадцать-тридцать процентов» | ✓ (slide picks midpoint, speech uses range) |
| Pfizer Vox +20 000 doses per batch | §3.1 + §4.3 ✓ | s24, s34 ✓ | line 473, 703 ✓ | ✓ |
| Yokogawa-JSR FKDPP 35 days Jan-Feb 2022 | §3.2 ✓ | s25 ✓ | line 493 ✓ | ✓ |
| Holcim 100 plants C3 AI | §3.3 ✓ | s27, s39 ✓ | not mentioned in speech (only BMW closing) | **P2 missing in speech** |
| Brewery line rate | §4.3c «**30 000** бутылок/ч × 24/7 = ~700 000/день» | s34c «**60 000**/ч, >1 млн/сутки» | line 749 «**60 тысяч** бутылок/ч, миллион в сутки» | **P0 DRIFT — chapter 30k vs slides+speech 60k** |
| Brewery defect rate | §4.3c 0,5% | s34c 0,5% ✓ | line 749 0,5% ✓ | ✓ |
| Brewery defect type list | §4.3c «скол горлышка, повреждённая этикетка, недолив, оторванная пробка» | s34c «повреждённые этикетки, кривые крышки, недолив» | line 749 «повреждённые этикетки, кривые крышки, недолив» | **P2 drift: slides+speech replace «скол горлышка/оторванная пробка» with «кривые крышки»** |
| 5 vendor questions | §5.2 chapter-part3 ✓ (5 incl. «3 documented failures за 24 months») | s35 = **4 questions**, s38 = **5 but Q5 = «архитектурный класс» not «прошлые провалы»** | line 829-837 = 5 incl. «прошлые провалы» | **P0 DRIFT — three different versions of question 5** |
| 4 categories criteria count | §4.1 chapter-part3 = **10 criteria + 1 bonus** (A=3, B=2, C=3, D=2 + anti-hype bonus) | s32 = **11 criteria** (A=3, B=2, C=3, D=3 — moves anti-hype to D11) | speech [s32] line 619 «10 критериев» in description but narrates 10 + bonus (matches chapter) | **P0 DRIFT — slide s32 is the lecture's most visible payoff slide and counts differently** |

## 6. Worked examples cross-check

Three worked examples — all 3 present, all 3 demonstrate framework-as-filter symmetry.

| Example | Chapter location | Slide | Speech | Verdict |
|---|---|---|---|---|
| Pfizer Vox **pass** | §4.3 chapter-part3 | s34 | [s34] line 685-709 | ✓ All 3 align on shape: 5 steps, all 4 categories pass, recommend-mode architecture, +20k doses outcome. |
| Авиадвигатель **fail** | §4.3 chapter-part3 (extended walk-through) | s34b | [s34b] line 717-739 | ✓ All 3 align on shape: MTBF 8 years, SIL 2, fail on data + cost + regulatory. ✓ Same RCM alternative. |
| Brewery packaging line **pass** | §4.3c chapter-part3 | s34c | [s34c] line 749-771 | **P0 drift on production rate (30k vs 60k bottles/hr); P2 drift on defect type list.** Framework conclusion identical (pass on all 5 steps). |

**P0 detail — brewery rate:**
- Chapter §4.3c line 186 + chapter-part3 line 196: «30 000 бутылок в час... 30 000/час × 24/7 = ~700 000 в день; defect rate 0,5% → ~3 500 дефектов в день. За 30 дней — 105 000 labelled examples.»
- Slide s34c body: «60 000 бутылок в час, более 1 миллиона бутылок в сутки. Доля брака ~0,5%».
- Speech [s34c] line 749, 757: «60 тысяч бутылок в час, миллион в сутки... миллион бутылок в день, полпроцента брака — пять тысяч размеченных дефектов каждый день».

**Cascade effect:** chapter math gives 700k/day × 0.5% = 3.5k defects/day → 105k in 30 days; slide+speech math gives 1M/day × 0.5% = 5k defects/day → 105k in 21 days. The downstream «класс-баланс за две-три недели» (speech) is **inconsistent с chapter's 30 days**.

**Recommendation:** Either uplift chapter to 60k/hr (and adjust derived numbers — 1M/day, 5k defects/day, 21 days for class balance) OR downshift slide+speech to 30k/hr matching chapter. **Preference: uplift chapter to 60k/hr** — 60k/hr is more realistic for modern bottling line (Anheuser-Busch, BrewMaxx range 30-80k/hr depending on bottle size); chapter v5 finalized but fact-correctable in Phase 11.

## 7. 5-step framework cross-check

| Step | Chapter §4.4 | Slide s35 | Speech [s35] |
|---|---|---|---|
| 1 | «Определить колонну» | «Identify class» (EN) | «Определить колонну» |
| 2 | «Картировать альтернативы» | «Map alternatives» (EN) | «Картировать альтернативы» |
| 3 | «Применить 4 категории критериев» | «Apply 4 categories» (EN) | «Четыре категории критериев» |
| 4 | «Пилот с явными критериями продолжения + базовая линия» | «Pilot с explicit go-criteria» | «Пилот с явными критериями плюс базовая линия» |
| 5 | «Промышленная эксплуатация с HITL + журналом аудита» | «Production с HITL + audit trail» | «Production с человеком в цикле плюс журналом аудита» |

**Same 5 steps, semantically identical.** Speech and chapter use Russian; slide s35 uses English step labels («Identify / Map / Apply / Pilot / Production»). For an RU-language deck for МГТУ ИУ6 universal audience, **English step labels on s35 = anglicism leak** that crosses Russification mandate ([[russification]]). P1 fix recommended in Phase 11.

## 8. 4 categories cross-check

**P0 DRIFT — most visible payoff slide.**

| Category | Chapter §4.1 | Slide s32 | Speech [s32] |
|---|---|---|---|
| **A. Данные** | 3 criteria (MTBF, known physics, expensive labels) | **3** ✓ | 3 ✓ |
| **B. Стоимость** | **2** criteria (FP cost ≫ FN cost, SIL 2/3) | **2** (#4 + #5) ✓ | 2 ✓ |
| **C. Регуляторика** | 3 criteria (audit trail, ATEX, Указ 250) | **3** (#6 + #7 + #8) ✓ | 3 ✓ |
| **D. Человек** | **2** criteria (operator distrust, pilot без go/no-go) | **3** (#9 + #10 + **#11 demo-hype bonus** — moved INTO D, not kept as bonus) | 2 + bonus («Сквозное правило: заявления на основе демонстраций без 6-мес истории — покупатель должен быть осторожен.» — line 651 keeps bonus separate) |
| **Bonus anti-hype** | Yes, separate from D | **NO — collapsed into D as #11** | Yes, mentioned as «Сквозное правило» |
| **Total count statement** | «10 критериев... плюс одна общая категория» (10+1) | «**11 критериев** в 4 категориях» (line 69 speaker notes) | line 619 «4 категории × **10 критериев**» |

**P0 implication:** slide s32 — самый длинный slide лекции (duration 4 min), payoff визуальный. Студент видит **11**; преподаватель говорит **10 + бонус**; chapter Q&A backup may reference «10 criteria + bonus». Numbering ambiguity на ЦЕНТРАЛЬНОМ payoff слайде = **structural P0**.

**Recommendation:** uplift slide s32 to chapter convention (3 + 2 + 3 + 2 = 10 numbered + 1 separate «bonus anti-hype» at bottom). Reorder body so D shows 2 items (#9 + #10), bonus в отдельной строке внизу. Update speaker notes to «10 криteriев + бонусный». Easy 2-paragraph edit.

## 9. 5 vendor questions cross-check

**P0 DRIFT — three different counts/contents.**

| Question | Chapter §5.2 chapter-part3 | Slide s35 | Slide s38 | Speech [s38] |
|---|---|---|---|---|
| 1. Baseline | ✓ | ✓ | ✓ | ✓ |
| 2. Окно измерения | ✓ | ✓ | ✓ | ✓ |
| 3. Перечень вмешательств | ✓ | ✓ | ✓ | ✓ |
| 4. OEE-канал | ✓ «Бонус» | ✓ | ✓ | ✓ |
| 5. ?? | **«Прошлые провалы — 3 documented failures за 24 months в той же индустрии»** | **NOT PRESENT — s35 lists only 4 questions** | **«Архитектурный класс — chat-помощник vs autonomous controller; FDA/ATEX/SIL»** | **«Прошлые провалы — 3 документированных провала за 24 месяца»** |

**Three artifacts disagree on whether there are 4 or 5 questions, and what Q5 actually is:**
- **Chapter + speech**: 5 questions, Q5 = past failures (most pedagogically valuable — это ловушка зрелости вендора).
- **Slide s35**: only 4 questions (Q5 missing entirely).
- **Slide s38**: 5 questions but Q5 = architectural class (chat vs autonomous).

**P0 fix:** Decide canonical Q5. Recommendation: chapter+speech version («past failures») is the more distinctive pedagogical hook (any vendor will state baseline; few will state failures). Plus slide s32 already covers architectural-class question in regulatory context (criterion #6). 

**Action:** 
1. Update slide s35 to show all 5 questions (add «5. Прошлые провалы — 3 документированных провала за 24 мес»).
2. Update slide s38 to replace Q5 «архитектурный класс» with «прошлые провалы», matching chapter+speech.

This is a Phase 11 batched edit, ~15 min.

## 10. Roadmap cross-check

**✓ CLEAN.**

5 sections, identical labels across:
- Chapter §0.3 (lines 131-134)
- Slide s03 (5 horizontal cards)
- Speech [s03] (line 119)
- deck.yaml comments (lines 31-90)

Section labels: «Общее → Дискретное → Процессное → Рамка решения → Замыкание». No drift. Pacing math: chapter says «§1 ≈ 12 мин, §2 ≈ 17 мин, §3 ≈ 17 мин, §4 ≈ 12 мин, §5 ≈ 6 мин»; speech has same allocation (lines 159, 275, 457, 609, 799); s03 says «12 мин, 17 мин, 17 мин, 12 мин, 6 мин». Total 64 min + 11 min hooks/dividers = 75 min. **Internally consistent.**

## 11. Attribution cross-check

| Attribution | Chapter | Slide | Speech | Notes |
|---|---|---|---|---|
| Musk April 2018 Twitter quote | ✓ EN verbatim | ✓ s01 + s19 EN verbatim | ✓ Russian translation «Да, чрезмерная автоматизация на Tesla была ошибкой. Точнее — моей ошибкой. Людей недооценивают.» | ✓ Translation consistent across speech (lines 93, 383). |
| Bainbridge 1983 «Ironies of Automation» | ✓ §2.4 chapter-part2 + ref [#] | ✓ s19 body + speaker notes | ✓ line 393 | ✓ Same attribution structure. |
| Toyoda 1924/1925 Type-G loom | ✓ §2.4 chapter-part2 | NOT in slides (s18 body mentions «Jidoka» only, no Toyoda year) | NOT in speech (only «дзидока» abstract) | **P2: chapter has historical depth (1924/1925), slides+speech compress to «Jidoka» without year/inventor** — acceptable simplification for time budget. |
| Toyota GAIA «10 000 моделей» | ✓ §2.3 | ✓ s18 | ✓ line 363 | ✓ |
| Trump «8th wonder of the world» 2018 | ✓ §1.3 | ✓ s12 «восьмое чудо света» | ✓ line 263 «восьмым чудом света» | ✓ all 3 say «глава государства назвал», anonymizing — consistent. |
| Foxconn Young Liu Computex May 2025 | ✓ §2.3 «Янг Лю (Young Liu)» | ✗ s21 says **«Молодой Лю»** (mistranslation of «Young» as adjective «young/молодой» — name treated as Russian word) | ✓ line 423 «Янг Лю» | **P2 — slide s21 transliteration error.** Fix: «Young Liu (Янг Лю)» в slide s21. |

## 12. References cross-check

**Chapter has 105 inline references (per frontmatter `references_count: 105`).** Speech doesn't cite inline (correct for spoken format). Slides cite minimally in YAML `references:` blocks (e.g., s05 has `[mckinsey-2025-state-of-ai, mit-sloan-2025-95-percent]`, s24 has `[pfizer-vox-2024]`).

**No orphan slide references across artifacts.** Pre-flight checklist references [s01, s07, s08, s10, s11, s12, s19, s21, s25, s28, s32, s34b] — all valid in deck.yaml.

**No orphan reference from speech to deleted slides.** Speech goes s01 → s39 in deck.yaml order, no missing slide IDs.

Minor (P2): chapter §3.5 introduces **«КАМАЗ автономные грузовики Маяк-2.5»** as Russian-context anchor — slide s29 keeps it implicit («Норникель + СИБУР + ММК/НЛМК/Северсталь»), speech [s29] line 575-587 also skips KAMAZ. Acceptable simplification; chapter Q&A backup catches it in Q4.

## 13. Bridge к Лекции 12 cross-check

| Anchor | Chapter §5.3 | Slide s39 | Speech [s39] |
|---|---|---|---|
| BMW 30+ заводов digital-twin-ready | ✓ | ✓ «BMW: 30+ plants digital-twin-ready» | ✓ line 851 «тридцати с лишним заводам» |
| Holcim первый цифровой двойник цементного завода | ✓ | ✓ «Holcim: world's first digital-twin cement plant (2024)» | ✗ NOT mentioned — speech jumps from BMW directly to «Лекция 12 — сшивка» |
| Foxconn-NVIDIA Omniverse | NOT in chapter §5.3 (only generic «цифровых двойников»); is in slide tier-6 fallback note | ✓ «Foxconn-NVIDIA Omniverse» | ✗ NOT mentioned |
| ГОСТ Р 57700.37-2021 | ✓ §5.3 line 305 | ✗ not on slide | ✓ line 855 «ГОСТ Р 57700.37-2021» |
| 5 anchor points for Lec 12 (OT/IT, edge L1.5, foundation models sandbox, OEE real-time, 5-step framework reuse) | ✓ explicit list in §5.3 lines 307-313 | NOT visible on slide | NOT in speech (compressed to «ось дискретное-процессное, четыре категории, пятишаговая рамка, пять вопросов») |

**P2 drift:** Chapter is the canonical source-of-truth and has the richest bridge anchors. Slide s39 mentions Holcim + Foxconn-NVIDIA (visual richness for closing hero). Speech minimalist (only BMW). Acceptable compression for time budget — speech is 5-min compression of chapter §5.3 — but the **closing visual on s39 will show Holcim + Foxconn-NVIDIA names** while lecturer says only «BMW». Possible audience confusion.

**Recommendation:** either (a) add 1-sentence Holcim mention to speech [s39] («И параллельно — Holcim первый в мире цифровой двойник цементного завода»), OR (b) simplify s39 hero to BMW-only to match speech.

## 14. Pre-flight checklist quality

**✓ STRONG — actionable, 0 orphan refs.**

- 8 slide-specific freshness checks (s01/s07/s08/s11/s12/s21/s25/s28) с конкретным URL для верификации.
- Все slide references valid в deck.yaml.
- Recovery cards (3) — concrete actions for fact-check fail, projector fail, Q&A drift.
- Day-of refresh (3 short items, 5 min before lecture).
- Reading-aloud-with-stopwatch для 6 fragment'ов (s07, s10, s19, s25, s32, s34b) — calibration of pacing ≤ 95 wpm.

**Minor improvements:** could add s09 OT/IT pronunciation note («о-тэ» / «ай-тэ» — speech uses Cyrillic, slide uses Latin); could add s39 Holcim mention guidance.

## 15. P0 / P1 / P2 issues catalogued

### P0 (3) — factual contradiction / structural drift on cornerstone

**P0-1. Brewery production rate drift (chapter 30k vs slides+speech 60k bottles/hr).**
- **Where:** chapter-part3 §4.3c line 186 vs slide s34c body vs speech [s34c] line 749.
- **Issue:** chapter math derives «3 500 defects/day, 30 days for class balance» from 30k/hr; slides+speech derive «5 000 defects/day, 2-3 weeks» from 60k/hr. Speech says «миллион в сутки», chapter says «700 000 в день».
- **Fix:** uplift chapter to 60k/hr matching slides+speech (more realistic for modern bottling), recalibrate derived numbers (1M/day, 5k defects, 2-3 wks). Recommended target: 60k/hr → slides+speech canonical. ~15 min edit in chapter-part3.md.

**P0-2. Number of criteria in §4 «AI не нужен»: chapter 10+1 bonus vs slide s32 «11» vs speech «10 + бонус».**
- **Where:** chapter-part3 §4.1 (line 40 «10 critериев... плюс одна общая категория»), slide s32 body (D has 3 items #9/#10/#11, speaker notes line 69 «11 критериев в 4 категориях»), speech line 619 («10 критериев»).
- **Issue:** slide s32 is the most visually rich payoff slide; differs from chapter+speech narrative.
- **Fix:** restructure slide s32 to A=3 + B=2 + C=3 + D=2 = 10 numbered, + 1 bonus «anti-hype» в отдельной строке. Update speaker notes to «10 critериев + бонус». ~10 min edit.

**P0-3. Vendor questions count: chapter+speech = 5 (incl. «past failures»); slide s35 = 4 questions; slide s38 = 5 but Q5 = «архитектурный класс».**
- **Where:** chapter-part3 §5.2 (line 280-296), slide s35 (line 26-34), slide s38 (line 28), speech [s38] (line 829-837).
- **Issue:** three different canonical lists для самого практичного payoff артефакта лекции — «5 вопросов к вендору».
- **Fix:** sync to chapter+speech version (5 questions incl. past failures). Update slide s35 from 4 → 5 questions. Update slide s38 Q5 from «архитектурный класс» → «прошлые провалы — 3 documented failures за 24 месяца». ~15 min edit.

### P1 (6) — significant drift

**P1-1. F-35 ALIS $44k FY2018 → $35k FY2024 — only $44k mentioned in slide s27 and speech [s27].**
- Chapter chapter-part2 §3.3 line 311 has both figures; slide s27 line 50 «$44 000» only; speech line 547 «44 тысячи» only.
- Fix: add «FY2018 базовая линия; FY2024 ~$35k» to slide s27 + speech callback. ~3 min edit.

**P1-2. Foxconn Wisconsin jobs count drift: speech opening line 99 «10000», speech later line 263 «13000», slide s12 «10000», chapter «13000 potential / 10000 contract».**
- Speech is **internally inconsistent**. Fix: align speech к chapter — «10 миллиардов долларов инвестиций и до 13 тысяч рабочих мест (потенциал), 10 тысяч по контракту с EDC».

**P1-3. Slide s35 step labels in English («Identify class / Map alternatives» etc.) — anglicism leak в RU-deck.**
- Russification mandate violation. Fix: translate to Russian («Определить класс / Картировать альтернативы / Применить 4 категории / Пилот с критериями / Production с HITL»).

**P1-4. Slide s21 «Молодой Лю» — transliteration error of Foxconn chairman's given name «Young».**
- «Young» — name, not adjective. Chapter + speech correctly use «Янг Лю». Fix: slide s21 line 50 → «Янг Лю».

**P1-5. Slide s32 mixes RU + EN body labels («SIL 2/3 safety-critical», «FP cost >10× FN», «Audit-trail», «Demo-hype», «Operator distrust», «Six Sigma, Jidoka, structured pilots»).**
- Anglicism leak в самом длинном payoff слайде. Speech narrates fully in Russian. Fix: render slide s32 fully in Russian (FP/FN → «ложн. срабатывание / пропущ. отказ», «audit-trail» → «журнал аудита», «demo-hype» → «демо-хайп»). ~10 min edit.

**P1-6. Slide s35 + s38 vendor questions language mix («Baseline до AI», «recommend mode для safety-critical», «explicit go-criteria», «HITL + audit trail»).**
- Same anglicism issue. Fix: Russification pass.

### P2 (7) — minor inconsistency

**P2-1. OT/IT (Latin in chapter+slide) vs ОТ и ИТ (Cyrillic in speech body).** Same concept; typographic.

**P2-2. S&P Global 46% / $7M sunk cost not visible in slide s07 or in speech.** Mentioned only in chapter §1.1. Optional: add 1-line callback in s07 OR in speech [s07] for completeness.

**P2-3. Holcim 100 plants C3 AI — in chapter §3.3, slide s27, but NOT mentioned in speech.** Speech compresses §3.3 to POSCO only. Acceptable for time budget.

**P2-4. Toyoda 1924/1925 Type-G — in chapter §2.4, NOT in slide s18 or speech.** Acceptable historical compression.

**P2-5. Brewery defect type list drift («скол горлышка/оторванная пробка» in chapter vs «кривые крышки» in slides+speech).** Cosmetic but visible.

**P2-6. Closing hero s39 mentions Holcim + Foxconn-NVIDIA Omniverse; speech [s39] only mentions BMW.** Slide visual richer than speech.

**P2-7. KAMAZ Маяк-2.5 in chapter §3.5, not in slide s29, not in speech.** Acceptable simplification.

## 16. Recommendations for Phase 11

**Single batched edit (estimated ~60-75 min for orchestrator + 1 designer pass + 1 speech-writer pass):**

### Slides (designer pass, ~30 min)
1. **Slide s32** — restructure to 10 numbered + 1 bonus (instead of 11 numbered). Russification pass.
2. **Slide s34c** — verify brewery rate matches chosen canonical (recommend 60k/hr) and update if drifted.
3. **Slide s35** — add 5th vendor question («Прошлые провалы — 3 documented failures за 24 мес»). Russify step labels (Identify → Определить, etc.).
4. **Slide s38** — replace Q5 «архитектурный класс» → «прошлые провалы». Russification pass on body.
5. **Slide s21** — fix «Молодой Лю» → «Янг Лю».
6. **Slide s27** — add F-35 FY2024 $35k context.
7. **Re-render PPTX after edits, verify visible body 0 anglicisms in scaffold patterns.**

### Chapter (book-editor pass, ~15 min)
1. **Chapter-part3 §4.3c** — uplift brewery rate to 60k/hr (or downshift slides+speech to 30k — orchestrator decides; recommend 60k as more realistic).
2. **Chapter-part3 §4.1** — keep «10 + бонус» canonical, no edit needed.
3. **Chapter §5.2** — already has «5 questions» canonical, no edit needed.

### Speech (speech-writer pass, ~15 min)
1. **Speech opening line 99** — change «десять тысяч рабочих мест» to «десять тысяч рабочих мест по контракту, до тринадцати тысяч в потенциале» — fix internal inconsistency with line 263.
2. **Speech [s27] line 547** — add F-35 FY2024 update: «44 тысячи за лётный час в 2018 году, около 35 тысяч в 2024».
3. **Speech [s39]** — add Holcim 1-liner to closing for visual-verbal alignment.
4. **Speech [s32] line 619** — verify «10 категорий» narration matches updated slide.

### Cross-artifact sweep (orchestrator, ~15 min)
1. Re-grep all 3 artifacts after fixes for: «11 critериев» (should be 0), «60 000 бутылок» (should match across all 3), «5 questions» (should be canonical 5 in all artifacts), «$35» (should appear in slide s27 + speech).
2. Re-verify pre-flight checklist all slide IDs still valid.
3. Run deep-latin-token scan on rendered PPTX visible body (Phase 11.2).

**Time budget for Phase 11 batched revision:** ~75 minutes. After, re-run consistency-checker mode=`terminology-only` for verification.

---

**Verdict (repeated):** **REVISE** — 3 P0 + 6 P1 issues. None require architectural rework; all are batch-editable in Phase 11. After fixes, consistency-checker should yield APPROVE-CLEAN.

**Strengths preserved:** central question alignment, cornerstones unified, worked-examples symmetry (Pfizer pass / avionics fail / brewery pass), strict-in failure-share ≥30%, pre-flight checklist actionable with 0 orphan refs, attribution discipline (Musk / Bainbridge / Trump «8th wonder» / Young Liu Computex), bridge к Лекции 12 anchored in OT/IT + L1.5 + 5-step reusability.

Speech v1 — strong artifact; consistency-checker flags primarily slide drift relative к chapter+speech (which are co-aligned with each other). Phase 11 batched fix-up cycle should resolve все P0 + P1 в один pass.
