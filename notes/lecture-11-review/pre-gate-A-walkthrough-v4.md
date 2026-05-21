# Pre-USER-GATE A walkthrough — Лекция 11, mode=chapter (v4)

**Дата:** 2026-05-21
**Branch:** issue-127-lec-11-manufacturing
**Target:** `library/lectures/lec-11/chapter.md` (commit 45bd1cc, 30 499 слов / 1438 строк, status: reviewed, version: v4)

## Summary
- Total checks: 16
- Passed: 15
- P0 issues: **1** (multi-part split — см. Block H, conditional на новое правило)
- P1 issues: **0**
- P2 polish: **2** (minor)

## Step 0 — Self-reported metric re-verification (ENFORCED)

| Метрика | Producer self-report (v4) | Orchestrator independent verify | Status |
|---|---|---|---|
| Word count | 30 499 (target 30k ±5%) | **30 499** (wc -w) | ✓ match, exact 30k target hit |
| Russification narrative anglicism (post-sweep) | «All in whitelist» | **Suspect tokens deep scan:** production×4 (Musk quote-gloss + Optimus inline + sources) / automation×9 (Musk quotes ×2 verbatim + Bainbridge 4 ironies English originals as inline gloss + Tesla «automation, automation, automation» quote + sources) / mistake×5 (Musk quote variants + sources) / manufacturing×6 (Industrial Foundation Model brand + sources) / controller×2, vision×3, rules-based×2 (all canonical с inline gloss) | ✓ all hits in whitelist (direct quotes / source titles / inline glosses with RU canonical) |
| `[FACT-CHECK]` markers | 0 | **0** (grep) | ✓ match |
| `[VFY-day-of]` markers | 33 (v3 preserved) | grep — adequate volatile-claim coverage | ✓ |
| Failure-bucket strict-in | ≥75-80% chapter words preserved | sample 5 параграфов из новых polish areas — strict-in preserved | ✓ comfortably ≥30% mandate |
| Version | v4 | frontmatter line 6: `version: v4` | ✓ |
| Status | reviewed | frontmatter line 4: `status: reviewed` | ✓ |
| References count | 105 | frontmatter line 16: `references_count: 105` | ✓ |

**Authoritative re-verification:** Russification was P1 critical in v3 critique (101 anglicism hits); post-sweep deep scan confirms all remaining tokens in legitimate whitelist (quotes / source titles / inline glosses). No focused critic re-spawn needed.

## Step 1-3 — N/A (slides mode)

## Step 4-6 — N/A (chapter mode, not final)

## Chapter-specific checks

### P0 fact fixes from v3 critique (all 3 — verified closed in v4)
- ✓ **P0-1 §3.5 duplicate paragraphs** — deduped (СИБУР appears once now, no verbatim copies).
- ✓ **P0-2 §4.4 ↔ §4.5 swapped** — body matches TOC: §4.4 (5-step framework) line 1064 → §4.5 (failure-pattern matrix) line 1078.
- ✓ **P0-3 §2.4 Toyoda 1924 → 1925** — «1924 — патенты Type-G; 1925 — собран в металле» (line 443).

### P1 fixes from v3 critique (11 actionable — all closed; 1 rejected per synthesis)
- ✓ **P1-1 Russification deep sweep** — initial 101 hits / 7 hot zones; post-revision all in whitelist (deep latin-token scan confirmed by orchestrator).
- ✓ **P1-3 typo «глаz»** — fixed (0 hits).
- ✓ **P1-4 recursive parens** — fixed (0 hits).
- ✓ **P1-5 Q11 CFO ROI rewrite** — «Как измерить OEE до и после AI-внедрения, чтобы получить честный baseline?» (engineering-side, OEE formula + Hawthorne effect detection).
- ✓ **P1-6 Edge Tier 1-4 RU subheaders** — «Уровень 1-4» в §3.3 (lines 697-700).
- ✓ **P1-7 §3.4 FDA warning letters generalize** — «иллюстративные паттерны предписаний без атрибуции к конкретным компаниям» (lines 740-745).
- ✓ **P1-8 §1.3 IBM Watson $5B → $4B** — «свыше 4 миллиардов» (lines 88, 234, 242).
- ✓ **P1-9 §2.4 GM Hamtramck 1985-1990** — «(1985-1990)» + Роджер Смит август 1990 (line 449).
- ✓ **P1-10 §1.2 FoxBrain distillation** — «обучен на основе Llama 3.1 70B методом дистилляции; в сравнении с дистилляционной моделью DeepSeek» (line 202).
- ✓ **P1-11 §1.3 Tesla Optimus «сотни» soften** — «пилотные развёртывания на площадках Tesla, точное количество не раскрывается, полное промышленное масштабирование отложено до V3 reveal late 2026» с `[VFY-day-of]` (line 256).
- ✓ **P1-12 §1.2 Honeywell MRO generalize** — «отраслевые игроки (Honeywell, GE Aerospace, Rockwell) обсуждают дорожные карты MRO copilots; production-deployed examples не подтверждены» (lines 206, 208).
- ❌ **P1-2 worked examples asymmetric** — rejected per synthesis rationale; keep 2 pass (Pfizer + brewery) + 1 fail (avionics).

### P2 fixes applied (6 of 13)
- ✓ §2.4 Tesla Shanghai: «декабрь 2019 — январь 2020».
- ✓ §2.1 TSMC abstain rate: «типичные AOI-линии полупроводникового производства».
- ✓ §3.4 Pepperl+Fuchs: «VisuNet / BPC3200» ATEX-certified.
- ✓ §2.1 BAAL: «ServiceNow AI Research, ex-Element AI».
- ✓ §1.3 IBM Watson MSKCC: «MSKCC впоследствии заявила, что эти случаи были частью system testing».
- ✓ §3.6 RL drift detection RU terminology + ALIS Russified.

### Anonymization (ENFORCED §3.7a)
- ✓ **0 named institutions** (grep МГТУ|Бауман|ИУ-?[0-9]|Кафедра|МАИ|СПбГУ|МФТИ|ВКА = 0). Russian companies (Норникель / СИБУР / ММК / Северсталь / КАМАЗ) — это corporate brands, permitted.

### Keystone consistency
- ✓ §0.1 «Keystone: две модели производства» — заголовок и 1-я строка про саму ось (Discrete vs Process), не cram-three-things.
- ✓ Belt: единый anchor (пилотное застревание + McKinsey 78%/5,5% + MIT 95%).
- ✓ §5 closure: callback к keystone в финале.

### Cornerstone consistency
- ✓ 10 cornerstones unified, drift variants = 0 (chapter v2 baseline preserved).

### Sample reading (3 sections after polish)
- ✓ §1.3 Tesla Optimus narrative (post-Russification sweep) — reads cleanly, Musk quotes preserved verbatim with English original + Russian gloss.
- ✓ §2.4 GM Hamtramck (1985-1990) + Toyoda 1925 — historical anchors aligned.
- ✓ §4.4 5-step framework (now correctly preceding §4.5 matrix) — payoff sequence correct.

### Q&A backup quality
- ✓ 14 questions (8 + 6 new), Q11 rewritten to engineering. All actionable answers.

## Block H — Multi-part split observation (CONDITIONAL P0)

**Issue:** chapter v4 = **1438 строк**. Превышает:
1. CLAUDE.md «Document Size Limit» (≤600 строк per file).
2. NEW «Chapter Depth Baseline» rule в PR #129 (multi-part split mandatory >600 строк).

**Context:**
- lec-08 chapter: 907 строк (single-file, merged).
- lec-09 chapter: 994 строки (single-file, merged).
- lec-11 v4: 1438 строк (1.4× больше lec-09).

**Decision:** **DEFER to owner**. Это новое правило (PR #129 ещё не merged); existing course precedent (lec-08/09) — single-file. Если owner хочет precedent-set для PR #129 → split now (~30-40 мин book-editor work). Иначе defer.

**Options:**
- A. **Approve v4 as single-file** (precedent matches lec-08/lec-09).
- B. **Apply multi-part split** (set precedent для PR #129 enforcement).

## P2 polish (cosmetic, non-blocking)

1. **§1.3 Tesla Optimus** — text mentions «дискретный контр-паттерн к Foxconn Wisconsin» — sentence could be one-clearance shorter, currently reads dense. **Non-blocking.**
2. **§2.4 Tesla 2018 + GM Hamtramck cross-reference** — appears trice (line 449 §2.4, line 149 §1.1) — fine if intentional (two angles). **Non-blocking.**

## Recommendation

- [X] **PRESENT USER GATE A** (no P0/P1 blockers remaining from v3 critique; multi-part split is conditional and decided by owner).
- [ ] FIX FIRST (only если owner выбирает multi-part split в Block H).

Chapter v4 ready for owner approval. Two paths:
- **Path A:** approve as single-file → proceed to Phase 5 (slides update from chapter).
- **Path B:** apply multi-part split first → spawn book-editor split → re-run pre-gate → present GATE A.
