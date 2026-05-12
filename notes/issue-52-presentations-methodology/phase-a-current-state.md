# Phase A — Текущее состояние генерации презентаций

**Issue:** #52
**Дата:** 2026-05-12
**Цель:** зафиксировать, что РЕАЛЬНО есть в проекте для сборки слайдов, и где у этого тонкие места.

---

## 1. Артефакты-источники (что инвентаризирую)

| Файл / артефакт | Роль |
|---|---|
| `.claude/skills/build-deck/SKILL.md` | Skill `/build-deck N` — основной публичный вход |
| `.claude/agents/deck-editor.md` | Subagent для исполнения |
| `templates/slide-outline.md` | Шаблон описания deck'а |
| `catalog/manifests/decks.yaml` | Реестр существующих deck'ов |
| `catalog/manifests/lectures.yaml` | Источник тем и `doc_id` для лекций |
| `catalog/exports/docs/lec-01-slides-plan-v3.1.md` | Старый план Л1 (26 слайдов) |
| `notes/lecture-1-review/final/new-plan-v4-final.md` | **Свежий улучшенный план Л1 v4 (29 слайдов)** |
| Google Slides `1BviVqnn7vtHGg09h22UzfUTyQswTHfvSXqol_JaRTyM` | Существующий deck Л1 (10 слайдов, status=draft) |
| `diagrams/`, `diagrams/exports/` | Источник диаграмм |

---

## 2. Что делает текущий `build-deck` SKILL

Шаги (SKILL.md, шаги 1–8):
1. Читает `lectures.yaml`, `decks.yaml`, `slide-outline.md`.
2. Если у лекции есть `doc_id` — читает Google Doc через `get_doc_as_markdown`.
3. Сканирует `diagrams/` и спрашивает онтологию SPARQL'ом, что иллюстрирует тему.
4. **Шаг 3 «Design slide structure»**: Title → Agenda → Content slides (`heading + 3-5 bullets + speaker notes + diagram?`) → Summary → Next lecture preview. **12–20 слайдов**.
5. Создаёт или обновляет `create_presentation` / `batch_update_presentation`.
6. Создаёт слайды с `predefinedLayout: TITLE_AND_BODY` и инсёртит текст в плейсхолдеры через `insertText`.
7. Обновляет `decks.yaml` и онтологию.

### Что фактически получается на выходе

Один тип слайда: «Заголовок + буллеты + примечания + (опционально) диаграмма». Это **классический корпоративный шаблон PowerPoint 2003-вида**, против которого выступает вся методика assertion–evidence.

Никаких других layout'ов:
- нет cover-слайда (используется generic title);
- нет section-divider'ов;
- нет «assertion + visual» (тезис + одно доказательство);
- нет process / hierarchy / comparison / case-study;
- нет poll-/reveal-слайдов (хотя план Л1 v4 их явно предполагает);
- нет progressive disclosure (один и тот же слайд с пошаговым появлением элементов реализуется как «несколько почти одинаковых слайдов» — у нас этого нет).

---

## 3. Что делает `deck-editor` агент

Файл `.claude/agents/deck-editor.md`:
- Перечислены MCP tools (Google Slides + Drive + drawio + RAG).
- 7 «conventions», все мягкие («следуй template», «используй batch_update», «обновляй manifest»).
- Workflow «New Deck» / «Update Deck» — список из 7–9 шагов, без проверки качества.

**Чего нет:**
- Проверки соответствия учебной цели слайда (нет связи `slide.learning_goal → LO лекции`).
- Проверки «одна мысль на слайд».
- Проверки на наличие «assertion» (тезис вместо темы).
- Симуляции студента/читателя.
- Никакой обратной связи, кроме «Report».

---

## 4. Что в `templates/slide-outline.md`

```markdown
# Slide Deck: {{title}}
## Metadata
- Lecture: {{lecture_number}}
- Google Slides URL:
- Last updated:
## Slide Sequence
### Slide 1 — Title
### Slide 2 — Agenda
### Slide 3 — {{topic}}
- Key points:
- Diagram:
- Notes:
### Slide N — Summary
- Key takeaways
- Next lecture preview
```

Это **markdown-скелет**, а не структурированная схема. Нет полей `assertion`, `visual_role`, `learning_goal`, `student_action`, `slide_type`, `interaction`. Subagent не может поставить себе задачу «сгенерируй слайд типа X» — потому что типов нет.

---

## 5. Что в `decks.yaml` сейчас

Две записи:
- Старая `.pptx` («ИИ и мир.pptx (old presentation)») — pptx-uploaded, не наша.
- **Лекция 1: «Введение — что такое AI и почему это важно», 10 слайдов, draft, создан 2026-03-31** — это deck, собранный ранним build-deck, до улучшенного плана v4.

То есть:
- В Drive лежит deck Л1, который не отражает ни v3.1, ни v4 план.
- Существующих 10 слайдов недостаточно для 75-минутной лекции (29 слайдов в v4).
- При новом запуске `/build-deck 1` он попадёт в ветку «Update existing deck» и будет править эту устаревшую версию, а не создаст новую — это ловушка.

---

## 6. Что в свежем плане Л1 v4 — материал для пилота

Из `notes/lecture-1-review/final/new-plan-v4-final.md`:

- **29 слайдов**, длительность 75 мин, центральный вопрос лекции.
- **Структурированная арка**: 0. Открытие+вовлечение → 1. Что такое AI → 2. Где мы сейчас → 3. Четыре способа → 4. Границы и безопасность → 5. Заключение.
- Каждый слайд имеет: описание, содержание, speaker notes, источники.
- Уже видно, что **типы слайдов разные**: live-демо, титульник, 2-шаговый poll-reveal, рамка с центральным вопросом, таймлайн, инфографика, сравнение-таблица.
- Это план в виде markdown-прозы. Чтобы автоматизировать сборку, его надо переложить в **структурированный deck.yaml** с явными `slide_type`.

### Первые 5 слайдов (для пилота):

1. **Слайд 1** — Ice breaker live-демо CV (3 мин). Тип: `live_demo`. Visual: реальная веб-камера.
2. **Слайд 2** — Титульный (0.5 мин). Тип: `cover`.
3. **Слайд 3** — Опрос «ваша оценка», шаг 1 reveal (1.5 мин). Тип: `poll_reveal_step1`.
4. **Слайд 4** — Данные РФ vs ваша оценка, шаг 2 reveal (2 мин). Тип: `poll_reveal_step2`.
5. **Слайд 5** — Обо мне + рамка лекции + центральный вопрос (2 мин). Тип: `instructor_intro_with_frame`.

**Эти 5 слайдов — уже сейчас неподъёмны для текущего build-deck**, потому что 4 из 5 не вписываются в Title+Body. Это идеальный отладочный набор: он сразу проявит ограничения существующего тулинга.

---

## 7. Какие агенты сейчас есть в `.claude/agents/`

| Агент | Назначение | Применим к слайдам? |
|---|---|---|
| `librarian` | Поиск, sync, export, index | косвенно (поиск исходников) |
| `course-curator` | Связи лекция↔материал | косвенно |
| `doc-editor` | Редактирование Google Docs | нет |
| `deck-editor` | Сборка/правка Google Slides | да, но он thin-wrapper |
| `issue-manager` | Issues / PR triage | нет |

**Чего нет (явно):**
- **Critic / instructional reviewer** — никто не задаёт «слайд несёт одну мысль? assertion есть? визуал не декоративный?».
- **Student simulator** — никто не проверяет «студенту понятно? слайд работает в его контексте?».
- **Reader simulator** — никто не проверяет «слайд читается без преподавателя?» (важно: студенты будут пересматривать слайды дома).

---

## 8. Найденные дыры (резюме для Phase B/C)

| Дыра | Проявление |
|---|---|
| Нет structured deck schema | Невозможно автоматически выбирать тип слайда |
| Нет slide-types library | Все слайды получаются Title+Body |
| Нет assertion-evidence паттерна | Заголовки слайдов = «темы», а не «тезисы» |
| Нет учебной валидации | Никто не проверяет связь слайд↔learning outcome |
| Нет critic/student/reader агентов | Нет петли обратной связи качества |
| Старый deck Л1 в Drive ловит «update» путь | При перезапуске испортит работу |
| План Л1 v4 живёт в md-прозе | Нет машиночитаемой версии для агента |
| Нет progressive disclosure | Reveal-слайды (3, 4 в v4) не реализуются как 2 слайда |

---

## 9. Открытые вопросы для пользователя

1. **Старый deck Л1** — оставляем как archive (move в Drive `archive/`) или удаляем из `decks.yaml`? Я предлагаю переместить в archive и обнулить запись.
2. **Формат контента deck**: пишем `library/lectures/lec-01/deck.yaml` (новый), или продолжаем держать narrative в `notes/lecture-1-review/final/new-plan-v4-final.md`? Я предлагаю первое — тогда есть source of truth.
3. **Pilot-deck** Л1 — собираем первые 5 слайдов в **новой** Google Slides (чтобы не портить существующую) и помечаем «pilot — first 5 slides only»? Я бы делал так.

→ Эти вопросы поднимутся в Phase E.
