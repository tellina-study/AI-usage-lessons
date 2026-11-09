---
id: s35
local_id: s2-08
section: "2. Teleoperation"
type: schema_matrix
title: "What it gave and what it required — Section 2"
assertion: "From automation on an explicitly carved-out piece — to automation on every cycle, but not the final word"
source: "—"
media: ""
media_needed: "Cumulative stage map — five cells filled after two sections. Phase 6."
table:
  headers: ["Grid cell", "Breakdown"]
  rows:
    - ["Forecasting × video", "Predictive latency compensation — the first appearance of the 'video' modality"]
    - ["Planning × structured data", "Astrobee"]
    - ["— (architecture not disclosed)", "Dragon"]
    - ["— (no trained model at all)", "Telesurgery over Starlink (mention)"]
in_bucket: false
status: draft
---

## Visible slide text

**Gave:** access to operations without physical presence at the event — the surgeon stays on Earth, the operator at the console, the crew a witness at the moment of docking.

**Required:** being willing to accept that not everything is routine practice (latency compensation is only an analog); deciding in advance exactly when automation acts without confirmation.

## Speaker notes

In sum, teleoperation expands where a task can physically be performed, but does not remove the dependence on the communication link — it only changes what exactly depends on that link: not the human's presence, but the channel's stability and delay.

The section's three detailed breakdowns fall into a clear order by the role automation plays within them. With Dragon, automation performs the final, most precise part of the task entirely, but on a pre-defined segment outside of which the human controls. With predictive latency compensation, the trained model compensates for the perception of the delay itself throughout the whole task, without making decisions for the operator — a research stage, not routine practice. With Astrobee, automation is built into every control cycle, proposing a draft that a classical controller refines before it becomes a command. Next to these three — compactly, but honestly — stands the extreme, fourth case of the spectrum: with telesurgery over Starlink, there is no automation in the decision at all, only communication infrastructure carrying the human's decision. From "no automation at all" through "automation compensates perception" and "automation on a pre-defined segment" to "automation on every cycle, but not the final word" — this is a gradual escalation that directly foreshadows the transition to Section 3, where the model's role grows further still.

Cumulative stage map: to the three cells filled after Section 1, Section 2 adds two new ones. For Dragon, the architecture is undisclosed (the cell is conditionally empty). For predictive latency compensation, the "forecasting × video" cell is filled — the first appearance of the "video" modality in the entire grid. For Astrobee, the "planning × structured data" cell is filled. After two sections, five cells are filled, and it is clear that maximum autonomy and the teleoperation spectrum together cover noticeably more task types than Section 1 alone.
