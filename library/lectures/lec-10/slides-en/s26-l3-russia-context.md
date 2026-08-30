---
id: s26
type: russia_parallel
duration_min: 2
assertion: "Connectome.ai (Skolkovo) — a narrow CV task for monitoring calf births. DeLaval / GEA / Lely AI services in Russia are in a gray status — the equipment is physically at farmers', the cloud analytics depend on Europe. Lobnya 2026 — hardware substitution; the AI stack requires a separate trajectory."
learning_goal: "F9 vapor risk vs documented Microsoft Azure / FieldView precedent"
learning_outcomes: [LO1b]
chapter_ref: "§3.5 + §3.6 Part 2 — Russia parallel of Section 3"
references: [connectome-ai-skolkovo, business-stat-2026-lobnya]
visual:
  pattern: 2col_working_vs_uncertain
  primary: "Left — Connectome.ai working case (CV of births); right — sanctions impact map + Lobnya 2026 hardware substitution"
---

# L3 Russia — Connectome.ai + the sanction uncertainty of the dairy AI stack

## Assertion

Connectome.ai (Skolkovo) — a narrow CV task for monitoring calf births. DeLaval / GEA / Lely AI services in Russia are in a gray status — the equipment is physically at farmers', the cloud analytics depend on Europe. Lobnya 2026 — hardware substitution; the AI stack requires a separate trajectory.

## Visual

A two-column layout.

**Left column (50%) — Working case Connectome.ai:**

At the top — a UI screenshot (camera feed + alert overlay) of Connectome.ai newborn-calf detection in an Ocean rounded box.

Below the UI — 3-row info:
- **Connectome.ai** (a Skolkovo resident)
- A narrow CV task: monitoring the onset of labor in cows
- Camera in the calving barn → recognition → alert to the vet
- A parallel to Cargill Birdoo and CattleEye — a narrow task, measurable ROI

**Right column (50%) — Sanctions impact + Lobnya:**

At the top — a small map / infographic: imported dairy equipment in Russia (DeLaval / GEA / Lely) + the status of the AI services.

Below this — 2 mini-cards in an Ocean rounded box:

**Card 1 — DeLaval / GEA / Lely AI stack:**
- The equipment is **physically at farmers'**
- Cloud services — **gray status** (formally work, access unstable)
- **Documented vendor-departure precedent:** Microsoft Azure (March 2022); AWS (April 2022); Climate FieldView (2022) — this class of risk **has already materialized** in adjacent sectors
- F9 — extrapolation of the same class of risk to the dairy-equipment AI stack

**Card 2 — Lobnya 2026:**
- Dairy-equipment production («Packaging Systems») March 2026
- **₽4B** of investment
- **Hardware substitution** is underway; the **AI stack has no Russian analog** at a production level yet
- A structural gap

Bottom callout 14pt italic in a Teal-tint box: «**The lesson is universal, not Russia-specific:** this class of risk applies to any farm in any peripheral country dependent on a cloud-AI vendor from another jurisdiction».

Footer 12pt italic: «Sources: Connectome.ai (Skolkovo resident); BUSINESS-stat 2026 (Lobnya)».

## Speaker notes

Russian L3 is an example of how vendor lock-in turns into political risk through an industry-specific mechanism.

First — the working case. Connectome.ai — a Skolkovo resident. The company works on CV systems for monitoring the birth of calves: a camera in the calving barn recognizes the onset of labor and passes an alert to the vet. On average a farm loses ten to fifteen percent of calves absent timely intervention; early notification reduces losses. This is a narrow working solution for one narrow task — a parallel to Cargill Birdoo and CattleEye in the sense of "a narrow CV task with measurable ROI". Connectome.ai doesn't try to be a "universal dairy-AI platform" — and that's precisely why it functions.

Now — the structural gap. Most of the AI functionality in dairy-industry robotics — DeLaval VMS, GEA DairyMaster, Lely Astronaut — found itself in a gray status in Russia after 2022. The equipment is physically at the farms, but the AI services — cloud analytics, dashboards, predictive maintenance — require firmware updates and cloud services from Europe.

No confirmed public cases of "the DeLaval AI service was shut off at a Russian farm on date X" with explicit attribution have been recorded. However, a recorded vendor departure from an adjacent class has already happened and validates the architectural risk: Microsoft Azure stopped accepting new Russian customers in March 2022; AWS halted new registrations in April 2022; Climate FieldView (Bayer) left Russia in 2022 — Russian agroholdings lost access all at once. This is the documented baseline: a cloud-dependent AI service from a foreign jurisdiction has already been shut off in agriculture after 2022. F-nine is the transfer of the same class of risk to the dairy-equipment AI stack.

Partial import substitution has been launched: in Lobnya in March 2026 dairy-equipment production was announced by the company "Packaging Systems" with four billion rubles of investment. However the AI stack — cloud analytics, training models on big herd data — has no Russian analog at a production level yet. This is a structural gap. The hardware layer can be substituted — mechanics, metal structures, simple electronics — while the AI stack requires a separate substitution trajectory: models, data, training, infrastructure. These are different layers of import substitution, not one task.

The main lesson for an engineer not tied to the Russian context: this same class of risk applies to any farm in any peripheral country dependent on a cloud-AI vendor from another jurisdiction. The Russian case is a natural experiment illustrating what happens when an imported AI stack becomes unavailable. We'll return to this general lesson in Section 4-bis through the Melitopol remote-brick and FTC v. Deere.

## Sources

- Connectome.ai — Skolkovo resident.
- BUSINESS-stat (2026) — Lobnya dairy-equipment production.
