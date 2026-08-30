---
id: s25b
type: reference
section: "Section 4. Agents"
assertion: "Real coding agents differ not in the quality of the model inside but in which harness slots are filled and where the agent physically lives"
learning_goal: "An overview of 4 coding agents through the harness frame; the conclusion «the difference is in the slots, not the model»"
learning_outcomes: [LO7]
chapter_ref: "§4.9 [for-slide-s25b]"
verify_day_of: true
---

# Visible content

## Title bar
«Coding agents through the harness frame»

## Body
[Four points on the harness map]
- **Claude Code** — a broad harness: memory, instructions, skills, subagents, MCP; a CLI tool
- **Aider** — thin, open-source: minimal harness, no subagents; a deliberate choice, not an "underdeveloped version"
- **Cursor** — an agent inside a desktop IDE (a VS Code fork); the form of integration — a separate axis
- **OpenHands** — self-hosted, MIT license, deploys locally/in Docker

[Gold callout, bottom]
The difference between the tools is **not in the quality of the model inside** but in which slots are filled and where the agent lives (terminal / IDE / self-hosted).

[Footer, italic]
*OpenHands — a working hypothesis for "OpenClaw" from the brief (a profile match, not a confirmed fact). By agent-harness-registry data; freshness quarterly.*

## Speaker notes

Let us gather the whole conceptual apparatus of the section — API and MCP, the agent loop, the distinction between a workflow and an agent, the five harness slots — into one practical reference point: how real coding agents of 2026 look through these concepts. We show each tool not through marketing but through the harness frame[1]: what harness it has by the map of five slots. Claude Code — a broad harness: its own memory between sessions, support for instruction files, built-in skills, full-fledged subagents with a separate context window, access to external systems through MCP; almost all slots are filled, which gives capabilities at the price of greater operational complexity. Aider — the opposite point: minimal file simplicity, no developed memory, no subagents, no formal skills; open-source, CLI-first. It demonstrates an important thesis: a thin harness is not an underdeveloped version of a full one but a deliberate working choice for tasks where a broad harness is not needed.

Cursor — the third point: not a terminal but a desktop editor with a built-in agent, a VS Code fork. It shows that the harness is not the only axis: the form of integration into the workflow, terminal versus IDE, is a separate architectural decision. OpenHands — a self-hosted autonomous platform with an MIT license, deploys locally or in Docker. By profile — open source, autonomy, MIT license — this is a likely candidate for the tool mentioned by ear as "OpenClaw"; this is a working hypothesis by profile match, not an established fact, and it is worth confirming. The general conclusion of the overview: the difference between real coding agents is not in the quality of the model inside them but in which harness slots are filled and where the agent physically lives. This is a direct application of the whole section map and of the same logic "do not take the most equipped option by default."

Sources:
[1] agent-harness-registry — an overview through the harness frame — source not confirmed; Claude Code/Aider/Cursor/OpenHands — vendor sites, verify day-of. [VFY: canonical URL not confirmed, present as data from an independent live-eval registry, not as a primary source]
