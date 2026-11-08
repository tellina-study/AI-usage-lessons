---
id: s06
type: assertion_visual
duration_min: 3.5
assertion: "Six classes of AI in design fall on one axis — deterministic ↔ probabilistic; the farther right, the fewer the built-in guarantees."
learning_goal: "Skeleton of the taxonomy: one axis, 6 labels with a micro-definition (NOT the full matrix — that's s31)"
learning_outcomes: [LO1]
chapter_ref: "§1.2 — Skeleton of the taxonomy: one axis, six labels"
references: []
visual:
  pattern: schema_axis
  primary: "A horizontal axis 'deterministic → probabilistic' with an arrow; 6 labels along the axis, each with a one-line micro-definition"
  illustration:
    type: schematic
    sources:
      - "Self-generated horizontal axis schema via PowerPoint shapes + connectors (Ocean palette)"
      - "Lucide icons https://lucide.dev — one icon per class (`sliders`, `git-branch`, `gauge`, `scan-eye`, `message-square`, `box`), 32px badge, recolored to Primary mid `#065A82`"
    caption: "Skeleton of the taxonomy: one axis, 6 labels"
interaction: none
---

# Six classes of AI on one axis

## Assertion

Six classes of AI in design fall on one axis — deterministic ↔ probabilistic; the farther right, the fewer the built-in guarantees.

## Visual

Center of the slide — a horizontal axis with an arrow left to right: the left end labeled "deterministic (solves an equation)," the right end "probabilistic (guesses from examples)." Along the axis, left to right, six labels with a one-line micro-definition: 1. Optimization ML / topology optimization — "moves material density, minimizing mass subject to σ ≤ [σ]." 2. Evolutionary / GA — "mutation and selection against a given objective function." 3. Surrogate / PINN — "a neural network that learned input→output from thousands of computations." 4. Computer vision — "a probabilistic image classifier." 5. LLM assistant — "text drafts, explanation of code clauses." 6. Generative AI for geometry — "generates 3D with no physical guarantees." Below the axis, small text: "classes 1–2 — optimization of a given function; 3 — approximation of a solver; 4–6 — probabilistic models." At the bottom, a caption (12pt italic): "The full matrix — at the end of the lecture, once every cell is filled with meaning." A gold marker (`#F0AB00`) on the direction arrow "fewer guarantees →."

## Speaker notes

With the load-bearing axis in hand, let's introduce the six classes of AI found in engineering design. Important: at this stage we are not building the full attribute matrix "class × guarantees × maturity × who is responsible." Presenting such a matrix right away would overload the exposition — half its cells would be terms not yet introduced. So here — a skeleton: one axis and six labels with a one-phrase definition each. The full matrix will be assembled gradually and presented in full at the end of the lecture.

There is one axis — deterministic math against a trained probabilistic model. Left to right: optimization ML and topology optimization — a numerical search that moves the density of material, minimizing mass subject to a stress constraint; this is what marketing calls generative design. Evolutionary and genetic algorithms — a stochastic population-based search against a given objective function. Surrogate models and PINNs — a neural network that learned the mapping "geometry and loads → stress fields" on thousands of past computations. Computer vision — convolutional networks for defect inspection and measurement. LLM assistant — a language model for text artifacts. Generative AI for geometry — diffusion and transformer models that generate 3D with no physical guarantees.

The structure matters: classes one and two — optimization of a given function, physics present as a constraint. Class three — approximation of a solver; physics was in the training data, but not in the model itself. Classes four, five, six — probabilistic models of perception and generation, with no physical law inside at all. The farther right along the axis, the fewer the built-in guarantees, and the higher the cost of error in responsible design.
