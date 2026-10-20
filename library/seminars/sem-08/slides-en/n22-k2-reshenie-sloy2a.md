---
id: n22
type: mechanism_node_graph
duration_min: 2.0
assertion: "Normalization strips case and extra whitespace; the condition compares the resulting hash against the same contact's recent request — neither of the two nodes calls a model"
learning_goal: "Layer 2a of the 'our solution' beat: the real configuration of the normalization node and the exact-match condition — actual parameters from the rig, with no system ids on screen (canon §2–§3). The crop was widened in the same 2026-10-20 round to show the full process path, with detailed settings panels split off onto the new letter-tail slide n22a."
visual:
  pattern: mechanism_node_graph
  figure: k2-n8n-mehanika-real.png
  primary: >
    A real, wide screenshot of the n8n canvas (workflow "C8 · Case 2 —
    two-level dedup", live rig): the whole path from `Request form` and
    `Extract fields` on the left, through the node `Normalize + hash` (Set)
    and `Exact duplicate in window?` (IF) with true/false branches, to
    `Vocabulary check` → `Write row` → `Result screen` at the top — an
    overview of the process, not a tight crop of two nodes.
  backup: >
    SCREENSHOT INSERTED 2026-10-20, WIDENED THE SAME DAY (second round of
    edits, issue #274): a crop from
    stend/n8n-screenshots-raw/case2-dedup-prod-jev.png — this is the full
    canvas of the same workflow as on n23 (the jev node is visible there
    too, further down the canvas; it doesn't fall in this crop, it has its
    own crop on n23). Saved as
    library/seminars/sem-08/rendered/figures/k2-n8n-mehanika-real.png, the
    region (390, 300)–(1600, 695) of the source file, no enlargement
    (1210×395, aspect ratio 3.06 — fits the layout without compression).

    The FIRST version of this field (morning of 2026-10-20) used a tight
    crop (855, 540)–(1420, 705), ×2 — only two nodes, no path to them. The
    owner looked at the deck and explicitly demanded: "every case needs a
    screenshot of the whole process with a comment on what was added, and
    then screenshots of individual nodes with settings descriptions" — this
    was the tight, non-overview version. The crop was widened the same day,
    in the same round that added n22a: the frame now shows the whole path —
    `Request form` and `Extract fields` on the left, down to `Normalize +
    hash` → `Exact duplicate in window?` with true/false outputs, and
    separately at the top `Vocabulary check` → `Write row` → `Result
    screen` (the successful result-logging path). The detailed parameter
    panels (fields, expressions, the condition) are deliberately NOT visible
    on this overview frame — this is the canvas, not an open node panel;
    those are on n22a, the next slide.

    REPLACED the previous field (a programmatic diagram,
    k2-n8n-mehanika.png) — that figure was left untouched on disk, the
    slide no longer references it. The field's previous state called a live
    screenshot "physically unreachable in this environment (no root for a
    headless browser)" and left the question "screenshot or programmatic
    diagram" open to the owner — that was true at the time it was written
    (morning of 2026-10-20) and stopped being true the same day: by evening
    screenshots had been captured (the same channel that produced
    case2-jev-node-config.png and the case3/case4 screenshots on
    neighboring slides), notes/mcp-limitations.md [#233-8] was lifted.

    What's literally visible on the screenshot: the node `Normalize + hash`
    (Set icon, blue pencil) is connected by an arrow to the node `Exact
    duplicate in window?` (IF icon, dark-green fork), which has two outputs
    — true and false. Nearby are the nodes the request's path leads
    through: `Request form` (trigger), `Extract fields`, `Vocabulary
    check`, `Write row`, `Result screen` — the real, dense layout of the
    live n8n canvas, not a crop artifact; left as is, not cleaned up,
    honestly — we cut a rectangle, we don't redraw what's inside it.
    Partially visible at the bottom of the frame is the circle of the
    `Model` node (the model-based request-parsing branch) — also not
    cleaned up, honestly cut off at the frame's edge.

    The mechanics of the two nodes were NOT changed by this day's
    architectural edit — they're the same now as before: hash plus window
    comparison, with not a single model call. The parameters match in
    substance stend/stage-2.json, nodes dedup_hash ("Normalize + hash") and
    dedup_mech_if ("Exact duplicate in window?"); that file on disk doesn't
    yet contain the jev node (it describes an earlier state of the
    workflow) — the current configuration is confirmed by a direct query to
    the live n8n API, not by reading a stale local file.
---

# Configuration: Normalization and Exact Match

## Assertion

Two nodes handle the entire first, cheap step: one computes the normalized hash, the other compares it against the same contact's recent request. Neither calls a model.

## Visual

> **Node `Normalize + hash` (`Set`).** Takes the request's text, lowercases it, trims the edges, collapses repeated internal spaces: `normalized_hash = text.toLowerCase().trim().replace(/\s+/g, ' ')`. Alongside — the same calculation for the same contact's recent message.

> **Node `Exact duplicate in window?` (`IF`).** Condition: `normalized_hash` is strictly equal to the recent request's hash — a string comparison, both values already lowercased. Match → a repeat is found, caught for free, no record written. No match → the request moves on down the chain.

## Speaker notes

Here's what the first, cheap step actually looks like in the real chain — not a principle, but two real, configured nodes from the rig, on a real screenshot of the canvas.

The first node, `Normalize + hash`, is a `Set` — it doesn't call anything, it only computes values. We take the request's text and lowercase it: "When" and "when" become the same string after that. We trim the edges and collapse repeated internal spaces — an extra space shouldn't turn matching text into non-matching text. The same thing gets computed for the same contact's recent message, so there's something to compare against.

The second node, `Exact duplicate in window?`, is an `IF`, and it has one condition: the current request's normalized hash is strictly equal to the recent request's normalized hash. The strings match — we have a repeat in front of us, and the chain stops there: the answer already exists, no new record is needed, and the run itself still finishes successfully — worth remembering, we'll come back to this in a couple of screens. The strings don't match — meaning the cheap filter didn't give an unambiguous answer, and the request moves on to the meaning check.

Notice: neither of these two nodes calls a model. String comparison is pure mechanics, cheap and instant, and you can afford it on every single request without exception — this step's cost doesn't grow with how many requests arrive per hour. This is exactly the same cheap step as before today's architectural edit: only what comes after it changes.

One parameter deserves separate attention here, even though it isn't visible on this screen — the time window we search for a recent message from the same contact. Too short a window will miss a repeat if the person didn't write back immediately. Too long a window will start confusing different, genuinely new questions from the same person with a repeat of the same question. This is a parameter that has a cost on both sides, and we'll come back to it in the nuances.

How each of the two nodes is built on the inside — on the next screen: we'll open each one's settings panel and look at the real fields and the condition, not the canvas labels.
