---
id: n13
type: cobuilding
duration_min: 1.25
assertion: "We settle it in two moves: first the list of operations the agent has to be able to perform, then, line by line down the broad token, we check which permissions out of that list are not needed and cross the surplus out"
learning_goal: "Co-building, part 1 of two: the operations are fixed first, then each line of the broad token's permissions list is checked for whether it is needed. The crossing-out happens on the screen, line by line. Round 2 of the owner's edits (issue 225, part A3): the word \"barrier\" was removed — we simply name what we are doing, with no invented term"
visual:
  pattern: cobuilding_config_reveal
  primary: "Two moves on one screen. Move 1 — a list of three operations, fixed by lines from the room. Move 2 — the list of a broad token's default permissions, and line by line, the crossing-out on the screen, until one account and two operations are left."
  backup: "Source — rework/section-1-mcp.md §A.1.7 (part 1), §B.6 (part1c.md). The operations and the permissions: the analogue in rework/section-1-khuk.md is not used; the list of default permissions is taken from research/stage-5-mcp.md. The .mcp.json artifact and the crossed-out screen come later in the case.
    A round of edits (issue 225, remarks 3/5 — readability): the operations of \"Move 1\" were
    written as bare text separated by \"·\" with no backticks — the parser did not recognize them
    as cards and glued the whole block (the Move 1 question + the list of operations + the Move 2
    question) into one bold paragraph with no breaks, visible in the preview as one run-on line.
    The fix — the operations were wrapped in backticks (the same card syntax as on n10/n11): now
    Move 1 and Move 2 are two separate accent blocks, with three readable operation cards between
    them, and the content did not change by a single character.
    The storytelling revision (issue 225): the slot went 1.5 → 1.25 — the 0.25 min given up went
    to n20, and the slide's speech (1.10 min) fits with room to spare. One thought was added to
    the speech about the order of the moves (operations before permissions), strengthening the
    return to this screen in the failure on n19. The screen did not change."
---

# We settle it: which operations to allow, then which permissions

## Assertion

The first move is the list of operations the agent has to be able to perform. The second is to cross out, line by line down the broad token, whatever the list does not require.

## Visual

**Move 1 — what specifically does the agent have to do?**

`read open issues` · `write a comment` · `create a draft edit`

**Move 2 — what does a broad personal access token give by default, and which of it is needed?**

| Default permission | Needed for our list of operations? |
|---|---|
| all of the user's repositories, including the private ones | no — cross it out |
| read and write | in part — reading is needed, and writing (a comment, a draft) is needed |
| managing settings | no — cross it out |
| deletion | no — cross it out |

> What remains: one repository, reading issues, creating a draft edit.

## Speaker notes

The file gets written at the end of this conversation. Starting from the syntax would mean skipping past two decisions that weigh more than the syntax does: which operations to allow the agent, and which permissions to issue for them.

The first move is a quick one: what specifically does the agent have to do? For our task the list is short — read the open issues, write a comment, prepare a draft edit. Three operations, nothing more. That list is drawn up for the task and is not taken from the server: the tracker's official server can do noticeably more than three things, and out of its full set you need to know your own. The operations set which permissions to ask for; the reverse order produces a key that is knowingly broader than the task it was issued for.

The second move carries the main weight. A broad personal access token gives four things by default: all of the user's repositories, including the private ones; read and write; managing settings; deletion. For each line the same question is asked — does our list of three operations require this? All repositories, including the private ones: no, the work goes on in one. Read and write: reading is needed for the issues, writing is needed for the comment and the draft — the line stays. Managing settings: no. Deletion: no. The crossing-out goes line by line, and what is left is one repository and two operations.

The order matters in itself: operations first, permissions after. The reverse order — take the token as it comes and see what turns out — leaves in the key precisely the line that will turn out to be decisive a few screens from now.

A temptation worth taking apart in full: create the token with the default permissions and simply not use the surplus. That will not do, and the reason lies outside discipline. A token can be used by whoever gets hold of it, and then what decides matters is what the key as made physically permits, irrespective of your intention. The question "do I use this permission" is beside the point entirely; the question is exactly one — is that permission in the key or not.

Surplus of this kind is the norm, not the exception. The same systematic sample shows that more permissions get issued than are needed, and that this concerns not only individual servers but the transport layer of the protocol's own official SDK.

How long such a check takes — there are no direct measurements in any source, and that is an honest gap. What can be said is something else: the conversation broken down into moves here happens at the moment the token is created anyway, and it requires no separate time.

This screen is worth remembering. A few screens from now there will be an incident that reproduces precisely when the top line has not been crossed out.

And the last thing — what to do when a fourth operation turns out to be needed. Come back to this same conversation and issue the key anew. Adding a permission to an existing token is cheaper, and that is exactly why a permissions list spreads over time far beyond the task it was set up for.
