---
id: s-rag-design
type: process
section: "Section 2. RAG"
duration_min: 2.5
assertion: "POC→production is a different architecture: a dual pipeline (ingestion is the first bottleneck), freshness, a full re-embed on model change, eval across two metric groups; the counterfactual «<200k tokens — you don't need RAG»"
learning_goal: "How search system design changes at scale (§2.11)"
learning_outcomes: [LO7, LO4]
chapter_ref: "§2.11 [for-slide-rag-design-pipeline]"
subtype: checklist_schema
new_in_v4: "#196 WAVE 2 — RAG deepening"
---

# Visible content

## Title
«POC → production — this is a different architecture, not a tweak.»

## Speaker notes

So far, RAG has been discussed as logic. Here — what breaks when that logic becomes a production system. And right away let's clear up a skew that the course owner rightly flagged: production problems aren't only at indexing. There are three groups: building the index, the query, and operations. We'll go through all three, because "production" breaks in any one of them.

The index side — building and maintaining it. In production, the ingest-chunk-embed-index pipeline becomes dual: an offline batch for bulk indexing and an incremental one for updates. The first bottleneck is usually ingestion, not search: at millions of documents, chunk and embed don't fit on a single machine; the intuition that search itself is slow is misleading — it's index preparation that's slow, not the query against it. Freshness has a real cost: batch reindexing is simple but goes stale, CDC sync is close to real time but triples operational complexity; one case — moving from batch to CDC improved the freshness SLA from twenty-four hours to sub-minute. A separate migration event: changing the embedding model requires re-embedding every vector — old and new ones aren't comparable; that's an index migration, not a line in a config. And evaluating the build: without a labeled set, degradation is invisible — recall@k with a target around zero point eight, nDCG, plus an LLM judge like RAGAS.

The query side — what happens at the query itself. First: retrieval quality degrades at scale — as the corpus grows, recall falls and drifts, and "found something" stops meaning "found the right thing." Second: latency and throughput. Thousands of concurrent queries plus a cross-encoder reranker computed on every query hit a hardware wall; autoscaling lags behind a spike, and the latency tail grows exactly when load is at its peak.

Operations — what stays invisible until it breaks. Observability: retrieval fails silently, with no exception and no stack trace — the system answers confidently on irrelevant context, so you need quality metrics on live traffic and tracing on every request, or users will notice the failure before your monitoring does. Security and access: who's allowed to retrieve what; personal data sitting in chunks; the permissions filter has to sit before the vector search, or semantic similarity will pull in someone else's fragment — that's a data-architecture problem, not a model setting.

And the load-bearing counterfactual: for a knowledge base under two hundred thousand tokens, everything goes into the prompt with caching — up to a ninety percent cost cut — and retrieval is skipped altogether. The first question before any of this infrastructure is whether you need RAG at all.

Sources:
[1] Redis — RAG at Scale (ingestion bottleneck, CDC 24h→sub-minute, cache ~69%) — POC→production is a dual pipeline; freshness batch vs CDC; semantic cache ~69%. https://redis.io/blog/rag-at-scale/ [VFY-day-of]
[2] futureagi — RAG Evaluation Metrics (recall@k ~0.8, nDCG, RAGAS) — two metric groups: label-based + LLM judge; check them against a human. https://futureagi.com/blog/rag-evaluation-metrics-2025/ [VFY-day-of]
