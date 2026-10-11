---
id: n62
type: code_artifact
duration_min: 1.5
assertion: "Two files from this class and the rule line about working copies will stay nothing but a plan: the demo repository is not built any further, and that is said directly, not hidden"
learning_goal: "A diagram, not a capture of the tree: the same way of marking honestly that the bridge of this same seminar has already used for the skill. A class about the boundary of an agent's context does not hide its own unfinishedness: the demo repository is not built any further, and that is said directly, with the same marker as the skill's"
visual:
  pattern: state_cards
  primary: >
    The leading line is the marker "A DIAGRAM, NOT A SNAPSHOT". Under it — a light table-box of seven
    rows, not a dark terminal: the top four rows repeat the bridge's table unchanged
    (hook, skill, CLAUDE.md, DECISIONS.md), the three new rows are today's rungs and the order of work
    with copies, all three with the marker "planned, no commit". At the bottom as a caption — the slide's only caption.
  backup: >
    The source: `rework/block-3-os.md` §A.2. The demo repository is not built any further
    (`SPLIT-PLAN-6-7.md` §1, the owner's decision): the MCP and subagent artifacts will not appear in
    `tellina-study/signup-landing-demo`. The marker on both is the same as the skill's on this seminar's
    bridge: "planned, no commit". The names `.mcp.json` and `diff-reviewer.md` are not
    invented — they are the artifacts of case 1 of each rung, confirmed by the material in full
    (`research/setka-keysov.md` §1.1, §2.1); confirmed during the stitching — the delivered sections
    use exactly these paths unchanged (`section-1-mcp.md` §A.1.7,
    `section-2-subagent.md` §A.1).

    The owner's round of edits (issue 225, §A4): the monospaced listing with two versions of the repository
    (the former form of this slide, mirroring n02) was replaced by a light table — the rule
    "dark code blocks and terminal insets are converted into a light form" applies to the whole deck, not
    only to the slides named. The division into "branch main" / "branch seminar-5-hook" was removed by the same
    decision as on n02: that is an internal detail of the git history rather than a state an engineer reads
    when opening the project.

    Revision (issue 225, round 2, checking the slide against the section): the same finding as on n02 of this
    seminar — six separate blocks of `**Name**` + path + status separated by a blank line are not recognized
    by the parser as separate cards (its `cards` format is one line, with items separated by "·"), and the
    text collapsed into one run-on paragraph. Replaced with a table of the same form as
    on n02/n03/n61 of this seminar; the facts and the paths did not change.

    The round of edits after the classes were held (issue 225, `qa/RAZBOR-PROVEDENIYA.md` §B.3): a seventh
    row was added to the table — the order of work with working copies, added into the already existing
    `Repository etiquette` section of the `CLAUDE.md` file. The artifact is taken apart on a separate slide of the working-copies
    case (`n55`); here it only takes its place in the diagram with its status. The count in
    the caption and in the slide's assertion was raised from "two files" to "two files and the rule line";
    the status of the new row is the same as that of the previous two. The other six rows, their statuses and
    their order are untouched. This is the only edit to an existing slide made by the material
    session after the classes were held — the overlap with the terminology session is named in its report.

    Storytelling revision (issue 225, `PERESMOTR-STORITELLING.md`, cause 4): the screen is
    untouched — neither the table, nor the honest markers, nor the caption. Three sentences were added to the speech, tying
    the two new rows of the diagram to the two moves of the seminar (bring inside / carry outside), so that the
    diagram reads as a continuation of the resolution begun on `n61` rather than as a separate inventory.
    The notes were supplemented with two answers (where to look at the assembled files in full; why the hook has
    a commit and the skill does not) — up to the notes norm of round 4.
---

# What appeared in the repository

## Assertion

Two files from this class and the rule line about working copies will stay nothing but a plan; the demo repository is not built any further.

## Visual

**A DIAGRAM, NOT A SNAPSHOT**

| Rung | Path or artifact | Status |
|---|---|---|
| Hook | `.claude/settings.json` + `.claude/hooks/selftest-branch-guard.sh` | there is a commit |
| Skill | `.claude/skills/deploy/SKILL.md` | planned, no commit |
| CLAUDE.md | 40 lines / 5 sections | there is a commit |
| DECISIONS.md | the repository's documentation layer | unchanged |
| MCP | `.mcp.json`, permissions struck out down to three operations | planned, no commit and there will not be one |
| Subagent | `.claude/agents/diff-reviewer.md`, `tools: Read, Grep, Glob` | planned, no commit and there will not be one |
| Working copies | `CLAUDE.md`, the `Repository etiquette` section — two lines: a copy per task, merge and clean-up at the end | planned, no commit and there will not be one |

> "Two files from this class and the rule line will stay nothing but a plan. They will not be in the public repository — and that is said directly, not hidden."

## Speaker notes


The marker "a diagram, not a snapshot" in the top line is part of the content. The seven rows below show what the project has and what confirms it, and the last three have no confirmation.

The top four rows stand as they did at the start of the class: the hook with a commit, the skill planned, `CLAUDE.md` at forty lines and five sections, the documentation layer `DECISIONS.md` unchanged. Three new rows are today's, and two of them are new files. `.mcp.json`, the connection file, in which the permissions are struck out down to three operations: read open issues, write a comment, create a draft edit. And `.claude/agents/diff-reviewer.md`, the subagent's file, whose `tools` field holds three tools — `Read`, `Grep`, `Glob` — instead of all the available ones.

The three operations in the connection file are what remained of the four permissions a broad personal access token grants by default. Access to all of the user's repositories, including private ones, is struck out: the list of operations does not need it. Managing settings is struck out, deleting is struck out. Of reading and writing, both remained — you cannot read issues and write a comment with a draft edit without them. What remained is one repository, reading issues and creating a draft; all the work of trimming the permissions was done before connecting.

Both files carry the marker "planned, no commit and there will not be one". The demo repository is not built any further: that is a decision taken in advance and announced directly. Two classes with the material on access to the outside and on trimmed permissions worked through are worth more than one class with the demo repository built out to the end. This is said directly for the same reason the class spent the whole hour on the difference between what is written and what is already working: hiding that same difference in its own outcome would be strange.

The file names were not invented to fit the diagram. Both were assembled in class line by line: the connection file in the first case of the MCP section, together with the order for resolving a name conflict between configuration scopes; the subagent's file on the rung's one-pager, where all six of its parts are taken apart. The paths are the same, with no discrepancies. For each of the two, which line is responsible for what is named on its own screen, and so is what is not in the file: for the connection file the key's permissions lie outside the file, in an environment variable, and are trimmed separately from it. The diagram here shows only the status of each row.

It is worth noticing what these two rows are. One brings inside what is not inside. The other carries outside what does not fit inside. The two moves with which the class answered both misses look, on this project, like two files at known paths — written, taken apart line by line, and not committed.

The seventh row stands apart from the previous two, and the difference is worth naming. The two files are new artifacts at new paths. The rule line about working copies is added into a file that already exists in the project and already contains rules of the same kind: the order of work in the repository, with the requirement not to commit straight into the main branch. The class adds two points there — a copy per task, and the merge with clean-up at the end. That is how an instruction file accumulates: a line per class, each one in the place of the case that called for it.

The marker "planned, no commit" was put there by the previous class already, and for the same reason: the hook was set up and tested on a live repository, the skill was taken apart part by part but never got as far as a commit. Today three more of the same kind have been added to it. What the material taken apart is then checked by is taken apart by the last screen: part of today's material is checked by a command, part is not, and which is which is named.
