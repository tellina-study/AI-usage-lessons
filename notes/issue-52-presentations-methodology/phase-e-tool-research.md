# Phase E — Расширенный research инструментов (PowerPoint MCP + Figma + визуальная оценка)

**Issue:** #52
**Дата:** 2026-05-12
**Контекст:** дополнение к `phase-e-tool-choice.md`. Пользователь потребовал добавить в сравнение PowerPoint MCP и Figma, а также оценить **реальные публичные decks** на каждом инструменте — оставить только те, что не выглядят гиковскими.

---

## 1. PowerPoint MCP servers — что есть в природе

### Найденные активные сервера (все используют python-pptx под капотом)

| Сервер | Tools | Shape primitives | Master/template | PNG snapshot | Move/resize/font | Last update | Статус |
|---|---|---|---|---|---|---|---|
| **GongRzhe/Office-PowerPoint-MCP-Server** | 32–34 (11 модулей) | 20+ auto-shapes (rect, oval, flowchart), connector lines/arrows | full template + slide-master mgmt + 25 встроенных шаблонов | НЕТ (отдельным шагом через LibreOffice) | да (left/top/width/height + font props) | 2025-12-31 (v2.0.7) | архивирован 2026-03-03, read-only |
| **gtonic/pptx-mcp** | средний набор | базовые + Mermaid/PlantUML рендерятся как **editable PowerPoint vector shapes** (не картинки) | reference template (extract style) | НЕТ | да | архивирован 2026-01-23 | read-only |
| **charleslukowski/ppt_mcp** | comprehensive | базовые shapes + charts + tables | да | НЕТ | да | актив | актив |
| **ltc6539/mcp-ppt** | базовый | text/image/table/section | базовый | НЕТ | да | актив | актив |
| **socamalo / Ichigo3766 / samos123 / jenstangen1** | базовые форки | базовые | вариативно | НЕТ | да | актив | мелкие |

### Ключевые находки
- **Минимум 8 живых проектов** на GitHub. Это уже стандарт «экосистемы», не экспериментальный самописный сервер.
- **Все используют python-pptx** — это значит ровно один реальный capability slice (что умеет python-pptx — то умеет MCP). Различие — в количестве high-level tools (templates, layout helpers, цветовые схемы).
- **Никто из них не делает PNG-snapshot напрямую** — это важное ограничение для visual-loop. Снимок надо собирать отдельным шагом: `libreoffice --headless --convert-to pdf` → `pdf2image` → PNG. Есть готовые wrapper-пакеты (`pptxtoimages`, `pptx2img`, `pptx-renderer` на PyPI).
- **Shape primitives работают**: rectangle, ellipse, line, arrow, connector — всё через python-pptx auto-shapes. У GongRzhe это явно богаче (20+ типов + connectors).
- **Mermaid/PlantUML как editable vectors** — реально умеет только `gtonic/pptx-mcp`. У остальных Mermaid либо вставляется как PNG-картинка, либо отсутствует.
- **Шаблоны**: GongRzhe ведёт впереди — round-trip с reference template + manage_slide_masters.

### Рекомендация по PowerPoint MCP
Главный «состоявшийся» вариант — **`GongRzhe/Office-PowerPoint-MCP-Server`** (32 tools, master mgmt, professional shapes, connectors), но **он архивирован и больше не развивается**. Это не блокер — функциональность зрелая, риск снижается тем, что под капотом стандартный python-pptx; в крайнем случае форкнем.

Для Mermaid-as-editable-shapes — **`gtonic/pptx-mcp`** уникален, можно подключить вторым сервером для diagram-задач.

PNG-снимки придётся делать **отдельным шагом** через LibreOffice headless — не блокер, но требует +1 install dependency на машине.

---

## 2. Figma — write capabilities в 2026

### Официальный Figma MCP (Dev Mode + Remote)
- В беккете 2026 у Figma MCP появился **`use_figma` tool — write-to-canvas**: умеет создавать/редактировать **frames, components, variants, variables, auto layout**, в FigJam — стикеры, секции, connectors, shapes, tables.
- Поддерживаемые клиенты: Augment, **Claude Code**, Claude Desktop, Codex, Copilot CLI, Cursor, Factory, Firebender, VS Code, Warp.
- Требует **paid Full seat** ($15+/мес/seat). Беттa бесплатна сейчас, но «eventually a usage-based paid feature».
- В документации **прямо не упомянута поддержка Figma Slides** через write-to-canvas. Подтверждённо — Design files и FigJam.

### Figma Slides — Plugin API (отдельный путь, не MCP)
- Plugin API теперь поддерживает Figma Slides: 4 новых node types (`SLIDE`, `SLIDE_ROW`, `SLIDE_GRID`, `INTERACTIVE_SLIDE_ELEMENT`), методы `getSlideGrid()`/`setSlideGrid()`, `getSlideTransition()`/`setSlideTransition()`.
- Плагин запускается **внутри Figma desktop/web** — это не headless-агент, его нельзя вызвать из CLI subagent'а как MCP-tool.
- Нативный экспорт **в PPTX и PDF** работает, но с известными потерями: шрифты съезжают на дефолты, интерактив становится статикой, градиенты упрощаются. **Bulk export не поддерживается** (только по слайду).
- Сторонние community-плагины (FPPT, Framedeck, .PPTX export) дают лучше editable PPTX, но это **ручной запуск из UI** — для агента не годится.

### Реалистичный путь для нашей задачи?
**Нет.** Figma MCP write-to-canvas:
1. Требует paid seat (доп. $15/мес минимум) — для соло-мейнтейнера и pet-проекта это пеня без явной выгоды.
2. **Не поддерживает Figma Slides** программно (только Design + FigJam).
3. Headless-цикл «агент → создал deck → экспортировал PPTX → posted в Drive» нативно не закрывается — экспорт всё равно ручной из UI.
4. Реальный сценарий — дизайнер-человек правит в Figma и отдаёт PPTX. Это **не наш случай**, агент-сборщик не работает в Figma editor.

**Figma — не подходит для агентного pipeline.** Подходит, если в будущем будет дизайнер-человек, который делает мастер-deck в Figma Slides → PPTX-экспорт → агент использует как reference template для PowerPoint MCP. Но это другой проект.

---

## 3. Реальные публичные примеры — визуальная оценка

Оценка по шкале «вынес бы я это студентам МГТУ как пример того, как должна выглядеть наша презентация».

### Slidev
- Reverse Engineering Denuvo — Navaja Negra 2025 (`momo5502.com/slides/denuvo`)
- Kubernetes/LLM scaling — KubeCon 2025 China (`baizeai.github.io/talks/2025-06-11-kubecon-hk/`)
- nCine 14-летняя ретроспектива (`encelo.github.io/nCine_14Years_Presentation/`)
- HD Moore — Hacker Numerology — LASCON 2024 (`hdm.io/decks/2024-LASCON-Numerology/`)

**Оценка:** очень dev-focused визуал. Тёмные темы, моноширинный код, минималистичный дизайн «как у Anthony Fu». Для **dev-конференции** — отлично. Для **первокурсников ИУ6, которым нужно влюбить в тему** — слишком «гиково», у студентов будет ощущение «опять что-то сложное от программистов». **На широкую публику — нет.**

### Marp
- Theme galleries: **marp-community-themes** (rnd195), **marpstyle** (cunhapaulo), **awesome-marp**.
- Лучшие темы: `Beam`/`Neobeam` (LaTeX-Beamer-стиль, академичный), `marpstyle` (минимализм с акцентом на читаемость), `Rosé Pine`/`Nord` (тёплые, аккуратные).
- Реальные публичные decks: разрозненны, в основном технические (EclipseCon talks, CodeBytes blog examples, dev.to walkthroughs).

**Оценка:** база Marp по умолчанию **скучная** (default/gaia/uncover), но `marpstyle` и `Beam`-производные **уже не выглядят гиковски** — это «академический минимализм», нормально читается профессорами/студентами. **На публику — да, при условии кастомной темы**, не дефолтной. Главный плюс: единый markdown → editable PPTX, что закрывает D1 (внешние комментарии в Drive с правкой текста).

### Google Slides (через workspace-mcp)
- Уже отвергнуто пользователем — первая итерация дала «уродливо».
- Объективная причина: TITLE_AND_BODY layout даёт template-look «корпоративный 2010». Можно лучше через custom positioning + reference template, но требует ручной theme-инвестиции, которая не оправдывается, когда есть PPTX-route.

**Оценка:** годится только если хост-человек правит руками. Для агентной сборки качество предсказуемо посредственное. **Не финалист.**

### PowerPoint (через MCP + reference template)
- Apple keynotes (исторически Keynote, но как эталон bar) — недостижимо без человека-дизайнера.
- McKinsey published decks (`mckinsey.com/featured-insights`), MS Build event decks — реальный «корпоративный» уровень, который **достижим в PPTX через reference template + аккуратное наполнение**.
- ORNL MEASUR через PptxGenJS — функциональные технические репорты, но визуально «как Excel-отчёт».

**Оценка:** PPTX **как формат** позволяет какой угодно визуал — вопрос не в формате, а в **reference template**. Если взять качественный community-шаблон (SlidesCarnival, Slidesmania) и через PowerPoint MCP заполнять его контентом — **выглядит на публику нормально**. **Финалист.**

### Figma Slides
- Templates от Mockuuups Studio (`mockuuups.studio/blog/post/best-figma-slides/`)
- Figma Community presentations (`figma.com/community/presentations` — 3400+ файлов)
- Award-winning Figma decks упоминаются с акцентом «whitespace, storytelling, interactivity».

**Оценка:** **визуально лучшие из всех** — Figma Slides делают красиво, профессионально, modern. Но как сказано в §2 — **агентный путь не закрывается** без человека-дизайнера в Figma editor. **Не финалист для нашей задачи**, хотя визуально образцовый.

### PptxGenJS
- ORNL MEASUR — реальный пример (treasure hunt reports)
- Demo gallery (`gitbrent.github.io/PptxGenJS/demos/`) — 75+ demo slides показывают возможности, но визуал «инженерный отчёт».

**Оценка:** мощный API, **полностью editable PPTX**, но писать каждый слайд кодом — это уровень программирования. Без markdown-source ломает наш repo-first workflow (уже отвергнуто в Phase B). **Не финалист.**

---

## 4. Финал — 3 кандидата и integration paths

Жёсткий отбор по критериям: профессиональный визуал на широкую публику + MCP/CLI совместимость + shape primitives + visual snapshot.

### Финалист 1 — **Marp + кастомная тема (marpstyle/Beam-derived)**
- **Сильные:** markdown source = repo-first, editable PPTX закрывает D1, multi-format (HTML/PDF/PPTX/PNG) одной командой, лёгкий toolchain (один npm), кастомная тема снимает «гиковость».
- **Слабые:** layout flexibility ниже среднего; shape-диаграммы — только через embedded mermaid → SVG (не editable shapes); кастомная тема требует CSS-инвестиции (~1-2 дня).
- **Integration path:**
  - CLI: `npm i -g @marp-team/marp-cli`
  - Тема: `tools/presentation-build/themes/iu6.css` (форк marpstyle, под наш бренд)
  - Snapshot: `marp slide.md --images png -o out/` — **встроенный PNG-export**, не нужен LibreOffice
  - MCP: не требуется, agent вызывает marp CLI напрямую
  - Workflow: `lectures/lec-NN/slides.md` → marp → `slides.pptx` + `snapshots/*.png` → workspace-mcp uploads в Drive
  - Diagrams: drawio MCP → SVG → embed как `<img>` в markdown

### Финалист 2 — **PowerPoint MCP (GongRzhe) + reference template**
- **Сильные:** **полноценный editable PPTX** с rich shapes (20+ types) и connectors; работа с reference template (SlidesCarnival/Slidesmania-уровень визуала); position/font edits как у дизайнера; визуальное качество **выше Marp** при правильном template.
- **Слабые:** **source = не markdown, а tool-calls агента** — менее git-friendly (нужно версионировать промежуточный YAML/JSON с layout-инструкциями); GongRzhe архивирован (но python-pptx стабилен); PNG-snapshot требует отдельного шага через LibreOffice headless.
- **Integration path:**
  - MCP: `pip install office-powerpoint-mcp-server`, добавить в `.mcp.json`
  - Template: `tools/presentation-build/templates/iu6-master.pptx` (взять качественный community-шаблон, ребрендировать раз)
  - Snapshot helper: `pip install pptxtoimages` (`libreoffice --headless` под капотом) — отдельный CLI step после генерации
  - Source-of-truth: `lectures/lec-NN/slides.yaml` (структурированное описание слайдов) → агент читает yaml → вызывает MCP-tools → `slides.pptx`
  - Diagrams: drawio MCP → SVG → MCP вставляет как picture, **или** native shapes через add_shape + connectors
  - Workflow: yaml → MCP-сборка → PPTX → LibreOffice→PNG → snapshot review → итерация → upload

### Финалист 3 — **Slidev + кастомная тема (только для web-публикации курса)**
- **Сильные:** богатые layouts из коробки (`cover`, `two-cols`, `image-right`, `iframe`, `live-coding`), встроенный mermaid, лучший интерактив для web-формата, активное community.
- **Слабые:** **PPTX = картинки** (текст не editable — ломает D1), требует Vue/CSS skills для кастомных layout'ов, тяжёлый toolchain (npm + playwright-chromium).
- **Когда выбирать:** если приоритет — **публичный web-курс с интерактивом** (студенты смотрят онлайн), а PPTX в Drive нужен только как «снимок для архива/комментариев на изображениях».
- **Integration path:**
  - CLI: `npm i -g @slidev/cli playwright-chromium`
  - Тема: `tools/presentation-build/slidev-theme-iu6/` (npm package, форк theme-academic)
  - Snapshot: `slidev export --format png` — встроенный PNG-export
  - MCP: не требуется
  - Workflow: `lectures/lec-NN/slides.md` (slidev frontmatter) → `slidev build` → `dist/` (HTML) + `slides.pptx` (картинки) + `snapshots/*.png`
  - Diagrams: встроенные mermaid + drawio через `<iframe>`

---

## Итоговая рекомендация

**Делать спайк только на двух финалистах**: **Marp** vs **PowerPoint MCP (GongRzhe + reference template)**. Slidev оставить как fallback-вариант №3 для будущей web-версии курса.

**Решающий вопрос для выбора между Marp и PowerPoint MCP:**

> Что важнее — **markdown как git-friendly source** (Marp) или **визуальное качество результата + editable shape-диаграммы** (PowerPoint MCP с reference template)?

- Если приоритет — простота и git-flow → **Marp + кастомная тема marpstyle**.
- Если приоритет — выглядеть как McKinsey deck для широкой аудитории и реально строить shape-схемы (process, comparison, quadrant) из примитивов → **PowerPoint MCP + community-template**.

Спайк (F.0): тот же слайд s05 (instructor-card + центральный вопрос) собрать обоими путями, сравнить визуально на snapshot'ах, оценить editability в Drive.

**Figma и Google Slides вычеркнуты окончательно** — Figma не закрывает агентный pipeline, Google Slides не достигает нужного уровня визуала через API.

---

## Источники

PowerPoint MCP:
- https://github.com/GongRzhe/Office-PowerPoint-MCP-Server
- https://github.com/gtonic/pptx-mcp
- https://github.com/charleslukowski/ppt_mcp
- https://github.com/ltc6539/mcp-ppt
- https://pypi.org/project/office-powerpoint-mcp-server/
- https://pypi.org/project/pptxtoimages/

Figma:
- https://developers.figma.com/docs/figma-mcp-server/
- https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/
- https://developers.figma.com/docs/plugins/working-in-slides/
- https://help.figma.com/hc/en-us/articles/24848334599447-Export-from-Figma-Slides
- https://www.figma.com/community/presentations

Slidev:
- https://sli.dev/resources/showcases
- https://github.com/slidevjs/slidev

Marp:
- https://github.com/marp-team/awesome-marp
- https://rnd195.github.io/marp-community-themes/
- https://github.com/cunhapaulo/marpstyle

PptxGenJS:
- https://gitbrent.github.io/PptxGenJS/demos/
- https://github.com/gitbrent/PptxGenJS
