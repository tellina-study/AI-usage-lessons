# Reflection Process

Post-session reflection workflow. Run after every working session to capture findings, identify improvements, and feed lessons back into the system.

## When to Reflect

Run a reflection after **every** working session, not just long ones. Specifically, reflect after any session where:

- New MCP tools or skills were used for the first time
- Problems were encountered (tool failures, auth issues, data errors)
- The user gave corrections or expressed preferences
- Significant work was completed (documents created, lectures updated, diagrams built)
- A workflow rule was violated or nearly violated

If in doubt, reflect. Short reflections (even 5 minutes) compound over time.

## Reflection Folder Structure

Each reflection lives in its own dated folder:

```
notes/reflections/{YYYY-MM-DD}-{session-topic}/
  tools.md          -- MCP servers, skills, subagents used: what worked, what failed
  workflow.md       -- git, issues, PRs, branches: process compliance
  content.md        -- documents, diagrams, ontology: what was created, quality assessment
  user-feedback.md  -- corrections, preferences, patterns discovered
  improvements.md   -- concrete next actions extracted from above
```

The `{session-topic}` should be a short kebab-case description, e.g. `lecture-3-slides`, `library-sync-fix`, `mcp-setup`.

## Reflection Questions per File

### tools.md

Answer each question based on what actually happened in the session:

- Which MCP tools were called? List server and tool name.
- Which tools failed? What was the error? Was it transient or structural?
- Were skills invoked (sync-library, catalog-docs, etc.)? If not, why not?
- Were subagents used (librarian, doc-editor, deck-editor, etc.)? What was their success/failure ratio?
- Any new tools discovered or needed that are not yet configured?
- Permission issues encountered (OAuth, file access, API scopes)?
- Tool selection mistakes: was the wrong tool used when a better one existed?

### workflow.md

Check compliance with CLAUDE.md rules:

- Were GitHub issues created before work started?
- Was branch-per-issue naming followed (`issue-{N}-{description}`)?
- Was roast-before-implement done for non-trivial work?
- Was phase gating respected (implement, verify, gate per phase)?
- Were commits properly structured with issue references (`#N`)?
- Was anything pushed to main? (This is a critical violation.)
- Was the orchestration rule followed (Claude Code plans, subagents implement)?
- Were any anti-patterns from CLAUDE.md triggered?

### content.md

Track what was produced and its quality:

- What documents were read, created, or modified? List with Google Drive or file paths.
- Were raw exports saved to `catalog/exports/`?
- Were manifests updated (`catalog/manifests/*.yaml`)?
- Was the ontology populated with new entities or relations?
- Were diagrams saved as `.drawio` files in `diagrams/`?
- Was the RAG index updated via `mcp-local-rag`?
- Quality assessment: are outputs complete, consistent, and correctly linked?
- Any content that needs follow-up work?

### user-feedback.md

Capture behavioral signals:

- What did the user explicitly correct? Quote or paraphrase.
- What did the user approve without comment? (Implicit approval signals.)
- What patterns emerge about user preferences (communication style, level of detail, autonomy vs. confirmation)?
- Any new behavioral rules to adopt based on this session?
- Did the user express frustration? What triggered it?

### improvements.md

Extract actionable items only. No observations without actions.

Format each improvement as:

```
### {Short title}
- **Priority:** P0 (do now) | P1 (do this week) | P2 (do this month) | P3 (backlog)
- **Effort:** S (< 30 min) | M (1-3 hours) | L (> 3 hours)
- **Component:** which file, skill, workflow, or config to change
- **Action:** specific change to make
- **GitHub issue:** link or "create"
```

## Post-Reflection Actions

After writing all reflection files:

1. **Update `notes/decisions.md`** with key findings that should persist as project knowledge
2. **Create GitHub issues** for all P0 and P1 improvements (use `issue-from-change` skill or `issue-manager` agent)
3. **Update CLAUDE.md** if any rules need adding, changing, or clarifying
4. **Update memory files** (`.claude/` memory) if user preferences changed
5. **Commit all reflection files** on the current working branch with message referencing the relevant issue
