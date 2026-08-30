---
lecture: 10
title: "Lecturer's speech — AI in agriculture"
audience: "студенты-инженеры 3 курса (универсальная)"
duration_min: 75
status: draft
version: v2
date: 2026-05-21
issue: 126
source_of_truth: false
derived_from: ["chapter.md (v3.3 finalized)", "chapter-part2.md", "chapter-part3.md", "deck.yaml v2", "43 slides/*.md"]
length_words: "~5940 (5510 narrative + 430 Q&A backup)"
length_min: 75
pacing_target: "≈73 мин активной речи + 2 мин Q&A buffer; cap 95 wpm на любом фрагменте"
pacing_actual: "v2 после s25 split + atomic edits — re-verify before record"
inclusive_markers_actual: "13 «мы с вами» distributed across 7 content sections"
bridge_phrases_actual: "6 dividers — «Раздел первый/второй/третий/четвёртый/четыре-бис/пятый из пяти»"
slides_covered: "43 slides (s01-s38 + 5 sub-IDs s30b/s37s/s38s/s35c/s36c) — все из deck.yaml v2"
strict_in_self_estimate: "~42% strict holistic, distributed по §1-§6 (failure-блоки F1-F11 + 5 анти-AI критериев + Раздел Среды + альтернативы для каждого случая)"
keystone_axis: "Лестница AI-проникновения в АПК — от поля к полке (L1 → L5)"
inclusive_markers_total: "≥12 «мы с вами» distributed across all 7 sections"
bridge_phrases: "7 dividers — «Раздел N из пяти» (Р1-Р5 + Р4-bis Среда)"
failure_blocks: "11 canonical: F1 vertical farming · F2 ChatGPT hallucinations · F3 Plantix · F4 Monarch · F5 FarmWise+Naïo · F7 strawberry · F8 Cainthus/tie-stall · F9 РФ dairy uncertainty · F10 USDA cancellation · F11 Verra phantom · плюс GNSS-jamming / Мелитополь как Среда-провалы"
anti_anglicism_self_grep: "v2 Russification pass — <15 critical narrative hits target после finalize"
excluded_items: "0 hits для МГТУ/Бауман/ИУ/МСХА/Тимирязевка; career section в родовой форме"
changelog_v2: "Phase 11 batched revision (issue #126): P0 Bowery $700M+ + AppHarvest $475M SPAC+$341M debt + AgFunder -53% novel farming (не -91% AI поля); P1 Tzachor ноябрь 2023 + Магнит F&R 4-я card в §5 + ЭФКО + Русагро Тех в s36c + Tacit knowledge в s12 + Sustainability paradox в s37; anti-anglicism atomic swaps (production → промышленная эксплуатация, vendor lock-in → привязка к поставщику, compliance → соответствие требованиям, supply chain → цепочка поставок, takeaway → главный вывод, state vector → вектор состояния, online learning → обучение в потоке, slippage → проскальзывание, notional → номинал, agentic → агентный); s25 pacing split"
---

# Lecturer's speech · Lecture 10 "AI in agriculture"

**Duration:** 75 minutes (≈73 min of active speech + 2 min Q&A buffer; plus another 10 min of dedicated Q&A afterward).
**Audience:** third-year engineering students, general — not agriculture specialists.
**Slides:** 43 (34 content + 7 dividers + cover + Q&A).
**Pace:** target 80–85 words per minute; hard ceiling 95 words per minute on any fragment.
**Delivery date:** May 21, 2026.
**Source of truth:** chapter v3.2 (finalized, 3 parts, ~32,000 words) + slides v2 (43 rendered).

---

## Preparation before the lecture (24–48 hours ahead)

- **[Presentation file]** Open `library/lectures/lec-10/rendered/lec-10.pptx` (5.17 MB, 43 slides). Check that it opens on the projector and that fonts are intact.
- **[s01 freshness]** Open `https://techcrunch.com/2025/03/24/plenty-vertical-farming-bankruptcy/` — confirm the Chapter 11 date of March 2025 and the –99% valuation.
- **[s07 freshness]** Open `https://www.deere.com/en/news/all-news/see-spray-technology-across-5-million-acres/` — confirm 5 million acres for the 2025 season.
- **[s16 freshness]** Open `https://carbonrobotics.com` — confirm 250,000 acres and 14 countries.
- **[s17 freshness]** Verify the number of Cognitive Pilot installations: vendor self-report, May 2024 = 1,700+. If newer, mention it.
- **[s19 freshness]** Open `https://techcrunch.com/2026/04/15/caterpillar-acquires-monarch-tractor/` — confirm the date of April 15, 2026.
- **[s28 freshness]** Open `https://www.cargill.com/2026/cargill-wins-2026-big-artificial-intelligence-excellence-award` — confirm it is still current.
- **[s32 freshness]** Open `https://habr.com/ru/companies/magnit/articles/1023866/` — verify Forecasting on 46 distribution centers + Replenishment pilot on 3 distribution centers.
- **[s34 freshness]** Confirm the status of the Starlink ban in Russia (April 30, 2026, 6 months) and the ICAO 2025 report on GNSS interference (122,000–123,000 flights in Q1 2025).
- **Read aloud with a stopwatch** the key fragments: [s01 Plenty hook], [s11 5-Why], [s17 Cognitive vs ITELMA], [s19 Monarch timeline], [s29 hedge pseudo-flow], [s37 closing]. Each — within its allotted timing (max 95 words per minute).
- **Callbacks for self-check:** Plenty Compton (s01) → keystone ladder (s05) → 5 anti-AI criteria (s38s) → closing payback (s37). These points form a single arc.
- **Backup plan:** if the projector fails — PDF on the laptop `library/lectures/lec-10/rendered/lec-10.pdf`. If the laptop fails — a paper checklist.

---

## Section 0. Entry — Plenty Compton and the ladder (≈7 min)

### [Slide 1 — Plenty Compton, "before and after" frames] 0:00–2:00

[On screen — two frames: on the left, the Los Angeles mayor's delegation, ribbon, reporters, May 2023; on the right — an empty warehouse with boarded-up windows, December 2024.]

"Hello. Before we say the first word about agriculture — look here.

[pause 3 seconds]

May two thousand twenty-three. Compton, California. The opening of the flagship of American vertical farming — the Plenty Unlimited greenhouse. The mayor's delegation. Reporters. A promise: four and a half million pounds of leafy greens a year — on an AI-managed farm optimizing light, nutrition, and climate at the level of the individual plant.

[pointing to the right frame]

December two thousand twenty-four. Nineteen months later — the facility is closed. March two thousand twenty-five — Chapter 11. Lost raised capital — about nine hundred forty million dollars. Valuation: from one billion nine hundred million down to less than fifteen million. Minus ninety-nine percent.

[pause]

Let us dwell on a question we will return to at the end of the lecture: what exactly did AI do in this failure — and in what sense could it not?

This is not 'AI is bad.' The microclimate controller worked. Computer vision recognized growth stages. Yield models were trained. What did not work — we will unpack in the finale."

[Transition to s02.]

### [Slide 2 — Cover] 2:00–2:15

"Lecture ten. AI in agriculture."

[Transition to s03.]

### [Slide 3 — Lecture map] 2:15–4:00

[On the slide — seven horizontal cards.]

"This lecture is built as a ladder. Of five levels — from field to shelf. At the bottom — an open field with dust, rain, pathogens. At the top — a store shelf with a digital trace on every SKU.

And at each step AI works differently. Somewhere excellently, somewhere catastrophically badly. The main skill you and I are training today is, for a specific task, to name the step and apply the right tool. Or to say 'AI is not needed here' and name the alternative. Let me flag this right away: this is exactly the engineering judgment we are learning.

Today there will be eleven failures unpacked. Plenty Compton — nine hundred forty million in losses. Monarch Tractor — lawsuits and the Caterpillar acquisition. ChatGPT as an agronomist — confident-wrong on pesticides. Plantix — ten to fifteen percent misdiagnosis. USDA Climate-Smart — canceled in a day. Verra phantom credits — ninety-four percent fakes. Five more cases along the way.

The tone — 'trust but verify.' We take apart what works, where it breaks, where the line runs that the engineer does not cross by a vendor's decision."

[Transition to s04.]

### [Slide 4 — Glossary] 4:00–4:50

[On the slide — two columns: closed-loop vs open-environment + 5 terms from L4.]

"Two formulations and five terms.

Open-environment AI — in a real field: dust, weather, pathogens. Closed-loop AI — inside a closed-loop within a controlled environment: greenhouse, factory, operating room. This working formulation appeared in Lecture seven on medicine.

Five supply-chain terms. Agentic AI — with an inference loop and tools. Basis points — one hundred equal one percent. Hedge divergence — the difference between the expected and the actual price. Scope 3 emissions — across the entire chain. AI-MRV — measurement, reporting, and verification systems for carbon credits."

[Transition to s05.]

### [Slide 5 — Keystone: the five-level ladder] 4:50–6:50

[On the slide — a vertical ladder of five steps from bottom to top + an arrow on the right.]

"Here is the ladder. Five levels.

First — the field. An open biological environment. AI works on narrow tasks — See & Spray from John Deere. It breaks in attempts to build an 'AI agronomist' and a closed-loop through vertical farming.

Second — the robot. A semi-controlled environment. AI works in narrow specializations — the Carbon Robotics laser weeder. It breaks on universal 'autonomous tractors' like Monarch.

Third — the animal. A semi-closed environment. AI works more stably — Allflex SenseHub monitors two million cows.

Fourth — the supply chain. Controlled flows plus fast feedback in basis points. Agentic AI leads. Cargill CMAX received the BIG AI Excellence Award.

Fifth — the consumer. A fully digitized environment. AI works reliably at Walmart, Tesco, X5.

[slowly]

The main point. The higher the step — the higher the controllability, the lower the biological unpredictability, the higher the measurable return. This explains the paradox. Venture investment in indoor farming and novel farming systems collapsed — minus fifty-three percent year over year according to the AgFunder Global AgriFoodTech Investment Report of two thousand twenty-five: for the first three quarters of twenty-five, one and a half billion dollars versus three and two-tenths billion for twenty-four. And investment in agentic AI for commodity trading is growing double-digit. The reason — the speed of feedback. The trader — basis points in minutes. The farmer — the result of a fertilizer application in five to six months."

[Transition to s06.]

### [Slide 6 — Section 1 divider] 6:50–7:05

"Section one of five. The field — an open biological environment."

[Transition to s07.]

---

## Section 1. L1 — The field (≈14 min)

### [Slide 7 — See & Spray Ultimate] 7:05–9:00

[On the slide — a photo of a sprayer in a field + a card of figures.]

"The canonical working case of the first step — See & Spray Ultimate from John Deere.

A standard sprayer. On the boom — thirty-six cameras. Each one, through a convolutional neural network, recognizes weeds and crop plants in real time. The decision — spot spraying of weeds only.

Let us look at the figures for the two thousand twenty-five season. Five million acres — about half a percent of the nine hundred million acres of US cropland. Minus fifty percent herbicides. Plus two bushels of soybeans per acre. Edge ML on NVIDIA Jetson — latency under fifty milliseconds. This is critical: the tractor moves at sixteen kilometers per hour, recognition must be instantaneous.

[slowly]

What works. A narrow task — to spray or not. A measurable return. Edge computing without cloud dependency. And no marketing promises of 'full autonomy.' The sprayer remains a sprayer; AI optimizes one step. You and I will see this pattern many times: AI works on narrow tasks with fast feedback."

[Transition to s08.]

### [Slide 8 — Vendor matrix L1] 9:00–11:00

[On the slide — a 5-by-5 table.]

"Besides Deere — five platforms of the first step, and let us look at them together. xarvio from BASF: since October two thousand twenty-five it offers a rice-yield contract in Japan. Climate FieldView from Bayer — two hundred fifty million acres of subscriptions, price five dollars per acre. Cropwise from Syngenta — an open platform for developers. Granular from Corteva. Taranis — satellite analytics.

The main skill on this slide is to map the mode of operation, not the brand. Two hundred fifty million acres of FieldView — that is the number of subscriptions, not 'AI optimizes every acre.' The AI inside itself — mostly rule-based recommendations plus satellite analytics.

And an important fact. Climate FieldView in two thousand twenty-two exited Russia together with Bayer Crop Science. Russian agricultural holdings lost access to the platform all at once. This is the first illustration of what we will unpack in the Environment section as vendor lock-in. A cloud-dependent AI service from a foreign jurisdiction has already been shut off in agriculture after two thousand twenty-two. Let us remember."

[Transition to s09.]

### [Slide 9 — Foundation models 2026] 11:00–12:30

[On the slide — a Sentinel-2 satellite image + a foundation-model diagram.]

"What is new in two thousand twenty-five to twenty-six. Foundation models for Earth observation. TerraMind from IBM and ESA. Prithvi-EO 2.0 from NASA and IBM. AgriFM from the University of Hong Kong and Wuhan University. Crop Wizard from the University of Illinois — this is a RAG application on top of a foundation model.

What changes. Previously, a team of two or three engineers could not train a CV model — it required millions of labeled images and large GPU infrastructure. Now the same team fine-tunes TerraMind on thousands of images. The barrier to entry dropped by two orders of magnitude.

But there is a risk. Concentration on two or three foundation models — IBM, NASA, ESA. The entire L1 industry is built on top of a few foundation ones. This is the same vendor lock-in, only at the level of the model."

[Transition to s10.]

### [Slide 10 — Vertical farming — a failure not due to bad AI] 12:30–14:30

[On the slide — a three-by-three mini-table + an interior photo of a vertical farm.]

"The first of eleven failures. Vertical farming as a class.

AppHarvest — four hundred seventy-five million through a SPAC plus three hundred forty-one million in debt, about eight hundred sixteen million in total disclosed financing. Bankruptcy of two thousand twenty-three, ToBRFV — tomato mosaic virus — infected all sixty acres of greenhouse within days. Plenty — nine hundred forty million in losses, as we saw at the beginning. Bowery — more than seven hundred million in raised capital, bankruptcy November two thousand twenty-four, liquidation of Locust Grove with thirty-two million in equipment that was never used. In two thousand twenty-five about fourteen vertical farms went bankrupt globally. The cumulative losses of the category — more than one and three-tenths billion dollars.

[pause]

And here is the most important thing. The AI systems inside these farms worked. The microclimate controller managed light, temperature, humidity. Computer vision classified growth stages. Models predicted yield.

What did not work — the structural economics. To that we now turn."

[Transition to s11.]

### [Slide 11 — 5-Why analysis of vertical farming] 14:30–16:30

[On the slide — a chain of five steps.]

"The five-whys method.

Step one. Plenty did not survive because the structural economics are negative — the cost of greens is higher than the market price.

Step two. High cost, because electricity for LEDs is about forty percent of operating costs.

Step three. LEDs are the main line item, because lighting in California at twenty-five cents per kilowatt-hour consumes a hundred times more energy per unit of area than a plant receives from free sun in an open field. The analysis is by Hannah Ritchie based on MDPI Sustainability.

Step four. AI did not close the gap, because it optimizes on the denominator — five to fifteen percent efficiency. The gap in the numerator — two orders of magnitude. No model closes a hundred-fold gap through a five-percent optimization.

Step five. This is exactly our first anti-AI criterion. The law of thermodynamics matters more than ML.

[slowly]

This is the first of five criteria we will return to in the finale. The alternative — open ground or an ordinary greenhouse at energy below ten cents per kilowatt-hour. Vertical farming works only for premium Oishii strawberries at ten dollars a pack — there the premium covers the energy. For commodity leafy greens — it does not work."

[Transition to s12.]

### [Slide 12 — ChatGPT/Bard as an agronomist] 16:30–18:00

[On the slide — a screenshot of a model's answer + a quote from a Nature Food article.]

"The second failure. Generic large language models as an advisory agronomist.

November two thousand twenty-three, a publication in Nature Food. Broad media resonance — May twenty-four via a Phys.org review. The lead author — Dr. Asaf Tzachor of Reichman University. The subject — scenarios of ChatGPT-model use by African farmers for the cassava crop.

What they found. One hundred eighty-four questions. GPT-3.5, GPT-4, Bard. In tens of percent of cases — a confident answer with a factual error.

[slowly]

And here is the most dangerous thing. If the model answers 'I don't know' — the farmer will turn to an agronomist. If the model answers confidently and incorrectly — the farmer will spray the field with the wrong product. A confident error is more dangerous than an honest 'I don't know.'

And there is a structural reason why a generic LLM does not work here. The farmer's tacit knowledge of his own specific field — what he knows from years of observation, which is neither in satellite images nor in IoT data. This is precisely tacit knowledge. A generic LLM will not build this model from satellite and sensors in one season. RAG grounding to a local regulator is a necessary but not sufficient step. A human expert as a mandatory link in the loop — is necessary.

The criterion: a generic LLM as an advisor for decisions with a high cost of error is a categorical anti-pattern. The alternative — a RAG application grounded to a local regulator. Plus abstention at low confidence. Plus a human in the loop."

[Transition to s13.]

### [Slide 13 — Plantix] 18:00–19:30

[On the slide — a screenshot of the Plantix mobile interface + an error breakdown.]

"The third failure. Plantix — a mobile app for diagnosing plant diseases from a photo of a leaf.

Ten million downloads, about seven million active in India. In India — one hundred twenty million smallholder farms. Ten million Plantix downloads — about eight percent coverage.

The claimed accuracy — eighty-five to ninety percent, there are no independent production metrics. Ten to fifteen percent misdiagnosis on ten million downloads — that is roughly one hundred thousand incorrect pesticide recommendations a year.

[slowly]

And here is the critical analysis. Ninety percent accuracy sounds like 'a good model.' At such a scale in production deployment — hundreds of thousands of mistakenly sprayed fields.

The criterion: threshold accuracy does not equal readiness for production rollout. The alternative — a model with an explicit measure of uncertainty. If confidence is below the threshold — the app declines the recommendation."

[Transition to s14.]

### [Slide 14 — Russian parallel L1] 19:30–20:50

[On the slide — a map of Russia + ExactFarming figures.]

"The Russian parallel of the first step.

ExactFarming — twelve thousand seven hundred farms, nine and eight-tenths million hectares. A precision-farming SaaS platform. Progress Agro Group — plus five percent profitability from differentiated nitrogen application, an internal measurement. AgroSignal — fuel-and-lubricant monitoring without ML.

The main figure. The digitalization index of Russian agriculture — twenty-seven and two-tenths out of a hundred according to Yakov and Partners. The US — seventy-five and five-tenths. A structural gap.

The lesson — Climate FieldView exited Russia in two thousand twenty-two. The political risk of the first step."

[Transition to s15.]

### [Slide 15 — Section 2 divider] 20:50–21:05

"Section two of five. The robot — where specialization beats universality."

[Transition to s16.]

---

## Section 2. L2 — The robot (≈14 min)

### [Slide 16 — Carbon Robotics LaserWeeder G2] 21:05–23:30

[On the slide — a photo of the LaserWeeder in a field + three specification cards.]

"The canonical working case of the second step — the Carbon Robotics LaserWeeder G2.

A towed implement, pulled by an ordinary tractor. Two hundred forty watts of water-cooled laser. One to two joules per shot. Twenty-five thousand weeds per hour. A convolutional neural network on forty million labeled images recognizes weeds and crop plants. The laser precisely burns out the weed's root system. No chemistry.

Two hundred fifty thousand acres treated by the end of two thousand twenty-five. Fourteen countries. Price — about one million four hundred thousand dollars per machine. Payback three to four years.

[slowly]

What works. Replacing chemistry with physics — this is not optimizing an existing operation. This is a new operation, physically impossible without AI: a human cannot precisely burn every weed with a laser at a rate of twenty-five thousand per hour. A narrow niche. No autonomous-tractor claims. The tractor remains under operator control.

The pattern of the second step: narrow specialization plus replacing physics with physics plus a measurable return. Specialization wins."

[Transition to s18.]

### [Slide 18 — Narrow wins L2] 23:30–25:30

[On the slide — four photographs.]

"Four successful cases of the second step.

Solinftec Solix — a solar self-refueling platform, sprays twenty-four by seven. Growth of installations in the US — two hundred forty-three percent for two thousand twenty-five. By vendor self-report — herbicide reduction of up to ninety-eight percent.

Saga Robotics from Norway — the Thorvald platform. An important warning: Saga does ultraviolet treatment of strawberries at night against powdery mildew. Not strawberry picking. Reviews often confuse this. UV-C — this is a nighttime field patrol with an ultraviolet lamp replacing fungicides.

Tevel from Israel — flying apple pickers. Drones with grippers fly up to an apple, assess ripeness, gently pluck it. A narrow niche: fruit on a tree is easier to grip than low-growing strawberries.

AGCO PTx Outrun from Trimble — a retrofit autonomy kit for existing John Deere, Case IH, New Holland tractors. Adding autonomy on top of what the farmer already has.

All four — narrow specializations. Nobody promises 'universal AI for the whole field.' Let us remember this regularity."

[Transition to s19.]

### [Slide 19 — Monarch Tractor: timeline] 25:30–28:00

[On the slide — a photo of the MK-V + a screenshot of a TechCrunch headline.]

"And now, let us look together at the canonical failure of the second step. Monarch Tractor.

A California company from two thousand eighteen. An electric tractor with an autonomous mode for vineyards. Raised capital — more than two hundred twenty million. Contract manufacturer since two thousand twenty-two — Foxconn. A demo video of autonomous operation.

[pause]

Timeline of two thousand twenty-five. In August, Foxconn sells the Lordstown plant for three hundred seventy-five million. The first clear signal of deterioration.

In September, the Idaho dealer Burks Tractor files a lawsuit. Ten tractors of the two thousand twenty-four model year for seven hundred seventy-three thousand eighty-eight dollars — unable to operate autonomously. Machines sold as autonomous are unable to operate autonomously.

On November eighteenth — TechCrunch publishes an investigation. On November nineteenth — layoffs down to one hundred two people, thirty-eight percent of the staff.

On April fifteenth two thousand twenty-six — Caterpillar acquires Monarch. An acqui-hire post-failure. An acquisition for the team and the IP. Monarch as a brand disappears.

[slowly]

The structural lesson. Marketing sold 'autonomous,' the machines required supervision. A demonstration does not equal production deployment. When a farmer buys a machine for eighty to one hundred thousand dollars on the promise of autonomy, and it does not work — he files a lawsuit.

The alternative — supervised autonomy with an explicit disclosure of what the machine can and cannot do. The operator stays in the cab, the machine performs routine operations autonomously."

[Transition to s20.]

### [Slide 20 — FarmWise + Naïo] 28:00–29:45

[On the slide — a photo of FarmWise + a Lemken mechanical weeder.]

"Two more failures, structurally close.

FarmWise — founded in two thousand sixteen, raised more than thirty million. Wind-down in two thousand twenty-five.

Naïo from Toulouse — revenue four million euros in two thousand twenty-one, fell to two and a half million. Minus forty percent. Judicial restructuring in June two thousand twenty-five.

The cause is the same. Documented on arXiv in August two thousand twenty-five. CV models trained in greenhouse conditions break in a real field. Dust covers the cameras. Cloud shadows change contrast within minutes. Shadow bias — the model classifies shadows as vegetation. Accuracy drops from ninety percent to fifty–sixty.

[slowly]

And an important alternative. When the CV stack cannot cope — there are mechanical weeders. Lemken Steketee. Kverneland Onyx. A deterministic solution without AI. Not 'smart,' does not require firmware updates. Less efficient — but robust.

This is a category of alternative — genuine non-AI. When AI does not work for a structural reason — sometimes the right solution is no AI at all."

[Transition to s21.]

### [Slide 21 — Strawberry-picking robot] 29:45–31:00

[On the slide — a photo of a manual picker + a prototype robotic arm.]

"A drawn-out pilot phase. The strawberry-picking robot.

Dozens of startups for ten to fifteen years already. One robot — two hundred to three hundred fifty thousand dollars of capital expenditure. The addressable market of manual labor in the US — fifty billion. Robots occupy less than five percent.

[slowly]

Why it got stuck. An experienced picker distinguishes ripe from unripe berries, does not crush the fruit, avoids broken shoots. Robotics plus ML does not catch up to this baseline level over years and tens of millions of R&D.

Canonically: harvesting is the last great unsolved problem in agricultural robotics. The alternative — guest-worker programs plus ergonomic improvements."

[Transition to s17.]

### [Slide 17 — Cognitive Pilot vs ITELMA] 31:00–33:30

[On the slide — two columns: CV stack on the left, GNSS stack on the right.]

"The most methodologically important case. The place where simplistic 'AI is good or bad' thinking leads to the wrong conclusion.

Cognitive Agro Pilot — a subsidiary of Sberbank (largest Russian bank, now a tech-and-AI conglomerate). An autopilot for combines based on computer vision. A camera on the cab recognizes the edge of the uncut field. More than one thousand seven hundred installations per the vendor's self-report of May two thousand twenty-four — about one and three-tenths percent of the one hundred thirty thousand combines in Russia.

What surfaced. Four lawsuits from farmers for twelve million seven hundred thousand rubles. CV could not cope in dust, in low sun, in rain. The same CV failure as at FarmWise.

[pause]

ITELMA — part of 'Tractor Plants' (Traktornye Zavody, a Russian heavy-machinery group). At the end of two thousand twenty-five it rolled out on 'Kirovets' tractors the autopilot 'Itelma Quadro.' A different architecture. Not CV. The machine determines its position through the processing of signals from several satellite constellations — GLONASS, GPS, Galileo, BeiDou — plus RTK corrections with an accuracy of two to five centimeters. This is sensor-fusion AI.

[slowly, the central idea]

The main methodological point. These two solutions are not competitors. They cover different functions.

ITELMA — 'where am I.' Precise navigation.

Cognitive Pilot — 'what do I see.' CV recognition of the edge and of obstacles.

Different classes of task. The engineering-correct solution for a modern combine is a combination of both. GNSS navigation primary, CV secondary for nonstandard situations. Comparing 'one is better than the other' is methodologically wrong.

This is the second important anti-AI criterion. Sometimes the right choice is a different class of AI. Sometimes — no AI at all. Cognitive Pilot CV breaks in dust — ITELMA sensor-fusion is robust. This is an architectural choice within the AI domain. It differs from FarmWise, where the alternative is no AI at all."

[Transition to s22.]

---

## Section 3. L3 — The animal (≈11 min)

### [Slide 22 — Section 3 divider] 33:30–33:45

"Section three of five. The animal — computer vision in livestock farming."

[Transition to s23.]

### [Slide 23 — Allflex SenseHub] 33:45–35:45

[On the slide — a photo of a collar + a dashboard interface.]

"The third step. And note: here AI works more stably than on the first two.

For two structural reasons. The first — the economics are concentrated. One cow — three to five thousand dollars of milk a year. The loss of a cow due to undetected mastitis — a measurable loss. The second — measurements are possible at the level of the individual animal. By tag, by collar, by camera. The open-environment farm turns into an array of micro-environments: one closed loop per animal.

Allflex SenseHub from Merck Animal Health. A collar with an accelerometer and a thermometer. Battery five to seven years. Cloud analytics compares activity patterns against the herd baseline and the cow's history. Alerts: estrus, calving, lameness, mastitis, respiratory disease.

In two thousand twenty-five — two million cows under monitoring. In the world — about two hundred sixty-five million dairy cows. Two million — three quarters of a percent. Payback for farms from one hundred cows.

[slowly]

The pattern. AI as augmentation, not replacement. The collar measures, the algorithm raises an alert, the farmer or veterinarian makes the decision. AI does not prescribe an antibiotic and does not replace the veterinarian. AI performs the function of an early signal at a scale that is impossible without sensors."

[Transition to s24.]

### [Slide 24 — CattleEye + DeLaval VMS + Cargill Birdoo] 35:45–37:45

[On the slide — three cards.]

"Three more working cases of the third step.

CattleEye — acquired by GEA in two thousand twenty-four. A cheap CCTV camera films the cow as it exits the milking parlour. The model scores the lameness grade from biomechanics. Sixty farms, eleven thousand cows directly; through the GEA channel — access to farms with more than two hundred fifty thousand cows. Lameness is one of the leading causes of reduced milk yield and premature culling.

DeLaval VMS V310 — a robotic milking machine. The cow enters the station on its own. Ninety-nine and eight-tenths percent attachment rate — nine hundred ninety-eight out of a thousand attempts are successful. Growth of North American installations by fifteen percent for two thousand twenty-five.

Cargill Birdoo — computer vision for estimating broiler weight. A camera overhead, the model estimates mass from the silhouette. Claimed accuracy over ninety-five percent. Savings of ten to thirty grams of feed per broiler. Only North and South America.

[slowly]

All three — narrow tasks with a measurable return. And market consolidation. MSD acquired Antelliq for three billion eight hundred fifty million. GEA — CattleEye. Cargill — Cainthus back in two thousand eighteen. A signal of market maturity: L3 startups become divisions of large corporations."

[Transition to s25.]

### [Slide 25 — Cainthus, tie-stall, Holstein-bias] 37:45–40:15

[On the slide — three blocks.]

"Three anti-hype lessons of the third step that you and I must state explicitly.

The first. Cainthus — Dublin, acquired by Cargill in two thousand eighteen. A CV system for monitoring cow behavior on cameras. The partnership was announced in two thousand eighteen. As of two thousand twenty-six, there are no publicly published production metrics.

[pause]

The pattern: the partnership is announced, the deployment is not verified. An important warning. Cainthus and Connecterra are different companies. Cainthus — Dublin, part of Cargill. Connecterra — Amsterdam, the IDA product with a sensor collar, customers Danone, Bayer, Kersia. They are often confused.

The second. Tie-stall barns. The cow is tied to a stall and milked in place. Common in Eastern Europe, in Russia, in part of Canada. CV solutions like CattleEye do not work: weak lighting, silhouettes obscured by structures, no moment of 'the cow walking down the aisle.'

[pause]

The same CattleEye model that works on a free-stall farm in Wisconsin does not work on a tie-stall farm in the Kaluga region. This is not 'the Russian context' — this is the physical configuration of the barn.

The third. Holstein-bias. Most CV models are trained on the Holstein black-and-white breed.

[pause]

For local Russian breeds — Kholmogory, Yaroslavl, Yakutian, Bestuzhev — the calibration is weak. The solution — transfer learning with locally labeled data. Collect five to ten thousand images. Fine-tune the model. An engineering workflow, done before deployment, not after.

[slowly]

The lesson of the third step is the same as with Plantix. Ninety percent on a benchmark says nothing about performance on the edge cases of your geography, configuration, breed."

[Transition to s26.]

### [Slide 26 — Russia L3] 40:00–41:45

[On the slide — on the left, the Connectome.ai interface; on the right — sanction impact.]

"The Russian parallel of the third step.

The working case — Connectome.ai, a Skolkovo (Russian innovation hub / tech park near Moscow) resident. A CV system for monitoring calf births. A camera in the calving unit recognizes the onset of labor and sends an alert to the veterinarian. A narrow working solution — a parallel of Cargill Birdoo.

It is more complicated with imported equipment. The AI functionality of DeLaval VMS, GEA, Lely after two thousand twenty-two is in a gray status in Russia. The equipment is with the farmers. Cloud services from Europe are available unreliably.

Cases of 'the AI service was shut off on date X' with explicit attribution have not been recorded. But a vendor departure from an adjacent class has already happened — Climate FieldView exited in two thousand twenty-two, Microsoft Azure and AWS at the same time. The architectural risk is documented.

[slowly]

The lesson is universal. It applies to any farm in any peripheral country that depends on a cloud-AI vendor from another jurisdiction.

Lobnya, March two thousand twenty-six — production of dairy equipment, four billion rubles. This is hardware substitution. The AI stack requires a separate trajectory."

[Transition to s27.]

---

## Section 4. L4 — The supply chain (≈11 min)

### [Slide 27 — Section 4 divider] 41:45–42:00

"Section four of five. The supply chain — the place where agentic AI leads."

[Transition to s28.]

### [Slide 28 — Cargill CMAX] 42:00–43:30

[On the slide — a screenshot of a press release + a photo of a port terminal.]

"The fourth step. Agentic AI leads in the production deployment of two thousand twenty-six.

Cargill CMAX. A commercial intelligence platform. In April two thousand twenty-six Cargill received the BIG AI Excellence Award for CMAX — predictive port and shipping logistics for grain flows, plus CarVe — computer vision for the protein chain. Cargill operates in more than seventy countries.

[slowly]

Why exactly the supply chain. The speed of feedback. A trader gets the result of a hedge in basis points within minutes to hours. A first-step farmer — over a season. Prices on the CBOT change daily. But the nature of the task — hedge, procurement, logistics — has been stable for decades. This is the ideal combination: fast feedback plus a stable structure.

McKinsey puts it this way: leading players are redesigning their hedging and logistics processes for agentic AI. Early adopters see a reduction in hedge divergence of twenty-five to thirty-five percent."

[Transition to s29.]

### [Slide 29 — Pseudo-flow 'how the agent makes a hedge'] 43:30–46:00

[On the slide — four steps horizontally.]

"So that the abstraction 'agentic AI for hedging' does not remain marketing — let us take apart together a concrete flow in four steps.

Step one — sensor. The agent reads streams. Futures prices on the CBOT. Weather in the Midwest, Brazil, the Krasnodar region. Currency rates. Everything is aggregated into a single state vector.

Step two — inference. The model estimates the direction of the price over five, thirty, ninety days plus uncertainty ranges. A distribution of probable prices.

Step three — decision. The agent initiates one of four actions: open a position, close it, rebalance, do nothing. A critical engineering detail. For trades over ten million dollars notional — mandatory human-in-the-loop approval. For small ones — autonomously. The boundary — an engineering choice.

Step four — feedback. Within minutes to hours the agent receives the result of the trade in basis points. The model updates in the stream — online learning.

[pause, example]

An example. August two thousand twenty-five. Corn prices on the CBOT fell by two percent. The model forecast rising volatility. The agent formed a long position of eight million dollars notional. Eight is less than ten — it executed autonomously. Three days later the price rose by one and eight-tenths percent. Hedge divergence — eight basis points versus forty-five in a typical manual one. A differential of thirty-seven basis points times eight million — about thirty-two thousand dollars of savings on a single trade. At Cargill's volumes — millions a year.

[slowly]

Important. This is a narrow agent. One action — hedge. This narrowness is the reason for success. Extending it to 'manage the entire chain from field to shelf' — does not work yet. That is an ambition of two thousand thirty, not the industry of two thousand twenty-six."

[Transition to s30.]

### [Slide 30 — Tract, Olam, Walmart×Cropin, Tesco] 46:00–47:30

[On the slide — four logos.]

"Besides Cargill — several key platforms.

Tract — founded in two thousand twenty-three by four anchor customers: ADM, Cargill, LDC, ofi. Eighteen and six-tenths million euros in Series A led by Icos Capital. Direct competitors jointly invest in shared compliance infrastructure.

A clarification. Tract is not agentic AI. This is a data backbone, a data infrastructure over which agents work at the customers'. A frequent error is to call Tract an 'agentic platform.'

Olam Mindsprint — spun off in two thousand twenty-four. Procuresprint — an example of agentic procurement: the agent compares suppliers automatically, escalating to a human only the nonstandard cases.

Walmart with Cropin — an Indian company. Satellite analytics over supplier farms in the US and South America. Not in India — a frequent error of reviews.

Tesco — a British retailer. AI for demand forecasting since two thousand seventeen. Minus thirty percent food waste."

[Transition to s31.]

### [Slide 31 — USDA Climate-Smart + Verra phantom] 47:30–50:00

[On the slide — two columns: USDA press release on the left, The Guardian on Verra on the right.]

"Two failures of the fourth step.

The first. USDA Climate-Smart Commodities. A program of the US Department of Agriculture. Budget three billion one hundred million. One hundred thirty-five projects, fourteen thousand farms, three and two-tenths million acres — about zero point thirty-six percent of US cropland. The program supported climate-smart practices with AI-MRV.

On April fourteenth two thousand twenty-five the Trump administration canceled the program. The replacement — AMP, Advancing Markets for Producers — without climate-outcome requirements.

Dozens of startups in AI-MRV built a business model on this flow. In a day — uncertainty.

The lesson: federal policy is a tail risk. The alternative — the structural economics of the project, not the tailwind of state policy.

[pause]

The second failure — Verra phantom credits. Verra is the largest verifier of voluntary carbon credits. In January two thousand twenty-three, The Guardian, Die Zeit, and SourceMaterial published a nine-month investigation. More than ninety-four percent of Verra's rainforest offset credits are phantom. Pachama — an overestimation by a factor of eight.

Carbon projects rely on AI systems for estimating carbon stock. Inference with large uncertainty is marketed as 'precise measurement.' Large-scale greenwashing.

[slowly]

An important caveat. Verra phantom credits pertain to rainforest offset projects. This does not mean that all AI-MRV is phantom. Agricultural soil-carbon is a different methodology. Indigo Ag uses not Verra but the Climate Action Reserve. Indigo has a twelve-year agreement with Microsoft for two million eight hundred fifty thousand tons. Indigo Ag is not in the Verra scandal. Do not do cascade misattribution.

The criterion. AI-MRV without direct measurement is large-scale greenwashing. The alternative — direct soil sampling plus transparent uncertainty bands. AI as a hypothesis, not as a fact."

[Transition to s32.]

### [Slide 32 — Russia L4] 50:00–52:00

[On the slide — four status cards.]

"The Russian parallel of the fourth step. One of the most mature segments of Russian agricultural AI.

X5 'Perekrestok' — an ML demand-forecasting system since two thousand twenty. More than two hundred factors. According to X5 Tech — world-class accuracy, an in-house ML team. Parity with Tesco and Walmart.

Magnit (large Russian grocery-retail chain) F&R. The stack is split into two modules. Forecasting — in production deployment on forty-six distribution centers in January two thousand twenty-six. The network level. Replenishment — a pilot on three centers, a plan up to ten to twenty by the start of twenty-seven.

[slowly]

It is important to distinguish. 'Forty-six distribution centers' is an over-claim for the whole F&R. 'Three pilot distribution centers' is an under-statement for Forecasting. Correctly — a modular separation.

RSHB — Rosselkhozbank. The 'Svoyo Fermerstvo' platform announces AI services. A caveat: these services are announced, but independent verification of the metrics is absent. Format: RSHB AI — announced, no metrics.

Sber GigaChat in one episode was presented as having 'passed an exam in agronomy.' A demo, not a production deployment.

The main Russian lesson. Parity with the world in L4–L5 at X5 and partly at Magnit. With a significant lag on L1–L2."

[Transition to s33.]

---

## Section 4-bis. The environment (≈8 min)

### [Slide 33 — Section 4-bis divider] 52:00–52:15

"Section four-bis of five. The environment — connectivity, vendor lock-in, regulation. Without it, no step works."

[Transition to s34.]

### [Slide 34 — Connectivity] 52:15–54:45

[On the slide — three numbers in large type + a map of GNSS jamming in Finland.]

"The first condition of the environment — connectivity. Most AgTech marketing relied on the scenario 'cloud AI optimizes your tractor in real time.' Note: this is a fantasy for most farms.

Three figures.

The first. Eighteen percent of American farms without internet access at all. About three hundred sixty thousand out of two million. According to BroadbandNow.

The second. One hundred twenty-three thousand air flights with GNSS interference in just the first four months of two thousand twenty-five. According to ICAO. The ICAO Assembly in October formally condemned Russia for disrupting the GNSS of civil aviation. Finnish farmers report: areas of farms are reportedly unfarmable using GNSS-based tractors. Precision farming — a civilian casualty of military electronic warfare.

The third. On April thirtieth two thousand twenty-six, Starlink was banned in Russia for six months. Single-vendor connectivity = single point of failure. Elon Musk unilaterally cut off Starlink for Ukraine in two thousand twenty-two. The same logic applies to any jurisdiction.

[slowly]

What this means. Edge ML and TinyML — the only realistic architecture for most farms. Machine learning on the device — without a cloud uplink. Models of megabytes, not gigabytes. Computation on a microcontroller or an edge-GPU. A hybrid architecture with redundancy for critical operations.

The criterion: cloud-first for an off-grid farm is an architectural error. The alternative — edge-AI and offline-first."

[Transition to s30b.]

### [Slide 30b — Vendor lock-in: the dual optics of John Deere] 54:45–57:00

[On the slide — a map Melitopol→Chechnya + a photo of an FTC press conference.]

"The most methodologically important ethical idea of the lecture — you and I must state it. The dual optics.

Two events.

May two thousand twenty-two. The Russian military seized twenty-seven units of John Deere from Melitopol to Chechnya. On site the machinery would not start. Deere remotely 'bricked' all twenty-seven via GPS and VIN-locking. For those who stole — five million in lost machinery.

January two thousand twenty-five. The US FTC files a suit against Deere over a decade of repair restrictions.

December two thousand twenty-five — the FCC banned foreign-made drones. DJI holds eighty percent of ag-spray drone flights in the US.

[pause, the central idea]

The dual optics. One mechanism — two opposite interpretations.

Side A. Anti-theft success. From the Ukrainian side — a victory of technology. Stolen machinery stopped. The AI function worked as designed.

Side B. Vendor control surface. The same mechanism: Deere can shut off any farmer's equipment. One who has not paid the subscription. One under sanctions. Russian farmers after twenty-two got this scenario. Climate FieldView exited with Bayer.

[slowly]

The engineering lesson. An AI security feature today — an AI control surface tomorrow. The same mechanism thanks to which a stolen combine does not work in Chechnya is a ground for alarm for every farmer in any jurisdiction that falls into a political rift.

One more anti-AI criterion — AI-driven equipment as a vendor lock-in trap. The alternative — open-source hardware, the right to repair, a multi-vendor strategy, a mechanical fallback."

[Transition to s35.]

### [Slide 35 — Regulation] 57:00–59:00

[On the slide — three columns: EU, US, Russia.]

"The third condition of the environment that you and I will discuss — regulation.

The EU AI Act — Regulation two thousand twenty-four slash one thousand six hundred eighty-nine. Agricultural machinery with AI-safety components is a high-risk category. Manufacturers need compliance teams. A mandatory technical file. A cascade of liability. Since February two thousand twenty-five — an AI-literacy requirement for operators.

The USDA AI Strategy has been formally published, largely declarative. In the US, AgTech regulation goes through the FCC for drones, the FTC for vendor lock-in, the USDA for programs — not through a single AI regulator.

Russia — the 'Agriculture of the Future' program, two thousand twenty-six to two thousand thirty. A Government Decree of December thirty-first, twenty-five. A declarative program. The previous 'Digital Agriculture' did not achieve its goals of doubling productivity. Agriculture in twenty-four — minus three and two-tenths percent.

[slowly]

The methodological lesson. A declarative document does not equal a real result. An engineer who assesses Russian agricultural AI by ministerial press releases systematically overestimates the maturity of the industry. The real metrics — a digitalization index of twenty-seven point two — a structural gap."

[Transition to s36.]

---

## Section 5. L5 — The consumer + payoff (≈6 min)

### [Slide 36 — Section 5 divider] 59:00–59:15

"Section five of five. The consumer — the most mature step plus five criteria plus the final callback."

[Transition to s37s.]

### [Slide 37s — L5: Walmart, Tesco, X5] 59:15–60:30

[On the slide — three logos + a photo of a sales floor.]

"The fifth step. A fully digitized environment. Every SKU has a digital trace.

Walmart Eden ML — assessment of fresh-produce quality and prediction of shelf life. Since two thousand seventeen. Minus twenty percent food waste.

Tesco AI demand forecast — since two thousand seventeen. Minus thirty percent waste.

X5 — world class since twenty, as we said in the fourth section.

And Magnit F&R — a hybrid status that we discussed in Section 4. The Forecasting module in production deployment on forty-six distribution centers since January twenty-six — the network level, parity with world leaders in this narrow task. The Replenishment module — a pilot on three distribution centers with a plan to scale to ten to twenty by the start of twenty-seven. Half of the F&R stack at world class, the other half — the pilot phase. The correct formulation — a modular separation.

[slowly]

An anti-hype caveat. The level works reliably. But most of the fifth step is not specific to agriculture. Demand forecasting by machine-learning methods in grocery retail is the same task as in clothing retail. The successes of the fifth step do not prove 'AI readiness of the entire agricultural chain.'"

[Transition to s38s.]

### [Slide 38s — Five criteria 'when not AI'] 60:30–63:00

[On the slide — a matrix of five rows × three columns.]

"Let us gather it into one matrix. Five criteria of 'when not AI.' The main takeaway.

Criterion one. The law of thermodynamics matters more than ML. When the economics are an order of magnitude above the market price — ML does not close the gap. Example — vertical farming. Alternative — open ground.

Criterion two. Threshold accuracy does not equal readiness for rollout. Ninety percent on a benchmark at scale — hundreds of thousands of erroneous decisions. Example — Plantix. Alternative — a model with an explicit measure of uncertainty and abstention.

Criterion three. A generic LLM as an advisor is a categorical anti-pattern. Example — Nature Food, Tzachor, ChatGPT on pesticides. Alternative — RAG grounded to a local regulator, plus abstention at low confidence, plus a human in the loop.

Criterion four. AI-driven equipment is a vendor lock-in trap. Example — FTC v. Deere, Melitopol, the exit of Climate FieldView. Alternative — open-source hardware, the right to repair, a mechanical fallback.

Criterion five. AI-MRV for carbon claims without direct measurement is large-scale greenwashing. Example — Verra, ninety-four percent phantom credits. Alternative — direct soil sampling plus transparent uncertainty bands.

[slowly]

And three criteria inline. An architectural choice within the AI domain — Cognitive Pilot and ITELMA. A genuine non-AI alternative — FarmWise and Lemken Steketee. Cloud-first for off-grid — edge-AI and TinyML.

This is a working tool. When you are offered an AI solution — we run it through the criteria. If at least one fires — a reconsideration is needed."

[Transition to s35c.]

### [Slide 35c — Pre-purchase verification checklist] 63:00–64:30

[On the slide — five blocks of two items each.]

"A concrete operational artifact that you and I take away from the lecture. A pre-purchase verification checklist. Ten questions in five blocks.

Block one — Classification. Which step? Which mode of AI operation?

Block two — Production status. How many production deployments, not 'sold,' not 'pilot'? What accuracy on edge cases?

Block three — Liability. If 'autonomous' — who is responsible for a collision? The regulatory status?

Block four — Vendor lock-in. Is there an exit path? Compatibility with a multi-vendor architecture?

Block five — Connectivity. The minimum required connectivity? A mechanical fallback when AI is off?

[slowly]

Eight to ten green answers — buy. Five to seven — a conditional pilot. Four or fewer — decline. Each answer is verified not by the vendor's words but by external sources: independent reports, customer reviews, filings with regulators. This is exactly the concrete skill you take away from the lecture."

[Transition to s36c.]

### [Slide 36c — Career landscape] 64:30–65:30

[On the slide — five segments.]

"The career landscape. Not a prescription — a segmentation.

L1–L2 internationally — John Deere, Bayer Digital, BASF, Carbon Robotics, Saga. Skills — computer vision, edge ML, sensor fusion.

L3 — DeLaval, GEA, Lely, Cargill Birdoo.

L4–L5 — Cargill, ADM, Tract, Walmart, Cropin. Skills — LLMs and agentic systems, RAG, supply chain.

Russia — Cognitive Pilot, ITELMA, Geoscan, EFKO Hi! (a FoodTech direction, plant-based meat using AI in R&D), Rusagro Tech (digital agronomy and digital initiatives), X5 Tech, Magnit digital, RSHB.tsifra, ExactFarming, Connectome.ai.

Educational tracks — specialized technical and agrarian universities with master's programs in agro-IT and digital farming. Career decisions are individual."

[Transition to s37.]

### [Slide 37 — Closing payback to Plenty Compton] 65:30–68:00

[On the slide — a photo of the LaserWeeder G2 + a gold callout on thermodynamics.]

"And you and I return to the beginning.

Plenty Unlimited in Compton. The opening in May twenty-three. The closing in December twenty-four. About nine hundred forty million in raised capital. Minus ninety-nine percent of valuation.

We asked: what did AI do in this failure — and in what sense could it not?

[slowly, the finale]

The answer.

Plenty did not close because of bad AI. It closed because of LED thermodynamics. The microclimate controller worked. CV recognized growth stages. Yield models were trained. What did not work was the arithmetic of energy. LEDs in California consume a hundred times more energy than a plant receives from free sun. AI optimizes the denominator — five to fifteen percent. The gap in the numerator — two orders of magnitude. The law of thermodynamics matters more than ML.

This works not only for Plenty. At every level — the same logic.

Where AI works — See & Spray, LaserWeeder, SenseHub, Cargill CMAX, Walmart Eden.

Where AI breaks — Plenty, Monarch, Cainthus tie-stall, USDA Climate-Smart, GNSS jamming and Melitopol.

The ladder — a map of engineering decisions.

[pause]

And one more criterion that we keep at the finale as an open question. The sustainability paradox. The AI systems we build to measure the carbon footprint in agriculture themselves have a significant ecological footprint. Training GPT-3 consumed about seven hundred thousand liters of water for cooling. Data centers in Iowa consume billions of gallons of water a year — in parallel with the fact that neighboring farms save water through predictive irrigation systems. AI-MRV without direct measurement is a scalable greenwashing, as we saw with Verra. Net-positive is not an automatic property of sustainable AI. It is a property that must be specifically calculated and proven in each concrete case.

[pause]

This is neither optimism nor skepticism. This is an apparatus for decision-making. Name the level. Assess the environment. Apply the criterion. Name the alternative.

The engineer holds this whole ladder in their head and knows where AI does not work.

[slowly]

In the next lecture — cyber-physical manufacturing. The production line is closer to L4–L5 in control, but with physical contact of AI with the product as in L2. A different class of AI applications: predictive maintenance, robotic assembly, quality control. The same methodological frame.

Thank you."

[Transition to s38.]

### [Slide 38 — Q&A] 68:00–75:00+

[On the slide — large 'Q&A' + contacts + a compact reading list.]

"Next — your questions. I have ready answers to the typical ones. If you want to argue against — those are the most valuable questions."

[Open Q&A. Below — talking points for the lecturer on typical questions.]

---

## Q&A — backup talking points for the lecturer

### Q1. Vertical farming — is it an AI fault or unit economics?

More likely unit economics. The AI systems inside Plenty, AppHarvest, Bowery worked — controlled-environment management, CV classification, predictive yield models. What did not work was the structural economics of LEDs versus the sun, a difference of about a hundred times in the cost of energy. This is a closed-loop architecture beyond where AI can close the gap. The exception — Oishii, premium strawberries at ten dollars a pack, where the premium covers the energy.

### Q2. Can an LLM advisor really replace an agronomist?

In 'full replacement' mode — no. See F2, Nature Food of two thousand twenty-four. In augmentation mode with RAG grounding to a local regulator plus abstention at low confidence plus a human in the loop — yes, for a certain class of tasks: retrieval of regulations, translation between languages, explanation of technical terms. The architectural choice is critical.

### Q3. ITELMA versus Cognitive Pilot — which is better?

This is a methodologically wrong question. They solve different tasks. ITELMA — 'where am I.' Precise navigation on multi-GNSS and RTK. Cognitive Pilot — 'what do I see.' CV recognition of the edge, of obstacles. The right solution — a combination: GNSS navigation primary, CV secondary for nonstandard situations. Comparing 'one is better than the other' is methodologically wrong.

### Q4. Will the autonomous tractor be mass-deployed by two thousand thirty?

Full autonomy — extremely unlikely. Supervised autonomy — the operator in the cab, AI performs routine operations — yes, most likely. Retrofit autonomy for a mixed fleet — probably, by two thousand thirty this will be a commercially significant segment. The Monarch and FarmWise bankruptcies are the failure of the point-model 'full autonomy,' not of the whole category.

### Q5. What will happen to Russian agriculture in five years if sanctions are lifted?

A speculative question. Structurally: the hardware layer — tractors, milking equipment — will recover faster than the AI stack — models, data, infrastructure. Models trained on local data cannot be 'bought and installed' from the US or Europe. A reassembly of the pipeline with the participation of Russian teams is needed. The same argument holds for any country.

### Q6. Cargill CMAX — does it open positions on the exchange itself?

Not fully. For large trades over ten million dollars notional — mandatory human-in-the-loop approval. For small ones — autonomously. This is an engineering choice. The notional boundary is governed by the regulator and by risk management. 'Agentic AI' does not mean 'full autonomy.' It means 'AI with an inference loop and tool-use, performing multi-step tasks with an explicit boundary of human approval.'

### Q7. Where is the ethical boundary of AI in agriculture given that eighty percent of farms globally are smallholders?

An open question. The digital divide is widening — large farms adopt faster, small ones lag. The Gates Foundation allocated one billion four hundred million for adaptation to climate change. AIM for Scale works with forty million Indian farmers via SMS. But the gap remains. The applicable criterion — threshold accuracy does not equal readiness for rollout in an environment with a different average profitability. Cloud-first for off-grid is an architectural error. The alternative — SMS advisories plus community animal-health workers."
