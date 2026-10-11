---
id: n58
type: failure_vignette_table
duration_min: 1.25
assertion: "This course is built by several sessions in one working copy, and its log holds three cases of collision: an empty PDF with exit code zero, a build error from a read landing in the middle of somebody else's write, and about two hours spent recovering a branch — in all three, the familiar signs of success lined up"
learning_goal: "The failure of the case on the material of the course's own production — the same register of evidence as the former case of this rung: not a documented case at third parties but an entry in the log of a repository open in front of the room, with a command the room runs on its own machine. The three cases show three different breakages from the previous screens: an overwritten input, a read in the middle of a write, one branch for two"
visual:
  pattern: failure_vignette_table
  primary: "A short line saying that the course is built the same way. Under it — a table in three columns: case · signs of success · what was actually the case, three rows. Below — a concluding line in gold. At the bottom — a check command, addressed to the room."
  backup: "All three cases are entries in this repository's log, read on 2026-10-07. Case 1: notes/mcp-limitations.md [#212-7] — \"bash render.sh 44 … 50 completed successfully, honestly printed rendered slide 44 … 50 and PDF copied, but all 54 pages of the PDF turned out to be blank… The PDF size dropped from 6.67 MB to 2.69 MB. Not a single line of error\"; the cause — \"a neighboring session launched build_lec05.py and rewrote the input file at the moment LibreOffice was reading it\"; caught by comparing timestamps (\"lec-05.pptx turned out to have a later mtime than lec-05.pdf\"); the context — \"six sessions in one worktree\", issue #212, 2026-09-30. Case 2: the same place, [#212-4] addendum 4 — \"when one builder is edited by two sessions at once, a read of the file can land in the middle of somebody else's write: python3 build_lec05.py failed with a NameError… half a minute later the same build went through with no changes on my side\". Case 3: CLAUDE.md § Multi-Lecture Parallel Production — \"Lecture 2 production had ~2 hours wasted on branch contention recovery (lec-04 parallel session, shared .git)\"; the number of switches — notes/decisions-2026-03-05-lectures-1-6.md, line 325: \"L2 7+ branch switches mid-session\". The counterfactual to the third case: the same place, line 523 — three parallel lectures on separate copies, \"zero contention\", and notes/decisions-2026-05-lectures-8-11.md line 93 — four copies at once, \"Pattern works for ≥4 parallel lectures\". [VFY-day-of] is not needed: log entries are historical and do not change with edits made before the class."
---

# Every sign of success lined up

## Assertion

This course is built by several sessions in one working copy, and its log holds three cases of collision: an empty PDF with exit code zero, a build error from a read landing in the middle of somebody else's write, and about two hours spent recovering a branch — in all three, the familiar signs of success lined up.

## Visual

> This course is built the same way — by several sessions at once, in one working copy. Three cases from its own log, all three recorded in the repository that is open in front of you.

| Case | Signs of success | What was actually the case |
|---|---|---|
| six sessions were editing one deck in one directory; a neighboring build rewrote the input file while the converter was reading it | exit code zero, "rendered slide 44 … 50" line by line, "PDF copied", the right page count | all 54 pages out of 54 blank, the file slimmed down from 6.67 to 2.69 MB. Caught by comparing timestamps: the input turned out to be newer than the output |
| two sessions were editing one build file; a read of the file landed in the middle of somebody else's write | the build failed, and the error pointed to a name that "does not exist" | the declaration line was in the file; half a minute later the same build went through without a single edit by anybody |
| a lecture was being built in parallel with another in one working copy, with the branch switched from both sessions | each session saw its own branch in place — at the moment it was looking | more than seven branch switches in one session and about two hours spent recovering. After the move to separate copies — three, then four parallel builds without a single collision |

> **The exit code, the page count, the freshness of the files — every familiar sign lined up, and not one session, taken separately, did anything wrong. The only thing that showed the truth was the result itself and the time of the edit.**

`git worktree list` — on your own machine: do you have even one separate copy, and how many sessions are standing on one directory right now?

## Speaker notes

This course is built the same way — by several sessions at once, in one working copy. The three cases below are recorded in the log of the very repository that is open in front of you, and each of the three shows its own breakage from the ones we examined.

**Case one: an empty PDF with exit code zero.** Six sessions were editing one deck in one directory. The build reads the presentation file and converts it into PDF; a neighboring session launched its own build and rewrote that input file at the moment the converter was reading it.

Every sign of success lined up. Exit code zero. Printed line by line: "rendered slide 44", "rendered slide 45" and so on up to the fiftieth. Printed: "PDF copied". The page count in the resulting file was right — fifty-four. And all fifty-four pages out of fifty-four were blank.

It is worth going through each sign separately, because the set is typical and comes up far beyond the building of slides.

Exit code zero means the converter did not crash. It reports on its own execution and says nothing about the contents of the result: it read what it got from the file, carried the work to the end, and exited normally. A file being rewritten underneath a read does not make the read an error — it makes what was read something else.

The line-by-line "rendered slide" with a number is printed by the builder itself as it goes through the pages. The line says that the step was launched and is silent about what ended up on the page.

"PDF copied" is a report on copying a file. The file existed and it was copied. That check does not look into the contents at all.

The right page count deceives more than the other signs, because it looks substantive: fifty-four expected, fifty-four received. The structure of the document survived — the pages were counted and laid out. There is no ink on them. A page count comes cheap and says nothing about contents.

The only visible trace lay in the size: the file slimmed down from 6.67 to 2.69 MB. Nobody was looking at sizes, and that is understandable — there is no sign of its own in a size until you have something to compare it with.

It was caught another way — by comparing timestamps. The input file turned out to have a later edit time than the output; which means the output was built from something else, and what was built cannot be trusted. That is the check that works here: compare the times of the input and the output, and reread the result itself. The question to put to a build is whether its output was built from that input; the fact that it went through does not answer that question.

Why the blank pages were not found sooner: people were looking for the breakage in their own slides. The pages are white, so whoever edited last must have broken it, and each of them went off to check their own content. The sign by which this is recognized does not lie in the content at all: it lies in the edit time of the input file.

**Case two: an error that was not there.** Two sessions were editing one build file, and a read of the file landed in the middle of somebody else's write. The build failed, complaining about a name that "does not exist" — the declaration line was in the file, visible to the naked eye. Half a minute later the same build went through without a single edit by anybody.

In sign, this case is the inverse of the first: there, a successful report with a broken result; here, a refusal with an intact file. The cause for both is the same — they read a state somebody was changing at that moment. The sign is worth remembering: an error that disappears by itself, with no edits, is a sign of reading a state in flux. Looking for a defect in the code in a situation like that is pointless, because there is no defect there.

**Case three: two lectures in one copy.** A lecture was being built in parallel with another in one working copy, and the branch was switched from both sessions. Each session saw its own branch in place — at the moment it was looking. The switches in one session came to more than seven, and about two hours went on recovering.

Alongside this case stands its inverse, and it weighs more than the breakage itself. After the move to separate copies the same work went on being done in parallel further: first three lectures at once, then four — and there was not a single collision. Parallel work, then, stayed and expanded. What had to be forbidden was the shared directory underneath it.

What follows from the three cases together. Every familiar sign of success lined up, and not one session, taken separately, did anything wrong: each did its own work and honestly reported on it. The truth was shown by two things — the result itself, reread after the build, and the edit time of the files. Hence the fifth technique from the previous screen, which without these three cases would look like a platitude.

In the course's own rules this ended in two entries. A separate copy per session became mandatory, and the reason is written down next to the requirement. The second workaround is not to touch the shared build file at all: build your own set of pages in your own directory, and then somebody else's build cannot rewrite your input.

In all three cases it was sessions that were working. For subagents there is one difference: they do not have a copy of their own by default, so the choice between a copy and zones does not arise there — zones are what is left. What breaks is the shared directory, and it is indifferent to who is working in it.

A check on your own machine: `git worktree list` will show whether you have even one separate copy, and how many sessions are standing on one directory right now.
