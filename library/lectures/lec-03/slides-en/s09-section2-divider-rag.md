---
id: s09
type: section_divider
section: "Section 2. RAG"
duration_min: 1
assertion: "Section 2 — RAG: retrieval-augmented generation on top of the embeddings of Lecture 2"
learning_goal: "Section 2 divider + a one-phrase «what RAG is»"
learning_outcomes: [LO7]
chapter_ref: "§2.1 [for-slide-s09]"
visual_brief: "A large «Section 2» centered (mega 120pt gold-outline). Below it — «RAG: retrieval-augmented generation». Frame phrase 20pt: retrieve the relevant → put into the context → answer grounded in the source. At the bottom — a roadmap bar (6 cards), gold marker on «2 RAG»."
interaction: none
---

# Visible content

## Title bar
(none — section divider)

## Body
[Center — mega «Section 2», 120pt gold-outline]
**Section 2**

[Below it — 36pt deep]
**RAG: retrieval-augmented generation**

[Frame phrase, 20pt semi-bold light]
*Retrieve the relevant → put into the context → answer grounded in the source*

[Bottom — roadmap bar: 6 cards]
0 Opening · 1 Prompt · **2 RAG** *(gold marker — current)* · 3 Fine-tune · 4 API·agents · 5 Framework

## Speaker notes

We finished the first section: the default is a single call, it can be strengthened with step-by-step reasoning, but reasoning has a limit of faithfulness, and the context needs to be curated rather than dumped. Now — the next rung of the ladder.

A single call with a good prompt runs into a natural boundary: the model knows only what got into its weights during training, plus what you manually put into the context. If the task requires knowledge that is not in the weights — for example, a company's private database — or that changes faster than new model versions come out — for example, current prices or documents — a single call will not handle it. This is where RAG begins: retrieval-augmented generation.

In one phrase, the principle is this: before calling the model, the system first retrieves relevant fragments from an external knowledge store, puts them into the context together with the question, and only then does the model generate an answer, grounded in these fragments. In this section we will work through: how RAG is structured in three steps and why its search mechanism is exactly the semantic search from Lecture 2; when RAG is the right choice and when it is not, and why the latter matters more; and how RAG quietly breaks at scale, closing the section back to the Air Canada case from the opening.
