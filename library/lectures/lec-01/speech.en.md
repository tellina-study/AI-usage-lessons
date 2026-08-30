---
lecture: 1
title: "Lecture 1. What is AI? History, classification, general concepts"
length_min: 75
length_words: ~6800
status: draft
version: v3.4
slides_covered: [s01, s00a, s00b, s02, s02a, s05a, s05c, s06, s06a, s07, s07a, s08, s09, s10, s11, s12, s13, s15, s16, s17, s18, s19, s19a, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s29a, s30, s31]
source: chapter v3.3 + deck v3.4 (36 slides, issue #153 21-fix polish + issue #155 batch 1, 10-fix polish + 2 new section dividers)
---

# Lecturer's Speech · Lecture 1 v3.4

**Duration:** 75 minutes.
**Version:** v3.4 (issue #155— Round 2 polish, cross-artifact sync after batch 1 fixes + section-divider audit).
**Sources for me:** chapter v3.3 (17350 words, source of truth) + deck v3.4 (36 slides).

---

## Changelog v3.3 → v3.4

Cross-artifact sync with deck v3.4 after issue #155 Round 2 batch 1 (10 copy fixes + section-divider audit #177). 15 targeted edits + 2 new sections (36 slides instead of 34).

- **** Added section **[s05c]**— new section divider "Section 1— What is AI" before the start of the first content section. Previously section 1 started without an explicit divider right after the lecturer's bio card.
- **** Added section **[s07a]**— new section divider "Section 2— Where we are now" before the section on the scale of AI and the breakthroughs. Now all 5 content sections of the lecture open with an explicit divider carrying the bridge phrase "Section N of five"— previously dividers appeared only before sections 3/4/5.
- **[s02]** The lecture title in the line was synced with the slide rename (#171): "Introduction— AI around us" → "What is AI? History, classification, general concepts".
- **[s02a]** Section title "Lecture map" → "Lecture plan" (#173); mention of block 0 "opening" → "introduction" (#172).
- **[s05a]** The lecturer's line was fully rewritten for the new bio card (#174): real name and role ("architect, technical and product leader"), 20+ years in IT, 10+ projects, real companies (Yandex, MTS, Magnit, Sibur), Telegram/Email contacts. The old duh-style "who I am and why this matters to me" with the abstract "1 phrase about the role" placeholder was removed.
- **[s07]** Added an optional reference to the new visual caption on the "Winters and breakthroughs" panel— "resources leave when promises don't come true"— right before the formulation of the methodological lesson about AI winters (#176). Structure and facts unchanged; there were no spoken references to the outdated layout (single line).
- **[s12]** The classification matrix was reconciled with the new 5×4 structure (#179-181): "six types" and "planning" removed from the X-axis wording (now five types, no planning); "code" removed from the Y-axis (modality now has no separate "code" row). Added a new paragraph about the Forecasting×Text cell = "GPT-4o, Claude"— text generation by modern LLMs is technically next-token prediction.
- **[s13]** Reconciled— purely visual edits (#182-184, axis label size), there were no spoken references to the old details, no edits required.
- **[s18]** Reconciled— the line did not describe the geometry of the USER circle, there were no references to the outdated layout, no edits required.
- **[s19a]** The line was synced with the new order of the right column (#193): it was in-the-loop→on-the-loop→out-of-the-loop→override top to bottom, now it is out-of-the-loop→on-the-loop→in-the-loop→override (mirroring the descent of autonomy on the staircase on the left). The wording of the left-hand staircase was brought to an explicit "User:..." (#192).
- **[s22]** The line was rewritten as connected text without announcing "now I'll show three reason cards" (the cards were removed from the slide)— the three thoughts (responsibility / systematic nature of errors / the "cannot do" boundary) remain, but are spoken as a single paragraph, in sync with the slide's new speaker notes.
- **[s23]** "Enterprise and API" → "Corporate tiers and API" (#194, russification of the column heading on the slide).
- **[s24]** Section title simplified: "Hallucinations: AI confidently generates nonexistent DOIs" → "Hallucinations— an inherent property of AI" (#195).
- **[s26]** Reconciled— the spoken conclusion "not one speaker holds a neutral position" was already spoken and remains the sole place of this conclusion after the removal of the closing callout from the slide (#196); no edits required.
- **[s29]** Reconciled— the line did not contain the mention "(30 hours, incl. preparation)" that was removed from the slide (#197); no edits required.
- **[s29a]** Section title synced with the new slide title "Semester grade" (#198); the line now begins with this title as spoken text.
- **[s31]** Removed the reference to a no-longer-existing contact placeholder (#199); added an explicit reference "my contacts were on the bio card slide at the start of the lecture" (contacts are now only on s05a).
- **** On recount after the edits, 5 fragments >95 WPM were found (s05a 194→80, s07a 126→88, s12 113→92, s19a 119→79, s22 129→83 words/min)— all tightened without loss of content, no fragment exceeds 95 WPM.
- **** Active speech 60.5 → 61.5 min (+1.0 from the 2 new 0.5-min dividers s05c/s07a). Buffer 14.5 → 13.5 min. Total of 75 min preserved. Section 1 "What is AI" 6.5→7.0 min, section 2 "Where we are now" 6→6.5 min (sync with deck.yaml pacing).

---

## Changelog v3.2 → v3.3

Polish Round Pattern— full resync of speech.md with the finalized chapter.md v3.3 and deck.yaml/slides v3.3 after the 21-fix polish round (issue #153). Not point edits— the whole file was reassembled to match the new order and content of the slides.

- **** Removed sections [s03] and [s04] (icebreaker poll about AI use in Russia)— the poll moved to seminar 1 and no longer appears in the lecture.
- **** Removed section [s05b] in its old form ("Main question of the course" as a separate slide after the bio card)— the content moved to the new s00b, which now comes **before** the title slide (s02).
- **** Added section **[s00a]**— a short welcome before the title: what the course is, what it is about, what it is not.
- **** Added section **[s00b]**— the course hook: the adoption funnel 100%→10% + the course's main question "not can you, but should you and where". This is now the first substantive statement of the lecture, before the title.
- **** Added section **[s06a]**— the prehistory of 1943 (McCulloch— Pitts), a fact-bridge between "what is AI" (s06) and the seventy-year timeline (s07): the idea of a neural network is 13 years older than the term "AI" itself.
- **** Added section **[s29a]**— the grade formula (100 = 10 attendance + 30 exam + 3×20 midterms), right after the semester map.
- **[s02a]** Rewritten for the new visual— a timeline-roadmap (the same pattern as the semester map s29), rather than section cards jumbled together.
- **[s08]** The market figure was updated: "$244–390B" → "390.9 billion dollars in 2025 → 539.5 billion in 2026 (Grand View Research)", with a footnote about Statista's narrower software-only estimate.
- **[s09]** The fourth episode was fully rewritten: Kimi K2.5 → Georgi Gerganov / llama.cpp / ggml.ai (solo project → joining Hugging Face on February 20, 2026 → 100,000+ stars on GitHub in March 2026, faster than PyTorch and TensorFlow). The lesson is about the infrastructure layer, not about a product. The flat lecture numbers "lectures four, five, eight" were replaced with a topic-based phrasing.
- **** Reconciled against outdated visual details (removed gold highlight on YOLO, labels under the quadrant points)— there were no spoken mentions of these details in the speech, no edits required.
- **** Added mentions of the eyebrow headings in sync with the new visual; the phrase "Not magic" at the very end of s16 was removed (replaced by a neutral ending); "Returning to..." was removed from s17.
- **[s18]** Fully rewritten for the new schema: linear ReAct pipeline Plan → Action → Observation → Reflection with an explicit gold loop-back arrow "continue" and a branch "stop → result to user" (instead of the old hub-and-spoke schema). Added Lilian Weng's formula and the canonical products.
- **[s19a]** The autonomy-level names were russified with an English gloss in parentheses: Operator (Operator) → Collaborator (Collaborator) → Consultant (Consultant) → Approver (Approver) → Observer (Observer).
- **[s23]** Added a spoken transition-bridge from the divider "Section 4 · Boundaries of AI" to the topic of data— previously the slide started "from nowhere" right after the divider.
- **[s25]** The russification of the timeline (rollback / social network / root-cause analysis) was reconciled— it was already correct in Russian.
- **[s26]** Updated the Hassabis line: "AGI by 2029–2030 (3–4 years); the window narrowed over 2026" (Axios/Google I/O, May 2026).
- **[s28]** Removed the homework for seminar 1— it is now entirely in the seminar, not in the lecture. The section was shortened to three takeaways.
- **[s29]** Fully rewritten for the new 4-block structure: "17 lectures, 3 modules + exam" (not "17 lectures × 3 modules"). Module 1 (1.1–1.6), Module 2 (2.1–2.5), Module 3 (3.1–3.6), with the Exam as a separate block (not "Module 4").
- **[s31]** Section title renamed "Q&A" → "Questions?".
- **** Active speech 62.5 → 60.5 min (recomputed from the sum of duration_min of all 34 slides in deck.yaml v3.3). Buffer 12.5 → 14.5 min. Total of 75 min preserved.

---

## Changelog v3.1 → v3.2

Point synchronization of speech blocks with the updated slides v3.2 (33 slides, +1 from the split of s19). 9 fixes + 1 new block (s19a), without rewriting the other 23 blocks.

- **** [s07]— removed the repeat of "AI Effect" (it stays in [s06]). Expanded the fragment on Vaswani-2017: 8 co-authors by name, self-attention replaced RNN/LSTM, as of May 2026— more than 160 thousand citations in Google Scholar.
- **** [s09]— the 4 episodes were rewritten for the new layout of slide v3.2: Mistral 7B → DeepSeek R1 → OpenClaw → Kimi K2.5. Llama-3 and MCP removed. Added: OpenClaw (P. Steinberger, November 2025, >100K★ in a quarter, February 14, 2026— move to OpenAI and a non-profit foundation) and Kimi K2.5 (Moonshot AI, January 2026, swarm mode with 100 sub-agents).
- **** [s16]— rewritten for the new visual: dialog cycle (USER ↔ Message ↔ LLM ↔ Response ↔ USER + system prompt on top + ⋮ at the bottom), rather than a 6-step linear flow. The same tone: "we remove the magic", two consequences— the lever of the system prompt and the limitation of the context window.
- **** [s17]— added a production disclaimer: "pure chats are almost never used in production— everywhere there are agents with RAG for long-term memory and search over the corporate knowledge base; the boundary 'chat vs agent' is blurred on the production side".
- **** [s19] split— now 2 blocks. [s19] = "Agent at work: 200 PDFs"— 7 numbered steps with an explicit tool at each (file system / PDF reader / extraction / vector DB / search+LLM / Sheets API / orchestrator loop). NEW [s19a] = "Levels of autonomy + Human-in/on/out-of-the-loop"— 5 levels of Feng/McDonald/Zhang 2025 in parallel with 4 frames for including the human in the loop. Total time for the 2 slides— 3 min (was 2.5).
- **** [s21]— updated the description of the visual for the new layout: Q1 on the left scale (vertically), Q2 on the bottom scale (horizontally)— as axis markers of the quadrant, not as cards on top. Worked examples preserved.
- **** [s28]— the assignment was simplified: the phrase "defense before the group" was removed, leaving "bring → run through the 2-question quadrant → a one-page analysis in any format".
- **** [s29]— updated the spoken description of the modules for the new structure of chapter §5.2: M1 = lectures 1-5+7 (6 lectures: introduction / architecture / agents+RAG / software / finance and retail / medicine); M2 = lectures 6, 9-12 (5 lectures: engineering design / aerospace / agriculture / manufacturing / digital twins); M3 = lectures 8, 13-17 (6 lectures: creative / logistics / telecom+cybersecurity / science / oil-and-gas / synthesis). Midterm 1 on S8, midterm 2 on S12, midterm 3 on S17.
- **** [s30]— removed the callback to YOLO/s01 ("the camera in s01 recognized in 30 ms— we'll break down how in lecture 2"). What remains is clean: 4 concepts + a 1-phrase frame.
- **** Active speech 62.0 → 62.5 min (+0.5 from the s19 split). Buffer 13 → 12.5 min. Total of 75 min preserved.

---

## Changelog v3 → v3.1

Targeted revision based on the 3-critic synthesis (methodology + fact-checker + consistency). 1 P0 + 6 P1 edits (~20 minutes).

- **** Removed the orphan pre-flight "" (s26 is now = "AGI forecasts: 4 speakers, 4 material interests", the ARC-AGI slide was removed in v3.1). Replaced with a pre-flight for the current AGI quotes.
- **** "Robot application" → "Application in automation mode" (sync chapter §3.6/§3.7 + s21 speaker notes + speech [s21]).
- **** Added bridge phrases "Section N of 5" in (continuous carry-over from the lecture map s02a).
- **** deck.yaml s13 axis labels updated (X=Delegation from the user, Y=Developer's control— sync with Fix-16).
- **** s09 Mistral founders "Meta and DeepMind" → "Meta and Google DeepMind" (to avoid confusion with pre-2014 DeepMind).
- **** Pearl reference removed from s28 speaker notes (orphan reference: the Pearl slide was removed, it is absent from the speech).
- **** s09 Llama-3 MMLU without rounding: "seventy-nine and a half versus sixty-eight point nine" (was "sixty-nine").
- **** s17 "Le Chat" → "Mistral Le Chat" (with the brand prefix for consistency with the chapter and notes).

---

## Changelog v2 → v3

Full rewrite for the structure of deck v3.1 after 23 edits by the user at USER GATE 3.

- **Structure.** 32 blocks instead of 30. New: s02a lecture map, s09 4 breakthroughs, s10 divider of section 3, s12 classifier "task × modality", s13 control quadrant (new axis orientation), s15 model + pipeline, s16 chat cycle 6 steps, s18 agent architecture, s27 divider of section 5, s28 summary + homework. Removed: the old s14 mini-divider (Fix-17), the old s15 RTC pattern, the old s28 takeaways.
- **Quadrant orientation.** s13— new orientation: X = delegation from the user, Y = developer's control. Agent in the top-right corner (gold). Model— in the bottom-left.
- **s06 rewritten.** Not "two definitions", but "there are many definitions— because AI is a moving target". Tesler via the AI Effect.
- **s09 new.** 4 breakthroughs (Mistral / Llama-3 / DeepSeek / MCP) with the motivating tone "don't despair, breakthroughs are made by different teams", without sacred knowledge.
- **s20 without Copilot.** Unambiguous applications: Translate / Notion AI / YandexGPT / Grammarly / Yandex Maps / Adobe Firefly.
- **s21— 2 questions + quadrant.** Not 4 questions + matrix. The top-right quadrant is called "Application (automation)", not "Robot application".
- **s25 Russian names.** Bias, sycophancy, drift (with the English in parentheses).
- **s26 table 4×4.** Speaker | Affiliation | AGI forecast | Material interest— without journalistic prose.
- **s28 new.** Summary + seminar assignment replaced the old s28-takeaways.
- **s29 real roadmap.** 17 lectures × 3 modules, synced with the Drive doc. Not "4 blocks".
- **s30 teaser in Russian.** Tokens / embeddings / attention mechanism / temperature.
- **Tone.** 0 "you'll make it into the 10%", "secrets", "across the whole zoo", "magic solution". Diagnosis, not a magic pill. "You and I" ≥ 12 instances.
- **Anglicisms.** 0 "stakes", "fallback", "overrun", "onboarding", "insight", "use case", "edge case", "collaboration", "misalignment". Kept: AI, LLM, RAG, MCP, API, RLHF, ML, CV, NLP, transformer, attention, embedding, fine-tuning, prompt, chat, agent (with expansion on first mention).

---

## Preparation before the lecture

- Turn on the laptop and projector **15 minutes before the start**. Check that the HDMI holds the connection, and that the projector resolution matches what is expected.
- Run `library/lectures/lec-01/assets/code/ice-breaker-cv/run.py` once as a test— make sure the camera sees the room, that bounding boxes are drawn, and that the "N people detected" counter updates.
- Open the **backup screenshot** of s01 in a separate tab: `library/lectures/lec-01/assets/code/ice-breaker-cv/backup/screenshot.png`. If the live demo fails— switch via Alt+Tab in two seconds.
- Open the **demo for s13** (three ways of solving one task): three windows— a browser with Claude web (the model via a web chat), a terminal with Claude Code (the agent), and a terminal with a curl request to the API (the model directly). Test task— extract fields from a training PDF contract. Backup— three screenshots in `assets/code/three-ways/backup/`.
- Check the internet (for Claude web in s13). If there's no internet— go straight to the video backup, don't panic.
- **** The day before the lecture— run a fresh hallucination test: ask ChatGPT and Claude to name three 2024–2025 articles with a DOI on a narrow topic ("seismic resistance of small-diameter underground pipelines"). Record the three invented DOIs. If today both chats give only real links— switch to the backup story "how we caught a hallucination in GPT-4 on a corporate case".
- **** Open fresh AI news (June–August 2026) and check whether new public statements by Altman / Amodei / Hassabis / LeCun about AGI timing have appeared. If so— replace the spoken quote with a current one, keeping the structure of the "speaker— affiliation— forecast— material interest" table.
- Checklist on paper: a slide-by-slide schedule with timestamps. A clock in front of you, don't depend on the clock in the room.

---

## [s01]— Real-time identification of people

[I turn on the laptop, the projector shows a live frame from the webcam. On the faces in the room— bounding boxes. The "N people detected" counter updates.]

"Hello. Before I say a single word about AI— look at the projector.

What you see is a laptop. An ordinary laptop. Running on it is a computer vision model. It was trained in twenty twenty-three. It sees you for the first time— there are none of your photos in its training set. And it runs locally. No internet. No cloud. No subscription. No sending data to anyone whatsoever.

This is AI. Not magic, not a threat, not "the future that will arrive"— but a tool that works right now, on a single laptop, in this room.

This is **narrow AI**. The model solves one task: find people in the frame. Nothing more. It doesn't understand who you are. It doesn't know your names. It draws no conclusions. Just detection of objects of the class "person".

[Backup line, if the demo failed: "The projector had bad luck today— but here's a screenshot of the same demo, run yesterday. See the two rectangles on the faces? That's the result: a model in real time, on a CPU, without the cloud, thirty frames per second."]

Today, over seventy-five minutes, you and I will walk through the main archetypes of AI tools. Not so that you memorize the names— for something else. So that you learn to **tell apart**: where AI works, where it doesn't work, and **how to figure that out in advance**, before you've invested three months of development in it."

---

## [s00a]— Welcome

"A couple of words about the course. This is the course "Industry Applications of Artificial Intelligence Systems"— about AI in real industries: from software development and finance to aerospace and medicine.

The course is not about training models from scratch. It is about how to competently choose and deploy ready-made AI solutions. Today— the first lecture, the introduction."

---

## [s00b]— The main question of the course

"The question "can AI be applied" is no longer interesting. It can. Nine hundred million people use ChatGPT every week. It has long been infrastructure.

But the question "should you and where" is open. Look at the funnel on the left: about ninety percent of corporate AI pilots in Russia do not reach production deployment. Similar figures— on other markets too, per McKinsey and Gartner.

Mass adoption and mass failure at the same time— the central engineering problem of the course. That is why the main question is not "can you", but **"where AI works, where it doesn't, and how to figure that out in advance"**. This is a diagnostic question, not a triumphant one. You and I will return to it every lecture of the course."

---

## [s02]— Cover

"Lecture one. What is AI? History, classification, general concepts.

This is the first of seventeen lectures of the course. Today— the general map. Later we'll descend into the details."

---

## [s02a]— Lecture plan

[On the slide— a horizontal timeline of 5 color blocks, the same visual pattern as the semester map s29; the current section (0) is highlighted in gold.]

"Briefly— the navigation. Five sections. Right now— the introduction. Next: what is AI; where we are now; four ways to implement— the largest section; and the boundaries of AI."

---

## [s05a]— Who I am and why this matters to me

"Briefly about myself.

I am an architect, a technical and product leader in IT— more than twenty years, more than ten completed projects.

I've worked with Yandex (leading Russian internet/search-and-services company), MTS (major Russian telecom operator), Magnit (large Russian grocery-retail chain), Sibur (largest Russian petrochemicals producer). Different industries, and in each, AI was applied in its own way. That is why I'm interested not in a conversation about "artificial intelligence in general", but in the engineering boundary: where AI saves time, and where it's a demonstration that falls apart in production.

This course is the map I didn't have at the start of my path. Boundaries will get as much attention as successful cases.

Questions outside the lecture— the contacts are on the slide."

---

## [s05c]— Section 1. What is AI

[On the slide— a divider: a large "Section 1", the title "What is AI", the 1-phrase frame "Definitions, history, classification", a roadmap bar at the bottom with the current section highlighted in gold.]

"We've introduced ourselves and stated the main question of the course. This is the first section of five— what is AI.

The structure of the section is short but dense: first— why there are many definitions of AI, then a fact-bridge from nineteen forty-three, and at the end— a condensed seventy-year timeline with a clear turning point."

---

## [s06]— What is AI: why there are many definitions

"AI has no single canonical definition. This reflects the nature of the subject: AI is a moving target. You and I keep four approaches in mind.

Russell and Norvig: four quadrants "thinking / acting" × "human / rationality". An academic frame.

The ISO/IEC 22989 standard: AI is a system that generates content, forecasts, recommendations, decisions for goals set by a human. Regulators use it.

Through learning: a program improves through experience. If the behavior is a set of rules, it's not AI; if it comes from a trained model, it's AI.

Through benchmarks: something can do a task at a human level. Here is where the discussion about AGI and Searle's Chinese Room objection lives.

The main point— why the definition shifts. Larry Tesler: "AI is whatever hasn't been done yet". Face recognition, navigation, a spam filter— at the moment they appeared, they were AI; now they are "a feature of an application". This is the **AI Effect**.

Don't pick one approach as the right one— all four are working."

---

## [s06a]— Prehistory: 1943

"Before we walk through the history of AI— one fact-bridge.

Even before the term "artificial intelligence" appeared, the neurophysiologist Warren McCulloch and the logician Walter Pitts formalized the neuron as a logical element: a network of such simple binary elements can theoretically compute any logical function. The paper came out in nineteen forty-three.

That is thirteen years earlier than the Dartmouth conference of fifty-six, where the term "artificial intelligence" would appear for the first time.

The formal neuron didn't solve applied tasks, but it anticipated the connectionist tradition— a line of thought from which neural networks and architectures like the Transformer would grow.

Keep this in mind: the idea of a neural network is older than the term "artificial intelligence". Next— the history from fifty-six on."

---

## [s07]— Seventy years of AI: discoveries, winters, the 2017 turning point

"A condensed timeline in three groups— seventy years, counting from fifty-six, when the term itself appeared.

**Discoveries and first practice, the fifties— eighties.** Fifty— Turing publishes the "Imitation Game". Fifty-six— the Dartmouth conference, McCarthy, Minsky, Rochester and Shannon introduce the term "artificial intelligence". Sixty-six— Weizenbaum creates ELIZA, a psychotherapist program: users ascribe to it an understanding that isn't there— the "ELIZA effect". The eighties— the commercial boom of expert systems: XCON, MYCIN, Dendral; Japan launches the "Fifth Generation".

**Two winters and breakthroughs, seventy-four— twenty twelve.** Seventy-four— eighty— the first AI winter: after the Lighthill report and the DARPA cuts, the field loses money. Eighty-seven— ninety-three— the second winter: the market for AI machines collapses, expert systems turn out to be brittle. Ninety-seven— IBM's Deep Blue defeats Kasparov: two hundred million positions per second by brute-force search. Twenty twelve— AlexNet wins ImageNet by a sharp margin: deep convolutional networks on GPUs beat hand-crafted features.

Note the caption under this panel: resources leave when promises don't come true. That's exactly how both winters worked— not because of a lack of ideas, but because of the gap between what was promised and what actually worked. The lesson: when promises massively fail to come true, the field loses resources. Today's wave is the fourth, and so far it avoids a winter, because part of the promises do come true. But not all of them will. Distinguish what works now from what is promised for twenty thirty.

**The turning point, twenty seventeen— twenty-six.** Everything we use today grew out of here.

In June of seventeen, eight authors from Google Brain and Google Research publish "Attention Is All You Need": Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin.

Before seventeen, the main architecture for sequences was recurrent networks— RNN and LSTM: tokens are processed one at a time, they parallelize poorly on GPUs, and they remember long context poorly. Vaswani and co-authors proposed the **self-attention mechanism** and the **Transformer** architecture with no recurrence at all— it replaced RNN and LSTM as the main building block.

As of May twenty-six, the paper has more than **one hundred sixty thousand citations** on Google Scholar. An influential work accumulates thousands over a lifetime; one hundred sixty thousand in eight years is a rarity even for a Nobel-level one.

Why seventeen exactly became the turning point. Three properties coincided: parallel trainability on large corpora; good scaling— more data and parameters, higher quality, nonlinearly (scaling laws); and universality— one design works with text, images, audio, biological sequences.

By the year twenty, GPT-3 appeared; by twenty-two— ChatGPT. All the modern large models are descendants of a single paper from seventeen.

We'll break down the mechanics of the Transformer later, when we look at how modern large models are built."

---

## [s07a]— Section 2. Where we are now

"Section two of five. We've figured out what AI is. Next— where it is now, in twenty-six.

First— the scale in figures, then— breakthroughs from teams that were not obvious favorites. The section is short, but it sets the scale: AI is at the same time everywhere and almost nowhere brought to completion."

---

## [s08]— AI became infrastructure in 3 years

"In three years AI became an infrastructure layer. A few telling figures.

ChatGPT— about nine hundred million weekly active users as of February twenty-six. Weekly exactly, not monthly— over a month it's higher.

Stack Overflow Developer Survey twenty-five, forty-nine thousand developers from one hundred seventy-seven countries— eighty-four percent use or plan to use AI; fifty-one percent turn to AI daily.

GitHub Copilot— among regular users, AI writes up to forty-six percent of lines of code, and for Java— sixty-one.

The size of the AI market. Per Grand View Research of twenty-six— three hundred ninety point nine billion dollars in twenty-five, with a forecast of growth to five hundred thirty-nine and a half billion in twenty-six. Per the narrow software-only Statista— lower, around two hundred forty-four to two hundred sixty billion. The spread comes from what you count as the AI market: models, infrastructure, embedded AI, integration. If you compare AI market figures— first compare the methodologies.

The flip side. Per a summary by CNews, Vedomosti, Intellectual Analytics, March twenty-six— about ninety percent of AI pilots in Russia do not reach production deployment. Thirty to forty percent are shut down without an effect, only seven to ten— are in operation.

A detail about trust. Per Stack Overflow— forty-six percent of developers do not trust the accuracy of AI code, versus thirty-one a year earlier. It looks like a contradiction: usage is growing, trust is falling? In fact both figures are consistent— the general trend is a rise in adoption, and the assessment of accuracy is more critical because developers have learned to see where AI errs. This is not "trust is falling", but "trust is becoming more nuanced". We'll return to hallucinations in the fourth section.

The lecture context. AI is already infrastructure with mass adoption and mass failure alike. The difference between these pictures is the place where engineering thinking works, and where you and I spend the next sixty minutes."

---

## [s09]— The space is open: four breakthroughs 2023–2026

"Looking at the figures from the previous slide, it's easy to conclude— "everything is already done, the biggest players lead". This impression is deceptive. Over three years— four loud episodes. Each shows: **the space is open**.

**September twenty-three, Mistral 7B.** A small French lab, founded at the start of that same year by alumni of Meta and Google DeepMind, releases a model under Apache 2.0. Mistral 7B beats Llama-2 13B— a nearly twice-as-large model. The lesson: a small team can release a model at the level of the big players in a matter of months.

**January twenty-five, DeepSeek-R1.** A little-known Chinese lab publishes an open reasoning model at the level of OpenAI o1. The final training run of V3— about **five million six hundred thousand dollars**; the full infrastructure— orders of magnitude more, these are different numbers. On January twenty-seventh, Nvidia lost **five hundred eighty-nine billion dollars** in a single day— the largest single-day loss of market capitalization in history.

**November twenty-five, OpenClaw.** Peter Steinberger single-handedly launches an autonomous open-source AI agent. By the start of twenty-six— more than **one hundred thousand stars on GitHub** in a quarter. On February fourteenth, Steinberger leaves for OpenAI, and the project goes into a non-profit foundation. The lesson: one person with the right concept can release an agent that shifts the market in weeks.

**The story of Georgi Gerganov, llama.cpp and ggml.ai.** A solo project grew into a small team. On February twentieth, instead of venture funding, it joined Hugging Face for support— keeping its autonomy.

In March, llama.cpp crossed **one hundred thousand stars on GitHub**— faster than PyTorch or TensorFlow.

The lesson here is a different one. Not "one person released a product", but **one person built an infrastructure layer on which the entire open ecosystem rests**— the foundation that makes it possible to run large models on an ordinary laptop.

In parallel, Russian tools are developing too: YandexGPT, GigaChat, T-Bank Talisman, Shedevrum. More on this— in the lectures on AI in software development, finance, and the creative industries.

"The space is open" for you and me. The course focuses on the durable concepts— they outlive the change of model generations."

---

## [s10]— Section 3. Four ways to implement

"Section three of five. You and I are in the largest section of today's lecture, twenty-three minutes. Four ways to implement systems with AI: model, chat, agent, application. And most importantly— a simple tool for choosing among them."

---

## [s11]— Ways to implement with AI: not alternatives, but layers

"The key idea of the section. These are **not four alternatives**. These are **four ways to implement one task with a layered structure**. Each next level includes the previous one.

**Model**— stateless inference on a single task. Data in, a prediction out. No interface, no memory, no tools.

**Chat**— a model plus an interface plus dialog memory.

**Agent**— a chat plus tools plus planning. The ability to call an API, read files, execute code, and the logic of choosing the tool at each step.

**Application**— an agent or a chat plus a product interface. On the outside, an ordinary product; the AI works inside as one of the components.

Don't choose "between" the levels as if they were alternatives. Each next wrapping adds capabilities— and at the same time complexity, cost, and error potential. You and I will return to this layered model the whole course."

---

## [s12]— Classification: task × modality

"To talk about concrete AI tools in one language— two axes.

The X-axis— the **task type**. What the system produces. Five types: classification, recognition, retrieval, generation, forecasting.

The Y-axis— the **modality**. What kind of data it works with. Text, image, audio-video, structured data.

These two axes are enough for our course. The technical depth— the architecture of a neural network— later, in the lecture on how large models are built.

One cell deserves attention— forecasting on text, where GPT-4o and Claude sit. At first glance it's strange: isn't that generation? In essence— the same phenomenon. A language model generates text by predicting the next token— the same semantics as in "Generation".

Calibration. **Google Translate**— generation on "text". **AlphaFold**— forecasting of a protein's structure on "structured data". **YOLO**, our demo at the start— recognition on "image".

When discussing each implementation type, you and I will ask: what task and what modality. This prevents mixing systems that are different by nature under the common label "AI"."

---

## [s13]— One task, three ways: the control quadrant

[On the slide— a 2×2 quadrant on top, the task on the right. Three points on the diagonal: Model in the bottom-left, Chat in the center, Agent in the top-right (gold), with a short caption under each point.]

"So the layered model isn't just theory, let's run it on one task through three ways of solving it.

The task: extract fields from an incoming PDF contract and put them into a table. Signing date, counterparty, amount, term of validity. Five or six fields. A familiar engineering task.

The axes of the quadrant. Horizontally— **delegation from the user**: how much the user hands the whole task over to the AI. Vertically— **the developer's control**: how rigid a framework they build around the AI. The more the user delegates, the more framework is needed.

That is why the three ways will fall on the diagonal.

**Way one— the model.** We take a specialized model for extracting structured fields, for example, DocVQA. The user integrates the API themselves: passes the PDF, gets JSON, puts it into a table. Delegation is low— the user controls every step. The developer's control is also low— the model is a raw access point with no orchestrator. Bottom-left corner— the caption "integrates the API themselves, full control".

**Way two— the chat.** We open Claude or ChatGPT in a browser, drag the PDF into the chat, and write: "extract the following fields". We get the result, copy it into a table. Delegation is medium— the user writes the prompt themselves, reads the answer, checks it. The developer's control is also medium— there is the provider's system prompt, basic constraints. The center of the quadrant— the caption "dialogue, clarifications along the way".

**Way three— the agent.** We open Claude Code in the terminal: "Take all the PDFs from this folder, extract the fields, and assemble a table". The agent decides for itself which tool to use, in what order to open the files, how to handle parsing errors. The user's delegation is high— they said "do it", walked away, got the result. The developer's control is also high— the agent works within an orchestrator with rules for tool permission and error-return logic. Top-right corner— the caption "delegation in full, the orchestrator decides".

Note the two empty corners. Top-left— "no point": why build an orchestrator if the user solves it themselves anyway. Bottom-right— the "danger zone": the user handed the task to the AI, but the developer provided no framework.

All three ways solve one task. The difference is not in quality, but in the **distribution of control**— an engineering decision that you and I make at the start of a project. The more we delegate— the more rigid the framework needs to be.

Next, you and I will break down each of the four types in more detail: model, chat, agent, application."

---

## [s15]— Model: input → preprocessing → model → postprocessing → output

[On the slide— an eyebrow pill "MODEL", on top a schema of 5 blocks horizontally in a common frame "This is already an application", at the bottom 4 examples of models.]

"Let's start with the bottom layer— the model, and from there you and I will climb up, layer by layer.

A model is a trained neural network that takes an input and returns an output. Without state between calls, without tools, without dialogue. From the integration point of view— the simplest component: a model call is a function.

An important detail: **a model is not a system, but a component**. In production operation there is always wrapping around it. Five blocks horizontally.

Raw input— a frame from a camera, text, an audio signal. Preprocessing— resizing, normalization, tokenization. Model— the actual output of the prediction. Postprocessing— filtering, formatting, for example cutting off extra boxes or normalizing probabilities. Output— an action, JSON, a class label.

Note— this whole five-block pipeline is enclosed in a common frame with the caption "This is already an application". This is not a visual accident: the model by itself is only one block within the whole. Preprocessing and postprocessing are the responsibility of the **system developer**, not the model itself. This is critical for budget estimation. A YOLO detector by itself— fifty lines of code. But a working system— hundreds of lines: reading the video stream, resizing, normalization, NMS, packaging for the plant's MES system. An estimate based on the model's own volume of work is understated by tens of times.

Canonical models. **YOLO**— object detection, our demo. **Whisper**— speech recognition. **Stable Diffusion and SDXL**— image generation from text. **AlphaFold**— protein structure prediction; Hassabis and Jumper received the Nobel Prize in Chemistry in twenty-four.

When a model is the right choice: high load (a video stream at thirty frames per second— impossible for a chat interface), a stable shape of input and output, a requirement of determinism, edge deployment without internet.

When it's wrong: a one-off request; a task that requires dialogue; a task that cannot be reduced to a single output type. Next— the chat."

---

## [s16]— How a chat works: the dialog cycle

[On the slide— an eyebrow pill "CHAT", a compact dialog-cycle schema: USER on the left in two roles, in the middle Message and Response, on the right a large LLM block, on top the System prompt with a gold arrow down, under the Response a growing history block with the caption "the whole text anew at each step".]

"Let's remove the magic from the chat. At each iteration of the dialogue a compact cycle happens.

On the left— the user in two roles. Sender on top, receiver on the bottom.

**Step one.** The user writes a message.

**Step two.** On top of the message the system prompt is attached— instructions set in advance by the developer: "You are a corporate assistant. Answer in Russian". Plus the **entire chat history** from the start of the session. This combined block is the full input for the model.

**Step three.** The whole package is passed to the LLM as one large piece of text. The model does not "remember" the previous conversation— each time it receives it anew.

**Step four.** The model generates the response token by token; the response is appended to the history and shown to the user.

**Step five.** Look at the growing block under the response— the history accumulates, and at the next step the model will again receive the whole text in full, not the increment.

Two important consequences— two notes on the right.

First— **the system prompt is an engineering lever**. The user doesn't see it, but it is precisely what defines the "character" of the chat: tone, role, constraints, formats. It is the engineer's tool for setting the frames.

Second— **the limitation of the context window**. GPT-4o about one hundred twenty-eight thousand tokens, Claude up to two hundred thousand, Gemini up to a million. A lot, but not infinite. When the history doesn't fit, **old messages drop out**— the chat "forgets" details.

A chat is a pipeline of "assemble → feed → append → show"."

---

## [s17]— Chat: model + interface + dialog memory

"A chat is a model wrapped in a text interface with dialog memory within a session. Canonical products: ChatGPT, Claude, Gemini, DeepSeek Chat, GigaChat, YandexGPT, Mistral Le Chat. They differ in quality, in the length of the context window, in cost— but the pattern is one.

The case. An engineer receives an incomprehensible normative document with a mass of references to standards. The task— figure it out and put together a checklist. A typical case for a chat: a one-off task that requires dialogue— "what does this clause mean", "give an example", "put together a checklist". No model is needed, no agent is needed, there is no specialized application.

Chats are tied to the main cause of failure of AI projects. Most of the rolled-back pilots tried to solve, with a chat, tasks that needed a model, an agent, or an application. A chat is convenient and accessible— that's why it is often chosen as a universal tool. And this is often the wrong decision.

An important caveat about practice. Pure chats— a model plus an interface plus a short memory— are almost never seen in production operation. Everywhere the chat is already extended to an agent: for long-term memory and search over the corporate knowledge base via RAG, retrieval-augmented generation. The boundary "chat vs agent" is blurred on this side. "A chat without an agent" is the interface of ChatGPT, Claude.ai, consumer services. We'll break down the agent architecture on the next slide.

The prompt. The minimal formula: **prompt = role + task + context**. In detail— later in the course."

---

## [s18]— Agent architecture: plan, action, observation, reflection

[On the slide— an eyebrow pill "AGENT". A linear ReAct pipeline: Plan → Action → Observation → Reflection, with labeled connectors to the Tools and Memory, a gold loop-back arrow "continue" and a branch "stop → result to user".]

"The agent— the next layer. Compared to the chat, the agent has three new components.

**First— the orchestrator.** It looks at the goal, breaks it into steps, chooses the tool, decides when to stop.

**Second— external memory.** A vector database, a file system, an action log— beyond a single session.

**Third— tools.** Calling an API, files, code, web search. Each tool is a function with a description.

Look at the schema— a linear cycle, the base model is called **ReAct**. **Plan**— an action plan is formulated. **Action**— a tool is called; the connector at the bottom shows the access to the tools. **Observation**— the result is written to memory; the connector shows the access to memory. **Reflection**— the goal is achieved or the next step is needed.

This gold arrow on top is the return loop: if the goal is not achieved, the reflection sends it back to the plan. And if it is achieved— the other branch: stop, the result to the user.

Lilian Weng's formula: **Agent = LLM + Memory + Planning + Tool Use**. Products today: Claude Code, Devin, OpenAI Operator, AutoGPT."

---

## [s19]— Agent at work: 200 PDFs— a sequence of steps

[On the slide— an eyebrow pill "AGENT". On the left the case "200 PDFs", on the right 7 numbered steps indicating the tool at each, gold highlight on step 7 (orchestrator loop).]

"A concrete case. Two hundred PDF reports; from each, extract the date, the counterparty, the amount, and assemble a summary table. A multi-step task with tools. Neither a model fits— there's no such specialized one— nor a chat— it's uncomfortable to copy two hundred files. The agent is the natural choice.

Look at the right part. Seven steps, at each— an explicit tool. The agent doesn't "think" the whole path itself; at each step it decides which tool is needed now.

Step one— get the list of files, **the file system**. Step two— open the PDF, **PDF reading**. Step three— extract the text, **text extraction** via OCR or a parser. Step four— embed into the **vector database**. Step five— find the key fields, **search plus an LLM call**. Step six— write the row, **Sheets API or CSV**. Step seven— loop over the two hundred files, **the orchestrator loop**.

Each step is an explicit tool call. This is exactly what an "agent" is: a chat plus orchestration plus tools plus memory. Canonical ones today: Claude Code, Devin, OpenAI Operator, AutoGPT, CrewAI, LangGraph."

---

## [s19a]— Levels of autonomy + human-in/on/out-of-the-loop

[On the slide— an eyebrow pill "AGENT". On the left a staircase of 5 levels with Russian names and an English gloss in parentheses (Operator → Collaborator → Consultant → Approver → Observer; level 5 in gold), on the right 4 frames, at the bottom a gold takeaway.]

"The autonomy level of an agent is an **engineering design decision**, not a property of the model.

**Five levels per Feng, McDonald, Zhang.** They differ by the user's role— captioned under each on the slide.

**Operator**— approves every action. Claude Code in command-confirmation mode.
**Collaborator**— works on par with the agent. Pair programming with Cursor.
**Consultant**— sets the goal, edits the plan. Devin on a ticket.
**Approver**— approves at checkpoints. A PR under review.
**Observer** in gold— only receives the result. AutoGPT overnight.

In parallel— a frame from safety engineering: where the human is relative to the loop. The order is the same, the most autonomous on top.

**Out of the loop** in gold— only the result, level five. **On the loop**— observes, can interrupt, levels three-four. **In the loop**— at every step, levels one-two. Separately— **manual override**: at any level.

The main point: **the autonomy level is a product choice, not a property of the model**."

---

## [s20]— Applications: AI packaged into a product interface

"The fourth layer— the application. Note, this is the last layer in our layered model.

A full-fledged product in which AI is one of the internal components. The user doesn't write prompts— they press buttons, fill in forms. **AI as a feature, not a product**. A good application has a deterministic interface: the same action gives the same reaction.

Canonical examples. **Google Translate**— neural machine translation, more than a billion users per month. **Notion AI**— GPT-4 or Claude inside, buttons "Summarize", "Improve writing". **YandexGPT in Search**— a proprietary LLM, a short answer above the search results. **Grammarly**— NLP plus LLM, underlines in any text field. **Yandex Maps**— ML for routing, ETA, traffic. **Adobe Firefly**— diffusion models, the Generate button in Photoshop.

The case: once a week, translate a block of technical documentation. No model is needed, no chat is needed, no agent is needed. Google Translate or YandexGPT in Search— a ready-made application. Overpaying with complexity is an anti-pattern."

---

## [s21]— Checklist "Which type of AI to choose": 2 questions + quadrant

"The culmination of the section— a practical tool. Two diagnostic questions, whose answers unambiguously determine the implementation type. Note: the axes of the quadrant are not separate questions, but **divisions of the scale**.

**Question one— on the left scale.** Is interaction with the user needed? "Yes"— the division on top, "no"— at the bottom. If yes— communication, clarifications, real time— the upper half, the **chat / agent** family. If no— autonomously by a trigger or a stream— the lower half, the **model / application in automation mode** family.

**Question two— on the bottom scale.** Is independent work with tools needed? "No" on the left, "yes" on the right. If yes— calling an API, files, code— the right half, the **agent / application in automation mode** family. If no— a single step "input → output"— the left half, the **chat / model** family.

The intersection of the two scales gives the quadrant. Bottom-left— no/no— **Model**. Bottom-right— no/yes— **Application in automation mode** (for example, an ETL pipeline with an AI classifier). Top-left— yes/no— **Chat**. Top-right— yes/yes— **Agent**.

Three cases.

A conveyor-belt defect detector. Q1: no. Q2: no. Bottom-left— **model**.

A corporate chat for parsing a norm. Q1: yes. Q2: no. Top-left— **chat**.

Two hundred PDFs and a table. Q1: yes— the user sets the task. Q2: yes— open files, parse. Top-right— **agent**, the point is gold.

Thirty seconds— turn to your neighbor. Name an AI tool you've used in the last month. Run it through the two questions. Which corner did you land in?

AI works where the task and the implementation type matched. Most of the rolled-back pilots didn't ask these two questions; they chose the tool by fashion. Apply this quadrant to your own case."

---

## [s22]— Section 4. The boundaries of AI— your zone of responsibility

"Section four of five. We move on to boundaries and safety. This is not a horror chapter— it's an inventory of problems that arise systematically in AI systems.

The theme— your zone of responsibility, not a question for separate specialists. You have already made the decision to embed AI— you answer for an incident, not the "model". AI errs systematically and predictably: bias, hallucinations, sycophancy, drift— these are properties of the technology, not random bugs. And the boundary "what AI cannot do"— is also your zone: beyond it you need verification and a fallback scenario.

Next: where the data goes, hallucinations, bias and sycophancy, AGI forecasts."

---

## [s23]— Consumer vs enterprise: where your data goes

[On the slide— a bridge label at the top under the title, two columns: consumer (data → training) vs corporate (data ≠ training) + Samsung incident + EU AI Act fines.]

"From the general frame of section four— to the first concrete risk that you and I are about to break down. Where does your data physically go when you write a request into a cloud AI service?

Your text— and often the attached files, images too— is sent to the provider's servers. What happens to it next— depends on the tier.

**Consumer.** OpenAI ChatGPT Free and Plus use the data for fine-tuning by default; you can turn it off in the settings. Anthropic Claude, since September twenty-five, asks for permission; on consent the retention period is five years. Google Gemini— data for training by default, part is selectively reviewed by people.

**Corporate tiers and API.** OpenAI Enterprise, the OpenAI API since March twenty-three, Anthropic for business, Google Workspace, Vertex AI— the data is **not used** to train the foundation models. Zero Data Retention agreements are available— the provider doesn't store the prompts at all.

The canonical incident— March–April twenty-three, Samsung. Engineers, in three episodes, uploaded proprietary code, a meeting transcript, and test sequences for chip debugging into the consumer ChatGPT. Samsung's secrets effectively ended up in OpenAI's dataset. Samsung banned employees from external AI and introduced a limit of one thousand twenty-four bytes per prompt. A year later the ban was partially lifted after the rollout of internal tools.

The alternative— local deployment of open models via Ollama, LM Studio, vLLM. It eliminates the leak, adds GPU costs. The empirical break-even point— on the order of one hundred thousand requests per day.

In the European Union, the EU AI Act: the standard level of fines is up to fifteen million euros or three percent of turnover. The top level for prohibited practices— up to thirty-five million or seven. The NIST AI RMF— US standards. Russian regulation is in the process of being formed.

**The practical conclusion. Never upload confidential data into consumer AI services without checking the policy of the specific tier.** The rule is simple, but it's systematically violated."

---

## [s24]— Hallucinations— an inherent property of AI

"A hallucination in the context of an LLM is the confident production of factually incorrect information in a form indistinguishable from the correct one. The model does not "know" that it's telling an untruth; for it, this is simply a statistically plausible continuation of the sequence of tokens.

A simple experiment you can repeat today. Ask a chat: "name three scientific articles from twenty twenty-four on the topic with authors and DOIs".

With significant probability you'll get three convincing-looking references, in which the author names may be mixed up or invented, the journals are real but there are no such articles in them, and the DOIs are syntactically correct but don't resolve. Verification takes a minute: you open doi.org, paste it, and see whether it resolves or not. Without verification— it looks credible.

Per the Vectara Hughes Hallucination Evaluation Model benchmark, the range of current models is very wide: from less than one percent on the standard summarization task (Gemini 2.0 Flash) to ten-fifteen percent on reasoning tasks. This means: speaking of a "hallucination percentage of an LLM" in general is incorrect. The figure depends heavily on the task and the benchmark.

Now a short exercise. I have here two AI answers to one and the same factual question. In each— one correct and one planted detail. Thirty seconds in pairs: which part is the fake? What did you check first?

**Anti-pattern number one: "AI knows everything".** Any AI answer to a factual question is a hypothesis that requires verification. Especially— links, figures, quotes, legal norms, medical recommendations. This does not mean "don't use AI for facts". It means "verify what AI gives out as a fact". A critical reading attitude is not an extra precaution, but a part of the standard working process.

We'll return to hallucinations in the lectures on specific industries— medicine, oil-and-gas, science— everywhere the cost of an error in a factual detail is high."

---

## [s25]— Bias, sycophancy, drift: three manifestations of one nature

"Let's break down three problems of a common nature: the model is a reflection of the data, not an independent source of truth.

**Bias— bias.** The model repeats the skews of the dataset. Example: a resume-screening model, trained on the data of a company where there are fewer women in technical positions, discriminates against female candidates— statistically predicting "such profiles were usually rejected". The hardest category to fix: the data records the structural inequalities of the world.

**Sycophancy— sycophancy.** First the term: **RLHF**, Reinforcement Learning from Human Feedback— a human ranks the answers, the rankings serve as a reward signal for fine-tuning. The standard step of turning an LLM into a chat assistant. The flip side: the labelers rate pleasant answers higher. The model tends to agree, to go along.

The case— April twenty-five. On April twenty-fifth, OpenAI rolled out an update to GPT-4o that was intrusively flattering. On the twenty-eighth, Altman wrote on a social network that they had already begun the rollback that same evening. On the twenty-ninth— a root-cause analysis was published. The most imperceptible category: the user, receiving compliments, doesn't notice the loss of the model's critical attitude.

**Drift— distribution shift.** The model behaves poorly outside the training distribution. Example: a model on code from twenty-three, in twenty-six, will suggest an outdated library and won't account for API changes. The most frequent category in long-lived systems: quality quietly degrades without explicit failures.

In your professional field, which is more dangerous— bias, sycophancy, or drift? Hands: bias— sycophancy— drift—

All three— one nature. The model doesn't know the truth, it reproduces the regularities of the data."

---

## [s26]— AGI forecasts: 4 speakers, 4 material interests

"All production AI systems are narrow AI: optimized for specific tasks. AGI— a hypothetical AI with a human level of capabilities across a wide range of domains. An open question with mutually exclusive forecasts.

A simple rule of critical reading. When you see a specific AGI forecast— **ask about the speaker's material interest**. This isn't about insincerity. It's about the fact that each leader is at the same time building a company and shaping investors' expectations.

**Sam Altman, OpenAI.** "We know how to build AGI; this is the start of the path to superintelligence", January twenty-six. What's advantageous: an IPO and hundred-billion rounds— AGI confidence supports the valuation.

**Dario Amodei, Anthropic.** "AGI in two-three years; AI will replace software developers within a year", Davos twenty-six. What's advantageous: pressure from OpenAI; a funding round.

**Demis Hassabis, Google DeepMind.** "AGI by two thousand twenty-nine— two thousand thirty, three-four years; the window narrowed over twenty-six", Axios and Google I/O, May twenty-six. What's advantageous: a leader of the research community; credibility with a cautious stance; Google doesn't need AGI hype.

**Yann LeCun, AMI Labs.** "The LLM paradigm won't lead to AGI; a new architecture is needed". What's advantageous: a round of about a billion in March twenty-six for an alternative path; a counter-consensus for a startup.

The pattern. Not one holds a neutral scientific position. Each forecast reflects a commercial interest or market positioning. This doesn't mean they don't believe it. It means that AGI forecasts are a **market statement**, not a scientific one.

When reading a top executive's interview, ask the question: "what decision does he want the market to make on the basis of this statement?" We'll return to AGI as a concept— in the final part of the course, during the synthesis of knowledge."

---

## [s27]— Section 5. What to take home

"Section five of five— the finale. You and I are on the last six and a half minutes. We've gone through four sections: what is AI, where we are now, four ways to implement, boundaries. Now— the summary, the semester map, the grade formula, what's in lecture two, and Q&A."

---

## [s28]— What we've covered: three main takeaways

"If there's one thing worth taking away from the lecture— the main question: where AI works, where it doesn't, and how to figure that out.

Three main takeaways.

**First.** AI is a spectrum of technologies, not a monolith. A tool belongs to one of four types: model, chat, agent, application.

**Second.** Choosing the AI type is an engineering skill, and you and I have a tool— two questions plus the quadrant. Most of the rolled-back pilots didn't ask them.

**Third.** AI amplifies the human, but goal-setting and responsibility remain ours. All the errors we broke down— hallucinations, bias, sycophancy, drift, leaks— require human verification."

---

## [s29]— Semester map: 17 lectures, 3 modules + exam

[On the slide— a horizontal timeline of 4 color blocks: 3 content modules + a separate "Exam" block; the block width is proportional to the number of lectures; gold highlight on the current lecture 1.1; the checkpoints Midterm1/Midterm2/Midterm3 at the module boundaries.]

"The course— seventeen lectures in three content modules, plus a concluding exam. Today you and I are at the first session of the first module.

**Module one— foundations and familiar industries, six lectures.** Introduction— right now; AI architecture; agents and RAG; software; finance and retail; the creative industries. **Midterm one— upon completion.**

**Module two— industries at the junction of the physical and the digital, five lectures.** Engineering design, aerospace, manufacturing, digital twins, agriculture. **Midterm two.**

**Module three— infrastructure, science, extraction, plus synthesis, six lectures.** Logistics, telecom and cybersecurity, science, oil-and-gas, medicine, systematization of knowledge. **Midterm three— the final one.**

And as a separate block— not a module, but the final assessment— **the exam**.

Today— the formula "prompt = role + task + context". Later— PARTS, chain-of-thought, few-shot. By the end of the course, prompting will become an engineering discipline."

---

## [s29a]— Semester grade

"The semester grade. Since we're on the semester map— I'll close the question about the grade right away.

One hundred points add up gradually: ten— attendance, thirty— the exam, three times twenty— the midterms, upon completion of each of the first three modules. The grade is formed over the whole semester, not just at the end."

---

## [s30]— Lecture 2: How modern large models work

"Lecture two— "How modern large models work". Not so as to make ML engineers out of you— but so that you understand **why** a model behaves the way it does.

Four concepts in Russian.

**Tokens**— the units into which the model cuts up the text.

**Embeddings (vector representations)**— the numeric addresses of tokens in the semantic space.

**The attention mechanism (attention)**— how the model decides which parts of the input to look at.

**Temperature**— the parameter of randomness in choosing the next token.

These four concepts explain the behavior of all modern LLMs— from ChatGPT to DeepSeek. With them, you and I will understand **why** prompts work, not just how."

---

## [s31]— Questions?

"That's the main part of what you and I have gone through today. Next— questions.

What's good to ask: clarifications on the implementation types; where to place your tool by the checklist; boundaries— if you've had an experience with hallucinations or a leak; the semester plan.

Who'll start?

I'll answer the most frequent one. Can you use AI right now? You can. The checklist already gives a tool.

If anything remains unclear after the session— my contacts were on the bio card slide at the start of the lecture, feel free to write.

Thank you for your attention."

---

## Reserve

If time remains after Q&A— backup stories to add:

- **More on AlphaFold.** The structure, scale (200M proteins), the 2024 Nobel Prize, the drug-discovery case. Fits if the questions went toward "AI in science".
- **The extended Samsung case.** The chronology of the three incidents, the corporation's reaction, the consequences for the industry. Fits if the questions went toward data safety.
- **An additional hallucination example.** Live demo: ask ChatGPT/Claude a fresh question on a narrow topic, break down the answer together with the room. Fits if there's a technical possibility and internet.
- **Levels of autonomy in a real project.** Where exactly to set the level for your task: an example of how one and the same Claude Code agent works in "operator" mode (a new developer) and "approver" mode (an experienced one).
- **More on MCP.** What it is technically, how it compares to OpenAI's tools API, why it became a standard. Fits if there are developers with experience in the room.
- **More on llama.cpp / ggml.ai.** How model quantization for running on ordinary hardware is arranged, why this matters for edge deployment. Fits if the questions went toward "how to run AI without the cloud".

If the time exceeds 75 minutes— **stop at Q&A, don't compress the reserve into the main flow**. Better to finish a bit early than to drag it out.
