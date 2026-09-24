---
id: s25
type: case_study
assertion: "Half the action items from May's minutes still have no owner"
learning_goal: "Action-items fact — a line with no conclusions, only a fact and a question"
learning_outcomes: [LO1]
references: []
visual:
  pattern: fact_card_plus_question
---

# Meeting minutes

## Assertion

"We still copy action items from the minutes into the task tracker by hand..."

## Visual

A quote card. Next to it — a task-tracker icon with manual task entry. On
the right — the question: "Does this change the architecture again?"

## Visual — quote

"Thanks for the search over the minutes, it genuinely saves time before
retros. But here's something I noticed: we still copy action items from
the minutes into YouTrack by hand — open the minutes, read what the
system found, create cards, fill in the owner and the deadline. YouTrack,
I checked, has an open REST API, you can create a task with a single
call. I went through May's minutes yesterday evening — roughly half the
action items are just sitting there with no owner, nobody's gotten around
to moving them over. Separately, I wanted to ask about tag colors in the
tracker, but that's probably a question for the tool admin."

## Speaker notes

Read the line out in full. The direct signal, not particularly
highlighted: the system already finds the action items in the minutes,
but they're still moved into the task tracker manually, one by one, and
half of May's action items are still sitting without an owner. The
indirect signal here is the key one for this step of the breakdown, spell
it out explicitly: the fact that YouTrack has an open REST API is exactly
what makes the next architectural step — an agent calling the tracker's
API — technically cheap rather than hypothetical. Without an open API
you'd have to hack something together through export-import or write an
integration from scratch. Tag colors in the tracker are a noise twin —
also about the task tracker, but a purely cosmetic question, no bearing on
the architecture. Question to the room: does this change the architecture
again? What's new here compared to the search over the base we were just
discussing a minute ago? Who's changed their mind — and more importantly
than the fact of changing your mind, why exactly did this detail make you
reconsider the architecture rather than just tack one more step onto the
previous solution? When you break it down, ask: which facts in the line
affected your choice, and which didn't?
