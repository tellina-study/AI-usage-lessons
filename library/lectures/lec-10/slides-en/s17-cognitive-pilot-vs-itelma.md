---
id: s17
type: architecture_comparison
duration_min: 2.5
assertion: "Cognitive Pilot CV: 1700+ installations (~1.3% of ≈130k combines in Russia; vendor self-report May 2024; [VFY-day-of]) + 4 farmer lawsuits for ₽12.7M over CV failures in dust. ITELMA Kvadro multi-GNSS sensor-fusion: GLONASS+GPS+Galileo+BeiDou + RTK 2-5 cm. This is NOT AI vs non-AI; it's one class of AI vs another class of AI."
learning_goal: "AP2a architectural choice within the AI domain; «where am I» vs «what do I see»"
learning_outcomes: [LO1b, LO5]
chapter_ref: "§2.7 Part 2 — Russia parallel Cognitive Pilot vs ITELMA"
references: [rtvi-2025-cognitive, fontanka-2026-itelma]
visual:
  pattern: schema_architecture_comparison
  primary: "2-col comparison: Cognitive Pilot CV-stack (what do I see) vs ITELMA sensor-fusion stack (where am I) + iconography + AP2a callout"
---

# Cognitive Pilot vs ITELMA — an architectural choice within the AI domain

## Assertion

Cognitive Pilot CV: 1700+ installations (~1.3% of ≈130k combines in Russia; vendor self-report May 2024) + 4 farmer lawsuits for ₽12.7M over CV failures in dust. ITELMA Kvadro multi-GNSS sensor-fusion: GLONASS+GPS+Galileo+BeiDou + RTK 2-5 cm. This is NOT AI vs non-AI; it's one class of AI vs another class of AI.

## Visual

A two-column layout. **2-col comparison schema** with an explicit contrast of architectures.

**Left column — Cognitive Pilot (CV-AI):**
- Icon `eye` 64px Primary mid at top + label «What do I see»
- Architecture: camera → CNN detector of the uncut-field edge
- Metrics: **1700+ installations** (~1.3% of ≈130k combines in Russia; vendor self-report)
- Claimed effects: +25% productivity, –13% grain loss
- **Failure mode** ★: 4 farmer lawsuits for **₽12.7M** over CV failures in dust / low sun / rain → the edge isn't "read"
- Failure type: a classic CV failure of dust and lighting (the same as FarmWise)

**Right column — ITELMA Kvadro (Sensor-fusion AI):**
- Icon `satellite-dish` 64px Primary mid at top + label «Where am I»
- Architecture: multi-GNSS → Kalman filtering → autopilot
- Sensor stack: **GLONASS + GPS + Galileo + BeiDou + RTK + Kalman**
- Accuracy: **2-5 cm** ★ gold
- Deployment: on «Kirovets» (K-7M) from late 2025
- **Failure mode:** requires functioning satellite reception (GNSS-jamming problem — see S4-bis)

Below the two columns — the main callout 18pt italic in a Teal-tint box:
- **These are NOT competitors — they cover different functions.**
- The correct solution for a modern autonomous combine is a **combination of both**: GNSS navigation (where am I) primary + CV (what do I see) secondary.
- The «one is better than the other» comparison is a false simplification.

Bottom callout with **gold accent** in an Ocean rounded box:
- **AP2a. Architectural choice within the AI domain.** When a CV stack can't withstand the open environment — another class of AI solution (sensor-fusion AI) may be more robust.
- **AP2a ≠ AP2b** (AP2b — a non-AI alternative, not «another class of AI»).

Footer 12pt italic: «Sources: RTVI 2025 (Cognitive Pilot lawsuits); Fontanka 2026-01-26 (ITELMA at PTZ)».

## Speaker notes

The Russia parallel of Section 2 requires special attention, because this is an important case of architectural choice within the AI domain — and one of the places where the simplistic interpretation "AI versus non-AI" leads to the wrong conclusion.

Cognitive Agro Pilot is a computer-vision-based autopilot system for combines, a subsidiary of Sberbank and SberAgro. A camera mounted on the combine's cab recognizes the edge of the uncut field — the visual boundary between the already-cut and the uncut strip — and passes the signal to the onboard computer, which corrects the trajectory. Per the company's data as of May 2024, more than one thousand seven hundred installations on combines of Russian and foreign manufacturers (about one point three percent of roughly one hundred thirty thousand combines in Russia per Minselkhoz data). The claimed effects — plus twenty-five percent productivity, minus thirteen percent grain loss. This is a CV solution: the task is to recognize a visual feature and steer the machine along it.

In 2025 a problem surfaced. Four lawsuits from farmers for twelve million seven hundred thousand rubles against Cognitive Pilot over cases when the CV system couldn't handle the conditions: in heavy dust, typical during grain harvesting on fields with sandy or dry soils, in low sun, in rain — the edge stopped being read, and the combine began veering off the line or stopping. This is a classic CV failure of dust and lighting — the same as in FarmWise.

The alternative solution is ITELMA. In late 2025 the Russian company ITELMA, part of the Tractor Plants group, rolled out a satellite autopilot under the "Itelma Kvadro" brand on «Kirovets» K-7M models. And this is a different architecture — not CV. The machine determines its position in the field through processing signals from several GNSS constellations: GLONASS plus GPS plus Galileo plus BeiDou — with RTK corrections giving accuracy of two to five centimeters, plus Kalman filtering for smoothing and compensating for delays. This is sensor-fusion AI: machine learning works at the level of processing sensor data and predicting position, but not at the level of "visually recognize the field boundary". This class of solution is more robust to dust because it doesn't depend on optics, but requires functioning satellite reception — in GNSS-jamming zones, which we'll return to in Section 4-bis, this becomes a separate problem.

And the main point. These two solutions are not competitors but cover different functions. ITELMA is "where am I": precise field navigation with two-to-five-centimeter accuracy based on the satellite signal. Cognitive Pilot is "what do I see": CV recognition of the uncut edge, obstacles, contours. These are different classes of task, and the engineering-correct solution for a modern autonomous combine is a combination of both. GNSS navigation as primary plus CV as secondary for recognizing nonstandard situations. The "one is better than the other" comparison is a false simplification.

And this gives us the anti-AI criterion AP-two-a — architectural choice within the AI domain. When one class of AI solution, for example CV, structurally doesn't work in a given environment — another class of AI solution, for example sensor-fusion AI on multi-GNSS, may be more robust. The alternative is not "non-AI", but "a different AI architecture". This is critically different from AP-two-b — a genuine non-AI alternative — which we discussed in the FarmWise case. AP-two-a and AP-two-b are two different categories, and not confusing them is the main value of this section.

## Sources

- RTVI (2025) — Cognitive Pilot farmer lawsuits.
- Fontanka (2026-01-26) — ITELMA «Kvadro» at PTZ.
