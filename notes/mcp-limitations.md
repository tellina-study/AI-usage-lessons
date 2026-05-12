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

При обнаружении новой limitation — добавить запись по шаблону, обновить дату «Last update» ниже, упомянуть в commit message: `Add MCP limitation #X (server) — see notes/mcp-limitations.md`.

---

**Last update:** 2026-05-12 (#60 — централизация каталога; добавлены 5 powerpoint, 2 workspace-mcp, 1 github, 1 local-rag, 1 render-toolchain).
