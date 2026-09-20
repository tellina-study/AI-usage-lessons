---
id: s-rag-chunk1
type: comparison
section: "Section 2. RAG"
duration_min: 2
assertion: "Chunking strategies from simple to complex (fixed / recursive / sentence-window / semantic / parent-document / late / contextual); there is no single correct default — you tune it to the corpus"
learning_goal: "Chunking strategies and when to use which (§2.9)"
learning_outcomes: [LO7]
chapter_ref: "§2.9 [for-slide-rag-chunk-strategies]"
subtype: schema_matrix
new_in_v4: "#196 WAVE 2 — RAG deepening"
---

# Visible content

## Title
«Chunking: how you cut is what you can find.»

## Speaker notes

Of the three steps in RAG, chunking is the one most underrated, and its leverage is high: how you cut a document into fragments determines what can even be retrieved. We already named poor chunking as one of the three technical roots of RAG failures; let's go through the strategies in order, from simple to complex.

Fixed-size cuts every N tokens or characters. It's crude, but fast, reproducible, and a surprisingly strong baseline. Recursive, or the character strategy, cuts along a hierarchy of separators — paragraph, then sentence, then word — respecting structure while bounding size; it's the pragmatic default. Sentence-window embeds a single sentence for precision but returns a window of neighboring sentences to the model for context. Semantic places the boundary where the embedding similarity of neighboring sentences drops sharply, i.e. at a topic shift; it sounds intuitive but often doesn't pay off — more on that on the next slide. Parent-document, also called small-to-big, indexes small chunks for retrieval precision but returns the larger parent block for generation — a widely recommended cure for lost context. Late chunking first embeds the whole document at the token level, then pools it into chunk embeddings so each one is context-aware, preserving pronouns and references.

Contextual Retrieval stands apart: an LLM prepends fifty to a hundred tokens of document-level context to each chunk before embedding and before BM25 indexing. This is exactly the technique that produced the miss-cascade drop from 5.7 to 1.9 percent that we saw on the RAG-principle slide.

Keep the main point in mind: neither chunk size nor strategy has a single correct default. You tune them to your corpus, and tuning without a metric is flying blind. Metrics come on the system-design slide.

Sources:
[1] firecrawl — Best Chunking Strategies for RAG — fixed / recursive / sentence-window / semantic / parent-document / late / contextual. https://www.firecrawl.dev/blog/best-chunking-strategies-rag
[2] Anthropic — Contextual Retrieval (50–100 tokens of context per chunk) — prepending document-level context before embedding and BM25 indexing. https://www.anthropic.com/engineering/contextual-retrieval
