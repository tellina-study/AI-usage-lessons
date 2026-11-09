---
id: n75
type: criteria_checklist_and_boundary
duration_min: 0.75
assertion: "On semantic similarity, the working model has a real signal — almost 8 times above random guessing — but it's noticeably weaker than text search by caption"
learning_goal: "The second, honest role of version 2 (n59/n61): not a repeat/rotation of the same scan (n74), but 'does this scan look similar by meaning to another, different document.' The result — neither a repeat of titan's failure, nor a replacement of n71's architecture (caption+text for meaning, phash for literal repeat): a measurable but limited signal, clearly weaker than the text reference. Part 2 of 2 (continuing n74: finding the model and the rotation boundary). Letter-suffix pending deck reconciliation (tools/seminar-production/README.md §1, issue #311)."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A table "method · agreement with the text reference · chance level ·
    correlation with text," an honest-conclusion tile (there is a signal,
    but it doesn't replace n71's architecture).
  backup: >
    Numbers — stend/raw/case4_mm_full_retrieval.json::part_C_semantic_
    similarity_agreement. The gold labeling "semantically nearest receipt"
    — from the already-checked working method, text embedding of the OCR
    (part B, recall@1 0.967 — its own, separate task: finds the right menu
    item from a short description, not the same question as part C).
    chance-level — 1/29 (one of 29 remaining scans under random choice).
---

# There is a signal on semantic similarity, but it's limited

## Assertion

The multimodal model agrees with the text reference almost 8 times more often than random guessing — and still noticeably less often than text search itself.

## Visual

| Method | agreement with the text reference, recall@1 | chance level | correlation with text |
|---|---|---|---|
| Working model (nemotron-3.5-embed-1b) | **26.7% (8/30)** | 3.45% (1/29) | 0.529 |
| Perceptual hash | 3.3% (1/30) | 3.45% (1/29) | −0.071 |

> **Honest conclusion.** The working model carries a measurable signal about the picture's meaning — recall@1 almost eight times above chance level, and a noticeable positive correlation with text similarity (0.529 against −0.077 for the broken titan). Text search by caption itself, which serves as the reference here, finds the semantically similar receipt in 96.7% of cases — direct comparison of pictures doesn't reach that bar. Perceptual hash is insensitive to meaning altogether: its result is at chance level, 0.033 against 0.0345 — exactly what n66/n71's boundary predicted.

## Speaker notes

Direct comparison of pictures has a second role — different from the previous beat. There, the model caught a literal repeat of the same document under rotation. Here the question is different: does this scan look similar by meaning to some other, different document out of the same thirty — the same question the second action card named back on n61.

The gold labeling for this check was taken from the already-checked working method — the text embedding of the receipt's recognized text, which finds the right menu item from a short description in ninety-six point seven percent of cases. For each of the thirty original scans, with not a single augmentation, we looked for which of the remaining twenty-nine receipts the working multimodal model and perceptual hash would call the nearest, and compared that choice to what the text method named as the gold neighbor.

The result is neither a failure nor a full win — an honest something in between. The working multimodal model agrees with the text choice in eight cases out of thirty — twenty-six point seven percent. Pure chance across twenty-nine possible neighbors would give three point four five percent — the model beats it almost eightfold, and the correlation between its similarity measure and the text similarity measure is positive and noticeable, zero point five two nine. That correlation can't be called statistical noise — the broken titan had a correlation of minus zero point zero seven seven on the same measure, which is effectively zero.

But a real signal isn't the same as the best method. Text search by caption itself finds the correct semantic neighbor in ninety-six point seven percent of cases — direct comparison of pictures doesn't clear that bar. For the task "find a document similar by meaning," caption and text search remain the working solution; direct comparison of pictures gives a partial result here, measurably distinguishable from chance but not an equivalent replacement. Perceptual hash, exactly as this case's architecture predicted, is insensitive to the content's meaning at all — its agreement with the text choice sits at the level of pure chance, three point three against three point four five percent.

The upshot of both beats of this repeat pass: the failure of the section before n73 turned out to be a property of one specific model; the approach "multimodal embedding through OpenRouter" as a whole held up. A working alternative was found, and it gives a measurable, imperfect benefit on both roles of version 2 — more reliable than the fingerprint on literal repeats under rotation, and noticeably better than chance, but weaker than the caption, on semantic similarity. This doesn't overturn n71's architecture — caption and text search for meaning, fingerprint for literal repeat: it now has a number across the full sample too, and both methods hold it up. A third option with measurable but limited strengths is material for a decision that stays beyond this session.

The session ends with the last divider and the shared interlude — next.
