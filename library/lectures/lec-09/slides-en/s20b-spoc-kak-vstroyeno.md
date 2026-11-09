---
id: s20b
local_id: s1-04-3
section: "1. Autonomous robots in space"
type: schema_layered
title: "How SPOC is built into route planning"
assertion: "SPOC labels the traversability map, but whether to drive or not is decided by the rover driver, not the model"
source: "—"
media: ""
media_needed: "Phase 10 (issue #317): a diagram of SPOC's specific instrument integration — shows exactly where the soil-class map is built into the route-planning process, and who decides after the model."
arhitektura:
  blocks:
    - head: "Input: rover camera images"
      role: "input"
      lines:
        - "orbital HiRISE and onboard NavCam — two sources of frames"
        - "the image is sliced into patches for pixel-level classification"
    - head: "Work: CNN soil classification"
      role: "work"
      lines:
        - "a deep convolutional network determines surface type right from pixels"
        - "no manual feature extraction — unlike AEGIS's random forest"
    - head: "Output: a traversability map"
      role: "output · with the driver"
      uzkoe: true
      lines:
        - "the map feeds into route planning, it doesn't replace the decision"
        - "whether to drive a section or not is decided by the rover driver on Earth"
in_bucket: false
status: draft
---

## Visible slide text

**The model labels, it doesn't decide.** The soil-class map is a recommendation for planning, not a command that goes straight to the hardware.

**The final authority is named directly.** The decision to drive or not drive a specific section stays with the rover driver on Earth — same as before SPOC.

## Speaker notes

The SPOC case study on neighboring slides has already named the accuracy — 98% — and the fact that it rests on a continuous stream of new AI4Mars labels. This diagram answers a different question: exactly where the model's output is built into the rover's route-planning process, and who decides after it.

The input is images from two sources: the orbital HiRISE camera gives a wide view of the terrain in advance, the rover's own NavCam navigation cameras give a detailed view immediately ahead of it. Both kinds of images are sliced into patches — small sections of the image that get classified separately.

The work is SPOC's deep convolutional network passing over every patch and determining surface type right from the image's pixels: soil, bedrock, sand, large rock. This sets SPOC apart from AEGIS's classifier (a random forest), which needs pre-computed geometric features before classification — SPOC doesn't need that intermediate step.

The output is a traversability map, assembled from the classifications of all the patches. The map is fed into the route-planning process as one of several inputs, alongside other terrain data — but it doesn't execute movement itself. The final authority — to drive a specific section or route around it — stays with the rover driver on Earth, the same person who made this decision before SPOC existed, just now with a more detailed hint on hand.
