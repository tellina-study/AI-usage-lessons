---
id: s08
type: case_study
assertion: "Regex for phone numbers and emails, a compact NER model for names in free text"
learning_goal: "Quickfire debrief — the line between a deterministic method and a small model runs inside a single task"
learning_outcomes: [LO1]
references:
  - "slovnet: https://github.com/natasha/slovnet"
visual:
  pattern: two_column_split_verdict
---

# Personal data in the logs — debrief

## Assertion

Regex covers the formatted fields, a compact NER model covers names in free text

## Visual

Two columns: on the left — "phone number, email" with a regex icon. On the right
— "names in free text" with a small NER model icon, and characteristics next to
it: ~30 MB, CPU, ~25 articles/sec. At the bottom, a shared takeaway line: "A
large share of text tasks are solved algorithmically or with small specialized
models — simpler, faster, and cheaper than a large LLM."

## Speaker notes

Phone numbers and emails are data with a clear, predictable format — a plain
regex scrubs them reliably and cheaply, no model is needed here and one would
only slow down processing 40 gigabytes of logs. But people's names and indirect
mentions in free text — like "pass this to Ivan in accounting" — require
understanding context. This doesn't call for a large LLM either: there are
compact named-entity-recognition models for this, for example slovnet from the
Natasha project — the model weighs around 30 megabytes, it runs comfortably on
a regular laptop's CPU with no GPU, at a speed of roughly 25 articles per
second. The model recognizes people's names, organization names, locations —
including company names and cities. By size, that's roughly 60 times smaller
than a comparable BERT-class model, at a quality loss of 1-2 percentage points.
The takeaway is worth stating explicitly: a large share of text tasks are
solved algorithmically or with small specialized models — that's simpler,
faster, and cheaper than running everything through a large LLM. The same
question of data sensitivity will come up again in the sales-calls case — where
the stakes are noticeably higher.
