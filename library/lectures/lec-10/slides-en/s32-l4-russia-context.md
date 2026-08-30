---
id: s32
type: russia_parallel
duration_min: 2
assertion: "X5 «Perekrestok» ML since 2020, 200+ factors — world-class. Magnit F&R split: Forecasting 46 DCs January 2026 in production; Replenishment pilot 3 DCs 2026. RSHB AI services claimed, no metrics. GigaChat — a demo episode, not a deployment."
learning_goal: "L4-L5 parity amid L1-L2 lag + Magnit nuance"
learning_outcomes: [LO1b]
chapter_ref: "§4.7 Part 2 — Russia parallel of Section 4"
references: [habr-magnit-2026, tadviser-x5]
visual:
  pattern: 4card_status_grid
  primary: "4-card status grid (X5 parity / Magnit hybrid Forecasting+Replenishment / RSHB vapor / GigaChat demo) with status icons"
---

# L4 Russia — X5 parity, Magnit hybrid, RSHB vapor

## Assertion

X5 «Perekrestok» ML since 2020, 200+ factors — world-class. Magnit F&R split: Forecasting 46 DCs January 2026 in production; Replenishment pilot 3 DCs 2026. RSHB AI services claimed, no metrics. GigaChat — a demo episode, not a deployment.

## Visual

Below the 28pt bold assertion — a 4-card status grid (2×2). Each card in an Ocean rounded box, with a status icon in the top-right corner:

**Card 1 — X5 «Perekrestok»** (status: ✓ parity, **gold**):
- ML since 2020 (6 years in production)
- **200+ factors**: historical demand, weather, day of week, local events, competitor prices, promotions, stock
- Categories — produce + dairy
- **World-class** (vs Tesco/Walmart since 2017 — a ~3-year gap, still narrowing)

**Card 2 — Magnit F&R** (status: ◐ hybrid):
- In-house development with Napoleon IT, split across 2 modules
- **Forecasting:** **46 DCs January 2026** ★ gold (production, network level)
- **Replenishment:** **pilot 3 DCs 2026**, plan 10-20 by early 2027, whole network by end of 2027
- IMPORTANT: «46 DCs» (v1 over-claim) and «3 DCs» (v2-v3 under-statement) — both formulations inaccurate; the correct one — **a modular split**

**Card 3 — RSHB «Svoyo Fermerstvo»** (status: ◯ vapor / claimed):
- 10,000 partners, 1.25M product SKUs (the number of platform users, not AI deployments)
- AI services (yield forecasting, geno-selection, advisory) — **claimed, no production metrics published**
- Misattribution warning (Section 8): the format «claimed N, no metrics», don't show as a deployment

**Card 4 — Sber GigaChat** (status: ✗ demo, not deployment):
- A 2025 episode — «passed an exam at a specialized university in agronomy»
- **A demo episode**, not a production deployment
- Demo quality (controlled environment, pre-prepared questions) ≠ production deployment quality

Bottom callout 14pt italic in a Teal-tint box: «**The main Russia lesson of Section 4:** there is parity with the world in L4-L5 retail supply (X5, Magnit's Forecasting) amid a significant lag in L1-L2. A structural unevenness across the ladder's rungs».

Footer 12pt italic: «Sources: Habr Magnit 2026-01 (F&R architecture); TAdviser X5 Tech 2024».

## Speaker notes

Russian L4 is paradoxically one of the most mature segments of agriculture-AI in the country, but with an important internal unevenness between the two main players.

X5 Group — Perekrestok, Pyaterochka, Chizhik — develops and operates production ML systems for demand forecasting since 2020. This is a stable production deployment with a six-year history of iterations. Per X5 Tech data, the system uses more than two hundred factors: historical demand, weather, day of week, local events, competitor prices, promotions, warehouse stock. The categories — produce and dairy. This is genuinely world-class: the architecture, data volume, and iteration history match the practice of Tesco, Walmart, Carrefour. The gap with the leaders — Tesco and Walmart since 2017 — is about three years, and it keeps narrowing.

Magnit F&R — Forecasting and Replenishment — an in-house development with participation from Napoleon IT. And here is an important nuance. The early formulation "46 DCs by January 2026" in the first version turned out to be an inaccurate over-claim for the whole F&R; the formulation "3 pilot DCs" in later versions is an under-statement for the Forecasting part. The correct formulation is a modular split. Forecasting, demand forecasting, is deployed in production at forty-six distribution centers in January 2026 — this is the network level for the forecasting half of the F&R stack. Replenishment, restocking — a pilot at three distribution centers in 2026, a plan to expand to ten-twenty by early 2027 and cover the whole network by the end of 2027.

This distinction matters. Half of the F&R stack is already network-wide in production, the second half is in the pilot phase. The statement "Russian retail ML is world-class" is correct for X5 end-to-end and for Magnit's Forecasting module. Magnit's full F&R stack lags the world leader by about nine years — Walmart Eden since 2017, Magnit F&R end-to-end by the end of 2027.

Rosselkhozbank is a different story. RSHB promotes the platform "Svoyo Fermerstvo"; per the bank's claims — more than ten thousand partners, one million two hundred fifty thousand product SKUs. In 2025-2026 it announced several AI services: AI yield forecasting, geno-selection, advisory chatbots. An important caveat: these services are claimed, but no confirmed independent production metrics have been published. This is the pattern "RSHB AI = claimed N, no metrics". Ten thousand partners is the number of platform users, not "ten thousand farms with a production AI deployment". Don't show it as a successful deployment.

Sber GigaChat, in one 2025 episode, was presented as "having passed an exam at a specialized university in agronomy" — this is a demonstration episode, not a production deployment. The quality of such demonstrations — pre-prepared questions, a controlled environment, question selection — is not comparable to a deployment in which the model answers arbitrary farmer questions in arbitrary contexts.

The main Russian lesson of the fourth section: there is parity with the world in L4-L5 retail supply — X5, Magnit's Forecasting — world-class — amid a significant lag in L1-L2 — field and robot. This unevenness across the ladder's rungs is a structural characteristic of Russian agriculture-AI in 2026, and it's explained by the same factors as the mirror asymmetry in the US — where L4-L5 are the most mature, L1-L2 the least — only in Russia sanction restrictions and vendor lock-in additionally play a role. We move to the general lesson about lock-in and the sanction shock right now in Section 4-bis.

## Sources

- Habr Magnit (2026-01) — F&R architecture.
- TAdviser X5 Tech (2024).
- RSHB Svoyo Fermerstvo (vendor self-report).
