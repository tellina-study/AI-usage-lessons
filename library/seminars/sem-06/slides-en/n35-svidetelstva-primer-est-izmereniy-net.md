---
id: n35
type: research_evidence
duration_min: 0.75
assertion: "A teaching example from the harness documentation — the subagent read 6,100 tokens of files, the session got a 420-token result — shows the order of magnitude of the saving qualitatively; a measurement over a sample of real sessions exists in no source at all"
learning_goal: "There is a number, but it is an illustration of one documentation scenario, not a statistic. The honest gap is named directly right here and for the first time in the class — the number is given to it as an illustration, and a gap it remains"
visual:
  pattern: mechanics_table
  primary: "A short quote of the teaching example in large type, with an explicit caption \"not a measurement — an example from the documentation\". Below it — a plate with the honest gap, named here for the first time and by its own name."
  backup: "The source is research/mechanics-6-subagent.md §2.2, verbatim: \"The subagent read 6,100 tokens of files. You got a 420-token result. That's the context savings\" (context-window.md, Anthropic's own teaching example, not a measured statistic). The honest gap is spoken out loud here, in this case's evidence, and nowhere else in the deck — which is exactly where the chapter puts it (`rework/section-2-subagent.md`, § \"Evidence\"): \"numbers for how much context a subagent saves compared with the same volume of work in the main session were not found in any source\". Owner's round 3 (issue 225): the number is new to the deck and is used here for the first time. Round 5 (issue 225, ZADANIE-KRUG-5.md, cross-cutting decision C1): the word \"window\" was removed from the slide entirely, replaced by \"context\"; \"parent\" was replaced by \"the session that called the role\"."
---

# There is an example; a measurement over a sample, no

## Assertion

"The subagent read 6,100 tokens of files. You got a 420-token result. That's the context savings" — the documentation's own teaching example, not a measurement.

## Visual

> **"The subagent read 6,100 tokens of files. You got a 420-token result. That's the context savings."** — the harness documentation on how context works, one illustrative scenario.

An order of magnitude of difference — but this is one invented example by the author of the documentation, not a statistic over many real runs.

> **An honest gap.** How much context delegation really saves compared with the same volume of work in the main session, measured over a sample of sessions, was not found in any source. This number fills the gap with a teaching example, not with a statistic.

## Speaker notes

The harness documentation on how context works gives its own example: the subagent read 6,100 tokens of files, you got a 420-token result — that is the context saving. An order of magnitude of difference, and the direction is the same one we arrived at by counting: the forty files stay in the subagent's context, only the result comes into the session.

The nature of this number is worth naming directly. It is one illustrative scenario, invented by the author of the documentation in order to explain the mechanism. It is not a measurement over many runs, and there is no sample of real sessions behind it.

Next to it stands an honest gap, and the seminar names it directly. How much context delegation really saves compared with the same work in the main session, measured over a sample of sessions, was not found in any source. The example does not close that gap — it illustrates it with a number.

So why show an illustration at all. The direction and the order of magnitude are real and are held up by the mechanics of the previous screen: forty files stay where they were read, a short list goes back. What would be dishonest is to serve an illustration as a statistic silently; named for what it is, it works as a bearing. As a proof it does not work.

In our scene the ratio is the same in meaning: forty files going in, four addresses coming out, and in the working session's context only the addresses remain. The documentation's numbers speak about the same arrangement, just on their own example.

It is worth saying separately how a number like this goes on living. It is lifted out of the documentation into a retelling, in the retelling the caption "the author's example" is lost, and two steps later it sounds like a measured saving. If you meet "delegation saves an order of magnitude of context" with no indication of where that was measured, you are most likely holding a retelling of a retelling of exactly this example. The check is simple: a measurement has a sample, a method and a spread; an illustration has one number.

What would count as an honest measurement is worth saying precisely — it is work any one of you could do on your own project. The same question, run in two modes over a sample of real sessions: reading in the working session against delegation, with the share of context taken up measured in both. No such work exists in open sources, and that is exactly the figure the course is missing.

About the convenience of the numbers themselves. The ratio of 6,100 to 420 was picked by the author to suit the illustration, and the caption on screen says so. What is worth trusting is the order of magnitude — a difference of tens of times; the second significant digit means nothing here, and there is no point arguing about it.

And the dependency that makes the number manageable. The saving depends directly on the size of the subagent's answer. A subagent asked to come back with a short conclusion comes back with hundreds of tokens; a subagent asked to retell what it read will come back with thousands, and the saving is eaten by the format of the answer. The same consideration is what the criterion closing this case grows out of: what you have to look at is what will be left in the context after the answer.
