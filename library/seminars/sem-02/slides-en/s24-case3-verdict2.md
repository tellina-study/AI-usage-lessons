---
id: s24
type: case_study
assertion: "Schema v2: a growing archive calls for RAG — search over the base layered on the one-off call"
learning_goal: "Breaking down intro 1 — a growing base justifies RAG; the schema visibly extends schema v1"
learning_outcomes: [LO1]
references: []
visual:
  pattern: schema_v2_expansion
---

# Meeting minutes — breakdown 1

## Assertion

A growing, changing archive plus an arbitrary query — that's when you need RAG

## Visual

A schema extending schema v1: the earlier blocks ("email with transcript" →
"model call with a template" → "minutes") stay in place, but are visually
dimmed — gray, faded tones. New blocks are highlighted in color and added
to the left/top: "minutes storage" → "indexing" → "search on query" →
"snippets into the model" (this chain leads into that same dimmed
"model call" block, showing that the old path wasn't thrown out, just
extended). No row of options under the diagram.

## Speaker notes

As long as it was one transcript of one meeting that fit entirely into the
model's context, a one-off call was the right and sufficient answer —
neither RAG nor an agent would have been needed, and either would only
have complicated things for no benefit. But now the base of minutes is
growing over time, constantly filling up with new meetings, and the whole
volume physically no longer fits into a single model request. So we need
search over this growing base for an arbitrary user query — and that's
exactly what RAG is for: finding relevant snippets of minutes by the
meaning of the query, rather than trying to feed the model the entire
archive every single time. Notice on the schema — the old path hasn't gone
anywhere, we've just added storage, indexing, and search before the
needed snippets reach that same model call we had at the previous step.
We didn't pick RAG ahead of time "just in case" — we arrived at it only
once a concrete requirement showed up that the simple option could no
longer handle.
