---
id: n28
type: criteria_boundary
duration_min: 1.5
assertion: "Keeping a server connected in the project file is worth it if it is needed in most of the project's sessions, if the definitions of its tools arrive on demand and if it has exactly as many toolsets as the task needs; what is never worth doing is keeping in the shared file what one person needs, setting the forced-loading flag with no reason written down, and believing that a large context settles the question — the accuracy of tool choice drops past 30–50 available tools"
learning_goal: "The generalization of the second case through direct headings — what to keep connected and what never to do. The fourth row of the right column takes the question beyond cost: an overflow costs tokens, while a drop in the accuracy of choice is visible in the result. Here too is the bridge to the subagent section: the agent has one context and it is finite"
visual:
  pattern: criteria_checklist_and_boundary
  primary: "A table in two columns: \"keep it connected\" and \"never needed\", each with a list of conditions. Under the table — a transition line to the subagent section: the fifth file in the configuration and one finite context."
  backup: "Source — rework/section-1-mcp-part1b.md §A.3.8, §B.28/§B.29 (part1e.md). Round 5 (issue 225): the criterion was written anew for the replacement of the case; the previous one (how long an old approval holds) was removed along with the case.
    The column headings are direct — round 2, the owner's item A7: \"write: when MCP is needed, when it is not needed, outright and clearly, people should not have to guess\". The frame \"too early / not needed at all\" does not come back.
    The base of the right column: the drop in the accuracy of choice past 30–50 available tools — docs.claude.com, \"Claude's ability to pick the right tool degrades once you exceed 30–50 available tools\" (read 2026-10-07, see n27 and research/mcp-kontekst-otkaz.md §2); the removed flag for issuing sets on demand on GitHub's official server — PR github/github-mcp-server#2512, merged 2026-05-20 (see n26).
    The bridge (§B.29) was rewritten for the case's new ending. The previous one passed the subagent section the question of a repeating subagent — the question of the sixth case, whereas the section's next slide (n29, \"Forty files for the sake of four places that are needed\") opens the case about the volume of reading. The new bridge passes exactly that: the fifth file in the configuration and one finite context, in which tool definitions are only one of the line items. The five files, the order of the sections and the bridge's addressee are preserved, and what changed is the question passed on. The seam is marked in the session's report as an edit affecting the neighboring section's zone."
---

# How many servers to keep connected

## Assertion

Keeping a server connected in the project file is worth it if it is needed in most of the project's sessions, if the definitions of its tools arrive on demand, and if it has as many toolsets as the task needs. What is never worth doing is keeping in the shared file what one person needs, and believing that a large context settles the question.

## Visual

| Keep it connected in the project file | Never needed |
|---|---|
| the server is needed in most of this project's sessions: the team uses it | keeping in the shared project file what one person needs: there is a personal scope for that |
| the definitions of its tools arrive on demand, and this has been checked | setting the flag that forces definitions to load without writing the reason down next to it: a month later it is somebody else's line with no explanation |
| it has as many toolsets as the task needs; the rest the server keeps switched off | believing that a large context settles the question: the accuracy of tool choice drops past 30–50 available tools, and it is visible in the result — the bill stays silent |
| — | relying on a flag found by a search: the server may have had it removed — it is checked against the description of the current version |

> There are five files in the configuration now: to the four we started the class with, `.mcp.json` has been added. It gave the agent hands — under permissions we crossed out ourselves, with a check we know how to carry out, and at a cost we can now see. The agent's context meanwhile is one and finite, and tool definitions in it are one line item. The next question is what does not fit into that context anyway, once there is more work.

## Speaker notes

The direct answer to the question of how many servers to keep connected consists of three conditions and four prohibitions.

Keeping a server connected in the project file is worth it when it is needed in most of this project's sessions and the team uses it. When the definitions of its tools arrive on demand, and this has been checked. And when it has as many toolsets as the task needs, while the rest the server keeps switched off.

Four things are never worth doing.

Keeping in the shared project file what one person needs. There is a personal connection scope for that, and it settles the same question without charging everybody else.

Setting the flag that forces definitions to load without writing the reason down next to it. A month later it is somebody else's line with no explanation, and the next person will either wipe it out blindly or not touch it out of caution. Neither of the two is a solution.

Relying on a flag found by a search. Flags appear and disappear; the page for the previous version reads as current instructions and is indistinguishable from them by its look. It is checked against the description of the server's current version.

And the fourth, which is worth the rest put together: believing that a large context settles the question. The accuracy of tool choice drops once there are more than 30–50 available tools, and overflow has nothing to do with it. Overflow costs tokens and is visible in the bill; an unsuitable tool chosen is visible only in the result of the work, and the bill stays silent about it.

The limit of 30–50 refers to tools, not to servers, and that divergence is worth keeping in mind. One server brings ten tools, and it brings forty. The count is therefore kept in tools while the decisions are taken in servers — connect, disconnect, move into the personal scope. In the gap between the two units of counting it is easy to come up short: four servers sounds modest, and there may be a hundred and fifty tools standing behind them.

The set is worth reviewing on an event: when a new server is added and when the project's task changes. The same structural criterion worked in the section's first case. A server that is needed rarely but genuinely lives in the personal scope and is connected for the duration of the work with it: the cost is paid for being connected, so disconnected it costs nothing.

How it ended for the developer from the scene: the two forced-loading flags were removed, he moved his own servers into the personal scope, and what stayed in the project file is what the whole team needs. The compaction on the next long task came later — the only thing he measured, and there will be no invented percentage here.

There are five files in the project's configuration now: to the four the class began with, `.mcp.json` has been added. It gave the agent hands — under permissions we crossed out ourselves, with a check we know how to carry out, and at a cost we can now see. The agent's context meanwhile is one and finite, and tool definitions in it are one line item of the expenditure. The next question is what does not fit into that context anyway, once there is more work.
