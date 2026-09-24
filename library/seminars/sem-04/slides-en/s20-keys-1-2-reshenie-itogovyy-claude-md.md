---
id: s20
type: code_artifact
duration_min: 1.5
assertion: "The final file is fifteen lines: the \"done\" criterion, the gate warning, an honest caveat about the limit, and one one-off step without which the tests fail for no good reason; AGENTS.md is a symlink to the same file"
learning_goal: "The solution of case 1.2 — the real final CLAUDE.md, the loading mechanics, the AGENTS.md symlink and the sharp edge of cp -R"
visual:
  pattern: code_artifact
  primary: "The final CLAUDE.md in full (15 lines) on the left. On the right — three mechanical details, one line each: the file is loaded in full every session; @-imports do not save context; AGENTS.md is a symlink with the sharp edge of cp -R."
  backup: "The file is `git show 1019546:CLAUDE.md` in tellina-study/signup-landing-demo, branch seminar-4-arc — the same file as assets/captures/28-code-CLAUDE.md.txt. The line count is taken from the repository by a command (`| wc -l` -> 15), not from this slide. The runs the readiness criterion refers to were done on this same commit: npm run build -> exit code 0, npx playwright test -> green."
---

# The final CLAUDE.md — fifteen lines

## Assertion

The final file is fifteen lines: the "done" criterion, the gate warning, an honest caveat about the limit, and one one-off step without which the tests fail for no good reason; `AGENTS.md` is a symlink to the same file.

## Visual

```markdown
# CLAUDE.md

signup-landing: a static landing page with a demo-lesson sign-up form.
Done = `npm run build` exit code 0, `npx playwright test` green, the
form submitted by hand from the built `dist/` — filled in and empty.

## Safety / scope boundaries
- Never run a deploy to production without an explicit request.

## Build, test, verify
- To verify: open `dist/index.html` after the build and submit the
  form by hand — with filled-in and with empty fields.
- Once per machine, before the first `npx playwright test`: `npm ci`,
  then `npx playwright install chromium`. Without the second command
  every test fails at once and for no good reason.
```

On the right — three mechanical details:

1. The file is loaded in full at the start of every session (the official guideline is up to 200 lines, our result is 15).
2. `@`-imports organize the file but do not save context — what is imported is still loaded in full.
3. `AGENTS.md` is a symlink to the same file (`ln -s CLAUDE.md AGENTS.md`). The sharp edge: the behaviour of `cp -R` on a symlink is **not defined by the standard** (POSIX.1-2024: with `-R` and none of `-H`/`-L`/`-P` the default is unspecified); `-P` states the intent, `-L` breaks the symlink for certain.

## Speaker notes

"Here is the result of case 1.2: fifteen lines — the readiness criterion, the gate warning to verify delivery by hand, an honest boundary on deploys, and one one-off step after cloning without which the tests fail instantly and for no good reason. The file is loaded in full at the start of every session; the official guideline is up to two hundred lines, and we have fifteen. `@`-imports organize the file but do not save context — what is imported is still loaded in full.

A word about that last line on its own. `npx playwright install chromium` is exactly the kind of step the 'Build, test, verify' section exists for in the first place: without it, a clean clone fails every test at once, and fails them for no good reason — not because the code is broken, but because there is no browser on the machine. An agent that has read this will not start repairing code that works.

`AGENTS.md` has been with us since day one — a symlink to this same file, one source of truth for different engines. Note that it is set up right away, and it holds exactly as much content as `CLAUDE.md`, because it is one and the same file. The sharp edge here is not that some system behaves incorrectly, but that the behaviour of `cp -R` on a symlink is simply not defined by the standard: POSIX states outright that with `-R` and none of `-H`, `-L` or `-P`, the default is unspecified. On GNU coreutils the symlink survives the copy, but that cannot be relied on — `-P` states the intent explicitly. What does break the symlink for certain is `-L`: `cp -RL` will give you a second real copy, and from then on the two files quietly drift apart. The safest way to move the project is `git clone` or `git archive`."
