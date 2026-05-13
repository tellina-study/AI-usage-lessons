---
name: pre-user-gate
description: Pre-USER-GATE walkthrough — orchestrator self-review before presenting GATE to user. Reduces user feedback rounds.
---

# Pre-USER-GATE Walkthrough

## Purpose

После critic-approve, ДО presenting USER GATE — orchestrator делает self-review для catch issues что critics miss. Cuts user feedback rounds (Лекция 1 had 3 rounds после critic-approve).

«Critics проходят там, где user отклоняет» — паттерн из Лекции 1 v3 production. Critics проверяют compliance с playbook (палитра, motif, footer-tax, англицизмы, LO coverage), но **не проверяют relevance, terminology drift, schema readability, structural coherence, designer-extras**. Pre-USER-GATE — orchestrator-level дублирование user-perspective.

## When to invoke

Before each USER GATE in lecture-production pipeline (см. `tools/lecture-production/README.md` §3):
- **GATE A** (chapter approved) — `mode=chapter`
- **GATE B** (slides approved) — `mode=slides`
- **GATE C** (final, all 3 artifacts) — `mode=final`

## Arguments

`/pre-user-gate mode=<chapter|slides|final> lecture=<N>` — например `/pre-user-gate mode=slides lecture=1`.

Если аргумент не дан — спросить, какая лекция и какой gate.

## Pre-flight

- `library/lectures/lec-NN/chapter.md` (если `mode=chapter` или `final`).
- `library/lectures/lec-NN/slides/*.md` + `library/lectures/lec-NN/rendered/snapshots/sNN.png` (если `mode=slides` или `final`).
- `library/lectures/lec-NN/speech.md` (если `mode=final`).
- Все critics уже отметили APPROVE (в `qa-reports/{date}/SYNTHESIS.md`).

Если что-то не готово — STOP, не запускать walkthrough на incomplete артефакты.

## Steps

### 1. Visual sweep (для slides — `mode=slides` and `mode=final`)

- Open all PNG snapshots: `library/lectures/lec-NN/rendered/snapshots/sNN.png`.
- For each slide:
  - 5-second look — can I state main message? (Anthropic-style 5-second test).
  - Schema slides (matrix / quadrant / layered / cycle / pipeline / timeline / architecture) — verify Schema Readability Checklist passed (cross-ref `tools/presentation-build/README.md` §5.5).
  - Flag schemas where I can't recall message in 5 sec — that's failure → P0 list.

### 2. Speaker notes read (для slides — `mode=slides`)

- Read 5-7 random speaker notes (random sample, not first/last).
- Verify per-note:
  - 150-300 words (count roughly).
  - Connected text (paragraphs, not bullet list of layout descriptions).
  - **No «Лектору» section** (cues for lecturer go to speech.md, not notes).
  - **No layout descriptions** («левый верхний угол: иконка», «справа: chart» — это для дизайнера, не для студента).
  - **No режиссёрские cues** в notes («пауза 5 сек», «спросить аудиторию» — go to speech.md).

### 3. Checklist (для slides — `mode=slides` / `mode=final`)

Каждый item — pass/fail:

- [ ] All schemas pass Schema Readability Checklist (§5.5).
- [ ] No designer-added extras: «Лектору» = 0, «Вы здесь» в visible content = 0, «мин» в visible (not metadata) = 0, subtitle добавленный по инициативе = 0, callback frame от designer = 0.
- [ ] No terminology drift (cross-artifact grep по watched terms лекции — например «Приложение-робот» variants).
- [ ] No orphan references к удалённым slides (grep speech / chapter / other slides на старые sNN ID).
- [ ] Pacing math sums correctly (sum of `duration_min` per slide = lecture total).
- [ ] Palette consistent — Ocean Gradient + Teal + Gold only, no anti-pattern colors (red, generic blue).
- [ ] Gold ≥1×/slide.
- [ ] 0 footer-tax (LO codes / методические комментарии в видимой области).
- [ ] 0 неестественных англицизмов (стейкс / фоллбек / etc. — sourced from chapter tone-rules).
- [ ] 0 «Лектору» секций в notes (округ #1 round 3 fix).

### 4. Cross-artifact consistency check (для `mode=final` only)

Проверить cornerstone concepts aligned:
- **Central question** идентичен в chapter §intro, slide cover, speech opening.
- **Ключевые типизации** (например, «4 типа реализации AI», «чек-лист из 4 пунктов», «3 модуля курса × 17 лекций») — same wording, same count, same examples в всех 3 артефактах.
- **Roadmap / структура курса** идентична в chapter, slide «карта», speech.
- **Specific facts** identical: dates, numbers, attributions, benchmark values.
- **Terminology unified** (grep по списку ключевых терминов лекции).

### 5. Pre-flight checklist actionability (для speech — `mode=final`)

В `speech.md` обычно есть «Подготовка перед лекцией» / «Pre-flight checklist» секция. Проверить:
- Каждый pre-flight item actionable (не abstract).
- **0 orphan references** к удалённым слайдам (Лекция 1 v3 имела `[s26 pre-flight для ARC-AGI]` после удаления s26).
- **Live data refresh items** explicit: «verify ARC-AGI numbers — день до лекции», «check freshness Llama / Kimi releases» — для AI tools/benchmarks с refresh cadence < 1 month.
- Cross-ref deck.yaml: для каждого pre-flight item — есть соответствующий live slide? (нет ссылок на удалённые).

### 6. Designer-extras grep (для slides — `mode=slides` / `mode=final`)

Технически — grep across all `library/lectures/lec-NN/slides/*.md`:

```bash
grep -nE "Лектору|Вы здесь|^\s*мин\s*$" library/lectures/lec-NN/slides/*.md
```

Acceptance:
- «Лектору» — should be 0 (round 3 #1 fix).
- «Вы здесь» в visible content (не в YAML metadata) — should be 0.
- «мин» в visible (не в YAML `duration_min`) — flag as suspicious.
- Subtitle в s02a-style cover — flag (designer adds by default, user removes).
- callback frames без brief — flag.

## Output

Return a report to orchestrator:

```markdown
# Pre-USER-GATE walkthrough — лекция N, mode=<>

## Summary
- Total checks: K
- Passed: M
- P0 issues: X
- P1 issues: Y

## P0 issues (blockers — must-fix before GATE)
1. [sNN] schema_quadrant — axis labels outside, can't read scale at 50%
2. [speech.md] orphan reference к s26 (deleted slide)
...

## P1 issues (should-fix before GATE)
1. [sNN] speaker notes 90 words (target 150-300)
...

## Recommendation
- [ ] PRESENT USER GATE (no P0/P1, all checks pass)
- [X] FIX FIRST then re-run pre-user-gate (P0 found)
```

## Failure handling

Если найдены P0/P1 issues:
- **DO NOT present USER GATE** to user.
- Spawn revision agent (`book-editor` для chapter / `presentation-designer` для slides / `speech-writer` для speech) с конкретным P0/P1 list.
- After revision — **re-run pre-user-gate** на refreshed artifacts.
- Repeat пока pre-gate-pass.
- Только после pass — present USER GATE с message: «Я провёл pre-gate walkthrough, нашёл N issues, исправил все. Передаю на approve.»

Если 3+ revision cycles на pre-user-gate без convergence — STOP, escalate to user: «Не могу довести артефакт до pre-gate-pass за 3 раунда — концептуальный issue, нужен ваш input».

## Что НЕ делает skill

- НЕ заменяет critic agents (они запускаются ДО pre-user-gate, на Phase 3/7/10).
- НЕ исправляет issues сам — спавнит revision agents.
- НЕ presenting USER GATE без pass.
- НЕ ignore-ит P0 («можно показать пользователю, он сам решит» — нет, fix first).

## Ссылки

- Pipeline: `tools/lecture-production/README.md` §3 (где gate'ы), §3.5 (cascade tracking).
- Slides QA: `tools/presentation-build/README.md` §5.5 (Schema Readability Acceptance Gate), §9 (anti-patterns).
- Build orchestration: `.claude/skills/build-deck/SKILL.md` (Phase 6.5).
- Reflections: `notes/reflections/2026-05-13-lec-01-v3-rebuild/REFLECTION-CONSOLIDATED.md` (исходный rationale).
