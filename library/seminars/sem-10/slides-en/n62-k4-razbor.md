---
id: n62
type: answer_breakdown_table
duration_min: 1.0
assertion: "One of the three options works correctly, one doesn't work on this rig at all, one solves only a narrow subclass of the task"
learning_goal: "Breakdown of the three options, 4-column form (A5). The second option's failure is named briefly here; the breakdown of the failure is a separate beat (n63-n66), not dissolved into this table."
visual:
  pattern: answer_breakdown_table
  primary: >
    Table: action · how it works · advantage · drawbacks. Three rows.
  backup: >
    Text — SETKA-KEYSOV.md Case 4, "Breakdown of options," 30 CORD scans.
    The third option's row is reworded by this edit (issue #311, owner's
    note "slide 57/58 — need to reword the third option and explain it
    more broadly"): the name and the "How it works"/"Drawbacks" columns
    are expanded with the physics of the method (what gets hashed, Hamming
    distance between bit fingerprints, why this is about "the same file
    again," not about "a document similar in meaning") — the facts and
    numbers weren't changed.
---

# What each of the three actions does

## Assertion

A caption loses everything that didn't make it into the text; comparing pictures directly doesn't work on this rig; an image fingerprint without a model solves only part of the task.

## Visual

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| Caption and search as text | The receipt's text turns into the same text embedding as in Cases 1-3 | Works correctly: embeddings differ meaningfully between receipts, reuses the entire mechanism of Cases 1-3 | A caption is a word retelling of the picture: field layout, the visual look of the form, the stamp, a handwritten note are lost before they ever reach search |
| Search picture by picture (multimodal embedding) | The model turns the picture itself into a numeric representation, with no text in between | In theory loses nothing of what a caption discards | **Doesn't work on this rig at the scan's real resolution — breakdown next beat** |
| Image fingerprint (perceptual hash) | The picture is compressed into a short bit string without calling a model; closeness is matching bits between fingerprints (Hamming distance) | Reliably catches near-duplicates under recompression — without calling a model, fast and local | The fingerprint stores only outward appearance: different documents occasionally give a close fingerprint by chance, meaning-level duplicates with a different layout — different. Good for "the same file again"; doesn't solve "a similar document" |

## Speaker notes

Thirty scans from CORD — an open dataset of real receipts with reference-labeled text for every field — run through all three actions.

Caption and search as text works correctly and without caveats: the receipt's reference or recognized text turns into the same text embedding we've used all session today, and that embedding meaningfully tells different receipts apart. The price for this is that a caption is a word retelling of the picture — the picture itself isn't passed along: everything that didn't make it into the text — field layout, the visual look of the form, the stamp, a handwritten note — is lost before it ever reaches the search step.

Searching picture by picture directly, through a multimodal embedding, in theory loses nothing of what a caption discards. But this exact option deserves a separate, more careful look: it doesn't work at all. Calling it weak work would be wrong — this is a flat zero, and how that was discovered is itself an important lesson. The next beats are exactly about that.

Comparing by image fingerprint works cleanly and predictably, but solves only a narrow sub-task. Here the picture is shrunk down to a tiny size and turned into a short bit string — a fingerprint of its general look, computed locally, without a single call to a model; the similarity of two pictures is the number of matching bits between their fingerprints, Hamming distance. The fingerprint doesn't know what's written on the picture — only what it looks like overall: the same scan, slightly recompressed or shifted a bit, gives a close fingerprint, while two differently made scans of the same document by meaning — different fingerprints, even if the text on them matches word for word. This doesn't solve the "document similar by meaning" task in general. This is its own, honestly named boundary; calling it a drawback of the method would be wrong — we'll come back to it in the nuances.

This table is built a little differently than in the previous three cases of this session: there, three actions competed for the same task, and the choice came down to which one solves it better. Here the first and third actions solve different tasks and don't have to compete at all — rather, they complement each other. This will become clearer at the solution beat, but for now keep in mind: the question "who won" isn't necessarily the main one here.
