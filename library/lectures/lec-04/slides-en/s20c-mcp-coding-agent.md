---
id: s20c
type: assertion_visual
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "MCP removes the human bridge between the agent and external systems, but it gives not the system's whole interface — only a curated subset of its API and commands; and that same single connection concentrates two corners of the lethal trifecta at once, a risk closed by read-only-by-default"
learning_goal: "Leading: MCP extends the agent beyond the file system (GitHub / Playwright / filesystem MCP) + the bridge to security (the lethal trifecta through one server)"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.3c [for-slide-s20c]"
references: [github_mcp_server, playwright_mcp, willison_lethal_trifecta]
verify_day_of: true
visual_brief: >
  schema_architecture: the coding agent on the left with its built-in access (files + shell); three MCP server
  cards to the right (GitHub MCP: issues/PRs/builds by selectively enabled toolsets · Playwright MCP: a
  structural element tree instead of a screenshot · Filesystem MCP: a class of servers reaching directories
  outside the working copy), joined by one dashed rail above the cards. Below — the "subset" bar: the system's
  full interface vs the narrower MCP toolset. Then an explicit risk → mitigation pair: the lethal trifecta
  (data + a channel out + untrusted content, two corners in one connection, the documented GitHub MCP
  exfiltration) → the three mitigations. Gold — read-only by default; write access is a deliberate per-task
  decision.
interaction: none
---

# Visible content

## Title bar
MCP removes the human bridge — at the cost of narrower system access

## Body
[Top — the agent and three MCP servers]

**AGENT** — built in: files + shell.

**GitHub MCP**: issues, pull requests, builds — by toolsets that are enabled selectively.

**Playwright MCP**: the browser — a structural tree of elements instead of a screenshot; clicks, fills in forms.

**Filesystem MCP**: a class of servers — access to directories OUTSIDE the working copy (a neighboring repo, a shared disk).

[Middle — MCP is narrower than direct access]
The system's full interface: its API and its terminal command. The MCP toolset — *a subset, not the whole interface.*

The server publishes a curated set of tools rather than the system's whole interface: what is not in the set is out of reach for the agent, even if the system can do it. And every tool schema occupies context permanently — so where the agent already has a shell, a narrow command is often cheaper than an MCP call.

[Bottom left — the danger: one connection, two corners out of three]
The lethal trifecta: access to data + a channel out + untrusted content. One server usually grants the first two at once, and the third arrives through the same channel. Documented: instructions hidden in public issues exfiltrated private-repository data through the pull requests the agent created.

[Bottom right — what closes it]
1. Read-only by default — write tools are skipped, even if the agent asked for them.
2. Write access is opened for a specific task, as a separate decision, not an out-of-the-box setting.
3. The fewest servers connected — fewer corners, less context.

[Gold callout]
This is a risk, not a convenience: read-only by default, and write access opened deliberately and per task.

## Speaker notes

Without MCP the agent sees only the files of the working copy and the terminal. That is enough for code, but not for anything outside the repository: the issue tracker, a live browser, the build system. While there is no bridge, the engineer is the bridge — carrying data across by hand. MCP removes that: on connection the server publishes the list of its tools, and the agent calls them in the same loop it uses for built-in ones.

There is a cost here that is discussed less often. The server publishes not the system's whole interface but a curated set of tools. What is not in the set is out of reach for the agent even if the system itself can do it: the GitHub MCP toolset is a subset of what is reachable through the GitHub API and through the gh command in the terminal. On top of that, every tool schema occupies context permanently, from the moment of connection rather than at call time. So where the agent already has a terminal, a narrow command is often cheaper than an MCP call, and the set of active servers is worth keeping minimal.

Security deserves its own point, and here it is important not to get the sign wrong. The lethal trifecta is access to data, a channel out, and untrusted content; what is dangerous is precisely their combination. One server usually grants the first two at once, in a single connection, and the third arrives through the same channel as soon as the agent reads someone else's issue. That is a risk, not a convenience: a concentration of access, not a defense. A documented case: instructions hidden in public issues made the agent leak private-repository data through the pull requests it created.

This is closed in three steps, and their order matters. Read-only by default: write tools are skipped even if the agent asked for them. Write access is opened for a specific task as a separate decision, not as an out-of-the-box setting. And the fewer servers are connected, the fewer corners of the trifecta and the less permanent context you carry.
