---
id: s21
type: summary
duration_min: 3
assertion: "Checklist \"Which type of AI to choose\": 2 questions + a 2×2 quadrant"
learning_goal: "Climax of Section 3 — an operationalizable tool"
learning_outcomes: [LO1, LO4]
references: [anthropic-2024-effective-agents, google-2024-ai-agents-whitepaper, ng-2024-design-patterns]
visual:
  pattern: checklist_2_questions_quadrant
  primary: "Two questions large at the top; below, a large 2×2 quadrant with 4 types + 3 worked examples"
retrieval_moment: "s21 think-pair-share \"which quadrant does your AI tool belong to\""
---

# Checklist "Which type of AI to choose": 2 questions + a 2×2 quadrant

## Assertion

Checklist "Which type of AI to choose": 2 questions + a 2×2 quadrant.

## Visual

Two Ocean rounded box cards large at the top: Q1 "Do you need interaction with the user?" and Q2 "Do you need autonomous work with tools?". Below, a large 2×2 quadrant (surface 60% of the slide). Corners: top-left "Chat" (Q1=Yes, Q2=No), top-right "Agent" (Yes/Yes), bottom-left "Model" (No/No), bottom-right "Application (automation)" (No/Yes). On the quadrant, three worked-example dots: "Assembly line → Model", "Corp chat → Chat", "200 PDFs → Agent". The "200 PDFs → Agent" case in gold. Axis labels Q1/Q2 — inside the quadrant along the edge, not outside.

## Speaker notes

The climax of Section 3 — a practical tool. Two diagnostic questions whose answers unambiguously determine one of four implementation types.

Question one: do you need interaction with the user? If yes — the system has to talk with a person, take their clarifications, respond in real time — that's the chat and agent family. If no — the system runs autonomously on a trigger or a data stream — that's model and application in automation mode.

Question two: does the solution need to work with tools on its own? If yes — the system has to call an API, read files, run code, search the internet — that's agent and application in automation mode. If no — a single "input → output" step is enough for the system — that's chat and model.

We combine these into a quadrant. No interaction plus no tools — model. Yes interaction plus no tools — chat. Yes interaction plus yes tools — agent. No interaction plus yes tools — application in automation mode.

Here's an important caveat about "application". Applications, as we saw on the previous slide, come in two types. The first — applications with a user interface: Notion AI, Translate, Grammarly. They have a UI, and they land in the top corners of the quadrant — either in "Model" (if the user presses a button and gets a result in one step, without a dialogue), or in "Chat" (if there's a dialogue inside). The second type — automated applications with no user interface at execution time: an ETL pipeline with an AI classifier, a backend service that pulls new data once an hour and writes it to a table. That's exactly the bottom-right corner of the quadrant — "application in automation mode". Not an agent — there's no dialogue with the user and no planning decision loop. Not a model — there are tools, multi-step logic, and orchestration.

Let's run three cases. An assembly-line defect detector: interaction — no, tools — no, model. A corporate chat for going through a normative document: interaction — yes, tools — no, chat. Two hundred PDFs plus a table: interaction — yes, tools — yes, agent. The fourth corner — application in automation mode — via the example of an ETL pipeline with an AI classifier.

Coming back to the central question of the lecture: AI works where the task and the implementation type matched. Most of the pilots that rolled back never asked these two questions before deployment; instead they chose the tool by fashion. Two questions plus the quadrant — a simple but disciplining practice that radically lowers the risk of such a mismatch.

In the first-week seminar, students will apply this quadrant to their own cases. For now, a short exercise: think for thirty seconds about a tool you use regularly, and figure out its quadrant corner.
