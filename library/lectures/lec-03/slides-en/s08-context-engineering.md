---
id: s08
type: assertion_visual
section: "Section 1. The prompt and its limits"
duration_min: 2.5
assertion: "Minimal high-signal context is an engineering requirement: accuracy falls with length (context rot = «lost in the middle» of Lecture 2)"
learning_goal: "Context engineering + context rot (an explicit stitch) + the criterion «when NOT RAG»"
learning_outcomes: [LO7]
chapter_ref: "§1.4 [for-slide-s08]"
visual_brief: "Left — a descending curve «retrieval accuracy ↓ as tokens in the context grow», caption «context rot = lost in the middle of Lecture 2 §3». Right — a criterion bar «when NOT RAG: a small stable corpus → full-context + caching». Gold — the failure zone on the curve."
interaction: none
---

# Visible content

## Title bar
«Context engineering: the minimum of high-signal»

## Body
[One distinction line, 16pt italic]
*Prompt engineering — a single instruction. Context engineering — curating the whole set of tokens the model sees at inference.*

[Left — a curve in an Ocean rounded box]
**Accuracy of retrieving the needed information**
↓ falls as the number of tokens in the context grows  *(the failure zone — gold accent)*

Caption: **context rot** = the same phenomenon as "lost in the middle" from Lecture 2 — a new practical term, not a new entity

[Right — a criterion bar]
**When NOT RAG (point 1):**
a small stable corpus that fits in the window → **full-context + prefix caching**, not RAG infrastructure

[Principle, bottom]
"Find the smallest set of high-signal tokens that maximizes the probability of the desired outcome" — this is an engineering requirement, not an aesthetic.

## Speaker notes

If chain-of-thought is about the form of a single call, then context engineering is about its content. Let us introduce a distinction. Prompt engineering, familiar from Lecture 1, is the wording of a single instruction: role, task, context in the text of the request. Context engineering is a broader and more iterative discipline: curating the whole set of tokens the model sees at inference[3], including system instructions, descriptions of available tools, loaded external data, and message history. The main principle is stated thus: find the smallest set of high-signal tokens that maximizes the probability of the desired outcome.

Why is minimal context not an aesthetic but an engineering requirement? Here we need to recall the effect from Lecture 2 that we called there "lost in the middle": a model makes worse use of information that landed in the middle of a long context compared to the beginning and the end. This phenomenon has acquired a second name — context rot: as the number of tokens grows, the accuracy with which the model retrieves the needed information falls. This is exactly what the graph shows: the horizontal axis is how many tokens are in the context, and the farther right along it (the longer the context), the lower the accuracy curve goes. This is the very same phenomenon as "lost in the middle" from Lecture 2, under a new practical name — I make this stitch explicit so the term is not perceived as a new entity. The mechanism is the same: the pairwise links of the attention mechanism grow quadratically with length.

The direct consequence: "just put everything into the context" is not a strategy. A large context window gives you the ability to fit a lot of text, but not a guarantee that the model will use that text correctly. And this, looking ahead, is one of the keys to the question "when NOT RAG," which we will examine in Section 2: sometimes the right answer is not to build retrieval infrastructure but to carefully curate a small stable context and reuse it via caching. That is the first practical criterion: if the knowledge corpus is small, stable, and fits in the window — RAG here would add fragility without a gain, and the right answer is simpler than it seems.

Sources:
[1] Chroma Research — Context Rot — retrieval accuracy falls as the number of tokens in the context grows. https://research.trychroma.com/context-rot
[2] Liu et al. 2023 — Lost in the Middle — the same "lost in the middle" phenomenon from Lecture 2 — a new term, not a new entity. https://arxiv.org/abs/2307.03172
[3] Anthropic — Effective Context Engineering — minimal high-signal context — an engineering requirement, not an aesthetic. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
