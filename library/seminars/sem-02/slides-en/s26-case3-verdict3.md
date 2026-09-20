---
id: s26
type: case_study
assertion: "Schema v3: an action in an external system — you need an agent on top of RAG"
learning_goal: "Breaking down intro 2 — an action in an external system justifies an agent; the closing lesson"
learning_outcomes: [LO1, LO7]
references: []
visual:
  pattern: schema_v3_expansion
---

# Meeting minutes — breakdown 2

## Assertion

Start with the simplest option, add complexity only when a requirement can't be met any other way

## Visual

A schema extending schema v2: the earlier blocks (email → model call →
minutes → storage → indexing → search → snippets into the model) stay in
place, dimmed gray/faded. New blocks are highlighted in color and added to
the right: "extract action item" → "call the task-tracker API" → "create
the task" → "verify the result." At the bottom — a separate takeaway line:
"every extension was paid for by a new requirement." Small caption: the
task tracker has an open API — the integration is cheap, not hypothetical.
No row of options under the diagram.

## Speaker notes

Now there's an action in an external system: you need to call the
task-tracker API, create tasks, verify that they were created correctly,
with the right owner and deadline. A single model call, or even search
over the base, doesn't cover that — you need a workflow or a full-fledged
agent that calls an external tool and verifies the result of the call.
Look at the whole schema: the earlier path with storage and search hasn't
gone anywhere, it's just been extended on the right with new blocks —
extract the action item, call the API, create the task, verify the
result. Every extension was paid for by a new requirement: the one-off
call was justified as long as everything fit into one transcript; RAG
showed up once the base grew; the agent showed up once an action in an
external system was needed. The architectural choice was driven by
concrete new requirements, not by a fashion for a technology. Start with
the simplest option that solves the current task, and add complexity only
once a requirement shows up that the simple option physically cannot
handle. Not the other way around.
