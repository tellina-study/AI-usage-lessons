---
id: s09
type: section_divider
duration_min: 0.3
assertion: "Part 2 — Generative design is not generative AI"
learning_goal: "Visual divider — transition into the optimization ML part"
learning_outcomes: [LO1, LO7]
chapter_ref: "frontmatter"
references: []
visual:
  pattern: section_divider_with_progress
  primary: "A large '2' + title + a one-phrase frame + a 7-card progress bar with the current part gold-highlighted"
  illustration:
    type: schematic
    sources:
      - "Self-generated divider layout (large '2' + 7-card progress bar in the Ocean palette)"
    caption: "Section divider — Part 2"
interaction: none
---

# Part 2. Generative design is not generative AI

## Assertion

Part 2 — Generative design is not generative AI.

## Visual

A minimalist divider: 7 horizontal cards for parts 0..6; the current one (2) is highlighted gold (`#F0AB00`). On the left, a large background digit "2" (Primary mid). At the top, a large 36pt title "Generative design is not generative AI" and a one-phrase frame at 20pt: "a deterministic optimizer with math from 1904–1989, not a generative model."

## Speaker notes

We have established the load-bearing axis and placed six classes on it. Now — the first of three parts of deep analysis, and it is about the class with the loudest terminological confusion.

When a CAD system shows a "Generative Design" window and accompanies the result with the words "AI generates the design," what is working under the hood is topology optimization — a deterministic numerical method that, for the same inputs, gives the same result and contains not a single trained generative model. In this part we will dissect the terminological trap and its engineering cost, build the classical lineage of the method from what is already known — from the strength condition in strength of materials and gradient descent — to the industrial standard SIMP, look at real cases from GM and Airbus with the kind of AI identified, at the honest Russian picture, and at the fundamental failure of this part.

The main conclusion of the part will sound like this: "AI generates" means convergence to the optimum of a function set by the engineer, under constraints set by the engineer — not a sample from a learned distribution. This distinction is immunity against the marketing substitution, and the foundation for all the parts that follow.
