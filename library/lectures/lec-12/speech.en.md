---
lecture_number: 12
lecture_title: "AI in Manufacturing Automation and Digital Twins"
artifact: speech
status: revised
version: v2
length_words: ~6200
duration_min: 75
target_wpm: 75
issue: 133
audience: "students-engineers 3rd year (universal)"
keystone_axis: "AI autonomy scale in manufacturing A0→A1→A2→A3; the digital twin — a bridge between steps"
locked_numbers_source: "chapter v3 (4 parts) + plan v2 carry-forward"
pacing_target: "≤ 95 wpm hard cap on each fragment; ~73 min of active speech + 2 min buffer"
inclusive_markers: "≥10 «мы с вами» distributed across 8 sections"
bridge_phrases: "8 dividers — каждый явно объявлен"
failure_blocks: "Southeast Asian Port + 75% twin fail + ChatGPT MOV %M99999 + sim-to-real T=300/315°C fouling + фарма ±0,5% vs FDA ±0,1% + Gartner 40% agentic + 11–14% energy expectation (EY 2025)"
derived_from:
  - "chapter.md (Part 1, v3)"
  - "chapter-part2.md (Part 2, v3)"
  - "chapter-part3.md (Part 3, v3)"
  - "chapter-part4.md (Part 4, v3)"
  - "deck.yaml (v3, 39 слайдов)"
  - "slides/sNN-*.md (39 файлов)"
created: 2026-05-22
---

# Lecture 12. Lecturer's Speech. AI in Manufacturing Automation and Digital Twins

**Duration:** 75 minutes (~73 min of active speech + 2 min buffer). **Pace:** ≤ 95 words per minute, target ~75 wpm.

**Structure:** 8 sections aligned with slides s01–s39.

---

## §0. Opening, cover, and the keystone axis (~5 min)

### [s01 · 1 min] Hero hook — Hannover Messe 2026

Good afternoon. On the screen is a shot from Hannover Messe this year, the world's leading industrial-automation trade fair. On the left — the Siemens booth with the Digital Twin Composer product. On the right — NVIDIA Omniverse and the Cosmos physical-AI models. These are two public premieres of 2026, after which the "digital twin" stopped being a marketing term and became a working tool.

[pause 2 sec]

Today I want us to answer together a simple question: to which level of AI autonomy can a real factory be raised, and where is the digital twin mandatory as a bridge between the levels. This is the keystone axis of the lecture.

### [s02 · 1 min] Lecture cover

The topic is "AI in Manufacturing Automation and Digital Twins." Lecture 12 builds on Lecture 11, where we worked through discrete and process manufacturing and the five key vendors. Lecture 11 asked "what kind of manufacturing." Today — "to which level of autonomy AI can be raised and under which architectural conditions." Two orthogonal axes that together give the full map.

### [s03 · 1 min] Lecture map

Eight sections. First the keystone axis — the autonomy scale. Then — what a digital twin is in 2026, per Kritzinger and per GOST R 57700.37. Next — the four steps in turn: A0 observes, A1 advises, A2 closes the loop, A3 acts autonomously. Then — a large section on the boundaries: ten structural criteria where AI is not needed, and which alternative is better. At the end — the operational architecture, the Russian context, and the career bridge.

### [s04 · 2 min] The keystone axis — autonomy scale A0→A3

Here is the axis we are here for. Four steps. **A0 — observe:** AI emits a signal, a human makes the decision. Example — computer vision for quality control. **A1 — advise:** AI proposes an action, the operator agrees explicitly. Example — alarm prediction. **A2 — close the loop:** AI changes parameters within a safe zone without the operator's consent to each individual move. The canonical example — Yokogawa FKDPP at JSR, 35 days in 2022. **A3 — act autonomously:** AI makes decisions without a human in the loop. In 2026 these are just a handful of cases — Toyota Digit and the BMW Leipzig pilot.

[pause]

An important caveat. A0–A3 is our pedagogical adaptation of SAE J3016 and ISO/IEC 22989, not an industrial norm. And do not confuse it with the ISA-95 layers L0–L2 from Lecture 11. ISA-95 describes where a system physically sits in the hierarchy. A0–A3 is how much trust the engineer delegates to AI. Two orthogonal axes.

The digital twin here is not a separate technology but a bridge. Without it, the climb from A1 to A2 is blind faith. With it, it is managed risk through a sandbox. We will keep coming back to this picture for the whole hour and a quarter.

---

## §1. What a digital twin is in 2026 (~10 min)

### [s05 · 0.5 min] Divider

Section one of eight. What a digital twin is in 2026. The foundation of the scale; without it the rest does not stand.

### [s06 · 2 min] Kritzinger taxonomy + GOST R 57700.37

In 2024–2025 the phrase "digital twin" was used for three different things. A CAD drawing of a pump — a twin. A monitoring screen with live sensors — also a twin. A full-fledged simulation with feedback — a twin again. Three artifacts, different architecture, different competencies.

Werner Kritzinger settled this question in 2018 in IFAC-PapersOnLine. Three levels. **Digital model** — no stream of live data. A CAD drawing. **Digital shadow** — a data stream from the physical to the digital, without feedback. A monitoring screen. **Digital twin** — a two-way loop, with the ability to simulate a control action and apply the result to the physical object.

Remember the strict definition: a twin is a two-way loop. CAD is not a twin. A dashboard is not a twin. Only when there is a link back — that is a twin.

Russia has its own standard — GOST R 57700.37-2021 "Digital twins of products." Approved by Rosstandart, in force since 2022. The definition essentially coincides with Kritzinger — "two-way information links." We will return to it in the seventh section.

### [s07 · 2 min] Four-layer architecture

Any working twin is four layers at once. Remove any one — and it is no longer a twin.

**Layer one** — the physical asset with sensors. A pump, a reactor, a furnace. On it — thermocouples, pressure, vibration, and flow sensors. Connected through OPC UA and MQTT — two industrial protocols, we will return to them in the sixth section.

**Layer two** — the digital model. Physical equations plus machine learning where the physics is complex. The combination is a hybrid model, or physics-informed machine learning.

**Layer three** — AI inference. A defect classifier, a remaining-useful-life predictor, an advising or controlling policy.

**Layer four** — the consumers of the result. The operator interface, the PLC, the humanoid. Without this layer AI thinks in a vacuum.

A subtle point. **The type of consumer determines the autonomy step.** The operator's screen — A0 or A1. A PLC without the operator's consent — A2. A humanoid without a human in the loop — A3. The same AI inference, different consumers, different steps.

### [s08 · 2 min] Market 36 → 180 billion

The numbers. The digital-twin market — **$36.19 billion in 2025, forecast $180.28 billion by 2030**, a compound annual rate of nearly 38 percent. In parallel — AI in manufacturing, forecast $155 billion by 2030 at a rate of 35.3 percent. Already in 2026 the subsegment "industrial AI on top of OPC UA and MQTT" is $17.15 billion.

[pause]

It sounds like a gold rush. But let us fix the counter-statistics right away. **75 percent of digital-twin projects do not reach payback because of a weak data layer.** In the energy sectors — oil and gas, chemicals, utilities — in the EY 2025 survey only 11–14 percent of users say the technology meets expectations: 14 percent in oil and gas and chemicals, about 11 percent in utilities. Gartner: **40 percent of agentic AI projects will be canceled by 2027.**

This is the gap between promise and delivery. Not a bug of the market but a statistical norm. The engineer will meet it in the very first year of work.

### [s09 · 2 min] Southeast Asian Port — 12 million down the drain

A concrete example of a failure. A large container port in Southeast Asia launched a twin project in early 2023. The goal — optimizing the movement of containers, cranes, and trucks, forecasting congestion. Budget — **$12 million**. Term — **18 months**. Result — **the project was written off in 2024.** No production deployment, no ROI.

What went wrong. Three causes out of six structural ones. Fragmented data — cranes of different years, trucks with different telematics, container tags of different standards. Low quality — some cranes without vibration sensors, GPS accurate to plus or minus five meters. And, crucially, the absence of a clear target task. The team was building "a twin of the port in general."

The main lesson. They built a beautiful 3D scene of the port in Unity. The camera flies over the port, containers light up. This is a **digital shadow with expensive graphics, not a twin** per Kritzinger. There is no feedback, the "what would have been" simulation does not work. Remember this pattern — 3D without a data layer. We will see it once more in the fifth section.

### [s10 · 2 min] Data-layer audit — five questions

From this lesson comes a practical tool. **The data-layer audit. Five questions before starting a pilot.**

First. Is there historical data for at least a year? A minimum to cover seasonal cycles and changeovers.

Second. Is the sensor polling frequency at least ten times higher than the required control bandwidth? The Nyquist rule.

Third. Is the provenance of the labeling documented? Who, by what criterion, when did the labeling?

Fourth. Is sensor drift calibrated and logged?

Fifth. Is a data owner assigned? A specific person with a last name and a phone number.

[pause]

If even one question is "no" — the pilot must not launch. This is a remediation project. First you fix the data layer, then you launch AI. Teams that do it the other way around fall into the category of the 75 percent of failures.

The cost of the audit — $20,000–50,000, two to four weeks. Three to five percent of the pilot budget. The most defensible investment in the project.

---

## §2. A0 — Observe (~10 min)

### [s11 · 0.5 min] Divider

Section two of eight. The first step — A0, observe. The safest, the most widespread, high ROI at manageable risk.

### [s12 · 3 min] Vision QC — 99% accuracy and 100 good parts per shift

Computer vision for quality control is the most mature application of AI in manufacturing. A camera on the conveyor, the model renders the verdict "good or defective."

The 2026 figures — accuracy of 99 percent and above, false positives from 0.1 to 2 percent. A concrete case — an electronics manufacturer, 1.8 percent false positives. A printed circuit board, 5 megapixels, 200 milliseconds per board.

This is a qualitative leap relative to the legacy machine vision of 2015–2020 with a typical false-positive rate of about 50 percent — a reduction of 25–500 times.

Note the word "tuned." Six stages: camera and lighting, the training set, model training, threshold calibration along the ROC curve, four weeks of field validation, drift monitoring. The term — four to six months. The cost — $200,000–500,000. Teams promising "vision quality control in two months" are skipping stages.

[pause, lower voice]

And now — the most important arithmetic of this section. Let us compute together. A line produces 10,000 parts per shift. False positives are one percent. **100 good parts per shift rejected as defective.** Over 250 shifts a year — 25,000 parts. At a rework cost of half a dollar — $12,500 extra. And this is the easy case.

In process manufacturing a false positive is a batch rejected as non-conforming. The cost — tens of thousands of dollars. On a semiconductor line with ten vision-control stations the cumulative risk is almost 10 percent.

This is not "AI is bad." This is a structural limitation. AI cannot simultaneously have zero false positives and zero misses — the two ends of the same ROC curve. The engineer chooses the point consciously.

And there is a cost that standard ROI models do not count — **the loss of operator trust.** If he sees AI reject a hundred good parts per shift, after three shifts he turns the system off. This is signal fatigue — the same mechanism by which pilots switched off GPWS after a series of false alarms.

### [s13 · 3 min] Predictive maintenance — ROI 10:1

The second dominant A0 application is predictive maintenance. Instead of the scheduled "every 500 hours of pump operation replace the bearing" — maintenance by actual condition. Machine learning looks at vibration, temperatures, acoustics, and predicts the remaining useful life. When the life approaches the threshold — a work order is issued.

The Deloitte 2026 figures. Average ROI — **ten to one over two years relative to scheduled calendar maintenance** — this is the baseline, when the bearing is changed on schedule regardless of condition. A reduction in maintenance costs — 25–40 percent relative to the same calendar mode. Unplanned downtime — minus 30–50 percent relative to the reactive "it breaks — we fix it." An extension of equipment life — 20–40 percent. Accidents — minus 40 percent.

Remember the baseline. If a vendor says "ROI 10:1" but does not name what they computed it against — that is a signal to stop.

Concrete cases. An average plant — investment $200,000–600,000, annual savings $1.2–3.5 million, payback 18–36 months. A cement plant — **a 57-fold ROI over six months** on software sensors alone, without replacing physical equipment. A chemical plant — **$2 million in annual savings.**

57 times in half a year sounds fantastic, but the logic is simple. One unplanned shutdown of a rotary kiln lasts three to seven days, costs hundreds of thousands of dollars in lost product. If predictive maintenance prevented two or three such shutdowns in half a year — an ROI of 57 comes out arithmetically.

[pause]

But here too — conditions of applicability. Three conditions. Historical data for at least a year with a detailed failure log. At least 30 events of each type in the training set. And the failure physics is gradual — bearing vibration grows over weeks before catastrophic destruction, not instantly. If even one of the three conditions is not met — an alternative is needed.

### [s14 · 2 min] Where vision and PdM do not apply

Two traps of A0.

The first — vision control for tolerances of plus or minus one thousandth of a millimeter. Precision parts: optics, aerospace, medical implants. No camera in 2026 delivers such accuracy on a conveyor. The physical limit — the wavelength of light, about half a micron.

The alternative — a combination of three tools. Metrology: coordinate-measuring machines. Geometric tolerances per ASME Y14.5. And statistical process control — Shewhart control charts, the Cp and Cpk indices. AI here is not "better than a human" — it physically falls short.

The second trap — predictive maintenance for rare events. Failures less than once a year — a training set of fewer than 30 events, statistically insignificant.

The alternative — physics-based simulation plus the RCM methodology, reliability-centered maintenance. Developed by Nowlan and Heap in 1978 in aviation for United Airlines and Boeing. The gold standard for aviation, nuclear power, high-risk oil and gas.

ML and RCM are not "AI better than a human." Different tools for different tasks. ML — where there are many events and gradual dynamics. RCM — where there are few events and each is potentially catastrophic.

---

## §3. A1 — Advise (~10 min)

### [s15 · 0.5 min] Divider

Section three of eight. A1 — advise. AI proposes a concrete action, the operator agrees explicitly. The most widespread active step of adoption in 2026.

### [s16 · 2 min] MES advisory mode + alarm prediction

The boundary between A0 and A1 is conceptual. A0 informs. A1 recommends. "Temperature 312 degrees, above normal" — A0. "Temperature 312, reduce steam flow by 5 percent over two minutes" — A1.

The first application — MES in advisory mode. MES knows which orders are in the queue, which machines are free. The AI layer advises a sequence. The simplest variant — energy-efficient scheduling: AI puts energy-intensive operations at night, saving tens of percent on electricity.

The second application — alarm prediction. In continuous manufacturing the dispatcher receives a stream of alarms from SCADA. In a crisis — dozens per minute, the operator cannot keep up. Machine learning learns to recognize the precursors of cascades: five to fifteen minutes before a big incident. Documented deployments give a reduction of the alarm flood by 30–60 percent and a reduction of reaction time by two to three times. Most accidents in chemical manufacturing include an episode when the operator drowned in a stream of alarms.

The condition of applicability is one and the same. If SCADA does not log historical values with precise timestamps — there is no training set, the project stalls. The data layer sinks the project.

### [s17 · 3 min] PLC Copilot 85% — and the failure of ChatGPT on the S7-1500

The third application of A1 is the most interesting. A PLC code assistant. Here 2026 brought the greatest progress.

PLC Copilot, PLCAutoPilot, Wipro PARI — specialized assistants trained on a corpus of verified PLC programs per IEC 61131-3. They know the legal memory addresses for Siemens S7-300, S7-1200, S7-1500. They understand the scan cycle.

The figures. Time to write a typical module — **from three or four days down to ten minutes.** A 20-fold speedup. Accuracy of generated code — **85 percent.** The remaining 15 — manual correction.

[pause, lower voice]

And now let us look at what happens when an engineer of the lazy path takes universal ChatGPT and writes: "Write ladder logic for the S7-1500: on I0.0 rewrite the value of T1 into address M99999."

ChatGPT outputs:

```
NETWORK 1
LD I0.0
MOV T1, %M99999
```

It looks plausible. The MOV command exists, timer T1 exists, the operand is syntactically valid. This code **will compile in TIA Portal with no visible errors.**

And it will not run on the hardware. In the Siemens S7-1500 the M memory area is limited to address **M65535.** M99999 is beyond the address space. ChatGPT does not know this: it was trained on the general internet, it does not distinguish controller models by architectural constraints, it has no model of scan-based execution.

The consequences. The controller goes into STOP mode — all equipment stops. In the best case the conveyor is down, thousands of dollars of losses per hour. In the worst — a batch stuck in the reactor, an unsafe state.

This is not "AI is bad." This is an **architectural mismatch** between the paradigm of large language models — generating plausible text — and the paradigm of the PLC — deterministic execution with hard physical constraints.

There is one alternative. Do not use universal LLMs on the PLC directly. A specialized assistant with the engineer in the loop. Or the classic — engineer plus simulator plus IEC 61131-3.

### [s18 · 2 min] The "engineer in the loop" architecture

From this comes the A1 architectural pattern. **Engineer in the loop. Four mandatory stages.**

Stage one — AI proposes. The specialized assistant generates a candidate with a rationale.

Stage two — the engineer verifies. Not "an eye over the shoulder" but responsible validation. In regulated environments this is a legal requirement. The engineer puts a signature under the decision.

Stage three — simulation. TIA Portal Test Suite, Studio 5000 Logix Emulate. The simulator reproduces scan-based execution, catches most of the errors.

Stage four — a safety check and staged deployment. Test bench, safe mode, metric monitoring. In stages: machine, line, shop floor.

This process is the operational condition of A1, not an option. Teams that economize on stages two through four fall into failures. The boundary between A1 and A3: at A1 the human must be in the loop.

A parallel from the world of programming — code review. Each PR is checked by a colleague, critical avionics DO-178C — by formal review. In manufacturing AI, the same principles apply.

---

## §4. A2 — Close the loop (~10 min)

### [s19 · 0.5 min] Divider

Section four of eight. A qualitative leap. A2 — AI changes parameters without the operator's consent to each action.

### [s20 · 3 min] Yokogawa FKDPP — 35 days at JSR

The canonical case of industrial-grade RL for continuous-process control is Yokogawa FKDPP at JSR. Lecture 11 worked through this case from the algorithmic angle. Today we look at it from the architectural one.

Yokogawa is a Japanese vendor of instruments and control systems for process manufacturing, founded in 1915. In 2018 the Yokogawa research team, together with the Nara Institute of Science and Technology, published the **FKDPP** algorithm — factorial kernel dynamic policy programming. This is off-policy reinforcement learning with factorial kernel decomposition.

In 2022 Yokogawa, together with JSR Corporation, a Japanese chemical holding, deployed FKDPP at a real chemical plant. The task — optimizing a distillation column. **35 days of continuous operation under RL control without operator intervention. The first documented industrial-grade case of RL in continuous-process control.**

What "35 days" means. Most cases before 2022 ran for hours or a few shifts, then RL was switched to advisory mode. 35 days is a full monthly cycle of operations: feedstock changes two or three times, planned changeovers, reactions to external changes. This is a demonstration of operational maturity, not merely algorithmic workability.

Yokogawa, in a public press release, reported significant energy savings, keeping quality within specification, and no safety violations.

[pause]

And here is the main architectural question. Why exactly did Yokogawa bring RL to production, whereas dozens of competitors got stuck in simulation? The answer is not the algorithm. The answer is the digital-twin architecture.

### [s21 · 3 min] The twin as a sandbox for RL

Yokogawa had an internal detailed physical simulation of the distillation column. Mass transfer by the Stefan-Maxwell equations. Heat transfer by Fourier's law. A tray model of equilibrium stages. This is a digital twin in the strict Kritzinger sense. A two-way loop, you can apply an action to the simulation and get a response.

The RL agent trained **in simulation** for thousands of episodes. Before release onto the real equipment. The simulation provided a safe sandbox. Erroneous actions did not lead to an explosion or a release. The learning speed was accelerated a hundredfold. Rare scenarios — non-standard compositions, sensor failures — were generated by the engineer, not "waited for until they happen."

[pause]

Without this sandbox RL is impossible. Had they trained directly on the real column, training would have taken years, and most of the trials would have ended in equipment shutdown or a safety violation.

In 2026 what used to be Yokogawa's internal infrastructure is available to external teams. **NVIDIA Omniverse plus Cosmos** — foundation models of physical AI. **Siemens Digital Twin Composer** with the ability to rewind the simulation. The engineer rewinds the process to any moment of the last 48 hours and checks what would have been under a different decision.

**The architectural infrastructure for safe learning is still required. And it is expensive.**

The practical takeaway for us. When a vendor proposes an A2 deployment, the first question is where is the twin for training the policy. If they trained on real equipment — ask for three years of safe-operation history. If they trained on a simplified simulation — a high risk of a gap. If there is a full physics-accurate twin plus domain randomization plus a runtime monitor — a serious case.

### [s22 · 2 min] Sim-to-real gap: T=300°C / T=315°C + fouling

And one last honest note about RL. The twin as a sandbox does not solve all the problems. The main residual risk is the "simulation → reality" gap.

A concrete example. RL is trained on a simulation at a temperature of 300 degrees on the feed tray. After two months of operation on the real column, surface deposits appear — a layer of polymerized products on the walls of the heat exchanger. The heat-transfer coefficient drops by 10–15 percent. To reach the same heating power, the real temperature of the supplied steam becomes 315 degrees.

The policy has not seen the 315-degree regime in the training set. It interprets it as abnormal. It overcompensates — sharply reduces steam flow. **A 10 percent deviation from nominal productivity.**

In the academic literature this is a documented pattern. MDPI Processes 2025. Six sources of the gap: fouling, catalyst wear, sensor drift, a change in feedstock composition, a change in pressure, failures of auxiliary equipment.

The defense — three levels. The first — domain randomization: training on a population of simulations with varied parameters. The second — fine-tuning on limited real data after simulation. The third — runtime monitors switching to MPC or manual control when going beyond the training distribution. Skipping any one — a structural risk.

### [s23 · 2 min] When RL is not needed — MPC and formal verification

The criteria of applicability of RL and its alternatives.

Case one. **Safety-critical logic.** Emergency shutdown, interlock chains. The **IEC 61508** standard, four Safety Integrity Levels. Most safety-critical control is SIL 2 or 3.

RL is **not certified** under IEC 61508. The reason — the stochasticity of the policy, no verification guarantees. The alternative — a hard-wired PLC plus formal verification: TLA+, SPIN, Coq, SCADE from ANSYS. Widely used in aviation, nuclear power, on the railways.

Case two. **A process with known physics.** If the physics is described by equations — Navier-Stokes, heat transfer, kinetics — choose MPC. Provable stability guarantees through Lyapunov theory, explicit constraints in the optimization, a transparent solution. Mature libraries — Aspen DMC3, Honeywell Profit Suite, gPROMS — since the 1970s.

By default for a new project — MPC. A move to RL — only when it is demonstrated that MPC is insufficient. The modern pattern is the CIRL hybrid: MPC inside with guarantees, RL as a tuning layer.

---

## §4.5. A3 — Act autonomously (~3 min)

### [s24 · 0.5 min] Divider

Section four and a half of eight. The highest step. The shortest section — in 2026 in manufacturing these are just a handful of cases.

### [s25 · 2 min] Toyota Digit + BMW Leipzig + three blockers

Two publicly known cases. **Toyota Digit** — humanoids from Agility Robotics. Since 2024 on the RAV4 assembly line, seven or more units on intra-shop logistics. **BMW Leipzig** — the first European humanoid pilot, 2026.

Almost all publicly known A3 in 2026 is these two cases. And the pattern is one: **the A3 cases of 2026 are logistical, not controlling.** No one has publicly launched RL autonomously on a chemical column. No one has given a humanoid the job of dosing an active component in pharma.

[pause]

Three structural blockers of mass A3.

**Regulatory.** IEC 61508, ATEX, ISO 10218 require a deterministic trajectory. Neural networks do not provide it. Toyota and BMW work around this by placing Digit in a non-critical logistics zone.

**Cost.** A humanoid — several hundred thousand dollars per unit. It pays off only in niches with a high cost of labor. Toyota in the US, at a rate of 30 dollars per hour, pays it back in two to three years.

**Stack complexity.** A3 requires a twin plus AI at the network edge plus a safety zone plus fleet management. Most factories have none of these components in an industrial-grade form.

A parallel from the automotive industry. Waymo as of May 2026 is deployed in more than six US cities — Phoenix, San Francisco Bay Area, Los Angeles, Miami, Atlanta, Austin — about three thousand robo-taxis. But this is still geo-fenced L4, in strictly defined zones, not "everywhere." Cruise suspended operations in October 2023 after a series of incidents; GM fully shut down the division in December 2024. Tesla FSD remains L2, not L4. In manufacturing — the same pattern.

---

## §5. Where AI is not applicable (~15 min)

### [s26 · 0.5 min] Divider

Section five of eight. The densest in the share of failures. **When AI is not needed and which alternative is better.** This is the central part of the course's mission: an engineer is valued for being able to say no to unsuitable AI.

### [s27 · 2 min] Southeast Asian Port — a second pass

Let us recall the case from the first section. Southeast Asian Port. 12 million, 18 months, written off in 2024. We already know the technical causes: fragmented data, low quality, the absence of a target task. Now — through the lens of the fifth section.

The team built a beautiful 3D scene of the port in Unity. Management was impressed. The budget was approved. **A 3D visualization without a data layer is a museum, not a twin.** This is not a rare anti-pattern. It is the most common mistake of 2024–2026.

The correct sequence is "data layer first, visualization last." Six to twelve months to set up the data layer. Then three to six months for a minimal physical model. Then three months for AI inference. And only at the end — the 3D visualization for communication with management.

### [s28 · 4 min] Ten criteria — the table

Ten structural criteria where AI is not a fit. This is an operational artifact. Print the table. Take it with you to your internship.

Four categories. **Data:** three, four, ten — rare events, an unstable process, a failed data-layer audit. **Cost of error:** one, five, nine — safety-critical, tight tolerances, negative ROI. **Regulation:** seven and eight — FDA without explainability, ATEX Zone 0. **Solution known:** two and six — known physics, universal PLC code.

Let us walk through the most important ones.

**Criterion one. Safety-critical logic.** RL is not certified under IEC 61508 SIL 2/3. The alternative — a hard-wired PLC plus formal verification. From half a million to two million dollars, one to two years to deploy, decades of maturity in aviation and nuclear power.

**Criterion two. A process with known physics.** MPC dominates. 300 thousand to 1.5 million dollars, half a year to a year and a half, maturity since the 1970s.

**Criterion five. Tight tolerances of plus or minus one thousandth of a millimeter.** Metrology plus geometric tolerances plus statistical process control. Vision physically falls short.

**Criterion six. Universal code generation for the PLC.** A catastrophe — we saw MOV %M99999. The alternative — a specialized PLC Copilot with the engineer in the loop.

**Criterion seven. A regulated environment without explainability.** FDA 21 CFR Part 11 and GAMP 5 do not accept a black-box ML. The alternative — explainable AI: SHAP and LIME, a hybrid with rules, a decision log.

**Criterion eight. ATEX Zone 0** — explosive category zero. A standard NVIDIA Jetson physically cannot go there. The alternative — ATEX-certified sensors in Zone 0 plus remote processing in a safe zone.

**Criterion ten. The absence of a clear target task.** The cause of 75 percent of failures. The alternative — a data-layer audit by our five questions.

The algorithm. Describe the task in one phrase. "Data" — three questions. At least one "no" — STOP. "Cost of error" — three questions. At least one "yes" — STOP. Regulation. Solution known. Only if all ten are passed — AI is applicable.

### [s29 · 3 min] Pharma + dosing + FDA — worked example

A concrete instantiation. A direct reference to Lecture 7, where we introduced the principle "AI in FDA-regulated processes works in advisory mode, not autonomy." Now we bring it to numbers.

The scenario. Pharmaceutical manufacturing, a tablet line with a dose of 100 milligrams. The FDA tolerance — **plus or minus 0.1 milligram, that is, 0.1 percent.** Manufacturing is continuous, with PAT sensors: NIR spectroscopy, Raman spectroscopy.

The ML model is trained on historical data. Accuracy on the test set — **plus or minus 0.5 milligram, 0.5 percent.** Decision accuracy — **90 percent.** On production data over half a year — similar.

[pause]

What the FDA requires. Accuracy of 0.1 percent — the USP level for critical components. A full audit log for every batch-release decision. Validated software per GAMP 5 category four or five. And the patient's right to appeal — the decision must be explainable in court.

The gap analysis. AI accuracy of 0.5 percent versus the required 0.1 — **a five-fold gap** not in AI's favor. 90 percent means: every tenth decision is wrong. For patient safety this is **unacceptable.**

**The verdict. AI is not a fit for the final batch-release decision. Period.**

The alternative — a two-layer architecture. Level one — AI as a process-knowledge tool at the design stage. Here the FDA accepts AI: the model helps choose setpoints, forecasts quality. Level two — for the release decision — a quality-control operator draws a statistical sample per USP <905>. Ten units of the batch with an acceptance value of no more than 15. A laboratory HPLC analysis. The operator signs off the release.

The procedure is validated over decades, transparent to the FDA, legally defensible. This is an application of the scale — for critical quality attributes in pharma we do not, in principle, climb above A1.

### [s30 · 2 min] Gartner cancellation context

Sober statistics for calibrating expectations. **Gartner: 40 percent of agentic AI projects will be canceled by 2027. 30 percent of GenAI initiatives will not pass the proof-of-concept stage by 2025.** In parallel — a study from the Sloan School of Management (MIT Sloan 2025): 95 percent of GenAI pilots do not reach production.

This is not "the industry is bad." This is a **baseline of expectations** in the early maturity phase of any technology. The cloud-services wave of 2008–2012, the mobile wave of 2010–2014, the AI wave of 2015–2020 — the first five to seven years of any wave give 70–80 percent of failures. Then the community accumulates success patterns and the share drops to 30–40 percent.

For us this means that **healthy skepticism** is statistically justified. When a vendor promises "agentic AI for manufacturing" — ask for three to five documented failures over the last 24 months in the same industry. If the vendor cannot name a single one — they are either a newcomer without a mature product or dishonest.

### [s31 · 2 min] Five questions for the vendor — a practical tool

From everything we went through in this section comes **a tool for your pocket.** Five questions for the vendor. Write them down.

**First.** Show three documented failures of your system over the last 24 months in the same industry. Request letters from clients, not press releases.

**Second.** At which step of the autonomy scale — A0, A1, A2, or A3? If the answer is "autonomously" — ask for a video of operation without a human in the loop over 30 days.

**Third.** What data-layer audit did you perform? It covers our five questions from the first section. If "we use your data as is" — that is a signal of a 75-percent failure.

**Fourth.** What is your alternative if the pilot does not reach production? Professionals offer a rollback agreement with metrics and financial terms.

**Fifth.** Show a client in our subsegment — discrete, process, regulated. Specifically: company, line, year, contact.

Most marketing offers do not withstand all five. Those that do are candidates for a serious pilot. This is an extension of the three questions from Lecture 11.

---

## §6. OT/IT architecture 2026 (~6 min)

### [s32 · 0.5 min] Divider

Section six of eight. Which architecture is needed if the task is applicable.

### [s33 · 2 min] Seven layers

A modern manufacturing AI system is **seven explicit layers.**

The first — sensors. Temperature, pressure, vibration, current, flow, video. Connected through OPC UA and MQTT.

The second — the network. The key technology of 2026 is **TSN, Time-Sensitive Networking**, IEEE 802.1. Deterministic delivery with a guaranteed latency. Without TSN, A2 is impossible on horizons faster than a second.

The third — AI at the network edge. GPU microservers on the equipment cabinets. NVIDIA Jetson Orin, Dell Edge Gateway. Inference time — **less than ten milliseconds.**

The fourth — the executive and dispatch layer: MES and SCADA.

The fifth — the digital twin. Siemens Xcelerator, NVIDIA Omniverse, PTC ThingWorx, AVEVA System Platform, Bentley iTwin.

The sixth — the cloud. Long-term storage, model training, fleet analytics, reporting.

The seventh — the human in the loop. All safety-critical decisions pass through a human.

A key feature of the 2026 stack — you do not need to reprogram existing PLCs. The AI layer is layered on top through OPC UA. Teams demanding "a full replacement of the PLC with AI at the network edge" are mistaken.

### [s34 · 2 min] OPC UA + MQTT + TSN

Three protocols without which the 2026 architecture does not exist.

**OPC UA — data semantics.** A standard that describes what a number means on the data bus. Not "0x4271 at address 40001," but a named object with a unit of measurement, a range, a timestamp, a status. The dominant exchange standard of 2026.

**MQTT — transport.** A lightweight publish-subscribe protocol, developed by IBM in 1999 for oil pipelines. Without built-in semantics. Often complements OPC UA: OPC UA at the lower level, MQTT — at the upper level to the cloud broker.

**TSN — determinism.** Time-Sensitive Networking. Time synchronization to microsecond accuracy — 802.1AS. Transmission of critical packets in protected time slots — 802.1Qbv. Duplication through redundant paths — 802.1CB. **Without TSN, A2 is limited by human reaction speed. With TSN — a closed loop on milliseconds.**

### [s35 · 2 min] Lighthouse Network

The benchmark the industry looks to. **Lighthouse Network** — a program of the World Economic Forum and McKinsey. Started in 2018. By 2026 — **220+ factories in 35 countries, 23 new ones declared this year.**

The characteristics of Lighthouse 2026: according to McKinsey and the World Economic Forum data for January 2026, **94 percent of successful transformations combine several technology domains** — AI is used most often, alongside IoT, the cloud, digital twins, autonomous mobile robots. This is against forty percent in ordinary factories, where there are usually one or two technologies. **Plus 16 percent EBIT** relative to industry peers. A multi-technology transformation — not AI alone, but a combination.

Examples: Schneider Electric Le Vaudreuil in France, BMW Regensburg, Siemens Amberg, Foxconn Shenzhen, Hitachi Hitachinaka, POSCO Pohang. There are no Russian factories in the Lighthouse Network as of 2026. This is a structural fact we will return to in the seventh section.

[pause]

A sober note. Lighthouse 220+ are the successes, a sample from the top quarter of global manufacturing. In parallel — per the EY 2025 survey, 11–14 percent of users in oil and gas, chemicals, and utilities say the digital twin meets expectations, and 40 percent of agentic projects will be canceled by 2027 per Gartner's forecast. **Architecture does not guarantee ROI if the data layer is weak.** The seven layers and Lighthouse are a map of the possible. The 75 percent failure is a map of the real. The engineer must live in both.

---

## §7. Russian context + career bridge (~5 min)

### [s36 · 0.5 min] Divider

Section seven of eight. The Russian context and the career bridge.

### [s37 · 2 min] GOST + KamAZ + Rosatom + Nornickel

Three anchor Russian cases.

**KamAZ** (a large Russian truck manufacturer) — a pioneer of digital twins in Russia since 2020. KAMA-1, an electric truck, was developed entirely in a twin up to the prototype. The effect, per RBC Trends, relative to the pre-twin baseline: a reduction of conveyor downtime by 10–30 percent, a reduction of the time to bring a new model into production by 15–25 percent.

**Rosatom** (Russian state nuclear-energy corporation) — a strategy of technological sovereignty. T-FLEX PLM as an alternative to Siemens NX. AtomMind — an internal platform: numerical modeling plus ML. Logos — a Russian CFD. Used for twins of reactors and turbines.

**Nornickel** (Russian mining/metals major — nickel, palladium) — process control with AI in metallurgy. Since 2024 — vision control and software sensors on flotation, a closed loop of micro-tuning of reagents in **non-critical zones.** This is A2 in the strict sense. The effect: an improvement of metal recovery by 0.5 percentage points from a base of 80–85 percent at the Talnakh plant; an upper estimate of up to 1.5 pp for AI flotation overall.

Regulation. **GOST R 57700.37-2021** — the Russian base. **Federal Law 187-FZ** — the law on critical information infrastructure. **Decree No. 250** of May 2022 — domestic software and certified protection means for significant facilities.

A CII engineer with 187-FZ expertise is one of the most in-demand competencies of 2026. The salary premium — 30–50 percent in large holdings.

### [s38 · 2 min] The career bridge — four roles

Where to go next. Four main career roles for a graduate going into industrial AI in 2027–2030.

**Industrial AI/ML engineer.** Designs and trains models for vision control, predictive maintenance, alarm prediction. Python, PyTorch, TensorFlow, MLOps. The decisive hiring factor — **knowledge of the process physics.**

**Digital-twins engineer.** Builds and maintains a twin for a specific line. Deep command of a single platform: Siemens Digital Twin Composer, NVIDIA Omniverse, PTC ThingWorx, Bentley iTwin. CAD, numerical modeling, OPC UA and MQTT, GOST R 57700.37.

**MES integration specialist.** Deploys the AI advisory mode into an existing MES. Siemens Opcenter, Rockwell FactoryTalk, SAP MII — one stack in depth. ISA-95.

**Edge AI engineer.** Deploys AI inference on devices near the equipment — this is "AI at the network edge." C++ or Rust, embedded Linux, ONNX, TensorRT, OpenVINO, OPC UA TSN, cybersecurity for CII facilities.

Beyond technical skills — understanding of physics and processes, communication with shop-floor engineers, knowledge of regulation. An AI engineer spends 30–50 percent of the time on communication, not on code.

---

## §8. Closing + bridge to Lecture 13 (~5 min)

### [s39 · 5 min] Closing — Toyota Digit as the first step of the supply chain

What we took away today. Five things.

**First — the A0–A3 scale.** An operational axis distinct from ISA-95. Observes, advises, closes the loop, acts autonomously.

**Second — the digital twin as a bridge.** Without a twin the climb to A2 is blind faith. With a twin — managed risk through a sandbox.

**Third — the ten criteria of "AI is not a fit."**

**Fourth — the seven OT/IT layers** with OPC UA, TSN, and AI at the network edge.

**Fifth — the Russian context:** GOST R 57700.37, KamAZ, Rosatom, Nornickel, and four career roles.

The main skill is beyond facts. **The ability to classify an AI offer by the scale and to refuse an unsuitable one.** When you hear "AI reduces downtime by 70 percent" or "agentic AI for our MES" — the first reaction is not "impressive" but: at which step? what data-layer audit? what baseline? what alternative on failure?

[pause]

And the bridge to the next lecture. On the screen — Toyota Digit on the RAV4 assembly line. Intra-shop logistics. **The first step of the supply chain.** When AI rises from intra-shop to multi-warehouse logistics, from the shop floor to the global chain — we move on to Lecture 13. The topic — **"AI in Logistics, Supply Chains, and Transport."**

The A0–A3 scale carries over into logistics with an adaptation. But the physical risk is higher: cars on public roads. Regulation is tougher: traffic rules, FMVSS, ECE. Certification procedures are better developed — UNECE WP.29.

You take away the scale as a model in your head. In Lecture 13 you will apply it in a new domain.

Thank you for your attention. I am ready for questions.

---

## Lecture preparation (pre-flight checklist)

Concrete actions for the lecturer on the day of the lecture, before going into the auditorium.

### Verify-on-day-of (current numbers)

1. **Lighthouse Network on s35.** Open https://www.weforum.org/communities/global-lighthouse-network/. If an updated list is published after WEF Jan 2026, update the number "220+ / 23 new 2026."
2. **Toyota Digit deployment on s25 and s39.** Check https://www.agilityrobotics.com/news + the Toyota Motor Corporation newsroom. On s25 and s39 it says "seven or more units." If an update is published by the lecture date — replace it.
3. **Yokogawa FKDPP attribution NAIST.** Verify via https://www.yokogawa.com/news/press-releases/. If the public press release states something other than NAIST — update §4 speech (s20).
4. **Gartner agentic AI 40% cancellation on s08 and s30.** Open https://www.gartner.com/en/newsroom. If a revised forecast is published — update the number.

### Technical checks

5. **Open the PPTX on the projector.** The file — `library/lectures/lec-12/rendered/lec-12.pptx`. Check the render of all 39 slides. Special attention: s17 (PLC Copilot vs ChatGPT), s22 (T=300/315°C), s28 (10-criteria table).
6. **PDF available as a fallback.** `library/lectures/lec-12/rendered/lec-12.pdf`. If the projector does not pick up the PPTX — switch to the PDF.
7. **Hero s01 and s39 — real images.** s01 Hannover Messe 2026 hero — visually corresponds to the fair. s39 closing — Toyota Digit on the RAV4 line.

### Content reserve

8. **Q&A backup ready.** Open `library/lectures/lec-12/chapter-part4.md` — 14 questions with answers of 250–350 words.
9. **Locked numbers reference card.** Print the page with the key numbers: 36→180 billion / 155 billion / 17.15 billion / 75% twin fail / 11–14% energy expectation (EY 2025) / 40% agentic / 99% vision (vs ~50% legacy) / 100 good / 10:1 PdM (vs calendar) / 57× cement / 35 days Yokogawa / 85% PLC Copilot / M65535 / 220+ Lighthouse / 94% multi-tech / 16% EBIT / Waymo 6+ cities ~3000 units / Cruise suspended 10.2023, GM shut down 12.2024.

### Open notes

- Bridge text to Lecture 13 — the exact wording: "AI in Logistics, Supply Chains, and Transport."
- If the audience asks "when full A3?" — the answer: "not because of the technology but because of regulation; aviation walked this path over 70 years, manufacturing is still at the stage of 1960s aviation."

---

**End of speech.** The duration of the active speech is ~73 minutes, plus a 2-minute buffer. Ready for Q&A.
