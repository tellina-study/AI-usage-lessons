---
id: s66
local_id: s5-08
section: "5. Assembly"
type: schema_matrix
title: "Where AI is flatly not needed"
assertion: "Five concrete situations where a trained model isn't needed or isn't justified — not abstract theory"
source: "—"
media: ""
media_needed: "A 5-row table: criterion × example from the lecture. Phase 6."
table:
  headers: ["Criterion", "Example from the lecture"]
  rows:
    - ["The task is fully described by known physics", "AutoNav/GESTALT, G-FOLD, Terrain-Relative Navigation, NASA IPEx"]
    - ["The decisive leap is in the infrastructure, not the algorithm", "telesurgery over Starlink"]
    - ["The task is new — classical methods simply have nothing to build an alternative from", "COROB-X, telesurgery, orbital data centers"]
    - ["The final check stays classical regardless of the model", "all of Section 3 is 'not enough alone', not 'not needed'"]
    - ["The model creates dependency with no proportionate payoff", "didn't come up in the 13 breakdowns — named honestly"]
in_bucket: true
status: draft
---

## Visible slide text

**Point 5 — honestly not found in this lecture's material.** That doesn't mean such a case doesn't exist in the industry at all — it means it didn't come up within the thirteen cases selected.

## Speaker notes

The course's rule requires explicitly naming where applying a trained model isn't needed or isn't justified, not just showing the successful cases. This lecture's material offers not one general slogan for this, but five concrete, engineering-grounded situations.

The task is fully described by known physics: a rover's geometric navigation, a rocket's landing, descent navigation, and regolith excavation — in all four cases the task has a precise mathematical solution, known to engineers in advance, and a trained model would add unpredictability with no compensating payoff. The decisive technological leap is in the infrastructure, not the algorithm: telesurgery over Starlink is a case with no trained model in the decision loop at all — what changes is the quality of the communication link, not the way decisions get made. The task is new, and classical methods simply have nothing to build an alternative from: COROB-X, telesurgery over satellite, and orbital data centers fall into column c — no classical solution exists for comparison at all, and that by itself is neither an argument for nor against using a model, just an honest statement of novelty.

The final check stays classical no matter how good the model is: this isn't a "AI isn't needed" situation, it's a "AI isn't enough alone" situation — a bench test, a digital twin, classical weather-data assimilation. The model creates dependency that didn't exist before, with no proportionate payoff: this situation simply didn't come up across the thirteen breakdowns — and it's worth saying honestly that the lecture didn't find a clear-cut case of overvalued model adoption in the civilian-space material it covered. That doesn't mean such a case doesn't exist in the industry at all — it means that within the thirteen cases broken down in this lecture, it didn't come up, and that's named honestly rather than glossed over for the sake of symmetry.
