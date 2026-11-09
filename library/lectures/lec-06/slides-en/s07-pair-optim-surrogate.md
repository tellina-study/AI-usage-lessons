---
id: s07
type: assertion_visual
duration_min: 3
assertion: "Optimization ML and surrogate/PINN — recognized by the boundary: when yes, when no, what the classical alternative is."
learning_goal: "Recognizing pair 1 (optimization ML + surrogate/PINN): example + boundary + alternative"
learning_outcomes: [LO1]
chapter_ref: "§1.3 — The six classes: recognition, example, boundary"
references: [michell-1904, bendsoe-kikuchi-1988]
visual:
  pattern: matrix
  primary: "2 row cards (Optimization ML / Surrogate-PINN) × 3 columns (When YES · When NO · Classical alternative); Lucide icons per row"
  illustration:
    type: schematic
    sources:
      - "Self-generated 2×3 matrix via PowerPoint shapes (Ocean palette)"
      - "Lucide icons https://lucide.dev — `sliders` (optimization ML), `gauge` (surrogate/PINN), 32px badge, recolored to Primary mid `#065A82`"
    caption: "Pair 1 — recognition, boundary, alternative"
interaction: none
---

# Optimization ML and surrogate/PINN — where the boundary is

## Assertion

Optimization ML and surrogate/PINN — recognized by the boundary: when yes, when no, what the classical alternative is.

## Visual

A table of 2 rows × 3 columns in an Ocean rounded box. Row 1 — "Optimization ML / topology optimization" (icon `sliders`): YES — "reduce mass at a given strength, parts for additive manufacturing"; NO — "when constraints are set incompletely — the optimum fits the wrong statement"; Alternative — "parametric optimization + code-based calculation." Row 2 — "Surrogate / PINN" (icon `gauge`): YES — "fast evaluation of many variants inside the training domain"; NO — "extrapolation beyond training, field discontinuities, certification"; Alternative — "full FEA/CFD with a mesh-convergence check." Each cell ≤2 lines of text, ≥14pt. A gold accent (`#F0AB00`) on the "When NO" column (the most important for judgment).

## Speaker notes

This block is built as a reference: you don't need to hold it all in memory at once — it is assembled as we go through the later parts. At this stage it is enough to go through it once, recognizing the classes. The format itself — "when it fits — when it's not applicable — the classical alternative" — is not decoration: it is the operational form of the course's central idea, and it recurs as an anchor in every part.

Optimization ML and topology optimization fit where you need to reduce mass at a given stiffness or strength, find a non-trivial force scheme, design a part for additive manufacturing, where an "organic" shape is manufacturable. Not applicable when constraints are set incompletely: the optimizer will honestly produce an optimum fitting the wrong statement, and it does not replace a manufacturability check and normative inspection. The classical alternative — parametric optimization with manual selection of sections from a standard range, plus a code-based calculation; for standard structures — a normative calculation with no optimization at all. This class is examined in depth in the part on generative design.

Surrogate models and PINNs fit for fast evaluation of many variants inside the training domain and preliminary screening. Not applicable: extrapolation beyond the training distribution, problems with field discontinuities, final certification calculations. The classical alternative — a full FEA or CFD solver with a mesh-convergence check. This class is examined in depth in the part on surrogates.
