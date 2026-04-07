---
title: "How to Organize a Repository for an LLM Agent"
slug: how-to-organize-repo-for-llm-agent
date: 2026-04-07
status: review
targets: [blog, habr]
tags: [claude-code, repository, llm-agent, knowledge-management, rag, devops]
lang: en
published_urls: {}
pair_slug: how-to-organize-repo-for-llm-agent-ru
issue: "#38"
categories: [Data architecture]
---

# How to Organize a Repository for an LLM Agent

> **More complex is better? I don't think so.** Five tiers of repository organization:
>
> - **Tier 0** — flat files. Everything in context. Prototypes, configs, small projects under 20 files.
> - **Tier 1** — text search + CLAUDE.md. How every AI coding agent works. Code projects up to 500 files.
> - **Tier 2** — docs-as-code. Structured documentation for teams. Stripe, Kubernetes, Django — no RAG needed.
> - **Tier 3** — LLM wiki, the Karpathy method. An LLM compiles a wiki from raw sources. Hundreds of documents.
> - **Tier 4** — wiki + RAG + knowledge graph. Semantic search and entity relationships. 500+ sources.
>
> Don't move to the next tier if the current one works.

LLM agents today solve radically different problems. One writes code in a ten-thousand-file repository. Another researches five hundred scientific papers. A third maintains documentation for two hundred people. Applying the same knowledge organization approach to all of these is overkill. I went through all five tiers on my own project — a university course on AI with hundreds of sources, dozens of artifacts, and a single author — and below I'll explain what works at which scale.

In 2024–2025, while the industry was building complex RAG pipelines and knowledge graphs, Cursor [soared to $100M ARR](https://dev.to/pockit_tools/cursor-vs-windsurf-vs-claude-code-in-2026-the-honest-comparison-after-using-all-three-3gof) with an approach built on an embedding index and text search over code. Not because text search is better than RAG — but because for code, it's the right tool. Specifically for code.

In the world of knowledge organization for agents, people make two symmetrical mistakes. Some underinvest: 500 documents plus text search equals chaos — nothing gets found. Others overinvest: as [Paul Hoke described](https://medium.com/@paulhoke/the-context-window-arms-race-what-i-learned-after-deleting-2-000-lines-of-rag-code-94bf38e5eca9), a developer deleted 2,000 lines of RAG code and accuracy jumped to 94%.

There is no "best" way to organize knowledge for an LLM agent. There are five tiers, each the best answer for its type of task and scale. Move to the next one only when the current tier breaks on a specific pain point. Context windows of all major models in 2026 have [reached a million tokens and beyond](https://codingscape.com/blog/llms-with-largest-context-windows) — Gemini, Claude, Llama, GPT — and this shifts the threshold at which search infrastructure is even justified.

## Tier 0: Everything Fits in Context — and That's Great

Google NotebookLM lets you upload up to 50 sources and ask questions about them. Claude Projects from Anthropic is a feature where you add files to a "project" and the agent works with them in their entirety. Tens of millions of users. No RAG, no vector indexes. Just files in context. This isn't an MVP — it's a [production architecture](https://elephas.app/blog/notebooklm-vs-claude-projects).

### The Core Idea

All files are loaded entirely into the LLM's context window. No search, no indexing. With 20 files of 200 lines each, that's roughly 16,000 tokens — 1.6% of Claude's window. As the [Ahoi Kapptn team writes](https://ahoikapptn.com/en/blog/from-long-prompt-to-rag-how-to-build-robust-ai-agents-with-your-knowledge-base): "If your knowledge base is under 200K tokens (~500 pages), include it entirely in the prompt."

Where this works perfectly: load 10 articles and ask questions — get synthesis with zero minutes of setup. A prototype with 5 files — the agent sees everything, accuracy is maximal. 15 infrastructure project configs — full context, zero latency. My AI course started exactly this way: two dozen files, everything fit in context, and the agent found what it needed instantly.

### Example Structure

```
my-project/
  notes.md                 # notes, ideas, drafts
  data-analysis.py         # all code — 3-5 files
  config.yaml
  research-paper-1.pdf     # all sources right in the root
  research-paper-2.pdf
```

### When to Move On

One day you notice the agent starting to "forget" information. [Research from Stanford and UC Berkeley](https://arxiv.org/abs/2307.03172) (Liu et al., 2023) demonstrated the lost-in-the-middle effect: accuracy drops by 30% or more when relevant information lands in the middle of the context. [Another study](https://arxiv.org/pdf/2509.21361) found that the effective context of all models on complex tasks turned out to be far smaller than advertised. The boundary: roughly 20 files or 50,000 tokens. If you feel this pain — time for the next tier. If not — stay put, you're in the right place.

| Pattern | Anti-pattern |
|---------|-------------|
| All files in one folder, no nesting | Setting up RAG for 5 documents |
| Maximally flat structure | Dumping 100 files into context "just in case" |
| Zero infrastructure, zero setup | Creating a folder hierarchy for 10 files |

## Tier 1: Text Search + CLAUDE.md — How Every AI Coding Agent Works

Cursor. Claude Code. Windsurf. None of them require developers to spin up a vector database. All use text search as their core infrastructure. As [BuildMVPFast writes](https://www.buildmvpfast.com/blog/ripgrep-10-years-fast-cli-tools-ai-agents-2026): "Text search has quietly become the load-bearing infrastructure for how AI writes code."

### The Core Idea

At this tier, the project has a CLAUDE.md (or [AGENTS.md](https://agents.md/), .cursorrules) that explains the codebase structure and conventions to the agent. The agent reads CLAUDE.md and understands the lay of the land — which directories are responsible for what, what naming conventions are in use. When a task arrives, the agent searches by keywords, finds the right files, then reads them in full for complete context. The directory structure itself becomes a navigation map.

At Tier 0, the agent sees everything but doesn't know what matters. CLAUDE.md provides priorities. Search lets the agent read only the files it needs rather than loading all 500 into context. AGENTS.md is already [standardized](https://agents.md/) by the Linux Foundation, supported by OpenAI, Anthropic, Google, AWS, and Bloomberg. Over 60,000 repositories include it. As [HumanLayer notes](https://www.humanlayer.dev/blog/writing-a-good-claude-md): "A CLAUDE.md written in 30 minutes gives the agent 80% of the context it needs." To get started — create a CLAUDE.md and describe the architecture, key conventions, and how to run and test the project.

Text search objectively outperforms semantic search for exact matches. As [ast-grep notes](https://ast-grep.github.io/blog/code-search-design-space.html): `ERROR_4532` in vector space is indistinguishable from `ERROR_4533` — yet these are completely different errors. My AI course moved to this tier when sources exceeded twenty — search over exported documents was fast and accurate.

### Example Structure

```
my-repo/
  CLAUDE.md              # ← instructions for the agent: architecture, conventions
  AGENTS.md              # standardized rules (can be used instead of CLAUDE.md)
  src/                   # project code
  tests/                 # tests alongside the code
  docs/
    architecture.md      # keep documentation next to the code
    adr/
      001-use-postgres.md  # architectural decisions in ADR format
```

### When to Move On

You have 300 code files and search works great. Then a task comes in: find all GDPR requirements across research notes, legal documents, and meeting transcripts. Searching for the word "GDPR" finds 5 out of 20 relevant documents — the rest talk about "personal data", "privacy regulation", "data processing". This is the [polysemy problem](https://arxiv.org/html/2601.23254v1): one concept, dozens of names. You don't need a better search engine — you need structured navigation. The boundary: roughly 500 files, predominantly code. For non-code knowledge — PDFs, regulations, research — this model doesn't work.

| Pattern | Anti-pattern |
|---------|-------------|
| CLAUDE.md with architecture and conventions | Hoping the agent will "figure it out" |
| Consistent naming conventions | Different styles in different parts of the project |
| AGENTS.md + separate .md files per subdirectory | One giant 2,000-line CLAUDE.md |
| Text search for code and identifiers | Text search for concepts in prose |

## Tier 2: Docs-as-Code — Structured Documentation for Teams

This tier is for projects where documentation is created by people for people, and the AI agent gets quality navigation for free. Stripe docs, Kubernetes (3,000+ pages), Django, Terraform — they serve millions of developers without RAG and have no plans to switch. As [Mintlify notes](https://www.mintlify.com/blog/stripe-docs): "At Stripe, a feature isn't considered shipped until the documentation is written."

### The Core Idea

Documentation is organized by content type. The [Diataxis framework](https://diataxis.fr/) divides it into 4 types — tutorials, how-to guides, reference, and explanation. When search finds the word "authentication" in 15 files, an agent without content typing has to read all 15. With Diataxis, it goes straight to `how-to/configure-oauth.md`. The framework is [adopted by](https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation) Cloudflare, Ubuntu, Django, and Gatsby.

The key advantage is a dual audience. A new team member reads the same documents as the AI agent. At Tier 3, the wiki is also human-readable but optimized for agent navigation. Here, there's a single source of truth for both audiences. Plus, documentation gets indexed by search engines — a wiki behind an LLM or a RAG system is invisible to Google. To get started: sort your documents into the 4 [Diataxis](https://diataxis.fr/) types and add a navigational index.md. One day for an average project.

### Example Structure

```
docs/
  index.md                 # ← navigation hub, start here
  tutorials/
    getting-started.md     # learning material for newcomers
  how-to/
    configure-auth.md      # instructions: "how to do X"
  reference/
    api/                   # reference docs, often generated from code
  explanation/
    architecture.md        # explanations: "why we chose X"
  adr/
    001-use-postgres.md    # architectural decisions in ADR format
```

### When to Move On

Maintenance cost — that's what breaks this tier. At 200+ documents, classification becomes the bottleneck, and heterogeneous sources — scientific papers, transcripts, regulatory documents — don't fit into neat templates.

| Pattern | Anti-pattern |
|---------|-------------|
| Diataxis: 4 content types | A flat docs/ folder with no typing |
| Build-time link validation | Manually checking "did we break any links" |
| ADRs for architectural decisions | Decisions in chat, lost within a month |

## Tier 3: The Karpathy Method — LLM as Librarian

According to [ussumant/llm-wiki-compiler](https://github.com/ussumant/llm-wiki-compiler), 383 files became 13 articles — 81x compression. 130 meeting transcripts became a single 244-line digest — 503x compression. And this isn't lossy summarization: the LLM finds connections between sources that a human would miss. As [Karpathy wrote](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): "With ~100 articles and ~400K words, the LLM's ability to navigate through summaries and index files is more than sufficient."

### The Core Idea

Three-layer architecture (Andrej Karpathy, April 2026): `raw/` — immutable sources (PDFs, transcripts, notes), append-only, no editing; `wiki/` — LLM-generated and LLM-maintained pages; `index.md` — a catalog of all wiki pages with one-line descriptions. The index is the search mechanism: the LLM scans it, finds the right page, reads it.

Three operations: **Ingest** — read a source, write a wiki page, update the index, update 10–15 related pages. **Query** — find an answer by scanning the index, save good answers as new pages. **Lint** — detect contradictions, orphaned pages, and outdated claims.

This is paradise for the solo researcher. One person plus one LLM replaces a documentation team. My AI course moved to this tier when sources reached the hundreds — a single maintainer manages the entire knowledge base through a wiki. Lint proactively detects outdated claims — unlike Tier 2 documentation, which goes stale silently. The entire "stack" is markdown in git. According to [ussumant/llm-wiki-compiler](https://github.com/ussumant/llm-wiki-compiler), the agent starts a session with a compact index (~7.7K tokens) instead of hundreds of files (~47K) — an 84% reduction.

[Karpathy's gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) garnered [millions of views](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an) — it struck a nerve. Full implementations have already appeared: [ussumant/llm-wiki-compiler](https://github.com/ussumant/llm-wiki-compiler) (Claude Code plugin), [atomicmemory/llm-wiki-compiler](https://github.com/atomicmemory/llm-wiki-compiler) (TypeScript, concept extraction), [xoai/sage-wiki](https://github.com/xoai/sage-wiki) (Go, hybrid text + vector search). As [MindStudio notes](https://www.mindstudio.ai/blog/llm-wiki-vs-rag-markdown-knowledge-base-comparison): "If your knowledge base is under 50,000–100,000 tokens, there's no technical reason to use RAG."

If you need semantic search over heterogeneous sources but without wiki compilation, you can simply load documents into a local RAG system and get meaning-based search in a single evening. To start with a wiki: create `raw/` and `wiki/`, add a CLAUDE.md with conventions from [Karpathy's gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Ingest 10–20 documents per session — the wiki grows organically.

### Example Structure

```
knowledge-base/
  CLAUDE.md                # ← schema and conventions from Karpathy's gist
  index.md                 # catalog: one line per wiki page
  log.md                   # operations log (append-only)
  raw/                     # immutable sources
    paper-attention-2017.pdf
    meeting-2026-03-15.txt
    regulation-gdpr.md
  wiki/                    # LLM-generated pages (flat structure)
    transformer-architectures.md
    gdpr-compliance.md     # ← the LLM found a connection to three sources
    team-decisions-q1.md
    # wiki is flat: LLM navigates via index.md, no subdirectories needed
```

### When to Move On

You're running a research project: 200 papers, 50 meeting transcripts, 30 regulatory documents. The wiki handles it beautifully. Then a request comes in: "find everything related to model fairness evaluation." But in wiki pages, this topic is called "fairness metrics"; in source files, "bias evaluation"; in regulatory documents, "equity assessment." The index is a precision tool: it finds what's listed. Semantic discovery is not its job. At 500+ sources, the index itself exceeds 50,000 tokens and no longer fits in context.

| Pattern | Anti-pattern |
|---------|-------------|
| raw/ append-only, wiki/ maintained by LLM | Editing the wiki by hand (breaks on recompilation) |
| One index.md with one-line descriptions | Nested indexes "for the future" with fewer than 100 pages |
| Incremental compilation | Full recompilation of 500 sources every time |
| Lint after every Ingest | Accumulating 100 sources and compiling them all at once |

## Tier 4: When the Index Doesn't Fit in Context — Add Semantics

In my AI course, the Karpathy-method wiki delivered a 7.6x reduction in tool calls and 9 out of 9 on completeness scores. But when I needed to find "everything about AI agents" across Russian-language documents, the wiki index didn't help. The topic appeared under five different names in fifteen different places. Only semantic search found what text search and the index missed.

### The Core Idea

At this tier, the wiki (Tier 3) is supplemented with one or two layers. **RAG (vector search)** — semantic search via embeddings, finds "equity measures" when you search for "fairness metrics." **Knowledge graph (ontology)** — structured relationships between entities: "paper X cites method Y, applied in domain Z." The wiki remains the foundation — readable, navigable, in git. RAG and the graph are additional search layers on top, with results combined via [Reciprocal Rank Fusion](https://www.pinecone.io/learn/vectors-and-graphs-better-together/).

The cost isn't necessarily high. In my course, I use local free tools: [Oxigraph](https://github.com/oxigraph/oxigraph) (an RDF store for the knowledge graph), mcp-local-rag (local semantic search with no external services) — everything lives in a single git repository, infrastructure cost is zero. For larger-scale tasks, [LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) from Microsoft promises order-of-magnitude reductions in indexing costs. [LightRAG](https://medium.com/accelerated-analyst/lightrag-a-better-approach-to-graph-enhanced-retrieval-augmented-generation-0ac9e7bf9b74) delivers 70–90% of the quality at a hundredth of the cost.

**Research library** — the wiki compiles literature reviews, RAG finds papers by meaning, the graph tracks citation chains. **Agent knowledge base** — in my course: wiki for navigation, RAG for bilingual search (Russian and English), ontology on Oxigraph for traceability: "requirement -> lecture -> seminar -> assessment." **Team knowledge base** — three years of accumulated experience: meeting transcripts, project documents, post-mortems; the wiki provides topic overviews, RAG finds "that time we already solved a similar problem." Start with RAG on top of an existing wiki — one evening. Add the graph only when specific relational queries appear.

### Example Structure

```
knowledge-base/
  CLAUDE.md
  index.md                 # wiki index (Tier 3)
  raw/                     # sources
    papers/
      by-topic/            # grouped by topic for convenience
    meeting-notes/
    regulations/
  wiki/                    # LLM-compiled pages
  index/                   # ← RAG index, add this first
  ontology/                # knowledge graph, add when you need relationships
    schema.ttl             # classes and properties (I use Oxigraph)
    store.ttl              # data
    queries/               # SPARQL queries for common questions
```

### When You Need This

| You need RAG when | You need a knowledge graph when |
|-----------------|--------------------------|
| Bilingual search (RU and EN) | Multi-hop queries ("papers by author X -> method Y -> domain Z") |
| "Find something similar" (fuzzy discovery) | Traceability (requirement -> test -> coverage) |
| Wiki index exceeds 50,000 tokens | Aggregation ("all papers with no citations") |
| Heterogeneous sources | Taxonomies and classifications |

| Pattern | Anti-pattern |
|---------|-------------|
| Wiki as foundation + RAG/graph as layers | RAG instead of wiki (you lose navigation) |
| Local free tools (Oxigraph, local-rag) | Paying $200/mo for a vector DB to index 100 documents |
| Adding layers one at a time | Building the entire infrastructure upfront "for growth" |
| Graph for specific relational queries | Graph "because it looks cool" with no clear use cases |

## How I Walked This Path

My AI course — hundreds of sources, dozens of artifacts, one maintainer.

I started at Tier 0: two dozen files, everything in context. Quickly outgrew it into Tier 1: search over exported documents. Tried RAG — got 10% precision on Russian-language queries. Tried an ontology — a beautiful schema, zero data.

I implemented Tier 3 — the Karpathy-method wiki: 7.6x reduction in tool calls, 9 out of 9 on completeness across test scenarios. Added RAG for semantic search on bilingual queries — but only after the wiki was working.

The key lesson: I tried to jump from Tier 1 to Tier 4 — and got beautifully empty infrastructure. Only when I went back to Tier 3 as the foundation and layered search on top did the system start working.

## How to Determine the Right Structure

The entire selection framework boils down to two questions:

1. **How many sources do you have?** (fewer than 20 / 20 to 500 / more than 500)
2. **What is it — code or documentation?** (code / documentation for people / research, papers, heterogeneous sources)

| Scale \ Content | Code | Documentation for people | Research, heterogeneous |
|-------------------|-----|----------------------|---------------------------|
| Fewer than 20 files | Tier 0 | Tier 0 | Tier 0 |
| 20--500 | Tier 1 (search + CLAUDE.md) | Tier 2 (docs-as-code) | Tier 3 (LLM wiki) |
| More than 500 | Tier 1 + indexed search | Tier 2 (scales to 3,000+) | Tier 3 + 4 (RAG/graph) |

Hybrid situations are the norm. "200 code files + 50 research papers" means code at Tier 1 (search + CLAUDE.md), papers at Tier 3 (wiki). Tiers aren't mutually exclusive — they're about content type.

## Most of You Are at Tier 1. And That's Fine

Entrepreneur Vamshi Reddy wrote to Karpathy: "Every business has a raw/ directory. Nobody has compiled it yet. There's the product."

I myself spent a sprint on a four-layer system with an ontology and SPARQL queries. Beautiful architecture. Graphs, relationships, validation. Then I opened the knowledge graph and discovered it was empty. Zero data. Right next to it sat a 40-line CLAUDE.md through which the agent had already been finding everything it needed for a week.

The right answer depends on the task. Tier 0 remains the best for small projects — NotebookLM serves millions of users without a single vector index. Tier 1 is for code. Stripe isn't switching to RAG for their documentation, and they see no reason to. The Karpathy-method wiki is for researchers with hundreds of heterogeneous sources. And hybrid Tier 4 is justified where the cost of unfound information is measured in lost revenue or patients.

Each tier is not a step on a ladder but the right tool for its scale. A simple rule: if you're not experiencing a specific pain point at your current tier — you're in the right place.
