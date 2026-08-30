---
id: s21
type: case_study
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "A benchmark number can be both true and misleading: Devin 13.86% — 79 of 570 (only 25% of the bench, with contamination); OpenAI \"70% more PRs\" — no denominator; brand/benchmark != discipline"
learning_goal: "[SI] Anti-hype: Devin 13.86% (79/570), Cursor admits its weakness, OpenAI \"70% more PRs\" with no denominator"
learning_outcomes: [LO7, LO4]
chapter_ref: "§3.5 [for-slide-s19]"
references: [devin-cognition, swe-bench-pro, openai-swe-bench, cursor]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study: left — the SWE-bench gap in an Ocean rounded box: Verified ~88% (public, resembles training data) vs Pro ~64%
  (private, contamination-resistant), gap ~24 pp → trust is inversely proportional to unfamiliarity/criticality.
  Right — 3 overclaims with baselines: Devin 13.86% = 79/570 = only 25% of the bench (contamination acknowledged; independently ~15% = 3/20) ·
  OpenAI "~59% of failures = test-design defects" + "70% more PRs" WITH NO DENOMINATOR · Cursor "Composer frontier-fast",
  but the blog itself admits GPT-5/Sonnet outperform (self-contradiction). Bottom — 5 questions for a vendor number (LO7):
  slice · contamination · comparison baseline · fact/opinion · what's in the fine print. Gold — "13.86% is true on exactly a quarter of the tasks".
  Source links — inline right next to the material (definition/claim/recommendation), NOT in a bottom footer; small and muted: all numbers [VFY-day-of], leaders weekly; brand/benchmark != discipline.
interaction: none
---

# Visible content

## Title bar
A brand and a benchmark number != engineering discipline

## Body
[Left — the SWE-bench gap in an Ocean rounded box]

**SWE-bench Verified** (~500 tasks, public code) — top ~**88-89%**.
**SWE-bench Pro** (private, contamination-resistant) — leader ~**64%**.
The gap of **~24 pp**: trust in the number is inversely proportional to how unfamiliar and critical your task is.

[Right — three overclaims with baselines]

**Devin (Cognition): 13.86%** "solved" vs a baseline of **1.96%** — but **only on 25% of the bench (79 of 570 tasks)**, acknowledged contamination, a 45-min limit; an independent evaluation gave ~**15% (3 of 20)**.

**OpenAI:** marketing of "~80% Verified" / "70% more PRs" — but OpenAI itself showed: **~59% of the model's "failures"** are test-design defects, not the model's; **"70% more PRs" has no denominator.**

**Cursor:** Composer marketing of "frontier, 4x faster", but its own blog admits: GPT-5 and Sonnet 4.5 "both outperform" → frontier-**fast**, not frontier-**best**.

[Five questions for any vendor number]
1. Which slice? 2. Contamination? 3. Comparison baseline? 4. Fact, or opinion/marketing? 5. What's in the fine print?

[Gold callout]
Devin 13.86% — technically true **on exactly a quarter of the tasks**. A number can be true and misleading at once; a high figure does not answer the merge-gate question. A brand/benchmark does not replace discipline.

## Speaker notes

The second failure of the implementation phase is not technical but a failure of judgment: swapping engineering discipline for a brand and a benchmark number. The measuring instrument here is SWE-bench: you take a real task from the issue tracker of an open project and measure what share of generated patches pass the tests. Importantly, it has two versions, and the gap between them is meaningful: on Verified (about five hundred validated tasks on public code) top systems score around eighty-eight to eighty-nine percent, while on Pro (private, contamination-resistant repositories) the leader is around sixty-four. The roughly twenty-four-point gap is not random: on code resembling the training data the number is higher; on unfamiliar and private code, lower. The practical takeaway: trust in the number is inversely proportional to how unfamiliar and critical your specific task is.

Now three model overclaims that teach you to read vendor numbers. Devin from Cognition was advertised with the figure of thirteen point eight-six percent of tasks solved against a baseline of almost two — it sounds like a breakthrough. But in the fine print: the result was obtained on only twenty-five percent of the bench, seventy-nine tasks out of five hundred seventy, with acknowledged data contamination and a forty-five-minute limit; an independent evaluation gave about fifteen percent, three out of twenty [1]. So the number is technically true — on exactly a quarter of the tasks — and misleading at the same time. OpenAI builds its marketing on "eighty percent of SWE-bench" and "seventy percent more pull requests", yet it publishes its own analysis where about fifty-nine percent of the model's "failures" are caused by test-design defects, and "seventy percent more PRs" is given with no denominator at all [2]. Cursor advertises its Composer as frontier and four times faster, but in its own blog admits that GPT-5 and Sonnet outperform it — frontier-fast, but not frontier-best.

From this comes a portable instrument of judgment — five questions for any vendor number [2]: on which slice it was obtained, whether there is contamination, what it is compared against, whether it is a measured fact or marketing, and what is written in the fine print. The load-bearing takeaway: a high benchmark figure does not answer the merge-gate question — whether this specific PR can be merged into your system. A brand and a benchmark do not replace engineering discipline.
