---
id: s29
local_id: s2-03
section: "2. Teleoperation"
type: schema_timeline
title: "Where a human is needed, where the boundary has already shifted"
assertion: "The delay to the ISS is a fraction of a second, to the Moon 1.3 seconds, to Mars 3 to 22 minutes: you cannot get around the speed of light"
source: "—"
media: ""
media_needed: "Timeline bar: ISS → Moon → Mars, delays in seconds/minutes, pivot — Mars larger. Phase 6."
blocks:
  - {label: "To the ISS", value: "a fraction of a second", note: "the same order as the Starlink delay in telesurgery — covered later in this section (~130 ms)"}
  - {label: "To the Moon", value: "1.3 seconds", note: "plus the controller's own operational delays"}
  - {label: "To Mars", value: "3–22 minutes", note: "depending on the relative position of the orbits — 2–3 orders of magnitude more than the lunar delay", key: true}
in_bucket: false
status: draft
---

## Visible slide text

**This is a physical, not an organizational, reason** why Section 1 and Section 2 need to be two separate sections at all — a property of the geometry of distance that no communication channel can outrun faster than the speed of light.

**Where an event unfolds faster than a human can react** — control is handed to automation **in advance**, with the right to intervene, not after the fact of an accident.

## Speaker notes

Teleoperation works as long as the communication delay and the speed at which events unfold leave the human real time to react. At low orbit that's seconds — enough for the operator to assess the picture and respond. At Martian minutes of delay, that is physically impossible — a direct bridge to why Section 1 is an engineering necessity on Mars, not a convenience.

The communication delay between two points in space is set by distance and the speed of light — a quantity that no engineering solution can get around, unlike channel bandwidth. The delay to the ISS is a fraction of a second, the same order as the Starlink delay in telesurgery — a case that comes up later in this section (~130 ms). The delay to the Moon is 1.3 seconds plus the controller's own operational delays. The delay to Mars is 3 to 22 minutes, depending on the relative position of the orbits; even the lower bound is two orders of magnitude greater than the lunar delay, and the upper bound is nearly three. This is a physical, not an organizational, reason why Section 1 and Section 2 need to be two separate sections: the boundary between them is not an engineer's choice but a property of the geometry of distance.

Where the event itself unfolds faster than human reaction — an emergency maneuver, the final fraction of a second of docking — control is handed to automation in advance, before the event happens, with the human's right to intervene, not the obligation to perform the action himself. This is a key distinction: the decision of "who acts at this moment" is made not after the human turns out unable to react, but in advance, by engineering, at the design stage.

All three detailed breakdowns in the section belong to different organizations and countries with no connection to each other, and each in its own way shows automation or a model inside the loop — not coordination, but a parallel, independent emergence of automation wherever that one physical constraint demands it.
