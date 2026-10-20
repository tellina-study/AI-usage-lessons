---
id: n52a
type: result_preview
duration_min: 0.75
assertion: "The coordinator doesn't see a node, a byte count, or a run log — he gets a photo card with a caption in the same notifications chat where only text used to arrive"
learning_goal: "New letter-tail slide between n52 and n53, owner's voice edit 2026-10-20 (issue #274), transcript 15:01: alongside the diagrams, every case needs a matching screen showing what the end user actually sees. Same pattern already used for Case 1 (n12) and Case 3 (n34b) — a positive mockup before the case wrap-up."
visual:
  pattern: result_preview
  primary: >
    A mockup of one Telegram chat message — a photo card with a short
    caption, in the same training-center notifications chat as Case 1.
    The caption under the mockup ties it to the scene (n46): shows the
    successful case, where the file fits the measured limit and the card
    arrives whole.
  backup: >
    The caption text is literally the same one already used in Case
    1's mockup (n12-k1-rezultat-preview.md: "New request from Maria:
    topic 'course', also mentioned: payment.") — not invented for this
    slide. The reuse is grounded in the solution's own architecture:
    n50 (speaker notes) directly names the chain's first node "the
    same value-substitution trick we configured in the
    'Notifications' case" — that is, the caption text in Case 4 is
    assembled by the same formula as the message text in Case 1, and
    it diverges from it only in that it now arrives as a photo's
    caption rather than a separate text message (that very card
    marketing asked for in the n46 scene). The mockup has no node
    name, no byte count, no `sendPhoto` threshold, and no
    workflow/execution id — only what the coordinator actually sees
    (canon §3 proektirovanie-keysa-i-voprosa.md: service ids belong in
    the production documentation, not on the visible screen). The
    SUCCESSFUL case is shown (the file fits the limit) as the flip
    side of the scene (n46, where the card disappeared quietly) and
    the measured boundary (n50, where the same file, but larger,
    produced an explicit API error) — the same trick as n34b: a
    positive mockup before the case wrap-up, not a repeat of the
    failure scene. There's no interface figure/mockup on disk yet —
    the slide is assembled as a text representation of the chat (a
    blockquote), like n12 and n34b, ready for the designer's visual
    realization at the render phase.
---

# What the coordinator sees on a successful send

## Assertion

One bubble in an already-existing notifications chat — a photo and a caption under it, no separate screen, no node name, no byte count.

## Visual

> **Telegram, "Training center notifications" chat.**
>
> A photo card, captioned with the notification text: "New request from Maria: topic "course", also mentioned: payment."

The same caption as in Case 1 — the notification text here is built by the same substitution formula, only now it arrives as a photo's caption instead of a separate message. This is the successful case: the file fits within the measured boundary, and the card arrives whole.

## Speaker notes

Before going back to wrapping up the case, it's worth pausing for a second to look at the exact same thing from the other side — through the coordinator's eyes, as he simply opens Telegram.

When the file fits within the limit — and we've just measured that limit with a real API call — the coordinator sees no run log, no sending node, no byte count. He opens the same notifications chat where he used to get text messages about new requests, back in the "Notifications" case, and sees a photo in it with a caption: "New request from Maria: topic "course", also mentioned: payment."

This caption isn't new text invented specifically for the card. It's the exact same text we already saw in the session's very first case, assembled by the same value-substitution formula from the request's fields. The only difference is that now it doesn't arrive as a separate message — it comes as a caption to the photo attached to the same notification, exactly the extension marketing asked for in this case's scene.

It matters what isn't on this screen. There's no name of the node that assembled the text or fetched the picture by its link. There's no byte count and no word "limit" — the coordinator doesn't need to know exactly where the boundary sits to understand that the request has arrived. There's no run log and no mark that everything is "green." This is the same boundary the course has talked about from the start: service-level details live in our breakdowns and in the production documentation, and on a real person's screen there's only what that person needs to know to understand what's happening.

And this is exactly the flip side of the scene the case opened with. There, the run was green, and the coordinator's chat was empty — or held a cut-off file. Here, the run is also green, but the coordinator sees a whole card, because this time the file fits within the measured boundary. The difference between these two states isn't visible in the n8n log or in the Telegram API's response by itself — it's only visible here, in the recipient's own chat, and by exactly one sign: did the picture arrive whole or not.

This is exactly why it was worth measuring the byte count as precisely as we did on the previous screens: the single reason to measure the size boundary is so the coordinator sees exactly this chat every time, instead of an empty space where a card should be.
