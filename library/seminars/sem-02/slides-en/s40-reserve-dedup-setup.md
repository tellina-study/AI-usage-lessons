---
id: s40
type: case_study
reserve: true
assertion: "News deduplication — you need to merge messages about the same event into one card"
learning_goal: "Reserve quickfire — setup and question"
learning_outcomes: [LO1]
references: []
visual:
  pattern: single_card_plus_question
---

# Reserve. News deduplication

## Assertion

"A stream of news from many sources — we need to merge identical ones into one card"

## Visual

A card: several similar news headlines from different sources → arrow →
one merged card. On the right — the question: "What technology do you
need?"

## Visual — quote

"Users are complaining to support that the feed is cluttered — for one
event they see ten nearly identical headlines in a row from different
outlets. We want to merge them into one card. There are already more than
a hundred sources, all coming in through a single RSS aggregator, the
headline and publication-time format is the same for all of them. We're
adding a few more this month. Separately, the editor asked to update the
design of the source card on the site, but that's not related to
deduplication. The budget for new features this quarter is modest."

## Speaker notes

Read the product manager's line out in full. The direct signal, not
particularly highlighted: a stream of news from many sources, need to
merge messages about the same event into one card. The indirect signal is
worth pulling out: all the sources are already normalized through a
single RSS aggregator, meaning the headline and metadata format is
uniform — no need to solve the problem of parsing different formats,
only the problem of comparing content. The source-card redesign is a
noise twin — it looks like a change to the same feed interface, but has
nothing to do with merging duplicates. Question to the room: what
technology do you need here? Intuitively, a lot of people right now will
say — you need to understand the meaning of the text, so you need a
model, and you'll have to run every pair of news items through an LLM,
comparing them pairwise. Do you agree with that, or does anyone in the
room already have doubts on that front? Think about how many such pairs
of news items you'd need to compare every day with a large stream of
sources. When you break it down, ask: which facts in the line affected
your choice, and which didn't?
