---
id: s19a
type: assertion_visual
duration_min: 1.5
assertion: "Levels of autonomy of AI agents: a design decision, not a property of the model"
learning_goal: "5 levels from Feng/McDonald/Zhang + Human-in/on/out-of-the-loop as a design choice"
learning_outcomes: [LO1, LO4, LO7]
references: [feng-mcdonald-zhang-2025-autonomy]
visual:
  pattern: levels_with_loop_framings
  primary: "Eyebrow pill «AGENT» at the top. On the left — a ladder of 5 levels with English names (Operator → Collaborator → Consultant → Approver → Observer; level 5 in gold), bottom-up, level 5 on top. On the right — 4 framings of where the human sits, ordered top to bottom (issue #155 QA fix #193): Human-out-of-the-loop (≈lvl 5, gold) → Human-on-the-loop (≈lvl 3-4) → Human-in-the-loop (≈lvl 1-2) → Manual-override modes (any level) — mirroring the decreasing autonomy of the left ladder from top to bottom. Each card of the left ladder (issue #155 QA fix #192) contains an explicit statement of the user's role of the form «User: ...» instead of an abstract process description. At the bottom, a gold takeaway: «The level of autonomy is a product choice, not a property of the model»."
---

# Levels of autonomy of AI agents: a design decision, not a property of the model

## Assertion

Levels of autonomy of AI agents: a design decision, not a property of the model.

## Visual

Eyebrow pill «AGENT» in the top-left corner — the same pattern as s15/s16/s17/s18/s19. On the left, an Ocean rounded box with a ladder of five levels of autonomy (Feng / McDonald / Zhang, 2025), bottom-up: 1. Operator, 2. Collaborator, 3. Consultant, 4. Approver, 5. Observer (this level in gold), each with a product example. On the right, an Ocean rounded box with four framings, top to bottom: Human-out-of-the-loop (≈ lvl 5, gold), Human-on-the-loop (≈ lvl 3-4), Human-in-the-loop (≈ lvl 1-2), Override modes (any level + manual intervention). At the bottom, a gold callout: «The level of autonomy is a product choice, not a property of the model».

**Issue #155 Round 2 QA fixes (#192, #193):**
- **#192** — all 5 short role descriptions on the left ladder were reworded into the explicit form «User: ...», so that the card directly answers the question «what does the user do at this level»: 1. Operator — «User: approves every action»; 2. Collaborator — «User: works as an equal with the agent»; 3. Consultant — «User: sets the goal, edits the plan»; 4. Approver — «User: approves at checkpoints»; 5. Observer — «User: only receives the result».
- **#193** — the order of the right column (the human relative to the loop) was reversed to visually match the high-levels-on-top order of the left ladder. It was (top to bottom): in-the-loop → on-the-loop → out-of-the-loop → Override. It became: out-of-the-loop (≈lvl 5, top) → on-the-loop (≈lvl 3-4) → in-the-loop (≈lvl 1-2) → Override (last, since it applies at any level).

## Speaker notes

An important concept that we'll come back to all course long: the levels of autonomy of an agent. Feng, McDonald, and Zhang, in their 2025 work, propose five levels, characterized by the user's role. Not by the model's complexity — precisely by the user's role.

Level one — Operator. The user actively manages every step, the agent executes subject to approval. Example: Claude Code in «approve each command» mode — you see the command before it runs and press Enter every time.

Level two — Collaborator. The user and the agent work together, flowing between roles. Example: pair programming with Cursor, where you and the AI write in the same file and edit each other's suggestions.

Level three — Consultant. The user sets the goal, the agent proposes a plan and leads through the steps, the user corrects. Example: Devin receives a ticket «fix bug X», proposes a decomposition, you fix one step, and then Devin continues on its own.

Level four — Approver. The agent acts autonomously, the user approves the key nodes. Example: the agent assembles a PR, opens it, waits for your review; merge only after approval.

Level five — Observer. The agent works fully autonomously, the user only observes the outcome. Example: AutoGPT launched overnight with the task «assemble a competitive analysis» — you come back in the morning and read the report.

In parallel with these five, there is an older framing, widely accepted in safety engineering: where the human sits relative to the loop. Human-in-the-loop — the human approves every step, this is levels one-two. Human-on-the-loop — the human observes in real time and interrupts on deviation, this is roughly levels three-four. Human-out-of-the-loop — the human only reads the outcome, this is level five. And separately — override modes: at any level you can preserve the ability to take over manually on alarming signals.

The main point of the slide: the level of autonomy is a design decision, not a property of the model. The very same agent in Operator mode and in Observer mode is a different product, with different requirements for reliability, explainability, and interface. In the seminars we'll come back to this scale when choosing a level to fit a specific risk.
