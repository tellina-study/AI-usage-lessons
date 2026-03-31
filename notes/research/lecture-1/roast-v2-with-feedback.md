# Roast v2: Lecture 1 Slide Plan (with professor feedback)

**Date:** 2026-03-31
**Context:** Professor reviewed roast v1 and provided critical corrections about audience level, lecture format, and pedagogical priorities.
**Key insight:** The original roast itself made assumptions that need correcting — it treated the audience as beginners and recommended bootcamp-style assignments. This v2 corrects both the plan AND the roast.

---

## 1. What Works in the Plan (Given the Audience Knows ML)

The plan has several strengths that the original roast undervalued:

**The Model/Chat/Agent/App section (slides 9-15) is NOT over-scoped — it IS the lecture.**
The original roast recommended compressing this to 10 minutes. That was wrong. These students already know what ML is, what neural networks do, how supervised/unsupervised learning works. What they do NOT know is the new interaction paradigm: the difference between calling a model API, chatting with an LLM, deploying an agent, and using an AI-powered application. This is the core value-add of Lecture 1. It deserves 25 minutes — but restructured around a live demo, not around quadrant diagrams.

**Live demo ideas are present** — the plan mentions "Живое демо: задать вопрос ChatGPT/Claude" on slide 12 and a demo of photo AI processing on slide 6. The instinct is right; the placement and scope need fixing.

**The "PIVOT" framing on slide 1 is gold.** "AI перестал быть тем, что ещё не работает" — this is exactly the right framing for students who learned classical ML but may not fully grasp how 2022-2026 changed the landscape.

**Security/Samsung case (slide 16)** is a strong practical segment. Relevant, memorable, actionable.

**The "anecdote" breaks (slides 6, 17)** are good lecture design — attention resets are necessary in a 75-minute session. Polls work well as part of these breaks.

**Comparison table (slide 15)** is a solid summary artifact, especially as a handout.

---

## 2. What Is Condescending (Treating Them Like Beginners)

### 2.1 The Entire "What is AI?" Section (15 minutes)

Slides 1-5 spend 15 minutes explaining what AI is to students who have completed an ML course. This is the equivalent of starting a Data Structures course by explaining what a variable is.

Specific problems:
- **Slide 1 (History timeline, 4 min):** Turing 1950, Dartmouth 1956, AI winters — they know this. The ONLY valuable part is the LLM pivot framing. Everything before 2012 can be one sentence.
- **Slide 2 (Multiple definitions, 4 min):** Showing 4-5 academic definitions of AI to students who already built ML models is patronizing. They know what AI is — they have used it. The "ask students for their definition" prompt is fine, but the setup is wrong.
- **Slide 3 (Classification by task, 3 min):** Detection, segmentation, generation, prediction — they learned this in their ML course. No value in repeating it.
- **Slide 4 (Classification by modality, 2 min):** Numbers/sound/images/text — they know this.
- **Slide 5 (Other classifications, 2 min):** Supervised/Unsupervised/RL, Generative/Discriminative — this is literally their ML course syllabus. Repeating it is a waste.

**The fix is NOT to cut all of this.** The fix is to reframe it: "You know ML classifications. Here is the NEW classification axis that did not exist in your ML course: how you INTERACT with AI. Model vs Chat vs Agent vs App."

### 2.2 "AI Around Us" Framing

"Достаньте телефон. В нём AI. Вы уже пользуетесь AI каждый день — просто не замечаете."

These students absolutely notice. They use ChatGPT daily. They know their phone has AI. The "surprise reveal" framing ("you did not realize!") is condescending for this audience.

**Better framing:** "You use AI every day. But here is what CHANGED in the last 2 years that you might not realize" — then hit them with the scale numbers (900M ChatGPT users, 46% of code from Copilot, 70% YouTube watch time from recommendations) and the qualitative shift (from ML-as-tool to AI-as-colleague).

### 2.3 "What AI Cannot Do" (slide 8)

"AI не может открыть дверь" — this is a 2020 joke. In 2026, with Boston Dynamics and Figure robots, the physical world gap is narrowing fast. More importantly, these students are computer scientists — they care about computational limitations, not "can a robot open a door."

**Better framing:** Engineering perspective — where does AI fail in YOUR future systems? Hallucination in production, distribution shift, adversarial attacks, the alignment problem.

---

## 3. What Is the Real Value-Add

### 3.1 Model vs Chat vs Agent vs App — THE Core Content

This is what they do NOT know from their ML course. The distinction between:
- **Model:** You have a trained YOLO, Whisper, or Stable Diffusion. You call it via API. Deterministic-ish, controlled, specialized.
- **Chat:** You talk to ChatGPT/Claude in natural language. Non-deterministic, flexible, general-purpose. Hallucination risk.
- **Agent:** AI that plans, uses tools, iterates. Claude Code, Devin. Multi-step, semi-autonomous.
- **App:** AI is invisible inside a product. Yandex Navigator, Google Translate, Copilot. User does not think about AI.

This taxonomy is not in any ML textbook. It emerged from practice in 2023-2025. It is immediately useful for every student's next project.

### 3.2 Live Demo as Centerpiece

The demo should show the SAME task attempted three different ways:
1. **Model:** Make a raw API call to a model via OpenRouter (show the JSON, the response, the raw output)
2. **Chat:** Ask the same question in a web chat interface (show the conversational wrapper, the formatting, the hallucination risk)
3. **Agent:** Give the same task to a coding agent (show it planning, calling tools, iterating)

This makes the Model/Chat/Agent distinction visceral, not theoretical. Screenshots work if live fails.

### 3.3 The Patterns/Antipatterns of Chat

Once the demo establishes the three modes, the chat segment becomes a masterclass in prompting patterns vs antipatterns — demonstrated live on the chat interface. This is practical knowledge they will use tomorrow.

---

## 4. Proposed Restructuring

### New Lecture Flow (75 minutes)

| # | Segment | Time | Notes |
|---|---------|------|-------|
| 1 | **Ice breaker with live demo** | 2 min | Something attention-grabbing that IS a demo. Ask AI a question about Bauman, show it working AND confidently failing (hallucination). Instant hook + sets up the "AI is powerful but unreliable" theme. |
| 2 | **About me** | 2 min | 3 points max. Why you care about AI in engineering practice. |
| 3 | **Quick poll** | 2 min | "Who uses AI daily? What for?" Show of hands or Telegram poll. This is not a reveal ("you use AI!") — it is a data collection ("what do YOU use it for?"). Part of the ice breaker flow. |
| 4 | **"What changed in 2 years"** | 5 min | NOT a history lecture. The PIVOT: "Your ML course taught you about models. Here is what happened since: LLMs, ChatGPT at 900M users, Copilot writing 46% of code, agents that code autonomously. The way we INTERACT with AI changed." This replaces the entire 15-minute history/definitions section. |
| 5 | **Quick classification refresh + new axis** | 5 min | 1 minute: "You know ML classifications — by task, by modality, by learning type. Quick refresh." 4 minutes: "Here is the NEW axis that your ML course did not cover: interaction type. Model / Chat / Agent / App. This is what this lecture is about." |
| 6 | **CORE: Model vs Chat vs Agent vs App** | 25 min | The centerpiece. Live demo for each type (or screenshots as backup). Show the SAME task solved three ways (Model API call, Chat conversation, Agent multi-step). Then App as the "invisible AI" category. Patterns and antipatterns for chat usage demonstrated live. |
| 7 | **Security: local vs cloud** | 5 min | Samsung case. "What happens to your data." Practical and memorable. |
| 8 | **Anecdote + poll** | 3 min | Attention reset. A fun story (AlphaZero mastered chess in 4 hours but cannot pour water). Poll: "Would you paste your company code into ChatGPT?" Extends the security point through participation. |
| 9 | **Human vs AI: engineering perspective** | 10 min | NOT philosophical (Narrow vs General AI debate). Instead: "Where to put AI in your system, where not to." AI excels at: pattern recognition, scale, speed. Humans excel at: goal-setting, context, causation. Engineering implication: AI is a component, not a replacement. Moravec's paradox as a design principle. |
| 10 | **Stats and scale** | 5 min | Market numbers, career data (500K+ open positions, $206K avg salary), Russian AI landscape. The "why this matters for YOUR career" segment. |
| 11 | **Wrap-up + preview of Lecture 2** | 5 min | 3 takeaways. Lecture 2 teaser (transformers, tokens, prompting). No assignment — action happens in seminars. Reserve 2 min for questions. |
|  | **TOTAL** | **69 min** | 6 min buffer for overruns and organic Q&A |

### Key Differences from Original Plan

1. **No 15-minute history/definitions section.** Replaced by 5-minute "what changed" pivot.
2. **Classifications are a 1-minute refresh**, not a teaching segment. The new axis (interaction type) is the teaching point.
3. **Model/Chat/Agent/App keeps its 25 minutes** but restructured around a live demo, not quadrant diagrams.
4. **"AI Around Us" is dissolved** — its best content (stats, scale, career) moves to segment 10; its "phone AI" content is unnecessary for this audience.
5. **Human vs AI reframed** from philosophical to engineering: where to put AI in your system.
6. **No homework or task recommendations.** This is a university lecture. Hands-on work happens in seminars.
7. **Polls integrated into ice breaker and anecdote breaks**, not standalone segments.

---

## 5. Slide-by-Slide: Keep / Cut / Modify

| Slide | Original Content | Verdict | Reasoning |
|-------|-----------------|---------|-----------|
| 0 | Ice breaker — Google interview quote | **MODIFY** | Replace passive quote with live demo. Ask AI something about Bauman, show it hallucinating confidently. 2 minutes, active, sets up the entire lecture theme. |
| 0.1 | About me | **KEEP** | 3 points, no CV. Add "why AI matters to me in practice." |
| 1 | History timeline (Turing to LLM) | **MODIFY heavily** | Cut everything before 2012 to one sentence. Keep ONLY the LLM pivot framing. Merge into the "what changed in 2 years" segment (5 min total, not 4 min for history alone). |
| 2 | Multiple definitions of AI | **CUT** | They know what AI is. Do not show 4 academic definitions to students who have taken an ML course. The "ask students" prompt moves to the poll in segment 3. |
| 3 | Classification by task | **CUT from main flow** | They learned this. One-sentence reference: "You know ML classifications — by task, by modality, by learning type." |
| 4 | Classification by modality | **CUT from main flow** | Same reason. Fold into 1-minute refresh. |
| 5 | Other classifications (ANI/AGI, Supervised/RL, Gen/Disc) | **CUT** | This is their ML course syllabus. Do not repeat. ANI/AGI mention moves briefly to Human vs AI segment. |
| 6 | AI in this room — phone AI | **MODIFY** | Drop the "surprise reveal" framing. These students know. Reframe: "Here is what CHANGED — the scale and speed." Best stats move to segment 10 (stats and scale). |
| 7 | AI in numbers — market stats | **MOVE** | Move to segment 10 (stats and scale). Good content, wrong position. |
| 8 | What AI cannot do (yet) | **MODIFY** | Drop the "AI cannot open a door" joke. Reframe for engineers: where does AI fail in production systems? Hallucination, distribution shift, adversarial inputs. Merge into Human vs AI engineering segment. |
| 9 | Quadrant diagram 1 (control vs determinism) | **MODIFY** | The quadrant concept is fine as a REFERENCE slide but should not lead the section. Lead with the live demo, then show the quadrant as a framework to explain what they just saw. |
| 10 | Quadrant diagram 2 (single-step vs multi-step) | **CUT** | Two quadrant diagrams is framework overload. One is enough. The second axis can be mentioned verbally. |
| 11 | Model (standalone) | **KEEP + demo** | Good content. Add: show a raw OpenRouter API call. Make it concrete: "This is what calling a model looks like. No chat, no agent. Just input-output." |
| 12 | Chat (dialogical AI) | **KEEP + expand demo** | This becomes the demo centerpiece. Show the SAME task from the model slide, now in chat. Demonstrate prompting patterns and antipatterns live. Hallucination demo stays. |
| 13 | Agent | **KEEP + demo** | Show a coding agent solving a task (Claude Code or similar). The plan-code-test-fix-deliver cycle. Can be a recording or screenshots if live is risky. |
| 14 | AI Application | **KEEP** | Yandex Navigator example is perfect. "AI as invisible helper" framing works. |
| 15 | Comparison table | **KEEP as handout** | Good summary. Better as a printed/digital handout than a lecture slide. If kept as slide, make it the "landing" after the demo. |
| 16 | Local vs cloud / security | **KEEP** | Samsung case is gold. Lead with the story, then the principle. |
| 17 | Anecdote / story break | **MODIFY** | Make it interactive: combine with a poll. "Would you paste your company code into ChatGPT?" extends the security point. AlphaZero story as the attention reset. |
| 18 | Narrow vs General AI | **CUT as standalone** | Merge into Human vs AI segment as a 30-second mention: "All current AI is narrow. AGI is an open research question." Do not spend 3 minutes on this for students who know ML. |
| 19 | What AI does better | **MODIFY** | Reframe from "interesting facts" to engineering guidance: "Where to deploy AI in your system." Pattern recognition at scale, 24/7 operation, speed. |
| 20 | What humans do better | **MODIFY** | Reframe to engineering: "Where NOT to deploy AI." Goal-setting, context understanding, ethical judgment, novel situations. The AI-as-component-not-replacement conclusion. |
| 21 | Physical world | **CUT** | 2 minutes on robotics is tokenism. Moravec's paradox as a one-liner in the Human vs AI segment is enough. |
| 22 | Summary — 3 takeaways | **MODIFY** | New takeaways: (1) The way we interact with AI changed — Model/Chat/Agent/App is the new axis. (2) Each type has patterns and antipatterns — choosing wrong costs time and security. (3) AI is an engineering component, not magic — know where to put it. |
| 23 | Lecture 2 preview | **KEEP** | Transformers, tokens, prompting. Good teaser. Remove any assignment reference. |
| 24 | Questions | **KEEP + expand** | Allocate 3 minutes minimum. Provocative question backup: "Will agents replace junior developers within 5 years?" |

**Score: 6 KEEP, 9 MODIFY, 5 CUT, 3 MOVE/MERGE, 2 CUT as standalone**

---

## 6. Top 5 Changes (Revised)

### 1. Kill the Intro-to-AI Section, Replace with "What Changed"

The 15-minute history/definitions/classifications section (slides 1-5) assumes beginners. These are not beginners. Replace with a 5-minute "what changed since your ML course" segment that leads directly into the Model/Chat/Agent/App taxonomy. The pivot framing ("AI went from tool to colleague") is the only history they need.

### 2. Make the Live Demo the Centerpiece

The same task, three ways: raw model API call, chat conversation, coding agent. This is the lecture's WOW moment. It makes the Model/Chat/Agent distinction visceral. The ice breaker should ALSO be a demo (AI hallucinating about Bauman). Screenshots as backup if tech fails.

### 3. Reframe Everything for Engineers, Not Consumers

- "AI Around Us" becomes "Stats and Scale" — they know AI is around them, show them the numbers that matter for their careers
- "What AI Cannot Do" becomes "Where NOT to Put AI in Your System"
- "Human vs AI" becomes an engineering design principle, not a philosophical debate
- "Narrow vs General AI" becomes a 30-second mention, not a 3-minute segment

### 4. No Assignments, No Tasks

This is a university lecture. Hands-on work happens in seminars. The original roast's recommendation to add homework ("try 3 AI tools and write a reflection") was wrong — it imposed a bootcamp model onto a university format. Cut all task recommendations.

### 5. Integrate Polls into Natural Breaks, Not as Standalone Segments

Polls are great for engagement but should be part of ice breakers and anecdote breaks (razryadka), not freestanding interactive segments. The opening poll ("who uses AI daily? for what?") is part of the ice breaker flow. The mid-lecture poll ("would you paste company code into ChatGPT?") is part of the anecdote/security break.

---

## Summary Verdict (Revised)

The original roast correctly identified that the plan reads like a textbook, not a lecture experience. But the roast itself made two critical errors: (1) it assumed the audience were beginners who need to be shown that AI exists, and (2) it recommended bootcamp-style assignments for a university lecture format.

With the professor's corrections, the picture clarifies: the Model/Chat/Agent/App section is NOT over-scoped — it is the entire point. The live demo is NOT a nice-to-have — it is the centerpiece. The history/definitions section is NOT too long — it is the wrong content entirely for this audience.

**Revised one-sentence verdict:** The plan has the right centerpiece (Model/Chat/Agent/App) but buries it under 15 minutes of content the audience already knows, and needs a live demo to make the taxonomy come alive.
