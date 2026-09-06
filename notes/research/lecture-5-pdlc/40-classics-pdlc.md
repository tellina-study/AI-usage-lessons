---
title: "PDLC Classics Backbone — pre-AI foundations for Lecture 5"
lecture: lec-05
purpose: "Classics backbone: timeless PDLC frameworks with phase models, one core idea, canonical example, KNOWN limitation (to teach judgment), and how the AI era 2025-26 stresses/extends each. Feeds keystone-axis selection."
access_date: 2026-09-06
audience: "advanced 3rd-year IT students who already vibe-code; teach judgment, not reverence"
status: research-complete
---

# PDLC Classics — the pre-AI backbone

The through-line of every framework below is the same skeleton: **the product is a feedback loop** — you form a hypothesis, build something, measure reality, learn, and decide the next move. The classics differ in *which arrow of the loop* they optimize (framing the problem, deciding what to build, measuring whether it worked) and *what unit* they loop over (a gate, an MVP, an interview, an experiment). The AI era does not delete any of them — it changes the **cost and trustworthiness of each arrow**, and it changes them *asymmetrically*. That asymmetry is the lecture's payload.

Each critique below is deliberately real and often comes from *insiders*, not outsiders — so the lecture teaches when a classic is the wrong tool, not just how to recite it.

---

## Master table

| # | Framework · Originator/Year | Phase model / stages | Core idea (one sentence) | Canonical example | Known limitation / critique | AI-era stress / extension (2025-26) |
|---|---|---|---|---|---|---|
| 1 | **Stage-Gate** · Robert G. Cooper (term in print 1988; *Winning at New Products* 1986) | Discovery → Scoping → Build Business Case → Development → Testing & Validation → Launch, with a go/kill/hold **Gate** between each | Retire risk incrementally: do defined cross-functional work in a stage, then make an explicit management go/kill decision before spending more | ~80% of North-American product firms (P&G, LEGO, Tetra Pak) run a Stage-Gate variant | Built for **physical goods**; empirically *slows* software (181-dev study links it to worse speed/cost); rigid, gate bureaucracy misses market windows. Cooper's own answer: the **Agile-Stage-Gate hybrid** (2016) — a tacit admission pure gating is too slow | AI collapses front-loaded planning: teams gate continuously on **evals/telemetry**, not calendar milestones; "start simple, add agentic complexity only when simpler solutions fail" is an anti-Stage-Gate stance |
| 2 | **Lean Startup / Build-Measure-Learn** · Eric Ries, 2011 (on Steve Blank's Customer Development) | **Build → Measure → Learn** loop; the **MVP** starts the loop with least effort; outcomes: persevere or **pivot** | Treat a venture as falsifiable hypotheses and use the smallest experiment to get **validated learning** from real users, not a plan executed on faith | Ries's own **IMVU** (6 months building the wrong feature); Dropbox explainer-video MVP (5k→75k waitlist); Zappos concierge MVP | **Vanity metrics** ("theater of success"); **"MVP theater"** — teams ship the *smallest imaginable*, not *minimally sufficient to test*; "validated learning" is noisy and often misapplied (a *misuse* critique, not a flaw in Ries) | AI drives **Build cost → ~0**, so the loop's bottleneck moves entirely to **Measure/Learn**; "the MVP is no longer a pared-down product, it's a maximum-insight engine"; loop now runs *continuously*, not in weeks |
| 3 | **Design Thinking** · IDEO / Stanford d.school (d.school founded 2005; T. Brown HBR 2008) **+ Double Diamond** · UK Design Council 2003–05 | DT: **Empathize → Define → Ideate → Prototype → Test**. Double Diamond: **Discover → Define** (problem) → **Develop → Deliver** (solution) — two diverge/converge cycles | Solve problems like designers: ground in empathic observation, generate many ideas before judging, learn by cheap prototypes — and diverge/converge *twice* (right problem, then right solution) | IDEO's ABC *Nightline* **shopping-cart redesign** (1999, 5 days on live TV) — also a cautionary case: the cart was never commercialized | **Insider** critiques: Natasha Jen "Design Thinking Is Bullshit" (Post-it ritual, no rigor/proof); Bruce Nussbaum "a failed experiment" (over-systematized the messy creative act into a process trick) | AI compresses Empathize/Ideate/Prototype (synthetic research, agents draft-then-you-critique); but LLMs invent fake "best practices" → teams must **re-insert human review gates** DT's fluid model didn't have; human value shifts to **Define & Test** |
| 4 | **Marty Cagan — "Inspired" / SVPG** · 2008 (2nd ed. 2017); Four Risks 2017; *Empowered* 2020 | **Discovery** (cheap throwaway prototypes) vs **Delivery** (production code), run in parallel; the **Four Big Risks**: Value, Usability, Feasibility, Business Viability; **empowered** vs **feature** teams | De-risk value/usability/feasibility/viability *cheaply in discovery* before expensive delivery; give teams **problems to solve** (outcomes), not roadmaps of features (output) | Prescriptive/abstract (the Four-Risks article names no company); exemplars in *Inspired*: Netflix, Adobe, BBC, Intuit | Cagan's own: most orgs run broken **feature teams** (PM as backlog-owner). External (John Cutler): **survivorship bias**, monocultural "excellence," blames individuals for systemic constraints; **empowerment aspirational** in regulated/enterprise orgs | SVPG "AI PM 2 Years In": AI makes discovery near-free, so the empowered/feature split becomes **existential** — feature teams "drift into irrelevance" against AI-native iterators |
| 5 | **Teresa Torres — Continuous Discovery Habits** · OST 2016; book 2021 | **Opportunity Solution Tree**: Outcome (root) → Opportunities → Solutions → Assumption tests; a **product trio** (PM+design+eng) does **weekly** customer touchpoints | Replace big up-front requirements with a weekly cadence of small customer touchpoints, mapped on a tree, so opportunity/solution choices are never more than weeks stale | Torres's generic **dining** example ("I'm hungry" → takeout / restaurant / meal-prep) to teach opportunity-vs-solution | **Brutal economics**: a proper 30-min interview costs 4–6 team-hours; collapses under deadlines → "aspirational not operational"; **gatekept customers** in B2B (Sales blocks access); hard in regulated industries | Torres is **contrarian to hype**: advises *against* synthetic-user interviews and one-click AI-generated trees — "the thinking and team alignment are the point"; sanctions AI only to mine existing call transcripts / test one assumption |
| 6 | **Jobs-to-be-Done** · Christensen (*Innovator's Solution* 2003; *Competing Against Luck* 2016) **+** Tony Ulwick / ODI (1999) | Christensen: job = *progress* a person seeks in a circumstance ("hire" a product). Ulwick/ODI: solution-free **job statement** (verb+object+context) → measurable desired-outcome statements → opportunity algorithm | Customers don't buy products, they **hire** them to make progress in a circumstance — so target the *stable job*, not the shifting attributes of today's solution | Christensen's **McDonald's milkshake**: half sold before 8:30am to solo commuters; hired to make a boring commute tolerable; real rivals = "bananas, bagels, and boredom" | **Two incompatible schools** under one name (jobs-as-progress vs jobs-as-activity); Christensen "never defined it with rigor" (theory, not method); "solution-free" jobs risk **over-abstracting** away from real segments | JTBD statement syntax ("When [situation], I want to [motivation], so I can [outcome]") becomes an **LLM-prompt scaffold** to auto-extract jobs from transcripts at scale — but mis-specified prompts bake in the solution-bias JTBD exists to avoid |
| 7 | **Pirate Metrics AARRR** · Dave McClure, 2007 · **+ North Star** (Sean Ellis) · **+ HEART** (Google, Rodden et al. 2010) · **+ Kano** (N. Kano, 1984) | AARRR: **Acquisition, Activation, Retention, Referral, Revenue**. NSM: one metric = core value. HEART: **Happiness, Engagement, Adoption, Retention, Task-success** via Goals→Signals→Metrics. Kano: **Must-be / Performance / Delighter** on two satisfaction dials | Instrument the value the product delivers so decisions are evidence-based, not opinion — funnel (AARRR), single alignment metric (NSM), UX at scale (HEART), and which features actually move satisfaction (Kano) | Airbnb NSM = nights booked; Spotify = time listening; Kano: 2007 iPhone pinch-to-zoom was a **Delighter**, now a Must-be | AARRR: funnel-only, vanity-metric risk, misfits B2B. NSM: single-metric **gaming** (LinkedIn chased ad-rev/user, killed engagement). Kano: **static** — delighters decay to basics (hedonic treadmill); clunky survey | AI **corrupts the proxies**: adoption rises because features are *ambient* not effective; token use rises from *verbosity* not value; satisfaction rises from *novelty*. Forces outcome-based NSMs (decision velocity, task success) over engagement counts |
| 8 | **Trustworthy Online Controlled Experiments (A/B)** · Ron Kohavi, Tang & Xu, 2020 (Microsoft/Amazon/Airbnb ExP) | Hypothesize → randomize Treatment/Control → instrument **OEC** + guardrails → run to pre-set sample size → check **SRM** → analyze → ship | Randomized controlled experiments are the **only** reliable way to prove a change *caused* an outcome — randomization neutralizes confounds correlation can't | **Bing ad-headline test**: backlogged 6 months, then +~12% revenue (~**$100M**) — the single best revenue idea in Bing history; tripped a "too-good-to-be-true" alert | **Peeking** (repeated significance checks inflate false positives); **Twyman's Law** ("any figure that looks interesting is usually wrong"); needs high traffic; can't generate the hypothesis, only test one you had | LLM apps adopt the same discipline but must control non-determinism (fixed prompts/seeds/eval versions); new bug: **session contamination** (per-turn randomization) → randomize by user; add LLM-as-judge, latency, token-cost as metrics |
| 9 | **OODA Loop** · John Boyd, USAF, ~1970s ("Patterns of Conflict", 1976) | **Observe → Orient → Decide → Act**, continuously re-entrant; Orient (the hard step) folds in heritage, culture, experience, new info | Whoever cycles observe→orient→decide→act **faster and more accurately** out-adapts the opponent and collapses their ability to react coherently | USMC **maneuver-warfare** doctrine (FMFM-1 *Warfighting*, 1989) grew directly from Boyd's briefings | Born **adversarial/military** — analogy stretch to cooperative product work; the 4-box popular diagram **guts "Orient"**, Boyd's richest step; becomes a buzzword hollowed of his real complexity | Agentic AI is explicitly framed as OODA (observe tools → reason → decide → act). Schneier (Oct 2025): agents Observe/Orient from **untrustworthy inputs** (prompt injection) and loop *too fast to verify* — Boyd's speed-advantage inverts into a **security liability** |
| 10 | **Feedback-loop / double-loop framing** · Shewhart 1939 → Deming **PDCA/PDSA** 1950 · Argyris & Schön **double-loop** 1978 · Ries B-M-L 2011 | PDCA: **Plan → Do → Check(Study) → Act**. Single-loop = correct the error vs fixed goal (thermostat); **double-loop** = also question the goal/assumptions | Improvement is a **closed feedback loop**; the deepest version periodically re-examines whether the *goal itself*, not just the method, is right | Deming's PDCA → post-war Japanese/Toyota quality; Argyris: firms that "solve" a recurring problem with more of the same policy (single-loop) instead of questioning the policy | Single-loop optimizes a **broken goal efficiently** ("better at the wrong thing"); double-loop is blocked by organizational **defensive routines** | **RLHF** is a mechanized single-loop controller on model behavior; **reward hacking / Goodhart's law** is exactly the single-loop failure — optimizing the measured proxy while missing the real goal → argues for double-loop discipline in AI products |

---

## Synthesis — the strongest SPINE for Lecture 5

Three classics are load-bearing enough to carry the whole lecture, and they nest cleanly rather than competing:

**1. The feedback loop itself (row 10 + row 2) is the keystone.** Build-Measure-Learn, PDCA, and OODA are the *same shape* — a control loop — arrived at independently by a statistician (Shewhart/Deming), a fighter pilot (Boyd), and a startup founder (Ries). That convergence is the lecture's most defensible "these people had no contact and drew the same diagram" moment (the pattern Lec-04 used to great effect with the git-loop). It also carries the single most important AI-era insight in one image.

**2. Discovery vs delivery (rows 4–5) is the horizontal axis of the loop.** Cagan's discovery/delivery split and Torres's opportunity-solution tree tell you *what each arrow is for*: discovery = "are we solving the right problem?" (the Measure/Learn arrows, the first Double Diamond), delivery = "are we building it right?" (the Build arrow, the second diamond). This is where the ≥30% judgment content lives: Torres's own "don't automate the tree" and Cagan's "feature teams drift into irrelevance" are *insider* limits, not strawmen.

**3. Trustworthy measurement (row 8) is what keeps the loop honest.** Kohavi's controlled experiments + Twyman's Law + the metric-corruption problem (row 7) are the reason the "Learn" arrow can lie. This is the strongest bridge to AI: LLM output is *probabilistic and per-session variable*, which breaks the shared assumption under AARRR, NSM, HEART, Kano, and A/B testing alike — a deterministic mapping from "user did X" to "product delivered value."

### Recommended single keystone axis

> **The product is a feedback loop — discover → build → measure → learn → decide — and AI changes what each arrow *costs* and how much you can *trust* it, asymmetrically.**

The asymmetry is the payload, and it is counter-intuitive enough to be worth a whole lecture: AI has driven the **Build** arrow toward zero cost (row 2, row 4), left the **Measure/Learn** arrows roughly as expensive *and made them less trustworthy* (rows 7, 8, 10 — corrupted proxies, non-determinism, reward hacking), and made the **Observe/Orient** arrows *faster but attackable* (row 9). So the classic advice inverts: when building is free, the scarce, decisive skill is no longer execution — it is **judging real signal from noise and knowing which arrow is now the bottleneck**. That is exactly the "when is AI the wrong tool" judgment the course exists to teach: an engineer who can build anything instantly but can't tell whether it worked is *more* dangerous than before, not less.

Runner-up axis (if a less abstract spine is wanted): **"discovery vs delivery — AI makes delivery cheap and discovery *more* important, not less"** (Cagan + Torres + Double Diamond). It is more concrete and product-manager-flavored but carries less of the trust/measurement payload; use it as the Section-1 framing under the loop keystone, not instead of it.

---

## Sources

All accessed **2026-09-06**.

**Stage-Gate**
- [Stage-Gate International — Our Story](https://www.stage-gate.com/about/our-story-2/) — origin, term-in-print 1988, *Winning at New Products*.
- [Bob Cooper — Agile-Stage-Gate](http://bobcooper.ca/articles/agile-stage-gate) — Cooper's own 2016 hybrid, "most significant change in 30 years."
- [SI Labs — Stage-Gate Guide & Critique](https://www.si-labs.com/en/articles/stage-gate-process/) — physical-goods bias, digital-product weakness.
- [ScienceDirect study (S0148296318302273)](https://www.sciencedirect.com/science/article/abs/pii/S0148296318302273) — 181-dev finding: negative on software speed/cost.
- [arXiv 2507.01069 — Agentic AI in Product Management](https://arxiv.org/pdf/2507.01069); [O'Reilly Radar — AI Agents Stack 2026](https://www.oreilly.com/radar/the-ai-agents-stack-2026-edition/) — continuous eval-gating vs milestone gating.

**Lean Startup / Build-Measure-Learn**
- [Shortform — IMVU history](https://www.shortform.com/blog/imvu-history-eric-ries-lean-startup/); [Dropbox MVP video](https://www.shortform.com/blog/dropbox-mvp-explainer-video/) — canonical examples.
- [Effective Software Design — vanity vs actionable metrics](https://effectivesoftwaredesign.com/2021/03/23/lean-startup-principles-vanity-metrics-and-actionable-metrics/); [Grokipedia — Lean Startup](https://grokipedia.com/page/Lean_startup) — MVP-theater, misapplication critique.
- [Userpilot — Rethinking Build-Measure-Learn in 2026](https://userpilot.com/blog/build-measure-learn/); [Reboot MBA — Lean Startup Is No Longer Lean, Nov 2025](https://www.reboot.mba/blog/2025-11-30-lean-startup) — Build→0, bottleneck shift.

**Design Thinking + Double Diamond**
- [Design Council — The Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/) — official stages; note 2003 vs secondary "2005" discrepancy.
- [Stanford d.school — Design Thinking Bootleg](https://dschool.stanford.edu/tools/design-thinking-bootleg) — 5 modes.
- [IDEO Journal — Reimagining the Shopping Cart](https://www.ideo.com/journal/reimagining-the-shopping-cart) — Nightline case.
- [Core77 — Natasha Jen "Design Thinking Is Bullshit"](https://www.core77.com/posts/68499/Natasha-Jens-Design-Thinking-is-Bullshit-Argument); [Nussbaum "A Failed Experiment" (Medium reprint)](https://medium.com/@stoweboyd/design-thinking-is-a-failed-experiment-so-whats-next-co-design-23713aa1d97a) — insider critiques.
- [Designlab — State of AI in UX/Product Design 2026](https://designlab.com/blog/ai-in-ux-product-design-trends-2026); [Eleken — AI Product Design 2026](https://www.eleken.co/blog-posts/ai-product-design) — agents draft-then-critique, re-inserted review gates.

**Cagan / SVPG**
- [SVPG — The Four Big Risks](https://www.svpg.com/four-big-risks/); [SVPG — Empowered Product Teams](https://www.svpg.com/empowered-product-teams/) — model definitions.
- [Cutlefish (John Cutler) — A Cagan Critique](https://cutlefish.substack.com/p/a-cagan-critique) — survivorship-bias critique.
- [SVPG — AI Product Management 2 Years In](https://www.svpg.com/ai-product-management-2-years-in/) — AI-era existential framing.

**Teresa Torres**
- [Product Talk — Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/); [Continuous Discovery Habits (book page)](https://www.producttalk.org/continuous-discovery-habits/) — OST structure, dining example.
- [Cieden podcast — Torres on Continuous Discovery in B2B & AI](https://cieden.com/podcast/teresa-torres-on-continuous-discovery-in-b2b-and-ai) — anti-synthetic-user stance.
- [elsevanderberg.substack — "What if customers don't want to talk to you?"](https://elsevanderberg.substack.com/p/what-if-your-customers-dont-want) — gatekept-customer / economics critique.

**Jobs-to-be-Done**
- [Strategyn (Ulwick) — Jobs to Be Done](https://strategyn.com/jobs-to-be-done/) & [History of JTBD](https://strategyn.com/jobs-to-be-done/history-of-jtbd/) — ODI 1999, solution-free job statements.
- [Alan Klement — Two very different interpretations of JTBD](https://jtbd.info/know-the-two-very-different-interpretations-of-jobs-to-be-done-5a18b748bd89) — schism critique.
- [HBR — The Jobs-to-Be-Done Theory of Innovation (podcast/2016)](https://hbr.org/podcast/2016/12/the-jobs-to-be-done-theory-of-innovation) — milkshake case.

**Metrics (AARRR / North Star / HEART / Kano)**
- [Inc. — AARRR: Dave McClure's Pirate Metrics](https://www.inc.com/walter-chen/aarrr-dave-mcclure-s-pirate-metrics-and-the-only-five-numbers-that-matter.html); [McGaw — Pirate Metrics PDF](https://mcgaw.io/wp-content/uploads/2016/04/PirateMetrics_Final.pdf) — 2007 origin, five stages.
- [Google Research — Measuring UX on a Large Scale (HEART paper, Rodden et al. 2010)](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) — HEART + Goals-Signals-Metrics.
- [Amplitude — Good vs Bad North Star Metric](https://amplitude.com/blog/good-bad-north-star-metric); [Brian Balfour — Don't Let Your North Star Deceive You](https://brianbalfour.com/essays/north-star-metric-growth) — Sean Ellis origin, single-metric gaming (LinkedIn).
- [Wikipedia — Kano model](https://en.wikipedia.org/wiki/Kano_model); [Product School — Kano Model](https://productschool.com/blog/product-fundamentals/kano-model) — 1984, three categories, delighter-decay (iPhone).
- [LeanPivot — Finding Your Agent's North Star Metric](https://leanpivot.ai/blog/finding-your-agents-north-star-metric/); [Estha — North-Star Metrics for AI Apps](https://estha.ai/blog/tracking-north-star-metrics-for-ai-apps-a-complete-guide-to-measuring-success/) — corrupted proxies (ambient adoption, verbose token use, novelty satisfaction).

**A/B testing (Kohavi)**
- [exp-platform.com](https://exp-platform.com/) — Kohavi bio, OEC, SRM, book.
- [Kohavi et al. — Controlled Experiments Pitfalls (PDF)](https://exp-platform.com/Documents/2017-05-17EmetricsControlledExperimentsPitfallsKohaviNR.pdf) — peeking, Twyman's Law.
- [Medium/Geek Culture — Bing $100M headline test](https://medium.com/geekculture/how-to-run-an-a-b-test-3b581afe2eb9) — canonical example (NB: the "$300M button" is a *different*, non-Kohavi UX case).
- [Atlan — A/B Testing LLM Applications 2026](https://atlan.com/know/ab-testing-llm-applications/) — non-determinism control, session contamination.

**OODA**
- [Wikipedia — OODA loop](https://en.wikipedia.org/wiki/OODA_loop) & [Patterns of Conflict](https://en.wikipedia.org/wiki/Patterns_of_Conflict) — Boyd origin, Orient richness, FMFM-1.
- [Schneier on Security — Agentic AI's OODA Loop Problem (Oct 2025)](https://www.schneier.com/blog/archives/2025/10/agentic-ais-ooda-loop-problem.html) — untrustworthy inputs, speed-as-liability.

**Feedback loop / double-loop**
- [Wikipedia — PDCA](https://en.wikipedia.org/wiki/PDCA); [Deming Institute — PDSA History (Moen PDF)](https://deming.org/wp-content/uploads/2020/06/PDSA_History_Ron_Moen.pdf) — Shewhart 1939, Deming 1950, PDSA.
- [infed.org — Argyris: double-loop learning](https://infed.org/dir/welcome/chris-argyris-theories-of-action-double-loop-learning-and-organizational-learning/) — single vs double loop, thermostat analogy.
- [Hugging Face — Illustrating RLHF](https://huggingface.co/blog/rlhf) — RLHF as single-loop controller; reward-hacking/Goodhart tie-in.
