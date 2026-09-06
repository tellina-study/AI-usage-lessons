# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI-usage-lessons is a personal knowledge management and course delivery system built entirely on Claude Code as the runtime. It manages a project library (normative documents, references) and a semester course for students (lectures, slides, materials) using an agent-based orchestration approach with MCP integrations.

**Owner:** single maintainer — speed and simplicity over enterprise patterns.

## Audience Profile (ENFORCED — owner observation 2026-09-05, после Семинара 1 и Лекции 1)

Реальная аудитория курса (группа 1, 09.03.01, 3 курс) **значительно сильнее** исходных допущений:

- **Все** активно пользуются AI-чатами в повседневной работе/учёбе.
- **Все** в той или иной мере вайбкодят (пишут код с AI-ассистентами).
- Многие понимают — как минимум верхнеуровнево — как работают нейросети вообще и LLM в частности.
- **Многие или все уже работают в ИТ** — это практикующие инженеры, не новички.

**Следствия для всех материалов курса (лекции и семинары):**
- Не тратить время на базовые определения и «что такое ChatGPT» — планка выше.
- Разминки уровня «классифицируй знакомый инструмент» и квизы на очевидные факты — слишком лёгкие, аудитория проходит их быстрее бюджета (Семинар 1 закончился раньше времени).
- Ценность — в **практике неочевидных решений**, разборе trade-offs, реальных рабочих кейсах; можно опираться на профессиональный опыт студентов (приносить задачи с их работы).
- Тайминг планировать с запасом материала (~×1,5 от слота) и явным cut-order.

## Architecture

### Runtime

Claude Code is the only runtime. No separate backend, no custom UI. All automation happens through subagents, skills, hooks, and MCP servers.

### MCP Stack (priority order)

| Layer | Server | Purpose |
|-------|--------|---------|
| Google | `workspace-mcp` | Read/write Google Docs, Sheets, Slides, Drive |
| Doc Loader | `document-loader` | Read PDF, DOCX, XLSX, PPTX, images — full office format support |
| Local RAG | `mcp-local-rag` | Semantic search over ingested documents (PDF, DOCX, TXT, MD) |
| Diagrams | `drawio` (@drawio/mcp) | Generate/preview `.drawio` and Mermaid diagrams |
| GitHub | `github` (github-mcp-server) | Issues, PRs, repo operations |
| Ontology | `open-ontologies` | RDF/SPARQL + OWL reasoning + SHACL validation (Oxigraph-based) |

**Tool selection rule:** `workspace-mcp` is the only Google integration server. Use it for all Google Workspace operations.

### MCP Configuration

- MCP servers are registered via `claude mcp add` or `.mcp.json` (NOT `.claude/settings.json`)
- Secrets (OAuth credentials, PATs) go in `.mcp.json` only — this file is gitignored
- `.claude/settings.json` is for non-secret server configs and permissions only
- After any MCP config change, restart Claude Code for changes to take effect
- Always verify registration with `claude mcp list` after adding a server

### Google Drive Work Folder

Primary working folder: `https://drive.google.com/drive/folders/1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am`

### Google Drive Folder Structure

| Path | ID | Contents |
|------|-----|----------|
| `00-course/` | `1sHXoLaIqCpBRv1IaLjS6lNtBdwI5cPc0` | Структура курса, нарратив, каталог тем (sheet), чит-шит |
| `01-formal/` | `1-sQ7H1CBNWaHvQIDE8TLCwVX2ilEeb0p` | РПД, ФОС, матрица компетенций |
| `02-lectures/` | `16osAMJ9y67Yem9T6fK6yDv1fXF8BGLEZ` | 17 папок лекций (lec-01 — lec-17), каждая: plan + slides + assets/ |
| `03-seminars/` | `1AZhb5q-yODrIJEnQBN8S1KJI0bby588J` | 17 папок семинаров (sem-01 — sem-17), каждая: task-brief + rubric |
| `04-resources/` | `1yDZrw9CcGtGljNGZ-QByyoUGIMVr9Tc4` | Библиотека промптов, статистика, список литературы |
| `archive/` | `1rZkywX5DufGJaf1htCa1Oa_zCKmUgKMT` | Старые версии |

**Правила размещения:**
- Ресурсы для одной лекции → `lec-NN/assets/` (не в 04-resources)
- Ресурсы для нескольких лекций → `04-resources/`
- Табличные данные → Google Sheets (не Docs с markdown-таблицами)
- Старые версии → `archive/` (перемещать, не удалять)

### GitHub Project Board

Issues and tasks are tracked at: `https://github.com/orgs/tellina-study/projects/1/views/1`

## Mandatory Git Rules

- **NEVER push to main directly** — always create feature branches and PRs. This is NON-NEGOTIABLE, even for "small" fixes, doc updates, or config changes.
- **Branch naming**: `issue-{NUMBER}-{short-description}`
- **Every commit references the issue**: `#{NUMBER}` in commit message
- **Workflow**: create branch → commit → push branch → create PR → review → merge
- **PR merge — только по прямому указанию пользователя.** Не мержить PR без явной команды («мерж», «merge», «давай», «go ahead»). Когда указание получено — Claude мержит сам через `gh pr merge <N> --merge --delete-branch`. НЕ перекладывать кнопку на пользователя.
- **No work without an issue.** If one doesn't exist, create it first.

---

## AI-Failure & Judgment Content Rule (ENFORCED — фундаментальное)

**Миссия курса.** Курс учит студентов **когда можно и нужно применять ИИ, а когда — нет**: генерировать идеи и **говорить «нет» неправильным**. Цель — критическое суждение и осознанный выбор инструмента, а не пропаганда ИИ. Это правило — **одно из фундаментальных**, наравне с Mandatory Git Rules.

**Правило.** В **каждой** лекции **≥30%** содержания описывает хотя бы одно из:
- документированные **провалы ИИ** + явно сформулированный **выученный урок**;
- разбор **фундаментальных ограничений / рисков** подхода;
- явные **критерии «здесь ИИ не нужен / не применим»**;
- **сравнение с более правильным альтернативным инструментом** (не-ИИ или другой класс ИИ/метод).

**Измерение — холистическое, strict-in.** Доля **strict-in ≥30%** должна быть видна **в каждом из 3 артефактов** (`chapter.md`, slides/deck, `speech.md`) отдельно, не сконцентрирована в одном. Метрика — доля слов / слайдов / минут. **Засчитывается только полностью in-bucket контент**: смешанные / частично-bucket блоки, общие оговорки и «риск мимоходом» **не учитываются** (partial → как out при подсчёте %). Решение #78 (2026-05-15): порог именно strict-in, не weighted.

**Что НЕ засчитывается:** общие дисклеймеры, однострочные оговорки, «ИИ иногда ошибается» без урока / критерия / альтернативы; «магическая пилюля» с приставкой «но будьте осторожны».

**Counter-check (mandatory):** лекция < 30% **ИЛИ** доля сконцентрирована в одном артефакте → verdict **REVISE** (не APPROVE). Это не «polish» — это структурный gap.

**Enforcement points:**
- План лекции (Phase 1) выделяет ≥30% бюджета на failure/judgment-контент.
- `methodology-critic` проверяет долю + холистичность на Phase 1/3/7/10; <30% или single-artifact concentration → REVISE.
- USER GATE A/B/C: pre-gate walkthrough включает failure-share check.
- `tools/lecture-production/README.md` §3.6 + `templates/lecture-outline.md` содержат обязательный блок «Провалы, ограничения и альтернативы».

**Owner waiver (только вводные L1–L3).** Для лекций **L1–L3** (introductory по curriculum-mapping) владелец курса может **явным документированным решением** снять требование strict-in ≥30%. Waiver обязан быть: (1) явным, не молчаливым; (2) записанным в реестре `tools/lecture-production/README.md` §3.6 со ссылкой на issue. Без записанного waiver правило применяется. Для **L4–L17 waiver недоступен** — strict-in ≥30% обязательно. Решение #82 (2026-05-15).

**Почему ENFORCED:** инженер, умеющий только запускать ИИ, опасен; ценность специалиста — знать границы и отвергать неподходящие применения. Лекция без провалов учит доверию, а не суждению.

---

## Chapter Depth Baseline (ENFORCED — фундаментальное)

**Правило.** `library/lectures/lec-NN/chapter.md` для всех **L4–L17 лекций — минимум 30 000 слов** (target 30k ±5% = 28 500–31 500). Это **базовый референс**, не конспект 75-мин лекции; chapter — это **полный методический референс уровня академического textbook chapter**, source-of-truth для slides+speech derivation + Q&A backup + self-study deep-dive материал.

**Применимость:**
- **L1–L3 (introductory):** owner waiver доступен (как для AI-Failure rule). Без записанного waiver — правило применяется. Реестр waivers в `tools/lecture-production/README.md` §3.6.
- **L4–L17:** ≥30 000 слов **mandatory**, waiver недоступен.

**Multi-part split:** если chapter >600 строк, обязательное разбиение на части:
- `chapter.md` — частина 1 + frontmatter с `parts: N`, `length_words: ~XXk`
- `chapter-part2.md` — часть 2
- `chapter-part3.md` — часть 3 (если нужно)
- Cross-link через TOC в chapter.md

Каждый файл ≤600 строк per CLAUDE.md «Document Size Limit».

**Что НЕ засчитывается в 30k:**
- Frontmatter YAML
- Markdown headings без содержания
- TOC / list-only sections
- Источники / bibliography (это отдельно)

**Counter-check (mandatory):** chapter <30k для L4+ → **REVISE verdict**, не «короткий — норм». Это структурный gap, не polish. `methodology-critic` Phase 3 проверяет word count + reading-as-textbook-chapter quality.

**Why ENFORCED:**
- 30k = textbook chapter depth (соответствует уровню expectation для серьёзного университетского курса).
- 75-мин лекция проходит ≤40% содержания chapter'а — остальное Q&A backup + self-study + источник для derivation slides/speech.
- Лекции 4-5 = 8.7-8.9k (рано) — owner explicit «недостаточно глубоко».
- Лекция 11 v2 = 13.4k — owner explicit «должен быть как L8/L9, минимум 30k для всех». Решение 2026-05-21, issue #128.

**Enforcement points:**
- Phase 1 plan-checklist выделяет 30k target в plan v1.
- Phase 2 chapter draft — book-editor target 30k.
- Phase 3 methodology-critic проверяет word count: <30k → REVISE; <28.5k для L4+ → P0 BLOCKING.
- Pre-USER-GATE A — word count check в orchestrator walkthrough.

**Связано:** [[feedback_chapter_depth]] (memory rule).

---

## Bilingual Production Rule (ENFORCED — фундаментальное, issue #172, 2026-08-30)

**Источник:** Owner explicit decision (2026-08-30) — курс публикуется публично на **русском И английском** (сайт `tellina-study/publishing`, сессия `cao-course-site`). Владелец выбрал **полный ре-рендер деков на EN** (не только комментарии).

**Правило.** Каждая лекция производится в **двух языках — RU и EN**. RU — source of truth и дефолт; EN — полноценный дубликат, а не машинный подстрочник.

**Обязательные EN-артефакты на лекцию:**
- `speech.en.md` — перевод комментариев/речи.
- `deck.en.yaml` + `slides-en/sNN-*.md` — перевод структуры и текста слайдов.
- `rendered/lec-NN-en.pptx` / `rendered/lec-NN-en.pdf` / `rendered/lec-NN-notes-en.pdf` — ре-рендер EN-дека (тот же визуальный QA-цикл, что и RU).
- `chapter.en.md` (+ `chapter-partN.en.md`) — когда/если публикуется глава (опционально, по решению владельца).

**Naming convention.** RU остаётся без суффикса. EN — суффикс `.en` для `.md`/`.yaml`, `-en` для rendered-бинарников, каталог `slides-en/` для per-slide EN. Не смешивать RU и EN в одном файле.

**Терминология — glossary lock (ENFORCED).** До массового перевода фиксируется единый EN-глоссарий терминов курса (anti-drift на 16 лекций). Переводчики обязаны следовать ему; расхождение термина между лекциями → REVISE.

**Anti-anglicism scope.** Russification / anti-anglicism mandate (§ ниже) применяется **только к RU-артефактам**. Для EN-артефактов английский — целевой язык, deep-latin-scan к ним НЕ применяется. Наоборот: EN-артефакт не должен содержать непереведённых русских фрагментов (mirror-check).

**Counter-check (mandatory):** лекция имеет только RU-артефакты (нет `speech.en.md` / EN-дека) ИЛИ EN-дек содержит русский непереведённый текст → **REVISE**, не «доделаем потом». `consistency-checker` проверяет RU↔EN parity; `fact-checker` — что цифры/факты не потеряны при переводе.

**Применимость:** все существующие лекции (backlog, issue #172) + все будущие. Введение (L1–L3) — EN обязателен так же (это публичный контент, не waiver-able).

**Enforcement points:**
- `tools/lecture-production/README.md` §1 — EN-артефакты в списке финальных + bilingual DoD.
- `templates/lecture-outline.md` — EN-трек в плане лекции.
- Phase gating: EN производится после approve RU-версии (RU — source), отдельной фазой с USER GATE.
- Pre-USER-GATE: RU↔EN parity check (нет пропущенных слайдов/секций; нет непереведённых фрагментов).

---

## Orchestration Rule (ENFORCED)

Claude Code acts as **planner and orchestrator only**. It MUST NOT make implementation changes directly. ALL implementation work MUST be delegated to subagents (Agent tool with appropriate prompts).

**Claude Code does:**
- Plan and design (create/update design docs, issues, plans)
- Research (read files, search code, web search)
- Orchestrate (spawn subagents, review their output, gate phases)
- Communicate (present results to user, ask for approval)

**Claude Code does NOT:**
- Edit source content files directly — subagents do this
- Create/modify documents, lectures, diagrams without delegation

**Exception:** CLAUDE.md, design docs, GitHub issue descriptions, repo scaffolding, and system setup (MCP installation, git operations, `.gitignore`, settings files) may be done directly — these are infrastructure/planning artifacts, not implementation content.

---

## Subagent Rules

**Delegate to subagents:** MCP operations, web research, document editing, diagram creation, content writing, analysis.

**When spawning subagents, always include:**
- Specific MCP tool names the subagent should use
- User email: `kzlevko@gmail.com` (for Google operations)
- Specific file paths (not just directory names)
- Error handling instructions ("if auth fails, stop and report")

**If a subagent fails, FIRST classify the failure, then act (ENFORCED — Лекция 4 lesson):**
- **Usage / rate / quota limit** (agent returns 0 tokens, "You've hit your limit · resets HH:MM", no tool uses) — this is **NOT a subagent failure**. Do **NOT** self-implement, do NOT apply the "do directly" rule. Wait for reset (`ScheduleWakeup`) and **re-delegate the same task**. Orchestrator MUST NOT author implementation content as a limit workaround (specific memory rule `feedback_subagent_usage_limit` overrides the generic rule below).
- **Logic failure** (agent ran but result is unusable / tool error / wrong output) — then do the work directly; do not retry the same delegation verbatim.

**Additional ENFORCED rules:**
- **All critic agents must use 4-level verdict scale:** APPROVE-CLEAN / APPROVE-WITH-POLISH / REVISE / REJECT (replace APPROVE-WITH-MINOR catch-all per Lec 1 lessons). Counter-check: если ≥5 P1 issues но verdict = APPROVE-WITH-POLISH — STOP, change to REVISE.
- **Schema Readability Checklist:** for any schema slide, designer must pass + critic must verify (cross-ref `tools/presentation-build/README.md` §5.5).

---

## Roast-Before-Implement Rule (ENFORCED)

For non-trivial tasks, after planning and before implementation:
1. **ROAST the plan** — self-critique for: over-engineering, unverified assumptions, premature abstractions, missing owners for new files, bundled risky changes that should be isolated
2. **Improve** — fix issues found in roast
3. **Present improvements** — show user the roast findings and proposed changes
4. **Get approval** — user approves improved plan before implementation starts

Key roast questions:
- Is this the simplest version that works?
- Are there unverified external dependencies (APIs, tools, auth)?
- Who owns each new file/process?
- Can risky changes be isolated instead of bundled?

---

## Phase Gating Rule (ENFORCED)

Multi-phase implementations MUST follow this sequence per phase:
1. **Implement** — make the changes
2. **Verify** — validate the result (test, inspect, check consistency)
3. **Gate** — user explicitly approves. Do NOT start next phase until approved.

Never skip verification. Never proceed to next phase without gate.

---

## Pre-USER-GATE Walkthrough Rule (ENFORCED)

Before presenting any USER GATE to user:
1. **Mandatory:** invoke `/pre-user-gate` skill (orchestrator can also do manual walkthrough)
2. **Visual sweep:** для slides — open all PNG snapshots, 5-sec look per slide, can I state main message?
3. **Notes read:** 5-7 random speaker notes — verify 150-300 words connected text, no «Лектору» / no layout descriptions
4. **Cross-artifact grep:** terminology drift, orphan references, pacing math
5. **Designer-extras grep (orchestrator-INDEPENDENT, ENFORCED — Лекция 4 + Лекция 10 lesson):** orchestrator runs its OWN grep over the **rendered pptx visible layer + speaker_notes** (frontmatter exempt) — subagent self-report TOTAL=0 is NOT accepted as verification. Паттерн ОБЯЗАН включать **3 группы**:
   - **Scaffold-фразы:** «Лектору» / «Вы здесь» / `[VERIFY-DAY-OF]` / `[FACT-CHECK]` / `LO[1-9][a-z]?` / `§[0-9]` / `→ s[0-9]+` / `(s[0-9][0-9])` / «точк* возврата» / «— в главе» / «в материалах лекции» / «это payoff» / «возвращаемся [0-9N]» / «не вводи* нов» / «course-scaffold»
   - **Timing-маркеры (ENFORCED Лекция 10):** `\b[0-9]+\s*мин(ут)?\b` (на section dividers / lecture-map / cover / Q&A — все 0); «Время раздел» / «Тайминг» / «Длительность»; «⏱» / «⏰»
   - **Методические комментарии (ENFORCED Лекция 10):** `(методическ|педагогическ)\s*\w+` / «На этом этапе студент» / «Здесь студент усваивает» / «Зачем это в Лекции» / «Этот раздел учит» / «главный методический пункт» / «методическая рамка/ценность/значимость» / «для инженера это означает» (если мета-комментарий, не утверждение из материала)
   All 0 в visible body + speaker_notes (frontmatter exempt). См. [[no-timing-no-methodology-in-slides]].
6. **Keystone-axis check (ENFORCED — Лекция 4 lesson):** несущая концептуальная ось лекции предъявлена **отдельным keystone-слайдом в Разделе 0 ДО первого погружения в неё**? Заголовок + 1-я строка — про саму ось, НЕ про устройство курса / защиту подхода / «мы не вводим нового». Если ось «всплывает» только в середине или это защитный recap — STOP, структурный gap (цена: Лекция 4 = ~5 циклов deck), не polish.
7. **Lec-N-1 pattern compliance (для slides):** does Lec-N have lecture-map slide? section dividers для всех major sections? dedicated Q&A slide? roadmap-bar только на dividers + cover (не на каждом content slide)?
8. **Artifacts в main repo (для GATE B):** `library/lectures/lec-NN/rendered/lec-NN.{pptx,pdf}` MUST exist в main repo path BEFORE opening GATE. If only в worktree → STOP, sync first.
9. **Hero check (ENFORCED — Лекция 8 lesson):** s01 и s39 имеют hero-иллюстрацию (≥40% area, real image via 6-tier acquisition, attribution label visible)? Stylized Ocean card с verbatim headline = mock, FAIL. ([[hero-images-required]])
10. **Deep latin-token scan (ENFORCED — Лекция 8 lesson):** на rendered pptx visible body + speech narrative + chapter body — broad regex + brand allowlist; **pattern-narrow grep НЕ достаточен**. `unique - whitelist = ∅` для narrative body content (URLs / case names / brand markers OK). Sample command: `python3 tools/presentation-build/deep_latin_scan.py <files>`. ([[russification]])
11. **Real-image verification (ENFORCED — Лекция 8 lesson):** sample 5 slides claiming external screenshots → identifiable real source URL? matches what source would show? stylized Ocean-palette card с verbatim headline = mock (FAIL). Per-image acquisition tier documented в `iteration-log.md`. ([[no-mock-fallbacks]])
12. **Baseline / counterfactual coverage check (ENFORCED — Лекция 10 lesson):** sample 5-7 measurable claims (acres / cows / $$ / % / kg / hours) на rendered pptx visible body + speaker_notes + chapter visible — каждый имеет inline baseline или counterfactual? «–50% гербицидов» БЕЗ исходного kg/acre = P1 «missing denominator». «Магнит 46 РЦ» без total Магнит РЦ baseline = P1. «5M acres» без US ag total baseline = P1. **Любое measurable claim без базы = P1 «missing denominator».** Orchestrator самостоятельно проверяет sample; subagent self-report «verified» — недостаточно. См. § «Baseline / Counterfactual Mandate for Measurable Claims».

**Если найдены P0/P1 issues — NOT present GATE.** Spawn revision first, re-run pre-gate, потом present.

**Why ENFORCED:**
- Лекция 1 production имела 3 раунда user feedback ПОСЛЕ critic APPROVE.
- **Лекция 2 production имела 5 раундов user feedback ПОСЛЕ critic APPROVE** на slides — driven by (a) Lec-1 pattern deviations (top bar everywhere, missing lecture-map, missing Q&A), (b) designer-extras leaks (`[VERIFY-DAY-OF]` on PNG, LO codes visible), (c) artifacts not synced to main repo (user opened wrong lecture's PPTX). Pre-gate walkthrough additions points 5-7 prevent these specifically.
- **Лекция 8 production имела 3 owner-интервенции на GATE B** (~3 revision rounds, ~83 мин wasted): (a) 16 stylized mocks вместо real images — self-report «87.2% coverage» прошёл orchestrator sweep, (b) 224 unique англицизмов в PPTX + 919 в speech (narrow grep показал 0-4 hits — pattern-маскировка), (c) missing hero на s01 + s39. Pre-gate additions points 9-11 prevent all 3 specifically.

---

## Orchestrator Self-Critique Rule

When making decisions on behalf of user:
- Slide composition (e.g., «which 4 breakthroughs in s09») — do **freshness pre-check** through web search before committing
- Term renames — do **cascade-of-changes** grep through all artifacts
- Slide adds/deletes — do **curriculum relevance** check (зачем это в лекции N?)
- Visual choices (palette deviations, motif breaks) — defer to designer/user, не decide alone

**Why:** Lec 1 — orchestrator chose Llama-3 + MCP в s09 (refused by user as «not прорывы»). Should have done freshness check.

---

## No Extra Content Rule (ENFORCED for all agents)

Agents do nothing not in task brief. Common temptations to RESIST:

- Designer adding «Лектору» sections, «Вы здесь» markers, timing on visible content, subtitles, callback frames, mini-dividers — FORBIDDEN
- Writer adding terminology variants without cross-artifact sync — FORBIDDEN
- Critic recommending content additions without curriculum relevance check — FORBIDDEN
- Orchestrator implementing «improvements» on behalf of user — FORBIDDEN

If agent SEES opportunity for improvement → REPORT to orchestrator. NEVER implement.

**Why:** Lec 1 had 8 designer-added items removed by user across 2 rounds.

---

## No Timing / No Methodology in Slides (ENFORCED — фундаментальное, 2026-05-21 Лекция 10 owner override)

**Источник:** Owner explicit instruction (2026-05-21, Lec-10 GATE B prep) — «в каждой лекции правлю»; memory `feedback_no_timing_no_methodology_in_slides` ([[no-timing-no-methodology-in-slides]]).

### Запрещено в **visible body** slides + speaker_notes (всё, что видит студент):

**1. Timing-маркеры любого вида:**
- «14 минут · X working cases» на section dividers footer
- «(5 мин)», «(14 мин)», «(15 мин)» в roadmap / lecture-map
- «75 минут», «10 минут Q&A» на cover / Q&A slide
- «⏱», «⏰», «Время раздела», «Тайминг», «Длительность»

**2. Методические комментарии любого вида:**
- «**методически** важно/значимо/неверное/важная мысль»
- «**педагогическ**ая цель / задача»
- «**главный методический пункт**», «**методическая рамка/ценность**», «**методический урок**»
- «**На этом этапе студент должен**», «**Здесь студент усваивает**»
- «**Зачем это в Лекции** N», «**Этот раздел учит**»
- «**Для инженера это означает**» (если используется как «мета-комментарий», не как утверждение из материала)
- «**Лектору**», «**Преподавателю**», «**Вы здесь**»

### Где timing/методология ВОЗМОЖНЫ (exempt):

- **frontmatter** `.md` (`duration_min`, `timing_min`, `learning_outcomes`, `learning_goal` — это metadata для оркестрации)
- **`deck.yaml`** `timing_min` / `chapter_ref` — metadata
- **`speech.md`** Phase 9-11 — речь лектора может содержать методологический discourse
- **plan files** / **critic reports** / **iteration-log.md** — planning artefacts

### Что писать вместо:

- **Section divider:** смысл раздела одной строкой + tag «3 working cases · 2 провала» (БЕЗ минут).
- Вместо «Методически важно X» — просто X. Если утверждение значимо — оно само звучит важно.
- Вместо «На этом этапе студент должен Y» — переформулируй как сам тезис Y.

### Enforcement points:

- **Pre-USER-GATE Walkthrough Rule §5** — расширено явным запретом timing + методологии (см. ниже)
- **`.claude/agents/presentation-designer.md`** — explicit no-timing / no-methodology mandate в каждый prompt
- **Pre-USER-GATE B/C independent grep** — паттерны:
  - `\b[0-9]+\s*мин\b` / `Время раздел` / `Тайминг`
  - `(методическ|педагогическ)\s*\w+`
  - «На этом этапе» / «Лектору» / «Преподавателю» / «Зачем это в»

### Cost-of-omission

Пользователь правил каждую лекцию L1-L9 + L10 (10× × ~10-15 мин cleanup) = ~2-3 часа wasted user time. Поэтому правило **фундаментальное**.

---

## Baseline / Counterfactual Mandate for Measurable Claims (ENFORCED — 2026-05-21 Лекция 10 owner override)

**Источник:** Owner explicit instruction (2026-05-21, Lec-10 GATE B prep) — «во многих оценках эффектов/потерь не хватает базы. а сколько на человека или без робота? а сколько было?».

**Правило.** Каждое **измеримое количественное утверждение** (acres / cows / $$ / % / kg / hours / времена) в всех 3 артефактах (chapter / slides / speech) ОБЯЗАНО иметь **базу** или **counterfactual**:

- «5M акров See & Spray» → **сколько было до See & Spray? сколько без selective spray? per-acre herbicide baseline?**
- «–50% гербицидов» → **от какого исходного значения? стандартное применение X kg/acre → Y kg/acre?**
- «Plenty $940M потерь» → **vs raised $X total? vs industry baseline VF capex?**
- «Monarch 102 layoffs (38%)» → **38% от какого пика workforce? в какой момент?**
- «Cargill $32k saved per trade» → **per annual hedge volume? total Cargill hedging $?**
- «Магнит 46 РЦ Forecasting» → **из скольких всего РЦ Магнит? denominator?**
- «Saga 20% UK strawberry» → **от какого total UK strawberry production? в каких единицах?**
- «X5 200 факторов прогноза» → **vs baseline без ML? accuracy improvement vs предыдущая система?**

### Что нужно (template):

| Утверждение | База / counterfactual | Источник |
|---|---|---|
| «5M acres See & Spray» | До 2021 (commercial launch): 0; baseline без selective = blanket spray на 100% поля | Deere press / Blue River timeline |
| «–50% non-residual herbicide» | Industry baseline blanket spray ≈ 1 lb/acre AI; selective ≈ 0.5 lb/acre | Deere field trial data |
| «Plenty $940M потерь» | $1B+ raised since 2014; total VF category $1.37B+ потерь 2025 | TechCrunch + AgFunder |
| «Cognitive Pilot 1700+ установок» | Total комбайнов в РФ ≈ 130k (Минсельхоз); penetration ≈ 1.3% | Минсельхоз stats + Cognitive Pilot press |

### Применимость:

- **Все 3 артефакта** (chapter / slides / speech) — каждое measurable claim либо имеет inline baseline, либо помечено «[VFY-baseline]» как known gap
- **Critics** (methodology + fact-checker) должны flag claims без baseline как **P1 «missing denominator»**
- **Pre-USER-GATE walkthrough** — добавлен check «baseline coverage» (sample 5-7 measurable claims → есть ли base?)

### Cost-of-omission:

Без базы цифры выглядят впечатляюще, но инженерно недостаточны для оценки **реального** effect size. Студент не может сравнить «5M acres» с total US ag acres (≈900M) — это 0.55%. «–50% гербицидов» без kg/acre baseline — не интерпретируется. **Это структурный gap, не polish.**

---

## Anti-Patterns (NEVER DO THESE)

| Anti-Pattern | Correct Approach |
|--------------|------------------|
| Push to main directly | Always use feature branches + PRs |
| Work without a GitHub Issue | Every task gets an issue, no exceptions |
| Store task state only in memory | GitHub Issues are source of truth |
| Skip issue creation for "quick" tasks | Every task gets an issue |
| Bundle risky changes together | Isolate risky changes into separate branches/PRs |
| Make implementation changes as orchestrator | Delegate all implementation to subagents |
| Skip roast step for non-trivial work | Always roast before implement |
| Proceed without phase gate approval | Wait for explicit user approval between phases |
| Designer-added extras без brief (subtitle, «вы здесь», тайминг, «Лектору») | Producer agents REPORT improvements, не apply (см. No Extra Content Rule) |
| Speaker notes как layout description («слева donut, справа bar») | Notes — readable student text 150-300 слов, derived from chapter+speech |
| Critic catch-all APPROVE-WITH-MINOR | 4-level verdict scale: APPROVE-CLEAN / APPROVE-WITH-POLISH / REVISE / REJECT |
| Term drift без cascade tracking | Glossary lock после chapter approval; cascade-of-changes grep при renames |
| `[VERIFY-DAY-OF]` / `[FACT-CHECK]` / LO codes / `§X.X` / `→ sNN` visible to students в body | Frontmatter / speaker_notes only; pre-render grep enforce 0 hits в visible body |
| Designer making independent decisions diverging from Lec-N-1 pattern | Lec-N-1 reference read MANDATORY at start of Lec-N design; match unless explicit divergence approval |
| Top progress bar / navigation bar на каждом content slide | Only on section dividers + cover (Lec-1 pattern) |
| Missing lecture-map / dedicated Q&A / section dividers для всех major sections | Lec-N-1 slide-type inventory matches by default |
| Hook outdated empirical test (strawberry-type, 2026 models pass) | 2026-evergreen visualization / cost-asymmetry / concept-reveal preferred; Hook Engagement check at plan stage |
| Missing concept fundamentals (attention matrix, embedding space, end-to-end flow) | Missing-Fundamentals check в methodology-critic per concept |
| Insufficient stock illustrations (text-heavy deck) | 5-10 supportive visual assets baseline in presentation-designer DoD |
| Artifacts only in temp worktree (not main repo) at GATE | Pre-USER-GATE artifacts sync mandatory (memory rule [[feedback-pre-gate-render-artifacts]]) |
| Branch contention from parallel session (shared `.git`) | Git worktree isolation mandatory для multi-lecture parallel |
| 5+ user feedback rounds на slides | Plan critique + Phase 7 critic checklists must include Lec-N-1 pattern + hook quality + missing-fundamentals checks |
| Per-artifact spawns for polish rounds (separate designer / writer per phase) | Single batched revision agent (book-editor OR speech-writer) для 3-artifact touches; Phase 11 pattern |
| Лекция < 30% контента про провалы/ограничения/альтернативы ИЛИ доля в одном артефакте | ≥30% holistic (chapter+slides+speech), иначе verdict REVISE (см. AI-Failure & Judgment Content Rule) |
| «Магическая пилюля»: ИИ-восторг без выученных уроков и границ применимости | Каждая лекция учит говорить «нет» неподходящему ИИ; ≥30% — провалы/ограничения/альтернативы |
| chapter.md <30k слов для L4+ (single-file 8-12k или multi-part 20-26k) | ≥30 000 слов mandatory (target 28 500-31 500); split на 4-5 частей по 6 500-8 500 слов; <28 500 = P0 BLOCKING REVISE (см. § «Chapter Depth Baseline (ENFORCED)», issue #128) |
| Timing на visible body slides («14 минут · X cases» на dividers / «(5 мин)» в lecture-map / «75 минут» на cover / «10 минут» на Q&A / ⏱) | Timing **ТОЛЬКО** в frontmatter / deck.yaml / iteration-log / plan files. Section dividers — смысл раздела + tag «X working cases · Y провала» БЕЗ минут (см. § «No Timing / No Methodology in Slides») |
| Методические комментарии в visible body slides («методически важно», «главный методический пункт», «педагогическая цель», «на этом этапе студент должен», «зачем это в Лекции N», «Лектору», «Преподавателю») | Только в speech.md / plan files / critic reports. Visible body — материал, не диалог-сценарий с лектором (см. § «No Timing / No Methodology in Slides») |
| Measurable claim без базы / counterfactual («–50% гербицидов» без kg/acre baseline; «5M acres» без US total ag baseline; «Магнит 46 РЦ» без denominator) | Каждая измеримая claim ОБЯЗАНА inline baseline или counterfactual: «–50% от X kg/acre до Y kg/acre», «5M из ≈900M US ag acres = 0.55%», «46 из N total Магнит РЦ» (см. § «Baseline / Counterfactual Mandate») |
| Несущая ось лекции не предъявлена отдельным keystone-слайдом до 1-го погружения (Раздел 0 защищается/делает recap вместо подачи оси) | Keystone-axis ENFORCED-check: methodology-critic (Phase 1 plan + Phase 4/7 deck) + lecture-outline template + Pre-USER-GATE п.6. Цена пропуска: Лекция 4 = ~5 циклов deck |
| Отраслевая лекция (L4+): несущая таксономия без named current tools на каждый уровень; plan §-named speech-narrative без слайда | lecture-outline (L4+) требует tools-per-taxonomy-level (вендор-режим+adoption-направление+anti-hype+mode≠brand, volatile→[VFY-day-of]); Phase-5: §-named narrative ⇒ слайд либо явное owner-обоснование устного якоря |
| usage/rate-limit субагента трактуется как failure → оркестратор пишет контент сам | Классифицировать сбой: limit ≠ failure → wait+re-delegate, НИКОГДА не self-implement (Subagent Rules; `feedback_subagent_usage_limit`) |
| lectures.yaml lec-NN→produced забыт после GATE C (батчится отдельным manifest-PR) | GATE-C definition-of-done включает manifest status→produced (в том же финализирующем PR) |
| Designer fallback to stylized mocks при paywall/JS-block | 6-tier real image acquisition (og:image / Wikipedia / press release / YouTube thumb / Wayback / Google Images); per-image honest log при failure ([[no-mock-fallbacks]]; `tools/presentation-build/README.md` §5.7) |
| Excessive англицизмы в visible body / speaker notes для RU-аудитории МГТУ ИУ6 | Anti-anglicism mandate в каждом producer prompt + Russification таблица 45+ + deep latin-token scan (не только pattern grep); explicit keep-list (brand names + established acronyms с inline gloss + mode names) ([[russification]]; `tools/presentation-build/README.md` §5.8) |
| Text-only s01 (ice-breaker) или s39 (closing) без hero иллюстрации | Hero ≥40% area на s01 + s39 для всех deck'ов курса; real image via 6-tier acquisition; foreshadow keystone (s01) / bridge к Lec-N+1 (s39) ([[hero-images-required]]; `tools/presentation-build/README.md` §5.9) |
| Pattern-narrow grep как verification «deck clean от anglicisms» | Deep latin-token scan (any English word вне brand allowlist) для RU-language deck — narrow pattern grep маскирует depth (Лекция 8: narrow 32 patterns = 0-4 hits, deep scan = 919 unique в speech) |
| Subagent claim «X% media coverage» trustworthy | Orchestrator visually verifies sample slides + checks real-source identifiability (Лекция 8 lesson: mocks с verbatim headlines прошли coverage check, но не real images) |

---

## Multi-Lecture Parallel Production (ENFORCED)

When starting Lec-N production while Lec-(N-1) или Lec-(N+k) is still в active production (parallel session с shared `.git`):

1. **Use git worktree isolation MANDATORY:**
   ```bash
   git worktree add --detach /tmp/lec-NN-wt <base-commit>
   cd /tmp/lec-NN-wt && git checkout -b phase-X-Y
   ```

2. **Agent prompts must include explicit working directory:**
   - «cd /tmp/lec-NN-wt FIRST»
   - «git branch --show-current should return phase-X-Y»
   - «If branch changes mid-session → STOP, report (don't recover)»

3. **Artifacts sync to main repo BEFORE every USER GATE:**
   - Copy from worktree to `/home/levko/AI-usage-lessons/library/lectures/lec-NN/rendered/`
   - Verify via `ls -la library/lectures/lec-NN/rendered/lec-NN.{pptx,pdf}`
   - GATE cannot open без main-repo artifacts accessible (memory rule [[feedback-pre-gate-render-artifacts]])

4. **Branch ref management через `git update-ref`:**
   - После phase commits в worktree → `git update-ref refs/heads/issue-NN-lec-NN <commit-sha>` from main repo
   - Это propagates branch HEAD без requiring main worktree checkout (avoids contention)

5. **Final merge:** push branch + create PR + merge after USER GATE C.

**Why ENFORCED:** Лекция 2 production имела ~2 hours wasted на branch contention recovery (lec-04 parallel session, shared `.git`). Worktree isolation после Phase 8.5 полностью eliminated issue.

---

## Document Size Limit (ENFORCED)

**No single document may exceed 600 lines.** If a document grows beyond 600 lines, split it into logical parts with cross-links. Code files are exempt but should still favor smaller, focused modules.

---

## Chapter Depth Baseline (ENFORCED — фундаментальное, issue #128, 2026-05-21)

**Источник:** Owner explicit override (Лекция 11 production); reference — memory `feedback_chapter_depth` ([[chapter-depth]]).

**Правило.** `library/lectures/lec-NN/chapter.md` для **L4+** — **минимум 30 000 слов** (target 30k ±5% = **28 500–31 500**). Это базовый референс уровня academic textbook chapter + Q&A backup + self-study deep-dive материал, **не конспект 75-мин лекции**.

**Что засчитывается в 30k:**
- Narrative body всех частей (chapter.md + chapter-part2.md + chapter-part3.md)
- Inline definitions / examples / case studies / failure deep-dives / cornerstone glossary
- Q&A backup ответы (раздел § Q&A)

**Что НЕ засчитывается:**
- Frontmatter YAML
- Markdown headings без содержания
- TOC / list-only sections
- Источники / bibliography (отдельный счёт `references_count`)

**Применимость:**
- **L1–L3 (introductory):** 8–12k acceptable; owner waiver доступен (аналогично AI-Failure rule).
- **L4–L17:** ≥30k mandatory, **waiver недоступен**. <28 500 слов → **P0 BLOCKING REVISE** (структурный gap, не polish).

**Why ENFORCED:** chapter = source-of-truth + Q&A резерв преподавателя + источник derivation slides/speech. На 75-мин лекции реально проходится **30–40% содержания chapter'а** — остальное Q&A backup + self-study + источник derivation. 30k = textbook chapter depth, соответствует уровню expectation для серьёзного университетского курса.

**Enforcement points:**
- **Phase 2 brief для book-editor:** explicit «target ≥30 000 слов», expansion mandates per section с конкретикой по deltas.
- **Phase 3 methodology-critic:** word count check; <28 500 для L4+ → P0 BLOCKING.
- **Pre-USER-GATE A walkthrough:** word count verify в orchestrator self-review.
- **Anti-Patterns table** — добавлено «chapter <30k для L4+».

**Эволюция правила:**
- Лекции 1–3 (introductory): ~8–12k слов.
- Лекции 4–5: 8.9k / 8.7k слов (ранний стиль single-file).
- Лекции 6–7: 12.7–12.9k слов.
- Лекции 8–9: 15.9k / 17k слов.
- Лекция 11 production 2026-05-21: owner override → **минимум 30k для всех L4+**.

**Старый red-flag «>15k слов»** из `tools/lecture-production/README.md` для L4+ — **НЕ применять** (обновлено issue #128).

---

## Chapter Multi-Part Pattern (ENFORCED — Lec-4/5 lesson)

**Все `library/lectures/lec-NN/chapter.md` для L4+ пишутся multi-part структурой** (4-5 частей при ≥30k слов; lec-04/lec-05 эталоны — 3 части, но lec-04/05 были 22-26k; для ≥30k baseline частей нужно 4-5).

### Структура

```
library/lectures/lec-NN/
  chapter.md          ← Часть 1 (≤600 строк, ~7-9k слов; frontmatter; § Введение + первые 1-2 раздела)
  chapter-part2.md    ← Часть 2 (≤600 строк, ~6-9k слов; средние разделы)
  chapter-part3.md    ← Часть 3 (≤600 строк, ~7-9k слов; финальные разделы + Q&A + Reading list + References)
```

### Обязательные элементы

1. **Frontmatter в `chapter.md`** включает: `parts: 3`, `length_words: ~XX000`, `slide_map`, `strict_in_self_estimate`, `lo: [...]`.
2. **Карта главы и индекс частей** — в `chapter.md` сразу после Changelog: оглавление 3 частей с cross-links.
3. **`## Оглавление (Часть N)`** в начале каждой части.
4. **Каждый файл ≤600 строк** (CLAUDE.md doc-size limit) — НЕ исключение для chapter; split строго принудительный.
5. **Slide-маркеры `[for-slide-sNN]`** — на каждом ≥150-слов разделе как Phase 5 anchor для speaker notes.
6. **Cross-references между частями:** «(см. §X.Y в части 2)» / «см. Часть 3 §Z» / forward-anchors / `[FACT-CHECK]` / `[VFY-day-of]` маркеры — все strip-safe (в конце клауз).
7. **Целевой word count:** **≥30 000 слов** total (см. § «Chapter Depth Baseline (ENFORCED)») — типично 4-5 частей по 6 500–8 500 слов. Lec-04/05 эталон 3-частной структуры был при 22-26k baseline; для ≥30k обычно нужно 4 части.

### Cost-of-omission

- **Lec-04 lesson:** chapter.md 23 700 слов в одном файле = unmanageable, methodology-critic не успевает прочесть, downstream cascade (speech/slides revise) ломается. Split → 3 файла → atomic edits, parallel critic-passes, диффы читаемы.
- Apply by default для всех новых лекций — не ждать пока документ перерастёт 600 строк.

---

## Best Practices Documentation

**Reference:** `notes/decisions.md` — accumulated findings, patterns, and anti-patterns.

### Update Rule
Every time a new finding, gotcha, or best practice is discovered during work, it MUST be added to `notes/decisions.md`. Before starting work, CHECK this file for existing findings relevant to your task.

---

## MCP Limitations Catalog (ENFORCED)

**Reference:** `notes/mcp-limitations.md` — централизованный каталог известных багов, отсутствующих фич и обходов в MCP-серверах + render-toolchain'е.

### Update Rule (обязательная актуализация)
Каждый раз, когда обнаружена новая limitation MCP-сервера или render-инструмента (failed tool call с явной причиной, баг внутри сервера, отсутствующая capability, render artifact), она **должна быть добавлена в `notes/mcp-limitations.md`** в той же сессии. Использовать готовый шаблон записи (см. начало файла).

### Read Rule (обязательная проверка)
**Перед использованием MCP-tool, который ранее давал проблемы**, или **в начале работы с малознакомым MCP-сервером**, агент **обязан** прочитать соответствующий раздел `notes/mcp-limitations.md`.

Это касается всех агентов (`presentation-designer`, `presentation-critic`, `librarian`, `course-curator`, `doc-editor`, `issue-manager`, `student-simulator`, `reader-simulator`) и Claude как orchestrator.

---

## Working Conventions

### Subagents (`.claude/agents/`)

**General-purpose / infrastructure:**
| Agent | Responsibility |
|-------|---------------|
| `librarian` | Search, sync, export, index documents |
| `course-curator` | Link normative docs, lectures, materials, assignments |
| `doc-editor` | Edit Google Docs via workspace-mcp |
| `issue-manager` | Create/triage GitHub Issues, track change queue |

**Lecture production (multi-artifact: chapter + slides + speech):**
| Agent | Producer/Critic | Responsibility |
|-------|---|---------------|
| `book-editor` | Producer | Пишет/правит главу методички (`chapter.md`, ≥30k слов для L4+, см. § Chapter Depth Baseline) |
| `presentation-designer` | Producer | Визуальный дизайнер deck'а — рендер через PowerPoint MCP с visual-loop, Ocean palette + Anthropic anti-patterns |
| `speech-writer` | Producer | Пишет речь лектора (`speech.md`, ~5k слов, conversational) |
| `methodology-critic` | Critic | Pedagogical depth, LO coverage, sequence, assertion-evidence (применяется к chapter, plan, slides, speech) |
| `fact-checker` | Critic | Проверка фактов, цифр, дат, citations (использует WebSearch для verification) |
| `presentation-critic` | Critic | Методико-визуальный ревью slides (vision-enabled) |
| `student-simulator` | Critic | Симулирует студента в зале (PNG + speaker notes) |
| `reader-simulator` | Critic | 2 режима: `text-only` (md без рендера) и `rendered` (PNG+notes через 2 нед) |
| `consistency-checker` | Critic | Cross-artifact alignment: chapter ↔ slides ↔ speech |

### Lecture Production Pipeline (ENFORCED, multi-artifact)

**Canonical doc:** `tools/lecture-production/README.md` — полный 10-фазный pipeline для production лекции с **3 финальными артефактами**:
1. `library/lectures/lec-NN/chapter.md` — глава методички (**≥30k слов** для L4+ per § Chapter Depth Baseline, **source of truth**, academic textbook chapter; multi-part split при >600 строк).
2. `library/lectures/lec-NN/rendered/lec-NN.pptx` — презентация со speaker notes (derived from chapter).
3. `library/lectures/lec-NN/speech.md` — речь лектора (~5k слов, conversational; derived from chapter+slides).

**Source of truth: book-first.** Chapter — primary, slides + speech derive. При conflict — fix slides/speech (если chapter сам не ошибается).

**3 USER GATEs** между phases 4-5 (chapter approved), 8-9 (slides approved), 11 (final). Не двигаться к следующей фазе без explicit user approval. **GATE-C definition-of-done (ENFORCED — Лекция 4 lesson):** финализирующий PR обязан включать `catalog/manifests/lectures.yaml` lec-NN status → `produced` (не оставлять как забытый follow-up для отдельного manifest-PR).

**Phase 9.5 (Pre-USER-GATE walkthrough)** — orchestrator must run pre-gate review before EACH USER GATE (см. `tools/lecture-production/README.md` + Pre-USER-GATE Walkthrough Rule выше).

**Critic agents применяются на каждом этапе** (промежуточные + финальные результаты — обязательное требование).

### Presentation Pipeline (slides-specific subset)

**Single source of truth:** `tools/presentation-build/README.md` — slides-specific pipeline + slide-types library (8 типов) + visual-loop workflow + 12-section design playbook + anti-patterns + tool catalog.

Используется в **Phase 5-8** lecture-production pipeline.

**Stack:**
- **Render-target:** PowerPoint (PPTX) через `office-powerpoint-mcp-server` (GongRzhe, `uvx`-установка, 37 tools).
- **Source-of-truth:** `library/lectures/lec-NN/deck.yaml` + `slides/*.md` (repo-first; Drive — только publish target, отложено).
- **Visual generation:** Generate→Convert (libreoffice + pdftoppm)→Inspect (Claude vision)→Fix цикл, **минимум 3 итерации на слайд** (Anthropic principle).
- **Visual elements:** PowerPoint MCP shapes + QuickChart API (charts) + mermaid CLI (diagrams) + ImageMagick + librsvg2-bin (icons recolor) + Lucide/Heroicons/Phosphor/LobeHub CDN.
- **Palette LOCKED:** Ocean Gradient (`#21295C` / `#065A82` / `#1C7293`) + Teal `#028090` secondary + Gold `#F0AB00` highlight ≥1×/слайд.
- **Visual motif:** «Ocean rounded box» (radius 12, surface `#F4F7FA`, stroke `#1C7293`) на каждом content слайде.

**Workflow:** `/build-deck N` — orchestrator-skill, спавнит `presentation-designer` для рендера + 3 QA agents (`presentation-critic` + `student-simulator` + `reader-simulator` mode=rendered) параллельно. `reader-simulator` mode=`text-only` запускается ДО рендера для методического контроля.

**Required reading для любого agent'а, работающего со слайдами:** `tools/presentation-build/README.md` (агенты начинаются с явной ссылки на этот файл). Также обязательно `notes/mcp-limitations.md` (PowerPoint MCP gotchas) и `notes/decisions.md` § «2026-05-12 — Presentation pipeline» (anti-patterns каталог).

### Skills (`.claude/skills/`)

Eight core skills: `sync-library`, `catalog-docs`, `extract-links`, `update-lecture`, `build-deck`, `diagram-refresh`, `issue-from-change`, `impact-check`.

Skills are invoked via `/skill-name` (e.g., `/sync-library`). Each SKILL.md must be an executable recipe with concrete MCP tool names and parameters, not just a description of steps. If a skill cannot be executed as-is, it needs implementation work.

### Repository Layout

```
catalog/         — exported Google artifacts and RAG index
  exports/       — docs/, sheets/, slides/, pdf/
  index/         — knowledge-rag index data
  manifests/     — documents.yaml, lectures.yaml, decks.yaml, diagrams.yaml
diagrams/        — canonical .drawio files and exports
library/         — source materials: normative/, lectures/, materials/, project/
ontology/        — RDF schema (TTL), vocab, SPARQL queries
templates/       — reusable templates for lectures, slides, issues, requirements
workflows/       — routine descriptions, checklists, triage rules
notes/           — decisions, limitations, experiments log
```

### Ontology (Oxigraph)

**Entities:** Document, Section, Requirement, Lecture, SlideDeck, Diagram, Task, Topic

**Relations:** cites, covers, illustrates, depends_on, supersedes, tracked_by, belongs_to_topic

**Attributes:** source_url, source_system, updated_at, status, owner, version_label

Keep ontology minimal — store structural facts and references only, never duplicate document text in RDF.

## File Conventions

- Always save raw document exports to `catalog/exports/docs/` before any processing or ingestion
- Always save `.drawio` diagrams to `diagrams/` — never just open in browser without saving the XML file
- Update `catalog/manifests/*.yaml` after every export or ingestion operation
- Use `ingest_file` (from saved local path), not `ingest_data` (from strings) — file-based ingestion creates traceable provenance
- **Creating Google Docs:** use `import_to_google_doc` with `source_format="md"`, NOT `create_doc`. The import tool converts markdown headings, bold, lists, tables to native Google Docs formatting. `create_doc` inserts raw text with no formatting.

## Security Rules

- `catalog/exports/` must NEVER be committed to a public repository (contains exported Google docs).
- Limit `workspace-mcp` to read-heavy mode initially; write only for owned Docs/Sheets/Slides.
- GitHub MCP: restrict to repo/issues/PR toolsets, no org/admin scopes.
- No API keys, tokens, or credentials in committed files.

## Daily Cycle

1. **Sync:** `sync-library` skill pulls changes from Google Drive
2. **Catalog:** `catalog-docs` + `extract-links` update index and ontology
3. **Tasks:** changes trigger `issue-from-change` to create/update GitHub Issues
4. **Content:** `update-lecture`, `build-deck`, `diagram-refresh` as needed

## Weekly Cycle

- `impact-check` — what changed and what it affects
- Issue triage via `issue-manager`
- Update `notes/decisions.md`

## Reflection Process

After each working session:
1. Create `notes/reflections/{date}-{topic}/` folder (or `notes/reflections/{topic}.md` for single-file reflections)
2. Write separate reflection files per area: tools, workflow, content, user-feedback
3. Update `notes/decisions.md` with key findings from reflections
4. Reflections feed into next session's improvements — always check `notes/reflections/` before starting work
