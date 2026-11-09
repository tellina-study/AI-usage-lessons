---
id: n61
type: question_with_option_cards
duration_min: 1.0
assertion: "Three actions for finding a similar scan — none of them named as a failure in advance"
learning_goal: "Case 4's question: three action cards, no verdicts (A6), including the option the breakdown will later honestly call unworkable — the card stays neutral, the failure is revealed by the breakdown, not by the question."
visual:
  pattern: question_with_option_cards
  primary: >
    The question in a gold frame, three equal-width cards, no arguments and
    no verdicts.
  backup: >
    Cards — SETKA-KEYSOV.md Case 4, "Question to the room," meaning kept.
    The third card is reworded by this edit (issue #311, owner's note
    "slide 57/58 — need to reword the third option and explain it more
    broadly"): "search for exact repeats by a separate, fast method" →
    "compare pictures by a short fingerprint, without calling a model."
    The old form named a narrow scope of use in advance ("exact repeats")
    — that's closer to hinting at a verdict than to a neutral action name
    (rule A6); the new one names the mechanism, not the outcome.
---

# How to search for a similar scan among the past ones

## Assertion

Three ways to compare images — by caption, directly, or by a separate fast method for exact repeats.

## Visual

> **How do you search for a similar scan among the past ones?**

`caption the picture in words and search as text` · `search the picture by the picture directly` · `compare pictures by a short fingerprint, without calling a model`

## Speaker notes

Three actions. Caption the picture in words and search as text — reuses the entire search mechanism we've worked through all session today; the only difference is that the text is now obtained by recognizing the image, instead of arriving ready-made from the client. Search the picture by the picture directly — compare the images themselves in their own numeric representation, with no text in between. Compare pictures by a short fingerprint — an action of a wholly different nature: the picture is shrunk and turned into a short bit string, computed locally, without a single call to a model; the closeness of two pictures is the number of matching bits between their fingerprints (Hamming distance). The fingerprint stores the picture's general look — its meaning plays no part in it, and that's exactly what decides whether it's any good for a given search task.

Think it through: what's lost when a picture is replaced by its text retelling — the layout of fields on a form, the visual look of a stamp, a handwritten note? And is comparing the pictures directly worth it?

Fifteen seconds to choose. The breakdown — on real scans from an open dataset.

This time, all three actions don't quite solve one and the same task, unlike the previous cases of this session. The first and second answer the question "does this scan look like one of the past ones by meaning," while the third answers a different question — "is this literally the same document, just scanned again." Keep that difference in mind while voting: the right answer doesn't have to be a single one of the three options.

One more hint for the vote, honest and without leaking a verdict: think about what physically happens to the picture in each of the three actions. In the first case, the picture turns into words and from then on lives in that form — the picture itself is no longer needed by anyone after that step. In the second case, the picture stays a picture the whole way through. In the third — it also stays a picture, but is compared by a short bit fingerprint of its general look: the meaning of the content takes no part in the comparison at all — the fingerprint doesn't know what's written on the picture, only what it looks like overall. This difference in what happens to the original data is exactly what decides what each method can, and fundamentally cannot, catch.
