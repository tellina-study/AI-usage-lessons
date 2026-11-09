---
id: n54
type: criteria_checklist_and_boundary
duration_min: 1.5
assertion: "Three classical defenses lower the cost of injection noticeably, but not to zero — and part of the remaining errors have nothing to do with injection at all, because they're rooted in the task itself that was handed to the model"
learning_goal: "Generalization and boundary of Case 4 (completely redefined 2026-10-29) in the plain imperative form (A7): 'when needed · when not' for the combination of three defenses, with a named limit of the approach and an external anchor on the cost of human confirmation and the execution channel. The session axis's fourth row closes here with a new wording."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A criterion as its own tile on top, below it a two-column "when
    needed · when not" table for the combination of defenses, then a
    tile on the approach's limit, a tile on human confirmation, a tile
    with documented cases about the execution channel, and a line
    closing the session axis's fourth row.
  backup: >
    The criterion and both columns of the table are this case's own
    measured material (`stend/zamery-k4-novyy/README.md`): 11 of 64
    residual errors in the best defended configuration, 64 of 64 for the
    rule in code (n51a), 31 of 64 manager escalations from the
    mechanical check (n49), 28 of 34 vs 5 of 34 catch rates for the
    mechanical check and the classifier separately (n50/n52).

    The external numbers and cases are the same as in the earlier
    edition, from `CHISLA-SVERENO.md`, and they still apply to the NEW
    setup without change: line 56 (Anthropic, confirmation telemetry
    ~93%), line 57 (four cases of a difference in execution channel).
    Both fit the new framing without strain — a refund, as in the earlier
    setup, has a real execution channel, so the divide of "did the step
    have authority or not" remains the same watershed.

    THE AXIS'S FOURTH ROW — the closing wording was checked VERBATIM
    against the left column of n04/n76/SETKA-KEYSOV-S9.md: "three
    classical defenses against injection — so text manipulation is
    closed."
---

# When three classical defenses are enough, and when they aren't

## Assertion

The defenses lower the cost of injection noticeably. The error born from the task's own construction remains — its source lies in the rule handed to the model, and defenses against injection don't touch it.

## Visual

> **Criterion.** Combine three classical defenses where the rule can't be fully computed by code. Where it can, its place is in code, not the prompt — no defense replaces that.

| When combining defenses is needed | When something else is needed |
|---|---|
| The rule requires understanding unstructured text — it can't be computed by code | The rule is entirely computable (a lookup + comparing dates, amounts) — then its place is in code: the code-only baseline already showed this |
| The business can accept the load on the manager (31 of 64 for the mechanical check alone) | The load is unacceptable — then the mechanical check alone isn't enough |
| The classifier is added TOGETHER with another defense | The classifier as the only layer — its own catch rate of 5 of 34 is too low |
| The decision has a real execution channel — money, a document, access | The step only drafts text that a human will read and decide on |

> **Limit of the approach.** Even the best combination leaves 11 errors out of 64 — none of them an attack. A defense against injection doesn't cure the model's error on the task itself.

> **The execution channel decides the cost of a miss.** Two cases with no real access (a one-dollar deal, a bot that badmouthed a company) cost nothing. Two cases with a real channel cost the companies dearly. A human isn't a cure-all either: a major provider's own telemetry shows about 93% of confirmations go through without a real look.

> **The axis's fourth row is closed.** "Three classical defenses against injection closes text manipulation": not confirmed. The best combination holds 0 of 34 attacks, but 11 of 64 errors remain, and none is manipulation.

## Speaker notes

Let's gather the case into a wording that can be carried off and applied to your own process.

The criterion is this. Three classical defenses are worth combining where the rule, by its own nature, requires understanding natural-language text — and can't be computed by code. Where the rule can be reduced to a lookup and a comparison, as in our own case with the client list and the course date, its place is in code, not in a defended prompt: we just saw that code on this same task gives 64 correct decisions out of 64 with not a single model call.

Now the boundaries, both sides stated plainly. Combining defenses is worth it where the load on the manager is acceptable to the business — for the mechanical check alone that's 31 requests out of 64, nearly half the flow, and that has to be accepted explicitly in advance, not discovered later. The classifier is worth adding only together with another defense: on its own it holds five attacks out of thirty-four, not enough to be the only layer. And if the decision has a real execution channel — money goes out, a document is sent, access opens up — the defense is worth it; if the step only drafts text that a human will read and decide on, there's not much worth substituting there.

The limit of the approach — and this is the most important thing to carry away. Even the best of the eight combinations we assembled leaves 11 errors out of 64, and we just went through this in detail: not one of these eleven has anything to do with manipulation. A defense against injection, by definition, can't cure the model's error on the task itself — these are two different sources of a miss, and fighting one with a tool meant for the other makes no sense.

Two outside observations still hold for this setup too. On confirming every request with a human — a major provider's own real telemetry shows about ninety-three percent of requests get confirmed, and the more of them there are, the less attention each one gets: routine human review remains one more imperfect layer alongside the structural defense, not a replacement for it. And on the execution channel: what sets apart a harmless mistake from a costly one is whether the step had real authority to act — the question isn't which model made the error. Our case has that authority: the money genuinely goes out, and that's what turns the whole breakdown into a question of cost.

Back to the session's axis. The fourth row said this: three classical defenses against injection — so text manipulation is closed. Not confirmed. The best combination really does hold zero successful attacks out of thirty-four. But eleven errors out of sixty-four remain, and not one of them is manipulation.
