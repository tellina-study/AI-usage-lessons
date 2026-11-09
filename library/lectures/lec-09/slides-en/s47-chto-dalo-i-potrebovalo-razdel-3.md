---
id: s47
local_id: s3-08
section: "3. Design and new capabilities"
type: schema_matrix
title: "What it gave and what it required — Section 3"
assertion: "The cost of a model's error grows from an engineer's hours to decisions that touch people entirely unconnected to the model"
source: "—"
media: ""
media_needed: "Cumulative stage map — eight cells filled after three sections. Phase 6."
table:
  headers: ["Breakdown", "Risk of a model error"]
  rows:
    - ["Raptor surrogate", "a few hours lost — filtered out by the stand"]
    - ["Claude/rover route", "a lost planning cycle — filtered out by the digital twin"]
    - ["AIFS/AIGEFS", "the highest cost — a real decision affecting many people"]
    - ["Generative design", "intermediate — an unfamiliar shape is costlier to check"]
in_bucket: false
status: draft
---

## Visible slide text

**Gave:** orders of magnitude more variants, routes, forecasts, or geometries in the same engineer-time.

**Required:** training data from already-computed classical cases — the surrogate does not exist without them — and a separate, non-AI checking step before trusting the result.

## Speaker notes

In sum, the gain is measurable and large in all four breakdowns, but not one of them removes the classical checking step — the model frees up time precisely so that step can be performed more thoroughly, not so it can be skipped.

All four of the section's breakdowns fall at different levels of risk when the model errs. An error in the Raptor surrogate costs the engineer a few wasted hours of a full simulation on an unsuccessful configuration — a noticeable but not catastrophic cost, because the final bench test will filter it out regardless. An error in the model planning the rover's route would, in the worst case, lead to sending a plan that fails the digital-twin check — that is, a lost planning cycle, not a real accident. An error in the weather-forecast model carries the highest cost: an incorrect forecast used for a real decision can affect the actions of many people with no direct connection to the model itself. An error in generative design sits in between: an unsuccessful geometry is filtered out by the final engineering qualification, but the cost of that check itself is higher — an unfamiliar shape takes more time to analyze.

SpaceX's surrogate model is narrowly specialized, predicting a number for an already-given configuration. Claude is a general-purpose model, planning a route over an already-given map. AIFS and AIGEFS are trained specifically for forecasting, but on years of historical data, and forecast the evolution of an already-given state. Generative design is a qualitatively different point: it produces a structure itself that no one specified in advance.

Cumulative stage map: Section 3 adds three new cells — "forecasting × structured data" (Raptor, AIFS/AIGEFS), "planning × multimodal combinations" (rover route), "generation × structured data" (generative design). After three sections, eight cells of the course's grid are filled.
