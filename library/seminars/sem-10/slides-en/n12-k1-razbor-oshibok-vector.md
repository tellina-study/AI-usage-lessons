---
id: n12
type: measured_outcome_table
duration_min: 0.75
assertion: "For vector, at 500 documents, a neighboring paragraph of the same article turns out closer in meaning than the gold one — a labeling edge case, not a miss by the method"
learning_goal: "Beat S2/S3/S4 (breakdown by group, n11's successor): an explicit verdict on the example (S3), a systematic error on its own tile (S4), a conclusion (S10). Part 2 of 2 (continuing n11 — the keyword error). Letter suffix brought to the deck's attention (tools/seminar-production/README.md §1, issue #311)."
visual:
  pattern: measured_outcome_table
  primary: >
    An example table: at 500 documents, vector finds a paragraph that is
    substantively relevant but formally incorrect, from the same article.
    Verdict INCORRECT, with a conclusion below the table about the nature
    of SberQuAD's "distractors" at this scale.
  backup: >
    The example is verbatim from `stend/raw/case1-results.json` (the
    `details` field) and `corpus/corpus_case1.json` (document texts), with
    no change to the model's answers.

    Error 2 (q3 — vector, only at 500 documents): the gold document is
    needle-3, about a marathon; at 500 documents vector finds
    `distractor-237` instead — judging by the shared footnote [17] in both
    texts, likely a neighboring paragraph of the SAME Wikipedia article
    about the marathon, which contains the literal numeric answer ("times
    get worse... above 14-16°C"), unlike needle-3, where the fact is
    phrased in general terms ("high temperatures... keep the best results
    out of reach"). The model answered confidently and sensibly in
    substance, but against the gold labeling — incorrectly. On this same
    question, keyword found the CORRECT document (needle-3), but the model
    still answered "no information" — because the literal number wasn't
    in the text it found; it sat in the neighboring paragraph, which in
    this run went to distractor-237.

    METHODOLOGICAL CONCLUSION (say it out loud, don't hide it): at a scale
    of 500 documents, part of SberQuAD's "distractors" are actually
    neighboring paragraphs of the same article as the needle document.
    Formally having a single `gold_doc_id` doesn't mean the rest of the
    corpus is irrelevant to the topic — recall@1 against one gold answer
    here understates the fact that the search found a substantively
    relevant text, just not that specific paragraph where the number lives.
---

# Vector's systematic error: confuses neighboring paragraphs

## Assertion

Vector confuses neighboring paragraphs of the same article — and this shows up only on a large base.

## Visual

**Error 2 — vector, a neighboring paragraph of the same article (only at 500 documents)**

| Question | Found document | Model's answer | Verdict |
|---|---|---|---|
| q3: "What summer temperature keeps marathon runners from showing their best results?" → gold answer "high," document needle-3 | `distractor-237` instead of needle-3 — likely a neighboring paragraph of the same article (shared footnote [17]) with a literal number | "Temperatures above 14-16°C make marathon runners' results worse." | **INCORRECT** (substantively sensible, against the gold answer) |

> Here keyword found the CORRECT needle-3 — but the model still answered "no information": there was no number in it; the number sat in the paragraph that went to the vector option instead.

## Speaker notes

The second systematic error belongs to vector, and it shows up only at five hundred documents, unlike keyword's error, which holds at any base size. Take the question about the high temperature that keeps marathon runners from showing their best results: at 10, 50, and 200 documents vector finds needle-3 without trouble, and at five hundred it returns `distractor-237` instead.

The miss isn't random: both texts share the same footnote number, [17] — most likely this is a neighboring paragraph of the same Wikipedia article about the marathon. It contains a literal number — "times get worse... above 14-16°C" — while needle-3 phrases the same fact in general terms, with no number. The model answered confidently and sensibly in substance: temperatures above 14-16°C make marathon results worse. By SberQuAD's gold labeling, that's still incorrect: the gold document is a different one. A detail on this same question: keyword found the correct document, needle-3 — and the model still answered "no information," because there was no literal number in it.

The conclusion, plainly: at a scale of five hundred documents, part of what we call SberQuAD's "distractors" are neighboring fragments of the same article as the needle document. Formally, a question has one gold `gold_doc_id`, and that still doesn't make the rest of the corpus on that topic irrelevant. recall@1 against a single gold answer understates the search here: vector found a substantively relevant piece of text, just not the paragraph where the number happens to sit.

For Olga's training center, this error is more dangerous than the first precisely because it's rarer and less noticeable: nine times out of ten vector finds the right chunk, and only on a large, grown base does it occasionally swap in a neighboring paragraph of the same article — the requester gets an answer that sounds confident and on-point, but is formally not the one encoded in the gold answer.

What's worth taking away from this breakdown is the difference between the two errors: for keyword it's a structural weakness of the method for the Russian language at any base size; for vector it's a labeling edge case that only opens up on a large base.
