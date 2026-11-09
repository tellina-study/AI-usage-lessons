---
id: s03
type: assertion_visual
duration_min: 2.5
assertion: "The lecture's spine is three questions to yourself and six parts: classification across all 6 classes of AI, depth for the three with the highest cost of error."
learning_goal: "Lecture map: 3 anchor questions + 6 parts"
learning_outcomes: [LO1]
chapter_ref: "§Introduction — the three questions; §1.2 promise/delivery"
references: []
visual:
  pattern: roadmap
  primary: "3 anchor questions, large, in an Ocean rounded box + a 6-card horizontal roadmap bar (parts 0–6); the current part is gold"
  illustration:
    type: schematic
    sources:
      - "Self-generated layout (3 questions in an Ocean rounded box + a horizontal 7-card roadmap bar)"
      - "Lucide icons https://lucide.dev — `help-circle` (question), `map` (map), 32px inline, recolored to Primary mid `#065A82`"
    caption: "Lecture map — the spine (3 questions) + 6 parts"
interaction: none
---

# The lecture's spine — three questions and six parts

## Assertion

The lecture's spine is three questions to yourself and six parts: classification across all 6 classes of AI, depth for the three with the highest cost of error.

## Visual

In the upper half — three large anchor questions (24pt bold deep) in one large Ocean rounded box: "1. Deterministic math or a trained probabilistic model? · 2. What is being optimized, and who set the constraints? · 3. Who bears responsibility?" Below the questions — a horizontal roadmap bar of 7 cards: 0 Hook · 1 Foundation + taxonomy · 2 Generative design ≠ generative AI · 3 Surrogate/PINN · 4 Generative AI/LLM · 5 When to say "no" · 6 Synthesis. The current part (0) is gold (`#F0AB00`). At the bottom, small text: "classification — for all 6 classes; depth — for three." The roadmap bar appears here, and from now on, only on section dividers.

## Speaker notes

The central idea of the course, applied to design, is formulated as a requirement you place on yourself. Before trusting a tool with a design decision, you must answer three questions. First: is this deterministic math, giving the same answer for the same inputs, or a trained probabilistic model that samples from a distribution? Second: what exactly is being optimized, and who set the constraints — the engineer, or the data? Third: who bears the legal and engineering responsibility for the result? These three questions recur as an anchor in every part of the lecture.

The lecture is organized into six content parts. First, the foundation and the taxonomy of six classes of AI. Then three parts of deep analysis — generative design as optimization ML, surrogate models and PINNs, generative AI and LLMs. Then the criteria by which an engineer says "no" in advance, and who bears responsibility. And at the end — a synthesis in the form of a decision rule, worked through on a concrete problem.

An important, honest caveat on scope. Every one of the six classes must be nameable and placeable on the axis — that is the skill of classification. But only three classes are examined in depth, with a dissection of their failures — the ones where the cost of error in design is highest. Computer vision and evolutionary algorithms each get one real example and an explicit boundary of applicability — that is enough for recognition. This is a deliberate decision about focus, not a gap: the spine promises classification of six classes, and depth for three.
