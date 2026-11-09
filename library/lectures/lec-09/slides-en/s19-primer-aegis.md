---
id: s19
local_id: s1-03
section: "1. Autonomous robots in space"
type: case_study
title: "Example: AEGIS — autonomous selection of scientific targets on Mars"
assertion: "AEGIS raised target-selection accuracy from 24% to 93% — with not a single command from Earth"
source: "[Francis et al., Science Robotics 2017](https://www.science.org/doi/abs/10.1126/scirobotics.aan4582) · [JPL, AEGIS project page](https://ai.jpl.nasa.gov/public/projects/aegis/)"
media: "assets/razdel-1/aegis/aegis-01-pia20762-curiosity-target-selection.jpg"
media_needed: "already downloaded (Tier 1, NASA PIA20762)."
graf: "a"
blocks:
  - {label: "Cost of a miss", value: "1 lost sol", note: "re-choosing a target costs another full communication cycle with Earth"}
  - {label: "Classical mode (before AEGIS)", value: "24% hit rate", note: "targeting by Earth command based on the previous image"}
  - {label: "The model (AEGIS, Rockster + random forest)", value: "93% hit rate", note: "routine on Curiosity since 2016 (first on Opportunity, 2010)", key: true}
  - {label: "How it works", value: "NavCam stereo-pair input → Rockster → features → random forest → ChemCam", note: "range — by geometry (Block 1), ranking — by random forest (Block 2)"}
in_bucket: false
status: draft
---

## Visible slide text

**What moved over.** Productivity grew almost fourfold — a scientist sets the target profile in advance, once, instead of choosing every target personally.

**An honest gap.** Sources don't disclose the feedback loop or the composition of the random forest's training set.

*Image classification.*

## Speaker notes

This case study carries the most evidentiary weight in the whole of the lecture's claim, and not by accident: of the thirteen cases, it's the one in continuous use the longest (continuously since 2016) and the most thoroughly confirmed by a peer-reviewed publication.

The cost of both sides: a target chosen from an old image without autonomous selection often turns out to be scientifically uninteresting — the rover spends its limited communication time and resources photographing something that contains no new knowledge. Re-choosing costs another full Martian sol, wasted: time on the ChemCam spectrometer, battery charge, and, most expensive of all, the bandwidth of the link to Earth.

The classical mode (column a — given a number in the same unit as the model): before AEGIS, Curiosity targeted by Earth command, based on the previous image with limited information. The result was a 24% hit rate on scientifically interesting targets.

The model: the Rockster algorithm finds potentially interesting objects by brightness contrast and edges in NavCam stereo images, extracts features — size, shape, intensity, range — filters out unsuitable candidates, and ranks the rest with a random-forest classifier against a pre-set target-of-interest profile. This is an honest architectural detail: not deep learning, but an interpretable classifier, which is enough for a task of this scale onboard with a limited, radiation-hardened processor.

The result: accuracy rose from 24% to 93%, saving one sol per target-selection cycle. Five questions of engineering depth: the processing happens onboard; before AEGIS, a scientist chose every target personally, afterward they set the profile in advance and the choice happens onboard; there's no human in the loop of the choice itself, the arbitration is inside the algorithm; a direct metric was measured (24%→93%), published in Science Robotics; the classifier was trained in advance, and no data on retraining during operation was found — an honest gap. All three case-selection criteria are met exemplarily: remove the random forest, and the rover reverts to 24%; the subject matter is industry-relevant; both sides are measured with a number and an explicit source.
