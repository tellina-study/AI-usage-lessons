---
id: s44a
local_id: s3-05-2
section: "3. Design and new capabilities"
type: case_study
title: "Status: AIFS operational"
assertion: "Official ECMWF graphics mark AIFS's move from a research stage to routine operational status"
source: "[ECMWF](https://www.ecmwf.int/sites/default/files/2025-02/AIFS-operational-690px.jpg?32568)"
media: "assets/razdel-3/aifs-aigefs/ecmwf-aifs-operational-photo.jpg"
media_hero: true
media_hero_target: 0.50
media_caption: "Graphic: ECMWF — official announcement of AIFS operational status"
media_needed: "already downloaded (Tier 1, ECMWF). Honestly: this is not a photo of a room, but an official ECMWF graphic by which the center announced AIFS's move to operational status — added at the owner's instruction (Phase 10, issue #317) as a large illustration for the breakdown."
in_bucket: false
status: draft
---

## Visible slide text

**Not a photo of an office, but an official status.** "AIFS operational" is an ECMWF announcement: the model has left the research stage and now counts as a forecast on par with the classical approach.

**The grid in the background is not decoration.** The pattern repeats the same thing: points on the atmosphere's grid, linked to each other — the design broken down on the neighboring attention slide.

## Speaker notes

This graphic is an official ECMWF material, by which the center marked the AIFS model's move from research development to operational status in 2025. It's worth saying honestly: this is not a photo of a room full of monitors, but a designed announcement — and the word "operational" here is not a marketing epithet but a technical boundary: from this exact moment, AIFS is not a demonstration prototype but part of the daily working weather-forecast service, on par with the classical physical IFS model it supplements.

The pattern in the background — a grid of crossing lines covering the image — visually echoes the design of the model itself: the neighboring breakdown already showed that AIFS treats the atmosphere as a grid of points, where each point "looks at" physically close neighbors through the attention mechanism. The coincidence is not accidental: this kind of graphic is typical of materials where a company illustrates a graph- or grid-based model architecture with an abstract pattern of connections.

The neighboring breakdown already named the numbers behind this status: AIFS computes a 10-day forecast in about 2.5 minutes on a single A100 processor, while the classical physical IFS computation takes hours on a supercomputer with more than a thousand processors. The freed-up compute budget is not wasted — ECMWF and NOAA put it toward the hybrid HGEFS ensemble, broken down nearby.

The honest boundary of "operational" status is also worth naming: neither AIFS nor its relative, AIGEFS, performs its own data assimilation — both receive an already-prepared analysis of the atmosphere from a classical system. Operational status applies to the forecast itself, not to the full data-processing cycle from observation to result.
