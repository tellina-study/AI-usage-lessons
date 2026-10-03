---
id: s04
type: schema_matrix
section: "Section 0. Introduction and keystone"
duration_min: 2
assertion: "Without the loop a product never reaches real use: the questions do not go away, assumptions take their place, and the error is found once the build is already paid for and rolling back costs more than the error itself"
learning_goal: "Why a product needs the loop at all: five questions ↔ six phases, the mechanism of late discovery, and why cheap building removed the only barrier there was"
learning_outcomes: [LO1, LO6]
chapter_ref: "§0.3a [for-slide-s04]"
interaction: none
verify_day_of: false
rebuilt: >
  issue #212 — the previous slide (the bridge from Lecture 4 + the central question) was
  rejected by the owner: "the value is not clear, beyond saying that we are using what was
  in Lecture 4". Rebuilt around §0.3a — the one piece of this section's content without
  which nothing later explains why six phases are needed at all. The bridge from Lecture 4
  is compressed into a single subordinate line; the central question moved to s06.
meme_or_visual: >
  A schema-matrix with no decorative shapes: on the left, five questions, each labelled with
  the phase that answers it (this is what ties the slide to the lecture map on s03); on the
  right, TWO labelled cards for the mechanism of having no loop. Every frame has a heading,
  no shape stands there without meaning.
source: "Cagan — Inspired, 2nd ed. (2017), the four product risks; Boehm — Software Engineering Economics (1981), the cost-of-fix curve [FACT-CHECK: present-day revision of the range]; MIT Project NANDA (2025), the 60/20/5 funnel"
---

# Visible content

## Title bar
Why a product needs the loop: without one, the error is found far too late

## Body

**Five questions a product answers by observation rather than by opinion**

1. Does anyone need this at all — *phase 1 · discovery*
2. Can a person actually use it, and will someone nobody thought about be harmed — *phase 2 · design*
3. Can we build it and release it safely — *phase 3 · build and launch*
4. Will it be chosen firmly enough that people pay for it — *phases 4 and 6 · measurement, governance*
5. Do those answers still hold a quarter later — *phase 5 · support*

*The first four are the product risks named by Marty Cagan (product leader, founder of the Silicon Valley Product Group, author of "Inspired"); the fifth only opens up after launch. Each has a phase of its own: the loop is the minimum set of places where these questions get answered.*

**When there is no loop**
The questions do not disappear — optimistic assumptions take their place.
The error does not disappear either; only the moment of finding it moves — to after the build has been paid for and the release has happened, where rolling back costs more than the error itself.
From requirements to release, the cost of a fix spreads out up to a hundredfold on large projects and fourfold on small ones (Barry Boehm, a researcher in the economics of software development, 1981).

**From inside the team it does not look like failure**
Built it, nobody uses it · got to a pilot and stalled · it works and it is not chosen · rolled it out, and a quarter later people stopped opening it.
In all four cases the build itself went through successfully — which is why from inside the team it reads as success; an error sitting inside an unchecked hypothesis is not visible to anyone.

[Gold]
**The expense of building worked as an involuntary barrier: while making the thing cost weeks, that cost alone forced teams to think in advance. AI is exactly what zeroed it out — and teams that never had an explicit loop now have nothing left holding them back from skipping these questions.**

## Speaker notes

Before we work out how the loop is put together, let us answer a more practical question: what happens to a product that has no loop. The answer here is concrete — a sequence of events you can list out.

A product is obliged to close five questions. Does anyone need this thing at all. Can a person use it, and will someone nobody thought about be harmed. Can we build it and release it safely. Will it be chosen firmly enough that people pay for it. And the fifth, which only opens up after launch: do all four answers hold over time. The first four are the product risks named by Marty Cagan: value, usability, feasibility, business viability. The terminology is secondary here, the structure is what works: every question has a phase of its own. The loop is the minimum set of places where these questions get answered by observation. There is no ritual in it sitting on top of the engineering work.

What happens without a loop can be described step by step. A team with no answers written down in advance does not end up with no answers at all — it records them as facts, usually optimistic ones, builds on that foundation, and learns the truth at the moment when finding out costs the most: the build is paid for, the release has happened, rolling back costs more than the error. This has half a century of measurement behind it: on Barry Boehm's estimate, drawn from projects of the seventies, the gap in the cost of a fix between the requirements stage and release reaches a hundredfold on large projects and about fourfold on small ones. The multiplier depends heavily on how quickly the loop closes, and it is not a physical constant. The loop does not remove the error in a hypothesis about the user — it moves the moment of finding it leftwards, into the cheap zone, where the error costs a conversation and the paid-for build is still ahead.

The third consequence is harder than the others: when the stopping criterion is not written down in advance, there is no way to tell "we stopped because the data said no" from "we gave up because we were tired". The anchor for that comes in the section on discovery: a product whose build went through in full and cost sixty-two million dollars never once reached real use.

And now the turn that makes all of this the subject of this particular lecture. Before generative models, the cost of building worked as a barrier against exactly this scenario: writing code was expensive, and that expense on its own forced people to think in advance. AI zeroed out precisely that cost — and with it went the one protective mechanism available to teams that never had an explicit loop.
