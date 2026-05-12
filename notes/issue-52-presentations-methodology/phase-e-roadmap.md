# Phase E — Роадмап: разбивка #52 на 5 sub-issues

**Issue parent:** #52 (становится EPIC — «Презентационная методика»).
**Дата:** 2026-05-12
**Принцип:** маленькие изолируемые задачи; каждая — своя ветка + PR + DoD; gate'ы между задачами.

---

## Структура

```
EPIC #52 — Презентационная методика
├── Sub-issue 1 — Setup PowerPoint MCP + 3 агента + базовая структура  [F.1]
├── Sub-issue 2 — 1-слайдный спайк (s05 Лекции 1) + выбор template     [F.2]
├── Sub-issue 3 — 5/6-слайдный пилот Лекции 1 (s01-s05/06)             [F.3-F.5]
├── Sub-issue 4 — Стабилизация методики (decisions, schema, skill)     [F-system, после пилота]
└── Sub-issue 5 — Factory: остальные слайды Л1 + перенос на Л2-Л17     [Long-term]
```

Прогресс: каждое подзадание зависит от предыдущего (gate). Начинаем с #1 после approval.

---

## Sub-issue 1 — Setup PowerPoint MCP + 3 агента + структура

**Объём:** инфраструктура. Никакого контента слайдов.

**Что делаем:**
1. Установить `office-powerpoint-mcp-server==2.0.7` через pip (локально).
2. Зарегистрировать в `.mcp.json` (секреты не нужны — full local Python).
3. Verify: `claude mcp list` показывает `powerpoint`.
4. Smoke-тест: subagent создаёт пустой PPTX через MCP, сохраняет в `/tmp/`.
5. Создать **3 агента** (`.claude/agents/`):
   - `presentation-critic.md` — методист (vision-enabled, видит yaml/md/PNG).
   - `student-simulator.md` — студент ИУ6 в зале (видит только PNG + speaker notes).
   - `reader-simulator.md` — два режима: `text-only` (читает md без рендера) и `rendered` (PNG + notes через 2 недели).
6. Создать `tools/presentation-build/README.md` — setup, MCP-команды, visual-loop workflow, slide-types library (первые 4 типа: cover, assertion_visual, poll_reveal, live_demo).
7. Обновить `CLAUDE.md` — добавить блок «Presentation Pipeline» в Working Conventions.
8. Создать пустую структуру `library/lectures/lec-01/` (deck.yaml пустой, slides/, assets/, rendered/).
9. Установить `libreoffice` (если не стоит) для PNG-snapshot из PPTX.

**DoD:**
- ✅ MCP сервер `powerpoint` отвечает на `list_tools`.
- ✅ 3 агента в `.claude/agents/`, каждый начинается с REQUIRED READING ссылки.
- ✅ `tools/presentation-build/README.md` написан.
- ✅ `CLAUDE.md` ссылается.
- ✅ Структура `library/lectures/lec-01/` готова.
- ✅ Smoke-тест: пустая PPTX создаётся.

**Ветка:** `issue-NN-pptx-mcp-setup`
**Размер:** ~0.5 дня.
**Гейт:** до Sub-issue 2 ничего не двигается.

---

## Sub-issue 2 — 1-слайдный спайк (s05 Лекции 1)

**Объём:** один слайд — отладка визуального цикла.

**Что делаем:**
1. Берём **s05** из плана v4 (`notes/lecture-1-review/final/new-plan-v4-final.md`) — *«Обо мне + рамка лекции + центральный вопрос»* как `assertion_visual` тип. Применяем methodical fix: на спайке делаем именно **s05b — рамка + центральный вопрос крупно** (не «обо мне»).
2. Subagent (`deck-editor` или прямой Agent) делает черновик `library/lectures/lec-01/slides/s05b.md` + кусок `deck.yaml`.
3. Subagent рендерит через PowerPoint MCP **без reference template** (чистый python-pptx). Сохраняет в `library/lectures/lec-01/rendered/spike/lec01-s05b.pptx`.
4. **Визуальный цикл:**
   - Сделать snapshot: PPTX → PNG через libreoffice headless (в `rendered/spike/snapshots/`).
   - Subagent (или критик-агент) **читает PNG визуально** через Claude vision.
   - Описывает что видит → находит проблемы → правит через MCP → re-snapshot.
   - Лимит: 5-7 итераций. Лог итераций в `rendered/spike/iteration-log.md`.
5. **Решение по template** (orchestrator + user):
   - Если визуально OK → продолжаем без template в Sub-issue 3.
   - Если требуется template → выбираем 2-3 community-кандидата, применяем на тот же s05b, сравниваем PNG, выбираем.
6. Результат записываем в `notes/issue-52-.../spike-result.md`.

**DoD:**
- ✅ Один слайд s05b отрендерён через PowerPoint MCP.
- ✅ Лог итераций визуального цикла (что видел → что менял → результат).
- ✅ PNG-снимок финальной версии — глазами «годен / не годен на широкую публику».
- ✅ Принято решение по template-подходу для пилота.
- ✅ Если template выбран — добавлен в `tools/presentation-build/templates/`.

**Ветка:** `issue-NN-pilot-spike-s05`
**Размер:** ~0.5-1 день.
**Гейт:** user approves «slide looks good enough» → Sub-issue 3.

---

## Sub-issue 3 — 5/6-слайдный пилот Лекции 1

**Объём:** полные первые 5-6 слайдов Лекции 1.

**Что делаем:**
1. **Применяем methodical fixes** (D8):
   - **s01** — Ice breaker live-demo CV (без изменений).
   - **s02** — Cover, выводим **центральный вопрос крупно** (D8 фикс).
   - **s03** — Poll: **2 вопроса вместо 3** (третий «кто проверяет ответы AI» переезжает в раздел про галлюцинации, не в пилот).
   - **s04** — Data vs estimate (без изменений).
   - **s05a** — Обо мне (новый, отколот от s05).
   - **s05b** — Рамка + центральный вопрос (отколот от s05).

   → 6 слайдов в пилоте.

2. **Reader-text-only** прогон: subagent читает только `slides/*.md` без рендера, проверяет методический текст. Отчёт → `library/lectures/lec-01/qa-reports/reader-text-only.md`. Если есть issues — фиксим до рендера.

3. **Render** все 6 слайдов через PowerPoint MCP (с template из спайка). Visual-loop по каждому слайду.

4. **3 QA агента параллельно** (после рендера):
   - `presentation-critic` — yaml + md + PNG.
   - `student-simulator` — PNG + видимые speaker notes.
   - `reader-simulator (rendered)` — PNG + speaker notes.
   - Каждый отчёт → `library/lectures/lec-01/qa-reports/`.

5. **Сводка** — orchestrator сводит 3 отчёта в `qa-reports/summary.md`. 3-5 главных правок.

6. **Re-render** с фиксами. Глазами сравниваем.

7. Результат: PPTX в `library/lectures/lec-01/rendered/lec-01-pilot.pptx` + PNG-snapshots всех 6 слайдов.

**DoD:**
- ✅ deck.yaml + 6 slides/*.md в `library/lectures/lec-01/`.
- ✅ Финальный PPTX + PNG-snapshots всех 6 слайдов.
- ✅ Reader-text-only отчёт + 3 QA отчёта от агентов.
- ✅ summary.md с фиксами.
- ✅ User глазами approves: «годно для проведения лекции».

**Ветка:** `issue-NN-pilot-lec01-first-5`
**Размер:** ~1-2 дня.
**Гейт:** user approves → Sub-issue 4.

---

## Sub-issue 4 — Стабилизация методики

**Объём:** превратить наработки пилота в воспроизводимый процесс.

**Что делаем:**
1. **Финализируем slide-types library** в `tools/presentation-build/README.md` — теперь знаем, что реально работает (использованные 4-5 типов + open list).
2. **Формализуем `deck.yaml` schema** (только реально использованные поля). Опционально — JSON-schema в `templates/deck.schema.json`.
3. **Обновляем `/build-deck` skill** — переписываем под новую методику (PowerPoint MCP + visual-loop + 3 QA агента). Заменяет старый build-deck SKILL.md.
4. **Обновляем `deck-editor` агент** — текущая обёртка над Google Slides API заменяется на работу с PowerPoint MCP + visual-loop.
5. **Обновляем `notes/decisions.md`**:
   - Repo-first как принцип.
   - PowerPoint MCP (GongRzhe форк) как primary.
   - Visual-loop как обязательная фаза.
   - 3 QA агента (с двумя режимами reader).
   - Anti-pattern catalog (что НЕ делаем — список найденного на пилоте).
6. **Обновляем CLAUDE.md** — финальная редакция блока про presentation pipeline.

**DoD:**
- ✅ `/build-deck` skill переписан и работает.
- ✅ `deck-editor` обновлён.
- ✅ `notes/decisions.md` дополнен.
- ✅ `tools/presentation-build/README.md` — финальная версия с slide-types.
- ✅ CLAUDE.md обновлён.

**Ветка:** `issue-NN-methodology-stabilization`
**Размер:** ~0.5-1 день.
**Гейт:** методика готова → можно начинать factory.

---

## Sub-issue 5 — Factory: остальные слайды + перенос на Л2-Л17

**Объём:** масштабирование. Это **долгосрочная** задача, разобьём на этапы.

**Этапы (каждый — своя мини-issue / PR):**

### 5.1. Завершить Лекцию 1 (слайды 6-29)
- Используем готовый pipeline.
- Отрабатываем оставшиеся slide-types: `process`, `comparison`, `data_block`, `quadrant`, `diagram_slide` (drawio через MCP).
- Возможно нужны новые типы — добавляем по мере появления.
- DoD: полный deck Лекции 1 готов.

### 5.2. Лекция 2 как stress-test factory
- Совершенно другая тема (архитектура трансформеров) — много схем и формул.
- Проверяем: переносится ли pipeline без боли? Хватает ли slide-types?
- DoD: Лекция 2 готова, найденные дыры — в decisions.md.

### 5.3. Skill `/pull-deck-feedback` (когда понадобится)
- Только когда первый внешний рецензент даст комментарии в Drive.
- Skill: read PPTX comments → map to slide_id → markdown report.
- Может стать своей issue.

### 5.4. Лекции 3-17 (одна-две на спринт)
- Поточно, по приоритету (близко к проведению).
- Каждая лекция — своя мини-issue.

**DoD overall:** все 17 лекций имеют рабочие decks. Достижимо за семестр.

**Гейт:** этот sub-issue открывается **после** Sub-issue 4 approval, и сам разбивается на меньшие задачи по мере движения.

---

## Сводка зависимостей

```
#52 EPIC ──▶ Sub-1 ──▶ Sub-2 ──▶ Sub-3 ──▶ Sub-4 ──▶ Sub-5 (long-term)
              │         │         │         │
              │         │         │         └── stabilizes methodology
              │         │         └── pilot validates
              │         └── spike validates tool
              └── infra ready
```

**Принцип:** ни одного «через голову» — каждая зависит от предыдущей. Между ними — explicit user gate.

---

## Что нужно от пользователя для старта

После этого роадмапа — **approval на Sub-issue 1** (и я создаю под него issue + ветку). Дальше каждое подзадание — своя итерация с гейтом.
