# Fact-Checker Report — Лекция 15 slides v1 (rendered PPTX) — 2026-05-27 (Phase 7 focused slides fact-check)

**VERDICT: REVISE**

**Rationale.** Cascade-integrity Phase 4.5/4.6/4.7 fixes (chapter v2.1+v2.2) **в основном пропагированы** в rendered PPTX visible body + speaker notes (10 из 11 anchors ✓ канонически). Однако **6 новых P0 (hallucinated arxiv IDs + fabricated numbers + wrong journal volume)** introduced by Phase 5/6 designer expansion — несколько hallucinated arxiv identifiers, неверный Nature volume для Coscientist, fabricated count для TESS exoplanets (2 449 vs реальные 1 595 + wrong first author), BLS algorithm date (1976 vs 2002), Boltz-1 arxiv ID, MICrONS Nature volume + neuron count. Эти P0 — структурные ошибки, проникшие в visible PPTX и speaker notes, блокируют APPROVE до Phase 8 fact-fix.

## Severity counts

- **P0 (hallucinated arxiv IDs + false fact / wrong number / wrong journal vol):** **6 NEW**
- **P1 (suspicious framing, attribution conflation, dated misalignment):** **5 NEW** (Galactica date conflation, Materials Project baseline framing, Recursion-Roche upfront framing, Akdel-Gopalan citation conflation, MICrONS Nature volume + neuron count в одной P1 cluster)
- **P2 (minor cite format, attribution ambiguity, NotebookLM users framing, Boltz-2 month):** ~5 minor
- **Cascade-integrity ✓:** 10 of 11 P0 anchors из Phase 4.5/4.6/4.7 chapter-fixes propagated cleanly
- **Hallucinated sources/IDs detected:** **4** (arxiv 2412.01184 Boltz-1, arxiv 2503.07372 Sakana, arxiv 2509.03029 AlphaProof, Nature volume 593 Coscientist)
- **UNVERIFIABLE:** 0 critical

---

## Section A. Cascade integrity from Phase 4.5/4.6/4.7 chapter fixes — 11 anchors

| # | Chapter-canonical fact (post Phase 4.5-4.7) | Slide propagation | Verdict |
|---|---|---|---|
| 1 | **A-Lab 41 of 58 в 17 дней** | s16 visible body «41 из 58 успешно (71%)»; s12 divider «41 из 58 за 17 дней»; s17 «41/58»; s38 «41 из 58 за 17 дней»; speaker notes s16/s17/s38 — все «41 из 58» канонически | ✓ |
| 2 | **GNoME 6 раундов active learning** (not 22) | s16 visible body «+ 6 раундов активного обучения»; s16 speaker notes «Modify: не «22 итерации» как часто пишут в популярной литературе — а ровно 6 раундов активного обучения» — **canonical + explicit anti-pattern callout** | ✓ |
| 3 | **Palgrave 35 of 36 errors** | s17 visible body «3 типа ошибок (35 из 36)»; s12 divider «Палгрейв-Шуп критика: 35 из 36 проб с ошибками»; s38 «35 из 36 содержит ошибки»; speaker notes везде «35 из 36» | ✓ |
| 4 | **Nobel 9 октября 2024** (not 8) | s01 visible body «9 октября 2024»; s13 visible body «9 октября 2024 — Нобелевская премия по химии»; speaker notes s01/s13 — «9 октября 2024» | ✓ (verified against nobelprize.org) |
| 5 | **NeurIPS 2025 21 575 / 5 290 / 24,52%** (not 15 000 / 3 700) | s30 visible body «21 575 поданных статей / 5 290 принятых / Acceptance rate 24,52%»; s04 glossary «NeurIPS 2025 — 24,52% принято»; s30 speaker notes — все canonical | ✓ (verified against NeurIPS 2025 PC chairs blog) |
| 6 | **AlphaProof P1/P2/P6 solved, P3+P5 unsolved** (no Task 3 fabrication) | s19 visible body «Решены: P1, P2, P6 (по 7 баллов)»; «Не решены: P3 и P5 (комбинаторика)»; s19 speaker notes — каноническое распределение | ✓ (verified against DeepMind blog) |
| 7 | **Recursion-Roche декабрь 2021 / 40 программ × >$300M / ~$12B** | s13 visible body «декабрь 2021 / Recursion + Roche — $300M / 40 программ × >$300M = до $12B»; s13 speaker notes «$150 миллионов upfront плюс до сорока программ по более чем 300 миллионов milestones каждая — суммарный потенциал до 12 миллиардов» | ⚠ partial — s13 visible body показывает «$300M» как headline figure в timeline-row, что может быть прочитано как upfront (актуально $150M upfront). Speaker notes — каноническая полная формулировка. P1 framing leak в visible body |
| 8 | **Указ Президента РФ № 490 (2019) + № 124 (2024)** | s37 visible body «Указ № 490 от 10 октября 2019 / Указ № 124 от 15 февраля 2024»; speaker notes аналогично | ✓ |
| 9 | **Insitro Series C $400M** | s13 «Insitro — Series C $400M, 2021» — только в slide MD, **не в rendered visible body** (timeline row на rendered показывает только Recursion-Roche); упоминание ОТСУТСТВУЕТ в rendered PPTX visible | ⚠ insitro mention dropped from rendered visible body (только в slide MD source). Speaker notes тоже не включают Insitro. Minor regression — не P0 |
| 10 | **ECMWF AIFS 25 февраля 2025 operational** (не просто «с 2024») | s18 visible body «AIFS оперативна с 25 февраля 2025 — собственная AI-модель ECMWF, не Aurora»; s04 glossary «AIFS оперативно с 25 фев 2025»; s18 speaker notes — каноническая дата | ✓ (verified against ECMWF news) |
| 11 | **Coscientist GPT-4 + Claude both** | s09 visible body «GPT-4 + Claude (оба, не один)»; s09 speaker notes «GPT-4 и Claude используются оба, как два разных reasoner-агента» — каноническая формулировка | ✓ |

**Cascade integrity sub-score: 9 of 11 fully ✓ canonical; 2 partial regressions (P1 «$300M» framing на s13 + Insitro dropped from rendered visible).**

---

## Section B. New P0 — Hallucinated arxiv IDs + wrong publication metadata (introduced by Phase 5/6 designer expansion)

### P0-NEW-1: Slide s09 visible body «Nature 593 (декабрь 2023)» for Coscientist

**Fact:** «Публикация: Nature 593 (декабрь 2023) / Boiko, MacKnight, Kline, Gomes»

**Source verification:**
- nature.com/articles/s41586-023-06792-0 — Coscientist paper **Nature volume 624** (December 21, 2023, issue 7992), DOI 10.1038/s41586-023-06792-0.
- Nature volume 593 corresponds to May 2021 (unrelated to Coscientist).

**Issue:** Designer-introduced wrong volume number в visible PPTX body. Chapter-part4 references entry #16 corrente Nature **624** ✓; slide source `.md` says только «Nature, doi:10.1038/s41586-023-06792-0» (без volume); rendered PPTX visible body hardcoded **«Nature 593»** в `build_lec15_slides.py:471`.

**Severity:** P0 (false fact в visible body, prominently displayed на attribution row).

**Recommendation:** Replace «Nature 593 (декабрь 2023)» → «Nature 624 (декабрь 2023)».

---

### P0-NEW-2: Slide s21 + s25 — arxiv 2512.00967 attribution + count mismatch

**Fact (s21 visible body):** «3 987 кандидатов из TESS surveys / CNN → ranking / **2 449 высокоуверенных (точность 83,9%)**»

**Fact (s21 attribution):** «Источники: Shallue & Vanderburg ApJ 155 (2018) · **Cui et al. arxiv 2512.00967**»

**Source verification (verified via arxiv.org/abs/2512.00967):**
- arxiv 2512.00967: «Machine Learning for Exoplanet Discovery: Validating TESS Candidates and Identifying Planets in the Habitable Zone»
- **Authors: Sarah Huang and Chen Jiang** (NOT «Cui et al.»)
- **Identified 1 595 new high-confidence planets** (NOT 2 449)
- 3 987 TESS candidates ✓
- 83.9% cross-validation accuracy ✓
- Recovered 86% (358/418) of previously confirmed TESS exoplanets (separate metric)

**Issue:** Two errors in single citation:
1. **Wrong first author:** «Cui et al.» — paper authored by Huang & Jiang.
2. **Fabricated count:** «2 449» — actual paper reports **1 595**.

**Cascade:** Error propagated to chapter-part3.md line 67 («2 449 высокоуверенных»), chapter-part4 references entry #25 («Cui, A., et al. (2025)»), slide s21 visible body, s21 speaker notes, slide s25 visible body, s25 speaker notes, build_lec15_slides2.py line 491 + 700 + 737. Это **multi-artifact propagation** — error originated в chapter Phase 4 expansion и cascaded в slides.

**Severity:** P0 BLOCKING (fabricated number + wrong attribution в visible body + cascade across artifacts).

**Recommendation:** Replace «Cui et al.» → «Huang & Jiang» (2025). Replace «2 449 высокоуверенных» → **«1 595 высокоуверенных»** across all artifacts (chapter-part3, chapter-part4 refs #25, s21 visible body + speaker notes, s25 visible body + speaker notes, deck.yaml/Source files).

---

### P0-NEW-3: Slide s21 + s25 + s33 visible body — BLS «1976»

**Fact (s21 visible body):** «AUC от BLS (1976) 78% → pre-trained CNN 89% → custom CNN на TESS+Kepler 92%»

**Fact (s25 visible body):** «BLS алгоритм 1976 → 78% baseline»

**Source verification:**
- Kovács, G., Zucker, S., Mazeh, T. (2002). «A box-fitting algorithm in the search for periodic transits». A&A, 391, 369-377.
- BLS algorithm for transit detection — **2002**, not 1976.
- Chapter-part4 references entry #26 correctly cites «Kovács, G., et al. (2002). BLS. **A&A**, 391, 369-377» ✓.

**Issue:** Designer-introduced fabricated date «1976» в visible body + speaker notes контрадицирует chapter's own references entry. Likely confused с another algorithm or fabricated entirely.

**Cascade:** Error in s21 visible body + s21 speaker notes + s25 visible body «BLS алгоритм 1976 года — 78% AUC» + s25 speaker notes «BLS (Box Least Squares) с 1976 года» + build_lec15_slides2.py.

**Severity:** P0 (false fact: dating canonical algorithm 26 years wrong, conflicts with own chapter references).

**Recommendation:** Replace «BLS (1976)» / «BLS алгоритм 1976» / «BLS (Box Least Squares) с 1976 года» → **«BLS (Kovács et al. 2002)»** in all visible body + speaker notes.

---

### P0-NEW-4: Slide s15 visible body — hallucinated arxiv 2412.01184 for Boltz-1

**Fact (s15 attribution):** «Источники: Corso, Wohlwend et al. arxiv 2412.01184 (Boltz-1) · Wohlwend et al. biorxiv 2025 (Boltz-2)»

**Source verification (verified via arxiv.org/abs/2412.01184):**
- arxiv 2412.01184: **«Computationally-assisted proof of a novel O(3)×O(10)-invariant Einstein metric on S^12»** by Timothy Buttsworth and Liam Hodgkinson — pure mathematics, unrelated to Boltz-1.
- Actual Boltz-1 preprint: **biorxiv 2024.11.19.624167** (Wohlwend, Corso, Passaro, et al.), DOI 10.1101/2024.11.19.624167.
- Chapter-part4 references entry #3 correctly cites «**bioRxiv**, 2024.11.19.624167» ✓.

**Issue:** Hallucinated arxiv identifier in visible body attribution — totally unrelated mathematics paper. Designer fabricated arxiv ID, didn't cross-check with chapter refs.

**Severity:** P0 (hallucinated source).

**Recommendation:** Replace «arxiv 2412.01184» → **«biorxiv 2024.11.19.624167»** in s15 visible body.

---

### P0-NEW-5: Slide s19 visible body — hallucinated arxiv 2509.03029 for AlphaProof

**Fact (s19 attribution):** «Источник: DeepMind blog июль 2024 · arxiv 2509.03029 (AlphaProof Nature)»

**Source verification (verified via arxiv.org/abs/2509.03029):**
- arxiv 2509.03029: **«Multimodal learning of melt pool dynamics in laser powder bed fusion»** by Mojumder, Halder, Tonge — metal additive manufacturing paper, totally unrelated to AlphaProof.
- Actual AlphaProof Nature paper: DOI 10.1038/s41586-025-09833-y (chapter-part4 ref #15 correctly cites this DOI ✓).

**Issue:** Hallucinated arxiv identifier in visible body. Designer fabricated arxiv ID.

**Severity:** P0 (hallucinated source).

**Recommendation:** Replace «arxiv 2509.03029 (AlphaProof Nature)» → «Nature 2025 doi:10.1038/s41586-025-09833-y» or «DeepMind blog июль 2024 / Nature paper 2025» (canonical chapter reference).

---

### P0-NEW-6: Slide s08 visible body — hallucinated arxiv 2503.07372 for Sakana

**Fact (s08 attribution):** «Источники: Sakana blog 12 марта 2025 · TechCrunch 12 марта 2025 · **Lu et al. arxiv 2503.07372**»

**Source verification (verified via arxiv.org/abs/2503.07372):**
- arxiv 2503.07372: **«Molecular Weight-Dependent Evaporation Dynamics and Morphology of PEG Sessile Drops on Hydrophobic Substrates»** by Feiyu An, Junyi Ye, Huanshu Tan — fluid dynamics paper, unrelated to Sakana AI Scientist.
- Actual Sakana v2 paper: **arxiv 2504.08066** «The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search» by **Yamada, Lange, Lu et al.** (first author Yamada, not Lu).
- Chapter-part4 references entry #18 correctly cites «**arxiv, 2504.08066**» (но first author записан как «Lu, C., et al.» — также incorrect; должен быть «Yamada, Y., et al.»).

**Issue:** Two errors:
1. Hallucinated arxiv ID 2503.07372 — actual is 2504.08066.
2. Wrong first author: «Lu et al.» — actual lead author Yutaro Yamada (Lu is co-author).

**Cascade:** Same error pattern in chapter-part4 refs #18 ([Lu et al. 2025 → должен Yamada et al. 2025]) — multi-artifact wrong attribution.

**Severity:** P0 (hallucinated source + wrong attribution).

**Recommendation:** Replace «Lu et al. arxiv 2503.07372» → **«Yamada, Lange, Lu et al. arxiv 2504.08066»** in s08 visible body. Also fix chapter-part4 references entry #18 lead author.

---

## Section C. New P1 — Suspicious framings, citation conflations, dated misalignments

### P1-NEW-1: Slide s01 speaker notes — Galactica launch date conflation

**Fact:** «17 ноября 2022 года, за два года до этого Нобеля, Meta запустила Galactica»

**Source verification:** Meta launched Galactica **November 15, 2022**; MIT Technology Review article published **November 18, 2022** («Why Meta's Galactica only survived three days online»); retracted Nov 18. «17 ноября» = the day Galactica was withdrawn (3 days after Nov 15 launch).

**Issue:** Speaker notes attribute Nov 17 as launch date — should be Nov 15 launch + Nov 18 retraction (with «прожила три дня» framing).

**Severity:** P1 framing.

**Recommendation:** Replace «17 ноября 2022 года, ... Meta запустила Galactica» → **«15 ноября 2022 года, ..., Meta запустила Galactica»** (или альтернативно: «к 17-18 ноября 2022, через три дня после релиза 15 ноября 2022, Galactica была отозвана»). s01 visible body bridge caption «17 ноября 2022 — Galactica прожила три дня» можно оставить (это retraction date), но в speaker notes должно быть launch=Nov 15.

---

### P1-NEW-2: Slide s24 — Akdel 2022 + Gopalan & Narayanan 2025 attribution conflation for 22%

**Fact (s24 visible body):** «AlphaFold даёт 22% галл. в IDP» (s04 glossary line); «**Akdel et al. Nature Struct Mol Biol 2022 · Gopalan & Narayanan arxiv 2510.15939 (2025)**»

**Source verification:**
- Akdel et al. 2022 (NSMB 29:1056) — community assessment of AlphaFold 2; finding ~15% confidently-folded IDR residues (not 22% hallucinations).
- Gopalan & Narayanan 2025 (arxiv 2510.15939) — «Hallucinations in AlphaFold3 for IDP with disorder in Biological Process Residues» — **22% hallucinations** number is from this paper.

**Issue:** Joint citation lists both papers as source for «22%», but the 22% specifically belongs to Gopalan & Narayanan 2025 (for AlphaFold 3); Akdel 2022 is older AF2 baseline (different metric ~15%).

**Severity:** P1 attribution conflation (true claim, wrong dual-citation).

**Recommendation:** Either: (a) drop Akdel reference and cite only «Gopalan & Narayanan arxiv 2510.15939 (2025)» for the 22% figure; OR (b) explicitly separate: «AF2 baseline IDR confidence ~15% (Akdel 2022); AF3 IDR hallucinations 22% (Gopalan & Narayanan 2025)».

---

### P1-NEW-3: Slide s22 — MICrONS Nature volume + neuron count

**Fact (s22 visible body):** «Allen MICrONS, апрель 2025 — Nature **641** (2025): / Один кубический миллиметр зрительной коры мыши = **84 000 нейронов** · 500 миллионов синапсов · 4 километра аксонов»

**Source verification:**
- Nature publication: «Functional connectomics spanning multiple areas of mouse visual cortex», Nature **volume 640**, April 2025 (NOT 641).
- Neuron count: ~75 000 neurons with functional imaging; ~120 000 neurons in anatomical reconstruction; 200 000 total cells. The «84 000» figure does not match any standard MICrONS metric.
- Synapses: 523 million (≈500M) ✓.
- 4 km axons — consistent ✓.

**Issue:** Two errors clustered: wrong Nature volume (641 → 640) + неточная neuron count (84 000 не отражает реальные ~75k physiology / ~120k anatomical reconstruction).

**Severity:** P1 (small but multiple errors in single attribution row).

**Recommendation:** Replace «Nature 641 (2025)» → «Nature 640 (2025)». Replace «84 000 нейронов» → «~120 000 нейронов в анатомической реконструкции (75 000 с functional imaging)» или эквивалентная formulation matching paper.

---

### P1-NEW-4: Slide s13 — Recursion-Roche «$300M» visible body row framing

**Fact (s13 visible body, timeline row):** «декабрь 2021 / Recursion + Roche — **$300M** / 40 программ × >$300M = до $12B»

**Source verification:**
- Recursion 8-K SEC dec 2021: **$150M upfront**; up to 40 programs each with **>$300M milestones**; total potential up to **~$12B**.
- Slide source md (s13 §Каскадный эффект) correctly states: «$150M upfront / До 40 программ × >$300M milestones каждая / Суммарный потенциал до ~$12 миллиардов».
- Speaker notes correctly state «$150 миллионов upfront плюс до сорока программ по более чем 300 миллионов milestones каждая».

**Issue:** Rendered PPTX timeline row visible body shows headline «**$300M**» on the «декабрь 2021» row — это создаёт misleading framing, что upfront был $300M (тогда как actual upfront $150M, а $300M = per-program max milestone). Speaker notes и slide source MD correct; только rendered visible body framing неточен.

**Severity:** P1 (visible body framing error; not outright false but misleading).

**Recommendation:** Edit visible body timeline row: «декабрь 2021 / Recursion + Roche — $150M upfront / до 40 программ × >$300M милстоунов = до ~$12B» (или sparser: «декабрь 2021 / Recursion + Roche — до $12B потенциал»).

---

### P1-NEW-5: Slide s16 visible body — Materials Project «48k» baseline framing

**Fact (s16 visible body):** «Масштаб vs альтернатив: / Materials Project — 48k / Open Quantum Materials — 60k / GNoME — 380k стабильных (44× больше Materials Project)»

**Source verification:**
- GNoME Nature paper baseline: ICSD experimentally identified ~20 000 stable crystals; Materials Project + OQMD + WBM **combined** ~48 000 stable crystals (boosted by computational efforts); GNoME adds 381 000 new stable materials, total «known stable» = 421 000.
- Materials Project alone currently has 150 000+ entries; OQMD has >1M compounds (different metrics).

**Issue:** «Materials Project — 48k» framing — the 48k baseline в GNoME paper is **MP + OQMD + WBM combined**, not MP alone. Also «Open Quantum Materials — 60k» is inaccurate (OQMD >1M compounds; if «60k» refers to OQMD-stable subset, unclear).

**Severity:** P1 minor (numbers are baseline-correct as cited in GNoME paper, but framing confuses readers about what these baselines represent).

**Recommendation:** Either: (a) replace «Materials Project — 48k / OQMD — 60k» → «MP + OQMD + WBM combined — ~48k stable crystals (per GNoME paper baseline)»; OR (b) preserve dual-listing but add caveat «*stable subsets per GNoME Nature 2023 baseline*».

---

## Section D. New sample claims audit (5 random factual claims verified primary)

| # | Claim | Source | Verdict |
|---|---|---|---|
| 1 | «GPTZero Research анализ: 100+ фейковых цитат / в 53 принятых статьях / (arxiv 2602.05930)» — s30 | arxiv 2602.05930 «Compound Deception in Elite Peer Review: Failure Mode Taxonomy of 100 Fabricated Citations at NeurIPS 2025» — confirmed 100 citations / 53 papers / 4 841 of 5 290 scanned | ✓ canonical |
| 2 | «Aurora 5000× быстрее эталона» — s18, s12, s38 | arxiv 2405.13063 Bodnar et al. — confirmed «approximately 5,000× faster» than IFS | ✓ |
| 3 | «NotebookLM 17 миллионов пользователей» — s27 | a16z Q4 2024 + late 2025 stats — ~17M MAU web (+ 8M mobile); slide framing «17 миллионов» = web-only без mobile distinction; total ~25M | ⚠ P2 framing (web/total ambiguity); 17M technically accurate for web |
| 4 | «Elicit 138 миллионов статей в индексе» — s27 | Elicit website + Texas A&M LibGuides: «138 million academic papers from Semantic Scholar, PubMed, OpenAlex» | ✓ |
| 5 | «Insitro Series C $400M, 2021» — s13 slide MD (но не в rendered visible body) | Insitro press release 15 марта 2021 — $400M Series C led by CPP Investments | ✓ slide MD; but DROPPED from rendered visible body (regression) |
| 6 | «AlphaFold DB 200 миллионов структур vs 200K в PDB» — s14, s39 | EMBL-EBI March 2026 — confirmed 200M+ AlphaFold predicted structures; PDB exhibits ~230k experimental entries as of 2025 | ✓ |
| 7 | «AlphaProof+AlphaGeometry 2: P1/P2/P6 by AlphaProof, P4 by AlphaGeometry, P3+P5 unsolved» — s19 | DeepMind blog 25 July 2024 — confirmed AlphaProof solved P1/P2/P6, AlphaGeometry 2 solved P4, P3/P5 (combinatorics) unsolved, 28/42 silver | ✓ |

---

## Section E. Mock vs real image — fact-checker angle (8 media slides sample)

Без визуального inspection PNG snapshots (separately covered by presentation-critic), невозможно гарантировать real-image identifiability vs stylized mock. Здесь fact-check ограничивается **claim verification** (что изображение должно показывать соответствует reality, если бы оно реально присутствовало).

| Slide | Image claim | Real-source verifiable? |
|---|---|---|
| s01 | Hassabis + Jumper + Baker Нобелевская церемония Стокгольм | ✓ DeepMind blog + nobelprize.org + Wikimedia Commons (real photo exists Dec 10 2024 ceremony) |
| s14 | AlphaFold DB Wikimedia ribbon | ✓ alphafold.ebi.ac.uk + Wikimedia CC-BY-SA AF2 ribbon exists |
| s17 | Palgrave ChemRxiv figure | ⚠ ChemRxiv paywall/access varies; Palgrave Schoop ChemRxiv preprint January 2024 verifiable existence ✓ |
| s21 | NASA TESS light curve / transit | ✓ NASA TESS public images CC-PD; transit light curves widely available |
| s22 | Allen MICrONS composite | ✓ Allen Institute press materials April 2025; MICrONS Nature volume 640 figures CC-BY |
| s23 | LIGO Caltech control room + black hole merger SXS | ✓ LIGO/Caltech press + SXS collaboration public visualizations |
| s27 | NotebookLM UI screenshot | ⚠ UI screenshots могут быть fair-use; freshness changes (UI updates) |
| s37 | AIRI / Sber / Yandex logos | ✓ corporate logos public; institutional cite verifiable (AIRI 2021, Sber AI Lab 2017, Yandex Research 2014 — all confirmed via web) |

Verdict: image attribution claims for 8 media slides — все «real image acquirable» (no fact-side fabrication of attribution). Actual rendered image identifiability — presentation-critic territory.

---

## Section F. Freshness alerts

| Claim | Source date | Current state (2026-05-27) | Refresh cadence | Action |
|---|---|---|---|---|
| «AlphaFold DB 200 миллионов структур» — s14, s39 | 2024 | 200M+ confirmed March 2026; complexes added in March 2026 (separate count) | yearly+ | ✓ no refresh needed; **note**: complexes расширение в March 2026 не упомянуто — могло бы добавить полноты |
| «NotebookLM 17 миллионов пользователей» — s27 | late 2025 | 17M web + 8M mobile (~25M total) | quarterly | ⚠ verify on day-of-lecture; user growth quarterly |
| «NeurIPS 2025: 21 575 / 5 290 / 24,52%» — s30 | NeurIPS 2025 final stats | confirmed canonical | yearly+ | ✓ no refresh |
| «ECMWF AIFS оперативно 25 фев 2025» — s18 | ECMWF news Feb 25 2025 | confirmed; AIFS 1.1.0 update Q3 2025 | yearly | ✓ slide says «AIFS оперативно с 25 фев 2025» — accurate; не упоминает 1.1.0 update — acceptable for narrative |
| «Sakana AI Scientist v2 март 2025 / 1 из 3 ICLR workshop» — s08 | March 2025 | confirmed canonical | yearly | ✓ |
| «Boltz-2 → почти-AlphaFold 3 в academic adoption, осень 2025» — s15 | speaker notes | Boltz-2 released **6 июня 2025** (not autumn) | yearly | P2 minor — replace «осень 2025» → «лето 2025 / июнь 2025» |

---

## P0 fact errors — Top 5 priorities for Phase 8 fact-fix

1. **P0-NEW-2 (BLOCKING):** Slide s21 + s25 + chapter-part3 + chapter-part4 ref #25 — «**Cui et al. arxiv 2512.00967 / 2 449 высокоуверенных**». Actual: Huang & Jiang, **1 595** high-confidence planets. Cascade fix needed (chapter+slides+speech if mentioned).
2. **P0-NEW-1 (BLOCKING):** Slide s09 visible body «Nature **593** (декабрь 2023)» for Coscientist. Actual: **Nature 624**. Single-line build script fix in `build_lec15_slides.py:471`.
3. **P0-NEW-3 (BLOCKING):** Slides s21, s25, speaker notes — «BLS **1976**». Actual: Kovács et al. **2002** (chapter-part4 ref #26 already correct). Fix all 4 visible body + speaker notes mentions.
4. **P0-NEW-5:** Slide s19 — hallucinated «arxiv 2509.03029» for AlphaProof Nature. Replace with «Nature 2025 doi:10.1038/s41586-025-09833-y» or canonical DeepMind blog reference.
5. **P0-NEW-6:** Slide s08 — hallucinated «arxiv 2503.07372» + wrong first author «Lu et al.» for Sakana v2. Replace with **«Yamada et al. arxiv 2504.08066»**. Also fix chapter-part4 ref #18 lead author.

(Plus P0-NEW-4: slide s15 hallucinated «arxiv 2412.01184» Boltz-1 → biorxiv 2024.11.19.624167.)

## P1 fact gaps — recommended for Phase 8 fact-fix

1. **P1-NEW-3:** Slide s22 — Nature volume **641 → 640**, neuron count «84 000» → «120 000 (анатом.) / 75 000 (functional)».
2. **P1-NEW-4:** Slide s13 visible body timeline row «$300M» framing → restore «$150M upfront / до $12B потенциал».
3. **P1-NEW-1:** Slide s01 speaker notes Galactica launch date «17 ноября» → «15 ноября» (или explicit «15 ноября launch / 17-18 ноября retraction»).
4. **P1-NEW-2:** Slide s24 attribution — disambiguate Akdel 2022 (AF2) vs Gopalan & Narayanan 2025 (AF3, 22%).
5. **P1-NEW-5:** Slide s16 visible body — Materials Project «48k» framing clarification.

Plus:
- Insitro regression (dropped from rendered visible body) — consider restoring for completeness.
- s37 «Yandex Research с 2014» — Yandex AI Lab founded 2014; confirm; brand «Yandex Research» более recent — verify.

---

## Hallucinated source URLs / IDs detected — 4 total

1. **arxiv 2412.01184** for «Boltz-1» — actually mathematics paper (Buttsworth & Hodgkinson, Einstein metrics on S^12).
2. **arxiv 2503.07372** for «Sakana v2» — actually fluid dynamics paper (An, Ye, Tan, PEG droplets).
3. **arxiv 2509.03029** for «AlphaProof Nature» — actually metal additive manufacturing paper (Mojumder, Halder, Tonge).
4. **Nature volume 593** for «Coscientist 2023» — actually a 2021 issue with unrelated content.

All four are **classic LLM-hallucinated identifiers** — designer fabricated plausible-looking arxiv IDs without cross-checking against arxiv.org. Chapter-part4 references list mostly correct; cascade-failure happened during Phase 5/6 slide build script authoring.

---

## Recommendation for Phase 8 priorities

1. **Cross-check ALL arxiv / DOI / journal-volume IDs in slides visible body + speaker notes** against actual database (arxiv.org abstract pages). Even single-character ID errors → completely unrelated paper.
2. **Fix multi-artifact cascade error 2 449 → 1 595** (chapter-part3, chapter-part4 ref #25, s21, s25, build script).
3. **Fix BLS 1976 → 2002** across all visible body + speaker notes.
4. **Single-line build script fixes** для P0-NEW-1 (Nature 593 → 624), s15 arxiv ID, s19 arxiv ID, s08 attribution.
5. **Galactica launch date** Nov 17 → Nov 15 в s01 speaker notes (preserve «прожила 3 дня» framing on visible).
6. **Pre-render check rule for Phase 8 retry:** every arxiv/DOI ID in any rendered artifact MUST be verified against database; this batch had 4 hallucinated IDs out of ~15 references, which is unacceptable failure rate.

Cascade integrity itself (Phase 4.5/4.6/4.7 fixes propagation) — strong success: 9 of 11 canonical anchors propagated cleanly; only 2 small partial regressions (s13 framing, Insitro mention dropped). The major issues are **NEW errors introduced by Phase 5/6 designer**, not cascade failures from chapter.

---

**End of report.**
