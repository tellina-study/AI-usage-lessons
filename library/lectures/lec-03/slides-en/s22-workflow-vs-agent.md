---
id: s22
type: comparison
section: "Section 4. Agents"
duration_min: 2.5
assertion: "A predictable task → workflow; unpredictable AND the value justifies a multiple increase in cost → agent; workflow and agent nest inside each other — the question is not about the whole system but about a specific place in it"
learning_goal: "Workflow vs Agent (LO7) — an operational distinction + the trade-off + nesting"
learning_outcomes: [LO7]
chapter_ref: "§4.3 [for-slide-s22]"
visual_brief: "2 equal columns: Workflow vs Agent. A diagnostic-question bar. Multi-agent debate — 1 line. Gold — the phrase «find the simplest»."
interaction: none
---

# Visible content

## Title bar
«Workflow vs Agent»

## Body
[2 equal columns in an Ocean rounded box, parallel structure]

**Workflow**
the LLM and tools are orchestrated along **paths predefined in code**
- the sequence of steps is known in advance
- predictable, auditable
- most reliable production systems are workflows

**Agent**
the LLM **dynamically** determines its own process
- the sequence is not fixed in advance
- many times more tokens than a chat
- lower auditability, higher risk of loops

[Diagnostic question — bar, center]
**Can I, in advance, before the run, write out the sequence of steps?**
yes (even with branching) → **workflow** · fundamentally no AND the value justifies the multiple cost/risk → **agent**

[Gold callout, bottom]
**Find the simplest solution. "Too lazy to formalize" does not make a task unpredictable.**

[Sub-caption, 12pt italic]
*The debate about multi-agents (Cognition «Don't Build Multi-Agents» vs Anthropic) — in the chapter. By default, multi-agent is not an upgrade.*

## Speaker notes

Before working through how agents break, we need to introduce a distinction that is, for the lecture's main learning goal, one of the most important. Anthropic in "Building Effective Agents" separates two concepts[1] that in everyday use are often conflated. A workflow is a system where the model and tools are orchestrated along paths predefined in code; the sequence of steps is known in advance and hardcoded, the model is called at specific steps but does not decide which steps to do and in what order. An agent is a system where the model dynamically determines its own process; the sequence is not fixed in advance.

The distinction is operational and gives a direct choice criterion. The task is predictable, the sequence is known — workflow. Unpredictable, the sequence depends on intermediate results, and the value justifies a multiple increase in cost — agent. Anthropic states the trade-off directly: agentic systems trade latency and cost for quality. Let us translate the criterion into one practical question: can I, in advance, before the run, write out the sequence of steps? If yes, even with known branches — it is a workflow. If the sequence fundamentally depends on intermediate results, and the value justifies the increase in risk — an agent. "Too lazy to formalize" does not make a task unpredictable. This is perhaps the industry's most expensive mistake: building a dynamic agent where a workflow would have sufficed.

An important note: the boundary runs not only along the task as a whole but also along what happens inside a specific step — workflow and agent nest inside each other, and this is the norm. An agent at the action step can call a whole workflow as a single tool: a code review agent itself decides what to check, but calls the step "linter, tests, formatting" as a single deterministic subprocess. And vice versa: a claims-processing workflow routes along fixed rules, but delegates the step "figure out a free-form complaint" to a mini-agent. This is not a third architecture but the recognition that the question "workflow or agent" is about a specific place in the system: dynamism is added only where it is needed. The full debate about multi-agents[2] stays in the chapter; in the narrative it is enough: multi-agent by default is not an upgrade.

Sources:
[1] Anthropic — Building Effective Agents (workflow vs agent) — workflow = predefined paths; agent = a dynamic process; the trade-off latency/cost↔quality. https://www.anthropic.com/research/building-effective-agents
[2] Cognition — Don't Build Multi-Agents — multi-agent by default is not an upgrade; the fragility of parallel subagents. https://cognition.ai/blog/dont-build-multi-agents
