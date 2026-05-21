# content.md — Лекция 9 production

## Documents produced

### Final artifacts (3)
- `library/lectures/lec-09/chapter.md` v4 — 994 строки, 17 000 слов, 104 источника
- `library/lectures/lec-09/deck.yaml` v3 + 35 `slides/*.md` + `rendered/lec-09.{pptx,pdf}` + 35 PNGs
- `library/lectures/lec-09/speech.md` v2 — 862 строки, ~6600 spoken words

### Research artifacts
- `notes/research/lecture-9/` — 6 files, 1820 строк, 110 unique source URLs

### Phase critique artifacts
- `notes/lecture-9-review/` — 16 files:
  - plan-of-attack v0, plan v1+v2, SYNTHESIS-plan-v1
  - critique-of-v1-methodology + reader-text (Phase 1)
  - critique-of-chapter-v1-methodology + fact-checker + reader-text (Phase 3) + SYNTHESIS-chapter-v1
  - critique-of-chapter-v2-fact-checker-subset (Phase 4.5)
  - pre-gate-A-walkthrough
  - critique-of-slides-v2-presentation + student-sim + reader-rendered + consistency + fact-checker (Phase 7) + SYNTHESIS-slides-v2
  - critique-of-slides-v3-consistency (Phase 8.5 retry)
  - pre-gate-B-walkthrough
  - critique-of-speech-v1-methodology + fact-checker + consistency (Phase 10) + SYNTHESIS-speech-v1
  - pre-gate-C-walkthrough

### Manifest update
- `catalog/manifests/lectures.yaml` lec-09 → produced (включён в финализирующий PR per Лекция 4 lesson)

## Quality assessment

### Strengths
- **Keystone-axis discipline ENFORCED** — OODA Sense→Decide→Act + Boyd 1976 sourcing предъявлена первым content slide (s05), identical across 3 артефакта, closing callback на s42. Лекция 4 cost-of-omission (~5 циклов deck) полностью предотвращена.
- **Strict-in distribution holistic** — chapter 45-46%, slides 32-38%, speech 81% (после Russification revealed real strict-in budget). Все ≥30% target.
- **9 canonical failure-blocks с уроками** consistent across artifacts.
- **17 real photos** Wikimedia CC-BY-SA — feedback_no_mock_fallbacks применён.
- **Anonymization v3** — chapter обезличен per user feedback, 0 named institutions (lec-07 pattern).
- **§4.7 narrative rebuilt** — устаревший «3 стран против UN LAWS» (2024) → актуальный «6 стран против в 2025 включая США» (UN press ga12736 + US Geneva Mission EOV).
- **Glossary §11 added** в chapter — 28 canonical terms RU+EN, lec-07 structural parity.

### Issues caught and fixed
- 43 → 35 slides cut (over-budget pacing)
- 0 → 17 real photos (no-mock-fallbacks rule)
- 107 → 0 anglicism patterns в speech spoken body (Russification)
- 2 P0 fact drift (Du→Ye + CENTCOM→EUCOM) — caught Phase 7 fact-checker, inherited from chapter
- s-08 stacked 3 issues (anglicism + ghost text + image quality)
- s-15 vendor density structural (SPLIT applied)
- s-27 «2024-2026» ghost text render artifact
- s-22 LO2 canonical case badge (didn't leak to render, source MD updated)
- §4.7 directional inversion (Russia outdated)
- Closing s34 promotional tail (course-scaffold leak)

### Residual P2 (defer-able, не блокеры)
- 4 anglicism в bracketed `[На слайде — ...]` stage directions (lecturer-only, not student-facing)
- Chapter Glossary §11 не имеет RU canonical column для 8 cross-cutting terms (ground truth/predictive maintenance/etc) — consistency-checker proposal, defer-able
- Replicator no dedicated slide (chapter+speech cover)
- $20B Anduril Lattice contract chapter-only
- source MD layout instructions в `## Visual` sections sometimes still mention outdated specs that designer overrode (suspended LO2 badge, §5.1 footer)

## Content patterns reusable

### Decision-axis OODA для отраслевых лекций
OODA (Sense → Decide → Act) — отлично ложится на любую decision-intensive отрасль. Phase 0 research evaluated 3 narrative axes (OODA / уровни автономии L1-L5 / dual-use). OODA победил по 5 критериям (familiarity / tools-per-taxonomy fit / strict-in natural distribution / Russian context fit / axis-boundary risk). Reusable для аналогичных decision-process отраслей (energy decisions, transport logistics, etc.).

### Glossary §11 lec-07-style
28 terms RU+EN canonical в **отдельной таблице** перед References. Структура: # | Канонический термин (RU) | Канонический термин (EN) | Определение. Group by AI fundamentals / Autonomy ladder / Tools / Failures. Lec-07 pattern proven.

### Russified body + brand-names exception
Anti-anglicism rule в visible body **с явными whitelisted exceptions** (brand names: Maxar/Anduril/Palantir, tech acronyms с RU расшифровкой: OODA/SAR/HITL). Speech-writer должен apply этого systematically — не ad-hoc.

### 6-tier image acquisition Tier 2 priority
Wikimedia REST API (Tier 2) — most reliable для CC-BY-SA real photos. Tier 1 og:image часто 404/429. Use Commons API `prop=imageinfo&iiurlwidth=960` thumbnails.

### Failure-block формат с явным уроком + альтернативой
Each canonical failure: что произошло → выученный урок → правильная альтернатива. Lavender / MCAS / ALIS — золотой эталон. Designer/speech-writer должен apply этот pattern systematically.
