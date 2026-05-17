# Improvements — конкретные изменения (Лекция 4 → не повторять)

Статус: [x] применено в этом PR · [ ] follow-up issue

## IMP-1 — Keystone-axis ENFORCED-проверка (главный quality-рычаг) [x]
**Проблема:** несущая ось A→D не была standalone keystone-слайдом до 1-го погружения → owner-браковка → ~5 циклов deck.
**Изменения:**
- [x] `CLAUDE.md` Anti-Patterns + Pre-USER-GATE Walkthrough Rule: пункт «несущая ось как keystone до первого погружения».
- [x] `.claude/agents/methodology-critic.md`: добавлен keystone-axis check в обязательный чек-лист (Phase 1 plan + Phase 4/7 deck).
- [x] `templates/lecture-outline.md`: обязательный пункт «Несущая ось → keystone-слайд Раздела 0».

## IMP-2 — Usage-limit ≠ subagent-failure (процессная дисциплина) [x]
**Проблема:** оркестратор сделал chapter-работу напрямую при usage-лимите субагента.
**Изменения:**
- [x] `CLAUDE.md` Subagent Rules: явная развилка классификации сбоя ПЕРЕД «do directly». usage/rate/quota-limit → ждать сброса + ре-делегировать, НИКОГДА не self-implement. specific (`feedback_subagent_usage_limit`) > generic.
- [x] memory `project_lec4_production` + `feedback_subagent_usage_limit` — нарушение зафиксировано, урок исправлен.
- [x] `notes/decisions.md` — синтез-запись.

## IMP-3 — Отраслевые лекции: tools-per-taxonomy-level в Phase-0/plan [x]
**Проблема:** named current tools per level отсутствовали до owner-запроса (#102); curl named-narrative без слайда (#103).
**Изменения:**
- [x] `templates/lecture-outline.md`: для L4+ обязательный блок «инструменты 2026 на каждый уровень несущей таксономии (вендор-режим + adoption-направление + anti-hype-граница + mode≠brand + инфраструктура≠уровень); volatile → [VFY-day-of]».
- [x] `CLAUDE.md` Anti-Patterns: «plan §5 named speech narrative без слайда» → проверять Phase-5 (deck-from-chapter), либо слайд, либо явное owner-обоснование устного якоря.

## IMP-4 — Pre-GATE orchestrator-independent grep TOTAL=0 (формализовать) [x]
**Проблема:** scaffold/§/[VFY]-leak рецидив; designer-self-grep ложный TOTAL=0.
**Изменения:**
- [x] `CLAUDE.md` Pre-USER-GATE Walkthrough Rule: orchestrator-independent grep по rendered pptx видимому слою (паттерн ВКЛЮЧАЕТ словесные scaffold-фразы: «точк* возврата», «— в главе», «payoff», «возвращаемся N», «не вводим нового»), цель TOTAL=0; self-report субагента НЕ засчитывается как verification.

## IMP-5 — GATE-C DoD включает manifest → produced [x]
**Проблема:** lectures.yaml lec-NN→produced — забытый follow-up каждую лекцию (lec-03/05/06 батчили отдельным PR #97/#103).
**Изменения:**
- [x] `catalog/manifests/lectures.yaml`: lec-04 → produced (закрытие #99, в этом PR).
- [x] `CLAUDE.md` Phase Gating / lecture-production: GATE-C definition-of-done включает «lectures.yaml lec-NN status → produced».

## IMP-6 — Рекуррентная toil [частично x, частично follow-up]
- [x] `notes/mcp-limitations.md` / decisions: secret-scanner false-positive на security-прозе — known-expected, не блокер (документировано).
- [ ] **follow-up issue:** `tools/presentation-build/side-effect-guard.sh` (вынести libreoffice-guard из копипасты в скрипт) — IMP-6b, отдельная инфра-задача.
- [x] decisions: convention «`git merge origin/main` в ветку ДО GATE-C» (ловить parallel-конфликт в production-фазе, не на merge-кнопке); decisions.md append-конфликт = объединять оба набора.

## Метрика успеха
Следующая отраслевая лекция: 0 owner-интервенций класса «нет keystone-оси» и «нет tools-per-level» (IMP-1+IMP-3 должны их полностью предотвратить на Phase-1). Цель — ≤1 owner-структурная интервенция post-APPROVE (только чистый вкус, не планёрные пробелы).
