---
id: n14
type: answer_breakdown_table
duration_min: 0.75
assertion: "Both separate-search methods hold the same low cost at any base size — keyword pays in accuracy, vector pays in a preparation step"
learning_goal: "Breakdown right after the measurement results (an A1 derivative). 4-column form 'Action · How it works · Advantage · Drawbacks' (rule A5), numbers from the previous screen (n10). Part 2 of 2 (continuing n13 — append everything to the prompt). Letter suffix brought to the deck's attention (tools/seminar-production/README.md §1, issue #311)."
visual:
  pattern: answer_breakdown_table
  primary: >
    A table: action · how it works · advantage · drawbacks. Two rows —
    "search by keyword" and "put it in a vector store."
  backup: >
    Breakdown text — SETKA-KEYSOV.md Case 1 / rework/section-1-khranenie-
    bazy.md, "Breakdown." Numbers are the same as n10's.

    The "How it works" column for the "search by keyword" action says
    "with no model" about THE SEARCH STEP ITSELF (keyword is a word
    overlap, with no model) — this doesn't contradict n13's model tile,
    which is about the answer, not the search.
---

# What the measurement confirmed: searching by word and by meaning

## Assertion

Both methods hold a constant low cost regardless of base size — but they pay for it in different ways.

## Visual

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| Search by keyword | Overlap of the query's words and the document's, with no model | Cheap and fast regardless of base size (~$0.00005) | Retrieval recall@1 = 0.8 at all four sizes without change: holds exactly in place regardless of the base's volume — the cause is comparing words without accounting for case endings (breakdown — a separate beat) |
| Put it in a vector store | The query's embedding is compared against the base's chunk embeddings; only the found chunk goes into the prompt | The prompt holds ~270 tokens and ~$0.00005 regardless of base size; retrieval recall@1 = 1.0 at 10/50/200 documents | Needs a separate preparation step (split the base, compute embeddings) before the first question arrives; recall@1 dips to 0.9 at 500 documents — at that scale, neighboring paragraphs of the same article start confusing the semantic search (breakdown — a separate beat) |

## Speaker notes

The two remaining actions, instead of appending everything to the prompt, search only for the needed chunk — and both hold the cost and the prompt's volume constant regardless of base size, unlike what we just saw.

Search by keyword makes not a single call to the model at the search step: it's a comparison of the query's words against the document's text. Cost and speed don't depend on base size at all here — searching five hundred documents costs the same as searching ten. But the needed chunk isn't always found: retrieval recall@1 equals 0.8 at each of the four sizes, and that number doesn't move up or down as the base grows. Since it's already identical at ten documents, where there are no distractors at all, the cause isn't the base's scale — it's the word-comparison method itself, and that gets its own breakdown, next beat.

Put it in a vector store works differently on a technical level — here numeric representations of meaning, embeddings, are compared — and economically it behaves the same way search by word does: constant cost, constant prompt volume. Recall@1 here is higher than keyword's — one at 10, 50, and 200 documents — but it has its own weakness too: at five hundred documents, recall@1 dips to 0.9. The price of this action is a separate preparation step that has to happen once, before the first question arrives: split the base into chunks and compute an embedding for each.

What unites both actions is the main thing: cost doesn't depend on the base's volume, and that's exactly what makes them candidates to replace prompt-stuffing. Which of the three actions closes Olga's need as the base grows is already obvious by this point in the breakdown, but how the solution's architecture looks, and how it's actually assembled on the real rig — next.
