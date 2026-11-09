---
id: s19b
local_id: s1-03-3
section: "1. Autonomous robots in space"
type: schema_layered
title: "How AEGIS is built into the rover"
assertion: "A human sets the target profile in advance, on Earth; the algorithm onboard makes the actual target choice in the moment"
source: "—"
media: ""
media_needed: "Phase 10 (issue #317): a diagram of this specific instrument's integration for AEGIS — separate from the general breakdown of the geometry and random-forest methods (§ 1.2a, slide s1-02a)."
arhitektura:
  blocks:
    - head: "Input: NavCam stereo pair"
      role: "input"
      lines:
        - "range to the object — by geometry, via parallax, not a neural network"
        - "Rockster searches for candidates by brightness contrast and edges"
    - head: "Work: random forest ranks them"
      role: "work"
      lines:
        - "the classifier scores candidates against the target-of-interest profile"
        - "the scientist sets the profile in advance, on Earth, once"
    - head: "Output: coordinates for ChemCam / SuperCam"
      role: "output"
      lines:
        - "the shot happens onboard, with no round-trip to Earth for approval"
        - "the choice of the specific target in the moment belongs to the algorithm, not a human"
in_bucket: false
status: draft
---

## Visible slide text

**Where a human used to stand.** Before AEGIS, a scientist chose every target personally, from the previous cycle's image — that is, in the spot held by this diagram's third block.

**What the automation did.** The third block moved onboard: the target's coordinates go straight to ChemCam or SuperCam, with no waiting for a command from Earth.

## Speaker notes

The AEGIS case study on neighboring slides has already named how it's built, in words — input, Rockster, random forest, ChemCam. This diagram gathers those same three blocks into one picture of the integration: what's at the input, what happens inside, what's at the output — and shows explicitly exactly where in this chain a human used to stand, and where an algorithm now stands.

The input is a stereo pair from the NavCam navigation cameras. Two cameras, set apart by a known distance, give the range to every point in the image by a geometric method, via parallax — a classical, non-trained part. The Rockster algorithm uses this stereo pair to find candidates for interesting objects, using brightness contrast and edges.

The work is a random-forest classifier ranking the candidates found against the target-of-interest profile. This profile isn't a choice the algorithm makes on its own: a scientist on Earth tunes it once, in advance — for example, "look for objects of such-and-such shape and brightness". Once the profile is set, the actual moment of choosing a specific target out of the many candidates happens onboard, with no human involved.

The output is the chosen target's coordinates, passed directly to the ChemCam instrument (on Curiosity) or SuperCam (on Perseverance, see the neighboring illustration) for imaging. This is exactly where the full cycle used to stand: an image to Earth, a scientist's decision, a command back to the rover — a cycle that cost a whole Martian sol for every miss. Now this entire stretch of the chain, except for setting the profile, runs onboard in a single pass.
