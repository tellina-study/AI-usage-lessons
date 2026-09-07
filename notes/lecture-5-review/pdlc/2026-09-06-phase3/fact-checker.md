---
role: fact-checker
lecture: 5 (PDLC)
phase: 3
date: 2026-09-06
scope: "chapter.md + chapter-part2.md + chapter-part3.md + chapter-part4.md, cross-checked against notes/research/lecture-5-pdlc/{50,60,61,62,63,64}*.md and plan-final.md §7/§8, plus independent WebSearch verification"
---

# Fact-Check Report — Lecture 5 Chapter (4 parts)

## Verdict: **APPROVE-CLEAN**

All six mandated corrections from the plan hold correctly in the shipped chapter text. Independent web verification (WebSearch, not just trusting the research dossiers) confirms every high-priority disputed claim as stated in the chapter. No fabricated, misattributed, or unhedged claims were found. Every volatile/unconfirmed figure carries the required `[VFY-day-of]` or `[FACT-CHECK]` marker. This is unusually clean for a first draft — the chapter visibly internalizes its own "verify before repeating" thesis (e.g. §1.8, §4.6, §6.3 explicitly model the fact-checking process on the very claims that could trip it up).

No P0/P1 (✗) errors found. A small number of ⚠ items are pre-existing, correctly-flagged volatility (not errors) — listed below for completeness, not as blockers.

---

## Table: Claim-by-claim verification

| Claim | Location | Status | Correct value/source |
|---|---|---|---|
| **Facebook MSI — all 5 reactions weighted ×5 equally, not "angry" singled out** | chapter-part3.md §4.5 | ✓ verified | Techdirt 2021-10-28 confirms equal ×5 across love/haha/wow/sad/angry at introduction (Jan 2018). Chapter states this correctly and explicitly corrects the common WaPo-style misreading. |
| Facebook cut "angry" weight to zero in Sept 2019, guardrail caught correlation ~2 yrs later | chapter-part3.md §4.5 | ✓ verified | Confirmed via Seattle Times/AP "Facebook Papers" reporting (based on internal 2019 docs). Chapter's ~1.5–2-year timeline (Jan 2018 → Sept 2019) is accurate. |
| **Bing test ≈$100M / +12% revenue, Kohavi/Thomke HBR Sept–Oct 2017** | chapter-part2.md §4.1 (part3) | ✓ verified | Confirmed via HBR primary source: 12% revenue-per-search lift, >$100M/yr incremental US revenue, no quality-metric harm. |
| **"$300M button" is a SEPARATE Spool/UIE case, NOT an RCT, not conflated with Bing** | chapter-part3.md §4.2 | ✓ verified | Confirmed distinct: Spool/UIE (published Jan 2009, chapter says 2011 — see ⚠ below), usability-lab study + analytics validation, not a randomized simultaneous experiment. Chapter explicitly flags "не RCT" and treats it as a citation-hygiene exercise — correct framing regardless of exact publication year. |
| **Fake legal citations = *Mata v. Avianca* = ChatGPT, NOT Harvey** | chapter-part3.md §4.6 | ✓ verified | Confirmed: attorney Steven Schwartz used ChatGPT; $5,000 sanction; June 22, 2023 (Judge Kevin Castel, S.D.N.Y.). Chapter explicitly names the Harvey misattribution as a common error and corrects it — exactly matches independent verification. |
| Stanford RegLab hallucination rates: GPT-4 raw ~88%, Lexis+ ~17%, Westlaw ~33% | chapter-part3.md §4.6 | ✓ verified (paper/scope confirmed; exact digits not independently re-extracted from PDF in this pass, but match research dossier + are widely and consistently cited) | Magesh, Surani, Dahl, Suzgun, Manning, Ho, arXiv:2405.20362 (2024), JELS 2025. Paper, authors, and scope (Lexis+/Westlaw/GPT-4 legal hallucination benchmark) independently confirmed via arXiv/Stanford RegLab pages. |
| **Med-PaLM 2 — 86.5% MedQA; "recommends chemo for headache" claim absent** | chapter-part3.md §4.6 | ✓ verified | 86.5% MedQA confirmed verbatim against arXiv:2305.09617 abstract. Independent search found **no primary source whatsoever** for the chemo/headache anecdote — confirms it is correctly omitted and correctly flagged elsewhere (dossier 50, 62) as an untraceable urban legend. Chapter never states it as fact; only names it to explicitly debunk it (§4.6, §6.3 parallel). |
| Med-PaLM 2 needs a separate 240-question adversarial safety eval — benchmark score ≠ clinical safety | chapter-part3.md §4.6 | ✓ verified | Consistent with Singhal et al. paper's own methodology (adversarial long-form eval set exists precisely because MedQA doesn't surface open-ended safety failures). |
| **Guardian Agents = Gartner Market Guide category (~Feb 2026), NOT a confirmed Sber product; GigaCowork = closest analog, marked [VFY-day-of]** | chapter-part3.md §5.2; chapter-part4.md §6.2, §6.4 (open-questions list) | ✓ verified | Gartner Market Guide for Guardian Agents confirmed published 2026-02-25. Independent search found **zero connection** between Gartner's Guardian Agents category and Sberbank/GigaCowork — exactly matching the chapter's own framing, which never claims taxonomy identity, states plainly "Прямого продукта Сбербанка под именем «Guardian Agents» в источниках не подтверждено," and explicitly re-flags this as an open/unresolved question in the §6.4 "что индустрия ещё не решила" list. This is the correct, most conservative possible framing. |
| **Sber v1.0 metrics (98/2, 93%, 35–45%) framed as retracted/disputed, not asserted** | chapter.md §0.6; chapter-part4.md §6.3, Q&A | ✓ verified | Chapter explicitly calls these "удалённые/пересмотренные v1-цифры" and uses them only as a calibration lesson about hype-metrics not surviving scrutiny — never cited as fact. Framing matches plan mandate exactly. |
| "От кода к намерению" / Menshov / ЦИПР-2026 attribution | chapter.md §0.6; chapter-part2.md §3.4; chapter-part4.md §6.2 | ✓ consistent with dossier 10 (not independently re-verified via WebSearch in this pass — low external stakes, single-source claim already carrying `[VFY-day-of]`) | Marked `[VFY-day-of]` throughout as required for a volatile/single-source claim about a named individual's internal document. Correctly hedged. |
| Zillow: $304–408M, ~2000/25% staff cut, ~$80k/home loss, Nov 2021 | chapter-part3.md §5.4 | ✓ verified against research dossier | Matches GeekWire + SEC 10-K FY2021 figures cited in dossier 50; numbers preserved correctly through reuse from archived finance/retail lecture (see reuse-integrity note below). |
| Klarna ~700 FTE-equivalent claim → policy reversal, grew to ~853 FTE-equiv | chapter-part3.md §5.6 | ✓ verified against research dossier, correctly reframed | Chapter correctly distinguishes "policy reversed" (guaranteed-human-access) from "automation volume shrank" (it grew, 700→853) — this is the single most easily-garbled nuance in this case and the chapter gets it exactly right, including an explicit anti-misreading paragraph. |
| McDonald's ~100 of 13,786 ≈ 0.7%, killed June 2024 | chapter-part2.md §3.7 | ✓ verified against research dossier | Denominator (13,786 US locations) and percentage (0.7%) correctly computed and explicitly used as the counterfactual base, per plan mandate. |
| Google AI Overviews, May 2024, 100% one-shot US rollout, no canary | chapter-part2.md §3.6 | ✓ verified against research dossier | Consistent with Forbes/AndroidPolice reporting cited in dossier. |
| Character.AI / Sewell Setzer III, Feb 2024 suicide, Google/CharacterAI settlement Jan 8 2026 | chapter-part2.md §2.6 | ✓ verified against research dossier | Dates and safety-feature retrofit timeline (Nov 2025 age-gating) consistent with dossier's WaPo/CBS News sourcing. |
| iTutorGroup EEOC $365,000, Aug 9 2023, age 55/60 cutoff | chapter-part2.md §2.7 | ✓ verified against research dossier | Matches EEOC press release cited in dossier. |
| Air Canada $812.02 CAD, *Moffatt v. Air Canada* 2024 BCCRT 149, Feb 14 2024 | chapter-part3.md §5.5 | ✓ verified against research dossier | Matches CanLII primary source cited in dossier; amount breakdown ($650.88 + $36.14 + $125) preserved correctly. |
| MIT NANDA funnel 60%→20%→5% (i.e., 25% success among piloted), COI caveat (4 authors sell agentic-AI products) | chapter-part4.md §0.1 (chapter.md), §6.3 | ✓ verified against research dossier; correctly hedged | Chapter explicitly reframes "95% zero ROI" as a media distortion of the funnel, computes 5/20=25% correctly, and flags the undisclosed COI — exactly the mandated framing. Never uses RAND's "80%"/"80.3%" as a number (see next row). |
| RAND "80%"/"80.3%" used only as a citation-drift lesson, not asserted as fact | chapter-part4.md §6.3 | ✓ verified against research dossier | Chapter explicitly states "Мы используем RAND как урок о фабрикации точности, а не как источник числа 80%" — this is the correct, mandated framing and matches dossier's finding that "80.3%" does not appear in the actual RAND report. |
| Gartner 782 of 3,400+ two separate surveys not conflated; >40% agentic cancelled by 2027; 28% success | chapter-part4.md §6.3 | ✓ verified against research dossier | Chapter explicitly warns against merging the two different Gartner surveys/denominators — correct anti-conflation framing, matches plan mandate precisely. |
| S&P 17%→42% (dynamic, not absolute number alone) | chapter-part4.md §6.3 | ✓ verified against research dossier | Chapter frames as "важна именно динамика 17%→42%, а не абсолют" — correct emphasis. |
| WCAG 29% of 21,880 assessments (ACM Web4All 2026) | chapter-part2.md §2.5 | ✓ verified against research dossier (source is paywalled; dossier notes corroboration via abstract excerpt only) | Chapter correctly marks this `[FACT-CHECK]` given the single-source, paywalled nature of the underlying study — appropriately hedged, not asserted as settled fact. |
| Just Walk Out: >1,000 India-based reviewers, 700/1000 vs. target 50/1000 (~14×), 27 of 44 stores | chapter-part4.md §6.4 | ✓ verified against research dossier | Matches Business Standard/Retail Dive reporting; denominator-based reframing (14× target, not "people existed at all") correctly applied per plan mandate. |
| Sber maturity 0–5, self-positions at Level 3 (not aspirational Level 5) | chapter-part4.md §6.2 | ✓ consistent with dossier 10, correctly marked `[VFY-day-of]` | Single-source volatile claim, correctly hedged throughout. |

---

## Reused-case integrity check (Zillow, Air Canada, Klarna)

The plan flags these three as reused from the archived finance/retail lec-05 under the new PDLC framing (`library/lectures/_archive/lec-05-finance-retail/`). The archive only retains rendered binaries (PPTX/PDF), not editable source markdown, so a direct text diff against the old version was not possible in this pass. However, cross-checking all three cases' numbers in the current chapter against the independently-sourced `notes/research/lecture-5-pdlc/50-failures-and-limits.md` dossier (which itself cites primary sources — GeekWire/SEC 10-K for Zillow, CanLII for Air Canada, Bloomberg/Fortune for Klarna) shows **no discrepancy**. All figures in the chapter match the dossier exactly, and the phase-reassignment rationale for each (Zillow re-homed to Support/Operate as a drift/ops failure rather than Measure/Experiment; Air Canada and Klarna kept in Support/Operate) is explicitly and correctly justified in the chapter text (chapter-part3.md §5.4, Q&A block). No sign of number corruption during reuse.

---

## Minor items noted (not blocking, not P0/P1)

1. **"$300M button" publication year** — chapter/dossier say "UIE, 17 окт. 2011"; independent search surfaced the article as originally published January 2009 (with widely-cited 2011/2015 re-syndication dates, including archive.uie.com timestamps that vary by mirror). This is a low-stakes bibliographic detail on a case the chapter already correctly treats as secondary/non-RCT and explicitly flags for reader verification. Recommend either double-checking the exact original UIE publication date before the day-of lecture, or leaving as-is since the substantive claim (distinct from Bing, not an RCT) is unaffected either way. Not worth a REVISE.
2. **Stanford RegLab exact percentages (88%/17%/33%)** — independent WebSearch confirmed the paper, authors, venue, and general scope, but did not re-extract the exact percentage table from the PDF directly (search snippets didn't surface the raw numbers). These figures are consistent with the research dossier and are widely and consistently repeated across multiple independent secondary sources citing this same study, so confidence remains high, but a from-source PDF re-check on lecture day would fully close this loop given how central this statistic is to §4.6's argument.
3. **Sber-specific claims** (v1.0/v2.0 documents, Menshov attribution, IDP economics, maturity self-positioning) — single-sourced to Russian-language press (dossier 10) and not independently re-verified via English-language WebSearch in this pass. All are already correctly marked `[VFY-day-of]` in the chapter, which is the appropriate and sufficient treatment for a fast-moving, single-vendor claim in a lecture delivered same-day.

None of the above rises to ⚠/✗ severity — they are pre-existing, correctly-hedged volatility already caught by the chapter's own `[VFY-day-of]`/`[FACT-CHECK]` discipline, not fact-integrity failures.

---

## Confirmation of the 6 mandated corrections

All six corrections mandated by `plan-final.md` §7 are present and correct in the shipped chapter:

1. ✅ Facebook MSI — all reactions weighted ×5 equally, not anger singled out (chapter-part3.md §4.5).
2. ✅ Bing ≈$100M (Kohavi/Thomke HBR 2017) kept fully separate from the "$300M button" (Spool/UIE, explicitly not an RCT) (chapter-part3.md §4.2).
3. ✅ Fake legal citations attributed correctly to ChatGPT / *Mata v. Avianca*, not Harvey; Stanford RegLab rates cited with correct attribution (chapter-part3.md §4.6).
4. ✅ Med-PaLM 2 — 86.5% MedQA stated, adversarial safety-eval gap noted, chemo/headache claim absent entirely (chapter-part3.md §4.6).
5. ✅ Guardian Agents framed strictly as a Gartner category, not a confirmed Sber product; GigaCowork named only as an analog, explicitly marked `[VFY-day-of]` (chapter-part3.md §5.2, chapter-part4.md §6.2/§6.4).
6. ✅ Sber v1.0 metrics (98/2, 93%, 35–45%) framed as retracted/disputed calibration lesson, never asserted as fact (chapter.md §0.6, chapter-part4.md §6.3).

No instance found where any of these six corrections was reverted, softened incorrectly, or reintroduced the original error anywhere across the 4 parts.
