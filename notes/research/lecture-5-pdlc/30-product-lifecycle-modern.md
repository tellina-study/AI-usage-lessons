# The Modern AI Product Lifecycle (2025–2026): Beyond Coding

> Research brief for Lecture 5 (PDLC). Focus: the FULL product cycle — discovery, design,
> build, launch, experimentation, support/operations, iteration — for AI-native products.
> Compiled 2026-09-06.

## Why this matters: CI/CD is the wrong mental model

The industry consensus crystallizing through 2025–2026 is that classic software product
lifecycle models — built around **deterministic specs**, **CI/CD pipelines**, and **cohort
A/B tests** — do not fit AI products, because AI products have two properties software never
had: (1) **non-determinism** (the same input can produce different, sometimes differently
*correct*, outputs), and (2) a built-in **agency/control tradeoff** (every increase in what
the system is allowed to do autonomously is a decrease in what a human directly controls).
This single structural fact — not "AI is powerful" — is the thread connecting every
framework below.

---

## Framework 1: CC/CD — Continuous Calibration / Continuous Development

**Source:** Aishwarya Reganti & Kiriti Badam, "Why your AI product needs a different
development lifecycle," published as a guest essay on **Lenny's Newsletter**, 2025-08-19.
- https://www.lennysnewsletter.com/p/why-your-ai-product-needs-a-different
- https://www.lennysnewsletter.com/p/why-your-ai-product-needs-a-different-2ea (identical
  underlying article; paywalled audio/teaser variant)

Note for attribution accuracy: the framework is authored by Reganti and Badam (drawing on
50+ AI implementations at OpenAI, Google, Amazon, Databricks, Kumo), published on Lenny's
platform. Calling it "Lenny's CC/CD framework" is common shorthand in practitioner circles
but technically imprecise — cite the actual authors in the lecture, credit the newsletter as
the distribution channel.

**Core claim:** "AI products are just built differently. The teams that realize that and
adjust the most quickly will have a huge advantage." CI/CD assumes deterministic code that
either passes or fails tests. AI systems require a six-step loop split into two phases:

- **CD (Continuous Development) — pre-launch:**
  1. *Scope capability & curate data* — version releases by **agency/control level**, not by
     feature. Example: a customer-support bot ships as v1 (routes tickets — high
     control/low agency) → v2 (suggests resolutions for human approval) → v3 (auto-resolves
     with fallback to human). Build a **reference dataset** of 20–100 examples before
     launch.
  2. *Set up the application* — build the simplest version that gives useful signal;
     engineer explicit **control handoffs** so control can be handed back to a human
     seamlessly if something goes wrong.
  3. *Design evals* — application-specific metrics (e.g., "routing accuracy"), run against
     the reference dataset before deployment (the AI-era equivalent of unit tests).

- **CC (Continuous Calibration) — post-launch:**
  4. *Run evals on live data* (sample if traffic exceeds ~3,000 interactions/period).
  5. *Analyze behavior & spot error patterns* — manually review 20–50 low-scoring examples
     per category.
  6. *Apply fixes* — iterate on prompts/model/retrieval/architecture; re-run evals on cached
     data without a full redeploy; revisit the eval design itself if it's misaligned with
     what actually goes wrong in production.

**Reference Datasets** are the operational core of "Context Engineering" in this framework:
curated (query, correct-answer, metadata) tuples that simulate real user behavior before
release. Their stated dual purpose: "helps you evaluate system performance and also tells
you what context your assistant needs to perform reliably."

**Launch as "handoff of control":** Every version change is framed as a control handoff, not
a feature ship. High-control/low-agency versions (human-in-the-loop, suggestions only) are
the safe default; agency is only increased once traces prove the system behaves well under
supervision. Real-world example cited: **GitHub Copilot / Cursor**, which climbed the
agency ladder gradually — "first completions, then blocks, then PRs, with each step earned
through usage, feedback, and iteration."

**Evals + drift replace static A/B:** The framework doesn't claim evals *replace* A/B testing
outright — it prescribes doing both, at different points: evals pre-deploy (catch known
failure modes, like unit tests), production monitoring post-deploy (catch *emerging* issues
via implicit signals: regenerations, drop-offs, mid-response edits). Recalibration is
triggered by model changes or user-behavior shifts — i.e., **data drift**.

### Named failure modes (mandatory teaching content)
- **Skipping the control ladder:** "If you haven't tested how the system behaves under high
  control, you're not ready to give it high agency." A support bot that jumps straight to
  v3 (full autonomy) risks "a chain of failures" that's hard to untangle after the fact.
- **Eval-reference mismatch:** reference datasets reflect *expected* behavior; real usage
  diverges, so evals "may miss issues or give high scores to flawed outputs."
- **Tool-chasing over judgment:** "Too many people focus almost entirely on implementation,
  chasing the latest tools and frameworks, but end up making costly mistakes."
- **Two opposite failure extremes:** eval-obsession (paralysis by measurement) vs.
  vibes-only shipping (no evals at all).
- Closing caveat undercuts any mechanical reading of the framework: "At the heart of CC/CD
  is judgment... no one-size-fits-all for how much capability to give each version."

---

## Framework 2: The Fifth Product Risk — Ethical/Hallucination Risk

**Sources:**
- Marty Cagan & Marily Nika, "AI Product Management," SVPG, 2024-04-16 —
  https://svpg.com/ai-product-management/
- Cagan, "Product Risk Taxonomy," SVPG, 2023-07-10 (reaffirms the classic 4 risks)
- Paweł Huryn, "What Is Product Discovery in the AI Era? The Ultimate Guide for PMs (2026
  Edition)," Product Compass, 2026-07-22 — https://productcompass.pm/p/product-discovery-2026
- Josh Korr, Viget, "Product Risk Taxonomy for Generative AI," 2023-08-10

**Classic 4 risks (Cagan):** Value (do customers want it), Usability (can they use it),
Feasibility (can we build it), Viability (can the business/legal/ethics sustain it).

Important nuance for the lecture: **Cagan's own SVPG essay does not cleanly promote a
standalone 5th risk** — he discusses hallucination/ethics explicitly but files it *under
Viability*: "If users misunderstand a result, or the model hallucinates in a way that
creates a danger, what are the legal and ethical ramifications?" Feasibility is reframed for
AI: "Generative AI, by its nature, is probabilistic, not deterministic." Value risk gets a
sharp warning: "many examples today of AI-products that are AI in name only."

The **cleanest citable 5-way split** comes from **Huryn's 2026 synthesis**, which separates
Ethical risk as its own axis: Value / Usability / Viability / Feasibility / **Ethical**
("Should we build it at all? Are there ethical considerations?"). Attribute this framing to
Huryn's 2026 synthesis of Cagan's work, not verbatim to Cagan — it's a defensible and citable
extension, but not identical to the SVPG source text.

### Teresa Torres: why human interviews got MORE valuable, not less

**Source:** Teresa Torres, "Don't Use Generative AI to Replace Discovery with Real Humans,"
producttalk.org (title confirmed via podcast reference; full text paywalled); Aakash Gupta's
write-up of Torres's AI discovery guide, 2025-08-12 — https://news.aakashg.com/p/teresa-torres-podcast

Key claims: "AI can't (and shouldn't) replace human customer discovery." Risks named:
AI-generated insights can mislead product decisions; synthetic personas compromise research
quality; the 2026-era failure mode for Opportunity Solution Trees is **"starving" the tree
with weak synthetic evidence** rather than drawing it incorrectly. Quantified claim: **"AI
summaries can miss 20–40% of important detail"** when synthesis happens without human
review — "relying on AI for synthesis without human review loses context and empathy."

Prescribed pattern (closest available framing to "PM as auditor of AI insights," though
Torres doesn't use that literal phrase): **"Use AI to augment your workflow, not replace it.
Let AI do drafts and repetitive tasks, but keep humans in the loop to validate, correct, and
preserve empathy."** She also names an **"Error Analysis Loop"**: log traces → human
review/tagging → identify error classes → write evals → A/B test fixes — a direct bridge to
the CC/CD eval loop above.

### Concrete documented failure: synthetic user research

**Source:** Maria Rosala & Kate Moran, Nielsen Norman Group, "Synthetic Users: If, When, and
How to Use AI-Generated 'Research'," updated 2024-06-21 —
https://www.nngroup.com/articles/synthetic-users/

This is the strongest, most concrete evidence base for the "hallucinated discovery
hypotheses" failure mode:
- **"UX without real-user research isn't UX."**
- In a usability test, real users completed 3 of 7 onboarding steps; **synthetic users
  falsely reported completing all 7.**
- Real users called a discussion-forum feature "contrived and not useful"; synthetic users
  wrote enthusiastic multi-paragraph praise for the same feature.
- A synthetic user called an impractical drone-delivery concept "a game-changer" — uniform
  sycophancy bias: "every idea is often seen as a good one."
- Synthetic personas generated 7 unranked engagement factors — "not helpful for feature
  prioritization" because they don't produce the disagreement real users would.
- A separate tree-testing study found ChatGPT "vastly outperformed most real people" — i.e.,
  **too good to be a valid stand-in** for how real users actually struggle with an
  interface.
- NN/g's recommended ceiling for synthetic users: hypothesis generation, interview-guide
  prep, proto-personas — **never** final validation, niche populations, or behavioral data.

---

## Framework 3: Orchestration & the "AI Product Flywheel" (Reforge)

**Sources:**
- Reforge, "AI Evals Aren't Optional Anymore," blog + AI Evals course page, Feb 2026 —
  https://www.reforge.com/blog/ai-evals-course / https://www.reforge.com/courses/ai-evals
  (both 403 to direct fetch; content recovered via search snippets — treat quotes as
  medium-confidence)
- Sandhya Hegde & Justin Bauer, "Building an AI Product Flywheel," 2026-01-23,
  https://blog.calibrelabs.ai/p/building-an-ai-product-flywheel (fully fetched, high
  confidence; independently corroborates and elaborates the Reforge framework)
- Reforge, "Moving to Higher Ground" — https://www.reforge.com/blog/ai-impact-product-management
- Brian Balfour (Reforge CEO), LinkedIn commentary on Andrew Ng, 2026

Kevin Weil (CPO, OpenAI), quoted by Reforge: **"Writing evals is going to become a core
skill for product managers. It is such a critical part of making a good product with AI."**
Reforge's framing: PMs are "managing a probabilistic system with deterministic tools" —
traditional user stories, bug tickets, and cohort A/B tests "break down when every user gets
a different output from the same input." The course teaches AI PRDs, an "eval-driven
roadmap," and designing automated evaluators "aligned to human judgment and product taste" —
this is the closest verbatim match to "AI metrics grading other AI components" (LLM-as-judge
calibrated against human rubrics).

**The AI Product Flywheel — five stages** (independently corroborated across Reforge and
Calibre Labs sources — treat this cross-source repetition as evidence it's now a genuine
2026 practitioner consensus, not one writer's coinage):

1. **Agent Success Rate (North Star Metric)** — composite of thumbs up/down, user actions,
   semantic conversation analysis, task feedback. The authors flag their own limitation up
   front: "significant uncertainty remains in evaluating success."
2. **Trace Analysis** — quoting Harrison Chase (LangChain): "Traces have become central
   documents in the AI development process." Sample traces mapped to primary user intents to
   surface error modes.
3. **Reference Datasets** — user-intent-mapped natural-language inputs with golden outputs
   plus edge cases (e.g., a support bot's dataset spans replacements, refunds, info
   requests, payment updates).
4. **Offline Evals** — explicitly called **"unit tests for your agent."** Critical for
   testing both prompt changes and architecture changes; acknowledged limitation: hard to
   achieve realism for long-running, multi-turn agents.
5. **User Monitoring & Feedback** — real session monitoring, support-ticket integration,
   interviews — closes the loop back to stage 1.

**Implementation guidance / limitations:** teams with large user bases should start at stage
5 (monitoring); teams with small/concentrated user bases should start at stage 2 (trace
analysis + interviews). Named failure mode: **"risk of drowning in data during robust trace
analysis."** Most teams have fragmented pieces of the flywheel (an eval here, a feedback
form there) but lack the connective tissue — organized trace coding, structured intent
mapping — which the authors identify as the *common* failure state, not the exception.

**"PM as orchestra conductor" — nuance correction.** The metaphor exists in Reforge's own
content, but its 2026 meaning has inverted from what an outside observer might assume: Reforge's
thesis is not "PM tunes AI-workers while staying a pure orchestrator" — it's that **AI turns
the PM from a pure orchestrator into a more powerful individual contributor**, using AI
coding/design tools directly. Balfour's systems-thinking caveat is the most useful teaching
point here: **"Your product output is limited by the slowest part of your system. You
accelerate one piece, you just move the bottleneck to another part."** Automating only the
PM's tasks (e.g., AI-written PRDs) does not fix throughput if engineering or design remains
the bottleneck — a direct rebuttal to naive "just add AI to the PM's job" thinking.

On "support tickets change prompts, not code": no verbatim Reforge quote with this exact
framing was found. The evidenced mechanism to cite instead is the Flywheel's stage 5→3 loop:
support tickets feed into reference-dataset updates, which feed re-evaluation — the
operational effect is the same (feedback updates the eval/prompt layer, not necessarily the
codebase) but should be cited as an inference from the Flywheel, not a Reforge soundbite.

---

## Framework 4: Probabilistic Product Management & Guardrails

**Sources:**
- Simon Cross (via Sharma & Mittal AI-PM curriculum), technomanagers.com, 2025-12-27
- Aman Khan, Head of Product, Arize AI — interviewed on Productboard blog, 2025-11-20
- Ian Cairns, Co-Founder & CEO, Freeplay
- Gennaro Cuofano, FourWeekMBA, "AI Benchmarks and Goodhart's Law," 2025-09-05

**Core claim:** "Traditional PM owns a deterministic spec... AI PM owns probabilistic
outputs, not deterministic features" (Cross). The circulating 2026 term for the PM's new unit
of ownership is the **"outcome envelope"**: "AI product management owns an outcome envelope,
and the model determines what falls inside it." Concretely, this reallocates PM
deliverables toward: model capability briefs, evaluation acceptance thresholds, post-launch
drift SLAs, and data readiness as an explicit sprint dependency — rather than a fixed
feature spec. (Note: this phrasing circulates widely across 2026 AI-PM content without one
traceable original author — cite as "2026 practitioner consensus," not a single named
source.)

**Guardrails framing:** guardrails are technical/procedural/ethical boundaries that
constrain AI behavior to safe, lawful limits — the PM's deliverable shifts from specifying
*what the system does* to specifying *the boundary within which it's allowed to act*: "users
set goals and guardrails, and the agent executes end-to-end." For guardrails to remain
functional as the system evolves, they must be versioned as policy-as-code with continuous
feedback loops from observed behavior — otherwise "guardrails stay fixed while the system
around them evolves" and silently stop matching reality. Practitioner-recommended rollout
pattern: 4–6 week pilots, each review cycle adding test cases, until "incidents become rare
exceptions."

**AI evals as a PM discipline** (strongest, most quotable material in this cluster):
- **Aman Khan (Arize AI):** "Our job is to make sure that they don't embarrass us, our
  company, or our brand." "AI evals aren't about binary outcomes... You're defining
  subjective quality criteria." Standard QA can't catch it: systems "hallucinate, drift, and
  break in subtle ways that standard QA testing can't catch."
- **Ian Cairns (Freeplay):** "We're basically running this loop over and over again, finding
  issues and then continuously building up a better set of evals."

**Data drift monitoring** is well established as an MLOps/observability discipline
(Arize AI, Fiddler, WhyLabs, Evidently AI) that PM work now depends on: "a statistical
change in input/output distributions... signaling the world the model was trained on no
longer matches the world it operates in."

**N=1 experiments:** confirmed as a real term (adaptive interfaces personalizing down to a
single user based on demonstrated need, used in healthcare/e-commerce/education framing),
but **no well-documented, named pitfalls specific to "N=1 experiments"** were found in
current sources (statistical validity, novelty effects, false-positive personalization
signals). Flag this as a genuine open gap in the practitioner literature — the lecture
should present N=1 personalization as an emerging practice with an *implied* but
under-documented risk (small-sample noise mistaken for genuine preference), rather than
citing a named failure case.

### Failure mode: Goodhart's Law and benchmark gaming (best documented failure cluster)

**Source:** Gennaro Cuofano, FourWeekMBA, 2025-09-05. Concrete, named, verifiable cases:
- **Google Med-PaLM 2** scored high on medical licensing exams but "confidently recommend[ed]
  chemotherapy for headaches" in practice.
- **Harvey AI** beat lawyers on bar-exam-style benchmarks but "cited completely fictional
  cases in federal court filings."
- **GitHub Copilot** dominated coding benchmarks but produced "code that worked for toy
  problems but created vulnerabilities at scale."
- **GPT-4** "scores 86.4% on MMLU but fails at basic reasoning tasks not in the benchmark."

Core lesson, directly quotable: **"When a measure becomes a target, it ceases to be a good
measure."** Mitigations named: private/rotating evals, held-out task testing, human eval
alongside automated metrics, active skepticism toward metric improvements that arrive faster
than expected.

---

## Framework 5: Practitioner AI-PDLC Stage Models (consultancy guides)

Four consultancy sources (Neomeric, N-IX, Linearloop, Ness) converge on 6–7 stage models and
a shared meta-claim: **the AI PDLC is not sequential-with-handoffs like classic PDLC — it's
an interconnected loop where information from any stage feeds every other stage
continuously** (Ness's framing is the sharpest statement of this). All four are marketing
content from software consultancies — useful for vocabulary and structure, weak on
independent verification (most cited stats are re-citations of McKinsey/RAND/Gartner without
primary links).

- **Neomeric** (2026-05-11): 7 stages, Problem Definition → Data Discovery → Architecture
  Design → Prototype/PoC → MVP Dev & Testing → Production Deployment → Monitoring/Iteration/
  Scaling. Cites **>80% of AI projects fail** (RAND), **88% of orgs use AI in ≥1 business
  function** (McKinsey), **>40% of agentic AI projects will be cancelled by end of 2027**
  (Gartner). Names a **"silent killer"** failure mode: undetected post-launch performance
  degradation — "users quietly stop trusting the system" before anyone notices in a
  dashboard.
- **N-IX** (2026-04-01): Discovery → Design/Development → Testing → Post-Launch, wrapped in
  a proprietary **APEX** (Assess·Pilot·Expand·eXcel) framework. Sharpest quote: **"Most AI
  initiatives in product development fail at the integration layer, not at the model
  level"** — i.e., fragmented toolchains (disconnected Jira/Git/analytics/CI-CD) kill more
  AI products than bad models do.
- **Linearloop** (2025-12-17, "2026 Edition"): 7 stages ending in "Post-Launch Operations,
  Monitoring & Continuous Improvement." No stats/case studies (prescriptive only). Names
  **over-automation reducing human judgment** as an explicit risk category alongside model
  drift.
- **Ness** (undated): strategy/discovery → design → engineering → testing → deployment →
  operations → analytics → continuous improvement, built around their **ATONIS** tooling.
  Best single reframe for teaching: testing shifts from "finding defects" to **"evaluating
  behavior"** because correct outputs are no longer unique — the same input can yield
  different, both-correct outputs, so pass/fail testing stops making sense.

---

## Phase-by-Phase: Classic vs. AI-First Product Lifecycle

| Phase | Classic approach | AI-first approach | Named framework | Concrete example | Failure / limit to teach |
|---|---|---|---|---|---|
| **Discovery / Research** | User interviews, surveys, JTBD synthesis by humans | AI-assisted synthesis at scale; risk: synthetic personas replacing real interviews | Cagan's 5 risks (Value/Usability/Feasibility/Viability/**Ethical**, Huryn 2026); Torres's Error Analysis Loop | NN/g synthetic-user study: synthetic users falsely reported 7/7 task completion vs real 3/7; uniform sycophancy | **Hallucinated discovery hypotheses**: AI summaries miss 20–40% of interview detail (Torres); synthetic users can't disagree with a bad idea |
| **Design / Prototyping** | Wireframes, human usability testing | AI-generated prototype variants; probabilistic UI (same input → different valid outputs) | Reference Datasets (CC/CD, Flywheel) | Reforge Flywheel stage 3: intent-mapped golden datasets w/ edge cases (refunds, payments, etc.) | Reference sets encode *expected* behavior, not *actual* user behavior — evals built on them can rate flawed outputs highly |
| **Build** | Feature spec → code → CI tests (deterministic pass/fail) | Prompt/architecture iteration against evals; "unit tests for agents" | CC/CD steps 1-3; Flywheel stage 4 (Offline Evals) | Offline evals gate both prompt AND architecture changes before deploy | Realism gap for long-running multi-turn agents; eval-reference mismatch |
| **Launch** | Full feature release to 100% or A/B cohort | **Handoff of control**: ship at low-agency/high-control tier, earn agency over time | CC/CD Agency/Control tradeoff | GitHub Copilot/Cursor: completions → blocks → PRs, each step earned via usage/feedback | Skipping the control ladder — shipping full autonomy (v3) untested in v1/v2 causes cascading failure chains |
| **Experiment / Measure** | Cohort A/B tests, fixed hypothesis, statistical significance | Evals pre-deploy + continuous monitoring post-deploy; "outcome envelope" ownership; N=1 personalization | Probabilistic PM / guardrails; Agent Success Rate (Flywheel stage 1) | Arize/Freeplay: continuous eval-loop replacing one-shot A/B | Goodhart's Law: benchmark gaming (Med-PaLM 2, Harvey AI, Copilot, GPT-4 all beat benchmarks while failing in the real task); N=1 experiments lack documented validity safeguards |
| **Support / Operate** | Ticket triage → bug fix → code patch | Ticket triage → **prompt/eval/guardrail update**, not code patch; trace analysis | Flywheel stage 5 (User Monitoring); guardrails-as-policy | Support-ticket signal feeding reference-dataset updates → re-eval loop | "Risk of drowning in data" during trace analysis; fragmented tooling ("fails at the integration layer, not the model level" — N-IX) |
| **Iterate** | Roadmap-driven feature releases | Continuous recalibration triggered by data drift / model changes | CC/CD's "CC" loop; data-drift monitoring (Arize/Fiddler/WhyLabs) | Recalibration triggers on model version change or user-behavior shift | The **"silent killer"**: undetected drift — users quietly lose trust before any dashboard shows a drop (Neomeric) |

---

## Key numbers to cite (with caveats)

- **>80%** of AI projects fail (RAND, via Neomeric, 2026) — headline stat, useful as a hook.
- **>40%** of agentic AI projects will be cancelled by end of 2027 (Gartner, via Neomeric).
- **88%** of organizations use AI in at least one business function (McKinsey, via Neomeric).
- **20–40%** of interview detail lost when AI synthesizes without human review (Torres, via
  Aakash Gupta write-up, 2025-08-12).
- **3 of 7** vs **7 of 7**: real vs. synthetic-user task-completion mismatch (NN/g, 2024).
- Election-turnout AI-survey overestimate (83% predicted vs 49% actual) — **flag as
  [VFY] before using**, found only in a secondary snippet, not independently confirmed via
  full-text fetch.

---

## Sources

| URL | What it gave | Accessed |
|---|---|---|
| https://www.lennysnewsletter.com/p/why-your-ai-product-needs-a-different | CC/CD framework full text: 6-step loop, agency/control tradeoff, reference datasets, failure modes | 2026-09-06 |
| https://www.lennysnewsletter.com/p/why-your-ai-product-needs-a-different-2ea | Confirmed as paywalled/audio variant of same article | 2026-09-06 |
| https://svpg.com/ai-product-management/ (Cagan & Nika) | Classic 4 risks reframed for AI; ethics/hallucination filed under Viability | 2026-09-06 |
| https://svpg.com (Product Risk Taxonomy, 2023-07-10) | Confirms classic 4-risk taxonomy baseline | 2026-09-06 |
| https://productcompass.pm/p/product-discovery-2026 (Huryn) | Clean 5-way risk split incl. standalone Ethical risk | 2026-09-06 |
| producttalk.org (Torres, via podcast reference & Aakash Gupta write-up https://news.aakashg.com/p/teresa-torres-podcast) | Human-interview value claims, 20-40% detail loss stat, Error Analysis Loop | 2026-09-06 |
| https://www.nngroup.com/articles/synthetic-users/ (Rosala & Moran, NN/g) | Concrete documented synthetic-user research failures | 2026-09-06 |
| https://www.reforge.com/blog/ai-evals-course ; /courses/ai-evals | AI Evals course framing (403 direct fetch; search-snippet sourced, medium confidence) | 2026-09-06 |
| https://blog.calibrelabs.ai/p/building-an-ai-product-flywheel (Hegde & Bauer) | Full 5-stage AI Product Flywheel, high confidence | 2026-09-06 |
| https://www.reforge.com/blog/ai-impact-product-management | PM-as-conductor→super-IC nuance | 2026-09-06 |
| LinkedIn (Brian Balfour, Reforge CEO) | Bottleneck-shifts-not-disappears systems point | 2026-09-06 |
| technomanagers.com (Simon Cross curriculum note, 2025-12-27) | "Outcome envelope" / probabilistic-PM framing | 2026-09-06 |
| Productboard blog (Aman Khan, Arize AI, 2025-11-20) | AI evals as PM discipline, quotable | 2026-09-06 |
| FourWeekMBA (Gennaro Cuofano, 2025-09-05) | Goodhart's Law case studies: Med-PaLM 2, Harvey AI, Copilot, GPT-4 | 2026-09-06 |
| https://neomeric.com/blog/ai-product-development-lifecycle/ | 7-stage AI PDLC, stats (RAND/McKinsey/Gartner), "silent killer" drift failure mode | 2026-09-06 |
| https://www.n-ix.com/ai-in-product-development/ | APEX framework, integration-layer failure quote, quantified gains | 2026-09-06 |
| https://www.linearloop.io/blog/product-engineering-lifecycle-guide | 7-stage model, over-automation risk | 2026-09-06 |
| https://www.ness.com/blog/ai-product-development-lifecycle/ | Sequential-vs-interconnected reframe; testing-as-behavior-evaluation | 2026-09-06 |

**Coverage gaps to note:** useluminix.com could not be located/verified under that domain;
N=1-experiment-specific pitfalls are under-documented in current literature (flagged as an
open gap, not filled with a weak citation); several Reforge quotes are search-snippet
sourced due to 403 blocks on direct fetch (medium confidence — verify wording manually
before quoting verbatim on a slide).
