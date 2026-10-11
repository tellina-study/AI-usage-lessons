---
id: n66
type: code_artifact
duration_min: 1.25
assertion: "The two stages added two commit-confirmed files to the repository, and one that is planned without a commit — the line between \"written down\" and \"already working\" is shown on the slide, not hidden"
learning_goal: "The final repository tree with an explicit line between what a commit confirms and what is planned — the same discipline of not confusing a plan with a fact that was the theme of the whole session"
visual:
  pattern: file_tree_snapshot
  primary: "A leading line about the `.claude/` directory not existing at all on the way in. Under it the monospace listing: every new line marked with its stage and a provenance marker, the hook's with a commit number, the skill's with \"planned, no commit yet\". As a separate block, the growth of the instruction file from twenty-four lines and four sections to forty and five: the name of the single new section and, a line below, the third item appended by the hook to a section that already existed. At the bottom, as a caption, the slide's only caption."
  backup: "rework/block-z5-os-promezhutochnaya.md §A.2. .claude/settings.json и .claude/hooks/selftest-branch-guard.sh — ветка seminar-5-hook, коммит 9803643, сверено напрямую gh api …/git/trees (ARCHITECTURE.md §2а, rework/section-1-khuk.md §A.7/§A.16). Рост CLAUDE.md 24/4 → 40/5 ПЕРЕСЧИТАН в круге 4 после одобрения наряда 7 (WORK-ORDER-demo-repo.md): раздел Repository etiquette переехал во ВХОДНОЕ состояние, поэтому прибавка занятия — не два раздела, а один (Хук защиты ветки) плюс третий пункт в уже существующий Repository etiquette. Прежняя редакция печатала 20/3 → 40/5 и говорила «оба новых дал хук», что после переноса стало неверным и спорило с n07 (rework-r4/SVERKA-OTCHET.md, стык 6). Выход ступени 3 НЕ изменился: git show origin/seminar-5-hook:CLAUDE.md → 40 строк, 31 непустая, 5 ##-заголовков (ПРОВЕРЕНО НАПРЯМУЮ по клону, gh в окружении нет). Вход 24/19/4 = 20/16/3 на origin/main плюс переносимые наряд-7 четыре строки. Разница 40 − 24 = 16 строк, 31 − 19 = 12 непустых. ВНИМАНИЕ: вход — состояние ЦЕЛЕВОЕ, в самом репозитории наряд 7 ещё не выполнен. .claude/skills/deploy/SKILL.md — по плану блока скиллов, коммита на момент сборки нет; граница проводится НА СЛАЙДЕ, не в примечании. Промежуточное состояние CLAUDE.md «26 строк» не показывается ни здесь, ни на n02 (qa/number-provenance.md строка 31). [EN-track note: provenance kept verbatim in Russian — decision D7 in EN-TRACK-BRIEF.md.]"
---

# What appeared in the repository

## Assertion

The two stages added two commit-confirmed files to the repository, and one that is planned without a commit — the line between "written down" and "already working" is shown on the slide, not hidden.

## Visual

> "On the way into the session there was no `.claude/` directory in the repository."

```
github.com/tellina-study/signup-landing-demo    branch seminar-5-hook, commit 9803643

.claude/                                ← did not exist on the way in
  settings.json                         ← hook · confirmed by a commit
  hooks/selftest-branch-guard.sh        ← hook · confirmed by a commit
  skills/deploy/SKILL.md                ← skill · planned only, no commit

CLAUDE.md    24 lines / 4 sections  →  40 lines / 5 sections  ← hook · confirmed by a commit
  + ## Branch protection hook           ← the barrier and who it does NOT stop
  + 3rd item in Repository etiquette    ← written for the hook
```

> Two files are confirmed by a commit, one exists only in the plan: a record of future work is not the same as work done.

## Speaker notes

On the way into the session there was no `.claude/` directory here. Look at what is in it now — and at the markers on the right, they matter more than the tree itself.

A commit confirmed two lines: the settings file and the hook's self-test. The commit number is on the slide, the repository address too. Clone it and run the self-test — it will print for itself where the barrier stays silent.

The third line is the skill's file. It is planned, it has no commit yet, and the marker says so right on the slide. The session was about the difference between "a file is lying there" and "a mechanism fires"; hiding that difference in my own summary would be strange.

The instruction file grew from twenty-four lines to forty. There is one new section here, and the hook gave it: a description of the mechanism and of who it does not stop. The rule about branches was already in the file on the way in — that is what the first case started from; the hook appended a third item to it, about switching a branch with a separate command.

"Written down that it will happen" is not yet "already working".

---

**Reference.**

*What the commands that check this do.* `git clone <address>` takes the repository in full. `git checkout seminar-5-hook` switches the working copy to the branch where both confirmed lines live — they are not in the main branch. `git log -1` prints the last commit; its number should match the one on the slide. Running the self-test is one command from the repository root, and it prints the table of checks itself.

*If asked why the skill has no commit.* Because its file is written in the stage's plan but has not been entered into the repository yet. There are no grounds for passing that off as done, so the marker is on the slide. It is the same criterion we spent the hour measuring mechanisms by.

*If asked why there are now five sections when one was added.* There were four: three from the previous session and the repository etiquette we started the first decision point from. The hook added a fifth — the description of the barrier. Four plus one is five; the file's growth is from twenty-four lines to forty, that is sixteen lines, checkable by counting lines.

*If asked why the rule in text when there is a barrier.* The barrier stops the agent at the moment of the call. The text explains to the person who opens the repository why the call was stopped and who the barrier does not stop at all. One works, the other gets read.

*If asked about the branch.* The stage's work was done in a separate branch on purpose: it gets merged into the main one after a check, and that is exactly the rule the barrier guards.
