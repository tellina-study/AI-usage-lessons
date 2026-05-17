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

## 2026-05-13 — Lec 1 v3.2 Reflection Findings

**Контекст:** day-long production Лекции 1 v3.x — chapter v3.1 (16k слов), slides v3.2 (33 слайда), speech v3.1 (5.1k слов). Все 4 critic agents APPROVE-WITH-MINOR. User вернулся с 23 + 8 + 19 = **62 substantive revisions** across 3 раундах (~50 user fixes).

**Reflections:**
- `notes/reflections/2026-05-13-lec-01-v3-rebuild/REFLECTION.md` — broad, 7 categories, 12 sections.
- `REFLECTION-roast.md` — methodology-critic roast (15 missed failures + 12 unactionable→concretize + 8 risks + 10 extra recommendations).
- `REFLECTION-visual-audit.md` — presentation-critic visual specialist (16 designer self-acceptance fails + 7 schema design patterns + Schema Readability Checklist + No Extra Content Rule + 5-Second Test + 20 visual anti-patterns 16-35).
- `REFLECTION-CONSOLIDATED.md` — implementation plan (16 файлов, 6-8 hours).

### Top failure modes

1. **Critic blind spots** — 4 critics дали APPROVE-WITH-MINOR, но user вернулся 3 раза:
   - Schema readability for laymen (s11/s13/s16/s21 переделывались 5+ iter каждый, user всё равно отверг).
   - Curriculum relevance (Pearl 3 уровня causality / ARC-AGI economics — методически OK, но не для introductory лекции).
   - Terminology drift («Приложение-робот» имел 3 формы across 3 артефакта).
   - Designer-added content без request (тайминг, «вы здесь», «Лектору» секция, subtitle, s14-deletion — 8 designer-added items removed by user).
   - Tools/data freshness (Llama-3 как «свежий пример», ARC-AGI 37.6% устарело за 2 дня к 68.8% / 85%).

2. **Designer self-acceptance** — designer self-checked → declared done → critic missed → user caught. Visual loop self-acceptance threshold = «no defects designer sees» != «no defects student sees from 5-го ряда».

3. **Terminology drift cycle** — chapter v3 «Приложение-робот» (book-editor) → consistency-checker П1 P1 «3 формы» → speech v3.1 unified «в режиме автоматизации» (speech-writer applied critic-suggested form, не original). **Pattern:** critic-driven rename без user approval создаёт drift.

4. **WPM regression** — speech v3.2 final имел s07/s09/s17 на 102-107 WPM, прошли как «8 of 10 ≤97 acceptable». Methodology DoD требует WPM ≤95, никто не поднял.

5. **Visual production process invisible** — 14+ visual loop iterations + 5 параллельных designers за 1 wall-day производства — user explicitly: «много правили визуал, но не вижу в рефлексии».

### Top corrections (per CONSOLIDATED implementation plan)

1. **Pre-USER-GATE Rule** (CLAUDE.md + lecture-production/README.md + build-deck/SKILL.md): orchestrator MUST run pre-review (visual scan + notes read + automated greps) перед каждым USER GATE. «Approve» = «orchestrator reviewed visually + critics approved», NOT «critics approved alone».

2. **Schema Readability Checklist** (presentation-designer.md + presentation-critic.md + presentation-build/README.md): per-subtype checklist для 7 subtypes (matrix/quadrant/timeline/layered/cycle/pipeline/comparison/architecture) + 5-Second Test + Projector Readability (50% zoom).

3. **No Extra Content Rule** (CLAUDE.md + presentation-designer.md + book-editor.md + speech-writer.md): 8 forbidden additions enforced — subtitle / navigation marker / тайминг / «Лектору» секция / decorative SVG / color-only highlight / slide deletion без request / cross-slide bridge text. Improvements REPORTED, не applied.

4. **WPM Hard Rule** (speech-writer.md): любой fragment с WPM > 95 = P0, не submit. Trim content или split slide.

5. **Speaker Notes Contract** (presentation-designer.md + book-editor.md + lecture-production/README.md): 150-300 words readable student text, derived from chapter + speech. FORBIDDEN: layout descriptions, director's cues, лекторские заметки, тайминг.

6. **4-level verdict scale** (all critic agents): REJECT (any P0) / REVISE (5+ P1) / APPROVE-WITH-POLISH (≤4 P1) / APPROVE-CLEAN (0 P1). Counter-check: если ≥5 P1 но verdict APPROVE-WITH-POLISH — STOP, change to REVISE.

7. **Glossary Lock** (CLAUDE.md + consistency-checker.md + lecture-production/README.md): после Phase 4 USER GATE 1 (chapter approved) — orchestrator generates `library/lectures/lec-NN/glossary.yaml`. Critics MAY flag inconsistency, MAY NOT propose rename без USER approval.

8. **Curriculum Relevance Check** (methodology-critic.md): Bloom-level × lecture-level decision matrix. For introductory lectures (L1-3), Evaluate/Create-level concepts → RECOMMEND DELETE.

9. **Tools/Benchmark Freshness Check** (methodology-critic.md + fact-checker.md): per-claim freshness metadata + verify-on-day-of-lecture для weekly-cadence data (AI benchmarks).

10. **Visual Loop Iteration Cap** (presentation-designer.md + presentation-build/README.md): hard cap 7 iterations per slide → escalate to orchestrator с alternatives (simplify / replace / split / delete).

### Anti-patterns 16-35 (extension к pipeline catalog 1-15)

| # | Anti-pattern | Чем заменить | Источник (Lec 1 round/fix) |
|---|---|---|---|
| 16 | «Лектору» секция в speaker notes | Notes — readable student text для self-study; lectorские cues → speech.md | Round 1 #1 + Round 3 #1 |
| 17 | «Вы здесь» текстовый маркер на nav-slides | Visual hierarchy через accent color на active section header (если нужно вообще) | Round 2 #4 + Round 3 designer-extras removal |
| 18 | Тайминг минут на student-visible content | Тайминг → только в speech.md (lecturer-facing) | Round 2 designer-added removal |
| 19 | Designer-added subtitles без request | No Extra Content Rule — designer asks before add | Round 1 #5 designer-added subtitle removal |
| 20 | Schema без start/end indicator (circular cycle) | Gold dot или label «start» + arrow direction explicit | s16 cycle redesigns 3 раза |
| 21 | Matrix <75% fill rate (skeleton accepted) | Each cell ≥1 marker + 1-2 line label; если cell empty — schema choice неверный | s11 v3 matrix iterations |
| 22 | Axis labels вне quadrant как titles | Labels INSIDE quadrant с explicit direction-of-scale arrow | s11/s12 visual-audit findings |
| 23 | Layered model centred (concentric balanced) | Common bottom edge — visual «foundation» feel; deepest layer = largest | s13 layered redesign |
| 24 | Architecture без USER actor | Add user/actor icon — student question «где Я в этой схеме?» | s21 architecture redesign |
| 25 | Cross-slide chart duplication | Pre-final grep на assertions + chart types; consolidate or differentiate | s04 + s17 bar chart duplicate |
| 26 | Mixed RU/EN sub-labels in pipeline | Unified language sub-labels (или RU only, или EN only — не mix) | Round 2 pipeline cleanup |
| 27 | Multi-line event labels через `\n` | Single-line через em-dash («2017 — Transformer paper»); split timeline if dense | s07 timeline 12 events fix |
| 28 | Equal-height boxes для unequal content | Visual mass match content weight; не force grid uniformity | Round 2 visual mass feedback |
| 29 | Inconsistent gold-emphasis across same-tier cards | Single mechanism per signal — color-only OR text marker, не both | Visual-audit redundancy finding |
| 30 | Projector-distance illegibility (<14pt axis) | Hard minimums: title ≥24pt, body ≥18pt, chart axis ≥14pt; 50% zoom test | Round 3 projector readability |
| 31 | Pivot year flat в timeline (same size as other years) | Pivot year ≥2× размер шрифта остальных + gold accent | s07 timeline pivot year fix |
| 32 | filled_rect + rotated_triangle гибрид как стрелки | MSO_SHAPE.RIGHT_ARROW shapes (proper proportions) | Fix-11 Л1 v3.2 |
| 33 | Cards с «4 названия без определений» | Each card 1-2 line definition + assertion-evidence pairing | Round 1 #18 Pearl/causality |
| 34 | Visual loop self-acceptance threshold = «no defects designer sees» | 5-Second Test as final gate: «would student с 5-го ряда понять main message за 5 sec?» | Visual-audit primary content |
| 35 | Schema iteration без questioning concept (s16 cycle 3 designs) | Hard cap 7 iter → escalate с alternatives (simplify / replace / split / delete) | s11/s13/s16/s21 5+ iter каждый |

### Critic blind spots каталог (10 items)

(Полный список с примерами — см. REFLECTION.md §4.1.) Top blind spots:
1. Schema readability for laymen.
2. Curriculum relevance (intro/intermediate/advanced match).
3. Visual centring of charts.
4. Cross-slide redundancy.
5. Term canonical-validity.
6. Tools/benchmark freshness.
7. Designer-added content.
8. Color-only highlights vs text markers.
9. Notes-as-readable-text vs layout descriptions.
10. Title-vs-body assertion alignment.

### Verdict scale recalibration

Old: APPROVE-WITH-MINOR / REJECT (binary-ish).
New: REJECT (any P0) / REVISE (5+ P1) / APPROVE-WITH-POLISH (≤4 P1) / APPROVE-CLEAN (0 P1).
Counter-check enforced в каждом critic agent prompt: если wrote ≥5 P1 но verdict APPROVE-WITH-POLISH — STOP, change to REVISE.

---

## 2026-05-14 — Лекция 2 production lessons

**Контекст:** 12 phases (Phase 0 → Phase 11), 3 USER GATEs, PR #75 merged 2026-05-14. Speech v1.1 + slides v1.7 (36 slides) + chapter v1.2 (11,477 слов) finalized. **5 раундов user feedback на slides** (Phase 8 → 8.5 → 8.6 → 8.7 → 8.8 → 8.9) caught issues that critics didn't.

**Reflection sources:** `notes/reflections/2026-05-14-lec-02-production/REFLECTION.md` + per-area files (improvements / user-feedback / tools / workflow / content).

### Anti-patterns 36-50 (extension к Lec-1 catalog 16-35)

> Disambiguation (merge #77↔#78/#82/#84): нумерация **anti-pattern-каталога** сквозная 16→50 (Lec-1: 16-35, Lec-2 #77: 36-50). Отдельная нумерация «findings 36–43» в секции «2026-05-16 … (#78/#82)» ниже — **независимый** список governance/git-выводов, НЕ продолжение anti-pattern-каталога (совпадение чисел случайно, списки различаются заголовками).

| # | Anti-pattern | Чем заменить | Источник |
|---|---|---|---|
| 36 | `[VERIFY-DAY-OF]` / `[FACT-CHECK]` markers visible в body | Frontmatter + speaker_notes only; pre-render grep enforce 0 hits | L2 R1 Phase 7 P0 (s16, s27) |
| 37 | LO codes (LO1/LO4/LO6/LO7) visible to students в body | Frontmatter `learning_outcomes` only | L2 R1 14 designer-extras |
| 38 | `§X.X` cross-references visible в body | Frontmatter `chapter_ref` only | L2 R1 designer-extras |
| 39 | Forward-refs «→ sNN» / «(см. sNN)» visible | Move to speaker_notes if needed | L2 R1 designer-extras |
| 40 | Top progress bar / navigation bar на каждом content slide | Only on section dividers + cover (Lec-1 pattern) | L2 R2: «нахрена этот хедер сверху везде?» |
| 41 | Missing lecture-map slide | Add s02a-style map after cover | L2 R3: «где слайд с содержанием?» |
| 42 | Missing dedicated Q&A slide | Add standalone Q&A slide (Lec-1 s31 pattern) | L2 R5: «сделай отдельный QA как в лекции 1» |
| 43 | Insufficient section dividers (only 1 of N) | Dividers для ALL major sections | L2 Phase 8.6 +4 dividers |
| 44 | Outdated empirical test as hook (strawberry-type) | 2026-evergreen visualization / cost-asymmetry / concept-reveal | L2 R4 #1: «strawberry test устарел» |
| 45 | Missing fundamental concepts (attention matrix, embedding space, end-to-end flow) | Methodology-critic Missing-Fundamentals check per concept | L2 R4 #7: «механизм же не линейный а матричный» |
| 46 | Insufficient stock illustrations (text-heavy deck) | 5-10 supportive visual assets baseline в designer DoD | L2 R4 #8: «докинь 5-10 картинок» |
| 47 | Artifacts only in temp worktree (not main repo) при GATE | Memory rule [[feedback-pre-gate-render-artifacts]] + pre-USER-GATE sync mandatory | L2: «запрети приходить на ревью слайдов без PPTX и PDF» |
| 48 | Branch contention from parallel session (shared `.git`) | Git worktree isolation mandatory для multi-lecture parallel | L2 7+ branch switches mid-session |
| 49 | Designer making independent decisions diverging от Lec-N-1 pattern | Lec-N-1 reference read MANDATORY at start | L2 R2, R3, R5 все Lec-1 deviations |
| 50 | Per-artifact spawns для polish rounds (separate designer/writer per phase) | Single batched revision agent (Phase 11 pattern) | Phase 11 vs 8.X sub-iterations efficiency |

### Lec-N-1 pattern compliance — new check category (3 agent layers)

After Лекция 1 production stabilized как canonical reference — all subsequent lectures должны pattern-match **unless explicit divergence approved**. 3 enforcement layers:

1. **methodology-critic** — Lec-N-1 Pattern Compliance Check (plan + slides critique).
2. **presentation-designer** — Lec-N-1 Reference Read MANDATORY at start.
3. **presentation-critic** — Lec-N-1 Pattern Compliance Check (visual perspective).

### Hook engagement quality — new check category

Hook (s01) is methodologically subjective beyond «is it correct?». Methodology-critic Hook Engagement Quality Check criteria:
- Time-evergreen (12 month stability)
- Emotionally engaging (surprise / curiosity / dissonance)
- «Висит на экране» worthy (visual richness)
- Connected to lecture assertion
- Counter-example check vs Lec-1 s01

### Missing-fundamentals check — new check category

Critics check what IS present; rarely check what's ABSENT. Per-concept checks:
- **Attention:** matrix nature? N×N cost? multi-head?
- **Embeddings:** vector space before similarity? dimensions? training?
- **Tokenization:** end-to-end flow? BPE compromise?
- **Sampling:** distribution → token explicit?

### Critic blind spots catalog (расширен 10 → 15)

Original Lec-1 list + 5 new from L2:

11. Hook engagement quality (correctness ≠ hook).
12. Lec-N-1 pattern compliance (designer independent decisions).
13. Missing-fundamental concepts (matrix nature, vector space, end-to-end flow).
14. Artifacts main-repo sync (worktree-only at GATE).
15. Branch contention в parallel sessions (shared `.git`).

### Batched revision pattern (Phase 11)

Phase 11 demonstrated single speech-writer agent doing 3-artifact touches (chapter + slides + speech) в 40 min closing 6/6 P1 + 9/16 P2. **5-10× more efficient than per-artifact spawns.** For polish rounds — single batched revision agent recommended.

## 2026-05-16 — Fundamental rule ≥30% failure-content + branch hygiene (#78/#82)

Рефлексия: `notes/reflections/2026-05-16-failure-content-rule/`.

### Governance / методика (findings 36–38, 43)

| # | Урок | Применение |
|---|---|---|
| 36 | Бриф субагентов, выведенный из спеки/правила, нельзя запускать до фиксации спеки | Спеку-чекпойнт ДО спавна параллельных агентов (lock rule → потом запуск критиков) |
| 37 | Измеримое правило без определения метода подсчёта → критики разъезжаются | В момент фиксации measurable-правила определить: что считается, что нет, как считать смешанное (partial). Якорь: 3 критика изобрели weighted vs strict-in |
| 38 | ENFORCED governance-правило без escape hatch → тихое нарушение или ненужная работа | Сразу проектировать явный документированный owner-escape + реестр + проверку критиком |
| 43 | Предпочтение пользователя: строгое правило + явная owner-дискреция для фундамента/вводных | При предложении governance — строгий порог + явный waiver для класса-исключения; миссия = дух, не слепой % |

### Git / repo hygiene (findings 39–42)

| # | Урок | Применение |
|---|---|---|
| 39 | squash-merge ломает `rev-list origin/main..branch` как признак merged | Классифицировать ветки через merged-PR: `gh pr list --state merged --json headRefName` (authoritative) |
| 40 | `git push origin --delete <много>` срабатывает частично и тихо | После batch-delete — верифицировать `git branch -r`, ретраить остаток; не доверять grep по выводу push |
| 41 | local main stale/dirty, нужно базироваться на remote | `git worktree add /tmp/wt -b <br> origin/main`; после merge — `worktree remove --force` |
| 42 | `comm` для сравнения деревьев чувствителен к префиксу пути | Нормализовать пути обеих сторон ИЛИ пофайловый `git show origin/main:p \| diff -` |

Заметка: pre-commit secret-scanner ложно warning'ит на arXiv-URL/ID в research-таблицах (checks всё равно passed) — не блокер, не MCP-limitation (это hook).

### Артефакты-наследие
- `notes/reviews/2026-05-15-failure-content-audit/{lec-01,lec-02,lec-04}.md` — seed-таблицы документированных провалов ИИ по темам (использовать при production failure-контента L3/L5–L17).
- Л4 = reference-модель структуры failure-контента (strict-in 62/53/53%, APPROVE-CLEAN).
- Системно: slides — слабейший артефакт для failure-контента (урок устно, не на видимом слое).

## 2026-05-16 — Лекция 3: owner-решения USER GATE 0 (#87)

**Контекст:** Phase 1 Лекции 3 «Архитектуры AI-систем». plan-v2-final после critique (methodology APPROVE-WITH-POLISH/4P1 + reader-text-only REVISE/7P1) + orchestrator roast.

### Governance escape-hatch (документированное owner-решение)

- **Глубина `lec-03/chapter.md` = 22k+ слов, без верхней границы.** Red-flag «chapter >15k слов = red-flag» (`tools/lecture-production/README.md` §6) **явно снят владельцем для lec-03** на USER GATE 0. Обоснование: глава = глубокий референс + Q&A-бэкап + deep-dive boxes («что не вошло в лекцию, но важно»); слайды/речь остаются 75-мин срезом. methodology-critic Phase 1 подтвердил методическую корректность (reference depth ≠ delivery scope). Это escape-hatch по принципу governance-правил (явное + документированное owner-решение для класса-исключения; см. memory feedback_governance_rules). **Действует только для lec-03**; для других лекций red-flag в силе без явного аналогичного решения.
- **Document Size Limit 600 строк — waiver НЕДОСТУПЕН.** chapter обязан быть разбит на `chapter.md` + `chapter-part2.md` с кросс-ссылками.

### Прочие решения GATE 0

- Hook s01 = Moffatt v. Air Canada (universal, юр. ставки, рамкирует тезис). $4,200 agent loop → s23.
- Slide-count Лекции 3 LOCKED = 30 (cascade-tracking).
- strict-in метрика: считать честно partial→out (решение #78) на этапе планирования, не только на Phase 3/7/10 — завышенный baseline в плане = downstream-ловушка (Phase 1 methodology P1-3). Plan §5 → честно 12/30≈40% + per-artifact таблица.
- book-first: speech-нарративные кейсы (#13 DPD, #14 Chevrolet) обязаны присутствовать в chapter (deep-dive) до использования в speech.

### Лекция 3 deck — owner-структурная ревизия после GATE-A QA (2026-05-16, #87)

Владелец после Phase 4 QA дал 7-пунктовую структурную правку + сторителлинг. Решения:
- Slide-count «LOCKED=30» (cascade-tracking) — **снят owner-директивой**: +6 слайдов (s04a/s13a/s13b/s23a/s25a/s31). Применена **suffix-ID схема** (как lec-04 s05b/s08a/s13a), чтобы НЕ перенумеровывать s01–s30 и не ломать `[for-slide-sNN]` маркеры finalized-главы — cascade-safe (глава не правится; новые слайды → существующие §). Lesson: cascade-lock защищает от случайного дрейфа, но осознанная owner-правка структуры исполняется через suffix-ID, а не renumber.
- deck.yaml >600 строк (Document Size Limit) + явное прежнее указание владельца «делай несколько» → split на `deck.yaml`+`deck-part2.yaml` с кросс-ссылками + обновить loader build-скрипта.
- divider'ы/определение/Q&A — strict-in partial→out; минутная доля (~43%) — честная метрика (divider'ы ~0.3 мин), слайдо-доля 12/36≈33% ≥30% сохранена; chapter strict-in ~58% не затронут.
- U-6: не выносить функцию слайда в title (ретайтл s30); section-divider с темой раздела — норма канона (не нарушение).

## 2026-05-16 — repo_dir = номер РПД: переименование lec-04→lec-07 (#94)

После #92 (медицина = Лекция 7) папка `library/lectures/lec-04` стала единственным mismatch repo_dir≠number → путаница владельца. Решение владельца: `git mv lec-04 → lec-07` + полный каскад. Теперь **repo_dir == номер РПД для всех произведённых лекций** (lec-01→Л1, lec-02→Л2, lec-03→Л3, lec-07→Л7); прежняя конвенция «repo_dir != number» (зафиксированная в #86) **отменена** — она и была корнем путаницы. Каскад: 206 файлов git mv, build_lec04.py→build_lec07.py, lec-04.pptx/pdf→lec-07, lectures.yaml/documents.yaml/course-plan/CLAUDE.md/wiki/plan-v2-final обновлены (16 текст-правок). **Историческое НЕ тронуто** (принцип всей сессии): qa-reports content, notes/lecture-4-review, reflections, mcp-limitations, decisions.md прежние записи, iteration-log, branch:issue-73 frontmatter — перемещены git mv, текст-история сохранена.

**Урок:** имя папки лекции должно сразу = номеру РПД (не порядку производства). Конвенция «repo_dir != number» из #86 создала путаницу за 2 шага (производство → перенумерация → переименование). Для будущих лекций: папка `lec-NN` = номер РПД сразу.

**Открытый pre-existing gap (НЕ из #94):** `ontology/store.ttl` моделирует старую структуру (lec_04=медицина, lec_07=этика) — рассинхрон с РПД. Отдельный issue #95 (требует RDF-ремоделяции, не path-rename; слепая замена = IRI-коллизия).

## 2026-05-16 — Лекция 4 USER GATE 0 (#99): owner-решения

Phase 1 Лекции 4 «AI в разработке ПО». plan-v2-final после critique (methodology REVISE 1P0/6P1 + reader-text-only APPROVE-WITH-POLISH) + roast — 8 пунктов закрыты.
- **Глубина `lec-04/chapter.md` = 22k+ слов** (как Глава 3): red-flag «>15k» (`tools/lecture-production/README.md` §6) **явно снят владельцем** на GATE 0 (тот же governance escape-hatch, что для lec-03; принцип memory feedback_governance_rules — явное+документированное owner-решение для класса-исключения). Только для lec-04. Document Size Limit 600 строк — split, waiver НЕТ.
- Hook s01 = METR −19% perception-gap; Replit → s16.
- Slide-count Лекции 4 LOCKED = 32.
- **L4 — owner-waiver ≥30% НЕдоступен** (∉ L1–L3, Решение #82): несущая ось A→D сама НЕ failure → failure/judgment-плотность главы проектируется намеренно (каждый раздел завершать failure-кейсом + критерием «когда не/опасно»; ось не засчитывается). strict-in slides честно 14/32≈44%, per-artifact операционализирован (chapter≥40%/slides≥40%/speech≥35% с именованными блоками).
- Конвенция repo-папок (после #94): `lec-04` = канон Лекция 4 (ПО); медицина = lec-07.

## 2026-05-17 — Лекция 4 deck v2: Раздел-0 сторителлинг-перетряска + сквозной tone-pass (Решение #100, #99)

deck v2 (после Phase-4 v1→v2 fix) показан владельцу — **сторителлинг сломан**: несущая ось A→D (хребет лекции) **нигде не показана отдельным слайдом**; s03 = защитный мэппинг «Лекция 4 не вводит новый аппарат» (оправдание), s04 = «возвращаемся 5 раз» meta + §-коды + course-scaffold disclaimer-футер, s05 = абстрактная рамка для невиданных уровней + «проекция правила Л3», s06 «внезапен». Цитата владельца: «где сами уровни и их описание?! ты вообще сторителлинг продумывал? надо перетряхивать».

**Корень (planning error, не designer):** в plan-v2-final не было keystone-слайда с самой лестницей — уровни «всплывали» по ходу; тон Раздела 0 = защита курсовой методологии вместо подачи нового студенту.

**Owner-решения (AskUserQuestion, подтверждено):**
- **Новый s03 = карта лестницы A→D (KEYSTONE)**: 4 строки A/B/C/D × «что делает AI · кто решает · живой пример»; бывш. s05-«единый паттерн» (линза анализа) **свёрнут в s03 как колонки**; Л3-связь = 1 строка в теле (не таблица-мэппинг).
- **s04** = ЦВ + 5 якорей «где человек обязателен» **именами по смыслу**; «возвращаемся N раз» и course-scaffold disclaimer-футер **удалены**.
- **s05** слот **переиспользован** (НЕ renumber — 32 ID и chapter `[for-slide-sNN]`/deck.yaml chapter_ref s06–s32 стабильны) → контентный несущий принцип «**цена ошибки растёт с автономией A→D**» (ранний посев → собирается в матрице s29).
- **Сквозной tone-принцип (ENFORCED, все 32 слайда)**: подаём новое студенту, впервые сталкивающемуся с темой — не защищаемся, не оправдываем методологию. Видимый слой: **0** §-кодов / (sNN) / (Раздел N) / LO-кодов / course-scaffold-disclaimer / «не вводим нового»/«проекция Л3»/«возвращаемся N раз» meta. Атрибуция course-scaffold + Л3-связь (научная честность) — **в speaker notes**, не на слайде. Закреплено: plan-v2-final §4 преамбула + §7 Forbidden; glossary.yaml note «лестница автономности».
- **strict-in:** s05 переопределён → judgment/limits-якорь, strict-in-eligible (15/32≈47%); пересчёт — methodology-critic Phase-7 re-QA.

**Урок:** несущая ось лекции обязана быть отдельным keystone-слайдом в Разделе 0 **до** первого погружения в неё; Раздел 0 учит новому, а не защищает курсовую методологию. Атрибуция homegrown-таксономии (научная честность) ≠ видимый disclaimer-футер — её место в speaker notes. Рецидив-класс Л2-R1/Л3 (§/meta-leak) → теперь явный deck-wide ENFORCED-принцип в плане, не только anti-pattern постфактум.

### Лекция 4 deck v3.1 → GATE B + owner-override slide-count (Решение #101, 2026-05-17)

deck v3.1 (Раздел-0 keystone + сквозной tone-strip): re-QA 5 критиков — presentation-critic/consistency-checker APPROVE-WITH-POLISH, methodology-critic/reader APPROVE-CLEAN, student APPROVE-WITH-POLISH; **0 открытых P0/P1**; independent grep оркестратора видимый слой TOTAL=0 ×2; pre-USER-GATE walkthrough PASS. Структурная браковка владельца (несущая ось не показана) — закрыта и независимо подтверждена 5/5.

**Owner GATE B (AskUserQuestion):**
- **+3 раздела-дивайдера Разделам 1/5/6** (симметрия 7-секционного roadmap-бара). Полная схема 6 дивайдеров: s04a(Р1)/s10(Р2)/s14(Р3)/s18(Р4)/s24a(Р5)/s28a(Р6).
- **Owner-override GATE-0 Q4 «slide-count LOCKED=32» → 35.** Явное документированное решение владельца (governance escape-hatch pattern, как chapter-depth Решение #82-класс). Реализация — **suffix-ID s04a/s24a/s28a, cascade-safe**: глава финализирована GATE A с `[for-slide-sNN]` s01–s32; renumber рассинхронит book-first → suffix-ID НЕ трогает chapter/chapter_ref/нумерацию (конвенция Лекции 3, post-GATE-A добавления).
- **GATE B: deck v3.1 принят → Phase 9 (речь).** Дивайдеры ложатся ДО речи (speech-writer derive из финального deck) — порядок: divider-add → re-QA delta → finalize → speech.
- strict-in: count=15 неизменно, дивайдеры partial→out; слайдо-доля 15/35≈43% (≥40% держится), минутная 54.5% не затронута (дивайдеры ~0.3 мин); methodology-critic re-confirm на delta.

**Урок:** post-GATE-A добавление слайдов = всегда suffix-ID (chapter `[for-slide-sNN]` финализирован — renumber = book-first drift). slide-count LOCK снимается ТОЛЬКО явным owner-решением с записью в реестр (как все governance escape-hatch'и). Owner-визуальная симметрия (roadmap ↔ дивайдеры) — решение владельца, не оркестратора (Orchestrator Self-Critique: визуальные структурные выборы defer to owner).

### Лекция 4: owner-требование «тулы на каждом уровне A/B/C/D» во всех 3 артефактах (Решение #102, 2026-05-17)

Владелец (после Phase 11, pre-GATE-C): «для каждого типа уровня не хватает тулов, обязательно дополни презу, часть, речь тулами на каждом уровне. смотри, что распространено в 2026». Реальный content-gap: лестница A→D без named-инструментов под каждый уровень.

**Owner-override:** chapter финализирован v1.1 (GATE A), deck GATE-B-approved, speech reviewed v1.1 — явное документированное owner-указание дополнить ВСЕ 3 (тот же governance escape-hatch pattern). Мы pre-GATE-C → окно открыто, ничего не финализировано окончательно.

**Решения:**
- **Research-first (свежесть критична — урок ARC-AGI устаревания):** веб-верифицировано 2026-05-17, `notes/research/lecture-4/tools-landscape.md` раздел «2026-05-17 update». Маппинг: A=Copilot tab/Cursor Tab/JetBrains; B=ChatGPT-чат/Copilot·Cursor inline; C=Claude Code/Cursor Agent/Codex; D=Copilot agent/Devin/Jules. Все adoption-числа `[VFY-day-of]` (волатильны), на видимом слое — только направление (паттерн s12/s27).
- **Book-first порядок:** chapter v1.1→**v1.2** (per-level тулы в Р1/Р2/Р3 + tools-landscape deep-dive) → deck derive → speech v1.1→v1.2 derive → re-QA delta (4 критика) → GATE C.
- **Owner-выбор размещения в deck (AskUserQuestion): per-level слайды** s06(A)/s07(B)/s11-12(C)/s15(D) — блок «Инструменты 2026» + 1 строка adoption-направление + 1 anti-hype-оговорка. **Keystone s03 НЕ трогаем** (5-сек читаемость защищена, presentation-critic warned). s27 держит мета-тренд «в/из». Без новых слайдов (35 LOCKED), без renumber.
- **AI-Failure усиление, не хайп:** тулы вносятся С judgment-оговорками (Devin overclaim, «Copilot стагнирует ≠ умер», «низкая доля ≠ decline», trust-gap 29%, mode≠brand, infrastructure≠level-tool) — это failure/limits-контент, не вендор-реклама.

**Урок:** при owner-расширении pre-GATE-C — строго book-first каскад (chapter → deck → speech, не параллельно); свежие vendor/adoption-факты ВСЕГДА `[VFY-day-of]` + только направление на видимом слое; добавление инструментов в обучающий материал обязано нести anti-hype/границы (mode≠brand, overclaim), иначе нарушает AI-Failure-правило. Размещение, трогающее user-approved keystone, → defer to owner (Orchestrator Self-Critique).

### Лекция 4 USER GATE C: финализировать + 3 pre-final owner-правки (Решение #103, 2026-05-17)

Все 3 артефакта reviewed, 0 P0/P1 через 11 фаз, обе owner-интервенции (storytelling #100/#101 + тулы #102) интегрированы и подтверждены 5/5 → 4/4 критиками. Owner GATE C (AskUserQuestion): **финализировать → PR**, предварительно применив 3 owner-note-правки (вариант «ничего» отменён выбором действий):
- **Тег-унификация:** `[VERIFY-DAY-OF]` → `[VFY-day-of]` в speech l.25/26/225 (project-tag-стандарт; косметика, нерендеримый lecturer-док).
- **«мейнтейнер» → «сопровождающий»:** добавлено в `glossary.yaml forbidden_anglicisms` (glossary-lock, orchestrator-owned). **Cascade-of-changes** (grep-scoped): chapter.md/part2/part3 (вкл. **заголовок §4.5 + TOC-якорь** — атомарная синхронизация anchor), speech l.43, slides/s01. book-first: chapter renames первым, deck/speech mirror.
- **curl #5 отдельным слайдом:** plan §5 изначально называл «#5 curl-slop» речевым нарративом; deck его не имел (s22=slopsquatting), был устный якорь. Owner: вынести в **suffix-ID s22a** (security-раздел, между s22 и s23), derive из chapter §4.5 (детальный ≥600-слов кейс уже есть — book-editor добавляет `[for-slide-s22a]` маркер, нового chapter-контента не нужно). Cascade-safe (s01–s32 + suffix неизменны). slide-count 35→**36** (owner-override, документировано). strict-in: s22a = named failure #5 → count 15→16, 16/36≈44% (methodology re-confirm).

**Порядок (book-first):** decisions/glossary → chapter v1.2→v1.3 (rename + §4.5 heading/TOC/anchor + [for-slide-s22a]) → deck v3.3→v3.4 (s22a + rename-if-present) → speech v1.2→v1.3 (tag + rename + curl-фрагмент s22a, корректировка s25/s32 якоря) → re-QA delta 4 критика → pre-GATE-C delta → finalize status→finalized → push → PR (мерж только по явной owner-команде).

**Урок:** term-rename = ВСЕГДА cascade-of-changes grep ПЕРЕД делегированием (заголовки/TOC/anchor — скрытая зависимость, ловится только грепом); slide-add post-review = suffix-ID + owner-документированный slide-count override; «принять как есть» + actions в multiSelect → actions выигрывают (явное намерение пользователя на изменение).

**ЗАКРЫТО (GATE C passed, 2026-05-17):** re-QA delta #103 — fact-checker + presentation-critic APPROVE-CLEAN, methodology + consistency APPROVE-WITH-POLISH, **0 P0/P1**. Подтверждено: s22a book-first==§4.5 (0 phantom), strict-in 16/36≈44% слайды (Р4 single-cluster НЕ вернулся, 31%), pacing ≤75 (~74 active, speech=истина доставки), rename ПОЛНЫЙ (0 остатка кроме changelog-doc), frozen/keystone байт-идентичны, ЦВ-возврат-4 цел, discrepancy #1 структурно RESOLVED. deck.yaml frontmatter синхронизирован (consistency P2 D1: v3.4/chapter v1.3/36). **Все 3 артефакта `status: finalized`** (chapter v1.3 / deck v3.4 / speech v1.3). **Лекция 4 ПРОИЗВЕДЕНА ПОЛНОСТЬЮ** через 11 фаз + 4 owner-интервенции (#100 storytelling-keystone, #101 дивайдеры, #102 тулы-per-level, #103 rename+curl-слайд). → push + PR (мерж по явной owner-команде).
## 2026-05-17 — Лекция 5: owner-решения USER GATE 0 (#100)

**Контекст:** Phase 1 Лекции 5 «AI в финансовом секторе и ритейле» (issue #100, branch `issue-100-lec-05-finance-retail`). plan-v2-final после Phase 1 critique (methodology APPROVE-WITH-POLISH/0P0·4P1·7P2 + reader-text-only APPROVE-WITH-POLISH/0P0·4P1) + orchestrator finalize. Производится параллельно с lec-04 (shared `.git`, worktree-изоляция `/tmp/lec-05-wt`).

### Governance escape-hatch (документированное owner-решение)

- **Глубина `lec-05/chapter.md` = 22k+ слов, без верхней границы.** Red-flag «chapter >15k слов = red-flag» (`tools/lecture-production/README.md` §6) **явно снят владельцем для `lec-05/chapter.md`** на USER GATE 0. Тот же governance-паттерн, что Л3 (2026-05-16, #87) и Л4 (#99): глава = глубокий референс + Q&A-бэкап + deep-dive boxes; слайды/речь = 75-мин срез. methodology-critic Phase 1 подтвердил методическую корректность (reference depth ≠ delivery scope). Escape-hatch по принципу governance-правил (явное + документированное owner-решение для класса-исключения; memory feedback_governance_rules). **Действует только для lec-05**; для других лекций red-flag в силе без явного аналогичного решения.
- **Document Size Limit 600 строк — waiver НЕДОСТУПЕН.** chapter обязан быть разбит на `chapter.md` (frontmatter+§0+Раздел 1+Раздел 2) + `chapter-part2.md` (Раздел 3–6+Глоссарий+Источники) с двусторонними кросс-ссылками.

### Fact-integrity: РПД-цифра «голосовые ассистенты >90% обращений» заменена verified-данными

- РПД-аспект Л5 содержит «голосовые ассистенты (>90% обращений)». Verified-источники (WebSearch, research 02) дают только «Т-Банк чат-бот >40% обращений» (TAdviser, 2025) и «70% банков планируют голос к 2025»; первоисточник «>90%» НЕ найден. **Решение владельца USER GATE 0:** на видимом слое слайдов и в плане используется **verified-формулировка** («значительная и растущая доля первого контакта автоматизирована; Т-Банк >40%; 70% планируют к 2025») с атрибуцией+датой; РПД-цифра «>90%» **НЕ используется**, не «округляется вверх». Обоснование — **fact-integrity**: лекция сама учит fact-checking (паттерн Р4, mastery — Семинар 5); assertion на неверифицированной цифре подорвал бы доверие к лекции. `[FACT-CHECK]` до day-of. Зафиксировано: research-02 §1, plan-v2-final G-3/§7/§9.

### Л7-мосты = forward-pointer'ы (Л7 идёт ПОСЛЕ Л5 по course-plan.md)

- Phase 1 critics (methodology P1-2/P2-2 + reader A2/A3/D) выявили: план v1 строил FP/FN, матрицу ошибок и прокси-bias как «мост назад к Л7, не переобъяснять» — но **Л7 (медицина) идёт ПОСЛЕ Л5** по `course-plan.md`; для студента, идущего по порядку, это первое формальное появление, не recall. **Решение владельца:** roast-4 v1 «не переобъяснять» **СНЯТ**; Л5 вводит FP/FN + матрицу ошибок (TP/FP/FN/TN на пальцах) + cost-sensitive + механизм прокси-bias **с нуля компактно** (БЕЗ медицинской prevalence/PPV-глубины), Л7-ссылки = **forward-pointer** «углубите там». Корректные §-якоря (verified против finalized `library/lectures/lec-07/chapter.md`): sensitivity/specificity = **Л7 §2.2**; Obermeyer/Optum = **Л7 §4.3** (НЕ §3 — §3 = drug discovery; P1-2 cascade-fix во всех местах плана/research). **Урок:** forward-reference на ещё-не-прочитанную лекцию ≠ «мост назад» — для студента по порядку это ввод нового понятия; план должен делать ввод самодостаточным + явный forward-pointer, а §-якорь forward-цели — verified против finalized chapter ДО GATE 0 (не «найдём на Phase 2»).

### Прочие решения GATE 0

- Hook s01 = Zillow iBuying коллапс (universal, крупные ставки 2021-исторический, рамкирует ЦВ, payoff в Р1/s09). Knight Capital → callback внутри s09/s14 (не отдельная failure-процентовка — reader C2).
- Slide-count Лекции 5 LOCKED = 32 + suffix-ID схема (как lec-03/lec-04) для structural-правок после GATE-A без renumber `[for-slide-sNN]`.
- CV = сквозной иллюстративный пласт + KYC в безопасности s31, НЕ отдельный 6-й раздел (75 мин не тянут 6 равновесных типов; methodology Curriculum-check D подтвердил).
- strict-in метрика: solid headline = 11/32≈34% slides (граничные s06/s16/s22 — upside, НЕ baseline; в bucket ТОЛЬКО при развёрнутом критерии ≥3 аргумента — P1-1). Per-artifact таблица chapter/slides/speech раздельно, цель solid ≥30% каждый; chapter измеряется долей слов (P2-1). Не повторять Л3 v1-ловушку (завышенный baseline 52%→40%).
- LO6 Bloom-разводка: Лекция 5 = Understand (распознать класс ошибки + назвать принцип проверки), Семинар 5 = Apply/Analyze (команды сами проверяют по первоисточникам). §3 success-критерий НЕ дублирует практику Сем5 (P1-3).
- Q3 plan-v2-final ОДОБРЕН → Phase 2 chapter draft.

## 2026-05-17 — Лекция 6 production (рефлексия, #101; reflection-folder `notes/reflections/2026-05-17-lec-06-engineering-cad-production/`)

- **Usage-лимит субагента ≠ «subagent failure».** Правило CLAUDE.md «if a subagent fails — do the work directly» НЕ распространяется на rate-/usage-лимит (transient infra). Корректно: дождаться сброса + перезапустить тот же спавн; провизорный orchestrator-self-review (если сделан) пометить provisional и заменить консолидатом по реальным отчётам критиков; артефакт не финализировать до реальных вердиктов. Якорь: 3 Phase-10 критика Л6 упали по лимиту, владелец скорректировал. memory `feedback_subagent_usage_limit`.
- **Pre-gate ловит post-critic regressions — это его ключевая ценность.** P1/P2-фиксы, внесённые revision-агентом ПОСЛЕ Phase-3/7/10 критиков, обходят critic-ревью. Л6: Phase-8 P2-фикс дат внёс покорёженную s11-аннотацию (прошла бы к студенту); pre-gate поймал. Нужен mandatory targeted re-grep + mini visual re-check затронутых после каждого revision-агента ДО pre-gate (improvement #2).
- **`[for-slide-sNN]` НЕ в finalized chapter body.** book-editor capability-маркеры — authoring scaffolding; lec-07 precedent = 0, lec-06 протёк 27× (pre-gate снял). Закрепить как book-editor DoD + pre-gate chapter-grep (improvement #3).
- **«Строить новое от известного студенту» лечит «матбаза-болезнь».** Сквозная проблема (KKT/Галёркин/гомогенизация/спектральный bias как данность) системно снята мостами от уже-пройденного (сопромат σ_vM≤[σ]/концентратор; градиентный спуск из лекции 2; КЭ как пользователь CAD). Переносимый content-паттерн для всех технических лекций; reader-simulator подтвердил снятие.
- **Worktree-изоляция масштабируется до 3+ параллельных лекций без contention.** lec-04 #99 + lec-05 #100 + lec-06 #101 одновременно, branch-ref propagation через `git update-ref` — ноль contention. ENFORCED Multi-Lecture policy валидирована на практике.
- **strict-in: разброс методик подсчёта высок** (book-editor 33% vs methodology 40%; speech 62% vs consistency 44% — вывод >30% устойчив, но variance большая). Канонизировать один счётный рецепт в README §3.6 (improvement #7).
- **Completeness-ожидание владельца.** «доделай все» = ноль висящих хвостов; манифест produced-flip нельзя оставлять «на потом» — закрывать сразу отдельным branch+PR (сделано: PR #103). Не предлагать «оставить на батч» без явного обоснования невозможности сейчас.

## 2026-05-17 — Лекция 5 production (рефлексия, #100; reflection-folder `notes/reflections/2026-05-17-lec-05-production/`)

- **Self-reported producer-метрика, погнавшая verdict, НЕ принимается как gate-сигнал без critic-ре-верификации ЕГО токенайзером.** Л5: speech-writer Phase 9 заявил «все 33 ≤95 WPM / PROVEN PASS» при фактическом s28=100.3 (non-greedy `«…»` баг самопроверки); methodology-critic Phase 10 поймал. Ad-hoc orchestrator-скрипт независимой ре-верификации (Phase 11.5) **тоже сломался** (s32=794, divider'ы 100-120). Вывод: pre-gate ре-верифицирует метрику, погнавшую REVISE, спавном focused critic re-check с методикой Phase N — НЕ orchestrator-grep'ом; producer помечает self-метрику «требует critic-ре-верификации», не «PROVEN». Расширяет «strict-in variance» (Л6) на любую self-reported метрику. → issue #111.
- **MANDATORY artifact-sync имеет silent-failure mode.** Compound `cd /tmp/wt && … && cp src dst` оставляет cwd в worktree → `cp` src==dst, sync в main-repo молча НЕ происходит (поймано только inode-check'ом). Sync обязан: абсолютные src+dst, без `cd`-в-worktree в compound, обязательный пост-верификатор (inode-diff / `rsync --checksum` + `ls`). → issue #112.
- **Pre-gate pacing/aggregate-greps по split deck (deck.yaml+deck-part2.yaml) двойной счёт.** Σ duration_min наивным grep/awk = 144 (реально 70+5) — суммировал `totals:`+metadata-поля обоих файлов. Scope строго per-slide ИЛИ читать deck `totals.slide_times_sum_min` + доверять critic. Doc-fix pre-gate SKILL (без issue, bundle).
- **Slide-count LOCK formulation.** «LOCKED=N» неоднозначно (Л5: план «32» vs deck 33 = 32 content + s04a divider; designer объяснял дважды). Канон-формулировка: «N content slides + структурные divider'ы через suffix-ID (НЕ в LOCK-счётчике)». Внести в `templates/lecture-outline.md` + presentation-build README (без issue, bundle).
- **Валидации (подтверждено, action не требуется):** Lec-N-1-check предотвратил ложный P1 (видимый `## Changelog` в chapter body = установленная конвенция lec-04, не designer-extra leak — сверка с Lec-N-1 обязательна ДО флага); usage-limit re-spawn сработал (консистентно с Л6); worktree-изоляция при 3 параллельных лекциях (lec-04/05/06) — 0 контеншена (повторное подтверждение).
- **Forward-pointer vs «мост назад» ловится на Phase 1 critique дёшево.** Л5: reader-критик Phase 1 поймал, что FP/FN/bias подаются как «мост назад к Л7», хотя Л7 идёт ПОСЛЕ Л5 по курсу; исправлено в plan-v2 ДО chapter-draft. Каскад-предотвращение на этапе плана >> фикс в 3 артефактах потом. Reusable: на Phase 1 critique проверять направление всех меж-лекционных ссылок против course-plan порядка.
