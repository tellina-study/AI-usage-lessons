---
id: n42
type: mechanics_map
duration_min: 0.5
assertion: "Launching in parallel is a mechanic of the harness, not a manual setting: subagents go into the background and work at the same time as each other and as the main session; the cap is twenty subagents running at once, not a cap on the total number of subagents per session"
learning_goal: "A support under the turn: the concurrency comes from the harness, there is nothing to configure — which means the whole cost of the decision falls on the layout. A concrete, checkable fact of the mechanics, not an abstraction"
visual:
  pattern: mechanics_table
  primary: "A box of two lines: subagents go into the background and work at the same time; the cap is twenty running at once, and it is changed by an environment variable. Under the box, one line in gold: for the whole session there is no cap at all."
  backup: "The source is research/mechanics-6-subagent.md §1.5, verbatim in substance: fork mode is on by default in an interactive session from version 2.1.232; \"Claude Code runs the subagent in the background... and Claude can't ask for the foreground\"; the concurrent limit is 20 by default (CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS, the error \"Concurrent subagent limit reached\" on the 21st); there is no overall cap on the number of subagents for a whole session — only on those running at once. Owner's round 5 (issue 225): the screen and the numbers are untouched, the speech is tied to the layout from the exercise, the word \"window\" was replaced by \"context\" in the notes (cross-cutting decision C1). Slot 0.75 → 0.5 — a quarter minute was given to the vote on n40, where the room talks; the speech was trimmed to the slot.
    Literary editing (issue 225, qa/pravki-nahodok-svedeniya.md item 3): the whole screen was one
    bold paragraph in a gold bracket — the builder was collapsing the source's two paragraphs into one block, and all five lines
    came out bold. Re-laid out according to the deck's grammar: the mechanics went into the box as two lines in
    ordinary weight, and one thought was left in gold — that for a whole session there is no cap.
    The paired contrast \"on concurrency, not on the number per session\" was separated into two independent
    statements (tools/editorial/README.md §1): the cap is named in the box, its absence
    by the gold line. The numbers, the version and the environment variable did not change."
---

# Background, not a queue — and a cap of twenty at once

## Assertion

Subagents go into the background and work at the same time as each other and as the main session. The cap is twenty subagents running at once, not a cap on the total number for a whole session.

## Visual

- **Background, not a queue.** From a certain version of the harness onward, parallel mode is on by default in an interactive session: the subagent goes into the background, and the main session does not wait for it before carrying on.
- **The cap is on concurrency.** By default no more than twenty subagents can be running at once; an attempt to set up a twenty-first fails with a separate, explicit error. The number is changed by an environment variable.

> **There is no overall cap on how many subagents can be called over a whole session.**

## Speaker notes

One clarification under the turn, and it changes how the cost of the decision reads.

Three subagents on three independent pieces would go at the same time. This is a mechanic of the harness, and there is nothing to configure: from a certain version onward, parallel mode is on in an interactive session by default. The subagent goes into the background, the main session does not wait for it and carries on working. No queue, no flag, no separate setting in the configuration — that is the behavior out of the box.

There is a cap, and it stands on concurrency. By default no more than twenty subagents can be running at once; an attempt to set up a twenty-first fails with a separate explicit error — `Concurrent subagent limit reached`. There is no overall cap on how many subagents can be called over a whole session at all: two hundred calls in a row, one subagent at a time, will run only into time and money.

From this follows a conclusion worth holding on to for the whole rung: concurrency is free. The harness provides it itself, which means the whole cost of the decision falls on the layout. The only thing you can get wrong is how many independent pieces there are in the task — and if you do get it wrong, concurrency will diligently multiply that error, because there is nothing to hold it back.

A twenty-first task at a cap of twenty will not get lost and will not wait its turn by itself. The harness refuses with an explicit error, and it will have to be launched by hand once room frees up. There is no silent queue here, and that is a fortunate arrangement: otherwise a twenty-first piece would sit quietly waiting its hour while being counted as checked.

The version and the variable, if precision is needed. Parallel mode by default appeared in an interactive session starting from version 2.1.232; the cap is set by the environment variable `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`. The version number is deliberately not put on the screen — it goes out of date faster than the fact does, and by the time of reading it has most likely already changed.

There is little point in raising the cap right after learning that it exists. Twenty subagents running at once are twenty contexts and twenty bills for tokens, and running into twenty on ordinary work is hard. If you have run into it, the first sensible action is to reread the layout and check whether there really are twenty independent pieces there. More often it turns out there are five, and the other fifteen are pieces cut along the lines of the task description that depend on each other.

Visibility is worth mentioning separately, because it is the cost concurrency does take after all. You can see that a background subagent is working, and you can see its result. The course of the work — what it was busy with, what it read, where it hesitated — is not visible. That is the very lost visibility this rung calls the price of delegation. On three independent pieces it hardly gets in the way: each result is checked separately and on its own. On dependent ones it gets in the way badly — that is exactly where you would need to see what one subagent learned before the other, and exactly what cannot be seen.
