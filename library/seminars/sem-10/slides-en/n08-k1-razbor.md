---
id: n08
type: answer_breakdown_table
duration_min: 1.0
assertion: "Three actions solve the same task by different means — which one survives the base's growth, this beat still doesn't say"
learning_goal: "Qualitative breakdown of Case 1's three actions RIGHT AFTER the question (course-owner requirement: the breakdown follows the question directly, with no gap for the measurement-structure beats — n07 → n08 → then measurement structure and result). The breakdown explains the mechanism and the qualitative pros/cons with not a single result number, on the model of n62-k4-razbor.md; the S2 canon (`forma-keysa-s-zamerom.md`) isn't broken — before the measurement-structure beat, not one result sits on a frame. The action names repeat question card n07's cards verbatim."
visual:
  pattern: answer_breakdown_table
  primary: >
    A table: action · how it works · advantage · drawbacks. Three rows.
    No numbers on the frame at all.
  backup: >
    Text is a number-stripped version of n13-k1-razbor.md (the "How it
    works" column and the qualitative part of "Advantage"/"Drawbacks");
    all numeric values ($, %, accuracy, recall@1) from the source table
    are removed, leaving only the mechanism and the qualitative judgment.
---

# What each of the three actions does

## Assertion

Three actions solve the same task by different means. Which one survives the base's growth — the next beats, not this one.

## Visual

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| Keep appending the base to the same prompt | The whole text of the base goes to the model, in full, on every question again | Needs no preparation at all in advance — the base just sits as text in the process's settings | The bigger the base, the more text goes out on every question — the cost grows together with the base |
| Search by keyword | The overlap of the query's words and the document's text, with not a single call to the model | Cheap and fast regardless of base size; the preparation — indexing by word — is done once, before the first question arrives | Finds a word match: meaning plays no role here — a question phrased in different words may miss the chunk where the answer actually lives |
| Put it in a vector store and pull out the needed chunk | The base is turned in advance into numeric representations of meaning; a query finds whatever is closest in meaning, with no exact word match needed | Only the found chunk goes into the prompt — the size of the whole base doesn't affect the cost | Needs a separate preparation step in advance: the base has to be split into chunks and an embedding computed for each, before the first question arrives |

## Speaker notes

Three actions, and none of them is named the winner yet — this beat only explains how each one works; what it showed on the measurement comes later.

Keep appending the base to the same prompt is exactly what we did last session, only with more items. It's the simplest of the three by design: nothing needs preparing in advance, the base just sits as text where the model reads it. The cost shows up as the base grows: the model gets the entire text again on every question, and the bigger the base, the more of that text there is.

Search by keyword works differently: it's classic full-text search that compares the question's words with the document's words, with not a single call to the model. The cost of such a search doesn't depend on base size — that's its strength, and its preparation has to happen only once, in advance. But that's also its limit: words match, meaning doesn't enter into the comparison, and a question phrased in different words may miss the chunk where the answer actually lives.

Put it in a vector store and pull out the needed chunk is the action where the base is turned in advance into numeric representations of meaning, and a query finds whatever is closest by that representation, with no exact word match needed. In the end only the found chunk goes into the prompt — the cost doesn't grow with the size of the whole base, unlike the first action. The price for this is a separate preparation step that has to happen in advance, before the first question arrives: split the base into chunks and compute an embedding for each.

Which of the three actions survives the base's growth best is a question this beat deliberately doesn't answer. Next we'll see exactly how the measurement that answers it was built, and only after that — the answer itself, as a number.
