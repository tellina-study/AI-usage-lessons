---
id: s04
type: code_artifact
duration_min: 2
assertion: "The agent built a working prototype from the spec without a single clarifying question — and chose the structure of the repository itself along the way, because spec.md does not describe it"
learning_goal: "The first run of the running project: a real empty repository, the task taken from the spec, an assembled prototype; the structural decisions were taken by the agent silently — the entry into case 1.1"
visual:
  pattern: terminal_task_and_dialogue
  primary: "Three tiers. Top tier, left — the real captured output of ls -la signup-landing/ before the run: an empty directory. Top tier, right — the task as put to the agent, verbatim (the functional part, matching spec.md in content). Middle tier — the line from the captured session saying there were no clarifying questions, in large type, in a gold frame. Bottom tier, left — what appeared in the repository after the run: four lines of a real capture under the caption \"created by the agent\". Bottom tier, right — the block of commands from the final answer. Caption: \"real output, not a mock\"."
  backup: "library/seminars/sem-04/assets/captures/01-ls-la-empty-dir.txt — transfer verbatim. library/seminars/sem-04/assets/captures/36-first-task-dialogue.md, block 1 (the text of the task), block 2 (the sentence about there being no clarifying questions) and a fragment of block 3 (the file list + the commands). The capture was made in a repository without spec.md/README.md — on the slide the list is captioned \"created by the agent\", so there is no discrepancy with the narrative."
---

# The first run: from an empty directory to a prototype

## Assertion

The agent built a working prototype from the spec without a single clarifying question — and chose the structure of the repository itself along the way, because `spec.md` does not describe it.

## Visual

Top tier. On the left — the real captured output before the run:

```
$ ls -la signup-landing/
total 8
drwxr-xr-x 2 harness harness 4096 Sep 20 12:45 .
drwxr-xr-x 3 harness harness 4096 Sep 20 12:45 ..
```

On the right — the task as put to the agent, verbatim, matching the functional part of `spec.md` in content:

> "build a landing page with a sign-up form for a demo lesson: a static HTML page, a Vite build (`npm run build` → `dist/`), form fields — name and email, a Playwright test that checks that the form does not submit with empty required fields (`tests/form.spec.ts`)"

Middle tier — the line from the captured session, in large type, in a gold frame:

> "No clarifying question was asked. All the parameters of the task were unambiguously derivable from the text of the task, so work was begun immediately, without clarifications."

Bottom tier. On the left — what appeared in the repository after the run, under the caption "created by the agent":

```
index.html
src/main.js
package.json
tests/form.spec.ts
```

On the right — the block of commands from its own final answer:

```
npm install
npm run build          # → dist/
npm run test:e2e       # playwright test
```

## Speaker notes

"The directory is empty — that is the real output of the command before the run. Then the agent gets the task from the spec and in a single pass hands back an assembled project: the markup, the form handler, the package manifest with the build and test scripts, a Playwright test. The prototype works — the commands from its final answer run.

There were no clarifying questions at all; the captured session records this outright: all the parameters of the task were derivable from the text.

And here it is worth pausing on what was not in that text. The acceptance criterion was there — we wrote it into the spec ourselves. But the structure: what to name the files, where to put the handler, how to lay the project out across folders — none of that is in the spec, and it should not be; that is how the code is put together, not a requirement on the product. The agent took those decisions itself, and silently: `src/main.js`, `tests/form.spec.ts`, the scripts in `package.json`.

We have a prototype. From here there are many days of work ahead in this repository — and this is where the question about the agent's configuration begins."
