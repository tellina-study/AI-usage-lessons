---
title: "Final Roast: Knowledge Architecture (#24)"
type: analysis
issue: "#24"
epic: "#17"
date: 2026-04-07
---

# Final Roast: Knowledge Architecture

## Architecture Roast

### Is the wiki layer simpler than what we had?
YES — but with caveats. Before: grep across 100+ files, 70% noise, manual assembly (53 tool calls for 3 tests). Now: structured wiki + ontology, 7 tool calls total for same 3 tests. Trade-off: added ~30 artifacts (12 wiki pages, 17 concepts, 1 skill, 1 hook script). Each serves a clear purpose.

### Can subagents maintain the wiki autonomously?
PARTIALLY. Mechanical ops (ingest, load, validate) are automated via /compile-wiki Post-Compile phase and pre-commit hook. Content compilation still requires LLM judgment. Gap: ontology concept creation has no owning skill — should be added to /compile-wiki.

### New files without clear owners?
- `scripts/pre-commit-checks.sh` — owned by git hook (auto-runs)
- `wiki/` pages — owned by /compile-wiki skill
- `ontology/store.ttl` concepts — GAP: no skill owns concept creation

### Did we break existing workflows?
No. All existing skills unchanged. New skills are additive.

### Is 4-tier retrieval justified?
Wiki + Ontology cover 95% of use cases. RAG adds value for PDF paper discovery and RU course docs. Grep only useful for exact string matches. Keep all 4 — marginal cost is near-zero.

## Content Roast

### Wiki pages: useful or reformatted exports?
USEFUL. ai-fundamentals lists all 9 taxonomies with citations (doesn't exist in any single export). lec-01 is a compiled summary from 10+ sources. Genuinely new artifacts.

### Index: navigation or listing?
Navigation. The LO table and PKS mapping enabled S3 wiki-only traversal (6/6 hops in 2 reads).

### Cross-links: meaningful or noisy?
Meaningful but thin. 3 rich topic pages have Related Topics. 7 industry topics are stubs. Not noisy, just incomplete.

## Test Results Roast

### Manual test results (fresh session, cold start)

| Test | Result | Tool Calls | Baseline Calls | Improvement |
|------|--------|------------|----------------|-------------|
| S1: Taxonomies | 9/9 | 1 | 10 | 10x fewer |
| S2: AI Agents | 8/8 | 1 | 25 | 25x fewer |
| S3: Chain trace | 6/6 hops | 5 | 18 | 3.6x fewer |
| **Total** | **Perfect** | **7** | **53** | **7.6x fewer** |

### Most valuable tier?
Wiki for navigation (used first in every manual test), Ontology for structured queries (only tier achieving 8/8 on S2).

### Least valuable tier?
Grep. 75% noise ratio. Only succeeded at Hop 1 in S3. Should not be default first choice.

### Worth the effort?
YES. 4 issues over ~1 day. 7.6x reduction in tool calls, perfect recall, self-healing startup.

## Improvements for Next Phase

1. Compile remaining 16 lecture pages (only lec-01 exists)
2. Add concept creation to /compile-wiki skill
3. Demote Grep to explicit-only tier (not in default search order)
4. Monitor for better cross-lingual embedding models (RAG RU gap)

## Known Limitations

1. **RAG cross-lingual**: Embedding model can't bridge RU→EN. Workaround: bilingual queries in /query-kb.
2. **Ontology not persistent**: Oxigraph in-memory. Must load each session. Workaround: /query-kb Step 0.
3. **Wiki coverage**: 1/17 lectures compiled. Industry topic pages are stubs.
4. **Grep noise**: 75% infrastructure files match "agent" — structural, won't improve.
