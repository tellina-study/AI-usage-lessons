---
id: n05
type: lecture_map
duration_min: 1.25
assertion: "Two sections — two opposing answers to one question: bring inside what is not inside, and carry outside what does not fit inside; three cases in each, named by the observable problem"
learning_goal: "The seminar's map: where we are going inside today's two sections. The sections are named by the direction of the move, in the same words as the seminar's question on the previous screen — so that they read as two answers to one question. The names of the cases are taken word for word from the titles of their dividers, with no reformulation and no answers on the cards"
visual:
  pattern: lecture_map
  primary: >
    Two sections in the order they are broken down in, with no minutes and no methodological
    marks — the same form as the Seminar 5 map: a rung line, with three decision-point cards in
    it. The top line of each card is the observable problem, word for word with half of the
    title of the case's divider; the bottom one is "we settle it", with no answer. At the bottom,
    as a caption — the slide's one closing line, with no mention of anything beyond today's two
    sections.
  backup: >
    Source: `rework/block-0-mostik.md` §A.5. Filled in during the stitch-up from the titles of
    the dividers `section-1-mcp.md` §A.1.1/§A.2.1, `section-1-mcp-part1b.md` §A.3.1,
    `section-2-subagent.md` §A.1, `section-2-subagent-part1a2.md` §A.2 and
    `section-2-subagent-part1a3.md` §A.3. The owner's round of edits (issue 225): re-checked
    line by line against the text of the real divider files (`n06`, `n21`, `n29`, `n38`, `n50`)
    after six case sessions had rewritten part of the titles. The round-3 consolidation
    re-checked all six cells anew against the text of the real dividers on disk: MCP case 2 was
    brought into line with "…and the agent does not go through it" by that case's decision point
    (the case was later folded down, see below), and all three cells of the subagent section
    were rewritten entirely — round 3 removed the previous case "the role returned a result"
    together with the trustworthiness arc, built two new cases in its place (the focus of the
    context, parallelism) and reordered the cases into the sequence of meaning in which
    specialization comes third. The cells now read word for word off `n29`, `n38`, `n50`. The
    owner's round of edits (issue 225, §A1): the line "one rung — the process — remains ahead"
    was removed from the slide, from the note and from the reference material entirely — the
    seminar's ladder has shrunk from five rungs to four, and there is no fifth, neither filled
    nor dashed. The map names only what happens today and nothing beyond that.

    The storytelling revision (issue 225, `PERESMOTR-STORITELLING.md`, reason 3 + the section
    "The load-bearing story"). The six case cells were not touched by a single character — they
    are checked character for character against the text of the real dividers and are protected.
    Three things changed, all about the FRAME: the names of the sections ("MCP — access to the
    outside" / "Subagent — a trimmed role" → the same names, but after the named direction of
    the move), the title and the closing line. Previously the map listed two topics in a row and
    read as a table of contents. Now the first words of each line are the direction, in the same
    words as in the seminar's question on the previous screen, and the lines stand as two
    opposing answers to one question. The tool names were not taken out of the cells: the map is
    the place where they are first heard.

    Edits after delivery (issue 225, qa/RAZBOR-PROVEDENIYA.md §A2): case 2 of the MCP section
    ("the server is connected, and the agent does not go through it") was folded down to a
    single screen inside the connection case — the lecturer dropped it aloud in both groups.
    That case's cell was taken off the map, its thought moved into the cell of the first case
    ("We settle it — and check that the agent really does go through the server"), the context cell
    moved into the second column, and the third column of the MCP line is empty: there are two
    cases in that section and three in the subagent section, and the map shows that outright.
    The cells of the subagent section were not touched.

    The post-delivery consolidation (issue 225, `qa/svedenie-posle-provedeniya.md`): in the line
    of the lower section, the title the owner approved was substituted in — "subagent, trimmed
    permissions" instead of "subagent, a trimmed role". The paragraph above about the names of
    the sections describes the PREVIOUS round of edits and therefore keeps the previous wording
    verbatim: it is a record of what was changed then, not the name in force. The name in force
    for the section is "Carry outside what does not fit inside — subagent, trimmed
    permissions", and the same stands in `rendered/svodka-tekst.yaml` (the input of the
    slide-map generator) and in `rework/block-0-mostik.md` §A.5. The six case cells were not
    touched.

    The second roast (issue 225, P1-3 — "the gold accent is absent on n05, by the PNG 0 gold
    pixels"): the slide's one quote is the map's closing line, not a remark cut in by the speaker
    along the way — but the `lecture_map` device in `PATTERN_ROLE` gives the role `fact` (a teal
    card) to any quote of its own regardless of the quotation marks, unlike `recap_table` (n03),
    where no role is assigned and removing the marks is enough. It was added to
    `GOLD_QUOTE_SIDS` (`build_sem06.py`) pointwise by sid, the same way that already fixed
    n02/n61/n62/n64 — the text of the line did not change by a single character.
---

# Two sections — two answers to one question

## Assertion

One limit, two opposing moves: bring inside what is not inside, and carry outside what does not fit inside.

## Visual

| Section | First | Second | Third |
|---|---|---|---|
| Bring inside what is not inside — MCP, access to the outside | The agent regularly needs data that is not in the repository. We settle it — and check that the agent really does go through the server. | Connected servers take up context before the work begins. We settle it. | — |
| Carry outside what does not fit inside — subagent, trimmed permissions | The reading needed for one edit crowds the edit itself out of the context. We settle it. | The task arrived as a single sentence, and the deadline on it is two days off. We settle it. | There are several workers, and they have one working folder. We settle it. |

> "One and the same limit. Two moves running toward each other."

## Speaker notes


The seminar's map: two sections, and they are two answers to one question.

The first move is to bring inside what is not inside. The agent gets a way to ask the system itself — the one that lives apart from the project and changes without us — instead of working off a snapshot taken by hand. That is how Monday's miss is closed. The mechanism is called MCP, and its two cases are named by observable problems: the agent regularly needs data that is not in the repository; connected servers take up context before the work begins. Inside the first case stands a separate screen on how you prove that the agent really does go through a connected server.

The second move runs the other way — carry outside what does not fit inside. The reading goes to a separate worker with a context of its own and trimmed permissions, and only the result comes back into the session where the work lies. That is how Wednesday's miss is closed. In the documentation this worker is called a subagent; that is what it is called in the rest of the seminar too. Its three cases are also named as problems: the reading needed for one edit crowds the edit itself out of the context; the task arrived as a single sentence, and the deadline on it is two days off; there are several workers, and the working folder is one.

The cards are named by the symptom you will notice in your own work; the name of the technique is not in the title, and that is done so that it is easier to recognize your own case in the card. There is no answer on the cards either: "connected servers take up context before the work begins" describes what is visible from outside and says nothing about what treats it. The answer lies in the case itself, together with the breakdown of the options and the cost.

Every card is labeled "we settle it": not one of the problems named is hypothetical, each has already happened — in the scene its case begins with.

The order of the sections is not accidental. The first move gives the agent back what it never had; the second unloads what it already has. There is little sense in starting by unloading a context that does not hold what is needed anyway — hence access first, then delegation.

There is a connection between the two moves that the map does not show. Access to the outside increases what the agent is able to do by itself in one sitting, and along with the volume of work grows the volume of reading that the work pulls into the session's context. The moves run toward each other, and their limit is one and the same: the more the first move lets you do in one sitting, the sooner you run into the second.

Both moves have a cost of their own, and the seminar names it outright: someone else's code in your work and a permanent place in the context for the first, extra permissions and lost visibility of what was done for the second. The six cases are built the same way: a scene in which something went wrong, a question, a breakdown of the options, mechanics or an assembled artifact, a documented failure, and the criterion by which you choose.

Carrying all of this over to your own repository is the work of a separate class. Here — the techniques, and the criteria by which they are chosen.
