---
id: n13
type: failure_vignette_table
duration_min: 1.5
assertion: "Two real runs of the model version: one text came out exactly as Olga asked, the other had the literal instruction text inside the message"
learning_goal: "Restored failure-demo slide (existed in deck v1, dropped at the v2/v3 transition, restored by the owner's voice edit 2026-10-20, issue #274). A table of 'request text / what came out and why', with no system ids on screen (canon §3) — not A5 (this is a demonstration of runs, not a breakdown of actions/options)."
visual:
  pattern: failure_vignette_table
  primary: >
    A two-row table: request text · what came out and why. Below the
    table, a conclusion that a format check doesn't catch this error.
  backup: >
    The data is from real runs on the rig; no execution ids are shown on
    the slide (canon §3): two requests through the workflow "С8 · Case 1
    (before) — LLM composes the notification" — confirmed in
    `stend/README.md`, "Case 1 — LLM notification vs. template", against
    the runData of each execution read directly. These are the only two
    documented runs of the model version on this rig; a third documented
    run (the template) is deliberately not included here — it has its own
    breakdown slide (n14), and this table is about the model version only.
---

# What two real runs actually produced

## Assertion

The same node, the same instruction — on one request the text is flawless, on the other the message contains the literal text of the instruction.

## Visual

| Request text | What came out and why |
|---|---|
| Maria: "I want to sign up for the analytics course and also ask about payment, please call back today" | Delivered: "New request from Maria: topic 'course,' also mentioned: payment." Free-form text, but it matched the goal in meaning — the model had enough from the instruction and the three values; interpreting was genuinely simple here. |
| Oleg: "I want to move my class to Friday and ask about course payment" | Delivered: "Hi, **[Coordinator's name]**! We have a new multi-topic request from Oleg about moving a class and about payment." The model inserted a literal fragment of its own instruction template — words addressed to itself, not to Olga. The node didn't fail, the message was delivered, the status was green: the mismatch is visible only in the content. |

> **A format check doesn't catch this.** Both runs are technically successful: both nodes completed, both messages were delivered. The only way to notice the difference is to read the actual text a real person received.

## Speaker notes

Here's what actually came out in practice, not just in theory — two separate runs of one and the same node, with one and the same instruction, run against real requests.

The first request — from Maria, about a course and about payment. The model received three values along with the instruction to write a short, friendly notification. The result: "New request from Maria: topic 'course,' also mentioned: payment." It sounds free and quite human — and at the same time it matches, in meaning, exactly what Olga asked for. On this particular request there was genuinely nothing complicated to interpret at all: the three values fall together easily into a single phrase.

The second request — from Oleg, about rescheduling a class and about payment. The very same node, the very same instruction. And here is what it actually wrote this time: "Hi, [Coordinator's name]! We have a new multi-topic request from Oleg about moving a class and about payment." Read that second word carefully. This is not a variable that simply failed to substitute correctly on a technical level — it is a literal fragment of the model's own instruction template, words addressed to the model itself and not to Olga, which the model was supposed to replace with real content and, in this case, did not.

And here is what matters about what happened at the level of the execution log: nothing at all. The node did not fail, did not return an error. The status reads success on both runs. If all you do is look at the log, the second run is completely indistinguishable from the first.

There is only one way to find out that something is actually wrong — you have to read the actual text that a real person received. A check on the message's format is powerless here: the resulting text is syntactically fine in both cases, and the difference between them shows up only in the content.

And there is the answer to the question left from the previous screen: the message sometimes comes out looking exactly the way it needs to, and sometimes it doesn't, and there is no way to predict in advance, just from looking at how the node is configured, which of the two outcomes the very next request will produce. Next comes an architecture that drops this node altogether, along with its real configuration.
