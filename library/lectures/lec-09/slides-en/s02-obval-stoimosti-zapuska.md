---
id: s02
local_id: I-02
section: "0. Introduction"
type: norm
title: "The collapse in launch cost — the lecture's foundation"
assertion: "Delivering a kilogram to orbit got 18–20 times cheaper over two decades — the foundation of the whole lecture"
source: "[Harry W. Jones, «The Recent Large Reduction in Space Launch Cost», NASA NTRS](https://ntrs.nasa.gov/citations/20200001093)"
media: ""
media_needed: "Phase 7 (issue #317): replaced with timeline bars (`timeline: mode: sroki`) — the bar's length carries 'how many times cheaper', as the form catalog intended. A tick-mark axis (`scheme: kind: shkala`) was tried first and rolled back: with an 18–20× spread, two close marks (2,900 and 6,000) land right at the line's leftmost edge, and the tick label's width (a third of the frame, set by the number of ticks, not by text length) pushes the label past the left margin — a structural limitation of `axis.py` on a value cluster at the edge, not a deck typo. QuickChart wasn't needed."
timeline:
  mode: sroki
  unit: "$ per kilogram of cargo to orbit"
  caption: "An 18–20× drop — not gradual, but a step change: first-stage reusability"
  rows:
    - {label: "Space Shuttle, 1981–2011", value: 54500}
    - {label: "Today's rideshare launch — cargo below rated capacity", value: 6000}
    - {label: "Falcon 9, reusable, 2024–2026", value: 2900}
in_bucket: false
status: draft
---

## Visible slide text

**There is one named cause: first-stage reusability.** 39 Falcon 9 boosters have flown an average of 14.9 times each — the rocket became an asset, not a consumable.

**An important caveat for every number that follows.** $2,700–3,140/kg is a price list divided by rated payload capacity, not the actual cost of a specific launch. For a satellite on a rideshare launch, the price is closer to $6,000/kg.

## Speaker notes

Let's start with the number that anchors everything that follows. The Space Shuttle, from 1981 to 2011, cost on average, across its entire program budget, about $54,500 per kilogram of payload to orbit — that isn't the price of one flight, it's the whole program's economics: development, infrastructure, upkeep between flights, divided by its rated payload capacity of 27,500 kilograms. Against that — today's reusable Falcon 9: its current price list gives about $2,700–3,140 per kilogram. The difference is an 18–20× drop, and that number isn't there for slide polish: it comes from the same peer-reviewed NASA paper (Harry Jones, NASA NTRS) that calculated the Shuttle's number too.

There is one named cause for the drop: first-stage reusability. At the time of the count, SpaceX had 39 boosters in circulation, flying an average of 14.9 times each. A rocket that isn't thrown away after one flight stops being counted as a consumable — it becomes an asset you can use dozens of times over.

And right away — an honest caveat worth keeping in mind for every number later in the lecture: the $2,700–3,140/kg price is a price list divided by rated payload capacity, not the actual cost of a specific launch with a specific payload. If the cargo is below the rated capacity, or flies as part of a rideshare launch, the price per kilogram for it is higher — closer to $6,000, twice the average. This doesn't disprove the 18–20× drop, but it does mean: the number is an order-of-magnitude reference point, not an exact price for any specific cargo. That same habit — asking "is this an average or a specific figure, what's the base it's calculated from, has it been reproduced" — will be useful for every number later in the lecture, including AEGIS's "93% hit rate" and AIFS's "~2.5 minutes per forecast".
