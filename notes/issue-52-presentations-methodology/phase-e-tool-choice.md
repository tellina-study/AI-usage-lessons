# Phase E — Выбор render-инструмента (раунд 2)

**Issue:** #52
**Дата:** 2026-05-12
**Контекст:** Google Slides выбрасываем (D0). Source — markdown в репо. Нужен инструмент для render markdown → файл публикации, совместимый с repo-first архитектурой.

---

## Критерии выбора

1. **Source = markdown** (или близкий к нему текстовый формат) — чтобы был git-friendly.
2. **Render = индустриально стандартный формат** для отправки/просмотра. На практике это **PPTX** (открывается везде), **PDF** (универсально, без интерактива), **HTML** (интерактив, но web-only).
3. **Layout flexibility** — нам нужны: cover, assertion+visual, poll/reveal-сцены, live-demo (внешний), data-block, diagram, comparison.
4. **Иллюстрации и схемы** (D7) — встраивание PNG/SVG, поддержка mermaid/drawio.
5. **Минимальный toolchain** — соло-мейнтейнер; не хотим тащить тяжёлый JS-стек ради 17 лекций.
6. **Editable PPTX как опция** — для D1 (внешние правки в Drive). Если PPTX → картинки, комментарии всё равно работают, но текст не правится.
7. **Переносимость** — не привязка к одной OS / одному vendor'у.

---

## Кандидаты

### A. **Marp** (Marp CLI + Marpit framework)
- **Source:** markdown с frontmatter и directives (`<!-- _class: lead -->`).
- **Output:** **HTML, PDF, PPTX, PNG, JPEG** — всё через `marp-cli`.
- **Themes:** CSS. Можно писать свои. Уже есть готовые (default, gaia, uncover).
- **Mermaid:** через плагин `marp-mermaid-plugin` или встраиванием HTML.
- **Изображения:** прямой markdown image, поддержка `bg`, `bg right:30%` directive для фоновых/positional.
- **Layout flexibility:** базовая (cover, default), кастомные через CSS classes. Не очень гибкая, но достаточная для наших 6 типов.
- **PPTX editability:** **редактируемый текст** в основном (по моему опыту, Marp PPTX-export = настоящий PPTX с текстом). Это сильный плюс для D1.
- **Toolchain:** `npm i -g @marp-team/marp-cli` — всё. VS Code extension есть.
- **Минусы:** layout'ы менее богатые чем Slidev; кастомные слайды требуют CSS-навыков.

### B. **Slidev** (Vue-based, by Anthony Fu)
- **Source:** markdown + Vue components.
- **Output:** **web (HTML)**, PDF, PPTX, PNG.
- **Themes:** Vue + CSS. Богатая экосистема (theme-default, theme-academic, theme-seriph итд).
- **Mermaid:** **встроенный** (` ```mermaid ... ` ).
- **Layouts:** богатый набор: cover/center/two-cols/quote/section/image-right/iframe/live-coding. Можно делать свои.
- **PPTX export:** через Playwright рендерит каждый слайд как **картинку** → собирает в PPTX. **Текст не редактируется в PPTX.** Это минус для D1.
- **Интерактив:** code-blocks с подсветкой, click animations, embeddable Vue components, monaco editor — всё это в web-режиме.
- **Toolchain:** `npm i -g @slidev/cli` + `npm i -g playwright-chromium` (для export).
- **Минусы:** web-first, PPTX = картинки.

### C. **PptxGenJS** (программная сборка)
- **Source:** TypeScript/JavaScript код.
- **Output:** PPTX напрямую.
- **Layout:** полный контроль через код, но писать руками каждый слайд тяжело.
- **PPTX editability:** **полностью редактируемый** PPTX.
- **Минусы:** не markdown-source, требует писать TS-код для каждого паттерна. Из рекомендации мы это **уже отвергли** в Phase B.

### D. **Pandoc → PPTX**
- **Source:** markdown.
- **Output:** PPTX, PDF (via LaTeX), HTML.
- **Reference template:** можно подключить `--reference-doc=template.pptx` для брендинга.
- **Layouts:** **очень ограничены** — Pandoc поддерживает только title slide, title+content, two-column. Не позволяет custom layouts.
- **PPTX editability:** редактируемый текст.
- **Toolchain:** уже есть в системе (если pandoc установлен — для wp-публикаций).
- **Минусы:** layout-ограничения убивают идею slide-types library. Не подходит для assertion-evidence и poll/reveal.

### E. **Quarto** (Posit, R/Python data-science)
- **Source:** `.qmd` (markdown с шапкой).
- **Output:** revealjs (HTML), PPTX, PDF.
- **Layouts:** revealjs богатый, PPTX следует Pandoc-ограничениям.
- **Минусы:** в основном для data-science workflow; для нашего курса — оверкилл, и PPTX слабый.

### F. **Reveal.js** (HTML/JS)
- **Source:** HTML или markdown.
- **Output:** **web only**, PDF через print.
- **PPTX:** через сторонние конвертеры — нестабильно.
- **Минусы:** web-only ломает D1 (нужен файл для Drive).

---

## Сводная таблица

| Critеrий | Marp | Slidev | PptxGenJS | Pandoc | Quarto | Reveal |
|---|---|---|---|---|---|---|
| Source = markdown | ✅ | ✅ | ❌ | ✅ | ✅ | ✅/часть |
| PPTX output | ✅ | ⚠️ картинки | ✅ | ✅ | ✅ | ❌ |
| PDF output | ✅ | ✅ | ✅(сторонне) | ✅ | ✅ | ✅(print) |
| HTML output | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Layout flexibility | ⚠️ через CSS | ✅ богато | ✅ полная | ❌ скудно | ⚠️ HTML богат, PPTX слаб | ✅ HTML |
| Mermaid встроенный | через plugin | ✅ | ❌ | через filter | ✅ | ✅ |
| Изображения легко | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| PPTX редактируемый | ✅ | ❌ | ✅ | ✅ | ✅ | n/a |
| Toolchain тяжесть | лёгкий | средний | средний | лёгкий | средний | лёгкий |
| Кривая обучения | низкая | средняя | высокая | низкая | средняя | средняя |
| Активность сообщества | большая | очень большая | средняя | огромная | растущая | огромная |

---

## Моё предложение

**Основной кандидат: Marp.**

**Почему:**
1. Markdown-source с минимальным CSS — идеально под repo-first.
2. **PPTX-output редактируемый** — критично для D1 (внешний рецензент может править/комментировать).
3. Multi-format одной командой: HTML / PDF / PPTX из одного `.md`.
4. Лёгкий toolchain — один npm package, работает в VS Code preview.
5. Достаточная гибкость для наших 6 типов через CSS classes.
6. Стабильный, активно развивается, никакой vendor lock-in.

**Backup-кандидат: Slidev.**

**Когда переключиться на Slidev:**
- Если в спайке окажется, что layout'ы Marp не покрывают `live_demo`, `poll_reveal`, `assertion_visual` без изобретательной возни с CSS.
- Если важнее web-публикация курса (интерактив).
- Принимая минус: PPTX = картинки, комментарии в Drive привязываются только к слайду как образу.

**Конкретный спайк (F.0):**
1. Беру слайд **s05** из плана v4 (instructor-card + центральный вопрос — `assertion_visual`).
2. Делаю в Marp: markdown + CSS-classes → PPTX.
3. Делаю в Slidev: markdown + layout → PPTX.
4. Сравниваем визуально, проверяем редактируемость текста в обоих PPTX.
5. Решаем.

Спайк делает subagent (как обычная реализация), результат — в `notes/issue-52-.../tool-spike/`.

---

## Что нужно от пользователя для перехода к F

1. **Подтвердить план спайка** (Marp vs Slidev на одном слайде s05) — или предложить другой инструмент / сразу выбрать без спайка.
2. **Уточнить D1 фидбэк-цикл** — на твой взгляд, для внешних рецензентов критична редактируемость PPTX, или достаточно комментариев в Drive поверх изображений? (Это тонкий момент: Marp = можно править текст; Slidev = только комментировать.)
3. **Где живёт renderer** — `tools/presentation-build/` в репо (новая папка) или в `library/lectures/_setup.md` инструкция «как поставить локально»? Я бы делал и то и другое: инструменты ставятся локально (npm global), а в `tools/presentation-build/` лежат CSS-темы / layout-шаблоны / npm scripts.
4. **OAuth (D10)** — если выбираем Marp/Slidev, render даёт PPTX-файл локально. Заливка в Drive — через `mcp__workspace-mcp__create_drive_file` (нужен живой OAuth). Если token не работает — пилот всё равно встанет на upload. Стоит проверить.

---

## Дополнительно (D8 — методические улучшения первых 5 слайдов плана v4)

Прохожу первые 5 слайдов критически:

**Слайд 1 (live-demo CV):** ✅ методически сильно. Только техническая надёжность критична — backup-план есть.

**Слайд 2 (cover):** ⚠️ «без комментариев», 0.5 мин. Cover читается студентами **молча**, и это пустое. Предложение: на cover вынести **центральный вопрос крупно** — это дает сюжетную линию с самого старта (а не отложенно на s05). Тогда на s05 центральный вопрос — уже знакомый якорь, не первая встреча.

**Слайды 3+4 (poll-reveal):** ⚠️ 3 вопроса в s03 за 1.5 мин — много. Каждый вопрос с reveal-руками = ~30 сек минимум. Предложение: **2 вопроса вместо 3**. Третий («кто проверяет ответы?») — переносится в раздел про галлюцинации (он там и нужен как мост к anti-pattern).

**Слайд 5 (instructor + рамка + центральный вопрос):** ⚠️ **4 разных идеи на один слайд за 2 мин** — нарушает «одна мысль на слайд». Предложение: **разделить** на:
- s05a — «Обо мне» (1 мин, простой instructor card).
- s05b — «Рамка курса для ИУ6 + центральный вопрос» (1 мин, assertion_visual с вопросом).

Это даёт **6 слайдов вместо 5 на старте**, но методически чище. Можно остановиться на 5 (s05a+b объединены), если хотим минимум для пилота.

**Общая нота по ритму:** 9 минут до первого содержательного материала про AI — **рискованно** для удержания. Можно ли сжать s02–s05 до 6 минут (-3 мин для содержания)?

→ Эти методические замечания не блокируют выбор инструмента; решаем в F.3 после F.0–F.2.

---

## Лог решений

(Заполнится после раунда 2.)
