---
id: s31
local_id: s2-04
section: "2. Teleoperation"
type: case_study
title: "Example: Dragon's autonomous docking to the ISS"
assertion: "At a distance of 220 meters, control of Dragon is handed to automation in advance — routine since 2020"
source: "[NASA/SpaceX, Demo-2 mission (2020)](https://www.nasa.gov/news-release/nasa-astronauts-launch-from-america-in-historic-test-flight-of-spacex-crew-dragon/)"
media: "assets/razdel-2/dragon/07-INFOGRAPHIC-esa-docking-sequence.png"
media_needed: "already downloaded (Tier 1, ESA). Official infographic of the docking sequence. A hero scale was tried (issue #317, task A, `media_hero_target` from 0.48 to 0.22) — it did not help: `place_hero_centered` narrows the body column, and this lecture's plates for 'cost/classical/model' (`PLATES`, `max_per_row=2`) are already sized for the slide's full width; at reduced width, long words ('millisecond', 'AUTOMATION') do not fit the frame. At 0.22 (below the 40% hero threshold, §5.9), the body text still does not fit (`[height] s31/body: no room left`). Enlarging the image without editing the plate/notes text is not possible here — the previous side size is kept."
graf: "b"
blocks:
  - {label: "Cost of manual error", value: "millisecond precision at the edge of motor control", note: "speed, angle, and position must coincide with hard-to-achieve precision"}
  - {label: "Cost of full automation with no manual intervention", value: "an unforeseen scenario", note: "any system designed for a finite set of scenarios risks running into a new one"}
  - {label: "Classical mode", value: "manual docking, Shuttle / Soyuz", note: "named, but the hours of preparation and attempt statistics are not published"}
  - {label: "Automation (NASA Docking System)", value: "autonomous from 220 meters", note: "routine since 2020; manual intervention available at any moment", key: true}
in_bucket: false
status: draft
---

## Visible slide text

**220 meters is not a physiological limit of reaction time, but an engineering decision:** where automation is reliably more precise than a human.

**What moved over.** Precision of the final approach — to automation; responsibility — stays with the human: he monitors and can intervene, though he almost never does.

## Speaker notes

Manual piloting on the final meters of docking requires millisecond precision with minimal margin for error — a task at the edge of human motor capability. Full automation with no ability to intervene is a risk in an off-nominal situation the algorithm did not anticipate.

Classical mode (column b): manual docking, performed by the crews of the Space Shuttle and Soyuz — a named but uncounted baseline: the procedure takes hours of pilot preparation, but the exact number and the statistics of successful attempts are not published — just as the success rate of Dragon's autonomous phase is not published either.

Model/automation: the NASA Docking System — on the Demo-2 mission in 2020, the commander manually piloted the ship to a distance of 220 meters, after which the ship autonomously performed soft docking. The crew monitors the process, and manual control is available to return at any moment. Input — laser rangefinders and video feed; output — attitude-control thruster commands. Why exactly 220 meters: a balance between how far out automation already has sufficiently precise rangefinder data, and the range within which human motor control still performs no worse than automation — the sources do not detail the exact methodology behind choosing this boundary.

Five questions of engineering depth: manual piloting has not disappeared, but is preserved for the stretch within 220 meters; the threshold is set in advance, arbitration is manual intervention; the sources characterize the operation as "routine since 2020" without publishing attempt statistics; the control system's architecture is not publicly disclosed by SpaceX — honestly unknown whether it is trained statistically or computed classically, like G-FOLD. Three selection conditions: the architecture is undisclosed, but the exception "AI enabled something that was impossible without it" applies; the subject is unconditionally industrial; column b — hours of preparation are named without a number.
