---
id: s42
local_id: s3-03
section: "3. Design and new capabilities"
type: case_study
title: "Example: surrogate models in Raptor engine design"
assertion: "SpaceX's surrogate model sorts through thousands of engine configurations instead of dozens — but the test stand decides the final outcome"
source: "[Job postings and publications of SpaceX's \"AI for Vehicle Engineering\" team](https://job-boards.greenhouse.io/spacex/jobs/8559015002?gh_jid=8559015002)"
media: "assets/razdel-3/raptor/raptor2-full-flow-combustion-cycle-diagram.svg"
media_needed: "already downloaded (Tier 1). A hero scale was tried (issue #317, task A) — the same structural conflict as `s31`/`s32`/`s44`: hero narrows this slide's column of 4 plates below the working width of `PLATES` (`max_per_row=2`, sized for full width), and the blocking `[width]`/`[height]` do not go away even at a target below the 40% hero threshold. The reason is not SVG quality (it's vector, scales without loss) — there simply isn't enough frame area next to the mandatory plates. The previous side size is kept."
graf: "a"
blocks:
  - {label: "Cost of a full CFD simulation", value: "hours of computation per variant", note: "limits the search to dozens of variants per cycle"}
  - {label: "Cost of the surrogate", value: "accurate only within the trained range", note: "outside it — the prediction is inaccurate, and there's no way to find out without a full check"}
  - {label: "Classical mode", value: "full CFD computation, dozens of variants per cycle", note: "a counted baseline"}
  - {label: "Model (SpaceX surrogate)", value: "thousands of variants in the same cycle", note: "prediction in seconds, calibrated against a subset of real CFD cases", key: true}
in_bucket: true
status: draft
---

## Visible slide text

**What moved over.** The engineer now sorts thousands of variants, not dozens — the stand still decides. The model widens the search, not the check.

**Honest gap.** SpaceX names no exact numbers for the surrogate-to-stand funnel.

*Forecasting on structured data.*

## Speaker notes

A full physical CFD simulation of one combustion configuration takes hours of computation. The surrogate model gives a prediction in seconds, but it is trained on a limited set of already-computed examples — and its accuracy is exactly as good as that set allows.

Classical mode (column a): a full CFD computation, hours per variant; the number of variants an engineer manages to consider in one design cycle is limited to dozens.

Model: a surrogate neural network, trained on an array of combustion and aerodynamics CFD simulation data, predicts a configuration's behavior orders of magnitude faster than the full physical simulation. The existence of a standing "AI for Vehicle Engineering" team inside SpaceX is confirmed by open job postings and publications — a working engineering tool, not a marketing claim. Input — engine configuration parameters; output — predicted combustion characteristics. Accuracy is calibrated against a subset of actually computed CFD cases — the surrogate is periodically checked against "real" physics.

Why combustion and aerodynamics specifically are especially well suited to surrogate modeling: a full CFD simulation solves a system of nonlinear differential equations anew for every new geometry — hence hours of computation. The surrogate does not solve these equations at all: it statistically approximates the relationship between input and output, having learned it once.

The classical process has not disappeared, but split into two stages: first the surrogate, as a wide filter, selects the most promising variants out of thousands, then the narrow selected set goes through a full CFD simulation and a bench test. SpaceX does not disclose exact public metrics — an honest gap. Three selection conditions are met, although the confirmation here is weaker than in many other breakdowns: the company does not publish exact numbers on either side.
