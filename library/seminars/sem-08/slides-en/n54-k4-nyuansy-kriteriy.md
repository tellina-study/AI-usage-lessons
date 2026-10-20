---
id: n54
type: criteria_checklist_and_boundary
duration_min: 2.5
assertion: "Two independent limits, not one, and a manual run on binary data eats memory noticeably harder; you always need to check a file's size and format, and you don't need anything beyond that — closes the axis's fourth row"
learning_goal: "Nuances (3 classes) + Case 4 criterion + closing the axis's fourth row. The third nuance is dropped last of the three, per CUT-ORDER.md — the first two carry the actual measured error from the screen."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    Three nuances as short paragraphs, below them a two-column criterion
    table, the axis's closing row as a separate callout.
  backup: >
    The nuances and the criterion are a direct unfolding of "Nuances"
    + "Criterion" from SETKA-KEYSOV-S8-part2.md, section "Card in
    Telegram," with no added numbers.
---

# When binary data needs separate attention

## Assertion

Two independent limits, not one, and a manual run on a file eats memory noticeably harder than on text.

## Visual

1. **n8n's own default limit — 16 MB** on binary data. For a photo with text that's usually enough, but a high-resolution scan or a phone photo — not always.
2. **Telegram's limits are a separate, narrower ceiling**, and they differ for photos and for documents. Something that got past n8n's limit can still fail to get past the delivery channel's limit — two independent thresholds, not one.
3. **A manual run with binary data uses noticeably more memory** than an automatic one — the difference is more noticeable than on text fields, and it's worth keeping in mind while debugging a node like this live.

| Always needed | Not required by this session |
|---|---|
| checking the size and format before sending any file or image in the chain | storing many files |
| knowing the delivery channel's limit, not just the orchestrator's own limit | searching among attachments and processing their content with a model |

> **The axis's fourth row is closed.** Looked reliable: the picture got assembled and sent to Telegram. Turned out to be: as long as it fits the limit — a large file either arrives partially or not at all, and the run stays green regardless.

## Speaker notes

Three classes of nuance, and then the criterion and the axis's last row.

First. n8n's own default limit on the size of binary data is 16 MB. For a photo with text that's usually enough, but a high-resolution scan or a phone photo straight from the camera — not always: that's exactly what the file in our scene looked like.

Second. Telegram's limits are a separate, narrower ceiling, and they differ for photos and for documents. Something that got past n8n's limit can still fail to get past the delivery channel's limit: these are two independent thresholds, not one, and checking one doesn't excuse you from checking the other.

Third. A manual run with binary data uses noticeably more memory than an automatic one — we already saw this with text data last session, but on a file the difference is more noticeable, and it's worth keeping in mind if you're debugging a node like this live on your own rig.

The criterion. You always need to treat binary data as a separate contract whenever a file or image passes through the chain, not just text fields: checking the size and format before sending, and knowing the delivery channel's limit specifically, rather than only the orchestrator's own default limit, is the baseline, with no exceptions carved out by task type. And what this session doesn't require of you — not in the deck, and not in your own process back home — is anything beyond that baseline: storing many files at once, searching among them, or processing their content with a model is a next-level task, not part of the introductory one, and nothing here asks you to reach for it yet.

Let's close the axis's last row. Looked reliable: the picture got assembled and was sent to Telegram without a single visible complaint anywhere along the way. Turned out to be: as long as it fits the limit — a large file arrives partially, or doesn't arrive at all, and the run still stays green regardless, exactly as it did in the very first scene of this case.
