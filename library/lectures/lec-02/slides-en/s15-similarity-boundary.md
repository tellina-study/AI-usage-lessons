---
id: s15
type: case_study
section: "Section 2. Embeddings"
duration_min: 3
assertion: "High similarity means 'about the same thing' — not 'with the same meaning': similarity ≠ relevance"
learning_goal: "Similarity heatmap (KEEP core) + failure boundary: 'configure SSL' ↔ 'disable SSL' — close vectors, opposite meaning; bridge to Lecture 3"
learning_outcomes: [LO1, LO6]
chapter_ref: "§2.4 [for-slide-s15] (heatmap — §2.3)"
visual_brief: "Left — 5×5 cosine similarity heatmap (SSL/HTTPS ~0.85, React pair ~0.78, borscht 0.05–0.15), Ocean scale. Right — failure card: 'How to configure SSL' ↔ 'How to disable SSL' — very high similarity (gold outline), opposite practical meaning. Callout: similarity is a candidate-generation signal; relevance is a separate task (reranker, hybrid search, filters)."
---

# Visible content

## Title bar
'High similarity means "about the same thing," not "with the same meaning"'

## Body
[Left — 5×5 cosine similarity heatmap, Ocean scale]

| | SSL | HTTPS | React comp. | React app | Borscht |
|---|---|---|---|---|---|
| How to configure SSL | 1.00 | **0.85** | 0.18 | 0.20 | 0.08 |
| Installing an HTTPS certificate | 0.85 | 1.00 | 0.22 | 0.19 | 0.07 |
| Deploying a React component | 0.18 | 0.22 | 1.00 | **0.78** | 0.12 |
| Building a React app | 0.20 | 0.19 | 0.78 | 1.00 | 0.10 |
| Borscht recipe | 0.08 | 0.07 | 0.12 | 0.10 | 1.00 |

[Right — failure card, gold outline]
"How to **configure** SSL" ↔ "How to **disable** SSL"
Very high similarity — opposite practical meaning.

[Callout at the bottom]
**Similarity is a candidate-generation signal; relevance is a separate task: reranker, hybrid search, filters.**

## Speaker notes

First — where similarity works well. Five short texts, a pairwise cosine similarity table on a modern embedding model: task-synonymous pairs — "configure SSL" and "installing an HTTPS certificate" — score around 0.85; topically related React texts — around 0.78; borscht against anything technical — 0.05 to 0.15. A query for "strawberries" finds documents about strawberry and wild strawberry without a synonym table — that's what embeddings add on top of full-text search.

Now — the boundary, and this is new material even for people already building semantic search. High cosine similarity means "about the same thing," not "about the same thing with the same meaning." The pair "how to configure SSL" and "how to disable SSL" gets a very high similarity score: same topic, same vocabulary, same syntactic frame — but the opposite practical meaning. An embedding averages the contextual statistics of an entire text; a short negation or an antonymic verb shifts the vector only weakly. In production this looks painful: a user asks how to enable certificate verification, search confidently surfaces an article on how to disable it, an LLM in a RAG pipeline dutifully summarizes it — and a system with great similarity metrics delivers harmful advice.

The engineering answers are well known: a reranker — a second model that scores the full query-document pair; hybrid search combined with full-text search for exact terms; filters and metadata for directional attributes. And a diagnostic trick: assemble a test set of "query → correct document" pairs with deliberate traps — on/off, before/after, different versions — and see what ranks at the top. The full design of a RAG pipeline is Lecture 3; the principle to take from here is: cosine similarity is about topical closeness, relevance is a separate task.
