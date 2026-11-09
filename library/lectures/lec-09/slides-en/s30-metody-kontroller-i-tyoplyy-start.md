---
id: s30
local_id: s2-03a
section: "2. Teleoperation"
type: schema_pipeline
title: "How the methods are built: the classical controller and the warm start"
assertion: "The classical controller measures, compares, and corrects dozens of times a second; the warm start only suggests a good starting point for it"
source: "—"
media: "assets/razdel-2/astrobee/10-INFOGRAPHIC-warm-start-flowchart.png"
media_needed: "already downloaded (Tier 1). A hero scale was tried (issue #317, task A, `media_hero_target` from 0.48 to 0.20) — it did not help: `place_hero_centered` ties the height of the ENTIRE body column (plates/architecture/text) to the height of the image box itself and at the same time narrows its width, and this slide's architecture diagram (3 boxes) is sized for the slide's full width — even at 0.20 (already below the 40% hero threshold, §5.9) `[architecture]`/`[height]`/`[point size]` remain blocking. Enlarging the image without cropping the block or notes text (forbidden by task bureaucracy) is not possible here — the previous side size is kept."
arhitektura:
  blocks:
    - head: "Controller (feedback)"
      role: "base"
      lines:
        - "measures → compares → computes a command, dozens of times a second"
        - "stability guarantees — strictly within the given conditions"
    - head: "Warm start"
      role: "acceleration"
      lines:
        - "the model suggests a starting point for the trajectory search"
        - "the final guarantee does not change — the controller checks the solution"
    - head: "Predictive latency compensation"
      role: "separate mechanism"
      lines:
        - "the model predicts the scene across the interval of the communication delay"
        - "changes what the operator sees, not what they decide"
in_bucket: false
status: draft
---

## Visible slide text

**The controller's key property.** Provable mathematical stability guarantees — but strictly within the conditions it was designed for in advance.

**A warm start in the worst case** — does not make the final decision any less safe, only spends more iterations refining it.

## Speaker notes

Behind the phrase "a boundary of responsibility set in advance, manual intervention, or a classical controller as the last line of defense" stand two specific mechanisms, different in nature.

The controller is an algorithm that performs the same sequence of three steps on every cycle: measures the current state, compares it with the desired one, and computes a control action. This cycle is feedback: the controller does not predict the entire future motion in advance, but continuously, dozens of times a second, corrects the course based on the observed deviation. No single correction has to be perfect — stability is provided by the cycle's own frequency. The key property is provable mathematical stability guarantees — but strictly within the conditions the controller was designed for in advance.

When the controller's task is not just "hold the course" but find a whole trajectory around obstacles (Astrobee's task), the controller solves the optimization problem iteratively: it starts from an initial guess and gradually improves it. A warm start is when that initial guess is not arbitrary but suggested: a model trained on the statistics of past trajectories offers a starting point already close to a good solution. Critically, the warm start does not change the final safety guarantee — it is simply a better starting point for the same classical mechanism, which still checks the final solution either way. In the worst case, if the warm start is unlucky, the controller simply spends more iterations — no worse off than without it.

The third, separate mechanism is predictive latency compensation. Neither the controller nor the warm start solves the control task here: the trained model directly predicts how the scene will change over an interval equal to the communication delay and overlays the prediction on the operator's video feed — it changes what they see, not what they decide.
