---
id: n06
type: section_divider
duration_min: 0.5
assertion: "The client keeps his tasks in a tracker — a separate system outside the repository, which changes every day without us; what the agent has in the chat is a snapshot taken by hand, and it is already inaccurate"
learning_goal: "The decision point of the section's first case. The divider's form is a line from the client, not the formula 'We fix what to do when…': this is the first of five dividers the room sees, and identical grammar across all the decision points turns them into a catalog of faults (the storytelling revision, P3). The line names the observable problem from the point of view of the person paying for the work, and holds the episode of scene n10 in advance; the words 'server' and 'MCP' are still not heard"
visual:
  pattern: section_divider_macro
  primary: "A dark Ocean background, the client's line in large type in quotation marks, a gold rule under it. Below it — a line of meaning: where the task lives and what the agent has. At the bottom — the section's case track."
  backup: "Source — rework/section-1-mcp.md §A.1.1, §B.1 (part1c.md). Rule A2 (the title comes from the observable problem, the tool that solves it is not named) is in force: the line names exactly the observable problem — a requirement from the task did not make it through to the work. Round 2 of the owner's edits (issue 225, A6): the divider's tag (\"4 moves of assembly · 2 layers of failure\") was removed from every case of the seminar. Case 1 of the section was carried over from sem-05/rework/section-3-mcp.md with no change of content — verified by fact-check, qa/fact-check-mcp.md §1.
    The storytelling revision (issue 225, PERESMOTR-STORITELLING.md P3): the previous title
    \"We fix what to do when the agent regularly needs data that is not in the repository\" was
    removed — it opened a row of six dividers with one grammar, and by the third repetition the
    room was starting to predict the screen. The forms were separated: a line here, other forms
    further on in the seminar. The content of the decision point did not change: the same
    observable problem, the same case, the same order."
---

# "But I did write that into the issue"

## Assertion

The client keeps his tasks in a tracker — a separate system outside the repository, which changes every day without us. What the agent has in the chat is a snapshot taken by hand, and it is already inaccurate.

## Visual

> The task lives in the tracker and changes without us. What the agent has in the chat is a snapshot taken by hand this morning.

## Speaker notes

The sentence this section opens with belongs to the client. He keeps his tasks in a tracker — a separate system outside the repository, which changes every day without the developer's involvement. And what the agent has in the chat is what was copied over for it by hand this morning. The section's scene is the Tuesday on which those two facts met; the whole section is taken up by one task — what to replace the transfer by hand with.

A tracker here is any system where a client or a team keeps a list of work apart from the code: the repository's built-in tracker, a separate task service, a board with columns. They have one property in common, and the whole section rests on it: the list lives outside the project's tree and changes without the involvement of whoever writes the code. The moment that property disappears — the list has moved into a specification file and is edited by the same commit as the code — the case falls apart, and the correct answer inside it becomes a different one.

The previous class stood on a different task. There the agent was being taught what it may and may not do inside its own repository, and that was checked with files and a command; everything that moved in the process lay in the project's tree. Here the agent needs to reach a system that is not part of the project and that we do not control directly. The difference is in where the data physically lies, and everything else follows from it: the permissions, the keys, the cost.

Why this task arises precisely now, after three tools inside the repository, is a matter of frequency. A one-off action is closed by an ordinary command in the terminal: called once, answered once. Something that repeats from session to session is not closed as cheaply, and by the end of the case it will be visible why: permanent access has a standing cost that a one-off command does not.

The tool of this section is the fourth in the course and the first that physically goes beyond the boundaries of one repository. The three before it lived inside the project's tree and were edited by the same commit as the code: they could be read, their versions compared, and rolled back. This one lives outside and is updated without our knowledge — and precisely for that reason it comes with a key and permissions that the previous three did not have.

The line on the screen belongs to the client because he is the one who noticed the requirement had gone missing: the developer learned of it last, from the question "what about the tablet?" in the issue. The cost of the mistake falls on both of them, it is presented by the one who pays for the work, and a cost like that needs no explaining.
