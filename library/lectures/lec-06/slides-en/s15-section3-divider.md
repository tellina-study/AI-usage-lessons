---
id: s15
type: section_divider
duration_min: 0.3
assertion: "Part 3 — AI speeds up the computation, it does not replace the physics"
learning_goal: "Visual divider — transition into the surrogate/PINN part"
learning_outcomes: [LO2]
chapter_ref: "frontmatter"
references: []
visual:
  pattern: section_divider_with_progress
  primary: "A large '3' + title + a one-phrase frame + a 7-card progress bar with the current part gold-highlighted"
  illustration:
    type: schematic
    sources:
      - "Self-generated divider layout (large '3' + 7-card progress bar in the Ocean palette)"
    caption: "Section divider — Part 3"
interaction: none
---

# Part 3. AI speeds up the computation, not the physics

## Assertion

Part 3 — AI speeds up the computation, it does not replace the physics.

## Visual

A minimalist divider: 7 horizontal cards for parts 0..6; the current one (3) is highlighted gold (`#F0AB00`). On the left, a large background digit "3" (Primary mid). At the top, a large 36pt title "AI speeds up the computation, not the physics" and a one-phrase frame at 20pt: "a surrogate guesses the solver's output from examples; a PINN smooths out sharp jumps."

## Speaker notes

In the previous part, AI turned out to sit on the left side of the axis — a deterministic optimizer solving an equation. This part is about the class on the right side: surrogate models and PINNs.

In the part on generative design, we solved the equilibrium equation inside the optimization loop without clarifying what that equation actually was. Here we'll first close that gap, starting from the known: FE analysis is familiar at least at the level of a CAD user — break the part into a mesh, get a field of stresses. A surrogate is a neural network that has learned the mapping "geometry and loads → stress fields" on thousands of past computations; it does not solve the equation, it guesses its solution from examples. This is exactly the right side of the load-bearing axis.

Further in this part — the state of the market in 2026, with a critical reading of the claimed speedups, a dissection of PINNs and their main limitation — smoothing out sharp stress peaks at a concentrator — and finally a direct answer to the question "why a surrogate at all": it speeds up enumeration at the search stage, but the final calculation for each selected candidate is done by a certified deterministic solver. The central conclusion of the part — the applicability criterion: a surrogate is valid only within its training domain; extrapolation beyond it gives a silent error.
