---
id: s-rag-elastic
type: assertion_visual
section: "Section 2. RAG"
duration_min: 2.5
assertion: "Three tiers: plain BM25 is enough / the built-in Elastic-OpenSearch hybrid is enough / a dedicated vector database is needed only at 100M+, multi-vector, or a latency SLA"
learning_goal: "The decision boundary for «do you need a dedicated vector database» + Elastic vs OpenSearch (§2.8)"
learning_outcomes: [LO7, LO4]
chapter_ref: "§2.8 [for-slide-rag-need-vectordb]"
subtype: meme_forward
new_in_v4: "#196 WAVE 2 — RAG deepening (anti-hype)"
---

# Visible content

## Title
"What to choose for your situation: three tiers."

## Speaker notes

This is a choice made in the open — for your scale and your requirements, not an assumption that you already have something in place. Three tiers, from the bottom up; you move up to the next one only when the previous one isn't enough for the actual workload.

The first tier: plain BM25 is enough. This is the case when queries and documents share a vocabulary — internal tools, search over logs, code, identifiers, curated knowledge bases. Here you need neither embeddings nor a vector store at all, and reindexing is cheap and observable — a real operational advantage, not a compromise. Before you build vector infrastructure, honestly check whether this is your case.

The second tier: a search engine that also does vectors is enough. This is when you need meaning on top of lexical matching at a scale of millions or tens of millions of vectors, but standing up a separate specialized store is still premature. Elasticsearch and OpenSearch are among the options for such an engine: both natively support an RRF hybrid and a linear combination of keyword and vector. Elasticsearch carries the dense_vector field type and kNN over HNSW, and ELSER — a sparse neural model that runs inside the cluster with no external GPU inference — is claimed to beat BM25 recall by ten to twenty percent on domain content. OpenSearch offers k-NN via FAISS and Lucene and allows a higher vector dimensionality. The point of this tier is to get semantics without standing up a separate GPU embedding service and a second store.

The third tier: you need a dedicated vector database. That's at a hundred million vectors or more, when you need multi-vector or late-interaction primitives, under a hard latency SLA on the product's hot path, or when you want to decouple the vector store from operating a logging cluster.

The anti-hype takeaway: a huge share of RAG systems never exceed a few million chunks. At that scale, pgvector or the Elastic/OpenSearch hybrid is the boring right answer, and a dedicated vector database is often a premature optimization.

Sources:
[1] Pureinsights — From Vector Hype to Hybrid Reality (do you need a vector database) — most systems ≤ a few million chunks → pgvector / the built-in hybrid is the right answer. https://pureinsights.com/blog/2026/from-vector-hype-to-hybrid-reality-is-elasticsearch-still-the-right-bet/
[2] bigdataboutique — Elastic/OpenSearch vector search (native RRF hybrid) — ELSER (no GPU), BBQ ~16× memory; OpenSearch k-NN via FAISS/Lucene. https://bigdataboutique.com/blog/opensearch-and-elasticsearch-vector-search-an-introduction-6af584 [VFY-day-of]
