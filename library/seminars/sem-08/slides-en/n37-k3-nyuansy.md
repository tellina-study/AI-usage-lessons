---
id: n37
type: criteria_checklist_and_boundary
duration_min: 1.5
assertion: "A calculator tool given to the model is not a guarantee and is measurably worse in practice; the threshold must live in exactly one place, not two copies; the extracting model can still make a mistake, and an explicit numeric field removes that part of the risk only if the form itself can be changed"
learning_goal: "Three nuances of Case 3; the calculator nuance is now backed by a real measurement (56/100), and card references were corrected after the question went from five cards to four."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    Three numbered banners, each a full-sentence nuance, not shortened to a
    headline.
  backup: >
    The calculator nuance is now backed by a real run of an agent with a
    genuine calculator tool on the same hundred requests (56/100) — worse
    than every other option, with new, unplanned-for failure modes. Card
    references were updated: the question now gives four cards, not five.
    Mirrors RU n37 (issue #274).
---

# Three nuances before applying the conclusion

## Assertion

"The decision must be code" is not an absolute guarantee, and not a reason to think the model is no longer needed at all.

## Visual

1. **A calculator tool for the model is not a guarantee, and in practice is measurably worse.** The probabilistic part doesn't disappear, it just moves one step earlier: whether the model calls the calculator at all, and how it passes values into it. Measured for real: 56 out of 100 — worse than every other option, with new failure modes (mixed alphabets in the answer, the tool not supporting comparisons, errors scattered across the whole range).
2. **The threshold X is the single source of truth.** If it lives in two copies — the prompt text and the `IF` condition — a mismatch between the two copies is the same class of problem as a broken contract between steps.
3. **The extracting model can still make a mistake.** The conclusion isn't "the model is never needed" — it's "the model must not be the decision point"; an explicit numeric field on the form removes this part of the risk too — but only if the request form itself can be changed; otherwise extraction remains the model's job.

## Speaker notes

Three nuances before carrying the case's conclusion away as an absolute rule.

The first is about the calculator, which we discussed among the question's four cards. Giving the model a tool for comparing numbers isn't the same as putting an `IF` node after extraction. Last time we only asserted this: the probabilistic part doesn't disappear, it moves one step earlier, to where the model decides whether to call the calculator at all and how to pass values into it. This time the claim was checked with a real run — we assembled an agent with a genuine calculator tool and ran it on the same hundred requests. The result turned out to be not just "no guarantee," but measurably worse than every other option: fifty-six correct answers out of a hundred. And failure modes turned up that nobody had specifically planned for: n8n's built-in calculator can't compare numbers, only do arithmetic, and in one case out of nine it honestly answered "I don't know how to do this"; a third of the agent's answers didn't even reduce to a clean word, "approve" or "escalate"; and almost a tenth of the errors were scattered across the whole range of amounts, rather than sitting neatly at the boundary the way version one's did. A tool given to the model is not a guarantee, it's a relocation of the problem — and now that's not just an argument, it's a number.

The second is about the threshold itself. Three thousand rubles currently live in two places: the version-1 prompt text and the version-2 `IF` condition. If the threshold ever changes — say, to three thousand five hundred — and someone fixes it in one place while forgetting the other, you get exactly the same problem as the contract between steps we already went through in earlier cases of this arc: two places that are supposed to match, with nothing guaranteeing that they do. The threshold must have exactly one source of truth.

The third, and it answers directly to the question card about an explicit numeric field on the form. A model that extracts an amount from free text can still make a mistake: read the wrong digit, confuse the amount in one sentence with the amount in another. This case's conclusion isn't "the model is needed nowhere in this process" — more precisely: "the model must not be the point where the decision is made." If the request form can be changed, an explicit numeric field removes the risk of incorrect extraction too — the amount arrives already structured, and there's no need to reconstruct it from text at all. But if the source is an email or a chat, rather than a form we control, extraction remains the model's job, and its own accuracy is a separate question that this solution doesn't close.
