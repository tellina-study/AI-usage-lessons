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
- **Status:** active.
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
