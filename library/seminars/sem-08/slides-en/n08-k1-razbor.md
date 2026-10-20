---
id: n08
type: answer_breakdown_table
duration_min: 2.0
assertion: "Three of the four actions solve a problem Olga no longer has: every value was already extracted, so there's nothing left to interpret"
learning_goal: "Breakdown right after the question (A1), 4-column form 'action · how it works · advantage · drawbacks' (A5, owner's voice edit 2026-10-20, issue #274, replaces the earlier 2-column form — README.md §3/§8.3 already updated in the same wave). No 'right/wrong' verdicts."
visual:
  pattern: answer_breakdown_table
  primary: >
    A table: action · how it works · advantage · drawbacks. Four rows, no
    verdict column — the decision comes on the next screen.
  backup: >
    Text condensed from SETKA-KEYSOV-S8.md, section "Breakdown", not
    reworded in substance, fit into the 4-column form (A5, a new owner
    decision, not a restoration of an old canon — see README.md §8.3).
    References to the practice finding ("we saw this in practice") are
    removed from this beat and moved forward, to the real-runs beat (n13) —
    at this point in the breakdown, the finding hasn't been shown to the
    room yet (owner's voice edit 2026-10-20, issue #274).
---

# What each action actually does

## Assertion

None of the four is a mistake by itself. The difference is whether it's left with work that genuinely needs doing.

## Visual

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| **the model writes the whole text** | gets three already-extracted values and freely composes the notification text, with no fixed form | the text sounds alive, not like a canned phrase — it can write like a human | the values are already extracted — there's nothing to interpret; the text is re-assembled on every run, with a risk of slipping in a detail that wasn't in the request |
| **the algorithm fills in the whole form** | substitutes three already-structured values into a template text fixed once, with no call to the model | the result is deterministic: it matches the given text example on any request, not just a lucky one | no room for variability: if the message form ever needs to change in meaning, not just in values, the expression has to be rewritten by hand |
| **algorithm + model for what requires interpretation** | structured values are substituted by the algorithm; whatever stayed unstructured and requires interpreting the request text is passed to the model separately | would work honestly for a genuinely mixed case — where at least one value really requires interpretation, not just is already known | for this specific need, there's nothing to interpret: all three values, including urgency, were already extracted structurally last session — there's simply no work left for the model here |
| **algorithm + model's tone on top** | an algorithmic backbone of text is assembled by substitution, and the model adds one short phrase of tone or comment on top | the scope of freedom is smaller than in the first action — the risk and cost of calling the model are correspondingly lower | the same kind of risk as the first action, just smaller in scale: the model still generates text and can slip in a detail that wasn't there |

## Speaker notes

Let's break down the four actions in order, and I'll say this up front: none of them is foolish — each has a situation where it would be the right choice. The question is which situation we actually have in front of us.

First — the model writes the whole text. It can do that, no question, and the text comes out alive, not like a canned phrase. But look at what it has on input: all three values — name, topic, extra topics — are already extracted, structured, and sitting ready. The model has nothing to interpret, literally nothing to add to what's already known. And since it still generates text freely on every run, it keeps a chance of slipping a detail into the message that wasn't in the request — we'll see this on a real run shortly, not in theory.

Second — the algorithm fills in the whole form. This is exactly the amount of work actually needed: the three values already exist, the message form is always the same, and there's essentially no variability required. The result predictably matches the text example Olga asked for.

Third — the mixed option, algorithm plus model only for what requires interpretation. The idea is sound on its own, and it would work if the request had at least one value that needs to be inferred from the text — the degree of urgency, say, if it hadn't been extracted explicitly as a word. But in our chain, urgency already exists as a separate structured field, from last session. There's literally no work left for the model here — this is a solution for a different need, one we don't have right now.

Fourth — an algorithmic backbone plus a phrase of tone from the model on top. This is a scaled-down version of the first option: the model still composes something, just less of it. The same kind of risk remains, just at a smaller scale.

Which action actually meets our need — next screen.
