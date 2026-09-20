---
id: s20
type: assertion_visual
assertion: "An agent as a loop: plan → tool → check → next"
learning_goal: "The intuition for an agent in one paragraph before the case where it's needed — not the details of planning"
learning_outcomes: [LO1]
references: []
visual:
  pattern: circular_flow_4_steps
---

# A word on agents

## Assertion

The model works in a loop with external tools, rather than a single call

## Visual

A circular diagram with four steps: "builds a plan" → "calls a tool (API,
search, code)" → "checks the result" → "decides what's next" → back to "builds
a plan." A caption at the bottom: "details — Lecture 3."

## Speaker notes

And second — agents. Here the model doesn't work as a single call, it works in
a loop: it builds a plan, calls an external tool — that could be an API, a
search, running code — checks the result of that call, decides what to do
next, and repeats several times in a row until the task is done or it needs a
human to step in. The key difference from RAG — here the model isn't just
answering a question based on retrieved fragments, it's actually doing
something in the outside world and checking whether it worked. The details of
how an agent plans internally — again, Lecture 3. For today, only one thing
matters: recognizing when a task needs this kind of loop with tools, rather
than a single answer from the model. Keep these two diagrams in mind — RAG and
agent — you'll need both in just a minute, in the next case.
