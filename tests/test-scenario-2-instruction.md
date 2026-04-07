# Test Scenario 2: Cross-Document Thematic Search

> Run this in a fresh Claude Code session. Follow each step exactly. Record all results.
> Issue: #28 | Epic: #17

## Query
"Find everything in the repo about AI agents -- definitions, architectures, frameworks, examples, and which lectures/seminars cover them."

## Ground Truth (8 categories)
1. **Definitions** -- model/chat/agent/app hierarchy (model-chat-agent-app.md)
2. **Architectures** -- ReAct, Toolformer, Anthropic spectrum, Ng patterns (model-chat-agent-app.md)
3. **Key papers** -- Yao 2022, Schick 2023, Wang 2023, Masterman 2024 + 5 more
4. **Industry frameworks** -- Anthropic, Google, LangChain, Andrew Ng guides
5. **Course coverage** -- which lectures/seminars mention agents
6. **Ontology** -- any agent-related topic nodes in store.ttl
7. **Capabilities** -- what agents can/can't do (human-vs-ai.md, 2026-updates.md)
8. **Levels of autonomy** -- 5 levels from arXiv:2506.12469

## Steps

### Step 1: Grep (broad)
```
rg "agent|агент|agentic|autonomous agent|автономн" --type md -l
```
Record:
- [ ] Total files matched: __
- [ ] Content files (not infra): __
- [ ] Infrastructure noise files: __
- [ ] Noise ratio: __%
- [ ] Categories identifiable from file list: __/8
- [ ] Tool calls: __

### Step 2: Grep (narrow)
```
rg "ReAct|Toolformer|multi-agent|мульти.агент" --type md -l
```
Record:
- [ ] Files matched: __
- [ ] Categories identifiable: __/8
- [ ] Tool calls: 1

### Step 3: Ontology
Run SPARQL:
```sparql
PREFIX aul: <https://ai-usage-lessons.local/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?entity ?label ?type WHERE {
  ?entity rdfs:label ?label .
  ?entity a ?type .
  FILTER(CONTAINS(LCASE(str(?label)), "agent") || CONTAINS(LCASE(str(?label)), "агент"))
}
```
Also: `SELECT ?topic ?label WHERE { ?topic a aul:Topic ; rdfs:label ?label }`

Record:
- [ ] Agent-related results: __
- [ ] Total topics in ontology: __
- [ ] Any covers/belongs_to relations for agents: yes/no
- [ ] Categories identifiable: __/8
- [ ] Tool calls: __

### Step 4: RAG (English)
Query: "AI agents definitions architectures frameworks" (limit=10)

Record:
- [ ] Results returned: __
- [ ] Relevant results: __
- [ ] Best relevance score: __
- [ ] Categories identifiable: __/8
- [ ] Tool calls: 1

### Step 5: RAG (Russian)
Query: "AI агенты автономные системы архитектуры" (limit=10)

Record:
- [ ] Results returned: __
- [ ] Relevant results: __
- [ ] Best relevance score: __
- [ ] Categories identifiable: __/8
- [ ] Tool calls: 1

### Step 6: Manual Assembly
Read these files and extract agent-related content:
1. `notes/research/lecture-1/model-chat-agent-app.md` -- primary
2. `notes/research/lecture-1/classifications.md` -- agentic taxonomy
3. `notes/research/lecture-1/human-vs-ai.md` -- capabilities
4. `notes/research/lecture-1/2026-updates.md` -- timeline
5. `notes/research/lecture-1/history-and-definitions.md` -- history
6. `catalog/exports/docs/course-structure.md` -- lecture plan
7. `catalog/exports/docs/course-narrative.md` -- narrative
8. `catalog/exports/docs/lec-01-plan.md` -- lecture 1 specifics
9. `ontology/store.ttl` -- topic entities

Record per file:
- [ ] Categories covered: __
- [ ] Key content found: __

### Step 7: Wiki Index (post-improvement only)
Read `wiki/index.md`, follow to `wiki/topics/ai-agents/_index.md` if exists.

Record:
- [ ] Topic page exists: yes/no
- [ ] Categories covered in topic page: __/8
- [ ] Tool calls: __

## Results Table

```
| Method | Categories (/8) | Files Found | Tool Calls | Precision | Noise Ratio | Notes |
|--------|-----------------|-------------|------------|-----------|-------------|-------|
| Grep broad | | | | | | |
| Grep narrow | | | | | | |
| Ontology | | | | | | |
| RAG EN | | | | | | |
| RAG RU | | | | | | |
| Manual | | | | | | |
| Wiki Index | | | | | | |
| **Total** | | | **sum** | | | |
```

## Save Results
Save as: `notes/research/test-scenario-2-{run-label}.md`

## Baseline Reference (2026-04-07)
- Grep broad: 5/8, 7 calls, 70% noise (35/50 files)
- Grep narrow: 3/8, 1 call, 0% noise
- Ontology: 0/8, 2 calls
- RAG EN: 1/8, 1 call, 10% precision
- RAG RU: 0/8, 1 call, 0% precision
- Manual: 8/8, 13 reads, 25 total calls
