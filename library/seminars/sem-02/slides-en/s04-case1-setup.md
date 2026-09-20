---
id: s04
type: case_study
assertion: "Accounting is drowning in supplier invoices — can this be automated?"
learning_goal: "Case 1 setup — a live, noisy quote from a product manager, two samples + a target 1C table"
learning_outcomes: [LO1]
references: []
visual:
  pattern: three_document_cards_plus_question
---

# Supplier documents

## Assertion

"Accounting is drowning in invoices — can this be automated?"

## Visual

Three cards in a row. The first two are sample supplier invoices, visually almost
identical in structure (a table: supplier, line items, amounts, dates). The third
is the target table in 1C with the same fields (Date / Invoice No. / Line item /
Amount), so the match in structure between source and target is visible at a
glance. On the right — a large-type question: "What would you propose?"

## Visual — quote

"Marina here, product manager for finance processes. Accounting is drowning:
three people are manually keying supplier invoices into 1C by hand, around 400 a
month, and by the end of the quarter it's a backlog with errors in the totals.
Attached two sample invoices from last week — the formats look about the same.
Can this be automated somehow? By the way, marketing has been running
YandexGPT over the API for product descriptions for six months now, there's
already a contract with them — maybe the same setup would work for us too.
Separately, we're migrating our mail to a new server, but that's not for you.
On timing — even a ballpark estimate by Friday would be great."

## Speaker notes

Read the product manager's quote in full, without shortening it — students should
pick out for themselves what's actually relevant to the task. Direct signals:
three people, around 400 invoices a month, all keyed by hand into 1C, backlog and
errors by the end of the quarter, two sample invoices where the formats "look
about the same." There's an indirect signal worth pulling out separately in
discussion: the company already has a contract and live experience running an
LLM over an API (marketing and YandexGPT) — that doesn't directly change the
architectural choice for this task, but it does close off the question "can we
even send data through an external API in the first place" before it comes up as
a hypothetical risk. The mail migration is a decoy fact: it sounds like an IT
detail about infrastructure, but it has nothing to do with parsing invoices. Show
both sample invoices on the slide and the third card — the target table in 1C
with the same fields (Date / Invoice No. / Line item / Amount) — so the audience
immediately sees the structural match between source and target. Ask the room:
what would you propose? Is AI even needed here, or can you get away without it?
Which fields specifically would you extract, and what, in your view, determines
how hard this task actually is? Who wants to go first? During the debrief, also
ask: which facts from the quote actually shaped your choice, and which didn't?
