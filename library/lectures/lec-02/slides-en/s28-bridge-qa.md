---
id: s28
type: summary
section: "Section 5. Wrap-up"
duration_min: 1.5
assertion: "Lecture 3: 'Agents, RAG, API: how AI goes beyond the chat'"
learning_goal: "Bridge to Lecture 3"
learning_outcomes: [LO1]
chapter_ref: "§5.5 [for-slide-s28]"
visual_brief: "4 Ocean rounded boxes with icons — the concepts of Lecture 3: RAG, Tools / Function calling, MCP, Agent loop."
---

# Visible content

## Title bar
"What's in Lecture 3"

## Body
[Under the title — the assertion large]
**Lecture 3:** "Agents, RAG, API: how AI goes beyond the chat"

[4 Ocean rounded boxes, 2×2 grid or horizontal]

**(1) RAG** *(icon: magnifier + document)*
Retrieval-Augmented Generation — embedding similarity (s10-s12) + LLM → an answer from your own base.

**(2) Tools / Function calling** *(icon: gear)*
The LLM generates **specially structured JSON** → an external system executes it → the result is returned to the model.

**(3) MCP** *(icon: connector)*
Model Context Protocol — an open standard for connecting tools (Anthropic, 2024; mentioned in Lecture 1).

**(4) Agent loop** *(icon: loop)*
act → observe → adjust — the model decides an action, sees the result, adjusts the plan.

[Sub-caption at the bottom]
*All 4 build on top of a single inference pass (s21). Multimodal — right there, as part of RAG.*

## Speaker notes

The topic of the next lecture is "Agents, RAG, API: how AI goes beyond the chat". In our inference pipeline, which we've just assembled, there is a hard limitation: the model sees only what's in the context and cannot reach out for information. Lecture 3 will show how this limitation is worked around through four classes of tools.

**RAG — Retrieval-Augmented Generation.** This is an extension in which, before turning to the LLM, a semantic search is run over your knowledge base on embeddings — exactly the ones we covered in the embeddings section of today's lecture — and the top-K relevant fragments are added to the context. At the inference level it's still the same four-stage pipeline, only with an enriched context. RAG is the most direct way to give the model access to information that isn't in its weights.

**Tools, or function calling.** The mechanism through which the model generates a specially structured call — usually in JSON format, sometimes in other formats depending on the API provider — indicating which tool it wants to call and with what parameters. An external system sees this call, executes it, and the result is returned to the model as part of the context. This is the canonical way to work around the limitations of character blindness (for arithmetic — a Python sandbox) and the stateless nature (for up-to-date information — web search).

**MCP — Model Context Protocol.** An open standard for connecting tools to an LLM, introduced by Anthropic in November 2024. It solves the problem of "every combination of a model and a tool is a separate integration": one protocol, a reusable connection. We mentioned MCP in Lecture 1; in Lecture 3 we'll cover it in more detail.

**Agent loop.** The act → observe → reflect loop, discussed back in Lecture 1. At each step the model decides an action, sees the result, adjusts the plan — and so on until the goal is reached. All four concepts build on top of the single-shot inference we assembled today. Multimodal extensions — CLIP embeddings for images, audio embeddings, unified models like GPT-4o that process text and image jointly — are right there, as part of RAG for non-text modalities.

At the seminar we'll go over your homework experiments with temperature; try to run the requests in advance. And for now — we devote the remaining time to your questions.

Sources:
[1] Lewis et al. (2020) — RAG — how AI goes beyond the chat: retrieval-augmented generation. https://arxiv.org/abs/2005.11401
[2] Anthropic — Model Context Protocol (Nov 25, 2024) — an open standard for connecting tools to an LLM. https://www.anthropic.com/news/model-context-protocol
[3] Yao et al. (2022) — ReAct — agent loop: act → observe → reflect. https://arxiv.org/abs/2210.03629 [VFY-day-of]
