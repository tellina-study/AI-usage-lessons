# Reflection — Tools & Git (сессия #78/#82, 2026-05-15/16)

## Git / repo hygiene

1. **squash-merge ломает `git rev-list --count origin/main..branch` как признак «смержено».**
   Многие локальные ветки показывали «N commits ahead» при том, что их работа уже в `main` (squash-merge схлопывает историю). Достоверная классификация — **через merged-PR**: `gh pr list --state merged --json number,headRefName`.
   → **Reusable cleanup pattern:** ветку считать удаляемой, если у неё есть merged PR (headRefName ∈ merged list), НЕ по diff с main. Добавлено в decisions.md.

2. **`git push origin --delete <много рефов>` отработал частично и тихо.**
   Первый батч (~28) удалил часть, оставил 10; `grep -c deleted` дал 0 (вывод на stderr/формат `- [deleted]`). Реальную картину дал `git branch -r` после `--prune`. Ретрай добил остаток.
   → **Урок:** после batch-удаления remote-веток **всегда верифицировать `git branch -r`**, не доверять exit code / grep по выводу push. Ретраить остаток. В decisions.md.

3. **git worktree от `origin/main` когда локальный main не может ff.**
   Локальный `main` застрял на старом коммите из-за untracked `library/lectures/lec-02/` (конфликт overwrite). Чтобы базировать правки #82 на #79-версиях, сделал `git worktree add /tmp/wt-... -b <branch> origin/main` — изолированно, не трогая рабочее дерево пользователя. После merge — `git worktree remove --force` + `branch -D`.
   → **Reusable:** «нужно базироваться на remote, а local dirty/stale» → worktree от origin/<base>, не ломая локальное состояние.

4. **`comm` для сравнения файловых деревьев чувствителен к префиксу пути.**
   `find .` даёт `./chapter.md`, `git ls-tree` (после sed) — `chapter.md`. Несогласованный префикс дал ложный список «local-only». Авторитетным был **пофайловый `git show origin/main:path | diff -`** по пересечению — показал 0 различий в конфликтующем наборе.
   → **Урок:** сравнение repo-state — нормализовать пути на обеих сторонах ИЛИ использовать пофайловый content-diff, не голый `comm`.

5. **lossless-разбор untracked-блокера sync.**
   Паттерн: бэкап всего untracked-каталога в `/tmp` → удалить → `git merge --ff-only` → extra-артефакты остаются в бэкапе под решение пользователя. Ничего не теряется, дерево чистое.

## Pre-commit / прочее

6. **Secret-scanner ложно срабатывает на arXiv-URL/ID в research-таблицах.**
   `Checking for secrets... WARNING: Possible secrets` на строках с `arxiv.org/abs/2309.12288` и т.п.; checks всё равно passed, коммит прошёл.
   → Не блокер; знать, что arXiv-ссылки в md триггерят warning. В decisions.md (не в mcp-limitations — это pre-commit hook, не MCP).

## Перенос в decisions.md
Findings 39–42 (merged-PR-as-truth; verify-remote-delete; worktree-from-origin; path-normalize-compare) + заметка про secret-scanner false-positive.
