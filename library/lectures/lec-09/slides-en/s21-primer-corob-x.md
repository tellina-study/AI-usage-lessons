---
id: s21
local_id: s1-05
section: "1. Autonomous robots in space"
type: case_study
title: "Example: COROB-X — three robots in a lava tube"
assertion: "Three robots explored a lunar lava tube in a place where no classical equivalent on Earth existed at all"
source: "[DFKI (Germany) together with Space Applications Services](https://www.dfki.de/en/web/news/corobx-feldtests-lanzarote) · [field testing, Lanzarote, 02.2023](https://www.gmv.com/en/communication/news/final-field-testing-completed-corob-x)"
media: "assets/razdel-1/corob-x/corobx-13-infographic-mission-phases-figure2.png"
media_needed: "already downloaded (Tier 1). Official infographic of the mission's four phases."
graf: "c"
blocks:
  - {label: "Cost of risk", value: "a ceiling collapse with no warning", note: "a human on a safety tether risks their life; three robots do not"}
  - {label: "Classical mode", value: "does not exist", note: "no industry on Earth had solved this task before this demonstrator", key: true}
  - {label: "Automation (SherpaTT + Coyote III + LUVMI-X)", value: "4 phases: mapping → sensor cube → tethered descent → 3D reconnaissance", note: "a three-tier SLAM in the spirit of the DARPA mine architecture + a YOLOv4 CNN layer"}
  - {label: "How it works", value: "visible+thermal spectrum → YOLOv4 → EaRLaP → geometry", note: "the arbitration is the EaRLaP pipeline, filtering out false detections"}
in_bucket: true
status: draft
---

## Visible slide text

**What moved over.** Safety unambiguously improved — three robots don't put a human life at risk. Complexity grew just as unambiguously: one human with a flashlight → three machines, a tether, a surface base station.

**An honest gap.** Sources don't give a numerical measure of map quality. The system has never flown to the Moon or Mars.

*Image recognition.*

## Speaker notes

A human on a safety tether descends into a lava tube slowly and risks their life under an unstable cave ceiling. Three robots exploring the same space in parallel work faster and don't risk a life — but at the cost of a noticeably higher system complexity.

The classical mode (column c — the task is new, no classical earthly equivalent exists in the same units, and the reason for that is stated): no industry on Earth had solved the task of "build a 3D map of a closed underground space with no GPS, no daylight, and no connection to the surface, using several autonomous machines" before this demonstrator.

Three machines of different designs: SherpaTT — a hybrid wheel-legged robot, a surface scout and anchor for the tether. Coyote III — a light rover that descends into the entry shaft and builds an autonomous 3D map. LUVMI-X — maps outside together with SherpaTT. The work runs in four phases: surface mapping → deploying a sensor cube at the entrance → tethered descent inward → autonomous 3D reconnaissance. Under the hood is an architecture in the spirit of LAMP, already broken down using the DARPA mine case at the start of the lecture: three-tier SLAM (local odometry → match search → joint graph optimization). Object detection is a separate CNN layer, including YOLOv4, across the visible and thermal spectrum; geometric localization of a found object is classical projective geometry, not a model.

An explicit arbitration mechanism is named by name — the EaRLaP pipeline, which filters out false and missed detections before they're counted as a confirmed artifact. A human on the surface checks already-aggregated data after the fact — there's no connection to the surface at all during the reconnaissance itself. The link to the NeBula/LAMP architecture is by the spirit of the approach and family of solutions, not shared code. The three selection criteria: remove the CNN detector and the result changes; the subject matter is industry-relevant; but there's no numerical "was X, became Y" outcome here, only a qualitative comparison of risks — an honestly acknowledged boundary of the selection, not a hidden weakness.
