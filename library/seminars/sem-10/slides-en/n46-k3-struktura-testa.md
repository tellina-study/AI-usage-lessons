---
id: n46
type: content
duration_min: 0.75
assertion: "Fifty questions, a pool of five hundred documents, three groups, selected by code — not by eye"
learning_goal: "Case 3's measurement-exposition beat (canon forma-keysa-s-zamerom.md §1, C2): test structure BEFORE the result — the corpus, the confusable clusters, the first two question groups with an example and an expectation each. Inserted as a letter-suffix between n41 (question) and n48 (summary) — see tools/seminar-production/README.md §1. Part 1 of 2 (n47 — the third group and the search-by-meaning model): split because 15pt half-size type leaves no room for three table rows plus the model tile on one frame (issue #311)."
visual:
  pattern: content
  primary: >
    A corpus tile (500 documents, 8 confusable clusters) · a table of two
    question groups (16/16) with an example, expected answer, and the
    reason for the group. No results on the frame.
  backup: >
    Numbers — SETKA-KEYSOV.md Case 3 + stend/corpus/case3_questions.json
    (classification by code — stend/measure/build_corpus_v2.py: lexical_gap
    = overlap_ratio ≤0.3; exact_match = a shared number/term where
    overlap >0.3; otherwise neutral). Group examples — c3q22 (lexical gap),
    c3q4 (exact match), c3q42 (neutral, the same question as in the
    nuances breakdown n57 further on). Qid appears only in this production
    note, NOT on the visible slide (canon §3 proektirovanie-keysa-i-
    voprosa.md + the S9 n48 precedent: "run numbers don't belong on the
    visible layer").

    The slide was inserted as a letter-suffix (n46) between n41 and n48,
    outside the running numbering at the time of insertion; `renumber_
    slides.py` dropped the suffix at the subsequent full deck-wide
    renumbering for the session (tools/seminar-production/README.md §1) —
    the number is already part of the running numbering.
---

# Test structure: five hundred documents, fifty questions, three groups

## Assertion

Fifty questions, a pool of five hundred documents, three groups, selected by code — not by eye.

## Visual

> **Corpus.** 500 SberQuAD documents, including 8 confusable clusters — groups of documents that split one and the same rare entity. Example: the "Zvyozdny" cluster — one document about spacecraft, another about concert programs from the mid-1980s; both use the word "zvyozdny" ("starry"), but answer completely different questions.

| Group | How many | Example question | Expected answer | Why this group |
|---|---|---|---|---|
| Lexical gap | 16 | "When did the battle take place?" | April 16, 1746 | The question and the document share almost no words — the expected zone of semantic search |
| Exact match | 16 | "Who took the title of Duke of Milan in 1395?" | Gian Galeazzo Visconti | The year and the title from the question sit literally in the text — the expected zone of keyword search |

## Speaker notes

Before looking at the numbers, it's worth understanding exactly what was measured and on what material — otherwise the figures of the next beat will float in the air without a base.

The corpus is the same five hundred SberQuAD documents that already took part in the first case of this session, except here eight confusable clusters have been specially added: groups of documents that split one and the same rare named entity. For example, a group of documents around the word "zvyozdny" ("starry") — one document talks about spacecraft from science fiction, another about the concert programs of a Soviet artist from the mid-eighties. Both use the same word, both are formally "about something starry," but they answer completely different questions. Such groups deliberately confuse both exact word matching and semantic closeness — they are exactly what makes the corpus tough: there's nothing toy-like about it.

Fifty questions are selected by code, into three classes — hands and eyes took no part here. Sixteen lexical-gap questions — the question shares almost no words with the text where the answer lies: "When did the battle take place?" and a document where the answer sits next to completely different words — Culloden, George II, the Duke of Cumberland. Even the cognate word "srazhenii" ("battle," inflected) in the text isn't counted by the classifier as a match for "srazhenie" ("battle") in the question — that strictly is the gap counted. This group is a guaranteed zone where semantic search should win, if it's capable of anything beyond matching letters at all. Sixteen exact-match questions — a number or name from the question sits literally in the text: "Who took the title of Duke of Milan in 1395?" directly repeats both the year and the title. This group is the zone of classic keyword search.

The third group, neutral, comes next.
