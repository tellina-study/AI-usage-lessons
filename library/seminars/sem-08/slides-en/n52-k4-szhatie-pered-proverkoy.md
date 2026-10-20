---
id: n52
type: mechanism_node_graph
duration_min: 2.5
assertion: "The mechanical check goes first and filters out junk cheaply, the content-check model goes second, only on what already passed; compressing a picture before that second step is fine and usually worth doing — but moderately, not below ~1024 px, if the model has to read text on the card"
learning_goal: "New slide, owner's voice edit 2026-10-20 (issue #274), a letter-tail between n51 and n53. Two explicit owner requirements: an explicit diagram of the mechanical-check → content-check-model order, not prose; an honest research answer on whether to compress before the check, with exact figures from the brief."
visual:
  pattern: mechanism_node_graph
  figure: k4-shema-szhatie-en.png
  primary: >
    A two-row diagram. Top — an explicit chain: file received → mechanical
    check → branch (did not pass → reject, goes no further / passed →
    content-check model, not built on the rig). Bottom — picture size
    before/after moderate compression ahead of sending to the content-
    check model, with a warning about reading text on the picture.
  backup: >
    The order "mechanical → model" isn't arbitrary: the mechanical
    check is essentially free (a condition over a number) and
    deterministic, while any model call doing image recognition costs
    real money per call (a separate figure from the GENERATION cost on
    n51 — the checking model's input is priced by image input tokens,
    not on the same scale as output generation, and this specific
    price wasn't estimated here, to avoid mixing two different pricing
    models without verification); putting the cheap filter first saves
    model calls on files that won't pass by format or size anyway —
    the same economy logic as Case 2's hybrid solution (hash first,
    jev on what's left), carried over to a picture. The answer about
    compression is VERBATIM from the voice-edit brief
    (`qa/BRIEF-GOLOSOVAYA-PRAVKA-2026-10-20.md`, lines 180-196, "Case 4
    research question — answer (WebSearch, not invented)"): 4032×3024
    uncompressed ≈1500 tokens, the same image at 720×540 at JPEG Q85
    ≈300 tokens — a fivefold saving; the caveat about OCR-like tasks
    and the ~1024 px limit on the longer side — the same quote, the
    numbers weren't changed. The source is marked on the slide as
    "public sources," not as a measurement on this rig — the checking
    model itself isn't built on the rig (see n49/n51), so the token
    saving can't be confirmed by our own run, only honestly cited.
---

# Check order and the compression question

## Assertion

The mechanical check comes first and is cheap, the content-check model comes second, only on what already passed. Compressing the picture before it is worth doing — but not past a limit.

## Visual

| Action | How it's done | Advantage | Drawback |
|---|---|---|---|
| No compression | as-is (4032×3024) | maximum detail | expensive — ≈1500 tokens |
| Moderate compression | Q75–85, ≤1024 px | ≈300 tokens, five times cheaper | clips fine print near the limit |
| Aggressive compression | low quality, < ~1024 px | even cheaper | text and detail become unreadable |

## Speaker notes

Before talking about compression, it's worth explicitly naming the order these two steps have to run in — and it isn't an arbitrary choice.

The mechanical check goes first. It's cheap, fast, and deterministic: it compares size, format, and resolution against a condition, and either lets the file through or rejects it right away, before it reaches anything more expensive. The content-check model goes second, and only on what already passed the first check: running an expensive model call on a file that won't pass by format anyway is a waste. This is the same economy we saw in Case 2: a cheap mechanical step absorbs most of the work, and the expensive tool only gets what genuinely needs its judgment.

Now — the question the course owner specifically asked us to research honestly rather than guess at: does it make sense to compress a picture before sending it to the content-check model. The answer, from public sources, not a measurement on our own rig: moderate compression is usually worth it and doesn't noticeably hurt accuracy. An example given in those sources: a 4032-by-3024 image, uncompressed, costs models roughly fifteen hundred tokens of processing; the same image, shrunk to 720 by 540 at JPEG quality 85, costs roughly 300 tokens — five times cheaper — and for most tasks that barely affects accuracy.

But there's an important caveat, and it can't be dropped silently. Tasks where the model has to read text in the image — and our card is exactly that kind, with readable text on it — degrade noticeably more from compression than most. The general recommendation is to compress carefully, not going below roughly 1024 points on the longer side, if the model needs to make out text or numbers on the card. Aggressive compression for a bit of extra savings isn't justified here: the cost of a misread is higher than the cost of a few extra tokens.

In the table this is laid out as three options to choose among, not one correct answer: no compression, moderate compression, and aggressive compression — each has its own cost and its own risk, and the choice depends on whether the model has to actually read text on the card or whether judging the picture as a whole is enough.
