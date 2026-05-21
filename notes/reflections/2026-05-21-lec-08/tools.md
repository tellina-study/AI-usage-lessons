# Лекция 8 — рефлексия по tools

**Дата:** 2026-05-21
**Лекция:** 8 «AI в креативных индустриях и медиа»

## Что работало

### PowerPoint MCP + libreoffice + pdftoppm visual loop
Generate (PowerPoint MCP / python-pptx через build_lec08.py) → Convert (libreoffice → pdf, pdftoppm → png) → Inspect (Claude vision на PNG) → Fix цикл. **Работал стабильно** — 39 слайдов × 3+ итерации без crashes. Build script (2196 строк после revisions) — single point of truth для visual layout, легко применять bulk edits.

### 6-tier image acquisition (после [[no-mock-fallbacks]])
- **Tier 1 (og:image direct):** 87.5% success rate (14/16). Метатег `og:image` присутствует на почти всех modern article pages и не блокируется paywall.
- **Tier 2 (Wikipedia/Wikimedia Commons):** 2/16 (Kelly McKernan plaintiff portrait, X-62 VISTA F-16 для s39 hero).
- **Tier 3 (Press release):** 1/16 (Nature paper Fig 1 with referer header).
- **Tier 4 (YouTube thumbnails):** 4/16 (Sora 2 mammoths, Toys R Us, Coca-Cola Holidays + Secret).
- **Tier 5 (Wayback Machine):** 2/16 (NYT HQ photograph когда live NYT 403'd).
- **Tier 6 (Google Images):** не понадобилось.

**Anti-bot bypassed sites:** BBC, Futurism, NYT, Reuters, ArsTechnica, TechCrunch, Wired, Hollywood Reporter, WSJ, Adobe — все 403/blocked напрямую. Bypassed via Tier 2-5 (DWT, PBS, Variety, Billboard, Wayback, YouTube CDN, Wikipedia).

**Insight:** og:image — universal solution. Каждая publication имеет og:image для social media preview. Curl + grep meta tag + curl image URL — без anti-bot blocks почти всегда работает.

### Independent orchestrator verification (deep grep)
Python-pptx + regex broad pattern scan на rendered pptx visible body — обнаружил 3 designer-extras leaks где designer self-report заявлял TOTAL=0. Ловит class ошибок которые subagent self-grep пропускает.

### Single batched revision agent (Phase 11)
Per CLAUDE.md anti-pattern «Per-artifact spawns for polish rounds», one book-editor agent смог touch chapter + slide MD + speech одним проходом для consistency fixes (4 P0 + 7 P1 + 5 P2). Эффективнее чем 3 separate agents.

### Worktree isolation
`/tmp/lec-08-wt` для Лекции 8, `/tmp/lec-09-wt` для Лекции 9 параллельно. Zero conflicts при общем `.git`. Push через `git push -u origin BRANCH` напрямую, merge через `gh pr merge` без проблем.

---

## Что не работало / создавало friction

### Subagent self-report не trustworthy для visual quality
Designer subagent заявлял «87.2% media coverage» — но coverage = visual area, не real-image presence. Stylized mock с verbatim headline = «visual mass» но не «real image». **Lesson:** measurement spec должен включать explicit «real source URL recorded per image», не агрегированную % метрику.

### Designer self-grep на forbidden phrases был too narrow
Designer заявлял TOTAL=0 на forbidden phrases — но проверял только узкий list. Реальные leaks: `(s9 caveat)` (без leading zero в slide ref regex), `s21-s27` range refs, «keystone» жаргон, «failure budget» pill, «sensitive case» мета-комментарий. **Solution:** orchestrator делает independent grep с broader patterns (per [[feedback-pre-gate-render-artifacts]] + [[no-mock-fallbacks]] + Лекция 4 lesson).

### Speech-writer attempt at Russification slabый
Speech-writer agent создал draft с 72 anglicism hits на 32-pattern check; deep latin-token scan показал 919 unique non-allowlist Latin tokens. Agent оставлял англицизмы потому что: (a) speech derived from chapter которая сама содержала англицизмы, (b) спорные «legal terms preserved verbatim» decision самостоятельно, не consulting [[russification]] таблицу.

### Pattern-narrow grep маскирует depth of problem
Orchestrator-independent grep с 32 patterns Russification таблицы вернул 4 hits на speech (после revision); deep latin-token scan показал 919. Difference: pattern grep ловит **только specific phrases** из заранее известного списка; latin-token scan ловит **любое English слово** вне brand allowlist. **Solution:** для media-heavy / Russian-language deck требуется latin-token scan, не только pattern grep.

### Pre-commit hook secret-scanner false positives
Pre-commit hook flag-нул content phrases как «possible secrets» (e.g., specific case quotes, lesson texts). Warning не блокировал commit, но создаёт шум. **Possible fix:** настроить hook на specific patterns или whitelist content directories.

---

## Tools / scripts created during this production (worth preserving)

- `library/lectures/lec-08/rendered/build_lec08.py` (2196 строк) — comprehensive deck builder, can serve as template для будущих лекций (особо: `add_image()` helper, layout functions для case_with_metric, taxonomy_2x2, citation_card patterns)
- `library/lectures/lec-08/rendered/generate_assets.py` — Pillow PNG generation (был использован для mocks; не нужен в production но useful как fallback)
- `library/lectures/lec-08/rendered/russify.py` + `russify2.py` — automation scripts для bulk Russification (sed-style replacements)
- `library/lectures/lec-08/rendered/image-acquisition-log.md` — per-slide Tier log; pattern для будущих deck'ов
- `library/lectures/lec-08/rendered/russification-deep-log.md` — replacement log

---

## Suggested tool improvements

### `tools/presentation-build/` 
- Add `templates/image-acquisition.py` — reusable 6-tier image fetcher
- Add `templates/russification-check.py` — deep latin-token scanner
- Add `templates/build-helpers.py` — extracted helper functions из build_lec08.py (Ocean palette constants, add_image, add_ocean_box, etc.)

### Build script structure
build_lec08.py разросся до 2196 строк — это monolith. Suggestion: разбить на:
- `helpers.py` — palette constants, common shape builders
- `slide_NN_section.py` — per-section slide builders (Section 0/1/2/3/4/5)
- `build.py` — orchestration only

Это уменьшит cognitive load при revision passes.

### Pre-USER-GATE skill update
[[pre-user-gate]] skill должен включать:
1. Visual sweep checklist с **«is this a REAL image or a mock?»** explicit check
2. Deep latin-token scan command snippet
3. Hero check на s01/s39
4. Real-image attribution check (source label visible per slide)
