---
id: n57
type: bridge_forward
duration_min: 2.5
assertion: "Today every step got the model or code in turn, one road for any input; in Seminar 9 different inputs start to need different paths"
learning_goal: "Closes this session and sets up the next. The rung is named for what it is, with no promise that 'it will get more interesting'."
visual:
  pattern: bridge_forward
  primary: >
    The current workflow's diagram, faded, with a dashed fork drawn over
    it at the spot where S9 will add branching. Below, three lines about
    the next session.
  backup: >
    Content follows KONTSEPTSIYA-7-12.md §7, the S9 row, exactly:
    "branching: condition versus switch, classification as a step, default
    branch, merge"; the typical problem "an input that fits no branch;
    Merge cuts by the first input"; the conceptual change-of-pace "Optum or
    IRS — what the classifier decides on" (the choice between the two
    cases had not been made yet as of this file — not prejudged here).
---

# What's next

## Assertion

Every request traveled the same single road. Going forward, we need more than one.

## Visual

> Now: **any input** → one and the same path through the chain
> Next: **input type A** → one path · **input type B** → another · **input that fits no type** → its own default path

**Seminar 9:**
condition versus switch · classification as a separate step of the chain · what to do with an input that fits none of the named branches · how branches that look parallel on the canvas actually execute

## Speaker notes

What we are ending on today, and what today's session was still missing.

All through today, each step of the chain in turn got handed either to the model or to code — but the path any given request actually traveled was still the same single path for everyone: every request went through the exact same sequence of steps, regardless of what it was actually about. The notification got assembled the same single way for every request. The duplicate check was one and the same check, applied to everyone alike. The refund decision got made by one piece of logic, for any amount at all, with no distinction drawn between them.

But the request's own topic has already been pulled out into its own separate field, ever since last session — and the moment it is pulled out like that, it becomes obvious that a request about payment and a request about rescheduling a class really do need to travel different ways from this point on: one of them should go to the accountant, the other should go to the schedule instead. That particular split simply cannot be done by sending both down the same single road.

The next session is about the fork in that road. Condition versus switch: when a branch point should decide one plain yes-or-no condition, and when it actually needs a choice among several named branches at once instead. Classification as its own separate step of the chain, one whose whole job is deciding which branch a given request goes down next. What to do with an input that does not fit any of the named branches at all — the tool itself has a built-in default answer for exactly that case, and it is not always the answer you would expect it to be. And there is one thing I will say ahead of time, specifically so that none of you talk yourselves into believing the opposite later: branches that look perfectly parallel sitting side by side on the canvas in fact execute one after another, in strict sequence, in the exact order they happen to sit on the screen.

The next session's conceptual change of pace will be either Optum or IRS — one more case where what is actually at stake is not a single conversation with one client, but a classifier's own decision, one that ends up governing how tens of thousands of people are handled all at once, together.
