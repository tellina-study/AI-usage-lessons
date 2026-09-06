---
id: s13
type: assertion_visual
section: "Section 2. Embeddings"
duration_min: 3
assertion: "Embeddings aren't just an inference internal: search and RAG run on a separate embedding model"
learning_goal: "Three lives of the embedding, from a search-practice angle (term-lock 'three lives'); which 'life' is the one at work in RAG; re-indexing isn't tied to the chat LLM"
learning_outcomes: [LO1, LO6]
chapter_ref: "§2.2 [for-slide-s13]"
visual_brief: "Thesis line under the title: 'when you build search or RAG, you're using the third life of the term — a separate embedding model'. 3 vertical cards: (1) The input lookup table — inside inference; static, the vector for [cat] is the same in every sentence; (2) The model's internal data representation — inside inference; vectors the model recomputes as it reads context, after the attention layers; (3) Vectors for search — a standalone tool (gold outline, marker 'this is your search/RAG'): a separate embedding model, not the internals of the chat LLM. Bottom gold callout: 'Updated the chat LLM → you do NOT need to re-index the database: the index lives in the embedding model's coordinate space'."
---

# Visible content

## Title bar
"Embeddings aren't just an inference internal — they're also a search tool"

## Body
[Thesis line under the title]
When you build search or RAG, you're using the third life of the term — a separate embedding model.

[3 vertical cards — the three lives of the term "embedding"]

**1. The input lookup table** *(inside inference)*
Static: the vector for `[cat]` is the same in every sentence. A lookup by ID, before any context exists.

**2. The model's internal data representation** *(inside inference)*
Vectors the model recomputes as it reads context: after the attention layers, each position's vector has been updated to reflect its surroundings. These are what carry the model's "understanding."

**3. Vectors for search** *(gold outline — "this is your search/RAG")*
A standalone tool: a vector for a whole text, from a **separate embedding model** — not the internals of your chat LLM. Its own product, its own training, its own leaderboards.

[Callout at the bottom, gold]
**Updated the chat LLM → you do NOT need to re-index the database: the index lives in the embedding model's coordinate space.**

## Speaker notes

Embeddings aren't just for inference — they're also a standalone search tool. In engineering usage, the word "embedding" refers to three different things; let's unpack the three lives of the term and see which one you're actually using when you build search.

Life one: the input lookup table — a static "token → vector" table at the LLM's input. The vector for the token "cat" is the same one, regardless of sentence. Life two: the model's internal data representation. The sequence of input vectors passes through dozens of attention layers, and at each layer, every position's vector is updated to reflect its surroundings — by the output, the vector at the position "cat" no longer equals the table entry, context has been mixed in; these are the vectors the model recomputes as it reads context. It's these representations that carry the model's "understanding" — the input table is just a starting point. Both of these lives are internal to inference. The third life is your working tool: when you call an embedding API for search or RAG, you get a vector for an entire text from a separate model, specifically trained for search and comparison. This isn't the internals of your chat LLM: the embedding model is a standalone product, and the chat model and the embedding model can come from different vendors entirely — that's normal practice.

The rule for keeping these apart: if it's about cost and context window — that's tokens and the input table; if it's about "what the model understood" — that's the internal data representation; if it's about search and vector databases — that's the output embeddings of a separate model.

And the typical mix-up mistakes this distinction exists to prevent. "We already pay for a chat-model subscription — why pay for an embedding model too?" — because the chat model doesn't give you search vectors. "Let's use an embedding model from the same vendor — they'll be more compatible" — there's no such thing as compatibility here as a category: vectors are only comparable against other vectors from the same embedding model; the LLM never even sees them. And, mirroring that: "we updated the LLM — we need to re-index the database" — no you don't; re-indexing is needed exactly when the embedding model itself changes.
