---
id: n12
type: result_preview
duration_min: 0.75
assertion: "Olga doesn't open a separate screen — the notification arrives in the same bot chat as other alerts, as one line"
learning_goal: "New slide (n12), inserted between n11 and n14 by the owner's voice edit, 2026-10-20, issue #274: shows what the final answer looks like visually for the user, before we show the real runs with the error. Placed BEFORE the failure-demo slide (n13), per the owner's direct instruction."
visual:
  pattern: result_preview
  primary: >
    A mockup of a single Telegram chat message — the target-shape
    notification text. A caption under the mockup ties it back to Olga's
    request from the scene (n06).
  backup: >
    The message text is the target example from the scene (n06), matching
    the text actually delivered in the real execution (the LLM version,
    Maria's request) — confirmed in `stend/README.md`, "Case 1 — LLM
    notification vs. template". No execution id is shown on the slide
    (canon §3). No figure asset exists on disk yet — the slide is
    assembled as a text representation of the chat (a block quote), ready
    for the designer to turn into a real interface mockup at render time.
---

# What the message looks like on Olga's phone

## Assertion

A single message bubble in a chat she already has with the bot — no separate screen, no attachments, no buttons.

## Visual

> **Telegram, chat "Training center notifications."**
>
> New request from Maria: topic "course," also mentioned: payment.

Exactly what Olga described in the previous scene, word for word: who wrote, on what topic, and what else they mentioned — one line, with no need to open the result screen.

## Speaker notes

Before we look at how this gets assembled inside the chain, let's look at what Olga herself actually sees — on her phone, not on the result screen inside n8n.

She doesn't open anything new. She already has a chat with the notifications bot — the same bot the center uses for other alerts too. One message lands in that chat: "New request from Maria: topic 'course,' also mentioned: payment." One bubble, no attachments, no buttons, nothing to click through to understand what it's about.

The message's shape wasn't chosen arbitrarily — it's exactly the three values Olga named as sufficient in the previous scene: who wrote, on what topic, what else they mentioned. Not more, not less. Add one more field to the line — say, payment status or an internal request number — and the notification stops reading at a glance: it turns into text you have to parse, instead of skimming among twenty similar messages a day.

In the interface, this looks ordinary, and that's the whole point of the slide. The new message simply appears in the same chat where the history of all the center's earlier notifications already lives — no separate tab, no new icon, nothing else to navigate to. Olga reads this chat top to bottom exactly the way she read it yesterday and the day before; only the content of one line changes, not the habit she already has.

This is exactly the example Olga named in the previous scene, word for word — who wrote, on what topic, what else they mentioned. Three values, one line. If the message looks like this on every request, the task is fully solved: it's enough for Olga to read the notifications, without opening the result screen over one multi-topic request among twenty ordinary ones.

The question is whether it looks like this every time, on any request, not just this one. The next screen shows real runs of this same node, not a made-up example — and one of them looks different from this.
