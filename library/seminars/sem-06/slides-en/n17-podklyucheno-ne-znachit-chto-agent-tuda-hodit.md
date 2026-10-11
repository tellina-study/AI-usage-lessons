---
id: n17
type: mechanics_map
duration_min: 1.0
assertion: "The green \"connected\" marker is a fact about the process: it came up and it answered. Whether the agent went to the server in your task is a separate fact, and one sign proves it: a call in the output signed with the server's name"
learning_goal: "The last screen of the assembly: the file is assembled, the marker is green — and precisely here the trap people fall into after a successful connection is named. The thought is taken wider than MCP itself: the absence of an error does not prove the work, because there will be no error where no signals are arriving at all either. There is one checkable move and it is cheap — name the server in the request and look at whether the call is signed with its name"
visual:
  pattern: mechanics_table
  primary: "Three blocks one under another. The first, in the quiet form — what exactly the green marker proves. The second, as a box of two lines — the proof call: what to say in the request and which sign to look for in the output. The third, in gold — the general rule of monitoring: the absence of errors and the presence of a connection."
  backup: "Source — rework/section-1-mcp-part1a2.md §A.2a (the folded-down case) and §B.8a
    (section-1-mcp-part1c2.md). The proof call and the sign in the output are VERIFIED by
    fact-check (qa/fact-check-mcp.md §2.2 item 9). Incident `[#49]` (a silent loss of access with
    the status still live) is VERIFIED against notes/mcp-limitations.md, in one sentence in the
    notes.

    Edits after delivery (issue #225, qa/RAZBOR-PROVEDENIYA.md §A2): the case \"the server is
    connected and the agent does not go through it\" — nine slides from the decision point to the
    criterion — was dropped aloud by the lecturer in both groups, and both times its point was
    spoken in a single sentence. The case was folded down to this screen inside the connection
    case; the scene with the week, the vote, the breakdown of four checks, the failure and the
    boundary were removed entirely. Two things named by the lecturer were carried over here out of
    what was removed: the rule of monitoring (you have to watch for the presence of a connection,
    not only for the presence of an error) and the checkable move (the work is proved by a call
    signed with the server's name). The numbers, sources and wording of what was carried over did
    not change.

    Literary editing (issue 225, qa/pravki-nahodok-svedeniya.md item 3): two gold blocks in a row
    each carried a whole paragraph in bold, and the bold face stopped standing out. The proof call
    was separated onto two lines in a box in the ordinary face — \"what to say\" and \"which sign to
    look for\", exactly as those two pieces of work are named in the primary above; the only bold
    left in them is the names of the lines. One block was left in gold on the screen — the rule of
    monitoring. The words did not change in any of the three blocks, only the form of the second
    one did."
---

# Connected does not mean the agent goes there

## Assertion

The green "connected" marker is a fact about the process: it came up and it answered. Whether the agent went to the server in your task is a separate fact. One sign proves it: a call in the output signed with the server's name.

## Visual

> "Connected" answers for the process: it came up, it answered the handshake, it handed over the list of its tools. About whether the agent went to it in your task, there is nothing in that marker.

- **The proof call.** Name the server in the request by name: "using the tracker server, print the list of open issues, then prepare a draft for each one".
- **The sign in the output.** The tool call is signed with the server's name.

> The absence of errors is not enough. There will be no error when no signals are arriving at all either — you have to watch not only for whether there is a failure, but for whether there is a connection to the thing you are watching.

## Speaker notes

The file is assembled, the marker is green. Precisely here begins the trap people fall into after a successful connection, and it costs more than the connection did.

The green marker tells the truth — about the server's process having come up, answered the client's handshake and handed over the list of its tools. That is a fact about a program. Whether the agent went to that server while it was carrying out your task is a fact about a conversation, and it is not in the marker. The two facts stand side by side in the interface and read as two sides of one state; experience does not protect you from that confusion, and the number of connected servers does not change it — whoever has one connected gets the same trap in full.

The answer to the second question comes from one place only — from the output of that same session. Hence the simple move: name the server in the request by name. "Using the tracker server, print the list of open issues, then prepare a draft for each one" instead of "have a look at what has piled up in the inbox". After the first wording there is something to check: the tool call in the output is either signed with the server's name or it is not, and how plausible the answer is has no bearing on that check. After the second there is nothing to check — the agent might have read the tracker, and it might have assembled an answer from the sense of the task, and both routes produce text of the same kind. The server's name is taken from the same status command; there is no need to guess it from the name of the service: a server for access to the tracker may be named after the package, after the service, or after the short name of whoever connected it.

The move costs a few words in the request and one glance at the output, and it cannot be faked by plausibility: the signed line is either there or it is not. A confident, substantive answer in the absence of such a line is itself the signature of lost work: the answer was built without the server and looks better than the real one from the outside, because it arrives faster. If the server is named and there is no signature, you then look at the state of the process: the connection may have dropped, the authorization may have expired, the list of tools may not have arrived. The reverse move works too: if by its sense the task should not touch the server, say so outright — then the appearance of a signed line becomes a signal. Checkability works in both directions.

Wider than this screen the rule goes like this, and it is not about MCP. Monitoring that waits for an error stays silent in two different cases: when everything is fine, and when no signals are arriving at all. They cannot be told apart by the absence of an error — only by the presence of a connection to the thing you are watching. One documented case from this course's own log is exactly that: a connected server silently lost access, the tools stopped working, and the status command went on showing "connected" — it was noticed because ordinary calls started demanding a repeat login, not from the status.

The habit of naming the server by name costs a few words in the request. An investigation after the fact — "did the agent really look at the tracker yesterday" — costs an order of magnitude more.
