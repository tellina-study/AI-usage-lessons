# Roast: Lecture 1 Slide Plan

**Date:** 2026-03-31
**Reviewer role:** Curriculum design expert + AI researcher
**Input:** Slide plan (Google Doc), all research files from notes/research/lecture-1/
**Verdict:** The plan has excellent *content* but mediocre *teaching design*. It reads like a textbook outline, not a lecture experience.

---

## 1. Structure Problems

### 1.1 The Opening Is Backward

The plan opens with history and definitions (slides 1-5, 15 minutes). Our own teaching-examples.md research explicitly warns:

> "НЕ начинать с 20-минутной истории AI. Даже Microsoft, у которых Lesson 1 = история, признают, что это работает только как фон. Краткая история (3-5 мин) достаточно."

We researched this. We wrote this. And then we ignored it.

The best courses do the opposite:
- **fast.ai** trains a model in 5 minutes (result-first)
- **CS50 AI** gives two projects on week 0
- **MIT 6.S191** gives a lab immediately after the lecture
- **Stanford CS221** opens with real tasks, then finds abstractions

Our plan opens with Turing (1950), Dartmouth (1956), and a timeline of AI winters. Students who came to learn about AI in 2026 are being sent to 1950 before they see a single working AI system. This is the "history-first" anti-pattern that our own research identifies as the least engaging approach.

**What the best courses do instead:** Hook with a live demo or a WOW moment in the first 5 minutes, then weave in minimal history (3-5 min) later, when students have context to care about it.

### 1.2 The Order Is Wrong

Current order: History/Definitions (15 min) -> AI Around Us (10 min) -> Model/Chat/Agent/App (25 min) -> Security + Human vs AI (15 min) -> Conclusion (5 min)

Problems:
1. **The strongest section is buried and starved.** "AI Around Us" (slides 6-8) is only 10 minutes but has the richest material: phone AI, recommendation stats, market numbers, wow-facts. This should be EARLY and LONGER.
2. **The most abstract section gets the most time.** Model/Chat/Agent/App (25 min) is a taxonomy that matters for practitioners but is premature for students who have not yet interacted with AI themselves. This belongs more naturally in Lecture 3 (architectures).
3. **Security and Human vs AI are awkwardly bundled.** These are two distinct topics sharing one section. Security (cloud vs local, Samsung case) is practical. Human vs AI (Narrow/General, Moravec's paradox) is philosophical. Bundling them weakens both.

**Recommended order:**
1. Hook + Ice Breaker (5 min) -- demo or interactive, not a quote
2. AI Around Us -- you already use AI (15 min, expanded)
3. What Is AI -- brief definitions + brief history (10 min, compressed)
4. What AI Can and Cannot Do -- capabilities + limitations + security warning (15 min)
5. How to Interact with AI -- Model/Chat/Agent/App LIGHT overview (10 min, not 25)
6. Live Demo + Interactive Element (10 min)
7. Conclusion + Assignment (5 min)

### 1.3 Pacing: 25 Slides in 75 Minutes

25 slides in 75 minutes = 3 minutes per slide average. But the plan is wildly uneven:

| Section | Slides | Time | Min/Slide |
|---------|--------|------|-----------|
| Opening | 2 | 5 min | 2.5 |
| History/Definitions | 5 | 15 min | 3.0 |
| AI Around Us | 3 | 10 min | 3.3 |
| Model/Chat/Agent/App | 7 | 25 min | 3.6 |
| Security + Human vs AI | 6 | 15 min | 2.5 |
| Conclusion | 3 | 5 min | 1.7 |

**Too tight:** Security + Human vs AI tries to cover cloud vs local, narrow vs general AI, human advantages, human disadvantages, AND physical world challenges in 15 minutes across 6 slides. That is 2.5 min/slide for complex topics. Something will be rushed.

**Too loose:** Model/Chat/Agent/App gets 25 minutes for material that could be a 10-minute overview in L1 and a deep dive in L3. Seven slides with detailed "when to use / when not to use / pattern / anti-pattern" tables is lecture-3 depth, not lecture-1 depth.

**Conclusion is dangerously short:** 5 minutes for summary + lecture 2 preview + Q&A. If any previous section runs over (and they will), Q&A disappears entirely. Q&A is where engagement happens. Protect it.

---

## 2. Content Problems

### 2.1 Classifications Are Too Academic for an Introductory Lecture

Slides 3-5 present three classification systems in 7 minutes:
- By task (detection, segmentation, generation, prediction)
- By modality (numbers, sound, images, text, multimodal)
- By capability + learning approach + generative/discriminative (slide 5 alone crams Narrow/General/Super AI + Supervised/Unsupervised/RL + Generative/Discriminative into 2 minutes)

Our classifications.md research file documents **six** classification taxonomies with academic sources for each. That research is for *us* to draw from, not for students to absorb in 7 minutes on day one. Students have not seen AI do anything yet. Asking them to memorize classification grids before they have intuition is putting the cart before the horse.

**The research file itself warns:** teaching-examples.md says "НЕ перегружать терминологией. Ng вводит термины постепенно, по одному, с примерами. Не давать AI/ML/DL/NLP/CV/RL/LLM/AGI/GenAI за одну лекцию."

Slide 5 alone tries to introduce: Narrow AI, General AI, Super AI, Supervised Learning, Unsupervised Learning, Reinforcement Learning, Generative Models, Discriminative Models -- eight concepts in 2 minutes. That is one new concept every 15 seconds.

**Recommendation:** Keep ONE classification (by task type, with vivid examples), mention Narrow vs General AI briefly, and defer everything else to later lectures.

### 2.2 "AI Around Us" Is Criminally Underweight

This section has the strongest material and gets the least time:
- industry-examples.md has stunning statistics (900M ChatGPT users, 70% YouTube watch time from AI, Gmail blocks 15B spam/day, Copilot writes 46% of code)
- Phone AI details (Neural Engine at 35 TOPS, Deep Fusion fusing 9 exposures)
- Russian market data (51% of Russians used AI in 2025, 47% prefer domestic solutions)
- Wow-facts (AlphaZero mastered chess in 4 hours, AlphaFold won Nobel Prize)

All of this gets crammed into 10 minutes and 3 slides. Meanwhile, the Model/Chat/Agent/App taxonomy gets 25 minutes and 7 slides.

The "AI Around Us" section is the one that will make students sit up and think "this course is relevant to MY life." It should be the backbone of Lecture 1, not a sidebar.

### 2.3 Model/Chat/Agent/App Is Over-Scoped for L1

The plan devotes 25 minutes (one-third of the entire lecture) to a detailed four-way taxonomy with:
- Two different quadrant diagrams (slides 9-10)
- Detailed "when to use / when not to use" for each type
- Patterns and anti-patterns for each type
- A comparison table

This is Lecture 3 material (architecture and interaction patterns). In Lecture 1, students need to know:
1. You can talk to AI (Chat) -- they probably already do
2. AI powers apps you use every day (Application)
3. There are also standalone models and agents -- we will explore these later

A 10-minute overview with one vivid example per category is sufficient. The quadrant diagrams and pattern/anti-pattern analysis belong in a later lecture where students have enough experience to appreciate the distinctions.

### 2.4 Human vs AI Section -- Too Philosophical, Too Late

Slides 18-21 cover:
- Narrow vs General AI (philosophical)
- What AI does better (empirical)
- What humans do better (philosophical + empirical)
- Physical world challenges (technical)

This is four distinct sub-topics in 10 minutes (excluding the "anecdote" break). The human-vs-ai.md research file is 320 lines of rich material including Pearl's Ladder of Causation, Moravec's Paradox, Chollet's ARC-AGI benchmark, and the autonomous driving SAE levels. Trying to touch all of this in 10 minutes guarantees superficiality.

**The core message for L1 is simple:** AI is very good at patterns in data, humans are very good at goals, context, and the physical world. That is a 5-minute point with 2-3 vivid examples. Save the depth for when students have hands-on experience.

---

## 3. Missing Elements

### 3.1 No Live Demo

This is the single biggest gap. Every course we researched uses live demos in L1:
- fast.ai trains a model live
- MIT 6.S191 gives a lab
- CS50 AI assigns two projects
- teaching-examples.md lists 7 specific demos (Quick Draw, Teachable Machine, ChatGPT, etc.)

The plan mentions "Живое демо: задать вопрос ChatGPT/Claude" as a note on slide 12, buried 40 minutes into the lecture. By then, students who were going to disengage have already disengaged.

**A live demo should happen in the first 10 minutes.** Options:
- Quick Draw (30 seconds to show, students can try on phones)
- ChatGPT solving a problem from their domain (engineering at Bauman)
- Teachable Machine (train a model in 2 minutes live)

### 3.2 No Interactive Element

The plan has exactly one interactive moment: "спросить студентов 'а вы как бы определили AI?'" (slide 2, minute 9). This is a raised-hand question buried in the definitions section -- the lowest-energy part of the lecture.

Harvard AI Pedagogy Project recommends think-pair-share. teaching-examples.md recommends:
- Audience poll ("Who has used ChatGPT? For what?")
- "Human or AI?" guessing game
- Teachable Machine group exercise
- Quick Draw on phones

The plan has zero audience participation with technology. In a lecture about AI tools, students never touch an AI tool.

### 3.3 No Assignment for Next Time

The plan ends with "Вопросы" (slide 24). No assignment. No homework. No "try this before next class."

What the best courses do:
- **CS50 AI:** Two projects on week 0
- **fast.ai:** "Train your own model" assignment
- **ETH Zurich:** "Zero project" due before lecture 2
- **teaching-examples.md recommends:** "Попробовать 3 AI-инструмента и написать рефлексию (что удивило, что не получилось)"

An introductory lecture without an assignment is a missed opportunity. Students are maximally motivated after L1. Capture that energy with a concrete task.

### 3.4 No Connection to Their Engineering Lives

The "AI in your phone" examples (Face ID, autocorrect, recommendations) are consumer-facing. These students are ИУ6 (Computer Science) at МГТУ Баумана -- future engineers. Where is:
- AI in software development (Copilot writes 46% of code -- this should terrify/excite them)
- AI in engineering workflows (CAD optimization, simulation, testing)
- AI in their future careers (500K+ open AI/ML positions globally, $206K average salary)
- AI they could build (not just use)

The career connection is one of the five key factors from the pedagogical research (ScienceDirect, 2024): "Интеграция с будущей карьерой -- зачем это студенту."

### 3.5 The Ice Breaker Is Passive

The ice breaker is a quote: "В 2025 году AI написал код, который прошёл техническое интервью в Google. Но AI не смог объяснить, ЗАЧЕМ он написал именно так."

This is a good fact but a passive delivery. The lecturer reads it, students listen. Compare with:
- **"Human or AI?" game:** Show 3 code snippets, students vote which was written by AI
- **Quick poll:** "Raise your hand if you used AI in the last 24 hours" (most hands go up -- powerful visual)
- **Live ChatGPT challenge:** Ask it to solve a Bauman exam problem in real-time

An ice breaker should require student *participation*, not just attention.

---

## 4. Research-Informed Critique

### 4.1 Scorecard Against Our Own Research Recommendations

teaching-examples.md Section 5.1 recommends 8 blocks for L1. How does the plan score?

| Recommended Block | Present in Plan? | Quality |
|-------------------|-----------------|---------|
| 1. Hook with live demo (5-7 min) | Partial -- quote, no demo | Poor |
| 2. Audience poll (3-5 min) | One question on slide 2 | Poor |
| 3. AI in your life (10 min) | Yes, slides 6-8 | Underweight |
| 4. What is AI? (15 min) | Yes, slides 1-5 | Over-academic |
| 5. What AI can and cannot (10 min) | Split across sections | Fragmented |
| 6. Interactive element (10-15 min) | Absent | Missing |
| 7. Course overview (10 min) | Slide 23 (1 min teaser) | Severely underweight |
| 8. First assignment (5 min) | Absent | Missing |

**Score: 2/8 adequate, 3/8 present but weak, 3/8 missing entirely.**

The plan does not follow the structure that our own research recommended.

### 4.2 Against Key Pedagogical Principles

| Principle | Source | Plan Status |
|-----------|--------|-------------|
| Result in first 5-10 min | fast.ai, MIT | No result shown |
| Interactive element mandatory | Harvard AI Pedagogy | Missing |
| Honest about limitations | Andrew Ng | Present (slide 8) but brief |
| Connection to student lives | CS50, Ng | Surface-level (phone only) |
| Assignment on day 1 | CS50, ETH | Missing |
| Course roadmap | CS221, CMU | 1-minute teaser only |

### 4.3 The Harvard CS50 Comparison

Harvard CS50 AI gives students two projects on Week 0: "Degrees" (six degrees of separation) and "Tic-Tac-Toe" (minimax AI). Students leave the first session with code to write.

Our plan gives students... a quote about Google interviews and a promise that Lecture 2 will talk about transformers.

### 4.4 The fast.ai Comparison

fast.ai trains a working image classifier in 5 minutes of Lesson 1. By Lesson 2, students deploy a model to Hugging Face. Jeremy Howard's philosophy: "You can use AI before you understand AI."

Our Lecture 1 spends 15 minutes on history before students see AI do anything. The first "demo" is buried at slide 12 as a side note.

---

## 5. Slide-by-Slide Critique

### Slide 0 -- Ice Breaker
**Content:** Quote about AI passing a Google interview but not explaining why.
**Strong:** Good fact, creates tension (AI is capable but limited). Sets the "it is interesting and ambiguous" tone.
**Fix:** Make it interactive. Show a real AI-generated code snippet and a human one. Ask students to vote. Then reveal the answer. Two minutes, active participation.

### Slide 0.1 -- About Me
**Strong:** "3 points max, no long CV" is the right instinct.
**Fix:** Include WHY you care about AI in practice, not just credentials. Students connect with passion, not titles.

### Slide 1 -- History Timeline
**Strong:** Good selection of milestones. "PIVOT" framing (LLMs changed what AI means) is the most valuable insight here.
**Fix:** This slide should NOT be the third thing students see. Move it to after "AI Around Us" when students have context. Compress to 2 minutes. The pivot framing is gold -- lead with that, not with Turing 1950.

### Slide 2 -- Multiple Definitions
**Strong:** Showing 4-5 definitions and concluding "no consensus, and that is okay" is intellectually honest. The "ask students for their definition" prompt is the plan's only interactive moment.
**Fix:** Four academic definitions (Turing, McCarthy, Russell & Norvig, ISO) in 4 minutes is a wall of text. Pick two: McCarthy ("the science and engineering of making intelligent machines" -- simple) and ISO 22989 ("engineered system that generates outputs for human-defined objectives" -- modern). Ask for student definitions FIRST, then show the academic ones.

### Slide 3 -- Classification by Task
**Strong:** The matrix (detection, segmentation, generation, prediction) with branded examples is concrete and memorable.
**Fix:** Good slide. Keep it. But the branded examples need updating -- mosmed.ai is niche. Use examples students use: Google Photos (detection), Copilot (generation), Yandex Weather (prediction).

### Slide 4 -- Classification by Modality
**Strong:** Modality classification is intuitive and visual.
**Fix:** 2 minutes is about right. Good slide. Could be combined with slide 3 into one "types of AI" overview.

### Slide 5 -- Other Classifications
**Weak:** Three classification systems (ANI/AGI/ASI + Supervised/Unsupervised/RL + Generative/Discriminative) in 2 minutes. This is a terminology dump. Students will retain zero of it at this speed.
**Fix:** Cut entirely from L1. Mention Narrow vs General AI as a single sentence ("All current AI is narrow -- good at one task"). Defer learning paradigms and generative/discriminative to later lectures.

### Slide 6 -- AI in This Room
**Strong:** Best slide concept in the entire plan. "Take out your phone. AI is already inside it." The "ask students for their own examples" prompt is excellent.
**Fix:** This should be slide 1 or 2, not slide 6. Expand to 7-8 minutes. Add the killer stats: 35 TOPS in your pocket, Deep Fusion fusing 9 exposures per photo, 12B Google Lens searches/month. Make it visceral.

### Slide 7 -- AI in Numbers
**Strong:** Good data. Market stats and adoption numbers create gravitas.
**Fix:** Add career-relevant numbers: 500K+ open AI positions, $206K average salary, 46% of code written by Copilot. These hit different for CS students.

### Slide 8 -- What AI Cannot Do (Yet)
**Strong:** Great bridge concept. Honest about limitations.
**Fix:** Expand with a concrete failure. The Chevy Tahoe for $1 story (from industry-examples.md) or the 2000 chicken nuggets story. Humor + humility. Currently only gets 2 minutes -- double it.

### Slides 9-10 -- Two Quadrant Diagrams
**Weak:** Two separate quadrant diagrams back-to-back (control vs determinism, then single-step vs multi-step). This is framework overload for L1. Students do not have the experience to populate these axes with intuition.
**Fix:** One simple diagram maximum. Or better: skip the axes entirely and show four concrete examples side by side. Students will build the mental model from examples, not from axes.

### Slide 11 -- Model (Standalone)
**Decent:** YOLO, Whisper, Stable Diffusion are good examples. The "anti-pattern: using LLM where a simple model suffices" is a genuine insight.
**Fix:** For L1, this needs to be 1-2 minutes, not 4. "Some AI is a specialized model that does one thing brilliantly. Example: YOLO detects objects in video at 30 FPS. You do not chat with it, you feed it data." Done.

### Slide 12 -- Chat
**Strong:** The hallucination demo idea is excellent. "Первый промпт студентов" is the right instinct.
**Fix:** THIS should be the centerpiece demo, not a note on slide 12. Move it forward. Make it a 5-minute interactive segment: everyone opens ChatGPT/Claude on their phone, asks a factual question about Bauman, checks the answer. Collective discovery of hallucinations.

### Slide 13 -- Agent
**Decent:** Good framing (plan -> code -> test -> fix -> deliver). Claude Code is a relevant example.
**Fix:** 4 minutes for agents in L1 is too much. Students have never used an agent. A 1-minute teaser ("In Lecture 3 we will build one") is sufficient. Save the ReAct framework, tool use details, and anti-patterns for when they have context.

### Slide 14 -- AI Application
**Strong:** Yandex Navigator example is perfect for this audience. "AI as invisible helper" is a memorable framing.
**Fix:** Good content, right length (4 min). The "AI-powered marketing without real AI" anti-pattern is fun and engaging.

### Slide 15 -- Comparison Table
**Decent:** Summary tables are good pedagogical practice.
**Fix:** If the section is compressed to 10 min, this table should be a handout or Telegram channel post, not a lecture slide. Students will not absorb a 4-column comparison table after hearing about these categories for the first time.

### Slide 16 -- Local vs Cloud
**Strong:** Samsung case is the single best teaching example in our entire research. Students will remember it.
**Fix:** Lead with Samsung, not with abstract "what happens to your data." Story first, principle second. This slide is correctly placed -- security awareness is critical even for L1.

### Slide 17 -- Anecdote/Story Break
**Strong:** Attention reset is good pedagogy.
**Fix:** Replace with something interactive rather than passive. A 1-minute poll: "Would you paste your homework code into ChatGPT? Your company's code? Why/why not?" This extends the security point through participation.

### Slide 18 -- Narrow vs General AI
**Decent:** The ANI/AGI distinction is important.
**Fix:** Keep it brief. The current framing is fine but 3 minutes is generous. One minute: "All existing AI is narrow. AGI is an open question. Here is what leading researchers disagree about." Link to the Davos 2026 debate (Hassabis vs Amodei vs LeCun) for color.

### Slide 19 -- What AI Does Better
**Strong:** Good list. "Reading 10,000 articles, analyzing X-rays 24/7" are vivid.
**Fix:** Good slide, keep. Could add: "AlphaZero mastered 1,500 years of chess knowledge in 4 hours."

### Slide 20 -- What Humans Do Better
**Strong:** The "AI = pattern recognition from data, human = goal-setting" summary is the key insight.
**Fix:** Lead with the summary, then support with 2 examples. Currently it reads as a list (context, causation, common sense, creativity, physical world, empathy, ethics) -- too many items at 3 minutes.

### Slide 21 -- Physical World
**Weak:** 2 minutes on robotics, drones, and autonomous driving is tokenism. Either spend 5 minutes or cut it.
**Fix:** Cut to one vivid example (Moravec's paradox: "ChatGPT writes an essay in a minute, but a robot still cannot fold laundry reliably"). Defer autonomous driving SAE levels to a later lecture.

### Slide 22 -- Summary
**Decent:** Three takeaways is the right number.
**Fix:** Good as is.

### Slide 23 -- Lecture 2 Preview
**Decent:** Teaser is fine.
**Fix:** Should also preview the ASSIGNMENT, not just the next lecture.

### Slide 24 -- Questions
**Weak:** "If no questions, ask a provocative one" is a fallback, not a plan. If students are engaged, there will be questions. If they are not, a provocative question will not save the situation.
**Fix:** Allocate 5 minutes, not 2. Plant specific discussion questions: "Will AI replace software engineers at Bauman within 10 years? Why or why not?" Better yet, use a live anonymous poll (Mentimeter, Telegram bot) for the final question.

---

## 6. Top 5 Recommendations

### 1. Flip the Structure: Demo First, History Last

Move the live demo and "AI Around Us" to the first 15 minutes. Compress history to 3-5 minutes, placed AFTER students have seen AI work. The goal of the first 10 minutes is to make students think "this is relevant to me right now."

Concrete action: Open with the ChatGPT/Claude hallucination demo (currently buried on slide 12) or a Quick Draw game. Then show the phone AI stats. THEN do a compressed history (pivot framing only: "AI meant something different before 2022, here is why").

### 2. Add a Real Interactive Segment (10 minutes)

Dedicate 10 minutes to students DOING something with AI. Options (pick one):
- **Everyone opens ChatGPT on their phone** and asks it a factual question about MGTU Bauman. Compare answers. Find hallucinations together.
- **Quick Draw tournament:** 3 rounds on phones, fastest classifier wins.
- **"Human or AI?" quiz:** 5 code/text/image samples, students vote via Telegram poll.

This replaces the second quadrant diagram (slide 10) and the detailed agent discussion (slide 13), which can move to L3.

### 3. Compress Model/Chat/Agent/App from 25 min to 10 min

For L1, students need to know that AI comes in different forms. They do NOT need quadrant diagrams, pattern/anti-pattern tables, or detailed "when to use" guides. Those belong in L3 (architectures).

L1 version: One slide with four columns, one vivid example each, 2 minutes per type. Total: 10 minutes. The comparison table becomes a handout.

### 4. Add an Assignment

End with a concrete task due before Lecture 2. Recommended (from our teaching-examples.md research):

> "Try 3 AI tools (ChatGPT, Claude, and one more of your choice). Ask each the SAME question related to your studies. Write a 1-page reflection: What surprised you? Where did AI fail? What would you use it for?"

This costs 5 minutes of lecture time and generates massive engagement. Students arrive at L2 with hands-on experience and opinions.

### 5. Expand "AI Around Us" to 15 Minutes and Make It the Lecture Core

This section has the best material and gets the worst treatment. Expand it:
- **Phone AI** (5 min): Neural Engine, Deep Fusion, Face ID, Google Lens 12B searches/month
- **AI you use daily** (5 min): YouTube 70% from AI, Netflix 80%, Gmail 15B spam blocked, Copilot 46% of code
- **Russian AI landscape** (3 min): 51% used AI, GigaChat/YandexGPT adoption, 520B rub market
- **Career connection** (2 min): 500K+ open positions, $206K salary, 4x productivity growth in AI-exposed industries

This is what makes students lean forward. Everything else is supporting material.

---

## Summary Verdict

The plan is built by someone who deeply researched the content but designed the lecture as a knowledge transfer document, not as a learning experience. The research files are excellent -- history-and-definitions.md, classifications.md, model-chat-agent-app.md, human-vs-ai.md, security-local-cloud.md, industry-examples.md all contain rich, well-sourced material. The problem is not the content. The problem is that the plan tries to present all of it, in textbook order, without enough moments where students DO something.

The plan violates its own research findings (teaching-examples.md) on at least 6 of 8 recommended principles. It prioritizes comprehensive coverage over pedagogical impact. For an introductory lecture, it is better to cover 60% of the material with high engagement than 100% of the material with passive listening.

**One-sentence verdict:** Great encyclopedia article, mediocre first lecture.
