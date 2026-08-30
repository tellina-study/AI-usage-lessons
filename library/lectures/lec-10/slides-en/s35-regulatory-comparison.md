---
id: s35
type: regulatory_comparison
duration_min: 2
assertion: "EU AI Act high-risk for autonomous ag-machinery (Regulation 2024/1689, in force since February 2025) + AI literacy for operators + liability cascade. USDA AI Strategy is formal. Russia's «Agriculture of the Future» 2026-2030 is declarative (the prior program failed its goals — agriculture 2024 –3.2%)."
learning_goal: "Regulatory comparison of three jurisdictions"
learning_outcomes: [LO1b]
chapter_ref: "§5.3 Part 3 — Regulation"
references: [eu-2024-ai-act, usda-ai-strategy-2025, government-rf-31-12-2025]
visual:
  pattern: 3col_comparison
  primary: "3-col regulatory comparison (EU AI Act / USDA / Russia «Agriculture of the Future») with flag icons + status badges"
---

# Regulation — EU AI Act vs USDA vs «Agriculture of the Future»

## Assertion

EU AI Act high-risk for autonomous ag-machinery (Regulation 2024/1689, in force since February 2025) + AI literacy for operators + liability cascade. USDA AI Strategy is formal. Russia's «Agriculture of the Future» 2026-2030 is declarative (the prior program failed its goals — agriculture 2024 –3.2%).

## Visual

Below the 28pt bold assertion — a 3-column comparison grid, each column in an Ocean rounded box with a flag icon at the top:

**Column 1 — EU AI Act** (EU flag at top, status: ◉ implemented):
- **Regulation 2024/1689** (August 2024)
- Agricultural machinery with AI safety components = **HIGH-RISK** ★ gold
- Since **February 2025** — AI literacy for operators mandatory
- **Compliance teams** for manufacturers (XAG, AGCO, Bonsai, Naïo, and eventually Cognitive Pilot/ITELMA when exporting to the EU)
- Mandatory pre-market conformity assessment
- Technical file + logs
- **Liability cascade**: manufacturer + AI provider + farmer in an autonomous collision

**Column 2 — USDA AI Strategy** (US flag, status: ◐ formal-only):
- **FY 2025-2026 Strategy** published
- Largely **declarative**
- Combined with the cancellation of Climate-Smart (April 2025) — US agriculture-AI regulation is **not as developed** as the European
- Regulation via **FCC** (drones), **FTC** (vendor lock-in), **USDA** (programs) — not via a single AI regulator
- Standards ISO 17532:2007 + ISO 19115 — not «hard» like DO-178C in aviation

**Column 3 — Russia «Agriculture of the Future»** (Russian flag, status: ✗ declarative):
- Russian Government Decree of **December 31, 2025**, 2026-2030
- Successor to «Digital Agriculture» 2019-2024
- **The goal of doubling productivity NOT achieved**: agriculture in 2024 –3.2% ★
- Real metrics: **digitalization index 27.2/100** (Yakov & Partners 2024)
- **A program document ≠ a real result**

Bottom callout 14pt italic in a Teal-tint box: «**The lesson for an engineer:** assessing the Russian agriculture-AI landscape by press releases, you systematically overestimate the industry's maturity. The real metrics — the digitalization index, which is not closed by declarations».

Footer 12pt italic: «Sources: EU Regulation 2024/1689; USDA AI Strategy FY2025-26; Russian Government Decree 31.12.2025; Cambridge EJRR 2024».

## Speaker notes

The third environmental condition — regulation. Here 2024-2026 produced three significant documents an engineer should know about.

The EU AI Act — Regulation 2024/1689 — came into force in August 2024. Agricultural machinery with AI safety components is a high-risk classification under this law. This means: manufacturers — XAG, AGCO, Bonsai Robotics, Naïo Technologies, and eventually Cognitive Pilot and ITELMA when exporting to the EU — need compliance teams; a mandatory pre-market conformity assessment; a mandatory technical file and logs; a liability cascade — the tractor manufacturer plus the AI provider plus the farmer in an autonomous collision. Since February 2025 a requirement for AI literacy for operators has been in force — a farmer operating a high-risk AI machine must be trained. This is the most serious regulation of AI in agriculture in the world as of 2026.

The USDA AI Strategy FY 2025-2026 — formally published, but largely declarative. Combined with the cancellation of Climate-Smart Commodities in April 2025, which we discussed on the previous slides, it shows: US agriculture-AI regulation is not as developed as the European. In the US, the main regulation of AgTech goes through the FCC — drones, the FTC — vendor lock-in, the USDA — programs, not through a single AI regulator.

Russia — the program "Agriculture of the Future" 2026-2030, a Government Decree of December thirty-first, 2025. This is a declarative program inheriting the structure of the previous "Digital Agriculture" 2019-2024, whose goal — doubling agricultural productivity — was not achieved. Agriculture in 2024 showed minus three point two percent. This is an important lesson: a declarative program document does not equal a real result. An engineer assessing the Russian agriculture-AI landscape by ministerial press releases systematically overestimates the industry's maturity. The real metrics — the agriculture digitalization index of twenty-seven point two out of one hundred per Yakov & Partners 2024 — a structural gap that is not closed by declarations.

Standards. ISO 17532:2007 plus ISO 19115 for farm data exist, but they're not "hard" like DO-178C in aviation — we examined this in Lecture 9. This is part of the historical regulatory vacuum in agriculture, and it explains why the best L1-L2 success cases are those where the vendors themselves invest in quality — Cargill, John Deere — rather than where a regulator prescribes.

The main practical conclusion of the environment section: connectivity, vendor lock-in, and regulation are the layer on which all the rungs of the ladder stand. Without AP-five, AP-six, and AP-seven — without edge ML, without a multi-vendor exit route, without direct measurement of carbon claims — no rung works sustainably. And these three anti-AI criteria plus the previous two — AP-one thermodynamics, AP-three accuracy threshold, AP-four generic LLM — make up the final five, which we'll move to in the next section.

## Sources

- EU Regulation 2024/1689 — AI Act.
- USDA AI Strategy FY 2025-26.
- Russian Government Decree of December 31, 2025.
- Cambridge EJRR (2024) — EU AI Act applied to agrifood.
