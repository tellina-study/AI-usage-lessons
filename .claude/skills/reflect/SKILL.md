# reflect

Run post-session reflection process.

## When to Use

Invoke after every working session to capture what happened, what worked, what failed, and what to improve. See `workflows/reflection-process.md` for the full specification.

## Steps

1. **Create reflection folder**
   - Path: `notes/reflections/{YYYY-MM-DD}-{session-topic}/`
   - Use today's date and a short kebab-case topic describing the session

2. **Write reflection files**
   For each area, review the conversation history for relevant events and write the corresponding file following the questions in `workflows/reflection-process.md`:
   - `tools.md` -- MCP servers, skills, subagents: what was called, what failed, why
   - `workflow.md` -- git process compliance: issues, branches, roast, phase gates
   - `content.md` -- documents, diagrams, ontology: what was produced, quality
   - `user-feedback.md` -- corrections, preferences, patterns from user behavior

3. **Write improvements.md**
   - Extract every actionable improvement from the four reflection files
   - For each: assign priority (P0-P3), effort (S/M/L), target component, and specific action
   - Link to existing GitHub issue or mark "create"

4. **Update notes/decisions.md**
   - Add key findings that should persist as project-level knowledge
   - Follow the existing format in the file

5. **Create GitHub issues**
   - For every P0 and P1 improvement, create a GitHub issue using `issue-manager` agent or `issue-from-change` skill
   - Reference the reflection folder in the issue body

6. **Commit reflection files**
   - Stage all files in the new `notes/reflections/{date}-{topic}/` folder
   - Commit with message: `Add reflection: {topic} #{issue-number}`
   - Include any updates to `notes/decisions.md` in the same commit
