---
id: s21
type: case_study
assertion: "After the call the transcript arrives by email — we need minutes: decisions, action items, deadlines"
learning_goal: "Case 3 setup — a live, noisy quote; the whole transcript fits"
learning_outcomes: [LO1]
references: []
visual:
  pattern: single_card_plus_question
---

# Meeting minutes

## Assertion

"About 15 meetings a week, minutes are currently written by hand by a project manager"

## Visual

A card: an icon for a full meeting transcript (a single document, a reasonable
length) → an arrow → an icon for structured minutes (decisions, action items,
deadlines). On the right — a question: "What architecture is needed?"

## Visual — quote

"After every Zoom call, the transcript lands in an email, and nobody gets
around to it. The project manager still writes the minutes by hand, 30-40
minutes each time. There are about 15 meetings a week, some in English with a
contractor — Zoom transcribes those too, just in another language. We already
put the finished minutes on the shared corporate drive, in a folder by
project. We track action items from meetings in YouTrack, which has an open
REST API if that's ever needed. Can we auto-generate minutes from the
transcript — decisions, action items, deadlines? Ideally by the end of the
quarter."

## Speaker notes

Read the quote in full. Direct signals, not flagged by intonation: after every
call, the full transcript arrives by email, minutes are needed with decisions,
action items, and deadlines, about 15 meetings a week, right now the project
manager writes the minutes by hand. Indirect signals worth pulling out
explicitly, even though they don't affect the v1 architecture right now: some
meetings are in English — the transcript is still one coherent document,
language doesn't change the v1 schema, but it'll come up as a detail later; and
the fact that YouTrack has an open REST API — that lays groundwork for v3 (an
agent that creates tickets itself), even though it's too early to talk about
that now. The minutes are already saved to the corporate drive too — also a
setup for the future (v2, storage), but it doesn't change the answer right
now. None of this is noise in the strict sense, but none of it should change
the answer to the first question either: what comes in is still one complete
transcript of a single meeting, of a reasonable length, and what needs to come
out is structured decisions, action items, and deadlines. Ask the room: what
architecture is needed here? Argue for it — what specifically in this setup
points you toward this choice and not another? Who wants to answer first?
During the debrief, ask: which facts from the quote actually shaped your
choice, and which didn't?
