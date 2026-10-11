---
id: n64
type: answer_breakdown
duration_min: 1.5
assertion: "Of today's five cases, two carry a support — the server's status and the count of separate copies of the repository; the other three rest on documented research that cannot be reproduced by one command in class. What the room carries away is the question with which you choose between the two moves"
learning_goal: "How the class ends: it is named what you can ask a checkable question about and get an answer by command, and after that a question to put to your own project, with which you choose between access to the outside and a separate worker. The asymmetry between the two supports and the three places where there is none is spoken out loud, once for the whole class"
visual:
  pattern: answer_breakdown_table
  primary: >
    A table of five rows: case, support ("yes" / blank), checked by what. The rows are in the order of the
    sections and cases of this class. No row is highlighted — there is no target answer here.
    Under the table — a quiet remark about the gap in checkability and the slide's last caption: the question
    with which the room chooses its move at home.
  backup: >
    The source: `rework/block-3-os.md` §A.4. The supports for checkability are the course repository
    (self-incrimination, subagents without trimmed permissions) and the student's machine (`claude mcp list`, `/mcp`,
    `/skill-doctor`, `/context`). The final grid is the one place in the class where the count is named
    in full: a support is carried by the connection check in case 1 of MCP and by the workers in one folder in the last case
    of the subagent section — exactly the two that
    `research/setka-keysov.md` §3 predicted before the sections were written. Revisions after the classes were held (issue 225,
    qa/RAZBOR-PROVEDENIYA.md §A2): the case "connected, and the agent does not go through it" was folded down to
    the n17 screen inside the connection case, which is why there are five rows in the grid, not six, and the checkable
    part moved into the row of the first case. Three cells with no support are not an oversight:
    most of the material here is documented research (CVE, arXiv, GitHub issues),
    which cannot be reproduced by one command in a classroom.

    The owner's round of edits (issue 225, §A2): the closing paragraph referred to "the difference between
    a report and a fact" — the wording of an arc the round removed entirely. Replaced by a wording
    that fits the class's new load-bearing thought: the agent runs up against the boundaries of its own context, extends it
    with data from outside or with a separate worker, and each extension has its own cost; an undeclared
    gap in what of this is checkable right now would cost more than a declared one. The line
    "four out of five, the fifth — the process — is ahead" was removed (§A1): the class's axis is four rows, all
    four closed by the class's axis.

    Storytelling revision (issue 225, `PERESMOTR-STORITELLING.md`, cause 4 "the close
    takes inventory instead of resolving"; rule P5 "the room applies the material to itself"). The slide
    used to end the class with a summing-up of the protocol: what became checkable, where there is no support. That is honest and
    stays on the screen unchanged — the table of five rows, both columns and the declaration of the
    gap are the same. What has been added is the thing the class was going for: the last caption is now
    the question with which the room chooses its move at home ("what is it short of — what is not inside
    at all, or the room taken up by reading?"), and straight after it, where each of the two
    cases goes. The former last caption ("The axis of this class is closed — all four rows can now
    be checked at least in part") was removed from here: the statement about the closed axis moved to
    `n61`, where the axis table itself stands next to it, and there is no point repeating it a second time at the end.
    The quiet remark about the gap in checkability was compressed by a third, so that the room for the question came out of this same
    slide rather than out of its slot. This is a question, not an assignment: the rule "a class ends on
    what became checkable, not on homework" (`AUTHOR-BRIEF.md` item 11) holds —
    nobody is asked to answer out loud or to send an answer in, and the notes say so directly.
---

# How the class ends

## Assertion

Of today's five cases, two carry a support; the other three are documented research that cannot be reproduced by one command.

## Visual

| Case | Support | Checked by what |
|---|---|---|
| MCP — the data is not in the repository | yes | `claude mcp list` / `/mcp` and a call signed with the server's name — on your own machine in a minute; the assembled file itself is a target state, with no commit behind it |
| MCP — tool definitions take up context | no | figures from documentation and engineering blogs; we do not take a measurement in class |
| Subagent — the reading goes off into the worker's context | no | requires a prepared parallel run, not reproducible in class |
| Subagent — a second worker, the gap | no | a claim from research (MAST); neither of the class's two supports demonstrates it |
| Subagent — workers in one folder | yes | `git worktree list` — on your own machine; and three collisions in the log of the repository opened in class |

> "Under some of today's cards there lies a command you can run and get an answer from. Under others there is none, and that is said directly: an undeclared gap would cost more than a declared one."

> "From here you carry away one question to put to your own work: what is it short of — what is not inside at all, or the room taken up by reading? The first you bring inside, the second you carry outside."

## Speaker notes


The last screen of the class does two things: it honestly divides today's material by what it can be checked with, and it hands over the question with which you choose your move at home.

Of the class's five cases, two carry a support.

The server's status — the first case of the MCP section, its last screen. It is checked right on your own machine: `claude mcp list` prints the list of connected servers and their state, `/mcp` shows the same from inside the session, and there you can see that "connected" answers for a process being up and for nothing else. What remains as proof that a server is really working is an explicit named call, visible in the output; that too can be checked on your own machine in a minute. The assembled connection file is itself a target state: there is no commit behind it either in the demo repository or in the course repository, and the screen says so directly.

Workers in one folder — the third case of the subagent section. `git worktree list` prints how many separate copies of the repository you have and which directory each one is standing on; from that you can see how many sessions are sharing one directory. On that same count the course caught itself: it is built by several sessions in one working copy, and three collisions are recorded in its log — an empty PDF with exit code zero, a build error from a read landing in the middle of somebody else's write, and about two hours spent recovering a branch. In all three, the familiar signs of success lined up. The log in which those cases are recorded is open.

Under the other three there is no support in the form of a command you can run here and now, and that is said directly. The figures on context taken up come from the protocol's documentation and from engineering blogs — we do not take a measurement in class. The gain from delegated reading requires a prepared parallel run, which you cannot set up in a classroom. Misalignment between workers rests on a measurement over 1600+ traces of multi-agent systems, where it accounts for 37% of failures, and neither of the class's two supports demonstrates that. The checkability here is of a different kind: you read the primary source, you do not run a command. Three cells with no command are a difference in the nature of the material, and there is no oversight behind it.

The result of the class is not measured by a number of files. The result is the question with which you choose a move, and the cost named at each of the two. Checkability is half of that result: about part of the material you can ask a question and get an answer by command, about the other part not yet, and an undeclared gap would cost more than a declared one.

And the last thing, the thing it was all going for. Two mechanisms have been taken apart; what is worth carrying away is the question with which you choose between them. Tomorrow, when your work stops fitting the agent: what is it short of — what is not inside at all, or the room taken up by reading? The first you bring inside, the second you carry outside. The developer whose two misses the class began with tells those cases apart himself — and that is the whole answer to the question that was asked a second time a screen earlier.

This is a question, and it does not become an assignment. Nobody needs to answer it, there is nowhere to send an answer, and it is not asked about in the next class: carrying it over to your own repository is the work of a class of its own, and beginning that with an unperformed assignment would be dishonest.
