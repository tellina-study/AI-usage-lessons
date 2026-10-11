---
id: n59
type: criteria_boundary
duration_min: 1.25
assertion: "A copy can be given to a subagent with one line in its description, and it is done rarely: the branch of such a copy grows off the repository's default branch, a subagent's channel back is a single one — the final text — and the edits stay in a separate directory, from which a person brings them over"
learning_goal: "The turn of the case closes here. The room's intuition \"they work at once, so everybody has to be divided\" gets a precise answer: dividing is possible, the field exists, and the cost of it is the return journey. The criterion separates two cases — when isolating a subagent pays off, and when it cuts the subagent off from the work; the boundary is drawn by the subagent's work, not by the number of subagents"
visual:
  pattern: criteria_checklist_and_boundary
  primary: "At the top — a line saying the field exists, and under it a concluding line in gold (the builder lifts quotes above the boxes). Below — a table in two columns: a copy is given to a subagent / a copy is not given to a subagent. At the bottom — three points of cost, each with a name of its own."
  backup: "The harness documentation, read by direct curl on 2026-10-07 (not by summarizing WebFetch — notes/mcp-limitations.md [#225-1]). The field: \"Set to worktree to run the subagent in a temporary git worktree, giving it an isolated copy of the repository branched by default from your default branch rather than the parent session's HEAD. The worktree is automatically cleaned up if the subagent makes no changes\"; how it is switched on — \"Ask Claude to “use worktrees for your agents”, or make the isolation permanent for a custom subagent by adding isolation: worktree to its frontmatter\"; the base of the branch and changing it — \"New worktrees branch from the repository's default branch… Set worktree.baseRef in settings to branch from your current work instead… \\\"head\\\": branch from your current local HEAD… Use this when isolating subagents that need to operate on in-progress work\"; the channel back — \"The parent doesn't see the subagent's intermediate tool calls or outputs, only that final result\"; the example of the work isolation is set up for — the subagent `refactorer` with the description \"Applies mechanical refactors across many files\" and an off-the-shelf technique that divides one large change among 5-30 isolated subagents; teammates — \"Agent teams don't isolate teammates in worktrees, so partition the work so each teammate owns a different set of files\". IMPORTANT for the consolidation pass: the round-5 brief assumed that copies \"are not created\" for subagents; checking the source showed that the field exists, so the case is built on the cost of the return journey rather than on impossibility — see qa/krug5-subagent-keys3.md §4."
---

# Why a copy is given to a subagent rarely

## Assertion

A copy can be given to a subagent with one line in its description, and it is done rarely: the branch of such a copy grows off the repository's default branch, a subagent's channel back is a single one — the final text — and the edits stay in a separate directory, from which a person brings them over.

## Visual

> A copy can be given to a subagent: one line in its description — and the subagent works in a temporary copy of the repository; it is cleaned up by itself if the subagent changed nothing. The field exists; it is switched on rarely.

- **The first cost — the branch.** A subagent's copy grows off the repository's default branch, until a separate setting is changed. The work you began in your own directory, an isolated subagent simply does not see.
- **The second cost — the return journey.** A subagent's channel back is a single one: the final text. File edits stay in its directory, on its branch, and bringing them into your work falls to you.
- **The third cost — the working environment.** In a copy that too is its own: dependencies and local files a subagent gets in whatever form they were put there.

| A copy is given to a subagent | A copy is not given to a subagent |
|---|---|
| the subagent's work is a whole change that it is normal to accept as a branch: a mechanical pass across many files | the subagent is working on what you began in your own directory: a separate copy will cut it off from that work |
| there are many changes, and it is more convenient to check them apart from your own edit | the edit is short and needed right here — bringing up a copy's working environment costs more than the edit itself |
| an off-the-shelf technique divides one large change among dozens of isolated subagents at once | the subagent reads and comes back with a result: it has nothing to collide with |

> **Isolating a subagent is a choice made to fit the work. Where its edit is normal to accept as a branch, a copy pays off; where the subagent is editing what you began, a copy cuts the subagent off from the work. Teammates in an agent team are not given copies at all, and the prescription for them is the same: divide the work up by files.**

## Speaker notes

A copy can be given to a subagent, and it is worth starting with that so no wrong "it cannot be done" comes out of the case. One line in the subagent's description — `isolation: worktree` — and the subagent works in a temporary copy of the repository; the copy is cleaned up by itself if the subagent changed nothing. As a one-off, the same thing is asked for in words: use separate copies for the subagents. The field exists and is documented. It is switched on rarely, and that rarity is a decision assembled out of three costs.

**The first cost — the branch.** A subagent's copy grows off the repository's default branch. It does not grow off the state your session is standing on, which means the work you began in your own directory an isolated subagent simply does not see: it gets a clean tree on the default branch and makes its edit on top of it. This can be switched — the base of the branch is set by a separate setting, and the documentation names outright the case the setting was made for: isolating a subagent that needs to work on something unfinished. Knowing about the setting is worth it, or the cost looks insurmountable. It is configurable, and reconfiguring it is a separate decision somebody takes deliberately.

**The second cost — the return journey.** A subagent's channel back is a single one: the final text. File edits stay in its directory, on its branch, and bringing them into your work falls to you. In the ordinary mode there is no such step at all: the subagent edits where the work lies, and the edit is already in place. Isolation changes that into "the edit is ready and lying off to one side", and from there somebody brings it in by hand or takes it by merging a branch. The whole answer rests on this: the cost of isolating a subagent is the appearance of a step that did not exist before it.

**The third cost — the working environment.** In a copy that is its own: dependencies and local files a subagent gets in whatever form they were put there. A subagent that needs to run tests will find nothing in an unprepared copy and will honestly report a refusal.

The criterion from here runs along the subagent's work, not along their number.

A copy is given when the subagent's work is a whole change that it is normal to accept as a branch: a mechanical pass across many files, one convention applied to the whole tree. It is given when there are many changes and it is more convenient to check them apart from your own edit. And there is an off-the-shelf technique that divides one large change among dozens of isolated subagents at once; it exists precisely because for work of that kind isolation pays off.

A copy is not given when the subagent is editing what you began: a separate copy will cut it off from that work, and the subagent will come back with an edit to a clean tree. It is not given when the edit is short and needed right here — bringing up a copy's working environment costs more than the edit itself. And it is not given to a reading subagent: it has nothing to collide with, there is nothing to isolate.

Teammates in an agent team are not given copies at all — teams like that work in one directory by design, and the prescription for them is the same: divide the work up by files. That is also the answer to the question of where the class of work suited to isolation ends. It ends where the workers are running one shared task and looking into the same files.

What becomes of a subagent's copy once the subagent has finished. If it changed nothing, the copy is removed straight away — the arrangement does that itself, with nobody's discipline involved. If it changed something, the copy stays lying there until it is cleaned up along with the branch. Forgotten subagent copies accumulate the same way forgotten branches do, and clearing them does not happen by itself.

A short takeaway to carry instead of "subagents are not given a copy": they are, for one class of work — the one where the subagent's edit is entirely its own and is accepted as a branch. In the other cases isolation cuts the subagent off from the work it was called in for.
