# Reflection — workflow (Лекция 5 production, issue #100)

## Git / process compliance

**Соблюдено полностью:**
- No work without issue (#100 создан до старта); branch-per-task; каждый commit `#100`; никогда не push в main напрямую; merge только по явной команде владельца («одобрить и сразу мерж» на GATE C).
- **Worktree-изоляция от активной lec-04-сессии — 0 контеншена.** lec-04 на `issue-99` в main-repo всё время; lec-05 в `/tmp/lec-05-wt` от чистого main; branch-ref через `git update-ref refs/heads/issue-100-...` после каждой фазы. Финальная проверка: main-repo осталась на issue-99 с 12 нетронутыми tracked-изменениями lec-04. ENFORCED Multi-Lecture policy валидирована (3-я подряд: lec-04/05/06).
- Phase Gating: GATE 0/A/B/C — каждый explicit user-approval, следующая фаза не стартовала без одобрения. Pre-gate walkthrough перед каждым GATE (4.5/8.5/11.5).
- Roast-Before-Implement: применён к плану (Phase 1) и к этой рефлексии (отфильтровал 7 наблюдений → 2 реальных P1, без issue-флуда).

**Сбои/трение:**
- **MANDATORY artifact-sync молча не сработал с первого раза.** Compound-команда `cd /tmp/lec-05-wt && ... && cp src dst` оставила cwd в worktree → `cp` получил src==dst («are the same file»), sync в main-repo НЕ произошёл. Поймано inode-check'ом (стат-сравнение), пере-сделано абсолютными путями. **Урок: процедуру sync документировать с абсолютными src+dst + обязательным inode/rsync-верификатором; никогда не полагаться на cwd-relative пути в compound с `cd`-в-worktree.**
- pre-gate ad-hoc greps (pacing 144, WPM 794) — ложные срабатывания на split-deck/крудовом regex; не блокировали (поймал глазами + пере-спавн critic'а), но отняли цикл. **Урок: pre-gate не должен полагаться на ad-hoc orchestrator-скрипты для метрик, погнавших verdict — делегировать ре-верификацию профильному critic'у.**

## Phase gating эффективность
- Critic-фаза поймала неверный self-report (WPM) — REVISE сработал по назначению. Pre-gate Lec-N-1-check предотвратил ложный P1 (changelog-в-теле = конвенция lec-04). Это валидация: дисциплина окупается.
