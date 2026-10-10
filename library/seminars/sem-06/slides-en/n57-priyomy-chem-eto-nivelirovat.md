---
id: n57
type: criteria_boundary
duration_min: 0.75
assertion: "Collisions in a shared folder are mitigated by five techniques — a zone layout, reading right before writing, editing a stretch, non-overlapping tasks with the bringing-together as a separate pass, and taking the check from the file itself; not one of them requires a separate copy, and each has what it does not close named"
learning_goal: "The applied answer of the case: what an engineer does on Monday. The techniques come with their boundaries, so the list does not read as a promise of safety. The first technique is a direct prescription from the harness documentation for teammates, who are not given copies at all"
visual:
  pattern: criteria_checklist_and_boundary
  primary: "A table in two substantive columns: technique / what it does not close, five rows. At the top — a concluding line in gold saying that not one technique requires a separate copy: the builder lifts quotes above the boxes, so it reads as the lead."
  backup: "The first technique is a verbatim prescription from the harness documentation for agent teams, read by direct curl on 2026-10-07: \"Agent teams don't isolate teammates in worktrees, so partition the work so each teammate owns a different set of files\". The third and fifth techniques are a generalization of the workarounds recorded by this repository's own log in the wake of six parallel sessions over one deck: notes/mcp-limitations.md [#212-4] (\"don't convert the shared file at all… build a subset of YOUR OWN slides\") and [#212-7] (\"A mandatory check after ANY render… The exit code, the presence of PNGs and their freshness — all three signs are false positives in this failure\"). The second technique is a consequence of the stale snapshot from the previous screen. The boundaries in the right-hand column were not invented for the sake of symmetry: the gap between reading and writing is named in those same log entries (\"a read of the file can land in the middle of somebody else's write\")."
---

# What this is mitigated with

## Assertion

Collisions in a shared folder are mitigated by five techniques — a zone layout, reading right before writing, editing a stretch, non-overlapping tasks with the bringing-together as a separate pass, and taking the check from the file itself; not one of them requires a separate copy, and each has what it does not close named.

## Visual

| Technique | What it does not close |
|---|---|
| divide the zones up before launching: every worker gets a file set of its own | a shared file needed by two of them; it stays a separate piece of work, and whose exactly is decided in advance |
| read the file right before writing, do not rely on what was read at the start of the work | the gap between reading and writing remains, and it is not zero |
| edit a stretch, do not rewrite the whole file | a structural rework of a file cannot be done that way — there the edit is "the whole thing" |
| give non-overlapping tasks, and bring the results together in a separate pass | that pass itself does not happen: somebody does it, and it is visible work |
| take the sign of success from the file itself: reread the result, check the time of the edit | catches a collision that has already happened, and prevents nothing |

> **Four techniques out of five are about the layout and the order of writing, the fifth catches what they let through. Not one requires a separate copy, and all five work where there is no copy to be had.**

## Speaker notes

Five techniques with which collisions in a shared folder are mitigated. Each has what it does not close named — which is why the list does not read as a promise of safety.

**Divide the zones up before launching: every worker gets a file set of its own.** The harness documentation prescribes this in so many words exactly where copies are not given at all — to teammates in an agent team: the work is divided so that each one owns a file set of its own. What the technique does not close is a shared file needed by two of them: it stays a separate piece of work, and whose exactly is decided in advance.

The zones are laid out by a person as the tasks are handed out: the zones are named in the setup itself, by file or directory names. Left to the workers' discretion, they drift apart, because each one sees its own task and does not see anybody else's files from inside it.

In the setup that looks like one line: "your zone is these files; do not go into the neighboring ones; before editing anything shared, reread it". The line is short, and without it the worker touches everything it considers related to the task.

**Read the file right before writing, without relying on what was read at the start of the work.** This is a direct consequence of the stale snapshot. What the technique does not close is the gap between the reading and the writing: it is short and not zero, and that is enough for somebody else's write to land between them. The technique lowers the frequency of collisions; promise anything it cannot.

**Edit a stretch, without rewriting the whole file.** The difference is visible on any shared file: editing a stretch leaves the neighboring lines as somebody else's, and somebody else's work survives; rewriting brings in your own idea of the file whole. The second is more convenient and more expensive. What the technique does not close is a structural rework of a file — there the edit is "the whole thing", and two workers do not do work like that at once in a shared folder.

**Give non-overlapping tasks, and bring the results together in a separate pass.** The technique works exactly up to the place where that pass is supposed to happen: it does not happen by itself, somebody does it, and it is visible work that has to be planned in.

**Take the sign of success from the file itself: reread the result, check the time of the edit.** Calling an ordinary check a separate technique is necessary because in parallel work the familiar signs of success all converge at once, and each of them is telling the truth about something else. What that means in practice is shown by the next screen. In advance this technique closes nothing: it catches a collision that has already happened.

The third and fifth techniques are a generalization of workarounds that had to be set up in this very repository; where they came from is visible on the next screen.

Four techniques out of five are about the layout and the order of writing, the fifth catches what they let through. Not one requires a separate copy, and all five work where there is no copy to be had.

Five are enough for what comes up most often. Not one of them promises that there will be no collision, and that is said at each of them. The question of who owns a shared file — a named owner, a queue, or a separate bringing-together pass — stays open and goes into the discussion.

A sixth move that comes up by itself and is not a technique is the hope that the workers will happen not to meet in one file. With two workers that hope is borne out often; with six it stops being borne out: the more workers there are, the more likely it is that one of them needs a file somebody is already holding.
