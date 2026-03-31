# Subagent Delegation: First Session Analysis

**Date:** 2026-03-31
**Session scope:** Initial repo setup, MCP configuration, formal program (RPD) rewrite, semester roadmap creation

---

## Executive Summary

Out of 7 subagent delegations attempted in the first session, 2 failed completely, 1 was not attempted (correctly), and 4 succeeded with varying degrees of efficiency. The failures share a common root cause: subagents operate in a sandboxed environment and do not inherit the parent session's tool permissions or MCP server connections. The successes demonstrate that subagents excel at well-scoped content creation tasks where the required tools (Write, MCP calls) are available.

---

## Failures

### 1. Research Subagents (6 parallel -- all failed)

**What happened:** Launched 6 subagents in parallel, each tasked with researching one MCP server (workspace-mcp, gws, document-loader, local-rag, drawio, open-ontologies). The idea was sound -- parallelize independent research tasks to save time.

**How they failed:** Every single agent attempted WebSearch, WebFetch, and Bash calls. Every call was denied. Each agent tried between 8 and 12 tool calls, cycling through different approaches (WebSearch with different queries, WebFetch with different URLs, Bash with curl commands), before concluding they couldn't complete the task.

**The waste:**
- 6 agents x ~30 seconds each = ~3 minutes of compute
- Zero useful output from any agent
- Each agent produced a polite apology and suggested "granting web access permissions"
- All research had to be redone in the main conversation using WebSearch/WebFetch directly

**Root cause:** Subagents inherit a restrictive permission set from the parent session. They cannot use WebSearch, WebFetch, or Bash (for arbitrary commands). This is not documented anywhere obvious -- you discover it by watching agents fail.

**The irony:** The parallelization strategy was correct. If subagents had web access, this would have been the fastest way to research 6 independent topics. The architectural limitation turned an optimization into pure waste.

**Lesson:** Never delegate web research to subagents. Do it directly in the main conversation, or batch WebSearch/WebFetch calls in parallel from the orchestrator level.

### 2. Document Export Subagent (failed)

**What happened:** After researching MCP servers, tried to delegate a combined task: save raw markdown research notes to disk and ingest them into the local-rag index.

**How it failed:** The agent couldn't write files. It tried Bash (denied), Write tool (denied), and various other approaches. It made 44 tool calls over its lifetime, trying increasingly creative workarounds before finally giving up.

**The 44-call death spiral:** This is a pattern worth noting. When an agent can't do something, it doesn't fail fast. It keeps trying variations: different tool names, different parameter combinations, asking for help. This burns compute and time while producing nothing. A well-designed agent should recognize "I don't have the tools for this" after 2-3 attempts, not 44.

**Additional context:** The user ultimately rejected the entire approach anyway, preferring to restart the session for native MCP support rather than working around missing integrations. So even if the agent had succeeded, the output would have been discarded.

**Lesson:** File write permissions are also restricted for subagents. Check what tools a subagent can actually use before delegating work that requires filesystem access. Also: agents need better fail-fast behavior.

### 3. MCP Server Testing (not attempted -- correctly)

**What happened:** After restarting with MCP servers configured, the decision was made to test MCP tools directly in the main conversation rather than delegating to a subagent.

**Why this was correct:** MCP tools are session-level resources. After a restart, the main conversation has the MCP connections; a subagent spawned from it might or might not inherit them. Testing directly avoided the risk of another failed delegation and gave immediate feedback on whether each MCP server was working.

**Lesson:** When you need to verify that infrastructure works, do it directly. Don't add a layer of indirection that might mask the very failures you're trying to detect.

---

## Successes

### 4. Formal Program (RPD) Rewrite Subagent (succeeded, but slow)

**What happened:** Delegated a full rewrite of the university formal program document (RPD) to a subagent. The document had complex structure: multiple sections, tables with specific formatting, regulatory language.

**How it worked:** The agent used workspace-mcp's `modify_doc_text` tool to read the document structure, locate specific text passages, and replace them section by section. It made 68 tool calls over approximately 47 minutes.

**Why 47 minutes:** Each text replacement required a multi-step process:
1. Read the current document structure to find insertion points
2. Locate the exact text to replace (Google Docs API requires precise character ranges)
3. Execute the replacement
4. Verify the replacement took effect

For a document with dozens of sections and tables, this adds up fast. The Google Docs API is not designed for bulk document rewriting -- it's designed for targeted edits.

**What could have been faster:** Draft the entire document as markdown locally, then use `create_doc` or `import_to_google_doc` to create it in one shot. This would trade edit-in-place precision for speed. The tradeoff: you lose the document's revision history and any existing sharing settings.

**What went well:** The agent handled complex table structures correctly. It managed regulatory language and formatting requirements. It maintained consistency across sections. For a task that required understanding document structure AND making precise edits, delegation was the right call -- this would have been tedious to do manually from the orchestrator.

**Lesson:** Document rewriting via MCP is viable but slow. For full rewrites, consider the create-new-document approach. For targeted edits (a few sections), the modify-in-place approach is appropriate.

### 5. Gap Analysis + Roadmap + Folder Creation Subagent (succeeded -- cleanest delegation)

**What happened:** Combined three related tasks into one subagent:
1. Analyze gaps between the old formal program and new requirements
2. Generate a Mermaid diagram showing the semester roadmap
3. Create a "formal" folder in Google Drive and copy the old program into it

**How it worked:** 9 tool calls, approximately 2 minutes. The agent:
- Read the existing program via workspace-mcp
- Performed gap analysis against the requirements provided in the prompt
- Created the Drive folder and copied the file
- Generated the Mermaid diagram

**Why this worked so well:**
- All three tasks were related (same domain context)
- Each task was clearly defined with concrete outputs
- The tools needed (workspace-mcp, write) were available to the agent
- The total scope was small enough to avoid the agent losing focus
- No web access or restricted tools were needed

**This is the model for good delegation:** 2-3 related tasks, clear outputs, available tools, bounded scope.

**Lesson:** Bundling related tasks in one subagent is more efficient than splitting them. The agent maintains context across tasks, avoiding redundant reads and setup.

### 6. Semester Roadmap Drawio Subagent (succeeded)

**What happened:** Delegated creation of a `.drawio` XML file representing the semester roadmap as a visual diagram.

**How it worked:** 6 tool calls, approximately 2.5 minutes. The agent:
- Generated the draw.io XML with proper formatting
- Used the drawio MCP to open/validate the diagram
- Saved the file to disk

**Why this worked:** Diagram creation is a self-contained task with clear input (roadmap data) and clear output (an XML file). The agent didn't need external data or restricted tools. The drawio MCP provided the domain-specific capability.

**Lesson:** Diagram creation is an ideal subagent task. It's creative work with a concrete deliverable, and MCP tools handle the domain complexity.

### 7. Session Reflection Subagent (succeeded, but shallow)

**What happened:** Delegated writing the session reflection document to a subagent.

**First attempt:** The agent produced a reflection, but it was surface-level. It listed what happened without analyzing why things worked or failed, what the implications were, or what should change.

**After feedback:** The user asked for more depth, and the reflection was improved (or redone -- the point is the first pass wasn't good enough).

**Why the first pass was shallow:** The prompt likely said something like "write a reflection on today's session" without specifying the expected depth, the specific areas to cover, or examples of what "good" looks like. The agent did exactly what was asked -- it just wasn't asked for enough.

**Lesson:** Writing tasks require detailed prompts. Specify: expected length, areas to cover, level of analysis (descriptive vs. analytical), audience, and what "done" looks like. A subagent will default to the minimum viable interpretation of your prompt.

---

## Patterns

### When subagents work

| Factor | Description |
|--------|-------------|
| Tools available | The required tools (MCP, Write) are accessible to the agent |
| Clear scope | 2-3 related tasks with concrete deliverables |
| No web access needed | Agent doesn't need WebSearch, WebFetch, or unrestricted Bash |
| Domain context in prompt | All necessary context is provided in the delegation prompt |
| Bounded duration | Task can complete in under 5 minutes |

### When subagents fail

| Factor | Description |
|--------|-------------|
| Web research required | Agents cannot use WebSearch or WebFetch |
| Arbitrary file I/O needed | Bash and sometimes Write are restricted |
| MCP tools not inherited | Agent may not have access to session-level MCP connections |
| Vague prompt | Agent produces minimum viable output, not what you actually wanted |
| Too many tasks | Agent loses coherence or takes excessively long (>30 min) |

### Failure modes to watch for

1. **The polite spiral:** Agent tries 10+ tool calls that all fail, produces a polite apology, suggests permission changes. Wastes 30+ seconds with zero output.
2. **The 44-call death spiral:** Agent tries increasingly creative workarounds instead of failing fast. Wastes minutes of compute.
3. **The shallow pass:** Agent technically completes the task but at insufficient depth because the prompt didn't specify expectations.

---

## Delegation vs. Direct Work: Decision Guide

| Task type | Approach | Rationale |
|-----------|----------|-----------|
| Web research | Direct | Subagents can't access web tools |
| MCP server setup/testing | Direct | Need to verify infrastructure in the session that owns it |
| Git operations | Direct | Branch/commit/push are orchestrator-level concerns |
| Settings/config editing | Direct | Planning artifacts, orchestrator exception applies |
| Document editing via MCP | Delegate | Well-suited: clear scope, MCP tools available |
| Google Drive operations | Delegate | Well-suited: workspace-mcp handles complexity |
| Diagram creation | Delegate | Well-suited: self-contained creative task |
| Gap analysis / structured analysis | Delegate | Well-suited: bounded scope, clear output format |
| Writing / content creation | Delegate | Works, but requires detailed prompts for quality |
| Full document rewrite | Delegate with caution | Works but slow; consider create-new vs. edit-in-place |

---

## The Orchestration Rule: Honest Assessment

CLAUDE.md states: "Claude Code acts as planner and orchestrator only. ALL implementation work MUST be delegated to subagents."

### Where it was followed
- Formal program rewrite (delegated to subagent)
- Diagram creation (delegated to subagent)
- Gap analysis and folder creation (delegated to subagent)
- Reflection writing (delegated to subagent)

### Where it was violated
- MCP server installation via Bash (direct)
- `.claude/settings.json` editing (direct)
- Git branch/commit/push operations (direct)
- MCP server testing (direct)
- Web research after subagent failures (direct)

### Assessment
The violations fall into two categories:

1. **Infrastructure work** -- MCP setup, settings, git operations. These are covered by CLAUDE.md's exception for "repo scaffolding" and are impractical to delegate (subagents can't install npm packages or push to git).

2. **Compensating for subagent limitations** -- web research that was originally delegated but failed. This is a pragmatic response to discovering that subagents can't do the work.

The rule is sound for content work (documents, diagrams, analysis). It is impractical for infrastructure and tooling tasks. The exception clause should be expanded to explicitly cover: MCP setup, tool configuration, web research, and git operations.

---

## Recommendations for Future Sessions

1. **Never delegate web research.** Do it directly or not at all.
2. **Test one subagent before launching six.** The parallel research attempt would have failed gracefully if one agent had been tested first.
3. **Write detailed prompts for writing tasks.** Specify depth, areas, audience, length.
4. **Bundle 2-3 related tasks per subagent.** The gap-analysis agent showed this is the sweet spot.
5. **For document rewrites, evaluate create-new vs. edit-in-place** based on whether revision history matters.
6. **Add fail-fast guidance to subagent prompts.** Tell agents: "If you can't access a required tool after 2 attempts, stop and report what you need."
7. **Update CLAUDE.md** to explicitly list what the orchestrator may do directly (infrastructure, git, web research, config).
