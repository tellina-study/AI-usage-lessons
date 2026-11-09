---
id: n12
type: measured_outcome_table
duration_min: 1.5
assertion: "On the three questions in the 'topic entirely absent' group, version 1 honestly admitted it didn't know — 0 made-up answers out of 3"
learning_goal: "Breakdown of the 'topic entirely absent' group (C2, beat 3) — continues n11a, the test's design is already shown. The case's turn (P1) starts here: the expectation 'the model will confidently lie' isn't confirmed, and the slide states the measured, not the expected. A verdict on every example (C3)."
visual:
  pattern: measured_outcome_table
  primary: >
    A tile with the headline pair "3 questions outside the knowledge base
    · 0 made-up answers," below it a table of the three questions with
    verbatim answers and an explicit verdict column (C3), and a separate
    callout at the bottom about a side finding from the same run, on a
    fragment in another language.
  backup: >
    All three questions and all three answers are verbatim from
    `stend/README.md`, section "Version 1 — free answer," runs 609, 610,
    and 611. Three more questions from the same run (606, 607, 608) asked
    about topics that ARE in the knowledge base, and the answers to them
    are correct per the knowledge base — hence the base fact "3 of the 6
    asked were outside the knowledge base."

    The side finding — run 607, the question about documents: the answer
    is correct on the merits but unfit to send: in the middle of the
    Russian text sits a fragment in Chinese characters instead of the
    words "copy of the spread" [passport pages]. The same class of
    failure was observed on the Seminar 8 rig, in the calculator-tool
    variant — two independent observations across two sessions
    (ARCHITECTURE.md, "Side finding from the same run, goes into the case
    as-is"). The fragment itself isn't reproduced on the slide: on the
    frame it would be meaningless Latin-rendered-as-glyphs for the room;
    naming the phenomenon is enough.

    Run numbers don't appear on the visible layer (BRIEF §2) — they're
    here, in the production documentation.

    The phrase "easy case" is named directly on the slide and explained by
    its own trait ("the topic doesn't exist at all"), not left as a
    judgment call: canon §8.11 requires a zero to be shown together with
    the trait that makes it easy, or it reads as a property of the model.

    THE VERDICT COLUMN WAS ADDED by the 2026-10-29 edit (C3): previously,
    the correctness of each answer had to be worked out by comparing the
    question to the answer in your head. Now every row carries an explicit
    "CORRECT."
---

# Three questions outside the knowledge base: what version 1 answered

## Assertion

Version 1 honestly wrote, on all three, that the knowledge base had nothing on it. The expectation that it would confidently lie wasn't confirmed.

## Visual

> **Group "topic entirely absent from the knowledge base" · 3 questions · 0 made-up answers**
> Of the six questions asked in this run, three asked about topics entirely absent from the knowledge base; the other three are answered correctly per the knowledge base.

| Question | What version 1 answered | Verdict |
|---|---|---|
| "What loyalty program do you have for returning clients?" | "Our knowledge base has no information about a special loyalty program for returning clients. If you have questions or suggestions on this, I can pass them on to the training center's staff." | **CORRECT** |
| "If I bring a friend to the course, do we get a discount?" | "Our knowledge base doesn't provide for a referral discount. If you have other questions or need help, I'd be glad to assist!" | **CORRECT** |
| "Is there a free demo class before buying the course?" | "Our knowledge base has no information about a free demo class before purchasing the course. If you have such a request, it's best to contact the administrator to clarify the options." | **CORRECT** |

> **Why this case is easy.** In all three questions, the topic is entirely absent from the knowledge base: there's not a line about loyalty, about a referral, or about a demo class. There's simply no nearby item to build an answer from.

> **A side finding from the same run.** One of the answers to a question whose topic IS in the knowledge base is correct on the merits — and unfit to send: in the middle of the Russian text sits a fragment in Chinese characters instead of two Russian words. We saw the same failure on last session's rig. Two observations across two sessions is no longer a coincidence.

## Speaker notes

The first run. Six questions through the real form on the rig, three of them about topics entirely absent from the knowledge base: the loyalty program, a referral discount, a free demo class.

Here's what we expected: that a model with no knowledge-base coverage on the question would still confidently answer something. That didn't happen. On all three, it honestly wrote that there was no such information in the knowledge base, and offered to pass the question to staff. Zero made-up answers out of three.

This is an honest result against our own hypothesis, and we're showing it as it is. But before concluding "so it can be trusted," look at exactly which questions were asked. The topic is entirely absent from the knowledge base in all three — there's not a line about loyalty, about a referral, or about a demo class. The model had nothing to build from: the nearest item simply doesn't exist. This is the easy case, and its zero is a property of the chosen questions just as much as it's a property of the model.

So the conclusion from this is a different one, and it's stronger. The self-report worked in this run. The question is what exactly guarantees it will work on the next one — and the answer is: nothing in the process's design promises that. The decision lives inside the composed text, nobody checks it, and the only way to find out whether it worked is to read the answer by eye after it's already gone out.

And one more thing from the same run, unplanned. One of the answers — to a question whose topic IS in the knowledge base — is correct in substance, but in the middle of the Russian sentence there's a fragment in Chinese characters instead of two Russian words. You can't send that to a client. We observed exactly the same failure on last session's rig, on a different process and a different task; two independent observations is no longer a one-off oddity. Remember this as a separate property: an answer can be correct in substance and unfit to send, and a "correct per the knowledge base" check won't catch that.

Next — the same process, but on harder questions.
