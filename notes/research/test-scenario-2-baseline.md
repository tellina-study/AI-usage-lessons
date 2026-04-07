---
title: "Test Scenario 2 Baseline: Cross-Document Thematic Search"
type: test-result
issue: "#28"
epic: "#17"
date: 2026-04-07
status: baseline
---

# Test Scenario 2: Cross-Document Thematic Search (Baseline)

## Query

"Find everything in the repo about AI agents -- definitions, architectures, frameworks, examples, and which lectures/seminars cover them. Include both Russian and English content."

## Ground Truth

All 8 expected categories are present in the repo. Here is what exists:

### 1. Definitions: model vs chat vs agent vs app hierarchy
- **Primary source:** `notes/research/lecture-1/model-chat-agent-app.md` (Section 3)
- Agent defined as: "A system that uses an LLM as its reasoning core, augmented with planning, memory, and tool use capabilities."
- Lilian Weng formulation: Agent = LLM + Memory + Planning + Tool Use
- Google Agents Whitepaper: Model + Tools + Orchestration Layer
- Four-level comparison framework (Model / Chat / Agent / App) with five axes

### 2. Architectures: ReAct, Toolformer, multi-agent
- **Primary source:** `notes/research/lecture-1/model-chat-agent-app.md` (Section 3 + Section 5)
- ReAct (Yao et al. 2022): interleave reasoning traces with actions
- Toolformer (Schick et al. 2023): LLM self-trains to decide API calls
- Anthropic's Agentic Spectrum: 5 workflow patterns (Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer)
- Andrew Ng's 4 agentic design patterns: Reflection, Tool Use, Planning, Multi-Agent Collaboration
- Google 3-component framework: Model + Tools + Orchestration Layer (ReAct, CoT, ToT)

### 3. Key papers
- Yao et al. (2022) -- ReAct -- arXiv:2210.03629
- Schick et al. (2023) -- Toolformer -- arXiv:2302.04761
- Wang et al. (2023/2025) -- LLM Agents Survey -- arXiv:2308.11432 (4500+ citations)
- Weng (2023) -- "LLM Powered Autonomous Agents" blog post
- Li et al. (2024) -- Multi-Agent Survey
- Liu et al. (2025) -- Agent Evaluation Survey -- arXiv:2503.16416
- Xinzhel et al. (2025) -- Prominent Paradigms for LLM-Based Agents -- CoLing 2025
- Levels of Autonomy Working Paper (2025) -- arXiv:2506.12469
- Masterman et al. (2024) -- Emerging AI Agent Architectures -- arXiv:2404.11584 (in classifications.md)

### 4. Industry frameworks: Anthropic, Google, LangChain guides
- Anthropic "Building Effective Agents" (Dec 2024)
- Google Agents Whitepaper (Nov 2024)
- LangChain State of AI Agents Report (2024)
- Andrew Ng Agentic Design Patterns (Mar 2024)

### 5. Course coverage: which lectures mention agents
- **Lecture 1** slide plan (`lec-01-plan.md`): "LLM, мультимодальные модели, AI-агенты" listed as key topic
- **Lecture 1** core section: Model/Chat/Agent/App taxonomy is the centerpiece (25 min)
- **Course structure** (`course-structure.md`): Lecture 1 "Введение: что такое AI и почему это важно" covers agents via interaction types
- **Course narrative** (`course-narrative.md`): agents mentioned implicitly in "AI-as-colleague" framing
- **Course plan v2** (RAG result from `ai-v-raznyh-industriyah.md`): "Будущее AI: тренды, карьера, роль инженера -- Мультимодальность, agents, reasoning models, AGI" -- appears to be a future lecture
- **Course plan v1** (`ai-v-tsikle-sozdaniya-po.md`): "coding agent workflow", "agent memory", practical agent usage in lectures 7-9
- **Seminar 1** (`sem-01-task.md`): first experience with AI tools (not agent-specific)
- **Comparable courses:** UC Berkeley LLM Agents course identified as "самый актуальный курс" in us-universities research

### 6. Ontology: any agent-related topic nodes
- **No agent-related topics exist in ontology.** The 10 Topic entities are: Expert systems, Recommender systems, Prompt engineering, AI ethics, AI in creative, AI in government, AI in manufacturing, AI in medicine, AI in finance, AI in software. None reference agents.

### 7. Capabilities: what agents can/can't do
- `model-chat-agent-app.md` Section 3 "When to Use": multi-step tasks, external tools, planning/iteration, self-reflection
- `history-and-definitions.md`: "AI agents emerge as a major paradigm" in 2025 timeline; "Gartner projects 40% of enterprise apps will embed AI agents by mid-2026"
- `2026-updates.md`: "2025: AI agents emerge -- Claude Code, Copilot Agents, Devin"; "2026: shift from chatbot era to autonomous agent era"
- `human-vs-ai.md`: 3 mentions (agents in context of capabilities comparison)

### 8. Levels of autonomy
- `model-chat-agent-app.md` Section 3 + Section 5: five levels from arXiv:2506.12469 -- Operator, Collaborator, Consultant, Approver, Observer
- Autonomy-Control Matrix: narrow/broad scope x low/high autonomy
- SAE autonomous driving analogy

## Method Results

### Grep (broad: `agent|агент|agentic|autonomous agent|автономн`)

- **Files matched:** 50 (hit the display limit)
- **Total occurrences:** 272 across 50 files
- **Relevant content files (not infrastructure):** ~15 files
  - `notes/research/lecture-1/model-chat-agent-app.md` -- 27 hits (PRIMARY)
  - `notes/research/lecture-1/history-and-definitions.md` -- 6 hits
  - `notes/research/lecture-1/2026-updates.md` -- 5 hits
  - `notes/research/lecture-1/roast-v2-with-feedback.md` -- 7 hits
  - `notes/research/lecture-1/roast-slide-plan.md` -- 4 hits
  - `notes/research/lecture-1/classifications.md` -- 1 hit
  - `notes/research/us-universities-courses.md` -- 5 hits
  - `notes/research/russian-european-courses.md` -- 2 hits
  - `notes/research/online-platforms-courses.md` -- 2 hits
  - `catalog/exports/docs/lec-01-plan.md` -- 1 hit (via separate grep)
- **Noise files (infrastructure, not content):** ~35 files
  - CLAUDE.md (12 hits) -- refers to Claude Code as "agent" in orchestration context
  - blueprint/*.md -- system architecture agents (librarian, curator, etc.)
  - .claude/agents/*.md -- Claude Code subagent definitions
  - .claude/skills/*.md -- skill definitions mentioning agents
  - notes/reflections/*.md -- session reflections about subagent usage
- **Categories identifiable from grep alone:** 5/8
  - Can identify: definitions (1), architectures (2), key papers (3), industry frameworks (4), capabilities (7)
  - Cannot identify without reading: course coverage mapping (5), ontology status (6), autonomy levels detail (8)
  - Grep finds the FILES but not the SYNTHESIS -- you still need to read and assemble
- **Tool calls:** 7 grep operations (broad, narrow, count, + 4 targeted file greps)
- **Notes:**
  - Massive false positive rate: 35/50 files are infrastructure ("agent" = Claude Code subagent), not course content about AI agents
  - The narrow search (`ReAct|Toolformer|multi-agent|мульти.агент`) found only 5 files -- much more precise but misses definitions and frameworks
  - No synonym expansion: "autonomous system" / "автономная система" would need separate queries
  - English and Russian terms both found, but mixing languages in one regex works well

### Grep (narrow: `ReAct|Toolformer|multi-agent|мульти.агент`)

- **Files matched:** 5
  - `notes/research/lecture-1/2026-updates.md`
  - `notes/research/lecture-1/roast-slide-plan.md`
  - `notes/research/lecture-1/model-chat-agent-app.md`
  - `notes/research/lecture-1/classifications.md`
  - `notes/research/russian-european-courses.md`
- **Categories identifiable:** 3/8 (architectures, key papers, comparable courses)
- **Tool calls:** 1
- **Notes:** High precision, low recall. Misses definitions, frameworks, course coverage, autonomy levels.

### Ontology (SPARQL)

- **Query 1** (filter for "agent" or "агент" in labels): **0 results**
- **Query 2** (list all topics): **0 results** (returned empty -- likely ontology not loaded in current session)
- **Manual inspection of `ontology/store.ttl`:** 10 Topic entities exist, none mention agents. Topics are industry-focused (AI in software, finance, medicine, etc.) and skill-focused (prompt engineering, AI ethics). No "AI agents" topic.
- **Categories identifiable from ontology:** 0/8
- **Tool calls:** 2 SPARQL queries
- **Notes:**
  - The ontology has NO agent-related entities at all -- no topic, no lecture-covers-topic link for agents
  - Even if the ontology were loaded, it would return nothing for this query
  - This is a structural gap: the ontology models documents and industry topics, but not AI concept topics like "agents"
  - The `covers` relation exists in the schema but has no instances linking lectures to topics

### RAG (English query: "AI agents definitions architectures frameworks")

- **Results:** 10 chunks returned
- **Relevance:**
  - 1 highly relevant: "Coding agent workflow | Agent memory настроен" (score 0.42) -- from course plan v1
  - 1 moderately relevant: "Будущее AI: agents, reasoning models, AGI" (score 0.45) -- from course plan v2
  - 2 weakly relevant: "coding agent" mentions in course plan v1 (scores 0.48-0.53)
  - 6 irrelevant: generic course content about AI classification, exams, etc. (scores 0.55+)
- **Critical miss:** The primary source (`model-chat-agent-app.md`) was NOT in the RAG index at all -- it is a local research file in `notes/`, not an exported doc in `catalog/exports/`
- **Categories identifiable from English RAG:** 1/8 (partial course coverage only)
- **Tool calls:** 1

### RAG (Russian query: "AI агенты автономные системы")

- **Results:** 10 chunks returned
- **Relevance:**
  - 0 highly relevant chunks
  - 1 weakly relevant: "AI-агенты" mention in `lec-01-plan.md` (score 0.23) -- but buried among irrelevant results
  - 9 irrelevant: prompt library, course plan fragments, seminar tasks (scores 0.19-0.31)
- **Categories identifiable from Russian RAG:** 0/8
- **Tool calls:** 1
- **Notes:** The Russian query performed worse than English. Low scores (0.19-0.31) indicate poor semantic match. The RAG index contains mostly course planning documents, not research content.

### RAG Combined Assessment

- **Categories identifiable from RAG (both queries):** 1/8 (partial course coverage)
- **Total tool calls:** 2
- **Key finding:** RAG index does not contain the primary research files (`notes/research/lecture-1/*.md`). Only `catalog/exports/` documents are ingested. This means the richest agent content in the repo is invisible to RAG.

### Manual Assembly

- **Files read:** 9 files (model-chat-agent-app.md, classifications.md, history-and-definitions.md, 2026-updates.md, roast-slide-plan.md, roast-v2-with-feedback.md, course-structure.md, course-narrative.md, ontology/store.ttl)
- **Additional grep-targeted reads:** 4 files (lec-01-plan.md, us-universities, russian-european, online-platforms -- via grep content mode)
- **Total files examined:** 13
- **Total tool calls for manual assembly:** 13 (9 reads + 4 targeted greps)
- **Categories found:** 8/8 (all categories fully populated)
- **Approximate wall-clock time:** ~5 minutes of sequential tool calls
- **Notes:** Required knowing which files to look at (from grep results) and then reading each one to extract agent-specific content. The synthesis -- connecting definitions to architectures to papers to course coverage -- was done manually by reading and cross-referencing.

## Comparison

| Method | Categories (/8) | Content Files Found | Tool Calls | Key Gap |
|--------|-----------------|---------------------|------------|---------|
| Grep (broad) | 5 | 15 relevant + 35 noise | 7 | 70% noise; finds files, not answers |
| Grep (narrow) | 3 | 5 | 1 | High precision, low recall |
| Ontology | 0 | 0 | 2 | No agent topics in ontology at all |
| RAG (EN) | 1 | 2 partial | 1 | Primary research files not indexed |
| RAG (RU) | 0 | 0 | 1 | Poor semantic match for Russian |
| Manual | 8 | 13 | 13 | Requires knowing what to look for |

**Total tool calls across all methods:** 25

## Key Findings

### What Works

1. **Grep is the only reliable discovery method** -- it found all relevant files, though with heavy noise. The broad pattern matched all content files; the narrow pattern provided precision for specific architectures.
2. **The content IS comprehensive** -- `model-chat-agent-app.md` alone contains definitions, architectures, papers, frameworks, examples, and autonomy levels. It is a well-structured 295-line research document.
3. **Cross-language grep works** -- combining English and Russian terms in one regex (`agent|агент`) catches both languages effectively.

### What Does Not Work

1. **Ontology is empty for this query** -- no agent-related Topic entities exist. The ontology models document metadata and industry topics, not AI concept topics. There are no `covers` relation instances linking lectures to topics.
2. **RAG misses the primary source** -- `notes/research/lecture-1/model-chat-agent-app.md` is not in the RAG index because only `catalog/exports/` docs are ingested. The richest content is invisible to semantic search.
3. **RAG Russian query performs poorly** -- scores indicate weak semantic matching. The index appears optimized for Russian course planning docs, not conceptual AI terminology.
4. **No method provides synthesis** -- every method returns fragments. None can answer "here is the full picture of agents across the repo" without manual reading and assembly.

### Structural Gaps Identified

1. **Research files not in RAG index:** 7 files in `notes/research/lecture-1/` totaling ~2000 lines of primary research are not searchable via RAG.
2. **No "AI agents" topic in ontology:** The topic vocabulary is industry-focused, missing concept-level topics like agents, LLMs, prompt engineering patterns, etc.
3. **No lecture-to-concept mapping:** The `covers` relation exists in the ontology schema but has zero instances. There is no way to query "which lectures cover agents?" except by reading every lecture plan.
4. **Grep noise ratio:** 70% of grep results are infrastructure files (CLAUDE.md, blueprint/, .claude/) where "agent" means "Claude Code subagent", not "AI agent as a course topic."

## What Would Each Tier Add?

- **Tier 1 (Wiki Topic Page "AI Agents"):** Would aggregate all 9+ sources into one page with sections for definitions, architectures, papers, frameworks, course coverage, and cross-links. A human asking "what do we have on agents?" would get one URL instead of 13 file reads. This is the highest-value improvement for this scenario.
- **Tier 2 (Ontology with concept topics):** Would add `topic_ai_agents` with `covers` links to Lecture 1, future lectures, and comparable courses. SPARQL query `?lecture covers topic_ai_agents` would instantly answer "which lectures cover agents?" Currently returns nothing.
- **Tier 3 (Vector/RAG with full index):** Would find `model-chat-agent-app.md` content via semantic search if research files were ingested. Would enable queries like "what architectures for autonomous AI systems exist?" to match ReAct, Toolformer without exact keyword overlap. Currently the most valuable content is outside the index.
- **Tier 4 (Grep):** Already tested. Good for exact terms, misses synonyms ("autonomous system" != "agent"), high noise for polysemous terms ("agent" = Claude subagent vs. AI agent concept). Adequate as a last resort but requires significant manual filtering and reading.
