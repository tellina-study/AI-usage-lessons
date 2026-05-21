# improvements.md — Лекция 9 production

Extracted actionable improvements from `tools.md` / `workflow.md` / `content.md` / `user-feedback.md`. Priority P0 (next session) / P1 (within 2 sessions) / P2 (deferred).

## P0 — Next session (before lec-10)

### I1 — Anonymization default in chapter brief
- **Target:** `tools/lecture-production/README.md` Phase 2 brief + `templates/lecture-outline.md` career section
- **Action:** Add mandate: «Career angle section MUST be anonymized — generic «профильные технические университеты + военно-космические академии» вместо named МГТУ/Бауман/ИУ/ВКА. Frontmatter audience generic «студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)».»
- **Effort:** S (edit 2 files)
- **Why P0:** User explicit correction at lec-09 cost 1 revision cycle (v2→v3). Repeatable mistake — prevent by default.

### I2 — Speech-writer mandatory anti-anglicism final scan
- **Target:** `.claude/agents/speech-writer.md` DoD checklist
- **Action:** Add «Before submission: run own regex grep на anti-anglicism blacklist (top 30 patterns from feedback_russification memory rule) on visible body — report ACTUAL hit count, not «0 hits» narrative.»
- **Effort:** S (edit 1 file)
- **Why P0:** Lec-09 speech v1 self-reported «0 hits» при 107 реальных. Massively inflated. Repeatable.

### I3 — Designer brief default media-rich metric definition
- **Target:** `.claude/agents/presentation-designer.md` + `tools/presentation-build/README.md`
- **Action:** Define media-rich strictly: «real photo (Wikimedia/NASA/CC) OR generated diagram (mermaid/drawio) OR chart (QuickChart) OR screenshot UI. NOT icons-in-boxes, NOT primitive shapes. Pre-render counter: list 18+ slides с specific media kind before render.»
- **Effort:** S (edit 1-2 files)
- **Why P0:** Lec-09 designer v1 self-reported 72% media-rich при 0 real photos (только primitives). Counterintuitive metric — fix definition.

### I4 — Full citation sweep на каждой chapter revision
- **Target:** `tools/lecture-production/README.md` Phase 4 brief + book-editor agent
- **Action:** Add «Phase 4 revision DoD: fact-checker re-runs **full citation sweep** (не subset) на revised chapter. Subset reruns acceptable только для targeted P0 verification, не Phase 4 closure.»
- **Effort:** S (edit 1-2 files)
- **Why P0:** Lec-09 chapter v3 had Du/CENTCOM P0 errors that Phase 4 subset rerun (UN LAWS only) missed. Found только на Phase 7 slides QA fact-checker.

## P1 — Within 2 sessions

### I5 — Designer-agent default включить `feedback_no_mock_fallbacks`
- **Target:** `.claude/agents/presentation-designer.md` opening checklist
- **Action:** Add mandatory pre-flight read: «Before media-heavy slide work, READ memory rule `feedback_no_mock_fallbacks` + execute 6-tier acquisition for each target hero slide.»
- **Effort:** S (edit 1 file)
- **Why P1:** Lec-09 v1 designer пропустил, потребовался orchestrator-driven v2 revision. Memory rule известен, но не embedded в default brief.

### I6 — Pre-USER-GATE skill auto-invoke
- **Target:** `.claude/skills/pre-user-gate/SKILL.md` + orchestrator habit
- **Action:** Document explicit trigger pattern: «Before presenting USER GATE X, MUST invoke `/pre-user-gate` skill — даже если manual walkthrough done.»
- **Effort:** S
- **Why P1:** Skill exists but используется неконсистентно. Lec-09 manual walkthroughs работали, но for compliance / репликации — auto-trigger лучше.

### I7 — API 529 retry pattern в Phase 7 critics
- **Target:** `tools/lecture-production/README.md` Phase 7 brief + critic agents
- **Action:** Document: «If critic returns 0 tool uses + API 529 error, defer retry 30+ min; не immediate retry. Третья попытка через ~1ч.»
- **Effort:** S
- **Why P1:** Lec-09 consistency-checker failed 2× back-to-back; 3-я retry через ~30 min recovery работал. Reusable pattern.

### I8 — feedback_hero_images compliance check для lec-09
- **Target:** Re-verify lec-09 s39 (7-criteria matrix table) vs «hero ≥40% площади» mandate
- **Action:** Open s39.png, measure hero element ratio. Если ниже 40%, follow-up polish issue.
- **Effort:** S
- **Why P1:** New memory rule, lec-09 may have non-compliance на s39 (matrix table вместо hero photo).

### I9 — Source MD `## Visual` sections may contain outdated layout specs
- **Target:** presentation-designer DoD + future revisions
- **Action:** «If layout spec was overridden in render (e.g. LO2 badge removed), book-editor / designer должен update source MD ## Visual section в same revision — не leave stale layout instructions.»
- **Effort:** S (process change)
- **Why P1:** Lec-09 source MD still says «Бейдж: LO2 canonical case (gold)» despite render fix. Future maintenance / re-render risks resurfacing leak.

### I10 — Speech-writer brief should include strict-in counter pre-submission
- **Target:** `.claude/agents/speech-writer.md` DoD
- **Action:** «Pre-submission: count failure-block words / total spoken words → strict-in %. Report distribution per section. Не submit if <30% holistic.»
- **Effort:** S
- **Why P1:** Lec-09 speech v1 reported 40.9%; v2 ended 81% — large variance suggests inconsistent counting. Standardize.

## P2 — Deferred

### I11 — Glossary RU canonical column expansion
- **Target:** Chapter Glossary §11 — add RU column for 8 cross-cutting terms (ground truth → эталонная разметка / predictive maintenance / multi-sensor fusion / automation bias / decision-support / pattern / anti-pattern / accuracy)
- **Effort:** M
- **Why P2:** Consistency-checker proposal. Lec-09 + future lectures could benefit. Defer to follow-up polish PR or batch update at lec-10/11 milestone.

### I12 — Memory rule `feedback_russification` should specify scope (visible body? stage directions? source MD?)
- **Target:** Memory file
- **Action:** Clarify: «Apply Russification к ALL visible-in-source text including bracketed stage directions, slide ## Visual specs, since lecturer / designer might read or copy from these.»
- **Effort:** S
- **Why P2:** Lec-09 speech v2 still has «gold callout» / «big-tech return» / «cost-asymmetry callout» в bracketed stage directions. Lecturer-facing only, но source MD readable by anyone.

### I13 — Build script (build_lec*.py) as another source-of-truth для slide text
- **Target:** `tools/presentation-build/README.md`
- **Action:** Document: «build scripts contain inline slide text — they ARE source of truth для actual render. Source MD slides/*.md must be kept synced with build script content.» Or alternative: minimize build script text content, source from slides/*.md programmatically.
- **Effort:** L (architectural)
- **Why P2:** Lec-09 had Du/CENTCOM in 4+ build script locations separate from chapter + slides. Triple source-of-truth = sync risk.

### I14 — Consistency-checker fallback when API 529
- **Target:** `tools/lecture-production/README.md` или `.claude/agents/consistency-checker.md`
- **Action:** «If 2 consecutive 529 — proceed to revision without consistency-checker; spawn retry on revised artifacts.»
- **Effort:** S
- **Why P2:** Lec-09 already applied this pattern ad-hoc. Document for replication.

## Linked existing GitHub issues

- #111 — Pipeline hardening (Lec 5 lesson, includes pre-gate re-verify) — partially covers I7 (retry patterns)
- #115 — Reflection Лекция 4 ENFORCED improvements — covers similar patterns

## New issues to create

- **I1+I2+I3+I4 — P0 group** can be one bundled hardening issue: «Lec 9 lessons: anonymization default + speech anti-anglicism scan + media-rich metric + full citation sweep»
- **I8 — feedback_hero_images compliance lec-09 s39** can be a tracking issue
- **I9 — Source MD layout sync** can be a process issue
