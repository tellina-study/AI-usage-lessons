---
id: s20
local_id: s1-04
section: "1. Autonomous robots in space"
title: "Example: SPOC — labeling Martian soil with a neural network"
type: case_study
assertion: "SPOC labels Martian soil with a deep network at 98% accuracy — already on the ground today, onboard only in the future"
source: "[NASA JPL, SPOC project page (nasa-jpl.github.io/SPOC)](https://nasa-jpl.github.io/SPOC/) · [AI4Mars/Zooniverse](https://www.zooniverse.org/projects/hiro-ono/ai4mars)"
media: "assets/razdel-1/spoc/spoc-03-sidebyside-segmentation.png"
media_needed: "already downloaded (Tier 1). Input (image) vs output (SPOC's class map) side by side — shows the mechanism directly."
graf: "b"
blocks:
  - {label: "Cost of error", value: "a stuck rover", note: "loose sand mistaken for firm soil — risk of months of recovery or losing the vehicle"}
  - {label: "Classical mode", value: "the driver's visual judgment", note: "named, but no precise figure exists in open sources"}
  - {label: "The model (SPOC-HiRISE / SPOC-NavCam)", value: "98% accuracy", note: "a deep CNN right on pixels, already used by Curiosity and Perseverance drivers", key: true}
  - {label: "How it works", value: "HiRISE/NavCam input → patches → CNN → soil-class map", note: "a ground tool today; forward-looking — SPOC-Lite (CPU) and SPOC-HPSC/SNPE (GPU) for a future onboard version"}
in_bucket: true
status: draft
---

## Visible slide text

**The feedback loop is explicitly closed** — unlike AEGIS and COROB-X: the AI4Mars project (Zooniverse) is recruiting volunteers to label Perseverance images right now.

**A forward-looking part.** SPOC-Lite and SPOC-HPSC/SNPE are for future missions, **not deployed** on flying rovers.

*Image classification.*

## Speaker notes

The volume of images piling up from the Mars program's orbital and ground cameras is growing faster than people can label them by hand — the same data growth named for the whole industry back in the Introduction. A soil-classification error isn't abstract: a misidentified surface type can lead to a stuck rover, months-long recovery, or the loss of the vehicle.

The classical mode (column b — the second mode is named, but has no number of its own in open sources): before SPOC, a human driver did the labeling, judging terrain danger by hand from their own experience; no precise figure for hours per image was found.

The model: SPOC is NASA JPL's family of deep convolutional neural networks. SPOC-HiRISE works with orbital images, SPOC-NavCam with the rover's own images. Unlike AEGIS's classifier (a random forest) and the classical AutoNav, SPOC is a full-fledged deep network, working right on pixels, with no intermediate manual extraction of geometric features. NASA states 98% accuracy. The model is already used by rover drivers for route planning on Curiosity and Perseverance right now — but it's a ground support tool, not an onboard module.

The training data isn't static: the AI4Mars project on the Zooniverse platform recruits volunteers to label Perseverance images, and those labels keep coming in and get used to improve the model — the feedback loop is set up explicitly, unlike AEGIS and COROB-X, where the composition of the training set isn't disclosed.

The forward-looking part: two variants for future onboard use — SPOC-Lite (a simple model for an ordinary CPU) and SPOC-HPSC/SNPE (a full network for a GPU, which neither Curiosity nor Perseverance has onboard). Neither is deployed today — an explicitly named, not-yet-realized direction. What moved over: labeling moved from the driver's sole visual judgment onto the model's classification layer — a decision aid, not a replacement for the driver.
