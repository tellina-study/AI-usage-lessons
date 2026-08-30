---
id: s04a
type: section_divider
section: "Section 1. The prompt and its limits"
duration_min: 0.3
assertion: "Section 1 — what a single call with a good prompt can do and where its ceiling is"
learning_goal: "Section 1 divider + a narrative bridge from the central question to the simplest rung of the ladder"
learning_outcomes: [LO7]
chapter_ref: "§1 [for-slide-s05]"
visual_brief: "The lecture's section_divider template (a giant decorative «1» on the right soft-outline, SECTION 1 + subtitle + 1 narrative bridge line on the left, roadmap bar of 6 cards with the gold marker on Section 1). Unified style with s09/s18."
interaction: none
suffix_insert_after: s04
---

# Visible content

## Title bar
(none — section divider)

## Body
[Right — a giant «1», soft-outline, decorative]

[Left — SECTION 1, 20pt teal]
**SECTION 1**

[Subtitle, 38pt deep]
**The prompt and its limits**

[Narrative bridge line, 18pt italic light]
*We saw the ladder in full — now from the bottom: what a single call can do and where its ceiling is, before complicating anything.*

[Bottom — roadmap bar: 6 cards]
0 Opening · **1 Prompt** *(gold marker — current)* · 2 RAG · 3 Fine-tune · 4 API·agents · 5 Framework

## Speaker notes

We have just posed the central question of the lecture: there is a task and access to a language model — which architecture to choose, and when the right answer is "not AI." And we saw the ladder of six rungs in full, as a map: ordinary code, a single call, RAG, workflow, agent, multi-agent. Now the first substantive section begins, and the logic here is fundamental: we go along the ladder bottom-up, not top-down. Not "what is the most powerful tool that exists," but "is the simplest one enough, and if not — for exactly which task requirement do we climb a rung higher."

The lowest rung involving a model is a single call with a good prompt. Before talking about RAG, fine-tuning, agents, and everything everyone is buzzing about, it is engineering-honest to first understand what a single call can even do, how far it stretches, and where exactly its natural ceiling lies. Because the overwhelming majority of tasks are closed right here, cheaply and predictably, while every climb up the ladder is paid for with growth in cost, latency, and the number of ways to break everything. In this section we will work through four things: why the default is a single call; what Chain-of-thought is and where it helps; why the reasoning the model verbalizes cannot be taken as its real reason; and how to curate the context rather than dumping everything into it. And this is the boundary beyond which the next rung begins.
