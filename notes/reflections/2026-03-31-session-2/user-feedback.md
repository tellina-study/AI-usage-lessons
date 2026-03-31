# User Feedback — Session 2 (2026-03-31)

## Explicit Corrections

### 1. "Do NOT delegate" removal
The user pointed out that CLAUDE.md contained contradictory language. A "Do NOT delegate" instruction existed alongside the orchestration rule requiring delegation to subagents. The user directed removal of the contradictory phrasing. This was a clarity issue from session 1 where rules were written incrementally without checking for consistency.

### 2. "Test before merge"
The user insisted that skills and tools must be tested before PRs are merged. Session 1 merged PR #2 with untested MCP configurations and skill stubs. Session 2 corrected this by testing 3 skills before considering the PR ready. The remaining 5 skills are still being tested before merge.

**Rule to adopt:** Never mark a PR as ready until all new functionality in it has been tested at least once.

### 3. "Save analysis results"
The user directed that analysis outputs (e.g., from extract-links, impact-check) should be saved to disk, not just displayed in conversation. Conversation context is ephemeral; disk artifacts persist. This led to saving raw docs to `catalog/exports/docs/` and ensuring skill outputs write to files.

**Rule to adopt:** Every skill that produces analysis output must write results to a file, not just return them to the conversation.

## Implicit Approvals

- User approved the blueprint folder structure without modifications
- User approved the reflection-process workflow specification
- User approved the skill rewrite approach (executable agent prompts with MCP tool names)
- User approved the 5-file reflection folder structure

## Patterns Observed

### Communication Preferences
- User prefers concrete deliverables over discussion. "Show me files, not plans."
- User values honest assessment of what works vs. what is untested.
- User gives clear, directive corrections. Minimal back-and-forth preferred.

### Autonomy vs. Confirmation
- User grants high autonomy for implementation details (file names, internal structure)
- User requires confirmation for process changes (workflow rules, CLAUDE.md edits)
- User expects phase gating for multi-step work but does not micromanage within a phase

### Frustration Triggers
- Contradictory rules in CLAUDE.md (session 1 issue, fixed in session 2)
- Merging untested work
- Losing analysis results because they were only in conversation context

## New Behavioral Rules

1. Always test new functionality before marking PR ready
2. Always save analysis/skill outputs to disk files
3. Check CLAUDE.md for internal contradictions when adding new rules
4. When user says "fix X", fix it immediately without extensive discussion
