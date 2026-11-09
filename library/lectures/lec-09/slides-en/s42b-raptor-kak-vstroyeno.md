---
id: s42b
local_id: s3-03-3
section: "3. Design and new capabilities"
type: schema_layered
title: "How the surrogate model is built into the Raptor engine"
assertion: "A surrogate, trained on SpaceX engineers' own CFD computations, suggests a configuration almost instantly; the final word stays with the full CFD check and the test stand"
source: "—"
media: ""
media_needed: "Phase 10 (issue #317): a named diagram of the surrogate model's integration (the method's design — on s40) specifically into the Raptor engine configuration, not a general section diagram."
arhitektura:
  blocks:
    - head: "Input: Raptor configuration parameters"
      role: "input"
      lines:
        - "combustion chamber geometry, fuel-feed parameters"
        - "the range of accuracy is set by the CFD training set"
    - head: "Work: the surrogate predicts in seconds"
      role: "work"
      lines:
        - "trained on SpaceX engineers' own combustion CFD computations"
        - "predicts characteristics instead of hours of computation"
    - head: "Output: selection moves on to CFD check and the stand"
      role: "output · bottleneck"
      uzkoe: true
      lines:
        - "selected configurations go through full computation and fire"
        - "accuracy is not guaranteed outside the trained range"
in_bucket: false
status: draft
---

## Visible slide text

**The surrogate's design is on the neighboring slide; here — exactly what it integrates into.** This same fast-evaluation technique works here for a specific Raptor engine, not an abstract example.

**The network does not decide the final outcome.** Selected configurations go through a full CFD computation and a static fire test — the same thing visible in the neighboring photo.

## Speaker notes

The neighboring slide already broke down the surrogate model's design as a general technique: engineers compute expensive CFD simulations in advance, pairs of "parameters → result" become training examples, and the trained network afterward predicts the result almost instantly — but only within the range it saw during training. This slide does not repeat that breakdown; it shows exactly which configuration of which engine this technique is built into at SpaceX.

Input — the parameters of a specific Raptor engine configuration: combustion chamber geometry, fuel-feed parameters. The range of parameters within which the surrogate's prediction can be trusted is set not by the physics of the engine itself, but by which configurations the engineers managed to compute in advance with a full CFD simulation and include in the training set.

Work — the surrogate neural network, maintained by the standing "AI for Vehicle Engineering" team inside SpaceX (the team's existence is confirmed by open job postings and publications, not a marketing claim), is trained on an array of combustion and aerodynamics CFD computations specifically for Raptor. After training, the network predicts combustion characteristics from configuration parameters in seconds — not because it computes physics faster, but because it does not compute physics at all: it statistically reproduces the relationship between input and output, learned from already-computed examples.

Output — this integration's bottleneck is named directly: the surrogate's prediction for Raptor is not the final decision. The wide set of promising variants selected by the surrogate goes on to a full CFD simulation, and then to a static fire test on the stand, the same one shown in the neighboring Starship SN4 photo. It is exactly this test that calibrates the surrogate's accuracy against real combustion physics and screens out configurations the surrogate misjudged by stepping outside what it saw during training.
