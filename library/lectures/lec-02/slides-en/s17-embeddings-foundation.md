---
id: s17
type: assertion_visual
section: "Section 2. Embeddings"
duration_min: 1.5
assertion: "Embeddings are the foundation of understanding an LLM: the model works in a space of vectors, not strings"
learning_goal: "Section wrap-up: the round-trip path + what 'understanding' actually gives you; one pointer line on choosing embedding models (chapter-only)"
learning_outcomes: [LO1]
chapter_ref: "§2.5 [for-slide-s17] (+§2.6 chapter-only)"
visual_brief: "Left — a vertical two-way diagram (words → tokens → vectors → LLM gold center → vectors → tokens → words). Right — 2 cards: paraphrases and synonyms / cross-lingual proximity. Gold callout: 'sentence-level semantic proximity — the basis of understanding.' Caption line: choosing an embedding model (MTEB, Matryoshka representations) — self-study material."
---

# Visible content

## Title bar
"Embeddings are the foundation of understanding: the model works with vectors, not strings"

## Body
[Left — vertical two-way diagram, LLM in gold at the center]

words → tokens → vectors → **LLM** → vectors → tokens → words

[Right — 2 cards]

**Paraphrases and synonyms.** "How to set up SSL" and "Installing an HTTPS certificate" — close vectors → the model answers the same way; same with "car" and "automobile."

**Cross-lingual proximity.** "клубника" and `strawberry` — close vectors → the answer is correct regardless of the query language.

[Gold callout]
**Sentence-level semantic proximity is the basis of "understanding" rephrasings.**

[Action line]
**What to do:** one embedding model and one index serve search, clustering, and RAG all at once — but switching models means re-indexing the entire store; choose it as an infrastructure decision, not on the fly.

[Small caption line]
*Choosing an embedding model for the task (MTEB, Matryoshka representations) — self-study material.*

## Speaker notes

Let's tie the section together. The model doesn't work with words or with strings — it works with vectors; words only exist at the boundaries. On the input side, text passes through tokenization into identifiers, then through an input table into vectors; on the output side, an internal vector is turned back into text via a distribution and a token choice. Between human input and human output, the path is entirely vector-based.

This explains what we intuitively call "understanding." When you ask "how to set up SSL" and then "installing an HTTPS certificate," the model answers similarly because both queries land at nearby points in the space. Same with synonyms and cross-lingual proximity: "клубника" and strawberry are close vectors, and the answer is correct regardless of the query language.

The practical side: the same vectors underpin three standard applications — similarity search, unsupervised clustering, and semantic search with RAG. One embedding model and one index serve several product functions at once, which is why choosing an embedding model is an infrastructure decision, and switching is expensive: it means re-indexing the entire store. In production systems, semantic search almost never lives alone: the working standard is a hybrid of a full-text index for exact matches, a vector index for conceptual proximity, and a reranker on top — a direct consequence of the similarity boundary we just discussed. And remember: there's no inverse operation for an embedding — you can't recover text from a vector; it's a one-way compression of meaning. How to choose an embedding model for your language and dimensionality budget — I'll leave that to you for self-study: in the coursebook it's a chapter, part 1 — the section on 2026 embedding models.
