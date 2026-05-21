# Лекция 8 — рефлексия по workflow

**Дата:** 2026-05-21
**Лекция:** 8 «AI в креативных индустриях и медиа»

## Pipeline timing (actual vs planned)

| Phase | Plan | Actual | Notes |
|---|---|---|---|
| Phase 1 — Research + Plan | ~1 hour | ~45 min | Research agent 4406 слов dossier (8 min) + RU mini-research (3 min) + plan v1 (11 min) + plan v2 update (5 min) + critic pass (4 min) |
| Phase 2-3 — Chapter draft + critic | ~2 hours | ~75 min | Chapter v1 16 min + 3 critics parallel ~10 min each + batched revision v1→v2 11 min |
| Phase 4 — USER GATE A | gate | done на 1 try | Owner approve clean |
| Phase 5-7 — Deck design (initial) | ~3-5 hours | ~36 min | Designer v1 single agent, all 39 slides |
| Phase 7.5 — Deck critique | ~30 min | ~30 min | 3 critics parallel |
| Phase 6+7 batch revision | ~1 hour | ~24 min | 3 critics all REVISE → batched fix |
| **Phase 7+ image revision** | **owner-triggered** | **26 min** | After GATE B rejection — real image acquisition |
| **Phase 7+ Russification** | **owner-triggered** | **51 min** | Deep Russification after second rejection (died at API 529 после rebuild — все changes сохранены) |
| **Phase 7+ Hero images** | **owner-triggered** | **6 min** | After third request |
| Phase 8 — USER GATE B | gate | **3 tries** | v2 rejected (mocks + anglicisms), v3 rejected (no hero), v4 approved |
| Phase 9 — Speech draft | ~30-45 min | ~25 min | Single speech-writer agent |
| Phase 10 — Consistency + revisions | ~30 min | ~50 min | Consistency-checker + batched Phase 11 revision (4 P0 + 7 P1 + 5 P2) + speech russification rounds |
| Phase 11 — USER GATE C + merge | gate | done на 1 try | Owner approve clean |

**Total actual:** ~6 hours (vs ~9-10 hours plan baseline).

## What made pipeline faster than baseline

- **Worktree isolation** — параллельная работа с Лекцией 9 без conflicts
- **Single batched revision agent (Phase 11)** — вместо per-artifact spawns
- **3 critics параллельно** в Phase 3, 7.5 — independent reviews
- **6-tier image acquisition strategy** — explicit URLs per slide, 87.5% Tier 1 success
- **deck builder script** — bulk edits applicable через python-pptx

## What made pipeline slower than baseline

- **3 owner-feedback rounds на GATE B** = 3 extra revision passes (~83 min total)
- **Russification depth миssed by narrow grep** — required 2 revision passes (initial cleanup + deep cleanup)
- **API 529 server overload** — Russification agent died at 51 min (но rebuild уже completed, no work lost — luck)
- **Mock generation by lazy designer** — wasted 1 hour Phase 6+7 batch revision на mocks before real-image attempt

## Pipeline gaps that allowed owner-interventions

### Gap 1: No «is image real» check в Phase 7.5
3 critics в Phase 7.5 (presentation-critic, student-simulator, reader-simulator) **flag-нули placeholder issues** в их REVISE verdicts. But все 3 не различили «placeholder text card» vs «stylized mock с verbatim headline + Ocean palette». **Stylized mock looked enough «real» to pass critic visual review.**

**Insight:** Critics need an explicit check: «If this slide claims to show a screenshot/image from EXTERNAL SOURCE, can you identify the source page URL? Does the image visually match what the source page would show?» This catches mocks that say «BLOOMBERG LAW · DEC 2023» в Ocean palette card but не есть actual Bloomberg Law screenshot.

### Gap 2: Russification narrow grep не достаточен
Mой Russification verification использовал 32-pattern check from таблицы. Deep latin-token scan показал 919 unique tokens that narrow check missed.

**Insight:** для RU-language deck — deep latin-token scan обязателен, не только pattern grep.

### Gap 3: Hero check на s01/s39 не был в pre-GATE checklist
До owner feedback, я не проверял hero на s01/s39 — slides просто text-cards Ocean palette. После [[hero-images-required]] memory rule этот check добавлен, но не в общую infra (только memory).

**Insight:** pre-USER-GATE walkthrough должен включать hero check.

## Critic-feedback patterns

**3 critics в Phase 7.5 (presentation-critic + student-simulator + reader-simulator rendered) — все 3 returned REVISE.** Это правильный сигнал: deck v1 действительно imali serious issues (mocks + designer-extras leaks + Ocean palette violations + layout monotony + text overflow + typos). Critics did their job.

**Что они НЕ caught:**
- «Mock vs real image» distinction (см. Gap 1)
- Russification depth (deep latin-token scan не в critic checklist)
- Hero на s01/s39 (не в critic checklist до [[hero-images-required]])

**После updates infra (этот PR) — critics получают expanded checklists, поэтому 3 owner-интервенции не повторятся automatically.**

## Memory rules created (3 ENFORCED)

1. **[[no-mock-fallbacks]]** — 6-tier real image acquisition mandatory
2. **[[russification]]** — anti-anglicism mandate в каждом producer prompt + post-rebuild deep grep
3. **[[hero-images-required]]** — hero иллюстрации на s01 + s39 для всех deck'ов курса

## Lessons applicable вне Лекции 8

### Subagent trust calibration
Self-reports от subagents требуют orchestrator-independent verification. Pattern:
- Subagent claims «N hits на X check» → orchestrator runs broader version of same check
- Subagent claims «media coverage Y%» → orchestrator visually verifies sample
- Subagent claims «all P0 fixed» → orchestrator spot-checks 2-3 P0 specifically

Не недоверие — calibration. Subagent context is limited; orchestrator integrates across artifacts.

### Producer-agent prompts must explicitly enforce
Implicit rules «high quality», «professional» — не работают. Producer agents в default mode produce «functionally correct but mediocre». Explicit rules with measurable acceptance criteria — работают:
- «≥80% slides with media» — measurable, designer optimizes
- «0 anglicism hits на deep latin-token scan» — measurable, agent optimizes
- «hero on s01/s39 ≥40% area» — measurable, designer optimizes

Inject mandates в prompt template, не оставлять на judgment.

### USER GATE walkthrough must be ENFORCING
Pre-USER-GATE walkthrough — последний line of defense. Если skip walkthrough → owner ловит в GATE → revision required. Cost of walkthrough = 15-30 min orchestrator time; cost of skipped walkthrough = 1-3 hours revision cycle.

Pre-GATE checklist должен быть exhaustive по learned issues — каждая past owner intervention становится pre-GATE check.
