---
id: s32
type: comparison_table
duration_min: 1
assertion: "The difference between the layers is not in the format, but in who initiates the entry, who will see it afterwards, and by what mechanism it gets into the context at all"
learning_goal: "Table of the four layers of writing: instruction file / auto-memory / DECISIONS.md / complex memory system — by authorship, where it lives, loading mechanism, review and portability; the table comes before the breakdown of the vote"
visual:
  pattern: comparison_table
  primary: "A four-column table filling the whole slide. The fourth column (complex memory system) is set apart visually by a thin line — it is not an equal candidate for today, but the next order of complexity. Under the table — four mechanical details, one line each."
---

# Four layers of writing

## Assertion

The difference between the layers is not in the format, but in who initiates the entry, who will see it afterwards, and by what mechanism it gets into the context at all.

## Visual

| | Instruction file | Auto-memory | `DECISIONS.md` | Complex memory system |
|---|---|---|---|---|
| Who writes it | you, in advance | the agent, as it goes | you, at the moment of the decision | the service: it extracts it from the work itself |
| Where it lives | in the repository, in git | outside the repository, on this machine | in the repository, in git | outside the repository, in a separate database or service |
| What gets loaded | all of it, automatically, every session | the index: the first 200 lines / 25 KB | nothing automatically — an ordinary file, the agent reads it on its own initiative or on an explicit pointer | nothing automatically — the service itself picks what to supply on request |
| Goes through code review | yes | no | yes | no: nothing sits in the repository, there is nothing to show at review |
| Survives a change of machine | yes | no | yes | yes, if the service is reachable from both |
| What goes into it | stable rules and boundaries | preferences, confirmed approaches | decisions and their "why" | whatever the service deemed worth writing down |

Under the table — four lines: the memory index is only an index · the agent itself skips what is derivable from the code · only files on disk survive context compaction · complicating the layer does not improve the result by itself: on small corpora a simple file regularly beats external systems.

## Speaker notes

One criterion of distinction, in one phrase: the difference is not in the format — the first three layers are all markdown — but in who initiates the entry, who will see it afterwards, and by what mechanism it gets into the context. You write the instruction file in advance, and it loads itself. Auto-memory is written by the agent, for itself, on this machine, without review. You write the decision log, for the team, into the repository, through review — but it does not load itself: the agent opens it on its own initiative or on an explicit pointer.

The fourth column is an external memory system: a vector or graph database, a separate service. There the entry is not composed by a human: the service extracts facts from the work itself and decides by itself what to supply into the context on request. On the plus side — it survives a change of machine, unlike auto-memory. On the minus side — nothing sits in the repository, which means no change history and no review, and you do not control the wording of the entry. And the gain from it is not automatic: on small corpora a simple file regularly beats it — the measurements for that are on the failure slide.

Four details, briefly: the memory index is only an index, beyond two hundred lines the content physically does not make it into the session; the agent itself skips what is derivable from the code; only files on disk survive context compaction — what was only said in conversation can disappear when the context is compacted; and complicating the layer does not improve the result by itself. The third detail is a direct answer to the previous section: the plan of "I'll explain it to the agent again as we go" does not work even inside a single long session.

Now, with this table in hand, let's go through what the room chose.
