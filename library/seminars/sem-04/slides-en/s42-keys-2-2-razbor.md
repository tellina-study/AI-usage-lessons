---
id: s42
type: answer_breakdown
duration_min: 1.5
assertion: "Splitting it into separate files (one per decision) with cross-links is the target answer, but not a free one: structure itself creates a new load"
learning_goal: "The breakdown of the five positions in the room's answer for case 2.2 + the target answer with an explicit list of costs"
visual:
  pattern: answer_breakdown_table
  primary: "In small type at the top — the question, for context. A breakdown table of the five positions, with the \"split it into separate files\" row highlighted in gold. At the bottom — the target-answer plate."
---

# The breakdown: how to reorganize the log

## Assertion

Splitting it into separate files (one per decision) with cross-links is the target answer, but not a free one: structure itself creates a new load.

## Visual

In small type at the top — the question, for context: "How do you reorganize a decision log that has outgrown itself?"

| Option | Where this works | Why it is too early here — and what instead |
|---|---|---|
| "Leave it as is, just grep it" | While there are dozens of records and they fit into the context in full | Flat memory degrading over time is documented (~72 h, −14 pp); our file has already outgrown that boundary |
| **"Split it into separate files (one per decision) with cross-links"** | **Exactly this case** | **The target answer, but not a free one** — structure itself creates a new load |
| "I'll install a graph/vector memory system" | On large multi-user corpora with semantic search | The counter-example is aimed right at our scale: a file store beat a graph-based system on LoCoMo |
| "One shared SUMMARY.md, rewritten in full" | For a really small project | Rewriting in full kills the append-only guarantee |
| "The agent will find it itself by searching" | For facts derivable from the code | Decisions are not facts about the code. "It'll find it itself" is the same fallacy as "it'll remember on its own" |

The bottom plate, gold: the target answer — split it into separate files (one per decision) with cross-links, presented with a list of the real costs rather than as an unconditional upgrade.

## Speaker notes

"'Leave it as is, just grep it' — acceptable while there are dozens of records; but we have just seen that flat memory degrades over time, and our file has already outgrown that boundary. 'I'll install a graph memory system' — well, what we have is essentially a graph of decisions. The target answer is still a different one: separate files, one per decision, with cross-links, not a graph system. The Letta benchmark showed it: a simple file store beat the graph-based Mem0. Structure is not a guaranteed win; it wins here because it solves a specific problem — the lost link between decisions — not because 'structured is always better than flat'.

'One shared SUMMARY.md' — rewriting in full kills the very append-only guarantee. 'The agent will find it itself by searching' — the same fallacy as 'it'll remember on its own' from the previous case: decisions are not facts about the code."
