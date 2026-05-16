# Phase 3 Synthesis — Chapter v1 Critique → Revision Brief for Chapter v2

**Date:** 2026-05-13
**Inputs:**
- `methodology-critic.md` — REVISE (0 P0 + 7 P1 + 11 P2)
- `reader-text-only.md` — APPROVE-WITH-POLISH (0 P0 + 11 P1 + 9 P2)
- `fact-checker.md` — REVISE (2 P0 + 6 P1 + 9 P2)

**Consolidated verdict: REVISE** (2 critics REVISE). Chapter has strong bones — central question lands, LO coverage explicit, mosmed retraction exemplary, §2.2 math + §5.2 Obermeyer + §5.5 4-actor are best sections. Revision is targeted, not from-scratch.

---

## P0 — MUST fix in chapter v2 (fact-checker only)

| # | Section | Claim (v1) | Correct value | Notes |
|---|---|---|---|---|
| 1 | §3.3 | Rentosertib placebo FVC **−62.3 мл** | **−20.3 мл** | Verified via PubMed 40461817. Chapter exaggerates placebo decline by ~3× → inflates treatment effect ~40 mL. **Also fix sources.md §1.3** (propagated error). |
| 2 | §5.2 | Obermeyer 17.5% → 46.5% Black patients served post-fix | **17.7%** → 46.5% | Verbatim mis-citation. **Also fix sources.md §9.1** (propagated). |

Both are factual primary-source errors in **flagship cases** (Rentosertib = success case; Obermeyer = bias deep-dive). MUST fix.

---

## P1 — should fix in chapter v2 (consolidated, de-duplicated across critics)

### Structural / methodological

| # | Section | Issue | Critic(s) | Fix |
|---|---|---|---|---|
| 1 | Throughout (27 occurrences) | `[for-slide-sXX]` markers contaminate source-of-truth artifact (Лекция 1 chapter = 0 markers) | methodology + reader | Strip all 27 markers. Optional: store mapping в `library/lectures/lec-04/slide-bindings.yaml`. |
| 2 | §6.2 | «Следующая лекция — AI в производстве» — Лекция 5 = **Коллоквиум 1**; AI в производстве = Лекция 6 | methodology | Restructure: «Следующее занятие — Коллоквиум 1 (Лекция 5). После — Лекция 6 "AI в производстве и сельском хозяйстве" с Cognitive Agro Pilot». |
| 3 | §4.2 | «на Лекции 9 будет Практикум 1» — Практикум 1 = **Лекция 7**; Лекция 9 = лекция «Этика и регулирование» | methodology | Replace: «на Лекции 7 будет Практикум 1 ("Анализ индустриальных кейсов с помощью AI"), а на Лекции 12 — Практикум 2». |
| 4 | §6.3 | LO8 «summative-уровень (Evaluate/Create)» — creates premature synthesis impression; chapter enumerates 3 principles right after | methodology | Rewrite §6.3 line 642: «LO8 требует Evaluate-уровень мышления... финал на Лекции 9 + 14. Принципы ниже — сырьё, не финал». Rename «принципы» → **«наблюдения»** before numbered list. |
| 5 | §5.5 / §6.3 | §5.5 enumerates 5 practices, §6.3 says «три принципа» — hedge «3 (или 5)» confuses | methodology | Make §5.5 enumerate same 3 as §6.3 (combine: 1=Transparency+Calibration; 2=Validation set/population — currently missing in §5.5, add it; 3=Audit-trail+Post-market monitoring). OR change §6.3 to «5 принципов» and renumber. |
| 6 | LO8 narrative thread | «LO8 / Лекция 9 / вход для черновика» repeated 6+ times — feels propaganda-like, reader feels «told this is important» | reader | Consolidate LO8 framing in §6.3 only with 1 brief callback in §5.5; drop redundant mentions in §0.3, §Введение, §3.5, §5.1. |
| 7 | §1 self-check Q3 | «Объясните, почему "4 млрд руб/год" не упоминается» — meta-question, не LO1 Apply | methodology | Replace с: «Сравните scale FDA-списка (1 451) и mosmed.ai (14M исследований / 70 сервисов на 43 области): что эти числа измеряют по-разному, и почему их нельзя напрямую сравнивать?». |
| 8 | §3.2 | AlphaFold «2M+ researchers» dropped while citing Insilico's «18 months» self-disclosure — inconsistent epistemic standard | methodology | Either include 2M с caveat-pattern («DeepMind заявляет 2M+; источник Nobel speech 2024; verifiable alternative — 200M structures»). OR state methodological rule in §3 intro. |

### Reader-friction (text-only critic)

| # | Section | Issue | Fix |
|---|---|---|---|
| 9 | §3.1 | 12-15 medical terms (TNIK, IPF, ADMET, hit, lead) introduced before defined; «терминологический минимум» at end instead of beginning | Move term box к началу §3 (после §3.1 intro paragraph). |
| 10 | §3.3 | RU acronym soup (AIDD, AIRI, MADD, DiMA, CD137, BHRF1); **same trio «Сбер+AIRI+Р-Фарм»** appears in 2 consecutive bullets for 2 DIFFERENT alliances (онкология CD137 / Альцгеймер) | Restructure 2 bullets: explicit «Alliance #1 (May 2024, CD137 oncology): Сбер + AIRI + Р-Фарм» and «Alliance #2 (November 2025, Alzheimer): AIRI + Р-Фарм + Сбер». Make distinction clear. |
| 11 | §3.5 | Wall of 10+ dates/law numbers in 3 paragraphs | Convert к tabular: 3 columns (FDA / EU AI Act / Росздравнадзор) × 4 rows (regulator / date / scope / key principle). |
| 12 | §5.3 | Visible `[FACT-CHECK: GigaChat/YandexGPT]` tag в reader-facing text — leaks editorial workflow | Remove tag; rewrite to plain prose: «Конкретные тексты политик следует проверить непосредственно в документации GigaChat и YandexGPT». |
| 13 | §2.2 | Self-check #1 (PPV calculation) lacks inline formula — student scrolls back | Add inline PPV formula в Self-check Q1 itself: `PPV = TP/(TP+FP) = sens·prev / (sens·prev + (1−spec)·(1−prev))`. |
| 14 | §2.2 LaTeX | $$...$$ blocks work в GitHub/VSCode (MathJax post-2022) but break в plain viewers | Keep LaTeX для main definitions + add ASCII fallback inline: e.g., `Sens = TP/(TP+FN)` plain text after LaTeX block. |

### Fact-checker P1 refinements

| # | Section | Issue | Fix |
|---|---|---|---|
| 15 | §3.3 | Rentosertib AE «14.8% diarrhea, 14.8% liver» — missing denominator label (across which arm?) | Add: «14.8% в 60mg QD arm (n=24)» per Nature Medicine table. |
| 16 | §2.3 | Goh JAMA — missing sample size n=50; median rounding inconsistency (76.3% vs 76 median) | Add n=50; standardize to «median diagnostic accuracy 76% GPT-4 alone vs 74% docs-with-GPT-4». |
| 17 | §3.5 | EU AI Act framing ambiguity — Aug 2026 = Annex III **non-MDR**; **Aug 2027 covers most medical AI (MDR-regulated)** | Add clarifying clause: «Annex III high-risk не-MDR — 2 августа 2026; MDR-regulated medical AI (большинство клинических устройств) — 2 августа 2027». |
| 18 | §2.3 | MASAI ratio 1.29 без confidence interval | Add CI: «1.29 (95% CI 1.16-1.44)» per Lancet 2024. |
| 19 | §2.2 | CheXNet sens 0.96/spec 0.93 — paper headline numbers vary by subgroup | Hedge: «AUC ~0.96 для pneumonia subset (Rajpurkar 2017); конкретные sens/spec depend on threshold + pathology». |

---

## P2 — apply where compatible (consolidated ~30 items, condensed)

**Typos / wording:**
- §3.3 «Каваэт» (caveat transliteration) → «оговорка» OR «caveat» italicized
- §1.1 «geomic» → «genomic»; «persona-driven» → «patient-specific»
- §5.3 «лозу 1–2 фунта» → «терять 1–2 фунта»
- §3.2 pLDDT undefined first use — add brief gloss

**Structure:**
- §0.2 «почти никто не поднимет» — rephrase для chapter-mode (reader alone, не in-class)
- §0.3 duplicates §Введение 4-block map — cut §Введение last paragraph
- §1.3 «три причины» но content has 4 (EU AI Act deadline = implicit 4th) — clarify
- §3.1 / §3.4 «marginally helps» vs «не имеет отношения к attrition» — harmonize to «AI ассистирует workflow, не влияет на attrition rate»
- §3.3 «российский Rentosertib некорректно» — strawman — rephrase: «Сравнение RF preclinical vs Insilico Phase IIa нельзя описать как "российский Rentosertib"»
- §5.5 «final clinical responsibility undivided» — callout treatment (blockquote)

**Cross-refs:**
- §6.3: full title Лекция 9 «AI, этика и регулирование: кто отвечает за AI?» (subtitle = central question Лекции 4) — explicit curriculum bridge
- §6.2 Cognitive Agro Pilot teaser — embed в P1-2 fix (Лекция 6, не Лекция 5)

**Compression (target -260 слов → ~12,240):**
- §5.3 Case 3 (patient self-diagnosis) — consolidate to 60-80 слов (drop threefold statistic restate)
- §3.5 ФЗ-152/ФЗ-23 duplicate of §5.4 — drop in §3.5
- §5.4 Sweeney 1997 — compress к 1 sentence (drop year detail)
- §5.1 — duplicates section headings уже в TOC — cut к 1 paragraph

**Sources block:**
- Propagate −62.3 → −20.3 fix to references
- Propagate 17.5% → 17.7% fix to references

---

## What to KEEP (strong points — do not disturb)

1. **§1.2 mosmed «4 млрд руб» retraction** — methodologically excellent teachable moment. Keep verbatim.
2. **§2.2 Self-check Q1** — strongest Apply question (numerical PPV calculation). Replicate pattern.
3. **§2.2 inline LaTeX** — works in GitHub/VSCode preview; keep + add ASCII fallback inline.
4. **§3.3 RU drug discovery «honest comparison» framing** — neither boosterism nor dismissal. Model for future RU sections.
5. **§5.2 Obermeyer engineer-takeaway** — «выбор метрики = выбор политики» — strongest engineering aha-moment per reader.
6. **§5.5 4-actor framework** — Analyze-level deliverable promised by LO3.
7. **§6.3 LO8 framing — 90% there.** P1-4 + P1-5 + P1-6 fixes complete it.
8. **Sources block 62 refs grouped by section** — industry-grade. Only need P0 propagation.

---

## Priority order for Phase 4 revision (book-editor)

1. **P0 (mandatory, 5 min):** Fix Rentosertib −62.3 → −20.3 (§3.3 + sources.md §1.3); Obermeyer 17.5 → 17.7 (§5.2 + sources.md §9.1).
2. **P1 fabricated cross-refs (5 min):** §6.2 Лекция 5/6 + Коллоквиум 1; §4.2 Лекция 7 (Практикум 1).
3. **P1 strip markers (5 min):** all 27 `[for-slide-sXX]` annotations + visible `[FACT-CHECK]` tag in §5.3.
4. **P1 LO8 framing (15 min):** §6.3 rewrite + rename «принципы» → «наблюдения»; consolidate LO8 thread из 6+ mentions to 2-3.
5. **P1 §5.5 / §6.3 5-vs-3 (10 min):** unify to 3 same principles or 5 throughout.
6. **P1 RU acronym clarity §3.3 (10 min):** explicit Alliance #1 / Alliance #2 labels.
7. **P1 §3.5 regulation table (15 min):** 3 jurisdictions × 4 attributes.
8. **P1 §3.1 medical terms (5 min):** move term box к началу §3.
9. **P1 self-check Q3 (5 min):** replace meta-question с FDA/mosmed scale comparison.
10. **P1 fact-check refinements (20 min):** Rentosertib AE denominator, Goh n=50, EU AI Act 2026/2027, MASAI CI, CheXNet hedge.
11. **P2 batch (15 min):** typos, callouts, compression −260 слов.
12. **AlphaFold 2M epistemic consistency (5 min):** caveat pattern OR §3 intro methodological rule.
13. **P2 propagation:** sources.md fix.

**Total estimated revision time: ~2 hours wall-clock.**

---

## Hand-off to revision agent

Agent: **book-editor** (revision pass on chapter.md).
Output: `library/lectures/lec-04/chapter.md` (overwrite v1; do NOT save v2 separately — chapter is single canonical artifact per pipeline).
Length target: **11,500-12,500 слов** (compression -260 слов applied).

After revision: pre-USER-GATE walkthrough → USER GATE A.
