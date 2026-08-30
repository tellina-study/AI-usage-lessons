---
id: s13
type: section_divider
section: "Раздел 3. Механизм внимания"
duration_min: 0.5
assertion: "Section 3 — The attention mechanism: how the model decides what matters right now"
learning_goal: "Single section divider лекции (для самого плотного раздела)"
learning_outcomes: [LO1]
chapter_ref: "§3 [for-slide-s13]"
visual_brief: "Большое «Раздел 3» по центру (120pt outline gold). Под ним — «Механизм внимания». Внизу — roadmap-bar (5 карточек) с gold-маркером «Вы здесь — Раздел 3»."
---

# Visible content

## Title bar
(нет — section divider слайд)

## Body
[Большое «Section 3» по центру верхней половины — 120pt outline gold]

[Под ним — sub-title]
**The attention mechanism**

[Caption мелким — assertion]
"How the model decides what matters right now"

[Roadmap-bar внизу — 5 карточек, gold-маркер на текущем]
- 0. Introduction
- 1. Tokenization
- 2. Embeddings
- 3. Attention mechanism ← **You are here** (gold)
- 4. Sampling
- 5. Wrap-up

## Speaker notes

We have passed two stages of the inference pipeline. The first — tokenization: text is cut into tokens, each getting an id from the model's vocabulary. The second — embeddings: each id is mapped to a learned vector, and geometric closeness in this space reflects closeness in meaning.

Section 3 is about the third stage and the mechanism hardest to grasp in the lecture: the **attention mechanism**. At the input we already have a sequence of token embeddings; at the output we need to decide which of them the model relies on most when generating the next token. It is exactly this "decision of what to look at" that the attention mechanism performs. On it depend why a prompt with a role works better than an empty one, what a context window is and what its limits are, and why important information in the middle of a long prompt is systematically lost.

This section has four slides plus this divider. First we pin down the basic definition through the metaphor of a flashlight in a dark room — without formulas, without Q/K/V matrices, without multi-head attention. Then we take apart a worked example on a concrete sentence and from it derive the effect of a role in the prompt — the first of Lecture 1's three "whys." Then we discuss the context window as a physical limit and the quadratic cost of attention. And we close the section by taking apart the "lost in the middle" effect — why a large window does not mean good use of context.

This section is the most conceptually dense in the lecture. This is deliberate: the attention mechanism is the most content-heavy part, and it is worth going through it slowly. One section divider for the whole lecture — here — to give a pause before the densest piece of the material.
