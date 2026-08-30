---
id: s26
type: process
section: "Section 5. The decision framework"
duration_min: 2
assertion: "The ladder of complexity: stay on the lowest rung, climb only for a task requirement; the bottom rung is ordinary code without AI"
learning_goal: "The ladder of complexity as a tool (LO7 payoff) + the rule of movement"
learning_outcomes: [LO7]
chapter_ref: "§5.1 [for-slide-s26]"
visual_brief: "A ladder of 6 rungs (bottom-aligned, bottom-up). At each transition arrow — the requirement that opens it. A rule strip «each climb is a trade, not an improvement». Gold — the bottom rung «ordinary code (no AI)»."
interaction: none
---

# Visible content

## Title bar
«The ladder of architectural complexity»

## Body
[A ladder of 6 rungs bottom-up, bottom-aligned, Ocean rounded boxes; at each arrow — the requirement]

6. **Multi-agent** ↑ *subtasks broadly parallel AND independent AND high-value*
5. **Agent** (loop plan→act→check→iterate, with budget/loop limits) ↑ *the task is unpredictable AND the value justifies the multiplied cost/risk*
4. **Workflow** (predefined paths) ↑ *the task is multi-step, but the sequence is known in advance*
3. **RAG / context engineering** (for a small stable corpus — long context + cache) ↑ *knowledge large AND changing AND provenance AND private*
2. **A single LLM call** (prompt; + CoT, + few-shot) ↑ *NL / unstructured input / inexact matching is needed*
1. **Ordinary code (no AI)**  *(gold accent — the reference point)*

[Rule strip, bottom]
**Stay on the lowest rung that closes the requirements; climb only for an explicitly stated requirement. Each climb is a TRADE (capabilities ↔ cost, latency, auditability, attack surface), not an improvement.**

## Speaker notes

Let us gather everything we have covered into one structure — the ladder of architectural complexity[1]. Each rung is an architecture we examined. Bottom-up: ordinary code without AI; a single model call with a prompt, possibly with step-by-step reasoning and examples; RAG or context engineering, and for a small stable corpus — long context with caching; a workflow with predefined paths; an agent with a dynamic loop and mandatory limits on budget and iterations; and at the top a multi-agent.

The rule for moving along the ladder is the load-bearing rule of the whole lecture: stay on the lowest rung that closes the task's requirements; climb to the next one only for an explicitly stated requirement that the current rung does not close. Each climb is paid for with new failure modes, cost, latency, degraded auditability, and a new attack surface. "Climbed because I could" is technical debt; "climbed because here is a requirement not closed by the rung below" is an engineering decision. Note that the bottom rung is ordinary code without AI: the ladder of AI system architectures begins with "maybe AI is not needed here at all."

Let us gather exactly which requirement opens each climb — this is the transition from a ladder-picture to a ladder-tool. Code to a single call: a requirement appeared to process natural language, unstructured input, fuzzy matching, which cannot be expressed with deterministic rules. A single call to RAG: a requirement for knowledge appeared that is not in the weights and that is large, and changing, and requiring provenance, and private simultaneously. To a workflow: the task became multi-step, but the sequence of steps is known in advance. A workflow to an agent: the sequence fundamentally depends on intermediate results such that it cannot be written out in advance, and the task's value justifies the multiplied cost, latency, and loss of auditability. An agent to a multi-agent: the subtasks are broadly parallel, independent, and high-value enough that the gain of parallelism outweighs the multiplied growth of tokens and the fragility of coordination. Each arrow is not an "improvement" but a trade: more capabilities in exchange for cost, latency, auditability, attack surface. An engineer who has this skill can name both sides of the trade, not only the left one.

Sources:
[1] Anthropic — Building Effective Agents (the ladder rule) — stay on the lowest rung; each climb is a trade, not an improvement. https://www.anthropic.com/research/building-effective-agents
