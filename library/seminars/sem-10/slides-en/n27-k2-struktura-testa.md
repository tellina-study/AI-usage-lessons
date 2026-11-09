---
id: n27
type: measured_outcome_table
duration_min: 1.0
assertion: "60 documents, 72 questions, five chunk sizes — and not a single model at this step"
learning_goal: "Beat 1 of the measurement exposition for Case 2 (canon forma-keysa-s-zamerom.md §1, rule C2): test structure BEFORE the result — corpus, a finding about data quality, five size groups, a concrete example with its gold answer. No results on the frame. The model is explicitly NOT named (C5 by contraposition) — it has no part in this step, the cutting is entirely classical code. Restructured 2026-11-04 per the owner's note ('a wall of text, unreadable'): run-together multi-line paragraphs split into separate paragraphs within the same tiles, the number of tiles unchanged (issue #311)."
visual:
  pattern: measured_outcome_table
  primary: >
    Corpus tile, finding-about-labeling tile, five-size-groups tile, a
    concrete document/question/answer example in prose, "no model here"
    tile. No result anywhere on the frame.
  backup: >
    The corpus and the finding about offsets — stend/measure/case2_chunking.py,
    exact calculation (22.0% = 1108/5036). The example — execution 2369
    (stend/raw/case2_chunking_execution.json), a real run of the demo
    scenario on the rig, the same document that's in the measurement's
    sample[:60] (seed=7). The five size groups and their order match
    exactly the ones on n28 (summary) and in the nuances on n38 — canon
    requires names and order to match across beats.
---

# Test structure: what was checked, and on what

## Assertion

The same corpus was run through five chunk sizes for all four cutting versions — without a single model at this step.

## Visual

> **Corpus.** SberQuAD, 60 documents (no shorter than 500 characters — otherwise there's nothing to cut), 72 questions with answer labels verified directly against the text.
> **Finding along the way.** In 22.0% of rows in the source dataset (1,108 of 5,036), the answer's position didn't match the document's text — such rows were excluded from the measurement entirely, with no adjustment for a convenient result.

> **Five groups — the same chunk size for all four versions:** 120 · 180 · 220 · 300 · 450 characters.
> 180 is this session's headline value.

> **Example.** A real run of the demo rig: a document about cybernetics, 587 characters.
> Question: "What kinds of sources can information flows come from in Gordon Pask's definition?" The gold answer is "from any sources", positions 528–547: a literal substring of the document at that spot, not invented by anyone.

> **There is no model at this step.** None of the four cutting versions calls an LLM or an embedding — all four "Chunking" nodes (next beat) are plain code.
> The model appears later, at the step of embedding an already-made chunk (Case 1), which this measurement does not touch. There are no results on this frame — what came out of this is next.

## Speaker notes

Before looking at the result, it's important to understand how the measurement itself is built — exactly what was run, and through what.

The corpus is sixty documents from the SberQuAD set, a standard Russian-language question-and-answer set, and seventy-two questions against these documents. The documents were selected to be no shorter than five hundred characters: shorter ones simply have nothing to cut into chunks, and splitting them makes no meaningful difference.

Along the way, a separate finding turned up about the quality of the source data. In twenty-two percent of rows in the source dataset — one thousand one hundred eight rows out of five thousand thirty-six — the field holding the answer's position didn't match where the text actually sat in the document: the labeling had shifted, already at the dataset-preparation stage. Such rows were excluded from the measurement entirely — no one adjusted for a convenient result here: if you can't trust the position label, you also can't honestly tell whether a chunk cut tore through it.

The measurement's five groups are five chunk sizes: one hundred twenty, one hundred eighty, two hundred twenty, three hundred, and four hundred fifty characters. One hundred eighty is the headline value, the one the main breakdown is built around; the other four exist to check that the result isn't a fluke tied to one particular number. Within each group, all four cutting versions are run — by character count, by sentence boundaries, by word boundaries, and by character count with overlap — on the same set of sixty documents and seventy-two questions.

Let's take a concrete example — a real run from the rig, not invented. A document about cybernetics, five hundred eighty-seven characters. Question: what kinds of sources can information flows come from in Gordon Pask's definition? The gold answer — "from any sources" — is a literal substring of the document, at positions five hundred twenty-eight through five hundred forty-seven; it wasn't guessed, it's right there in the text itself.

And one last thing that matters for how the test is built: there isn't a single model at this step. All four cutting versions are plain code, with no call to an LLM and no embedding; what that looks like on a real screen — two beats from now. The model appears later, once a finished chunk goes on to be embedded — and that's a different, separate step that today's measurement doesn't touch. There are deliberately no results on this frame: first the test's structure, then its outcome.
