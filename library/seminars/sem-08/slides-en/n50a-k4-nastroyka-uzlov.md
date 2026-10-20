---
id: n50a
type: mechanism_node_graph
duration_min: 2.25
assertion: "Settings panels, not the canvas and not a retelling: on the left the `Compose notification (template)` node — the same expression as in Case 1, unchanged; in the middle `Fetch card image (HTTP)` — the GET method and the real picture URL at the top, the «File» response format and the binary field name at the bottom; on the right `Send card (Telegram photo)` — the real recipient, the binary data, and the caption built from the notification text, all visible in full"
learning_goal: "Owner's voice edit 2026-10-20 (issue #274): every case needs a full-chain screenshot with a comment on what was added, followed by per-node settings screenshots. n50 gives the wide chain view; this slide is the second half — real settings panels for all three nodes. Revision: added a minimal Compose panel to confirm the node is unchanged, not re-explain substitution."
visual:
  pattern: mechanism_node_graph
  figure: k4-uzly-nastroyka-real.png
  primary: >
    A composite of three real crops of the live rig, side by side: on the
    left — the minimal panel of the `Compose notification (template)`
    node (title, Mode, Fields to Set, the expression line itself — no
    lower service tail); in the middle — the `Fetch card image (HTTP)`
    node's panel, top (title · Method · URL) and bottom (Response Format ·
    Put Output in Field) of the SAME screenshot, stitched vertically with
    an explicit caption naming exactly what's skipped between them; on the
    right — the `Send card (Telegram photo)` node's panel in full, one
    solid crop, with the Chat ID masked by a rectangle.
  backup: >
    SCREENSHOTS TAKEN 2026-10-20 from the live rig (the same Playwright
    capture channel as n50/n22a):
    library/seminars/sem-08/stend/n8n-screenshots-raw/
    case4-compose-notification.png, case4-fetch-image.png, and
    case4-send-telegram.png (1900×1100 each) — the open settings panels
    of the workflow "C8 · Case 4 — photo in Telegram"'s three nodes,
    the same process as on n50's overview frame and on n48
    (`k4-n8n-razbor-real.png`).

    LEFT panel (`Compose notification (template)`) — NEW in this
    revision round, one solid crop (0,0)–(1160,430): the node's title,
    the Parameters tab, `Mode` = Manual Mapping, `Fields to Set` → the
    `notification_text` field (type String) and the entire expression
    line itself, word-for-word the same one that was already on Case
    1's panel (n11a/n14a): «Новая заявка от {{
    $('Request form').item.json['Имя'] }}: тема «{{
    $('Vocabulary check').item.json.topic }}»...» — in English, what
    this produces: "New request from {name}: topic '{topic}'...". The
    crop is deliberately kept to a minimum — below this point the real
    panel still continues with "Drag input fields here / Add Field,"
    "Include Other Input Fields," and "Options," the same service tail
    already shown and named uninteresting on the Fetch panel (see
    below), and here it's cut off with no separate caption noting the
    omission: the crop stops at a meaningful boundary (the end of the
    visible expression line), not mid-field, so it doesn't read as
    misleading. This is a CONFIRMATION that the node is the same one,
    not a repeat breakdown of the substitution trick — the breakdown
    of the substitution itself stays with Case 1 (canon §8.1 isn't
    violated here: the term and the mechanism aren't introduced again,
    only recognized on a new screen).

    MIDDLE panel (`Fetch card image (HTTP)`) is assembled as a
    TWO-STRIP crop of one screenshot, not a splice of different
    screenshots: top — the region (0,0)–(1160,290) (the node's title,
    the Parameters tab, Method=GET, URL=
    `https://picsum.photos/800/450`); bottom — the region
    (0,630)–(1160,900) (Response Format=File, Put Output in
    Field=data). Between them — an honest caption right on the figure:
    "Authentication / Send Query Parameters / Send Headers / Send Body
    — untouched, default" — these are exactly the panel's four
    disabled toggles, none of them carries a lesson, and the slide
    doesn't pretend they don't exist — it names the omission out loud
    rather than staying silent about it. The reason for the two-strip
    crop isn't aesthetic: the needed fields (the URL at the top, the
    response format at the bottom) sit farther apart on the real panel
    than fits the slide's allotted height without shrinking the
    diagram (canon `deck_kit.py: FIG_MIN_FILL` — a solid crop of the
    whole panel gives a portrait ratio that has already broken the
    layout once before, see the n23 backup on
    `case2-jev-node-config.png`).

    RIGHT panel (`Send card (Telegram photo)`) — one solid crop
    (0,0)–(1160,700), with nothing skipped: `Credential` = Telegram
    account (C8), `Resource` = Message, `Operation` = Send Photo,
    `Chat ID` (masked, see below), `Binary File` is on, `Input Binary
    Field` = data, `Reply Markup` = None, `Additional Fields` →
    `Caption` = `{{ $json.notification_text }}`. There was nothing to
    skip here — every field is set away from its default and carries a
    lesson (the recipient, the binary data, the caption built from the
    chain's first node's text).

    MASK: the `Chat ID` field on the right panel showed the real
    number 266536553 — the rig's test account's personal Telegram id,
    not relevant to the lesson. Masked with a rectangle captioned
    "masked, the rig's personal id" — the field is titled `Chat ID` on
    the screenshot itself, so the room sees what kind of parameter it
    is, just not whose number it is.

    HONESTLY, about INPUT: on all three screenshots the INPUT panel is
    empty — "No input data" / "Execute previous nodes," unlike n22a
    (there the INPUT tree shows the previous nodes' real fields) — on
    these rig nodes, the chain's earlier steps weren't run before the
    screenshot was taken. The frame is left as it is, not touched up;
    the only thing actually measured here, and the only thing that
    needs to be real, is the parameters panel on each of the three
    halves, and it is real and complete within its allotted bounds.

    The composite is assembled in `rendered/make_figures_k4.py`, the
    function `uzly_nastroyka()` — a direct PIL crop + splice, with no
    redrawing, the same principle as `k2-n8n-panels-real.png` (n22a).
    The final file is 3528×700 (ratio 5.04) — fits the intake layout
    without compression, with a comfortable margin above the
    `FIG_MIN_FILL` threshold. No workflow/execution id on screen
    (canon §2–§3).
---

# Node settings: the parameters screen

## Assertion

Here's what's actually inside these three nodes — not the canvas and not a retelling of the formula, but each one's settings panel, with the fields shown in full.

## Visual

> **The `Compose notification (template)` node.** `Mode`: Manual Mapping. The `notification_text` field: the same expression that was already on this node's panel back in Case 1 — not rewritten, not simplified for the demo.

> **The `Fetch card image (HTTP)` node.** `Method`: **GET**. `URL`: `https://picsum.photos/800/450` — the real source of the test picture, not invented for the example. Below, past a skipped block of unchanged toggles: `Response Format` = **File** (from this point on the node's content is binary data, not text or JSON), `Put Output in Field` = `data`.

> **The `Send card (Telegram photo)` node.** `Credential`: Telegram account (C8). `Resource`: Message, `Operation`: Send Photo. `Chat ID` — the real recipient (masked on the figure, not relevant to the lesson). `Binary File` is on, `Input Binary Field` = `data` — the same field name the previous node set. `Caption`: `{{ $json.notification_text }}` — the photo's caption comes from the chain's first node.

## Speaker notes

Here's what these three nodes actually look like once you open each one's settings panel on the live rig — not a retelling in words, but what's really on screen.

The left panel is the `Compose notification (template)` node, the chain's first step. On the previous screen it was said that it assembles the text with the same substitution trick we configured in the "Notifications" case — and here you don't have to take that on faith: here's the panel itself, and the `notification_text` field holds exactly the same expression that was already on screen back in Case 1. There's no point breaking it down again — that's already been done there — but it was worth showing right here that this is literally the same node, not one rewritten from scratch for a new task.

The middle panel is the `Fetch card image (HTTP)` node. The request method is GET, and the URL is visible in full: `picsum.photos/800/450`, a real public test-picture service, not a source invented for the example. Further down the real panel there are four toggles — authentication, query parameters, headers, request body — and all four are off, untouched by anyone; on the figure that part of the panel is replaced with a direct caption naming exactly what's skipped, not silently cleaned away. But the next setting after them matters: the response format is set to `File`, not text, not JSON. It's exactly this field that turns the node's content into binary data — that's the whole difference between "download a picture" and "download text that happens to contain a link to one." Below it is the name of the field the node will put that binary data into: `data`.

The right panel is the `Send card (Telegram photo)` node. At the top — the Telegram account's credentials and the chosen operation: sending a photo, not a text message. Further down — `Chat ID`, a real numeric recipient; on this screen it's masked, because it's the live rig's test Telegram account's personal id and has nothing to do with the lesson, but the field itself and its role are shown honestly. Below — the `Binary File` toggle is on, and the input field's name is `data`, the exact name the previous node put the picture into: these nodes are connected not only by an arrow on the canvas, but by a matching field name. And at the very bottom — `Caption`, the photo's caption: `{{ $json.notification_text }}`, the same expression the chain's first node assembled, already broken down back in Case 1.

Notice the INPUT panel on all three screenshots — it says "No input data": the chain's earlier nodes weren't run before this screenshot was taken, this is an open configuration, not the result of a run. That's shown honestly, not dressed up as something bigger, and the only thing actually being measured here is the real parameters panel on each of the three halves, not an empty left-hand side.

Now we have not just a path on the canvas, but what's really configured inside each step of that path — including the first one, already familiar from last case.
