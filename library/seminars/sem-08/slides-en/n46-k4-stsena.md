---
id: n46
type: problem_scenario
duration_min: 2.0
assertion: "Marketing asked for a card with a picture instead of plain text; we put a chain together, it worked on test pictures, and on the first real one the result vanished quietly during a formally successful run; closes with an explicit list of requirements the solution has to meet"
learning_goal: "Case 4 scene, canon §1 form: need first, version 1 as the natural first attempt, the practice finding as the cost paragraph, and now a new footer — two classes of concrete requirement, moved here from the former separate slide n48 as part of stating what must be met, not part of why the split is right."
visual:
  pattern: problem_scenario
  primary: >
    A callout with marketing's need, below it a numbered timeline of
    assembly and the first real run, a paragraph on the cost of the quiet
    loss, and a new footer — a two-class requirements table the solution
    has to meet. Still no table in the scene's main body — the table lives
    only in the footer.
  backup: >
    The scene's content is a direct unfolding of "Need" + "Version 1" +
    "What the practice showed" from SETKA-KEYSOV-S8-part2.md, section
    "Card in Telegram," folded into the scene's form (callout → timeline
    → cost). The footer with the two requirement classes was moved here
    by the owner's 2026-10-20 edit (issue #274) from the former separate
    slide n48 (`slides/n48-k4-razbor.md` before the move) — the wording
    is the same, the framing shifted from "breakdown" to "statement
    requirement" (canon `proektirovanie-keysa-i-voprosa.md` §1: the
    statement is formulated as a need, not as a review of an
    already-built solution). Slide n48 wasn't deleted — it was
    repurposed into a breakdown of the answer to question n47 and a
    bridge to implementation (layers n49/n50), without duplicating this
    table — see its own backup.
---

# Marketing's need and the first version

## Assertion

Marketing asked for a card with a picture instead of plain text. We put a chain together, and it worked fine on ordinary pictures.

## Visual

> The training center already sends the coordinator a text notification about a new request (Case "Notifications"). Marketing asks: instead of plain text — a card, text over a picture, in the same channel.

1. We put a chain together: the notification text is prepared with the same substitution trick as in "Notifications"; the next step fetches the picture by its link; the last step sends the picture to Telegram with that text as the caption.
2. On test pictures the chain works without a hitch: the card gets assembled and sent, the coordinator sees it in Telegram.
3. Marketing sends the first real card for an actual mailing — a high-resolution scan straight from a phone, noticeably bigger than the test pictures.
4. The run finishes successfully: the n8n log is green, the sending node got a positive response from the Telegram API. The coordinator's Telegram has no card — either it never arrived at all, or it arrived cut off.

> **The cost you don't see in the log.** This isn't a node failing and it isn't a call error — we already know how to catch those. This is a quiet loss of the result during a formally successful run, and until now we've had no reason to check binary data by anything other than the bare fact that it got assembled.

**What has to be true before a card counts as ready.** Two classes of requirement, different in kind:

| Requirement class | What gets checked |
|---|---|
| **Mechanical** | file size, format, resolution — the file has measurable, enumerable properties |
| **Semantic / content-based** | the picture actually shows what's needed — not a broken placeholder file, not someone else's image, not an empty frame |

## Speaker notes

This case's scene doesn't open with a complaint, but with a request — and that's an ordinary story of extending an already-working process.

The training center already sends the coordinator a text notification about a new multi-topic request — the same substitution-into-a-ready-form trick we put together in the "Notifications" case. Marketing looks at that plain message and asks: instead of text, send a card — an image with text over it, in the same channel, in the same notification.

We put a chain together the same way anyone assembles an extension of an already-working process. The text is prepared by the same substitution node as before. The next step fetches the picture by its link and gets it as binary data, not as a text field. The last step sends that picture to Telegram, with the notification text going along as its caption.

On test pictures everything works without a single hitch: the card gets assembled, it's sent, the coordinator sees it in Telegram in exactly the same place where he used to see text. The chain was put into production on that basis — it passed the check we knew how to run.

And then marketing sent the first real card for an actual mailing — not a test image, but a high-resolution scan straight from a phone, noticeably larger than the files the chain was checked on. The run that processed it finished the same way every previous one had: the n8n log is green, the sending node got a positive response from the Telegram API, nobody saw any error at all.

And the coordinator's Telegram had no card — either the message never arrived, or it arrived cut off, missing part of the image.

Here's the real cost of this scene. This isn't a node failing: we've known how to catch failures since last session, with a retry and a branch. This is a quiet loss of the result exactly where everything formal says "success" — because until now we've had no reason to check binary data by anything beyond the bare fact that it got assembled at all.

Which means that before calling this a solution, we need to explicitly name what the card is obligated to meet — not after the fact, looking at a failure, but ahead of time, as a requirement. And there isn't one requirement here, there are two, and they're different in kind. The first is mechanical: a file has a size, a format, a resolution, and these are numbers and enumerable values you can compare against a condition. The second is semantic, or content-based: does the picture actually show what it's supposed to show, rather than a broken placeholder, someone else's image, or an empty frame. The difference isn't a formality — it directly decides which tool is even capable of checking a requirement like that, and that's exactly the question that comes up next.
