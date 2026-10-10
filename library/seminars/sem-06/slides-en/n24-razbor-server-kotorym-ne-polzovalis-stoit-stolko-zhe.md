---
id: n24
type: answer_breakdown
duration_min: 2.25
assertion: "The cost is paid for being connected: a server that was not reached for even once in a session costs the same as a working one; two measures work — check that the definitions arrive on demand, and keep a set of servers for the task"
learning_goal: "The breakdown of all five cards in form A5 — two substantive columns. The conclusion names the turn of the case and separates the two working measures by order: one costs nothing and is often already on, the other requires work with the scopes"
visual:
  pattern: answer_breakdown_table
  primary: "A table of five rows in two substantive columns: what it does · what it does not do or the limit. The order of the rows matches the order of the question's cards. Every cell is a short phrase, not a sentence: it reads in one pass of the eye along the row."
  backup: "Source — rework/section-1-mcp-part1b.md §A.3.4, §B.24 (part1e.md). Round 5 (issue 225): the table was written anew for the replacement of the case.
    The turn is carried into the slide's title and into the conclusion under the table: the cost is paid for being connected, and a server that was not reached for in a session costs the same as a working one. That follows directly from the mechanics of deferred loading (sem-05/research/mechanics-5-mcp.md §2.3): what gets into the context at start-up is the tool names and the server's instructions, and they get in by the fact of connection, with no relation at all to whether anyone reached for the server or not.
    The third row carries an honest caveat, without which the slide would be lying: getting definitions on demand is the default behavior on current models, so the room's action here is a checking one: they look at whether the mode has been cancelled (mechanics-5-mcp.md §2.3, the ENABLE_TOOL_SEARCH table and the alwaysLoad field). The fifth row rests on the fact that tool definitions arrive in every request separately from the history of the conversation, which is why compaction does not touch them.
    The form of the table is \"variant · what it does · what it does not do / the limit\", the same as on n12 (ZADANIE-KRUG-2-VLADELTSA.md §A5, no third substantive column is set up)."
---

# A server you did not use costs the same

## Assertion

All five options are broken down by what they do and what they do not do. The cost is paid for being connected: a server that was not reached for even once in a session costs the same as a working one.

## Visual

| Option | What it does | What it does not do / the limit |
|---|---|---|
| nothing — the context is large | leaves everything as it is: on a short task it is not even noticeable | you have already paid the cost, and it holds for the whole session: on a long task the compaction comes earlier, and some of the decisions taken go into a paraphrase |
| disconnect the servers you do not use | removes the cost entirely: a server that is not connected has neither names nor instructions about itself in the context | it requires knowing in advance what will be needed; a needed server that has been disconnected brings back the work by hand that the section's first case began with |
| get the definitions on demand | leaves the tool names and the server's instructions at start-up; the model pulls in the full schema once it has needed the tool | this is the default behavior — which means your action here is a checking one: has a flag on a server or an environment variable cancelled it |
| keep a set of servers for the task | the personal connection scope gives a set for your own work, while the shared project file stays the team's | it sets up a second record of what is connected: the divergence between the personal and the project set has to be kept in your head |
| compact the conversation more often | frees up the room taken by the history of the conversation | tool definitions do not go away with compaction: they arrive anew in every context, separately from the history |

> **Out of the combination of the columns:** the cost is paid for being connected — a server that was not reached for even once in a session costs the same as a working one. Which is why two measures work, and in this order: first check that the definitions arrive on demand — that costs nothing and is often already on; then work through the set of servers for the task — that is work, and it gets done once.

## Speaker notes

It is worth beginning the breakdown with the thought carried into the turn of the case three screens earlier: being connected is what pays. It applies to all five options at once, and that is why the question "who was using what" does not reduce the count — it only reduces the feeling of guilt over somebody else's lines.

"Nothing — the context is large" is unnoticeable on a short task, and that is true: while the conversation is short, the reserve is enough. The cost meanwhile has already been paid and holds for the whole session. On a long task it turns into a shift in the moment of compaction: the conversation gets condensed earlier, and some of the decisions taken go into a paraphrase. What pays for that is the middle of the work, when going back to the beginning is most expensive.

"Disconnect the servers you do not use" removes the cost entirely, and it is a strong move: a server that is not connected has neither tool names nor instructions about itself in the context. The price is that you need to know in advance what will be needed. A needed server that has been disconnected brings back that very work by hand the section's first case began with: open the tracker in a browser, copy, carry it over, retell it to the agent.

"Get the definitions on demand" leaves the tool names and the server's short instructions about itself at start-up; the model pulls in a tool's full schema once it has decided the tool will be needed. This is the default behavior on current models — which means the action here is a checking one: you look at whether the deferral has been cancelled by a flag on an individual server or by an environment variable. The check costs a minute and breaks nothing.

"Keep a set of servers for the task" works through the connection scopes: the personal scope gives a set for your own work, while the shared project file stays the team's. The price is a second record of what is connected: the divergence between the personal and the project set has to be kept in your head and remembered when working out somebody else's fault.

"Compact the conversation more often" frees up the room taken by the history, and it does not apply to tool definitions at all: they arrive anew in every context, separately from the history. A useful measure, but it has no effect on this line item of the expenditure.

Hence the order, and it matters more than the choice of a single card. First check the loading mode of the definitions: that costs nothing, requires no agreement with the team and does not require knowing what will be needed in the next task — and it closes half the count at once. Then work through the set of servers by scope: that is real work, it gets done once, and it requires both agreement and a notion of your own tasks.

Cleaning somebody else's servers out of the project file is possible, and sometimes it is the right decision — but it is a team decision. The colleague needs them as much as the first person needs the tracker. The personal scope closes the same question without breaking anything for anybody, and so it comes earlier in the order of actions.

Disconnecting everything altogether and connecting as needed is a working mode for solitary work and a bad one for shared work. A connection from the project file arrives together with the repository precisely so that nobody has to assemble their environment again and so that the composition of what is connected is the same for everyone working out one fault.

It is worth noting that the two working measures act on different parts of the count and therefore add up. The check on the mode reduces how much every connected server's definitions take up. The work on the set reduces the number of connected servers. Done together they give a result that neither of them gives on its own: short definitions for a small number of servers that are needed.
