---
id: s09
type: content
duration_min: 1.5
assertion: "Foundation models change the barrier to entry: a team of 3 fine-tunes TerraMind on thousands of images instead of millions. The risk — vendor concentration: the entire L1 industry is built on 2-3 models from IBM / NASA / ESA."
learning_goal: "Foundation model + RAG pattern + vendor concentration risk"
learning_outcomes: [LO1a]
chapter_ref: "§1.3 Part 1 — Foundation models 2026"
references: [ibm-research-2025-terramind, nasa-earth-2025-prithvi, arxiv-2505-agrifm]
visual:
  pattern: 2col_diagram
  primary: "Left — satellite imagery sample (Sentinel-2 multispectral) + diagram TerraMind multimodal transformer; right — vendor concentration risk callout + Prithvi-EO 2.0 cite"
---

# Foundation models 2026 — TerraMind, Prithvi-EO 2.0

## Assertion

Foundation models change the barrier to entry: a team of 3 fine-tunes TerraMind on thousands of images instead of millions. The risk — vendor concentration: the entire L1 industry is built on 2-3 models from IBM / NASA / ESA.

## Visual

A simplified layout — 3 key ideas, without term overload. The AgriFM disambiguation and architecture details are in the speaker notes.

**Left column (55%) — what TerraMind is:**
- At the top — a sample Sentinel-2 satellite image (10-meter resolution) in an Ocean rounded box. Caption 12pt italic: «Sentinel-2 / ESA Copernicus — the class of data for TerraMind».
- Below it — a short formula 14pt: «**TerraMind (IBM + ESA, 2025) = "GPT-3 for Earth observation"**. A team of 3 fine-tunes on thousands of images instead of millions — the barrier to entry fell by 2-3 orders of magnitude».

**Right column (45%) — two callouts:**
- Callout 1 (Ocean rounded box, GOLD accent): «**Vendor concentration risk.** The entire L1 industry rests on 2-3 foundation models from IBM / NASA / ESA. A model shutdown = teams lose capabilities all at once».
- Callout 2 (Ocean rounded box): «**Advisor architecture 2026:** foundation model + retrieval (RAG) to a local regulator + LLM generation + explicit abstention under low confidence».

Footer 12pt italic: «Sources: IBM Research, April 2025; NASA Earth Observatory, 2025».

## Speaker notes

Two developments in 2025 changed the picture of the first rung on a three-to-five-year horizon, and an engineer should know about them.

TerraMind — a foundation model from IBM Research and the European Space Agency, released into open access in 2025. This is the first "GPT-3 moment" model for Earth observation: pretrained on one trillion tokens of satellite data, supporting several modalities — optical imagery, synthetic-aperture radar, multispectral images, time series, IoT-sensor metadata, agronomic reports in textual form. A dual-scale architecture links local pixel-level and global region-level context. Application in agriculture: variable-rate prescriptions, field-level yield forecasting, crop-stress detection weeks before visible symptoms.

Prithvi-EO 2.0 — a continuation of the joint IBM and NASA project, a specialized foundation model for agromonitoring. The main improvements from 1.0 to 2.0 are deeper metadata understanding and temporal capability: the model can work with time series of the same field, not only snapshots.

What does this change for the engineer? Previously, every AgTech startup team trained its own convolutional network from scratch on its own labeled datasets — that required millions of images, millions of dollars, years of work. A foundation model shifts the balance: a team of three can fine-tune TerraMind on a specialized task using thousands of images instead of millions. This lowers the barrier to entry for university teams and small startups.

But at the same time it creates a systemic risk. If all L1 AgTech solutions are built on two or three foundation models, the reliability of the entire layer depends on the continuity of those models. Three classes of risk. First — model shutdown: a Hugging Face account is deleted or a license is changed. Second — support degradation: the model isn't updated, the training data grows stale. Third — geopolitical unavailability: sanction restrictions, export controls on ML models. Russian teams formally have open access to Prithvi-EO via Hugging Face, but fine-tuning requires a GPU cluster of NVIDIA H100s or A100s, which are themselves under sanction restrictions.

A small but important technical correction: AgriFM is a publication by research groups at the University of Hong Kong and Wuhan University in May 2025, not Carnegie Mellon, as it's sometimes stated in survey materials. Crop Wizard is a RAG-grounded advisory application, not a separate "Crop-LLM" foundation model. This is an example of misattribution that our own fact-checking skills work against.

The advisor architecture of 2026 is a pattern, not a model. A foundation layer as perception plus RAG to a local regulator plus an LLM on top for generating a recommendation plus explicit abstention under low confidence plus a human in the loop for critical decisions. We'll return to this pattern in every following failure story.

## Sources

- IBM Research blog (2025-04) — TerraMind.
- NASA Earth Observatory (2025) — Prithvi-EO 2.0.
- arXiv 2505.21357 (May 2025) — AgriFM (University of Hong Kong + Wuhan).
