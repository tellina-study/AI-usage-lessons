---
id: n64
type: content
duration_min: 1.0
assertion: "The same call at the same resolution must give different vectors for two different receipts — otherwise the check proved nothing"
learning_goal: "S2 beat 1 for Case 4's finding (forma-keysa-s-zamerom.md §1): the structure of the check BEFORE the result — what's being compared (three resolutions of the same pair of receipts), which model and with what settings. There's no result on this frame — it's on n66. Part 1 of 2 (n65 — the expectation): split, because the 15pt floor font size leaves no room for the call tile, the table, and the expectation tile on one frame (issue #311)."
visual:
  pattern: content
  primary: >
    A fact tile: the model and the call (S5) — `amazon/titan-embed-image-v1`,
    POST `/v1/embeddings`, input — a data URL (base64 JPEG). A table of
    three resolutions of the same pair of CORD receipts, with not a single
    result in it.
  backup: >
    The setting numbers — stend/measure/case4_measure.py::to_data_url (w,h,q
    default 64×96×80) and debug_mm.py…debug_mm6.py (a sweep of
    resolutions, live calls). stend/README.md, "Open technical risk,
    ARCHITECTURE.md §5/§7 point 1" — the table "Picture resolution →
    base64, characters," the exact figures for the ranges. The beat's form
    — canon forma-keysa-s-zamerom.md §1, beat 1 of 3: corpus/groups/
    model/expectation, no result. The three resolutions here are THREE
    GROUPS in the canon's terms, not three independent runs: the same
    call, the same pair of receipts, only the input picture size differs.
---

# Structure of the measurement: one pair of receipts, three resolutions

## Assertion

The same model, the same call, the same pair of CORD receipts — the only thing that changes is how hard the picture is compressed before sending.

## Visual

> **The call.** `POST https://openrouter.ai/api/v1/embeddings`, `model: amazon/titan-embed-image-v1`, input — a single `data URL` string (`data:image/jpeg;base64,…`), with no separate text field.

| Resolution | JPEG quality | Approximate base64 size |
|---|---|---|
| 300×450 (real scan) | q80 | ~18,000–26,000 characters |
| 128×192 (preview) | q75 | ~4,300–4,600 characters |
| 64×96 (icon preview) | q80 | ~6,000–8,000 characters |

## Speaker notes

This is the structure of the measurement, and this frame deliberately has not a single result on it — that's on the next beat.

What's being compared is the same call on the same pair of receipts from the open CORD dataset — three separate experiments weren't set up here; only one thing changes: how hard the picture is compressed before sending. Three hundred by four hundred fifty pixels is the resolution of a real scan, the very same size the other three cases of this session work with all day today: this is exactly the size that should be used in a working production solution, if it ever got there. One hundred twenty-eight by one hundred ninety-two and sixty-four by ninety-six are two downsized previews, taken as a bracket: they weren't added here for show — if the model stops seeing a difference between pictures at some level of compression, a bracket of three points shows whether that happens gradually or sharply.

The model is the same across all three rows — `amazon/titan-embed-image-v1`, called through OpenRouter by an ordinary HTTP request to `/v1/embeddings`, the same endpoint already seen in this session's text cases. The input is a single `data URL` string: there are no two separate fields for "text" and "picture" here, only a header with the content type and encoding, then the picture itself in base64. The size of that string is exactly what's named in the table — it's what determines how much "weight" of the picture actually reaches the model: the lower the resolution and the compression quality, the shorter the string.

This is multimodal embedding, a continuation of this session's binary-data line: S8 gave the payload limits and a basic introduction to pictures, S9 — the model reading a document, and here the line is extended to storage and search by image, through the same vector-store node that already worked with text in the first case.

Next — what result this check should give if the model really does see the picture.
