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

**Last update:** 2026-08-30 (notes-PDF rewrite — добавлен [#170-4b]: `notes_pages_pdf.py` переписан по owner-спеке — ноты/заголовки читаются из PPTX (URL вернулись), матч слайд↔нота позиционный, футер = номер страницы, continuation без «продолжение»; supersedes match-по-.md из [#170-4]/[#170-4a]/[#171-1]. Ранее: #171 — [#171-1] build-order mismatch + wrapper, [#171-2] anchor-driven [N]-инъекция; #170 — [#170-4] notes-pages PDF builder, [#170-3] надстрочные [N] через run-split lxml).

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
