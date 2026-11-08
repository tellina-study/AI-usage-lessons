---
id: s18
type: assertion_visual
duration_min: 3.3
assertion: "A PINN smooths out sharp transitions: at a stress concentrator (known from strength of materials), it 'smears' the peak and produces an underestimate — the worst type of error in a strength calculation."
learning_goal: "PINN: hype vs. reality (FAILURE/limitation) — spectral bias at the concentrator; where it is genuinely useful"
learning_outcomes: [LO2]
chapter_ref: "§3.4 — PINN: hype versus reality"
references: [pinn-flaws-sciencedirect-2025, pinn-vs-fem-oxford]
visual:
  pattern: assertion_visual
  primary: "Sketch: the true sharp stress peak at a groove/hole vs. the smoothed, underestimated PINN curve; a gold marker on the underestimate"
  illustration:
    type: schematic
    sources:
      - "Self-generated stress-curve sketch via PowerPoint freeform/connector (Ocean palette): sharp peak vs. smoothed curve"
      - "Lucide icons https://lucide.dev — `activity` (stress peak), `trending-down` (underestimate), 32px inline, recolored to Primary mid `#065A82`"
    caption: "Spectral bias: a PINN smears out the concentrator"
interaction: none
---

# A PINN smears out the stress concentrator

## Assertion

A PINN smooths out sharp transitions: at a stress concentrator (known from strength of materials), it "smears" the peak and produces an underestimate — the worst type of error in a strength calculation.

## Visual

On the left, in an Ocean rounded box — a sketch graph of "stress along a section near a hole/groove": a solid line with a sharp, high peak (caption "true — the concentrator, where the part actually fails") and a dashed, smoothed curve below the peak (caption "PINN — a smeared, underestimated peak"). A gold marker (`#F0AB00`) and an arrow on the gap between the peaks, captioned "an underestimated stress in the dangerous cross-section = an underestimated risk of fracture." On the right — a card, "Other limitations": "does not outperform mature solvers on forward problems, often slower · does not generalize beyond training · opaque on failure · amplifies high-frequency data noise." At the bottom — a plate: "Where a PINN is genuinely useful: sparse data, inverse problems, complex geometry — NOT a replacement for FEM/CFD."

## Speaker notes

A separate subclass — physics-informed neural networks, PINNs. The idea is elegant: a penalty for the residual of a differential equation is added to the network's loss function, so the network trains to "respect" the physics. Marketing presents this as "a neural network that knows physics." The reality, per peer-reviewed surveys, is substantially more modest, and the main limitation is easiest to explain through strength of materials.

From the course on strength of materials you know the stress concentrator: at a hole, a fillet, a groove, the stress field has a sharp local peak — that is precisely where the part fails, and it is precisely for the sake of this peak that the stress concentration factor is computed. A neural network with smooth activation functions easily learns smooth fields, but poorly learns sharp jumps. This property is called spectral bias: the network gravitates toward smoothed solutions. The practical consequence is direct: a PINN trained on a part with a concentrator tends to smear out the stress peak at the hole and produce an underestimated value in the dangerous cross-section. An underestimated stress at a concentrator is an underestimated risk of fracture — the worst possible type of error in a strength calculation.

There are other limitations too. A PINN does not outperform mature numerical methods on standard forward problems and is often slower than solving the same problem with a classical solver; it does not generalize beyond the training scenario; on failure it is opaque — you cannot tell whether the physics, data noise, or network capacity is to blame. Differentiation amplifies high-frequency measurement noise. This is documented in peer-reviewed surveys as a fundamental property of the method, not a flaw in the implementation — it cannot be "fixed" with a bigger network. Where a PINN is genuinely useful: sparse data, inverse problems, complex geometry — a narrow but real niche, not a replacement for a solver on forward problems.
