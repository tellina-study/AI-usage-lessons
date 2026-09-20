---
id: s11
type: case_study
assertion: "An AI assistant for support-desk operators — response suggestions, similar-ticket search"
learning_goal: "Case 2 setup — a live, noisy quote; operators live inside the helpdesk all day"
learning_outcomes: [LO1]
references: []
visual:
  pattern: single_card_plus_question
---

# Support assistant

## Assertion

"An AI assistant for support-desk operators — response suggestions, similar-ticket search"

## Visual

A card with a mockup of a support-desk operator's screen: a ticket list, a
customer-reply window. On the right — a question: "Where should this assistant
live?"

## Visual — quote

"Simple idea: an AI assistant for operators — response suggestions on tickets,
search for similar past cases. There are 12 operators on the line, throughput is
around 300 tickets a day, peak from 10:00 to 13:00. Some of the same operators
also answer customers on Telegram in parallel — there's a separate chat channel
for that, about 4 people keep it open all the time. Everyone logs in through
corporate SSO, so authorization shouldn't be an issue. Separately, we're
currently refreshing the laptop fleet in support, but that's not for you. It
would be great to be able to show something at the quarterly review."

## Speaker notes

Read the whole quote out. Direct signals: the idea of response suggestions and
similar-case search, 12 operators on the line, around 300 tickets a day, peak
from 10:00 to 13:00. There's an indirect signal worth explicitly pulling out in
discussion: part of the operator team already works in Telegram in parallel —
that's a second, separate integration point for the assistant that the client
didn't ask about directly, but it really exists and could turn out to matter as
much as the helpdesk itself. Corporate SSO is also an indirect plus: a single
login reduces the cost of integration if the assistant ends up as a separate
window. The laptop-fleet refresh is a decoy fact: it sounds like an IT detail
about support infrastructure, but it has nothing to do with the assistant's
architecture. The slide shows a support-desk operator's screen: a ticket list,
a customer-reply window. Operators spend the entire workday in the same
helpdesk-system interface — something like Zendesk or Jira Service
Management — opening ticket after ticket, switching between cases dozens of
times a shift. Ask the room: where should this assistant live? What would you
propose — a separate window, a suggestion built right into the interface,
something else? And just as important, why that and not something else? During
the debrief, ask: which facts from the quote actually shaped your choice, and
which didn't?
