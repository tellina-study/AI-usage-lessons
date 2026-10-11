---
id: n31
type: mechanics_map
duration_min: 2.0
assertion: "A subagent is built out of six parts: where it is declared, how to call it and how to see
  who was called, what arrives on the input and what goes back, what each entry of the permissions
  list means, and what all of it is paid for with"
learning_goal: "The full picture of a subagent in one screen — the anchor slide of the whole rung, not
  of one case. The round-3 consolidation (issue 225): the slide was moved from the middle of the
  specialization case to the start of the section, straight after the base — in the same order as the
  MCP one-pager n09 stands before its case. All three cases, the third one's failure (state 3 of
  block 5 — the entry does not resolve) and the criterion come back to this screen. The round after
  gate B (issue 225, the owner's remark 4): the slide's previous version carried only three facts
  (input/output/permissions) — those same facts are kept unchanged, and three new blocks were added
  that had not been on any slide of the case in full before: where a subagent is declared, line by
  line down the file's fields; how to call it and how to tell an explicit call from the model's
  automatic choice; and a summary of the cost of delegation. Round 3 (issue 225,
  ZADANIE-KRUG-3-SUBAGENT.md item 2 — the same complaint that the MCP one-pager n10 has already
  measured): the smallest text on the diagram stood at 13 px, which at the slide's working width
  gives about 7.16 pt — below the deck's own threshold of 7.5 pt. The fix is in
  `make_figures_subagent.py`, not here: the point size was raised to 16–17 px (about 8.8–9.4 pt), and
  the canvas's height grew along with the margins (566 → 760 px) and takes up almost all the free
  height under the diagram instead of the previous roughly 1.5″ of empty space. The facts and the
  horizontal layout did not change. The storytelling revision (issue 225, PERESMOTR-STORITELLING.md,
  rule P6 \"the speech gets cut\"): the slide's speech was 337 words — 2.59 min against a slot of
  2.00, the rung's only overrun. It was squeezed down to 175 words with no loss of facts: all six
  blocks are still named aloud, and the extended explanations and edge cases were moved into the
  reference material (144 → 231 words), with not one detail thrown out. The screen, the diagram and
  the point size were not touched"
visual:
  pattern: mechanics_with_figure
  figure: subagent-n31-subagent-tselikom-en.png
  primary: "A diagram filling the slide, six numbered blocks each on its own backing. Two tiers of two
    blocks: 1 — where it is declared (a real piece of `diff-reviewer.md` on a light card — the name
    and the permissions verbatim, not an abstract field caption with no value — plus two lines on what
    `description:` and the body of the file do) and
    2 — how to call it and how to see who was called (explicitly / by description / the line in the
    chat). 3 — what arrives on the input (the subagent's system prompt, the task, the hierarchy of
    instructions, a snapshot of the repository — and what is not there) and 4 — what goes back (only
    the result, a one-way channel). Below, across the full width —
    5: the three states of the `tools:` entry (not specified → everything; an empty list → nothing,
    but it is alive; does not resolve → it does not start). At the bottom, as a narrow gold plate —
    6: what it is paid for with."
  backup: "Source — section-2-subagent.md §A.1 \"The artifact\" and \"The mechanics\" (blocks 1, 3, 4, 5) +
    library/seminars/sem-05/research/mechanics-6-subagent.md §1.2–1.3 and §4.1 (block 2 — an explicit
    call vs the automatic choice by description, the transcript line `<name>(<task>)`, \"general-purpose
    instead of the expected name — the routing did not work\", the verbatim quote from the quickstart
    documentation) and §2.3 (block 1 — name/description are obligatory, the rest of the fields are
    optional). Block 5, the outcome \"an empty list — alive with no tools\": confirmed by a repeat check
    (issue 225, fact-check round 2, 2026-10-05) by a direct `curl` against `code.claude.com/docs/en/errors`,
    the section \"Agent would be spawned with zero tools\" — verbatim: \"If you leave the tools list empty,
    or disallowedTools removes every entry in it, Claude Code also skips the refusal and launches the
    subagent without tools\" (the previous run through the summarizing `WebFetch` did not find this — a
    known limitation, `notes/mcp-limitations.md` `[#225-1]`). Block 6 — the harness provider's own estimate
    (Anthropic), about 15× against an ordinary chat. The caption was edited by the consolidation of the
    \"notes for the site\" round (issue 225): it used to read \"the vendor; the honest gap is in the
    evidence of the second case\", and both halves were dangling — \"vendor\" was the only instance of
    that word on the deck's visible layer, and the honest gap on n47 is about the mismatch between two
    parallel subagents, not about the cost of delegation; the figure's previous carrier, n54, was
    replaced in round 5 by the mechanics of a working copy, after which n31 remained the deck's one
    place where it stands. The gap is named outright on the spot: there are no measurements over a
    sample behind the estimate, it is an order of magnitude — in the same words the chapter names it in
    (`rework/section-2-subagent-part1b.md`, the note for n31). The owner's round 2 (issue 225): block 1
    was reassembled — the same request that enlarged the MCP one-pager n09 (\"show a mini-template of the
    file\") applied to the subagent. It was: five lines of field captions with no values
    (`.claude/agents/<name>.md`, `name:`, `description:`, `tools:`, `the body of the file`). It became: a
    real extract from `diff-reviewer.md` (n57) on a light card (`code_card`, `rendered/
    make_figures_subagent.py`) — three lines with real values (`name: diff-reviewer`,
    `tools: Read, Grep, Glob`), plus the two remaining caption lines where the value does not fit
    briefly (`description:`, `the body of the file`). The facts did not change — the same content the
    previous version carried, presented as a verbatim extract instead of abstract captions. The form
    follows the model of sem-05/slides/n11 \"The hook in full, in one screen\" (a full map in one screen
    that people come back to; the visual content lives in the diagram, the markdown body of Visual is
    empty; every block's number is a circle). The budget: the slide grew from 1.5 to 2.0 minutes — the
    growth was compensated by cuts to n54/n56/n58 of this same case
    (qa/krug-vladeltsa-subagent-keys1.md). Round 5 (issue 225, ZADANIE-KRUG-5.md, cross-cutting
    decision C1): across the slide and the diagram's canvas, \"agent\" and \"role\" were separated — the
    word \"parent\" was replaced by \"the calling session\" or \"the agent\" wherever the matter is who
    called the subagent; \"the subagents' tools\" in block 5 by \"the tools available to the role\". The
    block numbers, the facts and the layout were not touched: four neighboring slides refer to this
    screen's blocks by number. The palette has no red; the gold is the number circles and the frame of
    block 6, no less than once on the slide.
    An edit after two delivered classes (issue 225, qa/RAZBOR-PROVEDENIYA.md §A1): the term
    \"role\" was replaced across the whole deck by \"subagent\" — the lecturer stumbled over it aloud in
    both groups. The records of round 5 above are left as they were said and are to be read with that
    correction: the caption of block 5 on the canvas now reads \"the tools available to subagents\", the
    canvas was renamed to `subagent-n31-subagent-tselikom.png`, and the slide's title is \"The subagent
    in full, in one screen\".
    The figures, the blocks, the layout and `duration_min` did not change.
    Literary editing (issue 225, qa/pravki-nahodok-svedeniya.md item 4): the note's last sentence
    pointed at the diagram's panels with the word \"block\" — \"The field stands here, in the first
    block… and what each of its three states gives is in the fifth\". There is no dangling reference
    there and the panels are on the screen, but the notes are published on the site, and a reader with
    no slide in front of them divides the seminar into the MCP and Subagent sections from the first
    minute. The panels are named by the work they do, not by their number; the panel numbers, the
    diagram and the facts were not touched."
---

# The subagent in full, in one screen

## Assertion

A subagent is built out of six parts: where it is declared, how to call it and how to see who was called, what arrives on the input and what goes back, what each entry of the permissions list means, and what all of it is paid for with.

## Visual

## Speaker notes

The six parts of a subagent in one screen. All three cases of the rung come back to this screen, so it is simpler to break it down in full once.

**Where it is declared.** The file `.claude/agents/<name>.md` in the repository. On the light card stands an extract from a real subagent file: `name: diff-reviewer`, `tools: Read, Grep, Glob` — three tools instead of all the available ones. A subagent is called explicitly by the `name` field. `description` says when to call it and when not to — that is what auto-selection reads. `tools` is the permissions list, an optional field. The body of the file is the subagent's system prompt in full, that is, everything it knows about its own work.

**How to call it, and who actually got called.** An explicit call is `@agent-<name>`: it guarantees that particular subagent. The second way is to write nothing, in which case the model chooses, by description. Who was called is visible from the line in the chat: the subagent's name and the task in brackets. If `general-purpose` stands there instead of a name, the subagent was not called at all — the choice never reached it.

The routing is decided by the description, and that is worth reading literally: the model looks at `description` as the condition "when to call this subagent and when not to". It does not interpret the name, so the word "reviewer" inside a name means nothing to auto-selection. Hence the practical conclusion: a subagent's description is written as a list of occasions to call it. A job title does not work in it.

The line in the chat proves exactly one thing: the harness decided to call this subagent. It does not confirm that its work was correct — that is a separate question, with a check of its own. What it does do is separate two cases that look identical from the outside: "the subagent worked wrongly" and "the subagent was never called". Without that line people confuse the two and fix the wrong thing.

**What arrives on the input.** Four things. The subagent's system prompt — the body of its file, not the harness's prompt in full. The task, formulated by the calling session in its own words: your line does not get there verbatim. The hierarchy of instruction files — `CLAUDE.md` and `AGENTS.md` at every level. And a snapshot of the repository as of start-up.

The correspondence of the session that called the subagent is not on the input. Neither are the files that session's agent has read, nor its auto-memory. A channel for them simply does not exist, and the discipline of whoever wrote the subagent has nothing to do with it — that is the construction. For the same reason the agent does not see the subagent's intermediate actions: the task is handed over once, the result comes back once, and there is no dialogue between those two events.

**What goes back.** Only the result — the final text. Not one of the tool calls the subagent made along the way is visible to the calling session. The channel is one-way.

**The permissions — the three states of the `tools` entry.** Intuition usually confuses these three outcomes, so they are worth keeping side by side. The field is absent entirely: the subagent gets all the tools available to subagents — the opposite of what an empty space suggests. The list is specified and empty: the subagent gets not one tool and yet stays alive — it starts, reads the task and answers with what it can do by itself. The entry does not resolve: the harness does not start the subagent at all. From the outside that looks like the absence of the subagent itself — and the permissions have nothing to do with it any more.

Taking a permission away in part is not possible with this mechanism. "Read everything except one directory" cannot be written that way: the list works at the level of a whole tool, not of an individual action inside it. If you need exactly that boundary, it is held by a different mechanism.

It is also worth knowing about the exception that is easy to confuse with an ordinary call. There is a mode that inherits everything in full — the same prompt, the same permissions, the whole history; in the documentation it is called a fork. It has no isolation of the context, so the saving a subagent is set up for does not arise in that mode at all. It is not used in this class.

**What it is paid for with.** Multi-agent work comes about fifteen times more expensive than an ordinary chat — this is the harness provider's own estimate, and on the screen it stands with that attribution. There are no measurements over a sample behind it, so it is worth using as an order of magnitude: a subagent is a move that pays in tokens for a freed-up context.

The permissions field itself is not assembled in this class: the rung's three breakdowns run along other decision points. Its real values are named where the declaration of a subagent was broken down; what each of the three states gives is named where the permissions themselves were.
