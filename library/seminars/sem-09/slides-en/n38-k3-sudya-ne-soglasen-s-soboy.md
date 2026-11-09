---
id: n38
type: measured_outcome_table
duration_min: 2.0
assertion: "On the full 20×3 measurement, the judge got a BYTE-FOR-BYTE IDENTICAL text twice in a row and rendered two different verdicts — a rejection, then an approval, with not one changed character"
learning_goal: "The case's load-bearing frame, now on a stronger example from the full 20×3 measurement (previously: a similar but not identical text on 3 questions). The false rejection (n37) can still be blamed on a strict checker; here the checker disagrees with ITSELF on the EXACT SAME text — that removes the very possibility of leaning on it."
visual:
  pattern: measured_outcome_table
  primary: >
    Two steps, one under the other — attempt, the verbatim text, verdict,
    and reason — laid out so it reads as: the text between the two steps
    DID NOT CHANGE AT ALL. Below that, a second, confirming pair
    (certificate, from the earlier version of the frame, with one minimal
    phrase change) and a cost banner.
  backup: >
    The main example — `raw/zamer3-full-20.json`, `variants.judge`, the
    question "Can I write in the group chat..." (kb10), executions in the
    989–1008 range (see README § "Measurement 4"). Both answer texts match
    byte for byte (173 characters) — confirmed by a direct string
    comparison, not by eye.

    WHY THIS EXAMPLE IS STRONGER THAN THE EARLIER ONE (certificate,
    169/172 characters, one changed phrase): there, you could (mistakenly)
    guess that the judge reacted to the difference between "end of the
    course" and "the last class." Here there is NO difference at all — the
    same model call returned the same text, and the same judge call on the
    same text returned a different verdict. The only variable is the
    judge's own randomness.

    THE SECOND EXAMPLE (certificate) IS KEPT AS CONFIRMATION, not as a
    replacement: the same question that appeared on the earlier version of
    the frame, the same pattern of a false reason ("doesn't mention the
    detail," even though the detail is in the text verbatim), and the same
    almost-unchanged phrase between attempts. The n38 finding isn't a fluke
    of one run — it's reproduced on a new, wider sample.

    The cost is named with numbers from this same run: on the group-chat
    question — 1 extra loop, 2 extra calls (1 attempt instead of 2); this
    is cheaper than the earlier example (certificate — 2 extra loops), but
    the phenomenon is the same.
---

# One text, two verdicts

## Assertion

The text did not change by a single character. The verdict flipped from rejection to approval.

## Visual

> **Attempt 1, 173 characters.** "Reach out through the 'Messages' section of your personal account to the specific instructor. The answer will arrive within one business day. If you still have questions, contact the administrator." Verdict: **not good enough**. Reason: **"Doesn't explicitly mention the detail 'Messages'"** — the detail is in the very first sentence.

> **Attempt 2, 173 characters — byte-for-byte the SAME text.** Not a single changed character. Verdict: **good enough**. Reason: **"the answer meets all requirements."**

> **Confirmed on a different question (the same finding as on the earlier version of this frame).** "When will the certificate arrive after the course?" — attempt 1 (134 characters, "...within **5 business days** after **the end of the course**..."): not good enough, "doesn't mention the detail '5 business days'" — the detail is in the text verbatim. Attempt 2 (143 characters, "...after **the last class**...," almost the same text): good enough.

> **What it cost.** On the group-chat question — 1 extra loop, 2 extra model calls, for a text that never changed at all.

## Speaker notes

This frame is updated on the full measurement — and the example got stronger, not weaker.

The question about whether it's okay to write in the group chat. First attempt: the judge answers "not good enough" — the detail "Messages" isn't explicitly mentioned. It's in the text, in the very first sentence, word for word. Second attempt — and here's what matters: the generated text MATCHES THE FIRST ONE BYTE FOR BYTE. Not a single changed character, I checked directly, not by eye. The judge this time: good enough, meets all requirements.

Earlier, on the previous version of this frame, there was a similar example about a certificate — there, one phrase changed between attempts, and you could think the judge reacted to that difference somehow. Here there's no difference at all. The only thing that changed between the two attempts was the judge's own internal state, on an identical input.

And incidentally, that same certificate example reproduced on this run too, almost identically: the detail "five business days" is in the text, the judge says it isn't. This isn't a one-off — it's a pattern, visible a second time on the expanded sample.

The cost is small on this particular question — one extra loop, two extra calls. But the point isn't the cost. A checker whose verdict changes on an input that didn't even change isn't rejecting or passing deliberately — it's producing a random number. You cannot build a decision on a check like that, even when it's sometimes cheap.

It's worth telling this apart from ordinary strictness in a checker. A strict judge is predictable: it rejects borderline cases more often, and you can account for that by moving the acceptance threshold. Here it's different. The same input, on adjacent calls, gets opposite verdicts with no system to it at all — never the same thing twice in a row where the text genuinely didn't change. No threshold fixes this kind of randomness: move it in either direction, and the number of wrong verdicts doesn't become predictable, because it never depended on the content of the answer in the first place. The difference between strictness and randomness is what decides the main question here: can you trust the number a checker produces at all. A strict one — yes, with a discount for the strictness itself. One like this — no, no matter how many times you re-check it on the same text.
