---
id: s25
type: research_evidence
duration_min: 3
assertion: "\"Where to put it\" is the question \"will the text reach the agent, and what does it cost\"; five channels give five different answers, and three tools out of four independently converged on one mechanism — a declared path pattern"
learning_goal: "The evidence for case 1.3, part 1 — the delivery mechanics: a table of five channels (guarantee × context cost) and the convergence of three tools out of four on a declared path pattern. The breakdown of the cards and the target answer are on the next slide"
visual:
  pattern: research_and_answer_combined
  primary: "Top — a table of the five delivery channels: channel · when it arrives · guarantee · context cost; the 'guarantee' column reads top to bottom as 'yes — conditional — follows from the mechanism — NO — no', and the 'nested file' row is highlighted as the only one with a 'no' across every tool. Bottom — a table of the four tools: on the left a 'declared path pattern' column, filled in for three of them, on the right a 'just put a file in the folder' column (four different refusals). Under the table — a single line about the standard."
---

# Five channels — and where each stands on guarantees

## Assertion

"Where to put it" is the question "will the text reach the agent, and what does it cost"; five channels give five different answers, and three tools out of four independently converged on one mechanism — a declared path pattern.

## Visual

| Channel | When it reaches the agent | Guarantee | Context cost |
|---|---|---|---|
| The root instruction file and its `@` imports | at the start of every session | yes | paid always, including in sessions where it isn't needed |
| A rule with a declared path pattern | when the agent works with a file matching the pattern | conditional — but the trigger is declared explicitly, and the file sits where the tool always looks | zero until it fires |
| A comment next to the code | when the agent has opened that file | follows from the mechanism: if you're editing the function, you have read the file | zero on top of what was being read anyway |
| **A nested instruction file in a subfolder** | when the agent has read a file from that folder — if the tool can do that at all | **no, in none of the four tools** | zero until it fires |
| A separate document with no pointer to it | if the agent thinks to go there | no | zero — and zero delivery |

Verbatim from the documentation: files in subdirectories, "instead of being loaded at launch, are included when Claude reads files in those subdirectories"; an import by `@` path "is expanded and loaded into context at launch"; a rule with a pattern "fires when Claude reads files matching the pattern, and not on every tool call". The only way to check what is actually loaded is `/context`.

**Four tools, two columns:**

| Tool | A declared path pattern | "Just put a file in the folder" |
|---|---|---|
| Claude Code | `.claude/rules/*.md`, the `paths:` field | a nested `CLAUDE.md` — on demand; #2571 closed as "not planned" on 11.02.2026 |
| Cursor | `.cursor/rules/*.mdc`, the `globs:` field — "attached automatically when a matching file lands in context" | nested `AGENTS.md`; a Cursor employee acknowledged the bug on the forum |
| VS Code (Copilot) | `.instructions.md`, the `applyTo:` field — "automatically attaches the file whose pattern matched the file being edited" | nested `AGENTS.md` — the setting is marked experimental and **off by default** |
| Copilot CLI | — | no recursive discovery at all: #3051 open since 30.04.2026 |

A line under the table:

> The promise that "agents automatically read the nearest file in the directory tree" comes from the `agents.md` standard — that is a description of typical behavior, not a requirement on the tool. The promise goes unmet because nobody ever made it.

## Speaker notes

"The question 'where to put it' is really the question 'will the text reach the agent, and what does it cost'. The answer is mechanical, and it differs across the five channels.

The root file and every directory above it load at the start of the session: it always arrives, and we always pay. An import via the at-sign is expanded at launch too — it organizes the file, it does not save context; we did that arithmetic in the previous case. A comment in the code arrives when the agent has opened the file — and it has opened the file if it is editing the function. A nested file in a subfolder arrives only when the agent has read something out of that folder, and even then only if the tool can do that at all.

Next comes the fact this case exists for. Three tools, independently of one another, built the very same mechanism: a rule with a declared path pattern, sitting in one shared rules directory. In Claude Code that is the `paths` field, in Cursor `globs`, in VS Code `applyTo`. The wording is the same everywhere: the rule is attached when the agent works with a file matching the pattern. The trigger is declared explicitly, and the file sits where the tool always looks — you don't have to hope it wanders into a subfolder.

And 'just put a file in the folder', across those same four tools: closed as 'not planned', acknowledged as a bug by an employee, marked experimental and off by default, not implemented at all. Four tools, four different refusals.

The promise everyone leans on comes not from a tool but from the `agents.md` standard: agents automatically read the nearest file in the directory tree. That is a description of typical behavior, not a requirement. The promise goes unmet because nobody ever made it."
