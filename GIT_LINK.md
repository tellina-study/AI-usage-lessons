# Git link (harness-control#306)

This folder is linked to `tellina-study/AI-usage-lessons` via the configured git connection `study_token` (https://github.com/tellina-study/AI-usage-lessons.git).

Auth method: `token` (stored token).

`git pull`/`git fetch`/`git push` run in this session's own shell are already authenticated -- the credential is set up in this session's environment, not stored in this repo's `.git/config`. You do not need to ask for, enter, or store a credential yourself. The `gh` CLI (e.g. `gh pr create`, `gh issue view`) is authenticated the same way, with the same credential -- no separate `gh auth login` needed either.

If git or `gh` ever DOESN'T work here, run `harness-git-check` -- it reports whether this session can actually authenticate (not merely whether an env var is set), names which mechanism authenticated it, and distinguishes *no credential at all* (exit 3, ask the operator to relaunch this session) from *a credential that was offered and rejected* (exit 2, the token itself must be replaced). `harness-git-check --check-only` reports without changing anything.

This directory is a git worktree of the folder's clone, checked out on its own branch `hc/session-35658a32-10b2f38b`. Getting work OUT: this branch is directly visible from the folder's own shared checkout via the shared `.git` object store, so a local merge there needs no push; pushing the branch and opening a PR is the standard route to review/merge elsewhere. Both are equally valid -- follow your own instructions/workflow.
