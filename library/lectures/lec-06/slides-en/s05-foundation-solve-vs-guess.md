---
id: s05
type: assertion_visual
duration_min: 3.5
assertion: "Deterministic optimization solves an equation set by the engineer; a trained generative model guesses from examples and contains no physical law inside it."
learning_goal: "The lecture's load-bearing axis: solving an equation vs. guessing from examples (foundation before taxonomy)"
learning_outcomes: [LO1]
chapter_ref: "§1.1 — The fundamental distinction"
references: []
visual:
  pattern: comparison
  primary: "Two equal columns in an Ocean rounded box: on the left 'SOLVES a given equation,' on the right 'GUESSES from examples.' No formulas"
  illustration:
    type: schematic
    sources:
      - "Self-generated 2-column comparison via PowerPoint shapes (Ocean palette)"
      - "Lucide icons https://lucide.dev — `function-square`/`equal` (solves an equation), `dices` (guesses from examples), 32px inline, recolored to Primary mid `#065A82` and Teal `#028090`"
    caption: "The load-bearing axis: solving an equation vs. guessing from examples"
interaction: none
---

# Solves a given equation vs. guesses from examples

## Assertion

Deterministic optimization solves an equation set by the engineer; a trained generative model guesses from examples and contains no physical law inside it.

## Visual

Two equal-width columns in one Ocean rounded box. Left column, heading "SOLVES a given equation" (Primary mid, icon `function-square`): "The engineer formulates the objective and constraints (equilibrium, strength, volume) · the algorithm numerically searches for a point satisfying the equations · the physical law is present explicitly · same input → same answer · reproducible and traceable." Right column, heading "GUESSES from examples" (Teal `#028090`, icon `dices`): "The model is trained on a corpus of examples · it reproduces 'what an answer usually looks or sounds like' · there is no equilibrium equation inside · an error does not self-diagnose." Below the columns — a gold thesis plate (`#F0AB00` bold): "Any tool labeled 'with AI' is first placed on this axis." No formulas.

## Speaker notes

Before the taxonomy of classes becomes meaningful, we need to establish one distinction — the load-bearing axis of the whole lecture.

Deterministic optimization solves an equation set by the engineer. The engineer formulates an objective function — say, the mass of a part — and constraints: force equilibrium, a strength condition, a volume constraint. The algorithm numerically searches for the point that satisfies these equations and minimizes the objective. Inside this process, the physical law is present explicitly — it is written into the equilibrium equations, solved at every iteration. For the same input data, the algorithm gives the same answer. This is a reproducible, traceable process. Topology optimization, which marketing calls generative design, belongs exactly here.

A trained generative model samples from a distribution learned from data. A diffusion model of geometry or a large language model contains no equilibrium equation inside it. It was trained on a huge corpus of examples and learned to reproduce the statistical regularities of that corpus — that is, "what a part usually looks like" or "how a paragraph of a specification usually sounds." When such a model generates a part, it produces something similar to the training data, not something that satisfies an equilibrium equation. That is why its error does not self-diagnose: the model does not "know" that the geometry does not carry the load, in exactly the same way it does not "know" that the GOST number it named does not exist. This axis is a working tool: on meeting any tool labeled "with AI," the first step is to place it on this axis.
