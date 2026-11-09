---
id: s33
local_id: s2-06
section: "2. Teleoperation"
type: case_study
title: "Example: Astrobee — ML-assisted piloting"
assertion: "Astrobee demonstrated a 'warm start': the model proposes a trajectory, a classical controller refines it"
source: "[Stanford + NASA, demonstration 12/2025](https://news.stanford.edu/stories/2025/12/ai-robot-international-space-station-autonomous-missions)"
media: "assets/razdel-2/astrobee/03-astrobee-autonomous-maneuver.jpg"
media_needed: "already downloaded (Tier 1, NASA)."
graf: "b"
blocks:
  - {label: "Cost without an assistant", value: "delay and load on the operator", note: "multiple small course corrections from Earth"}
  - {label: "Cost of full autonomy without a check", value: "collision risk", note: "the station's cramped interior space"}
  - {label: "Classical mode", value: "manual remote piloting", note: "named, the number of interventions per maneuver is not published"}
  - {label: "Model (warm start)", value: "TRL5, tested aboard the ISS", note: "Stanford + NASA, 12/2025; the robot was handed to Arkisys in summer 2025", key: true}
in_bucket: false
status: draft
---

## Visible slide text

**Arbitration is not human, but machine.** The classical controller automatically refines or rejects the model's proposal on every cycle, before it becomes a thrust command.

**The only breakdown in the section where the sources name the developing organization (Stanford) separately from the operating organization (NASA).**

## Speaker notes

Fully manual remote control of a free-flying robot creates delay and load on the operator with every small course correction. Full autonomy with no human check is a risk of collision with the station's equipment in its cramped interior space.

Classical mode (column b): manual remote piloting — the number of operator interventions per maneuver without the assistant is not given as an exact number; the reduction in load with the model is also not expressed as a percentage.

Model: a joint Stanford and NASA demonstration, December 2025 — the first demonstration of ML control on the "warm start" principle: the model proposes an initial approximation of the trajectory, which is refined by a classical controller before execution. TRL5, tested in a real operational environment aboard the ISS, not in a lab. Input — current position and target point; output — the proposed trajectory for the controller to check. The robot has flown on the ISS since 2019; in summer 2025 it was handed to the commercial company Arkisys — the warm-start demonstration took place after that handover.

Why a warm start is needed if the controller can solve the task on its own: a controller that has to find a trajectory from scratch either has to search through more options for longer, or accept a coarser solution; the model proposes a starting point significantly closer to a good solution, and the controller is left not to search but to refine — at the same final safety guarantee. Arbitration here is not human but machine: the classical controller automatically refines or rejects the model's proposal. What moved over: the load from small corrections dropped, but the warm start is not full autonomy — the model's proposal still passes through the classical controller. Three selection conditions are met without caveats on the first two, column b on the third.
