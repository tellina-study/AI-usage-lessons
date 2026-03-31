# User Feedback — Session 2 Part 2 (2026-03-31)

## Explicit Corrections

### "Do NOT delegate web research"
- Context: Orchestration rule in CLAUDE.md was overly broad
- Action taken: Removed from CLAUDE.md — permissions were already fixed

### "Test before merge"
- Context: PR was about to be merged without verifying all skills work
- Action taken: All 9 skills tested before merge was approved
- **Pattern:** User values verification before merge, not just implementation

### "Save analysis results"
- Context: Ontology analysis was done but results only shown in chat
- Action taken: Ontology snapshot + analysis reports saved to files
- **Pattern:** User wants durable artifacts, not ephemeral chat output

### "Show me other options before commit"
- Context: I was about to commit to pyvis without exploring alternatives
- Action taken: Presented all visualization options (OntoSpy, pyvis, D3, Graphviz, etc.) with pros/cons
- **Pattern:** User wants to see options and make the choice, not have it made for them

### "Create table view in separate file"
- Context: I tried to add table view into the graph script
- Repeated: "No! Create table view in separate file"
- Action taken: Created generate_table.py as a separate script
- **Pattern:** User prefers separation of concerns, one script per output

### "Where is README with links?"
- Context: GitHub Pages was enabled but no README pointed to it
- Action taken: Created README.md with project description and visualization links

### "Remove from gitignore! We need them!"
- Context: Generated HTML files were gitignored
- Action taken: Removed from .gitignore, committed HTMLs to repo
- **Pattern:** Generated visualization artifacts should be committed for GitHub Pages

### "HTMLs open as raw text"
- Context: GitHub shows HTML source, not rendered page
- Action taken: Enabled GitHub Pages so HTMLs render properly
- **Pattern:** User expects visual results to be immediately viewable

### "Roast and revise your suggestion"
- Context: Drive folder structure plan for issue #11
- Action taken: First time roast was explicitly requested and properly executed
- Result: Structure was simplified from overly nested to practical 17+17 format
- **Pattern:** User values the roast step and will request it when they see over-engineering

### "Now just fix area, not if very small vertically"
- Context: A layout fix was being over-engineered
- Action taken: Applied minimal fix
- **Pattern:** User prefers minimal, targeted fixes over comprehensive refactors

### Feedback on Drive structure: "17+17 format, assets in lesson folders"
- Context: Initial plan had separate assets tree
- Action taken: Assets placed within each lesson folder
- **Pattern:** User prefers co-location of related content over deep categorization

## Implicit Approvals

- pyvis as visualization tool (after seeing options)
- GitHub Pages for serving HTML visualizations
- 4 parallel subagents for Drive folder creation
- Reflection skill and process workflow
- Issue-per-task workflow with branch-per-issue naming

## Emerging Patterns

1. **Show options, let user choose** — don't commit to a tool/approach without presenting alternatives
2. **Separate concerns** — one script per output, one file per function
3. **Minimal fixes** — don't over-engineer corrections
4. **Durable artifacts** — save results to files, not just chat
5. **Verify before merge** — testing is mandatory, not optional
6. **Roast is valued** — user actively requests it for non-trivial plans
7. **Co-locate related content** — keep assets with their parent, not in separate trees

## Frustration Triggers

- Mixing multiple outputs into one script (table + graph in same file)
- Not showing alternatives before making choices
- Generated files being gitignored when they need to be served
- Raw markdown appearing in Google Docs (create_doc vs import_to_google_doc)
