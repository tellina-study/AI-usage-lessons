---
id: s28
local_id: s2-02
section: "2. Teleoperation"
type: norm
title: "Stage: teleoperation"
assertion: "Teleoperation — controlling a system from a distance, where the decision stays with the human"
source: "—"
media: ""
media_needed: "5-block diagram, the same template as §1.1. Phase 6."
blocks:
  - {label: "Term", value: "teleoperation", note: "controlling a system from a distance, the decision stays with the human"}
  - {label: "Data", value: "real-time video feed + telemetry", note: "the question: how long a human can stay in the loop at a given delay"}
  - {label: "Decision", value: "confirm or cancel an action", note: "as far as the communication delay allows"}
  - {label: "Without teleoperation", value: "a human physically on site", note: "safer in terms of control, requires presence and risk", key: true}
in_bucket: false
status: draft
---

## Visible slide text

**This section follows Section 1 for a reason:** it shows where the boundary of autonomy has not yet been crossed — a human holds it deliberately, not by default.

## Speaker notes

The five parts below continue the general schema opened for Section 1: term, data and question, how the data is obtained, the decision made, the alternative. Here the schema follows an unusual order of presentation — after the scene, not before it.

What kind of stage this is. The industry term is teleoperation: controlling a system from a distance, where the decision stays with the human. What data is obtained and what question it answers. The human receives a real-time video feed and telemetry. The question is how long a human can stay in the decision-making loop given the communication delay and the speed at which events unfold. How this data is obtained. A direct telemetry channel — radio or laser link — and an operator console with video and a joystick or touch interface. What decision gets made. The human confirms or cancels the system's action in real time, as far as the delay allows. This section comes after Section 1 in the lecture for a reason: it shows where the boundary of autonomy has not yet been crossed — a human holds it deliberately, not by default, not because no one bothered to build a more autonomous system. How this decision is made without teleoperation. The classical alternative is fully manual execution of the task by a human physically present on site: an astronaut personally pilots the ship or performs the operation. Safer from the standpoint of direct control, but requires physical presence and the risk that comes with it.
