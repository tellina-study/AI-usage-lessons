---
id: s03
type: assertion_visual
section: "Section 0. Opening"
duration_min: 1.5
assertion: "Four wrappers are built around a single model call — and one of them (RAG) stands directly on the embeddings of Lecture 2"
learning_goal: "Recap of Lecture 2 (single-shot + embeddings) + bridge to RAG"
learning_outcomes: [LO7]
chapter_ref: "Introduction [for-slide-s03]"
visual_brief: "Hub & spokes: at the center — «A single LLM call» in a gold Ocean rounded box (the slide's only gold accent, the reference point). Around it — 4 equal-weight wrappers (no per-card gold): RAG, Function calling, MCP, Agent loop. Footer — what we take ready-made from Lecture 2."
interaction: none
---

# Visible content

## Title bar
"What we carry over from Lecture 2 — and what we build on top."

## Subtitle
"Four wrappers are built around a single model call. Two ready-made blocks from Lecture 2 we do not re-explain."

## Body
[At the center — a gold hub in an Ocean rounded box]

**A single LLM call**
*single-shot inference from Lecture 2: one pass, no memory between calls*

[Around the center — 4 equal-weight wrapper spokes, each in an Ocean rounded box]

**RAG** — external knowledge into the context before the answer

**Function calling** — the model reaches out to external systems

**MCP** — a standard for connecting tools

**Agent loop** — many steps around a single pass

[Footer, bottom, 12pt italic]
*From Lecture 2 we take ready-made: single-shot inference and semantic search on embeddings (the basis of RAG). The details of each wrapper — later in the sections.*

## Speaker notes

From Lecture 2 we carry two ready-made blocks over here and will not re-explain them. The first is semantic search on embeddings from Lecture 2, section 2: text is turned into a vector, closeness of vectors means closeness of meanings, so you can search by meaning without an exact word match. RAG stands entirely on this block, and we will refer to it as known. The second block is single-shot inference from Lecture 2, section 4: a single model call is one pass with no memory between calls. It is around this single pass that we will be building up tools, loops, and agents today. If semantic search or single-shot are only vaguely remembered — it is worth rereading the corresponding sections of Lecture 2 before this lecture.

The picture on the slide sets up the structure of the whole lecture. At the center — a single model call, the most basic architecture. Around it — four wrappers we will work through. The first is RAG: this is exactly that semantic search from Lecture 2 plus generation on top of what was retrieved; the arrow from embeddings to the RAG node emphasizes that the new material here is built on top of the already familiar, rather than introduced from scratch. The second is function calling: a way to give the model the ability to reach an external system. The third is MCP: the standard by which tools connect to the model. The fourth is the agent loop: many steps around a single pass. By the end of the lecture these four wrappers will be, for you, not a list of buzzwords but a set of tools with known limits of applicability, between which you can consciously choose. The details of RAG — in Section 2; here it is only important to note that it stands on a familiar foundation.
