---
id: s07
type: assertion_visual
section: "Section 0. Introduction and methodological frame"
duration_min: 2.5
assertion: "The tool is secondary — the method decides, the tool executes; \"we adopted an AI tool\" ≠ \"we adopted an AI discipline\", and the first without the second multiplies the mess"
learning_goal: "[SI] Leading thesis v4: the method decides, the tool executes + the failure \"tool instead of practice\""
learning_outcomes: [LO7, LO1]
chapter_ref: "§0.8, §0.9 [for-slide-s07]"
in_bucket: true
visual_brief: "assertion_visual: ONE large thesis in an Ocean rounded box \"the method decides, the tool executes\" (28pt). Below it — three pillars \"why so\" as compact plates (volatility · the DORA multiplier · responsibility). On the right/bottom — the failure \"tool instead of practice\": AI without spec/ADR/gates = the DORA multiplier in the worse direction (down arrow), in one line the link prompt-and-pray/poisoned context/70%/Replit. Gold — \"the tool is chosen TO FIT the discipline, not the other way around\". Lucide icons (scales, multiplier, shield-responsibility)."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
The method decides, the tool executes

## Body
[A large thesis in an Ocean rounded box]

A methodological practice is a decision about **which artifact to produce, in what order, with what check, and who is responsible**. The tool is the executor: interchangeable and secondary.

[Three pillars "why so" — compact plates]

**Volatility** — tools and their "leadership" change over quarters; practices are durable for years because they rest on the nature of complexity (Brooks), not on the maturity of a product.

**The DORA multiplier** — "AI amplifies what is already there"; it is primary to build the discipline, not to choose the tool — a tool without discipline multiplies chaos.

**Responsibility** — the tool is not responsible for the consequences, the human is; responsibility materializes in artifacts and gates, that is, in the practice.

[Failure — tool instead of practice]
"We adopted an AI tool" ≠ "we adopted an AI discipline". The tool is there, the practice is not — and the DORA multiplier works **in the worse direction**. This is precisely what is behind all the failures of the lecture: prompt-and-pray, poisoned context, the 70% problem, the Replit incident — everywhere the tool was applied **without practice**.

[Gold callout]
Method-first order: first build the practice of the phase (artifact, gate, who is responsible), then pick the tool to fit it. **The tool is chosen to fit the discipline, not the discipline to fit the tool.**

## Speaker notes

Now let's present the load-bearing dichotomy of the whole lecture in a single thesis: the method decides, the tool executes [3]. A methodological practice is a decision about which artifact to produce, in what order, with what check, and who is responsible; the tool is the executor, interchangeable and secondary. From this follows the reading rule for the whole lecture: in each phase the practice is named first — what to do and why, who prescribes it, which artifact it ends in — and only then the tools, "here is what it's done with today", as a compact secondary block with the judgment "durable pattern or vendor hype".

Why exactly so, and not the other way around? For three reasons. First — volatility: tools change over quarters, while practices like "spec before code", "versioned decisions", "human on the merge" are durable for years; the essential complexity of the task is not removed by a tool — it is in the task itself [1]. Second — the multiplier: AI amplifies what is already there, so it is primary to build the discipline, not to choose the tool [2]. Third — responsibility: the tool is not responsible for the consequences, the human is, and responsibility materializes in human-owned artifacts and human gates [3].

And now let's examine the main failure mode this lecture treats. A team chooses a tool instead of a practice: it installs a trendy AI assistant, runs tasks through it straight into code, and considers that it has "adopted AI." There is no discipline in this: no spec before code, no versioned decisions, no gates, the human is not on the merge. And here the multiplier works in the worse direction: AI amplifies what is there, and what is there is a process without discipline, so the mess multiplies faster than it can be noticed [2]. It is precisely this mechanism that is behind all the documented failures of the lecture: prompt-and-pray — a tool without the spec discipline, poisoned context — without managing the architecture, the 70% problem — without reviewing the thirty percent, the Replit incident — without a human production gate. Each of them is not "AI made a mistake" but "the tool was applied without practice." The lesson: "we adopted an AI tool" is not the same as "we adopted an AI discipline." The alternative is the method-first order: first the practice of the phase, then the tool to fit it [3]; the tool is chosen to fit the discipline, not the other way around, and the whole lecture is an unfolding of this order across the phases.
