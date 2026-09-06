---
id: s39
type: summary
section: "Section 6. Wrap-up"
duration_min: 1.5
assertion: "An LLM isn't always the right tool; and when it is, you don't always need the top-tier one"
learning_goal: "A 'when not an LLM' decision tree + a new 2026-level idea: an escalation ladder within the LLM class"
learning_outcomes: [LO6]
chapter_ref: "§5.5 (chapter-part3.md) [for-slide-s39]"
visual_brief: "Left 60% — a decision tree in Ocean rounded boxes: root 'When not an LLM?', 4 branches: labeled classification into fixed categories → classic ML (+note 'an LLM is also non-deterministic at T=0'); explainability before a regulator → transparent methods; response <100ms → a specialized small model; exact character-level/arithmetic operations → code. Otherwise → LLM. Right 40% — a card 'and not always the top LLM': an escalation ladder — a wide bottom rung '90% of requests → a cheap model', a narrow top rung '10% hard cases → premium'; the math $10,000 vs $1,180/mo (gold). No repeat of the Kimi line (verbatim thesis from s36 — the price ladder makes the point on its own)."
---

# Visible content

## Title bar
"When not an LLM — and when not the top LLM"

## Body
[Left — decision tree, Ocean rounded boxes]

**When an LLM is not the right tool:**
- **Classification** into fixed categories with thousands of labeled examples → classic ML: cheaper, faster, reproducible — and an LLM is also non-deterministic at T=0
- **Explainability before a regulator** → transparent classic methods
- **Response < 100ms** (anti-fraud, offline devices) → a specialized small model
- **Exact character-level and arithmetic operations** → code, not a model

**Otherwise** — language processing, flexible formats, multi-step reasoning, generation → an LLM applies and is often optimal

[Right — escalation ladder]

**...and not always the top LLM**
- 90% of requests → a model at $0.20/M; 10% hard cases → premium at $10/M
- One billion tokens/month: **$10,000** all on premium vs **$1,180** with routing *(gold)*

## Speaker notes

Knowing the internals is also useful for seeing where a large language model is not the right tool. Classification into a fixed set of categories with thousands of labeled examples — classic ML: cheaper, faster, reproducible, and an LLM, as we now know, is also non-deterministic at zero temperature — for a classifier that's a straight-up drawback. Explainability before a regulator — transparent classic methods: an LLM won't explain an individual prediction. Response under a hundred milliseconds — anti-fraud in a payment pipeline, offline devices — a specialized small model: prefill alone eats the time budget. Exact character-level and arithmetic operations — code, not a model. In everything else — natural language processing, flexible formats, multi-step reasoning, generation — an LLM applies and is often optimal.

A new layer of this decision in 2026: the choice within the LLM class has stopped reducing to "grab the strongest one." The Kimi-versus-GPT-5.5 pair — comparable results on a guarded benchmark at a price 80 percent lower. The working pattern is an escalation ladder: mass-volume simple requests go to a cheap model, and only hard cases — by an explicit criterion — get escalated to the expensive one. The arithmetic: a pipeline handling a billion input tokens a month, entirely on a premium model, costs ten thousand dollars on input alone; with routing — "ninety percent to a twenty-cent model, ten percent to premium" — it's around eleven hundred eighty, almost an order of magnitude less. The difference comes down to one difficulty classifier at the entry point and your own eval set confirming that the cheap tier holds up. There's nothing new in this formula — what's new is only the habit of doing the math.
