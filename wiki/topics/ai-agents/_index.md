---
title: "AI Agents"
type: topic-index
sources_count: 30
sub_topics: [definitions, architectures, frameworks, autonomy-levels]
lectures: [1]
coverage: high
updated_at: 2026-04-07
---

# AI Agents

## Overview
AI agent architectures, definitions, frameworks, and autonomy levels. Covered as part of Lecture 1's landscape overview. No dedicated lecture exists yet.

## Sub-topics

### Definitions
- Agent = LLM + Memory + Planning + Tool Use (Lilian Weng 2023)
- Google: Model + Tools + Orchestration Layer
- Model vs Chat vs Agent vs App comparison framework
- Primary: [model-chat-agent-app.md](../../../notes/research/lecture-1/model-chat-agent-app.md)

### Architectures
- ReAct (Yao et al. 2022) -- interleave reasoning + actions
- Toolformer (Schick et al. 2023) -- self-taught tool use
- Anthropic's 5-pattern spectrum (prompt chaining -> evaluator-optimizer)
- Andrew Ng's 4 agentic patterns (reflection, tool use, planning, multi-agent)

### Frameworks and Products
- Claude Code, Devin, AutoGPT, CrewAI, LangGraph, OpenAI Assistants, Manus
- Anthropic "Building Effective Agents" (Dec 2024)
- Google Agents Whitepaper (Nov 2024)
- LangChain State of AI Agents (2024)

### Autonomy Levels (arXiv:2506.12469)
- L1 Operator -> L2 Collaborator -> L3 Consultant -> L4 Approver -> L5 Observer

## Key Papers (downloaded)
- [yao-2022-react.pdf](../../../library/papers/lecture-1/yao-2022-react.pdf)
- [schick-2023-toolformer.pdf](../../../library/papers/lecture-1/schick-2023-toolformer.pdf)
- [wang-2023-llm-agents-survey.pdf](../../../library/papers/lecture-1/wang-2023-llm-agents-survey.pdf)
- [masterman-2024-agent-architectures.pdf](../../../library/papers/lecture-1/masterman-2024-agent-architectures.pdf)

## Lectures
- [Lecture 1](../../lectures/lec-01.md) -- overview as part of AI landscape

## Gap
No dedicated lecture on agents in 17-lecture structure. Consider adding or expanding Lecture 1 coverage.

## Related Topics
- [AI Fundamentals](../ai-fundamentals/_index.md) -- agents are a classification category in the taxonomy
- [AI in Software](../ai-in-software/_index.md) -- coding agents (Claude Code, Devin, Copilot)
- [Prompt Engineering](../prompt-engineering/_index.md) -- prompt design for agent orchestration

## Backlinks
- [Lecture 1](../../lectures/lec-01.md) -- model/chat/agent/app hierarchy overview
- [AI Fundamentals](../ai-fundamentals/_index.md) -- agentic AI as classification taxonomy #8
- [wiki/index.md](../../index.md) -- topic listing
