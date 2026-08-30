---
id: s16
type: working_case
duration_min: 2.5
assertion: "250,000 acres treated, 15 billion weeds destroyed, 14 countries. $1.4M / machine. 240W laser + CNN on 40M images. Replacing chemistry with physics — a narrow substitution, not an «autonomous tractor»."
learning_goal: "Working case L2: narrow niche + replacing physics with physics + measurable ROI"
learning_outcomes: [LO1a, LO1b]
chapter_ref: "§2.2 Part 1 — LaserWeeder G2 deep dive"
references: [carbon-robotics-2025-businesswire, geekwire-2025]
visual:
  pattern: photo_hero_spec_grid
  primary: "Hero photo of LaserWeeder G2 in the field (Carbon Robotics press) + 3-card spec (metrics / architecture / limitations) + per-acre economics callout"
---

# Carbon Robotics LaserWeeder G2 — the canonical L2 success

## Assertion

250,000 acres treated, 15 billion weeds destroyed, 14 countries. $1.4M / machine. 240W laser + CNN on 40M images. Replacing chemistry with physics — a narrow substitution, not an «autonomous tractor».

## Visual

At the top (45% of the slide height) — a hero photo of the LaserWeeder G2 in the field, the machine towed behind a tractor, cameras and lasers visible along the boom. Framed in an Ocean rounded box. Caption below 12pt: «Carbon Robotics LaserWeeder G2 launch, February 2025. Source: carbonrobotics.com press».

Below the photo — a 3-column spec grid in Ocean rounded boxes:

**Column 1 — 2025 metrics:**
- **250,000 acres treated** ★ gold
- 15 billion weeds destroyed
- 150 machines in 14 countries
- $1.4M / machine

**Column 2 — Architecture:**
- 240W water-cooled diode laser
- 25 ms pulse, 1-2 J energy
- 25k weeds / hour throughput
- CNN on 40M images, 100+ crop species
- Modular boom 6.6-60 feet (G2 Feb 2025)

**Column 3 — Limitations:**
- Daytime only (CV requires light)
- Doesn't work in heavy dust
- ~5 tons without a tow vehicle
- Not for commodity row crops
- Not for high-density crops (sweet corn)

Bottom callout 14pt italic in a Teal-tint box: «**Per-acre economics:** replaces $200-400/acre of herbicide treatment (vegetables); payback 3-4 years for a large farm (1000+ acres) with high-margin crops. **A narrow but genuinely working category** — organic, herbicide-free, specialized vegetables».

Footer 12pt italic: «Sources: Carbon Robotics businesswire 2025-02-10; GeekWire 2025; CES 2025 demo».

## Speaker notes

The canonical success case of the second rung in 2026 is the Carbon Robotics LaserWeeder G2. This is a machine towed behind a tractor across the field that destroys weeds with a laser pulse based on computer vision. Replacing chemistry with physics.

The architecture. Downward-pointing cameras are mounted along the machine's boom; the number depends on the width — from six to sixty feet; the G2 model, unveiled in February 2025, is modular. Each camera scans the ground in real time; a convolutional neural network trained on forty million labeled images distinguishes crop plants from weeds — the model recognizes more than one hundred crop species. When a weed is detected, a two-hundred-forty-watt laser is aimed at the point and delivers a pulse of about twenty-five milliseconds that burns out the meristem — the weed's growing point. The plant dies; the soil and crop plants are not damaged. No chemicals.

The 2025 metrics. Carbon Robotics reports: more than two hundred fifty thousand acres treated by LaserWeeder machines; more than fifteen billion weeds destroyed; about one hundred fifty machines deployed in fourteen countries; the cost of a machine — about one million four hundred thousand dollars per unit.

What makes the case canonical. Three structural conditions, analogous to See & Spray but with different emphases. First — a narrow task with a direct alternative: not an "AI-managed tractor", but laser destruction of weeds instead of chemical. The alternative — herbicides — is well known, as are its cost and risks. The difference in outcome is counted directly: gallons of herbicide saved times price times area. Second — replacing physics with physics, not talk of replacing a human. The LaserWeeder replaces neither the agronomist nor the farmer; it replaces the chemical spray with a laser. A very narrow substitution in which the gain is clear — no chemical residue on the crop and in the soil. Third — the gradualness of deployment. One point four million per machine is not an object of mass demand; it's a solution for large vegetable and specialized farms.

Limitations and caveats. The LaserWeeder's laser is a diode, two hundred forty watts of peak power, water-cooled. Power consumption is on the order of thirty to fifty kilowatts per machine; it runs off a generator on the towing tractor or off its own battery pack. This is high-energy electrical consumption — one of the main caveats: the machine is not an "eco-friendly replacement for herbicides" in the broad sense, since it shifts the ecological footprint from chemistry to electricity.

ML failure modes — when weed and crop are visually similar. A concrete example: pigweed in spinach. Pigweed and spinach are both of the amaranthus family; at the two-to-three-leaf stage their foliage is morphologically similar; the model may flag spinach as a weed and burn it with the laser. Carbon Robotics documents this failure mode and sells a "calibration mode" for test field runs before production treatment.

Per-acre economics. The cost of herbicide treatment in the US for vegetable crops is two hundred to four hundred dollars per acre per year. The LaserWeeder replaces this chemistry; the payback period is three to four years for a large farm with high-margin crops. Limitations: doesn't work in high-density crops with dense planting; doesn't work in muddy conditions; requires electrical power.

This is a working category: organic producers, specialized vegetable farms, buyer hostility to chemical residues. This is specialization in L2.

## Sources

- Carbon Robotics businesswire press (2025-02-10).
- GeekWire (2025).
- CES 2025 demo coverage.
