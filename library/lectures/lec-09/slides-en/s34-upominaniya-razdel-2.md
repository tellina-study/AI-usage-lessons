---
id: s34
local_id: s2-07
section: "2. Teleoperation"
type: norm
title: "Mentions from Section 2"
assertion: "Telesurgery over Starlink works at a delay of ~130 ms — but there is no trained model in the decision loop at all"
source: "[University of Bristol](https://phys.org/news/2025-11-robotic-exosuit-trousers-boost-astronauts.html) · ESA · [PMC (telesurgery)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12712185/)"
media: ""
media_needed: "List, each line is one observation. Phase 6."
in_bucket: true
status: draft
---

## Visible slide text

- **Exosuit with "artificial muscles"** (Bristol) — tested only in Earth analog missions, **never flew** in space
- **ESA exosuit** — force feedback: the operator feels the tool's resistance physically, not just visually
- **Earth–ISS delay** — a fraction of a second, the lower bound of the range that Section 1 stretches out to 22 minutes
- **Telesurgery over Starlink** — delay ~130 ms; lung resection on an animal model, performed remotely; **there is no trained model in the decision loop at all**

## Speaker notes

These four mentions hold up the side of the section not covered by the three detailed breakdowns: two show teleoperation through a physical, wearable shell, the third brings the delay scale back to Section 1's numbers, and the fourth is an honestly kept compact case where the decisive leap was made not by a model but by communication infrastructure.

An exosuit with "artificial muscles" (University of Bristol) for teleoperating a manipulator robot outside the station — tested only in Earth analog missions, reduces operator muscle fatigue; never flew in space. The ESA exosuit is a different design for the same purpose: a teleoperator on the station controls an external robot through force feedback, feeling the tool's resistance physically.

The Earth–ISS communication delay is a fraction of a second, the lower bound of the same range that Section 1 stretches out to twenty or more minutes at Martian distances.

Telesurgery over Starlink — the decisive leap was made by communication infrastructure, not by a model. Starlink provides a delay on the order of ~130 milliseconds, which proved sufficient to perform a lung resection on an animal model remotely: the surgeon controls the instrument through a console directly, and there is no trained model in the decision loop at all — automation here is limited to transmitting the signal. There is no classical Earth-based analog for "telesurgery over a low-orbit satellite" (column c): terrestrial telesurgery over fiber-optic cable is a different delay and different infrastructure. This case stands not as a weak fourth breakdown, but as an explicit example of where the boundary of AI's application passes right by the task altogether: the decisive leap belongs to communication infrastructure, and calling this an application of artificial intelligence would be a substantive error.
