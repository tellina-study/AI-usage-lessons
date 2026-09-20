---
id: s07
type: case_study
assertion: "Personal data in the logs — what's the fastest, cheapest way to clean it up?"
learning_goal: "Quickfire setup — a question about speed and cost, no hint at where the solution boundary sits"
learning_outcomes: [LO1]
references: []
visual:
  pattern: single_card_plus_question
---

# Personal data in the logs

## Assertion

"Personal data in the logs — what's the fastest, cheapest way to clean it up?"

## Visual

One card with a sample log line where a phone number, an email, and a phrase
like "pass this to Ivan in accounting" show up mixed together. On the right — a
question: "What's the fastest, cheapest way to clean this up?"

## Visual — quote

"The performance contractor is asking for a quarter's worth of prod logs — they
can't find the load spikes without them. I pulled around 40 GB, the archive is
already on the server. Inside, mixed in, there are phone numbers, customer
emails, and one instance of the phrase 'pass this to Ivan in accounting' — it
got logged from a request body. The logs are already in standard line-delimited
JSON, easy to parse the structure. The contractor needs timings and error codes,
not people's data. Separately, we're testing a new VPN solution for remote
access, but that's not related to the logs. They want the archive by Friday."

## Speaker notes

Read the colleague's message — they're preparing the logs for the contractor.
Direct signals: 40 GB of logs for the quarter, Friday deadline, the contractor
needs request structure/timings/errors but not specific people's data, and
inside the logs there's a mix of a phone number, an email, and a phrase like
"pass this to Ivan in accounting." An indirect signal worth pulling out
separately: the logs are already line-delimited JSON — meaning the field
boundaries and request structure are already deterministic, so you only need to
search for personal data inside the values, not parse the log format itself
from scratch. The VPN testing is a decoy fact: it sounds like an adjacent
data-security topic, but it has no bearing on how you'd scrub personal data out
of an already-exported archive. The sample log line on the slide shows exactly
that mix: a phone number, an email address, a name inside free text. Ask the
room: what's the fastest, cheapest way to clean up these 40 gigabytes by
Friday? Who has an opinion on what you'd try first? During the debrief, ask:
which facts from the quote actually shaped your choice, and which didn't?
