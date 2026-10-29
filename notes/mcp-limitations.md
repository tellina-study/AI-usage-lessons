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

### [#86] `uvx workspace-mcp` не стартует — регрессия транзитивной зависимости `aiofile` 3.10.0 (`KeyError: 'Author'`)

- **Server:** `workspace-mcp` (uvx, без пина версии).
- **Tool / feature:** запуск сервера целиком (все 120 tools недоступны, `claude mcp list` → `✗ Failed to connect`).
- **Symptom:** При старте — Python traceback на импорте: `workspace-mcp → fastmcp.server.auth.oauth_proxy → key_value.aio.stores.filetree → aiofile/__init__ → aiofile/version.py` → `__author__ = package_metadata["Author"]` → `KeyError: 'Author'` (через `importlib_metadata/_adapters.py:102`).
- **Root cause:** `aiofile==3.10.0` (последняя на 2026-05-16) собрана без поля `Author` в wheel-метадате, а её `version.py` обращается к `package_metadata["Author"]` напрямую (хрупкий код, без `.get`). `uvx` без пина тянет latest → ломается. Баг не в workspace-mcp, а в транзитивной зависимости.
- **Severity:** P0 (сервер полностью не стартует; блокирует весь Google Workspace).
- **Workaround:** пин рабочей версии `aiofile` через uvx `--with`. В `.mcp.json` (gitignored) `workspace-mcp.args` = `["--with", "aiofile==3.9.0", "workspace-mcp"]`. Проверено эмпирически: `3.9.0` и `3.8.8` стартуют чисто («Starting MCP server 'google_workspace' with transport 'stdio'»), `3.10.0` падает. Требуется рестарт Claude Code для применения (как любая MCP-config-правка).
- **Status:** active (workaround в .mcp.json применён 2026-05-16, вступает в силу после рестарта; upstream aiofile/workspace-mcp не патчены).
- **First seen in:** #86 (2026-05-16) — забор плана курса; обойдено пользовательской вставкой текста + пином.

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

### [#201-4] `pdftoppm -r 150` на 70+ слайдах регулярно превышает 2-минутный дефолтный bash-timeout

- **Tool:** `pdftoppm` (poppler-utils, portable build из `/home/harness/.local/lo-portable-env.sh`).
- **Symptom:** `pdftoppm -r 150 -png sem-04.pdf snapshots/iter` на 72-слайдной колоде (16:9, 150dpi ≈ 2000×1125px на страницу) занимает **~76 секунд только на растеризацию**, не считая предшествующей `soffice --headless --convert-to pdf` конверсии (тоже не мгновенная на 72 слайда с множеством shape'ов/таблиц). Суммарно `soffice`+`pdftoppm` в одной команде на такой колоде **надёжно превышает** дефолтный 120-секундный timeout инструмента Bash — команда была прервана (`exit 143`) на середине, PDF уже успел перезаписаться, но PNG-растеризация осталась недоделанной (52 из 72 страниц).
- **Root cause:** не баг — `pdftoppm` растеризует постранично однопоточно; 150dpi на 16:9-канвасе с плотным контентом (таблицы, множество текстовых фигур) даёт ~1 сек/страницу, что на 70+ слайдах суммарно превышает типичный дефолтный Bash-таймаут инструментов агента.
- **Severity:** P2 (workaround тривиален, но легко попасть в состояние «PDF свежий, PNG устарели/неполные», если не заметить прерывание).
- **Workaround:** (a) запускать конвертацию/растеризацию с явным увеличенным `timeout` (например 180000ms) вместо дефолтного; (b) разделять `soffice --convert-to pdf` и `pdftoppm` на отдельные команды, чтобы таймаут/прогресс каждой был виден отдельно, а не терялся в одной составной цепочке; (c) после любого прерывания — **обязательно сверить количество PNG в `snapshots/` с числом слайдов в PDF/PPTX** (`pdfinfo`/`python-pptx`), не полагаться на то, что команда «в целом отработала».
- **Status:** active (workaround рабочий).
- **First seen in:** #201 (Семинар 4 v3, полная пересборка 65→72 слайдов, 2026-09-22).

### [#201-5] Общий `ROOT`/`OUT`-путь в build-скрипте и его `.bak`-копии — случайный запуск бэкапа молча перезаписывает свежий артефакт

- **Tool:** паттерн build-скрипта (`build_semNN.py`/`build_lecNN.py` — техника, не баг конкретного tool'а).
- **Symptom:** Если перед правкой build-скрипта сохранить старую версию рядом как `build_sem04.py.v2.bak` (стандартная практика этой сессии для диагностики/сравнения OVERFLOW-варнингов), а затем **исполнить её напрямую** (`python3 build_sem04.py.v2.bak`) для получения списка старых warning'ов — скрипт вычисляет `ROOT = Path(__file__).resolve().parent.parent`, что для файла `rendered/build_sem04.py.v2.bak` резолвится **в тот же самый** `sem-04/`-каталог, что и для актуального `build_sem04.py`. Оба пишут в один и тот же `OUT = ROOT / "rendered/sem-04.pptx"` — бэкап **молча перезаписывает** только что собранный актуальный `.pptx` старой (65-слайдной) версией, без единого предупреждения (скрипт не знает и не может знать, что он не «канонический»).
- **Root cause:** `ROOT`/`OUT` вычисляются относительно `__file__`, а не абсолютным хардкодом с проверкой имени файла — предположение «в этой папке всегда ровно один build-скрипт, который когда-либо исполняется» ломается, как только появляется вторая исполняемая копия рядом.
- **Severity:** P1 (тихая порча только что провалидированного артефакта; обнаруживается только по несовпадению числа слайдов при следующей проверке — в этой сессии поймано немедленно, но легко пропустить).
- **Workaround:** (a) никогда не оставлять `.bak`-копии build-скрипта **исполняемыми на этом же PATH/cwd** дольше, чем нужно для непосредственного diff — удалять сразу после сравнения (`diff`/`grep`), не как «на всякий случай»; (b) если нужно именно прогнать старую версию (не только почитать), явно менять `OUT` inline (`sed`/аргумент) или копировать в отдельную scratch-директорию с собственным `ROOT`; (c) после любого запуска стороннего/архивного варианта скрипта — обязательно пересобрать актуальный перед следующим шагом пайплайна (конвертация/снапшоты), не полагаться на «наверное ничего не изменилось».
- **Status:** active (дисциплина, не инструмент — воспроизведено и исправлено в той же сессии).
- **First seen in:** #201 (Семинар 4 v3, 2026-09-22) — `build_sem04.py.v2.bak` перезаписал `sem-04.pptx` 65-слайдной версией между двумя проверками OVERFLOW-варнингов; поймано по несовпадению числа слайдов, немедленно исправлено повторным запуском канонического скрипта + полной пересборкой PDF/PNG.

---

## Историческая справка

- **2026-04-29 (#49):** workspace-mcp OAuth fix.
- **2026-04-29 (#51):** find_and_replace_doc gotcha с большими таблицами.
- **2026-05-12 (#54):** PowerPoint MCP — 5 limitations найдено за один спайк.
- **2026-05-12 (#55 redo):** PowerPoint MCP — 3 новых (slide-size 4:3 default, dark bg ignored, inline runs); render-toolchain — 2 (mermaid Chrome missing, QuickChart v4 explicit).
- **2026-05-13 (#71 — Лекция 1 v3.x production):** добавлены [#71-1] PowerPoint MCP fork-priority elevation (production scale), [#71-2] LibreOffice convert overhead, [#71-3] Snapshots bloat → P0 gitignore policy.
- **2026-05-16 (#86 — снимок плана курса):** добавлен [#86] workspace-mcp P0 — регрессия `aiofile` 3.10.0 (`KeyError 'Author'`); workaround — пин `aiofile==3.9.0` через uvx `--with` в `.mcp.json`.

При обнаружении новой limitation — добавить запись по шаблону, обновить дату «Last update» ниже, упомянуть в commit message: `Add MCP limitation #X (server) — see notes/mcp-limitations.md`.

### [#171-1] `notes_pages_pdf.py` pairs page N с natural-sorted md — ломается на decks с непоследовательным build-order (lec-03)

- **Tool:** `tools/presentation-build/notes_pages_pdf.py` — техника/gotcha, не баг.
- **Symptom:** notes-PDF спаривает изображение слайда N (из `lec-NN.pdf`, build-order) с нотами N-го md в **natural-sort** порядке (`slide_md_by_index`). Если презентация рендерится НЕ в natural-sort порядке — ноты уезжают. Лекция 3 build_v3.py рендерит s15 ДО s14 и s23 поздно (после s25/s25b/s25a) по педагогическим причинам → на 6 страницах notes-PDF пары «картинка sX + ноты sY» были неверны (page 20: image s15 + notes s14 и т.д.).
- **Root cause:** `slide_md_by_index` предполагает natural-sort = build-order (верно для монотонных decks lec-01/02/04, неверно для lec-03).
- **Severity:** P1 (тихая рассинхронизация — ноты не того слайда; не видно без проверки хедеров «слайд N / M» против картинки).
- **Workaround:** тонкий per-lecture wrapper, monkeypatching `slide_md_by_index` явным build-order списком (тем же `sids`, что в build-скрипте). Пример: `library/lectures/lec-03/rendered/make_notes_pdf.py` — импортирует `notes_pages_pdf as N`, ставит `N.slide_md_by_index = _md_by_index` (по BUILD_ORDER), затем `N.build(LECDIR, dpi=150)`. Проверка: хедер каждой страницы «SNN · слайд K / 40» должен совпасть с позицией slide в build-order.
- **Status:** active (workaround рабочий; долгосрочно — добавить в notes_pages_pdf опциональный `--order` / чтение build-order из deck.yaml).
- **First seen in:** #171 (lec-03 reference-system + notes-PDF, 2026-08-30).

### [#171-2] Anchor-driven post-hoc [N] injection в готовый deck без baked-in маркеров (техника)

- **Tool:** `python-pptx` (build-скрипт) — техника, не баг.
- **Контекст:** нужно добавить надстрочные [N]-ref-маркеры на 26 слайдов, у которых body-текст НЕ содержал [N] (в отличие от lec-04, где [N] baked-in при авторинге). Переписывать 26 builder'ов вручную — рискованно.
- **Приём (reusable):** registry `ANCHORS[sid] = [(ref_nums, anchor_substr), …]`, где `anchor_substr` — verbatim фрагмент существующего run. Post-build pass (`inject_ref_markers`) обходит `slide.shapes`→text_frame→paragraphs→runs, находит run, содержащий anchor, и делает `run.text = run.text.replace(anchor, anchor + f"[{ref_nums}]", 1)`. Затем `shrink_refs_in_frame` (#170-3) уменьшает маркеры в надстрочные муты. Меняются ТОЛЬКО [N] — ноль изменений в словах visible-контента (подтверждено diff old↔new visible text: 40/40 слайдов идентичны после strip [N]+ref-list+pageno). Скрипт репортит любой unmatched anchor.
- **Аналогично для нот:** `NOTES_ANCHORS` + `patch_notes.py` вставляет [N] в `## Speaker notes` body .md + аппендит блок «Источники:». ВАЖНО: оперировать только над секцией Speaker notes (не над frontmatter/Title/Body) — иначе маркер уедет в `assertion:` frontmatter (случилось однажды, откачено). Split по `md.find("## Speaker notes")`, не по `md.find("Источники:")`.
- **Status:** working-pattern (reusable для любого deck без baked-in [N]).
- **First seen in:** #171 (lec-03, 2026-08-30).

---

**Last update:** 2026-09-22 (Семинар 4 v4, раскол на два семинара, 72→49 слайдов, полная
пересборка `build_sem04.py` с нуля — добавлен [#201-6] `grep -E`/`grep -P` `\b`
word-boundary ненадёжен на кириллице под `en_US.UTF-8` locale, даёт ложные срабатывания
внутри кириллических слов (например `\bмин\b` матчится внутри «минут») — воркэраунд:
верифицировать anti-pattern grep'ы через Python `re`, не голый shell `grep`). Ранее того же
дня: Семинар 4 v3, 65→72 слайдов — добавлены [#201-4] `pdftoppm`
на 70+ слайдах @150dpi регулярно превышает 2-минутный дефолтный bash-timeout (~76s только
растеризация) и [#201-5] общий `ROOT`/`OUT`-путь build-скрипта и его `.bak`-копии — случайный
прямой запуск бэкапа молча перезаписывает свежесобранный `.pptx` старой версией). Ранее:
2026-08-30 — notes-PDF rewrite, [#170-4b] `notes_pages_pdf.py` переписан по owner-спеке — ноты/заголовки читаются из PPTX (URL вернулись), матч слайд↔нота позиционный, футер = номер страницы, continuation без «продолжение»; supersedes match-по-.md из [#170-4]/[#170-4a]/[#171-1]. Ранее: #171 — [#171-1] build-order mismatch + wrapper, [#171-2] anchor-driven [N]-инъекция; #170 — [#170-4] notes-pages PDF builder, [#170-3] надстрочные [N] через run-split lxml).

### [#170-4] Reusable «notes-pages PDF» builder (портрет: слайд сверху + ноты снизу) на pymupdf — техника

- **Tool:** `tools/presentation-build/notes_pages_pdf.py` (pymupdf/fitz; не MCP) — техника, а не баг.
- **Контекст:** нужен «раздаточный» портретный PDF, где каждая страница = один
  слайд (картинкой) + его speaker notes читаемым текстом снизу, с поддержкой
  кириллицы и БЕЗ обрезки длинных нот. Переиспользуемо для lec-01..NN.
- **Приём (reusable):**
  1. **Slide-image source (fallback):** сперва `rendered/lec-NN.pdf` постранично
     (`page.get_pixmap(dpi=…)`, страница i = слайд i+1); если PDF нет —
     `rendered/snapshots/slide-*.png` (sorted). Это переживает и «без снапшотов»,
     и «без PDF».
  2. **Slide↔notes matching:** тем же ключом, что и deck-build — по префиксу
     `sNN` из `slides/sNN-*.md`, секция `## Speaker notes` (тот же regex, что
     `_helpers.load_notes`). Индекс слайда N ↔ `slides/sNN-*.md`.
  3. **Кириллица:** встроенный `helv`/base-14 у pymupdf НЕ содержит кириллицу —
     обязательно грузить TTF (`pymupdf.Font(fontfile=…)` + `page.insert_font`).
     Авто-дискавери по `/home/harness/.local/lo-sysroot/usr/share/fonts` и др.,
     кандидаты DejaVuSans/LiberationSans/NotoSans (regular+Bold).
  4. **Word-wrap по реальным метрикам:** `font.text_length(s, size)` для точного
     переноса (не эвристика по числу символов); есть hard-break для длинного
     одиночного слова/URL.
  5. **Overflow без обрезки:** если ноты не влезают в остаток страницы —
     continuation-страница с компактным повтором хедера («SNN · заметки
     (продолжение) · слайд N / M»), картинка не повторяется. Никакого клиппинга.
- **Проверка не-обрезки (reusable):** извлечь последние ~8 слов нот каждого слайда
  и убедиться, что они присутствуют в тексте PDF-страниц этого слайда
  (`page.get_text()` по диапазону страниц). На lec-04: 41/41 PASS.
- **Результат lec-04:** 41 слайд → 70 страниц (41 + 29 continuation), кириллица
  ок, s10 (355 слов, самые длинные) и s30 не обрезаны.
- **Severity:** N/A (техника). **Status:** working-pattern (reusable, аргумент —
  папка лекции: `python3 tools/presentation-build/notes_pages_pdf.py library/lectures/lec-NN`).
- **First seen in:** #170 lec-04 notes-pages deliverable (2026-08-30).

### [#170-4a] `notes_pages_pdf.py` — slide↔notes matching по числовому префиксу ломается на letter-suffix слайдах / gap-нумерации

- **Tool:** `tools/presentation-build/notes_pages_pdf.py` (`slide_md_by_index`) — reusable notes-pages PDF builder.
- **Symptom:** Для deck'ов с **letter-suffix слайдами** (s02a, s04a, s04b, s08a…) и/или **пропусками в нумерации** (нет s11 / s27) каждая нота PDF-страницы N привязывалась к `slides/sN*.md` по **числовому** значению префикса, а не по **позиции слайда в колоде**. Результат: PDF-страница показывает картинку слайда s16 (21-й по порядку), но снизу печатались ноты **s21** (числовой 21). Тихая рассинхронизация нот на большинстве страниц (визуально «ноты не про тот слайд»), без ошибки.
- **Root cause:** `slide_md_by_index` строила `{int(prefix): file}`. Для lec-04 это работало **случайно** (s01–s41 без пропусков и суффиксов → числовой == позиционный). Для lec-02 (35 слайдов, но 8 letter-variant + пропуски s11/s27) числовой ≠ позиционный.
- **Severity:** P1 (тихая рассинхронизация; deliverable выглядит готовым, но ноты не те).
- **Workaround / fix:** маппить PDF-страницу N (1-based) → **N-й md в natural-sorted порядке** (`s(\d+)([a-z]*)` → `(int, suffix)`, чтобы s02 < s02a < s03 < s04 < s04a). Это = фактический build-order колоды и backward-compatible с чисто числовыми деками. Исправлено в `slide_md_by_index` (issue #156-lec02 ref-pass, 2026-08-30). Проверка: извлечь последние ~8 слов нот каждого слайда и убедиться, что они присутствуют в тексте PDF (lec-02: 35/35 PASS после фикса; до фикса 8 dividers мисматчились).
- **Status:** fixed-in-tool (2026-08-30).
- **First seen in:** lec-02 refs + notes-PDF deliverable (2026-08-30).

### [#170-4b] `notes_pages_pdf.py` переписан по owner-спеке: ноты/заголовки из PPTX (не .md), позиционный матч, футер=номер страницы, continuation без «продолжение»

- **Tool:** `tools/presentation-build/notes_pages_pdf.py` — reusable notes-pages PDF builder (rewrite, supersedes матч-по-.md из [#170-4]/[#170-4a]).
- **Контекст:** owner review 5 пунктов — (1) убрать «lec-NN · SNN» из футера; (2) футер = номер страницы документа «N / total»; (3) хедер ~9-10pt muted = «‹полное название лекции› · ‹название слайда› · слайд N» (без «S01»-аббревиатур); (4) continuation-страницы БЕЗ слова «продолжение» (тот же хедер, продолжение нот, без картинки); (5) вернуть URL референсов в ноты.
- **Ключевые приёмы (reusable):**
  1. **Ноты — из `rendered/lec-NN.pptx`** через python-pptx `slide.notes_slide.notes_text_frame.text` в порядке презентации, НЕ из `slides/*.md`. Это даёт ПОЛНУЮ ноту: нарратив + inline `[N]` + блок «Источники:» с URL. Блок «Источники:» существует ТОЛЬКО в pptx (аппендится из ref-registry при build, не пишется обратно в .md) — поэтому notes-PDF из .md имели 0 URL. Решает пункт 5 разом.
  2. **Матч слайд↔нота — чисто позиционный:** PDF-страница i (из `lec-NN.pdf`) ↔ pptx-слайд i, оба в порядке презентации. Удалена вся хрупкая логика match-по-имени (`slide_md_by_index`/`_slide_natkey`/BUILD_ORDER-обёртки из [#171-1]) — decks с letter-suffix/непоследовательным build-order больше не рассинхронизируются в принципе.
  3. **Название лекции** — `deck.yaml` → `deck.title` (мини-скан YAML, без PyYAML-зависимости).
  4. **Название слайда** — title-placeholder слайда если есть, иначе верхний/крупнейший текстовый блок (первая строка); pure-number/tiny-глифы (большая «04» на обложке, page-маркеры) отфильтрованы.
  5. **Хедер: eliding ТОЛЬКО середины (slide-title).** При переполнении строки эллипсис ставится в slide-title, а `‹lecture title› ·` префикс и `· слайд N` суффикс сохраняются целиком. Иначе длинный lecture-title съедал «слайд N» (наблюдалось до фикса — «слайд N» пропадал за «…»).
  6. **Continuation-страница: тот же хедер, картинка не повторяется, слова «продолжение» НЕТ.** Пагинация считается в PASS-1 (без растеризации) → известно total_pages для футера; PASS-2 рендерит и штампует футер inline. (NB: держать список `pymupdf.Page` для отложенного футер-прохода НЕЛЬЗЯ — в этой сборке pymupdf у Page теряется живой doc-handle → `AttributeError: NoneType.is_pdf` в `insert_text`. Отсюда двухпроходная схема.)
- **Проверка (программная):** на 4 лекциях — URL>0 (lec-01/02/03/04 = 58/15/45/90), футер без «lec-NN·»/«·SNN» (0), «заметки (продолжение)»-лейблов 0, tail-нот присутствуют whitespace-insensitive 36/35/40/41 = 100% (длинные URL hard-wrap'ятся mid-token — при проверке коллапсить пробелы). ВНИМАНИЕ: слово «продолжение» встречается в самом тексте нот («правдоподобное продолжение», «продолжение обучения») — не путать со scaffold-лейблом; проверять именно «заметки (продолжение)»/«(продолжение».
- **Результат:** lec-01 36→54 стр, lec-02 35→57, lec-03 40→67, lec-04 41→72.
- **Severity:** N/A (техника). **Status:** working-pattern (rewrite, аргумент — папка лекции).
- **First seen in:** notes-PDF owner-spec rewrite (2026-08-30).

### [#170-3] Мелкие надстрочные [N]-ref-маркеры: post-hoc run-split через lxml (обход #54-2/#55-3 inline-runs)

- **Tool:** `python-pptx` (прямой build-скрипт, не MCP) — техника, а не баг.
- **Контекст:** нужно, чтобы [N]-ссылочные маркеры внутри готового body-текста
  были «существенно меньше» основного (≈50–55%), надстрочными и приглушёнными,
  БЕЗ переписывания сотни `text_box`/`text_runs`-вызовов с baked-in `[N]`.
  MCP `format_runs` для inline-эмфазиса ломает paragraph (#54-2), а строить
  каждый run вручную — неподъёмно при масштабе.
- **Приём (reusable):** после построения text_frame пройтись по `paragraphs`→
  `runs`, найти `[\d+(?:[,–-]\d+)*]` в тексте run'а, разрезать run: хвост-текст
  остаётся, а маркер вставляется НОВЫМ `<a:r>` сразу после через lxml
  (`etree.SubElement(anchor_r.getparent(), qn a:r)` + `anchor_r.addnext(new_r)`),
  с `rPr`:
  - `sz = round(base_pt * 0.52 * 100)` (сотые pt),
  - `baseline="30000"` (30% надстрочность),
  - `<a:solidFill><a:srgbClr val="1C7293"/>` (muted), `i="1"`.
  Клонировать шрифт (`latin/cs/ea typeface`) и цвет исходного run'а для
  «между-маркерного» текста. Проверено: 13.5pt-body → маркер `sz=702` (7.02pt)
  с `baseline=30000` рендерится LibreOffice→PDF корректно как мелкий надстрочный.
- **Где применено:** `library/lectures/lec-04/rendered/_helpers.py`
  (`shrink_refs_in_frame`, авто-вызов в `text_box`/`text_runs`; `gold_callout`/
  `teal_callout` покрыты транзитивно). Позволяет одной правкой хелпера
  «уменьшить все [N]» на 41-слайдовом deck.
- **Severity:** N/A (техника). **Status:** working-pattern.
- **First seen in:** #170 lec-04 v4.1 ref-completion (2026-08-30).

### [#157-1] Render toolchain (libreoffice/pdftoppm/rsvg) отсутствует в PATH — есть standalone bundle в /tmp/claude-999/local

- **Tool:** `libreoffice`/`soffice`, `pdftoppm`, `rsvg-convert`, `fc-list` (весь Visual Loop render toolchain).
- **Symptom:** `command -v libreoffice/soffice/pdftoppm/rsvg-convert/convert` → MISSING в стандартном PATH. `apt-get install` невозможен (нет passwordless sudo, dpkg lock). `LibreOffice.AppImage` в /tmp/claude-999 запускается в JuNest/proot и **консистентно падает на записи** любого output-файла: `SfxBaseModel::impl_store ... failed: 0xc10 (Error Area:Io Class:Write Code:16)` — независимо от outdir / UserInstallation / TMPDIR. Читает PPTX нормально, но не может записать PDF.
- **Root cause:** сборочная среда без системного office-стека; AppImage-proot слой не даёт writable output mount.
- **Severity:** P0 (блокирует Visual Loop — без PNG нет vision-inspection).
- **Workaround:** есть **standalone native toolchain** в `/tmp/claude-999/local/usr/bin/` (soffice, libreoffice, pdftoppm 24.02, rsvg-convert 2.58, fc-list). Работает при выставленном `LD_LIBRARY_PATH` с program-dir LibreOffice:
  ```bash
  export LOPROG=/tmp/claude-999/local/usr/lib/libreoffice/program
  export PATH="/tmp/claude-999/local/usr/bin:$PATH"
  export LD_LIBRARY_PATH="$LOPROG:/tmp/claude-999/local/usr/lib:/tmp/claude-999/local/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH"
  soffice --headless -env:UserInstallation=file:///tmp/claude-999/loprofile_lec03 \
    --convert-to pdf --outdir REND REND/lec-03.pptx        # PDF OK
  pdftoppm -r 150 -png REND/lec-03.pdf SNAP/p               # PNG OK
  ```
  Без `LOPROG` в LD_LIBRARY_PATH: `libreglo.so: cannot open shared object file`. Cyrillic рендерится (DejaVu доступен через /usr/share/fonts + local fc-cache). Inter/Arial отсутствуют → build использует fallback (DejaVu Sans через substitution) — визуально приемлемо.
- **Status:** active (workaround рабочий, проверен end-to-end 2026-08-09).
- **First seen in:** #157 (lec-03 полная пересборка, 2026-08-09).
- **Update (2026-09-23, sem-04 раунд 6):** `/tmp/claude-999/local` bundle из исходной записи больше
  не существует в окружении (проверено — путь отсутствует). Взамен есть постоянный (не в `/tmp`)
  portable-инсталл: `source /home/harness/.local/lo-portable-env.sh` даёт рабочие `soffice`
  (LibreOffice 26.2.4.2) и `pdftoppm` (poppler 24.02) без дополнительной возни с `LD_LIBRARY_PATH`
  вручную — скрипт уже выставляет `LO_HOME`/`LO_SYSROOT`/`LD_LIBRARY_PATH`/`FONTCONFIG_FILE`/`PATH`
  сам. Рабочая команда: `soffice --headless -env:UserInstallation=file:///tmp/<profile> --convert-to
  pdf --outdir <dir> <file>.pptx`, затем `pdftoppm -r 150 -png <file>.pdf <outdir>/<prefix>`. Ни
  один из двух путей (`/tmp/claude-999/local` или `/home/harness/.local/lo-portable-env.sh`)
  гарантированно не присутствует в любом произвольном окружении — перед использованием проверять
  `command -v soffice pdftoppm`, и если пусто — читать этот файл, а не считать инструмент
  отсутствующим совсем.

### [#sem01-render-2] python-pptx `Presentation.save()` re-serializes every XML part, including untouched slides — raw byte-diff is NOT a valid "unchanged" check

- **Tool:** `python-pptx` (`Presentation.save()`).
- **Symptom:** When a script opens a `.pptx`, edits ONE slide (e.g. replaces an
  image + adds a few text runs on slide 6 only), and saves — a raw `diff`/`cmp`
  of the extracted slide XML for every OTHER, untouched slide reports a byte
  difference. Also `_rels/*.xml.rels` files may show relationship entries
  reordered (same `Id`/`Target` pairs, different sequence in the file).
- **Root cause:** `python-pptx` re-serializes the entire OPC package tree on
  `save()` via lxml, which normalizes whitespace, attribute/namespace-prefix
  ordering, and XML declaration quoting (`'` vs `"`) for every part it touched
  in memory — which in practice is every part `Presentation()` parsed, not
  just the ones the script explicitly mutated. This is cosmetic
  re-serialization, not a content change: canonicalizing both XML trees
  (`lxml.etree.tostring(tree, method="c14n2")`) and comparing shows byte-for-byte
  semantic equality for every part the script didn't touch.
- **Severity:** P2 (verification-workflow gotcha, not a rendering bug — but can
  cause a false "I broke other slides" panic, or worse, a false-pass if you
  only trust `diff -q` in the other direction).
- **Workaround:** When asked to verify "only slide N changed, everything else
  byte-identical" after any python-pptx round-trip (open→edit→save), do NOT
  use raw `diff`/`cmp` on the extracted part XML. Instead: (a) extract text via
  `python-pptx` shape iteration and compare per-slide (catches real content
  drift), AND (b) canonicalize each XML part with
  `lxml.etree.tostring(etree.parse(path), method="c14n2")` and compare those
  byte strings (catches real structural/attribute drift while ignoring
  serializer-cosmetic reordering). Also diff the file list inside both zips
  (`find . -type f`) to confirm no parts were unexpectedly added/removed
  beyond the intended new media files.
- **Status:** active (by design in python-pptx/lxml; not fixable without
  avoiding python-pptx round-trips entirely, e.g. raw zip/XML surgery).
- **First seen in:** sem-01 slide-6 surgical edit (2026-08-08) — owner-provided
  final PPTX had to be edited on exactly one slide with all 19 others
  guaranteed untouched; naive `diff -q` on extracted slide XML falsely flagged
  all 19 other slides as changed.

### [#118-1] mmdc / mermaid-cli: missing Chrome browser dependency

- **Tool:** `mmdc` (mermaid-cli @mermaid-js/mermaid-cli)
- **Symptom:** «Error: Could not find Chrome (ver. 148.0.7778.97)» — puppeteer cannot launch headless Chrome
- **Root cause:** puppeteer-core dependency requires Chrome at `~/.cache/puppeteer/`; not installed in current env
- **Severity:** P2 (mermaid blocked; have python-pptx shapes alternative)
- **Workaround:** Build all diagrams via python-pptx primitive shapes (`add_shape` + `add_connector`) instead of mermaid PNG embed. This is actually closer to "diagrams as shapes" principle from `tools/presentation-build/README.md` §1.
- **Status:** active
- **First seen in:** #118 (lec-09 Phase 6, 2026-05-20)
- **Fork target:** Install Chrome OR use alternative renderer

### [#sem01-render-1] python-pptx: literal `\n` inside a single text run does not reliably line-break under LibreOffice PDF export

- **Tool:** `python-pptx` (direct script usage, not PowerPoint MCP) + LibreOffice headless PDF export (render toolchain).
- **Symptom:** A helper (`text_box`) that sets `r.text = "line one\nline two"` on a
  single run — intending a 2-line label inside a fixed-height box — did not render as
  2 wrapped lines in the LibreOffice-produced PDF/PNG. The label rendered effectively
  as one run and, depending on box sizing assumptions made for 2 lines, either got
  visually clipped or overlapped an adjacent shape positioned assuming the label was
  taller (2 lines) than it actually rendered.
- **Root cause:** python-pptx does not interpret `\n` inside `run.text` as an
  OOXML line-break (`<a:br/>`) — it is written as a literal character in `<a:t>`.
  Some renderers may collapse/ignore it; LibreOffice's behavior here was inconsistent
  enough to cause layout bugs when downstream code assumed a hard line break.
- **Severity:** P2 (silent layout bug — no error, just wrong-looking output; easy to
  miss without visual snapshot inspection).
- **Workaround:** Never rely on literal `\n` inside a single run for line breaks.
  Either (a) call `tf.add_paragraph()` once per intended line (proper OOXML paragraph
  break, renders reliably), or (b) avoid manual line breaks entirely and size the text
  box for natural word-wrap at the target font size (what we did — simpler when the
  label is short enough to auto-wrap acceptably).
- **Status:** active.
- **First seen in:** sem-01 seminar deck production (2026-08-06), s05 Deloitte stat-panel
  labels (iteration 2 → 3, see `library/seminars/sem-01/rendered/iteration-log.md`).

### [#sem03-render-1] `render-env.sh` `$HOME` override breaks `python-pptx` import (user-site-packages)

- **Tool:** bootstrapped render toolchain (`/tmp/claude-999/render-env.sh`) +
  `python-pptx` (installed under `~/.local/lib/python3.12/site-packages`, not a venv).
- **Symptom:** Sourcing `render-env.sh` and then running `python3 build_semNN.py`
  fails with `ModuleNotFoundError: No module named 'pptx'`, even though the exact
  same `python3` binary (`which python3` unchanged) successfully imports `pptx`
  when `render-env.sh` has NOT been sourced.
- **Root cause:** `render-env.sh` sets `export HOME="${RENDER_HOME:-/tmp/claude-999/loffice-home}"`
  (needed so LibreOffice's first-run profile bootstrap doesn't write into the real
  home directory). Python's default `sys.path` includes a user-site-packages entry
  derived from `$HOME` (`~/.local/lib/python3.X/site-packages`) — overriding `$HOME`
  silently drops the real user-site path from `sys.path`, so anything installed
  there (here: `python-pptx`, not a system/venv package) becomes unimportable.
  Confirmed via `python3 -c "import sys; print(sys.path)"` before/after sourcing —
  the user-site entry is present only when `$HOME` is unmodified.
- **Severity:** P1 (blocks the entire direct-python-pptx-build workflow if the
  build script is invoked after sourcing render-env.sh in the same shell).
- **Workaround:** Never source `render-env.sh` before running the `build_semNN.py` /
  `build_lecNN.py` script itself. Build the PPTX first with a plain `python3
  build_semNN.py` (normal `$HOME`, `pptx` importable) — only source
  `render-env.sh` (or better, let `pptx_to_png.sh` do it internally, which it
  already does) for the PDF/PNG conversion step. The two steps never need to
  share a shell environment; running them as two separate `Bash` tool calls
  (build, then convert) sidesteps the issue entirely and is what actually
  happened in sem-03 production once the error was diagnosed.
- **Status:** active.
- **First seen in:** sem-03 seminar deck production (2026-08-09), first
  `python3 build_sem03.py` attempt immediately after sourcing render-env.sh for
  toolchain verification (see `library/seminars/sem-03/rendered/iteration-log.md`).
- **Fork target:** low priority — workaround is a one-line process change (don't
  chain the two steps in one sourced shell). Could alternatively fix in
  `render-env.sh` by additionally exporting `PYTHONPATH` to include the real
  user-site-packages dir before overriding `$HOME`, but untested and not needed
  given the trivial workaround.
### [#153-1] libreoffice/pdftoppm/rsvg-convert not on default PATH — portable install exists under `/tmp/claude-999/local`

- **Tool:** `libreoffice` (headless PDF export), `pdftoppm` (PDF→PNG), `rsvg-convert` (SVG→PNG icon recolor)
- **Symptom:** `command -v libreoffice soffice pdftoppm rsvg-convert mmdc` all empty on a fresh harness session — none on default `$PATH`, and a naive `apt`/`find /usr` search finds nothing either, suggesting the tools are missing.
- **Root cause:** A portable/sandboxed install DOES exist, just not on `PATH` and not with its shared libs on `LD_LIBRARY_PATH`: binaries live at `/tmp/claude-999/local/usr/bin/{libreoffice,soffice,pdftoppm,rsvg-convert}`, and their `.so` dependencies (`libXinerama.so.1`, `libpoppler.so.134`, `libcairo.so.2`, `libreglo.so`, etc.) live under `/tmp/claude-999/local/usr/lib/x86_64-linux-gnu/` and `/tmp/claude-999/local/usr/lib/libreoffice/program/`. Running the binary without both exports fails with `error while loading shared libraries`.
- **Severity:** P1 (blocks the entire visual-loop Generate→Convert→Inspect step until diagnosed — cost ~15 min of exploration in Лекция 1 issue #153 polish session).
- **Workaround:** Export both before any visual-loop command:
  ```bash
  export PATH="/tmp/claude-999/local/usr/bin:$PATH"
  export LD_LIBRARY_PATH="/tmp/claude-999/local/usr/lib/libreoffice/program:/tmp/claude-999/local/usr/lib/x86_64-linux-gnu:/tmp/claude-999/local/usr/lib:$LD_LIBRARY_PATH"
  ```
  Verified working: `libreoffice --headless --convert-to pdf ...`, `pdftoppm -r 110 -png ...`, `rsvg-convert --version`. `mmdc` (mermaid-cli) was NOT found under this path in this session — still blocked, see [#118-1] python-pptx-shapes workaround.
- **Status:** active
- **First seen in:** #153 (Лекция 1 21-fix polish round, 2026-08-07)
- **Fork target:** N/A (environment quirk, not an MCP server bug) — worth adding these two `export` lines to a shared onboarding snippet/skill so future sessions don't re-discover this by trial and error.

### [#156-1] Custom `add_image()` helper (build_lecNN.py convention) — height-only call silently ignores `h`

- **Tool:** project-local convention, not upstream python-pptx or MCP — the `add_image(slide, path, x, y, w=None, h=None)` helper defined per-lecture in `library/lectures/lec-NN/rendered/build_lecNN.py` (first seen in `build_lec02.py`, likely copy-pasted across other lecture build scripts too — worth checking).
- **Symptom:** Calling `add_image(s, path, x=X, y=Y, h=H)` with **only** `h` set (no `w`) silently ignores `h` entirely and embeds the picture at its **native pixel size interpreted at 72dpi** (python-pptx default when the source PNG carries no DPI metadata — true for PNGs produced by `rsvg-convert`). A 900×700px PNG rendered at native size becomes 12.5"×9.72" — many times larger than a typical slide region — overflowing any containing box/motif silently (`add_picture()` doesn't error, it just places an oversized picture).
- **Root cause:** the helper's `if/elif/else` chain only had branches for `(w and h)` and `(w only)`; the final `else` branch (meant for "neither given, use native size intentionally") also caught the `(h only)` case because there was no dedicated `elif h is not None` branch.
  ```python
  # BUGGY (pre-#156):
  if w is not None and h is not None:
      add_picture(..., width=Inches(w), height=Inches(h))
  elif w is not None:
      add_picture(..., width=Inches(w))
  else:                              # <-- also matches h-only calls!
      add_picture(...)               # native size, h silently dropped
  ```
- **Severity:** P1 — silent, no exception raised; only visible on PNG inspection (caught during visual-loop iter-1 inspection on lec-02 s01, issue #156). Any prior height-only `add_image(...)` call in any lecture's build script may have this defect unnoticed if the image happened to already be close to native size, or the overflow wasn't checked at 150dpi.
- **Workaround / fix:** add the missing branch:
  ```python
  elif h is not None:
      slide.shapes.add_picture(str(path), Inches(x), Inches(y), height=Inches(h))
  ```
  Fixed directly in `library/lectures/lec-02/rendered/build_lec02.py` (issue #156). **Recommend auditing other `build_lecNN.py` files for the same copy-pasted helper** and applying the same fix, or better: promote a single shared helper module instead of per-lecture copies.
- **Audit result (2026-08-11):** confirmed via `grep -A20 "^def add_image"` across all `library/lectures/lec-*/rendered/build_lec*.py` — **13 of 14** lecture build scripts still carry the buggy version (lec-01, lec-04 through lec-13, lec-15, lec-17). Only lec-02 is fixed. None of these were in scope for issue #156; flagging for a future dedicated fix/backport pass.
- **Status:** active (fixed in lec-02's copy only; other 13 lectures' copies not yet checked/patched).
- **First seen in:** #156 (lec-02 polish pass, s01 hook redesign, 2026-08-11).

### [#170-1] LibreOffice PDF export `Io Class:Abort/NotExists` from a corrupted default profile — needs isolated UserInstallation

- **Tool:** portable LibreOffice headless (`--convert-to pdf`) in the Visual Loop.
- **Symptom:** After several successful conversions in one session, `soffice
  --headless --convert-to pdf --outdir snapshots lec-NN.pptx` starts failing with
  `Error: Please verify input parameters... (SfxBaseModel::impl_store ... failed:
  0x11b Io Class:Abort Code:27)` and later `0x302 Io Class:NotExists Code:2` — the
  PDF is never written, and `render.sh` silently produces no PNGs (exit swallowed).
  The pptx itself is valid (opens fine; `python-pptx` counts all slides).
- **Root cause:** the shared default LibreOffice user profile (under the overridden
  `$HOME=/tmp/claude-999`) gets into a locked/corrupted state across repeated
  headless invocations; the store step then aborts on the output path.
- **Severity:** P1 (blocks the entire generate→inspect loop until diagnosed; the
  silent-no-output failure mode makes it look like "nothing rendered").
- **Workaround:** pass a per-lecture isolated profile and a fresh scratch outdir on
  every convert:
  ```bash
  soffice --headless -env:UserInstallation=file:///tmp/claude-999/loprofile_lecNN \
    --convert-to pdf --outdir /tmp/claude-999/lecNN-snap lec-NN.pptx
  ```
  Then render pages with pymupdf. Codified in `/tmp/claude-999/lec04-build/render.sh`.
- **Related (image blank):** LibreOffice renders 8-bit **colormap/palette PNGs**
  (e.g. arXiv/blog og:image) as a **blank** picture even though `python-pptx`
  embeds them correctly. Convert acquired heroes to clean **RGB** and downsize
  (<200 KB) with Pillow before `add_picture` — fixes both the blank render and
  the `Io:Abort` (oversized 5 MB media pushed the store step over the edge).
- **Status:** active (workaround reliable, verified end-to-end 2026 lec-04 v3 render).
- **First seen in:** #170 (lec-04 SDLC re-spine, 37-slide render).

### [#170-2] Render script sets `HOME=/tmp/claude-999` for LibreOffice → drops user-site → pymupdf ImportError

- **Tool:** `render.sh` pipeline (portable `soffice` PDF export + `pymupdf` PDF→PNG).
- **Symptom:** After `export HOME=/tmp/claude-999` (needed so LibreOffice writes
  its profile into scratch, not real home), the subsequent `python3` step that
  uses `pymupdf` fails with `ModuleNotFoundError: No module named 'pymupdf'`,
  even though the same interpreter imports it fine without the `HOME` override.
- **Root cause:** same mechanism as [#sem03-render-1] — Python derives its
  user-site-packages path from `$HOME` (`~/.local/lib/python3.X/site-packages`);
  in this harness `pymupdf`/`python-pptx` live under the *account* dir
  `/home/harness/harness-control-data/accounts/256/claude-code-...
  /.local/lib/python3.12/site-packages`, which is dropped once `$HOME` is
  overridden.
- **Severity:** P1 (silent — the render.sh here swallowed the traceback and
  produced 0 PNGs, looking like "nothing rendered").
- **Workaround:** in `render.sh`, in addition to `HOME`, `export PYTHONPATH=`
  pointing at the account's real `.local/lib/python3.12/site-packages` before the
  pymupdf step. Do NOT chain `python3 build_lecNN.py` in the same `HOME`-overridden
  shell (build with plain `$HOME` first, then render). Codified in
  `library/lectures/lec-04/rendered/render.sh`.
- **Status:** active (workaround reliable, verified lec-04 v4 40-slide render 2026-08-30).
- **First seen in:** #170 (lec-04 v4 methodology-first render).

### [#172-1] EN re-render coupling: RU-keyed `NOTES_INLINE` anchors silently drop `[N]` refs on translated notes

- **Tool:** `build_lecNN.py` reference system (inline `[N]` injection into speaker notes) when re-used for a translated (EN) deck.
- **Symptom:** After translating speaker notes to EN (via `slides-en/`), the `NOTES_INLINE` dict keys are still Russian phrases (e.g. `("Трансформер", "[1]")`, `("границ", "[1] [2] [3]")`). The injector matches `phrase in note_body`; on EN notes those RU phrases never match, so the inline superscript `[N]` markers **silently vanish** — no error, notes just lose their citation anchors. The bottom numbered source list still renders (it's keyed on `SLIDE_REFS`, independent), so the divergence is easy to miss.
- **Root cause:** the anchor phrases are load-bearing content coupled to note language, but they live in the build script, not in the (translated) md. Duplicating the script for EN does not translate them.
- **Severity:** P2 (citations degrade, not a hard break). Must translate `NOTES_INLINE` keys to the EN phrase that actually appears in the EN note.
- **Workaround:** when producing `build_lecNN_en.py`, translate every `NOTES_INLINE` key alongside the visible strings. Confirmed for lec-01 (#172): 21 anchor phrases translated.
- **Also:** `notes_sources_block` detects the sources heading by literal `startswith("Источники:")` — must become `"Sources:"` for EN, and the EN notes md must use `Sources:` (not `Источники:`) as the in-note heading, or the numbered list won't attach.
- **First seen in:** #172 (bilingual production calibration, lec-01, 2026-08-30).

### [#172-2] Canonical portable-LibreOffice env wrapper on this host: `source /home/harness/.local/lo-portable-env.sh`

- **Tool:** portable LibreOffice + poppler render toolchain (headless PDF export + `pdftoppm`). Complements [#170-1] / earlier `/tmp/claude-999/local` note.
- **Symptom:** `libreoffice`/`soffice`/`pdftoppm` are absent from `PATH`; `soffice` fails with `libXinerama.so.1: cannot open shared object file`; there is no passwordless `sudo` to `apt-get install`.
- **Root cause:** a no-root portable install exists at `/home/harness/.local/{libreoffice-portable,lo-sysroot}` with its own env wrapper; nothing is on `PATH`/`LD_LIBRARY_PATH` by default.
- **Workaround:** `source /home/harness/.local/lo-portable-env.sh` in the same shell before any convert/raster — it exports `LD_LIBRARY_PATH` (Xinerama etc.), `FONTCONFIG_FILE`, and prepends `$LO_HOME/program` + `$LO_SYSROOT/usr/bin` (gives `soffice` 26.2 + `pdftoppm` 24.02) to `PATH`. Then combine with the [#170-1] isolated-`$HOME`/profile workaround for repeated converts.
- **First seen in:** #172 (lec-01 EN render, 2026-08-30).

### [#183-1] PyMuPDF SVG import ignores `<linearGradient>` — gradient fill renders BLACK

- **Tool:** `pymupdf` (`pymupdf.open("file.svg")` → `get_pixmap()`), used as SVG→PNG fallback when `rsvg-convert` is absent (lec-02 v2.0 batch-1 hero illustration).
- **Symptom:** a `<rect fill="url(#gradId)">` referencing a `<linearGradient>` in `<defs>` renders with a solid **black** fill (unresolved paint → default), silently: no warning, file converts "successfully". A deliberately muted background illustration came out as a heavy black block.
- **Root cause:** MuPDF's SVG parser has partial SVG support; gradient paints on shapes are not resolved.
- **Severity:** P2 (silent visual corruption; obvious on inspect).
- **Workaround:** use only solid `fill="#rrggbb"` (+ opacity) in SVGs destined for PyMuPDF rasterization; emulate gradients with stacked semi-transparent solids if needed. Text, paths, strokes, dash arrays render fine.
- **First seen in:** #183 (lec-02 v2.0 batch 1, s01 hero «чёрный ящик с трещинами», 2026-09-05).

### [#183-2] QuickChart v4 — annotation line `label` не рендерится

- **Tool:** QuickChart POST `/chart` (`"version": "4"`), плагин chartjs-plugin-annotation (`options.plugins.annotation.annotations.<id>`).
- **Symptom:** сама annotation-линия (`type: "line"`, `borderDash`, `borderColor`) рендерится корректно, но вложенный `label` (`{"enabled": true, "content": "...", ...}`) молча не появляется на PNG — ни ошибки, ни текста.
- **Root cause (предположительно):** в annotation-плагине v2 (Chart.js v4) синтаксис метки сменился с `enabled` на `display` + иная структура; QuickChart молча игнорирует нераспознанные ключи. Вариант с `display: true` не проверялся (обход оказался проще).
- **Severity:** P3 (косметика; линия работает).
- **Workaround:** накладывать подпись текстовым слоем python-pptx поверх вставленного PNG (lec-02 s25: «11 из 13 — ниже 50%» gold-текст на белом поле чарта).
- **First seen in:** #183 (lec-02 v2.0 batch 2, s25 NoLiMa chart, 2026-09-05).

### [#162-1] `add_image()` молча возвращает `None` при отсутствующем файле иконки — не рендерится, без ошибки

- **Tool:** `_helpers.py` `add_image()` (python-pptx build-скрипт), паттерн этого репозитория для recolored SVG→PNG иконок из `rendered/assets/icons/`.
- **Symptom:** слайд `s20e` (schema_matrix, Лекция 4) рендерился без иконки в заголовке колонки (а) — не было ни исключения, ни визуального placeholder'а, просто пусто. Обнаружено только vision-ревью (`presentation-critic`), не автоматической проверкой.
- **Root cause:** `assets/icons/file-stack-white.png` физически отсутствовал на диске (не был сгенерирован в исходном design-проходе); `add_image()` при `FileNotFoundError`/отсутствии пути тихо возвращает `None` вместо ошибки — вызывающий код не проверяет возврат.
- **Severity:** P2 (silent visual gap — не видно без vision-QA, легко пропустить при self-report designer'а).
- **Workaround:** генерация недостающей иконки на этом хосте без `rsvg-convert`/`ImageMagick`/`inkscape` (недоступны, `apt install` запрещён правами) — через `cairosvg` (pip), но ему нужен `libcairo.so.2`, которого нет в системном `LD_LIBRARY_PATH`. Рабочая команда: `LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu python3 -c "import cairosvg; cairosvg.svg2png(...)"` — та же sysroot-библиотека, что уже используется для LibreOffice headless (см. [#172-2]). Recolor через lucide SVG source + цветовая замена в тексте SVG перед рендером.
- **Long-term fix:** добавить sanity-check в `add_image()` (raise вместо silent `None`) или pre-build assertion «все referenced icon-файлы существуют» перед сборкой pptx — предотвратит повтор на будущих лекциях.
- **First seen in:** #162 (Лекция 4, s20e schema_matrix icon gap, 2026-09-19).

### [#render-bootstrap-1] Canonical no-root render toolchain, consolidated: `tools/presentation-build/{render-bootstrap.sh,render-env.sh,pptx_to_png.sh}`

- **Tool:** LibreOffice headless (PPTX→PDF) + `pdftoppm` (PDF→PNG) + `rsvg-convert`/ImageMagick `convert` (icon recolor/raster post-processing), no root/sudo available on this host.
- **Symptom / gap this closes:** [#172-2] already documented a working no-root LibreOffice+poppler install at `/home/harness/.local/{libreoffice-portable,lo-sysroot}` with a minimal sourceable wrapper (`/home/harness/.local/lo-portable-env.sh`) — but that wrapper does not cover `rsvg-convert`/ImageMagick (needed by the icon-recolor step of the visual-loop pipeline, §5 of this project's `tools/presentation-build/README.md`), and does not address the separate `$HOME`-override trap already logged in [#sem03-render-1] (overriding `$HOME` for an isolated LibreOffice profile silently breaks `python-pptx`/`pymupdf` imports, since those come from user-site-packages which is also `$HOME`-derived on this host, not a venv).
- **What was built (sem-04 production, 2026-09-20/21):** `render-bootstrap.sh` — idempotent, no-root setup script. Prefers the platform installer (`/opt/harness-control/scripts/install-libreoffice-portable.sh`) for the LibreOffice+poppler core (same install [#172-2] already documents) when present, and always builds `rsvg-convert`+ImageMagick `convert` itself via `apt-cache depends --recurse` + `apt-get download` + `dpkg-deb -x` flat-extraction into `/home/harness/.local/lo-sysroot` (98 packages, ~86MB, functionally verified: SVG→PNG and PNG resize both tested live). `render-env.sh` — single file to `source` that exports `PATH`/`LD_LIBRARY_PATH`/`FONTCONFIG_FILE` for the whole toolchain (superset of `lo-portable-env.sh`) *and* pre-empties the `$HOME`-override trap by capturing+re-exporting the real `PYTHONPATH` before anything else can touch `$HOME` — safe to source even before the toolchain is built (warns to stderr, doesn't fail the shell). `pptx_to_png.sh` — the common "PPTX → PNGs" case, sources `render-env.sh` internally and passes `soffice -env:UserInstallation=file://<fresh temp dir>` per invocation (avoids both the `$HOME` trap and the parallel-run profile-collision failure mode of earlier ad-hoc `$HOME`-override scripts).
- **Root cause (why 3 separate fixes converged into 1 toolchain):** LibreOffice/poppler had a working install+wrapper ([#172-2]), the `$HOME` trap had a documented workaround but no reusable fix ([#sem03-render-1] — "never source render-env.sh before running the build script" was a discipline rule, not a structural fix), and rsvg-convert/ImageMagick had no no-root install path documented anywhere. Each new lecture/seminar session was re-discovering pieces of this independently.
- **Severity:** P1 (blocks the entire render pipeline on a fresh worktree without this).
- **Workaround / usage:** `tools/presentation-build/render-bootstrap.sh` once per host (idempotent, `FORCE=1` to rebuild), then `source tools/presentation-build/render-env.sh` — but **only ever immediately before the PDF/PNG conversion step, never before running a `build_*.py` script itself** (sourcing first still breaks `python-pptx` imports in that same shell despite the `PYTHONPATH` re-export, because `$HOME` itself changes what `import pptx` resolves against before the export can help — keep `python3 build_*.py` and `source render-env.sh` as two separate shell invocations, per [#sem03-render-1]). For the common case, just call `tools/presentation-build/pptx_to_png.sh` directly instead of hand-rolling the convert step.
- **Status:** active, verified end-to-end on `library/seminars/sem-04/rendered/sem-04.pptx` (56-slide deck, full visual-loop + fix passes, 2026-09-21). Supersedes [#172-2] for any deck that also needs `rsvg-convert`/ImageMagick; [#172-2]'s `lo-portable-env.sh` remains valid standalone if only LibreOffice/poppler are needed.
- **First seen in:** #201 (Семинар 4 production, "Сборка кодинг-агента", 2026-09-20/21).

### [#201-1] python-pptx: literal `\n` inside one run's text does NOT center per-line under `align=CENTER` (LibreOffice render)

- **Tool:** `python-pptx` direct build (`text_box()`-style helper: one `add_textbox` + one run whose `.text` contains embedded `\n` characters), rendered via LibreOffice headless.
- **Symptom:** A 2-line label built as a single run (`r.text = "ответить\nв чате"`) with paragraph `alignment = PP_ALIGN.CENTER` renders with the first line roughly centered and every subsequent line visibly offset (usually shifted right relative to the first line's centering) — NOT independently centered per visual line. Same text/box built as *separate paragraphs* (one `tf.add_paragraph()` per line, each with its own `alignment = PP_ALIGN.CENTER`) renders correctly, every line centered independently. The identical single-run-with-`\n` pattern renders fine when `align=LEFT` — the bug is specific to `CENTER` (and presumably `RIGHT`) combined with an embedded `\n`.
- **Root cause:** not confirmed from source (LibreOffice's Impress text layout engine, not python-pptx itself — python-pptx just writes the literal `\n` character into the `<a:t>` run text). Working theory: OOXML does not define `\n` inside `<a:t>` as a real line break at all; what actually produces the visual break here is LibreOffice's own wrap/render behavior treating the embedded control character as a forced break within a *single* paragraph, and then computing the per-line CENTER offset against the wrong width basis (likely the full un-broken string's measured width, not each visual line's own width) — an artifact of forcing a break where OOXML expects none, not a real per-paragraph centering bug.
- **Severity:** P1 (silent, visually obvious only on inspection — easy to ship centered-looking-but-actually-broken option cards; affected 8+ slides across `library/seminars/sem-04` before caught).
- **Workaround:** never put a literal `\n` in one run's `.text` when the paragraph alignment is CENTER (or RIGHT) and word-wrap-independent centering per line matters. Build real separate paragraphs instead — split the string on `\n` yourself and call `tf.add_paragraph()` (or an equivalent multi-paragraph helper) once per line, each with its own `alignment`. A `multipara_box()`-style helper (paragraph list of `{text, size, color, align, ...}` dicts, one `tf.paragraphs[0]` for the first + `tf.add_paragraph()` for the rest) sidesteps this entirely and was the fix applied throughout `build_sem04.py`. LEFT-aligned multi-line single-run text boxes are unaffected and don't need this treatment.
- **Status:** active (LibreOffice rendering behavior, workaround is a straightforward paragraph-per-line discipline rule for any *centered* multi-line label).
- **First seen in:** #201 (Семинар 4 v2 production, 2026-09-21) — `option_row()` cards (s06/s10/s17/s24/s33/s40/s50/s58) and `cobuilding_map()` slot labels (s07/s08/s64) all showed the bug before being switched to `multipara_box()`.

### [#201-2] Line-count-based overflow estimate for monospace `terminal_card`/`code_card` helpers needs a ~15-18% height margin beyond the naive `size*line_spacing/72` calc

- **Tool:** custom `terminal_card()`/`code_card()` python-pptx helper (dark rounded-rect + monospace `multipara_box` body), not a bug in python-pptx or LibreOffice per se — a calibration note for any home-grown overflow-diagnostic helper built on top of them.
- **Symptom:** A naive per-line height estimate (`needed_h = n_lines * (size * line_spacing / 72) + n_lines * space_after`) compared against the box's available height with only a small fixed tolerance (`+0.1in`) under-predicted real overflow on several slides (`s14`, `s28`, `s36`, `s43`, `s53` in `library/seminars/sem-04`) — the diagnostic reported "fits" while the actual LibreOffice render visibly clipped the last 1-2 lines below the dark card's rounded-rect boundary (text fades onto the white background below the shape).
- **Root cause:** not fully isolated — plausibly the Consolas→fallback-monospace substitution LibreOffice performs on this host renders taller glyphs/line-height than the nominal point size implies, or `multipara_box`'s per-paragraph `space_after` compounds slightly differently than the flat `n_lines * space_after` approximation.
- **Severity:** P2 (diagnostic-calibration issue, not a rendering bug — but a diagnostic that under-reports overflow is worse than no diagnostic, since it creates false confidence).
- **Workaround:** inflate the estimated per-line height by a ~18% empirically-calibrated safety factor (`line_h = size * line_spacing * 1.18 / 72.0`) before comparing to available box height, and drop the flat `+0.1in` tolerance entirely (compare directly). This caught all 5 real overflows above. Caveat: at this stricter margin the diagnostic also produces some false positives on short/low-line-count cards with comfortable slack (visually confirmed fine on manual spot-check) — treat diagnostic warnings as a **candidate list to visually verify**, not an auto-fix trigger.
- **Status:** active (calibration heuristic, not a structural fix — a true fix would require measuring actual rendered glyph metrics, out of scope for a build-time Python helper with no font-metrics library).
- **First seen in:** #201 (Семинар 4 v2 production, 2026-09-21).

### [#211-2] То же, что `[#211-1]`, на моноширинных карточках: `terminal_card` меряет строку как 1,30 × кегль, LibreOffice рисует ≈1,57 × — последняя строка листинга уезжает ЗА коробку

- **Инструмент:** `library/seminars/sem-05/rendered/deck_kit.py`, приём `terminal_card` (он же путь `metrics.line_h(fs, 1.3)`); конвертация `tools/presentation-build/pptx_to_png.sh` (LibreOffice headless → `pdftoppm`).
- **Симптом.** На собранном `sem-05.pptx` два слайда рамки теряют нижние строки кодового блока — но **только на настоящем рендере**:
  - `n02` «Где мы остановились»: листинг на 12 строк, последняя — `.claude/ — нет вовсе: ни хука, ни скилла, ни субагента, ни настроенного сервера` — целиком выпадает НИЖЕ тёмной коробки и дорисовывается почти невидимым серым на белом фоне. Это та самая строка, которую `learning_goal` слайда называет точкой входа в занятие;
  - `n65` «Что появилось в репозитории»: листинг на 10 строк, последняя (`+ ## Хук защиты ветки ← и кого он НЕ останавливает`) обрезается нижней кромкой коробки.
- **Почему не ловится.** Три сторожа молчат одновременно: (1) сборка не даёт предупреждения — по её собственной мерке блок помещается; (2) `rendered/qa_preview.py` рисует предпросмотр СВОЕЙ меркой и показывает блок внутри коробки с запасом (сравните `rendered/preview/n02.png` с настоящим рендером той же страницы); (3) `ПЕРЕПОЛНЕНИЕ`/`ЗА КРАЕМ ПОЛОТНА` считаются от той же заниженной высоты строки. То есть «предупреждений нет» здесь не значит «текст на месте».
- **Корень, измеренный.** `terminal_card` берёт высоту строки как `M.line_h(fs, 1.3)` = `кегль × 1,30 / 72`. Замер по настоящему рендеру `n02` (110 dpi, 12 строк, кегль 11 pt, шаг между строками 0,236–0,245″) даёт **множитель ≈ 1,573**, то есть мерка занижена на **21%**. На 12 строках это 0,42″ — ровно полторы потерянные строки. Замер воспроизводится: PNG страницы, полосы текста по светлым пикселям внутри коробки, шаг между полосами.
- **Отношение к `[#211-1]` — это одна и та же поломка, найденная двумя сессиями независимо и с разных сторон.** `[#211-1]` (сессия кейса 5) называет МЕХАНИЗМ: `deck_kit.text_box` пишет `p.line_spacing` вещественным числом, а и LibreOffice, и PowerPoint понимают такое значение как долю собственной высоты строки шрифта, тогда как `metrics.line_h` считает его долей кегля. Эта запись называет СЛЕДСТВИЕ на моноширинных карточках и даёт второй, независимый замер той же величины: 1,573 / 1,30 = **+21%** против измеренных там 28,1 / 23,4 = **+19,7%**. Два замера разными способами на разных слайдах сошлись в пределах процента — значит величина настоящая, а не артефакт одного измерения. Чинить следует по `[#211-1]` (`p.line_spacing = Pt(size × spacing)`), а не подгонкой множителя в `terminal_card`: подгонка вылечила бы кодовые карточки и оставила все прочие приёмы.
- **Отношение к `[#201-2]`.** Тот же класс, но запас там назван «~15–18%», и этого **мало**: нужен ≥20%. Плюс `deck_kit.terminal_card` Семинара 5 не применяет вообще никакого запаса — рекомендация `[#201-2]` до этого рендерера не доехала.
- **Серьёзность:** P1. Содержание со слайда пропадает молча, и сторож подтверждает, что всё в порядке.
- **Починка — по `[#211-1]`, не здесь.** Правка пересобирает КАЖДЫЙ текстовый блок деки, не только кодовый, поэтому в круге 4 она принадлежит сквозному прогону рендерера, а не сессии одного раздела: несколько сессий правят эти файлы параллельно. Слайды рамки, которые после починки надо пересмотреть глазами: `n02` и `n65`.
- **Проверка после правки — только глазами по настоящему рендеру.** `qa_preview.py` этот дефект не показывает по построению, поэтому его «чисто» зачётом не является.
- **Статус:** ПОЧИНЕНО по `[#211-1]`, как и было предписано (сквозной прогон рендерера, круг 4, 2026-10-01) — множитель в `terminal_card` не трогали. Обе названные здесь карточки пересмотрены глазами на настоящем рендере: `n02` и `n65` (в сквозной нумерации — стр. 2 и 65), плюс все четыре страницы, на которых `check_tracks_pdf.py` ругался (45/50/51/66). Листинги лежат внутри коробок с запасом, последние строки на месте. Отдельно подтверждено, что `terminal_card` после правки честно ВЫРАСТАЕТ под свой листинг: проба на 44 строки не дала ни одного вываливания, упёрлась только в дно кегля (7,5 pt) и сказала об этом. Номер сменён с `#211-1` на `#211-2`: сессия кейса 5 заняла первый номер в своей ветке тем же дефектом, и при слиянии вышло бы две записи под одним идентификатором.
- **Впервые замечено:** #211 (Семинар 5, круг 4, 2026-10-01).

### [#201-3] Duplicate `def build_sNN` function bodies appeared in a build script mid-session, with an `Edit`-tool warning ("file had been modified on disk since you last read it … contains other changes not in your context") preceding the divergence

- **Tool:** direct file editing (`Write`/`Edit` tools) on `library/seminars/sem-04/rendered/build_sem04.py`, not an MCP server — recorded here because it's a toolchain-adjacent hazard for any long single-file build-script session.
- **Symptom:** After a sequence of `Write` (initial helpers) + multiple `Edit` (append-new-content) calls, the resulting file contained **two full definitions each** of `build_s01` through `build_s08` (~370 lines of duplicated/divergent code — different docstrings, different helper functions like `title_size_for`/`move_tag`/`_equipment_map` not defined anywhere else, different layout constants) sitting back-to-back in the file, with the second (later, structurally consistent with the rest of the file) copy being the one Python actually executes (later `def` wins). At least two of the `Edit` tool calls in the same session returned a result body containing the sentence "the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context" — timed close to when the divergence must have been introduced.
- **Root cause:** not confirmed. The warning text itself implies a write to the same file path from outside this session's own tool-call stream (a concurrent process, a stale/leftover write from a previous attempt at the same task per the task's own framing that "a previous attempt failed", or a harness-level autosave/checkpoint mechanism) — normal sequential `Write`-then-`Edit`-then-`Edit` calls from a single session should not by themselves produce two divergent copies of the same function names.
- **Severity:** P1 (silent — the duplicated code was inert dead code since Python's later definition wins, so the render was NOT visually affected, but the file was confusing/bloated and the root cause is a real integrity concern for any session editing a large single file over many tool calls).
- **Workaround:** periodically run `grep -n "^def " file.py | awk -F'[( ]' '{print $2}' | sort | uniq -c | sort -rn | awk '$1>1'` to detect duplicate top-level function definitions in a long-lived build script; if found, diff the two copies to confirm the later one is what's live (matches actual render output), then delete the earlier dead copy (`sed -i 'STARTLINE,ENDLINEd' file.py`) and re-verify with `ast.parse` + a full rebuild+re-render to confirm no visual change.
- **Status:** active / unresolved root cause — documented as an observed hazard, not a fix. If this recurs, worth escalating: check whether this harness runs any autosave/background-checkpoint process against files a session is actively editing, and whether a "previous failed attempt" session's process can outlive its own termination and keep writing to files in the same working directory.
- **First seen in:** #201 (Семинар 4 v2 production, 2026-09-21), discovered via visual inspection of `s14`'s rendered PNG not matching a code review of `build_s14`'s apparent source (an earlier, dead-code copy was being read by mistake during investigation before the duplication itself was noticed).

### [#201-6] `grep -E`/`grep -P` `\b` word-boundary is unreliable on Cyrillic text under the default `en_US.UTF-8` locale — false positives inside Cyrillic words

- **Tool:** `grep -E`/`grep -o -E` (GNU grep, not an MCP server) — recorded here because it's the exact anti-pattern verification tool `CLAUDE.md`'s Pre-USER-GATE Walkthrough Rule and this project's own designer-extras grep discipline (`\b[0-9]+\s*мин(ут)?\b`, `методическ\w*`, etc.) prescribe for slide QA, so a false-positive here can produce a false "found a violation" (or, more dangerously, a false-negative masking a real one) on every future deck.
- **Symptom:** Running `grep -noE '\bмин\b'` against a line containing only the Cyrillic word «минут» (not the free-standing word «мин») reports a match — `\b` is firing *inside* a single Cyrillic word, between "мин" and "ут", where no real word boundary exists. Same command run against ASCII text (e.g. `grep -noE '\bmin\b'` on "minute") behaves correctly (no match). Reproduced live on `library/seminars/sem-04/rendered/build_sem04.py`'s own extracted visible-text (`s06`'s body contains «пятнадцать минут» and `\bмин\b` — part of a combined anti-pattern alternation copied from this project's own established grep pattern for timing markers — flagged it as a hit).
- **Root cause:** under `LANG=en_US.UTF-8` / `LC_CTYPE=en_US.UTF-8` (this host's default, confirmed via `locale`), GNU grep's regex engine does not reliably classify multi-byte Cyrillic letters as "word" characters (`\w`) for the purposes of `\b` boundary computation — `\b` ends up firing at some position inside the multi-byte sequence rather than only at a true word/non-word transition. A locale with native Cyrillic collation (e.g. `ru_RU.UTF-8`) was not tested here and may behave correctly; this host does not have one installed by default.
- **Severity:** P1 for any QA step that trusts a bare `grep -E '\bPATTERN\b'` result on Cyrillic content without independent verification — a **false positive** wastes investigation time (as it did here, briefly), but the structurally scarier failure mode is a **false negative**: a real short Cyrillic word sitting mid-string next to other Cyrillic characters could fail to be flagged if the boundary math happens to land wrong in the other direction. Not verified which direction is more common; treat both as possible.
- **Workaround:** for any Cyrillic-content anti-pattern grep that matters (timing markers, methodology-comment markers, LO-code markers, etc.), do NOT rely on bare `grep -E '\bPATTERN\b'`. Instead verify with Python's `re` module (`re.findall(r'\bPATTERN\b', text)`), which correctly classifies Cyrillic as word characters regardless of the shell locale (Python's `re` Unicode-mode word-char classification is locale-independent). On `library/seminars/sem-04/rendered/build_sem04.py`'s extracted visible text, `grep -E` flagged 12 lines as containing `мин\b`/other anti-patterns; re-checking the identical alternation with `python3 -c "import re; ..."` against the same text returned **0** genuine hits for all 10 checked patterns (all 12 `grep` hits were this false-positive class, not real timing/methodology leaks). If `grep` must be used standalone (no Python available), prefer a byte-safe substitute check instead of `\b`, e.g. anchor on an explicit non-letter delimiter set (`(^|[^а-яёА-ЯЁ])мин([^а-яёА-ЯЁ]|$)`) rather than `\b`.
- **Сведено с `[#225-7]` (2026-10-10).** Та запись замеряла то же место и получила симптом ПРОТИВОПОЛОЖНЫЙ — `command grep -P '\bроль\b'` даёт **ноль** там, где совпадения есть. Противоречия нет: корень один — буквы классифицируются по байтам, а не по Unicode, — и симптом зависит от того, где в шаблоне стоит граница. Внутри слова `\b` срабатывает лишнее (эта запись), на краю строки не срабатывает вовсе (`[#225-7]`). Разошлись и инструменты: в сентябре `grep` здесь был GNU grep, в октябре это функция-обёртка над `ugrep`, и она на `\b` по кириллице отвечает верно. Общий вывод обеих записей один: мерить Python `re` с якорями по обе стороны, а результату `-P` по кириллице не верить ни в какую сторону.
- **Status:** active (upstream grep/locale behavior, not fixable from this project; workaround is a tooling-choice discipline rule).
- **First seen in:** #201 (Семинар 4 v4 production, full 49-slide rebuild after раскол на два семинара, 2026-09-22) — caught while running this project's own standard designer-extras anti-pattern grep against the rebuilt deck's extracted visible text.

### [#212-1] `render.sh`'s `timeout 260` silently kills the LibreOffice pptx→pdf conversion on a large deck — zero PNG, zero error text

- **Tool:** render-toolchain (`library/lectures/lec-05/rendered/render.sh` → `soffice --headless --convert-to pdf`), not an MCP server.
- **Symptom:** `./render.sh` exits **0**, prints nothing, and leaves `snapshots/` empty. The stale `lec-05.pdf` from a previous build stays in place with its old timestamp, so a casual `ls` looks like the render "worked" while the PDF is actually the PREVIOUS deck. The only live evidence is a `[soffice.bin] <defunct>` zombie and a `.~lock.lec-05.pdf#` left in `/tmp/claude-999/lec05-snap/`. Reproduced twice on the rebuilt 56-slide Лекция 5 deck (5.0 MB pptx, heavy `schema_matrix` slides with monospace artefact boxes).
- **Root cause:** `render.sh` wraps soffice in `timeout 260`. On this host that deck needs longer than 260 s of wall time (the killed runs had only ~94 s of CPU each — soffice spends most of the wall time blocked, so CPU time badly under-reports how long it needs). `timeout` kills soffice before it writes the PDF; the subsequent `python3 … pymupdf` step then opens nothing, and because the final `cp` targets a file that already exists, nothing in the script fails loudly. `set -e` does not help: every step "succeeded".
- **Severity:** P1 — a silent no-op render is worse than a crash, because the next step (visual inspection, pre-gate walkthrough) is then performed against the PREVIOUS deck's snapshots/PDF and reports them as current.
- **Workaround:** raise the budget (done for lec-05: `timeout 260` → `timeout 900`) **and** verify the render by artefact rather than by exit code — `ls snapshots/*.png | wc -l` must equal the deck's slide count, and `lec-05.pdf`'s mtime must be newer than `lec-05.pptx`'s. Treat "exit 0" from `render.sh` as meaningless on its own.
- **Status:** active (mitigated for lec-05 only — every other `render*.sh` in the repo still carries its own hard-coded timeout and the same silent-failure shape).
- **First seen in:** #212 (Лекция 5, пересборка раскладки 69 → 56 слайдов, 2026-09-28).

### [#212-2] Two concurrent `soffice --convert-to` runs sharing one `-env:UserInstallation` profile deadlock — the second never starts, the first goes into uninterruptible sleep

- **Tool:** render-toolchain (`soffice --headless -env:UserInstallation=file:///tmp/…/loprofile_lec05`).
- **Symptom:** After a first conversion appeared hung, a second `soffice` was launched against the **same** `UserInstallation` path while the first was still alive. Neither produced output: the first moved to state `Dl` (uninterruptible sleep) and stopped accumulating CPU, the second sat at 0:00 forever. `pkill -f soffice` did not clear the first — it had to be killed by PID with `-9`. Deleting the profile directory out from under a live instance (`rm -rf loprofile_lec05`) makes the stuck state worse, not better.
- **Root cause:** a LibreOffice user profile is single-instance by design; a second process pointed at the same profile tries to hand its command to the first over the existing connection instead of converting anything itself.
- **Severity:** P2 — self-inflicted, but easy to inflict precisely when a render looks stuck and the reflex is "just run it again".
- **Workaround:** never launch a second conversion while `pgrep -f soffice.bin` returns anything. Before retrying: kill by PID with `-9`, confirm `pgrep` is empty (a `<defunct>` zombie is harmless and can be ignored), THEN `rm -rf` both the outdir and the profile dir, and only then re-run. If two renders genuinely must overlap, give each its own `-env:UserInstallation` path.
- **Status:** active (upstream LibreOffice behavior; discipline rule, not a fix).
- **First seen in:** #212 (Лекция 5, пересборка раскладки, 2026-09-28) — while investigating [#212-1].

### [#212-3] `render_chunked.sh` returns exit 0 while leaving `lec-05.pptx` stale — a successful-looking render that rendered nothing

- **Symptom:** after editing a slide builder, `bash render_chunked.sh` completed with `exit=0` and no error output, but `lec-05.pptx` kept its previous mtime and still contained the pre-edit text. An independent check of the built file (not of the script's exit code) found the old wording still on slides 45 and 49.
- **Why it matters:** this is the second failure mode in the same session where a render tool reports success without producing output (see [#212-1]). The dangerous part is not the failure — it is that every downstream check passes: the deck opens, the slide count is right, the notes are correct, and only the specific edited string is missing. A visual sweep of a *sample* of slides will not catch it.
- **Root cause:** not fully established. The chunked path builds per-chunk pptx files and merges them; on this run the merge step appears to have reused an existing artifact rather than the freshly built chunks. Not reproduced deterministically.
- **Severity:** P1 — silently ships a stale deck under a green exit code.
- **Workaround:** after any builder edit, rebuild with `python3 build_lec05.py` directly (it prints `saved … — N slides` and updates mtime), then convert to PDF. Do not trust the chunked wrapper's exit code alone. **Verification rule: check the built `.pptx` for the string you just changed, not the script's exit status** — `python3 -c "from pptx import Presentation; ..."` over the visible layer costs seconds and is the only check that actually falsifies this failure.
- **Status:** active.
- **First seen in:** #212 (Лекция 5, замена англицизмов на дивайдере управления, 2026-09-28) — found by the orchestrator while verifying a subagent's work against the built file.

### [#212-3b] Сборка молча не состоялась, а `render.sh` отрисовал предыдущую деку — тот же стоялый артефакт, другой триггер

- **Когда:** issue #212, правка Разделов 6–7 Лекции 5, 2026-10-01.
- **Что произошло:** команда вида `cd <lec-05> && python3 build_lec05.py && cd rendered && ./render.sh 50 54` выполнялась из оболочки, которая сбрасывает рабочий каталог между вызовами. `build_lec05.py` лежит в `rendered/`, поэтому сборка упала с `can't open file`, а следующая за ней отрисовка отработала штатно и выдала пять строк `rendered slide N` — по СТАРОМУ `lec-05.pptx`. Правка ячейки таблицы «отсутствовала» на снимке, хотя в исходнике была.
- **Почему попадается:** признак успеха снова взят не из артефакта. Все пять `rendered slide N` настоящие, PDF настоящий, число страниц верное — неверен только возраст входа. Это тот же класс, что `[#212-3]`, но ломается не рендер, а сборка ПЕРЕД ним, поэтому «проверил, что render.sh отработал» здесь не спасает.
- **Обход:** запускать сборку и отрисовку РАЗНЫМИ вызовами, каждый с явным абсолютным `cd` в `rendered/`, и сверять `ls -la --time-style=+%H:%M:%S lec-05.pptx` ПОСЛЕ сборки и ДО отрисовки. Если `mtime` не изменился — сборка не состоялась, что бы ни печатала следующая команда.

### [#212-4] `render.sh` hard-codes ONE shared LibreOffice profile, so N parallel sessions in the same worktree collide by construction — and `[#212-2]`'s "wait for pgrep to clear" workaround does not apply

- **Tool:** render-toolchain (`library/lectures/lec-05/rendered/render.sh`, the literal `-env:UserInstallation=file:///tmp/claude-999/loprofile_lec05`).
- **Symptom:** during the owner-review fix-out (six parallel sessions, one shared worktree, one shared `lec-05.pptx`), `bash render.sh` exited **2** with no output and left `lec-05.pdf` with an mtime OLDER than `lec-05.pptx`. `ps` showed **three** concurrent `timeout 900 … soffice --convert-to pdf` invocations, all pointed at the same `loprofile_lec05` and the same input file, launched by different sessions.
- **Why this is not just [#212-2]:** that entry treats the collision as self-inflicted ("the reflex is just run it again") and prescribes "never launch a second conversion while `pgrep -f soffice.bin` returns anything". With several sessions rendering the same deck on their own schedule, `pgrep` is essentially never empty, so the prescribed wait never terminates — and the profile is not a thing the caller chooses, it is baked into the script. The collision is structural, not a discipline failure.
- **Severity:** P1 — combined with [#212-1]/[#212-3] it means a parallel session can visually "verify" its slides against a PDF produced by, and for, somebody else's build.
- **Workaround (used in #212 Раздел 7):** do not render the shared deck at all for a per-section visual check. Build a throwaway pptx containing only the section's own builders (slide layout does not depend on slide position, so the check is still valid), convert it with a **private** `-env:UserInstallation` path into a **private** outdir, and assert the string you just changed is present in the produced PDF's text. Cost is seconds instead of the full deck's minutes, and it cannot be disturbed by, or disturb, a concurrent session.
- **Proper fix (not done here):** give `render.sh` a per-invocation profile and outdir (e.g. suffix by `$$` or by session id) so overlap is safe by default — the one-line change [#212-2] already names as the escape hatch but the script never took.
- **Дополнение (правка P0 по фактчеку, 2026-09-30):** приватный рендер по этому рецепту падает, если скопировать
  только строку `soffice`. Бинарник нуждается в `export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH`
  (её ставит `render.sh`, и только поэтому общий рендер работает). Без неё `oosplash` умирает на
  `libXinerama.so.1: cannot open shared object file`, PDF не создаётся вовсе, а сообщение уходит в `2>&1`,
  который в рецепте обычно погашен в `/dev/null` — то есть отказ выглядит как «конвертация прошла, файла нет».
  Заодно ставить `HOME` в свой каталог: профиль пишется относительно него.
- **Дополнение 2 (правка по student-roast, 2026-09-30):** в рецепте приватного рендера выше команда названа
  `soffice` — но такого исполняемого файла **нет в `PATH`**: `render.sh` вызывает его по полному пути
  `/home/harness/.local/libreoffice-portable/program/soffice`. Скопировав рецепт дословно, получаешь
  `timeout: failed to run command 'soffice': No such file or directory` и **exit 2 без единого слова о причине** —
  то есть отказ выглядит как очередная неудачная конвертация, а не как опечатка в рецепте. Полный рабочий вызов:
  ```bash
  export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
  export HOME=/tmp/<свой-каталог>
  timeout 600 /home/harness/.local/libreoffice-portable/program/soffice --headless \
    -env:UserInstallation=file:///tmp/<свой-каталог>/loprofile \
    --convert-to pdf --outdir /tmp/<свой-каталог> /tmp/<свой-каталог>/subset.pptx
  ```
  И следом — **вторая ловушка того же рецепта**: `export HOME=<свой-каталог>` уводит интерпретатор от
  `~/.local/lib/python3.12/site-packages`, поэтому `import pymupdf` в том же вызове падает с `ModuleNotFoundError`,
  хотя модуль установлен. Шаг PDF→PNG надо выполнять **отдельной командой, без подменённого `HOME`**.
- **Дополнение 3 (там же):** `gen_charts.py` не запускается из коробки — `matplotlib` в системном python3
  отсутствует, а `pip install` блокирован PEP 668. Рабочая установка:
  `python3 -m pip install --user --break-system-packages matplotlib`.
- **Дополнение 4 (там же):** при одновременной правке одного билдера двумя сессиями чтение файла может попасть
  в середину чужой записи: `python3 build_lec05.py` упал с `NameError: name 'text_runs' is not defined` в
  `slides_band5.py`, хотя импорт в файле был — через полминуты та же сборка прошла без изменений с моей стороны.
  Вывод тот же, что у всей этой группы записей: **единственная честная проверка — перечитать собранный
  `.pptx`**, а не доверять ни коду возврата, ни одной неудачной сборке.
- **Status:** active.
- **First seen in:** #212 (Лекция 5, правка по owner-review 2026-09-30, Раздел 7 — six sections revised in parallel in one worktree).

### [#212-4b] Параллельные сессии, конвертирующие одну деку, отъедают друг у друга LibreOffice: полный рендер не укладывается в разумное время

> Тот же корень, что у `[#212-4]` выше: обе записи заведены параллельными сессиями независимо и в один и тот же момент, поэтому и номер совпал. `[#212-4]` описывает общий профиль, эта — конкуренцию за процесс. Чинится одним фиксом (см. ниже).

- **Tool:** render-toolchain (`library/lectures/lec-05/rendered/render.sh` → `soffice --headless --convert-to pdf`), не MCP-сервер.
- **Симптом:** при правке Раздела 0 по owner-review 2026-09-30 полная конвертация 54-слайдовой деки не завершилась за ~7 минут; в процессах висели ДВА одновременных `soffice --convert-to` от разных сессий (`loprofile_lec05` и `r2design-loprofile`), у одного — `[soffice.bin] <defunct>`. Профили разные, то есть это НЕ дедлок из [#212-2], а обычная конкуренция за ресурсы: каждая сессия конвертирует всю деку целиком, хотя правит 5-6 слайдов.
- **Severity:** P2 — не портит результат, но делает цикл «посмотреть глазами» неприменимым при параллельной работе шести сессий над одной декой.
- **Workaround (проверен):** собирать подмножество СВОИХ слайдов отдельной декой и конвертировать её — секунды вместо минут, и нет конкуренции. Глобальная нумерация страниц сохраняется, если передать полный `total`:
  ```python
  p = setup_pres()
  for fn in B.ORDER[:5]: fn(p)
  for i, sl in enumerate(p.slides, start=1): page_number(sl, i, len(B.ORDER))
  ```
  Конвертировать в СВОЙ каталог и со СВОИМ `-env:UserInstallation` (иначе [#212-2]).
- **Сопутствующие грабли:** проверка готовности вида `until [ -f out/s5.png ]` срабатывает мгновенно на файле от ПРЕДЫДУЩЕГО прогона, если `rm -rf` каталога происходит внутри того же фонового задания. Ждать завершения самого задания либо сверять mtime, а не факт существования файла. Это тот же класс ошибки, что [#212-1]/[#212-3]: признак успеха взят не из артефакта.
- **Status:** active.
- **First seen in:** #212 (Лекция 5, пересборка Раздела 0 по замечаниям владельца, 2026-09-30).

### [#212-7] `render.sh` отдал exit 0 и ПУСТОЙ PDF: параллельная сборка переписала `lec-05.pptx` прямо во время конвертации

- **Tool:** render-toolchain (`library/lectures/lec-05/rendered/render.sh` → `soffice --convert-to pdf`), не MCP-сервер.
- **Симптом:** `bash render.sh 44 … 50` завершился успешно, честно напечатал `rendered slide 44 … 50` и `PDF copied`, но **все 54 страницы PDF оказались пустыми** (`page.get_text()` = 0 символов на каждой), а все PNG вышли одинакового размера 9211 байт — белые листы. Размер PDF упал с 6,67 МБ до 2,69 МБ. Ни одной строки ошибки.
- **Как поймано:** сравнением времён — у `lec-05.pptx` mtime оказался **позже**, чем у `lec-05.pdf`. То есть соседняя сессия запустила `build_lec05.py` и переписала входной файл в тот момент, когда LibreOffice его читал. Проверка «PNG свежее pptx» этого не ловит: PNG действительно свежие, они просто пустые.
- **Чем отличается от соседей:** [#212-1] — таймаут, [#212-3] — стоялый артефакт при зелёном коде, [#212-4] — общий профиль LibreOffice, [#212-4b] — конкуренция за ресурсы. Здесь новое именно то, что **портится ВХОД, а не выход**: файл валиден, конвертация проходит до конца, на выходе структурно корректный PDF нужного числа страниц — и он пустой. Это худший вид отказа: все счётчики сходятся.
- **Severity:** P1 — визуальная проверка по такому PDF показывает белые листы, и легко принять это за поломку своей правки вместо поломки рендера.
- **Workaround (проверен в Разделе 6):** не конвертировать общий `lec-05.pptx` вообще. Собрать подмножество СВОИХ слайдов в **приватный** файл вне репозитория, конвертировать его с **приватным** `-env:UserInstallation` в **приватный** outdir. Тогда вход не может быть переписан чужой сборкой:
  ```python
  from _helpers import setup_pres, page_number
  import build_lec05 as B
  names = [f.__name__ for f in B.ORDER]
  mine = ["s44", "s45", "s45a", "s45b", "s46", "s47", "s48"]
  p = setup_pres()
  for sid in mine:
      B.ORDER[names.index(sid)](p)
  for i, sid in enumerate(mine):            # глобальная нумерация сохраняется
      page_number(p.slides[i], names.index(sid) + 1, len(names))
  p.save("/tmp/r6-render/r6-subset.pptx")
  ```
  Семь слайдов конвертируются за секунды против минут на полной деке.
- **Обязательная проверка после ЛЮБОГО рендера:** `len(doc[i].get_text().strip()) > 0` хотя бы на одной своей странице. Код возврата, наличие PNG и их свежесть — все три признака в этом отказе ложно-положительные.
- **Статус:** активна.
- **Впервые встречено:** #212 (Лекция 5, правка Раздела 6 по owner-review 2026-09-30, шесть сессий в одном worktree).

### [#212-5] Сторож переполнения в `slides_band6.py` не видит примитивы, рисующие МИМО текстовых блоков — фигура молча уезжает за полосу карточки

- **Инструмент:** render-toolchain (`library/lectures/lec-05/rendered/slides_band6.py`, функции `_check` / `md_box` / `mono_box`), не MCP-сервер.
- **Симптом:** на слайде практики третья мини-схема (полоса собственного разброса модели с отметкой порога) отрисовалась ВНЕ своей полосы: сама полоса видна, а обе подписи к ней — «собственный разброс системы» и «порог — внутри него» — оказались за нижней границей и в PDF не попали. Сборка при этом прошла молча: `b6.WARN` пуст. Тот же класс ошибки во втором месте — подпись под рядом иконок легла ПОВЕРХ второго ряда иконок и читалась сквозь них.
- **Причина:** `_check` вызывается только из `md_box` и `mono_box`. Прямые вызовы `text_box`, `tiny`, `icon`, `filled_rect`, `connector`, `circle` никакой проверки не проходят — у них нет ни расчёта нужной высоты, ни сверки с `_BAND[1]`. Поэтому высота полосы, заданная в `C.band(...)` на глаз, проверяется только для текста в коробке, а нарисованные рядом схемы могут вылезать сколько угодно. Ни `WARN`, ни исключение не срабатывают, и `python3 build_lec05.py` печатает обычное `saved … — N slides`.
- **Severity:** P1 — визуальный дефект, который не ловится ни одной автоматической проверкой в цепочке: сборка зелёная, число слайдов верное, заметки на месте, текстовая сверка исходника с собранным `.pptx` (совпадение ключевых слов) тоже зелёная, потому что подписи В СЛАЙДЕ ЕСТЬ — они просто нарисованы за границей видимой области. Найти можно только глазами на PNG.
- **Workaround:** после любой правки слайда, где рядом с текстом рисуются схемы, считать нижнюю границу руками: последний рисуемый элемент не должен выходить за `y + h` полосы, где `h` — то, что передали в `C.band(...)`. Практически: рендерить страницу в PNG и смотреть. Пустой `WARN` — НЕ доказательство, что всё поместилось; он доказывает только, что поместился текст в коробках.
- **Возможное исправление (не сделано):** прогонять через `_check` и остальные примитивы либо добавить в `Cursor.band` финальную сверку «самый нижний нарисованный y против границы полосы». Требует трогать общий для двенадцати практик файл, поэтому отложено.
- **Status:** active.
- **First seen in:** #212 (Лекция 5, перестройка практик Раздела 5 по правилу Р8 владельца, 2026-09-30).

### [#212-6] Оценка высоты текста в `slides_band6.py` откалибрована под 10,5 pt — на большем кегле `_check` молчит, а текст вылезает

- **Инструмент:** render-toolchain (`library/lectures/lec-05/rendered/slides_band6.py`, `est_lines` / `est_h` / `_check`), не MCP-сервер.
- **Симптом:** при перестройке практики Раздела 2 по правилу Р8 из карточки убраны блоки «артефакт» и «критерий», освободившееся место отдано кеглю — текст слоёв поднят с 9,5 до 11 pt. Текст верхнего слоя вылез за нижнюю границу своей коробки («часть урока.» оказалась поверх соседнего слоя), при этом `b6.WARN` был пуст и сборка прошла молча.
- **Причина:** `est_lines` делит длину строки на константу `122/size` (для жирного `114/size`). Комментарий в самом файле честно говорит, что она «калибрована на первом прогоне этой же полосы (150 dpi, DejaVu Sans): ~120 символов на дюйм ширины **при 10,5 pt**». Реальная плотность в LibreOffice ближе к ~104 символам на дюйм, и расхождение растёт с кеглем и с сужением колонки. То есть `_check` отработал — просто его оценка оказалась ниже факта, и переполнение не попало в `WARN`.
- **Отличие от [#212-5]:** там примитив вообще не проходит через `_check`; здесь проходит, но получает заниженную оценку. Лечится по-разному, поэтому записано отдельно.
- **Severity:** P2 — ловится глазами на PNG за один прогон, но именно правило Р8 (убрать блоки, отдать место кеглю) систематически выводит карточки практик в эту зону.
- **Workaround (проверен):** считать по ~104 символа на дюйм ширины вместо 122 при кегле выше 10,5 pt, то есть закладывать примерно +15-20% высоты против того, что обещает `est_h`; и обязательно смотреть PNG. Пустой `WARN` при изменённом кегле ничего не доказывает.
- **Возможное исправление (не сделано):** сделать константу функцией кегля либо просто занизить её до ~104 и пересверить все двенадцать карточек практик. Требует трогать общий файл в момент, когда его правят другие сессии, поэтому отложено.
- **Status:** active.
- **First seen in:** #212 (Лекция 5, перестройка практики Раздела 2 по правилу Р8 владельца, 2026-09-30).

> **Статус `[#212-6]`: ИСПРАВЛЕНО для `slides_band6.py` 2026-09-30** (сведение форм двенадцати
> карточек практик). Константа плотности в `est_lines` приведена к факту — `104` символа на
> дюйм ширины обычным начертанием и `98` жирным вместо прежних `122`/`114`; остаточный запас
> вынесен в отдельный множитель `SF = 1.04`, который применяется ТОЛЬКО при расчёте высоты
> полос (`fit_h`), а сторож `_check` по-прежнему считает по голой оценке, иначе он молчал бы
> там, где текст реально вылезает. Проверено на всех двенадцати карточках: до правки шаг
> механизма на `s24a` оценивался в две строки, а рисовался в три и наползал на следующий шаг
> при ПУСТОМ `WARN`; после правки оценка совпадает с фактом рендера. Остальные полосы
> (`slides_band1..5.py`) сохраняют прежнюю калибровку — там свои, уже подогнанные глазами
> высоты, и менять их без пересверки каждого слайда нельзя.
>
> **`[#212-5]` (примитивы мимо `_check`) остаётся активной, но на этой полосе сужена:** высота
> полосы МЕХАНИЗМ у всех двенадцати карточек теперь берётся как максимум из посчитанной высоты
> шагов и ЯВНО ОБЪЯВЛЕННОЙ высоты схемы (`mechanism(..., schema_h=...)`), а не назначается на
> глаз. Ошибиться по-прежнему можно — `schema_h` пишет человек, — но ошибка теперь одна и
> видна в одном месте, а не разбросана по координатам отдельных фигур. Три случая реального
> вылезания (`s11b`, `s24a`, `s24c`) были найдены именно глазами на PNG, а не сборкой.

> **Статус `[#212-4]` и `[#212-4b]`: ИСПРАВЛЕНО 2026-09-30.** В `render.sh` профиль LibreOffice и каталог вывода получили суффикс `$$` (идентификатор процесса), то есть у каждого вызова они свои. Обходные пути со сборкой в `/tmp` и приватным профилем больше не нужны. Правило проверки остаётся в силе: сверять собранный `.pptx`, а не код возврата скрипта.

### [#212-8] Норма «заметки 280–350 слов» меряется по исходнику, а в рендере к ним приписывается библиография — сквозная проверка даёт ложную тревогу

- **Симптом:** после правки всех восьми разделов сквозная проверка по собранному `.pptx` показала 14 слайдов с заметками вне нормы (до 475 слов), хотя каждая сессия независимо отчиталась, что её слайды в коридоре 280–350.
- **Причина не в содержании.** У всех четырнадцати исходные заметки в `.md` лежат в норме (281–346 слов). Перебор целиком даёт блок «Источники:», который `notes_with_sources()` приписывает к заметкам при сборке: от 19 до 129 слов библиографии со ссылками и пояснениями.
- **Почему это важно записать:** очевидная реакция на такую проверку — «сократить заметки», то есть вырезать реальный устный текст ради цифры, которую раздувает справочный аппарат. Это ровно тот класс ошибки, от которого спасает разделение «тело против аппарата», уже применённое к главе (источники вынесены из измеряемого тела, см. `chapter-references.md`).
- **Правило измерения:** норма 280–350 слов относится к **устному тексту**, то есть к разделу `## Speaker notes` в `.md`. Блок источников в неё не входит — он адресован лектору, а не аудитории, и в устной речи не произносится. Мерить надо исходник; проверка по собранному `.pptx` годится для запрещённых оборотов и для факта непустоты, но не для длины.
- **Severity:** P2 — не ломает артефакт, но провоцирует вредную правку.
- **First seen in:** #212 (Лекция 5, сведение восьми параллельных сессий, 2026-09-30).



### [#211-3] `notes_budget.py` знал один шов из двух и приговаривал к переполнению речь, написанную по норме: 10 слайдов из 68 мерились не по той границе

- **Инструмент:** `library/seminars/sem-05/rendered/notes_budget.py` (проверка контракта заметки, `AUTHOR-BRIEF.md` §3 п. 9), не MCP-сервер.
- **Симптом.** Восемь слайдов приходили с приговором «речь не влезает в слот»: `n01` (1,72 мин при слоте 0,75), `n09` (2,26 при 1,50), `n04` (2,08), `n67` (2,04), плюс `n02`, `n68`, `n66`, `n36`. Четыре слайда вдобавок получали «справки нет вовсе» при полной справке на экране. Шесть из восьми приговоров были ложными.
- **Причина.** Шов между речью и справкой искался ОДНИМ оборотом — «Если спросят». Так написаны 58 слайдов из 68. Остальные десять — слайды рамки и закрытия — отбивают справку явной чертой `---` и заголовком `**Справка.**`, а оборот «Если спросят» стоит в них не первым абзацем справки, а в середине. На этих десяти проверка резала заметку по позднему шву, и всё, что лежало до него, — заголовок справки и абзацы `*Про …*` — попадало в РЕЧЬ. На `n01` произносимая часть 72 слова приходила 223-словной; сам слайд при этом пишет про себя: «речевая часть короче ста двадцати слов намеренно: в сорок пять секунд больше не входит».
- **Почему не ловилось.** Самопроверка была, прогонялась и проходила 4/4 — но все четыре пробы написаны на обороте «Если спросят». Проверка, чьи пробы знают один вид входа, подтверждает, что она работает на этом виде, и молчит про остальные. Это не дырка в наборе случаев, а дырка в наборе ФОРМ входа.
- **Серьёзность:** P1. Ложный приговор дороже молчания: он отправляет сессию переписывать заметку, которая написана правильно, а настоящие нарушения тонут среди ложных (16 сообщений, из них настоящих 10).
- **Починка (применена, 2026-10-01).** Швы ищутся по очереди: сначала явный (`---` / `**Справка.**`), и только если его нет — оборотный. Порядок важен: на слайде с обоими маркерами явный стоит раньше. Голая черта в счёт слов не идёт, заголовок `**Справка.**` идёт (он её слова).
- **Проверка.** В самопроверку добавлены две пробы на явный шов — годная и сломанная. Мутация проверена: на прежнем коде годная заметка 150/197 мерится как 193/154 и получает сразу два ложных приговора, код возврата 1.
- **Что показала верная мерка.** 16 нарушений → 10. Переполнений слота 8 → 0: шесть из восьми были этим дефектом, настоящих оказалось два (`n09` — вся заметка одной частью, справка не отбита; `n36` — перебор на три слова). «Справки нет вовсе» 4 → 1.
- **Остаточное, не чинилось намеренно.** `n01`: речь 72 слова при нижней границе 82 — слайд обосновывает краткость сам, а добивать речь словами ради порога значит дописывать содержание. Вынесено находкой владельцу, не правкой.
- **Статус:** ПОЧИНЕНО.
- **Впервые замечено:** #211 (Семинар 5, круг 4, сквозной прогон рендерера, 2026-10-01).

### [#211-1] `line_spacing` вещественным числом — доля высоты строки ШРИФТА, а `metrics.line_h` считает её долей КЕГЛЯ: строка рисуется на 19,7% выше мерки

- **Инструмент:** render-toolchain (`library/seminars/sem-05/rendered/deck_kit.py` → `text_box`, `metrics.py` → `line_h`), не MCP-сервер.
- **Симптом (видимый, три класса сразу).** На `n46` ряд пилюль-терминов, который приём `base_and_edge` ставит под базой, заходил на последнюю строку базы на **4,8 pt** — текст перечёркнут рамками пилюль. На `n45`, `n50`, `n51`, `n07`, `n13` последняя строка залитой терминальной карточки печатается **ниже её дна** (от 1,2 до 10,7 pt), тёмным по белому фону, то есть нечитаемо. Сборка при этом молчит: по всей деке `ПЕРЕПОЛНЕНИЕ`/`НА ДНЕ КЕГЛЯ`/`ШИРЕ РАМКИ` не дают ни одного сообщения про эти слайды.
- **Причина.** `deck_kit.text_box` пишет `p.line_spacing = spacing` вещественным числом. И LibreOffice, и PowerPoint понимают такое значение как долю **собственной высоты строки шрифта** (для Arial/Liberation Sans ≈ 1,197 кегля), а `metrics.line_h` считает ту же величину долей **кегля**: `size_pt * spacing / 72`. При кегле 18 и `TRACK_SPACING = 1.30` мерка даёт 23,4 pt, LibreOffice рисует **28,1 pt**. Ошибка копится по строкам, поэтому ловит её первой та фигура, которую ставят вплотную под текст, и последний ряд в карточке фиксированной высоты.
- **Почему не ловится ничем существующим.** `qa_preview.py` рисует картинку САМ и той же меркой — расхождение с LibreOffice он не видит **по построению**, и на `n46` в предпросмотре наложения не было вовсе. Все сборочные сторожа тоже меряют через `metrics`. Поправки `K_LAYOUT`/`K_REPORT` здесь ни при чём: они про **ширину** (DejaVu против Arial), а расходится **высота строки**.
- **Severity:** P1 — дефект виден студенту (перечёркнутый текст, нечитаемая строка за краем карточки), не ловится ни одной автоматической проверкой цепочки и воспроизводится на любом слайде, где под текстом стоит фигура.
- **Проверка (написана, прогоняется).** `rendered/check_tracks_pdf.py` — читает PDF, выданный LibreOffice, и сверяет нарисованные строки с рамками фигур из `.pptx`. Два сообщения: `РЕЖЕТ` (фигура пересекает строку, не будучи её рамкой) и `ВЫВАЛИЛСЯ` (строка ниже дна залитой карточки). `--self-test` гоняет четыре пробы — две сломанные и две годные, по одной паре на каждое сообщение; на сломанных обе срабатывают, на годных молчат.
- **Исправление — проверено замером, но НЕ применено.** `p.line_spacing = Pt(size * spacing)` вместо вещественного числа: на пробе из двух одинаковых надписей шаг строки стал ровно **23,4 pt** против прежних 28,1, то есть совпал с меркой знак в знак. Не применено намеренно: правка переверстает всю деку (текст станет на 19,7% плотнее) и затронет шесть приёмов сразу, а `deck_kit.py` в круге 4 правят параллельно несколько сессий. Передано в сквозной прогон рендерера (волна 4).
- **Обход до исправления.** Сокращать содержание бесполезно и вредно: выигрыш составляет всего `(28,1 − 23,4) = 4,7 pt` на одну убранную строку при кегле 18 и ≈2,0 pt при кегле 10, то есть карточке `n45` пришлось бы отдать четыре строки из десяти. Смотреть PNG настоящего рендера и прогонять `check_tracks_pdf.py`; пустой вывод сборки и чистый `qa_preview` ничего не доказывают.
- **Status:** ПОЧИНЕНО (круг 4, сквозной прогон рендерера, 2026-10-01). `deck_kit.text_box`
  пишет `p.line_spacing = Pt(size * spacing)`; в файл идёт `<a:spcPts>`, абсолютный шаг.
  Замер после правки: мерка 23,4 pt, нарисовано 23,4 pt — расхождение 0,1% против прежних
  19,9%. `check_tracks_pdf.py` по всем 68 страницам: было 5 сообщений, стало 0 (закрылись
  и `ВЫВАЛИЛСЯ` на стр. 45/50/51/66, и `РЕЖЕТ` по цифре «05» на обложке). Переверстка НЕ
  сменила ни одного кегля и ни одной рамки — 0 фигур из 68 слайдов изменили геометрию или
  кегль, 6 `ПОДГОНКА` до = 6 после; изменились только 837 абзацев в представлении
  межстрочного. Так и должно быть: мерка всегда была права, врал только писатель в файл,
  поэтому вёрстке нечего было пересчитывать — ей вернули ту высоту, которую она и считала.
- **Побочное, починено заодно:** `qa_preview.py` читал межстрочный как `isinstance(…, float)`
  и на `Length` молча брал 1.22 — сразу после правки предпросмотр разошёлся бы с рендером
  снова, только в другую сторону. Теперь читает оба вида.
- **Сторож, который умер от этой починки, и что с ним сделано.** `--self-test` в
  `check_tracks_pdf.py` ломал свои пробы САМОЙ недомеркой (длинная база → пилюли режут;
  длинный листинг → карточка мала). После правки обе пробы перестали ломаться, и прогон
  честно сказал `ПРОВЕРКА МЁРТВАЯ` — проба, которая больше не ломается, не доказывает
  ничего про проверку. Пробы переписаны на ЯВНУЮ ГЕОМЕТРИЮ (фигура, поставленная на строку;
  карточка, чьё дно приходится на середину строки) — они не зависят от арифметики ни одного
  приёма и не умирают от её починки. Добавлена пятая проба — на ШАГ СТРОКИ: она поймала бы
  исходный дефект и ловит возврат вещественного числа. Мутация проверена: откат правки даёт
  код возврата 1 и строку «НЕДОМЕРКА ВЕРНУЛАСЬ (допуск 2%) … расхождение +19,9%».
- **First seen in:** #211 (Семинар 5, круг 4, кейс 5 — `n46` «база и кромка», 2026-10-01).

### [#211-4] `deck_kit._col_shares` меряет шапку таблицы КАК НАПИСАНО, а `table_card` рисует её ЖИРНЫМИ КАПИТЕЛЯМИ: заголовок колонки переносится посреди слова, и ни один сторож об этом не говорит

- **Где:** `library/seminars/sem-05/rendered/deck_kit.py` — `_col_shares` (стр. 377-406) и
  `table_card` (стр. 553).
- **Что происходит.** `_col_shares` даёт колонке ПОЛ шириной «самое длинное слово + 0,2″»,
  и меряет это слово как `M.text_w(wd, size, mono=…)` — то есть **без жирного и без
  капители**. Дальше `table_card` печатает шапку `text_box(…, ht.upper(), …, bold=True)` в
  ширину `shares[j] - gap`, где `gap = 0,16″`. У DejaVu жирное шире обычного на 11,9%,
  капитель прибавляет сверху ещё ≈15%. Замерено на кегле 9,5 pt: `Reinforcement` меряется
  в 1,095″, а `REINFORCEMENT` рисуется в 1,264″ при доступных 1,170″ — не влезает и
  переносится как `REINFORCEMEN / T`.
- **Почему не ловится ничем.** Ячейка ПЕРЕНОСИТ текст, а не вываливает его: `_fits`
  меряет переполнение по высоте блока, а здесь блок своей высоты не превысил — он просто
  некрасиво разорвал слово. `ПЕРЕПОЛНЕНИЕ` молчит, `ШИРЕ РАМКИ` молчит (слово уже рамки
  колонки по НЕЖИРНОЙ мерке), `check_text_overlap_pdf.py` молчит (ничего ни на что не
  наехало). Дефект виден только глазами на настоящем рендере.
- **Почему русская дека на этом не горела.** Та же шапка по-русски — «УСИЛЕНИЕ», 0,820″
  жирным: внутри любого пола с запасом. Дефект латентный и достаётся только более длинному
  языку. Нашла его английская дорожка (`n03`, круг переводов), а не русская сборка.
- **Обход на сегодня — только в английском драйвере.** `build_sem05_en.py._col_shares_bold`
  меряет шапку так, как её рисуют (`.upper()`, `bold=True`), и добирает недостающую ширину
  у колонок, у которых есть запас, сохраняя сумму. Применяется ТОЛЬКО к английской сборке:
  поднять пол в самом `deck_kit.py` значит перепропорционировать уже одобренные русские
  таблицы, а русский рендер двигать нельзя.
- **Что делать правильно.** Либо чинить в `deck_kit._col_shares` (мерить шапку
  `plain(h).upper()` жирным и прибавлять `gap`) и пересматривать русский рендер глазами,
  либо оставить как есть и держать шапки короткими. Решение владельца; записано открытым
  пунктом в `library/seminars/sem-05/EN-TRACK-BRIEF.md`.
- **Впервые замечено:** #211 (Семинар 5, английская дорожка, рамка `n01`-`n05`/`n65`-`n68`,
  2026-10-03).

### [#211-5] `build_sem05.py` НЕ байт-воспроизводим: три пересборки неизменённой деки дают три разных файла — «русский рендер цел» нельзя подтвердить хешем

- **Где:** `library/seminars/sem-05/rendered/build_sem05.py` (и любой сборщик на python-pptx).
- **Замер.** Три подряд пересборки неизменённых `deck.yaml` + `slides/` дали sha256
  `8c3026fd…`, `f1d26a88…`, `2b46be0a…`. Причина — python-pptx проставляет собственные
  отметки времени в записи zip-архива.
- **Чем это опасно.** Во-первых, у ревьюера НЕТ хеша, которым можно показать, что русский
  рендер не тронут: сравнение «было/стало» всегда расходится, даже когда ничего не менялось.
  Во-вторых — и это ловушка, в которую легко попасть, — запуск `build_sem05.py` «просто
  чтобы проверить, что всё собирается» **портит закоммиченный артефакт**, и его приходится
  возвращать через `git checkout`. Ровно это и случилось в начале английской дорожки.
- **Как с этим жить.** Неизменность русского рендера держится КОНСТРУКЦИЕЙ, а не сравнением:
  русские скрипты не правятся, английский драйвер физически отказывается писать
  `sem-05.pptx` (`build_sem05_en._save_guard`), а `refresh_manifest()` сам пропускается для
  любого манифеста, кроме `deck.yaml`. Проверка прозрачности драйвера сделана через
  `build_sem05_en.py --selftest`, который сравнивает СОДЕРЖИМОЕ слайдов (типы форм,
  геометрию, тексты прогонов, заметки) с закоммиченным `sem-05.pptx`, а не байты.
- **Правило для английской дорожки:** не запускать `build_sem05.py` вовсе (решение D9 в
  `library/seminars/sem-05/EN-TRACK-BRIEF.md`).
- **Впервые замечено:** #211 (Семинар 5, английская дорожка, 2026-10-03).

### [#225-1] `WebFetch` на длинной официальной HTML-странице конфликтует само с собой между повторными вызовами — не только на PDF

- **Tool:** `WebFetch` (не MCP-сервер, встроенный инструмент харнесса), на `arxiv.org/html/...` и `code.claude.com/docs/...` — живые HTML-страницы, не PDF.
- **Симптом.** Три независимых случая за один проход фактчека:
  1. **Арифметика категорий MAST** (`arxiv.org/html/2503.13657`). Первый запрос («quote exact category-level percentages») вернул `FC1≈43.9%, FC2≈31.35%, FC3≈23.5%` — числа, которые инструмент явно получил, **суммируя** подпункты сам (`11.8+1.5+15.7+2.80+12.4`), причём даже собственная сумма посчитана с ошибкой (`2.20+6.80+7.40+0.85+1.90+13.2` даёт 32.35, в ответе — 31.35). Независимый `WebSearch` по тем же категориям дал другие числа — `41.8% / 36.9% / 21.3%` — совпадающие с цифрами уже в курсовом research-документе (`sem-05/research/stage-6-subagent.md`). Третий, более осторожный запрос («не считай сам, только цитируй напечатанные totals») честно ответил «category-level totals не напечатаны явно».
  2. **Семантика `tools: []` у субагента** (`code.claude.com/docs/en/sub-agents`). Первый запрос (широкий, «extract everything relevant») вернул таблицу из трёх строк, где «Empty List» ведёт к тому же тексту ошибки, что и «Unresolvable Tool Name» (`usually fails to launch with error: Agent would be spawned with zero tools`) — то есть инструмент **слил два разных кейса документации в один**. Третий запрос («quote word-for-word, if not addressed say so») по той же странице ответил: «Case 1 (`tools: []`) is NOT explicitly addressed» — то есть опроверг собственный более ранний вывод.
  3. **Цитата `code-reviewer` vs `debugger`.** `WebSearch` дважды выдал связный, грамматически законченный «ответ» с цитатой `«Unlike the code reviewer, this one includes Edit because fixing bugs requires modifying code»` и списком прав `Read, Edit, Bash, Grep, Glob`, представив её как «from the official Anthropic documentation». Прямой `WebFetch` той же страницы с явной инструкцией «search character by character, if not found say NOT FOUND, do not guess» не нашёл **ни фразы, ни списка** нигде на странице; полный дамп оглавления страницы (все `##`/`###` заголовки с превью) подтвердил — раздела с таким сравнением на странице нет вовсе.
- **Root cause (предположительно).** `WebFetch` прогоняет контент через «small, fast model» (см. собственное описание инструмента) — она не копирует, а **пересказывает**, и при длинном/табличном источнике со склонностью доделывать недостающую арифметику или правдоподобный пример выдаёт связный, но не обязанный быть точным текст. `WebSearch` обёрнут так же — его «ответ» строится по сниппетам выдачи, не по прямому чтению страницы, и может звучать как цитата, не будучи ею. Ни один из двух инструментов не возвращает сырой HTML/текст без прохода через суммаризацию.
- **Severity:** P1 — не блокирует работу (есть обход), но может подтвердить **несуществующую** цитату как «VERIFIED», если остановиться на первом ответе; ровно то расхождение, которое в `issue #223` ранее документировали для PDF, здесь воспроизводится на обычном HTML официальной документации.
- **Workaround:**
  1. Не доверять первому ответу `WebFetch`/`WebSearch` на числовой/цитатный вопрос без перепроверки.
  2. Переформулировать запрос как «quote verbatim, if not found say NOT FOUND, do not compute/guess» и сравнить с первым, более широким запросом — расхождение между ними само по себе сигнал.
  3. Кросс-проверять через второй независимый путь (`WebSearch` с другим запросом, полный дамп оглавления страницы, либо курсовой research-документ, если утверждение уже туда занесено с датой обращения) — число, подтверждённое ОДНИМ инструментом ОДИН раз, не считать VERIFIED.
  4. Явная цитата («дословно», «verbatim») из официальной документации — отдельный повод для третьего, максимально узкого перепроверочного запроса именно по этой фразе, а не по теме вообще.
  5. **Самый надёжный обход — не спрашивать модель вообще.** `curl -s -L <url> | strip-tags` (или эквивалент) и прямой `grep`/чтение получившегося текста глазами — без прохода через суммаризирующую модель ни на одном шаге. На повторной проверке (issue #225, круг 2, 2026-10-05) этот способ на первой же попытке нашёл все три утверждения, которые три разных прохода `WebFetch`/`WebSearch` не смогли подтвердить согласованно: цитату и оба списка прав `code-reviewer`/`debugger` (`code.claude.com/docs/en/sub-agents`, раздел «Example subagents», буква в букву) и правило для `tools: []` (`code.claude.com/docs/en/errors`, раздел «Agent would be spawned with zero tools», дословно «If you leave the tools list empty… Claude Code also skips the refusal and launches the subagent without tools»). Обе страницы оказались на месте и не изменились — ложноотрицательный результат порождала именно суммаризация, не отсутствие материала на странице.
- **Status:** active (инструмент по-прежнему ненадёжен; обход п.5 закрывает проблему полностью, но требует ручного `curl`, не встроен в `WebFetch`/`WebSearch`).
- **Resolution note (issue #225, круг 2, 2026-10-05):** оба случая из п.2 и п.3 симптома, ранее поднятые как P0/P1 в `qa/fact-check-krug-vladeltsa.md`, при повторной проверке через обход п.5 оказались **корректными утверждениями деки** — цитата и `tools: []` подтвердились, ложноотрицательными были именно прежние прогоны `WebFetch`. Случай п.1 (арифметика MAST) ранее уже был закрыт через `WebSearch` + курсовой research-документ и правок не потребовал.
- **First seen in:** #225 (Семинар 6, круг правок владельца, фактчек нового материала блоков MCP/субагент, 2026-10-05). Примечание: бриф этой сессии ссылался на более раннюю запись «issue #223» с тем же классом проблемы на PDF — в файле на момент написания этой записи такой записи не нашлось (возможно, не была сохранена в своё время); эта запись фиксирует её заново на HTML-материале и может считаться продолжением того же наблюдения.

---

### [#225-2] `soffice` и `pdftoppm` не лежат на `PATH` — переносимая сборка стоит в `~/.local`, и без неё PPTX→PDF не собирается вовсе

- **Server / tool:** render-toolchain (LibreOffice headless + poppler `pdftoppm`), конвейер сборки деки семинара.
- **Симптом:** `soffice --headless --convert-to pdf` и `pdftoppm` отвечают `command not found`. Отдельная ловушка: `sem-06.pdf` от прошлой сборки остаётся на диске, и проверки `check_text_overlap_pdf.py` / `check_tracks_pdf.py` честно отрабатывают **по устаревшему файлу**, печатая ноль наложений для деки, которой уже нет. Зелёный результат при этом ничего не значит.
- **Корневая причина:** системных пакетов LibreOffice и poppler на машине нет; обе программы стоят переносимой сборкой в домашнем каталоге, и обе требуют своего `LD_LIBRARY_PATH` (`pdftoppm` без него падает на `libpoppler.so.134`).
- **Severity:** P1 — без обхода не собирается ни PDF, ни снимки, то есть не работают три сторожа из пяти.
- **Workaround:**
  ```bash
  export LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
  export PATH=/home/harness/.local/libreoffice-portable/program:/home/harness/.local/lo-sysroot/usr/bin:$PATH
  soffice --headless -env:UserInstallation=file:///tmp/lo-<своё-имя> --convert-to pdf --outdir . <файл>.pptx
  pdftoppm -r 110 -png <файл>.pdf snapshots/iter
  ```
  Своя `UserInstallation` обязательна, когда рядом работает другая сессия, иначе вторая конвертация молча виснет на занятом профиле. Первый запуск занимает больше двух минут — ставить таймаут от 400 с.
  **Перед прогоном PDF-сторожей удалять старый `sem-06.pdf` и `snapshots/iter-*.png`**, а не перезаписывать: иначе неудавшаяся конвертация оставит прошлый файл и проверка пройдёт по нему.
- **Status:** `active`.
- **Где впервые:** issue #225, сведение круга правок владельца Семинара 6 (2026-10-05); LibreOffice 26.2.4.2, poppler 24.02.0.

---

### [#225-3] Прерванный `soffice --convert-to` оставляет `.~lock.<выход>#`, и каждая следующая конвертация падает с непрозрачным `Io … Abort Code:27`

- **Server / tool:** render-toolchain (LibreOffice headless), конвейер PPTX→PDF деки семинара.
- **Симптом:** после конвертации, убитой по таймауту (`[#225-2]` предупреждает, что первый прогон занимает больше двух минут, и 120-секундный таймаут убивает именно её), **все** последующие попытки на том же выходном файле падают:
  ```
  Error: Please verify input parameters... (SfxBaseModel::impl_store
  <file://…/sem-06.pdf> failed: 0x11b(Error Area:Io Class:Abort Code:27))
  ```
  PDF не создаётся вовсе. Сообщение говорит про «входные параметры», хотя входной `.pptx` исправен и параметры те же, которыми минуту назад конвертация шла, — то есть текст ошибки указывает не туда, где причина. Новая `-env:UserInstallation` не помогает: профиль здесь ни при чём. `pgrep soffice` чист — висящего процесса нет, и обход «дождаться, пока `pgrep` опустеет» из `[#212-2]` к этому случаю не применяется.
- **Корневая причина:** LibreOffice кладёт рядом с выходным файлом скрытый файл блокировки `.~lock.sem-06.pdf#` и снимает его при нормальном завершении. Убитый процесс снять его не успевает, файл остаётся на диске, и `impl_store` отказывается писать поверх живой, с его точки зрения, блокировки. Проверено прямо: `ls -la | grep lock` показал `.~lock.sem-06.pdf#` (76 байт), после `rm` конвертация прошла с первой попытки без иных изменений.
- **Severity:** P1 — отказ выглядит как порча исходника и уводит разбор в сторону (проверка `.pptx`, профилей, диска, параметров), хотя лечится одной командой.
- **Workaround:** перед конвертацией снимать блокировку заодно со старым выходом:
  ```bash
  rm -f sem-06.pdf '.~lock.sem-06.pdf#'
  ```
  Это дополняет указание `[#225-2]` «удалять старый `sem-06.pdf` перед прогоном сторожей»: удалять надо **оба** файла, иначе удаление самого PDF оставляет блокировку и отказ сохраняется. Таймаут на конвертацию ставить от 400 с — тогда причина не возникает вовсе.
- **Status:** `active`.
- **Где впервые:** issue #225, сведение круга «заметки на сайт» Семинара 6 (2026-10-07); LibreOffice 26.2.4.2.

## [#225-4] Субагент `literary-editor` не запускался вовсе: `tools: All tools` во фронтматтере = ноль инструментов

**Дата:** 2026-10-10 · **Где:** `.claude/agents/literary-editor.md`

**Симптом.** Запуск отказывает до старта: «Agent 'literary-editor' would be spawned with zero
tools — refusing. Its tools list resolved to nothing: unrecognized [All, tools]».

**Причина.** `tools: All tools` в YAML-фронтматтере разбирается как **список из двух строк**
`["All", "tools"]` — двух инструментов с такими именами не существует. Строка «All tools» в
реестре агентов (`(Tools: All tools)`) — это то, как реестр печатает **отсутствие** ограничения,
а не значение, которое надо туда вписать. У всех остальных агентов проекта `tools:` нет вовсе.

**Починка.** Строку удалить. Отсутствующий `tools:` = наследуются все инструменты. Пустой
список `[]` = запуск без инструментов; нераспознанное имя = отказ запуска.

**Почему записано повторно.** Тот же класс уже записан в `notes/decisions.md` (2026-10-01, из
issue #212) — **но сам файл агента тогда не поправили**, и агент оставался незапускаемым девять
дней. Запись о грабле не заменяет починку того места, где она живёт.

**Дополнение того же дня.** Правка фронтматтера **не действует в текущей сессии** — реестр
агентов читается один раз при её запуске, и после удаления строки запуск отказывал тем же
сообщением. Нужен перезапуск Claude Code. Обход на сейчас: взять другого агента (`book-editor`)
и передать ему базу редактуры `tools/editorial/` явной ссылкой в задании.

---

### [#225-5] Сторож `audit_sluzhebnoe.py` не видел подсказку ведущего от первого лица — ловил только обращение ко второму/третьему лицу

- **Server / tool:** собственный скрипт проекта (не MCP) — `library/seminars/sem-06/rendered/audit_sluzhebnoe.py`, проверка видимого слоя готовой `.pptx` на служебные надписи (правило А4).
- **Symptom:** на слайде n52 Семинара 6 в видимом слое стояла строка «Состав верного ответа до разбора не называю» — ведущий сам объявляет свой приём там, где это видит зал, ровно то, что запрещает А4. Сторож дал ноль совпадений: фраза уже была снята вручную до того, как это заметили, но сам факт, что она прошла мимо пяти действовавших правил, — дефект проверки, не только слайда.
- **Root cause:** все пять правил, написанных до правки, собраны по фразам, которые владелец назвал дословно («Лектору:», «Преподавателю —», «вы здесь», «выбор делает зал», «здесь ничего не решается») — все они адресованы ведущему СО СТОРОНЫ (2/3 лицо). «Не называю» грамматически 1 лицо — тот же дефект по смыслу (подсказка на экране вместо заметок), другая форма, которую ни один из пяти шаблонов не покрывал класс.
- **Severity:** P1 — ровно тот тип дефекта, ради которого сторож существует; не блокировал сборку (фраза снята руками раньше, чем это обнаружилось), но до правки класс был дырой целиком, не частным пропуском одной фразы.
- **Workaround / Fix:** добавлено шестое правило `подсказка от первого лица (А4, лектор о своём приёме)` — два смысловых куста шаблонов, не одна фраза: (а) отказ назвать/показать/раскрыть прямо сейчас в 1 л. ед. числа наст./буд. времени («не называю», «пока не скажу», «не раскрываю», модальное «не буду/стану раскрывать» и т.п.); (б) обещание вернуться или разобрать позже («вернёмся к этому», «разберём позже», «расскажу позже», «оставим на потом»). Деепричастия и безличные формы («называются», «называя») исключены намеренно — иначе обычные описательные предложения ловились бы ложно. Проверено на исторической копии `sem-06.pptx` (`git show 4f7f72b6:…`, фраза ещё на экране) — 1 точное совпадение, слайд 52; и на нуле ложных срабатываний на трёх живых деках (Семинар 4 — 57 слайдов, Семинар 5 — 68, Семинар 6 — 64, 189 слайдов итого) плюс на отдельном списке каверзных слов (`контроль`, `роль`, `называются`, `станция` и т.п.). Подробности — `library/seminars/sem-06/qa/storozh-podskazka-ot-pervogo-litsa.md`.
- **Status:** `fixed-in-fork` (в контексте этого проекта — «починено на месте», файл свой, не внешний MCP-сервер) — класс закрыт для найденных форм, не для всех возможных перефразировок; отчёт выше честно называет, что ещё не поймается (безглагольная отсрочка, деепричастия, глаголы вне списка, подсказка, разбитая на две фигуры слайда).
- **First seen in:** #225 (Семинар 6, сведение после двух проведённых занятий, 2026-10-10).

---

### [#225-6] Шелл `grep` в этом окружении — функция, запускающая `ugrep`; `\b` на кириллице без `-P` ненадёжен

- **Tool:** шелл-команда `grep` (на деле функция, которая через `exec -a ugrep` запускает `ugrep` без `-P`, то есть не PCRE, а собственный режим `ugrep`), не сам `audit_sluzhebnoe.py` — тот работает через Python `re` и этой проблемы не имеет.
- **Symptom:** `grep -no '\bроль\b'` на входе из четырёх строк (`контроль`, `контроля`, `контролируемый`, `роль`) не находит «роль» на своей строке, а при родственном шаблоне `\bрол\b` вместо этого даёт ложное совпадение на строке «роль» (подстрока «рол» из четырёх букв слова «роль» — само слово «роль» длиннее совпадения). При этом `command grep` (настоящий GNU `grep`) и чистый Python `re.compile(r'\bроль\b')` на тех же четырёх строках ведут себя предсказуемо: совпадение только на «роль», ноль на остальных трёх.
- **Root cause:** шелл-функция `grep` в этой сессии переопределена на запуск `ugrep` в режиме `-G` (basic/extended regex, не PCRE) без явного `-P`; граница слова `\b` в этом режиме на кириллице работает не так, как в PCRE/Python `re` (которые по умолчанию unicode-aware). Сам факт переопределения виден через `type grep` (печатает тело функции).
- **Severity:** P2 — не блокирует работу, но может завести по ложному следу при ручной проверке regex-идеи через шелл перед тем, как закладывать её в скрипт (ровно то, от чего предостерегала эта сессия: «рол» внутри «контроль/контроля/контролируемый» дало пять ложных срабатываний при проверке через шелл).
- **Workaround:** новые regex-шаблоны для `audit_sluzhebnoe.py` (и вообще для кириллических `\b`-шаблонов) проверять **через сам `python3 -c "import re; ..."`** либо через `command grep -P` (настоящий GNU `grep`, PCRE-режим) — не через голый `grep`/`ugrep` без `-P`.
- **Status:** `active` (особенность окружения, не баг конкретного инструмента проекта).
- **First seen in:** #225 (Семинар 6, проверка нового правила сторожа `audit_sluzhebnoe.py`, 2026-10-10).

## [#225-7] Поправка к `[#225-6]`: это `grep -P` лжёт на кириллице, а не оболочечный `grep`

**Дата:** 2026-10-10 · замер оркестратора, локаль `en_US.UTF-8`

Запись `[#225-6]` утверждает обратное тому, что есть. Проверено на файле со словами
`роль · контроля · субагент · зал · показал`, шаблоны `\bроль\b`, `\bзал\b`, `\bсубагент\b`:

| Чем | Результат |
|---|---|
| `grep` оболочки (обёртка над `ugrep`) | **верно** |
| Python `re` | **верно** |
| `command grep -P` | **0 совпадений там, где они есть** |
| `grep -P` с `(?<!\w)…(?!\w)` | ложное совпадение: «зал» внутри «показал» |

То есть опасен именно `-P`: `\b` и `\w` в PCRE здесь считают по байтам, и отказ приходит в виде
**ложного нуля**, неотличимого от чистоты. Обход через `(?<!\w)` лжёт в другую сторону.

Отдельно: пять ложных срабатываний, которые и завели это правило, дал не инструмент, а
**односторонний якорь** в шаблоне оркестратора (`[Рр]ол[ьияею]\b` находит «роля» внутри
«контроля»). С якорями по обе стороны Python отвечает верно.

**Правило:** Python `re` или `grep` оболочки; `-P` по кириллице не использовать; якорить с двух
сторон; смотреть контекст совпадений, а не счёт.

**Сведено с `[#201-6]`.** Та запись (сентябрь, #201) замерила противоположный симптом —
`\bмин\b` срабатывало ВНУТРИ слова «минут». Корень один: буквы классифицируются по байтам, и
`\b` врёт в обе стороны в зависимости от того, где стоит в шаблоне. Плюс сменился инструмент:
в сентябре `grep` был GNU grep, сейчас это обёртка над `ugrep`, которая отвечает верно. Вывод
обеих записей совпадает — Python `re`, якоря с двух сторон, `-P` по кириллице не использовать.

### [#233-1] `slide_parts.blocks()` рассекает ряд карточек-вариантов, записанный в несколько строк markdown

- **Tool:** `slide_parts.py` (библиотека приёмов семинарского деки-кита, сем-04→сем-07 без изменений).
- **Symptom:** Приём-карточки (`· вариант1 · вариант2 ·`) опознаётся только если на ОДНОЙ строке
  исходника стоят «·» и ≥4 бэктика (2+ сегмента). Если автор слайда записал те же варианты в
  НЕСКОЛЬКО строк (по одному варианту на строку, или по два), разбор либо вообще не находит
  триггер (1 сегмент/2 бэктика на строку — условие `>=4` не выполняется, строки тихо копятся в
  обычный абзац), либо находит, но **на пороге «≥3 варианта» внутри ОДНОЙ строки** — у `flush()`
  в `blocks()` нет памяти о том, что он уже резал предыдущую строку: `flush()` вызывается ПЕРЕД
  проверкой количества, поэтому две строки по 2 сегмента каждая разрезаются на ДВА отдельных
  `para`-блока по 2 сегмента, и порог «≥3» не набирается ни в одном по отдельности.
- **Root cause:** `slide_parts.blocks()` детектирует карточки СТРОГО построчно (`"·" in ln and
  ln.count("\`") >= 4`), без накопления между строками. Работает для деки, где автор уже знает
  про это ограничение и пишет карточки одной строкой (так писали в Семинаре 6); ломается молча,
  когда следующий автор естественно переносит длинные варианты на отдельные строки для
  читаемости исходника — результат не падает с ошибкой, а тихо превращается в `para`-блок с
  ролью `fact`/`formula` и ВИДИМЫМИ бэктиками на слайде вместо четырёх карточек-вариантов.
- **Severity:** P1 (находка Семинара 7, Фаза 5 — 2 из 2 слайдов с приёмом `question_with_option_
  cards` этой деки были задеты, оба с разным паттерном разреза: 1×4 строки/сегмент и 2×2
  строки/сегмента).
- **Workaround:** Не правь `slide_parts.py` (кит общий на несколько семинаров, менять его —
  менять поведение для уже собранных дек). Чини в build-слое занятия: после `SP.blocks(visual)`
  прогони повторную детекцию по ТОМУ ЖЕ признаку (бэктики + «·»), но (а) внутри уже склеенных
  `para`-блоков и (б) слиянием СОСЕДНИХ `para`-фрагментов, если каждый по отдельности — «чистый»
  (после вычитания `` `сегментов` `` остаётся только «·» и пробелы), пока суммарно не наберётся
  порог. Реализация — `build_sem07.py`, `_card_fragment`/`_merge_card_fragments`/`sanitize_
  blocks`. Дешёвая альтернатива на будущее: писать карточки-варианты ОДНОЙ строкой в исходнике
  (как делал Семинар 6) — тогда обходной код в build-слое не нужен вовсе.
- **Status:** active (workaround в сем-07 работает; `slide_parts.py` не пофикшен).
- **First seen in:** #233 (Семинар 7, Фаза 5 сборки деки, 2026-10-11), слайды `n21`/`n27`.

### [#233-2] `deck_kit.inline_runs`/`metrics.fits` не умеют одиночный курсив `*…*` — печатает честное предупреждение, но не чинит

- **Tool:** `deck_kit.py`/`metrics.py` (библиотека приёмов, без изменений с Семинара 5-6).
- **Symptom:** `inline_runs()` разбирает только `**жирный**` и `` `моноширинный` ``; одиночная
  `*звёздочка*` (markdown-курсив) не интерпретируется — звёздочки печатаются на слайде буквально
  («*(независимого гейта нет)*»). `metrics.fits()` это УЖЕ ловит (`_ITALIC` regex, предупреждение
  «РАЗМЕТКА … вёрстка не умеет») — но только называет находку, не чинит её: это осознанное
  решение авторов кита (см. комментарий у `fits()` — «молча срезать звёздочки нельзя, так
  прошлая версия теряла целевые ответы, помеченные жирным»), и относится оно к `**bold**`, не к
  одиночному курсиву, который кит в принципе не поддерживает как начертание.
- **Root cause:** `inline_runs`/`M.inline_segments` никогда не реализовывали курсив как третье
  начертание (только bold/mono) — не баг, а недостающая фича.
- **Severity:** P2 (находка Семинара 7 — 2 слайда, `n13`/`n18`, с одиночным курсивом внутри
  формульной строки/цитаты).
- **Workaround:** В build-слое занятия, ДО передачи текста в `block_drawer`, снять одиночный
  курсив (`_LONE_ITALIC` regex, ТОТ ЖЕ паттерн, что `metrics._ITALIC` использует для детекции)
  — текст остаётся, начертание курсива теряется. Реализация — `build_sem07.py`,
  `_degloss_italic`, вызывается из `sanitize_blocks`. Не вариант для `code`-блоков (там `*` часто
  настоящий знак — `*args`, глоб-шаблон) — там снятие не применяется.
- **Status:** active (workaround в сем-07 работает; `deck_kit.py` не получил третьего начертания).
- **First seen in:** #233 (Семинар 7, Фаза 5 сборки деки, 2026-10-11), слайды `n13`/`n18`.


### [#233-3] n8n Public API: нет метода «запустить сценарий» — запуск только через настоящий триггер

- **Tool:** n8n Public API 1.1.1 (стенд `n8n.lessons.tellian.io`, n8n 2.42.7).
- **Symptom:** в спецификации нет ни одного эндпойнта, исполняющего сценарий по требованию.
  Ближайший — `POST /workflows/{id}/test-runs` («запустить тестовый прогон»), и он про набор
  тестовых случаев, а не про «выполни этот сценарий сейчас». Выложить сценарий через API можно,
  убедиться что он работает — нельзя.
- **Root cause:** осознанное решение n8n: исполнение привязано к триггеру, а не к API.
- **Severity:** P1 для любой автоматической проверки учебного примера: без обхода «проверено»
  означает только «API принял JSON», что не то же самое.
- **Workaround:** дать сценарию настоящий триггер и позвать его извне. Для учебных примеров
  Семинара 7 это Form Trigger: `POST https://<host>/form/<path>` с `multipart/form-data`.
  Дальше результат читается из `GET /executions?includeData=true` и из строк таблицы
  (`GET /data-tables/{id}/rows`). Реализация — `library/seminars/sem-07/stend/README.md`.
- **Status:** active (обход работает, фичи в API нет).
- **First seen in:** #233 (Семинар 7, сборка учебных примеров на стенде, 2026-10-12).

### [#233-4] n8n Form Trigger: поля на проводе зовутся `field-N`, отправка по подписям молча даёт `null`

- **Tool:** `n8n-nodes-base.formTrigger` (typeVersion 2.2), n8n 2.42.7.
- **Symptom:** узел отдаёт данные под ПОДПИСЯМИ полей (`$json['Что нужно']`), и это же видно в
  браузере — поэтому отправка снаружи делается по подписям. HTML-форма при этом посылает
  `field-0`, `field-1`, `field-2` по порядку. Отправка по подписям проходит с кодом **200**,
  сценарий исполняется **успешно**, и во всех полях оказывается `null`. Замерено: первый прогон
  записал в таблицу строку из трёх `null` и темы «Недостаточно информации.» — модель честно
  ответила на пустой запрос, и ни одна проверка в сценарии этого не заметила.
- **Root cause:** раскладка `field-N` → подпись живёт внутри узла; наружу имена подписей не
  принимаются и неизвестные поля не отвергаются.
- **Severity:** P1 — отказ молчаливый, с зелёным статусом прогона. Ровно тот класс, про который
  занятие и говорит.
- **Workaround:** отправлять `-F 'field-N=…'` по ПОРЯДКУ полей в узле, и обязательно сверять
  результат: прочитать выход триггера в `GET /executions?includeData=true`, а не доверять
  коду 200.
- **Отдельно, и это стоило одного круга прогонов:** в нумерации участвуют и поля, которые
  НЕ являются вводом. Блок разметки (`fieldType: html`, объяснение наверху формы) занимает
  `field-0`, и настоящие поля сдвигаются на `field-1..3`. Замерено: после добавления блока
  прогоны стали падать с `Text for item 0 is not defined`, а код ответа формы остался 200.
  Добавили или убрали любое поле, включая разметку — проверять нумерацию заново.
- **Status:** active.
- **First seen in:** #233 (Семинар 7, проверка учебных примеров, 2026-10-12).

### [#233-5] n8n: прогон с узлом завершения формы остаётся в статусе `waiting`, пока экран не запросят

- **Tool:** `n8n-nodes-base.form` (`operation: completion`), n8n 2.42.7.
- **Symptom:** сценарий отработал полностью — все узлы в `runData`, строка в таблице записана, —
  а `GET /executions` показывает `status: "waiting"`, а не `success`. Автоматическая проверка
  «прогон успешен?» по статусу даёт ложное «нет».
- **Root cause:** узел завершения формы — узел ожидания: прогон ждёт, пока браузер запросит
  страницу результата (`/form-waiting/<id>?signature=…`). Подробный механизм (подтверждён
  2026-10-18, Семинар 8): HTML-ответ формы несёт встроенный JS, который делает `POST` именно
  на этот `formWaitingUrl` (подпись приходит только в ответе на исходный
  `POST /form/<path>`) — и только этот POST переводит execution из `waiting` в `success`.
  Скриптовый клиент, который отправляет форму и уходит (а не ведёт себя как браузер до конца),
  никогда не делает этот второй шаг — отсюда `waiting` навечно, независимо от корректности
  бизнес-логики до этого узла. **Прямое воспроизведение:** `curl -X POST
  ".../form-waiting/<id>?signature=..."` на зависшем execution немедленно переводит его в
  `success` без повторного прогона — проверено на execution `41` стенда Семинара 8 (`waiting`
  до вызова, `success` после, те же данные).
- **Severity:** P2 — на занятии незаметно (окно открыто и забирает страницу сразу), ломает только
  автоматическую проверку; стоит часа недоверия к совершенно корректным данным, если принять
  `waiting` за признак обрыва и начать перепроверять/перезапускать бизнес-логику вместо того,
  чтобы понять, какой именно узел ждёт браузера.
- **Workaround:** судить по `runData` (все ли узлы отработали, нет ли `error`) и по данным на
  выходе, а не по полю `status`, если сценарий дёргают скриптом не из браузера. Там, где нужен
  чистый `success`-статус без браузера — либо завершить handshake программно (`POST` на
  `formWaitingUrl` с подписью из ответа на отправку формы), либо заменить `Form`-ответ на
  `Webhook`/обычный ответ без второй страницы.
- **Status:** active.
- **First seen in:** #233 (Семинар 7, проверка экрана результата, 2026-10-12); confirmed again
  in #274 (Семинар 8, эксперимент Кейса 3 — root cause и прямое воспроизведение уточнены там).

### [#233-6] n8n: `Split Out` игнорирует `destinationFieldName` при записи через API

**Замерено 2026-10-15** на стенде (n8n 2.42.7). Узел `n8n-nodes-base.splitOut` с
`fieldToSplitOut: "output.topics"` и `destinationFieldName: "topic_raw"` кладёт значение
в поле с именем **`output.topics`** — то есть с точкой внутри имени. Обращаться нужно
`$json['output.topics']`; `$json.topic_raw` возвращает `undefined`.

**Чем опасно:** выражение, читающее несуществующее поле, не падает, а тихо уходит в ветку
по умолчанию. У нас обе расщеплённые строки получили тему «другое» — результат выглядел
правдоподобным и прошёл бы беглый взгляд.

### [#233-7] n8n: процесс, созданный через API, не отдаёт форму по своему `path`

**Замерено 2026-10-15.** Процесс создан через `POST /api/v1/workflows`, активирован через
`/activate`, в интерфейсе помечен `Published`, `triggerCount: 1`, `activeVersionId` заполнен.
При этом `GET /form/<path>` отдаёт **404**, а `GET /form/<webhookId>` — **200**.
Деактивация с повторной активацией не помогает.

**Обход:** пользоваться адресом `/form/<webhookId>` либо пересохранить процесс руками в
интерфейсе.

### [#233-8] n8n: экран `/executions/<id>` в браузерном UI недостижим для агента на этом стенде — только API-ключ, не логин

- **Где:** стенд `n8n.lessons.tellian.io` (та же дуга С7–С12), Семинар 8, Фаза production
  (#274), попытка снять настоящий скриншот интерфейса n8n для пары executions Кейса 3.
- **Симптом.** `/home/harness/.n8n-lab-credentials` и хендовер-файлы дают только
  `N8N_API_KEY` (управляющий REST API, заголовок `X-N8N-API-KEY`) — ни логина, ни пароля,
  ни сессионной куки для веб-интерфейса n8n нет. Открыть `https://n8n.lessons.tellian.io/
  workflow/<id>/executions/<id>` в браузере без интерактивного логина нельзя.
- **Root cause:** API-ключ и UI-сессия — два разных, не связанных механизма входа. Сам
  API-ключ в этом развёртывании минтится ТОЛЬКО из уже залогиненного UI (Settings → n8n
  API → Create an API key — курица и яйцо: чтобы получить ключ, нужен логин, которого у
  агента нет). Отдельно: headless-браузер в этой среде не поднимается без root (`[#229-3]`
  — `no new privileges`, нет 14 системных библиотек); даже если бы поднялся — страница
  execution всё равно требует залогиненной сессии, которой взять неоткуда.
- **Severity:** P2 — не блокирует занятие (данные execution полностью читаются через
  `GET /executions/<id>?includeData=true` и `runData`), но исключает класс материала
  «настоящий скриншот интерфейса n8n» для любого слайда, который показывает конкретный
  execution с этого стенда.
- **Workaround:** слайд показывает РЕАЛЬНЫЕ значения полей execution (сумма, решение,
  текст заявки, id) как оформленный блок/таблицу, подписанный `execution <id>,
  n8n.lessons.tellian.io` — не стилизованный fake-UI (запрещён правилом `no-mock-fallbacks`
  курса), а прямые данные из `runData` настоящего прогона. Этот путь уже используется в
  принятой деке Семинара 7 (`n32-k3-reshenie-demo.md` — таблица настроек узла вместо
  скриншота карточки).
- **Status:** ~~active~~ **resolved** (см. апдейт 2026-10-20 ниже) — для класса материала
  «скриншот канваса/списка узлов» живого стенда. Диагноз про `/executions/<id>` (конкретный
  экран прогона с данными execution) не переисследован этим апдейтом и может оставаться
  актуальным отдельно.
- **First seen in:** #274 (Семинар 8, Фаза production, добыча иллюстраций для Кейсов 1–4
  и эксперимента Кейса 3, 2026-10-18).
- **Update 2026-10-19 (#274, v3-пересборка по 16-пунктовой правке владельца):** владелец
  лично дал UI-логин/пароль (сохранён в `/home/harness/.n8n-lab-credentials` как
  `N8N_UI_EMAIL`/`N8N_UI_PASSWORD`) — курица-и-яйцо из исходной записи снята, предположение
  «нет логина» было неверным допущением. Блокер не снялся: `npm install playwright` +
  `npx playwright install chromium` проходят без root (скачивание бинарника не требует
  привилегий), но `browserType.launch()` падает с `error while loading shared libraries:
  libatk-1.0.so.0: cannot open shared object file` — подтверждено через `ldd` 8 отсутствующих
  системных библиотек, и `sudo -n true` подтверждает отсутствие root ни у оркестратора, ни у
  изолированного worktree субагента. Т.е. корневая причина — не отсутствие логина (снято), а
  то же самое ограничение окружения, что и `[#229-3]` (нет root нигде в этом харнессе), просто
  теперь подтверждено заново с валидными credentials в руках. **Решение для v3-деки:**
  вместо живых скриншотов — максимально точные программные схемы (Ocean-палитра,
  `n8n_canvas_kit.py`, реальные значения параметров со стенда), явно помеченные в
  `backup:`-поле фронтматтера каждого такого слайда как «программно нарисованная схема, не
  снимок живого UI» — не silent genre-substitution.
- **Update 2026-10-20 (#274, та же голосовая правка владельца «обязательно вернуть реальные
  скрины настройки узлов n8n»): ограничение СНЯТО для живого UI-канваса.** Та же техника,
  что уже задокументирована для Лекции 7 (headless-браузер через обход
  `~/.cache/page-shot-libs/x`), применена к этому стенду и сработала: `libatk-1.0.so.0` и
  остальные 7 библиотек из апдейта 2026-10-19 были отсутствующими системными `.so`, а не
  запрещёнными к установке — обход кладёт совместимый набор библиотек в путь, который
  Playwright-браузер находит без `LD_LIBRARY_PATH`-магии и без root. `browserType.launch()`
  поднимается, логин по `N8N_UI_EMAIL`/`N8N_UI_PASSWORD` (из апдейта выше) проходит, и с
  живого стенда `https://n8n.lessons.tellian.io` сняты 9 настоящих скриншотов канваса
  (воркфлоу Кейсов 1, 2 и 3 — список `library/seminars/sem-08/stend/n8n-screenshots-raw/`).
  Корневая причина апдейта 2026-10-19 была верно диагностирована (отсутствующие системные
  библиотеки), но вывод «недостижимо в этой среде окончательно» — неверным: `[#229-3]`
  описывает отсутствие ROOT, а обход через `~/.cache/page-shot-libs/x` решает именно нехватку
  библиотек БЕЗ root, что и было пропущено при записи апдейта 2026-10-19. **Применено к
  Семинару 8, фаза апдейта материала (#274):** 4 слайда (`n11`, `n14`, `n34`, `n50`)
  переведены с программных Ocean-схем на кропы настоящих скриншотов —
  `rendered/figures/{k1-n8n-versiya1,k1-n8n-versiya2,k3-n8n-if-uzel,k4-n8n-tsepochka}-real.png`;
  прежние программные файлы (без суффикса `-real`) оставлены на диске, слайды на них больше
  не ссылаются. Кейс 2 (`n17`–`n26`) сознательно НЕ тронут этой правкой — ждёт отдельного
  решения владельца (jev-перестройка), хотя скрин `case2-dedup-prod.png` текущего состояния
  уже снят и лежит в той же папке про запас. **Для следующих семинаров (С9+): если снова
  возникает «headless-браузер не поднимается», сначала проверить обход
  `~/.cache/page-shot-libs/x`, прежде чем записывать limitation как `active`.**
  Экран `/executions/<id>` этим апдейтом отдельно не переисследован — он требует открытия
  конкретного прогона, а не только канваса, и мог не тестироваться; если понадобится для
  будущего слайда — перепроверить отдельно, а не наследовать старый вывод «недостижимо».
- **Update 2026-10-20, вечер (#274, Кейс 2 закрыт тем же днём): отложенное выше «ждёт
  отдельного решения владельца» — решено.** Владелец голосом явно подтвердил переход на
  гибрид хэш+jev как реально собранное решение (не рекомендацию), и в тот же день воркфлоу
  «С8 · Кейс 2 — дедупликация в два уровня» (id `c7evxIhox45tn127`) перестроен через
  управляющий API: узлы «Same question, reworded? (LLM)» и «Model (dedup)» удалены, вместо
  них — httpRequest-узел «Jev decision (reworded?)». Сняты ещё 2 настоящих скрина той же
  техникой (`~/.cache/page-shot-libs/x`): `case2-jev-node-config.png` (открытая панель
  параметров узла) и `case2-dedup-prod-jev.png` (полный канвас перестроенного воркфлоу).
  Слайды `n22`/`n23` переведены с программных Ocean-схем на кропы этих скринов —
  `rendered/figures/{k2-n8n-mehanika,k2-n8n-jev}-real.png`; прежние программные файлы
  (`k2-n8n-mehanika.png`, `k2-n8n-llm-provexa.png`) оставлены на диске как запись устройства
  прежней версии цепочки (модель-судья), слайды на них больше не ссылаются. Экран
  `/executions/<id>` по-прежнему отдельно не переисследован в этом апдейте.

### [#229-1] `/tmp` общий между параллельными сессиями одного воркера: файл субагента перезаписан чужим содержанием

- **Где:** окружение исполнения субагентов (не MCP-сервер), каталог `/tmp`.
- **Симптом.** Субагент, собиравший исследование по фармацевтике, разбивал длинный отчёт на
  части через промежуточные файлы в `/tmp`. Часть 2 оказалась перезаписана содержанием
  другой параллельной сессии (клинический и регуляторный контуры того же круга). Обнаружено
  по системному сообщению о внешней модификации файла; агент перепроверил содержимое грепом
  по характерным словам и пересоздал часть напрямую, минуя `/tmp`.
- **Корневая причина.** В этом развёртывании `/tmp` разделяется между сессиями, работающими
  в одном воркере. Одновременно шли четыре исследовательские сессии одного круга, и
  предсказуемые имена промежуточных файлов совпали.
- **Severity:** P1. Отказ **молчаливый**: содержимое подменяется, а запись проходит успешно.
  Если бы агент не проверил файл по словам, в план лекции попало бы исследование не о том.
- **Workaround.** Субагент пишет результат **напрямую в рабочий каталог репозитория**, в
  файл со своим уникальным именем. Промежуточные файлы в `/tmp` при параллельной работе не
  использовать; если без них никак — имя обязано содержать идентификатор сессии. Проверка
  после записи — по содержанию (грепом по словам, которых не может быть у соседа), не по
  факту успешной записи.
- **Отдельное следствие для брифов:** в задание субагенту, работающему в волне, добавлять
  строку «пиши напрямую в репозиторий, не через `/tmp`».
- **Status:** `active`.
- **Впервые замечено:** #229 (Лекция 7, волна исследования кейсов, 2026-10-10).

### [#229-2] Дополнение к `[#223-6]`: `timeout` обязателен на любом тяжёлом внешнем вызове

- **Где:** любой внешний вызов из Bash без встроенного предела — `ugrep`/`grep -P` с широким
  квантификатором без привязки к строке (`[^.]\{0,80\}`, `.{0,60}`), `soffice --convert-to`,
  конвертеры, рендереры.
- **Что произошло (2026-10-10, три случая за сутки на этом воркере).** Сестринская сессия сняла
  внешним TERM процесс, провисевший **два часа** в `mem_cgroup_handle_over_high` на
  `ugrep -o -i 'change[a-z -]*condition[^.]\{0,80\}' out.txt`. Отдельно был случай с
  `soffice --convert-to`.
- **Почему отказ невидим.** Процесс упирается в `memory.high` (1,54 ГБ), **`oom_kill` не
  срабатывает** (`memory.max` 3 ГБ не достигнут), и ядро дросселирует его бесконечно. Снаружи это
  не видно **ни в API, ни в чате**: сессия просто молчит. Изнутри дроссель не снимается.
- **Правило.** `timeout <N>` на каждый потенциально тяжёлый внешний вызов. **Если не укладывается в
  timeout — сужать шаблон, а не ждать:** невлезание само означает, что шаблон патологический.
  Для поиска по крупным файлам предпочитать python с построчным чтением.
- **Severity:** P0 — цена одного случая измерена в часах простоя, и простой невидим.
- **Status:** `active`. Обобщает `[#223-6]`, заведённую сессией Лекции 6.
- **Впервые замечено:** #223 (Лекция 6); подтверждено трижды 2026-10-10 на #229.

---

### `[#229-3]` Браузера нет, root недоступен — снимки веб-страниц для слайдов не добывались вовсе

**Обнаружено:** 2026-10-11, добыча иллюстраций Лекции 7.

**Симптом.** Восемь кадров деки просят снимок веб-страницы (страница регулятора, карточка
испытания, лента отзыва). Сессия добычи проверила `chromium`, `chromium-browser`,
`google-chrome`, `firefox`, `wkhtmltoimage`, `cutycapt`, `playwright` — нет ничего, и записала
восемь кадров как «не добыто, нет браузера». Среди них **обязательный hero `s105`**, у которого
права как раз чистые (уведомление регулятора США — общественное достояние): кадр упирался
только в съёмку.

**Почему обычные обходы не работают.**

- `apt-get install` требует root.
- `sudo` запрещён **флагом ядра «no new privileges»**, а не паролем: `sudo -n true` отвечает
  «The "no new privileges" flag is set». Это конфигурация контейнера, обойти изнутри нечем.
- `pip install playwright` падает на PEP 668 («externally-managed environment»).
- `python3 -m venv` не создаёт рабочее окружение (нет `ensurepip`).
- Браузер, скачанный `playwright install`, не запускается: **недостаёт 14 системных библиотек**
  (`libasound`, `libatk`, `libcairo`, `libcups`, `libpango`, `libX*`, `libxcb-render`,
  `libXi`, `libXrender` и далее). `ldconfig -p` не знает ни одной — их нет в системе,
  а не просто нет на пути загрузчика.

**Обход, который работает (без root).** Скачать системные пакеты обычным пользователем,
распаковать в свой каталог, подложить браузеру через `LD_LIBRARY_PATH`:

```bash
apt-get download libcairo2 libpango-1.0-0 …   # 37 пакетов, права root не нужны
dpkg-deb -x <pkg>.deb ~/.cache/page-shot-libs/x
export LD_LIBRARY_PATH="$(find ~/.cache/page-shot-libs/x -name '*.so*' \
  | xargs -n1 dirname | sort -u | tr '\n' ':')"
pip install --break-system-packages --user playwright && python3 -m playwright install chromium
```

**Закреплено в репозитории, чтобы не выводить заново:**
`tools/presentation-build/setup_page_shots.sh` (идемпотентный подъём) и
`tools/presentation-build/shoot_page.py` (съёмка: `--full`, `--selector`, двойная плотность
точек). Проверено от начала до конца на странице перечня устройств с ИИ у регулятора США.

**Библиотеки кладутся в `$HOME/.cache/page-shot-libs`, не в `/tmp`** — `/tmp` общий между
сессиями и чистится, это уже стоило файла в `[#229-1]`.

**Что `shoot_page.py` печатает после каждого снимка и почему.** Напоминание записать адрес,
дату съёмки и **права на содержимое страницы**: снимок страницы не делает её содержимое
свободным. Инструмент снимает что угодно, включая подписную статью, — решение о правах
остаётся за тем, кто снимает.

### Поправки к `[#229-3]` по итогам второго применения (2026-10-12, добыча hero s105)

Инструмент работает как описано — но запись выше трижды неполна, и каждая неполнота стоила
прогона.

**1. `source` нельзя заворачивать в конвейер.** `source setup_page_shots.sh 2>&1 | tail -5`
исполняет скрипт в **подоболочке**, экспорт `LD_LIBRARY_PATH` теряется, и chromium падает с
`exitCode=127`. Выглядит это **точно как отсутствие библиотек** — то есть отправляет обратно в
тот самый тупик, который скрипт и существует закрыть. Запускать `source` без конвейера; вывод
смотреть отдельной командой.

**2. «Проверено на сайте регулятора США» — неверно для его же базы данных.** Запись выше
проверялась на `www.fda.gov`, и этот хост действительно работает. **`accessdata.fda.gov` —
не работает:** его краевой фильтр отвергает сам браузер, перебрасывая каждый запрос на
`apology_objects/excessive-requests-apology.html`, который отдаёт 404 — бесконечная петля
перенаправлений до таймаута `goto`. Это **не** ограничение частоты и **не** User-Agent:
`curl` с того же адреса в ту же секунду получает 200, а подстановка настоящего UA вместе с
блокировкой всех подресурсов до единственного документа не меняет ничего. Блокировка по
отпечатку клиента.

**Обход, проверенный на этой съёмке:** перехватывать запросы к такому хосту через
`ctx.route` и отдавать их из `curl`. Байты при этом подлинные, настоящий браузер их
отрисовывает, ничего не дорисовано и не перекрашено; страница выходит такой, какой её видит
посетитель. **Сделано флагами `--via-curl` и `--user-agent`** (коммит `a8e28087`).

**Поправка к этому рецепту — без неё он НЕ работает.** Абзац выше говорит, что делать с
блокирующим хостом, и молчит про **остальные**. Очевидное прочтение — пропускать их
(`r.continue_()`) — **отказывает**: эта же страница FDA тянет `dap.digitalgov.gov`,
`s7.addthis.com`, `www.googletagmanager.com`, исход на них отсюда висит, и браузер досиживает
весь таймаут `goto` **без единого кадра** — ровно тот симптом, который обход и лечит. Два
прогона потеряно на этом. Непопадающие хосты надо **обрывать**, а не пропускать; инструмент
теперь печатает, какие хосты оброшены и сколько раз, чтобы «страница как её видит посетитель»
осталось проверяемым утверждением, а не допущением.

**Поправка о числе:** «все ~20 подресурсов» — заниженное. На этой странице **46 запросов**
(скрипты, стили, изображения шапки плюс два XHR датчика Akamai). Число взято из самоотчёта
первой съёмки и перенесено мной в запись без пересчёта — ровно та ошибка, про которую
этот каталог и ведётся.

**И третий ложный успех, найденный при проверке:** один повторный прогон получил на главный
документ transient 400, и инструмент **жизнерадостно отчитался об успешной съёмке страницы
ошибки**. Теперь при ответе ≥400 на главный документ он громко предупреждает и выходит с кодом
1. Это тот же класс, что и ложный «готово» при нуле библиотек: средство сообщало об успехе,
измеряя не то, что обещало.

**3. Скрипт не идемпотентен, хотя объявлен таким.** Он пропускает всю загрузку, если
`$LIBDIR/x` уже существует. Значит **первый прогон, убитый на середине, оставляет навсегда
неполный набор библиотек, который повторный запуск не починит** — а симптом будет тот же
`exitCode=127`, то есть снова неотличимый от «библиотек нет». Лечится файлом-сигналом,
записываемым после последнего `dpkg-deb -x`.

**Отдельно — не про инструмент.** Предыдущий агент записал «ничего в этом окружении не умеет
снимать веб-страницы» и перечислил шесть проверенных отсутствующих программ. Вывод был
добросовестным и **неверным**: средство лежало в этом же репозитории, добытое прошлой сессией
ровно под эту задачу. Проверка наличия программ в системе отвечает на вопрос «что установлено»,
а не на вопрос «чем это делается здесь» — на второй отвечает `notes/`, и читать его надо
**до** перечисления тупиков, а не после.

---

### `[#229-4]` Третий случай одной ловушки: `git gc --auto` после коммита душит весь cgroup, и выглядит это как «отвалился классификатор разрешений»

**Обнаружено:** 2026-10-11, производство деки Лекции 7. **Диагноз поставила сестринская сессия,
не я** — изнутри задушенного процесса причина не видна, и это главная часть записи.

**Симптом, который видит агент.** Любой вызов оболочки возвращает «`claude-sonnet-5[1m]` is
temporarily unavailable (timed out), so auto mode cannot determine the safety of Bash». Чтение
файлов при этом работает. Вывод, который делает агент и который **неверен**: «сломался
классификатор разрешений, переживём, подожду».

**Что на самом деле.** `git gc --auto` запускается **сам** после `git commit`. Его
`git pack-objects` на этом репозитории съедает ~1,1 ГБ, cgroup прижимается к `memory.high`
(1,6 ГБ при `memory.max` 3 ГБ — поэтому **`oom_kill` не срабатывает**), давление доходит до
~90%, и ядро дросселирует **cgroup целиком**, включая главный процесс `claude`. Классификатор
не отвечает не потому, что сломан, а потому, что задушен вместе со всем остальным.

**Цена в этом производстве.** Шесть субагентов из одиннадцати убиты сторожом (600 с без
продвижения): оба P0-фикса главы, сверка первоисточников Разделов 7–9, блоки деки A, C, E, F и
добыча обязательного hero. Содержание они дописать успели — умерли на фазе самопроверки, то
есть ровно на вызовах оболочки. Работа спаслась целиком, но только потому, что лежала в
worktree и её никто не удалял.

**Почему это именно третий случай, а не новый баг.** `[#223-6]` и `[#229-2]` — тот же
`mem_cgroup_handle_over_high`, та же невидимость, тот же дроссель без `oom_kill`. Виновник
каждый раз другой: широкий квантификатор `ugrep`, затем `soffice --convert-to`, теперь
`git gc`. **Класс один: тяжёлый внешний процесс в общем cgroup.** Запись `[#229-2]` требовала
`timeout` на «любой тяжёлый внешний вызов» — и промахнулась по этому случаю, потому что
`git gc --auto` **никто не вызывает явно**: его запускает `git commit`, и обернуть его
`timeout` снаружи нечем.

**Почему стреляло на каждом коммите, а не иногда.** В `lessons-3bb49d40/.git/objects` лежало
**8 642 loose-объекта** при пороге `gc.auto` 6 700 по умолчанию. То есть auto-gc был не
случайностью, а **гарантией**: он запускался практически на каждом коммите, и репак такого
количества объектов в cgroup с `memory.high` 1,6 ГБ надёжно вызывает дроссель. Ловушка
срабатывала трижды за день именно поэтому.

**Починено структурно (2026-10-11, сестринская сессия):**
```bash
git config gc.auto 0      # в lessons-3bb49d40/.git/config
```
Настройка лежит в основном репозитории и **наследуется всеми worktree**, включая временные в
`/tmp`. Auto-gc при коммитах больше не запускается вовсе. Если объекты когда-нибудь реально
понадобится сжать — это делается явным `git gc` руками, в заведомо спокойный момент, а не
побочным эффектом коммита.

**Обход, пока фикс не был сделан** (оставлен для истории и для случая, если настройка где-то
не унаследуется):
```bash
git -c gc.auto=0 commit ...      # и то же для add/merge/fetch
```

**Разница между этими двумя лечениями — и есть урок записи.** Три раза подряд ловушка снималась
вручную: снять процесс `TERM`-ом, убрать осиротевший `gc.log.lock`, продолжить. Каждый раз это
работало и каждый раз возвращалось, потому что чинился **случай**, а не **причина**: порог
`gc.auto` оставался превышен, и следующий коммит стрелял снова. Одна строка `git config`
закрыла класс. Сигнал, по которому это стоило опознать раньше: **одна и та же поломка на третьем
круге — это не три инцидента, а один незакрытый корень.**

**Как опознать изнутри, если повторится.** «Классификатор отвалился» + «чтение работает» +
**только что был коммит** = почти наверняка это, а не классификатор. Проверять
`memory.current` своего cgroup и `pgrep -a 'pack-objects|git gc|repack'`; снимать `TERM`-ом
безопасно (временные файлы, атомарный `rename`, репозиторий не повреждается), после — убрать
осиротевший `.git/worktrees/<имя>/gc.log.lock`.

**Отдельный урок, не про git.** Я записал в чат неверную причину («отвалился классификатор») и
сообщил её владельцу как факт. Симптом был назван причиной, потому что изнутри дросселя видно
только симптом. **Правильная формулировка в такой ситуации — «вызовы оболочки не проходят, причину
изнутри не вижу»**, а не диагноз инструмента, который просто первым перестал отвечать.

**Severity:** P0 — цена измерена в шести убитых агентах, и отказ невидим: ни в API, ни в чате,
ни в логах самого git.
**Status:** `active`. Обобщает `[#223-6]` и `[#229-2]` третьим виновником.
**Впервые замечено:** #229 (Лекция 7, сборка деки, 2026-10-11).

---

### [#229-3] `deckkit/tables.py`: клетка матрицы красится полужирным ЦЕЛИКОМ, если в ней есть хоть одна пара звёздочек

- **Server / инструмент:** не MCP — `tools/presentation-build/deckkit/tables.py` (общее ядро сборщиков дек Лекций 6 и 7).
- **Feature:** разметка внутри ячейки таблицы.
- **Симптом.** Накопительная карта стадии задумана двухслойной: разборы ЭТОГО раздела
  полужирным, разделы, занявшие клетку раньше, — светлым, в одной ячейке. На экране оба слоя
  вышли одним начертанием, и различить их стало нельзя.
- **Причина.** `tables.py:219` — `col, bold = DEEP, "**" in cell`: признак берётся по НАЛИЧИЮ
  звёздочек в ячейке, а сам текст рисуется через `markup.plain(cell)`, то есть разметка
  снимается целиком. Прогонов внутри ячейки у таблицы нет вовсе (в отличие от тела кадра, где
  работает `markup.inline_runs`). Значит внутри одной клетки двух начертаний не бывает в
  принципе — только «вся клетка полужирная» либо «вся светлая».
- **Severity:** P2 — видимый дефект замысла, не поломка; молчит (предупреждения нет).
- **Обход, применённый на `s51` Лекции 7.** Слои разведены **скобками, а не начертанием**:
  имя без скобок — разбор этого раздела, имя в скобках — раздел, занявший клетку раньше, и
  это сказано строкой чтения прямо под таблицей. Звёздочки из ячеек убраны совсем, чтобы
  таблица не красилась наполовину. Тот же обход годится любой накопительной карте.
- **Чего делать НЕ надо.** Писать `**` вокруг части ячейки в расчёте на частичный акцент:
  предупреждения не будет, а полужирной станет вся клетка — расхождение замысла с экраном
  обнаруживается только глазами на снимке.
- **Status:** `active`. Чинится в ядре (прогоны внутри ячейки) — это правка `deckkit`, и её
  цену надо считать отдельно: ширины столбцов меряются по `plain()`, и переход на прогоны
  затронет подбор кегля таблицы.
- **Впервые замечено:** #229 (Лекция 7, блок 3 «Постановка диагноза», карта стадии `s51`, 2026-10-13).

### [#229-5] `deckkit/tables.py`: полужирность ставилась на ячейку целиком

**Симптом.** Накопительная карта стадии — «своё полужирным, пройденное светлым в одной
клетке» — не рисуется: клетка выходит полужирной вся. Сборщик при этом **молчит**.

**Причина.** `draw_table` решала начертание одним выражением `bold = "**" in cell`, а текст
рисовала через `plain(cell)` одной однородной надписью (`prims.text_box` — «одно начертание,
один кегль» по собственной доке). Двух начертаний в клетке не существовало в принципе.

**Чем обнаружено.** Тремя независимыми сессиями подряд (блоки 3, 5–6, 7–8) — и каждая сочла
это свойством жанра и обошла скобками, переписав легенду карты под то, что рисуется.
Предупреждения нет ни одного, в снимке видно сразу.

**Починка.** Клетка набирается прогонами (`markup.inline_runs` + `prims.text_runs`) под
переключателем `tables.CELL_RUNS`, читаемым **в момент вызова**, а не защёлкнутым в значении
по умолчанию — ровно та ошибка, которой в этом же пакете болел `floor.VIS_PT`.

**Почему переключатель, а не просто починка.** Лекция 6 сдана и прочитана залу с полужирной
клеткой целиком, её отпечаток держит регрессия. Замерено: включение прогонов по умолчанию
двигает кадры 75 и 88 доставленной деки (ячейки из одного прогона становятся тремя-восемью).
Поэтому ядро по умолчанию ВЫКЛЮЧЕНО, Лекция 7 включает флаг сама. После правки Лекция 6
снова воспроизводится: 100 кадров, 2202 фигуры, **0 расхождений содержимого**.

**Мера не плывёт:** ширины столбцов и так считались с `bold=True` (самый широкий случай).

**Проверка:** `[клетка-прогоны]` в `deckkit/selftest.py`, доказана разностно в обе стороны —
что включённый флаг даёт два начертания и что выключенный не двигает вид Лекции 6. 59 из 59.

### [#229-6] `deckkit/render.py`: относительный путь ломал рендер молча

**Симптом.** `render()` на относительном пути складывает PDF в `<папка>/<папка>/`, затем
`pdftoppm` падает «Couldn't open file». С абсолютным путём всё работает.

**Причина.** Обе команды делают `cd` в папку деки, а `--outdir` и путь снимков подставлялись
**как переданы**. После `cd` относительный путь указывает уже не туда, куда указывал у
вызывающего. Это второй случай того же класса в этом пакете: первым было `render()`, который
передавал окружение `soffice`, но не `pdftoppm`, и выходил с кодом 127 **после** записи PDF —
сборка докладывала провал при готовом PDF на диске.

**Чем обнаружено.** Сессией заключения круга #229, на живой попытке отрендерить свой диапазон.

**Починка.** `Path(...).absolute()` на оба пути в начале `render()`, `mkdir(parents=True)`.
Строки команд вынесены в `render_cmds()` — чтобы путь проверялся **без запуска LibreOffice**.

**Проверка:** `[рендер-путь]` в `deckkit/selftest.py`, доказана на сломанном входе: подаётся
относительный путь и проверяется, что команды выходят именно такими, на каких рендер ломался.
60 из 60.

### [#229-7] `deckkit/pdfmeasure.size_hist` берёт ПУТЬ, а не поток страницы: подстановка потока даёт `OSError: File name too long` на 4 КБ содержимого

**Симптом.** Соседние функции модуля (`text_runs(stream, …)`, `images(stream)`) принимают поток
страницы, а `size_hist(pdf, *, grid)` — путь к файлу. Вызов `size_hist(st)` внутри обычного
цикла `for n, st, box in pm.pages(pdf)` падает не `TypeError`, а
`OSError: [Errno 36] File name too long`, и в текст ошибки вываливается четыре килобайта
PostScript — потому что поток уходит в `Path(...).read_bytes()` как имя файла.

**Severity:** P2 — лечится правильным аргументом, но симптом не указывает на причину и съедает
прогон: сообщение читается как «проблема с файловой системой», а не «не тот аргумент».

**Обход.** `size_hist` зовётся ОДИН раз на файл и сама возвращает `(hist, by_page)`: гистограмму
целиком и разбивку по страницам. Внутри цикла по страницам её звать не надо вовсе — образец
правильного вызова есть в `library/lectures/lec-07/rework/deck/zamer_pdf.py:156`.

**Status:** `active`. Чинится либо приёмом потока вторым путём, либо переименованием параметра в
`pdf_path`; ни то, ни другое не сделано в этом круге — правка меры требует своей пробы, а круг
был про сторожей контраста и hero.

**Обнаружено:** 2026-10-14, при заведении независимого замера пола кегля по PDF
(`zamer-storozha-2026-10-14/zamer_pola_pdf.py`).

## [#229-8] Wayback: служебный ответ «снимков нет» ложен, `timemap` их отдаёт

**Что наблюдалось (2026-10-14, разведка мировых аналогов по issue #229).** Служебная точка
`https://archive.org/wayback/available?url=…` возвращала пустой ответ — то есть «снимков нет», —
а `http://web.archive.org/web/timemap/link/<url>` на том же адресе отдавал снимки **трижды**,
включая свежие: 2026-07-25 и 2026-10-05.

**Почему это опасно.** Пустой ответ выглядит как установленный факт («страницы в архиве нет»), и на
нём строится вывод «источник недоступен, утверждение не проверить». Это тот же класс ошибки, что
уже записан здесь как `[#225-1]`: **отрицательный ответ служебной точки — не доказательство
отсутствия.** В этом же производстве он стоил дорого в обе стороны: один «P0 фактчека» был найден
только после прямого чтения препринта, и один — **снят**, когда выяснилось, что рецензируемая
версия лежит в другой публикации.

**Обход.** Прежде вывода «в архиве нет» — спросить `timemap`:

```bash
timeout 60 curl -sL "http://web.archive.org/web/timemap/link/<URL>" | head -40
```

Пустой `timemap` при непустом `available` тоже встречается; отрицательным считать только случай,
когда **оба** молчат, и говорить об этом словами «не нашёл двумя способами», а не «в архиве нет».

## [#229-17] Ограничитель памяти контейнера душит ВСЮ сессию, а не только тяжёлую команду

**Запись была ошибочно заведена под номером `[#229-9]`, который уже занят** (`measure_body.py`
печатает выбранный кегль вместо вставшего). Перенумерована 2026-10-15. Ссылки на диапазоны
`[#229-9]`–`[#229-15]` в записях ниже означают **тот** `[#229-9]` — класс «отчёт инструмента
расходится с состоянием»; эта запись к нему не относится, она про среду исполнения. Два разных
предмета под одним адресом — тот же дефект, который каталог и описывает, допущенный самим
каталогом.

**Что наблюдалось (2026-10-14, замер нормы текста по issue #229).** Поиск `ugrep` с широким
захватом контекста по большому плоскому файлу (`garner2009.flat`, шаблоны вида `.{1500}`) съел
**1,18 ГБ** и прижал cgroup к `memory.high` (**1,6 ГБ**); давление доходило до ~55%. Торможение
накрыло **весь контейнер целиком, включая главный процесс агента** — то есть сессия выглядела
зависшей, хотя её собственная работа была ни при чём. Снято внешним `TERM`; память упала с 1,67 ГБ
до 0,49 ГБ.

**Почему это важно знать заранее.** Симптом — «сессия висит», и причина ищется в содержании работы,
а лежит в одной команде поиска. По словам сессии, снявшей затор, **эта ловушка на этой лекции и
семинарах срабатывала уже несколько раз**.

**Как искать по большим плоским файлам здесь:**

```bash
timeout 60 grep -n -m 20 -o '.\{0,300\}words per slide.\{0,300\}' big.flat
# нашли номера строк → читаем точечно
sed -n '12340,12380p' big.flat
```

Правила: узкий захват контекста (`.{0,300}`, не `.{1500}`) · предел совпадений (`-m 20`) ·
обязательный `timeout` · `grep -o` вместо выдачи целых строк · на файлах в десятки мегабайт — два
прохода (номера строк, затем `sed -n`). То же относится к `ugrep` и `rg`: широкий квантификатор
опаснее самого объёма файла (ср. `[#229-2]` — там он вешал процесс на часы).

## [#229-9] `measure_body.py` печатает выбранный кегль, а не вставший на страницу — ложное «чисто»

**Что случилось.** Сессия разрядов свидетельства получила от `measure_body.py` строку
`s18 13,5 пт · ниже 12 пт: 0`, тогда как сборка в тот же момент ругалась `[пол] s18/тело: 10,5 пт`,
и PDF подтверждал знаки на 10,5 пт. То есть прогон дал **ложное «чисто»** на кадре, который
сборка считает сломанным.

**Причина.** Он мерит кегль, выбранный по тегу `/тело`, и не видит того, что реально встало на
страницу после раскладки.

**Чем мерить вместо.** Только `[пол]` самой сборки и `deckkit/pdfmeasure` по собранному PDF.

**Тот же класс рядом:** `predict.py` на `comparison`-кадрах давал 95 слов против 140 по PDF;
`render_sec.py` **не печатает предупреждений ни на каком входе по устройству** (оборачивает
сборку в `report.snapshot()`/`report.restore()` и `report.blocking()` не зовёт) — его молчание
дважды прочли как «предупреждений нет».

**Правило, общее для всех трёх:** прогон, который по замыслу чего-то не делает, обязан это
печатать. Молчание инструмента читается как ответ — за один вечер производства #229 так вышло
шесть раз, в том числе у двух сессий, которые сами же это и записывали.

## [#229-10] `git push` напечатал `! [remote rejected] … (failed)` — а пуш прошёл

**Что случилось.** Сессия получила от `git push` отказ с кодом ошибки и проверила состояние:
`git ls-remote` показал, что удалённая голова **совпадает с локальной**, то есть пуш прошёл, а
сообщение об отказе было ложным. Поверив отчёту, она начала бы «починку» и пушила бы поверх уже
запушенного.

**Рядом, тот же вечер, тот же класс:** в клонах этого проекта refspec тянет с удалённого **только
`main`**, поэтому `git branch -r`, `origin/...` и `--contains` показывают по чужим ветвям
**осевшее состояние**, а `git push` отвечает «Everything up-to-date» по настоящему. Две сессии
независимо заключили «моей ветки на origin нет», когда она была.

**Чем проверять состояние ветки:** `git ls-remote origin refs/heads/<ветка>` либо `gh api
repos/<owner>/<repo>/branches/<ветка>`. Не `git branch -r`, не `origin/...`, не текст ответа
`push`.

**Общее правило вечера (восемь случаев):** **слово инструмента нельзя брать за ответ — проверяется
состояние.** Молчание прогона, его «чисто», его отказ и его успех — всё это отчёты, и каждый из
восьми раз отчёт расходился с состоянием.

## [#229-11] `render_sec.py N --zamer` мерит СУЩЕСТВУЮЩИЙ PDF и молча отдаёт старые числа

**Что случилось.** Сессия прочла вес кадра **126** и **137** из двух разных файлов в одной задаче,
не сверив, какой свежий, и на этом основании «подтянула» верный объявленный пол (140 при реальном
весе 137, запас +3) до 132 — то есть **испортила верное значение, доложив это как применение
правила**. Отката потребовала не проверка, а собственный перемер.

**Корень шире одного прогона: репозиторный `lec-07-karkas.pdf` никем не обязан пересобираться.**
Замерено в тот же вечер: PDF собран коммитом в 19:48, после него правлено **62 файла кадров**, и
приёмка всё это время мерила веса по нему. Сторож «кадр тяжелее своего объявленного пола» при этом
**молчал на живом дефекте** (кадр перевесил свой пол на шесть слов).

**Чем лечится.** Прогон, читающий собранный бинарник, обязан печатать: **каким коммитом он собран**
(`git log -1 --format='%h %ci' -- <pdf>`) и **сколько файлов кадров правлено после него**
(`git diff --name-only <коммит>..HEAD -- slides/`). Тогда «веса относятся к 19:48, после него
правлено 62 кадра» читается само. Пересборка бинарника назначается **явной работой** кому-то, иначе
её не делает никто.

**Класс:** тот же, что `[#229-9]` и `[#229-10]` — отчёт инструмента расходится с состоянием. За
вечер девять случаев, и три из них привели к порче верного значения либо к работе на уже сделанном.

## [#229-12] Сокращение ЗНАКОВ словом не считается — а на глаз выглядит экономией

Кадр стоял на 139 словах при пределе 140, и к нему требовалось добавить единицу измерения
(4 слова). Сессия «освободила» четыре слова: «на арбитраже» → «арбитраж», «от доверия автомату» →
«доверие автомату», **«48 секунд» → «48 с»**, **«+53 процента» → «+53 %»**. Собранный PDF дал
**141** — на одно больше предела: два последних сокращения короче **знаками**, но это **те же два
слова**. Пришлось добирать пятым («названо словами: понять, возразить, остановить» → «названо:
…», три глагола следом и есть те слова) — кадр сел на 140 ровно.

**Почему это стоит записи:** ошибка тихая и повторяемая, и **ни один счёт по телу файла её не
поймает** — мера курса считает слова на странице собранного PDF. «Сократил знаки» читается как
«сократил», пока не пересоберёшь.

**Правило:** правка под предел проверяется **пересборкой**, а не арифметикой в голове; «я снял
N слов» — это гипотеза до собранной страницы.

## [#229-13] `git show origin/<ветка>:<файл>` врёт так же, как `origin/<ветка>` — молча отдаёт прошлое

**Что случилось.** Сессия проверяла, дошла ли её правка пола до ветки: `git show
origin/issue-229-...:<файл>` напечатал **прежнее** значение (110 вместо 115), потому что в этом
клоне `origin/<ветка>` стоит на старом коммите — **refspec тянет с удалённого только `main`**
(`+refs/heads/main:refs/remotes/origin/main`). Она почти доложила «правка потерялась» — шестая
ложная тревога того же класса за вечер; спасло то, что она посмотрела ещё `HEAD` и рабочее
дерево и перепроверила **явным** `git fetch origin <ветка>`.

**Как читать состояние ветки в этих клонах:**
- `git ls-remote origin refs/heads/<ветка>` — хеш головы;
- `git fetch origin <ветка>` и затем `FETCH_HEAD` — содержимое;
- `gh api repos/<owner>/<repo>/branches/<ветка>` — то же через API.

**Чем НЕ читать:** `git branch -r`, `origin/<ветка>`, `git show origin/<ветка>:<файл>`, текст
ответа `git push`, `git merge-base --is-merged` (такой формы у git нет — ненулевой код читается
как «отстал»).

**ДОПОЛНЕНО 2026-10-15, замером: запрет шире, чем список команд выше — не свидетель НИ ОДНА
`origin/*`-ссылка, в любой команде.** Сессия проверяла, дошла ли чужая правка ядра до сводной
ветки, и трижды получила уверенный неверный ответ: `git merge-base --is-ancestor … origin/<ветка>`
сказал «не слито», `git show origin/<ветка>:<файл>` — «нужного имени в файле 0 вхождений».
Одновременно `git rev-parse origin/<ветка>` отдавал `92c5d26f`, а `git ls-remote` в ту же
секунду — `a2bfefe9`. Правка была на месте; сессия едва не доложила дирижёру, что её нет.

Причина прежняя: refspec тянет только `main`, локальная ветка слежения `origin/<что угодно ещё>`
**не обновляется никогда** и молча отдаёт состояние на момент своего создания; `git fetch origin`
без аргументов её не двигает. Под это попадают **`rev-parse`, `show`, `merge-base`, `log`,
`diff`** — всё, что принимает `origin/<ветка>` как ссылку, а не только `git branch -r`, на
который предупреждал наряд круга.

Порядок, которым получен верный ответ:

```bash
git ls-remote origin refs/heads/<ветка>            # истина о голове
git fetch origin refs/heads/<ветка>                # и только теперь
git show FETCH_HEAD:<файл>                         # читать по FETCH_HEAD
git merge-base --is-ancestor <мой коммит> FETCH_HEAD
```

**Класс:** вместе с `[#229-9]`–`[#229-12]` это шесть случаев одного дефекта — **отчёт инструмента
расходится с состоянием, и расхождение молчит**. Общее правило вечера: **слово инструмента нельзя
брать за ответ, проверяется состояние**; у проверки должен быть отрицательный результат, который
видно.

## [#229-14] `build_lec07.py --only sNN` молча переписывает выпуск деки частичной сборкой

**ЗАКРЫТО 2026-10-15 правкой пути, а не памятью.** `--only` пишет теперь в
`chastichnaya-sborka.pptx` и печатает «выпуск НЕ ТРОНУТ»; `verify_built` / `report` /
`verify_links` смотрят на тот же частичный файл. Выпуску частичная сборка недоступна
по построению.

**Почему чинилось путём, а не правилом.** Сессия круга знала о ловушке, восстанавливала файл
`git checkout` после каждой поштучной сборки и **предупредила письмом отдельно**. Оркестратор
это письмо прочёл, через час собрал один кадр и сам же превратил 7,9 МБ выпуска в 178 КБ.
**Предупреждение, прочитанное и не сработавшее, — доказательство, что лечить надо не памятью.**

**Что случилось (2026-10-15, разделы 6–10, issue #229).** Проверка блокирующих предупреждений
на одном кадре делается только так: `python3 build_lec07.py --only s67`. Прогон отчитывается
`собрано кадров: 1 → lec-07-karkas.pptx` — и это не временный файл, а **тот самый выпуск деки,
который лежит в репозитории**: после прогона `git status` показывает `M lec-07-karkas.pptx`, и
в пакете один кадр вместо ста одного. Ключа `--out` у прогона нет.

**Чем опасно.** Проверять кадр на блокирующие — рядовое действие, оно делается по многу раз за
круг правок, и каждый раз оставляет за собой подменённый выпуск. Коммит `git add -A` из любой
сессии уносит в ветку деку из одного кадра, а прогон при этом **не соврал**: он честно написал,
сколько собрал. Расходится не отчёт с состоянием, а ожидание («проверка ничего не меняет») с
тем, что проверка делает.

**Что делать.** Сразу после каждой частичной сборки:

```bash
timeout 900 python3 build_lec07.py --only s67,s68,s69   # `--only` принимает список через запятую
git checkout -- lec-07-karkas.pptx                      # вернуть выпуск на место
```

Список через запятую (`slidefile.slide_files`, ключ `only`) закрывает весь круг проверки одним
прогоном — и одним восстановлением вместо девятнадцати.

**Класс:** соседний к `[#229-11]`: там репозиторный PDF никем не обязан пересобираться, здесь
репозиторный PPTX пересобирается тем, кто его собирать не просил.

## [#229-15] `scan_deck_visible.visible_lines` видит НЕ ВЕСЬ видимый слой — и молчит об этом

**Что случилось (2026-10-15, issue #229).** Две сессии независимо прогнали свои полосы деки
Лекции 7 «сплошным проходом по видимому слою» через `visible_lines` и получили ноль там, где
нарушение было. Функция берёт `title`, плашки (`blocks[]`), схему (`caption` · ряд · шаг),
столбцы и раздел `## Видимый текст слайда` — и **пропускает**:

- `headline_number` — крупное число кадра (1 кадр деки),
- `figure.value` / `figure.unit` / `figure.base` — карточка одного числа (1 кадр),
- `media_caption` — подпись под иллюстрацией (3 кадра),
- `scheme.unit` / `scheme.base` / `scheme.marks` (5 кадров).

**Цена, замеренная на деке.** На `s64` проход по производственному словарю дал ноль, а крупное
число кадра стояло голым — «9,5 %» без единицы, при том что 9,5 % означает в деке две разные
величины. Тем же классом мимо прохода уехали подписи единиц на `s05` и `s45`. На полосе
разделов 6–10 так же не осматривался `figure` кадра `s105` — три знаменателя подряд без
указания, какой к какому числу; поймано только потому, что адрес пришёл письмом, а не прогоном.

**Почему ноль обманчив именно здесь.** Докстринг самого `scan_deck_visible.py` предупреждает
ровно об этом классе у СОСЕДНЕГО прогона (`scan_visible_layer.py` ищет видимый слой по разметке
ПЛАНА и на файлах кадров даёт «видимых полей: 0 — чисто» на любом входе). Тот же дефект на
ступень ниже: поле, которого извлекатель не читает, неотличимо от поля, в котором чисто.

**Чем лечится.** Полный извлекатель — `deck/vidimyy_sloy_polnyy.py`: `polnyy(path)` отдаёт
«где · текст» по всем перечисленным полям, `kadry_polosy([...])` отбирает кадры полосы.
Перечень собран пересчётом всех ключей фронтматтера всех 101 кадра, а не на глаз: **редкое поле
и есть то, которое проход пропускает**.

**Главное в нём — то, чего не делал прежний прогон: он печатает рядом с нулём список полей,
которые НЕ смотрит, и причину по каждому** (17 полей: `assertion` — служебное, `media_note` —
рабочая записка, `vizforma` — имя первоосновы, и так далее). Если видимых полей не нашлось
вовсе, он говорит это прямо: «видимых полей не нашлось — и вот где не искали». Проверка, которая
молчит, не отличима от проверки, которой нечего сказать.

**Практическое, если правишь эти поля: ёмкость у них разная, и разница блокирующая.** Подпись
единицы в полосе плашек выросла с 21 до 58 знаков — блокирующих ноль, кегля ниже 12,0 нет.
Та же по смыслу правка в `figure.unit` карточки одного числа (`s105`) дала
`[высота] 0,96" > 0,64"` при 16,0 пт: строка там короче, чем кажется, и лечится только
сокращением. Проверять пересборкой кадра, а не на глаз.

**Класс:** тот же, что `[#229-9]`–`[#229-14]` — отчёт инструмента расходится с состоянием, и
расхождение молчит. Проверке нужен отрицательный результат, который видно: у извлекателя это
список полей, которые он НЕ смотрит, напечатанный рядом с нулём.


## [#229-16] Перечень полей видимого слоя поддерживался руками — и отставал от ядра

**Вывод, собранный из четырёх случаев за два дня** (решение О17, issue #229). Проход по
«видимому слою» не читал `media_caption`, `headline_number`, `figure.*` и
`scheme.unit/base/marks` — все четыре поля **видит зал**. Это уже не частный промах сторожа:
поле «видимый слой» определялось **перечислением**, а перечисление отставало от ядра.

**Правило:** перечень полей видимого слоя обязан собираться из того, **что рисует сборщик**, а
не поддерживаться руками — иначе каждая новая форма в ядре открывает новую слепую зону.

**И обратная половина того же правила, замеренная в тот же час: поле из перечня может не
рисоваться вовсе.** `media_caption` выводится ТОЛЬКО при `media_hero: true`, и уходит не под
картинку, а последним сегментом строки источника в подвале (`build_lec07.py:275` и `:327`,
`deckkit/media.py:309`). На `s106` (боковая иллюстрация, `media_hero` нет) подпись в файле
стояла, а на экране её не было никогда: снятие тринадцати слов не изменило вес страницы
(102 → 102), и дорендерный снимок подтверждает пустое место под картинкой. То есть по одному
полю одновременно верны оба: **проход его не читает** и **сборщик его местами не рисует**.
Вывод для проверки: «поле есть» и «зал это видит» — разные утверждения, и решать надо по
рендеру, а не по наличию ключа.

**Отсюда — конфликт двух правил, который этим и вскрылся.** `tools/presentation-build`
§5.9 требует у обязательного hero ВИДИМОЙ подписи об источнике, и `deckkit/media.py:318`
предупреждает `[кадр] … обязательный hero без поля media_caption`. А `CLAUDE.md` § «Форма
подачи слайда» (решение владельца 2026-10-08) говорит: «Источники фотографий на слайде не
подписывать». На hero-кадре эти два правила противоположны, и сторож исполняет **отменённое**.
Это ровно анти-паттерн `CLAUDE.md` §8.3: «Отменил правило — поправь сторож в том же круге,
иначе сторож возвращает снятое». Снятие подписи с hero-кадра (`s01`, `s105`) без правки
`media.py` даст предупреждение на каждой сборке.

**Класс:** тот же, что `[#229-9]`–`[#229-15]`.

## [#229-18] `measure_body.py` не патчит ветку ДВУХ КОЛОНОК — и такие кадры в замер не попадают вовсе

**Что наблюдалось (2026-10-15, Лекция 7, #229).** Исполнитель мерил кегль тела по семи своим
кадрам и получил **три строки вместо семи**. Четыре недостающих кадра не «показали плохой
результат» — их в выводе **не было**.

**Причина.** `measure_body.py` подменяет четыре функции подбора кегля: `metrics.fit_runs`,
`flow.fit_blocks`, `wrap.fit_runs_wrap`, `wrap.fit_pushed`. **`twocol.fit_two` среди них нет.**
Кадр, чьё тело набрано в две колонки, через подменённые функции не проходит — и в таблицу не
попадает. Прогон при этом не падает и ничего не говорит.

**Как обнаружено, и это главное в записи:** исполнитель **знал, сколько строк ждёт**. Сработало
сравнение ожидаемого с полученным, а не чтение вывода. Читатель, не знающий числа своих кадров,
прочтёт короткий список как «эти кадры померены», а не как «эти четыре я не смотрел».

**Класс:** третий случай подряд за круг — `headline_number` (`[#229-15]`), `media_caption`
(`[#229-16]`), теперь `twocol`. Общее: **прогон молчит о том, чего не смотрел, и молчание
читается как чистота.**

**Лечение, выбранное из двух.** Не «добавить `twocol.fit_two` в подмены» (закроет этот случай и
промолчит о следующей ветке), а **печатать рядом с результатом «кадров в деке N, в замер попало
M»** — тогда следующая невидимая ветка объявляется сама, без того, чтобы кто-то заранее знал
ожидаемое число. Записано как работа; в круге #229 не сделано.

---

## [#241-1] Российские правовые базы отдают заглушку всем не-браузерным клиентам

**Дата:** 2026-10-17 · **Инструменты:** `curl`, WebFetch · **Статус:** обход не найден

**Что происходит.** Проверка нормы приказа Минздрава №2н (когда клинические испытания
заменяются «анализом и оценкой клинических данных») не прошла ни по одному из пяти маршрутов:

| Маршрут | Ответ |
|---|---|
| `base.garant.ru/70291692` (ПП 1416) | HTTP 200, 236 КБ — **ни одного ключевого слова в тексте** |
| `base.garant.ru/70578592` (приказ 2н) | HTTP 404, при этом 45 КБ тела |
| `consultant.ru/document/cons_doc_LAW_158640` | HTTP 200, но текста всего 3 379 знаков — заглушка |
| `normativ.kontur.ru` | HTTP 200, 8 КБ — заглушка |
| `pravo.gov.ru/proxy/ips` | HTTP 000 — соединение не установилось |
| `docs.cntd.ru` | HTTP 000 |

**Ловушка, которая здесь опаснее отказа:** `HTTP 200` с большим телом выглядит как успех.
Гарант отдал 236 КБ, и наивная проверка «код 200, размер приличный» прошла бы — но в этих
236 КБ нет ни слова «аналог», ни «клинических данных». То есть **отказ замаскирован под
успешную загрузку**, и поймать его можно только проверкой на присутствие ожидаемого содержания,
а не на код ответа и размер.

**Как применять.** Утверждение о российской правовой норме не считать проверенным по этим
источникам, даже при HTTP 200. Проверять наличием ожидаемых ключевых слов в тексте. Рабочие
альтернативы для РФ, подтверждённые в этом же проходе: `zakonrf.info` (отдал полный текст
НК РФ ст. 333.32.2 — все семь сумм пошлин), `medvestnik.ru`, `kommersant.ru`, `meditex.ru`,
`zdrav.expert`, `pravo.ppt.ru`.

**Отдельно:** реестр ЕАЭС (`eec.eaeunion.org`) недоступен не по отказу, а по устройству —
Angular SPA отдаёт идентичную заглушку на любой путь. Это проверено экспериментом с перебором
вариантов API-пути, а не предположено.

## [#270-1] `WebFetch` не вскрывает PDF регулятора, отданный как сжатый/бинарный поток

**Дата:** 2026-10-17 · **Инструмент:** `WebFetch` · **Статус:** обход не найден, активно

**Что происходит.** Поиск инженерных деталей допуска IDx-DR/LumineticsCore (issue #270,
Раздел 1 главы Лекции 7) требовал текста из двух документов FDA: De Novo-решения
`DEN180001` и последующего `510(k)` `K213037` (обновление классификатора качества снимка
2.1.1→2.3.0). Оба опубикованы на `accessdata.fda.gov` как PDF. `WebFetch` на оба URL не
вернул читаемого текста — содержимое пришло как бинарный/сжатый поток, который инструмент
не распарсил ни на один абзац. В отличие от `[#241-1]` (заглушка при HTTP 200), здесь не
было даже правдоподобной текстовой подделки — просто пустой/нечитаемый результат, что хотя
бы не маскируется под успех.

**Root cause (предположительно).** Те же PDF у FDA часто лежат как сканы или как потоки с
нестандартной кодировкой текстового слоя; `WebFetch` не делает OCR и не скачивает сырой
байтовый поток для внешней обработки — у него нет пути, кроме встроенного текстового
экстрактора.

**Как применять.** Для регуляторных PDF с `accessdata.fda.gov` (и вероятно аналогичных
правительственных PDF-архивов) не считать `WebFetch` исчерпывающей попыткой: если он вернул
пусто или нечитаемо, это не означает «документа там нет» или «по этому вопросу источника не
существует» (см. соседнее правило в `CLAUDE.md` — «источника не существует» по отрицательному
ответу WebFetch/WebSearch без прямого чтения — ложный вывод, §8.7 этого же класса ошибок).
Рабочий обход не найден в этом проходе; следующий шаг — прямой `curl`/скачивание файла и
локальный PDF-парсер (`pdftotext` и т.п.), а не повторный `WebFetch` с другой формулировкой
запроса.

---

### [#285-1] `deep_latin_scan.py` принимает текстовые файлы, а на PDF падает `UnicodeDecodeError` — и это выглядит как «сканер сломан», а не как «подан не тот вход»

**Дата:** 2026-10-19 · **Инструмент:** `tools/presentation-build/deep_latin_scan.py` · **Статус:** обход рабочий, активно

**Что происходит.** Pre-USER-GATE правило §10 (`CLAUDE.md`, «Deep latin-token scan») требует
гонять сканер **по rendered pptx visible body**, и прямое прочтение этого требования ведёт к
`python3 deep_latin_scan.py <раздел>.pdf`. Вызов падает с `UnicodeDecodeError` на первом байте
PDF-заголовка. Ошибка не называет причину — выглядит как поломка сканера, хотя подан просто не
тот вход: скрипт читает файл как текст в UTF-8 и ничего не знает про PDF.

**Root cause.** Сканер — текстовый: открывает путь как обычный файл и ищет латинские токены
регуляркой. Слоя извлечения текста из PDF в нём нет и не предполагалось; требование §10 написано
про содержимое видимого слоя, а не про формат файла, в котором это содержимое лежит.

**Severity:** P2 — не блокирует, но съедает проход и даёт ложный сигнал «инструмент не работает»
на шаге, где сессия как раз проверяет чистоту артефакта.

**Как применять.** Сначала извлечь текстовый слой, потом сканировать:

```bash
pdftotext -layout sec3-vedenie-dokumentatsii.pdf /tmp/sec3_visible.txt
python3 tools/presentation-build/deep_latin_scan.py /tmp/sec3_visible.txt
```

Заметки лектора лежат во втором PDF (`*-notes.pdf`) и извлекаются так же — проверять **оба**,
правило §6.3 требует видимое тело И заметки. На этом разделе итог после извлечения: 18 уникальных
латинских токенов, все — названия журналов и фамилии авторов в ссылках, то есть разрешённый
остаток, а не долг.

**Status:** active (обход дешёвый; добавлять PDF-ветку в сам сканер не стали — решение владельца,
не сессии).

### [#285-1] Ярус 3 добычи изображений: сайты госведомств США из этой среды недоступны

**Когда:** 2026-10-20, круг 2 раздела «Ведение документации» Лекции 7.

**Что произошло.** `images.md` §14 называет фотослужбу Национального института рака США
находкой прошлого круга и советует искать по подписям её собственного каталога. Попытка
открыть каталог напрямую: `visualsonline.cancer.gov` — **имя не разрешается в DNS**
(`curl: (6) Could not resolve host`); `www.nih.gov` — **HTTP 403**. То есть ярус 3 (сайт
ведомства-первоисточника) из этой среды закрыт не по содержанию, а по сети.

**Обход, который работает.** Те же снимки лежат на Викискладе категорией
`Category:Media from National Cancer Institute Visuals Online` — 2 336 файлов, перечисляются
через `list=categorymembers` с `cmlimit=500` и продолжением. То есть ярус 2 покрывает ярус 3
для этого источника целиком.

**Отдельно: `upload.wikimedia.org` отдаёт HTML-ошибку вместо файла**, если у запроса нет
заголовка `Referer`. Симптом обманчив: файл скачивается, `file` показывает «HTML document»,
а `PIL` падает с `UnidentifiedImageError`. Лечится парой заголовков:
`-H "User-Agent: <имя-проекта>/1.0 (<почта>)" -H "Referer: https://commons.wikimedia.org/"`.
Хост `thumb.wikimedia.org`, который возвращает API в поле `thumburl`, в этой среде не
резолвится вовсе — брать `upload.wikimedia.org` и собирать адрес уменьшенной копии руками
(`/wikipedia/commons/thumb/<a>/<ab>/<имя>/<N>px-<имя>`).

## [#274-1] Render-toolchain (LibreOffice/python-pptx): символ ₽ в плотных/мелкокегльных таблицах рендерится отдельным наложенным объектом

**Дата:** 2026-10-20 · **Инструмент:** `tools/seminar-build/` (python-pptx генерация + LibreOffice `--convert-to pdf`) · **Статус:** активно, обход найден

**Что происходит.** Семинар 8 (issue #274), Кейс 3 — после расширения тестового набора в
таблицах/цитатах появились суммы вида «3000₽», «1000–3000₽» в плотных блоках с уменьшенным
кеглем (9–9.5 pt, `ПОДГОНКА`/`НА ДНЕ КЕГЛЯ`). `check_text_overlap_pdf.py` по настоящему
собранному PDF (`soffice --headless --convert-to pdf`, не python-pptx оценка) нашёл 13–14
настоящих наложений текста: символ «₽» рендерится как ОТДЕЛЬНЫЙ текстовый объект, наложенный
на предыдущее слово/число (100% высоты строки — «это две надписи в одном месте»), только в
этих плотных/уменьшенных блоках. В обычных по плотности слайдах (крупнее кегль) та же схема
«число+₽» не встречалась нигде в корпусе курса до этого — ₽ использовался впервые именно в
этих новых слайдах Кейса 3.

**Root cause (предположительно).** `metrics.py` (`has_glyph`, `text_w`) подтверждает, что ₽
ЕСТЬ в основном начертании (и regular, и bold) по собственной проверке инструмента — то есть
проблема не в отсутствии глифа и не ловится существующим стражем `НЕТ ГЛИФА`. Вставка пробела
(обычного и неразрывного) перед ₽ не устранила наложение и один раз даже добавила новое
(`СЛИПЛИСЬ`) — то есть это не кернинг-пара. Похоже на расхождение между шрифтом/метрикой,
которой `metrics.py` оценивает раскладку (для расчёта авто-уменьшения кегля и переносов), и
тем, что фактически подставляет LibreOffice при рендере PDF в этой headless-среде
(`/home/harness/.local/libreoffice-portable/`) — т.е. несовпадение design-time оценки ширины
и render-time рендеринга конкретно для этого относительно нового юникод-символа (U+20BD,
добавлен в Unicode 7.0/2014), в отличие от широко протестированных ASCII/кириллицы.

**Severity:** P2 (не блокирует сборку штатно — находится только прогоном `check_text_overlap_pdf.py`
по настоящему PDF, который требует `soffice`/`pdftoppm`; но даёт реальный видимый дефект на
слайде, если не проверить).

**Workaround.** Не использовать символ «₽» в плотных/мелкокегльных блоках (таблицы на грани
`НА ДНЕ КЕГЛЯ`, уменьшенные цитаты) — писать «руб.» текстом. В некритично плотных местах
символ, вероятно, безопасен (весь остальной курс использует только «руб.»/«рублей» и не
встречал проблемы), но это не проверено отдельно — не доказано, что ₽ безопасен где-либо,
только что видимый дефект воспроизводится именно в плотных местах. **До продолжения
использования символа ₽ в курсе — явно прогонять `check_text_overlap_pdf.py` по настоящему
PDF, не доверять только `build.py`'s собственным предупреждениям** (они этот класс дефекта не
ловят вовсе — `build.py` для этой же колоды показал 0 связанных предупреждений, дефект нашёлся
только отдельным прогоном по PDF).

**Как применять.** Если render-toolchain (`soffice`, `pdftoppm`) доступен в среде (проверить
`/home/harness/.local/lo-portable-env.sh`, не считать `README.md`'s общую оговорку «рендера
нет в этом окружении» окончательной — она устарела для текущей машины/сессии), ОБЯЗАТЕЛЬНО
прогонять `check_text_overlap_pdf.py` и `check_tracks_pdf.py` по настоящему PDF перед гейтом,
а не полагаться только на `build.py`'s текстовую/геометрическую оценку без рендера — это
разные классы проверки, и один не покрывает другой.

---

## [#229-19] Сессия в harness-worktree: нет LibreOffice и нет `gh` — пере-рендер PDF и открытие PR изнутри невозможны

- **Server / feature:** render-toolchain (LibreOffice) + git-surface (`gh` CLI) в окружении сессии, запущенной в harness-worktree (`harness-control-data/.../.worktrees/folder-NNN/...`)
- **Symptom:** два независимых отказа в одной сессии продвижения Лекции 7 в канонический корень:
  1. `libreoffice --headless --convert-to pdf` → `timeout: failed to run command 'libreoffice': No such file or directory`. Ни `libreoffice`, ни `soffice` нет в PATH. Значит **штатная проверка «пересобрался ли дек в те же 96 страниц» внутри такой сессии недоступна** — PPTX собирается (`python-pptx` на месте), а шага PPTX→PDF нет.
  2. `gh pr create` → `gh: command not found`; поиск по всему PATH пуст. При этом **`git push` работает** (stored token через credential helper) — то есть «запушить» можно, а «открыть PR» нельзя, и это легко принять за одну и ту же возможность.
- **Root cause:** образ сессии несёт Python-стек сборки (`python-pptx`, PyMuPDF, ImageMagick), но не несёт офисный пакет и не несёт `gh`. GitHub-MCP harness-control **additive-only by design**: чтение + `github_create_issue` / `github_comment_on_issue`, **verb создания PR в нём отсутствует** (это не бага, а заявленная граница сервера), поэтому обойти отсутствие `gh` через MCP нельзя.
- **Severity:** P1 — не ломает работу, но ломает **проверку** и **выдачу**, если планировать их на эти два инструмента.
- **Workaround:**
  - *Вместо пере-рендера в PDF:* сверять на уровне PPTX. Собрать дек с канонического места (`build(out=..., slides_dir=..., root=...)` — у `build_lec07.py` есть оба параметра, `SLIDES_DIR` script-relative, а `SL='slides'` в `make_deck_yaml.py` **CWD**-relative) и сравнить с лежащим в репо `.pptx` по видимому тексту и заметкам через `python-pptx`. Это сильнее паритета по числу страниц: ловит расхождение содержания, а не только счёт кадров. Страницы переносимого PDF при этом читаются PyMuPDF'ом (`page_count`) без LibreOffice.
  - *Вместо `gh pr create`:* запушить ветку, положить готовое тело PR файлом рядом с материалами круга и передать открытие сессии/владельцу, у кого `gh` есть (`list_sessions` показывает, кто в workspace; `send_message` — запрос). **Токен из credential helper не извлекать** — это прямо запрещено, и MCP-инструменты заявлены как санкционированная замена именно этому.
- **Отдельно, та же сессия — ложное спокойствие от сборки:** `build_lec07.py::build()` **накапливает** предупреждения через `report.warn()`, а печатает их `main()` после `rnd.verify_built()`. Программный вызов `build()` из своего скрипта поэтому даёт **пустой вывод**, и это читается как «0 предупреждений», хотя их 47. Звать `report.blocking()` / `report.other()` явно (и `report.reset()` между прогонами, если сравниваешь два места). Класс тот же, что `[#229-9]`–`[#229-18]`: **молчание инструмента о том, чего он не печатал, неотличимо от чистого результата.**
- **Status:** active
- **Ссылки:** issue #229 (продвижение переделки в канонический корень, 2026-10-21); ветка `lec07-prodvizhenie-v-koren`

## [#293-1] LibreOffice красит гиперссылку своим синим ПОВЕРХ явного цвета прогона — тёмный кадр теряет подвал

- **Server / feature:** render-toolchain (`soffice --convert-to pdf`, через `tools/presentation-build/pptx_to_png.sh`) + `deckkit.prims.text_runs`
- **Symptom:** строка источника кадра-удара `s01_1` (заливка кадра `21295C`, прогон набран `FFFFFF`) на собранной странице вышла **чистым синим** `(0,0,255)`. Замер по пикселям PNG, не на глаз. В пакете при этом записано ровно то, что просили: `<a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>` рядом с `<a:hlinkClick r:id="…"/>` в одном `rPr`.
- **Root cause:** импорт-фильтр LibreOffice вешает на прогон с `hlinkClick` свой символьный стиль «Интернет-ссылка» и берёт цвет из него, игнорируя прямой `solidFill` прогона. Поведение не зависит от порядка установки цвета и ссылки — проверено обоими способами.
- **Severity:** P1. На белых кадрах деки то же самое и происходит (**все** подвальные ссылки Лекции 7 на экране синие, а не `065A82`), просто синий на белом даёт 8,6 : 1 и читается; на `21295C` это 1,57 : 1 — не читается вовсе.
- **Отдельно опасно:** сторож контраста (`deckkit.contrast`) мерит цвет, ЗАПИСАННЫЙ В ПАКЕТ, и по построению этого не видит: он честно показывает 5,42 : 1 для `065A82` на белом и ничего не скажет про экранный синий. То есть измеренная чистота и видимая картинка здесь расходятся молча — класс `[#229-9]`–`[#229-18]`.
- **Workaround (применён):** на тёмном кадре подвал набирается белым и **без** `hlinkClick`; адрес стоит настоящей ссылкой в заметках. Снятие ссылки не молчаливое — сборка печатает `[подвал] <sid>: … БЕЗ гиперссылки (N адресов)`. Код: `build_lec07.udar_footer`, проба `[удар и подвал]` в `selftest_lec07.py` (разностная, по собранному пакету).
- **Чего обход НЕ делает:** не чинит цвет ссылок на белых кадрах — там он останется синим до тех пор, пока кто-нибудь не задаст теме деки собственный `hlink`-цвет (`<a:clrScheme><a:hlink>` в `theme1.xml`). Это настоящая починка, она не сделана и стоит отдельной работы.
- **Status:** active
- **Ссылки:** issue #293 (прожарка сторителлинга, Этап A), ветка `hc/lec07-prozharka-fable-56380373`

## [#293-2] Поправка к [#229-19]: LibreOffice в harness-worktree ЕСТЬ — через `render-env.sh`

- **Symptom прежней записи:** «нет LibreOffice, пере-рендер PDF изнутри такой сессии недоступен». Проверено 2026-10-22 в сессии той же природы (`.worktrees/folder-288/...`): `libreoffice`/`soffice` действительно нет в `PATH` **по умолчанию**, но `source tools/presentation-build/render-env.sh` ставит на `PATH` рабочий `soffice` (`/home/harness/.local/libreoffice-portable/program/soffice`) и `pdftoppm`, а `tools/presentation-build/pptx_to_png.sh` делает это сам. 93-кадровая дека конвертирована и растрирована без единой ошибки.
- **Чем это важно:** `[#229-19]` предлагает «сверять на уровне PPTX вместо рендера» — обход, который на этом хосте не нужен и уводит от визуальной приёмки, то есть от единственной проверки, ловящей «красиво/понятно».
- **Что остаётся верным в [#229-19]:** `gh` по-прежнему нет, PR изнутри не открыть; `build()`, вызванная программно, по-прежнему печатает пустоту (предупреждения печатает `main()`).
- **Status:** `fixed-upstream` для половины про рендер — запись `[#229-19]` читать вместе с этой.
- **Ссылки:** issue #293

## [#293-3] `pol_slov_po_pdf.py` проверяет свежесть PDF КОММИТОМ — пересобранный, но не закоммиченный выпуск читается как устаревший

- **Server / feature:** `library/lectures/lec-07/rework/deck/pol_slov_po_pdf.py` (вес кадра по собранному PDF) + `ocenka.files_for`
- **Symptom (2026-10-22, issue #293, Этап E):** дека пересобрана и пере-рендерена в том же проходе, свежий PDF положен на место выпуска — прогон отказывает: «после сборки этого PDF правлено кадров: 53. Веса относились бы к прошлому состоянию». Отказ ложный: правленые кадры и есть те, из которых этот PDF только что собран.
- **Root cause:** свежесть входа меряется `git log -1 --format=%h -- <pdf>` против `git diff --name-only <sha>..HEAD -- slides/`, то есть **коммитом, которым PDF записан в индекс**. Оракул слеп к пересборке рабочего дерева без коммита. Этап, которому коммитить запрещено нарядом, не может получить от него ни одного верного ответа.
- **Второй отказ, срабатывающий следом:** сверка «страница стоит на своём кадре» идёт через `ocenka.files_for`, а тот берёт заголовок кадра из ПЕРВОГО markdown-заголовка файла. На кадре с пустым разделом «Видимый текст слайда» (диаграмма во весь кадр, удар, кадр-пауза) это даёт «Заметки лектора», и восемь кадров деки объявляются несовпавшими, хотя страницы на своих местах. Тот же класс, что починенный в `slidefile._SEC_VIS` разбор пустого раздела (#293, Этап A), — но во второй, независимой копии читателя.
- **Чего делать НЕ надо:** `PRIYOMKA_MERIT_USTAREVSHEE=1` снимает первый отказ, но печатает «замер идёт по УСТАРЕВШЕМУ PDF» — утверждение, которое в этом случае ложно, и в отчёт оно уедет как признание. Второй отказ этим флагом не снимается вовсе.
- **Workaround (применён):** отдельный прогон `zamer_minut_po_pdf.py` — порядок страниц берётся у самого сборщика (`slidefile.slide_files`, тот же, которым `build()` пишет страницы), сверка идёт по заголовку из ФРОНТМАТТЕРА и только там, где он не пуст, темп и округление те же (122 слова в минуту, шаг 0,05), чтобы два прогона нельзя было сравнить и получить разные ответы. Провенанс входа называется в отчёте словами («пересобрано и пере-рендерено в этом проходе с головы `f16e41c0e` плюс незакоммиченные правки»), а не выводится из индекса.
- **Настоящая починка, которой нет:** свежесть надо мерить СОДЕРЖИМЫМ (хеш собранного пакета против хеша файлов кадров), а не коммитом; разбор заголовка — брать из фронтматтера, а не из первого markdown-заголовка. Обе — отдельная работа.
- **Status:** active
- **Ссылки:** issue #293 (Этап E), ветка `hc/lec07-prozharka-fable-56380373`

---

### [#299-1] `fig_toolkit.node()` молча выносит содержимое за верхний край карточки

- **Tool:** `tools/seminar-build/fig_toolkit.py`, функция `node()`.
- **Symptom:** когда содержимое не помещается в карточку, оно рисуется ВЫШЕ её верхней границы,
  налезая на то, что стоит над ней. **Предупреждения не выдаётся никакого** — ни в выводе
  сборки, ни в логе рисовалки.
- **Как обнаружено:** только просмотром PNG глазами (Семинар 9, схемы слоя 1). Ни один сторож
  этого не ловит: в собранной деке это пиксели, а `build.py` меряет недобор ширины фигуры, а не
  выход содержимого за её рамку.
- **Обход:** после рисования каждой схемы открыть PNG и посмотреть. Самоотчёт генератора
  «нарисовано» к этому дефекту нечувствителен по построению.
- **Статус:** не чинено (вне мандата производства С9). Чинить — добавить в `node()` проверку
  вместимости с предупреждением в `M._WARNINGS`, как это сделано для схем-жанров.

### [#299-2] `fig_toolkit.lock()` рисует закрытый замок открытым

- **Tool:** `tools/seminar-build/fig_toolkit.py`, функция `lock()`.
- **Symptom:** дуга замка заканчивается выше корпуса, поэтому «закрытый» замок визуально читается
  как открытый — то есть означает на схеме ровно противоположное задуманному.
- **Как обнаружено:** Семинар 9, при рисовании схемы Кейса 1 (значок у поля «решение лежит в
  отдельном поле»). Та же геометрическая ошибка была независимо исправлена в локальной копии
  (`padlock` в `rendered/make_figures_common.py` С9) — то есть дефект воспроизводится.
- **Обход:** использовать `padlock` из `library/seminars/sem-09/rendered/make_figures_common.py`
  либо не ставить значок замка вовсе.
- **Статус:** не чинено в общем ките. Чинить — свести `lock()` с рабочей геометрией `padlock`,
  со сверкой уже сданных дек (значок встречается в С7/С8).

---

### [#299-3] Знак рубля «₽» рядом с числом — LibreOffice кладёт его отдельной надписью поверх предыдущей

- **Tool:** `soffice --headless --convert-to pdf` (LibreOffice 26.2.4.2), обнаружено через
  `tools/seminar-build/check_text_overlap_pdf.py` на собранной деке Семинара 9.
- **Symptom:** строка вида `3000 ₽` или `6500 ₽` в PDF-рендере иногда кладёт глиф `₽`
  ОТДЕЛЬНОЙ надписью, перекрывающей конец предыдущей строки той же фразы — `check_text_
  overlap_pdf.py` ловит это как `НАЛОЖЕНИЕ` (две надписи в одном месте). На экране это
  читается как число с посторонней чертой или сдвоенным знаком поверх последней цифры.
- **Непоследовательность, которая исключила простое объяснение.** Из десяти мест деки, где
  встречалось «ЧИСЛО ₽», ровно четыре давали наложение (дивайдер-цитата, сцена-цитата,
  заголовок слайда, ячейка таблицы) и шесть — нет (включая другую таблицу с тем же
  форматом). Непостоянство исключает простую гипотезу «баг всегда»; больше похоже на
  редкий дефект позиционирования при переносе строки/подстановке шрифта конкретно для
  этого символа, не воспроизведённый детерминированно по тексту.
- **Что НЕ помогло:** неразрывный пробел (U+00A0) между числом и `₽` вместо обычного —
  наложение осталось на тех же четырёх местах, только пробел визуально задвоился.
- **Обход, который сработал:** заменить `₽` на слово `рублей`/`рубль` в конкретных местах,
  где наложение воспроизводится. Проверено на всех четырёх местах Семинара 9 — после
  замены `check_text_overlap_pdf.py` даёт 0 наложений, визуально заголовок и цитаты
  чистые. Экономика и числа не меняются, только обозначение валюты — тот же приём, что
  уже используют соседние фразы в тех же файлах («6500 рублей»).
- **Статус:** не чинено на уровне инструмента (вне мандата производства С9, и причина не
  установлена — LibreOffice headless, возможно связано с заменой шрифта для
  нестандартного глифа). Если встретится на следующем занятии — не считать «уже
  известным и безопасным»: непостоянство (4 из 10, не 10 из 10) означает, что и следующее
  появление `₽` нужно гнать через `check_text_overlap_pdf.py`, а не полагаться на память
  о прошлом разборе.

---

### [#299-4] `tools/seminar-build/deck_kit.write_notes` не поддерживал markdown-ссылки — `[текст](url)` печатался буквально со скобками — ПОЧИНЕНО

- **Tool:** `tools/seminar-build/deck_kit.py::write_notes` (заметки докладчика) и
  `deck_kit.py::text_box` (тело кадра), используются `tools/seminar-build/build.py` для
  каждого слайда.
- **Symptom (было):** `write_notes` разбирал только три вида разметки — `` **жирный** ``,
  `` `моноширинный` `` и `*курсив*` (регулярка `_NOTE_RUNS`). Markdown-ссылка
  `[Название](https://...)` не входила ни в один из трёх шаблонов и печаталась в заметках
  докладчика буквально, со скобками и URL в скобках — не становилась гиперссылкой
  (`r:id`/`hlinkClick` в XML не возникал). `text_box` (тело кадра) ссылок не разбирал вовсе
  и к тому же активно ВЫРЕЗАЛ markdown-ссылку до одного видимого текста без адреса
  (`metrics.inline_segments`/`_LINK.sub`) — для тела это было бы потерей адреса молча, не
  просто нечитаемыми скобками.
- **Где поймано:** Кейс 5 Семинара 9 (`n58-k5-razbor.md`), при попытке оформить ссылку на
  источник (Thinking Machines Lab) в заметках по правилу CLAUDE.md «Форма подачи слайда» —
  правило унаследовано из lecture-pipeline (`tools/presentation-build/deckkit/render.py`,
  `markup.py`, там `add_hyperlink`/`r:id` реально реализованы), а seminar-build этой
  функции не имел вовсе.
- **Root cause:** `deckkit` (lecture-pipeline) и `seminar-build` (seminar-pipeline) — два
  независимых модуля без общего кода; гиперссылки были реализованы только в первом.
- **Severity:** было P2 (некликабельный текст, не блокирует сборку) — теперь закрыто.
- **Fix (issue #299, этот круг):** `write_notes` и `text_box` в `deck_kit.py` разбирают
  `[текст](адрес)` и голый `https://…`/`www.…` ДО разбора `**жирный**`/`` `код` ``/
  `*курсив*`, и ставят настоящий `r.hyperlink.address` (новая функция `deck_kit.link_parts`
  — минимально скопирован разбор из `tools/presentation-build/deckkit/markup.py::URL`/
  `MDLINK`/`abs_url`/`link_parts`, не переимпортирован как объект, потому что у `deckkit`
  своя `theme`/`report`-подсистема с относительными импортами; разойдётся — чинить в обоих
  местах). В теле кадра ссылка разбирается только при `rich=True`: `code_card` с
  `markup=False` передаёт `rich=False` нарочно, и адрес внутри кодовой карточки (листинг,
  вывод команды) остаётся литералом — ссылкой не становится, это разметка самого
  показываемого вывода, а не источник.
- **Сторож, которого не было:** `tools/seminar-build/check_hyperlinks_pptx.py` — читает
  прогоны (`run.text`/`run.hyperlink.address`) собранного `.pptx` отдельно в теле и в
  заметках, и `r:id` в XML (как `deckkit/render.py::verify_links` для лекций) отдельно;
  падает (код 1), если нашёлся адрес текстом без гиперссылки. Проверено своей поломкой:
  `--self-test` строит один `.pptx` с адресом, вписанным напрямую в `text_frame`/
  `notes_text_frame` мимо `deck_kit` (ровно старый баг) — сторож находит 2 мёртвых адреса;
  и второй `.pptx`, собранный заново через `K.text_box`/`K.write_notes` — сторож находит 0 и
  видит ровно 3 настоящих `r:id` (1 в теле, 2 в заметках).
- **Проверено по реальной деке Семинара 9:** `python3 build.py --seminar 09 --block n`
  (предпросмотр ВСЕХ 95 слайдов в `sem-09-n.pptx`, не трогает `deck.yaml`/`sem-09.pptx`) +
  `check_hyperlinks_pptx.py sem-09-n.pptx` → адресов текстом 0, гиперссылок 1 (заметки n58),
  мёртвых 0 — и то же самое ДО фикса источника (`git stash` на правку n58) даёт 0
  гиперссылок при 0 найденных адресов: единственный реальный адрес в заметках всей деки был
  уже лишён схемы (`thinkingmachines.ai/blog/…` без `http(s)://`) силой прежнего
  workaround'а и поэтому не опознавался ДАЖЕ регулярным выражением как адрес — не только
  как ссылка. Восстановлена markdown-ссылка с полной схемой в `n58-k5-razbor.md`; факт/текст
  источника не менялись, адрес проверен `curl` (200).
- **Важная поправка к постановке issue #299:** заявленные «276 адресов в заметках, 0
  гиперссылок» — артефакт измерения, не факт о деке. 92 заметки × 3 `xmlns:*="http://
  schemas.openxmlformats.org/…"` в объявлении корня КАЖДОГО `notesSlideN.xml` = 276; это
  совпадение чисел проверено (`92 × 3 = 276`) и воспроизведено отдельным прогоном — исходный
  замер, видимо, считал подстроку `http` по сырому XML-файлу целиком, а не по `<a:t>`.
  Реальных адресов текстом в собранной деке на момент находки было 0 (после фикса — 0
  мёртвых, 1 настоящая ссылка). Это не повод не чинить инструмент — пробел был настоящим и
  описан выше, — но масштаб «276» в постановке неверен, и дальнейшим читателям тикета не
  стоит ему доверять.
- **Status:** `fixed`. Остаётся отдельным инструментом от `deckkit` (lecture-pipeline) по
  архитектурному решению этого круга (копия, не импорт пакета) — см. причину в комментарии
  `deck_kit.py` над `link_parts`.

---

### [#303-1] Узел `chainLlm` в n8n не отдаёт `usage` — метрики кэша и стоимости вызова через него не измеримы вообще

- **Tool:** n8n, узел `@n8n/n8n-nodes-langchain.chainLlm` (typeVersion 1.4), связка с
  `@n8n/n8n-nodes-langchain.lmChatOpenRouter`. Обнаружено на перепрогоне замера кэша
  Кейса 2 Семинара 9 (issue #303).
- **Symptom:** наружу узел отдаёт только `text` ответа; в `runData` по узлу есть
  `executionTime` и больше ничего количественного. Поля `usage` ответа провайдера —
  `prompt_tokens`, `completion_tokens`, `cost`, `prompt_tokens_details.cached_tokens`,
  `prompt_tokens_details.cache_write_tokens`, `cost_details`, `cache_discount` — через этот
  узел не доходят ни до выхода узла, ни до `GET /executions/<id>?includeData=true`.
- **Severity:** P1 для любого замера, где измеряется цена, расход токенов или кэш. Для
  замеров качества ответа (верно/неверно) узел годится и ограничением не задет.
- **Чем это опасно именно здесь — не ошибкой, а правдоподобной подменой.** Под рукой
  остаётся `executionTime`, и замер естественно съезжает на латентность: «кэш должен
  ускорять, померим время». Латентность через посредника определяется сетью, очередью и
  загрузкой исполнителя, попадание в кэш в ней не различимо даже когда оно есть. Прежний
  замер (`library/seminars/sem-09/stend/zamery-k2/README.md`, направление A) так и получил
  «эффекта кэша не измерено, направление даже обратное ожидаемому» — вывод честный по
  собранным числам и ни о чём по сути. Отрицательный результат на непригодном приборе
  выглядит как содержательная находка, и именно поэтому он дороже обычной ошибки.
- **Workaround (сработал):** вызывать провайдера сырым HTTP-узлом
  `n8n-nodes-base.httpRequest` (typeVersion 4.2) на `POST
  https://openrouter.ai/api/v1/chat/completions`, тело собирать на python-стороне,
  читать полный ответ из execution. Ключ при этом через свой процесс не проходит:
  `authentication: predefinedCredentialType` + `nodeCredentialType: openRouterApi`, n8n
  подставляет его на своей стороне. Рабочий образец —
  `library/seminars/sem-09/stend/zamery-k2-kesh/kesh_stend.py` (сценарий `s9-k2-kesh`),
  он же даёт `options.response.response.neverError: true`, чтобы тело ошибки провайдера
  возвращалось, а не терялось в падении узла.
- **Побочное:** поставить `cache_control`, закрепить исполнителя (`provider.order` +
  `allow_fallbacks: false`) или задать `max_tokens` через `chainLlm`/`lmChatOpenRouter`
  тоже нельзя — у узла нет этих параметров. Сырой HTTP-узел закрывает и это.
- **Статус:** `active` (ограничение узла, не баг). Правило на будущее: **замер, в котором
  есть слово «стоимость», «токены» или «кэш», через `chainLlm` не ставить** — сначала
  проверить, доходит ли нужное поле до execution, и только потом строить серию.
- **Ссылки:** issue #303; протокол замера —
  `library/seminars/sem-09/stend/zamery-k2-kesh/README.md`.
