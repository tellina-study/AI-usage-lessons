---
id: s22b
type: assertion_visual
section: "Section 4. Agents"
assertion: "An assistant agent is the loop plus five harness slots (memory, instructions, skills, subagents, access); each slot is a trade-off, not an upgrade by default"
learning_goal: "The map of the agent harness: 5 slots + the thesis «a slot = a trade-off»; a rhyme with the ladder"
learning_outcomes: [LO7]
chapter_ref: "§4.4 [for-slide-s22b]"
interaction: none
---

# Visible content

## Title bar
«What an assistant agent is made of: 5 slots»

## Body
[Five harness slots]
1. **Memory** — what the agent remembers between sessions
2. **Instruction-rules** — convention files + a task log
3. **Skills** — reusable procedures
4. **Subagents** — delegated sub-agents with their own window
5. **Access / MCP** — access to external systems

[Gold callout, bottom]
**Each slot is a trade-off between cost, complexity, and fault tolerance, not an upgrade by default.** The same logic as the ladder: do not add a slot without a requirement of the task.

## Speaker notes

So far we have talked about an agent as an abstract loop: plan, act, check, repeat. But a real assistant agent, the one an engineer works with every day, is not a bare loop but a loop plus a harness[1]. A set of additional mechanisms that determine what the agent remembers, what it follows, which procedures it can reuse, whom it can delegate work to, and which external systems it has access to. Further in this section we will repeatedly rely on data from the agent-harness-registry — an independent public registry that tests agent harnesses (memory, skills, subagents, MCP) through live-eval benchmarks on real tasks, rather than through vendor self-reports of capabilities. By its data one can distinguish five typical slots of this harness. The first is memory: what the agent remembers between sessions. The second is instruction-rules: the project's convention files and a progress log. The third is skills, reusable procedures for repeating tasks. The fourth is subagents, delegated sub-agents with their own context window. The fifth is access to external tools through MCP.

Before working through each slot separately, let us fix a thesis that rhymes with the central rule of the whole lecture and with the ladder of architectural complexity. Each harness slot is a trade-off between cost, complexity, and fault tolerance, not an upgrade by default. Exactly as one should not climb the ladder of architectures without a requirement of the task, one should not add memory, subagents, or new access to an agent just in case: each added slot carries its own cost — operational complexity, a new failure surface, a new trust boundary — and must answer a concrete, not an abstract, trigger. Next we will walk along this map slot by slot and at each check this thesis.

Sources:
[1] agent-harness-registry — the map of agent harness slots — source not confirmed by a canonical URL as of 2026-08-30; Claude Code/Cursor/Aider — vendor sites, verify day-of. [VFY: not confirmed by a canonical URL, present as data from an independent live-eval registry, not as a primary source]
