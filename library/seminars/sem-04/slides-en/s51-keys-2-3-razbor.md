---
id: s51
type: answer_breakdown
duration_min: 1.25
assertion: "The target answer is a line in CLAUDE.md obliging the agent to append an agreement to the task file at the moment it is made; the task file is not the same thing as the decision log"
learning_goal: "The breakdown of the room's five answer positions for case 2.3 + the target answer as an instruction to the agent (not as human discipline), echoing case 1.2's formula \"rules in the prompt are requests\" and with the caveat about the simplification down to a single file"
visual:
  pattern: answer_breakdown_table
  primary: "In small type at the top — the question for context. A breakdown table of the five positions, the \"a rule in CLAUDE.md\" row highlighted in gold. At the bottom — the target-answer plate: the addressee of the rule is the agent that keeps the file, not the developer's memory."
---

# Breakdown: what to do differently

## Assertion

The target answer is a line in `CLAUDE.md` obliging the agent to append an agreement to the task file at the moment it is made; the task file is not the same thing as the decision log.

## Visual

In small type at the top — the question for context: "The task file misled — what should be done differently?"

| Option | Where it works | Why it's too early — and what instead |
|---|---|---|
| "Never compact, never close the session" | For a task that fits entirely into one short session | The context window is finite; on a multi-step task compaction will happen sooner or later |
| "Write the plan into DECISIONS.md" | Never — the wrong layer of memory | DECISIONS.md is about decisions that stay in force for good; the status of one task does not belong there |
| **"A rule in CLAUDE.md: an agreement goes into the task file right away"** | **Exactly our case** | **The target answer.** The file doesn't need to be created — what's needed is telling whoever keeps it **when** to write into it |
| "A folder per task with a file for each step" | Parallel subtasks, several subagents | Over-engineering for one linear task here and now |
| "Ask it to 'continue from where we left off'" | Inside one uninterrupted session, before compaction | After compaction there is literally nothing to continue beyond what is written in the file |

The bottom plate, gold:

> The target answer is a line in `CLAUDE.md` addressed to the agent that keeps this file anyway: an agreement made in the course of the work goes into the log right away, in the same reply. A rule in the text of the instructions is a request, not a law: it won't work every time. But the request is addressed to the executor that opens these instructions every session — and human attentiveness does not scale.

## Speaker notes

"The task file is not the same thing as the decision log. DECISIONS.md is about what stays in force for good, for all future tasks. The progress of this particular task is not a project decision, it is a status: what is done, what comes next, what small things we happened to settle along the way. How to store the wizard's state is a decision for exactly the duration of this task: once we're finished it is just a detail of the code, not a project rule. When the task ends, all of this can be thrown away. A completely different type of memory, not the next rung of the same ladder.

The target answer is not 'set up a file' — it already exists — and not 'do not forget to keep appending'. The file was there, the practice was there. What was missing was a single line — not in the log, but in CLAUDE.md: append an agreement to the task file the moment it is made, not 'when there is time'.

The addressee of that line is not the developer but the agent that keeps the file anyway: it reads the instructions at the start of every session, it checks off the steps, it writes the log. It simply was never told when to write. The solution to the case is to say that in the instruction file, rather than relying on someone remembering it on their own.

And exactly the same caveat as in the case about the readiness gate: a rule in text is a request, not a law, and it won't work every time. The difference is that the request is addressed to an executor that opens these instructions every session — whereas human attentiveness does not scale at all, in any way."
