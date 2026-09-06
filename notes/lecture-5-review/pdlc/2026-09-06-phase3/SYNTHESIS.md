# Phase 3 critique — SYNTHESIS (chapter v1, Лекция 5 PDLC)

**Date:** 2026-09-06 · **Artifact:** `library/lectures/lec-05/chapter{,-part2,-part3,-part4}.md` (29,783 wc-raw)

## Verdicts
| Critic | Verdict |
|---|---|
| methodology-critic | **REVISE** (2× P0) |
| fact-checker | **APPROVE-CLEAN** |
| reader-text-only | **APPROVE-WITH-POLISH** (4 items) |

**Net: REVISE** — methodology P0 governs. Structure/keystone/LO/fact-integrity/baselines all confirmed strong → preserve; fixes are word-count + Part-1 strict-in rebalance + reader polish. One batched book-editor revision.

## P0 (methodology — BLOCKING)
- **P0-1 Word count.** 27,843 content words (excl. frontmatter/glossary/sources per CLAUDE.md count) < 28,500 floor. → **+~2,500–3,500 слов** до ≥30k content (запас над floor; plan declared ~31k).
- **P0-2 Strict-in 28.3% < 30%, Part 1 = 16.1%** (single-part concentration counter-check). → поднять holistic ≥33% и **каждую часть ≥30%**, Part 1 — приоритет.

## Fixes (batched into one revision)
1. **[P0-2 + P0-1] Р1 Discovery: добавить ТРЕТИЙ on-point провал полным блоком ≥600 слов — IBM Watson for Oncology** (обучен на синтетических кейсах MSK, не реальных пациентах; $62M; 0 пролеченных; discovery/research-data провал — ровно фаза Discovery). Урок+критерий+альтернатива+«когда НЕ AI-first» ≥80 слов. Это чинит и Part-1 strict-in, и часть word-count.
2. **[P0-2] Углубить §1.7/§1.8** (ограничения+что оставить в Discovery) на ~200–300 слов (in-bucket судебная часть — критерии «когда живое интервью > AI»).
3. **[P0-1] Догнать word-count** равномерным углублением тонких мест (не filler): §0 payoff, §3 (Build limits), §4 (evals), §6 (governance argument) — по мере правок ниже.
4. **[reader] §4.2 experiment-traps:** 8 терминов сгруппировать явно в 3 суб-кластера (до теста / интерпретация / эффект) с мини-recap; не плоский список.
5. **[reader] §6.2 Governance:** 5-source stat-list (Deloitte/Sber/Gartner/McKinsey/Forrester) свести в АРГУМЕНТ (тезис→2-3 цифры в подтверждение), не перечисление.
6. **[reader] Strong-half callout-боксы** (§3.2 feature flags/canary, §5.1 SLI/SLO) переставить ПЕРЕД базовыми определениями («вы это знаете — вот отличие»), не после.
7. **[reader] DEFECT: убрать протёкшую авторскую пометку** «re-homed from Build/Measure» в §5.4 (Zillow) — переформулировать с точки зрения читателя.
8. **[fact-checker minor] «$300M button»** дата 2011 → «конец 2000-х (≈2009), многократно ре-синдицирован» (не влияет на суть).
9. **[frontmatter] Обновить** `length_words` и `strict_in_self_estimate` честно после правок.

## Preserve as-is (не трогать)
Структура base→AI→limits→failure (все 6 фаз), keystone §0, LO1/2/3/6 (вкл. LO3 data-security блоки), baseline-дисциплина (10/10 sampled с знаменателем), все 6 fact-integrity корректировок.

## Re-verify после правок
Orchestrator-независимый recount по словам: total content ≥30k; каждая часть strict-in ≥30% (Part 1 — обязательно); grep «re-homed»/authoring-notes = 0.
