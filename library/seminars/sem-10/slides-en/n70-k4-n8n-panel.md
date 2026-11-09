---
id: n70
type: mechanism_node_graph
duration_min: 0.5
assertion: "The request body isn't text with the model's name in view, but the expression `{{ $json.body }}`: the picture and the model are assembled by an earlier node, this node only sends them"
learning_goal: "Case 4's layer 2, beat 2 of 2: the real settings panel of the Embed image node — a JSON body as an expression, not a literal. The OpenRouter credential — the same type as in Case 1 (not repeated in detail here — already named and shown on n17, S8: don't assume the room remembers another session, but this is the same day and the same course node, a reference is enough). A separate beat (letter-tail, per README §1 reconciliation), not folded into n69."
visual:
  pattern: mechanism_node_graph
  figure: case4-n8n-embed-panel-real.png
  primary: >
    A real screenshot of the bottom part of the `Embed image` node's
    settings panel: `Body Content Type: JSON` → `Specify Body: Using JSON`
    → `JSON: {{ $json.body }}`.
  backup: >
    Source: `stend/n8n-screenshots-raw/case4-embed-image-panel.png`
    (846×1846, taken by `stend/n8n_shots.py`), crop —
    `rendered/compose_case4_real_screens.py::embed_panel()` — cut out at
    (0,1253)-(846,1621), frame proportion 846×368 ≈ 2.3 (the same
    proportion as the crop of Case 1's `Simple Vector Store` panel,
    matched to the same height ceiling, `deck_kit.FIG_NATURAL_H`,
    otherwise the frame ends up as a narrow column with a "DIAGRAM
    SQUEEZED" warning).

    WHY THIS PART OF THE PANEL WAS TAKEN, AND NOT THE TOP ONE (`Method`/
    `URL`/`Authentication`/`Credential Type`/`OpenRouter account`): the
    full node form, 846×1846, doesn't fit a landscape frame as a single
    piece of the needed height — a choice between top and bottom is
    unavoidable, and the bottom was chosen. The URL endpoint
    `/v1/embeddings` and the credential type "OpenRouter" were already
    shown and named once in text on Case 1's panel (`n17`, the same
    session day) — going over it again here would add not something new,
    but the same thing again (the selection rule — node design, Case 4 of
    Seminar 8: "confirming the node's identity, not a second lecture on
    the same thing"). The bottom part shows exactly what wasn't on Case
    1's panel at all: the request body as an EXPRESSION, not literal text.

    WHAT EXACTLY IS VISIBLE AND WHAT FOLLOWS FROM IT: the `JSON` field
    holds not the picture itself and not the model's name literally, but a
    reference `{{ $json.body }}` — an n8n expression substituting a value
    computed FURTHER UP the chain (in the node that assembles the request
    body — the model's name, the picture's data URL, and the JSON
    structure). This honestly shows the node's setup rather than hiding
    it: the picture itself isn't visible on this frame for the same reason
    it isn't visible on any panel in the course — system identifiers and
    large binary values aren't surfaced on screen (canon
    proektirovanie-keysa-i-voprosa.md §3) — and here additionally, simply
    because by the time the panel is shown live, the node hasn't yet been
    executed with a real input (the same property of the capture moment as
    the empty `INPUT` on Case 4's panels in Seminar 8).
---

# The real panel: the request body is an expression, not text

## Assertion

The `JSON` field doesn't literally hold the picture and the model's name — it holds a reference to a value assembled by an earlier node in the chain.

## Visual

> `Body Content Type: JSON` → `Specify Body: Using JSON` → `JSON: {{ $json.body }}` — the same request-body setup the text-embedding node already showed in the first case of this session, only here `$json.body` holds a picture, with no text.

## Speaker notes

This is the bottom part of the `Embed image` node's settings panel — a continuation of the screen we just saw. The top part of the panel — the address, the auth type, the choice of OpenRouter account — is set up exactly the same way as the text-embedding node in the first case of this session, and there's no point going over it a second time here: the same node type, the same way of connecting, the same place for the credentials.

The bottom part is more interesting, and that's exactly what this frame shows. The request body's content type is JSON, the way to set it is "Using JSON," and the content itself isn't text or a picture you could literally read on screen: it's the expression `{{ $json.body }}`. This is n8n's notation for "take a ready-made value already computed earlier in the chain, and substitute it here whole." The picture itself as a `data URL`, the model's name, and the request structure are assembled by the node before this one — this node has nothing to do with that part, and `Embed image` only forwards them further, to OpenRouter.

This is an honest picture of the node's setup; calling it stripped down would be wrong. System-level details — such as the content of the long `data URL` string with the picture inside — are deliberately not surfaced on the course's screen: looking at a few thousand characters of base64 gives the viewer nothing — it only eats up space on the frame. The expression `{{ $json.body }}` is exactly the honest way to show the request's setup, without hiding the detail and without dressing it up as a decorative label: the frame shows exactly what an engineer would see opening this node on the live rig — a reference to the value; the value itself isn't shown here.

This doesn't contradict the fact that the node is really executed and really sent the request. The settings panel shows the node's CONFIGURATION — how it's assembled; it doesn't show the state of a specific run. The fact that the model at the other end of this request doesn't use the picture at the real scan's resolution is a finding from the controlled measurement at three resolutions that we just broke down, and that finding is about the model's behavior — it has nothing to do with the n8n node's setup: the node is configured correctly and does exactly what's asked of it — sends the stated body to the stated address. What the model does with that body on the provider's side after that is beyond this point — n8n takes no further part — and that's exactly what needs to be checked by a controlled experiment; reading the settings panel won't check it.
