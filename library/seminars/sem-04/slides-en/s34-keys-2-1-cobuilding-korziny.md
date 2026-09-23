---
id: s34
type: assertion_visual
duration_min: 1.75
assertion: "Not everything the agent has learned is worth writing down at all — the third basket is just as legitimate as the first two"
learning_goal: "Co-building for case 2.1: sorting five fact cards into three baskets plus assembling the final entry"
visual:
  pattern: cobuilding_baskets_and_record
  primary: "Three baskets — auto-memory / DECISIONS.md / nowhere — with the cards distributed according to the discussion. Below — the assembled entry appearing: the date, the decision in one line, the reason."
---

# Three baskets, one entry

## Assertion

Not everything the agent has learned is worth writing down at all — the third basket is just as legitimate as the first two.

## Visual

Three baskets in a row — **auto-memory** · **DECISIONS.md** · **nowhere** — with the cards distributed according to the discussion:

| Card | Basket |
|---|---|
| "We are not pulling in a third-party validation library — the form has two fields" | `DECISIONS.md` |
| "The developer asks for short answers, with no preamble" | `auto-memory` |
| "The form handler lives in `src/main.js`" | `nowhere` |
| "On September 24 a test failed because of a timeout, we raised the wait" | `nowhere` |
| "We are not building our own backend — the request goes to an external form-intake service" | `DECISIONS.md` |

Below — the assembled entry appears: the date, the decision in one line, the reason in one to three sentences — the one that actually sits in the demo repository.

## Speaker notes

The facilitator takes the cards one at a time and asks, briefly: "which one?". The comment on each is one phrase, no more.

Two cards carry most of the load. "The form handler lives in src/main.js" — almost always someone proposes writing it down: the agent will read that in a second by ordinary file reading, while the memory index is loaded into every session and has a hard limit. "On September 24 a test failed because of a timeout" — this is the card the room most often pulls into DECISIONS.md: it is a "what", not a "why", and the "what" is already in the change history.

For the "nowhere" basket, the mechanics are stated once: the space in the memory index is finite, and everything put there "just in case" occupies it in every session that follows.

After the sorting — the facilitator asks part by part: "the date?", "the decision in one line?", "the reason?" — and reveals on the slide the entry that actually sits in the demo repository. It is important to say out loud that this is a real file from a real repository, not an example made up for the slide, and that the file itself has been in the repository since day one — only the line is new.
