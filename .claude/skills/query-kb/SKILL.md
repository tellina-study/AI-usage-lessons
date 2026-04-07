# query-kb

Search the knowledge base using 4-tier hybrid retrieval: wiki index → ontology SPARQL → RAG semantic search → grep fallback.

## Role

You are a knowledge retrieval agent. Given a user query, use the appropriate tier(s) to find the answer. Start with the cheapest tier and escalate as needed.

## Constants

- Repo root: `/home/levko/AI-usage-lessons`
- Wiki index: `wiki/index.md`
- Ontology files: `ontology/schema.ttl`, `ontology/store.ttl`
- RAG tool: `mcp__local-rag__query_documents`
- Ontology tool: `mcp__open-ontologies__onto_query`, `mcp__open-ontologies__onto_load`
- User email: `kzlevko@gmail.com`

## Tier Selection Guide

| Query Type | Start Tier | Examples |
|------------|-----------|---------|
| **Navigational** ("what lectures cover X", "find topic page for Y") | Tier 1: Wiki | "What does Lecture 1 cover?", "Find the AI ethics topic" |
| **Relational** ("what depends on X", "trace requirement to lecture") | Tier 2: Ontology | "Which LOs fulfill PKS-3?", "What seminars assess LO1?" |
| **Semantic** ("find everything about X", "papers related to Y") | Tier 3: RAG | "Papers on agent architectures", "Everything about bias" |
| **Exact** ("find file containing X", "where is string Y") | Tier 4: Grep | "Which file defines ReAct?", "Find ПКС-3 text" |
| **Cross-cutting** ("find all about X across all sources") | All tiers | "Everything about AI agents" |

## Execution Steps

### Step 0: Load Ontology (if needed)
The Oxigraph store is in-memory and may be empty at session start. Check first:
```sparql
SELECT (COUNT(*) as ?count) WHERE { ?s ?p ?o }
```
If count is 0, load both files:
1. `mcp__open-ontologies__onto_load` with file_path `/home/levko/AI-usage-lessons/ontology/schema.ttl`, format `turtle`
2. `mcp__open-ontologies__onto_load` with file_path `/home/levko/AI-usage-lessons/ontology/store.ttl`, format `turtle`

### RAG Coverage Check
Run `mcp__local-rag__status` and verify:
- documentCount >= 60 (current: 61)
- If significantly lower, wiki pages may not be ingested. Run `/compile-wiki` Post-Compile phase.

### Step 1: Tier 1 — Wiki Index Navigation (always try first)
Read `wiki/index.md`. Scan for relevant topics, lectures, LOs, or requirements.
If a topic matches, follow the link to `wiki/topics/{topic}/_index.md`.
If a lecture matches, follow to `wiki/lectures/lec-NN.md`.
Use cross-links and backlinks to navigate between pages.

**Tools:** `Read` on local markdown files
**Cost:** 1-3 file reads

### Step 2: Tier 2 — Ontology SPARQL (for relational queries)
Use when the query involves relationships: covers, fulfills, assesses, depends_on, belongs_to_topic, supports.

Common query patterns:
```sparql
# What topics does a lecture cover?
PREFIX aul: <https://ai-usage-lessons.local/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?topic ?label WHERE {
  aul:lec_01 aul:covers ?topic .
  ?topic a aul:Topic ; rdfs:label ?label .
}

# Trace requirement -> LO -> lecture -> seminar
PREFIX aul: <https://ai-usage-lessons.local/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?req ?lo ?lec ?sem ?reqL ?loL ?lecL ?semL WHERE {
  ?lo aul:fulfills ?req . ?req rdfs:label ?reqL . ?lo rdfs:label ?loL .
  ?lec aul:covers ?lo ; rdfs:label ?lecL .
  ?sem aul:assesses ?lo ; rdfs:label ?semL .
}

# What research supports a lecture?
PREFIX aul: <https://ai-usage-lessons.local/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?doc ?label ?url WHERE {
  ?doc aul:supports aul:lec_01 ; rdfs:label ?label .
  OPTIONAL { ?doc aul:source_url ?url }
}

# Find entities related to a topic
PREFIX aul: <https://ai-usage-lessons.local/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?entity ?label ?type WHERE {
  ?entity aul:belongs_to_topic ?topic ; rdfs:label ?label ; a ?type .
  ?topic rdfs:label ?topicLabel .
  FILTER(CONTAINS(LCASE(str(?topicLabel)), "agent"))
}
```

**Tools:** `mcp__open-ontologies__onto_query`
**Cost:** 1-3 SPARQL queries

### Step 3: Tier 3 — RAG Semantic Search (for discovery)
Use when looking for content by meaning, not exact terms. Good for: finding papers, discovering related content.

```
mcp__local-rag__query_documents:
  query: "your semantic query here"
  limit: 10
```

**Cross-language rule:** The embedding model does NOT support cross-lingual matching. Russian queries only find Russian content; English queries only find English content. To search effectively:
1. If the user query is in Russian, **translate key concepts to English** and run a SECOND query in English
2. Always run at least 2 RAG queries: one in each language
3. Merge results from both queries, deduplicate by file path
4. Example: user asks "найди всё про AI агентов" → run both:
   - `"AI агенты автономные системы архитектуры"` (finds Russian course docs)
   - `"AI agents definitions architectures frameworks"` (finds English research + wiki)

**Tools:** `mcp__local-rag__query_documents`
**Cost:** 2-4 queries (always bilingual)

### Step 4: Tier 4 — Grep Fallback (for exact matches)
Use when you need exact string matches: specific IDs, competency codes, technical terms.

```
Grep tool: pattern, path, type
```

**Tools:** `Grep`
**Cost:** 1-2 searches

### Step 5: Merge & Report
Combine results from all tiers used. Deduplicate. Present with provenance:
- Which tier found each result
- Confidence level (direct hit vs inferred)
- Links to source files

## Error Handling
- If ontology is empty after loading: report "Ontology load failed" and skip Tier 2
- If RAG returns 0 results: try alternative query phrasing or different language
- If a wiki page doesn't exist: note it as a gap, fall through to other tiers

## Current Coverage (2026-04-07)
- Wiki: 12 pages (10 topics, 1 lecture, 1 index)
- Ontology: 389 triples (12 topics, 17 concepts, 8 lectures, 8 LOs, 2 requirements, 4 seminars, 10 documents)
- RAG: 61 documents, 13,712 chunks (16 exports, 15 papers, 10 research notes, 12 wiki pages, 8 other)
- Grep: all repo files
