---
id: s03
local_id: I-03
section: "0. Introduction"
type: norm
title: "Satellites and data grew by an order of magnitude"
assertion: "Satellites grew ~12× in 10 years, data grew by a multiple more: this can no longer be served by hand"
source: "[Union of Concerned Scientists](https://www.ucsusa.org/resources/satellite-database) · [planet4589.org (J. McDowell)](https://planet4589.org/) · [CelesTrak](https://celestrak.org/) · [BryceTech](https://brycetech.com/) · [NASA EOSDIS](https://www.earthdata.nasa.gov/) · [Copernicus/DLR](https://www.copernicus.eu/en)"
media: ""
media_needed: "Phase 7 (issue #317): replaced with a tick-mark axis (`scheme: kind: shkala`) for the satellite count — the magnitude is visible from its position on the line. Starlink's share / launches / archive stayed as plates: a different unit, they don't belong on the same axis as the satellite count (`axis.py`: 'a form does NOT put values with DIFFERENT bases on one axis')."
scheme:
  kind: shkala
  unit: "active satellites in orbit"
  caption: "A ~12× increase in 10 years — more tasks than operators able to handle them by hand"
  from: 0
  marks:
    - {value: 1381, label: "2015"}
    - {value: 16800, label: "2026", key: true}
blocks:
  - {label: "Starlink's share of all active satellites", value: "~65%", note: "~11,100–11,150 satellites in one constellation"}
  - {label: "Copernicus (Sentinel) archive, 2018 → 2025", value: "9.7 → ~91 petabytes", note: "a ×9 increase in 7 years; EOSDIS by 2030 — ~600 petabytes", key: true}
in_bucket: false
status: draft
---

## Visible slide text

**Algorithms didn't get smarter on their own — the number of tasks grew faster than the number of operators able to handle them by hand.**

## Speaker notes

The second explosion is a direct, quantitative consequence of the first: once getting to orbit became several times cheaper, the number of things actually put into orbit jumped sharply. The number of active satellites grew ~12× in ten years — from 1,381 in 2015 to 16,800–17,100 today, according to independent tracking databases from Jonathan McDowell and CelesTrak. Of those, one constellation, Starlink, accounts on its own for about 65% of all active spacecraft in orbit.

The number of orbital launches per year grew from 87 in 2015 to 325 in 2025 — a quarter more year over year, while the number of satellites deployed grew by 54%: a modern launch carries, on average, more spacecraft at once than it did ten years ago. Of those 325 launches in 2025, SpaceX carried out 165 — about half of all launches worldwide.

In parallel, the volume of data coming down from satellites and needing processing is growing too. NASA's EOSDIS archive grew from 116 petabytes at the start of 2024 to a projected ~600 petabytes by 2030; the European Copernicus program's archive grew from 9.7 petabytes in 2018 to ~91 petabytes in 2025 — a ninefold increase in seven years. The German DLR archive grows by 15–30 terabytes a day.

These three numbers aren't three different stories but one: launch cost fell, the number of satellites grew by an order of magnitude, and the volume of data those satellites produce grows at the same pace. There are now more machines and more data in orbit than the old model — "one operator watches one system and reads every image by hand" — can physically service. That's exactly what explains why the issue of autonomy in space has become so acute right now, rather than a decade earlier or later — and why this growth in data comes back directly later in the lecture: it motivates the LeoLabs case study in Section 1 and is named directly as the reason for demand for computation in Section 4.
