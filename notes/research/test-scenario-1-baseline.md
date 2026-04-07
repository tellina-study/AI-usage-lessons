---
title: "Test Scenario 1 Baseline: Single-Document Deep Retrieval"
type: test-result
issue: "#27"
epic: "#17"
date: 2026-04-07
status: baseline
---

# Test Scenario 1: Single-Document Deep Retrieval (Baseline)

## Query

"What specific AI classification taxonomies does the course use, and where does each come from?"

## Ground Truth

Extracted from `notes/research/lecture-1/classifications.md` (184 lines). The file documents **9 taxonomies**, each with academic sources:

| # | Taxonomy | Primary Source(s) |
|---|----------|-------------------|
| 1 | By Task Type | Russell & Norvig (2021); LeCun, Bengio & Hinton (2015) |
| 2 | By Modality | Baltrusaitis, Ahuja & Morency (2019) |
| 3 | By Learning Approach | Mitchell (1997); Sutton & Barto (2018); Balestriero et al. (2023) |
| 4 | By Capability Level (ANI/AGI/ASI) | Searle (1980); Bostrom (2014) |
| 5 | By Architecture | Vaswani et al. (2017); Ho et al. (2020); LeCun et al. (2015) |
| 6a | Generative vs. Discriminative | Ng & Jordan (2001); Goodfellow et al. (2014) |
| 6b | Foundation Models vs. Task-Specific | Bommasani et al. (2021) |
| 6c | Agentic AI Taxonomy | Masterman et al. (2024) |
| 6d | Reactive/Limited Memory/Theory of Mind/Self-Aware | Hintze (2016) |

## Method Results

### Grep

**Searches run:**
1. `rg "классификац|taxonom|taxonomy|таксоном" notes/research/lecture-1/ --type md` — 15 matches across 5 files
2. `rg "классификац|taxonom|taxonomy|таксоном" catalog/exports/docs/ --type md` — 13 matches across 5 files

**Tool calls:** 2 (grep search) + 2 (count mode for precise numbers) = 4

**Files found in research dir:**
- `classifications.md` — 6 matches (the source file itself)
- `roast-slide-plan.md` — 4 matches (mentions taxonomies in critique)
- `roast-v2-with-feedback.md` — 3 matches (mentions taxonomy in revised plan)
- `teaching-examples.md` — 1 match (image classification example)
- `human-vs-ai.md` — 1 match (mentions three-level taxonomy ANI/AGI/ASI)

**Files found in catalog/exports:**
- `ai-v-raznyh-industriyah.md` — 9 matches (course program, classification assessment criteria)
- `lec-01-plan.md` — 1 match
- `sem-05-midterm-1.md` — 1 match
- `sem-17-final-exam.md` — 1 match
- `prog-otraslevoe-primenenie-AI.md` — 1 match

**Taxonomies identifiable from grep alone: ~3/9.** Grep finds the word "taxonomy" in context lines but does not surface the structured tables or full taxonomy descriptions. From the 6 hits in `classifications.md`, you can see mentions of modality taxonomy (Baltrusaitis), multimodal classification (Bayoudh), visual foundation model taxonomy (Du & Kaelbling), agentic taxonomy (Masterman), and Hintze's four-type framework. But you cannot reconstruct the full list of 9 taxonomies or their details from grep snippets alone. Grep is best as a **pointer** — it tells you which file to read, not what the file says.

**Key observations:**
- Grep immediately identifies `classifications.md` as the primary file (highest match count in research dir)
- The keyword "taxonomy/таксоном" works well; "классификац" adds noise from assessment rubrics
- Grep cannot distinguish between a file that *defines* taxonomies vs. one that *mentions* them

### Ontology (SPARQL)

**Queries run:**
1. Filter for entities with labels containing "classif", "taxonom", or "класс" — **0 results**
2. All Topic entities — **0 results**
3. Total triple count — **0 triples**

**Tool calls:** 3

**Taxonomies identifiable: 0/9**

**Notes:** The ontology store is completely empty (0 triples loaded). The Oxigraph-based MCP server is running and responds to queries, but no ontology data has been loaded. The TTL schema exists at `ontology/` but was never ingested into the running store. This means the ontology layer is non-functional for retrieval purposes.

### RAG (Vector Search)

**Query:** "AI classification taxonomies used in the course" (limit=10)

**Tool calls:** 1 (query) + 1 (list_files to check index state) = 2

**Results returned:** 10

**Relevant results:** 0 directly relevant to the query.

Top results and their actual content:
1. Course plan chunk — "Intro, course overview..." (score 0.33) — not about taxonomies
2. Course plan table row (score 0.34) — lecture schedule, not taxonomies
3. Industry AI chunk (score 0.42) — manufacturing AI examples
4. Bibliography reference (score 0.45) — Russell & Norvig citation (tangentially relevant)
5-10. Various course admin chunks (scores 0.46-0.60) — exam criteria, seminar tasks

**Taxonomies identifiable: 0/9**

**Notes:**
- The file `notes/research/lecture-1/classifications.md` is **not indexed** in RAG at all. The RAG base directory is `catalog/exports/`, so research notes are outside its scope.
- Only 16 files from `catalog/exports/docs/` are indexed (plus 2 Google Doc direct ingestions).
- Even if the file were indexed, the chunking would likely split taxonomies across chunks, making it hard to retrieve the complete list.
- The best RAG result (score 0.33) is about course structure, not classification taxonomies — a clear semantic miss.

### Direct File Read

**File:** `notes/research/lecture-1/classifications.md`

**Tool calls:** 1

**Lines:** 184

**Taxonomies found:** All 9, with full descriptions, tables, and 25+ academic sources with DOIs.

**Notes:** One read operation returns the complete, authoritative answer. The file is well-structured with numbered sections, markdown tables, and a summary table at the end. No disambiguation needed — the file title exactly matches the query topic.

## Comparison

| Method | Taxonomies Found (/9) | Tool Calls | Precision | Key Gap |
|--------|----------------------|------------|-----------|---------|
| Grep | ~3 (partial context) | 4 | Low — finds keywords, not structure | Cannot extract structured content; best as file-finder |
| Ontology | 0 | 3 | N/A — store empty | No data loaded; infrastructure exists but unused |
| RAG | 0 | 2 | 0% — no relevant results | Source file not in index scope |
| Direct Read | 9 | 1 | 100% | Requires knowing the exact file path |

## Key Findings

1. **Direct file read is the only method that works today** — and it works perfectly, in a single tool call.
2. **Grep is useful as a file-discovery heuristic** — it correctly identifies `classifications.md` as the top-match file, but cannot extract structured knowledge from it.
3. **RAG is blind to research notes** — the index covers only `catalog/exports/`, missing the entire `notes/research/` tree where deep content lives.
4. **Ontology is non-functional** — 0 triples loaded despite schema files existing in `ontology/`.
5. **The critical bottleneck is discoverability** — if you know the file path, you get a perfect answer instantly. If you don't, no current method reliably leads you there.

## What Would Each Tier Add?

- **Tier 1 (Wiki Index):** A topic index page for "AI Classification Taxonomies" would map directly to `notes/research/lecture-1/classifications.md`. This would eliminate the discoverability gap — instead of guessing file paths or running grep, you look up the topic and get the file. **Highest impact for lowest cost.** Would take this scenario from "requires insider knowledge" to "1 lookup + 1 read = complete answer."

- **Tier 2 (Ontology):** Would allow queries like "what Topics are covered by Lecture 1?" or "what Documents cite Bostrom (2014)?". Useful for cross-referencing (e.g., "which lectures use the ANI/AGI/ASI framework?") but requires loading data first. For this specific single-document query, ontology adds less value than a wiki index — it's more useful for multi-document graph traversal (Test Scenario 2+).

- **Tier 3 (Vector Search):** Would help if the source file were indexed AND the query were semantically ambiguous. For this query, the topic is specific enough that keyword search (grep) already finds the right file. Vector search would add value for fuzzy queries like "what frameworks does the course use to explain different kinds of AI?" — but only if `notes/research/` is added to the index scope. Current RAG scope gap is a critical blind spot.

- **Tier 4 (Grep):** Already tested. Works as a file-finder but not as a knowledge extractor. Will always be available as a fallback. Most useful when combined with direct read: grep to find, read to extract.
