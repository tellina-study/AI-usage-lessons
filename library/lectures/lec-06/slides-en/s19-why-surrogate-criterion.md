---
id: s19
type: assertion_visual
duration_min: 2.6
assertion: "A surrogate speeds up the evaluation of hundreds of variants at the search stage; the final calculation for the selected candidates is done by a certified deterministic solver."
learning_goal: "Why a surrogate at all + the applicability criterion (silent error out-of-domain) + Russia; cascade: ≤3 numbers / ≤4 names"
learning_outcomes: [LO2]
chapter_ref: "§3.5 — Why a surrogate at all: the applicability criterion and Russia"
references: [logos-rosatom, cml-bench-spbpu]
visual:
  pattern: schema_pipeline
  primary: "Pipeline 'hundreds of variants → the surrogate screens them → 5–10 candidates → a certified solver computes the final result' (RIGHT_ARROW); a gold criterion"
  illustration:
    type: schematic
    sources:
      - "Self-generated pipeline via PowerPoint shapes + RIGHT_ARROW (Ocean palette)"
      - "Lucide icons https://lucide.dev — `layers` (hundreds of variants), `filter` (the surrogate screens), `shield-check` (certified solver), 32px badge, recolored to Primary mid `#065A82`"
    caption: "Why a surrogate: it speeds up enumeration; the final result — on the solver"
interaction: none
---

# A surrogate for enumeration; the final result on a certified solver

## Assertion

A surrogate speeds up the evaluation of hundreds of variants at the search stage; the final calculation for the selected candidates is done by a certified deterministic solver.

## Visual

A horizontal pipeline in an Ocean rounded box (RIGHT_ARROW between blocks): "Hundreds of variants at the search stage (what if the rib is thicker, what if a different material)" (icon `layers`) → "The surrogate runs them in minutes, screens out the obviously weak ones" (icon `filter`) → "5–10 candidates" → "A certified deterministic solver computes the final result" (icon `shield-check`, gold frame `#F0AB00`). Below the pipeline — a gold criterion plate (bold, 16pt): "A surrogate is valid only inside its training domain; extrapolation = a silent error (the model does not report that it left the domain)." At the bottom, on one line (12pt): "Russia: 'Logos' (Rosatom) — surrogates in the wrapper, not inside the solver's kernel; CML-Bench (SPbPU) — an accumulated archive → an assistant." No more than three numbers and four names on the slide.

## Speaker notes

After dissecting PINNs, a natural question arises: if a surrogate guesses, and a PINN smears things out, why does this part even exist? The answer is direct and constructive. At the search stage, a designer evaluates dozens and hundreds of variants: what if the rib is thicker, what if the boss is moved, what if a different material is used. Computing each variant with a full certified FEA is expensive in time. Here a surrogate is in its place: run hundreds of bracket variants in minutes, screen out the obviously weak ones, keep five to ten candidates. But — and this is the criterion — the final calculation for each selected candidate is done by a certified deterministic solver. A surrogate speeds up enumeration at the search stage; it does not produce a certifiable result.

The central conclusion of the part is the applicability criterion. A surrogate is valid only inside the domain it was trained on. Extrapolation beyond it — a new regime, a new material, geometry out of distribution — gives a silent error: the model does not report that it has left its domain of applicability, it simply confidently produces a wrong number. The phrase "silent error" is key here: the absence of an error message does not mean correctness. That is why a surrogate is not admissible where a guarantee is needed — certification, a calculation with a safety factor — and is admissible where a fast preliminary screen followed by precise verification is needed.

In Russia, the CAE package "Logos" is the flagship of import-independent supercomputer simulation; native neural-network solvers inside its kernel are not confirmed in open sources — surrogates are applied in the wrapper of the ecosystem, not inside the solver itself. The CML-Bench platform is an example of an accumulated engineering knowledge base feeding a system of assistants: the same pattern of "archive of computations → surrogate." Claims of the "a thousand times" kind are narrow special cases that ignore the cost of the training archive.
