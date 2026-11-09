---
id: n31
type: measured_outcome_table
duration_min: 0.75
assertion: "Character-count cutting can tear not just a sentence but a word in half — on this document, it did"
learning_goal: "Beat 3 of the measurement exposition (canon forma-keysa-s-zamerom.md §1, C2): a breakdown on a concrete document with an explicit verdict for each version (C3: INTACT/BROKEN). Part 1 of 2 (n32 — the systematic error, one document doesn't overturn the summary, conclusion): split because the 15pt floor size doesn't leave room for the table and three tiles on one slide (issue #311)."
visual:
  pattern: measured_outcome_table
  primary: >
    A short document quote with the cut boundary marked, a 4×3 table
    (version · where the cut falls · verdict).
  backup: >
    All numbers and text — verbatim from execution 2522
    (stend/raw/case2_chunking_execution.json). Chunk boundaries: v1 —
    [0,180)/[180,360)/[360,540)/[540,587); v2 — [0,189)/[190,410)/
    [411,587); v3 — [0,173)/[173,348)/[348,528)/[528,587); v4 —
    [0,180)/[153,333)/[306,486)/[459,587). Gold answer "from any
    sources" — positions 528–547.
---

# Breakdown on a real document: where the cut fell

## Assertion

In the document about cybernetics, version 1 cuts right through the word "sources" itself — the other three keep the whole answer in one chunk.

## Visual

> Document (the same example as in the test structure): "…Gordon Pask broadened the definition, including information flows from any sources, from stars to the brain." Gold answer — "from any sources", positions 528–547.

| Version | Where the cut falls near the answer | Verdict |
|---|---|---|
| Cut by character count (180) | chunk 3 ends on "…from any sour", chunk 4 begins with "ces…" — the cut at character 540 fell inside a word | **BROKEN** |
| Cut by sentence boundaries | the whole answer sits inside one chunk [411–587): "…Gordon Pask broadened the definition, including information flows from any sources…" | **INTACT** |
| Cut by word boundaries | the chunk boundary sits exactly at character 528 — right at the start of the answer; chunk 4 [528–587) begins with the word "sources" and carries the whole answer | **INTACT** |
| Cut by character count with overlap | overlap shifts the start of the last chunk back to character 459; the whole answer (528–547) fits inside the chunk [459–587) | **INTACT** |

## Speaker notes

The summary's numbers speak about the average across sixty documents. Let's look at one real document in full — the very example already named while describing the test structure.

The document is a short text about cybernetics, five hundred eighty-seven characters. When cut by character count, one hundred eighty per chunk, the document splits into four parts: from character zero to one hundred eighty, from one hundred eighty to three hundred sixty, from three hundred sixty to five hundred forty, and from five hundred forty to the end. The gold answer to the question "what kinds of sources can information flows come from in Gordon Pask's definition" is the words "from any sources", and in the document's text they sit at positions five hundred twenty-eight through five hundred forty-seven.

Five hundred forty is exactly the boundary between the third and fourth chunks of version one. And the word "sources" in the text sits so that its start falls into the third chunk, and its end — into the fourth: the third chunk breaks off at "…from any sour", the fourth begins with "ces…". The cut didn't fall between sentences, or even between words — it fell inside a single word form. The verdict for version one on this example: the answer is broken.

Version two, cutting by sentence boundaries, splits the same document into three parts, and the boundary between the second and third chunk sits exactly where one sentence ends and the next begins. The entire sentence containing the word "sources" sits whole inside the third chunk. The verdict for version two: the answer is kept intact.

Version three, cutting by word boundaries, happens to place its boundary exactly where the answer begins — at character five hundred twenty-eight — and the word "sources" goes entirely to the fourth chunk. Version four, cutting with overlap, shifts the start of the last chunk back to character four hundred fifty-nine — enough for the answer to fit inside one chunk. Both give the verdict "intact" here.

This illustrates version one's general problem more precisely than any percentage: cutting by character count doesn't look at the text's content at all, and the chunk boundary can land anywhere by chance, including inside a single word. Here that word is "sources", but the cut could just as easily have landed inside any other word of any other document. How typical this one document is — next frame.
