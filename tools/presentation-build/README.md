# Presentation Build Pipeline

Source-of-truth: this file. Любой агент, работающий со слайдами курса, читает этот файл **первым**.

---

## 1. Архитектурные принципы

1. **Repo-first.** Source — `library/lectures/lec-NN/deck.yaml` + `slides/*.md`. Готовый PPTX лежит рядом в `rendered/`. Google Drive — только публикация и сбор обратной связи (отложено в pilot).
2. **Visual-loop сборка.** Агент работает как живой дизайнер: render → snapshot PNG → читает визуально через Claude vision → правит через MCP → re-snapshot. Лимит: 5-7 итераций на слайд.
3. **Slide-types library.** Каждый слайд — один из определённых типов (см. §4). Title+body как универсальный шаблон **запрещён**.
4. **Assertion-evidence.** Заголовок слайда = тезис (полное предложение), не «тема». Визуал = доказательство тезиса.
5. **Diagrams as shapes.** Схемы строятся примитивами PowerPoint MCP (`add_shape` + `add_connector`), а не как embedded картинки. Embed только когда нет другого пути.

---

## 2. Стек инструментов

| Слой | Инструмент | Назначение |
|---|---|---|
| Source format | `library/lectures/lec-NN/deck.yaml` + `slides/*.md` | структурированный source |
| Render engine | **`powerpoint` MCP** (`office-powerpoint-mcp-server==2.0.7`, GongRzhe) | сборка PPTX из примитивов |
| Snapshot | LibreOffice headless + `pdf2image` | PPTX → PDF → PNG для visual loop |
| Vision | Claude Sonnet/Opus встроенно | агент читает PNG визуально |
| Diagrams (alt) | `drawio` MCP | для сложных схем, когда shape primitives не хватает |

### Установка

```bash
# 1. PowerPoint MCP — через uvx, уже зарегистрирован в .mcp.json
#    (pip install не нужен, uvx запускает в изолированном venv)
uvx --from office-powerpoint-mcp-server==2.0.7 ppt_mcp_server --help

# 2. LibreOffice headless для snapshot — нужен sudo, ставится один раз
sudo apt install -y libreoffice-impress libreoffice-core poppler-utils

# 3. (опционально) pdf2image / Pillow для конвертации PDF → PNG
pip install --user --break-system-packages pdf2image Pillow
```

После установки — verify:
```bash
claude mcp list                                              # powerpoint должен отвечать
libreoffice --headless --convert-to pdf /tmp/test.pptx       # smoke test conversion
```

---

## 3. PowerPoint MCP — критичные tools (37 всего)

Полный список — `tools/list` через MCP. Здесь — только то, что регулярно используется в pipeline.

| Категория | Tools |
|---|---|
| Создание | `create_presentation`, `create_presentation_from_template`, `open_presentation`, `save_presentation` |
| Слайды | `add_slide`, `apply_slide_template`, `manage_slide_masters`, `manage_slide_transitions`, `populate_placeholder` |
| Текст | `manage_text`, `add_bullet_points`, `optimize_slide_text`, `manage_fonts` |
| Шейпы (примитивы) | `add_shape`, `add_connector` |
| Изображения | `manage_image`, `apply_picture_effects`, `manage_hyperlinks` |
| Таблицы и графики | `add_table`, `format_table_cell`, `add_chart`, `update_chart_data` |
| Inspection | `get_presentation_info`, `get_slide_info`, `extract_slide_text`, `extract_presentation_text`, `list_presentations` |
| Шаблоны | `list_slide_templates`, `apply_professional_design`, `auto_generate_presentation`, `get_template_info` |

**Limitation:** **нет** нативного `list_shapes` / `get_shape_properties`. Для visual-loop правок агент держит локальный «mental model» расположения шейпов (либо ведёт их в `deck.yaml` со стабильными ID).

---

## 4. Slide-types library (на старте — 4 типа, расширяется по мере появления)

| Type | Когда | Layout-pattern |
|---|---|---|
| `cover` | Титул лекции | большой заголовок + центральный вопрос лекции крупно + meta-блок |
| `assertion_visual` | Содержательный слайд (основной тип) | тезис сверху + большой визуал в центре (картинка/схема/число) |
| `poll_reveal` | Опрос/reveal (2 шага) | step1 — вопросы; step2 — данные vs оценка |
| `live_demo` | Внешнее демо/код | минимальный слайд + backup-ссылка в speaker notes |

После пилота #55 добавятся: `process`, `comparison`, `quadrant`, `data_block`, `diagram_slide`, `summary`. Список открытый — добавляем по реальной нужде, не upfront.

### Правила для `assertion_visual`
- **Заголовок слайда = assertion** (полное предложение, например: «Главный вопрос курса — не "можно ли AI?", а "НУЖНО ли и ГДЕ?"»). Не «Введение». Не «Цели лекции».
- **Визуал в центре** = доказательство тезиса (схема / число / изображение). Не декоративная картинка.
- **Не больше 4 буллетов**, если без визуала — заменить на текстовый блок крупным шрифтом.
- **Speaker notes** — что говорит преподаватель (1-3 абзаца).

---

## 5. Visual-loop workflow (по одному слайду)

```
1. Read deck.yaml + slides/sNN.md            ← source
2. Render slide via PowerPoint MCP            ← create_presentation / add_slide / add_shape...
3. Save .pptx in library/lectures/lec-NN/rendered/
4. Snapshot: libreoffice --headless --convert-to pdf, then pdf2image → PNG
5. Read PNG visually (Claude vision)          ← agent describes what it sees
6. Compare with assertion + intent
7. If issues → patch via MCP (move_shape / update_text_style / etc.)
8. Re-snapshot, re-look
9. Loop steps 5-8 until acceptable, max 5-7 iterations
10. Log iterations in rendered/iteration-log.md
```

---

## 6. `deck.yaml` schema (минимальная, расширяется по необходимости)

```yaml
deck:
  lecture_number: 1
  title: "Введение — AI вокруг нас"
  audience: "бакалавры ИУ6 МГТУ Баумана"
  duration_min: 75
  central_question: "Как инженеру ИУ6 попасть в оставшиеся 10% AI-пилотов?"
  learning_outcomes: [LO1, LO4, LO6, LO7]
  language: ru

slides:
  - id: s01
    file: slides/s01-ice-breaker-cv.md
    type: live_demo
    duration_min: 3
    assertion: "Narrow AI работает на ноутбуке без облака — рабочая инженерная лошадка"
    learning_goal: "Эмоциональный hook + снять страх 'AI = магия'"
    visual:
      pattern: external_demo
      backup: assets/code/ice-breaker-cv/backup/screenshot.png
    interaction: live_demo
    references: [yolov8-ultralytics-2023]
```

Поля минимально нужные: `id`, `file`, `type`, `assertion`, `learning_goal`. Остальные — по необходимости.

---

## 7. Папочная раскладка одной лекции

```
library/lectures/lec-01/
  deck.yaml              ← структура deck'а
  slides/
    s01-*.md             ← один слайд = один файл (diff-friendly), markdown с frontmatter
    s02-*.md
    ...
  assets/
    images/, diagrams/, code/
  rendered/
    lec-01.pptx          ← последний рендер
    snapshots/
      s01.png, s02.png, ...
    iteration-log.md     ← лог визуальных циклов (для каждого слайда)
  qa-reports/
    YYYY-MM-DD/
      reader-text-only.md
      presentation-critic.md
      student-simulator.md
      reader-rendered.md
      summary.md
```

---

## 8. Связанные агенты (`.claude/agents/`)

| Агент | Перспектива | Видит |
|---|---|---|
| `deck-editor` | Сборщик/редактор | всё (yaml + md + PNG) |
| `presentation-critic` | Методист | yaml + md + PNG |
| `student-simulator` | Студент ИУ6 в зале | только PNG + видимые speaker notes |
| `reader-simulator` | Тот же студент через 2 недели; **2 режима**: `text-only` и `rendered` | text-only: только md; rendered: PNG + notes |

Каждый агент в своём `.md`-файле — первая строка `**REQUIRED READING:** этот файл`.

---

## 9. Что НЕ делаем (anti-patterns)

- **Не используем Title+Body универсально.** Каждый слайд — конкретный тип из библиотеки.
- **Не делаем декоративные картинки.** Визуал = доказательство.
- **Не пишем 8+ буллетов.** Лимит 4.
- **Не делаем заголовок «Тема X».** Заголовок = тезис.
- **Не правим Drive напрямую.** Source — репо, Drive — только artifact (когда подключим upload).
- **Не пропускаем visual loop.** Минимум 1 итерация для каждого слайда.

---

## 10. Roadmap инструмента (sub-issues EPIC #52)

- **#53 (этот setup)** — установка MCP + агенты + структура.
- **#54** — 1-слайдный спайк s05b, валидация visual-loop.
- **#55** — 6-слайдный пилот Лекции 1 (s01-s05b), 3 QA агента в действии.
- **#56** — стабилизация: переписать `/build-deck` skill, формализовать `deck.yaml` schema, обновить `decisions.md`.
- **#57** — factory: остальные слайды Л1, потом Л2-Л17.

---

## 11. Открытые вопросы / TODO для следующих sub-issues

- **list_shapes / get_shape_properties** — отсутствуют в GongRzhe MCP. При первой реальной потребности (вероятно в #55) — форкнуть `tellina-study/Office-PowerPoint-MCP-Server` и добавить как 2 простых обёртки над python-pptx.
- **Reference template** — выбираем после спайка #54.
- **Drive upload + feedback pull** — отложено до момента, когда понадобится внешний рецензент.
- **/build-deck skill update** — текущий SKILL.md ориентирован на Google Slides. Переписывается в #56.
