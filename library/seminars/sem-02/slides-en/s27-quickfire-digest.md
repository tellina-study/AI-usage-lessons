---
id: s27
type: case_study
assertion: "A digest of chats and email — what architecture does that need?"
learning_goal: "Quickfire setup with noise — just the question"
learning_outcomes: [LO1]
references: []
visual:
  pattern: single_card_plus_question
---

# Digest of chats and email

## Assertion

"A digest of chats and email — what architecture does that need?"

## Visual

A card: several source icons (chat, email) → arrow → a summary-digest
icon. On the right — the question: "What architecture does this need?"

## Visual — quote

"We talked about this at the standup — we want a weekly digest of the
team's work chat and email: what was discussed, what was decided that
week, in one message. Needed by 5 PM on Fridays. There are a few
sources: the team's work chat and email, both have an API for pulling
message history. It needs to come together into one coherent message, not
just chunks stitched together. By the way, we also separately discussed
whether to move to a different messenger, and in parallel we're testing a
new VPN solution for remote workers — but that's got nothing to do with
the digest."

## Speaker notes

Read the line out in full. The direct signal, not particularly
highlighted: we need specifically a weekly (scheduled, not on-demand)
digest of a few specific sources — the work chat and email — once a week
by 5 PM on Friday, and the information needs to come together into one
coherent message. It's worth pulling out the indirect signal: both
sources (chat and email) already have an API for pulling history — so the
technical ability to collect data on a schedule already exists, the only
question is what architecture processes what's collected. Moving to a
different messenger and testing the VPN are noise twins — both about the
company's communication infrastructure, but neither affects the digest's
architecture. Question to the room: what architecture does this need — a
one-off model call, RAG, an agent, or something else? Argue it, don't
just name a technology — explain why you picked it, and what specifically
in the setup pointed you toward that idea. Who's ready? Argue your
choice. When you break it down, ask: which facts in the line affected
your choice, and which didn't?
