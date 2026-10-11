---
id: n22
type: problem_scenario
duration_min: 1.25
assertion: "He connected the tracker himself, a colleague added three more servers to the same project file — and on a long edit the agent compacted the conversation noticeably earlier than usual; over the whole task one server out of four was needed"
learning_goal: "The hook of the second case: a person and a named cost. The overflow is discovered through the conversation being compacted in the middle of a long task, and the cause only opens up when the person looks for himself at what the context is made up of before his first question. The cost is named in a working register — an hour spent going over the decisions again, and one edit made on a decision that had already been reversed"
visual:
  pattern: problem_scenario
  primary: "At the top — one line about the composition of the project file: one server his, three somebody else's. Below — four steps: what he noticed, what it is made up of, what he found in the other person's lines, what it cost. At the bottom, as a separate line, the count: over the task, calls went to one server out of four."
  backup: "Source — rework/section-1-mcp-part1b.md §A.3.2, §B.22 (part1e.md). Round 5 (issue 225, ZADANIE-KRUG-5.md): the scene was written anew for the replacement of the case. The previous scene (a tool definition that changed between the approval and the re-reading) was removed along with the case.
    The person is the same developer as in the seminar's hook (n01/n04) and in the section's first case: the tracker in the project file is his own artifact from the first case (n16), and the scene begins with precisely that. The three servers belonging to somebody else arrive by a mechanism the room has already broken down on n14: the project scope of the connection file is shared, and everyone who clones the repository sees it (sem-05/research/mechanics-5-mcp.md §1.2).
    The field alwaysLoad: true is taken from the documentation, not invented for the scene: it forcibly loads all of a server's tools at once, irrespective of deferred loading, and the documentation names the cost outright — \"each upfront tool consumes context that would otherwise be available for your conversation\" (mechanics-5-mcp.md §2.3, accessed 2026-09-27). The colleague's motive (\"so the tools do not get lost\") is the ordinary reason that flag gets set.
    The scene is a teaching one, like every scene in the seminar: the project is real, the situation is assembled out of typical ones. The measured numbers stand separately, on n25 and n27, and always with a source — not one share of the context is named in the scene, deliberately, so as not to pass a teaching estimate off as a measurement."
---

# One server is his. A colleague added three more

## Assertion

He connected the tracker himself in the previous case. A colleague added three more servers to the same project file — for his own work. On a long edit the agent compacted the conversation noticeably earlier than it had on the same kind of task a week before.

## Visual

> The project connection file: the issue tracker is his own; the browser, the database, the documentation server are a colleague's, for his own work. The scope is the project's, and everyone who works with the repository sees it.

- **What he noticed.** On a long edit the agent compacted the conversation noticeably earlier than usual and re-asked what they had agreed at the start.
- **What it is made up of.** He looked at what lies in the context before his first question: the system part, the project's instruction files, the tool definitions of four servers.
- **What he found in the other person's lines.** Two of the servers have `alwaysLoad: true` set — the deferred loading of definitions is cancelled for them, and all of their tools are described at start-up. The colleague set the flag so the tools "would not get lost".
- **The cost.** An hour spent going over the decisions lost in the compaction again. One edit had managed to go out into the branch on a decision he had already reversed by then.

> Over the whole task he reached for one server out of four. The cost was paid for four.

## Speaker notes

The issue tracker in the project connection file is his own, from the section's first case. He assembled it: he listed the operations, crossed out the surplus permissions, hid the key in an environment variable, chose the project scope so that the connection would travel together with the repository to the whole team.

Three more servers were added to the same file by a colleague, for his own work: a browser-control server, a server for access to a database, a documentation server. The scope is the project's — which means those three got connected at his place too, at the same moment he once again opened a session in his own repository. The property that had been paid for deliberately came back from its other side: a connection travels with the repository in both directions.

What he noticed. On a long edit the agent compacted the conversation noticeably earlier than it had on the same kind of task a week before, and after the compaction it re-asked what they had agreed at the start. Compaction is a standard thing: when the context fills up, the conversation gets condensed, and some of the detail is replaced by a paraphrase of it. What was noticeable here was the shift in the moment: the condensing came earlier than usual.

What it is made up of. He looked at what lies in the context before his first question: the system part from the client, the project's instruction files, the tool definitions of four servers. In the other person's lines of the connection file he found the field `alwaysLoad: true` on two servers. It cancels the deferred loading of definitions: all of those servers' tools are described at start-up in full. The colleague set the flag for an understandable reason — so that the tools would not get lost and would be available at once.

The cost. An hour spent going over the decisions lost in the compaction again: what has already been agreed, what has been reversed, which of the two options was chosen. One edit had managed to go out into the branch on a decision he had already reversed by then — it had to be rolled back separately.

The count. Over the whole task he reached for one server out of four. The cost was paid for four.

The scene is a teaching one, like every scene in the seminar: the project is real, the situation is assembled out of typical ones. The shares of the context in it are deliberately not named — the measured numbers come later in the case and always with a source, because a teaching estimate passed off as a measurement would cost more than the absence of a number. The field `alwaysLoad: true`, meanwhile, was not invented for the scene: it is in the documentation, and the documentation names its cost outright — every tool described up front takes up room that would otherwise have gone to the conversation.

Asserting that the compaction came precisely because of the servers is not possible from one observation, and the scene does not assert it. Compaction comes when the context is full; tool definitions are one of the items filling it, taken up before the work begins. The share of each item is different for everyone and is checked the same way he checked it.

The colleague's right to add to that file raises no questions: the file is one, it lies in the repository under shared version control, and an edit to it is an ordinary commit. The project scope is the project's precisely for that. Choosing it in the first case meant buying exactly that property: the connection arrives together with the repository, and nobody has to assemble it again. Its side effect is visible here — everyone who opens a session pays with context, including those who do not need those servers in any task at all.
