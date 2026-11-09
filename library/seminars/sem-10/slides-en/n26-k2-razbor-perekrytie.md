---
id: n26
type: answer_breakdown_table
duration_min: 0.65
assertion: "Word-boundary chunking and chunking with overlap are two cheap patches on the first method: both reduce the rate of breaks without reaching the level of sentence-boundary chunking"
learning_goal: "Qualitative breakdown of actions 3-4 of Case 2, continuing n25 (owner's requirement: the breakdown follows the question directly). The breakdown explains the mechanism and the qualitative pros/cons without a single result number. Part 2 of 2 (n25 — actions 1-2: the two fundamentally different ways). Regrouped 2026-11-04 per the owner's note: it used to be 3+1 rows (visually read as '3 analyzed, the fourth tacked on'), now it's 2+2 — two fundamentally different ways kept apart from two patches on the first one, equal visual weight with n25 (issue #311)."
visual:
  pattern: answer_breakdown_table
  primary: >
    Table: action · how it works · advantage · drawbacks. Two rows — the
    two cheap patches on the first method (by word boundaries, by
    character count with overlap). No numbers on the frame.
  backup: >
    Text — the number-free version of n33-k2-razbor.md, the same method
    as n25.
---

# Two patches on the first method: by words and with overlap

## Assertion

Word-boundary chunking and chunking with overlap are two cheap patches on the first method: both reduce the rate of breaks without reaching the level of sentence-boundary chunking.

## Visual

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| Cut by word boundaries | The document is split into words; a chunk accumulates until it exceeds the target size, and the cut falls only at the boundary between two neighboring words | Doesn't tear a word in half; simpler to implement than parsing sentence boundaries — all it needs to know is where a word ends | This method knows nothing about sentence boundaries: the cut can still land right in the middle of a phrase, even if no word is touched |
| Cut by character count with overlap | The same logic as cutting by character count, but neighboring chunks overlap — part of the characters at the end of one chunk repeats at the start of the next | Part of the answers torn at the first action's boundary end up falling entirely inside the neighboring overlapping chunk | The store grows due to character duplication; overlap doesn't guarantee a result for an answer of any length |

## Speaker notes

The third and fourth actions are two cheap patches on top of the first cutting method: both reduce the number of broken answers, while the underlying "cut by character count" principle stays the same.

Cutting by word boundaries is an in-between option, between the first action and cutting by sentences. The document is split into separate words, a chunk accumulates until its total length approaches the target size, and the cut falls strictly at the boundary between two neighboring words. A word is never torn in half — that's the difference from the first action, and it's simpler to implement than parsing sentence boundaries: all it needs to know is where a word ends. What this method can't do is know where a thought ends: the cut can still land exactly in the middle of an answer, even if no single word is touched.

Cutting by character count with overlap works the same way as the first action, with one addition: neighboring chunks partially repeat the same stretch of text. If the first action's cut tears an answer at its boundary, the overlapping chunk gets a chance to contain that same stretch in full — at the cost of part of the text in the store being duplicated, with no guarantee that the chosen overlap size is enough for an answer of any length.

This action stands apart from the first three. It's an add-on on top of the simplest and crudest of them, cutting by character count with no regard for the text: no new cutting principle is introduced here. The idea is intuitively clear: if a cut is bound to land badly somewhere, let the neighbor provide a backup. But that backup has a concrete engineering cost that needs to be weighed just as seriously as the gain: with an overlap equal to a third of the chunk size, the store grows by roughly that same third. This cost isn't one-off: the growth is constant and proportional to the size of the base.

From outside, at the level of the rest of the chain, there's no visible difference between any of the four actions: all four feed the same format into the next step — a list of text chunks ready to have an embedding computed for each. The entire difference is hidden inside one node — which is exactly why it's easy to miss until you check the result by the numbers.

Four actions have now been broken down, and none of them was named correct in advance — each has its own mechanism, its own advantage, and its own price. That's what we'll turn to next: the structure of the measurement, and then the result on real documents, which will show which of these prices is actually worth paying in practice.
