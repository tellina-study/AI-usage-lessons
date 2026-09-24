---
id: s20f
type: case_study
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "Every parallel session should have its own working folder, and all that stays shared is the history: a worktree separates the files (claude-code #60295 — a branch swap between sessions in one directory), but a shared .git means a shared lock — in claude-code #55724, 8 of 13 parallel agents lost unsaved work on .git/index.lock"
learning_goal: "Git worktree as the answer to a shared working copy under parallel agent sessions; honest verifiability on two public incidents"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.3f [for-slide-s20f]"
references: [git-worktree-docs, claude-worktree-docs]
verify_day_of: true
visual_brief: >
  A two-panel schema carries the meaning. Left panel "without worktree": three session chips → one shared
  working copy → one repository history. Right panel "with worktree": the same three session chips → three
  separate folders, each with its own branch → the SAME history row, deliberately worded identically so the
  eye reads what did and did not change. Three row labels down the left edge (SESSIONS / FILES IN PROGRESS /
  HISTORY .git). A caption under each panel: what breaks (#60295) and what changes. Bottom band: the two
  commands, the enforced isolation, and the honest boundary (#55724, the shared .git lock). Gold — the
  mechanic is older than any AI agent; what is new is only the frequency.
interaction: none
---

# Visible content

## Title bar
Every parallel session gets its own folder; all they share is the history

## Body
[Left panel — without worktree, one folder for everyone]
SESSIONS: Session A · Session B · Session C → **one working copy for all** (uncommitted edits sit in the very same files) → **one repository history**.

*What breaks: one session silently switches another's working tree — claude-code #60295. This course lost hours to it.*

[Right panel — with worktree, a folder of its own per session]
SESSIONS: Session A · Session B · Session C → `/wt-a` · `/wt-b` · `/wt-c`, each with its own branch → **the same history — this level did not change**.

*What changes: only the files are separated. Branches and commits stay shared — the folder is a view on the same history, not a copy.*

[Bottom — two commands and the folder is ready]
`git worktree add --detach /wt-a <commit>`
`cd /wt-a && git checkout -b task-A`
*Cheaper than cloning: the history is not duplicated.*

[Bottom — not on trust alone]
Claude Code blocks edits whose working directory is outside the assigned folder: a neighboring session cannot be touched even by mistake.

[Bottom — the boundary: a shared .git is a shared lock]
*The files are separated, but .git is one for everyone: 8 of 13 parallel agents lost unsaved work on the .git/index.lock. At 5 sessions — occasionally; at 10+ — almost certainly.*

[Gold callout]
The worktree mechanic is older than any AI agent; what is new is only the frequency: parallel sessions make a shared folder an expensive mistake every day.

## Speaker notes

While there is only one session, there is one working copy of the repository and no question arises. The problem appears when several agent sessions — or several tasks of one developer — run in parallel: their files are shared, and one session's uncommitted edits are visible to, and can be ruined by, another. This is not a speculative risk. The write-up of claude-code #60295 describes exactly this case: two sessions worked in one directory on different branches, one switched branch, and the second session's working tree silently changed; the second session had no way to learn that its picture of the state was stale, and trying to "fix" such a state with destructive commands risks losing data outright. This course lost hours of its own work to the same class of conflict.

Git worktree separates precisely the files: each session gets its own working directory with its own branch. The history stays single — the folder is not a copy of the repository but another view on the same history, which is why creating one is cheaper than cloning: the object graph is not duplicated. Two commands are enough. In Claude Code the isolation is also enforced rather than taken on trust: the tool blocks edits whose working directory is outside the assigned folder, so a neighboring session cannot be touched even by mistake.

It is worth knowing in advance where that isolation ends. Only the files are separated; the .git directory is shared, and so is the lock on it. In the write-up of claude-code #55724, of thirteen parallel agents five committed successfully and eight lost unsaved work to contention on .git/index.lock; at five sessions the failure happens occasionally, at ten and above almost certainly. As for how many folders to keep in parallel, there is no single norm: three-to-five and four-to-eight are both quoted, but that is a consensus of blog posts rather than a measured figure from documentation.

The conclusion: the worktree mechanic itself is older than any AI agent and does not depend on one; what is new is only the frequency with which parallel sessions make a shared folder an expensive mistake.
