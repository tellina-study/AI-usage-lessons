---
id: n36
type: criteria_boundary
duration_min: 0.75
assertion: "By default a subagent's context inherits the definitions of every connected server of the calling session in full, including those its task does not need a single tool from — the focus works for the contents of the repository, but not by itself for what is brought in by servers"
learning_goal: "The boundary of applicability of the previous two slides: a subagent's clean context is not automatically clean across all sources. A direct, verbatim quote from the documentation on harness errors, with no cleverness added. A bridge to the subagent's tool list, which stands as the fifth block on the rung's one-pager. Round 5 (issue 225): the third band of the rung's base diagram (\"the definitions of connected servers\") is presented here once more — now in the subagent's context, and the slide leans on it instead of introducing the thought afresh"
visual:
  pattern: criteria_checklist_and_boundary
  primary: "A short text block: the verbatim quote about inheriting servers' tools. Below it — the application to the scene (the issue tracker and the documentation server from the previous section of the seminar land in the subagent's context for free, although they have nothing to do with the search). The bottom line is what to do about it: the same subagent tool list that stands as the fifth block on the rung's one-pager."
  backup: "The source is research/mechanics-6-subagent.md §2.5, verbatim from errors.md: \"Subagents inherit every MCP tool definition from the parent session, which can fill their context window before the first turn. Disable MCP servers you are not using before spawning subagents.\" Owner's round 3 (issue 225): a new boundary, which ties the MCP section and the subagent section of this same seminar together without repeating the material of either. Round 5 (issue 225, ZADANIE-KRUG-5.md): the word \"window\" was removed from the slide entirely (10 occurrences), \"parent\" was replaced by \"the session that called the role\"; the slide leans on the upper tier of the n30 diagram (the third band, \"the definitions of connected servers\"), which is why the introductory part of the speech could be dropped and the slot squeezed from 1.0 to 0.75 min — and that is the compensation for n30 growing from 1.25 to 2.0."
---

# A clean context — but not clean of everything

## Assertion

By default a subagent inherits the definitions of every connected server of the calling session — including those its task does not need. The focus works for the repository, but not by itself for the servers.

## Visual

> **"Subagents inherit every MCP tool definition from the parent session, which can fill their context window before the first turn. Disable MCP servers you are not using before spawning subagents."** — the harness documentation on troubleshooting errors.

> This is the third band on the base diagram — "the definitions of connected servers". It moves into the subagent's context in full. For our search over the limit on members: if the issue tracker and the documentation server from the previous section of the seminar are connected in the session, a subagent that needs to read forty files of code gets their definitions for free.

**The focus from the previous two slides is about the contents of the repository. What is brought in by servers is watched separately: by the same subagent tool list that stands as the fifth block on the rung's one-pager.**

## Speaker notes

A subagent's context is cleaner than yours and at the same time it is not clean of everything. It does get its own prompt and a fresh start, and together with them, by default, the definitions of every connected server in full — including those its task does not need a single tool from. This is the third band on the base diagram: it gets inherited.

Verbatim from the troubleshooting documentation: subagents inherit every MCP tool definition from the calling session, and that can fill their context before the first turn; disable the MCP servers you are not using before you spawn subagents.

Let us apply that to the scene. The protagonist is looking for the places where the limit on members is checked — work entirely inside the repository, with not a single reach outside. If the issue tracker and the documentation server from the previous section of the seminar are connected in his session, the subagent will get their definitions for free: room in its context is taken before it has opened the first file.

How much that costs the seminar has already measured: the standing cost of connected servers was named in tokens and as a share of the context in the previous section. What matters here is something else: that cost is paid once more, separately, into the context of every subagent set up. Five subagents — five times.

There is no contradiction with the previous two screens; both statements are about one contract. The focus works for the contents of the repository: the forty files really do stay in the subagent's context and close along with it. This screen names what enters the contract in addition and by default, over and above the wishes of whoever wrote the subagent. The saving remains; it is counted with a caveat.

What to do about it. Connected servers are watched by the same subagent tool list that stands as the fifth block on the one-pager: the subagent's permissions list also decides what will end up in its context. There is a reverse technique to the same mechanics as well: a subagent can declare the server it needs for itself — the server comes up when the subagent starts and is switched off when it finishes, and the calling session's context never sees its definitions at all. For a heavy server needed by one task, that is cheaper than keeping it connected for the whole session.

Two moves of the seminar converge here, and they do not converge in favor of carelessness. Access to the outside widens what the agent can do; the cost of that widening is paid in every session and now in every subagent as well. The more servers are connected, the more expensive every delegation becomes — and it becomes more expensive silently, because this is visible on no screen of the work: the subagent simply starts with less room.

The order of actions that comes out of this is short. Before setting up a subagent for a bulk read, it is worth looking at what is connected in the session and switching off whatever you are not using today: switching off applies to the session, and therefore to every subagent it will call.

The mechanics of hooks and skills are their own thing here, and the seminar does not break them down. One thing is enough: switching off unneeded servers is a deliberate move before a subagent is set up. A single tidy-up at the start of the day does not replace it, because a session accumulates servers as the work goes on, and by midday more is usually connected than you remember.
