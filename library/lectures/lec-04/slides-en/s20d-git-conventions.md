---
id: s20d
type: assertion_visual
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "A git convention is not a requirement of git but a voluntary team agreement: the marker in a commit is there for a program (which assembles the changelog and the version number itself), the prefix in a branch name is there for the reviewer before the diff is opened, and the pull-request template is there so nobody has to reconstruct the intent; an agent follows only the agreement it can see written down"
learning_goal: "Leading: git conventions (commit/branch/PR) as one level above build commands in the contract with the agent; the specific of scale — an agent commits systematically and an order of magnitude more"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.3e [for-slide-s20d]"
references: [conventional_commits, conventional_branch]
verify_day_of: true
visual_brief: >
  assertion_visual: a full-width teal definition band first — git checks none of this, a convention is a
  voluntary team agreement written down in AGENTS.md. Below, three Ocean rounded cards (Commit / Branch /
  Description), each with a chip, an icon, a "WHAT IT IS" paragraph, a monospace example plate, and a "WHY IT
  IS NEEDED" paragraph built from the reason rather than the syntax. One muted italic line common to all
  three: an agent never commits straight into the shared branch. Gold — an agreement written down nowhere
  does not work.
interaction: none
---

# Visible content

## Title bar
Git conventions are a team agreement, not a requirement of git

## Body
[Definition band]
Git itself is indifferent to what a commit message says and how a branch is named — it checks none of it. A convention is a voluntary team agreement, written down in AGENTS.md: shape the history the same way every time, so that both a human and a program can parse it. An agent follows only the agreement it can see written down.

[Card 1 — Commit]
WHAT IT IS: an agreed-in-advance shape for the first line of a commit: first a marker for "what kind of change is this", then the description.
`feat(auth): sign-in with a one-time code` / `fix(api): do not drop the header on retry`
WHY IT IS NEEDED: that marker is read by a program, not a human: from it, the release changelog and the new version number assemble themselves (fix → 2.4.1, feat → 2.5.0). An agent commits an order of magnitude more often than a human — there is no longer anyone to re-read every commit by eye.

[Card 2 — Branch]
WHAT IT IS: task type, a slash, a short lowercase description. For an agent's branches — dedicated prefixes.
`claude/security-patch` / `ai/refactor-auth-flow`
WHY IT IS NEEDED: the branch name is the only thing a reviewer sees before opening the changes. The prefix says immediately that an agent drove this branch, and such branches can carry their own rule. Without an agreement the branch list reads "test2" and "fix-final".

[Card 3 — Description]
WHAT IT IS: a pull request — the window where changes are shown to a human before they reach shared code.
`Why → What changed → What was not touched → How it was checked → Risks → Deferred`
WHY IT IS NEEDED: the reviewer spends time on checking, not on reconstructing the intent. The biggest saving is the "what was not touched" line: no hunting for side effects where there were none. Without a template every request is shaped differently. The agent fills the template in as it works.

[Line common to all three]
*A rule common to all three: an agent never commits straight into the shared branch — every task gets its own. The same thing this course asks of people.*

[Gold callout]
An agreement written down nowhere does not work: an agent follows only the rule it can see in AGENTS.md.

## Speaker notes

Git itself is indifferent to what a commit message says and how a branch is named: it checks none of it. A convention is not a requirement of the tool but a voluntary team agreement, written down where everyone can see it — including the agent. What makes it written down is AGENTS.md: a rule that lives only in a developer's head is a rule the agent cannot read.

The point of each of the three agreements is worth understanding separately from its syntax.

The commit. The first line begins with a marker for what kind of change this is, and only then the description. The marker is not there for a human but for a program: from it, the release changelog and the new version number assemble themselves automatically — a fix bumps the last digit, a new capability the middle one. With an agent the point gets stronger: it commits systematically and an order of magnitude more often than a human, and there is no longer anyone to re-read every commit by eye — structure turns volume into an asset rather than noise.

The branch. Task type, a slash, a short lowercase description; and for an agent's branches, dedicated prefixes. The branch name is the only thing a reviewer sees before opening the changes. The prefix says immediately that an agent drove this branch, and such branches can carry a separate checking rule. Without an agreement the branch list turns into "test2" and "fix-final".

The pull-request description. A fixed set of sections: why, what changed, what was not touched, how it was checked, risks, what was deferred. The reviewer spends time on checking rather than on reconstructing the intent. The biggest saving comes from "what was not touched" — it removes the need to hunt for side effects where there were none. The agent fills the template in as it works rather than recalling it at the end.

A rule common to all three: an agent never commits straight into the shared branch — every task gets its own.
