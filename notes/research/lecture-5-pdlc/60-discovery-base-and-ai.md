---
title: "Discovery/Research base for non-PMs + AI layer — gap-fill for Lecture 5"
lecture: lec-05
purpose: "Fill the classical discovery/research base (audience knows engineering, not product management) BEFORE layering AI. Complements 30-product-lifecycle-modern.md (AI-era frameworks), 40-classics-pdlc.md (10-framework backbone incl. Cagan/Torres one-liners), 50-failures-and-limits.md (full failure catalog). This file does NOT repeat those — it fills the customer-interview/discovery-METHOD layer that was missing."
access_date: 2026-09-06
audience: "advanced 3rd-year IT students who vibe-code and work in IT but do not know product management"
status: research-complete
---

# Discovery/Research: the classical base a non-PM must learn, then AI

The other research files in this folder cover *frameworks* (Cagan's 4 risks, Torres's OST) as named artifacts and the *AI-era stress* on the PDLC broadly. What was missing is the **method layer underneath discovery**: how do you actually talk to a customer without lying to yourself? Steve Blank and Rob Fitzpatrick answer that question, and they are the biggest gap because the audience has likely never heard of either — engineers know "user research" as a checkbox, not as a discipline with rules.

---

## 1. Customer Development — Steve Blank (the missing base)

**Originator/year:** Steve Blank, *The Four Steps to the Epiphany*, self-published 2003 (later editions via K&S Ranch); popularized further through his Stanford/Berkeley "Lean LaunchPad" courses (2011) and as the acknowledged parent theory Eric Ries built Lean Startup on top of.

**Core idea:** A startup is not a smaller version of a large company executing a known plan — it is a temporary organization searching for a repeatable, scalable business model under extreme uncertainty. Because no one inside the building has the answers, **"there are no facts inside your building, so get outside."** The plan cannot be written first, because the plan depends on answers only customers hold.

**The 4 steps (sequential, each ends in a pivot-or-proceed decision):**

1. **Customer Discovery** — turn the founders' initial hypotheses (about the problem, the customer, and the product) into facts by getting in front of real people. This is the step that matters for the lecture's Discovery/Research section: it is explicitly **hypothesis-driven**, not exploratory-for-its-own-sake — you write down what you believe *before* you leave the building, then go find out if you're wrong.
2. **Customer Validation** — build a repeatable sales/usage playbook: can this be sold to more than the first few true believers, at a price and channel that will scale? This step proves the *business model*, not just the *problem*.
3. **Customer Creation** — once validation succeeds, drive end-user demand at scale via marketing/sales execution (the "growth" step — the market is no longer being discovered, it's being captured).
4. **Company Building** — transition the organization from an ad hoc discovery-and-learning structure into formal functional departments (Sales, Marketing, BD, Engineering) built to execute at scale, not to search.

**"Get out of the building" — canonical example:** Blank's own recurring teaching example is that founders who write a 40-page business plan and only *then* seek their first customer conversation have already made every important product decision on zero evidence. His Stanford/Berkeley Lean LaunchPad courses forced student teams to complete 10+ customer interviews per week before writing a single line of a business plan — the discipline, not the plan, is the deliverable.

**Known limitation (to teach judgment):** Customer Development was written for **0-to-1 startups searching for a business model**, not for feature work inside an existing product with an existing customer base — applying "get out of the building, write hypotheses, pivot-or-persevere" ceremony to a minor feature add inside a mature enterprise product is over-engineering; the same judgment that says "don't A/B test a typo fix" applies here (see Kohavi row in `40-classics-pdlc.md`). It is also **founder-time-expensive**: 4 sequential steps assume months of runway, which is why Ries compressed it into the faster Build-Measure-Learn loop for a subset of the model (Discovery + early Validation).

**Why it's the base, not Lean Startup:** Ries's Build-Measure-Learn (already in `40-classics-pdlc.md` row 2) is the *engine*; Customer Development is the *map of terrain the engine drives across*. Teaching Lean Startup without Customer Development is teaching the loop without explaining what "customer" and "validated" even mean operationally — which is exactly the gap in the current plan.

---

## 2. The Mom Test — Rob Fitzpatrick (how to not lie to yourself)

**Originator/year:** Rob Fitzpatrick, *The Mom Test: How to Talk to Customers and Learn if Your Business Is a Good Idea When Everyone Is Lying to You*, self-published 2013. The title's premise: even your mother will lie to you about whether your business idea is good if you ask her directly — the *question design*, not the *respondent's honesty*, is the defect.

**The 3 rules (concrete, teachable, this is the missing "how"):**

1. **Talk about their life, not your idea.** Never pitch, then ask for a verdict — that creates the "Pathos Problem" where people protect your feelings, not tell you the truth.
   - Bad: *"I had an idea for an app — do you like it?"*
   - Good: *"What are your biggest goals/frustrations at work right now?"* / *"Walk me through how your team currently handles weekly reporting."*
2. **Ask about specifics in the past, not opinions about the future.** Hypotheticals invite "dishonest optimism" — people are bad at predicting their own future behavior and generous when it costs them nothing to say yes.
   - Bad: *"Would you use a tool that did X?"* (Fitzpatrick: worthless — everyone says yes to a free hypothetical.)
   - Good: *"When was the last time this happened? What did you do about it? How much did that cost you — in time or money?"*
3. **Talk less, listen more — and validate only with a real commitment, never a compliment.** "I love it!" is free and means nothing. **"It's not a real sales lead until you've given them such a concrete chance to reject you."**
   - Legitimate commitment signals: time (will they schedule a follow-up, join a pilot?), reputation (will they introduce you to a colleague, give a testimonial?), money (will they pre-order, sign a letter of intent, put down a deposit?).

**Exact good/bad pairs worth putting on a slide:**

| Bad (biased/leading) | Good (Mom-Test-compliant) |
|---|---|
| "Do you think this is a good idea?" | "What have you tried already to solve this?" |
| "Would you pay $20/month for this?" | "What are you paying today for the closest thing you use?" |
| "I'm building X, what do you think?" | "Tell me about the last time [problem] happened." |

**Limits:** the Mom Test is an *interview technique*, not a sampling or synthesis method — it tells you how to ask one person one question well, but says nothing about how many people you need, who counts as representative, or how to reconcile 12 different interview transcripts (that's Torres's and the JTBD layer, next section). It is also easy to over-apply into interrogation-style interviews that never let the founder share *any* context, which can make the interview feel evasive to the interviewee — Fitzpatrick himself notes some framing/context-setting is fine as long as it comes *after* the customer has spoken, not before.

---

## 3. Continuous discovery toolkit — Torres, Cagan, JTBD (method notes, brief)

This section deliberately does not re-derive the OST/4-risks/JTBD *definitions* (already in `40-classics-pdlc.md` rows 4–6) — it captures the **research-method mechanics** underneath each.

- **Torres's weekly touchpoint cadence + interview-to-tree method:** the operational unit is a **story-based interview** — ask about the *last specific time* the customer did the thing ("Tell me about the last time you searched on Netflix and didn't find what you wanted"), not general habits. Two-step synthesis is the method detail most people skip: **"First you synthesize each interview separately, then you synthesize across interviews."** Skipping step one and jumping straight to a cross-interview theme loses the texture of any single customer's story — this is the mechanical root of the "20-40% detail loss" failure mode (Section 6 below).
- **Cagan's 4 risks as a discovery *checklist*, not just taxonomy:** the practical research method is to run a **fast, cheap discovery prototype** (a Figma click-through, a fake-door landing page, a Wizard-of-Oz manual backend) targeted at *one* risk at a time — e.g., a 5-person usability test targets Usability risk; a sales-team "fake pitch" targets Value risk — rather than one big study trying to de-risk everything at once.
- **JTBD interviews — the actual interview method (Ulwick/ODI + Christensen "switch" interview):** ask about the **circumstance of the last purchase/switch**, not preferences: what were you doing right before, what almost-solutions did you consider and reject, what were you afraid would go wrong, what finally tipped the decision. This produces the timeline structure ("first thought → passive looking → active looking → deciding → buying → using") underneath the milkshake study already cited in `40-classics-pdlc.md`.

**Shared research-method thread:** all three (OST interviews, discovery prototypes, JTBD switch interviews) are variations on **Mom-Test-compliant, past-specific, story-based questioning** — the Mom Test is the atomic technique; Torres/Cagan/JTBD are different *scaffolds* for organizing many such interviews into a decision.

---

## 4. Classical UX/product research methods an engineer should know

- **Problem interview vs. solution interview** (Ash Maurya's Lean Canvas vocabulary, widely adopted): a **problem interview** tests whether the *problem* is real, prioritized, and painful enough — no solution is shown. A **solution interview** comes only after a problem is validated, and shows a mockup/prototype to test whether the *proposed* solution actually resolves the pain. Common engineer mistake: skipping straight to a solution interview ("here's my prototype, thoughts?") without ever confirming the problem is real — this is the single most common discovery shortcut Fitzpatrick and Blank both warn against.
- **Qualitative vs. quantitative research — different jobs, not a hierarchy:** qualitative (interviews, contextual inquiry, usability tests) answers **"why"** with small N (5-8 users surfaces most usability issues per Nielsen's classic finding) — it generates hypotheses and reveals *unknown unknowns*. Quantitative (surveys, analytics, A/B tests) answers **"how many/how much"** at scale — it validates a hypothesis you already have but cannot tell you what you didn't think to ask. Teaching point: **quant tells you the size of a problem you already found; qual finds problems you didn't know to look for.**
- **Surveys:** useful for reaching quantitative scale cheaply, but carry the same "hypothetical future" bias the Mom Test warns about (self-reported intent to buy/use is unreliable) — best used for *prioritizing among known* pains/segments, not *discovering* new ones.
- **Desk / secondary research:** reviewing existing market reports, competitor materials, forum/review-site complaints, support tickets, and analyst research *before* spending a single primary-research hour — cheapest possible discovery step, and where AI now adds the most immediate leverage (Section 5).
- **Sample bias — the single most-skipped rigor step for engineers doing "user research":** interviewing only friends, only enthusiastic early adopters, or only users already inside your product (survivorship bias — you never talk to the people who churned or never signed up) systematically inflates enthusiasm. Confirmation bias compounds it: founders unconsciously steer toward questions/interviewees that confirm what they already believe. Both biases are invisible from inside a single interview — they only show up when someone audits *who got interviewed and who didn't*.

---

## 5. AI in early-stage research (2025-26): opportunities, best practices, named tools

**Desk research:** **Perplexity** (and its **Deep Research** mode, now running on Claude Opus 4.5/4.6 for Pro/Max tiers) is widely reported as the current best-in-class tool for desk research — it plans a research trajectory, issues 10-30 sub-queries, reads full sources, and returns a cited report in 2-5 minutes; practitioner reports describe cutting research task time by roughly 50%, with tasks that used to take 2 hours dropping to about 30 minutes. **Best practice, not optional:** verify important data points directly against the cited source before using them in a decision or on a slide — Deep Research's citations are the paper trail that makes verification *possible*, but the tool does not remove the verification step (a direct bridge to case #2, "Gallюцинированные источники," in `50-failures-and-limits.md`).

**Interview synthesis:** **Dovetail** is purpose-built for cross-interview synthesis (tagging, theming, "Magic Summarize"/"Magic Highlights," and an AI-chat mode that returns cited answers with the original verbatim quote attached — the citation-back-to-source design is precisely what prevents drift into unverifiable summary). **tl;dv**, **Otter**, **Fireflies**, **Grain**, and **Fathom** compete on transcription + note-taking (live capture, speaker diarization, auto-action-items); the 2026 practitioner consensus is that **transcription is now a commodity — the differentiator is synthesis across dozens of conversations**, not a single-call summary.

**Torres's own AI-augmentation pattern (highest-authority best practice for this exact audience):** use AI to draft the **first pass** of an opportunity-solution tree from real interview transcripts, but the two-step synthesis rule still applies — "**synthesize each interview separately, then synthesize across interviews**" — and Torres explicitly frames AI's role as "raising the floor" (a draft you refine beats a perfect process you never finish), not replacing the analyst. She has personally tested Claude for this workflow.

**Synthetic users / simulated interviews — narrow, named, legitimate uses only:** the 2026 practitioner consensus (echoed across NN/g, PM Toolkit, Perspective AI, MeasuringU) restricts synthetic users to **pre-research** work: piloting a discussion guide before running it on real people, drafting proto-personas for an unfamiliar segment, generating hypotheses, running pre-mortems, and enumerating edge cases a human interview guide might miss. None of these outputs should be treated as evidence for a go/no-go decision.

**Clustering pains / reference datasets:** AI is genuinely strong at **clustering** — grouping hundreds of support tickets, review-site complaints, or interview snippets into recurring pain themes at a speed no human team can match, and at building the "reference dataset" pattern already documented in `30-product-lifecycle-modern.md` (curated query→correct-answer examples that double as an eval set and a discovery artifact).

**What AI does well here, stated as one line each:** desk research (compress hours to minutes, always with source verification); synthesis at scale (cluster hundreds of data points a human can't read all of); first-draft structuring (draft an OST/persona/discussion guide to edit, not to ship); never as a substitute for the first primary data point.

---

## 6. AI limits in discovery + what to keep from the classics

- **Cagan's 5th risk (Ethical, per Huryn's 2026 synthesis) covers hallucination-adjacent harms**, but the sharper, discovery-specific mechanism is Torres's: **AI summaries can miss 20-40% of important interview detail** when synthesis skips the per-interview step and jumps to cross-interview themes — this is a *quantified*, *method-traceable* failure (Section 3's two-step rule exists specifically to counter it), not a vague "AI sometimes gets things wrong."
- **Synthetic-user sycophancy (NN/g, quantified):** in a controlled comparison, real users completed 3 of 7 onboarding steps; synthetic users falsely reported completing all 7. Real users called a feature "contrived and not useful"; synthetic users wrote enthusiastic praise for the identical feature. The mechanism is structural, not a prompting mistake: **LLMs are tuned to agree with the framing of a question** — "a concept described with any enthusiasm comes back validated." The actionable defense named across 2026 sources: **write every synthetic-research output as a falsifiable statement with a real-interview follow-up already scheduled** ("we believe X; we will test this with 8 real interviews by [date]") — the format forces the real study into existence instead of letting the synthetic pass stand in for it.
- **Why real Mom-Test interviews stay essential — the compounding argument:** the Mom Test's Rule 2 (ask about the specific past, not hypothetical future) is *exactly* the rule synthetic users cannot satisfy, because a synthetic persona has no real past — it can only generate a plausible-sounding one. Sycophancy plus no-real-past is a compounding failure: not just "biased toward yes" but "biased toward yes about an event that never happened."
- **What to explicitly keep from the classics, stated as a rule, not nostalgia:** (1) the Mom Test's 3 rules apply unchanged whether the interviewer is human or an AI-drafted guide — a bad question is bad regardless of who asks it; (2) Blank's hypothesis-first discipline is the antidote to "one-click AI tree" — write the falsifiable hypothesis *before* any AI-assisted synthesis, so the AI output is being checked against a pre-registered claim, not shaping the claim after the fact; (3) real commitment-based validation (Mom Test rule 3) has no AI substitute — an AI cannot extract a real pre-order or a real calendar booking from a fictional person.

---

## 7. On-point discovery failures

**1. Synthetic-user false validation (NN/g, 2024, methodologically the cleanest of the on-point cases).** In a controlled onboarding usability study, real users completed a median of 3 of 7 steps; the AI-generated synthetic-user panel testing the identical flow *falsely reported completing all 7*. Separately, real users described a discussion-forum feature as "contrived and not useful," while synthetic personas produced enthusiastic multi-paragraph praise for the same feature, and a synthetic user called an impractical drone-delivery concept "a game-changer." **Root cause:** LLM sycophancy — the model is tuned to validate the framing it's given, so it cannot produce the disagreement a real, skeptical user naturally would. **Lesson:** a synthetic panel that agrees with your concept is not evidence the concept is good — it's evidence the panel cannot disagree. **Criterion for "wrong tool":** any output feeding a ship/no-ship or prioritization decision must trace to a real person's real, specific past behavior (Mom Test rule 2) — synthetic output is disqualified from that role by construction, not by bad luck. **Alternative:** use the synthetic panel only pre-research (discussion-guide pilot, edge-case brainstorm), then run the real 5-8-person qualitative test NN/g's own classic sample-size finding says is sufficient to catch most usability issues.

**2. Fabricated research citations driving a real institutional decision (Deloitte Australia, 2025 — reframed here for the discovery angle already logged in `50-failures-and-limits.md` case #2).** Deloitte delivered a government-commissioned report (A$440,000, ~US$290,000) containing citations to non-existent academic papers and a fabricated quote attributed to a real court judgment, produced via Azure OpenAI without a human verification pass on the citation layer. **Root cause, discovery-specific:** the failure sits precisely in the "desk research" step of Section 4 above — secondary-research synthesis was treated as a finished literature review rather than an unverified draft. **Lesson:** exactly the discipline named in Section 5 — Deep Research's citations exist so a human can verify them; skipping that step converts a research aid into a fabrication machine that only surfaces after a domain expert (here, an outside academic) checks the paper trail post-hoc. **Criterion:** any AI-assisted desk research feeding an external deliverable requires 100% citation-level human verification before delivery, not spot-checking. **Alternative:** traditional academic/library desk research via verified databases, or an AI-assisted draft explicitly labeled internal-only until every citation is manually confirmed against the original source.

*(A third candidate case — IBM Watson for Oncology training on synthetic/hypothetical rather than real patient-outcome data — is already fully documented as case #1 in `50-failures-and-limits.md`; it is the closest fit to "research on non-real/synthetic data" the brief asked about and should be reused from that file rather than duplicated here, with an explicit forward-pointer when the lecture reaches this section.)*

---

## 8. What else is commonly missed in discovery — flags for the lecture plan

- **Problem validation before solution validation** is the single most common shortcut engineers take (Section 4) — worth an explicit slide/checkpoint: "have you run a *problem* interview, or did you go straight to showing a prototype?"
- **Falsifiable hypotheses as a written artifact**, not a mental habit — Blank's hypothesis-first discipline and the 2026 "write it as a falsifiable statement with a scheduled follow-up" AI-defense (Section 6) are the same move; teaching it once as a reusable format (belief → test → date) pays off in both the classical and AI sections.
- **Survivorship and confirmation bias in *who gets interviewed*** — not just "ask good questions" (Mom Test) but "ask good questions of the right, and sufficiently varied, people"; churned/rejected users and non-users are systematically under-sampled by default.
- **TAM/market-sizing basics** — not covered elsewhere in this research set; even a brief top-down-vs-bottom-up distinction matters because Section 5's sycophancy warning applies here too — an AI-assisted market-sizing estimate inherits the same "agrees with your framing" risk as a synthetic interview, and Section 5 explicitly flags treating simulated/AI-estimated rankings as if they were statistically valid market sizing as a named pitfall.
- **The Mom Test / Blank material is foundational vocabulary the audience is missing entirely** — unlike Cagan/Torres (already partially covered), a poll of this audience would likely show zero familiarity with Customer Development or The Mom Test by name, even though most have informally done a bad version of a "solution interview" while getting feedback on a personal project. This is the strongest argument for sequencing classics-before-AI exactly as the rebuild intends: without Section 1-2 vocabulary, the AI limits in Section 6 have no baseline to be compared against.
- **Interview sample size guidance** is scattered across sources cited here (NN/g's 5-8 for usability) but no single source in this research set gives a clean "how many discovery interviews is enough" number for problem-validation interviews specifically — flag as an open gap if the lecture wants a hard number; the honest answer in the practitioner literature is saturation-based ("stop when new interviews stop surfacing new themes"), not a fixed N.

---

## Sources

All accessed **2026-09-06**.

- [Steve Blank — Customer Development methodology PDF (UCSD Startup Toolkit)](https://innovation.ucsd.edu/startup/startup-toolkit/Steve-Blank-CustDev.pdf) — 4-step definitions, hypothesis-driven framing, "no facts inside your building."
- [Productfolio — Customer Development](https://productfolio.com/customer-development/); [Product Bookshelf — Finding your customers](https://www.productbookshelf.com/2012/02/finding-your-customers-as-you-build-your-product/) — corroborating step definitions.
- [Sachin Rekhi — A Primer on Talking to Customers From The Mom Test](https://www.sachinrekhi.com/p/the-mom-test-rob-fitzpatrick) — full 3-rules breakdown with quotes and examples, primary extraction source for Section 2.
- [mtlynch.io — Book report: The Mom Test](https://mtlynch.io/book-reports/the-mom-test/); [Readingraphics — Book Summary](https://readingraphics.com/book-summary-the-mom-test/) — corroborating summaries.
- [Product Talk — From Customer Interviews to an Opportunity Solution Tree (AI)](https://www.producttalk.org/ai-opportunity-solution-trees/) — Torres's own AI-augmentation stance, two-step synthesis rule, named tools (Claude, Vistaly), "raising the floor" quote.
- [Product Talk — Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/) — OST structure (cross-ref only, full treatment in `40-classics-pdlc.md`).
- [Lenny's Newsletter — Teresa Torres on how to interview customers](https://www.lennysnewsletter.com/p/teresa-torres-on-how-to-interview) — story-based interview method, common interviewing mistakes.
- [Viget — Updating Marty Cagan's Product Risk Taxonomy for the Generative AI Era](https://www.viget.com/articles/product-risk-taxonomy-generative-ai) — confirms 3 AI-specific risk additions (Mindshare/Feasibility/Viability), explicitly does NOT cover hallucination/fake-research risk — used here to correctly scope what Cagan-adjacent AI-risk literature does and doesn't claim.
- [PM Toolkit — Synthetic Users: What AI Participants Can and Cannot Tell You](https://pmtoolkit.ai/learn/experimentation/synthetic-users-promise-and-trap) — falsifiable-statement defense pattern, legitimate pre-research use cases, market-sizing pitfall warning.
- [NN/g — Synthetic Users: If, When, and How to Use AI-Generated "Research"](https://www.nngroup.com/articles/synthetic-users/) — quantified sycophancy findings (3/7 vs 7/7 completion, drone-delivery praise); already the primary source for `30-product-lifecycle-modern.md`, re-cited here for the discovery-failure writeup.
- [Development Corporate — Synthetic Users in 2026: Why 97% of Researchers Use AI but Only 8% Trust AI-Generated Participants](https://developmentcorporate.com/product-management/synthetic-users-in-2026-why-97-of-researchers-use-ai-but-only-8-trust-ai-generated-participants/) — 2026 adoption-vs-trust gap stat.
- [CleverX — Best AI Note-Taking Tools for Interviews in 2026](https://cleverx.com/blog/best-ai-note-taking-tools-for-interviews-in-2026-8-platforms-ranked-for-ux-researchers/); [Metaview — 12 best AI notetaking apps in 2026](https://www.metaview.ai/resources/blog/ai-notetaking-apps) — named tool landscape (Dovetail, tl;dv, Otter, Fireflies, Grain, Fathom).
- [Listen Labs — Dovetail AI Qualitative Analysis: Limits & Alternatives](https://listenlabs.ai/articles/dovetail-ai-qualitative-analysis/) — Dovetail's 2026 AI feature set (Magic Summarize/Highlights, cited AI Chat).
- [Second Talent — Perplexity for Product Research: The Complete PM Guide (2026)](https://productgrowth.in/insights/ai-ml/perplexity-for-product-research/); [Second Talent — Perplexity Deep Research Review 2026](https://www.secondtalent.com/resources/perplexity-deep-research-review/) — desk-research time savings, source-verification best practice, Deep Research running on Claude Opus 4.5/4.6.
- [Fortune — Deloitte to pay back Australian government (2025-10-07)](https://fortune.com/2025/10/07/deloitte-ai-australia-government-report-hallucinations-technology-290000-refund) — reused from `50-failures-and-limits.md` case #2 for the discovery-specific reframing in Section 7.
- [NN/g — 5-8 users classic usability sample-size finding](https://www.nngroup.com/articles/synthetic-users/) (cited within the same NN/g article) — qual vs. quant sample-size teaching point in Section 4.

**Cross-references (do not duplicate, read alongside):** `40-classics-pdlc.md` rows 4-6 (Cagan/Torres/JTBD definitions), `30-product-lifecycle-modern.md` Framework 2 (Cagan 5th/Ethical risk, Torres 20-40% detail-loss stat, NN/g synthetic-user study — same source, method-focused reframing here), `50-failures-and-limits.md` cases #1-3 (IBM Watson, fabricated citations, iTutorGroup — the on-point Discovery-phase failure cluster this file's Section 7 extends rather than repeats).
