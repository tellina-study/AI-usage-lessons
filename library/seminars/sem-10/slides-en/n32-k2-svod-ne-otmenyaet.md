---
id: n32
type: measured_outcome_table
duration_min: 0.5
assertion: "Version 1's systematic error is that it doesn't look at the text at all — and one lucky document still doesn't overturn the summary across the whole sample"
learning_goal: "The systematic error named in its own tile (C4), an explicit conclusion from the single-document breakdown, returning to the summary (C10) — canon forma-keysa-s-zamerom.md §1. Part 2 of 2 (continuing n31 — the breakdown on the cybernetics document). Letter-suffix pending deck finalization (tools/seminar-production/README.md §1, issue #311). Restructured 2026-11-04 per the owner's note ('a wall of text, unreadable'): run-together paragraphs split into separate paragraphs within the same tiles, the number of tiles unchanged."
visual:
  pattern: measured_outcome_table
  primary: >
    Tile on version 1's systematic error, a warning tile about a single
    document, a conclusion tile that returns to the summary across sixty
    documents.
  backup: >
    IMPORTANT: v3 and v4 are intact specifically on the cybernetics
    document (n31) — the summary across the whole sample (n28) still
    shows them worse than version 2 (8.3% and 5.6% broken answers against
    1.4%); don't carry the single-document conclusion over to the general
    case.
---

# Version 1's systematic error — and the lesson of one document

## Assertion

Cutting by character count doesn't look at the text at all — and one lucky document still doesn't overturn the summary across the whole sample.

## Visual

> **Version 1's systematic error.** Cutting by character count doesn't look at the text at all — the chunk boundary can fall anywhere, including inside a single word.
> Here, character 540 of the document happened to land exactly in the middle of the word "sources".

> **One document illustrates the mechanism; the conclusion for the whole sample comes from the summary.** On this document, versions 3 and 4 keep the answer intact.
> But the summary across sixty documents (previous beat) still shows them, on average, noticeably worse than version 2 — 8.3% and 5.6% broken answers against 1.4%.

> **Conclusion.** This isn't a one-off failure on a single document — the summary across sixty documents and seventy-two questions shows the same effect on average.
> Version 1 systematically tears answers in half; version 2 almost never does.

## Speaker notes

The verdict for version one on the previous document — the answer is broken — illustrates version one's general problem more precisely than any percentage: cutting by character count doesn't look at the text's content at all, and the chunk boundary can land anywhere by chance, including inside a single word. Here that word is "sources", but the cut could just as easily have landed inside any other word of any other document; the fact that this is a specific, easily checkable case doesn't make it an exception from the overall picture.

Version three, cutting by word boundaries, happens in this document to place its boundary exactly where the answer begins, and the word "sources" goes entirely to the fourth chunk. Version four, cutting with overlap, shifts the start of the last chunk back — enough for the answer to fit inside one chunk. Both give the verdict "intact" here — but this is one document: the summary across sixty shows version three at eight and three tenths percent broken answers, version four at five and six tenths, noticeably more often than version two (one and four tenths percent). One lucky document doesn't overturn the average across the sample.

The conclusion is simple: this isn't the rarity of a single document and not an unlucky coincidence — the summary across sixty documents and seventy-two questions, which we already saw in the previous beat, showed the same effect on average, several times more often for version one than for version two. One document just makes an abstract percentage tangible: behind the figure 12.5% stands one specific word, cut in half — that's more vivid than detached statistics, which are easy to let slip past your attention.

Next — the case's solution architecture and how it's assembled on the real rig.
