---
id: s27
type: assertion_visual
duration_min: 1.5
assertion: "The root file stayed the same, fifteen lines long: the detail went off into a comment on the function, the test convention already sits in the tests themselves, not a single nested instruction file got set up — and knowledge that appears in the course of the work has a different address, and that is section two"
learning_goal: "The resolution of case 1.3 (state of the repository + the threshold for switching on each address) and the closing bridge from section 1 to section 2 — memory"
visual:
  pattern: assertion_visual
  primary: "Top — the state of the repository at month 1: the root instruction file is still a single file of the very same length, a comment has appeared inside src/main.js, and neither tests/CLAUDE.md nor src/CLAUDE.md is anywhere in the tree. Middle — a compact table of thresholds: address · when to switch it on · when it's too early. Bottom — a large summary line for the three decision points of section 1 and the transition into section 2."
  backup: "The state of the repository is taken from the real commit ffbb258 in tellina-study/signup-landing-demo, branch seminar-4-arc (`git ls-tree -r --name-only ffbb258`): submitForm() with a retry on timeout, the comment on it, three files in tests/ and not a single nested instruction file. The product layer is shown — the build infrastructure is omitted (.gitignore, package-lock.json, vite.config.js, playwright.config.ts, src/style.css, src/validate.js). The scenario \"two pieces of knowledge accumulated over a month\" is a narrative convention; the code and the tests themselves are real: npx playwright test -> 8 passed, and the comment on submitForm() is held in place by tests/delivery.spec.ts, not by trust."
---

# Three addresses — and the bridge to memory

## Assertion

The root file stayed the same, fifteen lines long: the detail went off into a comment on the function, the test convention already sits in the tests themselves, not a single nested instruction file got set up — and knowledge that appears in the course of the work has a different address, and that is section two.

## Visual

The state of the repository, month 1:

```
README.md
spec.md
DECISIONS.md
CLAUDE.md              ← the same 15 lines, no growth
AGENTS.md              → symlink to CLAUDE.md
index.html
package.json
src/main.js            ← comment on submitForm(): retry on timeout,
                         the handler has to be idempotent
tests/form.spec.ts
tests/delivery.spec.ts
tests/page-objects/form.page.ts
# tests/CLAUDE.md and src/CLAUDE.md — never appear
```

The test convention did not get set up as a separate file: it is already embodied in the three existing tests — an agent that opens any one of them sees the page object in the code itself. The same logic as in case 1.1, and with the same caveat: it follows from the mechanism, it has not been measured directly.

**The threshold for switching on each address:**

| Address | When to switch it on | When it's too early |
|---|---|---|
| A comment in the code | right away, with no signal: it is useful to a human anyway, and the agent gets it for free | never too early |
| A rule with a path pattern | when the convention for a class of files has stopped fitting into the root file **and** the pattern can be named in a single expression | while the convention is two lines long |
| A corpus pointer in the root file | when a document to point at has appeared, and a person who maintains it | a pointer with no document — a line of context in every session for nothing |
| A nested file in a subfolder | never as the only guarantee: only after checking with `/context` that your tool, in your version, picks it up | always, until that check has been done |

A large summary line:

> "Three decision points, one and the same file: we decided what not to write into it in advance; we wrote down the readiness gate, set up on day 0; and we decided that knowledge has an address — and a nested folder is not one. All of that is knowledge you had before the work started. But there is knowledge of another kind: the kind that appears in the course of the work itself — what has already been tried and rejected, why it was rejected, what decisions were taken between sessions. It has an address too. That is section two — memory."

## Speaker notes

"On our repository the root file has not changed — the same fifteen lines. The detail about the retried submit went off into a comment on the function itself: you edit it, you read the file, you see the comment. The test convention did not get set up as a separate file, because it already sits in the three existing tests: an agent that opens any one of them sees the page object in the code. The same logic as in the first case — whatever is derivable, the agent will derive by itself — and with the same honest caveat: it follows from the mechanism, it has not been measured directly. Neither `tests/CLAUDE.md` nor `src/CLAUDE.md` ever appeared in the repository.

The threshold for each address. A comment in the code — no signal needed, it is useful to a human as well, and the agent gets it for free. A rule with a path pattern — when the convention has stopped fitting into the root file and you can name the pattern in a single expression; while it is two lines long, it's too early. A corpus pointer — when a document to point at has appeared, and a person who maintains it; a pointer with no document is a line of context in every session for nothing. A nested file in a subfolder — never as the only guarantee: only if you have checked through `/context` that your tool, in your version, picks it up, and are prepared to re-check after every update.

Three decision points, one and the same file: we decided what not to write into it in advance; we wrote down the readiness gate that we set up on day 0; and we decided that knowledge has an address — and a nested folder is not one. All of that is knowledge you already had before the work started: written down in advance, or checked on the first real task.

But there is knowledge of another kind: the kind that appears in the course of the work itself. You cannot write it down in advance, because you do not know it yet. And it has an address too. That is section two — memory."
