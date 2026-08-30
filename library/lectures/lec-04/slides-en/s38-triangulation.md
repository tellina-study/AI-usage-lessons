---
id: s37
type: case_study
section: "Section 7. Synthesis — discipline by phase"
duration_min: 3
assertion: "Triangulation of three independent methods (DORA / GitClear / METR): individual AI benefits != system quality; the strength is in the convergence of independent methods → the method matters more than the tool"
learning_goal: "[SI] Triangulation DORA ('amplifies what is already there') / GitClear / METR → the method matters more than the tool"
learning_outcomes: [LO1, LO7]
chapter_ref: "§7.2 [for-slide-s37]"
references: [dora-report, gitclear, metr-study]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study triangulation: 3 independent measuring bodies converge on one point (visual — 3 arrows into a common center "individual AI benefits != system quality"),
  each in its own Ocean rounded box plate with a number+baseline: DORA (n~5000, system-level): ~90% throughput positive, BUT the link of AI to stability
  is negative for the 2nd year running; "AI amplifies what is already there" · GitClear (211M lines): refactoring ~25%→<10%, duplicates 8.3%→12.3%, churn grew (correlation, not RCT) ·
  METR (n=16, experts on familiar code): -19%, while believing in a speed-up of ~-20% = the perception gap (on unfamiliar code the effect differs).
  The strength of the argument — a plate "convergence of independent methods: different blind spots → low probability of a matching error". Practice: a CI gate on duplication/churn; measure the system effect, not the feeling.
  Gold — "the method matters more than the tool". Source references — inline right at the material (definition/claim/recommendation), NOT in a bottom footer; small and muted: DORA/GitClear/METR.
interaction: none
---

# Visible content

## Title bar
Three independent methods converge: an individual AI benefit != system quality

## Body
[Triangulation — three arrows into a common center, each method in an Ocean rounded box]

**DORA** (n ≈ 5000, system-level) — ~90% of reports: throughput is **positive**, but the link of AI to **stability is negative for the second year running**. Lens: "AI amplifies what is already there".

**GitClear** (211M lines) — refactoring **~25% → <10%**; duplicates **8.3% → 12.3%**; churn **grew**. Three markers of one process — the accumulation of tech debt. *(Correlation, not an RCT.)*

**METR** (n = 16, experts on familiar code) — tasks with AI took **-19%** more time, while they believed in a speed-up (~-20%) = the perception gap. *(On unfamiliar code the effect differs.)*

[The strength of the argument]
The value is in the **convergence of independent methods**: DORA, GitClear, and METR have different blind spots, so the probability that all three got it wrong the same way is low. The shared conclusion is more reliable than any single number.

[Gold callout]
The conclusion is one: **the method matters more than the tool**. The practice — a CI gate on duplication and churn; measure the **system effect**, not the feeling.

## Speaker notes

The penultimate synthesis tool is triangulation, and this is an important methodological technique in its own right, not just a summary of numbers. Three independent measuring bodies, each by its own method, arrive at one conclusion: the individual and especially the perceived benefit of AI is not the same as the system quality of the product.

DORA is the largest system-level program, about five thousand respondents. Its picture is dual and honest: in roughly ninety percent of cases throughput grows, but the link of AI adoption to delivery stability is negative, and already for the second year running [1]. Hence their load-bearing lens: AI amplifies what is already there, it is a multiplier, not a source of quality. GitClear looks at the code itself: over two hundred eleven million lines the share of refactored and reused code fell from twenty-five to under ten percent, the share of duplicates grew, churn grew — three markers of the accumulation of technical debt [2]; the caveat is honest — this is a correlation, not a controlled experiment. And METR, which we saw at the very start: sixteen experts on familiar code, objectively minus nineteen percent to speed while believing in a speed-up — the perception gap [3]; the mandatory baseline — on unfamiliar code the effect differs.

Why I bring them together rather than citing one number. The strength of the argument here is precisely in the convergence of independent methods: the DORA survey [1], the GitClear code analysis [2], and the controlled METR experiment [3] have different blind spots and different ways of being wrong. When three such different methods point the same way, the probability that all three got it wrong the same way is low — the shared conclusion is more reliable than any single number. And their conclusion is one, and it is also the conclusion of the whole lecture: the method matters more than the tool, AI multiplies the existing discipline. The practical consequence — put a gate on duplication and churn in CI and measure the system effect of your work rather than trusting the feeling of speed.
