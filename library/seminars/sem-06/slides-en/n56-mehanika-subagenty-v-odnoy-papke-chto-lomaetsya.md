---
id: n56
type: mechanics_map
duration_min: 1.25
assertion: "A subagent works in the directory where the calling session stands — that is how it is built, and it is the normal mode; hence three breakages: an edit written over, work done against a stale state, and two successful reports that show no collision"
learning_goal: "The second half of the breakdown: what happens inside one session, where there are no copies. Three facts of the arrangement are named directly, and each is matched with the breakage it makes possible. The key thought the room should carry away: a shared directory for subagents is the norm, and that is exactly why the defense has to be a layout"
visual:
  pattern: mechanics_table
  primary: "At the top — a line saying that a shared directory for subagents is the standard mode. Below — a table in two substantive columns: how it is built / what breaks because of it, three rows. At the bottom — a concluding line about why isolation is not the first answer here."
  backup: "The harness documentation, read by direct curl on 2026-10-07 (not by summarizing WebFetch — notes/mcp-limitations.md [#225-1]). Verbatim: \"A subagent starts in the main conversation's current working directory\"; \"Within a subagent, cd commands don't persist between Bash or PowerShell tool calls and don't affect the main conversation's working directory\"; the snapshot of the state — \"Git status: a snapshot Claude Code reads from your repository when the subagent starts\", and it is not refreshed as the work goes on; \"You can't change which subagents receive git status. Only Explore and Plan skip it\"; what comes back — \"The parent doesn't see the subagent's intermediate tool calls or outputs, only that final result\" (the same line already stands in the foundation of the rung, research/mechanics-6-subagent.md §2.2). The three breakages are consequences of these three facts, named as consequences; the documented cases from the production of this course itself come a screen later (n58). The quotes with the date they were read are in qa/krug5-subagent-keys3.md §5."
---

# Subagents in one folder: what breaks here

## Assertion

A subagent works in the directory where the calling session stands — that is how it is built, and it is the normal mode; hence three breakages: an edit written over, work done against a stale state, and two successful reports that show no collision.

## Visual

> A subagent starts in the directory where the calling session stands, and it cannot leave: a change of directory inside a subagent does not survive the subagent's own calls. A shared folder for subagents is the standard mode, the one they work in almost always.

| How it is built | What breaks because of it |
|---|---|
| a subagent's directory is the same as the calling session's; the edit tool belongs to every subagent that has not had it taken away by a line | two subagents edit the same files; whichever wrote later writes over the first one's work — and writes it over entirely when it rewrites the file instead of editing a stretch |
| a subagent receives the state of the repository as a snapshot at the moment it starts, and the snapshot is not refreshed as the work goes on | the subagent writes against a state that is no longer in the directory: it creates afresh a file that "was not there", or edits a line that has already been rewritten alongside |
| the calling session receives a subagent's result; the steps by which it was arrived at, it does not see | both results come back successful, and they show no collision — it shows up in the files themselves |

> **That is how it is built, and it is normal: a subagent works where the work lies, otherwise there would be nowhere to return the result to. So the first defense here is a zone layout. Isolation for a subagent exists too, and its cost is examined later in the case.**

## Speaker notes

Now inside one session, where there are no copies.

A subagent starts in the directory where the calling session stands, and it cannot leave: a change of directory inside a subagent does not survive the subagent's own calls — every next call begins where the first one began. A shared folder for subagents is the standard mode, the one they work in almost always.

Three facts of the arrangement, and out of each one a breakage of its own.

First: a subagent's directory is the same as the calling session's, and the edit tool belongs to every subagent that has not had it taken away by a line in its description. Hence an edit written over: two subagents edit the same files, and whichever wrote later writes over the first one's work. It writes it over entirely when it rewrites the file instead of editing a stretch — and then nothing is left of the first one's edit.

The line in question is the tool list in the subagent's description: what is not in that list, the subagent does not do. Taking the edit tool away from a reading subagent costs nothing, and it is the first thing to check when several workers are working in a folder.

Second: a subagent receives the state of the repository as a snapshot at the moment it starts, and the snapshot is not refreshed as the work goes on. You cannot choose who gets it: every subagent receives it except for two purely reading modes. Hence work done against a state that is no longer in the directory: a subagent creates afresh a file that "was not there", or edits a line that has already been rewritten alongside. The snapshot was made that way deliberately — a subagent has to understand what state the repository was in on the way in, and a refreshing snapshot would make its behavior depend on somebody else's pace of work. What we pay for that is that by the middle of the work the snapshot is stale.

Two subagents launched at the same moment receive identical snapshots — and from then on each acts by that snapshot, knowing nothing about the other. That is what makes the breakage quiet: both are working against a state that is correct as far as they are concerned.

Third: the calling session receives a subagent's result; the steps by which it was arrived at, it does not see. Hence two successful reports that show no collision at all — it shows up in the files themselves. What remains in the conversation is that the subagent worked and what it came back with; which writes it made along the way is reconstructed from the files and from the repository history.

That is how it is built, and it is normal: a subagent works where the work lies, otherwise there would be nowhere to return the result to. So the first defense here is a zone layout.

Forbidding a subagent to write is possible, and for reading subagents that is the answer: the tool list is the composition of the arsenal, and what is not in it the subagent physically cannot do. For writing ones, the layout remains.

The move "let the subagents read the file right before writing" is the right one, it is examined on the next screen, and it has a limit: between the reading and the writing a gap remains, and it is not zero.

How many subagents one folder can take is a question with two different answers. The arrangement allows twenty at once. How many the folder can take depends on how many non-overlapping zones you have managed to lay it out into, and that question is what the discussion at the end of the case closes.

The position "it is better not to have writing subagents at all" is a workable one, and some teams live exactly that way: subagents read and report, the session writes. The cost is named honestly — everything written gets written at one pace, one thing after another.

An edit written over is discovered by the same two signs that work throughout this case: reread the file after the work, and look at the time it was last edited. The subagent's conversation does not answer that question.
