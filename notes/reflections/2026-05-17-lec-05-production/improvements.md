# Improvements — Лекция 5 production reflection (issue #100)

| # | Priority | Effort | Target | Action | Issue |
|---|---|---|---|---|---|
| I-1 | **P1** | S | `.claude/skills/pre-user-gate/SKILL.md` + `tools/lecture-production/README.md` §3 | **Self-reported producer метрика, погнавшая verdict, ре-верифицируется профильным critic'ом с ЕГО токенайзером — не ad-hoc orchestrator-скриптом.** Добавить в pre-gate (mode=final/chapter/slides) шаг: «если REVISE был из-за метрики (WPM/strict-in%/word-count) и producer заявил fix — спавн focused critic re-check (узкий scope, та же методика Phase N), НЕ полагаться на orchestrator-grep». Producer-агенты: self-reported метрика помечается «требует critic-ре-верификации», не «PROVEN». | create → #111 |
| I-2 | **P1** | S | `tools/lecture-production/README.md` §8 (Multi-Lecture Parallel) + `notes/decisions.md` | **MANDATORY artifact-sync hardening.** Зафиксировать sync-сниппет: абсолютные src+dst, НИКОГДА `cd`-в-worktree в том же compound; обязательный пост-верификатор (inode-diff или `rsync --checksum` + `ls` подтверждение). Silent-failure mode (cp src==dst) обязан ловиться before GATE. | create → #112 |
| I-3 | P2 | S | `.claude/skills/pre-user-gate/SKILL.md` | pre-gate pacing/aggregate-greps по split `deck.yaml`+`deck-part2.yaml` обязаны scope'иться к per-slide entries (исключать `totals:`/metadata) ИЛИ использовать deck `totals.slide_times_sum_min` + critic. Не ad-hoc `grep|awk` сумму по обоим файлам. | decisions.md (bundle, no issue) |
| I-4 | P2 | S | `templates/lecture-outline.md` + `tools/presentation-build/README.md` | Формулировать slide-count lock как **«N content slides + структурные divider'ы через suffix-ID (НЕ входят в LOCK-счётчик)»**. Убирает Phase-5/8 неоднозначность «LOCKED=32 vs deck 33». | decisions.md (bundle, no issue) |
| I-5 | P3 | — | — | Валидации (no action): Lec-N-1-check предотвратил ложный P1 (changelog-в-теле = конвенция); usage-limit re-spawn сработал; worktree-изоляция 3+ параллельно — 0 контеншена. Зафиксировать как подтверждённые в decisions.md. | decisions.md |

## Сводка
- **2 P1 → GitHub issue** (I-1 pre-gate self-report re-verify, I-2 sync hardening).
- **2 P2 + 1 P3 → notes/decisions.md** (без отдельных issue — низкий effort, doc-level, bundle).
- Roast применён: из 7 наблюдений сессии только 2 дотянули до P1-issue; остальное — doc-level или валидации. Без issue-флуда.
