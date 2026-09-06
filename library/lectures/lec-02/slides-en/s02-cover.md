---
id: s02
type: cover
section: "Section 0. Introduction"
duration_min: 0.5
assertion: "Lecture 2. How Modern Large Language Models Work"
learning_goal: "Cover — title + lecture number + subtitle for the new structure (7 sections)"
learning_outcomes: [LO1, LO4, LO6, LO7]
chapter_ref: "§Введение [for-slide-s02]"
visual_brief: "Large '02' in outline gold, title, subtitle 'The inference pipeline — and the boundaries that change engineering decisions' + hero motif (4-stage pipeline icon). No roadmap bar (the map is s02a)."
---

# Visible content

## Title bar
"02 · How Modern Large Language Models Work"

## Body
[Left — large "02" in outline gold (~200pt), below it title 60pt bold #21295C]

**Lecture 2. How Modern Large Language Models Work**

[Subtitle, one line]
*The inference pipeline — and the boundaries that change engineering decisions*

[Right — hero motif: 4-stage pipeline icon (4 circular elements connected by arrows: token / vector / attention weights / distribution)]

## Speaker notes

This is the second lecture of the course. Today we'll look at how a large language model works on the inside: we'll systematize the pipeline's structure and unpack the nuances that directly affect engineering decisions. If you work with models daily, this will refresh the fundamentals and add nuance; if these concepts are new to you, you'll get everything you need.

The lecture's backbone is the inference pipeline: the path of a single request from text to answer. Text gets cut into tokens, tokens turn into vectors, the attention mechanism decides which parts of the context matter, a token gets picked from a probability distribution — and the cycle repeats. Four stages, four sections; a fifth section — new in this version of the course — covers model types and sizes: what they run on and what they can do; a sixth section assembles the pipeline as a whole and wraps up.

Let's move on to the map.
