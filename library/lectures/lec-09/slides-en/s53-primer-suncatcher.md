---
id: s53
local_id: s4-04
section: "4. Space for AI"
type: case_study
title: "Example: Google Project Suncatcher"
assertion: "Google Project Suncatcher is a satellite with four TPUs, with a plan for 81 spacecraft in a single laser-linked cluster"
source: "[CNN, 01.10.2026](https://www.cnn.com/2026/10/01/science/google-ai-data-center-satellites-space)"
media: "assets/razdel-4/suncatcher/suncatcher-transporter18-liftoff.jpg"
media_needed: "already downloaded (Tier 1)."
graf: "c"
blocks:
  - {label: "Cost", value: "the same logic as Starcloud", note: "a different company, a different chip"}
  - {label: "Classical mode", value: "does not exist", note: "the same gap, for the same reason"}
  - {label: "Model/automation (satellite + 4 TPUs)", value: "launched 01.10.2026", note: "first AI model response from a data-center-class TPU in orbit", key: true}
  - {label: "Company's plan", value: "81 satellites in a cluster ~1 km in radius", note: "laser inter-satellite links; partnership with Planet Labs — 2 satellites by early 2027"}
in_bucket: true
status: draft
---

## Visible slide text

**The engineering sense of the name:** "sun catcher" — not cooling, not radiation shielding, but the continuity of sunlight as the main resource.

**The company openly admits:** some engineering decisions can only be verified in real orbital conditions, not on Earth.

*General-purpose generation/inference — an infrastructure demonstrator, not tied to a single task.*

## Speaker notes

The project's name states the engineering essence of Google's choice plainly: "suncatcher," and the name itself honestly lays out the priority — not cooling, not radiation shielding, but the continuity of sunlight as the main resource that gives the whole design its point.

The cost on both sides and the classical mode (column c) are the same logic as Starcloud, carried out by a different company with a different chip: the same gap in a classical equivalent, for the same reason.

Model/automation: a refrigerator-sized satellite equipped with four tensor processing units, launched on a Falcon 9 rocket on October 1, 2026 — the first recorded AI model response from a data-center-class TPU in orbit. The company's plan is to grow the constellation to 81 satellites, joined into a cluster about one kilometer in radius via laser inter-satellite links; a partnership with Planet Labs calls for launching two satellites by early 2027.

Why specifically laser inter-satellite links: they carry significantly more data per unit of time at the same distances than a radio-frequency channel — a cluster running distributed computation needs exactly that kind of high bandwidth between its own nodes. The company openly admits to technical difficulties: some engineering decisions can only be verified in real orbital conditions, not on Earth — an honest admission of the limit of what can be simulated in advance.

What moved over: competition for where to put the computing moved from the Earth-based electricity market to the orbital sunlight market — the same shift in criterion as Starcloud's, confirmed independently by a second major technology company. The three selection conditions are the same as Starcloud's: the first applies in its purest form, the second holds unconditionally, the third is the weakest point — the numerical takeaway is limited to the fact that it works.
