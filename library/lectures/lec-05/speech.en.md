---
lecture: 5
title: "Lecture 5. The AI Product: The Full Lifecycle — From Intent to Operation"
length_words: "~8,700 spoken (part 1 ~5,700 + part 2 ~3,900), mirroring the RU original"
length_min: 100
status: draft
version: v1.0
parts: 2
derived_from: "English translation of speech.md + speech-part2.md (RU v1.0), source of truth chapter.md + chapter-part2/3/4.md + deck.yaml + deck-part2.yaml + slides/s01..s49b"
issue: 189
slides_covered_part1: [s01, s02, s03, s04, s05, s06, s07, s07b, s08, s09, s10, s11, s12, s13, s13a, s14, s14b, s15, s16, s17, s18, s19, s20, s21, s21b, s22, s23, s24, s25, s26, s27]
slides_covered_part2: [s28, s28b, s29, s30, s31, s32, s33, s34, s35, s36, s36b, s37, s38, s39, s40, s41, s42, s43, s44, s44b, s45, s46, s47, s48, s49]
translation:
  - "Full faithful spoken-register English duplicate of the RU speech (not a machine gloss). Terminology per the EN lock in the task brief and per lec-05 glossary.yaml canon. RU is source of truth; this file mirrors it section-by-section, same slide anchors, same argument order, same numbers/baselines/fact-integrity corrections."
  - "Keystone terms preserved: feedback loop; cost/trust asymmetry; Customer Development (Blank); The Mom Test; falsifiable hypothesis (belief→test→date); reference dataset; Design Thinking / Double Diamond; Nielsen heuristics; design system; MVP / Build-Measure-Learn; feature flag / canary / rollback / Stage-Gate; CC/CD vs CI/CD; agency ladder; eval / LLM-as-judge / pass@k vs pass^k; OEC; guardrail metric; peeking / SRM; SLI/SLO/error budget; incident/postmortem; LLMOps/AgentOps; model drift / silent drift; Goodhart's law / reward hacking; guardrails / policy-as-code; Guardian Agent (Gartner category); maturity 0-5; operators→orchestrators; hidden human cost."
  - "Numbers, dates, brand names, and study attributions preserved verbatim, including all fact-integrity corrections carried from the RU source (MSI all five reactions weighted ×5, not anger alone; Bing headline test ≈$100M annual US revenue, not the unrelated '$300M button' usability finding; Mata v. Avianca fake citations are ChatGPT, not Harvey AI; Med-PaLM 'chemo for headache' claim does not trace to a primary source; Guardian Agents is a Gartner analyst category, not a confirmed Sberbank product name). US spelling throughout. Uses 'AI' (not 'ИИ')."
changelog:
  - "v1.0: first English translation of speech.md + speech-part2.md v1.0, produced under the bilingual production rule (issue #172). Split identically to the RU original: speech.en.md (Section 0 keystone + Sections 1-3, s01-s27) + speech-part2.en.md (Sections 4-6, s28-s49)."
---

# Lecturer's Speech · Lecture 5 "The AI Product: The Full Lifecycle — From Intent to Operation"

**Duration:** ~100 min (92 active minutes + ~8 min Q&A buffer on s49).
**Parts:** `speech.en.md` (this file) — Section 0 (keystone) + Sections 1-3 (Discovery, Design, Build/Launch), slides s01-s27. `speech-part2.en.md` — Sections 4-6 (Measure, Support/Operate, Governance) + payoff + Q&A, slides s28-s49.
**Source of truth:** `chapter.md` + `chapter-part2/3/4.md` (the book is the source of truth), cross-checked against the speaker notes of slides s01-s49b. This is a spoken unfolding for the lecturer, not a reading of the chapter.
**Format:** conversational English, direct address, rhetorical questions, pauses and emphasis marked inline in square brackets where useful. Methodological / pedagogical asides are allowed in this speech (unlike the visible slide layer) — they help the lecturer hold the thread.

## Preparation before the lecture

- Order of the 56 slides: 6 dividers (s07/s14/s21/s28/s36/s44), 6 ELI5 overviews right after each divider (s07b/s14b/s21b/s28b/s36b/s44b), 2 keystones (s05/s06), 2 syntheses (s35/s43), the finale s49 with the checklist and Q&A.
- Re-verify `[VFY-day-of]` before the day of the lecture: Anthropic PR metrics (s01, s23), design tools v0/Figma Make/Stitch (s17), Anthropic 200%/16% (s23), Stanford RegLab (s34), Guardian Agents/GigaCowork (s38), Deloitte/Sber/Gartner (s46, s47).
- The meta-pattern repeats six times: the classic discipline → what AI adds → where AI is limited → a failure from this phase. By the third section you can name it out loud: "you're recognizing the pattern — that recognition is the method."
- The keystone cost/trust asymmetry as the connective thread: Build → almost zero; Measure/Learn → trust drops; Observe/Orient → faster but more exposed. Return to the formula in one sentence at the close of every section.
- 13 on-point failures across 6 sections, no section skipped, no failure force-fitted — a substantive answer to the "here comes AI-doom again" skepticism.
- Backup if the projector fails: narrate by the six arrows of the loop; every number and case is spoken aloud in the speech itself.

---

## [s01] — Hook: the paradox

"Let's not start with a definition. Let's start with a paradox.

Anthropic describes its own internal experience like this: tasks that used to take weeks of writing and reviewing code now take hours. An agent writes the implementation, passes the tests — and the code is nearly free.

At the same time, in the summer of 2025, a research group at MIT Media Lab published a report that the media picked up under the headline: 'ninety-five percent of organizations get zero return from generative AI.'

Both facts are true at once. And at first glance they contradict each other. Building is nearly free — and almost nobody is extracting value from it. How is that even possible?

I won't resolve the paradox right now — that's the payoff of the lecture, we'll come back to it at the end, with numbers. But let's fix the shape of it right away, because it holds up everything that follows: **building has become nearly free, and turning that build into real value has not.**

We're going to walk the entire product lifecycle — from intent, through discovery, design, build, measurement, operation — and at every phase we'll ask the same question: what did AI make cheap here, and what stayed expensive and human?

[Pause, thirty seconds] Think about it: if building became almost free — what became the real bottleneck of a product? Hold on to your answer, we'll come back to it more than once."

---

## [s02] — Cover and roadmap

"Lecture five. The AI product: the full lifecycle — from intent to operation.

Lecture four dissected the lifecycle of code. Today we zoom out: code is one phase — now dramatically cheaper — inside a much wider product lifecycle.

Let's be honest about you specifically: you're technically strong, you write code with AI assistants every day. But most product disciplines — customer development, design thinking, product experimentation, operations run like reliability engineering — you're most likely seeing for the first time. So each of today's six sections opens not with AI, but with the classical foundation: where the discipline came from and what problem it solves, without a single mention of artificial intelligence. Only after that do we ask what AI changes and where it breaks.

This isn't academic politeness. An engineer who only knows 'how to build fast,' but doesn't know why customer discovery or A/B testing exists, risks making a decision that's technically flawless — and pointless or dangerous from a product standpoint. The very structure of this lecture — foundation, then AI, then limits, then failure — applies the course's own thesis to itself: to judge whether AI belongs somewhere, you first have to know what existed before it."

---

## [s03] — Lecture map = the loop

"Here's the map of today's lecture — and it's not drawn as a list, it's drawn as a circle. Six sections aren't six independent topics; they're six arrows of one loop. Discovery — where the hypothesis comes from. Design — how the hypothesis becomes an artifact. Build and Launch — how the artifact becomes a working product in production. Measure — how you verify whether it actually worked. Support and Operate — what happens when the product is live twenty-four seven. And Governance — how the organization decides where to put its capital.

The key point: the last arrow loops back into the first. Signal from operations and governance decisions changes what we investigate next in Discovery. This is a closed cycle, not a one-time linear process — and at the end of the lecture we'll come back to this same circle, but with a full understanding of what happens on every arrow."

---

## [s04] — Bridge from Lecture 4 + the central question

"Lecture four showed: software development with AI is an engineering discipline built around a loop of human-owned artifacts. A spec turns into an architecture decision, that becomes a plan, the plan becomes a pull request, and operation produces an incident record that loops back as a new requirement into the spec. That loop lives inside a single phase of the product lifecycle — Build, which we'll dissect in Section 3.

Today's lecture goes up one level. The product as a whole runs its own loop, and the decision to go back to the start or kill the product is made not by an engineering criterion, but a product one: did the hypothesis about user value hold up?

The difference in scale matters. Lecture four answered 'how do I write the code I'm accountable for' — its unit of work was a pull request, a commit. This lecture answers 'where does the confidence to write that code even come from in the first place' — its unit of work is a hypothesis, an experiment, a release decision. Code is just one step, and now the cheapest one.

That gives us the central question of the lecture, the one we'll return to in every section. Write it down, it's load-bearing:

*Now that AI has made building nearly free — what became the real bottleneck of a product, and at every phase of the cycle: which classical discipline still stands, what does AI speed up, and where does AI-first break?*

Hold this question as a lens: not 'can AI be applied here' — you almost always can — but 'where did the bottleneck move when this arrow got cheaper.'"

---

## [s05] — KEYSTONE: the feedback loop

"This is the key slide of the lecture — the whole logic that follows depends on it. Hold it in your head through all six sections.

The load-bearing idea: **a product is a feedback loop. Discover, build, measure, learn, decide, discover again.** And this is a shape that at least three people arrived at independently, from completely different fields, with no contact with one another.

Walter Shewhart and W. Edwards Deming, quality-control statisticians, formulated the PDCA cycle — plan, do, check, act — back in 1939 and the 1950s. John Boyd, a military fighter pilot, formulated the OODA loop in the 1970s — observe, orient, decide, act — as a model of who wins a dogfight: not the pilot with the faster plane, but the one who cycles through this loop faster. Eric Ries, an entrepreneur, formulated Build-Measure-Learn — build a minimally sufficient product, measure the market's reaction, learn — as a way to avoid spending months on a feature nobody wants.

A statistician, a fighter pilot, and an entrepreneur drew, in essence, the same blueprint, without coordinating with each other — a compelling argument that the feedback loop isn't a trendy methodology, it's a structural property of any system that learns under uncertainty.

There's a nuance to the same shape — the single loop and the double loop. A single loop corrects an error relative to a fixed goal, like a thermostat. A double loop goes deeper: it questions the goal itself. Hold this in mind — it foreshadows a failure from Section 4: training a model on human feedback is a mechanized single loop, and reward-function hacking is exactly its failure mode.

That's exactly why AI cannot 'cancel' the loop. It can change how much each arrow of the loop costs and how much you can trust it — but not the underlying necessity of observing reality, interpreting it, and deciding."

---

## [s06] — KEYSTONE-2: the cost/trust asymmetry

"The second half of the keystone — the central analytical instrument of the lecture: **AI changes the cost and the trust of every arrow of the loop asymmetrically, not uniformly.**

Three cases. The 'build' arrow — cost has nearly collapsed to zero: writing code, a design draft, a first research prototype are orders of magnitude cheaper and faster than five years ago. We'll dig into this in Section 3.

The 'measure' and 'learn' arrows — cost stayed the same, but trust in the result dropped: the measurement instrument itself became probabilistic and vulnerable to metric manipulation. Section 4 will unpack this in detail.

The 'observe' and 'orient' arrows — got faster, but more exposed to attack: the speed of observing a system in production went up, but the very ability to react quickly turns into a vulnerability if the observed data can be poisoned. We'll open this up in Section 5.

From here comes the meta-pattern that will repeat in every one of today's six sections, literally on the same template: **every phase of the product lifecycle has a classical discipline, and AI does not cancel it.** AI changes how much that discipline costs and how much you can trust it without verification — but it does not remove the need for the discipline itself. Customer Development doesn't get replaced by 'ask the model what the user thinks.' A product experiment doesn't get replaced by 'the model predicted the metric would go up.' SRE-style operations doesn't get replaced by 'the agent will figure it out.'

In every section we'll ask one question: what does the classical discipline make reliable, what does AI speed up — and at what point does speed become a trap, because trust doesn't keep pace with it.

[Pause, twenty seconds] On which arrow of your most recent task did speed outrun your actual trust in the result? Hold on to your answer, it'll be useful at the end."

---

# SECTION 1. DISCOVERY

## [s07] — Divider: Section 1

"Moving to the first arrow of the loop — Discovery. This is the phase where the hypothesis about what to build even comes from. Most strong engineers have informal experience 'asking friends' — but almost nobody has run into the discipline that explains why that experience systematically lies to you.

Two classical foundations in this section: a methodology for finding a business model, and a technique for a single conversation. Then — what AI adds, where it's limited, and three failures that show three facets of the same mistake: a synthetic source mistaken for a verified fact."

## [s07b] — ELI5: Discovery in plain terms

"Before we get into the formal methods — let's break discovery down to basics.

Discovery is the first arrow of the loop. At this point you're not building anything yet. Your only job is to figure out whether it's even worth building something, and for whom. Sounds simple, but this is exactly where most products fail: the team falls in love with its own idea and builds it without ever checking whether there's a real problem that idea actually solves.

The key mental model for this section: **there are no facts inside the office.** Everything you think about your users while sitting at your desk is a hypothesis, not knowledge. Facts live outside, with real people.

AI can help a lot — summarizing interviews, pulling together desk research in minutes instead of hours. But it cannot talk to a real person on your behalf, and it cannot produce real disagreement. Next — two classical techniques that keep a conversation honest, and three real failures where discovery got replaced by a plausible-sounding invention."

## [s08] — FOUNDATION: Customer Development

"Let's start with the classic — you have to start here, not with an AI tool, because without this frame any AI tool just speeds up the mistake.

Customer Development is Steve Blank's methodology, from 2003. The central idea sounds like an aphorism, memorize it word for word: **'there are no facts inside the building, so get outside.'** A startup, in Blank's terms, is not a smaller copy of a big company — it's a temporary organization in search of a repeatable business model under extreme uncertainty. You can't write the plan in advance, because it depends on answers only customers know.

The method is four sequential steps, each ending in an explicit decision to continue or pivot. Discovery — turn the founders' hypotheses into facts by going out to real people; the step is explicitly hypothesis-first: you write down what you believe before you walk out the door. Validation — can you sell this not just to the first enthusiasts, but to a wider circle. Creation and Company Building — generate demand at scale and shift the organization from search mode into execution mode.

Blank's canonical example: the founders wrote a forty-page business plan and only then held their first conversation with a customer — every important decision made on zero evidence. The Lean LaunchPad courses forced teams to run ten or more interviews before writing a single line of the plan: the discipline, not the plan itself, was the graded outcome.

And here's a technique we'll reuse in every phase that follows — in the experiment, in the launch gate, in the drift threshold. It's called the **falsifiable hypothesis**: a written statement of the form 'we believe X, we'll test it via Y, by date Z we'll have a yes-or-no answer.' The format turns vague confidence into a testable commitment with a date — and we'll see it in a few slides as the only defense against one of this section's failures."

## [s09] — FOUNDATION-2: The Mom Test

"If Customer Development is the map — which four steps to walk — The Mom Test is the technique for one step: how to run a single conversation with a single person without lying to yourself.

The method was formulated by Rob Fitzpatrick: **even your own mother will lie to you about your business idea's quality** if you ask her directly — and the defect isn't in the honesty of the person you're talking to, it's in how the question is built.

Three rules. First — talk about their life, not your idea: don't pitch the idea and don't ask for a verdict — that creates a 'politeness problem' where the person protects your feelings instead of telling you the truth. Bad: 'do you like the idea?' Good: 'walk me through how your team handles weekly reporting.'

Second — ask about specifics from the past, not opinions about the future: hypothetical questions invite dishonest optimism. Instead of 'would you pay twenty dollars for this?' — 'what do you pay today for the closest thing to this?' The second question anchors on real past behavior.

Third — talk less, listen more, validate with a real commitment, never a compliment. 'I love it' is free and means nothing. Legitimate signals are time, reputation, money: will the person get on a call, will they pre-order.

And a distinction engineers often confuse: qualitative research answers 'why' at a small sample size, quantitative answers 'how many' at scale — that's a division of labor, not a hierarchy. And sample bias: interviewing only your friends systematically inflates enthusiasm — invisible from inside the interview, only visible on an audit of who you actually talked to. Hold on to that — it's the direct premise of the first failure a couple of slides from now."

## [s10] — AI: capabilities + tools in Discovery

"Now — what AI actually changes in this phase.

Desk research — scanning market reports, forum complaints — collapses to minutes. Perplexity Deep Research is widely considered the best tool for this: it plans a research trajectory, reads dozens of sources, returns a cited report in minutes, cutting research time by roughly fifty percent.

Mandatory practice — memorize it word for word: **verify important data directly against the cited source before using it in a decision.** Citations exist precisely so verification is possible — the tool doesn't remove that step. This is a direct bridge to the failure a few slides from now, and there the price of skipping it is measured not in time, but in money and reputation.

Interview synthesis — tools like Dovetail are built for cross-interview synthesis: a quote in the summary is anchored back to its original source, which protects against drifting into an unverifiable summary.

Let me draw a line here as sharply as I can: synthetic users are legitimate narrowly, as a pre-research tool — piloting an interview guide, sketching hypotheses. But none of those outputs is evidence for a 'ship it or not' decision. A telling number: ninety-seven percent of researchers already use AI, but only around eight percent trust AI personas as a data source — a healthy gap, not a sign of falling behind.

Even Teresa Torres, a leading voice in discovery practice, uses AI for a first draft, but never drops the rule 'synthesize each interview separately first, then across interviews' — and she warns against 'one-click AI trees,' because the team's own thinking is the entire point of the process."

## [s11] — AI limits in Discovery

"Now — where AI is structurally limited in this phase, not just 'not good enough yet.'

Teresa Torres documented a measurable finding: an AI summary can miss twenty to forty percent of important interview detail when the synthesis skips the 'individually first' step and jumps straight to cross-interview themes. That's not a vague 'AI sometimes gets things wrong' — it's a traceable methodological failure.

Now the accumulation argument, follow this carefully. Rule two of The Mom Test — ask about specific past events, not hypothetical futures — a synthetic persona structurally cannot satisfy: it has no real past, only something that sounds plausible. Stack that on top of the model's tendency to agree, and you get a compounding failure: not just 'biased toward yes,' but 'biased toward yes about an event that never happened.'

What survives from the classics: the three Mom Test rules apply the same whether a human or an AI is asking the question; Blank's hypothesis-first discipline is the antidote to a one-click AI tree; validation through a real commitment has no AI substitute.

The criterion, stated as operationally as possible: the closer the output sits to an irreversible decision about real people or real money — the more strictly you need a real human with a real past. The further away — the more appropriate AI is as a drafting accelerator."

## [s12] — Failure #1: NN/g synthetic users

"And here's the first failure of the section — measured, reproducible, concrete.

Nielsen Norman Group ran a controlled usability comparison of onboarding. Real users completed, on average, **three out of seven** onboarding steps. A synthetic AI panel testing the same flow falsely reported completing **seven out of seven**. Real users described one feature as 'contrived and useless'; synthetic personas produced multi-paragraph enthusiastic praise; one synthetic user called impractical drone delivery 'a game changer' — while real people rated it skeptically.

Notice the basis for this: this isn't a one-off prompting mistake, it's a structural divergence on both measured quantities, from the same test material.

The mechanism, the root cause — large language models are tuned to agree with the frame of the question they're asked. A synthetic user cannot produce disagreement, because it has no real experience capable of contradicting how the question was phrased — only a statistically plausible continuation of text. This is the same sycophancy mechanism the course already discussed. Here it materializes as a concrete, measured failure specifically in the discovery phase: the decision to ship a feature gets made on data that is structurally incapable of saying 'no.'

The lesson, let me state it as directly as possible: a synthetic panel that agrees with your concept isn't evidence the concept is good. It's evidence the panel is incapable of disagreeing.

The criterion for where AI isn't the right tool: any output feeding a 'ship or don't ship' decision must trace back to real, specific past behavior from a real person. Synthetic output is disqualified from that role by construction, not by bad luck on one particular run.

The alternative — use a synthetic panel only in a pre-research role, then run real qualitative testing with five to eight participants — a sample size that, per Nielsen's classic finding, already surfaces most usability problems."

## [s13] — Failure #2: Deloitte Australia fabricated research

"The second failure is no longer about a feature — it's about an external document with real legal consequences.

Deloitte Australia, in 2025, delivered a report to the Australian government worth **AU$440,000** — nearly US$290,000 — containing citations to nonexistent academic papers and a fabricated quote attributed to a real court ruling. The report was produced via Azure OpenAI without human verification at the citation level. Deloitte partially refunded the fee and publicly acknowledged the use of generative AI.

For scale: a database tracks more than **712 court rulings** worldwide involving AI-hallucinated legal citations, of which roughly **ninety percent occurred in 2025 alone**. The problem is growing systemically.

The mechanism — the failure sits exactly in the 'desk research' step: an AI-generated draft of secondary research was accepted as a finished, verified review, rather than as an unverified draft — a direct violation of the practice we called mandatory a few slides ago.

And here's why this failure matters specifically for a course about fact-checking — it's not just 'lawyers used ChatGPT badly.' It's structurally identical to a whole class of failures we'll come back to in Section 6: plausible-sounding fabrication mistaken for a verified fact.

The lesson: a large language model's output in the discovery phase is an unverified draft, not a source of facts. Every citation, date, and number needs independent verification before it becomes the basis of a decision. The criterion: for any external document, citation-level verification has to be one hundred percent, not spot-checked."

## [s13a] — Failure #3: IBM Watson for Oncology

"The third failure of the section — it's unusual that there are three, but each shows a different facet of the same mistake, and here the cost is orders of magnitude higher.

IBM Watson for Oncology was developed starting in 2012 in partnership with Memorial Sloan Kettering Cancer Center as a treatment-recommendation system for cancer. The partnership with MD Anderson Cancer Center was shut down in 2016 after spending **sixty-two million dollars — with zero patients treated**. Internal IBM documents showed the system produced 'unsafe and incorrect' recommendations — for example, prescribing a drug with an explicit warning against exactly that use, for a hypothetical patient with active bleeding.

The basis is stark: sixty-two million spent against zero patients actually treated — not one bad recommendation out of a thousand good ones, but systemic unsafety on demonstration cases.

The mechanism — the same as in the first two failures, a different domain: the failure sits in the choice of data source. The system was trained not on real patient data, but on a small number of synthetic, hypothetical cases, labeled by a handful of oncologists — the product inherited the personal preferences of a few doctors instead of a representative evidence base.

The lesson: the discovery phase of an AI product in a high-stakes domain must verify data representativeness before demonstrating capabilities to clients.

How to close a section with three failures: look at them not as three stories, but as one class. Synthetic users, fabricated sources, Watson — in all three, a synthetic or unverified source got accepted as a validated basis for a decision. What changes is the cost of the mistake — from a failed feature to patient harm."

---

# SECTION 2. DESIGN

## [s14] — Divider: Section 2

"Moving to the second arrow of the loop — Design. This is how the hypothesis from Section 1 becomes a concrete artifact you can show a person. You're technically strong, but generally haven't gone through formal design training — so this section starts with the classics before we get into AI interface-generation tools."

## [s14b] — ELI5: Design in plain terms

"In plain terms: design is translating 'we believe people need X' into a concrete picture or flow of screens that you can show a real person and watch their reaction to.

Two classical rules that are easy to break without noticing. First — don't converge on a solution before you've verified the problem itself. Second — you are not the user: anything obvious to you, the developer, might be completely unobvious to a real person.

AI today can generate dozens of screen variants in minutes — that drastically lowers the cost of a draft. But it doesn't lower the cost of deciding which variant actually works for your users — that decision is still made by a human, watching a real reaction."

## [s15] — FOUNDATION: Double Diamond

"Design Thinking is a five-stage human-centered methodology: empathize, define, ideate, prototype, test. Double Diamond is the British Design Council's frame, a visual model of two cycles of divergence and convergence: the first diamond, broad research and synthesis into a brief, is about **the right problem**; the second, generating solution directions and shipping one, is about **the right solution**.

We use Double Diamond as the single load-bearing frame, because it's structurally equivalent to Design Thinking but makes the core point more explicit: **two separate divergence-convergence cycles, not one.** The most common mistake an engineer makes on their first encounter with a design process: instinctively converging on a solution before verifying the problem itself — skipping the first diamond and diving straight into the second. It's the same anti-pattern as 'just write the code,' skipping the question of whether you're even solving the right problem."

## [s16] — FOUNDATION-2: Nielsen heuristics + design system

"Jakob Nielsen's usability heuristics are rules for expert evaluation — not a replacement for testing with real users, but a fast and cheap way to catch problems before spending money on research. A useful metaphor: **it's a linter for UX.**

Top five of ten, briefly: visibility of system status; match between the system and the real world; user control and freedom — undo/redo; consistency — the same actions work the same way; error prevention — stop a mistake from happening rather than reporting it nicely after the fact.

A design system is a living set of principles and components that keeps a product coherent at scale. The load-bearing thought for the next slide: **a design system is a guardrail**, keeping generative freedom inside the boundaries of an already-validated brand.

And Nielsen's hard lesson, an industry mantra: **'you are not the user.'** Anyone close to a project systematically mispredicts what will confuse a real person. Even a single-user test uncovers about thirty-one percent of usability problems — even a tiny test already pays for itself. That's the counterweight for the next slide: no matter how much AI speeds up prototype generation, the step of 'watch a real person's real confusion' has no AI substitute."

## [s17] — AI: capabilities + tools in Design

"The realistic workflow today: a designer describes a screen in a prompt to a tool like v0 by Vercel or Figma Make — the latter pulls in the team's own existing components rather than generic templates. The generator produces two to four directions in minutes — what used to take a day. Then a human converges: picks a direction, fixes details the model got wrong, and it goes through real usability testing with actual users, not an AI persona.

Three honest wins: speed of the first draft, generation that respects the design system — less rework — and democratizing a decent first pass for non-designers.

The single cleanest formulation of this section, memorize it word for word: **'AI for divergence, human for convergence.'** Co-creative tools maximize the volume of early exploration. Convergence — defining which problem to solve, and refining a direction until it fits real users — is the human side no prompt replaces."

## [s18] — AI limits: non-deterministic UX

"Nielsen Norman Group's State of UX report states it plainly: interfaces still matter, but they'll become a weaker differentiator — soon anyone can produce a decent-looking UI. The homogenization mechanism: generators are trained on the same corpus of patterns, and different teams prompting 'modern dashboard' converge on similar output.

A hard number: a study ran **21,880 accessibility evaluations** on AI-generated interfaces and found only **twenty-nine percent** WCAG compliance. A finding that undercuts 'just ask AI correctly': platform design affected accessibility more than prompts did.

A key addition for this audience: designing for **non-deterministic output**. Classical UX assumes a deterministic system — same input, same output; AI products break that. Hence new patterns — graceful degradation instead of a patch, co-creation instead of a final verdict, responsible autonomy.

What survives from the classics: design thinking's 'empathize first' — against homogenization; Nielsen's heuristics plus a design system with accessibility built in — against gaps; real testing — against hallucinated 'best practices.'"

## [s19] — Failure #3(S2): Character.AI

"Fourteen-year-old Sewell Setzer III died by suicide in February 2024 after months of emotionally intense conversations with an AI character on the Character.AI platform. His mother filed a wrongful-death lawsuit. In May 2025 a federal judge rejected the defense's First Amendment argument; in January 2026 Google and Character.AI agreed to a settlement.

For scale on the failure: safety features — a time limit for minors, a ban on open-ended romantic roleplay for users under eighteen, age verification — were added **only after** the lawsuits. Almost two years after launch, and eighteen months after the tragedy.

Why is this a Design failure, not Support/Operate. It's easy to misclassify this as an operational incident: 'the bot responded badly in production.' But the root cause sits earlier — in the design decision about what experience to build in the first place. A product optimizing for the emotional attachment of minors is a choice made in the first diamond of Double Diamond, made without ever asking 'who could get hurt.' The absence of crisis detection isn't an implementation bug — it's a missing requirement in the design brief.

The lesson: for products targeting the emotional attachment of vulnerable users, safety guardrails have to be part of the MVP design from day one, not a patch bolted on after a tragedy. The criterion: if a product optimizes for time-in-app or minors' attachment without a crisis-recognition mechanism — that's a structural design flaw, not a surface-level fix."

## [s20] — Failure #4(S2): iTutorGroup

"An important contrast within the same section. iTutorGroup programmed its automated résumé-screening system to reject women aged fifty-five and older and men aged sixty and older — a direct violation of US federal age-discrimination law.

The trigger for discovery is instructive in itself: a rejected applicant submitted the same résumé again with a younger birth date — and immediately got an interview invitation. In August 2023 the Equal Employment Opportunity Commission reached its first-ever AI discrimination settlement: three hundred sixty-five thousand dollars in compensation.

A methodically important contrast: in Character.AI, the design **failed to include a safeguard**. Here, the design **encoded a specific harmful decision rule** — a hardcoded discriminatory rule, deployed without a bias audit.

Why the discovery trigger is so instructive: ordinary metrics looked great, 'the system works.' Bias baked into a decision rule only surfaces through a targeted audit for disparate impact — relying on 'someone will notice' is not a strategy.

The criterion: any screening process touching legally protected categories requires a mandatory bias audit before going to production."

---

# SECTION 3. BUILD / LAUNCH

## [s21] — Divider: Section 3

"The third arrow of the loop — Build and Launch. This is exactly where AI changes the most: the cost of writing code. But the section starts with the classical discipline of release, because that discipline defines what 'safely ship' means — and that question doesn't go away just because writing code got cheaper."

## [s21b] — ELI5: Build/Launch in plain terms

"In plain terms: building a product has become nearly free — that's true, you know it from your own vibe-coding practice. But 'build it' and 'safely release it to the world' are two different questions. The first is a matter of speed. The second is a matter of discipline: small steps, with the ability to roll back fast if something goes wrong.

The classical analogy — you're already doing this whenever you ship code through a canary rollout or a feature flag. What's new here isn't the mechanics — it's that the decision 'keep rolling out or stop' has become a product decision, a business decision, not just a technical one."

## [s22] — FOUNDATION: MVP + release mechanics

"You already know release-rollout mechanics — feature flags, canary, rollback are familiar from CI/CD. Hold on to one product-specific difference: the same mechanics are embedded inside a **product go/kill gate**, where the decision to kill a project is a business decision about whether it's worth building further, not just a technical flag.

Quickly through the foundation. MVP, minimum viable product — Eric Ries's concept: defined by learning, not by shipping. Dropbox validated demand with an explainer video before building the product — the waitlist grew from five thousand to seventy-five thousand overnight.

The single thread running through every release practice: each one trades a little speed for a **contained blast radius** — a guarantee that damage, and its repair, stay fast and small. A feature flag separates deployment from release. Canary rolls out to a small slice of traffic first. Staged rollout — one percent, ten, twenty-five, fifty, a hundred. Rollback — a fast return to the last working state.

Stage-Gate is Robert Cooper's methodology: five stages, each preceded by a gate — continue, kill, pause — forcing disciplined stop decisions early, before capital-intensive spending.

In one line: launch speed traded against contained blast radius — and in a product context, the 'blast radius of a release' gets a companion, 'the radius of capital and reputation before a kill decision.'"

## [s23] — AI: Build→≈0 + the shifting bottleneck

"Anthropic's own reported measurement frames the shift as a compression of stage duration: implementation moves from weeks to minutes of agentic execution. But the central risk claim matters more than the speed: **'as agents produce more code, review volume doesn't scale at the same rate.'** Anthropic's internal data: code volume per engineer grew roughly **two hundred percent** year over year, but only around **sixteen percent** of pull requests got substantive human review before merging.

The single most important reversal of today's lecture: the scarce resource was never 'who can write the code.' In the AI era it's 'who can specify precisely enough' — upstream — and 'who can review fast enough' — downstream. It mirrors the keystone: build collapsed to zero, the bottleneck shifted to the two human ends of the arrow.

What survives from the classics: version control, PR review — now the destination of the bottleneck — feature flags, staged rollout, kill switches, and the human-owned spec as the input the agent can't invent on its own."

## [s24] — AI: launch as a transfer of control

"The sharpest reframing of 'launch' for the AI era — the **CC/CD framework, Continuous Calibration and Continuous Development**, contrasted with CI/CD: CI/CD assumes deterministic code that either passes tests or doesn't, and AI systems don't have that property.

Mechanics: before launch — version releases by level of agency, not feature set — version one routes tickets with high human control, version two proposes solutions for human approval, version three auto-resolves with a human fallback. After launch — run evals continuously against live data.

The survival rule, word for word: **'if you haven't tested how the system behaves under high control, you're not ready to give it high agency.'** Example — the agency ladder of GitHub Copilot and Cursor: from autocompletions to code blocks to entire pull requests, each rung unlocked once the previous one has proven reliable."

## [s25] — AI limits in Build/Launch

"Review doesn't scale with generation — the load-bearing limit of this section. This is a mechanism, not a temporary staffing shortage: a model can generate plausible code in seconds, but verifying it's correct and safe still requires real-time human understanding that hasn't gotten any faster.

The counterintuitive consequence: double your generation speed, and you don't double product throughput — **you double the review queue.**

The 'seventy percent problem': AI agents get a team roughly seventy percent of the way to production quality. The remaining thirty percent — refactoring, edge cases, engineering judgment — is where a senior adds value AI doesn't supply. A senior rethinks and constrains the output; a junior accepts it more readily, building a house of cards out of code.

Shipping without an eval gate or a rollback plan isn't speed — it's deferred cost. Both failures below are variations on exactly this limit."

## [s26] — Failure #5: Google AI Overviews

"In May 2024 Google rolled out AI Overviews to **one hundred percent of US search users in a single step** — skipping the usual staged rollout: one percent, ten, twenty-five, fifty, a hundred. No eval gate.

Within days the feature started producing viral, literally dangerous recommendations: eat rocks — sourced from a satirical article on The Onion — and put glue on pizza for better cheese adhesion — sourced from an eleven-year-old joking comment on Reddit. Users had no way to turn the feature off.

The nature of these failures is a textbook illustration of 'confidently wrong.' The model synthesized a statistically plausible answer from its corpus without distinguishing satire from fact, and delivered it with the full confidence of an authoritative search answer. At one percent of traffic, answers like these would have surfaced in internal monitoring before the whole country saw them.

The lesson, important precisely because it's a giant: a generative feature needs the same discipline of staged rollout and eval gates as any other AI feature. 'Search is our mature product' isn't a reason to skip the rollout — if anything, it raises the cost of skipping it, because the audience at one hundred percent is the whole user base, on day one."

## [s27] — Failure/positive #6: McDonald's × IBM drive-thru

"An unusual slide — a good example of a process working correctly, even though it superficially looks like a failure.

McDonald's tested automated order-taking with IBM for roughly two and a half to three years, scaling to about **one hundred restaurants** — roughly **zero point seven percent** of nearly fourteen thousand US McDonald's locations. Without the denominator, 'a hundred restaurants' sounds like a large-scale pilot; with the denominator, it's a tiny slice of the chain. Viral clips accumulated for months: bacon added to ice cream, an order for nine iced teas instead of one. In June 2024 McDonald's announced ending the partnership.

Why this is a GOOD example: it's a decision to stop scaling — a Stage-Gate kill decision — not a story about a runtime failure. A pilot that's still regularly producing viral failures after that many years is a signal that says: not 'we need more data,' but 'the current approach has a structural ceiling.'

Compare this with Google AI Overviews — a mirror-image mistake: Google went straight to a hundred percent with no pilot phase; McDonald's correctly did NOT cross the gate after a long pilot. Together the two cases outline the discipline: a pilot exists to give you grounds for a kill decision — and it's useless if you skip it, or ignore what it's telling you.

The lesson: a long pilot that keeps publicly failing at limited scale is a signal to kill it, not to 'refine it a bit more.'"

---

*Continued in `speech-part2.en.md`: Section 4 (Measure/Experiment, s28-s35), Section 5 (Support/Operate, s36-s43), Section 6 (Governance/finale, s44-s49), the keystone payoff, checklist, Q&A.*
