---
lecture: 13
title: "AI in Logistics and Transportation"
module: 3
duration_min: 75
audience: "3rd-year engineering students (general, not domain specialists)"
status: draft
version: 1
created: 2026-05-22
issue: 135
branch: issue-135-lec-13-logistics
type: speech
length_words_target: ~5k
derived_from: [chapter.md, chapter-part2.md, chapter-part3.md, deck.yaml, slides/*]
keystone_axis: "Environment-structure ladder — 5 levels from controlled warehouse to exception black-swan"
pacing_target: "~73 minutes of active speech + 2 minutes buffer; conversational, ~70 words/minute in Russian"
strict_in_share: ">50% (failure-cases + criteria + alternatives distributed across §1–§4)"
bridge_phrases: "4 dividers — each 'Section N of five'; soft-bridge to Lecture 14"
---

# Lecture 13. AI in Logistics and Transportation — Lecturer's Speech

**Duration:** 75 minutes (~73 minutes of speech + 2 minutes buffer).
**Slides:** 41 (33 content + 4 dividers + cover + Q&A + closing hero).
**Source of truth:** chapter v2 (3 parts) + slides v1 (41 rendered).

---

## Lecturer's Preparation (before the lecture)

### What to keep in mind

The main idea is the **environment-structure ladder**, five levels from the warehouse to the black swan. If, by the end, the students are left with the ladder and the seven decision criteria — the lecture succeeded.

The tone is "trust but verify." More than half of the content is about failures. AVs are one of the most expensive stories of burning through venture capital. Cruise (s29) is the most emotional. Uber Tempe (s30) is the heaviest — deliver it quietly. UPS ORION (s16) and the decision framework (s38) are the main anti-hype moments.

### What to verify the day of

- Waymo press: `https://waymo.com/press/` — number of rides per week.
- NHTSA SGO: `https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting` — confirmed Tesla fatalities.
- Pony.ai 6-K: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=PONY` — Guangzhou first, Shenzhen second.
- Aurora press: `https://aurora.tech/news/` — route status.
- KamAZ press: `https://kamaz.ru/press/` — expansion onto the M-12.
- Tesla Robotaxi tracker: `https://nationaltoday.com/us/tx/austin/news/` — number of crashes.
- Read slides 1, 5, 16, 17, 29, 34, 38 aloud with a stopwatch.

### 30 minutes before

Projector. Presentation in presenter mode. Bottle of water. Phone on silent.

### If something goes wrong

- Data has been updated — say so verbally.
- Projector fails — printed key slides (1, 5, 16, 29, 34, 38).
- Q&A drifts into marketing — gently steer back: "let's look at this from the engineering side."

---

## s01 — Hook · Three pictures side by side · 3 minutes

Hello. Before we say the first word about AI in logistics — look here.

[pause 3 seconds]

Three business-press headlines over eighteen months. Three pictures that changed our understanding of where autonomous transportation systems work and where they don't.

[pointing at the left panel]

**December 2024.** General Motors shuts down Cruise after eight years of investment. Ten billion dollars in operating losses. Less than five hundred million in revenue over its entire history. For every dollar of revenue — twenty dollars of burned capital. The cause — a single incident on October 2, 2023, in San Francisco.

[center panel]

**March 2026.** Waymo. Five hundred thousand paid rides per week. Three thousand sixty-seven vehicles. More than ten US cities. Over nineteen months — a tenfold growth. And at the same time — the company does not publicly report profitability per ride.

[right panel]

**February 2026.** Tesla Robotaxi in Austin. Launched June 22, 2025. Fourteen crashes over eight months. About eight hundred thousand paid miles. The first public statistics for a vision-only stack, without lidar and without an HD map.

[pause, lower your voice]

Three pictures pose one question.

**Why did Waymo survive, Cruise go bankrupt, and Tesla is only just beginning?**

[pause 2 seconds]

If it were only about technology — all three use similar sensor stacks. If it were only about capital — Cruise had GM's ten billion, Waymo had Alphabet's practically infinite capital. If it were only about regulation — both operated in the same cities under the same DMV.

It's about **the environment** and about the discipline of what we will today call the operational design domain — **ODD**. This is the main idea of the lecture, one I will return to for the next hour and a quarter.

[Transition to s02]

---

## s02 — Cover · 1 minute

Lecture thirteen. AI in logistics and transportation. Part of the course's third module.

Today — where AI works in this industry, where it doesn't, and how an engineer should decide. Three goals: name the five levels of the environment ladder; critically assess the vendor's "our autonomous transport will replace X percent of drivers"; describe the regulatory landscape and formulate the criteria for "AI isn't needed or doesn't work."

[Transition to s03]

---

## s03 — Lecture route · 1 minute

The route — five sections.

First — the **controlled environment**: warehouse, port, rails. Where AI works maturely.

Second — the **semi-structured highway**. Aurora the first commercial one, KamAZ on the M-11, a series of twenty-billion-dollar bankruptcies.

Third — the **urban street of robotaxis** and the last mile. Waymo survived, Cruise went bankrupt, Tesla is only just beginning.

Fourth — the **black swan and the decision framework**. Where AI is blind by definition.

Fifth — the **closing** and the bridge to Lecture fourteen.

This is a heavy lecture. More than half of it is about failures. That is intentional.

[Transition to s04]

---

## s04 — Ten acronyms · 2 minutes

Ten acronyms without which we can't go further. They'll recur for the whole hour.

**SAE J3016** — the standard, six levels of automotive autonomy from zero to five. The key ones for us are L3 "you can take your eyes off the road" and L4 "driverless within a defined domain."

**ODD** — Operational Design Domain. A formal description of the conditions under which the system was designed to operate. The most important engineering concept of the lecture.

**AV** — Autonomous Vehicle. **AMR** — Autonomous Mobile Robot, warehouse-type.

**OR** — Operations Research. Mathematical optimization: linear programming, the traveling salesman problem, the vehicle routing problem. **This is not AI in the modern sense**, and for cleanly defined tasks it is often better.

**HD map** — a detailed map of the road, accuracy about ten centimeters. Tesla rejected it; the others use it.

**EOQ** — Economic Order Quantity. The optimal order size, a 1913 formula, three parameters, it works.

**TSP** and **VRP** — the traveling salesman problem and the vehicle routing problem.

**HITL, HOOL, HOTL** — human-in-the-loop, human-on-the-loop, human-out-of-the-loop. Three levels of human participation.

Remember **ODD** and **OR** — the two key words of the lecture.

[Transition to s05]

---

## s05 — Keystone: the environment ladder · 2 minutes

**The key slide of the lecture.** I will return to this ladder for the whole next hour.

[pointing at the ladder]

**Level one — the controlled environment.** Warehouse, port, depot. Lighting is known, geometry is fixed. AI works maturely here. Symbotic, Amazon, KONUX.

**Level two — the highway.** A known direction, an HD map is possible. Aurora Dallas–Houston, May 2025. KamAZ-54901 on the M-11. **Twenty billion burned on the ones that didn't survive.**

**Level three — the urban street of robotaxis.** Pedestrians, cyclists, emergence. Waymo survived, Cruise went bankrupt, Tesla is only just beginning. The difference is not algorithmic — it is **ODD discipline**.

**Level four — the last mile.** Sidewalk, campuses, drone. Starship on campuses. Zipline a hundred million miles in Africa. Narrow niches.

[pause, slower]

**Level five — the emergency.** The black swan. The Houthis 2024. Ever Given 2021. COVID 2020. **At this level ML is blind by definition.** The tools are **not AI**. Human dispatchers. Scenario planning. Operations research. Classical formulas.

This ladder is the main predictor of AI's success. Every section today is a motivated descent along this axis.

[Transition to s06]

---

## s06 — Section 1 divider · 30 seconds

**Section one of five.** The controlled environment: warehouse, port, rails.

The level where AI works maturely. Let's examine where the boundaries of this "maturely" are.

[Transition to s07]

---

## s07 — Symbotic + Walmart · 2 minutes

The canonical example of warehouse integration in 2024–2025 is Symbotic with Walmart. In January 2025 Walmart committed to deploying Symbotic across four hundred accelerated-fulfillment centers. **A backlog of more than five billion dollars.** That is four years of Symbotic's annual revenue in advance — an extraordinary signal.

What Symbotic does technically. Full warehouse automation — palletizing, depalletizing, picking, sorting. Under the hood — classical industrial robots plus mobile platforms plus computer vision for recognizing SKUs. **This is not one machine-learning model**, but an integrated system in which ML handles recognition while the core control logic is deterministic.

The main risk is **capital intensity**. One Symbotic center costs tens of millions to install. Small retailers can't afford it. The alternative for a small company is traditional manual picking with minimal automation.

The second risk is **single-vendor lock-in**. Walmart, by investing billions in Symbotic, gets a long-term dependency. Classic OEM lock-in. **The lesson for the engineer** is to ask about the exit strategy in a long-term contract.

[Transition to s08]

---

## s08 — Amazon Robotics · 2 minutes

Amazon chose a different strategy — not to buy from a vendor, but to build in-house. In June 2025 Amazon announced it had surpassed **one million robots** in its own network.

Four main models. **Sparrow** — a picker with a vacuum grip and vision. **Sequoia** — mobile storage, the container comes to the workstation. **Proteus** — a fully autonomous mobile robot, working in the same space as people. **Vulcan** — the most interesting: a **tactile sensor** added on top of vision.

The lesson of the multimodal stack. Vision-only works for typical objects. For **soft packaging, transparent bottles** — tactile information is needed. The industry is moving from vision-only to **the fusion of several sensors**.

The comparison — **a thousand to one**. For every Waymo autonomous vehicle there are roughly a thousand warehouse robots in the world. AI in logistics in 2026 is deployed en masse in the warehouse, not on the road.

[Transition to s09]

---

## s09 — AMR Locus + GreyOrange · 2 minutes

AMR is a category of warehouse robotization where the robot moves along the floor in cooperation with a human picker.

**Locus Robotics** — more than five billion picking operations. The robot follows the picker, who puts the item in a basket, and the robot carries it to packing. **GreyOrange Butler** works differently: the shelf itself moves to the workstation. **Geek+** — the Chinese analog.

Important — **AMR is not plug-and-play**. It requires integration with the warehouse management system and staff training.

And here is the **first failure-bucket of level one** — pressure on the worker. Unions in the UK and the US in 2023–2024 raised the alarm: after AMR deployment, the human picker's pace is **imposed by the robot**. The robot waits at the shelf — the picker can't linger. This is analogous to the pushback we discussed in Lecture eleven — **Toyota Jidoka**, AI augments the worker, does not replace. If the robot is giving the orders — that is no longer augmentation. The unions register this boundary, and the engineer must understand it in advance.

[Transition to s10]

---

## s10 — Port automation · 2 minutes

Port automation is the next category. Fully automated terminals exist. Maasvlakte II in Rotterdam. Long Beach LBCT. Yangshan in Shanghai. The vendors are **ABB Marine**, **Konecranes**, **ZPMC**.

The technology works. The container is automatically unloaded, rides on a cart, and is stacked automatically.

But in October 2024 there was an **ILA strike** — International Longshoremen's Association. The main demand — to **stop further automation of East Coast ports**. A compromise was reached, but new automated terminals are frozen.

**The technology is ready. It is economically advantageous. But labor politics is blocking it.**

This is an important lesson: technological readiness does not equal adoption. Maasvlakte II has operated since 2015, Yangshan since 2017. **The same technology, different outcomes across continents.** Adoption depends on the environment in the broad sense — not only the physical, but also the social.

[Transition to s11]

---

## s11 — KONUX rail + boundaries of level 1 · 2 minutes

Let's close level one. **KONUX** — predictive maintenance of railway switches on Deutsche Bahn. Vibration and temperature sensors, ML predicts when a switch will need maintenance. **A mature use case**, saving millions of euros a year.

Now the boundaries of level one. Three key ones.

**First. Humanoid hype.** Tesla Optimus, Figure 02, UBTech Walker S1. By 2026 — all at the stage of **pilots on tens of units**, not production operation. When a vendor shows a slick video — ask: how many units, under what conditions, what failure statistics.

**Second. Capital intensity.** Tens of millions per installation.

**Third. The "lights-out warehouse" myth.** A fully unstaffed warehouse for a broad assortment is a myth. Existing technology works for narrow categories. A real broad-SKU warehouse **requires a human** for edge cases.

[Transition to s12]

---

## s12 — Failure matrix, Section 1 · 1.5 minutes

Let's close section one with four boundaries.

First — capital intensity, tens of millions per installation. Small players drop out.

Second — OEM lock-in, a long-term dependency on a single vendor.

Third — the myth of the fully unstaffed warehouse, not feasible for a broad assortment.

Fourth — seasonal distribution shift. Black Friday, Christmas. The catalog fills with new categories. The vision classifier errs more often. The model is trained on the typical distribution; the peak is beyond its bounds.

These are the boundaries of level one. AI works maturely — but the boundaries are real.

[Transition to s13]

---

## s13 — Section 2 divider · 30 seconds

**Section two of five.** The semi-structured highway.

A step up the ladder. Weather, speed, emergent situations. Here the startup story is brutal.

[Transition to s14]

---

## s14 — Aurora Dallas-Houston · 2.5 minutes

Aurora Innovation — **the first company in the US** to launch a fully driverless commercial freight run on the highway. **May 1, 2025.** The Dallas–Houston route, about two hundred forty miles of the I-45.

The fleet by the end of 2025 — **about ten vehicles**. The PACCAR Peterbilt platform plus the Aurora Driver software stack. Expansion in 2026 — Fort Worth–El Paso, Phoenix.

The main thing that sets Aurora apart from the ones that didn't survive is **crawl-walk-run**. First you crawl, then you walk, then you run.

**Crawl** — years of tests with a safety operator, 2018–2024. Billions of kilometers of simulation, tens of millions on the roads.

**Walk** — Dallas–Houston with a safety operator, 2023–2024.

**Run** — the driverless commercial launch of May 2025 on a **single route**, worked out over years. Not "driverless across the whole network" — one route.

This is engineering discipline. Aurora **does not promise** "we'll replace X percent of drivers." It does not expand the ODD aggressively. Every new route requires extensive validation.

[pause]

Remember: **ten vehicles**. Not a million, not a hundred thousand — ten. That is the survivor pattern at level two. Everyone else promised thousands and didn't make it. Aurora promised ten and got there.

[Transition to s15]

---

## s15 — Mobileye + KamAZ · 2 minutes

Alongside Aurora — two other highway programs.

**Mobileye** — spun off from Intel in 2022, public on NASDAQ. **SuperVision** — a camera-only stack, without lidar. About three hundred thousand consumer vehicles by 2025. **Chauffeur** — the next level, L3 eyes-off. Launch on premium European models: Polestar 4, Audi Q6 e-tron, Volkswagen Touareg.

A different business model than Aurora's. Aurora — ten L4 trucks on one route. Mobileye — a million L3 passenger cars. Different bets, different customers, one shared environment — the highway.

**The Russian context.** KamAZ-54901 with the Cognitive Pilot stack has operated on the M-11 "Neva" since June 2023. By the end of 2024 — sixty-seven units, of which about ten in commercial operation. The 2025 plan — a hundred units, expansion onto the M-12 and the TsKAD.

The Russian model is a state pilot within an experimental legal regime, the EPR. A special legal framework. The M-11 is a specially designated highway. **The Russian survivor pattern**: not the most technically advanced, but crawl-walk-run, state support, no overpromise.

Cognitive Pilot also makes autonomous combines — five hundred ninety thousand tons of grain over a hundred thirty thousand hectares. **A different environment — the field — but the same logic of a controlled environment plus crawl-walk-run.**

[Transition to s16]

---

## s16 — UPS ORION fundamental · 3 minutes

One of the most important slides of the lecture. Remember the numbers.

**UPS ORION.** A hundred million miles saved per year for the whole fleet. Ten million gallons of fuel. **Three to four hundred million dollars saved per year.** The UPS fleet — about a hundred twenty-five thousand vehicles.

[pause]

And now — **what's under the hood**.

ORION is **operations research**. Integer programming plus heuristics plus VRP. **Not deep learning. Not reinforcement learning. Not generative AI.** The tools are Gurobi, CPLEX, Google OR-Tools. The algorithms date to the 1950s–60s.

[slowly, emphasize]

Let me repeat. **A hundred million miles saved per year. Three to four hundred million dollars. Without machine learning. Classical 1950s math.**

This is the **canonical anti-hype example**. A cleanly stated optimization problem is solved through classical mathematics **better** than through ML. Cheaper, more explainable, more reliable.

Three questions for an ML routing vendor.

**First.** What is the comparison against the OR baseline? If they don't show a Gurobi or OR-Tools baseline — a red flag.

**Second.** What is your VRP solver? If it's "end-to-end deep learning" — ask about explainability and edge cases. End-to-end RL for VRP is an active research area, **not production as of 2026**.

**Third.** Is demand stationary or not? For stationary demand — EOQ plus safety stock plus ABC analysis work no worse than ML. Formulas from 1913.

[pause]

Take this with you. UPS saves three hundred million a year **without machine learning**. When a vendor says "our AI optimizes by twenty-five percent" — ask about the comparison to an OR baseline.

[Transition to s17]

---

## s17 — AV-bankruptcy timeline · 3 minutes

Now the heaviest part. Five points on one timeline.

**March 2020 — Starsky Robotics.** The first wave of casualties. Stefan Seltz-Axmacher writes the essay "The End of Starsky Robotics." Quote: **"Supervised machine learning doesn't live up to the hype. The sim-to-real gap has very real limits."** A first-person admission from the founder.

**October 2022 — Argo AI.** The biggest failure. **Seven billion burned in five years.** Ford — more than five billion, VW — two point six. On October 26, 2022, Ford announced the wind-down. **More than two thousand engineers laid off.** Ford wrote off two billion seven hundred plus eight hundred twenty-seven million in losses.

**The lesson.** Even when two OEMs with practically infinite capital simultaneously decide that "L4 driverless everywhere" is too big — **the project instantly falls apart**.

**March 2023 — Embark Trucks.** Sixteen months from SPAC IPO to bankruptcy. The SPAC target was five point one six billion. By March 2023 — two hundred thirty laid off. **A canonical SPAC collapse** in one company.

**2023 — Waymo Via.** Alphabet closed its own freight division. If even Alphabet couldn't find a profitable model — a structural signal that the industry doesn't work on unit economics as of that date.

**January 2024 — TuSimple.** Delisting from Nasdaq. Transfer of assets to Chinese structures. **Ninety-one percent of shareholder value lost.**

The common pattern. Capital intensity without revenue. One to seven billion burned before the first commercial dollar. The SPAC bubble. The sim-to-real gap. The carriers wanted **dedicated lanes plus a safety operator**, not full autonomy.

[Transition to s18]

---

## s18 — Cumulative $20B+ · 2 minutes

The aggregate picture. Argo — seven billion. Cruise — ten. TuSimple — about a billion plus the IPO. Embark — three hundred million. Starsky — about two hundred. Waymo Via — Alphabet doesn't disclose.

**In total more than twenty billion dollars** on the ones that didn't survive alone, from 2017 to 2024. Broaden the scope — up to fifty billion.

Compare with Lecture eleven. There, ninety-five percent of GenAI pilots never reach production. The median pilot — tens or hundreds of thousands of dollars. In autonomous transport a provider is **a company that burned one to ten billion**. The AV industry is **thousands of times more expensive** per single failure.

Of the thirty-plus serious AV startups of 2015–2020, **three or four** survived. Survivor consolidation is **ten to one**.

The lesson. When you assess an AV startup as an employer — ask not "is the technology technically cool," but "does the business model work? how much capital per unit of revenue? is there a survivor pattern?"

This slide is **not an argument against AVs as such**. The survivors work — Aurora, Waymo, Apollo Go. There are just fewer of them than it seemed in 2018–2020.

[Transition to s19]

---

## s19 — Survivor consolidation · 2 minutes

Of the thirty-plus — three or four survived. Who and why?

**Waymo** — Alphabet's patient capital, crawl-walk-run, Sun-Belt-only ODD.

**Aurora** — crawl-walk-run, one route, ten vehicles.

**Mobileye** — doesn't do L4 robotaxi at all. Stays in ADAS plus L3 on premium OEMs. **A narrow bet — narrow survivability.**

**Apollo Go** — a Baidu subsidiary, patient capital, the Chinese market.

What do they have **in common**?

First — a **patient-capital parent**. The parent corporation is prepared to wait ten to fifteen years. Argo didn't have one — Ford and VW demanded a return on a five-year horizon. Embark, TuSimple — after the SPAC the public market demanded quarterly revenue.

Second — **ODD discipline**. All stay within a narrow operating domain.

Third — **the absence of overpromise**. No one promised "a million vehicles by next year."

Fourth — **respect for the regulator**. All invest in transparency.

Remember these four traits. This is the survivor pattern, and we'll see it once more in section three.

[Transition to s20]

---

## s20 — Trucker shortage false framing · 2 minutes

Often in meetings you'll hear the argument: "Driverless trucks will solve the trucker shortage." Let's work through it mathematically.

**The ATA figures.** The peak shortage — **seventy-eight thousand drivers in 2022**. **About sixty thousand for 2023** — a decline after the pandemic.

**Aurora's fleet on commercial routes** — **about ten vehicles**. The goal — several tens by 2027.

[pause, slowly]

Seventy-eight thousand shortage. Ten vehicles. **The math doesn't work.**

What **actually works** against the shortage? Structural measures. Recruiting policy. Programs for foreign drivers. Retraining veterans. Wages. Working conditions.

**The lesson for the engineer.** When a vendor uses a macro argument like "we'll solve the labor shortage" — check the arithmetic. If the deployment doesn't scale to the size of the problem — it's a **marketing argument, not an engineering one**. The trucker shortage is a structural labor-market problem. It's solved by policy, not by AVs.

[Transition to s21]

---

## s21 — Highway failure matrix · 1.5 minutes

Let's close section two with four causes of failure for AV-trucking startups.

First — capital intensity without revenue.

Second — regulatory uncertainty. NHTSA SGO plus the legal patchwork across states.

Third — the SPAC collapse of 2021–2023.

Fourth — the sim-to-real gap. **The most fundamental — the technical cause** onto which the others layer.

[Transition to s22]

---

## s22 — Starsky sim-to-real · 1.5 minutes

Before we move to the city — one quote.

March 2020. Stefan Seltz-Axmacher, founder of Starsky Robotics, writes the essay "The End of Starsky Robotics." Verbatim:

[slowly, as if reading]

**"Supervised machine learning doesn't live up to the hype. The sim-to-real gap has very real limits."**

[pause]

The first person in the industry to openly admit that ML doesn't do what was promised. Not a journalist — the founder and CEO of the company that shut down. A candid post-mortem.

When you read optimistic forecasts about autonomous driving — come back to this quote. Seltz-Axmacher wrote it in March 2020 and **predicted everything that would happen to Argo, Embark, TuSimple in 2022–2024**.

This essay is required reading for every AV engineer.

[Transition to s23]

---

## s23 — Section 3 divider · 30 seconds

**Section three of five.** The urban street of robotaxis and the last mile.

Another step up. Pedestrians, cyclists, emergence. Here — the most expensive failure in robotaxi history.

[Transition to s24]

---

## s24 — Waymo survivor · 2.5 minutes

Waymo — the canonical robotaxi survivor.

**March 2026.** Five hundred thousand paid rides per week. Three thousand sixty-seven fifth-generation vehicles. More than ten cities: Phoenix, San Francisco, Los Angeles, Austin, Atlanta, Miami, Dallas, Houston, San Antonio, Orlando. Over 2025 — fourteen million rides.

A tenfold growth over nineteen months.

**The stack.** All sensors, no compromises. An HD map with accuracy about ten centimeters. Lidar — the primary 3D sensor. Cameras. Radar for reliability in bad weather. **Remote operators** — human-in-the-loop for edge cases. They don't drive remotely, but give advice; the vehicle executes on its own.

And **a formal safety case** — a regulatorily auditable document.

What Waymo **does not publish** — profitability per ride. That means either "still negative" or "not disclosed." Any skeptic assumes the former. **The operational scale is impressive, but the unit economics is not yet proven.**

**Waymo's survivor pattern.** Crawl-walk-run. Alphabet's patient capital. Narrow ODD expansion. No overpromise. Respect for the environment. This is **not algorithmic superiority.** Cruise used a similar stack, but violated ODD discipline and went bankrupt. More on that in a few slides.

[Transition to s25]

---

## s25 — China robotaxi · 2 minutes

Alongside Waymo — in China there are three major players.

**Apollo Go (Baidu).** The leader in absolute volumes. **Two hundred forty million autonomous kilometers** globally. **More than seventeen million orders** across twenty-two cities. More than Waymo cumulatively.

**Pony.ai.** Three hundred seventh-generation vehicles, the goal — a thousand by the end of 2025. The only one with a commercial driverless-operation license in **all four tier-one cities**: Beijing, Shanghai, Guangzhou, Shenzhen. More on the next slide.

**WeRide.** Public on Nasdaq. Q3 2025 — revenue thirty-five point three million yuan. Plus seven hundred sixty-one percent year over year.

Goldman Sachs's forecast — the Chinese robotaxi market by 2035 is valued at **forty-seven billion dollars**. A seven-hundred-fold growth. A bull-case scenario, treat it skeptically.

And one more thing. By 2026 the robotaxi industry had split into **two non-overlapping markets**. The Western one — Waymo, Tesla, Aurora. The Chinese one — Apollo Go, Pony.ai, WeRide. A geopolitical feature, worth considering in career planning.

[Transition to s26]

---

## s26 — Pony.ai unit economics · 2 minutes

One detail that the commercial press often confuses.

**In November 2025 in Guangzhou** — this is the **first city** — Pony.ai reached **positive operating profit per vehicle** for the first time. The first publicly confirmed case of positive unit economics in the entire robotaxi industry.

**In February 2026 in Shenzhen** — this is the **second city** — a repeat of the pattern. Three hundred thirty-eight yuan of daily net revenue per vehicle. Twenty-three orders per day. SEC 6-K data.

[pause, slowly]

Remember the sequence. **Guangzhou first. Shenzhen second.** Not the other way around.

What they mean. The unit economics per vehicle in individual cities has turned positive. The vehicle brings in more than it costs to operate.

What they **don't** mean. They don't mean that Pony.ai as a company is profitable. R&D and marketing expenses are not covered by two cities.

**An important milestone** — the first signal that robotaxis can exit venture-burn mode. But not a magic pill. To become profitable — it must repeat in ten cities simultaneously while lowering R&D.

The lesson. **Always demand unit economics per vehicle.** "Total revenue growth" is a red flag.

[Transition to s27]

---

## s27 — Tesla Robotaxi Austin · 2.5 minutes

Tesla Robotaxi is a separate story. Elon Musk's **philosophical bet** on a vision-only stack, without lidar and without an HD map.

June 22, 2025 — the start in Austin. About ten Model Y vehicles. By May 2026 — about **seven hundred thousand paid miles**. **Fourteen crashes** by February 2026.

The main question. **Can this statistic be compared with Waymo?**

The answer — **no, methodologically it can't.**

[slowly]

A correct comparison requires accounting for mileage. Waymo, at five hundred thousand rides a week, drives **tens of thousands of times more miles**. Per million miles Waymo shows a significantly lower crash rate than a human. **For Tesla the sample is too small.** Fourteen incidents over seven hundred thousand miles — a wide confidence interval. You can't categorically conclude "safer or less safe."

To make a statistically valid comparison — you need several million miles in each group. Tesla **doesn't have that yet.**

**The lesson** — anti-confirmation-bias. Crashes per million miles is the right metric. The absolute number is deceptive. "Tesla has fewer crashes than Waymo" — a categorically wrong framing without normalization by mileage.

Tesla **may turn out to be right** in the long run. But for today — the statistical evidence is insufficient, and the engineer must keep the question open.

[Transition to s28]

---

## s28 — Last-mile · 2 minutes

Level four — the last mile. AI in **narrow niches**.

**Starship.** Nine million autonomous deliveries. More than two thousand seven hundred robots. More than sixty university campuses in the US. It works on campuses — a semi-controlled environment. **Doesn't scale in a dense urban environment**: snow, vandalism, handing over a package without a human is impossible.

**Coco Robotics.** More than a thousand robots in Los Angeles. Expansion: Dallas, Miami, Helsinki, Chicago.

**Zipline.** The most impressive story. A hundred million autonomous miles. Two million commercial deliveries. **Twenty-two million vaccine doses in Africa** cumulatively. A seven point six billion valuation.

Where Zipline works — medical delivery in Africa. Strong emotional motivation. A narrow ODD. Regulatory openness.

Where **drone delivery doesn't work** — a dense American or European city. Complaints about noise. FAA restrictions. Handing a package to a tenth floor of a building — an unsolved problem.

**Nuro — a pivot.** Until 2024 — B2C delivery. In 2024 — exit from B2C, a pivot to licensing the stack to OEMs. **The lesson** — B2C delivery isn't profitable in the American urban context. Even a well-funded startup exits when the unit economics doesn't work.

[Transition to s29]

---

## s29 — Cruise centerpiece · 3.5 minutes

This is the **central case of the lecture**. The Cruise-GM exit gathers all the lessons in one place.

[slowly, serious tone]

In 2016 GM acquired Cruise. 2018–2023 — extensive funding. August 2023 — the DMV issued Cruise a commercial robotaxi license.

**On October 2, 2023** — an incident in downtown SF. Around half past nine in the evening. A pedestrian — a woman in her thirties — was crossing the street on a **green light**. A Lexus under human control — **not Cruise** — ran a red, struck her, and threw her **under the Cruise robotaxi**.

Cruise registered the collision in less than a second. But instead of stopping immediately, it **performed an evasive maneuver** — a parallel park to the curb. And it **dragged the victim about twenty feet**.

[pause]

Serious injuries. Lengthy hospitalization.

**On October 24** the DMV revoked the license. Importantly: **not for the incident itself**. On the first request Cruise provided partial video that cut off **before the evasive maneuver**. The full video — only after a specific request.

This is the "misrepresentation" that the DMV cited as the cause. Cruise could have survived the incident itself. **The cover-up it could not survive.**

Next — mass layoffs. **December 2024** — GM announces a full exit. **More than ten billion** in losses. **Less than five hundred million** in revenue. **Twenty to one.**

**Four levels of failure.**

First — **technical**. The stack saw the pedestrian. But the Decide logic produced "pull over" — in the context of "pedestrian under the vehicle" a catastrophe. **A failure of the second stage of the OODA loop** from Lecture nine.

Second — **the business model**. Capital intensity without revenue.

Third — **regulatory and trust**. A violation of transparency. **Trust is a prerequisite; one violation destroyed eight years of work.**

Fourth — **cultural**. The GM-Cruise hybrid culture. SF startup vs Detroit OEM. **A hardware OEM making a pivot into a software platform — an anti-pattern.** GE Predix, IBM Watson, Foxconn Wisconsin — the same story.

[pause]

**The lesson.** When you work at a technology company with regulatory engagement — **transparency with the regulator is not a PR question. It's a structural survival question.** One dragging incident plus a trust violation **kill a billion-dollar program**. This is a lesson of engineering ethics.

[Transition to s30]

---

## s30 — Uber Tempe 2018 · 2.5 minutes

[quietly, seriously]

The heaviest part of the lecture. The most important safety case in the AV industry.

March 18, 2018, around ten in the evening, Tempe, Arizona. **Elaine Herzberg**, forty-nine, was killed. The first victim of an autonomous vehicle in history. She was crossing the road with a bicycle outside a crosswalk. An Uber Volvo XC90, forty miles per hour.

**What happened technically.** The camera detected the pedestrian **five point six seconds before impact**. Perception worked. But **the classifier didn't classify the object as a pedestrian** — Herzberg was outside the crosswalk and with a bicycle, **out-of-distribution** for the training data. The model saw "something," but didn't understand that it was a pedestrian.

**The deliberate disabling of AEB.** Uber disabled the factory automatic emergency braking **deliberately**, to avoid conflicting interventions. When Uber's stack failed the classification, the factory AEB also didn't fire.

**The safety operator** was watching a Hulu TV show. She wasn't watching the road.

The NTSB report: **"Deactivating the AEB increased the risks."** And: **"Uber's inadequate safety culture."**

[pause]

**Four lessons.**

First — **ODD is critical**. Expand the sample to the full distribution, including edge cases.

Second — **never disable factory safety systems**. If your stack conflicts — raise its quality, don't disable the factory system.

Third — **the safety operator's attention is unreliable**. Drivers lose vigilance within ten to fifteen minutes. A structural feature of human attention. One operator is not enough.

Fourth — **safety culture matters**. Not algorithms, but engineering culture determines the safety profile.

This case became the foundation for the NHTSA Standing General Order. An institutional legacy from the death of Elaine Herzberg.

[Transition to s31]

---

## s31 — Tesla Autopilot NHTSA · 2.5 minutes

Tesla Autopilot — the largest-scale safety story in AVs. By October 2025 — in the NHTSA database **sixty-five reports, fifty-four confirmed fatalities**.

**Investigation EA22002.** Opened by NHTSA in 2022. Identified **thirteen fatal crashes with a pattern of foreseeable misuse**.

If a user uses a product in a way the designer could have foreseen — that is a **structural design problem**, not individual fault. The pattern: drivers use Autopilot to sleep. To read. To perform non-driving tasks.

**The 2024 expansion** — crashes in reduced visibility. Sun glare. Parked emergency vehicles — flashing lights disrupt perception. **A new 2025 investigation** — covering roughly two million nine hundred thousand Teslas.

**Four lessons.**

First — **naming matters**. "Autopilot" invites overtrust. In reality — L2 ADAS, requiring attention one hundred percent of the time.

Second — **driver monitoring is mandatory**.

Third — **edge cases in perception**. Distribution shift in real-world conditions.

Fourth — **vision-only without an HD map** is still a research stage for L4. Waymo's approach is proven. Tesla's stack is not.

**The lesson.** When Tesla publishes "Autopilot is safer than a driver" — check the denominator. Tesla compares "a mile on Autopilot" with human fatalities on **all** miles, not on comparable highway ones. An apples-to-oranges comparison.

[Transition to s32]

---

## s32 — Urban failure matrix · 1.5 minutes

Let's close section three with four lessons.

First — **ODD discipline is critical**. Cruise.

Second — **driver monitoring is mandatory**. Tesla, thirteen fatal crashes.

Third — **naming matters**. "Autopilot" invites overtrust.

Fourth — **a hardware OEM does not equal a software platform**. Cruise, GE Predix, IBM Watson, Foxconn Wisconsin — a structural anti-pattern.

These four lessons apply beyond AVs — in any safety-critical AI system.

[Transition to s33]

---

## s33 — Section 4 divider · 30 seconds

**Section four of five.** The black swan and the decision framework.

The topmost step. Here AI is blind by definition. And here — the most important payoff of the lecture.

[Transition to s34]

---

## s34 — Houthi Red Sea · 3 minutes

The Houthis in the Red Sea — the canonical black swan for logistics of the 2020s.

The Houthis began attacking container ships at the end of November 2023. **By February 2024, over two months**, container traffic through the Red Sea **fell by ninety percent**.

The numbers. Daily transit — four million metric tons before the crisis, one point seven after. **Minus fifty-seven and a half percent.**

Through the Red Sea passed about fifteen percent of the world's maritime trade, thirty percent of global container traffic. Shipping companies rerouted around the Cape of Good Hope — plus **thirty percent of transit time**. J.P. Morgan estimated a nine percent reduction in effective global container capacity.

**What happened technically.** Demand-forecasting models trained on 2018–2023 had no signal at all about the Houthi attacks. **Not a poorly trained model.** This was a **complete distribution shift**. The model learned on a distribution **that ceased to exist**.

**Just-in-time chains broke.** Companies optimized for minimum inventory found themselves in shortage.

**What didn't work.** ML demand forecasting — entirely out-of-distribution. Optimization solvers — no data on the new transit times. Real-time tracking — enough data, but that's a symptom, not a cause.

**What worked.** Human dispatchers in the exception teams of Maersk, MSC, CMA CGM. **The real rerouting decisions were made by people, not models.** Scenario planning — companies with pre-built scenarios could respond quickly.

[pause]

**The main pedagogical point.** ML is by definition **blind to out-of-distribution events**. This is not "the AI was trained badly" — it's a **structural feature of any supervised ML**. At level five the right tools are human dispatchers, scenario planning, OR. **Not ML.**

[Transition to s35]

---

## s35 — Suez Ever Given · 2 minutes

The Ever Given — the second canonical example. March 2021. A container ship the size of the Empire State Building **blocked the Suez Canal for six days**.

**Twelve percent of world trade** passes through Suez. **Nine point six billion dollars of cargo** held up.

The main point. **AI had no role. None.**

What happened — **physics plus pilot error**. A strong crosswind. The ship was loaded high — a large sail area. The pilot couldn't compensate. Ran aground.

What unblocked it — **dredging. Tugboats. High water.** Engineering, not AI.

When a vendor says "our AI would have helped prevent Suez" — ask how. Wind forecasting — meteorological services already do that. Coordination between pilot and vessel — communication. Load analysis — statics.

**Sometimes the right answer is not AI. Sometimes the right answer is better engineering.** Better pilots. Better training. Better loading protocols. Better tugs at the ready.

One of the most important lessons of the lecture. When the task is physical — the tool is physical. When the task is in-distribution optimization — operations research. ML occupies a narrow category of tasks where the data exists, the distribution is stationary, the ROI is measurable.

[Transition to s36]

---

## s36 — COVID 2020 · 2 minutes

The third black swan — COVID 2020.

March 2020. A simultaneous demand and supply shock. Demand for toilet paper, masks, disinfectants — up ten to twenty times. Demand for airline tickets — minus eighty to ninety percent. Suppliers in China shutting down.

**ML demand forecasting failed completely.** Models on 2015–2019 saw a stationary distribution. March 2020 went beyond any previous signal.

What broke structurally. **Just-in-time** — the dominant philosophy of logistics for the past thirty years. Minimize inventory. This is optimal in a stationary environment. In a non-stationary one — **fragile**. Companies with zero buffer found themselves in shortage. Just-in-time plus ML forecasting = a fragile system.

What saved them. Human exception teams. Rerouting containers by hand. Arrangements with alternative suppliers. A temporary abandonment of just-in-time.

**The lesson.** Just-in-time plus ML — optimal in-distribution, fragile at black swans. Resilience requires redundancy. This contradicts classical optimization, and management must **consciously** invest in resilience.

After COVID, Maersk, Walmart, Apple began investing seriously in scenario planning. Pre-building scenarios for major disruptions. When the event happens — you already have a ready scenario.

[Transition to s37]

---

## s37 — Trucker shortage structural · 2 minutes

The trucker shortage is an important negative case where **AI doesn't solve the problem**.

Seventy-eight thousand at the 2022 peak estimate. About sixty thousand for 2023. The problem is **structural**, not technological. Inflation-adjusted pay hasn't grown substantially in decades. Working conditions — a lot of time away from home. The average driver's age is about fifty, and young people don't take the job.

**What works.** Policy. Programs for foreign drivers. Retraining veterans. Wages. Working conditions.

**What doesn't solve it.** AV deployments as of 2026. Aurora — about ten vehicles. By the end of the decade — maybe several thousand. But seventy-eight thousand — no.

[pause]

**The lesson.** When a vendor uses a macro argument, "we'll solve the labor shortage" — check the arithmetic. If the deployment doesn't scale to the size of the problem — it's **marketing**. The right answer is **not to buy the AV stack**. The right answer is policy-level measures.

AI **can improve the productivity of existing drivers** — better routes, assistants. UPS does this. But **AI doesn't replace drivers in numbers sufficient for a structural shortage**.

[Transition to s38]

---

## s38 — Decision framework · 3 minutes

**The central payoff of the lecture.** Seven criteria — AI or not AI. Five structural predictors plus two anti-hype filters.

[slowly, clearly]

**First. Is the environment controlled?** Warehouse, port, rails — yes. Level one. Symbotic, Amazon, KONUX. If it's an urban street or a highway — the next criterion.

**Second. Is the task a cleanly stated optimization?** Traveling salesman, routing, scheduling. If yes — **operations research**. Gurobi, CPLEX, OR-Tools are better, cheaper, more explainable than RL or ML. **UPS ORION — the canonical example.**

**Third. Is demand stationary?** If it's predictable across seasons — **EOQ**, safety stock, ABC analysis. Formulas from 1913. They work.

The lesson — an inventory audit. What percentage of SKUs actually requires ML? **Often less than twenty percent.**

**Fourth. Is it safety-critical with a regulatory audit?** FDA, FAA, IMO, ICAO. If yes — **a rule-based approach plus human-in-the-loop**. An ML black box doesn't work in regulated industries.

**Fifth. Is the event in-distribution?** Daily operations under normal demand — ML scoring. A black swan — **a human dispatcher plus scenario planning**. Not ML.

**Sixth. A track record in production operation of six months or more?** This is the first anti-hype filter. Three references with documented metrics — the product is justified. A vendor demo without public metrics — **REJECT by default**. Ninety-five percent of GenAI pilots don't reach production.

**Seventh. Are a baseline and a counterfactual comparison explicitly stated?** This is the second anti-hype filter. A concrete baseline in the same units — manual picking, OR-Tools, EOQ. If the supplier says "better than the competitors" without numbers — **REJECT**. Without a baseline any percentage is marketing.

[pause]

**Application.**

Symbotic warehouse robotization — criterion one "yes." AI applicable.

UPS ORION — criterion two "yes." **OR, not ML.**

Demand forecasting during the Houthi crisis — criterion five "no." **A human dispatcher.**

FDA-regulated cold-chain pharma — criterion four "yes." **Rule-based plus HITL.**

A retailer's seasonal inventory — criterion three partially. **A hybrid of EOQ plus targeted ML.**

A vendor pitch, "a GenAI agent will plan the supply chain itself" — criteria six and seven usually "no." **REJECT.**

**This is not "always AI" or "never AI."** A decision framework that breaks the load into categories and, for each, determines the right tool. The main payoff of Lecture thirteen. Take it with you.

[Transition to s39]

---

## s39 — Alternative toolkit · 2.5 minutes

The alternative toolkit. Six classes of tools as alternatives to AI.

**First — operations research.** Gurobi, CPLEX are commercial. Google OR-Tools is open. **UPS ORION — the canonical proof.**

**Second — classical inventory.** EOQ, safety stock, ABC analysis. Formulas from 1913. Relevant for a large share of SKUs.

**Third — scenario planning.** Not software — a methodology. Shell since the 1970s. Pre-built scenarios: "What if the Red Sea is closed?" When the event happens — you have a ready scenario.

**Fourth — rule-based vision.** OpenCV is open. HALCON and Cognex are commercial. Bottle inspection at a brewery — the example from Lecture eleven.

**Fifth — hybrid vision plus signal processing.** Container-damage inspection — vision plus ultrasound plus radar.

**Sixth — human-in-the-loop.** Regulatory audit and emergency events. Maersk exception teams rerouted around the Cape of Good Hope — HITL in action.

**The main point.** A logistics engineer who knows only AI is **an incomplete engineer**. The complete toolkit — six tools. AI is **one of six**.

The lesson. When you start a job — **the first bet is on classical tools**: OR plus EOQ plus rule-based. If they don't work — then add ML. **Not the other way around.** Vendor proposals often try to sell you AI where OR-Tools is enough.

The second main payoff of the lecture. Take it with you.

[Transition to s40]

---

## s40 — Q&A + seven questions for the vendor · 3 minutes

The last content slide. **Seven questions** you will ask any logistics AI vendor.

**First.** What is the comparison against the OR baseline — Google OR-Tools, Gurobi, CPLEX? If "we didn't do such a comparison" — a red flag.

**Second.** What is your ODD, and how is a new expansion validated? The Cruise dragging incident — a failure of ODD discipline specifically.

**Third.** What is your driver-monitoring stack? Tesla EA22002, thirteen fatal crashes with foreseeable misuse.

**Fourth.** What is the ratio of kilometers in simulation to kilometers on the road? Starsky's sim-to-real gap — the main cause of failure. Millions in simulation and zero on the road — a serious red flag.

**Fifth.** What is the error rate on seasonal distribution shifts? Black Friday, Christmas. How often is the model retrained?

**Sixth.** What certifications? FDA Part 11, ATEX, ISO 26262, NHTSA SGO. A regulatory audit is mandatory.

**Seventh.** What are the unit economics? Per vehicle, per route, per ton. Pony.ai the first with positive operating profit per vehicle — Guangzhou November 2025 first, Shenzhen February 2026 second. If a vendor doesn't publish unit economics — it's either "still negative" or "not disclosed." The skeptic assumes the former.

[pause]

**Carry the seven questions with you.** The second practical part of the toolkit.

And now — a few minutes for your questions.

[Q&A pause — 2-3 minutes]

[Transition to s41]

---

## s41 — Closing hero + bridge to Lecture 14 · 2 minutes

[shift to a closing tone]

The final slide.

Today we walked through the five levels of the environment ladder. **One** — the warehouse, AI mature. **Two** — the highway, Aurora the first commercial one, twenty billion burned. **Three** — the urban street, Waymo survived, Cruise went bankrupt. **Four** — the last mile, narrow niches. **Five** — the black swan, AI blind, the tools are human dispatchers and scenario planning.

[slowly]

**Survivors respect the environment. They stay in a narrow ODD. They don't overpromise.** Cruise vs Waymo — both with the same stack. Waymo survived because it was cautious in its expansion. **A lesson of engineering humility.** Discipline, transparency with the regulator, the priority of safety.

**The bridge to Lecture fourteen.** In the next lecture — telecommunications, network infrastructure, cybersecurity. A different environment — cyber instead of physical. This environment will have its own structure, which the next lecture will reveal on its own terms.

What **carries over** — the seven AI/not-AI criteria: environment, task type, demand profile, regulatory setting, in-distribution event, the vendor's track record, and an explicit baseline. The cyber environment has all of these, and the same skeptical skill applies. The specific telecom tools are different, but the logic of parsing a vendor's proposal is the same.

The specific tools will be different. The skill — the same.

The main point: **the main predictor of AI's success in logistics is the structure of the environment, not the ambition of the stack and not the volume of capital.**

Thank you.

---

## After the lecture (for the lecturer)

### Q&A — what might come up

- **On Tesla** — why is vision-only not proven? Answer — statistical volume, not philosophy. Tesla may turn out to be right, but not on seven hundred thousand miles.
- **On Russia** — what should a graduate do? Answer — Cognitive Pilot, autonomous KamAZ, Sber logistics, Wildberries, Delovye Linii. A master's in AI or operations research.
- **On OR vs ML** — where is the boundary? Answer — well-defined optimization → OR. Pattern recognition + big data + non-stationarity → ML. Most tasks are in the first category, most vendors sell the second.
- **On black swans** — how to prepare? Scenario planning plus redundancy plus exception teams. Not ML.

### Next steps

- Announce the next lecture (telecommunications).
- For students — read NTSB HAR-19/03 (Uber Tempe) and the Seltz-Axmacher essay before the seminar.
- Seminar tasks — three cases: an AV-trucking pilot checklist, a Cruise root-cause analysis, an ML routing vendor evaluation.
