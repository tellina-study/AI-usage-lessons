---
id: s-rag-hybrid
type: process
section: "Section 2. RAG"
duration_min: 2.5
assertion: "Hybrid search = BM25 + dense vectors, fused by rank (RRF), plus a reranker; adopted for a measured gap, not by default"
learning_goal: "How hybrid retrieval works and why it became the production default (§2.6)"
learning_outcomes: [LO7]
chapter_ref: "§2.6 [for-slide-rag-hybrid-rrf]"
subtype: schema_pipeline
new_in_v4: "#196 WAVE 2 — RAG deepening"
---

# Visible content

## Title
"Hybrid search: two stages, fused by rank."

## Speaker notes

Earlier we established: strong RAG brings classical search back on top of the semantic layer. Here that conclusion unfolds into hybrid search, which has become the production default. Why combine the two: BM25 finds exact word matches — codes, identifiers, names, error numbers — but is powerless against a synonym: "broken login" won't match "authentication failure." Dense search does the opposite: it catches meaning but blurs on rare exact tokens. Hybrid search takes both sources of recall at once.

Let's clear up two questions first. The first is "hybrid of what with what," and here it's easy to get tangled in the word "vector." Sparse search is classical lexical search: BM25 or TF-IDF, plus the learned SPLADE and ELSER, on an inverted index; the unit is the word. When people say "sparse vector," they don't mean searching by the meaning of a vector — just a way of writing word-level search: a vector as long as the entire vocabulary, with almost all coordinates at zero. It's still lexical, not semantic. Dense search is the opposite: an embedding of 384–1024 floats, meaning encoded across all coordinates, approximate search (ANN), not interpretable, catches paraphrase. In one phrase: BM25 is sparse, embeddings are dense, SPLADE is sparse too — a neural network just assigns the term weights.

The second question: the word "hybrid" carries three different senses, and they get mixed up. Sense (a), the basic one, is a fusion of two distinct branches: sparse (lexical, BM25) and dense (semantic, embedding), merged by rank via RRF. Sense (b) is semantics plus a strict metadata filter (jurisdiction, date): an orthogonal lever, not a fusion of retrievers. Sense (c) is BM25 plus SPLADE or ELSER: both branches are sparse, both are lexical — one classical, one neural-weighted; there are no semantic dense vectors here. What follows is the mechanics of sense (a).

Now the mechanics, step by step. Both retrievers run in parallel: BM25 returns its top-N from the inverted index, dense search returns its own from ANN. Then they need to be merged, and here's the trap: BM25 scores are unbounded and corpus-dependent, while cosine similarity lies in the zero-to-one range — the scales aren't comparable. Reciprocal Rank Fusion sidesteps this by merging on rank rather than score: a document's weight is the sum, across retrievers, of one divided by "k plus rank." Only the order matters, so scale incomparability stops being a problem. The default k is around sixty — that's a convention, and it's worth tuning.

The reranker is the second stage, and the distinction between the two encoder types carries the weight here. A bi-encoder encodes the query and the document separately and in advance: at query time it's a fast comparison of ready-made vectors — cheap but coarse. A cross-encoder runs the "query plus document" pair together, in a single transformer pass: more accurate, but it can't be precomputed. Hence the rule: it's expensive, so it's applied only to reranking the top fifty-to-one-hundred candidates the hybrid stage selected.

We read the gains against a baseline, and skeptically. On WANDS, hybrid search gives NDCG 0.7497 against 0.6983 for BM25 — about a seven-percent gain over a tuned baseline. The large gains show up where lexical or semantic matching breaks down on its own: at Anthropic, the miss rate dropped from 5.7 to 1.9 percent. The payoff depends on the corpus: measure the gap on your own queries first, then add complexity.

Sources:
[1] denser.ai — Hybrid Search for RAG (WANDS / financial-table deltas) — WANDS NDCG 0.7497 hybrid vs 0.6983 BM25 / 0.6953 vector; financial text Recall@5 0.816 vs 0.587. https://denser.ai/blog/hybrid-search-for-rag/ [VFY-day-of]
[2] Anthropic — Contextual Retrieval (miss-rate cascade 5.7→1.9%) — context+BM25 → 2.9%; +reranking → 1.9% from a 5.7% baseline. https://www.anthropic.com/engineering/contextual-retrieval
