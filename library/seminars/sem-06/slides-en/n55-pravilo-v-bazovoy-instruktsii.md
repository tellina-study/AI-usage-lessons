---
id: n55
type: code_artifact
duration_min: 1.25
assertion: "The agreement that every task is run in a working copy of its own is written into the project's root instruction file — next to the requirement already standing there to work in a branch — and is written out at the other end as well: when you have finished the task, offer to merge and to clean the copy up"
learning_goal: "The artifact of the case, and it takes the seminar back to the first rung of the arc: the project's instruction file, set up two classes earlier, takes a third line of the same kind. It explains why the order of work gets written down rather than held in memory, and why the rule is written out at both ends — set a copy up and close it"
visual:
  pattern: code_artifact
  primary: "Three points on a light card: the file and the section the lines go into, the lines themselves as inline code, and the status of the artifact. Below — two lines: why this is written into the project's instructions and why the rule is written out at both ends; the second carries the cost of an unclosed end — more than a hundred old copies on a work machine."
  backup: "The source is a direct recommendation from the course author, voiced at a class that was held (transcript `qa/rasshifrovki/gruppa-2.txt`, 1:00:25). Added under section B of the delivery breakdown (`qa/RAZBOR-PROVEDENIYA.md`), item 3.

    Verbatim supports. The recommendation itself: \"I'd recommend moving these rules into the root instruction file here. Because of how it's organized for me: besides the requirement to make branches… it also says there, and then at the end of the task don't forget to merge\" (group 2, 1:00:25). The motive for the second end: \"there's a temptation, especially with some initial task, that you quickly sorted something out in a session, abandoned the session, and so the branch is lying there separately, unmerged, we'll never get to it, so it's better to write the full cycle of solving a task into the instructions, how it should finish it\" (group 2, 1:00:51). The cost of an unclosed end is his own case, named in group 1: \"I recently discovered that my work machine had filled up because there are more than a hundred old worktrees sitting there\" (group 1, 47:45). The delivery breakdown (§C2) calls admissions like this the strongest places in both classes and asks for them to be built into the material deliberately — here that has been done, with explicit attribution.

    The state of the file the lines are added to is not invented: the `Repository etiquette` section in the demo repository's `CLAUDE.md` has existed since the entry point of the previous class and contains, among others, the line \"We don't commit straight into `main`\" (`sem-05/ARCHITECTURE.md` §2a, checked against the clone on 2026-10-02). Both kinds of rule have stood side by side in that file since the previous class: the `Repository etiquette` section — what is written down in words; the `Branch-guard hook` section — executable code (`sem-05/ARCHITECTURE.md` §2a). The slide that took that pair apart inside Seminar 6 (`n25`) was removed by the neighboring session along with the case that was folded away, so the support is taken directly from the state of the file rather than from a neighboring screen.

    The status marker is the same as that of the two artifacts of today on `n62`: \"planned, there is no commit and there will not be one\". The demo repository is not built any further (`SPLIT-PLAN-6-7.md` §1, the owner's decision), and hiding that at the third artifact would be strange in a class that spends the whole hour on the difference between what is written and what is already working.

    The overlap with a neighboring zone is named directly: this artifact's line was added to the `n62` table (the seventh row), and that is the only edit to an existing slide made by this session."
---

# The order of work with copies — as a line in the project's instructions

## Assertion

The agreement that every task is run in a working copy of its own is written into the project's root instruction file — and is written out at the other end as well: when you have finished the task, offer to merge and to clean the copy up.

## Visual

- `CLAUDE.md`, the `Repository etiquette` section — next to the line already standing there, "We don't commit straight into `main`", two more are added.
- "Every task is run in a working copy of its own: `--worktree <name>` at launch, or `git worktree add`." · "When you have finished the task, offer to merge the branch and clean the copy up; do not leave a copy unclosed."
- The status is the same as that of today's other two artifacts: planned, there is no commit and there will not be one.

> **Why into the file.** The project's instructions are read at the start of every session, and the order of work with copies reaches every one of them alike. An agreement that lives in memory reaches the sessions somebody remembered about.

> **Why at both ends.** Setting a copy up gets done willingly: without it you cannot start. Merging the branch and cleaning the copy up gets done after the task has been solved, and for that reason it gets forgotten. On the course author's work machine more than a hundred old copies turned up; it came to light when the disk ran out of space.

## Speaker notes

The move we examined — a working copy of its own for every task — lives as one line in the project's instruction file. That is the artifact of the case, and it takes the seminar back to the rung the project passed two classes earlier.

That file already exists and already contains rules of the same kind: a section with the order of work in the repository, and in it a line saying that you do not commit straight into the default branch. The requirement to work in a branch, then, has been written down for a long time. Next to it two lines are added. The first: every task is run in a working copy of its own — by a flag at launch, or by a git command. The second: when you have finished the task, offer to merge the branch and clean the copy up, do not leave a copy unclosed.

Why this gets written into a file rather than held in memory is explained by an arrangement the seminar has already examined. The instruction file is read at the start of every session, and the order of work with copies reaches every one of them alike — including the one brought up in a hurry on Friday evening. An agreement that lives in memory reaches the sessions somebody remembered about, and it is precisely the forgotten sessions that bring collisions.

The form here is a rule written down in words, one that gets read and does not execute itself. In the same file, since the previous class, there also stands a rule of the second kind: a branch-guard hook, code that fires on an event. The order of work with copies is not made into a hook: the event "time to set up a separate copy" cannot be described in advance, it is recognized by a person or by a session from the sense of the task.

The second end of the rule is worth noticing separately. The first end, setting a copy up, gets done willingly: without it you cannot start work. The second end, merging the branch and cleaning the copy up, gets done after the task has been solved, and for exactly that reason it drops out. The temptation looks harmless: the task turned out to be small, it was solved quickly in a separate session, the session was closed — and the branch was left lying separately, unmerged. There is no longer any reason to go back to it: the work is done, the result is in your head, and it is not in the default branch. A month later there are so many such branches that nobody will go through them.

The cost of the second end is measured on the machine. On the course author's work computer more than a hundred old working copies turned up — it came to light when the disk ran out of space. Tidying does not happen by itself: a copy stays on disk and in the branch list until the moment somebody removes it by hand. A hundred copies of a repository are a hundred working trees, and for a project with heavy files the count runs into tens of gigabytes.

The wording of the line is worth choosing with care. What works best is a wording that goes through the full cycle: how the task begins and how it finishes. A session told "set up a copy" sets up a copy. A session told "set up a copy, and at the end offer to merge and clean up" gets to the end of the cycle itself and asks whether to merge — and the decision stays with the person, while the reminder arrives at the moment when it is apt.

The status of this artifact is the same as that of today's other two: planned, there is no commit and there will not be one. The demo repository is not built any further, and that is said directly.
