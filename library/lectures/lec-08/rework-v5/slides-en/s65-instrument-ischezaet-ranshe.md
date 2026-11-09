---
id: s65
local_id: "s65"
section: "3. Moving Image"
type: analitika
title: "The Tool Disappears Faster Than Training the Team Pays Off"
assertion: "Preview API access to one flagship model was shut down on 10/22/2026; thirteen months before that, another flagship went down the same path — its app shut down 04/26/2026, API access 09/24/2026 — with a major studio announcing a three-year, billion-dollar licensing deal four months before that shutdown, a deal that never closed; a feature film announced on the baseline of 'under $30 million and nine months against the usual $100–200 million and three years' was left without a technology partner and slipped by a year"
source: "a provider's documentation page, read 10/27/2026; reports on Sora's shutdown"
chapter_ref: "chapter-part2d.md §3.9"
media: ""
media_needed: "visual content — a lifeline of the tool from its first examples to its shutdown; there's no such thing as an authentic photograph of a software service shutting down — a screenshot of the documentation page announcing the shutdown would be the most honest candidate, but there's nothing to reproduce a provider's interface with as a slide in this deck — the page is available at the address given in the notes"
scheme:
  arrows: true
  rows:
    - {label: "2024", steps: ["February: first examples shown", "December: launch for subscribers"]}
    - {label: "2025", steps: ["Sept 30: 2nd generation + app", "Dec 11: $1B / 3yr deal — against 3 unions"]}
    - {label: "2026", steps: ["Mar 24: the deal falls through", "Apr 26/Sept 24: app, access both shut down"]}
blocks:
  - {label: "Two flagships", value: "within 13 months", note: "the second shut down 10/22/2026"}
  - {label: "A demo decision", value: "$800M of expansion halted", note: "a producer's call, on the first examples, 2024"}
  - {label: "Economics", value: "$1M/day, <500K users", note: "peak ~1M; not free of charge", key: true}
  - {label: "The project", value: "9 mo. instead of 3 yr — slipped a year", note: "no partner, Q1 2027"}
itog:
  yarlyk: "The matching answer"
  text: "a successor is named, a migration path is given"
timing_min: 1.5
in_bucket: true
status: собран
---

## Visible slide text


## Speaker notes

This cost layer has one price, and it's a production one: it's not in any price list, but it belongs in the budget.

One provider's documentation page, read on 10/27/2026, states: preview access to the flagship video model in the API was shut down on 10/22/2026, with developers directed to migrate to another model. Thirteen months earlier, another flagship went down the same path: its app was shut down 04/26/2026, API access 09/24/2026.

The second one's cycle can be traced in full, and it's worth knowing. February 2024: first examples shown, and producer Tyler Perry halts an $800 million studio expansion after watching them. December 2024: public launch for subscribers. September 30, 2025: second generation and an app; within a week, tools for removing the visible watermark spread across the net. December 11, 2025: a major studio invests a billion dollars under a three-year licensing agreement, more than 200 characters inside the service; three unions oppose it. March 24, 2026: discontinuation announced, the studio deal never closes. April 26 and September 24, 2026: the app is shut down, then API access.

Causes, per reports: a shortage of compute, costs, a pivot toward enterprise products. Numbers worth stating: peak users at about a million, then under five hundred thousand; operating cost estimated at about a million dollars a day. Divide one by the other — a dollar per user per day. Video generation was never free for a single second; it was simply not the user who paid.

Three conclusions, and all three are engineering ones. First: halting an $800-million construction project was done on something shown rather than measured — this is the cost of a decision made on a demo reel, and it's named by a single figure. Second: two of this lecture's headline cases are built on a tool that has shut down. A feature film announced on the baseline of "under $30 million and nine months against the usual $100–200 million and three years" was left without a technology partner after the service shut down, missed its announced premiere, and slipped to the first quarter of 2027. Nine months of production against three years is worth nothing if the tool disappeared in month eight. Third: dependence on someone else's service is a project risk, and it doesn't belong in the category of organizational trivia.

The matching working answer, without which this section would read as an accusation. Both models migrated, and that cannot be called disappearance: a successor is named right on the same documentation page, a migration path is given, and the enterprise track is kept separate from the preview one for exactly the purpose of keeping a production dependency from breaking along with an experimental interface. In other words, the provider did exactly what it promised under the terms of preview access, and the complaint belongs to whoever built a production pipeline on a preview interface.

Three rules for planning: each one follows from the paragraphs above, and none requires believing anyone's forecast.

First: a tool's expected lifespan belongs in the project budget. If a production cycle runs longer than a year while the tool lives on a preview interface, the probability of a replacement happening mid-cycle has to be assessed the same way you'd assess the risk of losing a key contractor. Nine months of production is exactly the length of time in which one flagship managed to shut down.

Second: portability matters more than demo-day quality. A pipeline in which the model is swappable — shot descriptions, reference frames, and the assembly order kept separate from any one provider — survives a shutdown; a pipeline tuned to one model's quirks shuts down along with it. In practice this means keeping prompts, references, and assembly rules in your own format, not inside a project living inside someone else's service.

Third: training a team amortizes more slowly than versions change. This is exactly the accounting put in the title. While a team is still learning one model's behavior, two new ones ship and one old one gets shut down; so the investment has to go into what carries over between models — specification, assembly, sign-off — while treating any one provider's particular settings as a consumable.
