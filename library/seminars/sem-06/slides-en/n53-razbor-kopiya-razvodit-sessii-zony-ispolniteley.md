---
id: n53
type: answer_breakdown
duration_min: 1.25
assertion: "All five moves work in their own cases; a copy of the repository divides sessions — a folder of its own and a branch of its own with a shared history — whereas inside one session there are no copies, and there the defense rests on the zone layout"
learning_goal: "A breakdown of all five cards in form A5 — two substantive columns, what it does / what it does not do. The conclusion is derived from the combination of the columns and separates two answers to the one word \"in parallel\": a copy for sessions, zones for workers inside a session. This is the landing ground for the turn of the case, which n58 and n59 prove"
visual:
  pattern: answer_breakdown_table
  primary: "A table of five rows in two substantive columns: what it does / what it does not do — the limit. The order of the rows matches the order of the question's cards. No row is highlighted: the conclusion goes as a separate line under the table."
  backup: "Form A5 — the same as the deck's other breakdowns (n12, n34, n41, n46). Round 5 (issue 225): the table was written from scratch along with the case. The facts in row 4 (what in a copy is its own and what is shared) and in row 3 (a subagent works in the directory of the calling session) come from the harness documentation, read by direct curl on 2026-10-07; the verbatim quotes and the analysis are in qa/krug5-subagent-keys3.md §5; on this slide they stand as consequences, the mechanics in full come a screen later (n54, n56)."
---

# A copy divides sessions. Inside a session you divide zones

## Assertion

All five moves work in their own cases; a copy of the repository divides sessions — a folder of its own and a branch of its own with a shared history — whereas inside one session there are no copies, and there the defense rests on the zone layout.

## Visual

| Move | What it does | What it does not do / the limit |
|---|---|---|
| commit before every switch | gets back what was lost: there is something to come back to, and somebody else's commit is visible in the history | the branch in the directory stays one for everyone; you learn about a collision after it |
| work one at a time, in one session | removes the collision entirely: one job in the directory, one branch, one worker | the second task stands waiting while the first runs — the very queue the previous case got away from |
| subagents in the first session instead of a second session | removes the argument about the branch: subagents work in the same branch, and the task does not have to be explained from scratch | their directory is shared by design, so the argument about the file stays where it was |
| a copy of the repository of its own for every session | gives each one its own files and its own branch with a shared history: a switch by one under the hands of another changes nothing | the copy has to be brought up as a working environment — dependencies, files outside version control; the work still has to be brought together by a branch |
| divide by files and agree on it | works where there are no copies: inside one session, between its workers | rests on the zones genuinely not overlapping — one shared file cancels the agreement |

> **Conclusion.** A copy of the repository divides sessions: a folder of its own, a branch of its own, a shared history. Inside one session there is nothing to divide with — the workers share the directory by design, and the defense there rests on the zone layout. One word, "in parallel", two different answers, and the rest of the case covers both.

## Speaker notes

The breakdown goes through all five moves. For each one, what it does and where its limit is are named; out of the combination of the two columns the conclusion assembles itself.

**Commit before every switch.** It gets back what was lost: there is something to come back to, and somebody else's commit is visible in the history. The branch in the directory meanwhile stays one for everyone, and you learn about a collision after it has happened. A legitimate choice where collisions are rare and recovery is cheap.

In the repository history it looks like this: somebody else's commit sits there, inside it are files the author of the commit never touched, and working out what came from where has to be done by file names. Everything can be recovered; what has to be spent is the time of whoever does the working out.

**Work one at a time, in one session.** It removes the collision entirely: one job in the directory, one branch, one worker. You pay in time — the second task stands waiting while the first runs, and that is the very queue the previous case was getting away from. A legitimate choice when the second task really can wait.

**Subagents in the first session instead of a second session.** It removes the argument about the branch: subagents work in the same branch as the session, and the task does not have to be explained from scratch. Their directory is shared by design, so the argument about the file stays where it was. This is half an answer, and its mechanics are taken apart by the screen about subagents in one folder.

**A copy of the repository of its own for every session.** It gives each one its own files and its own branch with a shared history: a branch switch by one under the hands of another changes nothing. The copy has to be brought up as a working environment — dependencies, files not under version control; the work still has to be brought together by a branch. Which is why the move "then always a copy of its own" has a cost: on a thirty-second typo fix, bringing a copy up costs more than the fix itself.

**Divide by files and agree on it.** It works where there are no copies: inside one session, between its workers. It rests on the zones genuinely not overlapping, and one shared file cancels the agreement entirely. There is almost always such a file — in this case it will play its part on the failure screen.

The conclusion assembles itself out of the fourth and fifth rows. A copy of the repository divides sessions: a folder of its own, a branch of its own, a shared history. Inside one session there is nothing to divide with — the workers share the directory by design, and the defense there rests on the zone layout. One word, "in parallel", two different answers, and the rest of the case covers both.

The question that comes up here immediately: why do subagents not get a copy of their own, if sessions do. They can get one — with a single line in the subagent's description. It is done rarely, and the reason is examined at the end of the case, where the cost is visible. For now it is enough to know that there is no prohibition here.

Two of the five moves do not cancel each other. A copy per session plus a zone layout inside each — that is how people most often work, because these moves answer different questions: the first about what two sessions see, the second about what the workers of one session see.

The "one at a time" row does not contradict the previous case. There it turned out that the parallelism lies in the task itself: if the work divides, a queue is an expense with no gain. Here the cost of parallelism is named — what gets paid for it in space. Both lines describe one decision from different sides.

The right-hand column of the table is the condition of use for each move. A move that has what it does not close named stays a working one: you simply know where it ends. A move with no such line looks like a promise of safety, and it is on promises exactly like that that parallel builds break — which is visible on the failure screen.
