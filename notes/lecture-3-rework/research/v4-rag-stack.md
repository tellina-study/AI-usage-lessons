# V4 — The 2026 RAG / Retrieval Stack (sourced research brief)

> Audience: 3rd-year CS students who already build RAG and run local fine-tuning.
> Tone: factual + skeptical. This lecture teaches **when NOT to reach for a component**.
> `[VFY-day-of]` = fast-moving version/number, re-verify before lecturing.
> Compiled 2026-09-13.

---

## 0. TL;DR decision spine (use this as the keystone axis)

1. **Start lexical (BM25). Prove it fails on your real queries. Then add vectors surgically.** Most "we need a vector DB" instincts are premature.
2. **Hybrid (BM25 + dense) + a reranker is the 2026 default**, not pure dense. The measured wins come from *combining* recall sources, not from a better single retriever.
3. **The database is rarely the bottleneck. Chunking and ingestion are.** Fixed-size recursive chunking is a shockingly strong baseline; fancy chunking often does not pay for itself.
4. **What breaks in production is not retrieval quality in the demo — it's freshness, re-indexing, latency at concurrency, and cost.**

---

## 1. Hybrid search: BM25 + dense, RRF, reranking

### 1.1 Why combine at all
- **BM25 (sparse/lexical)** matches exact terms — product codes, error strings, names, acronyms, identifiers. It cannot bridge paraphrase ("car" vs "automobile") or synonyms.
- **Dense vector search** matches semantic meaning but blurs on rare exact tokens (a SKU, a function name) and drifts when two teams name the same thing differently.
- The failure point that forces you off pure-BM25: **acronym/synonym drift** — the moment two teams call the same thing by different names, lexical overlap collapses. ([Maven / BM25+friends](https://maven.com/p/62d95c/could-your-search-be-better-without-vectors-bm25-friends), [InfoQ](https://www.infoq.com/articles/vector-search-hybrid-retrieval-rag/))
- Skeptic's note: hybrid is **not free** — you now run two indexes, two query paths, and a fusion step. Only adopt when a *measured* gap exists. ([DEV — you probably don't need a vector DB](https://dev.to/arthurpro/you-probably-dont-need-a-vector-database-for-rag-3op))

### 1.2 Reciprocal Rank Fusion (RRF)
- **Formula:** `score(d) = Σ_over_retrievers 1 / (k + rank_i(d))`. Each retriever contributes based on the **rank** it gives a doc, not its raw score. ([dev.to RRF](https://dev.to/srijan_bhai/stop-choosing-between-bm25-and-vector-search-implement-hybrid-search-with-rrf-2c89), [Weaviate](https://weaviate.io/blog/hybrid-search-explained))
- **Why it works:** BM25 scores (unbounded, corpus-dependent) and cosine similarity (0–1) live on **incompatible scales**. Normalizing raw scores is fragile. RRF sidesteps this by fusing on ranks — robust and parameter-light.
- **`k` parameter:** smoothing constant, **default 60** in most implementations (Elastic/OpenSearch default). Larger `k` flattens the contribution of top ranks (democratizes across retrievers); smaller `k` (some use ~10) sharpens emphasis on each retriever's top hits. `k=60` is a convention, not a law — tune it. `[VFY-day-of]` ([dev.to RRF](https://dev.to/srijan_bhai/stop-choosing-between-bm25-and-vector-search-implement-hybrid-search-with-rrf-2c89))
- Alternative to RRF: **weighted linear combination** of normalized scores (gives finer control but requires you to normalize and pick weights — more tuning, more brittleness). Both Elastic and OpenSearch support RRF *and* weighted linear. ([bigdataboutique](https://bigdataboutique.com/blog/opensearch-vs-elasticsearch-compared))

### 1.3 Reranking (second stage, cross-encoder / late interaction)
- **Bi-encoder** (used for first-stage retrieval) embeds query and doc *separately* → fast, precomputable, but lossy. **Cross-encoder** feeds `[query, doc]` jointly through a transformer → far more accurate relevance score, but you must run it at query time on every candidate → expensive, so it only reranks the top-N (e.g. top 50–100). ([Towards Data Science — cross-encoders](https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/))
- **The 2026 default is a cross-encoder reranker** on top of hybrid retrieval. ([localaimaster](https://localaimaster.com/blog/reranking-cross-encoders-guide), [Thread Transfer](https://thread-transfer.com/blog/2026-06-17-rag-reranking-llm-colbert/))
- **Models:**
  - **Cohere Rerank** (managed API, broad language coverage; "Rerank 4" cited) — pick when you want no GPU ops. `[VFY-day-of]` on version.
  - **BGE-reranker-v2-m3** — open (Apache-2.0), multilingual, ~568M params, ~80 ms per batch of 50 query-doc pairs on a single A10G GPU. Pick for self-hosting / open license. `[VFY-day-of]`
  - **ColBERT / ColBERTv2 (late interaction)** — keeps one vector *per token*; scores via MaxSim (sum of per-query-token max similarity across doc tokens). Good under tight latency budgets self-hosted, but **niche in 2026**: multiple sources call the bi-encoder + cross-encoder pipeline simpler and usually equivalent in quality, and ColBERT's per-token vectors blow up the index size. ([futureagi rerankers](https://futureagi.com/blog/best-rerankers-for-rag-2026/), [Thread Transfer](https://thread-transfer.com/blog/2026-06-17-rag-reranking-llm-colbert/))
- Benchmark starting points: **BEIR, MTEB, MIRACL** — but the consistent caveat is *your* corpus has its own term distribution; leaderboard rank does not transfer. Evaluate on your data. ([futureagi](https://futureagi.com/blog/best-rerankers-for-rag-2026/))

### 1.4 When hybrid beats pure dense / pure lexical — measured deltas (with baselines)
| Setting | Metric | Hybrid / reranked | Baseline(s) | Source |
|---|---|---|---|---|
| WANDS e-commerce | NDCG | **0.7497** (tuned hybrid) | BM25 **0.6983** / pure vector **0.6953** → ~7.4% lift over *either* | [denser.ai hybrid guide](https://denser.ai/blog/hybrid-search-for-rag/) |
| Financial text+tables | Recall@5 | **0.816** (hybrid + neural rerank) | dense-only **0.587** | [denser.ai](https://denser.ai/blog/hybrid-search-for-rag/) / [arXiv 2604.01733](https://arxiv.org/pdf/2604.01733) |
| Anthropic internal RAG (top-20 retrieval **failure** rate, lower is better) | failure % | contextual-embeddings+BM25 **2.9%**; +reranking **1.9%** | baseline **5.7%** (−49% then −67%) | [Anthropic Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval) |

- **Read the deltas skeptically:** WANDS lift is ~7.4% NDCG — real but modest, and it's over an *already tuned* baseline. The Anthropic and financial-table numbers are larger because those corpora are exactly where lexical *or* dense alone breaks (jargon + tables + cross-references). **Hybrid's payoff is corpus-dependent**; on clean prose with well-phrased queries the gap can be small.

---

## 2. Vector databases & orchestration stack

### 2.1 Per-engine cheat sheet (2026)
| Engine | Sweet spot | Pick when | Rough scale ceiling |
|---|---|---|---|
| **pgvector (Postgres)** | RAG bolted onto data you already have in Postgres; IVFFlat + HNSW indexes | You already run Postgres; want one system, transactional consistency, no new ops | **~50M vectors comfortably**; degrades beyond ~50–100M unless using pgvectorscale. `[VFY-day-of]` |
| **Qdrant** | Dedicated engine, minimal ops, native sparse + multi-vector | Want a purpose-built engine but not a big platform; budget-conscious (strong free tier) | Cited **~10–25% faster** than Weaviate/Milvus on common workloads; scales to large single-node + clustered |
| **Weaviate** | Built-in **hybrid** (vector + BM25 + metadata filters), modular embeddings | You want hybrid + filtering out of the box without wiring it yourself | Mid-to-large; hybrid is the differentiator |
| **Milvus** | Billions of vectors, separated compute/storage | **100M+ vectors**, heavy horizontal scale | Designed for **billions**; needs real ops investment |
| **FAISS** | Library, not a DB — in-process ANN | You want raw speed + full control, no persistence/CRUD/filtering layer needed (build it yourself) | Huge, but you own sharding/persistence/serving |
| **Chroma** | Prototyping / MVP; now object-storage backend + collection forking | Early dev, notebooks, small prod | Prototype → light prod |
| **LanceDB** | Embedded, local-first, columnar (Lance format); edge / data-science | No server wanted; local or edge; DS workflows | Local / embedded scale |

Sources: [firecrawl best vector DBs](https://www.firecrawl.dev/blog/best-vector-databases), [dreaming.press open-source comparison](https://dreaming.press/posts/best-open-source-vector-database-2026.html), [DataCamp top-5](https://www.datacamp.com/blog/the-top-5-vector-databases), [Medium top-15 production guide](https://medium.com/@pratik-rupareliya/top-15-vector-databases-in-2026-a-production-decision-guide-from-100-enterprise-deployments-dd58a04f51a5).

### 2.2 pgvector scale — the numbers, and where sources disagree
- pgvectorscale benchmark (**May 2025**): **471 QPS at 99% recall on 50M vectors — cited 11.4× Qdrant's 41 QPS** at the same recall. `[VFY-day-of]` ([firecrawl](https://www.firecrawl.dev/blog/best-vector-databases), [Tiger Data pgvector vs Qdrant](https://www.tigerdata.com/blog/pgvector-vs-qdrant))
- **Disagreement to flag in lecture:** this benchmark is published by TigerData/Timescale, the vendor of pgvectorscale — treat as vendor-favorable. Independent comparisons (e.g. Qdrant's own benchmarks) put Qdrant on top. **Both are true and both are marketing** — the lesson is *benchmark on your own data and query mix*.
- **Physical constraints that actually bite:** HNSW index must stay **in RAM** to be fast; index overhead ≈ **2–3× the base vector size**; billion-vector HNSW build can need **>1.5 TB RAM**. Beyond ~50–100M vectors, general-purpose extensions hit throughput/latency walls that purpose-built systems avoid. ([Instaclustr pgvector perf](https://www.instaclustr.com/education/vector-database/pgvector-performance-benchmark-results-and-5-ways-to-boost-performance/), [firecrawl](https://www.firecrawl.dev/blog/best-vector-databases), [arXiv d-HNSW 2603.13591](https://arxiv.org/pdf/2603.13591))

### 2.3 Managed vs self-hosted
- Managed (Pinecone, Qdrant Cloud, Weaviate Cloud, managed Elastic/OpenSearch): you pay to not run HNSW-in-RAM ops, sharding, backups, and re-index jobs. Self-hosted (FAISS/Milvus/pgvector on your infra): cheaper per vector at scale, but you own the operational failure modes (memory eviction, index rebuilds, freshness lag).

### 2.4 LlamaIndex vs LangChain — 2026 positioning
- **They are complementary, not competitors** — the 2026 consensus. ([nutrient.io](https://www.nutrient.io/blog/llamaindex-vs-langchain-rag/), [Applied AI Studio](https://studio.appliedai.club/blog/comparison/langchain-vs-llamaindex-enterprise-rag))
- **LlamaIndex** — strongest starting point when the hard problem is **retrieval over messy private documents** (ingestion, indexing, retrieval with sensible defaults).
- **LangChain / LangGraph** — LangChain is the broad integration + agent framework; **LangGraph** is the low-level stateful runtime that has become *the* way to build agents in 2026: durable execution, checkpointing, human-in-the-loop pause/resume across hours/days.
- **Common production shape:** *LlamaIndex for ingestion + retrieval, LangGraph for orchestration, LangSmith/Langfuse for observability.* ([rahulkolekar production RAG 2026](https://rahulkolekar.com/production-rag-in-2026-langchain-vs-llamaindex/))
- Skeptic's note: for a simple RAG endpoint, **neither framework is required** — a few hundred lines of your own glue avoids version churn and abstraction leaks. Frameworks earn their keep at agentic/multi-step complexity.

---

## 3. Elastic vs OpenSearch vs "do I even need a dedicated vector DB?"

### 3.1 What each brings (2026)
- **Both** support **RRF hybrid** and **weighted linear combination** of keyword + vector scores natively. ([bigdataboutique compared](https://bigdataboutique.com/blog/opensearch-vs-elasticsearch-compared))
- **Elasticsearch:**
  - `dense_vector` field type + HNSW kNN.
  - **ELSER** (Elastic Learned Sparse EncodeR) — sparse *neural* model, ships in-cluster, **no external GPU inference needed**; sits between BM25 and dense; **cited to beat BM25 recall by 10–20%** on benchmark/domain content. `[VFY-day-of]`
  - **ESRE** bundles ELSER + multilingual E5 dense + **BBQ (Better Binary Quantization)**: 32-bit floats → ~2 bits, **~16× memory reduction, claimed <1% recall loss**. `[VFY-day-of]` ([Pureinsights](https://pureinsights.com/blog/2026/from-vector-hype-to-hybrid-reality-is-elasticsearch-still-the-right-bet/), [bigdataboutique intro](https://bigdataboutique.com/blog/opensearch-and-elasticsearch-vector-search-an-introduction-6af584))
- **OpenSearch:**
  - k-NN via **FAISS, Lucene, and Nmslib** engines; **neural search** plugin wires embedding models.
  - **3.0: concurrent segment search for k-NN on by default → up to 2.5× faster vector queries**. Max vector dims **16,000 via FAISS** vs Elasticsearch's **4,096**. `[VFY-day-of]` ([bigdataboutique compared](https://bigdataboutique.com/blog/opensearch-vs-elasticsearch-compared))
  - License/cost angle: OpenSearch is Apache-2.0 (AWS fork after Elastic's license change); Elastic later re-added AGPL. Flag the licensing lineage but don't overweight it. `[VFY-day-of]`

### 3.2 The decision boundary (be concrete)
1. **Classic lexical (BM25) alone is enough** when queries and documents share vocabulary: internal tools, log/code/ID search, well-curated KBs, early prototypes. No embeddings, no vector store, **re-indexing is cheap and observable** — a real operational advantage. ([Medium — ditch vector DB for BM25](https://medium.com/@ThinkingLoop/when-to-ditch-your-vector-db-for-simple-bm25-b4f044f1076b), [SQLServerCentral](https://www.sqlservercentral.com/articles/you-probably-dont-need-a-vector-database))
2. **Elastic/OpenSearch built-in semantic/hybrid is enough** when you already run one of them for logs/search and your scale is in the *millions-to-tens-of-millions* of vectors. ELSER especially lets you get semantic lift **without standing up a GPU embedding service or a second datastore**. This is the "you already have the hammer" case.
3. **You actually need a dedicated vector DB / specialized approach** when: (a) **100M+ vectors** or billions (→ Milvus); (b) you need native **multi-vector / late-interaction / sparse** primitives or aggressive quantization tuning (→ Qdrant/Milvus); (c) vector search latency/QPS at high concurrency is your product's hot path and a general-purpose engine can't hit the SLA; (d) you want the vector store decoupled from your logging/search cluster's ops.
- **Anti-hype:** a huge share of RAG systems never exceed a few million chunks. At that scale **pgvector or Elastic/OpenSearch hybrid is the boring correct answer**; a dedicated vector DB is often premature optimization. ([Pureinsights — hybrid reality](https://pureinsights.com/blog/2026/from-vector-hype-to-hybrid-reality-is-elasticsearch-still-the-right-bet/))

---

## 4. Chunking — the highest-leverage / most-underrated knob

### 4.1 Strategies
- **Fixed-size (token/char)** — split every N tokens. Dumb, fast, reproducible. Surprisingly strong baseline.
- **Recursive / character** — split on a hierarchy of separators (¶ → sentence → word) to respect structure while capping size. The pragmatic default.
- **Sentence-window** — embed a single sentence for precision, but return a window of neighboring sentences to the LLM for context.
- **Semantic chunking** — place boundaries where embedding similarity between adjacent sentences drops. Intuitive, but *frequently* not worth the cost (see 4.3).
- **Parent-document / small-to-big** — **index small chunks for retrieval precision, return the larger parent block for generation.** Widely recommended fix for "lost context." ([atlan](https://atlan.com/know/chunking-strategies-rag/))
- **Late chunking** (Günther et al., 2024) — embed the *whole document* at token level first, *then* pool into chunk embeddings, so each chunk embedding is context-aware (preserves pronouns/references/theme). ([firecrawl chunking](https://www.firecrawl.dev/blog/best-chunking-strategies-rag))
- **Contextual Retrieval** (Anthropic, 2024) — use an LLM to prepend 50–100 tokens of document-level context to each chunk *before* embedding + BM25 indexing. (See §1.4 numbers.)

### 4.2 Trade-offs
- **Chunk size:** too small → *contextual fragmentation* (retrieve step 6 without steps 1–5; model invents the gap). Too large → *semantic dilution* (one vector tries to represent several topics, represents none cleanly). ([Medium — RAG chunking 9 strategies](https://medium.com/@ThinkingLoop/rag-chunking-9-strategies-that-stop-lost-context-b4777df4c908))
- **Overlap:** modest overlap reduces boundary loss but inflates index size and duplicates hits.
- **Metadata attachment:** attach source, section, timestamps → enables filtering and freshness, and lets small chunks carry provenance.

### 4.3 Measured impact — and where studies openly disagree
| Study | Finding | Baseline / counterfactual |
|---|---|---|
| MDPI Bioengineering, Nov 2025 (clinical) | Adaptive/topic-boundary chunking **87% accuracy** | vs **13%** fixed-size baseline (p=0.001) — huge gap, but narrow clinical domain |
| Feb 2026 benchmark, 7 strategies over 50 academic papers | **Recursive 512-token split ranked #1 at 69%** | **Semantic chunking 54%** (produced tiny ~43-token fragments) |
| NAACL 2025 Findings | **"Computational costs aren't justified by consistent gains"** — fixed 200-word chunks match/beat semantic chunking | across retrieval + answer-gen tasks |

Sources: [firecrawl chunking](https://www.firecrawl.dev/blog/best-chunking-strategies-rag), [arXiv systematic investigation 2603.06976](https://arxiv.org/html/2603.06976), [arXiv cost/limits eval 2606.00881](https://arxiv.org/html/2606.00881v1).
- **The honest read for students:** the "fancy chunking wins" claims are **domain-specific and not consistent**. On many corpora, plain recursive fixed-size chunking is the strong baseline and semantic chunking loses on both quality *and* cost. **Don't cargo-cult semantic chunking.**

### 4.4 Common chunking FAILURES → the lesson
- **Tables** are "the single most common cause of *silent* retrieval failures" — flattening a table to text destroys row/column relationships; the LLM can't reconstruct them. **Lesson: handle tables as structured objects, don't string-flatten.** ([Towards Data Science — your chunks failed](https://towardsdatascience.com/your-chunks-failed-your-rag-in-production/))
- **Anaphora / broken references** — "it", "the city", "this" lose their antecedent when split → the chunk embeds ambiguously. **Lesson: use parent-document, late chunking, or contextual prepending.**
- **Stale 200-char defaults** leave the embedder almost nothing to represent. **Lesson: the copy-pasted tutorial default is usually wrong for your data.**
- **Meta-lesson (best teams):** teams that went from 3–4 months per RAG use case to reliable deployment **"stopped tuning chunk size and started governing the knowledge layer"** — i.e. document quality, table handling, freshness, and metadata matter more than the perfect chunk size. ([atlan](https://atlan.com/know/chunking-strategies-rag/), [Towards Data Science](https://towardsdatascience.com/your-chunks-failed-your-rag-in-production/))

---

## 5. How system design changes — indexing, freshness, eval, cost at scale

### 5.1 Indexing pipeline
`ingest → chunk → embed → index`. In production this is **dual pipelines**: one offline/batch for bulk indexing, one incremental for updates. The **first bottleneck is usually ingestion**, not search: at millions of docs, chunk+embed can't run on one machine. ([Redis — RAG at scale](https://redis.io/blog/rag-at-scale/), [Introl](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide))

### 5.2 Freshness / re-indexing (a real cost, not a footnote)
- **Batch re-index** = simple but stale; **CDC (change-data-capture) sync** = near-real-time but "triples operational complexity." One cited case: moving off batch to CDC improved freshness SLA **from 24 h to sub-minute** — at real ops cost. `[VFY-day-of]` ([Redis](https://redis.io/blog/rag-at-scale/))
- **Vector-store-specific failure mode:** every document edit forces **re-chunk + re-embed**. If that job silently lags, retrieval degrades **invisibly** — no error, just worse answers. Keyword indices don't have this failure mode (reindex is cheap + observable). This is a genuine argument *against* jumping to vectors. ([Maven](https://maven.com/p/62d95c/could-your-search-be-better-without-vectors-bm25-friends))
- **Embedding drift:** if you change the embedding model, **every vector must be re-embedded** — old and new vectors are not comparable. Model upgrades are migration events.

### 5.3 Retrieval eval metrics
- **Retrieval-side (need labels):** Recall@k (target ~**0.8+ at k=20** for broad datasets), Precision@k (**0.7+** narrow / **0.5+** broad domains), MRR (1/rank of first relevant), nDCG (relevance-weighted ranking, target **0.8+ at k=10**). ([futureagi metrics](https://futureagi.com/blog/rag-evaluation-metrics-2025/), [Label Your Data](https://labelyourdata.com/articles/llm-fine-tuning/rag-evaluation))
- **End-to-end (LLM-as-judge, no labels needed) — RAGAS:** *Faithfulness* (are answer claims grounded in retrieved context), *Context Precision* (share of retrieved chunks that are relevant), *Context Recall* (share of needed info actually retrieved). ([futureagi](https://futureagi.com/blog/rag-evaluation-metrics-2025/))
- **2026 practice:** compute **both** discrete label-based metrics and LLM-judge metrics and **reconcile** them; evaluate **continuously** (batch + online A/B), not once. Skeptic's note: LLM-judge metrics are cheap but noisy — they need spot-checking against human labels, or they quietly reward confident-wrong answers. ([futureagi](https://futureagi.com/blog/rag-evaluation-metrics-2025/), [arXiv applied RAG metrics 2607.07302](https://arxiv.org/pdf/2607.07302))

### 5.4 Latency & cost at scale — what breaks going prototype → production
- **The core lesson:** *"Prototypes work great with 1,000 documents and a few users; things break at millions of vectors and thousands of concurrent queries."* Response times spike, autoscalers kick in too late, LLM costs spiral because every request hits the API uncached. ([Redis](https://redis.io/blog/rag-at-scale/))
- **Cost drivers:** ingestion/embedding, vector search, **reranking** (cross-encoder at query time is a real per-query cost), and **LLM token usage** (dominant). Sub-50 ms retrieval SLAs push infra spend. ([Introl](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide))
- **Semantic caching** cited to cut LLM cost **up to ~68.8%** in typical production workloads. `[VFY-day-of]` ([Redis](https://redis.io/blog/rag-at-scale/))
- **Contextual-retrieval preprocessing cost:** ~**$1.02 per million document tokens** to generate contextual chunks *with prompt caching* (800-tok chunks, 8k-tok docs). One-time, but non-trivial at corpus scale. ([Anthropic](https://www.anthropic.com/engineering/contextual-retrieval))
- **The "maybe skip RAG" counterfactual:** for a knowledge base **under ~200k tokens**, Anthropic notes you can just put the whole thing in the prompt with caching (up to ~90% cost reduction) and **skip retrieval entirely**. Long-context + caching is a legitimate *alternative* to a RAG pipeline at small scale. ([Anthropic](https://www.anthropic.com/engineering/contextual-retrieval))
- **The architectural jump is not parameter tuning** — POC→prod means a *different architecture*: dual pipelines, hybrid retrieval, semantic caching, monitoring/governance. ([Redis](https://redis.io/blog/rag-at-scale/), [ragie.ai architect's guide](https://www.ragie.ai/blog/the-architects-guide-to-production-rag-navigating-challenges-and-building-scalable-ai))

---

## 6. "When NOT to" checklist (teach this explicitly)
- **Don't reach for a vector DB first** — start BM25, prove it fails on real queries, add vectors where a *measured* gap exists.
- **Don't default to a dedicated vector DB** at <~50M vectors — pgvector or Elastic/OpenSearch hybrid is the boring correct answer.
- **Don't cargo-cult semantic chunking** — recursive fixed-size is a strong, cheap baseline; multiple studies show semantic chunking loses on quality *and* cost.
- **Don't trust vendor benchmarks** (pgvectorscale vs Qdrant both claim wins) — benchmark on your data + query mix.
- **Don't trust leaderboard reranker rank** — MTEB/BEIR/MIRACL don't transfer to your corpus.
- **Don't assume RAG at all** for small KBs — long-context + prompt caching can beat a pipeline under ~200k tokens.
- **Don't treat LLM-judge eval as ground truth** — reconcile with labels or it rewards confident-wrong answers.

---

## Source index (primary/authoritative first)
- Anthropic — Contextual Retrieval (primary, exact failure-rate + cost numbers): https://www.anthropic.com/engineering/contextual-retrieval
- Weaviate — Hybrid Search Explained: https://weaviate.io/blog/hybrid-search-explained
- bigdataboutique — OpenSearch vs Elasticsearch (2026) / vector-search intro: https://bigdataboutique.com/blog/opensearch-vs-elasticsearch-compared | https://bigdataboutique.com/blog/opensearch-and-elasticsearch-vector-search-an-introduction-6af584
- Pureinsights — hybrid reality / is Elasticsearch still the right bet: https://pureinsights.com/blog/2026/from-vector-hype-to-hybrid-reality-is-elasticsearch-still-the-right-bet/
- firecrawl — best vector DBs / best chunking strategies: https://www.firecrawl.dev/blog/best-vector-databases | https://www.firecrawl.dev/blog/best-chunking-strategies-rag
- Instaclustr — pgvector performance benchmark: https://www.instaclustr.com/education/vector-database/pgvector-performance-benchmark-results-and-5-ways-to-boost-performance/
- Tiger Data — pgvector vs Qdrant: https://www.tigerdata.com/blog/pgvector-vs-qdrant
- Redis — RAG at scale: https://redis.io/blog/rag-at-scale/
- Towards Data Science — cross-encoders/reranking; "your chunks failed": https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/ | https://towardsdatascience.com/your-chunks-failed-your-rag-in-production/
- futureagi — rerankers 2026 / RAG eval metrics: https://futureagi.com/blog/best-rerankers-for-rag-2026/ | https://futureagi.com/blog/rag-evaluation-metrics-2025/
- rahulkolekar — production RAG 2026 LangChain vs LlamaIndex: https://rahulkolekar.com/production-rag-in-2026-langchain-vs-llamaindex/
- denser.ai — hybrid search for RAG (WANDS/finance deltas): https://denser.ai/blog/hybrid-search-for-rag/
- Maven — could your search be better without vectors: https://maven.com/p/62d95c/could-your-search-be-better-without-vectors-bm25-friends
- Medium — ditch vector DB for BM25 / RAG chunking 9 strategies: https://medium.com/@ThinkingLoop/when-to-ditch-your-vector-db-for-simple-bm25-b4f044f1076b | https://medium.com/@ThinkingLoop/rag-chunking-9-strategies-that-stop-lost-context-b4777df4c908
- atlan — chunking strategies: https://atlan.com/know/chunking-strategies-rag/
- arXiv — chunking systematic investigation (2603.06976), cost/limits eval (2606.00881), text+table retrieval benchmark (2604.01733), applied RAG metrics (2607.07302), d-HNSW (2603.13591)
- InfoQ — why vector search alone isn't enough: https://www.infoq.com/articles/vector-search-hybrid-retrieval-rag/

> Note on dates: many secondary sources carry 2026 datelines and forward-dated arXiv IDs; treat all specific QPS/version/percentage figures as `[VFY-day-of]`. Where vendor-authored (TigerData, Elastic, Redis), numbers are directionally useful but marketing-inflected — state the provenance in lecture.
