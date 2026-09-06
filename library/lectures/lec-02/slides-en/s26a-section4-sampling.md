---
id: s26a
type: section_divider
section: "Section 4. Sampling and Generation"
duration_min: 0.5
assertion: "Section 4 — Sampling and Generation: how a probability distribution gives birth to a single token"
learning_goal: "Section divider for section 4 — transition to the fourth stage of the pipeline"
learning_outcomes: [LO1, LO4]
chapter_ref: "§4 (chapter-part2.md) [for-slide-s26]"
visual_brief: "v3.1 (#183 round 3): 2-column composition (unified pattern) — left text: 'Section 4' (92pt gold), 'Sampling and Generation', frame phrase, tag '4 case studies · 2 failures'. Right — real photo of a pair of casino dice (Caesars Palace, Wikimedia Commons) in an Ocean rounded box, ≈25% of slide area, with attribution. Bottom, full width — pipeline progress bar: stage 'Sampling' highlighted gold, completed stages teal, future stages muted. NO 'You are here' label, NO minutes."
---

# Visible content

## Title bar
(none — section divider slide)

## Body
[Large "Section 4" centered in the upper half — 140pt gold]

[Below it — sub-title]
**Sampling and Generation**

[Caption — the section's meaning in one line]
"How a probability distribution gives birth to a single token — and which knobs steer that choice"

[Tag line, small]
4 case studies · 2 failures

[Pipeline progress at the bottom — the pipeline diagram from s04b, stage "Sampling" highlighted gold]

[Small illustration of "dice" — corner of the slide]

## Speaker notes

Three pipeline stages are behind us: text was cut into tokens, tokens received vectors, attention decided what to lean on in the context. The result of those three stages is a probability distribution over the model's entire vocabulary: for each of roughly two hundred thousand tokens, a probability of being next.

The fourth stage is sampling: the rule for picking one token out of that distribution. All the "creativity" and all the "randomness" of large models live in this rule, and it is the only part of the pipeline you control directly, through the API's knobs.

The order we'll move through the section. First we'll pin down the distribution itself — that it is the "real" output of the model, and everything else is a policy layered on top of it. Then the precise mechanics of temperature and its neighbors — with a live comparison of behavior at zero versus one-point-five. Next — a check of the trickiest of the six claims: does zero temperature really give identical answers every time; the answer will likely surprise you, and it matters for anyone writing tests against an LLM. After that — how the classic set of four API knobs grew to six, guaranteed response format via structured outputs, the autoregressive loop that assembles everything into one whole, and reasoning tokens — an invisible but billed line item on your invoice. We'll close the section with a fresh look at the choice between a local model and the cloud.
