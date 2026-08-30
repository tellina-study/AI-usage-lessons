---
id: s12
type: comparison
section: "Section 2. RAG"
duration_min: 2.5
assertion: "Knowing when RAG is NOT needed is more valuable: a small corpus → full-context; a fixed policy → lookup; data available live via API/MCP → no index needed"
learning_goal: "3 criteria for «when NOT RAG» (contribution to LO7)"
learning_outcomes: [LO7]
chapter_ref: "§2.3 [for-slide-s12]"
visual_brief: "3 equal columns, each — a «not RAG» criterion + the correct alternative: (1) corpus <~200k tokens → full-context+cache; (2) a fixed policy → deterministic lookup; (3) no observation of retrieval → a hidden bomb. Gold — «hidden bomb»."
interaction: none
---

# Visible content

## Title bar
«When RAG is NOT the right choice»

## Body
[One framing line, 16pt italic]
*Knowing when RAG is not needed is more valuable than when it is: it is a fashionable architecture, put where it does harm.*

[3 equal columns in an Ocean rounded box, parallel structure]

**1. The corpus fits in the window**
*(a rough guide — under ~200k tokens, changes rarely)*
→ full-context + **prefix caching**, not RAG infrastructure

**2. The task is to return a fixed policy / value**
*(a fare, a price, a regulation clause, a rule)*
→ a deterministic **lookup** / a static page

**3. The data is available live via API / MCP**
*(the data already sits in a system with direct programmatic access)*
→ a direct tool call directly, **without** a separate RAG index  *(gold accent)*

[Rule, bottom]
**RAG is redundant or inappropriate if (a) the corpus fits in the window and is stable, (b) the task reduces to a fixed value, or (c) the knowledge is already available directly and live through a tool.**

## Speaker notes

Knowing when RAG is not needed is more valuable than knowing when it is, because RAG is a fashionable architecture, and it is put where it does harm. Three clear "not RAG" criteria[1].

First. The corpus fits in the window — a rough guide of the order of under two hundred thousand tokens — and does not change often. The right answer is full-context with prefix caching, not RAG infrastructure. This is simpler, cheaper, and does not introduce the risk of "retrieval pulled the wrong thing": there is no vector store, no indexing pipeline, no retrieval component that can break. RAG here is bought without need.

Second. The task is to return a fixed policy or value: a fare, a price, a regulation clause, a rule. If the answer is deterministic and known in advance, the right architecture is a deterministic lookup or a static page, not "retrieval plus generation on top." Generation on top of a fragment always carries the risk that the model will paraphrase, generalize, or make things up — this is exactly what happened in the Air Canada case.

The third criterion is often missed. The data is already available directly and live via API, MCP, or search in another system. If the knowledge already sits in an internal service with a REST interface or in a database accessible through MCP — building a separate RAG index on top of it is redundant. RAG exists to give access to knowledge for which there is no direct path; if the path already exists, RAG adds an extra, more fragile, and aging layer. The difference is strategic: a direct tool call returns the data as of the query moment, while a RAG index — as of the last indexing. The signal is simple: if to the question "why doesn't the model just ask system X directly through a tool?" the answer is "indeed, why not," — RAG is not needed.

Let us fold it into a rule: RAG is redundant if the corpus fits in the window and is stable, if the task reduces to a fixed value, or if the knowledge is already available live through a tool. Any of the three is met — a signal to stop. And even when none of them triggered and RAG is justified, this does not guarantee it will work well at scale — a separate question.

Sources:
[1] Red Hat — RAG vs Fine-Tuning (when not RAG) — corpus fits in the window → full-context+cache; fixed value → lookup; live → API without an index. https://www.redhat.com/en/topics/ai/rag-vs-fine-tuning
[2] McCarthy Tétrault — Air Canada («generation on top of a fixed policy») — a fixed policy → a deterministic lookup, not retrieval+generation. https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot
