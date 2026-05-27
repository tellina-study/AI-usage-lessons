# Phase 3 Chapter v1.0 Critique Synthesis

**Date:** 2026-05-27.
**Combined Verdict:** **REVISE** (methodology driven; fact + reader APPROVE-WITH-POLISH).
**Total P0:** 4. **Total P1:** 18 (deduplicated). **Total P2:** 15+.

---

## Verdicts по критикам

| Critic | Verdict | P0 | P1 | P2 |
|---|---|---|---|---|
| methodology-critic | REVISE | 2 | 9 | 4 |
| fact-checker | APPROVE-WITH-POLISH | 2 | 7 | 10+ |
| reader-text-only | APPROVE-WITH-POLISH | 0 | 9 | 5 |
| **Combined** | **REVISE** | **4** | **18** | **15+** |

---

## P0 issues — BLOCKING до USER GATE A

### P0-1 — Russification failure (methodology)
**485 critical anglicism hits** в narrative body (per-file: 113/228/144). 906 mixed-language sentences с ≥4 Latin words. Examples из chapter:
- «(a) **default к open-source** unless есть сильная причина для closed; (b) **проверьте, активна ли open community** (GitHub stars, recent commits, разнообразие contributors)» — 23 Latin words.
- «Применимы в **scientific logistics** (clinical trial design — minimizing patient enrollment time под constraints)» — 27 Latin words.

**Top offenders:** verification 64×, review 93×, ML 51×, baseline 30×, workflow 27×, accuracy 27×, ground truth 26×, pipeline 21×, structural 20×, training data 18×, deployment 18×.

**Cost-of-omission:** lec-08 имел 919 unique latin tokens → owner reject «провал» → 3h cycle.

**Fix:** deep Russification rewrite через 3 файла; explicit 30-term blacklist + 12 cornerstones + brand whitelist; pre-submission deep latin scan target = 0 critical hits.

### P0-2 — Systematic per-section depth shortfall (methodology)
28 604 слов = +104 over 28 500 floor, но **-1 396 под 30k center**. **Все 7 sections under plan-v2 budget:**

| Section | Plan target | Actual | Delta |
|---|---|---|---|
| §2 Experiment | 7 500 | **5 012** | **-33%** CRITICAL |
| §6 Замыкание | 1 800 | **767** | **-57%** CRITICAL |
| §5 Когда AI не нужен | 5 000 | 3 979 | -20% |
| §1 Hypothesis+Design | 4 500 | 3 986 | -11% |
| §3 Analyse | 4 500 | 3 994 | -11% |
| §4 Write+Review | 5 500 | 4 799 | -13% |
| §0 Введение | 1 200 | 2 232 | +86% (over) |

**Fix:** +5 200 слов distributed:
- §2: +2 500 (AlphaFold transformer / Boltz benchmarks / Aurora data assimilation / AlphaProof Lean detail)
- §6: +1 000 (per-pledge anchor + reflection prompt + lec-16 bridge expanded)
- §5.6: +700 (per-case detail + compute gap quantification + citation visibility data)
- §1/§3/§4: ~+500 each
- **Target narrative:** 30 500-31 000 слов (deck-target met с margin)

### P0-3 — NeurIPS 2025 numbers wrong (fact-checker)
- Plan/chapter: «15 000 submissions / ~3 700 accepted»
- Actual: **21 575 submissions / 5 290 accepted** (24.52% acceptance rate stays correct)
- Cascade: §4.5 line 323 + §1.2 line 233 (also incorrectly attributes 24.52% к «ICLR 2024» вместо «NeurIPS 2025»)
- Numbers convention lock #11 — update

### P0-4 — Russia decree wrong (fact-checker)
- Plan/chapter: «Указ Президента РФ № 145»
- Actual: **№490 (October 2019)**, updated by **№124 (February 2024)** — нет такого decree №145
- Affects §5.6 RU context line 221 + Q&A Q15 line 374
- **Fact-fabrication; damages credibility с RU audience**

---

## P1 issues — should fix

### Methodology (9):
- **P1-3** «Pedagogical» labels cascade (6 instances): chapter.md:163, 306; part2.md:184, 289; part3.md:241, 251 — strip всех, rewrite как direct prose
- **P1-4** §2 technical depth shallow — AlphaFold transformer architecture 1 para, Boltz benchmarks vague, Aurora data assimilation 2 sentences, AlphaProof Lean без example tactic
- **P1-5** §6 Замыкание underdelivered — pledge 5 lines, reflection 6 bullets, lec-16 bridge 3 bullets
- **P1-6** §5.6 RU context superficial — cases 250-300 слов each, compute gap unquantified
- **P1-7** Q&A 18 vs target 15 — Q16-Q18 bonus OK или trim
- **P1-8** Differentiation table lec-13/14/15 missing в chapter (был обещан в plan-v2)
- **P1-9** References 50 vs claimed ~120 — frontmatter inflated 2.4×
- **P1-10** Sakana 3% vs 1% disambiguation — chapter §1.2 says 3%, Q12 says 1%; need clarify 3 canonical: 3/100 selection / 1/3 peer-review-pass / 1/100 autonomous-rate
- **P1-11** VFY markers — добавить на GPT-5.5 Pro, Boltz-2; standardize `[VFY]` → `[VFY-day-of]`

### Fact-checker (7):
- **P1-12** Akdel et al. citation conflated — chapter cites «Akdel et al., Nature Methods 2024, arxiv 2510.15939»; actual = Nature Structural & Molecular Biology 2022; arxiv 2510.15939 is separate 2025 paper
- **P1-13** LIGO arxiv 2504.17587 — authors actually Ashton/Malz/Colombo (not «LIGO-VIRGO Collaboration»); year 2025 (not 2024)
- **P1-14** Insitro $150M wrong — actual Series C $400M (2021)
- **P1-15** Reproducibility Project 36% — primary source = 39 of 100 studies
- **P1-16** AlphaFold 2 baseline GDT_TS «~60» — more accurate ~75 average; ~60 only on hardest FM targets
- **P1-17** ECMWF AIFS «operational с 2024» — actually Feb 25, 2025
- **P1-18** Hurricane Milton + Aurora pairing — no primary source; generalize OR find source

### Reader (9):
- **P1-19** Russification — 30-50 high-frequency offenders (workflow / pipeline / deploy / mainstream / benchmark / inference / performance / adoption / insight / tradeoff) — overlaps с P0-1
- **P1-20** §3.5 IDP deep-dive redundancy с §2.1 — start §3.5 с «we discussed... here deep-dive» + technical detail
- **P1-21** §5.6 RU context structure overloaded (5 subsections in one) — split or compact
- **P1-22** WE-3 chemistry-heavy — gloss VASP / Quantum ESPRESSO / BET surface area OR replace с universal example
- **P1-23** Lean / proof assistant — 1 sentence gloss в §2.7
- **P1-24** MSA / homology modeling / ab initio folding — 2-3 sentence brief в §2.1
- **P1-25** Acquisition function / Expected Improvement / UCB — 1 sentence в §1.6
- **P1-26** Conformal prediction vs classical CI — 1 sentence distinguishing в §3.4
- **P1-27** Glossary §0.4 — convert numbered list → table

---

## P2 issues — nice to fix

- Frontmatter `length_words: ~30000` inflated → align к actual или expand
- Slide-marker s15 missing
- Typos: medienно / реcomбинировать / opаsным / vereft / нaкbind
- §3.3 параллельные проекты one-liner — drop or table
- §4.6 ICMJE compress ~1200 → ~700-800
- §5.6 add concrete publication per case (AIRI Nature Communications 2024 etc.)
- WE-1 add inline Минобрнауки приказы balance
- Q&A Q19 (AlphaFold low pLDDT IDP region)
- Self-check questions LO-tagging
- References quality audit (BoTorch / Ax / GROBID gloss)

---

## Path to USER GATE A

1. **Phase 4 — single comprehensive book-editor revision** (~10-14h estimated):
   - Deep Russification rewrite (6-8h)
   - Per-section depth expansion (+5 200 слов, 3-4h)
   - Fact P0/P1 fixes (~1h)
   - Pedagogical labels strip + structural improvements (~1h)
   - Multi-part split re-check (≤600 lines each)
2. **Phase 4.5 — focused critic re-spawn** (methodology + fact-checker only; reader optional):
   - Verify P0/P1 closure; expect APPROVE-WITH-POLISH
3. **Phase 4.7 — Pre-USER-GATE A walkthrough** (orchestrator-independent grep):
   - Russification deep latin scan — target 0 critical hits в narrative body
   - Pedagogical labels grep — target 0
   - Numbers cascade-check spot 5-7
   - Anonymization grep — target 0 named universities
4. **USER GATE A** — present к owner

**Storage:** `/tmp/lec-15-wt/library/lectures/lec-15/qa-reports/2026-05-27-v1-chapter/SYNTHESIS.md`

**Owner notification recommended:** REVISE verdict, ~10-14h Phase 4 estimated. Hardest single task — Russification rewrite (485 hits) which directly addresses owner's repeatedly-flagged pain point.
