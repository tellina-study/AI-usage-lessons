---
id: n03
type: recap_table
duration_min: 1.25
assertion: "The two closed rows of the axis — hook and skill — work inside the repository; the two empty ones, which are closed today, are both about its edge"
learning_goal: "The checkpoint the seminar carries on from: the same table that closed the previous class, word for word, with no change to the filled rows. The turn of the opening is to read it by a new sign: both closed rungs live inside the repository, both empty ones are about its edge"
visual:
  pattern: recap_table
  primary: >
    A light background and a table-box, not a PPTX grid. A table of four rows: the top two
    (hook, skill) are filled in completely, the bottom two (MCP, subagent) are dashed empty
    slots. Two substantive columns — "what it does" and "what it does not do / the
    the limit" — plus a short column "prevent / settle". At the bottom, as a caption — the slide's
    one closing line.
  backup: >
    Source: `rework/block-0-mostik.md` §A.3. The wording of the two filled rows carries the same
    fact as the table that closed the previous class (the file `os-dve-stroki-zakryty.md` of the
    Seminar 5 deck) — the room saw that content at the end of the previous class, and there are
    no grounds for changing it here. The owner's round of edits (issue 225, §A5): the columns
    "what the construction promises" / "what the check showed" were replaced by "what it does" /
    "what it does not do — the limit" — the previous form read as blurry. The "process" row
    was removed entirely (§A1): the seminar's ladder is hook, skill, MCP, subagent, four rungs,
    not five. The order of the rows — hook, skill, MCP, subagent — is the same as on the
    question of the next slide and on the seminar's map; it does not change, and the return of
    the question in section 3 rests on that match.

    The storytelling revision (issue 225, `PERESMOTR-STORITELLING.md`, reason 3). The table,
    both filled rows and the order of the rows were not touched by a single character — they are
    verified and protected. What changed are the title and the closing line: the previous ones
    ("Two rows closed" / "Two rows are closed. Two more are closed today.") counted rows, and
    the slide read as an item in a table of contents. They now name the SIGN by which the two
    closed rows differ from the two empty ones: the closed ones work inside the repository,
    today's are about its edge. That is the turn of the opening: the same screen read by a new
    sign, and from it the seminar's two opposite moves follow directly. The content of the table
    is meanwhile exactly what closed the previous class.

    The second roast (issue 225, P1-3 — "the gold accent is absent on n03, by the PNG 0 gold
    pixels"): the closing line was wrapped in quotation marks, which under the rules of
    `quote_role()` in `build_sem06.py` draws it as the speaker's quiet aside (a teal bar) rather
    than as a closing formula, even though it is the slide's one closing line. The quotation
    marks were removed: the `recap_table` device has no default role assigned in `PATTERN_ROLE`,
    so without the marks the line lands in the formula (a gold plate) automatically, with no
    edit to the builder's code. The text of the line did not change by a single character.
---

# Two rows closed — both about what is inside

## Assertion

Both closed rungs work inside the repository. Both of today's are about its edge.

## Visual

| Rung | Prevent / settle | What it does | What it does not do / the limit |
|---|---|---|---|
| Hook | Settle — the rule has already been broken | Rejects one pattern of writing into `main` out of six ways of committing | On the other five it is silent; a person with a terminal it does not see at all |
| Skill | Settle — on a signal that the instruction file is overloaded | Loads a file on an exact match of the trigger description | Without an exact trigger it will not fire at all — the file's contents are not in the context until it fires |
| MCP | | | |
| Subagent | | | |

> Hooks and skills work inside the repository. Both of today's rows are about its edge.

## Speaker notes


This table closed the previous class, and here it stands in the same form. Two rows are filled, each with three columns: whether we are settling something that has already arisen or preventing something in the future, what the mechanism does, and what it does not do.

The hook rejects one pattern of writing into the main branch — out of six reproduced ways of making a commit. On the other five it stays silent, and a person sitting at a terminal themselves it does not see at all. The skill loads on an exact match of the trigger description; without a match it does not fire, and the contents of its file are simply not in the context before it fires.

The short column on the left is the axis along which the course compares mechanisms with one another: does the mechanism prevent a problem that does not exist yet, or settle one that has already arisen. Both filled rows say "settle" here, and each names the signal on which the mechanism gets set up. A hook gets set up once the rule has already been broken: a write to the main branch happened once, and from then on it is rejected. A skill gets set up on a signal that the instruction file is overloaded: the instructions have grown, part of them is needed rarely, and the rare part is moved out into a separate file with a trigger description. Today's two rows will get such a label as well, and for one of them it will turn out to be mixed.

The column "what it does not do" deserves a word of its own, because it is easy to read as a list of shortcomings. It is not a defect in the mechanism and not anybody's naivety: it is what the check showed beyond the frame of what the mechanism was set up for. The hook was set up against one specific way of breaking the rule — and against that one it works. The difference between this column and the one beside it is exactly what those two mechanisms were measured for, and exactly what will repeat today on two new rows.

Now the sign by which these two rows are read on the way into today's class. Both work inside the repository, and that can be checked straight off them: the hook is a file in `.claude/` standing guard over a write to a branch of this same repository; the skill is a file in this same repository that gets pulled into the context. Neither of the two reaches out anywhere beyond the project, and neither of them carries work out of the agent's context. Everything the two classes in a row dealt with lay within the agent's reach.

The two bottom rows are empty, and both are about the edge of that reach. One is about what is not inside at all: the data lives in someone else's system, and however much context the agent is given, it will not appear there. The other is about what does fit inside and crowds the work out: the reading fits whole and takes up the room the task was lying in. Both are closed today.

The order of the rows — hook, skill, MCP, subagent — does not change from here on: the same on the seminar's question, on the map and in the closing. Comparing all four with one another makes sense because they are chosen by one sign: what exactly is missing from the work. That is the question the seminar assembles an answer to.
