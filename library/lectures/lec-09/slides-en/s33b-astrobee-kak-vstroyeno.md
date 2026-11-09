---
id: s33b
local_id: s2-06-3
section: "2. Teleoperation"
type: schema_layered
title: "How the warm start is built into Astrobee"
assertion: "Astrobee flies with no tether, on fans; the model only suggests a route through the station's module, the final check rests with the classical controller"
source: "—"
media: ""
media_needed: "Phase 10 (issue #317): a named diagram of the warm start's integration (the method's design — on s30) specifically into Astrobee's free flight — a specific robot, not a general section diagram."
arhitektura:
  blocks:
    - head: "Input: free flight inside the station's module"
      role: "input"
      lines:
        - "current position and target point, fans instead of a tether"
        - "the space is cramped — risk of collision on a maneuver"
    - head: "Work: the model proposes, the controller refines"
      role: "work"
      lines:
        - "the model, on statistics of past trajectories, suggests a start"
        - "the feedback controller refines it before the maneuver"
    - head: "Output: thrust command to the fans"
      role: "output · bottleneck"
      uzkoe: true
      lines:
        - "the controller carries the final safety guarantee"
        - "an unlucky start only costs more iterations, no worse off"
in_bucket: false
status: draft
---

## Visible slide text

**The warm start's design is on the neighboring slide; here — what it is built into.** This mechanism suggests the starting point of the trajectory specifically for Astrobee's free flight inside the station's cramped module.

**The final decision is not the model's.** The controller checks and refines the proposed trajectory before every command to the fans.

## Speaker notes

The neighboring slide already broke down the warm start's design as a general technique: a feedback controller measures, compares, and corrects dozens of times a second, while the model only suggests a good starting point for the trajectory search. This slide does not repeat that breakdown — it shows exactly which device and exactly which task it is built into for Astrobee.

Input — Astrobee is a cube-shaped body roughly 32 centimeters on a side, with no tether and no mechanical attachment to the station; internal fans that push air out through controllable nozzles on the sides of the body keep it aloft and move it. The task's input is the robot's current position and a target point inside the "Kibo" module, a cramped space full of equipment, where the risk of collision exists on every maneuver.

Work — here the controller needs not just to hold a course, but to find an entire trajectory through this cramped space around obstacles. A model trained on the statistics of Astrobee's past trajectories (the robot has flown on the ISS since 2019, without constant manual control, which is what allowed this statistics to accumulate) proposes an initial approximation of the route — already close to a good solution, not an arbitrary point. The classical feedback controller accepts this approximation as the starting point for its own iterative search and gradually refines it.

Output — a corrected thrust command to the fans, which the controller executes only after its own check. The final safety guarantee of the maneuver does not change because the start was suggested by the model: if the suggestion turns out unlucky, the controller simply spends more iterations refining it — the result will be no worse than if there had been no warm start at all.
