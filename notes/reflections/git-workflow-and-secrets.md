# Reflection: Git Workflow, Secrets Management, and PR Process

**Session:** First session (2026-03-31)
**Scope:** Repository bootstrap, MCP server configuration, initial document work

---

## 1. Initial Commit Directly to Main

CLAUDE.md states unambiguously: "NEVER push to main directly." Yet the very first commit -- 45 files, 792 lines of scaffolding -- went straight to main. The justification was "one-time bootstrap exception for an empty repo," and the user explicitly approved it.

**Was it justified?** Partially. An empty repo has no main branch until the first commit, so there is a genuine chicken-and-egg problem: you cannot create a branch off main if main does not exist yet. However, the workaround is simple -- push an empty initial commit (or a single README) to main, then immediately branch for the real scaffolding. That way the rule is never broken, not even once.

**Why it matters:** Rules that tolerate exceptions on day one teach the habit of exception-making. The 45-file commit was large enough to deserve its own branch and PR, which would also have provided a review checkpoint before the project's foundational structure was locked in.

**Verdict:** The exception was understandable but unnecessary. A two-step approach (empty commit to main, then branch for scaffolding) would have cost almost nothing and preserved the rule from the start.

---

## 2. Branch Workflow

The `issue-1-mcp-setup` branch was created correctly for MCP configuration work. Four commits landed on it, each referencing `#1` in the message. PR #2 was opened with a structured summary and test plan. So far, textbook.

**Problem 1: PR #2 was never merged.** The session moved on to Issue #3 work while PR #2 was still open. This means the main branch never received the MCP changes, and any future branch cut from main will lack them.

**Problem 2: Issue #3 work landed on the Issue #1 branch.** CLAUDE.md requires branch-per-issue (`issue-{NUMBER}-{short-description}`). By committing Issue #3 changes to the `issue-1-mcp-setup` branch, two concerns got entangled:

- The PR for Issue #1 now contains unrelated changes, making review harder.
- There is no clean PR for Issue #3 alone.
- If Issue #1's PR needs to be reverted, Issue #3's work goes with it.

**What should have happened:**
1. Finish Issue #1 work on its branch.
2. Open PR #2, get it reviewed and merged.
3. Create `issue-3-document-work` from updated main.
4. Commit Issue #3 changes there.

This is the most basic branch hygiene, and skipping it on day one normalizes the shortcut.

---

## 3. Secrets Near-Miss

This was the most consequential mistake of the session. The sequence:

1. **First attempt:** `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET`, and `GITHUB_PAT` were placed directly into `.claude/settings.json` -- a file tracked by git. Had a commit been made at that point, secrets would have entered version history permanently (git never truly forgets, even after force-push and rewrite).

2. **Caught before commit.** Secrets were moved to `.claude/settings.local.json`, a new file. But `.gitignore` did not yet exclude it -- that entry was added reactively.

3. **Second vector:** Running `claude mcp add` wrote secrets into `.mcp.json` at the repo root. This file was also not yet in `.gitignore`. Another reactive addition.

4. **Third vector:** The PAT was provided by the user as plain text in the chat. Conversation history is stored by the platform. This is a less severe risk (the history is not public), but it means the secret exists in a location outside the user's direct control.

**Root cause:** There was no secrets convention established before configuration began. The session jumped straight into "let's configure MCP servers" without first asking: "Where will secrets live? How do we ensure they never touch git?"

**What a good convention looks like:**
- All secrets go into environment variables (`.env` file, already in `.gitignore` from day one).
- MCP configs reference `${ENV_VAR}` syntax, never literal values.
- `.claude/settings.local.json` and `.mcp.json` are added to `.gitignore` before any MCP configuration begins, not after.
- Never accept secrets as plain text in chat. Instead: "Please set the environment variable `GITHUB_PAT` in your shell, then I will reference it."

**Severity:** High. A committed secret in a public repo is an immediate security incident requiring rotation. This was avoided only by luck (the mistake was caught manually before staging), not by process.

---

## 4. .gitignore Evolution

The `.gitignore` started with reasonable basics: `catalog/exports/`, `.env`, IDE files, `oxigraph-data/`. But every subsequent addition was reactive:

| Addition | Trigger |
|----------|---------|
| `.claude/settings.local.json` | Secrets almost committed |
| `.mcp.json` | Secrets almost committed (again) |
| `lancedb/` | local-rag created data directory |
| `models/` | local-rag downloaded embedding models |

Each of these was predictable. The MCP servers being configured were known in advance -- their documentation describes what local files they create. A five-minute review of each server's docs would have produced a complete `.gitignore` before any configuration started.

**Pattern:** Reactive `.gitignore` management is a symptom of "configure first, think later." The fix is simple: before adding any tool or server, check what local artifacts it creates, and update `.gitignore` proactively.

---

## 5. Commit Quality

**What went well:**
- Every commit references its issue (`#1` or `#3`).
- Every commit includes `Co-Authored-By` attribution.
- Commit messages describe intent, not just mechanics ("Add workspace-mcp, document-loader and secure secrets handling" rather than "Update settings.json").

**What could improve:**
- Some commits bundle multiple concerns. For example, one commit included changes to `settings.json`, `CLAUDE.md`, and `.gitignore` together. These are three different concerns: tool configuration, documentation, and build/ignore rules. Splitting them would make history easier to navigate and individual changes easier to revert.
- The bar for "one logical change" was interpreted loosely. A stricter standard: if two changes could be reverted independently and it would make sense, they should be separate commits.

---

## 6. PR Process

PR #2 was well-structured:
- Clear summary with bullet points.
- Test plan with checkboxes.
- Proper base branch (main) and head branch (issue-1-mcp-setup).

**But:**
- The PR was never reviewed or merged during the session.
- Work continued on the same branch for a different issue, polluting the PR's scope.
- No PR was created for Issue #3 changes at all.

The PR process is only valuable if it is completed. An open, unmerged PR that accumulates unrelated changes is worse than no PR, because it creates the illusion of process without the substance.

---

## 7. What Should Have Been Different

Ranked by impact:

1. **Establish secrets convention before any configuration.** Define where secrets live, how they are referenced, and what files must be in `.gitignore` -- all before touching a single config file. This prevents the entire class of secrets-in-git near-misses.

2. **Proactive `.gitignore` for all tools.** Before adding each MCP server, review its docs for local artifacts. Update `.gitignore` in one commit before configuration begins.

3. **Separate branches for separate issues.** Issue #3 work should never have landed on the Issue #1 branch. This is the most basic branch discipline and the easiest rule to follow.

4. **Merge PR #2 before starting Issue #3.** Unmerged PRs that grow stale are technical debt. Completing the cycle (branch, PR, review, merge) before starting new work keeps the repo clean.

5. **Bootstrap via branch, not direct push.** Push an empty commit to main, then branch for the real scaffolding. Preserves the "never push to main" rule from commit zero.

6. **Never accept secrets in chat.** Ask the user to set environment variables instead of pasting tokens into the conversation. This is a defense-in-depth measure.

---

## 8. Patterns to Carry Forward

**Good patterns from this session:**
- Issue-driven workflow (every task has a GitHub issue)
- Commit messages that reference issues and explain intent
- PR with summary and test plan structure
- Catching secrets before commit (even if by luck)

**Anti-patterns to eliminate:**
- "One-time exceptions" to fundamental rules
- Reactive `.gitignore` management
- Secrets in tracked config files, even temporarily
- Multiple issues on one branch
- Unmerged PRs accumulating scope

**Decision to record in `notes/decisions.md`:**
Secrets convention: all secrets in environment variables or `.env` only. Config files reference `${ENV_VAR}`. Files `.claude/settings.local.json`, `.mcp.json`, and `.env` must be in `.gitignore` before any tool configuration begins. Never accept secrets as plain text in chat.
