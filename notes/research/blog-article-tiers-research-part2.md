---
title: "Research: 5 Tiers of Knowledge Organization for LLM Agents"
part: 2
parts_total: 2
description: "Part 2: Tiers 3-4 (LLM-compiled wiki, Hybrid retrieval) + Cross-cutting findings"
issue: "#37"
date: 2026-04-07
type: research-note
---

# Research: 5 Tiers of Knowledge Organization for LLM Agents (Part 2)

> Part 2: Tiers 3-4 + Cross-cutting. See also: [Part 1 — Tiers 0-2](blog-article-tiers-research-part1.md)

---

## Tier 3: LLM-Compiled Wiki (Karpathy Method)

### Definition

Raw sources go into a `raw/` directory. An LLM reads them, compiles wiki pages, maintains an index. The index is the primary retrieval mechanism — the LLM scans it to find relevant pages. No vector DB needed at this scale.

### Karpathy's Original Pattern (April 2026)

Three layers: `raw/` (immutable sources), `wiki/` (LLM-generated markdown), `CLAUDE.md` (schema/conventions). Two supporting files: `index.md` (catalog with one-line summaries) and `log.md` (append-only operations record).

Three operations: **Ingest** (read source, write summary, update index, update 10-15 related pages), **Query** (search wiki to synthesize answers, file good answers as new pages), **Lint** (detect contradictions, orphan pages, stale claims).

**Scale quote from Karpathy:** "At ~100 articles and ~400K words, the LLM's ability to navigate via summaries and index files is more than sufficient. For a departmental wiki or personal research project, 'fancy RAG' infrastructure often introduces more latency and retrieval noise than it solves."

Source: [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

### Implementations (as of April 2026)

**1. ussumant/llm-wiki-compiler (Claude Code Plugin)**

- Coverage indicators per section: high (5+ sources — trust wiki), medium (2-4 — check raw for detail), low (0-1 — read raw directly)
- Compression: 383 files (13.1 MB) -> 13 articles (161 KB) = **81x compression**
- Meeting transcripts: 130 transcripts (122,625 lines) -> 1 digest (244 lines) = **503x compression**
- Session startup token reduction: ~47K -> ~7.7K tokens = **84% reduction**
- Concept articles auto-discovered when a topic appears across 3+ sources
- Three adoption modes: staging (wiki on demand), recommended (wiki before raw), primary (wiki is source)

Source: [GitHub — ussumant/llm-wiki-compiler](https://github.com/ussumant/llm-wiki-compiler)

**2. atomicmemory/llm-wiki-compiler (TypeScript + Anthropic API)**

- Structured tool_use for concept extraction (3-8 concepts per source, with `is_new` flag to prevent duplicates)
- Cross-reference resolver ensures bidirectional links
- Orphan page detection — pages that exist but aren't referenced
- Dependency graph for navigating related concepts

Source: [GitHub — atomicmemory/llm-wiki-compiler](https://github.com/atomicmemory/llm-wiki-compiler)

**3. xoai/sage-wiki (Go, production-grade)**

- 5-pass pipeline: diff detection, summarization, concept extraction, article writing, embedding generation
- Hybrid BM25 + vector search (weight: 0.7 BM25 / 0.3 vector)
- SQLite backend with checkpoint/resume for interrupted compilations
- Per-task model selection (cheap for summarize, quality for write)
- Watch mode with 2s debounce for continuous compilation

Source: [GitHub — xoai/sage-wiki](https://github.com/xoai/sage-wiki)

**4. Astro-Han/karpathy-llm-wiki** — Skill-based implementation that fetches content into raw/ then compiles to wiki articles.

### Comparison: LLM Wiki vs RAG

From MindStudio's analysis:

| Dimension | LLM Wiki | RAG |
|-----------|----------|-----|
| Setup complexity | Low (markdown files) | High (vector DB + embedding pipeline) |
| Infrastructure | None | Vector DB, embedding service |
| Updates | Edit markdown | Re-chunk, re-embed, re-index |
| Token cost (small KB) | 90-95% cheaper than naive loading | Higher due to embedding overhead |
| Best under | 50K-100K tokens (~150-200 pages) | 100K+ tokens |
| Source attribution | Manual (explicit wiki links to raw) | Built-in (chunk provenance) |

**Threshold:** "If your knowledge base is under 50,000-100,000 tokens, there's no technical reason to use RAG."

Source: [MindStudio — LLM Wiki vs RAG](https://www.mindstudio.ai/blog/llm-wiki-vs-rag-markdown-knowledge-base-comparison)

### Comparison: LLM Wiki vs Obsidian/Notion AI

**Obsidian + AI plugins (2026):**
- Local-first plain text, bidirectional links, Graph View
- AI Assistant plugin (Jan 2026) supports GPT-4, Claude, local models via Ollama
- All processing on device — no data leaves
- 8% market share but dominates PKM niche among developers/researchers

**Notion AI (2026):**
- Notion 3.0 (Sep 2025) rebuilt AI as a full agent
- $10/user/month add-on: summaries, Q&A over databases, automated fill
- 70% of Fortune 500 teams, < 5% Obsidian adoption in enterprise
- Cloud-only, proprietary models

**Key difference:** LLM Wiki is a *compilation* pattern — the LLM transforms raw sources into structured knowledge. Obsidian/Notion are *note-taking tools* with AI features bolted on. The wiki approach creates a knowledge artifact that stands on its own; the tool approach keeps knowledge in a proprietary format tied to the editor.

Sources: [Notion vs Obsidian 2026](https://www.browse-ai.tools/blog/ai-automation-agency-guide-notion-vs-obsidian-2026), [NxCode — Obsidian AI](https://www.nxcode.io/resources/news/obsidian-ai-second-brain-complete-guide-2026)

### Where Tier 3 Shines

**1. The Compression Miracle**

This isn't just smaller — it's BETTER because the LLM synthesizes across sources:
- ussumant/llm-wiki-compiler: 383 files (13.1 MB) -> 13 articles (161 KB) = **81x compression**
- Meeting transcripts: 130 transcripts (122,625 lines) -> 1 digest (244 lines) = **503x compression**
- Session startup: ~47K -> ~7.7K tokens = **84% reduction**

The compiled wiki doesn't just compress — it surfaces cross-cutting themes, resolves contradictions, and creates navigational structure that didn't exist in the raw sources.

**2. Zero-Infrastructure Semantic Search**

The index IS the search. No vector DB, no embedding pipeline, no managed service. Just markdown files in a git repo. Deploy by pushing to GitHub. The entire "infrastructure" is `git push`. Compare this to Tier 4's minimum ~$185/month for vector DB + graph DB + BM25 index.

**3. Solo Researcher Paradise**

One person + one LLM can maintain a knowledge base that would require a dedicated documentation team at Tier 2. The LLM does the librarian work: classifying, cross-referencing, summarizing, detecting concept overlap. Karpathy's gist amassed 16 million views and thousands of reposts because it resonated with solo researchers drowning in unstructured sources.

Source: [VentureBeat — Karpathy LLM Knowledge Base](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an)

**4. Self-Healing Knowledge Base**

The Lint operation detects stale claims, orphan pages, and contradictions. Tier 2 docs go stale silently — a tutorial linking to a deprecated API passes validation if the page still exists. Tier 3 wiki actively maintains itself: the LLM can flag "this claim from source X contradicts the newer finding in source Y."

**5. Real Adoption Beyond Karpathy**

- DPC Messenger team found they "already implement ~70% of the LLM Wiki pattern" and extended it into a social knowledge system
- Lex Fridman and others echoed similar setups, confirming the pattern's resonance
- One user built a full personal-life knowledge base from X data, Google Takeout, health exports, and AI chat histories
- Entrepreneur Vamshi Reddy: "Every business has a raw/ directory. Nobody's ever compiled it. That's the product." Karpathy agreed.
- Our own repo (AI-usage-lessons) uses this pattern for course material management

Sources: [DAIR.AI — LLM Knowledge Bases](https://academy.dair.ai/blog/llm-knowledge-bases-karpathy), [Antigravity — Karpathy's LLM Wiki Guide](https://antigravity.codes/blog/karpathy-llm-wiki-idea-file)

### When NOT to Upgrade from Tier 3

- Your knowledge base is < 500 heterogeneous sources — the wiki index fits in context, no need for RAG
- You're a solo researcher or small team — the LLM-as-librarian model works perfectly
- Your queries are navigational ("what do we know about X?") not discovery ("find something related to fairness") — index scanning handles navigational queries well
- You value zero infrastructure over marginally better fuzzy search — markdown files in git > vector DB
- "If your knowledge base is under 50,000-100,000 tokens, there's no technical reason to use RAG" — MindStudio

### Pain Points (Why Tier 3 Breaks)

**1. Index Exceeds Context Window**

At ~300 entries, a single index.md exceeds 600 lines. At ~500+ sources, even a compact index with one-line summaries can reach 50K+ tokens. When the index doesn't fit in context, the LLM can't scan it to find relevant pages, and the entire premise breaks.

**2. Compilation Cost**

Full recompilation of 500 sources requires hundreds of LLM calls. At $3/M tokens input, recompiling a 500-source wiki costs $10-50 depending on source length. Incremental compilation helps but concept extraction still requires cross-referencing against existing wiki.

**3. No Fuzzy Discovery**

The wiki index is precise — you find what's listed. But "find me something related to fairness metrics" requires semantic understanding of all wiki pages, not just scanning titles. If the concept was named "equity measures" in the wiki, index scanning misses it.

**4. Single-Maintainer Bottleneck**

Karpathy's pattern assumes a single LLM maintainer. Multiple agents or users updating the wiki simultaneously create merge conflicts, inconsistent cross-references, and competing compilation decisions.

### Threshold

Tier 3 works well for solo researchers, departmental knowledge bases, and project documentation with up to ~500 heterogeneous sources. Breaks down when the index exceeds context, when semantic discovery is needed, or when multiple agents need concurrent access.

---

## Tier 4: Hybrid Retrieval (Wiki + RAG + Optional Knowledge Graph)

### Definition

Combine a compiled wiki (Tier 3) with vector search for semantic discovery and optionally a knowledge graph for relational queries. Multiple retrieval strategies are merged via Reciprocal Rank Fusion (RRF) or learned routing.

### Microsoft GraphRAG (2024-2026)

**Pipeline:** LLM extracts entities + relationships from text chunks -> Leiden community detection -> hierarchical community summaries -> queries answered by map-reducing over summaries.

**Scale numbers (podcast corpus, 1M tokens):** 8,564 nodes, 20,691 edges. Communities: 34 root, 367 level-1, 969 level-2, 1,310 leaf.

**vs Naive Vector RAG:** Comprehensiveness win rate 72-83%, diversity 75-82%. Claims per answer: 31-34 vs 25-27. Key insight: "Naive RAG retrieves similar chunks. GraphRAG answers global sensemaking questions requiring synthesis across entire corpus."

**Cost:** 281 minutes indexing for 1M tokens with GPT-4-turbo. "$33K indexing cost for large datasets" made it impractical for most teams initially.

Sources: [Microsoft GraphRAG paper](https://arxiv.org/html/2404.16130v2), [Microsoft Research](https://www.microsoft.com/en-us/research/project/graphrag/)

### LazyGraphRAG (Microsoft, 2025-2026)

A radical cost reduction: defers LLM summarization to query time instead of indexing time.

- **Indexing cost:** Same as vector RAG, **0.1% of full GraphRAG** (1000x cheaper)
- **Query cost at budget=500:** Comparable quality to GraphRAG Global Search at **700x lower query cost**
- **How:** NLP-based extraction instead of LLM entity recognition, graph optimization for hierarchical communities, iterative relevance testing with configurable budget

**When to use:** One-off queries, exploratory analysis, streaming data, when indexing costs are prohibitive.
**When NOT to use:** When summarized indexes provide independent value beyond Q&A.

Source: [Microsoft Research — LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)

### LightRAG

Simpler extraction with flat graph structure. Delivers **70-90% of GraphRAG's quality at ~1/100th indexing cost**. Requires < 100 tokens for retrieval tasks that need 610K+ tokens in traditional GraphRAG — a **6000x efficiency improvement**. Cost: ~$0.15 vs $4-7 per document.

Source: [Medium — LightRAG](https://medium.com/accelerated-analyst/lightrag-a-better-approach-to-graph-enhanced-retrieval-augmented-generation-0ac9e7bf9b74)

### HybridRAG (NVIDIA/BlackRock, 2024)

Two parallel channels: VectorRAG (embed + cosine similarity) + GraphRAG (entity extraction + graph traversal). Results concatenated before generation. Tested on financial earnings call transcripts.

**Finding:** HybridRAG outperforms both individual approaches. Vector captures semantic similarity, graph captures structured relational facts ("Company X acquired Company Y in Q3").

**Limitation:** KG extraction expensive and error-prone on messy text. On opinion/narrative without clear entities, graph channel adds cost without benefit.

Source: [HybridRAG paper](https://arxiv.org/abs/2408.04948)

### Production Hybrid Systems

**Glean (enterprise search):** Vector embeddings + BM25 + organizational knowledge graph (ownership, reporting, permissions). Graph provides permission-aware retrieval.

**Neo4j + Pinecone:** Vector search returns top-k -> entity extraction -> Neo4j traversal enriches context -> merged context feeds LLM.

**Reciprocal Rank Fusion (RRF):** `score = sum(1/(k + rank))` across ranked lists. Simple, parameter-light, consistently outperforms learned fusion.

**Cost of 3-strategy system:** Vector DB ~$70/month per 1M vectors, Graph DB ~$65/month for 200K nodes, BM25 index ~$50/month managed, embedding ~$0.10/1M tokens one-time.

Source: [Pinecone + Neo4j](https://www.pinecone.io/learn/vectors-and-graphs-better-together/)

### Enterprise RAG Metrics (2026)

- 85% of enterprise AI applications use RAG as foundational architecture (up from 40% in 2025)
- RAG reduces hallucinations by 70-90%
- Average ROI: $3.70 per $1 invested
- BUT: Stanford AI Lab found poorly evaluated RAG produces hallucinations in up to 40% of responses despite accessing correct information
- 60% of new RAG deployments include systematic evaluation from day 1 (up from < 30% in 2025)

Sources: [LabelYourData](https://labelyourdata.com/articles/llm-fine-tuning/rag-evaluation), [Techment](https://www.techment.com/blogs/rag-in-2026/)

### When Knowledge Graph Is Justified

**Justified:**
- Multi-hop reasoning: "Papers citing Author X published in Venue Y"
- Provenance chains: Requirement -> test case -> coverage
- Aggregation/negation: COUNT, FILTER, "entities WITHOUT relationship R"
- Permission-aware retrieval (enterprise)
- When performance gains plateau at 5-15M tokens for vector-only approaches

**Over-engineering:**
- Knowledge base < 500 sources (wiki index suffices)
- No relational queries (vector search covers semantic similarity)
- Narrative/opinion content without clear entities
- Budget < $200/month for infrastructure
- Solo maintainer without graph expertise

Source: [Oxigraph benchmarks from our raw research](knowledge-architecture-raw-research-part2.md)

### Where Tier 4 Shines

**1. Discovery of Unknown Unknowns**

"Find me something related to fairness" — only semantic search can do this. All other tiers require you to know what you're looking for. Vector search finds conceptually related content even when terminology differs ("equity measures" matches "fairness metrics"). This is the tier where the system surfaces knowledge you didn't know you had.

**2. Multi-Hop Reasoning**

"Papers by Author X citing Method Y applied to Domain Z" — only graph traversal answers this efficiently. "Company X acquired Company Y in Q3" — vector similarity misses structured relational facts that graph traversal captures naturally. HybridRAG (NVIDIA/BlackRock) demonstrated that combining vector + graph outperforms either alone on financial earnings call transcripts.

Source: [HybridRAG paper](https://arxiv.org/abs/2408.04948)

**3. Enterprise Compliance — Requirements, Not Nice-to-Haves**

Permission-aware retrieval (Glean), audit trails, provenance chains — these are regulatory requirements in finance, healthcare, and legal. A multi-agent knowledge graph framework for regulatory QA enables agents to build and maintain knowledge graphs by extracting subject-predicate-object triplets from regulatory documents, with embedded triplets stored for both graph-based reasoning and efficient retrieval.

Source: [arxiv — RAGulating Compliance](https://arxiv.org/html/2508.09893v1), [Oxford Semantic — Rules and Regulation Compliance](https://www.oxfordsemantic.tech/rules-and-regulation-compliance-with-knowledge-graphs-and-ai)

**4. Real Enterprise ROI Numbers**

The investment pays back when missing information has real cost:
- RAG implementation: $200K-$500K year one, with average return of **$3.70 per $1 invested** (300-500% ROI)
- Customer support: ticket resolution time from 45 minutes to under 10 minutes (one client, 90 days)
- Cynet: 14-point CSAT lift, 47% ticket deflection, resolution times cut nearly in half
- Internal search: employee information retrieval from 9 minutes to 30 seconds (**95% improvement**)
- A major European bank: automated audit and compliance saving **EUR 20M+ over 3 years**, ROI in 2 months
- Northwestern Mutual: processing time from hours to minutes for compliance-heavy workflows

Sources: [LeanWare — Enterprise RAG Consulting](https://www.leanware.co/insights/enterprise-rag-consulting), [Techment — RAG Architectures 2026](https://www.techment.com/blogs/rag-architectures-enterprise-use-cases-2026/), [Squirro — RAG in 2026](https://squirro.com/squirro-blog/state-of-rag-genai)

**5. When It's NOT Over-Engineering**

Domains where missing information has real cost justify Tier 4 complexity:
- **Legal/compliance**: regulatory documents with cross-references, version tracking, audit requirements
- **Medical knowledge bases**: clinical decision support where missed connections can harm patients
- **Financial research**: earnings calls, filings, market data requiring relational reasoning across entities
- **Large enterprise knowledge**: 10K+ sources where no single tier handles both precision and discovery

### When NOT to Upgrade to Tier 4

This is the "are you SURE?" checklist before adding hybrid retrieval:
- Your knowledge base is < 500 sources — Tier 3 wiki handles this without infrastructure
- You don't have relational queries ("who cited whom", "which requirement maps to which test") — vector search alone suffices
- Your budget is < $200/month for infrastructure — the 3-system stack is expensive
- You're a solo maintainer without graph expertise — the learning curve is steep
- Your content is narrative/opinion without clear entities — the graph channel adds cost without benefit

### Pain Points of Tier 4

Tier 4 is the current ceiling, but it has its own costs:
- Infrastructure complexity: 3+ systems to maintain (wiki, vector DB, optionally graph DB)
- Cold-start: populating KG from scratch requires significant LLM spending
- Evaluation: no standard metrics; each deployment needs custom evaluation
- Diminishing returns: performance gains plateau at 5-15M tokens

---

## Cross-Cutting Findings

### The Progression of Pain Points

| Transition | Core Pain Point | Evidence |
|-----------|----------------|----------|
| Tier 0 -> 1 | Lost-in-middle, cost, no structure | 30%+ accuracy drop for middle context |
| Tier 1 -> 2 | Polysemy, non-code knowledge, no taxonomy | grep misses semantically related code |
| Tier 2 -> 3 | Authoring overhead, no semantic discovery, manual curation | 200+ docs = classification bottleneck |
| Tier 3 -> 4 | Index exceeds context, no fuzzy search, no relational queries | 500+ sources = index too large |

### RAG vs Long Context: The Benchmark Evidence

From the LaRA benchmark (ICML 2025, 2,326 test cases):
- Long Context outperforms RAG overall: **56.3% vs 49.0% accuracy**
- But RAG exclusively answers ~1,300 questions (10%) that LC misses
- LC excels: structured/dense contexts (Wikipedia), fact-based questions
- RAG excels: dialogue-based sources, open-ended "how" questions, multi-source synthesis
- RAPTOR (summarization-based retrieval): 38.5% accuracy vs chunk-based 20-22%
- Speed: RAG 1s average vs LC 45s average response time

Source: [Long Context vs RAG paper](https://arxiv.org/abs/2501.01880)

### Counter-Arguments

**When "just RAG" beats wiki:**
- Rapidly changing content where wiki compilation lag is unacceptable
- When source attribution is legally required (RAG has built-in provenance)
- When the knowledge base has no coherent topic structure (random FAQ)

**When flat files beat structure:**
- Prototypes and throwaway projects (structure overhead > project lifetime)
- When the entire knowledge base changes weekly (structure becomes stale faster than useful)
- Pair programming sessions where the human provides all context verbally

**When grep beats embeddings:**
- Exact identifiers: `ERROR_CODE_4532` (near-identical vectors for similar codes)
- Structured data: logs, JSON, config files
- Zero setup, zero maintenance, zero cost

### Metrics for Tier Comparison

| Metric | Tier 0 | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|--------|--------|--------|--------|--------|--------|
| Setup time | 0 | Hours | Days-weeks | Hours | Days-weeks |
| Maintenance | None | Low | Medium | Medium | High |
| Cost/query (at scale) | High (full context) | Low (grep) | Low (static site) | Medium (LLM compilation) | Medium-High (multi-retrieval) |
| Precision (known queries) | High (if fits) | High (exact match) | High (navigational) | High (index scan) | Highest (multi-strategy) |
| Recall (discovery) | High (if fits) | Low (polysemy) | Medium (taxonomy) | Medium (index only) | High (semantic + graph) |
| Scale ceiling | ~50K tokens | ~500 files | ~3000 pages | ~500 sources | 10K+ sources |
| Infrastructure | None | None | Static site gen | None (markdown) | Vector DB + optional graph |

---

## Verified/Disproven Theses

| Thesis | Status | Evidence |
|--------|--------|----------|
| 1M token context windows make RAG unnecessary | **Disproven** | Lost-in-middle (30% drop), effective context << advertised, cost scales linearly |
| AGENTS.md will become the universal standard | **Partially verified** | 60K repos, Linux Foundation backing, but Claude Code still uses native CLAUDE.md |
| Karpathy's wiki works to ~500 sources | **Verified** | Multiple implementations confirm; index breaks at ~500+ |
| GraphRAG is too expensive for most teams | **Was true, now changing** | LazyGraphRAG reduces cost 1000x for indexing; LightRAG delivers 70-90% quality at 1/100 cost |
| RAG always beats long context | **Disproven** | LC wins 56.3% vs 49.0% overall; RAG wins for specific query types |
| Knowledge graphs add value at any scale | **Disproven** | Justified only for multi-hop/relational queries at 500+ sources |
| Diataxis is the best doc framework | **Partially verified** | Works well for product docs; doesn't address research, papers, heterogeneous sources |
| Flat files work for small projects | **Verified** | Unequivocally works under ~20 files / 50K tokens |
| Every tier has a "forever" sweet spot | **Verified** | Tier 0: NotebookLM/Claude Projects serve millions; Tier 1: all AI coding tools use grep; Tier 2: Stripe/K8s docs never need RAG; Tier 3: solo researchers at < 500 sources |
| Upgrading tiers is often over-engineering | **Verified** | Developer deleted 2K lines of RAG, accuracy jumped to 94%; filesystem agents beat RAG on correctness (8.4 vs 6.4) |

---

## Sources (Master List)

### Context Windows & LLM Capabilities
- [Codingscape — LLMs with largest context windows](https://codingscape.com/blog/llms-with-largest-context-windows)
- [Elvex — Context Length Comparison 2026](https://www.elvex.com/blog/context-length-comparison-ai-models-2026)
- [Morph — LLM Token Limits 2026](https://www.morphllm.com/llm-token-limit)
- [Liu et al. — Lost in the Middle (2023)](https://arxiv.org/abs/2307.03172)
- [Maximum Effective Context Window (2025)](https://arxiv.org/pdf/2509.21361)

### Agent Config Files & Coding Tools
- [DeployHQ — AI Coding Config Files Guide](https://www.deployhq.com/blog/ai-coding-config-files-guide)
- [AgentRuleGen — cursorrules vs CLAUDE.md](https://www.agentrulegen.com/guides/cursorrules-vs-claude-md)
- [AGENTS.md specification](https://agents.md/)
- [Morph — Codebase Indexing](https://www.morphllm.com/codebase-indexing)
- [DEV.to — Cursor vs Windsurf vs Claude Code 2026](https://dev.to/pockit_tools/cursor-vs-windsurf-vs-claude-code-in-2026-the-honest-comparison-after-using-all-three-3gof)
- [HumanLayer — Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)

### Documentation Frameworks
- [Diataxis.fr](https://diataxis.fr/)
- [Sequin — We fixed our docs with Diataxis](https://blog.sequinstream.com/we-fixed-our-documentation-with-the-diataxis-framework/)
- [adr.github.io — Architecture Decision Records](https://adr.github.io/)
- [AWS — ADR Best Practices](https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/)
- [Kubernetes content guide](https://kubernetes.io/docs/contribute/style/content-guide/)
- [Stripe blog — Markdoc](https://stripe.dev/blog/markdoc)
- [Mintlify — How Stripe creates docs](https://www.mintlify.com/blog/stripe-docs)

### Karpathy LLM Wiki
- [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [ussumant/llm-wiki-compiler](https://github.com/ussumant/llm-wiki-compiler)
- [atomicmemory/llm-wiki-compiler](https://github.com/atomicmemory/llm-wiki-compiler)
- [xoai/sage-wiki](https://github.com/xoai/sage-wiki)
- [Analytics Vidhya — LLM Wiki Revolution](https://www.analyticsvidhya.com/blog/2026/04/llm-wiki-by-andrej-karpathy/)
- [VentureBeat — Karpathy LLM Knowledge Base](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an)
- [MindStudio — LLM Wiki vs RAG](https://www.mindstudio.ai/blog/llm-wiki-vs-rag-markdown-knowledge-base-comparison)

### Hybrid Retrieval & GraphRAG
- [Microsoft GraphRAG paper](https://arxiv.org/html/2404.16130v2)
- [Microsoft — LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)
- [LightRAG (Medium)](https://medium.com/accelerated-analyst/lightrag-a-better-approach-to-graph-enhanced-retrieval-augmented-generation-0ac9e7bf9b74)
- [HybridRAG paper](https://arxiv.org/abs/2408.04948)
- [Pinecone + Neo4j](https://www.pinecone.io/learn/vectors-and-graphs-better-together/)
- [GraphRAG in 2026 — practitioners guide](https://medium.com/graph-praxis/graph-rag-in-2026-a-practitioners-guide-to-what-actually-works-dca4962e7517)
- [GraphRAG-Bench (arxiv)](https://arxiv.org/html/2506.05690v3)

### RAG vs Long Context
- [Long Context vs RAG paper (2025)](https://arxiv.org/abs/2501.01880)
- [LaRA benchmark (ICML 2025)](https://openreview.net/forum?id=CLF25dahgA)
- [Meilisearch — RAG vs long-context LLMs](https://www.meilisearch.com/blog/rag-vs-long-context-llms)

### Enterprise RAG & Metrics
- [LabelYourData — RAG Evaluation 2026](https://labelyourdata.com/articles/llm-fine-tuning/rag-evaluation)
- [Techment — RAG Architectures 2026](https://www.techment.com/blogs/rag-architectures-enterprise-use-cases-2026/)

### Code Search
- [ast-grep — Code Search Design Space](https://ast-grep.github.io/blog/code-search-design-space.html)
- [GrepRAG paper](https://arxiv.org/html/2601.23254v1)
- [burntsushi — ripgrep benchmarks](https://burntsushi.net/ripgrep/)
- [Semgrep — Stop grepping code](https://semgrep.dev/blog/2020/semgrep-stop-grepping-code/)

### Tier Strengths & Over-Engineering Evidence (NEW)
- [Paul Hoke — Deleting 2000 Lines of RAG Code](https://medium.com/@paulhoke/the-context-window-arms-race-what-i-learned-after-deleting-2-000-lines-of-rag-code-94bf38e5eca9)
- [RAGFlow — 2025 Year-End Review](https://ragflow.io/blog/rag-review-2025-from-rag-to-context)
- [Ahoi Kapptn — From Long Prompt to RAG](https://ahoikapptn.com/en/blog/from-long-prompt-to-rag-how-to-build-robust-ai-agents-with-your-knowledge-base)
- [Elephas — Claude Projects vs NotebookLM 2026](https://elephas.app/blog/notebooklm-vs-claude-projects)
- [Atlas Workspace — NotebookLM vs Claude Projects](https://www.atlasworkspace.ai/blog/notebooklm-vs-claude-projects)
- [MindStudio — Is RAG Dead?](https://www.mindstudio.ai/blog/is-rag-dead-what-ai-agents-use-instead)
- [Medium — RAG Retrieval Beyond Semantic Search: grep](https://medium.com/@vanshkharidia7/rag-retrieval-beyond-semantic-search-day-1-grep-599cec898a68)
- [LlamaIndex — Filesystem Tools vs Vector Search 2026](https://www.llamaindex.ai/blog/did-filesystem-tools-kill-vector-search)
- [BuildMVPFast — Ripgrep at 10 Years](https://www.buildmvpfast.com/blog/ripgrep-10-years-fast-cli-tools-ai-agents-2026)
- [Ubuntu — Diataxis Foundation](https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation)
- [DAIR.AI — LLM Knowledge Bases](https://academy.dair.ai/blog/llm-knowledge-bases-karpathy)
- [Antigravity — Karpathy's LLM Wiki Guide](https://antigravity.codes/blog/karpathy-llm-wiki-idea-file)
- [arxiv — RAGulating Compliance](https://arxiv.org/html/2508.09893v1)
- [Oxford Semantic — Rules and Regulation Compliance](https://www.oxfordsemantic.tech/rules-and-regulation-compliance-with-knowledge-graphs-and-ai)
- [LeanWare — Enterprise RAG Consulting](https://www.leanware.co/insights/enterprise-rag-consulting)
- [Squirro — RAG in 2026](https://squirro.com/squirro-blog/state-of-rag-genai)
- [Milvus — RAG Latency](https://milvus.io/ai-quick-reference/what-is-an-acceptable-latency-for-a-rag-system-in-an-interactive-setting-eg-a-chatbot-and-how-do-we-ensure-both-retrieval-and-generation-phases-meet-this-target)
- [arxiv — RAG Systems Trade-offs](https://arxiv.org/html/2412.11854v1)

### Knowledge Management Tools
- [Notion vs Obsidian 2026](https://www.browse-ai.tools/blog/ai-automation-agency-guide-notion-vs-obsidian-2026)
- [NxCode — Obsidian AI Second Brain 2026](https://www.nxcode.io/resources/news/obsidian-ai-second-brain-complete-guide-2026)
