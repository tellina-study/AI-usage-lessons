---
lecture: 9
title: "Lecture 9. Lecturer's Speech. AI in the Aerospace Industry and the Defense Sector"
length_words: ~6600
length_min: 75
status: finalized
version: v2
issue: 118
branch: issue-118-lec-09-aerospace-defense
date: 2026-05-20
pacing_target: "≈73 min of active speech + 3 min Q&A buffer; cap 95 wpm on any fragment (max=95)"
pacing_actual: "≈90 wpm avg across 34 content fragments; 0/34 over cap; total 75.75 min"
audience: "3rd-year engineering students (general audience, not aerospace/defense specialists)"
slide_anchors: "35 slides in the render; source IDs s01-s43 with gaps"
source: "chapter v4 (status=finalized, ~17k words, 994 lines) + slides v3 (35 rendered slides)"
keystone_axis: "OODA — Sense → Decide → Act (Boyd 1976) + L1-L5 autonomy ladder + HITL/HOOL/HOTL triad"
inclusive_markers: "13 «мы с вами»/«нам с вами» distributed across 5 sections"
bridge_phrases: "5 dividers — каждый «Раздел N из пяти»"
strict_in_share: "~43% (failure-cases + regulation + criteria, distributed; v2 +foreshadowing Section 0 + Replicator/V-BAT additions)"
failure_blocks: "9 canonical: ALIS, GPS spoofing, Lavender, Lancet rollback, Vincennes 1988, MCAS, Patriot, Replicator, плюс V-BAT anti-hype caveat"
excluded_items: "0 hits для МГТУ/Бауман/ИУ/Можайск/Aerostate/GigaChat (Q&A backup only — disclaim); 0 hits для Du et al. (Ye applied); 0 hits для CENTCOM (INDOPACOM/EUCOM applied)"
v2_changes: "P0-2 Replicator added (s24 MCAS+Patriot section); P0-3 V-BAT added (s21 Fury section); P1-1 anglicism cleanup (107→target ≤5); P1-2 Section 0 foreshadowing; P1-3 closing course-promo trimmed; P1-4 lessons unified ('Урок первый/второй/третий'); P1-5 FMEA/FTA/FedRAMP RU expansion inline; P1-7 accuracy→точность в Lavender; P1-9 Section 2 minor pacing fill"
---

# Lecture 9. Lecturer's Speech

**Duration:** 75 minutes (≈73 min of active speech + 3 min Q&A buffer).
**Audience:** 3rd-year engineering students, general audience — not aerospace or defense specialists.
**Slides:** 35 (29 content + 5 dividers + cover + Q&A).
**Pace:** target 80-90 words per minute; hard ceiling 95 words per minute on any fragment.
**Reading date:** May 20, 2026.
**Source of truth:** chapter v4 (finalized, 2026-05-20) + slides v3 (35 rendered).

---

## Pre-lecture preparation (24-48 hours out)

- **[s01 hook]** Open the Maxar Sentry press release: `https://www.businesswire.com/news/home/20250625291245/`. On the desktop — a pair of "before/after" images from `library/lectures/lec-09/assets/sentinel2-port-before-after.png`. Fallback if the internet fails — the presentation PDF offline.
- **[s14 freshness Lavender]** Verify the numbers against `https://www.972mag.com/lavender-ai-israeli-army-gaza/`: ~37,000 flagged, ~90% accuracy, ~20 seconds per check. If fresh ICRC or AOAV reports appear — mention them.
- **[s15 freshness Palantir MSS]** Open `https://defensescoop.com/2025/05/23/dod-palantir-maven-smart-system-contract-increase/`. Confirm the ceiling of ~$1.3 billion through 2029.
- **[s21 freshness Anduril Fury YFQ-44A]** Open `https://theaviationist.com/2026/03/24/yfq-44a-fury-cca-is-now-in-production/`. Confirm: first flight October 31, 2025; production run since March 23, 2026 at Arsenal-1.
- **[s21 freshness Shield AI V-BAT]** Open `https://shield.ai/shield-ai-selected-to-provide-v-bat-unmanned-aircraft-systems-and-hivemind-autonomy-software-to-the-indian-army/`. Confirm: USCG contract $198M (July 2024), Indian Army $35M emergency (January 2026), JSW Defence production $90M in Hyderabad.
- **[s23 freshness Geran-2]** Verify the estimates from ISW and Ukrainian military intelligence: ~2,700-3,000 drones/month, planned capacity 5,000+. Source: `https://www.understandingwar.org/`.
- **[s24 freshness Replicator/DAWG]** Open `https://defensescoop.com/2025/09/03/` (DefenseScoop September 2025). Confirm: "hundreds" delivered, not "thousands"; Replicator-2 refocused on counter-UAS; DAWG the successor (December 2025). If fresh news from Breaking Defense appears — update the DAWG status.
- **[s27 freshness UN GGE]** Verify the two November 2025 vote tallies: 164/6/7 per `https://press.un.org/en/2025/ga12736.doc.htm` and 156/5/8 per `https://www.stopkillerrobots.org/news/156-states-support-unga-resolution/`. Explain the discrepancy by the counting methodologies.
- **[s30 freshness Russia votes]** Confirm: Russia against since 2018, the US moved to "against" in 2025.
- **Read aloud with a stopwatch** the fragments [s17 Lavender], [s21 Fury+V-BAT], [s24 MCAS+Replicator], [s26 L1-L5]. Each — into its allotted slide timing (max 95 wpm).
- **A paper slide checklist** and your own watch. Do not depend on the clock in the hall.
- **Fallback plan:** if the projector fails — PDF on the laptop. If the laptop fails — paper printout, the core thread OODA + 7 criteria.

---

## Section 0. Three links of the chain (≈10 min)

### [Slide 1 — A satellite spotted changes overnight] 0:00–2:30

[On the screen — a pair of "before/after" satellite images. On the left — an empty shoreline; on the right — the same coordinates with two new buildings and a red bounding box. In the info card: "Maxar Sentry · 250 PB archive · detections in hours".]

"Hello. Before we say our first word about aerospace and defense — look at this.

[3-second pause]

An ordinary Monday in May 2026. On the Maxar Sentry service, an analyst opens the fresh digest in the morning. Overnight the system automatically flagged about two dozen anomalies around the world. Among them — a pair of buildings in a new port in Africa, appearing between images taken eight hours apart. The analyst clicks "before and after" and sees two pictures.

[I point at the bounding box]

Three things in this picture matter for us.

First, the analysis was done not by human eyes. Maxar Sentry was trained on an archive of 250 petabytes spanning two decades. Its pipeline compares fresh images against a baseline through the fusion of several sensors: optical imagery, synthetic-aperture radar, and automatic vessel identification work together.

Second, the human is still in the loop. He looks at the "before and after", confirms the system's hypothesis or rejects it. AI accelerated Sense — but Decide and Act remained with humans.

Third — this works within hours from image to digest. Not within days, as it was before 2022.

[pause, slowly]

This frame is neither a victory of AI nor its defeat. It is a small fragment of a long chain, where in some links AI hands off to humans, and in other links humans deliberately keep control for themselves. This chain is exactly what we will now present as the map of the lecture."

[Transition to s02.]

### [Slide 2 — Cover] 2:30–2:45

[On the slide — the large numeral "09", a title.]

"Lecture nine. AI in the aerospace industry and the defense sector."

[Short pause. Transition to s03.]

### [Slide 3 — Map of the lecture] 2:45–5:45

[On the slide — six cards: Section 0 Keystone OODA · Sense · Decide · Act · Boundary · Assembly.]

"This lecture is one of two in the course where the cost of a model's error is measured not in money but in lives. The first such lecture was about medicine — Lecture 7. And today we take on the second.

And one more distinctive feature. In aerospace and defense the engineer is embedded in three frames at once. The first — civilian certification: DO-178C, ARP4754A. The second — the defense policy of an individual country: DoD Directive 3000.09 in the US. The third — international law: UN GGE, the International Committee of the Red Cross, the protocols of the Geneva Conventions. These frames sometimes coincide, sometimes compete. The skill of finding a path among them is a distinct engineering competence, and today we train it.

[slowly, foreshadowing]

And I want to say honestly where we are headed. In this lecture there will be nine dissected failures of AI systems. Lavender in Gaza — 37 thousand flagged people and an average of 20 seconds of review per target. MCAS on the Boeing 737 — 346 dead because of a single sensor and closed documentation. F-35 ALIS — a predictive-maintenance system that had to be abandoned in 2024. Patriot 2003 — two friendly aircraft shot down by their own batteries. DoD Replicator — a target program for thousands of drones that delivered hundreds. And four more cases that we will dissect along the way. This is not "AI is bad." This is about exactly where the chain breaks — and what lesson the engineer must draw from each break.

[I point at the map]

The map — five sections. Sense, where AI works best. Decide, where the hype of large language models is most dangerous. Act, where loud demonstrations are far ahead of real combat readiness. Boundary and regulation — the meta level. And assembly: criteria, career, closure.

The tone of the lecture is "trust, but verify." Not evangelism, not dissidence. We dissect what works, where it breaks, and where the boundary lies that the engineer does not cross by decision of a vendor."

[Transition to s04.]

### [Slide 4 — Six acronyms] 5:45–6:45

[On the slide — six cards: SAR, ATR, ISR, EW, LAWS, OODA. Each — acronym + expansion + one line.]

"Before we enter the first link — six acronyms. You can come back to this slide.

SAR — Synthetic Aperture Radar. Sees through clouds and at night.

ATR — Automatic Target Recognition. The chief decorated term in military AI advertising.

ISR — intelligence, surveillance, reconnaissance. The umbrella term for reconnaissance tasks.

EW — Electronic Warfare. Suppression and deception of signals.

LAWS — Lethal Autonomous Weapon Systems. Negotiations at the UN revolve around these.

OODA — Observe — Orient — Decide — Act. John Boyd's cycle. This is exactly what we now move on to."

[Transition to s05.]

### [Slide 5 — Keystone: three links of the chain] 6:45–9:45

[On the slide — three cards in a horizontal chain: Sense → Decide → Act. On top — a gray ribbon "Civilian ↔ Military · dual-use".]

"Any aerospace or defense task — intercepting a missile, correcting a course, monitoring a territory — decomposes into the same chain.

First you have to see. Collect signals from the world — from sensors, cameras, radars, open sources. This is Sense.

Then interpret the signals and decide. Classify the object, assess the threat, choose the reaction. This is Decide.

And finally do something. Give a command to an operator, deploy an air-defense system, launch a drone. This is Act.

[pause, slowly]

This model was formulated in 1976 by the American pilot and theorist Colonel John Boyd. The full acronym is OODA. Boyd used it to explain why one pilot defeats another in aerial combat: the one who goes through the cycle faster.

We use it as the keystone axis of the whole lecture. We simplify it to three links, folding Observe and Orient into a single Sense.

The main thing to take away from this slide: AI enters each link differently. Failures happen at the seams.

In Sense AI works best. There is lots of data, reference labeling is available, the cost of a false positive is tolerable.

In Decide AI works as an accelerator for the analyst. But it works poorly as a replacement. Here the hallucinations of large language models and the tendency to trust the automation scale up.

In Act AI works in narrow scenarios with crewed cover. Full autonomy in combat in 2026 is marketing and a subject of negotiations, not deployed practice.

[I point at the gray ribbon]

The gray ribbon on top is dual-use. The same pipelines work in both the civilian and the military loops. Satellite agri-analytics is the same convolutional network as territory reconnaissance. Rolls-Royce's predictive maintenance uses the same digital-twin architecture as the F-35.

This means: an engineer in a civilian direction is constantly adjacent to a defense application of their technologies. Danger and opportunity at once."

[Transition to s06.]

### [Slide 6 — Section 1 divider] 9:45–10:00

"Section one of five. Sense — eyes in the sky and on the ground."

[Transition to s07.]

---

## Section 1. Sense — eyes in the sky and on the ground (≈12 min)

### [Slide 7 — Sense intro] 10:00–11:45

[On the slide — 4 types of sensor inputs on the left + 3 reasons "why AI works here" on the right.]

"Sense is the collection and initial interpretation of signals about the external world. Four main types.

The first — satellite imagery: optical, multispectral, infrared, SAR.

The second — telemetry from one's own platforms: engines, onboard systems, vibrometry.

The third — the adversary's radio signals. SIGINT, ELINT, COMINT — intercepting messages and analyzing the situation.

The fourth — open sources: social networks, news, commercial AIS data on vessels.

AI in Sense is mostly computer vision for images, signal processing with a machine-learning overlay for radar, and predictive time-series analytics for telemetry.

Why is Sense the most well-off link? Three reasons, and I want us to remember them.

First — available reference labeling. Satellite images can be verified by a field visit, a second sensor, historical data.

Second — a tolerable cost of a false positive. An extra alert on the analyst is lost time, not a life.

Third — a multitude of sensors. You can build a fusion of several sources, which reduces the individual fragility of each model."

[Transition to s08.]

### [Slide 8 — Maxar Sentry] 11:45–13:15

[On the slide — a real Maxar satellite image + 4 info cards.]

"By 2026 a stable foursome of players had taken shape in commercial satellite analytics. Their own satellites, a machine-learning overlay, and the sale of the service to agencies and commercial clients.

Maxar Sentry launched on June 25, 2025 as a "predictive intelligence suite." Under the hood — models over an archive of 250 petabytes plus the fusion of several sensors. The main contract — the Luno A D01 program with the American National Geospatial-Intelligence Agency. Maxar is obligated to deliver detections of aircraft, ships, and equipment within hours of imaging.

[slowly, anti-hype]

And now — the anti-hype caveat. The label "AI detection" in these services often means not a single foundation model but an orchestration of classical computer-vision methods, change detection, and sensor fusion. Maxar Sentry is a set of tools, not a single model. The marketing language runs ahead of the technical. When you assess such a vendor, we must distinguish AI marketing from AI architecture."

[Transition to s09.]

### [Slide 9 — BlackSky, Planet, Capella, edge AI] 13:15–15:15

[On the slide — 4 cards: BlackSky, Planet, Capella+ICEYE, edge AI on-orbit.]

"Besides Maxar — three more significant players.

BlackSky Gen-3 — a constellation of small satellites with a high revisit rate, several times a day for each point. 2024 revenue — about 102 million dollars.

Planet Labs — the most massive network. Hundreds of small satellites with daily coverage. The main contract — the EOCL program of the National Reconnaissance Office, first stage 146 million.

Capella Space and the Finnish ICEYE — these are synthetic-aperture radar operators. The advantage — all-weather imaging. The main application — maritime surveillance, tracking the shadow fleet.

[I point at the fourth card]

And in parallel — edge AI on-orbit. The machine computations are carried out directly on the satellite. The goal — to reduce latency and channel bandwidth. Instead of megabytes of raw imagery, a kilobyte of digest is sent down: "here is a change." The European agency in August 2024 launched Φ-sat-2 with command-updatable models. Lockheed deployed Pony Express 2 as a military analog. Slingshot Aerospace in July 2025 launched TALOS — surveillance of space itself, not of the ground.

The adoption of AI in the Sense link is growing fast. The scenario for 2026-2028: from detections in hours to predictive intelligence before the event."

[Transition to s10.]

### [Slide 10 — The Russian layer] 15:15–16:45

[On the slide — 3 info cards: TERRA TECH, SCANEX, SPUTNIX.]

"The Russian layer in Sense develops along three paths. The public part — civilian satellite analytics.

TERRA TECH — a subsidiary of Roscosmos since 2017. Satellite imagery plus aerial photography plus external sources in a web interface with classification. The main public case — monitoring of agricultural land in the BRICS countries under a 2024 agreement.

SCANEX — the only company in Russia directly receiving remote-sensing data at its own stations. The archive — 3.5 million images. The exclusive supplier for Yandex Maps.

SPUTNIX — a subsidiary of the Sistema conglomerate. More than 100 CubeSats since 2013. The main constellation is Zorky-2M: three satellites in orbit plus three ready for launch. A 2.5-meter camera.

The Russian layer is asymmetric to the Western one. There are fewer vendors, fewer public metrics — but real operational cases exist. This is not PR in the sense of "there is nothing," and it is not full transparency. This is what there is."

[Transition to s11.]

### [Slide 11 — Predictive maintenance + the F-35 ALIS failure] 16:45–19:30

[On the slide — two columns: Rolls-Royce + Airbus Skywise (success); F-35 ALIS → ODIN (failure) with a photo of an F-35.]

"AI in Sense works at scale on one's own aircraft. Predictive maintenance — predict the failure of a component before it happens.

Rolls-Royce IntelligentEngine has been operating since 2018. A digital twin of every flying engine plus machine-learning pipelines. The metric — about 400 unscheduled maintenance events prevented per year. Millions of euros in savings.

Airbus Skywise — a broad platform for airlines. By the end of 2024 — about 11,600 aircraft. easyJet reported fuel savings of 8.1 tonnes per aircraft per year and 44 prevented cancellations in July 2024.

[pause, change of tone]

And now — a failure that we will dissect in detail. F-35 ALIS — the predictive-maintenance system of the F-35 fighter. By the late 2010s it had turned into a source of problems. A high rate of false positives: ALIS flagged an aircraft as "not fit to fly" when there was no problem. The US Government Accountability Office in its 2020 report stated directly: inaccurate data at times led the system to signal that an F-35 should not fly — even though there was no problem. It was so hard to use that personnel worked around the system through Excel. The cost of a flight hour — 42-44 thousand dollars. The finale — June 2024, the move to a new platform, ODIN.

[slowly]

The lesson of this slide. Predictive maintenance in a safety-critical domain works only under three conditions.

**Lesson one.** A fast feedback loop. Model drift is detected in days, not in years.

**Lesson two.** Available reference labeling. There must be a way to verify every warning the system issues.

**Lesson three.** The cost of a false positive is no greater than the cost of a miss.

ALIS violated all three. ODIN is being built in explicit awareness: a smaller scope, a program owned by the state, an explicit human in the loop to authorize flights."

[Transition to s12.]

### [Slide 12 — Adversarial SAR ATR + GPS spoofing] 19:30–22:00

[On the slide — two topics: corner reflectors attack SAR ATR; a map of Latvia with the figure "820 cases of GPS interference in 2024, a 32× rise since 2022".]

"The second failure of the Sense link — adversarial attacks on synthetic-aperture-radar target recognition. A classifier is trained to recognize tanks from a radar picture. The adversary places cheap metal reflectors on the equipment — and the classifier begins to misclassify.

Research by Ye and co-authors in 2023 shows the physical feasibility of such attacks. This is knowledge available to any opposing side.

Lesson: accuracy on curated datasets is deceptive for adversarial domains. The adversary defines the distribution at test time. Defense requires three things: Bayesian uncertainty estimates; training on adversarial examples; a decision-refusal route with escalation to a human.

[I point at the right-hand part]

The third failure — GPS spoofing of civil aviation. AI has nothing to do with it — but the case shows the fragility of systems dependent on global navigation satellites. According to Latvia, in 2024 there were 820 recorded cases of signal distortion — against 26 in 2022. Most is attributed to Russian electronic-warfare assets.

Lesson: a single navigation network is a single point of failure. Defense — simultaneous work with GPS, GLONASS, Galileo, BeiDou; inertial navigation as a fallback; eLORAN; long-term — quantum inertial navigation.

Military electronic warfare spreads to non-combatants. Civil aircraft regularly fall into zones of distorted GPS. Protecting global navigation systems is a collective good.

[pause]

From two failures — two engineering criteria. First: low data density or distribution shift. Second: a decision with a life-cost on a single sensor is a single point of failure."

[Transition to s13.]

### [Slide 13 — Section 2 divider] 22:00–22:15

"Section two of five. Decide — from observation to decision."

[Transition to s14.]

---

## Section 2. Decide — from observation to decision (≈14 min)

### [Slide 14 — Decide intro] 22:15–23:45

[On the slide — a pipeline: 4 types of input → fusion → COA recommendation. At the bottom — a gold callout "10% × 37,000 = 3,700".]

"Decide — the transition from observation to the choice of an action. The family of tasks: operational planning, target identification, source integration, decision support.

This link is the most delicate. The demand for acceleration is enormous. But here the hallucinations of large language models and the tendency to trust the automation turn into decisions about people's lives.

In the Decide link, large language and foundation models process a mixed input: texts, images, maps, telemetries. Every major AI company comes in here: Anthropic, OpenAI, the Chinese DeepSeek and Qwen, the classical defense vendors Palantir, Scale, Helsing.

[slowly, I point at the accent block]

The main point of the slide — a single number. 10 percent of 37 thousand is 3,700. This is a preview of Lavender, which we will reach in four slides. "90% accuracy" sounds good. But accuracy was designed for symmetry — a false positive and a false miss are equivalent. In tasks where a life is at stake, this is never true."

[Transition to s15.]

### [Slide 15 — US vendors: Palantir + Scale + Anthropic] 23:45–27:00

[On the slide — three columns: Palantir MSS timeline, Scale Donovan/Defense Llama/Thunderforge, Anthropic-Palantir-AWS IL6.]

"The main American flagship — Palantir MSS, the Maven Smart System. The history with the Maven program began in 2017 — a US Department of Defense program to analyze drone footage. In March 2018, through a leak, it became known that Google was helping. By June 2018 Google did not renew the contract. The program was picked up by Anduril, Palantir, and Scale.

Today MSS is the Palantir layer through which a commander works with the models of the Maven program. Contracts: 480 million in May 2024; plus 99.8 million in September; plus 795 million in May 2025. The cumulative ceiling — about 1.3 billion through 2029.

The system's capabilities — the fusion of intelligence from many sources, assistance in targeting, dashboards for commanders. The level — L1, assistive. AI issues detections, the commander decides. This is the pattern "AI-accelerator, not AI-decision-maker" in its pure form.

[pause]

The Scale AI line — an evolution through three products. Donovan, 2022-2023 — a large language model for decision support of the XVIII Airborne Corps. Donovan read thousands of pages of operational documentation and in minutes produced recommendations that the corps staff previously spent hours on. Defense Llama, November 2024 — a fine-tuned Llama 3 for the defense loop. Thunderforge, March 2025 — a product for wargaming and strategic planning for the Pacific and European commands of the US. FedRAMP HIGH authorization — that is, a federal cloud authorization at the HIGH level — the highest level for unclassified but critical workloads.

The third line — the partnership of Anthropic, Palantir, and AWS, November 2024. Claude 3 and 3.5 at the IL6 level — the highest secrecy level of the US government cloud. This is a significant shift: as recently as 2023 Anthropic avoided military contracts.

[slowly]

What matters to the engineer. Palantir won the market not only with models but with an infrastructure stack. FedRAMP HIGH plus authorization on several classified networks — this is engineering work comparable in volume to AI development. When you assess a defense AI vendor, we must separate two axes: the AI capabilities and the authorization stack. These are different competences, and often the market is won by the second, not the first."

[Transition to s16.]

### [Slide 16 — EU + Russian C2] 27:00–29:15

[On the slide — two columns: Helsing (€12B) + Russian C2 Svod/Glaz/Groza/ZOV with an explicit single-source caveat.]

"The main European player — Helsing. Altra — a system for fusing intelligence from drones and observers for ground combat. Centaur — an AI pilot, tested on the Saab Gripen E in June 2025. Round D — 600 million euros, a valuation of 12 billion. The lead investor — Prima Materia, managed by Daniel Ek, co-founder of Spotify. The fact that venture capital of this profile enters defense is exactly that drift of 2024-2026 that we will return to in Section 4.

[pause]

The Russian attempt at an analog for decision support — the Svod ecosystem and Glaz-Groza-ZOV. According to the CSIS analytical center as of April 2026, three components. Svod — a situational-awareness complex, announced in August 2025. Glaz — applications for drone operators. Groza — fire control. ZOV Maps — a geospatial platform.

[slowly, with emphasis]

And now an explicit and important caveat. Information about Svod and Glaz-Groza comes from two sources: the Russian official press and CSIS analysis based on it. Independent Western verification is absent. Effectiveness in combat — per the CSIS assessment — is uneven.

Pedagogically we mention these systems because they exist as an attempt, and an engineering student must know that in Russian defense AI this class of tasks is being developed. Not to mention them would be a distortion. To report them as a success would be propaganda. We choose the middle path: to mention them with an explicit source caveat."

[Transition to s17.]

### [Slide 17 — Lavender failure] 29:15–33:00

[On the slide — a funnel chart: 37,000 → ×90% → ~3,700 false positives → 20 seconds of review → 15-20 civilian casualties. On the right — 3 lesson cards.]

"The main pedagogical failure of the Decide link — IDF Lavender, an AI system for the mass identification of targets in Gaza.

Lavender — a database flagging Palestinian men as "suspected members of Hamas or Palestinian Islamic Jihad." Per the testimony of six officers of Israeli intelligence, published in +972 Magazine in April 2024, Lavender flagged about 37,000 people. By the IDF's own admission — accuracy about 90 percent. One in ten — about 3,700 people — is a false positive.

[slowly]

The review process. A quote from the material: officers spent almost no resources double-checking the targets. The average time to check one target — about 20 seconds. Authorized collateral damage — up to 15-20 civilian casualties per one lower-tier operative.

The reaction. The UN Secretary-General expressed deep concern. The IDF denied the publication. The Lieber Institute and AOAV flagged this as a precedent for automated target lists.

[3-second pause]

There are three lessons. Each — a self-contained engineering lesson. This is the main thing we take away from the lecture.

**Lesson one.** Accuracy in percent is the wrong metric when a life is at stake. If a model errs in 10% of cases and is applied to 37 thousand people, the error scales into thousands of people. The correct metric is a composition: the cost of a false positive multiplied by the size of the population and by the frequency of the trigger. In medicine, in Lecture 7, we saw a similar pattern: a false miss of a cancer is costlier than a false positive. In Lavender — the reverse: a false positive is the life of an innocent person. But the system was designed for symmetry. The first structural error.

**Lesson two.** AI removes friction — and sometimes that is bad. Previously it took time, an analytical resource, a commander's signature. These are natural brakes. AI lowers the cost of a decision — the pace rises, the quality of deliberation falls. By removing friction, AI scales not quality but speed.

**Lesson three.** A human in the loop is not the same as a human actually making the decision. Lavender formally satisfied the requirement of "a human in the loop": every decision was authorized by an officer. But 20 seconds of review is a formal confirmation, not an examination. If HITL degenerates into a signature without deliberation — this is HOTL under the mask of HITL.

[slowly]

The alternative is not "let's make Lavender more accurate." The alternative is a change of architecture. AI assists the initial triage. The human retains authority with real time for examination. AI is an accelerator, not the decision-maker."

[Transition to s18.]

### [Slide 18 — Lancet rollback + Vincennes 1988] 33:00–36:15

[On the slide — two columns: Lancet with the UI "Target Locked" and a rollback timeline; USS Vincennes 1988 with a photo of Iran Air.]

"The second failure of the Decide link — the Russian "Lancet" and the rollback of the automatic target-recognition function. The canonical case — to distinguish a demonstration from combat use.

"Lancet-3" — a Russian loitering munition. The 2022-2023 marketing promised that the device would itself find and strike a target. The video recordings contained the caption "Target Locked." Analysis of field events by CSIS and the Modern War Institute showed: the Russian side turned off the automatic guidance. The latest videos no longer contain the automatic target-lock interface.

The hypothesis — a premature move to combat use. Recognition worked in the demonstration: a narrow distribution, known targets, the absence of electronic warfare. It did not work under real conditions: dust, smoke, jamming, damaged equipment. Edge cases — and that is most of the battlefield.

[slowly]

Lesson: a demonstration is not equal to combat use. Not a specific of the "Lancet." Machine quality in a narrow distribution does not carry over to the full variability of the battlefield. An engineering student must ask the question: under what conditions was the capability demonstrated? What changes in combat use?

[pause, transition]

The third failure — a historical one. Not AI in the strict sense, but the lesson applies to large language models. On July 3, 1988, the US Navy cruiser Vincennes shot down the Iranian civilian aircraft Iran Air 655. 290 people died.

The Aegis combat information and control system correctly recorded the trajectory as "climbing." Operators under combat stress reported to the captain: the aircraft is descending in an attack. The root cause — not an algorithm error. A failure at the human-machine interface.

The lesson — not about automation, but about how to test the interface. If a system assumes that people will catch the machine's error, design the process for the predictable failures of people themselves.

[slowly]

And why this is about large language models. A language model produces smooth, confident text. An operator under time pressure is inclined to accept it as correct. Vincennes — a lesson of 1988, applicable to 2026.

From these failures — two criteria of the Decide link. Third: cases with a long tail of the distribution and low confidence — an explicit decision refusal is needed. Fourth: a decision with a life-cost without a formal human in the loop. Lavender — the counterexample."

[Transition to s19.]

### [Slide 19 — Section 3 divider] 36:15–36:30

"Section three of five. Act — autonomy on the platform."

[Transition to s20.]

---

## Section 3. Act — autonomy on the platform (≈15 min)

### [Slide 20 — Act intro + L1-L5 mini-preview] 36:30–38:00

[On the slide — a preview of L1-L5 + a cost-asymmetry callout "$300 drone vs $3M Patriot".]

"Act in OODA — the last link. AI not only observes or recommends — it executes. Controlling an air platform, coordinating a swarm of drones, autonomous interception of drones, unmanned ground platforms.

Adoption in the Act link grows fast in terms of the number of platforms. But — a critical caveat for the whole lecture — most combat strikes remain either with an operator in the loop or with semi-automatic guidance on the final segment. "AI will replace pilots" — an exaggeration. "AI will replace gunners" — an exaggeration. The reality — pilots paired with supervised AI.

[I point at the accent block]

A special place in the Act link — autonomy for the interception of enemy drones. The main reason for the growth — the asymmetry of cost. A 300-dollar drone against a 3-million surface-to-air Patriot missile. To replace 3 million with an AI perimeter of comparable cost — an economic necessity. This is exactly where the explosive growth of 2026 is."

[Transition to s21.]

### [Slide 21 — Anduril Fury YFQ-44A + Shield AI V-BAT] 38:00–41:30

[On the slide — a photo of Anduril Sentry + an L3 badge + a timeline: first flight October 31, 2025, production run March 23, 2026, Arsenal-1.]

"The showcase of the modern American bet — Anduril Fury YFQ-44A. CCA — Collaborative Combat Aircraft — a US Air Force program to create unmanned wingmen flying alongside crewed fighters.

Fury YFQ-44A: altitude up to 50,000 feet, Mach 0.95, a 9g load factor, a Williams engine. First flight — October 31, 2025. Series production started on March 23, 2026 at the new Arsenal-1 plant in Ohio. Investment — a billion dollars.

Controlled by the Shield AI Hivemind autonomous stack plus the Anduril Lattice operating system. Flies with the AIM-120 missile — a medium-range air-to-air missile.

The level of autonomy — L3, supervised autonomy. AI executes in a pre-authorized corridor. The crewed wingman above watches the execution.

[pause]

The Anduril Lattice contract with the American army has a ceiling of up to 20 billion dollars over 10 years. This is an enormous financial shift, concerning not one company but the whole configuration of defense AI in the US.

[pause, transition to V-BAT]

And since we mentioned Hivemind, we should tell about the second major platform on it — Shield AI V-BAT. V-BAT is a Group 3 class device, a medium-heavy vertical-takeoff-and-landing drone. The acronym stands for Vertical Takeoff Bat. Flight endurance — more than 12 hours, a ducted fan, heavy fuel, resistance to electronic warfare.

The contracts for V-BAT are serious. The US Coast Guard in July 2024 signed a contract for 198 million dollars — the largest in its category. The Indian Army in January 2026 chose V-BAT with a license for Hivemind in an emergency procurement of 35 million; the Indian JSW Defence is building production in Hyderabad for another 90 million. The level — L2-L3: target confirmation by the operator at the lower level, supervised autonomy at the upper.

[slowly, anti-hype]

And right away — the anti-hype caveat. At its trade-show demonstrations Shield AI likes to show clips where Hivemind leads 64 autonomous targets simultaneously. This is a demonstration in a controlled environment, not a confirmed combat capability. Full mission autonomy under real conditions is so far an unconfirmed class of tasks, neither for Hivemind nor for any other Western stack. And here the same lesson works as in the case of the "Lancet": a demonstration is not equal to combat use."

[Transition to s22.]

### [Slide 22 — X-62A VISTA + Saker Scout] 41:30–43:45

[On the slide — DARPA X-62A VISTA + a timeline; Saker Scout (Brave1, Ukraine) + AI mother-drone.]

"DARPA ACE X-62A VISTA — the world's first real-time aerial combat of AI against a human. A modified F-16 in which an AI agent controls the aircraft.

December 2022 — the start of testing. September 2023 — the first combat of AI against a crewed fighter: defensive and offensive maneuvers, 2,000 feet nose-to-nose at a speed of 1,200 miles per hour. May 2024 — US Air Force Secretary Kendall personally flew in the X-62A under AI control.

[slowly, anti-hype]

And again — the anti-hype caveat. X-62A is a narrow, pre-scripted scenario. One-on-one aerial combat in a known zone. Beyond-visual-range combat is excluded. Fuel management is not covered. Rules of engagement were not taken into account. "AI will replace pilots in real combat" — this is a marketing extrapolation from a narrow demonstration. The reality is closer to Fury — a wingman, not a replacement.

[I point at the right column]

And in parallel — the Ukrainian Saker Scout. One of the most combat-tested loitering munitions with autonomous recognition. It identifies autonomously up to 64 targets, a range of about 10 kilometers, transmits coordinates under electronic jamming. Part of Brave1 — the state platform of Ukraine with more than 300 AI developments. In 2025 a carrier drone appeared, delivering two strike drones with AI onboard over 300 kilometers behind the front line.

The level — L2, semi-automatic. AI recommends a target lock. The operator confirms every trigger."

[Transition to s23.]

### [Slide 23 — Geran-2 + Cognitive Pilot] 43:45–46:00

[On the slide — a photo of the Shahed/Geran-2 + the figure "~2700-3000/month production"; a photo of a KAMAZ with Cognitive Pilot.]

"Russia in the Act link. "Geran-2" — based on the Iranian "Shahed-136," produced in the Alabuga special economic zone. By the end of 2025 — about 2,700-3,000 drones per month. Planned capacity — five thousand and more. Total volume — more than 26,000 units by late spring 2025.

The evolution of AI onboard: analysis of debris recovered by the Ukrainian side shows NVIDIA Jetson modules, high-resolution cameras, thermal imagers, programmable logic arrays. In 2026 a variant with an anti-radiation homing head appeared.

[pause]

A caveat on "autonomy." Debris analysis confirms machine learning onboard. But the real role of autonomous decision versus operator override is not confirmed. Most strikes remain under operator control plus GPS guidance.

And an engineering footnote — the supply chain. Documented: 1,111 Dell PowerEdge servers with GPUs were sent through the Indian Shreya Life Sciences to Russia in April-August 2024. The hardware supply chain is a strategic risk that is not closed by software.

[I point at the right column]

And a civilian analog. Cognitive Pilot — a joint venture of Sber and Cognitive Technologies. Autonomous systems for agricultural machinery, urban transport, the railway. The stack: computer vision plus radar plus lidar. Plans — up to 50,000 systems a year.

Cognitive Pilot is not identified as a defense supplier. This is a civilian analog of the autonomy of "Geran-2": the same stack, but for civilian transport. Russian AI is not reducible to the military."

[Transition to s24.]

### [Slide 24 — MCAS + Patriot + Replicator failures] 46:00–51:30

[On the slide — photos of a 737 MAX and a Patriot, a timeline of the crashes 2018-2019, 4 MCAS lessons.]

"The canonical failure of the Act link that I want us to remember — the Boeing 737 MAX MCAS.

Lion Air 610, October 2018 — 189 dead. Ethiopian Airlines 302, March 2019 — 157 dead. 346 people. A 20-month suspension of operations.

The Boeing 737 MAX received larger engines. This shifted the aerodynamic center. Boeing's solution — a software one. MCAS automatically corrects the position of the stabilizer downward. The system was activated by a single angle-of-attack sensor. Without redundancy. When the sensor gave a false reading, MCAS repeatedly commanded "nose down," and the pilot could not override the command. Neither training nor an understanding of the system.

[slowly]

MCAS — not AI in the strict sense. But pedagogically this is the canonical anti-pattern for all safety-critical AI systems. Four lessons.

**Lesson one.** A single point of failure. One model, one sensor. Never make safety-critical systems dependent on a single sensor.

**Lesson two.** Opacity. The pilots did not know MCAS existed. If the operator does not know what the system does, no override works.

**Lesson three.** Software does not cure hardware. Software patches for physical problems are a dangerous path. A second angle-of-attack sensor would have cost orders of magnitude less than all the costs of a corrective AI.

**Lesson four.** The FMEA and FTA analyses were not passed. FMEA — Failure Mode and Effects Analysis. FTA — Fault Tree Analysis. These are standard engineering procedures in aviation. A single point of failure should have been caught at this stage.

[pause]

This analysis works further. F-35 ALIS — a failure of redundancy. Lavender — a failure of FMEA. And now — Patriot.

Patriot in 2003 in Operation Iraqi Freedom. A British Tornado GR4 and an American F/A-18C — both shot down by their own Patriot batteries. The Tornado was misclassified as an Iraqi anti-radiation missile; the identification-friend-or-foe query received no answer. Operators perceived the automatic mode as "better than a human" and relaxed their oversight. The tendency to trust the automation in its pure form.

Lesson: when the automation is statistically "better than a human," operators stop double-checking it. Engineering design must deliberately create friction for critical decisions, not remove it.

[pause, transition to the third failure]

And the third canonical failure of the Act link — the DoD Replicator program. The US Department of Defense in August 2023, through Deputy Secretary Kathleen Hicks, announced the goal: to field tens of thousands of expendable autonomous platforms by August 2025. A response to China's numerical advantage in platforms.

What happened. September 2025: hundreds of systems delivered, not thousands. A difference of an order of magnitude. Replicator-2 reoriented to counter-UAS. In December 2025 the program was de facto renamed DAWG with a focus on larger platforms and smaller quantities.

[slowly]

The root cause — not an inability to produce the hardware. Producing 10,000 drones a month is possible. The root cause — a lag in software integration. Command-and-control software for coordinating heterogeneous drones from different vendors is a gigantic systems-engineering challenge. Swarm software is the weakest link.

**The Replicator lesson.** The hardware exists. Software integration is a different time horizon. The readiness of an AI component is not the readiness of an AI system for deployment. When you see a program in the style of "thousands of drones by such-and-such a year" — ask the question: what will the supplier make by that date? Hardware? Software? The integration between them? Slowing down under an honest assessment is better than premature scale with marketing hype.

[pause]

The criteria of the Act link — the fifth and the sixth. Fifth: autonomy is not needed, the human is slower but safer — MCAS as "a solution to a problem that might not have existed." Sixth: an off-the-shelf commercial component is cheaper and more reliable than a model on a single sensor."

[Transition to s25.]

### [Slide 25 — Section 4 divider + micro-pause] 51:30–52:30

[On the slide — the large numeral "4", the title "Boundary and regulation".]

"Section four of five. Boundary and regulation.

[slowly, a change of tone to a more direct one]

Let's catch our breath for a second. Section four is the most conceptually dense of the whole lecture. We are now going to enter the L1-L5 ladder of autonomy. This is the central model in the head of your career in this industry — not just a concept.

I will ask you to put your phones away for the next 15 minutes. This is the section that we, in essence, gathered for. If you take away from here the L1-L5, the HITL/HOOL/HOTL triad, and the 6 canonical criteria — this lecture is already enough.

Ready? Let's go."

[Transition to s26.]

---

## Section 4. Boundary and regulation (≈13 min)

### [Slide 26 — The L1-L5 ladder of autonomy] 52:30–56:00

[On the slide — a 5-row table: L1 Assistive → L2 Semi-auto → L3 Supervised → L4 Pre-authorized → L5 Full LAWS. With 2026 examples and ms-to-intervention.]

"To talk about the boundary, we need a common scale. The industry uses the L1-L5 ladder — an analog of the SAE levels of autonomy for cars. By 2026 this is the most cited scale for weapon autonomy.

The key — at each level it explicitly states what AI does and what the human does.

[I read from the table slowly]

L1, assistive. AI issues detections. The human decides. Example — Palantir MSS. The time available to the human to intervene — minutes and hours.

L2, semi-automatic perception. AI recommends an action. The human authorizes each one. Example — Saker Scout. The time to intervene — seconds.

L3, supervised autonomy. AI executes in a pre-authorized corridor. The human watches the execution. Example — the Anduril Fury wingman. The time to intervene — 100-1,000 milliseconds.

L4, pre-authorized automatic engagement. AI opens fire under pre-established rules of engagement. The human may intervene but is not obliged to be in the loop. Example — the automatic mode of Patriot. The time to intervene — less than 100 milliseconds.

L5, full lethal autonomy. AI executes a lethal action without human authorization. The human is out of the loop. Today a subject of negotiations, not deployed practice.

[pause]

Two boundaries to pay attention to.

The L3 — L4 boundary is the place of an engineering dispute. The pre-authorized corridor — how narrow is it? If an operator pre-authorized "open fire on any object in zone X," and that zone is a large city, — this is de facto L5, covered by an L4 slip of paper. Engineering must quantify the width of the corridor.

The L4 — L5 boundary is the place of a legal dispute at the UN. L5 is formally deployed nowhere. The negotiations are precisely about fixing this in law. Even Lavender formally requires human approval — albeit a 20-second one — that is, formally this is the L4 boundary, not L5. This is pointed out by the ICRC and the Stop Killer Robots coalition (more than 30 countries): the ban must cover functional autonomy, not a formal signature. And this is a difference we must keep in mind.

[slowly, summary]

The pedagogical conclusion. An engineering student must be able to say about a system what level it sits at. Not "autonomous," but "L3 with a corridor of width X." This is the professional language."

[Transition to s27.]

### [Slide 27 — UN GGE timeline + ICRC] 56:00–58:15

[On the slide — a UN GGE timeline 2024 161/3/13 → 2025 164/6/7 → 2026 treaty goal. + 2 key ICRC formulations.]

"The UN GGE on lethal autonomous systems — the main international forum for negotiations. Established in 2016. Over three years a shift — from "we are discussing whether a treaty is needed" to "we are working on a text."

November 5, 2024 — the First Committee of the UN General Assembly: 161 for, 3 against, 13 abstentions. Against — Belarus, North Korea, Russia.

November 6, 2025 — the third consecutive resolution: 164 for, 6 against, 7 abstentions per the official UN press release. Per the Stop Killer Robots coalition — 156 for, 5 against, 8 abstentions. The discrepancy is due to the counting methodologies. Against in 2025 — Belarus, Burundi, the DPRK, Israel, Russia, the US. A significant shift: the US in 2024 — "for," in 2025 — "against."

September 2025 — 42 states signed a joint UN GGE statement, the working text was declared a sufficient basis. The goal of the UN Secretary-General — a treaty by 2026.

[pause]

In parallel — the ICRC, the International Committee of the Red Cross. The main authority on the application of international humanitarian law. Two key formulations.

The ethical core: the transfer of life-and-death decisions to machine sensors and software is a process of dehumanization.

The procedural core: it is not the weapon system that must comply with international law, but the people who use it.

The first says what. The second — who. In both, the central subject is the human."

[Transition to s28.]

### [Slide 28 — The exit from Maven → the return of the big AI companies] 58:15–60:30

[On the slide — a timeline of 3 eras: 2018 Maven walkout / 2018-2024 vendor consolidation / 2024-2026 big-tech return.]

"To understand the discussion between the big AI companies and defense — the Maven program.

In March 2018, through a leak, it became known that Google was helping the Pentagon analyze drone footage. More than 4,000 employees signed an open letter. About 12 engineers resigned voluntarily. By June 2018 Google does not renew the contract.

[pause]

Google managed to leave. The Maven program — did not. The contract was picked up by Anduril, Palantir, and Scale. By 2026 MSS reached 1.3 billion dollars.

**Lesson one.** Personal ethics is not equal to industry regulation. Only legal regulation blocks broad adoption.

**Lesson two.** "Not working for the Department of Defense" is now a rare luxury.

[I point at the slide]

From 2018 to 2026 — a shift. January 2024 — OpenAI removed the ban on military use. November 2024 — the partnership of Anthropic, Palantir, AWS, Claude at the IL6 level. 2024 — Cohere in classified loops. 2025 — Mistral, defense partnerships with the EU. September 2025 — Google returns through Google Cloud.

[slowly]

The story arc. The exit from Maven in 2018 → vendor consolidation → the return of the big AI companies in 2024-2026. Just 6 years. The AI industry went through a cycle from "refusing military contracts" to "military contracts are a critical revenue line."

What this means. When you choose a company, you choose its position in this drift. A legitimate engineering decision — but it must be a conscious one."

[Transition to s29.]

### [Slide 29 — The HITL / HOOL / HOTL triad] 60:30–62:45

[On the slide — 3 panels: HITL (L1-L2), HOOL (L3-L4), HOTL (L5). + ms-to-intervention as an axis.]

"The most important model in the head of this section — the triad of levels of human control. The same L1-L5 levels, but a view from the opposite side.

HITL — human-in-the-loop. The human at every decision point. AI does not act without explicit authorization. Correspondence — L1, L2.

HOOL — human-on-the-loop. The human watches the cycle, can intervene, but is not obliged to be at every decision point. Correspondence — L3, L4.

HOTL — human-out-of-the-loop. The human outside the execution cycle, without the ability to intervene in real time. Correspondence — L5.

[slowly]

What matters for a graduating engineer? The HOOL → HOTL boundary is the place that US DoD Directive 3000.09, the UN GGE working text, and the ICRC position are all focused on. This boundary is formally defined by an engineering decision: how many milliseconds the operator has to intervene.

If 10 seconds — HOOL. If 200 milliseconds — formally HOOL, factually HOTL. If 5 milliseconds — this is already HOTL.

The engineering conclusion. "How many milliseconds the operator has" — the formal categorization of the system, and it has legal consequences in the new international regime. The answer must be fixed in the system requirements, not in the marketing.

The connection to the failures. Lavender — a degenerate HITL: 20 seconds is HOTL under the mask of HITL. MCAS — the absence of a meaningful ability to override the automation: the pilot formally could cancel the command, but the information was not there."

[Transition to s30.]

### [Slide 30 — Russia's votes + 3 actions for the engineer] 62:45–65:00

[On the slide — a map of the 2025 votes + 3 actions for the engineer.]

"Russia votes against the UN resolutions on lethal autonomous systems. November 2025: 164 for, 6 against, 7 abstentions per the UN; 156 for, 5 against, 8 abstentions per Stop Killer Robots. Against — Belarus, Burundi, the DPRK, Israel, Russia, and the US.

The shift: the US in 2024 — "for," in 2025 — "against." Russia — against since 2018. But the "against camp" in 2025 is more than three countries, and its composition is politically diverse.

[pause]

This is a fact. What is the engineer to do with it?

We do not prescribe a political position — that is each person's choice. But we are obliged to give the landscape. Three actions.

**Action one.** Know the landscape. UN GGE, ICRC, the General Assembly votes, US DoD Directive 3000.09 — professional literacy, like knowing the Federal Aviation Regulations.

**Action two.** Know that HITL/HOOL/HOTL and L1-L5 apply regardless of geopolitical alignment. Engineering design is defined identically.

**Action three.** Make a conscious choice within the frames. You can go into dual-use — Cognitive Pilot, TERRA TECH. You can go into defense at L1-L2. You can go at L3-L4. Each choice is legitimate, but different.

[slowly]

In this area the engineer does not remain neutral — he is inside the frames. Professionalism is how consciously he senses these frames. States vote differently. Engineering design is defined identically.

The seventh criterion: the HOOL → HOTL boundary is the territory of an international treaty, not of engineering. When you design near the boundary, you enter the zone of international law."

[Transition to s31.]

### [Slide 31 — Section 5 divider] 65:00–65:15

"Section five of five. Assembly: criteria, career, closure."

[Transition to s32.]

---

## Section 5. Assembly (≈7 min)

### [Slide 32 — The seven-criteria matrix] 65:15–68:00

[On the slide — a table of 7 rows × 3 columns: # / link / criterion / illustration. A gold accent on #4 (Lavender) and #5 (MCAS).]

"Let's assemble into one matrix all six criteria by section plus one cross-cutting one — a total of seven criteria for "when not AI."

In the Sense link — two. First: a domain with a small volume of data or a distribution shift. The illustration — adversarial attacks on synthetic-aperture-radar target recognition. Second: a decision with a life-cost on a single sensor without redundancy. The illustration — F-35 ALIS without a human in the loop for flight authorization.

In the Decide link — two. Third: edge cases on the long tail of the distribution with low confidence, a structural decision refusal is needed. The illustration — planning tasks under new rules of engagement. Fourth: a decision with a life-cost without a formal human in the loop. The canonical counterexample — Lavender.

In the Act link — two. Fifth: autonomy is not needed, the human is slower but safer. The canonical example — the 737 MAX MCAS as "a solution to a problem that did not exist." Sixth: an off-the-shelf commercial component is cheaper and more reliable. A second angle-of-attack sensor would have cost orders of magnitude less than all the corrective AI systems.

And one cross-cutting, seventh: the HOOL → HOTL boundary is the territory of an international treaty, not of engineering. This is about lethal autonomous systems and the UN GGE.

[slowly]

The main thing — this is a tool. Not a slogan, not a dogma. When you are offered an AI solution for an aerospace or defense task, we run it through the seven criteria. If even one triggers — this is not "you may not," this is "a review is needed." If several — it is worth reconsidering the fundamental approach.

The matrix is not dogma. It works in 2026 with the data we have. In 5 years, perhaps, new criteria will appear — for example, about the energy consumption of AI systems in combat conditions. This is a working tool that must be updated with experience."

[Transition to s33.]

### [Slide 33 — The career angle + reading] 68:00–70:30

[On the slide — 3 columns: profiles + Russian dual-use + the global loop.]

"Without evangelizing — real career paths.

The Russian academic loop. Specialized technical universities offer master's programs in AI in control systems and space engineering. Themes: AI systems, computer vision for satellite analytics, machine learning on embedded systems. Access through university channels gives a deeper conversation.

Civilian dual-use in Russia. Cognitive Pilot — autonomy of agricultural machinery. VisionLabs — computer vision. TERRA TECH, SCANEX, SPUTNIX — satellite analytics.

The global loop. Boeing, Airbus — predictive maintenance, avionics. Lockheed Martin, Northrop Grumman, RTX — the large defense contractors. Anduril, Palantir, Helsing, Shield AI, Scale AI — the new-generation defense AI startups. NASA, ESA — space science. Electric vertical-takeoff aircraft — Joby Aviation, Wisk Aero.

Profiles. Computer vision and deep learning — satellite analytics. Machine learning and reinforcement learning — autonomous platforms. Embedded systems — on-orbit processing. Systems engineering and safety — certification under DO-178C and ARP4754A. Ethics and law — the UN GGE process and interaction with the ICRC.

The main thing — there is a choice. And it does not reduce to "either the military industry or nothing." The civilian aerospace industry is a full-fledged professional field.

[pause]

A list for those who want to go further. Paul Scharre, "Army of None," 2018. CSIS Bondar, April 2026 — the Russian ecosystem of drones with AI. Abraham, +972 Magazine, 2024, on Lavender. ICRC, position document 2024. DARPA ACE briefings. US Government Accountability Office reports on ALIS and ODIN. Stop Killer Robots coalition briefing, 2025."

[Transition to s34.]

### [Slide 34 — Closing callback] 70:30–72:45

[On the slide — a repeat of the OODA chain visual from s05. In the center — a gold callout "The chain is still held by the engineer".]

"We have gone through the Sense → Decide → Act chain three times in this lecture. The first — positively, where AI works. The second — critically, where AI breaks. The third — the meta level, where AI is trimmed by regulation.

[slowly, the central thought]

The main thought I want to leave you with today — the chain is still held by the engineer.

AI entered every link but did not replace the human. It accelerated Sense — but Sense without human verification does not work: ALIS, GPS spoofing. It accelerated Decide — but Decide without a real human in the loop turns into Lavender. It expanded Act — but Act without supervised pilots does not leave the demonstration stage: X-62A, "Lancet." And now we know one more slice — Replicator: even when the hardware exists, software integration lags by orders of magnitude.

The same computer-vision and machine-learning pipelines, the same sensor stacks work in both civilian aerospace and defense. The engineer chooses the loop.

[3-second pause]

This does not mean that AI is "small" or "deceptive." It means that in an industry with a life-cost of error, AI is a tool in engineering hands, not an autonomous subject. Professionalism is the ability to say "yes" where AI gives a measurable advantage. And "no" where AI creates a risk that is not closed by a single model.

[slowly, finale]

The chain is still held by the engineer.

Thank you."

[Transition to s35.]

### [Slide 35 — Q&A] 72:45–75:45+

[On the slide — a large "Q&A" + contacts + a compact reading list.]

"Next — your questions. I have ready answers in reserve for the typical tricky questions. If something was not mentioned — ask. If something remained unclear — ask. If you want to argue against — ask, these are the most valuable questions."

[Open Q&A. Below — ready theses for the lecturer.]

---

## Q&A — reserve theses for the lecturer

### Q1. "If the ICRC and the UN GGE are so concerned about lethal autonomous systems, why do the US, Russia, and China not sign a concrete treaty?"

Three reasons. Military capability: each of the three great powers invests in autonomy as a strategic advantage. Diplomatic — definitions: in the UN GGE there is no single agreed definition of lethal autonomous systems. Technical — monitoring: how do you verify whether a country is or is not using autonomy? This distinguishes lethal autonomous systems from the Chemical Weapons Convention, where inspections are possible.

### Q2. "And what about Russian large language models for space?"

As of May 2026, the source of this information is a single one, from the Russian side. Independent verification is absent. We deliberately do not include it in the main analysis. If confirming data appears later — we will reassess.

### Q3. "Aerostate is mentioned in the press as a Russian aviation-weather AI company. Is it worth dissecting?"

A search in open sources did not find confirmed information about Aerostate as an identifiable Russian startup in the area of aviation weather analytics on AI. The recommendation — do not mention it without an explicit additional source. To illustrate Russian dual-use, we use confirmed names — Cognitive Pilot and VisionLabs.

### Q4. "What can the closed Russian programs of the Ministry of Defense and Roscosmos on AI actually do?"

There is little open data. What we know is an external projection through CSIS, the Russian press, debris analysis. Internal programs are not published. We avoid hypotheses. If interested — the path is through the academic loop, where access is via university channels.

### Q5. "Lavender is discussed with condemnation. And what about the criticism of +972 — maybe they exaggerated?"

The IDF officially denies it. +972 relies on the testimony of six officers of Israeli intelligence. Independent reproduction is impossible. The ICRC and the Lieber Institute — both authoritative legal institutions — dissected the case as a serious subject of discussion. Even under the most conservative assessment — this is a serious case. We make no moral judgment about the IDF; we make an engineering judgment about the pattern "accuracy percentage as the wrong metric" — it does not depend on which side made the error.

### Q6. "If the 737 MAX MCAS is not AI, why dissect it?"

MCAS — the canonical anti-pattern for all safety-critical AI systems: a single point of failure, opacity, software patches for physical problems, a failure of FMEA. All these patterns apply directly to AI systems. AI makes each of them worse, not better.

### Q7. "Where should I go to work in 2 years if this area attracts me but I do not want a defense load?"

Three directions. Civilian satellite analytics — TERRA TECH, SCANEX, SPUTNIX in Russia; Maxar, Planet, BlackSky internationally. Civil aviation — Boeing, Airbus, Wisk Aero, electric vertical-takeoff-aircraft startups. Dual-use civilian transport — Cognitive Pilot.

### Q8. "And does Russian AI satellite analytics really work or is it PR?"

TERRA TECH — a publicly confirmed BRICS 2024 agreement. SCANEX — the only operator of direct data reception in Russia. SPUTNIX — more than 100 CubeSats. This is publicly documented. The machine quality of specific models is not published — as with Maxar or BlackSky. Not PR in the sense of "there is nothing," but also not full transparency.

### Q9. "What if AI does the work so much better that human control simply slows it down?"

This is the main question of the UN GGE debates. The ICRC's answer: it is not the weapon system that must comply with international humanitarian law, but the people who use it. A human in the loop is not a question of optimization, it is a legal requirement. The task of engineering is to find solutions in which the human remains but the pace does not slow dramatically.

### Q10. "What do you yourself think — will there be a treaty on lethal autonomous systems by 2026?"

A personal opinion — doubtful. The goal of the UN Secretary-General is ambitious. But the structural reasons (the capability gap between countries, the definitions problem, the verification problem) make a binding treaty by the calendar year 2026 unlikely. More realistic — a working text as a political signal, without binding obligations, by 2027-2028. This is speculation, not a forecast.

---

*End of speech. Version v2. Ready for the Phase 11.5 pre-gate walkthrough.*
