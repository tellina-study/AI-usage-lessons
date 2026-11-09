---
id: n11
type: measured_outcome_table
duration_min: 0.75
assertion: "For keyword, Russian case endings throw off the word match at any base size — the cause isn't the base's scale, it's the method"
learning_goal: "Beat S2/S3/S4 (breakdown by group, n10's successor): an explicit verdict on every example (S3), a systematic error on its own tile (S4). The group here isn't a type of action but a type of ERROR, found in the measurement data itself after the questions were rebuilt on 2026-11-02 (issue #311). Part 1 of 2 (n12 is the vector error): split so each error gets its own frame (issue #311, the 15pt type floor leaves no room for two tables on one slide)."
visual:
  pattern: measured_outcome_table
  primary: >
    A table of examples: keyword misses the document because of case
    endings, repeating at any base size. Every row carries an INCORRECT
    verdict; the conclusion sits under the table.
  backup: >
    The example is verbatim from `stend/raw/case1-results.json` (the
    `details` field) and `corpus/corpus_case1.json` (document texts), with
    no change to the model's answers.

    Error 1 (q4, q10 — keyword): `retrieved_doc_id` does NOT match
    `gold_doc_id` at ALL FOUR base sizes identically, including size 10,
    where there are no distractors at all — so the cause isn't the base's
    scale, it's the comparison method itself. q4: the question "by
    paleontologists... Eldredge and... Gould" (instrumental case in
    Russian) against a document reading "paleontologists Eldredge and
    Gould" (nominative case); the overlap with the correct document,
    needle-4, is just one word ("year"); keyword found needle-2 (about
    Mozart, off-topic) — also one shared word ("year"), a coincidental
    match on an everyday word; with a tied score, keyword picked the wrong
    document. q10: the question "the model of the universe... taken as a
    basis" against document needle-10, "the Keplerian model of the
    universe is based on Copernicus's model" — the overlap with the
    correct document is one word ("universe"); keyword found needle-3
    (about a marathon) — there TWO words matched, "model" (from the phrase
    "the whole training model") and "universe" (from the phrase "world
    championships"), and the 2-to-1 margin pulled the choice away from the
    correct document.
---

# Keyword's systematic error: mixes up case endings

## Assertion

Keyword confuses Russian case endings — and that doesn't depend on base size.

## Visual

**Error 1 — keyword, case endings (identical at every base size)**

| Question | Overlap with the correct document | Overlap with the found (wrong) document | Verdict |
|---|---|---|---|
| q4: "...by paleontologists Niles Eldredge and Stephen Jay Gould..." → gold answer "1972" | needle-4: "...in 1972 paleontologists Eldredge and Gould..." — 1 word ("year") | needle-2 (about Mozart): 1 word ("year") — a tie, the wrong one was picked | **INCORRECT** |
| q10: "...whose model of the universe was taken as a basis by Kepler?" → gold answer "Copernicus" | needle-10: "...the Keplerian model of the universe is based on Copernicus's model..." — 1 word ("universe") | needle-3 (about a marathon): 2 words ("model," "universe") — the margin went against the correct one | **INCORRECT** |

> Keyword doesn't count case-form matches as a match — the error holds even at 10 documents with no distractors: the cause isn't the base's scale, it's the method.

## Speaker notes

The previous frame showed the summary numbers: keyword holds recall@1 = 0.8 at all four base sizes, vector holds 1.0 at three sizes and 0.9 at five hundred. Here's what's behind those numbers on concrete questions and documents. The first cause belongs to keyword, and it doesn't depend on base size at all.

The same error already repeats at ten documents, where there are no distractors whatsoever, and it holds at five hundred. Take the question about the debate revived by paleontologists Eldredge and Gould: in the question the names are in the instrumental case in Russian — "by paleontologists... Eldredge and... Gould" — while the document holding the answer, needle-4, has them in the nominative — "paleontologists Eldredge and Gould." Keyword compares words literally, with no normalization to a base form, and a different case ending is simply a different word to it. The overlap between the question and the correct document stays at one word: "year." And the document keyword actually picked, needle-2, about Mozart, isn't on topic at all — it overlaps with the question by that same single word, "year." The score ties, and on a tie the choice goes astray.

On the question about Kepler's model of the universe, it's worse: the overlap with the correct document, needle-10, is one word, "universe," while the overlap with the marathon document, needle-3, which keyword actually picked, is two words — "model" and "universe" — which happen to sit in a passage about preparing for a world championship. Here the margin clearly favors the wrong document. This is a weakness of the method itself for a language with a rich case system, and it holds at any base size — which is exactly why keyword's 0.8 doesn't change at any of the four sizes.

For Olga's training center this means something concrete: a requester who writes a question with names in a different grammatical case than the source document risks getting the wrong document simply because the method compares letters — it doesn't catch a word form's meaning. This can be fixed by normalization (reducing every word to its base form), but that's a separate step that doesn't by itself guarantee anything — it merely shifts the same problem onto harder cases of grammatical agreement. Next — the second systematic error, belonging to vector, and it's built in a completely different way.
