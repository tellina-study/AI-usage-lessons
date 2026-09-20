---
id: s28
type: case_study
assertion: "You need an agent — to go through the sources; you don't need RAG — no arbitrary query against a large base"
learning_goal: "Breaking down the quickfire — a common mistake: mistaking RAG for 'many sources'"
learning_outcomes: [LO1, LO7]
references: []
visual:
  pattern: two_column_needed_not_needed
---

# Digest — breakdown

## Assertion

Many sources isn't the same thing as RAG

## Visual

Two columns: "You need an agent" — to go through several sources on a
schedule, a multi-step task. "You don't need RAG" — there's no arbitrary
user query against a large base, the crawl runs on a schedule, and the
summarization is a single call after the material is collected.

## Speaker notes

You often hear "you need RAG because there are many sources" here — and
that's not right, even though the intuition is understandable. You need an
agent or a pipeline, because someone has to go through several sources on
a schedule — check the chat, check the email, collect the messages — and
that's a multi-step task involving calls to external systems. RAG, on the
other hand, isn't needed here: the sources are crawled directly on a
schedule, not on an arbitrary user query, and once the material is
collected, the summarization is done with a single model call, with no
search over an archive. RAG is specifically about search over a large,
changing base on an arbitrary user query, not about "we have a lot of
data sources" by itself. Mixing up these two signals is a common practical
mistake worth remembering separately from the case itself.
