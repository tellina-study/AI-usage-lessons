# User Corrections and Behavioral Patterns

Analysis of every course correction the user made during the 2026-03-31 setup session.
Each correction reveals a preference that should become a permanent behavioral rule.

---

## Correction 1: "No, you should work with real files from Drive"

### Context

The assistant needed to test `document-loader` MCP server. Instead of fetching actual documents from Google Drive, it attempted to create a synthetic DOCX file using `python-docx` -- a throwaway test document with fake content.

### What Was Wrong

The user has a Google Drive folder full of real course documents (normative PDFs, lecture materials, program descriptions). Testing with a synthetic file proves nothing about the actual workflow. It proves the tool can read *a* DOCX, not that it can read *the user's* documents. The gap between "tool works on test data" and "tool works on production data" is where real problems hide -- encoding issues, large file sizes, complex formatting, embedded images, Cyrillic text.

### The User's Actual Need

Validate the toolchain against real content. If document-loader chokes on a specific PPTX from Drive, that's a finding. If it handles a synthetic hello-world DOCX, that's nothing.

### Preference Extracted

**Always work with real production data.** Never create synthetic fixtures when real data is available. The point of testing is to find real problems, not to demonstrate capability in a vacuum.

### Side Effect

The user provided their Google email (`kzlevko@gmail.com`), which enabled the OAuth flow for `workspace-mcp`. The correction didn't just fix behavior -- it unblocked the next step.

---

## Correction 2: "No, I will restart Claude Code now"

### Context

After MCP servers failed to appear in `claude mcp list`, the assistant started building workarounds: `curl` commands to hit MCP server HTTP endpoints directly, Python scripts to simulate tool calls, manual JSON-RPC payloads piped through stdio. The assistant was treating the MCP integration as broken and routing around it.

### What Was Wrong

The MCP servers weren't broken. The configuration was in the wrong file (`.claude/settings.json` instead of `.mcp.json`). The correct fix was to put the config in the right place and restart Claude Code. Instead of diagnosing the root cause, the assistant built an elaborate scaffolding of workarounds that would need to be thrown away once the real integration worked.

### The User's Actual Need

A working MCP setup. Not a simulation of one. The user understood that restarting with correct config would solve the problem. The assistant was burning time on a dead-end approach.

### Preference Extracted

**Fix root causes, don't build workarounds.** If a tool isn't working, diagnose why and fix it. Don't construct a parallel system that bypasses the broken part. Workarounds accumulate technical debt and mask real problems.

### Broader Principle

The user has a low tolerance for "creative" solutions to configuration problems. The right answer to "MCP server not loading" is never "let me call it via curl instead." It's "let me figure out why it's not loading."

---

## Correction 3: "It's not a real result -- save and index documents, create semester roadmap..."

### Context

The assistant had successfully connected all MCP servers, listed their tools, made test calls, and presented a summary: "All 6 MCP servers operational, X tools available." The assistant treated this as the end of the setup phase.

### What Was Wrong

Having working MCP servers is the *starting point*, not the deliverable. The user didn't ask for MCP infrastructure. The user asked for a system that manages course materials. MCP servers are plumbing. The user wants water.

The assistant's report was essentially: "I installed the pipes, they don't leak, here's a list of pipe diameters." The user wanted: "Here are your documents, indexed and searchable. Here's a semester roadmap. Here's the lecture flow diagram."

### The User's Actual Need

Tangible artifacts:
- Documents pulled from Drive and saved locally
- RAG index populated with real content
- Semester roadmap reflecting actual lecture topics
- Diagrams showing course structure

### Preference Extracted

**Infrastructure is invisible. Artifacts are the deliverable.** Never present "system X is configured" as a result. The result is what the system *produced*. Configuration is a prerequisite, not an achievement.

### Impact on Session

This correction pivoted the entire session from "setup and verify" mode to "use the tools and produce outputs" mode. Everything that followed -- document ingestion, diagram creation, gap analysis -- came from this redirection.

---

## Correction 4: "Where are the raw docs before ingestion? Why aren't they saved?"

### Context

The assistant used `workspace-mcp` to read Google Docs and then immediately passed the content to `local-rag`'s `ingest_data` tool (which accepts raw strings). The documents went straight from Google API response into LanceDB vector storage. No intermediate files existed on disk.

### What Was Wrong

The pipeline was: Google Drive --> API response (in memory) --> RAG index (in lancedb/). If the RAG index gets corrupted, deleted, or needs rebuilding, there's no local source to re-ingest from. The user would have to re-fetch everything from Drive. Worse: there's no way to inspect what was actually ingested, diff it against the source, or track changes over time.

### The User's Actual Need

A traceable data pipeline:
1. Fetch from Google Drive
2. Save raw file to `catalog/exports/docs/` (this step was missing)
3. Ingest from saved file into RAG
4. File on disk serves as cache, audit trail, and re-ingestion source

### Preference Extracted

**Every data pipeline must save intermediate artifacts.** Raw source files must exist on disk before any processing. The repo layout already has `catalog/exports/docs/` for exactly this purpose -- the assistant ignored it.

### Underlying Principle

**Traceability.** The user thinks in terms of data lineage: where did this come from, when was it fetched, can I see the original? Ephemeral in-memory processing violates this. If it's not on disk, it's not real.

---

## Correction 5: "Why don't you save the raw .drawio file for viewing and editing?"

### Context

The assistant created a draw.io diagram using the `drawio` MCP server. The diagram opened in a browser for viewing. But no `.drawio` XML file was saved to the repository. The diagram existed only as a transient browser session.

### What Was Wrong

A diagram that isn't saved as a file:
- Can't be version controlled
- Can't be edited later without recreating it
- Can't be referenced from other documents
- Disappears when the browser tab closes
- Violates the repo layout (which has `diagrams/` specifically for this)

### The User's Actual Need

A `.drawio` file saved in `diagrams/lecture-flows/` that can be:
- Committed to git
- Opened in draw.io desktop or web editor
- Updated when lecture content changes
- Exported to PNG/SVG for embedding in slides

### Preference Extracted

**Every artifact must be saved to the repo in an editable source format.** Browser views, terminal outputs, and API responses are ephemeral. The repo is the source of truth. If it's not committed, it doesn't exist.

### Pattern

This is the same underlying principle as Correction 4 (save raw docs) but applied to outputs instead of inputs. Both directions of the pipeline -- source materials coming in, and generated artifacts going out -- must leave files on disk.

---

## Correction 6: "Why don't you auto-renew ingestion after doc changes?"

### Context

Documents were ingested into the RAG index once, manually. When asked about keeping the index current, the assistant had no answer -- there was no mechanism for detecting changes and re-ingesting.

### What Was Wrong

A one-time manual operation is a demo, not a system. The user's documents will change. New lectures will be added. Normative documents will be updated. If every change requires the user to manually trigger re-ingestion, the system has no value over just reading the files directly.

### The User's Actual Need

An automated pipeline:
1. `sync-library` detects changes in Google Drive
2. Changed files are re-exported to `catalog/exports/`
3. Changed files are re-ingested into RAG
4. This happens as part of the daily cycle, not as a manual step

### Preference Extracted

**Build systems, not one-off operations.** Every manual action should be evaluated: "Will this need to happen again?" If yes, automate it. The user thinks in pipelines and cycles (the daily cycle is literally defined in CLAUDE.md), not in isolated actions.

### Implications

This means:
- Skills should be idempotent and re-runnable
- The `sync-library` skill should trigger downstream re-ingestion
- Hooks should connect pipeline stages automatically
- Manual "run this once" operations are acceptable only as prototypes for automation

---

## Correction 7: "Yes, the formal program needs to reflect the real lectures and content"

### Context

The assistant performed a gap analysis comparing the old formal course program (from the university documentation) with the new V2 lecture content. The analysis showed near-zero overlap -- the formal program described completely different topics. The assistant then asked the user what to do next.

### What Was Wrong

The answer was obvious from context. If the formal program doesn't match the actual lectures, and the user confirmed the V2 content is correct, then the formal program needs to be rewritten to match. Asking "what should we do?" when the logical next step is self-evident wastes the user's time and signals that the assistant isn't thinking autonomously.

### The User's Actual Need

For the assistant to take the obvious next step without asking. The gap analysis was not an end in itself -- it was a diagnostic that pointed to a clear action (rewrite the formal program).

### Preference Extracted

**When the next step is logically obvious, take it.** Don't ask for permission to do what clearly needs doing. The user wants an autonomous collaborator, not a tool that stops after every step to ask "now what?"

### Calibration Note

This doesn't mean "never ask." It means: distinguish between situations where multiple valid paths exist (ask) and situations where there's one clear path (act). "The program is wrong, should I fix it?" is not a real question when fixing it is the entire point of the analysis.

---

## Correction 8: "Why so short findings? You have so many troubles -- go over each step and tool..."

### Context

The first reflection document was a brief summary with bullet points: "MCP setup had issues," "some tools worked better than others," "need to improve automation." High-level, shallow, executive-summary style.

### What Was Wrong

The session had 6+ hours of detailed, painful, specific experiences. Configuration files in wrong locations. OAuth flows that silently failed. Tools that returned empty results. Workarounds that had to be abandoned. Each of these is a specific, valuable lesson. Collapsing them into "MCP setup had issues" throws away all the specifics.

### The User's Actual Need

Deep, honest, specific analysis. Not "we had some problems with MCP" but "workspace-mcp OAuth silently expired after 47 minutes, causing the batch document fetch to fail at item 12 of 15 with no error message, requiring a full re-authentication and restart of the ingestion pipeline from scratch."

### Preference Extracted

**Depth over brevity. Specifics over summaries.** When reflecting or analyzing, go deep. Name the specific tool, the specific error, the specific workaround, the specific consequence. The user reads these documents to learn and to prevent repeating mistakes. Vague summaries teach nothing.

### Impact

This correction led to the creation of separate detailed reflection files (the sibling documents in this directory), each covering a specific topic in depth. This document itself is a product of this correction -- thorough analysis of every correction, not a bullet list.

---

## Meta-Patterns: What the User Actually Values

These eight corrections, taken together, reveal a coherent philosophy. The user is not making random complaints. There is a consistent worldview underneath.

### 1. Real Work Over Demonstrations

Corrections 1, 3. Don't test with fake data. Don't present infrastructure as the deliverable. The user measures value by artifacts produced (documents saved, diagrams created, programs rewritten), never by systems configured or tools verified.

**Rule:** After any tool interaction, ask: "What tangible artifact did this produce?" If the answer is "proof that the tool works," that's not enough.

### 2. Fix Root Causes, Don't Build Workarounds

Correction 2. When something doesn't work, the correct response is diagnosis, not circumvention. Workarounds are technical debt. They obscure the real problem and create parallel maintenance burdens.

**Rule:** If a tool/config/integration isn't working, spend time understanding WHY before writing any workaround code. Restarting, reconfiguring, or reinstalling is almost always faster than building a bypass.

### 3. Every Artifact Must Be a File in the Repo

Corrections 4, 5. Inputs (source documents from Drive) must be saved to `catalog/exports/`. Outputs (diagrams, generated content) must be saved to their designated directories. In-memory processing and browser-only views are ephemeral and unacceptable.

**Rule:** Before closing any task, verify: are all inputs saved as files? Are all outputs saved as files? Are they in the correct repo directory? Can they be version-controlled?

### 4. Build Systems, Not One-Off Operations

Correction 6. Any action that will need to happen again must be automated. Skills should be idempotent and composable. The daily and weekly cycles in CLAUDE.md are the user's mental model -- everything should fit into a repeatable pipeline.

**Rule:** After any manual operation, ask: "Will this need to happen again?" If yes, either automate it immediately or create an issue to automate it.

### 5. Act When the Path Is Clear

Correction 7. Don't ask for permission when there's one obvious next step. The user hired an autonomous collaborator, not a step-by-step wizard that needs a button click between every action.

**Rule:** If the analysis points to a single clear action, take it. Reserve questions for genuine decision points where the user's preference between multiple valid options is unknown.

### 6. Go Deep, Not Shallow

Correction 8. Summaries are for executives. This user is a practitioner. They want specifics: which tool, which error, which workaround, which consequence. Shallow analysis is worse than no analysis because it creates an illusion of reflection without actual learning.

**Rule:** When documenting, reflecting, or analyzing, include specifics. Name tools, quote errors, describe exact sequences. If a section could apply to any project, it's too generic.

### 7. Data Traceability Is Non-Negotiable

Corrections 4, 5 (deeper pattern). The user thinks in terms of data lineage. Every piece of data should have a traceable path: source --> raw export --> processed form --> output. Skipping steps in this chain (e.g., going directly from API to RAG without saving the raw file) is a violation.

**Rule:** Every data transformation must leave an artifact at each stage. Source URL, raw file, processed output -- all must be inspectable after the fact.

---

## Behavioral Checklist for Future Sessions

Derived from the corrections above. Check these before presenting any result to the user.

### Before Starting Work

- [ ] Am I using real data or synthetic test data? (Use real data)
- [ ] Is the tool/integration actually working, or am I about to build a workaround? (Fix the tool)
- [ ] Did I check `notes/decisions.md` for existing findings?

### During Work

- [ ] Am I saving raw source files to disk before processing them?
- [ ] Am I saving generated artifacts (diagrams, documents) to the repo?
- [ ] Is this a one-off operation that should be automated?
- [ ] Am I asking the user a question with an obvious answer? (Just do it)

### Before Presenting Results

- [ ] Is my deliverable a tangible artifact, or just a status report?
- [ ] Are all files saved in the correct repo directory?
- [ ] Can someone trace the data lineage from source to output?
- [ ] Is my analysis specific and detailed, or vague and summary-level?
- [ ] Did I take the obvious next step, or am I punting it to the user?

### After Completing Work

- [ ] Are new findings added to `notes/decisions.md`?
- [ ] Are generated files committed (or staged for commit)?
- [ ] Is there an automation gap that needs an issue?

---

## How These Corrections Shaped the Session

The corrections weren't just fixes -- they redirected the entire session's trajectory.

**Before corrections (first ~2 hours):** The session was heading toward a "setup complete, all systems green" endpoint. Infrastructure would be configured, tools would be verified, and the assistant would present a nice summary of what's available. Zero usable output.

**After corrections (remaining ~4 hours):** The session produced real artifacts: documents exported and saved, RAG index populated with actual content, semester roadmap created, draw.io diagrams saved to repo, gap analysis performed, formal program rewrite initiated. The corrections turned a setup session into a production session.

**The fundamental shift:** From "proving the system works" to "using the system to work." This is the single most important insight from the entire session. The user never cared about whether MCP servers respond to ping. They cared about whether their course materials are organized, indexed, and actionable.
