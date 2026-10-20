---
id: n50
type: mechanism_node_graph
duration_min: 3.5
assertion: "Three nodes assemble the card without a single model call, and the uncompressed 12,812,355-byte file — between n8n's 16 MB limit and Telegram's 10,485,760-byte photo limit — produced a real, explicit Telegram Bot API error, not silence"
learning_goal: "Case 4 solution, layer 2 — a real screenshot of the live n8n rig (Playwright, 2026-10-20) with the actual three-node chain + a real size boundary, checked with an actual call. Parameters are real, taken from the rig's files; no workflow/execution id on screen. The error text is a real API quote, not a service id, so it's given in full."
visual:
  pattern: mechanism_node_graph
  figure: k4-n8n-tsepochka-real.png
  primary: >
    A real screenshot of the n8n canvas (workflow "C8 · Case 4 — photo
    in Telegram," live rig): node "Compose notification (template)" → node
    "Fetch card image (HTTP)" (a GET request to a link is visible) → node
    "Send card (Telegram photo)." Below the diagram — a three-number table
    and the real Telegram Bot API error text (a separate text block, not
    part of the screenshot).
  backup: >
    SCREENSHOT TAKEN 2026-10-20 from the live rig
    https://n8n.lessons.tellian.io via Playwright (workaround —
    ~/.cache/page-shot-libs/x; update to notes/mcp-limitations.md
    [#233-8]): a crop from
    stend/n8n-screenshots-raw/case4-telegram-image.png, workflow "C8 ·
    Case 4 — photo in Telegram." REPLACED the schematic diagram — the
    former file rendered/figures/k4-n8n-tsepochka.png stays untouched on
    disk, the slide no longer references it. Node names are read
    literally off the screenshot: "Compose notification (template),"
    "Fetch card image (HTTP)" (under the title the parameter `GET:
    https://picsum.photos/8…` is visible — real, this is the actual
    source of the test picture, not invented for the example), "Send
    card (Telegram photo)" (caption `sendPhoto: message`). The nodes
    and parameters match stend/stage-4.json by meaning
    (BRIEF-PROIZVODSTVO.md §3). The numbers and the error quote are
    from SETKA-KEYSOV-S8-part2.md and stend/README.md, section "Case
    4," checked by a direct call to the Telegram Bot API (an ephemeral
    host for feeding a file this size into the image-fetch node was
    unavailable at the time of checking) — named honestly, not
    disguised as a run through n8n; this is still true, the screenshot
    only changes the fact that the canvas is now real. HONESTLY:
    stage-4.json on the rig contains exactly these three nodes and does
    not contain a separate size/format-check node — layer 1's
    architectural rule (n49) is demonstrated on the rig by the boundary
    diagnostic below, not by a separate built node, unlike Cases 1 and
    3, where both versions are actually built. This remains an open
    item of the production phase, not a contradiction of the source.
    The owner requested real n8n node-settings screenshots via the
    2026-10-20 voice edit (issue #274); the "live UI unreachable"
    limitation (notes/mcp-limitations.md [#233-8]) was lifted the same
    day.
---

# The chain in n8n and the size boundary, checked with a real call

## Assertion

Text gets assembled by substitution, the picture by a direct request to a link, sending by an ordinary API call. A model takes part in none of the steps, and the size boundary is checked by a real call, not by assumption.

## Visual

| What | Bytes |
|---|---|
| Checked file | **12,812,355** (~12.8 MB) |
| Telegram's photo limit | **10,485,760** (10 MB) |

> Telegram Bot API's response: `"Bad Request: file of size 12812355 bytes is too big for a photo; the maximum size is 10485760 bytes"`

## Speaker notes

The second layer is the same architecture, assembled in n8n as three specific nodes, plus a real check of the exact boundary layer one talked about.

The first node is the same substitution trick we configured in the "Notifications" case: a single expression that assembles the notification text out of fields the request already carries. The second node fetches the picture by its link; the important setting detail is that the response format is set to file, not text or JSON — from that point on, this node's content is binary data. The third node sends it to Telegram in photo-sending mode, with the picture's binary data as input and a caption — the text from the first node. Notice what's missing from this chain: a model never shows up at any of the three steps, and there's no separate size-or-format check node either — layer one's rule still lives at the architecture level, not inside a specific node, and that's shown honestly, not papered over.

That's why we checked the boundary with a real call instead of an assumption. n8n's own default limit for binary data is 16 MB. Telegram's limit on photos is separate and narrower: 10,485,760 bytes, that is, 10 MB. We deliberately assembled an uncompressed file right between these two thresholds — 12,812,355 bytes, about 12.8 MB: under n8n's limit, but over Telegram's photo limit. We sent it directly through the Telegram Bot API — the same call the sending node inside the chain uses.

The response that came back is real, not invented for the example: a file of a given size is too big for a photo, with the maximum size stated. Telegram directly names the size and directly names the limit — not silence, but an explicit, readable error. And this sharpens what we saw in the case scene: there, the card disappeared quietly — because a problem at n8n's boundary more often looks exactly like that, while Telegram, at its own boundary, answers differently, in plain text. A size check inside the chain can't rely on either side necessarily reporting an error honestly.
