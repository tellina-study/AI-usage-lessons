---
id: n57
type: question_with_option_cards
duration_min: 1.5
assertion: "Five actions on the node and the prompt, each one sounding like a way to get the same answer"
learning_goal: "Case 5's question beat: bare action cards, pro-argument only, with no hint that none of them solves the task directly (A6). Owner's 2026-10-27 edit: 'seed' was dropped (it doesn't exist on the node, as n59 shows), and few-shot and description-in-the-prompt were added."
visual:
  pattern: question_with_option_cards
  primary: >
    A question in a gold frame and a row of five equal-width cards. None
    is marked, none carries a counter-argument — the breakdown comes on
    the next screen.
  backup: >
    The first three cards are verbatim from SETKA-KEYSOV-S9-part2.md,
    section "Case 5", subsection "Question" (seed was dropped in the
    owner's 2026-10-27 edit — it doesn't exist on the rig's node, see
    n59). Two new ones — few-shot and description-in-the-prompt — were
    added by the same edit, measured by
    `stend/zamery-k5-povtorno/run_fewshot_desc.py`.

    Checked for leaks (A6), passed card by card: none names a verdict.
    All the measurement numbers live in beats n60–n62; this beat doesn't
    touch them.

    Card order — five independent knobs an engineer tries one after
    another, not points on one scale.
---

# How to Get the Same Answer to the Same Question

## Assertion

Five actions on the node and the prompt — all five sound like a way to get the same answer.

## Visual

> **What to do so an identical question gets an identical answer?**

`lower the model's temperature to zero — zero sounds like "switch off randomness"` · `pin a specific model provider in the node's settings instead of automatic selection` · `in the structured-output schema, put the "reasoning" field before the "answer" field` · `add several question-answer examples to the prompt — few-shot, the model learns from a sample` · `add an explicit explanation of the rule to the prompt`

## Speaker notes

Olga asked for one thing: that the process answer an identical question identically. Let's translate that into the language of node settings and the prompt — there are five things that come to mind first for anyone who's ever configured a language model.

The first — lower the temperature to zero. It sounds literal: zero is "switch off randomness," and the setting's own wording reads exactly that way. It sits in the node's panel on the very first line under the model selector, and touching it is the most obvious of all five actions.

The second — pin a specific model provider in the node's settings, instead of leaving automatic selection by price or availability. Pinning one looks like a sensible measure that removes this variable entirely.

The third is built differently: it's not about randomness in the call itself, it's about the structure of the answer. In the structured-output schema, you can put the "reasoning" field before the "answer" field, so the model first explains in words what it's doing and only then gives the final text.

The fourth and fifth concern the prompt itself — they don't touch the node's panel. The fourth — add several question-answer examples, few-shot: the model sees a sample and, in theory, repeats its logic on the new question. The fifth — add an explicit explanation of the rule to the prompt: a direct explanation, with not a single example, of where the boundary runs.

Notice: all five cards describe an action. None is marked with a plus or a minus, and none names a verdict about the model itself in advance. What each of the five actions is worth in practice — the breakdown comes next.

These five weren't chosen at random: these are exactly the actions an engineer names first if they've ever configured a language model by hand, and exactly what gets tried in practice before throwing up one's hands and admitting that none of them solves the task directly. The next breakdown doesn't hand down a verdict on all the cards at once — it takes them one at a time and honestly counts the cost.

Fifteen seconds to choose, then show of hands.
