---
id: n47
type: question_with_option_cards
duration_min: 2.0
assertion: "Four ways to check that a picture matches the requirements before the file goes to Telegram — a direct continuation of the «model or code» axis, applied to an image"
learning_goal: "Case 4's question: not «what happens past the limit» but how to build the check. The cards split the mechanical check from the semantic one — the case's central methodological finding, continuing the session's axis. Cards are actions."
visual:
  pattern: question_with_option_cards
  primary: >
    The question in a gold frame, below it four cards of equal width,
    with no explanations and no highlight on the correct option.
  backup: >
    The cards are verbatim from SETKA-KEYSOV-S8-part2.md, section "Card
    in Telegram," the paragraph "Question to the room: how do you check
    that a picture matches the requirements?" — no rephrasing. The
    question was rewritten this wave: it used to be "how do you handle a
    picture that might turn out to be over the limit" — it became "how
    do you check that a picture matches the requirements," an explicit
    continuation of the session's axis.
---

# How to check that the picture matches the requirements

## Assertion

The run is green, and the card never reached the coordinator. The question isn't what happens past the limit — it's what check to build ahead of time.

## Visual

> **How do you check that a picture matches the requirements?**

`check the file's size and format before sending — in code` · `check that the picture opens without errors — in code` · `check that the picture actually shows what's needed — with a vision model` · `don't check anything — trust the sending node to handle it`

## Speaker notes

We just saw the finding: the run is green, and the card never reached the coordinator all the same. All day today we've been asking this chain the exact same question, over and over — does this step belong to the model, or does it belong to code. Let's apply that same question to the picture now.

The question on the screen: how do you check that a picture matches the requirements?

Four cards are on offer, and this is deliberately not the question "what do we do once the file goes over the limit" — it's a question about what check to build ahead of time, before the file goes any further down the chain at all. The first option — check the file's size and format before sending, in code: the same action, in essence, as the IF node in "Refund approval," just applied to a file's properties instead of a money amount. The second — check that the picture opens without errors, also in code: make sure the file is technically sound and not broken somewhere inside. The third — check that the picture actually shows what it's supposed to show, with a vision model: a different kind of task by its very nature, and it needs a fundamentally different tool to answer it. The fourth — don't check anything at all, just trust the sending node to handle it on its own: exactly what quietly happened in our scene.

Notice that the first two cards and the third one are different kinds of action underneath, even though all three are worded alike, as "check." Size, format, whether the file opens cleanly — these are properties you can count and compare directly against a number. Whether the picture's actual content matches what's needed — that question is no longer a number at all, it's meaning, and meaning doesn't compare the same way.

Choose not by whichever option merely sounds more reliable on first read, but by which tool is genuinely capable of running a check like that in practice: can the question be expressed as a plain condition over a number, or does it need someone — a human being or a model — to actually look at the content itself and judge it.

Fifteen seconds to choose a card, and then let's compare what everyone picked.
