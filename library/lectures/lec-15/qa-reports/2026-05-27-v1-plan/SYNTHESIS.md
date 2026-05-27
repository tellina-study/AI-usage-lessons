# Phase 1 Critique Synthesis — Лекция 15 plan-v1

**Date:** 2026-05-27.
**Verdict combined:** **REVISE** (methodology P0×2 + fact-checker P0×2 = blocking; reader/orchestrator nominal APPROVE-WITH-POLISH).
**Total P0:** 4. **Total P1:** 14 (deduplicated). **Total P2:** 17.

---

## Verdicts по критикам

| Critic | Verdict | P0 | P1 | P2 |
|---|---|---|---|---|
| methodology-critic | REVISE | 2 | 7 | 6 |
| reader-text-only | APPROVE-WITH-POLISH | 0 | 5 | 4 |
| fact-checker | REVISE | 2 | 4 | 6 |
| orchestrator-roast | APPROVE-WITH-POLISH | 0 | 3 | 6 |
| **Combined** | **REVISE** | **4** | **14** | **17** (after dedup) |

---

## P0 issues — MUST FIX до Phase 2 chapter draft

### P0-1 (methodology) — Worked-examples crisis
Plan claims «6 worked examples», но фактически **1 applicable** worked example (s34 catalyst pipeline). 5 — case studies. LO8 «Применять и создавать» не покрывается.
**Fix:** (a) reframe self-check claim «3 applicable + 4 case studies»; (b) добавить ≥2 applicable walked examples — §1 «grant idea decision tree», §4 «coллaboratorov bibliography verification»; (c) expand s25 «спектральные сигналы» с 1 предложения до 150-word walked example; (d) fill s34 catalyst (propylene oxidation specific) **в плане**, не в Phase 2 brief.

### P0-2 (methodology) — Keystone Variant A differentiation underaddressed
R2 mitigation поверхностный — Лестница цикла отличается от lec-13 «среда» и lec-14 «автономия» только визуально, не operationally.
**Fix:** (a) добавить в plan **side-by-side таблицу 6 dimensions: lec-13 vs lec-14 vs lec-15**; (b) **lock keystone choice в Phase 1**, не defer-to-Phase-2; (c) если choice Variant A — consider rename «Лестница» → «Сцены научного цикла» / «Стадии» / «Фазы» (термин «лестница» уже занят); (d) рассмотреть Variant B (closed/open-world) для cleaner differentiation. **Owner-decision request в plan-approval gate.**

### P0-3 (fact-checker) — A-Lab Berkeley «36 of 57 in 17 days» wrong
Actual Nature Szymanski et al. Nov 2023: **41 of 58 in 17 days**. Cascade в 4+ plan locations.
**Fix:** replace «36 of 57» → «41 of 58» во ВСЕХ местах плана; добавить в Numbers convention lock как #6 (canonical) + Phase 2 brief explicit «cascade-check 41/58 везде».

### P0-4 (fact-checker) — Allen MICrONS conflation
Plan conflates 3 separate efforts:
- MICrONS Apr 2025: 84K neurons + 500M synapses + 4km axons в 1 mm³ visual cortex.
- Brain Knowledge Platform 2025: 34M brain cell datasets.
- ChatGPT-like AI + 1,300 mouse brain regions: Oct 2025 UCSF+Allen separate project.
**Fix:** distinguish 3 efforts в s21; либо drop conflated framing; либо pick ONE (MICrONS Apr 2025 как primary, остальные опционально mentioned).

---

## P1 issues — SHOULD FIX (boost plan-v2 quality, не отдельный re-critique)

### Structural (methodology + reader + orchestrator overlap)
- **P1-1 (methodology):** §2 strict-in 23% per-section — не санкционировано CLAUDE.md (правило про артефакты, не sections), но pedagogically thin. Fix: inline failure callbacks в s12 (IDP) / s18 (Aurora extreme weather miss) / s19 (AlphaProof time-cost) → boost §2 strict-in до ~35%.
- **P1-2 (methodology):** Cognitive overload §4 + §5 = 24 мин failure-heavy подряд. Fix: insert capability beacons (s33 alternatives как success story «proven 30+ years»; s37 recap с positive markers «AlphaFold 200M structures, Aurora 5000× speed, IMO silver»).
- **P1-3 (methodology + orchestrator):** Hero side-by-side risk — split attention dilutes hook. **Owner-decision required.** Single hero AlphaFold ribbon ИЛИ Nobel ceremony альтернатива.
- **P1-4 (methodology):** Phase 2 chapter brief = 350 слов; needed 600+. Fix: expand с (a) section word budgets per all 7 sections; (b) 12-15 Q&A backup questions; (c) 10-12 cornerstones lock list; (d) references breakdown; (e) cross-reference policy; (f) multi-part split boundaries.
- **P1-5 (methodology):** s25 spectra worked example — pedagogically слабый (decision prompt, не walked). Fix: replace с domain-honest worked, e.g., «TESS transit search 1000 hours; CNN vs Bayesian Optimization vs classical» walked decision tree.
- **P1-6 (reader):** §2 terminology overload — 15-20 новых названий за 15 мин. Fix: expand s04 glossary с 6-8 → 12-15 terms (CASP, IDP, DFT/MD, BO+GP, ECMWF, FrontierMath, ICMJE, closed/open-world).
- **P1-7 (reader):** §4 rebalance 1.5+8.5 → 3+7.5 (positive ground для NotebookLM/Elicit/Consensus).
- **P1-8 (reader):** Coscientist (CMU 2023) vs Co-Scientist (DeepMind 2026) — two products, same name. Fix: explicit disambiguation в s07-s09 + glossary.

### Factual (fact-checker)
- **P1-9 (fact-checker):** Nobel Chemistry 2024 date — 8 октября → **9 октября**.
- **P1-10 (fact-checker):** Palgrave framing — examined **36 success samples, found 35/36 errors** (not «41 novel → derivatives»).
- **P1-11 (fact-checker):** Coscientist «GPT-4-driven» → **GPT-4 + Claude both** (Nature 2023 primary).
- **P1-12 (fact-checker):** ECMWF «4 weather models operational с 2026» — likely overstatement. ECMWF runs own **AIFS**; Aurora/GraphCast/Pangu/FourCastNet — benchmarks not deployments. **Verify before chapter Phase 2.**

### Volatility / freshness (orchestrator + methodology)
- **P1-13 (methodology):** Volatile claims без inline `[VFY-day-of]` markers в outline (FrontierMath, AlphaFold DB, Co-Scientist, NotebookLM MAU). Fix: inline в plan где numbers появляются.
- **P1-14 (orchestrator + reader):** Co-Scientist Nature May 2026 — **9 days до даты**. Downgrade primary case → secondary mention; primary Hypothesis-level = Sakana failures.

---

## P2 issues — NICE TO FIX

### Reader + orchestrator
- §3 unifying mental model intro («"Analyse" — это AI-augmented data science»).
- Worked example 2 (AlphaProof) — brief explain «Lean» (formal proof language).
- s10 + s30 merge consideration (Sakana mentioned twice).
- Allen MICrONS / replication crisis brief context.

### Methodology
- Russification table 22 → расширить с backbone/scaffold/binding affinity/zero-shot etc.
- Sakana «cherry-pick» mechanics explicit — Sakana writes ~100 papers per cycle; human curator selects 3 to submit.
- Lec-16 bridge «closed-world domain» — soften «частично closed-world».
- Galactica 3-day dates — verify (some sources say 2 days).
- «Сколтех Centers of Excellence» = named institution; rename «отечественные центры компетенций».
- Раздел 0 numbering vs «Введение» (lec-14 pattern).
- Section dividers explicit в plan (lec-13/14 имели; lec-15 не explicit).

### Fact-checker freshness markers (P2 — already в plan `[VFY-day-of]` list)
- FrontierMath leaderboard, AlphaFold DB count, NotebookLM MAU, NeurIPS exact citations count.

### Orchestrator
- Russification table extension (45+ anglicisms expected в full chapter).
- Numbers gaps (AlphaFold 2 CASP14 GDT_TS, Insilico ISM001-055 trial size, Aurora 1.3B parameters, Coscientig tool-call counts).
- §2 inline IDP callback (P1-1 cross-link).

---

## OWNER DECISIONS REQUIRED в plan-approval gate

### Decision #1 — Keystone choice
- **Variant A** «Лестница / Сцены научного цикла» 6 phases (рекомендация после revision): возможный rename из «Лестница» → «Сцены» / «Стадии» / «Фазы» для cleaner differentiation от lec-13/14.
- **Variant B** «closed-world vs open-world»: cleaner differentiation, но термин в логике (CWA) — может потребовать RU rename.
- **Variant C** «Discovery × Validation × Production triple»: fallback.

### Decision #2 — Hero pattern s01
- **Side-by-side** «две стороны медали» (AlphaFold Nobel + Galactica retraction) — novel, риск split attention.
- **Single hero AlphaFold ribbon / Nobel ceremony**, Galactica callback на s02 — safer, follows lec-14 pattern.

### Decision #3 — Co-Scientist (Nature May 2026) treatment
- **Primary mention** (s07 dedicated, risk if retracted к лекции).
- **Secondary** (one-liner inline, `[VFY-day-of]`).

### Decision #4 — Russian context depth
- РНФ (whitelisted) + AI Russia 2030 Strategy. Без «Сколтех» (named). ~3 мин в §5.

---

## Path to APPROVE (plan-v2 acceptance)

1. **plan-v2 produced** с all P0 (4) + P1 (14) fixes baked in.
2. **Owner approves** 4 decisions в plan-approval gate.
3. **Re-spawn focused critics** на plan-v2 (methodology only, scope = «P0/P1 fixes verified + new owner decisions integrated»). Не full re-critique.
4. **Phase 2 chapter brief** built из plan-v2 + owner decisions.

---

## Storage

`/tmp/lec-15-wt/library/lectures/lec-15/qa-reports/2026-05-27-v1-plan/SYNTHESIS.md`

**End of synthesis.**
