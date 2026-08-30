---
id: s23
type: working_case
duration_min: 2
assertion: "A collar with an accelerometer + 5-7 year battery + cloud analytics. Alerts: estrus / calving / lameness / mastitis / BRD. AI — early warning, not prescribing medication. Augmentation, not replacement."
learning_goal: "Working case L3: augmentation pattern + sensor + ML pipeline"
learning_outcomes: [LO1a, LO1b]
chapter_ref: "§3.2 Part 2 — Allflex SenseHub"
references: [merck-2025-sensehub-2m]
visual:
  pattern: photo_hero_3card
  primary: "Photo SenseHub ear-tag on a cow (Merck press) + 3-card flow (sensor → ML pipeline → alert) + 2M milestone gold accent"
---

# Allflex SenseHub — 2 million cows mounted

## Assertion

A collar with an accelerometer + 5-7 year battery + cloud analytics. Alerts: estrus / calving / lameness / mastitis / BRD. AI — early warning, not prescribing medication. Augmentation, not replacement.

## Visual

At the top (40% of the height) — a hero photo of SenseHub: a cow with a sensor collar, a dashboard UI in the background. Framed in an Ocean rounded box. Caption below 12pt italic: «Merck Animal Health · 2 million cows milestone 2025».

Below the photo — a large central figure — **2 million cows mounted** ★ gold accent (48pt bold).

Below the central figure — a 3-card flow grid:

**Card 1 — Sensor:**
- Collar: accelerometer + temperature + position
- Battery 5-7 years
- Wear — a built-in alert for replacement

**Card 2 — ML pipeline:**
- Cloud analytics, training on the individual baseline of each cow (per-cow baseline)
- Comparison of patterns against the herd baseline and the individual cow
- Inference on Merck's edge infrastructure

**Card 3 — Alert:**
- Estrus (reproductive cycle)
- Calving (birth)
- Lameness
- Mastitis
- BRD (Bovine Respiratory Disease)

Bottom callout 16pt italic in a Teal-tint box: «**AI — early warning, not prescribing medication**. The farmer / vet makes the decision based on the alert; AI performs the function of a signal at a scale impossible without sensors. **Augmentation, not replacement**».

Footer 12pt italic: «Source: Merck Animal Health newsroom 2025; SenseHub Cow Calf for beef breeding; SenseHub Feedlot».

## Speaker notes

SenseHub is a classic example of "AI as an augmentation, not a replacement". Augmentation, not replacement.

A collar on the cow measures, via an accelerometer, its activity, rest, and rumination time — that is, chewing. A cloud algorithm compares patterns against the herd baseline and the individual cow and issues an alert to the farmer: "Cow number three hundred forty-two — a thirty-percent drop in activity over the last twenty-four hours, elevated temperature, possibly the onset of mastitis".

The farmer or vet makes the decision based on the alert — conduct a physical exam, prescribe an antibiotic, isolate from the herd. AI doesn't prescribe medication and doesn't replace the vet; it performs the function of an early signal at a scale impossible without sensors. Thousands of cows on a large farm — you can't review each one visually. This is precisely the structural success: the task is narrow — detecting a deviation from the baseline, the result is measurable — the number of mastitis cases diagnosed earlier, reduced milk loss, the alternative — visual observation — is clear and its limitation is known.

SenseHub's technical stack. The collar contains an accelerometer, a temperature sensor, position tracking. The battery — five to seven years of operation, which is critical for the economics: the farmer doesn't replace the collar every two years. The ML pipeline in the cloud: training on the individual baseline of each cow — the system trains on the individual cow for the first weeks after installation, then monitors deviations. The alerts are typed: estrus — the reproductive cycle; calving — the onset of birth; lameness; mastitis; BRD — bovine respiratory disease.

The 2025 metric — two million cows mounted. This is a significant milestone: the number of cows with an active sensor as of 2025; it gives a tangible sense of the deployment size in a real industry.

Allflex is a brand of MSD Animal Health, which is itself part of Merck. In 2024-2025 MSD acquired Antelliq, Allflex's parent company, for three billion eight hundred fifty million dollars. This is a signal of market maturity: individual L3 startups become divisions of large corporations in the veterinary and dairy-equipment business. For an engineer this means: new entries into L3 in 2026 are harder, the market is consolidated, but architectural failures are also rarer — the leaders have gone through correction cycles.

## Sources

- Merck Animal Health newsroom (2025) — 2 million cows milestone.
- SenseHub product info (Allflex / Merck).
