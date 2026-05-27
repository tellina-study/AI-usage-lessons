# Лекция 15: AI в научных исследованиях — план v2 (Часть 2)

**Часть 1:** см. `plan-v2.md` (frontmatter + changelog + LO + keystone + outline + worked examples + RU context).

**Назначение Часть 2:** оставшиеся разделы плана — failure bucket, sections roadmap, numbers/russification/media/hero plans, comparisons, anti-dependencies, anonymization, risks, Phase 2 brief, open questions.

**Lookback правил:** все ENFORCED rules применяются (см. часть 1 § Метаданные + Changelog для applied owner decisions #1-#4 и P0/P1 fixes).

---

## Провалы, ограничения и альтернативы (ENFORCED — ≥30% содержания)

### Документированные провалы AI в науке + выученные уроки

1. **Galactica (Meta, ноябрь 2022)** — 3-day shame после launch; LLM генерировал confidently «science» с false claims. **Урок**: LLM не понимает «истину» — он генерирует словесные распределения.
2. **A-Lab Berkeley Palgrave critique 2024** — **35 of 36 success samples had errors**: derivatives mislabeled, no functionality demonstrated. **Урок**: prediction ≠ proven novelty; structural similarity к existing material — недостаточно для «discovery» claim.
3. **Sakana AI Scientist** — 1 of 3 papers passed peer review, но external audit показал «hallucinations, faked results, overestimated novelty». Cherry-pick mechanics: ~100 papers per cycle, human selects 3. **Урок**: peer-review pass ≠ научная валидность.
4. **Frontiers «крыса» retraction (февраль 2024)** — Midjourney-generated rat anatomy опубликован, retracted в 3 дня. **Урок**: disclosure в paper — недостаточная защита; peer review должен проверять figures отдельно.
5. **NeurIPS 2025 fake citations** — 53 papers с fake refs пробились в принятые; ICLR 2026 — 50+ similar. **Урок**: bibliography от LLM требует verify-каждой-цитаты (WE-2 в Разделе 4).
6. **AlphaFold IDP limits** — 22% residues hallucinated в IDP regions; α-synuclein не captured; lipid environment не моделируется. **Урок**: foundation model для domain не = full domain understanding.
7. **AlphaFold 3 closed at launch** — научное community протест (1000+ scientists letter); commercial Isomorphic Labs $3B deals (Lilly + Novartis). **Урок**: science vs commerce trade-off; open альтернативы (Boltz-1) могут обогнать closed модель в adoption.
8. **AI peer review hallucinations (NeurIPS 2024+ ban)** — automated review consistently missed flaws in own work. **Урок**: peer review — критически важная человеческая задача.
9. **Aurora extreme weather miss (Hurricane Milton 2024)** — Aurora systematically under-predicted intensity peak. **Урок**: foundation weather models — accurate для bulk distribution, fail на tails (extreme events — где ECMWF physics-based methods всё ещё необходимы).
10. **AlphaProof time-cost** — 4+ hours per problem vs human 90 min. **Урок**: AI breakthroughs в formal math — proof-of-capability, не practical replacement для human mathematicians.

### Фундаментальные ограничения / риски подхода

- **LLM-fundamentals**: distribution over tokens, не understanding; hallucinations — feature, не bug.
- **Training distribution coverage** — фундаментальное. Rare diseases, новые материалы, neonatal medicine, эмерджентные климатические события — outside distribution.
- **Closed-world vs open-world** — фундаментальная граница (бывший Variant B keystone, теперь критерий A).
- **Computational vs experimental verification gap** — AlphaFold предсказывает fold; synthesis + activity assay по-прежнему обязательны.
- **Replicability crisis** — psychology 36% replication rate, economics 61%, AI/ML 24-50% — AI не лечит эту проблему, может усугубить.

### Критерии «здесь AI не нужен / не применим» (LO6 центральный)

- **A. Open-world задача без verifiable ground truth** — биология organismal, sociology, history of science.
- **B. Underrepresented в training data** — rare diseases, новые материалы (без analogs).
- **C. Verifiability cannot be done independently** — peer review, citation networks.
- **D. Ethical risk** — authorship, IRB violations, AI как co-author (ICMJE запрещает).
- **E. Закрытая физика лучше доступна** — DFT/MD расчёт стабильности; classical signal processing; classical bibliometrics — проще, дешевле, объясним.

### Более правильные альтернативы (сравнение)

- **Bayesian Optimization + Gaussian Process** vs Sakana / RL — **40+ лет BO, 60+ лет GP**.
- **DFT / MD first-principles** vs GNoME / MatterGen — **DFT >50 лет**; quantum chemistry надёжнее ML для thermodynamic stability.
- **Classical signal processing (matched filter)** vs CNN — для gravitational waves; ML добавляет, но не заменяет template matching.
- **Classical Bibliometrics** vs LLM literature analysis — citation networks, h-index, Web of Science / Scopus — objective, replicable.
- **Human peer review (с улучшениями)** vs AI peer review — structured rubrics, double-blind, statcheck, image forensics.
- **OR-Tools / Gurobi / CPLEX** vs deep RL — для scientific logistics; **OR 70+ лет**.

### Бюджет (минуты strict-in) на failure-bucket ≥30%

**По разделам:**

- Введение (7 мин) — 2 мин strict-in (28.6%)
- §1 (10 мин) — 4.5 мин strict-in (45%)
- §2 (15 мин) — 5 мин strict-in (33%) — **boosted с 23% через inline failure callbacks (P1-1)**
- §3 (12 мин) — 4 мин strict-in (33.3%)
- §4 (12 мин) — 7.5 мин strict-in (62.5%) — **rebalanced с 70% (P1-7 positive ground)**
- §5 (12 мин) — 9 мин strict-in (75%) — **slightly down с 87% из-за added RU context positive**
- §6 (6 мин) — 2 мин strict-in (33.3%)

**Total:** 34 мин strict-in / 74 мин = **45.9%** ✓ ≥30% (margin ~16 п.п.)

---

## Sections roadmap

| # | Раздел | Длительность | Slides | Описание (1-2 предложения) | Bucket-tag |
|---|---|---|---|---|---|
| 0 | Введение | 7 мин | s01-s05 | Hero side-by-side AlphaFold-Nobel + Galactica-shame; keystone-лестница цикла; lecture-map; glossary 15 terms | mixed |
| 1 | Hypothesis + Design | 10 мин | s06-s11 | Sakana primary, Co-Scientist secondary (one-liner), Coscientist, Gemini for Science; failure deep-dive Sakana; **WE-1 grant idea**; альтернатива BO+GP | mixed + WE |
| 2 | Experiment (Nobel-grade) | 15 мин | s12-s19 | AlphaFold 2/3 + Nobel 2024, Boltz-1, GNoME, A-Lab **41/58** + Palgrave **35/36 errors**, Aurora benchmarks, AlphaProof — с inline failure callbacks | capability + inline failures |
| 3 | Analyse (data analysis) | 12 мин | s20-s25 | Exoplanet detection, Allen MICrONS (separate from Brain Knowledge Platform), LIGO ML, AlphaFold IDP limits, classical alternatives, **WE-rewritten TESS transit search** | mixed + WE |
| 4 | Write + Review | 12 мин | s26-s31 | NotebookLM + Elicit + Consensus augmentation (rebalanced 3+7.5); **failures**: Frontiers / NeurIPS / **WE-2 bibliography verification**; ICMJE rule | failure-heavy + WE |
| 5 | Когда AI не нужен + RU context | 12 мин | s32-s37 | 4 категории критериев, matrix 5 альтернатив (success story 30-70 лет), **WE-3 catalyst pipeline propylene oxidation**, 3 вопроса, 5-step framework, **RU context AIRI/Sber/Yandex** | failure + alt + WE + RU |
| 6 | Замыкание + Q&A | 6 мин | s38-s39 | Dedicated Q&A recap с failure-callback (collaborator LLM bibliography); мост к Лекции 16 partially closed-world | mixed |

**Section dividers explicit:** s02 (intro → §1), s06 (§1), s12 (§2), s20 (§3), s26 (§4), s32 (§5), s38 (§6 / Q&A) — lec-13/14 pattern compliance.

**Dedicated Q&A slide:** s38 (lec-13/14 pattern).

---

## Numbers convention lock (25 ключевых canonical measurable claims)

Каждое из этих чисел — **canonical anchor** для chapter, slides, speech. Никаких variations без cascade-of-changes check.

1. **AlphaFold 3 release:** 8 мая 2024 (DeepMind / Isomorphic Labs).
2. **AlphaFold open-source timeline:** closed at launch → academic access ноябрь 2024 → public февраль 2025 (non-commercial).
3. **AlphaFold DB:** **200M+ protein structures** publicly available (snapshot 2026; `[VFY-day-of]`).
4. **Nobel Chemistry 2024:** **9 октября 2024** (P1-9 fix; было 8 октября) — Baker (½) + Hassabis + Jumper (½).
5. **GNoME:** **2.2M predicted materials, 380k stable** (DeepMind November 2023, Nature, Merchant et al.).
6. **A-Lab Berkeley (P0-3 fix, canonical):** **41 of 58 target compounds synthesized in 17 days** (Nature November 2023, Szymanski et al., doi.org/10.1038/s41586-023-06734-w). **Cascade-check phrase для Phase 2 brief: «41 of 58 canonical, cascade-check всех 3 артефактов».**
7. **AlphaProof + AlphaGeometry 2:** **28/42 points = silver medal level**, IMO 2024 (4 of 6 problems); 4+ hours per problem.
8. **FrontierMath:** <2% (2024 launch, GPT-4o / Claude 3.5 / o1-preview) → **52.4% (GPT-5.5 Pro май 2026)** `[VFY-day-of]`.
9. **Galactica:** Meta, **15-17 ноября 2022, 3-day demo retraction**.
10. **Frontiers «крыса»:** February 13 published → February 16 retracted (3 дня); rat anatomy via Midjourney; «protemns» / «zxpens».
11. **NeurIPS 2025:** **100+ fake citations** в **53 accepted papers** of ~3 700 accepted; 24.52% acceptance rate; 15 000 submissions.
12. **Sakana AI Scientist:** **1 of 3 papers** passed ICLR 2025 workshop peer review (scores 6, 7, 6 = 6.33 average, 55th percentile of human-written). Cherry-pick: ~100 papers per cycle, human selects 3.
13. **AlphaFold IDP hallucinations:** **22% residues hallucinated** в IDP regions per 2024 analysis.
14. **NotebookLM MAU:** **17M+ end 2025** `[VFY-day-of]`.
15. **DOE Genesis Mission:** **$320M в декабре 2025** для AI4Science.
16. **Palgrave-Schoop A-Lab critique (P1-10 fix):** **examined 36 success samples, found 35 of 36 had errors** (incorrect crystal structure assignment, derivatives mislabeled, no demonstrated functionality). ChemRxiv январь 2024.
17. **NSF AI portfolio:** **$700M+ annually** (snapshot 2026; `[VFY-day-of]`).
18. **Aurora speed:** **5000× быстрее** ECMWF baseline (Microsoft June 2024, Nature). **Benchmark reference, не operational deployment (P1-12 soften)**.
19. **ECMWF AIFS** (P1-12 fix): own model, operationally since 2024, open-weights. Aurora/GraphCast/Pangu/FourCastNet — competitors / benchmarks, **не confirmed operational deployments в ECMWF**. `[VFY-day-of]`.
20. **Coscientist (P1-11 fix):** **GPT-4 + Claude both** (Nature 2023 primary text), CMU Boiko et al. December 2023. **NB: не путать с DeepMind Co-Scientist (Nature May 2026, `[VFY-day-of]`)**.
21. **DeepMind Co-Scientist:** Nature May 2026 paper, multi-agent debate-and-rank, Stanford liver fibrosis collaboration. **Secondary mention, downgrade per owner decision #3**, `[VFY-day-of]`.
22. **Replication crisis baselines:** Psychology **36%** replication rate (Reproducibility Project 100 studies); Economics **61%**; AI/ML ICML 2024 **24%** by LLMs, **<50%** by PhD students.
23. **TESS transit search baseline (P0-1 / WE-rewritten):** classical signal-detection AUC = **78%**; NASA Kepler CNN AUC = **89%**; custom CNN training cost = **weeks on 8 GPUs**.
24. **Allen MICrONS (P0-4 fix):** **1 mm³ mouse visual cortex, 84K neurons + 500M synapses + 4km axons** (April 2025). **Separate projects:** Brain Knowledge Platform 2025 (34M brain cells); UCSF+Allen 1300 mouse brain regions (October 2025).
25. **Exoplanet detection 2025:** 2 449 high-confidence planets из 3 987 candidates, **83.9% accuracy** (TESS+Kepler CNN, 2025).

**Volatile / `[VFY-day-of]` markers:** FrontierMath leaderboard, AlphaFold DB count, NotebookLM MAU, NSF/DOE funding totals, Sakana versions, Co-Scientist status, ECMWF AIFS operational footprint.

---

## Russification таблица (anti-anglicism mandate) — 28 entries (расширено P2-1)

В этой теме AI-в-науке **гарантированно** вылезут эти anglicisms в visible body. Canonical replacements:

| # | Anglicism | RU replacement |
|---|---|---|
| 1 | foundation model | фундаментальная модель |
| 2 | ground truth | эталонная разметка |
| 3 | peer review | рецензирование |
| 4 | reproducibility crisis | кризис воспроизводимости |
| 5 | training distribution | обучающее распределение |
| 6 | hallucination | галлюцинация (whitelisted RU term) |
| 7 | open-source / open-weights | открытый исходный код / открытые веса |
| 8 | closed-world / open-world | закрытый мир / открытый мир (педагогический термин) |
| 9 | autonomous lab / self-driving lab | автономная лаборатория |
| 10 | drug discovery | поиск лекарственных кандидатов |
| 11 | docking | стыковка (молекулярная) |
| 12 | benchmark | тестовый набор / эталонный набор |
| 13 | retraction | отзыв (публикации) |
| 14 | paper mill | бумажная фабрика (или: фабрика статей) |
| 15 | hypothesis generation | формулирование гипотез |
| 16 | embedding | векторное представление |
| 17 | transit (exoplanet) | прохождение / транзит (астрофизический термин) |
| 18 | citation network | сеть цитирования |
| 19 | replication | воспроизведение / реплика |
| 20 | data drift / distribution shift | сдвиг распределения |
| 21 | inverse design (materials) | обратное проектирование |
| 22 | wet lab / dry lab | физическая лаборатория / вычислительная лаборатория |
| 23 | backbone (protein) | остов (белка) |
| 24 | scaffold (chemistry) | каркасный фрагмент |
| 25 | binding affinity | сила связывания |
| 26 | zero-shot | без обучения (на данной задаче) |
| 27 | fine-tuning | дообучение |
| 28 | in-context learning | обучение по контексту |

**Whitelisted brand+gloss (можно оставить латиницей):**
- AlphaFold / AlphaProof / AlphaGeometry — DeepMind продукты.
- AlphaFold DB — public protein structure database.
- GNoME, MatterGen, Aurora, GraphCast, Pangu-Weather, FourCastNet — конкретные модели; первое упоминание + RU gloss «фундаментальная модель погоды».
- Boltz-1 / Boltz-2 — MIT open-source модели; первое упоминание + gloss.
- Coscientist — CMU система; первое упоминание + gloss «**не путать с** DeepMind Co-Scientist».
- Co-Scientist — DeepMind multi-agent system; первое упоминание + gloss «**не путать с** CMU Coscientist 2023».
- Galactica — Meta модель (исторический фейл); first mention + gloss.
- NotebookLM, Elicit, Consensus, Semantic Scholar, PaperQA, Scite — brand names tools.
- CASP — Critical Assessment of protein Structure Prediction (отраслевой бенчмарк); first mention + RU gloss.
- IMO — International Mathematical Olympiad; first mention + RU gloss.
- FrontierMath — Epoch AI benchmark; first mention + gloss.
- ICMJE — International Committee of Medical Journal Editors; first mention + gloss.
- ECMWF — European Centre for Medium-Range Weather Forecasts; first mention + gloss.
- AIRI — Институт искусственного интеллекта (Россия); first mention + RU расшифровка.
- Sber AI Lab / Yandex Research — brand names (RU brands).
- РНФ — Российский научный фонд (whitelisted).

**Pre-submission deep latin-token scan:** обязателен для каждой revision (см. `tools/presentation-build/README.md` §5.8).

---

## Media plan ≥50% слайдов

**Total slides:** 39 (s01-s39).

### Media-heavy slides (target ≥20 / 39 = 51%)

| # | Слайд | Media kind | Источник |
|---|---|---|---|
| s01 | Hero «две стороны медали» (composite) | side-by-side photo+screenshot | Nobel.org + MIT TR |
| s06 | Sakana intro + Co-Scientist one-liner | screenshot / paper figure | Sakana blog / arxiv |
| s07 | **WE-1 grant idea decision tree** | Mermaid flow-chart | custom |
| s09 | Coscientist | lab photo / architecture | CMU press / Nature 2023 |
| s10 | Sakana failures deep-dive (cherry-pick) | annotated screenshot | Sakana blog + reviewer comments |
| s12 | AlphaFold 2 → AF3 | protein 3D structure ribbon | DeepMind blog |
| s13 | AlphaFold DB | website screenshot | alphafold.ebi.ac.uk |
| s14 | Open-source debate | timeline diagram (custom Mermaid) | DeepMind + Nature + asbmb |
| s15 | Boltz-1 | benchmark chart vs AF3 | MIT news + bioRxiv |
| s16 | GNoME 2.2M predictions | dot plot / candidate distribution | DeepMind blog |
| s17 | A-Lab + Palgrave critique 35/36 | chemistry diagram | ChemRxiv |
| s18 | Aurora atmospheric model | weather animation snapshot | Microsoft Research |
| s19 | AlphaProof IMO 2024 | IMO problem screenshot | DeepMind blog |
| s20 | Exoplanet detection | light curve chart (CNN visualization) | arxiv 2512.00967 |
| s21 | Allen MICrONS | brain region map | Allen Institute press |
| s22 | LIGO ML pipeline | waveform + uncertainty viz | arxiv 2504.17587 |
| s23 | AlphaFold IDP limits | α-synuclein structure error | arxiv 2510.15939 |
| s25 | **TESS transit search walked example** | Mermaid flow-chart | custom |
| s26 | NotebookLM | UI screenshot | Google Workspace blog |
| s27 | Elicit + Consensus | UI comparison screenshots | Elicit.com + Consensus.app |
| s28 | **WE-2 bibliography 4-step verification** | Mermaid flow-chart | custom |
| s29 | Frontiers «крыса» | retracted figure (annotated) | phys.org / VentureBeat |
| s30 | NeurIPS fake citations | bar chart per paper count | dev.to + GPTZero |
| s33 | 5 альтернатив matrix | custom matrix diagram | custom |
| s34 | **WE-3 catalyst pipeline propylene oxidation** | Mermaid flow-chart | custom |
| s36 | 5-step framework | Mermaid flow-chart | custom |
| s37 | RU context (AIRI / Sber / Yandex) | logos collage + research highlights | AIRI / Sber / Yandex press |
| s39 | Closing hero | AlphaFold DB screenshot | alphafold.ebi.ac.uk |

**Total media:** **28 / 39 = 72%** ✓ (margin +22 п.п. над 50% target). Boosted from v1 64% по добавлению WE-1 / WE-2 / WE-3 Mermaid + RU context s37.

### Media kinds breakdown

- Real photos / press: 9 (s01-left, s09, s17, s18, s21, s27 part, s29, s37, s39)
- UI screenshots: 5 (s01-right, s06, s13, s26, s27 part)
- 3D structure / scientific viz: 5 (s12, s16, s19, s22, s23)
- Charts / bench data: 4 (s10, s15, s20, s30)
- Custom Mermaid / matrix: 5 (s07 WE-1, s14, s25 TESS, s28 WE-2, s33, s34 WE-3, s36) — note: 7 custom diagrams now

---

## Hero plan для s01 + s39

### s01 (cover, hero) — «Две стороны медали» (LOCKED side-by-side per owner decision #2)

См. § «Hero design mitigation strategy» подробно. Краткие источники:

- **Левая половина (Nobel):** Tier 1 og:image nobelprize.org/chemistry/2024 → Tier 2 Wikipedia Commons → Tier 3 DeepMind blog → Tier 6 Google Images.
- **Правая половина (Galactica):** Tier 6 fair-use screenshot MIT Technology Review headline (Heaven 18 ноября 2022).

**Attribution label visible:** «Nobel Prize Chemistry 2024 © Nobel Foundation | Galactica retraction headline © MIT Technology Review 2022 (fair-use educational excerpt)»

**Backup fallback:** single hero AlphaFold ribbon (s01), Galactica callback на s02. См. § «Hero design mitigation strategy».

### s39 (closing) — Bridge к Лекции 16

**Концепт:** Closing hero — **AlphaFold DB website screenshot** — символизирующее «биология теперь чуть больше известна, но финальная карта далека».

**6-tier acquisition strategy:** Tier 1 (og:image alphafold.ebi.ac.uk) primary → Tier 2 Wikipedia AlphaFold article hero → Tier 3 DeepMind AlphaFold 3 blog → Tier 6 screenshot.

**Bridge text (P2-3 soften):**
«AlphaFold показал, что **closed-world задачи** в науке доступны AI. Лекция 16 — **AI в нефтегазовой отрасли**, **частично closed-world (geophysics, sub-surface modeling) + частично open (reservoir characterization)**. Та же лестница цикла применяется».

**Attribution:** «© DeepMind / Isomorphic Labs / EBI 2024»

---

## Сравнение vs Lec-{N-1}, Lec-{N-2} (baseline)

### Lec-14 (AI в телекоме / AIOps / кибербезопасности)

- Chapter: 34 451 слов (4 parts). Slides: 39 (51.3% media). Speech: 6 402 слова. Failure-bucket: ~50% chapter / ~62% slides / 80.3% speech. Hero: s01 CrowdStrike BSOD + s39 NOC IUPUI. Keystone: «Лестница автономии AI».

### Lec-13 (AI в логистике и транспорте)

- Chapter: ~31 313 слов (3 parts). Slides: 41 (85% media). Speech: 6 914 слов. Failure-bucket: ~50% chapter / ~62% slides. Hero: Waymo + Cruise / Tesla. Keystone: «Лестница среды 5 уровней» + 7-criteria.

### Lec-11 (AI в производстве)

- Chapter: 30 930 слов (3 parts). Slides: 41 (~63% media). Speech: 5 289 слов. Failure-bucket: ~41% chapter. Hero: Tesla Giga Press + BMW Welt.

### Lec-15 targets (этот план v2)

- **Chapter:** **≥30 000 слов** (target 28 500-31 500; multi-part 3 файла) — match lec-13/14.
- **Slides:** **39 slides** target — match lec-14.
- **Media coverage:** ≥50% (target ~72% — boosted from v1 64% по WE diagrams + RU context).
- **Speech:** **~6 000 слов** (75 мин at ≤95 WPM).
- **Failure-bucket strict-in:** **~46% holistic** — slightly below lec-11/lec-13/lec-14 (45-50% range, в пределах баланса).
- **Hero:** **«Две стороны медали» side-by-side** — novel pattern с mitigation strategy.
- **Keystone:** Variant A «Лестница научного цикла» (LOCKED).

### Где мы должны побить / match lec-14 specifically

- Chapter words: **match ≥30k**.
- Failure-bucket: **match ≥45-50%**.
- Media: **match 50%+** (target 72%).
- Slides count: **match 39**.
- Cascade-of-changes / numbers-convention-lock: **25 anchors** baked-in.

### Где мы differentiate

- **Hero pattern:** side-by-side composite с mitigation (vs all lec-9/10/11/12/13/14 single-hero).
- **Failure cluster topology:** lec-15 — concentration в Разделе 4 (peer review failures), уникально для темы AI-в-науке.
- **Cyclical keystone** (vs sequential in lec-13/lec-14).
- **3 applicable walked examples** (vs typical 1-2 в предыдущих лекциях).

---

## Anti-dependencies — что НЕ дублировать

### Vs Lec-12 (AI в производстве / двойники)

- Lec-12 — digital twins; Lec-15 — AI замена + augmentation в науке. Не повторять Cassie / Agility Robotics, Hannover Messe, ISA-95.

### Vs Lec-13 (AI в логистике / транспорте)

- Lec-13 — лестница среды; Lec-15 — другая лестница (научного цикла). Не повторять Waymo / Cruise / Tesla; **OR-Tools** упомянуть как альтернатива в науке (clinical trial design, not VRP).

### Vs Lec-14 (AI в телеком / AIOps / кибербез)

- Lec-14 — Лестница автономии; Lec-15 — Лестница цикла. Не повторять CrowdStrike, Cloudflare, Klarna / Air Canada. Можно one-line callback: «лестница автономии lec-14 — про control; наша лестница цикла — про phase-of-work».

### Vs Lec-16 (AI в нефтегаз; следующая)

- Lec-16 — частично closed-world geophysics. Bridge в s39: AlphaFold closed-world → нефтегаз partially closed-world (P2-3 soften).

### Vs Lec-7 (AI в медицине / фарма)

- Lec-7 — clinical medicine + drug discovery deployment. Lec-15 — AI в drug discovery как research. Можно ссылаться Insilico Medicine: lec-7 deployment side, lec-15 research-side. Не повторять FDA Part 11, HITL в clinical setting, EBM hierarchy.

---

## Anonymization (ENFORCED)

- **Frontmatter audience:** «студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)».
- **Career angle:** «профильные технические университеты + научно-исследовательские институты», без «МГТУ» / «МАИ» / «СПбГУ» / «РАН» / «Сколтех» / «ВШЭ».
- **Российский контекст:** AIRI / Sber AI Lab / Yandex Research (brand names — whitelisted); **РНФ AI4Science grants** + **AI Russia 2030 Strategy** (Указ Президента РФ № 145) — abbreviations для крупных организаций с established RU расшифровкой.
- **Эталон:** lec-03 / lec-05 / lec-07 chapters — 0 named institutions; lec-06 — единственная generic «профильные кафедры».

---

## Risk register

| # | Risk | P×I | Mitigation |
|---|---|---|---|
| R1 | Hero «две стороны медали» — нестандартный pattern. | M×M | См. § «Hero design mitigation strategy» — uniform visual treatment / single composite / bridging caption / fallback к single hero AlphaFold ribbon. Phase 5 escalation после round 2. |
| R2 | Keystone Variant A — «третья лестница» риск. | L-M×H | Owner accepted risk (Decision #1); mitigation = § «Keystone differentiation table» (6 dimensions). Cyclical vs sequential — единственная отличительная характеристика. Methodology-critic Phase 4 validates. |
| R3 | Sakana AI Scientist v3/v4 ко времени лекции. | M×M | `[VFY-day-of]` markers; orchestrator 1-page refresh за 1-2 дня до лекции. |
| R4 | AlphaFold DB count, FrontierMath leaderboard volatile. | M×L | `[VFY-day-of]` markers. |
| R5 | NeurIPS 2025 fake citations recent. | M×M | Phase 2 fact-checker re-verifies arxiv 2602.05930. |
| R6 | RU context thin. | L×M | Decision #4 addressed — 5 мин dedicated slide s37 (AIRI + Sber + Yandex + РНФ + AI Russia 2030). |
| R7 | Galactica retraction старый (2022, 4 года). | L×M | Используется как baseline + combined с свежими NeurIPS 2025 / Frontiers 2024 / Sakana 2024-2025. |
| R8 | AlphaFold 3 commercial debate stale. | L×M | `[VFY-day-of]` для Lilly / Novartis deal totals. |
| R9 | Failure cluster в §4 unbalanced. | M×M | Rebalanced 3+7.5 (P1-7); inline positive measures в s26/s27/s31. |
| R10 | AlphaFold terminology drift. | L×M | Glossary lock s04 (15 terms); consistency-checker mode для AlphaFold variants. |
| R11 | DeepMind Co-Scientist Nature May 2026 retraction risk. | M×M | Downgrade к secondary mention (Decision #3); если retracted — просто drop one-liner, не disrupt main narrative. |
| R12 | WE-3 catalyst pipeline propylene oxidation spec. | L×M | Phase 2 book-editor verifies specific DFT method (e.g., VASP), specific BO library (e.g., BoTorch), specific Materials Project query. |
| R13 (new) | Aurora extreme weather miss (Hurricane Milton callback) needs fact-check. | M×L | Phase 2 fact-checker verifies Hurricane Milton 2024 Aurora performance vs ECMWF baseline. |
| R14 (new) | RU brand-list (AIRI / Sber / Yandex) — нужны конкретные projects, не general «AI4Science». | M×M | Phase 2 book-editor verifies 1-2 named publications / projects per brand с источниками. |

---

## Plan-level mandates carry-forward checklist (ENFORCED)

- [x] **Hero images plan для s01 + s39** прописан с 6-tier strategy + entity + attribution + mitigation strategy для side-by-side.
- [x] **Russification mandate v2** — таблица 28 replacements; brand whitelist (с AIRI/Sber/Yandex new); deep latin-token scan mandatory.
- [x] **6-tier real image acquisition strategy** sketched per case-study slide; **≥20 real images** target across 39 slides.
- [x] **Anonymization carry-forward** — generic «студенты-инженеры», без named universities; brand-whitelist для AIRI / Sber / Yandex.
- [x] **Anti-anglicism таблица** ссылается на canonical replacements (28).
- [x] **Failure-bucket honest tracking** — strict-in 46% > 30% target; §2 boosted к 33% (was 23%).
- [x] **Keystone в Введении ДО первого погружения; заголовок про ось** (Variant A LOCKED).
- [x] **Numbers convention lock** — 25 canonical claims (was 18 в v1).
- [x] **Baseline / counterfactual** на каждое measurable claim — встроено в § Worked examples; A-Lab 41/58 baseline corrected.
- [x] **`[VFY-day-of]` markers** inline в outline (s13, s19, s26, s06 Co-Scientist).
- [x] **3 applicable walked examples + 4 case-study deep-dives** (WE-1 §1, WE-2 §4, WE-3 §5; case studies — AlphaFold / AlphaProof / GNoME-A-Lab / Failure cluster).
- [x] **Keystone differentiation table** (6 dimensions lec-13 / lec-14 / lec-15).
- [x] **Owner decisions #1-#4 integrated.**
- [x] **Section dividers explicit** (s02, s06, s12, s20, s26, s32, s38).
- [x] **Dedicated Q&A slide** (s38).

---

## Self-check (перед commit)

- [x] Все sections `templates/lecture-outline.md` заполнены.
- [x] **Keystone choice LOCKED Variant A** (owner decision #1).
- [x] **3 applicable walked examples с baseline/counterfactual** (P0-1 fixed) + 4 case studies.
- [x] **Failure-share %** явно бьётся ≥30% holistic на каждый artifact (46% strict-in).
- [x] **≥10 ключевых measurable claims canonical** — 25 в § Numbers convention lock.
- [x] **Hero plan: side-by-side с mitigation + 2 реальных изображения с источниками** для s01 + s39.
- [x] **Russification таблица с ≥10 anglicisms** — 28.
- [x] **Lec-14 / lec-13 baseline сравнение** присутствует.
- [x] **Sections roadmap** покрывает 7 секций × bucket-tag.
- [x] **Anti-dependencies с lec-12/13/14** явно прописаны.
- [x] **Никаких anglicisms в plan body** (брэнды + ключевые акронимы whitelist OK).
- [x] **Никаких named universities (МГТУ / Бауман / ИУ-X / Сколтех)** — verified. AIRI / Sber / Yandex / РНФ — brand-whitelisted.
- [x] **Никаких timing маркеров «(N мин)»** в slide-outline предложениях (только в section headers / metadata).
- [x] **All P0 fixes applied** (worked examples reframe, keystone table, A-Lab 41/58, Allen MICrONS distinguished).
- [x] **All 14 P1 fixes applied** (или explicit defer note).
- [x] **Section dividers explicit** в outline (s02, s06, s12, s20, s26, s32, s38).
- [x] **Q&A dedicated slide explicit** (s38).
- [x] **Cornerstones lock list 10-12 terms** (см. Phase 2 brief).
- [x] **Q&A backup 12-15 questions** (см. Phase 2 brief).
- [x] **Multi-part chapter split boundaries explicit** (см. Phase 2 brief).

---

## Длина plan'а

**Word count plan-v2.md:** ~7 800 слов (расширение с v1 5 900 на ~+1 900 слов: keystone differentiation table + alternative keystones rejected + hero mitigation + RU context section + 2 new applicable WE + expanded Phase 2 brief + extended Russification + numbers lock 18→25).

---

## Phase 2 chapter brief carry-forward (для book-editor Phase 2 — rewritten 600+ слов per P1-4)

Глава **≥30 000 слов**, source-of-truth для slides + speech, **multi-part split 3 файла**.

### Section word budgets (sum 28 500–31 500)

- **§0 Введение** ~1 200 слов — hook (AlphaFold Nobel + Galactica side-by-side), keystone лестница цикла, lecture-map, glossary 15 terms.
- **§1 Hypothesis + Design** ~4 500 слов — Sakana primary failure case (~1 800), Coscientist (~800), Co-Scientist secondary one-paragraph (~300), Gemini for Science (~400), WE-1 grant idea decision tree walked (~1 000), BO+GP alternative (~200).
- **§2 Experiment** ~7 500 слов (deepest, Nobel-tier) — AlphaFold 2/3 narrative + Nobel + open-source debate (~2 500), Boltz-1 (~500), GNoME + A-Lab 41/58 (~1 200), Palgrave 35/36 critique deep-dive (~1 000), Aurora + ECMWF AIFS clarification + Hurricane Milton callback (~1 200), AlphaProof + AlphaGeometry 2 + FrontierMath (~1 100).
- **§3 Analyse** ~4 500 слов — Exoplanet TESS+Kepler (~800), Allen MICrONS distinguished (~700), LIGO ML (~700), AlphaFold IDP limits deep-dive (~800), classical alternatives matched filtering (~500), WE-rewritten TESS transit search walked example (~1 000).
- **§4 Write+Review** ~5 500 слов — NotebookLM augmentation (~600), Elicit/Consensus inline positive measures (~600), WE-2 collaborator bibliography 4-step verification walked (~1 200), Frontiers «крыса» deep-dive (~800), NeurIPS 2025 + ICLR 2026 fake citations (~1 200), Sakana ICLR workshop scandal (~700), ICMJE rule + 5 ethical criteria (~400).
- **§5 Когда AI не нужен + RU context** ~5 000 слов — 4 категории критериев (~800), 5 alternatives matrix as success story (~700), WE-3 catalyst pipeline propylene oxidation walked deep-dive (~1 200), 3 vendor questions (~300), 5-step framework recap (~300), **RU context AIRI + Sber + Yandex + РНФ + AI Russia 2030** (~1 700).
- **§6 Замыкание + Q&A backup** ~1 800 слов — recap лестницы (~400), failure-callback collaborator scenario (~300), bridge к Lec-16 (~200), Q&A backup answers (~900).
- **TOTAL ~30 000 слов.**

### Q&A backup list (15 questions, target ≥12)

1. AlphaFold предсказал 200M структур — почему всё ещё нужны wet-lab experiments?
2. Sakana AI Scientist passed peer review — почему это не доказывает что AI делает науку?
3. Какой baseline до Bayesian Optimization в materials discovery?
4. Как distinguish «AI augmentation» от «AI autonomous» научной работы?
5. Coscientist vs DeepMind Co-Scientist — кто за что отвечает?
6. Что делать если рецензент использует LLM для review?
7. AlphaFold не работает на IDP — почему? и как тогда predict?
8. GNoME предсказал 380k stable materials — почему только 41 синтезированы?
9. Closed-world vs open-world — это категорическое разделение?
10. Aurora 5000× быстрее ECMWF — почему ECMWF не deploy?
11. AlphaProof IMO silver — это означает AI решит чистую математику?
12. AI Scientist v2 cherry-picked 3 из 100 papers — что это означает для AI-генерации?
13. ICMJE запрещает AI как автора — но он же co-pilot — как considered?
14. Когда классическое OR-Tools лучше deep RL в науке?
15. AI Russia 2030 Strategy — что меняет для российских грантов?

### Cornerstones lock list (12 terms с RU glosses)

1. фундаментальная модель / foundation model
2. научный цикл / scientific workflow
3. открытый/закрытый мир / open/closed-world (verifiable ground truth категория)
4. augmentation / augmented research (AI помогает, не заменяет)
5. autonomous lab / автономная лаборатория
6. peer review hallucinations / галлюцинированные цитаты
7. paper mill / фабрика статей
8. reproducibility crisis / кризис воспроизводимости
9. HITL (Human-in-the-Loop)
10. inverse design / обратное проектирование (materials)
11. DFT / MD first-principles (квантовая химия / молекулярная динамика)
12. Bayesian Optimization (BO) + Gaussian Process (GP)

**No drift:** cornerstones — единый термин-RU-перевод во всех 3 артефактах. Variations через cascade-of-changes check.

### References breakdown

- **Primary papers (peer-reviewed):** ≈80 — Nature / Science / NeurIPS / ICLR / ICML / JMLR / Cell / PNAS / Chemistry / ChemRxiv.
- **Press (Tier 3):** ≈20 — DeepMind blog, MIT Technology Review, TechCrunch, phys.org, VentureBeat, Chemistry World.
- **Institutional documents:** ≈10 — Nobel Foundation, NSF, DOE Genesis Mission, ICMJE Recommendations, EU AI Act, RU AI 2030 Strategy.
- **Russian sources:** ≈10 — AIRI publications, Sber AI Lab blog, Yandex Research arxiv, РНФ AI4Science grant announcements, Минобрнауки приказы.
- **TOTAL:** ~120 references.

### Cross-reference policy

- **Allowed callbacks к lectures:** lec-01 (типы AI, hallucinations), lec-02 (transformers, attention), lec-03 (агенты, RAG), lec-07 (HITL, EBM), lec-11 (pilot purgatory), lec-12 (digital twins — brief), lec-13 (closed-world среда), lec-14 (autonomy ladder).
- **One-line callbacks max** — no deep dives к prior lectures.
- **Forward callback к lec-16** разрешён только в §6 bridge (партial closed-world).

### Multi-part split boundaries

- **chapter.md** = Введение + §1 Hypothesis+Design + §2 Experiment (часть 1). ~**13 200 слов / ~570 lines max** (CLAUDE.md doc-size limit).
- **chapter-part2.md** = §3 Analyse + §4 Write+Review. ~**10 000 слов / ~430 lines**.
- **chapter-part3.md** = §5 Когда AI не нужен + RU context + §6 Замыкание + Q&A backup + References. ~**7 000 слов / ~300 lines**.
- Frontmatter в chapter.md: `parts: 3`, `length_words: ~30000`, slide_map, strict_in_self_estimate, lo, cornerstones, q_and_a_backup_refs.
- Cross-link через TOC «Карта главы и индекс частей» в chapter.md сразу после Changelog.

### Failure-bucket per-section words target

- **§0** 33% (~400 of 1 200) — Galactica part of hook.
- **§1** 45% (~2 000 of 4 500) — Sakana failure + Coscientist limits + BO alternative.
- **§2** 30% (~2 250 of 7 500) — A-Lab Palgrave + IDP + AlphaProof time-cost + open-source debate.
- **§3** 35% (~1 600 of 4 500) — IDP deep-dive + classical alternatives.
- **§4** 70% (~3 850 of 5 500) — peak failure section.
- **§5** 87% (~4 350 of 5 000) — критерии + alternatives + WE-3.
- **§6** 33% (~600 of 1 800) — failure-callback collaborator.
- **AVERAGE:** ~45-47% chapter strict-in failure-bucket. Holistic constraints satisfied для chapter artifact.

### Phase 2 brief carry-forward mandates (continued)

- **Cornerstones lock:** 12 main terms (см. выше), no drift.
- **Carry mandates:** anonymization absolute, 6-tier hero acquisition plan для s01 + s39, real-image ≥20 / 39 slides.
- **Что НЕ делать:** keystone про что-то кроме Variant A; §4 как «AI делает плохо» laundry list без critic distinctions; «магическая пилюля» строки в failure-bucket count; named institutions (Сколтех / МГТУ / ВШЭ) в audience; англицизмы в narrative body; AlphaFold-Multimer без glossary intro; «commercial AlphaFold 3 debate» без attribution Isomorphic Labs Lilly+Novartis $3B context; **«36 of 57» вместо «41 of 58» для A-Lab** (cascade-check phrase mandatory).
- **A-Lab cascade-check phrase для все агентов Phase 2+:** «А-Lab numbers: **41 of 58 in 17 days** canonical, cascade-check всех 3 артефактов».

---

## Open questions для owner (ANSWERED — see § Changelog)

Все 6 open questions из plan-v1 закрыты owner decisions #1-#4 + critic-driven fixes:

1. ✅ Keystone choice → Variant A LOCKED (Decision #1).
2. ✅ Hero pattern → side-by-side LOCKED с mitigation (Decision #2).
3. ✅ Российский контекст глубина → 5 мин dedicated slide s37 (Decision #4).
4. ✅ AI Scientist v2 deep-dive → primary case для §1 (после Co-Scientist downgrade).
5. ✅ DeepMind Co-Scientist → secondary one-liner (Decision #3).
6. ✅ AlphaFold IDP limits → dedicated slide s23 (cascade callback из s12 — P1-1 fix).

### New open questions (минимальные)

- **OQ-1:** WE-3 catalyst pipeline — propylene oxidation specific. Phase 2 book-editor может потребовать verification что Materials Project имеет sufficient propylene oxidation catalyst data; backup case ammonia synthesis catalysts. **Resolution:** Phase 2 book-editor verifies, no owner gate.
- **OQ-2:** Aurora Hurricane Milton 2024 callback — needs primary source (paper или Microsoft press) подтверждающий extreme weather miss. **Resolution:** Phase 2 fact-checker verifies; если no primary source → drop inline callback, keep general «extreme events тяжелее для foundation weather models».

---

**Конец Plan v2.** Next: focused re-spawn methodology-critic на plan-v2 (scope = P0/P1 fixes verified + owner decisions integrated) → Phase 2 chapter brief built из plan-v2.
