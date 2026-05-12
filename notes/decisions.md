# Decisions Log

## 2026-03-31 — Initial architecture

- Runtime: Claude Code only, no separate backend
- MCP stack: workspace-mcp (primary Google) + gws (fallback) + knowledge-rag + drawio-mcp + draw-mcp + github-mcp + oxigraph
- Ontology: minimal RDF with 8 entity types and 7 relation types
- Workflow: issue-driven, create-roast-revise cycle
- Priority: speed to working state over feature completeness

## 2026-03-31 — First session findings

### MCP configuration
- MCP servers register via `claude mcp add` → `.mcp.json` (NOT `.claude/settings.json`)
- `.mcp.json` contains secrets → must be gitignored
- `.claude/settings.json` is for non-secret configs only (document-loader, local-rag, drawio, open-ontologies)
- Each restart needed after config changes for MCP tools to appear

### Actual MCP stack (updated)
- workspace-mcp v3.2.0 (115 tools) — primary Google layer, OAuth with kzlevko@gmail.com
- github-mcp-server v0.32.0 (41 tools) — binary at ~/.local/bin, needs PAT
- awslabs.document-loader-mcp-server v3.2.0 (3 tools) — reads XLSX/PPTX/DOCX/PDF/images
- mcp-local-rag v1.0.0 (6 tools) — semantic search, hybrid mode
- @drawio/mcp v1.0.0 (3 tools) — Mermaid/XML/CSV diagrams
- open-ontologies v1.1.1 (43 tools) — replaces planned mcp-server-oxigraph, much richer

### Conventions discovered
- Always save raw exported docs to catalog/exports/docs/ BEFORE ingesting into RAG
- Always save .drawio files to diagrams/ — never just open in browser
- Never use curl/python workarounds for MCP — restart Claude Code for native access
- Work with real files from Google Drive, not synthetic test data
- Subagents cannot use WebSearch/WebFetch — do web research in main conversation

### Top priority: sync pipeline
- No automated Google Drive → local export → RAG ingest flow yet
- This is the #1 blocker for daily operations
- Needs: sync-library skill implementation

## 2026-03-31 — Ontology visualization

- Primary tool: pyvis (Python) → standalone interactive HTML
- OntoSpy broken on Python 3.12
- WebVOWL for one-off schema views
- draw.io for presentation-quality static diagrams
- Pyvis script at scripts/viz-ontology.py (to be created)
- Output to catalog/exports/viz/ontology-graph.html

## 2026-04-07: Knowledge Architecture Complete (#17)

**Decision:** Implemented 4-tier hybrid retrieval (Wiki → Ontology → RAG → Grep) with wiki compilation, ontology concepts, and automated validation.

**Results:** Manual tests show 7.6x reduction in tool calls (53→7) with perfect recall across all 3 scenarios. Wiki and Ontology are the primary tiers; RAG useful for paper discovery; Grep demoted to fallback.

**Key findings:**
- Wiki index is the best entry point for navigational queries (2 reads for full chain)
- Ontology concepts enable structured SPARQL queries (9/9 taxonomies, 8/8 agent categories)
- RAG cross-lingual gap: embedding model can't bridge RU→EN, compensate with bilingual queries
- Pre-commit hook + Post-Compile phase automate mechanical validation and indexing

**Open items:** 16 lecture pages not yet compiled, concept creation not owned by a skill.

## 2026-04-07: Publication storage format (#36)

**Decision:** Publications live in `publications/` directory with `drafts/` and `published/` subdirectories. Organized by work (each publication is a folder), not by target type.

**Structure:**
- `publications/drafts/{slug}/` — one folder per publication with: outline.md, draft-vN.md, article-ru.md, article-en.md
- `publications/drafts/{slug}/assets/` — images, diagrams, screenshots for the publication
- `publications/published/` — final versions copied here after publication
- Template at `templates/publication.md` with YAML frontmatter (title, slug, date, status, targets, tags, lang, published_urls, pair_slug)

**Rationale:**
- One publication can be published to multiple targets (blog, LinkedIn, journal, Habr), so organizing by target type creates false hierarchy
- The `targets` field in frontmatter specifies where the publication gets published; `published_urls` tracks published locations
- Slug-based folders keep bilingual pairs (RU + EN) together with their assets
- Frontmatter enables future automation (status tracking, multi-target publishing)
- Drafts vs published separation mirrors the editorial workflow
- Top-level `publications/` keeps article content separate from course materials (`library/`, `catalog/`)

## 2026-04-07: WordPress publishing mechanism (#39)

**Decision:** Use WordPress.com REST API v1.1 with OAuth2 bearer token for publishing articles from the repo to https://tellian.io/.

**Key findings:**
- tellian.io is WordPress.com hosted (not self-hosted), theme TwentySixteen
- The standard `/wp-json/` REST API is not available (404); must use WordPress.com API v1.1 at `public-api.wordpress.com`
- Bilingual posts use manual in-post structure: two `<div class="lang-block">` sections (EN default, RU), not a multilingual plugin
- WordPress.com built-in MCP is read-only — cannot create posts, only read analytics
- AI Engine MCP plugin requires Business plan upgrade ($33/mo) to install plugins — overkill
- OAuth2 password grant flow works from CLI without browser interaction

**Approach:** Shell script (`scripts/publish-to-wp.sh`) that converts MD to HTML via pandoc, wraps in bilingual div structure, POSTs via API. Future Claude Code skill to orchestrate.

**Setup required:** Register OAuth2 app at developer.wordpress.com/apps, get bearer token, store in `.env` (gitignored).

**Research:** `notes/research/wordpress-publishing-research.md`

## 2026-04-29 — workspace-mcp OAuth refresh expiry (#49)

**Симптом:** все вызовы `workspace-mcp` (Drive/Docs/Sheets/Slides) возвращают `ACTION REQUIRED: Google Authentication Needed`, хотя `claude mcp list` показывает сервер как `✓ Connected`.

**Диагноз:**
- Файл токена `~/.google_workspace_mcp/credentials/kzlevko@gmail.com.json` существует, имеет `refresh_token` и 39 scopes.
- `expiry` access_token: `2026-03-31T16:30:56` (т.е. протух 16+ дней назад).
- Refresh не сработал — Google отозвал refresh_token. Причина: OAuth-приложение в Google Cloud Console находится в **Testing** publishing status, в этом режиме refresh_token автоматически отзывается через 7 дней неактивности.

**Лечение (разовое):** пройти OAuth-flow заново — любой первый вызов `workspace-mcp`-инструмента возвращает auth URL, после клика и согласия в браузере токен пишется обратно в credentials/. Файл `kzlevko@gmail.com.json` обновляется (mtime меняется), последующие вызовы работают.

**Долгосрочный фикс (рекомендуется):** в Google Cloud Console → OAuth consent screen → переключить Publishing status с **Testing** на **In production**. Тогда refresh_token становится бессрочным и не требует ручного обновления каждую неделю.

**Как проверить, что подключение живо:**
```
mcp__workspace-mcp__list_docs_in_folder \
  user_google_email=kzlevko@gmail.com \
  folder_id=1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am
```
Если возвращает список Docs — ок. Если возвращает auth URL — токен снова отвалился, см. «Лечение».

**Не помогает / не нужно:**
- Удалять `kzlevko@gmail.com.json` — НЕ требуется, авто-flow перепишет файл.
- Перезапускать Claude Code — НЕ требуется, MCP-сервер сам подхватывает новые credentials.
- Менять `.mcp.json` — конфиг корректный (`GOOGLE_OAUTH_CLIENT_ID` и `..._SECRET` валидны).

## 2026-05-12 — Presentation pipeline (EPIC #52, sub-issues #53-#56)

**Контекст:** масштабная переработка генерации презентаций. От тонкой обёртки над Google Slides API (TITLE_AND_BODY default) к full repo-first pipeline через PowerPoint MCP + visual-loop + 3 QA-агента + presentation-designer. Пилот — 6 слайдов Лекции 1, 5 итераций v1→v3.6, ~22 часа реальной работы.

### Архитектурные решения

1. **Repo-first source of truth.** `library/lectures/lec-NN/deck.yaml` + `slides/*.md` — единственный источник. Google Drive — только publish target (отложено), не для прямой правки.
2. **Render-target PPTX, не Google Slides.** `office-powerpoint-mcp-server` (GongRzhe, PyPI v2.0.7) через uvx. 37 tools. Архивирован upstream, но стабилен (python-pptx mainline). При нужде форкаем.
3. **Visual-loop — first-class фаза**, не QA-after-thought. Generate→Convert (libreoffice+pdftoppm)→Inspect (Claude vision)→Fix через MCP→Repeat. **Минимум 3 итерации на слайд**, обычно 3-7.
4. **Slide-types library** обязательна. Universal Title+Body — anti-pattern. Каждый слайд имеет тип с конкретным layout-рецептом.
5. **Visual motif** — повторяющийся элемент через весь deck (Anthropic skill principle). У нас — «Ocean rounded box» (radius 12, surface `#F4F7FA`, stroke `#1C7293`).
6. **Палитра локирована.** Ocean Gradient (`#21295C` deep, `#065A82` mid, `#1C7293` light) + Teal `#028090` secondary + Gold `#F0AB00` ≥1×/слайд highlight. Без красного, cream, dark backgrounds (кроме deliberate cover).
7. **Иконки/иллюстрации через локальный workflow.** SVG (Lucide/Heroicons/Phosphor/LobeHub CDN) → ImageMagick recolor → rsvg-convert PNG → manage_image. Никаких URL/SVG в `manage_image` напрямую.
8. **Charts через QuickChart API** (curl + URL-encoded JSON), не PowerPoint MCP native `add_chart` (даёт Office 2010 вид).

### 3 QA-агента (обязательная петля)

- `presentation-critic` — методист + визуальный ревью (vision-enabled, yaml+md+PNG).
- `student-simulator` — студент в зале (PNG + видимые speaker notes).
- `reader-simulator` — 2 режима: `text-only` (md без рендера — методический контроль ДО рендера) и `rendered` (PNG+notes через 2 недели после лекции).

Запускать **параллельно после рендера** на стабильной версии, синтезировать в SYNTHESIS.md, делать fix-итерации.

### Anti-patterns catalog (из пилота #55)

| # | Anti-pattern | Чем заменить | Источник |
|---|---|---|---|
| 1 | Accent lines под titles | Whitespace или background slab | Anthropic pptx skill — «AI-tell» |
| 2 | Red on cream / corporate 2003 | Ocean Gradient + Teal + Gold | пилот v2 |
| 3 | Centered body text везде | Body left-aligned, только titles центрировать | Anthropic |
| 4 | Repeating identical layouts | Каждый слайд distinct visual approach | Anthropic |
| 5 | Generic blue / monochrome | 2-3 уровня + 1 secondary + sparingly gold | пилот v3 |
| 6 | Text-only slides | ≥1 визуал (icon/chart/diagram/illustration) на слайде | пилот v1→v3 |
| 7 | Familiar CTA tone («УГАДАЙ», «ты») | Уважительная «вы»-форма, нейтрально | пилот v3.6 |
| 8 | Local audience binding («инженер ИУ6») | Обезличить (инженер, выпускник, без курсо-зависимости) | пилот v3.6 |
| 9 | Methodist comments на слайдах (footers с D8/refs) | Перенести в speaker notes | пилот v3.6 |
| 10 | Magic-pill framing («за 75 минут разберёмся») | Exploratory navigation tone | пилот v3.6 |
| 11 | Native `add_chart` PowerPoint MCP | QuickChart API → PNG → manage_image | пилот v3 |
| 12 | URL/SVG в `manage_image` напрямую | rsvg-convert → локальный PNG | MCP limitation [#55-1] |
| 13 | Dark cover в light deck | Coherent palette: cover same family as content | пилот v2→v3 |
| 14 | Footer-tax (5 типов мелкого курсива) | 1 общий стиль, max 2 строки, только источники | пилот v3 designer self-review |
| 15 | Cover как ещё один content slide | Distinct typography + composition (tinted bg, big lecture number, no motif callout) | пилот v3.6 |

### Anthropic pptx skill discovery (важное!)

В ходе #55 нашли официальный **Anthropic pptx skill** в `github.com/anthropics/skills` — содержит 10 проверенных палитр с HEX, явный список anti-patterns (включая «NEVER accent lines under titles»), Generate→Convert→Inspect→Fix loop как канон.

**Skill сам не используем** (он на PptxGenJS, у нас PowerPoint MCP), но **знания инкорпорированы** в `.claude/agents/presentation-designer.md` и `tools/presentation-build/README.md`.

### Инструменты установлены (system-level)

- `libreoffice-impress` + `libreoffice-core` + `poppler-utils` (PPTX→PDF→PNG snapshot pipeline).
- `imagemagick` + `librsvg2-bin` (SVG icon recolor + resize).
- `@mermaid-js/mermaid-cli` npm global (`mmdc`) — для диаграмм при нужде.

### PowerPoint MCP limitations (5 новых из пилота — см. `notes/mcp-limitations.md`)

`[#54-1]` нет list_shapes/get_shape_properties · `[#54-2]` format_runs ломает inline runs · `[#54-3]` нет update_shape_position (каждая итерация = full rebuild) · `[#54-4]` vertical_alignment middle неполный · `[#55-1]` 4:3 default — нужен python-pptx post-process для 16:9 · `[#55-2]` `add_slide background_type=solid` не работает — XML inject · `[#55-3]` inline runs (часть текста другим цветом) недоступны через MCP.

### Цикл итераций пилота (важный урок)

| Версия | Главная проблема | Метод обнаружения |
|---|---|---|
| v1 | TITLE_AND_BODY default — corporate 2003 | User жёсткая критика |
| v2 | Монохромно, accent lines, dark cover, дубль question, factual error на chart | Critic + student + reader + designer self-review (4 параллельных agents) |
| v3 | Visual bugs (donut overlap, chip wraps, funnel overflow), tone issues | Orchestrator vision (мой собственный осмотр) |
| v3.5 | Tone/content issues (фамильярный CTA, ИУ6 binding, magic-pill) | User content review |
| v3.6 | Acceptable for publication | Visual + content + tone все ОК |

**Урок:** Anthropic правило «Assume there are problems. Your job is to find them. A first render without issues indicates insufficient scrutiny» — буквально работает. 5 итераций реально нужны.

### Что в #56 стабилизуется

- `/build-deck` skill переписывается под новый pipeline (PowerPoint MCP + visual-loop + 3 QA + designer).
- `tools/presentation-build/README.md` финализируется — slide-types библиотека до 8+ типов с конкретными рецептами.
- Старая Google Slides Лекции 1 удаляется из Drive.
- `deck-editor` agent либо удаляется (orchestration через skill достаточна), либо repurposed под deck.yaml maintenance.
- CLAUDE.md presentation pipeline block финализируется.
