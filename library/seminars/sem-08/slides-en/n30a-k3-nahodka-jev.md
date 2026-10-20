---
id: n30a
type: failure_vignette
duration_min: 1.5
assertion: "The proposal to pull the amount out with the jev service and compare it to the threshold in code could not be built as intended — the jev service structurally does not return an open-ended number, only a quantized answer"
learning_goal: "An honestly-reported dead end: an idea tested on the live rig and found not to be buildable as proposed — not a less-accurate option, but a structural capability gap in the jev service, placed right after the four-action table and before the version-2 solution diagram."
visual:
  pattern: failure_vignette
  primary: >
    A three-block vignette, top to bottom: the proposed idea · what the
    live-rig test showed (the decisive 2,999/3,001 test) · how this differs
    from the calculator on the previous screen, and the lesson. No accuracy
    percentage — there isn't one here by construction, not by omission.
  backup: >
    Source: a diagnostic protocol of three real calls through a temporary
    workflow on the live rig, removed after the test. The numbers quoted
    (2,999 and 3,001 rubles; the four jev response types — yes/no with
    probability, single choice, scale position, image region) are exactly
    what the protocol recorded. No accuracy percentage is invented or
    measured — the task never reached the stage where accuracy could be
    computed, and that is the content of the finding. Mirrors RU n30a
    (issue #274).
---

# Testing an idea: the jev service for extracting the amount

## Assertion

The idea was a reasonable one — hand off the amount extraction to a specialized service that, in the neighboring case, already outperformed a general-purpose model. A live-rig test showed: this particular service is not a fit for extracting a number — not worse, but structurally unable.

## Visual

> **The proposed idea.** Pull the refund amount out not with a general-purpose model, but with the specialized jev service — the same one that, in Case 2, told a repeat question from a new one — and still leave the threshold comparison to code, the same `IF` node already chosen by version 2.

> **What the test showed.** The jev service has exactly four response types: yes/no with a probability, a choice from a fixed list of options, a position on a predefined scale, a region on an image. An open-ended number is not among them. The decisive test: amounts of 2,999 and 3,001 rubles — on opposite sides of the real 3,000-ruble threshold — both came back with the same scale bucket, with full confidence. The service did not tell them apart. The only way to tell them apart would have been to build the bucket boundary at exactly 3,000 in advance — that is, to know the threshold at the moment of framing the question to the service, exactly as in the version-1 prompt text.

> **How this differs from the calculator.** With the "give the model a calculator tool" action (previous screen), the model COULD call the tool — the probabilistic part didn't disappear, it just moved one step earlier. With jev in this task, the operation "return an open number" simply does not exist in the API at all — this isn't a job done poorly, it's a job the service structurally does not take on.

> **The lesson.** First verify that a service can actually do what you want from it, and only then design the step around it — not the other way around.

## Speaker notes

Before moving on, it's worth telling you about one idea that came up after the table on the previous screen was already finished, and which did not make it in as a fifth row — not because anyone shied away from it, but because testing showed it could not be built the way it was conceived.

The idea sounded reasonable. We already have the specialized jev service — the same one that, in the previous case, told a repeat question from a new one better than a cheap judge model. Why not use it here too — to pull the amount out of the request text, while still letting code compare it with the threshold?

Before assembling the chain, the idea was checked with direct calls on the live rig — you cannot make up a number, you have to measure it. And it turned out: the jev service has only four response types — yes or no with a probability, a choice of one option from a predefined list, a position on a given scale, a region on an image. An open number isn't among them at all, in any form.

The decisive test showed why this isn't a minor point. Two amounts, 2,999 and 3,001 rubles, sit on opposite sides of the real three-thousand-ruble threshold. Both were given the same predefined scale of ranges. The service returned the same range for both, with full confidence each time — it did not tell them apart. Telling them apart would have worked only if the range boundary had been hard-coded at exactly three thousand in advance — that is, if the threshold had to be known at the moment of framing the question to the service, exactly as in the version-1 prompt text, which is the very thing we're trying to get away from.

This is a different story from the calculator we went through a minute ago. With the calculator, the model could call the tool — the probabilistic part simply moved one step earlier and kept living there. With jev, in this particular task, the operation "return a number" simply does not exist in the service's interface — this is not a poorly performed job, it is a job of a different class that the service doesn't take on at all.

The lesson is simple and general, not just about refunds: before designing a step around a third-party service, you first have to verify it can physically do what you want from it — not assume that because it's good at a neighboring task, it will fit here too. "Choose from ready-made options" and "extract an arbitrary number" are different classes of task, and success at one says nothing about the other.

Now — what we actually did with this finding: a solution that replaces exactly the node where the mistake happens. That's the next beat.
