---
id: s08a
type: section_divider
section: "Раздел 2. Эмбеддинги"
duration_min: 0.5
assertion: "Section 2 — Embeddings: the space of meanings"
learning_goal: "Section divider раздела 2 — переход к векторам"
learning_outcomes: [LO1]
chapter_ref: "§2 [for-slide-s08a]"
visual_brief: "Большое «Раздел 2» по центру (140pt gold). Под ним — «Эмбеддинги». Под этим — frame-фраза «Пространство смыслов». Внизу — roadmap-bar (6 секций) с gold-маркером на «2 Эмбеддинги»."
---

# Visible content

## Title bar
(нет — section divider слайд)

## Body
[Большое «Section 2» по центру верхней половины — 140pt gold]

[Под ним — sub-title]
**Embeddings**

[Caption мелким — frame phrase]
"The space of meanings"

[Roadmap-bar внизу — 6 карточек, gold-маркер на «2 Embeddings»]
- 0. Introduction
- 1. Tokens
- 2. Embeddings ← **You are here** (gold)
- 3. Attention
- 4. Sampling
- 5. Wrap-up

## Speaker notes

We have passed the first stage — tokenization. Text turns into a sequence of ids from the model's vocabulary. Next comes the second stage, embeddings. This is the step where each vocabulary id is replaced by a vector in a high-dimensional space: for small embedding models this is 384 or 1536 dimensions, for the inner layers of large LLMs — thousands. And the key property of this space, learned during training: geometric closeness of vectors reflects semantic closeness of tokens and fragments.

Embeddings are not an interesting layer in themselves; the model uses them internally as an intermediate step toward attention and sampling. Why talk about them separately? Because a whole applied field rests on them: similarity, clustering, and semantic search. And semantic search is the base layer of RAG, Retrieval-Augmented Generation, which we will return to in Lecture 3.

This section has four slides plus this divider. First we pin down what an embedding is through the "token → vector" schematic. Then we take apart sentence similarity — closeness at the level of sentences on modern 2026 embeddings, not just at the level of words. Then three practical applications: similarity, clustering, search — a map for later lectures. And we close the section by comparing semantic search with full-text search on a simple query "strawberry" — what each one finds.
