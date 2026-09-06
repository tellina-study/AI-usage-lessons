---
id: s04
type: assertion_visual
section: "Section 0. Introduction"
duration_min: 1.5
assertion: "Lecture goal: examine how a language model works — and get into the details that change engineering decisions"
learning_goal: "Lecture goal + lecture promises for the new 7-section structure"
learning_outcomes: [LO1, LO7]
chapter_ref: "§Введение [for-slide-s04]"
visual_brief: "Lecture goal, large (28-32pt bold #21295C). Below it — 7 compact promise chips (one per lecture section, no M-codes): 'why a fixed strawberry answer proves nothing', 'why a role-based prompt genuinely changes the answer', 'what a 1M window can actually do', 'why T=0 doesn't give identical answers', 'what invisible tokens actually cost', 'small model vs. giant — what criterion to choose by', 'what to replace blind trust in benchmarks with'. Gold marker on 'important details'."
---

# Visible content

## Title bar
"Lecture goal"

## Body
[Lecture goal, large, top half of the slide — 28-32pt bold #21295C; "important details" — gold]

> "Examine how a language model works — and get into the important details that change how you build prompts, agents, and decisions."

[7 compact promise chips, bottom half]

- why a fixed "strawberry" answer proves nothing
- why a role-based prompt genuinely changes the answer
- what a 1M-token window can actually do
- why T=0 doesn't guarantee identical answers
- what invisible reasoning tokens actually cost
- small model vs. giant — what criterion to choose by
- what to replace blind trust in benchmarks with

## Speaker notes

The goal of this lecture: examine how a language model works — and get into the important details that change how you build prompts, agents, and decisions. We'll walk the inference pipeline from text to answer, and at every stage — alongside the mechanism — we'll show its boundaries.

We'll show exactly where tokenization breaks arithmetic and why a "fixed" strawberry answer proves nothing. We'll show the mechanism that makes a role in the prompt genuinely change the answer. We'll unpack why temperature=0 doesn't give you reproducibility and what it actually costs to get real reproducibility. On top of that, we'll add the real cost of invisible reasoning tokens, the criterion for choosing between a small model and a giant, and what to replace blind trust in benchmarks with when picking a model.

Seven lines under the goal — one per section we'll cover today: each one will get an answer through a concrete mechanism by the end of the lecture, not through intuition. If at any point it looks like some mechanism doesn't affect practice, call me out on it — we don't cover those today.
