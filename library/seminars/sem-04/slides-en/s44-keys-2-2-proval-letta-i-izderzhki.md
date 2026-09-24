---
id: s44
type: failure_vignette
duration_min: 1.5
assertion: "A file store beat graph memory — but what was measured was questions about a long conversation, not finding a related decision in a project log"
learning_goal: "The counter-example to structure with the measurement conditions taken apart: what LoCoMo is, what stands behind 74.0% and 68.5%, and what this result does NOT prove. The costs of structure itself are on the next slide"
visual:
  pattern: failure_vignette
  primary: "At the top — a \"what was measured\" block: how the LoCoMo benchmark works, in one paragraph. In the center — a two-row table with the conditions of each measurement spelled out right in the cell. Below — three points on \"what this result does not say\". The closing line leads to the next slide, on the cost of structure."
  backup: "The source of the numbers is a post on Letta's engineering blog dated August 12, 2025; the 68.5% there is quoted as Mem0's claimed result, not as a re-measurement of their own."
---

# The counter-example: what exactly was measured

## Assertion

A file store beat graph memory — but what was measured was questions about a long conversation, not finding a related decision in a project log.

## Visual

The "what kind of measurement is this" block:

> **LoCoMo** — a benchmark for memory in very long dialogues (Maharana et al., 2024). One example is a conversation between two fictional interlocutors: up to 35 sessions, on average about 300 turns and on the order of 9 thousand tokens. The models are asked questions about facts that came up in that conversation; the percentage is the share of questions whose answer was scored correct.

The table:

| What was run | Share of correct answers |
|---|---|
| **Letta's file store** (model gpt-4o-mini): the conversation was put into a file, and the agent was given semantic search, a text `grep` and "answer" | **74.0%** |
| **Mem0, the graph variant** — the number is taken from Mem0's own publication | 68.5% |

The authors' explanation: file operations were in the models' training data, so the agent uses them confidently; a "smart" but unfamiliar retrieval mechanism regularly loses to a familiar one.

The "what this result does not say" block — three points:

- **This is not a single run.** The two numbers come from two different publications. Letta's own authors call such a comparison "apples to oranges" and add that today's memory benchmarks may not be very meaningful at all.
- **"A file store" is not "grep only".** The file is automatically parsed and indexed, and the agent had semantic search too. The conclusion "one grep is enough" does not follow from this.
- **The task is a different one.** What was measured was questions about facts from a conversation, not finding a related decision in a project's decision log. Carrying this over to our case has not been measured by anyone.

The closing line: "Structure is not a guaranteed win. And not a free one: its cost comes next."

Source caption: "Letta, a post on the company's engineering blog, August 12, 2025 — not a peer-reviewed paper. LoCoMo — a 2024 paper."

## Speaker notes

"Before we accept this number, let us work out what stands behind it — otherwise it means something other than it seems to.

LoCoMo is a benchmark for memory in very long dialogues. One example is a conversation between two fictional interlocutors: up to thirty-five sessions, about three hundred turns, on the order of nine thousand tokens. Then they ask questions about facts that came up in that conversation and count the share of correct answers.

The company Letta put together the simplest possible solution: they dropped the whole conversation into a file and gave the agent three tools — semantic search, a text grep and 'answer'. The model was gpt-4o-mini, not the strongest one. The result was seventy-four percent. Mem0, a specialized graph-based memory system, has sixty-eight and a half in its own publication. The authors' explanation is simple: file operations were in the training data, the agent handles them confidently, and an unfamiliar retrieval mechanism, however smarter, regularly loses to a familiar one.

Now three caveats without which this number cannot be used. First: this is not a single run — the numbers come from two different publications; Letta's own authors call such a comparison 'apples to oranges' and write that today's memory benchmarks may not be very meaningful at all. Second: 'a file store' here is not 'grep only' — the file is indexed, and the agent did have semantic search. Third, the main one for us: what was measured was questions about facts from a conversation — not finding a related decision in a project's decision log. Nobody has measured our case.

What we take from this: structure by itself guarantees no win. Next — what it costs."
