---
id: s41
type: research_evidence
duration_min: 1.25
assertion: "Flat memory degrades over time, and structure may pay off for an agent precisely where it does not pay off for a human — but \"smarter\" does not mean \"better\" without a check"
learning_goal: "A separate evidence slide for case 2.2 — the honest methodological caveat about very recent preprints, MEMTIER, the logic of the raw sources→wiki→schema pattern, the Letta counter-example"
visual:
  pattern: research_evidence
  primary: "The honest caveat about how recent the sources are at the top. Then — MEMTIER (flat memory degrading over time), the logic of the wiki pattern (human vs agent), the Letta counter-example (a file store against a graph system) — three blocks. The vote has already happened; this is the first slide where numbers are spoken."
---

# What the evidence says about structure

## Assertion

Flat memory degrades over time, and structure may pay off for an agent precisely where it does not pay off for a human — but "smarter" does not mean "better" without a check.

## Visual

The honest caveat at the top, in italics:

> "Almost all of the sources below are very recent (2026), non-peer-reviewed arXiv preprints in a fast-growing niche. The numbers are given marked 'claimed in a preprint', not as established fact."

**Flat memory degrading over time.** MEMTIER (arXiv:2605.03675): flat memory degrades over a horizon on the order of 72 hours of work — minus 14 percentage points in tool-call success. Three mechanisms: context saturation, temporal decay, semantic drift.

**The logic of "raw sources → wiki → schema".** For a human, the cost of maintaining a wiki grows faster than its value — so they abandon it. For an LLM agent, the cost of editing a dozen and a half files in a single pass is close to zero — the same scheme can pay off. There is no direct quantitative comparison against a flat log here — this is an argument from mechanism.

**A counter-example — important for balance.** The Letta benchmark on LoCoMo: a file store — automatically parsed and indexed, with semantic search available to the agent, not only `grep` — **74.0%**, beating the graph-based memory system Mem0 — **68.5%**. Models are trained on file operations as the most familiar tool there is.

## Speaker notes

"Before I show any numbers — a short honest remark. Almost everything I am about to say about structured memory is research from literally this year, preprints that have not been peer-reviewed yet. The niche is growing faster than science can check it. I will say 'claimed in a preprint', not 'proven'.

There is a measurement: flat memory degrades over a horizon of roughly three days of work — minus fourteen percentage points in tool-call success. There are three reasons: the context saturates, older records lose weight, and the meaning of a record drifts away from the current state of the project.

And here is an interesting argument for why structure may pay off for an agent where it does not pay off for a human. A human sets up a wiki, and it dies: maintaining it costs more than it is worth. For an agent, the cost of editing a dozen and a half files in a single pass is almost zero. That is an argument from mechanism — there is no direct measurement of 'structure versus a flat log' at our scale.

And a counter-example. The Letta benchmark, the long-term memory task LoCoMo: a file store — automatically parsed and indexed, with semantic search available to the agent, not only grep — seventy-four percent. The graph-based memory system Mem0 — sixty-eight point five. The simple store beat the structured one. The reason the authors name: models are trained on file operations as the most familiar tool there is. We will need this number once more in the breakdown."
