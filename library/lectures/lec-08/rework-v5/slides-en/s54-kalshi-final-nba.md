---
id: s54
local_id: "s54"
section: "3. Moving Image"
type: analitika
title: "Breakdown: Kalshi, NBA Finals, June 2025"
grafa: "a — both classical modes are counted in the same unit as the model"
assertion: "An ad for the National Basketball Association Finals broadcast was made by one person in two to three days: 300–400 generations down to 15 usable clips, a 95 percent cost reduction against an ordinary ad in the same slot, meaning about two thousand dollars against forty thousand; the failure rate was 96 percent, and it is this, not the price of a single generation, that explains where the savings came from"
source: "NPR, 06/23/2025; the work's author — PJ Accetturo"
chapter_ref: "chapter-part2c.md §3.4"
media: "assets/screenshots/s54-kalshi-ad-frame-portret.png"
media_note: "a frame from the ad itself, published in NPR's own piece about this work; obtained at the first acquisition tier. Provenance — images-log.md"
blocks_per_row: 3
voronka:
  vhod: {value: "300–400", text: "generations reviewed by one person"}
  vyhod: {value: "15", text: "usable clips"}
  yarusy:
    - {head: "Generation", text: "seconds and cents per attempt"}
    - {head: "Selection — the bottleneck", text: "character consistency checks; a 96% failure rate"}
blocks:
  - {label: "Classical versus the model, in money", value: "≈$40,000 · 10,000 ₽/sec  →  $2,000 · 4–10 ₽/sec", note: "a 95% reduction against the same slot's budget — the NBA Finals, not the Super Bowl", key: true}
timing_min: 1.3
in_bucket: false
status: собран
---

## Visible slide text


## Speaker notes

Here the axis of the whole lecture shows up with no admixture, and the numbers are named by the work's own author.

A detail that must not be lost: this is the National Basketball Association Finals. The National Football League does not accept prediction-market advertising; the error migrates from retelling to retelling, and the student will be the first to check it.

The cost of both kinds of error is given as a ratio: 300–400 generations down to 15 usable clips. The cost of a failed attempt is seconds of compute and cents. The cost of a missed successful one is the whole ad. This gap is exactly what the case is about.

The first classical mode is shooting an ad of the same slot's complexity. The author counted it relatively: a 95 percent cost reduction against an ordinary ad in that slot. At two thousand dollars for the model, that works out to about forty thousand dollars for the classical budget. The second classical mode is a Russian baseline band for the same work, so it can be counted in its own units: a basic ad runs 300,000–800,000 rubles with a crew of 3–5; a mid-tier one, 800,000–2,500,000; a premium one, 2,500,000–10,000,000, with a crew of 10–20. Converting to a common unit: 300,000 rubles for a thirty-second ad is 10,000 rubles per second of finished airtime, against 4–10 rubles per second of generation, at an exchange rate of around 80 rubles to the dollar, to be checked on the day you read this. The gap runs from a thousand to twenty-five hundred times — the same order of magnitude as with the image and with voice.

The dishonesty of this comparison is named right there. 300,000 rubles buys an idea, a script, a storyboard, a location, lighting, music rights, rights to faces on screen, editing, and delivery to the client. Ten cents buys one attempt at one shot. The exact formulation: generation zeroes out the cost of the shot and leaves the cost of the ad untouched. All the rest of the breakdown's content is about what fills that gap.

How this works. The input is text descriptions of the shots, and a breakdown with the published prompts is publicly available; the output is video clips that the ad is cut together from. The product's name is Google Veo 3. What it was trained on is not disclosed. The human threshold and action: one person reviews 300–400 generations and selects 15; that is the entire team.

What exactly the person does on the input side is worth breaking down separately. The prompts for this work have been published, and they're built like a director's shot list: shot type, camera movement, lighting, character behavior, emotion, duration. The model's input functions as a structured specification, closer to a technical brief than to a search-engine query. The skill that pays off here is called shot specification in the trade, and it carries over between models better than knowledge of any one specific interface.

The tool's durability: the Veo 3.1 Preview version was shut down in the API on 10/22/2026, with developers directed to migrate to its successor. This is the second flagship shut down inside thirteen months, and it is covered in the section's cost layer.

Those two or three days are worth picturing concretely: the description "one person made the ad in two days" drops out the actual content of the work. The person writes the shot description, starts the generation, waits, watches, rejects it, revises the description, runs it again. Fifteen clips that made it in came out of three to four hundred such cycles. In between is a check: does the character match the previous shot, is it the same light, the same camera. This is the work of an editor and a director at once, done at the pace the generation queue sets.

What moved. The profession of selection moved. The cheapness here comes from a failed attempt costing almost nothing: a ratio of 400 to 15 means a 96 percent failure rate. Engineering-wise this matters more than the two thousand dollars, because it carries over to any task: the savings equal the price of an attempt divided by the usable share.

The other half of this pair is the short film "Air Head," April 2024. Its own creators' estimate: a ratio of 300 to 1 between source material and what made the final cut. The baseline without which this number doesn't read: in classical documentary, the ratio of footage shot to footage released runs in the tens-to-one; in scripted advertising, about ten-to-one. That means the model didn't invent selection — it increased it by an order to an order-and-a-half against the mode it imitates. And there's a line item in the expenses that appears in no price list anywhere: the film's protagonist has a balloon for a head, and the model kept insisting on drawing a face onto the balloon, which had to be cleaned out by hand, frame by frame.
