---
id: s13
type: failure_case
duration_min: 1.5
assertion: "Plantix self-reports 85-90% accuracy (not independent). 10-15% misdiagnosis × 10M+ downloads = ~100k wrong pesticide recommendations per year. AP3 — threshold accuracy ≠ readiness for deployment. The alternative — calibrated confidence + abstention."
learning_goal: "AP3 + FP/FN dose-criticality breakdown"
learning_outcomes: [LO5]
chapter_ref: "§1.6 Part 1 — Strict-in F3 Plantix"
references: [frontiers-plant-2020-plantix, plantix-net]
visual:
  pattern: ui_screenshot_breakdown
  primary: "Left — Plantix mobile UI screenshot; right — FP/FN dose-criticality breakdown table + AP3 callout"
---

# Plantix — 10-15% misdiagnosis on 10M+ downloads

## Assertion

Plantix self-reports 85-90% accuracy (not independent). 10-15% misdiagnosis × 10M+ downloads = ~100k wrong pesticide recommendations per year. AP3 — threshold accuracy ≠ readiness for deployment. The alternative — calibrated confidence + abstention.

## Visual

A two-column layout.

**Left column (45%) — Plantix UI screenshot:**

A screenshot of the Plantix mobile app: a photo of a plant leaf with the diagnosis «Late Blight detected — 92% confidence» + a recommendation of a specific fungicide. Caption 12pt italic below the screenshot: «Plantix.net mobile app · 10M+ downloads · primary market: smallholders in India (7M active)».

**Right column (55%) — breakdown + alternative:**

A mini-table in an Ocean rounded box, 3 rows (FP / FN / Alternative) × 3 columns (type / dose-criticality / error class):

| Type | Example | Dose-criticality |
|---|---|---|
| **False-positive** | «disease X», the plant is actually healthy | low (nitrogen overdose) → high (category B pesticides in fruit) |
| **False-negative** | «all fine», there is actually a fungal infection | medium (missed nutrient) → high (missed systemic viral infection) |
| **Geographic asymmetry** | Plantix is trained on Indian / SEA diseases | for Russia / East Africa — accuracy falls below the claimed level |

Below the mini-table — a callout with **gold accent** in an Ocean rounded box:
- **AP3. Threshold accuracy ≠ readiness for deployment.** 90% accuracy at scale = ~100k wrong recommendations / year.
- **Alternative:** calibrated confidence + abstention. When confidence < 80% → abstain + switch to a local extension agent.
- **Engineering pattern:** ensemble methods (Monte Carlo Dropout, Deep Ensembles), +30% inference time. **A working production pattern**, not a research idea.

Footer 12pt italic: «Source for 85-90% accuracy — self-reported Plantix (Frontiers in Plant Science 2020). Independent field validation is absent».

## Speaker notes

The third first-level failure is Plantix, a smartphone app that identifies a plant disease from a photo of a leaf and recommends a pesticide. Per Plantix's claims, the app has been downloaded more than ten million times, with about seven million active users in India, and a diagnostic accuracy of eighty-five to ninety percent on their own dataset. This is a popular example of "AI for smallholders": a free app that replaces an in-person visit from an agronomist where agronomists are scarce.

The failure mechanism matters in the details. The claimed accuracy is Plantix's self-assessment on their own image dataset, not an independent field validation. Real accuracy under field conditions is lower due to many factors: photo quality, disease stage, individual crop variability, the specific cultivar. Even if we grant ninety percent accuracy on ten million downloads and assume that only ten percent of downloads lead to a pesticide-application decision — that's about one hundred thousand wrong pesticide recommendations per year. Each such recommendation is either an incorrect application of chemicals with risk to the farmer's and consumer's health, or the absence of application where it is needed.

The breakdown on the right — ten to fifteen percent misdiagnosis by type. False-positive: the model recognized a disease, but the plant is actually healthy or has a different disease. Dose-criticality varies: if the recommendation is to treat with a nitrogen foliar fertilizer, the damage from the error is low; if with a systemic pesticide of a specific class, the damage is medium — yield loss from chemical stress; if with a category-B organochlorine insecticide, the damage is high — residue in the fruit and a health risk. False-negative: the model failed to recognize a disease and advised "all fine". A missed nutrient deficiency is treated in the next cycle; a missed fungal infection lowers yield by ten to thirty percent; a missed systemic viral infection like ToBRFV can destroy more than fifty percent of the planting.

An additional characteristic — geographic asymmetry. Plantix is trained predominantly on diseases dominant in India and Southeast Asia — fall armyworm, rice brown spot, rice blast, potato late blight. Applied under Russian conditions or in East Africa to cultivars not in the training set — accuracy falls below the claimed level. This is the same applicability gap as in L3 for Holstein bias, which we'll move to in Section 3.

And the main anti-AI criterion of the slide — AP-three. Threshold accuracy does not equal readiness for deployment. Ninety percent on a benchmark does not guarantee deployment quality. The alternative on the right — calibrated confidence plus abstention. The ML model estimates not only the disease class but also an uncertainty estimate for each prediction. When confidence is below eighty percent — abstain from the recommendation, switch to "contact a local extension agent". This is a working engineering pattern, not a "research idea"; it's implemented in production at several medical AI startups from Lecture 7 and appears in state-of-the-art plant-disease classification in the academic literature of 2024-2025.

## Sources

- Frontiers in Plant Science (2020) — Plantix accuracy self-report.
- Plantix.net — official product info.
