---
id: s19a
local_id: s1-03-2
section: "1. Autonomous robots in space"
type: case_study
title: "AEGIS on Perseverance"
assertion: "The same AEGIS that raised accuracy to 93% on Curiosity first fired on Perseverance in 2022 — with a different instrument, SuperCam"
source: "[NASA Science, PIA25289, 05.31.2022](https://science.nasa.gov/photojournal/perseverances-supercam-uses-aegis-for-the-first-time)"
media: "assets/razdel-1/aegis/aegis-03-pia25289-perseverance-supercam-aegis.jpg"
media_hero: true
media_hero_target: 0.50
media_caption: "Photo: NASA/JPL-Caltech/LANL/CNES/IRAP, first use of AEGIS on the Perseverance rover's SuperCam, 05.18.2022"
media_needed: "already downloaded (Tier 1, NASA PIA25289). A large illustration for the AEGIS case study, added per owner instruction (Phase 10, issue #317) — every example now has a large illustration, not just a few."
in_bucket: false
status: draft
---

## Visible slide text

**Not a one-off trick on a single rover.** AEGIS first fired on the Perseverance rover's SuperCam instrument in May 2022 — the same algorithm, a different rover, a different instrument.

**It's the architecture that transfers, not the number.** Rockster and the random forest stay the same; the target profile is tuned for the new instrument from scratch.

## Speaker notes

The photo marks the shot NASA used to note the first use of AEGIS on the Perseverance rover's SuperCam science instrument, May 18, 2022. Up to this point, the case study on the neighboring slide spoke only about Curiosity and the ChemCam instrument, where AEGIS has run routinely since 2016 and holds 93% accuracy against the previous 24%. This shot shows the story doesn't end with one rover: the same technology carried over to a second rover and a different science instrument.

It's important to understand exactly what carried over and what was retuned from scratch. The architecture — the Rockster algorithm, which searches for candidates by brightness contrast and edges in stereo images, and the random-forest classifier, which ranks them — stayed the same, with no retraining from zero. Only the target-of-interest profile is retuned: what SuperCam's science team considers an interesting object differs from ChemCam's profile on Curiosity.

An honest gap: sources don't publish a separate accuracy figure for AEGIS on Perseverance and SuperCam, comparable to the 24%→93% for Curiosity and ChemCam. What this case shows isn't a new number — it's proven transferability: a system that works once extends to new instrument-and-rover configurations without being rewritten from scratch, just by retuning one parameter — the target profile.
