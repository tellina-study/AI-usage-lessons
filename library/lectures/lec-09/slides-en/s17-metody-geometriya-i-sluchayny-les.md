---
id: s17
local_id: s1-02a-1
section: "1. Autonomous robots in space"
type: norm
title: "How the methods work: geometry and random forest"
assertion: "A stereo pair computes range by geometry, not by training; a random forest is an ensemble of trees you can read all the way through"
source: "—"
media: "assets/razdel-1/aegis/aegis-04-rockster-detection-coverphoto.png"
media_needed: "already downloaded (Tier 1). Detections from the Rockster algorithm on a NavCam image — illustrates the random forest's input."
blocks:
  - {label: "Stereo vision (parallax)", value: "disparity → range by geometry", note: "two cameras on a known baseline, similar triangles, no trained parameters"}
  - {label: "Random forest", value: "dozens to hundreds of decision trees", note: "bagging + a random subset of features at each node"}
  - {label: "The key property of a random forest", value: "interpretability", note: "a tree can be read all the way through, step by step — not a black box", key: true}
in_bucket: false
status: draft
---

## Visible slide text

**Why exactly this mechanics matters: it's what holds up AEGIS.** Distance to the target (Block 1) is one of the features by which interest is ranked (Block 2). Both blocks are below, before we move on to the case study itself.

## Speaker notes

§1.2 drew the line between the classical approach and learning in two paragraphs — but a named boundary and a mechanically understood boundary aren't the same thing. This slide makes it mechanically clear before we move on to the first three detailed case studies.

Block 1. Stereo vision and parallax — why distance doesn't need to be learned. Two cameras, set apart by a precisely known distance (the baseline), photograph the same point in a scene. If the point is close, it projects onto noticeably different positions in the left and right frames; if far, onto almost the same position. The difference is called disparity. Knowing the baseline, the focal length, and the measured disparity, the distance to the point is computed directly from the formula for similar triangles, with not a single parameter that would need to be fit from the statistics of examples. This is the same principle by which a pair of human eyes judges the depth of a scene. That's exactly why the distance to an object in AEGIS is a classical geometric quantity, not something a classifier guesses from statistics.

Block 2. Random forest — an ensemble of trees you can read all the way through. This isn't one model but many (dozens to hundreds) of independently trained decision trees, voting together. A single tree easily overfits to the noise of specific examples; a random forest fixes this with two tricks: each tree is trained on its own random subsample of examples (bagging), and at each split point the tree chooses its test from a random subset of features. Because of these two sources of randomness, the trees come out different, and their errors cancel each other out when voting.

This design has an engineering consequence: a random forest is not a black box in the sense a deep neural network is often called a black box. A specific tree can be read all the way through, step by step: which feature and which threshold it checked at every node. For a deep network with millions of weights, unpacking a decision the same way is structurally much harder. A random forest doesn't try to solve the task end-to-end from a raw image — it works on a small set of already-extracted features, and for a task of this scale a heavier architecture wouldn't deliver a gain that would justify its computational cost onboard a Mars rover.
