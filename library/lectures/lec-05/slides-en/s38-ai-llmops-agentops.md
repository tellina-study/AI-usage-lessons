---
id: s38
type: process
section: "Section 5. Support / Operate"
duration_min: 2.5
assertion: "Tracing catches what infrastructure monitoring misses: hallucination drift, retrieval failures, prompt regressions"
learning_goal: "AI: LLMOps/AgentOps — tracing, drift monitoring, runtime guardrails, circuit breaker, data-security risk"
learning_outcomes: [LO1, LO3]
chapter_ref: "§5.2 [for-slide-s38]"
interaction: none
verify_day_of: true
partial_out_strict_in: true
meme_or_visual: >
  process: a request's path through 4 nodes (prompt→retrieval→tools→response), a small
  "surveillance camera" icon (tracing) above each node. A separate small warning card:
  "regulated PII" with a crossed-out arrow into an external cloud service.
source: "LangSmith / Langfuse / Arize Phoenix / Helicone; Gartner Market Guide for Guardian Agents (25 Feb 2026)"
---

# Visible content

## Title bar
Tracing catches hallucination drift where infrastructure monitoring stays silent

## Body
[Request path: prompt→retrieval→tools→response, a camera icon over each node]

**LLMOps/AgentOps**
- Tracing: LangSmith · Langfuse · Arize Phoenix · Helicone
- Data drift / concept drift · runtime guardrails · circuit breaker
- **Guardian Agents** (a Gartner category) — agents that watch agents

[Ocean rounded box]
Don't send regulated PII into uncontrolled external tracing without anonymization or self-hosting

## Speaker notes

An AI product in production has two properties classical software doesn't: non-determinism and the agency/control tradeoff. This is a measurable engineering problem: accuracy varies by up to fifteen percent between runs of the same prompt even at zero temperature, with a gap of up to seventy percent between the best and worst run.

Tracing is observability under the LLM stack: the full path prompt → retrieval → tool calls → final response. The main platforms: LangSmith, Langfuse, Arize Phoenix, Helicone. Their purpose is to catch what infrastructure monitoring misses: hallucination drift, retrieval failures, prompt regressions at scale. Data drift is a change in the distribution of inputs; concept drift is a change in the relationship between the input and the correct answer itself. Runtime guardrails validate inputs and outputs before the response reaches the user.

Guardian Agents is a Gartner category, the first-ever Market Guide on it, published in February 2026: agents that watch other agents. Almost seventy percent of enterprises already run AI agents in production. An honest caveat: most deployments are prototypes, mature production deployments are still few. Three operational practices are direct parallels to classical SRE: the circuit breaker as an error budget applied to live automated decisions; canary releases and rollback for model updates; human escalation as an architectural layer, not an afterthought.

A separate, often-overlooked risk: tracing and LLMOps tools, by construction, send request content to external services. Regulated personal data, medical and financial information, is a leak into an uncontrolled external boundary. The rule: don't send regulated PII without anonymizing it at the input, or without a self-hosted deployment.
