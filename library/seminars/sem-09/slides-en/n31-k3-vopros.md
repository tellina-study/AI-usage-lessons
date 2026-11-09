---
id: n31
type: question_with_option_cards
duration_min: 1.5
assertion: "Four actions, spanning a spectrum from 'the model checks itself' to 'code checks' and 'nobody checks, frequency decides'"
learning_goal: "Case 3's question: bare action cards, no verdicts, no cost, no solution composition (A6). Each card is a design choice — an action you can take — not a fact about a tool's capabilities (canon §5 for case design)."
visual:
  pattern: question_with_option_cards
  primary: >
    The question in a gold frame and a row of four equal-width cards laid
    out as a spectrum: on the left, the model does its own check; on the
    right, code or repeat-frequency. No explanations, no arguments, no
    annotations on the cards — the breakdown is the next screen.
  backup: >
    The cards are verbatim from SETKA-KEYSOV-S9.md, section "Case 3,"
    subsection "Question"; the wording is not rewritten. The framed
    question is also a verbatim line from there.

    Leak check (A6), passed for each card separately: not one names a
    verdict, not one names a cost, not one says how many model calls it
    takes, and not one hints that more than one is correct. There are no
    numbers from this rig at all on this screen (0 of 6, 5 of 5, three
    verdicts on one text) — those belong in beats n37 and n38. No external
    numbers either: those come a screen later, in the breakdown.

    Fact-frame check (case-design canon §5): every card already opens with
    an action verb — "ask," "ask," "run," "run." Not one turns into a
    statement about a tool's property ("the judge catches meaning but
    confuses order") — all four stay actions you can choose and build.

    The card order is a spectrum, not scrambled: the first keeps the check
    inside the same model, the second calls in a second model, the third
    doesn't call a model for the check at all, the fourth drops the idea of
    checking and replaces it with repeat-frequency.
---

# How to build a check on the answer before it's sent

## Assertion

Five requirements for the answer are written down and checkable. Who checks them, and with what, before the text goes out to the person?

## Visual

> **How do you build a check on the answer before it's sent?**

`ask the same model to reread its own answer and fix it if it sees a mistake` · `ask a second model (or the same one) which of two answer variants is better` · `run a deterministic check (a rule, a test, a schema) and only redo what failed it` · `run the model several times and take the answer that came up most often`

## Speaker notes

Five requirements for the answer are written down, and each one is checkable: length, the needed detail, a pointer to where to go next, no stray numbers, language. There's one question: who checks them, and with what, before sending. Four ways to build this.

The first — ask the same model to reread its own answer and fix it if it sees a mistake. This is Olga's own proposal, and it's the cheapest of all: nothing needs to be set up, just a second call to the same model with a different request.

The second — call in a judge. The model gets two answer variants and says which is better. The judge can be a second model, or it can be the same one, called separately, not told that it wrote both texts.

The third — write the check in code. A formal criterion: length, whether a needed word is present, a list of allowed numbers, a set of characters. Code decides whether to accept the answer or send it back for a retry, and only what failed the check gets redone.

The fourth drops the check and bets on quantity instead: run the model several times on the same question and send whichever answer came up most often.

Choose with one thought in mind. A month from now Olga shows up with a specific answer that went out to a person and turned out bad, and asks: why did this check let it through. Which of the four ways lets you answer that question by producing a reason? And which of the four gives you the same reason if you rerun the same answer again tomorrow?

The cards sit as a spectrum. On the left, the check is done by the very model that wrote the answer. Next, a second call to a model appears, now in the role of judge. The third option moves the check out of the model entirely, into code. The fourth drops the idea of checking altogether and replaces it with repeat-frequency. Fifteen seconds to choose, then we break down all four.
