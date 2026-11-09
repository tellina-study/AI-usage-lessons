---
id: n07
type: question_with_option_cards
duration_min: 1.5
assertion: "Five actions, spread from 'the model decides everything' to 'string comparison decides, no model at all'"
learning_goal: "Case 1's question: bare action cards, no verdicts, no cost, no description of the solution's parts (A6). Each card is a design choice — an action you could take — not a fact about a tool's capabilities (case-design canon §5)."
visual:
  pattern: question_with_option_cards
  primary: >
    The question in a gold frame and a row of five equal-width cards laid
    out as a spectrum: on the left "the decision lives entirely in the
    model", on the right "there's no model in the decision at all", the
    fifth card is a separate approach (searching an external store) next
    to the spectrum. No explanations, arguments, or notes on the cards —
    the breakdown comes on the next screen.
  backup: >
    The cards are verbatim from SETKA-KEYSOV-S9.md, section "Case 1",
    subsection "Question"; the wording hasn't been rewritten. The question
    in the frame is also a verbatim line from there.

    FIFTH CARD ADDED by the 2026-10-29 edit (BREAKDOWN, K1-4): "missing the
    external-knowledge-base (RAG) option — add it so we can explicitly
    rule it out at this stage: the base is small." The card holds the same
    A6 neutrality as the first four — it names an action ("search an
    external store"), not a conclusion about it; the argument itself
    ("the base is small, no need to search") belongs in the breakdown
    (n08), not here.

    Checked against leaks (A6), card by card: none names a verdict, none
    names a cost, none lists what the solution it's building is made of,
    and nowhere does it say how many answers are correct. The rig's own
    numbers (0 of 3, 6 of 15, 4 of 15, 2 of 15) are absent from this screen
    entirely — they belong in beats n11a, n12, n13, and n16.

    Checked against the "fact frame" (case-design canon §5): each card is
    put in an imperative verb — "let the model decide", "compare by
    string", "put grounding in a field", "ask for confidence as a number",
    "search an external store." None of them turns into a statement about
    the tool's properties ("the model grasps meaning but confuses similar
    things") — all five remain actions.

    Card order is a spectrum, not scattered: the first hands the decision
    entirely to the model, the second never calls the model at all, the
    third and fourth split the work between the model and code in two
    different ways. The fifth stands last as a separate axis (knowledge-
    base size), not a continuation of the same spectrum.
---

# How to build the "answer myself or hand off to a human" decision

## Assertion

There's a ten-item knowledge base. The question arrives as arbitrary text. Who, and by what means, decides whether this question is covered by the knowledge base or not?

## Visual

> **How do you build the "answer myself or hand off to a human" decision?**

`the model gets the whole knowledge base and the whole question, decides on its own — answer on the merits or honestly decline — and writes the answer text itself` · `the client's question is compared by exact match against a list of ready-made knowledge-base topics, with zero model calls` · `the model assigns the question to one of the known knowledge-base items (or explicitly — to none), and then code decides by a condition whether to answer or hand off to a human` · `the model answers freely and also names a number — how confident it is in its own answer — and code hands off to a human everything below a set confidence threshold` · `the needed item is searched for in an external store, and only the retrieved fragment is given to the model`

## Speaker notes

The knowledge base already exists — ten items, the same ones Olga carries in her head. The question arrives as whatever text a person writes. One thing needs deciding: does the knowledge base close this question or not. Five ways to build that.

First — hand the decision to the model entirely. It gets the whole knowledge base and the question, and in one call decides on its own whether to answer on the merits or honestly decline, and writes the answer text itself. No separate machinery around it at all.

Second — no model at all. The question is compared by exact match against the knowledge base's list of ready-made topics: a match, and we answer with the fixed text; no match, and we hand off to a human.

Third — split the work. The model does exactly one thing: it assigns the question to one of the known knowledge-base items, or explicitly says it belongs to none of them. Code then decides — by an ordinary condition — whether to answer or hand off to a human.

Fourth — leave the model a free-text answer, but also ask it to name a number: how confident it is in that answer. Code then decides, by a set threshold, what goes to the client and what goes to Olga.

Fifth, separate from this spectrum: search an external store for the needed item and give the model only the retrieved fragment, instead of putting the whole knowledge base into the call. This solves a different problem — the problem of a large knowledge base that doesn't fit into one call at all. Whether it stays in the running for a ten-item knowledge base — that's the breakdown, next screen.

Don't choose by which option looks the most modern. Think of it this way instead: a month from now Olga comes to this process and asks about a specific request — why it was answered on its own and she wasn't called. Which of the five ways gives an answer to that question you could actually show? And which one gives it every time — on any next request, not just this one?

The cards stand as a spectrum. On the left, the option where the decision lives entirely inside the model. On the right, where the model has no part in the decision at all, and string comparison does the work. Between them, two options that split the work between the model and code, but split it differently: one asks the model for an item's name, the other for a confidence number. The fifth card is a separate axis, about knowledge-base size, not the same division of labor.

None of the four is marked as obviously weak, and that's not politeness: each one has a task where it would be the sensible choice. Today's question is exactly matched to Olga's need, with her ten-item knowledge base and an answer that goes straight to the requester. Fifteen seconds to choose, then show of hands.
