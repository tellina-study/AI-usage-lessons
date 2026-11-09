---
id: s21b
local_id: s1-05-3
section: "1. Autonomous robots in space"
type: schema_layered
title: "How COROB-X's three robots build one map with no GPS"
assertion: "SherpaTT, Coyote III, and LUVMI-X each map on their own; the exact same three-tier SLAM broken down on the neighboring slide stitches the tube into one map"
source: "—"
media: ""
media_needed: "Phase 10 (issue #317): a named diagram of the three-tier SLAM (the method's mechanism is on s18), built specifically for the COROB-X mission — three specific robots, not the section's general diagram."
arhitektura:
  blocks:
    - head: "Input: three robots, three different maps"
      role: "input"
      lines:
        - "SherpaTT and LUVMI-X are outside, Coyote III is inside the tube"
        - "each computes its own displacement from sensors — with no GPS"
    - head: "Work: matches between the robots' maps"
      role: "work"
      lines:
        - "finds places where different robots were at the same point"
        - "works even if the robots never met directly"
    - head: "Output: one map of the tube, with no connection to the surface"
      role: "output · bottleneck"
      uzkoe: true
      lines:
        - "matches become edges of a shared pose graph"
        - "the three maps stitch into one during the descent itself"
in_bucket: false
status: draft
---

## Visible slide text

**The mechanism is on the neighboring slide, this one is the application.** The three SLAM tiers are already broken down on the methods slide; this slide shows exactly how they're built into the COROB-X mission.

**Three robots of different designs, one map.** SherpaTT and LUVMI-X work outside, Coyote III inside the tube; each with no GPS and no direct link to the others during the descent.

## Speaker notes

The neighboring slide has already named how the three-tier SLAM works, in words — local odometry, match search between robots, joint pose-graph optimization. This slide doesn't repeat that breakdown; it gathers the same three tiers into one picture specifically for COROB-X: what exactly is at the input, what happens inside, what's at the output of this specific mission in the Lanzarote lava tube.

The input: COROB-X has three machines of different designs, and each builds its own local map independently of the others. SherpaTT, a hybrid wheel-legged robot, maps the surface outside and simultaneously serves as the anchor for the tether. LUVMI-X maps outside together with SherpaTT. Coyote III descends on that tether through the skylight opening into the tube itself and builds its own 3D map there — with no GPS, no daylight, no connection to the surface. The first SLAM tier — local odometry — belongs to each robot on its own: without it, none of the three even has a map of its own.

The work: three separate maps aren't enough — without a way to stitch them together, three maps stay three unconnected maps, not one shared space. The second tier is match search between robots: the algorithm looks for moments when two different robots were at the exact same physical spot in the tube or its surroundings, even if they never met there directly.

The output: the third tier, joint pose-graph optimization, turns the matches found into additional edges of a shared graph and looks for a position for every node such that the total inconsistency across all edges is minimal. For COROB-X, this is the exact moment when the three separate maps from SherpaTT, LUVMI-X, and Coyote III become one map of the lava tube — and the stitching happens during the descent itself, while there's no connection to the surface at all yet; a human on the surface only sees the aggregated result after the fact.
