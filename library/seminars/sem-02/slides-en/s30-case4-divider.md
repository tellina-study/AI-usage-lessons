---
id: s30
type: section_divider
assertion: "External API or local inference?"
learning_goal: "Visual divider — transition into case 4, the choice's topic instead of the case number"
learning_outcomes: [LO1]
references: []
visual:
  pattern: section_divider_plain
---

# External API or local inference?

## Assertion

The fourth choice: where the data is physically computed, not which model is better

## Visual

A large heading with the choice's topic on a neutral background + a
background illustration (the designer will pick one) + one comment line
with no spoiler.

## Speaker notes

The last, fourth question today: process the data through an external
cloud API, or on your own infrastructure. This is about where the data is
physically processed, not about which model gives a better-quality
answer — both models can produce a similar result, and the difference
turns out to be in exactly where the request goes and what happens to the
content at the other end. An external API gives you maximum power with no
investment in hardware; local inference gives you control over what
leaves the company's perimeter, and independence from someone else's
service. You have to weigh these sides not in the abstract, but against
the concrete data of a concrete task — there's no one-size-fits-all
answer here for different companies. As before, we'll start with the task
stated in one line by the client.
