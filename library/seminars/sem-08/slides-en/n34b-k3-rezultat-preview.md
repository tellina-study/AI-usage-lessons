---
id: n34b
type: result_preview
duration_min: 0.75
assertion: "The client doesn't open a separate screen and doesn't see a node or a threshold — they get one short message saying the request is approved and the money has already been sent to their card"
learning_goal: "A new slide pairing the solution diagrams/setup (n30b, n34, n34a) with what the end user actually sees, before the version-comparison table (n35) — the same 'what the user sees' pattern already used in Case 1 (n12)."
visual:
  pattern: result_preview
  primary: >
    A mockup of a single support-chat message — short text about the
    approved refund and the money transfer to the card. The caption under
    the mockup ties it to the request from the scene (n28): 2,500 rubles, an
    example below the threshold.
  backup: >
    The amount is taken verbatim from the example already used in the deck
    (n28: "please refund 2,500 rubles for a missed class") — an amount
    below the 3,000-ruble threshold, i.e. exactly the case version 2
    approves automatically (the `IF` node, n30b/n34); no new amount was
    invented. The mockup shows no node name, threshold, or workflow/
    execution id — only what the client actually sees. No interface figure
    exists on disk yet; the slide is built as a text representation of the
    message (a blockquote), same as n12, ready for the designer's visual
    pass at render time. Mirrors RU n34b (issue #274).
---

# What the client sees on automatic approval

## Assertion

The client doesn't open a result screen inside the chain and doesn't see which node made the decision — into the chat where they've already been messaging the center comes one short message: the request is approved, the money has been sent.

## Visual

> **Training-center support chat.**
>
> Your refund request has been approved. 2,500 rubles have already been sent to the card you used to pay for the class.

The same amount from this case's scene: "please refund 2,500 rubles for a missed class" — an example below the threshold, so version 2 approves it on its own, without the manager, and the client sees the result, not the mechanics of the decision.

## Speaker notes

Before returning to comparing the versions, it's worth stepping into the client's shoes for a second and looking at what they see when their request is approved automatically.

Recall the request from the scene: "please refund 2,500 rubles for a missed class." The amount is below the three-thousand-ruble threshold, so both version one and version two would approve it on their own, without the manager. The difference between the versions is in how that decision gets made inside the chain — the client doesn't see it at all.

The client doesn't open any separate result screen, doesn't log into a personal account, and doesn't wait for an email with an attachment. Into the chat where they've already been messaging the training center comes one short message: the request is approved, and the specific amount has already been sent to the card they used to pay for the class. One bubble, no attachments, no buttons — exactly like the first case of this session, where the same kind of short notification arrived in an already-existing chat.

What matters is what this message doesn't contain. No name of the node that made the decision, no word "threshold" or number "three thousand," no internal request or execution id — none of what we just walked through on the diagram and in the node settings. This is the same boundary the course has pointed to from the start: operational details live in our breakdowns and in production documentation, while the screen a real person sees carries only what they need to know to understand: the money is already theirs.

And this isn't a feature specific to version two. If version one, with its text prompt, had also decided to approve this request, the client would have seen exactly the same message — because everything that changes between the versions happens before this screen, inside the chain, not in the interface the client sees. The difference between the versions is a difference in how reliable the decision itself is, not in what the person ultimately receives.

A question worth holding onto: if the request amount happened to land exactly on the three-thousand-ruble threshold — and we just saw exactly where version one kept getting this wrong — would the client get this same message, or a different one, about the request being passed to the manager? The answer is in the comparison we're returning to now.
