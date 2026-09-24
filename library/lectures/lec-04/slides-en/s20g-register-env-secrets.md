---
id: s20g
type: case_study
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "\"Ignored by git\" and \"ignored by Claude Code\" are two different things governed by different config files: Claude Code read .env despite both .gitignore and .claudeignore, and a Bash subprocess walks around even an explicit deny rule on reading"
learning_goal: "Secrets are a separate, independently configured contract from the git conventions; a two-layer limit (.claudeignore + permissions.deny) and a three-layer scanner defense"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.3e [for-slide-s20g]"
references: [register-env-secrets, gitleaks, trufflehog]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study: left — an Ocean rounded box with the Register incident (icon key): Claude Code v2.1.12
  (2026-01-28) reads .env despite both .gitignore AND .claudeignore; the verbatim quote in a teal-framed
  monospace plate. Below it a second honest-limit block (icon shield-alert): permissions.deny(Read) does not
  block a Bash subprocess (`cat .env` walks around the rule) — two independent contracts, OS-level sandboxing
  required. Right — the three-layer defense (icon lock): (1) pre-commit Gitleaks, advisory, bypassable with
  --no-verify; (2) CI gate Gitleaks + TruffleHog verified, binding; (3) server-side push protection, holds
  even when client hooks are bypassed. Gold callout — what you commit and what the agent may read are two
  contracts; closing one does not close the other.
interaction: none
---

# Visible content

## Title bar
Secrets are a separate contract: .gitignore does not mean "the agent will not read it either"

## Body
[Left — the incident]

**The Register, 2026-01-28.** Claude Code (v2.1.12) read `.env` files containing secrets even when they were listed in both `.gitignore` and `.claudeignore` — the tool prints a warning about credentials and then prints the contents anyway. At least **4 open issues** at the date of publication.

*"Ignored by git" and "ignored by Claude Code" are two different things, governed by different config files.*

[Left, below — the second limit]

`permissions.deny` (for example, `Read(./.env)`) blocks the built-in file-reading tool — but it **does not block a Bash subprocess**: `cat .env` through Bash walks around the rule. Closing this needs **OS-level sandboxing**, not just an agent setting.

[Right — the three-layer defense]

**(1) pre-commit hook (Gitleaks)** — local and fast, but bypassable with `--no-verify`: an advisory barrier, not a binding one.

**(2) CI gate (Gitleaks + TruffleHog verified)** — on every PR, a binding gate: CI cannot be dodged by branching around the hook.

**(3) server-side push protection** — at the git-hosting level, holds even when client hooks are bypassed.

[Gold callout]
What you commit (`.gitignore`) and what the agent is allowed to **read** (`.claudeignore` / `permissions.deny`) are two different, independently configured contracts; closing one does not close the other.

## Speaker notes

Even a discipline as apparently settled as "we do not commit secrets" has a practical hole that opens specifically in the agent context. On 28 January 2026 The Register independently documented and verified the following: Claude Code, checked on version v2.1.12, reads .env files containing secrets even when they are explicitly listed in both .gitignore and .claudeignore — the tool prints a warning that the file contains credentials, and then prints the contents anyway. At the date of publication there were at least four open issues on GitHub. The source's key formulation demolishes an intuitive but wrong assumption: "ignored by git" and "ignored by Claude Code" are two different things, governed by different configuration files. A file being excluded from version control does not mean the agent will leave it alone either — the git ignore list and the agent's file access are independent systems with independent policies.

There is a practical but honestly incomplete mitigation: a permissions.deny rule in the agent settings blocks the built-in file-reading tool. It has a specific, checkable limit: a deny rule on Read does not block Bash subprocesses — the command cat .env executed through Bash walks around the rule, because the rule applies to one particular file tool rather than to every way of reading a file. Really closing the hole needs OS-level sandboxing — a restriction at the process level that applies to all of the agent's subprocesses.

The baseline defense is built in three layers of increasing strictness: Gitleaks as a rule-first pre-commit scanner, fast but bypassable with the --no-verify flag; the same Gitleaks plus TruffleHog in verified mode on every pull request in CI, which is already a binding gate because CI cannot be dodged; and server-side push protection on the git-hosting side, which holds even when client hooks are bypassed. The lesson: the convention about what to commit and the policy about what the agent may read are two different contracts.
