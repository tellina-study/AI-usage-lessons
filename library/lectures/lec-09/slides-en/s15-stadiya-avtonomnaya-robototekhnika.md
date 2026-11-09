---
id: s15
local_id: s1-01
section: "1. Autonomous robots in space"
type: norm
title: "The stage: autonomous robotics"
assertion: "Autonomous robotics — deciding and physically acting with no dispatcher at every step"
source: "—"
media: ""
media_needed: "A 5-block diagram (term/data/methods/decision/alternative) — the section's recurring template. Phase 6."
blocks:
  - {label: "Term", value: "autonomous robotics", note: "deciding and acting with no dispatcher at every step of the cycle"}
  - {label: "Data", value: "environment + own state", note: "soil, terrain / position, charge, remaining range"}
  - {label: "Decision", value: "a specific physical action", note: "dig here, drive this route, photograph this object"}
  - {label: "Without automation", value: "a human on the spot", note: "an astronaut in a suit, an engineer on a tether — limited by risk and the length of the excursion", key: true}
in_bucket: false
status: draft
---

## Visible slide text

**This section comes first, and not arbitrarily.** This is the lecture's point of maximum autonomy, against which the rest of the sections can later be compared.

**Three ways of getting data — all onboard the machine itself:** cameras (stereo pairs), LIDAR, inertial sensors.

## Speaker notes

The five parts below are the general template by which each of the lecture's four content sections opens; it will recur almost verbatim in the descriptions of teleoperation, design, and orbital computing, and that's a deliberate choice: once we've learned the template once, we spend our attention on the content from then on, not on the structure of the text itself.

What kind of stage this is. The industry term is autonomous robotics: deciding and physically acting with no dispatcher at each individual step of the cycle. What data gets captured and what question it answers. The machine receives two streams: the state of the environment (soil, terrain, the geometry of the space) and its own internal state (position, charge, remaining range). The question is what to do right now, with no waiting for confirmation from Earth. How this data is captured. Three methods, all onboard: cameras (stereo pairs for recovering depth), LIDAR, inertial sensors. What decision gets made. A specific physical action: dig here, drive this route, photograph exactly this object. How this is decided without automation. The classical alternative is a human physically present: an astronaut in a suit, an engineer on a safety tether. It works, but is limited by the length of a spacewalk and, above all, by physical risk where a machine doesn't risk a life.

Why does this section come first, rather than third or fourth? Maximum autonomy sets the scale: by showing what a machine can do when there's no human in the loop at all, we get a reference point against which we can later measure how much autonomy is actually used in Section 2, and why Section 3 is even needed, where autonomy is replaced by a different kind of contribution — design, not action.
