---
id: s-classic-rag
type: assertion_visual
section: "Section 2. RAG"
duration_min: 2
assertion: "The R in RAG is retrieval, a discipline with half a century of history: the inverted index, boolean search, TF-IDF, BM25; RAG adds a semantic layer on top, the classics do not disappear"
learning_goal: "Classical baseline §2.0: classical information retrieval as the foundation of RAG"
learning_outcomes: [LO7]
chapter_ref: "§2.0 [for-slide-s-classic-rag]"
visual_brief: "Three classical-search cards (inverted index/catalog; boolean search; TF-IDF→BM25) + gold callout \"the BM25+vectors hybrid — a return of the classics\" + a bridge to the semantic layer."
interaction: none
new_in_v5b: "#185 WP8 — classical baseline of Section 2"
---

# Visible content

## Title bar
"How text was searched before embeddings"

## Body
[Three classical-search cards, Ocean rounded box]

**Inverted index** — for each word, a list of documents where it occurs (the machine analogue of a library catalog). The foundation of Lucene, Elasticsearch, PostgreSQL full-text.

**Boolean search** — a query as a logical expression ("error AND authentication NOT tomcat"): precise, predictable, explainable selection.

**TF-IDF → BM25** — ranking by word importance (rarer in the collection = stronger signal). BM25 (the Okapi family) — a cheap, explainable baseline that many do not beat.

[Gold callout — what to keep from the classics]
**What to keep: the classics work on lexical match — precise on codes and identifiers, where meaning-based search blurs. The best RAG-2026 is a hybrid of BM25 + dense vectors, lexical filters over metadata, ranking discipline (a reranker), and observability: recall/precision on a reference set (golden set).**

[Bridge, bottom]
Semantic search on embeddings (Lecture 2) adds meaning-based match on top of the classics instead of lexical match — but does not replace it. RAG is an extension of classical search with a semantic layer, not a rejection of it.

## Speaker notes

RAG is usually presented as a new technology grown out of embeddings. This hides something essential: the R in RAG is retrieval, search — a discipline with half a century of history, and it is exactly its design that determines where RAG works and where it breaks. Let us reconstruct classical information retrieval from scratch, how text was searched before embeddings, because without this baseline semantic search looks like magic, and it is not magic but the next layer on top of an understood foundation.

The everyday ancestor of machine search is the library catalog: cards ordered by author, title, and subject heading, plus "see also" references. Exactly this idea a machine reproduces through an inverted index — a structure that, for each word, stores a list of documents where it occurs. Instead of scanning all texts, the system looks up the query words in the index and instantly obtains candidates. This is the foundation of any full-text system and to this day the workhorse of industrial operation.

On top of the index the classics solve two tasks — selection and ranking. Selection is set by boolean search: a query as a logical expression selects documents precisely and explainably. Ranking answers in what order to show what was selected. TF-IDF weights a word the more strongly the more frequent it is in this document and the rarer across the whole collection. The industry standard to this day is BM25 from the Okapi family: a development of TF-IDF with frequency saturation and length normalization. BM25 is not an obsolete artifact but a strong, cheap baseline.

The key property of these classics — they work on lexical match: they find documents with the same words as in the query. Hence the strength on codes and identifiers and the limit on synonyms. Semantic search on embeddings adds the missing layer of meaning, but the classics do not disappear: strong RAG systems of 2026 are a hybrid of BM25 and vectors, not dense-only. RAG is an extension of classical search, and its failures are largely where the classical foundation was forgotten.
