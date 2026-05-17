# Tools / toolchain — рефлексия Лекции 4

## Рекуррентная toil (повторяется каждую лекцию — митигировать системно)

### T1. secret-scanner false-positive на security/QA-прозе
Pre-commit secret-scanner WARNING'ит на прозе со словами «secret-scan», «[VFY]», «RISK-1/2», цитатами QA-отчётов — каждый коммит лекции по безопасности/QA. Каждый раз: «Pre-commit checks passed» (не блокер), но шум + риск, что реальный секрет утонет в привычном false-positive.
**Митигация (IMP-6a):** задокументировать в `notes/mcp-limitations.md` / pre-commit как known-expected для lec-04-класса (security-контент); при будущей настройке — allowlist прозовых паттернов или snapshot-сравнение, чтобы WARNING срабатывал только на НОВЫЕ потенциальные секреты.

### T2. libreoffice пересобирает чужие lec-NN PDF + `~$*.pptx` lock
Каждый рендер deck → libreoffice трогает `library/lectures/lec-0X/rendered/*.pdf` других лекций + создаёт `~$*.pptx`. Guard `git checkout origin/main -- lec-01/02/03/07` + `find -name '~$*.pptx' -delete` гоняется вручную ПЕРЕД каждым commit/return.
**Митигация (IMP-6b):** вынести guard в один скрипт `tools/presentation-build/side-effect-guard.sh` (вызывается designer-агентом и оркестратором перед commit) — вместо копипасты команды в каждый бриф/шаг. Снижает риск пропуска.

### T3. Merge-конфликты от parallel-сессий (lec-05/06)
PR #109 пришёл CONFLICTING: (а) untracked stray-копии lec-05/lecture-5-review в working tree (parallel-сессия, уже merged в main) блокировали merge; (б) `notes/decisions.md` append-конфликт (обе ветки дописали в один хвост).
**Митигация (IMP-6c):**
- decisions.md append-конфликт неизбежен при параллельных сессиях. Convention: ВСЕГДА `git merge origin/main` в ветку ДО открытия GATE-C (а не после), чтобы конфликт ловился в production-фазе, не на merge-кнопке. Резолв append-only = объединить оба набора (никогда не выбирать одну сторону).
- untracked strays: оркестратор работает с git worktree-изоляцией при known parallel-сессии (CLAUDE.md Multi-Lecture Parallel Rule уже это предписывает — НЕ был применён здесь, т.к. lec-05/06 стартовали в другой сессии незаметно). Урок: проверять `git status` на чужие untracked в начале И перед merge.

## Что сработало (tools)
- `pdftoppm` + python-pptx XML-extract для independent grep видимого слоя — надёжная orchestrator-verification (поймал ложный designer TOTAL=0).
- suffix-ID + `build_lec04.py` sequence-вставка — рендер 36 слайдов без renumber, валидатор `assert base s01–s32` поймал бы дрейф.
- Backup-перемещение untracked strays в `/tmp` (обратимо) вместо `rm -rf` перед merge — безопасный разрешающий приём.
