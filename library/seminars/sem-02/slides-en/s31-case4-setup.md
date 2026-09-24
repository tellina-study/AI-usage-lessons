---
id: s31
type: case_study
assertion: "A call card: need, objections, agreements — how do you build that?"
learning_goal: "Setting up case 4 — a live line with noise"
learning_outcomes: [LO1]
references: []
visual:
  pattern: single_card_plus_question
---

# Sales calls

## Assertion

"A call card: need, objections, agreements — how do you build that?"

## Visual

A card: a call-recording icon → arrow → a mockup of a summary card
(need / objections / agreements). On the right — the question: "How do you
build that?"

## Visual — quote

"I want a card for every manager's call: need, objections, agreements.
Managers rewind the recording, hunting for where they left off last time.
There are 8 managers in the department, 15-20 calls a day each, the phone
system writes the conversation to mp3 and drops the file into the cloud
by itself — no need to pull it out manually. Our CRM is Bitrix24, open
REST API. The department's analysts already use a cloud AI over the API
for quarterly report drafts. The CRM, by the way, also needs cleaning up
from duplicate contacts at some point, but that's a separate headache."

## Speaker notes

Read the sales manager's line out in full. The direct signal, not
particularly highlighted: they want a summary card per call (need /
objections / agreements), 8 managers, 15-20 calls a day each. Indirect
signals worth pulling out explicitly: the phone system already drops
recordings into the cloud on its own — no need to solve the extraction
problem separately; the CRM is Bitrix24 with an open REST API — the card
can be written straight into the CRM with no custom integration; and the
analysts' existing habit of using a cloud AI over an API is an indirect
signal that the organization is already psychologically ready for an
external API, and this won't be a new class of risk for them per se
(though call data isn't the same thing as report drafts — we'll come back
to that question later). Duplicate contacts in the CRM are a noise
twin — also about the CRM, but purely about data quality, not about the
extraction architecture. On input — a call recording, an ordinary
free-form conversation between a manager and a client, with no structure
at all, with interruptions, pauses, digressions from the topic, sometimes
with background noise. Question to the room: how do you build this? What
would you propose, and why exactly that? Who'll start? When you break it
down, ask: which facts in the line affected your choice, and which didn't?
