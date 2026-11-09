---
id: n66
type: question_with_option_cards
duration_min: 1.5
assertion: "Three ways to read a receipt photo — merge the reading and the cross-check into one call (an uncompressed or a compressed photo), or split them apart via classic text recognition"
learning_goal: "Case 6's question: bare action cards, no verdicts, no cost, no decision composition (A6). 2026-10-29 edit (issue #299): option 1 clarified — one model gets BOTH the photo and the request's text AT ONCE (a single call); option 2 — the same thing with a compressed photo; the fourth option (checking the answer's format) was removed — it isn't about HOW to read the photo, it's about what to do with an already-finished answer, and lives in its own beat, n73."
visual:
  pattern: question_with_option_cards
  primary: >
    A question in a gold frame and a row of three equal-width cards. No
    explanations, arguments, or hints on the cards — the breakdown comes
    on the next screen.
  backup: >
    The cards follow SETKA-KEYSOV-S9-part2.md, section "Case 6," subsection
    "Question" (2026-10-29 edit, issue #299). There used to be four
    options, now three: the fourth ("check the response format's
    validity") was removed from this screen — it isn't about reading the
    photo, it's about what to do with an already-finished model answer, and
    on the visible layer it would duplicate the question without its own
    fork in the reading mechanism. That same material occupies a separate
    beat, n73 ("format versus cross-check"), where it belongs.

    Checked for leaks (A6), one card at a time: not one names a verdict,
    not one names a cost, not one lists the composition of the decision
    being assembled, and nowhere does it say how many of the three ways are
    the right ones. The rig's own numbers (27 out of 30, 25 out of 30, the
    echo of the request on the heaviest resolution) are not on this screen
    at all — they belong in beats n70–n73a–n73e.

    Checked against the fact-frame rule (canon §5 of the case-design
    canon): every card uses an imperative verb form — "process," "compress,"
    "run." None of them turns into a claim about a property of the tool.

    Card order follows the case grid's order, not a spectrum: the first
    two are the same architecture (a single call) on an uncompressed and a
    compressed photo; the third is an architecturally different device (a
    separate recognition step before the model).
---

# How should the process read the receipt photo

## Assertion

The photo is there, and there's one question: what to do with it before asking the model to name the amount and the date?

## Visual

> **How should the process read the receipt photo?**

`process the request's text and the uncompressed photo together in one model, in a single call` · `the same thing, but the photo is compressed before sending` · `first run classic text recognition and build the model's request from the recognized text instead of pixels`

## Speaker notes

A photo of the receipt is already sitting in the request, next to the text where the client wrote the amount themselves. There's one question: what to do with this pair — the photo and the text — before getting an answer. Three ways to build this step.

The first is to hand the model both parts of the request at once, in one call: the photo without compression, and the text where the client stated the amount. The model, in this case, reads the photo itself and decides for itself whether what it read matches what was written — one request for the whole step, with no separate comparison operation outside it.

The second is the same device, but the photo is compressed before sending. A file from a phone is often heavier than it needs to be for one short receipt, and shrinking the size looks like a direct saving — a smaller file, less to pay for the call.

The third splits reading and understanding into two separate steps a different way: first the photo goes through classic text recognition — a separate tool with no connection to the model at all — and the resulting text goes on into the request to the model. The model, in this case, never sees the image at all, only the letters it's already been turned into.

None of the three options is absurd on its own. Each has a reasonable basis that would justify picking it: simplicity and savings on the call for the first two, division of labor for the third. How technologically impressive an option looks settles very little — what matters is what each one actually delivers and what it doesn't, once money and dates on a real, far-from-ideal photo are on the line.

What we have in front of us is a phone shot: there's no scanner anywhere in this story, and that condition is the same for all three ways. Which of them holds up against a crumpled sheet and uneven light, and which turns out fragile exactly where that's most expensive — the breakdown comes on the next screen.
