---
id: s05
type: assertion_visual
section: "Section 1. The prompt and its limits"
duration_min: 2
assertion: "The default is a single call with a good prompt; any climb up the ladder is paid for by a task requirement"
learning_goal: "The reference point of the ladder + distribution of the burden of proof"
learning_outcomes: [LO7]
chapter_ref: "§1.1 [for-slide-s05]"
visual_brief: "Left — a large block «1 call = minimum cost + latency + maximum predictability». Right — a list «what each climb adds»: RAG → indexing pipeline/storage/retrieval degradation; agent → external calls/loops/nondeterminism/attack surface. Gold — the rule phrase «complexity is paid for by a task requirement»."
interaction: none
---

# Visible content

## Title bar
"The default is a single call"

## Body
[Left — the main block in an Ocean rounded box]

**A single LLM call with a good prompt**
- minimum cost (one pass)
- minimum latency (no extra requests)
- maximum predictability (no loops, no retrieval that quietly degrades)

[Right — "what each climb costs you", 2 blocks]

**You add RAG** → an indexing pipeline + a vector store + a retrieval component (may silently degrade) + metrics for its quality

**You add tools / a loop** → external calls (fail, slow down) + loops (diverge) + nondeterministic trajectory + a new attack surface

[Gold callout, bottom]
**Do not complicate the architecture without a reason expressed in the task's requirements. This is a distribution of the burden of proof, not primitivism.**

## Speaker notes

Before choosing between RAG, fine-tuning, and agents, let us fix the reference point. The cheapest, most reliable, and most predictable AI architecture is a single model call with a well-composed prompt[1]. A single call — in Lecture 2 this was single-shot inference — has neither external search, nor a loop, nor tools: a prompt in, an answer out, no memory between calls. It has minimum cost, minimum latency, and maximum predictability: no loops that diverge, no retrieval that quietly degrades.

Let us fix the boundary that is load-bearing for the whole section: the model knows only what got into the prompt, plus what settled in its weights during training. This is the only source of information available to a single call. Everything that is in neither the prompt nor the weights is unknown to the model, and then it either honestly refuses to answer or generates plausible but ungrounded text. It is precisely this boundary that is the reason RAG appears next, expanding what is "in the prompt," and fine-tuning, expanding what is "in the weights."

The default engineering rule: do not complicate the architecture without a reason expressed in the task's requirements. This is not a call for primitivism but a distribution of the burden of proof. By default the architecture is a single call. Any move higher requires an explicit justification: here is a task requirement that a single call does not close, so I add RAG, a tool, or a loop. If no such requirement can be stated, the complexity is technical debt you take on without need.

It helps to fix what each climb costs, so that the burden of proof is an itemized list. Adding RAG, you add an indexing pipeline, a vector store, a retrieval component that can silently degrade, and metrics for its quality. Adding tools and an agent loop — external calls that fail and slow down, loops that diverge, a nondeterministic trajectory, and a new attack surface. None of these items appear with a single call. So "a single call by default" is not conservatism but a refusal to pay for infrastructure and failure modes the task does not require.

Sources:
[1] Anthropic — Building Effective Agents ("find the simplest") — do not complicate the architecture without a task requirement — distribution of the burden of proof. https://www.anthropic.com/research/building-effective-agents
