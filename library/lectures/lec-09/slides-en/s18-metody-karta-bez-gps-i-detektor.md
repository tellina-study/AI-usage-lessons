---
id: s18
local_id: s1-02a-2
section: "1. Autonomous robots in space"
type: schema_layered
title: "How the methods work: a map without GPS and a single-glance detector"
assertion: "Three SLAM tiers stitch robots' maps together with no GPS; a YOLO detector finds an object in a single pass"
source: "—"
media: ""
media_needed: "Phase 7 (issue #317): replaced with an architecture that breaks the mechanism down INSIDE the boxes (`arhitektura:`) instead of a simple row diagram — the three tiers carry their own breakdown of how it works, not just the order."
arhitektura:
  blocks:
    - head: "Local odometry"
      role: "input"
      lines:
        - "estimating one's own displacement from sensors"
        - "without it, the robot has no map of its own"
    - head: "Match search between robots"
      role: "work"
      lines:
        - "finds places where different robots were at the same spot"
        - "even if the robots never met directly"
    - head: "Joint pose-graph optimization"
      role: "output · bottleneck"
      uzkoe: true
      lines:
        - "matches become edges of a shared graph"
        - "minimizes the total inconsistency across all edges"
blocks:
  - {label: "CNN detection (the YOLO family)", value: "coordinates + class in a single pass", note: "'you only look once' — the whole frame's grid at once, not window by window"}
in_bucket: false
status: draft
---

## Visible slide text

**Three tiers, not two** — each one closes a gap the previous one leaves.

**A detector ≠ geometry.** The detector decides "what this is and where on the frame" (pixels); geometric localization in space is, again, the classical approach, not a neural network.

## Speaker notes

The DARPA mine case study at the start of the lecture already named SLAM and said LAMP's architecture has three tiers — but it didn't explain what each tier means or why there are exactly three. This slide closes that gap before we examine COROB-X in detail.

SLAM — simultaneous localization and mapping: a robot answers two questions at once, "where am I" and "what does the space around me look like", with no ready-made map in advance and no external positioning signal. For a single robot, there's one tier: local odometry, estimating one's own displacement from sensors. When there are several robots, as in COROB-X, one tier isn't enough: without a way to stitch the maps together, three separate maps stay three separate maps. The second tier is match search between robots, the inter-robot version of loop closure: the algorithm looks for moments when two different robots were at the same physical place, even if they never met directly. The third tier is joint pose-graph optimization: the matches found become additional edges of a shared graph, and the task is to find a position for every node such that the total inconsistency across all edges is minimal. This is a classical graph-optimization task, not a trained model.

YOLO-family object detection differs from a classifier (like a random forest) in the kind of task it solves: a classifier answers "what is this", a detector answers two questions at once — "where in the image is the object" (a bounding box) and "what kind of object is it". YOLO does this in a single pass of the network over the entire image — the network splits the frame into a grid of cells and, for each one, simultaneously predicts the probability of an object, its coordinates, and its class. It's trained on labeled examples — a fully trained component. But once the detector has found the artifact and given its pixel coordinates, converting those coordinates into a real distance is, again, classical projective geometry, the same task as the range measurement in AEGIS, not a neural network.
