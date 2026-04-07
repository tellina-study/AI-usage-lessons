---
title: "Test Scenario 2 Post-Compile: Cross-Document Thematic Search"
type: test-result
test_type: tool-test
issue: "#28"
epic: "#17"
date: 2026-04-07
status: post-compile
---

# Test Scenario 2: Post-Compile Tool Test

## Query
"Find everything in the repo about AI agents — definitions, architectures, frameworks, examples, and which lectures/seminars cover them."

## Ground Truth Categories (8)
1. Definitions, 2. Architectures, 3. Key papers, 4. Frameworks, 5. Course coverage, 6. Ontology, 7. Capabilities, 8. Autonomy levels

## Method Results

### Grep (broad)
Pattern: `rg "agent|агент|agentic|autonomous agent|автономн" --type md -l`
- Total files: 48
- Content files: 9 (model-chat-agent-app, history-and-definitions, classifications, 2026-updates, roast-slide-plan, roast-v2-with-feedback, us-universities-courses, russian-european-courses, online-platforms-courses)
- Noise files: 39 (subagent blueprints, reflections, test baselines, CLAUDE.md, wiki-architecture, decisions.md, etc.)
- Noise ratio: 81%
- Categories identifiable: 7/8 (definitions, architectures, key papers, frameworks, course coverage, capabilities, autonomy levels; missing: ontology)
- Tool calls: 1

### Grep (narrow)
Pattern: `rg "ReAct|Toolformer|multi-agent|мульти.агент" --type md -l`
- Files: 8 (5 content, 3 test infrastructure noise)
- Content files: model-chat-agent-app.md, classifications.md, 2026-updates.md, roast-slide-plan.md, russian-european-courses.md
- Categories: 4/8 (architectures, key papers, frameworks, course coverage)
- Tool calls: 1

### Ontology
Query 1 (agent-labeled entities): 0 results — no entities with "agent" or "агент" in rdfs:label
Query 2 (all topics): 10 topics returned — none agent-specific (ai_in_software, ai_in_finance, ai_in_medicine, ai_in_manufacturing, ai_in_government, ai_in_creative, ai_ethics, prompt_engineering, recommender_systems, expert_systems)
- Agent-related results: 0
- Total topics: 10
- Categories: 0/8
- Tool calls: 2
- Note: Ontology has no agent-related entities or topics. The current topic vocabulary does not model "AI agents" as a concept. This is unchanged from baseline — ontology schema needs agent-related topics to be useful for this query.

### RAG (English)
Query: "AI agents definitions architectures frameworks"
- Results: 10
- Relevant: 9 (all but last result about agent architecture variety was borderline but still relevant)
- Top result: [library/papers/lecture-1/masterman-2024-agent-architectures.pdf, chunk 26, score 0.179]
- Second best: [same paper, chunk 9 (keywords section), score 0.219]
- Third: [library/papers/lecture-1/wang-2023-llm-agents-survey.pdf, chunk 11, score 0.235]
- Also found: notes/research/lecture-1/classifications.md (score 0.245), notes/research/us-universities-courses.md (score 0.266)
- Categories: 5/8 (definitions, architectures, key papers, frameworks, course coverage)
- Tool calls: 1

### RAG (Russian)
Query: "AI агенты автономные системы архитектуры"
- Results: 10
- Relevant: 4 (online-platforms-courses agent mention, course plan with agent lecture, online-platforms agent career path, russian-european courses header)
- Top result: [notes/research/online-platforms-courses.md, chunk 120, score 0.126]
- Also found: catalog/exports/docs/ai-v-tsikle-sozdaniya-po.md (course plan mentioning AI agents), catalog/exports/docs/sem-01-task.md
- Categories: 2/8 (course coverage, frameworks — via course plan references to agent topics)
- Tool calls: 1

## Comparison: Baseline vs Post-Compile

| Method | Baseline Categories | Post-Compile Categories | Baseline Calls | Post-Compile Calls |
|--------|--------------------|-----------------------|----------------|-------------------|
| Grep broad | 5 | 7 | 7 | 1 |
| Grep narrow | 3 | 4 | 1 | 1 |
| Ontology | 0 | 0 | 2 | 2 |
| RAG EN | 1 | 5 | 1 | 1 |
| RAG RU | 0 | 2 | 1 | 1 |

## Key Changes

### Major improvements
1. **RAG English jumped from 1 to 5 categories.** After compile-phase ingestion of research notes and papers (masterman-2024, wang-2023), RAG now surfaces the primary agent architecture papers directly with strong relevance scores (0.18-0.28). It finds definitions, architectures, key papers, frameworks, and course coverage in a single query. This is the biggest win from the compile phase.
2. **RAG Russian improved from 0 to 2 categories.** Now finds course coverage references and some framework mentions via online-platforms and course plan documents. Still weaker than English — most research content was written in English.
3. **Grep broad improved from 5 to 7 categories** — not because grep itself changed, but because more content files now exist in the repo (model-chat-agent-app.md, 2026-updates.md, classifications.md were created during compile phase). However noise ratio remains very high at 81%.
4. **Grep broad calls dropped from 7 to 1.** In baseline, multiple iterative searches were needed; now a single broad pattern captures all relevant files.

### Unchanged
- **Ontology remains at 0/8.** The ontology schema does not model "AI agents" as a topic or entity type. Adding agent-related topics (e.g., `topic_ai_agents`, `topic_agent_architectures`) would be needed for ontology to contribute to this query.

### Conclusions
- **RAG is now the best single-query method** for thematic search after compile — 5/8 categories from one call vs grep's 7/8 but with 81% noise requiring manual filtering.
- **Combined RAG EN + RU covers 5/8 categories** in 2 calls with high precision (most results relevant).
- **Full coverage (8/8) still requires multi-method approach:** RAG for papers/definitions + grep for exhaustive file discovery + ontology (once populated) for structural relationships.
- **Ontology is the main gap** — no agent-related entities means it contributes nothing to this query type.
