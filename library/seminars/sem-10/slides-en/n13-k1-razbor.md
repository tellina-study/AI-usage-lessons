---
id: n13
type: answer_breakdown_table
duration_min: 0.75
assertion: "Appending everything to the prompt pays for volume the action doesn't have: accuracy gives no warning while cost grows, until the request fails outright"
learning_goal: "Breakdown right after the measurement results (an A1 derivative — here the breakdown follows the numbers, not the question directly, since the case's own S6 requires a multi-sided measurement all at once, not a sequential iteration). 4-column form 'Action · How it works · Advantage · Drawbacks' (rule A5), numbers from the previous screen. Part 1 of 2 (n14 — keyword and vector): split because the 15pt type floor leaves no room for three table rows on one slide (issue #311)."
visual:
  pattern: answer_breakdown_table
  primary: >
    A table: action · how it works · advantage · drawbacks. One row —
    "append everything to the prompt." Above it, a tile naming the model
    shared by all three of the case's actions.
  backup: >
    Breakdown text — SETKA-KEYSOV.md Case 1 / rework/section-1-khranenie-
    bazy.md, "Breakdown," fit into the 4-column form without rewording the
    substance. Numbers are the same as n10's, not repeated in full but
    folded down into a range.

    THE MODEL IS NAMED ONCE, FOR THE WHOLE TABLE (C5, on the model of
    `sem-09/slides/n08-k1-razbor.md`): all three actions end up calling
    `gpt-4o-mini` for the final answer — the only difference is which text
    gets passed to it (the whole base or one found chunk).
---

# What the measurement confirmed: appending everything to the prompt

## Assertion

Appending everything to the prompt isn't foolish — it's an action with a short shelf life: it works while the base is small; past that, it pays in volume.

## Visual

> **The model that forms the final answer in all three actions is the same one: `gpt-4o-mini`, with no explicitly set call settings.** Action 3 additionally uses `text-embedding-3-small` for the search.

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| Append everything to the prompt | The whole text of the base goes to the model, in full, on every question again | Accuracy holds at one level, 0.7, at 10/50/200 documents — with no visible warning signal | Cost grows 17.0-fold from 10→200 documents at the same accuracy; at 500 documents it doesn't work at all — the request exceeds the model's context, with no prior quality drop |

## Speaker notes

We've already gone through how each action works — here's what it came to as a number. We're going through the three actions in order, starting with the simplest in design. None of them is foolish: each one has a base size at which it would be a sensible choice. And before we even get to the difference between them — one thing they share: the final answer in all three actions is formed by the same model, `gpt-4o-mini`, with no specially set call settings anywhere. The model is the same everywhere; only the text handed to it before it starts answering differs.

Append everything to the prompt is the simplest in design: the whole text of the base goes to the model, in full, on every question again. At ten documents, at fifty, and at two hundred, accuracy holds at the same level, 0.7 — with no visible warning signal at all that the decision is about to fail. Meanwhile the cost keeps growing almost linearly with the number of documents the whole time: a seventeen-fold increase on the way from ten to two hundred documents, with no connection at all to what's happening with accuracy. And at five hundred documents the decision doesn't gradually get worse — it stops working entirely, instantly: the request physically doesn't fit into the model's context.

It's exactly this absence of a warning signal that makes the action treacherous for an engineer who sets it up on a small base: ten documents work, fifty work, two hundred work — nothing hints that a cliff is coming ahead: gradual degradation simply doesn't happen here. Appending everything isn't a mistake at a small scale — it's bound to be the first natural attempt, the thing you start with: the complexity of a store and a search isn't justified while the base fits in the context and costs a reasonable amount of money. The only question is exactly where that boundary sits, and that's what the rest of the breakdown is about.

Next — the two actions that, instead of appending everything, search only for the needed chunk.
