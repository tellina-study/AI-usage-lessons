# build-deck

Build/rebuild a PowerPoint (PPTX) presentation for a lecture using the repo-first pipeline + visual loop + 3 QA agents.

## Role

You are an orchestrator. **Do NOT render slides yourself.** Delegate rendering to `presentation-designer` agent and QA to `presentation-critic` + `student-simulator` + `reader-simulator` agents. Your job is to coordinate, gate phases, synthesize results.

## ОБЯЗАТЕЛЬНОЕ ЧТЕНИЕ перед инвокацией

1. **`tools/presentation-build/README.md`** — pipeline + slide-types + visual-loop + anti-patterns.
2. **`notes/mcp-limitations.md`** — известные баги PowerPoint MCP + workaround'ы.
3. **`notes/decisions.md`** § «2026-05-12 — Presentation pipeline» — anti-pattern catalog + iteration journey.

## Arguments

`/build-deck N` где N — номер лекции (1-17). Пример: `/build-deck 3`.

Если аргумент не дан — спросить, какую лекцию строить.

## Pre-flight (before starting)

Проверить готовность:
- `mcp__powerpoint__get_server_info` отвечает (PowerPoint MCP живой).
- `which mmdc convert rsvg-convert libreoffice pdftoppm` — все 5 утилит доступны.
- `library/lectures/lec-NN/deck.yaml` существует и содержит `slides: [...]`.
- `library/lectures/lec-NN/slides/sNN-*.md` существуют для каждой записи в `deck.yaml`.

Если что-то не готово — STOP, report пользователю.

## Execution

### Phase 1 — Read source

```
1. Read library/lectures/lec-NN/deck.yaml
2. Read all library/lectures/lec-NN/slides/*.md
3. Read catalog/manifests/lectures.yaml — lecture N entry
4. (optional) Read notes/lecture-N-review/final/new-plan-vN-final.md если есть narrative source
```

### Phase 2 — Reader-text-only QA (ДО рендера)

Спавнить `reader-simulator` agent в режиме `text-only`:
- Читает только `slides/*.md` без PNG.
- Проверяет методический текст ДО рендера.
- Отчёт → `library/lectures/lec-NN/qa-reports/{YYYY-MM-DD}/reader-text-only.md`.

Если P0 issues найдены — STOP, фиксить source markdowns, повторить.
Если только P1/P2 — фиксить инкрементально или продолжать с пометками.

### Phase 3 — Render через presentation-designer

Спавнить `presentation-designer` agent с инструкцией:
- Читать `library/lectures/lec-NN/deck.yaml` + `slides/*.md`.
- Применять Ocean Gradient + Teal palette + Gold highlight ≥1×/слайд.
- Применять Visual motif (Ocean rounded box) на каждом content слайде.
- Visual loop **минимум 3 итерации на слайд** (Anthropic principle: «assume there are problems»).
- Output: `library/lectures/lec-NN/rendered/lec-NN-pilot.pptx` + `snapshots/sNN.png` + `iteration-log.md` + assets.

Designer должен прочитать `.claude/agents/presentation-designer.md` (его playbook) — там палитра, типы слайдов, anti-patterns.

После завершения — orchestrator смотрит snapshots глазами через Read tool.

### Phase 4 — 3 QA agents в параллель (после рендера)

Спавнить **в одном сообщении** (parallel):
1. `presentation-critic` — методист + визуальный (yaml + md + PNG).
2. `student-simulator` — студент в зале.
3. `reader-simulator` mode=`rendered` — студент через 2 недели.

Каждый пишет отчёт в `library/lectures/lec-NN/qa-reports/{YYYY-MM-DD-vN}/`:
- `presentation-critic.md`
- `student-simulator.md`
- `reader-rendered.md`

### Phase 5 — Synthesize + fix iteration

Orchestrator:
- Сводит 3 отчёта в `qa-reports/{YYYY-MM-DD-vN}/SYNTHESIS.md`.
- Identifies convergent findings (≥2 agents agree) — это блокеры.
- Identifies unique findings — каждое оценить severity.
- Подготовить top-N (5-10) правок для следующей итерации.
- Представить пользователю: «согласен на эти фиксы? нужны ли другие?»
- После approval — спавнить fix iteration через presentation-designer (короткий subagent с конкретным списком).

### Phase 6 — Repeat until acceptable

Повторять Phase 4-5 пока:
- User approve визуально OK для проведения лекции.
- Все P0 закрыты.

Каждая итерация архивируется в `library/lectures/lec-NN/rendered/archive-vN/` (orchestrator делает `mv` через Bash перед новой итерацией).

### Phase 7 — Update manifest + commit

После accept:
- Update `catalog/manifests/decks.yaml` — добавить/обновить запись для лекции N (status: pilot/draft/final, version: vN, snapshots дата).
- Commit на feature branch + PR.

## Output (deliverables)

- `library/lectures/lec-NN/rendered/lec-NN-pilot.pptx` — финальный PPTX.
- `library/lectures/lec-NN/rendered/lec-NN-pilot.pdf` — PDF render.
- `library/lectures/lec-NN/rendered/snapshots/s01.png ... sNN.png` — финальные snapshots.
- `library/lectures/lec-NN/rendered/iteration-log.md` — лог всех итераций.
- `library/lectures/lec-NN/rendered/build_vN.py` — build script (чтобы воспроизвести).
- `library/lectures/lec-NN/rendered/assets/{icons,charts,diagrams,illustrations}/*` — все assets.
- `library/lectures/lec-NN/qa-reports/{YYYY-MM-DD}/reader-text-only.md`.
- `library/lectures/lec-NN/qa-reports/{YYYY-MM-DD-vN}/{critic,student-simulator,reader-rendered,SYNTHESIS}.md`.

## Что НЕ делает skill

- НЕ рендерит сам — делегирует presentation-designer.
- НЕ проверяет качество — делегирует 3 QA agents.
- НЕ загружает в Drive — пилот всё локально (Drive integration отложена).
- НЕ коммитит без approval пользователя.

## Если что-то падает

- MCP error → проверить `notes/mcp-limitations.md`. Если новая limitation — добавить запись по шаблону.
- libreoffice/pdftoppm/mmdc/ImageMagick недоступны → STOP, попросить установить.
- presentation-designer не справляется → orchestrator смотрит snapshots глазами, формирует точечный fix-prompt и спавнит снова.
- 5+ итераций без прогресса → STOP, обсудить с пользователем (возможно концепция слайда нуждается в пересмотре, не дизайн).

## Ссылки

- Pipeline: `tools/presentation-build/README.md`
- Designer playbook: `.claude/agents/presentation-designer.md`
- Anti-patterns + journey: `notes/decisions.md`
- MCP gotchas: `notes/mcp-limitations.md`
