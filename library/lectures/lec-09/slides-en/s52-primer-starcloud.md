---
id: s52
local_id: s4-03
section: "4. Space for AI"
type: case_study
title: "Example: Starcloud — the first data-center-class GPU in space"
assertion: "Starcloud-1 is the first data-center-class H100 in space, already serving requests to the Gemma model"
source: "CNBC, 02.11.2025"
media: "assets/razdel-4/starcloud/starcloud-launch-deployment-frame.jpg"
media_needed: "already downloaded (Tier 1)."
graf: "c"
blocks:
  - {label: "Cost of a ground-based data center", value: "cheap to build", note: "limited by the power grid's throughput and climate"}
  - {label: "Cost of an orbital data center", value: "launch and upkeep cost orders of magnitude more", note: "near-continuous sunlight is the main resource gained in return"}
  - {label: "Classical mode", value: "does not exist", note: "'a data center in space' is a new category, not a faster version of the old one", key: true}
  - {label: "Model/automation (Starcloud-1, 60 kg)", value: "launched 02.11.2025", note: "first data-center-class H100 in space; serving requests to the Gemma model"}
in_bucket: true
status: draft
---

## Visible slide text

**An FCC (the US telecom regulator) filing for 88,000 satellites is the company's plan, not a fact.** Series A round of $170 million (03.2026) + $250 million at a $2.3 billion valuation (08.2026).

**What moved over.** The question "where is land and electricity cheaper" moved into the question "where is the sun more continuous."

*Text generation.*

## Speaker notes

The company's name states the direction of its work plainly: Starcloud — literally "a cloud in the sky." The earlier name, Lumen Orbit, is also worth knowing — it shows up in earlier sources.

A ground-based data center is cheap to build but limited by the power grid's throughput and the climate. An orbital data center gets near-continuous sunlight, but launch and upkeep cost orders of magnitude more than a ground-based one.

Classical mode (column c — a task that's genuinely new, with no classical earthly equivalent at all): for "a data center in space," no classical Earth-based equivalent exists — this is a new infrastructure category, not a faster version of the old one.

Model: Starcloud-1 (60 kg, launched November 2, 2025) — the first data-center-class Nvidia H100 GPU in space; already serving real requests to the open Gemma model. Input is an inference task, delivered over the satellite link; output is the computation result — the process itself doesn't differ from Earth's; the difference is in the physical location and power source. Why specifically the open Gemma model: the demonstrator's job is to prove that standard hardware physically withstands orbital conditions and keeps doing the same computing work, without mixing two different questions into one experiment.

The company filed with the FCC for a future constellation of 88,000 satellites — this is a stated plan, not a fact of today. Funding: a Series A round of $170 million (March 2026) and an additional $250 million at a $2.3 billion valuation (August 2026). An honest gap: the sources confirm the fact that requests are being served, but they don't publish latency, bandwidth, or per-request cost statistics. The three selection conditions: the first applies in its purest form — without hardware in orbit, the fact of "computation in space" wouldn't exist at all; the second holds unconditionally; the third is the weakest point of the breakdown — the numerical takeaway is limited to the fact that "the device works."
