---
id: s19
type: assertion_visual
assertion: "RAG in one flow: question → search over the base → fragments into context → answer"
learning_goal: "The intuition for RAG in one paragraph before the case where it's needed — not how the search works inside"
learning_outcomes: [LO1]
references: []
visual:
  pattern: horizontal_flow_4_steps
---

# A word on RAG

## Assertion

Search over a knowledge base drops the right fragments into the model's context before it answers

## Visual

A horizontal diagram with four steps: "user's question" → "search for relevant
fragments in the base" → "fragments into the model's context" → "the model
generates an answer." A caption at the bottom: "details — Lecture 3."

## Speaker notes

Before we move to the next case, a word on RAG — you'll need this term right
now, and it'll keep coming up through the rest of the session. Here's how it
works: the user asks a question → the system searches for relevant fragments in
a knowledge base → the fragments it finds get dropped into the model's context
→ the model generates an answer based on the question and what it found. RAG
is needed when the knowledge base is large, changes over time, and its full
volume physically doesn't fit into a single request to the model — meaning the
model literally can't "read" all of it at once, it needs to find just the
relevant piece ahead of time. How the search itself works inside — embeddings,
indexing — we'll cover that in detail in Lecture 3; for today this intuition is
enough to recognize the architecture when you need it, instead of reinventing
it from scratch every time.
