---
id: s26
type: assertion_visual
section: "Section 4. Sampling and Generation"
duration_min: 2.5
assertion: "At every step, the model outputs a probability distribution over ALL tokens in the vocabulary — then picks one"
learning_goal: "Probability distribution as the model's 'real' output; sampling as the rule for choosing"
learning_outcomes: [LO1]
chapter_ref: "§4.1 (chapter-part2.md) [for-slide-s26]"
visual_brief: "Bar chart, top-5 candidates after 'Today I ate …': apple 0.32 (gold), pizza 0.19, salad 0.14, a sandwich 0.11, a cucumber 0.08 — in an Ocean rounded box. Down arrow 'Sampling → one token'. Footnote: the remaining ~200k tokens each < 0.05, sum = 1. Caption: the numbers are illustrative."
---

# Visible content

## Title bar
"At every step — a probability distribution over the entire token vocabulary"

## Body
[Bar chart, top-5 candidates, Ocean rounded box]

**Context:** "Today I ate …"

**P(next token):**
- `apple` — **0.32** *(gold — the maximum)*
- `pizza` — 0.19
- `salad` — 0.14
- `a sandwich` — 0.11
- `a cucumber` — 0.08

[Down arrow: "**Sampling → one token**"]

[Footnote, small]
*The remaining ~200,000 tokens in the vocabulary — each below 0.05. All probabilities sum to 1. The numbers are illustrative.*

[Gold callout]
**The distribution is the model's "real" output. A confident answer and a hallucination existed simultaneously before sampling — as probability mass; the policy made the choice.**

## Speaker notes

The result of three pipeline stages: the model's output is a probability distribution over the entire vocabulary — for each of roughly two hundred thousand tokens, a probability of being next; the sum equals one. For the prompt "Today I ate," the distribution looks roughly like this: "apple" — 0.32, "pizza" — 0.19, "salad" — 0.14, then a long tail; the numbers are illustrative, but the picture is stable. The distribution isn't uniform — the model has statistical preferences — but it isn't a single spike either: there are several plausible candidates.

Sampling is the rule for picking one token out of this distribution. All the "creativity" and all the "randomness" of large models live in this rule, and it is the only part of the pipeline you control directly, through the API's knobs.

It's worth internalizing once and for all how much this distribution is the "real" output of the model, with everything else a policy layered on top of it. A confident answer and an evasive one, an accurate fact and a hallucination, "Paris" and "perhaps you mean…" — before sampling, all of this existed simultaneously, as probability mass spread across different continuations; the policy made the choice, not some "opinion" of the model.

A practical consequence for anyone building pipelines: some providers expose a slice of this information through the API — log-probabilities of the top candidates at each step. This is a useful diagnostic channel: a wide, spread-out distribution at a key token in the answer is an honest signal of the model's uncertainty, one that the answer's own text may never reveal. For classification, this is a cheap way to get a confidence measure without a second call asking "how sure are you?" — that second call, incidentally, doesn't measure the model's confidence, it measures how well-trained it is at answering such questions.
