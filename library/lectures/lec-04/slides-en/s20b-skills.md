---
id: s20b
type: assertion_visual
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "In development a skill pays off on a rare but repeatable multi-step procedure (running the checks, a throwaway database for an integration test, building the docs); what is needed every turn belongs in AGENTS.md, and a one-off is just a request in chat"
learning_goal: "Leading: skills as progressive disclosure of instructions (an on-demand layer over the permanent AGENTS.md) + an honest cross-vendor calibration"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.3b [for-slide-s20b]"
references: [agent_skills_std, claude_skills_docs]
verify_day_of: true
visual_brief: >
  assertion_visual: left (the bulk of the visual weight) — three genuinely common development skills as Ocean
  rounded cards with icons (terminal: run every check with one command · database: a throwaway Postgres/Kafka
  for an integration test · file-code: build the documentation from the code), plus a compact one-token-per-card
  example line. Right — the boundary "when a skill is not the answer" (four short non-wrapping bullets), the
  loading-mode mechanic (AGENTS.md always in context vs SKILL.md loaded only on call), and the honest
  cross-vendor limit: the format is open and confirmed in Codex CLI, but Cursor has no on-demand layer.
  Gold — the dividing rule between AGENTS.md, a skill, and a chat request.
interaction: none
---

# Visible content

## Title bar
In development, a skill pays off on a rare but repeatable procedure

## Body
[Left — WHAT DEVELOPERS ACTUALLY MOVE INTO A SKILL, three cards]

**Run every check with one command.** Linter → type check → tests (ruff/mypy/pytest or eslint/tsc/vitest) are invoked in a single call, instead of being reconstructed from scratch against this repository's conventions.

**A throwaway database for an integration test.** How to bring up a real Postgres or Kafka in a container for the duration of a run and tear it down after. The procedure is written down — the agent is not recalling the configuration from memory.

**Building documentation from the code.** Walk the project structure and its dependencies, assemble the README and the architecture decision records. Many steps, needed rarely — exactly the profile a skill exists for.

Example: `lint+type-check+test skill` · `testcontainers-docker skill` · `README Generator skill`

[Right — when a skill is NOT the answer]

• needed every turn (build, tests) — that is AGENTS.md
• a one-off task — just ask for it in chat
• one fact, not a procedure — a line in AGENTS.md
• "everything at once" — the model will not pick it

[Right — the loading mode, which is why the split works]
**AGENTS.md** — in context every turn; you pay for it always.
**SKILL.md** — loaded only on call; until then it costs zero.

[Honest limit]
*Honestly: the format is open (the Agent Skills standard) and confirmed in Codex CLI, but Cursor has no on-demand layer — there the rules are always active. "The tool supports skills" is worth double-checking.*

[Gold callout]
The dividing rule: needed every turn — into AGENTS.md; rare but detailed — into a skill; once — just say it in chat.

## Speaker notes

The permanent instruction layer — AGENTS.md — is read by the agent on every turn, and you pay for it in context always, even for an instruction needed once a quarter. A skill resolves exactly that trade-off: it is a folder with a SKILL.md file that is loaded only when the task matches it. Until it is called, it costs almost nothing.

The more important question is not the mechanism but what is actually worth moving into a skill in development. Practice reduces to three recognizable types. The first is running every check with one command: this repository's linter, type checker and tests are invoked in a single call rather than reconstructed by the agent from fragments of configuration. The second is a throwaway database for an integration test: how to bring up a real Postgres or Kafka in a container for the duration of a run and tear it down after. The third is building documentation from the code: walking the project structure and dependencies, assembling the README and the architecture decision records. All three share one profile — many steps, needed rarely.

The boundary matters as much as the list. A skill is not the answer when the procedure is needed every turn — that belongs in AGENTS.md; when the task is a one-off — just ask in chat; when it is a single fact rather than a sequence of steps — a line in the instructions is enough. Skills about "everything at once" are actively harmful: the agent picks a skill by its description, and a vague description means it either will not find the skill in time or will apply it in the wrong place. The same rule was formulated independently in recent software-engineering work: one skill, one coherent capability recognizable from its description.

The format is declared an open standard and is confirmed in Codex CLI, but Cursor has no on-demand layer — there the rules are always active. The phrase "the tool supports skills" is worth checking rather than taking on trust.
