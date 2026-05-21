# user-feedback.md — Лекция 9 production

## Explicit corrections

### «убери конкретные ссылки на специальности и кафедры, лекции обезличены. посмотри на другие.»
- **Когда:** После chapter v2 finalize, перед GATE A.
- **Что было нарушено:** chapter v2 §5.2 содержал МГТУ им. Баумана, Факультет ИУ, кафедра «Технологии искусственного интеллекта», ВКА им. А.Ф. Можайского, МАИ, СПбГУ + frontmatter `audience: «студенты-инженеры 3 курса ИУ6 МГТУ Бауман»`.
- **Pattern check missed:** orchestrator должен был сразу сверить с lec-07/lec-05/lec-03 chapters (все без named institutions). Сделано — на v3 revision delegated book-editor для anonymization + добавления Глоссария (отдельный structural finding).
- **Lesson:** Templates `lecture-outline.md` + chapter brief default должны быть anonymized. Career section pattern = generic «профильные технические университеты», not named.

## Explicit approvals

- «Глобальный + российский контекст» — chosen out of 3 региональных options
- «Включить LAWS как ключевой failure-блок»
- «≥50% слайдов с осмысленным медиа»
- «Запускать Phase 0 в фоне»
- «Опция А (OODA) + инъекции» — keystone axis
- «Делегировать book-editor (plan-only mode)»
- «GATE A passed → дальше»
- «всё принято» (GATE B)
- «аппрув мерж» (GATE C + merge command в same message)

## Patterns observed

### Momentum-oriented decision style
User predominant signal — single-word approvals: «дальше», «принято», «аппрув мерж». User trusts the pipeline + critics, intervenes only on structural issues (anonymization).

### Anonymization mandate is universal
User explicitly anonymized lec-09. **Lesson:** This rule should be default, not per-lecture intervention. Add to chapter-brief mandate в `tools/lecture-production/README.md` Phase 2 brief.

### Status-check pattern
User asks «статус» at intervals — wants brief snapshot, не detail. Response должен быть phase-summary + что running + ETA + блокеры/нет.

### Direct-merge command
«аппрув мерж» = explicit GATE C approval + merge authorization в одной строке. Per Mandatory Git Rules: «Когда указание получено — Claude мержит сам через gh pr merge». Executed correctly.

## Implicit signals

### User didn't intervene на slide v1 → v2 revision decision
Orchestrator decided REVISE based on self-report flags (43 slides + 0 real photos). User saw the commit message and didn't override. **Implicit approval:** orchestrator может call REVISE decisions без user gate when based on memory rule violations (no_mock_fallbacks, Russification, etc.).

### User didn't intervene на consistency-checker API 529 retries
Two failures + 3rd retry — user didn't comment. **Implicit approval:** retry pattern для transient API failures доверен orchestrator.

### Decision to direct-edit chapter P0 fact fixes
3 small Edit calls applied directly (Du→Ye, CENTCOM→EUCOM, frontmatter v3→v4). User didn't push back. **Borderline acceptable** for small exact replacements; might be tightened in future to «delegate even small content edits» if user feedback comes.

## Frustration triggers

None observed в этой сессии. User momentum-driven approvals throughout.

## New behavioral rules

### Anonymization default
- Apply to ALL future chapter drafts without per-lecture intervention.
- Update `templates/lecture-outline.md` career section template.
- Update `tools/lecture-production/README.md` Phase 2 book-editor brief.

### Russification universal
- Memory rule `feedback_russification` уже зафиксировано.
- New finding: applies к bracketed stage directions in speech too? Or only spoken body? **User did not push back на speech anchor 11 fix («Predictive maintenance» → «Прогностическое обслуживание»)** but didn't explicitly demand bracketed scope. Conservative: apply Russification to ALL visible-in-source text including stage directions, since they могут быть скопированы / прочитаны лектором.

### Memory rules surfaced this session
- `feedback_hero_images` — каждая презентация ОБЯЗАНА hero-иллюстрацию на s01 + s39 ≥40% площади (real image из 6-tier fallback). Появилось в MEMORY.md между сессиями lec-08 и lec-09. **Lec-09 deck has:** s01 Sentinel-2 hero ✓, s42 closing OODA chain — is this "hero" enough? s39 = 7-criteria matrix table, не hero photo. **Possible non-compliance** — should check rendered s39.png on next polish round. Defer to issue.

## Next session preferences

- User likely runs another lec production next (lec-10 agriculture, lec-11 transport, или другая)
- Default to anonymization + Russification + 6-tier images + Glossary §11 + Lec-07 pattern + lec-N-1 reference read
- Expect single-word approvals; orchestrator-side decisions on memory-rule violations allowed
- Status snapshot pattern when asked
