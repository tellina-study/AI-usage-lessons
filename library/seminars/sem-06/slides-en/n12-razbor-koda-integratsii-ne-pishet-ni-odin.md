---
id: n12
type: answer_breakdown
duration_min: 2.25
assertion: "Not one of the five ways requires integration code — the agent sends the request itself and parses the answer itself; what separates them is whether the agent knows in advance what the system can be asked, and for regular access from several sessions that leaves two legitimate variants of connection"
learning_goal: "The breakdown of all five cards in form A5 (two columns — what it does / what it does not do or the limit, with the variant not counted as a column of its own). Round 2 of the owner's edits (issue 225, the line-by-line breakdown of n12): the direct API is described correctly — the agent calls it itself, with no integration code, and the real limit is not knowing the specification; \"remotely\"/\"locally\" got a direct explanation of what they are; \"your own server\" got an honest assessment of the cost; the fifth card was replaced by a named tool (gh)"
visual:
  pattern: answer_breakdown_table
  primary: "A table of five rows in two substantive columns: what it does · what it does not do or the limit. The order of the rows matches the order of the question's cards. Under the table — the conclusion in three short moves: what drops out at once, what remains for a one-off call, and the two legitimate variants with the grounds for which one we take."
  backup: "The source of the cards is the owner's remark on round 1 (issue 225, item 2), with the fifth card replaced in round 2 — see the backup of n11. The fact about the change of transport in GitHub's official example (local npx → remote http api.githubcopilot.com/mcp/) — research/mechanics-5-mcp.md §1.6. The form of the table is round 2, part A5: two substantive columns instead of the previous three (\"variant · where it runs · limitations\" was cancelled by that round for the whole seminar).
    The second roast (issue 225 — the owner looked at this slide separately and confirmed: \"break
    the conclusion under the table into three short moves — what drops out at once, what remains
    for a single case, the two legitimate variants and why we take one\"; the same was noted
    independently by the methodology critic, P2 \"six lines of solid conclusion… four different
    conclusions in one paragraph with no breaks\", and by the student simulator, \"retelling it to
    myself takes some 15 seconds, not 5\"): one paragraph of about 95 words was split into three
    separate `>` blocks, each its own closing formula (a gold plate). The facts and the order of
    the reasoning did not change — the same combination of columns, the same basis for the choice.
    The storytelling revision (issue 225, P1 — the turn of the case): the title \"Five ways, each
    with its own cost\" was an inventory of the table and overturned nothing. The material for the
    turn had been lying in the first row of the table from the very beginning (\"no separate
    integration code needs to be written\") — exactly the place where the check overturns the
    obvious, hidden away in the second column of a five-row table. It was brought to the front:
    the title names the turn, the first block of the conclusion is called \"The turn\" and carries
    its wording, and the speech opens with it too. Not one row of the table, not one fact and not
    one decision of the case was changed — what changed is the order of presentation. The second
    half of the same turn is on n18 (the standing cost is the same for your own, somebody else's
    and a remote server). The speech was cut from 251 words (1.93 min) to 176 (1.35 min), and the
    line-by-line breakdown of the five cards moved into the reference material."
---

# Not one of the five writes integration code

## Assertion

Not one of the five ways requires integration code: the agent sends the request itself and parses the answer itself. What separates them is whether the agent knows in advance what the system can be asked. For regular access from several sessions that leaves two legitimate variants of connection.

## Visual

| Way | What it does | What it does not do / the limit |
|---|---|---|
| call the API directly | the agent writes and sends the requests to the endpoints itself and parses the answer itself — no separate integration code needs to be written | it does not know the service's specification in advance: which points there are, what their parameters and limits are — without documentation or a Swagger description the agent will not guess them |
| connect somebody else's server — remotely | a service somebody hosts and updates themselves; no separate process runs at your place | you are not the one managing it: there is no seeing what the service does inside or when something in it changes; plus the ordinary security questions of a remote service — whom you trust the key to, who else has access |
| connect somebody else's server — locally | the package runs at your place, the configuration is a line in the repository, visible to the whole team in review; more control than with a remote one | it is still a live process on your machine and somebody else's code — with all of its dependencies and its right to update itself |
| write your own server | gives exactly the set of operations and permissions needed, with no outside code in the process | writing a minimal server is quick these days — there is a ready-made plugin for it; what comes expensive is maintenance: the protocol, outside users, the security of the transport — a separate project alongside the main one |
| call the `gh` command every time | GitHub's ready-made official CLI — it has already solved authorization and parsing the answer for you, no code needs writing | every call is a separate command with no shared list of capabilities: the agent does not see in advance what can be done at all, and the call it needs has to be known in advance |

> **The turn.** No integration gets written in any of the five ways: the agent sends the request itself and parses the answer itself. What separates the five is something else — whether the agent knows in advance what the system can be asked.
> **What that leaves.** Your own server is excessive: an official one for the tracker already exists. `gh` and a direct API call cover a call that is known in advance; a growing list of operations they offload onto the developer's memory.
> **Two legitimate variants.** Between "remotely" and "locally" there is no ready answer: the latest official example connects remotely, and the seminar's decision is a local process, because the configuration then becomes code in the repository, visible in review.

## Speaker notes

First, what the breakdown overturns. You will not have to write integration code in any of the five ways. The agent will assemble the request itself and parse the answer itself — that it can do, and it can do it identically in all five cases. The guess we walked into the case with turns out to be false, and the choice has to be made on a different basis.

The basis is this: does the agent know in advance what the system can be asked. That is what the five ways get broken down by.

**A direct API call.** The agent writes and sends the requests to the endpoints itself and parses the answer itself. The limit here lies somewhere else: the agent will not guess the service's specification — which points there are, what their parameters are, what their limits are. It has to be given: by documentation, by a Swagger description, by an example request. As long as the description is fresh, the way works, and it works flexibly — any of the service's points are available, including those that are in no ready-made server. The description goes out of date silently: the service changed its version, the description stayed as it was, and the agent confidently sends requests to the old addresses.

**Somebody else's server, remotely.** A service somebody hosts and updates themselves; no separate process runs at your place, there is nothing to start and nothing to crash. The price for that is management: there is no seeing what the service does inside or when something in it changed. The ordinary security questions of a remote service belong here too: whom you trust the key to, and who else has access to it. What that ends in at worst is visible in the failure of the next case of the section: on one MCP server for databases, the "read only" flag did not make the connection genuinely restricted.

**Somebody else's server, locally.** The package runs at your place, the configuration is a line in the repository, visible to the whole team in review. There is more control here than with a remote one: the version is pinned by you, and an update happens when you have made it happen. What remains is that this is a live process on your machine and somebody else's code — with all of its dependencies and its right to update itself.

**Your own server.** Gives exactly the set of operations and permissions needed, with no outside code in the process. Writing a minimal server is quick these days — there is a ready-made plugin for it. What comes expensive is maintenance: updates to the protocol, outside users, the security of the transport. This is a separate project alongside the main one, and it is worth setting up when none of the ready-made providers has the set of operations you need.

**The `gh` command every time.** GitHub's ready-made official CLI: it has already solved authorization and parsing the answer for you, no code needs writing. Every call, meanwhile, is a separate command with no shared list of capabilities. The agent does not see in advance what can be done at all; the call it needs has to be known in advance — and the one who knows it is the developer.

The conclusion adds up out of the combination, in three moves.

The first: your own server is excessive. An official server for the tracker already exists, and your own implementation would repeat its work, adding a second project to the project.

The second: `gh` and a direct API call cover a call that is known in advance. That is their legitimate area, and it is a wide one. A growing list of operations they offload onto the developer's memory — and it is exactly there that the Tuesday from the scene happens again, only now with commands: the command needed exists, but nobody recalled it.

The third: between "remotely" and "locally" there is no ready answer, both are legitimate. The latest official example of connecting to this same service is a remote http service; this case's decision is a local process, because the configuration then becomes code in the repository, visible in review to the whole team. The local way meanwhile stays officially supported, so the decision is not spoiled by the existence of the remote example. Something else is worth knowing: the official route of one and the same provider changes over time, and a reference to "the official way" in your own documentation has to be re-checked.

How to apply this breakdown to your own system — four questions, in order. Is there a ready-made server for it: if there is, there is no point writing your own. How many operations are needed and is their number growing: one known operation is covered by a command or a direct call, a growing list requires that the agent see it itself. Are you prepared to keep one more live process with access to secrets: if not, a one-off call is more reliable than a process nobody services. And only after that — where the configuration should lie: in the repository if the connection concerns the whole team, at your own place if it is an experiment.

What remains is the question the breakdown leaves open: what, then, do you pay for with a connection at all, if an ordinary command gives you access too? What you pay for is the list of capabilities that the agent reads itself. How much that costs in tokens is counted further on in the case, on the screen of the standing cost, and the figure there is unexpected.
