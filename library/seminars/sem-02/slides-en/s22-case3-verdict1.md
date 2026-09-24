---
id: s22
type: case_study
assertion: "Schema v1: email with transcript → model call with a template → minutes"
learning_goal: "Breaking down the setup — one one-off call, no storage, no loop"
learning_outcomes: [LO1]
references: []
visual:
  pattern: schema_v1_single_call
---

# Meeting minutes — breakdown

## Assertion

One call, no storage, no loop

## Visual

A three-block diagram: "email with transcript" → "model call with a template" →
"minutes." No row of options under the diagram — just the final schema
for the solution. Small caption: the transcript already arrives as a ready-made
email — no separate input-assembly step is needed.

## Speaker notes

The entire transcript of one meeting fits into the model's context in one
go — which means we need a single one-off model call, no RAG, no agent
required, and either one would be unnecessary complexity. The schema is
simple: an email with the transcript comes in as input → one model call with
a preset template ("pull out decisions, action items, deadlines") → out comes
a finished set of minutes. No storage, no loop checking intermediate
results — because the task doesn't call for it. Everything the model needs
to answer fits into a single request in full, and the result comes back
right away, with no intermediate steps and no calls to any external
systems. This is the simplest option there is, and it's fully justified
by the task as currently stated — complicating it now would mean solving
a problem that simply doesn't exist yet.
