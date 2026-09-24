---
id: s37
type: criteria_boundary
duration_min: 1
assertion: "A flat file is enough as long as the history of decisions fits into the context in full and there are no links between the entries yet"
learning_goal: "The \"too early here\" criterion for a flat file + the explicit boundary where DECISIONS.md stops coping — the transition to case 2.2"
visual:
  pattern: criteria_checklist_and_boundary
  primary: "A six-item checklist on the left. On the right/below — the statement of the boundary to the next case."
---

# The "too early" criterion and where a flat file ends

## Assertion

A flat file is enough as long as the history of decisions fits into the context in full and there are no links between the entries yet.

## Visual

Checklist — if most of the items hold, a complex memory system is not needed:

- The task is one-off, there will be no second session on this context.
- All the context you need fits into a single context window without loss.
- The project's rules are stable and fit into an instruction file shorter than 200 lines.
- Nobody is manually repeating the same edit or clarification from session to session.
- There are not several participants who need to share context asynchronously.
- The fact is derivable from the code or from the change history.

Below — the explicit boundary to the next case: a flat `DECISIONS.md` stops coping when there are so many entries that finding the one you need by reading linearly takes longer than re-explaining the decision from scratch — and links have appeared between the entries, for which there is physically nowhere to put them in an append-only log.

## Speaker notes

The criterion — off the checklist, out loud, briefly.

Then the boundary is named directly: a flat file stops coping not instantly and not because of size in itself, but when two conditions hold at once — there are so many entries that finding the one you need by reading linearly takes longer than recalling and re-explaining the decision from scratch, and links have appeared between the entries for which there is physically nowhere to put them in a flat append-only log: decision number seven cancels part of decision number two, and next to decision number two there is not a word about it. This is not "we need a vector database" — this is exactly the next case: the very same decision log, only grown and now requiring structure.
