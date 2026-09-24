---
id: s33
type: answer_breakdown
duration_min: 1.25
assertion: "A team decision with a justification goes into DECISIONS.md, a personal preference goes into auto-memory, what is derivable from the code goes nowhere"
learning_goal: "Breakdown of the five positions in the room's answer to case 2.1 + the target answer \"both mechanisms at once, with the roles split\"; the slide comes straight after the table of four layers and builds on it"
visual:
  pattern: answer_breakdown_table
  primary: "In a small font at the top — the question itself, for context. Below — the breakdown table of the five positions; the layer columns were shown on the previous slide and are not repeated here. The bottom plate is the target answer in gold: both mechanisms at once."
---

# Breakdown: where to put a rejected decision

## Assertion

A team decision with a justification goes into `DECISIONS.md`, a personal preference goes into auto-memory, what is derivable from the code goes nowhere.

## Visual

In a small font at the top — the question, for context: "Where to write the rejected decision down — and why not in the instruction file?"

| Option | Where it works | Why it is too early here — and what instead |
|---|---|---|
| "I'll add it to CLAUDE.md" | Mechanically it will work: the file is read every session | Mixes stable rules with a growing log of decisions. At a dozen decisions the file goes past the 200-line guideline |
| "Nothing, the agent will remember on its own" | Nowhere: this is not a setting someone forgot to switch on | The model has no state between calls, by construction |
| "I'll tell the agent 'remember this'" | For a personal preference — perfect | Half the answer. It goes into auto-memory: a machine-local layer with no sync and no code review |
| "I'll write it in DECISIONS.md — it already exists" | For a team decision with a justification — exactly what is needed | The second half of the answer. The point is not creating it but the discipline: writing the "why", not the "what" — and remembering that the file does not load itself: the agent will open it on its own initiative or on an explicit pointer |
| "I'll install a memory system" | At dozens or hundreds of entries, several users — the fourth column of the previous slide | An order of magnitude too early: on small corpora a simple file is regularly competitive with complex systems |

Bottom plate, gold: **the target answer — both mechanisms at once, with the roles split.**

## Speaker notes

"The layers are in front of us — now to the options that were named.

"I'll add it to CLAUDE.md" — mechanically it will work, there is nothing to argue about; but imagine thirty such decisions over half a year — the file is read in full every session, the guideline is two hundred lines. "The agent will remember on its own" — answer not with "no" but with the mechanics: between two calls the model stores not a single bit. "I'll say 'remember this'" — half the answer, it goes into auto-memory, a machine-local layer with no sync and no review. "I'll write it in DECISIONS.md — it already exists" — acknowledge it: correct, the file is already there, there is nothing to create. The question is not "where to set it up" but "who actually writes into it, and when, at the moment of the decision" — and how the agent is going to reach that file, given that it does not load itself. "I'll install a memory system" — acknowledge that the direction is reasonable and defer it to the failure slide.

The target answer — both mechanisms at once, with the roles split — and that split gets assembled at the next step, live, from the cards."
