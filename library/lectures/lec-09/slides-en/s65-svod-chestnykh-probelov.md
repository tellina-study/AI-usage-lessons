---
id: s65
local_id: s5-07
section: "5. Assembly"
type: norm
title: "Summary of honest gaps"
assertion: "What the sources honestly don't disclose isn't a gap in preparation — it's a map of the boundary of public knowledge"
source: "—"
media: ""
media_needed: "List, 6 categories of gaps. Phase 6."
in_bucket: true
status: draft
---

## Visible slide text

- **Operating budget and decision-revision protocol** — the number of ChemCam measurements per cycle, IPEx's behavior in an off-nominal situation, manual intervention in Dragon at the last moment
- **Feedback loop between outcomes and system updates** — whether AEGIS's profile gets revised, whether COROB-X's quality cycle closes
- **Composition and volume of training data** — not disclosed for AEGIS, COROB-X's CNN, Astrobee, LeoLabs; contrast with AIFS/AIGEFS and SPOC, which disclose it in detail
- **System architecture, not disclosed by the vendor** — the NASA Docking System (Dragon), ICON's quality-control layer
- **Economics at the level of a single operation** — Starcloud/Suncatcher don't publish per-request cost; generative design's 10x is an internal estimate
- **The step after a warning, outside the organization's control** — LeoLabs has no data on operators' actual maneuvers

## Speaker notes

Gathering the gaps already named earlier into one place matters for a substantive reason, not just for completeness: scattered across thirteen different breakdowns, they read easily as random details; brought together, they show a systemic boundary of what the industry discloses publicly today about its own AI systems in space.

Operating budget and decision-revision protocol: the exact number of measurements AEGIS is allowed per cycle; IPEx's behavior in an off-nominal situation; Dragon's behavior if manual intervention is attempted at the last moment — none of these thresholds is disclosed quantitatively. Feedback loop: whether AEGIS's target profile gets revised based on failed selections; whether COROB-X's map quality cycle closes; whether Astrobee's warm-start model gets updated after the handover to Arkisys — none of these questions has a published answer. Composition and volume of training data: not disclosed for AEGIS, COROB-X's CNN, Astrobee, or LeoLabs's own model; the contrast with AIFS/AIGEFS and SPOC is telling — there, these details are disclosed in noticeably more depth, which means the absence of this detail for most of the others is a specific developer's choice, not an industry-wide rule.

System architecture not disclosed by the vendor: the NASA Docking System for Dragon, ICON's qualification system. Economics at the level of a single request: Starcloud and Suncatcher confirm the fact that they work but don't publish the cost of a single request; generative design's 10x savings is an internal estimate, not an independently confirmed fact. The step after a warning, outside the control of the organization being discussed: LeoLabs publishes the frequency and accuracy of its warnings but not statistics on operators' actual maneuvers — an honest gap of a different kind, the absence of data on a third party's action.
