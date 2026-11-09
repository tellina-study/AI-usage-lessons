---
id: s09
local_id: I-09
section: "0. Introduction"
type: norm
title: "From an earthly mine to a lunar lava tube"
assertion: "A solution for an earthly mine turned out to fit a lunar lava tube — the frontier became its own laboratory"
source: "[DARPA Subterranean Challenge (2018–2021)](https://www.darpa.mil/research/challenges/subterranean) · [JPL/Caltech/MIT/KAIST/Luleå, the NeBula/CoSTAR family](https://costar.jpl.nasa.gov/)"
media: ""
media_needed: "Phase 7 (issue #317): the photo of COROB-X at a cave entrance was removed from this slide — the slide body was overloaded with the transfer timeline plus the open field for the owner's testimony; the same shot (corobx-01-drone-view-cave-entrance.jpg) stays in Section 1's assets, where COROB-X is examined in detail (s21)."
owner_placeholder: true
timeline:
  unit: "transfer stage of the solution"
  caption: "One architecture, three stages: from a mine competition to a lunar demonstrator"
  stages: ["DARPA Subterranean\nChallenge, 2018–2021", "LAMP 2.0 architecture", "COROB-X — lunar\nlava tube"]
  marks:
    - at: 0
      head: "Mine"
      text: "a competition for autonomous reconnaissance of mines and collapsed buildings — GPS and comms don't work underground, same as in space"
    - at: 1
      head: "LAMP 2.0"
      text: "8+ robots stitch maps together over kilometer-scale distances — measured at the earthly competition"
    - at: 2
      head: "Moon"
      text: "carried over in spirit, not in code; tested on Earth, Lanzarote, 02.2023 — never flown to the Moon"
in_bucket: false
status: draft
---

## Visible slide text

**The transfer: the lecturer's own testimony.**

What follows is a case from the lecturer's own practice about carrying a solution from one frontier to another; told orally, with no text on screen.

**Closing line.** The familiar answer: "solutions come from the lab, space applies them". The lecture's question: what happens when the frontier itself becomes the laboratory?

## Speaker notes

Before the lecture starts proving its claim piece by piece across thirteen case studies, it presents that claim with one measured case — the very case study promised to the room, which is the lecture's claim itself, not an illustration of it.

The NeBula/LAMP architecture was not born in space. It appeared as the winner of the DARPA Subterranean Challenge — a competition for autonomous reconnaissance of mines and collapsed buildings, that is, an earthly frontier where satellite navigation and stable communication also physically do not work: underground, GPS doesn't penetrate rock, and radio is jammed by the same walls. The team built a SLAM system called LAMP — a three-tier architecture: each robot's own local odometry, place-match search between maps at a base station, and joint pose-graph optimization. The LAMP 2.0 version scales to 8 or more heterogeneous robots over kilometer-scale distances — a figure measured at the earthly competition, not in space.

This architecture was then adapted — in the spirit of the approach, not directly by code, and that's an honest caveat worth stating right here — for conditions harsher still than earthly mines: lunar lava tubes, where there is not only no GPS and no stable communication, but no daylight and no connection to the surface at all. The COROB-X demonstrator, which we'll examine in detail in Section 1, uses an architecture from the same family. There is no direct confirmation in public sources that COROB-X literally uses NeBula/LAMP code: the connection is by family of solutions and by the underlying task, not by shared source code. The technology was tested on Earth, in Lanzarote, in February 2023; it has never flown to the Moon.

The second part of this case study is, by the course's own canon, given over to the owner's own testimony about carrying a solution from one frontier to another. The field is left open on purpose: without that testimony it stays a placeholder, not a story invented on the owner's behalf — the owner fills it in themselves.

Closing line: the familiar answer says "engineering solutions come from the lab, space applies them". The question this lecture asks with its material going forward is — what happens when the frontier itself becomes the laboratory?
