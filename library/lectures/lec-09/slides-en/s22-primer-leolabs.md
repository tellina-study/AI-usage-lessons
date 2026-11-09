---
id: s22
local_id: s1-05a
section: "1. Autonomous robots in space"
type: case_study
title: "Example: LeoLabs — radar prioritization and collision warnings"
assertion: "LeoLabs prioritizes the radar and issues up to 400% more close-approach warnings — but doesn't know how many of them resulted in a maneuver"
source: "[LeoLabs (eoportal.org, leolabs.space/conjunction-alerts, SpaceNews)](https://leolabs.space/conjunction-alerts/)"
media: ""
media_needed: "An honest gap — no asset was found for this case (the LeoLabs gap analysis was added separately from the main Tier 1–6 pass over Section 1). Phase 6: a 6-tier acquisition attempt was made before falling back."
graf: "b"
blocks:
  - {label: "Cost of a miss", value: "loss of a satellite + a debris cascade", note: "Kessler syndrome: threatens every neighboring satellite at the same altitude"}
  - {label: "Cost of a false alarm", value: "fuel depletion + noise for the operator", note: "unnecessary maneuvers, after which a real warning gets lost"}
  - {label: "Classical mode", value: "government networks, named, no figure found", note: "less frequent radar imaging, a coarser detection threshold"}
  - {label: "The model (LeoLabs)", value: "up to 400% more warnings", note: "11 radars at 7 sites, detection from 2 cm; ~$60 million in annual contracts in 2026", key: true}
in_bucket: true
status: draft
---

## Visible slide text

**An honest caveat.** Sources don't state how many maneuvers satellites actually performed in response to these warnings in 2026 — a warning issued ≠ a maneuver performed.

**For contrast.** With Starlink, the automation both warns and maneuvers itself — there's no third party at all.

*Classification (prioritization) on structured data.*

## Speaker notes

This case study is the fourth in the section, added as an explicit exception to the "up to three case studies per section" rule: it answers a question the industry overview left open — satellites grew ~12× in ten years, so what happens with that growth next, when you have to decide which two objects might collide?

The cost of a missed close approach is losing a satellite, and worse, a debris cascade threatening every neighboring satellite at the same altitude. The cost of the opposite error is too-frequent, low-quality warnings: fuel wasted on unnecessary maneuvers and operator overload, after which a real warning risks getting lost in the noise.

The classical mode (column b): before dense commercial radar networks, the catalog was maintained by government networks with less frequent imaging and a coarser detection threshold; what share of close approaches that network missed, no figure is named.

The model: LeoLabs is a commercial radar network for low Earth orbit, with 11 operating radars at 7 sites as of 2026; the company entered 2026 with annual contracts worth ~$60 million (including a SpaceWERX STRATFI grant for a new UHF radar in the Indo-Pacific, announced in March 2026), plus a NASA Space Act agreement. It detects objects from 2 cm. Its own model doesn't predict a collision directly — it prioritizes which object is most worth the radar observing next given limited time, predicting the probability of getting a good-quality measurement. There are 3–5 close approaches of large objects a week, and accounting for small debris the risk is estimated at 20 times higher; warnings prioritized by the model come out up to 400% more often.

The arbitration: the decision to maneuver stays entirely with the specific satellite's operator; LeoLabs only warns. What moved over: the decision of "what to observe next" moved from a pre-set rule onto the model; the decision of "whether to maneuver or not" didn't move anywhere.
