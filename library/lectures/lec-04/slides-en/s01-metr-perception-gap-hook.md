---
id: s01
type: hero_cover
section: "Section 0. Introduction and methodological frame"
duration_min: 3
assertion: "16 experienced developers with AI worked 19% longer — yet were convinced AI was speeding them up: the feeling of productivity is a hypothesis, not data, so reliability comes from discipline, not from a feeling"
learning_goal: "Hook: the perception gap on a clean experiment; justification of the method-first axis of the lecture"
learning_outcomes: [LO7]
chapter_ref: "§0.1 [for-slide-s01]"
visual_brief: "HERO ≥40%: a real illustration of time measurement / the METR chart (predicted −24% → believed −20% → actual +19%) full-bleed on the left or top; assertion + 3 numbers in an Ocean rounded box. Real image via 6-tier acquisition (Phase 6): the diagram from the METR paper arXiv:2507.09089 or a photo of a development environment. Gold highlight — the contrast \"believed −20% vs actual +19%\" (an error in the sign). Attribution: \"METR · 2025\"."
interaction: open_question
verify_day_of: true
hero_required: true
---

# Visible content

## Title bar
"16 experts were sure AI was speeding them up — and got the sign wrong"

## Body
[Left / hero illustration — time measurement, real image ≥40% of the area]

**The METR experiment, first half of 2025**
- 16 experienced open-source developers, 246 real tasks in **their own** well-known repositories
- Some tasks — with a modern AI tool, some — without; they measured **real time**, not the feeling

[Right — Ocean rounded box: three numbers about one thing]

**Three numbers about the same thing**
- Prediction before the experiment: AI will speed things up by **−24%**
- Belief afterward, having already worked: sped up by roughly **−20%**
- Measured fact: with AI the tasks took **+19% more time**

**Perception gap** — the divergence between the subjective feeling of speed ("AI is speeding me up") and the objectively measured fact

[Gold callout, bottom]
Professionals who have written code for years got it wrong not in magnitude — but **in the sign**. "I feel the tool helps" is a hypothesis, not data; so reliability comes not from a feeling but from **discipline** with a built-in check.

[Open question, below in small type]
Does AI speed you up personally — by how much? And how do you know?

## Speaker notes

Let's start not with excitement and not with a warning, but with a measurement. In the first half of 2025, the research organization METR ran a randomized controlled trial with sixteen experienced open-source developers [1]. These were not students but maintainers of mature projects with tens of thousands of stars, working on two hundred forty-six real tasks in their own, well-known codebases [1]. Some tasks were allowed with a modern AI tool, some without; what was measured was not the feeling but the real completion time [1].

Before starting, the developers predicted that AI would speed them up by about twenty-four percent, and after the experiment, having already worked with the tools, they estimated the speed-up at about twenty percent. The objective data showed the opposite: with AI allowed, the tasks took on average nineteen percent more time [1]. The baseline without which this number can't be read: these are experienced developers on code familiar to them, only sixteen people [1]; on an unfamiliar, isolated task the effect is different and positive — we'll come back to that. Professionals who have written code for years got it wrong not in the magnitude but in the sign.

Let's introduce a term that will run through the whole lecture. The perception gap is the divergence between the subjective feeling of speed and the objectively measured fact [1]. This does not mean AI always slows you down: on isolated tasks it measurably speeds you up. It means something else, and more important for an engineer: "I feel the tool helps" is not data but a hypothesis, and in development this hypothesis is systematically biased [1]. And since even an expert cannot sense whether the tool helps or hinders, the decision "whether to apply AI and how" cannot be made by feeling — it is made by discipline: measurable criteria built into the process. Consider: does AI speed you up personally — and how do you know?
