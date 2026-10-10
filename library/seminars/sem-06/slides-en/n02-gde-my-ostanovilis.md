---
id: n02
type: code_artifact
duration_min: 1.25
assertion: "Four things are already in the repository: the hook is confirmed by a commit, the skill remains only a plan, the instruction file has grown, the documentation layer with the decisions is in place — and all four lie inside, which is why the agent held the project whole"
learning_goal: "The state of the repository read off the screen rather than reconstructed from memory of the previous class: what is confirmed by a commit and what is only planned. As its second job, the slide explains the miss from the cover: everything listed lies INSIDE, and as long as the work was here, the agent did not miss. The one question addressed to the listener in the opening is placed here too"
visual:
  pattern: state_cards
  primary: >
    A lead line about the point the seminar carries on from. Under it — a light table-box of
    four rows, not a dark terminal: "hook" (has a commit), "skill" (only a plan, no commit),
    "CLAUDE.md" (more lines and more sections now), "DECISIONS.md" (the documentation layer, no
    change). At the bottom, as a full-width caption — the slide's one closing line.
  backup: >
    Source: `rework/block-0-mostik.md` §A.2, verified by reading the tree directly
    (`ARCHITECTURE.md` §3): `.claude/settings.json` and
    `.claude/hooks/selftest-branch-guard.sh` are confirmed by commit `9803643`;
    `.claude/skills/deploy/SKILL.md` exists only in the plan of the skill section, it has no
    commit; `CLAUDE.md` grew from 24 lines / 4 sections to 40 lines / 5 sections — also
    confirmed by a commit; `DECISIONS.md` has been part of the repository's documentation layer
    since Seminar 4 (`sem-05/ARCHITECTURE.md` §2), the previous class did not change it and here
    it is shown with no change — what has already been set up does not get lost between
    classes. The owner's round of edits (issue 225, §A2 of the map): the slide's previous
    form — a monospaced listing of two versions of the repository one under the other in a dark
    code block — was replaced by a light table; the mention that the hook and `CLAUDE.md` lie
    separately from what anyone who simply clones the repository will see was removed from the
    slide entirely, as an internal detail of git history rather than a state that an engineer
    opening the project reads. The table shows the four things as they stand now, with no
    explanation of where in the repository's history each of them lies.

    The storytelling revision (issue 225, `PERESMOTR-STORITELLING.md`, reason 3 + rule P5). The
    table and its honest labels are kept without a single edit — they work. Two things changed.
    The closing line: instead of enumerating the four rows ("the hook is confirmed by a commit,
    the skill remains a plan…"), which the table already reads out by itself, it now names what
    those four rows have IN COMMON — all of them lie inside the repository — and by that
    explains the miss from the cover. And the one question addressed to the listener in the
    whole opening (rule P5) is placed here too: does the agent hold the listener's own working
    project whole. It stands in the second minute deliberately — from here on the room watches
    the material already trying it against its own repository.

    Revision (issue 225, round 2, the slide checked against its section): the original "cards"
    form — separate blocks of `**Title**` + path + status, separated by a blank line — is not
    recognized by the `slide_parts.py` parser as separate cards (the `cards` format there is ONE
    line, items separated by "·" with backticks, not paragraphs separated by a blank line); such
    text collapsed into one run-on bold paragraph with no line breaks, which directly
    contradicted the description "four separate cards" in this same `backup`. Replaced by a
    table ("Rung" / "Path or artifact" / "Status") — the same form that already renders
    correctly on `n03`/`n61` of this seminar; the facts did not change.
---

# Where we left off

## Assertion

The hook is confirmed by a commit, the skill remains only a plan, the instruction file has grown, the documentation layer is in place.

## Visual

| Rung | Path or artifact | Status |
|---|---|---|
| Hook | `.claude/settings.json` + `.claude/hooks/selftest-branch-guard.sh` | has a commit |
| Skill | `.claude/skills/deploy/SKILL.md` | only a plan, no commit |
| CLAUDE.md | was 24 lines / 4 sections → now 40 lines / 5 sections | has a commit |
| DECISIONS.md | the repository's documentation layer | no change |

> "Four things, and all four of them inside the repository. As long as the work was here, the agent held the project whole."

## Speaker notes


The table on the screen is the state of the project as we enter the seminar, and it is worth reading by two signs at once: what the project has, and what confirms it.

The hook is the settings file `.claude/settings.json` and the self-test `.claude/hooks/selftest-branch-guard.sh`. It has a commit, `9803643`: the repository can be cloned with `git clone` and you can see for yourself that both files are in place, and `git log -1` on that commit will print the same number. The skill — `.claude/skills/deploy/SKILL.md` — was written in the breakdown of the previous class, but it has no commit, and the table carries the honest label "only a plan". There are no grounds here for passing a plan off as a fact: the previous class was devoted to that very discipline. The instruction file `CLAUDE.md` has grown: it was twenty-four lines and four sections, it is now forty and five — also confirmed by a commit, and `wc -l CLAUDE.md` prints forty. `DECISIONS.md` is the file with the decisions that were taken as the project went along. It has been in the repository since an earlier class, the previous one did not touch it, and here it is shown with no change: what is set up once is not lost between classes.

Those four rows have something in common, and it explains Monday's miss. All four lie inside the repository. A rule, a procedure, a check, a recorded decision — everything that was set up across two classes in a row, the agent opens by itself, at any moment, with nobody's involvement: it is enough that these files are in the project's tree. As long as all the work lived here, the agent held the project whole and answered to the point. The miss happened on the day part of the work turned out to be beyond that boundary: none of the four rows reaches there, and the number of rows changes nothing about it.

It is worth holding this same table up against your own working project. The question is simple: does your agent hold it whole — or do you explain the same things over again in every new session? The second case is ordinary, and it means exactly what this table means: part of what is needed lies beyond the boundary of what the agent sees by itself. What to do about that depends on which part went past the boundary. The seminar gives two answers to it, and a criterion for choosing between them.

The line "has a commit" deserves a pause, because it is what separates what is set up from what is intended. A file that has a commit lies in the project's tree: anyone who has cloned the repository sees it, and the agent opens it by itself, without a reminder. A file that was broken down in a class and never entered into the repository does not exist for the agent at all. The difference between those two states was the content of the previous class, which is why every row of the table carries its own label: one common list of files cannot convey that difference. What the table does not show is where in the repository's history each row lies: for an engineer who has opened the project that is an internal detail, and the state of the project does not depend on it.

Knowing the previous class in order to read on is not required. This table and the axis on the next screen are enough: they hold everything about the two earlier rungs that is needed today.
