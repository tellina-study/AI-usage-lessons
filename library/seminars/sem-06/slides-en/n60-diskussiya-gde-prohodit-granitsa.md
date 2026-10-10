---
id: n60
type: reflection_question
duration_min: 2.0
assertion: "Two questions with no single answer: what has to be true for two pieces of work to be run in one folder, and how many workers with the right to write a team is prepared to keep there — the room answers, and the answer is named together with the condition under which it changes"
learning_goal: "The discussion that closes the case. The open part of the case is a direct requirement from the owner (round 5, issue 225: \"part of it could be made more of a discussion\"). The questions are chosen so that the answer depends on a team's circumstances and has no single correct form: the boundary between a zone layout and working one at a time, and the limit on the number of writing workers per folder. The slide carries no target answer and cannot carry one"
visual:
  pattern: reflection_question
  primary: "At the top, in a quiet form — a one-line lead-in: a copy divides sessions, zones divide workers. Below — a frame with two questions and the requirement to name the condition under which the answer changes. There are no option cards: here the options are not five, there are as many as there are working habits in the room."
  backup: "Round 5 (issue 225, ZADANIE-KRUG-5.md): \"part of it could be made more of a discussion\", and 2.0 minutes of the case's slot out of 11.25 were given to the discussion — together with the n52 vote the room talks for 2.75 minutes. The former n60 slide (the boundary of trimming permissions, the `code-reviewer` against `debugger` example from the documentation) was removed along with the specialization case; the fact from it stays in the foundation of the rung and in the chapter and does not come out into the deck any more. The form is a question frame with no cards: cards mean a choice from a named set, and here the set is brought by the room. This is the deck's second slide using the `reflection_question` pattern with no cards after n04 (the seminar's question), and they do one job — a question the room answers. IMPORTANT: this case no longer carries the rung's axis as a line on a slide (the former locked formula \"A custom role — we settle it, on a signal of repetition…\" was removed along with the case); the new wording for the axis lies in rework/section-2-subagent-part1a3.md § \"The axis line\", and section 3 takes it (n61, somebody else's zone) — see qa/krug5-subagent-keys3.md §7."
---

# Where the boundary runs for you

## Assertion

Two questions with no single answer: what has to be true for two pieces of work to be run in one folder, and how many workers with the right to write a team is prepared to keep there — the room answers, and the answer is named together with the condition under which it changes.

## Visual

> A copy divides sessions, zones divide the workers inside a session. Where one ends and the other begins is a matter for each team.

> **Two questions, and they have no ready answer. Name yours — and name the condition under which it changes.**

1. What has to be true about two pieces of work for you to agree to run them in one folder? And by what sign do you set up a separate copy rather than work one at a time?
2. How many workers with the right to write are you prepared to keep in one folder at once? Name a number and the sign by which you would stop.

## Speaker notes

A copy divides sessions, zones divide the workers inside a session. Where one ends and the other begins, each team decides for itself. The two questions below have no ready answer, and the reason for that can be named directly: the answer comes up against circumstances that differ from team to team — how expensive it is to bring up a copy's working environment, how often the shared file gets touched, who brings the results together and how much time they have for it. So the question is put together with a requirement to name the condition under which the answer changes: a named condition transfers to another tool, a habit does not.

**The first question: what has to be true about two pieces of work for you to agree to run them in one folder, and by what sign you set up a separate copy rather than working one at a time.**

It has two strong positions, and both are legitimate.

"Always a separate copy, no exceptions." Collisions then become physically impossible: every piece of work has its own files and its own branch. The cost shows up in two cases. Fixing a typo in text takes thirty seconds, while bringing up a copy's working environment takes minutes, and on work like that a copy costs more than the fix itself. A repository with heavy files takes a long time to copy and takes up as much space as a working tree. To that are added abandoned copies, which accumulate, and a permission granted inside a copy that outlives it.

"One at a time is more reliable." Also honest: one piece of work in the directory, one branch, one worker, nothing to collide with. The cost is time, and the position is tested by one question: what happens when the queue is longer than the working day. The previous case of the seminar showed that the parallelism lies in the task itself: if the work divides, a queue becomes a loss with no gain.

Between these positions lies the way people most often work: a copy per session plus a zone layout inside each. The condition the choice depends on is then formulated around the shared file. If two pieces of work touch no shared file — one folder with a zone layout is enough. If they touch one rarely — a queue on that file will do. If they touch one constantly — either a copy is needed, or one worker on both pieces.

The sign for "a copy rather than a queue" comes down to one question: can the second piece of work wait as long as the first one runs. If it can — a queue is cheaper, and there is nothing more to count. If it cannot — you pay for a copy, and bringing up the working environment is part of that bill.

**The second question: how many workers with the right to write you are prepared to keep in one folder at once. A number, and the sign by which you would stop.**

The arrangement allows twenty subagents at the same time, and it is usually not that cap people run into. What they run into is the person who reads the results: bringing together the work of ten workers is a separate piece of work, and the more workers there are the longer it takes. So a number above ten is worth testing with the question "who brings it together and how long does that take", and the tool's capabilities settle little here.

The sign by which people stop is named through zones: how many non-overlapping file sets can you name in advance. Managed to name six — then six workers are what work. A seventh, which got no zone of its own, takes somebody else's, and the gain from it is eaten by the collision.

The second sign is the shared file. If there is one file everybody needs, the ceiling for it is one writer, regardless of the total number of workers. Reading subagents do not enter that number at all: they have nothing to collide with, and the restriction applies to the right to write.

**A third question, if the first two closed quickly:** who owns a file needed by two of them — a named owner, a queue, or a separate bringing-together pass. The answer depends on the frequency. A file touched once a week is closed by a queue. A file touched constantly asks for an owner. A file assembled out of pieces asks for a separate pass — and somebody does that pass, it does not happen by itself.
