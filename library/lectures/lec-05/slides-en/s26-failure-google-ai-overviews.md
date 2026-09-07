---
id: s26
type: case_study
section: "Section 3. Build / Launch"
duration_min: 2.5
assertion: "Google shipped AI Overviews to 100% of US search in one step, skipping canary rollout — and got \"eat rocks\" / \"glue on pizza\""
learning_goal: "On-point failure #5: Google AI Overviews (LO2/LO6)"
learning_outcomes: [LO2, LO6]
chapter_ref: "§3.6 [for-slide-s26]"
in_bucket: true
interaction: none
verify_day_of: false
meme_or_visual: >
  case_study: a comparison of two rollout paths — the correct one (1%→10%→25%→50%→100%, a
  step ladder) crossed by an arrow going straight from 0% to 100% (Google). Next to it, small
  warning icons "a rock" and "pizza with glue" as symbols of the viral failures.
source: "Forbes / AndroidPolice (May 2024)"
---

# Visible content

## Title bar
0% → 100% in one step — skipping canary rollout entirely

## Body
[Comparison: a step rollout (correct) vs a direct 0→100% arrow (Google), crossed out]

**Google AI Overviews, May 2024**
- Rolled out to **100%** of US search in one step
- No eval gate: "eat rocks" (a satirical Onion article), "glue on pizza" (a Reddit joke)
- Users couldn't turn the feature off

[Gold callout]
At 1% of traffic the pattern would have surfaced within days in internal monitoring — instead: public ridicule in front of 100% of the audience

## Speaker notes

In May 2024, Google rolled out its AI Overviews feature to one hundred percent of US search users in a single step — skipping the usual staged rollout and with no eval gate. Within days the feature started producing viral, literally dangerous recommendations: eating rocks — the source, a satirical article from The Onion — and putting glue on pizza to help the cheese stick better — the source, an eleven-year-old joke comment on Reddit. Users couldn't turn the feature off. Google's response was reactive — all the fixes came after full deployment, not before it.

The mechanism, tied to the Build/Launch phase: this is exactly the missing-staged-rollout case the previous slide warns about — a full-traffic launch of a generative feature with no canary phase that would have caught the source-quality failure pattern before every user saw it. Notice the nature of the specific failures: the model didn't break — it synthesized a statistically plausible answer from its corpus, failing to distinguish satire from fact, and delivered the result with the full confidence of an authoritative search answer. This is the "confidently wrong" failure mode a canary phase would have caught within days at one percent of traffic.

The lesson: a generative feature that synthesizes content from the open web needs the same discipline of staged deployment and an eval gate as any other AI feature — "search is our mature core product" is not a reason to skip rollout, it raises the cost of skipping it. The criterion: any generative feature whose failure mode is "confidently wrong, sourced from low-quality content" needs pre-launch source-quality gating and post-launch staged exposure. The alternative: a canary launch to a small percentage with automatic monitoring of known risk classes, and a persistent user opt-out toggle.
