---
id: n38
type: criteria_checklist_and_boundary
duration_min: 0.75
assertion: "Chunk size doesn't behave monotonically on its own — checking against your own data is needed for any size choice"
learning_goal: "Nuances and boundary for Case 2 in direct form (A7): the open item about overlap is now closed with a measured number, not a third hypothesis. The session's second axis line closes here, now on the material of four measured versions."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A tile on size non-monotonicity, a tile on the partial gain from
    overlap and from word-boundary cutting, a tile closing the session's
    second axis line.
  backup: >
    SETKA-KEYSOV.md / rework/section-2-razbienie-dokumenta.md,
    "Nuances", verbatim. Overlap was measured by the follow-up run of
    2026-11-02 (`stend/raw/case2-results.json`, a local Python
    measurement on the same 60 documents/72 questions, not a live n8n
    call) — the previous version of the slide's open item is now closed
    with a number, not dropped as a question.
---

# What a fuller measurement showed

## Assertion

Overlap and word-boundary cutting reduce version 1's share of broken answers, but not to version 2's level.

## Visual

> **Chunk size doesn't behave monotonically on its own.** For version 1, the share of broken answers doesn't fall smoothly as chunk size grows: 9.7% → 12.5% → 4.2% → 6.9% → 2.8%. Choosing a "nice-looking" size doesn't guarantee quality — checking against your own data is required: a borrowed empirical rule doesn't carry over.

> **Overlap gives a partial gain.** At the headline size, adding overlap cuts version 1's share of broken answers almost in half — from 12.5% to 5.6%. It doesn't close the gap to version 2's level (1.4%).

> **Word-boundary cutting shows the same picture.** At the same size, the share of broken answers drops from 12.5% to 8.3% — the word is protected from being torn, the sentence still isn't.

> **The session's second axis line is closed:** a document CAN technically be cut into chunks any way you like — but what share of future answers arrives intact depends directly on this, and cheap fixes for the symptom reduce that share without removing it.

## Speaker notes

Next — the nuances of this fuller measurement.

The first: chunk size alone doesn't behave monotonically. Intuition suggests that the larger the chunk, the smaller the chance of a break at a random boundary. We've already seen by the numbers that this isn't so: version 1's share of broken answers jumps up and down moving from one size to the next, not falling smoothly. The practical conclusion from this: choosing a "nice-looking" value for the chunk-size parameter — say, because it's a round number or because that's how it's done in someone else's project — guarantees nothing on its own. Checking against your own data is needed for any choice.

The second nuance is something that used to be an open question and is now measured. Adding overlap between neighboring chunks reduces version 1's share of broken answers noticeably — at the headline size, almost by half, from twelve and a half to five and six tenths percent. This is a gain confirmed by measurement. But the gap to version 2's level, one and four tenths percent, still doesn't close: overlap fixes part of the cases where the cut falls exactly on a phrase boundary, but doesn't change the fact that the chunk boundary itself is still set without regard for the text's meaning.

The third nuance — cutting by word boundaries behaves similarly. It protects an individual word from being torn and reduces the share of broken answers from twelve and a half to eight and three tenths percent at the same chunk size. But protecting a word isn't protecting a phrase: the cut can still fall between two words of the same sentence, exactly where the answer to a question begins.

The general lesson of these two additional versions: a word isn't the unit that's responsible for protecting meaning — that's the sentence's job. Both overlap and word-boundary cutting treat the symptom — the fact that an answer sometimes doesn't fit whole into one chunk. The cause of the symptom stays the same: the chunk boundary is set without regard for the text's boundary of meaning.

And so the session's second axis line is closed — now on the material of four measured versions. It looked reliable that a document could be cut into pieces however you like, as long as the chunk made it into the store. It turned out: where the cut falls directly decides what share of future answers reaches the requester intact, and what share arrives torn in half; cheap fixes like overlap or word-boundary cutting reduce that share, but don't remove it, and the difference between them and a careful cut by meaning is still counted in multiples.

Before moving to the next case, it's worth fixing the link between this breakdown and the previous one. The first case decided where to store the base. The second decided how to prepare it so that the storage units carry complete meaning. Together, the two decisions give a store where chunks are both cheap to find and safe to read on their own — but neither of them yet answers the question of how to actually find the needed chunk among many others just like it. That's the next, separate step.
