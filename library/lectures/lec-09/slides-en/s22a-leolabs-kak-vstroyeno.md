---
id: s22a
local_id: s1-05a-2
section: "1. Autonomous robots in space"
type: schema_layered
title: "How LeoLabs is built into the warning system"
assertion: "The model decides what to observe next; whether to maneuver or not is decided by the specific satellite's operator, not LeoLabs"
source: "—"
media: ""
media_needed: "No illustration — an honest gap: no asset for LeoLabs was found either in the main Tier 1–6 pass over Section 1, or on a repeat attempt (see slide s22's own `media_needed`). This integration diagram was built with no photo, from the case study's text alone."
arhitektura:
  blocks:
    - head: "Input: a growing catalog of objects"
      role: "input"
      lines:
        - "11 radars at 7 sites, detection of objects from 2 cm"
        - "the orbital-debris catalog grows with every pass"
    - head: "Work: a prioritization model"
      role: "work"
      lines:
        - "ranks which object is most worth the radar observing next"
        - "predicts the probability of getting a good-quality measurement"
    - head: "Output: a close-approach warning"
      role: "output · an honest boundary"
      uzkoe: true
      lines:
        - "up to 400% more warnings than the previous mode"
        - "whether to maneuver or not is decided by the satellite's operator, not LeoLabs"
in_bucket: false
status: draft
---

## Visible slide text

**The model doesn't predict a collision directly.** It solves a different task — where to point the radar next, given limited observation time.

**The boundary is stated directly, with no guesswork.** LeoLabs issues the warning; the decision to maneuver belongs to the specific satellite's operator, not to LeoLabs.

## Speaker notes

The LeoLabs case study on the neighboring slide has already named the numbers — up to 400% more warnings, 11 radars at 7 sites. This diagram shows exactly how the chain is built inside: what's at the input, what the model does, and where the boundary of its responsibility ends.

The input is a growing catalog of low-Earth-orbit objects, gathered by LeoLabs's 11 operating radars at 7 sites, with detection from 2 centimeters. The catalog grows with every radar pass: new debris, new satellites, new measurements of existing objects.

The work: LeoLabs's own model doesn't predict a collision directly. It solves a different task: given limited radar observation time, which of the many objects in the catalog is most worth observing next, in order to get a good-quality measurement exactly where the risk of a close approach is higher. This is a prioritization task, not a trajectory-prediction task.

The output is a close-approach warning, issued up to 400% more often than the classical mode, with its less frequent imaging and coarser detection threshold. The boundary here isn't an accidental oversight but something stated explicitly on the neighboring case study too: LeoLabs only warns. The decision to maneuver — and whether it's even worth spending fuel on a maneuver at all — stays entirely with the specific satellite's operator. What share of the warnings issued led to an actual maneuver is something sources don't publish — the same honest gap named on the neighboring slide.
