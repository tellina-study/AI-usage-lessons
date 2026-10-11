---
id: n54
type: mechanics_map
duration_min: 0.75
assertion: "A separate working copy is a directory of files of its own and a branch of its own, with a history shared with the main copy; it is set up with one launch flag, and more in it is shared than it seems"
learning_goal: "The mechanics of the move the breakdown chose: what exactly a separate copy gives and what it does not. The supporting line is the shared directory of the repository's internal data: it is precisely because of that directory that work does not have to be carried anywhere out of a copy, and precisely why a copy stays part of the same repository rather than a separate clone"
visual:
  pattern: mechanics_table
  primary: "At the top — a line about what this thing is, with the launch command inline. Below — a table in two substantive columns: what in a copy is its own and what is shared with the main one. At the bottom — a line about what a copy does not bring with it."
  backup: "The harness documentation, the section on isolating sessions with copies, read by direct curl on 2026-10-07 (not by summarizing WebFetch — notes/mcp-limitations.md [#225-1]). Verbatim: \"A git worktree is a separate working directory with its own files and branch, sharing the same repository history and remote as your main checkout\"; the flag and the defaults — \"Pass --worktree or -w with a name… By default, the worktree is created under .claude/worktrees/<name>/ at your repository root, on a new branch named worktree-<name>\"; \"Run the command again with a different name in another terminal to start a second isolated session\"; what is shared — \"The repository's .git directory: git commands in a worktree write to the main repository's shared .git directory\", project-level plugins, and the \"Yes, and don't ask again\" permissions, which are saved into the main copy's `.claude/settings.local.json` and apply in every copy; \"A worktree is a fresh checkout, so initialize your development environment there\", carrying over files outside version control — `.worktreeinclude`. The git command for setting one up by hand comes from the same section (`git worktree add ../project-feature-a -b feature-a`). The quotes and the links with the date they were read are in qa/krug5-subagent-keys3.md §5."
---

# A copy of your own: what in it is its own and what is shared

## Assertion

A separate working copy is a directory of files of its own and a branch of its own, with a history shared with the main copy; it is set up with one launch flag, and more in it is shared than it seems.

## Visual

> A separate working copy — a directory of files of its own and a branch of its own; the history and the remote repository are the same as the main copy's. In git this is a `worktree`. A launch with the `--worktree` flag and a name creates it under `.claude/worktrees/<name>/` on the branch `worktree-<name>`; the same launch with a different name in another terminal brings up a second isolated session. By hand the same thing is done by `git worktree add ../project-fix -b fix`.

| Its own in every copy | Shared with the main copy |
|---|---|
| the files in the directory — a branch switch in one copy does not change the files in another | the repository's internal directory: commands from a copy write into the shared history, so a commit from a copy is visible everywhere and the work does not have to be carried anywhere |
| the branch and the uncommitted state | plugins installed at project level |
| a working environment of its own: dependencies and everything not under version control are brought up in the copy separately | a permission granted once by answering "don't ask again": it is saved into the main copy and applies in all of them |

> A fresh copy arrives without whatever is not under version control: dependencies are not installed in it, local settings files are not in it. Which of those to carry over into every new copy is specified by a separate list.

## Speaker notes

A separate working copy — a directory of files of its own and a branch of its own; the history and the remote repository are the same as the main copy's. In git this is called a worktree.

It looks like a second directory next to the main one: inside it the same project tree, the same file paths, a different branch. Two directories, one repository.

It is set up with one launch flag: `--worktree` with a name creates a copy under `.claude/worktrees/<name>/` on a new branch, `worktree-<name>`. The same launch with a different name in another terminal brings up a second isolated session — and that is the standard way of running two tasks at once. By hand the same thing is done by `git worktree add ../project-fix -b fix`.

Three things are a copy's own. The files in the directory: a branch switch in one copy does not change the files in another, and that is exactly what broke in the scene. The branch and the uncommitted state. And the working environment: dependencies and everything not under version control are brought up in the copy separately.

More is shared with the main copy than it seems, and the first shared thing settles all the rest — the repository's internal directory. Commands from a copy write into the shared history, so a commit made in a copy is visible from the main directory immediately, and work does not have to be carried anywhere out of a copy. Hence the difference from a second clone of the repository: a clone is a separate repository with a history of its own, and work is carried between repositories out of it; a copy shares the history, so a branch from a copy is taken by an ordinary merge. For parallel work on one project it is that property that settles things.

The second shared thing is plugins installed at project level. The third is worth remembering separately: a permission granted once by answering "don't ask again" is saved into the main copy's settings and applies in all of them. The convenience is obvious — nobody wants to confirm the same thing in every new copy. The flip side: a permission granted inside a copy goes on applying after the copy itself has been removed.

A fresh copy arrives without whatever is not under version control: dependencies are not installed in it, local settings files are not in it. That is the ordinary reason the first attempt to build the project in a new copy fails. Which of those files to carry over into every new copy is specified by a separate list — it lies in the repository and is read when the copy is created.

On disk space: the project's files in every copy are its own, the internal directory is shared. For a source repository that is usually not much; for a repository with heavy binaries it is worth counting in advance — a copy takes a long time to bring up and takes up as much as a working tree.

A copy is removed once the work has been merged; if anything uncommitted is left in it, you will be asked about that on the way out. Abandoned copies pile up on disk and in the branch list — that is ordinary tidying, which does not happen by itself.

You can see what you have with one command: `git worktree list` prints the directory and the branch of every copy, including the main one. It is also the command to start a post-mortem with when it is unclear which directory the work is currently going on in.

What a copy would have changed in the scene we examined. The second session, launched in a copy of its own, starts a branch in its own directory; the first one's files stay where they were, with the uncommitted edit on its branch. The second session's commit is visible from the main directory immediately, because the history is shared. Bringing two pieces of work together still has to be done by a branch — a copy neither cancels that nor promises to.
