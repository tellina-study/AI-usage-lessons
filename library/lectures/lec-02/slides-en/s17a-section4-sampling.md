---
id: s17a
type: section_divider
section: "Section 4. Sampling"
duration_min: 0.5
assertion: "Section 4 — Sampling: from the distribution to a token"
learning_goal: "Section 4 divider — transition to token selection"
learning_outcomes: [LO1, LO4]
chapter_ref: "§4 [for-slide-s17a]"
visual_brief: "Large 'Section 4' centered (140pt gold). Below — 'Sampling'. Under it — the frame phrase 'From the distribution to a token'. Bottom — roadmap bar (6 sections) with the gold marker on '4 Sampling'."
---

# Visible content

## Title bar
(none — section divider slide)

## Body
[Large "Section 4" centered in the top half — 140pt gold]

[Below it — sub-title]
**Sampling**

[Caption in small print — frame phrase]
"From the distribution to a token"

[Roadmap bar at the bottom — 6 cards, gold marker on "4 Sampling"]
- 0. Introduction
- 1. Tokens
- 2. Embeddings
- 3. Attention
- 4. Sampling ← **You are here** (gold)
- 5. Wrap-up

## Speaker notes

We've closed the section on attention: the model can distribute importance over the context tokens. But inference isn't finished yet. The model has an intermediate internal result — a probability distribution over all ~200 thousand vocabulary tokens — and it must pick exactly one token from that distribution to become the next one in the answer.

This step is called sampling. It determines what a user perceives as the model's "style": how deterministically it answers identical requests, how creative or dull it is, how predictable. And it is sampling that closes the third of Lecture 1's three "whys": why the same request gives different answers.

There are five slides in this section. First we'll fix what a probability distribution is on a concrete example of next-token prediction. Then we'll cover the main API knob — temperature — in three modes: T=0 (deterministic argmax), T≈1 (the standard for chat), T=2 (chaos). Next — a practical matrix of four API parameters for four scenarios: classification, code generation, chat explanation, creative writing. Then we'll show sampling in the context of the full autoregressive generation loop — where it sits between two forward passes of the model. And we'll close the section by comparing inference locally and in the cloud: the same pipeline, but a different model size and environment.
