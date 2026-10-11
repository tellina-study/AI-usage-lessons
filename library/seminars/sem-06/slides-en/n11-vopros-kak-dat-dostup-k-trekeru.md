---
id: n11
type: reflection_question
duration_min: 1.0
assertion: "The agent regularly needs to look at the tracker's open issues and prepare draft edits; the room first recalls how it has already given an agent access to the outside itself, and picks a way for regular access on the strength of that case of its own"
learning_goal: "The case's open question — the room has already seen the sources of data (n07) and the construction of MCP (n09) and has read the scene (n10); now comes the choice of a specific way. The cards set the concreteness: not abstract caution, but a specific way and the grounds for it. There is no target answer on the slide, the breakdown comes with the next slide"
visual:
  pattern: question_with_option_cards
  primary: "At the top, in the quiet form — a line about the room's own experience: who has had an agent go outside already, and what it was done with. Below, in a gold frame — the choice itself: find your own way among the five and say whether it will stand up to regular access. Under the frame, five equal cards in a fixed order, none of them highlighted. No figures and no sources on the slide."
  backup: "Source — the owner's remark on round 1 of the edits (issue 225, item 2, verbatim): \"besides how mcp itself works let us put in the choice — api, remote Mcp, your own mcp Server…\". The three obligatory variants from that quote are api, a remote MCP server, your own server; a local MCP server splits \"a ready-made server\" along \"where it physically runs\" (mechanics-5-mcp.md §1.4). The fifth card is from round 2 (issue 225, the line-by-line breakdown of n12): the previous one, \"make do with a one-off command\", was unclear to the owner — \"it is not about connecting to the tracker\". It was replaced by a concrete, named tool — `gh`, GitHub's official CLI: it genuinely can do the same action without MCP, and that is exactly what the Scalekit benchmark later in the case compares by cost in tokens (research/stage-5-mcp.md §1.3), rather than an abstract \"one-off command\".
    The second roast (issue 225 — the student simulator: \"I was holding the question from n11 in my
    head and waiting for one winner. I got two legitimate ones plus a caveat… the feeling that 'the
    answer is more complicated than the question implied'\"): the question in the gold frame was
    reworded from \"and why that one in particular\" to \"and explain why the other four are a worse
    fit for regular access\" — the room is set up to compare all five cards against the scenario
    (regular access) rather than to name the first familiar one. The cards and the target breakdown
    (n12) did not change.
    The storytelling revision (issue 225, P2): the first sentence of the question is tied to the
    episode of the scene (\"so that that Tuesday does not happen again\") — the room chooses a way
    against a specific miss, not against a general state. The cards, the wording of the choice and
    the order did not change; the reference material was extended with four breakdowns of the
    room's answers.
    An edit after two delivered classes (issue 225, qa/RAZBOR-PROVEDENIYA.md §C3): questions about
    the room's own experience produced answers, questions about an abstract choice did not. So the
    choice now comes as the second move: the first line asks what the room has already given an
    agent access to the outside with, and each person looks for their own way among the five cards.
    The cards, their order and the breakdown (n12) did not change."
---

# How do you give the agent access to the issue tracker?

## Assertion

Which of you has already had an agent go outside — into a tracker, into a database, into documentation? Recall what you gave it access with back then. Pick your own way out of the five cards and say whether it would have stood up to that Tuesday, when the tracker has to be visited every day.

## Visual

> Which of you has already had an agent go outside — into a tracker, into a database, into documentation? What did you give it access with back then?

> **Pick your own way out of the five — and say whether it stands up to regular access, or whether you would take the card next to it now.**

`call the API directly` · `connect somebody else's server — remotely` · `connect somebody else's server — locally` · `write your own server` · `call the ready-made gh command every time`

## Speaker notes

It is worth starting from your own case. Who has already had an agent go outside — into a tracker, into a database, into documentation? What was it done with? Almost everyone who has worked with an assistant for more than a month has some access to the outside by this class, and your own way comes to mind faster than somebody else's gets chosen.

Next, that way of your own has to be checked against the scene. So that that Tuesday does not happen again, the agent must look at the tracker's open issues itself at the moment of the work and prepare draft edits from them — that is, go there every day, not once. Pick your own way out of the five cards and say whether it stands up to that frequency; if it does not — which of the neighboring cards you would take now.

Five ways: call the API directly; connect somebody else's server — remotely; connect somebody else's server — locally; write your own server; call the ready-made `gh` command every time. The choice here weighs less than the reason for it: naming a way is easy, saying what exactly it demands of you in advance and what it takes up permanently is harder.

`gh` on this list is GitHub's official CLI tool. It is already installed for many developers and can read and write the tracker's issues without any MCP server at all, by an ordinary command call. The difference between "remotely" and "locally" is also worth saying out loud before the choice: in the first case the server is somebody else's process, which somebody else keeps on the network and maintains themselves; in the second the program runs at your place, and its start-up, its updates and its crashes are your concern.

Four answers to this question come up more often than the rest, and with each of them the same piece of work is worth doing.

"Write your own server." There is one checking question: what will be in your server that is not in the official one? Sometimes there is an answer — none of the ready-made providers really does have the set of operations needed — and then the choice is the right one. More often there is no answer, and then this is work that has already been done for you.

"We will take the API, because that way it is more flexible." A legitimate choice, and the breakdown does not overturn it. One thing is worth clarifying: where the description of the endpoints you feed the agent is going to live, and who will update it when the service changes its version. That description is as much an artifact of the project as the configuration, and it must have a named owner.

"What is the difference at all, if the result is the same?" The result really is the same: in all five cases the agent gets a fresh list of issues. The difference is in what each way demands of you in advance, and in what it takes up permanently. Both sides are broken down further on: the first in the breakdown of the five ways, the second on the screen with the cost.

An answer that does not match any of the five. Almost always it fits into one of the five, just in different words: "we will write a script that pulls the tracker" is a direct API call, "we will ask them to connect a ready-made service" is somebody else's server remotely. Such an answer is worth bringing round to one of the five, and after that it is broken down along with the rest.

Picking two is also allowed, and it is even more accurate: two of the five stay legitimate right to the end of the breakdown. In that case name both, and the condition under which you take the first.
