---
id: s44b
local_id: s3-05-3
section: "3. Design and new capabilities"
type: schema_layered
title: "Where AIFS and AIGEFS stand in the forecast pipeline"
assertion: "Without classical data assimilation, AIFS and AIGEFS simply have no input — the model computes the forecast, but does not assemble the picture of the atmosphere itself"
source: "—"
media: ""
media_needed: "Phase 10 (issue #317): a diagram of AIFS/AIGEFS's integration into the whole forecast pipeline — a different angle than slide s41 ('attention on the weather grid'), which breaks down the mechanism INSIDE the model. Here it breaks down WHERE the model stands among non-AI steps."
arhitektura:
  blocks:
    - head: "Input: classical data assimilation"
      role: "input · not AI"
      uzkoe: true
      lines:
        - "4D-Var (ECMWF) or GDAS (NOAA) fold observations into an atmospheric analysis"
        - "without this step the model simply has no input"
    - head: "Work: transformer / graph network"
      role: "work"
      lines:
        - "AIFS — a 16-layer transformer with an attention mechanism"
        - "AIGEFS — a message-passing graph network on the GraphCast architecture"
    - head: "Output: a weather forecast to weather services"
      role: "output"
      lines:
        - "AIFS — ~2.5 minutes, AIGEFS — under 4 minutes, on one A100"
        - "NOAA combines AIGEFS with the classical model into an ensemble, it does not replace it"
in_bucket: false
status: draft
---

## Visible slide text

**This is a different question than on the attention slide.** There — how the attention mechanism works inside the model. Here — where the model itself stands among the steps AI does not perform at all.

**The honest boundary is at the input, not the output.** The model does not assemble the picture of the atmosphere itself: without classical data assimilation, there simply is no input for it to use.

## Speaker notes

The neighboring slide already broke down how the attention mechanism inside AIFS is built — the same principle as a language model, except here the neighbors are not tokens but points on the atmosphere's grid. This slide asks a different question: where does the forecast model itself stand among all the steps needed for the forecast to exist at all, and which of those steps AI does not perform.

Input — this is where the honest boundary stands, and it needs to be stated directly rather than quietly skipped: neither AIFS nor AIGEFS performs its own data assimilation. Both models receive an already-prepared analysis of the atmosphere from a classical system — 4D-Var at ECMWF, GDAS at NOAA — which folds heterogeneous observations (from satellites, weather stations, radiosondes) into a consistent picture of the atmosphere's current state. Without this classical step, the forecast model simply has no data to start computing from.

Work — AIFS's architecture is a 16-layer transformer with a sliding attention window, trained on 38 years of ERA5 reanalysis data; AIGEFS is a message-passing graph network based on the GraphCast architecture, around 36.7 million parameters. Both architectures are encoder–processor–decoder, where the processor performs the main computational work of the forecast.

Output — AIFS computes a 10-day forecast in about 2.5 minutes on a single A100 processor, AIGEFS in under 4 minutes. But even at the output, the model's place is not final: NOAA does not replace the classical GEFSv12 with the new model, but combines 31 runs of AIGEFS with 31 runs of the classical model into a single hybrid HGEFS ensemble of 62 members — the model takes its place in the pipeline, it does not retire the rest.
