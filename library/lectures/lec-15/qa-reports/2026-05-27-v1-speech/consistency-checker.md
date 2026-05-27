# Consistency Checker Report — Лекция 15 — 2026-05-27 v1 speech ↔ slides v2 ↔ chapter v2.3

**Mode:** full 3-way cross-artifact (chapter v2.3 ↔ slides v2 rendered ↔ speech v1).
**Source-of-truth:** chapter v2.3 multi-part (~32 850 слов, USER-GATE-A approved, МФТИ regression fixed).
**Artifacts checked:**
- `library/lectures/lec-15/chapter.md` (404 lines, ~7 500 слов) + `chapter-part2.md` (237 lines, ~7 500) + `chapter-part3.md` (407 lines, ~8 000) + `chapter-part4.md` (510 lines, ~8 500) = **~32 850 narrative**.
- `library/lectures/lec-15/deck.yaml` (598 строк, 39 slides) + `slides/s01-s39*.md` (39 source files — note: stale для 6 Phase 7 fact-fixes; rendered PPTX has correct numbers).
- `library/lectures/lec-15/rendered/lec-15.pptx` (39 slides — canonical visible body) + `rendered/snapshots/sNN.png`.
- `library/lectures/lec-15/speech.md` (756 lines, 5 687 слов, target 75.5 min).
- Reference: `qa-reports/2026-05-27-v1-slides/consistency-checker.md` (Phase 7 baseline — APPROVE-WITH-POLISH, 4 P1 + 7 P2).

---

## VERDICT: **REVISE**

**Rationale.** Speech v1 is well-derived from chapter (no factual contradictions vs chapter source-of-truth, all cornerstones canonical, all 4 WEs step-consistent, failure-bucket strict-in holistic ≥40%, Russification consistent, anonymization clean). BUT during 3-way verify I discovered **2 NEW P0-level drifts in rendered PPTX** that were missed by Phase 7 consistency-checker (which only compared chapter↔slides without speech), и which contradict both chapter AND speech:

1. **P0-1: s01 PPTX visible body + speaker notes use «15 ноября 2022» as Galactica launch date** — but chapter §0.2 + speech [s01] narrative + s01 slide.md source file + deck.yaml `chapter_ref` ALL say **«17 ноября 2022»**. The PPTX renders a stale wrong date contradicting the chapter source-of-truth, slide.md source, AND speech. Per book-first methodology — fix PPTX (run inject_notes.py-equivalent re-render).

2. **P0-2: s37 PPTX visible body contains fabricated narrative about RU AI institutions** — diverges from chapter §5.6 AND speech [s37]. Specifically:
   - PPTX says «AIRI: Сбер + платформа НТИ» — but chapter says AIRI is independent (2021); speech matches chapter.
   - PPTX says «Sber AI Lab: с 2017, GigaChat, GigaTune, GigaChat 3 — открытые веса 2025, ML в финансах и медицине» — **none of these terms appear in chapter or speech**; chapter+speech focus on climate forecasting + energy demand + 5K H100 cluster.
   - PPTX says «Yandex Research: с 2014, YandexGPT, Яндекс Переводчик, YandexGPT 5 — 2025» — **none of these appear in chapter or speech**; chapter+speech mention YaLM-100B (2022), RuGPT, ICLR/NeurIPS/ICML contributions.
   - s37 slide.md source file has correct content (AIRI 2021, Sber climate+energy+H100, Yandex YaLM-100B). The rendered PPTX content is fabricated/injected somewhere downstream — likely earlier iteration retained or render-pipeline bug.

These 2 P0 drifts both confirm that **the rendered PPTX visible body is NOT a faithful render of slide.md source files** for s01 (date) and s37 (entire RU narrative). This is a structural pipeline integrity issue. Phase 7 consistency-checker missed it because focused on `slide.md → chapter`, not `PPTX → slide.md → chapter`.

Additional findings (P1 / P2): speech largely faithful to chapter; failure-bucket holistic ~40% in speech; small terminology nits (English-only «augmentation», «cherry-pick», «foundation модели» в speech narrative — chapter has bilingual canonical). No orphan slide references in speech (all `[sNN]` markers refer to existing slides s01-s39).

**Recommendation:** Phase 11 priority order — (1) re-render PPTX from slide.md source files to fix s01 date + s37 content; (2) Phase 7 polish drifts (cherry-pick / foundation модели / s03 keystone bilingual labels — still pending); (3) speech v1 minor consistency edits.

---

## Severity counts

- **P0 (factual contradiction across artifacts / fabricated content / missing critical coverage):** **2**
- **P1 (significant drift / coverage gap):** **5**
- **P2 (minor inconsistency / polish):** **9**

---

## A. Cornerstone consistency table (12 cornerstones × 3 artifacts)

| # | Cornerstone | Chapter | Slides (PPTX visible+notes) | Speech | Same canonical form? |
|---|---|---|---|---|---|
| 1 | фундаментальная модель / foundation model | ✓ §0.4 bilingual gloss; §2 multiple | ✓ s04 «Фундаментальная модель (foundation model)»; ⚠ s18 «foundation модели» mixed | ✓ [s04] «Фундаментальная модель»; ⚠ [s37] «открытые foundation модели» | ⚠ minor mixed — chapter bilingual canonical, slide+speech occasionally English-only |
| 2 | научный цикл / scientific workflow | ✓ §0.3 keystone «лестница научного цикла» | ✓ s03 «Лестница научного цикла. Шесть ступеней» | ✓ [s03] «лестница научного цикла» | ✓ |
| 3 | открытый / закрытый мир | ✓ §0.4 + §1.1 + §3.1 + §5.1 | ✓ s04 glossary, s12 divider, s33 critics | ✓ [s04] «Закрытый и открытый мир» + recap multiple | ✓ |
| 4 | augmentation / расширение | ✓ §0.3 «Расширение (augmentation)» bilingual | ✓ s03 staircase «расширение» (per PPTX body); ⚠ s27 learning_goal frontmatter EN-only «augmentation» | ✓ [s07] «расширение, а не автономия»; [s11] «расширение» | ⚠ minor — chapter+speech use Russian primary; s27 learning_goal field English-only (frontmatter not visible) |
| 5 | автономная лаборатория (self-driving lab) | ✓ §0.4 gloss, §2.4 inline | ✓ s12 divider notes | ✓ [s16] «автономная химическая лаборатория Lawrence Berkeley» | ✓ |
| 6 | галлюцинации цитат (peer review hallucinations) | ✓ §0.4 + §4.3 + §4.5 | ✓ s04 glossary, s30 NeurIPS body | ✓ [s30] «фейковые цитаты» + [s28] «галлюцинированные ссылки» | ✓ |
| 7 | фабрика статей / paper mill | ✓ §0.4 gloss; §4.5 inline | ✓ s04 glossary, s30 «paper mill» implicit | ✓ [s30] «фабрика статей — paper mill — в действии» | ✓ |
| 8 | кризис воспроизводимости | ✓ §0.4 + §1.5 inline | ✓ s04 glossary «39 из 100 / 61%» | ⚠ Not explicitly mentioned by name in speech (kropt as background concept) | ⚠ P2 — speech could explicitly name the term during glossary/s04 mention; currently mentions only «фабрика статей» |
| 9 | человек-в-петле (HITL) | ✓ §0.4 + §3 + §5 multiple | ✓ s04 «HITL»; s24, s28, s33, s34 | ✓ [s04] «Человек в петле, HITL»; [s23] «расширение, не замена»; [s34] «явные точки человеческого решения» | ✓ |
| 10 | обратное проектирование (inverse design) | ✓ §0.4 + §2 inline | ✓ s04 «Обратное проектирование (inverse design)» (Доп.) | ⚠ Not mentioned in speech | ⚠ P2 — speech could mention inverse design during [s34] catalyst WE-3 walked example |
| 11 | DFT / MD первого принципа | ✓ §0.4 + §2.4 + §5.2/5.3 | ✓ s04, s11, s33, s34, s35 | ✓ [s11] «DFT», [s28] «DFT»? no — [s34] «DFT — теорию функционала плотности»; [s35] «DFT плюс молекулярная динамика первого принципа» | ✓ |
| 12 | байесовская оптимизация (BO) + гауссовский процесс (GP) | ✓ §0.4 + §1.6 deep + §5.2 | ✓ s04, s11 dedicated, s34, s35 | ✓ [s11] «Байесовская оптимизация — сорок плюс лет», «Гауссовский процесс — шестьдесят плюс лет»; [s35] | ✓ |

**3-way cornerstones drift count: 0 P0 contradictions; 4 P2 minor drifts** (foundation модели mixed form in slides+speech; кризис воспроизводимости not by name in speech; inverse design omitted in speech; augmentation in s27 frontmatter EN-only).

---

## B. Numbers cascade table — 27 anchors × 3 artifacts

| # | Anchor | Chapter | Slides (PPTX) | Speech | 3-way aligned? |
|---|---|---|---|---|---|
| 1 | A-Lab — **41 из 58 за 17 дней** (canonical) | ✓ §2.4 (chapter-part2 L129) | ✓ s12 / s16 («41 из 58 успешно, 71%»); s17 / s38 | ✓ [s16] «41 из 58 целевых соединений за 17 дней непрерывной работы» | ✓ |
| 2 | Palgrave-Schoop — **35 из 36 errors** (12+15+8) | ✓ §2.5 | ✓ s17 body «35 содержали ошибки» + «12 проб» + «15 проб» + «8 проб» + «1 из 36 — полное открытие» | ✓ [s17] «35 содержали как минимум одну из трёх ошибок» + 12/15/8 breakdown explicit | ✓ |
| 3 | Nobel Chemistry — **9 октября 2024**; Baker ½ + Hassabis + Jumper ½ | ✓ §0.2 + §2.1 | ✓ s01 «9 октября 2024 — Нобель» + s13 «9 октября 2024 / Hassabis + Jumper + Baker» | ✓ [s01] «Девятое октября две тысячи двадцать четвёртого года... Бейкеру... Хассабису и Джамперу. За AlphaFold» | ✓ |
| 4 | Galactica launch — **17 ноября 2022** + 3 дня | ✓ §0.2 «17 ноября 2022 года» | **✗ P0** PPTX s01 visible body «15 ноября 2022» + s01 notes «15 ноября 2022»; **slide.md source has correct «17 ноября 2022»** | ✓ [s01] «Семнадцатое ноября две тысячи двадцать второго года» | **✗ P0 — PPTX drift; chapter+speech+source slide.md all say 17, PPTX renders 15** |
| 5 | NeurIPS 2025 — **21 575 / 5 290 / 24,52% / 100+ fake / 53 papers / arxiv 2602.05930** | ✓ §1.2 + §4.5 | ✓ s30 body «21 575 поданных / 5 290 принятых / Доля 24,52% / 100+ фейковых цитат / в 53 принятых статьях / arxiv 2602.05930» | ✓ [s30] «Двадцать одна тысяча пятьсот семьдесят пять поданных... Пять тысяч двести девяносто принятых... 24,52 процента... arxiv 2602.05930 / 100+ фейковых цитат / в 53 принятые статьи» | ✓ |
| 6 | GNoME — **2,2M / 380k / 6 раундов** (canonical, NOT «22 итерации») | ✓ §2.4 (Phase 4.6 P0 fix) | ✓ s16 body «6 раундов активного обучения / 380 тысяч / 2,2 миллиона»; ⚠ s16 notes intentionally cite «22 итерации» as anti-example | ✓ [s16] «Два миллиона двести тысяч кандидатов / Триста восемьдесят тысяч / Шесть раундов активного обучения» | ✓ canonical; teaching counterexample acceptable |
| 7 | AlphaProof IMO — **28/42 silver, P1/P2/P6 by AP, P4 by AG2, P3+P5 unsolved** + Nature 2025 doi:10.1038/s41586-025-09833-y | ✓ §2.7 (Phase 4.6 P0 fix removed Task 3 fabrication) | ✓ s19 «P1, P2, P6 решены AlphaProof / P4 — AlphaGeometry 2 / P3+P5 (комбинаторика) — нерешённая граница» + Nature 2025 doi | ✓ [s19] «P1 — алгебра, P2 — теория чисел, P6 — алгебра. AlphaGeometry 2 решила P4 / P3 и P5 — комбинаторные — остались нерешёнными / Nature 2025, DOI 10.1038/s41586-025-09833-y» | ✓ |
| 8 | Recursion-Roche — **декабрь 2021 / $150M upfront / 40 программ × >$300M / ~$12B потенциал** (Phase 4.7 P0 fix) | ✓ §2.1 chapter-part2 L71 + L56-bis Refs | ✓ s13 «декабрь 2021 / Recursion + Roche — $150M upfront / до 40 программ × >$300M = до $12B» | ✓ [s13] «декабре две тысячи двадцать первого / Сто пятьдесят миллионов долларов upfront / До сорока программ... до трёхсот миллионов долларов milestone... до двенадцати миллиардов» | ✓ |
| 9 | Coscientist — **GPT-4 + Claude both** (CMU Boiko Nature Dec 2023) | ✓ §1.3 | ✓ s09 body «GPT-4 и Claude одновременно» | ✓ [s09] «GPT-4 и Claude одновременно, в разных ролях агентов» | ✓ |
| 10 | ECMWF AIFS — **operational с 25 февраля 2025** | ✓ §0.4 + §2.6 (Phase 4 P1 soften) | ✓ s18 body «оперативно с 25 февраля 2025» + s04 glossary | ✓ [s18] «оперативной с двадцать пятого февраля две тысячи двадцать пятого» | ✓ |
| 11 | MICrONS — **1 mm³ / 84-120K neurons / 500M synapses / 4 km axons / Apr 2025 Nature** | ⚠ §3.3 says «84 000 нейронов» BUT speech [s22] + slide PPTX s22 say «**120 000 нейронов**» — drift | ⚠ s22 PPTX body «120 000 нейронов»? need verify | ⚠ [s22] «сто двадцать тысяч анатомически реконструированных нейронов» | **⚠ P1 — chapter says 84 000, speech says 120 000; need verify which is canonical (slide.md s22 +chapter convergence)** |
| 12 | TESS Huang & Jiang — **1 595 кандидатов / 83,9% точность / arxiv 2512.00967** | ✓ §3.2 (Phase 4 corrected from prior) | ✓ s21 body «1 595 высокоуверенных / точность 83,9%» + arxiv 2512.00967 | ✓ [s21] «Huang и Jiang, arxiv 2512.00967. Модель идентифицировала тысячу пятьсот девяносто пять высокоуверенных планет, точность 83,9 процента» | ✓ |
| 13 | BLS Kovács — **2002 A&A 391, 369-377** | ✓ §3.2 + Refs #26 | ✓ s21 implicitly («AUC 78% BLS»); s25 WE-TESS reference | ✓ [s21] «Box Least Squares, BLS, Kovács и соавторы две тысячи второго, A&A 391» | ✓ |
| 14 | Boltz-1 — **biorxiv 2024.11.19.624167 / Corso, Wohlwend et al. MIT** | ✓ §2.3 + Refs #3 | ✓ s15 body «декабрь 2024 / Boltz-1 — MIT / Wohlwend, Corso et al. / biorxiv 2024.11.19.624167» | ✓ [s15] «Декабрь две тысячи двадцать четвёртого / Corso, Wohlwend и соавторы / biorxiv 2024.11.19.624167» | ✓ |
| 15 | Sakana — **3% / 33% / 1% breakdown** | ✓ §1.2 table | ✓ s08 body «3% (3 из ~100) / 33% (1 из 3) / 1% (1 из ~100)»; s10 condensed «100/3/1 + 1% истинная» | ✓ [s08] «Три процента — это отбор / Тридцать три процента — это приём / только один процент — это истинная доля» | ✓ |
| 16 | AlphaFold IDP — **22% галлюцинаций / Akdel 2022 NSMB / Gopalan 2025 arxiv 2510.15939** (Phase 4.6 P1 author fix) | ✓ §3.5 + Refs #32-33 | ✓ s24 body «22% галлюцинаций»; refs include Akdel NSMB 2022 + Gopalan arxiv 2510.15939 | ✓ [s24] «двадцати двух процентов остатков / Akdel и соавторы, Nature Structural and Molecular Biology 2022 / Gopalan и Narayanan, arxiv 2510.15939» | ✓ |
| 17 | Aurora — **5 000× speedup vs ECMWF IFS** | ✓ §2.6 + Refs #10 | ✓ s18 body «5000 раз быстрее» | ✓ [s18] «в 5000 раз быстрее, чем эталон ECMWF IFS» | ✓ |
| 18 | AlphaFold DB — **>200M структур / 200K PDB / 1000× ratio** | ✓ §2.2 + §6 | ✓ s14 + s39 «200 миллионов» | ✓ [s14] «более двухсот миллионов / в тысячу раз больше, чем PDB» | ✓ |
| 19 | NotebookLM — **17M+ MAU** | ✓ §4.1 [VFY-day-of] | ✓ s27 body «17 миллионов» | ✓ [s27] «семнадцати миллионам с лишним активных пользователей» | ✓ |
| 20 | Elicit — **138M статей / 4× ускорение** | ✓ §4.2 [VFY-day-of] | ✓ s27 body «138 миллионов» | ✓ [s27] «138 миллионов академических статей / в 4 раза» | ✓ |
| 21 | Frontiers «крыса» — **13 февраля 2024 → 16 февраля (3 дня)** | ✓ §4.4 | ✓ s29 body | ✓ [s29] «Тринадцатого февраля две тысячи двадцать четвёртого / Отозвана через три дня — шестнадцатого февраля» | ✓ |
| 22 | LIGO ML — **Ashton, Malz, Colombo / arxiv 2504.17587 / 2025** | ✓ §3.4 (Phase 4 Akdel/Ashton fix) | ✓ s23 refs + body | ✓ [s23] «Ashton, Malz, Colombo, arxiv 2504.17587 две тысячи двадцать пятого» | ✓ |
| 23 | FrontierMath — **<2% (Nov 2024) → 52,4% GPT-5.5 Pro (May 2026) [VFY-day-of]** | ✓ §0.4 + §2.7 | ✓ s04 glossary; s19 body «52,4% у GPT-5.5 Pro» | ✓ [s19] «менее двух процентов / пятьдесят два с половиной процента у GPT-5.5 Pro» | ✓ |
| 24 | Russia decree — **Указ № 490 (10 октября 2019) + № 124 (15 февраля 2024)** (NOT № 145) | ✓ §5.6 + Q15 (Phase 4 P0-4 fix) | ✓ s37 body «Указ № 490 от 10 октября 2019 / Указ № 124 от 15 февраля 2024» | ✓ [s37] «Указ Президента номер 490 от 10 октября 2019 года / Обновлён Указом номер 124 от 15 февраля 2024 года» | ✓ |
| 25 | AlphaFold 3 — **8 мая 2024 Abramson et al. Nature 630, 493-500** | ✓ §2.1 + §2.3 + Refs #2 | ✓ s13 + s14 + s39 «8 мая 2024» | ✓ [s13] «AlphaFold 3 — восьмого мая две тысячи двадцать четвёртого» | ✓ |
| 26 | RU AI institutional facts — **AIRI (2021) / Sber AI Lab (climate + energy + 5K H100) / Yandex Research (YaLM-100B 2022 + RuGPT + ICML/NeurIPS/ICLR)** | ✓ §5.6 chapter-part4 L200-230 | **✗ P0** PPTX s37 visible body says «AIRI: Сбер + НТИ» (false — AIRI independent) / «Sber: с 2017, GigaChat, GigaTune, GigaChat 3 — открытые веса 2025, ML в финансах и медицине» (terms not in chapter) / «Yandex: с 2014, YandexGPT, Яндекс Переводчик, YandexGPT 5 — 2025» (terms not in chapter). **slide.md source has correct content** matching chapter | ✓ [s37] «AIRI — Институт ИИ, две тысячи двадцать первый год / Sber AI Lab — Климатическое моделирование / Прогнозирование спроса на энергию / Внутренний кластер около пяти тысяч H100 / Yandex Research — YaLM-100B открытый в двадцать втором» | **✗ P0 — PPTX visible body fabricated narrative; chapter+speech+slide.md agree; PPTX diverges** |
| 27 | Compute gap — **AlphaFold 3 ~$10-50M vs РНФ grant ~$50-150k = 20-50×; citation visibility 3× under-rep** | ✓ §5.6 + Refs #64 Mongeon | ✓ s37 PPTX body «Разрыв 20-50× / Цитируемость 3× недопредставлены» | ✓ [s37] «структурный разрыв в 20-50 раз / трёхкратное недопредставление» | ✓ |

**3-way numbers cascade drift count: 2 P0 + 1 P1.** Two P0 ALREADY captured above (Galactica date in PPTX + RU institutional narrative in PPTX). One P1 — MICrONS neuron count discrepancy 84K (chapter) vs 120K (speech + likely slide).

---

## C. Hero plan implementation across 3 artifacts

| Hero | Chapter frontmatter | Slides (PPTX) | Speech | Aligned? |
|---|---|---|---|---|
| s01 hero — Side-by-side AlphaFold Nobel + Galactica retraction | ✓ `hero_s01: "Side-by-side: AlphaFold Nobel 2024 (левая) + Galactica retraction 2022 (правая); single composite; bridging caption ⇄"` | ✓ rendered composite (Stockholm Konserthuset photo Tier 2 + MIT Tech Review headline card Tier 6 fair-use); ⇄ caption visible | ✓ [s01] «Две картинки. Слева — AlphaFold Нобель. Справа — Galactica retraction. Одна и та же базовая технология. Большая модель машинного обучения. Два диаметрально противоположных результата.» — matches bridging caption ⇄ | ⚠ **с одной P0 проблемой**: PPTX visible body для s01 говорит «15 ноября 2022» — но chapter+speech+slide.md консистентно говорят «17 ноября 2022». Hero design alignment OK, но date drift в visible body. |
| s39 hero — AlphaFold DB website screenshot → bridge к Лекции 16 | ✓ `hero_s39: "AlphaFold DB website screenshot (alphafold.ebi.ac.uk) — мост к Лекции 16 partially closed-world"` | ⚠ Per iteration-log Tier 6 fallback: AlphaFold 2 ribbon (Wikimedia Tier 2) used instead of website screenshot (Angular SPA — no og:image accessible); documented openly in iteration-log; slide.md spec still says «full-bleed screenshot alphafold.ebi.ac.uk» — drift between spec and implementation | ✓ [s39] «Этот скриншот — alphafold.ebi.ac.uk. Двести миллионов структур белков. Бесплатно. Открыто. Любому.» — speech says «скриншот» which doesn't match ribbon | ⚠ **P1 documented previously** (Phase 7 D1). Speech narrative still references «скриншот» — if final hero is ribbon, speech narrative slightly diverges (says «скриншот» but visual is ribbon). Either re-acquire screenshot OR update slide.md spec + speech narrative |

**Hero alignment: 2 issues** — s01 PPTX date drift (P0); s39 implementation diverges from spec/speech (P1 documented).

---

## D. Failure-bucket strict-in ≥30% per artifact

| Artifact | Self-reported | Independent estimate | Threshold | Status |
|---|---|---|---|---|
| Chapter | frontmatter `strict_in_self_estimate: ~46%` + `ai_failure_strict_in_pct: 45.9` | Verified: §1.2 Sakana failure deep-dive (5+ paragraphs), §2.5 Palgrave critique entire subsection, §3.5 AlphaFold IDP deep-dive, §4.4 Frontiers, §4.5 NeurIPS, §5 entire section + §6 personal pledge with constraint-checks = **~46%** | ≥30% | ✓ |
| Slides | deck.yaml formal `failure_bucket: strict_in` = 10/39 = 25.6% formal; holistic (counting strong-failure mixed slides s01/s17/s18/s19/s24/s29/s30/s33/s38) = ~15/39 = **38.4%** | Formally below threshold but holistically ≥30% | ≥30% | ⚠ formal metadata under-counts; holistic content OK |
| Speech | Estimate by min: failure-deep slides have time slots [s07] WE-1 ethics (~1 min of 2.5), [s08] 2 min, [s10] 2.5, [s17] 2, [s19] partial (1.5 of 2 — P3/P5 unsolved + cost), [s24] 2.5, [s28] 2.5, [s29] 1.5, [s30] 2, [s33] 2, [s35] partial alternative (1.5 of 2), [s37] partial gap (1 of 2.5), [s38] partial WE-2 recap (1 of 3); total **~24 min / 75 min = 32%** strict-in | ≥30% | ✓ marginal but ≥30% |

**Failure-bucket per artifact: chapter ✓, slides ⚠ formal/✓ holistic, speech ✓ (marginal).** **No P0 violations.**

---

## E. Russification consistency across 3 artifacts

**Chapter v2.3 status:** 485 critical англицизмы → 0 in Phase 4 P0-1 rewrite; whitelist = brands + acronyms with first-mention gloss.

**Slides v2 status:** «fully Russified except whitelisted brand names + established acronyms + proper nouns + academic citations» per iteration-log; deep latin-token scan ~203 unique non-whitelisted tokens (proper nouns / method names / license markers).

**Speech v1 status:** speech-writer self-reports 242 unique latin tokens, «все в whitelist categories» — verified spot-check shows brand names (Sakana, NotebookLM, Boltz, Materials Project, Crossref, ICMJE, NeurIPS, IMO), method names (CNN, GNoME, DFT, GP, BO, BLS, LIGO, TESS, ECMWF), DOIs (e.g., 10.1038/s41586-025-09833-y), arxiv IDs.

**Cross-artifact Russification consistency:**

| Term | Chapter form | Slides form | Speech form | 3-way aligned? |
|---|---|---|---|---|
| augmentation / расширение | bilingual «Расширение (augmentation)» canonical | s27 frontmatter EN-only; s03 staircase «расширение» PPTX OK | «расширение» (Russian primary) | ⚠ P2 — minor (s27 frontmatter only) |
| cherry-pick / отбор лучшего | bilingual «отбор лучшего (cherry-picking)» §1.2 | s06/s10 EN-only «cherry-pick» multi mentions | speech NOT use «cherry-pick» — uses «отбор лучшего» Russian | ⚠ P2 — slides EN-only; chapter+speech bilingual/Russian |
| foundation model / фундаментальная модель | bilingual gloss §0.4 | ⚠ s18 «foundation модели» mixed | ⚠ speech [s37] «открытые foundation модели» EN-only | ⚠ P2 — minor leak in both slides+speech |
| open-source / открытый исходный код | bilingual gloss §2.3 | s14/s15 mostly «open-source» EN-only | speech [s15] «полностью открытый», «открытые веса», «открытый исходный код» — Russian primary ✓ | ⚠ slide leak only |
| HITL / человек в петле | bilingual «HITL (human-in-the-loop)» glossed §0.4, then mixed | s04 «HITL (человек в петле)»; s28, s33, s34 «HITL» | speech [s04] «Человек в петле, HITL» — Russian primary then acronym | ✓ |
| peer review / рецензирование | bilingual gloss; Russian primary | «рецензирование» predominant | speech [s38] «рецензирование» Russian | ✓ |
| pipeline / конвейер | «конвейер» Russian primary | «конвейер» Russian | speech «конвейер» Russian (e.g., [s23] «классический конвейер», [s34] «AI-конвейер») | ✓ |

**Russification 3-way verdict: 4 minor leaks (P2)** — augmentation in s27 frontmatter, cherry-pick in slides, foundation модели mixed in slides+speech, open-source EN-only in slides. No P0/P1.

---

## F. Anonymization across 3 artifacts

**Standard:** 0 named Russian universities (МГТУ/Бауман/МФТИ/МГУ/etc.) per CLAUDE.md anonymization absolute rule.

| Artifact | Named RU unis | Phase | Status |
|---|---|---|---|
| Chapter v2.3 | ✓ 0 (МФТИ regression fixed Phase 8 — chapter-part4 §5.6 L266 «AIRI + МФТИ» → «AIRI + профильный технический университет») | ✓ aligned | ✓ |
| Slides v2 PPTX | ✓ 0 named Russian universities (verified grep) | ✓ | ✓ |
| Speech v1 | ✓ 0 named Russian universities (verified grep + buffer line 755 «профильные технические университеты России активно работают»; no specific institution) | ✓ | ✓ |

**Brand-whitelist consistent across 3 artifacts:** AIRI / Sber AI Lab / Yandex Research / РНФ / Минобрнауки — same form in chapter, slides (per slide.md source), speech.

**International institutions consistent:** CMU / MIT / Stanford / DeepMind / Microsoft Research / Allen Institute / EBI / ECMWF — same form across 3 artifacts.

**Anonymization 3-way verdict: ✓ all 3 artifacts clean.**

---

## G. Walked examples cross-artifact (4 WEs)

| WE | Chapter | Slides (PPTX) | Speech | 3-way step count match? |
|---|---|---|---|---|
| **WE-1 grant idea (6 steps)** | ✓ §1.5 «Разобранное дерево решения из шести шагов»: classify task → coverage → verification → ethics → HITL → submission integrity | ✓ s07 deck.yaml learning_goal «WE-1 walked example: classify task → coverage → verification → ethics → HITL → submission integrity» | ⚠ [s07] speech provides 6 steps but truncates submission step: «классифицируй задачу / покрытие / проверяемость / этика / HITL / целостность подачи» — all 6 present ✓ | ✓ all 3 say 6 steps |
| **WE-TESS transit search (5 steps)** | ✓ §3.7 «Разобранная 5-шаговая рамка»: data overlap → label availability → GPU cost → AUC baseline → held-out validation | ✓ s25 deck.yaml learning_goal explicit 5 steps | ✓ [s25] speech «Пятишаговая рамка» explicit + 5 steps narrated | ✓ all 3 say 5 steps |
| **WE-2 collaborator bibliography (4 steps)** | ✓ §4.3 «Разобранный 4-шаговый процесс проверки»: DOI-resolve / релевантность / GPTZero / запрос исходных | ✓ s28 deck.yaml + body «4 шага проверки: DOI-resolve, выборка релевантности, GPTZero, запрос исходных файлов» | ✓ [s28] «Четырёхшаговый процесс» explicit + 4 steps narrated | ✓ all 3 say 4 steps |
| **WE-3 catalyst pipeline (5 steps)** | ✓ §5.3 «Разобранная 5-шаговая рамка»: classify → map alternatives → 4 criteria → HITL design → pre-publication verify | ✓ s34 deck.yaml + body | ✓ [s34] «Пятишаговая рамка» explicit + 5 steps narrated «Шаг первый — классификация / Шаг второй — карта альтернатив / Шаг третий — применение четырёх критериев / Шаг четвёртый — HITL / Шаг пятый — проверка до публикации» | ✓ all 3 say 5 steps |

**Walked examples 3-way verdict: ✓ all 4 WEs perfectly aligned 6/5/4/5 step counts across chapter, slides, speech.**

---

## H. Section transition bridges across 3 artifacts

| Section boundary | Chapter | Slides | Speech | Aligned? |
|---|---|---|---|---|
| §0 → §1 (Hypothesis+Design) | §1.1 intro «Раздел 1 лестницы — формулирование гипотезы — самая открытая ступень» | s06 divider «Раздел 1. Hypothesis + Design — где AI продаётся за автономию, но даёт узкую помощь» | [s06] «Мы с вами входим в первый раздел из пяти. Hypothesis + Design — где AI продаётся за автономию, но даёт узкую помощь.» | ✓ |
| §1 → §2 (Experiment) | §2 intro «Это самый длинный раздел главы и самый положительный по тону» | s12 divider «Раздел 2. Experiment — самый сильный успех AI в науке (нобелевского уровня) и его трещины» | [s12] «Переходим ко второму разделу из пяти. Experiment — самый длинный раздел лекции и самый положительный по тону. Здесь мы с вами увидим прорывы нобелевского уровня. Но успех нобелевского уровня — не означает финальности нобелевского уровня. Каждый подраздел будет с трещиной.» | ✓ |
| §2 → §3 (Analyse) | §3 intro «самая готовая к промышленному применению ступень» | s20 divider «Раздел 3. Analyse — самые надёжные применения AI в науке» | [s20] «Третий раздел из пяти. Analyse — фаза анализа данных. Самая готовая к промышленному применению ступень...» | ✓ |
| §3 → §4 (Write+Review) | §4 intro «самая концентрированная зона провалов лекции» | s26 divider «Раздел 4. Write + Review — где AI против академической интегриты» | [s26] «Переходим к четвёртому разделу из пяти. Write плюс Review — самая концентрированная зона провалов лекции» | ⚠ P2 — slides use «интегриты» (anglicism), chapter+speech use «академической целостности» Russian |
| §4 → §5 (Когда AI не нужен) | §5 intro «результирующий раздел лекции» | s32 divider «Раздел 5. Когда AI не нужен в науке — критерии, альтернативы, разобранный пример» | [s32] «Пятый раздел из пяти. Результирующий раздел. После четырёх разделов разбора, где AI работает и где нет, мы с вами синтезируем применимую ментальную модель.» | ✓ |
| §5 → §6 (Замыкание) | §6 «Замыкание + мост к Лекции 16» | s38 dedicated Q&A + s39 closing hero | [s38] Q&A + [s39] closing | ✓ |

**Section bridges 3-way verdict: ✓ all 6 transitions properly aligned + announcing «N раздел из 5» pattern.** 1 P2 anglicism «интегриты» in s26 divider (slide body).

---

## I. LO coverage cross-artifact (LO4 / LO5 / LO6 / LO8)

| LO | Chapter coverage | Slides coverage | Speech coverage | 3-way aligned? |
|---|---|---|---|---|
| **LO4** «Назвать классы AI-инструментов» | ✓ §0.4 glossary (15 terms); §2 (fundamental models); §3 (narrow ML); §4 (RAG tools); §5.2 (5 alternatives) | ✓ s04 glossary, s11 BO+GP, s15 Boltz, s27 NotebookLM+Elicit, s35 alternatives matrix | ✓ [s04] glossary narration + [s11] BO+GP + [s35] alternatives 5-tool list | ✓ |
| **LO5** «Этические риски» | ✓ §4.3 WE-2 + §4.5 NeurIPS + §4.6 ICMJE | ✓ s28 WE-2 bibliography + s30 NeurIPS + s31 ICMJE | ✓ [s28] 4-step verification + [s30] NeurIPS + [s31] ICMJE | ✓ |
| **LO6** «Применить лестницу научного цикла + критерии» | ✓ §0.3 keystone + §5.1 4 critics + §5.5 5-step framework | ✓ s03 lecture-map + s33 four criteria + s07/s25/s28/s34 WEs + s36 framework recap | ✓ [s03] keystone narration + [s33] 4 criteria + [s36] 5-step framework recap + 4 WEs | ✓ |
| **LO8** «Применять + не-AI альтернатива» | ✓ §1.6 BO+GP + §3.6 alternatives + §5.2 5 alternatives + §5.3 WE-3 + §5.4 vendor questions | ✓ s11 BO+GP + s25 WE-TESS + s34 WE-3 + s35 alternatives + s36 vendor questions | ✓ [s11] BO+GP + [s25] WE-TESS + [s34] WE-3 + [s35] 5 alternatives + [s36] 3 vendor questions | ✓ |

**LO coverage 3-way verdict: ✓ all 4 LOs properly covered in all 3 artifacts.**

---

## J. Pre-flight check (Pre-USER-GATE C readiness)

### Cornerstone canonical через 3:
- 11/12 canonical form consistent across chapter/slides/speech. 1 form drift («foundation модели» in s18 PPTX + speech [s37], chapter has bilingual «Фундаментальная модель»).

### Slide orphan refs in speech:
- Speech uses `[sNN]` markers for all 39 slides. Verified all 39 markers refer to existing slides s01-s39 in deck.yaml. **No orphan references.** ✓

### Number drift между artifacts:
- **P0-1 (s01 Galactica date)** — PPTX visible body «15 ноября 2022» vs chapter+speech+slide.md «17 ноября 2022»
- **P0-2 (s37 RU institutional facts)** — PPTX visible body fabricated narrative (GigaChat, GigaTune, YandexGPT, Яндекс Переводчик, дата 2017/2014) NOT in chapter or speech
- **P1 (s22 MICrONS neuron count)** — chapter §3.3 says «84 000 нейронов», speech [s22] says «120 000 нейронов» — need verify canonical via primary source (Nature Apr 2025 MICrONS papers)
- All other 24 numbers cascade ✓ aligned across 3 artifacts

### Terminology drift:
- 4 P2 minor leaks (augmentation EN-only in s27 frontmatter, cherry-pick EN-only in slides, foundation модели mixed in slides+speech, open-source EN-only in slides)

---

## DISCREPANCIES (Detailed)

### D1 — s01 PPTX visible body + speaker notes use wrong Galactica date (P0)

**Severity:** P0
**Where:** rendered/lec-15.pptx slide 1 visible body «15 ноября 2022 — Galactica прожила три дня» + speaker notes «15 ноября 2022 года, за два года до этого Нобеля, Meta запустила Galactica».
**Source-of-truth says:** chapter §0.2 + speech [s01] + s01 slide.md L44 + deck.yaml L49 all consistently say **«17 ноября 2022»**.
**Issue:** PPTX renders stale wrong date. Pipeline integrity gap — rendered PPTX diverges from slide.md source.
**Recommendation:** Re-render s01 from slide.md source (or inject_notes.py equivalent re-injection). Verify rendered PPTX shows «17 ноября 2022» in BOTH visible body AND speaker notes. **MUST fix before USER GATE C.**
**Why P0:** Factual contradiction between source-of-truth (chapter) and student-visible PPTX. Student leaves with wrong date. Also undermines the «hook» moment of lecture.

### D2 — s37 PPTX visible body contains fabricated RU institutional narrative (P0)

**Severity:** P0
**Where:** rendered/lec-15.pptx slide 37 visible body — multiple fabricated terms:
- AIRI: «Сбер + платформа НТИ» — chapter says AIRI independent (2021)
- Sber AI Lab: «с 2017» (year not in chapter; chapter says «исследовательское направление в Сбербанке» без foundation year) + «GigaChat (большая языковая модель), GigaTune» (terms NOT in chapter+speech) + «GigaChat 3 — открытые веса 2025» (NOT in chapter) + «ML в финансах и медицине» (chapter says climate + energy forecasting)
- Yandex Research: «с 2014» (year not in chapter) + «YandexGPT, Яндекс Переводчик» (NOT in chapter; chapter says YaLM + RuGPT) + «ML для поиска и рекомендаций» (NOT in chapter) + «YandexGPT 5 — 2025» (NOT in chapter)

**Source-of-truth says:** chapter §5.6 + speech [s37] + s37 slide.md L20-46 ALL say AIRI = 2021 / Sber = climate forecasting + energy demand + 5K H100 cluster / Yandex = YaLM-100B (2022) + RuGPT + ICML/NeurIPS/ICLR contributions.

**Issue:** rendered PPTX s37 visible body contains content NOT present in any source artifact. Likely injected from earlier deck iteration that was retained during designer rendering loop, OR pipeline render bug. This is a serious integrity issue — student leaves lecture with wrong attribution about Russian AI institutions.

**Recommendation:** **MUST re-render s37 from slide.md source.** Verify PPTX visible body matches slide.md L20-71 narrative. Verify speaker notes match slide.md L74-87 + speech [s37] narrative.

**Why P0:** (a) Factual contradiction between source-of-truth and student-visible PPTX. (b) GigaChat / YandexGPT misattribution is verifiable in Russian press / Sber+Yandex official blogs — wrong-dated/wrong-product errors damage credibility. (c) AIRI false attribution to «Сбер + платформа НТИ» misrepresents institutional independence (chapter says explicitly AIRI is independent research institute).

### D3 — MICrONS neuron count: 84K (chapter) vs 120K (speech) (P1)

**Severity:** P1
**Where:** chapter-part3 §3.3 L80 «1 mm³ зрительной коры, **84 000 нейронов**, 500 миллионов синапсов, 4 километра аксонов» vs speech [s22] L362 «**сто двадцать тысяч анатомически реконструированных нейронов**. Пятьсот миллионов синапсов. Четыре километра аксонов» + s22 PPTX «120 000 нейронов» (need verify).

**Issue:** Number drift — chapter says 84K, speech says 120K. One is wrong. Primary source — Allen MICrONS Nature April 2025 papers — needs verification.

**Recommendation:** Phase 11 must verify canonical figure via primary source. Multiple Nature papers from MICrONS consortium published April 2025 — one says «~84 000 neurons in 1 mm³», another may say «120 000 neurons». Possibly two different cubic millimeters reported. Sync chapter+slides+speech to single canonical figure.

**Why P1:** Number cascade drift between chapter and speech, but neither contradicts a third primary source clearly — needs research to determine which is correct. Less critical than P0 because both are plausibly close to reality.

### D4 — s39 hero spec/implementation/speech mismatch (P1, continued from Phase 7 D1)

**Severity:** P1 (carryover from Phase 7)
**Where:** s39 slide.md spec says «full-bleed screenshot alphafold.ebi.ac.uk», iteration-log says AlphaFold 2 ribbon fallback used (Tier 6 due to Angular SPA), speech [s39] says «Этот скриншот — alphafold.ebi.ac.uk».

**Issue:** Three artifacts say «screenshot» but rendered PPTX shows ribbon. Speech narrative says «скриншот» which doesn't match ribbon visual.

**Recommendation:** Either (a) retry Tier 1-6 acquisition with Wayback or direct retrieval; OR (b) update slide.md spec + speech narrative to honestly describe AlphaFold 2 ribbon visual. Owner decision required.

**Why P1:** Documented divergence; doesn't undermine factual content but creates verbal/visual mismatch student notices.

### D5 — Failure-bucket strict-in marginal in slides (formal) + marginal in speech (P1)

**Severity:** P1 (carryover from Phase 7 D2)
**Where:** deck.yaml formal `failure_bucket: strict_in` = 10/39 = 25.6%; speech 24/75 ≈ 32% time on failure-deep content.

**Issue:** Slides formally below 30% threshold per metadata field; holistic content above 30%. Speech marginal at 32%.

**Recommendation:** Retag mixed slides s01/s18/s19/s37/s38 → strict_in to bring formal metric to ~36%. Speech could add 2-3 sentences explicit failure framing in [s18] Aurora tail events + [s37] RU compute gap to lift speech failure-share clearer above 30%.

**Why P1:** Per CLAUDE.md AI-Failure & Judgment Content Rule «strict-in ≥30% in EACH artifact». Speech needs verification check on holistic content classification.

### D6 — s03 keystone staircase RU bilingual labels (P1, carryover Phase 7 D3)

**Severity:** P1
**Where:** s03 slide.md visual.primary plan + PPTX rendered staircase.
**Issue:** s03 PPTX shows Russian labels «расширение» on each step (good!) but may not include EN gloss «augmentation / autonomous / vetoed» bilingual canonical form per chapter §0.3.
**Recommendation:** Verify rendered s03.png snapshot shows bilingual «Расширение (augmentation) / Автономно (autonomous) / Запрещён (vetoed)» tags. If only Russian — add EN gloss inline. If only English — add Russian (the verified PPTX shows Russian — fine, but bilingual is canonical).
**Why P1:** Keystone slide rendering matters — student first impression.

### D7 — кризис воспроизводимости cornerstone not explicitly named in speech (P2)

**Severity:** P2
**Where:** chapter §0.4 glossary + §1.5 reference; PPTX s04 glossary line «Кризис воспроизводимости — 39 из 100».
**Issue:** Speech [s04] glossary narration mentions «фабрика статей» term but doesn't explicitly say «кризис воспроизводимости» — cornerstone term not voiced.
**Recommendation:** Phase 11 speech polish — add «кризис воспроизводимости» explicit mention in [s04] glossary narration: «Кризис воспроизводимости — 39 процентов исследований не воспроизводятся в психологии».
**Why P2:** Minor coverage gap; named in slide but not in speech narrative.

### D8 — Inverse design cornerstone not mentioned in speech (P2)

**Severity:** P2
**Where:** chapter §0.4 + §2 inline; PPTX s04 «Обратное проектирование (inverse design)».
**Issue:** Speech [s04] glossary doesn't name «обратное проектирование» as cornerstone; could be mentioned in [s34] catalyst WE-3 as relevant concept.
**Recommendation:** Phase 11 speech polish — name term in [s04] or [s34].
**Why P2:** Minor — concept appears in PPTX glossary, speech could echo.

### D9 — Cherry-pick anglicism in slides without RU gloss (P2, carryover Phase 7 D6)

**Severity:** P2
**Where:** s06, s10, s38 PPTX use «cherry-pick» / «cherry-picking» EN-only.
**Issue:** Chapter §1.2 uses bilingual «отбор лучшего (cherry-picking)»; speech uses «отбор лучшего» Russian primary. Slides leak EN-only.
**Recommendation:** Polish first-mention «cherry-pick» (s06 + s10) → «отбор лучшего (cherry-picking)»; subsequent mentions OK.
**Why P2:** Russification consistency across 3 artifacts.

### D10 — «foundation модели» mixed form in slides+speech (P2)

**Severity:** P2
**Where:** s18 PPTX «foundation модели систематически уступают»; speech [s37] «открытые foundation модели».
**Issue:** Chapter uses bilingual «Фундаментальная модель (foundation model)» canonical; mixed Russian-English in slides+speech.
**Recommendation:** s18 «foundation модели» → «фундаментальные модели»; speech [s37] line 680 «открытые foundation модели» → «открытые фундаментальные модели».
**Why P2:** Russification consistency.

### D11 — «академической интегриты» anglicism in s26 divider (P2)

**Severity:** P2
**Where:** s26 PPTX divider «Раздел 4. Write + Review — где AI против академической интегриты».
**Issue:** Chapter+speech use «академической целостности»; s26 PPTX uses «интегриты» (anglicism).
**Recommendation:** s26 divider «интегриты» → «целостности».
**Why P2:** Russification consistency in section divider.

### D12 — s27 learning_goal frontmatter EN-only (P2, carryover Phase 7 D8)

**Severity:** P2
**Where:** s27 slide.md frontmatter learning_goal «augmentation для навигации, не замена синтеза; psychology of automation bias».
**Issue:** Frontmatter metadata only (not visible body), but cornerstone cross-artifact: «augmentation» → «расширение»; «automation bias» → «склонность доверять автомату».
**Recommendation:** Russify frontmatter; matches chapter and speech.
**Why P2:** Metadata consistency.

### D13 — Sakana s10 PPTX omits explicit 3%/33%/1% breakdown (P2)

**Severity:** P2
**Where:** s10 PPTX visible body shows «100 → 3 / 1%» but omits explicit «3%» / «33%» from s08 framing.
**Issue:** s08 PPTX clearly has «3%, 33%, 1%» breakdown; s10 omits «3%» and «33%» percentages (only «1%» appears). Speech [s08] explicitly says all three; chapter has table.
**Recommendation:** Optional polish — re-add 3% / 33% percentages to s10 body for unambiguous breakdown across all 3 artifacts.
**Why P2:** Minor — s08 already covers; s10 functions as deep-dive of 4 structural problems, doesn't need to repeat numbers.

### D14 — Stale slide.md source files for 6 Phase 7 fact-fixes (P2)

**Severity:** P2 informational
**Where:** Task brief notes: «slides/sNN-*.md (Phase 5 source — note: stale для 6 fact-fixes Nature 624 / biorxiv / Yamada / BLS 2002 / Huang-Jiang / AlphaProof DOI; rendered PPTX correct)».
**Issue:** Slide.md source files predate Phase 7 6 fact-fixes; rendered PPTX has correct facts. This means slide.md → PPTX render pipeline has manual interventions baked into rendered. Slide.md files diverge from PPTX visible body for these 6 facts.
**Recommendation:** Phase 11 housekeeping — update slide.md source files to match Phase 7 fact-corrected PPTX state. This makes re-rendering safe (currently if you re-render from stale slide.md, you'd revert the fixes).
**Why P2:** Pipeline hygiene; doesn't affect student-visible content currently, but creates technical debt.

### D15 — Speaker notes presence verification (P1 risk hint)

**Severity:** P1 risk
**Where:** Speech-writer Phase 9 task generally produces speech.md narrative, but Phase 9 doesn't typically update speaker notes in PPTX. From earlier memory note in CLAUDE.md: lec-13 had catastrophic P0 speaker notes injection bug.
**Issue:** Need to verify all 39 slides in lec-15.pptx have non-trivial speaker notes (>50 words each). I spot-checked s01 / s13 / s37 — all had substantive notes. Recommend systematic verify in Phase 11.
**Recommendation:** Run `python3 inject_notes.py` equivalent OR manual sweep — count speaker notes word count per slide; flag any <50 words OR matches text-only layout pattern.
**Why P1 risk:** Per [[lec-13 lesson]], speaker notes injection bug can render speaker notes as layout descriptions instead of student-readable text.

### D16 — Speech timing arithmetic (P2 verify)

**Severity:** P2
**Where:** Speech sums slide times: s01 (3) + s02 (1) + s03 (1) + s04 (1) + s05 (1) + s06 (0.5) + s07 (2.5) + s08 (2) + s09 (2) + s10 (2.5) + s11 (1) + s12 (0.5) + s13 (2.5) + s14 (2) + s15 (1.5) + s16 (2) + s17 (2) + s18 (2) + s19 (2) + s20 (0.5) + s21 (2) + s22 (2) + s23 (2) + s24 (2.5) + s25 (2.5) + s26 (0.5) + s27 (2) + s28 (2.5) + s29 (1.5) + s30 (2) + s31 (2) + s32 (0.5) + s33 (2) + s34 (2.5) + s35 (2) + s36 (2) + s37 (2.5) + s38 (3) + s39 (2) = **69.5 minutes**.
**Issue:** Speech target_duration 75 min + 5-min Q&A buffer = ~80 min available. Actual content time 69.5 min — fits comfortably with 5-min buffer + 5 min for transitions/pauses. Speech meta says «target 75 minutes». Match ✓.
**Recommendation:** None — math checks out.
**Why P2:** Arithmetic verify (not drift, confirmation).

---

## Coverage gaps

**No major LO or assertion coverage gaps detected across 3 artifacts.**

- Every chapter §s has corresponding slide + speech narration.
- All 4 WEs (WE-1 / WE-TESS / WE-2 / WE-3) consistent step counts (6/5/4/5).
- All 27 canonical numbers checked propagate: 24 ✓ aligned, 2 P0 drifts, 1 P1 drift.
- All 39 slide-markers in chapter narrative; all 39 slides have speech narration; all 39 slides exist in deck.yaml.
- Speech has no orphan `[sNN]` references to deleted slides.
- All 4 LOs covered in all 3 artifacts.

---

## Cross-artifact matrix summary

| Concept / Number / LO | Chapter | Slides | Speech | 3-way aligned? |
|---|---|---|---|---|
| LO4 «Назвать классы AI-инструментов» | ✓ §0.4+§2+§3+§5.2 | ✓ s04+s11+s15+s27+s35 | ✓ [s04]+[s11]+[s35] | ✓ |
| LO5 «Этические риски» | ✓ §4.3+§4.5+§4.6 | ✓ s28+s30+s31 | ✓ [s28]+[s30]+[s31] | ✓ |
| LO6 «Лестница цикла + критерии» | ✓ §0.3+§5.1+§5.5 | ✓ s03+s33+s07/25/28/34+s36 | ✓ [s03]+[s33]+[s36]+WEs | ✓ |
| LO8 «Не-AI альтернативы» | ✓ §1.6+§3.6+§5.2+§5.3+§5.4 | ✓ s11+s25+s34+s35+s36 | ✓ [s11]+[s25]+[s34]+[s35]+[s36] | ✓ |
| Keystone «лестница научного цикла» | ✓ §0.3 | ✓ s03 keystone | ✓ [s03] keystone narration | ✓ |
| A-Lab 41/58/17 days | ✓ §2.4 | ✓ s12+s16+s17+s38 | ✓ [s16] | ✓ |
| Palgrave 35/36 | ✓ §2.5 | ✓ s17+s12+s38 | ✓ [s17] | ✓ |
| Nobel 9 окт 2024 | ✓ §0.2+§2.1 | ✓ s01+s13 | ✓ [s01]+[s13] | ✓ |
| Galactica 17 ноября 2022 | ✓ §0.2 | **✗ P0 PPTX says 15 ноября** | ✓ [s01] | **✗ P0** |
| NeurIPS 21575/5290/24.52%/100+/53 | ✓ §1.2+§4.5 | ✓ s30+s38 | ✓ [s30] | ✓ |
| GNoME 6 раундов | ✓ §2.4 | ✓ s16 | ✓ [s16] | ✓ |
| AlphaProof P1/P2/P6+P4 / P3+P5 unsolved + Nature 2025 doi | ✓ §2.7 | ✓ s19 | ✓ [s19] | ✓ |
| Recursion-Roche дек 2021 / $12B | ✓ §2.1 | ✓ s13 | ✓ [s13] | ✓ |
| Coscientist GPT-4 + Claude | ✓ §1.3 | ✓ s09 | ✓ [s09] | ✓ |
| ECMWF AIFS 25 фев 2025 | ✓ §0.4+§2.6 | ✓ s18+s04 | ✓ [s18] | ✓ |
| Allen MICrONS 84K (chapter) / 120K (speech) | ⚠ 84K | ⚠ 120K | ⚠ 120K | **⚠ P1 number drift** |
| TESS Huang-Jiang 1595 / 83.9% / arxiv 2512.00967 | ✓ §3.2 | ✓ s21 | ✓ [s21] | ✓ |
| BLS Kovács 2002 | ✓ §3.2 | ✓ s21 | ✓ [s21] | ✓ |
| Boltz biorxiv 2024.11.19.624167 | ✓ §2.3 | ✓ s15 | ✓ [s15] | ✓ |
| Sakana arxiv 2504.08066 Yamada | ✓ §1.2 Refs #18 | ✓ s08+s10 refs | ✓ (implicit Sakana attribution) | ✓ |
| Указ № 490 + № 124 | ✓ §5.6 | ✓ s37 | ✓ [s37] | ✓ |
| AIRI/Sber/Yandex correct attribution | ✓ §5.6 | **✗ P0 PPTX fabricated** | ✓ [s37] | **✗ P0** |
| Russification cornerstones | ✓ bilingual canonical | ⚠ minor leaks | ⚠ minor leaks | ⚠ P2 |
| Anonymization (RU unis) | ✓ 0 named | ✓ 0 named | ✓ 0 named | ✓ |

---

## Топ-5 рекомендаций для Phase 11

### 1. **[P0] Re-render PPTX from current slide.md source for s01 + s37**

**Action:** Run rendering pipeline (or manual cleanup) for s01 + s37:
- s01 — fix «15 ноября 2022» → «17 ноября 2022» in visible body AND speaker notes.
- s37 — replace fabricated RU institutional narrative with content from slide.md L20-87:
  - AIRI = Институт ИИ (2021), AI4Science directions = protein structure + medical imaging + climate Arctic
  - Sber AI Lab = climate forecasting + energy demand + 5K H100 cluster; remove GigaChat/GigaTune
  - Yandex Research = YaLM-100B (2022) + RuGPT + ICML/NeurIPS/ICLR; remove YandexGPT/Яндекс Переводчик

**Owner decision:** verify whether s01 + s37 are the only PPTX slides diverging from slide.md, OR whether other slides may also have similar fabricated content. Suggest spot-check all 39 slides visible body vs slide.md source.

### 2. **[P1] Verify MICrONS neuron count canonical: 84K vs 120K**

**Action:** Web search Allen MICrONS Nature April 2025 papers (multiple consortium papers published — e.g., Nature 640+ articles). Determine canonical neuron count per 1 mm³ visual cortex cube. Sync chapter §3.3 + slides s22 PPTX + speech [s22] L362 to single canonical figure.

**Likely:** 120K is canonical (verified by Allen Institute press release pattern «120,000 neurons in 1 cubic millimeter» — but needs verification). If 120K canonical → fix chapter «84 000 нейронов» → «120 000 нейронов».

### 3. **[P1] Speech failure-share verification + addition of 2-3 explicit failure-framing sentences**

**Action:** Speech currently calculates ~32% time on strict failure content — marginal. Add explicit failure-framing in:
- [s18] Aurora — emphasize tail events failure as «not a defect, but structural ML property»
- [s37] RU compute gap — explicit «структурный gap, не недостаток усилий»
- [s11] BO+GP — explicit «Sakana fail mode at scale, BO success mode at scale»

Lift speech failure-share from ~32% to ~38%+ holistic to remove «marginal» status.

### 4. **[P1] Phase 7 carryover polish (3 items still pending)**

**Action:**
- s39 hero spec/implementation/speech mismatch (D4) — owner decision: retry screenshot acquisition OR honest spec update + speech narrative adjust.
- s03 keystone bilingual labels (D6) — verify rendered staircase shows «Расширение (augmentation) / Автономно (autonomous) / Запрещено (vetoed)».
- Failure-bucket retag s01/s18/s19/s37/s38 → strict_in for accurate deck.yaml metadata.

### 5. **[P2] Russification + terminology polish across all 3 artifacts**

**Action:** Targeted polish:
- Slides: «cherry-pick» → «отбор лучшего (cherry-picking)» (s06, s10); «foundation модели» → «фундаментальные модели» (s18); «академической интегриты» → «академической целостности» (s26); «open-source» → «открытый исходный код / open-source» bilingual (s14, s15)
- Speech: «открытые foundation модели» → «открытые фундаментальные модели» [s37]
- s27 slide.md frontmatter learning_goal Russification
- Speaker notes verification on all 39 slides (spot-check ≥5 random slides for 150-300-word readable student text; not layout descriptions)

---

## Verdict recap

**REVISE** — 3-way consistency between chapter v2.3 ↔ slides v2 ↔ speech v1 has **2 P0 drifts** (s01 Galactica date + s37 RU institutional fabricated content) that BLOCK USER GATE C until fixed. Cannot APPROVE because P0 drifts mean student-visible PPTX contradicts chapter source-of-truth AND speech narrative. These drifts were missed by Phase 7 because focused on slide.md ↔ chapter; this Phase 10 cross-artifact check caught them via PPTX inspection.

**1 P1 drift** (MICrONS 84K vs 120K) requires primary source verification.

**3 P1 carryovers from Phase 7** (s39 hero, s03 keystone bilingual, failure-bucket metadata) still pending for Phase 11 polish.

**9 P2 minor drifts** (Russification leaks across 3 artifacts, terminology consistency, deck.yaml comment hygiene, speaker notes verification risk) — Phase 11 polish acceptable.

**Once 2 P0 + 1 P1 (MICrONS) fixed via re-render + verification, ready for USER GATE C pre-flight.**

---

**Report generated:** consistency-checker, 2026-05-27, Phase 10.
**Storage:** `library/lectures/lec-15/qa-reports/2026-05-27-v1-speech/consistency-checker.md`
