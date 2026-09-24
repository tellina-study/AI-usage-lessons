---
id: s41
type: case_study
reserve: true
assertion: "Fuzzy matching handles ~90% of cases cheaper and more predictably. The LLM handles the rest"
learning_goal: "Reserve: back to the regex/model boundary on new material"
learning_outcomes: [LO1, LO7]
references: []
visual:
  pattern: two_card_setup_vs_split_verdict
---

# Reserve. Deduplication — breakdown

## Assertion

A cheap deterministic filter covers the bulk of it, the model covers the rest

## Visual

Two cards: on the left — "fuzzy matching / shingling" — comparing overlapping
text fragments, ~90% of duplicate cases, cheap and predictable. On the
right — "LLM" — only for paraphrases with no lexical overlap between
messages.

## Speaker notes

As it turns out, comparing texts by overlapping fragments — fuzzy
matching and shingling — with no call to a model covers roughly 90% of
duplicate cases, and does it cheaper and more predictably than calling a
model on every pair of news items: the result is deterministic, easy to
debug, and doesn't depend on the model's mood. A model is only needed for
the remaining part — cases where two messages about the same event are
written in completely different words and share almost no text
fragments, meaning it's more of a paraphrase than a match. It's the same
lesson we had at the very start of the session with personal data in
logs: a cheap deterministic filter covers the bulk of the cases first, and
the model handles only the remainder the filter physically can't catch.
