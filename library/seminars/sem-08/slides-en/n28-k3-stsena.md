---
id: n28
type: problem_scenario
duration_min: 1.5
assertion: "Version 1 is a continuation of the classification process from Seminar 7: a person describes the situation in their own words, the system reads it and decides on its own whether to approve the amount or hand it to the manager; a month in production, no complaints"
learning_goal: "The scene for Case 3, written as a connected story with a numbered sequence and a closing paragraph about what today's trust rests on. The explicit prompt text is kept off the visible layer; the process is framed as a continuation of the Seminar-7 classification step, and the approval branch explicitly ends with the money landing on the client's card automatically."
visual:
  pattern: problem_scenario
  primary: >
    A framed vignette with the setting, below it the numbered steps of
    handling one request, then a closing paragraph — what today's trust
    rests on. No tables. The prompt text is not shown on screen.
  backup: >
    The rule used to be shown as the literal text of the prompt in step 1;
    it now reads at the level of the business process ("the system reads and
    decides"). The model is named (`qwen/qwen-2.5-7b-instruct`) but its
    prompt text is not quoted here — it appears on n34, layer 2. The link to
    Seminar 7 is explicit: same classification process, one decision step
    added after a request is recognized as a refund request, not a new
    process. Mirrors RU n28 after this round's edits (issue #274).
---

# Version 1: a continuation of the classification process

## Assertion

The step we're adding to the classification process from Seminar 7: once a request is recognized as a refund request, the system reads the amount and decides on its own whether to approve it or hand it to the manager. A month in production, no complaints.

## Visual

> The same request form we've already used in the previous cases: a person describes the situation in their own words — "please refund 2,500 rubles for a missed class."

1. A person writes a request in free text — it contains both the ask and the amount.
2. The process that in Seminar 7 determined the topic of a request now goes one step further here: it reads the text and decides on its own — approve the amount automatically, or pass it to the manager (model `qwen/qwen-2.5-7b-instruct`).
3. Decision "approve" — the money moves to the client's card automatically, with no human involved.
4. Decision "escalate" — the request goes to the manager, and the manager decides from there.

> **What today's trust rests on.** The version has been running for a month. Nobody has complained that something was approved that should have been escalated, or the other way around. The team considers the rule reliable — on exactly that basis: nothing bad has been noticed.

## Speaker notes

Here is how this works today, and it is not a new process built from scratch — it is a continuation of what we already built in Seminar 7. There the system read the text of a request and determined its topic: payment, rescheduling, a question about the course. Here, once a request is recognized as a refund request, one more step is added: the same system reads the amount inside the text and decides on its own whether to approve it automatically or pass it to the manager.

The request arrives through the same form we used in the previous two cases: a person writes in their own words, and the amount is stated inside the text rather than in a separate field. "Please refund 2,500 rubles for a missed class" — an ordinary phrasing, nothing structured.

One step of the chain makes the decision, and makes it in full. Inside that single step, three operations are combined at once: read the amount, compare it with the threshold, and formulate the answer — and the model does all three itself, with no check from outside. It is exactly this capability — adding an automatic refund up to a set threshold within the same form, without sending every small request to the manager — that the team implemented a month ago.

From there the fork is simple, and it brings a detail that wasn't in the previous cases: if the decision is "approve," the money is not just "processed" — it moves to the client's card automatically, with no human touch at all. If the decision is "escalate," the request lands with the manager, who then decides.

And here is what today's trust in this version rests on. It has been running for a month. In that month nobody has come forward to say "this request was approved incorrectly" or "this one was escalated for nothing." The team naturally reads that as confirmation: the rule works, the model handles it.

But it's worth saying out loud exactly what the absence of complaints confirms — and what it doesn't. It confirms that no mistake was noticeable or costly enough for someone to come back and complain. It does not confirm that there were no mistakes at all. The difference between these two claims is exactly the next beat.

Also notice what this version lacks between reading the amount and the final word of the answer. There is no separate step that states out loud, "the amount is this," and separately, "the threshold is that," and separately, "here is the result of comparing them." All of it happens inside a single model call, and the only thing that comes out is the finished word "approve" or "escalate" — with no intermediate trace by which you could check how the model arrived at that word in a given case. It is exactly this opacity of a single call that will need to be unpacked next.
