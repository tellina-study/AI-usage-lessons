---
id: s18
type: schema_layered
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "An agent's context lives at four distinct levels — permanent instructions, the context of one session, the operational history of tasks, and memory (slot 1 of the Lecture 3 map) — and each is maintained differently: instructions are written, sessions are curated, history is dated, memory is configured and audited"
learning_goal: "Leading: four levels of context/memory as an explicit structure (who maintains it · lifetime · a development example) + an explicit definition of JIT retrieval + how context is distributed across repository artifacts"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.2 [for-slide-s18]"
references: [anthropic-context-engineering, agents-md]
verify_day_of: false
visual_brief: >
  schema_layered: on the left — four horizontal level bands (1 permanent instructions · 2 context of one
  session · 3 operational task history · 4 memory-slot-1). Each band has three zones: (a) icon + "LEVEL N" +
  name + in small italics "who maintains it · lifetime"; (b) what it is; (c) a concrete development example
  (AGENTS.md with a verbatim command · the definition of JIT retrieval · an incident record with a date and a
  status · Mem0/Cognee/Graphiti/Letta). Under the bands — a teal plate with the honest limit: context rot
  (Chroma, 18 models) + baseline ~172k against ~334k tokens, marked "a direction, not a measured multiplier".
  On the right — a "What goes where in the repository" column: README · AGENTS.md · ADR · code comment ·
  incident record, each with one phrase about its own type of context, and a gold rule plate. At the bottom
  a gold callout. Lucide icons, level colors alternate mid/teal.
interaction: none
---

# Visible content

## Title bar
Four levels of agent context — each one is maintained differently

The agent is stateless: between runs it remembers nothing — everything it must know about the project sits at one of these four levels.

## Body

[Level 1 — Permanent instructions · human · lives with the repo]
A static file at the repository root: the agent rereads it every session — precisely because it has no memory between runs.
**AGENTS.md** (the analog is `CLAUDE.md`): "Tests: pnpm test" — verbatim build and test commands, code style, guardrails.

[Level 2 — Context of one session · human+agent · one session]
The window of the current dialogue. Three curation primitives: JIT retrieval, compaction, notes. More context ≠ better.
**JIT retrieval** — the agent opens the file it needs at the moment the task calls for it, instead of loading the whole repository up front.

[Level 3 — Operational task history · people · between tasks]
Past incidents and "how we fixed it" notes — as retrievable documents, so the agent does not reinvent them. No mature standard exists.
**An incident record** with a date and a status: "current" / "obsolete, see commit X" — otherwise the archive ages unnoticed.

[Level 4 — Memory (slot 1) · system · a human checks it]
A separate system: it decides for itself what to retain across sessions. You do not edit it line by line — you organize and audit it.
**Mem0 · Cognee · Graphiti · Letta** — you tune the selection rules, you do not edit the contents.

[Honest limit plate]
Why level 2 is curated rather than accumulated: retrieval accuracy drops non-linearly as the input grows — degradation starts **before** the window overflows (Chroma, 18 models). *Demo: ~172k tokens vs ~334k without curation — a direction, not a measured multiplier.*

[Column "What goes where in the repository"]
**README** — why the project exists and where to start — for a person opening it for the first time.
**AGENTS.md** — commands and constraints the agent executes literally, with no paraphrasing.
**ADR** — why a decision was taken and what was rejected — what the code does not say.
**Code comment** — why this particular piece is non-obvious; ships in the same change.
**Incident record** — how it was fixed last time — with a date and a freshness marker.

*Rule: put it where the artifact gets reread together with the code. Whatever must not be lost silently goes to level 1.*

[Gold callout]
Context lives **in the repository, not in the prompt** — but each level is maintained differently: instructions are written, sessions are curated, history is dated, memory is configured and audited.

## Speaker notes

The agent is stateless: between runs it remembers nothing. So everything it must know about the project sits not in the prompt but at one of four levels — and confusing them is expensive, because each is maintained in a different way.

Level one is permanent instructions: a static AGENTS.md file at the repository root (Anthropic's analog is called CLAUDE.md) that the agent rereads every session [1]. The key recommendation is to write it in commands rather than explanations: "Run the tests: pnpm test" works, while "we use such-and-such build system" makes the agent invent the setup steps. A human writes and updates this file, and it lives exactly as long as the repository does.

Level two is the context of one session — that is, managing the window of the current dialogue. There are three primitives: JIT retrieval, compaction, notes [3]. JIT retrieval is worth spelling out: the agent opens a specific file at the moment the task calls for it, instead of loading the whole repository at the start of the session. Curation is not about saving tokens: Chroma's study across eighteen models showed that retrieval accuracy drops non-linearly as the input grows, and the degradation begins before the window overflows [2].

Level three is the operational history of tasks: past incidents and "how we fixed it" notes, kept as retrievable documents. The practice is alive, but it has no mature standard yet, and every document needs a date and a freshness marker.

Level four is memory as a separate system: Mem0, Cognee, Graphiti, Letta. You do not edit it line by line the way you edit a file: it accumulates on its own, so you organize it and audit it periodically.

From this follows the practical conclusion about distribution. README answers a person's question of why the project exists. AGENTS.md answers the agent's question of which commands to execute literally. An ADR says why a decision was taken. A code comment says why this particular piece is non-obvious. An incident record says how it was fixed last time. Put context where it will be reread together with the code.
