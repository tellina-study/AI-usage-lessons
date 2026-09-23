---
id: s35
type: code_artifact
duration_min: 0.75
assertion: "What is new is not the file (it was set up on day 0) but the first substantive entry in it, dated the day the decision was written down"
learning_goal: "The concrete decision of case 2.1 — the contents of an already existing file, with no creation diff: the file has existed since day 0, only the entry in it is new"
visual:
  pattern: code_artifact
  primary: "DECISIONS.md in full, the real file. On the right — the state of the repository at the end of the first week, the DECISIONS.md line highlighted in gold. NO diff panel: the file has existed since day 0, there is no creation diff on the slide."
  backup: "The product layer of the tree — assets/captures/22-tree-stage2.txt; spec.md and README.md were set up on day 0 and did not make it into that git snapshot. On the slide the state of the repository is shown in full. The date of the entry (2026-09-26) is the end of the first week on the session's running calendar, not the day the repository was created (2026-09-20)."
---

# The first entry in a file that was already set up

## Assertion

What is new is not the file (it was set up on day 0) but the first substantive entry in it, dated the day the decision was written down.

## Visual

On the left — the file in full, the real one:

```markdown
# Decisions

Append-only log of why, in date order.

## 2026-09-26 — no third-party widgets in the form
The form has two fields (name, email), the native `required`/`pattern` in `index.html` are enough.
A third-party widget is an extra dependency and extra kilobytes in the bundle for this much functionality.
```

On the right — the state of the repository at the end of the first week, the `DECISIONS.md` line highlighted in gold:

```
README.md
spec.md
DECISIONS.md
CLAUDE.md
AGENTS.md
index.html
package.json
src/main.js
tests/form.spec.ts
```

## Speaker notes

Two mechanisms, not one. The runtime's auto-memory lives outside the repository, in a memory directory on the developer's machine: an index of the first 200 lines or 25 KB plus topic files that the agent creates itself. The command "remember: no third-party widgets in the form" creates a topic file exactly there — it does not make it into the tree on the right.

`DECISIONS.md` is the second mechanism, a git-tracked append-only log, set up on day 0. What is new here is not the file but the first substantive entry in it, and its date is today's: the decision was made a few days ago and was written down only now. This is a real file from a real demo repository, not an example made up for the slide.
