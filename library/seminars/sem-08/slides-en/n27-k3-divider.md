---
id: n27
type: case_divider_quote
duration_min: 0.5
assertion: "The training center approves small refunds itself and escalates large ones to the manager; the decision splits them by amount"
learning_goal: "Case 3 divider. The title names the task ('Refund approval'), not the lesson. The quote states the business rule ('automatic refund up to a set amount'), not the literal model prompt — the literal prompt is shown later, on n34, for contrast."
visual:
  pattern: case_divider_quote
  primary: >
    Dark background, the business rule large and centered. Below it, the
    four-case track of the session, the third one highlighted.
  backup: >
    The quote used to be the literal text of the version-1 prompt ("Rule: do
    not automatically refund more than 3,000 rubles, otherwise escalate to
    the manager"); the owner asked for it to read as a business rule instead,
    with no technical detail. The literal prompt text is not removed from the
    deck — it appears later, on n34, in direct contrast with the IF-node
    setting. Mirrors RU n27 after this round's edits (issue #274).
---

# Case 3. Refund approval

## Assertion

The training center accepts refund requests. It must approve a small amount itself, and hand a large one to the manager. The decision about what counts as "small" splits them by a single threshold.

## Visual

> "Automatic refund — up to a set amount. Above the threshold — only through the manager."

## Speaker notes

The third case of the day, and the subject shifts from text to money. In the first case we decided how to assemble a notification from values we already knew. In the second — how to tell a repeat question from a new one. Here the decision rests on a single number: the amount of the refund.

The training center accepts refund requests — a missed class, a course that did not fit, a change of mind. Part of these requests the center must approve on its own, without pulling the manager into every small case: this is routine work, and it needs to be handled fast, without approvals from above. Another part — the large amounts — must go to the manager without exception: there the cost of a mistake is higher, and the decision cannot be left uncontrolled. A threshold splits these two categories: three thousand rubles.

Why it can't simply all go to the manager, or all be handed to automation, needs little explaining. If every case is handled by hand, the manager drowns in small requests and has no time left for what actually needs them. If automation is trusted with absolutely everything, a large amount can go out without a single human glance — and where the count runs into the tens of thousands, that is a risk nobody takes on knowingly. The threshold is the compromise between these two extremes, and how precisely it holds is what decides whether the compromise works in practice or only on paper.

The phrase on the screen is not a technical prompt or an instruction to the model — it is how the business would state this idea before handing it over for implementation: automatic refund — up to a set amount. This is a direct continuation of the process we already built in Seminar 7: there the system read the text of a request and determined its topic; here it goes one step further — once a request is recognized as a refund request, the same system decides whether to approve the amount automatically or pass it to the manager. Not two separate processes, but one process with an extra step added.

Inside this step the rule sounds simple and, at first glance, entirely unambiguous — there is a threshold, there is a comparison, what could possibly go wrong.

It is exactly this seeming unambiguity that will turn out, under testing, to be incomplete. But let's not get ahead of ourselves: first let's see how this rule lives today and who carries it out — next screen.

The case track at the bottom of the screen — third of four; after this the session moves to a business case with a similar story at a different scale, and then to the last, fourth case of this session.
