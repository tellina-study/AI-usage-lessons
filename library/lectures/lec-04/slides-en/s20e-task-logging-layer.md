---
id: s20e
type: schema_matrix
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "Task logging is grown in ascending order of complexity — one file, then a folder with one file per task, then a folder per task with files inside; the choice is compound (who works × how long the task lives × the need for an audit trail), and a fourth option — the log in the tracker — is visible to non-technical participants but sits outside the agent's file context"
learning_goal: "Leading: criteria for choosing between three file-based task-logging patterns — a method with no single right answer"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.3d [for-slide-s20e]"
references: [backlog_md, claude_task_tools]
verify_day_of: true
visual_brief: >
  schema_matrix 3x3, columns ordered simple → elaborate with the header fill darkening as complexity grows:
  (a) one file, a shared log · (b) a folder, one file per task · (c) a folder per task + files; icons on each
  header (list-ordered / clipboard-list / file-stack). The visible layer keeps the three most contrasting
  criteria (solo or a team, task lifetime, audit trail) plus one compact example line, one token per column.
  Below — the fourth, non-file option (the tracker) with an explicit for/against, and, visually separated in
  muted grey, what is NOT a task log (session-scoped TodoWrite/Task*, commit history as the only log).
  Gold callout — the criterion is compound, not a default.
interaction: none
---

# Visible content

## Title bar
Task logging is grown to fit the task, not taken at maximum

## Body
[Ordering principle]
COMPLEXITY GROWS LEFT TO RIGHT: one file → a set of files in one folder → a folder structure

[Matrix header — 3 columns]
**(a) One file — a shared log** · **(b) A folder, one file per task** · **(c) A folder per task + files**

[Matrix rows — the three most contrasting criteria]

Solo or a team: (a) a team — one shared chronology, but frequent merge conflicts · (b) a mid-sized team — fewer conflicts · (c) one developer or a small team; breeds directories

Task lifetime: (a) short, frequent · (b) "1 context window = 1 pull request" · (c) long-lived, complex

Audit trail: (a) chronological — "what and when" · (b) partial — outcome + structured fields · (c) detailed — intermediate steps of the reasoning

[Compact example line — one token per column]
Example: `notes/decisions.md` · `Backlog.md` · `notes/research/*.md`

[A fourth option — the log in the tracker (Jira, Linear, GitHub Issues)]
**For:** visible to non-technical participants, fits the process the team already has, keeps the repository clean.
**Against:** it sits outside the agent's file context — you need a bridge over MCP or an API; an extra external dependency and a network call instead of a local read.

[Contrast line — not a task log at all]
The built-in **TodoWrite/Task\*** lives inside one session; **commit history** as the only log — workable, but formalized nowhere.

[Gold callout]
The criterion is compound: who works + how long the task lives + why an audit trail is needed — not whatever came to hand first.

## Speaker notes

The task-logging layer is grown to fit the task rather than taken at maximum from the start. The patterns line up in ascending order of complexity.

The simplest is one file, a shared chronological log: everything that happened is written down in sequence. It gives a coherent picture of "what and when" and reads well for a human, but in a team it becomes a bottleneck — everyone edits the same place, and merge conflicts are constant. The next step is a folder in which each task gets one file. Conflicts drop noticeably: different people write into different files. The granularity here is not arbitrary: the open-source project Backlog.md ties the size of a file to the rule "one task — one context window — one pull request", so that a change stays the size a human can read in one sitting. The most elaborate option is a folder per task with several files inside: only this gives a detailed trail of the intermediate steps, it is needed on long complex tasks, and it noticeably breeds directories.

Three questions decide the choice: who works — one person or a team; how long the task lives; and why the trail is needed — to reconstruct a chronology, to report, or to review the line of reasoning.

There is also a fourth option that is not file-based: keeping the operational log in the tracker — Jira, Linear, GitHub Issues. The advantages are real: it is visible to non-technical participants, it fits the process the team already has, and it keeps the repository clean. The drawback is specific: the tracker sits outside the agent's file context, and for the agent to read it you need a bridge over MCP or an API — an extra external dependency and a network call instead of a local file read.

It is worth separately distinguishing what is not a task log at all: the built-in to-do lists live inside a single session and do not survive it, and commit history as the only log is a workable approach that is formalized nowhere.
