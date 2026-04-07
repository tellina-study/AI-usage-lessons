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

LLM agents today solve radically different problems. One agent writes code in a repository with 10,000 files. Another researches 500 scientific papers. A third maintains documentation for two hundred people. Applying the same knowledge organization approach to all of these is overkill.

While the industry was building complex RAG pipelines and knowledge graphs, Cursor [soared to $100M ARR](https://dev.to/pockit_tools/cursor-vs-windsurf-vs-claude-code-in-2026-the-honest-comparison-after-using-all-three-3gof) with a simple approach: embedding index + grep over the codebase. Not because grep is better than RAG. But because for code, grep is the right tool. Specifically for code.

In the world of knowledge organization for agents, people make two symmetrical mistakes. Some underinvest: 500 documents and grep --- chaos, nothing gets found. Others overinvest: as [Paul Hoke described](https://medium.com/@paulhoke/the-context-window-arms-race-what-i-learned-after-deleting-2-000-lines-of-rag-code-94bf38e5eca9) --- a developer deleted 2,000 lines of RAG code, and accuracy jumped to 94%. In the [LlamaIndex 2026 benchmark](https://www.llamaindex.ai/blog/did-filesystem-tools-kill-vector-search), filesystem agents beat classic RAG on correctness: 8.4 versus 6.4.

There is no "best" way to organize knowledge for an LLM agent. There are five tiers, each of which is the best answer for its type of task and scale. You should only move to the next one when the current tier breaks on a specific pain point.

The 2026 context: context windows have reached 1M+ tokens across all major providers. As [Codingscape notes](https://codingscape.com/blog/llms-with-largest-context-windows): Gemini 3, Claude 4.6, Llama 4 Scout --- all offer a million tokens and more. This shifts the threshold at which search infrastructure is even justified.

## Tier 0: Everything Fits in Context --- and That's Great

Google NotebookLM lets you upload up to 50 sources and ask questions about them. Claude Projects from Anthropic is a feature where you add files to a "project" and the agent works with them in full context. Tens of millions of users. No RAG, no embeddings. Just files in context. This isn't an MVP --- it's a [production architecture](https://elephas.app/blog/notebooklm-vs-claude-projects).

The definition is simple: all files are loaded entirely into the LLM's context window. No retrieval, no indexing. With 20 files of 200 lines each, that's ~16K tokens --- 1.6% of Claude's window.

Where this works perfectly: load 10 papers into a Claude Project --- ask questions, get synthesis with zero setup time. Prototyping --- all code < 5 files, the agent sees everything, recall and precision are both 100%. Configuration and dotfiles --- 15 infra project configs, full context, zero latency. As the [Ahoi Kapptn team writes](https://ahoikapptn.com/en/blog/from-long-prompt-to-rag-how-to-build-robust-ai-agents-with-your-knowledge-base): "If your knowledge base is < 200K tokens (~500 pages), include it entirely in the prompt."

```
my-project/
  README.md              # ← everything starts here
  src/
    main.py              # all code — 3-5 files
    utils.py
    config.yaml
  docs/
    architecture.md      # the agent sees everything at once
    api-reference.md
```

| Pattern | Anti-pattern |
|---------|-------------|
| Load all files into Claude Project | Set up a RAG pipeline for 5 documents |
| One README + a few configs | Dump 100 files into context "just in case" |
| Simple flat structure | Create a folder hierarchy for 10 files |

But one day you notice the agent starts "forgetting" information. [Research from Stanford/UC Berkeley](https://arxiv.org/abs/2307.03172) (Liu et al., 2023) demonstrated the lost-in-the-middle effect: accuracy drops by 30%+ when relevant information is in the middle of the context. A separate [study (arxiv, 2025)](https://arxiv.org/pdf/2509.21361) found that the effective context of all models turned out to be 99% smaller than advertised on complex tasks. Query costs grow linearly with context: at $3/M input tokens, 500K per request means $1.50 per call. The boundary: ~20 files / ~50K tokens. If you feel this pain --- it's time for the next tier. If not --- stay put, you're in the right place.

## Tier 1: Grep + CLAUDE.md --- How All AI Coding Tools Work

Cursor. Claude Code. Windsurf. None of them require developers to spin up a vector DB. All use grep as core infrastructure. As [BuildMVPFast writes](https://www.buildmvpfast.com/blog/ripgrep-10-years-fast-cli-tools-ai-agents-2026): "Ripgrep has quietly become the load-bearing infrastructure for how AI writes code." An agent with a 10-minute timeout can execute 500 ripgrep queries --- or 2 classic grep queries on a large codebase. That's the difference between an agent that understands your code and one that guesses.

At this tier, the project has a CLAUDE.md (or [AGENTS.md](https://agents.md/), .cursorrules) that explains the structure and conventions to the agent. The agent uses grep/ripgrep for search, reads files on demand, and navigates through the project's natural structure --- directories, imports, naming conventions.

What Tier 0 problems does this solve? At Tier 0, the agent sees everything --- but doesn't know what matters. CLAUDE.md provides priorities. Grep lets the agent read only the files it needs rather than loading all 500 into context. The directory structure itself is a navigation map. [LlamaIndex 2026 benchmarks](https://www.llamaindex.ai/blog/did-filesystem-tools-kill-vector-search) showed that filesystem agents outperform classic RAG: average correctness 8.4 vs 6.4, average relevance 9.6 vs 8.0. RAG is faster (7.36s vs 11.17s) but less accurate. At scale up to 100 documents, filesystem agents win where accuracy matters more than speed.

AGENTS.md is already [standardized](https://agents.md/) by the Linux Foundation (AAIF), supported by OpenAI, Anthropic, Google, AWS, Bloomberg, Cloudflare. Over 60,000 repositories include it. As [HumanLayer notes](https://www.humanlayer.dev/blog/writing-a-good-claude-md): "A CLAUDE.md written in 30 minutes gives the agent 80% of the context it needs." To get started --- create a CLAUDE.md or AGENTS.md and describe the architecture, key conventions, how to run, how to test. 30 minutes of work, 80% of the effect. Keep docs/ next to the code (colocation), use ADRs to record architectural decisions.

Grep objectively outperforms semantic search for exact matches. As [ast-grep notes](https://ast-grep.github.io/blog/code-search-design-space.html): `ERROR_4532` in vector space is indistinguishable from `ERROR_4533` --- yet these are completely different errors. Grep finds exactly what you need. Claude Code --- agentic grep with no pre-built index. Cursor --- embedding index + grep. Windsurf --- enterprise RAG pipeline, but starts with grep. All work out of the box at $0 infrastructure cost.

```
my-repo/
  CLAUDE.md              # ← instructions for the agent: architecture, conventions
  AGENTS.md              # standardized rules (Linux Foundation)
  src/
  tests/
  docs/
    architecture.md      # keep docs/ next to the code
    adr/
      001-use-postgres.md  # ADR for architectural decisions
```

| Pattern | Anti-pattern |
|---------|-------------|
| CLAUDE.md with architecture and conventions | Hoping the agent will "figure it out" |
| Consistent naming conventions | Different styles in different parts of the project |
| AGENTS.md + .md files per subdirectory | One giant 2,000-line CLAUDE.md |
| Grep for code and identifiers | Grep for searching concepts in prose |

You have 300 code files and grep works great. Then a task comes in: find all GDPR requirements in research notes, legal documents, and meeting transcripts. Grep for the word "GDPR" finds 5 out of 20 relevant documents --- the rest refer to "personal data", "privacy regulation", "data processing". This is the [polysemy problem](https://arxiv.org/html/2601.23254v1): one word in hundreds of contexts, dozens of synonyms for a single concept. You don't need a better search engine --- you need structured navigation. The boundary: ~500 files, predominantly code. For non-code knowledge --- PDFs, regulations, research --- the code-first model doesn't work.

## Tier 2: Docs-as-Code --- When Documentation Works for Both People and Agents

Stripe docs. Kubernetes docs (3,000+ pages). Django docs. Terraform docs. They serve millions of developers. None of them use RAG or LLM compilation. And they don't plan to. As [Mintlify notes](https://www.mintlify.com/blog/stripe-docs): "At Stripe, a feature isn't considered shipped until the documentation is written. Docs count toward promotions."

Documentation at this tier is organized by content type with formal templates, cross-references validated at build time, and navigational structure: sidebars, breadcrumbs, indexes.

Why does an agent need this? Grep across 50 markdown files finds the word "authentication" in 15 of them. But the agent doesn't know which file answers "how to set up OAuth?" vs "why we chose OAuth" vs "what to do if OAuth breaks". Without content typing, the agent is forced to read all 15 files. With the [Diataxis framework](https://diataxis.fr/) --- it goes straight to `how-to/configure-oauth.md`. Diataxis divides documentation into 4 types (tutorials, how-to, reference, explanation) and is [adopted by](https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation) Cloudflare, Ubuntu, Django, Gatsby. [Sequin Stream](https://blog.sequinstream.com/we-fixed-our-documentation-with-the-diataxis-framework/) restructured their documentation using Diataxis --- and it uncovered dozens of product improvements.

Stripe [created Markdoc](https://stripe.dev/blog/markdoc) --- their own Markdown syntax for structural validation of docs. Interactive code samples with automatically inserted API keys. Kubernetes --- 3,000+ pages, 4 content types, build-time validation of glossary terms: a broken link = a failed build. To achieve similar guarantees in your project, Docusaurus, MkDocs, or Sphinx will do --- all support auto-generated sidebars from the file structure. Numbered files (`01-intro.md`) set the order without configuration.

[AWS reports](https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/) on their experience with "200+ Architecture Decision Records" that improved team collaboration. The [ADR](https://adr.github.io/) format (Nygard, 2011) standardizes how architectural decisions are recorded: Title, Status, Context, Decision, Consequences. If decisions in your team get lost in Slack --- create an `adr/` folder and record each decision in a single markdown file.

The key advantage of this tier is the dual audience. A new team member reads the same docs as the AI agent. At Tier 3, wiki pages are also human-readable but optimized for agent navigation, not human onboarding. Here --- a single source of truth for both audiences. Documentation simultaneously serves as a developer acquisition channel: Stripe docs, Terraform docs, Django docs --- they are indexed by search engines and attract millions of developers. A wiki behind an LLM or a RAG system --- is a black box for Google.

To apply [Diataxis](https://diataxis.fr/) to existing documentation: sort your files into 4 types, add a navigational index.md. One day for an average repo.

```
docs/
  index.md                 # ← navigation hub, start here
  tutorials/
    getting-started.md     # learning material for newcomers
    deploy-first-app.md
  how-to/
    configure-auth.md      # tasks: "how to do X"
    scale-workers.md
  reference/
    api/                   # generated from code
    cli/
  explanation/
    architecture.md        # context: "why we chose X"
    security-model.md
  adr/
    001-use-postgres.md    # architectural decisions (Nygard format)
    002-event-sourcing.md
```

| Pattern | Anti-pattern |
|---------|-------------|
| Diataxis: 4 content types | A flat docs/ folder with no typing |
| Build-time link validation | Manually checking "did we break any links" |
| ADRs for architectural decisions | Decisions in Slack/email, lost within a month |
| One navigational index.md + sidebar | Every document is an island with no connections |

Authoring overhead --- that's what breaks this tier. Every document must conform to a template, have correct frontmatter, belong to the right type. At 200+ documents, classification becomes the bottleneck: "Is this a tutorial or a how-to?" --- a question requiring human judgment. No semantic discovery --- "find everything about fairness in AI" is impossible if you don't know what to search for. The boundary: ~3,000 pages with well-defined content types. It breaks on heterogeneous sources --- papers, transcripts, regulations --- that don't fit into neat templates.

## Tier 3: The Karpathy Method --- LLM as Librarian

383 files became 13 articles. 81x compression. 130 meeting transcripts became a single 244-line digest --- 503x compression. And this isn't lossy summarization: the LLM finds connections between sources that a human would miss. As [Karpathy wrote](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): "With ~100 articles and ~400K words, the LLM's ability to navigate through summaries and index files is more than sufficient."

Three-layer architecture (Andrej Karpathy, April 2026): `raw/` --- immutable sources (PDFs, transcripts, notes), append-only; `wiki/` --- LLM-generated and LLM-maintained pages; `index.md` --- catalog of all wiki pages with one-line descriptions. The index is the search mechanism: the LLM scans it, finds the right page, reads it.

Three operations: **Ingest** --- read a source, write a wiki page, update the index, update 10-15 related pages. **Query** --- find an answer by scanning the index, save good answers as new pages. **Lint** --- detect contradictions, orphan pages, outdated claims.

This is paradise for the solo researcher. One person + one LLM replaces a documentation team. Our AI-usage-lessons project --- a single maintainer manages 200+ course sources through a wiki. Lint proactively detects outdated claims and contradictions --- unlike Tier 2 docs, which go stale silently. The entire "stack" is markdown in git. `git push` = deployment. Data from [ussumant/llm-wiki-compiler](https://github.com/ussumant/llm-wiki-compiler) shows an 84% reduction in starting tokens: the agent begins a session with a compact index (~7.7K) instead of hundreds of files (~47K).

Karpathy's gist garnered [16 million views](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an) --- it struck a nerve. The DPC Messenger team discovered they had already implemented ~70% of the pattern. One user built a personal-life knowledge base from X data, Google Takeout, health exports, and AI chat histories. Full implementations have already appeared: [ussumant/llm-wiki-compiler](https://github.com/ussumant/llm-wiki-compiler) (Claude Code plugin, coverage indicators, three adoption modes), [atomicmemory/llm-wiki-compiler](https://github.com/atomicmemory/llm-wiki-compiler) (TypeScript, concept extraction, orphan detection, bidirectional links), [xoai/sage-wiki](https://github.com/xoai/sage-wiki) (Go, 5-pass pipeline, SQLite, hybrid BM25 + vector search, watch mode with 2-second debounce). As [MindStudio notes](https://www.mindstudio.ai/blog/llm-wiki-vs-rag-markdown-knowledge-base-comparison): "If your knowledge base is < 50,000--100,000 tokens, there's no technical reason to use RAG."

To get started: create `raw/` and `wiki/` directories, add a CLAUDE.md with conventions from Karpathy's gist. Don't compile everything at once --- ingest 10-20 documents per session. The wiki grows organically.

```
knowledge-base/
  CLAUDE.md                # ← schema and conventions from Karpathy's gist
  index.md                 # catalog with one-line summaries
  log.md                   # append-only operations log
  raw/                     # immutable sources
    paper-attention-2017.pdf
    meeting-2026-03-15.txt
    regulation-gdpr.md
  wiki/                    # LLM-generated markdown
    transformer-architectures.md
    gdpr-compliance.md     # ← LLM itself found the connection to 3 sources
    team-decisions-q1.md
```

| Pattern | Anti-pattern |
|---------|-------------|
| raw/ append-only, wiki/ LLM-maintained | Editing wiki by hand (breaks on recompilation) |
| One index.md with one-line descriptions | Nested indexes "for the future" with < 100 pages |
| Incremental compilation | Full recompilation of 500 sources every time |
| Lint after every Ingest | Accumulating 100 sources then compiling all at once |

You're running a research project: 200 papers, 50 meeting notes, 30 regulatory docs. The wiki handles it beautifully. Then a request comes in: "find everything related to fairness metrics." But in wiki pages the topic is called "equity measures", in source files --- "bias evaluation", in regulatory documents --- "equity assessment". The index is a precision tool: it finds what's listed. But semantic discovery is not its job. At 500+ sources, the index itself exceeds 50K tokens and no longer fits in context. The boundary: ~500 heterogeneous sources.

## Tier 4: When the Index Doesn't Fit in Context --- Add Semantics

Imagine a research library: 500 papers on a research topic, in two languages, with cross-citations. The Karpathy-method wiki compiles thematic reviews --- but when you search for "methods for evaluating model fairness", the index doesn't help: the topic is called "fairness metrics", "equity measures", "bias evaluation" --- and scattered across 15 different pages. You need semantic search that understands meaning, not word matching.

At this tier, the wiki (Tier 3) is supplemented with one or two layers. **RAG (vector search)** --- semantic search via embeddings, finds "equity measures" when you search for "fairness metrics". **Knowledge graph (ontology)** --- structured relationships: "paper X cites method Y, applied in domain Z." The wiki remains the foundation --- readable, navigable, in git. RAG and the graph are additional search layers on top of it, with results combined via [Reciprocal Rank Fusion](https://www.pinecone.io/learn/vectors-and-graphs-better-together/).

The cost isn't necessarily high. Local open-source tools make Tier 4 accessible to a single person: Oxigraph (RDF store) --- free, mcp-local-rag --- local semantic search without external services, everything lives in a single git repository. [LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) from Microsoft reduced indexing costs by 1,000x compared to classic GraphRAG. [LightRAG](https://medium.com/accelerated-analyst/lightrag-a-better-approach-to-graph-enhanced-retrieval-augmented-generation-0ac9e7bf9b74) delivers 70-90% of the quality at 1/100th the cost.

Where this works: **Research library** --- wiki compiles literature reviews, RAG finds papers by semantics, graph tracks citation chains. **Agent knowledge base** --- a single maintainer manages a course with 200+ sources: wiki for navigation, RAG for cross-lingual search, ontology for traceability "requirement -> lecture -> seminar -> assessment". **Team knowledge base** --- 3 years of working knowledge: meeting notes, design docs, post-mortems, RFCs; wiki provides topic overviews, RAG finds "that time we already solved a similar problem".

Start with RAG on top of an existing wiki --- one evening: install local-rag, ingest the wiki/ folder, test search. Add a graph only when specific relational queries appear --- "show all papers citing method X" or "which lectures cover requirement Y".

| You need RAG when | You need a knowledge graph when |
|-----------------|--------------------------|
| Cross-lingual search (RU and EN) | Multi-hop queries ("papers by author X -- method Y -- domain Z") |
| "Find something similar" (fuzzy discovery) | Traceability (requirement -- test -- coverage) |
| Wiki index > 50K tokens | Aggregation ("all papers without cited-by") |
| Heterogeneous sources | Taxonomies and classifications |

```
knowledge-base/
  CLAUDE.md
  index.md                 # wiki index (Tier 3)
  raw/                     # sources
    papers/
      by-topic/
    meeting-notes/
    regulations/
  wiki/                    # LLM-compiled pages
  index/                   # ← RAG index (embeddings), add this first
  ontology/                # knowledge graph, add when you need relationships
    schema.ttl
    store.ttl
    queries/               # SPARQL queries for common questions
```

| Pattern | Anti-pattern |
|---------|-------------|
| Wiki as foundation + RAG/graph as layers | RAG instead of wiki (you lose navigation) |
| Local free tools | Enterprise vector DB at $200/mo for 100 documents |
| Adding layers one at a time | Building all infrastructure at once "for growth" |
| Graph for specific relational queries | Graph "because it looks cool" with no clear use cases |

## How We Walked This Path: From Flat Files to Wiki + Ontology

Our AI-usage-lessons repository is a teaching course on AI with 200+ sources and a single maintainer.

We started at Tier 0: 20 files, everything in context. Quickly outgrew into Tier 1: grep over catalog/exports/. Tried RAG --- got 10% precision on Russian-language queries. Tried an ontology --- beautiful schema, zero instance data.

We implemented Tier 3 --- wiki using the Karpathy method: 7.6x reduction in tool calls, 9/9 completeness on test scenarios. Added RAG for semantic search on cross-lingual queries --- but only after the wiki was working.

The key lesson: we tried to jump from Tier 1 to Tier 4 --- and got beautifully empty infrastructure. Only when we went back to Tier 3 as the foundation and added search layers on top --- the system started working.

## Two Questions That Determine Your Tier

The entire selection framework boils down to two questions:

1. **How many sources do you have?** (< 20 / 20-500 / 500+)
2. **What is it --- code or documentation?** (code and code-adjacent docs / documentation for people / research, papers, heterogeneous sources)

| Scale \ Content | Code | Documentation for people | Research, papers, mixed |
|-------------------|-----|----------------------|--------------------------|
| < 20 files | Tier 0 | Tier 0 | Tier 0 |
| 20--500 | Tier 1 (grep + CLAUDE.md) | Tier 2 (docs-as-code) | Tier 3 (LLM wiki) |
| 500+ | Tier 1 + indexed search | Tier 2 (scales to 3,000+) | Tier 3 + Tier 4 (RAG/graph) |

Hybrid situations are the norm. "200 code files + 50 research papers" --- code at Tier 1 (grep + CLAUDE.md), papers at Tier 3 (wiki). Tiers aren't mutually exclusive; they're about content type.

The key rule: don't move to the next tier until you've experienced a specific pain point at the current one.

## Most of You Are at Tier 1. And That's Probably Right

In the world of enterprise AI, there's a popular genre: "we implemented a Knowledge Graph and got 300% ROI." But there are also reverse stories that get told less often. A developer [deleted 2,000 lines of RAG code](https://medium.com/@paulhoke/the-context-window-arms-race-what-i-learned-after-deleting-2-000-lines-of-rag-code-94bf38e5eca9) and loaded all the documentation into a single 200K-token prompt --- accuracy jumped to 94%. Entrepreneur Vamshi Reddy wrote to Karpathy: "Every business has a raw/ directory. Nobody has compiled it yet. There's the product." Karpathy agreed. We ourselves spent a sprint on a four-layer system with an ontology, SPARQL queries, and SHACL validation --- then opened the knowledge graph at a demo and discovered it was empty. Next to it sat a 40-line CLAUDE.md through which the agent had already been finding everything it needed for a week.

The right answer depends on the task. Tier 0 will always be the best for small projects --- NotebookLM serves millions of users without a single embedding. Tier 1, always --- for code. Stripe will never switch to RAG for their docs, nor should they. The Karpathy-method wiki is ideal for researchers with hundreds of heterogeneous sources. And hybrid Tier 4 is justified where the cost of unfound information is measured in lost revenue or patients.

Each tier is not a step on a ladder but the right tool for its scale. A simple rule: if you're not experiencing a specific pain point at your current tier --- you're in the right place.
