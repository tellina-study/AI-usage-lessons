---
id: s07
type: working_case
duration_min: 2
assertion: "5 million acres in the 2025 season, –50% non-residual herbicides, +2.0 bushels of soybeans per acre. 36 cameras along the boom + a CNN trained on millions of labeled images (Deere/Blue River >1M). Edge ML on NVIDIA Jetson — latency <50 ms."
learning_goal: "Working case L1: narrow task + edge ML + measurable ROI"
learning_outcomes: [LO1a, LO1b]
chapter_ref: "§1.1 Part 1 — John Deere See & Spray Ultimate"
references: [agtechnavigator-2025-see-spray, deere-press-2025, growiwm-2024]
visual:
  pattern: photo_left_data_right
  primary: "Photo of See & Spray at work (Deere press) + 3-card data: 5M acres / –50% herbicides / +2.0 bushels soybeans · spec card: 36 cameras · CNN on >1M images · NVIDIA Jetson edge"
---

# See & Spray Ultimate — the canonical L1 success case

## Assertion

5 million acres in the 2025 season, –50% non-residual herbicides, +2.0 bushels of soybeans per acre. 36 cameras along the boom + a CNN trained on millions of labeled images (Deere/Blue River >1M). Edge ML on NVIDIA Jetson — latency <50 ms.

## Visual

On the left (60% width) — a photograph of a John Deere ExactApply sprayer with See & Spray Ultimate at work in a cotton or soybean field; cameras and nozzles are visible along the boom. The frame is set in an Ocean rounded box with a caption below: «John Deere ExactApply + See & Spray Ultimate · November 2025».

On the right (40% width) — three data cards in an Ocean rounded box, stacked vertically:
1. **5 million acres** in the 2025 season (area > the state of New Jersey) **gold accent**
2. **–50% non-residual herbicides** · savings of ~31 million gallons / season
3. **+2.0 bushels of soybeans / acre** (in the best cases — up to 4.8)

Below this — a 14pt spec card: «**Architecture:** 36 cameras along the boom · CNN detector + detection head · >1M labeled images (the 40M figure belongs to LaserWeeder G2 §2.2, a different case) · edge ML on NVIDIA Jetson · latency <50 ms».

Footer 12pt italic: «Sources: AgTechNavigator 2025-11-10; Deere press release November 2025; GrowIWM 2024».

## Speaker notes

Let's begin the climb up the ladder from the very lowest level — the open field. This is an environment of maximal unpredictability, and the canonical L1 success case of 2026 is the John Deere See & Spray Ultimate system.

This is not an "autonomous tractor" and not an "AI farm assistant". It's a narrow application of computer vision for the selective application of herbicides. On a standard R-series sprayer, thirty-six cameras are mounted along the boom, pointed downward. Each camera scans about two and a half thousand square feet per second at a speed of twenty-five kilometers per hour. The frames pass through a convolutional neural network trained on millions of labeled images (per the primary Deere and Blue River sources — more than one million; the forty-million figure often confused with See & Spray belongs to a different product — LaserWeeder G2 from Carbon Robotics, which we'll examine in Section 2); the model distinguishes a crop plant from a weed by leaf shape, texture, density, and context. If a weed is detected in the frame, the corresponding nozzle fires within milliseconds and injects a droplet of herbicide only at that point.

An important architectural decision — inference is performed on the device. On each boom section an edge GPU of the NVIDIA Jetson class is installed. The latency from pixel to nozzle must be less than fifty milliseconds, otherwise the weed has already passed under the boom. This is edge ML in its canonical form — not a simplification of cloud ML, but a structural architectural decision fit to the task. A cloud uplink at twenty-five kilometers per hour in fields with variable cellular coverage would be a single point of failure.

The 2025 metrics: the system is deployed across more than five million acres per season — that's an area larger than the state of New Jersey. The average reduction of non-residual herbicides is about fifty percent; savings of roughly thirty-one million gallons of mix per season; a soybean yield gain of two bushels per acre on average, in the best cases up to four point eight. This is a rare example of an AgTech solution in which the numbers are confirmed by independent agricultural extension-service reports.

What makes the case canonical? Three structural conditions. First — the task is narrow: selective spraying on the binary feature "crop or weed", not "optimize the whole field". Second — feedback arrives within the same season: the amount of herbicide is compared with last year's, the yield gain is assessed at harvest. Third — the alternative (blanket spraying) is well known, and the difference in outcome is easily counted in dollars. This is not "magic AI"; it's a narrow application of CV at a point where economics and measurability allow AI to pay off in one or two seasons.

And there is a caveat. See & Spray works only in John Deere ExactApply systems; outside the US Midwest a validation bias is documented — on cotton in Texas it works (Palmer amaranth is represented in the dataset), but in Brazil's Cerrado early pilot farms reported detection degradation on broadleaf weeds not represented in the training data. Every CV-AI product has a zone of applicability, and the promise of universal application beyond it is usually vendor maskirovka.

## Sources

- AgTechNavigator (2025-11-10) — 5M acres milestone.
- John Deere press release (November 2025).
- GrowIWM (2024) — Palmer amaranth detection deep-dive.
