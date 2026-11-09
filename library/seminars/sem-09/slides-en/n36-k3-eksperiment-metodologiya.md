---
id: n36
type: mechanism_node_graph
duration_min: 1.5
assertion: "Code and judge got the same wording of the five requirements and the same answer text — 36 calls on the live rig, four builds"
learning_goal: "Methodology beat: exactly what was measured, on what, and how much. Without this screen, the next beat's numbers mean nothing — and the measurement's limit is named honestly: the judge-in-the-loop variant was run on four of the six questions."
visual:
  pattern: mechanism_node_graph
  primary: >
    Four vignettes in a row: why measure at all · what counts as a good
    enough answer · which four builds were run and how many calls each ·
    where the measurement hits a limit. No screenshot on this frame: the
    canvas and the panel were already shown two screens back.
  backup: >
    All the content is from `stend/zamery-k1-k3/README.md`, Measurement 2:
    the five requirements verbatim from the "Task" section, six questions
    on six knowledge-base items, four builds and each one's call count from
    the "Actual call count" table (6 + 8 + 16 + 6 = 36).

    The `judge-check` build is named as its own vignette because it is the
    load-bearing part of the whole design: it hands code and judge ONE AND
    THE SAME finished text. Without it, the comparison would be a
    comparison of two different answer samples, and the n37 finding
    wouldn't read as a disagreement between checkers.

    THE MEASUREMENT'S LIMIT IS NAMED ON THE FRAME, not hidden in the notes:
    the judge-in-the-loop variant was run on four of the six questions —
    stopped by the call budget, not because the finding had stopped
    holding up (protocol, section "Measurement 2, judge variant, not run to
    completion").

    The model's name (`qwen/qwen-2.5-7b-instruct`) is named on the frame as
    "the same model across all four builds": what matters for the argument
    is exactly this identity, not the brand. Scenario ids, webhook
    addresses, and run numbers do not go onto the visible layer (BRIEF §2).

    The word "measurement" from the rig's own scenario names is not carried
    onto the frame: on the slide this is the case's own process, not
    measurement scaffolding (BRIEF §3).
---

# How it was measured: one text, two checkers

## Assertion

Code and judge got the same wording of the requirements and the same finished answer.

## Visual

> **Why measure, if there were no complaints.** A complaint only arrives for a mistake that was noticed and judged costly. A checker that lets a bad answer through, or rejects a good one, never draws a complaint either way: in the first case nobody finds out, in the second a person just waits longer. You can only see this by measuring.

> **What counts as a good enough answer.** The same five requirements: no longer than 280 characters · names the key detail of the matching knowledge-base item · says where to go next · contains no numbers that aren't in that item · entirely in Russian. **The wording is identical** — in the checker's code and in the judge model's prompt, word for word. Six questions, one per knowledge-base item. The same model in every build.

> **Four builds, 36 calls.** With no loop, one call — **6 calls**, the baseline for comparison. A loop with a code check — **8 calls** on six questions. A loop with a judge model, up to three attempts — **16 calls**. And separately: the judge reads an **already-finished answer**, one whose code verdict is already known — **6 calls**.

> **Where the measurement hits a limit.** The loop with a judge was run on **four of the six questions**: the call counter was approaching its cap, and the remaining two questions gave way to the fourth build. This is a budget decision, made before the result was known.

## Speaker notes

Before looking at the numbers, you need to know exactly what was measured — otherwise the numbers mean nothing.

First, why at all. We've already talked about a month without complaints: a complaint only arrives for a mistake that was noticed and that cost something. A bad checker makes both kinds of mistakes quietly. Let a bad answer through — nobody finds out. Reject a good one — the person just waits longer, and the process makes an extra loop. Neither one surfaces on its own, and the only way to see it is to measure.

What counts as a good enough answer — the same five requirements, and here's the main detail of the whole design. The wording is identical in both checkers, word for word: whatever is written in the code is also written in the request to the judge. Six questions, one per knowledge-base item. The same model across every build.

Four builds. The first — no loop at all, one call: this is the baseline the others are compared against. The second — a loop with a code check. The third — the same loop, but checked by a judge model, up to three attempts. And the fourth, the one that makes the comparison honest: the judge gets an already-finished answer, one whose code verdict is already known. The same text, two checkers, no difference in the sample. Thirty-six calls in total.

I'll name the measurement's limit right away. The loop with a judge was run on four of the six questions: the call counter was approaching its cap, and the remaining two questions gave way to the fourth build — the one where code and judge talk about the same text. The decision was made before the results were known.

And before we flip the screen, place your own bet. The task is toy-simple: string length, whether a word appears, a set of characters. How many times out of six, in your guess, will the judge model get it wrong where code is just reading a substring — and in which direction will the mistake go?
