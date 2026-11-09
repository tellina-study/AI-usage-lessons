---
id: n34
type: mechanism_node_graph
duration_min: 0.75
assertion: "A chunk's boundary must coincide with a boundary of meaning inside the document, not with an arbitrary character count"
learning_goal: "Layer 1 of Case 2: architecture without a tool name. The n8n screen comes next slide. The rejection of a model is explicitly named (C5 by contraposition) — all four versions of this step are purely algorithmic, this is an architectural fact, not an implementation detail."
visual:
  pattern: content
  primary: >
    One formula tile with the architectural thesis, below it a short
    tile about the absence of a model at this step.
  backup: >
    Wording — SETKA-KEYSOV.md Case 2, "Solution", layer 1, verbatim.
---

# Where the chunk boundary should fall

## Assertion

Saving on the text-parsing step is paid for by a share of answers torn between two chunks.

## Visual

> A chunk's boundary must coincide with a boundary of meaning inside the document — character count has no bearing here. Cutting that slices the document "however it falls" saves one preparation step, and pays for it by having part of the answers to future questions end up torn between two chunks.

> **This decision doesn't need a model.** All four cutting versions — by character count, by sentence boundaries, by word boundaries, and by character count with overlap — are purely algorithmic: the boundary's position is computed by code, with no call to an LLM.

## Speaker notes

This is an architecture layer, framed so that it stays true regardless of which tool is used. It's worth saying right away about this architectural decision: it doesn't need a model at all. Cutting by character count, cutting by sentence boundaries, cutting by word boundaries, and cutting by character count with overlap — all of this is ordinary code that computes the chunk boundary directly from the text, with no call to an LLM and no embedding. This is part of the architectural decision itself; you can't call it an implementation detail: for this step, the right tool is an algorithm, and the model has nothing to do with it.

The idea is simple: the boundary along which a document is cut into store chunks must coincide with a boundary of meaning inside that document — character count has no bearing here. Cutting that slices the document "however it falls" — by a fixed number of characters, without looking at the text — saves one step of data preparation. But we just saw by the numbers what that saving costs: part of the answers to future client questions ends up torn between two neighboring chunks, and search will later find only half of the needed fact.

This architectural observation isn't tied to a specific text-cutting tool and isn't tied to a specific language — it stays true for any document cut into pieces before being placed into a store. How this gets configured on a real screen — next beat.

A "boundary of meaning" is a quite concrete, measurable thing; it's hard to call it an abstract philosophical term: it's the boundary between sentences, between list items, between paragraphs. A document almost always already contains this markup — punctuation marks, line breaks, numbered items — and the task of cutting by meaning comes down to respecting the structure the document already has: no arbitrary character counting layered on top, no understanding of the text invented on the fly.

This is why the decision is called architectural: it's more than just "a more careful setting". It sets a rule applicable to any training-center document in advance, before anyone knows which specific question will be asked about it. The rule is simple and verifiable: the cut never falls inside a sentence. Everything else — the specific chunk size, the specific sentence-splitting tool — is already an implementation detail of this one principle; none of those are independent decisions in their own right.
