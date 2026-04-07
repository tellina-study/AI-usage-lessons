---
title: "Test Scenario 2 E2E Baseline: Fresh Session, Query Only"
type: test-result
test_type: e2e
issue: "#28"
epic: "#17"
date: 2026-04-07
status: baseline
session_id: "e1ce8841-b4a8-491e-bf1b-5d9996749b18"
---

# Test Scenario 2: E2E Baseline (Fresh Claude Code Session)

## Setup
- Fresh Claude Code session, no prior context
- User input: "Find everything in the repo about AI agents -- definitions, architectures, frameworks, examples, and which lectures/seminars cover them."
- No instructions given, no file paths hinted
- Model: claude-opus-4-6, CLI entrypoint

## What the System Did
1. Spawned 1 Explore subagent with broad search prompt
2. Subagent performed 34 tool calls (grep, glob, read across repo)
3. Compiled comprehensive structured report
4. Main agent formatted final answer with summary tables

## Metrics

| Metric | Value |
|--------|-------|
| Ground truth categories found (/8) | 8/8 |
| Total tool calls (inner subagent) | 34 |
| Total tool calls (outer) | 1 (Agent spawn) |
| Wall-clock time | 87.9 seconds |
| Total tokens consumed | 151,071 |
| Primary source file found | Yes (model-chat-agent-app.md) |
| Additional source files found | 6+ (classifications.md, 2026-updates.md, course-structure.md, lec-01-plan.md, blueprint/agents/, CLAUDE.md) |
| Precision | ~95% (minor noise from internal agent infra docs) |
| Recall (vs 8 categories) | 100% |
| Answer quality | Structured with tables, paper citations, file paths |
| User effort | 1 query, no follow-up needed |

## Categories Found

| # | Category | Found | Source File(s) |
|---|----------|-------|---------------|
| 1 | Definitions (model/chat/agent/app) | Yes | model-chat-agent-app.md |
| 2 | Architectures (ReAct, Anthropic spectrum, Ng patterns) | Yes | model-chat-agent-app.md |
| 3 | Key papers (Yao, Schick, Wang, Masterman + 4 more) | Yes | model-chat-agent-app.md, classifications.md |
| 4 | Industry frameworks (Anthropic, Google, LangChain) | Yes | model-chat-agent-app.md |
| 5 | Course coverage (lectures/seminars) | Yes | lec-01-plan.md, 2026-updates.md |
| 6 | Ontology topic nodes | Noted as absent | ontology/store.ttl checked |
| 7 | Capabilities (what agents can/can't do) | Yes | model-chat-agent-app.md, 2026-updates.md |
| 8 | Levels of autonomy | Yes | model-chat-agent-app.md (L1-L5) |

## Bonus Findings (beyond ground truth)
- Internal agent architecture of this repo (5 subagents, 211 MCP tools)
- Practical lessons from notes/reflections/subagents-and-delegation.md
- MCP (Model Context Protocol) as emerging agent standard
- Framework comparison table (Claude Code, Devin, AutoGPT, CrewAI, LangGraph, etc.)
- Key gap identified: no dedicated lecture on agents in 17-lecture structure

## Methods Used by Subagent (inferred from 34 tool calls)
- Grep across repo with agent/agentic keywords
- Glob for file discovery
- Read of 6+ content files and ontology store
- Read of blueprint and CLAUDE.md (internal architecture)
- No ontology SPARQL queries attempted
- No RAG queries attempted

## Comparison with Tool Test Baseline

| Metric | E2E (fresh session) | Tool Test (subagent baseline) |
|--------|---------------------|-------------------------------|
| Categories found | 8/8 + bonus | 8/8 (manual assembly only) |
| Tool calls | 34 + 1 = 35 | 25 (across 5 methods) |
| Time | 87.9s | not timed |
| Tokens | 151,071 | not tracked |
| Used ontology | No (checked store, noted gap) | Yes (returned 0) |
| Used RAG | No | Yes (1 relevant EN, 0 RU) |
| Used grep | Yes (via Explore) | Yes (5/8 broad, 3/8 narrow) |
| Noise from infra files | Low (~5%) | High (70% with broad grep) |
| Synthesis quality | Full answer with tables | Per-method breakdown, no synthesis |

## Key Observations
1. Fresh session found ALL 8 categories without any guidance -- brute-force search works
2. Correctly identified "no dedicated agents lecture" as a gap -- useful meta-finding
3. Included internal repo agent architecture as bonus context (relevant to query)
4. 34 tool calls and 88s is expensive but comprehensive
5. Skipped ontology/RAG entirely -- went straight to grep+read via Explore
6. Noise was much lower than tool test's broad grep (Explore agent filtered intelligently)
7. The system compensates for missing wiki/index by reading many files and synthesizing
