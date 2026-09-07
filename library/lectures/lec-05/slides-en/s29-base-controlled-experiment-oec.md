---
id: s29
type: process
section: "Section 4. Measure / Experiment"
duration_min: 2.5
assertion: "Randomization gives causation, not coincidence; the OEC is the metric the team agreed on in advance"
learning_goal: "BASE: the controlled experiment + OEC + guardrail metrics; Kohavi's teaching example (time-on-site)"
learning_outcomes: [LO1]
chapter_ref: "§4.1 [for-slide-s29]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  process: 2 groups of silhouettes, split randomly (a die/coin icon between them) — "Control"
  on the left, "Treatment" on the right, a metric-comparison arrow between them leads to a
  decision-diamond "cause, not coincidence."
---

# Visible content

## Title bar
Randomization tells cause apart from coincidence

## Body
[2 groups: Control / Treatment, split randomly, an arrow to "cause, not coincidence"]

**Controlled experiment (Kohavi)**
- A hypothesis with a mechanism → randomization → a sample size fixed in advance → a decision

**OEC** — the metric the organization **agreed on in advance**
- The teaching trap (Kohavi): "time on the support site" — good or bad?

## Speaker notes

A controlled online experiment applies the logic of randomized studies to a live product: users are randomly split into Control and Treatment, and a metric is measured for each group. Because the assignment is random, a statistically significant difference can be attributed to the change itself, not to pre-existing differences. Without randomization you have correlation; with randomization you have causation. That's exactly why a canary rollout is not equivalent to an A/B test: it has no held-out control group, so it answers "did something break," not "did this cause an improvement."

The canonical process: formulate a hypothesis with a mechanism — a hypothesis without a mechanism is a guess, not an experiment — choose a metric, randomize users, run to a sample size fixed in advance, check data quality, analyze, decide.

The OEC is the metric the experiment is actually trying to move — what the organization agreed to count as success. Kohavi's teaching example: a team optimizing a support website adopted "time on site" as the metric. When asked to state the direction, the team split: more time — good, deep engagement, or bad, the user is stuck? The team unanimously adopted the metric without ever agreeing what it meant. Guardrail metrics are what you monitor but don't optimize: they catch collateral damage the OEC can't see. This is a structural fix for a significant classical trap — optimizing a single proxy metric in isolation — which we'll see in this section's failure.
