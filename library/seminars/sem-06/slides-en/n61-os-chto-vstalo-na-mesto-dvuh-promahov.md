---
id: n61
type: recap_table
duration_min: 1.5
assertion: "In the place of Monday's miss stands the third row of the axis, in the place of Wednesday's the fourth; with four rows the seminar's axis is closed"
learning_goal: "The close begins by returning to the person and to the two misses the seminar opened with, and shows what has taken their place: the hook and skill rows are carried over verbatim from the bridge of this same seminar, MCP and subagent are filled in from the breakdown of today's two sections"
visual:
  pattern: recap_table
  primary: >
    A table of four rows, the same look as on n03: now all four are filled in. Two
    substantive columns — "what it does" and "what it does not do / the limit" — plus a short
    column "prevent / settle". At the bottom as a caption — the slide's only caption: it
    names which row has taken the place of which miss.
  backup: >
    The source: `rework/block-3-os.md` §A.1. The "hook" and "skill" rows are carried over verbatim from
    the n03 table of this same seminar — unchanged, the room has already seen them on the bridge. The "MCP" and
    "subagent" rows were supplied during the stitching from the axis line of case 1 of each section
    (`research/setka-keysov.md` §1.1/§2.1, `section-2-subagent.md` A.1 "The axis line"; MCP had
    no axis slide of its own, the wording was assembled from §A.00/§A.1.3/§A.1.5 of the same section
    during the stitching). The cell format is the same as the hook's and the skill's.

    The owner's round of edits (issue 225, §A1+§A5): the "process" row was removed entirely —
    the seminar's ladder ends on the subagent, four rows are the whole axis of this seminar, not four out of
    five. The columns "what the arrangement promises" / "what the test showed" were replaced by "what it does" /
    "what it does not do — the limit", by the same method as on n03. The right-hand cells of MCP and the subagent — the
    densest on the slide — were slightly compressed (MCP: the chain "first… then… next" replaced by
    arrows; subagent: repetitions of "this" and the words "so much"/"at all" removed with no loss of sense) —
    the facts, the figures and the source did not change. Correction (issue 225, fact-check round 2,
    2026-10-05): the MCP cell was quoting the conclusion of the breakdown of access methods ("first whether it is
    needed at all, then the permissions, then the cost") in a wording the round of edits had already replaced with another
    (the n12 breakdown now ends with a choice between a remote and a local server, not with an order of
    three questions) — the quote did not reflect what the breakdown now says. Replaced with the single
    fact that remains true and is confirmed by n19: permissions are trimmed before connecting, not after, and
    without the struck-out line a documented exfiltration is reproduced.

    The second roast (issue 225, P2, methodologist): the "prevent / settle" column at the MCP row
    called the whole section "prevent", although by ARCHITECTURE.md §4 the axis of the MCP section is mixed —
    case 1 really does prevent, by trimming permissions before connecting, whereas cases 2 and 3 settle: how to
    check what has already been connected, what to do with what has already been approved. The row rested only
    on the logic of case 1. The edit — a short mixed wording, "prevent on the way in, settle afterwards", instead of
    "prevent — check before connecting": it carries both halves of the section without the cell growing.
    The "what it does" column did not change — it was already naming the fact correctly.

    The second roast (issue 225, P1-3): the gold on this slide was not being applied (0 gold pixels,
    measured on the PNG) — `GOLD_QUOTE_SIDS` declares `n61` gold, but the genre function
    `g_axis_table` was not reading that declaration. The fix is in `build_sem06.py` (see the comment above
    the function), not here: the text and the structure of the slide were not changed for the sake of this finding.

    Storytelling revision (issue 225, `PERESMOTR-STORITELLING.md`, cause 4 "the close takes
    inventory instead of resolving"). The slide used to open the close with the words "The axis is closed: four
    rows" — a report on work done, which resolves nothing. The seminar opens with two misses by one
    person (`n01`, `n04`); the third and fourth rows of this table are exactly
    what has taken their place, and before the revision that coincidence was named nowhere. The edit
    to the headline and the caption: the headline names the resolution ("What has taken the place of the two misses"),
    the caption separates the misses by row. **The table is untouched to the character** — all four rows,
    both of its columns and the order of the rungs are the same; the edit lives in the headline, the caption and the speech.
    The speech was rewritten around the return to Monday and Wednesday, the facts of the MCP and subagent rows in it are the same.
---

# What has taken the place of the two misses

## Assertion

In the place of Monday's miss — the third row; in the place of Wednesday's — the fourth.

## Visual

| Rung | Prevent / settle | What it does | What it does not do / the limit |
|---|---|---|---|
| Hook | Settle — the rule has already been broken | Rejects one pattern of writing into `main` out of six ways of committing | On the other five it is silent; a person with a terminal it does not see at all |
| Skill | Settle — on a signal that the instruction file is overloaded | Loads a file on an exact match of the trigger description | Without an exact trigger it will not fire at all — the file's contents are not in the context until it fires |
| MCP | Prevent on the way in, settle afterwards | Trims the permissions before connecting, not after | Without the struck-out line "all repositories, including private ones", a documented exfiltration is reproduced (Invariant Labs, May 2025) |
| Subagent | Settle — on a signal that reading has crowded the work out | Delegates a task for free, without a single line of configuration; the reading goes off into the subagent's context, and a result comes back | It does not divide the working directory: the workers edit where the work lies, and collisions are removed by a zone layout |

> "Monday is closed by the third row, Wednesday by the fourth. Four rows are filled in, the seminar's axis is closed."

## Speaker notes


The close begins with the same person the seminar began with. On Monday the agent answered from the repository, and two of the client's requests were not in the answer: they were not inside at all. On Wednesday, already in a real product, it read everywhere the limit on members could be checked, assembled a correct list of four places — and asked again about what had been explained to it that morning: the reading had eaten the room the work itself was sitting in. The third and fourth rows of this table are exactly what has taken the place of those two misses.

The third row, Monday. MCP gives the agent access to a system outside, and the permissions on that access are trimmed before connecting, not after. The order has a cost here, and it is documented: in the case examined in that section (Invariant Labs, May 2025) the agent was working with a token covering all of the user's repositories, including private ones; in a public repository there lay an ordinary-looking issue with an instruction to collect data about other repositories and publish it right there; the developer asked the agent to deal with the open issues, the agent honestly read them, the instruction landed in the context as a task, and the contents of the private repositories rode off into an automatically created public pull request. The line "all repositories, including private ones", struck out during the co-building, closes that scenario entirely: there is nothing to read. The "prevent or settle" column at this row is mixed — on the way in the section prevents, further on it settles what has already arisen: how to check what has been connected, and what to do with what has already been approved.

The fourth row, Wednesday. Delegating a task to a separate worker can be done for free, without a single line of configuration: the reading goes off into the subagent's context, and a result comes back into the session. What this row does not do — it does not divide the working directory. A subagent works where the calling session stands, and several workers edit the very same files; collisions are removed by a zone layout, delegation by itself does not remove them.

Why Monday is closed by MCP and Wednesday by the subagent follows from what was missing. On Monday what was needed was not inside at all, and a context of any size does not change that: what helps is access to a system that lives apart from the project. On Wednesday everything needed did fit inside and crowded the work out: what helps is somebody else's context, where the reading is done for us and a result comes back.

The "what it does not do" column at the new rows is read by the same criterion as at the hook and the skill. That is how a mechanism is described before it has been measured; here what is shown is where what it actually does comes to an end. And by the same criterion both of today's rows stand next to the two earlier ones: the hook and the skill were carried over from the start of the seminar unchanged, the order of the rungs is the same — hook, skill, MCP, subagent. Four rows are filled in, and that is the whole axis of the seminar.

The measurements the two new rows rest on lie in different places. For MCP — in the product documentation and in a particular server's card inside the session; they are not in the repository. For the subagent — with you yourselves: `git worktree list` prints whether there is even one separate copy of the repository and how many sessions are standing on one directory right now.
