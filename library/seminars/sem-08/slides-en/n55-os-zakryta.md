---
id: n55
type: keystone_axis
duration_min: 2.5
assertion: "The four rows of the axis are filled in, and they were filled in by the screens, not by a story; the session's question comes back to the room verbatim"
learning_goal: "Closing of the session's axis. The pairs sit side by side; the session's question returns verbatim. Case names match SETKA-KEYSOV-S8.md: 'Notifications', 'Duplicate check', 'Refund approval', 'Card in Telegram'."
visual:
  pattern: keystone_axis
  primary: >
    The same table that opened the session, now with the right column
    filled in. Below it — the session's question returned, verbatim, in a
    gold line.
  backup: >
    The right column quotes the "Closes the axis row" paragraphs from each
    section of SETKA-KEYSOV-S8.md / SETKA-KEYSOV-S8-part2.md (Cases 1-4).
    The left column and the session's question are verbatim from the
    "Session axis" section of the same file; the case names are checked
    against the renaming table in §1 of the proektirovanie-keysa-i-voprosa.md
    canon.

    EN track note (this file, issue #172/#274): case names in the right
    column ("Notifications" / "Duplicate check" / "Refund approval" /
    "Card in Telegram") are this translator's own direct rendering of
    the four Russian case names used in the RU slide (slides/n55-os-zakryta.md,
    row by row), built from terms already locked in glossary.en.yaml
    (deduplication/duplicate, refund, approve/approval, card). glossary.en.yaml
    does not lock a dedicated case-name list — reconciled 2026-10-20
    (issue #274, consistency-checker audit) against the case-divider slide
    (n45-k4-divider.md, title "Card in Telegram"): the fourth case name now
    matches it exactly.
---

# Four rows of the axis: what they turned out to be

## Assertion

We saw every right-hand cell on screen — we did not just hear it from me.

## Visual

| Looks reliable | Turned out to be |
|---|---|
| the message reached the coordinator, the chain got shorter and cheaper without an LLM | the LLM here was just an extra step — a template did the same job, with no model and no risk of hallucination (**"Notifications"**) |
| a repeat request about the same question came in — handled as new | without a duplicate check, every repeat request restarts the chain from zero; neither an exact match nor word-level similarity catches this fully — a rephrasing needs a meaning-based check (**"Duplicate check"**) |
| the prompt says "don't refund more than amount X" | the decision stayed probabilistic: the model worked around the rule in a measured share of runs, right at the edge of the condition; an algorithmic gate — never (**"Refund approval"**, confirmed at company scale — Zillow) |
| the image got assembled and sent to Telegram | only as long as it fits the limit — a large file either arrives incomplete or doesn't arrive at all, while the run still shows green (**"Card in Telegram"**) |

> **Where in the chain does the model decide, and where must code — and what stays silent when that boundary is never named explicitly?**

## Speaker notes

Back to the table we started with. The right column isn't empty anymore, and it wasn't my words that filled it — it was the screens we just watched.

First row. The message reached the coordinator, the chain got shorter and cheaper without an LLM — that's how the decision looked after the first case. What it turned out to be: the LLM node for assembling the notification was just an extra step — a template did the same job, with no model, no variability, and no risk that the text would say something the request never contained at all.

Second row. A request about the same question came in again, and it got handled as new — until we put in a duplicate check. What it turned out to be: without that check, every repeat request restarts the whole chain from zero, and neither an exact text match nor similarity by shared words catches a rephrasing in full — we counted it ourselves on real text: zero shared words between two phrasings of the same question. A meaning-based check was needed, and only on whatever the cheap filter didn't already screen out.

Third row, the most expensive one in terms of proof. The prompt said "don't refund more than amount X" — and the decision was considered reliable for a month, because there were no complaints. What it turned out to be: the decision stayed probabilistic, and the model worked around the rule in a measured share of runs — right at the edge of the condition, not by chance. The algorithmic gate — a condition in code — didn't get it wrong once in the same experiment. And after that we saw the same shape of failure at the scale of an entire company: Zillow lost a quarter of its workforce and hundreds of millions of dollars on that same ungated threshold, which cost us one awkward conversation with a client.

Fourth row. The image got assembled and sent to Telegram — it looked like a completed action. What it turned out to be: only as long as the file fits the limit. A large file either arrives incomplete or doesn't arrive at all, while the run still shows green — the same contract that broke on text in the first case, only here it breaks on size and format.

All four rows are about the same thing: where in the chain the model makes the decision, and where code must, and what stays silent when that boundary is never named explicitly. The line between "it works" and "you can stand behind it" today ran not through one node, but through every single step of the chain.
