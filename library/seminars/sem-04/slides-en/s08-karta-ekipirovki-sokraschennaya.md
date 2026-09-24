---
id: s08
type: keystone_axis
duration_min: 3.5
assertion: "An agent's configuration breaks down into five slots; today's project puts two of them to work — instruction-rules and memory"
learning_goal: "A single harness-map slide — co-building the five slots from memory of Lecture 3, two of them in focus, the ladder rule"
visual:
  pattern: keystone_scope_map
  primary: "The map in an Ocean rounded box: five slots in a row, numbered 1-5, appearing by co-building as the room names them. Two accented in gold — \"memory\" and \"instruction-rules\"; three in gray — \"skills\", \"subagents\", \"access to the outside (MCP)\". Under the map a line: \"Two are in play today. Skills, subagents, access to the outside and the mechanical layers (hook, process) — Seminar 5\". Below that, in a gold frame — the ladder rule in a single line. Not a single anglicism on the slide (in the RU deck all the labels are Russian)."
---

# Five slots, two in play

## Assertion

An agent's configuration breaks down into five slots; today's project puts two of them to work — instruction-rules and memory.

## Visual

The map — five slots in a row, numbered 1-5, filled in one at a time as the room names them:

| № | Slot | What it is |
|---|---|---|
| 1 | **memory** (gold accent) | what the agent remembers between sessions |
| 2 | **instruction-rules** (gold accent) | the project's convention file + a task log |
| 3 | skills (gray) | reusable procedures for repeating tasks |
| 4 | subagents (gray) | delegation with its own context window |
| 5 | access to the outside — MCP (gray) | access to external systems |

Under the map — a single line:

> "Two are in play today. Skills, subagents, access to the outside and the mechanical layers (hook, process) — Seminar 5."

Below that, in a gold frame — the ladder rule:

> "Stay on the lowest rung that closes the requirements of the task. Climb to the next one only when you can name a requirement that the current rung does not close. Every climb is paid for with new cost, new failure modes, and a new attack surface."

There is not a single anglicism on the slide: every label is in the language of the course (in the RU deck, all the labels are Russian).

## Speaker notes

The slide starts out empty: five empty slots in a row. The slots are not read off the screen — the room pulls them out of memory, they were worked through in Lecture 3.

The opening line: "In Lecture 3 we worked through what an assistant agent is made of on top of the loop 'plan → act → check → repeat'. In the chapter this is called the harness, and the slots are named Memory, Instruction-rules, Skills, Subagents, Access/MCP — the same names we will use from here on, on the slides and in conversation. There are five slots. Name the ones you remember."

Reveal them one at a time, with one line on each: memory — "not the context of the current conversation, but what survives the end of the session"; instruction-rules — "what you write yourself and what gets loaded at the start of every session"; skills — "a manual you take down off the shelf, not a regulation lying on your desk"; subagents — "a separate performer with a clean context"; access to the outside — "every connection is a new trust boundary". Any slot the room does not name, name yourself and move on.

Then, in one sentence: "In today's project two slots are at work: instruction-rules and memory. The other three, and the mechanical layers — hook and process — are a session of their own, Seminar 5."

The ladder rule — verbatim, under the map: "Stay on the lowest rung that closes the requirements of the task. Climb to the next one only when you can name a requirement that the current rung does not close. Every climb is paid for with new cost, new failure modes, and a new attack surface."

Bridge: "Back to the repository. The prototype is built, there are many days of work ahead with it — and the first decision about the agent's configuration is taken right now."
