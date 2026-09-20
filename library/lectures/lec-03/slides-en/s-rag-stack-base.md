---
id: s-rag-stack
type: comparison
section: "Section 2. RAG"
duration_min: 2.5
assertion: "A vector engine is chosen for scale: pgvector up to ~50M, Milvus for 100M+; frameworks (LlamaIndex/LangGraph) are added for agentic complexity, not by default"
learning_goal: "The 2026 catalog of vector databases and frameworks + the rule «no framework is needed for simple RAG» (§2.7)"
learning_outcomes: [LO7]
chapter_ref: "§2.7 [for-slide-rag-vectordb]"
subtype: schema_matrix
new_in_v4: "#196 WAVE 2 — RAG deepening"
---

# Visible content

## Title
"Where vectors live: the engine is chosen for scale."

## Speaker notes

Once hybrid search is justified and the corpus has grown, the question becomes "where do you store and search the vectors." It's easy to overcomplicate here: the sub-catalog of engines is large, but the right choice for most systems is boring. Let's clear up right away a question the owner rightly raised: Elasticsearch and OpenSearch are also full-fledged vector stores, not something outside the landscape. Both hold dense vectors and search over them: Elastic via the dense_vector field type and kNN over HNSW; OpenSearch via a k-NN plugin with a choice of engine. It's just more honest to place them on their own axis — "a search engine that also does vectors" — as opposed to vector-native engines (Qdrant, Milvus, Weaviate), which were built around approximate nearest-neighbor search from day one. Both categories are vector databases; what tells them apart is their origin, and that origin brings a set of strengths with it. Let's run through the 2026 cheat sheet, keeping in mind that scale ceilings keep moving and are worth checking on the day of the lecture.

pgvector is a Postgres extension. You reach for it when the data is already in Postgres and you need one system with transactional consistency. It comfortably holds on the order of fifty million vectors, and degrades past fifty-to-one-hundred million without special add-ons. Qdrant is a dedicated engine with minimal operational overhead, with native sparse and multi-vector primitives. Weaviate carries a built-in hybrid: vector, BM25, and metadata filters out of the box. Milvus is built for hundreds of millions and billions of vectors, with compute and storage split apart, but it requires a real operational investment. FAISS is a library, not a database: raw speed and full control, but you write persistence, CRUD, and filters yourself. Chroma and LanceDB cover prototyping, notebooks, and the local edge scenario.

Frameworks are a separate topic. The 2026 consensus: LlamaIndex and LangChain aren't competitors but complementary layers. LlamaIndex is strong when the hard part is retrieval over messy private documents: ingestion, indexing, sensible defaults. LangGraph provides orchestration: durable execution, checkpointing, human-in-the-loop with pauses of hours or days.

And a skeptical caveat that ties back to the ladder rule: for a simple RAG endpoint, where everything comes down to "retrieve, then generate," you don't need any framework at all. A few hundred lines of your own glue code spare you version churn and leaky abstractions. A framework gets added for agentic, multi-step complexity, not by default.

Sources:
[1] firecrawl — Best Vector Databases 2026 (engine ceilings) — pgvector ~50M; Milvus 100M+/billions; Qdrant/Weaviate/FAISS/Chroma/LanceDB. https://www.firecrawl.dev/blog/best-vector-databases [VFY-day-of]
[2] TigerData — pgvector vs Qdrant (vendor benchmark, read skeptically) — 471 QPS@99% recall at 50M — a vendor number; measure on your own data. https://www.tigerdata.com/blog/pgvector-vs-qdrant [VFY-day-of]
