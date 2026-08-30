---
id: s18
type: schema_architecture
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "A persistent layer of instructions and memory in the repository (AGENTS.md, memory, context-engineering) — what the agent reads every session: context lives in the repo, not in fleeting prompts"
learning_goal: "Leading: persistent layer of instructions/memory (AGENTS.md conventions/guardrails, memory, context-eng JIT/compaction/context-rot)"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.2 [for-slide-s18]"
references: [anthropic-context-engineering, agents-md]
verify_day_of: false
visual_brief: >
  schema_architecture: in the center — the AGENT (stateless, icon), left — the DEVELOPER (human, curates), right — the REPOSITORY.
  From the repository into the agent EVERY SESSION a persistent layer is read (a bidirectional arrow "reads / human curates"):
  AGENTS.md (build/test commands, style, guardrails) · memory-notes · operational task history.
  A separate block context-engineering: 3 primitives (JIT-retrieval · compaction · memory) + a warning "more context ≠ better".
  A failure plate: context rot (Chroma, 18 models: retrieval accuracy drops non-linearly, BEFORE the window overflows) +
  "stale context rots". Baseline memory demo: peak ~172k vs ~334k tokens WITHOUT memory — mark "cookbook demo, direction, not a multiplier".
  Gold — "context lives in the repo, not in the prompt". USER actor explicit. Lucide icons.
interaction: none
---

# Visible content

## Title bar
A persistent memory layer in the repository — what the agent reads every session

## Body
[schema_architecture — developer (curates) ↔ repository → agent (stateless, reads every session)]

The agent is **stateless**: memory is not preserved between runs. Therefore context must live not in the prompt but in the **repository** — a human-curated, versioned layer that the agent reads every session:

**AGENTS.md** (a vendor-neutral standard; the analog is `CLAUDE.md`) — "what you would tell a new colleague": build and test commands, style, guardrails. Rule: **lead with commands, not explanations** (otherwise the agent hallucinates the setup).

**Memory-notes** + **operational task history** — what has already been decided and why.

[context-engineering block]
Three curation primitives (Anthropic): **JIT retrieval · compaction · memory-notes**. Principle: **more context ≠ better**.

[Failure plate]
**context rot** (Chroma, 18 frontier models): retrieval accuracy drops **non-linearly** as input grows — degradation begins **before** the window overflows. "Stale context rots."
*Baseline: the memory demo — peak ~172k vs ~334k tokens without memory — is a cookbook demonstration of direction, not a controlled multiplier.*

[Gold callout]
Context lives **in the repository, not in the prompt**. The durable pattern is a curated persistent layer; the hype is "our AGENTS.md will decide everything by itself."

## Speaker notes

The second practice of the implementation phase is the organization of the environment, and this is a separate engineering discipline that is easy to confuse with the first. The first was about how to work; this is about what to store. The key fact: the agent is stateless, its memory is not preserved between sessions. This means that if context lives in fleeting prompts, it is lost every run, and the agent starts from a blank slate each time, filling in the missing parts with guesses. The solution is a persistent layer of instructions and memory that lives in the repository and that the agent reads every session.

The form of this layer today is the AGENTS.md file, an open vendor-neutral standard (Anthropic's analog is called CLAUDE.md), which holds build and test commands, style, and guardrails — what you would tell a new colleague on the first day [1]. An important recommendation: lead with commands, not explanations — if you write "we use such-and-such build system" instead of the exact command, the agent hallucinates the setup steps [1]. The second component of the layer is memory-notes and operational task history: what we have already decided and why, so the agent doesn't rediscover it from scratch.

And here comes an honest limitation. More context does not mean better. Chroma's study on eighteen frontier models showed the context rot effect: retrieval accuracy drops non-linearly as input grows, and the degradation begins even before the window overflows [2]. Plus Böckeler's rule "stale context rots": an outdated note is worse than its absence, because it actively misinforms. Therefore Anthropic proposes three curation primitives — retrieve what's needed precisely at the moment of need, compact the history, and keep short memory-notes [3]. The section's judgment: the durable pattern is a curated persistent layer of instructions and memory in the repository; the vendor hype is the promise that the file itself or the memory itself will decide everything. Context lives in the repository, not in the prompt, and it must be actively curated, not merely accumulated.
