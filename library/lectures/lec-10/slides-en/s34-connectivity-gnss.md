---
id: s34
type: failure_case_environmental
duration_min: 2.5
assertion: "18% of American farms without internet at all. 123,000 flights with GNSS interference Q1 2025 (Finland unfarmable). Starlink banned in Russia April 2026. AP5 — cloud-first for off-grid = an architectural error. Alternative: edge ML / TinyML."
learning_goal: "AP5 + edge ML as a realistic architecture"
learning_outcomes: [LO5]
chapter_ref: "§5.1 Part 3 — Connectivity"
references: [icao-2025-gnss, stanford-itm-2025, broadband-now-2024]
visual:
  pattern: 3numbers_map
  primary: "3 large figures (18% / 123k / Starlink ban) + GNSS-jamming Finland map (Stanford ITM 2025 figure)"
---

# Connectivity — 18% of farms without internet + GNSS jamming

## Assertion

18% of American farms without internet at all. 123,000 flights with GNSS interference Q1 2025 (Finland unfarmable). Starlink banned in Russia April 2026. AP5 — cloud-first for off-grid = an architectural error. Alternative: edge ML / TinyML.

## Visual

A two-column layout.

**Left column (45%) — 3 large figures in Ocean rounded boxes (gold accent on the main one):**

1. **18% of American farms without internet** ★ gold (BroadbandNow / Feedstuffs 2024)
   - 39% of the rural population without broadband (vs 4% urban)
   - 40% fixed-line; 42% on cellular/satellite (unstable)

2. **123,000 flights with GNSS interference Q1 2025** (ICAO 2025)
   - Sources: Russian EW stations (a side effect of military operations)
   - Finland unfarmable: «areas of farms reportedly unfarmable using GNSS-based tractors and combines»
   - ICAO Assembly October 2025 formally condemned Russia

3. **Starlink banned in Russia April 2026** (6 months)
   - Single-vendor connectivity = single point of failure
   - Elon Musk 2022 — unilateral cutoff of Starlink for Ukraine as a precedent

**Right column (55%) — Map / figure + alternative:**

At the top — a GNSS-jamming Finland map / figure from the Stanford GPS Lab ITM 2025 paper in an Ocean rounded box. Caption 12pt italic: «Stanford GPS Lab ITM 2025 — ADS-B / LCM detection technology».

Below the map — a callout in a Teal-tint box:
- **AP5. Cloud-first for an off-grid farm = an architectural error.**
- **Alternative: edge-AI / TinyML / offline-first**
  - Models — megabytes instead of gigabytes
  - Compute — a microcontroller (ESP32, STM32) or an edge-GPU (Jetson Orin Nano)
  - Hybrid: cellular + LoRa + Starlink + RTK ground link for redundancy
- **Not «simpler AI»** — a different class of architecture fit to the environment's constraints

Bottom callout 14pt italic: «**Precision agriculture — a civilian casualty of military electronic warfare.** Auto-steering, variable-rate seeding — all fully dependent on GNSS».

Footer 12pt italic: «Sources: ICAO 2025 (report CH/FI/EE/LT/LV/PL); Stanford GPS Lab ITM 2025; BroadbandNow / Feedstuffs 2024».

## Speaker notes

The first environmental condition — connectivity. Most AgTech marketing of 2018-2023 relied on the scenario "cloud AI optimizes your tractor in real time via a constant uplink". This is a fantasy for most farms, and three concrete figures show why.

The first figure — eighteen percent of American farms without internet at all. Per BroadbandNow and Feedstuffs, eighteen percent of American farms have no internet access whatsoever. Only forty percent have a fixed-line connection — DSL, cable, fiber; the remaining forty-two percent are on cellular or satellite, which is unstable. Thirty-nine percent of the US rural population has no broadband access versus four percent of the urban. Deploying broadband on farmland would give the economy about sixty-five billion a year through yield gains at a deployment cost of thirty-five to forty billion — these are public estimates, not realized plans. Cloud-first AI for agriculture is an architectural error for the overwhelming majority of farms.

The second figure — GNSS jamming. Per ICAO — a report by representatives of Switzerland, Finland, Estonia, Lithuania, Latvia, Poland in 2025: nearly one hundred twenty-three thousand flights with GNSS interference in the first four months of 2025 alone. The ICAO Assembly in October 2025 formally condemned Russia for disrupting the GNSS signal of civil aviation. Since 2022 Russian EW systems aimed at the territory of Ukraine have had a side effect — jamming the GNSS signal over the territories of Finland, Estonia, Latvia, Lithuania. The Stanford GPS Lab publishes separate research on jamming-source detection technology. Finnish farmers report: areas of farms reportedly unfarmable using GNSS-based tractors and combines because of the interference from Russian EW installations. Precision agriculture — a civilian casualty of military electronic warfare. Auto-steering, variable-rate seeding, variable-rate spraying — all these functions are fully dependent on GNSS, and without it they turn into an ordinary tractor.

The third figure — Starlink as a solution and a new dependency. Starlink has become a de facto backbone for dispersed farms and for Africa. The cost — ninety dollars a month for the "excess capacity" mode, one hundred twenty for "limited". Reliability — snow, rain, physical obstructions. In Russia Starlink is banned from April thirtieth, 2026 for six months, which closes off one of the redundancy options for Russian farms. The main observation — single-vendor connectivity is a single point of failure. Elon Musk unilaterally cut off Starlink for Ukraine at a critical moment in 2022; the same logic applies to farmers in any jurisdiction.

And the main anti-AI criterion — AP-five. Cloud-first for an off-grid farm is an architectural error. The alternative: edge-AI and TinyML. This is machine learning executed on the device — a sensor, a gateway, a tractor cab, a cow collar — without a cloud uplink. Model sizes — megabytes instead of gigabytes; compute — on a microcontroller or edge-GPU instead of cloud GPUs. A hybrid architecture — cellular plus LoRa plus Starlink plus RTK ground link with redundancy — for critical operations. This is not "simpler AI"; it's a different class of AI architecture, where the model is designed for the environment's constraints from the start.

## Sources

- ICAO (2025) — GNSS-interference report (CH/FI/EE/LT/LV/PL).
- Stanford GPS Lab (ITM 2025) — Russia GNSS Spoofing detection.
- BroadbandNow / Feedstuffs (2024) — 18% of farms without internet.
