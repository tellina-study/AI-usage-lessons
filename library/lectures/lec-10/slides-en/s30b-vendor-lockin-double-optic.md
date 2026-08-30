---
id: s30b
type: failure_case_double_optic
duration_min: 2.5
assertion: "May 2022: John Deere remote-brick of 27 units in Melitopol ($5M) — anti-theft success. January 2025: FTC v. Deere — decade-long repair restrictions. December 2025: FCC ban on DJI (80% of US ag-drones). One mechanism, two sides: an AI security feature today = an AI control surface tomorrow."
learning_goal: "AP6 + the double optic as a stand-alone framework"
learning_outcomes: [LO5]
chapter_ref: "§5.2 Part 3 — Vendor lock-in + Melitopol + FTC + FCC"
references: [register-2022-05-deere, ftc-2025-01-deere, north-dakota-monitor-2025-fcc-dji]
visual:
  pattern: schema_double_optic
  primary: "Double optic center diagram: one mechanism geo-locking + VIN-locking → 2 interpretations (Side A anti-theft / Side B vendor control); + 3 timeline events"
---

# Vendor lock-in — the double optic of John Deere

## Assertion

May 2022: John Deere remote-brick of 27 units in Melitopol ($5M) — anti-theft success. January 2025: FTC v. Deere — decade-long repair restrictions. December 2025: FCC ban on DJI (80% of US ag-drones). One mechanism, two sides: an AI security feature today = an AI control surface tomorrow.

## Visual

At the top center — a diagram of the "double optic". One central mechanism box: **«Geo-locking + VIN-locking»**. From it — two arrows in two directions:

**Side A (←):** **anti-theft success** (from the owner's viewpoint) — Mr/Mrs. Ukrainian farmer ★ + photo (Deere green tractor)
**Side B (→):** **vendor control surface** (from the dependent party's viewpoint) — a Russian farmer / FieldView user ★ + photo (a locked FieldView dashboard)

Above the diagram — a caption: «**One mechanism. Two sides. Seen from different positions**».

Below the diagram — 3 horizontal timeline events in Ocean rounded boxes:

**Event 1 — May 2022: Melitopol** (photo / map):
- John Deere remote-brick of 27 machines
- Transported from Melitopol to Chechnya (~1126 km)
- **$5 million** market value, wouldn't start
- The anti-theft AI worked by design (Side A)

**Event 2 — January 2025: FTC v. Deere** (photo of the FTC press conference):
- FTC + AG Illinois + AG Minnesota
- Decade-long repair restrictions
- Only Deere-authorized dealers have the **Service ADVISOR** software tool
- Trial 2026 (vendor control surface — Side B)

**Event 3 — December 2025: FCC ban on DJI** (icon + press headline):
- December 22, 2025: foreign-made drones on the Covered List
- **DJI = 80% of US ag-spray drone flights**
- Non-Chinese alternatives (Skydio, Geo-scan) **2.5× more expensive**
- Vendor lock-in at the geopolitical level

Bottom callout 14pt italic in a Teal-tint box: «**AP6. «AI-driven equipment» = a vendor lock-in trap.** The more AI and telematics, the stronger the vendor control surface. Alternative: open-source farming hardware (Farm Hack), the right to repair, a multi-vendor strategy, mechanical fallbacks».

Footer 12pt italic: «Sources: The Register 2022-05-02 (Melitopol); FTC press 2025-01-15; North Dakota Monitor 2025 (FCC DJI)».

## Speaker notes

The second environmental condition — vendor lock-in. And here we see a paradoxical double optic that an engineer must understand in full.

January 2025 — FTC versus John Deere. On January fifteenth, 2025, the US Federal Trade Commission, together with the attorneys general of Illinois and Minnesota, filed suit against Deere for unfair practices — decade-long restrictions on farmers' and independent repairers' ability to fix Deere equipment. Only Deere-authorized dealers have access to the Service ADVISOR software tool required for all full-functional repairs. A federal judge rejected Deere's attempt to dismiss the case; a trial is expected in the second half of 2026. What this means: a farmer doesn't "buy" a five-hundred-thousand-dollar combine with an AI stack — they license the right to use it as long as Deere permits. This is the same pattern as Tesla with the FSD subscription, but applied to agricultural equipment.

May 2022 — the John Deere remote-brick in Melitopol. In May 2022 Russian forces seized twenty-seven pieces of John Deere equipment from Melitopol in Zaporizhzhia Oblast and moved them to Chechnya — about one thousand one hundred twenty-six kilometers. On arrival the equipment wouldn't start. Deere remotely "bricked" all twenty-seven units via GPS plus VIN-locking. For those who stole them — five million dollars of lost market value. For Deere — a practical demonstration of remote control.

And here is the most methodologically important ethical point of the section. This point must be treated as a stand-alone framework, not as a footnote in the flow. One and the same mechanism yields two opposite interpretations depending on the side of observation.

Side A — anti-theft success. From the Ukrainian side's and the public's viewpoint — this is a victory of technology over war, a defense of private property. The stolen equipment was indeed stopped; the damage to the thief was five million. The AI function worked by design. This scenario is a legitimate anti-theft application of AI and IoT, an analog of Apple's Find My system for private property at an industrial scale.

Side B — vendor control surface. The same mechanism means that Deere can remotely disable any farmer's equipment: one who hasn't paid the subscription, hasn't signed an EULA update, ended up under sanctions, fell into a political rift. Russian farmers after February 2022 experienced this scenario in practice — the equipment is physically with them, but the cloud services, firmware updates, and the Service ADVISOR tool are unavailable. Climate FieldView left Russia in 2022 simultaneously with the exit of Bayer Crop Science; Russian agroholdings that had invested in FieldView lost access to the platform. Microsoft and Amazon left in that same 2022.

The engineering lesson. An AI security feature today is an AI control surface tomorrow. The same mechanism thanks to which a stolen combine doesn't work in Chechnya is a cause for concern for every farmer in any jurisdiction that falls into a political rift. Ownership of the equipment becomes fictitious — the farmer licenses the right to use, not owns the equipment with a built-in AI stack. The Russian experience after 2022 is a natural experiment illustrating what happens when an imported AI stack becomes unavailable. This is a universal lesson, not Russia-specific — it applies to any farmer in any peripheral country.

And December 2025 — the FCC ban on DJI and Autel. On December twenty-second, 2025, the FCC added all foreign-made drones plus UAS-critical components to the Covered List, banning new product authorizations. DJI occupies eighty percent of all ag-spray drone flights in the US; Chinese drones overall — about ninety percent of the market. In 2024 spray drones treated ten point three million acres in the US, about two hundred fifteen million in revenue from custom applications. Non-Chinese alternatives — Skydio, Geo-scan — are on average two and a half times more expensive. This same logic — vendor lock-in at the geopolitical level, cutting off the supply chain not because of AI quality but because of politics.

And the main anti-AI criterion — AP-six. AI-driven equipment is a vendor lock-in trap. The alternative: open-source farming hardware — Farm Hack, Open Source Ecology — the right to repair, a multi-vendor strategy with an explicit exit route, mechanical fallback — that is, readiness to operate without AI functions when they're switched off.

## Sources

- The Register (2022-05-02) — John Deere disables Ukraine tractors.
- FTC press release (2025-01-15) — FTC v. Deere.
- North Dakota Monitor (2025) — FCC ban DJI ag-drones.
- CSO Online 572811 — Melitopol analysis.
