---
id: s20g
type: case_study
section: "Раздел 3. Реализация — дисциплина и харнес"
duration_min: 3
assertion: "«Ignored by git» и «ignored by Claude Code» — две разные вещи, управляемые разными конфиг-файлами: Claude Code читал .env вопреки и .gitignore, и .claudeignore, а Bash-подпроцесс обходит даже явный deny-запрет на чтение"
learning_goal: "Секреты — отдельный, независимо настраиваемый контракт от git-конвенций; двухслойный предел (.claudeignore + permissions.deny) и трёхслойная защита сканерами"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.3e [for-slide-s20g]"
references: [register-env-secrets, gitleaks, trufflehog]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study: слева — Ocean rounded box, инцидент Register (icon key): Claude Code v2.1.12 (2026-01-28) читает
  .env вопреки .gitignore И .claudeignore; verbatim-цитата в teal-рамке моноширинным. Ниже — второй honest-limit
  блок (icon shield-alert): permissions.deny(Read) не блокирует Bash-подпроцесс (`cat .env` обходит правило) —
  два независимых контракта, требуется OS-level sandboxing. Справа — 3-слойная защита (icon lock): (1) pre-commit
  Gitleaks — advisory, обходим --no-verify; (2) CI-gate Gitleaks+TruffleHog verified — authoritative; (3)
  server-side push-protection — устойчив даже к обходу client-hook. Gold callout — «то, что коммитить, и то,
  что агенту читать, — два разных контракта; закрытие одного не закрывает другой».
interaction: none
---

# Visible content

## Title bar
Секреты — отдельный контракт: .gitignore не значит «агент тоже не прочитает»

## Body
[Слева — инцидент]

**The Register, 2026-01-28.** Claude Code (v2.1.12) читал `.env`-файлы с секретами, даже когда они перечислены и в `.gitignore`, и в `.claudeignore` — инструмент выводит предупреждение о credentials, но всё равно печатает содержимое. Минимум **4 открытых issue** на дату публикации.

*«"Ignored by git" and "ignored by Claude Code" are two different things, governed by different config files».*

[Ниже — второй предел]

`permissions.deny` (например, `Read(./.env)`) блокирует встроенный инструмент чтения — но **не блокирует Bash-подпроцесс**: `cat .env` через Bash обходит правило. Закрытие требует **OS-level sandboxing**, а не только настройки агента.

[Справа — 3-слойная защита]

**(1) pre-commit hook (Gitleaks)** — локально, быстро, но обходим `--no-verify`: рекомендательный барьер, не обязывающий.

**(2) CI-gate (Gitleaks + TruffleHog verified)** — на каждый PR, обязывающий гейт: CI не обойти веткой мимо hook'а.

**(3) server-side push-protection** — на уровне git-хостинга, устойчив даже к обходу клиентских hook'ов.

[Gold callout]
То, что коммитить (`.gitignore`), и то, что агенту разрешено **читать** (`.claudeignore`/`permissions.deny`), — два разных, независимо настраиваемых контракта; закрытие одного не закрывает другой.

## Speaker notes

Даже такая, казалось бы, решённая дисциплина, как «секреты не коммитим», имеет практическую дыру именно в агентном контексте. The Register 28 января 2026 года независимо задокументировал и верифицировал: Claude Code, проверено на версии v2.1.12, читает файлы .env с секретами, даже когда они явно перечислены и в .gitignore, и в .claudeignore — инструмент выводит предупреждение, что файл содержит credentials, но всё равно печатает их содержимое. На дату публикации — минимум четыре открытых issue на GitHub. Ключевая формулировка источника разрушает интуитивное, но неверное допущение: «ignored by git» и «ignored by Claude Code» — две разные вещи, управляемые разными конфигурационными файлами. То, что файл исключён из версионирования, не означает, что агент его тоже не тронет — git-игнор и agent-файловый-доступ — независимые системы с независимыми политиками.

Практическая, но честно неполная митигация — правило permissions.deny в настройках агента блокирует встроенный инструмент чтения файлов. Но у неё есть конкретный, проверяемый предел: правило deny на Read не блокирует Bash-подпроцессы — команда cat .env, выполненная через Bash, обходит правило, потому что оно применяется к конкретному file-tool, а не ко всем способам чтения файла. Реальное закрытие дыры требует OS-level sandboxing — ограничения на уровне процесса, применяющегося ко всем субпроцессам агента.

Базовая защита строится в три слоя разной строгости: Gitleaks как rule-first pre-commit-сканер — быстрый, но обходимый флагом --no-verify; тот же Gitleaks плюс TruffleHog в verified-режиме на каждый PR в CI — уже обязывающий гейт, потому что CI не обойти; и server-side push-protection на стороне git-хостинга — устойчив даже к обходу клиентских hook'ов. Урок: конвенция, что коммитить, и политика, что агенту разрешено читать, — два разных контракта.
