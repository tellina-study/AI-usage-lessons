---
id: s10
type: process
section: "Section 2. RAG"
duration_min: 3
assertion: "RAG = indexing → retrieval (semantic search of Lecture 2) → grounded generation; «I don't know» is a correct answer, invention is a defect"
learning_goal: "The RAG principle in 3 steps + the grounding invariant"
learning_outcomes: [LO7]
chapter_ref: "§2.1 [for-slide-s10]"
visual_brief: "A horizontal 3-stage pipeline (RIGHT_ARROW): indexing → retrieval (marked «= semantic search L2 §2») → grounded generation (answer + citation). Below the pipeline — a gold invariant plate: «an answer with a citation ≠ plausible text; „I don't know" is correct»."
interaction: none
---

# Visible content

## Title bar
"The RAG principle — three steps"

## Body
[A horizontal 3-stage pipeline with RIGHT_ARROW, Ocean rounded boxes]

**(1) Indexing** *(in advance, offline)*
corpus → chunks → an embedding of each → vector store

→

**(2) Retrieval** *(on the query)*
question → embedding → top-k nearest fragments
*= that same semantic search from Lecture 2 — not re-explained*

→

**(3) Grounded generation**
fragments + question → answer **with a reference to the source**

[Gold callout — invariant, bottom]
**"I don't know" / "see source X" is a correct answer of a RAG system. A plausible answer under irrelevant retrieval is a defect, not "better than nothing."**

## Speaker notes

RAG — retrieval-augmented generation — is an architecture in which, before calling the model, the system first retrieves relevant fragments from an external store, puts them into the context together with the question, and only then does the model generate an answer grounded in these fragments[1]. Let us introduce a term: retrieval — the stage of searching for and extracting relevant fragments; it is precisely this that distinguishes RAG from "put the document into the prompt manually."

The key point: the retrieval mechanism in RAG is exactly that semantic search on embeddings that we built in Lecture 2, and we will not re-explain it. A reminder in one phrase: text is turned into a vector, closeness of vectors means closeness of meaning, so a fragment can be found by the meaning of the question rather than by a word match. RAG builds up three steps. The first is indexing, in advance, offline: the corpus is cut into fragments, each is turned into an embedding and placed into a vector store. The second is retrieval, on the query: the question is turned into an embedding, and by closeness of vectors the k relevant fragments are pulled. The third is grounded generation: the fragments are placed into the context together with the question, the model answers relying on them, and in a good implementation — with a reference to the source.

Let us introduce one more term that carries the main load in this section. Grounding — the property of an answer being derived from specific retrieved fragments, rather than composed by the model out of thin air, with the ability to show which fragment each fact was taken from. A good RAG system is designed so that the answer is grounded, and so that to a question for which the retrieved fragments contain no answer, the system says "I don't know" or "see the source," rather than composing one. Let us state it as an engineering invariant: "I don't know" is a correct answer of a RAG system; a plausible answer under irrelevant retrieval is a defect, not "better than nothing." The distinction between "an answer with grounding and a citation" versus "plausible text" will turn out to be central further on and directly explains the Air Canada case.

Sources:
[1] Lewis et al. 2020 — Retrieval-Augmented Generation (NeurIPS) — the canonical RAG paper: indexing → retrieval → grounded generation. https://arxiv.org/abs/2005.11401
