---
id: s43
local_id: s3-04
section: "3. Design and new capabilities"
type: case_study
title: "Example: Claude/Anthropic plans a rover route"
assertion: "Claude planned the rover's route across Jezero crater — a digital twin checked the plan against 500,000 variables"
source: "[Anthropic + NASA/JPL, Jezero crater, December 8 and 10, 2025](https://www.anthropic.com/features/claude-on-mars)"
media: "assets/razdel-3/claude-jpl/anthropic-hero-first-ai-planned-drive.webp"
media_needed: "already downloaded (Tier 1, Anthropic)."
graf: "b"
blocks:
  - {label: "Cost of manual planning", value: "hours of work, proportional to route length", note: "segment by segment from HiRISE imagery"}
  - {label: "Cost of insufficient checking", value: "an unchecked dangerous stretch", note: "risk of sending the rover onto unverified terrain"}
  - {label: "Classical mode", value: "'roughly twice as fast' — engineers' own estimate", note: "no exact hour count for a route of the same length is in the sources"}
  - {label: "Model (Claude, general-purpose)", value: "456 meters over 2 sols", note: "sum of two drives (210 m + 246 m; one source rounds to ~400 m) in RML format — the same format humans use", key: true}
in_bucket: false
status: draft
---

## Visible slide text

**The final check is a separate, non-AI step.** JPL's digital twin ran the plan through more than **500,000 variables** for compatibility with the flight software.

**The most recent breakdown in the lecture** — December 2025.

*Planning on multimodal data.*

## Speaker notes

This is the most recent breakdown in the lecture: December 8 and 10, 2025, Jezero crater on Mars.

Manual route planning by JPL engineers from HiRISE camera imagery and digital terrain models takes hours of work, proportional to route length. A plan without careful checking carries the risk of sending the rover onto a dangerous stretch.

Classical mode (column b): manual planning is named and described, but the exact number of hours is not given in public sources; engineers estimate the gain as "roughly twice as fast" — named as an estimate, not an invented exact number.

Model: Claude Code analyzed HiRISE orbital imagery and digital terrain models, stitched a route out of segments roughly 10 meters long, placed waypoints, checked and edited them for safety itself, and then converted the final plan into Rover Markup Language — the same command format used by live human operators. The model is general-purpose, not specially trained on Martian data. By outputting the plan in RML, the system plugs into the existing production process without reworking downstream systems — and that is what makes it usable in a real operation, not just a paper demonstration.

The final check is a separate, non-AI step, and that needs to be said explicitly. JPL's digital twin ran the final plan through more than 500,000 telemetry variables for compatibility with the flight software — classical engineering constraint verification, not re-modeling the terrain's physics. The result — a 456-meter route (the exact sum of two drives, 210 m and 246 m; one source rounds it to ~400 m), covered over two sols. Claude is a general-purpose model, not specially trained for this task: the question "what was it trained on" does not apply here, the same as for the classical IPEx automation, but for a different reason. Three selection conditions: the first is met literally, the second unconditionally, the third is column b with an honest caveat.
