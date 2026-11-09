---
id: s23
local_id: s1-06
section: "1. Autonomous robots in space"
type: norm
title: "Section 1 mentions"
assertion: "The classical approach drives Perseverance for 90% of its route with not a single neural network; Starlink carries out 300,000 maneuvers a year on its own"
source: "[NASA JPL](https://www.jpl.nasa.gov/) · [NASA NTRS (IPEx)](https://ntrs.nasa.gov/citations/20220005125) · [ICON](https://www.iconbuild.com/) · [Starlink](https://www.space.com/space-exploration/satellites/every-spacex-starlink-satellite-has-to-dodge-a-collision-almost-weekly-and-experts-fear-the-worst)"
media: ""
media_needed: "A list, each line one observation, not a name (§5.15). Phase 6."
in_bucket: true
status: draft
---

## Visible slide text

- **AutoNav/GESTALT** — the classical approach, not a neural network: drives Perseverance for **90%** of its route (against 6% for Curiosity)
- **NASA IPEx** — an autonomous lunar excavator, **with not a single trained model**: up to 10,000 kg of regolith per lunar day, TRL5 (technology readiness level 5 of 9 — tested under real conditions, not just in the lab)
- **ICON Project Olympus** — laser sintering of regolith; the claimed AI quality-control layer is **not publicly disclosed**
- **Starlink** — ~300,000 autonomous maneuvers a year **on its own, with no third party**: it warns and executes within one organization
- **JPL GIMLI / Moon Diver** — proposed missions into lava tubes, early selection stage, **not flying vehicles**
- **ISRU autonomy** — oxygen extraction TRL6, water extraction (LADI) TRL4

## Speaker notes

This section's mentions aren't chosen as a list of "a few more interesting facts" — they're chosen by the same principle that holds up the whole course: each carries one numerical observation that none of the four detailed case studies carries — a different kind of task, a different readiness status, or a direct consequence of constellation scale.

AutoNav/GESTALT — a stereo pair builds a point cloud, a classical algorithm fits planes and builds a traversability map, over which a heuristic planner lays out a route. This is the classical approach, not a neural network, and it's exactly this system that drives Perseverance autonomously for 90% of its route — against 6% for the older Curiosity with a weaker onboard computer.

NASA IPEx — an autonomous excavator on the Moon. Its working tool is rotating bucket drums, not a classical bucket. The Auto-dig digging algorithms are classical heuristics, with not a single trained model: the physics of the soil and the drum's geometry are known to engineers in advance. Autonomy is supervised at the campaign level; up to 10,000 kg of regolith per lunar day, TRL5, hasn't flown to the Moon yet. This is the section's cleanest case where there's no trained model at all, at any level.

ICON Project Olympus — laser and microwave sintering of regolith in layers, right at the construction site; vacuum testing has been passed, delivery to the Moon is planned for 2026–2027. The architecture of the AI print-quality-control layer isn't publicly disclosed — the level is product announcements, not an engineering spec.

Starlink performs on the order of 300,000 autonomous maneuvers a year, with no waiting for operator approval at a critical moment; at that scale, maintaining a team to confirm every decision by hand would be physically impossible. This is a different point on the same spectrum of task as LeoLabs: there, a third-party network prioritizes observation and warns; here, the operator itself both observes and executes the maneuver.
