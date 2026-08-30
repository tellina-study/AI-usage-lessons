---
lecture: 11
title: "AI in Discrete and Process Manufacturing"
length_words: ~5200
duration_minutes: 75
wpm_target: 75
status: reviewed
version: v2
issue: 127
branch: issue-127-lec-11-manufacturing
date: 2026-05-21
audience: "3rd-year engineering students (universal)"
keystone_axis: "Discrete vs Process — two models of manufacturing; AI enters both, but differently"
pacing_target: "≈73 min active speech + 2 min buffer; ≤ 95 wpm on each fragment (hard cap)"
pacing_actual: "≈79 wpm avg across 41 fragments; goal — 0 fragments > 95 wpm"
inclusive_markers: "≥10 «we together» distributed across 5 sections"
bridge_phrases: "5 dividers — each «Section N of five»"
strict_in_share: "~42% (failure-cases + criteria + alternatives distributed across §1–§5)"
failure_blocks: "Tesla 2018 + Tesla 2024 + GE Predix + IBM Watson + Foxconn Wisconsin + Tesla Optimus + Boeing 737 + F-35 ALIS + GM Hamtramck + RL drift quartet + avionics MTBF worked-example fail"
derived_from:
  - "chapter.md (Part 1, v5)"
  - "chapter-part2.md (Part 2, v5)"
  - "chapter-part3.md (Part 3, v5)"
  - "deck.yaml (v2, 41 slides)"
  - "slides/sNN-*.md (41 files)"
---

# Lecture 11. Lecturer's Speech. AI in Discrete and Process Manufacturing

**Duration:** 75 minutes (≈73 min active speech + 2 min buffer).
**Audience:** 3rd-year engineering students, universal — not industry specialists.
**Slides:** 41 (33 content + 5 dividers + cover + Q&A + closing hero).
**Pace:** target 70-85 words per minute; hard ceiling 95 words per minute on any fragment.
**Delivery date:** May 21, 2026.
**Source of truth:** chapter v5 (Parts 1-3, finalized) + slides v2.1 (41 rendered).

---

## Pre-flight checklist for the lecturer

### The day before the lecture

- **[s01 hook]** Verify Tesla retreats 2018 + 2024. URL: `https://www.cnbc.com/2024/05/01/tesla-retreats-from-next-generation-gigacasting-manufacturing-process.html`. Open the split-screen "Giga Press 2018 vs 2024" from `library/lectures/lec-11/assets/`.
- **[s07 freshness McKinsey]** Open the latest McKinsey State of AI: `https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai`. Confirm 78% / 5.5% high performers; if there is a new edition as of May 2026 — update.
- **[s08 freshness market estimates]** Cross-check three analysts: Markets&Markets ($155 billion by 2030), Fortune Business Insights ($7.6 billion 2025), Precedence Research ($8.57 billion 2025). The fivefold divergence is the point of the slide.
- **[s11 freshness Tesla Optimus]** Tesla Investor Update: `https://ir.tesla.com/`. Check deployment status — as of May 2026, pilots at dozens of units, production deployment not confirmed. If Musk announced V3 — update.
- **[s12 freshness Foxconn Wisconsin / Fairwater]** Microsoft Fairwater: `https://news.microsoft.com/source/topics/ai/`. Confirm $3.3 billion + December 2025 another $569 million. Cross-check the sequence: 13,000 announced / 10,000 contract / 281 actual (NPR 2020) / 1,454 after revision.
- **[s18 freshness Hyundai Atlas]** Hyundai investor pages + RMAC (Hyundai Robotics Metaplant Application Center) press release: `https://www.hyundai.news/`. Check the target capacity of thirty thousand Atlas units per year by 2028 — status "announcement" or updated production rate.
- **[s18 freshness Toyota GAIA]** Toyota Global AI Accelerator: check the number of AI models created by employees. As of 2024 — ten thousand; look at secondary industry reviews, not Toyota's financial statements. The claim "10,000 hours per year" is the vendor side.
- **[s21 freshness FoxBrain]** Foxconn Computex 2025: `https://www.foxconn.com/en-us/press-center/press-releases`. 80% configuration claim — currency.
- **[s24 freshness BASF Geismar]** Search `https://www.basf.com/global/en/media.html` for "soft sensor" / "Geismar". Confirm: the 20-30% figure is an industry review; BASF Geismar does **not publicly confirm** a specific number. If BASF has published fresh data — update the caveat.
- **[s25 freshness FKDPP]** Yokogawa-JSR — `https://www.yokogawa.com/news/`. 35 days of autonomous control 2022 is a historical fact.
- **[s27 freshness POSCO]** POSCO Newsroom: `https://newsroom.posco.com/`. Check the number of edge nodes (as of 2024 — 180); if there is a new edition "N+ nodes as of 2026" — update.
- **[s28 freshness FDA Part 11 / AI/ML SaMD guidance]** FDA guidance updates 2023-2024 at `https://www.fda.gov/regulatory-information/search-fda-guidance-documents`. Cross-check — specific guidance documents on AI/ML in the SaMD context (including the Discussion Paper 2023, Action Plan 2024).
- **[s29 freshness Russian context]** Check public reviews of AI adoption at Nornickel, Sibur, MMK, NLMK, Severstal, KAMAZ. Sources: TASS, RBC, Kommersant. As of May 2026 — most declarations are without verifiable production metrics. Financial context: Severstal's profit –55% in 2024 — update if there is fresh reporting.
- **[s27 freshness F-35 ALIS]** GAO reports: `https://www.gao.gov/search/F-35`. Confirm the baseline of $44,000 per flight hour FY2018, estimate $35,000 FY2024; status of the transition to ODIN 2025-2028.
- **Read aloud with a stopwatch** the fragments [s07], [s10], [s19], [s25], [s32], [s34b]. Each — within its allotted timing (≤ 95 wpm).
- **Paper checklist by slide** and your own watch — do not depend on the clock in the hall.

### 30 minutes before the lecture

- Connect the laptop, check the projector + audio.
- Open `lec-11.pptx` in Presenter Mode with speaker notes.
- A bottle of water on the lectern.
- Phone on silent.

### Recovery cards (if something goes wrong)

- AI fact-check fail: always-true backup statistic — RAND 80.3% of AI projects deliver no business impact.
- Tech projector fail: printed key sections of speech.md.
- Q&A drifting toward management: gently steer back with "let's look at it from the engineering side."

### Day-of refresh (5 minutes before the lecture)

- Markets and Markets / S&P Global — market data within ±10%.
- Tesla Optimus latest statement (Musk's Twitter / investor brief).
- Microsoft Fairwater Wisconsin progress.

---

## Section 0. Entering the lecture: two models of manufacturing (≈8 min)

### [Slide 1 — Tesla Giga Press: BEFORE/AFTER 2018→2024] 0:00–3:00

[On screen — split-screen. On the left, Giga Press 2018; on the right, the 2024 retreat.]

"Hello. Before we together say the first word about AI in manufacturing — look here.

[pause 3 seconds]

May 2024. Tesla quietly retreats from the plan. Gigacasting the underbody as a single part for the Model 2 — a giant press the size of a two-story house, replacing 70 welded parts with one casting — canceled. A return to the three-section scheme.

[pointing at the right panel]

And this is the **second** cancellation. The first happened in April 2018, at the height of Model 3 "production hell." Musk wrote on Twitter what became the canonical quote of a manufacturing failure of the AI era.

[slowly, reading with expression]

"Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated."

[pause 2 seconds, lower your voice]

The most famous evangelist of aggressive automation himself said — I overestimated, they underrated. And six years later he repeated the same mistake. This is not the story of one brand. This is a **structural pattern**.

In parallel — GE burned over four billion on the Predix platform. IBM Watson Health was sold for about a fifth of what was spent — around twenty percent of the investment. Foxconn in Wisconsin: three billion dollars of subsidies against a promise of ten thousand jobs by contract, up to thirteen thousand in potential — in fact fewer than fifteen hundred.

The numbers show that this is a system. McKinsey: 78 percent use AI, only 5.5 percent get an effect on operating profit above five percent. MIT: 95 percent of generative AI pilots never reach production deployment. RAND: 80.3 percent of AI projects deliver no stated value.

[pause]

The question we together will unpack today: if Tesla retreated twice, GE burned four billion, and 95 percent of pilots never reach production deployment — **where does AI work, where does it not work, and how should an engineer decide?**"

[Transition to s02.]

### [Slide 2 — Cover] 3:00–4:00

"Lecture eleven. AI in discrete and process manufacturing. Part of the course's second module."

[Short pause.]

### [Slide 3 — Lecture map] 4:00–5:00

[On the slide — five horizontal section cards.]

"Lecture map — five sections. The first — what is common to both models: adoption numbers and foundation models. The second — discrete in depth: Tesla 2018, Boeing 737. The third — process: soft sensors, MPC and RL, regulation. The fourth — the summary section: four categories of criteria and a five-step framework. The fifth — closing and the bridge to Lecture 12.

The tone of the lecture is "trust, but verify." Not enthusiasm, not denial. We examine what works, where it breaks, and where the line is that an engineer does not cross."

[Transition to s04.]

### [Slide 4 — Six abbreviations] 5:00–6:00

[On the slide — six cards: ISA-95, PLC, SCADA, MES, OEE, soft sensor.]

"Six terms you can come back to for the whole hour.

ISA-95 — the standard for the "enterprise — shop floor" pyramid. PLC — a programmable logic controller with a deterministic cycle of one to ten milliseconds. SCADA — monitoring and the operator interface, not control. MES — a manufacturing execution system, the carrier of the electronic batch record in pharma. OEE — overall equipment effectiveness: the product of three components — availability, performance, quality. A soft sensor — a computed estimate of a variable from other signals, without taking a laboratory sample."

[Transition to s05.]

### [Slide 5 — Keystone: two models of manufacturing] 6:00–8:00

[On the slide — a two-column discrete | process schematic + a universal failure belt.]

"This is the keystone slide of the lecture. Remember this division — we will keep returning to it for the whole next hour.

Manufacturing — two parallel branches with different physics, different regulatory maps. AI enters both, but **differently**.

[pointing at the left column]

Discrete. Units are counted piece by piece: a car, a chip, a phone, an aircraft engine. AI here is computer vision for quality control, cobots, industrial copilots. Regulation — ISO 9001, Six Sigma. The canonical failure — Tesla 2018.

[pointing at the right column]

Process. Material flows in a continuous stream: chemistry, pharma, metal, cement. The unit is a batch. AI here is soft sensors, an MPC-and-RL hybrid, predictive maintenance. Regulation — FDA, ATEX, REACH. The canonical failure — F-35 ALIS from Lecture 9.

[slowly, lowering your voice]

And on top of both columns — a common belt. **Getting stuck at the pilot stage is universal.** 78 percent use AI — only 5.5 percent get an effect. Most of the AI initiatives you will encounter early in your career will end up in this stuck state. This is the statistical norm."

[Transition to s06.]

---

## Section 1. What is common to both models (≈12 min)

### [Slide 6 — Section 1 divider] 8:00–8:30

"**First section of five.** What is common to both models."

### [Slide 7 — Adoption landscape: 78% / 5.5%] 8:30–10:30

[On the slide — an adoption-value gap chart.]

"The numbers that set the proportions of the lecture — and that we together keep in mind for the whole next hour.

McKinsey "State of AI" 2025. 78 percent of organizations use AI in at least one function. But only 5.5 percent are high performers, with profit above five percent. Two-thirds are stuck at the pilot.

MIT Sloan: 95 percent of generative AI pilots never reach production deployment. Overrun — 380 percent on average. The median time to shutdown — fourteen months. RAND: 80.3 percent of AI projects deliver no stated value.

These three reports measure **different things**. McKinsey — about the effect on profit. MIT — about generative AI pilots. RAND — about the share of projects with no business impact. Manipulating them as interchangeable is a typical mistake.

[slowly]

The main structural cause of getting stuck is the **OT/IT split**. These are two different worlds. AI comes from IT into OT and runs into this split.

And the last thing. What does "AI improves manufacturing" mean? A change in OEE. Remember the question: **into which OEE component is the effect being added?**"

[Transition to s08.]

### [Slide 8 — Diverging market estimates] 10:30–12:00

[On the slide — three market-estimate figures.]

"The size of the "AI in manufacturing" market is estimated by vendors with diverging figures. Let's look at how much.

Markets and Markets: 34 billion dollars in 2025, forecast 155 billion by 2030. Fortune Business Insights: 7.6 billion in the same 2025. Precedence Research: 8.57 billion.

[pause]

**A fivefold difference.** Never trust a single market estimate from a single analyst firm. If three estimates diverge fivefold — the definition is unstable. This is the first pre-lesson: do not trust a single analyst estimate."

[Transition to s09.]

### [Slide 9 — OT/IT split] 12:00–13:30

[On the slide — a structural schematic of the two worlds.]

"OT and IT are structurally different worlds.

OT. A one-to-ten-millisecond cycle, **deterministic**. The software update cycle is measured in years. Safety — physical isolation plus certified equipment at SIL 2 and 3 levels.

IT. Response from milliseconds to minutes, nondeterministic. The update cycle — weeks. Safety — channel encryption, a role-based access model.

When an engineer says "setpoint, loop, alarm" — that is OT. "Endpoint, message queue, load" — that is IT. AI at the edge and any ML model at the shop-floor level are forced to bridge across this boundary. It is precisely the bridge that breaks at the pilot stage."

[Transition to s10.]

### [Slide 10 — Foundation models as augmentation] 13:30–16:00

[On the slide — Siemens IFM + FoxBrain + three reasons.]

"In 2025 specialized **foundation models for manufacturing** appeared — not general large language models, but models built on engineering data.

Siemens Industrial Foundation Model — an industrial foundation model. Announced at Hannover Messe 2025. 150 petabytes of validated engineering data. Capabilities — identifying process elements in CAD models, accelerating piping schematics.

Foxconn FoxBrain. Presented in March 2025, trained on the basis of Llama 3.1 70B by distillation. Application — tuning injection parameters, detecting defects in molding.

[pause, slowly, emphasize]

A critical boundary. Industrial foundation models are an **augmentation tool for the engineer, not an autonomous controller**. They assist, but they do not run the machine directly. Three reasons — fundamental, not "for now."

**First.** Inference latency. A large language model — one hundred to five hundred milliseconds per query. The PLC cycle — one to ten milliseconds, deterministic. This is a difference of orders of magnitude. A language model cannot sit inside the control loop.

**Second.** Hallucinations and nondeterministic output. For an engineer's chief assistant this is acceptable — a human will check. For closing the control loop — no.

**Third.** Certification and the audit trail. SIL 2 and 3, FDA 21 CFR Part 11, the GAMP®5 standard require traceability. The black box of a language model does not pass these requirements.

Architecturally this gives two classes. **Decision support** — it advises, the human decides. And an **autonomous controller** — closing the loop. Foundation models live in the first."

[Transition to s11.]

### [Slide 11 — Tesla Optimus reality check] 16:00–17:30

[On the slide — split: video demo vs production reality.]

"Tesla Optimus is an illustration of the pattern "there's a demo, there's no deployment." Musk announced Optimus at Tesla AI Day in August 2021, the promised price — under twenty thousand. In 2022 they showed the walking prototype Bumblebee. The 2025 update: several thousand units by the end of the year for Tesla's internal use, a million by 2027, target price twenty-five thousand.

Reality check as of May 2026. Pilots at dozens of units, moving small objects under supervision. Tesla does not disclose the exact quantity. Full scaling is deferred to Optimus V3 in late 2026.

At Cybercab in October 2024 Optimus handed out drinks. Bloomberg confirmed — they were controlled by humans remotely.

[slowly]

When you see a beautiful video — ask: how many units, under what conditions, failure statistics. Between a demo and production deployment there are usually five to ten years."

[Transition to s12.]

### [Slide 12 — Hype-collapse trio] 17:30–20:30

[On the slide — GE Predix · IBM Watson · Foxconn Wisconsin.]

"Three stories — three lessons. Each about a different failure mechanism.

**GE Predix**, 2011-2020. Over four billion burned. Predix — GE Digital's industrial Industrial Internet of Things platform, the core of a six-year digital transformation. The goal by 2020 — fifteen billion in revenue. Reality — twelve, and the sale of the digital division in pieces. The lesson — industrial AI does not equal a general-purpose cloud.

**IBM Watson**, 2018-2022. On the manufacturing side Watson was promoted as "–47 percent downtime, –48 percent defects." Deployments at scale did not materialize. January 2022 — Watson Health was sold to Francisco Partners for a bit over a billion, renamed Merative. Twenty percent of what was spent. The lesson — the gap between demo and deployment. Watson won Jeopardy, but it did not treat patients or optimize manufacturing.

**Foxconn Wisconsin**, 2018-2024. The claim — ten billion in investment; the governor cited a potential of up to thirteen thousand jobs, and by the contract with Wisconsin Economic Development — ten thousand by 2025. Three billion dollars of tax subsidies. The head of state called the project "the eighth wonder of the world." Then — a series of revisions. According to NPR for 2020, by the first audit around 281 employees worked at the site. In 2021 the contract was revised to 1,454 jobs and 80 million in subsidies. Reality 2024 — fewer than fifteen hundred. May 2024 — Microsoft buys the site for 3.3 billion dollars for the Fairwater data center. December 2025 — another 569 million. Microsoft uses the **land and infrastructure** built at the municipality's budget expense.

[pause]

The lesson of the last one is practical. **If a project is publicly declared "the eighth wonder of the world" — this predicts failure, not success.**

These three stories are not "AI does not work." This is **"certain forms of bets systematically fail"**: large platforms for everyone, politically motivated megaprojects, hardware-hard demos with a sliding deadline."

[Transition to s13.]

---

## Section 2. Discrete manufacturing (≈18 min)

### [Slide 13 — Section 2 divider] 20:30–21:00

"**Second section of five.** Discrete manufacturing in depth."

### [Slide 14 — CV inspection real cases] 21:00–23:30

[On the slide — BMW + TSMC + Boeing CV cases.]

"Computer vision for quality control is the most widespread scenario of applying AI in manufacturing 2024-2026. A camera photographs a part, a neural network classifies "pass — fail" or localizes a defect.

Where this works.

**TSMC.** Deep learning for detecting defects on wafers. 95 percent accuracy. AI agents orchestrate shop-floor operations. The claim of ten-to-fifteen-percent yield improvement is an industry estimate, not financial reporting.

**BMW GenAI4Q.** Regensburg, 2025. Not a unified checklist — an **individual inspection catalog for each car** based on its configuration. Trained personnel inspect each car, AI sets the priority.

**Volkswagen DPP.** A digital platform built on AWS. 43 plants. Over 1,200 AI applications. A twelve-percent reduction in energy costs at the plant in Poznań.

**Boeing 737.** AI quality inspection deployed in Renton and Everett in early 2024. Machine vision plus AI algorithms for detecting fuselage defects.

[pause]

CV works broadly. But there are **three places** where CV systematically breaks. And that is what we move on to."

[Transition to s15.]

### [Slide 15 — Boeing 737 MAX 9 door plug] 23:30–25:30

[On the slide — the door plug incident + AI inspection failure.]

"January 5, 2024. Alaska Airlines Flight 1282, a Boeing 737 MAX 9. Six minutes after takeoff at an altitude of sixteen thousand feet — sudden decompression. The door plug fell out. The captain made an emergency landing. 171 passengers — without serious injuries.

[lower your voice]

The NTSB findings six weeks later. All four retaining bolts were absent at the time of flight. The plug had been removed to fix a rivet defect in September 2023, but was not correctly reinstalled. Documentation of this operation was not in the system.

The AI inspection tool deployed by Boeing in Renton in early 2024 **did not catch** this defect. Three reasons. The model was not trained on "missing bolt" scenarios. Computer vision ran in the final phase — the bolts were already behind the skin, visually inaccessible. And a human inspector was supposed to cross-check against the record system, but this check was not in the standard procedure.

[slowly, emphasize]

A formula to say aloud. **"Computer vision in inspection is the last line of defense, not the first."** If the process before inspection is broken — computer vision will not fix it. **AI detects defects, but does not create quality.** Quality is created by the process before final inspection — by discipline, training, an audit trail."

[Transition to s16.]

### [Slide 16 — Labeling cost vs data volume] 25:30–27:00

[On the slide — an illustration of cost asymmetry.]

"A cornerstone slide of the lecture. A fundamental concept.

In CV quality control the defect rate is one-to-two percent. Class imbalance: thousands of "pass" images and dozens of "fail." To get a dataset for rare defects — you need either a lot of time or a lot of experts. Expert times hours equals expensive.

[pause]

Raw data is cheap. **Reference labeling is expensive.** This is a lever for Section four — the first criterion "AI does not fit" is whether there is reference labeling of adequate volume.

And the typical picture — five-to-fifteen percent **noise** in the labeling. An ML model does not exceed the agreement among experts. To discipline it — active learning, consistency across multiple labelers, an "abstain" class, calibrated uncertainty."

[Transition to s17.]

### [Slide 17 — Discrete PdM + OEE callback] 27:00–29:00

[On the slide — PdM cases + OEE math.]

"Predictive maintenance. The 2024-2025 marketing: "–25 to –40 percent costs, –50 to –70 percent downtime." Reality is more complicated.

Tata Steel: "–20 percent downtime" in hot rolling. BMW AIQX — continuous monitoring, verification by a human at the final step.

McKinsey in the report "Forecasting at scale" 2025: most companies do not capture the predicted value. A comparison by quartiles. Vendor claim: 25-40 percent. **Top quartile** — 15-20 percent. **Median** — 5-10 percent. **Bottom quartile** — zero-to-two percent, sometimes a negative effect.

[lower your voice]

And the OEE callback. Remember Section 1: **"–25 percent downtime does not equal +25 percent OEE."** If PdM reduces downtime but false alarms force the line to stop more often — performance will sag, and OEE will stay put.

Where PdM works: fast feedback, available labeling, the cost of a false alarm not exceeding the cost of a miss. Where it does not: a long MTBF, safety-critical — there RCM is better."

[Transition to s18.]

### [Slide 18 — Toyota Jidoka cobots] 29:00–31:00

[On the slide — Hyundai-BD Spot + Toyota GAIA.]

"Cobots — robots designed to work safely alongside a human. Not a "lights-out factory," but an augmentation tool.

**Hyundai plus Boston Dynamics.** Spot, the four-legged robot — quality control at the welding area of Hyundai Metaplant America. Atlas, the humanoid — the first commercial deployment, announced January 2026. Hyundai declared 26 billion dollars in investment. The target capacity for Atlas — thirty thousand units per year by 2028. **This is an announcement**, not the current output level. The real rate as of May 2026 — dozens of units in pilots under supervision.

**Toyota.** A counter-example. GAIA — the global AI accelerator. AI models created by **plant employees** — eight thousand in 2023, ten thousand in 2024. The philosophy — jidoka for Industry 4.0. AI as a tool for workers, not as a replacement. **If a worker does not understand the model — the model is not deployed on the line.**

[slowly]

Toyota — the world's largest automaker — publicly opposes full automation. This is not skepticism toward AI in general. This is skepticism toward AI as a **replacement** for the human. And, as we together will see in a minute, this is precisely the right pattern."

[Transition to s19.]

### [Slide 19 — Tesla 2018 over-automation] 31:00–34:00

[On the slide — Q1 2018 timeline + Musk quote + IMD root cause.]

"Tesla 2018 is a lecture within a lecture. The automation literature of the last eight years is built around this case.

First quarter 2018. Tesla plans 2,500 Model 3 per week. By the end of the quarter — 2,020. "Production hell" lasts for months.

On April 13 Musk writes the canonical phrase.

[slowly, direct speech]

"Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated."

CBS the same day: "We had this crazy, complex network of conveyor belts, and it was not working, so we got rid of that whole thing."

What failed. The Model 3 conveyor system — dismantled and replaced by manual transfer. The robot for automatically installing fiberglass mats on batteries — did not work reliably. Battery module assembly — too many automated stages, a bottleneck when any robot fails.

The root cause per IMD. **Tesla tried to replace humans in zones where human variability is a feature, not a bug.** Wiring harness assembly, tubing routing — the geometry varies in part. The robot breaks on variability.

[lower your voice]

The structural lesson is Bainbridge's 1983 automation paradox. Lisanne Bainbridge in the essay "Ironies of Automation": **the more automation, the more critical the remaining operators.** If the operator only monitors — skills fade, while the responsibility for getting out of an emergency is higher. Bainbridge in 1983 predicted the 2026 AI-copilot paradox almost literally.

The alternative — the Toyota Production System plus jidoka. **The rule we together take away: humans in zones of variability, machines in zones of repeatability.**

And the last detail. Six years later, in May 2024, Tesla retreats again — from gigacasting a single part for the Model 2. **Tesla does not learn "once."** This is not an individual failure — it is a structural gravitation toward "more automation is better.""

[Transition to s20.]

### [Slide 20 — CV limits and alternatives] 34:00–36:00

[On the slide — three places where CV breaks + alternatives.]

"Three places where CV systematically breaks, plus an alternative for each.

**First.** Low-contrast defects — roughness on a uniform paint coat, microcracks in composites. The alternative — **amplifying the physical signal**: structured light, X-ray, thermal imaging. Then — simple rule-based vision.

**Second.** Distribution shift when the product changes. A model on product A does not transfer to B without retraining. A plant deploys CV on one line — and discovers that it needs five models. The alternative — statistical process control, Shewhart control charts.

**Third.** Expensive reference labeling — we talked about it on the previous slide.

[pause]

Empirically — **60-70 percent of inspection tasks in production are adequately solved by rule-based vision.** ML is needed for the remaining 30-40. When a vendor says "you need deep ML" — ask what share of your tasks is solved by simple thresholds. Often the answer will reveal that half the tasks do not require ML."

[Transition to s21.]

### [Slide 21 — Foxconn FoxBrain 80% vendor claim] 36:00–37:30

[On the slide — Young Liu quote + 3 clarifying questions.]

"Foxconn chairman Young Liu in May 2025: "The software does about 80 percent of the work of configuring the equipment to launch a new production run."

[pause, emphasize]

**This is a vendor statement, not an independent metric.** And here is the skill we together take away. When you hear such a figure — three clarifying questions.

**First.** The baseline. How many hours and people did the setup require before?

**Second.** The measurement window. One run, an average over a month, or the best case?

**Third.** The list of interventions. What exactly is automated — parameters, fixtures, documentation?

Without answers, 80 percent is a press-release thesis. In the academic literature, similar systems give a thirty-to-sixty-percent reduction in setup time."

[Transition to s22.]

### [Slide 22 — Discrete failure matrix] 37:30–39:00

[On the slide — 4 types of failures in discrete.]

"A summary slide. Four types of failures in discrete.

The first — excessive automation in zones of variability: Tesla 2018, GM Hamtramck 1985. The alternative — Toyota jidoka.

The second — distribution shift when the product changes: AOI for printed circuit boards. The alternative — rule-based vision.

The third — reference labeling more expensive than the model itself: a defect rate of one percent. The alternative — amplifying the physical signal, active learning.

The fourth — a vendor statement without a baseline: Foxconn 80, IBM Watson. The alternative — three clarifying questions plus the OEE question."

[Transition to s23.]

---

## Section 3. Process manufacturing (≈16 min)

### [Slide 23 — Section 3 divider] 39:00–39:30

"**Third section of five.** Process manufacturing in depth."

### [Slide 24 — Soft sensors BASF Pfizer] 39:30–42:30

[On the slide — soft sensors + Pfizer Vox + AI-formulation.]

"Process. The unit is a batch or a flow. The main tool here is the soft sensor.

A soft sensor — a computed estimate of a variable from other signals. Impurity concentration at the column outlet — estimated from temperatures, pressures, flow rates inside. Without taking a laboratory sample. The drawback — it works only within the distribution it was trained on.

**BASF Geismar.** BASF's largest integrated chemical complex in the US. Real-time soft sensors. According to industry reviews of soft-sensor deployments in petrochemicals — a twenty-to-thirty-percent reduction in batch defects. This is a range across reviews, not a publicly confirmed figure specifically for Geismar. BASF does not disclose a specific metric in public documents. In parallel — a knowledge model on 150 years of chemical literature for R&D formulation selection.

**Pfizer Vox.** An internal GenAI platform on AWS Bedrock. In manufacturing — reference-batch identification, anomaly detection, **recommending actions to operators in real time**. The claim — plus twenty thousand vaccine doses per batch.

[pause, emphasize]

The critically important word is **"recommendation,"** not autonomy. An explicit signal of a "human-in-the-loop" architecture, aligned with FDA 21 CFR Part 11. Pfizer Vox will become a worked example in Section 4.

And the last detail. In pharma the dominant soft-sensor tool is **PLS, partial least squares regression**. Not a neural network. Why? PLS is explainable and passes the FDA regulatory audit. **In regulated industries, explainability is often more important than accuracy.**"

[Transition to s25.]

### [Slide 25 — MPC / RL / CIRL hybrid] 42:30–45:30

[On the slide — Yokogawa-JSR FKDPP + CIRL diagram.]

"MPC — Model Predictive Control. On each cycle an optimization is solved: what the setpoint should be over the next N steps under constraints. Requires an **explicit dynamic model**. Explainable, validatable, **dominant in process control**.

RL — reinforcement learning. A black box. Trust is harder to give.

[pause]

The first precedent of an industrial deployment of RL — Yokogawa plus JSR, January-February 2022. **35 days of autonomous control of a distillation column.** The FKDPP algorithm. What FKDPP did that PID could not — it resolved the "quality — energy — throughput" trade-off in a nonlinear system. The Prime Minister of Japan's award 2023.

An architectural subtlety: FKDPP does not control valves directly. It selects setpoints at the upper level; the underlying PID controllers perform control in the tight loop.

[slowly]

And here is **CIRL** — Control-Informed RL, 2024-2026. BASF plus the Royal Academy of Engineering. And here is an architectural detail that is often misunderstood. This is **not "RL instead of PID"** — and **not "two parallel loops."** CIRL is **PID working inside the loss function of deep RL**. RL trains a policy with a state that already has the PID baseline applied.

**RL extends PID, does not replace it.** PID gives base stability; RL adds nonlinear modeling. A validated baseline plus a layer of improvements on top.

The structural principle we together take away: in an industrial ML application **the hybrid dominates over the replacement**."

[Transition to s26.]

### [Slide 26 — RL distribution drift] 45:30–47:30

[On the slide — four triggers of RL drift.]

"RL breaks in four places. Each — fundamental.

**First.** Transitions between batches. At startup or shutdown — going out of distribution; the policy may switch to unsafe actions.

**Second.** A change of raw material. New raw material — new dynamics. A reactor with a batch from a new supplier may find itself out of the training distribution within hours.

**Third.** Seasonal shifts. RL trained in summer does not work in winter.

**Fourth.** Equipment wear. The dynamics drift slowly; the policy slowly degrades.

[pause]

The through conclusion. **MPC is more reliable than RL when raw material changes.** MPC uses an explicit model that is easier to update. RL trains an implicit one, and when it goes out of range the policy breaks without a signal.

That is why RL in industrial deployment always requires a **safety supervision layer** — a separate module that, when it goes out of range, switches the loop to MPC. Not "optimal." **"Safe."** The gold standard for industrial RL."

[Transition to s27.]

### [Slide 27 — Edge PdM + determinism] 47:30–50:00

[On the slide — POSCO 180 nodes + 1ms vs 100ms.]

"POSCO. 180 inference nodes at the edge on rolling equipment. Failure detection works **independently of corporate network availability**. According to industry reports — several percentage points of improvement, up to a ten-percent reduction in energy consumption.

And where do these 180 nodes architecturally live? **Between the PLC and SCADA levels** in ISA-95. This is a new "L1.5," or an OT edge layer. AI at the edge bridges the boundary between them.

[slowly, emphasize]

Determinism of inference at the edge is a fundamental concept. The formula: **"Latency equals determinism, not just speed."**

The PLC cycle — one to ten milliseconds, deterministic. An LLM — one hundred to five hundred milliseconds, nondeterministic. It could be a hundred, it could be eight hundred — it depends on the load.

That is why AI at the edge works by the pattern: **the PLC executes deterministic logic; ML at the edge gives advice; the operator or the PLC makes the final decision.**

Why the edge, not the cloud? Loop latency. Resilience to network failure. Throughput — 4K cameras produce terabytes per day. Confidentiality and regulation.

And a reference to Lecture 9, in one line. F-35 ALIS — around $44,000 per flight hour at the FY2018 baseline, per 2024 data — around $35,000; replacement by ODIN, false alarms undermined trust. Civilian predictive maintenance teaches the same thing."

[Transition to s28.]

### [Slide 28 — Regulatory blockers FDA + ATEX + Decree 250] 50:00–52:30

[On the slide — three regulatory frameworks.]

"Process is regulated. Regulation already exists, and AI is obliged to fit into it.

**FDA 21 CFR Part 11**, pharma. Electronic records and signatures require audit trails, validated systems. The ML black box does not give a clear trail.

What works — AI for forecasting batch quality as a hint to the operator. Pfizer Vox is the model. What **does not work — autonomous batch release by AI means.** The final decision "the batch is good" cannot be automatic, even at 99.9 percent accuracy. This is not a question of accuracy — it is a question of legal responsibility.

**ATEX**, explosive environments. In zone 0 uncertified AI hardware is **physically prohibited**. Standard edge equipment — NVIDIA Jetson, Intel NUC — is not certified. The workaround — sensors in the zone transmit data over fiber optics to a gateway outside the zone.

**Presidential Decree of the RF number 250**, 2022. Wrapping of critical information infrastructure. Most of process manufacturing falls under CII: the fuel-and-energy complex, metallurgy, chemistry. Import substitution by 2027. Local AI at the edge is mandatory.

[pause]

The summary conclusion. AI must be validated **as software**, not get a special regime. GAMP®5 — the validation standard that the FDA accepts. When a vendor says "we have AI, we need special rules" — ask about GAMP®5 IQ, OQ, PQ. A mature vendor knows these abbreviations."

[Transition to s29.]

### [Slide 29 — Russian context] 52:30–55:00

[On the slide — Nornickel + Sibur + MMK/NLMK/Severstal.]

"The Russian context. Publicly verifiable deployments are scarce, but not absent.

**Norilsk Nickel.** AI in flotation and grinding — pilot, early production stage. Publicly confirmed. A substantial caveat — full compliance with the OEE criterion **cannot be verified** from open sources. The company does not publish a detailed metric.

And in parallel — a separate case. In November 2024 an agreement was announced by Gazprom Neft at the Severo-Soleninskoye gas-condensate field. This is not Nornickel — different operations, different operators. They are often conflated in the review press.

**Sibur.** A process-modeling marketplace. Launch announced for the first quarter of 2025. This is an attempt to build a "GitHub for process models" within one company. The context — import substitution, the state goal of 2027.

**MMK, NLMK, Severstal.** General declarations without production metrics. The 2024-2025 financial context — a deep crisis: Severstal's profit minus 55 percent in 2024.

[lower your voice]

The pedagogical conclusion. Public disclosure is scarce — this is **an anti-pattern in reporting itself**, not proof of the absence of deployment. **Distinguishing a press statement from a measurable effect is one of the key skills we together are training here.** In Russian industry you will ask the same three clarifying questions, but the answer will often be "commercial secret." Your right and duty — to treat a figure as a hypothesis, not as a fact."

[Transition to s30.]

### [Slide 30 — Process failure matrix] 55:00–56:30

[On the slide — 4 types of failures in process.]

"A summary slide of Section 3. Symmetric to slide 22.

The first — distribution shift in reinforcement learning, four triggers. The alternative — MPC as a safe fallback plus a supervision layer.

The second — a regulatory blocker. FDA Part 11 prohibits autonomous release, ATEX zone 0 prohibits uncertified equipment. The alternative — recommendation mode plus human-in-the-loop.

The third — the OT/IT split. The model in the IT cloud, the process on the OT side; the audit trail does not stitch together. The alternative — AI at the edge, on the L1.5 layer.

The fourth — vendor advertising claims without metrics. The alternative — five questions to the vendor."

[Transition to s31.]

---

## Section 4. The decision map — when AI is not needed (≈14 min)

### [Slide 31 — Section 4 divider] 56:30–57:00

"**Fourth section of five.** This is the summary section of the lecture. A pocket tool."

### [Slide 32 — Four categories of criteria] 57:00–61:00

[On the slide — 4 categories × 10 criteria.]

"Ten criteria for "AI does not fit," grouped into four categories. This is precisely the pocket tool for which we together set out on this lecture. Concrete control knobs.

**Category A — Data.**

First. **A small sample of failures** — MTBF more than a year. Alternative: CBM, RCM, scheduled maintenance.

Second. **The phenomenon is described by known physics.** Alternative: CFD, FEA, kinetic models, a hybrid via physics-informed neural networks.

Third. **Reference labeling is expensive** — class imbalance. Alternative: amplifying the physical signal, rule-based vision, DOE.

**Category B — Cost asymmetry.**

Fourth. **The cost of a false alarm significantly exceeds the cost of missing a failure.** A false alarm in rolling — four hours of downtime, up to a million dollars. ML is rarely calibrated that precisely. Alternative: SPC, RCM.

Fifth. **SIL 2 or 3 — safety-criticality.** ML is the last choice, not the first. Alternative: deterministic PLC logic, formal verification.

**Category C — Regulation.**

Sixth. **An audit trail is mandatory** — FDA 21 CFR Part 11, GAMP®5. Alternative: explainable AI, a hybrid with rules, human-in-the-loop.

Seventh. **ATEX Zone 0** — a physical limitation.

Eighth. **Decree 250 and CII in the RF.** Alternative: local domestic software.

**Category D — Human.**

Ninth. **Operator distrust — workaround behavior is inevitable.** Alternative: model development by the workers themselves.

Tenth. **A pilot without continuation or shutdown criteria — getting stuck.** The 80-95 percent statistic. Alternative: structured pilots with a baseline plus criteria **before** the start.

[pause]

The through rule: **claims based on demonstrations without a six-month history of production deployment** — buyer beware."

[Transition to s33.]

### [Slide 33 — Matrix of alternatives, 6 tools] 61:00–63:30

[On the slide — a 6×5 matrix.]

"Six tools **without AI** or with a **smaller** share of AI — each we together must know and be able to apply.

**First. SPC** — statistical process control plus Six Sigma. Univariate monitoring by Shewhart charts. Explainable, friendly to the FDA audit. Weak on multivariate correlations.

**Second. DOE** — Design of Experiments. Defensible traceability. Weak with more than ten variables.

**Third. MPC.** Dominant in process control. Requires an accurate model.

**Fourth. RCM plus CBM.** An engineering approach without ML. Certified in aviation.

**Fifth. Physical modeling** — CFD, FEA, kinetics. Known physics, extrapolation beyond the training distribution.

**Sixth. Rule-based vision.** A controlled environment, clear defects.

[pause, emphasize]

And four hybrid patterns. **PINN** — physics in the ML loss function. **CIRL** — PID inside RL. **ML on top of SPC** — ML reduces SPC false alarms. **PLC plus an ML co-processor at the edge** — the PLC is deterministic, ML advises.

In each hybrid AI **augments** a validated tool, does not **replace**. For the third time this lecture: **the hybrid dominates over the replacement.**"

[Transition to s34.]

### [Slide 34 — Pfizer Vox worked example PASS] 63:30–66:30

[On the slide — 5-step framework + Pfizer application.]

"We return to Pfizer Vox and apply the five-step framework. To show that the framework works on a real case.

**Step one.** The column — process, bioprocess. Passes.

**Step two — map the alternatives.** SPC — yes for individual parameters, insufficient for multivariate anomalies. DOE — not for operation. MPC — can control setpoints, does not cover rare anomalies. A classic soft sensor — insufficient. There is a baseline, but there is a gap.

**Step three — the four categories.**

Data — a lot of batch data, labeling from laboratory tests. Passes.

Cost — manageable. FP — the operator will check. FN — a bad batch may get out. Passes.

**Regulation — the critical moment.** FDA 21 CFR Part 11 — **recommendation** mode, not autonomous batch release. The architecture "Vox recommends to operators" complies. If Pfizer had attempted autonomous release — it would have been a regulatory failure. **Passes under the right architecture.**

Human — the operators are trained. Passes.

All four categories pass.

**Step four.** Pfizer claimed plus twenty thousand doses — the baseline is known.

**Step five.** "Vox recommends" — explicit augmentation. The architecture — **decision support, not a controller.**

[emphasize]

The lesson. The difference between "works" and "does not work" here is in the **architectural choice**, not in the quality of the model. The same AI in recommendation mode passes; in autonomy mode — does not pass."

[Transition to s34b.]

### [Slide 34b — Aircraft engine worked example FAIL] 66:30–69:00

[On the slide — 5-step framework with a failure.]

"A symmetric example. Pfizer showed how the framework passes. This one will show how the framework cuts off.

An aircraft-engine manufacturer wants AI for predictive maintenance of a turboshaft engine's gearbox. MTBF — eight years. SIL 2. FP — an unplanned gearbox disassembly, around two hundred thousand dollars. FN — a catastrophe in flight.

**Step one.** Discrete. We pass.

**Step two.** RCM exists — vibration analysis, oil analysis, scheduled inspection. The baseline is mature, worked out over fifty years in aviation.

**Step three.**

Data — **failure.** MTBF eight years, a fleet of 500 engines, twenty years of operation — around one hundred failures. A small sample. Labeling is expensive — disassembly plus the expertise of metallurgists.

Cost — **failure.** A single miss is catastrophic. But the failure rate is lower than the false-alarm rate of any ML model. A false-alarm rate of 1 percent on 500 engines — five false alarms per year; each — an unplanned disassembly at 200 thousand. **Structurally more expensive than scheduled maintenance.**

Regulation — **failure.** SIL 2 in aviation requires a deterministic trace. ML is not certified as safety-critical under DO-178C.

[pause]

Three categories failed. Steps 4 and 5 are not performed.

**Conclusion.** AI PdM on an aircraft-engine gearbox is **not needed**. The alternative — reliability-centered maintenance plus physical sensors plus data exchange across the entire engine fleet. **Without introducing the certification risk of ML.**

This is precisely critical judgment — the main goal of the whole course. **The ability to say "no" to unsuitable AI** on the basis of structural criteria, not intuition."

[Transition to s34c.]

### [Slide 34c — Brewery worked example PASS] 69:00–71:30

[On the slide — 5-step framework passes.]

"A third example. A brewery, packaging control.

The line runs thirty thousand bottles per hour, about seven hundred thousand per day. Defects — a chipped neck, a damaged label, an underfill, a torn-off cap. The defect share is half a percent. Manual sampling misses defects — the eye cannot keep up.

**Step one.** Discrete. We pass.

**Step two.** Manual sampling and periodic control exist, but are insufficient. The bottleneck is clear.

**Step three.**

Data — seven hundred thousand bottles per day, half a percent defects — about three and a half thousand labeled defects each day. Class balance over thirty days — around one hundred thousand labeled examples. Labeling is cheap — visually obvious crooked labels. **Passes easily.**

Cost — a false alarm is the loss of a bottle, negligible. A miss — a customer gets a bottle with a chip, a potential claim. The asymmetry is in the right direction. Passes.

Regulation — ISO 22000 for food safety. Softer than FDA Part 11 or aviation DO-178C. The "characterization" mode is appropriate. Passes.

Human — operators move from continuous visual inspection to exception handling. An improvement in the quality of work life. Passes.

**Step four.** The baseline — manual inspection misses 0.3 percent of defects. The pilot criterion — AI must show no more than 0.2 percent missed with an "abstain" share of no more than 15 percent over three months.

**Step five.** 12 cameras, AI inference at the edge, an "abstain" queue to the operator station. An audit trail with a timestamp and confidence.

[pause]

**The through lesson of the three examples.** The framework works as a **filter in both directions**. Pfizer passes — recommendation mode. The aircraft engine does not pass — little data, certification blocks. The brewery passes — the asymmetry is right."

[Transition to s35.]

### [Slide 35 — The five-step framework] 71:30–73:30

[On the slide — the 5 steps of the framework.]

"A compact closing of the framework. Five steps.

**First. Determine the column.** Discrete or process? It determines the AI stack.

**Second. Map the alternatives.** Six tools — SPC, DOE, MPC, RCM, physical modeling, rule-based vision. If a non-AI one solves it adequately — AI is not needed.

**Third. The four categories of criteria.** Data, cost, regulation, human. At least one fails — AI does not fit without an architectural change.

**Fourth. A pilot with explicit criteria plus a baseline.** Before the start, define: what is the baseline? What are the criteria for "production deployment" and "shutdown"?

**Fifth. Production deployment with human-in-the-loop plus an audit trail.** Decision support or an autonomous controller? In a regulated industry — almost always support.

[pause, emphasize]

The through conclusion at the level of the lecture's keystone axis. **AI in manufacturing is an augmentation tool, not a replacement.** The engineer's job is to know where AI is applicable, where a traditional tool is better, and where their cooperation is. This is critical judgment — the main goal of the course."

[Transition to s36.]

---

## Section 5. Closing (≈6 min)

### [Slide 36 — Section 5 divider] 73:30–74:00

"**Fifth section of five.** Closing."

### [Slide 37 — Two-column recap + failure callback] 74:00–76:00

[On the slide — a two-column recap.]

"Summarizing the discrete-process axis.

**Discrete** — computer vision, cobots, copilots. The failure mode — excessive automation and distribution shift. Tesla 2018 is canonical. Boeing 737: "CV is the last line of defense, not the first."

**Process** — soft sensors, an MPC-and-RL hybrid, predictive maintenance, regulation. Yokogawa-JSR FKDPP — the first precedent of industrial RL. POSCO 180 nodes — determinism of inference at the edge. FDA Part 11 prohibits autonomous batch release.

**Common** — foundation models as augmentation, not a controller. Getting stuck is universal. Four categories of criteria: data, cost, regulation, human.

[slowly, emphasize]

Back to failures. Tomorrow a vendor promises "–70 percent downtime" — ask three questions plus the OEE question. If the answers are vague — this is a demo, not production deployment. **95 percent of pilots never reach production deployment not because AI is bad, but because engineers do not ask these questions.**"

[Transition to s38.]

### [Slide 38 — Q&A + 5 vendor questions] 76:00–79:00

[On the slide — five questions to the vendor.]

"An artifact for your pocket. Print it and keep it with you. Use it at every AI-vendor presentation regardless of industry.

**First. The baseline.** What metric existed before deployment and how was it measured? Separates "AI improved it" from "we started measuring."

**Second. The measurement window.** Over one run, an average over a month, or the best case? Separates the demo from a sustained effect.

**Third. The list of interventions.** What exactly changed — people, process, technology? Separates the AI's contribution from reorganization.

**Fourth (bonus) — the OEE question.** Into which OEE component is the effect being added — availability, performance, or quality? The answer "into everything at once" means the vendor did not count.

**Fifth — past failures.** Give me three documented failures of your system over the last 24 months in the same industry. What happened, what is the lesson learned, how was the architecture changed?

[pause]

If a vendor cannot name **a single** failure — this is a strong signal. Either there is no real production deployment, or they are hiding problems. A mature vendor answers: "we had X, we changed Y, now we do Z" — and that inspires trust.

These five questions we together will ask throughout our careers. They apply to any vendor claim in any industry."

[Transition to s39.]

### [Slide 39 — Closing hero BMW Digital Twin + bridge to Lecture 12] 79:00–81:00

[On the slide — BMW Werk + digital twin overlay.]

"The closing illustration — an overlay of a digital twin on a BMW plant. BMW's digital twins are ready for all thirty-plus plants in 2024-2025. And here we together will stop — this is the territory of **another lecture**.

Today — separate tools: computer vision, predictive maintenance, soft sensors, an MPC-and-RL hybrid. Each — pointwise, with its own task.

**Lecture 12 — the stitching.** Digital twins as a unifying abstraction. AI in automation as the load-bearing fabric of manufacturing. GOST R 57700.37-2021 provides the regulatory basis in the RF.

What we take into the next lecture: the discrete-process axis, the four categories of criteria, the five-step framework, the five questions to the vendor. On the digital twin this will work with the same core of judgment — the task remains the same: **to know where AI works, where it does not work, and how to choose.**

[pause, slowly]

The final thought. AI in manufacturing 2026 is not a "revolution" in the sense of a full replacement of the old tools. It is a **new layer** laid on top of SPC, DOE, MPC, RCM, physical modeling, and rule-based vision. The right pattern is the **hybrid**. The engineering art is to know where AI adds value, where it does not, and where it is dangerous.

This lecture was about developing this art.

Thank you. Questions — at the seminar next week. See you."

[Lights, applause.]

---

## Q&A reserve (buffer if needed)

If time remains — open one or two questions from the prepared Q&A backup list in `chapter-part3.md` (14 typical questions). Priority — Q1 Tesla Optimus + GigaCast, Q5 FDA autonomous batch release, Q8 "what exactly NOT to automate," Q9 OEE baseline measurement.

---
