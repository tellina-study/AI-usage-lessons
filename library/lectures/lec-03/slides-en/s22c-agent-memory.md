---
id: s22c
type: assertion_visual
section: "Section 4. Agents"
assertion: "Agent memory scales by the same question as RAG for a corpus: a flat file is sufficient while the history is small; a structured store is needed when the history is large or requires retrieval by facts"
learning_goal: "Agent memory: flat file → mem0/Cognee/Graphiti-Zep; the same question of scale as RAG, but for memory"
learning_outcomes: [LO7]
chapter_ref: "§4.5 [for-slide-s22c]"
interaction: none
---

# Visible content

## Title bar
«Agent memory: from a flat file to a graph»

## Body
[The spectrum of memory complexity]
- **Flat file** — the agent appends to a log, on startup reads it whole (while the log is small)
- **mem0** — cross-session memory about the user (personalization)
- **Cognee** — memory on a knowledge graph (retrieval by relations, not only by text)
- **Graphiti / Zep** — a temporal knowledge graph (knows when a fact became true and went stale)

[Gold callout, bottom]
**The same question of knowledge scale that RAG solves for a corpus — here it arises for the agent's own memory.** A flat file ≈ "the corpus fits in the window"; a graph store ≈ "the knowledge is large + provenance is needed".

## Speaker notes

The first harness slot is memory: what the agent remembers between sessions, as opposed to the context of a single conversation, which lives only while the dialogue is open. The simplest form of memory is a flat file[1]: the agent appends facts, conclusions, a history of decisions to a text log, and on the next startup reads this file whole. This works while the log is small and does not grow uncontrollably. At the other end of the spectrum are specialized vector or graph memory stores. The mem0 system gathers facts about the user and their preferences and reuses them in future sessions. Cognee builds memory on a knowledge graph where facts are connected through an ontology, and retrieval accounts not only for text closeness but for relations between entities. Graphiti and Zep go further — these are temporal knowledge graphs that explicitly track the time a fact is valid and its origin: the system knows when a fact became true, when it went stale, and where it came from.

Here a question we already worked through for RAG repeats directly. The same question of knowledge scale that RAG solves for a corpus of documents arises for the agent's own memory. A flat file works while the history is small and stable — a direct parallel to the criterion "the corpus fits in the window." A structured store is needed when the history is large, growing, or requires retrieval by facts — who said what, when, is it still current — rather than just "give me the last messages." The criterion is one and the same, applied to a different object. And symmetrically the ladder rule works: do not give a graph memory store to an agent that has short unconnected sessions and nothing to recall in a structured way — it is the same technical debt without a requirement as RAG for ten articles.

Sources:
[1] agent-harness-registry (live-eval) — the spectrum of agent memory — source not confirmed by a canonical URL as of 2026-08-30; a parallel with the RAG scale criterion. [VFY: not confirmed by a canonical URL, present as data from an independent live-eval registry, not as a primary source]
