---
id: n25
type: mechanics_map
duration_min: 1.75
assertion: "Before your first question there are four line items in the context: the system part, the project's instruction files, the tool names of every connected server and the server's instructions about itself; a tool's full schema is pulled in on demand, and the deferral is cancelled by a flag on a server or by an environment variable"
learning_goal: "The mechanics of start-up: what arrives in the context before the work begins and from exactly where, where the boundary runs between a standing line item and loading on demand, and what cancels the deferral. The measured figure for the worst case, named in the section's first case on the slide about the cost of a connection, also adds up here"
visual:
  pattern: mechanics_table
  figure: mcp-n25-chto-v-kontekste.png
  primary: "A diagram: the four line items that arrive in the context at start-up by default, each with its source — the client, the repository, the server. As a separate line below — what arrives on demand. At the bottom, a gold zone of exceptions: the two ways of cancelling the deferral and the measured cost of the worst case with a reference to the measurement."
  backup: "Source — rework/section-1-mcp-part1b.md §A.3.5, §B.25 (part1e.md). Round 5 (issue 225): the slide was written anew for the replacement of the case; the previous diagram of trust by name (mcp-n25-tsepochka.png) was removed along with the case, and in its place mcp-n25-chto-v-kontekste.png is drawn (rendered/make_figures_mcp.py, section n25).
    Round 5's cross-cutting decision (C2, the owner's direct requirement: \"we need to show what comes into it at start-up and from where\") is closed here as far as MCP is concerned: four line items, each with its source. The project's instruction files are named in one line deliberately — the room assembled their composition itself over three classes, and there is no point breaking it down again.
    The base: sem-05/research/mechanics-5-mcp.md §2.1 (the client requests the list of capabilities itself, with no involvement from the model), §2.3 — the deferred loading of definitions as the default behavior, with the documentation quoted verbatim: \"Tool search keeps MCP context usage low by deferring tool definitions until Claude needs them. Only tool names and server instructions load at session start\", the table of ENABLE_TOOL_SEARCH values, the truncation of definitions and instructions at 2,048 characters each (CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH), the field alwaysLoad: true with the cost named in the documentation — \"each upfront tool consumes context that would otherwise be available for your conversation\". The documentation was accessed 2026-09-27.
    Separating the contradictions (issue 225, 2026-10-07): the condition is named in the heading of the diagram's column (\"WHAT IS ALREADY TAKEN — BY DEFAULT\"), and the alwaysLoad line was supplemented with the words \"regardless of the general mode\" — verbatim per the documentation (\"regardless of the ENABLE_TOOL_SEARCH setting\"). The count of 42–55 thousand tokens and the 21% did not change.
    The figure of 42,000–55,000 tokens for 93 definitions, about 21% of a context of 200,000 — sem-05/research/stage-5-mcp.md §1.3 (getunblocked.com, \"line-item autopsy\", 2026). The same figure stands on n18 as the upper bound of the cost of a connection; here it is shown in which mode it adds up. The slide introduces no new figures."
---

# What is sitting in the context before your first question

## Assertion

Before the first question there are four line items in the context: the system part, the project's instruction files, the tool names of every connected server and the server's instructions about itself. A tool's full schema is pulled in on demand, once the model has decided it is needed. The deferral is cancelled by a flag on a server and by an environment variable.

## Visual

## Speaker notes

The cause of the compaction is to be found before the conversation begins. Here is what is sitting in the context by the moment you have not yet asked anything, and where each line item arrives from.

The system part — from the client. Its own instructions and the definitions of its own tools: reading files, editing, searching, running commands. That line item is always there and does not depend on the connected servers.

The project's instruction files — from the repository. Their composition was assembled over the three previous classes, and there is no point breaking it down again; here they are needed as a neighboring line item of expenditure, one that takes up room in the same context.

From every connected server two things arrive. The first is the names of all of its tools. The second is the server's instructions about itself: a short text that the server sends in full, one for the whole server. Both items arrive by the fact of connection, with no relation at all to whether anyone reached for the server or not. The length of both is limited: the client truncates both each tool's definition and each server's instructions at 2,048 characters, and the limit is changed by the variable `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH`. The limit here is no accident: without it one talkative server would take up the context single-handed.

Full tool schemas do not arrive at start-up. The documentation describes this outright: deferred loading keeps the spend on MCP low by deferring tool definitions until the moment they are needed; at the start of a session only tool names and server instructions are loaded. A particular tool's schema the model pulls in by a separate move, once it has decided the tool may be needed. This is the default behavior on current models, and it is exactly what makes a fourth connected server tolerable.

Two mechanisms cancel the deferral, and both are worth knowing by name.

The field `alwaysLoad: true` on an individual server in the connection file loads all of its schemas at once, regardless of the general mode. That is the very flag that was found in somebody else's lines. The documentation names its cost outright: every tool described up front takes up room that would otherwise have gone to the conversation.

The environment variable `ENABLE_TOOL_SEARCH` governs the mode as a whole. Unset, it means deferral — the default behavior. The value `false` cancels the deferral completely: all definitions are loaded at once. The value `auto` turns on a threshold mode: definitions are loaded at once while they take up less than ten percent of the context, and are deferred once the threshold is reached; the form `auto:N` sets your own percentage instead of ten.

When there is no deferral, the count runs on the full schemas, and the measured order of magnitude is known: 93 tool definitions come to between 42,000 and 55,000 tokens, about 21 percent of a context of 200,000 tokens. The same figure stands in the section's first case as the cost of a connection. Here it is visible in which mode it adds up, and that is an important caveat: 42–55 thousand is the upper bound for the mode without deferral. By default a session comes cheaper, and by how much exactly depends on how many tools were actually needed over that session.

This can be checked at your own place with two looks. The list of connected servers and their state is given by the status command; a server's card inside a session shows what exactly it described about itself. The value of the variable is checked in the same place you look at the rest of the project's environment. An exact count of tokens per server those two looks do not give — the quantity has to be taken from an external measurement, and it is named above precisely as an order of magnitude.

A separate axis of expenditure that it is useful not to confuse with this one: the size of a call's result. A tool's definition is the cost of being connected; a tool's answer is the cost of one call. Different line items, they grow independently, and the measures against them are different.
