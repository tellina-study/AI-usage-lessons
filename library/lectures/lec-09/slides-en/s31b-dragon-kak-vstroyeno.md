---
id: s31b
local_id: s2-04-3
section: "2. Teleoperation"
type: schema_layered
title: "How Dragon's docking automation is built"
assertion: "Dragon automation's input and output are known from public data; what happens inside — SpaceX does not publicly disclose"
source: "—"
media: ""
media_needed: "Phase 10 (issue #317): diagram of the NASA Docking System's integration. The honest gap in the middle block is not a research shortfall, but exactly the substance of what is known about Dragon (see `s31` notes: 'the control system's architecture is not publicly disclosed by SpaceX')."
arhitektura:
  blocks:
    - head: "Input: laser rangefinders and video"
      role: "input"
      lines:
        - "per public data — LIDAR and cameras on approach to the station"
        - "range and approach angle are measured in real time"
    - head: "Work: internal control logic"
      role: "work · honest gap"
      uzkoe: true
      lines:
        - "the NASA Docking System's architecture is not publicly disclosed by SpaceX"
        - "trained statistically or computed classically, like G-FOLD — unknown"
    - head: "Output: autonomous docking from 220 meters"
      role: "output"
      lines:
        - "routine since 2020, precision at the edge of human motor control"
        - "the crew can take manual control at any moment"
in_bucket: false
status: draft
---

## Visible slide text

**An honest gap — not a research shortfall, but a fact about Dragon.** SpaceX does not publish what happens inside the middle block of this diagram, and the chapter states this directly instead of guessing.

**The outer blocks are known precisely.** Input — sensors per public data; output — routine autonomous docking since 2020, with manual intervention standing ready.

## Speaker notes

This diagram is built differently than its neighbors: the middle block — "work" — is not described in detail here, not because the breakdown was too lazy to find a source, but because the company itself has not publicly disclosed this part. That deserves to be shown honestly, not filled in with a plausible guess.

Input — per public data, Dragon's approach to the International Space Station uses laser rangefinders and a video feed that measure distance, angle, and relative velocity to the docking port in real time (see the neighboring illustration of its actual components). This is the only part of the diagram confirmed openly by technical descriptions.

Work — but exactly what happens between the measurement and the command to the thrusters, SpaceX does not publicly disclose. It is unknown even at the level of principle: whether the control logic is computed classically, like, for example, the G-FOLD algorithm for stage landings, or whether part of the solution is statistically trained on data from past dockings. Calling it a "neural network" or a "classical controller" without a source would mean guessing a fact that is not publicly available — so the lecture's breakdown openly leaves this block as an honest gap.

Output — nonetheless known precisely: starting with the Demo-2 mission in 2020, the automation routinely performs autonomous docking from a distance of 220 meters, with precision at the edge of human motor control. The crew is not taken out of the loop, though: manual control is available to return at any moment, although it is almost never used. This case shows that an "honest gap" is not a sign of a weak breakdown: sometimes the most precise thing you can say about a system's internal design is to call it undisclosed, rather than invent a plausible design in its place.
