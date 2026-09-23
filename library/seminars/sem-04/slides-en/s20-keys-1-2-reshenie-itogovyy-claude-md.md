---
id: s20
type: code_artifact
duration_min: 1.5
assertion: "The final file is thirteen lines: the \"done\" criterion, the gate warning, an honest caveat about the limit; AGENTS.md is a symlink to the same file"
learning_goal: "The solution of case 1.2 — the real final CLAUDE.md, the loading mechanics, the AGENTS.md symlink and the sharp edge of cp -R"
visual:
  pattern: code_artifact
  primary: "The final CLAUDE.md in full (13 lines) on the left. On the right — three mechanical details, one line each: the file is loaded in full every session; @-imports do not save context; AGENTS.md is a symlink with the sharp edge of cp -R."
---

# The final CLAUDE.md — thirteen lines

## Assertion

The final file is thirteen lines: the "done" criterion, the gate warning, an honest caveat about the limit; `AGENTS.md` is a symlink to the same file.

## Visual

```markdown
# CLAUDE.md

signup-landing: a static landing page with a demo-lesson sign-up form.
Done = npm run build exit code 0, npx playwright test green,
the form really sends the request in production.

## Safety / scope boundaries
- Never run a deploy to production without an explicit request.

## Build, test, verify
- To verify: open dist/index.html after the build and manually
  submit the form with filled-in and with empty fields.
```

On the right — three mechanical details:

1. The file is loaded in full at the start of every session (the official guideline is up to 200 lines, our result is 13).
2. `@`-imports organize the file but do not save context — what is imported is still loaded in full.
3. `AGENTS.md` is a symlink to the same file (`ln -s CLAUDE.md AGENTS.md`). The sharp edge: `cp -R` without `-P` on macOS silently dereferences the symlink into a second copy — copy with `cp -a` / `git clone` / `git archive`.

## Speaker notes

"Here is the result of case 1.2: thirteen lines — the readiness criterion, the gate warning to verify delivery by hand, an honest boundary on deploys. The file is loaded in full at the start of every session; the official guideline is up to two hundred lines, and we have thirteen. `@`-imports organize the file but do not save context — what is imported is still loaded in full.

And we set up `AGENTS.md` as a symlink to the same file — one source of truth for different engines. The sharp edge: `cp -R` without `-P` on macOS silently dereferences the symlink into a second real copy — copy with `cp -a`, `git clone` or `git archive`."
