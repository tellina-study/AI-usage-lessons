# Phase E — Глубокий research: PowerPoint MCP после архивации GongRzhe

**Issue:** #52
**Дата:** 2026-05-12
**Контекст:** дополнение к `phase-e-tool-research.md`. Пользователь спросил: «почему берём архивный GongRzhe? Поисследуй причину архивации и есть ли что-то объективно сильнее живое». Это глубокая ревизия именно по PowerPoint MCP, без повторения общего сравнения форматов.

---

## 1. Почему GongRzhe архивирован

### Факты
- `GongRzhe/Office-PowerPoint-MCP-Server` — заархивирован **2026-03-03**, баннер «archived by the owner». **1700 stars, 228 forks, 27 open issues** на момент архивации.
- Последний коммит — **2025-12-31** (v2.0.7, bump version, добавлены MCP tool annotations).
- В README **никакого explicit deprecation notice или объяснения** причины. Архивация без прощального сообщения.

### Главная находка: это массовая архивация всего портфеля GongRzhe
Запрос `gh api users/GongRzhe/repos --paginate` показывает: **из 22 публичных репо у GongRzhe — 20 заархивированы**. Активны только два мелких: `Figma-Context-MCP` (1 star, форк) и `remote-mcp-server-with-auth` (1 star). Заархивировано в том же марте 2026:

| Репо | Stars | Last commit |
|---|---|---|
| Office-Word-MCP-Server | 1949 | 2025-12-31 |
| Office-PowerPoint-MCP-Server | 1700 | 2025-12-31 |
| Gmail-MCP-Server | 1110 | 2025-08-06 |
| Human-In-the-Loop-MCP-Server | 160 | 2025-06-18 |
| Quickchart-MCP-Server | 160 | 2025-05-13 |
| MCP-Server-Creator | 40 | 2025-06-18 |
| Office-Visio-MCP-Server | 55 | 2025-05-14 |
| opencv-mcp-server | 103 | 2025-09-11 |
| ...и ещё 12 |

**Интерпретация:** автор массово свернул сопровождение всего MCP-портфеля (выгорание, смена работы, переключение на другие проекты — но это домыслы; публичного блог-поста или Twitter-анонса с объяснением я не нашёл, поиски `GongRzhe + announcement` ничего конкретного не дают). Это **не deprecation в пользу official-сервера** — официального M365 PowerPoint MCP с эквивалентным API не существует (см. §3).

### Что это значит для нас
- Код **функциональный, стабильный, последняя версия 2.0.7 от 2025-12-31** — не сырая разработка, а прошедший несколько итераций релиз. Issues #39 «unstable when generating presentations» и #41 «can randomly die» — есть, но из 27 open issues большинство — feature requests и UX-баги, а не критические крэши.
- Под капотом — `python-pptx` (Microsoft-supported, MIT, 2.5k stars, regular releases). Это значит **capability slice стабилен**: что умеет python-pptx, то умеет MCP.
- **Форк есть смысл**, если нужна доработка. Уже есть **15+ публичных форков**, самый свежий — `S1ang0/Customized-Office-PowerPoint-MCP-Server` (2026-05-11, добавляет morphing transitions). Также на PyPI есть `mseep-office-powerpoint-mcp-server` (mseep делает аудит и переупаковку MCP-серверов; что именно они меняют — не подтверждено через WebFetch).

**Вывод:** архивация — это сигнал «не будет новых фич», но **не сигнал «код сломан»**. Риск управляемый: форкнуть на свой org займёт час.

---

## 2. Сравнительная таблица живых альтернатив

Все Linux-friendly Python-сервера на python-pptx (COM-based решения вычеркнуты — см. §3). Stars, дата последнего коммита, количество tools, состояние shape-API на 2026-05-12.

| Сервер | Stars | Last commit | Tools | Shape primitives | Connectors | Slide masters | Reference template | Inspect API |
|---|---|---|---|---|---|---|---|---|
| **GongRzhe (архив)** | 1700 | 2025-12-31 | **32** в 11 модулях | **20+ auto-shapes** (rect, oval, flowchart) | **add_connector** | **manage_slide_masters** | create_presentation_from_template + 25 встроенных | get_presentation_info, get_slide_info, extract_slide_text |
| **charleslukowski/ppt_mcp** | 5 | 2025-07-01 | ~20 | `add_professional_shape` (без явного перечня типов) | НЕТ явно | `create_master_slide_theme`/`apply_master_theme` | `create_template`/`apply_template` | `get_presentation_info`, `extract_text`, `analyze_presentation_style` |
| **ltc6539/mcp-ppt** | 66 | 2025-06-01 | **14** | **НЕТ** (только title/content/section/image/table) | НЕТ | НЕТ | НЕТ | get_presentation_info, get_presentation_outline |
| **supercurses/powerpoint** | 145 | 2025-03-15 | 10 | НЕТ | НЕТ | НЕТ | НЕТ | НЕТ |
| **Ichigo3766/powerpoint-mcp** (форк supercurses) | 53 | 2025-03-27 | 10 | НЕТ | НЕТ | НЕТ | НЕТ | НЕТ |
| **jenstangen1/pptx-xlsx-mcp** | 29 | 2025-03-28 | средне | базовые | НЕТ | НЕТ | НЕТ | базовые |
| **Softeria/ms-365-mcp-server** | 701 | 2026-05-09 | 200+ Graph tools | **PowerPoint функций НЕТ вообще** | — | — | — | — |

### Ключевое:
- **Никто из живых не дотягивает до GongRzhe** по составу шейпов, мастеров и количеству инструментов. Самый функциональный из живых — `charleslukowski`, но и он на ⅔ по фичам и **с июля 2025 коммитов нет** (фактически тоже мёртв, просто без архив-баннера).
- **`ltc6539`** при 66 stars — самый «модный» из живых, но это **slide-builder низкого уровня**: 14 tools, всё крутится вокруг готовых типов слайдов (title/content/image/table). Никаких shape primitives, masters, layouts — ноль возможностей строить process-диаграммы из rect+arrow. **Не подходит.**

---

## 3. Что нашлось «нового» (Microsoft / Aspose / стартапы)

### Официальный Microsoft 365 MCP (Anthropic-blessed)
- В 2026 Microsoft + Anthropic выпустили **«M365 MCP Server for Claude»** — бесшовная интеграция Claude в Word/Excel/PowerPoint Copilot (источник: arcade.dev blog, office365itpros.com). Но это **client-side connector внутри Office Copilot**, не self-hostable MCP-server для агентной сборки PPTX-файлов. Для нашего use-case (Claude Code собирает .pptx из YAML и складывает в Drive) **это не то**.
- **`Softeria/ms-365-mcp-server`** (701 stars, активный, 2026-05-09) — самый популярный третьесторонний M365 MCP. Покрывает Outlook/Excel/OneNote/SharePoint через Graph API. **PowerPoint-функций нет** (Graph API для Slides очень ограничен — только outline/notes, не shapes). **Не финалист.**
- **Arcade.dev MCP for PowerPoint** — коммерческий cloud-сервис, тулы уровня «add slide / set notes / read as markdown». **Никаких shape primitives**. Cloud-only с OAuth, платный. **Не финалист.**

### Aspose.Slides MCP
- Aspose.Slides — мощная коммерческая библиотека (Java/.NET/Python), но **MCP-обёртки для неё нет** (только Aspose.Cells MCP в их собственном каталоге). Лицензия дорогая (от $1199/год dev seat).

### Windows COM-based (мощные, но Windows-only)
- **`ykuwai/ppt-mcp`** (16 stars, 2026-03-31) — **154 tools в 26 категориях**, включая connectors, freeform, masters. Но **требует Windows + установленный PowerPoint** (COM automation). У нас Linux/WSL2. **Не подходит.**
- **`trsdn/mcp-server-ppt`** (25 stars, 2026-03-21) — **204 операции в 33 tools** через .NET COM interop. Те же ограничения. **Не подходит.**

### Slidev/Marp/Gamma/Plus AI MCP
- В 2026 у Gamma, Tome, Beautiful.ai, Plus AI — **нет публичных MCP-серверов**. У Marp/Slidev — нет MCP, только CLI (его и так можно вызывать без MCP).

### Generic python-pptx через mcp-python-runner?
- Идея: вызывать python-pptx напрямую через какой-нибудь generic Python-MCP. Реальных таких серверов с production-качеством нет — `mcp-run-python` от pydantic есть, но он sandboxed и без графики/файловой персистентности для нашего сценария избыточно сложен. Лучше готовый PPTX MCP.

**Итог §3:** ничего объективно сильнее GongRzhe в нашем сегменте (Linux + python-pptx + богатые шейпы + masters) **не появилось**.

---

## 4. Тестирование 6 критичных операций

| Операция | GongRzhe (архив) | charleslukowski | ltc6539 |
|---|---|---|---|
| `add_shape(rect/oval/arrow, x,y,w,h)` | **ДА** — `add_shape` с 20+ MSO_SHAPE типами | частично — `add_professional_shape` (типы не задокументированы) | **НЕТ** |
| `add_connector(start_shape, end_shape)` | **ДА** — `add_connector` | **НЕТ** явно | **НЕТ** |
| `apply_reference_template(template.pptx)` | **ДА** — `create_presentation_from_template` + 25 встроенных + любой свой | частично — `apply_template` (data-driven, не visual reference) | **НЕТ** |
| `update_shape_properties(shape_id, ...)` | **ДА** — через `manage_text`, `manage_image`, `format_table_cell` | через `apply_style_profile` (не на конкретный shape) | **НЕТ** |
| `get_slide_count`, `list_shapes`, `get_shape_properties` | частично — `get_presentation_info`, `get_slide_info`, `extract_slide_text` (нет полноценного list_shapes) | `get_presentation_info` + `extract_text` | `get_presentation_info`, `get_presentation_outline` |
| `create_slide(layout_name)` из reference template | **ДА** — `add_slide` + `apply_slide_template` | **ДА** — `add_slide` с layout selection | частично (только title/content/section/image/table) |

**Победитель по операциям: GongRzhe — 5/6 «полных», 1/6 «частично».**
**charleslukowski: 2/6 полных, 3/6 частично, 1/6 нет.**
**ltc6539: 1/6 полных, 5/6 нет.** Дисквалифицирован для нашей задачи.

Единственный недостаток GongRzhe — нет полноценного `list_shapes`/`get_shape_properties` для итеративных правок. Но **этого нет ни у кого из живых** — это лимит python-pptx-обёрток вообще. Для visual-loop придётся читать PPTX отдельным шагом (`python-pptx` напрямую через короткий Python-скрипт или через `document-loader` MCP).

---

## 5. Финальная рекомендация

### Primary: **GongRzhe/Office-PowerPoint-MCP-Server** (архивный, форкнуть на свой org)

**Обоснование:**
1. **Только он закрывает 5 из 6 критичных операций**, включая connectors, slide masters, reference templates и 20+ shape primitives. Альтернатив этого уровня **нет в природе** на Linux/python-pptx.
2. Архивация — массовая по всему портфелю автора, а не deprecation в пользу лучшего решения. Код стабилен, под капотом mainline `python-pptx`. Риск bus-factor управляется форком.
3. У форкания есть **прецеденты** (15+ публичных форков, S1ang0 с активной разработкой). Ничто не мешает форкнуть `tellina-study/Office-PowerPoint-MCP-Server` и накатывать туда свои патчи (например, `list_shapes`, `get_shape_properties`).
4. Конкуренты на Linux — либо Toy (`ltc6539`), либо тоже неактивный (`charleslukowski`, последний коммит 2025-07-01), либо без shape-API вообще (`supercurses`, `ms-365-mcp-server`).

**План внедрения:**
1. Форкнуть `GongRzhe/Office-PowerPoint-MCP-Server` → `tellina-study/Office-PowerPoint-MCP-Server` (через `gh repo fork`).
2. Установить с PyPI (он там опубликован):
   ```bash
   pip install office-powerpoint-mcp-server==2.0.7
   ```
3. Добавить в `.mcp.json`:
   ```json
   {
     "mcpServers": {
       "powerpoint": {
         "command": "python",
         "args": ["-m", "office_powerpoint_mcp_server"],
         "env": {
           "PPTX_TEMPLATE_DIR": "/home/levko/AI-usage-lessons/templates/pptx"
         }
       }
     }
   }
   ```
4. **Сразу после форка** — добавить в issues нашего форка задачу «add `list_shapes` and `get_shape_properties` tools» (нужно для visual-loop правок). Это +2-3 часа на python-pptx-обёртку.
5. Для PNG-снимков — отдельный шаг через `libreoffice --headless --convert-to png` или `pip install pptxtoimages` (это ортогонально MCP-серверу).

### Backup: **charleslukowski/ppt_mcp** (если форк GongRzhe оказался реально сломан)

**Когда переходить на бэкап:**
- Если на GongRzhe не получится поднять PyPI-пакет на нашей версии Python.
- Если find критический баг, который невозможно быстро запатчить.

**Trade-off:** теряем явные connectors, manage_slide_masters, 25 встроенных шаблонов, гранулярный `add_shape` с 20+ типами. Но получаем `analyze_presentation_style` + `apply_style_profile` (полезно для бренд-консистентности) и `screenshot_slides` (хотя он Windows-only — для нас бесполезен). Этот вариант — **plan B**, не первый выбор.

**Не рассматривать:** `ltc6539` (нет шейпов вообще), `Softeria/ms-365-mcp` (нет PowerPoint), Windows COM-сервера (`ykuwai`, `trsdn`) — несовместимы с Linux.

---

## Источники

GongRzhe и его портфель:
- https://github.com/GongRzhe/Office-PowerPoint-MCP-Server (архивный 2026-03-03, 1700★)
- https://github.com/GongRzhe?tab=repositories (массовая архивация, 20 из 22 репо)
- https://pypi.org/project/office-powerpoint-mcp-server/ (актуальная v2.0.7)
- https://github.com/S1ang0/Customized-Office-PowerPoint-MCP-Server (живой форк, 2026-05-11)

Живые альтернативы (проверено через `gh api repos/...`):
- https://github.com/charleslukowski/ppt_mcp (5★, 2025-07-01)
- https://github.com/ltc6539/mcp-ppt (66★, 2025-06-01)
- https://github.com/supercurses/powerpoint (145★, 2025-03-15)
- https://github.com/Ichigo3766/powerpoint-mcp (53★, 2025-03-27)
- https://github.com/jenstangen1/pptx-xlsx-mcp (29★, 2025-03-28)

Microsoft / Anthropic экосистема:
- https://github.com/softeria/ms-365-mcp-server (701★, активный, без PowerPoint)
- https://www.arcade.dev/blog/microsoft-office-365-mcp-servers-launch/
- https://office365itpros.com/2026/04/08/microsoft-365-connector-for-claude/

Windows COM-based (вычеркнуты — несовместимы с Linux):
- https://github.com/ykuwai/ppt-mcp (16★, 154 tools, COM)
- https://github.com/trsdn/mcp-server-ppt (25★, 204 ops, .NET COM)

Каталоги и обзоры:
- https://mcp.directory/publishers/gongrzhe
- https://mcpservers.org/servers/charleslukowski/ppt_mcp
- https://www.pulsemcp.com/servers (полный реестр MCP)
