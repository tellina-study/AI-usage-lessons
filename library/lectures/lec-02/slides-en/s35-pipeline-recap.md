---
id: s35
type: assertion_visual
subtype: schema_pipeline
section: "Section 6. Wrap-up"
duration_min: 2
assertion: "We've covered how the model works — let's assemble the picture: the new topics didn't add stages, they slotted into the existing ones"
learning_goal: "Recap assembly of the pipeline with new layers overlaid (KV-cache → attention, thinking → the loop, schema → sampling, glitch tokens → tokenization); diagnostic tree"
learning_outcomes: [LO1]
chapter_ref: "§5.1 (chapter-part3.md) [for-slide-s35]"
visual_brief: "Horizontal 4-stage pipeline with RIGHT_ARROW, Ocean rounded boxes: Tokenization → Embeddings → Attention → Sampling → 'next token' (gold) with a loop-arrow back. ABOVE/BELOW the stages — 4 overlay callout cards for new topics, each connected by a dotted line to its stage: 'glitch tokens → a vocabulary property at the tokenization stage', 'KV-cache → inside attention; prompt caching — an add-on at the request boundary', 'structured outputs → a sampling filter', 'reasoning tokens → the same loop, part of the output marked as a draft'. Overlay cards teal with gold outline."
---

# Visible content

## Title bar
"We've covered how the model works — let's assemble the picture"

## Body
[Horizontal 4-stage pipeline, RIGHT_ARROW, loop-arrow]

**Tokenization** → **Embeddings** → **Attention** → **Sampling** → *next token* ⟲

[4 overlay cards, dotted lines to their stages]
- **Glitch tokens** — a vocabulary property at the tokenization stage
- **KV-cache** — inside attention; **prompt caching** — an add-on on top of it at the request boundary
- **Structured outputs** — a filter at the sampling stage
- **Reasoning tokens** — the same loop; part of the output marked as a "draft"

[Gold callout]
**The pipeline is a diagnostic tree — the symptom almost always points to the culprit stage. Ask: "at which stage does this happen?"**

## Speaker notes

Let's put the diagram together. The inference pipeline — four stages, closed into a loop: tokenization turns text into IDs from a fixed vocabulary; embeddings turn IDs into learned vectors; attention enriches vectors with context through three projections and produces a probability distribution over the next token; sampling picks one token and appends it to the context. This is the same "model" black box from Lecture 1 — now transparent.

It's worth pinning down: this lecture's new topics didn't add stages — they slotted into the existing ones. Glitch tokens are a vocabulary property at the tokenization stage. KV-cache lives inside the attention stage, and prompt caching is a commercial add-on on top of it at the request boundary. Structured outputs are a filter at the sampling stage: zeroing out the probabilities of invalid tokens. Reasoning tokens aren't a new stage — they're the same autoregressive loop, with part of the output marked as a "draft." If every new term has found its place in the diagram for you, the picture is assembled.

And the most compact way to carry this diagram with you: the pipeline works as a diagnostic tree — the symptom almost always points to the culprit stage. The model "doesn't see" something obvious in the text — letters, digits, typos — that's tokenization. Search returns thematically-close junk — that's embeddings and the similarity boundary. The answer ignores an instruction from a long prompt, the chat slows down and gets pricier with every turn — that's attention, its window, and its cache. The same query gives different answers, the count doesn't match the visible volume, JSON breaks — that's sampling and its knobs. Getting into the habit of asking "at which pipeline stage does this happen?" turns the lecture from a reference sheet into a working debugging tool.
