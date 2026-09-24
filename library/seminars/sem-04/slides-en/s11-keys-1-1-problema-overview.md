---
id: s11
type: problem_scenario
duration_min: 1.5
assertion: "The prototype is built, the next session is tomorrow — CLAUDE.md already has the readiness-gate line in it and nothing else, and the standard first section of such a file is called 'Repository overview'"
learning_goal: "The problem of case 1.1 — a decision-point scenario at the entry into CLAUDE.md, where there is nothing yet apart from the gate line. NO question, NO cards, NO evaluation of the options — those are on the following slides"
visual:
  pattern: problem_scenario
  primary: "On the left — the state of the repository after the first run. On the right — the scenario: the developer opens CLAUDE.md — there is one line in it, the readiness gate, the rest is empty; the typical first section of such a file is 'Repository overview' (what the site is built from, where the form lives, what the folder structure is), and that is how instruction files are put together in most public repositories. NO question, NO cards, NO evaluation."
  backup: "The tree is the product layer of assets/captures/21-tree-stage1.txt (`git ls-tree -r --name-only 1019546` in tellina-study/signup-landing-demo, branch seminar-4-arc); at this step the file list is identical to commit 25bd3f0, where the prototype has just been built — verified by diff. The build infrastructure is omitted: .gitignore, package-lock.json, vite.config.js, playwright.config.ts, src/style.css, src/validate.js. AGENTS.md is shown on the slide because it is real in the repository: a symlink to CLAUDE.md, set up on day 0 (commit 10699a2, mode 120000)."
---

# An almost empty CLAUDE.md

## Assertion

The prototype is built, the next session is tomorrow — `CLAUDE.md` already has the readiness-gate line in it and nothing else, and the standard first section of such a file is called "Repository overview".

## Visual

The state of the repository:

```
README.md
spec.md
DECISIONS.md
index.html
package.json
src/main.js
tests/form.spec.ts
CLAUDE.md        ← set up, has the gate line, nothing else
AGENTS.md        → symlink to CLAUDE.md, set up on day 0
```

On the right — the scenario:

> The prototype works, and there are still several days of tasks on it. The developer sets up `CLAUDE.md` so that the agent will work with the project the same way in the sessions that follow, and opens the file — there is one line in it, the readiness gate, the rest is empty.
>
> The first section such a file usually starts with is "Repository overview": what the site is built from, where the form lives, what the folder structure is. That is how most of the instruction files you can open in public repositories are put together.

There is neither a question nor any option cards on this slide.

## Speaker notes

"The prototype is built, but the work isn't finished: there are still several days of tasks ahead on this same repository, and each one is a new agent session from scratch. The developer sets up `CLAUDE.md` — the file that gets loaded at the start of every session — and opens it: there is one line in it, the readiness gate, the rest is empty.

Open almost any public repository that has such a file and it starts with a "Repository overview" section: what this project is, how it is put together, where things live. That is an established convention, and the question of the first decision point is exactly about it: which of that is worth writing down here, in this repository, at this step."
