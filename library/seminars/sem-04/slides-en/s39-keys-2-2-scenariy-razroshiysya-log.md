---
id: s39
type: problem_scenario
duration_min: 1.5
assertion: "Month four: two hundred records in DECISIONS.md, two of them about the same question — and neither one links to the other"
learning_goal: "The scenario of case 2.2 — the state of the decision log in month four and what came of it. NO question, NO cards, NO statement of the solution"
visual:
  pattern: scenario_pain
  primary: "A large scenario block: month four, two hundred records, two related records (September 26 and November 28) at opposite ends of the file with no links to each other. At the bottom — a state line: in a flat log, both records can only be found by reading linearly. Note: the example is illustrative."
---

# Month four: two records about the same thing, no links

## Assertion

Month four: two hundred records in `DECISIONS.md`, two of them about the same question — and neither one links to the other.

## Visual

The scenario:

> Month four of work on `signup-landing`. The form started getting spam; by now there is a second developer on the team, someone who was not around for the earlier discussions, and they ask the agent to put protection in place. The agent reads `DECISIONS.md` — two hundred records — and answers from the record of September 26: "no third-party widgets in the form". So a captcha is out, and the agent proposes reopening the question from scratch.
>
> The record of November 28 — "anti-spam is a honeypot field, no captcha" — sits a hundred and fifty records further down, near the end of the file, and settles exactly this case. Neither does the September record link to the November one, nor the November one to the September one.

A state line at the bottom, in a gold frame:

> "Both records sit in the same file. In a flat append-only log, the only way to find both is to read all two hundred linearly."

Note: "The example is illustrative — no real 200-record `DECISIONS.md` has been captured."

## Speaker notes

"The previous case ended at a boundary: a flat file stops coping not when it gets big, but when it has accumulated links that a linear log has no room for. Here is that same boundary played out.

Month four of work on the repository. The form started getting spam. By now there is a second person on the team, someone who was not around for the earlier discussions, and they ask the agent to put protection in place. The agent honestly reads the decision log — there are two hundred records in it by now — and answers from the record of September twenty-sixth: no third-party widgets in the form. So a captcha is out, and it proposes reopening the question from scratch.

But on November twenty-eighth a second record appeared in the log: anti-spam is a honeypot field, no captcha. It settles exactly this case, and it sits a hundred and fifty records further down, near the end of the file. Neither of the two links to the other.

Both records are in the same file. There is only one way to find both in a flat log — read all two hundred in a row."
