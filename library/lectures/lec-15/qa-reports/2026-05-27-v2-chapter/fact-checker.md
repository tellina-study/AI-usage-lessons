# Fact-Checker Report — Лекция 15 chapter v2.0 — 2026-05-27 (Phase 4.5 focused re-fact-check)

**VERDICT: REVISE**

**Rationale.** Все 2 P0 из v1 (NeurIPS numbers + Russia decree) — **успешно закрыты**, canonical и cascaded. 6 из 7 P1 fact fixes из v1 — также закрыты корректно (Insitro $400M ✓, ECMWF 25 Feb 2025 ✓, reproducibility 39/100 ✓, GDT_TS ~75 disambiguated ✓, Hurricane Milton → tail events generalized ✓, LIGO Ashton/Malz/Colombo ✓). **Однако новое expansion §2 в v2** ввело **2 новых P0 и 2 новых P1**:

- **P0-NEW-1 (CRITICAL):** §2.7 фабрикует worked example «как AlphaProof решил задачу 3 IMO 2024» (~10 строк технических деталей: 50 строк Lean, ~10 000 кандидатов, ~4 часа GPU) — **но AlphaProof фактически НЕ решил задачу 3** (обе combinatorics задачи P3 и P5 остались нерешёнными). Это сфабрикованный worked example.
- **P0-NEW-2:** §2.4 GNoME заявляет «цикл повторяется ~22 раза» (22 итерации активного обучения) — **фактически 6 раундов** per Nature paper Methods.
- **P1-NEW-1:** Akdel/Bryant disambiguation **выполнена неверно** — chapter говорит «продолжение анализа — arxiv:2510.15939, Bryant et al. 2025», но фактические авторы arxiv 2510.15939 — **Gopalan & Narayanan, 2025** (Bryant нет в author list).
- **P1-NEW-2:** Sources entry 13 — Charlton-Perez et al. 2024 цитируется как «**GRL** (Geophysical Research Letters), 51» — фактически опубликовано в **npj Climate and Atmospheric Science** (DOI 10.1038/s41612-024-00638-w, 22 апреля 2024).

Эти 2 новых P0 — структурные ошибки в техническом expansion §2 и блокируют APPROVE. Требуется focused fact-fix mini-revision (~30-45 мин) до GATE A: убрать сфабрикованный worked example IMO 2024 task 3 либо заменить на реальный (task 1/2/6); поправить GNoME 22→6 итераций; поправить Bryant → Gopalan & Narayanan; поправить Charlton-Perez journal.

## Severity counts

- **P0 (false fact / wrong number / hallucinated source / direction inversion):** **2 NEW** (v1 P0 = 0 remaining — оба closed)
- **P1 (suspicious number, missing source / framing):** **2 NEW** (v1 P1 = 7 closed of 7)
- **P2 (cite format / volatile, minor framing):** ~5 inherited from v1 + few new (volatile markers OK)
- **Verified ✓:** v1 closures = 9 of 9 + new sample claims partly ✓
- **Hallucinated sources detected:** **1** (Bryant et al. for arxiv 2510.15939 — wrong author attribution = hallucinated cite)
- **UNVERIFIABLE:** 0 critical

---

## Section A. v1 P0 closure verification ✓ — BOTH CLOSED

### P0-3 (v1): NeurIPS 2025 «21 575 / 5 290 / 24,52%» — ✓ CLOSED canonical

**Cascade verification:**
- chapter.md §0.4 line 178 (Glossary): «NeurIPS 2025 — 24,52% принятых из 21 575 поданных» ✓
- chapter.md changelog line 48 (P0-3 explicitly noted): «21 575 поданных / 5 290 принятых / 24,52%» ✓
- chapter.md §1.2 line 260 (Sakana comparison): «3% (отбор) сама по себе ниже среднего acceptance rate ICLR 2024 (24,52%)» — note: ICLR vs NeurIPS conflation **partially remains** (chapter says ICLR 2024 acceptance was 24.52%, but 24.52% is NeurIPS 2025). See §A-residual below.
- chapter-part3.md §4.5 line 327: «NeurIPS 2025 имел 21 575 поданных статей, 5 290 принятых (доля принятых 24,52%)» ✓
- chapter-part3.md §4.5 line 339: «разбор 21 575 поданных требует инфраструктуры» ✓
- chapter-part3.md §4.5 line 345: «Рецензирование при большом объёме подач (21 575 в NeurIPS)» ✓
- chapter-part4.md References 36: «NeurIPS 2025 fake citations [21 575 поданных / 5 290 принятых]» ✓

**Source confirmed:** arxiv 2602.05930 «Compound Deception in Elite Peer Review» — 53 papers / 100+ citations / 4,841 of 5,290 papers scanned by GPTZero / 21 575 submissions / 24.52% acceptance ✓.

**Closure status: ✓ Canonical в 7 instances. Minor residual: §1.2 line 260 framing «ICLR 2024 acceptance 24,52%» — это NeurIPS 2025 number, не ICLR. Recommend cleanup to «… acceptance rate среднего workshop ICLR 2024 (24,52% — для конференции NeurIPS 2025; ICLR 2024 — отдельный показатель)» или drop conference label here. P2 residual.**

### P0-4 (v1): Указ № 490 (2019) + № 124 (2024) — ✓ CLOSED canonical

**Cascade verification:**
- chapter.md changelog line 49 (P0-4 explicitly noted): «Указ Президента РФ № 490 от 10 октября 2019 г.» + «Указ № 124 от 15 февраля 2024 г.» ✓
- chapter-part4.md §5.6 line 234: «Указ Президента РФ № 490 от 10 октября 2019 г. ... обновлён Указом Президента РФ № 124 от 15 февраля 2024 г.» ✓ + источники kremlin.ru/acts/bank/44731 + kremlin.ru/acts/bank/50091 ✓
- chapter-part4.md Q&A Q15 line 425: «Указ Президента РФ № 490 от 10 октября 2019 г., обновлён Указом № 124 от 15 февраля 2024 г.» ✓
- chapter-part4.md References 60-61: «Указ Президента РФ № 490 ... kremlin.ru/acts/bank/44731. Указ Президента РФ № 124 ... kremlin.ru/acts/bank/50091» ✓

**Closure status: ✓ Canonical в 4 instances + 2 source URLs. Old wrong № 145 completely removed.**

---

## Section B. v1 P1 closure verification — 7 of 7 CLOSED

### P1-12 (v1): Akdel citation disambiguation — ✗ NEW ISSUE

**Verification (chapter-part2.md line 51, chapter-part3.md line 120):**
- Chapter says: «Akdel et al., Nature Structural & Molecular Biology, 2022; продолжение анализа — arxiv:2510.15939, 2025»
- chapter-part3.md line 120 elaborates: «arxiv 2510.15939 — это последующий анализ 2025 года другой группы»
- chapter-part4.md References 32-33: «32. Akdel, M., et al. (2022). AlphaFold2 community assessment. Nat Struct Mol Biol, 29, 1056-1067. **33. Bryant, P., et al. (2025). AlphaFold IDP follow-up. arxiv, 2510.15939.**»

**Web verification — arxiv 2510.15939:**
- Actual authors: **Shreya Gopalan и Sundar Narayanan** (per arXiv abstract + ResearchGate)
- Title: «Hallucinations in AlphaFold3 for Intrinsically Disordered Proteins with disorder in Biological Process Residues»
- Year: 2025 (submitted Oct 8, 2025; revised Nov 11, 2025)
- **Bryant нет в authors list.**

**Severity: P1-NEW (cite hygiene + hallucination)**

**Where in chapter:**
- chapter-part4.md References entry 33

**Cite for Akdel 2022 NSMB itself:** ✓ verified Akdel M., et al. (2022). «A structural biology community assessment of AlphaFold2 applications.» Nat Struct Mol Biol 29, 1056-1067. Real, correct.

**Recommended fix:**
> «33. Gopalan, S., Narayanan, S. (2025). Hallucinations in AlphaFold3 for IDPs with disorder in Biological Process Residues. **arxiv**, 2510.15939.»

И в narrative §2.1 / §3.5 при упоминании последующего анализа — корректировать «Bryant et al.» → «Gopalan & Narayanan» либо просто оставить arxiv:2510.15939 без имени authors.

### P1-13 (v1): LIGO Ashton/Malz/Colombo — ✓ CLOSED

- chapter-part3.md §3.4 line 103: «Эштон, Малц и Коломбо (Ashton, Malz, Colombo) опубликовали детальный анализ ... (arxiv:2504.17587, 2025). Это не коллективная публикация LIGO-VIRGO, а независимый анализ группы методологов» ✓
- chapter-part4.md References 29: «Ashton, G., Malz, A. I., Colombo, S. (2025). Conformal Prediction для LIGO. arxiv, 2504.17587.» ✓

**Closure: ✓ Both authorship (3 individuals) and year (2025) and «not LIGO-VIRGO Collaboration» properly noted.**

### P1-14 (v1): Insitro Series C $400M (2021) — ✓ CLOSED

- chapter-part2.md line 71 (Nobel cascade effect): «Insitro (Series C $400 млн, 2021, проверено по Crunchbase/PitchBook)» ✓

**Web verification — confirmed.** Insitro Raises $400 Million in Series C, March 15 2021, led by CPP Investments. Multiple sources (BusinessWire, Crunchbase, BioSpace, Fierce Biotech) confirm $400M ✓.

**Note: Recursion claim** — v1 fact-checker flagged "Recursion $300M" as unclear. In v2 chapter-part2.md line 71 reads «Recursion (раскрытие финансирования см. ниже)» — i.e., chapter softens к narrative «см. ниже» but no specific «ниже» reference about Recursion follows in §2.3. **P2 residual:** «см. ниже» dangling reference if Recursion finances не explicitly cited later.

**Closure: ✓ Insitro corrected. Recursion softened to «см. ниже» — слабая, но допустимая текстовая стратегия. Minor cleanup recommended.**

### P1-15 (v1): Reproducibility 39 of 100 — ✓ CLOSED

- chapter.md §0.4 line 179 (Glossary): «Психология — 39 из 100 (Open Science Collaboration, 2015); экономика — 61%» ✓
- chapter-part4.md References 37: «Open Science Collaboration (2015). Reproducibility psychology [39 из 100]. Science, 349, aac4716.» ✓

**Web verification:** Open Science Collaboration 2015 Science aac4716 «Estimating the reproducibility of psychological science» — 39 of 100 replicated с p<0.05 significance criterion ✓.

**Closure: ✓ canonical 39 instead of 36. No instances of old «36%» remain в narrative.**

### P1-16 (v1): AlphaFold 2 baseline GDT_TS disambiguation — ✓ CLOSED

- chapter.md §0.4 line 183 (Glossary): «CASP14 — средний GDT_TS ~92 против ~75 в среднем у лучших методов до AF2 — а на труднейших Free Modeling целях разрыв был ещё больше: ~92 против ~60» ✓
- chapter-part2.md §2.1 line 41: «средний GDT_TS ~92 при том, что лучшие методы до AF2 показывали в среднем по всем задачам CASP13 около ~75, и только на труднейших задачах Free Modeling — около ~60» ✓

**Closure: ✓ Disambiguation correctly cascaded в 2 instances. Free Modeling vs all-targets разделение явно отмечено.**

### P1-17 (v1): ECMWF AIFS 25 февраля 2025 — ✓ CLOSED

- chapter.md §0.4 line 186 (Glossary): «AIFS оперативно с 25 февраля 2025 г.» ✓
- chapter-part2.md §2.6 line 180: «оперативная с 25 февраля 2025 года» ✓
- chapter-part4.md Q11 line 405: «оперативно с 25 февраля 2025 года» ✓
- chapter-part4.md References 12: «ECMWF AIFS Team (2025). AIFS operational deployment. ECMWF Press, 25 февраля 2025» ✓

**Web verification:** ECMWF news page «ECMWF's AI forecasts become operational» — operational date **25 February 2025** ✓.

**Closure: ✓ Canonical в 4 instances. Old «с 2024 года» полностью удалён.**

### P1-18 (v1): Hurricane Milton specific → tail events generalized — ✓ CLOSED

- chapter-part2.md §2.6 line 182: «Aurora и подобные фундаментальные модели показывают конкурентную среднюю точность, но систематически уступают на экстремальных событиях — ураганы пиковой интенсивности, локальные события сильных осадков, атмосферный блокинг ... мета-анализ Charlton-Perez et al., 2024» ✓
- No specific «Hurricane Milton + Aurora» pairing remains в narrative.

**Closure: ✓ Specific Milton-Aurora pairing dropped; generalized к «tail events» with мета-analysis reference. Reference: see Section D for separate Charlton-Perez **journal citation issue**.**

---

## Section C. NEW P0 FACT ERRORS

### P0-NEW-1 (CRITICAL): Fabricated worked example AlphaProof решил задачу 3 IMO 2024

**Where:** chapter-part2.md §2.7 lines 197-205.

**Chapter claim (line 197):**
> «**AlphaProof — три остальные задачи (алгебра, теория чисел, комбинаторика).**»

**Chapter claim (line 203):**
> «**Конкретный пример: как AlphaProof решил задачу 3 IMO 2024.** Задача 3 — комбинаторная задача о расположении 2024 чисел в круге с условием на разности соседей. Человек-олимпиадник решает её через выбор инварианта (постоянной величины через перестановки) и доказательство свойств этого инварианта. AlphaProof решал её так: (а) задача формализована в Lean как теорема (~50 строк формальной постановки); (б) AlphaProof сгенерировал ~10 000 кандидатных доказательств через нейро-управляемый поиск; (в) каждый кандидат проверен компилятором Lean — большинство отвергнуты, ~5 прошли проверку; (г) лучший из 5 (по длине / читаемости) был представлен как решение. Общее время — **~4 часа на GPU-кластере**.»

**Primary source — DeepMind blog «AI achieves silver-medal standard» (July 2024) + Nature paper (s41586-025-09833-y, 2025):**

- **AlphaProof решил**: P1 (algebra), P2 (number theory), P6 (algebra).
- **AlphaGeometry 2 решил**: P4 (geometry).
- **Нерешённые**: **P3 (combinatorics) И P5 (combinatorics)** — обе комбинаторные задачи остались нерешёнными.
- Цитата из DeepMind: «The two combinatorial problems (P3 and P5) remained unsolved by our systems ... due to difficulties in formalization and explosive search.»

**Delta:**
- Chapter line 197 говорит «комбинаторика» среди решённых — **wrong** (комбинаторика была НЕ решена).
- Chapter line 203 фабрикует **детальный worked example** о том, как AlphaProof решил task 3 — со специфическими цифрами (50 строк Lean, 10 000 кандидатов, 4 часа GPU) — **полностью сфабрикованные данные**, так как AlphaProof не решал task 3 вообще.

**Severity rationale:** P0 CRITICAL — это **прямая false claim о научной capability** + **сфабрикованный worked example** с конкретными числами, которые невозможно подтвердить (потому что событие не произошло). Особенно опасно для текстбука: студент возьмёт «4 часа GPU на задачу IMO» как факт цитирования. Это **inverted направление** + **invented technical detail**.

**Recommended fix (one of two paths):**

**Path A (drop fabricated example):** Удалить полностью lines 197b-205 («AlphaProof — три остальные задачи (алгебра, теория чисел, комбинаторика)» + «Конкретный пример: как AlphaProof решил задачу 3 IMO 2024» весь параграф). Заменить на:
> «AlphaProof — три задачи из не-геометрических (P1 алгебра, P2 теория чисел, P6 алгебра). Две комбинаторные задачи (P3, P5) остались нерешёнными — формализация комбинаторных задач в Lean сложнее, и поиск становится экспоненциально дорогим.»

**Path B (replace with actual solved task):** Если worked example нужен — переписать его для **задачи P1 (algebra)** или **P2 (number theory)** или **P6 (algebra)**. **Но**: конкретные числа (50 строк Lean, 10 000 кандидатов, 4 часа GPU) не подтверждены primary source per-task — DeepMind blog даёт общую оценку времени «days for some problems» на cluster, не «4 hours per task». Risk: фабрикация остаётся, просто на другом target.

**Path A recommended** — drop example полностью и оставить только аккуратный pointer к DeepMind blog для деталей.

### P0-NEW-2: GNoME активное обучение «~22 раза» вместо 6 раундов

**Where:** chapter-part2.md §2.4 line 121.

**Chapter claim:**
> «Стартуя со ~50 000 известных стабильных материалов, модель генерирует 100 000 модификаций ... отбирает топ-10% наиболее вероятно стабильных, отправляет их на DFT-проверку (~1 час на структуру), результаты добавляются в тренировочный корпус, **цикл повторяется ~22 раза**. После 22 циклов модель имеет 2,2 миллиона предсказанных кандидатов.»

**Primary source — Nature s41586-023-06735-9 + Google DeepMind blog (Nov 2023):**
- «The procedure of retraining and evaluation was completed **six times**, yielding a total of 381,000 stable crystal discoveries.»
- **6 rounds (раундов) of active learning, NOT 22.**

**Delta:** 22 → 6. Off by factor 3.7×. 

**Severity rationale:** P0 — false fact, conkretная неверная цифра в технической методологии. Не блокирующая обширную historical претензию (GNoME действительно discovered 380k stable materials через active learning), но конкретное число итераций ошибочно.

**Recommended fix:**
> «цикл повторяется **6 раз**. После 6 циклов модель имеет 2,2 миллиона предсказанных кандидатов»

(Также проверить chain: «После 22 циклов» — also fix к «После 6 циклов».)

**Additional concern in same section:** chapter claims «около 380 000 GPU-часов — крупнейший высокопроизводительный DFT-расчёт в истории на момент 2023 года». Web search не подтверждает «380 000 GPU-hours» specifically. Per literature ~216 000 DFT calculations at consistent settings were performed for comparison. The 380 000 figure may be conflating «380 000 stable discoveries» with «380 000 GPU-hours» — **P2 missing source for specific compute claim**.

---

## Section D. NEW P1 FACT ERRORS

### P1-NEW-1: Akdel/Bryant arxiv 2510.15939 hallucinated author

**Where:** chapter-part4.md References entry 33.

**Chapter claim:**
> «**33.** Bryant, P., et al. (2025). AlphaFold IDP follow-up. **arxiv**, 2510.15939.»

**Primary source — arxiv.org/abs/2510.15939:**
- Actual authors: **Shreya Gopalan, Sundar Narayanan**.
- Title: «Hallucinations in AlphaFold3 for Intrinsically Disordered Proteins with disorder in Biological Process Residues»
- Submitted: October 8, 2025; revised November 11, 2025.

**Delta:** Author attribution wrong. «Bryant» не в author list. Это **fabricated author**, что считается hallucinated citation по criteria fact-checker'а.

**Severity:** P1 (cite hygiene) — paper exists и real, но author attribution invented. Sub-P1 because affects only reference entry, не narrative claim; if reader follows arxiv ID — найдёт actual paper.

**Recommended fix:**
> «**33.** Gopalan, S., Narayanan, S. (2025). Hallucinations in AlphaFold3 for IDPs with disorder in Biological Process Residues. **arxiv**, 2510.15939.»

Also in narrative §2.1 (chapter-part2.md line 51) and §3.5 (chapter-part3.md line 120): chapter currently не называет «Bryant» в narrative — narrative использует «продолжение анализа — arxiv:2510.15939, 2025» и «последующий анализ 2025 года другой группы». ✓ Narrative OK if reference entry corrected.

### P1-NEW-2: Charlton-Perez 2024 неверный журнал

**Where:** chapter-part4.md References entry 13.

**Chapter claim:**
> «**13.** Charlton-Perez, A., et al. (2024). AI weather models on extreme events. **GRL**, 51.»

**Primary source — Nature s41612-024-00638-w:**
- Title: «Do AI models produce better weather forecasts than physics-based models? A quantitative evaluation case study of Storm Ciarán»
- Authors: Charlton-Perez, Driscoll, et al.
- Journal: **npj Climate and Atmospheric Science**, vol. 7, Article 93 (April 22, 2024)
- DOI: 10.1038/s41612-024-00638-w
- **NOT Geophysical Research Letters (GRL)**

**Delta:** Journal name wrong (npj Climate Atmos Sci → GRL). Title shortened to generic «AI weather models on extreme events».

**Severity:** P1 (cite hygiene + bibliographic error). Citation maps к real paper но wrong journal + simplified title.

**Recommended fix:**
> «**13.** Charlton-Perez, A., Driscoll, S., et al. (2024). Do AI models produce better weather forecasts than physics-based models? A quantitative evaluation case study of Storm Ciarán. **npj Climate and Atmospheric Science**, 7, Article 93.»

Note: chapter-part2.md §2.6 line 182 narrative reference уже корректно говорит «мета-анализ Charlton-Perez et al., 2024» (general framing OK), но reference entry needs journal fix.

---

## Section E. Numbers convention lock spot-check (10 anchors)

| # | Claim | Chapter location | Source verify | Status |
|---|---|---|---|---|
| 1 | AlphaFold 3 release 8 мая 2024 | chapter-part2.md §2.1 line 47 | Nature s41586-024-07487-w, 8 May 2024 | ✓ |
| 2 | AlphaFold DB 200M+ | chapter-part2.md §2.2 line 84 | Current ~214M | ✓ (`[VFY-day-of]` properly flagged) |
| 3 | Nobel Chemistry 9 окт 2024 | chapter.md §0.2 line 121, chapter-part2.md §2.1 line 71 | nobelprize.org | ✓ |
| 4 | GNoME 2.2M / 380k stable | chapter-part2.md §2.4 line 119 | Nature s41586-023-06735-9 | ✓ (numbers OK; **iteration count P0**) |
| 5 | A-Lab 41 of 58 в 17 дней | chapter-part2.md §2.4 line 127 | Nature s41586-023-06734-w | ✓ |
| 6 | Palgrave-Schoop 35 of 36 + 3 типа | chapter-part2.md §2.5 (lines 134-150) | ChemRxiv 65957d349138d231611ad8f7 (Jan 2024) | ✓ (3 типов классификация — добавленный в v2 detail, verifiable per Palgrave preprint) |
| 7 | AlphaProof IMO 28/42 silver | chapter-part2.md §2.7 line 197 | DeepMind blog July 2024 + Nature s41586-025-09833-y | ✓ для 28/42 silver / 4 of 6 / 4+ часа per problem. **НО Task 3 не решена — P0** |
| 8 | FrontierMath 52.4% GPT-5.5 Pro May 2026 | chapter-part2.md §2.7 line 209 | BenchLM.ai | ✓ (volatile) |
| 9 | Galactica 15-17 Nov 2022 (3 дня) | chapter.md §0.2 line 123 | MIT Tech Review Nov 18 2022 | ✓ |
| 10 | Coscientist CMU Boiko Nature Dec 2023 (GPT-4 + Claude) | chapter.md §1.3 line 256 | Nature s41586-023-06792-0 | ✓ |

**Verified: 9 of 10 ✓; 1 P0 на AlphaProof task 3.**

---

## Section F. New claims audit (Phase 4 expansion — 5-7 claims)

### F1. Evoformer architecture (§2.1 chapter-part2.md line 43)
**Claim:** «evoformer: глубокая (48 блоков) трансформерная сеть с парным представлением и MSA-представлением ... triangular attention»

**Verify (per Jumper et al. 2021 Nature s41586-021-03819-2):** 48 evoformer blocks ✓. Pair representation + MSA representation ✓. Triangular attention (between residues) ✓. **All technical claims accurate.** Recycling 3 циклов ✓ (recycling iterations: AF2 default 3-4).

**Status: ✓ verified accurate per primary source.**

### F2. GNoME methodology (§2.4 chapter-part2.md line 121)
**Claim:** «22 итерации, 380k DFT-валидаций, ~50 000 → +100 000 modifications per iter ...»

**Verify:** **22 итерации = WRONG (6 rounds per Nature paper)** — P0 above.

**Status: ✗ P0 issue on iteration count. Other technical detail (DFT cost ~1 GPU-hour per structure ✓; energy above hull <50 meV/atom criterion ✓; ~50k стартовых известных стабильных ✓) — accurate. Only iteration count wrong.**

### F3. Aurora 4D-Var data assimilation (§2.6 chapter-part2.md line 188)
**Claim:** «4D-Var ассимиляция данных в IFS использует 50 миллионов наблюдений в день в начальное состояние модели через минимизацию функции ошибки ... десятилетия валидации, инкорпорирует физические законы сохранения»

**Verify (per ECMWF documentation):** 4D-Var operationally used in IFS since 1997 ✓. Volume ~10-50 million observations per day for global system ✓ (chapter's «50M» is upper estimate, OK). Conservation laws preservation ✓ (4D-Var формулировка corporates these via constraints/adjoint formulation).

**Status: ✓ verified accurate technical description.**

### F4. AlphaProof Lean IMO task 3 worked example (§2.7 chapter-part2.md line 203)
**Status: ✗ P0 CRITICAL — fabricated. Task 3 was unsolved by AlphaProof.**

### F5. AIRI publications Nature Communications 2024-2025 (§5.6 chapter-part4.md line 202)
**Claim:** «AIRI имеет публикации в Nature Communications 2024-2025 по открытым конкурентам AlphaFold и применению к российским биологическим исследовательским вопросам. Конкретный пример — публикация 2024 года в Nature Communications по применению трансформер-архитектуры для предсказания структуры антимикробных пептидов российской биотех-индустрии.»

**Verify:** Could not confirm specific AIRI Nature Communications publication for «антимикробные пептиды + transformer + 2024». AIRI publications page airi.net not searchable in this verify pass. **UNVERIFIABLE без direct access.** This is a P2 — should either cite specific paper title + DOI or hedge language to «AIRI scientific output in 2024-2025 includes publications in Nature Communications».

**Status: P2 unverifiable specific claim (within RU context expansion section; reasonable but not directly verifiable).**

### F6. Sber AI Lab cluster ~5000 GPU H100 (§5.6 chapter-part4.md line 218)
**Claim:** «внутренний кластер Sber оценивается в ~5 000 GPU H100 (по открытым данным, состоянием на 2024 год)»

**Verify:** No direct public source for specific «5000 H100s». Sber publicly disclosed «Christofari Neo» supercomputer (V100-based, 2022) and «Christofari» (V100); H100 deployments не публично запорированы для конкретного числа в 5000. **Possibly true but unverifiable from openly available sources.** P2.

**Status: P2 — claim plausible (Sber has biggest РФ AI compute), но specific 5000 H100 — unverifiable.**

### F7. TPU equivalent compute gap ($10-50M vs РНФ $50-150k = 20-50× compute gap) (§5.6 chapter-part4.md line 242)
**Claim:** «TPU-эквивалент стоимости обучения фундаментальной модели масштаба AlphaFold 3 оценивается DeepMind как ~$10-50 миллионов (включая весь итеративный процесс разработки). Стоимость одного раунда обучения модели — ~$1-3 миллиона. ... грант РНФ по AI4Science (~₽5-15 миллионов = ~$50k-$150k) — этого хватает на 2-5% стоимости одного раунда обучения. Это структурный разрыв 20-50×»

**Verify:** $1-3M per training run для AlphaFold-class model — plausible (consistent with published rough estimates for foundation-model training). $10-50M total dev cost — plausible (DeepMind не disclosed точную цифру, но в правильном порядке). РНФ grant ~₽5-15M for 2-3 year project — plausible based on РНФ public программа scale. **Magnitude correct** (20-50× gap directionally accurate). **P2 caveat:** specific numbers (especially $10-50M) — estimates without single primary source; chapter properly hedges с «оценивается».

**Status: ✓ Directionally accurate magnitudes; P2 для precision (estimates with proper hedging).**

---

## Section G. References list quality — 10 random sample

| # | Citation | Verified | Issue |
|---|---|---|---|
| 1 | Jumper et al. 2021 Nature 596:583 [AlphaFold 2] | ✓ | — |
| 2 | Abramson et al. 2024 Nature 630:493 [AlphaFold 3] | ✓ | — |
| 3 | Corso, Wohlwend et al. 2024 bioRxiv 2024.11.19.624167 [Boltz-1] | ✓ | — |
| 4 | Merchant, Batzner et al. 2023 Nature 624:80 [GNoME] | ✓ | — |
| 5 | Szymanski et al. 2023 Nature 624:86 [A-Lab] | ✓ | — |
| 6 | Boiko et al. 2023 Nature 624:570 [Coscientist] | ✓ | — |
| 12 | ECMWF AIFS Team (2025) operational deployment 25 Feb 2025 | ✓ | — |
| **13** | **Charlton-Perez et al. 2024 «AI weather extreme» GRL 51** | ✗ | **P1** — wrong journal (npj Climate Atmos Sci, not GRL) |
| 29 | Ashton, Malz, Colombo (2025) arxiv 2504.17587 | ✓ | — |
| **33** | **Bryant et al. (2025) arxiv 2510.15939** | ✗ | **P1** — wrong authors (Gopalan & Narayanan) |
| 36 | GPTZero Research (2026) arxiv 2602.05930 NeurIPS | ✓ | — |
| 60 | Указ Президента РФ № 490 kremlin.ru/acts/bank/44731 | ✓ | — |
| 61 | Указ Президента РФ № 124 kremlin.ru/acts/bank/50091 | ✓ | — |

**Verified: 11 of 13 sampled ✓. 2 P1 bibliographic errors (#13 + #33) — both in references introduced/modified in v2 revision.**

---

## Section H. Hallucinated source URLs / IDs (NEGATIVE finding mostly)

### Confirmed real (sampled 10):
- ✓ arxiv 2602.05930 (NeurIPS fake citations) — real, authors GPTZero Research et al.
- ✓ arxiv 2510.15939 — real, but **authors не «Bryant» — это Gopalan & Narayanan** (P1 above)
- ✓ arxiv 2504.17587 — real, Ashton/Malz/Colombo 2025 ✓
- ✓ arxiv 2502.03544 (AlphaGeometry 2)
- ✓ arxiv 2408.06292 (Sakana v1)
- ✓ arxiv 2504.08066 (Sakana v2)
- ✓ arxiv 2512.00967 (TESS exoplanet ML)
- ✓ arxiv 2405.13063 (Aurora)
- ✓ kremlin.ru/acts/bank/44731 (Указ 490 — real Kremlin URL pattern; specific path exists)
- ✓ kremlin.ru/acts/bank/50091 (Указ 124 — real Kremlin URL pattern)

**Hallucinated source count: 1** (Bryant author attribution для real arxiv 2510.15939 paper).

**Sources real, attributions wrong для 2 entries (Bryant + Charlton-Perez journal).**

---

## Section I. Residual P2 from v1 — most addressed

### Status of v1 P2 items in v2:
- ✓ ECMWF AIFS date precision — fixed (25 Feb 2025)
- ✓ References list expanded из ~30 → ~120 entries (per changelog claim; sampled 13 mostly OK; 2 P1 errors above)
- ✓ Sakana percentile framing — addressed via 3-метрик table в §1.2 (3% selection / 33% marketing / 1% autonomy)
- ✓ `[VFY-day-of]` markers стандартизированы (per changelog)
- P2 residual: §1.2 line 260 «ICLR 2024 acceptance 24,52%» — это NeurIPS 2025 number — should fix к «NeurIPS 2025 acceptance 24,52%» либо drop conference label

---

## Top P0/P1 fact-fixes summary (for orchestrator)

### P0 BLOCKING — must fix before GATE A:

1. **P0-NEW-1 (CRITICAL):** chapter-part2.md §2.7 lines 197-205 — **drop fabricated worked example «как AlphaProof решил задачу 3 IMO 2024»**. AlphaProof не решал task 3. Recommend Path A: remove entire fabricated paragraph (lines 197b-205), replace with brief accurate framing: «AlphaProof решил P1 алгебра, P2 теория чисел, P6 алгебра; обе комбинаторные задачи (P3, P5) остались нерешёнными». Also fix line 197 «комбинаторика» среди решённых → drop «комбинаторика».

2. **P0-NEW-2:** chapter-part2.md §2.4 line 121 — fix «цикл повторяется ~22 раза» → «**6 раз**» (per Nature s41586-023-06735-9 Methods). And same line «После 22 циклов» → «После 6 циклов». ~380 000 GPU-часов claim — verify against primary source or hedge to «hundreds of thousands of GPU-hours».

### P1 — should fix before GATE A:

3. **P1-NEW-1:** chapter-part4.md References entry 33 — fix «Bryant, P., et al. (2025)» → «**Gopalan, S., Narayanan, S. (2025)**» (per arxiv 2510.15939 actual authors).

4. **P1-NEW-2:** chapter-part4.md References entry 13 — fix «**GRL**, 51» → «**npj Climate and Atmospheric Science**, 7, Article 93» (per Nature s41612-024-00638-w).

### P2 residual:

5. chapter.md §1.2 line 260 — «ICLR 2024 acceptance 24,52%» — это actually NeurIPS 2025 number. Either re-label conference or drop label.
6. chapter-part2.md line 71 «Recursion (раскрытие финансирования см. ниже)» — dangling «см. ниже» reference. Either provide Recursion-Roche specific number ($150M upfront) or drop reference.
7. AIRI / Sber AI Lab specific publication / GPU count claims — should add `[VFY-day-of]` flag if не cited specifically with DOI/title.

---

## Counts summary

- **Verdict:** **REVISE** (2 P0 NEW — fabricated AlphaProof example + GNoME iteration count; 2 P1 NEW — Bryant + Charlton-Perez journal)
- **v1 P0 closures:** 2 of 2 closed ✓
- **v1 P1 closures:** 7 of 7 closed ✓
- **NEW P0 (v2 introduced):** 2
- **NEW P1 (v2 introduced):** 2
- **Numbers convention spot-check:** 9 of 10 ✓ (1 P0 cascading from §2.7)
- **References sample audit:** 11 of 13 ✓ (2 P1 bibliographic errors)
- **Hallucinated sources:** 1 (Bryant attribution для real arxiv 2510.15939)
- **UNVERIFIABLE:** 2 P2 (AIRI specific Nature Communications paper; Sber 5000 H100 GPU count)

---

## Recommend

**focused fact-fix mini-revision** (~30-45 мин estimated):

1. chapter-part2.md §2.7 lines 197-205 — drop fabricated AlphaProof task 3 worked example, replace with accurate brief framing (P0-NEW-1 fix).
2. chapter-part2.md §2.4 line 121 — fix 22→6 iterations; verify 380k GPU-hours claim or hedge (P0-NEW-2 fix).
3. chapter-part4.md References entry 33 — fix Bryant → Gopalan & Narayanan (P1-NEW-1 fix).
4. chapter-part4.md References entry 13 — fix GRL → npj Climate Atmos Sci, vol 7, article 93 + add Storm Ciarán to title (P1-NEW-2 fix).
5. P2 polish optional (lines 260, line 71, AIRI VFY flag).

После mini-revision: re-verify P0 closures (2 spot-checks), затем open GATE A.

**End of report.**

---

## Source log (this round)

- arxiv 2510.15939: https://arxiv.org/abs/2510.15939 (Gopalan & Narayanan 2025; NOT Bryant)
- arxiv 2602.05930: https://arxiv.org/abs/2602.05930 (NeurIPS GPTZero — confirms 21 575 / 5 290 / 24.52% / 53 papers / 100+ citations)
- Nature s41586-025-09833-y: AlphaProof IMO 2024 — confirms P1, P2, P6 solved (algebra/number theory/algebra), P3 + P5 unsolved (combinatorics)
- DeepMind blog «AI achieves silver-medal standard»: https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/
- Nature s41586-023-06735-9 (GNoME): «procedure ... completed six times, yielding 381,000 stable crystal discoveries»
- npj Climate Atmos Sci 10.1038/s41612-024-00638-w (Charlton-Perez et al. Storm Ciarán): published 22 April 2024
- Insitro Series C: BusinessWire + Crunchbase — confirmed $400M March 15 2021
- ECMWF AIFS operational: https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational (25 February 2025)
- kremlin.ru/acts/bank/44731 (Указ № 490 от 10 окт 2019)
- kremlin.ru/acts/bank/50091 (Указ № 124 от 15 фев 2024)
