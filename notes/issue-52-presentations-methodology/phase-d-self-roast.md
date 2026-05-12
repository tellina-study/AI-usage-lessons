# Phase D — Самопрожарка proposal'а

**Issue:** #52
**Дата:** 2026-05-12
**Объект жарки:** `phase-c-proposal.md`.

---

## 1. Чек-лист (CLAUDE.md «Roast-Before-Implement Rule»)

| Вопрос | Ответ | Действие |
|---|---|---|
| Это **simplest version**, что работает? | Скорее да — отказались от 70% рекомендации (PPTX/Figma/Slidev), но всё ещё **3 новых агента + 3 новых skill'а одной партией** | Раздробить на «минимальный пилот» и «полный пайплайн» |
| Нет ли **unverified deps**? | Master Google Slides template — не проверено, что layout'ы можно надёжно использовать через `batch_update_presentation` `slideLayoutReference` с custom layout'ом | Перед F.4 — провести 30-мин spike: создать тестовую презу, попробовать `slideLayoutReference: { layoutId: ... }` |
| Кто **owner каждого нового файла**? | Не у всех явно | Прописать в §6 ниже |
| Можно ли **изолировать риск**? | Riskи: (а) идемпотентность рендера, (б) комментарии→issues, (в) PNG-снимки. Все три можно отдельно тестировать | Из пилота вынести (б) и (в) — добавим позже |

---

## 2. Конкретные дыры в proposal'е

### 2.1. **Слишком много новых артефактов в один заход**
Proposal вводит сразу:
- `library/lectures/lec-NN/` структура (новая папка верхнего уровня для контента)
- `deck.yaml` schema + JSON validator
- 10 slide-types
- 3 новых агента (critic/student/reader)
- 3 новых skill'а (`draft-deck`, `qa-deck`, `pull-deck-feedback`)
- master Google Slides template
- обновление `build-deck` + `deck-editor`

→ **Это 8 новых движущихся частей одновременно.** Если пилот сломается — непонятно, в чём именно.

**Фикс:** в Phase F явно делим на 2 партии.
- **F-pilot (минимум для 5 слайдов):** structure `library/lectures/lec-01/`, `deck.yaml` (только реально использованные поля), 5 типов из 10 (`cover`, `live_demo`, `poll_reveal`, `assertion_visual`, ничего больше), агенты critic+student+reader **в простой read-only форме**, обновлённый `build-deck` или временный inline-рендер subagent'ом без skill-изации.
- **F-system (после успешного пилота):** schema-валидация, `/draft-deck`, `/qa-deck`, `/pull-deck-feedback` как полноценные skill'ы, master template, остальные slide-types по мере появления реальной нужды.

### 2.2. **`deck.yaml` schema может быть преждевременной**
Я расписал поля до того, как написан хоть один реальный `deck.yaml` для реального deck'а. Классический premature-design.

**Фикс:** в пилоте сначала вручную пишем `deck.yaml` для 5 слайдов, и только из реального опыта формализуем schema. Если поле `student_action` не используется — выкидываем. Если нужно `interaction.kind` — добавляем.

→ JSON-схему в `templates/deck.schema.json` **откладываем до конца Phase F**.

### 2.3. **Master template — критическая зависимость, не верифицирована**
Я предложил «layout'ы под каждый slide-type», но Google Slides API в `batch_update_presentation` имеет ограничение: `slideLayoutReference` принимает либо `predefinedLayout` (один из ~13 встроенных), либо `layoutId` (уникальный ID layout'а в пресентации). Создание custom layout'ов программно — возможно, но геморройно.

**Спайк:** до Phase F.4 я (orchestrator) выясняю, как именно работают custom layout'ы в Google Slides API. Если плохо — fallback: создаём слайды как `BLANK` layout и расставляем shape'ы программно.

### 2.4. **Идемпотентность рендера — заявлена, не проверена**
Я написал «двойной рендер из одного `deck.yaml` даёт одинаковый результат». На практике Google Slides API создаёт новые слайды с новыми `objectId`. Чтобы это работало:
- Либо хранить `slide_id_map` и при ре-рендере **обновлять existing slides** (`updateText` вместо `createSlide`+`insertText`).
- Либо **очищать всю презу** и пересоздавать с нуля (`deleteObject` для всех слайдов кроме титула).

**Решение для пилота:** второе (clean-and-rebuild). Это проще и достаточно. Идемпотентность по содержанию, не по slide IDs.

### 2.5. **Critic/student/reader — что они на самом деле читают?**
Я написал «читают `deck.yaml` + `slides/*.md` + `rendered/slide-png/`». Но:
- Critic должен видеть и YAML, и markdown, и PNG. Ок.
- Student должен видеть **то, что видит реальный студент** = только PNG слайдов + (опц.) speaker notes из markdown. **Видит ли он assertion как title? Да, он на PNG.** Чтение `deck.yaml` дало бы ему «знание из-за кулис» — это уже не симуляция студента.
- Reader — то же самое + (опц.) бамажная распечатка.

**Фикс:** в Phase F агенты получают:
- critic: всё (yaml + md + PNG)
- student: только PNG + speaker notes (если они «открытые»)
- reader: только PNG + speaker notes

### 2.6. **«Параллельно spawn'им 3 агента» — это деньги и время**
3 параллельных subagent-вызова × сложный контекст (5 PNG, markdown'ы) = заметная стоимость. Для **пилота из 5 слайдов** — норм. Для production-ритма (17 лекций) — нужен trigger «когда запускать QA».

**Фикс на потом:** `/qa-deck` запускается **только перед коммитом deck'а в "ready"** статус, а не на каждый рендер.

### 2.7. **Старая Google Slides Л1 — что делаем?**
Я предложил в `decks.yaml` пометить как archive, но **не удалять из Drive**. ОК, но нужно ещё:
- Переименовать в Drive: «[ARCHIVE 2026-05] Лекция 1 v0».
- Перенести в `archive/` папку Drive.
- В `decks.yaml` сменить `lecture: 1` → `lecture: null` или переместить в отдельную секцию `archived:`.
- В новом рендере **создать новую** Google Slides с именем «Лекция 1 v1 — Введение — AI вокруг нас».

→ Включить эти шаги в F.4 (subagent сделает).

### 2.8. **Refeedback loop через Google Slides comments — не верифицирован**
`mcp__workspace-mcp__list_presentation_comments` — есть в инвентаре `deck-editor.md`. Но я не проверил, возвращает ли он позиционные ссылки на конкретный slide_id. Если возвращает только тред-уровень — не сможем мапить на слайды.

**Фикс:** spike-проверка на пилотной презе — оставлю комментарий вручную, проверю response.

### 2.9. **Локализация slide-types на русский**
Я назвал типы английскими ключами (`assertion_visual`, `poll_reveal`). Для consistency с остальным проектом (русский UI, русский контент) — может стоит русские? **Нет:** ключи в YAML лучше английские (стандарт), а отображаемые названия — на русском в SKILL.md. Это просто, не правлю.

### 2.10. **Permissions для новых агентов**
Memory feedback `feedback_subagent_permissions.md`: «wildcards set, delegate everything freely». Но новые агенты — read-only по контенту, и им нужны workspace-mcp для PNG-снимков. Проверить, что `.claude/settings.json` (или local) разрешает соответствующие операции для новых названий агентов.

**Фикс:** в Phase F.1 — проверить `settings.json`, добавить агентов в permissions если нужно.

---

## 3. «Что я не учёл» (из user-памяти)

Просмотрел `~/.claude/projects/-home-levko-AI-usage-lessons/memory/MEMORY.md`:

- ✅ **`feedback_use_mcp_directly.md`** — не использовать curl/python workarounds. → Уточнено: рендер только через `workspace-mcp`. ОК.
- ✅ **`feedback_orchestration.md`** — issue-driven, subagent delegation, branch-per-task. → Соблюдено.
- ✅ **`reference_course_research.md`** — 29 курсов, per-lecture sources. → Не используется в этом proposal'е напрямую, но `references` в `deck.yaml` совместим.
- ⚠️ **`feedback_rag_crosslingual.md`** — «не добавлять переводы для починки RAG, чинить на query layer». → **Не релевантно слайдам напрямую**, но может всплыть при `/qa-deck`, если critic захочет искать аналоги в research/. ОК, отложу.

---

## 4. Уточнённый F-pilot (минимум)

**Изменения по сравнению с §9 Phase C proposal:**

```diff
F.1. Подготовить инфраструктуру:
-    schema, master template, агенты critic/student/reader, новые skills (хотя бы заглушки).
+    минимум:
+    - папка library/lectures/lec-01/ с базовой структурой
+    - 3 новых агента .claude/agents/{presentation-critic,student-simulator,reader-simulator}.md
+    - спайк: проверить custom layouts vs BLANK + shapes; выбрать подход
+    - спайк: list_presentation_comments — проверить, мапятся ли на slide_id
+    БЕЗ: schema validator, новые skills, master template (всё это — в F-system)

F.2. Subagent делает deck.yaml + 5 md-файлов слайдов из плана v4.
+    Поля deck.yaml — только реально нужные для 5 слайдов; lazy schema.

F.3. Orchestrator пересматривает содержание. Без рендера.

F.4. Subagent:
-    рендерит 5 слайдов в новую Google Slides (старый deck Л1 не трогаем).
+    (а) переименовывает старый deck Л1 в "[ARCHIVE 2026-05] Лекция 1 v0", двигает в archive/ папку Drive
+    (б) обновляет decks.yaml — старая запись в `archived:`
+    (в) создаёт НОВУЮ Google Slides "Лекция 1 v1 — Введение — AI вокруг нас" в работчей папке Drive
+    (г) рендерит первые 5 слайдов через подход, выбранный в спайке F.1
+    (д) сохраняет rendered/last-render.json (presentation_id, slide_id_map)

F.5. Запускаем 3 агента параллельно (без skill-изации, прямо Agent tool):
+    critic — видит deck.yaml + md + PNG
+    student — видит только PNG + speaker notes (без deck.yaml)
+    reader — видит только PNG + speaker notes
+    Результаты — в notes/issue-52-.../qa-pilot/

F.6. Orchestrator сводит summary, фиксим 3–5 главных замечаний.

F.7. Re-render через clean-and-rebuild (delete all slides except title, recreate).
+    Сравниваем visual diff (вручную глазами на PNG).

F.8. Презентуем пользователю.
+    GATE: решаем, что из найденного фиксим в системе (skills/agents),
+    что — точечный фикс контента, и переходим к F-system или не переходим.
```

---

## 5. Owner-карта новых артефактов

| Артефакт | Owner | Где |
|---|---|---|
| `library/lectures/lec-01/deck.yaml` | `deck-editor` (создаёт), пользователь+orchestrator (правят) | repo |
| `library/lectures/lec-01/slides/*.md` | `deck-editor` (черновик из плана), пользователь (финал) | repo |
| `.claude/agents/presentation-critic.md` | orchestrator (создаёт), пользователь approve | repo |
| `.claude/agents/student-simulator.md` | orchestrator (создаёт), пользователь approve | repo |
| `.claude/agents/reader-simulator.md` | orchestrator (создаёт), пользователь approve | repo |
| Новая Google Slides Л1 v1 | `deck-editor` (создаёт+пишет), no manual edit | Drive `02-lectures/lec-01/` |
| `notes/issue-52-.../qa-pilot/*.md` | 3 агента (write), orchestrator (sum) | repo |
| `decks.yaml` правки | `deck-editor` (после рендера) | repo |
| Спайки (custom layouts, comments mapping) | orchestrator (выполняет, fix или fallback) | session-only |

---

## 6. Что меняется в proposal'е (delta для Phase E)

**Чистые delta:**
1. Сокращаем F.1 до минимума (3 агента + 2 спайка). Skills, schema, master template — в F-system после approval F-pilot.
2. clean-and-rebuild идемпотентность вместо обновления-в-месте.
3. Critic видит yaml; student/reader — только PNG + speaker notes (правильная симуляция).
4. Старый deck Л1 — переименовать+переместить в archive Drive в F.4(а), новую создать v1 в F.4(в).
5. JSON-schema deck.yaml — после пилота, не до.
6. `/qa-deck`/`/draft-deck`/`/pull-deck-feedback` skills — после пилота, не до.
7. Permissions проверить в F.1.

**Что не меняется (стоит):**
- Repo-first архитектурный принцип.
- Assertion-evidence паттерн.
- 10 slide-types как ориентир (но реализуем 4 на старте).
- Critic/student/reader как 3 разных перспективы.
- pilot = первые 5 слайдов Лекции 1.
