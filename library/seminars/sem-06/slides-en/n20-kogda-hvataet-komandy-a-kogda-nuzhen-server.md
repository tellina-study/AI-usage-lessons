---
id: n20
type: criteria_boundary
duration_min: 1.0
assertion: "MCP is needed when access is required regularly, from several sessions, and the agent itself decides when to reach for the source; it is not needed when a snapshot of the data is enough, when the task comes down to a known CLI call, or when the connection completes the third element of the lethal trifecta"
learning_goal: "The generalization of the case, straight by rule A7 (issue 225, round 2 — the owner: \"write: when MCP is needed, when it is not needed, outright and clearly, people should not have to guess\"). The frame \"too early / not needed at all\" was removed entirely — both columns speak about the mechanism itself, not about the stage of the decision. A natural transition to the next case, not a declaration of the axis"
visual:
  pattern: criteria_checklist_and_boundary
  primary: "A table in two columns: \"MCP is needed when\" and \"MCP is not needed when\", four rows in each, mirrored line by line. Under the table — a transition line to the next case, with no unfolding into a declaration of the synthesis."
  backup: "Source — rework/section-1-mcp.md §A.1.11, §B.11 (part1c.md). The title is verbatim from the plan (items 16/18 of the cross-check: its own title on every limit, not a general frame).
    Round 2 of the owner's edits (issue 225, part A7, the line-by-line breakdown of n20): the
    previous titles \"Too early (waiting for a signal)\" / \"Not needed at all (not a question of
    the moment)\" were removed entirely — the owner outright forbade that frame for a section's
    conclusion. The columns were renamed to \"MCP is needed when\" / \"MCP is not needed when\", and
    the contents were regrouped so as to mirror line by line (it was: 4 items of \"early\" + 2 items
    of \"never\" as separate blocks; it became: 4 rows, each with a positive condition on the left
    and its mirror opposite on the right). The stop criterion of the lethal trifecta was moved into
    the right column (\"not needed\") as a direct condition rather than as a special item inside
    \"early\" — by content it is exactly the same limitation as before, just without the division
    into \"waiting for a signal\" and \"a structural property\". The facts and figures did not change,
    only the layout.
    The storytelling revision (issue 225, P1/P6): the third row of the table is named through the
    list of operations — the thing that, by the case's turn (n12, n18), the standing cost is paid
    for; the criterion thereby closes the turn rather than standing next to it. The content of the
    row is the same: regularity, the growing number of operations, the agent's decision in the
    moment. The slot went 0.75 → 1.0, and the speech was cut from 165 words (1.27 min against a
    slot of 0.75) to 130 (1.00 min); what was cut went into the reference material."
---

# When MCP is needed, and when it is not

## Assertion

MCP is needed when access is required regularly, from several sessions, and the agent itself decides when to reach for the source. It is not needed when a snapshot of the data is enough, when the task comes down to a known CLI call, or when the connection completes the third element of the lethal trifecta.

## Visual

| MCP is needed when | MCP is not needed when |
|---|---|
| access is needed regularly, from several sessions — a one-off snapshot of the data is not enough | access is one-off or rare, and a snapshot of the data as of today is enough |
| you are prepared to maintain one more permanently running process with access to secrets | there is no such readiness — then a one-off call is more reliable than a process nobody services |
| there is more than one operation, the list of operations is growing, and the agent itself decides which one to reach for — it is for that list that the standing cost is paid | the task comes down to one known CLI call: a list of capabilities is surplus here, and the thirty-two-fold difference in tokens is not going anywhere |
| the connection does not complete the third element of the lethal trifecta | the connection does complete the third element of the lethal trifecta — access to private data and the processing of someone else's text are already there, and what remains is a channel to the outside; this is a stop criterion |

> There is access to the outside, and there is something with which to prove the agent uses it. The next question is what being connected costs in itself, while nobody has reached for the server at all.

## Speaker notes

The conclusion of the case, outright: when MCP is needed and when it is not. Four rows on each side, and the rows are mirrored — one and the same quantity from both ends.

Needed — when access is required regularly, from several sessions, and a snapshot as of this morning is already not enough. Needed — when you are prepared to maintain one more permanently running process with access to secrets. Needed — when there is more than one operation, the list of them is growing, and the agent itself decides which one to reach for in the moment: it is precisely for that list that the standing cost is paid, and a server is justified exactly when the list is worth its price. And needed — only if the connection does not complete the third element of the lethal trifecta.

Not needed — in the mirror cases. Access is one-off or rare: a snapshot of the data is enough. There is no readiness to maintain a live process: a one-off call is more reliable than a process nobody services. The task comes down to one known CLI call: a list of capabilities is surplus here, and the thirty-two-fold difference in tokens is not going anywhere. And if the connection completes the trifecta — that is a stop criterion at once, with no deliberation.

The columns are named outright, with the words "needed" and "not needed", and that was done deliberately. Formulations like "too early" or "not needed at all" invite you to guess which stage of the decision is being discussed, and they hide the answer behind a shade of meaning. There is one question here: is a server needed for this task or not.

The right column refers to the task. There is no verdict on the mechanism itself in it: the same server is surplus for one piece of work and necessary for the next, and that is settled anew every time, by the four rows of the left column.

The mirroring of the rows works here as a check: every right-hand row is obtained from the left-hand one by negating one quantity, and nothing else. The first pair measures frequency, the second readiness to keep a process, the third the number of operations, the fourth the composition of the trifecta. If your case does not fit either side of some pair, then the quantity has been named inaccurately, and it is the quantity you have to deal with, not the conclusion.

How to apply the criterion to your own project today: take one action you repeat by hand every week and walk down the four rows of the left column. If even one of them does not hold, the connection can wait. The answer meanwhile changes over time, and more often towards "needed": a one-off action becomes a regular one imperceptibly — exactly as, in our scene, carrying an issue over from the tracker became a habit in a month.

A separate case — the trifecta is complete and the access is needed anyway. Then you break the trifecta. Narrow the permissions down to one repository, remove the channel to the outside, move the reading of someone else's text into a separate session with no access to private data — any one of the three legs is enough, and you pick the one that comes cheaper for the work.

And the discipline after connecting, without which the criterion runs out of breath in a month: re-read the configuration periodically and remove the servers that are not used. Every forgotten server is at once a tax on the context, an attack surface, and a holder of keys.

There is access to the outside, and there is something with which to prove the agent uses it. The next question is what being connected costs in itself, while nobody has reached for the server at all.
