---
id: s53b
local_id: s4-04-3
section: "4. Space for AI"
type: schema_layered
title: "Suncatcher's second AI case: the model holds formation"
assertion: "Suncatcher has a second, separate AI use case: a model holds the formation of dozens of satellites collision-free in real time — not answering a user's request"
source: "[Google, Project Suncatcher preprint — Supplementary Information, Orbital dynamics modeling](https://services.google.com/fh/files/misc/suncatcher_paper.pdf)"
media: ""
media_needed: "No image — a control mechanism, not a physical object, the same logic as `s50a`. Phase 10 (issue #317): text and scope follow `chapter-part3.md`, §4.4, the paragraph 'Suncatcher's second AI use case' (added to the chapter in commit 4a165734a5)."
arhitektura:
  blocks:
    - head: "Input: the formation's orbital dynamics"
      role: "input · not AI"
      lines:
        - "position and velocity of every satellite in the formation, in real time"
        - "numerical integration of the equations of motion — classical mechanics"
    - head: "Work: differentiable optimization of the formation"
      role: "work"
      lines:
        - "objective function — the formation's geometry: a cluster ~1 km across with no collisions"
        - "gradient — adjoint-state methods"
        - "reverse-mode automatic differentiation (AD) in JAX — into the model"
    - head: "Output: a maneuver command for every satellite"
      role: "output"
      lines:
        - "a corrected maneuver command for every satellite in the formation"
        - "keeps the cluster at a radius of about 1 km with no collisions"
in_bucket: false
status: draft
---

## Visible slide text

**Suncatcher's second AI case isn't inference — it's formation control.** The tighter the formation, the higher the bandwidth of the laser links between satellites.

**The mechanism is differentiable optimization, not prediction from examples.** The gradient runs backward through the motion's integration — into the model's parameters, the same way neural networks are trained.

## Speaker notes

Unlike Starcloud, Suncatcher has a second AI use case, separate by nature. It's broken down on this slide on its own, not dissolved into the general formula "the same thing as Starcloud": this isn't a variation on the inference task already covered — it's a task of a different type altogether, not computing an answer to a ready-made request, but controlling the physical position of many moving bodies in real time.

Input: to hold formation, the system needs to know the position and velocity of each satellite in the formation at every moment — this is computed by numerically integrating the equations of motion, classical celestial mechanics with no AI in it at all.

Work: according to the preprint's supplementary materials (Supplementary Information, section "Orbital dynamics modeling"), the approach is described as differentiable optimization, not prediction from pre-labeled examples. An objective function is set, whose minimum describes the desired formation geometry — a cluster about 1 km in radius in which the satellites won't collide. This function's gradient is propagated backward through the motion integration itself using adjoint-state methods, and then reverse-mode automatic differentiation (AD) — the same mechanism neural networks are trained by, and whose implementation, per the preprint's text, is substantially simplified by the JAX tool — carries the gradient into the parameters of the flight-control model itself, which is being trained.

Output: a corrected maneuver command for every satellite in the formation. The official preprint describes the result in these words: "An ML-based flight control model enables the satellites to maintain close flight proximity while avoiding collisions" — a flight-control model keeps the satellites in a tight formation while simultaneously preventing them from colliding with each other.

The difference from Starcloud here is fundamental, not a matter of degree — and it's worth naming directly: there, the model is someone else's finished network, answering a single user request via inference, one pass from input to answer, and not a single one of its weights changes on board. Here, a trainable model itself, in real time, controls the physical position of dozens of moving objects — this isn't a variation on the inference task, it's a separate task of control and optimization by nature.
