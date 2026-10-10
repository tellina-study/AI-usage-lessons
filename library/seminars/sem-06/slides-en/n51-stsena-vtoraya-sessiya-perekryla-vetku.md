---
id: n51
type: problem_scenario
duration_min: 1.5
assertion: "The developer opened a second session in the same directory so as not to wait for the first; the second started a branch of its own, and the first's unfinished edit rode off into somebody else's commit — both sessions reported that they had managed it"
learning_goal: "The opening of the third case: an observable problem with no solution, with a person and a named cost. The tasks in the scene DO NOT OVERLAP on a single file — that makes it visible that what breaks things is not the choice of work but the shared working copy: there is one branch in the directory for everyone, and switching it changes the files under somebody else's hands. The room does not yet know about a separate copy, or about the fact that there is no such copy inside one session"
visual:
  pattern: problem_scenario
  primary: "At the top — a short line about the state going in: an edit begun and not committed. Four steps of one story as a numbered list: the second session in the same directory, its own branch, two reports of success, the morning post-mortem. At the bottom — a highlighted line with the cost."
  backup: "Round 5 (issue 225): the scene was written from scratch, the former one (three weeks of diverging wordings from the diff reviewer) was removed along with the specialization case. The protagonist is the seminar's running protagonist (n01/n04), the project is the same fictional `signup-landing`; the scene introduces no checkable figures. The behavior of git in the scene is standard and checkable: a working copy stands on one branch for everyone working in it; `git checkout -b` carries uncommitted edits onto the new branch; `git add -A` takes everything lying in the directory, including somebody else's. There is not a single invented mechanism in the scene — only consequences of a shared directory."
---

# The second session started a branch. The first did not notice

## Assertion

The developer opened a second session in the same directory so as not to wait for the first; the second started a branch of its own, and the first's unfinished edit rode off into somebody else's commit — both sessions reported that they had managed it.

## Visual

> On the branch `fix/email-pattern` there is an edit under way: the address regular expression in `index.html` has been fixed, the message in `src/validate.js` has not yet. There is no commit so far.

1. A second task arrives: bump a dependency that is making the build complain. It does not overlap with the address validation on a single file. There is no reason to wait for the first session, and the developer opens a second — in the same directory, on the same repository.
2. The second session starts with a branch of its own: `git checkout -b chore/bump-deps`. The directory is one, the branch in it is one for everyone — and the uncommitted address edit moves onto the new branch along with the directory.
3. The second session finishes its work and takes into its commit everything it sees in the directory. Into the commit with the dependency goes the half-done address validation — for this session it is simply part of the state of the files.
4. The first session carries on from what it read earlier: it finishes the message, runs the tests, reports that the edit is ready. Its branch is no longer under it — the directory stands on the dependencies branch.

> **Both sessions reported success, and both were right taken separately. In the morning it turned out that the dependencies branch contains somebody else's unfinished edit, the address branch contains nothing, and half an hour went on the question of why the form tests are failing where nobody touched the form.**

## Speaker notes

The address-validation edit is the one from after the bug in front of the client: the form accepted a space before the domain. On the branch `fix/email-pattern` the work is begun and not committed: the regular expression in `index.html` is fixed, the error message in `src/validate.js` is not yet.

A second task arrives: bump a dependency that is making the build complain. It does not overlap with the address validation on a single file. There is nothing to wait for the first session for — the tasks are independent and the session is busy; that is exactly the ordinary reason to open a second. The developer opens it in the same directory, on the same repository.

The second session starts with a branch of its own: `git checkout -b chore/bump-deps`. This is where everything is decided. The directory is one, the branch in it is one for everyone working in that directory, and the uncommitted address edit moves onto the new branch along with the files.

Git did not stop this, and there was nothing to stop: a new branch is started from the current state of the directory and carries uncommitted edits with it. This is standard behavior, and it is what people count on when they discover they began work on the wrong branch. A refusal comes in a different case — when switching would touch the very lines you are editing. Here the files were different, and it all went through quietly.

The second session finishes its own work and takes into its commit everything it sees in the directory: `git add -A` takes modified files whole, without sorting out whose they are. The half-done address validation is, for this session, part of the state of the files. You cannot tell "mine" from "somebody else's" by the state: the state does not record who made it.

The first session carries on from what it read earlier: it finishes the error message, runs the tests, reports that the edit is ready. Its own branch is no longer under it — the directory stands on the dependencies branch.

Both sessions reported success, and each was right taken separately. In the morning it turned out that the dependencies branch contains somebody else's unfinished edit, the address branch contains nothing, and half an hour went on the question of why the form tests are failing where nobody touched the form.

This story has a property worth noticing separately: the tasks share not a single file. The address edit touches the markup and the validation script, the dependency bump touches the file with the list of packages. The answer "do not take overlapping tasks" does not work here, because they were not taken. What breaks things is the shared working copy itself, with any choice of work at all.

What was happening could have been seen earlier too: the name of the current branch is the same for both sessions, and it is in plain view. Nobody goes and looks at that spot — each session has its own task, and both of them look as if they are going fine.

The objection "my agent does not switch branches by itself" is worth checking before leaning on it: switching branches is the ordinary first step on a new task, and a project's instruction file demands it more often than it forbids it. A commit before launching the second session would have saved this story: there would have been something to come back to. It does not cancel one branch per directory, though, and the next pair of tasks will collide in the same place.
