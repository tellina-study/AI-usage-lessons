---
id: s33a
local_id: s2-06-2
section: "2. Teleoperation"
type: case_study
title: "Astrobee on the ISS"
assertion: "Astrobee flies inside the station on its own, on fans, with no tether and no hands — this exact free flight is what the warm start controls"
source: "[NASA Johnson Space Center, Wikimedia Commons, 05/01/2024](https://commons.wikimedia.org/wiki/File:A_free-flying_Astrobee_robot_pictured_aboard_the_International_Space_Station_%28iss071e046284%29.jpg)"
media: "assets/razdel-2/astrobee/01-astrobee-free-flying-iss071e046284.jpg"
media_hero: true
media_hero_target: 0.50
media_caption: "Photo: NASA Johnson Space Center, public domain"
media_needed: "already downloaded (Tier 1, NASA, Wikimedia Commons). A large illustration for the Astrobee breakdown, added at the owner's instruction (Phase 9, issue #317) — the photo was downloaded earlier but had not been used large on any slide."
in_bucket: false
status: draft
---

## Visible slide text

**A cube-shaped body with no tether and no legs.** Astrobee holds itself in the air with fans that push air out through side nozzles — not magnets, not wheels, not grabbing the walls.

**This exact free flight is what the warm start refines.** The model proposes a flight path through the station's module, and the classical controller checks it before every maneuver.

## Speaker notes

The photo shows Astrobee in free flight inside the Japanese "Kibo" module of the International Space Station, taken by NASA Johnson Space Center. The body is a cube roughly 32 centimeters on a side, with no tether and no mechanical attachment to the station: internal fans keep it aloft and move it by pushing air out through controllable nozzles on the sides of the body, generating thrust in the needed direction. This is fundamentally different from the station's earlier robots, which held onto handrails or moved along guide rails — Astrobee moves through the module's entire free volume on its own.

It is exactly this kind of movement — finding a path through a cramped space full of equipment, with a risk of collision on every maneuver — that is the task refined by the "warm start" covered on the neighboring slide: a model trained on the statistics of past trajectories proposes a draft route, and a classical feedback controller checks and refines it before execution, without changing the final safety guarantee.

The robot has flown on the ISS since 2019, in several units — the photo shows one of them, with no human visibly present nearby: it is exactly the absence of constant manual control that allows the trajectory statistics to accumulate, on which the warm-start model is later trained.
