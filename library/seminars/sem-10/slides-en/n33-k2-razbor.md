---
id: n33
type: answer_breakdown_table
duration_min: 1.0
assertion: "Version 2 costs a bit more implementation complexity — and pays for it with a share of broken answers that drops several times over"
learning_goal: "Breakdown after the measurement (the story of one iteration — design canon §4): v1 tried → problem found by the numbers → v2 as the fix; v3/v4 — two additional options, measured by the same run. 4-column form (rule A5), four rows."
visual:
  pattern: answer_breakdown_table
  primary: >
    Table: action · how it works · advantage · drawbacks. Four rows.
  backup: >
    Text — SETKA-KEYSOV.md Case 2, "Breakdown of the options", fit into
    the 4-column form. v3/v4 numbers — follow-up run 2026-11-02 (local
    Python measurement, `stend/raw/case2-results.json`, not a live n8n
    call).
---

# What the measurement confirmed for each of the four actions

## Assertion

Version 1's simplicity costs a few percent of broken answers at every chunk size; versions 3 and 4 reduce that price without closing it to version 2's level.

## Visual

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| Cut by character count | The document is chopped into pieces of a set length with no regard for the text inside | Simplest to implement — one parameter, one pass | Breaks the answer to a question in 2.8–12.5% of cases depending on size; there's no way to tell in advance which size is "more convenient" without checking |
| Cut by sentence boundaries | The cut falls only where a sentence ends | The share of broken answers drops several times over — almost always 0–1.4% across all tested sizes | A bit more involved to implement (needs text parsing into sentences — character counting alone isn't enough); depends on the quality of sentence splitting for the specific language and text |
| Cut by word boundaries | The document is split into words, a chunk accumulates to the target size, the cut only falls at a word boundary | A cheap alternative to version 1: keeps the word whole and is simpler to implement than parsing sentences | Breaks the answer in 0–9.7% of cases: holds the word boundary, but knows nothing about sentence boundaries |
| Cut by character count with overlap | The same logic as version 1, but neighboring chunks overlap by part of the chunk's length | Breaks the answer less often than version 1 — 0–5.6% against 2.8–12.5% | The store grows from character duplication; doesn't close the gap to version 2's level |

## Speaker notes

We've already broken down how each action works — here's what it came to by the numbers. Four actions, and the difference between them isn't about whether they work at all — it's about how many answers to future questions they damage along the way.

Cutting by character count is the simplest to implement: one parameter setting the chunk's length, one mechanical pass through the text. This decision pays for itself by having part of the answers to future questions end up torn between two neighboring chunks — from 2.8 to 12.5 percent depending on the chosen size, and, as we just saw, with no clear link between size and quality.

Cutting by sentence boundaries is a bit more involved: it needs a separate step that understands where a sentence ends in the given language — a dependency version 1 doesn't carry at all. But the price for this complexity pays back many times over: the share of broken answers drops several times across all five tested chunk sizes, staying within 0–1.4%.

Cutting by word boundaries — the same run measured it too: a cheap alternative to version 1 that doesn't tear a word in half, but knows nothing about sentence boundaries. The share of broken answers is zero to nine and seven tenths percent: better than version 1, but at none of the five sizes better than version 2.

Cutting by character count with overlap — the same simple logic as version 1, with added overlap between neighboring chunks. The share of broken answers drops to 0–5.6% — almost half that of version 1 without overlap — but the gap to version 2's level still doesn't close: overlap also increases the store's volume, because part of the text is stored twice.

The architectural decision that follows from this, and the screen where it's configured in n8n — next beats.

This is exactly the form the rule of sequential iteration requires: we first tried the simplest solution, saw by the numbers that it damages part of the answers, and only then proposed an alternative as a response to the problem found; nobody compared two options invented upfront on equal footing here. Versions 3 and 4 are two additional options, checked by the same run in parallel with version 1 and version 2: both are cheaper to implement, both beat version 1 by the numbers, and neither replaces version 2 as the solution.

The "drawbacks" column for version 2 carries real weight — the table isn't here for symmetry. Splitting text into sentences in Russian isn't an absolutely reliable task: abbreviations, initials, direct speech with lines inside one paragraph sometimes throw off simple sentence-boundary detection algorithms. This doesn't overturn the measurement's overall conclusion, but it does mean that "cut by sentences" is a solution whose quality is worth periodically rechecking on your own real documents.
