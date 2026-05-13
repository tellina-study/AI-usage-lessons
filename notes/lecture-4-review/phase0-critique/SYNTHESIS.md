# Phase 0b Synthesis — Plan-v1 Critique → Revision Brief for plan-v2

**Date:** 2026-05-13
**Inputs:**
- `notes/lecture-4-review/phase0-critique/methodology-critic.md` (REVISE, 2 P0 + 9 P1 + 12 P2)
- `notes/lecture-4-review/phase0-critique/reader-text-only.md` (APPROVE-WITH-POLISH, 2 P0 + 7 P1 + 5 P2)
- `notes/lecture-4-review/phase0-critique/fact-checker.md` (REVISE, 3 P0 + 14 P1 + 4 P2)
- `notes/research/lecture-4/sources.md` (research ground truth, 82 sources)
- `notes/lecture-4-review/plan-v1.md` (the plan being revised)

**Consolidated verdict: REVISE** (2 critics REVISE, 1 APPROVE-WITH-POLISH). Plan has strong bones (central question, arc, frame matrix, glossary, illustration briefs per slide). Revision is targeted, not from-scratch.

---

## P0 — must fix in plan-v2 (consolidated, de-duplicated)

| # | Issue | Slides | Critic source | Fix |
|---|---|---|---|---|
| 1 | **DSP-1181 narrative imbalance** — discontinued drug as flagship, missing peer-reviewed Insilico Rentosertib (Nature Med June 2025, Phase 2a positive IPF readout — +98.4 mL FVC vs −62.3 mL placebo, n=71) | s17 (3.5 min) | methodology + fact-checker | Restructure §3 drug discovery: split s17 into **s17a Rentosertib (success case, 2.5 min)** + **s17b DSP-1181 (reality check, 2.5 min)**. Total section 14 → still 14 min (merge s18+s25 per P1 saves time). Update central question payoff narrative. |
| 2 | **LO8 unilaterally added** — course program maps LO8 to Lec 9+14 only; Lec 4 LO list (per program) = LO1+LO2+LO3 + LO4 (micro-exercise) | header + s5, s8, s18, s23-25, s27, s28 | methodology | **Option B (preferred):** Keep LO8 framing but explicitly tag as «input for Lec 9 checklist draft». s28 teaser mentions «эти 3 принципа responsibility — input для черновика Lec 9». Add **LO4** to header (course-doc requires it for s19 micro-exercise). Re-tag s24/s25 primary LO as LO3-deep + LO8-preparatory. |
| 3 | **mosmed.ai «4 млрд руб/год» unverified** — cited in s5, s8, s12, s26 без proper caveat | s5, s8, s12, s26 | fact-checker (methodology P1-2) | Remove «4 млрд руб/год» everywhere. Replace with **verified operational metrics:** «>14 млн исследований за 5 лет, 2000+ организаций, 74 региона, 18+ млн изображений, 70 AI-сервисов, 11 национальных стандартов» (per sources.md §2.2). |
| 4 | **FDA device count outdated** — plan-v1 cites «1016 to Aug 2024 + projection 1300-1500», verified actual is **1,451 cumulative end-2025** | s4, s7 | fact-checker | Replace with «**1,451 cumulative end-2025** (258 new в 2024 + 295 new в 2025)». Bar chart endpoints: 2024 cumulative 1,193; 2025 cumulative 1,451. Day-of-lecture re-fetch flagged для лектора. |
| 5 | **s18 (FDA PCCP) — missing pre/post contrast** — reader can't understand WHY innovation | s18 | reader-text-only | Add one sentence: «До PCCP — каждое обновление требовало new full submission в FDA (12-18 мес). С PCCP — vendor pre-declares допустимые updates → может обновлять без re-submission». |
| 6 | **s17 timeline overloaded** — DSP-1181 efficacy + Exscientia CEO firing + Recursion merger competing for attention; second story doesn't serve main message | s17 | reader-text-only | Remove Exscientia 2025 turbulence (CEO firing, Recursion merger) from visible content. Speaker notes only if relevant. Keep timeline до 2022 discontinuation + insight «AI ускорил design, эффективность — отдельная задача». |

---

## P1 — should fix in plan-v2 (consolidated)

| # | Issue | Slides | Source | Fix |
|---|---|---|---|---|
| 1 | **LO4 missing from header** — course doc explicit «LO4 — Применить AI web-chat» for Lec 4 | header + s19 | methodology | Add LO4 to header. s19 LO mapping: «LO4 CORE + LO2 + LO3». |
| 2 | **Regulatory overload s18+s25** (4.5 min dense regulatory content) | s18, s25 | methodology + reader | **Option A:** Merge s18+s25 → single «Регулирование 3-jurisdictions short» (2 min). Drop ГОСТ specifics, EU AI Act timeline. Save 2.5 min → redirect to s17 expansion + s19 (10 min per course doc) + s22 expansion. |
| 3 | **Goh JAMA Oct 2024 augmentation gap missing** — s11 framing «AI+врач > each alone» — defensible for imaging (MASAI) but contradicted for clinical reasoning (Goh) | s11 | methodology | Refine assertion: «Для imaging — AI+врач > каждый alone (MASAI RCT 2024-2025). Для clinical reasoning — augmentation gap: врач+AI ≈ врач alone (Goh JAMA Oct 2024).» Add 3-row comparison: Liu 2019 / MASAI 2024-2025 / Goh 2024. |
| 4 | **MASAI Sweden RCT missing entirely** — strongest peer-reviewed AI mammography evidence | s10, s11 | fact-checker | Add to s11 evidence row: MASAI 2024-2025 (sensitivity 80.5% AI vs 73.8% standard radiologist; 44% workload reduction; 12% interval cancer reduction). Lancet 2024+2025. |
| 5 | **LLM coverage thin** — pattern CORE = 1 slide; anti-pattern CORE = 2 slides | s22 | methodology | Expand s22 to 4 min covering 3 cases: NEDA Tessa + adversarial hallucination 83% rate (Communications Medicine 2025) + 40M Americans use ChatGPT for healthcare (OpenAI/Gallup 2024-2025). |
| 6 | **Schema readability constraints not explicit per slide** | s10, s17, s24 | methodology | Add explicit subtype rules to slide-level entries. s17: split timeline OR reduce to 3 events (2020 entry, 2022 discontinue, 2024 merger). s24: actor cards «1-word role + 1-line responsibility» max. s10: add prevalence/PPV row (per reader P1-2 — 4 metrics not 2). |
| 7 | **Glossary lock for «AI-диагностика»** — high drift risk без canonical form pre-lock | glossary candidates | methodology | Pre-lock «AI-диагностика» = canonical RU form; «CADe» = FDA-specific subset; «AI medical imaging» = English research form. Add aliases_forbidden + aliases_allowed map. |
| 8 | **s1 hook decision: SELECTED, not PROPOSED** | s1 | methodology | Pick **AlphaFold-server (alphafoldserver.com)** — public, 30-sec query, 3D structure visual impact. Backup PNG always shown if internet fails. Decision-tree in speaker notes. Update Точки выбора table → SELECTED. |
| 9 | **s19 micro-exercise: 8 min compresses course-doc 10 min; output unclear** | s19 | methodology + reader | Extend to 10 min (course-doc compliance). Concrete output: «Открой web-chat → задай готовый промпт → отметь карандашом 1 неточность ИЛИ 1 unverifiable claim ИЛИ 1 место где объяснение слишком абстрактное. На reveal — 2-3 студента читают (1 min each)». Fallback: pre-printed 3-5 sample AI responses (3 EN + 2 RU). |
| 10 | **s15 pharma jargon hit/lead undefined** for non-medic | s15 speaker notes | reader | Add to speaker notes: «Hit = молекула, у которой есть начальный signal активности vs target. Lead = hit, доведённый до preclinical-readiness (улучшенная affinity, selectivity, stability)». |
| 11 | **s10 missing prevalence/PPV intuition** — students will think «94% = good» | s10 | reader | Add 4th metric row: prevalence + PPV. Speaker notes: «Sens/spec не зависят от prevalence; PPV — зависит. При prev=1%, sens=0.94, spec=0.89 → PPV ~8%.» |
| 12 | **s6 4-type matrix axes ad-hoc** | s6 | reader | Justify axes in speaker notes: «modality важна = определяет ML stack (CV vs NLP vs generative chemistry); scope важна = определяет regulatory pathway (single patient = device, population = analytics)». OR linear list instead of matrix. |
| 13 | **s13 vs s21 bias repetition** (Obermeyer cited twice) | s13, s21 | reader | **Option:** на s13 — drop Obermeyer; keep dermatology + pulse-oximeter only. On s21 — exclusive deep-dive Obermeyer (mechanism + actionable engineer lesson). |
| 14 | **s23 Change Healthcare weak AI connection** + outdated $2-3B figure | s23 | reader + fact-checker | (a) Strengthen AI connection in visible content: «Medical AI training datasets inherit medical-data security risk; mosmed.ai has 18M+ images — what if dataset exfiltrated?». (b) Use precise figure: **$2.457 млрд** (UHG Q3 2024). |
| 15 | **NEDA Tessa dates wrong** — Tessa wasn't launched May 31 2023; was running for months before Cass modified rule-based → generative without NEDA approval; suspended **May 30 2023** (not June 2) | s22 | fact-checker | Update timeline: «**~2018-2022:** Tessa runs as rule-based chatbot. **March 2023:** Cass (vendor) silently switches to generative LLM without NEDA knowledge. **May 30, 2023:** Sharon Maxwell screenshots harmful weight-loss advice; NEDA suspends Tessa within 24h.» Frame as **vendor accountability story**, not chatbot story. |
| 16 | **mosmed sens/spec 0.94/0.89 fabricated** | s10 | fact-checker | Replace with verified numbers: **CheXNet pneumonia (Rajpurkar 2017): sens 0.96, spec 0.93** OR **MASAI mammography (2024-2025): sens 80.5% AI vs 73.8% radiologist**. |
| 17 | **AI market size «$50+ млрд» inflated** | s5 | fact-checker | Replace with «десятки миллиардов долларов (Markets and Markets / Towards Healthcare 2025, $22-38B range — methodology-dependent)». |
| 18 | **s25 3-jurisdiction too dense** | s25 | reader | (subsumed by P1-2 merge — drop ГОСТ specifics, drop EU AI Act timeline). |

---

## P2 — apply if room (consolidated 21 items, condensed list)

- s2 cover 0.5 min → 0.1 min, redistribute 0.4 min to s19
- s4 «1,451 устройств» actual not «1300-1500 проекция»
- s6 «text/molecule» counter-intuitive — clarify в notes (molecules = SMILES strings)
- s7 «11% кардиология» → use «остальное — кардиология/неврология/другие» без specific %
- s15 «Clinical I/II/III» — speaker note expand «3 phases, ~7-10 лет, different attrition»
- s17 Exscientia CEO firing — drop (P0-6 already)
- s23 «Russian ransomware» — speaker note script: «tech-criminal orgs don't respect borders; healthcare AI built anywhere must defend against any threat»
- s26 takeaway #2 Нобель 2024 — add Baker (computational protein design) alongside Hassabis+Jumper
- Glossary candidate #24 «Хосзу-роль» → replace «Healthcare operator role»
- s28 «Cognitive Agro Pilot 1500+ машин, +30-40%» — verify exact phrasing per course doc
- §Сводка arithmetic fix: 9+7+14+14+8+14+6 = 72, claim says 68 — fix
- s14 mid-callback — add pause beat between s13 (bias) → s14 (mosmed callback)
- s3 + s4 poll length verify
- «mat-применение» → «применение математики» (or similar non-jargon)
- Russian context patchy outside mosmed — add 1-2 explicit mentions
- s22 dates correction subsumed by P1-15
- Fact-checker freshness watchlist: 4 items for day-of-lecture re-verification (FDA count, Insilico Rentosertib news, mosmed operational stats, Recursion Q2 2026 readouts)

---

## What to KEEP (strong points — do not disturb in revision)

1. **Central question + 4 explicit returns + emotional payoff** (s12, s14, s17, s24-25, s27).
2. **6-frame mapping table** at end — clean matrix, useful for downstream agents.
3. **Glossary candidates 25 terms upfront** — proactive Glossary Lock prep.
4. **Russian context explicit** at multiple slides — strong adherence to user spec.
5. **Speaker notes hints per slide** — book-editor-ready hand-off.
6. **Pre-USER-GATE walkthrough checklist embedded** — addresses L1 reflection root cause.
7. **Точки выбора table** explicitly marking PROPOSED vs SELECTED — methodological discipline. (Convert remaining PROPOSED → SELECTED in plan-v2.)
8. **Trust-but-verify tone** declared in §Tone — should now be more defensible after P0-1 (Rentosertib success + DSP-1181 reality check).

---

## Recommended slide structure changes (summary)

| Original | Revised | Change |
|---|---|---|
| s17 (3.5 min DSP-1181 only) | s17a Rentosertib (2.5) + s17b DSP-1181 (2.5) = 5 min | Split — add Rentosertib success case |
| s18 (FDA PCCP, 2.5) | s18 condensed (2 min) | Add pre/post contrast; trim |
| s25 (3-juris, 2) | merge into s18 OR drop | Save 2 min |
| s19 (micro-exercise, 8) | s19 (10 min, concrete output) | Course-doc compliance |
| s22 (NEDA Tessa, 3) | s22 (4 min, 3 LLM anti-pattern cases) | Expand LLM coverage |
| s11 (AI vs radiologist, 3) | s11 (3 min — split imaging vs reasoning) | Add Goh JAMA + MASAI |
| s10 (sens/spec 2 metrics) | s10 (4 metrics — add prevalence/PPV) | Reader P1-2 fix |
| s13 (3 bias cards) | s13 (2 cards — drop Obermeyer here) | Reader P1-5 dedup |
| s21 (Obermeyer deep) | s21 (exclusive Obermeyer focus) | Reader P1-5 dedup |
| LO8 added | LO8 framed as «input for Lec 9» + LO4 added | Methodology P0-2 + P1-1 |

**Time math check post-revision:**
- Original arc: 9+7+14+14+8+14+6 = 72 → actual ~68 min content + 7 buffer = 75
- Revised: 9+7+14+(14+0.5 from s17 split)+10+(14−2 from s18/s25 merge)+6 = 73 content + 2 from transitions = 75 ✓

---

## Hand-off to revision agent

The revision agent should:
1. Read plan-v1 + 3 critic reports + sources.md.
2. Apply all P0 fixes (mandatory).
3. Apply all P1 fixes (strongly recommended; if conflict — defer to user at USER GATE 0 with explicit note).
4. Apply P2 fixes where compatible (do not bloat plan-v2).
5. Produce **plan-v2.md** maintaining same format as plan-v1.md (frontmatter, central question, arc table, slide-by-slide breakdown, glossary, frames matrix, notes for next phases).
6. End with **changelog v1 → v2** table (similar to plan-v5 changelog for Лекция 1).
7. Update Точки выбора table — all PROPOSED items resolved to SELECTED.
8. Pre-lock glossary canonical forms (P1-7).

**Expected length:** ~1400-1600 lines (plan-v1 was 1377; revision adds 1 slide split + changelog).
