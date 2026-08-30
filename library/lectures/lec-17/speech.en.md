---
lecture: 17
module: 3
title: "Lecture 17. Systematizing knowledge and skills — the engineer's AI map"
audience: "студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)"
status: draft
version: 1.1
target_duration_min: 75
target_words: ~6450
wpm_max: 95
keystone: "2D-плоскость инженерной карты AI: горизонталь — Применимость ИИ (нужен ли AI), вертикаль — Лестница автономии L0→L5 (сколько ему доверить)"
updated_at: "2026-05-28"
author: "speech-writer v1 (Phase 9 draft from chapter v3 multi-part); Phase 11a polish v1.1 (book-editor)"
changelog:
  - "v1.0 (2026-05-28) — Phase 9 draft from chapter v3 multi-part."
  - "v1.1 (2026-05-28) — Phase 11a cascade polish per Phase 10 critics: s37 finale collapsed to single list-of-three + 8-cases as separate unit (reader P1-3); s22 tail 5→3 industries with contrast-anchors (reader P1-1); s09 ЖКХ weak flags grouped + «район без воды» elevated as culmination (reader P1-4); s30 thematic anchor between failures 9-12 (reader P1-2); s05 «0.76→0.63» named as 0-to-1 quality metric (reader P2); WPM trim — all fragments now ≤95 wpm (methodology P1-1); 5 section-dividers varied off «N-й раздел из пяти» (methodology P1-2); «дидактически важно»×2 → direct theses (methodology P1-3); «почти революционная»→«дефицитная» (methodology P1-4); D1 robotaxi geometry «середина справа»→«верхний левый/зона предупреждения» + black swan→«нижний левый» per scatter_coords canon (consistency P1)."
slides_covered: [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37]

preflight:
  - "Open https://www.gartner.com/en/research/methodologies/gartner-hype-cycle — verify that AI is still near the peak of hype in the current Hype Cycle; if Gartner has shifted it into the trough — reflect this verbally on s01."
  - "Check https://sloanreview.mit.edu — the status of MIT NANDA / Sloan «State of AI in Business 2025» (95% of GenAI pilots never reach production); if the 2026 report is out with a different number — fix it on s30/s31."
  - "Check https://www.mckinsey.com/capabilities/quantumblack/our-insights — McKinsey «State of AI» 5.5% high-performers; make sure this is a DIFFERENT measurement from MIT (do NOT conflate it with the 95%)."
  - "Prepare a backup screenshot of the title slide s01 (assets/screenshots/s01-*.png — a collage of successful and failed cases) in case the projector fails."
  - "Prepare printouts of the 4 reference cards (cheatsheets/ — Decision matrix #1, Autonomy ladder #2, Failure-modes #3 A4 + Master-map #4 A1): ≥30 copies of #3, hang poster #4 on the lecture-hall wall before the start."
  - "Open https://artificialintelligenceact.eu — verify the dates of the EU AI Act phased enforcement (prohibited practices February 2025, high-risk August 2026) on s07."
  - "Check https://www.waymo.com — the current status of Waymo cities (on s14/s22 — SF / Phoenix / LA); if they have expanded the ODD — mention it as a live shift of a point on the map."
---

# Lecturer's speech · Lecture 17. Systematizing knowledge and skills — the engineer's AI map

**Duration:** 75 min (with a reserve for Q&A).
**Version:** v1.1 (Phase 11a cascade polish — Phase 10 critic findings applied).

## Preparation before the lecture
- Hang poster-card #4 (the map of 16 industries, A1) on the lecture-hall wall before the students arrive — it will be the physical anchor of Section 3.
- Hand out or lay out the printouts of cards #1, #2, #3 — the students must take away a paper artifact.
- Open Gartner's Hype Cycle + MIT Sloan + McKinsey in separate tabs to verify that the numbers are current (see the checklist at the top of the file).
- A backup screenshot of the title slide s01 in case the projector fails.
- Remember: this lecture **does not introduce a new technology** — it is a synthesis. If something "hangs" — we go back to the map on s02 and to the poster on the wall.

---

## [s01 · 2 min] — Title + hook: one skill out of the entire course

[slowly, straight to the room]

Let me open with a provocation. **If I could give you only one skill out of this entire course — what would it be?**

[pause]

Not "being able to write prompts." Not "knowing what a transformer is." Not "being able to hook up ChatGPT through the API." All of that is useful. But each of these skills has a short shelf life. Prompt engineering was a hot profession in twenty twenty-three — and by twenty twenty-six the models rewrite bad prompts themselves.

[pause 2 sec]

The one skill that will not go stale is the **ability to say "no" to AI**. More precisely — the ability to articulate **in which tasks AI does not fit**. And this skill is asymmetrically valuable. There are too many people who can launch ChatGPT and put together a demo. But an engineer who looks at someone else's project and in fifteen minutes says "this won't fly in production, and here are the reasons why" — that person saves the company millions.

That person is you. After this course. And today the two of us will assemble everything we covered across sixteen lectures into a single map.

That is the topic of Lecture seventeen. The final one.

[Transition to s02]

---

## [s02 · 2 min] — Keystone: the 2D plane of the engineer's AI map

[more slowly — this is the keystone axis]

Here is the course's main artifact. Memorize this picture — the two of us will keep coming back to it for the whole hour.

Before us is a **two-dimensional plane**. Two axes.

**The horizontal axis — AI applicability.** It answers the question: **is AI even needed here?** On the left — deterministic non-AI tools: operations research, the classics. On the right — full AI. And note: a high value on the right **does not mean "better."** It means "AI fits." And on the left it is not "backwardness" — it is "the classics win."

**The vertical axis — the ladder of autonomy, from zero to five.** It answers a different question: **how much do you trust it with?** At the bottom — the human does everything. At the top — full autonomy with no human.

[pause]

And here is the key idea; it is important that we lock it in right away. **These are two independent axes.** You can have high applicability and low autonomy: medical diagnosis from images — AI works beautifully, but it always advises, and the doctor decides.

Two axes give four quadrants. The upper right — mature success stories. The lower right — high applicability, but autonomy screwed down by the regulator; the quadrant is **filled**. The lower left — the classics win. And the upper left — low applicability with high autonomy — is the **empty and dangerous quadrant**. The warning zone. If you end up there — stop, redesign.

The entire lecture is about how to use this map. Let's go.

[Transition to s03]

---

## [s03 · 0.5 min] — Section 1 (section intro)

We start with the horizontal axis of the map.

**When to apply AI, and when not. Seven measurable criteria.**

Seven working cases, two failures — and all of it about one thing: how to tell a task for AI from a task where AI does not belong.

---

## [s04 · 2 min] — The seven criteria as sequential gates

Seven criteria. Let me get to the main rule for applying them right away.

**This is not a scored checklist.** We do not add up points. The criteria work as **sequential gates**. If you get a clear "no" on even one of them — the task is not suitable for full AI autonomy. Full stop. One "no" — and that's it.

[pause]

Here are the seven questions. Write them down.

First. **Is the environment closed or open?** Is there fast feedback?
Second. **Is there enough training data?** And does it match what will occur in operation?
Third. **Is the task repeatable and high-volume — or one-off?**
Fourth. **What is the cost of an error and the blast radius?**
Fifth. **Is there a ground truth against which to check quality?**
Sixth. **Are explainability and audit required?**
Seventh. **Does AI pay off against the best classical alternative?**

[pause]

Seven questions. On a new task — fifteen to twenty minutes. And in those twenty minutes you save the company months on a failed pilot.

Let's go through them in pairs — because in real life they work in tandem.

---

## [s05 · 2.5 min] — Criteria 1 + 2: the closed loop and the data

**Criterion one — a closed loop versus an open environment.** The most fundamental one.

A closed loop is when the result is visible quickly and unambiguously, and the environment does not deliberately resist. Remember software development? You wrote code — the compiler tells you in seconds whether it compiled or not, the tests tell you in minutes whether they pass. An open environment is the opposite: the result is visible slowly or not at all, the environment changes on its own, and things happen that were not in the data.

[pause]

And here is the canonical failure. Remember **Zillow** — buying up housing based on ML valuation, iBuying? The model was trained on pre-pandemic prices; the volatility of twenty came — and the model could no longer keep up. The result: a three-hundred-four-million-dollar write-down, the division shut down, about two thousand people out of eight thousand facing layoffs. The open market killed the model.

And now a closed loop. Remember **See & Spray** from John Deere — vision on a tractor that distinguishes a weed from the crop? A controlled row, a clear picture, fast feedback. Minus fifty percent herbicide: instead of about a pound per acre — half a pound. Across five million acres — but for scale that is half a percent of the nine hundred million agricultural acres in the US.

**Criterion two — is there enough data?** And, most importantly — does it match the reality of operation. Remember **Epic Sepsis** — the sepsis-prediction model? Here the quality metric is on a scale from zero to one. The vendor promised close to zero point seven six. An independent check on thirty-eight thousand patients gave zero point six three — nearly chance. This is not "seventy-six percent dropped to sixty-three percent"; this is the model's quality collapsing to a coin flip. The lesson: the vendor's benchmark is not your productivity. Recheck on your own data.

---

## [s06 · 2.5 min] — Criteria 3 + 4: repeatability and the cost of an error

**Criterion three — repeatability and volume.** Trivial economics that gets ignored again and again. AI pays off only if the task occurs often.

Remember **GitHub Copilot**? Code autocomplete. It happens billions of times a day. Over twenty million paying users. The cost of one error is a second — you press Escape. Enormous volume, tiny cost of an error — perfect for AI.

And here is the opposite: an architectural decision for a large system. Once every year or year and a half, an enormous cost of an error, the context does not fit into any model. Here AI does not pay off. Here you need a senior.

[pause]

**Criterion four — the cost of an error and the blast radius.** This is the criterion most often underestimated at the start.

The cost of an error — what happens if AI makes a mistake? From "you press Escape" to a catastrophe. And the blast radius is how widely the consequences of a **single** failure spread.

[lower your voice]

Remember **CrowdStrike** — July twenty twenty-four? A computer-protection system shipped one update with a bug. It automatically flew out to **eight and a half million** devices within hours. Blue screens across the whole world. Delta canceled seven thousand flights. Damage to the affected companies — over five billion dollars.

[pause]

Compare: a Copilot error — one developer, roll back in a second. A CrowdStrike error — eight and a half million devices, roll back by manually rebooting each one. A difference of **orders of magnitude**. The engineer's heuristic: high cost multiplied by a large radius, plus slow detection, plus slow rollback — **do not let AI act**. Only advise.

---

## [s07 · 2.5 min] — Criteria 5 + 6: ground truth and explainability

**Criterion five — is there a ground truth?** Here Judea Pearl's ladder of causation from the very first lecture will help us. Three levels.

The first — association: "what usually goes together with what." Correlation. AI can do this natively. The second — intervention: "what will happen if I do this." A controlled experiment is required. The third — counterfactuals: "what would have happened if this had not occurred." And this — is the human's territory. The model has no access to hypothetical worlds.

[pause]

Remember **Galactica** from Meta? "AI for science," launched in November twenty-two. Pulled within forty-eight hours. The model confidently generated fake papers with fake authors and fake references — everything formally correct-looking. Why? In science the ground truth is a **reproducible experiment**, not nice-looking text. No ground truth — hallucinations are inevitable.

**Criterion six — explainability and audit.** Regulators around the world are moving toward mandatory explainability. The EU AI Act — the law came into force in August twenty-four, the prohibitions took effect in February twenty-five, the requirements for high-risk systems — from August twenty-six. High-risk — medicine, hiring, credit, infrastructure — is required to explain its decisions.

Remember **Apple Card**, twenty nineteen? The viral tweet that a husband was given a limit twenty times higher than his wife with the same income. The New York State investigation in twenty twenty-one **cleared** the charge of intentional discrimination — sex was not even a feature in the model. And the reputation was destroyed anyway. The lesson is not about bias. The lesson is about explainability: a black box in a regulated field kills trust, even when there is no malicious intent.

---

## [s08 · 2.5 min] — Criterion 7: economics versus the classics

**Criterion seven — does AI pay off against the classical alternative.** The most ignored one. AI has to beat the **known classics** on money.

Remember **UPS ORION** — optimizing couriers' routes? Since two thousand three. Three to four hundred million dollars saved per year. And you know what? There is **not a single neural network** in it. It is classical operations research: integer programming, heuristics. Dispatchers trust the system almost automatically — but this is trust in a deterministic solver with mathematical guarantees, not in a learned model.

[pause]

When vendors offered UPS to "improve ORION with deep learning" — the question was only one: by how many percent better? The answer — a couple of percent on narrow subtasks, and the cost of integration and support ate up that benefit. UPS stayed with the classics.

The same in process control. Remember MPC — model predictive control? It has worked in petrochemicals and metallurgy for decades. When they offer to replace it with reinforcement learning — we ask: by how much better? Yokogawa demonstrated the first industrial application in twenty-two — an improvement of a few percent on a very narrow task. A success, but **not a displacement** of MPC.

[straight to the room]

The lesson of the seventh criterion: **measure the baseline before you start.** How much does the classics give? What delta does AI promise? Will the delta pay off all the infrastructure, monitoring, and the risk of the model going stale? If not — declining AI is **not a defeat**. It is an engineering decision. And that, by the way, is what distinguishes an engineer from someone with hype in their eyes.

---

## [s09 · 2.5 min] — A worked example: AI for water in utilities

Let's apply all seven criteria to a task that was **not** in the course. This is an exercise.

The scenario. The city administration comes to you. A vendor offers a system called "AquaOptima" for optimizing drinking water. The promise: minus thirty percent losses, twenty-five million rubles saved per year, payback in eighteen months. Deep learning plus automatic valve control. They want a six-month pilot.

We go through the criteria — and immediately see that the weak spots pile up in clusters.

**First — three yellow flags in a row.** The environment: the water main is partly closed, but consumption depends on the weather, holidays, a soccer match — semi-open. The data: meters have existed for decades, but leaks may not have been recorded, repairs — in paper logs; an audit is needed before the pilot. The ground truth: total consumption is known, hidden leaks are not. Three "caution" flags even before the main one.

**And here is the main one.**

[lower your voice]

The cost of an error. What happens if AI closes the wrong valve? **A district without water for hours. Tens of thousands of residents.** That right there — is a stop for full automation. Valves are operated by a human, full stop.

[pause]

Add explainability — the decisions are public, they get contested, a black box will not pass. And the economics: minus thirty percent — compared to what? To zero or to classical EPANET? A comparison is needed.

**The verdict.** We do **not** go into a six-month pilot with full automation. Instead: two months — a data audit and a baseline on EPANET. Four months — an A/B pilot: half the city with AI advice, half — EPANET only. All actions — by a human.

And note the main thing: **the procedure is the same** for any task. Tomorrow they'll offer you AI for the shop's energy consumption — you apply the same seven questions.

---

## [s10 · 0.5 min] — Section 2 (section intro)

We have worked through the seven criteria — that is the horizontal axis. Now we climb onto the second axis.

**The ladder of autonomy, from zero to five.** Exactly how much to trust AI with.

---

## [s11 · 2.5 min] — The ladder of autonomy: the full display

Six rungs. Memorize them along with me — this is the vertical axis of our map.

**L0 — no automation.** AI is not involved. The human does everything. And this is **not backwardness** — many tasks remain here deliberately: the final strength calculation for an aircraft wing with the signature of a certified engineer, for example.

**L1 — advisory, it advises.** AI classifies, predicts, recommends. But the decision is **always** the human's. This is the most common level of mature industrial operation. Most AI in medicine and finance lives right here — by design, not out of underdevelopment.

**L2 — supervised, it acts with confirmation.** AI performs an action, the human confirms each one.

**L3 — conditional, a narrow domain.** AI acts autonomously, but only within a strictly delineated area. Once it leaves its boundaries — it hands control back to the human.

**L4 — high, a broad domain.** AI acts across a broad range of conditions. The human is on the loop, observes, intervenes occasionally.

[lower your voice]

**L5 — full, everywhere and always with no human.** This is a **theoretical limit**. In twenty twenty-six it is practically **unattainable** in any industry of the course. That is why it is gray at the top.

[pause]

And one more thing. Why are the rungs discrete, rather than a smooth scale? Because between them are **real boundaries**. Legal ones: L1 is allowed everywhere, L4 in medicine — already not. Engineering ones: moving from one rung to the next is a different discipline, not "more of the same."

---

## [s12 · 2.5 min] — Mapping the local scales

The main scientific result of this lecture — right now the two of us will fold **all the local scales of the course** into a single ladder. But with an important caveat.

Remember, in software development there was an A-B-C-D ladder: autocomplete, a block, a whole pull request, an engineer-agent. In aerospace — L1 to L5. In factory automation — A0 to A3. All three — are **scales of autonomy**, degrees of AI's participation in the action. And they map directly: autocomplete and A1 — are our L1, the engineer-agent and A3 — our L4.

[pause]

But here is a subtlety; it is important that we understand it. **Not all the local scales of the course are about autonomy.**

Remember logistics? There was a ladder of five levels of environment structure: a controlled warehouse, a semi-structured highway, a city street, the last mile, a black swan. That is **not autonomy** — it is about the **environment** in which AI works. An orthogonal axis.

And remember cybersecurity? "Sees — Decides — Acts." That is **not autonomy** — it is a **functional decomposition**. And each of the three functions can be at its own level: "Sees" — at L3, "Decides" — at L1, "Acts" — on rules with no AI at all.

And here is what follows from this in practice. When a vendor comes and says "our AI is at level L3" — you ask: **"In which notation? Is that about autonomy, about the environment, or about a function? Where is the formal definition of L3? Where is the regulatory approval?"** These three clarifying questions weed out some eighty percent of marketing claims.

---

## [s13 · 2 min] — L1 advisory: deeper

Let's stop on L1 — the most common rung. AI advises, the human decides.

What does AI do at L1? It classifies — sepsis or not, a pathology on an image or normal, fraud or a legitimate transaction. It predicts — demand, reactor temperature, delivery time. It recommends — a line of code, the order in which to read images.

Examples we have covered. **Stripe Radar** flags a suspicious transaction — an analyst decides. **Aidoc** in medicine prioritizes images — a radiologist decides. **Crop Wizard** in agriculture answers the farmer with references — the farmer decides. **Project Maven** in intelligence marks objects on satellite images — an analyst decides.

[pause]

Now — how to move up from L1 to L2? Four conditions. The baseline and the improvement from AI are measured. There is a change-control procedure. A rollback is ready. And false positives are acceptable — because at L2 the human confirms each action, and if AI triggers falsely often, the human gets tired.

And right away an anti-pattern. Remember **Klarna**? The fintech in February twenty-four announced that AI had replaced seven hundred agents. And a year later — a **reverse hire**. AI could not cope with rare, complex requests. The lesson: you cannot call a system "advisory" if in fact it acts without a human.

---

## [s14 · 2.5 min] — L2 supervised and L3 conditional

Two middle rungs.

**L2 — supervised.** AI acts, the human confirms each action. **Stripe Radar** in auto-block mode for clear fraud — it blocked, the team sees it and can unblock. Yokogawa in chemistry — AI turns the reactor's parameters, the operator can intervene at any moment.

[lower your voice]

And the main anti-pattern of L2 — the **bored human in the loop**. Remember **Uber in Tempe**, twenty eighteen? An autonomous car, a safety driver in the seat. The dashcam showed: in the moment before the collision the driver was looking at their phone. The pedestrian Elaine Herzberg was killed. The lesson is harsh: L2 does not work when confirmation is boring and rare. A human physically cannot pay close attention for hours to something that is almost always correct.

[pause]

**L3 — conditional.** AI acts autonomously, but only within a strictly delineated operational area. The main concept here is the **operational design domain**, ODD. A formal definition: what weather, what time, what district. And the system must **know** when it has left its boundaries, and refuse to operate.

Remember **Waymo**? A robotaxi in specific districts of San Francisco and Phoenix, without heavy rain. Within its domain it works beautifully. Beyond it — it does not go.

And here is the anti-pattern — **expanding the domain without verification**. Remember **Cruise** — another robotaxi? On October second, twenty-three, after a collision the car dragged a pedestrian twenty feet while trying to pull over to the shoulder. The license was revoked, and in December twenty twenty-four GM shut down the division entirely. The lesson: the domain is expanded **gradually**, with verification at each step.

---

## [s15 · 2 min] — L4 high and L5 full

The top rungs.

**L4 — high.** AI acts autonomously across a broad range of conditions. The human is on the loop, not in each step. Remember warehouse robotics — **Symbotic**, **Amazon Sparrow**? Millions of operations a day, minimal human intervention. Waymo in a broad domain. See & Spray across five million acres — the operator monitors, but not every frame.

[pause]

And again an anti-pattern — and we already know it. **CrowdStrike.** A broad domain — eight and a half million devices — means an **enormous** blast radius. And the update flew out without a canary release, without a staged rollout. The lesson inverts intuition: a broad domain requires **stricter** deployment discipline, not less.

[lower your voice]

**L5 — full.** Everywhere and always with no human. Why is it unattainable? Five structural blocks. Insurers do not insure L5. Regulators require human oversight. Out-of-distribution events cannot be structurally cured — no amount of data will cover the whole future. Legal liability is undefined. And the economics: L4 already covers ninety-nine percent of real scenarios — reaching for L5 is expensive for a tiny benefit.

And the ethical block. Remember the debate about lethal autonomous weapons systems? Technically L5 for weapons is possible. Ethically — no. This is not a technical limit, but a human choice.

---

## [s16 · 2.5 min] — Anti-patterns at each rung

Let's assemble the anti-patterns together — one for each rung. This is entirely about the boundaries of applicability.

[rhythmically, an enumeration]

**At L1 — exceeding the role.** Klarna. The AI was called advisory, but it acted. The result — a reverse hire.

**At L2 — the bored human in the loop.** Uber in Tempe. A pedestrian died because confirmation was boring and rare.

**At L3 — expanding the domain without verification.** Cruise. Dragged a pedestrian, the license revoked, the division shut down.

**At L4 — acting without a canary and a rollback.** CrowdStrike. A broad domain multiplied every error.

**At L5 — the ethical and regulatory block.** The debate about autonomous weapons. Technically possible, ethically forbidden.

[pause]

And a separate anti-pattern across all the levels — **skipping a rung**. Companies try to jump from L1 straight to L3-L4, bypassing L2. This **never** works. Why? Because each transition is a different engineering discipline and months or years of work.

Numbers for scale. The path from L1 to L4 in a single task — typically three to six years. Waymo started from the DARPA race in two thousand seven, and commercial L4 — in twenty-four. **Seventeen years.** So a startup promising "L4 in two years" is either being disingenuous or has miscalculated.

---

## [s17 · 2 min] — A worked example: AI for administering exams

Let's apply the ladder to another task not from the course.

The scenario. A university is considering an AI assistant for administering exams: it checks answers, searches for plagiarism, assigns preliminary grades. **What is the maximum permissible level of autonomy?**

Let's work through it.

The cost of an error — high. An unfair grade, an accusation of plagiarism, an academic mark for life. Explainability — critical: the student has the right to appeal, and it is necessary to explain **why** AI decided that this is plagiarism. The regulatory window — academic rules usually require a human examiner. The ground truth — for tests there is one, for essays — partly.

[pause]

**The verdict: L1 at most. It advises.** AI reads the answers, assigns a preliminary grade, flags possible plagiarism with an explanation and references. The instructor sees this package and makes the final decision. The student can contest it — the expertise is human.

And what is needed to raise it to L2, where AI assigns and the instructor confirms in batches? Measure the baseline: how many errors the instructor makes now, how many — AI on a test sample. If AI is **systematically more accurate** — then you can. But with explicit change control.

L3 and L4 for this task — are **impermissible**. Both by regulation and by ethics. The student has the right to a human decision. This is the typical diagnostic of the ladder: each application is a question of "what is the maximum permissible here, and why."

---

## [s18 · 0.5 min] — Section 3 (section intro)

We have built both axes. The seven criteria — are the horizontal. The ladder — is the vertical. Now we have a plane — time to populate it with points.

**Sixteen industries on a single map.** Right now we'll plot them all.

---

## [s19 · 1.5 min] — The map of 16 industries: lead-in

Before plotting — let the two of us look at the course's sixteen industries all together.

[sweep your hand over the mini-grid]

Each of them raised its own **local axis**. Software development — the A-B-C-D ladder. Finance — the closed versus the open world. Medicine — closed loops and the human in the loop. Aerospace — the observe-decide-act loop. Agriculture — the agro ladder. Logistics — five levels of environment structure. Cybersecurity — "sees-decides-acts." Science — the ladder of the scientific cycle. Oil and gas — a two-by-two matrix.

[pause]

And when you see them side by side, one thing emerges. **All these axes are about one thing.** About how much AI takes on the action, how much the environment allows it, and where the line runs beyond which the human must remain in the loop.

Sixteen lectures — are not a list of topics. They are sixteen angled views of **one and the same** task. Now let's bring them together onto a single plane.

---

## [s20 · 2 min] — The map, set 1: software, finance, medicine, aerospace

We plot the first four points — one from each family of the course.

**Software development** — the upper right corner. High applicability, high autonomy. Why? Code is text, the models are strong in it. The compiler gives an instant ground truth. The volume is enormous. The cost of an error is tiny. All the criteria converge.

**Finance and retail** — the upper middle. Applicability medium-to-high: fraud in the closed world — high, and iBuying in the open — low, Zillow showed that. Autonomy medium.

[pause]

**Medicine** — and here, attention. The **lower right** corner. Applicability from images is high. But autonomy is screwed down to L1 — and **not by technology, but by the regulator**. The FDA does not allow AI to make a diagnosis without a doctor. This is an ethical and legal decision, not a technological one.

**Aerospace** — the upper middle with a limited ceiling. Observation — high applicability. Action — limited by ethics and the regulator.

And already on four points the structure is visible: what borders IT — is upper right, regulated medicine — is lower right. The map starts to speak.

---

## [s21 · 2 min] — The map, set 2: CAD, creative, agriculture, manufacturing

We add the middle set. And here **dual** industries appear.

**CAD/CAM, engineering design** — the middle. The main lesson: "AI in design" — is **not one category**, but six different classes. Geometry optimization — high applicability. And an LLM assistant for writing scripts — accuracy of forty-five to sixty-three percent, below the industrial threshold. Marketing glues them together, and you — distinguish them.

**Creative** — the upper middle, dual. Mass assets — concept art, background music — high applicability. And a subscription author's work — a director's flagship film — low. And right there the risks: rights leakage, deepfake fraud.

[pause, circle the point's split]

**Agriculture** — and here is a vivid duality. The point **splits in two**. See & Spray — a narrow, delineated task, a closed loop — flies to the upper right. And **Monarch** — an autonomous tractor in the open field — falls to the upper left, into the failure zone. Thirty-eight percent layoffs in January twenty-five, about fifty-three people out of a hundred forty at the peak. The same industry — two opposite outcomes.

**Manufacturing** — middle-to-low. Also two physics: discrete versus process. Safety systems per regulations — at L0, vision on the conveyor — higher. And right there the pilot swamp: ninety-five percent of AI pilots never reach production. But more on that in the fourth section.

---

## [s22 · 2.5 min] — The map, set 3: robotaxi, logistics, cybersecurity, science, oil-and-gas

The final set. And the most telling case of duality — **logistics**.

[circle the three points]

Logistics — is **three** distinct points of a single industry, and each — in its own quadrant. The first — **warehouse robotics**: Symbotic, Amazon Sparrow. A controlled environment, the upper right corner, L4. The second — the **city robotaxi**: here, attention — the **upper left**, the warning zone. An open city environment, an attempt at high autonomy with low applicability. Waymo holds up only thanks to a tightly narrowed domain; Cruise tried to expand — and failed. The third — the **black swan**: Suez, the pandemic, a crisis. This — is the **lower left**, near the origin: effectively L0 — a task for people, not for AI. Note: the robotaxi and the black swan are both on the left, but for different reasons — one failed from ambition, the other was deliberately handed to the human.

[pause]

And here is what follows from this. **One and the same industry** holds three quadrants at once. Inside a single company — Amazon, FedEx — AI in the warehouse works almost autonomously, and when the chain breaks down everything rests on a human dispatcher. Maturity is **local to tasks**, not global to the company. This contradicts the intuition that "a company is either AI-mature or not."

[faster]

Three more telling points. **Science** — the closed world high, the open world low: AlphaFold versus Galactica, the same class of models, but the different anchoring to physics decides everything. **Cybersecurity** — high applicability on observation, but low on action: the blast radius keeps it lower right. And **oil and gas** gives the lesson of transfer: a "rock" chatbot on an LLM will not replace a geologist — the porosity and permeability of the rock the LLM simply does not know.

After the full display on the map — about twenty points.

---

## [s23 · 2 min] — The closed-loop cluster (upper right)

Now — a cluster analysis. Three key clusters. The two of us will start with the densest — the **upper right, the closed loop**.

Who is here? The engineer-agent in software development. Fraud detection — Stripe Radar. See & Spray in agriculture. Warehouse robotics — Symbotic. Protein folding — AlphaFold.

[pause]

Memorize the **five common features** of this cluster — this is the profile of a successful AI application. One — the environment is controlled or closed. Two — the ground truth is fast and unambiguous: the compiler, a chargeback, visual labeling, a lab analysis. Three — the volume of tasks is large. Four — the cost of an error is low or absorbable. Five — the training data matches operation.

That right there — is the working cases. Here AI pays off, here it is mature, here it is not marketing.

And here is why we need these five features. When you encounter a **new** industry, not from the course, and the tasks in it satisfy all five — the project has good odds. That is transfer of experience: not to memorize the companies by heart, but to recognize the **profile**.

---

## [s24 · 2 min] — The open-environment cluster (upper left, the warning zone)

The second cluster — the **upper left**. The warning zone. The cluster of failures: low applicability with an attempt at high autonomy.

Who is here? Monarch — the tractor in the open field. Plenty — vertical farms that raised more than nine hundred forty million dollars and collapsed into bankruptcy in March twenty-five. The city robotaxi Cruise. The black swan of Suez. The iBuying of Zillow. Galactica with open hypothesis generation.

[pause]

What do they have in common? The environment is open, there is resistance — weather, competition, politics, biology. The data does not cover rare events. The cost of an error is high — a pedestrian's life, a company's bankruptcy, disinformation in science. The ground truth is slow or absent.

[slowly, with emphasis]

And here is the main idea; it is important that we take it in. **An open environment is not a shortcoming of the technology. It is the physics of the task.** No model of twenty twenty-six will close this gap. And the expected model of twenty-eight will not close it either. Because the problem is not in the model, but in the **data distribution**.

What to do if your task lands here? Three options. Narrow the domain — Cruise's path to Waymo. Move to advisory L1 with a human in the loop. Or decline AI and take the classics.

---

## [s25 · 2 min] — The high-stakes cluster (lower right, the regulator's ceiling)

The third cluster — the **lower right**. High stakes. High applicability, but autonomy screwed down by the regulator.

Who is here? Medicine — clinical decisions at L1 by FDA mandate. Aerospace — action limited by regulation. Safety systems in manufacturing — by regulations. Action in cybersecurity — by the discipline of the blast radius. Explosion-hazard zones in oil and gas — by equipment certification.

[pause]

What do they have in common? Applicability may be high, but the regulator limits it. The cost of an error is high. Explainability is mandatory. Audit is mandatory.

And here is the key lesson. In these domains autonomy is **not the goal**. The goal is **augmentation**, not replacement. A radiologist with an AI assistant is better than a radiologist without — but the radiologist always decides. A pilot with AI awareness is better than a pilot without — but pulling the trigger is always the pilot's.

[straight to the room]

And this **does not mean AI is worse**. It means AI works in the role of an advisor — and this role is mature, measurable, paying off. Aidoc processes millions of images a year in "human in the loop" mode — that is a success, not a failure. By the way, augmentation often brings in more money than full automation — because full automation in high-stakes settings is almost never achieved, and the attempts fail. Remember IBM Watson Health? Sold for a billion, having accomplished not one of its stated goals.

---

## [s26 · 2 min] — The empty quadrants as a teaching tool

Let's look at the two off-diagonal quadrants. Their **asymmetry** is the key to reading the entire map.

[circle the upper left]

**The upper left — empty and dangerous.** Low applicability and, at the same time, high autonomy. Who tried to get in here? CrowdStrike — action at L4 for a system of medium applicability, an enormous radius. F-35 ALIS — predictive maintenance with high autonomy on a life-critical system. Cruise — high autonomy in an open environment, where applicability was not confirmed.

The lesson of this quadrant: if applicability is not high — **do not reach for high autonomy**. This is the asymmetry. Low applicability multiplied by high autonomy — is a catastrophe.

[circle the lower right]

**The lower right — on the contrary, is filled.** High applicability, low autonomy. Aidoc, Project Maven, scoring under the EU AI Act. This is **not emptiness, but a ceiling** — set by the regulator, not by technology.

[pause]

And here is a practice for you. Diagnose your project: am I landing in the upper left? If yes — what to change to shift out? Two paths. Shift **right** — raise applicability: close the environment, gather data, improve the ground truth. This is an investment in the **framing of the task**. Or shift **down** — lower the autonomy, add a human to the loop. This is an investment in the **design of the system**. Both paths are correct. Only one route is invalid — **staying in the upper left** while building up autonomy without growth in applicability.

---

## [s27 · 0.5 min] — Section 4 (section intro)

And now — the core of the lecture on boundaries.

**The course's twelve failures.** For each — what we learned and what the alternative is.

This is not gloating over other people's mistakes. This is an inoculation: you recognize the pattern in a project — you ask a question — and often that is enough to stop it.

---

## [s28 · 2.5 min] — Failures 1-4

Let the two of us systematize the course's failures into twelve canonical classes. The first four.

**Failure one — the open world without a closed loop.** Zillow, Monarch, Cruise. All three applied AI in an open environment. The distribution shifted — the model died. The lesson: distribution shift is **not cured** by adding data, it is cured by **changing the framing**. The alternative — narrow the domain or move into advisory mode.

**Failure two — accumulation of unreliability.** Remember the four-thousand-two-hundred-dollar loop? An agent with no budget cap looped over the night. Here it is pure math: if each step succeeds with a probability of ninety-five percent, then over ten steps the end-to-end success is fifty-nine percent. Over twenty — thirty-six. The lesson: this is an **architectural** limitation of multi-step agents. The alternative — a budget cap, a step limit, a human controller every few steps.

[pause]

**Failure three — a demo does not equal production.** Devin, IBM Watson, Epic Sepsis, Klarna. The vendor shows a demo — production shows something else. Epic promised an accuracy of zero point seven six, in operation — zero point six three. The lesson: the vendor's benchmark is measured on their data, in their environment. The alternative — **recheck on your own data** before committing. If they refuse to give it — that is a strong signal.

**Failure four — the bored human in the loop.** Uber in Tempe, F-35 ALIS. A human set to watch for rare events is psychologically incapable of doing it for hours. The alternative — a human **on** the loop woken by an alarm, not **in** the loop at each step.

---

## [s29 · 2.5 min] — Failures 5-8

The next four.

**Failure five — over-automation.** Remember Tesla during the production ramp in eighteen? Musk admitted: excessive automation slows the conveyor. The tweet "humans are underrated" — April eighteen. This is the automation paradox, described back by Bainbridge in eighty-three: automation is good in zones of low variability and breaks in zones of high. The alternative — Toyota's jidoka principle: augmentation, not replacement.

**Failure six — acting without a canary and a rollback.** CrowdStrike, Cloudflare. A broad domain means a large radius. The lesson: action with a large radius **must** have a canary release to one to five percent, telemetry with early warning, a one-click rollback, and a staged rollout. CrowdStrike had none of the four.

[pause]

**Failure seven — a scientific hallucination of the Galactica class.** Fake papers, fake references. The lesson: in science the ground truth is an experiment, not text. The alternative — anchoring to verified sources and human review with a checklist for every reference.

[lower your voice]

**Failure eight — fraud via voice and video.** Remember the deepfake in Hong Kong, February twenty-four? An employee of the engineering company Arup transferred **twenty-five million dollars** after a video conference where both the CFO and the colleagues were deepfakes. This is already a **multimodal** attack — video plus voice. The lesson: for large transfers — a mandatory verification through an **independent channel**. Call back on a verified phone number, not on the same channel the request came from.

---

## [s30 · 2.5 min] — Failures 9-12

The last four. And note: the first eight failures were about **action** — about how AI does something wrong. These four — are about **data and money**: about what you risk even before AI began to act.

**Failure nine — training data leaking verbatim.** Getty versus Stability, NYT versus OpenAI. Large models have a "memorization tail": part of the training examples is stored verbatim in the weights and is extracted by the right prompt. This is a legal risk for you as a user too. The alternative — licensed datasets, provenance audit.

**Failure ten — vendor lock-in in regulated industries.** Climate FieldView, F-35 ALIS, Watson Health. The vendor cloud gets your sensitive data — and exiting costs millions. The alternative — your own infrastructure, data-export clauses in the contract, a multi-vendor strategy.

[pause]

**Failure eleven — slopsquatting.** This is a new vector that appeared **because of** AI. When generating code the models **invent** the names of nonexistent libraries — plausible ones. Attackers register these invented names and put malware there. You run the AI code — you import the malware. The alternative — a software composition check, a whitelist of imports, verifying the library exists before committing.

[slowly]

**Failure twelve — the pilot swamp.** And here it is important to distinguish the numbers: marketing glues them together. MIT NANDA and Sloan: **ninety-five percent** of GenAI pilots never reach production. McKinsey: only **five and a half percent** of companies are high performers with an effect on profit. These are **different measurements**: MIT measures pilot failure, McKinsey — the concentration of leaders. In Russia — nine out of ten pilots do not make it. The alternative — explicit "go further or shut down" points, a baseline before the start, a budget cap.

---

## [s31 · 2.5 min] — Synthesis: three mega-patterns

[slowly, this is the section's climax]

Twelve failures. And now — the main thing, and it is important that we take it away. Almost all of them reduce to **three mega-patterns**. If you remember only three things from this section — let them be these.

**Mega-pattern one — AI applied beyond the boundary of the closed loop.** Zillow, Monarch, Cruise, Galactica. Full automation where feedback is slow, the ground truth is ambiguous, the environment is open. The check in one phrase: **"What is the environment — closed or open?"** Open — stop.

**Mega-pattern two — the human in the loop is poorly designed.** Uber, F-35, CrowdStrike. The human was formally present, but in fact did not work: boring monitoring, no canary, no rollback. The check: **"Who is this human, what are they busy with, how many times an hour do they look? Aren't they bored?"**

**Mega-pattern three — the economic baseline was ignored.** Demo failures, the pilot swamp, vendor lock-in. They did not measure the classical alternative before the start. The check: **"What is the baseline? How much does the classics give? Will AI pay off the delta?"**

[pause]

These three questions — are a **thirty-second procedure**, and the two of us will find it useful on any AI proposal. And you know what? Most of the catastrophes in the registry could have been prevented at the planning stage, had the engineer asked these three questions.

And the main thing — these patterns **transfer across industries**. When you land in a new industry, not from the course, they will show up there too. Recognize them — and you save the company millions.

---

## [s32 · 1.5 min] — What you take away: four cards

And finally — what you take away with you physically.

Sixteen lectures were an intensive immersion. After the exam the details will be forgotten — which company, which year, which percentages. That is normal. **What must not be forgotten** — is the diagnostic tools.

And so that they are not forgotten, the two of us packed them into **four reference cards** — compact printed documents that you take with you.

[gesture to the screen / to the printouts]

Card number one — the **matrix of seven criteria**. Card number two — the **ladder of autonomy**. Card number three — the **registry of twelve failures**, the main one by practical value. And card number four — the **map of sixteen industries**, a large poster on the wall. By the way, it is already hanging here in the lecture hall.

Why cards? Atul Gawande in "The Checklist Manifesto" showed: in aviation and surgery checklists sharply reduce the number of errors. Under stress — under the pressure of a vendor presentation — we forget to check something important. A card is external memory. Let's go through them.

---

## [s33 · 2 min] — Card #1: the decision matrix

**Card number one — the "Should we apply AI" matrix.** Seven rows, four columns.

Each row is a criterion we have already worked through. Environment. Data. Repeatability. Cost of an error. Ground truth. Explainability. Economics versus the classics. In each row is an indicator: a checkmark if AI fits; a warning triangle if a human in the loop is needed; a cross if it does not fit. And an example from the course.

[pause]

The rule of application is simple. You go through the seven rows **in order**. At least one cross — **stop, decline** full AI for this task. Two or more warnings — stop, justify a human in the loop plus a canary plus a rollback. All seven checkmarks — we go into a pilot, but with explicit "go further or shut down" points.

This is the **most common** tool you will apply. On any vendor presentation, any planning meeting of "let's implement AI" — go through the seven rows. In five to ten minutes you get a more structured assessment than most project managers.

And an excellent technique for a team: put the card up on the screen and go through the seven rows **together**. Instead of "seems like it'll work" — "on row two we have a warning, let's discuss the data." This reduces conformity and raises quality.

---

## [s34 · 1.5 min] — Card #2: the ladder of autonomy

**Card number two — the ladder of autonomy, from zero to five.** Six rows, five columns.

The level, the name, what AI does, who decides, and the criteria for climbing to the next rung. In the footer of the card — the anti-patterns: exceeding the role at L1, the bored human at L2, expanding the domain at L3, acting without a canary at L4, the ethical block at L5.

[pause]

The rule of application. For any AI application, determine **two** things: the current level and the **maximum permissible** one. If they differ — a climb plan is needed with explicit criteria. Most mature applications of twenty twenty-six are L1-L2. L3-L4 — for special domains: Waymo, See & Spray, warehouses. L5 — practically nowhere.

And remember: this card is a **living document**. It is a snapshot of twenty twenty-six. In five years the criteria for climbing may change — regulators, insurance markets, standardization. Take it with you and revisit it every two or three years.

---

## [s35 · 2 min] — Card #3: the registry of failures

**Card number three — twelve failures and antidotes.** The main card by practical value. Twelve rows, four columns.

The name of the failure, the source, the lesson in one phrase, the alternative. This is the very inoculation we assembled throughout the fourth section.

[pause]

The rule of application. When you read a vendor presentation, take part in a planning meeting, review a paper — go through the twelve rows. You recognize the pattern — you ask a clarifying question. Often that is enough to save a project.

Why exactly twelve? Psychologists have known since Miller's time: a human holds seven plus-or-minus two items in working memory. Twelve — is **beyond** working memory. That is why they are kept on **paper**, not in the head. Cut it to five — we lose patterns. Expand it to fifty — the card dissipates. Twelve — is a compromise.

And one more habit that I strongly recommend. After **each** of your AI projects, go through the twelve rows: which failures you avoided and why, which ones you nearly fell into and what you understood. This is a personal debrief. After several years of such practice you will distinguish patterns better than most colleagues.

---

## [s36 · 1.5 min] — Card #4: the master map

**Card number four — the map of sixteen industries.** A large poster, A1 format. The one hanging on the wall.

A scatter diagram: horizontal — applicability, vertical — autonomy. Color zones of the quadrants. Green — the closed loop, the working cases. Red — the warning zone. Gray — the classics win. Blue — high applicability with the regulator's ceiling.

[pause]

The rule of application — literal. **Hang the poster on the wall.** When you discuss a new project, ask your colleagues to **point a finger** at which quadrant the task is in. This exercise alone puts the project into a structured frame.

And for a new industry that was not in the course, the poster gives **analogies**. "This task resembles See & Spray by the structure of its closed loop." Or "this one resembles Cruise's expansion — the domain is not narrow enough." Transfer of experience through analogy is the poster's main function.

And remember: the map is updated. Waymo may move from a narrow domain into a broad one. The points shift. But the **axes** — applicability and autonomy — are stable.

---

## [s37 · 3 min] — The main takeaway + questions and answers + farewell

[slowly, this is the finale of the course]

The main takeaway of the whole course. One phrase.

> **To know AI is to know its boundaries.**

[pause 2 sec]

At the start of the course this sounded like a slogan. Now — it is an engineering discipline that the two of us built. Seven criteria. Six rungs of autonomy. Twelve failure patterns. Two axes of the map.

A non-engineer reaches for the tool without understanding its boundaries. An engineer **first** checks the boundaries, **then** takes the tool. A simple sequence — but in the era of hype, a scarce one.

[straight to the room]

You leave this course with three things. First — **knowledge of sixteen industries**: what works, what failed, and why. Second — **diagnostic tools**: the map, the criteria, the ladder, the failures, the four cards. And third — a **professional stance**: you are not an "AI engineer" in the marketing sense, and not a "prompt engineer." You are an engineer who knows when to apply AI and when not to. These three things will not go stale when the models of twenty twenty-six go stale.

[pause]

And there is an anchor that I want to leave you with separately. The course's eight canonical cases — memorize them by name: Zillow, Watson, CrowdStrike, Galactica, Klarna, Plenty, Cruise, Uber. When a new CrowdStrike happens — and it will happen — you will remember and not repeat it.

[pause]

That is the essence of the course. Thank you for these seventeen lectures. Good luck in your work.

Questions — let's have them.

[Closing pause]

**Until next time.**

---

## [Reserve · 5 min] — Questions and answers + backup options

- **If the demo/projector does not work on s02 (keystone)** — I draw both axes and the four quadrants in chalk on the board within a minute; that is the best insurance, the map is deliberately simple.
- **If the question is "And when will AI reach L5 / general intelligence?"** — we answer: L5 in the course is a theoretical horizon, not a goal. Five structural blocks (insurance, the regulator, out-of-distribution events, liability, economics) keep most tasks at L1-L4 deliberately. This is not "we haven't gotten there yet," this is "we should not strive for it."
- **If the question is "Are you against AI in general?"** — we answer: no. The course showed mature, paying-off applications — Copilot, Stripe Radar, See & Spray, Aidoc, Symbotic, AlphaFold. They are real and valuable. The skill of saying "no" feeds from the same knowledge as the skill of saying "yes."
- **If the question is "How do I start a career with this skill?"** — we answer broadly: not "catch up with AI," but specialize where AI works poorly; position yourself as "an engineer with AI expertise," not as an "AI engineer"; read one or two failure analyses a month. Regulated industries hire AI-aware engineers into stable roles.
- **If the question is about a specific university / job placement / industry** — we answer broadly: "specialized technical universities lay down the diagnostic skill at the undergraduate level; beyond that — professional communities and certifications." Without tying it to specific institutions.
- **If time remains** — we cover the ten classes of career anti-patterns from §5.5 (overrating prompt engineering as a permanent role, lock-in to a single model, silence in planning meetings, the pilot swamp in one's own career) or the backup questions from chapter-part4 Appendix B (8 questions).
