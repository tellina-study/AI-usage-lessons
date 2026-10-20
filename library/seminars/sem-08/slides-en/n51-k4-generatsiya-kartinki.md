---
id: n51
type: mechanism_node_graph
duration_min: 2.0
assertion: "The assembled chain puts text in the caption, not on the picture — marketing asked for text on top of the picture; getting that for real takes a separate generation step, and it has a cost and its own output format"
learning_goal: "New slide, owner's voice edit 2026-10-20 (issue #274), a letter-tail between n50 and n53. Names the honest gap: n50 assembles text as a caption to a photo fetched by link, not text baked into the image marketing asked for in the scene (n46). Closing that gap takes a separate generating model — an architectural estimate, not a node on the rig."
visual:
  pattern: mechanism_node_graph
  figure: k4-shema-generatsii-en.png
  primary: >
    A single-row, four-step diagram: notification text → specialized
    generating model → finished card (text already in the pixels) →
    sent to Telegram. Below it two blocks: the cost of generating one
    picture, with a source, an assumption, and an illustrative monthly
    estimate, and a note about re-encoding before Telegram.
  backup: >
    New slide at the direct request of the owner's voice edit
    (`qa/BRIEF-GOLOSOVAYA-PRAVKA-2026-10-20.md`, section "Case 4,"
    paragraph "Add a picture-generation diagram"). Honestly: this step
    is NOT built on Seminar 8's rig — neither a generating model nor a
    node that would receive its result exists in `stend/stage-4.json`
    (see the honest note in the `n50-k4-reshenie-sloy2.md` backup: the
    chain on the rig is three nodes, the text goes in as a caption to
    a photo fetched by link). This is an architectural estimate of the
    missing step, not a run. The cost — the public price of
    gpt-image-1.5 (OpenAI), 1024×1024, by quality tier: low $0.009 ·
    medium $0.034 · high $0.133 per picture (checked via WebSearch,
    October 2026, OpenAI pricing aggregators; gpt-image-1, this
    model's predecessor, is being discontinued on 2026-10-23 — which
    is why the current version was used). The choice of tier is a
    producer's assumption: a notification card doesn't need the
    highest generation precision, so the reference point is medium
    quality, ≈$0.034/picture; if the owner considers the assumption
    wrong, the figure is easily recalculated off the same table. The
    note about re-encoding is a direct brief requirement: generated
    pictures come at a large standard size, lightly compressed, and
    the `sendPhoto` 10,485,760-byte limit (measured on n50) hasn't
    gone anywhere.

    BASELINE/COUNT (2026-10-20 edit, issue #274): the ≈$0.034/picture
    price was given bare, with no tie to this case's real mailing
    volume — a structural gap (CLAUDE.md § "Baseline / Counterfactual
    Mandate": any measurable claim is required to have a baseline).
    The case scene (n46) and the neighboring slides
    (n45/n47/n48/n49/n50/n53/n54) do NOT explicitly state how many
    cards a day/month go out in the mailing — checked by direct
    reading of every Case 4 file, the frequency is nowhere. The only
    explicitly named volume for the training center in the whole deck
    is Case 1 (n06, the scene): "twenty requests a day"; this is the
    center's overall request flow, and the card in Case 4 replaces
    that very notification sent for every new request (n46: "instead
    of plain text — a card ... in the same notification") — that is,
    with a full switch to cards, the card volume equals the request
    volume, the same denominator, not invented separately.
    Calculation: ≈20 cards/day × ≈30 days ≈ 600 cards/month × $0.034 ≈
    $20.4/month. This is an ILLUSTRATIVE EXAMPLE OF A CALCULATION, NOT
    A MEASURED VOLUME — neither the mailing frequency nor the decision
    "switch 100% of notifications to cards" is explicitly fixed in the
    scene; if the real-world volume is smaller (not every request
    needs a card) or larger (several mailings a day), the sum is
    recalculated off the same formula. Added as a third line to the
    "Generation cost" callout on the figure
    `k4-shema-generatsii.png` (function `generatsiya()`,
    `rendered/make_figures_k4.py`) — the callout was widened from
    h=160 to h=185, the canvas CH stayed at 560 (the aspect ratio
    didn't drop below the `deck_kit.py: FIG_MIN_FILL`-safe threshold
    of ~2.84 — checked: 2.857).
---

# Generating the card: text inside the image

## Assertion

What we assembled on the previous screen is text as a caption to a photo fetched by link. Marketing asked for text on top of the picture — that is, inside the image itself — and that's a separate step.

## Visual

> Notification text and the "text on top of the picture" requirement → **specialized generating model** (text → image) → a finished card, text already baked into the pixels → sent to Telegram as a photo.

**Cost of generating one picture** — gpt-image-1.5 (OpenAI), 1024×1024: low quality $0.009 · medium $0.034 · high $0.133 per picture. Medium quality fits a notification — ≈$0.034 per card. **Illustrative, not a measured volume:** the case scene doesn't state the mailing frequency explicitly — if it's ≈20 cards a day, the same request flow as Case 1 (n06), that comes to ≈600 cards a month and ≈$20.4 a month.

**Note.** Pictures out of generating models come at a large standard size, lightly compressed — before sending to Telegram they need re-encoding into a lighter format, the same `sendPhoto` 10 MB limit we already measured.

## Speaker notes

Let's pause for a second on what we actually assembled on the previous screen, and compare it with what marketing asked for at the start of the case.

Marketing asked for a card: text on top of a picture, in one image. The chain we configured does something else — it fetches a ready-made picture by its link and puts the notification text next to it, as a caption, a separate text field of the Telegram message. This works, Telegram really will show the text next to the photo, but the text isn't inside the image — that's not the same thing as "a card with text on top of the picture," and it's worth saying so honestly rather than papering over the difference in silence.

To get a real card — an image with the text physically baked into the pixels — you need a separate step, and the ordinary "fetch a file by link" node won't do it: it knows how to download a ready-made picture, not how to draw on one. You need a specialized generating model: on the input, the notification text and the task "turn this text into a readable image"; on the output, a finished file with the text already inside it.

This step has a cost, and it isn't zero. As a reference point, take the public price of a comparable model — OpenAI's gpt-image-1.5: generating one picture at 1024 by 1024 points runs from under a cent at low quality to thirteen cents at high quality, depending on how much precision and detail you choose. For a short text notification on a card, the highest precision is unlikely to be needed — a reasonable reference point here is about three and a half cents a picture, medium quality. This isn't a measurement on our own rig — there's no such step on the rig — but an honest estimate against someone else's, but current and checkable, pricing.

Three and a half cents for one card doesn't say anything on its own until it's tied to a volume — and this case's scene doesn't state the mailing frequency explicitly. The volume shouldn't be invented out of thin air: the card replaces the very notification sent for every new request, and we know that flow from Case 1 — twenty requests a day. If the whole flow switches to cards, that comes out to about six hundred cards a month and about twenty dollars a month. This is an illustrative example of a calculation, not a measured volume: neither the mailing frequency nor a full switch to cards is explicitly fixed in the scene. But with a base now in place, you can see: for the training center, this isn't a price that argues against the solution, and it isn't zero either, the kind of thing you can skip counting.

And one last thing worth keeping in mind even without building this step: generating models usually hand back a file at a large standard size that isn't compressed very hard. That means the finished card can't be sent to Telegram as-is — it needs re-encoding into a lighter format ahead of time, by the same logic we already saw on the previous screen with the 10,485,760-byte limit on photos. Generation doesn't remove the size check — it adds it again, at a new point in the chain.
