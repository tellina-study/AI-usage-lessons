---
id: s30
type: assertion_visual
duration_min: 2.4
assertion: "One problem — lighten a bracket — gives different justified answers for serial milling and for additive manufacturing, worked through the three anchor questions."
learning_goal: "Worked decision (a measurable LO7): a problem → a tree through 3 questions → a justified class + why NOT the others"
learning_outcomes: [LO1, LO2, LO7]
chapter_ref: "§6.1 — Worked decision: lighten the bracket"
references: []
visual:
  pattern: schema_pipeline
  primary: "A decision tree: a problem → 2 branches (serial milling / additive) × 3 anchor questions → different justified conclusions"
  illustration:
    type: schematic
    sources:
      - "Self-generated decision tree via PowerPoint shapes + connectors (Ocean palette)"
      - "Lucide icons https://lucide.dev — `git-fork` (branching), `factory` (serial milling), `printer` (additive), 32px badge, recolored to Primary mid `#065A82`"
    caption: "Worked decision: one problem, two scenarios, different answers"
interaction: none
---

# Lighten the bracket: one anchor question split the answers

## Assertion

One problem — lighten a bracket — gives different justified answers for serial milling and for additive manufacturing, worked through the three anchor questions.

## Visual

At the top — the problem in an Ocean rounded box: "Reduce the mass of a load-bearing bracket." Below — a branch point (icon `git-fork`) into two branches. Left branch, "(a) serial milling" (icon `factory`): Q1 a guarantee is needed → deterministic; Q2 the critical constraint is manufacturability by the cutter — pure topology optimization will produce a non-manufacturable shape; Q3 certified verification + a signature are needed → a conclusion plate: "parametrics + manual topology optimization for manufacturability, with the final step on a certified FEA; NOT generative AI, NOT a surrogate for the final step." Right branch, "(b) additive" (icon `printer`): Q1 the same need for a guarantee → deterministic; Q2 additive removes shape constraints — topology optimization applies at full strength; Q3 the final step is on a certified solver, a surrogate is for enumeration → a conclusion plate: "deterministic topology optimization + a final step on the solver; a surrogate is optional for enumeration; generative AI for geometry — still no." At the bottom, a gold plate (`#F0AB00` bold): "One anchor question (Q2 — what is being optimized and what are the constraints) split the answers."

## Speaker notes

Let's assemble everything into one fully worked decision example. The problem given: reduce the mass of a load-bearing bracket. Consider two production scenarios: a serial part, manufactured by milling on a five-axis machine, and a single part, manufactured additively. Run both branches through the three anchor questions.

Serial milling. First question: a strength guarantee for a serial part is needed — so the base tool is deterministic, and generative AI for geometry drops out right away as probabilistic, with no physical guarantees. Second question: we are optimizing mass subject to a strength constraint — this is the statement of topology optimization, but the critical constraint here is milling manufacturability, and pure topology optimization will produce a shape the cutter cannot manufacture; a surrogate is not applicable for certifying a serial part because of the silent error. Third question: a serial, responsible part requires certified verification and the engineer's signature. Conclusion: the right tool is a classical parametric model plus manual topology optimization for manufacturability, with a final certified FEA.

Additive, a single part. The same first question — the same need for a guarantee, the base tool is deterministic. Second: additive removes most of the shape-related manufacturing constraints, the topology-optimization statement applies at full strength, but the constraints must include the features of printing. Third: if the part is load-bearing, the final calculation is still done by a certified solver, and a surrogate is appropriate for enumerating hundreds of topologies at the search stage, not for the final step. Conclusion: deterministic topology optimization with the full set of printing-related technological constraints, the final step a certified FEA, generative AI for geometry still not used. The same problem gave different justified answers — and both were obtained not by taste, but by walking through the three questions with an explicit "why not the other classes."
