---
id: s43b
local_id: s3-04-3
section: "3. Design and new capabilities"
type: schema_layered
title: "How Claude is built into route planning"
assertion: "Claude plans and checks its own plan for safety, but the final check before flight belongs to the digital twin, not to Claude"
source: "—"
media: ""
media_needed: "Phase 10 (issue #317): a diagram of Claude/Anthropic's integration into the JPL process — focused on exactly where in the pipeline the final-check threshold sits."
arhitektura:
  blocks:
    - head: "Input: HiRISE imagery and terrain models"
      role: "input"
      lines:
        - "orbital imagery and digital terrain models of Jezero crater"
    - head: "Work: Claude plans and checks"
      role: "work"
      lines:
        - "stitches a route out of ~10 m segments, places waypoints"
        - "checks the plan for safety itself, converts it to RML format"
    - head: "Output: the digital twin, then the rover"
      role: "output · threshold"
      uzkoe: true
      lines:
        - "the final check is not Claude's: >500,000 compatibility variables"
        - "classical verification, not re-modeling the terrain"
in_bucket: false
status: draft
---

## Visible slide text

**The threshold sits where it doesn't appear to.** Claude checks its own plan for safety — but that is not the final check; the final one belongs to the digital twin, a separate non-AI step.

**RML is not a demo simplification.** It's the same command format real human operators use — the plan plugs into the existing process with no rework needed.

## Speaker notes

The neighboring breakdown already named the outcome — a 456-meter route over two sols. This diagram breaks the process itself into three parts and separately shows exactly where the final-check threshold sits, because it sits somewhere other than where one might assume by default.

Input — orbital imagery from the HiRISE camera and digital terrain models of Jezero crater, the same material JPL engineers use for manual planning, and the same type of data visible in the neighboring front-camera photo of the rover.

Work — Claude Code analyzes this imagery and these models, stitches a route out of segments roughly 10 meters long, places waypoints, and checks and edits the result itself for safety. After that, it converts the final plan into Rover Markup Language (RML) — the same command format used by live human operators. It is exactly this output in RML, rather than some proprietary format, that makes the plan suitable for plugging into the existing production process without reworking downstream systems.

Output — this is where the honest threshold stands, and it needs to be stated directly: Claude's own safety check is not the final authority. The final check is performed by a separate digital twin at JPL, unconnected to Claude, which runs the plan through more than 500,000 telemetry variables for compatibility with the rover's flight software. This is classical engineering constraint verification, not re-modeling the terrain's physics — and only after it does the plan actually go to the rover for execution.
