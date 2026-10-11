---
id: n41
type: answer_breakdown
duration_min: 1.5
assertion: "Not one of the five means speeds up all six pieces: the parallelism lies in the task, and in this one there is exactly three pieces' worth of it — subagents take it where it exists and multiply the error where it does not"
learning_goal: "The turn of the case, named as a turn. The room's guess counted workers: six pieces, six workers. The breakdown moves the cause of the gain off the number of workers and onto a property of the task, and lays the five means out across the pieces each of them works on. Form A5 — two substantive columns"
visual:
  pattern: answer_breakdown_table
  primary: "A table of five rows in two substantive columns: what it does / what it does not do — the limit. Under the table — the turn plate, in gold: the number of independent pieces set next to the number of workers the room said out loud."
  backup: "Owner's round 5 (issue 225, ZADANIE-KRUG-5.md): a breakdown of five means instead of a breakdown of four variations on one means. The turn of the case is preserved verbatim and remained the headline of the slide — \"The parallelism lies in the task\": it survived the shift into a practical exercise, because the room now runs up against the dependency of the pieces itself. The numbers 17.2 and 4.4 are deliberately NOT brought up here — they stand on n47 and n49, where the source and the conditions of measurement are named; here they are only pointed to ahead. The row about several sessions in one folder is deliberately held to a single clause: the folder and file conflicts are the zone of the neighboring case of this rung, and unfolding them here would mean taking content away from it (handed over as a line in qa/krug5-subagent-keys2.md)."
---

# The parallelism lies in the task

## Assertion

Not one of the five means speeds up all six pieces. Three pieces are independent, and each of the rest needs a means of its own.

## Visual

| Means | What it does | What it does not do / the limit |
|---|---|---|
| lay it out and do the pieces one at a time | one predictable order, nothing collides with anything | three independent pieces wait for each other for no reason: the waits add up |
| run the pieces in several sessions | the pieces go at the same time, each session has a context of its own | two sessions in one folder edit the very same files — for us that is the field and the error messages, one `src/validate.js` |
| hand the pieces out to subagents and launch them at once | the harness provides the concurrency, there is nothing to configure; each subagent has its own context and a short result | it takes the parallelism where it exists: on the field and the messages, two subagents will see different versions of one file |
| move the repeating part into a check that runs itself | the pre-release run leaves the queue altogether — it is not a human doing it | the check has to be written in advance and once; on Friday, when the task has already arrived, it will only speed up the next task like it |
| narrow the task down | the campaign needs the field and the consent — two pieces out of six | that is not decided by the person doing the work: narrowing can be done by whoever is answerable for the deadline |

> **The turn.** Not one of the five means speeds up all six pieces. The parallelism lies in the task, and in this one there is exactly three pieces' worth of it: subagents take it where it exists and multiply the error where it does not — on the piece that reaches into somebody else's file, and on the piece standing in a queue. Set two numbers side by side: the number of workers you said out loud, and the number of independent pieces the layout produced.

## Speaker notes

Five means and six pieces. Let us go through each means: what it does and where it stops working.

**Do the pieces one at a time.** The order is single and predictable, the pieces cannot collide. The cost — three independent pieces wait for each other for no reason at all, and the waits add up. On six pieces a queue costs more than any other order, and it is also the only one that never breaks.

**Run the pieces in several sessions.** The pieces go at the same time, each session has its own context and its own conversation. The move stumbles at the same spot the layout found: the field and the error messages live in one file, `src/validate.js`, and two sessions in one folder will both reach it. What fixes that is a separate decision point later in the seminar; here what matters is the fact of the overlap itself, because it decides the choice between this card and its neighbor.

**Hand the pieces out to subagents and launch them at once.** The concurrency is provided by the harness itself: there is nothing to configure, each subagent has its own context and a short result on the way out. This means works where the parallelism already exists in the task — on the three independent pieces. On the piece that reaches into somebody else's file, two subagents will see different versions of one `src/validate.js`; on the piece standing in a queue, the second worker will be waiting for the first and taking up room while it does.

**Move the repeating part into a check that runs itself.** The pre-release run leaves the queue altogether: it is not a human doing it, and it repeats without the worker's participation as many times as you like. The move has a hard condition: a check like that has to be written in advance and once. On Friday, when the task has already arrived, it will only speed up the next task like it — writing it for this one is too late, and that is the honest price of the move existing at all.

**Narrow the task down.** The campaign needs the field and the consent — two pieces out of six. The other four do not have to be done by Monday at all, and that is cheaper than any speeding-up. This is decided by whoever is answerable for the deadline, so the move requires a conversation with them.

Now the turn the case was assembled for. Not one of the five means speeds up all six pieces. The parallelism lies in the task, and in this one there is exactly three pieces' worth of it: subagents take it where it exists and multiply the error where it does not — on the piece that reaches into somebody else's file, and on the piece standing in a queue behind another.

This is where the number written down in the exercise comes in useful. Set it next to the three independent pieces. Most often the number written down is six — one worker per piece — and the discrepancy with three shows what people usually count from: the amount of work they would like to hand out. What has to be counted from is a property of the task.

Independence can be checked cheaply and in an engineering way, with no theory at all. Two questions: do the pieces overlap on files, and does one need another's result. Different files and not a single shared dependency — the pieces are independent. The same file, a shared module, "first we rename, then we fix the calls" — dependent, and from then on they are worth reading as one job.

The number of workers does not turn out to be beside the point — it stands second. It sets the ceiling of the gain, while the gain itself is given by the independent pieces. Where there is no independence, raising the number of workers changes sign and starts working against you: instead of one job there appear two plus the seam between them. The easiest way to hold it is in this order: first count the independent pieces in the task, then set up workers — exactly as many as the pieces you counted.

Where "multiply the error" comes from — from a measurement, which comes later in the case together with its source and the conditions of the experiment. For now the direction is enough: dependent steps, divided between different workers, lose the connection the next step was supposed to see.
