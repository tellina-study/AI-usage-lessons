---
id: s33
type: case_study
assertion: "No GPU server and no budget. We need five fields in the CRM, not a conversation"
learning_goal: "Intro 2 — two lines with background noise, no conclusions"
learning_outcomes: [LO1]
references: []
visual:
  pattern: two_quote_cards_plus_question
---

# Sales calls

## Assertion

"We don't have a GPU server, and no budget for one this year" / "I don't need a conversation — I need five fields in the CRM"

## Visual

Two quote cards side by side: CTO — "We don't have a GPU server, and no
budget for one this year." Sales manager — "I don't need a conversation —
I need five fields in the CRM." On the right — the question: "Does this
change the architecture again?"

## Visual — quote (CTO)

"This came up on the budget call. Let me flag an infrastructure
constraint: we don't have a GPU server, and there's no budget for one this
year either — the quarter's priorities are locked in, and they went to
migrating to a new email system and refreshing the laptop fleet in
support. If the model is heavy, we'll have to go through a cloud API, but
that comes with its own data questions, which we've already discussed. Maybe
next year we'll come back to the conversation about our own server."

## Visual — quote (sales manager)

"What I need for my work is simple: five fields in the CRM per call —
need, objections, agreements, next step, deal-probability estimate. Not a
full retelling of the conversation, not a tone-of-voice analysis. Just
these five fields filling themselves in right inside Bitrix24, so I can
see them in my department report, which I currently put together by hand
from the team's notes every Monday."

## Speaker notes

Read both lines out one after another, without highlighting the key
words with your intonation. The direct signals are dissolved in the
context: the CTO says there's no GPU server and no budget for one this
year, meaning heavy local infrastructure for a heavy model is off the
table; the sales manager needs exactly five specific fields in the CRM,
not a conversation and not tone-of-voice analysis. It's worth pulling out
the indirect signal from the sales manager's line: the fields need to be
written straight into Bitrix24 — that's the same CRM with the open API
we already mentioned in the setup, which means the solution's output has
nowhere new to be plugged in, the integration point is already known.
The email migration and laptop refresh are noise twins — both about this
quarter's IT budget, but not about model inference. Question to the
room: does this change the architecture again? What from earlier should
now be reconsidered, and how do these two lines together, not
separately, change the picture? When you break it down, ask: which facts
in the lines affected your choice, and which didn't?
