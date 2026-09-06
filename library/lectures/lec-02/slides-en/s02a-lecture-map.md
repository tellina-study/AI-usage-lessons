---
id: s02a
type: roadmap
section: "Section 0. Introduction"
duration_min: 0.5
assertion: "Lecture map — 7 sections"
learning_goal: "Route map across the inference pipeline + new section 'Model types and sizes'"
learning_outcomes: [LO1]
chapter_ref: "§Карта главы [for-slide-s02a]"
visual_brief: "7 horizontal cards (0 Introduction / 1 Tokenization / 2 Embeddings / 3 Attention / 4 Sampling / 5 Model types and sizes / 6 Wrap-up) with one-line descriptions; active Section 0 — gold outline. No chips, no minutes, no references to checklist assertions."
---

# Visible content

## Title bar
"Lecture map — 7 sections"

## Body
[7 horizontal cards, top to bottom; active card (Section 0) — gold outline]

**0. Introduction** — the frame and the pipeline as a whole *(active, gold outline)*

**1. Tokenization** — how the model sees your text

**2. Embeddings** — the space of meaning and the boundary of similarity

**3. Attention mechanism** — what matters right now: roles, caching, long context

**4. Sampling** — from distribution to token: temperature, determinism, invisible tokens

**5. Model types and sizes** — what models run on, multimodality, the 2026 landscape

**6. Wrap-up** — assembling the pipeline, recap of the mechanisms

## Speaker notes

A quick route map before we dive in. The lecture follows the inference pipeline: the order of sections mirrors the order of stages every one of your requests passes through.

Section 1 — tokenization: how the model sees text, why a "fixed" strawberry answer proves nothing, where number-chunking and glitch tokens come from. Section 2 — embeddings: the space of meaning, three different things that all get called "embedding," and the boundary where semantic similarity stops meaning usefulness. Section 3 — the attention mechanism: why a role-based prompt genuinely changes the answer; where caching economics comes from; what a one-million-token window can actually do. Section 4 — sampling: temperature, the reason T=0 doesn't give you determinism, structured output, and the invisible reasoning tokens you're paying for. Section 5 — new in this version of the course: model types and sizes — what a small model runs on versus a giant, what each class can do in terms of multimodality, and the landscape of specific models as of September 2026. Section 6 — wrap-up: the pipeline as a whole and a recap of the mechanisms we covered.

Keep the map in mind — it will keep you from getting lost in the details.
