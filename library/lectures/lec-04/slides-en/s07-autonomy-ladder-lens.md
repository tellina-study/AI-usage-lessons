---
id: s06
type: assertion_visual
section: "Section 0. Introduction and methodological frame"
duration_min: 2
assertion: "The autonomy ladder A→D is a supporting lens (not the load-bearing axis); and the level of autonomy is a property of the mode, not the brand: one product lives on several rungs at once"
learning_goal: "A→D demoted lens + mode ≠ brand in one line (boundaries B↔C / C↔D compactly)"
learning_outcomes: [LO1, LO7]
chapter_ref: "§0.7 [for-slide-s06]"
visual_brief: "assertion_visual: on the left — a ladder of 4 rungs A→D in an Ocean rounded box (A autocomplete · B small tasks · C coding agent · D orchestrator), captioned \"a supporting lens, not the load-bearing axis\". On the right — ONE line \"mode ≠ brand\": one product on several rungs (Copilot A/B/C/D, Cursor A/B/C, Claude Code C→D) + 2 boundaries: B↔C (iterates on its own and runs tests) · C↔D (task from the tracker → PR). Gold — \"name the mode and the phase, not the logo\". Lucide icons (an up arrow for escalation)."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
Autonomy is a property of the mode, not the brand

## Body
[On the left — the ladder A→D in an Ocean rounded box, marked "a supporting lens"]

**The autonomy ladder** (a lens, not the load-bearing axis):
- **A — autocomplete** — completes the line; the human accepts each suggestion
- **B — small tasks** — a function/fix in a dialog; the human sets the task, reviews afterward
- **C — coding agent** — plans, edits many files, runs tests; the human reviews the PR and decides on the merge
- **D — orchestrator** — takes a task from the tracker, makes a PR; the human — strategy, approval, merge, production gate

[On the right — mode ≠ brand]

One product lives **on several rungs at once**: Copilot — A, B, C, and D; Cursor — Tab (A), Cmd-K (B), Composer (C); Claude Code — C, rising to D.

Two boundaries: **B↔C** — does it iterate on its own and run tests without you (yes → C). **C↔D** — where the task comes from and where the result goes (from the tracker → PR → D).

[Gold callout]
Reading rule: the higher the autonomy, the stricter the criterion "here the human is required" and the tighter the harness around the agent. The phrase "we use Copilot" **conveys** neither the level nor the phase — we name the **mode and the phase**, not the logo.

## Speaker notes

Let's give one supporting lens that we will use pointwise, mainly in the implementation phase. Within any phase AI can participate with varying independence — this is the autonomy ladder, four modes from autocomplete to an orchestrator-agent [2]. At level A — autocomplete: AI completes the line by context, the human accepts each suggestion. B — small tasks via chat: AI generates a function or fix, the human sets the task and reviews the result. C — coding agent: AI plans, edits many files, runs tests itself and iterates, while the human reviews the pull request and decides on the merge. D — orchestrator: AI takes a task from the issue tracker and makes a PR, sometimes with several agents, while the human is occupied with strategy, approval, and the production gate.

An important disclaimer: this ladder is a supporting lens, not the load-bearing axis of the lecture. The load-bearing thing is the cycle of artifacts and the phase practices we saw on the keystone; the ladder answers only the narrow question "how autonomously" and is silent about which phase and which artifact. The ladder's general rule: the higher the level of autonomy, the stricter and more explicit the criterion "here the human is required" must be, and the tighter the harness around the agent.

And one reading rule, without which the lecture will be misunderstood: the level of autonomy is a property of the working mode, not the tool brand [1]. One and the same product lives on several rungs at once. GitHub Copilot is autocomplete, and chat, and an agentic mode, and an "issue to PR" orchestrator; Cursor is Tab, Cmd-K, and the Composer agent; Claude Code by default is a coding agent and rises to orchestration [2]. Two operational boundaries: between B and C — does the tool iterate on its own and run tests without you; between C and D — where the task comes from and where the result goes. The practical consequence: the phrase "we use Copilot" conveys neither the level of autonomy nor the phase — that is set by how exactly and in which phase you apply it [1]. Therefore what you should name is the mode and the phase, not the logo: the practice matters, not the tool.
