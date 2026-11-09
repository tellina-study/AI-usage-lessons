---
id: n07
type: question_with_option_cards
duration_min: 1.0
assertion: "Three actions for a growing base — none is named the winner in advance"
learning_goal: "Case 1's question: bare action cards, no verdicts, no cost, no solution composition (A6). Each card is a design choice (design canon §5), not a fact about a tool's properties."
visual:
  pattern: question_with_option_cards
  primary: >
    The question in a gold frame, three equal-width cards, no arguments
    and no verdicts. The breakdown comes as the next screen.
  backup: >
    The cards are verbatim from SETKA-KEYSOV.md, Case 1, "the audience
    question": three actions, not facts about a tool's capabilities
    (design canon §5 check — an imperative verb fits into each one:
    "keep appending," "search," "put").
---

# How to build a knowledge base that grows

## Assertion

The base grows from ten items to hundreds of documents. How should the process keep finding the answer in it?

## Visual

> **How to build a knowledge base that grows?**

`keep appending the base to the same prompt` · `search by keyword` · `put it in a vector store and pull out the needed chunk`

## Speaker notes

Three actions, and none of them is flagged as obviously weak. Read them again: keep appending the base to the same prompt is exactly what we did last session, just with more items. Search by keyword is classic full-text search, with not a single call to the model: the question is compared against the documents' text directly. Put it in a vector store and pull out the needed chunk means the base is turned in advance into numeric representations of meaning, and a query finds whatever is closest in meaning, with no exact word match needed.

Don't choose by which option looks more technically modern. Think it through this way: in six months the base will have grown from ten items to five hundred documents — which of the three actions will still give a fast, cheap answer, and which will start to slow down or simply stop working?

Fifteen seconds to choose, then show of hands. The breakdown of how each action actually works comes as the next screen; the numbers that test this breakdown in practice come after that, on the measurement's structure and on the result itself.

All three actions solve the same task by different means, and none of them requires changing the rest of the process — the request-intake form, how the row gets written, the notification to Olga. The difference sits in exactly one place in the chain: where the model gets the fact it answers from. Keep that in mind: the next screen has concrete numbers at concrete base sizes, and the choice that looks right at ten documents may turn out very different at five hundred.

One more observation before you vote. The first action needs no preparation at all in advance — the base just sits as text in the process's settings. The second and third need a separate step before the first question ever arrives: the base has to be either indexed by word or turned into numeric representations of meaning. That's not a minor detail — it means the choice between actions affects not only how the process will behave when questions come in, but also how much work has to be done before the first one of them does.
