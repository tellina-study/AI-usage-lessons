---
id: s19
type: research_evidence
duration_min: 3
assertion: "Rules in the prompt are requests, rules in code are laws; a textual gate catches an honest mistake but does not hold under pressure — the boundary for a mechanism runs where the action, the cost and the frequency have been named"
learning_goal: "The evidence and breakdown of case 1.2, part 2 (slide 1.2.4b) — the unconditional \"requests/laws\" formula and a full answer to the question \"can we get by without a hook today\", resting on the previous slide's sources, with no new numbers"
visual:
  pattern: research_and_answer_combined
  primary: "A gold plate with the formula \"rules in the prompt are requests, rules in code are laws\" — UNCONDITIONALLY, not as a reaction to a particular answer from the room. Below — a separate large block, \"Can we get by without a hook today\": a four-row table (what the text gives / what it does not give / where the boundary runs / where we are in the project) and an explicit conclusion on why it is worth knowing about a level we are not setting up today."
---

# Rules in the prompt are requests, rules in code are laws

## Assertion

Rules in the prompt are requests, rules in code are laws; a textual gate catches an honest mistake but does not hold under pressure — the boundary for a mechanism runs where the action, the cost and the frequency have been named.

## Visual

**The formula — UNCONDITIONALLY, not a reaction to a particular answer:**

> "Rules in the prompt are requests, rules in code are laws. What we wrote did not become a law just because we wrote it down proactively."

**Can we get by without a hook today — and why:**

| | |
|---|---|
| **What a textual gate gives you** | It catches the honest mistake: not "the agent worked around the check" but "nobody remembered it existed". Starting discipline at the price of one line — and in our case it worked exactly once out of three times: the time somebody mentioned it out loud |
| **What it does not give you** | It does not hold under pressure — a deadline, a rush, "the test is green, let's report it". TDAD: strengthening the same instruction with text raised regressions to 9.94%; Agent Scaffolding: the mechanism gives +20 pp, switching the model — ~1 pp. What works against pressure is not the wording but the mechanism |
| **Where the boundary runs** | A hook is needed when the cost of a violation is high and **predictable** — when you can name a concrete action, a concrete command and concrete damage. Until such an action has been named, it is too early to set up a mechanism: it costs time on every call and it checks a pattern match, not meaning |
| **Where we are in this project** | The action has been named: "done" without a manual check, twice in a row, and the cost is a sign-up request that fails to arrive in time for the demo. That is exactly the boundary. So today we are recording not "the text is enough" but "the text is enough up to exactly this point", and from there we move on to Seminar 5 |

> **Why know about the hook if we are not setting one up today.** So as not to mistake a textual gate for a solution. Someone who does not know about the next level strengthens the text — in caps, with a duplicate, with a third checklist file; TDAD measured where that leads. A hook is needed not "for reliability in general" but as an answer to a named action with a named cost: once you have named the action, the cost and the frequency — it is time; if you have not — the text is enough.

The second half of the criterion is about the "improvement" loop: "look at your code again" — never do that; "run a real check and fix what it shows" — always do that.

## Speaker notes

"The option "I'll rewrite it in caps" is exactly the path TDAD tested. Caps do not turn a request into a law. And none of the five options except "I'll hand it to a mechanism outside the text" solves the problem systematically — and we are not going there today, that is the next session. So the honest answer today is: we will still leave the gate as text, because that is better than nothing — but we will tell ourselves plainly that it is unreliable, even having been set up on the first day, and we will name the direction to go when it lets us down a second time.

And here is the formula that holds today's whole breakdown together: rules in the prompt are requests, rules in code are laws. The textual gate we have had since day one is a request, and that is fine for a basic practice. But calling things by their names is part of the job: what we wrote down as text did not become a law just because we wrote it down proactively.

Now a direct question worth answering here rather than leaving it hanging: can we get by without a hook today — and if we can, why are we talking about it at all.

We can get by today, and here is the basis for that. A textual gate catches the honest mistake: the case where the check was not worked around, people simply did not remember it. That is real work, and it costs one line. In our case you can see it literally: out of three times the gate worked once — the time it was mentioned out loud. What it does not do is hold under pressure. A deadline, a rush, "the test is green, let's report it" — and the line in the file stops existing. That has been measured too: strengthening text with text raised regressions to almost ten percent, while the mechanism gives twenty percentage points where switching the model gives one.

The boundary does not run along how important the rule is, but along whether you can name the specifics. A hook is needed when the cost of a violation is high and predictable: there is a concrete action, a concrete command, concrete damage. Until the action has been named, it is too early to set up a hook — it charges you on every call and it checks a pattern match, not meaning.

In our project the action has in fact been named: "done" without a manual check, twice in a row, and the cost is that the request never arrived while the client has a demo coming up. So the honest conclusion today is not "the text is enough" but "the text is enough up to exactly this point" — and from there the material of the next session begins.

And that gives the answer to the question "why do we need to know about the hook if we are not setting one up today". So as not to mistake a textual gate for a solution. A person who does not know about the next level strengthens the text: in caps, with a duplicate, with a third checklist — exactly the path TDAD measured. Knowing about the hook gives you the criterion by which you recognize the moment: name the action, the cost of a violation and the frequency. Named them — time to set up a hook. Have not named them — the text is enough.

And the second point of the breakdown, about "improvement": if it is "agent, look at your code again" — do not do that, the evidence is unambiguous. If it is "agent, open dist/index.html and submit the form by hand" — always do that."
