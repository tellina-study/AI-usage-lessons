VERDICT: REVISE

# Methodology Critic Report — Лекция 15 chapter v1.0 — 2026-05-27

**Артефакт:** `library/lectures/lec-15/chapter.md` + `chapter-part2.md` + `chapter-part3.md` (28 604 слов суммарно, 3 файла)
**Phase:** 3 (post-Phase-2 book-editor initial draft critique)
**Reference:** plan-v2 APPROVE-WITH-POLISH (qa-reports/2026-05-27-v2-plan/methodology-critic.md)

---

## Severity counts

- **P0 (blocking — must fix до USER GATE A):** 2
- **P1 (should-fix — shipping degrades quality):** 9
- **P2 (nice-to-fix):** 4

**Counter-check:** 9 P1 > 5 threshold → verdict **REVISE** (not APPROVE-WITH-POLISH). P0 #1 (Russification structural failure) — also independently triggers REVISE.

---

## Executive summary

Chapter v1 — **substantively сильный методологический draft** на verbal-content уровне:
- Структурно соответствует plan-v2 ToC (39 slide-маркеры в narrative, multi-part split valid, 3 walked examples explicit, 4 case-deep dives present).
- Number anchors verified: A-Lab «41 of 58 за 17 дней» canonical 6× + Palgrave «35 of 36» canonical 4×, Nobel 9 октября 2024, Coscientist «GPT-4 + Claude both», AlphaFold IDP 22%, NeurIPS 100+/53/24.52%, FrontierMath 52.4%, AlphaProof 28/42 + 4ч, GNoME 2.2M/380k/44×, MICrONS отделён от BKP/UCSF+Allen, Galactica 3 дня, Frontiers 13→16 февраля — 8/8 spot-checked anchors консистентны.
- Cornerstones cyclically reinforced через 3 части: 12 терминов lock все встречаются ≥2× с canonical first-mention gloss.
- 0 named Russian universities в narrative body (anonymization absolute holds).

**Но** chapter v1 имеет **2 catastrophic-class P0 проблемы**, обе structural-не-polish:

1. **P0-CHAPTER-1: Russification mandate failure (≈485 critical anglicism hits + 906 mixed-language sentences).** Это нарушает explicit MEMORY rule [[russification]] и **CLAUDE.md "Russification" anti-pattern**. Narrative body читается как **English-Russian code-switch**, не как Russian с whitelisted terminology. Many sentences contain 20-35 English words (top extreme: 35-word Latin density). Critical blacklist hits: 485 (production / accuracy / pipeline / workflow / verification / review / ML / baseline / deployment / training data + 15 more). Per-file: 113 / 228 / 144. Это **producer-agent excessive anglicism leak**, требующий полного rewrite narrative voice. **Owner правит каждую лекцию вручную** — это P0 systemic failure.

2. **P0-CHAPTER-2: Chapter depth target undershoot, all sections under plan budget.** Total 28 604 слов = +104 слов over P0-BLOCKING floor (28 500), но **-1 396 слов под 30k target center** (4.7% under). Critically — **все 7 sections under plan-v2 word budget**: §0 OK / §1 −514 / **§2 −2 488 (33% under target)** / §3 −506 / §4 −701 / §5 −1 021 / §6 −1 033. §2 «Experiment» — самый длинный раздел плана (7 500 целевых) — реально 5 012 (33% short). §6 «Замыкание» — 767 vs target 1 800 (43% short). Single weak file = noise, но **систематический undershoot ВСЕХ sections** = book-editor systematically underdelivered depth. Это не «approach к target», это «under target почти везде». Per CLAUDE.md «Chapter Depth Baseline (ENFORCED)» — L4+ chapter target **28 500–31 500** strict; 28 604 формально passes floor, но pedagogically lecture truncates intended depth. **P0 потому что P0-BLOCKING floor 28 500 met, но systematic per-section shortfall означает каждый section ослаблен** vs intended depth. Phase 4 revision MUST expand §2 / §6 minimum, ideally all sections к plan target.

**Cascade P1 issues (from plan-critique forewarned):**
- **P1-CHAPTER-3 — «Pedagogical» label cascade leak materialised (predicted in plan v2 critique P1-new).** 4 instances confirmed: chapter.md:306 «Pedagogical insight.» / part2.md:289 «Главный pedagogical insight» / part3.md:241+251 «pedagogical insight / takeaway». Plus 1 meta-comment: «central pedagogical goal этой лекции» (part2.md:184). Plus 1 more «педагогический термин лекции» (chapter.md:163). Violates No-Methodology-In-Slides mandate cascade (applies to ALL student-facing body per [[no-timing-no-methodology-in-slides]] ENFORCED).

Все остальные P1 — recoverable polish, не structural.

**Strict-in AI-failure measurement re-verified:** producer self-report 45.9% accurate; my close-reading estimate weighted 54.6%. ≥30% holistic threshold met. §3 lowest (~35%) but ≥30% boundary respected. Holistic distribution across 6 sections — pass. **No P0 on failure-share.**

**Verdict drivers:** P0 #1 (Russification) alone = REJECT-territory if reading strict; combined with P0 #2 (depth shortfall в каждом section) + 9 P1 → **REVISE**, не APPROVE-WITH-POLISH. Phase 4 revision required: deep Russification rewrite + per-section expansion + 6 P1 fixes.

---

## P0 findings (BLOCKING — must fix до USER GATE A)

### P0-CHAPTER-1: Russification mandate failure — narrative body excessive anglicisms

**Severity:** P0 (structural, не polish; explicit memory rule [[russification]] + CLAUDE.md mandate)

**Evidence:**
- **485 critical-blacklist anglicism hits в narrative body** (per-file: 113 / 228 / 144):
  - `pipeline` 21×, `workflow` 27×, `verification` 64×, `review` (вне «peer review») 93×, `baseline` 30×, `ML` 51×, `ground truth` 26×, `accuracy` 27×, `production` 16×, `deployment / deployed / deploy` 18×, `training data / training distribution` 18×, `downstream` 8×, `insight` 8×, `structural` 20×, `interpretable` 6×, `regulatory` 6×, `ecosystem` 2×, `scaling` 7×, `approach` 5×, `tradeoff` 0×, `takeaway` 1×
- **906 mixed-language sentences с ≥4 Latin words** total (chapter.md 162 / part2.md 421 / part3.md 323). 
- **Extreme density samples** (real text from chapter):
  - «Когда выбираете AI-tool для academic work: (a) **default к open-source** unless есть сильная причина для closed (например, нужен specific feature, доступный только в closed); (b) **проверьте, активна ли open community** (GitHub stars, recent commits, разнообразие contributors); (c) **планируйте, что вы будете делать через 3-5 лет**…» — 23 Latin words в одном предложении.
  - «Применимы в scientific logistics (clinical trial design — minimizing patient enrollment time под constraints; biology experiment scheduling — multi-step protocols под resource constraints; particle physics experiment optimization — beamtime allocation), grant allocation, resource planning.» — 27 Latin words.
  - «**OK only with verification + disclosure** — generating bibliography (vereft each citation), generating draft sections (rewrite в your voice)…» — 28 Latin words.
  - «ECMWF operational system requires: (a) data assimilation (часами supercomputer time, not part of Aurora benchmark); (b) operational reliability (decades of validation, not yet established для foundation models)…» — 32 Latin words.
- Many sections read как pure English с Russian connectives: «scaling task that would otherwise be impossible» / «**Это** the form of AI применение **in science**, которая работает в 2026 году» / «Это **promising**, но still **in pilot phase**».

**What's allowed (whitelist):**
- Brand names: AlphaFold, GNoME, Sakana, NotebookLM, Elicit, Aurora, GraphCast, AIRI, Sber, Yandex, etc.
- Established acronyms с inline gloss: HITL (human-in-the-loop, человек в петле), RAG, DFT, MD, BO, GP, CASP, IMO, ICMJE
- Mode names: «augmentation», «autonomous», «paper mill» (these have RU equivalents — but если фиксированы как cornerstones, OK)
- URLs / DOIs / paper titles

**What's NOT allowed (must be Russified):**
- `pipeline` → конвейер / процессная цепочка / пайплайн (если cornerstone — fix once)
- `workflow` → рабочий процесс / схема работы
- `verification` → проверка / верификация (RU равноценная)
- `production` → производство / промышленная среда / эксплуатация
- `deployment` → развёртывание
- `accuracy` → точность
- `baseline` → базовая линия / эталон / отправная точка
- `ground truth` → эталонная истина / эталонная разметка
- `training data` → обучающие данные
- `training distribution` → обучающее распределение
- `downstream` → последующий / нисходящий
- `ML` → МО (или ML с pre-gloss)
- `tradeoff` → компромисс / соотношение
- `insight` → инсайт is OK, но «Главный insight» лучше «Главный вывод»
- `peer review` cornerstone OK once defined, но «review» standalone → «рецензирование» / «проверка»
- `framework` → фреймворк (OK как cornerstone)
- `papers / paper` → статьи / статья
- Десятки others (`research`, `verification`, `infrastructure`, `commercial`, `vendor`, etc.)

**Why P0 не P1:**
- Owner explicit memory rule [[russification]] flagged repeatedly: «producer-agents склонны excessive англицизмам... user правит в КАЖДОЙ лекции»
- Lec-08 production: 919 unique latin tokens в speech → owner REJECT «провал» → 3h wasted
- This chapter has same scale of anglicism leak в narrative
- **Not polish.** Requires systematic narrative rewrite, not local edits

**Recommendation:**
1. **Phase 4 brief к book-editor:** mandatory pass «глубокая руссификация narrative body».
2. **Explicit blacklist** (top 30 critical anglicisms with canonical RU replacements) включить в brief.
3. **Whitelist** (12 cornerstones + brand names + acronyms with gloss) explicit.
4. **Pre-submission orchestrator grep** на rendered chapter — strict-in: critical-blacklist hits = 0 в narrative body.
5. **Cost estimate:** ~6-8 hours systematic rewrite (3 files × 2-3h each) — но pays off vs owner manual rewrite каждой лекции.

---

### P0-CHAPTER-2: Systematic per-section depth shortfall — every section under plan-v2 budget

**Severity:** P0 (28 604 слов meets 28 500 floor, **но всех 7 sections shortfall** означает каждый pedagogical block недодан)

**Evidence:**

| Section | Plan target | Actual | Delta | % under | Severity |
|---|---|---|---|---|---|
| §0 Введение | ~1 200 | 2 232 | +1 032 | +86% | OVER (Acceptable) |
| §1 Hypothesis+Design | ~4 500 | 3 986 | -514 | -11.4% | Borderline |
| **§2 Experiment** | **~7 500** | **5 012** | **-2 488** | **-33%** | **CRITICAL** |
| §3 Analyse | ~4 500 | 3 994 | -506 | -11.2% | Borderline |
| §4 Write+Review | ~5 500 | 4 799 | -701 | -12.7% | Borderline |
| §5 Когда AI не нужен | ~5 000 | 3 979 | -1 021 | -20.4% | Significant |
| **§6 Замыкание** | **~1 800** | **767** | **-1 033** | **-57%** | **CRITICAL** |
| Q&A backup | ~1 500 | 1 526 | +26 | OK | OK |
| Источники | varies | 849 | n/a | OK | OK |
| **TOTAL narrative** | ~30 000 | **27 755** narrative + 849 sources = **28 604 total** | -1 396 vs 30k center | -4.7% | Marginal |

**Why §2 + §6 are CRITICAL:**

**§2 Experiment** — самый длинный раздел плана (7 500 слов = 25% deck-time = 18-минутный peak section). Actual 5 012 = 33% short. Per plan v2 ToC: §2.1 AlphaFold deep-dive / §2.2 AlphaFold DB / §2.3 Open-source debate + Boltz / §2.4 GNoME+A-Lab / §2.5 Palgrave-Schoop / §2.6 Aurora+ECMWF / §2.7 AlphaProof+IMO — 7 sub-sections, each averaged 715 words. Plan target distribution: §2.1 ~1500 / §2.5 ~800 / §2.6 ~1500 / §2.7 ~1500 — book-editor delivered только ~700/section average. **Missing depth signals:** (a) AlphaFold transformer architecture detail thin (one para vs ~500 words intended); (b) Boltz technical comparison к AF3 minimal (~150 vs ~400 intended); (c) Aurora data assimilation discussion present but compressed.

**§6 Замыкание** — final raised payoff section. Plan target 1 800 = pledge + mosт к Лекции 16 + reflection prompt. Actual 767 = 43% short. **Missing depth:** (a) Final synthesis recap каждой ступени лестницы — present but truncated; (b) personal pledge expanded к 5 commitments OK, но reflection prompt only ~200 words vs ~600 intended; (c) bridge к Лекции 16 just 3 bullets, не full mini-section.

**§5 also significantly short (-20%):** 5 категорий критериев present, но §5.6 Russian context received only ~1 500 words vs ~2 000 intended (3 cases + regulatory frame + failures — each compressed).

**Pedagogical impact:** Phase 4 GATE A reviewers will reach end of chapter feeling lecture **completes prematurely**. §2 (Nobel-grade core) lacks deep technical exposition student-engineer expects from серьёзного university chapter. §6 closing doesn't earn its pedagogical weight; pledge + reflection prompt deserve fuller treatment.

**Why P0:**
- CLAUDE.md «Chapter Depth Baseline» says 28 500 floor met → P0 BLOCKING does not technically apply
- **But systematic per-section shortfall** = degraded depth pattern, не «one shy section, rest fine»
- Phase 4 revision must address §2 + §6 minimum; ideally all 6 sections
- Cost-of-omission high: lecture feels truncated; chapter no-longer-serves as deep Q&A reference

**Recommendation:**
1. **Phase 4 brief:** explicit expansion targets per section с conкретикой:
   - §2: +2 500 words (deepen §2.1 AlphaFold transformer architecture / §2.3 Boltz technical / §2.6 Aurora extended critique).
   - §6: +1 000 words (full pledge with reasoning / reflection prompt deeper / mostик к Лекции 16 expanded к 200+ words).
   - §1 / §3 / §4 / §5: +500-1 000 words each (deepen alternative comparisons, expanded counter-claims).
2. **Total target:** chapter narrative к ~30 500-31 000 (deck-target met с margin).
3. **Acceptance criterion:** every section ±10% of plan-v2 budget; no section <80% of plan.

---

## P1 findings (should-fix)

### P1-CHAPTER-3: «Pedagogical» label cascade leak (predicted by plan-v2 critique)

**Severity:** P1 (forewarned by plan-v2 critique P1-new; not blocking but explicit ENFORCED rule violation)

**Evidence (6 instances):**
1. **chapter.md:163** «**Closed-world / open-world** — **педагогический термин лекции**.»
2. **chapter.md:306** «**Pedagogical insight.** Применение AI в hypothesis generation **тренирует**…»
3. **chapter-part2.md:184** «…что и есть **central pedagogical goal этой лекции**.»
4. **chapter-part2.md:289** «**Главный pedagogical insight**. В 2026 году студент-выпускник…»
5. **chapter-part3.md:241** «Главное pedagogical insight: Russian aspirant…»
6. **chapter-part3.md:251** «**Pedagogical takeaway.** Russian scientific work…»

**Why P1:**
- Plan-v2 critique explicitly predicted this cascade risk (строки 444+453 в plan «Pedagogical lesson:» / «Pedagogical context.» annotations)
- Recommendation #1 from plan-critique: «**Phase 2 brief explicit instruction:** strip 'Pedagogical lesson:' / 'Pedagogical context.' labels from RU context narrative»
- **Book-editor did NOT strip; instead carried forward + expanded** к 6 instances across all 3 parts
- Violates No Timing/Methodology in Slides rule [[no-timing-no-methodology-in-slides]] which applies to ALL student-facing narrative (chapter is student-facing material)
- CLAUDE.md anti-pattern entry: «Методические комментарии в visible body slides» — chapter also visible body per [[no-timing-no-methodology-in-slides]]

**Recommendation:**
1. **Strip all 6 instances:** rewrite каждое как direct chapter prose without meta-label.
   - «**Pedagogical insight.** X» → «**X.**» (direct claim)
   - «central pedagogical goal этой лекции» → «central capability аспирант должен build» OR remove entirely
   - «педагогический термин лекции» → «термин лекции» (drop «педагогический»)
2. **Phase 4 brief:** explicit «zero pedagogical/methodological meta-labels в chapter body, even в Acknowledgements section».
3. **Pre-USER-GATE A walkthrough:** grep `(методическ|педагогическ|pedagogical)\s*\w+` на rendered chapter mandatory (0 hits в body, frontmatter OK).

---

### P1-CHAPTER-4: §2 Experiment shallow technical depth (AlphaFold + Boltz + Aurora technical exposition compressed)

**Severity:** P1 (related to P0-CHAPTER-2 but specific section quality issue)

**Evidence:**
- **§2.1 AlphaFold 2 architecture explanation** — line 383-385 says «AlphaFold 2 — третий путь: использовать **multiple sequence alignment** (MSA) как proxy для evolutionary information, и attention mechanism transformer'а для извлечения геометрии…» This is **one paragraph for a Nobel-grade prize-winning architecture**. Plan-v2 budget intended ≥500 words здесь — actual ~250 words technical depth (rest is context/Nobel narrative).
- **§2.3 Boltz comparison к AF3** — line 422 «На бенчмарках protein-only prediction Boltz-1 и AlphaFold 3 показывают сравнимые результаты (median GDT_TS в пределах нескольких единиц).» Specific GDT_TS numbers not provided; protein-only vs ligand-binding accuracy difference not quantified; only «несколько единиц» vague.
- **§2.6 Aurora — operational reasons ECMWF doesn't deploy** — line 490 mentions «data assimilation» как один компонент но technical detail на 2 предложениях; conservation laws violation mentioned «нарушаются» без quantification.
- **§2.7 AlphaProof Lean tactics** — line 501 «генерирует доказательство как последовательность tactic'ов Lean» — без example tactic'а или example proof structure.

**Why P1:** Chapter позиционируется как «academic textbook chapter + Q&A backup + self-study reference». Aspirants reading it for self-study need **deeper technical exposition**. AlphaFold/Boltz/Aurora — each is multi-paper deep dive opportunity; current draft = surface-level summaries.

**Recommendation:** Phase 4 brief — expand §2 technical depth (~1 500-2 000 words across §2.1/2.3/2.6/2.7):
- §2.1: walk through evoformer architecture (high-level), structure module, recycle process
- §2.3: actual benchmark numbers Boltz vs AF3 на protein-only + ligand-binding subset
- §2.6: data assimilation specifics + conservation law specifics (one example each)
- §2.7: example Lean tactic or one example completed AlphaProof problem

---

### P1-CHAPTER-5: §6 Замыкание (closing) underdelivered — pledge + reflection prompt compressed

**Severity:** P1 (related to P0-CHAPTER-2)

**Evidence:**
- Plan target 1 800 words; actual 767 (43% short)
- **Pledge** (5 commitments) present, но per-pledge только 1-2 sentences — no example scenario per pledge to anchor commitment.
- **Reflection prompt** «найдите 30 минут для следующего exercise» — 6 шагов на one bullet каждый; intent was deeper exercise prompt с baseline questions per step.
- **Мост к Лекции 16** — 4 bullets in raw list form. Plan intent: full paragraph foreshadowing + 2-3 specific analogies lec-15↔lec-16. Currently 3 analogies listed but each gets only 5-10 words.

**Recommendation:** Phase 4 brief — expand §6 к ~1 800 слов:
- Per-pledge anchor scenario: 1-2 sentence example of what the pledge looks like в practice.
- Reflection prompt: each of 6 steps expanded к 2-3 sentence guide.
- Mост к Лекции 16: full 200-word paragraph linking keystone «лестница цикла» к нефтегазовому контексту + 3 specific analogies с explanation.

---

### P1-CHAPTER-6: §5.6 Russian context — pedagogical takeaway pattern + thin failures discussion

**Severity:** P1 (Russian context section is ~1500 words vs intended ~2000; «pedagogical takeaway» violates rule)

**Evidence:**
- §5.6 word count ~1 500 vs plan target ~2 000-2 500 для 5-minute coverage
- Three cases (AIRI / Sber / Yandex) all receive ~250-300 words each — superficial relative к plan brief
- **Failure / limit** sub-bullets per case present но 1-2 sentence each — no depth on actual constraints
- **Compute gap** discussion mentions «~$1M+ compute estimated» one para — without specific contrast к international compute access
- **Citation visibility** mentions «Russian-language papers under-represented in Semantic Scholar» но без quantification (% missing, examples)
- **«Pedagogical takeaway.»** label at line 251 (one of 6 P1 instances above)

**Recommendation:** Expand §5.6 к ~2 200 слов:
- Per case (AIRI/Sber/Yandex): +200 words each — specific recent publications, specific datasets used, specific limitations
- Compute gap: quantify with comparison к DeepMind/Google compute available
- Citation visibility: data point on Russian paper coverage в major LLM training corpora
- Strip «Pedagogical takeaway.» label per P1-CHAPTER-3

---

### P1-CHAPTER-7: Q&A backup — 18 questions vs plan target 15; check answer depth

**Severity:** P1 (count overshoot и answer depth varied)

**Evidence:**
- Plan-v2 brief specified «15 questions backup»; chapter delivered Q1-Q15 + bonus Q16-Q18 = **18 questions**
- Answers vary 50-180 words. Q1-Q15 within plan band (~50-100 words). Bonus Q16-Q18 longer (Q17 ~150 words, Q18 ~160 words).
- Q6 «Что делать если рецензент использует LLM для review?» — answer thin (~70 words), does not address ICMJE specifics or specific journal policies (Frontiers/Springer/Elsevier prohibit list).
- Q9 «Closed-world vs open-world категорическое разделение?» — answer ~90 words, but spectrum claim needs 1-2 concrete intermediate examples.
- Q10 «Aurora 5000× ECMWF» — answer good but final sentence «as augmentation, not replacement classical IFS» — could specify percentage of forecast volume served by AIFS in 2026.

**Recommendation:** Phase 4:
- Either limit к 15 (remove bonus Q16-Q18) OR document explicit «3 bonus questions для systematic literature review tooling» extension в brief.
- Tighten Q6 with ICMJE rule reference; Q9 add 1-2 intermediate examples; Q10 add operational deployment estimate.

---

### P1-CHAPTER-8: Cross-lecture references (Лекция 13 / Лекция 14) — accurate but lack analogy explanation

**Severity:** P1

**Evidence:**
- Line 112 (chapter.md §0.1): «**Лекции 13 и 14 представили лестницы как структурный приём**…» — useful framing but very brief
- Differentiation table lec-13 vs lec-14 vs lec-15 (Cyclical / Sequential) — promised in plan но **not in chapter** (only mentioned 1 sentence на line 143 «В Лекции 13 «лестница среды» — пять уровней… была sequential»)
- Plan v2 explicitly required «6-dim differentiation table» — chapter does not include table

**Recommendation:** Phase 4 — add explicit 3×6 comparison table:
- Rows: lec-13 / lec-14 / lec-15
- Cols: дисциплина / уровней / тип движения (sequential vs cyclical) / диагностический вопрос / failure pattern / verification approach
- Place в §0.3 keystone introduction (после description лестницы)

---

### P1-CHAPTER-9: References (~120 entries) — chapter has только ~50 entries listed

**Severity:** P1 (frontmatter declares `references_count: ~120`, actual is ~50 inline + ~10 institutional + ~6 RU = ~66 distinct references visible в Источники section)

**Evidence:**
- chapter-part3.md:391-466 References section:
  - Primary papers — Foundation models: 10 entries
  - Primary papers — Autonomous labs: 4 entries
  - Primary papers — Analyse-phase: 5 entries
  - Primary papers — Hallucinations: 4 entries
  - Press references: 6 entries
  - Institutional documents: 6 entries
  - Russian context: 6 entries
  - Further reading: 7 entries
  - **Total: ~48 entries**
- Plan v2 brief: «~120 entries broken down 80 primary + 20 press + 10 institutional + 10 Russian»
- Many inline cited authors in body не listed в References (e.g., Akdel et al. 2024 referenced inline но в References list as «arxiv 2510.15939»; Häse et al. 2020 / Shields et al. 2021 не listed)
- Frontmatter `references_count: ~120` therefore **inflated by 2.4×**

**Recommendation:** Phase 4:
- Either expand References к claimed ~120 (preferable for academic depth)
- OR update frontmatter `references_count: ~50` (honest reporting)
- Audit: каждая inline citation должна appear в References list
- Особенно RU context references — 6 entries thin для «5 минут RU coverage»; expand к 12-15 references

---

### P1-CHAPTER-10: §1.2 Sakana cherry-pick 3% acceptance rate calculation — internally inconsistent

**Severity:** P1 (number-anchor verification — minor inconsistency)

**Evidence:**
- chapter.md:233 «3%, что ниже среднего acceptance rate ICLR 2024 (24.52%)»
- chapter-part3.md:362 Q12 «1/100 = 1% true success rate»
- **Inconsistency:** 3/100 = 3% (cited в chapter) vs 1/100 = 1% (cited в Q12)
- Plan v2 numbers convention lock #15: «Sakana 1/3 6.33 + cherry-pick 100→3»
- Surface-level: 3 of 100 generated → submitted; of those, **1 passed peer review** = «1/3 prepared peer review» from marketing
- True success rate from systems perspective: 1 / 100 generated = 1% (per Q12)
- Marketing claim: «1 of 3 papers accepted» = 33% (misleading framing)
- Chapter §1.2 conflates: «3%» (= 3 of 100 SELECTED, not 3 of 100 ACCEPTED)

**Recommendation:** Phase 4 — disambiguate:
- 3 of 100 generated = «human filter rate» (selection layer)
- 1 of 3 = «peer-review acceptance among selected» (33% — comparable к ICLR workshop ~50%)
- 1 of 100 generated = **true autonomous science rate** (1%)
- Plan v2 numbers convention lock should clarify which 3 figures are canonical

---

### P1-CHAPTER-11: Inline `[VFY-day-of]` markers present, но claims marked are mixed in importance

**Severity:** P1

**Evidence (VFY markers found):**
- chapter.md:170 FrontierMath 52.4% [VFY-day-of] ✓
- chapter.md:260 Co-Scientist Nature May 2026 [VFY-day-of] ✓
- chapter.md:392 AlphaFold DB 200M+ [VFY-day-of] ✓
- chapter.md:484 ECMWF AIFS [VFY-day-of] ✓
- chapter.md:486 Hurricane Milton Aurora extreme weather [VFY: needs primary source confirmation; if not confirmed, generalize…] ✓ (conditional fallback specified)
- chapter.md:507 FrontierMath dynamics 2024-2026 [VFY-day-of] (duplicate marker context) ✓
- chapter-part2.md:212 NotebookLM 17M+ MAU [VFY-day-of] ✓
- chapter-part2.md:233 Elicit 4× literature time [VFY] ✓
- chapter-part3.md:413 Co-Scientist (Nature May 2026) [VFY-day-of] ✓

**Issues:**
- **9 VFY markers present** (good)
- **Missing VFY на:**
  - GPT-5.5 Pro reference (model name not confirmed for May 2026 release — should be `GPT-5.5 [VFY-day-of model name]`)
  - Boltz-2 (2025) — release timing
  - Some specific dates not verifiable as of writing (Sakana v2 «April 2025» — present но без VFY marker)
- One marker uses informal `[VFY]` instead of `[VFY-day-of]` (chapter-part2.md:233)

**Recommendation:** Phase 4 — add VFY markers to:
- GPT-5.5 Pro reference (`GPT-5.5 Pro [VFY-day-of model name]`)
- Boltz-2 release date если non-canonical
- Standardize all `[VFY]` → `[VFY-day-of]` for consistency

---

## P2 findings (nice-to-fix)

### P2-CHAPTER-1: Frontmatter `length_words: ~30000` inflated (actual 28 604)

**Severity:** P2

**Evidence:**
- chapter.md:12 `length_words: ~30000` declares ~30k
- Actual sum 28 604 = -4.7% from claimed 30k
- Plan target was 30k, frontmatter declares ~30k, actual is below floor of «target ±5%»

**Recommendation:** Either expand к 30k (preferred per P0-CHAPTER-2) OR update frontmatter `length_words: ~28600`.

---

### P2-CHAPTER-2: Slide-marker s15 gap unexplained

**Severity:** P2

**Evidence:**
- Chapter slide markers found: s01-s14, s16-s31, s32-s39 (38 unique markers)
- **s15 marker missing** — gap in §2 between s14 (AlphaFold 3 / Boltz) and s16 (GNoME + A-Lab)
- Plan-v2 deck:39 slides — but only 38 [for-slide-sXX] anchors

**Recommendation:** Either (a) book-editor add `[for-slide-s15]` anchor to §2.4 Boltz extension OR §2.3 closing discussion; OR (b) plan-v2 ToC verify whether s15 is in fact a section divider needing no chapter anchor.

---

### P2-CHAPTER-3: Some Cyrillic typos / mixed language artifacts

**Severity:** P2

**Evidence:**
- chapter.md:247 «**medienно**» — German/garbled word (should be «медленно»)
- chapter.md:204 «реcomбинировать» — Russian + Latin mix (should be «рекомбинировать»)
- chapter.md:445 «opаsным» — Cyrillic + Latin (should be «опасным»)
- chapter-part2.md:280 «vereft» — typo (should be «verify»)
- chapter-part2.md:316 «**Реastantance**», «**Pertentage**» (intentional? as AI-generated nonsense example — OK if intentional but unclear in context)
- chapter-part3.md:241 «нaкbind» — mixed (should be «накопленный» / «накапливающийся»)

**Recommendation:** Phase 4 cleanup pass — fix typos. Many are mixed-language artifacts which will resolve through P0-CHAPTER-1 Russification rewrite anyway.

---

### P2-CHAPTER-4: Self-check questions per section — consistent but could include LO-tagging

**Severity:** P2

**Evidence:**
- Self-check questions present after Введение / §1 / §2 / §3 / §4 / §5 (6 sets, 3-4 questions each = ~22 questions)
- Questions don't specify which LO they assess (would help future Q&A backup mapping)
- Some questions Yes/No-able (e.g., «AlphaProof достиг серебра — это AI решил математику?») — but answers should reference framework

**Recommendation:** Phase 4 nice-to-have — tag each self-check question with relevant LO (e.g., «1. [LO6] Объясните, почему cherry-picking…»). Not blocking; could be Phase 5 polish.

---

## Cross-cutting issues

### LO coverage analysis

| LO | Chapter section coverage | Bloom level | Assessment |
|---|---|---|---|
| **LO4** (Знание + Применять — классы инструментов) | §1.4 industrial suites + §3.6 alternatives + §4.2 literature tools + §5.2 5 alternatives + Q&A Q16 specific tool recommendation | Помнить + Применять | **Strong**. Каждый «класс» AI tool разобран. |
| **LO5** (Этика) | §4.6 ICMJE rules / §4.4 Frontiers / §4.5 NeurIPS / §5.1 Critique D ethical risk / §5.6 RU regulatory | Оценивать | **Strong**. 3+ ethical risks explicit. |
| **LO6** (Central — лестница + augmentation/HITL/vetoed) | §0.3 keystone introduction / each section returns to ступень / §1-4 explicit augmentation classifications / §5.1 4-category criteria | Анализировать + Оценивать | **Strong — central LO covered systematically** |
| **LO8** (Применять + создавать — выбрать AI tool, предложить alternative) | WE-1 §1.5 grant idea / WE-2 §4.3 bibliography / WE-TESS §3.7 / WE-3 §5.3 catalyst pipeline / §5.4 3 vendor questions / §5.5 5-step framework | Применять + Создавать | **Strong — 4 walked examples with verification chain** |

**Verdict:** All 4 LOs adequately covered with appropriate Bloom levels. **No LO gap.** Chapter pedagogically delivers central learning outcome.

### Cognitive load hotspots

1. **§0 Введение 2 232 слов** — overlong для introduction (target 1 200, actual 86% over). Risk of cognitive overload before keystone introduced. Mitigation: §0.4 Glossary (15 terms) cleanly compartmentalised; §0.2 Hook narratively grounded; §0.3 keystone clear. Borderline acceptable but could trim.
2. **§4 Write+Review 4 799 слов** — failure-heavy zone; chapter explicitly acknowledges «failure-bucket ~70% слов». Risk of bleak emotional tone overwhelming student. Mitigation: NotebookLM/Elicit «augmentation OK» framings interleaved; section closes с positive measures (Elicit 4× speed, NotebookLM 50+ sources/hour).
3. **§5.6 RU context** — 4 sub-sections × 4 cases × 3 limits + 5 takeaway points в single 1 500-word section. High info density per word. Risk: feels like a list rather than narrative. Mitigation: Phase 4 expansion will help.

### Sequence breaks

- **AI-failure prevalence per section:** §0 (50%) → §1 (60%) → §2 (40%) → §3 (35%) → §4 (70%) → §5 (70%) → §6 (50%). §3 dip к 35% borderline acceptable (analyse-phase IS positive); §1 60% intentional (Sakana failure focus); §2 40% peak Nobel success + critique balance.
- **Cyclical keystone reinforcement** present at end of each section через self-check questions referencing «на какой ступени лестницы».
- **No major sequence break.** Cognitive load manageable.

### Tone drifts

- **Russification failure (P0-1) drives major tone drift:** narrative reads as English-Russian code-switching. This is the dominant tone problem.
- **«We», «Мы», «вы» voice consistent** with «вы» being respectful student-facing voice. No «УГАДАЙ» / «ребят» / «короче» — formal voice maintained.
- **No magical-pill framing:** chapter centrally argues «AI requires judgment»; AlphaFold success balanced by Galactica failure throughout.
- **Pedagogical labels (P1-3) create occasional meta-tone drift** — when narrative breaks into «Pedagogical insight.» mode, it loses textbook narrative voice.

---

## Self-reported metrics verification

| Metric | Producer self-report | My measurement | Verdict |
|---|---|---|---|
| Total words | ~30 000 (frontmatter) | 28 604 | Producer **inflated by 4.7%** |
| AI-Failure strict-in % | 45.9% | 54.6% holistic | Producer **underreported**; actual higher (Phase 2 critique was 45.9% **plan target**; book-editor exceeded) |
| References count | ~120 | ~48-50 visible | Producer **overstated by ~2.4×** |
| Multi-part split | 3 files, ≤600 lines each | 534 / 406 / 471 lines | ✓ Pass |
| Slide map | 39 slides s01-s39 | 38 anchors found (s15 missing) | ✓ Pass borderline; s15 gap |
| Cornerstones lock | 12 terms canonical | 12 verified inline | ✓ Pass |
| Numbers convention | 25 anchors | 8/8 spot-checked correct | ✓ Pass |
| Failure-share holistic | ≥30% per section | min 35% / weighted 54.6% | ✓ Pass |
| 0 named universities | Asserted | 0 grep hits | ✓ Pass |

**Number anchors spot-check (8/8 pass):**
- ✓ A-Lab 41 of 58 за 17 дней — canonical 6× (lines 81, 437, 439, 446, 524, 347 part3)
- ✓ Palgrave 35 of 36 — canonical 4× (lines 82, 458, 461, 525)
- ✓ Nobel 9 октября 2024 — verified (line 121)
- ✓ Coscientist GPT-4 + Claude both — verified (lines 256, 335 part3, 410 part3)
- ✓ AlphaFold IDP 22% — verified (line 375)
- ✓ NeurIPS 100+ fake / 53 papers / 24.52% — verified (line 323 part2, line 233 part2 для 24.52%)
- ✓ FrontierMath 52.4% — verified с VFY (line 170, line 507)
- ✓ Allen MICrONS 1 mm³ / 84K neurons / 500M synapses / 4 km axons — verified (line 80 part2)

**Conclusion на self-reported metrics:** producer mostly accurate on quality content; **inflated на word count** (claim ~30k vs 28.6k) and **References count** (claim ~120 vs ~50). These are accountable to Phase 4 fix.

---

## Top 5 правок (приоритизированные)

### 1. P0-CHAPTER-1 — Deep Russification rewrite narrative body (~6-8 hours)
- Strip 485 critical anglicism instances (production / pipeline / workflow / verification / review / ML / baseline / etc.)
- Rewrite 906 mixed-language sentences to RU-narrative + whitelisted technical terms
- Apply explicit 30-term blacklist with canonical RU substitutions
- Whitelist 12 cornerstones + brand names + acronyms-with-gloss
- Sanity-check: re-run deep latin token scan, target = 0 critical-blacklist hits in narrative body
- **Cost-of-omission:** Owner manual rewrite каждой лекции (memory [[russification]]); per L8 production ~3h wasted

### 2. P0-CHAPTER-2 — Per-section depth expansion (~3-4 hours)
- §2 Experiment +2 500 words (deepen AlphaFold transformer / Boltz technical / Aurora data assimilation / AlphaProof Lean detail)
- §6 Замыкание +1 000 words (per-pledge anchor / reflection prompt deeper / мост к Лекции 16 expanded)
- §5.6 RU context +700 words (per-case detail + compute gap quantification + citation visibility data)
- §1/§3/§4 ~+500 words each (deeper alternative comparisons, expanded counter-claims)
- Total expansion: ~5 200 words → narrative к 32 955 (still split 3 files ≤600 lines)
- **Target:** every section ±10% of plan-v2 budget; no section <80% of plan; total narrative ~30 500-31 500

### 3. P1-CHAPTER-3 — Strip all 6 «Pedagogical» labels (~30 minutes)
- chapter.md:163 / 306; part2.md:184, 289; part3.md:241, 251 — rewrite each as direct chapter prose without meta-label
- Phase 4 brief explicit: «zero pedagogical/methodological meta-labels in body»
- Pre-USER-GATE A grep on rendered chapter mandatory: `(методическ|педагогическ|pedagogical)` = 0 hits

### 4. P1-CHAPTER-8 + 9 — Cross-lecture differentiation table + References expansion (~1 hour)
- Add 3×6 differentiation table lec-13/lec-14/lec-15 in §0.3 keystone introduction
- Expand References from ~50 к ~120 (verify каждая inline citation appears; добавить missing Häse 2020 / Shields 2021 / etc.)
- Update frontmatter `references_count: ~120` (or honest ~50 if not expanded)

### 5. P1-CHAPTER-10 + P2-CHAPTER-3 — Sakana 3% vs 1% disambiguation + typo cleanup (~30 minutes)
- Sakana §1.2: disambiguate 3 of 100 (selection rate) vs 1 of 100 (autonomous-science rate) vs 1 of 3 (peer-review-passed-of-submitted)
- Numbers convention lock entry: clarify 3 canonical values
- Typo fixes: medienно → медленно, реcomбинировать → рекомбинировать, opаsным → опасным, vereft → verify, нaкbind → накапливающийся

**Total Phase 4 estimated cost:** ~11-14 hours (one book-editor + 1 fact-checker minor consultation)
**Phase 4 verification gate:** re-run methodology-critic + pre-USER-GATE walkthrough

---

## Verdict justification (final)

**REVISE** (not APPROVE-WITH-POLISH) because:

1. **2 P0 issues:** Russification structural failure + systematic per-section depth shortfall — both require book-editor revision pass, не USER-GATE-A polish.
2. **9 P1 issues > 5 threshold:** counter-check triggers REVISE per CLAUDE.md.
3. **Pedagogical content is strong;** LO coverage is strong; number anchors verified; failure-share holistic > 30% pass. **Chapter v1 is on the right substantive trajectory** but Russification + depth gaps prevent USER GATE A acceptance.
4. **Phase 4 revision well-scoped:** ~12 hours focused effort by single book-editor agent. After Phase 4 → re-critique → expected APPROVE-WITH-POLISH or APPROVE-CLEAN.

**Not REJECT** because:
- Substantive content is methodologically valid и aligned с plan-v2
- Cornerstones cyclically reinforced
- Walked examples deliver applicable framework
- 0 named-university violations
- Failure-share holistic ≥30% met
- Multi-part structure clean, cross-links intact, slide markers ~complete

After Phase 4 revision addressing P0+P1, chapter should converge к APPROVE level и unblock USER GATE A.
