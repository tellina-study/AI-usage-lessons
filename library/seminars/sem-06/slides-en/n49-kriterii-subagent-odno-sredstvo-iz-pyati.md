---
id: n49
type: criteria_boundary
duration_min: 1.25
assertion: "A subagent is one means out of five, and it is justified where there are several pieces and they are independent; on dependent steps, on a repeating piece and on a piece that is not needed for the deadline, another means is cheaper — and getting the count of workers wrong cost our developer a week of working one piece at a time"
learning_goal: "The close of the case: the industry's reversal + the axis line with its cost + the criterion by which a subagent is chosen among five means, all on one slide. The cost is twofold and the second part matters more: the bug in front of the client cost an hour, the wrong count cost a week of refusing a working technique. Rule A7 of round 2 — stated directly, nothing left unsaid"
visual:
  pattern: criteria_checklist_and_boundary
  primary: "A short plate at the top — the industry's reversal of opinion (10 months, two narrow patterns, the \"swarm\" still not recommended), in one paragraph. Below — the axis plate with the cost of a week. Below that — a table in two columns, the same grammar as the rung's other boundaries (n20/n28/n59). The axis line has a thick gold bar on the left, no fill."
  backup: "The sources are section-2-subagent-part1a2.md §A.2 \"The criterion\" + section-2-subagent-part1c.md n48/n49, verbatim in substance and in figures (Cognition, 2025-06-12 → 2026-04-22, a difference of ten months — a fact-check round-2 correction, kept; 17.2 and 4.4 — Google Research, arXiv:2512.08296). Owner's round 5 (issue 225, ZADANIE-KRUG-5.md): the right-hand column of the criterion stopped being a column about a superfluous coordinator and became a column about the OTHER MEANS — \"it's not only subagents there, after all\" was written straight into the criterion, as two rows, about a repeating piece and about a piece that is not needed for the deadline. The refusals \"a coordinator is superfluous\" and \"merging is superfluous\" moved in here from the removed fifth row of n46. The axis line was rewritten around the exercise: the guess counted workers, the layout named the condition. The facts, the figures and the sources did not change. Slot 1.75 → 1.25 (half a minute given to the n39 exercise), the speech trimmed to the slot."
---

# A subagent is one means out of five. Where it is justified

## Assertion

A subagent is justified where there are several pieces and they are independent. On dependent steps, on a repeating piece and on a piece that is not needed for the deadline, another means is cheaper.

## Visual

> **The industry's reversal, as a marker of the boundary.** A year ago one team rejected multi-agent work outright, calling an unstructured "swarm" a distraction. Ten months later that same team came back to two narrow patterns — a review chain (a separate subagent finds on average two bugs per edit, of which about 58% are serious) and a pairing of two different top models on complex scenarios. The boundless "swarm" it still calls a distraction.

> **The parallelism lies in the task.** The guess counted workers: six pieces, six workers. The layout named the condition: three pieces are independent, and each of the rest needs a means of its own. Getting the count wrong cost our developer a week of working one piece at a time — including the pieces that divided quite happily. Reconciling the diverged configurations cost longer than the configuring itself; trust in the technique cost a week.

| A subagent is justified when | Another means is cheaper when |
|---|---|
| there are several pieces and they are independent — one's step does not need another's output | the steps are dependent: splitting multiplies the error — 17.2× with no coordinator, 4.4× even with centralized checking |
| each piece has its own narrow zone and a short result — the lookup list and the form are exactly this case, once what is shared between them has been written down before the start | nobody wrote down what is shared between the pieces: two honest jobs add up to a readiness that does not exist |
| — | a piece repeats after every one of the others: its place is in a check that runs itself |
| — | a piece is not needed for the deadline at all: a piece like that gets narrowed away, and there is nothing in it to speed up |

## Speaker notes

Where is the line past which coordination itself becomes the cost. The marker of that line was planted by the industry, and planted twice in the same direction.

A year ago one team rejected working with several agents outright, calling an unstructured "swarm" a distraction and explaining publicly why. Ten months later that same team came back to this work — to two narrow schemes. The first: a review chain where a separate subagent finds on average two bugs per edit, and about 58% of them are serious. The second: a pairing of two different strong models on complex scenarios. The boundless "swarm" this same team still calls a distraction. The reversal is valuable precisely because of who made it: people who paid for both positions in practice came back to two narrow schemes, leaving the general case rejected.

The criterion that folds out of this is as follows. A subagent is justified when there are several pieces and they are independent — one's step does not need another's output. The lookup list and the form fall into this case when what is shared between them — the names, the composition and the required flags of the fields — has been written down before the work starts.

Another means is cheaper in four situations, and every one of them turned up in the task we laid out. The steps are dependent: splitting multiplies the error — 17.2 times with no coordinator and 4.4 times even with centralized checking. Nobody wrote down what is shared between the pieces: two honest jobs add up to a readiness that does not exist. A piece repeats after every one of the others: its place is in a check that runs itself. A piece is not needed for the deadline at all: a piece like that gets narrowed away, and there is nothing in it to speed up.

How it ended for the developer in this story. For a week after the divergence he did everything with one subagent, one piece at a time, including the pieces that divided quite happily. The reconciling of the diverged configurations itself cost longer than the configuring took. Trust in the technique cost a week of working one piece at a time, and that is the second cost, which here matters more than the first.

The difference between those two failures is worth separating out. A failure of the technique is fixed by one line in the subagent's description. A failure of the count taken off the technique is fixed only by somebody naming the condition out loud again — and until that moment a working means lies idle. The developer remembered the count of workers; the condition under it he did not, and the week went on that.

How he found the condition in the end: he sat down and wrote a shared description — the very one that should have been written before the start, with the names and the composition of the fields in one place. That is exactly the technique from the previous screen, applied a week late. On his task it is worth noting separately: configuring the lookup list and the form with two subagents was in fact fine, which is where the decision to keep both of them and add a shared description came from. The mistake was the silence about what they shared.

Two reasons to set up a separate worker have been examined by this point: somebody else's context for a long read, and work at the same time on independent pieces. The third reason is about the subagent itself, and it comes next.
