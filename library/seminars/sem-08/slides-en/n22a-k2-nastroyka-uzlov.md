---
id: n22a
type: mechanism_node_graph
duration_min: 1.5
assertion: "Settings panels, not a paraphrase: on the left — the three fields of the `Normalize + hash` node with their expressions shown whole on screen; on the right — the single condition of the `Exact duplicate in window?` node, line for line with what's actually configured on the rig"
learning_goal: "Letter-tail slide between n22 and n23, per the owner's 2026-10-20 voice edit asking for real node-settings screenshots instead of prose paraphrase. The expressions on these real panels reference actual Russian-language field names from the live n8n form — a documented, deliberate exception to the EN track, not an untranslated artifact (see glossary.en.yaml and the explanation below)."
visual:
  pattern: mechanism_node_graph
  figure: k2-n8n-panels-real.png
  primary: >
    A composite of two real n8n settings-panel screenshots, side by side: on
    the left — the node `Normalize + hash` (`Set`, Manual Mapping mode,
    three fields with expressions), on the right — the node `Exact duplicate
    in window?` (`IF`, one condition). Both are live-rig parameter panels,
    not a canvas and not a drawn diagram.
  backup: >
    SCREENSHOTS TAKEN 2026-10-20 from the live rig (the same capture channel
    as n22/n23): library/seminars/sem-08/stend/n8n-screenshots-raw/
    case2-normalize-hash.png (1900×1100) and case2-exact-duplicate-if.png
    (1900×1100) — the open parameter panels of two nodes in the workflow
    "C8 · Case 2 — two-level dedup", the same process as on n22. The
    composite was assembled by a direct crop + join (no redrawing): the
    region (0,0)–(1160,660) was cut from each screenshot — the node's
    header, the Parameters tab, the whole parameter panel, without the empty
    right OUTPUT panel ("No output data") and without the left INPUT tree
    beyond the visible schema — the INPUT tree was kept, it's real and shows
    actual fields from earlier nodes. The two crops are joined horizontally
    with a neutral 24px gray bar between them; the result is saved as
    library/seminars/sem-08/rendered/figures/k2-n8n-panels-real.png,
    2344×660 (aspect ratio 3.55 — fits the layout without compression,
    canon deck_kit.py: FIG_MIN_FILL).

    The text on the panels reads literally, line by line:

    Left panel, node `Normalize + hash` (`Set`), Mode: `Manual Mapping`,
    three fields under Fields to Set — `normalized_hash` (String) = `{{
    $('Request form').item.json['Что нужно'].toLowerCase().trim()
    .replace(/\s+/g, ' ') }}`; `recent_same_contact_text` (String) = `{{
    $('Request form').item.json['Предыдущее сообщение (тест)'] || '' }}`;
    `recent_same_contact_hash` (String) = `{{ ($('Request
    form').item.json['Предыдущее сообщение (тест)'] || '').toLowerCase()
    .trim().replace(/\s+/g, ' ') }}`. Below that — the toggle "Include Other
    Input Fields" is on, "Input Fields to Include": All.

    ON THE FIELD NAMES: `'Что нужно'` ("what's needed") and
    `'Предыдущее сообщение (тест)'` ("previous message (test)") are NOT
    translation artifacts — they are the literal, real field names of the
    live n8n intake form (`Request form`), which was itself built with
    Russian field names. The expressions reference those fields by their
    real names because that is what the form actually calls them; renaming
    them on the slide would make the screenshot stop matching the live
    system. This is a documented, deliberate exception to the EN track's
    anti-mirror rule (see glossary.en.yaml) — the figure and the expressions
    inside it are left exactly as captured.

    Right panel, node `Exact duplicate in window?` (`IF`), Conditions tab:
    `{{ $json.normalized_hash }}` — operator "is equal to" — `{{
    $json.recent_same_contact_hash }}`; the toggle "Convert types where
    required" is off; the "Add condition" button shows there's exactly one
    condition.

    The earlier n22 text conveyed the formula `normalized_hash =
    text.toLowerCase().trim().replace(/\s+/g, ' ')` in prose and mentioned
    only one calculation "alongside, for the recent message" — correct in
    meaning, but it didn't show that this is actually THREE separate fields
    (including the raw, unnormalized text) and that the IF condition
    compares specifically the third field against the first, not the
    formula directly. This slide doesn't change the mechanics (they're the
    same as on n22/n21/n20) — it shows them exactly as they stand on
    screen, which is the fix for "the settings descriptions are also
    so-so".

    No workflow/execution id on screen (canon §2–§3) — both screenshots are
    clean parameter panels, with no address bar and no workflow ID.
---

# Node Settings: The Parameters Screen

## Assertion

Here's what's actually inside these two nodes — not a retelling of the formula, but each one's settings panel, with the fields and the condition shown whole on screen.

## Visual

> **Node `Normalize + hash` (`Set`, `Manual Mapping` mode).** Three fields with expressions: `normalized_hash` — the current request's normalized text (`$('Request form').item.json['Что нужно'].toLowerCase().trim().replace(/\s+/g, ' ')` — the field name `'Что нужно'` is the real, literal name of this field on the live Russian-language intake form, not an artifact of translation); `recent_same_contact_text` — the same contact's recent message as is, unchanged; `recent_same_contact_hash` — that same text, normalized by the same formula. "Include Other Input Fields" is on (All) — the rest of the request's fields pass through untouched.

> **Node `Exact duplicate in window?` (`IF`).** One condition: `{{ $json.normalized_hash }}` **is equal to** `{{ $json.recent_same_contact_hash }}` — the previous node's third field compared against its first. "Convert types where required" is off: the strings are compared as-is, with no hidden type coercion.

## Speaker notes

Here's what these two nodes actually look like if you open each one's settings panel — not a retelling in words, but what you'd see on screen if you opened the live rig yourself.

The left panel — the node `Normalize + hash`, `Manual Mapping` mode. It has three fields, not one. The first, `normalized_hash`, takes the current request's text from the `Request form` node — by the real, literal name that field carries on the live form (shown on the Visual above; it's in Russian, since the form itself is Russian, not a translation leftover) — and normalizes it: lowercase, trimmed edges, repeated internal spaces collapsed. The second field, `recent_same_contact_text`, is simply the same contact's recent message, unchanged, in case the text needs to be shown as-is rather than only compared. The third, `recent_same_contact_hash`, is that same text from the second field, run through the same normalization. The word "hash" in the field name isn't about a cryptographic hash here — it's a normalized string, the same operation as for the current request, just applied to a different text. At the bottom of the panel, the toggle "Include Other Input Fields" is on with the value "All" — the rest of the request's fields, topic, urgency, status, pass through the node intact and aren't lost along the way.

The right panel — the node `Exact duplicate in window?`, type `IF`. It has one condition, and it's shown in full: `{{ $json.normalized_hash }}` is compared with the operator "is equal to" against `{{ $json.recent_same_contact_hash }}` — that is, exactly against the third field the previous node computed. The toggle "Convert types where required" is off — the strings are compared as-is, with no hidden type coercion that could silently turn different values into "equal" ones. The "Add condition" button below shows the node has exactly one condition — there's no hidden logic off-screen.

Together these two nodes aren't the abstract formula from the previous screen — they're exactly what's configured on the rig: three fields in `Set` and one condition in `IF`, both shown in full. Next — the second, expensive node, the one that only sees what this condition didn't resolve.
