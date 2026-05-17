---
title: "AI Agents"
type: topic-index
sources_count: 30
sub_topics: [definitions, architectures, frameworks, autonomy-levels, capabilities]
lectures: [3, 1]
coverage: high
updated_at: 2026-05-16
---

# AI Agents

## Overview
AI agent architectures, definitions, frameworks, and autonomy levels. Primary lecture: **Lecture 3 "Архитектуры AI-систем: агенты, RAG, API"** (produced) — dedicated lecture covering the agent loop (plan → act → check → iterate), RAG, fine-tuning vs prompting, API access, and MCP / tool use. Lecture 1 introduces agents only as a brief landscape mention in the model/chat/agent/app hierarchy.

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

### Capabilities and Limitations
- Planning: decomposing complex tasks into steps (Ng 2024)
- Tool Use: API calls, web browsing, code execution (Schick 2023)
- Memory: short-term (context window) and long-term (RAG, vector stores)
- Multi-Agent Collaboration: specialized agents working together (Li et al. 2024)
- Limitations: hallucination in tool calls, lack of causal reasoning, prompt sensitivity
- Primary: [human-vs-ai.md](../../../notes/research/lecture-1/human-vs-ai.md), [2026-updates.md](../../../notes/research/lecture-1/2026-updates.md)

## Key Papers (downloaded)
- [yao-2022-react.pdf](../../../library/papers/lecture-1/yao-2022-react.pdf)
- [schick-2023-toolformer.pdf](../../../library/papers/lecture-1/schick-2023-toolformer.pdf)
- [wang-2023-llm-agents-survey.pdf](../../../library/papers/lecture-1/wang-2023-llm-agents-survey.pdf)
- [masterman-2024-agent-architectures.pdf](../../../library/papers/lecture-1/masterman-2024-agent-architectures.pdf)

## Lectures
- [Lecture 3](../../lectures/lec-03.md) -- primary lecture: agents, RAG, API, MCP / tool use (produced)
- [Lecture 1](../../lectures/lec-01.md) -- brief overview mention as part of AI landscape

## Related Topics
- [AI Fundamentals](../ai-fundamentals/_index.md) -- agents are a classification category in the taxonomy
- [AI in Software](../ai-in-software/_index.md) -- coding agents (Claude Code, Devin, Copilot)
- [Prompt Engineering](../prompt-engineering/_index.md) -- prompt design for agent orchestration

## Backlinks
- [Lecture 1](../../lectures/lec-01.md) -- model/chat/agent/app hierarchy overview
- [AI Fundamentals](../ai-fundamentals/_index.md) -- agentic AI as classification taxonomy #8
- [wiki/index.md](../../index.md) -- topic listing
