---
id: s12a
type: section_divider
section: "Section 2. Embeddings"
duration_min: 0.5
assertion: "Section 2 — Embeddings: the space of meaning"
learning_goal: "Divider: entry into stage 2 of the pipeline"
learning_outcomes: [LO1]
chapter_ref: "§2"
visual_brief: "v3.1 (#183 round 3): 2-column composition (unified pattern) — left, text: 'Section 2' (92pt gold), 'Embeddings', frame phrase 'The space of meaning — and where similarity breaks down', tag '4 case studies · 1 failure'. Right — a real illustration: the word2vec classic 'king − man + woman ≈ queen' (Jay Alammar, illustrated word2vec) in an Ocean rounded box, ≈25% of slide area, with attribution. Bottom, full width — mini-pipeline with the 'Vectors' stage in gold highlight (no text markers, no minutes)."
---

# Visible content

## Title bar
(none — section divider)

## Body
[Large "Section 2" centered in the top half — 140pt gold]

**Embeddings**

"The space of meaning — and where similarity breaks down"

[Tag line]
4 case studies · 1 failure

[Bottom — mini-pipeline: Text → Tokens → **Vectors** (gold highlight) → LLM → Distribution → Token → Text]

[Small "map of meaning" illustration — corner of the slide]

## Speaker notes

The first stage is behind us: text became a sequence of vocabulary identifiers. But a neural network can't meaningfully work with a bare number — there's no meaningful arithmetic between token IDs. The second stage of the pipeline turns identifiers into a representation you can actually compute with — vectors.

Here's the plan for this section. First, we'll pin down what an embedding actually is: a vector lookup from the model's input table — quick, this is the basics. Then — the section's main organizing move: the word "embedding" in engineering usage refers to three different things, and they're often conflated; we'll carefully unpack the three lives of the term — and see that embeddings work not only inside inference but also as a standalone search tool. After that — the space of meaning: how coordinates get learned, why texts close in meaning end up near each other, and how that's measured via cosine similarity. Then — the section's one important failure case: the similarity boundary, where high similarity delivers a document with a nearly opposite practical meaning, and what production search systems do about it. And we'll close the section by tying it together: why embeddings are the foundation of the model "understanding" rephrasing, and what that implies for search systems and RAG, which we'll get to in Lecture 3.
