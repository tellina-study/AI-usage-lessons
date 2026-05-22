# Improvements — Лекция 10 production retrospective

**Дата:** 2026-05-21. **Source files:** `tools.md`, `workflow.md`, `content.md`, `user-feedback.md` в этой папке.

Extract actionable items only. No observations без actions.

---

### 1. Pre-USER-GATE B/C preflight grep script (automation)

- **Priority:** P2 (do this month)
- **Effort:** S (< 30 min)
- **Component:** `tools/presentation-build/preflight_grep.py` (новый script)
- **Action:** написать one-shot bash/python script, который запускает orchestrator-INDEPENDENT broad regex grep на 3 группах patterns (scaffold + timing + methodology) + baseline coverage sample на 5-7 measurable claims в rendered PPTX visible body + speaker_notes + chapter visible. Output: structured report «N hits per group». Goal: снизить manual grep cognitive load для Pre-USER-GATE walkthrough.
- **GitHub issue:** create (рекомендую label: infrastructure)

### 2. Post-Phase-5 sub-ID renumbering check

- **Priority:** P3 (backlog)
- **Effort:** S
- **Component:** `tools/presentation-build/README.md` § 5 (presentation-designer guidance)
- **Action:** добавить guidance — если presentation-designer на Phase 5 создаёт sub-IDs (sNN-b, sNN-s, sNN-c), orchestrator должен **renumber to sequential** перед Phase 6 rendering. lec-10 v1: s30b/s37s/s38s/s35c/s36c — non-sequential, путало Phase 7 critics (presentation-critic uses pptx index 1-43, consistency-checker — slide_id с sub-IDs). Sequential renumbering предотвращает mapping confusion.
- **GitHub issue:** create

### 3. Tier 1 og:image fetch — investigate playwright/chromium для JS-rendered pages

- **Priority:** P3 (backlog)
- **Effort:** M
- **Component:** `tools/presentation-build/` image-acquisition helpers
- **Action:** Phase 6 fetched 0/6 Tier 1 og:images (TechCrunch / Deere / BASF / Carbon Robotics / Merck / Monarch — все JS-rendered/paywalled). Все 32 photos через Tier 2 Wikimedia fallback. Investigate playwright или chromium headless для JS-rendered og:image extraction. Это улучшит real-image acquisition rate для всех future lectures.
- **GitHub issue:** create

### 4. Self-report inflation detection metric

- **Priority:** P2 (do this month)
- **Effort:** S
- **Component:** `.claude/agents/presentation-designer.md` + `.claude/agents/speech-writer.md`
- **Action:** Phase 6 designer self-report 66 anglicism candidates → independent 84 (27% inflation). Phase 9 speech 2 → independent 43. **Pattern:** subagent self-grep систематически underestimates. Recommend explicit prompt в agent definitions: «при self-grep на anglicism / designer-extras, использовать **broad regex** (любое латин-слово ≥4 chars вне whitelist), не pattern-narrow grep. Self-report ≥30 false-negative — known failure mode.»
- **GitHub issue:** create

### 5. RAG ingest для finalized chapter v3.3

- **Priority:** P2
- **Effort:** S
- **Component:** `mcp-local-rag` + `catalog/manifests/lectures.yaml`
- **Action:** ingest `library/lectures/lec-10/chapter.md` + part2/part3 через `mcp-local-rag ingest_file`. Update manifest `rag_indexed: true`. Это improves future cross-lecture queries (e.g., «найди все mentions vendor lock-in across L4-L10»).
- **GitHub issue:** create

### 6. Cascade-tracking автоматизация: chapter ↔ slides ↔ speech number-drift detector

- **Priority:** P2
- **Effort:** M (1-3h)
- **Component:** `tools/lecture-production/` cascade-check helper
- **Action:** Phase 11 нашёл 3 drift cases (Cognitive Pilot 1200 в chapter vs 1700+ в slides; Tzachor дата; Bowery $500M speech vs $700M chapter). Write helper script: для каждой measurable claim в chapter, find same claim в slides + speech (через cross-reference search) и flag if numbers different. Это complementary к consistency-checker agent.
- **GitHub issue:** create

### 7. Vendor image alternative acquisition path: try Wayback machine archived og:images для JS-rendered vendor pages

- **Priority:** P3
- **Effort:** M
- **Component:** image-acquisition Tier 4 (Wayback)
- **Action:** Tier 4 в plan-v2 был «Wayback machine» но не использовался Phase 6 (Tier 1 failed → jumped to Tier 2 Wikimedia). Pattern для future: Tier 1 og:image failed → **always try Tier 4 Wayback before Tier 2 Wikimedia** (Wayback может иметь archived og:image от earlier crawl). Update agent guidance.
- **GitHub issue:** create

### 8. Лекция 12+ production: apply 2 NEW ENFORCED rules from start

- **Priority:** P0 (do now — affects active lec-12/13/14 production)
- **Effort:** S
- **Component:** open issues for lec-12/13/14 (`/tmp/lec-12-wt`, `/tmp/lec-13-wt`, `/tmp/lec-14-wt` worktrees exist)
- **Action:** **No Timing / No Methodology in Slides** + **Baseline / Counterfactual Mandate** уже в CLAUDE.md (PR #136 merged) + memory files updated. Pre-USER-GATE Walkthrough Rule §5 + точка 12 расширены. **Verify active lec-12/13/14 production picks up rules** — orchestrators worktree уже на ветке от main commit `816e4db` (post-PR-#136), значит rules applied. Spot-check pre-USER-GATE walkthrough для каждой active лекции с новыми grep patterns.
- **GitHub issue:** create (или comment на existing lec-12/13/14 issues)

### 9. Phase 5 slide-budget tighter bound

- **Priority:** P3
- **Effort:** S
- **Component:** `.claude/agents/presentation-designer.md` Phase 5 brief template
- **Action:** lec-10 spawned 43 slides (target 33-37 в plan-v2 — overflow +6). Pattern: presentation-designer склонен add sub-IDs для content density. Recommend explicit ceiling «slide count ≤ plan target + 2; если больше — consolidate sub-slides ИЛИ request orchestrator approval». 43 slides × 1.74 min/slide = tight для 75 min content.
- **GitHub issue:** create

---

## Summary

9 improvements identified:
- **1 P0** (apply 2 NEW ENFORCED rules to lec-12/13/14 active production — affects 3 in-flight lectures)
- **4 P2** (preflight grep script automation + self-report inflation detection + RAG ingest + cascade-tracking detector)
- **4 P3** (sub-ID renumbering check + Tier 1 og:image playwright + Wayback Tier 4 pattern + slide-budget tighter bound)

P0 + P2 = create GitHub issues (per reflection-process.md). P3 = backlog (no immediate issue).
