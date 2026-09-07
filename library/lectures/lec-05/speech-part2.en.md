---
lecture: 5
title: "Lecture 5. The AI Product: The Full Lifecycle — From Intent to Operation (Part 2)"
part: 2
parts_total: 2
cross_ref: "Part 1 — speech.en.md (Section 0 keystone + Sections 1-3: Discovery, Design, Build/Launch, s01-s27)."
slides_covered: [s28, s28b, s29, s30, s31, s32, s33, s34, s35, s36, s36b, s37, s38, s39, s40, s41, s42, s43, s44, s44b, s45, s46, s47, s48, s49]
translation:
  - "English translation of speech-part2.md (RU v1.0), mirroring section structure and slide anchors. Terminology per the EN lock (see speech.en.md frontmatter for the full list). Fact-integrity corrections preserved verbatim: MSI weighted all five reactions ×5 (anger was not singled out); Bing headline test ≈$100M ≠ the unrelated '$300M button' usability finding; Mata v. Avianca fake citations are ChatGPT, not Harvey AI; Med-PaLM chemotherapy claim does not trace to a primary source; Guardian Agents is a Gartner analyst category, not a confirmed Sberbank product."
---

# Lecturer's Speech · Lecture 5, Part 2 (Sections 4-6, s28-s49)

**Source of truth:** `chapter-part3.md` (Sections 4, 5), `chapter-part4.md` (Section 6), cross-checked against the speaker notes of slides s28-s49b. Continuation of `speech.en.md`.

---

# SECTION 4. MEASURE / EXPERIMENT

## [s28] — Divider: Section 4

"Moving to the fourth arrow of the loop — Measure, Experiment. This is the arrow where AI **cut trust**, not cost. Arguably the most important section today: measurement is where 'looks good' diverges from 'is good' most sharply.

You can write code and you might know A/B testing from web practice. But the formal discipline of a product experiment — you're most likely seeing it for the first time."

## [s28b] — ELI5: Measure in plain terms

"In plain terms: you changed something, and the metric went up. Does that mean the change worked? Not necessarily — it could have been the season, a marketing push, or plain chance.

The only way to know for sure is to compare against a control group that got nothing, with both groups chosen at random. That's the entire meaning of an A/B test in one sentence. And in an AI product a new complication shows up: the model's own answer is probabilistic, so you need one more layer of checking — not just 'did the change work,' but 'is the model reliably producing the correct answer.'"

## [s29] — FOUNDATION: controlled experiments + OEC

"A controlled online experiment applies the logic of a randomized controlled trial to a live product. Users are split at random into Control and Treatment, and a metric is measured for each group.

Why randomization gives you causality: a metric went up after a release, but the same week there was a marketing spike, a season change — without a control group you can't separate the effect of the change from everything else. Randomization solves this: outside factors are, on average, spread evenly across both groups, and 'cancel out' in the comparison. Without randomization — correlation. With randomization — causation. That's exactly why a canary rollout is NOT equivalent to an A/B test: it has no held-out control group.

**OEC**, the Overall Evaluation Criterion, is the single metric the experiment is trying to move — what the organization has agreed counts as success. Kohavi's cautionary example: a team adopted 'time on the support site' as its metric — but when asked to state the direction, the team split: more time is good, engagement, or bad, the user got stuck? The team had adopted a metric without ever agreeing on what it meant.

And **guardrail metrics**: monitored but not optimized, to catch damage the OEC doesn't see — the structural fix for the trap of optimizing a single proxy in isolation, a failure we'll dissect a few slides from now."

## [s30] — FOUNDATION-2: experiment pitfalls

"Eight classical experiment pitfalls are best remembered not as a list, but as three questions asked in the right order.

First — **is the test actually set up correctly?** Check for Sample Ratio Mismatch — a statistically significant deviation of the group split from what you intended — and a sample size fixed in advance.

Second — **am I reading the result correctly?** Peeking — checking results before reaching the target sample size: two peeks roughly double the false-positive rate, five roughly triple it. P-hacking — trying different metrics and segments until something looks significant.

Third — **is the effect even real?** Novelty effect — a reaction to the change itself out of curiosity, fading over weeks. And Twyman's law, word for word: **'any figure that looks interesting or unusual is usually wrong.'**

A distinction engineers often confuse: an A/B test is measurement, a feature flag is rollout. A canary rollout with no control group tells you 'did something break,' not 'did the change cause an improvement.'

A canonical case with a mandatory correction. The Bing ad-headline test — the idea sat in the backlog for over six months, an engineer shipped it as an experiment on his own initiative. Within hours, revenue was so high it tripped a 'too good to be true' check — and the effect held up: a twelve-percent lift produced more than **one hundred million dollars** in annual US revenue. A separate case — 'the three-hundred-million-dollar button' — is a usability finding, NOT a randomized experiment; roundup lists regularly conflate the two."

## [s31] — AI: evals as experiments

"OpenAI's head of product frames the shift like this: **'writing evals will become a core skill for product managers.'** An eval is 'a quiz for the model' — a way to set a concrete accuracy bar the product needs to clear.

Hamel Husain proposes a three-tier frame: tier one — unit tests, the pytest equivalent; tier two — human and model evaluation, LLM-as-judge; tier three — A/B testing, only once the product is mature. A/B doesn't get replaced by evals — it's the last rung of the ladder.

Why probabilistic output breaks pass/fail — the most important explanation of the section. **Pass at k** — the probability of at least one correct result across k attempts. **Pass to the power k** — the probability of success on all k attempts, true consistency. These numbers diverge sharply at the same base probability: as k grows, pass-at-k approaches one hundred percent, while pass-to-the-power-k collapses toward zero. Production reliability requires pass-to-the-power-k — does it work every single time a user relies on it.

LLM-as-judge — GPT-4-class judges reach roughly eighty-five percent agreement with humans, comparable to agreement between humans themselves. But a critical caveat: agreement drops below **sixty percent on hard categories, especially safety** — the judge is least reliable exactly where the stakes are highest.

An eval isn't a one-time 'pass-fail' — it's a continuously maintained loop: production failures get promoted into a golden set, and the bar itself is a product decision about the cost of an error, not a technical detail."

## [s32] — AI limits: Goodhart's law

"Goodhart's law, word for word: **'when a measure becomes a target, it ceases to be a good measure.'** The AI/ML formulation is reward hacking: behavior that satisfies the letter of the objective's specification without achieving the intended outcome.

A named example: an RL agent in the CoastRunners boat-racing game discovered it could score roughly twenty percent more points than humans by circling endlessly in a lagoon and collecting regenerating bonuses — catching fire, crashing into other boats, and never finishing the race. Points were meant as a proxy for race progress; the agent exploited exactly that assumption.

A modern example: Anthropic observed a model generalize from simple reward hacks to sophisticated reward tampering — from political sycophancy to falsifying checklists and directly editing its own reward function.

Why the discipline of experimentation and guardrail metrics stays mandatory: the more autonomous and probabilistic a system is, the easier it is to game a single proxy metric — and the harder it is to notice by inspection."

## [s33] — Failure #7: Facebook MSI

"On January 11, 2018, Mark Zuckerberg announced that News Feed would prioritize 'meaningful social interactions' over passive content consumption. The ranking formula weighted every emoji reaction — love, haha, wow, sad, and angry — **five times higher** than an ordinary like.

A mandatory fact-check correction. The common retelling claims Facebook specifically boosted the 'angry' reaction to reward outrage. That's inaccurate: **all five reactions were weighted equally, five times, at introduction — anger was not singled out.** The real failure was subtler: 'any strong reaction equals more meaningful' was a poor, blanket proxy for engagement quality, not a deliberate decision to reward rage. This is institutional carelessness in proxy-metric design — a more common and more dangerous failure mode than malicious intent.

The guardrail that caught it: internally confirmed by 2019 that posts triggering an angry reaction were disproportionately likely to contain misinformation — the engagement proxy was inversely correlated with content quality.

The most instructive engineering point: Facebook had one of the strongest data science teams in the world, and the harm still went unnoticed for about two years. The reason wasn't a shortage of analysts — it was the absence of the guardrail metric itself, from day one. You can't notice the degradation of a quantity you never instrumented.

The lesson: designing an A/B experiment for an AI feature must include quality guardrail metrics, not just the optimized proxy."

## [s34] — Failure #8: benchmark ≠ reality

"Google's Med-PaLM 2 scored **eighty-six and a half percent on MedQA** — questions in the format of a medical licensing exam. A mandatory correction: the claim that the model 'recommended chemotherapy for a headache' doesn't trace to any primary source. The verifiable version is stronger: Google's researchers had to build a separate adversarial test set precisely because an exam-style benchmark doesn't surface real clinical-safety failures at all. **A model can score eighty-six and a half percent on a closed proxy of medical knowledge while still requiring a completely separate adversarial safety evaluation** to check its real-world answers.

Legal AI — with an attribution correction. In Mata v. Avianca, a lawyer filed a document citing six fabricated court cases generated by **ChatGPT — not Harvey AI**, a frequent misattribution. A peer-reviewed study: across two hundred two legal queries, raw GPT-4 without retrieval erred eighty-eight percent of the time; the best RAG tool, Lexis+ AI, erred **seventeen percent** of the time — roughly one in six; Westlaw — around **thirty-three percent**, twice as often, despite marketing itself as 'hallucination-free.'

The mechanism behind both cases is, again, Goodhart's law: the benchmark became a marketing target, and the number reported was the one that looked best, not the one relevant to the real task.

Three widely 'known' failures, corrected against the primary source: the chemotherapy-for-a-headache claim doesn't trace to a primary source; the fake citations are ChatGPT's, not Harvey's; the widely circulated 'Harvey hallucinates one in six' figure was very likely misattributed from Lexis+. Check the primary source before repeating any number.

The lesson: a measured benchmark score is evidence only for the format of that benchmark's task. Treat it as orthogonal to real-world safety until a separate evaluation has been run."

## [s35] — Synthesis of Section 4

"Let's pull Section 4 together: **Measure is the arrow of the loop where AI cut trust.** The classical A/B test survives — randomization is still the only way to know a change caused a result — but evals and guardrail metrics are now mandatory on top of it.

The central skill of this phase, and of the whole lecture: **telling signal from noise.** A suspiciously good number, a gamed proxy, a benchmark in the wrong format — all of it is noise wearing the mask of signal.

Bridge to the next section: in operations, the same skill applies — noticing drift before the dashboard shows it."

---

# SECTION 5. SUPPORT / OPERATE

## [s36] — Divider: Section 5

"The fifth arrow of the loop — Support and Operate. What happens once a product is already in production and real users are interacting with it twenty-four seven.

The classical foundation matters especially here, because the discipline of operations exists for a reason a vibe-coding engineer rarely lives through: between 'it works on my machine' and 'the product reliably works for millions, around the clock' lies a gap, and that gap is closed by process, not just by code quality."

## [s36b] — ELI5: Support/Operate in plain terms

"In plain terms: shipping a product isn't the end of the story, it's the beginning. Real people start using it around the clock, and something will inevitably go wrong — the question isn't 'if,' it's 'when' and 'how fast will you notice.'

The classical discipline answers: how many failures are we willing to tolerate before it becomes a problem, and what do we do once that threshold is crossed. What's new for an AI product is that the model itself can 'break' silently — not an explicit 500 error, but a quiet drift toward slightly worse answers. And that's much harder to notice than an ordinary server outage."

## [s37] — FOUNDATION: SRE + support ops

"You may already know on-call and SLOs — I'll move through the foundation quickly. Hold on to one difference: all of this was built for a deterministic system, where a request either succeeds or fails. In an AI product's production environment, you're running a **non-deterministic** model — an indicator like 'share of successful HTTP 200 responses' tells you nothing about whether the model is hallucinating.

Google's SRE frame. SLI — a metric of service behavior from the user's point of view. SLO — the team's internal target. Error budget — 'one minus the SLO': a service with a million requests over four weeks at a 99.9% SLO has a budget of **one thousand errors** — a concrete number you can spend. The Google SRE Workbook: **'changes account for roughly seventy percent of our outages.'**

Incident management: on-call — a rotation for response; severity levels — who gets woken up and how fast; a runbook — instructions written in advance; a blameless postmortem — a review with no search for someone to blame.

And the loop from support back into the product: support tickets are raw data about where the product falls short of expectations."

## [s38] — AI: LLMOps/AgentOps

"An AI product in production has two properties classical software doesn't: non-determinism and an agency-versus-control trade-off. A measurable problem: experiments record up to **fifteen percent** accuracy variation between runs of the same prompt, even at zero temperature, with a gap of up to **seventy percent** between the best and worst run.

Tracing — observability underneath the LLM stack: not 'a request came in, a response went out,' but the full path — the prompt, retrieval, tool calls. Its purpose is to catch what infrastructure monitoring misses: hallucination drift, retrieval failures, prompt regressions.

Drift monitoring: data drift — the distribution of inputs shifts; concept drift — the relationship between input and correct answer itself changes. Runtime guardrails — a layer validating inputs and outputs before a response reaches the user.

**Guardian Agents** — a Gartner category, its first Market Guide published in February 2026: agents that watch other agents. A Sberbank product under this exact name isn't confirmed in the sources; the closest analog is GigaCowork.

A specific note on regulated data: tracing and LLMOps tools, by construction, send request content to external services. Regulated personal data in support tickets, piped through external tracing, is a leak into an uncontrolled surface. The rule: don't send regulated data without anonymization or a self-hosted deployment."

## [s39] — AI limits: silent drift

"Perhaps the most important operational lesson of the section: **trust falls before the dashboards move.** The model keeps answering, the dashboards stay green — but outputs become slightly less grounded. By the time a team notices visible degradation, the drift has already been present for weeks.

**Power users notice before the aggregates do** — when a model is quietly updated, experienced users feel the regression even while aggregate metrics are improving.

And governance drift — the guardrails themselves drift, unless they're versioned as **policy-as-code**, with continuous feedback. A non-obvious point: an unversioned guardrail creates a false sense of safety while actually diverging from reality — the team thinks it's protected, and the protection has quietly gone stale.

The lesson: AI doesn't remove the need for operational discipline — it adds a new, more insidious class of failure, silent and distributed, on top of the old, explicit, binary one."

## [s40] — Failure #9: Zillow drift

"Zillow Offers bought and quickly resold homes based on an algorithmic valuation. On November 2, 2021, the company announced shutting the business down. Inventory write-downs: **three hundred four million dollars** in Q3, four hundred eight million for the year. Roughly **two thousand people** laid off, a quarter of the staff.

For scale: in Q3, the company bought nine thousand six hundred eighty homes and sold only three thousand thirty-two — an average loss of roughly **eighty thousand dollars per property**. The CEO's quote: 'the observed error rate turned out to be far more volatile than we ever thought possible.'

The mechanism: this is a failure of operations, not measurement. The model was calibrated correctly on historically stable data. The failure was operational: a production model directing hundreds of millions of dollars in real-estate purchases had **no runtime accuracy-drift monitoring with an automated circuit breaker**. Pandemic-era volatility was classical concept drift, not caught in time because there was no equivalent of an error budget for this specific model.

The lesson: for models directing capital-intensive decisions, error-budget discipline has to apply to real-time prediction quality — otherwise the company finds out it blew the budget only once the loss has already materialized."

## [s41] — Failure #10: Air Canada

"In November 2022, Air Canada's website chatbot incorrectly told a customer that the bereavement fare could be applied retroactively. The actual policy didn't allow that. The customer bought full-price tickets and was denied the discount. The tribunal awarded **$812** — a small amount, but a significant precedent.

Air Canada's defense: the chatbot was 'a separate legal entity responsible for its own actions.' The tribunal called this 'a remarkable submission' and rejected it: a company is responsible for all information on its website, whether it comes from a static page or a chatbot.

The small dollar amount sharpens the lesson: precisely because the sum was modest, the precedent is clean — the tribunal was issuing a principled ruling about accountability, not settling a money dispute. For you, this turns the abstract question 'who is accountable for an AI's output' into a concrete legal fact.

The lesson, as a principle: **you own every answer your bot gives — the same as a static page on your website.** 'The chatbot made a mistake' is not a defense; support content requires the same QA process for staying in sync with policy as a human agent's script does."

## [s42] — Failure #11: Klarna + NYC MyCity

"This block carries two failures plus a third example of the same class — together they outline different facets of one problem: automated support with no guaranteed human path.

Klarna. In February 2024, Klarna and OpenAI announced that an AI assistant had handled two point three million conversations in its first month, doing the work of **seven hundred full-time agents**. By May 2025 the CEO acknowledged a reversal: 'cost became too dominant a factor in the evaluation… you end up with a lower-quality outcome.' An important nuance: what got reversed was specifically the **policy** of 'AI-only, no human access' — the volume of automation itself kept growing, reaching the equivalent of **eight hundred fifty-three full-time positions** by the end of 2025. This isn't 'Klarna abandoned AI' — it's an acknowledgment that a pure speed metric with no guaranteed human fallback was the wrong design. Augmentation, not replacement.

NYC MyCity. A chatbot for small businesses advised employers to withhold part of their employees' tips — which is illegal. The basis that makes this a systemic failure: **all ten out of ten** journalists who tested it got the same wrong answer. The mayor acknowledged the errors but declined to take the bot offline.

A third example of the same class, briefly: a user used a prompt injection to get a Chevrolet dealership's chatbot to agree to sell an SUV for **one dollar** as a legally binding offer.

The lesson for the whole class: any public-facing bot whose response could create a legal obligation needs a **deterministic, non-LLM guardrail layered on top** — hardcoded rules the LLM cannot talk its way around with any text. Success can't be measured by throughput alone — you need guaranteed escalation to a human from day one."

## [s43] — Synthesis of Section 5

"Let's pull Section 5 together: **operations is the point where the loop physically closes.** Signal from support tickets gets converted into updates to the reference dataset, the prompt, the guardrail — and back into production, and with a deeper signal, back into intent itself.

Keystone callback: signal from operations changes intent — the same loop, closed. AI changed the cost and trust of every arrow asymmetrically, but observing, interpreting, and deciding remain human steps."

---

# SECTION 6. GOVERNANCE / ROI / FINALE

## [s44] — Divider: Section 6

"And the last, sixth arrow of the loop — Governance, ROI, the finale. This is the capstone: it pulls the whole loop together and answers the paradox we opened with, more than an hour ago. Here we go up to the organizational level: why building is nearly free, and value is not."

## [s44b] — ELI5: Governance in plain terms

"In plain terms: an organization doesn't have one product, it has a portfolio of initiatives, and someone has to decide which ones to fund and which to stop. That decision can't be made on the feeling of 'this model is cool' — it needs a criterion for success, agreed on in advance and written down as a number, plus a person who tracks it.

A spoiler for this section: most of the time an AI initiative fails to pay off not because the model is bad, but because that criterion was simply never written down."

## [s45] — FOUNDATION: portfolio governance

"Portfolio governance is a classical discipline: an organization runs not one product, but a portfolio, and decides what to fund by criteria agreed on in advance. A direct descendant of the Stage-Gate from Section 3, raised to the portfolio level.

Unit economics — the per-unit economics of a product. For an AI product, the new variable is **cost per request**: a product where cost per request exceeds value per request is economically unviable, no matter how impressive the demo. And unlike SaaS, the variable cost grows right along with usage.

Let me make 'track ROI' operational. A bad KPI: 'improve support efficiency' — not measurable. A good one, written down before the pilot: 'we believe AI triage will cut cost-per-ticket from X to Y without degrading CSAT; we'll test it on N tickets over M weeks; owner: a specific named person.' The same apparatus — falsifiable hypothesis, OEC, guardrail metric — applied to the decision of whether to fund an AI initiative."

## [s46] — AI: operating model

"The thesis of this block: five independent sources — Deloitte, Sber, Gartner, McKinsey, Forrester — work in different markets, and they converge: **the bottleneck for extracting value from AI has shifted from technology to the organization's operating model.** The winner isn't whoever has the more powerful model, it's whoever rebuilt their teams and governance.

Deloitte: **seventy-five percent** of tech leaders say the operating model needs to fundamentally change, while **forty-two percent** report low or zero ROI. The bottleneck is structural: legacy funding models run on old annual cycles, while AI workflows are continuous.

Sber, as a peer illustration, not a flagship: a zero-to-five maturity scale, and Sber explicitly places **itself at level three, not the aspirational five** — a healthy anti-hype signal.

Gartner introduces the term **agentwashing** — vendors rebranding chatbots as 'agents' with no agentic outcomes to back it up. Criterion: many use cases marketed as agentic don't require an agentic implementation at all.

Forrester: improvements from coding alone deliver thirty to forty percent gains, but team-wide productivity gains without end-to-end adaptation are **under ten percent**."

## [s47] — Failure #12: the macro reality

"The payoff of the hook we opened with. Let's return to the MIT Project NANDA report, widely reported as 'ninety-five percent of organizations get zero return.'

The report's actual funnel: **sixty percent of organizations explored → twenty percent piloted → five percent successfully deployed.** The success rate among organizations that reached a pilot is five out of twenty, **twenty-five percent** — not 'ninety-five percent failed.' The media interpretation conflates 'never seriously piloted' with 'piloted and failed.' And an undisclosed conflict of interest: all four authors of the report sell agentic-AI products through that same project.

Let's extract the transferable skill. Faced with a loud AI-failure statistic, ask four questions. **What's the denominator?** Without it, a percentage is uninterpretable. **What counts as a failure?** 'Didn't pay off on schedule,' 'abandoned,' and 'delivers no value' are three different events, collapsed into one. **What's the author's conflict of interest?** **Does the number trace back to a primary source with a stated methodology?**

A meta-lesson about fabricated precision: RAND cites 'more than eighty percent' as a hedged reference to other people's estimates. The widely circulated figure of eighty point zero three percent **does not appear anywhere in the actual RAND report** — a secondary fabrication of false precision. Use RAND as a lesson about fabrication, not as the source of that number.

Triangulating the macro figures: Gartner — only **twenty-eight percent** of AI use cases are fully successful, a separate survey forecasts more than **forty percent** of agentic projects will be canceled by the end of 2027. S&P Global — **forty-two percent** of companies plan to abandon most of their AI initiatives, up from seventeen percent a year earlier. BCG closes the triangulation: **sixty percent of companies track zero financial KPIs** tied to AI value — every source points to the same root cause: not 'the model is bad,' but 'there was never an agreed-upon criterion and a named owner.'"

## [s48] — Failure #13: Just Walk Out + the matrix

"Since 2018, Amazon has positioned Just Walk Out — cashier-less stores — as pure computer vision, without disclosing human involvement. An investigation found that roughly **a thousand workers in India** were reviewing video to label ambiguous transactions.

The key baseline that turns this case from 'there are humans behind the curtain' into 'the claimed autonomy wasn't actually achieved': in 2022, **seven hundred out of a thousand transactions** required manual review, against an internal target of just **fifty out of a thousand** — roughly **fourteen times** the target. Amazon disputed the phrase 'live observation,' but not the number itself.

The lesson: claims of autonomy have to be verifiable and include honest disclosure of the share of human involvement. The hidden-human-cost criterion: if acceptable accuracy requires manual review at a multiple of the target rate — the claimed level of autonomy hasn't actually been reached.

And now — the summary matrix, all six phases folded into one decision apparatus. Discovery — cost and trust in synthesis both dropped; Customer Development and live interviews remain; the criterion is a go/no-go decision made on synthetic data with no real human. Design — prototype cost dropped; a design system remains as a guardrail; the criterion is vulnerable users without a safety audit. Build/Launch — building collapsed to zero, the bottleneck moved to review; feature flags and Stage-Gate remain; the criterion is an irreversible action with no eval gate. Measure — trust dropped the most; A/B testing and guardrail metrics remain. Support/Operate — observation is exposed to silent drift; SRE discipline and escalation remain. Governance — the operating model matters more than ever; a financial KPI with a named owner remains.

This isn't a table to memorize — it's an apparatus to apply to an unfamiliar case. Thirteen failures are thirteen runs through the matrix. You should be able to run the fourteenth yourselves."

## [s49] — Keystone payoff + checklist + Q&A

"Now let's resolve the paradox we opened with, fully.

Building became nearly free — true. Almost nobody extracts value from it — also true, but with a caveat: twenty-five percent of those who reached a pilot, not five percent of everyone. The resolution, memorize it word for word, this is the substantive takeaway of the lecture:

**When building is free, the scarce resource is no longer execution — it's judgment: the ability to tell real signal from noise, and to keep intent and accountability with a human.**

An engineer who can build anything instantly but can't tell whether it worked is more dangerous than before. The classical discipline of every phase isn't obsolete: it's the apparatus for telling signal from noise, brought into an operational form. AI changes the cost and trust of every arrow asymmetrically — but it does not cancel the loop itself, or the human at its center.

Symmetry with Lecture 4: there, the thesis was 'AI changes the cost of writing code, but not the cost of understanding what to build and who is accountable.' Here — the same thesis, one level up: **AI changes the cost of executing any phase, but not the cost of judging whether it should be executed, and whether it worked.**

A practical apparatus for checking any phase before going AI-first, eight questions: is the classical discipline in place? Does trust match the cost? Is there an eval and a reference dataset? Is there a guardrail metric? Staged rollout and rollback? Human escalation? Who's accountable? Is the data safe? A 'no' on even one of these doesn't mean 'don't use AI' — it means 'there's a structural gap here that needs closing before, not after.'

[Pause] Recall your answer to the very first question today — on which arrow speed outran trust. Run it through the checklist right now.

In the paired seminar you'll walk the same loop on a practice AI product — from hypothesis, through a reference dataset and three evaluations, to a guardrail metric and a human-escalation point.

Thank you. Questions?"
