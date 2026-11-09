---
id: n67
type: answer_breakdown_table
duration_min: 2.0
assertion: "Merging the reading and the cross-check into one model saves a call; splitting them apart via classic recognition is measurably more accurate on noisy documents — each way has its own cost, and the breakdown later in the session names it"
learning_goal: "Breakdown right after the question (A1), 4-column form 'action · how it's done · advantage · drawbacks' (A5). 2026-10-29 edit (issue #299): three rows instead of four (the fourth option — the format check — was removed from the question, its breakdown is in n73); the model is named in the first two rows' actions (C5); the action descriptions were clarified (K6-6). The single call's own numbers are deliberately absent from this frame — beat n73a's exposition comes before their result (C2)."
visual:
  pattern: answer_breakdown_table
  figure: k6-shema-tri-potoka-en.png
  primary: >
    Above — a scheme (issue #303, Part B): where in the flow the
    recognition happens. The first two ways sit at ONE point — the photo
    and the text converge directly inside the model; the third sits at a
    DIFFERENT point: recognition is a separate node BEFORE the model, and
    it never sees the pixels at all. Table: action · how it's done ·
    advantage · drawbacks. Three rows, no verdict column — the decision
    comes on the next screen. The external number in the advantages column
    is set as a "before → after" card.
  backup: >
    The breakdown text is distilled from SETKA-KEYSOV-S9-part2.md, section
    "Case 6," subsection "Breakdown" (2026-10-29 edit), laid out in the
    4-column form.

    THREE ROWS INSTEAD OF FOUR. The former fourth row ("checking the
    response format's validity") carried both an external measurement and
    the rig's own number ("0 out of 15 ... 15 out of 15") — it was removed
    from the question (n66, K6-5) and from the breakdown along with it:
    this material isn't about reading the photo, it's about what to do
    with an already-finished answer, and its place is a separate beat,
    n73, where it's broken down in full, with both sides and distinguishing
    captions.

    THE SINGLE CALL'S OWN NUMBERS AREN'T HERE (C2). The first two rows name
    the risk of the "one model reads and cross-checks itself" device
    qualitatively, with no count of "27 out of 30" and no word "echo" —
    these numbers are revealed by beats n73a–n73e, which stage their own
    three-part exposition of the measurement (test structure → summary →
    breakdown by group) BEFORE this same result. An edit naming the result
    here would rob that exposition of what it's the first to reveal.

    The model is named in the first two rows' action (C5): `qwen/qwen3-vl-
    8b-instruct` — the same model as in the baseline (n69) and in the
    single call (n73a). The third row doesn't name a model — it describes
    the architecture of the broader market (an external study), not a node
    on our rig.

    The number in the third row's advantages, and its source, are
    external, CHISLA-SVERENO.md, line 61 (OCBC, arXiv:2604.26462, status
    VERIFIED): Direct VLM 55.38% versus the best pairing, PaddleOCR+MiniCPM
    87.27% (+31.9 percentage points) on 120 documents. Nothing was taken
    from `research/*` (BRIEF §2 forbids it).
---

# What each of the three ways does

## Assertion

None of the three ways is foolish on its own. The difference is in exactly where each one loses reliability — and whether anything inside the process notices.

## Visual

| Action | How it's done | Advantage | Drawbacks |
|---|---|---|---|
| **Single call, uncompressed photo** | the model `qwen/qwen3-vl-8b-instruct` gets the whole photo and the request's text in one request; it names the read amount and date itself and decides itself whether they match what was written | one call for the whole step — there's no separate comparison operation outside it | the same model that reads the photo also hands down the "matched" verdict: reading and comparing have one and the same performer, and there's nothing inside this one call to check the decision with a third party — how robust this device is gets broken down later in the session |
| **Single call, compressed photo** | the same device, but the photo is shrunk before sending | lower cost of transferring the file at small resolutions | the same single-performer risk as the uncompressed version |
| **Classic recognition, then a text prompt** | the text is recognized classically first; the model gets only the finished recognized text, with none of the photo's original pixels | on an independent check of documents, this pairing is measurably more accurate than feeding the image straight to the same model: field accuracy **87.27% versus 55.38%, a 31.9-percentage-point gap**, on 120 documents (OCBC) | on a clean, single-page document, this advantage disappears — parity on quality; there is no recognition node on our rig in either of the measured devices |

## Speaker notes

Let's go through the three ways one by one. None of them is foolish: each has a task on which it would be a sensible choice. The question is exactly where each one loses reliability, and whether anything inside the process itself notices.

The first two ways are built the same: the model `qwen/qwen3-vl-8b-instruct` gets both the photo and the request's text at once, in one request, and decides for itself whether what was read matches what was written. The only difference between them is whether the photo is compressed or not. The advantage is obvious: one call for the whole step, with no separate comparison operation outside it. But this advantage has a flip side. Reading the photo and comparing the result with the text are done by one and the same performer. If something fails somewhere along this chain for it — in reading, in comparing, anywhere — there's nothing left inside that same call to check the decision with. How dangerous that really is gets its own breakdown later in the session, with the rig's own numbers.

The third way is built differently: classic recognition first turns the photo into text, and from there on the model only gets this text, with none of the original shot's pixels. On an independent check of real documents, this pairing reads fields noticeably more accurately than feeding the image straight to the same model: accuracy drops from eighty-seven percent for the pairing to fifty-five for the direct feed — almost thirty-two percentage points of difference on the same body of documents. But this advantage is measured on noisy, multi-page documents. On a single-page, relatively clean document — and our receipt is exactly that — the pairing and the direct feed land at the same level of quality: parity, with neither side clearly ahead. And there's no recognition node on our own rig in any of the measured devices — this option is hypothetical, with no node built for it.

Weigh it before choosing: the photo we're working with is shot on an ordinary phone, with no scanner, and that condition is the same for all three ways. Which of them will hold up against a crumpled sheet and uneven light without a quiet failure inside itself — the breakdown on the next screens, with the real rig and real numbers.
