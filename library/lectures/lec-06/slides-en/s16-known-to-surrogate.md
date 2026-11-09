---
id: s16
type: assertion_visual
duration_min: 3
assertion: "FE analysis solves the equilibrium equations on a mesh; a surrogate does not solve them — it guesses the stress field from thousands of past computations."
learning_goal: "From KNOWN FE analysis to a surrogate; Galerkin/K·u=f mentioned in one phrase only (the derivation is in the chapter)"
learning_outcomes: [LO2]
chapter_ref: "§3.1 — From known FE analysis to a surrogate; §3.2 — the weak form (one phrase)"
references: [turner-clough-1956]
visual:
  pattern: comparison
  primary: "Two columns in an Ocean rounded box: 'The FE solver solves K·u=f' vs. 'The surrogate guesses from examples'"
  illustration:
    type: schematic
    sources:
      - "Self-generated 2-column comparison via PowerPoint shapes (Ocean palette)"
      - "Lucide icons https://lucide.dev — `grid-3x3` (mesh/solver), `gauge` (surrogate), 32px inline, recolored to Primary mid `#065A82` / Teal `#028090`"
    caption: "From known FE analysis to a surrogate"
interaction: none
---

# FE analysis solves an equation — a surrogate guesses from examples

## Assertion

FE analysis solves the equilibrium equations on a mesh; a surrogate does not solve them — it guesses the stress field from thousands of past computations.

## Visual

Two columns in an Ocean rounded box. Left, heading "FE solver" (icon `grid-3x3`, Primary mid): "part → finite-element mesh → solves a system of equilibrium equations → stress field · proven, traceable, deterministic math · error controlled by a mesh-convergence check." Right, heading "Surrogate" (icon `gauge`, Teal `#028090`): "learned the mapping 'geometry and loads → stresses' on thousands of past computations → an answer almost instantly · does NOT solve the equation, guesses from examples · trained offline, in advance, on an expensive archive." Below the columns — a gold plate (`#F0AB00`): "under the hood is a system of equilibrium equations; the surrogate does not solve it." The formal derivation of the system (the weak Galerkin form) is not put on the slide — it is in the chapter.

## Speaker notes

In the previous part we solved the equilibrium equation inside the optimization loop without clarifying what equation it was. Let's close the gap, starting from the known. FE analysis — the finite element method — is familiar at least at the level of a CAD user: a part is broken into a mesh of finite elements, loads and fixtures are applied, and the program produces a colored picture of the stress field. In substance, the solver takes a load vector, solves a system of linear equilibrium equations for displacements, and from the displacements computes strains and stresses. This is proven, traceable, deterministic math, more than sixty years old, and its accuracy is controlled by a mesh-convergence check as the mesh is refined.

A surrogate model, also called a metamodel, is a neural network that has learned the mapping "geometry and loads → stress field" on thousands of past FE computations and now produces an answer almost instantly. The key word is learned. The surrogate does not solve the system of equilibrium equations; it guesses its solution from the examples it was trained on. This is exactly the right side of the load-bearing axis: guessing from learned examples. The difference between a surrogate and a generative model is that the surrogate's training examples were physically correct — computed by a certified solver — so within what the surrogate has "seen," it is reliable. Beyond that, it is not.

Also remember when the training happens: offline, in advance, on an archive of thousands of expensive computations, not at the moment of use. This matters for the method's economics: for a surrogate to be useful, someone must first pay for thousands of runs of the exact solver. Under the hood there is still a system of equilibrium equations — its derivation through the weak form is dissected in detail in the chapter; the surrogate does not solve this system, it only predicts the result faster and approximately.
