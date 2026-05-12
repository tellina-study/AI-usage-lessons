# Phase C — Расширенный proposal по методике презентаций

**Issue:** #52
**Дата:** 2026-05-12
**Базируется на:** Phase A (текущее состояние) + Phase B (критика рекомендаций) + явное требование пользователя «repo-first».

---

## 1. Архитектурный принцип: **repo-first, Drive — only render+publish**

```
[ library/lectures/lec-NN/ ]    ←  source of truth (git tracked)
        │
        │ render
        ▼
[ Google Slides на Drive ]      ←  published, для живой презентации и комментариев
        │
        │ pull comments
        ▼
[ GitHub issues / notes ]       ←  обратная связь возвращается в репо
        │
        │ feed back into edits
        ▼
[ обновление library/lectures/lec-NN/, новый render ]
```

**Жёсткие правила:**

1. **Никаких content-edit'ов в Drive напрямую.** Если правка нужна — открываем `library/lectures/lec-NN/`, правим там, ре-рендерим. Drive-версия пересоздаётся.
2. **Drive-версия одноразовая.** При re-render предыдущая Google Slides уходит в `archive/` (как папки документов сейчас).
3. **Комментарии в Drive — это feedback, не правки.** Skill `pull-deck-feedback` собирает их в issues.
4. **Идемпотентность.** Двойной рендер из одного `deck.yaml` даёт одинаковый результат (с точностью до слайд-IDs). Тестим это.

---

## 2. Раскладка `library/lectures/lec-NN/`

```text
library/lectures/lec-01/
  deck.yaml                  ← структура deck'а: метаданные + список слайдов с типами
  slides/
    s01-ice-breaker-cv.md    ← один слайд = один файл (легко diff'ать)
    s02-cover.md
    s03-poll-step1.md
    s04-poll-step2.md
    s05-instructor-frame.md
    ...
  notes/
    speaker-notes.md         ← сводные speaker-notes (для печати), генерируются из slides/*.md
    references.bib           ← академические источники, общая библиография лекции
  assets/
    images/
    diagrams/                ← .drawio + .png
    code/
      ice-breaker-cv/
        run.py
        requirements.txt
        backup/
  rendered/
    last-render.json         ← мета: presentation_id, slide_id_map, hash deck.yaml, дата
    slide-png/               ← PNG-снимки последнего рендера (для visual regression)
```

**Принцип «slide = file»:** диффабельно по одному слайду, можно делать PR на правку одного слайда без шума.

---

## 3. Schema: `deck.yaml`

Минимальная, но достаточная для всех slide-types.

```yaml
deck:
  lecture_number: 1
  title: "Введение — AI вокруг нас"
  audience: "бакалавры ИУ6, МГТУ Баумана, прошли ML, ежедневно пользуются AI"
  duration_min: 75
  central_question: "Как инженеру ИУ6 попасть в оставшиеся 10% AI-пилотов?"
  learning_outcomes: [LO1, LO4, LO6, LO7]
  language: ru
  master_template_id: null   # позже — id Google Slides шаблона

slides:
  - id: s01
    file: slides/s01-ice-breaker-cv.md
    type: live_demo
    duration_min: 3
    assertion: "Narrow AI уже работает на ноутбуке без облака — это рабочая инженерная лошадка"
    learning_goal: "Создать эмоциональный hook и снять страх 'AI = магия'"
    visual:
      pattern: external_demo
      backup: assets/code/ice-breaker-cv/backup/screenshot.png
    interaction: live_demo
    student_action: "увидеть AI в действии в этой комнате"
    references: [yolov8-ultralytics-2023, mediapipe-google]

  - id: s02
    file: slides/s02-cover.md
    type: cover
    duration_min: 0.5
    assertion: null   # cover не несёт тезиса
    learning_goal: "Зафиксировать контекст лекции"
    visual:
      pattern: title_block
    interaction: none

  - id: s03
    file: slides/s03-poll-step1.md
    type: poll_reveal
    step: 1
    duration_min: 1.5
    assertion: "Сейчас оцените сами — потом сравним с реальностью"
    learning_goal: "Активировать аудиторию, зафиксировать их prior"
    visual:
      pattern: poll_questions
      questions: 3
    interaction: hands_up
    paired_with: s04   # связка двух reveal-слайдов

  - id: s04
    file: slides/s04-poll-step2.md
    type: poll_reveal
    step: 2
    duration_min: 2
    assertion: "Разница между вашей оценкой и реальностью — это ваши слепые зоны про AI"
    learning_goal: "Создать осознание дельты, мотивировать на курс"
    visual:
      pattern: data_vs_estimate
    interaction: discussion
    paired_with: s03

  - id: s05
    file: slides/s05-instructor-frame.md
    type: assertion_visual
    duration_min: 2
    assertion: "Главный вопрос курса — не 'можно ли AI?', а 'НУЖНО ли и ГДЕ?'"
    learning_goal: "Установить рамку курса и центральный вопрос"
    visual:
      pattern: instructor_card_with_question
    interaction: none
    references: [ano-cifrovaya-ekonomika-2025, gartner-2025]
```

### Поля
- **id** — `sNN`, стабильный.
- **file** — `slides/sNN-*.md`, source текста и speaker notes.
- **type** — из библиотеки slide-types (см. §4).
- **duration_min** — для контроля ритма.
- **assertion** — основной тезис (для assertion-evidence типов; null для cover/divider/poll).
- **learning_goal** — что должно произойти со студентом.
- **visual** — паттерн визуала + специфичные параметры.
- **interaction** — `none / hands_up / discussion / live_demo / question / exercise`.
- **student_action** — что студент делает (опционально).
- **paired_with / step** — для reveal/progressive disclosure.
- **references** — ссылки на bibtex-ключи в `references.bib`.

### Schema-validation
Лёгкая JSON-схема в `templates/deck.schema.json`. Валидация запускается в pre-commit или в skill'е перед рендером.

---

## 4. Slide-types library (минимальная, 10 типов)

Каждый тип = layout + правила контента + чек-лист QA.

| Type | Когда | Layout (Google Slides master) |
|---|---|---|
| `cover` | Титул лекции | Большой title + meta-блок |
| `section_divider` | Разделитель раздела | Крупный номер + название раздела |
| `assertion_visual` | Содержательный слайд (основной тип) | Тезис сверху + большой визуал в центре |
| `process` | Последовательность шагов (3–5) | Numbered horizontal flow |
| `comparison` | Сравнение 2 вариантов | Два столбца, одинаковая структура |
| `quadrant` | 2×2 матрица | Quadrant с подписями осей |
| `data_block` | Цифры/инфографика | Крупное число + подпись + источник |
| `live_demo` | Внешнее демо/код | Минимальный слайд + backup-ссылка |
| `poll_reveal` | Опрос/reveal (2 шага) | Step1 — вопросы; step2 — данные |
| `summary` | 3 главных вывода | 3 крупных пункта |

### Поведение типа `assertion_visual` (главный тип)
- **Заголовок слайда = assertion** (полное предложение, не «Тема»).
- **Визуал в центре** = доказательство тезиса (схема, число, изображение).
- **Не больше 4 буллетов**, если без визуала — можно заменить на текст-блок.
- Speaker notes — что говорит преподаватель.

### Не входит сейчас (добавим по необходимости)
`hierarchy`, `dependency_chain`, `case_study`, `example_bad_good`, `exercise`, `reflection`, `sources`. Вводим, когда первый раз понадобится в реальной лекции.

---

## 5. Новые агенты (`.claude/agents/`)

### 5.1. `presentation-critic`
**Роль:** «Опытный методист, проверяет педагогический и визуальный дизайн».

**Чек-лист:**
- Каждый содержательный слайд имеет `assertion` (не «тема»).
- Одна мысль на слайд.
- Визуал не декоративный — играет роль доказательства/примера/якоря.
- Время слайда соответствует плотности контента.
- Цепочка слайдов читается как нарратив (есть переходы).
- Нет переполнения (по сводным данным из `slide-png/`).
- Соответствие `learning_outcomes` лекции (каждый LO покрыт минимум одним слайдом).

**Output:** markdown-отчёт с findings по слайдам (P0/P1/P2 severity), рекомендации, что переписать.

### 5.2. `student-simulator`
**Роль:** «Студент 3-го курса ИУ6 МГТУ Баумана. Прошёл курс ML, ежедневно использует ChatGPT/Copilot. Сидит на лекции 1 — впервые видит deck».

**Перспектива:** живая лекция, голос преподавателя присутствует.

**Чек-лист:**
- Что я понял из этого слайда?
- Что меня сбило с толку (термин без пояснения, переход непонятен)?
- Какие вопросы у меня возникли?
- Скучно ли мне? Где я отвлёкся?
- Совпадает ли уровень с моим ML-бэкграундом (не слишком тривиально и не слишком абстрактно)?

**Output:** «дневник студента» — комментарии по каждому из 5 слайдов от первого лица + сводный список вопросов и точек скуки.

### 5.3. `reader-simulator`
**Роль:** «Тот же студент, через 2 недели, готовится к РК1. Открыл слайды на повторение. Преподавателя нет. Только slides + speaker notes».

**Чек-лист:**
- Понимаю ли слайд из слайда + speaker notes БЕЗ воспоминания о лекции?
- Хватает ли контекста (определения, ссылки, источники)?
- Можно ли восстановить мысль преподавателя?
- Где speaker notes отсутствуют или слишком кратки?
- Где визуал был самодостаточен на лекции, но без слов теряет смысл?

**Output:** «отчёт читателя» — какие слайды self-contained, какие требуют преподавателя, что докручивать в speaker notes.

### Архитектурное замечание
Эти 3 агента — **read-only**, не редактируют контент. Их output идёт в `notes/issue-52-.../qa-reports/` и/или в комментарии к PR. Решает, что чинить, **оркестратор** (Claude Code) или пользователь.

---

## 6. Обновлённые skills

### 6.1. `/build-deck N` — переписать под repo-first

**Старый flow:** читает Google Doc → создаёт Google Slides с буллетами.

**Новый flow:**
1. Читает `library/lectures/lec-NN/deck.yaml` (источник истины).
2. Валидирует schema.
3. Рендерит каждый слайд через `mcp__workspace-mcp__batch_update_presentation`, используя layout'ы из master-template и тип слайда из `deck.yaml`.
4. Сохраняет `rendered/last-render.json` (presentation_id, slide_id_map, hash deck.yaml).
5. Экспортирует PNG каждого слайда в `rendered/slide-png/` (через download URL).
6. Обновляет `decks.yaml`.

**Пред-условие:** `deck.yaml` валиден; нет напрямую отредактированной Google Slides без коммита соответствующего обновления `deck.yaml`.

### 6.2. **Новый skill** `/draft-deck N` — генерация черновика `deck.yaml` из narrative-плана
**Цель:** мост между «план лекции в md-прозе» (как `notes/lecture-1-review/final/new-plan-v4-final.md`) и `library/lectures/lec-NN/deck.yaml`.

**Flow:**
1. Берёт план Л-NN.
2. Spawn'ит subagent (prompt: «инструктор-методист») — для каждого слайда: assertion, learning_goal, slide_type, duration.
3. Создаёт `deck.yaml` + `slides/sNN-*.md` (контент + speaker notes).
4. **Не рендерит в Google.** Это draft-этап.

### 6.3. **Новый skill** `/qa-deck N` — прогон через 3 агентов
**Flow:**
1. Читает `deck.yaml` + `slides/*.md` + `rendered/slide-png/`.
2. Параллельно spawn'ит:
   - `presentation-critic` — методический/визуальный отчёт.
   - `student-simulator` — отчёт «глазами студента в зале».
   - `reader-simulator` — отчёт «глазами читателя дома».
3. Сохраняет 3 отчёта в `library/lectures/lec-NN/qa-reports/{date}/`.
4. Сводит в `qa-reports/{date}/summary.md` — что починить.

### 6.4. **Новый skill** `/pull-deck-feedback N` — забрать комментарии из Google Slides
**Flow:**
1. `mcp__workspace-mcp__list_presentation_comments` для presentation_id из `decks.yaml`.
2. Маппит каждый комментарий на slide_id через `slide_id_map` из `last-render.json`.
3. Создаёт markdown-отчёт `library/lectures/lec-NN/feedback/{date}.md`.
4. (Опционально) создаёт GitHub issues для P0/P1 фидбэка.

### 6.5. Обновлённый `deck-editor` агент
- Источник: `library/lectures/lec-NN/deck.yaml` + `slides/`.
- Знает про slide-types и их layout'ы.
- При неясности — спрашивает оркестратора, не решает сам.
- Не делает direct-edit Drive вне рендера.

---

## 7. Master template для Google Slides

**Что это:** одна Google Slides, скопированная вручную в нужный folder, с layout'ами для каждого slide_type. Создаётся **один раз**, потом используется для всех 17 лекций.

**Layout'ы** (= slide-types из §4): cover, section_divider, assertion_visual, process, comparison, quadrant, data_block, live_demo, poll_reveal_step1, poll_reveal_step2, summary.

**Где создаётся:**
- Phase F — после approval.
- Я (как orchestrator) могу разово сделать в Google Slides UI (это не «edit content», а инфраструктура).
- Альтернатива: subagent через `create_presentation` + `batch_update_presentation` создаёт layout'ы программно. Менее красиво, но воспроизводимо.

**Решение по визуалу:**
- Без брендинга МГТУ пока (можно добавить шапку/футер).
- Шрифты: системные (Roboto / Arial) — переносимо.
- Цветовая схема: 1 акцент + 1 нейтральный.

→ Конкретику и владельца — в Phase E.

---

## 8. Pipeline (orchestration end-to-end)

```
1. /draft-deck N
   → deck.yaml + slides/*.md (черновик из narrative-плана)

2. (manual) review deck.yaml
   → правки в md/yaml в репе

3. /build-deck N
   → Google Slides по deck.yaml
   → rendered/last-render.json + slide-png/

4. /qa-deck N
   → critic + student + reader отчёты
   → summary.md

5. (manual) review summary
   → правки в slides/*.md и/или deck.yaml
   → goto 3 (re-render)

6. (live presentation in Drive)
   → собираем фидбэк через комментарии в Google Slides

7. /pull-deck-feedback N
   → feedback/{date}.md + (опционально) issues

8. (manual) cycle 5–7 после каждого проведения
```

---

## 9. Пилот: первые 5 слайдов Лекции 1 (Phase F)

**Подготовка:**
- Создать `library/lectures/lec-01/` со структурой §2.
- Перенести narrative-план v4 (только первые 5 слайдов) в `deck.yaml` + `slides/s01..s05.md`.
- Создать master template (или начать без — генерировать layout программно).

**Реализация (последовательно, с гейтами):**
1. **F.1.** Подготовить инфраструктуру: schema, master template, агенты critic/student/reader, новые skills (хотя бы заглушки).
2. **F.2.** Subagent делает `deck.yaml` + 5 markdown-файлов слайдов из плана v4.
3. **F.3.** Я (orchestrator) пересматриваю содержание. Без рендера.
4. **F.4.** Subagent рендерит 5 слайдов в **новую** Google Slides (старый deck Л1 не трогаем).
5. **F.5.** Запускаем `/qa-deck` — параллельно 3 агента.
6. **F.6.** Сводим отчёт, фиксим 3–5 главных замечаний.
7. **F.7.** Re-render. Сравниваем visual diff (PNG-snapshots).
8. **F.8.** Презентуем пользователю — обсуждаем, что работает, что нет, что менять в методике.

**Намеренные ограничения пилота:**
- Только 5 слайдов из 29.
- Только Лекция 1.
- Старая Google Slides Л1 не трогается (помечаем archive в `decks.yaml`).
- Никаких anti-pattern catalog'ов / global skill changes до Phase F.8 review.

---

## 10. Что добавляем в `notes/decisions.md` после approval

- Repo-first как архитектурный принцип (Drive = render+publish).
- Slide-types library как обязательный набор.
- Assertion-evidence как методический паттерн.
- Critic / student / reader как обязательные QA-агенты для образовательных deck'ов.
- Master Google Slides template owner и его расположение в Drive.

---

## 11. Что НЕ делаем сейчас (явно отложено)

- Slidev / web twin.
- PPTX-native pipeline.
- Figma kit.
- Visual regression CI (только snapshots сейчас, без diff-tooling).
- Полный набор slide-types (берём 10 на старт).
- Брендинг МГТУ.
- Бек-перенос наработок на Лекции 2–17 (только после стабилизации Лекции 1).
