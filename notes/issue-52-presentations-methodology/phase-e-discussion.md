# Phase E — Обсуждение с пользователем (живой лог)

**Issue:** #52
**Дата старта:** 2026-05-12
**Статус:** РАУНД 1 ОТВЕТОВ ПОЛУЧЕН → нужно выбрать инструмент → раунд 2

---

## Решения раунда 1

| # | Тема | Решение пользователя |
|---|---|---|
| **0** | Render-target | **Google Slides — выбрасываем.** В индустрии массово другой инструмент; первая версия получилась плохо. Нужен спайк по выбору. |
| **D1** | Repo-first | **OK с оговоркой:** внешние рецензенты могут оставлять заметки в файле на Drive — мы должны забрать, отработать, обновить файл. Снаружи это «правка Drive». |
| **D2** | Объём пилота | **Нужно пояснить «до/после пилота»** (см. ниже). |
| **D3** | Старая Google Slides Л1 | **Удалить.** |
| **D4** | Master template | **Делаем после пилота, и не факт что в Google.** |
| **D5** | 3 агента | **OK.** Дополнительно: reader-режим **«читает голый текст»** до создания слайдов — методический контроль текста-методички. |
| **D6** | Идемпотентность | **Обсудим после выбора инструмента.** |
| **D7** | Slide-types | **Обязательно: схема и иллюстрации.** Остальное OK. |
| **D8** | Источник narrative | **v4 берём.** Можно предлагать улучшения **методики/смысла/нарратива**, не только инструментов. |
| **D9** | Воспроизводимость | **Отдельный setup-файл с инструкциями**, ссылаться где нужно. |
| **D10** | OAuth | **Решим после инструмента.** |

---

## Что меняется в proposal'е по итогам раунда 1

### Изменения архитектуры
1. Render-target ≠ Google Slides. Source — markdown в репо. Publish — файл в формате X (выбираем) загружается в Drive.
2. Drive остаётся feedback-каналом: внешние рецензенты комментируют файл, мы забираем комментарии skill'ом.
3. Master template создаётся **после пилота**, в формате выбранного инструмента.
4. Старый deck Л1 — **удалить из Drive** (не archive).

### Изменения агентов
5. `reader-simulator` получает **2 режима**:
   - `text-only`: читает только `slides/*.md` без рендера → методический контроль текста-методички. Запускается **до** создания слайдов.
   - `rendered`: читает PNG слайдов + speaker notes → проверка финального deck'а через 2 недели после лекции.

### Изменения slide-types для пилота
6. Добавляем `diagram_slide` (для схем drawio/mermaid → image) и `data_block` (для инфографики цифр) в библиотеку. В пилотных 5 слайдах используются `cover`, `live_demo`, `poll_reveal`, `assertion_visual`, `data_block`.

### Изменения процесса
7. Setup-инструкции — отдельный файл `library/lectures/_setup.md` (или `tools/presentation-build/README.md`) с воспроизводимостью: чем рендерим, как ставится, как запустить, ожидаемый результат. На него ссылаются skills/agents.
8. Методическая критика narrative v4 — часть F.3 (orchestrator review до рендера).

---

## Что отвечаю на D2 — «до пилота / в пилоте / после пилота»

### Раунд «ДО пилота» (F.0–F.1) — что делаем перед F.4 рендером
- **F.0 — выбор инструмента** (СЕЙЧАС, нужен ответ пользователя). Спайк на 1 пробном слайде в 1–2 кандидатах. Без него остальное не имеет смысла.
- **F.1.a** — установить выбранный инструмент локально, задокументировать в `library/lectures/_setup.md`.
- **F.1.b** — создать 3 агента (`presentation-critic`, `student-simulator`, `reader-simulator`) как `.claude/agents/*.md`. Reader получает 2 режима.
- **F.1.c** — проверить permissions для новых агентов.
- **F.1.d** — создать структуру `library/lectures/lec-01/` (папки + пустой deck.yaml).
- **F.1.e** — спайк фидбэк-цикла: загрузить тестовый файл в Drive, оставить комментарий, проверить как `workspace-mcp` его отдаёт.

### Раунд «В пилоте» (F.2–F.7) — собственно 5 слайдов
- **F.2** — subagent делает черновик `deck.yaml` + `slides/s01..s05.md` из плана v4 первых 5 слайдов.
- **F.3** — orchestrator + `reader-text-only` агент проверяют **методический текст** ДО рендера. Записываем замечания. Правим.
- **F.4** — subagent рендерит → файл (формата выбранного инструмента) → загружает в Drive. Удаляет старый Slides из Drive и из `decks.yaml`.
- **F.5** — параллельно: `presentation-critic` (всё видит) + `student-simulator` (PNG+notes) + `reader-rendered` (PNG+notes).
- **F.6** — сводный отчёт. Решаем 3–5 главных правок.
- **F.7** — re-render. Глазами сравниваем.

### Раунд «ПОСЛЕ пилота» (F-system) — после F.8 approval
- Скилы (`/draft-deck`, `/qa-deck`, `/pull-deck-feedback`) формализуем как полноценные.
- `deck.yaml` schema → JSON-schema.
- Master template (в формате выбранного инструмента) — финализируем.
- Расширение slide-types library до 10+ типов.
- Перенос на остальные 16 лекций (постепенно).
- `notes/decisions.md` пополняется.
- `library/lectures/_setup.md` — финальная версия.

→ **В пилоте — только то, что нужно для 5 слайдов.** В F-system — стабилизация и расширение.

---

## Открытые вопросы раунда 2

См. отдельный файл `phase-e-tool-choice.md` — детальный разбор кандидатов на render-target и моё предложение.

---

## Раунд 3 — input пользователя про визуальный цикл

**Дата:** 2026-05-12
**Цитата:** «в генерации ты можешь и должен участвовать так, как это делал бы реальный человек (или полностью создавать слайды через mcp/skills/api или править и улучшать то что сделано инструментально), потом смотреть ВИЗУАЛЬНО что получилось и при необходимости улучшать»

**Главное:** в моём proposal'е был упущен **first-class компонент** — итеративный визуальный цикл сборки. Это меняет архитектуру и взвешивание инструментов.

**Конкретные апдейты:**
- Visual loop становится обязательной частью сборки (не отдельным QA-шагом).
- Google Slides **возвращается в кандидаты** (он отлично совместим с visual loop через `get_page_thumbnail` и `batch_update_presentation`).
- `presentation-critic` теперь смотрит PNG-снимки (мультимодальное чтение).
- `render_log` в `last-render.json` для воспроизводимости «человеческих» правок.
- Inline sanity-check в сборщике (переполнение/отрезанный текст), без отдельного агента.

**Спайк меняем:** вместо «Marp vs Slidev на s05» — **«Google Slides + визуальный цикл vs Marp + python-pptx fix + визуальный цикл»** на одном слайде s05. Параллельно, по 3-5 итераций каждый, с логом.

См. отдельный файл `phase-e-visual-loop.md` — полный разбор и новая рекомендация.

→ Жду твоего OK на новый формат спайка + ответы на 4 вопроса в §9 `phase-e-visual-loop.md`.

---

## Раунд 4 — input пользователя про Figma, PowerPoint MCP, shape-диаграммы и реальные примеры

**Дата:** 2026-05-12
**Цитаты:**
- «и где фигма и powerpoint mcp?! Они тоже должны быть среди кандидатов»
- «так же посмотри сам примеры реальных презентаций на предлагаемых инструментах и оставь только те, которые ты сам выносил бы на широкую публику»
- «диаграммы можно размещать тоже фигурами, а не только mermaid»

**Делегировано research-агенту.** Полный отчёт — `phase-e-tool-research.md`.

**Краткие итоги:**
- **PowerPoint MCP** — экосистема из 8+ серверов на python-pptx; лидер `GongRzhe/Office-PowerPoint-MCP-Server` (32 tools, 20+ shapes, connectors, slide masters, 25 templates) но архивирован 2026-03 (стек стабилен — низкий риск). Нативного PNG-snapshot нет → через LibreOffice headless.
- **Figma — отвергаем.** Figma MCP write поддерживает Design+FigJam, но **не Figma Slides** программно. Slides Plugin API работает только в Figma editor (не headless). Paid seat $15+/мес. Агентный pipeline не закрывается.
- **Slidev** — реальные публичные decks dev-focused (тёмные темы, моноширь, «гиково»). Не для широкой публики студентов ИУ6. Оставляем как fallback для будущей web-версии.
- **Marp с дефолтной темой** — скучно. С темой типа `marpstyle`/`Beam` — академический минимализм, **годится** для широкой аудитории.
- **Google Slides** — подтверждается отказ.
- **PptxGenJS** — отвергнут (не markdown-source, требует TS-кода).

### Финалисты: 2 кандидата
1. **Marp + кастомная тема (marpstyle/Beam-derived)** — markdown-source, editable PPTX, multi-format одной командой. Слабость: shape-диаграммы только через embedded mermaid SVG, не editable shapes.
2. **PowerPoint MCP (GongRzhe + reference template)** — лучший визуал, **rich editable shapes + connectors из примитивов** (закрывает требование пользователя про shape-диаграммы), возможность взять качественный community-шаблон. Слабость: source — структурированный YAML с tool-вызовами, не markdown.

### Решающая развилка
**Markdown-source как git-friendly первоисточник (Marp)** vs **визуальное качество + native shape-диаграммы (PowerPoint MCP)**.

Третье требование пользователя (диаграммы как фигуры) — **сильный аргумент в пользу PowerPoint MCP**: GongRzhe умеет 20+ shape primitives + connectors, агент может строить process/comparison/quadrant из примитивов. В Marp это только через pre-rendered SVG/PNG.

---

## Раунд 5 — input пользователя про архивацию GongRzhe

**Дата:** 2026-05-12
**Цитата:** «powerpoint ок, но почему берем архивный инструмент? поисследуй почему его архивировали, какие есть альтернативы. форкнуть можем, но может есть что-то объективно лучшее?»

**Делегировано research-агенту.** Полный отчёт — `phase-e-pptx-mcp-deep.md`.

### Краткие итоги

**1. Почему GongRzhe архивирован.**
Не deprecation в пользу лучшего решения, а **массовая архивация всего портфеля автора**: 20 из 22 публичных MCP-репо у GongRzhe заархивированы в марте 2026 (включая Word 1949★, Gmail 1110★, Visio, Quickchart, Human-In-the-Loop). Никакого explicit notice, скорее всего — burnout/смена занятости. **Код стабилен**, последняя версия v2.0.7 от 2025-12-31, под капотом mainline `python-pptx`.

**2. Что есть объективно лучше — ничего на нашем стеке (Linux + python-pptx + богатые шейпы).**

| Альтернатива | Статус | Вердикт |
|---|---|---|
| `charleslukowski/ppt_mcp` | 5★, last commit 2025-07-01 (10 мес тишины) | Фактически тоже мёртв; backup, не primary |
| `ltc6539/mcp-ppt` | 66★, активный | **14 tools, нет shape primitives** — дисквалифицирован |
| `supercurses/powerpoint`, `Ichigo3766` форк | средне | без шейпов |
| `Softeria/ms-365-mcp` | 701★, активный | **PowerPoint функций нет** (Graph API не покрывает Slides) |
| Microsoft + Anthropic M365 MCP (2026) | официальный | Client-side connector в Office Copilot, **не для агентной сборки PPTX** |
| Arcade.dev cloud MCP | коммерческий | Без shape primitives |
| Aspose.Slides | $1199/год | MCP-обёртки **нет** |
| `ykuwai/ppt-mcp` (154 tools), `trsdn/mcp-server-ppt` (204 ops) | мощные | **Windows + COM PowerPoint** — несовместимо с нашим Linux/WSL |

**3. По 6 критическим операциям:**
- GongRzhe — 5/6 полностью, 1/6 частично.
- charleslukowski — 2/6 полностью, 3/6 частично, 1/6 нет.
- ltc6539 — 1/6 полностью, 5/6 нет.

### Финал

**Primary: GongRzhe, через форк `tellina-study/Office-PowerPoint-MCP-Server`.**
- Архивация — управляемый риск (стабильный python-pptx под капотом, 15+ публичных форков как прецеденты).
- На PyPI пакет существует и устанавливается: `pip install office-powerpoint-mcp-server==2.0.7` — можно использовать без форка изначально, форкнуть только если потребуются доработки.
- Сразу добавить issue в наш форк: «add `list_shapes`/`get_shape_properties` для visual-loop» (~2-3 часа на python-pptx-обёртку).

**Backup: charleslukowski/ppt_mcp** — если форк GongRzhe сломается.

---

## Финальные решения (раунд 6 — закрытие Phase E)

**Дата:** 2026-05-12

| # | Тема | Финал |
|---|---|---|
| Tool | PowerPoint MCP | **GongRzhe via PyPI** (`office-powerpoint-mcp-server==2.0.7`). Форк `tellina-study/...` — только при необходимости. Backup: `charleslukowski/ppt_mcp`. |
| Reference template | Подход | **Постепенно**: для 1-слайдного спайка — без template, чистый python-pptx; после спайка решаем (community-template SlidesCarnival/Slidesmania vs custom). Подробнее в Roadmap → Sub-issue 2. |
| Спайк | Marp vs PPTX | **Не делаем**. Прыгаем сразу к PowerPoint MCP — Marp отвергнут shape-диаграммами. Спайк превращается в «1 слайд → отладка → 5 слайдов → factory». |
| Methodical fixes s02-s05 | (D8 раунд 1) | **Берём в пилот**. Cover с центральным вопросом, poll с 2 вопросами, s05 разделить на s05a (instructor) + s05b (рамка). Получается 6 слайдов в пилоте, не 5. |
| Setup-документ | Местоположение | **`tools/presentation-build/README.md`** — основной файл. Discoverability: (a) ссылка в `CLAUDE.md` → секция «Working Conventions»; (b) каждый presentation-агент начинается с явной строки `**REQUIRED READING:**`. |
| OAuth/Drive | Pilot | **Всё локально**. Drive integration — отложить, добавим только когда понадобится feedback-loop от внешних рецензентов. |
| Roadmap | Подход | **Разбить #52 на 5 sub-issues**, чтобы не растягивать одну мега-задачу. См. файл `phase-e-roadmap.md`. |

---

## Подробнее по reference template — моя рекомендация

**Многошаговый подход вместо одного решения upfront:**

1. **Для 1-слайдного спайка (Sub-issue 2)** — **без template**. Чистый python-pptx defaults + типографика средствами MCP (font_name, font_size, font_color). Понимаем, как выглядит наш шейп-набор «голым».
2. **После спайка** — решаем на основе результата:
   - Если результат «голого» python-pptx уже визуально OK → продолжаем без template.
   - Если уродливо → выбираем 2-3 community-template'а (SlidesCarnival categories: «education», «academic»; Slidesmania: «lecture», «education»), визуально сравниваем, прикладываем к одному слайду.
3. **Для 5-слайдного пилота (Sub-issue 3)** — применяем выбранный template/подход.
4. **Для factory (Sub-issue 5)** — финализируем (custom template или ребрендинг community) только когда пилот стабилен.

**Зачем так:** потратить день на template до того, как мы знаем, какие layout'ы вообще работают в нашем сценарии — деньги на ветер. Сначала смотрим, что получается, потом инвестируем в визуальную полировку.

---

## Подробнее по setup-документу discoverability

Чтобы агенты/Claude **читали без поиска**, делаем три уровня явности:

1. **Главный файл** — `tools/presentation-build/README.md` (детальный).
2. **Ссылка в CLAUDE.md** — в секции «Working Conventions» добавляется блок:
   ```
   ### Presentation Pipeline
   See `tools/presentation-build/README.md` for: PowerPoint MCP setup,
   visual-loop workflow, slide-types library, render commands.
   Required reading for `deck-editor`, `presentation-critic`,
   `student-simulator`, `reader-simulator` agents.
   ```
3. **Явный pre-amble в каждом presentation-агенте** — первая строка после `# Agent name`:
   ```
   **REQUIRED READING:** Before any work, read `tools/presentation-build/README.md`
   for the full pipeline (MCP tools, snapshot workflow, slide-types).
   ```

Один canonical документ + два дублирующих указателя. Никаких поисков.
