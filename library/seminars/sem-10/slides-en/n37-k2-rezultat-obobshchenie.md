---
id: n37
type: content
duration_min: 1.0
assertion: "The requester sees a broken answer; Olga sees a number — what share of questions risks getting one under the current setting"
learning_goal: "Result and generalization for Case 2: what the requester sees vs. what Olga sees, and the transferable principle (a store chunk is a unit inside which meaning must be preserved)."
visual:
  pattern: content
  primary: >
    Two tiles side by side: "to the requester", "to Olga" — then a
    formula tile with the transferable principle.
  backup: >
    Text — SETKA-KEYSOV.md Case 2, "Result and generalization", verbatim.
---

# What Olga sees, and what the requester sees

## Assertion

A broken answer looks incomplete or wrong — even though search found exactly what it was looking for.

## Visual

The requester sees the result directly: if the answer to their question is torn between two chunks, the model gets only half of the needed fact and answers incompletely or incorrectly — this isn't a matter of search quality; what it found was itself incomplete. Olga sees a number — what share of questions risks getting a broken answer under the current cutting setting.

> **The principle is general: applicable to any text-cutting tool, and the chunking node in n8n is just one example here. A store chunk is a unit inside which meaning must be preserved; the choice of where to cut directly determines how many answers arrive intact, and it carries far more weight than an ordinary technical setting.**

## Speaker notes

Two different observers of the same decision — and for both, the result is tangible, just in different ways.

The requester sees the direct effect. If the answer to their question ends up torn between two store chunks, the model receives only half of the needed fact as input — and answers incompletely or outright incorrectly. Importantly: this isn't because search performed poorly. Search found exactly what it was looking for — the chunk closest in meaning. The problem is that the chunk it found contained only half the answer. From the outside this looks like a search error, though in reality it's a cutting error, made back at the data-preparation stage.

Olga sees a number, and this isn't a one-off case — what share of questions from a typical stream risks getting a broken answer under the current cutting setting. We just saw this number — from 2.8 to 12.5 percent when cutting by characters, from 0 to 1.4 percent when cutting by sentences.

And here is the principle worth carrying forward past this session. A store chunk is a unit inside which meaning must be preserved; you can't call it an arbitrary fragment of text of a given length. The choice of the cut's boundary is a decision that directly determines how many answers reach the requester intact and how many arrive torn in half; you can't set it "by eye" and forget about it. This holds true for any text-cutting tool: the chunking node in n8n is only one specific example here, the rule isn't limited to it.

This error is more dangerous than many others precisely because it's silent. The process doesn't fail, doesn't return an error, the execution log stays green — the model gets a piece of text and honestly answers based on what's in it. From the outside, everything looks like the system is working as expected. There's only one way to see the problem — compare the answer against what should have come out; which is exactly why, from the very start of this breakdown, a measurement with a known correct answer was needed — the subjective judgment "looks reasonable" doesn't work here.
