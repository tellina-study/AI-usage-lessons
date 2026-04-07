---
title: "Research: 5 Tiers of Knowledge Organization for LLM Agents"
part: 1
parts_total: 2
description: "Part 1: Tiers 0-2 (Flat files, Code-first, Structured docs) — evidence, pain points, examples"
issue: "#37"
date: 2026-04-07
type: research-note
---

# Research: 5 Tiers of Knowledge Organization for LLM Agents (Part 1)

> Part 1: Tiers 0-2. See also: [Part 2 — Tiers 3-4 + Cross-cutting](blog-article-tiers-research-part2.md)

## Thesis

There is no single "best" way to organize knowledge for LLM agents. The right approach depends on scale. This research supports a 5-tier model where each tier emerges from concrete pain points of the previous one. All tiers are valid choices — the article argues you should pick the right tool for the scale.

---

## Tier 0: Flat Files (< 20 files, everything fits in context)

### Definition

Drop all your files into the LLM's context window. No retrieval, no indexing, no structure needed. The context window IS the retrieval mechanism.

### Evidence: Context Window Sizes (2025-2026)

| Model | Context Window | Release |
|-------|---------------|---------|
| Llama 4 Scout (Meta) | 10M tokens | 2026 |
| Gemini 3 Pro (Google) | 2M tokens | 2026 |
| Grok (xAI) | 2M tokens | 2025 |
| Claude Opus/Sonnet 4.6 (Anthropic) | 1M tokens | March 2026 |
| Gemini 3.1 Pro (Google) | 1M tokens | Feb 2026 |
| Llama 4 Maverick (Meta) | 1M tokens | 2026 |
| GPT-5.4 (OpenAI) | 272K standard, 1M via API (2x pricing) | 2026 |

Sources: [Codingscape](https://codingscape.com/blog/llms-with-largest-context-windows), [Elvex](https://www.elvex.com/blog/context-length-comparison-ai-models-2026), [Morph](https://www.morphllm.com/llm-token-limit)

**Key shift:** All major platforms at paid tiers now offer 1M+ tokens. 1M tokens is roughly 750K words or ~3,000 pages of text. For a project with 20 files averaging 200 lines each, that's ~4,000 lines = ~16K tokens. Easily fits.

### When Tier 0 Works

- Personal projects with < 20 source files
- Small config repos, dotfile collections
- Single-topic research with a handful of papers
- Prototypes and POCs where the entire codebase is < 50K tokens
- Karpathy himself notes: "At ~100 articles and ~400K words, the LLM's ability to navigate via summaries and index files is more than sufficient" — implying that at much smaller scale, even indexes are unnecessary

Source: [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

### Pain Points (Why Tier 0 Breaks)

**1. Lost-in-the-Middle Effect**

Stanford/UC Berkeley research (2023, confirmed 2025) showed LLMs attend poorly to information in the middle of context. Performance degrades by 30%+ when relevant information is in the middle vs. beginning/end. MIT researchers (2025) identified the architectural cause: causal masking means earlier tokens accumulate more attention weight.

Sources: [Liu et al. 2023](https://arxiv.org/abs/2307.03172), [Towards AI](https://pub.towardsai.net/why-language-models-are-lost-in-the-middle-629b20d86152)

**2. Effective Context < Advertised Context**

Research shows "all models fell short of their advertised Maximum Context Window by more than 99% in some cases" for complex tasks. A model handling simple retrieval at 5K tokens may fail at complex reasoning at 400-1,200 tokens.

Source: [arxiv 2509.21361](https://arxiv.org/pdf/2509.21361)

**3. Cost Scales Linearly with Context**

At $3/M input tokens (Claude Sonnet 4.6), stuffing 500K tokens into every query costs $1.50 per query. With 100 queries/day that's $150/day. RAG that retrieves only relevant chunks costs a fraction.

**4. No Persistence Between Sessions**

Flat files in context have no memory. Every session starts from scratch. No accumulated knowledge, no incremental refinement.

### Threshold

Tier 0 works well up to ~20 files / ~50K tokens of total content. Beyond that, the lost-in-the-middle effect, cost, and lack of navigational structure make it unreliable.

---

## Tier 1: Code-First (grep + CLAUDE.md / .cursorrules)

### Definition

The project has a CLAUDE.md (or equivalent) file that tells the LLM about the codebase structure, conventions, and architecture. The LLM uses grep/ripgrep to search for specific code, reads files on demand, and navigates via the project's natural structure (directory layout, imports, naming conventions).

### How AI Coding Tools Actually Work (2026)

**Claude Code — Agentic Search (no index):**
Executes grep, glob, and file reads iteratively at runtime. Each search result informs the next query. No pre-built index, no embedding pipeline. The model decides what to search based on the task. Effective context: ~150K+ tokens, read on demand.

Source: [Morph — Codebase Indexing](https://www.morphllm.com/codebase-indexing)

**Cursor — Embedding-Based Indexing:**
Scans projects, computes Merkle trees of file hashes, uses tree-sitter for AST-aware chunking, generates vector embeddings per chunk, stores in Turbopuffer. Re-syncs every ~5 minutes. Effective code context: ~60-80K tokens.

**Windsurf — Enterprise RAG Pipeline:**
Pre-computes code snippet indexes, retrieves relevant context during generation. Reads files on demand following import chains. Effective context: ~50-70K tokens.

**GitHub Copilot — Embedding index (Copilot Enterprise):**
Similar to Cursor's approach but less documented publicly.

Source: [DEV.to — Cursor vs Windsurf vs Claude Code 2026](https://dev.to/pockit_tools/cursor-vs-windsurf-vs-claude-code-in-2026-the-honest-comparison-after-using-all-three-3gof)

### Agent Config Files Comparison (2026)

| File | Creator | Supported By | Scoping |
|------|---------|-------------|---------|
| CLAUDE.md | Anthropic | Claude Code | Directory hierarchy (global -> project -> subdir) |
| AGENTS.md | OpenAI/Codex CLI, now Linux Foundation | 60K+ repos; Codex, Cursor, Claude Code, Gemini CLI, Windsurf, Aider, Zed, Warp | Directory hierarchy + override files |
| .cursorrules | Cursor | Cursor (legacy, deprecated) | Single file, project root |
| .cursor/rules/*.mdc | Cursor | Cursor (current) | Glob patterns, alwaysApply flags, scoped activation |
| copilot-instructions.md | GitHub | GitHub Copilot | .github/ directory, glob patterns in frontmatter |
| GEMINI.md | Google | Gemini CLI | Directory hierarchy with dynamic discovery |

Sources: [DeployHQ](https://www.deployhq.com/blog/ai-coding-config-files-guide), [AgentRuleGen](https://www.agentrulegen.com/guides/cursorrules-vs-claude-md), [Medium — Agent Memory Files](https://medium.com/data-science-collective/the-complete-guide-to-ai-agent-memory-files-claude-md-agents-md-and-beyond-49ea0df5c5a9)

**Key finding:** AGENTS.md has won the standardization race. In December 2025, the Linux Foundation placed it under the Agentic AI Foundation (AAIF) alongside MCP and Goose. Members include OpenAI, Anthropic, Google, AWS, Bloomberg, Cloudflare. Over 60K open-source repos already include an AGENTS.md.

Source: [AGENTS.md specification](https://agents.md/)

### Real Examples of Good Agent-Friendly Repos

- **wshobson/agents** — 182 specialized AI agents, 16 orchestrators, 147 skills, 95 commands organized into 75 plugins for Claude Code
- **shanraisshan/claude-code-best-practice** — detailed guidance on structuring CLAUDE.md, agents, commands, skills
- **awesome-claude-code** (hesreallyhim) — curated list including agnix linter that validates CLAUDE.md, AGENTS.md, SKILL.md
- **Matthew Groff's guide** — Why/What/How/Progressive Disclosure structure for agent documentation

Sources: [HumanLayer](https://www.humanlayer.dev/blog/writing-a-good-claude-md), [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)

### Pain Points (Why Tier 1 Breaks)

**1. Grep Polysemy / Terminology Mismatch**

"If developers use different names than the specification, text-based searches won't find relevant code." Grep carries limitations where "if you're looking for deeply-buried critical business logic, you cannot describe it — you have to accurately guess what naming patterns would have been used." The keyword `init` appears in hundreds of files with different meanings.

Sources: [ast-grep blog](https://ast-grep.github.io/blog/code-search-design-space.html), [GrepRAG paper](https://arxiv.org/html/2601.23254v1)

**2. Context Fragmentation**

"Grep only returns the matching line, and even with surrounding lines via -C, it may not be sufficient to understand the entire function or class." Cross-file reasoning requires understanding import chains, type hierarchies, and call graphs that grep cannot reconstruct.

**3. Scale: When Ripgrep Meets Its Limit**

Ripgrep handles 1.4GB monorepos (250K files) in under 1 second for simple pattern matching. But Cursor's indexed search beats ripgrep at ~500K-1M files: 0.013s indexed vs 15s for ripgrep. At this scale, you need semantic indexing.

Source: [burntsushi ripgrep benchmarks](https://burntsushi.net/ripgrep/)

**4. Non-Code Knowledge Doesn't Fit**

CLAUDE.md works for code conventions, architecture decisions, and build instructions. But research papers, regulatory documents, course materials, customer feedback — these aren't code. Grep over PDFs and Google Docs doesn't work. You need a different organizational paradigm.

### Threshold

Tier 1 works well for typical software repos up to ~500 files where the knowledge is mostly code and the team shares naming conventions. Breaks down for non-code knowledge bases, cross-domain projects, and repos where the same concept has multiple names.

---

## Tier 2: Structured Docs (docs-as-code, ADR, navigational README)

### Definition

Documentation organized by content type with formal templates, cross-references validated at build time, and navigational structure (sidebars, indexes, breadcrumbs). The knowledge isn't just "files in a folder" — it has taxonomy.

### Diataxis Framework

The Diataxis framework (created by Daniele Procida) divides documentation into 4 types along two axes:

|  | Practical (doing) | Theoretical (understanding) |
|---|---|---|
| **Learning** | Tutorials (learning-oriented) | Explanation (understanding-oriented) |
| **Working** | How-to guides (task-oriented) | Reference (information-oriented) |

**Key insight:** "The engineer's impulse is to explain everything upfront" but users only truly understand after hands-on interaction. Sequin Stream's experience: they rebuilt docs with Diataxis, reduced quickstart to a single outcome (~3 minutes), and found that writing how-to guides "forced them to think through real user scenarios" and "surfaced dozens of product improvements."

Sources: [Diataxis.fr](https://diataxis.fr/), [Sequin blog](https://blog.sequinstream.com/we-fixed-our-documentation-with-the-diataxis-framework/)

**Who uses Diataxis:** Gatsby, Cloudflare, Ubuntu/Canonical, Django, OCaml community.

### Architecture Decision Records (ADRs)

Format originated with Michael Nygard (2011): Title, Status, Context, Decision, Consequences.

**Templates:** Nygardian (original 5-section), MADR (Markdown ADR with options considered), Y-Statements (one-sentence format).

**Tools:** adr-tools (CLI), Log4brains (static site generator), ADR Manager (web-based), Backstage plugin.

**Best practice:** AWS reports experience with "over 200 ADRs across multiple projects" improving team collaboration and decision-making.

Sources: [adr.github.io](https://adr.github.io/), [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/), [Nygard original](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

### Real Examples at Scale

**Kubernetes docs (3000+ pages, Hugo):**
- 4 content types: concept, task, tutorial, reference
- Archetypes enforce required sections (Prerequisites, Steps, Verification for tasks)
- Cross-references via validated shortcodes: `glossary_tooltip term_id="cluster"` — invalid term_id halts build
- Build time: ~3 minutes for 3000+ pages
- Versioning: entire doc tree duplicated per version = 5000+ files for 10 versions

Source: [Kubernetes content guide](https://kubernetes.io/docs/contribute/style/content-guide/)

**Stripe docs (Markdoc):**
- Built Markdoc — a custom Markdown-based syntax for interactive docs
- "A feature isn't shipped until its documentation is written" — docs count toward promotions
- Interactive code examples with user's test API keys auto-inserted
- Language switching across all code samples (Python, Node, Ruby, Go)

Sources: [Stripe blog on Markdoc](https://stripe.dev/blog/markdoc), [Mintlify analysis](https://www.mintlify.com/blog/stripe-docs)

**Docusaurus sidebar auto-generation:**
- Number-prefixed files: `01-intro.md` -> position 1, slug "intro"
- `_category_.json` per directory for metadata
- Convention-over-configuration: sidebar mirrors filesystem

### Pain Points (Why Tier 2 Breaks)

**1. Authoring Overhead**

Every document must fit a template, have correct frontmatter, belong to the right content type. For a team producing 100+ documents per month, this becomes a bottleneck. The Kubernetes contributor guide is itself a significant documentation project.

**2. No Semantic Discovery**

Structured docs solve navigation ("where is the tutorial for X?") but not discovery ("find me everything related to fairness in AI"). You can only find what you know to look for. Cross-references are explicit and manual — implicit connections between concepts are invisible.

**3. Stale Cross-References at Scale**

Build-time validation catches broken links but cannot detect conceptually stale references. A tutorial linking to a deprecated API reference will pass validation if the reference page still exists, even if the content is outdated.

**4. Human Bottleneck for Structure Decisions**

"Does this belong in tutorials or how-to guides?" requires human judgment. With hundreds of documents, classification disagreements multiply. PARA reclassification becomes a bottleneck past ~200 items.

**5. LLM Navigation Limitations**

An LLM can navigate a 3000-page Kubernetes-style doc site — but only if it has an index or sitemap in context. Without it, the LLM has to grep through thousands of files, which circles back to Tier 1 limitations.

### Threshold

Tier 2 works well for product documentation, API references, and team knowledge bases up to ~3000 pages where content types are well-defined. Breaks down when you have hundreds of heterogeneous sources (papers, transcripts, regulations, notes) that don't fit neat templates, or when you need semantic discovery across topics.

---

> Continue to [Part 2 — Tiers 3-4 + Cross-cutting findings](blog-article-tiers-research-part2.md)
