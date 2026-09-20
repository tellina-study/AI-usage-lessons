---
id: s-agent-frameworks
type: comparison_table
section: "Section 4. Agents"
duration_min: 2.5
assertion: "An agent framework is an abstraction tax; every framework shares five drawbacks (customization / transparency / lock-in / version churn / overhead). LangGraph / CrewAI / AG2 / OpenAI Agents SDK / Claude Agent SDK / smolagents / LlamaIndex / Pydantic AI — and \"none: plain code\""
learning_goal: "Survey of agent frameworks on a stable schema — core abstraction · what it's for · one drawback + five shared drawbacks (§4.3c)"
learning_outcomes: [LO7, LO4]
chapter_ref: "§4.3c [for-slide-agent-frameworks-cons, agent-frameworks-intro, agent-frameworks-list, agent-frameworks-none]"
subtype: comparison_table
new_in_v4: "#196 WAVE 3 — agent frameworks"
changed_in_v6d2: "#196 WAVE D2 owner #15 — ADD five shared drawbacks of ALL frameworks as a panel above the table"
---

# Visible content

## Title bar
«An agent framework is an abstraction tax; all of them share five drawbacks»

## Body
[Panel — 5 drawbacks shared by ALL frameworks]
Customization — debt beyond the "happy path" · Transparency — hides prompts and control flow · Lock-in — vendor SDKs tie you to their ecosystem · Version churn — breaking API changes · Overhead — CrewAI +18% tokens vs LangGraph.

[Table: framework · core abstraction · what it fits · one honest drawback]
LangGraph (stateful graph) · CrewAI (role-based crews) · AutoGen → AG2 · OpenAI Agents SDK (handoffs) · Claude Agent SDK · smolagents · LlamaIndex · Pydantic AI · and "NONE — plain code".

[Gold] The five drawbacks apply to EVERY row; a deterministic path → plain code, no framework.

## Speaker notes

The engineer has decided an agent is justified — now the question is what to build it on. A frame-level thesis holds the whole slide: Anthropic's "Building Effective Agents" writes that many patterns can be implemented in a few lines of direct API calls[1], and frameworks add layers of abstraction that hide the underlying prompts and responses and make debugging harder. A framework is an abstraction tax; you pay it only when it demonstrably improves the outcome, not by default. So first — the five drawbacks common to every framework, because marketing stays silent about them, and that is exactly the judgment content of this slide.

The first is a limit on behavior customization. A highly abstract framework accrues technical debt right at the moment you need to go past the "happy path": override a built-in prompt, change the control flow. The second is transparency and debuggability: a framework hides the actual prompts and control flow, and debugging a stuck agent in a five-agent pipeline becomes painful. The third is lock-in: vendor SDKs tie you to a single model ecosystem, and portability costs a rewrite. The fourth is version churn: the LangChain ecosystem has had too many breaking API changes across its history, and an upgrade breaks working code. The fifth is overhead: a benchmark found that a three-agent "crew" on CrewAI spent roughly 18% more tokens than an equivalent build on LangGraph — abstraction is not free at runtime either.

Now, by the stable schema "core abstraction, what it fits, one honest drawback." LangGraph is a stateful graph[2], for production with control over flow and state; the drawback — a steep learning curve, over-engineering for a single loop. CrewAI is role-based crews, for fast prototyping; the drawback — the "role" masks what is actually happening. AutoGen turned into AG2 and Microsoft Agent Framework — this is exactly version churn and rename churn, a risk at adoption time. OpenAI Agents SDK — handoffs, but OpenAI-centric. Claude Agent SDK — the same loop that powers Claude Code, for coding and computer-use; the drawback — a heavy harness versus the bare API. smolagents — code agents, the drawback — code execution is an attack surface. LlamaIndex — an agent on top of a RAG stack. Pydantic AI — a type-safe loop. And the bottom row is not there for completeness: a deterministic path plus known steps plus cost sensitivity is plain code, without an agent and without a framework. The five drawbacks above apply to every row: the tooling complexity is paid for by the demands of the task, not taken on in advance.

Sources:
[1] Anthropic — Building Effective Agents (framework = abstraction tax) — many patterns are a few lines of direct API calls; frameworks hide prompts and make debugging harder. https://www.anthropic.com/research/building-effective-agents
[2] LangGraph (LangChain) — stateful graph, production orchestration — framework versions are volatile in 2026 (rename churn) — verify day-of. https://github.com/langchain-ai/langgraph [VFY-day-of]
