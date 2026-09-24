---
id: s53
type: failure_vignette
duration_min: 3.25
assertion: "A bad plan is worse than no plan at all — and the 100% failure was measured precisely with no check of whether the plan was current, so the measure is a direct one: reconcile the plan at the start and at the end of a session"
learning_goal: "The failure/limitation of case 2.3 with nothing cut: a stale plan is worse than not having one (13 pp, 100% across 30 runs) + the risk-reduction measure derived from the experiment's own condition (reconciling + the \"Reconciled: date\" line), Index Sickness (n=1, an honest caveat), how niche the practice is"
visual:
  pattern: failure_vignette
  primary: "A table of two sources: Evaluating Plan Compliance (bad plans hurt performance more than no plan at all) and Fresh Memory, Stale Plans (100% across 30 runs — with NO check of whether the plan is current). Directly under the table — the \"measure\" block: reconciling at the start and at the end of a session + the \"Reconciled: date\" line, three reasons why exactly this way, and the honest boundary \"once again a request in text\". Below — the Index Sickness case study (n=1, honestly flagged). At the bottom — the caveat about how niche the practice is."
---

# A bad plan is worse than no plan

## Assertion

A bad plan is worse than no plan at all — and the 100% failure was measured precisely with no check of whether the plan was current, so the measure is a direct one: reconcile the plan at the start and at the end of a session.

## Visual

| Source | Result |
|---|---|
| Evaluating Plan Compliance, 21,120 trajectories, SWE-bench Verified/Pro | "bad plans hurt performance more than no plan at all"; compliance with the plan drops by ~13 pp on the harder benchmark |
| Fresh Memory, Stale Plans, 30 controlled live scenarios | **with no check of whether the plan was current** the executor acted on a stale plan in all 30 cases (100%) |

The "what to do about it" block — the third line of the block from `CLAUDE.md`:

> At the start **and at the end** of a session, reconcile the plan with the state of the repository and add the line "Reconciled: `<date>`".

- **"And at the end", not only at the start.** Reconciling at the start protects the current session; reconciling at the end protects the next one — it writes down what came to light towards the end, while the context is still intact.
- **The "Reconciled: date" line.** Without it, the next session cannot tell a fresh plan from a three-week-old one: they look equally confident — the very mechanism that makes a bad plan worse than no plan.
- **Reconcile against the repository, not against memory.** The code and the change history survive context compaction.

The boundary of the measure: this is once again a request in text — it lowers the risk but does not remove it. A mechanical barrier that would not let you work from an unreconciled plan is beyond this session.

The "Index Sickness" case study (n=1, an honest caveat): a real project, 391 sessions in a month. The solution — physically separating the baseline instructions from an append-only session log. The result: the volume of AI instructions shrank by ~75%, and there were no relapses over the next ~150 sessions. n=1 action research by a single author, not a controlled experiment.

At the bottom: the "a file/a folder per task" practice is not mainstream yet — 2,853 real repositories, dominated by static context files.

## Speaker notes

"The numbers I promised. Twenty-one thousand one hundred and twenty trajectories, SWE-bench: having a plan helps on average. And right there, a direct quote from the authors: 'bad plans hurt performance more than no plan at all'. An agent's compliance with its own plan drops by about thirteen points on the harder benchmark.

And here is an experiment with a stricter condition: thirty controlled live working scenarios in which the plan was not checked for currency as the work went on. A stale plan was followed in literally all thirty cases. A task file that nobody updates is not a neutral piece of paper. It is a source of systematically wrong actions.

And read the condition of that experiment once more: a hundred percent refers to runs with no check of whether the plan was current. What was measured is not the inevitability of failure but the price of skipping one specific step. So the step has to be put back — and that is exactly the third line we wrote down a couple of slides ago: reconcile the plan with the state of the repository at the start and at the end of a session, and put a 'reconciled' line with the date into the file.

Three things in that wording are not accidental. The first is 'and at the end'. Reconciling at the start protects this session, reconciling at the end protects the next one: it writes down what came to light towards the end, while the context is still intact. In our scenario the session broke off in the middle of the third step, and no reconciling at the end happened — but reconciling at the start of the second session would have compared the plan against the code and shown: the step has been started, and how to do it is not stated in the file. Not a guarantee, but a place where the divergence becomes visible.

The second is the 'reconciled, date' line itself. Without it the next session cannot tell a fresh plan from a three-week-old one: both look equally confident, and that is exactly the mechanism that makes a bad plan worse than no plan. The date makes freshness visible. The third is to reconcile against the repository, not against memory: the code and the change history survive context compaction, memory does not.

And the boundary of this measure is the same as for the readiness gate from the first section: it is once again a request in text. It lowers the risk but does not remove it. With Manus, which we talked about on the previous slide, the same trick works inside a single session — they rewrite the to-do list to the end of the context; reconciling does the same thing between sessions. We are not putting up a mechanical barrier today that would make it impossible to work from an unreconciled plan.

There is also a case study very close to our situation: a real project, three hundred and ninety-one sessions in a month. The authors observe the agent losing touch with the project's actual semantics as the rules grow. The solution is the same separation we have been drawing all through this section: the stable kept apart from the current. The result — minus seventy-five percent in the volume of AI instructions, zero recurrences of the problem over the next hundred and fifty sessions. Honestly, up front: this is one project, one author, action research, not a controlled experiment.

And the last thing that has to be said plainly: the 'a file or a folder per task' pattern is not mainstream right now. A study of almost three thousand real repositories shows that static context files dominate. Individual leaders push the practice — but it is not an accepted norm yet."
