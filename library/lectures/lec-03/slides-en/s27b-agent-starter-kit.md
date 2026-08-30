---
id: s27b
type: assertion_visual
section: "Section 5. The decision framework"
assertion: "The agent starter kit is a thin default (one instruction file + flat memory, no subagents, minimal MCP); the harness is complicated only on a concrete trigger"
learning_goal: "The agent starter kit: a thin default + triggers for complication; a rhyme with the ladder and the map of 5 slots"
learning_outcomes: [LO7]
chapter_ref: "§5.2b [for-slide-s27b]"
---

# Visible content

## Title bar
«The agent starter kit»

## Body
[Default — a thin agent]
One instruction file + flat memory · **no** subagents · no complex set of skills · minimal MCP access

[Triggers for complication — each for a concrete question]
- **A memory backend** ← the history outgrew the window OR retrieval by facts is needed
- **Subagents** ← a separate window is needed (not to clutter the context) OR isolation of untrusted work
- **More MCP** ← a concrete task requires a concrete tool, not "just in case"

[Gold callout, bottom]
The same ladder, one level down: **the burden of proof is on complication, not on simplicity.** "Give everything at once" is a cargo cult.

## Speaker notes

The ladder gave a rule for the architecture of the whole system. The same principle must be applied inside a single rung — "agent" — to the question of exactly which harness to equip it with by the map of five slots. This is not a new idea but the same ladder one level down. The default is a thin agent. By the harness registry's data, the starting point for a new assistant agent is one instruction file and flat memory, without subagents, without a complex set of skills, with minimal access to external tools. This is exactly the same default as "a single call" on the ladder of architectures: not because a thin harness is always sufficient, but because the burden of proof lies on complication, not on simplicity.

The triggers for complication are explicit, and each answers a concrete question rather than a general "will come in handy." A memory backend instead of a flat file is added when the history has outgrown what fits in the context, or when structured retrieval by facts is needed — this is verbatim the same criterion that determines the transition from a prompt to RAG, only applied to the agent's own history. Subagents are added when a concrete subtask requires a separate context window or isolation of untrusted work; an abstract "let it be there for flexibility" is not a trigger. More access through MCP is added when a concrete task requires a concrete tool, not just in case, because every connection is a new trust boundary. And an important detail: the presence-paradox study directly shows that adding an instruction file as a ritual does not work without a real gap that it fills. Giving the agent everything at once is that very cargo cult the whole ladder works against.
