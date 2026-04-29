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
