---
id: n07
type: base_and_edge
duration_min: 0.75
assertion: "The agent takes data from two familiar places — the repository's files and files it was handed explicitly; the list of issues in the tracker fits into neither, it lives apart and changes without us — a snapshot will not save you here — the agent needs a way to ask the system itself"
learning_goal: "A gentle way into the section instead of the abstraction 'tool · resource · prompt' (round 2 of the owner's edits, issue 225, part B.1: the previous slide was rejected wholesale — 'we have never once looked at resources or prompts before this'). It names the three sources of data for an agent by where the data physically lies, and leads up to an API call as the third source — not as a protocol, that is the next slide"
visual:
  pattern: base_and_edge
  primary: "Two tracks. On the left, under the label \"BASE\" — the two familiar sources of data as a list. On the right — the third case, which fits into neither of the two, and the conclusion: a call is needed, not a file."
  backup: "Source — rework/section-1-mcp.md §A.1.2 (rewritten), §B.2 (part1c.md). Round 2 of the owner's edits (issue 225, part B.1, verbatim): \"Sources of data for an agent — a gentle way in instead of the abstraction... where the agent gets data from at all — files in the repository, files outside, an API call. The question 'and where do requests go' is the occasion to name the API\". The \"tool/resource/prompt\" taxonomy of the previous n09 was removed entirely — the owner rejected it outright as an abstraction that had not been introduced in class before.
    The storytelling revision (issue 225, P1/P6): the screen's closing line now names out loud
    the guess the case goes on to refute (\"you will have to pay for a call with an integration
    you write\") — without planting it, the turn on n12 has nothing to refute. The speech was cut
    from 157 words (1.21 min against a slot of 0.75) to 97 (0.75 min), and what was cut moved
    into the reference material. The table of the three sources did not change."
---

# Files inside, files outside — and the issue tracker?

## Assertion

The agent already knows how to read the repository's files and files it was handed explicitly. The list of issues in the tracker fits into neither: it lives apart from the project and changes without us. A snapshot will not save you here — the agent needs a way to ask the system itself.

## Visual

| WHAT THE AGENT ALREADY USES | AND THE LIST OF ISSUES IN THE TRACKER? |
|---|---|
| The repository's files — the agent reads them directly, this is the material of previous classes. | The client keeps it apart from the project: there is no such file in the repository's tree. |
| Files handed over explicitly: text pasted into the chat, a document attached. | Handing it over once and forgetting about it will not work — the list changes without us every day. |
| Both sources are files. Read it and get to work. | A snapshot as of this morning will be out of date by lunchtime. What is needed is a way to ask the system at the moment of the work. |

> Reaching a system like that is called an API call. The usual guess at this point: you will have to pay for it with an integration you write. We will check that against five ways.

## Speaker notes

By this point in the course the agent knows how to work with two sources of data, and both are files.

The first is the repository's files. The agent reads them directly: it opens a path, it gets the contents. This is the material of previous classes: the instructions, the specification, the recorded decisions all stand on the repository's files — everything that lies in the project's tree and is edited by the same commit as the code.

The second is files handed over explicitly: text pasted into the chat, a document attached. A different source, the same property: the contents got into the context once and do not change by themselves after that.

The list of issues in the tracker fits into neither of the two. It is not a file of the repository — the client keeps it in a separate system, and there is no such file in the project's tree. It does not become an attached file either: attaching the list once and forgetting about it will not work, because it changes every day without us, and a snapshot taken in the morning is already inaccurate by lunchtime.

What separates the first two sources from the third is time. A file has a moment at which it was read, and after that it stays as it was read: the answer to "what is written in it" does not depend on the second. Reaching a system has no such moment — the answer depends on the second in which you asked. Hence the requirement: the agent needs a way to ask the system at the moment of the work, because what was read in advance has time to go out of date by that moment.

Reaching out over the network like that is called an API call: the agent sends a request and gets an answer immediately, with no file as an intermediary. In other courses the same subject is often called an integration or a connector — a different word, one subject.

The temptation at this point is to treat the tracker as one more external file and attach it before every request. People really do that, and it is exactly what the developer in this case's scene does. The practice breaks on the day an edit goes out to the client before anyone has re-read the issue. As long as the list changes less often than it is consulted, a snapshot will do: a one-off export of the open issues before sprint planning is a working technique. Frequency is what moves the task from "copy the text" to "grant access".

And the guess to walk into the case with — the one that comes to almost everyone at this point: you will have to pay for a call with an integration you write, that is, with code that knows the addresses, the format of the request and how to parse the answer. Keep it in mind: the breakdown of the five ways will begin with precisely that.

The first two sources are listed here for the same reason. The choice ahead runs between five ways of getting access, and three of them take up context permanently precisely because the third source is built differently from a file. Without that boundary the five ways read as five names for one and the same thing, and the only basis for choosing is recognition.
