---
id: n43
type: content
duration_min: 0.5
assertion: "RRF adds up a document's scores from both lists — the most even-handed candidate comes out on top, and simply being first somewhere once isn't enough for that"
learning_goal: "An explicit request from the owner (issue #311): 'add an explanation to the case of what RRF is' — not just the formula's name (n42 already names that), but the mechanism in words and a numeric example on several documents, at a professional level, with no formula-as-literal-text on screen (15pt half-size type and the ban on scientific notation, §5.14 trebovaniya-k-soderzhaniyu-forma.md). Letter-suffix inserted before deck-wide renumbering (tools/seminar-production/README.md §1, issue #311), placed between n42 (actions, formula named explicitly) and n44 (fourth action, reranker) — RRF belongs to the third action (hybrid), not the fourth."
visual:
  pattern: content
  primary: >
    A principle-in-words tile + a table on three illustrative candidates:
    rank by words · rank by meaning · outcome after RRF. The numbers are a
    teaching illustration of the mechanics, not a measured result from the
    rig (measured numbers appear on n51/n58 later in this same case).
  backup: >
    k=60 is the real constant of the rig's merge node (`stend/measure/
    case3_measure.py`, the same node the real n8n panel later in this case
    draws in literal code). The three candidates' ranks are an invented
    teaching example, not a question from the corpus: chosen so that NONE
    of the three is first in either of the two lists (first place in both
    lists belongs to a candidate off-screen) — exactly the case where RRF
    is shown rewarding evenness, not first place in a single signal.
    Arithmetic: a document's score in a list = 1/(k+rank), k=60; the scores
    from the lists are summed; the winner has the largest sum. A:
    1/62+1/64=0.0318; B: 1/63+1/62=0.0320; V: 1/64+1/63=0.0315 — B wins by
    the smallest margin, not by a landslide, which is exactly what shows
    the mechanics honestly (not a rigged "convenient" example with a wide
    gap).
---

# How RRF computes a single list: an example on three candidates

## Assertion

RRF adds up a document's scores from both lists — the most even-handed candidate comes out on top, and simply being first somewhere once isn't enough for that.

## Visual

> **The principle in words.** Each document in both lists — by words and by embedding — earns a score: the higher the rank, the larger the score. The order is built on the sum of a document's scores from both lists at once.

| Candidate | Rank by words | Rank by meaning | Outcome after RRF |
|---|---|---|---|
| Candidate A | 2nd | 4th | 2nd |
| Candidate B | 3rd | 2nd | 1st |
| Candidate V | 4th | 3rd | 3rd |

> Candidate B was never first, either by words or by meaning — but it was never weak anywhere either, and that was enough to beat both rivals, each of which had one strong rank and one weak one.

## Speaker notes

The formula already has a name from the previous frame — Reciprocal Rank Fusion — but a name alone isn't a mechanism. Here's how it actually computes, in words and on numbers, with no formula-as-literal-text on screen.

Each document arrives at the merge with two ranks — its rank in the list by words and its rank in the list by meaning. Each rank is turned into a score: one, divided by the sum of a smoothing constant and the rank itself. The smoothing constant here is sixty — the very same number that, later in this same session, will literally sit in the code of the real merge node on the rig's canvas. It's chosen so that first place in a list means noticeably more than tenth, but without sharp jumps between neighboring ranks. A document's scores from both lists are added together, and the final list is built on that sum.

The three candidates on the frame are a teaching example for illustrating the mechanics — a question from the real corpus has nothing to do with it here. Candidate A stands second by words and fourth by meaning: it's almost the best on one signal, but noticeably weak on the other. Candidate B stands third by words and second by meaning: never first, but never weak either. Candidate V is fourth by words, third by meaning — weaker than both in the sum. The formula's count: A's score sums to 0.0318, B's to 0.0320, V's to 0.0315. B wins, and wins by the smallest margin, by thousandths of a point. This is exactly what a real merge usually looks like: it shifts the balance toward a candidate that's stable in both lists at once.

This also explains the hybrid's drawback, which we already named on the previous frame: if a document's full-text signal is weak but its vector signal is strong, two middling ranks sometimes pull the sum toward where a pure semantic search alone wouldn't have gone. The very same formula, with the very same constant k=60, will a few beats from now compute the merge on the real five hundred documents of the corpus — as a measured result.
