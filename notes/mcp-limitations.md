# MCP Limitations & Workarounds — централизованный каталог

**Назначение:** единое место для всех известных limitations, багов, отсутствующих фич и обходов в MCP-серверах проекта (и render-toolchain'а).

**Зачем:** не наступать дважды на одни и те же грабли. До использования MCP-tool, который раньше падал, **обязательно** проверь свой сервер ниже.

---

## Правило обязательной актуализации

Этот файл **поддерживается всеми**, кто работает с MCP в проекте (Claude как orchestrator, любой subagent).

**Когда обновлять (немедленно, в той же сессии):**
- MCP-tool вернул ошибку, которая не лечится исправлением аргументов.
- MCP-tool отработал, но результат явно неверен (баг внутри сервера).
- Нужная функциональность отсутствует, и мы выкрутились через workaround.
- Render-toolchain (libreoffice, pdftoppm, drawio CLI и т.п.) даёт устойчивый артефакт.

**Что записывать (см. шаблон ниже):**
1. Сервер + tool/feature.
2. Симптом — что конкретно происходит.
3. Корневая причина — если выяснили (и где увидели в исходнике).
4. Severity (P0 блокер / P1 серьёзно мешает / P2 надо при масштабировании / P3 косметика).
5. Workaround — что делать прямо сейчас.
6. Status: `active` / `fixed-in-fork` / `fixed-upstream` / `wontfix-by-upstream`.
7. Ссылки: issue, где впервые обнаружено + версия сервера.

**Когда снимать запись:**
- `fixed-upstream` подтверждён — оставить как «historical» (date stamp), не удалять (для истории).
- `fixed-in-fork` после миграции на форк — переписать в «как было» с пометкой fork SHA.

---

## Шаблон записи

```markdown
### [#NN] Краткое название (sNN — server, tool/feature)

- **Server:** `powerpoint` (office-powerpoint-mcp-server v2.0.7)
- **Tool / feature:** `format_runs`
- **Symptom:** Каждый run после первого попадает в новый paragraph.
- **Root cause:** `tools/content_tools.py:456-459` — `text_frame.add_paragraph()` вместо `paragraph.add_run()`. Подтверждено чтением исходника.
- **Severity:** P1
- **Workaround:** Для inline-эмфазиса — несколько отдельных textbox'ов с разным форматированием либо отказаться от inline. Если нужно несколько paragraph'ов — оставить как есть.
- **Status:** active
- **First seen in:** #54 (s05b spike, 2026-05-12)
- **Fork target:** наш форк (планируется в #56)
```

---

## powerpoint (office-powerpoint-mcp-server v2.0.7, GongRzhe — архивирован)

### [#54-1] Нет `list_shapes` / `get_shape_properties` для visual-loop правок

- **Server:** `powerpoint` (v2.1.0 internal / pip 2.0.7)
- **Tool / feature:** отсутствуют tools для inspection шейпов на слайде.
- **Symptom:** Чтобы знать что лежит на слайде (тип, позиция, размер, текст), агент держит mental-model порядка `add_shape`/`add_text`-вызовов и shape_index'ов. При длинных deck'ах легко рассинхронизироваться.
- **Root cause:** GongRzhe MCP не предоставляет inspection-API над `slide.shapes`. python-pptx это умеет (`slide.shapes` → list, `.shape_type`, `.left`, `.top`, `.width`, `.height`, `.text_frame.text`).
- **Severity:** P1
- **Workaround:** Держать «mental model» индексов в порядке добавления. Каждая итерация = новая presentation с нуля (см. #54-3).
- **Status:** active
- **First seen in:** #54 (s05b spike, 2026-05-12)
- **Fork target:** добавить `list_shapes(slide_index)` → массив `{shape_index, type, name, left, top, width, height, text?}` и `get_shape_properties(slide_index, shape_index)`. ~2-3 часа работы. Планируется в #56.

### [#54-2] `format_runs` ломает inline-эмфазис (теряет paragraph и alignment)

- **Server:** `powerpoint`
- **Tool / feature:** `manage_text(operation="format_runs")`.
- **Symptom:** Каждый run после первого попадает в **новый paragraph**, а не в текущий → каждый bold-кусочек на отдельной строке. Также теряется alignment текстового бокса (сбивается на left). Inline-выделение цифр в одной строке (например, `bold "10%"` внутри обычного текста) невозможно.
- **Root cause:** `tools/content_tools.py:456-459` GongRzhe MCP — использует `text_frame.add_paragraph()` вместо `paragraph.add_run()`. Подтверждено чтением исходника.
- **Severity:** P1 (для типографики критично)
- **Workaround:** Для inline-эмфазиса — несколько отдельных textbox'ов с разным форматированием рядом. Либо отказаться от inline-выделения (use uniform color). Если нужны несколько строк — оставить как есть.
- **Status:** active
- **First seen in:** #54 (s05b spike, iter-2, 2026-05-12)
- **Fork target:** Зафиксить — добавить ключ `inline: true` в run schema, либо новую операцию `format_inline_runs`. Сохранять alignment textbox'а. Планируется в #56.

### [#54-3] Нет `update_shape_position` / `delete_shape` / `resize_shape`

- **Server:** `powerpoint`
- **Tool / feature:** отсутствуют mutating-tools для существующих шейпов.
- **Symptom:** Чтобы что-то «передвинуть» в visual-loop — нужно создавать presentation с нуля и заново добавлять все шейпы с новыми параметрами. Дёшево для 1-3 слайдов, дорого для 29-слайдной деки.
- **Root cause:** GongRzhe MCP не оборачивает python-pptx mutating-API.
- **Severity:** P2 (узкое место при масштабе)
- **Workaround:** Полная пересборка presentation на каждой итерации. ОК для пилота #55 (6 слайдов).
- **Status:** active
- **First seen in:** #54 (s05b spike, 2026-05-12)
- **Fork target:** `update_shape_position(slide_index, shape_index, left?, top?, width?, height?)` + `delete_shape(slide_index, shape_index)`. Планируется в #56 при первой реальной нужде (вероятно когда дека станет >10 слайдов).

### [#54-4] `vertical_alignment="middle"` неполный с `auto_fit`

- **Server:** `powerpoint`
- **Tool / feature:** `manage_text(operation="add", vertical_alignment="middle")`.
- **Symptom:** Текст оседает в верхней части textbox'а с пустым пространством снизу (~30%). Конфликт с python-pptx auto_fit.
- **Root cause:** Не выяснено детально (предположительно: auto_fit меняет высоту шрифта/строк, vertical_alignment работает с фактической высотой контейнера, а не с актуальной высотой текста).
- **Severity:** P2
- **Workaround:** Подгонять `height` бокса под визуальную высоту текста (~1.0× визуальной высоты). На спайке #54 этим путём дошли до годного результата (iter-5 → iter-6: уменьшили height с 2.5 до 2.0).
- **Status:** active
- **First seen in:** #54 (s05b spike, iter-5, 2026-05-12)
- **Fork target:** низкий приоритет — workaround надёжный.

### [#55-1] `create_presentation` создаёт 4:3 (10×7.5") по умолчанию, нет опции 16:9

- **Server:** `powerpoint`
- **Tool / feature:** `create_presentation` (нет параметров `slide_width` / `slide_height` / `aspect_ratio`).
- **Symptom:** Все новые презентации — 9144000×6858000 EMU = 10×7.5 дюймов = 4:3. Современные decks 16:9 (13.333×7.5) — нужен post-processing.
- **Root cause:** GongRzhe MCP оборачивает `Presentation()` без overrides. python-pptx default — это шаблон с 4:3 размером.
- **Severity:** P1 (на современных проекторах 4:3 выглядит дёшево + контент строится для 13.333" wide и обрезается).
- **Workaround:** После `save_presentation` патчить через python-pptx:
  ```python
  from pptx import Presentation
  from pptx.util import Inches
  p = Presentation('path.pptx')
  p.slide_width = Inches(13.333)
  p.slide_height = Inches(7.5)
  p.save('path.pptx')
  ```
  Шейпы при ресайзе **не двигаются** — остаются на абсолютных координатах. Поэтому строй контент сразу для 13.333×7.5, потом ресайзи canvas.
- **Status:** active.
- **First seen in:** #55 redo (2026-05-12). Документировано в `library/lectures/lec-01/rendered/iteration-log.md`.
- **Fork target:** добавить `aspect_ratio` параметр в `create_presentation` (`"4:3" | "16:9" | "16:10" | "widescreen"`). ~30 минут работы.

### [#55-2] `add_slide(background_type="solid", background_colors=...)` НЕ применяет фон слайда

- **Server:** `powerpoint`
- **Tool / feature:** `add_slide(layout_index=6, background_type="solid", background_colors=[[10,14,39]])`.
- **Symptom:** Параметр `background_colors` не создаёт `<p:bg>` элемент в slide XML — слайд остаётся с дефолтным белым фоном (наследуется от master). Команда возвращает success, но визуально dark background не появляется.
- **Root cause:** Не выяснено детально — возможно, фон применяется к `slide.background` через python-pptx API, который меняет shape-fill master'а (или просто игнорируется без `gradient_direction` валидации).
- **Severity:** P1 (для cover/section divider слайдов с тёмным фоном)
- **Workaround:** После save patch через python-pptx с inject `<p:bg>` XML:
  ```python
  from lxml import etree
  from pptx.oxml.ns import qn
  cSld = slide.element.find(qn('p:cSld'))
  bg_xml = '<p:bg xmlns:p="..."><p:bgPr><a:solidFill><a:srgbClr val="0A0E27"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>'
  cSld.insert(0, etree.fromstring(bg_xml))
  ```
- **Status:** active.
- **First seen in:** #55 redo (2026-05-12), s02 cover slide.
- **Fork target:** проверить почему `background_colors` arg не работает; вероятно нужно прокинуть в `slide.background.fill.solid()` + `fore_color.rgb`. ~1 час работы.

### [#55-3] `manage_text(text_runs=...)` для inline-эмфазиса — отсутствует операция inline runs

- **Server:** `powerpoint`
- **Tool / feature:** `manage_text` operation set.
- **Symptom:** Чтобы выделить часть текста (например, «10%» отдельным цветом в central question), `manage_text(text_runs=...)` есть в schema, но `format_runs` ломает paragraph (см. #54-2). Inline runs недоступны через MCP.
- **Root cause:** Связано с #54-2 — `format_runs` использует `add_paragraph` вместо `add_run`.
- **Severity:** P1 (для accent typography)
- **Workaround:** После save patch через python-pptx:
  ```python
  from pptx.dml.color import RGBColor
  tf = shape.text_frame
  tf.clear()
  para = tf.paragraphs[0]
  r1 = para.add_run(); r1.text = "часть 1"; r1.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
  r2 = para.add_run(); r2.text = "10%"; r2.font.color.rgb = RGBColor(0xF0,0xAB,0x00)
  ```
- **Status:** active (см. #54-2 fork target).
- **First seen in:** #55 redo (2026-05-12), s02 cover slide highlight «10%».
- **Fork target:** см. #54-2.

### [#54-5] `manage_text(operation="add")` шейп-индексация после правок

- **Server:** `powerpoint`
- **Tool / feature:** `manage_text` использует positional `shape_index`.
- **Symptom:** При итерациях с `format_runs` (см. #54-2) и пересборкой стека, проще всего создать presentation заново — индексы шейпов плывут.
- **Root cause:** Связано с #54-1 (нет list_shapes) и #54-3 (нет mutating tools).
- **Severity:** P2 (следствие #54-1 + #54-3)
- **Workaround:** Same as #54-3 — пересборка с нуля.
- **Status:** active
- **First seen in:** #54 (s05b spike, 2026-05-12)
- **Fork target:** закроется через #54-1 + #54-3.

### [#71-1] PowerPoint MCP — нет `list_shapes` / `update_shape_position` (Лекция 1 production scale)

- **Server:** `powerpoint` (office-powerpoint-mcp-server v2.0.7).
- **Tool / feature:** отсутствуют `list_shapes`, `update_shape_position`, `delete_shape`, `resize_shape` (extension #54-1 + #54-3 при production scale).
- **Symptom:** Полная пересборка presentation на каждой visual-loop итерации вместо in-place modifications. Для 33-слайдной деки Лекции 1 × 14+ visual loop iterations = ~2-3 hours overhead just на rebuild scaffolding.
- **Root cause:** см. #54-1 + #54-3 — отсутствие inspection + mutating API.
- **Severity:** **P0 fork candidate.** ROI estimate (full course): list_shapes + update_shape_position сэкономит ~3-5 min per visual iter × 14 iter × 17 lectures = 12-20 hours. Fork = 3 hours one-time → **4× ROI**.
- **Workaround:** Текущий — full python-pptx rebuild каждую iteration. Designer держит mental model индексов в порядке добавления.
- **Status:** active (fork recommended до Лекции 2).
- **First seen in:** Л1 v3.x production (2026-05-13).
- **Fork target:** см. #54-1 + #54-3 — добавить `list_shapes(slide_index)` + `update_shape_position(slide_index, shape_index, left?, top?, width?, height?)` + `delete_shape(slide_index, shape_index)`. См. CONSOLIDATED implementation phase 6.

### [#71-2] LibreOffice convert overhead at scale

- **Tool:** `libreoffice --headless --convert-to pdf` в Visual Loop.
- **Symptom:** Каждая визуальная итерация = libreoffice headless ~2-3 sec на 30+ slides. 32 slides × N iterations = significant cumulative time. С 14 итерациями × 5 параллельных designers = 1+ minute чистого latency только на convert.
- **Root cause:** LibreOffice headless single-threaded; каждый convert spawns full process.
- **Severity:** P2 (workaround существует).
- **Workaround:** (a) limit to N=5 iter cap per slide; (b) batch convert vs per-iter (запускать convert one для всех designers); (c) reduce slide count для visual loop (focus на изменённые slides only); (d) per-slide convert если возможно.
- **Status:** active.
- **First seen in:** Л1 v3.x production (2026-05-13).

### [#71-3] Snapshots bloat — repo size scaling

- **Tool:** `pdftoppm` snapshots в Visual Loop.
- **Symptom:** Лекция 1 production оставила 562 PNG snapshots @ 110-150 dpi = 71 MB в repo. Estimated 17 lectures × 71 MB = **1.2-3.6 GB на курс** если без `.gitignore`. GitHub max repo рекомендация ≤1 GB soft.
- **Root cause:** Snapshots — build artefacts (regenerable from PPTX через libreoffice), но commit'ились по умолчанию.
- **Severity:** **P0 для масштабирования** (без gitignore = repo unusable за 6 лекций).
- **Workaround:** `.gitignore` policy:
  ```
  # Lecture rendered snapshots (regeneratable from PPTX)
  library/lectures/*/rendered/snapshots/
  # Iteration logs per-version (use single rolling iteration-log.md instead)
  library/lectures/*/rendered/iteration-log-v*.md
  # Old build scripts (consolidate to single canonical build.py per lecture)
  library/lectures/*/rendered/build_*_v*.py
  ```
  Decision: ALL snapshots gitignored (включая финальные `sNN.png`) — regenerable from PPTX. Если нужен публичный snapshot view — separate `published/` directory.
- **Status:** active (hygiene phase pending).
- **First seen in:** Л1 v3.x production (2026-05-13). См. CONSOLIDATED implementation phase 5.

---

## workspace-mcp (uvx workspace-mcp)

### [#49] OAuth refresh token отзывается каждые 7 дней (Testing publishing status)

- **Server:** `workspace-mcp`
- **Tool / feature:** все Drive/Docs/Sheets/Slides tools.
- **Symptom:** Все вызовы возвращают `ACTION REQUIRED: Google Authentication Needed`, хотя `claude mcp list` показывает сервер как `✓ Connected`.
- **Root cause:** OAuth-приложение в Google Cloud Console находится в **Testing** publishing status. В этом режиме refresh_token автоматически отзывается через 7 дней неактивности.
- **Severity:** P0 (всё лежит)
- **Workaround:** Пройти OAuth-flow заново — любой первый вызов `workspace-mcp`-инструмента возвращает auth URL, после клика и согласия в браузере токен пишется обратно в `~/.google_workspace_mcp/credentials/kzlevko@gmail.com.json`.
- **Long-term fix:** в Google Cloud Console → OAuth consent screen → переключить Publishing status с **Testing** на **In production**. Тогда refresh_token становится бессрочным.
- **Status:** active (workaround working; long-term fix не сделан)
- **First seen in:** #49 (2026-04-29). См. также `notes/decisions.md` § «2026-04-29 — workspace-mcp OAuth refresh expiry».

### [#27] `find_and_replace_doc` ломает таблицы при неуникальных match'ах

- **Server:** `workspace-mcp`
- **Tool / feature:** `find_and_replace_doc`.
- **Symptom:** При работе с большими таблицами с похожими ячейками, `find_and_replace_doc` может затронуть лишние occurrences (например, `8.5` → `15` затрагивает не только нужную ячейку, но и числа в других ячейках/ISBN страниц книг).
- **Root cause:** Plain-text поиск без контекста; короткие/неуникальные строки имеют ложные совпадения.
- **Severity:** P1 (data corruption риск)
- **Workaround:** Использовать `mcp__workspace-mcp__batch_update_doc` + explicit `replace_text` по start/end character indices, полученным из `debug_table_structure`. Применять правки highest-to-lowest, чтобы не сдвигать индексы. Для больших таблиц `debug_table_structure` >25KB — читать в чанках через `Read` с offset/limit.
- **Status:** active (поведение by design)
- **First seen in:** #51 Phase 4B (2026-04-29). См. `notes/decisions.md` § «2026-04-29 — Phase 4B Doc#2 РПД (#51) — partial, lessons learned».

---

## drawio (npx @drawio/mcp)

_Пока не обнаружено. Записи добавляются по мере появления._

---

## document-loader (uvx awslabs.document-loader-mcp-server)

_Пока не обнаружено._

---

## github (github-mcp-server)

### [common] Pagination для `list_*` tools требует `endCursor`

- **Server:** `github`
- **Tool / feature:** `list_issues`, `list_pull_requests`, `list_branches` etc.
- **Symptom:** При большом числе записей по умолчанию возвращается первая страница. Без явной pagination легко пропустить старые записи.
- **Root cause:** by design (GraphQL pagination).
- **Severity:** P3 (поведение нормальное, но ловушка для невнимательных)
- **Workaround:** Использовать `endCursor` из `pageInfo` предыдущего ответа в параметре `after`. Также, согласно MCP server instructions, лимит 5-10 элементов на страницу для context management.
- **Status:** active (by design)
- **First seen in:** документация MCP server.

---

## local-rag (npx mcp-local-rag)

### [generic] Cross-lingual RAG слабо работает RU↔EN

- **Server:** `local-rag`
- **Tool / feature:** `query_documents`.
- **Symptom:** Query на одном языке плохо находит документы на другом языке.
- **Root cause:** Используемая embedding-модель не bilingual.
- **Severity:** P2 (понятно, но мешает)
- **Workaround:** **Не добавлять переводы документов** для починки RAG. Чинить на query layer — делать bilingual queries (написать запрос на двух языках), либо использовать Wiki/Ontology tier для cross-lingual поиска.
- **Status:** active (architectural)
- **First seen in:** ранние тесты RAG. См. user memory `feedback_rag_crosslingual.md`.

---

## open-ontologies (open-ontologies serve)

_Пока не обнаружено._

---

## Render toolchain (adjacent инструменты, не MCP)

### [#55-render-1] mermaid-cli (`mmdc`) требует Chrome, отсутствует в WSL Ubuntu 24.04 by default

- **Tool:** `mmdc` (`@mermaid-js/mermaid-cli` 11.14.0).
- **Symptom:** `mmdc -i in.mmd -o out.png` падает с `Could not find Chrome (ver. 148.0.7778.97)` и `puppeteer-core` cache miss.
- **Root cause:** `mmdc` использует Puppeteer, который ждёт chromium binary по `~/.cache/puppeteer`. В WSL по умолчанию Chrome нет, `npx puppeteer browsers install chrome-headless-shell` не выполнялся.
- **Severity:** P2 (workaround надёжный).
- **Workaround:** Писать диаграммы вручную как **SVG** (литеральный XML с rect/circle/path/text) → конвертить через `rsvg-convert -w W -h H -f png in.svg -o out.png`. Полный контроль над typography, цветами палитры, layout. Эта же стратегия лучше для строгого соответствия palette (Mermaid не даёт точно палитру).
- **Status:** active.
- **First seen in:** #55 redo (2026-05-12). Документировано в `library/lectures/lec-01/rendered/iteration-log.md`.

### [#55-render-2] QuickChart `indexAxis: y` игнорируется без `version: "4"`

- **Tool:** QuickChart API (`https://quickchart.io/chart`).
- **Symptom:** Запрос на horizontal bar chart с `options.indexAxis: "y"` рендерится как vertical bar; `dataset.label` не задан → легенда показывает `undefined`. С `borderRadius` для каждого bar и др. Chart.js v3+ свойствами тоже не работает.
- **Root cause:** QuickChart по умолчанию использует Chart.js **v2**, где `indexAxis` отсутствует, нужен `chart.type: "horizontalBar"`. Чтобы получить v3/v4 поведение, надо явно передать `"version": "4"` в JSON-payload.
- **Severity:** P2 (workaround точечный).
- **Workaround:** В POST-запросе в JSON всегда добавлять `"version": "4"` рядом с `"chart"`, `"width"`, `"height"`. Также включать `plugins.legend.display: false` чтобы скрыть `undefined`-label при пустом `dataset.label`.
- **Status:** active.
- **First seen in:** #55 redo (2026-05-12), при сборке s04 charts.

### [#69-render-1] Snapshot resolution mismatch: 110dpi скрывает overlap-bugs которые видны на 150dpi

- **Tool:** `pdftoppm` snapshots при iterative visual loop.
- **Symptom:** При итерациях с 110dpi PNG-снапшотами всё «выглядит ОК», но при финальной 150dpi inspection обнаруживаются множественные overlapping textbox'ы и обрезанные элементы (например s09 deck Лекции 1 — счётчик «$244-390B» прятался за gold counter-fact band'ом, видно только при 150dpi).
- **Root cause:** Не баг — поведение by design. 110dpi даёт ~1450×815 PNG, в котором мелкий текст (10-12pt) сжимается до неразличимости; 150dpi даёт ~2000×1125 PNG где видна каждая строка.
- **Severity:** P2 (workaround — discipline).
- **Workaround:** Финальная inspection слайдов с тяжёлыми content (charts, multi-region layouts, dense tiles) ОБЯЗАТЕЛЬНА при 150dpi. Iterations 1-2 ОК на 110dpi (быстрее); iter-3 final accept — всегда 150dpi.
- **Status:** active (workflow rule).
- **First seen in:** #69 (full 29-slide deck Лекции 1, 2026-05-12). Обнаружено при iter-3 inspection s09 — на 110dpi казалось ОК, на 150dpi видна явная overflow проблема.

### [#73-render-1] python-pptx `add_picture(width=W, height=H)` стрейчит изображение non-proportionally

- **Tool:** `python-pptx` `slide.shapes.add_picture(path, x, y, width=W, height=H)`.
- **Symptom:** When BOTH `width` AND `height` are passed, python-pptx stretches
  the image to exactly `(W, H)` dimensions — non-proportional distortion.
  Portraits become squashed landscapes; landscapes become elongated rectangles.
  User-visible quality issue («иллюстрации сжаты непропрорционально»).
- **Root cause:** by design in python-pptx — both dimensions are absolute, not
  "fit-inside-box". To preserve aspect, caller must compute either width-only
  or height-only based on image actual dimensions.
- **Severity:** P1 (visible quality bug, easy to overlook in build scripts).
- **Workaround:** Wrap `add_picture` in a helper that uses Pillow (PIL) to read
  image dimensions, then:
  - Compute `img_ratio = img_w / img_h` and `box_ratio = w / h`.
  - If `img_ratio > box_ratio` → constrain by width, center vertically.
  - Else → constrain by height, center horizontally.
  - Pass ONLY the constraining dimension to `add_picture()`.
  - Example: `library/lectures/lec-04/rendered/build_lec04.py:add_image()`.
- **Status:** active (workaround standard).
- **First seen in:** Лекция 4 Phase 8.6 surgical revision (2026-05-13, #73).

### [#69-svg-fallback] Литерал-SVG + rsvg-convert как fallback для diagrams когда mermaid не работает

- **Tool:** `rsvg-convert` + ручной SVG.
- **Symptom:** Mermaid CLI требует Chrome (см. [#55-render-1]); в WSL не установлен.
- **Workaround:** Создавать SVG литералом (heredoc или через Write tool) с inline styles в палитре проекта, конвертировать через `rsvg-convert -w W -h H -f png in.svg -o out.png`. Полный контроль типографики и палитры. Использовался для `d2-funnel-v36-clean.png` (3-уровневая воронка с Ocean palette + gold endpoint).
- **Преимущества vs mermaid:** точное соответствие палитре; нет рандомных layout shifts; reproducible bit-by-bit.
- **Недостатки:** ручная работа на каждую diagram; не подходит для сложных flowchart'ов с автоматическим layout.
- **Status:** preferred fallback when mermaid не работает.
- **First seen in:** #69 (2026-05-12).

### [#54-render-1] LibreOffice headless добавляет drop-shadow к rectangle при PDF-export

- **Tool:** `libreoffice --headless --convert-to pdf` (LibreOffice 24.2.7.2).
- **Symptom:** При конверсии PPTX → PDF на rectangle-shape, созданных через python-pptx, появляется дефолтная drop-shadow. В реальном PowerPoint клиента её может не быть — артефакт LibreOffice render.
- **Root cause:** LibreOffice применяет default shadow на shape без явного `effectLst`.
- **Severity:** P3 (косметика)
- **Workaround:** На спайке #54 принимаем как есть. Для production — можно явно `shadow=False` через python-pptx (но текущий MCP-tool это не выставляет).
- **Status:** active (LibreOffice behavior)
- **First seen in:** #54 (s05b spike, 2026-05-12).

---

## Историческая справка

- **2026-04-29 (#49):** workspace-mcp OAuth fix.
- **2026-04-29 (#51):** find_and_replace_doc gotcha с большими таблицами.
- **2026-05-12 (#54):** PowerPoint MCP — 5 limitations найдено за один спайк.
- **2026-05-12 (#55 redo):** PowerPoint MCP — 3 новых (slide-size 4:3 default, dark bg ignored, inline runs); render-toolchain — 2 (mermaid Chrome missing, QuickChart v4 explicit).
- **2026-05-13 (#71 — Лекция 1 v3.x production):** добавлены [#71-1] PowerPoint MCP fork-priority elevation (production scale), [#71-2] LibreOffice convert overhead, [#71-3] Snapshots bloat → P0 gitignore policy.

При обнаружении новой limitation — добавить запись по шаблону, обновить дату «Last update» ниже, упомянуть в commit message: `Add MCP limitation #X (server) — see notes/mcp-limitations.md`.

---

**Last update:** 2026-05-13 (Лекция 4 Phase 8.6 — добавлен [#73-render-1] python-pptx add_picture non-proportional stretch bug + Pillow-based workaround).
