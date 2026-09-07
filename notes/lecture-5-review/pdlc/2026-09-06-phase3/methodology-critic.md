---
title: "Лекция 5 (AI-PDLC) — methodology-critic, Phase 3 (Chapter, 4 parts)"
issue: 189
phase: 3
reviewer: methodology-critic
date: 2026-09-06
---

# VERDICT: **REVISE**

Two independent structural gaps, both counter-check-mandatory per CLAUDE.md:

1. **Word count.** Honest content word count (excluding frontmatter/headings/glossary/sources/further-reading, per CLAUDE.md "что НЕ засчитывается в 30k") is **27,843 words** — below the 28,500 P0-BLOCKING floor. Even the generous count that includes glossary+sources+further-reading is 29,514 — still short of the 28,500–31,500 target band's midpoint and short of the plan's own ≥30k target.
2. **Strict-in ≥30%.** Honest independent recount (by words, full-block-only, partial→out, per Decision #78) is **28.3% holistic** — under the 30% floor — and **Part 1 (chapter.md) is only 16.1%**, a severe single-part concentration failure. The self-estimate in the frontmatter (Ч1 ~41%, holistic ~40-45%) is not supportable from the actual text; it appears to count partial/base material as in-bucket, which CLAUDE.md explicitly forbids.

Both are structural gaps per CLAUDE.md, not polish items. Neither is waivable for L5 (L4+ lecture, no waiver available for either rule).

---

## 1. Word count

| File | Lines | Body words (excl. frontmatter) | Content words (excl. glossary/sources/further-reading) |
|---|---|---|---|
| chapter.md (Ч1) | 299 | 7,536 | 7,536 |
| chapter-part2.md (Ч2) | 285 | 7,077 | 7,077 |
| chapter-part3.md (Ч3) | 308 | 8,702 | 8,702 |
| chapter-part4.md (Ч4) | 272 | 6,199 | 4,528 (excludes Глоссарий+Источники+Дальнейшее чтение = 1,673 words) |
| **TOTAL** | 1,164 | **29,514** | **27,843** |

- **Line limit:** all 4 files ≤600 lines. ✅ (max is 308, well under the cap.)
- **Word count vs rule:** CLAUDE.md § Chapter Depth Baseline explicitly excludes "Источники / bibliography (это отдельно)" from the 30k count. Applying that literally, content words = **27,843**, which is **below 28,500 → P0 BLOCKING** per the rule's own counter-check clause ("<28 500 слов для L4+ → P0 BLOCKING").
- Even under the more generous reading that folds bibliography/glossary back in (29,514), the chapter still misses the plan's own stated target of ≥30,000 (`length_words: "~31000"` in frontmatter is **not accurate** — actual is ~1,500 words short of even the loose count, ~2,150 short of the strict count).
- **Fix:** expand by ~2,200–3,200 words minimum to clear 30k under either counting convention, ideally concentrated in Part 1 (currently the thinnest part at 7,536 words and also the weakest strict-in part — see §2) and/or Part 4 (4,528 content words, thinnest of the four).

## 2. Strict-in ≥30% — honest recount (HOLISTIC + per-part, by words)

**Method:** For each phase, in-bucket = only the full failure block (case + numeric baseline + root-cause tied to that phase + explicit lesson + criterion "when NOT AI-first" + alternative) **plus** any adjacent explicit "Когда здесь НЕ AI-first" paragraph belonging to that phase's AI-limits section. Base material, AI-capability material, "what remains from classic" material, and synthesis paragraphs are **out** even when excellent, per Decision #78 (partial→out). This matches the plan's own methodology (`plan-final.md` §5) but the plan's chapter self-estimate (Ч1~41%/Ч2~43%/Ч3~45%/Ч4~40%) could not be reproduced from the actual text — likely double-counting base/limits paragraphs as in-bucket.

| Part | File | Content words | In-bucket words | In-bucket % | Verdict |
|---|---|---|---|---|---|
| Ч1 | chapter.md | 7,536 | 1,215 (wnaif §1.6: 124 + Provал#1 §1.7: 572 + Provал#2 §1.8: 519) | **16.1%** | **FAIL — severe** |
| Ч2 | chapter-part2.md | 7,077 | 2,217 (wnaif×2: 94+92 + Provал#3: 542 + #4: 493 + #5: 485 + #6: 511) | **31.3%** | PASS (barely) |
| Ч3 | chapter-part3.md | 8,702 | 3,066 (wnaif×2: 113+92 + Provал#7: 678 + #8: 675 + #9: 355 + #10: 440 + #11: 713) | **35.2%** | PASS |
| Ч4 | chapter-part4.md (content-only) | 4,528 | 1,393 (Provал#12: 942 + Provал#13: 451, criterion+alternative already inline) | **30.8%** | PASS (barely) |
| **TOTAL** | | **27,843** | **7,891** | **28.3%** | **FAIL (holistic <30%)** |

**Both counter-check triggers fire simultaneously:**
- Holistic total (28.3%) is below the 30% floor.
- Distribution is **not holistic**: Part 1 at 16.1% is roughly half the required floor and less than half of Part 3's 35.2% — a textbook "concentrated in fewer artifacts" pattern at the part level, which CLAUDE.md's counter-check explicitly calls out ("доля сконцентрирована в одном артефакте → verdict REVISE").

**Why Part 1 is so far under:** Part 1 covers §0 (keystone, ~2,500 words — necessarily 0% in-bucket, it's the axis, not a failure) plus Раздел 1 (Discovery). Раздел 1's base material (Customer Development, Mom Test, JTBD, continuous discovery, qual/quant, sample bias — §1.1–1.4) and AI-capability material (§1.5) are unusually long and rich (good content, wrong bucket for this metric) relative to the two failure blocks (§1.7, §1.8), which are of normal length (~520–570 words each, comparable to failures in other parts). The imbalance is structural: §0 keystone material inflates the denominator for Part 1 specifically (no other part carries a ~2,500-word non-failure-eligible keystone section), while the numerator (2 failures) is the same count as other parts.

**Target reminder:** the plan mandates chapter target ≥40% (not just ≥30%) — "chapter target ≥40% (каждая фаза: провал ≥600 слов + блок «когда НЕ AI-first» ≥80 слов)". By that stricter internal target, **all four parts fail** except Ч3 borderline; only Ч2 and Ч4 clear even the lower 30% floor, and only barely.

**Fix options (do not implement — orchestrator/book-editor decision):**
- Add one more on-point, fully-worked failure to Раздел 1 (Discovery currently has only 2 of the lecture's 13 failures, same count as Design/Build, but Раздел 1 carries the extra ~2,500-word keystone overhead that those other parts don't) — OR
- Shorten §0 keystone exposition (currently very thorough, arguably over-built relative to its role as scene-setting) — OR
- Deepen §1.7/§1.8 with additional numeric baseline/mechanism detail to lift them past 600–700 words each (they are already reasonably deep; diminishing returns) — OR
- Move some §0 material to Part 4 (§6.5 keystone payoff) framing, shortening Part 1's non-failure share.
Recommend a combination: trim §0.5/§0.6 by ~300-400 words (the Sber intent-loop illustration in §0.6 is good material but could be tightened) and add a third short on-point moment to Раздел 1 or deepen the existing two — whichever the book-editor judges cheaper without diluting the discovery pedagogy.

## 3. Structure compliance (base → AI → limits+what-to-keep → on-point failure)

| Section | Base | Base-2 | AI capabilities | AI limits + what remains | Failure(s) | Verdict |
|---|---|---|---|---|---|---|
| §0 Keystone | n/a (this is the axis, not a phase) | — | — | — | — (hook parodox only, correctly not counted as strict-in) | N/A, correctly structured as axis |
| Раздел 1 Discovery | §1.1 Customer Dev | §1.2 Mom Test + §1.3 falsifiable hyp. + §1.4 qual/quant | §1.5 | §1.6 | §1.7 (#1), §1.8 (#2) | ✅ full compliance |
| Раздел 2 Design | §2.1 Double Diamond | §2.2 Nielsen + design systems + §2.3 fidelity/usability-test | §2.4 | §2.5 | §2.6 (#3), §2.7 (#4) | ✅ full compliance |
| Раздел 3 Build/Launch | §3.1 MVP/BML | §3.2 release mechanics | §3.3 + §3.4 | §3.5 | §3.6 (#5), §3.7 (#6) | ✅ full compliance |
| Раздел 4 Measure | §4.1 controlled experiment/OEC | §4.2 pitfalls | §4.3 evals | §4.4 Goodhart | §4.5 (#7), §4.6 (#8) | ✅ full compliance, plus §4.7 synthesis (good addition, not required but strengthens LO1) |
| Раздел 5 Support/Operate | §5.1 SRE | (folded into §5.1) | §5.2 LLMOps/AgentOps | §5.3 silent drift | §5.4 (#9), §5.5 (#10), §5.6 (#11, dual-case + 3rd inline example) | ✅ full compliance, plus §5.7 synthesis |
| Раздел 6 Governance | §6.1 portfolio governance | (folded into §6.1) | §6.2 operating model | (folded into §6.2, "облегчённый" per plan design) | §6.3 (#12), §6.4 (#13) | ✅ compliant — plan explicitly designs Governance as a "lightened" capstone round (macro-payoff + keystone), and this is executed as designed, not a gap |

No section is missing a classical base. No failure reads as off-topic for its phase (Zillow correctly re-homed to Support per plan's own fix; McDonald's/Character.AI/iTutorGroup contrasts are correctly paired). This axis of the review is clean — **structure is the chapter's strongest dimension**.

## 4. Keystone

- §0.4 (PDCA/Deming, OODA/Boyd, BML/Ries — "three independent inventions of the same loop") and §0.5 (cost/trust asymmetry + meta-pattern "every phase has a classic discipline AI doesn't delete") are both established in §0, before Раздел 1 begins. ✅ satisfies the ENFORCED keystone-axis rule (established before first phase-dive, not a mid-lecture surprise or a defensive recap).
- Each phase explicitly ties back: Раздел 1 opens referencing the loop's first arrow; §3.3 explicitly invokes "прямая симметрия с keystone"; §4.7 synthesis calls back to asymmetry ("Measure — стрелка, у которой AI снизил доверие"); §5.7 synthesis explicitly names "keystone-callback"; §6.5 delivers the full payoff resolving the §0.1 hook paradox. ✅ Callback discipline is consistently maintained across all 4 parts — this is a genuine strength, not just a checklist item.
- Double-loop learning (Argyris/Schön) is a nice, non-obligatory addition in §0.4 that pays off later by explaining RLHF/reward-hacking (§4.4) — good forward cross-reference design.
- Minor: §0.6 (Sber intent-loop) is explicitly framed "не флагман" per plan/changelog, correctly executed — no flagship-vendor overreach.

## 5. LO coverage

- **LO1** (classify classic/AI-assisted/AI-first per phase + reason): covered structurally by the base→AI→limits pattern itself in every section, plus explicit synthesis in §4.7, §5.7, §6.5, and the summary matrix in §6.4. ✅ strong.
- **LO2** ("when AI-first hurts" criterion per phase): every phase has an explicit "Когда здесь НЕ AI-first" block (§1.6, §2.5, §3.5, §4.4, §5.3) plus one embedded in §6.3's failure block. ✅ present in all 6 phases, consistently formatted.
- **LO3** (risks via guardrails/evals/human-escalation gate — including the **data-security facet** the curator required): present as two dedicated "LO3-акцент" blocks — chapter-part3.md §5.2 (line 223, "что безопасно скармливать сторонним AI-инструментам" — PII/regulated data into external tracing tools) and chapter-part4.md §6.2 (line 64, same theme elevated to org governance/policy-as-code). ✅ **curator's required facet is present and reasonably substantive** (~200 words combined, tied to concrete regulated-data examples). This closes the curator's sign-off note satisfactorily — good.
- **LO6** (recognize failure→phase→criterion/alternative from description): the 13-failure structure plus explicit closing Q&A drilling exactly this skill ("В: как их запомнить, чтобы это был аппарат") in §6's Q&A. ✅ strong, this is the LO the chapter is most confidently built around.
- **Bloom boundary vs seminar:** Lecture stays at Understand/Analyze/Evaluate; the practical construction of hypothesis→reference-dataset→3-evals→guardrail→escalation-point is explicitly deferred to the paired seminar (Сем7, noted as re-scope follow-up, correctly NOT claimed as already resolved in this chapter). ✅ clean separation, no scope creep into Apply.

## 6. Baseline/Counterfactual — sample of 10 measurable claims across all 4 parts

| # | Claim | Baseline/counterfactual present? | Location |
|---|---|---|---|
| 1 | MIT NANDA "95% zero ROI" | ✅ Yes — funnel 60%→20%→5% + "25% of those who piloted" reframe + COI flagged `[FACT-CHECK]` | chapter.md §0.1, chapter-part4.md §6.3 |
| 2 | NN/g synthetic users 7/7 vs real 3/7 | ✅ Yes — direct paired comparison, same test material | chapter.md §1.7 |
| 3 | Deloitte Australia A$440k report | ✅ Yes — cross-referenced to Charlotin DB "712 cases, ~90% in 2025" for base rate | chapter.md §1.8 |
| 4 | WCAG 29.0% compliance in AI UI tools | ✅ Yes — denominator given (21,880 evaluations), `[FACT-CHECK]` flagged | chapter-part2.md §2.5 |
| 5 | McDonald's ~100 restaurants | ✅ Yes — explicit denominator "≈13,786 US restaurants = 0.7%" | chapter-part2.md §3.7 |
| 6 | Anthropic PR volume +200%/16% substantive review | ✅ Yes — both numbers paired as ratio, `[VFY-day-of]` flagged | chapter-part2.md §3.3 |
| 7 | Facebook MSI 5× reaction weight | ✅ Yes — internal 0.05% holdout test showing 50% more hidden posts as counterfactual | chapter-part3.md §4.5 |
| 8 | Lexis+ 17% / Westlaw 33% hallucination | ✅ Yes — paired against raw GPT-4 88% baseline, n=202 queries | chapter-part3.md §4.6 |
| 9 | Zillow $304-408M writedown | ✅ Yes — "9,680 bought, 3,032 sold, ~$80k/unit loss" denominator | chapter-part3.md §5.4 |
| 10 | Just Walk Out 700/1000 manual review | ✅ Yes — explicit target denominator "50/1000 target → 14× over" | chapter-part4.md §6.4 |

**Result: 10/10 sampled claims carry an inline baseline, denominator, or explicit `[VFY-day-of]`/`[FACT-CHECK]` flag.** This is the chapter's second-strongest dimension after structure compliance — no P1 "missing denominator" issues found in this sample. The chapter is unusually disciplined about this compared to typical first-draft output; worth noting as a strength to preserve in revision.

## 7. Depth/quality

- Reads as genuine textbook-chapter prose, not a slide outline — dense paragraphs with mechanism explanations (e.g., the rationale for why randomization implies causality in §4.1, the p-hacking inflation math in §4.2, the pass@k vs pass^k explanation in §4.3) rather than bullet-listed facts. ✅
- Q&A backup is present per section (Раздел 1 through Раздел 6, plus a "сводные" Q&A block) and is substantive — each answer adds a distinct pedagogical angle rather than restating the section, e.g. the Klarna Q&A explicitly re-derives the augmentation-vs-replacement distinction. ✅
- Glossary (chapter-part4.md) is comprehensive (~45 terms) and ordered by appearance; includes an explicit anti-anglicism note. ✅
- Sources (40 numbered entries, chapter-part4.md) are properly separated from narrative and dated. ✅
- Cross-references between parts work mechanically: each part's frontmatter has `cross_ref`, and inline "(см. §X, Часть N)" pointers were spot-checked and resolve to real sections (e.g., chapter-part3.md §5.2 correctly points back to reference-dataset defined in Part 1 §1.5 and Part 2 §3.4). No broken forward/back references found in spot-check.

## 8. Pedagogical sequence & cross-part drift

- No contradictions found between parts. The Sber narrative is consistently distributed as designed (peer-illustration in §0.6, dual-loop in §3.4, maturity ladder + retracted v1 numbers in §6.2/§6.3) without being over-elevated to flagship status anywhere — matches the plan's explicit intent.
- Terminology is consistent across parts (reference dataset, guardrail-метрика, circuit breaker, agency-ladder all reused with identical definitions on reuse, not redefined differently).
- One very minor sequencing note (not a P1): §4.7 and §5.7 are useful per-section syntheses that were added post-critique per the plan's own v3→v3.1 changelog (meth-P0 fix); Раздел 6 has no equivalent per-section synthesis before §6.5, but this is intentional since §6.5 *is* the full-chapter keystone payoff, not a section-local synthesis — no gap here.

---

## P0 (BLOCKING)

1. **[P0]** Content word count = 27,843 (excl. bibliography) / 29,514 (incl.) — both below plan's declared ~31,000 and the strict count is below the 28,500 floor. **Fix:** expand ~2,200-3,200 words, concentrated where strict-in is also weakest (Part 1) to solve both P0s at once if possible.
2. **[P0]** Strict-in holistic = 28.3%, below 30% floor, AND concentrated (Part 1 = 16.1%, less than half the required floor and roughly half of Part 3's 35.2%). This is exactly the "REVISE not polish" scenario the counter-check is designed to catch. **Fix:** rebalance Part 1 — either add a third on-point failure moment to Раздел 1, or trim §0 keystone exposition (~300-400 words) to shrink the non-failure-eligible denominator, or deepen §1.7/§1.8. Recommend book-editor decide the cheapest path that doesn't dilute discovery pedagogy; do not pad with restated "Урок" sentences, which would not survive an honest re-recount.

## P1

3. **[P1]** frontmatter `strict_in_self_estimate` (Ч1~41%···Ч2~43%···Ч3~45%···Ч4~40%) is materially wrong (actual 16.1/31.3/35.2/30.8) — self-estimate methodology needs correction before future chapters trust it. Likely cause: base/AI-capability paragraphs counted as in-bucket contrary to Decision #78's partial→out rule. Flag for book-editor's estimation process, not just this chapter's number.
4. **[P1]** frontmatter `length_words: "~31000"` is inaccurate (actual ~29,514 gross / 27,843 net) — update once word-count fix lands.

## P2

5. **[P2]** Раздел 1's keystone-heavy opening (§0, ~2,500 words) is good content but structurally penalizes Part 1's strict-in ratio versus other parts that don't carry equivalent scene-setting overhead — worth a design note for future multi-part chapters (put keystone in its own accounting bucket rather than folding it into Part 1's denominator), separate from whether this specific chapter needs trimming.
6. **[P2]** Раздел 6 has no per-section synthesis paragraph before §6.5 (unlike Раздел 4's §4.7 and Раздел 5's §5.7) — not a gap since §6.5 serves that role at chapter scale, but worth confirming in Phase 7 (slides) that s44-46 don't need an analogous synthesis beat that Раздел 4/5 dividers imply by pattern-matching.

---

## Summary for orchestrator

**Verdict: REVISE.** Two independent P0s: (1) content word count is 27,843–29,514 depending on counting convention, below both the 28,500 BLOCKING floor (strict count) and the plan's declared ~31,000 target; (2) honest strict-in recount is 28.3% holistic — below the 30% floor — with Part 1 (chapter.md, §0+Раздел 1) at only 16.1%, roughly half the required share and about half of Part 3's 35.2%, triggering the single-part-concentration counter-check. The book-editor's self-estimate (~40-45% per part) is not reproducible from the text; it appears to have counted base/AI-capability material as in-bucket, which Decision #78 explicitly forbids (partial→out, full-block-only).

**What's strong:** structure compliance is excellent — all 6 sections cleanly follow base→AI→limits→failure with no off-topic failures (Zillow correctly re-homed to Support, contrasts like Character.AI/iTutorGroup and Google/McDonald's are pedagogically sharp). The keystone (PDCA/OODA/BML + cost/trust asymmetry) is established in §0 before any phase-dive and is consistently called back in every part's synthesis. LO coverage is complete including the curator-required LO3 data-security facet (two dedicated blocks, ~200 words). Baseline/counterfactual discipline is very strong: 10/10 sampled measurable claims carry a denominator or explicit flag — no P1 "missing denominator" issues found. Fact-integrity corrections from the plan (Med-PaLM, Mata v. Avianca attribution, Facebook MSI, Guardian Agents/Sber) are all correctly applied in the text.

**Top fixes before USER GATE A:** (1) expand chapter by ~2,200–3,200 words to clear the word-count floor; (2) rebalance Part 1's strict-in share — cheapest fix is likely trimming §0.5/§0.6 by 300-400 words plus modestly deepening §1.7/§1.8, or adding a third on-point moment to Раздел 1; (3) correct frontmatter `length_words` and `strict_in_self_estimate` once the above lands so future phases trust the self-report; (4) no changes needed to structure, keystone, LO coverage, or baseline discipline — these are already solid and should be preserved as-is during revision, not touched.

Full report: `notes/lecture-5-review/pdlc/2026-09-06-phase3/methodology-critic.md`
