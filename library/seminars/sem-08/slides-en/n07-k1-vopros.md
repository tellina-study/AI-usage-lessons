---
id: n07
type: question_with_option_cards
duration_min: 2.0
assertion: "Four actions, laid out as an explicit spectrum from full model freedom to full algorithmic assembly"
learning_goal: "Case 1 question: bare action cards, no arguments and no verdicts (A6, canon §5 — a design choice, not a fact)."
visual:
  pattern: question_with_option_cards
  primary: >
    The question in a gold frame and a row of four equal-width cards laid
    out as a spectrum: from "the model decides everything" to "the
    algorithm decides everything." No explanations or arguments on the
    cards — the breakdown comes later, on screen.
  backup: >
    The cards — verbatim from SETKA-KEYSOV-S8.md, section "Question to the
    room: how do you assemble the notification text from these three
    values?", not reworded. Each card names an action ("fill in," "call the
    model," "add"), not a fact about what the tool can do (canon §5).
---

# How to assemble the notification from three values

## Assertion

The name, the topic, and the extra topics are already known. How do you assemble them into one line of text?

## Visual

> **How do you assemble the notification text from these three values?**

`the model writes the whole notification text freely` · `we fill in a ready-made message form entirely by algorithm — substitution only` · `whatever the algorithm can close, it closes; whatever requires interpreting the request text, we call the model for that separately` · `we take the algorithmically assembled text as the base and add one phrase of tone from the model on top`

## Speaker notes

All three values needed to assemble the notification are already structured: the name, the main topic, the extra topics. The question isn't what to assemble — it's how.

The first card: the model writes the whole notification text freely. This is what Version 1 already does.

The second: we fill in a ready-made message form entirely by algorithm — just substituting values into a template fixed in advance, with no model call at all.

The third: a mixed option — whatever the algorithm can close (the values themselves), it closes; whatever requires interpreting the request text and wasn't extracted structurally in advance, we call the model for that, and only for that.

The fourth: we take the algorithmically assembled text as a solid backbone, and add one short phrase of tone or comment on top, composed by the model.

Don't choose by feel — estimate: which of the four approaches reliably produces text matching what Olga asked for, on any request, not just a lucky one.

Notice that the cards are laid out as a spectrum, not at random: on the left, the option where the model does all the work; on the right, where the algorithm does all the work; and between them, two mixed options, each splitting the work between model and code differently. This is deliberate: the question isn't "model or code," it's "how much of the work in this specific task actually requires interpretation, and how much is just substituting what's already known."

No card here is marked as obviously weak — each of the four has a situation, in principle, where it would be a sound choice. Today's question is tailored to Olga's need specifically, with her concrete text example and with already-structured values on input. For a different need, with a different set of known and unknown values, the answer could be different — worth keeping in mind while picking a card, but we'll break down this one, today's.

Fifteen seconds to decide, then let's see the cards.
